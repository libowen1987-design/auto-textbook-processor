#!/usr/bin/env python3
"""
Hemming Ch4 - Shielding Effectiveness
Covers: SE calculation, material conductivity, shield penetration
"""
import numpy as np, matplotlib.pyplot as plt
OUT = '/home/ubuntu/.openclaw/workspace/textbooks/hemming/figures'
import os; os.makedirs(OUT, exist_ok=True)

def shielding_effectiveness(f_ghz, d_mm, sigma, mu_r=1.0):
    """SE in dB for a conductive shield (simplified model)."""
    lam = 300.0 / f_ghz  # mm
    skin_depth = 1.0 / np.sqrt(np.pi * f_ghz * 1e9 * mu_r * 4e-7 * sigma)
    if isinstance(d_mm, np.ndarray):
        return 8.68 * d_mm / (skin_depth * 1000)
    else:
        return 8.68 * d_mm / (skin_depth * 1000) if skin_depth > 0 else 100

def SE_reflection(f_ghz, Z_s):
    """Reflection loss in dB."""
    return 20 * np.log10(np.abs(Z_s) / (4 * 377))

print("=" * 60)
print("Hemming Ch4 — Shielding Effectiveness")
print("=" * 60)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# --- SE vs frequency for different metals ---
ax = axes[0, 0]
f = np.linspace(0.1, 40, 400)
for sigma, label in [(5.7e7, 'Copper'), (3.5e7, 'Aluminum'), (1e6, 'Steel')]:
    d = 1.0  # 1 mm
    sd = np.sqrt(1.0 / (np.pi * f * 1e9 * 4e-7 * 1.0 * sigma))
    se = 8.68 * d / (sd * 1000)
    ax.plot(f, se, label=label)
ax.set_xlabel('Frequency (GHz)'); ax.set_ylabel('SE (dB)')
ax.set_title('SE vs Frequency (d=1mm, mu_r=1)')
ax.legend(); ax.grid(True, alpha=0.3)

# --- SE vs thickness ---
ax = axes[0, 1]
d_range = np.linspace(0.01, 5, 200)
for sigma, label in [(5.7e7, 'Cu'), (3.5e7, 'Al'), (1e6, 'Steel')]:
    se = 8.68 * d_range / (np.sqrt(1.0 / (np.pi * 10 * 1e9 * 4e-7 * sigma)) * 1000)
    ax.plot(d_range, se, label=label)
ax.set_xlabel('Shield thickness (mm)'); ax.set_ylabel('SE (dB)')
ax.set_title('SE vs Thickness (f=10 GHz)')
ax.legend(); ax.grid(True, alpha=0.3)

# --- SE contour map ---
ax = axes[1, 0]
f_grid, d_grid = np.meshgrid(np.linspace(0.1, 40, 100), np.linspace(0.1, 5, 100))
sigma_cu = 5.7e7
sd_grid = np.sqrt(1.0 / (np.pi * f_grid * 1e9 * 4e-7 * 1.0 * sigma_cu))
se_grid = 8.68 * d_grid / (sd_grid * 1000)
im = ax.pcolormesh(f_grid, d_grid, se_grid, shading='auto', cmap='RdYlGn')
ax.set_xlabel('Frequency (GHz)'); ax.set_ylabel('Thickness (mm)')
ax.set_title('Copper Shield SE (dB)'); plt.colorbar(im, ax=ax, label='SE (dB)')

# --- Multiple reflections correction ---
ax = axes[1, 1]
f = np.linspace(0.1, 40, 300)
d = 0.5  # mm
sigma = 5.7e7
sd = np.sqrt(1.0 / (np.pi * f * 1e9 * 4e-7 * sigma))
se_main = 8.68 * d / (sd * 1000)
# Approx multiple reflection correction
se_total = se_main - 20 * np.log10(1 - np.exp(-2 * d / (sd * 1000) * 8.68))
ax.plot(f, se_main, 'b--', label='Without multiple reflection')
ax.plot(f, se_total, 'r-', lw=2, label='With multiple reflection')
ax.set_xlabel('Frequency (GHz)'); ax.set_ylabel('SE (dB)')
ax.set_title('Multiple Reflection Correction (d=0.5mm Cu)')
ax.legend(); ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/hemming_ch04_shielding.png', dpi=150, bbox_inches='tight')
plt.close()
print(f"  -> hemming_ch04_shielding.png")
print()
