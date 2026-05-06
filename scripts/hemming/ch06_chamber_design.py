#!/usr/bin/env python3
"""Hemming Ch6 - Chamber Design Topics"""
import numpy as np, matplotlib.pyplot as plt
from scipy.constants import c, pi
OUT = '/home/ubuntu/.openclaw/workspace/textbooks/hemming/figures'
import os; os.makedirs(OUT, exist_ok=True)
fig, ax = plt.subplots(figsize=(8, 5))
f = np.linspace(0.5, 40, 300)
for i, thickness in enumerate([5, 10, 20, 40]):
    RL = 10 + 20 * np.log10(f * thickness / (c / (f * 1e9)) / 100)
    ax.plot(f, RL, label=f'd={thickness}cm')
ax.set_xlabel('Frequency (GHz)'); ax.set_ylabel('RL (dB)')
ax.set_title('Hemming Ch6 - Chamber Performance')
ax.legend(); ax.grid(True, alpha=0.3)
plt.savefig(f'{OUT}/hemming_ch06_chamber_design.png', dpi=150, bbox_inches='tight')
plt.close()
print(f"Ch6 done")
