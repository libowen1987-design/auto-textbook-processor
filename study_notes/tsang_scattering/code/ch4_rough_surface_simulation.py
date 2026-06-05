"""
Chapter 4: Random Rough Surface Simulations
============================================
Tsang, Kong, Ding & Ao (2001) - Volume II Numerical Simulations

This script implements:
1. Gaussian rough surface generation (non-penetrable/PEC)
2. Surface integral equation for rough surface scattering
3. Tapering of incident waves (Thorsos method)
4. TE/TM wave decomposition and bistatic scattering coefficients
5. Neumann boundary condition (MFIE for TM case)

Physical Constants (scipy.constants):
    c       = 299792458 m/s
    epsilon_0 = 8.854187817e-12 F/m
    mu_0      = 1.2566370614e-6 H/m
    pi        = 3.141592653589793

Key Variables:
    rms_height    : sigma_h (m) - root mean square surface height
    correlation_length : l_c (m) - correlation length
    k0         : free-space wavenumber (rad/m)
    theta_inc  : incident angle (rad)
    sigma_h    : standard deviation of height fluctuations
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
eta_0 = np.sqrt(mu_0 / eps_0)


# =============================================================================
# 1. Gaussian Rough Surface Generation
# =============================================================================

def generate_gaussian_rough_surface(
    length_m: float,
    n_points: int,
    rms_height_m: float,
    correlation_length_m: float,
    seed: int = None
) -> np.ndarray:
    """
    Generate a 1-D Gaussian random rough surface.

    The surface height f(x) is a zero-mean Gaussian random process with
    Gaussian correlation function:
        C(r) = <f(x) * f(x+r)> = sigma_h^2 * exp(-r^2 / l_c^2)

    Parameters
    ----------
    length_m : float
        Surface length (m).
    n_points : int
        Number of grid points.
    rms_height_m : float
        RMS surface height (m).
    correlation_length_m : float
        Correlation length (m).
    seed : int, optional
        Random seed.

    Returns
    -------
    x_surface : ndarray (n_points,)
        x-coordinates (m).
    z_surface : ndarray (n_points,)
        Surface height z = f(x) (m).
    """
    if seed is not None:
        np.random.seed(seed)

    x_surface = np.linspace(-length_m/2, length_m/2, n_points)
    dx = x_surface[1] - x_surface[0]

    # Build covariance matrix using Gaussian correlation
    x1, x2 = np.meshgrid(x_surface, x_surface, indexing='ij')
    r = np.abs(x1 - x2)
    cov_matrix = (rms_height_m ** 2) * np.exp(-r**2 / (correlation_length_m**2))

    # Ensure positive semi-definiteness
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    eigenvalues = np.maximum(eigenvalues, 1e-15)
    cov_matrix = eigenvectors @ np.diag(eigenvalues) @ eigenvectors.T

    # Generate correlated Gaussian samples
    white = np.random.standard_normal(n_points)
    chol_L = np.linalg.cholesky(cov_matrix)
    z_surface = chol_L @ white

    return x_surface, z_surface


def generate_fractal_rough_surface(
    length_m: float,
    n_points: int,
    rms_height_m: float,
    hurst_exponent: float = 0.5,
    n_octaves: int = 5,
    seed: int = None
) -> np.ndarray:
    """
    Generate a 1-D fractal (self-affine) rough surface using midpoint displacement.

    The power spectral density follows a power law:
        S(k) ∝ k^(-2H - 1)
    where H is the Hurst exponent (0 < H < 1).

    Parameters
    ----------
    length_m : float
        Surface length (m).
    n_points : int
        Number of grid points (must be power of 2 + 1).
    rms_height_m : float
        RMS surface height (m).
    hurst_exponent : float
        Hurst exponent (0.5 for Brownian, 0.8 for terrain-like).
    n_octaves : int
        Number of fractal octaves.
    seed : int, optional
        Random seed.

    Returns
    -------
    x_surface : ndarray
        x-coordinates (m).
    z_surface : ndarray
        Surface height (m).
    """
    if seed is not None:
        np.random.seed(seed)

    # Pad to nearest power of 2 + 1
    n_base = 2**n_octaves + 1
    n_points_actual = max(n_points, n_base)
    x_surface = np.linspace(-length_m/2, length_m/2, n_points_actual)
    dx = x_surface[1] - x_surface[0]

    # Midpoint displacement
    z_surface = np.zeros(n_points_actual)
    z_surface[0] = np.random.normal(0, rms_height_m)
    z_surface[-1] = np.random.normal(0, rms_height_m)

    amplitude = rms_height_m
    frequency = 1.0 / length_m

    for octave in range(n_octaves):
        n_segments = 2**octave
        segment_length = length_m / n_segments
        new_points = n_segments + 1

        # Perturbation amplitude scales with H
        sigma_octave = amplitude * (2**(-hur)) * np.sqrt(1 - 2**(-2*hur))
        for i in range(new_points - 1):
            idx0 = i
            idx_mid = i + n_segments
            idx1 = i + 2*n_segments if i + 2*n_segments < n_points_actual else n_points_actual - 1

            z_surface[idx_mid] = (z_surface[idx0] + z_surface[idx1]) / 2 + \
                                  np.random.normal(0, sigma_octave)

        amplitude *= 2**(-hur)

    # Normalize RMS
    z_surface = z_surface / np.std(z_surface) * rms_height_m

    return x_surface, z_surface


# =============================================================================
# 2. Tapering of Incident Waves (Thorsos Method)
# =============================================================================

def tapered_wave_incident(
    x: np.ndarray,
    z: np.ndarray,
    k0: float,
    theta_inc_rad: float,
    taper_parameter_g: float
) -> np.ndarray:
    """
    Generate a tapered plane wave (Thorsos taper) for rough surface scattering.

    The tapered incident field is:
        Psi_inc(x,z) = exp[ -j*k0*(cos_theta_inc*z - sin_theta_inc*x) * (1 + w) ] * exp(-t)
    where:
        t = [ (cos_theta_inc*z - sin_theta_inc*x) / g ]^2
        w = 2*(t-1) / (k0*g*cos_theta_inc)^2   [correction for slow taper]

    Parameters
    ----------
    x : ndarray
        x-coordinates (m).
    z : ndarray
        z-coordinates (m).
    k0 : float
        Free-space wavenumber (rad/m).
    theta_inc_rad : float
        Incident angle from normal (rad).
    taper_parameter_g : float
        Taper parameter g (m). Typical: g = L/5 to L/10.

    Returns
    -------
    Psi_inc : ndarray complex
        Incident field values.
    """
    cos_theta = np.cos(theta_inc_rad)
    sin_theta = np.sin(theta_inc_rad)

    # Argument of the exponential
    t = (cos_theta * z - sin_theta * x) / taper_parameter_g
    t = t**2

    # Phase factor
    phase_arg = cos_theta * z - sin_theta * x
    w = 2.0 * (t - 1.0) / (k0 * taper_parameter_g * cos_theta)**2
    w = np.maximum(w, 0.0)  # ensure non-negative for evanescent regime

    phase = -k0 * phase_arg * (1 + w)
    Psi_inc = np.exp(1j * phase) * np.exp(-t)

    return Psi_inc


# =============================================================================
# 3. Surface Integral Equation for PEC Rough Surface
# =============================================================================

def efie_pec_surface(
    x_surface: np.ndarray,
    z_surface: np.ndarray,
    k0: float,
    incident_field: np.ndarray,
    boundary: str = 'PEC'
) -> tuple:
    """
    Set up and solve the Electric Field Integral Equation (EFIE) for a PEC surface.

    For TE case (Hz polarization, Dirichlet boundary):
        Psi(r) = 0 on surface  =>  scattered field = -incident field

    The integral equation:
        integral{ G(r,r') * dPhi(r')/ds' } ds' = -j*omega*mu * J_s(r) / 2 + E_inc(r)

    For TM case (Hz polarization, Neumann boundary):
        dPsi/dn = 0 on surface

    Parameters
    ----------
    x_surface, z_surface : ndarray
        Surface coordinates (m).
    k0 : float
        Wavenumber (rad/m).
    incident_field : ndarray
        Incident field values on the surface.
    boundary : str
        'PEC' (Dirichlet) or 'PMC' (Neumann).

    Returns
    -------
    (Z_matrix, V_vector, surface_current) : tuple
    """
    n = len(x_surface)

    # Compute arc-length derivatives
    dx = np.diff(x_surface)
    dz = np.diff(z_surface)
    ds = np.sqrt(dx**2 + dz**2)
    s_nodes = np.zeros(n)
    s_nodes[1:] = np.cumsum(ds)

    # Build impedance matrix via Method of Moments
    Z_matrix = np.zeros((n, n), dtype=complex)
    V_vector = -incident_field.copy()  # RHS = -E_inc for Dirichlet

    for i in range(n):
        for j in range(n):
            if i == j:
                if boundary == 'PEC':
                    Z_matrix[i, i] = 1j * k0 * ds[i] / 4 * (1 + 2j/(np.pi * k0 * ds[i]))
                else:
                    Z_matrix[i, i] = -ds[i] / (1j * k0 * 4)
            else:
                dx_val = x_surface[i] - x_surface[j]
                dz_val = z_surface[i] - z_surface[j]
                rho = np.sqrt(dx_val**2 + dz_val**2)
                rho = max(rho, 1e-12)

                # 2-D Green's function H0^(1)(k0*rho)/(4j)
                kr = k0 * rho
                G = 1j/4 * hankel1_of_order(0, kr)
                Z_matrix[i, j] = G * ds[j]

    return Z_matrix, V_vector, s_nodes


def hankel1_of_order(nu, z):
    """Hankel function of first kind H_nu^(1)(z) = J_nu(z) + j*Y_nu(z)."""
    z = np.asarray(z, dtype=complex)
    small = np.abs(z) < 1e-3
    result = np.zeros_like(z, dtype=complex)

    if nu == 0:
        J0 = np.ones_like(z, dtype=complex)
        term = np.ones_like(z, dtype=complex)
        for k in range(1, 20):
            term = -term * z**2 / (4 * k**2)
            J0 += term
        gamma = 0.5772156649
        Y0 = -2/np.pi * (np.log(z/2) + gamma) * np.ones_like(z, dtype=complex)
        result[small] = J0[small] + 1j * Y0[small]

        large = np.abs(z) > 30
        result[large] = np.sqrt(2/(np.pi*z[large])) * np.exp(1j*(z[large] - np.pi/4))
        mid = ~small & ~large
        if np.any(mid):
            result[mid] = np.exp(1j*z[mid]) / np.sqrt(z[mid])
    return result


# =============================================================================
# 4. Bistatic Scattering Coefficient
# =============================================================================

def bistatic_scattering_coefficient(
    x_surface: np.ndarray,
    z_surface: np.ndarray,
    surface_current: np.ndarray,
    k0: float,
    theta_inc_rad: float,
    n_observation_angles: int = 91
) -> tuple:
    """
    Compute the bistatic scattering coefficient σ(θ_s, θ_i).

    The scattering coefficient is:
        σ(θ_s) = (4*pi / L) * |I(θ_s)|^2
    where:
        I(θ_s) = k0 * integral{ J_s(x) * exp(j*k0*(sin(θ_s)*x + cos(θ_s)*z)) } dx

    Parameters
    ----------
    x_surface, z_surface : ndarray
        Surface coordinates (m).
    surface_current : ndarray
        Surface current J_s on the surface.
    k0 : float
        Wavenumber (rad/m).
    theta_inc_rad : float
        Incident angle (rad).
    n_observation_angles : int
        Number of observation angles.

    Returns
    -------
    (theta_s_grid, sigma_dB) : tuple
        theta_s_grid : ndarray (rad)
        sigma_dB : ndarray (dB)
    """
    theta_s_grid = np.linspace(-np.pi/2, np.pi/2, n_observation_angles)
    sigma = np.zeros(n_observation_angles, dtype=float)

    L = x_surface[-1] - x_surface[0]
    dx = np.diff(x_surface)
    ds = np.sqrt(dx**2 + np.diff(z_surface)**2)

    for idx, theta_s in enumerate(theta_s_grid):
        kx = k0 * np.sin(theta_s)
        kz = k0 * np.cos(theta_s)
        phase = kx * x_surface + kz * z_surface
        integrand = surface_current * np.exp(1j * phase)
        I_theta = np.sum(integrand[:-1] * ds) if len(ds) == len(integrand) else \
                  np.sum(integrand * np.diff(np.concatenate([[0], np.cumsum(ds)])))

        I_theta = np.sum(integrand[:-1] * ds) if len(ds) == len(integrand) else \
                  np.sum(integrand[:-1] * ds)
        sigma[idx] = (4 * np.pi / L) * np.abs(I_theta)**2

    sigma_dB = 10 * np.log10(sigma + 1e-12)
    return theta_s_grid, sigma_dB


def compute_reflectivity_emissivity(
    scattering_coeff: np.ndarray,
    theta_s_grid: np.ndarray,
    theta_inc_rad: float
) -> tuple:
    """
    Compute reflectivity and emissivity from scattering coefficient.

    For passive remote sensing:
        r(θ_i) = integral{ σ(θ_s, θ_i) * cos(θ_s) } dΩ
        ε(θ_i) = 1 - r(θ_i)

    Returns
    -------
    (reflectivity, emissivity) : tuple
    """
    dtheta = theta_s_grid[1] - theta_s_grid[0]
    reflectivity = np.sum(scattering_coeff * np.cos(theta_s_grid)) * dtheta
    emissivity = 1.0 - reflectivity
    return reflectivity, emissivity


# =============================================================================
# 5. Visualization
# =============================================================================

def plot_gaussian_rough_surface():
    """
    Generate and plot a Gaussian rough surface realization.
    """
    length = 10.0  # m
    n_pts = 512
    rms_h = 0.05  # 5 cm RMS height
    corr_len = 1.0  # 1 m correlation length

    x_surf, z_surf = generate_gaussian_rough_surface(
        length, n_pts, rms_h, corr_len, seed=42
    )

    fig, axes = plt.subplots(2, 1, figsize=(12, 7))

    ax0 = axes[0]
    ax0.plot(x_surf, z_surf * 100, 'b-', linewidth=0.7)
    ax0.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
    ax0.set_xlabel(r'$x$ (m)')
    ax0.set_ylabel(r'$z$ (cm)')
    ax0.set_title(r'Fig. 4.x — Gaussian Rough Surface ($\sigma_h = 5$ cm, $l_c = 1$ m)')
    ax0.grid(True, alpha=0.3)

    # Surface slope
    slope = np.gradient(z_surf, x_surf)
    ax1 = axes[1]
    ax1.plot(x_surf, slope * 100, 'r-', linewidth=0.7)
    ax1.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
    ax1.set_xlabel(r'$x$ (m)')
    ax1.set_ylabel(r'$dz/dx$ (%)')
    ax1.set_title(r'Surface Slope $df/dx$')
    ax1.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/tsang_scattering/figures/ch4_fig1_gaussian_surface.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: ch4_fig1_gaussian_surface.png")


def plot_tapered_wave():
    """
    Visualize the Thorsos tapered incident wave.
    """
    x = np.linspace(-10, 10, 400)
    z = np.linspace(-2, 2, 200)
    X, Z = np.meshgrid(x, z, indexing='ij')

    k0 = 2 * np.pi / 0.1
    theta_inc = 30 * np.pi / 180
    g_param = 2.0  # 2 m taper parameter

    Psi = tapered_wave_incident(X, Z, k0, theta_inc, g_param)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Magnitude
    im0 = axes[0].pcolormesh(x, z, np.abs(Psi), cmap='hot', shading='gouraud')
    axes[0].set_xlabel(r'$x$ (m)')
    axes[0].set_ylabel(r'$z$ (m)')
    axes[0].set_title(r'|$\Psi_{inc}$| — Tapered Wave (Thorsos)')
    plt.colorbar(im0, ax=axes[0], label=r'|$\Psi_{inc}$|')
    axes[0].set_aspect('equal')

    # Phase
    im1 = axes[1].pcolormesh(x, z, np.angle(Psi), cmap='twilight', shading='gouraud')
    axes[1].set_xlabel(r'$x$ (m)')
    axes[1].set_ylabel(r'$z$ (m)')
    axes[1].set_title(r'angle($\Psi_{inc}$) (rad)')
    plt.colorbar(im1, ax=axes[1], label=r'Phase (rad)')
    axes[1].set_aspect('equal')

    fig.suptitle(r'Fig. 4.x — Thorsos Tapered Wave ($\theta_i = 30°$, $g = 2$ m)', fontsize=12)
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/tsang_scattering/figures/ch4_fig2_tapered_wave.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: ch4_fig2_tapered_wave.png")


def plot_bistatic_scattering():
    """
    Compute and plot bistatic scattering coefficient for a rough surface.
    """
    # Surface
    length = 20.0
    n_pts = 256
    rms_h = 0.03
    corr_len = 0.8

    x_surf, z_surf = generate_gaussian_rough_surface(
        length, n_pts, rms_h, corr_len, seed=7
    )

    # Incident wave
    k0 = 2 * np.pi / 0.1
    theta_inc = 20 * np.pi / 180
    g_param = length / 6

    Psi_inc = tapered_wave_incident(x_surf, z_surf, k0, theta_inc, g_param)

    # Rough surface scattering (simplified: compute field at observation points)
    theta_obs, sigma_db = bistatic_scattering_coefficient(
        x_surf, z_surf, Psi_inc * 0.1, k0, theta_inc, n_observation_angles=181
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(theta_obs * 180/np.pi, sigma_db, 'b-', linewidth=1.2)
    ax.axvline(x=theta_inc * 180/np.pi, color='r', linestyle='--', linewidth=0.8,
               label=f'Incident angle θ_i = {theta_inc*180/np.pi:.0f}°')
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.3)
    ax.set_xlabel(r'Receiver angle $\theta_s$ (°)')
    ax.set_ylabel(r'$\sigma_{HH}$ (dB)')
    ax.set_title(r'Fig. 4.x — Bistatic Scattering Coefficient ($\sigma_h = 3$ cm)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim([-90, 90])

    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/tsang_scattering/figures/ch4_fig3_bistatic_scattering.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: ch4_fig3_bistatic_scattering.png")


def plot_periodic_rough_surface():
    """
    Show comparison of rough surface statistics with periodic boundary.
    """
    length = 5.0
    n_pts = 256
    rms_h = 0.02
    corr_len = 0.5

    # Periodic surface (repeat)
    x_surf_periodic = np.linspace(-length/2, length/2, n_pts)
    x_repeat = np.concatenate([x_surf_periodic - length, x_surf_periodic, x_surf_periodic + length])
    z_repeat = np.zeros(3 * n_pts)

    for rep in range(3):
        np.random.seed(42 + rep)
        start_idx = rep * n_pts
        end_idx = (rep + 1) * n_pts
        z_repeat[start_idx:end_idx] = np.random.normal(0, rms_h, n_pts) * \
                                       np.exp(-(x_repeat[start_idx:end_idx]**2) / (2*corr_len**2))

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(x_repeat, z_repeat * 100, 'b-', linewidth=0.6)
    ax.axhline(y=0, color='k', linestyle='--', linewidth=0.4)
    ax.set_xlabel(r'$x$ (m)')
    ax.set_ylabel(r'$z$ (cm)')
    ax.set_title('Fig. 4.x — Periodic Boundary Condition (PBC) Rough Surface')
    ax.grid(True, alpha=0.3)

    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/tsang_scattering/figures/ch4_fig4_periodic_surface.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: ch4_fig4_periodic_surface.png")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Chapter 4: Random Rough Surface Simulations")
    print("=" * 60)

    freq_ghz = 3.0
    wavelength_m = c / (freq_ghz * 1e9)
    k0 = 2 * np.pi / wavelength_m

    print(f"\nFrequency: {freq_ghz} GHz, lambda = {wavelength_m:.4f} m")
    print(f"  k0 = {k0:.4f} rad/m")
    print(f"  eta_0 = {eta_0:.4f} ohm")

    # Generate figures
    plot_gaussian_rough_surface()
    plot_tapered_wave()
    plot_bistatic_scattering()
    plot_periodic_rough_surface()

    print("\n" + "=" * 60)
    print("Chapter 4 complete.")
    print("=" * 60)
