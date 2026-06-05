"""
Landau & Lifshitz, Volume 8: Electrodynamics of Continuous Media
Chapter II: Electrostatics of Dielectrics

Example 1: Dielectric sphere in a uniform external field.
(Landau §8)

For a dielectric sphere of permittivity ε in a uniform field E₀:
  E_inside = 3ε₀E₀ / (ε + 2ε₀)   (Landau §8, formula (8.2))
  D_inside = 3ε·ε₀E₀ / (ε + 2ε₀)

The polarisation is uniform:
  P = χ·ε₀·E_inside = 3ε₀(ε - ε₀)E₀ / (ε + 2ε₀)  (dipole moment per unit volume)

Surface bound charge density:
  σ = P·n̂ = 3(ε - ε₀)E₀·cosθ / (4π(ε + 2ε₀))

The field outside is the applied field plus that of a dipole.
"""

import numpy as np
import matplotlib.pyplot as plt

eps0 = 8.8541878128e-12


def dielectric_sphere_in_field(eps_r=5.0, E0=1e5, R=0.05, n=200):
    """
    Compute the field of a dielectric sphere in a uniform external field.
    
    Landau §8: sphere in uniform field.
    
    Returns dict with grid data and derived quantities.
    """
    # Field inside sphere (uniform)
    E_inside = 3 * eps0 * E0 / (eps_r * eps0 + 2 * eps0)
    # Actually using relative permittivity ε_r = ε/ε₀
    E_inside = 3 * E0 / (eps_r + 2)   # since ε = ε_r * ε₀
    
    D_inside = eps_r * eps0 * E_inside
    
    # Polarization
    chi = eps_r - 1
    P = chi * eps0 * E_inside   # dipole moment per unit volume
    
    # Surface bound charge density (normal component of P)
    theta_surf = np.linspace(0, 2*np.pi, 500)
    sigma_bound = P * np.cos(theta_surf)  # = P·n̂, n̂ = radial unit vector
    
    # Create 2D grid (r, θ) in cross-section
    r = np.linspace(R * 0.8, 4 * R, n)
    theta = np.linspace(0, np.pi, n)
    R_grid, THETA = np.meshgrid(r, theta)
    
    # Outside: applied field + dipole field
    # φ = -E₀r cosθ + (R³/r²)E₀ cosθ
    cos_theta = np.cos(THETA)
    phi_outside = -E0 * cos_theta * (R_grid - R**3 / R_grid**2)
    
    # Field outside
    # E_r = -∂φ/∂r = -E₀ cosθ (1 + 2R³/r³)   (directed outward from sphere)
    # Actually for a dipole field: radial component
    E_r_out = -E0 * cos_theta * (1 + 2 * R**3 / R_grid**3)
    E_theta_out = E0 * np.sin(THETA) * (1 - R**3 / R_grid**3)
    
    # Inside sphere: uniform field
    # φ_inside = -E_inside · r = -E_inside * r * cosθ
    phi_inside = -E_inside * R_grid * cos_theta
    
    # Combine: inside vs outside
    phi = np.where(R_grid >= R, phi_outside, phi_inside)
    
    # Dipole moment of sphere
    V = 4 * np.pi * R**3 / 3
    P_total = P * V  # total dipole moment
    
    return {
        'r_grid': R_grid, 'theta_grid': THETA,
        'phi': phi,
        'E_r_out': E_r_out, 'E_theta_out': E_theta_out,
        'E_inside': E_inside, 'E0': E0,
        'D_inside': D_inside, 'P': P,
        'sigma_theta': theta_surf, 'sigma_bound': sigma_bound,
        'P_total': P_total, 'R': R, 'eps_r': eps_r,
        'chi': chi
    }


def plot_dielectric_sphere(result):
    """Visualize dielectric sphere in uniform field."""
    R, E0, eps_r = result['R'], result['E0'], result['eps_r']
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # --- Left: potential ---
    ax = axes[0]
    phi = result['phi'] / (E0 * R)
    X = result['r_grid'] * np.cos(result['theta_grid']) / R
    Z = result['r_grid'] * np.sin(result['theta_grid']) / R
    inside = result['r_grid'] < R
    
    phi_plot = phi.copy()
    phi_plot = np.where(inside, np.nan, phi_plot)
    
    levels = np.linspace(-2, 2, 30)
    cf = ax.contourf(X, Z, phi_plot, levels=levels, cmap='coolwarm')
    ax.contour(X, Z, phi_plot, levels=15, colors='k', linewidths=0.4)
    ax.set_aspect('equal')
    ax.set_xlabel(r'$x/R$')
    ax.set_ylabel(r'$z/R$')
    ax.set_title(rf'Dielectric sphere ($\varepsilon_r$={eps_r}) in uniform field $E_0$')
    plt.colorbar(cf, ax=ax, label=r'$\phi/(E_0R)$')
    
    # Sphere outline
    theta_c = np.linspace(0, 2*np.pi, 200)
    ax.plot(np.cos(theta_c), np.sin(theta_c), 'k-', lw=2)
    
    # --- Right: surface bound charge ---
    ax2 = axes[1]
    theta_s = result['sigma_theta'] * 180 / np.pi
    sigma = result['sigma_bound'] * 1e3  # mC/m²
    ax2.plot(theta_s, sigma, 'b-', lw=2)
    ax2.axhline(0, color='k', ls='--', lw=0.8)
    ax2.fill_between(theta_s, sigma, 0, where=(sigma > 0), alpha=0.3, color='blue')
    ax2.fill_between(theta_s, sigma, 0, where=(sigma < 0), alpha=0.3, color='red')
    ax2.set_xlabel(r'$\theta$ (degrees)')
    ax2.set_ylabel(r'$\sigma_{bound}$ (mC/m$^2$)')
    ax2.set_title(r'Bound surface charge $\sigma = \mathbf{P}\cdot\hat{n}$')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 360)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch2_dielectric_sphere.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    
    print(f"[landau_ch2_dielectric] eps_r = {eps_r}")
    print(f"[landau_ch2_dielectric] E_outside at r=R (theta=0): E_r = {result['E_r_out'][0,0]:.4e} V/m")
    print(f"[landau_ch2_dielectric] E_inside (uniform) = {result['E_inside']:.4e} V/m")
    print(f"[landau_ch2_dielectric] P (per unit volume) = {result['P']:.4e} C/m²")
    print(f"[landau_ch2_dielectric] Total dipole moment P*V = {result['P_total']:.4e} C·m")
    print(f"[landau_ch2_dielectric] Plot saved.")


if __name__ == '__main__':
    result = dielectric_sphere_in_field(eps_r=5.0, E0=1e5, R=0.05)
    plot_dielectric_sphere(result)
    
    # Also show eps_r -> infinity (conducting limit)
    result_cond = dielectric_sphere_in_field(eps_r=1e10, E0=1e5, R=0.05)
    print(f"\n[landau_ch2_dielectric] Conducting limit (eps_r->inf): E_inside = {result_cond['E_inside']:.2e} V/m → 0 ✓")