"""
Kraus 'Antennas' 2nd Edition — Chapter 5: The Linear Antenna (Dipole)
====================================================================
Key topics:
- Sec 5-2/5-3: Short dipole (Hertzian) — fields, radiation resistance
  E_θ = j·η₀·I₀·L·e^(-jβr)·sinθ / (2πr)
  H_φ = I₀·L·e^(-jβr)·sinθ / (4πr)
  R_r = 20π²·(L/λ)²  [Ω]
- Sec 5-5/5-6: Half-wave dipole — current distribution, input impedance
  I(z) = I₀·cos(βz), z from −λ/4 to λ/4
  Z_in ≈ 73 + j42.5 Ω  (below resonance), R_r ≈ 73 Ω at resonance
- Sec 5-7: Radiation resistance at a point NOT at current maximum
  R(d) = R_r·sin²(β·d)  (d = distance from current max)
- Sec 5-8: Thin linear antenna with uniform traveling wave
- Sec 5-9: Mutual impedance between two dipoles (Z_12 calculation)
- Sec 5-10: Folded dipole (λ/2) — input impedance multiplied by 4
  Z_in(folded) ≈ 4 × 73 = 292 Ω  (for 2-wire fold, 1:1 transformation)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

c = constants.c
eps0 = constants.epsilon_0
mu0 = constants.mu_0
Z0 = np.sqrt(mu0 / eps0)

print("=" * 65)
print("Kraus Ch5 — Linear Antenna: Short & Half-Wave Dipole")
print("=" * 65)
print(f"Z0 = {Z0:.4f} Ω,  c = {c:.4e} m/s")

# ── Sec 5-2: Short dipole far-field pattern ─────────────────────────────────
lam = 1.0
beta = 2*np.pi / lam
theta = np.linspace(0, np.pi, 3601)
E_theta = np.abs(np.sin(theta))    # normalized field pattern |sinθ|
P_theta = E_theta**2              # power pattern ∝ sin²θ

fig, axes = plt.subplots(1, 3, subplot_kw={'projection':'polar'}, figsize=(15, 5))
axes[0].plot(theta, E_theta, 'b-', lw=2); axes[0].fill(theta, E_theta, alpha=0.15)
axes[0].set_ylim(0,1.3); axes[0].set_title("Short dipole — |E_θ| field pattern\n(Sec 5-2)", fontsize=9)
axes[1].plot(theta, P_theta, 'r-', lw=2); axes[1].fill(theta, P_theta, alpha=0.15, color='red')
axes[1].set_ylim(0,1.3); axes[1].set_title("Short dipole — power pattern\n(Sec 5-3)", fontsize=9)

# ── Sec 5-5a: Half-wave dipole current distribution ─────────────────────────
z = np.linspace(-0.25, 0.25, 1001)   # in wavelengths
I_z = np.cos(2*np.pi * np.abs(z))   # I(z) = I0·cos(β|z|)
axes[2].plot(z, I_z, 'g-', lw=2)
axes[2].axvline(-0.25, color='k', lw=0.8, ls='--'); axes[2].axvline(0.25, color='k', lw=0.8, ls='--')
axes[2].set_xlabel("z / λ"); axes[2].set_ylabel("I(z)/I0"); axes[2].set_title("λ/2 dipole current dist.\n(Sec 5-5a)", fontsize=9)
axes[2].grid(True, alpha=0.3)
plt.suptitle("Kraus Ch5 — Short & Half-Wave Dipole (Sec 5-2 to 5-6)", fontsize=12, fontweight='bold')
plt.tight_layout()
out = "/home/ubuntu/.openclaw/workspace/textbooks/kraus/code/kraus_ch5_dipole.png"
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f"\n✓ Saved: {out}")

# ── Sec 5-3: Radiation resistance R_r = 20π²(L/λ)² ─────────────────────────
print("\n--- Sec 5-3: Radiation resistance of short dipole ---")
for L_lam in [0.01, 0.05, 0.1, 0.25, 0.5]:
    R_r = 20*np.pi**2 * L_lam**2
    print(f"  L/λ = {L_lam:.2f}  →  R_r = {R_r:.4f} Ω")

# ── Sec 5-6: Half-wave dipole impedance ────────────────────────────────────
print("\n--- Sec 5-6: Half-wave dipole input impedance ---")
print(f"  R_r ≈ 73 Ω  (radiation resistance at resonance)")
print(f"  X_r ≈ ±42.5 Ω  (depending on frequency below/above resonance)")
print(f"  Z_in ≈ 73 + j42.5 Ω  (typical, below resonance)")

# ── Sec 5-7: R(d) = R_r·sin²(βd) ──────────────────────────────────────────
print("\n--- Sec 5-7: Radiation resistance at distance d from current max ---")
R_r = 73.0
for d_lam in [0.0, 0.05, 0.1, 0.25, 0.5]:
    R = R_r * np.sin(2*np.pi*d_lam)**2
    print(f"  d/λ = {d_lam:.2f}  →  R(d) = {R:.4f} Ω")

# ── Sec 5-10: Folded dipole (2-wire λ/2) ───────────────────────────────────
print("\n--- Sec 5-10: Folded dipole (λ/2, 2-wire) ---")
Z_in_halfwave = 73.0
Z_in_folded = 4 * Z_in_halfwave   # transformation ratio (1:4) for 2-wire fold
print(f"  Z_in(folded) ≈ 4 × {Z_in_halfwave:.0f} = {Z_in_folded:.0f} Ω  (typical)")

# ── Sec 5-9: Mutual impedance Z_12 between two parallel dipoles ───────────
print("\n--- Sec 5-9: Mutual impedance (approximate) ---")
# For two λ/2 dipoles with center-to-center spacing d:
# Z_12 ≈ 73 - j45  Ω at d=λ/2 (from Kraus tables)
for d_lam in [0.25, 0.5, 0.75, 1.0]:
    # Approximate from Kraus tables (Sec 5-9):
    if d_lam == 0.25:
        Z12 = 73.0 - 44.5j
    elif d_lam == 0.5:
        Z12 = -12.5 - 30.0j
    elif d_lam == 0.75:
        Z12 = -4.0 - 20.0j
    else:
        Z12 = 1.0 - 13.0j
    print(f"  d/λ = {d_lam:.2f}  →  Z_12 ≈ {Z12:.1f} Ω")

print("\n✓ Chapter 5 code complete.")