#!/usr/bin/env python3
"""Griffiths Ch.3: Potentials - Method of Images & Separation of Variables"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants, integrate

plt.style.use('seaborn-v0_8')
eps0 = constants.epsilon_0

def example_3_2_point_charge_near_plane():
    """Point charge q at distance d above infinite conducting plane (V=0)."""
    print("="*60+"\nExample 3.2: Point charge near grounded plane\n"+"="*60)
    q, d = 1e-9, 0.5
    x = np.linspace(-1, 1, 300)
    z = np.linspace(0.01, 1, 300)
    X, Z = np.meshgrid(x, z)
    R1 = np.sqrt(X**2 + (Z-d)**2)
    R2 = np.sqrt(X**2 + (Z+d)**2)
    V = (1/(4*np.pi*eps0)) * (q/R1 - q/R2)
    sigma = -q*d/(2*np.pi*(x**2+d**2)**(1.5))
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    c1 = ax1.pcolormesh(X, Z, V, shading='auto', cmap='RdBu')
    fig.colorbar(c1, ax=ax1, label='V (V)')
    ax1.set_title('Potential above grounded plane')
    ax1.set_xlabel('x (m)'); ax1.set_ylabel('z (m)')
    ax2.plot(x, sigma*1e9, 'b-', linewidth=2)
    ax2.set_xlabel('x (m)'); ax2.set_ylabel('sigma (nC/m^2)')
    ax2.set_title('Induced surface charge'); ax2.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch3_ex2_image.png', dpi=150)
    plt.close(fig)
    print(f"Total induced charge (integrated): {np.trapezoid(sigma, x):.2e} C (expect -q = {-q:.2e} C)")
    print("Figure saved: griffiths_ch3_ex2_image.png")
    return V

def example_3_6_sphere_in_uniform_field():
    """Conducting sphere (radius R) in uniform external field E0 z-hat."""
    print("\n"+"="*60+"\nExample 3.6: Sphere in uniform field\n"+"="*60)
    R, E0 = 0.1, 1000
    theta = np.linspace(0, np.pi, 200)
    r_vals = np.linspace(R*1.01, 3*R, 200)
    R_grid, Theta = np.meshgrid(r_vals, theta, indexing='ij')
    V = -E0 * R_grid * np.cos(Theta) + E0 * R**3 * np.cos(Theta) / R_grid**2
    # Er = -dV/dr
    Er = E0 * np.cos(Theta) + 2*E0 * R**3 * np.cos(Theta) / R_grid**3
    # Surface field: Er(R) = 3E0*cos(theta)
    Er_surface = 3*E0*np.cos(theta)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), subplot_kw={'projection': 'polar'})
    c1 = ax1.pcolormesh(Theta, R_grid/R, V, shading='auto')
    ax1.set_title('Potential V(r,theta)')
    ax2.plot(theta, Er_surface*1e-3, 'r-', linewidth=2)
    ax2.plot(theta, np.abs(Er_surface)*1e-3, 'b--', linewidth=1)
    ax2.set_title('E_r at surface (kN/C)'); ax2.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch3_ex6_sphere_field.png', dpi=150)
    plt.close(fig)
    print(f"Max surface field: {Er_surface.max()/1e3:.1f} kN/C = 3*E0 = {3*E0/1e3:.1f} kN/C")
    print("Figure saved: griffiths_ch3_ex6_sphere_field.png")

if __name__ == "__main__":
    example_3_2_point_charge_near_plane()
    example_3_6_sphere_in_uniform_field()
    print("\n✅ Ch.3 examples done")
