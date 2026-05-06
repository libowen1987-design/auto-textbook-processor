#!/usr/bin/env python3
"""
Hemming Ch2 - Electromagnetic Absorbing Materials
Covers: reflection loss, impedance matching, RAM types, pyramid/wedge absorbers
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, pi, epsilon_0, mu_0

OUT = '/home/ubuntu/.openclaw/workspace/textbooks/hemming/figures'
import os; os.makedirs(OUT, exist_ok=True)

def RL_dB(f_GHz, d_cm, epsilon_r, mu_r=1.0-0.1j):
    """Reflection loss of RAM layer (simplified model)."""
    lam = c / (f_GHz * 1e9)
    Z0 = np.sqrt(mu_0 / epsilon_0)
    Z_ram = Z0 * np.sqrt(mu_r / epsilon_r)
    Gamma = (Z_ram - Z0) / (Z_ram + Z0)
    return -20 * np.log10(np.abs(Gamma))

def multi_layer_RL(f_GHz, d_cm, epsilons, thicknesses_cm):
    """Multi-layer absorber reflection loss."""
    Z0 = 377.0
    Z = Z0
    for eps, d in zip(reversed(epsilons), reversed(thicknesses_cm)):
        Z = Z * np.sqrt(eps)  # approximate
        # Quarter-wave transformer at each layer
        Z_next = Z * np.sqrt(eps)
        Z = Z_next
    Gamma = (Z - Z0) / (Z + Z0)
    return -20 * np.log10(np.abs(Gamma) + 1e-12)

print("=" * 60)
print("Hemming Ch2 — Electromagnetic Absorbing Materials")
print("=" * 60)

# --- Reflection Loss vs Frequency for different RAM types ---
f_range = np.linspace(0.5, 40, 500)
d_10cm = 10.0  # 10 cm thick absorber
d_20cm = 20.0

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Pyramid absorber (effective permittivity gradient)
ax = axes[0, 0]
for d in [5, 10, 20, 30]:
    RL = []
    for f in f_range:
        lam = c / (f * 1e9)
        # Simplified: RL improves with thickness and frequency
        RL.append(10 + 20 * np.log10(f * d / lam))
    ax.plot(f_range, RL, label=f'd={d} cm')
ax.set_xlabel(r'Frequency (GHz)')
ax.set_ylabel(r'Reflection Loss (dB)')
ax.set_title('Pyramid Absorber — RL vs Frequency/Thickness')
ax.legend(); ax.grid(True, alpha=0.3)

# Wedge absorber
ax = axes[0, 1]
for d in [5, 10, 20]:
    RL = []
    for f in f_range:
        lam = c / (f * 1e9)
        RL.append(8 + 15 * np.log10(f * d / lam))
    ax.plot(f_range, RL, label=f'd={d} cm')
ax.set_xlabel(r'Frequency (GHz)')
ax.set_ylabel(r'Reflection Loss (dB)')
ax.set_title('Wedge Absorber — RL vs Frequency/Thickness')
ax.legend(); ax.grid(True, alpha=0.3)

# Dielectric constant effect
ax = axes[1, 0]
for eps_r in [1.5, 2.0, 3.0, 4.5]:
    RL = []
    for f in f_range:
        lam = c / (f * 1e9)
        # Simple sheet absorber model
        Z_ram = 377 / np.sqrt(eps_r)
        Gamma = np.abs((Z_ram - 377) / (Z_ram + 377))
        RL.append(-20 * np.log10(Gamma + 1e-12))
    ax.plot(f_range, RL, label='' + f'{eps_r}')
ax.set_xlabel(r'Frequency (GHz)')
ax.set_ylabel(r'Reflection Loss (dB)')
ax.set_title('Sheet Absorber - RL vs epsilon_r')
ax.legend(); ax.grid(True, alpha=0.3)

# Reflection loss contour (frequency vs thickness)
ax = axes[1, 1]
f_grid, d_grid = np.meshgrid(f_range, np.linspace(1, 40, 100))
RL_grid = 10 + 20 * np.log10(f_grid * d_grid / (c / (f_grid * 1e9)) / 1e2)
im = ax.pcolormesh(f_grid, d_grid, RL_grid, shading='auto', cmap='RdYlGn')
ax.set_xlabel(r'Frequency (GHz)')
ax.set_ylabel(r'Thickness (cm)')
ax.set_title('Reflection Loss Contour (dB)')
plt.colorbar(im, ax=ax, label='RL (dB)')

plt.tight_layout()
plt.savefig(f'{OUT}/hemming_ch02_absorption_materials.png', dpi=150, bbox_inches='tight')
plt.close()
print(f"  → hemming_ch02_absorption_materials.png")

# --- Example calculations ---
print("\n--- RAM Reflection Loss Examples ---")
for f in [1, 10, 30]:
    for d in [5, 10, 20]:
        lam = c / (f * 1e9)
        RL = 10 + 20 * np.log10(f * d / lam * 100)
        print(f"  f={f:2d} GHz, d={d:2d} cm → RL≈{RL:.1f} dB")

print()
