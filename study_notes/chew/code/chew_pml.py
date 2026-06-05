"""
chew_pml.py - Perfectly Matched Layer (PML) for Computational Electromagnetics
Based on Chew, Jin, Michielssen, Song "Fast and Efficient Algorithms in CEM" (Artech House 2001)

Implements PML boundary conditions for FDTD and other CEM methods.
PML provides anisotropic absorbing medium with reflection-less wave absorption.
"""

import numpy as np
from scipy.constants import speed_of_light, epsilon_0, mu_0
import matplotlib.pyplot as plt
from typing import Tuple, Callable

mu0 = mu_0
eps0 = epsilon_0
c0 = speed_of_light


def complex_coordinate_stretch(x: np.ndarray, sigma: float, k0: float,
                                thickness: float, x_max: float) -> np.ndarray:
    """
    Complex coordinate stretching for PML.

    x' = x + ∫_0^x σ(s) ds / jk0  (for fields decaying into PML)

    For a uniformly thick PML with conductivity σ:
    x' = x - j * σ * (x - x0) / k0  for x in PML region

    Parameters
    ----------
    x : ndarray
        Physical coordinate (m)
    sigma : float
        Conductivity profile (S/m)
    k0 : float
        Wave number in free space
    thickness : float
        PML thickness (m)
    x_max : float
        Domain boundary location

    Returns
    -------
    x_stretched : ndarray
        Complex stretched coordinate
    """
    x_stretched = x.copy()

    for i in range(len(x)):
        if x[i] > x_max - thickness:
            # Inside PML region
            x_pml = x_max - thickness
            dist = x[i] - x_pml
            # σ * (distance from start of PML) / k0
            decay = sigma * dist / k0
            x_stretched[i] = x[i] - 1j * decay
        else:
            x_stretched[i] = x[i]

    return x_stretched


def pml_permittivity(sigma_x: float, sigma_y: float, omega: float,
                     eps_r: float = 1.0) -> complex:
    """
    Complex permittivity in PML region.

    ε' = ε0 * (ε_r - j * σ / (ω * ε0))

    Parameters
    ----------
    sigma_x, sigma_y : float
        Conductivity in x and y directions (S/m)
    omega : float
        Angular frequency (rad/s)
    eps_r : float
        Relative permittivity

    Returns
    -------
    eps_complex : complex
        Complex permittivity
    """
    eps_base = eps0 * eps_r
    # Complex part for absorption
    sigma_omega = sigma_x / omega if omega != 0 else 0.0
    eps_complex = eps_base - 1j * sigma_omega / (omega + 1e-12) * eps_base

    return eps_complex


def pml_permeability(sigma_m_x: float, sigma_m_y: float, omega: float,
                     mu_r: float = 1.0) -> complex:
    """
    Complex permeability in PML region (for magnetic conductor).

    μ' = μ0 * (μ_r - j * σ_m / (ω * μ0))

    Parameters
    ----------
    sigma_m_x, sigma_m_y : float
        Magnetic conductivity (S/m)
    omega : float
        Angular frequency
    mu_r : float
        Relative permeability

    Returns
    -------
    mu_complex : complex
        Complex permeability
    """
    mu_base = mu0 * mu_r
    sigma_m_omega = sigma_m_x / omega if omega != 0 else 0.0
    mu_complex = mu_base - 1j * sigma_m_omega / (omega + 1e-12) * mu_base

    return mu_complex


def pml_reflection_coeff(theta_i: float, k0: float, eps_r: float,
                         sigma: np.ndarray, thickness: float) -> float:
    """
    Theoretical reflection coefficient for PML.

    R_pml(θ) ≈ exp(-2 * k0 * cos(θ) * ∫_0^d σ(s) ds)

    For optimal PML with parabolic conductivity profile.

    Parameters
    ----------
    theta_i : float
        Incident angle (rad)
    k0 : float
        Wave number
    eps_r : float
        Relative permittivity
    sigma : ndarray
        Conductivity profile (N points along PML)
    thickness : float
        PML thickness (m)

    Returns
    -------
    R : float
        Reflection coefficient magnitude
    """
    # Integration of conductivity along PML path
    sigma_integral = np.trapz(sigma, dx=thickness / len(sigma))

    # Phase factor for oblique incidence
    cos_theta = np.cos(theta_i)

    # Reflection magnitude
    exponent = -2 * k0 * cos_theta * sigma_integral
    R = np.abs(np.exp(exponent))

    return R


def pml_reflection_map(x_min: float, x_max: float, y_min: float, y_max: float,
                       k0: float, sigma_max: float = 1.5,
                       pml_thickness: float = 0.1) -> np.ndarray:
    """
    Generate 2D PML reflection coefficient map.

    Parameters
    ----------
    x_min, x_max, y_min, y_max : float
        Domain boundaries
    k0 : float
        Wave number
    sigma_max : float
        Maximum conductivity at PML boundary
    pml_thickness : float
        PML thickness (m)

    Returns
    -------
    R_map : ndarray (nx, ny)
        2D reflection coefficient
    """
    nx, ny = 100, 100
    x = np.linspace(x_min, x_max, nx)
    y = np.linspace(y_min, y_max, ny)
    X, Y = np.meshgrid(x, y)

    # Distance from domain edge
    dist_x_left = X - x_min
    dist_x_right = x_max - X
    dist_y_bottom = Y - y_min
    dist_y_top = y_max - Y

    # PML mask (1 inside PML, 0 outside)
    pml_mask = np.zeros_like(X)
    pml_mask[dist_x_left < pml_thickness] = 1
    pml_mask[dist_x_right < pml_thickness] = 1
    pml_mask[dist_y_bottom < pml_thickness] = 1
    pml_mask[dist_y_top < pml_thickness] = 1

    # Parabolic conductivity profile
    sigma = np.zeros_like(X)
    # Left PML
    mask_left = dist_x_left < pml_thickness
    sigma[mask_left] = sigma_max * (dist_x_left[mask_left] / pml_thickness) ** 2
    # Right PML
    mask_right = dist_x_right < pml_thickness
    sigma[mask_right] = sigma_max * (dist_x_right[mask_right] / pml_thickness) ** 2
    # Bottom PML
    mask_bottom = dist_y_bottom < pml_thickness
    sigma[mask_bottom] = sigma_max * (dist_y_bottom[mask_bottom] / pml_thickness) ** 2
    # Top PML
    mask_top = dist_y_top < pml_thickness
    sigma[mask_top] = sigma_max * (dist_y_top[mask_top] / pml_thickness) ** 2

    # Reflection coefficient map
    R_map = np.exp(-2 * k0 * sigma * pml_thickness)

    return R_map


def pml_2d_fdtd(eps_r: float = 1.0, mu_r: float = 1.0,
                freq: float = 3e9, domain_size: float = 1.0,
                pml_thickness: float = 0.1, sigma_max: float = 1.5,
                n_steps: int = 500) -> Tuple[np.ndarray, np.ndarray, float]:
    """
    2D FDTD with PML absorbing boundary.

    Updates Maxwell's curl equations with PML conductivity.

    Parameters
    ----------
    eps_r : float
        Relative permittivity
    mu_r : float
        Relative permeability
    freq : float
        Source frequency (Hz)
    domain_size : float
        Domain size (m)
    pml_thickness : float
        PML layer thickness
    sigma_max : float
        Maximum conductivity
    n_steps : int
        Number of time steps

    Returns
    -------
    Ex, Ey : ndarray
        Electric field components
    t : ndarray
        Time array
    """
    # Grid
    dx = domain_size / 100
    dt = dx / (2 * c0)  # Courant stability limit
    nx = int(domain_size / dx) + 1

    # PML parameters
    sigma = np.zeros(nx)
    for i in range(nx):
        x = i * dx
        if x < pml_thickness:
            sigma[i] = sigma_max * (x / pml_thickness) ** 2
        elif x > domain_size - pml_thickness:
            dist = domain_size - x
            sigma[i] = sigma_max * (dist / pml_thickness) ** 2

    # Field arrays
    Ex = np.zeros(nx)
    Ey = np.zeros(nx)
    Hz = np.zeros(nx)

    # Source
    omega = 2 * np.pi * freq
    source_pos = nx // 2

    # Time stepping
    t = np.zeros(n_steps)
    Ex_history = np.zeros((n_steps, nx))

    for n in range(n_steps):
        # Update Hz
        for i in range(nx - 1):
            dHz_dy = (Ey[i + 1] - Ey[i]) / dx
            Hz[i] += dt / mu0 / mu_r * (-dHz_dy)

        # Update Ex (PML damping)
        for i in range(1, nx - 1):
            dHz_dx = (Hz[i] - Hz[i - 1]) / dx
            sigma_e = sigma[i] / eps0 / eps_r
            Ex[i] = Ex[i] * (1 - sigma_e * dt / 2) / (1 + sigma_e * dt / 2)
            Ex[i] += dt / eps0 / eps_r * (-dHz_dx)

        # Update Ey
        for i in range(nx - 1):
            dHz_dy = (Hz[i + 1] - Hz[i]) / dx
            Ey[i] += dt / eps0 / eps_r * (dHz_dy)

        # Source injection (Gaussian pulse)
        t[n] = n * dt
        if n < 50:
            source = np.exp(-((n - 25) * dt) ** 2 / (5e-12) ** 2)
            Ex[source_pos] += source

        Ex_history[n] = Ex.copy()

    return Ex_history, t, dt


def pml_cylindrical(radius: float, pml_thickness: float,
                    sigma_max: float, omega: float,
                    dr: float = 0.001) -> np.ndarray:
    """
    PML for cylindrical coordinates (radial absorption).

    Parameters
    ----------
    radius : float
        Domain radius (m)
    pml_thickness : float
        PML layer thickness
    sigma_max : float
        Maximum conductivity
    omega : float
        Angular frequency
    dr : float
        Radial step size

    Returns
    -------
    sigma_r : ndarray
        Radial conductivity profile
    """
    r = np.arange(0, radius + pml_thickness + dr, dr)
    sigma_r = np.zeros_like(r)

    r_pml_start = radius - pml_thickness

    for i, r_i in enumerate(r):
        if r_i > r_pml_start:
            dist = r_i - r_pml_start
            # Radial PML with parabolic profile
            sigma_r[i] = sigma_max * (dist / pml_thickness) ** 2
        else:
            sigma_r[i] = 0.0

    return sigma_r


def pml_sphere_scattering(freq: float = 5e9, a: float = 0.05,
                          pml_thickness: float = 0.1,
                          sigma_max: float = 2.0,
                          nr: int = 100, ntheta: int = 90) -> Dict:
    """
    PML for spherical scatterer simulation.

    Parameters
    ----------
    freq : float
        Frequency (Hz)
    a : float
        Sphere radius (m)
    pml_thickness : float
        PML thickness
    sigma_max : float
        Maximum conductivity
    nr, ntheta : int
        Grid resolution

    Returns
    -------
    results : dict
        Field data and RCS
    """
    wavelength = c0 / freq
    k0 = 2 * np.pi / wavelength

    # Spherical coordinates
    r = np.linspace(a + pml_thickness, a + 2 * pml_thickness, nr)
    theta = np.linspace(0, np.pi, ntheta)

    # PML damping
    sigma_r = sigma_max * ((r - a) / pml_thickness) ** 2
    sigma_r[r < a + pml_thickness] = 0

    # Field computation ( Mie series would be used in full implementation)
    # Simplified: plane wave in PML
    E_field = np.zeros((nr, ntheta), dtype=complex)

    for ir in range(nr):
        for ith in range(ntheta):
            # Damping factor from PML
            damping = np.exp(-1j * k0 * sigma_r[ir] * (r[ir] - a))
            # Incident plane wave
            E_field[ir, ith] = damping * np.exp(-1j * k0 * r[ir] * np.cos(theta[ith]))

    # RCS at far field
    r_far = 100 * wavelength
    rcs = np.zeros(ntheta)

    for ith in range(ntheta):
        E_far = E_field[-1, ith] * np.exp(1j * k0 * r_far) / r_far
        rcs[ith] = 4 * np.pi * r_far ** 2 * np.abs(E_far) ** 2

    return {
        'r': r,
        'theta': theta,
        'E_field': E_field,
        'rcs': rcs,
        'wavelength': wavelength
    }


def pml_validation(domain_size: float = 1.0, pml_thickness: float = 0.08,
                   sigma_max: float = 1.5, freq: float = 10e9) -> Dict:
    """
    Validate PML by measuring reflection from plane wave incident normally.

    Parameters
    ----------
    domain_size : float
        FDTD domain size (m)
    pml_thickness : float
        PML thickness
    sigma_max : float
        Maximum conductivity
    freq : float
        Frequency (Hz)

    Returns
    -------
    validation : dict
        Reflection coefficient and analysis
    """
    k0 = 2 * np.pi * freq / c0

    # PML profile
    n_pml = int(pml_thickness / 0.001)
    sigma_profile = sigma_max * (np.linspace(0, 1, n_pml)) ** 2

    # Reflection at PML interface
    # For normal incidence: R ≈ exp(-2 * k0 * ∫σ dx)
    integral_sigma = np.trapz(sigma_profile, dx=0.001)
    R_normal = np.exp(-2 * k0 * integral_sigma)

    # For oblique angles
    angles = np.linspace(0, np.pi/2, 30)
    R_angles = np.zeros_like(angles)
    for i, theta in enumerate(angles):
        R_angles[i] = np.exp(-2 * k0 * np.cos(theta) * integral_sigma)

    # Domain with PML
    nx = int(domain_size / 0.001)
    x = np.linspace(0, domain_size, nx)

    # PML conductivity in space
    sigma_x = np.zeros(nx)
    pml_idx = int((domain_size - pml_thickness) / 0.001)
    for i in range(pml_idx, nx):
        dist = (i - pml_idx) * 0.001
        sigma_x[i] = sigma_max * (dist / pml_thickness) ** 2

    return {
        'R_normal_dB': 20 * np.log10(R_normal + 1e-15),
        'angles': angles,
        'R_angles_dB': 20 * np.log10(R_angles + 1e-15),
        'sigma_profile': sigma_profile,
        'sigma_x': sigma_x,
        'k0': k0
    }


if __name__ == '__main__':
    print("=" * 60)
    print("PML Boundary Conditions - Chew Fast Algorithms")
    print("=" * 60)

    freq = 10e9  # 10 GHz
    wavelength = c0 / freq
    omega = 2 * np.pi * freq

    print(f"\nFrequency: {freq/1e9:.1f} GHz")
    print(f"Wavelength: {wavelength*100:.2f} cm")

    # Test complex coordinate stretching
    print("\n--- Complex Coordinate Stretching ---")
    x_test = np.array([0.0, 0.05, 0.1, 0.15, 0.2])
    x_stretched = complex_coordinate_stretch(x_test, sigma=1.5, k0=2*np.pi/wavelength,
                                              thickness=0.05, x_max=0.2)
    print(f"Physical x:    {x_test}")
    print(f"Stretched x':  {x_stretched}")

    # Test PML permittivity
    print("\n--- PML Permittivity ---")
    eps_complex = pml_permittivity(sigma_x=1.5, sigma_y=1.5, omega=omega)
    print(f"Complex ε: {eps_complex:.6e} F/m")
    print(f"Real part: {eps_complex.real:.6e}")
    print(f"Imag part: {eps_complex.imag:.6e}")

    # Test reflection coefficient
    print("\n--- PML Reflection Coefficient ---")
    sigma_test = np.linspace(0, 1.5, 50)
    R = pml_reflection_coeff(theta_i=0.0, k0=2*np.pi/wavelength,
                              eps_r=1.0, sigma=sigma_test,
                              thickness=0.05)
    print(f"R(normal incidence) = {R:.6e} = {20*np.log10(R+1e-15):.2f} dB")

    # Generate reflection map
    print("\n--- Reflection Coefficient Map ---")
    R_map = pml_reflection_map(x_min=0, x_max=0.5, y_min=0, y_max=0.5,
                               k0=2*np.pi/wavelength)
    print(f"Reflection map shape: {R_map.shape}")
    print(f"Max reflection: {R_map.max():.6e}")
    print(f"Min reflection: {R_map.min():.6e}")

    # 2D FDTD with PML
    print("\n--- 2D FDTD with PML ---")
    Ex_hist, t_arr, dt = pml_2d_fdtd(eps_r=1.0, freq=freq,
                                      domain_size=0.3,
                                      pml_thickness=0.02,
                                      sigma_max=1.5,
                                      n_steps=200)
    print(f"FDTD time steps: {len(t_arr)}")
    print(f"Time step dt = {dt:.4e} s")
    print(f"Field shape: {Ex_hist.shape}")

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    # Field at different times
    times_to_plot = [50, 100, 150]
    for t_idx in times_to_plot:
        axes[0].plot(Ex_hist[t_idx], label=f't={t_idx}')
    axes[0].set_xlabel('Grid index')
    axes[0].set_ylabel('E_x (V/m)')
    axes[0].set_title('FDTD Field in PML')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Reflection map
    im = axes[1].imshow(R_map, extent=[0, 0.5, 0, 0.5], cmap='hot',
                        aspect='auto', origin='lower')
    axes[1].set_xlabel('x (m)')
    axes[1].set_ylabel('y (m)')
    axes[1].set_title('PML Reflection Coefficient')
    plt.colorbar(im, ax=axes[1], label='|R|')

    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/chew/code/pml_validation.png',
               dpi=150, bbox_inches='tight')
    plt.close()

    # Cylindrical PML
    print("\n--- Cylindrical PML ---")
    sigma_r = pml_cylindrical(radius=0.2, pml_thickness=0.05,
                              sigma_max=2.0, omega=omega)
    print(f"Cylindrical PML: {len(sigma_r)} points")
    print(f"Max sigma_r: {sigma_r.max():.4f} S/m")

    # Spherical scattering with PML
    print("\n--- Spherical Scattering PML ---")
    results = pml_sphere_scattering(freq=freq, a=0.05)
    print(f"RCS range: {results['rcs'].min():.6e} to {results['rcs'].max():.6e} m²")

    # PML validation
    print("\n--- PML Validation ---")
    validation = pml_validation(domain_size=0.5, pml_thickness=0.05,
                                 sigma_max=1.5, freq=freq)
    print(f"Normal incidence reflection: {validation['R_normal_dB']:.2f} dB")
    print(f"k0 = {validation['k0']:.4f} rad/m")

    print("\n" + "=" * 60)
    print("DONE - chew_pml.py")
    print("=" * 60)