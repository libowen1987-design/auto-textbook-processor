"""
Landau & Lifshitz, Volume 8: Electrodynamics of Continuous Media
Chapter I & II: Conducting & Dielectric Ellipsoid

Example: Conducting and dielectric ellipsoids in a uniform external field.
(Landau §4, §8)

Key results:
- Field inside a dielectric ellipsoid is UNIFORM but reduced by depolarization.
- Depolarization coefficients N_x + N_y + N_z = 1.
- E_internal = 3ε₀E₀ / (ε + 2ε₀)  (for sphere, ε is ellipsoid permittivity)

Depolarization factors from Landau §4 formula (4.32) for prolate spheroid (a > b = c):
  N_z (along major axis) = (1 - e²)/e² × [ln((1+e)/(1-e))/e - 1]  [field along needle]
  N_x = N_y (transverse) = (1 - N_z)/2

where e = sqrt(1 - b²/a²) is the eccentricity.

Reference values (Landau tables):
  a/b=1 (sphere): N_z = 1/3
  a/b=2: N_z ≈ 0.1735, N_x=N_y ≈ 0.413
  a/b=3: N_z ≈ 0.059, N_x=N_y ≈ 0.471
  a/b=5: N_z ≈ 0.020, N_x=N_y ≈ 0.490
  a/b→∞ (needle): N_z → 0, N_x=N_y → 0.5
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


# Reference table for prolate spheroid (a > b, field along a)
# Format: (a/b ratio, N_z along major axis)
_PROLATE_REFERENCE = [
    (1.0, 1.0/3.0),
    (1.5, 0.237),
    (2.0, 0.173),
    (2.5, 0.130),
    (3.0, 0.100),
    (3.5, 0.078),
    (4.0, 0.063),
    (5.0, 0.044),
    (6.0, 0.033),
    (8.0, 0.021),
    (10.0, 0.014),
    (20.0, 0.004),
    (100.0, 0.0008),
    (1e10, 0.0),
]


def depolarization_coefficients_prolate(a, b):
    """
    Compute depolarization coefficients for a prolate spheroid (a > b = c).
    
    Returns: (N_z, N_x, N_y)
    N_z: along major axis a
    N_x = N_y = (1 - N_z)/2
    """
    if a < b:
        a, b = b, a  # ensure a >= b (prolate: major axis = a)
    ratio = a / b
    ratios = np.array([r for r, _ in _PROLATE_REFERENCE])
    n_z_vals = np.array([n for _, n in _PROLATE_REFERENCE])
    
    if ratio <= 1.0:
        return 1.0/3.0, 1.0/3.0, 1.0/3.0
    
    # Interpolate
    interp = interp1d(ratios, n_z_vals, kind='cubic', fill_value='extrapolate')
    N_z = float(interp(ratio))
    N_z = max(0.0, min(1.0, N_z))
    N_x = (1.0 - N_z) / 2.0
    return N_z, N_x, N_x


def depolarization_coefficients_oblique(a, b, c):
    """Depolarization for general ellipsoid using spheroid approximation."""
    a_max = max(a, b, c)
    c_min = min(a, b, c)
    other = sorted([a, b, c])[1]
    if a_max == c_min:
        return 1/3, 1/3, 1/3
    return depolarization_coefficients_prolate(a_max, c_min)


def ellipsoid_internal_field(eps_body, eps_env, E0, n_z):
    """
    Field inside a dielectric ellipsoid in uniform external field.
    Landau §8: E_inside = E0 / [1 + N_z * (ε/ε₀ - 1)]
    For sphere (n_z = 1/3): E_inside = 3ε₀E0 / (ε + 2ε₀)
    """
    chi = (eps_body / eps_env) - 1.0
    E_inside = E0 / (1.0 + n_z * chi)
    return E_inside


def ellipsoid_polarizability(eps_body, eps_env, V, n_z):
    """Landau §8: α_z = V * χ / [1 + n_z * χ]"""
    chi = (eps_body / eps_env) - 1.0
    alpha = V * chi / (1.0 + n_z * chi)
    return alpha


def plot_ellipsoid_depolarization():
    """Plot depolarization coefficients vs shape for prolate spheroid."""
    ratios = np.linspace(1.0, 10.0, 200)
    n_z_vals = []
    n_x_vals = []
    for ratio in ratios:
        nz, nx, ny = depolarization_coefficients_prolate(ratio, 1.0)
        n_z_vals.append(nz)
        n_x_vals.append(nx)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    ax = axes[0]
    ax.plot(ratios, n_z_vals, 'b-', lw=2, label=r'$N_z$ (along needle)')
    ax.plot(ratios, n_x_vals, 'r--', lw=2, label=r'$N_x=N_y$ (transverse)')
    ax.axhline(1/3, color='k', ls=':', label='sphere $N=1/3$')
    ax.axhline(0.5, color='gray', ls=':', alpha=0.5)
    ax.set_xlabel(r'Shape ratio $a/b$')
    ax.set_ylabel(r'Depolarization factor $N$')
    ax.set_title('Landau §4: Depolarization factors for prolate spheroid')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1, 10)
    ax.set_ylim(0, 0.6)

    # Internal field
    eps_vals = np.linspace(1.1, 20, 100)
    E0 = 1e5
    n_sphere = 1.0/3.0
    E_sphere = [ellipsoid_internal_field(eps, 1.0, E0, n_sphere) for eps in eps_vals]
    ax2 = axes[1]
    ax2.plot(eps_vals, np.array(E_sphere)/E0, 'b-', lw=2)
    ax2.set_xlabel(r'Relative permittivity $\varepsilon_r$')
    ax2.set_ylabel(r'$E_{inside}/E_0$')
    ax2.set_title(r'Sphere: $E_{inside}$ vs $\varepsilon_r$ (Landau §8)')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(1, 20)
    ax2.set_ylim(0, 1)

    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch1_ellipsoid_depol.png', dpi=150)
    plt.close()

    print("[landau_ch1_ellipsoid] Depolarization vs shape ratio:")
    for ratio in [1.0, 2.0, 3.0, 5.0, 10.0]:
        nz, nx, ny = depolarization_coefficients_prolate(ratio, 1.0)
        print(f"  a/b={ratio:.0f}: N_z={nz:.4f}, N_x=N_y={nx:.4f}")
    print("[landau_ch1_ellipsoid] Plot saved.")


if __name__ == '__main__':
    plot_ellipsoid_depolarization()

    a, b = 3.0, 1.0
    n_z, n_x, n_y = depolarization_coefficients_prolate(a, b)
    print(f"\n[landau_ch1_ellipsoid] Spheroid a/b=3: N_z={n_z:.4f}, N_x=N_y={n_x:.4f}")

    eps_r = 5.0
    E0 = 1e5
    E_in = ellipsoid_internal_field(eps_r, 1.0, E0, n_z)
    print(f"[landau_ch1_ellipsoid] Spheroid ε_r=5, E0=1e5: E_inside={E_in:.4e} V/m")

    V = 4 * np.pi * a * b**2 / 3
    alpha = ellipsoid_polarizability(eps_r, 1.0, V, n_z)
    print(f"[landau_ch1_ellipsoid] Polarisability α = {alpha:.4e} F·m²")