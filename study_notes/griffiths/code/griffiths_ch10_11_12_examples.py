#!/usr/bin/env python3
"""Griffiths Ch.10-12: Potentials, Radiation, Relativity"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

plt.style.use('seaborn-v0_8')
mu0, eps0 = constants.mu_0, constants.epsilon_0
c = constants.c

# === Ch.10 ===
def example_10_1_moving_charge():
    """Fields of a point charge moving at constant velocity."""
    q, v = 1e-9, 0.8*c
    beta = v/c; gamma = 1/np.sqrt(1-beta**2)
    theta = np.linspace(0, 2*np.pi, 200)
    r = 1.0  # distance in plane perpendicular to motion
    # Coulomb field (in rest frame) transformed: E = (q/(4pi*eps0*r^2)) * (1-beta^2)/(1-beta^2*sin^2(theta))^(3/2)
    numerator = 1 - beta**2
    denominator = (1 - (beta*np.sin(theta))**2)**(3.0/2.0)
    E_mag = q/(4*np.pi*eps0*r**2) * numerator/denominator
    fig, ax = plt.subplots(figsize=(8, 5), subplot_kw={'projection': 'polar'})
    ax.plot(theta, E_mag, 'b-', linewidth=2)
    ax.set_title(f'E-field of moving charge (v={beta:.1f}c)')
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch10_ex1_moving_charge.png', dpi=150)
    plt.close(fig)
    print(f"[Ch.10] Moving charge: v={beta}c, gamma={gamma:.2f}")
    print(f"  E_max/E_rest = {E_mag.max()/(q/(4*np.pi*eps0*r**2)):.2f}")
    print("Figure saved: griffiths_ch10_ex1_moving_charge.png")

# === Ch.11 ===
def example_11_1_dipole_radiation():
    """Oscillating electric dipole radiation pattern."""
    p0, omega = 1e-9, 2*np.pi*1e8  # 100 MHz
    theta = np.linspace(0.01, np.pi-0.01, 200)
    # dP/dOmega = (mu0*p0^2*omega^4)/(32*pi^2*c) * sin^2(theta)
    P_const = mu0 * p0**2 * omega**4 / (32 * np.pi**2 * c)
    dP_dOmega = P_const * np.sin(theta)**2
    total_P = dP_dOmega[0] * 2*np.pi * np.trapezoid(np.sin(theta), theta) / np.sin(theta[0])
    # Actually: P = (mu0*p0^2*omega^4)/(12*pi*c)
    P_analytic = mu0 * p0**2 * omega**4 / (12 * np.pi * c)
    print(f"\n[Ch.11] Dipole radiation: f={omega/(2*np.pi)/1e6:.0f} MHz")
    print(f"  Total power P = {P_analytic:.6e} W")
    fig, ax = plt.subplots(figsize=(8, 5), subplot_kw={'projection': 'polar'})
    ax.plot(theta, np.abs(dP_dOmega)/dP_dOmega.max(), 'b-', linewidth=2)
    ax.plot(2*np.pi-theta, np.abs(dP_dOmega)/dP_dOmega.max(), 'b-', linewidth=2)
    ax.set_title('Dipole radiation angular distribution (sin^2 theta)')
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch11_ex1_dipole.png', dpi=150)
    plt.close(fig)
    print("Figure saved: griffiths_ch11_ex1_dipole.png")

def example_11_2_cyclotron_radiation():
    """Larmor formula for charge in circular motion."""
    q, m, R = 1.6e-19, 9.11e-31, 0.01  # electron in B field
    B = 0.1
    v = q*B*R/m  # cyclotron motion
    a = v**2/R
    P = mu0 * q**2 * a**2 / (6 * np.pi * c)
    f_cyc = q*B/(2*np.pi*m)
    print(f"\n[Ch.11] Cyclotron: B={B}T, f_cyc={f_cyc/1e9:.2f} GHz")
    print(f"  v = {v:.2e} m/s, a = {a:.2e} m/s^2")
    print(f"  Radiated power P = {P:.2e} W")

# === Ch.12 ===
def example_12_7_field_transformation():
    """Transformation of E and B fields between inertial frames.
    In lab frame: B = B0 z_hat only.
    In moving frame: E_z' = gamma*v*B_z."""
    B0 = 1.0  # Tesla
    v = 0.6*c
    gamma = 1/np.sqrt(1-(v/c)**2)
    print(f"\n[Ch.12] Field transformation:")
    print(f"  Lab frame: B = ({B0:.1f}, 0, 0) T")
    print(f"  Frame moving at v = {v/c:.1f}c along x:")
    print(f"    E'_y = gamma*v*B_z = {gamma*v*B0:.2e} V/m")
    print(f"    B'_z = gamma*B_z = {gamma*B0:.2f} T")
    # Invariants
    E, B = 1e5, 0.5
    E2_c2B2 = E**2 - c**2*B**2
    EdotB = E*B
    print(f"  Invariants for typical EM field:")
    print(f"    E^2 - c^2 B^2 = {E2_c2B2:.2e}")
    print(f"    E·B = {EdotB:.2e}")

def lorentz_contraction_example():
    """Length contraction and time dilation."""
    v_vals = np.linspace(0, 0.99*c, 100)
    gamma_vals = 1/np.sqrt(1 - (v_vals/c)**2)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(v_vals/c, gamma_vals, 'b-', linewidth=2)
    ax.set_xlabel('v/c'); ax.set_ylabel('gamma')
    ax.set_title('Lorentz factor vs velocity')
    ax.grid(True, alpha=0.3)
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch12_lorentz.png', dpi=150)
    plt.close(fig)
    print("\nFigure saved: griffiths_ch12_lorentz.png")

if __name__ == "__main__":
    example_10_1_moving_charge()
    example_11_1_dipole_radiation()
    example_11_2_cyclotron_radiation()
    example_12_7_field_transformation()
    lorentz_contraction_example()
    print("\n✅ Ch.10-12 examples done")
