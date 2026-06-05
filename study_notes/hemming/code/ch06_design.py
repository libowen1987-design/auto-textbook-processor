#!/usr/bin/env python3
"""Hemming Ch6 - Chamber/Scattering Design"""
import numpy as np, matplotlib.pyplot as plt
OUT = '/home/ubuntu/.openclaw/workspace/textbooks/hemming/figures'
import os; os.makedirs(OUT, exist_ok=True)
fig, ax = plt.subplots(figsize=(8, 5))
f = np.linspace(0.5, 40, 300)
for i, d in enumerate([5, 10, 20, 40]):
    RL = 10 + 20 * np.log10(f * d / (300.0 / f) / 100)
    ax.plot(f, RL, label=f'd={d}cm')
ax.set_xlabel('Frequency (GHz)'); ax.set_ylabel('RL (dB)')
ax.set_title('Hemming Ch6')
ax.legend(); ax.grid(True, alpha=0.3)
plt.savefig(f'{OUT}/hemming_ch06.png', dpi=150, bbox_inches='tight')
plt.close()
print("Hemming ch6 done")
