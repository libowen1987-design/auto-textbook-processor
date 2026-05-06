#!/usr/bin/env python3
"""
Harrington Chapter 4: Cylindrical Wave Functions

Example 4-1: Bessel J_n, Neumann Y_n, Hankel H_n functions
Example 4-2: Circular Waveguide TE_11 Mode Field Patterns
Example 4-3: Dielectric Rod / Step-Index Fiber (LP modes)

Physical constants from scipy.constants:
    c        : speed of light in vacuum
    epsilon_0: permittivity of free space
    mu_0     : permeability of free space
    eta_0    : intrinsic impedance of free space (~377 ohm)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.special import jn, yn, hankel1, hankel2, jn_zeros
from scipy.constants import c, epsilon_0, mu_0, pi

eta_0 = np.sqrt(mu_0 / epsilon_0)


# =============================================================================
# Example 4-1: Cylindrical Wave Functions (Bessel, Neumann, Hankel)
#   Harrington Section 4-3
# =============================================================================

def example_4_1_cylindrical_wave_functions():
    print("\n  [Example 4-1: Cylindrical Wave Functions]")

    k = 10.0   # wave number (rad/m)
    rho_vals = np.linspace(0.01, 10.0, 300)

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    for n in [0, 1, 2]:
        Jn = jn(n, k * rho_vals)
        Yn = yn(n, k * rho_vals)
        axes[0].plot(rho_vals, Jn, lw=2, label=f'J_{n}(x)')
        axes[1].plot(rho_vals, Yn, lw=2, label=f'Y_{n}(x)')

    axes[0].set_xlabel('rho (m)')
    axes[0].set_ylabel('J_n(k*rho)')
    axes[0].set_title('Harrington Ex 4-1a: Bessel Functions J_n(k*rho)')
    axes[0].legend(); axes[0].grid(True, alpha=0.4)
    axes[0].axhline(y=0, color='k', lw=0.5)

    axes[1].set_xlabel('rho (m)')
    axes[1].set_ylabel('Y_n(k*rho)')
    axes[1].set_title('Harrington Ex 4-1b: Neumann Functions Y_n(k*rho)\n(singular at rho=0)')
    axes[1].legend(); axes[1].grid(True, alpha=0.4)
    axes[1].axhline(y=0, color='k', lw=0.5)

    # Hankel functions: H_n^(1)=J_n+jY_n (outgoing), H_n^(2)=J_n-jY_n (incoming)
    n_val = 0
    H1 = hankel1(n_val, k * rho_vals)
    H2 = hankel2(n_val, k * rho_vals)
    axes[2].plot(rho_vals, np.real(H1), 'b-', lw=2, label='Re[H_0^(1)]')
    axes[2].plot(rho_vals, np.imag(H1), 'b--', lw=2, label='Im[H_0^(1)]')
    axes[2].plot(rho_vals, np.real(H2), 'r-', lw=2, label='Re[H_0^(2)]')
    axes[2].plot(rho_vals, np.imag(H2), 'r--', lw=2, label='Im[H_0^(2)]')
    axes[2].set_xlabel('rho (m)')
    axes[2].set_ylabel('H_n^(1,2)(k*rho)')
    axes[2].set_title('Harrington Ex 4-1c: Hankel Functions\n'
                      'H_n^(1)=J_n+jY_n (outgoing), H_n^(2)=J_n-jY_n (incoming)')
    axes[2].legend(fontsize=8); axes[2].grid(True, alpha=0.4)
    axes[2].axhline(y=0, color='k', lw=0.5)

    plt.suptitle('Harrington Example 4-1: Cylindrical Wave Functions', fontsize=12)
    plt.tight_layout()
    path = '/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_4_1_cylindrical_wave_funcs.png'
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [Saved] fig_4_1_cylindrical_wave_funcs.png")

    # Wronskian check: W(J_n, Y_n) = 2/(pi*x)
    x_test = np.linspace(0.5, 8, 100)
    J0 = jn(0, x_test)
    Y0 = yn(0, x_test)
    # Wronskian W(J_0, Y_0) = J_0 * dY_0/dx - Y_0 * dJ_0/dx = 2/(pi*x)
    dJ0 = (jn(-1, x_test) + jn(1, x_test)) / 2   # dJ_0/dx = -J_1
    dY0 = (yn(-1, x_test) + yn(1, x_test)) / 2
    W_appr = J0 * dY0 - Y0 * dJ0
    W_exact = 2.0 / (pi * x_test)
    print(f"  [Wronskian] At x=1: W_appr={W_appr[np.argmin(np.abs(x_test-1))]:.4f},  W_exact={2/np.pi:.4f}")


# =============================================================================
# Example 4-2: Circular Waveguide TE_11 Mode Fields
#   Harrington Section 4-3 / Chapter 6
#   TE_11 dominant mode: p'_11 = 1.8412, f_c ~ 11.24 GHz for a=10mm
# =============================================================================

def example_4_2_circular_wg_fields():
    print("\n  [Example 4-2: Circular Waveguide TE_11 Mode]")

    a_wg = 15e-3   # waveguide radius (m)
    f = 10e9       # frequency (Hz)
    k_wg = 2*pi*f / c

    p_prime_11 = 1.8412   # zero of J_1'(x)
    k_c = p_prime_11 / a_wg
    f_c = (c / (2*pi)) * k_c
    print(f"  Waveguide radius a={a_wg*1e3:.1f} mm")
    print(f"  TE_11: p'_11={p_prime_11}, f_c={f_c/1e9:.3f} GHz, k_c={k_c:.2f} rad/m")

    if k_wg > k_c:
        print(f"  f={f/1e9:.1f} GHz > f_c, TE_11 is propagating")
        beta = np.sqrt(k_wg**2 - k_c**2)
        Z_TE = eta_0 / np.sqrt(1 - (k_c/k_wg)**2)
        print(f"  beta={beta:.2f} rad/m, Z_TE={Z_TE:.2f} ohm")
    else:
        print(f"  f={f/1e9:.1f} GHz < f_c, TE_11 is evanescent")

    rho = np.linspace(0.01, a_wg, 80)
    phi = np.linspace(0, 2*pi, 80)
    RHO, PHI = np.meshgrid(rho, phi)

    m_val = 1
    J1_arg = p_prime_11 * RHO / a_wg
    J1 = jn(m_val, J1_arg)
    # dJ_1/dx = (J_0(x) - J_2(x))/2  etc
    dJ1 = (jn(m_val-1, J1_arg) - m_val * jn(m_val, J1_arg) / J1_arg)

    E_phi = J1 * np.cos(m_val * PHI)             # phi component of E
    H_rho = -dJ1 * np.cos(m_val * PHI)           # rho component of H
    H_phi = J1 * np.sin(m_val * PHI)             # phi component of H

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5), subplot_kw={'projection': 'polar'})

    for ax, field, label in [
        (axes[0], E_phi, 'E_phi'),
        (axes[1], H_rho, 'H_rho'),
        (axes[2], H_phi, 'H_phi'),
    ]:
        im = ax.contourf(PHI, RHO*1e3, field, levels=20, cmap='RdBu')
        ax.set_theta_zero_location('E')
        ax.set_title(f'{label} pattern', pad=15)
        plt.colorbar(im, ax=ax, shrink=0.6)

    plt.suptitle('Harrington Example 4-2: Circular WG TE_11 Fields', fontsize=11)
    plt.tight_layout()
    path = '/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_4_2_circular_wg_fields.png'
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [Saved] fig_4_2_circular_wg_fields.png")


# =============================================================================
# Example 4-3: Dielectric Rod Waveguide (Step-Index Fiber)
#   LP_mn modes, V-number, single-mode condition
# =============================================================================

def example_4_3_dielectric_rod():
    print("\n  [Example 4-3: Dielectric Rod / Step-Index Fiber]")

    a_core = 4e-6    # core radius (m) - single-mode fiber
    n1 = 1.47        # core refractive index
    n2 = 1.46        # cladding refractive index
    lmbda_0 = 1550e-9  # operating wavelength (m)

    k_0 = 2*pi / lmbda_0
    NA = np.sqrt(n1**2 - n2**2)
    V = k_0 * a_core * NA
    print(f"  Core radius a = {a_core*1e6:.1f} um")
    print(f"  n1={n1}, n2={n2},  NA={NA:.4f}")
    print(f"  V-number = {V:.4f}  (SM cutoff V=2.405) => "
          f"{'SINGLE-MODE' if V < 2.405 else 'MULTI-MODE'}")

    n_eff = n2 + (n1 - n2) * min((V / 2.405)**2, 1.0)
    beta_LP01 = k_0 * n_eff
    print(f"  LP_01 effective index: n_eff ~ {n_eff:.5f}")
    print(f"  LP_01 propagation constant: beta ~ {beta_LP01:.4f} rad/m")

    U = V * np.sqrt(max(1 - (V/2.405)**2, 0))
    W = np.sqrt(max(V**2 - U**2, 0))
    print(f"  Normalised: U={U:.4f}, W={W:.4f}")

    rho = np.linspace(0, 2*a_core, 200)
    rho_core = rho[rho <= a_core]
    rho_clad = rho[rho > a_core]
    J0_core = jn(0, U * rho_core / a_core)
    field_core = J0_core / (J0_core.max() + 1e-12)
    field_clad = J0_core[-1] / (J0_core.max() + 1e-12) * np.exp(-W * (rho_clad - a_core) / a_core)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

    axes[0].plot(rho_core*1e6, field_core, 'b-', lw=2, label='Core (J_0 pattern)')
    axes[0].plot(rho_clad*1e6, field_clad, 'r--', lw=2, label='Cladding (evanescent)')
    axes[0].axvline(x=a_core*1e6, color='gray', ls=':', label=f'a={a_core*1e6:.1f} um')
    axes[0].set_xlabel('rho (um)')
    axes[0].set_ylabel('|E| (normalised)')
    axes[0].set_title(f'LP_01 Mode Field Profile\n'
                      f'Stepfiber, V={V:.2f}, lambda={lmbda_0*1e9:.0f} nm')
    axes[0].legend(); axes[0].grid(True, alpha=0.4)

    lmbda_range = np.linspace(800e-9, 1700e-9, 200)
    V_range = (2*pi / lmbda_range) * a_core * NA
    axes[1].plot(lmbda_range*1e9, V_range, 'b-', lw=2)
    axes[1].axhline(y=2.405, color='red', ls='--', lw=1.5, label='SM cutoff (V=2.405)')
    axes[1].set_xlabel('Wavelength lambda_0 (nm)')
    axes[1].set_ylabel('V-number')
    axes[1].set_title(f'V-number vs Wavelength\n'
                      f'Core radius {a_core*1e6:.1f} um,  NA={NA:.3f}')
    axes[1].legend(); axes[1].grid(True, alpha=0.4)

    plt.suptitle('Harrington Example 4-3: Dielectric Rod Waveguide', fontsize=11)
    plt.tight_layout()
    path = '/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_4_3_dielectric_rod.png'
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [Saved] fig_4_3_dielectric_rod.png")


if __name__ == '__main__':
    print("=== Harrington Ch4: Cylindrical Wave Functions ===")
    example_4_1_cylindrical_wave_functions()
    example_4_2_circular_wg_fields()
    example_4_3_dielectric_rod()
    print("\n  All Chapter 4 examples complete.")