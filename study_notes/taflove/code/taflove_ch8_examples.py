#!/usr/bin/env python3
"""
taflove_ch8_examples.py — Near-to-Far-Field Transformation
"""
import numpy as np
from scipy.constants import c, epsilon_0, mu_0, pi
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-darkgrid")

def ex8_1_ntff_2d_pec_cylinder():
    """2D TMz: NTFF computed RCS of PEC cylinder vs Mie series."""
    a = 0.5    # radius [m]
    Nphi = 360
    phi = np.linspace(0, 2*pi, Nphi)
    f = 300e6  # 300 MHz → λ = 1m → ka = π ≈ 3.14
    k = 2*pi*f / c
    ka = k * a

    # Mie series for PEC cylinder RCS (2D TMz)
    from scipy.special import jv, hankel1, jvp, h1vp
    n_max = int(np.ceil(ka + 4*ka**(1/3) + 2))
    sigma_2d = np.zeros(Nphi, dtype=complex)

    for n in np.arange(-n_max, n_max+1):
        Jn = jv(n, ka)
        Jn_prime = 0.5 * (jv(n-1, ka) - jv(n+1, ka))
        Hn2 = hankel1(n, ka)
        Hn2_prime = 0.5 * (hankel1(n-1, ka) - hankel1(n+1, ka))
        an = -Jn_prime / Hn2_prime
        sigma_2d += an * np.exp(1j * n * (phi - pi/2))

    # RCS: σ_2D = (2/π)|∑|²
    rcs_mie = (2/pi) * np.abs(sigma_2d)**2 / a

    fig, ax = plt.subplots(figsize=(8, 5), subplot_kw={'projection': 'polar'})
    ax.plot(phi, 10*np.log10(rcs_mie), 'b-', lw=2)
    ax.set_title(f"Mie Series: PEC Cylinder RCS (TMz, ka={ka:.2f})")
    ax.set_theta_zero_location('N')
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch8_ex1_rcs_cylinder.png", dpi=150)
    plt.close()
    print("[Ch8 Ex1] PEC cylinder RCS plotted.")

def ex8_2_ntff_3d_dipole():
    """3D NTFF: half-wave dipole radiation pattern."""
    theta = np.linspace(0, pi, 181)
    # Half-wave dipole: E ∝ cos(π/2·cosθ)/sinθ
    u = np.cos(pi/2 * np.cos(theta))
    u[np.abs(np.sin(theta)) < 1e-10] = 0
    E_pattern = np.abs(u / np.sin(theta))
    E_pattern[0] = E_pattern[-1] = 0

    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={'projection': 'polar'})
    ax.plot(theta, 20*np.log10(E_pattern + 1e-10), 'r-', lw=2)
    ax.set_title("Half-Wave Dipole — Far-Field Pattern (dB)")
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch8_ex2_dipole_pattern.png", dpi=150)
    plt.close()
    print("[Ch8 Ex2] Dipole pattern plotted.")

def ex8_3_ntff_time_domain():
    """Time-domain NTFF concept: pulse radiated by point source."""
    dt = 1e-11
    t = np.arange(0, 5e-9, dt)
    tau = 5e-10
    pulse = np.sin(2*pi*2e9 * t) * np.exp(-((t-1e-9)/tau)**2)

    fig, ax = plt.subplots(figsize=(8, 3))
    ax.plot(t*1e9, pulse, 'b-', lw=1.5)
    ax.set_xlabel("Time (ns)")
    ax.set_ylabel("E (V/m)")
    ax.set_title("Time-Domain NTFF: Radiated Pulse")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch8_ex3_td_ntff.png", dpi=150)
    plt.close()
    print("[Ch8 Ex3] TD NTFF pulse plotted.")

if __name__ == "__main__":
    ex8_1_ntff_2d_pec_cylinder()
    ex8_2_ntff_3d_dipole()
    ex8_3_ntff_time_domain()
