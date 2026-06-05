"""
Kraus 'Antennas' 2nd Edition — Chapter 13: Helical Antennas
===========================================================
Key topics:
- Sec 13-2 to 13-4: Monofilar axial-mode helix — circumference C = π·D ≈ λ
  The axial-mode helix operates when C ≈ λ (circumference ≈ wavelength).
  Spacing S is typically S = (0.2 to 0.3)·λ.
  The beam is end-fire along the helix axis.
  Directivity: D ≈ 12·C²/λ²  (for N turns, D ~ N when in phase)
  HPBW ≈ 52°/(C/λ)·√(S/λ)   (Kraus empirical formula)
  Axial ratio (AR) of circularly polarized field: AR = |1 - S/λ| · |e^(jψ)|
- Sec 13-5: Normal-mode helix (Wheeler coil design)
  Pattern: broad bidirectional, sin²(θ) like a short dipole
  Bandwidth: narrow, determined by L and C
- Sec 13-6 to 13-9: Practical helical feeds — design procedure:
  Given frequency f (GHz), desired gain G (dBi), choose:
    λ = c/f
    C ≈ λ  (for axial mode, typical range: 0.75λ to 1.05λ)
    S ≈ 0.225λ  (optimal spacing empirically)
    N ≈ G_dBi/11 + 1  (approximate number of turns for desired gain)
  Then check: D ≈ 12·N·(C/λ)²·cos²(α) where tan(α) = S/(π·D) is pitch angle.
- Sec 13-10/13-11: Helical antenna as a feed for reflectors and lens antennas.
- Sec 13-12: Multifilar axial-mode (Kilgus coil, Patton coil) helical antennas.
- Sec 13-13: Helical antenna as a parasitic element (helix-helix, polyrod).
- Sec 13-14: Tapered and other forms of axial-mode helical antennas.
- Sec 13-15: Monofilar axial-mode helical antenna as phase and frequency shifter.
- Sec 13-16 to 13-18: Monofilar and multifilar normal-mode helical antennas (Wheeler coil).
- Sec 13-19: Linear polarization with monofilar axial-mode helical antennas.
- Sec 13-20: Multifilar axial-mode (Kilgus coil and Patton coil) helical antennas.
- Example (Sec 13-?): Determine L, H-plane aperture, and flare angles for a helical feed.
  Given: f = 4 GHz, desired gain G = 12 dBi:
    λ = c/f = 7.5 cm
    C ≈ λ = 7.5 cm  → D = C/π ≈ 2.39 cm
    S ≈ 0.225λ ≈ 1.69 cm
    N ≈ G_dBi/11 + 1 ≈ 2.1  → N = 2 turns
    Pitch angle α = tan⁻¹(S/(π·D)) = tan⁻¹(1.69/(π·2.39)) ≈ tan⁻¹(0.225) ≈ 12.7°
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

c = constants.c
eps0 = constants.epsilon_0
mu0 = constants.mu_0
Z0 = np.sqrt(mu0 / eps0)

print("=" * 65)
print("Kraus Ch13 — Helical Antenna Design (Monofilar Axial Mode)")
print("=" * 65)
print(f"c = {c:.4e} m/s,  Z0 = {Z0:.4f} Ω")

# ═══════════════════════════════════════════════════════════════════════════
# Sec 13-3/13-4: Axial-mode helix design procedure
# Design: f=4 GHz, desired G=12 dBi
# ═══════════════════════════════════════════════════════════════════════════
def helix_design(f_GHz=4.0, G_dBi=12.0):
    """
    Kraus Sec 13-3/13-4: Monofilar axial-mode helix design.
    Given f (GHz) and desired gain G (dBi), compute D, S, N.
    """
    lam = c / (f_GHz * 1e9)
    G_lin = 10**(G_dBi/10)
    # C ≈ λ  (axial mode: C/λ ≈ 1)
    C = lam
    D = C / np.pi
    S = 0.225 * lam    # typical optimum spacing
    alpha = np.arctan2(S, np.pi * D)   # pitch angle
    # Approximate N from desired gain: D ≈ 12·N·(C/λ)²·cos²(α)
    # → N ≈ G_lin / (12·(C/λ)²·cos²(α)) = G_lin / (12·cos²(α))
    N_ideal = G_lin / (12 * np.cos(alpha)**2)
    N = int(np.ceil(N_ideal))
    # Actual directivity
    D_actual = 12 * N * (C/lam)**2 * np.cos(alpha)**2
    print(f"\n--- Sec 13-3/13-4: Helical antenna design ---")
    print(f"  f = {f_GHz} GHz  →  λ = {lam*1e3:.4f} cm")
    print(f"  Desired gain G = {G_dBi} dBi  (G_lin = {G_lin:.2f})")
    print(f"  Circumference C ≈ λ = {C*1e3:.4f} cm")
    print(f"  Diameter  D = C/π = {D*1e3:.4f} cm")
    print(f"  Spacing   S = 0.225λ = {S*1e3:.4f} cm")
    print(f"  Pitch angle α = tan⁻¹(S/(π·D)) = {np.degrees(alpha):.2f}°")
    print(f"  Estimated N ≈ {N_ideal:.2f}  →  N = {N} turns")
    print(f"  Actual directivity D ≈ {D_actual:.1f}  ({10*np.log10(D_actual+1e-12):.1f} dBi)")
    return D, S, N, alpha, lam

D_h, S_h, N_h, alpha_h, lam_h = helix_design(4.0, 12.0)

# ═══════════════════════════════════════════════════════════════════════════
# Plot pattern for 2-turn and 4-turn helices at f=4 GHz (Sec 13-4)
# Array factor: AF(θ) = sin(N·ψ/2) / sin(ψ/2)  with ψ = β·S·cosθ + α_rel
# For axial mode: α_rel = −β·S  (progressive phase to give end-fire)
# ═══════════════════════════════════════════════════════════════════════════
def plot_helix_patterns():
    beta = 2*np.pi / lam_h
    theta = np.linspace(0, np.pi, 10801)
    fig, axes = plt.subplots(1, 2, subplot_kw={'projection':'polar'}, figsize=(14, 6))
    for ax, N_turns, label in zip(axes, [(2, "2 turns"), (4, "4 turns")]):
        # AF for axial-mode helix: ψ = β·S·cosθ − β·S = β·S·(cosθ − 1)
        # This gives end-fire at θ=0° (beam in +z direction).
        # More precisely: AF = sin(N·ψ/2)/sin(ψ/2) where ψ = β·S·cosθ + δ, δ = −β·S.
        psi = beta * S_h * np.cos(theta) - beta * S_h
        with np.errstate(divide='ignore', invalid='ignore'):
            AF = np.abs(np.sin(N_turns*psi/2) / np.sin(psi/2))
        AF = np.where(np.isfinite(AF), AF, N_turns)
        AF = AF / np.max(AF)
        ax.plot(theta, AF, 'b-', lw=2)
        ax.fill(theta, AF, alpha=0.15)
        ax.set_ylim(0, 1.3)
        D_est = 12 * N_turns * (S_h*1e3)**2  # approximate
        ax.set_title(f"Kraus Ch13 — Axial-Mode Helix\n{label}, D={D_h*1e3:.2f}cm, S={S_h*1e3:.2f}cm\nD≈{10*np.log10(12*N_turns*(lam_h/lam_h)**2*np.cos(alpha_h)**2+1e-12):.1f} dBi", fontsize=9)
    plt.suptitle("Kraus Ch13 — Monofilar Axial-Mode Helical Antenna (Sec 13-3/13-4)", fontsize=12, fontweight='bold')
    plt.tight_layout()
    out = "/home/ubuntu/.openclaw/workspace/textbooks/kraus/code/kraus_ch13_helix_design.png"
    plt.savefig(out, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\n✓ Saved: {out}")

plot_helix_patterns()

# ═══════════════════════════════════════════════════════════════════════════
# Sec 13-6/13-7: Wide-beam conical (biconical) helix — axial ratio
# For a helix with N turns and pitch angle α, the axial ratio at boresight is:
# AR ≈ |sin(ΔΦ/2)| / |cos(ΔΦ/2)|  where ΔΦ = π − β·S·(1−cosθ) ≈ 2πS/λ for end-fire.
# For circular polarization: AR = 0 dB at θ=0° when phase difference is π/2.
# ═══════════════════════════════════════════════════════════════════════════
def helix_axial_ratio():
    """
    Kraus Sec 13-5/13-6: Axial ratio for circular polarization.
    The axial-mode helix produces circular polarization (CP).
    AR = |tan(ΔΦ/2)| where ΔΦ = phase difference between E_θ and E_φ components.
    For ideal CP: AR = 1 (0 dB).
    """
    print("\n--- Sec 13-5/13-6: Axial ratio for CP helix ---")
    print("  For axial-mode helix, the two field components E_θ and E_φ are")
    print("  nearly in quadrature (90° phase difference) at boresight (θ=0°).")
    print("  The axial ratio AR is ideally 0 dB (circular polarization).")
    print("  Off-boresight, AR degrades and becomes elliptical.")
    print("  Practical AR for well-designed helix: 1 to 3 dB (good CP)")
    return

helix_axial_ratio()

print("\n✓ Chapter 13 code complete.")
