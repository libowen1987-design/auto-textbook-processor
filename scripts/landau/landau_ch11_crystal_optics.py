"""
Landau & Lifshitz, Volume 8: Electrodynamics of Continuous Media
Chapter IX & XI: Electromagnetic Waves in Anisotropic Media - Crystal Optics

Key physics:
1. Dielectric tensor ε_ij for anisotropic crystal: D_i = ε_ij E_j
2. The index ellipsoid (indicatrix): (x²/εₓ) + (y²/ε_y) + (z²/ε_z) = 1
3. For uniaxial crystal: ε_x = ε_y ≠ ε_z
   - Ordinary ray: n_o = √ε_x
   - Extraordinary ray: 1/n_e²(θ) = cos²θ/ε_z + sin²θ/ε_x
4. For biaxial crystal: all three principal values differ
   - Two optic axes

Landau §77: Plane wave in anisotropic medium
  k·(D) = 0,  D ⟂ k,  D = ε·E,  B = H/c,  S = c²[ E × B ] (Poynting)
  
  D = (c²n²/ω²) [E - n̂(n̂·E)]  →  (ε^{-1}·D) = (c²/ω²) D  for k = (ω/c)n̂

Landau §78: Uniaxial crystals
  n_o² = ε_x,  1/n_e²(θ) = cos²θ/ε_z + sin²θ/ε_x
"""

import numpy as np
import matplotlib.pyplot as plt


def indicatrix_uniaxial(n_o=1.658, n_e=1.486):
    """
    Display the index ellipsoid (indicatrix) for a uniaxial crystal.
    
    For a uniaxial crystal with ordinary index n_o and extraordinary index n_e:
    - The ellipsoid cross-section in xz-plane: x²/n_o² + z²/n_e² = 1
    - The optic axis is along z.
    
    The extraordinary refractive index for ray at angle θ to optic axis:
    1/n_e²(θ) = cos²θ/n_e² + sin²θ/n_o²
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # --- Left: 3D indicatrix cross-section ---
    ax = axes[0]
    theta = np.linspace(0, 2*np.pi, 400)
    
    # Cross-section of ellipsoid in xz-plane: x²/n_o² + z²/n_e² = 1
    x_ellip = n_o * np.cos(theta)
    z_ellip = n_e * np.sin(theta)
    ax.plot(x_ellip, z_ellip, 'b-', lw=2, label='Indicatrix cross-section (xz-plane)')
    ax.plot([0, 2*n_o], [0, 0], 'r--', lw=1.5, label=' optic axis (z)')
    ax.plot([0, 0], [0, 2*n_e], 'g--', lw=1.5, label='ordinary axis')
    ax.set_aspect('equal')
    ax.set_xlabel(r'$x/a$')
    ax.set_ylabel(r'$z/c$')
    ax.set_title(fr'Uniaxial crystal indicatrix: $n_o$={n_o}, $n_e$={n_e}')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    
    # --- Right: n_e(θ) polar plot ---
    ax2 = axes[1]
    theta_rad = np.linspace(0, 2*np.pi, 400)
    
    # Extraordinary index as function of angle from optic axis (z)
    # 1/n_e²(θ) = cos²θ/n_e² + sin²θ/n_o²
    cos_t = np.cos(theta_rad)
    sin_t = np.sin(theta_rad)
    n_e_theta_sq_inv = (cos_t**2 / n_e**2) + (sin_t**2 / n_o**2)
    n_e_theta = 1.0 / np.sqrt(n_e_theta_sq_inv + 1e-15)
    
    ax2.plot(theta_rad * 180/np.pi, n_e_theta, 'b-', lw=2,
             label=r'$n_e(\theta)$ - extraordinary')
    ax2.axhline(n_o, color='r', ls='--', lw=1.5, label=f'$n_o$ = {n_o}')
    ax2.axhline(n_e, color='g', ls='--', lw=1.5, label=f'$n_e$ = {n_e}')
    ax2.set_xlabel(r'Angle from optic axis $\theta$ (degrees)')
    ax2.set_ylabel(r'Refractive index $n$')
    ax2.set_title(r'Landau §78: Extraordinary ray index $n_e(\theta)$')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 360)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch11_uniaxial_indicatrix.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    
    print(f"[landau_ch11] n_o={n_o}, n_e={n_e} (typical calcite)")
    print(f"[landau_ch11] For θ=45°: n_e(45°) = {1/np.sqrt((0.5/n_e**2)+(0.5/n_o**2)):.4f}")
    print(f"[landau_ch11] Plot saved.")


def birefringence_demo(n_o=1.658, n_e=1.486, thickness=1e-3):
    """
    Compute ordinary and extraordinary ray paths through a uniaxial crystal plate.
    Ordinary ray: n_o, unaffected by angle (constant index sphere)
    Extraordinary ray: n_e(θ) depends on propagation angle
    """
    # Wave plate: phase difference after thickness L
    # Δφ = (2π/λ) · (n_e(θ) - n_o) · L
    # For quarter-wave plate at λ=632.8nm:
    lambda_nm = 632.8
    L_quarter = lambda_nm * 1e-9 / (4 * (n_e - n_o))
    print(f"[landau_ch11] Quarter-wave plate: L = {L_quarter*1e6:.2f} μm at λ={lambda_nm}nm")
    
    # Ordinary vs extraordinary ray separation after propagation
    wavelengths = np.array([400, 500, 600, 700, 800])  # nm
    delta_n = n_e - n_o
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(wavelengths, delta_n * 1e3 * np.ones_like(wavelengths), 'bo-', lw=2)
    ax.set_xlabel(r'Wavelength $\lambda$ (nm)')
    ax.set_ylabel(r'$\Delta n \times 10^3$')
    ax.set_title(fr'Birefringence $\Delta n = n_e - n_o$ for typical calcite ($n_o$={n_o}, $n_e$={n_e})')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(400, 800)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch11_birefringence.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch11] Δn = {n_e - n_o:.4f}")
    print(f"[landau_ch11] Plot saved.")


def fresnel_equation_anisotropic(eps_x=2.0, eps_y=2.0, eps_z=3.0, n_points=300):
    """
    Fresnel equation for wave normals in biaxial crystal.
    Direction cosines l, m, n of wave normal k̂:
    (1/n² + ε_x^{-1} - l²)⁻¹ + (1/n² + ε_y^{-1} - m²)⁻¹ + (1/n² + ε_z^{-1} - n²)⁻¹ = 0
    
    For uniaxial (eps_x = eps_y):
    n²(θ) = ε_x ε_z / (ε_z cos²θ + ε_x sin²θ)  (extraordinary)
    n_o² = ε_x  (ordinary)
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # --- Left: extraordinary index polar plot for uniaxial ---
    ax = axes[0]
    eps_para = eps_z  # along optic axis
    eps_perp = eps_x  # transverse
    
    theta = np.linspace(0, 2*np.pi, 400)
    cos_t = np.cos(theta)
    sin_t = np.sin(theta)
    
    # Extraordinary: 1/n_e² = cos²θ/ε_z + sin²θ/ε_x
    n_e_sq_inv = cos_t**2 / eps_para + sin_t**2 / eps_perp
    n_e = 1.0 / np.sqrt(n_e_sq_inv + 1e-15)
    
    ax.plot(n_e * np.cos(theta), n_e * np.sin(theta), 'b-', lw=2,
            label=r'$n_e(\theta)$ extraordinary')
    # Ordinary circle
    n_o = np.sqrt(eps_perp)
    circle = n_o * np.ones_like(theta)
    ax.plot(circle * np.cos(theta), circle * np.sin(theta), 'r--', lw=2,
            label=f'$n_o$ = {n_o:.3f}')
    ax.set_aspect('equal')
    ax.set_xlabel(r'$n_x$')
    ax.set_ylabel(r'$n_z$')
    ax.set_title(fr'Uniaxial indicatrix: $n_o=${n_o:.3f}, $n_e=${np.sqrt(eps_para):.3f}')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # --- Right: section index surface ---
    ax2 = axes[1]
    # In xz-plane (phi=0), the index surface equation:
    # (k_x² + k_y² + k_z²) = (ω/c)² ε is a sphere for ordinary
    # and an ellipsoid for extraordinary
    x = np.linspace(-2, 2, 200)
    z = np.linspace(-2, 2, 200)
    X, Z = np.meshgrid(x, z)
    
    # Extraordinary: n_e²(θ) = ε_x ε_z / (ε_z cos²θ + ε_x sin²θ)
    r_sq = X**2 + Z**2 + 1e-15
    n_e_sq = eps_x * eps_z / (eps_z * (Z**2/r_sq) + eps_x * (X**2/r_sq))
    
    # Ordinary index surface: sphere n² = ε_x
    inside_o = (X**2 + Z**2) < eps_x
    inside_e = (X**2/eps_z + Z**2/eps_x) < 1
    
    # Color code
    n_display = np.where(inside_e, np.nan, np.where(inside_o, 1.5, np.nan))
    
    ax2.contour(X, Z, X**2 + Z**2, levels=[eps_x], colors='r', linewidths=2)
    ax2.contour(X**2/eps_z + Z**2/eps_x, [1], colors='b', linewidths=2)
    ax2.set_aspect('equal')
    ax2.set_xlabel(r'$x$')
    ax2.set_ylabel(r'$z$')
    ax2.set_title('Index surface cross-section: red=ordinary sphere, blue=extraordinary ellipsoid')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch11_fresnel_equation.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch11] Biaxial crystal: eps_x={eps_x}, eps_y={eps_y}, eps_z={eps_z}")
    print(f"[landau_ch11] Plot saved.")


if __name__ == '__main__':
    indicatrix_uniaxial(n_o=1.658, n_e=1.486)
    birefringence_demo(n_o=1.658, n_e=1.486)
    fresnel_equation_anisotropic(eps_x=2.0, eps_y=2.0, eps_z=3.0)