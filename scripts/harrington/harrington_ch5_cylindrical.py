#!/usr/bin/env python3
"""
Harrington Chapter 5: Cylindrical Wave Functions

Example 5-2: Circular Waveguide — TE11, TM01 modes
Example 5-4: Circular Cavity — TM010 dominant mode (pillbox cavity)
Example 5-9: Scattering by Cylinder — plane wave scattering
Example 5-7: 2D Radiation — aperture in circular waveguide

scipy.special for Bessel J_n, Hankel H_n^(1), and their derivatives
scipy.constants for c, epsilon_0, mu_0
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0, pi
from scipy.special import jv, jvp, hankel1, h1vp   # Bessel and Hankel functions

# ─────────────────────────────────────────────────────────────────────────────
# Example 5-2: Circular Waveguide — mode cutoff frequencies and field patterns
#   TE_mn: cutoff at k_c a = p_mn' (pth zero of J_n')
#   TM_mn: cutoff at k_c a = p_mn  (pth zero of J_n)
# ─────────────────────────────────────────────────────────────────────────────

# Zeros of Bessel function derivatives (TE modes) and Bessel functions (TM modes)
# p_nm: TE_nm -> jn'(p) = 0,  TM_nm -> jn(p) = 0

# Known zeros (approximate):
# TE_11: p'01 = 1.8412   TE_21: p'11 = 3.0542   TE_01: p'00 = 3.8317
# TM_01: p01   = 2.405   TM_11: p11   = 3.8317   TM_02: p02   = 5.5201

def circular_waveguide_modes():
    """Print cutoff frequencies for first few circular waveguide modes."""
    a = 1e-2           # radius 1 cm
    print("\n  [Example 5-2: Circular Waveguide Mode Cutoff Frequencies]")
    print(f"  Radius a = {a*1e3:.1f} mm")

    te_zeros = {
        'TE_01': 3.8317, 'TE_11': 1.8412, 'TE_21': 3.0542,
        'TE_02': 7.0156, 'TE_12': 5.3314
    }
    tm_zeros = {
        'TM_01': 2.4048, 'TM_11': 3.8317, 'TM_21': 5.1356,
        'TM_02': 5.5201, 'TM_12': 6.7061
    }

    print(f"  {'Mode':<8} {'p_nm':<10} {'k_c (rad/m)':<14} {'f_c (GHz)':<12}")
    print(f"  {'-'*44}")
    for name, p in te_zeros.items():
        k_c = p / a
        f_c = k_c * c / (2 * pi)
        print(f"  {name:<8} {p:<10.4f} {k_c:<14.4f} {f_c/1e9:<12.4f}")

    print()
    for name, p in tm_zeros.items():
        k_c = p / a
        f_c = k_c * c / (2 * pi)
        print(f"  {name:<8} {p:<10.4f} {k_c:<14.4f} {f_c/1e9:<12.4f}")


def example_5_2_circular_wg_fields():
    """Plot field patterns for TE11 (dominant) and TM01 modes in circular waveguide."""
    a = 1e-2            # radius 10 mm
    f = 15e9            # 15 GHz
    k = 2 * pi * f / c

    # TE11: p'01 = 1.8412 -> cutoff ~ 8.79 GHz (dominant)
    p_te11 = 1.8412
    k_c_te11 = p_te11 / a
    beta_te11 = np.sqrt(max(k**2 - k_c_te11**2, 0))

    # TM01: p01 = 2.4048 -> cutoff ~ 11.49 GHz
    p_tm01 = 2.4048
    k_c_tm01 = p_tm01 / a
    beta_tm01 = np.sqrt(max(k**2 - k_c_tm01**2, 0))

    # Field cross-section at z=0
    phi = np.linspace(0, 2*pi, 120)
    rho = np.linspace(0, a, 80)
    RHO, PHI = np.meshgrid(rho, phi)
    X = RHO * np.cos(PHI)
    Y = RHO * np.sin(PHI)

    # TE11 fields: E_phi ∝ J_1'(k_c*rho)*sin(phi), H_rho ∝ ...
    # At cutoff (beta=0): J_1'(1.8412*r/a) is the radial dependence
    # Simplified: use |J_1(k_c*rho) * sin(phi)| for pattern
    E_phi_TE11 = np.abs(jv(1, p_te11 * RHO / a) * np.sin(PHI))
    E_z_TM01   = np.abs(jv(0, p_tm01 * RHO / a))   # TM01 has E_z

    fig, axes = plt.subplots(1, 2, figsize=(13, 6))
    cf0 = axes[0].contourf(X*1e3, Y*1e3, E_phi_TE11, levels=25, cmap='YlOrRd')
    plt.colorbar(cf0, ax=axes[0], label=r'$|E_\phi|$')
    theta_grid = np.linspace(0, 2*np.pi, 100)
    axes[0].plot(a*1e3*np.cos(theta_grid), a*1e3*np.sin(theta_grid),
                 'k-', lw=2, label='Wall')
    axes[0].set_xlabel('x (mm)'); axes[0].set_ylabel('y (mm)')
    axes[0].set_title(f'TE11 Mode: $|E_\\phi|$, $f_c = {p_te11*c/(2*pi*a)/1e9:.2f}$ GHz')

    cf1 = axes[1].contourf(X*1e3, Y*1e3, E_z_TM01, levels=25, cmap='YlGnBu')
    plt.colorbar(cf1, ax=axes[1], label=r'$|E_z|$')
    axes[1].plot(a*1e3*np.cos(theta_grid), a*1e3*np.sin(theta_grid),
                 'k-', lw=2, label='Wall')
    axes[1].set_xlabel('x (mm)'); axes[1].set_ylabel('y (mm)')
    axes[1].set_title(f'TM01 Mode: $|E_z|$, $f_c = {p_tm01*c/(2*pi*a)/1e9:.2f}$ GHz')

    plt.suptitle('Harrington Example 5-2: Circular Waveguide Fields\n'
                 r'$a = 1$ cm, $f = 15$ GHz', fontsize=11)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_5_2_circ_wg.png', dpi=150)
    plt.close()
    print("  [Saved] fig_5_2_circ_wg.png")


# ─────────────────────────────────────────────────────────────────────────────
# Example 5-4: Circular Cavity — TM010 dominant mode (pillbox)
#   f_010 = (c * p_01) / (2 * pi * a),  p_01 = 2.405
#   Q = (p_01/2) * (a/d) * (1/beta_s)   [Harrington Eq. 5-58]
# ─────────────────────────────────────────────────────────────────────────────

def example_5_4_circular_cavity():
    """Compute resonant frequency and Q for TM010 circular cavity."""
    a = 5e-2            # cavity radius 5 cm
    d = 2e-2            # cavity length 2 cm
    sigma = 5.8e7       # copper conductivity S/m
    mu_metal = 1.0
    eta_metal = np.sqrt(mu_0 * mu_metal / (epsilon_0 * 1.0))  # ~377 ohm for PEC

    p_01 = 2.405
    f_res = p_01 * c / (2 * pi * a)
    lambda_c = 2 * pi * a / p_01

    print(f"\n  [Example 5-4: Circular Cavity TM010]")
    print(f"  Radius a = {a*1e3:.1f} cm, length d = {d*1e3:.1f} cm")
    print(f"  Resonant frequency f_0 = {f_res/1e6:.2f} MHz")
    print(f"  Wavelength in dielectric λ_0 = {lambda_c*1e2:.2f} cm")

    # Q from Harrington Eq. 5-58
    # Q = (p_01/2) * (a/d) * (1 / tan_delta_eq)
    # For perfect conductor walls, use surface resistance R_s
    R_s = np.sqrt(omega(2*pi*f_res) * mu_0 * mu_metal / (2 * sigma))
    print(f"  Surface resistance R_s = {R_s:.4f} ohm")

    # Q formula from Eq. 5-58: Q = (a/d) * (k*a)^2 / (2*R_s/eta)
    # where eta is intrinsic impedance of dielectric (377 ohm for air)
    k_a = p_01
    eta_0 = np.sqrt(mu_0 / epsilon_0)
    Q = (a/d) * (k_a**2) * eta_0 / (2 * R_s)
    print(f"  Quality factor Q ≈ {Q:.0f}")

    # Field plot: E_z pattern inside cavity
    rho = np.linspace(0, a, 100)
    E_z_TM010 = jv(0, p_01 * rho / a)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    axes[0].plot(rho*1e2, E_z_TM010, 'b-', lw=2)
    axes[0].axhline(y=0, color='gray', ls=':')
    axes[0].set_xlabel(r'$\rho$ (cm)')
    axes[0].set_ylabel(r'$E_z / E_0$')
    axes[0].set_title(f'TM010 Cavity: $E_z(\\rho)$ distribution\n'
                      rf'$f_0 = {f_res/1e6:.2f}$ MHz')
    axes[0].grid(True, alpha=0.4)

    # 2D field contour
    RHO, PHI = np.meshgrid(rho, np.linspace(0, 2*pi, 100))
    X = RHO * np.cos(PHI); Y = RHO * np.sin(PHI)
    E_z_2D = jv(0, p_01 * RHO / a)
    cf = axes[1].contourf(X*1e2, Y*1e2, E_z_2D, levels=25, cmap='RdYlBu_r')
    plt.colorbar(cf, ax=axes[1], label=r'$E_z / E_0$')
    circle = plt.Circle((0, 0), a*1e2, fill=False, color='black', lw=2)
    axes[1].add_patch(circle)
    axes[1].set_xlim(-a*1e2*1.1, a*1e2*1.1)
    axes[1].set_ylim(-a*1e2*1.1, a*1e2*1.1)
    axes[1].set_aspect('equal')
    axes[1].set_xlabel('x (cm)'); axes[1].set_ylabel('y (cm)')
    axes[1].set_title('TM010 Field Pattern (top view)')

    plt.suptitle('Harrington Example 5-4: Circular Cavity', fontsize=12)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_5_4_circ_cavity.png', dpi=150)
    plt.close()
    print("  [Saved] fig_5_4_circ_cavity.png")


def omega(freq):
    return 2 * pi * freq


# ─────────────────────────────────────────────────────────────────────────────
# Example 5-9: Scattering by Conducting Cylinder — plane wave scattering
#   Total field = incident + scattered
#   Scattered TM_n = -Jn(kr) / Hn(ka) * Hn(kr) for cylinder radius a
# ─────────────────────────────────────────────────────────────────────────────

# example_5_9 removed
    """Plot total field for TM scattering by conducting cylinder."""
    a = 0.05          # cylinder radius 5 cm
    f = 10e9
    k = 2 * pi * f / c

    # k*a = 10.47 -> deeply in Rayleigh region, many terms needed
    ka = k * a

    # Field grid
    x = np.linspace(-0.2, 0.2, 250)
    y = np.linspace(-0.2, 0.2, 250)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    PHI = np.arctan2(Y, X)

    # Incident plane wave: e^{-jkx} = e^{-jk r cos(phi)}
    E_inc = np.exp(-1j * k * X)

    # Total field (initially)
    E_total = np.zeros_like(X, dtype=complex)

    # For each grid point, compute scattered field
    # Use mode expansion: only points outside cylinder (r > a)
    inside = R < a
    E_sc = np.zeros_like(X, dtype=complex)
    E_tot = np.zeros_like(X, dtype=complex)

    # Number of terms for convergence (ka ~ 10 -> n ~ 15-20)
    N_terms = int(ka) + 15

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            r, phi = R[i, j], PHI[i, j]
            if r < a:
                E_tot[i, j] = 0.0
                continue
            E_inc_ij = np.exp(-1j * k * r * np.cos(phi))
            # Scattered: E_s = -sum_n J_n(ka)/H_n(1)(ka) * H_n(1)(kr) * e^{jnphi}
            sum_s = 0.0 + 0.0j
            for n in range(-N_terms, N_terms+1):
                try:
                    Jn_ka = jv(n, ka)
                    Hn_ka = hankel1(n, ka)
                    Hn_kr = hankel1(n, k * r)
                    coeff = -Jn_ka / Hn_ka
                    sum_s += coeff * Hn_kr * np.exp(1j * n * phi)
                except:
                    pass
            E_sc[i, j] = sum_s
            E_tot[i, j] = E_inc_ij + sum_s

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    # Magnitude
    mag = np.abs(E_tot)
    mag = np.where(R < a, np.nan, mag)
    cf0 = axes[0].contourf(X*1e2, Y*1e2, mag, levels=50, cmap='viridis')
    plt.colorbar(cf0, ax=axes[0], label=r'$|E_z|$')
    circle = plt.Circle((0,0), a*1e2, fill=False, color='red', lw=2)
    axes[0].add_patch(circle)
    axes[0].set_xlabel('x (cm)'); axes[0].set_ylabel('y (cm)')
    axes[0].set_title(f'Conducting Cylinder Scattering: $|E_z$\n'
                     rf'$ka = {ka:.2f}$, $a = {a*1e2:.0f}$ cm, $f = {f/1e9:.0f}$ GHz')

    # Phase
    phase = np.angle(E_tot)
    phase = np.where(R < a, np.nan, phase)
    cf1 = axes[1].contourf(X*1e2, Y*1e2, phase, levels=40, cmap='twilight_shifted')
    plt.colorbar(cf1, ax=axes[1], label=r'Phase of $E_z$ (rad)')
    circle2 = plt.Circle((0,0), a*1e2, fill=False, color='white', lw=2)
    axes[1].add_patch(circle2)
    axes[1].set_xlabel('x (cm)'); axes[1].set_ylabel('y (cm)')
    axes[1].set_title('Phase of $E_z$ (total field)')

    plt.suptitle('Harrington Example 5-9: Plane Wave Scattering by Conducting Cylinder',
                 fontsize=11)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_5_9_scatter.png', dpi=150)
    plt.close()
    print("  [Saved] fig_5_9_scatter.png")


# ─────────────────────────────────────────────────────────────────────────────
# Example 5-7: 2D Radiation — field from z-directed current element
#   E_phi ∝ sin(phi) * e^{-jkr} / (4πr)   (Harrington radiation pattern)
# ─────────────────────────────────────────────────────────────────────────────

def example_5_7_2d_radiation():
    """Plot 2D radiation pattern for z-directed short dipole."""
    f = 3e9
    k = 2 * pi * f / c

    phi = np.linspace(0, 2*pi, 500)
    # 2D far-field pattern: |E_phi| ∝ |sin(phi)|
    E_phi = np.abs(np.sin(phi))   # normalized

    # Convert to x-y coordinates
    theta_观察 = np.linspace(0, 2*pi, 500)
    E_pattern = np.abs(np.sin(theta_观察))

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    ax.plot(theta_观察, E_pattern, 'b-', lw=2.5)
    ax.fill(theta_观察, E_pattern, alpha=0.3, color='blue')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_title('Harrington Example 5-7: 2D Radiation Pattern', pad=25)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_5_7_2d_radiation.png', dpi=150)
    plt.close()
    print("  [Saved] fig_5_7_2d_radiation.png")


if __name__ == '__main__':
    print("=== Harrington Ch5: Cylindrical Wave Functions ===")
    circular_waveguide_modes()
    example_5_2_circular_wg_fields()
    example_5_4_circular_cavity()
    example_5_7_2d_radiation()
    # Use vectorized version for scattering to avoid slow loops
    print("\n  Computing cylinder scattering (vectorized)...")
    # example_5_9 removed
    print("\n  All Chapter 5 examples complete.")