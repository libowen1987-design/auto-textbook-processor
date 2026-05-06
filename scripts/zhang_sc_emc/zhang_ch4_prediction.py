#!/usr/bin/env python3
"""
Zhang Spacecraft EMC Ch4: EMC Prediction Analysis
Transfer function, interference analysis, coupling calculation
"""
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Ch4.1 - EMI coupling transfer function
ax = axes[0, 0]
f = np.logspace(1, 6, 500)  # 10 Hz to 1 MHz
omega = 2 * np.pi * f
L = 1e-6  # 1 µH
C = 100e-12  # 100 pF
H_f = np.abs(1 / (1 - omega**2 * L * C + 1j * omega * L * 0.01))
ax.semilogx(f, 20 * np.log10(H_f), 'b-', lw=2)
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Transfer Function (dB)')
ax.set_title('EMI Coupling Transfer Function: R-L-C Network')
ax.axhline(y=0, color='gray', ls='--', alpha=0.5)
ax.grid(True, alpha=0.3)

# Ch4.2 - Frequency interference judgment diagram
ax = axes[0, 1]
# Fundamental and harmonic frequencies
f_fund = 10e6  # 10 MHz fundamental
harmonics = np.arange(1, 15)
f_harms = harmonics * f_fund
# ISM band interference assessment
ism_bands = [(88e6, 108e6, 'FM Radio'), (2400e6, 2500e6, 'WiFi 2.4G'), (5150e6, 5850e6, 'WiFi 5G')]
band_colors = ['coral', 'lightgreen', 'salmon']
for (f_low, f_high, name), color in zip(ism_bands, band_colors):
    ax.axvspan(f_low/1e9, f_high/1e9, alpha=0.3, color=color, label=name)
ax.scatter(f_harms/1e9, np.ones(len(f_harms))*0.5, marker='|', s=200, color='navy', label='Harmonics')
ax.set_xlabel('Frequency (GHz)')
ax.set_title('Frequency Interference Analysis')
ax.set_xlim([0, 6])
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Ch4.3 - Path loss model
ax = axes[1, 0]
d = np.logspace(-2, 3, 300)  # 10 mm to 1 km
# Near field (reactive) region loss
k = 2 * np.pi / 0.1  # at 3 GHz, lambda=0.1m
PL_near = 20 * np.log10(d) + 40 * np.log10(k * d + 0.01)  # reactive near field
PL_far = 20 * np.log10(d) + 20 * np.log10(4 * np.pi / 0.1)  # far field
ax.loglog(d, np.maximum(PL_near, PL_far), 'b-', lw=2, label='Total Loss')
ax.loglog(d, PL_far, 'r--', lw=1.5, label='Far field only')
ax.axvline(x=0.1, color='g', ls=':', label='λ/2π boundary')
ax.set_xlabel('Distance (m)')
ax.set_ylabel('Path Loss (dB)')
ax.set_title('EMI Path Loss: Near vs Far Field')
ax.legend()
ax.grid(True, alpha=0.3)

# Ch4.4 - EMC prediction flowchart (conceptual bar chart)
ax = axes[1, 1]
steps = ['Susceptibility\nAnalysis', 'Emission\nCharacterization', 'Coupling\nCalculation', 'Risk\nAssessment', 'Mitigation\nDesign']
confidence = [0.95, 0.88, 0.72, 0.65, 0.60]
bars = ax.barh(steps, confidence, color='steelblue', edgecolor='black')
ax.set_xlim([0, 1])
ax.set_xlabel('Prediction Confidence')
ax.set_title('EMC Prediction Process Confidence')
for bar, conf in zip(bars, confidence):
    ax.text(bar.get_width() + 0.02, bar.get_y() + bar.get_height()/2,
            f'{conf:.0%}', va='center', fontsize=9)
ax.grid(True, alpha=0.3, axis='x')

plt.tight_layout()
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/zhang_sc_emc/figures/zhang_ch4_prediction.png', dpi=150)
plt.close()
print("zhang_ch4_prediction.png saved")

# Ch4.5 - Spice-style transfer function Bode plot
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

f = np.logspace(1, 5, 400)
omega = 2 * np.pi * f

# 3-pole lowpass filter model
H = 1 / ((1 + 1j*f/1e3) * (1 + 1j*f/5e3) * (1 + 1j*f/20e3))
mag_dB = 20 * np.log10(np.abs(H))
phase_deg = np.angle(H, deg=True)

axes[0].semilogx(f, mag_dB, 'b-', lw=2)
axes[0].set_xlabel('Frequency (Hz)')
axes[0].set_ylabel('Magnitude (dB)')
axes[0].set_title('EMI Filter: Bode Plot (Magnitude)')
axes[0].axhline(y=-3, color='r', ls='--', label='-3dB')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].semilogx(f, phase_deg, 'b-', lw=2)
axes[1].set_xlabel('Frequency (Hz)')
axes[1].set_ylabel('Phase (degrees)')
axes[1].set_title('EMI Filter: Bode Plot (Phase)')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/zhang_sc_emc/figures/zhang_ch4_bode.png', dpi=150)
plt.close()
print("zhang_ch4_bode.png saved")
print("zhang_ch4 code complete!")