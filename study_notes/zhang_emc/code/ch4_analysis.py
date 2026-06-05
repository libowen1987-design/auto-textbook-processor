#!/usr/bin/env python3
"""
Zhang EMC - Chapter 4: EMC Prediction Analysis Methods
======================================================
Core topics:
- S-parameter coupling analysis between elements
- Statistical electromagnetics (Monte Carlo, parametric)
- MIL-STD-461 CE/CS/RE/RS limits
- Spectrum compatibility analysis

Ref: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Ch4
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0, pi
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────
# 1. S-Parameter Coupling Analysis
# ─────────────────────────────────────────────

def s_parameters_to_z(s):
    """
    Convert S-parameters to Z-parameters (input impedance).
    Z = Z0 * (1 + S) / (1 - S)  for single-port.
    For 2-port: Z11 = Z0*(1-S11)*(1+S22)-S12*S21 / ...
    Here we implement the general 2-port conversion.
    """
    z0 = 50.0  # reference impedance
    s11, s12, s21, s22 = s[0,0], s[0,1], s[1,0], s[1,1]
    denom = (1 - s11) * (1 - s22) - s12 * s21
    z11 = z0 * ((1 + s11) * (1 - s22) + s12 * s21) / denom
    z12 = z0 * (2 * s12) / denom
    z21 = z0 * (2 * s21) / denom
    z22 = z0 * ((1 - s11) * (1 + s22) + s12 * s21) / denom
    return np.array([[z11, z12], [z21, z22]])


def coupling_coefficient_from_s(S21_dB, Z0=50.0):
    """
    Coupling coefficient C = |S21|^2 * P_ref / P_in.
    S21_dB: S21 in dB
    Returns: coupling coefficient (linear)
    """
    S21_linear = 10**(S21_dB / 20.0)
    C = S21_linear**2
    return C


def check_emc_coupling(S21_dB, immunity_threshold_dBm, emission_level_dBm):
    """
    Verify EMC margin given two-port coupling and levels.
    If emission_level + coupling > immunity_threshold → EMI risk.
    """
    S21_linear = 10**(S21_dB / 20.0)
    received_power_dBm = emission_level_dBm + 10 * np.log10(S21_linear**2)
    margin = immunity_threshold_dBm - received_power_dBm
    return {
        'received_power_dBm': received_power_dBm,
        'immunity_threshold_dBm': immunity_threshold_dBm,
        'margin_dB': margin,
        'pass': margin > 6.0  # 6 dB safety margin per MIL-STD-461
    }


def crosstalk_between_traces(d_trailing, d_receiving, l_coupling,
                              V_source=3.3, Z0=50.0, f=100e6):
    """
    Simplified crosstalk model for parallel microstrip traces.
    d_trailing:  spacing from aggressor to reference (m)
    d_receiving: spacing from victim to reference (m)
    l_coupling:  coupling length (m)
    V_source:    signal voltage (V)
    f:            frequency (Hz)
    Z0:           characteristic impedance (ohm)

    Near-end crosstalk (NEXT) approximation:
    Xtalk_NEXT ≈ (V_src / (4*π)) * (d_receiving / d_trailing) * (l_coupling / λ)
    """
    wavelength = c / f
    k0 = 2 * pi / wavelength
    # Mutual capacitance and inductance simplified model
    # C_m ≈ ε0 * w * h / d  (parallel plate approximation)
    h = 0.2e-3  # substrate height ~0.2mm
    w = 0.3e-3  # trace width ~0.3mm
    d = d_trailing
    C_m = epsilon_0 * w * h / d  # F/m
    L_m = mu_0 * h * d / w       # H/m  (rough)
    Z_aggressor = Z0
    V_aggressor = V_source
    # Coupling coefficient
    gamma = (C_m * Z_aggressor * l_coupling) / wavelength
    V_crosstalk = V_aggressor * gamma * np.sin(k0 * l_coupling)
    return abs(V_crosstalk)


# ─────────────────────────────────────────────
# 2. MIL-STD-461 CE/CS/RE/RS Limit Envelopes
# ─────────────────────────────────────────────

def mil_std_461_ce102_limit(f_min=10e3, f_max=10e6):
    """
    MIL-STD-461 CS102/CE102 conducted emission limits for power leads.
    Returns (frequencies, limit_dBuV) in quasi-peak.
    Limit: 60 dBμV quasi-peak from 10 kHz to 1 MHz, decreasing to 50 dBμV at 10 MHz.
    """
    f = np.logspace(np.log10(f_min), np.log10(f_max), 500)
    limit = np.where(f < 1e6,
                     60.0 * np.ones_like(f),
                     60.0 - 20.0 * np.log10(f / 1e6))
    limit = np.clip(limit, 50.0, 100.0)
    return f, limit


def mil_std_461_re102_limit(f_min=10e3, f_max=18e9):
    """
    MIL-STD-461 RE102 electric field radiated emission limits.
    Limits depend on application (Army/Navy/Air Force).
    Army: 54 dBμV/m at 10 MHz declining to 20 dBμV/m at 10 GHz.
    """
    f = np.logspace(np.log10(f_min), np.log10(f_max), 600)
    # Army envelope
    limit = np.where(f < 1e5,
                     54.0 * np.ones_like(f),
                     np.where(f < 1e6,
                             54.0 - 10.0 * np.log10(f / 1e5),
                             np.where(f < 1e7,
                                     54.0 - 20.0 * np.log10(f / 1e5),
                                     np.where(f < 1e8,
                                              54.0 - 30.0 * np.log10(f / 1e5),
                                              np.where(f < 1e9,
                                                      54.0 - 40.0 * np.log10(f / 1e5),
                                                      20.0 - 10.0 * np.log10(f / 1e9))))))
    limit = np.clip(limit, 10.0, 80.0)
    return f, limit


def mil_std_461_cs114_limit(f_min=10e3, f_max=200e6):
    """
    MIL-STD-461 CS114 bulk cable injection conducted susceptibility.
    Limit: 77 dBμA from 10 kHz to 30 MHz, flat, then declining.
    """
    f = np.logspace(np.log10(f_min), np.log10(f_max), 400)
    limit = np.where(f < 30e6,
                     77.0 * np.ones_like(f),
                     77.0 - 15.0 * np.log10(f / 30e6))
    limit = np.clip(limit, 60.0, 90.0)
    return f, limit


# ─────────────────────────────────────────────
# 3. Spectrum Compatibility Analysis
# ─────────────────────────────────────────────

def emission_spectrum_envelope(f_clock, n_harmonic=50, V_0=3.3, t_r=2e-9):
    """
    Periodic digital signal spectrum envelope (Zhang Eq. related to clock).
    Approximate envelope of harmonics for a digital waveform:
    For a periodic clock with period T=1/f_clock:
    Broadband noise floor ≈ V_0 * t_r / T
    Discrete harmonics at n*f_clock with envelope ~ V_0 / (n*π) * |sin(π n t_r/T)|
    """
    n = np.arange(1, n_harmonic + 1)
    f_harm = n * f_clock
    # Envelope: sinc-type rolloff from risetime
    envelope = V_0 * np.abs(np.sin(pi * n * f_clock * t_r)) / (pi * n)
    return f_harm, envelope


def spectrum_compatibility_check(emission_freq_MHz, emission_dBuV_m,
                                 receiver_bw_kHz, antenna_gain_dBi,
                                 separation_m, frequency_MHz):
    """
    Check compatibility between a radiated emission and a receiver.
    Simplified free-space path loss model.
    emission_freq_MHz: emission center frequency (MHz)
    emission_dBuV/m: field strength at 1m
    receiver_bw_kHz: receiver bandwidth (kHz)
    antenna_gain_dBi: receive antenna gain (dBi)
    separation_m: separation distance (m)
    frequency_MHz: same as emission_freq
    """
    # Field to power density: S = |E|^2 / 377
    E_1m = 10**(emission_dBuV_m / 20e6) * 1e-6  # V/m (reference 1 μV/m = 0 dBμV/m)
    # Actually: dBμV/m to V/m: E(V/m) = 10^((dBuV/m - 120) / 20)
    E_1m = 10**((emission_dBuV_m - 120) / 20)
    # Free-space path loss
    lambda_m = 3e8 / (frequency_MHz * 1e6)
    L_fs = 20 * np.log10(4 * pi * separation_m / lambda_m)
    # Received field at separation
    E_sep = E_1m * 10**(-L_fs / 20)
    # Power density → available power
    S = E_sep**2 / 377.0
    # Effective aperture
    A_eff = (lambda_m**2) / (4 * pi) * 10**(antenna_gain_dBi / 10)
    P_received = S * A_eff
    # Normalize to receiver bandwidth
    P_dBm = 10 * np.log10(P_received * 1000)
    return {
        'E_sep_uV_m': E_sep * 1e6,
        'P_received_dBm': P_dBm,
        'path_loss_dB': L_fs
    }


# ─────────────────────────────────────────────
# 4. Numerical EM Methods - MoM/FE/BE/FIT concepts
# ─────────────────────────────────────────────

def method_of_moments_basic(wire_length, wire_radius, frequency,
                             incident_field_E=1.0):
    """
    Simplified Method of Moments (MoM) for straight wire antenna.
    Input:
        wire_length: wire length (m)
        wire_radius: wire radius (m)
        frequency:   operating frequency (Hz)
    Output:
        current_distribution: array of currents along wire (A)
        input_admittance: Y_in complex
    This is a simplified pulse-basis MoM using thin-wire kernel.
    """
    f = frequency
    k0 = 2 * pi * f / c
    N = 21  # number of basis functions (pulse basis)
    dz = wire_length / N
    z = np.linspace(-wire_length/2, wire_length/2, N)
    
    # Pulse basis functions, point matching at nodes
    # G(z,z') = (e^{-jk0R})/(4πR)  for thin wire
    G = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i == j:
                R = wire_radius
            else:
                R = np.sqrt((z[i] - z[j])**2 + wire_radius**2)
            G[i, j] = np.exp(-1j * k0 * R) / (4 * pi * R)
    
    # Incident field (assumed z-polarized uniform plane wave)
    V = incident_field_E * np.ones(N)
    # Solve G * I = V → I = G^{-1} * V
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        try:
            I = np.linalg.solve(G, V)
        except np.linalg.LinAlgError:
            I = np.zeros(N)
    
    Z_in = 1.0 / (np.mean(I) + 1e-10)
    return z, I, Z_in


def finite_difference_frequency_domain(eps_r, a_r, b_r, f,
                                        N_r=100, N_theta=180):
    """
    Simplified 2D FDFD for coaxial cable cross-section.
    Simulates TEM mode characteristic impedance.
    eps_r: relative permittivity of dielectric
    a_r:   inner radius (m)
    b_r:   outer radius (m)
    f:     frequency (Hz)
    """
    # Coaxial TEM mode characteristic impedance
    # Z0 = (60/√ε_r) * ln(b/a)
    Z0_TEM = (60.0 / np.sqrt(eps_r)) * np.log(b_r / a_r)
    # Cutoff for TE11 in coax: f_c ≈ c / (π*(a+b)*√ε_r)
    f_c = c / (pi * (a_r + b_r) * np.sqrt(eps_r))
    # Propagation constant
    beta = 2 * pi * f * np.sqrt(eps_r) / c
    return Z0_TEM, f_c, beta


# ─────────────────────────────────────────────
# 5. Statistical EM - Monte Carlo EMI Margin
# ─────────────────────────────────────────────

def monte_carlo_emi_margin(n_samples=5000,
                            emission_mean_dBm=-20.0,
                            emission_std_dB=3.0,
                            coupling_mean_dB=-40.0,
                            coupling_std_dB=2.0,
                            immunity_mean_dBm=-30.0,
                            immunity_std_dB=1.5):
    """
    Monte Carlo simulation of EMI margin accounting for statistical variation.
    Margin = immunity - (emission + coupling_loss)
    A pass requires margin > 6 dB with 90% confidence (worst-case 95th percentile).
    """
    np.random.seed(42)
    margin_failures = 0
    margins = []
    
    for _ in range(n_samples):
        emission_dBm = emission_mean_dBm + emission_std_dB * np.random.randn()
        coupling_dB = coupling_mean_dB + coupling_std_dB * np.random.randn()
        immunity_dBm = immunity_mean_dBm + immunity_std_dB * np.random.randn()
        received = emission_dBm - abs(coupling_dB)
        margin = immunity_dBm - received
        margins.append(margin)
        if margin < 6.0:
            margin_failures += 1
    
    margins = np.array(margins)
    fail_rate = margin_failures / n_samples * 100
    p5 = np.percentile(margins, 5)  # 5th percentile (worst case)
    p50 = np.percentile(margins, 50)
    
    return {
        'n_samples': n_samples,
        'fail_rate_pct': fail_rate,
        'margin_p5_dB': p5,
        'margin_p50_dB': p50,
        'pass': fail_rate < 10.0
    }


# ─────────────────────────────────────────────
# 6. Plotting utilities
# ─────────────────────────────────────────────

def plot_mil_std_461_limits():
    """Plot MIL-STD-461 CE102, RE102, CS114 envelopes."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    f_ce, lim_ce = mil_std_461_ce102_limit()
    axes[0].semilogx(f_ce / 1e3, lim_ce, 'b-', lw=2)
    axes[0].set_xlabel('Frequency (kHz)')
    axes[0].set_ylabel('Limit (dBμV)')
    axes[0].set_title('MIL-STD-461 CE102 Conducted Emission')
    axes[0].grid(True, which='both', alpha=0.3)
    axes[0].set_xlim([10, 1e4])
    axes[0].set_ylim([40, 70])
    
    f_re, lim_re = mil_std_461_re102_limit()
    axes[1].semilogx(f_re / 1e6, lim_re, 'r-', lw=2)
    axes[1].set_xlabel('Frequency (MHz)')
    axes[1].set_ylabel('Limit (dBμV/m)')
    axes[1].set_title('MIL-STD-461 RE102 Radiated Emission (Army)')
    axes[1].grid(True, which='both', alpha=0.3)
    axes[1].set_xlim([0.01, 18e3])
    axes[1].set_ylim([10, 70])
    
    f_cs, lim_cs = mil_std_461_cs114_limit()
    axes[2].semilogx(f_cs / 1e3, lim_cs, 'g-', lw=2)
    axes[2].set_xlabel('Frequency (kHz)')
    axes[2].set_ylabel('Limit (dBμA)')
    axes[2].set_title('MIL-STD-461 CS114 Conducted Susceptibility')
    axes[2].grid(True, which='both', alpha=0.3)
    axes[2].set_xlim([10, 200e3])
    axes[2].set_ylim([55, 90])
    
    plt.tight_layout()
    out = '/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures/ch4_mil_std_461_limits.png'
    plt.savefig(out, dpi=150, bbox_inches='tight')
    print(f"Figure saved: {out}")
    plt.close()


def plot_spectrum_compatibility():
    """Plot emission spectrum envelope vs receiver bands."""
    f_clock = 100e6  # 100 MHz clock
    
    n = np.arange(1, 51)
    f_harm = n * f_clock
    env = (3.3 / (pi * n)) * np.abs(np.sin(pi * n * f_clock * 2e-9))
    # Noise floor (wideband)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.semilogx(f_harm / 1e6, 20 * np.log10(env + 1e-12), 'bo-', ms=4, label='Clock harmonics')
    ax.axhline(y=-40, color='r', linestyle='--', label='CE102 limit approx')
    ax.set_xlabel('Frequency (MHz)')
    ax.set_ylabel('Emission Level (dBV)')
    ax.set_title('Digital Clock Emission Spectrum Envelope')
    ax.legend()
    ax.grid(True, which='both', alpha=0.3)
    plt.tight_layout()
    out = '/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures/ch4_clock_spectrum.png'
    plt.savefig(out, dpi=150, bbox_inches='tight')
    print(f"Figure saved: {out}")
    plt.close()


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == '__main__':
    import os
    os.makedirs('/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures', exist_ok=True)
    
    print("=== Chapter 4: EMC Prediction Analysis Methods ===\n")
    
    # 1. S-parameter coupling
    print("--- 1. S-Parameter Coupling ---")
    coupling = coupling_coefficient_from_s(-40.0)  # -40 dB coupling
    print(f"  Coupling coefficient (|S21|^2) for -40 dB: {coupling:.2e}")
    result = check_emc_coupling(S21_dB=-40, immunity_threshold_dBm=-30,
                                 emission_level_dBm=-20)
    print(f"  Received power: {result['received_power_dBm']:.1f} dBm")
    print(f"  Margin: {result['margin_dB']:.1f} dB → {'PASS' if result['pass'] else 'FAIL'}")
    
    # 2. MIL-STD-461
    print("\n--- 2. MIL-STD-461 CE102 Limit ---")
    f, lim = mil_std_461_ce102_limit()
    print(f"  CE102 limit at 100 kHz: {lim[0]:.1f} dBμV")
    print(f"  CE102 limit at 1 MHz:   {lim[len(f)//2]:.1f} dBμV")
    
    # 3. Crosstalk
    print("\n--- 3. Microstrip Crosstalk ---")
    V_x = crosstalk_between_traces(d_trailing=0.3e-3, d_receiving=0.3e-3,
                                    l_coupling=50e-3, f=100e6)
    print(f"  Near-end crosstalk voltage: {V_x*1000:.3f} mV (aggressor=3.3V @ 100MHz, l=50mm)")
    
    # 4. Monte Carlo EMI margin
    print("\n--- 4. Monte Carlo EMI Margin (n=5000) ---")
    mc = monte_carlo_emi_margin()
    print(f"  5th percentile margin: {mc['margin_p5_dB']:.2f} dB")
    print(f"  50th percentile margin: {mc['margin_p50_dB']:.2f} dB")
    print(f"  Fail rate (< 6 dB): {mc['fail_rate_pct']:.2f}% → {'PASS' if mc['pass'] else 'FAIL'}")
    
    # 5. Spectrum
    print("\n--- 5. Spectrum Compatibility ---")
    sc = spectrum_compatibility_check(emission_freq_MHz=1000,
                                      emission_dBuV_m=60,
                                      receiver_bw_kHz=100,
                                      antenna_gain_dBi=3,
                                      separation_m=3,
                                      frequency_MHz=1000)
    print(f"  E-field at 3m: {sc['E_sep_uV_m']:.3f} μV/m")
    print(f"  Path loss: {sc['path_loss_dB']:.1f} dB")
    print(f"  P_received: {sc['P_received_dBm']:.2f} dBm")
    
    # 6. Coaxial Z0
    print("\n--- 6. Coaxial Cable Z0 (FDFD concept) ---")
    Z0, f_c, beta = finite_difference_frequency_domain(eps_r=2.1, a_r=0.5e-3,
                                                          b_r=1.7e-3, f=1e9)
    print(f"  Z0 = {Z0:.2f} Ω  (RG-214 equivalent)")
    print(f"  TE11 cutoff f_c = {f_c/1e9:.3f} GHz")
    
    # 7. Plots
    print("\n--- 7. Generating Figures ---")
    plot_mil_std_461_limits()
    plot_spectrum_compatibility()
    
    print("\n✓ Chapter 4 code complete.")
