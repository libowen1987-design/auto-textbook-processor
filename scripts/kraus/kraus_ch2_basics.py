"""
Kraus 'Antennas' 2nd Edition — Chapter 2: Basic Antenna Concepts
===============================================================
Key topics:
- Sec 2-3: Radiation resistance — power radiated by antenna
- Sec 2-4: Antenna input impedance Z_in = R + jX
  R = R_rad + R_loss   (radiation resistance + loss resistance)
- Sec 2-5: Beam area (beam solid angle) Ω_A
  For isotropic: Ω_A = 4π sr. For directional: Ω_A < 4π.
- Sec 2-6: Directivity D = 4π / Ω_A
  Also D = 10·log10(D_lin) in dBi.
- Sec 2-7: Beam efficiency η_B = Ω_M / Ω_A  (main-lobe solid angle / total beam area)
- Sec 2-8: Directivity pattern theorem: D = 4π / (∫∫P(θ,φ)/P_max·sinθ dθ dφ)
- Sec 2-9: Gain G = G_0·η_rad  (directivity × efficiency)
  G_dBi = D_dBi + 10·log10(η_rad)
- Sec 2-10/2-11: Radiation efficiency η_rad = R_rad / (R_rad + R_loss)
- Sec 2-12: Relative power pattern P(θ,φ)/P_max and normalized field pattern
- Sec 2-13/2-14: HPBW (half-power beam width) and FBR (front-to-back ratio)
- Sec 2-16: Effective aperture A_e = (D·λ²)/(4π)  [m²]
- Sec 2-17: Friis transmission formula: P_r = P_t·G_t·G_r·(λ/(4πR))²
- Sec 2-18: Radar equation: P_r = P_t·G_t·σ·A_e/(4π·R⁴)
- Sec 2-19: Polarization mismatch loss factor k_p
- Sec 2-20: System noise temperature T_s and G/T ratio
- Sec 2-36: Polarization — Poincaré sphere representation.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

c = constants.c
eps0 = constants.epsilon_0
mu0 = constants.mu_0
Z0 = np.sqrt(mu0 / eps0)

print("=" * 65)
print("Kraus Ch2 — Basic Antenna Parameters")
print("=" * 65)
print(f"c = {c:.4e} m/s,  Z0 = {Z0:.4f} Ω")

# ═══════════════════════════════════════════════════════════════════════════
# Sec 2-5/2-6: Beam area and directivity for isotropic vs directional antenna
# Ω_A (isotropic) = 4π sr
# D = 4π / Ω_A  →  D_isotropic = 1
# ═══════════════════════════════════════════════════════════════════════════
def beam_area_directivity():
    print("\n--- Sec 2-5/2-6: Beam Area and Directivity ---")
    omega_isotropic = 4 * np.pi   # sr
    D_iso = 4 * np.pi / omega_isotropic
    print(f"  Isotropic: Ω_A = {omega_isotropic:.4f} sr  →  D = {D_iso:.1f} (0 dBi)")
    # Directional: say HPBW=30° in both planes → approximate Ω_A ≈ Ω_E·Ω_H
    # Ω_E ≈ (π/180)·HPBW_E in radians? No: for small angles Ω ≈ (HPBW_rad)²
    # Better: for a pencil beam with HPBW_E=30°, HPBW_H=30°:
    #   Ω_A ≈ (π/180·30)² = (0.5236)² = 0.274 sr  →  D = 4π/0.274 ≈ 45.8 (16.6 dBi)
    HPBW_E_deg, HPBW_H_deg = 30.0, 30.0
    omega_main = np.radians(HPBW_E_deg) * np.radians(HPBW_H_deg)
    D_dir = 4 * np.pi / omega_main
    print(f"  Directional (HPBW_E={HPBW_E_deg}°, HPBW_H={HPBW_H_deg}°): Ω_A≈{omega_main:.3f} sr  →  D≈{D_dir:.1f} ({10*np.log10(D_dir):.1f} dBi)")
    return omega_isotropic, D_dir

omega_iso, D_dir = beam_area_directivity()

# ═══════════════════════════════════════════════════════════════════════════
# Sec 2-7: Beam efficiency η_B = Ω_M / Ω_A
# Example: main-lobe Ω_M = 0.1 sr, total Ω_A = 0.5 sr  →  η_B = 0.2 (20%)
# ═══════════════════════════════════════════════════════════════════════════
def beam_efficiency():
    print("\n--- Sec 2-7: Beam Efficiency ---")
    Omega_M_vals = [0.1, 0.2, 0.5]
    Omega_A = 1.0  # sr
    for omegam in Omega_M_vals:
        eta_b = omegam / Omega_A
        print(f"  Ω_M = {omegam:.1f} sr, Ω_A = {Omega_A:.1f} sr  →  η_B = {eta_b:.2f} ({eta_b*100:.0f}%)")
    return

beam_efficiency()

# ═══════════════════════════════════════════════════════════════════════════
# Sec 2-9/2-10: Gain and radiation efficiency
# G = D × η_rad   with η_rad = R_rad / (R_rad + R_loss)
# Example: R_rad = 73 Ω (half-wave dipole), R_loss = 7 Ω  →  η_rad = 73/80 = 91.3%
#   D_halfwave = 1.64 (2.15 dBi)  →  G = 1.64×0.913 = 1.50 (1.76 dBi)
# ═══════════════════════════════════════════════════════════════════════════
def gain_radiation_efficiency():
    print("\n--- Sec 2-9/2-10: Gain and Radiation Efficiency ---")
    R_rad_vals = [73.0, 50.0, 30.0]   # various antenna types
    R_loss = 7.0
    for R_r in R_rad_vals:
        eta_rad = R_r / (R_r + R_loss)
        D_lin = 1.64  # half-wave dipole directivity (linear)
        D_dBi = 10*np.log10(D_lin)
        G_lin = D_lin * eta_rad
        G_dBi = 10*np.log10(G_lin + 1e-12)
        print(f"  R_rad = {R_r:.0f} Ω, R_loss = {R_loss:.0f} Ω  →  η_rad = {eta_rad*100:.1f}%")
        print(f"    D = {D_lin:.2f} ({D_dBi:.2f} dBi)  →  G = {G_lin:.3f} ({G_dBi:.2f} dBi)")
    return

gain_radiation_efficiency()

# ═══════════════════════════════════════════════════════════════════════════
# Sec 2-16: Effective aperture A_e = (D·λ²)/(4π)
# Example: D=10 (10 dBi), f=10 GHz (λ=3 cm)  →  A_e = 10×(0.03)²/(4π) = 7.16e-3 m²
# ═══════════════════════════════════════════════════════════════════════════
def effective_aperture():
    print("\n--- Sec 2-16: Effective Aperture A_e = D·λ²/(4π) ---")
    for f_GHz in [2.45, 5.8, 10.0, 24.0]:
        lam = c / (f_GHz * 1e9)
        for D_dBi in [0.0, 10.0, 20.0, 30.0]:
            D_lin = 10**(D_dBi/10)
            A_e = D_lin * lam**2 / (4*np.pi)
            print(f"  f = {f_GHz:5.1f} GHz, λ = {lam*1e2:.2f} cm, D = {D_dBi:3.0f} dBi  →  A_e = {A_e*1e4:.4f} cm²")
    return

effective_aperture()

# ═══════════════════════════════════════════════════════════════════════════
# Sec 2-17: Friis transmission formula
# P_r = P_t · G_t · G_r · (λ/(4πR))²
# Example: P_t=1W, G_t=10 dBi, G_r=10 dBi, f=5.8 GHz, R=1000m
#   λ = c/f = 5.17 cm, G_lin=10, loss_factor = (λ/(4πR))²
#   P_r = 1×10×10×(0.0517/(4π×1000))² = 100×(4.11e-6)² = 1.69e-9 W = -58 dBm
# ═══════════════════════════════════════════════════════════════════════════
def friis_transmission():
    print("\n--- Sec 2-17: Friis Transmission Formula ---")
    P_t_dBm = 20.0    # 100 mW = 20 dBm
    G_t_dBi = 15.0    # directional antenna gain
    G_r_dBi = 15.0
    f_GHz = 5.8
    R_km = 10.0
    lam = c / (f_GHz * 1e9)
    R = R_km * 1000.0
    G_t_lin = 10**(G_t_dBi/10)
    G_r_lin = 10**(G_r_dBi/10)
    loss_factor = (lam / (4*np.pi*R))**2
    P_r_lin = (10**((P_t_dBm-30)/10)) * G_t_lin * G_r_lin * loss_factor
    P_r_dBm = 10*np.log10(P_r_lin*1e3)
    print(f"  P_t = {P_t_dBm:.0f} dBm, G_t = {G_t_dBi:.0f} dBi, G_r = {G_r_dBi:.0f} dBi")
    print(f"  f = {f_GHz} GHz  →  λ = {lam*1e2:.2f} cm,  R = {R_km:.0f} km")
    print(f"  λ/(4πR) = {lam/(4*np.pi*R):.4e}")
    print(f"  P_r = {P_r_lin*1e6:.4f} μW = {P_r_dBm:.2f} dBm")
    return

friis_transmission()

# ═══════════════════════════════════════════════════════════════════════════
# Sec 2-18: Radar equation
# P_r = P_t·G_t·σ·A_e / (4π·R⁴)   with A_e = G·λ²/(4π)
# → P_r = P_t·G_t·σ·G·λ² / (16π²·R⁴)
# Example: P_t=1 MW, G=40 dBi, σ=1 m² (Boeing 737), R=100 km, f=10 GHz
#   λ=3 cm, G_lin=10^4=10000, P_r = 1e6×10000×1×10000×(0.03)²/(16π²×(1e5)⁴)
#   = 1e6×1e4×1×1e4×9e-4 / (16π²×1e20) = 9e13 / (1.58e21) = 5.7e-8 W = -72 dBm
# ═══════════════════════════════════════════════════════════════════════════
def radar_equation():
    print("\n--- Sec 2-18: Radar Equation ---")
    P_t_W = 1e6      # 1 MW
    G_dBi = 40.0     # 40 dBi (large dish)
    sigma_m2 = 1.0   # 1 m² (small aircraft)
    R_km = 100.0
    f_GHz = 10.0
    lam = c / (f_GHz*1e9)
    R = R_km * 1000.0
    G_lin = 10**(G_dBi/10)
    A_e = G_lin * lam**2 / (4*np.pi)
    P_r = P_t_W * G_lin * sigma_m2 * A_e / (4*np.pi * R**4)
    print(f"  P_t = {P_t_W:.0e} W, G = {G_dBi:.0f} dBi ({G_lin:.0e}), σ = {sigma_m2:.0f} m²")
    print(f"  f = {f_GHz} GHz, λ = {lam*1e2:.2f} cm, R = {R_km:.0f} km")
    print(f"  λ/(4πR)² = {(lam/(4*np.pi*R))**2:.4e}")
    print(f"  P_r = {P_r*1e12:.4f} pW = {10*np.log10(P_r/1e-3):.1f} dBm")
    return

radar_equation()

# ═══════════════════════════════════════════════════════════════════════════
# Sec 2-36: Polarization — Poincaré sphere
# Represent polarization states on unit sphere.
# Linear (θ=0° or 90°): poles of sphere. Circular (RHCP/LHCP): equator.
# Elliptical: anywhere on sphere.
# Axial ratio AR = |E_major/E_minor| = tan(β) where β = arctan(b/a)
# ═══════════════════════════════════════════════════════════════════════════
def poincare_sphere():
    print("\n--- Sec 2-36: Poincaré Sphere — Polarization States ---")
    print("  Linear (0°):     (S1=1, S2=0, S3=0)")
    print("  Linear (90°):     (S1=-1, S2=0, S3=0)")
    print("  Linear (45°):     (S1=0, S2=1, S3=0)")
    print("  RHCP:             (S1=0, S2=0, S3=1)  [right-hand circular]")
    print("  LHCP:             (S1=0, S2=0, S3=-1) [left-hand circular]")
    print("  Elliptical:       intermediate points on sphere")
    # Show a few polarization states and their Stokes parameters
    import numpy as np
    cases = ["Linear 0°", "Linear 90°", "Linear 45°", "RHCP", "LHCP", "Elliptical 45° AR=3"]
    S1 = [1, -1, 0, 0, 0, 0]
    S2 = [0, 0, 1, 0, 0, 0.8]
    S3 = [0, 0, 0, 1, -1, 0.6]
    print(f"\n{'Polarization':<20} {'S1':>8} {'S2':>8} {'S3':>8}")
    for name, s1, s2, s3 in zip(cases, S1, S2, S3):
        print(f"  {name:<20} {s1:8.2f} {s2:8.2f} {s3:8.2f}")
    return

poincare_sphere()

# Plot directivity vs beam solid angle (fundamental limit)
def plot_D_vs_omega():
    omega = np.logspace(-2, 1, 101)  # 0.01 to 10 sr
    D = 4*np.pi / omega
    plt.figure(figsize=(9, 5))
    plt.loglog(omega, D, 'b-', lw=2)
    plt.xlabel("Beam solid angle Ω_A (sr)", fontsize=12)
    plt.ylabel("Directivity D (linear)", fontsize=12)
    plt.title("Kraus Ch2 — Directivity vs Beam Solid Angle: D = 4π/Ω_A", fontsize=12, fontweight='bold')
    plt.grid(True, which='both', alpha=0.3)
    plt.axhline(1, color='gray', lw=1, ls='--', label='Isotropic (D=1, 0 dBi)')
    plt.axvline(4*np.pi, color='gray', lw=1, ls=':', label='Isotropic beam area (4π sr)')
    plt.legend()
    out = "/home/ubuntu/.openclaw/workspace/textbooks/kraus/code/kraus_ch2_directivity.png"
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\n✓ Saved: {out}")

plot_D_vs_omega()

print("\n✓ Chapter 2 code complete.")