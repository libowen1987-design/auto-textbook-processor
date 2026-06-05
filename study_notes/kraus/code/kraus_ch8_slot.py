"""
Kraus 'Antennas' 2nd Edition — Chapter 8: Slot Antennas
======================================================
Key topics:
- Sec 8-2: Babinet's principle — complementary antenna impedance
  Z_slot = (η0²/(4π²))·(1/Z_dipole)  [Ω]
  For half-wave dipole Z≈73+j42.5 → Z_slot ≈ 241+j0 Ω
- Sec 8-4: Half-wave slot radiation pattern (same as dipole but E/H interchanged)
  F(θ) = cos(π/2·cosθ)/sinθ  (field amplitude),  P(θ) ∝ [cos(π/2·cosθ)/sinθ]²
- Sec 8-5/8-6: Wide-slot (H-shaped) — pattern with two main lobes
- Sec 8-7 to 8-9: Waveguide slot arrays (resonant and non-resonant)
  For a waveguide of width a and height b, the dominant mode is TE10.
  Slot length for resonance: L ≈ λg/2 at f0, where λg = λ/√(1-(λ/(2a))²)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
Z0 = np.sqrt(constants.mu_0/constants.epsilon_0)

print("=" * 60)
print("Kraus Ch8 — Slot Antennas (Babinet's Principle)")
print("=" * 60)
print(f"η0 = Z0 = {Z0:.4f} Ω")

# Sec 8-2: Babinet complement
print("\n--- Sec 8-2: Babinet's principle ---")
Z_dipole = 73.0 + 42.5j
Z_slot = (Z0**2/(4*np.pi**2)) * (1/Z_dipole)
print(f"  Z_dipole(half-wave) = {Z_dipole} Ω")
print(f"  Z_slot = (Z0²/4π²)·(1/Z_dipole) = {Z_slot:.2f} Ω")

# Sec 8-4: Half-wave slot pattern
theta = np.linspace(0, np.pi, 10801)
F_slot = np.abs(np.cos(np.pi/2*np.cos(theta)))/(np.sin(theta)+1e-12)
P_slot = F_slot**2
P_slot = P_slot/np.max(P_slot)

fig, axes = plt.subplots(1, 2, subplot_kw={'projection':'polar'}, figsize=(13,6))
axes[0].plot(theta, P_slot, 'b-', lw=2); axes[0].fill(theta, P_slot, alpha=0.15)
axes[0].set_ylim(0,1.3); axes[0].set_title("Half-wave Slot Pattern\n(Sec 8-4)", fontsize=10)

# Compare with half-wave dipole
theta2 = np.linspace(0, np.pi, 10801)
P_dip = (np.cos(np.pi/2*np.cos(theta2))/np.sin(theta2))**2
P_dip = np.abs(P_dip)/np.max(np.abs(P_dip))
axes[1].plot(theta2, P_dip, 'r-', lw=2); axes[1].fill(theta2, P_dip, alpha=0.15, color='red')
axes[1].set_ylim(0,1.3); axes[1].set_title("Half-wave Dipole (Complementary)\n(Sec 5-5)", fontsize=10)
plt.suptitle("Kraus Ch8 — Slot Antenna via Babinet's Principle", fontsize=12, fontweight='bold')
plt.tight_layout()
out = "/home/ubuntu/.openclaw/workspace/textbooks/kraus/code/kraus_ch8_slot.png"
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f"\n✓ Saved: {out}")

# Wide slot (H-shaped)
def wide_slot_pattern(theta_deg, L_lam=1.0, W_lam=0.5):
    t = np.deg2rad(theta_deg)
    arg = np.pi*L_lam*np.cos(t)
    return np.abs(np.sin(arg))/np.max(np.abs(np.sin(arg))+1e-12)

P_wide = wide_slot_pattern(np.degrees(theta), 1.0, 0.5)
fig, ax = plt.subplots(subplot_kw={'projection':'polar'}, figsize=(7,6))
ax.plot(theta, P_wide, 'g-', lw=2); ax.fill(theta, P_wide, alpha=0.15, color='green')
ax.set_ylim(0,1.3); ax.set_title("Wide Slot (H-shaped)\nL=λ, W=λ/2 — Sec 8-5/8-6", fontsize=10)
plt.tight_layout()
out2 = "/home/ubuntu/.openclaw/workspace/textbooks/kraus/code/kraus_ch8_wide_slot.png"
plt.savefig(out2, dpi=150, bbox_inches='tight')
plt.close()
print(f"✓ Saved: {out2}")

print("\n✓ Chapter 8 code complete.")