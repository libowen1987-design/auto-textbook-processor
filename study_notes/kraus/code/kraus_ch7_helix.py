"""
Kraus 'Antennas' 2nd Edition — Chapter 7: The Helical Antenna
=============================================================
Key topics:
- Sec 7-11/7-12: Monofilar axial-mode helix — C≈λ, end-fire, directivity D≈12NC²/λ²
- Sec 7-12a/7-12b: 4-element and 96-element arrays of helical feeds
- Sec 7-13: Helix as parasitic element
- Sec 7-15 to 7-19: Normal-mode helical antenna (Wheeler coil) — sin²(θ) pattern
- Sec 7-18: Monofilar axial-mode design formulas:
    D ≈ 12·N·C²/λ²  (for N≥3 turns, axial mode)
    HPBW ≈ 52°/(C/λ)·√(S/λ)
    Pitch angle α = tan⁻¹(S/(π·D_helix))
- Sec 7-19: Practical design example — f=4 GHz, G=12 dBi
    C≈λ=7.5cm, D=2.4cm, S=1.7cm, N=3 turns, α≈12.7°
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
c = constants.c;  Z0 = np.sqrt(constants.mu_0/constants.epsilon_0)
lam = 1.0;  beta = 2*np.pi/lam

print("=" * 60)
print("Kraus Ch7 — Helical Antenna (Monofilar Axial & Normal Mode)")
print("=" * 60)

# ── Axial-mode helix: C≈λ, S≈0.225λ, N turns, end-fire pattern ────────────
def af_axial_helix(D_helix, S, N, theta_arr):
    C = np.pi*D_helix
    alpha = np.arctan2(S, np.pi*D_helix)  # pitch angle
    # Array factor for N turns: ψ = β·S·cosθ - β·S (end-fire progressive phase)
    psi = beta*S*np.cos(theta_arr) - beta*S
    with np.errstate(divide='ignore', invalid='ignore'):
        AF = np.abs(np.sin(N*psi/2)/np.sin(psi/2))
    AF = np.where(np.isfinite(AF), AF, N)
    return AF/N

theta = np.linspace(0, np.pi, 10801)
fig, axes = plt.subplots(1, 2, subplot_kw={'projection':'polar'}, figsize=(13, 6))
for ax, (D_h, S_h, N_h, lbl) in zip(axes, [
    (lam/np.pi, 0.225*lam, 4,  "4 turns, C=λ, S=0.225λ"),
    (lam/np.pi, 0.225*lam, 8,  "8 turns, C=λ, S=0.225λ")]):
    AF = af_axial_helix(D_h, S_h, N_h, theta)
    D_est = 12*N_h*(np.pi*D_h/lam)**2
    ax.plot(theta, AF, 'b-', lw=2); ax.fill(theta, AF, alpha=0.15)
    ax.set_ylim(0, 1.3)
    ax.set_title(f"Kraus Ch7 — Axial-mode helix\n{lbl}\nD≈{10*np.log10(D_est+1e-12):.1f} dBi", fontsize=9)
plt.suptitle("Kraus Ch7 — Monofilar Axial-Mode Helical Antenna (Sec 7-11/7-12)", fontsize=12, fontweight='bold')
plt.tight_layout()
out = "/home/ubuntu/.openclaw/workspace/textbooks/kraus/code/kraus_ch7_helix.png"
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f"✓ Saved: {out}")

# Design example (Sec 7-18)
print("\n--- Sec 7-18: Design example — f=4 GHz, G=12 dBi ---")
f_GHz = 4.0;  lam_m = c/(f_GHz*1e9);  G_dBi = 12.0
C = lam_m;  D_h = C/np.pi;  S = 0.225*lam_m
G_lin = 10**(G_dBi/10)
N_est = G_lin/(12*(C/lam_m)**2*np.cos(np.arctan2(S,np.pi*D_h))**2)
N = int(np.ceil(N_est))
alpha = np.degrees(np.arctan2(S, np.pi*D_h))
D_actual = 12*N*(C/lam_m)**2*np.cos(np.arctan2(S,np.pi*D_h))**2
print(f"  f={f_GHz} GHz → λ={lam_m*1e2:.2f} cm, C≈λ={C*1e2:.2f} cm")
print(f"  D={D_h*1e2:.2f} cm, S={S*1e2:.2f} cm, N={N} turns")
print(f"  Pitch angle α={alpha:.1f}°, D_actual={10*np.log10(D_actual+1e-12):.1f} dBi")

# Normal-mode (Wheeler coil) — broad, sin²θ pattern
theta_nm = np.linspace(0, np.pi, 1001)
P_nm = np.sin(theta_nm)**2
fig, ax = plt.subplots(subplot_kw={'projection':'polar'}, figsize=(7,6))
ax.plot(theta_nm, P_nm, 'g-', lw=2); ax.fill(theta_nm, P_nm, alpha=0.15, color='green')
ax.set_ylim(0, 1.3)
ax.set_title("Kraus Ch7 — Normal-Mode Helix (Wheeler coil)\nP(θ)∝sin²(θ), D≈1.5", fontsize=10)
plt.tight_layout()
out2 = "/home/ubuntu/.openclaw/workspace/textbooks/kraus/code/kraus_ch7_normal_mode.png"
plt.savefig(out2, dpi=150, bbox_inches='tight')
plt.close()
print(f"✓ Saved: {out2}")

print("\n✓ Chapter 7 code complete.")