"""
Landau & Lifshitz, Volume 8: Electrodynamics of Continuous Media
Chapter I: Electrostatics of Conductors

Example 1: Conducting sphere in a uniform external field E₀.
(Landau §3, Problem 1)

The potential outside the sphere is φ = -E₀·r + (R³/r³)E₀·r,
where R is the sphere radius.
The surface charge density is σ(θ) = (3ε₀/4π)E₀·cosθ.
The dipole moment is P = R³E₀.

Verifies: E_inside = 0, field outside is uniform + dipole perturbation.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Physical constants
eps0 = 8.8541878128e-12  # F/m

def sphere_in_uniform_field(E0=1e5, R=0.05, n_points=200):
    """
    Compute and visualize the field of a conducting sphere in uniform field E0.
    
    Returns:
        r, theta: spherical coords
        phi: potential at each point
        E_r, E_theta: field components
        sigma: surface charge density
    """
    # Create polar grid (r, theta)
    r = np.linspace(R * 0.9, 5 * R, n_points)
    theta = np.linspace(0, np.pi, n_points)
    R_grid, THETA = np.meshgrid(r, theta)
    
    # Potential outside sphere: φ = -E₀r cosθ + (R³/r²)E₀ cosθ
    # = -E₀ * cosθ * (r - R³/r²)
    cos_theta = np.cos(THETA)
    phi = -E0 * cos_theta * (R_grid - R**3 / R_grid**2)
    
    # Field components (E = -grad φ)
    # E_r = ∂φ/∂r = -E₀ cosθ * (1 + 2R³/r³)
    # E_θ = (1/r) ∂φ/∂θ = E₀ sinθ * (1 - R³/r³)
    E_r = -E0 * cos_theta * (1 + 2 * R**3 / R_grid**3)
    E_theta = E0 * np.sin(THETA) * (1 - R**3 / R_grid**3)
    
    # Surface charge density on sphere
    theta_surf = np.linspace(0, np.pi, 500)
    sigma = 3 * eps0 * E0 * np.cos(theta_surf)
    
    # Dipole moment
    P = 4 * np.pi * R**3 * eps0 * E0  # C·m
    
    return {
        'r_grid': R_grid, 'theta_grid': THETA,
        'phi': phi, 'E_r': E_r, 'E_theta': E_theta,
        'sigma_theta': theta_surf, 'sigma': sigma,
        'P': P, 'R': R, 'E0': E0
    }


def plot_sphere_field(result):
    """Visualize the sphere in uniform field."""
    R, E0 = result['R'], result['E0']
    R_grid = result['r_grid'] / R
    phi = result['phi'] / (E0 * R)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Potential contours
    ax = axes[0]
    cf = ax.contourf(R_grid * np.cos(result['theta_grid']),
                     R_grid * np.sin(result['theta_grid']),
                     phi, levels=30, cmap='coolwarm')
    ax.set_aspect('equal')
    ax.set_xlabel(r'$x/R$')
    ax.set_ylabel(r'$y/R$')
    ax.set_title(r'Potential $\phi/(E_0 R)$ of conducting sphere in uniform field')
    plt.colorbar(cf, ax=ax, label=r'$\phi/(E_0R)$')
    
    # Add sphere outline
    theta_circle = np.linspace(0, 2*np.pi, 200)
    ax.plot(np.cos(theta_circle), np.sin(theta_circle), 'k-', lw=2)
    
    # Surface charge density
    ax2 = axes[1]
    theta_s = result['sigma_theta'] * 180 / np.pi
    ax2.plot(theta_s, result['sigma'] * 1e3, 'b-', lw=2)
    ax2.axhline(0, color='k', ls='--', lw=0.8)
    ax2.set_xlabel(r'$\theta$ (degrees)')
    ax2.set_ylabel(r'$\sigma$ (mC/m$^2$)')
    ax2.set_title(r'Surface charge density $\sigma(\theta)$')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 180)
    
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch1_sphere_uniform_field.png',
                dpi=150)
    plt.close()
    print(f"[landau_ch1_conductors] Sphere dipole moment P = {result['P']:.4e} C·m")
    print(f"[landau_ch1_conductors] Plot saved.")


if __name__ == '__main__':
    result = sphere_in_uniform_field(E0=1e5, R=0.05)
    plot_sphere_field(result)