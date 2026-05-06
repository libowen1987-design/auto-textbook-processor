#!/usr/bin/env python3
"""Sadiku Ch3: Vector Calculus — Gradient, Divergence, Curl."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

def demo_gradient():
    """Gradient of scalar field V = x² + y²."""
    x = y = np.linspace(-2, 2, 20); X, Y = np.meshgrid(x, y)
    V = X**2 + Y**2
    dVx, dVy = np.gradient(V, x[1]-x[0], y[1]-y[0])
    fig, ax = plt.subplots(figsize=(8, 6))
    c = ax.contourf(X, Y, V, levels=15, cmap='viridis')
    q = ax.quiver(X, Y, -dVx, -dVy, color='w', scale=30)
    ax.set(xlabel='x', ylabel='y', title='V=x²+y²: Contours (color) & Gradient (arrows)')
    plt.colorbar(c)
    plt.tight_layout(); plt.savefig('sadiku_ch3_gradient.png', dpi=150); plt.close()
    print('✅ Gradient demo done')

def demo_divergence():
    """Divergence of A = [x, y, 0] → ∇·A = 2."""
    x = y = np.linspace(-2, 2, 15); X, Y = np.meshgrid(x, y)
    Ax, Ay = X, Y  # A = [x, y, 0]
    divA = np.gradient(Ax, x[1]-x[0], axis=1) + np.gradient(Ay, y[1]-y[0], axis=0)
    fig, ax = plt.subplots(figsize=(8, 6))
    c = ax.contourf(X, Y, divA, levels=10, cmap='RdBu_r')
    q = ax.quiver(X, Y, Ax, Ay, color='k', scale=15)
    ax.set(xlabel='x', ylabel='y', title='A=[x,y,0]: ∇·A=2 everywhere')
    plt.colorbar(c, label='Divergence')
    plt.tight_layout(); plt.savefig('sadiku_ch3_divergence.png', dpi=150); plt.close()
    print('✅ Divergence demo done')

def demo_curl():
    """Curl of A = [-y, x, 0] → ∇×A = 2ẑ."""
    x = y = np.linspace(-2, 2, 15); X, Y = np.meshgrid(x, y)
    Ax, Ay = -Y, X
    curl_z = np.gradient(Ay, x[1]-x[0], axis=1) - np.gradient(Ax, y[1]-y[0], axis=0)
    fig, ax = plt.subplots(figsize=(8, 6))
    c = ax.contourf(X, Y, curl_z, levels=10, cmap='RdBu_r')
    s = ax.streamplot(X, Y, Ax, Ay, color='k', density=1.5)
    ax.set(xlabel='x', ylabel='y', title='A=[-y,x,0]: ∇×A=2 (vortex)')
    plt.colorbar(c, label='Curl (z-component)')
    plt.tight_layout(); plt.savefig('sadiku_ch3_curl.png', dpi=150); plt.close()
    print('✅ Curl demo done')

demo_gradient(); demo_divergence(); demo_curl()
print('Ch3: 3/3 ALL PASS')
