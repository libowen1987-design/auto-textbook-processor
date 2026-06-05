#!/usr/bin/env python3
"""
Hemming Ch1 - Measurement Principles for Anechoic Chamber Design
Friis formula, dB conversions, range criteria
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, pi

OUT = '/home/ubuntu/.openclaw/workspace/textbooks/hemming/figures'
import os; os.makedirs(OUT, exist_ok=True)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# --- dB power ratio conversions ---
def dB_to_ratio(dB):
    return 10 ** (dB / 10.0)

# --- Friis Transmission Formula ---
f = 10e9  # 10 GHz
lam = c / f
P_tx_dBm = 30.0
G_tx_dB = 20.0
G_rx_dB = 20.0
R = 5.0
polarization_eff = 0.9
L_fspl = 20 * np.log10(4 * pi * R / lam)
P_rx_dBm = P_tx_dBm + G_tx_dB + G_rx_dB - L_fspl + 10 * np.log10(polarization_eff)

ax1 = axes[0]
# Test region vs range length at different frequencies
K_vals = [10, 20, 50]
R_range = np.linspace(1, 30, 200)
for K in K_vals:
    region_size = K * lam**2 / (2 * np.pi * R_range)
    ax1.plot(R_range, region_size * 100, label=f'$K={K}$')
ax1.set_xlabel(r'$R$ (m)')
ax1.set_ylabel(r'Test region diameter (cm)')
ax1.set_title('Test Region Size vs Range Length (f=10 GHz)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# --- Field error vs extraneous signal ---
ax2 = axes[1]
alpha_db = np.linspace(0.5, 10, 200)
alpha = 10 ** (alpha_db / 10.0)
E_ratio = np.abs((-1 + alpha) / (1 + alpha))
ax2.semilogy(alpha_db, E_ratio, 'b-', lw=2)
ax2.set_xlabel(r'$\alpha$ (dB max/min difference)')
ax2.set_ylabel(r'$E_R/E_p$')
ax2.set_title('Field Error vs Extraneous Signal Level')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/hemming_ch01_measurement_principles.png', dpi=150, bbox_inches='tight')
plt.close()

print(f"Figure saved: hemming_ch01_measurement_principles.png")
print(f"  f={f/1e9:.0f} GHz, lambda={lam*100:.2f} cm, R={R}m")
print(f"  FSPL={L_fspl:.2f} dB, P_rx={P_rx_dBm:.2f} dBm")
