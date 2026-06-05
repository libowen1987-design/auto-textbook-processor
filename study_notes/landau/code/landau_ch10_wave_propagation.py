"""
Landau & Lifshitz, Volume 8: Electrodynamics of Continuous Media
Chapter X: Propagation of Electromagnetic Waves

Key results:
1. Reflection and refraction at dielectric interface (Landau §66):
   θ_i = θ_r   (law of reflection)
   n₁ sin θ₁ = n₂ sin θ₂   (Snell's law)
   
   Fresnel coefficients (normal incidence):
   r = (n₂ - n₁)/(n₂ + n₁)    [amplitude reflection]
   t = 2n₁/(n₂ + n₁)           [amplitude transmission]
   R = |r|²,  T = n₂ cos θ₂ / (n₁ cos θ₁) · |t|²

2. Total internal reflection (TIR):
   θ_c = arcsin(n₂/n₁) for n₁ > n₂
   Evanescent wave in medium 2: E₂ ~ exp(-κz) where κ = (ω/c)√(n₁²sin²θ - n₂²)

3. Goos-Hänchen shift (Landau §73, absorption):
   Lateral shift of reflected beam upon TIR

4. Geometric optics (Landau §65):
   Ray trajectory: d/dr (n · dr/ds) = grad n

Landau §66: Reflection and refraction of electromagnetic waves
Landau §67: Surface impedance of metals
"""

import numpy as np
import matplotlib.pyplot as plt


def snell_law(n1=1.5, n2=1.0):
    """
    Illustrate Snell's law and Fresnel coefficients.
    
    n1 sin θ1 = n2 sin θ2
    """
    theta1 = np.linspace(0, 90, 200) * np.pi/180
    theta2 = np.arcsin((n1/n2) * np.sin(theta1))
    # Clip to valid range (NaN for evanescent beyond critical)
    theta2_valid = np.where(np.isfinite(theta2), theta2, np.nan)
    
    # Critical angle
    if n1 > n2:
        theta_c = np.arcsin(n2/n1) * 180/np.pi
    else:
        theta_c = 90
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    ax = axes[0]
    ax.plot(theta1 * 180/np.pi, theta2_valid * 180/np.pi, 'b-', lw=2)
    ax.plot([0, 90], [0, 90], 'k--', lw=1, label='θ₁ = θ₂ (air-glass equiv)')
    ax.axvline(theta_c, color='r', ls='--', label=f'θ_c = {theta_c:.1f}°')
    ax.set_xlabel(r'Incident angle $\theta_1$ (degrees)')
    ax.set_ylabel(r'Refracted angle $\theta_2$ (degrees)')
    ax.set_title(f'Snell law: n₁={n1}, n₂={n2}')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 90)
    ax.set_ylim(0, 90)
    
    # --- Fresnel coefficients vs angle ---
    ax2 = axes[1]
    
    # s-polarization (TE) and p-polarization (TM) amplitude coefficients
    # For simplicity, show normal incidence first
    r_normal = (n2 - n1) / (n2 + n1)
    t_normal = 2*n1 / (n2 + n1)
    R_normal = r_normal**2
    T_normal = 1 - R_normal
    
    # Full Fresnel formulas
    theta1_arr = np.linspace(0, 85, 200) * np.pi/180
    sin_t1 = np.sin(theta1_arr)
    cos_t1 = np.cos(theta1_arr)
    sin_t2 = np.minimum((n1/n2)*sin_t1, 0.9999)
    theta2_arr = np.arcsin(sin_t2)
    cos_t2 = np.cos(theta2_arr)
    
    # s-pol (TE): Es perpendicular to plane of incidence
    r_s = (n1*cos_t1 - n2*cos_t2) / (n1*cos_t1 + n2*cos_t2)
    t_s = 2*n1*cos_t1 / (n1*cos_t1 + n2*cos_t2)
    R_s = np.abs(r_s)**2
    T_s = (n2*np.real(cos_t2)/(n1*np.real(cos_t1))) * np.abs(t_s)**2
    
    # p-pol (TM): Es parallel to plane of incidence
    r_p = (n2*cos_t1 - n1*cos_t2) / (n2*cos_t1 + n1*cos_t2)
    t_p = 2*n1*cos_t1 / (n2*cos_t1 + n1*cos_t2)
    R_p = np.abs(r_p)**2
    T_p = (n2*np.real(cos_t2)/(n1*np.real(cos_t1))) * np.abs(t_p)**2
    
    ax2.plot(theta1_arr*180/np.pi, R_s*100, 'b-', lw=2, label=r'$R_s$ (s-pol)')
    ax2.plot(theta1_arr*180/np.pi, R_p*100, 'r--', lw=2, label=r'$R_p$ (p-pol)')
    ax2.axhline(R_normal*100, color='k', ls=':', alpha=0.5, label=f'$R$(norm)={R_normal*100:.1f}%')
    ax2.axvline(theta_c, color='g', ls='--', label=f'θ_c={theta_c:.1f}°')
    ax2.set_xlabel(r'Incident angle $\theta_1$ (deg)')
    ax2.set_ylabel('Reflectivity R (%)')
    ax2.set_title(f'Fresnel reflectivity: n₁={n1} → n₂={n2}')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 85)
    ax2.set_ylim(0, 100)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch10_reflection_refraction.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    
    print(f"[landau_ch10] n1={n1}, n2={n2}")
    print(f"[landau_ch10] Normal incidence: R={R_normal*100:.2f}%, T={T_normal*100:.2f}%")
    if n1 > n2:
        print(f"[landau_ch10] Critical angle θ_c = {theta_c:.2f}°")
    print(f"[landau_ch10] Plot saved.")


def total_internal_reflection(n1=1.5, n2=1.0, theta_i=60.0, λ0=632.8e-9):
    """
    Show evanescent wave in medium 2 during total internal reflection.
    
    Landau §66: For θ₁ > θ_c:
    κ = (2π/λ₀) √(n₁² sin²θ₁ - n₂²)  [decay constant]
    E₂(z) = E₀ exp(-κ z)
    """
    theta_c = np.arcsin(n2/n1) * 180/np.pi
    theta_i_rad = theta_i * np.pi/180
    
    omega = 2*np.pi * 3e8 / λ0
    kappa = (omega / 3e8) * np.sqrt(n1**2 * np.sin(theta_i_rad)**2 - n2**2)
    
    z = np.linspace(0, 2*λ0, 300) * 1e9  # nm
    E_ev = np.exp(-kappa * z * 1e-9)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    ax = axes[0]
    ax.plot(z, E_ev, 'b-', lw=2)
    ax.axhline(1/np.e, color='r', ls='--', label=f'1/e = {1/np.e:.3f}')
    decay_depth = 1/kappa * 1e9
    ax.axvline(decay_depth, color='g', ls=':', label=f'δ = {decay_depth:.1f} nm')
    ax.set_xlabel(r'Depth $z$ into medium 2 (nm)')
    ax.set_ylabel(r'Evanescent amplitude (normalized)')
    ax.set_title(f'TIR: θ_i={theta_i}° > θ_c={theta_c:.1f}°, n₁={n1}, n₂={n2}')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Phase shift (Goos-Hänchen)
    phi_s = 2 * np.arctan(np.sqrt(n1**2*np.sin(theta_i_rad)**2 - n2**2) / 
                            (n1 * np.cos(theta_i_rad)))
    phi_p = 2 * np.arctan(n1**2 * np.sqrt(n1**2*np.sin(theta_i_rad)**2 - n2**2) /
                           (n2**2 * n1 * np.cos(theta_i_rad)))
    
    theta_range = np.linspace(theta_c + 0.5, 85, 100)
    phi_s_arr = 2*np.arctan(np.sqrt(n1**2*np.sin(theta_range*np.pi/180)**2 - n2**2) /
                              (n1*np.cos(theta_range*np.pi/180))) * 180/np.pi
    phi_p_arr = 2*np.arctan(n1**2 * np.sqrt(n1**2*np.sin(theta_range*np.pi/180)**2 - n2**2) /
                             (n2**2 * n1*np.cos(theta_range*np.pi/180))) * 180/np.pi
    
    ax2 = axes[1]
    ax2.plot(theta_range, phi_s_arr, 'b-', lw=2, label=r'$\phi_s$ (s-pol)')
    ax2.plot(theta_range, phi_p_arr, 'r--', lw=2, label=r'$\phi_p$ (p-pol)')
    ax2.axhline(90, color='k', ls=':', alpha=0.5)
    ax2.set_xlabel(r'Incident angle $\theta_i$ (degrees)')
    ax2.set_ylabel(r'Phase shift $\phi$ (degrees)')
    ax2.set_title(r'Landau §66: Goos-Hänchen phase shift for TIR')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(theta_c, 85)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch10_tir.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch10] TIR evanescent decay depth δ = {decay_depth:.1f} nm at λ={λ0*1e9:.1f}nm")
    print(f"[landau_ch10] Goos-Hänchen: φ_s={phi_s*180/np.pi:.1f}°, φ_p={phi_p*180/np.pi:.1f}° at θ_i={theta_i}°")
    print(f"[landau_ch10] Plot saved.")


def geometric_optics_bending():
    """
    Geometric optics: light bending in gradient-index medium.
    Landau §65: Ray equation d/dr(n dr/ds) = grad n
    
    For GRIN lens (radial index variation):
    n(r) = n₀ · (1 - (r/a)²/2)  (parabolic profile)
    """
    import matplotlib.patches as patches
    
    n0 = 1.5
    a = 1e-3  # radius (m)
    
    r = np.linspace(0, a, 200)
    n_r = n0 * (1 - (r/a)**2 / 2)
    
    # Ray trajectory in GRIN medium
    # For n(r) = n0(1 - (r/a)²/2): d²r/dz² = -(1/n0)grad n = (r/a²)
    # Solution: r(z) = r0 cos(z/a) + ... (oscillatory)
    z = np.linspace(0, 10*a, 500)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    ax = axes[0]
    ax.plot(r * 1e3, n_r, 'b-', lw=2)
    ax.set_xlabel(r'Radial distance $r$ (mm)')
    ax.set_ylabel(r'Refractive index $n(r)$')
    ax.set_title(r'Landau §65: GRIN lens index profile $n(r) = n_0(1 - r²/2a²)$')
    ax.grid(True, alpha=0.3)
    
    # Trajectory for rays launched parallel to axis
    ax2 = axes[1]
    for r0 in [0.2*a, 0.4*a, 0.6*a, 0.8*a]:
        # Parabolic trajectory
        trajectory = r0 * np.cos(z/a)
        ax2.plot(z * 1e3, trajectory * 1e3, lw=1.5, alpha=0.8)
    ax2.set_xlabel(r'Axial distance $z$ (mm)')
    ax2.set_ylabel(r'Ray displacement $r$ (mm)')
    ax2.set_title(r'Landau §65: Ray trajectories in GRIN medium')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 10)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch10_geometric_optics.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print("[landau_ch10] Plot saved.")


if __name__ == '__main__':
    # From air to glass
    snell_law(n1=1.0, n2=1.5)
    snell_law(n1=1.5, n2=1.0)
    
    # Total internal reflection
    total_internal_reflection(n1=1.5, n2=1.0, theta_i=60.0)
    
    geometric_optics_bending()