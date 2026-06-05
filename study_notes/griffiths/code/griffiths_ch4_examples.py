#!/usr/bin/env python3
"""Griffiths Ch.4: Electric Fields in Matter"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

plt.style.use('seaborn-v0_8')
eps0 = constants.epsilon_0

def example_4_4_dielectric_sphere():
    """Dielectric sphere in uniform field E0 z-hat.
    Internal field is uniform: E_in = 3/(eps_r+2) * E0"""
    eps_r_vals = [2.0, 4.0, 10.0, 80.0]
    E0 = 1000.0
    for er in eps_r_vals:
        E_in = 3.0 / (er + 2.0) * E0
        print(f"eps_r = {er:.1f}: E_in = {E_in:.1f} V/m = {E_in/E0:.3f} × E0")
    # Visualize field distortion
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    for idx, er in enumerate([2.0, 10.0]):
        ax = axes[idx]
        R = 0.1
        x = np.linspace(-3*R, 3*R, 30)
        y = np.linspace(-3*R, 3*R, 30)
        X, Y = np.meshgrid(x, y)
        r_xy = np.sqrt(X**2 + Y**2)
        theta_xy = np.arctan2(Y, X)
        # Outside: superposition of uniform + dipole
        E_out_x = E0 + E0 * R**3 / r_xy**3 * (2*np.cos(theta_xy)**2 - np.sin(theta_xy)**2)
        E_out_y = E0 * R**3 / r_xy**3 * np.sin(2*theta_xy)
        # Inside: uniform
        E_in_val = 3.0/(er+2.0) * E0
        mask = r_xy < R
        E_x = np.where(mask, E_in_val, E_out_x)
        E_y = np.where(mask, 0.0, E_out_y)
        # Reduce for plotting
        skip = 2
        ax.quiver(X[::skip,::skip], Y[::skip,::skip], 
                  E_x[::skip,::skip], E_y[::skip,::skip], scale=2e4, width=0.003)
        circle = plt.Circle((0,0), R, fill=False, color='red', linewidth=2)
        ax.add_patch(circle)
        ax.set_title(f'eps_r = {er}')
        ax.set_aspect('equal')
        ax.set_xlim(-3*R, 3*R); ax.set_ylim(-3*R, 3*R)
    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch4_ex4_dielectric_sphere.png', dpi=150)
    plt.close(fig)
    print("Figure saved: griffiths_ch4_ex4_dielectric_sphere.png")

def example_4_7_capacitor_with_dielectric():
    """Parallel plate capacitor with dielectric C = eps*A/d."""
    A, d = 0.01, 0.001
    eps_r_vals = [1, 2, 5, 10]
    for er in eps_r_vals:
        C = er * eps0 * A / d
        print(f"eps_r = {er}: C = {C*1e12:.2f} pF")
    print(f"\nWith eps_r=3.0: C = {3*eps0*A/d*1e12:.2f} pF (3x vacuum)")

def force_on_dielectric():
    """Force on dielectric partially inserted into capacitor."""
    eps_r = 3.0
    l, d, V0 = 0.1, 0.001, 100
    x = np.linspace(0, l, 100)
    C_total = eps0 * d / l * (x + eps_r * (l - x))
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x*1e2, C_total*1e12, 'b-', linewidth=2)
    ax.set_xlabel('Insertion x (cm)'); ax.set_ylabel('C (pF)')
    ax.set_title('Capacitance vs dielectric insertion')
    ax.grid(True, alpha=0.3)
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch4_extra_capacitor.png', dpi=150)
    plt.close(fig)
    print("Figure saved: griffiths_ch4_extra_capacitor.png")

if __name__ == "__main__":
    example_4_4_dielectric_sphere()
    example_4_7_capacitor_with_dielectric()
    force_on_dielectric()
    print("\n✅ Ch.4 examples done")
