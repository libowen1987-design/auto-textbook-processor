"""
Chapter 11 — Antennas and Radiating Systems
Field and Wave Electromagnetics, David K. Cheng (2nd Edition)

Examples covered:
- Section 11-2: Hertzian dipole (infinitesimal dipole) radiation pattern
- Section 11-2.1: Radiation resistance of Hertzian dipole
- Section 11-4.1: Half-wave dipole radiation pattern
- Section 11-5: Antenna array factor (two-element, uniform linear arrays)
- Section 11-3: Antenna parameters (directivity, gain, effective aperture)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import mu_0, epsilon_0, pi, c

# =============================================================================
# Section 11-2.1: Hertzian Dipole (Infinitesimal Dipole)
# =============================================================================

def example_11_2_hertzian_dipole():
    """
    Hertzian dipole (length l << lambda) with uniform current I_0.
    Far-field:
      E_theta = j * eta_0 * I_0 * l * sin(theta) * exp(-jkr) / (2*pi*r)
      H_phi = E_theta / eta_0
    Radiation pattern: |sin(theta)| — maximum at theta=90°, null at theta=0,180
    Radiation resistance: R_rad = 80*pi^2 * (l/lambda)^2  [ohms]
    """
    I_0 = 1.0     # Current, A
    l = 0.01      # dipole length, m (1 cm)
    f = 300e6     # 300 MHz

    lam = c / f
    k = 2 * pi / lam

    eta_0 = np.sqrt(mu_0 / epsilon_0)

    # Radiation resistance
    R_rad = 80 * pi**2 * (l / lam)**2

    # Far-field E_theta amplitude (normalized to r=1m)
    def E_theta(theta_deg, r=1.0):
        theta = np.radians(theta_deg)
        return np.abs(eta_0 * k * I_0 * l * np.sin(theta) / (2 * pi * r))

    # Polar radiation pattern
    theta = np.linspace(0, 360, 500)
    theta_rad = np.radians(theta)
    E_pattern = np.abs(np.sin(theta_rad))

    fig = plt.figure(figsize=(14, 6))

    # 1. Polar plot of radiation pattern
    ax = fig.add_subplot(121, projection='polar')
    ax.plot(theta_rad, E_pattern, 'b-', lw=2)
    ax.fill(theta_rad, E_pattern, alpha=0.2)
    ax.set_rmax(1.0)
    ax.set_rticks([0.25, 0.5, 0.75, 1.0])
    ax.set_rlabel_position(45)
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_title(r'Example 11-2: Hertzian Dipole — $|\sin\theta|$ Pattern', fontsize=11)

    # 2. 3D radiation intensity (U = r^2*P_rad/4pi)
    ax3d = fig.add_subplot(122, projection='3d')
    theta_3d = np.linspace(0.01, np.pi - 0.01, 30)
    phi_3d = np.linspace(0, 2*pi, 30)
    TH, PH = np.meshgrid(theta_3d, phi_3d)
    U = np.sin(TH)**2  # Relative radiation intensity

    X = U * np.sin(TH) * np.cos(PH)
    Y = U * np.sin(TH) * np.sin(PH)
    Z = U * np.cos(TH)

    ax3d.plot_surface(X, Y, Z, cmap='plasma', alpha=0.8, linewidth=0)
    ax3d.set_xlabel('X')
    ax3d.set_ylabel('Y')
    ax3d.set_zlabel('Z')
    ax3d.set_title('Example 11-2: 3D Radiation Pattern')

    plt.suptitle(rf'Example 11-2: Hertzian Dipole — $l$ = {l*100:.0f} cm, $f$ = {f*1e-6:.0f} MHz, $\lambda$ = {lam*100:.0f} cm',
                 fontsize=12)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch11_hertzian_dipole.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nSection 11-2: Hertzian Dipole")
    print(f"  l = {l*100:.0f} cm, f = {f*1e-6:.0f} MHz, λ = {lam*100:.2f} cm")
    print(f"  l/λ = {l/lam:.4f}")
    print(f"  R_rad = 80π²(l/λ)² = {R_rad:.4f} Ω")
    print(f"  Peak E_theta at r=1m: {E_theta(90):.4f} V/m")
    print(f"  Figure saved.")
    return R_rad

# =============================================================================
# Section 11-4.1: Half-Wave Dipole
# =============================================================================

def example_11_4_halfwave_dipole():
    """
    Half-wave dipole (l = lambda/2) with sinusoidal current distribution.
    Far-field E_theta = j*eta_0*I_0*cos(pi/2*cos(theta)) / (2*pi*r*sin(theta)^2)
    Directivity D = 1.64 (2.15 dBi)
    Input impedance Z_in ~ 73 + j42.5 ohms (off resonance ~ 67 - j0 at 0.49*lambda)
    """
    eta_0 = np.sqrt(mu_0 / epsilon_0)
    I_0 = 1.0

    def E_halfwave(theta_deg, r=1.0):
        """E_theta amplitude of half-wave dipole"""
        theta = np.radians(theta_deg)
        cos_term = np.cos(pi/2 * np.cos(theta))
        sin_term = np.sin(theta)
        # Avoid division by zero
        sin_term = np.where(np.abs(sin_term) < 1e-10, 1e-10, sin_term)
        return np.abs(eta_0 * I_0 / (2 * pi * r) * cos_term / sin_term)

    theta = np.linspace(0.1, 359.9, 500)
    E_pat = E_halfwave(theta)
    E_pat_norm = E_pat / np.max(E_pat)

    # Half-power beamwidth
    half_max = 1 / np.sqrt(2)
    above_half = np.where(E_pat_norm > half_max)[0]
    if len(above_half) > 0:
        hpbf = theta[above_half[-1]] - theta[above_half[0]]
    else:
        hpbf = None

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    ax = fig.add_subplot(121, projection='polar')
    theta_rad = np.radians(theta)
    ax.plot(theta_rad, E_pat_norm, 'b-', lw=2)
    ax.fill(theta_rad, E_pat_norm, alpha=0.2)
    ax.set_rmax(1.0)
    ax.set_rticks([0.25, 0.5, 0.75, 1.0])
    ax.set_rlabel_position(45)
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_title(r'Example 11-4.1: Half-Wave Dipole — Normalized Pattern')

    # E-plane pattern (linear)
    ax = axes[1]
    ax.plot(theta, E_pat_norm, 'b-', lw=2)
    ax.axhline(y=1/np.sqrt(2), color='r', ls='--', alpha=0.7,
               label=f'Half-power level = {1/np.sqrt(2):.3f}')
    if hpbf:
        ax.axvline(x=theta[above_half[0]], color='g', ls=':', alpha=0.7)
        ax.axvline(x=theta[above_half[-1]], color='g', ls=':', alpha=0.7,
                   label=f'HPBW ≈ {hpbf:.1f}°')
    ax.set_xlabel(r'Polar angle $\theta$ (degrees)')
    ax.set_ylabel(r'$|E|/|E_{\max}|$')
    ax.set_title(rf'Example 11-4.1: Half-Wave Dipole — Linear Pattern (D = 1.64, 2.15 dBi)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 180)
    ax.set_ylim(0, 1.05)

    plt.suptitle(r'Example 11-4.1: Half-Wave Dipole Radiation Pattern', fontsize=12)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch11_halfwave_dipole.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    # Directivity
    D = 1.64
    G = 0.95 * D  # assuming 95% efficiency
    lam = 0.1  # 10 cm (3 GHz)
    A_e = (lam**2 / (4*pi)) * D

    print(f"\nSection 11-4.1: Half-Wave Dipole")
    print(f"  Directivity D = {D:.2f} ({10*np.log10(D):.2f} dBi)")
    print(f"  Gain G ≈ η·D ≈ {G:.3f} ({10*np.log10(G):.2f} dBi)")
    print(f"  HPBW ≈ {hpbf:.1f}° (theoretical ~78°)")
    print(f"  Input impedance Z_in ≈ 73 + j42.5 Ω (off resonance)")
    print(f"  Effective aperture A_e = λ²D/(4π) = {A_e*1e4:.4f} cm²")
    print(f"  Figure saved.")
    return D

# =============================================================================
# Section 11-5: Antenna Array Factor
# =============================================================================

def example_11_5_array_factor():
    """
    N-element uniform linear array.
    Array Factor: AF = |sin(N*Psi/2) / sin(Psi/2)|
    where Psi = k*d*cos(theta) + psi (progressive phase)
    """
    k = 2 * pi       # normalized k
    d = 0.5          # d = lambda/2 spacing
    psi = 0          # no progressive phase (broadside)

    N_vals = [2, 4, 8]
    theta = np.linspace(0, 180, 1000)

    fig, axes = plt.subplots(1, 3, figsize=(15, 5), subplot_kw={'projection': 'polar'})

    colors = ['blue', 'red', 'green']

    for idx, N in enumerate(N_vals):
        ax = axes[idx]
        Psi = k * d * np.cos(np.radians(theta)) + psi
        AF = np.abs(np.sin(N * Psi / 2) / np.sin(Psi / 2 + 1e-12))
        AF_norm = AF / N  # normalize

        ax.plot(np.radians(theta), AF_norm, color=colors[idx], lw=2)
        ax.fill(np.radians(theta), AF_norm, alpha=0.1, color=colors[idx])
        ax.set_theta_zero_location('N')
        ax.set_theta_direction(-1)
        ax.set_title(f'{N}-Element Array\n(d=λ/2, broadside)', fontsize=11)
        ax.set_rmax(1.05)

    plt.suptitle(r'Example 11-5: Uniform Linear Array — Array Factor', fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch11_array_factor.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    # Also plot linear version for N=2 with different spacings
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    spacings = [0.25, 0.5, 1.0]  # in lambda units
    for idx, d_lam in enumerate(spacings):
        ax = axes[idx]
        for psi_val, label in [(0, 'Broadside (ψ=0)'), (-pi, 'Endfire (ψ=-kd)')]:
            Psi = k * d_lam * np.cos(np.radians(theta)) + psi_val
            AF = np.abs(np.sin(2 * Psi / 2) / np.sin(Psi / 2 + 1e-12))
            AF_norm = AF / 2
            ax.plot(theta, AF_norm, lw=2, label=label)

        ax.set_xlabel(r'Angle $\theta$ (degrees)')
        ax.set_ylabel('|AF| (normalized)')
        ax.set_title(f'2-Element Array, d = {d_lam}λ')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_xlim(0, 180)
        ax.set_ylim(0, 1.1)

    plt.suptitle(r'Example 11-5: 2-Element Array — Broadside vs Endfire', fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch11_2element_array.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nSection 11-5: Antenna Array Factor")
    print(f"  AF = |sin(N·Ψ/2)/sin(Ψ/2)|")
    print(f"  Ψ = k·d·cos(θ) + ψ")
    print(f"  For 2-element broadside (ψ=0, d=λ/2): main beam at θ=90°")
    print(f"  For 2-element endfire (ψ=-kd, d=λ/2): main beam at θ=0°")
    print(f"  Figure saved.")
    return None

# =============================================================================
# Section 11-3: Antenna Parameters
# =============================================================================

def example_11_3_antenna_parameters():
    """
    Compute key antenna parameters for a half-wave dipole.
    - Directivity D
    - Gain G = η·D
    - Effective aperture A_e = λ²·D/(4π)
    """
    D = 1.64
    eta_rad = 0.95  # radiation efficiency
    G = eta_rad * D

    f = 1e9   # 1 GHz
    lam = c / f

    A_e = lam**2 * D / (4 * pi)

    print(f"\nSection 11-3: Antenna Parameters")
    print(f"  f = {f*1e-9:.1f} GHz, λ = {lam*100:.2f} cm")
    print(f"  Directivity D = {D:.3f} ({10*np.log10(D):.2f} dBi)")
    print(f"  Gain G = η·D = {G:.3f} ({10*np.log10(G):.2f} dBi)")
    print(f"  Effective aperture A_e = λ²D/(4π) = {A_e*1e4:.4f} cm²")

    # Plot gain vs efficiency
    eta_range = np.linspace(0.1, 1.0, 100)
    G_range = eta_range * D

    plt.figure(figsize=(8, 5))
    plt.plot(eta_range * 100, 10*np.log10(G_range), 'b-', lw=2)
    plt.axhline(y=10*np.log10(D), color='r', ls='--', alpha=0.7,
               label=f'Perfect efficiency: {10*np.log10(D):.2f} dBi')
    plt.xlabel('Radiation Efficiency η (%)')
    plt.ylabel('Gain $G$ (dBi)')
    plt.title(rf'Example 11-3: Antenna Gain vs Efficiency ($D$ = {D:.2f})')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch11_antenna_gain.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Figure saved.")
    return G

# =============================================================================
# Section 11-7: Yagi-Uda Antenna (Simplified Pattern)
# =============================================================================

def example_11_7_yagi():
    """
    Simplified Yagi-Uda pattern (conceptual).
    A Yagi has a driven element, reflector, and directors.
    Directivity typically 7-15 dBi for 3-6 element arrays.
    """
    N_elements = 4  # 1 driven + 1 reflector + 2 directors
    D_yagi = 7.0    # approximate directivity for 4-element Yagi

    lam = 0.1   # 10 cm (3 GHz)
    A_e = lam**2 * D_yagi / (4 * pi)

    # Simulated pattern (simplified): cos^4(theta) beam in forward direction
    theta = np.linspace(-90, 90, 500)
    theta_rad = np.radians(theta)
    pattern = np.cos(theta_rad)**4
    pattern = pattern / pattern.max()

    plt.figure(figsize=(10, 5))
    plt.subplot(121, projection='polar')
    theta_full = np.linspace(-180, 180, 500)
    pattern_full = np.cos(np.radians(theta_full))**4
    pattern_full = np.where(np.abs(theta_full) < 90, pattern_full, pattern_full * 0.1)
    pattern_full = pattern_full / pattern_full.max()
    plt.polar(np.radians(theta_full), pattern_full, 'b-', lw=2)
    plt.title(r'Example 11-7: Yagi-Uda Pattern (4-element, simplified)')

    plt.subplot(122)
    plt.plot(theta, pattern, 'b-', lw=2)
    plt.xlabel(r'Angle $\theta$ (degrees)')
    plt.ylabel('Normalized Field')
    plt.title(f'Example 11-7: Yagi-Uda E-plane\n(D ≈ {D_yagi:.0f} dBi, HPBW ≈ 40°)')
    plt.grid(True, alpha=0.3)
    plt.xlim(-90, 90)
    plt.ylim(0, 1.05)

    plt.suptitle(r'Example 11-7: Yagi-Uda Antenna — Directional Pattern', fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch11_yagi_uda.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nSection 11-7: Yagi-Uda Antenna (Simplified)")
    print(f"  4-element Yagi: D ≈ {D_yagi:.0f} dBi")
    print(f"  HPBW ≈ 40°")
    print(f"  Effective aperture A_e = {A_e*1e4:.2f} cm²")
    print(f"  Figure saved.")
    return D_yagi

# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Chapter 11 — Antennas (Cheng, 2nd Ed.)")
    print("=" * 60)

    example_11_2_hertzian_dipole()
    example_11_4_halfwave_dipole()
    example_11_5_array_factor()
    example_11_3_antenna_parameters()
    example_11_7_yagi()

    print("\n" + "=" * 60)
    print("All Chapter 11 examples completed.")
    print("=" * 60)
