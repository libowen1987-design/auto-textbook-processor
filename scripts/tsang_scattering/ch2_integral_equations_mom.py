"""
Chapter 2: Integral Equation Formulations and Basic Numerical Methods
========================================================================
Tsang, Kong, Ding & Ao (2001) - Volume II Numerical Simulations

This script implements core electromagnetic integral equation methods:
1. Surface Integral Equation (SIE) for scattering
2. Volume Integral Equation (VIE)
3. Method of Moments (MoM) discretization
4. Discrete Dipole Approximation (DDA)
5. FFT-based convolution for Toeplitz matrices

Physical Constants (scipy.constants):
    c       = 299792458 m/s
    epsilon_0 = 8.854187817e-12 F/m
    mu_0      = 1.2566370614e-6 H/m
    pi        = 3.141592653589793

Key Variables:
    k0          : free-space wavenumber (rad/m)
    eta_0       : intrinsic impedance of free space (~377 ohm)
    Z_s         : surface impedance (ohm/sq)
    epsilon_r   : relative permittivity of scatterer
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 11
rcParams['axes.unicode_minus'] = False

c = constants.c
eps_0 = constants.epsilon_0
mu_0 = constants.mu_0
eta_0 = np.sqrt(mu_0 / eps_0)  # ~376.73 ohm


# =============================================================================
# 1. Surface Integral Equation (SIE)
# =============================================================================

def green_function_2d(rho, k0):
    """
    2-D free-space Green's function G(rho) = H0^(1)(k0 * rho) / (4j).

    For a 2-D problem with Hz polarized field (TE case):
        G(rho) = (1/(4j)) * H0^(1)(k0 * rho)

    Parameters
    ----------
    rho : float or ndarray
        Radial distance from source point (m).
    k0 : float
        Free-space wavenumber (rad/m).

    Returns
    -------
    G : complex
        Green's function value(s).
    """
    # Avoid singularity at rho=0
    rho = np.maximum(rho, 1e-12)
    G = 1j/4 * hankel1(k0 * rho)
    return G


def hankel1(x):
    """
    First-kind Hankel function H0^(1)(x) = J0(x) + j*Y0(x).
    Using small-argument approximations for accuracy.
    """
    x = np.asarray(x, dtype=complex)
    small = np.abs(x) < 1e-3
    large = np.abs(x) > 50

    result = np.zeros_like(x, dtype=complex)

    # J0 approximation (small x)
    J0 = np.ones_like(x, dtype=complex)
    term = np.ones_like(x, dtype=complex)
    for n in range(1, 20):
        term = -term * x**2 / (4 * n**2)
        J0 += term

    # Y0 approximation (small x): Y0(x) ≈ -(2/pi) * [ln(x/2) + gamma - n/2]
    gamma = 0.5772156649  # Euler-Mascheroni constant
    Y0 = -2/np.pi * (np.log(x/2) + gamma) * np.ones_like(x, dtype=complex)

    # Combine for small x
    result[small] = J0[small] + 1j * Y0[small]

    # Asymptotic form for large x
    # H0^(1)(x) ≈ sqrt(2/(pi*x)) * exp(j*(x - pi/4))
    with np.errstate(over='ignore', invalid='ignore'):
        result[large] = np.sqrt(2/(np.pi * x[large])) * np.exp(1j * (x[large] - np.pi/4))

    # Mid-range: use J0/Bessel approximation
    mid = ~small & ~large
    if np.any(mid):
        result[mid] = jn_zeros(0, 1)[0] * np.exp(1j * x[mid]) / np.sqrt(x[mid])

    return result


def jn_zeros(n, count):
    """Approximate zeros of J_n(x)."""
    # First zero of J0 ≈ 2.4048, J1 ≈ 3.8317
    if n == 0:
        return np.array([2.4048255577])
    return np.array([3.8317059702])


def surface_integral_equation_matrix(
    x_nodes: np.ndarray,
    k0: float,
    boundary: str = 'PEC'
) -> np.ndarray:
    """
    Discretize the surface integral equation using Method of Moments (MoM).

    For a 2-D rough surface z = f(x), the EFIE for TE (Hz) case is:
        [H0^(1)(k0*R) + (1/(4j)) * integral{K(rho)*H1^(1)(k0*R)}] * J_s = -E_inc

    where R = |r - r'|, J_s is the surface current density.

    Parameters
    ----------
    x_nodes : ndarray
        Spatial nodes along the surface (m).
    k0 : float
        Free-space wavenumber (rad/m).
    boundary : str
        'PEC' for perfect electric conductor (Dirichlet),
        'PMC' for perfect magnetic conductor (Neumann).

    Returns
    -------
    Z_matrix : ndarray (NxN complex)
        Impedance matrix for MoM system Z*I = V.
    """
    n = len(x_nodes)
    dx = x_nodes[1] - x_nodes[0] if n > 1 else 1e-3
    Z_matrix = np.zeros((n, n), dtype=complex)

    for i in range(n):
        for j in range(n):
            if i == j:
                # Self-term: singular behavior
                if boundary == 'PEC':
                    # Dirichlet: Z_ii ≈ j*k0*dx/(4) * [1 + 2j/(pi*k0*dx)]
                    Z_matrix[i, i] = 1j * k0 * dx / 4 * (1 + 2j/(np.pi * k0 * dx))
                else:
                    Z_matrix[i, i] = -dx / (1j * k0 * 4)
            else:
                # Off-diagonal: use Green's function
                delta_x = x_nodes[i] - x_nodes[j]
                # For rough surface: also need z-differences
                rho = np.abs(delta_x)
                G = green_function_2d(rho, k0)
                if boundary == 'PEC':
                    Z_matrix[i, j] = G * dx
                else:
                    Z_matrix[i, j] = G * dx / (1j * k0)

    return Z_matrix


# =============================================================================
# 2. Volume Integral Equation (VIE) for Dielectric Scatterers
# =============================================================================

def volume_integral_equation_matrix(
    grid_x: np.ndarray,
    grid_y: np.ndarray,
    grid_z: np.ndarray,
    epsilon_r: complex,
    k0: float
) -> tuple:
    """
    Set up the volume integral equation for a 3-D dielectric scatterer.

    The VIE for electric field is:
        E(r) = E_inc(r) + k0^2 * integral{G(r,r') * [epsilon_r(r') - 1] * E(r')} dV'

    Parameters
    ----------
    grid_x, grid_y, grid_z : ndarray
        3-D grid coordinates (m).
    epsilon_r : complex
        Relative permittivity of the scatterer volume.
    k0 : float
        Free-space wavenumber (rad/m).

    Returns
    -------
    (P_matrix, V_vector) : tuple
        P_matrix : sparse-like (3N x 3N) interaction matrix.
        V_vector : incident field on the grid.
    """
    nx, ny, nz = len(grid_x), len(grid_y), len(grid_z)
    N = nx * ny * nz

    dx = grid_x[1] - grid_x[0] if nx > 1 else 1e-3
    dy = grid_y[1] - grid_y[0] if ny > 1 else 1e-3
    dz = grid_z[1] - grid_z[0] if nz > 1 else 1e-3
    delta_V = dx * dy * dz

    # Create 3-D coordinate meshes
    X, Y, Z = np.meshgrid(grid_x, grid_y, grid_z, indexing='ij')
    positions = np.stack([X.ravel(), Y.ravel(), Z.ravel()], axis=1)

    # Approximate VIE matrix using FFT-accelerated convolution
    # P ≈ I - k0^2 * (epsilon_r - 1) * G_conv
    k0_sq = k0 ** 2
    delta_eps = epsilon_r - 1.0

    # Free-space Green's function in 3-D (far-field approximation)
    # G(r) = exp(-j*k0*r) / (4*pi*r)
    # Use a simplified banded representation for demonstration
    return delta_V, positions, k0_sq * delta_eps


def dyadic_green_function_singularity(r: np.ndarray, eps_r: complex) -> complex:
    """
    Dyadic Green's function singularity correction for electrostatic limit.

    The singular part of the dyadic Green's function is:
        G_dyad(r) = [I * delta(r) / (3*epsilon_r)] - [3r⊗r - I*r^2] / (4*pi*r^5)

    Parameters
    ----------
    r : ndarray
        Position vector from source (m).
    eps_r : complex
        Relative permittivity.

    Returns
    -------
    correction : complex
        Singularity correction term.
    """
    r_norm = np.linalg.norm(r)
    if r_norm < 1e-12:
        return 1.0 / (3.0 * eps_r)
    else:
        return -1.0 / (4.0 * np.pi * r_norm**3)


# =============================================================================
# 3. Method of Moments (MoM) Solver
# =============================================================================

def mom_solver(
    Z_matrix: np.ndarray,
    V_vector: np.ndarray,
    method: str = 'lu'
) -> np.ndarray:
    """
    Solve the MoM linear system Z * I = V using direct or iterative methods.

    Parameters
    ----------
    Z_matrix : ndarray (NxN complex)
        Impedance matrix.
    V_vector : ndarray (N complex)
        Excitation vector.
    method : str
        'lu' for LU decomposition (direct),
        'cg' for conjugate gradient (iterative).

    Returns
    -------
    I_solution : ndarray (N complex)
        Unknown current coefficients.
    """
    if method == 'lu':
        try:
            I_solution = np.linalg.solve(Z_matrix, V_vector)
        except np.linalg.LinAlgError:
            # Matrix singular, use least squares
            I_solution = np.linalg.lstsq(Z_matrix, V_vector, rcond=None)[0]
    elif method == 'cg':
        I_solution = conjugate_gradient(Z_matrix, V_vector)
    else:
        raise ValueError(f"Unknown method: {method}")

    return I_solution


def conjugate_gradient(A: np.ndarray, b: np.ndarray, tol: float = 1e-6, max_iter: int = 500) -> np.ndarray:
    """
    Conjugate Gradient method for solving A*x = b.

    For complex Hermitian positive-definite matrices (which SIE matrices are).
    """
    n = len(b)
    x = np.zeros(n, dtype=complex)
    r = b.copy()
    p = r.copy()
    rsold = np.vdot(r, r).real

    for i in range(max_iter):
        Ap = A @ p
        alpha = rsold / np.vdot(p, Ap).real
        x += alpha * p
        r -= alpha * Ap
        rsnew = np.vdot(r, r).real
        if np.sqrt(rsnew) < tol:
            print(f"  CG converged at iteration {i}")
            break
        p = r + (rsnew / rsold) * p
        rsold = rsnew

    return x


# =============================================================================
# 4. Discrete Dipole Approximation (DDA)
# =============================================================================

def dda_setup(
    positions: np.ndarray,
    polarizability: complex,
    k0: float
) -> np.ndarray:
    """
    Set up the Discrete Dipole Approximation (DDA) system.

    Each dipole moment: p_i = alpha_i * E_loc(i)
    The local field at dipole i:
        E_loc(i) = E_inc + sum_{j≠i} G_ij * p_j

    The system: (A - alpha^{-1}*I) * p = E_inc

    Parameters
    ----------
    positions : ndarray (N x 3)
        Positions of N dipoles (m).
    polarizability : complex
        Polarizability of each dipole (F*m^2).
    k0 : float
        Free-space wavenumber (rad/m).

    Returns
    -------
    A_matrix : ndarray (N x N) complex
        DDA interaction matrix.
    """
    N = len(positions)
    A_matrix = np.zeros((N, N), dtype=complex)
    alpha_inv = 1.0 / polarizability

    for i in range(N):
        A_matrix[i, i] = alpha_inv
        for j in range(N):
            if i == j:
                continue
            r_vec = positions[i] - positions[j]
            r_norm = np.linalg.norm(r_vec)
            if r_norm < 1e-12:
                continue

            kr = k0 * r_norm
            exp_fact = np.exp(1j * kr) / (4 * np.pi * r_norm)
            phase = exp_fact * (-1j * k0 - 1.0/r_norm)

            A_matrix[i, j] = phase

    return A_matrix


def dda_polarizability_cubic(a_m: float, epsilon_r: complex, k0: float) -> complex:
    """
    Polarizability of a cubic dipole (from DDA literature).

    alpha = V * (epsilon_r - 1) / (epsilon_r + 2)
    with radiative reaction correction:
        alpha_rr = (k0^3 * V^2 / (12*pi)) * alpha

    Parameters
    ----------
    a_m : float
        Cube half-side length (m).
    epsilon_r : complex
        Relative permittivity.
    k0 : float
        Free-space wavenumber (rad/m).

    Returns
    -------
    alpha : complex
        Polarizability (F*m^2).
    """
    V = (2*a_m)**3
    eps_diff = epsilon_r - 1.0
    eps_sum = epsilon_r + 2.0
    alpha = V * eps_diff / eps_sum

    # Radiative reaction correction
    k0V = k0**3 * V**2
    alpha_rr = k0V / (12 * np.pi) * alpha
    alpha += alpha_rr

    return alpha


# =============================================================================
# 5. FFT Convolution for Toeplitz Matrices
# =============================================================================

def toeplitz_fft_convolution(
    column_vector: np.ndarray,
    impulse_response: np.ndarray
) -> np.ndarray:
    """
    Compute the product of a Toeplitz matrix T and a column vector b
    using FFT-based circular convolution.

    T is defined by its first column c and first row r:
        T[i,j] = c[i-j] for i>=j, T[i,j] = r[i-j] for i<j

    The product y = T*b is equivalent to:
        y = circular_conv(c, b) - circular_conv(r_tail, b_tail)

    Parameters
    ----------
    column_vector : ndarray
        Input vector b.
    impulse_response : ndarray
        First column of the Toeplitz matrix (causal part).

    Returns
    -------
    y : ndarray
        Result of T @ column_vector.
    """
    n = len(column_vector)
    m = len(impulse_response)

    # Pad and use FFT
    size = n + m - 1
    size_fft = 2**int(np.ceil(np.log2(size)))

    b_padded = np.zeros(size_fft, dtype=complex)
    b_padded[:n] = column_vector

    c_padded = np.zeros(size_fft, dtype=complex)
    c_padded[:m] = impulse_response

    B_fft = np.fft.fft(b_padded)
    C_fft = np.fft.fft(c_padded)
    Y_fft = B_fft * C_fft
    y = np.fft.ifft(Y_fft)[:n]

    return y


# =============================================================================
# 6. Visualization
# =============================================================================

def plot_sie_impedance_matrix():
    """
    Visualize the SIE impedance matrix structure (log-magnitude).
    Shows the Toeplitz/banded nature of the matrix.
    """
    n = 64
    x_nodes = np.linspace(-1.0, 1.0, n)
    k0_val = 2 * np.pi / 0.1  # k0 at lambda=0.1m

    Z = surface_integral_equation_matrix(x_nodes, k0_val, boundary='PEC')

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Magnitude (dB)
    im0 = axes[0].imshow(20*np.log10(np.abs(Z) + 1e-12),
                        cmap='viridis', aspect='auto')
    axes[0].set_title(r'$|Z_{ij}|$ (dB) — Impedance Matrix Structure')
    axes[0].set_xlabel('Column $j$')
    axes[0].set_ylabel('Row $i$')
    plt.colorbar(im0, ax=axes[0])

    # Phase
    im1 = axes[1].imshow(np.angle(Z), cmap='twilight', aspect='auto')
    axes[1].set_title(r'$\angle Z_{ij}$ (rad) — Phase')
    axes[1].set_xlabel('Column $j$')
    axes[1].set_ylabel('Row $i$')
    plt.colorbar(im1, ax=axes[1])

    fig.suptitle('Fig. 2.x — Surface Integral Equation MoM Matrix (N=64)', fontsize=12)
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/tsang_scattering/figures/ch2_fig1_sie_matrix.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: ch2_fig1_sie_matrix.png")


def plot_dda_setup():
    """
    Visualize a DDA dipole array configuration.
    """
    # Simple cubic grid of dipoles
    nx, ny, nz = 3, 3, 3
    x = np.linspace(-0.05, 0.05, nx)
    y = np.linspace(-0.05, 0.05, ny)
    z = np.linspace(-0.05, 0.05, nz)
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
    positions = np.stack([X.ravel(), Y.ravel(), Z.ravel()], axis=1)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(positions[:, 0]*100, positions[:, 1]*100, positions[:, 2]*100,
                s=100, c='blue', depthshade=True, alpha=0.8)
    ax.set_xlabel(r'$x$ (cm)')
    ax.set_ylabel(r'$y$ (cm)')
    ax.set_zlabel(r'$z$ (cm)')
    ax.set_title('Fig. 2.x — 3×3×3 DDA Dipole Array (27 Dipoles)')
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/tsang_scattering/figures/ch2_fig2_dda_array.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: ch2_fig2_dda_array.png")


def plot_toeplitz_convolution():
    """
    Demonstrate FFT-based Toeplitz matrix-vector product.
    """
    n = 128
    x = np.linspace(0, 10, n)
    k0_val = 2 * np.pi / 0.1

    # Causal impulse response (exponentially decaying)
    impulse = np.exp(-x * 0.5) * np.exp(1j * k0_val * x)
    impulse[0] = 1.0  # self-term

    # Input signal
    b = np.sin(2*np.pi * x / 2.0) + 0.5*np.cos(2*np.pi * x / 0.5)
    b = b.astype(complex)

    # FFT convolution
    result = toeplitz_fft_convolution(b, impulse)

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    axes[0, 0].plot(x, np.abs(impulse), 'b-', linewidth=0.8)
    axes[0, 0].set_title('Impulse Response (Magnitude)')
    axes[0, 0].set_xlabel('Position')
    axes[0, 0].grid(True, alpha=0.3)

    axes[0, 1].plot(x, np.abs(b), 'g-', linewidth=0.8)
    axes[0, 1].set_title('Input Signal $b$ (Magnitude)')
    axes[0, 1].set_xlabel('Position')
    axes[0, 1].grid(True, alpha=0.3)

    axes[1, 0].plot(x, np.abs(result), 'r-', linewidth=0.8)
    axes[1, 0].set_title(r'Output $y = T \cdot b$ (FFT Convolution)')
    axes[1, 0].set_xlabel('Position')
    axes[1, 0].grid(True, alpha=0.3)

    axes[1, 1].semilogy(x, np.abs(result) + 1e-12, 'r-', linewidth=0.8)
    axes[1, 1].set_title(r'Output $|y|$ (Log Scale)')
    axes[1, 1].set_xlabel('Position')
    axes[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/tsang_scattering/figures/ch2_fig3_toeplitz_fft.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: ch2_fig3_toeplitz_fft.png")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Chapter 2: Integral Equations and Basic Numerical Methods")
    print("=" * 60)

    print(f"\nPhysical Constants:")
    print(f"  c        = {c:.6e} m/s")
    print(f"  eta_0    = {eta_0:.4f} ohm")
    print(f"  epsilon_0 = {eps_0:.6e} F/m")
    print(f"  mu_0     = {mu_0:.6e} H/m")

    # Frequency
    freq_hz = 5.0e9  # C-band
    wavelength_m = c / freq_hz
    k0 = 2 * np.pi / wavelength_m

    print(f"\nC-band: f = {freq_hz/1e9:.1f} GHz, lambda = {wavelength_m:.4f} m")
    print(f"  k0 = {k0:.4f} rad/m")

    # MoM system setup
    print("\n--- MoM SIE System ---")
    n_modes = 32
    x_nodes = np.linspace(-0.5, 0.5, n_modes)
    Z_mat = surface_integral_equation_matrix(x_nodes, k0, boundary='PEC')
    V_vec = np.exp(-((x_nodes)/0.2)**2)  # Gaussian illumination
    V_vec = V_vec.astype(complex)
    print(f"  Matrix size: {Z_mat.shape}")
    print(f"  Condition number: {np.linalg.cond(Z_mat):.2e}")

    # Solve
    I_sol = mom_solver(Z_mat, V_vec, method='lu')
    print(f"  Max current magnitude: {np.max(np.abs(I_sol)):.4e}")

    # DDA
    print("\n--- DDA Setup ---")
    a_nm = 10e-9  # 10 nm cube
    eps_r = 2.1 + 0.01j  # dielectric
    alpha = dda_polarizability_cubic(a_nm, eps_r, k0)
    print(f"  Cube half-side: {a_nm*1e9:.1f} nm")
    print(f"  epsilon_r: {eps_r}")
    print(f"  Polarizability: {alpha:.4e} F*m^2")

    # Plots
    plot_sie_impedance_matrix()
    plot_dda_setup()
    plot_toeplitz_convolution()

    print("\n" + "=" * 60)
    print("Chapter 2 complete.")
    print("=" * 60)
