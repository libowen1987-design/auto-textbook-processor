#!/usr/bin/env python3
"""
Zhang Spacecraft EMC Ch6: EMC Design of General Electronic Equipment
Decoupling, grounding, filtering design examples
"""
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Ch6.1 - Decoupling capacitor frequency response
ax = axes[0, 0]
f = np.logspace(3, 9, 500)  # 1 kHz to 1 GHz
C_vals = [1e-9, 10e-9, 100e-9, 1e-6]  # 1nF, 10nF, 100nF, 1µF
ESL = 5e-9  # 5 nH typical ESL
colors = plt.cm.viridis(np.linspace(0, 0.8, len(C_vals)))

for C, color in zip(C_vals, colors):
    Z = 1 / (1j * 2 * np.pi * f * C) + 1j * 2 * np.pi * f * ESL
    ax.loglog(f, np.abs(Z), color=color, lw=2, label=f'C={C*1e9:.0f}nF')

ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Impedance (Ω)')
ax.set_title('Decoupling Capacitor Impedance vs Frequency')
ax.legend()
ax.axhline(y=1, color='r', ls='--', label='1Ω target')
ax.grid(True, alpha=0.3)

# Ch6.2 - PI-filter insertion loss
ax = axes[0, 1]
f = np.logspace(4, 9, 400)
L = 1e-6  # 1 µH
C = 1e-6  # 1 µF
# PI filter: L-C-L
Z_L = 1j * 2 * np.pi * f * L
Z_C = 1 / (1j * 2 * np.pi * f * C)
H_pi = np.abs(1 / (1 + Z_L/Z_C + Z_L/(50)) + Z_L/(50))
IL_dB = 20 * np.log10(H_pi + 1e-10)

ax.semilogx(f, IL_dB, 'b-', lw=2)
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Insertion Loss (dB)')
ax.set_title('PI Filter Insertion Loss')
ax.axhline(y=-3, color='r', ls='--', label='-3dB point')
ax.legend()
ax.grid(True, alpha=0.3)

# Ch6.3 - Grounding impedance model
ax = axes[1, 0]
f = np.logspace(1, 6, 300)
# Bond wire model: R + jωL
R_bond = 0.01  # 10 mΩ
L_bond = 10e-9  # 10 nH/m
Z_ground = R_bond + 1j * 2 * np.pi * f * L_bond
ax.loglog(f, np.abs(Z_ground) * 1000, 'b-', lw=2)
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Ground Impedance (mΩ)')
ax.set_title('PCB Ground Plane Impedance')
ax.grid(True, alpha=0.3)
ax.axhline(y=1, color='r', ls='--', label='1 mΩ budget')
ax.legend()

# Ch6.4 - CM/DM separation in mixed grounding
ax = axes[1, 1]
f = np.logspace(3, 6, 300)
# CM choke impedance model
L_cm = 100e-6  # 100 µH common mode
R_loss = 1  # loss resistance
Z_cm = np.sqrt(R_loss**2 + (2*np.pi*f*L_cm)**2)
Z_dm = 0.1 + 1j * 2 * np.pi * f * 100e-9  # differential mode

ax.loglog(f, Z_cm, 'b-', lw=2, label='CM impedance')
ax.loglog(f, Z_dm, 'r--', lw=2, label='DM impedance')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Impedance (Ω)')
ax.set_title('CM Choke: CM vs DM Impedance')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/zhang_sc_emc/figures/zhang_ch6_design.png', dpi=150)
plt.close()
print("zhang_ch6_design.png saved")

# Ch6.5 - via impedance and stub resonance
fig, ax = plt.subplots()
f = np.logspace(7, 11, 500)
# Via stub resonator: λ/4 at ~3 GHz for typical PCB via
Z_via = 1j * 200 * np.tan(2 * np.pi * f / 3e9 * 0.25)
ax.semilogx(f/1e9, np.abs(Z_via), 'b-', lw=2)
ax.set_xlabel('Frequency (GHz)')
ax.set_ylabel('|Impedance| (Ω)')
ax.set_title('Via Stub Resonance (λ/4 Model)')
ax.grid(True, alpha=0.3)
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/zhang_sc_emc/figures/zhang_ch6_via.png', dpi=150)
plt.close()
print("zhang_ch6_via.png saved")
print("zhang_ch6 code complete!")