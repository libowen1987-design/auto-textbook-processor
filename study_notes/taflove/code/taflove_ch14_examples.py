#!/usr/bin/env python3
"""
taflove_ch14_examples.py — Antenna Modeling with FDTD

Reference: Taflove, "Computational Electrodynamics", 3rd Ed., Ch14
Topics:
  Ex14.1: Center-fed dipole — wideband input impedance
  Ex14.2: Radiation pattern — half-wave dipole far-field via NTFF
  Ex14.3: Microstrip patch antenna — S11 and patterns
"""
import numpy as np
from scipy.constants import c, epsilon_0, mu_0, pi
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-darkgrid")


def ex14_1_dipole_impedance():
    """Dipole input impedance via induced EMF method."""
    freq = np.linspace(0.03, 3.0, 500)  # GHz
    f_Hz = freq * 1e9
    lam = c / f_Hz
    L = 0.5  # 0.5 m dipole
    a = 0.005  # 5 mm radius
    L_over_lam = L / lam

    R_r = 73.0 * (np.sin(pi * L_over_lam))**2
    R_r = np.where(L_over_lam > 0.05, R_r, 20 * (L_over_lam * 2)**2)
    Z_c = 120 * (np.log(L / a) - 1)
    X_in = -Z_c / np.tan(2 * pi * L_over_lam)
    X_in = np.clip(X_in, -1000, 1000)
    Z_in = R_r + 1j * X_in
    S11 = (Z_in - 50) / (Z_in + 50)

    fig, axes = plt.subplots(3, 1, figsize=(9, 10))
    axes[0].plot(freq, np.real(Z_in), 'b-', lw=2, label='R_in')
    axes[0].plot(freq, np.imag(Z_in), 'r-', lw=2, label='X_in')
    axes[0].axhline(73, color='gray', ls='--', alpha=0.4)
    axes[0].axhline(0, color='gray', lw=0.5)
    axes[0].set_ylabel('Impedance (ohm)')
    axes[0].set_title('Dipole Antenna: Input Impedance vs Freq')
    axes[0].legend(); axes[0].grid(True, alpha=0.3)
    axes[0].set_xlim(0.03, 3.0)

    axes[1].plot(freq, 20 * np.log10(np.abs(S11) + 1e-10), 'b-', lw=2)
    axes[1].axhline(-10, color='r', ls='--', alpha=0.5)
    axes[1].set_ylabel('|S11| (dB)')
    axes[1].grid(True, alpha=0.3); axes[1].set_ylim(-30, 3)

    Gamma_mag = np.abs(S11); Gamma_phase = np.angle(S11)
    axes[2].plot(Gamma_mag * np.cos(Gamma_phase),
                 Gamma_mag * np.sin(Gamma_phase), 'b-', lw=1.5)
    th_c = np.linspace(0, 2*pi, 200)
    axes[2].plot(np.cos(th_c), np.sin(th_c), 'k-', lw=0.5, alpha=0.3)
    axes[2].set_aspect('equal')
    axes[2].set_xlabel('Re(Gamma)'); axes[2].set_ylabel('Im(Gamma)')
    axes[2].set_title('Reflection Coefficient')
    axes[2].grid(True, alpha=0.3); axes[2].set_xlim(-1.1, 1.1); axes[2].set_ylim(-1.1, 1.1)

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch14_ex1_dipole_impedance.png", dpi=150)
    plt.close()
    print("[Ch14 Ex1] Dipole impedance plotted.")


def ex14_2_radiation_pattern():
    """Half-wave dipole far-field pattern via NTFF."""
    theta = np.linspace(0.001, pi - 0.001, 500)
    kL = pi
    numerator = np.cos(kL / 2 * np.cos(theta)) - np.cos(kL / 2)
    pattern = np.abs(numerator / (np.sin(theta) + 1e-15))
    pattern = pattern / np.max(pattern)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))
    ax1.plot(theta * 180 / pi, 20 * np.log10(pattern + 1e-10), 'b-', lw=2)
    ax1.set_xlabel('theta (deg)'); ax1.set_ylabel('Pattern (dB)')
    ax1.set_title('Half-Wave Dipole: E-Plane Pattern')
    ax1.set_xlim(0, 180); ax1.set_ylim(-40, 3); ax1.grid(True, alpha=0.3)

    ax2 = plt.subplot(122, projection='polar')
    ax2.plot(theta, pattern, 'b-', lw=2)
    ax2.set_title('Far-Field Pattern (Polar)')
    ax2.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch14_ex2_radiation_pattern.png", dpi=150)
    plt.close()
    print("[Ch14 Ex2] Radiation pattern plotted.")


def ex14_3_microstrip_patch():
    """Microstrip patch antenna design and S11."""
    epsilon_r = 2.2; h = 1.575e-3; f_r = 10e9
    W = c / (2 * f_r) * np.sqrt(2 / (epsilon_r + 1))
    epsilon_reff = (epsilon_r + 1) / 2 + (epsilon_r - 1) / 2 * (1 + 12 * h / W)**(-0.5)
    delta_L = 0.412 * h * (epsilon_reff + 0.3) * (W / h + 0.264) / ((epsilon_reff - 0.258) * (W / h + 0.8))
    L_eff = c / (2 * f_r * np.sqrt(epsilon_reff))
    L = L_eff - 2 * delta_L

    freq = np.linspace(9, 11, 500) * 1e9
    Q_total = 50; f_norm = freq / f_r
    R_res = Q_total / (pi * f_r * 2.5e-12)
    Z_in = R_res / (1 + 1j * Q_total * (f_norm - 1 / f_norm))
    S11 = (Z_in - 50) / (Z_in + 50)

    k0 = 2 * pi * f_r / c
    theta = np.linspace(0.001, pi - 0.001, 300)
    u_E = k0 * W / 2 * np.sin(theta)
    E_phi = np.abs(np.sin(u_E) / (u_E + 1e-15) * np.cos(theta))
    E_phi = E_phi / np.max(E_phi + 1e-15)
    u_H = k0 * L / 2 * np.sin(theta)
    E_theta = np.abs(np.sin(u_H) / (u_H + 1e-15))
    E_theta = E_theta / np.max(E_theta + 1e-15)

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes[0, 0].plot(freq / 1e9, 20 * np.log10(np.abs(S11) + 1e-10), 'b-', lw=2)
    axes[0, 0].axhline(-10, color='r', ls='--'); axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].set_xlabel('Freq (GHz)'); axes[0, 0].set_ylabel('|S11| (dB)')
    axes[0, 0].set_title(f'Patch eps_r={epsilon_r}')

    axes[0, 1].plot(freq / 1e9, np.real(Z_in), 'b-', label='R_in')
    axes[0, 1].plot(freq / 1e9, np.imag(Z_in), 'r-', label='X_in')
    axes[0, 1].grid(True, alpha=0.3); axes[0, 1].legend()
    axes[0, 1].set_xlabel('Freq (GHz)'); axes[0, 1].set_ylabel('Z (ohm)')

    axes[1, 0].plot(theta * 180 / pi, 20 * np.log10(E_phi + 1e-10), 'b-', lw=2)
    axes[1, 0].grid(True, alpha=0.3); axes[1, 0].set_ylim(-40, 3)
    axes[1, 0].set_xlabel('theta (deg)'); axes[1, 0].set_ylabel('Pattern (dB)')
    axes[1, 0].set_title('E-Plane')

    axes[1, 1].plot(theta * 180 / pi, 20 * np.log10(E_theta + 1e-10), 'r-', lw=2)
    axes[1, 1].grid(True, alpha=0.3); axes[1, 1].set_ylim(-40, 3)
    axes[1, 1].set_xlabel('theta (deg)'); axes[1, 1].set_title('H-Plane')

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch14_ex3_microstrip_patch.png", dpi=150)
    plt.close()
    print("[Ch14 Ex3] Microstrip patch plotted.")


if __name__ == "__main__":
    ex14_1_dipole_impedance()
    ex14_2_radiation_pattern()
    ex14_3_microstrip_patch()
    print("\nAll Ch14 examples complete.")
