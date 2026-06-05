"""
Kraus 'Antennas' 2nd Edition — Chapter 11: Reflector Antennas
==============================================================
Key topics:
- Sec 11-9/11-10: Paraboloid aperture efficiency
  η_illum = cos²(θ0)·10^(-0.1·Te), η_spill = 1 - sin²(θ0)·10^(-0.1·Te)
  θ0 = tan⁻¹(1/(4f/D)), Te = edge taper (dB)
- Sec 11-11/11-12: Cassegrain and Gregorian dual-reflector systems
- Sec 11-13/11-14: Offset-feed configurations (reduced blockage)
- Sec 11-15/11-16: Surface tolerance: ΔG/G ≈ -13.6·(σ/λ)²  (random RMS error σ)
- Sec 11-17: Noise temperature and G/T ratio for receiving systems
- Example: D=3m, f/D=0.4, Te=10dB → θ0=32.9°, η_illum=0.075, η_spill=0.91 → η_ap≈0.068
  → G≈{10log10(0.068*(π*3/0.03)²)}≈38dBi at 10 GHz
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
c = constants.c

print("=" * 60)
print("Kraus Ch11 — Reflector Antennas (Paraboloid)")
print("=" * 60)

# Aperture efficiency vs f/D and edge taper
def reflector_efficiency(f_D, Te_dB):
    theta0 = np.arctan2(1.0, 4.0*f_D)
    eta_i = np.cos(theta0)**2 * 10**(-0.1*Te_dB)
    eta_s = 1 - np.sin(theta0)**2 * 10**(-0.1*Te_dB)
    return eta_i, eta_s, eta_i*eta_s

print("\n--- Sec 11-9/11-10: Aperture efficiency ---")
D, f_GHz = 3.0, 10.0
lam = c/(f_GHz*1e9)
for f_D in [0.3, 0.4, 0.5, 0.6]:
    eta_i, eta_s, eta_ap = reflector_efficiency(f_D, 10.0)
    G_lin = eta_ap*(np.pi*D/lam)**2
    print(f"  f/D={f_D}: θ0={np.degrees(np.arctan2(1,4*f_D)):.1f}°, η_i={eta_i:.3f}, η_s={eta_s:.3f}, η_ap={eta_ap:.3f}, G={10*np.log10(G_lin):.1f}dBi")

# Plot
T_vals = np.linspace(5, 20, 101)
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
for f_D in [0.3, 0.4, 0.5, 0.6]:
    etas = [reflector_efficiency(f_D, T)[2] for T in T_vals]
    axes[0].plot(T_vals, etas, label=f'f/D={f_D}', lw=2)
axes[0].set_xlabel("Edge taper Te (dB)"); axes[0].set_ylabel("Aperture efficiency η_ap")
axes[0].set_title("Kraus Ch11 — η_ap vs Edge Taper\n(Sec 11-9/11-10)", fontsize=10)
axes[0].legend(); axes[0].grid(True, alpha=0.3)

for f_D in [0.3, 0.4, 0.5, 0.6]:
    G_vals = [10*np.log10(reflector_efficiency(f_D,T)[2]*(np.pi*D/lam)**2+1e-12) for T in T_vals]
    axes[1].plot(T_vals, G_vals, label=f'f/D={f_D}', lw=2)
axes[1].set_xlabel("Edge taper Te (dB)"); axes[1].set_ylabel("Gain (dBi)")
axes[1].set_title(f"Kraus Ch11 — Gain vs Edge Taper\n(D={D}m, f={f_GHz}GHz, λ={lam*1e2:.1f}cm)", fontsize=10)
axes[1].legend(); axes[1].grid(True, alpha=0.3)
plt.suptitle("Kraus Ch11 — Paraboloid Reflector: Efficiency & Gain", fontsize=12, fontweight='bold')
plt.tight_layout()
out = "/home/ubuntu/.openclaw/workspace/textbooks/kraus/code/kraus_ch11_reflector.png"
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f"\n✓ Saved: {out}")

# Surface tolerance effect
print("\n--- Sec 11-15/11-16: Surface tolerance effect on gain ---")
for sig_lam in [0.01, 0.02, 0.05, 0.1]:
    dG = -13.6 * sig_lam**2
    print(f"  σ/λ={sig_lam:.2f} → ΔG≈{dG:.2f} dB")

print("\n✓ Chapter 11 code complete.")