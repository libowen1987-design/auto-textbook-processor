"""
Chapter 8 — Plane Electromagnetic Waves
Field and Wave Electromagnetics, David K. Cheng (2nd Edition)

Examples covered:
- Section 8-2: Uniform plane wave in free space (properties)
- Section 8-2.2: Polarization (linear, circular, elliptical)
- Section 8-3: Plane waves in conducting media (skin depth)
- Section 8-4: Poynting vector (power flow)
- Section 8-7: Normal incidence at dielectric interface (reflection/transmission)
- Section 8-9: Snell's law, critical angle, Brewster angle
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import mu_0, epsilon_0, pi, c

# =============================================================================
# Section 8-2: Uniform Plane Wave in Free Space
# =============================================================================

def example_8_2_plane_wave_properties():
    """
    Properties of a uniform plane wave in free space:
    - Wave number: k = omega*sqrt(mu*epsilon)
    - Intrinsic impedance: eta = sqrt(mu/epsilon) = 120*pi Ohms
    - Phase velocity: u = 1/sqrt(mu*epsilon) = c
    - Wavelength: lambda = 2*pi/k
    """
    f = 3e9      # 3 GHz
    omega = 2 * pi * f
    k = omega * np.sqrt(mu_0 * epsilon_0)
    eta_0 = np.sqrt(mu_0 / epsilon_0)
    u = omega / k
    lam = 2 * pi / k

    print(f"\nSection 8-2: Uniform Plane Wave in Free Space")
    print(f"  f = {f*1e-9:.1f} GHz")
    print(f"  ω = {omega:.4e} rad/s")
    print(f"  k = {k:.4f} rad/m")
    print(f"  η₀ = {eta_0:.4f} Ω  (= {eta_0/pi:.4f}π Ω)")
    print(f"  u = {u:.4f} m/s  (= c = {c:.4f} m/s)")
    print(f"  λ = {lam*100:.4f} cm")

    # Visualize wave propagation
    z = np.linspace(0, 3 * lam, 1000)
    T = 1 / f
    t_vals = [0, T/4, T/2, 3*T/4]

    E_0 = 1.0   # V/m (normalized)
    H_0 = E_0 / eta_0

    fig, axes = plt.subplots(2, 1, figsize=(12, 7))

    colors = ['blue', 'red', 'green', 'orange']
    for i, t in enumerate(t_vals):
        E_z_t = E_0 * np.sin(omega * t - k * z)
        H_z_t = H_0 * np.sin(omega * t - k * z)
        axes[0].plot(z * 100, E_z_t, color=colors[i], lw=1.5,
                     label=f't = {t*1e9:.2f} ns')
        axes[1].plot(z * 100, H_z_t, color=colors[i], lw=1.5,
                     label=f't = {t*1e9:.2f} ns')

    for ax in axes:
        ax.set_xlabel('Distance z (cm)')
        ax.set_ylabel('Field amplitude (V/m or A/m)')
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=9)
        ax.set_xlim(0, 3 * lam * 100)

    axes[0].set_title(r'Example 8-2: $\mathbf{E}_x(z,t) = E_0\sin(\omega t - kz)\,\hat{\mathbf{x}}$')
    axes[1].set_title(r'$\mathbf{H}_y(z,t) = H_0\sin(\omega t - kz)\,\hat{\mathbf{y}}$')
    plt.suptitle(r'Example 8-2: Uniform Plane Wave in Free Space ($\lambda$ = ' +
                 f'{lam*100:.2f} cm)', fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch08_plane_wave_propagation.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Figure saved: ch08_plane_wave_propagation.png")
    return k, eta_0, lam

# =============================================================================
# Section 8-2.2: Polarization
# =============================================================================

def example_8_2_polarization():
    """
    Visualize linear, circular, and elliptical polarization.
    """
    t = np.linspace(0, 2*pi, 500)

    fig, axes = plt.subplots(1, 3, figsize=(15, 5), subplot_kw={'projection': None})

    # Linear polarization: E_x and E_y in phase
    Ex_lin = np.cos(t)
    Ey_lin = np.cos(t)
    ax = axes[0]
    ax.plot(Ex_lin, Ey_lin, 'b-', lw=1.5)
    ax.set_xlabel('$E_x$')
    ax.set_ylabel('$E_y$')
    ax.set_title('Linear Polarization\n(phase difference = 0)')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_facecolor('#f0f0f0')

    # Circular polarization (RHC): E_x leads E_y by 90°
    Ex_circ = np.cos(t)
    Ey_circ = np.sin(t)
    ax = axes[1]
    ax.plot(Ex_circ, Ey_circ, 'r-', lw=1.5)
    ax.set_xlabel('$E_x$')
    ax.set_ylabel('$E_y$')
    ax.set_title('Circular Polarization (RHC)\n$E_y$ leads $E_x$ by 90°')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_facecolor('#f0f0f0')

    # Elliptical polarization
    Ex_ell = np.cos(t)
    Ey_ell = 0.5 * np.sin(t)
    ax = axes[2]
    ax.plot(Ex_ell, Ey_ell, 'g-', lw=1.5)
    ax.set_xlabel('$E_x$')
    ax.set_ylabel('$E_y$')
    ax.set_title('Elliptical Polarization\n(amplitude ratio 2:1)')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_facecolor('#f0f0f0')

    plt.suptitle(r'Example 8-2.2: Wave Polarization ($\omega t$ varying)', fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch08_polarization.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\nSection 8-2.2: Polarization")
    print(f"  Linear: E_x and E_y in phase")
    print(f"  Circular (RHC): E_y leads E_x by 90° (clockwise when viewed from source)")
    print(f"  Elliptical: general case with amplitude ratio ≠ 1 and phase ≠ 0, 90°")
    print(f"  Figure saved: ch08_polarization.png")

# =============================================================================
# Section 8-3: Plane Wave in Conducting Medium (Skin Depth)
# =============================================================================

def example_8_3_skin_depth():
    """
    Wave propagation in a good conductor (copper).
    alpha = beta = sqrt(pi*f*mu*sigma)  [for sigma >> omega*epsilon]
    delta_s = 1/alpha = sqrt(2/(omega*mu*sigma))
    """
    f = 60.0        # Hz
    sigma_cu = 5.8e7   # S/m (copper)
    mu_r = 1.0

    omega = 2 * pi * f
    alpha = np.sqrt(pi * f * mu_0 * mu_r * sigma_cu)
    beta = alpha
    delta_s = 1 / alpha

    # Frequency sweep
    f_range = np.logspace(1, 8, 500)   # 10 Hz to 100 MHz
    omega_range = 2 * pi * f_range
    alpha_range = np.sqrt(pi * f_range * mu_0 * sigma_cu)
    delta_range = 1 / alpha_range

    plt.figure(figsize=(10, 5))
    ax = plt.subplot(121)
    ax.loglog(f_range, delta_range * 100, 'b-', lw=2)
    ax.set_xlabel('Frequency $f$ (Hz)')
    ax.set_ylabel(r'Skin depth $\delta_s$ (cm)')
    ax.set_title(r'Example 8-3: Skin Depth in Copper ($\sigma$ = 5.8×10⁷ S/m)')
    ax.grid(True, which='both', alpha=0.3)
    ax.axvline(x=f, color='r', ls='--', alpha=0.7, label=f'60 Hz: δ = {delta_s*100:.2f} cm')
    ax.legend()

    # Also show attenuation vs depth at f = 60 Hz
    z_range = np.linspace(0, 10 * delta_s, 300)
    E_z = np.exp(-alpha * z_range)

    ax = plt.subplot(122)
    ax.plot(z_range * 100, E_z, 'b-', lw=2)
    ax.axhline(y=1/np.e, color='r', ls='--', alpha=0.7,
               label=f'1/e = {1/np.e:.3f} at δ = {delta_s*100:.2f} cm')
    ax.set_xlabel(r'Depth $z$ (cm)')
    ax.set_ylabel(r'$|E|/|E_0|$')
    ax.set_title(rf'Example 8-3: Field Attenuation in Copper ($f$ = {f} Hz)')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch08_skin_depth.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nSection 8-3: Plane Wave in Conducting Medium")
    print(f"  Copper at f = {f} Hz:")
    print(f"  α = β = √(πfμσ) = {alpha:.4f} Np/m")
    print(f"  δ_s = 1/α = {delta_s:.4f} m = {delta_s*100:.4f} cm")
    print(f"  γ = α + jβ = {alpha:.4f} + j{beta:.4f}  [per meter]")
    print(f"  Figure saved: ch08_skin_depth.png")
    return delta_s

# =============================================================================
# Section 8-4: Poynting Vector
# =============================================================================

def example_8_4_poynting_vector():
    """
    Poynting vector S = E × H for a uniform plane wave.
    For a plane wave: S_avg = |E|^2 / (2*eta) W/m^2
    """
    E_0 = 100.0    # V/m (peak)
    eta_0 = np.sqrt(mu_0 / epsilon_0)

    S_avg = E_0**2 / (2 * eta_0)

    print(f"\nSection 8-4: Poynting Vector")
    print(f"  E_0 = {E_0} V/m")
    print(f"  S_avg = |E|²/(2η₀) = {E_0**2}/{2*eta_0:.2f} = {S_avg:.4f} W/m²")
    print(f"  Also: S_avg = H_0²·η₀/2 = {E_0/eta_0**2 * eta_0/2:.4f} W/m²")

    # Visualize instantaneous Poynting vector
    t = np.linspace(0, 2*pi, 300)
    z = np.linspace(0, 1.0, 200)
    T, Z = np.meshgrid(t, z)
    omega_norm = 1.0; k_norm = 1.0  # normalized

    S_z = E_0 * (E_0/eta_0) * np.sin(omega_norm*T - k_norm*Z)**2  # instantaneous S_z

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax = axes[0]
    ax.plot(t, S_z[0, :], 'b-', lw=2)
    ax.set_xlabel(r'$\omega t$ (rad)')
    ax.set_ylabel(r'$S_z$ (W/m²)')
    ax.set_title(rf'S_z at z=0: $S = \frac{{E_0^2}}{{\eta_0}}\sin^2(\omega t)$')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, S_avg * 3)

    # z vs time at fixed point
    ax = axes[1]
    t_idx = 0  # at t=0
    ax.plot(z, S_z[:, t_idx], 'b-', lw=2)
    ax.set_xlabel(r'Distance $z$ (m)')
    ax.set_ylabel(r'$S_z$ (W/m²)')
    ax.set_title(r'$S_z$ vs $z$ at fixed $t$: standing wave pattern (PEC boundary)')
    ax.grid(True, alpha=0.3)

    plt.suptitle(r'Example 8-4: Poynting Vector — $S = \mathbf{E} \times \mathbf{H}$', fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch08_poynting_vector.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Figure saved: ch08_poynting_vector.png")
    return S_avg

# =============================================================================
# Section 8-7: Normal Incidence at Dielectric Boundary
# =============================================================================

def example_8_7_normal_incidence():
    """
    Reflection and transmission at normal incidence on a dielectric.
    n1 = sqrt(eps_r1), n2 = sqrt(eps_r2)
    Gamma = (eta2 - eta1) / (eta2 + eta1)
    Tau = 2*eta2 / (eta2 + eta1)
    """
    eps_r1 = 1.0    # air
    eps_r2 = 2.1    # glass (Teflon)
    eta_1 = np.sqrt(mu_0 / (epsilon_0 * eps_r1))
    eta_2 = np.sqrt(mu_0 / (epsilon_0 * eps_r2))

    Gamma = (eta_2 - eta_1) / (eta_2 + eta_1)
    Tau = 2 * eta_2 / (eta_2 + eta_1)
    SWR = (1 + abs(Gamma)) / (1 - abs(Gamma))

    print(f"\nSection 8-7: Normal Incidence — Dielectric Interface")
    print(f"  Medium 1: ε_r = {eps_r1} (air), η₁ = {eta_1:.2f} Ω")
    print(f"  Medium 2: ε_r = {eps_r2} (glass), η₂ = {eta_2:.2f} Ω")
    print(f"  Γ = (η₂-η₁)/(η₂+η₁) = {Gamma:.4f}")
    print(f"  τ = 2η₂/(η₂+η₁) = {Tau:.4f}")
    print(f"  SWR = {SWR:.4f}")

    # Reflected/transmitted power
    R = abs(Gamma)**2
    T = 1 - R  # for normal incidence, power transmittance = 1 - R

    print(f"  Reflected power fraction: R = |Γ|² = {R:.4f} ({R*100:.2f}%)")
    print(f"  Transmitted power fraction: T = 1 - R = {T:.4f} ({T*100:.2f}%)")

    # Visualize standing wave in medium 1
    z = np.linspace(-1.0, 0.0, 300)
    k1 = 10.0  # normalized
    E_total = (np.exp(-1j * k1 * (z - 0)) +
               Gamma * np.exp(1j * k1 * (z - 0)))
    E_mag = np.abs(E_total)

    plt.figure(figsize=(10, 5))
    plt.plot(z * 100, E_mag, 'b-', lw=2)
    plt.axvline(x=0, color='k', ls='--', label='Interface (z=0)')
    plt.xlabel(r'Distance $z$ (cm)  [medium 1: air]')
    plt.ylabel(r'$|E|/|E_i|$')
    plt.title(rf'Example 8-7: Standing Wave in Medium 1 (Γ = {Gamma:.3f})')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch08_standing_wave.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Figure saved: ch08_standing_wave.png")
    return Gamma, Tau

# =============================================================================
# Section 8-9: Snell's Laws, Critical Angle, Brewster Angle
# =============================================================================

def example_8_9_snells_law():
    """
    Snell's law, critical angle, and Brewster angle.
    n1*sin(theta_i) = n2*sin(theta_t)
    Critical angle (total internal reflection): theta_c = arcsin(n2/n1)
    Brewster angle: theta_B = arctan(n2/n1)  [for parallel polarization]
    """
    eps_r1 = 1.0    # air
    eps_r2 = 2.1    # denser medium
    n1 = np.sqrt(eps_r1)
    n2 = np.sqrt(eps_r2)

    theta_i = np.linspace(0, 90, 500)
    theta_t = np.degrees(np.arcsin(n1 / n2 * np.sin(np.radians(theta_i))))

    # Critical angle
    theta_c = np.degrees(np.arcsin(n2 / n1)) if n2 < n1 else 90.0
    # Brewster angle (parallel polarization)
    theta_B = np.degrees(np.arctan(n2 / n1))

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax = axes[0]
    ax.plot(theta_i, theta_t, 'b-', lw=2)
    ax.plot(theta_i, theta_i, 'k--', lw=1, alpha=0.5, label='θ_t = θ_i (if n2=n1)')
    if eps_r1 > eps_r2:
        ax.axvline(x=theta_c, color='r', ls='--', alpha=0.7,
                   label=f'θ_c = {theta_c:.1f}°')
    ax.set_xlabel(r'Angle of incidence $\theta_i$ (°)')
    ax.set_ylabel(r'Angle of refraction $\theta_t$ (°)')
    ax.set_title(f"Example 8-9: Snell's Law — n₁={n1}, n₂={n2}")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Reflectance for perpendicular and parallel polarization
    theta_i_plot = np.linspace(0, 89, 400)
    sin_i = np.sin(np.radians(theta_i_plot))
    cos_i = np.cos(np.radians(theta_i_plot))
    sin_t = n1 / n2 * sin_i
    cos_t = np.sqrt(1 - sin_t**2 + 0j)

    # R_perp = |(n1*cos_i - n2*cos_t)/(n1*cos_i + n2*cos_t)|^2
    R_perp = np.abs((n1 * cos_i - n2 * cos_t) / (n1 * cos_i + n2 * cos_t))**2
    # R_par = |(n2*cos_i - n1*cos_t)/(n2*cos_i + n1*cos_t)|^2
    R_par = np.abs((n2 * cos_i - n1 * cos_t) / (n2 * cos_i + n1 * cos_t))**2

    ax = axes[1]
    ax.plot(theta_i_plot, R_perp, 'b-', lw=2, label=r'$\perp$ (S) polarization')
    ax.plot(theta_i_plot, R_par, 'r-', lw=2, label=r'$\parallel$ (P) polarization')
    ax.axhline(y=0, color='k', lw=0.5)
    ax.axhline(y=1, color='k', lw=0.5)
    ax.axvline(x=theta_B, color='g', ls='--', alpha=0.7,
               label=f'Brewster θ_B = {theta_B:.1f}°')
    ax.set_xlabel(r'Angle of incidence $\theta_i$ (°)')
    ax.set_ylabel('Reflectance $R$')
    ax.set_title(rf'Example 8-9: Reflectance at Air→Glass ($n_1$={n1}, $n_2$={n2})')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 89)
    ax.set_ylim(0, 1.05)

    plt.suptitle(rf'Example 8-9: Snell''s Law, Critical Angle & Brewster Angle', fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch08_snells_law.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nSection 8-9: Snell's Law and Related Phenomena")
    print(f"  n₁ = {n1}, n₂ = {n2}")
    print(f"  Critical angle θ_c = {theta_c:.2f}° (total internal reflection if n₁>n₂)")
    print(f"  Brewster angle θ_B = arctan(n₂/n₁) = {theta_B:.2f}° (R_par = 0)")
    print(f"  At θ_B, reflected wave is purely S-polarized (perpendicular)")
    print(f"  Figure saved: ch08_snells_law.png")
    return theta_c, theta_B

# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Chapter 8 — Plane Electromagnetic Waves (Cheng, 2nd Ed.)")
    print("=" * 60)

    example_8_2_plane_wave_properties()
    example_8_2_polarization()
    example_8_3_skin_depth()
    example_8_4_poynting_vector()
    example_8_7_normal_incidence()
    example_8_9_snells_law()

    print("\n" + "=" * 60)
    print("All Chapter 8 examples completed.")
    print("=" * 60)
