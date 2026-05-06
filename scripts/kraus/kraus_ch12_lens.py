"""
Kraus 'Antennas' 2nd Edition — Chapter 12: Lens Antennas
========================================================
Key topics:
- Sec 12-2 to 12-4: Biconvex dielectric lens (zoned or unzoned)
  t = 2R(n-1)/n,  f = R/(2(n-1)),  n = √ε_r
- Sec 12-5 to 12-7: Zoned (Fresnel) lens — step zones to reduce thickness
  r_k = √(2kλf + k²λ²) ≈ √(2kλf)
- Sec 12-8: Artificial dielectric lens (metal-plate, resistive-sheet)
  ε_eff = (λ/λ_g)² > 1
- Sec 12-9 to 12-12: E- and H-plane beam widths of lens:
  HPBW_E ≈ 58°/(D/λ), HPBW_H ≈ 67°/(D/λ) for elliptical lens
- Example: f=10 GHz, ε_r=2.56 (n=1.6), R=10 cm → t=7.5 cm, f=8.3 cm
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
c = constants.c

print("=" * 60)
print("Kraus Ch12 — Lens Antennas")
print("=" * 60)

# Biconvex dielectric lens
def lens_design(R_cm=10.0, eps_r=2.56):
    n = np.sqrt(eps_r)
    t = 2*R_cm*(n-1)/n
    f = R_cm/(2*(n-1))
    print(f"\n--- Sec 12-2/12-3: Biconvex dielectric lens ---")
    print(f"  R={R_cm}cm, ε_r={eps_r} → n={n:.3f}")
    print(f"  Center thickness t={t:.2f}cm, focal length f={f:.2f}cm")
    return t, f, n

t, f, n = lens_design(10.0, 2.56)

# Fresnel zones
def fresnel_zones(f_cm=20.0, lam_cm=10.0, N=6):
    r_k = [np.sqrt(2*k*lam_cm*f_cm + k**2*lam_cm**2) for k in range(1, N+1)]
    print(f"\n--- Sec 12-5/12-6: Fresnel lens zones ---")
    print(f"  f={f_cm}cm, λ={lam_cm}cm, N={N} zones")
    print(f"  r_k = {[f'{r:.2f}' for r in r_k]} cm")
    return r_k

r_k = fresnel_zones(20.0, 10.0, 6)

# Plot Fresnel lens zones
fig, ax = plt.subplots(figsize=(8, 8))
f_cm, lam_cm = 20.0, 10.0
for k in range(1, 8):
    r = np.sqrt(2*k*lam_cm*f_cm + k**2*lam_cm**2)
    circle = plt.Circle((0,0), r, fill=False, lw=1.5)
    ax.add_patch(circle)
    ax.text(r*0.87, 0.5, f'k={k}', fontsize=9)
ax.set_xlim(-25, 25); ax.set_ylim(-25, 25)
ax.set_xlabel("x (cm)"); ax.set_ylabel("y (cm)")
ax.set_title("Kraus Ch12 — Fresnel Lens Zones (Sec 12-5/12-6)", fontsize=11)
ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
out = "/home/ubuntu/.openclaw/workspace/textbooks/kraus/code/kraus_ch12_fresnel.png"
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f"✓ Saved: {out}")

# Beam widths
print("\n--- Sec 12-9/12-12: Lens antenna HPBW ---")
for D_lam in [5.0, 10.0, 20.0]:
    hpbw_E = 58.0/D_lam
    hpbw_H = 67.0/D_lam
    print(f"  D={D_lam}λ → HPBW_E≈{hpbw_E:.2f}°, HPBW_H≈{hpbw_H:.2f}°")

print("\n✓ Chapter 12 code complete.")