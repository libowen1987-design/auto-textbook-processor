#!/usr/bin/env python3
"""
Tsang Ch3 - Brightness Temperature and Passive Remote Sensing
Covers: radiative transfer, brightness temperature, emission from rough surfaces
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, Boltzmann, epsilon_0, mu_0

OUT = '/home/ubuntu/.openclaw/workspace/textbooks/tsang_scattering/figures'
import os; os.makedirs(OUT, exist_ok=True)

T0 = 290.0  # physical temperature K
f_ghz = 10.0

def brightness_temp(eps_r_real, eps_r_imag, T, f):
    """Brightness temperature of a medium."""
    lam = c / (f * 1e9)
    e = eps_r_real - 1j * eps_r_imag
    # Emissivity = 1 - |R|^2 for smooth surface
    R = (np.sqrt(e) - 1) / (np.sqrt(e) + 1)
    emissivity = 1 - np.abs(R)**2
    return T * emissivity

def radiative_transfer(T_s, T_sky, tau):
    """Simple radiative transfer: brightness at top of atmosphere."""
    return T_sky * np.exp(-tau) + T_s * (1 - np.exp(-tau))

print("=" * 60)
print("Tsang Ch3 — Brightness Temperature & Passive Sensing")
print("=" * 60)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# --- Brightness temp vs soil moisture ---
ax = axes[0, 0]
eps_r_grid = np.linspace(1.5, 30, 200)
# Typical soil: eps_r = 3.15 + j*0.1 at dry → 20 + j*5 at wet
for moisture_pct in [5, 15, 30]:
    eps_imag = 0.1 + 0.15 * moisture_pct
    Tb = [brightness_temp(e, eps_imag, T0, f_ghz) for e in eps_r_grid]
    ax.plot(eps_r_grid, Tb, label=f'moisture={moisture_pct}%')
ax.set_xlabel(r'$epsilon_r^\prime$')
ax.set_ylabel(r'$T_B$ (K)')
ax.set_title('Brightness Temperature vs Soil Permittivity')
ax.legend(); ax.grid(True, alpha=0.3)

# --- Emission from rough surface ---
ax = axes[0, 1]
theta_range = np.linspace(0, 80, 200)
sigma_rms = 0.5  # cm
lam = c / (f_ghz * 1e9)
ks = 2 * np.pi / lam * sigma_rms / 100  # normalized roughness
for s in [0.1, 0.5, 1.0, 2.0]:
    sigma_rms = s
    ks = 2 * np.pi / lam * sigma_rms / 100
    # Rough surface scattering reduces emissivity
    e_s = np.exp(-4 * ks**2 * np.cos(np.radians(theta_range)))
    Tb = T0 * (1 - e_s * np.abs((np.sqrt(3.15) - 1) / (np.sqrt(3.15) + 1))**2)
    ax.plot(theta_range, Tb, label=f'$\sigma$={s} cm')
ax.set_xlabel(r'$theta$ (deg)')
ax.set_ylabel(r'$T_B$ (K)')
ax.set_title('Brightness Temp vs Observation Angle')
ax.legend(); ax.grid(True, alpha=0.3)

# --- Radiative transfer ---
ax = axes[1, 0]
tau_range = np.linspace(0, 3, 200)
for T_s in [280, 290, 300]:
    Tb = radiative_transfer(T_s, 10, tau_range)
    ax.plot(tau_range, Tb, label=f'$T_s$={T_s}K')
ax.set_xlabel(r'$\tau$ (optical depth)')
ax.set_ylabel(r'$T_B$ (K)')
ax.set_title('Radiative Transfer: Atmospheric Emission')
ax.legend(); ax.grid(True, alpha=0.3)

# --- Passive sensor brightness temp vs frequency ---
ax = axes[1, 1]
f_range = np.linspace(1, 40, 200)
e_real = 5.0  # moderate moisture soil
e_imag = 1.0
Tb_f = [brightness_temp(e_real, e_imag, T0, f) for f in f_range]
ax.plot(f_range, Tb_f, 'b-', lw=2)
ax.set_xlabel('Frequency (GHz)')
ax.set_ylabel(r'$T_B$ (K)')
ax.set_title(f'Soil Emission Spectrum ($\epsilon_r$={e_real}, $\epsilon_r$"{e_imag}=' + f'{e_imag})')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{OUT}/tsang_ch3_brightness_temperature.png', dpi=150, bbox_inches='tight')
plt.close()
print(f"  → tsang_ch3_brightness_temperature.png")

print("\n--- Brightness Temp Examples ---")
for f in [1.4, 6.9, 10.7, 18, 37]:
    Tb = brightness_temp(5.0, 0.5, T0, f)
    print(f"  f={f:5.1f} GHz: T_B={Tb:.1f} K")
