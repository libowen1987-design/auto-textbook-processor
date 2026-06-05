"""
balanis ch09 - broadband dipoles and matching techniques

Covers:
  1. Cylindrical dipole: impedance vs radius ratio
  2. Folded dipole: impedance transformation (4:1)
  3. Biconical antenna: characteristic impedance vs cone angle
  4. Bandwidth vs dipole radius (King's tables)
  5. Current distribution: thick vs thin dipole

Author: Xiaolongxia
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from typing import Tuple, List
import os
import sys

# Ch8 import for MoM current distribution
sys.path.insert(0, os.path.dirname(__file__))
from balanis_ch08_mom import (hallen_point_matching, hallen_galerkin,
                               half_wave_self_impedance_ch4,
                               ETA_0, PI, C0)

# === Constants ===
FIG_DIR = 'figures/ch09'
os.makedirs(FIG_DIR, exist_ok=True)


# =========================================================================
# 1. Cylindrical Dipole: Impedance vs Radius
# =========================================================================

def example_1_thick_dipole():
    """Example 1: Cylindrical dipole impedance vs radius."""
    print("=" * 65)
    print("  Example 1: Cylindrical Dipole Impedance vs Radius")
    print("=" * 65)
    
    f = 300e6  # 300 MHz
    lam = C0 / f
    k = 2 * PI / lam
    L_dipole = 0.5 * lam  # half-wave
    
    L_over_a_vals = np.array([500, 200, 100, 50])
    R_ref, X_ref = half_wave_self_impedance_ch4()
    
    print(f"\n  Half-wave dipole (L = {L_dipole/lam:.2f}*lambda):")
    print(f"  {'L/a':>8s}  {'a/lambda':>10s}  {'Z_MoM (Ohm)':>20s}")
    print(f"  {'-'*8}  {'-'*10}  {'-'*20}")
    
    Z_mom_list = []
    for L_over_a in L_over_a_vals:
        a_radius = L_dipole / L_over_a
        _, _, R_in, X_in = hallen_point_matching(
            L_dipole, a_radius, k, 51, V_0=1.0)
        Z_mom_list.append(complex(R_in, X_in))
        a_over_lam = 1.0 / (2 * L_over_a)
        print(f"  {L_over_a:>8d}  {a_over_lam:>10.5f}"
              f"  {R_in:8.2f} + j{X_in:7.2f}")
    
    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    Omega_vals = 2 * np.log(L_over_a_vals)
    
    axes[0].semilogy(Omega_vals, [Z.real for Z in Z_mom_list], 'bo-', lw=1.5,
                     label='MoM (Hallen PM)')
    axes[0].axhline(y=R_ref, color='k', ls='--', alpha=0.5,
                    label=f'EMF limit = {R_ref:.1f} Ohm')
    axes[0].set_xlabel('Omega = 2*ln(L/a)', fontsize=13)
    axes[0].set_ylabel('R_in [Ohm]', fontsize=13)
    axes[0].set_title('Input Resistance vs Thickness', fontsize=14)
    axes[0].grid(True, alpha=0.3)
    axes[0].legend(fontsize=10)
    
    axes[1].plot(Omega_vals, [Z.imag for Z in Z_mom_list], 'ro-', lw=1.5,
                 label='MoM (Hallen PM)')
    axes[1].axhline(y=X_ref, color='k', ls='--', alpha=0.5,
                    label=f'EMF limit = {X_ref:.1f} Ohm')
    axes[1].set_xlabel('Omega = 2*ln(L/a)', fontsize=13)
    axes[1].set_ylabel('X_in [Ohm]', fontsize=13)
    axes[1].set_title('Input Reactance vs Thickness', fontsize=14)
    axes[1].grid(True, alpha=0.3)
    axes[1].legend(fontsize=10)
    
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/ch09_ex1_dipole_vs_radius.png', dpi=150)
    plt.close()
    print(f"  -> {FIG_DIR}/ch09_ex1_dipole_vs_radius.png")


# =========================================================================
# 2. Folded Dipole
# =========================================================================

def example_2_folded_dipole():
    """Example 2: Folded dipole impedance at half-wave."""
    print("\n" + "=" * 65)
    print("  Example 2: Folded Dipole Impedance Characteristics")
    print("=" * 65)
    
    f = 300e6
    lam = C0 / f
    k = 2 * PI / lam
    a_radius = 0.001 * lam
    spacing = 0.005 * lam
    
    # Sweep around half-wave (few points for speed)
    L_ratios = np.array([0.35, 0.40, 0.45, 0.48, 0.50, 0.52, 0.55, 0.60, 0.65])
    Z_d_vals = []
    Z_f_vals = []
    
    print(f"  Sweeping L from 0.35 to 0.65 lambda...")
    for i, L_ratio in enumerate(L_ratios):
        L = L_ratio * lam
        _, _, R_d, X_d = hallen_point_matching(L, a_radius, k, 31)
        Z_d = complex(R_d, X_d)
        
        # Folded dipole using twin-line transmission line model
        Z_0 = ETA_0 / PI * np.arccosh(spacing / (2 * a_radius))
        Z_t = 1j * Z_0 * np.tan(k * L / 2)
        Z_f = 4 * Z_d * Z_t / (2 * Z_d + Z_t) if abs(Z_d) > 1e-10 else 4 * Z_d
        
        Z_d_vals.append(Z_d)
        Z_f_vals.append(Z_f)
        
        if (i+1) % 3 == 0:
            print(f"    ... L={L_ratio:.2f}*lambda done")
    
    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    axes[0].plot(L_ratios, [Z.real for Z in Z_d_vals], 'b.-', lw=1.5,
                 label='Dipole (MoM)')
    axes[0].plot(L_ratios, [Z.real for Z in Z_f_vals], 'r.-', lw=1.5,
                 label='Folded Dipole')
    axes[0].axhline(y=300, color='gray', ls=':', alpha=0.5, label='300 Ohm')
    axes[0].set_xlabel('L / lambda', fontsize=13)
    axes[0].set_ylabel('R_in [Ohm]', fontsize=13)
    axes[0].set_title('Input Resistance', fontsize=14)
    axes[0].grid(True, alpha=0.3)
    axes[0].legend(fontsize=10)
    
    axes[1].plot(L_ratios, [Z.imag for Z in Z_d_vals], 'b.-', lw=1.5,
                 label='Dipole (MoM)')
    axes[1].plot(L_ratios, [Z.imag for Z in Z_f_vals], 'r.-', lw=1.5,
                 label='Folded Dipole')
    axes[1].axhline(y=0, color='k', ls='-', lw=0.5, alpha=0.3)
    axes[1].set_xlabel('L / lambda', fontsize=13)
    axes[1].set_ylabel('X_in [Ohm]', fontsize=13)
    axes[1].set_title('Input Reactance', fontsize=14)
    axes[1].grid(True, alpha=0.3)
    axes[1].legend(fontsize=10)
    
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/ch09_ex2_folded_dipole.png', dpi=150)
    plt.close()
    print(f"  -> {FIG_DIR}/ch09_ex2_folded_dipole.png")
    
    # Report at half-wave
    idx = np.argmin(np.abs(L_ratios - 0.50))
    Z_d_h = Z_d_vals[idx]
    Z_f_h = Z_f_vals[idx]
    print(f"\n  At L = 0.50*lambda:")
    print(f"    Dipole:          Z_in = {Z_d_h.real:.1f} + j{Z_d_h.imag:.1f} Ohm")
    print(f"    Folded Dipole:   Z_in = {Z_f_h.real:.1f} + j{Z_f_h.imag:.1f} Ohm")
    print(f"    Ratio (R_f / R_d) = {Z_f_h.real/Z_d_h.real:.2f}x (theory: 4x)")


# =========================================================================
# 3. Biconical Antenna
# =========================================================================

def example_3_biconical_antenna():
    """Example 3: Biconical antenna characteristic impedance."""
    print("\n" + "=" * 65)
    print("  Example 3: Biconical Antenna Characteristics")
    print("=" * 65)
    
    angles_deg = np.linspace(5, 89, 200)
    alpha = np.radians(angles_deg)
    Z_c = ETA_0 / (2 * PI) * np.log(1.0 / np.tan(alpha / 2))
    
    key_angles = [10, 20, 30, 45, 60, 90]
    key_Z = ETA_0 / (2 * PI) * np.log(1.0 / np.tan(np.radians(key_angles) / 2))
    
    print(f"\n  Z_c = eta_0/(2*pi) * ln(cot(alpha/2))")
    print(f"  {'alpha (deg)':>12s}  {'Z_c (Ohm)':>12s}")
    print(f"  {'-'*12}  {'-'*12}")
    for a, z in zip(key_angles, key_Z):
        print(f"  {a:>12d}  {z:>12.1f}")
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    axes[0].plot(angles_deg, Z_c, 'b-', lw=2)
    axes[0].axhline(y=50, color='r', ls='--', alpha=0.5, label='50 Ohm')
    axes[0].axhline(y=75, color='g', ls='--', alpha=0.5, label='75 Ohm')
    axes[0].axhline(y=300, color='orange', ls='--', alpha=0.5, label='300 Ohm')
    axes[0].set_xlabel('Half-Cone Angle alpha [deg]', fontsize=13)
    axes[0].set_ylabel('Z_c [Ohm]', fontsize=13)
    axes[0].set_title('Characteristic Impedance vs Cone Angle', fontsize=14)
    axes[0].grid(True, alpha=0.3)
    axes[0].legend(fontsize=10)
    axes[0].set_xlim(0, 90)
    
    tan_half = np.tan(np.radians(angles_deg) / 2)
    axes[1].semilogy(tan_half, Z_c, 'b-', lw=2)
    axes[1].set_xlabel('tan(alpha/2)', fontsize=13)
    axes[1].set_ylabel('Z_c [Ohm]', fontsize=13)
    axes[1].set_title('Z_c vs tan(alpha/2)', fontsize=14)
    axes[1].grid(True, alpha=0.3)
    axes[1].invert_xaxis()
    
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/ch09_ex3_biconical.png', dpi=150)
    plt.close()
    print(f"  -> {FIG_DIR}/ch09_ex3_biconical.png")


# =========================================================================
# 4. Bandwidth vs Dipole Radius
# =========================================================================

def example_4_bandwidth_vs_radius():
    """Example 4: Swept-frequency impedance for various dipole radii."""
    print("\n" + "=" * 65)
    print("  Example 4: Dipole Bandwidth vs Radius (Frequency Sweep)")
    print("=" * 65)
    
    f_res = 300e6
    lam_res = C0 / f_res
    L_dipole = 0.5 * lam_res
    
    configs = [(500, 'L/a=500'), (100, 'L/a=100'), (50, 'L/a=50')]
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    for L_over_a, label in configs:
        a_radius = L_dipole / L_over_a
        k_res = 2 * PI / lam_res
        
        # Sweep frequency: 0.7 to 1.3 of resonant frequency
        f_frac = np.linspace(0.7, 1.3, 31)
        freq = f_res * f_frac
        R_vals = []
        X_vals = []
        
        print(f"  Computing {label}...")
        for fi in freq:
            ki = 2 * PI * fi / C0
            _, _, R_in, X_in = hallen_point_matching(L_dipole, a_radius, ki, 31)
            R_vals.append(R_in)
            X_vals.append(X_in)
        
        R_vals = np.array(R_vals)
        X_vals = np.array(X_vals)
        
        axes[0].plot(f_frac, R_vals, '.-', lw=1.5, label=label)
        axes[1].plot(f_frac, X_vals, '.-', lw=1.5, label=label)
    
    axes[0].axvline(x=1.0, color='k', ls=':', alpha=0.3)
    axes[0].set_xlabel('f / f_res', fontsize=13)
    axes[0].set_ylabel('R_in [Ohm]', fontsize=13)
    axes[0].set_title('Input Resistance vs Frequency', fontsize=14)
    axes[0].grid(True, alpha=0.3)
    axes[0].legend(fontsize=10)
    
    axes[1].axvline(x=1.0, color='k', ls=':', alpha=0.3)
    axes[1].axhline(y=0, color='k', ls='-', lw=0.5, alpha=0.3)
    axes[1].set_xlabel('f / f_res', fontsize=13)
    axes[1].set_ylabel('X_in [Ohm]', fontsize=13)
    axes[1].set_title('Input Reactance vs Frequency', fontsize=14)
    axes[1].grid(True, alpha=0.3)
    axes[1].legend(fontsize=10)
    
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/ch09_ex4_bandwidth_vs_radius.png', dpi=150)
    plt.close()
    print(f"  -> {FIG_DIR}/ch09_ex4_bandwidth_vs_radius.png")


# =========================================================================
# 5. Current Distribution for Thick vs Thin Dipole
# =========================================================================

def example_5_current_thick_vs_thin():
    """Example 5: Current distribution for thick vs thin dipole."""
    print("\n" + "=" * 65)
    print("  Example 5: Current Distribution: Thick vs Thin Dipole")
    print("=" * 65)
    
    f = 300e6
    lam = C0 / f
    k = 2 * PI / lam
    L_dipole = 0.5 * lam
    N_basis = 51
    
    configs = [
        ('Thin (L/a=500)', 500),
        ('Medium (L/a=100)', 100),
        ('Thick (L/a=50)', 50),
    ]
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    for label, Loa in configs:
        a_radius = L_dipole / Loa
        z_m, I_n, R_in, X_in = hallen_point_matching(L_dipole, a_radius, k, N_basis)
        
        axes[0].plot(z_m / lam, np.abs(I_n), '.-', lw=1.5,
                     label=f'{label}  Z={R_in:.0f}+j{X_in:.0f}Ohm')
        axes[1].plot(z_m / lam, np.angle(I_n, deg=True), '.-', lw=1.5,
                     label=label)
        print(f"  {label:20s}: Z_in = {R_in:7.1f} + j{X_in:7.1f} Ohm")
    
    axes[0].axvline(x=0, color='k', ls=':', alpha=0.3)
    axes[0].set_xlabel('z / lambda', fontsize=13)
    axes[0].set_ylabel('|I(z)| [A]', fontsize=13)
    axes[0].set_title('Current Magnitude: Thick vs Thin Dipole', fontsize=14)
    axes[0].grid(True, alpha=0.3)
    axes[0].legend(fontsize=9)
    
    axes[1].axvline(x=0, color='k', ls=':', alpha=0.3)
    axes[1].set_xlabel('z / lambda', fontsize=13)
    axes[1].set_ylabel('Phase [deg]', fontsize=13)
    axes[1].set_title('Current Phase: Thick vs Thin Dipole', fontsize=14)
    axes[1].grid(True, alpha=0.3)
    axes[1].legend(fontsize=9)
    
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/ch09_ex5_thick_vs_thin_current.png', dpi=150)
    plt.close()
    print(f"  -> {FIG_DIR}/ch09_ex5_thick_vs_thin_current.png")


# =========================================================================
# Main
# =========================================================================

def main():
    print("=" * 65)
    print("  Balanis Ch9: Broadband Dipoles and Matching Techniques")
    print("=" * 65)
    
    # Example 1: Cylindrical dipole impedance vs radius
    example_1_thick_dipole()
    
    # Example 2: Folded dipole
    example_2_folded_dipole()
    
    # Example 3: Biconical antenna
    example_3_biconical_antenna()
    
    # Example 4: Bandwidth vs radius
    example_4_bandwidth_vs_radius()
    
    # Example 5: Current distribution (thick vs thin)
    example_5_current_thick_vs_thin()
    
    print("\n" + "=" * 65)
    print("  Ch9 examples complete.")
    print(f"  Figures saved to: {FIG_DIR}/")
    print("=" * 65)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
