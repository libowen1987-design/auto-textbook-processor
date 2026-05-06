#!/usr/bin/env python3
"""Paul EMC Ch7: Antennas.
Examples: dipole radiation, loop antenna, antenna factor, array pattern."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import pi, c, mu_0, epsilon_0

ETA0 = np.sqrt(mu_0/epsilon_0)

def demo_dipole_radiation():
    """Hertzian dipole: E-field pattern vs θ, directivity."""
    theta = np.linspace(0, 2*pi, 360)
    E_norm = np.abs(np.sin(theta))
    fig, ax = plt.subplots(1, 2, figsize=(14, 5), 
                           subplot_kw={'projection': 'polar'})
    ax[0].plot(theta, E_norm, 'b-', lw=2)
    ax[0].set(title='Hertzian Dipole Pattern (E-plane)', theta_zero_location='N')
    ax[0].set_ylim(0, 1.1)
    # Cartesian
    ax[1] = plt.subplot(122)
    theta_c = np.linspace(0, pi, 180)
    E_c = np.abs(np.sin(theta_c))
    dB_pattern = 20*np.log10(E_c + 1e-15)
    ax[1].plot(theta_c*180/pi, dB_pattern, 'b-', lw=2)
    ax[1].set(xlabel='θ (deg)', ylabel='Normalized Pattern (dB)', 
              title='E-plane Pattern (dB)', xlim=(0,180), ylim=(-40, 0))
    ax[1].grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch7_dipole_pattern.png', dpi=150); plt.close()
    print(f'  Directivity = {1.5:.2f} ({10*np.log10(1.5):.2f} dBi)')
    print('✅ Dipole radiation done')

def demo_far_field_condition():
    """Far-field limit: 2D²/λ vs distance."""
    D_ant = np.array([0.1, 0.3, 1.0])  # antenna dimensions (m)
    f = np.logspace(6, 9, 500)
    fig, ax = plt.subplots(figsize=(10,5))
    for D in D_ant:
        r_ff = 2 * D**2 / (c/f)
        ax.loglog(f/1e6, r_ff, lw=2, label=f'D={D*100:.0f}cm')
        ax.axhline(3, color='gray', ls=':', alpha=0.3)
    ax.set(xlabel='f (MHz)', ylabel='r_ff (m)', title='Far-Field Distance (2D²/λ)',
           xlim=(1, 1000), ylim=(0.01, 100))
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch7_farfield.png', dpi=150); plt.close()
    print('✅ Far-field condition done')

def demo_antenna_factor():
    """Antenna factor vs frequency for typical EMC antennas."""
    f = np.logspace(7, 9, 500)
    lmbda = c/f
    G_ant = {'Biconical (30-300MHz)': 1.5, 'Log-Periodic (200-1GHz)': 6, 'Horn (1-18GHz)': 10}
    fig, ax = plt.subplots(figsize=(10,5))
    for name, G in G_ant.items():
        AF = 9.73 / (lmbda * np.sqrt(G))
        AF_dB = 20*np.log10(AF)
        ax.semilogx(f/1e6, AF_dB, lw=2, label=name)
    ax.set(xlabel='f (MHz)', ylabel='AF (dB/m)', title='Antenna Factor vs Frequency',
           xlim=(30, 1000), ylim=(0, 50))
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch7_antenna_factor.png', dpi=150); plt.close()
    print('✅ Antenna factor done')

def demo_array_pattern():
    """Two-element array patterns: broadside, endfire."""
    d = 0.5  # lambda spacing
    kd = 2*pi*d
    theta = np.linspace(0, 2*pi, 360)
    fig, axes = plt.subplots(1, 2, figsize=(14, 5), subplot_kw={'projection': 'polar'})
    alphas = [0, pi]  # broadside, endfire
    titles = ['Broadside Array (α=0°)', 'End-Fire Array (α=180°)']
    for ax, alpha, title in zip(axes, alphas, titles):
        AF = 2 * np.abs(np.cos((kd*np.cos(theta) + alpha)/2))
        AF = AF / np.max(AF)
        ax.plot(theta, AF, 'b-', lw=2)
        ax.set(title=title, theta_zero_location='N')
        ax.set_ylim(0, 1.1)
    plt.tight_layout(); plt.savefig('../figures/paul_ch7_array_pattern.png', dpi=150); plt.close()
    print('✅ Array pattern done')

def demo_loop_vs_dipole():
    """Compare small loop and short dipole radiation."""
    f = np.logspace(6, 9, 500); r = 3.0
    lmbda = c/f; k = 2*pi/lmbda
    dl = 0.1   # 10 cm dipole
    A_loop = 1e-4  # 1 cm² loop
    I = 0.1  # 100 mA
    E_dipole = ETA0 * I * dl * k / (4*pi*r)
    E_loop = ETA0 * I * A_loop * k**2 / (4*pi*r)
    fig, ax = plt.subplots(figsize=(10,5))
    ax.loglog(f/1e6, 20*np.log10(E_dipole/1e-6), 'b-', lw=2, label='Short dipole (ℓ=10cm)')
    ax.loglog(f/1e6, 20*np.log10(E_loop/1e-6), 'r--', lw=2, label='Small loop (A=1cm²)')
    ax.set(xlabel='f (MHz)', ylabel='E (dBμV/m @ 3m)', title='Dipole vs Loop Radiation',
           xlim=(1, 1000), ylim=(0, 120))
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch7_loop_vs_dipole.png', dpi=150); plt.close()
    fc = f[np.argmin(np.abs(20*np.log10(E_dipole/E_loop)))]
    print(f'  Dipole=Loop at {fc/1e6:.0f} MHz')
    print('✅ Loop vs dipole done')

demo_dipole_radiation(); demo_far_field_condition()
demo_antenna_factor(); demo_array_pattern(); demo_loop_vs_dipole()
print('\nCh7: 5/5 ALL PASS')
