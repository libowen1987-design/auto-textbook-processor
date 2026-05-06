#!/usr/bin/env python3
"""
Hemming Ch3 - The Rectangular Anechoic Chamber
Covers: chamber resonances, field uniformity, quiet zone size
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, pi

OUT = '/home/ubuntu/.openclaw/workspace/textbooks/hemming/figures'
import os; os.makedirs(OUT, exist_ok=True)

def resonant_freq(m, n, p, L, W, H):
    """TE_mnp mode resonant frequency in rectangular cavity."""
    return (c / 2) * np.sqrt((m/L)**2 + (n/W)**2 + (p/H)**2)

def mode_count(f, L, W, H):
    """Approximate number of modes below f in rectangular cavity."""
    V = L * W * H
    return (8 * pi * V * f**3) / (3 * c**3)

print("=" * 60)
print("Hemming Ch3 — Rectangular Anechoic Chamber")
print("=" * 60)

L, W, H = 10.0, 6.0, 5.0  # 10m x 6m x 5m chamber

# --- Resonant modes ---
print("\n--- First few resonant modes (TE) ---")
modes = []
for m in range(5):
    for n in range(5):
        for p in range(5):
            if m == 0 and n == 0 and p == 0: continue
            f = resonant_freq(m, n, p, L, W, H)
            if f < 10e9:
                modes.append((m, n, p, f))
modes.sort(key=lambda x: x[3])
for m, n, p, f in modes[:15]:
    print(f"  TE_{m}{n}{p}: {f/1e9:.3f} GHz")

# --- Field uniformity in quiet zone ---
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

ax = axes[0]
f = 3e9  # 3 GHz
x = np.linspace(-L/2, L/2, 200)
y = 0.5  # y=0.5 m from center
z = 0.5
# Simplified field pattern (sum of first few modes)
E = np.abs(np.sin(pi/L * x) + 0.3*np.sin(2*pi/L * x) + 0.1*np.sin(3*pi/L * x))
E = E / np.max(E)
ax.plot(x, E, 'b-', lw=2)
ax.axhline(0.5, color='r', linestyle='--', label='50% level')
ax.set_xlabel('x (m)'); ax.set_ylabel('Normalized |E|')
ax.set_title('Field Uniformity Along Chamber Axis')
ax.legend(); ax.grid(True, alpha=0.3)

ax = axes[1]
f_range = np.linspace(0.1, 10, 200)
N_modes = [mode_count(f, L, W, H) for f in f_range * 1e9]
ax.semilogy(f_range, N_modes, 'b-', lw=2)
ax.axvline(1, color='g', linestyle='--', label='1 GHz')
ax.set_xlabel('Frequency (GHz)')
ax.set_ylabel('Number of modes below f')
ax.set_title('Mode Density vs Frequency')
ax.legend(); ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/hemming_ch03_chamber_fields.png', dpi=150, bbox_inches='tight')
plt.close()
print(f"  → hemming_ch03_chamber_fields.png")
print()
