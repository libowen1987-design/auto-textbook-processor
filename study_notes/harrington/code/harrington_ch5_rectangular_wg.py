#!/usr/bin/env python3
"""
Harrington Chapter 5: Rectangular Waveguides and Cavities

Example 5-1: TE_mn Rectangular Waveguide Dispersion
Example 5-2: Rectangular Cavity Resonator (TE_101 mode)

Physical constants from scipy.constants:
    c        : speed of light in vacuum
    epsilon_0: permittivity of free space
    mu_0     : permeability of free space
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c as c_light, epsilon_0, mu_0, pi

eta_0 = np.sqrt(mu_0 / epsilon_0)   # ~377 ohm


# =============================================================================
# Example 5-1: TE_mn Rectangular Waveguide Dispersion
#   Table 2-4 (Harrington)
#   Cutoff: k_c = sqrt((m*pi/a)^2 + (n*pi/b)^2)
#   Propagation: beta = sqrt(k^2 - k_c^2)   for f > f_c
#   Attenuation (evanescent): alpha = sqrt(k_c^2 - k^2)  for f < f_c
#   Z_mode = eta / sqrt(1 - (f_c/f)^2)   (TE modes)
# =============================================================================

def example_5_1_waveguide_dispersion():
    print("\n  [Example 5-1: Rectangular Waveguide Dispersion]")

    # Standard WR-90 waveguide dimensions
    a_wg = 22.86e-3   # inner broad dimension (m)
    b_wg = 10.16e-3   # inner narrow dimension (m)
    print(f"  WR-90 waveguide: a={a_wg*1e3:.2f} mm, b={b_wg*1e3:.2f} mm")

    modes = [(1, 0), (2, 0), (0, 1), (1, 1)]
    mode_labels = ['TE$_{10}$', 'TE$_{20}$', 'TE$_{01}$', 'TE$_{11}$']
    colors = ['blue', 'green', 'red', 'orange']

    f_c = {}
    for m, n in modes:
        k_c_val = np.sqrt((m*pi/a_wg)**2 + (n*pi/b_wg)**2)
        f_c[(m, n)] = (c_light / (2*pi)) * k_c_val
        print(f"  Mode TE_{m}{n}: f_c = {f_c[(m,n)]/1e9:.3f} GHz,  lambda_c = {2*pi/k_c_val*1e3:.2f} mm")

    # Frequency range: 0.5*f_c(TE10) to 3*f_c(TE10)
    f_min = 0.5 * f_c[(1, 0)]
    f_max = 3.0 * f_c[(1, 0)]
    f_vals = np.linspace(f_min, f_max, 600)

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    for (m, n), label, col in zip(modes, mode_labels, colors):
        k_c_val = np.sqrt((m*pi/a_wg)**2 + (n*pi/b_wg)**2)
        k_vals = 2*pi*f_vals / c_light
        beta = np.sqrt(np.maximum(k_vals**2 - k_c_val**2, 0.0))
        alpha = np.sqrt(np.maximum(k_c_val**2 - k_vals**2, 0.0))

        ratio = f_c[(m, n)] / f_vals
        Z_mode = eta_0 / np.sqrt(np.maximum(1 - ratio**2, 0.0) + 0j)
        Z_mode_real = np.where(ratio < 1, np.real(Z_mode), np.nan)
        Z_mode_imag = np.where(ratio < 1, np.imag(Z_mode), 0.0)

        axes[0].plot(f_vals/1e9, beta, color=col, lw=2, label=label)
        axes[1].plot(f_vals/1e9, alpha * 1e-3, color=col, lw=2, label=label)
        axes[2].plot(f_vals/1e9, Z_mode_real, color=col, lw=2, label=f'{label}: R')

    for (m, n), label in zip(modes, mode_labels):
        fc = f_c[(m, n)]
        for ax in axes[:2]:
            ax.axvline(x=fc/1e9, color='gray', ls=':', lw=0.8)

    axes[0].set_xlabel('Frequency (GHz)')
    axes[0].set_ylabel(r'Phase constant $\beta$ (rad/m)')
    axes[0].set_title(r'Harrington Example 5-1a: $\beta$ vs Frequency')
    axes[0].legend(fontsize=9); axes[0].grid(True, alpha=0.4)

    axes[1].set_xlabel('Frequency (GHz)')
    axes[1].set_ylabel(r'Attenuation $\alpha$ (Np/km)')
    axes[1].set_title(r'$\alpha$ vs Frequency (evanescent below cutoff)')
    axes[1].legend(fontsize=9); axes[1].grid(True, alpha=0.4)

    axes[2].set_xlabel('Frequency (GHz)')
    axes[2].set_ylabel(r"Mode impedance $Z_{\mathrm{TE}}$ ($\Omega$)")
    axes[2].set_title(r"Characteristic Impedance $Z_{\mathrm{mode}}$ vs Frequency")
    axes[2].legend(fontsize=9); axes[2].grid(True, alpha=0.4)
    axes[2].set_ylim(0, 800)

    plt.suptitle('Harrington Example 5-1: Rectangular Waveguide Dispersion', fontsize=12)
    plt.tight_layout()
    path = '/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_5_1_waveguide_dispersion.png'
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [Saved] fig_5_1_waveguide_dispersion.png")

    print(f"\n  [TE_10 guide wavelength vs frequency]")
    for f in [8e9, 10e9, 12e9, 15e9]:
        m, n = 1, 0
        k_c_val = np.sqrt((m*pi/a_wg)**2 + (n*pi/b_wg)**2)
        k_wg = 2*pi*f / c_light
        if k_wg > k_c_val:
            beta_f = np.sqrt(k_wg**2 - k_c_val**2)
            lambda_g = 2*pi / beta_f
            v_p = f / beta_f
            print(f"  f={f/1e9:.1f} GHz: lambda_g={lambda_g*1e3:.2f} mm,  v_p={v_p/c_light:.4f} c")


# =============================================================================
# Example 5-2: Rectangular Cavity Resonator
#   TE_mnp modes: f_mnp = (c/2) * sqrt((m/a)^2 + (n/b)^2 + (p/c)^2)
#   Dominant TE_101 mode when a > b, c > b  (a is widest)
# =============================================================================

def example_5_2_rectangular_cavity():
    print("\n  [Example 5-2: Rectangular Cavity Resonator]")

    a_cav = 30e-3   # m (x dimension)
    b_cav = 30e-3   # m (y dimension)
    c_cav = 30e-3   # m (z dimension)

    print(f"  Cubic cavity: a=b=c={a_cav*1e3:.1f} mm")

    # TE modes: at least one of m,n >= 1, p >= 1
    # (m=0, n=0, p>0 are TM modes; p=0, m>0 or n>0 are TE with k_z=0)
    modes_cavity = []
    for m in range(0, 4):
        for n in range(1, 4):    # n >= 1 for TE (from boundary: sin(n*pi*y/b))
            for p in range(1, 4):
                # TE mode: E_z = 0, H_z present
                # From boundary: sin terms require m>0 or n>0
                if m == 0 and n == 0:
                    continue
                k_sq = (m*pi/a_cav)**2 + (n*pi/b_cav)**2 + (p*pi/c_cav)**2
                f_res = (c_light / 2) * np.sqrt(k_sq)
                modes_cavity.append((m, n, p, f_res))

    modes_cavity.sort(key=lambda x: x[3])
    print("\n  First 10 resonant frequencies (TE_mnp modes):")
    for m, n, p, f in modes_cavity[:10]:
        print(f"  TE_{m}{n}{p}: f_res = {f/1e9:.4f} GHz")

    # TE_101 resonant frequency
    f_101_list = [f for m, n, p, f in modes_cavity if (m, n, p) == (1, 0, 1)]
    if f_101_list:
        f_101 = f_101_list[0]
    else:
        # compute directly
        m, n, p = 1, 0, 1
        k_sq = (m*pi/a_cav)**2 + (n*pi/b_cav)**2 + (p*pi/c_cav)**2
        f_101 = (c_light / 2) * np.sqrt(k_sq)
    print(f"\n  TE_101 mode: f_res = {f_101/1e9:.4f} GHz")

    # Q for copper cavity (Eq. 2-103)
    sigma_cu = 5.8e7
    delta_s = np.sqrt(1.0 / (pi * f_101 * mu_0 * sigma_cu))
    Q_cubic = 1.07e6 / (f_101/1e9)**0.5
    print(f"  Skin depth at {f_101/1e9:.2f} GHz: delta_s = {delta_s*1e6:.4f} µm")
    print(f"  TE_101 Q (copper, ideal cubic): ~{Q_cubic:.0f}")

    # ---- Field pattern for TE_101 ----
    m, n, p = 1, 0, 1
    x = np.linspace(0, a_cav, 80)
    z = np.linspace(0, c_cav, 80)
    X, Z = np.meshgrid(x, z)

    # E_y field: E_y = E_0 * sin(m*pi*x/a) * sin(p*pi*z/c)
    E_y = np.sin(m * pi * X / a_cav) * np.sin(p * pi * Z / c_cav)
    # H_x from Maxwell: H_x ~ -(p*pi/c) * cos(m*pi*x/a) * sin(p*pi*z/c)
    H_x = -(p * pi / c_cav) * np.cos(m * pi * X / a_cav) * np.sin(p * pi * Z / c_cav)
    # H_z from Maxwell: H_z ~ -(m*pi/a) * sin(m*pi*x/a) * cos(p*pi*z/c)
    H_z = -(m * pi / a_cav) * np.sin(m * pi * X / a_cav) * np.cos(p * pi * Z / c_cav)

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    for ax, field, title, label in [
        (axes[0], E_y, rf'TE$_{{101}}$: $E_y$ pattern at $f$={f_101/1e9:.2f} GHz', r'$E_y/E_0$'),
        (axes[1], H_x, rf'TE$_{{101}}$: $H_x$ pattern', r'$H_x/H_0$'),
        (axes[2], H_z, rf'TE$_{{101}}$: $H_z$ pattern', r'$H_z/H_0$'),
    ]:
        im = ax.contourf(X*1e3, Z*1e3, field, levels=20, cmap='RdBu')
        ax.set_xlabel(r'x (mm)'); ax.set_ylabel('z (mm)')
        ax.set_title(title)
        ax.set_aspect('equal')
        plt.colorbar(im, ax=ax, label=label)

    plt.suptitle('Harrington Example 5-2: TE_101 Cavity Field Pattern', fontsize=11)
    plt.tight_layout()
    path = '/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_5_2_cavity_field_pattern.png'
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [Saved] fig_5_2_cavity_field_pattern.png")

    # Q vs frequency for different metals
    f_range = np.linspace(1e9, 30e9, 300)
    Q_range = 1.07e6 / (f_range/1e9)**0.5

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.loglog(f_range/1e9, Q_range, 'b-', lw=2, label='Copper (ideal)')
    ax.set_xlabel('Frequency (GHz)')
    ax.set_ylabel('Quality factor $Q$')
    ax.set_title('Harrington Example 5-2b: Cavity Q vs Frequency\n'
                 r'$Q = 1.07\times10^6/\sqrt{f_{\mathrm{GHz}}}$ (copper, air-filled)')
    ax.grid(True, alpha=0.4, which='both')
    ax.legend()
    plt.tight_layout()
    path = '/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_5_2_cavity_Q.png'
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [Saved] fig_5_2_cavity_Q.png")


if __name__ == '__main__':
    print("=== Harrington Ch5: Rectangular Waveguides and Cavities ===")
    example_5_1_waveguide_dispersion()
    example_5_2_rectangular_cavity()
    print("\n  All Chapter 5 examples complete.")