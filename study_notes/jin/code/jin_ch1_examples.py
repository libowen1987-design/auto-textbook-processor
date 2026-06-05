#!/usr/bin/env python3
"""
Jin Ch1 Example Codes: Basic Electromagnetic Theory
- Ex 1.6: Lorentz model of dielectric permittivity
- Ex 1.7: Power dissipation in a slotted metallic box
- Ex 1.8: Drude model of plasma permittivity
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Physical constants
epsilon_0 = 8.854187817e-12       # F/m
mu_0 = 4 * np.pi * 1e-7           # H/m
c_0 = 1 / np.sqrt(epsilon_0 * mu_0)  # m/s
eta_0 = np.sqrt(mu_0 / epsilon_0)    # ~377 Ohm
q_e = 1.602176634e-19             # C
m_e = 9.10938356e-31              # kg


# ============================================================
# Example 1.6: Lorentz Model of Dielectric Permittivity
# ============================================================
def lorentz_permittivity(f, N_e, delta, f0):
    """
    Lorentz model: epsilon_r(omega) = 1 + N_e q_e^2 / [epsilon_0 m_e (omega0^2 - omega^2 + j omega delta)]

    Parameters:
        f : frequency array (Hz)
        N_e : electron density (m^{-3})
        delta : damping coefficient (rad/s)
        f0 : resonance frequency (Hz)
    Returns:
        epsilon_r : complex relative permittivity array
    """
    omega = 2 * np.pi * f
    omega_0 = 2 * np.pi * f0
    eps_r = 1 + (N_e * q_e**2) / (epsilon_0 * m_e * (omega_0**2 - omega**2 + 1j * omega * delta))
    return eps_r


def plot_lorentz():
    """Plot Lorentz model permittivity for typical dielectric."""
    # Parameters for a typical dielectric (e.g., fused silica-like)
    N_e = 1e28            # m^{-3}
    delta = 1e14          # rad/s
    f0 = 3e15             # Hz (UV resonance)

    f = np.logspace(12, 16, 2000)  # 1 THz to 10 PHz
    eps_r = lorentz_permittivity(f, N_e, delta, f0)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

    ax1.semilogx(f / 1e12, eps_r.real, 'b-', linewidth=2)
    ax1.set_ylabel(r"$\epsilon'_r(\omega)$", fontsize=14)
    ax1.set_title("Lorentz Model: Complex Relative Permittivity", fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.axhline(1, color='gray', linestyle='--', linewidth=0.8)

    ax2.semilogx(f / 1e12, -eps_r.imag, 'r-', linewidth=2)
    ax2.set_xlabel("Frequency (THz)", fontsize=14)
    ax2.set_ylabel(r"$-\epsilon''_r(\omega)$", fontsize=14)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/python/jin_ex1_6_lorentz.png", dpi=150)
    plt.close()
    print("[Ex1.6] Lorentz model plot saved to jin_ex1_6_lorentz.png")

    # Print values at selected frequencies
    f_sel = np.array([1e12, 1e14, 1e15, 3e15, 1e16])
    eps_sel = lorentz_permittivity(f_sel, N_e, delta, f0)
    print("\n--- Lorentz model at selected frequencies ---")
    for fi, ei in zip(f_sel, eps_sel):
        print(f"  f = {fi:.2e} Hz:\t eps_r = {ei.real:.4f} {ei.imag:+.4f}j")


# ============================================================
# Example 1.7: Power Dissipation in a Slotted Metallic Box
# ============================================================
def example17_verify():
    """
    Verify the results from Example 1.7.
    Fields over the slot (z=0 plane, assuming box at z<0):
        E = y-hat * E0 * sin(pi*x/l)
        H = x-hat * (sqrt(3) + j) * E0 / (2*eta) * sin(pi*x/l)
    Compute: complex exiting power, time-average dissipated power, energy difference.
    """
    eta = 377.0        # Ohm
    E0 = 1.0           # V/m (normalized)
    w = 0.05           # m
    l = 0.1            # m
    freq = 1e9         # 1 GHz
    omega = 2 * np.pi * freq

    # Complex Poynting vector S = 1/2 * E x H*
    # E = y * E0 * sin(pi*x/l), H = x * (sqrt(3)+j) * E0 / (2*eta) * sin(pi*x/l)
    # E x H* = y x x * E0 * conj(H_amp) * sin^2(pi*x/l)
    # y x x = -z, so E x H* = -z * E0 * conj(H_amp) * sin^2(pi*x/l)
    H_amp = (np.sqrt(3) + 1j) * E0 / (2.0 * eta)

    # (E x H*) . z = -E0 * conj(H_amp) * sin^2(pi*x/l)
    S_z_amp = -0.5 * E0 * np.conj(H_amp)  # amplitude of 1/2 * (E x H*) . z including sin^2

    # Integrate over slot: integral of sin^2(pi*x/l) dx from 0 to l = l/2
    # integral over y from 0 to w = w
    Pe = S_z_amp * (l / 2.0) * w   # complex exiting power (book: -(sqrt3 - j) wlE0^2/(8eta))

    print(f"\n--- Example 1.7: Slotted Metallic Box (f = {freq/1e9:.1f} GHz) ---")
    print(f"  Slot dimensions: w = {w*100:.1f} cm, l = {l*100:.1f} cm")
    print(f"  H_amplitude = ({H_amp.real:.4f} {H_amp.imag:+.4f}j) A/m")
    print(f"  Complex exiting power Pe = {Pe.real:.6e} {Pe.imag:+.6e}j W")

    # Time-average power exiting (negative = entering the box, being dissipated)
    P_exit_real = np.real(Pe)
    Pd = -P_exit_real  # dissipated power = -Re(Pe) since Pe is power "leaving"

    # Energy difference: W_e - W_m = Im(Pe) / (2 * omega)
    We_minus_Wm = np.imag(Pe) / (2.0 * omega)

    print(f"  Time-avg power exiting box: Re(Pe) = {P_exit_real:.6e} W")
    print(f"  Time-avg power DISSIPATED:  Pd = -Re(Pe) = {Pd:.6e} W")
    print(f"  Energy difference W_e - W_m = {We_minus_Wm:.6e} J")
    print(f"  (Matches Pd = sqrt(3)*w*l*E0^2/(8*eta) = {np.sqrt(3)*w*l*E0**2/(8*eta):.6e} W)")


# ============================================================
# Example 1.8: Drude Model of Plasma Permittivity
# ============================================================
def drude_permittivity(f, N_e, nu):
    """
    Drude model: epsilon_eff = epsilon_0 + epsilon_0 * omega_p^2 / [j*omega*(nu + j*omega)]

    Parameters:
        f : frequency array (Hz)
        N_e : electron density (m^{-3})
        nu : collision frequency (Hz)
    Returns:
        eps_eff : effective permittivity (complex) relative to epsilon_0
    """
    omega = 2 * np.pi * f
    omega_p = np.sqrt(N_e * q_e**2 / (epsilon_0 * m_e))  # plasma frequency (rad/s)
    nu_rad = 2 * np.pi * nu
    # eps_rel = 1 + omega_p^2 / [j*omega*(nu + j*omega)]
    eps_rel = 1.0 + omega_p**2 / (1j * omega * (nu_rad + 1j * omega))
    return eps_rel


def plot_drude():
    """Plot Drude model permittivity for a typical plasma."""
    # Typical ionospheric plasma: N_e ~ 1e12 m^-3, nu ~ 1e3 Hz
    f = np.logspace(3, 9, 2000)  # 1 kHz to 1 GHz

    # Case 1: Low-density plasma (ionosphere)
    N_e1 = 1e12
    nu1 = 1e3
    eps1 = drude_permittivity(f, N_e1, nu1)
    fp1 = np.sqrt(N_e1 * q_e**2 / (epsilon_0 * m_e)) / (2 * np.pi)
    print(f"\n--- Example 1.8: Drude Model ---")
    print(f"  Case 1 (Ionosphere): N_e = {N_e1:.0e} m^-3, fp = {fp1/1e6:.2f} MHz")

    # Case 2: High-density plasma
    N_e2 = 1e18
    nu2 = 1e9
    eps2 = drude_permittivity(f, N_e2, nu2)
    fp2 = np.sqrt(N_e2 * q_e**2 / (epsilon_0 * m_e)) / (2 * np.pi)
    print(f"  Case 2 (Laboratory): N_e = {N_e2:.0e} m^-3, fp = {fp2/1e9:.2f} GHz")

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

    # Real part
    ax1.semilogx(f, eps1.real, 'b-', linewidth=2, label=f'Plasma 1 (f_p={fp1/1e6:.1f} MHz)')
    ax1.semilogx(f, eps2.real, 'r-', linewidth=2, label=f'Plasma 2 (f_p={fp2/1e9:.1f} GHz)')
    ax1.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    ax1.set_ylabel(r"$\epsilon'_r(\omega)$", fontsize=14)
    ax1.set_title("Drude Model: Effective Relative Permittivity", fontsize=14)
    ax1.legend(fontsize=12)
    ax1.grid(True, alpha=0.3)

    # Imaginary part
    ax2.semilogx(f, -eps1.imag, 'b-', linewidth=2, label=f'Plasma 1')
    ax2.semilogx(f, -eps2.imag, 'r-', linewidth=2, label=f'Plasma 2')
    ax2.set_xlabel("Frequency (Hz)", fontsize=14)
    ax2.set_ylabel(r"$-\epsilon''_r(\omega)$", fontsize=14)
    ax2.legend(fontsize=12)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/python/jin_ex1_8_drude.png", dpi=150)
    plt.close()
    print("[Ex1.8] Drude model plot saved to jin_ex1_8_drude.png")

    # Print specific values
    f_check = np.array([1e4, 1e6, fp1, fp2 * 10, 1e9])
    eps_check = drude_permittivity(f_check, N_e1, nu1)
    print("\n  Drude (low-density) at selected frequencies:")
    for fi, ei in zip(f_check, eps_check):
        print(f"    f = {fi:.2e} Hz:\t eps_r = {ei.real:.6f} {ei.imag:+.6f}j")


# ============================================================
# Additional: Poynting vector visualization (for Sec 1.6-1.7)
# ============================================================
def plot_poynting_visualization():
    """Simple plane wave plot showing E, H, S relationship."""
    z = np.linspace(0, 2, 100)  # wavelengths
    # Plane wave at t=0: E = x * cos(2*pi*z), H = y * cos(2*pi*z)
    E_x = np.cos(2 * np.pi * z)
    H_y = np.cos(2 * np.pi * z)
    # Poynting vector S_z = E_x * H_y = cos^2(2*pi*z)
    S_z = E_x * H_y

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(z, E_x, 'b-', linewidth=2, label=r'$E_x$')
    ax.plot(z, H_y, 'r--', linewidth=2, label=r'$H_y$')
    ax.plot(z, S_z, 'g-', linewidth=2, label=r'$S_z = E_x H_y$')
    ax.set_xlabel('z (wavelengths)', fontsize=14)
    ax.set_ylabel('Normalized amplitude', fontsize=14)
    ax.set_title('Plane Wave: Electric Field, Magnetic Field, and Poynting Vector', fontsize=14)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 2)
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/python/jin_ex_pozynting.png", dpi=150)
    plt.close()
    print("[Poynting] Visualization saved to jin_ex_pozynting.png")


# ============================================================
# Main execution
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Jin Ch1 — Example Codes")
    print("=" * 60)

    plot_lorentz()
    example17_verify()
    plot_drude()
    plot_poynting_visualization()

    print("\n" + "=" * 60)
    print("All examples completed successfully.")
    print("=" * 60)
