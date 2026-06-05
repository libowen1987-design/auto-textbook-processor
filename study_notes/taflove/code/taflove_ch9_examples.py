#!/usr/bin/env python3
"""
taflove_ch9_examples.py — Dispersive, Nonlinear, Gain Materials
"""
import numpy as np
from scipy.constants import c, epsilon_0, mu_0, pi
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-darkgrid")

def ex9_1_drude_metal():
    """Drude model: permittivity of silver from 400–800 nm."""
    freq = np.linspace(0.3e15, 1e15, 1000)  # Hz
    omega = 2 * pi * freq

    # Drude parameters for silver
    omega_p = 1.37e16  # plasma frequency [rad/s]
    gamma = 3.21e13    # collision frequency [rad/s]
    eps_inf = 1.0

    eps_r = eps_inf - omega_p**2 / (omega**2 + 1j * omega * gamma)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    wavelength_nm = c / freq * 1e9
    ax1.plot(wavelength_nm, np.real(eps_r), 'b-', lw=2)
    ax1.set_ylabel("Re(ε_r)")
    ax1.set_title("Drude Model: Silver Permittivity")
    ax1.grid(True, alpha=0.3)

    ax2.plot(wavelength_nm, -np.imag(eps_r), 'r-', lw=2)
    ax2.set_xlabel("Wavelength (nm)")
    ax2.set_ylabel("-Im(ε_r)")
    ax2.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch9_ex1_drude_metal.png", dpi=150)
    plt.close()
    print("[Ch9 Ex1] Drude metal plotted.")

def ex9_2_lorentz_dielectric():
    """Lorentz model: permittivity with resonance."""
    freq = np.linspace(0.1e14, 5e14, 1000)
    omega = 2 * pi * freq

    # Single Lorentz pole
    omega_0 = 2 * pi * 1e14
    delta = 0.1 * omega_0
    delta_eps = 2.0
    eps_inf = 1.5

    eps_r = eps_inf + delta_eps * omega_0**2 / (omega_0**2 - omega**2 + 2j * omega * delta)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 5), sharex=True)
    ax1.plot(freq/1e14, np.real(eps_r), 'b-', lw=2)
    ax1.axhline(eps_inf, color='gray', ls='--', alpha=0.5)
    ax1.set_ylabel("Re(ε_r)")
    ax1.set_title("Lorentz Model: Dispersive Dielectric")
    ax1.grid(True, alpha=0.3)

    ax2.plot(freq/1e14, np.imag(eps_r), 'r-', lw=2)
    ax2.set_xlabel("Frequency (×10¹⁴ Hz)")
    ax2.set_ylabel("Im(ε_r)")
    ax2.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch9_ex2_lorentz.png", dpi=150)
    plt.close()
    print("[Ch9 Ex2] Lorentz dielectric plotted.")

def ex9_3_debye_water():
    """Debye model: permittivity of water."""
    freq = np.logspace(7, 11, 500)
    omega = 2 * pi * freq

    # Single-pole Debye for water
    eps_s = 80.0
    eps_inf = 4.0
    tau = 8.2e-12  # relaxation time [s]

    eps_r = eps_inf + (eps_s - eps_inf) / (1 + 1j * omega * tau)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 5), sharex=True)
    ax1.loglog(freq, np.real(eps_r), 'b-', lw=2)
    ax1.set_ylabel("Re(ε_r)")
    ax1.set_title("Debye Model: Water Permittivity")
    ax1.grid(True, alpha=0.3, which='both')

    ax2.loglog(freq, np.imag(eps_r), 'r-', lw=2)
    ax2.set_xlabel("Frequency (Hz)")
    ax2.set_ylabel("Im(ε_r)")
    ax2.grid(True, alpha=0.3, which='both')
    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch9_ex3_debye.png", dpi=150)
    plt.close()
    print("[Ch9 Ex3] Debye water plotted.")

if __name__ == "__main__":
    ex9_1_drude_metal()
    ex9_2_lorentz_dielectric()
    ex9_3_debye_water()
