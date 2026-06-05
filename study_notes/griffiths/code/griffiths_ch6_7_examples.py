#!/usr/bin/env python3
"""Griffiths Ch.6: Magnetic Fields in Matter & Ch.7: Electrodynamics"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

plt.style.use('seaborn-v0_8')
mu0, eps0 = constants.mu_0, constants.epsilon_0

# === Ch.6 ===
def example_6_2_magnetized_sphere():
    """Uniformly magnetized sphere: Bin = (2/3)*mu0*M, Bout = dipole field."""
    M = 1e5  # A/m
    R = 0.1
    Bin = 2.0/3.0 * mu0 * M
    r_vals = np.linspace(0.01, 3*R, 300)
    theta = np.pi/2  # equatorial plane
    B_inside = Bin * np.ones_like(r_vals[r_vals < R])
    r_out = r_vals[r_vals >= R]
    B_outside = mu0 * M * R**3 / (3 * r_out**3)  # dipole field on equator
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(r_vals[r_vals<R]*1e2, Bin*np.ones_like(r_vals[r_vals<R])*1e4, 'b-', linewidth=2, label='Inside')
    ax.plot(r_out*1e2, B_outside*1e4, 'r-', linewidth=2, label='Outside (dipole)')
    ax.axvline(R*1e2, color='gray', linestyle='--', label='Surface')
    ax.set_xlabel('r (cm)'); ax.set_ylabel('B (Gauss)')
    ax.set_title(f'B field of uniformly magnetized sphere (M = {M*1e-3:.0f} kA/m)')
    ax.legend(); ax.grid(True, alpha=0.3)
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch6_ex2_magnetized_sphere.png', dpi=150)
    plt.close(fig)
    print(f"Bin = {Bin*1e4:.2f} Gauss = (2/3)*mu0*M")
    print("Figure saved: griffiths_ch6_ex2_magnetized_sphere.png")

def example_6_3_core_solenoid():
    """Solenoid with magnetic core: B = mu*n*I"""
    for mu_r in [1, 100, 1000]:
        n, I = 1000, 5.0
        B = mu_r * mu0 * n * I
        print(f"mu_r = {mu_r}: B = {B*1e4:.2f} Gauss")

# === Ch.7 ===
def example_7_4_motional_emf():
    """Sliding rod on U-shaped rail in uniform B field."""
    B, v, L = 0.5, 2.0, 0.3  # B=0.5T, v=2m/s, L=0.3m
    emf = B * v * L
    I = emf / 1.0  # assume R=1ohm
    print(f"\n[Ch.7] Motional EMF: epsilon = Blv = {emf:.3f} V, I = {I:.3f} A")
    # Power
    F = B * I * L
    P_mech = F * v
    P_elec = emf * I
    print(f"F = {F:.4f} N, P_mech = {P_mech:.4f} W, P_elec = {P_elec:.4f} W")

def example_7_7_charging_capacitor():
    """B field between plates of charging capacitor."""
    I, R, a = 1.0, 0.05, 0.03  # I=1A, plate radius=5cm, separation=3cm
    s = np.linspace(0.001, R, 200)
    B_inside = mu0 * I * s / (2 * np.pi * R**2)
    B_outside = mu0 * I / (2 * np.pi * s)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(s*1e2, B_inside*1e5, 'b-', linewidth=2, label='Inside plates')
    ax.plot(np.linspace(R, 2*R, 100)*1e2, B_outside[::2]*1e5, 'r--', linewidth=2, label='Outside plates')
    ax.axvline(R*1e2, color='gray', linestyle='--', label='Plate edge')
    ax.set_xlabel('s (cm)'); ax.set_ylabel('B (Gauss)')
    ax.set_title('B field between charging capacitor plates (displacement current)')
    ax.legend(); ax.grid(True, alpha=0.3)
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch7_ex7_capacitor_B.png', dpi=150)
    plt.close(fig)
    print(f"Max B inside plate: {B_inside.max()*1e5:.2f} Gauss at s=R")
    print("Figure saved: griffiths_ch7_ex7_capacitor_B.png")

if __name__ == "__main__":
    example_6_2_magnetized_sphere()
    example_6_3_core_solenoid()
    example_7_4_motional_emf()
    example_7_7_charging_capacitor()
    print("\n✅ Ch.6-7 examples done")
