#!/usr/bin/env python3
"""Sadiku Ch2: Coordinate Systems — Visualization Demos."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import pi

def demo_cartesian_grid():
    """3D Cartesian coordinate grid visualization."""
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    X, Y, Z = np.meshgrid([-1,0,1], [-1,0,1], [-1,0,1], indexing='ij')
    ax.scatter(X, Y, Z, c='b', s=20)
    ax.quiver(0,0,0, 1,0,0, color='r', linewidth=2, label='x')
    ax.quiver(0,0,0, 0,1,0, color='g', linewidth=2, label='y')
    ax.quiver(0,0,0, 0,0,1, color='b', linewidth=2, label='z')
    ax.set(xlim=(-1.5,1.5), ylim=(-1.5,1.5), zlim=(-1.5,1.5))
    ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    ax.legend(); ax.set_title('Cartesian Coordinates')
    plt.tight_layout(); plt.savefig('sadiku_ch2_cartesian.png', dpi=150); plt.close()

def demo_cylindrical_grid():
    """Cylindrical coordinate grid."""
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    rho = np.linspace(0, 1, 4); phi = np.linspace(0, 2*pi, 8)
    R, P = np.meshgrid(rho, phi)
    X = R*np.cos(P); Y = R*np.sin(P); Z = np.zeros_like(X)
    for z in [-0.5, 0, 0.5]:
        ax.plot_wireframe(X, Y, Z+z, alpha=0.3, color='b')
    ax.quiver(0,0,0, 1,0,0, color='r', lw=2, label='x')
    ax.quiver(0,0,0, 0,1,0, color='g', lw=2, label='y')
    ax.quiver(0,0,0, 0,0,1, color='b', lw=2, label='z')
    # Show a point
    p_rho, p_phi, p_z = 0.7, pi/4, 0.3
    px = p_rho*np.cos(p_phi); py = p_rho*np.sin(p_phi)
    ax.scatter([px], [py], [p_z], c='r', s=80)
    ax.set(xlim=(-1.2,1.2), ylim=(-1.2,1.2), zlim=(-1,1))
    ax.set_title(f'Cylindrical: (ρ={p_rho}, φ={p_phi:.1f}, z={p_z})')
    plt.tight_layout(); plt.savefig('sadiku_ch2_cylindrical.png', dpi=150); plt.close()

def demo_spherical_grid():
    """Spherical coordinate grid."""
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    # Sphere wireframe
    theta = np.linspace(0, pi, 10); phi = np.linspace(0, 2*pi, 15)
    T, P = np.meshgrid(theta, phi)
    X = np.sin(T)*np.cos(P); Y = np.sin(T)*np.sin(P); Z = np.cos(T)
    ax.plot_wireframe(X, Y, Z, alpha=0.2, color='b')
    # Point
    p_r, p_th, p_ph = 0.8, pi/3, pi/4
    px = p_r*np.sin(p_th)*np.cos(p_ph)
    py = p_r*np.sin(p_th)*np.sin(p_ph)
    pz = p_r*np.cos(p_th)
    ax.scatter([px], [py], [pz], c='r', s=80)
    ax.quiver(0,0,0, 1,0,0, color='r', lw=2)
    ax.quiver(0,0,0, 0,1,0, color='g', lw=2)
    ax.quiver(0,0,0, 0,0,1, color='b', lw=2)
    ax.set(xlim=(-1.2,1.2), ylim=(-1.2,1.2), zlim=(-1.2,1.2))
    ax.set_title(f'Spherical: (r={p_r}, θ={p_th:.1f}, φ={p_ph:.1f})')
    plt.tight_layout(); plt.savefig('sadiku_ch2_spherical.png', dpi=150); plt.close()

demo_cartesian_grid(); demo_cylindrical_grid(); demo_spherical_grid()
print('Ch2: 3 coordinate system visualizations ✅')
