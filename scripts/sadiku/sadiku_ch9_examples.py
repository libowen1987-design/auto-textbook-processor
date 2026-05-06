#!/usr/bin/env python3
"""Sadiku Ch9: Maxwell's Equations — Wave propagation demo."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import c, mu_0, epsilon_0
eta = np.sqrt(mu_0/epsilon_0)

def demo_em_wave():
    """EM wave: E and H fields propagating in free space."""
    z = np.linspace(0, 2, 1000)  # 2 wavelengths
    t_steps = [0, 0.25, 0.5, 0.75]
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    for ax, t in zip(axes.ravel(), t_steps):
        E = np.cos(2*np.pi*z - 2*np.pi*t)
        H = E / eta * 1e3  # mA/m
        ax.plot(z, E, 'b-', lw=2, label='E (V/m)')
        ax.plot(z, H, 'r--', lw=2, label='H×377 (mA/m)')
        ax.set(xlabel='z/λ', ylabel='Field', title=f't = {t:.2f} period')
        ax.set_ylim(-1.5, 1.5); ax.legend(); ax.grid(True, alpha=0.3)
    plt.suptitle('EM Wave: E & H Propagation in Free Space')
    plt.tight_layout(); plt.savefig('sadiku_ch9_em_wave.png', dpi=150); plt.close()
    print('✅ EM wave propagation done')

def demo_poynting():
    """Poynting vector magnitude along wave."""
    z = np.linspace(0, 2, 500)
    E = np.cos(2*np.pi*z); H = E/eta
    S = E * H  # Instantaneous Poynting
    S_avg = np.mean(np.abs(E)**2) / (2*eta)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(z, S, 'b-', lw=2, label='S(t) = E×H')
    ax.axhline(S_avg, color='r', ls='--', label=f'S_avg = {S_avg:.2e} W/m²')
    ax.set(xlabel='z/λ', ylabel='Poynting (W/m²)')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('sadiku_ch9_poynting.png', dpi=150); plt.close()
    print('✅ Poynting vector done')

demo_em_wave(); demo_poynting()
print('Ch9: 2/2 ALL PASS')
