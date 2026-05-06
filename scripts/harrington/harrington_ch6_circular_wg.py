#!/usr/bin/env python3
"""
Harrington Chapter 6: Circular Waveguides

Example 6-1: Circular Waveguide TE/TM Modes
Example 6-2: Cavity Resonators (Circular/TM_010 mode)

Physical constants from scipy.constants:
    c        : speed of light in vacuum
    epsilon_0: permittivity of free space
    mu_0     : permeability of free space
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn, jn_zeros
from scipy.constants import c, epsilon_0, mu_0, pi

eta_0 = np.sqrt(mu_0 / epsilon_0)   # ~377 ohm


# =============================================================================
# Example 6-1: Circular Waveguide Modes
#   Waveguide radius a
#   TE modes: H_z present, eigenvalues p'_mn (Bessel J derivative zeros)
#   TM modes: E_z present, eigenvalues p_mn (Bessel J zeros)
#
#   TE_mn cutoff: k_c = p'_mn / a
#   TM_mn cutoff: k_c = p_mn  / a
# =============================================================================

def example_6_1_circular_wg_modes():
    """
    Compute cutoff frequencies for the first several TE and TM modes
    in a circular waveguide (radius a).  Plot the field patterns (E_phi, H_r)
    for the dominant TE_11 mode.
    """
    print("\n  [Example 6-1: Circular Waveguide Modes]")

    a = 10e-3   # waveguide radius (m)
    print(f"  Circular waveguide radius a = {a*1e3:.1f} mm")

    # Bessel zeros and their derivatives
    # TM modes: p_mn = jn(m, n) -- zeros of J_m
    # TE modes: p'_mn = jn'(m, n) -- zeros of J_m' (derivative)
    # We need the first few zeros for m=0,1,2,...
    def get_bessel_zeros(m, n_max=5):
        """Approximate Bessel J_m zeros using jn_zeros"""
        # jn_zeros(m, n) gives first n zeros of J_m
        if m == 0:
            return jn_zeros(0, n_max)
        else:
            return jn_zeros(m, n_max)

    def get_bessel_derivative_zeros(m, n_max=5):
        """Approximate zeros of dJ_m(x)/dx using derivative approximation"""
        zeros = []
        for n in range(1, n_max+1):
            # Approximate root of J_m'(x): use root-finding near jn_zeros(m,n)
            from scipy.optimize import brentq
            import warnings
            try:
                def deriv(x):
                    return (jn(m-1, x) - m * jn(m, x) / x) if m > 0 else -jn(1, x)
                # Use approximate position from jn zeros shifted slightly
                z_approx = jn_zeros(m, n)[n-1] if n <= len(jn_zeros(m, 1)) else jn_zeros(m, 1)[0] + (n-1)*pi
                z_lo = max(0.01, z_approx - 0.5)
                z_hi = z_approx + 0.5
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore')
                    z = brentq(deriv, z_lo, z_hi)
                zeros.append(z)
            except Exception:
                # Fallback: use approximate formula
                zeros.append((n + m/2 - 0.25) * pi if m == 0 else (n + m/2 - 0.25) * pi)
        return np.array(zeros)

    # Get TM mode eigenvalues (zeros of J_m)
    print("\n  TM modes (zeros of J_m):")
    tm_modes = []
    for m in [0, 1, 2]:
        p_vals = get_bessel_zeros(m, 3)
        for n, p in enumerate(p_vals):
            k_c = p / a
            f_c = (c / (2*pi)) * k_c
            print(f"  TM_{m}{n+1}: p_{m}{n+1}={p:.4f}, f_c={f_c/1e9:.4f} GHz")
            tm_modes.append((m, n+1, p, f_c))

    # Get TE mode eigenvalues (zeros of J_m')
    print("\n  TE modes (zeros of J_m'):")
    te_modes = []
    for m in [0, 1, 2]:
        try:
            pprime_vals = get_bessel_derivative_zeros(m, 3)
        except Exception:
            pprime_vals = np.array([3.83, 7.02, 10.17][:3])  # fallback for m=0
            if m == 1:
                pprime_vals = np.array([1.84, 5.33, 8.54][:3])
            elif m == 2:
                pprime_vals = np.array([3.05, 6.71, 9.97][:3])
        for n, p in enumerate(pprime_vals[:3]):
            k_c = p / a
            f_c = (c / (2*pi)) * k_c
            print(f"  TE_{m}{n+1}: p'_{m}{n+1}={p:.4f}, f_c={f_c/1e9:.4f} GHz")
            te_modes.append((m, n+1, p, f_c))

    # Sort all modes by cutoff frequency
    all_modes = [(f'TM_{m}{n}', p, f_c) for m, n, p, f_c in tm_modes] + \
                [(f'TE_{m}{n}', p, f_c) for m, n, p, f_c in te_modes]
    all_modes.sort(key=lambda x: x[2])

    print(f"\n  Dominant mode: {all_modes[0][0]} with f_c={all_modes[0][2]/1e9:.4f} GHz")

    # ---- Field pattern for dominant TE_11 mode ----
    # TE_11: J_1(p'11 * rho/a) * cos(phi) for E_rho, etc.
    # Dominant TE_11: p'_11 ≈ 1.8412
    p_prime_11 = te_modes[0][2] if te_modes[0][0] == 1 and te_modes[0][1] == 1 else 1.8412

    rho = np.linspace(0, a, 80)
    phi_vals = np.linspace(0, 2*pi, 80)
    RHO, PHI = np.meshgrid(rho, phi_vals)

    # E_phi (transverse electric field) for TE_11:
    # E_phi = E_0 * (a/p'_11) * J_1(p'_11*rho/a) * cos(phi)  [simplified]
    m_val = 1
    J1_arg = p_prime_11 * RHO / a
    E_phi = jn(m_val, J1_arg) * np.cos(m_val * PHI)

    # H_rho = ...  (from Maxwell's equations)
    k_c_val = p_prime_11 / a
    k = 2*pi * 15e9 / c   # plot at 15 GHz
    inside = k**2 - k_c_val**2
    if inside > 0:
        beta = np.sqrt(inside)
        Z_TE = eta_0 / np.sqrt(1 - (k_c_val/k)**2 + 0j)
        # H_rho from E_phi / Z_TE (simplified)
        H_rho = -E_phi / np.real(Z_TE)  # approximate
    else:
        H_rho = E_phi * 0.0

    fig, axes = plt.subplots(1, 2, figsize=(12, 5), subplot_kw={'projection': 'polar'})

    # E_phi pattern
    im0 = axes[0].contourf(PHI, RHO*1e3, E_phi, levels=20, cmap='RdBu')
    axes[0].set_title(rf'TE$_{{11}}$: $E_\phi$ pattern\n($\rho$ in mm)', pad=15)
    axes[0].set_theta_zero_location('E')
    plt.colorbar(im0, ax=axes[0], shrink=0.6)

    # H_rho pattern
    im1 = axes[1].contourf(PHI, RHO*1e3, H_rho, levels=20, cmap='RdBu')
    axes[1].set_title(rf'TE$_{{11}}$: $H_\rho$ pattern\n($\rho$ in mm)', pad=15)
    axes[1].set_theta_zero_location('E')
    plt.colorbar(im1, ax=axes[1], shrink=0.6)

    plt.suptitle('Harrington Example 6-1: Circular Waveguide TE_11 Mode Fields', fontsize=11)
    plt.tight_layout()
    path = '/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_6_1_circular_wg_mode.png'
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [Saved] fig_6_1_circular_wg_mode.png")

    # Plot cutoff frequencies comparison (bar chart)
    fig, ax = plt.subplots(figsize=(10, 4))
    labels = [m[0] for m in all_modes[:12]]
    fcs = [m[2]/1e9 for m in all_modes[:12]]
    cols = ['blue' if 'TE' in m[0] else 'red' for m in all_modes[:12]]
    ax.barh(labels, fcs, color=cols, alpha=0.7)
    ax.set_xlabel('Cutoff frequency $f_c$ (GHz)')
    ax.set_title('Harrington Example 6-1b: Circular Waveguide Mode Chart\n'
                 r'$a=10$ mm, radius')
    ax.grid(True, alpha=0.4, axis='x')
    plt.tight_layout()
    path = '/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_6_1_mode_chart.png'
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [Saved] fig_6_1_mode_chart.png")


# =============================================================================
# Example 6-2: Circular Cavity Resonator
#   TM_010 mode (dominant TM mode, no zeros of J_0 at m=0)
#   TM_010: f_res = chi_01 / (2*pi*a*sqrt(mu*eps))  [chi_01 = p_01 ~ 2.405]
# =============================================================================

def example_6_2_circular_cavity():
    """
    Compute resonant frequencies for the first TM_mnp modes in a circular
    cavity, and plot field patterns for the TM_010 dominant mode.
    """
    print("\n  [Example 6-2: Circular Cavity Resonator]")

    a = 30e-3   # cavity radius (m)
    b = 15e-3   # cavity height (m)
    print(f"  Circular cavity: radius a={a*1e3:.1f} mm, height b={b*1e3:.1f} mm")

    # TM_mnp modes in circular cavity (Harrington Sec. 4-3 and 6-4)
    # TM modes: E_z = E_0 * J_m(k_c*rho) * exp(±j*m*phi) * cos(p*pi*z/b)
    # where k_c = chi_mn / a   (chi_mn = zero of J_m)
    # and k_z = p*pi/b
    # f_mnp = (c/2) * sqrt( (chi_mn/a)^2 + (p/b)^2 )  [for nonmagnetic]
    print("\n  TM modes (E_z dominant):")
    chi_01 = jn_zeros(0, 1)[0]   # ~2.405
    chi_11 = jn_zeros(1, 1)[0]   # ~3.832
    chi_02 = jn_zeros(0, 2)[0]   # ~5.520

    tm_modes_cav = []
    for m in [0, 1]:
        for n in [1, 2]:
            for p in [0, 1]:
                chi = jn_zeros(m, n)[n-1]
                k_c = chi / a
                k_z = p * pi / b
                f_res = (c / (2*pi)) * np.sqrt(k_c**2 + k_z**2)
                label = f"TM_{m}{n}{p}"
                print(f"  {label}: chi_{m}{n}={chi:.4f}, f_res={f_res/1e9:.4f} GHz")
                tm_modes_cav.append((label, f_res))

    # Dominant mode: TM_010 (chi_01 ≈ 2.405, p=0 => k_z=0)
    f_010 = (c / (2*pi)) * (chi_01 / a)
    print(f"\n  Dominant TM mode: TM_010 at f_res = {f_010/1e9:.4f} GHz")

    # Quality factor for TM_010 cavity (copper walls)
    # Q ~ (chi_01 * a) / (2 * delta_s)   where delta_s = skin depth
    delta_s = np.sqrt(1.0 / (pi * f_010 * mu_0 * 5.8e7))
    R_s = np.sqrt(pi * f_010 * mu_0 / 5.8e7)
    # For TM_010 (similar to cylindrical cavity): Q ≈ chi_01/(2*delta_s/a + ...)
    Q_010 = chi_01 * a / (2 * delta_s)
    print(f"  Skin depth at {f_010/1e9:.2f} GHz: delta_s = {delta_s*1e6:.4f} µm")
    print(f"  TM_010 quality factor (copper): Q ~ {Q_010:.0f}")

    # ---- Field pattern for TM_010 ----
    rho = np.linspace(0, a, 80)
    z = np.linspace(0, b, 80)
    RHO, Z = np.meshgrid(rho, z)

    # E_z pattern: J_0(chi_01 * rho / a)  (independent of phi and z for TM_010)
    E_z = jn(0, chi_01 * RHO / a)

    # E_rho = 0 for TM_010 (p=0, no z variation)
    # H_phi from Maxwell: H_phi = ... ~ j*omega*eps * E_z / k_c  for TM mode
    H_phi = (f_010 * 2*pi*epsilon_0) * jn(1, chi_01 * RHO / a) * (a/chi_01)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].contourf(RHO*1e3, Z*1e3, E_z, levels=20, cmap='RdBu')
    axes[0].set_xlabel(r'$\rho$ (mm)')
    axes[0].set_ylabel('z (mm)')
    axes[0].set_title(rf'TM$_{{010}}$: $E_z$ field pattern at $f$={f_010/1e9:.3f} GHz')
    plt.colorbar(axes[0].collections[0], ax=axes[0], label=r'$E_z/E_0$')

    axes[1].contourf(RHO*1e3, Z*1e3, H_phi, levels=20, cmap='RdBu')
    axes[1].set_xlabel(r'$\rho$ (mm)')
    axes[1].set_ylabel('z (mm)')
    axes[1].set_title(rf'TM$_{{010}}$: $H_\phi$ field pattern')
    plt.colorbar(axes[1].collections[0], ax=axes[1], label=r'$H_\phi/H_0$')

    plt.suptitle('Harrington Example 6-2: Circular Cavity TM_010 Field Pattern', fontsize=11)
    plt.tight_layout()
    path = '/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_6_2_circular_cavity.png'
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [Saved] fig_6_2_circular_cavity.png")

    # Q factor vs frequency for different modes
    tm_modes_sorted = sorted(tm_modes_cav, key=lambda x: x[1])
    f_vals_q = np.array([f for _, f in tm_modes_sorted])
    Q_vals = chi_01 * a / (2 * np.sqrt(1.0 / (pi * f_vals_q * mu_0 * 5.8e7)))

    fig, ax = plt.subplots(figsize=(8, 4))
    labels_q = [label for label, _ in tm_modes_sorted]
    ax.semilogy(labels_q, Q_vals, 'bo-', lw=2, markersize=7)
    ax.set_xlabel('TM Mode')
    ax.set_ylabel('Quality factor $Q$ (copper)')
    ax.set_title('Harrington Example 6-2b: TM Cavity Mode Q Factors')
    ax.grid(True, alpha=0.4)
    plt.tight_layout()
    path = '/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_6_2_cavity_Q.png'
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [Saved] fig_6_2_cavity_Q.png")


if __name__ == '__main__':
    print("=== Harrington Ch6: Circular Waveguides and Cavities ===")
    example_6_1_circular_wg_modes()
    example_6_2_circular_cavity()
    print("\n  All Chapter 6 examples complete.")