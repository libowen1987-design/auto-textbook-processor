"""
Kraus 'Antennas' 2nd Edition — Chapter 9: Stub and Microstrip Antennas
======================================================================
Key topics:
- Sec 9-3: Stub input impedance — short-circuited Z_in=jZ0tan(βL), open-circuited Z_in=−jZ0cot(βL)
- Sec 9-4/9-5: Single-stub matching (example: Z_L=100+j50Ω, Z0=50Ω → find d, L_stub)
- Sec 9-6 to 9-10: Rectangular microstrip (patch) antenna
  L ≈ λ/(2√ε_eff) (TM010 resonance), W ≈ λ/(2√ε_r)
  ε_eff = (ε_r+1)/2 + (ε_r-1)/2/√(1+12h/W)
  R_in ≈ 90·(W/L)²/√ε_eff  Ω at resonance
  BW (VSWR≤2) ≈ (h/λ0)·(W/L)·√ε_eff/(ε_eff-1) (fractional)
- Sec 9-11: Circular microstrip (TM110 mode): f_r = 1.8412·c/(2π·a·√ε_eff)
- Example: f=2.45 GHz, ε_r=2.2, h=1.59 mm → L≈30mm, W≈38mm, R_in≈30Ω
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
c = constants.c;  Z0 = np.sqrt(constants.mu_0/constants.epsilon_0)

print("=" * 60)
print("Kraus Ch9 — Stub and Microstrip (Patch) Antennas")
print("=" * 60)

# Stub impedance locus
L_vals = np.linspace(0, 1.0, 1001)
Z_sc = 1j*Z0*np.tan(2*np.pi*L_vals)
Z_oc = -1j*Z0/np.tan(2*np.pi*L_vals)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
stub_data = [(Z_sc, "Short-circuited stub"), (Z_oc, "Open-circuited stub")]
for ax_obj, (Z, name) in zip(axes.flat, stub_data):
    ax_obj.plot(Z.real/Z0, Z.imag/Z0, 'b-', lw=1.5)
    ax_obj.set_xlim(-3, 3); ax_obj.set_ylim(-3, 3)
    ax_obj.axhline(0, color='k', lw=0.5); ax_obj.axvline(0, color='k', lw=0.5)
    ax_obj.set_xlabel("Re(Z)/Z0"); ax_obj.set_ylabel("Im(Z)/Z0")
    ax_obj.set_aspect('equal'); ax_obj.grid(True, alpha=0.3)
    ax_obj.set_title(f"Kraus Ch9 — {name} Stub Impedance\nL=0 to λ (Sec 9-3)", fontsize=10)
plt.suptitle("Kraus Ch9 — Transmission-Line Stub Reactance", fontsize=12, fontweight='bold')
plt.tight_layout()
out = "/home/ubuntu/.openclaw/workspace/textbooks/kraus/code/kraus_ch9_stub.png"
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f"✓ Saved: {out}")

# Microstrip patch design
def patch_design(f_GHz=2.45, eps_r=2.2, h_mm=1.59):
    h = h_mm*1e-3;  lam0 = c/(f_GHz*1e9)
    W = lam0/(2*np.sqrt(eps_r))
    eps_eff = (eps_r+1)/2 + (eps_r-1)/2/np.sqrt(1+12*h/W)
    L0 = lam0/(2*np.sqrt(eps_eff))
    Delta_L = 0.412*h*(eps_eff+0.3)/(eps_eff-0.258)*(W/h+0.264)/(W/h+0.8)
    L = L0 - 2*Delta_L
    R_in = 90*(W/L)**2/np.sqrt(eps_eff)
    f_actual = c/(2*L*np.sqrt(eps_eff))
    print(f"\n--- Sec 9-6/9-10: Microstrip patch design ---")
    print(f"  f={f_GHz}GHz, ε_r={eps_r}, h={h_mm}mm → λ0={lam0*1e3:.2f}mm")
    print(f"  W={W*1e3:.2f}mm, L={L*1e3:.2f}mm (after fringe correction)")
    print(f"  ε_eff={eps_eff:.4f}, R_in≈{R_in:.1f}Ω, f_r={f_actual/1e9:.4f}GHz")
    return L, W, eps_eff, lam0

L, W, eps_eff, lam0 = patch_design(2.45, 2.2, 1.59)

# Patch pattern (E- and H-plane)
theta = np.linspace(0, np.pi, 7201)
F_E = np.abs(np.cos(np.pi*W/lam0*np.sin(theta)))/(np.sin(theta)+1e-12)
F_H = np.abs(np.cos(np.pi*L/lam0*np.sin(theta)))/(np.sin(theta)+1e-12)
F_E /= np.max(F_E);  F_H /= np.max(F_H)

fig, axes = plt.subplots(1, 2, subplot_kw={'projection':'polar'}, figsize=(13,6))
axes[0].plot(theta, F_E, 'b-', lw=2); axes[0].fill(theta, F_E, alpha=0.15)
axes[0].set_ylim(0,1.3); axes[0].set_title(f"E-plane (W={W*1e3:.1f}mm)\nSec 9-9", fontsize=9)
axes[1].plot(theta, F_H, 'r-', lw=2); axes[1].fill(theta, F_H, alpha=0.15, color='red')
axes[1].set_ylim(0,1.3); axes[1].set_title(f"H-plane (L={L*1e3:.1f}mm)\nSec 9-9", fontsize=9)
plt.suptitle("Kraus Ch9 — Microstrip Patch Pattern (Sec 9-9)", fontsize=12, fontweight='bold')
plt.tight_layout()
out2 = "/home/ubuntu/.openclaw/workspace/textbooks/kraus/code/kraus_ch9_patch.png"
plt.savefig(out2, dpi=150, bbox_inches='tight')
plt.close()
print(f"✓ Saved: {out2}")

print("\n✓ Chapter 9 code complete.")