#!/usr/bin/env python3
"""
Zhang Spacecraft EMC Ch2: EMC Standards and EMI Control
Key EMC standards visualization, cable shielding effectiveness, skin depth
"""
import numpy as np
import matplotlib.pyplot as plt

# MIL-STD-461 Conducted Emission Limits
freqs_mHz = np.array([10, 15, 30, 50, 100, 200, 500, 1000, 2000, 5000, 10000])  # kHz

# CS101 limits (30Hz-150kHz) - military
cs101_limit_dBuV = 120 - 20 * np.log10(freqs_mHz / 1e3 + 0.01)  # rough approximation
cs101_limit_dBuV = np.clip(cs101_limit_dBuV, 60, 120)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Ch2.1 - EMC Terms visualization
ax = axes[0, 0]
ax.set_title('EMC Key Concepts: SNR and Interference Margin')
snr_db = np.linspace(-20, 60, 200)
prob_interference = 1 / (1 + np.exp(0.15 * (snr_db - 20)))
ax.plot(snr_db, prob_interference * 100, 'b-', lw=2)
ax.axhline(y=10, color='r', ls='--', label='10% threshold')
ax.axvline(x=20, color='g', ls='--', label='SNR=20dB target')
ax.set_xlabel('Signal-to-Noise Ratio (dB)')
ax.set_ylabel('Probability of Interference (%)')
ax.legend()
ax.grid(True, alpha=0.3)

# Ch2.2 - Skin depth for copper at different frequencies
ax = axes[0, 1]
f = np.logspace(1, 6, 200)  # 10 Hz to 1 MHz
mu = 4e-7 * np.pi  # vacuum permeability
sigma_cu = 5.8e7  # S/m
sigma_al = 3.5e7
delta_cu = np.sqrt(1 / (np.pi * f * mu * sigma_cu))
delta_al = np.sqrt(1 / (np.pi * f * mu * sigma_al))
ax.loglog(f, delta_cu * 1000, 'b-', lw=2, label='Copper')
ax.loglog(f, delta_al * 1000, 'r--', lw=2, label='Aluminum')
ax.axvline(x=60, color='g', ls=':', label='60 Hz')
ax.axvline(x=1e6, color='orange', ls=':', label='1 MHz')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Skin Depth (mm)')
ax.legend()
ax.set_title('Skin Depth: Copper vs Aluminum')
ax.grid(True, alpha=0.3)

# Ch2.3 - Cable shielding effectiveness
ax = axes[1, 0]
d_over_lambda = np.logspace(-3, 0, 200)  # d/λ ratio
shielding_braid = 20 * np.log10(1 + 2 * d_over_lambda)  # simple braid model
shielding_foil = 40 * np.log10(1 + 5 * d_over_lambda)
ax.semilogx(d_over_lambda, np.clip(shielding_braid, 0, 80), 'b-', lw=2, label='Braid shield')
ax.semilogx(d_over_lambda, np.clip(shielding_foil, 0, 100), 'r--', lw=2, label='Foil shield')
ax.set_xlabel('$d/\lambda$ (conductor diameter / wavelength)')
ax.set_ylabel('Shielding Effectiveness (dB)')
ax.set_title('Cable Shielding Effectiveness vs Frequency')
ax.legend()
ax.grid(True, alpha=0.3)

# Ch2.4 - EMI coupling paths
ax = axes[1, 1]
coupling = {
    'Conducted\n(CS)': 45,
    'Radiated\n(RE)': 30,
    'Common\nMode': 55,
    'Differential\nMode': 25
}
colors = ['steelblue', 'coral', 'goldenrod', 'mediumseagreen']
bars = ax.bar(coupling.keys(), coupling.values(), color=colors, edgecolor='black')
ax.set_ylabel('Coupling Level (dBpV)')
ax.set_title('EMI Coupling Path Priority')
for bar, val in zip(bars, coupling.values()):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{val}dB', ha='center', fontsize=10)

plt.tight_layout()
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/zhang_sc_emc/figures/zhang_ch2_standards.png', dpi=150)
plt.close()
print("zhang_ch2_standards.png saved")

# Additional: Bonding impedance frequency response
fig, ax = plt.subplots()
f = np.logspace(0, 5, 300)
# Bonding impedance model: inductive at high freq
Z_bond = 0.01 + 1j * 2 * np.pi * f * 1e-9  # 1 nH/mm typical
Z_mag = np.abs(Z_bond)
ax.loglog(f, Z_mag * 1000, 'b-', lw=2)
ax.axvline(x=1e3, color='r', ls='--', label='1 kHz boundary')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('|Impedance| (mΩ)')
ax.set_title('Bonding Impedance vs Frequency')
ax.legend()
ax.grid(True, alpha=0.3)
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/zhang_sc_emc/figures/zhang_ch2_bonding.png', dpi=150)
plt.close()
print("zhang_ch2_bonding.png saved")

print("zhang_ch2 code complete!")