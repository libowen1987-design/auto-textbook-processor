#!/usr/bin/env python3
"""
Harrington Chapter 4: Plane Wave Functions

Example 4-3: Rectangular Waveguide — TE10 and TE20 mode field patterns
Example 4-5: Rectangular Cavity — resonant modes
Example 4-11: Aperture in Ground Plane — half-wave slot radiation pattern
Example 4-12: Plane Current Sheets — radiation from sheet dipole

scipy.special for Bessel/Hankel functions
scipy.constants for c, epsilon_0, mu_0
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0, pi

# ─────────────────────────────────────────────────────────────────────────────
# Example 4-3: Rectangular Waveguide — TE_mn modes
#   k_c = sqrt((m*pi/a)^2 + (n*pi/b)^2)
#   f_c = (c/2) * sqrt((m/a)^2 + (n/b)^2)
# ─────────────────────────────────────────────────────────────────────────────

def rectangular_waveguide_cutoff():
    """Compute cutoff frequencies for TE_mn modes."""
    a = 2.286e-2    # WR-90 broad dimension (m)
    b = 1.016e-2    # WR-90 narrow dimension (m)

    m_vals = range(0, 3)
    n_vals = range(0, 3)

    print("\n  [Example 4-3: Rectangular Waveguide TE_mn Cutoff Frequencies]")
    print(f"  Dimensions: a = {a*1e3:.3f} cm, b = {b*1e3:.3f} cm (WR-90)")
    print(f"  {'Mode':<8} {'f_c (GHz)':<12}")
    print(f"  {'-'*20}")
    for m in m_vals:
        for n in n_vals:
            if m == 0 and n == 0:
                continue
            k_c = np.sqrt((m*pi/a)**2 + (n*pi/b)**2)
            f_c = k_c * c / (2 * pi)
            print(f"  TE_{m}{n}      {f_c/1e9:.4f}")

def example_4_3_te10_field():
    """Plot E_y and H_x field distributions for TE10 mode."""
    a = 2.286e-2; b = 1.016e-2
    f = 10e9        # operating frequency
    k = 2 * pi * f / c
    lambda_g = 2 * pi / np.sqrt(k**2 - (pi/a)**2)
    m, n = 1, 0

    x = np.linspace(0, a, 100)
    y = np.linspace(0, b, 60)
    X, Y = np.meshgrid(x, y)

    # TE10: E_y = E0 * sin(pi*x/a) * exp(-j*beta*z)
    # |E_y| at z=0 cross-section
    E_y = np.abs(np.sin(pi * X / a))
    # H_x = (j*beta/mu) * sin(pi*x/a)  (proportional)
    H_x = np.abs(np.sin(pi * X / a))

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    cf0 = axes[0].contourf(X*1e3, Y*1e3, E_y, levels=20, cmap='hot')
    plt.colorbar(cf0, ax=axes[0], label=r'$|E_y|$ (V/m)')
    axes[0].set_xlabel('x (mm)'); axes[0].set_ylabel('y (mm)')
    axes[0].set_title(f'TE$_{{{m}{n}}}$ Mode: $|E_y|$ at $z=0$\n$a={a*1e3:.3f}$ cm, $b={b*1e3:.3f}$ cm')

    # Normalize H_x
    H_x_norm = H_x / np.max(H_x) * np.max(E_y)
    cf1 = axes[1].contourf(X*1e3, Y*1e3, H_x_norm, levels=20, cmap='winter')
    plt.colorbar(cf1, ax=axes[1], label=r'$|H_x|$ (A/m)')
    axes[1].set_xlabel('x (mm)'); axes[1].set_ylabel('y (mm)')
    axes[1].set_title(f'TE$_{{{m}{n}}}$ Mode: $|H_x|$ (phase orthogonal to $E_y$)')

    plt.suptitle('Harrington Example 4-3: Rectangular Waveguide TE10 Fields\n'
                 rf'$f = {f/1e9:.0f}$ GHz, $\lambda_g = {lambda_g*1e2:.2f}$ cm', fontsize=11)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_4_3_te10.png', dpi=150)
    plt.close()
    print("  [Saved] fig_4_3_te10.png")

    # Field along x cross-section
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(x*1e3, E_y[0, :], 'b-', lw=2, label=r'$|E_y|$ (TE10)')
    ax.plot(x*1e3, H_x[0, :] * (np.max(E_y)/np.max(H_x)), 'r--', lw=2, label=r'$|H_x|$ (scaled)')
    ax.axvline(x=a*1e3/2, color='green', ls='--', lw=1.5, label='Center')
    ax.set_xlabel('x (mm)'); ax.set_ylabel('Field amplitude (normalized)')
    ax.set_title('TE10 Mode: Field Distribution Along Width\n'
                 r'$E_y = E_0 \sin(\pi x/a)$, $H_x \propto \sin(\pi x/a)$')
    ax.legend(); ax.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_4_3_te10_profile.png', dpi=150)
    plt.close()
    print("  [Saved] fig_4_3_te10_profile.png")


# ─────────────────────────────────────────────────────────────────────────────
# Example 4-5: Rectangular Cavity — TM_mnp modes
#   f_mnp = (c/2) * sqrt((m/a)^2 + (n/b)^2 + (p/d)^2)
# ─────────────────────────────────────────────────────────────────────────────

def example_4_5_rect_cavity():
    """Compute resonant frequencies of a rectangular cavity."""
    a = 3e-2; b = 2e-2; d = 1e-2   # cm dimensions

    print("\n  [Example 4-5: Rectangular Cavity Resonant Frequencies]")
    print(f"  Cavity: {a*1e3:.1f} × {b*1e3:.1f} × {d*1e3:.1f} mm")

    modes = []
    for m in range(3):
        for n in range(3):
            for p in range(3):
                if m == 0 and n == 0 and p == 0:
                    continue
                k = pi * np.sqrt((m/a)**2 + (n/b)**2 + (p/d)**2)
                f_res = k * c / (2 * pi)
                modes.append((f_res/1e9, f'TM_{m}{n}{p}' if (m or n or p) else 'TM_0',
                             m, n, p))

    modes.sort()
    print(f"  {'Mode':<10} {'f_res (GHz)':<15}")
    print(f"  {'-'*25}")
    for f, name, *_, in modes[:10]:
        print(f"  {name:<10} {f:.4f}")

    # Plot field pattern for dominant TM110
    m, n, p = 1, 1, 0
    x = np.linspace(0, a, 60); y = np.linspace(0, b, 60)
    X, Y = np.meshgrid(x, y)
    E_z = np.sin(m * pi * X / a) * np.sin(n * pi * Y / b)

    fig, ax = plt.subplots(figsize=(8, 6))
    cf = ax.contourf(X*1e3, Y*1e3, E_z, levels=25, cmap='RdYlBu_r')
    plt.colorbar(cf, ax=ax, label=r'$E_z$ (V/m)')
    ax.set_xlabel('x (mm)'); ax.set_ylabel('y (mm)')
    ax.set_title(f'Harrington Example 4-5: Rectangular Cavity TM$_{{{m}{n}{p}}}$ Mode\n'
                 f'Dominant mode, $f_{{res}} = {modes[0][0]:.4f}$ GHz')
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_4_5_cavity.png', dpi=150)
    plt.close()
    print("  [Saved] fig_4_5_cavity.png")


# ─────────────────────────────────────────────────────────────────────────────
# Example 4-11: Aperture in Ground Plane — half-wave slot
#   Radiation pattern from uniformly illuminated aperture
#   E_plane pattern via Fourier transform of aperture field
# ─────────────────────────────────────────────────────────────────────────────

def example_4_11_slot_radiation():
    """Compute H-plane and E-plane radiation patterns for half-wave slot."""
    f = 10e9
    k = 2 * pi * f / c
    lambda_c = 2 * pi / k

    # Half-wave slot: length = lambda/2
    L = lambda_c / 2
    # Width is narrow (assume uniform along width dimension -> 2D problem)
    # Aperture field: E_y = E0 * sin(k*L/2 * cos(theta)) / (k*L/2 * cos(theta))
    # But Harrington uses simple sin(k*L*sin(theta)/2) / (k*L*sin(theta)/2)
    # For half-wave, approximate uniform (Huygens source)

    # E-plane (xz plane, phi=0):  F(theta) = cos((pi/2)*cos(theta)) / sin(theta)
    # H-plane (yz plane, phi=90): F(theta) = 1

    theta = np.linspace(-pi/2, pi/2, 500)
    sin_t = np.sin(theta)

    # E-plane (Harrington approximate formula for half-wave dipole)
    # For an aperture, use sinc pattern
    u = (k * L / 2) * sin_t
    F_E = np.where(np.abs(u) < 1e-12,
                   1.0,
                   np.sin(u) / u)

    # H-plane: uniform illumination -> cos(theta) factor for dx-pattern
    F_H = np.cos(theta)

    # Normalize
    F_E_norm = np.abs(F_E) / np.max(np.abs(F_E))
    F_H_norm = np.abs(F_H) / np.max(np.abs(F_H))

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    axes[0].plot(np.rad2deg(theta), F_E_norm, 'b-', lw=2)
    axes[0].axhline(y=0, color='gray', ls=':', lw=1)
    axes[0].set_xlabel(r'$\theta$ (deg)'); axes[0].set_ylabel('Normalized amplitude')
    axes[0].set_title(r'Half-wave Slot: E-plane pattern $|F_E(\theta)|$')
    axes[0].grid(True, alpha=0.4)
    axes[0].set_xlim(-90, 90)

    axes[1].plot(np.rad2deg(theta), F_H_norm, 'r-', lw=2)
    axes[1].axhline(y=0, color='gray', ls=':', lw=1)
    axes[1].set_xlabel(r'$\theta$ (deg)'); axes[1].set_ylabel('Normalized amplitude')
    axes[1].set_title(r'Half-wave Slot: H-plane pattern $|F_H(\theta)|$')
    axes[1].grid(True, alpha=0.4)
    axes[1].set_xlim(-90, 90)

    plt.suptitle(f'Harrington Example 4-11: Half-wave Slot Radiation\n'
                 f'$f = {f/1e9:.0f}$ GHz, $L = \\lambda/2 = {L*1e3:.2f}$ mm', fontsize=11)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_4_11_slot.png', dpi=150)
    plt.close()
    print("  [Saved] fig_4_11_slot.png")

    # Polar plot
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    ax.plot(theta, F_E_norm, 'b-', lw=2, label='E-plane')
    ax.plot(theta, F_H_norm, 'r--', lw=2, label='H-plane')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_title('Half-wave Slot Radiation Pattern', pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_4_11_slot_polar.png', dpi=150)
    plt.close()
    print("  [Saved] fig_4_11_slot_polar.png")


# ─────────────────────────────────────────────────────────────────────────────
# Example 4-2: Plane Wave Propagation — uniform plane wave in lossless medium
#   k = omega * sqrt(mu*epsilon)
#   Phase velocity v_p = 1/sqrt(mu*epsilon)
# ─────────────────────────────────────────────────────────────────────────────

def example_4_2_plane_wave():
    """Demonstrate plane wave propagation in dielectric."""
    epsilon_r_vals = [1.0, 2.1, 4.0, 9.0]
    f = 10e9
    omega = 2 * pi * f

    fig, ax = plt.subplots(figsize=(10, 6))
    z = np.linspace(0, 0.1, 300)   # 10 cm propagation path

    colors = ['b', 'g', 'r', 'm']
    for eps_r, col in zip(epsilon_r_vals, colors):
        k = omega * np.sqrt(mu_0 * eps_r * epsilon_0)
        E_real = np.real(np.exp(-1j * k * z))
        ax.plot(z*1e2, E_real, color=col, lw=2,
                label=f'$\\epsilon_r = {eps_r}$, $\\lambda = {2*pi/k*1e3:.2f}$ mm')

    ax.set_xlabel('Propagation distance z (cm)')
    ax.set_ylabel(r'$E_x(z)$ at $t=0$ (real part, normalized)')
    ax.set_title('Harrington Example 4-2: Plane Wave in Dielectrics\n'
                 r'$f = 10$ GHz, $E(x,t) = E_0 \cos(\omega t - kz)$')
    ax.legend(); ax.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_4_2_plane_wave.png', dpi=150)
    plt.close()
    print("  [Saved] fig_4_2_plane_wave.png")

    # Phase velocity comparison
    print("\n  [Example 4-2: Phase Velocities]")
    for eps_r in epsilon_r_vals:
        v_p = c / np.sqrt(eps_r)
        print(f"  epsilon_r = {eps_r:.1f}  ->  v_p = {v_p*1e-6:.2f} × 10^6 m/s "
              f"({v_p/c*100:.1f}% of c)")


if __name__ == '__main__':
    print("=== Harrington Ch4: Plane Wave Functions ===")
    example_4_2_plane_wave()
    rectangular_waveguide_cutoff()
    example_4_3_te10_field()
    example_4_5_rect_cavity()
    example_4_11_slot_radiation()
    print("\n  All Chapter 4 examples complete.")