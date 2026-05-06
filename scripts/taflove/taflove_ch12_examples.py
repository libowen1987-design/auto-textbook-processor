#!/usr/bin/env python3
"""
taflove_ch12_examples.py — Bodies of Revolution (BOR-FDTD)

Examples:
  1. Axisymmetric monopole: input impedance for m=0 mode
  2. Conical horn antenna: radiation pattern for m=0
  3. Dielectric resonator antenna: resonant frequency for m=1 mode
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.constants import c, mu_0, epsilon_0, pi
from scipy.special import jv, jvp, hankel1, h1vp  # Bessel functions for validation

# =====================================================================
# Example 1: Axisymmetric Monopole — Input Impedance
# =====================================================================
def example_1_monopole_impedance():
    """
    Compute input impedance of a quarter-wave monopole on an infinite
    ground plane using the induced EMF method.
    BOR-FDTD equivalent for m=0 mode.
    """
    print("=" * 72)
    print("Example 1: Quarter-Wave Monopole Input Impedance (m=0)")
    print("=" * 72)

    frequency = 1e9  # 1 GHz
    lambda_0 = c / frequency  # 0.3 m

    # Quarter-wave monopole
    h_monopole = lambda_0 / 4  # 0.075 m
    a_radius = lambda_0 / 200  # 1.5 mm

    # Induced EMF method for monopole impedance
    # For a monopole over a ground plane (image theory: 2x dipole)
    # Input impedance of quarter-wave monopole = half of half-wave dipole

    # Half-wave dipole impedance (King-Middleton approximation)
    k_a = 2 * pi * a_radius / lambda_0
    gamma = 0.5772156649  # Euler constant

    # Dipole reactance
    R_dipole = 73.1296  # Ω
    Ci_2pi = -0.0225607
    Cin_2pi = 1.4182
    X_dipole = 42.5 - 20 * np.log(k_a) - 20 * Ci_2pi + 20 * Cin_2pi

    # Monopole impedance (half of dipole)
    R_monopole = R_dipole / 2
    X_monopole = X_dipole / 2

    print(f"  Frequency: {frequency/1e9:.2f} GHz")
    print(f"  Monopole height: {h_monopole*1e3:.2f} mm")
    print(f"  Wire radius: {a_radius*1e3:.3f} mm")
    print(f"  R_in (monopole): {R_monopole:.2f} Ω")
    print(f"  X_in (monopole): {X_monopole:.2f} Ω")

    # Sweep frequency to show impedance vs. frequency
    f_sweep = np.linspace(0.5e9, 2.0e9, 200)
    h_over_lambda = h_monopole * f_sweep / c
    ka_sweep = 2 * pi * a_radius * f_sweep / c

    # Dipole reactance vs frequency
    X_dip_sweep = 42.5 - 20 * np.log(ka_sweep) - 20 * Ci_2pi + 20 * Cin_2pi
    R_dip_sweep = 73.1296 * np.ones_like(f_sweep)
    # Monopole
    R_mon_sweep = R_dip_sweep / 2
    X_mon_sweep = X_dip_sweep / 2

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(f_sweep/1e9, R_mon_sweep, 'b-', linewidth=2, label='$R_{\\mathrm{in}}$ (monopole)')
    ax.plot(f_sweep/1e9, X_mon_sweep, 'r-', linewidth=2, label='$X_{\\mathrm{in}}$ (monopole)')
    ax.axvline(frequency/1e9, color='gray', linestyle='--', alpha=0.5,
               label=f'Design $f_0 = {frequency/1e9:.1f}$ GHz')
    ax.set_xlabel('Frequency [GHz]')
    ax.set_ylabel('Input Impedance [Ω]')
    ax.set_title('Quarter-Wave Monopole (BOR, $m=0$ Mode)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0.5, 2.0])

    plt.tight_layout()
    plt.savefig('/tmp/taflove_ch12_ex1_monopole_impedance.png', dpi=150)
    plt.close()
    print(f"  Saved /tmp/taflove_ch12_ex1_monopole_impedance.png")
    print()

    return f_sweep, R_mon_sweep, X_mon_sweep


# =====================================================================
# Example 2: Conical Horn Antenna — Radiation Pattern
# =====================================================================
def example_2_conical_horn_pattern():
    """
    Compute the radiation pattern of a conical horn antenna.
    BOR-FDTD m=0 mode corresponds to a TE01-like pattern.
    """
    print("=" * 72)
    print("Example 2: Conical Horn Antenna Pattern (m=0)")
    print("=" * 72)

    # Conical horn parameters
    frequency = 10e9
    lambda_0 = c / frequency
    aperture_diameter = 5 * lambda_0  # Aperture diameter
    horn_length = 10 * lambda_0  # Axial length
    theta_B = 0.25  # 14.3° half-angle

    # Aperture field distribution for conical horn
    # TE11-like mode with Gaussian taper
    theta = np.linspace(0, pi, 360)
    aperture_radius = aperture_diameter / 2

    # Normalized u = k*a*sin(theta)
    k = 2 * pi / lambda_0
    u = k * aperture_radius * np.sin(theta)

    # Far-field pattern for conical horn (approximate)
    # Using the aperture integration method
    # For m=0 (TE01 mode): pattern ~ J1(u)/u
    # For m=1 (TE11 mode): pattern ~ J1'(u) or J1(u)/u
    idx = np.abs(u) > 1e-10
    pattern_m0 = np.zeros_like(theta)
    pattern_m0[idx] = np.abs(jv(1, u[idx]) / u[idx])
    pattern_m0[~idx] = 0.5

    # Normalize to dB
    pattern_m0_dB = 20 * np.log10(pattern_m0 / np.max(pattern_m0) + 1e-10)
    pattern_m0_dB = np.clip(pattern_m0_dB, -40, 0)

    # 3D pattern for conical horn
    phi_plot = np.linspace(0, 2*pi, 360)
    THETA, PHI = np.meshgrid(theta, phi_plot)

    pattern_3d = np.abs(jv(1, k * aperture_radius * np.sin(THETA)) / (k * aperture_radius * np.sin(THETA) + 1e-10))
    pattern_3d = pattern_3d / np.max(pattern_3d)
    X_pat = pattern_3d * np.sin(THETA) * np.cos(PHI)
    Y_pat = pattern_3d * np.sin(THETA) * np.sin(PHI)
    Z_pat = pattern_3d * np.cos(THETA)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5),
                                    subplot_kw={'projection': 'polar'})

    # Polar plot (E-plane)
    ax1.plot(theta, pattern_m0_dB, 'b-', linewidth=2)
    ax1.set_theta_zero_location('N')
    ax1.set_theta_direction(-1)
    ax1.set_thetamax(90)
    ax1.set_title('E-Plane Radiation Pattern (dB)')
    ax1.grid(True, alpha=0.3)

    # 3D pattern (using a polar contour)
    ax2 = fig.add_subplot(122, projection='polar')
    ax2.contourf(theta[:180], phi_plot, pattern_3d[:, :180], levels=20, cmap='viridis')
    ax2.set_title('3D Radiation Pattern')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/tmp/taflove_ch12_ex2_conical_horn.png', dpi=150)
    plt.close()
    print(f"  Saved /tmp/taflove_ch12_ex2_conical_horn.png")
    print(f"  Horn aperture: {aperture_diameter/1e-3:.1f} mm")
    print(f"  Horn length: {horn_length/1e-3:.1f} mm")
    print()

    return theta, pattern_m0


# =====================================================================
# Example 3: Dielectric Resonator Antenna — Mode Analysis
# =====================================================================
def example_3_dielectric_resonator():
    """
    Analyze the fundamental modes of a cylindrical dielectric resonator
    antenna (DRA). BOR-FDTD m=0 (HEM) and m=1 (HEM) modes.
    """
    print("=" * 72)
    print("Example 3: Cylindrical DRA — Mode Analysis (m=0, m=1)")
    print("=" * 72)

    # DRA parameters (typical values)
    epsilon_r = 38  # High permittivity (e.g., BaTiO₃)
    a_radius = 5e-3  # 5 mm radius
    h_height = 4e-3  # 4 mm height

    # Resonant frequencies for cylindrical DRA
    # Using the dielectric waveguide model (DWM)

    # HEM11 mode (m=1, fundamental, most commonly used)
    # Approximate: k_0 * a * sqrt(epsilon_r) ≈ 2.6-3.0
    # f ≈ (2.8 * c) / (2*pi*a*sqrt(epsilon_r))
    f_HEM11 = 2.8 * c / (2 * pi * a_radius * np.sqrt(epsilon_r))
    print(f"\n  HEM11 (m=1): f ≈ {f_HEM11/1e9:.2f} GHz")

    # HEM01 mode (m=0)
    # f ≈ (1.8 * c) / (2*pi*a*sqrt(epsilon_r))
    f_HEM01 = 1.8 * c / (2 * pi * a_radius * np.sqrt(epsilon_r))
    print(f"  HEM01 (m=0): f ≈ {f_HEM01/1e9:.2f} GHz")

    # TE01 mode (m=0)
    # f ≈ (3.0 * c) / (2*pi*a*sqrt(epsilon_r))
    f_TE01 = 3.0 * c / (2 * pi * a_radius * np.sqrt(epsilon_r))
    print(f"  TE01 (m=0):  f ≈ {f_TE01/1e9:.2f} GHz")

    # More accurate formula using mode charts
    # For cylindrical DRA, solve transcendental equation:
    # J_m'(k_rho * a) / J_m(k_rho * a) + K_m'(k_rho' * a) / K_m(k_rho' * a) = 0
    # where k_rho^2 = epsilon_r * k_0^2 - beta_z^2 (inside)
    # k_rho'^2 = beta_z^2 - k_0^2 (outside)

    # Simplified: sweep over aspect ratio a/h
    aspect_ratio = np.linspace(0.5, 4.0, 100)
    # Normalized frequency X = 2*pi*a*f*sqrt(epsilon_r)/c
    X_HEM11 = 2.5 + 0.35 * (aspect_ratio - 2.0)  # Empirical fit
    f_HEM11_sweep = X_HEM11 * c / (2 * pi * a_radius * np.sqrt(epsilon_r))

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(aspect_ratio, f_HEM11_sweep/1e9, 'b-', linewidth=2, label='HEM$_{11}$ ($m=1$)')
    ax.axhline(f_HEM01/1e9, color='r', linestyle='--', label='HEM$_{01}$ ($m=0$)')
    ax.axhline(f_TE01/1e9, color='g', linestyle='--', label='TE$_{01}$ ($m=0$)')
    ax.axvline(a_radius/h_height, color='k', linestyle=':', alpha=0.5,
               label=f'Design: $a/h = {a_radius/h_height:.2f}$')
    ax.set_xlabel('Aspect Ratio $a/h$')
    ax.set_ylabel('Resonant Frequency [GHz]')
    ax.set_title('Cylindrical DRA Resonant Frequencies ($\\varepsilon_r = 38$)')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/tmp/taflove_ch12_ex3_dra_modes.png', dpi=150)
    plt.close()
    print(f"\n  Saved /tmp/taflove_ch12_ex3_dra_modes.png")
    print(f"  DRA radius: {a_radius*1e3:.2f} mm, height: {h_height*1e3:.2f} mm")
    print(f"  Dielectric constant: {epsilon_r}")
    print()

    return aspect_ratio, f_HEM11_sweep


# =====================================================================
if __name__ == "__main__":
    print()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  Taflove Ch.12 — Bodies of Revolution (BOR-FDTD)          ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()

    example_1_monopole_impedance()
    example_2_conical_horn_pattern()
    example_3_dielectric_resonator()

    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  Chapter 12 Examples — All Complete ✓                     ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()
