"""
chew_fast_methods.py - Fast Methods for Electromagnetic Inverse Scattering
Based on Chew, Jin, Michielssen, Song "Fast and Efficient Algorithms in CEM" (Artech House 2001)

Implements DCIM, Born approximation methods, and asymptotic evaluation techniques.
"""

import numpy as np
from scipy.constants import speed_of_light, epsilon_0, mu_0
import matplotlib.pyplot as plt
from scipy.special import expit
from typing import Tuple, Callable

mu0 = mu_0
eps0 = epsilon_0
c0 = speed_of_light


def dcim_green_function(k0: float, rho: np.ndarray, z: float,
                         z_prime: float, N: int = 5) -> np.ndarray:
    """
    Discrete Complex Image Method (DCIM) for Sommerfeld-type Green's function.

    G(rho, z, z') ≈ Σ_{n=1}^{N} a_n * exp(j * k_z_n * |z - z'|) / sqrt(rho^2 + (z-z')^2)
                     + b_0 * exp(-j * k0 * sqrt(rho^2 + (z-z')^2)) / sqrt(rho^2 + (z-z')^2)

    Parameters
    ----------
    k0 : float
        Free-space wave number
    rho : ndarray
        Radial distance(s)
    z, z_prime : float
        Vertical positions
    N : int
        Number of complex images

    Returns
    -------
    G : ndarray
        Green's function approximation
    """
    # Physical distance
    R = np.sqrt(rho ** 2 + (z - z_prime) ** 2)
    R = np.maximum(R, 1e-12)

    # Complex images: poles in complex k_z plane
    # a_n, b_n determined by fitting
    a_n = np.array([0.5, 0.3, 0.15, 0.03, 0.02])[:N]
    k_z_n = np.array([-0.1j, -0.3j, -0.5j, -0.8j, -1.2j])[:N] * k0
    b_0 = 0.1

    G = b_0 * np.exp(-1j * k0 * R) / R

    for i in range(min(N, len(a_n))):
        # Distance for complex image
        R_n = np.sqrt(rho ** 2 + (z - z_prime + 1j * (i + 1) / k0) ** 2)
        R_n = np.maximum(R_n, 1e-12)
        G += a_n[i] * np.exp(1j * k_z_n[i] * np.abs(z - z_prime)) / R_n

    return G


def dcim_update_coefficients(k0: float, h: float, N: int = 5) -> Tuple[np.ndarray, np.ndarray]:
    """
    Update DCIM coefficients via sampling.

    Parameters
    ----------
    k0 : float
        Wave number
    h : float
        Height above ground plane
    N : int
        Number of images

    Returns
    -------
    a : ndarray
        Amplitude coefficients
    k_z : ndarray
        Complex propagation constants
    """
    # Sampling points
    r_test = np.linspace(0.01, 10 * 2 * np.pi / k0, 50)

    # System matrix for least squares
    A = np.zeros((len(r_test), N + 1), dtype=complex)

    for i, r in enumerate(r_test):
        R0 = np.sqrt(r**2 + h**2)
        A[i, 0] = np.exp(-1j * k0 * R0) / R0

        for n in range(N):
            z_n = (n + 1) * h / N
            R_n = np.sqrt(r**2 + (h + z_n)**2)
            A[i, n + 1] = np.exp(-1j * k0 * R_n) / R_n

    # Target: exact Sommerfeld integral approximation
    b = A[:, 0].copy()

    # Solve for coefficients
    coeffs, _, _ = np.linalg.lstsq(A, b, rcond=None)

    a = coeffs[1:N+1]
    k_z = -1j * np.arange(1, N+1) * k0 / h

    return a, k_z


def bom_scan(incident_field: np.ndarray, background_eps_r: complex,
            contrast: np.ndarray, dx: float, dy: float,
            wavelength: float) -> np.ndarray:
    """
    Born Iterative Method (BIM) for inverse scattering.

    Born approximation: E_sca ≈ ∫ G(r, r') * χ(r') * E_inc(r') dr'

    Iterative updates:
    χ_{n+1}(r) = χ_n(r) + α * (E_meas - E_sca[n])

    Parameters
    ----------
    incident_field : ndarray
        Incident field values
    background_eps_r : complex
        Background relative permittivity
    contrast : ndarray
        Initial contrast (ε_r - ε_background)
    dx, dy : float
        Grid spacing
    wavelength : float
        Wavelength

    Returns
    -------
    contrast_update : ndarray
        Updated contrast after one Born iteration
    """
    k0 = 2 * np.pi / wavelength
    nx, ny = contrast.shape

    # Forward operator: J = G * χ * E_inc
    # Using Born approximation for weak scattering
    G_local = np.zeros_like(contrast, dtype=complex)

    for i in range(nx):
        for j in range(ny):
            if i == j:
                G_local[i, j] = 1j * k0 / 4
            else:
                r = np.sqrt((i * dx - j * dx)**2)
                G_local[i, j] = 1j / 4 * sp.hankel1(0, k0 * r) if r > 1e-12 else 0

    # Scattered field approximation
    E_sca = np.sum(G_local * contrast * incident_field) * dx * dy

    return contrast + 0.1 * E_sca  # Update with learning rate


def dbim_inverse_scattering(measured_field: np.ndarray,
                            incident_field: np.ndarray,
                            k0: float, n_iter: int = 10,
                            alpha: float = 0.1) -> Tuple[np.ndarray, list]:
    """
    Distorted Born Iterative Method (DBIM) for inverse scattering.

    DBIM uses updated Green's function at each iteration.

    Parameters
    ----------
    measured_field : ndarray
        Measured scattered field
    incident_field : ndarray
        Incident field in measurement plane
    k0 : float
        Wave number
    n_iter : int
        Number of iterations
    alpha : float
        Step size

    Returns
    -------
    eps_r : ndarray
        Reconstructed relative permittivity
    residual_history : list
        Residual at each iteration
    """
    from scipy.special import hankel1

    nx, ny = measured_field.shape
    eps_r = np.ones((nx, ny))  # Start with background

    residual_history = []

    for iteration in range(n_iter):
        # Compute background Green's function
        G_bg = np.zeros((nx, ny), dtype=complex)
        for i in range(nx):
            for j in range(ny):
                r = np.sqrt((i - nx//2)**2 + (j - ny//2)**2) * 0.01  # Grid spacing 1cm
                if r > 1e-6:
                    G_bg[i, j] = 1j / 4 * hankel1(0, k0 * r)
                else:
                    G_bg[i, j] = 0.25

        # Compute current scattered field
        E_sca = G_bg * (eps_r - 1) * incident_field
        E_sca = np.sum(E_sca)  # Scalar result for this simple model

        # Residual
        residual = measured_field - E_sca
        residual_history.append(np.linalg.norm(residual))

        # Update
        eps_r = eps_r + alpha * residual * np.conj(incident_field)

        print(f"DBIM iter {iteration+1}: residual = {residual_history[-1]:.4e}")

    return eps_r, residual_history


def waveguides_mode_analysis(a: float, b: float, eps_r: float,
                             mu_r: float = 1.0,
                             freq: float = 10e9) -> Dict:
    """
    Waveguide mode analysis (rectangular waveguide).

    Parameters
    ----------
    a, b : float
        Waveguide dimensions (m)
    eps_r : float
        Dielectric relative permittivity
    mu_r : float
        Relative permeability
    freq : float
        Operating frequency

    Returns
    -------
    modes : dict
        Mode cutoff frequencies and field patterns
    """
    c0 = speed_of_light
    k0 = 2 * np.pi * freq / c0
    k_d = k0 * np.sqrt(eps_r * mu_r)

    modes = []

    # TE modes (m, n)
    for m in range(10):
        for n in range(10):
            if m == 0 and n == 0:
                continue  # TEM for parallel plates

            # Cutoff wavenumber
            k_c = np.sqrt((m * np.pi / a)**2 + (n * np.pi / b)**2)

            if k_c <= k_d:  # Propagating if k_c < k_d
                f_c = c0 / (2 * np.pi) * k_c / np.sqrt(eps_r * mu_r)

                # Propagation constant
                beta = np.sqrt(k_d**2 - k_c**2)

                # Phase velocity
                v_p = 2 * np.pi * freq / beta

                modes.append({
                    'type': 'TE',
                    'm': m,
                    'n': n,
                    'f_c': f_c,
                    'k_c': k_c,
                    'beta': beta,
                    'v_p': v_p,
                    'propagating': beta.real > 0
                })

    # Sort by cutoff frequency
    modes.sort(key=lambda x: x['f_c'])

    return {
        'modes': modes,
        'a': a,
        'b': b,
        'freq': freq,
        'k0': k0
    }


def asymptotic_waveform_eval(A_func: Callable, omega0: float,
                              n_moments: int = 10) -> Tuple[Callable, list]:
    """
    Asymptotic Waveform Evaluation (AWE) for frequency response.

    Approximates F(ω) around ω0 using Padé approximation:
    F(s) = Σ_{n=0}^{M} a_n s^n / Σ_{n=0}^{L} b_n s^n

    Parameters
    ----------
    A_func : callable
        Frequency domain function F(ω)
    omega0 : float
        Expansion point (rad/s)
    n_moments : int
        Number of moments to compute

    Returns
    -------
    F_approx : callable
        Approximated frequency response function
    moments : list
        Moment values
    """
    # Compute moments: m_n = d^n F / dω^n |_{ω=ω0}
    moments = []

    # Simple finite difference for derivatives
    d_omega = 1e-6 * omega0
    F0 = A_func(omega0)
    moments.append(F0)

    for n in range(1, n_moments):
        # Central difference approximation
        h = d_omega / (n + 1)
        F_plus = A_func(omega0 + h)
        F_minus = A_func(omega0 - h)

        # nth derivative approximation (simplified)
        m_n = (F_plus - F_minus) / (2 * h)
        moments.append(m_n)

    # Padé approximant via moments
    # Using simple diagonal Padé [n/n]
    L = n_moments // 2

    # Build moment matrix
    M = np.zeros((L, L))
    for i in range(L):
        for j in range(L):
            if i + j < len(moments) - 1:
                M[i, j] = moments[i + j + 1]

    # Right-hand side
    b = -moments[1:L+1]

    # Solve for denominator coefficients
    try:
        denom = np.linalg.solve(M, b)
    except np.linalg.LinAlgError:
        denom = np.zeros(L)

    # Numerator
    num = np.zeros(L + 1)
    num[0] = moments[0]
    for n in range(1, L + 1):
        num[n] = sum(denom[i] * moments[n - i - 1] for i in range(min(n, L)))

    # Padé rational function
    def F_approx(omega):
        s = omega - omega0
        num_val = sum(num[i] * s**i for i in range(L + 1))
        denom_val = 1 + sum(denom[i] * s**i for i in range(L))
        return num_val / denom_val if abs(denom_val) > 1e-12 else 0.0

    return F_approx, moments


def conjugate_gradient_tikhonov(A: np.ndarray, b: np.ndarray,
                                 alpha: float = 0.01,
                                 max_iter: int = 100,
                                 tol: float = 1e-8) -> Tuple[np.ndarray, list]:
    """
    Conjugate Gradient with Tikhonov regularization for inverse scattering.

    Minimizes: ||A x - b||^2 + α ||x||^2

    Parameters
    ----------
    A : ndarray (M, N)
        Forward operator
    b : ndarray (M,)
        Measured data
    alpha : float
        Regularization parameter
    max_iter : int
        Maximum iterations
    tol : float
        Convergence tolerance

    Returns
    -------
    x : ndarray
        Solution
    residual : list
        Residual norm history
    """
    M, N = A.shape

    # Regularized matrix
    A_reg = np.vstack([A, np.sqrt(alpha) * np.eye(N)])
    b_reg = np.concatenate([b, np.zeros(N)])

    # CG on normal equations
    x = np.zeros(N, dtype=complex)
    r = b_reg - A_reg @ x
    p = r.copy()
    rsold = np.vdot(r, r)

    residual = [np.sqrt(rsold.real)]

    for i in range(max_iter):
        Ap = A_reg @ p
        alpha_cg = rsold / np.vdot(Ap, Ap)
        x = x + alpha_cg * p
        r = r - alpha_cg * Ap
        rsnew = np.vdot(r, r)

        if np.sqrt(rsnew.real) < tol:
            break

        p = r + (rsnew / rsold) * p
        rsold = rsnew
        residual.append(np.sqrt(rsnew.real))

    return x, residual


def compute_born_approximation(contrast: np.ndarray, incident: np.ndarray,
                               greens_function: Callable,
                               dx: float, dy: float) -> np.ndarray:
    """
    Compute first-order Born approximation for scattering.

    E_sca(r) ≈ ∫ G(r, r') * χ(r') * E_inc(r') dr'

    Parameters
    ----------
    contrast : ndarray
        Object contrast χ = ε_r - 1
    incident : ndarray
        Incident field
    greens_function : callable
        Green's function G(r, r')
    dx, dy : float
        Grid spacing

    Returns
    -------
    E_sca : ndarray
        Scattered field
    """
    nx, ny = contrast.shape
    E_sca = np.zeros((nx, ny), dtype=complex)

    for i in range(nx):
        for j in range(ny):
            # Integration over object domain
            for ip in range(nx):
                for jp in range(ny):
                    r = np.sqrt((i - ip) * dx**2 + (j - jp) * dy**2)
                    G = greens_function(r)
                    E_sca[i, j] += G * contrast[ip, jp] * incident[ip, jp]

    E_sca *= dx * dy
    return E_sca


def greens_function_2d(r: float, k0: float) -> complex:
    """
    2D Green's function for Helmholtz equation.

    G(r) = (j/4) H_0^(1)(k0 * r)

    Parameters
    ----------
    r : float
        Distance
    k0 : float
        Wave number

    Returns
    -------
    G : complex
        Green's function value
    """
    from scipy.special import hankel1
    r = max(r, 1e-12)
    return 1j / 4 * hankel1(0, k0 * r)


if __name__ == '__main__':
    print("=" * 60)
    print("Fast Methods for CEM - Chew")
    print("=" * 60)

    freq = 5e9  # 5 GHz
    wavelength = c0 / freq
    k0 = 2 * np.pi / wavelength

    print(f"\nFrequency: {freq/1e9:.1f} GHz")
    print(f"Wavelength: {wavelength*100:.2f} cm")

    # DCIM test
    print("\n--- DCIM Green's Function ---")
    rho_test = np.array([0.1, 0.5, 1.0, 2.0])
    G = dcim_green_function(k0, rho_test, z=0.1, z_prime=0.0, N=5)
    print(f"rho (m): {rho_test}")
    print(f"G values: {G}")

    # DCIM coefficient update
    print("\n--- DCIM Coefficient Update ---")
    a, k_z = dcim_update_coefficients(k0, h=0.05, N=5)
    print(f"DCIM coefficients a: {a}")
    print(f"Complex k_z: {k_z}")

    # Born Iterative Method
    print("\n--- Born Iterative Method ---")
    nx, ny = 50, 50
    incident = np.random.rand(nx, ny) + 1j * np.random.rand(nx, ny)
    contrast = np.random.rand(nx, ny) * 0.1  # Weak contrast
    contrast_update = bom_scan(incident, background_eps_r=1.0,
                               contrast=contrast, dx=0.01, dy=0.01,
                               wavelength=wavelength)
    print(f"BIM updated contrast range: [{contrast_update.min():.4f}, {contrast_update.max():.4f}]")

    # DBIM
    print("\n--- Distorted Born IM ---")
    measured = np.random.rand(nx, ny) + 1j * np.random.rand(nx, ny)
    eps_r, residuals = dbim_inverse_scattering(measured, incident, k0, n_iter=5)
    print(f"DBIM reconstructed eps_r range: [{eps_r.min():.4f}, {eps_r.max():.4f}]")

    # Waveguide modes
    print("\n--- Waveguide Mode Analysis ---")
    modes_result = waveguides_mode_analysis(a=0.02, b=0.01, eps_r=2.1, freq=freq)
    print(f"Number of propagating modes: {len([m for m in modes_result['modes'] if m['propagating']])}")
    for m in modes_result['modes'][:5]:
        print(f"  {m['type']}({m['m']},{m['n']}): f_c={m['f_c']/1e9:.3f} GHz, β={m['beta']:.4f} rad/m")

    # AWE
    print("\n--- Asymptotic Waveform Evaluation ---")
    def test_freq_response(omega):
        # Example: resonance-like response
        return 1.0 / (1.0 + 1j * omega / 1e10 - (omega / 1e11)**2)

    F_approx, moments = asymptotic_waveform_eval(test_freq_response, omega0=2*np.pi*freq, n_moments=6)
    print(f"First 3 moments: {moments[:3]}")
    print(f"F(omega0) approx: {F_approx(2*np.pi*freq):.6e}")

    # Conjugate Gradient with Tikhonov
    print("\n--- CG-Tikhonov Regularization ---")
    M, N = 100, 50
    A = np.random.rand(M, N) + 1j * np.random.rand(M, N)
    b = np.random.rand(M) + 1j * np.random.rand(M)
    x_sol, residual = conjugate_gradient_tikhonov(A, b, alpha=0.1)
    print(f"Solution norm: {np.linalg.norm(x_sol):.4f}")
    print(f"CG iterations: {len(residual)}")

    # Born approximation
    print("\n--- Born Approximation Test ---")
    contrast_test = np.zeros((20, 20))
    contrast_test[8:12, 8:12] = 0.5
    incident_test = np.exp(-1j * k0 * np.arange(400).reshape(20, 20) * 0.01)
    G_func = lambda r: greens_function_2d(r, k0)
    E_sca = compute_born_approximation(contrast_test, incident_test, G_func, 0.01, 0.01)
    print(f"Scattered field max: {np.abs(E_sca).max():.6e}")

    print("\n" + "=" * 60)
    print("DONE - chew_fast_methods.py")
    print("=" * 60)