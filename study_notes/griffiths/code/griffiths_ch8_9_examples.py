#!/usr/bin/env python3
"""Griffiths Ch.8: Conservation Laws & Ch.9: EM Waves"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

plt.style.use('seaborn-v0_8')
mu0, eps0 = constants.mu_0, constants.epsilon_0
c = constants.c

# === Ch.8 ===
def example_8_1_coaxial_cable():
    """Poynting vector in coaxial cable: S = (V*I)/(2*pi*r^2) * z_hat * 1/ln(b/a)"""
    V, I = 12.0, 2.0
    a, b = 0.001, 0.005
    r_vals = np.linspace(a, b, 100)
    # E radial: lambda/(2*pi*eps0*r), B phi: mu0*I/(2*pi*r)
    # S = (1/mu0) * E x B = (VI)/(2*pi^2*r^2*ln(b/a)) * z_hat... actually:
    lam = 2*np.pi*eps0*V/np.log(b/a)  # charge per length
    E_r = lam/(2*np.pi*eps0*r_vals)
    B_phi = mu0*I/(2*np.pi*r_vals)
    S_z = (1/mu0) * E_r * B_phi
    power_total = np.trapezoid(S_z * 2*np.pi*r_vals, r_vals)
    print(f"[Ch.8] Coaxial cable: V={V}V, I={I}A, P=S·da={power_total:.2f}W (expect VI={V*I:.2f}W)")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(r_vals*1e3, S_z/1e6, 'b-', linewidth=2)
    ax.set_xlabel('r (mm)'); ax.set_ylabel('S_z (MW/m^2)')
    ax.set_title('Poynting vector in coaxial cable')
    ax.grid(True, alpha=0.3)
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch8_ex1_coax.png', dpi=150)
    plt.close(fig)
    print("Figure saved: griffiths_ch8_ex1_coax.png")

# === Ch.9 ===
def example_9_1_em_plane_wave():
    """EM plane wave in vacuum: E0 = c*B0, S = (1/2)*c*eps0*E0^2"""
    f = 1e9  # 1 GHz
    omega = 2*np.pi*f
    k = omega/c
    lam = 2*np.pi/k
    E0 = 100.0  # V/m
    B0 = E0/c
    I_avg = 0.5 * c * eps0 * E0**2
    print(f"\n[Ch.9] EM plane wave: f={f/1e9:.1f} GHz, lambda={lam:.3f}m")
    print(f"  E0 = {E0:.1f} V/m, B0 = {B0*1e6:.2f} microT")
    print(f"  c*B0 = {c*B0:.1f} V/m = E0 ✓")
    print(f"  I_avg = {I_avg:.2f} W/m^2")
    # Wave visualization
    z = np.linspace(0, 3*lam, 500)
    t = 0
    E = E0 * np.cos(k*z - omega*t)
    B = B0 * np.cos(k*z - omega*t)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(z/lam, E, 'b-', linewidth=2, label='E (V/m)')
    ax.plot(z/lam, B*1e7, 'r-', linewidth=2, label='B × 10^7 (T × 10^7)')
    ax.set_xlabel('z / lambda'); ax.set_ylabel('Field amplitude')
    ax.set_title('EM plane wave at t=0 (E and B in phase, perpendicular)')
    ax.legend(); ax.grid(True, alpha=0.3)
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch9_ex1_em_wave.png', dpi=150)
    plt.close(fig)
    print("Figure saved: griffiths_ch9_ex1_em_wave.png")

def example_9_4_reflection_normal():
    """Reflection and transmission at normal incidence."""
    n1, n2 = 1.0, 1.5  # air to glass
    R = ((n1-n2)/(n1+n2))**2
    T = 4*n1*n2/(n1+n2)**2
    print(f"Normal incidence air->glass: R={R:.3f} ({R*100:.1f}%), T={T:.3f} ({T*100:.1f}%)")
    print(f"R+T = {R+T:.10f} ✓")
    # Vary n2
    n2_vals = np.linspace(1.0, 4.0, 100)
    R_vals = ((1 - n2_vals)/(1 + n2_vals))**2
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(n2_vals, R_vals*100, 'b-', linewidth=2)
    ax.set_xlabel('n2 (n1=1, air)'); ax.set_ylabel('Reflectance R (%)')
    ax.set_title('Reflectance vs refractive index (normal incidence)')
    ax.grid(True, alpha=0.3)
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch9_ex4_reflection.png', dpi=150)
    plt.close(fig)
    print("Figure saved: griffiths_ch9_ex4_reflection.png")

if __name__ == "__main__":
    example_8_1_coaxial_cable()
    example_9_1_em_plane_wave()
    example_9_4_reflection_normal()
    print("\n✅ Ch.8-9 examples done")
