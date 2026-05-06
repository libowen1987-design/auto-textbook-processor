"""
Chapter 1: Monte Carlo Simulations of Layered Media
===================================================
Tsang, Kong, Ding & Ao (2001) - Volume II Numerical Simulations

This script implements:
1. 1-D continuous random medium with Gaussian statistics (permittivity fluctuations)
2. Monte Carlo generation of layered media profiles
3. Application to Antarctica: density profile simulation and effective permittivity

Physical Constants (scipy.constants):
    c       = 299792458 m/s  (speed of light)
    epsilon_0 = 8.854187817e-12 F/m
    mu_0      = 1.2566370614e-6 H/m

Key Variables:
    mean_density    : g/cm^3 (mean mass density)
    std_density     : g/cm^3 (standard deviation in density)
    correlation_length : mm (spatial correlation length)
    depth            : cm (depth into medium)
    relative_permittivity : epsilon_r = epsilon / epsilon_0
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 11
rcParams['axes.unicode_minus'] = False
plt.style.use('default')

# =============================================================================
# 1. Continuous Random Medium: Gaussian Process Generation
# =============================================================================

def generate_gaussian_random_profile(
    depth_cm: np.ndarray,
    mean_density: float,
    std_density: float,
    correlation_length_mm: float,
    seed: int = None
) -> np.ndarray:
    """
    Generate a single realization of a 1-D continuous Gaussian random profile.

    The permittivity is related to mass density via the Clausius-Mossotti relation
    or a simplified linear model. Here we use density as the primary variable.

    Parameters
    ----------
    depth_cm : array-like
        Depth positions (cm). Must be uniformly spaced.
    mean_density : float
        Mean mass density (g/cm^3).
    std_density : float
        Standard deviation of mass density (g/cm^3).
    correlation_length_mm : float
        Correlation length in mm (exponential correlation function).
    seed : int, optional
        Random seed for reproducibility.

    Returns
    -------
    density_profile : ndarray
        Realization of density at each depth (g/cm^3).

    Mathematical Model
    ------------------
    The correlation coefficient (exponential form):
        r(z1 - z2) = exp(-|z1 - z2| / l_c)    [Eq. 1.1.3]
    where l_c is the correlation length.
    """
    if seed is not None:
        np.random.seed(seed)

    n = len(depth_cm)
    depth_m = depth_cm / 100.0  # convert cm -> m
    corr_len_m = correlation_length_mm / 1000.0  # mm -> m

    # Build covariance matrix using exponential correlation
    # C(i,j) = std^2 * exp(-|depth[i] - depth[j]| / correlation_length)
    z1, z2 = np.meshgrid(depth_m, depth_m, indexing='ij')
    cov_matrix = (std_density ** 2) * np.exp(-np.abs(z1 - z2) / corr_len_m)

    # Ensure positive semi-definiteness via eigenvalue clipping
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    eigenvalues = np.maximum(eigenvalues, 1e-12)
    cov_matrix = eigenvectors @ np.diag(eigenvalues) @ eigenvectors.T

    # Generate correlated Gaussian samples
    white_noise = np.random.standard_normal(n)
    chol_L = np.linalg.cholesky(cov_matrix)
    density_profile = mean_density + chol_L @ white_noise

    return density_profile


def density_to_permittivity(
    density_g_cm3: np.ndarray,
    reference_density: float = 0.4,
    reference_permittivity: complex = 3.2 + 0.02j
) -> np.ndarray:
    """
    Convert mass density to complex relative permittivity.

    Uses a simplified linear volume fraction model:
        epsilon_r = 1 + 3 * vol_frac * (epsilon_s - 1) / (epsilon_s + 2)
    based on the Maxwell-Garnett mixing formula at low frequency.
    For the Antarctica case (snow/ice), we use a direct linear mapping.

    Parameters
    ----------
    density_g_cm3 : array-like
        Mass density profile (g/cm^3).
    reference_density : float
        Reference density for normalization (g/cm^3).
    reference_permittivity : complex
        Permittivity at reference density.

    Returns
    -------
    epsilon_r : ndarray
        Complex relative permittivity (real + j*imag).
    """
    # Linear volume fraction model
    volume_fraction = density_g_cm3 / 2.0  # ice density ~0.917 g/cm^3 -> max vol_frac ~0.5
    volume_fraction = np.clip(volume_fraction, 0.0, 0.6)

    # Maxwell-Garnett effective permittivity
    eps_matrix = 1.05 + 0.05j  # air matrix
    eps_inclusion = 3.15 + 0.001j  # ice

    numerator = eps_inclusion + 2*eps_matrix + 2*(eps_inclusion - eps_matrix)*volume_fraction
    denominator = eps_inclusion + 2*eps_matrix + (eps_inclusion - eps_matrix)*volume_fraction
    epsilon_r = eps_matrix * numerator / denominator

    return epsilon_r


# =============================================================================
# 2. Random Discrete Layering (Binary Mixture)
# =============================================================================

def generate_binary_layered_medium(
    depth_cm: np.ndarray,
    volume_fraction: float,
    seed: int = None
) -> np.ndarray:
    """
    Generate a binary random medium where each layer is either air or scatterer.

    This represents discrete random layering (e.g., ice layers in snow).
    The permittivity contrast drives the scattering coefficient.

    Parameters
    ----------
    depth_cm : array-like
        Depth positions (cm).
    volume_fraction : float
        Volume fraction of the high-permittivity component (0 to 1).
    seed : int, optional
        Random seed.

    Returns
    -------
    permittivity_profile : ndarray
        Complex relative permittivity at each depth.
        0 = air (epsilon_r = 1.0), 1 = scatterer (epsilon_r = ice_permittivity)
    """
    if seed is not None:
        np.random.seed(seed)

    n = len(depth_cm)
    rand_vals = np.random.uniform(0.0, 1.0, n)
    is_scatterer = (rand_vals < volume_fraction).astype(int)

    eps_air = 1.0 + 0.0j
    eps_ice = 3.15 + 0.001j
    eps_snow = 1.5 + 0.001j  # effective snow permittivity

    epsilon_r = np.where(is_scatterer == 1, eps_ice, eps_air)

    return epsilon_r


# =============================================================================
# 3. Coherent Field and Effective Permittivity Calculation
# =============================================================================

def coherent_field_1d(
    incident_field: complex,
    depth_cm: np.ndarray,
    permittivity_profile: np.ndarray,
    k0: float
) -> tuple:
    """
    Calculate the coherent (average) field and effective permittivity
    for a 1-D layered medium using the transfer matrix method.

    Parameters
    ----------
    incident_field : complex
        Incident field amplitude at z = 0.
    depth_cm : array-like
        Depth positions (cm). Must be sorted ascending.
    permittivity_profile : ndarray
        Complex relative permittivity at each depth.
    k0 : float
        Free-space wavenumber (rad/m).

    Returns
    -------
    (coherent_field, effective_permittivity) : tuple
        coherent_field : ndarray of complex
            Average field at each depth.
        effective_permittivity : complex
            Effective relative permittivity of the medium.
    """
    n = len(depth_cm)
    dz = np.diff(depth_cm) / 100.0  # cm -> m, layer thicknesses

    # Initialize field
    E_plus = incident_field * np.ones(n)  # forward traveling wave
    E_minus = np.zeros(n, dtype=complex)  # backward traveling wave

    # Simple forward scattering approximation
    # delta_eps[i] = epsilon_r[i] - <epsilon_r>
    eps_avg = np.mean(permittivity_profile)

    for i in range(1, n):
        delta_eps = permittivity_profile[i] - eps_avg
        # Phase accumulation
        k_local = k0 * np.sqrt(permittivity_profile[i].real + 0j)
        phase = k_local * dz[i-1]
        # Coupling coefficient
        coupling = 0.25 * delta_eps * k0 / k_local
        E_plus[i] = E_plus[i-1] * np.exp(1j * phase) * (1 + coupling)
        E_minus[i] = E_minus[i-1] * np.exp(-1j * phase) * coupling

    coherent_field = E_plus * np.exp(-np.abs(np.imag(np.sqrt(eps_avg))) * k0 *
                                   depth_cm / 100.0)

    return coherent_field, eps_avg


# =============================================================================
# 4. Monte Carlo Ensemble Averaging
# =============================================================================

def monte_carlo_ensemble(
    depth_cm: np.ndarray,
    mean_density: float,
    std_density: float,
    correlation_length_mm: float,
    n_realizations: int = 100,
    seed_base: int = 42
) -> dict:
    """
    Run Monte Carlo ensemble over many realizations to compute
    <epsilon_r> and the variance.

    Parameters
    ----------
    depth_cm : array-like
        Depth grid (cm).
    mean_density : float
        Mean density (g/cm^3).
    std_density : float
        Std density (g/cm^3).
    correlation_length_mm : float
        Correlation length (mm).
    n_realizations : int
        Number of Monte Carlo realizations.
    seed_base : int
        Base random seed.

    Returns
    -------
    results : dict
        Dictionary with keys: 'mean_density', 'std_density',
        'all_realizations', 'ensemble_mean', 'ensemble_std'.
    """
    all_densities = np.zeros((n_realizations, len(depth_cm)))

    for i in range(n_realizations):
        density = generate_gaussian_random_profile(
            depth_cm, mean_density, std_density,
            correlation_length_mm, seed=seed_base + i
        )
        all_densities[i] = density

    ensemble_mean = np.mean(all_densities, axis=0)
    ensemble_std = np.std(all_densities, axis=0)

    return {
        'mean_density': ensemble_mean,
        'std_density': ensemble_std,
        'all_realizations': all_densities,
        'depth_cm': depth_cm
    }


# =============================================================================
# 5. Visualization
# =============================================================================

def plot_antarctica_application():
    """
    Reproduce Figure 1.1.2 style: single realization of continuous Gaussian
    random profile for Antarctica snow/ice conditions.

    Physical parameters from the text:
        mean_density = 0.4 g/cm^3
        correlation_length = 2 mm
        std_density = 0.0156 g/cm^3
    """
    # Depth grid
    depth_cm = np.linspace(0, 250, 500)

    # Generate profile
    density = generate_gaussian_random_profile(
        depth_cm=depth_cm,
        mean_density=0.4,
        std_density=0.0156,
        correlation_length_mm=2.0,
        seed=42
    )

    # Convert to permittivity
    eps_r = density_to_permittivity(density)

    fig, axes = plt.subplots(2, 1, figsize=(10, 8))

    # Panel (a): Density profile
    ax1 = axes[0]
    ax1.plot(depth_cm, density, 'b-', linewidth=0.8)
    ax1.axhline(y=0.4, color='k', linestyle='--', linewidth=0.8, label=r'$\langle \rho \rangle = 0.4$ g/cm$^3$')
    ax1.set_xlabel(r'Depth (cm)')
    ax1.set_ylabel(r'Mass Density $\rho$ (g/cm$^3$)')
    ax1.set_title('Fig. 1.1.2 — Single Realization of Gaussian Random Profile (Antarctica)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim([0, 250])
    ax1.set_ylim([0.34, 0.46])

    # Panel (b): Effective permittivity
    ax2 = axes[1]
    ax2.plot(depth_cm, eps_r.real, 'b-', linewidth=0.8, label=r'$\varepsilon_r^\prime$')
    ax2.plot(depth_cm, eps_r.imag * 100, 'r--', linewidth=0.8, label=r'$100 \times \varepsilon_r^{\prime\prime}$')
    ax2.set_xlabel(r'Depth (cm)')
    ax2.set_ylabel(r'$\varepsilon_r$')
    ax2.set_title('Complex Relative Permittivity from Density Profile')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim([0, 250])

    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/tsang_scattering/figures/ch1_fig1_density_profile.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: ch1_fig1_density_profile.png")


def plot_monte_carlo_ensemble():
    """
    Monte Carlo ensemble averaging: show mean and confidence interval
    for the density profile.
    """
    depth_cm = np.linspace(0, 250, 100)
    n_runs = 50

    results = monte_carlo_ensemble(
        depth_cm=depth_cm,
        mean_density=0.4,
        std_density=0.0156,
        correlation_length_mm=2.0,
        n_realizations=n_runs,
        seed_base=42
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    mean_d = results['mean_density']
    std_d = results['std_density']

    ax.fill_between(depth_cm, mean_d - 2*std_d, mean_d + 2*std_d,
                    alpha=0.25, color='blue', label=r'$\pm 2\sigma$ band')
    ax.fill_between(depth_cm, mean_d - std_d, mean_d + std_d,
                    alpha=0.4, color='blue', label=r'$\pm 1\sigma$ band')
    ax.plot(depth_cm, mean_d, 'b-', linewidth=1.2, label=r'$\langle \rho \rangle$')
    ax.axhline(y=0.4, color='k', linestyle='--', linewidth=0.8, label='True mean')

    ax.set_xlabel(r'Depth (cm)')
    ax.set_ylabel(r'Mass Density $\rho$ (g/cm$^3$)')
    ax.set_title(f'Monte Carlo Ensemble ({n_runs} realizations)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, 250])

    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/tsang_scattering/figures/ch1_fig2_monte_carlo.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: ch1_fig2_monte_carlo.png")


def plot_binary_layering():
    """
    Simulate binary random discrete layering (air/ice mixture).
    """
    depth_cm = np.linspace(0, 100, 200)
    eps_profile = generate_binary_layered_medium(depth_cm, volume_fraction=0.3, seed=7)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.fill_between(depth_cm, eps_profile.real, 1.0,
                    where=(eps_profile.real > 1.01),
                    color='cyan', alpha=0.6, label='Ice layer')
    ax.fill_between(depth_cm, eps_profile.real, 1.0,
                    where=(eps_profile.real <= 1.01),
                    color='lightyellow', alpha=0.6, label='Air layer')
    ax.plot(depth_cm, eps_profile.real, 'k-', linewidth=0.5)
    ax.set_xlabel(r'Depth (cm)')
    ax.set_ylabel(r'$\varepsilon_r^\prime$')
    ax.set_title('Binary Random Discrete Layering ($\chi_v = 0.3$)')
    ax.legend()
    ax.grid(True, alpha=0.3)

    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/tsang_scattering/figures/ch1_fig3_binary_layering.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: ch1_fig3_binary_layering.png")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Chapter 1: Monte Carlo Simulations of Layered Media")
    print("=" * 60)

    # Physical constants from scipy.constants
    c = constants.c  # m/s
    eps_0 = constants.epsilon_0  # F/m
    mu_0 = constants.mu_0  # H/m

    print(f"\nPhysical Constants:")
    print(f"  c        = {c:.3e} m/s")
    print(f"  epsilon_0 = {eps_0:.3e} F/m")
    print(f"  mu_0     = {mu_0:.3e} H/m")

    # Wavelength and wavenumber
    freq_hz = 1.3e9  # L-band (from Antarctica application)
    wavelength_m = c / freq_hz
    k0 = 2 * np.pi / wavelength_m

    print(f"\nL-band application: f = {freq_hz/1e9:.1f} GHz, lambda = {wavelength_m:.4f} m")

    # Generate figures
    plot_antarctica_application()
    plot_monte_carlo_ensemble()
    plot_binary_layering()

    print("\nMonte Carlo ensemble statistics:")
    depth_cm = np.linspace(0, 250, 100)
    results = monte_carlo_ensemble(depth_cm, 0.4, 0.0156, 2.0, n_realizations=20, seed_base=42)
    print(f"  Ensemble mean density at z=125cm: {results['mean_density'][50]:.4f} g/cm^3")
    print(f"  Ensemble std at z=125cm:          {results['std_density'][50]:.4f} g/cm^3")

    print("\n" + "=" * 60)
    print("Chapter 1 complete.")
    print("=" * 60)
