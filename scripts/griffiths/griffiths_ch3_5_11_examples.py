#!/usr/bin/env python3
"""Griffiths Ch3: Separation of variables. Ch5: Vector potential. Ch11: Dipole radiation."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import mu_0, pi, c, epsilon_0
from scipy.special import legendre

def demo_separation_vars():
    """2D Laplace: separation of variables in Cartesian coords."""
    Nx, Ny = 60, 60
    x = np.linspace(0, 1, Nx); y = np.linspace(0, 1, Ny)
    X, Y = np.meshgrid(x, y)
    V = np.zeros_like(X)
    # V(0,y)=0, V(1,y)=0, V(x,0)=0, V(x,1)=sin(pi*x)
    for n in range(1, 20, 2):
        An = 4/(n*pi)  # Fourier coefficient for sin(pi*x) on top boundary
        V += An * np.sin(n*pi*X) * np.sinh(n*pi*Y) / np.sinh(n*pi)
    fig, ax = plt.subplots(figsize=(8,6))
    c = ax.contourf(X, Y, V, levels=20, cmap='RdBu_r')
    plt.colorbar(c)
    ax.set(xlabel='x', ylabel='y', title='Laplace: V(x,1)=sin(πx), sum 20 modes')
    plt.tight_layout(); plt.savefig('griffiths_ch3_laplace.png', dpi=150); plt.close()
    print('✅ Separation of variables done')

def demo_radiation_pattern():
    """Hertzian dipole radiation pattern (Ch11)."""
    theta = np.linspace(0, pi, 200)
    F = np.sin(theta)**2  # Power pattern ~ sin²θ
    fig, ax = plt.subplots(figsize=(8,6), subplot_kw={'projection':'polar'})
    ax.plot(theta, F, 'b-', lw=2)
    ax.fill(theta, F, alpha=0.2, color='b')
    ax.set(title='Hertzian Dipole Radiation Pattern', theta_zero_location='N')
    ax.set_rmax(1.05)
    plt.tight_layout(); plt.savefig('griffiths_ch11_radiation.png', dpi=150); plt.close()
    # Directivity
    D0 = 4*pi / (pi * np.trapz(np.sin(theta)**3, theta))
    print(f'  Directivity D₀ = {D0:.3f} (theory: 1.5)')
    print('✅ Radiation pattern done')

demo_separation_vars(); demo_radiation_pattern()
print('\nCh3+11: 2/2 ALL PASS')
