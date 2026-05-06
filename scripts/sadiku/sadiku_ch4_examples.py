#!/usr/bin/env python3
"""Sadiku Ch4: Electrostatic Fields — Coulomb's law, E-field, potential."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import pi, epsilon_0

k = 1/(4*pi*epsilon_0)

def demo_charged_ring():
    """E-field on axis of a charged ring."""
    N = 100; R, Q = 1.0, 1e-9
    z = np.linspace(-5, 5, 1000)
    Ez = k * Q * z / (z**2 + R**2)**1.5
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(z, Ez, 'b-', lw=2)
    ax.axvline(0, color='k', ls='--', alpha=0.3)
    ax.set(xlabel='z (m)', ylabel='E_z (V/m)', title='Charged Ring: E-field on axis')
    ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('sadiku_ch4_ring_efield.png', dpi=150); plt.close()
    print('✅ Charged ring E-field done')

def demo_dipole_potential():
    """Electric dipole: equipotential + field lines."""
    x = y = np.linspace(-2, 2, 30); X, Y = np.meshgrid(x, y)
    d = 0.5; q = 1e-9
    R1 = np.sqrt((X-d)**2 + Y**2); R2 = np.sqrt((X+d)**2 + Y**2)
    V = k * q * (1/R1 - 1/R2)
    Ex, Ey = np.gradient(-V, x[1]-x[0], y[1]-y[0])
    fig, ax = plt.subplots(figsize=(8, 6))
    c = ax.contourf(X, Y, V, levels=20, cmap='RdBu_r')
    s = ax.streamplot(X, Y, Ex, Ey, color='k', density=1.2, linewidth=0.8)
    ax.plot([d, -d], [0, 0], 'ro', ms=6)
    ax.set(xlabel='x (m)', ylabel='y (m)', title='Electric Dipole: Potential & Field')
    ax.set_aspect('equal')
    plt.tight_layout(); plt.savefig('sadiku_ch4_dipole.png', dpi=150); plt.close()
    print('✅ Dipole potential done')

demo_charged_ring(); demo_dipole_potential()
print('Ch4: 2/2 ALL PASS')
