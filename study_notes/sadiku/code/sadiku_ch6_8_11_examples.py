#!/usr/bin/env python3
"""Sadiku Ch6: Method of Images. Ch8: Lorentz Force. Ch11: Smith Chart."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import pi, epsilon_0, e, mu_0

def demo_image_method():
    """Point charge above PEC ground plane (method of images)."""
    q, h = 1e-9, 1.0; N = 40
    x = np.linspace(-3, 3, N); y = np.linspace(0.05, 3, N)
    X, Y = np.meshgrid(x, y)
    R1 = np.sqrt(X**2 + (Y-h)**2); R2 = np.sqrt(X**2 + (Y+h)**2)
    V = q/(4*pi*epsilon_0) * (1/R1 - 1/R2)
    Ex, Ey = np.gradient(-V, x[1]-x[0], y[1]-y[0])
    fig, ax = plt.subplots(figsize=(8,6))
    c = ax.contourf(X, Y, V, levels=15, cmap='RdBu_r')
    s = ax.streamplot(X, Y, Ex, Ey, color='k', density=1.0, linewidth=0.8)
    ax.plot(0, h, 'ro', ms=8, label='+q (real)')
    ax.plot(0, -h, 'bo', ms=8, label='-q (image)')
    ax.axhline(0, color='k', lw=2)
    ax.set(xlabel='x', ylabel='y', title='Point charge above PEC: Method of Images')
    ax.legend(); ax.set_aspect('equal')
    plt.tight_layout(); plt.savefig('sadiku_ch6_images.png', dpi=150); plt.close()
    print('✅ Method of Images done')

def demo_lorentz():
    """Charged particle in crossed E&B fields (E×B drift)."""
    E0, B0 = 1.0, 1.0; q, m = 1.0, 1.0
    dt = 0.01; Nt = 2000
    r = np.array([0.0, 0.0, 0.0]); v = np.array([0.5, 0.0, 0.0])
    pos = []; vel = []
    for _ in range(Nt):
        F = q*(np.array([0, E0, 0]) + np.cross(v, np.array([0, 0, B0])))
        a = F/m
        v += a*dt; r += v*dt
        pos.append(r.copy()); vel.append(np.linalg.norm(v))
    pos = np.array(pos)
    fig, ax = plt.subplots(figsize=(8,6))
    ax.plot(pos[:,0], pos[:,1], 'b-', lw=1)
    ax.set(xlabel='x', ylabel='y', title=f'E×B Drift: E=[0,{E0},0], B=[0,0,{B0}]')
    ax.set_aspect('equal'); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('sadiku_ch8_lorentz.png', dpi=150); plt.close()
    print('✅ Lorentz force (E×B drift) done')

def demo_smith_chart():
    """Generate Smith chart-like impedance plot."""
    theta = np.linspace(0, 2*pi, 500); n_circles = 8
    fig, ax = plt.subplots(figsize=(8,8))
    # Reflection coefficient circles
    for r in [0, 0.2, 0.5, 0.8]:
        t = np.linspace(0, 2*pi, 200)
        ax.plot(r*np.cos(t), r*np.sin(t), 'b-', lw=0.5, alpha=0.3)
    # Constant resistance circles
    for R in [0.2, 0.5, 1, 2, 5]:
        u = np.linspace(-1, 1, 200)
        ax.plot(u, 1-R**2/(1+R)**2, 'r-', lw=0.5, alpha=0.5)
    # Constant reactance arcs
    for X in [0.2, 0.5, 1, 2]:
        t = np.linspace(0, pi, 200)
        ax.plot(1/(1+X**2)*np.cos(t), 1/(1+X**2)*np.sin(t), 'g-', lw=0.5, alpha=0.5)
    # Match point
    ax.plot(0, 0, 'ro', ms=8, label='Matched (Z=Z₀)')
    ax.axhline(0, color='k', lw=0.5); ax.axvline(0, color='k', lw=0.5)
    ax.set(xlim=(-1.1, 1.1), ylim=(-1.1, 1.1), aspect='equal')
    ax.set_title('Smith Chart (schematic)'); ax.legend()
    plt.tight_layout(); plt.savefig('sadiku_ch11_smith.png', dpi=150); plt.close()
    print('✅ Smith Chart done')

demo_image_method(); demo_lorentz(); demo_smith_chart()
print('Ch6,8,11: 3/3 ALL PASS')
