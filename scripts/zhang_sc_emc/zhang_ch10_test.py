#!/usr/bin/env python3
"""
Zhang Spacecraft EMC Ch10: EMC Test Verification
Test setup, LISN, measurement uncertainty
"""
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Ch10.1 - LISN (Line Impedance Stabilization Network) frequency response
ax = axes[0, 0]
f = np.logspace(1, 7, 400)  # 10 Hz to 10 MHz
# Standard LISN: 50 µH || 50 Ω or 5 µH design
L_lisn = 50e-6  # 50 µH
R_lisn = 50  # 50 Ω
Z_lisn = 1 / (1/R_lisn + 1/(1j * 2 * np.pi * f * L_lisn))
ax.loglog(f, np.abs(Z_lisn), 'b-', lw=2)
ax.axhline(y=50, color='r', ls='--', label='50 Ω target')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('|Z_lisn| (Ω)')
ax.set_title('LISN Impedance: 50 µH Design (MIL-STD-461)')
ax.legend()
ax.grid(True, alpha=0.3)

# Ch10.2 - Measurement uncertainty budget
ax = axes[0, 1]
categories = ['LISN\nTolerance', 'Cable\nLoss', 'Receiver\nAccuracy', 'Mismatch', 'Ambient\nInterference']
k_vals = [2, 2, 2, 2, 2]
u_i = np.array([1.5, 0.5, 0.3, 1.2, 0.8])  # individual std uncertainties (dB)
U_combined = np.sqrt(np.sum((k_vals * u_i)**2))
dof = [10, 20, 50, 8, 15]  # degrees of freedom

ax.bar(categories, u_i, color='steelblue', edgecolor='black')
ax.set_ylabel('Uncertainty (dB)')
ax.set_title(f'Combined Uncertainty: {U_combined:.2f} dB (k=2)')
ax.grid(True, alpha=0.3, axis='y')

# Ch10.3 - Near-field to far-field conversion
ax = axes[1, 0]
D = np.linspace(0.01, 0.5, 200)  # 10mm to 500mm
freqs = [1e6, 10e6, 100e6, 1e9]  # 1MHz, 10MHz, 100MHz, 1GHz
colors = ['blue', 'green', 'orange', 'red']
R_fff = 2 * D**2 / (3e8 / 1e9)  # far field boundary at 1 GHz
for freq, color in zip(freqs, colors):
    lambda_c = 3e8 / freq
    R_ff = 2 * D**2 / lambda_c
    ax.plot(D * 1000, R_ff, color=color, lw=2, label=f'{freq/1e6:.0f} MHz')
ax.set_xlabel('Antenna dimension D (mm)')
ax.set_ylabel('Far-field boundary R_ff (mm)')
ax.set_title('Near-Field / Far-Field Boundary')
ax.legend()
ax.grid(True, alpha=0.3)

# Ch10.4 - ESD immunity test levels
ax = axes[1, 1]
test_levels = ['Level 1', 'Level 2', 'Level 3', 'Level 4']
contact_kV = [2, 4, 6, 8]
air_kV = [2, 4, 8, 15]
x = np.arange(len(test_levels))
width = 0.35
bars1 = ax.bar(x - width/2, contact_kV, width, label='Contact Discharge', color='steelblue')
bars2 = ax.bar(x + width/2, air_kV, width, label='Air Discharge', color='coral')
ax.set_xlabel('Test Level')
ax.set_ylabel('Voltage (kV)')
ax.set_title('IEC 61000-4-2 ESD Immunity Levels')
ax.set_xticks(x)
ax.set_xticklabels(test_levels)
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/zhang_sc_emc/figures/zhang_ch10_test.png', dpi=150)
plt.close()
print("zhang_ch10_test.png saved")

# Ch10.5 - Radiated emission limit comparison
fig, ax = plt.subplots()
f = np.logspace(7, 10, 300)  # 100 MHz to 10 GHz
# FCC Part 15 Class B limit
limit_fcc = np.where(f < 1e8, 240/(f/1e6)**0.5, 240/(f/1e6)**0.5)
limit_cispr = np.where(f < 1e8, 40, 47 - 20 * np.log10(f/1e8))
ax.loglog(f/1e6, limit_fcc, 'b-', lw=2, label='FCC Class B')
ax.loglog(f/1e6, limit_cispr, 'r--', lw=2, label='CISPR 22 Class B')
ax.set_xlabel('Frequency (MHz)')
ax.set_ylabel('E-field Limit (µV/m)')
ax.set_title('Radiated Emission Limits Comparison')
ax.legend()
ax.grid(True, alpha=0.3)
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/zhang_sc_emc/figures/zhang_ch10_emission_limit.png', dpi=150)
plt.close()
print("zhang_ch10_emission_limit.png saved")
print("zhang_ch10 code complete!")