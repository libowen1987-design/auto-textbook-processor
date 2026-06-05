#!/usr/bin/env python3
"""
Harrington Chapter 1: Fundamental Concepts

Example 1-1: Complex Permittivity and Loss Tangent
Example 1-2: Complex Poynting Vector and Power

Physical constants from scipy.constants:
    c        : speed of light in vacuum
    epsilon_0: permittivity of free space
    mu_0     : permeability of free space
    eta_0    : intrinsic impedance of free space
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import (
    c, epsilon_0, mu_0, pi,
    speed_of_light as c_val
)
from scipy.special import j0, j1

eta_0 = np.sqrt(mu_0 / epsilon_0)   # ~377 ohm


# =============================================================================
# Example 1-1: Complex Permittivity and Loss Tangent
#   eps_c(w) = eps' - j*eps''
#   tan_delta = eps'' / eps'
# =============================================================================

def example_1_1_complex_permittivity():
    """
    Plot complex permittivity and loss tangent vs frequency for a typical
    dielectric (Debye model approximation), and compare with polystyrene
    data from Fig. 1-10 of Harrington.
    """
    print("\n  [Example 1-1: Complex Permittivity and Loss Tangent]")
    eps_r_static = 2.56   # relative permittivity at DC (polystyrene)
    eps_r_infinity = 1.0   # relative permittivity at optical freq
    tau_relaxation = 1e-10  # relaxation time (Debye model, ~ps range)
    sigma_dc = 0.0         # no DC conductivity for polystyrene

    f_vals = np.logspace(6, 10, 500)   # 1 MHz to 10 GHz

    omega = 2 * pi * f_vals
    eps_r_complex = eps_r_infinity + (eps_r_static - eps_r_infinity) / (1 + 1j * omega * tau_relaxation)

    eps_prime = np.real(eps_r_complex)
    eps_doubleprime = np.imag(eps_r_complex)
    tan_delta = eps_doubleprime / eps_prime

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    axes[0].loglog(f_vals/1e9, eps_prime, 'b-', lw=2)
    axes[0].set_xlabel('Frequency (GHz)')
    axes[0].set_ylabel(r'$\epsilon_r^\prime$')
    axes[0].set_title(r'Harrington Example 1-1a: $\epsilon_r^\prime$ vs Frequency')
    axes[0].grid(True, alpha=0.4, which='both')

    axes[1].semilogx(f_vals/1e9, tan_delta, 'r-', lw=2)
    axes[1].set_xlabel('Frequency (GHz)')
    axes[1].set_ylabel(r'$\tan\delta = \epsilon_r^{\prime\prime}/\epsilon_r^\prime$')
    axes[1].set_title(r'$\tan\delta$ vs Frequency (Debye model, $\epsilon_r^{dc}=2.56$)')
    axes[1].grid(True, alpha=0.4)

    axes[2].semilogx(f_vals/1e9, eps_doubleprime, 'g-', lw=2)
    axes[2].set_xlabel('Frequency (GHz)')
    axes[2].set_ylabel(r'$\epsilon_r^{\prime\prime}$')
    axes[2].set_title(r'$\epsilon_r^{\prime\prime}$ (loss factor) vs Frequency')
    axes[2].grid(True, alpha=0.4)

    plt.suptitle('Harrington Example 1-1: Complex Permittivity', fontsize=13)
    plt.tight_layout()
    path = '/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_1_1_complex_permittivity.png'
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [Saved] fig_1_1_complex_permittivity.png")

    # Print some values at key frequencies
    for f in [1e6, 1e9, 10e9]:
        idx = np.argmin(np.abs(f_vals - f))
        print(f"  f={f/1e6:.0f} MHz: eps'={eps_prime[idx]:.4f}, tan_d={tan_delta[idx]:.4f}")


# =============================================================================
# Example 1-2: Complex Poynting Vector and Power
#   S = E x H*   (complex Poynting)
#   P_avg = Re(S) = time-average power density
# =============================================================================

def example_1_2_complex_poynting():
    """
    Compute and visualise the complex Poynting vector for a uniform plane
    wave in a lossy medium (good dielectric).  Compare the time-average
    power density with the instantaneous power density.
    """
    print("\n  [Example 1-2: Complex Poynting Vector and Power]")

    f = 3e9             # 3 GHz
    omega = 2 * pi * f
    eps_r = 2.1 - 1j * 0.002   # slightly lossy dielectric (tan_d ~ 0.001)
    mu_r = 1.0

    eps = eps_r * epsilon_0
    mu = mu_r * mu_0

    # Intrinsic wave number and impedance
    k_sq = 1j * omega * mu * (1j * omega * eps + 0.0)
    gamma = np.sqrt(k_sq)          # in lossless medium gamma = omega*sqrt(mu*eps)
    k = omega * np.sqrt(mu * eps)  # complex wave number
    eta = np.sqrt(mu / eps)       # complex intrinsic impedance

    print(f"  k = {k:.4f} rad/m")
    print(f"  eta = {eta:.4f} ohm")
    print(f"  lambda = {2*pi/np.real(k):.4f} m")

    # Uniform plane wave, z-polarised, +z travelling
    E_0 = 1.0   # V/m (rms)
    z_vals = np.linspace(0, 5 * (2*pi/np.real(k)), 500)

    E_z = E_0 * np.exp(-1j * k * z_vals)
    H_x = E_z / eta   # because E_z / H_x = eta for +z travel

    # Complex Poynting vector S = E x H*
    # E = u_z E_z, H = u_x H_x  =>  S = u_z x u_x * E_z * H_x* = -u_y * E_z * H_x*
    S_complex = E_z * np.conj(H_x)   # = -u_y * S_complex
    S_real = np.real(S_complex)    # time-average power density
    S_imag = np.imag(S_complex)     # reactive power density

    # For lossless dielectric: S_real should be constant (= eta * |H|^2)
    # For slightly lossy: decays exponentially
    skin_depth = 1.0 / np.imag(k) if np.imag(k) > 0 else np.inf

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    axes[0].plot(z_vals*100, np.abs(E_z), 'b-', lw=2, label=r'$|E_z|$')
    axes[0].plot(z_vals*100, np.abs(H_x), 'r--', lw=2, label=r'$|H_x|$')
    axes[0].set_xlabel('z (cm)')
    axes[0].set_ylabel('Field magnitude (V/m)')
    axes[0].set_title('Field amplitudes: $|E_z|$, $|H_x|$ vs z')
    axes[0].legend(); axes[0].grid(True, alpha=0.4)

    axes[1].plot(z_vals*100, S_real, 'b-', lw=2, label=r'$\mathrm{Re}(S_y)$ = avg power')
    axes[1].plot(z_vals*100, S_imag, 'g--', lw=2, label=r'$\mathrm{Im}(S_y)$ = reactive')
    axes[1].set_xlabel('z (cm)')
    axes[1].set_ylabel(r'$S_y$ (W/m$^2$)')
    axes[1].set_title('Complex Poynting: real (avg) and imag (reactive)')
    axes[1].legend(); axes[1].grid(True, alpha=0.4)

    # Instantaneous fields (for animation sketch, plot at 3 instants)
    t_vals = [0, pi/(4*omega), pi/(2*omega)]
    colors = ['blue', 'green', 'red']
    for t, col in zip(t_vals, colors):
        E_inst = np.sqrt(2) * np.real(E_z * np.exp(1j*omega*t))
        axes[2].plot(z_vals*100, E_inst, color=col, lw=1.5,
                     label=f't={t*1e12:.1f} ps')
    axes[2].set_xlabel('z (cm)')
    axes[2].set_ylabel(r'$\mathcal{E}_z$ (V/m)')
    axes[2].set_title('Instantaneous $E_z$ at several time instants')
    axes[2].legend(); axes[2].grid(True, alpha=0.4)

    plt.suptitle('Harrington Example 1-2: Complex Poynting Vector', fontsize=13)
    plt.tight_layout()
    path = '/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_1_2_poynting.png'
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [Saved] fig_1_2_poynting.png")
    print(f"  Skin depth (for eps_r={eps_r}): {skin_depth*100:.2f} cm")


if __name__ == '__main__':
    print("=== Harrington Ch1: Fundamental Concepts ===")
    example_1_1_complex_permittivity()
    example_1_2_complex_poynting()
    print("\n  All Chapter 1 examples complete.")