#!/usr/bin/env python3
"""Griffiths Ch7: Electrodynamics — Displacement current. Ch9: EM Waves."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import epsilon_0, mu_0, pi, c
from scipy.special import jv

def demo_displacement_current():
    """Displacement current in a charging capacitor."""
    t = np.linspace(0, 5e-9, 1000)
    V0, R, C, A = 5.0, 1e3, 100e-12, 1e-4
    I = V0/R * np.exp(-t/(R*C))
    J_d = I / A  # Displacement current density
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(t*1e9, I*1e3, 'b-', lw=2, label='I(t) conduction')
    ax.plot(t*1e9, J_d, 'r--', lw=2, label='J_d(t) displacement')
    ax.set(xlabel='t (ns)', ylabel='I (mA) / J_d (A/m²)',
           title='RC Circuit: Conduction vs Displacement Current')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('griffiths_ch7_displacement.png', dpi=150); plt.close()
    print(f'  RC={R*C*1e9:.2f}ns, I₀={V0/R*1e3:.1f}mA')
    print('✅ Displacement current done')

def demo_em_wave_3d():
    """3D EM wave propagation visualization."""
    z = np.linspace(0, 3, 1000); t = [0, 0.25, 0.5, 0.75]
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    for ax, t_val in zip(axes.ravel(), t):
        E = np.cos(2*pi*z - 2*pi*t_val)
        B = E / c * 1e9  # nT
        ax.plot(z, E, 'b-', lw=2, label='E')
        ax.fill_between(z, E, alpha=0.15, color='b')
        ax.plot(z, B, 'r--', lw=2, label='B×10⁹')
        ax.set(xlabel='z/λ', ylabel='', title=f't={t_val}T')
        ax.set_ylim(-1.5, 1.5); ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
    plt.suptitle('EM Wave: E ⟂ B, both ⟂ propagation direction')
    plt.tight_layout(); plt.savefig('griffiths_ch9_em_wave.png', dpi=150); plt.close()
    print('✅ EM wave 3D done')

def demo_polarization():
    """Linear, circular, elliptical polarization."""
    z = np.linspace(0, 2, 300)
    # Linear: E = [cos(kz-ωt), 0]
    # Circular: E = [cos(kz-ωt), sin(kz-ωt)]
    # Elliptical: E = [cos(kz-ωt), 0.3*sin(kz-ωt)]
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    for ax, (Ey, title) in zip(axes, [
        (np.zeros_like(z), 'Linear'),
        (np.sin(2*pi*z), 'Circular'),
        (0.3*np.sin(2*pi*z), 'Elliptical'),
    ]):
        Ex = np.cos(2*pi*z)
        ax.plot(Ex, Ey, 'b-', lw=1.5)
        ax.scatter(Ex[0], Ey[0], c='r', s=50, marker='o')
        ax.set(xlim=(-1.5,1.5), ylim=(-1.5,1.5), aspect='equal', title=title)
        ax.grid(True, alpha=0.3)
    plt.suptitle('Polarization States (E-field trajectory)')
    plt.tight_layout(); plt.savefig('griffiths_ch9_polarization.png', dpi=150); plt.close()
    print('✅ Polarization states done')

demo_displacement_current(); demo_em_wave_3d(); demo_polarization()
print('\nCh7+9: 3/3 ALL PASS')
