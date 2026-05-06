#!/usr/bin/env python3
"""
Harrington Chapter 2: Introduction to Waves

Example 2-5: Reflection of Plane Waves (Fresnel Coefficients)
Example 2-6: Transmission Line Analogy for TEM Waves

Physical constants from scipy.constants:
    c        : speed of light in vacuum
    epsilon_0: permittivity of free space
    mu_0     : permeability of free space
    eta_0    : intrinsic impedance of free space = sqrt(mu_0/epsilon_0)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0, pi
from numpy import sqrt

# ─────────────────────────────────────────────────────────────────────────────
# Example 2-5: Fresnel Reflection Coefficients
# Plane wave incident from medium 1 (epsilon_r1, mu_r1=1) onto medium 2
# ─────────────────────────────────────────────────────────────────────────────

def fresnel_coefficients(epsilon_r1, epsilon_r2, mu_r1=1.0, mu_r2=1.0,
                         theta_i_deg=30.0, polarization='TE'):
    """
    Compute Fresnel reflection and transmission coefficients for a plane wave
    incident from medium 1 onto medium 2 at angle theta_i.

    Parameters
    ----------
    epsilon_r1, epsilon_r2 : relative permittivities
    mu_r1, mu_r2           : relative permeabilities (default 1.0)
    theta_i_deg            : incidence angle in degrees
    polarization           : 'TE' (s-polarization) or 'TM' (p-polarization)

    Returns
    -------
    R, T : complex reflection and transmission coefficients
    """
    theta_i = np.deg2rad(theta_i_deg)
    n1 = np.sqrt(epsilon_r1 * mu_r1)
    n2 = np.sqrt(epsilon_r2 * mu_r2)
    sin_theta_t = (n1 / n2) * np.sin(theta_i)

    # Check total internal reflection
    if abs(sin_theta_t) > 1.0 + 1e-12:
        print("  [Total Internal Reflection] |sin_theta_t| > 1")
        return None, None

    cos_theta_t = np.sqrt(1 - sin_theta_t**2)
    k1 = 2 * pi * 1e9 / c          # wave number at 1 GHz
    Z1 = sqrt(mu_r1 / epsilon_r1)   # relative impedance medium 1
    Z2 = sqrt(mu_r2 / epsilon_r2)   # relative impedance medium 2

    if polarization == 'TE':
        # TE (s-polarization): E perpendicular to plane of incidence
        R = (Z2 * np.cos(theta_i) - Z1 * cos_theta_t) / \
            (Z2 * np.cos(theta_i) + Z1 * cos_theta_t)
        T = 2 * Z2 * np.cos(theta_i) / (Z2 * np.cos(theta_i) + Z1 * cos_theta_t)
    else:
        # TM (p-polarization): E parallel to plane of incidence
        R = (Z1 * np.cos(theta_i) - Z2 * cos_theta_t) / \
            (Z1 * np.cos(theta_i) + Z2 * cos_theta_t)
        T = 2 * Z1 * np.cos(theta_i) / (Z1 * np.cos(theta_i) + Z2 * cos_theta_t)

    return R, T

def example_2_5_fresnel():
    """Plot |R| vs incidence angle for air-to-dielectric interface."""
    epsilon_r = 2.1   # typical dielectric (Teflon)
    theta_vals = np.linspace(0, 89, 500)

    R_TE = []; R_TM = []
    for th in theta_vals:
        R, _ = fresnel_coefficients(1.0, epsilon_r, 1.0, 1.0, th, 'TE')
        R_TE.append(abs(R) if R is not None else 1.0)
        R, _ = fresnel_coefficients(1.0, epsilon_r, 1.0, 1.0, th, 'TM')
        R_TM.append(abs(R) if R is not None else 1.0)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(theta_vals, R_TE, 'b-', lw=2, label=r'TE (s-pol) $|R|$')
    ax.plot(theta_vals, R_TM, 'r--', lw=2, label=r'TM (p-pol) $|R|$')
    ax.axhline(y=1.0, color='gray', ls=':', lw=1)
    theta_B = np.rad2deg(np.arctan(np.sqrt(epsilon_r)))  # Brewster angle
    ax.axvline(x=theta_B, color='green', ls='--', lw=1.5,
               label=f'Brewster angle = {theta_B:.1f}°')
    ax.set_xlabel(r'Incidence angle $\theta_i$ (deg)')
    ax.set_ylabel(r'Amplitude reflection coefficient $|R|$')
    ax.set_title('Harrington Example 2-5: Fresnel Reflection Coefficients\n'
                 r'$\epsilon_{r1}=1$, $\epsilon_{r2}=2.1$ (air→Teflon)')
    ax.legend(); ax.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_2_5_fresnel.png',
                dpi=150)
    plt.close()
    print("  [Saved] fig_2_5_fresnel.png")

# ─────────────────────────────────────────────────────────────────────────────
# Example 2-6: Transmission Line Analogy - TEM wave on parallel-plate
# Z0 = (d/w) * sqrt(mu/epsilon)  (per-unit-width characteristic impedance)
# ─────────────────────────────────────────────────────────────────────────────

def example_2_6_transmission_line():
    """Compute and plot the per-unit-length L and C of a parallel-plate line."""
    f = 10e9              # 10 GHz
    omega = 2 * pi * f
    d = 2e-3              # plate separation (m)
    w = 10e-3             # plate width (m)
    epsilon_r = 2.1

    # Intrinsic impedance of dielectric
    eta = np.sqrt(mu_0 / (epsilon_r * epsilon_0))   # wave impedance
    # Per-unit-length capacitance (parallel plate)
    C_pl = epsilon_r * epsilon_0 * w / d
    # Per-unit-length inductance
    L_pl = mu_0 * d / w

    # Characteristic impedance
    Z0 = np.sqrt(L_pl / C_pl)
    print(f"\n  [Example 2-6: Parallel-Plate Transmission Line]")
    print(f"  Plate separation d = {d*1e3:.1f} mm, width w = {w*1e3:.1f} mm")
    print(f"  epsilon_r = {epsilon_r}")
    print(f"  L' = {L_pl*1e9:.4f} nH/m,  C' = {C_pl*1e12:.4f} pF/m")
    print(f"  Z0 = {Z0:.4f} ohm")

    # Phase velocity
    v_p = 1 / np.sqrt(L_pl * C_pl)
    print(f"  Phase velocity = {v_p*1e-6:.2f} × 10^6 m/s "
          f"({v_p/c*100:.1f}% of c)")

    # Plot L and C vs frequency
    f_vals = np.linspace(1e9, 20e9, 300)
    Z0_vals = np.full_like(f_vals, Z0)   # lossless: Z0 constant

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    # Z0 vs frequency (flat for lossless)
    axes[0].plot(f_vals/1e9, Z0_vals, 'b-', lw=2)
    axes[0].set_xlabel('Frequency (GHz)')
    axes[0].set_ylabel(r'$Z_0$ ($\Omega$)')
    axes[0].set_title('Characteristic Impedance (Lossless)\n'
                      r'$Z_0 = \sqrt{L/C}$ constant')
    axes[0].grid(True, alpha=0.4)

    # Field lines between plates (electrostatic approximation)
    x = np.linspace(0, w, 200)
    y = np.linspace(0, d, 100)
    X, Y = np.meshgrid(x, y)
    E_z = np.ones_like(X)   # uniform field for parallel plate
    # Stream function for E field lines
    axes[1].set_title(r'Electric field $E_z$ between plates (uniform)')
    axes[1].set_xlabel('x (m)'); axes[1].set_ylabel('y (m)')
    cf = axes[1].contourf(X*1e3, Y*1e3, E_z, levels=10, cmap='YlOrRd')
    axes[1].set_title(r'$E_z$ field (uniform, $V/d$)')
    plt.colorbar(cf, ax=axes[1], label=r'$E_z$ (V/m)')
    for ax in axes:
        ax.set_xlabel('x (mm)'); ax.set_ylabel('y (mm)')

    plt.suptitle('Harrington Example 2-6: Parallel-Plate Transmission Line', fontsize=12)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_2_6_tline.png', dpi=150)
    plt.close()
    print("  [Saved] fig_2_6_tline.png")


# ─────────────────────────────────────────────────────────────────────────────
# Example 2-4: Wave Propagation in Lossy Medium
#   gamma = alpha + j*beta = sqrt(j*omega*mu*(sigma + j*omega*epsilon))
# ─────────────────────────────────────────────────────────────────────────────

def example_2_4_lossy_medium():
    """Compute alpha, beta for a lossy medium at various frequencies."""
    print("\n  [Example 2-4: Waves in Lossy Matter]")
    sigma = 0.1          # conductivity S/m (moderate loss)
    epsilon_r = 4.0
    mu_r = 1.0
    f_vals = np.linspace(100e6, 10e9, 400)   # 100 MHz to 10 GHz

    alpha = np.zeros_like(f_vals)
    beta  = np.zeros_like(f_vals)

    for i, f in enumerate(f_vals):
        omega = 2 * pi * f
        # gamma^2 = j*omega*mu*(sigma + j*omega*epsilon)
        k_sq = 1j * omega * mu_0 * mu_r * (sigma + 1j * omega * epsilon_r * epsilon_0)
        gamma = np.sqrt(k_sq)
        alpha[i] = np.real(gamma)
        beta[i]  = np.imag(gamma)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].plot(f_vals/1e9, alpha * 1e3, 'b-', lw=2)
    axes[0].set_xlabel('Frequency (GHz)')
    axes[0].set_ylabel(r'Attenuation constant $\alpha$ (Np/m)')
    axes[0].set_title(r'Harrington Example 2-4: $\alpha$ vs Frequency')
    axes[0].grid(True, alpha=0.4)

    axes[1].plot(f_vals/1e9, beta, 'r-', lw=2)
    axes[1].set_xlabel('Frequency (GHz)')
    axes[1].set_ylabel(r'Phase constant $\beta$ (rad/m)')
    axes[1].set_title(r'$\beta$ vs Frequency (Lossy Medium, $\sigma=0.1$ S/m)')
    axes[1].grid(True, alpha=0.4)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_2_4_lossy.png', dpi=150)
    plt.close()
    print("  [Saved] fig_2_4_lossy.png")


if __name__ == '__main__':
    print("=== Harrington Ch2: Introduction to Waves ===")
    example_2_4_lossy_medium()
    example_2_5_fresnel()
    example_2_6_transmission_line()
    print("\n  All Chapter 2 examples complete.")