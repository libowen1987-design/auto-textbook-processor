"""
Kraus 'Antennas' 2nd Edition — Chapter 10: Horn Antennas
========================================================
Key topics:
- Sec 10-2 to 10-5: Sectoral E-plane, H-plane, and pyramidal horns
- Sec 10-6/10-7: Optimum-gain pyramidal horn design
  For given frequency f and required gain G, compute aperture W_E, W_H:
    A_e = G·λ²/(4π) → W_E·W_H = A_e/η_ap (η_ap≈0.5 typical)
    Optimum horn length: L_opt ≈ (W_E)²/(8·λ)  [for E-plane], L_opt ≈ (W_H)²/(8·λ) [for H-plane]
  Flare angles: θ_E = tan⁻¹(W_E/(2L)), θ_H = tan⁻¹(W_H/(2L))
- Sec 10-11: HPBW_E ≈ 57°/(W_E/λ), HPBW_H ≈ 67°/(W_H/λ)
- Sec 10-13: Practical horn feeds for parabolic reflectors
  Example: f=10 GHz, G=15 dBi → λ=3cm, G_lin=31.6 → A_e≈0.071m²=710cm²
    W_E=W_H=√710≈26.6cm → L=26.6²/(8×3)≈29.5cm → θ_E=θ_H≈tan⁻¹(26.6/(2×29.5))≈24.2°
    HPBW_E≈57/(26.6/3)≈6.4°, HPBW_H≈67/(26.6/3)≈7.5°
- Sec 10-8/10-9: Conical and corrugated horns — dual-mode and商会mode for low sidelobes
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
c = constants.c;  Z0 = np.sqrt(constants.mu_0/constants.epsilon_0)

print("=" * 60)
print("Kraus Ch10 — Horn Antennas")
print("=" * 60)

# Example: f=10 GHz, G=15 dBi → pyramidal horn design
def horn_design(f_GHz=10.0, G_dBi=15.0):
    lam = c/(f_GHz*1e9)
    G_lin = 10**(G_dBi/10)
    A_e = G_lin*lam**2/(4*np.pi)
    eta_ap = 0.5
    W = np.sqrt(A_e/eta_ap)   # square aperture
    L_E = W**2/(8*lam)       # optimum length for E-plane
    L_H = W**2/(8*lam)       # same (square)
    theta_E = np.degrees(np.arctan(W/(2*L_E)))
    theta_H = np.degrees(np.arctan(W/(2*L_H)))
    HPBW_E = 57.0/(W/lam)
    HPBW_H = 67.0/(W/lam)
    print(f"\n--- Sec 10-6/10-7/10-11: Horn design for f={f_GHz}GHz, G={G_dBi}dBi ---")
    print(f"  λ={lam*1e2:.2f}cm, G_lin={G_lin:.2f}, A_e={A_e*1e4:.2f}cm²")
    print(f"  Square aperture W_E=W_H≈{W*1e2:.2f}cm, L≈{L_E*1e2:.2f}cm")
    print(f"  Flare angles θ_E≈{theta_E:.1f}°, θ_H≈{theta_H:.1f}°")
    print(f"  HPBW_E≈{HPBW_E:.1f}°, HPBW_H≈{HPBW_H:.1f}°")
    return W, L_E, HPBW_E, HPBW_H

W, L_E, HPBW_E, HPBW_H = horn_design(10.0, 15.0)

# Aperture illumination pattern (sinc for uniformly illuminated rectangular aperture)
def horn_pattern(W_lam, theta_deg):
    t = np.deg2rad(theta_deg)
    k_W = np.pi*W_lam
    F = np.abs(np.sin(k_W*np.sin(t))/(k_W*np.sin(t)+1e-12))
    return np.where(np.isfinite(F), F, 1.0)

theta_deg = np.linspace(-90, 90, 10801)
F_E = horn_pattern(W/lam, theta_deg)
F_H = horn_pattern(W/lam, theta_deg)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
for ax, F, label in zip(axes, [(F_E, f"E-plane (W={W*1e2:.1f}cm)"), (F_H, f"H-plane (W={W*1e2:.1f}cm)")]):
    ax.plot(theta_deg, F, 'b-', lw=2)
    ax.axhline(0.707, color='gray', lw=1, ls='--', label='-3 dB')
    ax.axvline(-HPBW_E/2, color='r', lw=1, ls=':', label=f'±HPBW/2')
    ax.axvline(HPBW_E/2, color='r', lw=1, ls=':')
    ax.set_xlabel("θ (deg)"); ax.set_ylabel("|F(θ)|")
    ax.set_title(f"Kraus Ch10 — Horn {label}\n(Sec 10-11)", fontsize=10)
    ax.legend(); ax.grid(True, alpha=0.3)
    ax.set_xlim(-90, 90); ax.set_ylim(0, 1.1)

plt.suptitle("Kraus Ch10 — Horn Antenna Aperture Patterns", fontsize=12, fontweight='bold')
plt.tight_layout()
out = "/home/ubuntu/.openclaw/workspace/textbooks/kraus/code/kraus_ch10_horn.png"
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f"\n✓ Saved: {out}")
print("\n✓ Chapter 10 code complete.")