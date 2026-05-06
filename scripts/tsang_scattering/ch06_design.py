#!/usr/bin/env python3
"""Tsang Ch6 - Scattering Design Topics"""
import numpy as np, matplotlib.pyplot as plt
OUT = '/home/ubuntu/.openclaw/workspace/textbooks/tsang_scattering/figures'
import os; os.makedirs(OUT, exist_ok=True)
fig, ax = plt.subplots(figsize=(8, 5))
f = np.linspace(0.5, 40, 300)
for i, d in enumerate([0.5, 1.0, 2.0]):
    ks = 2 * np.pi / (300.0 / f) * d
    se = np.exp(-4 * ks**2)
    ax.plot(f, se, label=f'sigma={d}cm')
ax.set_xlabel('Frequency (GHz)'); ax.set_ylabel('Emissivity')
ax.set_title('Tsang Ch6')
ax.legend(); ax.grid(True, alpha=0.3)
plt.savefig(f'{OUT}/tsang_ch06.png', dpi=150, bbox_inches='tight')
plt.close()
print("Tsang ch6 done")
