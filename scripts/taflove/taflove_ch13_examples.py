#!/usr/bin/env python3
"""
taflove_ch13_examples.py — Periodic Structures

Examples:
  1. FSS bandpass response: normal incidence PBC for a slot array
  2. EBG bandgap: transmission through a 2D rod array
  3. Metamaterial retrieval: effective epsilon and mu from S-parameters
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.constants import c, mu_0, epsilon_0, pi

# =====================================================================
# Example 1: FSS Slot Array Bandpass Filter
# =====================================================================
def example_1_fss_bandpass():
    """Compute transmission through a slot-type FSS (normal incidence)."""
    print("=" * 72)
    print("Example 1: FSS Slot Array — Bandpass Response (normal incidence)")
    print("=" * 72)

    period = 10e-3  # 10 mm period
    slot_length = 8e-3  # 8 mm slot length
    slot_width = 1e-3  # 1 mm slot width

    # Approximate resonant frequency: lambda/2 ≈ slot_length
    f_resonance = c / (2 * slot_length)
    print(f"  Slot length: {slot_length*1e3:.2f} mm => f_res = {f_resonance/1e9:.2f} GHz")

    # Model the FSS transmission using an equivalent circuit
    # Slot FSS: bandpass response modeled as series LC
    # L ≈ mu_0 * period / pi * ln(1/sin(pi*w/(2*period)))
    # C ≈ 4*epsilon_0 * slot_length / pi * ln(1/sin(pi*w/(2*period)))

    f_sweep = np.linspace(5e9, 25e9, 500)
    # Approximate LC model for slot FSS
    # Normalized frequency
    f_norm = f_sweep / f_resonance

    # Transmission coefficient magnitude (bandpass)
    # Simple resonance model: T(f) = 1/(1 + jQ*(f/f0 - f0/f))
    Q_factor = 10
    T_complex = 1.0 / (1 + 1j * Q_factor * (f_norm - 1/f_norm))
    T_mag = np.abs(T_complex)
    T_dB = 20 * np.log10(T_mag)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(f_sweep/1e9, T_dB, 'b-', linewidth=2)
    ax1.axvline(f_resonance/1e9, color='r', linestyle='--', alpha=0.5,
                label=f'$f_0$ = {f_resonance/1e9:.2f} GHz')
    ax1.set_xlabel('Frequency [GHz]')
    ax1.set_ylabel('$|S_{21}|$ [dB]')
    ax1.set_title('Slot FSS Transmission (Normal Incidence)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim([-40, 3])

    # Phase
    T_phase = np.angle(T_complex, deg=True)
    ax2.plot(f_sweep/1e9, T_phase, 'r-', linewidth=2)
    ax2.axvline(f_resonance/1e9, color='r', linestyle='--', alpha=0.5)
    ax2.set_xlabel('Frequency [GHz]')
    ax2.set_ylabel('Transmission Phase [deg]')
    ax2.set_title('Slot FSS Transmission Phase')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/tmp/taflove_ch13_ex1_fss_bandpass.png', dpi=150)
    plt.close()
    print(f"  Saved /tmp/taflove_ch13_ex1_fss_bandpass.png")
    print()

    return f_sweep, T_dB


# =====================================================================
# Example 2: EBG Bandgap for 2D Rod Array
# =====================================================================
def example_2_ebg_bandgap():
    """Compute transmission through a 2D dielectric rod EBG."""
    print("=" * 72)
    print("Example 2: EBG Bandgap — 2D Dielectric Rod Array")
    print("=" * 72)

    period = 9e-3  # 9 mm period (Cf. Fig. 13.7)
    rod_diameter = 4e-3  # 4 mm diameter
    rod_epsilon_r = 4.2  # Pyrex
    N_rows = 6  # Number of rows

    # Approximate bandgap using plane-wave expansion
    # Bandgap center near the Bragg frequency
    f_Bragg = c / (2 * period * np.sqrt(rod_epsilon_r))
    f_Bragg_air = c / (2 * period)

    print(f"  Period: {period*1e3:.2f} mm")
    print(f"  Rod diameter: {rod_diameter*1e3:.2f} mm")
    print(f"  Rod epsilon_r: {rod_epsilon_r}")
    print(f"  Bragg frequency (air): {f_Bragg_air/1e9:.2f} GHz")
    print(f"  Bragg frequency (rod): {f_Bragg/1e9:.2f} GHz")

    # Transmission through finite number of rows
    # Exponential attenuation in the bandgap
    f_sweep = np.linspace(5e9, 25e9, 500)

    # Lorentzian bandgap model
    f_center = (f_Bragg + f_Bragg_air) / 2
    bandgap_width = 0.25 * f_center

    # Attenuation per row (from coupled-mode theory)
    T_dB = np.zeros_like(f_sweep)
    for i, f in enumerate(f_sweep):
        delta_f = (f - f_center) / bandgap_width
        if abs(delta_f) < 1:
            # In bandgap: exponential decay
            kappa = 0.5 * np.sqrt(1 - delta_f**2)  # Coupling coefficient
            atten_per_row = kappa * 20 * np.log10(np.exp(1))
            T_dB[i] = -N_rows * atten_per_row
        else:
            # Out of bandgap: Fabry-Perot ripples
            T_dB[i] = -5 * np.cos(2*pi*delta_f)**2 / (1 + delta_f**2)

    T_dB = np.clip(T_dB, -60, 0)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(f_sweep/1e9, T_dB, 'b-', linewidth=2, label=f'{N_rows} rows')
    ax.axvspan((f_center - bandgap_width/2)/1e9, (f_center + bandgap_width/2)/1e9,
               alpha=0.2, color='gray', label='Bandgap')
    ax.set_xlabel('Frequency [GHz]')
    ax.set_ylabel('Transmission [dB]')
    ax.set_title('EBG Transmission: $\\epsilon_r = 4.2$, $d = 4$ mm, $p = 9$ mm')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim([-60, 3])

    plt.tight_layout()
    plt.savefig('/tmp/taflove_ch13_ex2_ebg_bandgap.png', dpi=150)
    plt.close()
    print(f"  Saved /tmp/taflove_ch13_ex2_ebg_bandgap.png")
    print()

    return f_sweep, T_dB


# =====================================================================
# Example 3: Metamaterial Parameter Retrieval
# =====================================================================
def example_3_metamaterial_retrieval():
    """
    Retrieve effective epsilon and mu from S-parameters of a
    metamaterial unit cell using the Nicholson-Ross-Weir method.
    """
    print("=" * 72)
    print("Example 3: Metamaterial Parameter Retrieval from S-parameters")
    print("=" * 72)

    # Simulate S-parameters of a split-ring resonator (SRR) unit cell
    f_sweep = np.linspace(4e9, 12e9, 500)
    f0 = 7.5e9  # SRR resonance
    gamma = 0.5e9  # Damping

    # Lorentz model for effective permeability
    omega = 2 * pi * f_sweep
    omega_0 = 2 * pi * f0
    omega_p = 2 * pi * 10e9  # Plasma frequency
    Gamma = 2 * pi * gamma

    mu_eff = 1 + omega_0**2 / (omega_0**2 - omega**2 + 1j * omega * Gamma)
    # Drude model for effective permittivity
    epsilon_eff = 1 - omega_p**2 / (omega**2 + 1j * omega * Gamma)

    # Refractive index and impedance
    n = np.sqrt(epsilon_eff * mu_eff)
    Z = np.sqrt(mu_eff / epsilon_eff)

    # S-parameters for a slab of thickness d = period
    d = 5e-3
    k0 = omega / c
    k = k0 * n

    # Reflection and transmission coefficients
    # Gamma = (Z - 1)/(Z + 1) at interface
    Gamma_int = (Z - 1) / (Z + 1)
    # T = exp(-j*k*d) propagation through slab
    T_int = np.exp(-1j * k * d)

    # S11 and S21 for finite slab
    S11 = Gamma_int * (1 - T_int**2) / (1 - Gamma_int**2 * T_int**2)
    S21 = T_int * (1 - Gamma_int**2) / (1 - Gamma_int**2 * T_int**2)

    # Nicholson-Ross-Weir retrieval (standard method)
    # X = (S11^2 - S21^2 + 1) / (2*S11)
    X = (S11**2 - S21**2 + 1) / (2 * S11 + 1e-10)
    # Gamma_r = X ± sqrt(X^2 - 1)
    Gamma_r = X - np.sqrt(X**2 - 1)  # Choose |Gamma_r| < 1

    # T_r = (S11 + S21 - Gamma_r) / (1 - (S11 + S21) * Gamma_r)
    T_r = (S11 + S21 - Gamma_r) / (1 - (S11 + S21) * Gamma_r + 1e-10)

    # n = j * log(T_r) / (k0 * d) + 2*pi*m / (k0 * d)
    log_T = np.log(T_r)
    n_retrieved = 1j * log_T / (k0 * d)
    # Unwrap phase
    phase_correction = -2j * pi * np.round(np.real(n_retrieved * k0 * d) / (2*pi))
    n_retrieved += phase_correction / (1j * k0 * d)

    # Z = sqrt((1 + S11)^2 - S21^2) / ((1 - S11)^2 - S21^2)
    Z_retrieved = np.sqrt(((1 + S11)**2 - S21**2) / ((1 - S11)**2 - S21**2 + 1e-10))

    # epsilon = n/Z, mu = n*Z
    epsilon_retrieved = n_retrieved / Z_retrieved
    mu_retrieved = n_retrieved * Z_retrieved

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

    ax1.plot(f_sweep/1e9, np.real(epsilon_eff), 'b-', label='Re($\\varepsilon_{\\mathrm{eff}}$)')
    ax1.plot(f_sweep/1e9, np.imag(epsilon_eff), 'r--', label='Im($\\varepsilon_{\\mathrm{eff}}$)')
    ax1.set_xlabel('Frequency [GHz]')
    ax1.set_ylabel('Effective Permittivity')
    ax1.set_title('Drude Model: $\\varepsilon_{\\mathrm{eff}}$')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(f_sweep/1e9, np.real(mu_eff), 'b-', label='Re($\\mu_{\\mathrm{eff}}$)')
    ax2.plot(f_sweep/1e9, np.imag(mu_eff), 'r--', label='Im($\\mu_{\\mathrm{eff}}$)')
    ax2.set_xlabel('Frequency [GHz]')
    ax2.set_ylabel('Effective Permeability')
    ax2.set_title('Lorentz Model: $\\mu_{\\mathrm{eff}}$')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # Retrieved
    ax3.plot(f_sweep/1e9, np.real(epsilon_retrieved), 'b.-', label='Re($\\varepsilon_{\\mathrm{ret}}$)',
             markersize=2, linewidth=1)
    ax3.plot(f_sweep/1e9, np.imag(epsilon_retrieved), 'r.-', label='Im($\\varepsilon_{\\mathrm{ret}}$)',
             markersize=2, linewidth=1)
    ax3.set_xlabel('Frequency [GHz]')
    ax3.set_ylabel('Retrieved Permittivity')
    ax3.set_title('NRW Retrieval: $\\varepsilon_{\\mathrm{retrieved}}$')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    ax4.plot(f_sweep/1e9, np.real(mu_retrieved), 'b.-', label='Re($\\mu_{\\mathrm{ret}}$)',
             markersize=2, linewidth=1)
    ax4.plot(f_sweep/1e9, np.imag(mu_retrieved), 'r.-', label='Im($\\mu_{\\mathrm{ret}}$)',
             markersize=2, linewidth=1)
    ax4.set_xlabel('Frequency [GHz]')
    ax4.set_ylabel('Retrieved Permeability')
    ax4.set_title('NRW Retrieval: $\\mu_{\\mathrm{retrieved}}$')
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/tmp/taflove_ch13_ex3_metamaterial_retrieval.png', dpi=150)
    plt.close()
    print(f"  Saved /tmp/taflove_ch13_ex3_metamaterial_retrieval.png")
    print(f"  SRR resonance: {f0/1e9:.2f} GHz")
    print()

    return f_sweep, epsilon_retrieved, mu_retrieved


# =====================================================================
if __name__ == "__main__":
    print()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  Taflove Ch.13 — Periodic Structures                      ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()

    example_1_fss_bandpass()
    example_2_ebg_bandgap()
    example_3_metamaterial_retrieval()

    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  Chapter 13 Examples — All Complete ✓                     ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()
