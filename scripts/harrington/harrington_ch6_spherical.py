#!/usr/bin/env python3
"""
Harrington Chapter 6: Spherical Wave Functions
Example 6-4: Spherical Cavity — resonant frequencies
Example 6-5: Short Dipole — radiation resistance, directivity
Example 6-8: Vector Spherical Harmonics — mode patterns

Uses jv, yv (Bessel), hankel1, lpmv (associated Legendre)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0, pi

# ─────────────────────────────────────────────────────────────────────────────
# Example 6-4: Spherical Cavity Resonator
# ─────────────────────────────────────────────────────────────────────────────

def example_6_4():
    a = 5e-2
    print(f"\n  [Example 6-4: Spherical Cavity, a={a*1e2:.1f} cm]")

    tm_modes = [('TM_010', np.pi), ('TM_011', 4.493), ('TM_020', 2*np.pi),
                ('TM_110', 5.764), ('TM_021', 5.986)]
    te_modes = [('TE_011', 3.832), ('TE_111', 1.841), ('TE_211', 3.054),
                ('TE_012', 4.973)]

    print(f"  {'Mode':<10} {'χ':<8} {'k (rad/m)':<14} {'f (GHz)':<12}")
    print(f"  {'-'*44}")
    for name, chi in tm_modes:
        k_v = chi / a; f_v = k_v * c / (2*pi)
        print(f"  {name:<10} {chi:<8.3f} {k_v:<14.3f} {f_v/1e9:<12.4f}")
    print()
    for name, chi in te_modes:
        k_v = chi / a; f_v = k_v * c / (2*pi)
        print(f"  {name:<10} {chi:<8.3f} {k_v:<14.3f} {f_v/1e9:<12.4f}")

    # TM010 field: Er ∝ j0(π*r/a) = sin(πr/a)/(πr/a)
    r = np.linspace(0, a, 100)
    Er = np.sin(np.pi*r/a) / (np.pi*r/a)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].plot(r*1e2, Er, 'b-', lw=2)
    axes[0].axhline(0, color='gray', ls=':')
    axes[0].set_xlabel('r (cm)'); axes[0].set_ylabel(r'$E_r/E_0$')
    axes[0].set_title(r'TM010: $E_r(r)$ radial distribution')
    axes[0].grid(True, alpha=0.4)

    R, TH = np.meshgrid(r, np.linspace(0, np.pi, 80))
    X = R*np.sin(TH); Y = R*np.cos(TH)
    Er_2D = np.sin(np.pi*R/a) / (np.pi*R/a)
    half = len(r)//2
    cf = axes[1].contourf(X[:,:half]*1e2, Y[:,:half]*1e2, Er_2D[:,:half],
                           levels=25, cmap='RdYlBu_r')
    plt.colorbar(cf, ax=axes[1], label=r'$E_r/E_0$')
    axes[1].set_xlabel('x (cm)'); axes[1].set_ylabel('z (cm)')
    axes[1].set_title('TM010 Field (meridional half-plane)')

    plt.suptitle('Harrington Example 6-4: Spherical Cavity', fontsize=12)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_6_4_sphere_cavity.png', dpi=150)
    plt.close()
    print("  [Saved] fig_6_4_sphere_cavity.png")

# ─────────────────────────────────────────────────────────────────────────────
# Example 6-5: Short Dipole (Hertzian dipole)
# ─────────────────────────────────────────────────────────────────────────────

def example_6_5():
    I0, dz, f = 1.0, 0.05, 300e6
    k = 2*pi*f/c
    lam = 2*pi/k

    R_rad = 80 * pi**2 * (dz/lam)**2
    D_dir = 1.5

    print(f"\n  [Example 6-5: Short Dipole]")
    print(f"  I={I0}A, dz={dz*1e2:.0f}cm, f={f/1e6:.0f}MHz")
    print(f"  λ={lam*1e2:.2f}cm, dz/λ={dz/lam:.4f}")
    print(f"  R_rad={R_rad:.2f}Ω, D={D_dir:.2f}")

    theta = np.linspace(0, pi, 400)
    E_pat = np.abs(np.sin(theta))

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    ax1 = axes[0]
    ax1.plot(np.rad2deg(theta), E_pat, 'b-', lw=2)
    ax1.set_ylabel('|E_theta| (norm)')
    ax1.set_title('Short Dipole: |Eθ| Radiation Pattern')
    ax1.grid(True, alpha=0.4)
    ax1.set_xlim(0, 180)

    ax2 = axes[1]
    phi_vals = np.linspace(0, 2*pi, 300)
    theta_p, phi_p = np.meshgrid(theta, phi_vals)
    D_3D = 1.5 * np.sin(theta_p)**2
    r_3D = D_3D
    X3 = r_3D*np.sin(theta_p)*np.cos(phi_p)
    Y3 = r_3D*np.sin(theta_p)*np.sin(phi_p)
    Z3 = r_3D*np.cos(theta_p)
    ax2.remove()
    ax2 = fig.add_subplot(122, projection='3d')
    ax2.plot_surface(X3, Y3, Z3, cmap='plasma', alpha=0.7)
    ax2.set_title('Directivity $D=1.5\\sin^2\\theta$')
    ax2.set_xlabel('X'); ax2.set_ylabel('Y'); ax2.set_zlabel('D')

    plt.suptitle('Harrington Example 6-5: Hertzian Dipole', fontsize=12)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_6_5_dipole.png', dpi=150)
    plt.close()
    print("  [Saved] fig_6_5_dipole.png")

# ─────────────────────────────────────────────────────────────────────────────
# Example 6-8: Vector Spherical Harmonics (n=0,1,2 mode shapes)
# ─────────────────────────────────────────────────────────────────────────────

def example_6_8():
    theta = np.linspace(0, np.pi, 150)
    phi = np.linspace(0, 2*np.pi, 150)
    TH, PH = np.meshgrid(theta, phi)

    n_vals = [0, 1, 2]
    fig, axes = plt.subplots(1, 3, figsize=(15, 5), subplot_kw={'projection': '3d'})
    for idx, n in enumerate(n_vals):
        if n == 0:
            p = np.ones_like(TH)
        elif n == 1:
            p = np.abs(np.sin(TH))
        else:
            p = np.abs(np.sin(TH)*np.cos(TH))
        r = p
        X = r*np.sin(TH)*np.cos(PH)
        Y = r*np.sin(TH)*np.sin(PH)
        Z = r*np.cos(TH)
        axes[idx].plot_surface(X, Y, Z, cmap='plasma', alpha=0.7)
        axes[idx].set_title(f'Spherical Harmonic n={n}')
        axes[idx].set_xlabel('X'); axes[idx].set_ylabel('Y'); axes[idx].set_zlabel('Z')
    plt.suptitle('Harrington Example 6-8: Spherical Harmonics n=0,1,2', fontsize=11)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_6_8_spherical_harm.png', dpi=150)
    plt.close()
    print("  [Saved] fig_6_8_spherical_harm.png")

if __name__ == '__main__':
    print("=== Harrington Ch6 ===")
    example_6_4()
    example_6_5()
    example_6_8()
    print("  Ch6 done.")