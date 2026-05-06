#!/usr/bin/env python3
"""
Zhang EMC - Chapter 8: EMC Design & Rectification for Typical Equipment
========================================================================
Core topics:
- Power supply & distribution equipment EMC design
- System Management Unit (SMU) design and rectification
- Integrated Services Unit (ISU) EMC design
- Solid State Power Amplifier (SSPA) design
- RF receiver EMC design

Ref: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Ch8
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0, pi
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────
# 1. Power Supply EMC Design
# ─────────────────────────────────────────────

def power_supply_emc_layout(V_bus_V=28.0, P_load_W=100.0,
                             f_sw_kHz=500, I_out_A=5.0):
    """
    Power supply EMC design layout principles.
    - Primary: EMI filter at input
    - Secondary: LC filter before output
    - Isolation: primary-secondary capacitance < 50 pF
    - Ground: single-point grounding at EMI filter ground
    """
    Z_bus = V_bus_V / I_out_A
    # Isolation requirement: C_iso < 50 pF for common-mode
    C_iso_max_pF = 50.0
    # Switching noise current (DM): I_sw ≈ P/V_bus / f_sw
    I_sw = P_load_W / V_bus_V
    V_sw_noise = I_sw * (1.0 / (f_sw_kHz * 1e3)) / (2 * pi * 1e-6)  # with 1 μF cap
    return {
        'Z_bus_ohm': Z_bus,
        'I_sw_A': I_sw,
        'V_sw_noise_mV': V_sw_noise * 1000,
        'C_iso_max_pF': C_iso_max_pF
    }


def emi_filter_attenuation_needed(emission_dBuV, limit_dBuV):
    """Determine required filter attenuation."""
    return emission_dBuV - limit_dBuV


def line_filter_design(V_in_V=28.0, I_in_A=5.0, f_sw_kHz=500,
                       target_attenuation_dB=40.0, Z_source_ohm=10.0):
    """
    EMI filter design for power supply input.
    Pi filter: C1 - L - C2
    L ≈ Z_source / (2π*f_sw)  for target attenuation
    C ≈ 1/(2π*f_sw*Z_source)
    """
    f_sw = f_sw_kHz * 1e3
    Z = Z_source_ohm
    
    # L from desired rolloff: f_c = 1/(2π√(L*C))
    # For f_c ≈ f_sw/10: L ≈ Z / (2π*f_c)
    f_c = f_sw / 10.0
    C_val = 1.0 / (2 * pi * f_c * Z)
    L_val = Z / (2 * pi * f_c)
    
    # Stage 1: C at input
    C1_uF = C_val * 1e6 * 2  # double for Pi stage
    # Stage 2: L in series
    L_uH = L_val * 1e6
    # Stage 3: C at output
    C2_uF = C_val * 1e6 * 2
    
    return {
        'C1_uF': C1_uF,
        'L_uH': L_uH,
        'C2_uF': C2_uF,
        'f_c_MHz': f_c / 1e6,
        'attenuation_dB': target_attenuation_dB
    }


# ─────────────────────────────────────────────
# 2. System Management Unit (SMU)
# ─────────────────────────────────────────────

def smu_emc_critical_circuits():
    """
    SMU critical EMI-sensitive circuits.
    - Reset circuit: susceptible to fast transients
    - Interrupt lines: susceptible to conducted noise
    - Clock oscillator: sensitive to RF fields
    - Power-on reset: requires filtered supply
    """
    return {
        'reset_pin': {
            'susceptibility': 'fast_transient_CS106',
            'protection': 'TVS + RC filter (100Ω + 100pF)',
            'threshold_V': 0.8
        },
        'interrupt': {
            'susceptibility': 'conducted_CS101',
            'protection': 'Series ferrite + bypass cap',
            'filter_fc_kHz': 10.0
        },
        'clock_oscillator': {
            'susceptibility': 'radiated_RS103',
            'protection': 'Shielded oscillator module + supply filtering',
            'frequency_MHz': 10.0
        },
        'power_on_reset': {
            'susceptibility': 'voltage_dip_CS101',
            'protection': 'Bulk cap 100μF + decoupling 100nF',
            'reset_V_uvlo': 4.5
        }
    }


def smu_emi_trace_separation(f_max_MHz=100.0):
    """
    Recommended trace separation for SMU PCB.
    For risetime t_r: ΔV = (0.2 * V_cc * l) / (t_r * v_prop * h)
    """
    # Propagation velocity on PCB: v ≈ c/√ε_r
    v_pcb = c / np.sqrt(4.5)  # ~1.4e8 m/s for FR4
    # 3σ rule: l_separation_mm = f_max_MHz * 0.3  (rule of thumb)
    l_sep_mm = f_max_MHz * 0.3
    return {
        'recommended_separation_mm': l_sep_mm,
        'v_pcb_m_s': v_pcb,
        'note': 'For coupled length at f_max, l_separation = 3*t_r*v'
    }


# ─────────────────────────────────────────────
# 3. Solid State Power Amplifier (SSPA) Design
# ─────────────────────────────────────────────

def sspa_spurious_emissions(Pout_dBm=40.0, n_harm=10, OIP3_dBm=50.0):
    """
    SSPA spurious and intermodulation products.
    - Harmonics: at n*f0, level ~ Pout - 10*log10(n)
    - Intermodulation: 3rd order IM = 2*P1 + 2*P2 - 2*OIP3 (dBc)
    """
    n = np.arange(1, n_harm + 1)
    # 2-tone intermodulation
    IM3_dBc = 2 * (Pout_dBm - OIP3_dBm)  # 3rd order IM
    # Harmonics (square wave approximation)
    harmonic_dBc = -20 * np.log10(n)  # each harmonic 6 dB down per n factor
    return {'IM3_dBc': IM3_dBc, 'harmonic_dBc': harmonic_dBc.tolist()}


def sspa_heatsink_thermal_noise(f_MHz=12000.0, T_K=300.0,
                                  bandwidth_MHz=500.0):
    """
    SSPA thermal noise from heatsink (Johnson-Nyquist).
    P_noise = k*T*B  (W)
    At f >> f_cutoff of thermal mass, noise couples to shielding.
    """
    k_B = 1.38e-23
    B = bandwidth_MHz * 1e6
    P_n_W = k_B * T_K * B
    P_n_dBm = 10 * np.log10(P_n_W * 1000)
    return {'P_noise_dBm': P_n_dBm, 'P_noise_W': P_n_W}


def sspa_input_filter_design(f_center_MHz=12000.0, bandwidth_MHz=500.0,
                              Z0_ohm=50.0, f_z_MHz=11000.0):
    """
    SSPA input/output bandpass filter design (Waveguide below cutoff).
    For mm-wave: use below-cutoff waveguide sections as high-Q filter.
    f_cutoff (circular WR):
      TE11: f_c ≈ 1.16 * c / d
    For d=2.5mm: f_c ≈ 46 GHz (for small package)
    """
    d_mm = 2.5
    f_c_GHz = 1.16 * c / (d_mm * 1e-3) / 1e9
    return {
        'f_center_GHz': f_center_MHz / 1e3,
        'bandwidth_MHz': bandwidth_MHz,
        'waveguide_cutoff_GHz': f_c_GHz,
        'filter_type': 'below-cutoff waveguide + E-plane iris'
    }


# ─────────────────────────────────────────────
# 4. RF Receiver EMC Design
# ─────────────────────────────────────────────

def rf_receiver_front_end_nf(P_in_dBm=-90.0, NF_dB=3.0, IIP3_dBm=10.0):
    """
    RF receiver front-end parameters.
    NF: noise figure (dB) — how much the front-end degrades SNR.
    IIP3: input-referred 3rd-order intercept point.
    """
    F = 10**(NF_dB / 10)  # linear
    noise_floor_dBm = -174 + 10 * np.log10(1e6) + NF_dB  # in 1 MHz BW
    return {
        'noise_floor_dBm': noise_floor_dBm,
        'dynamic_range_dB': IIP3_dBm - noise_floor_dBm,
        'IIP3_dBm': IIP3_dBm
    }


def lna_stability_factor(K_factor, delta):
    """
    LNA stability factor K.
    K > 1 for unconditional stability.
    K = (1 - |S11|² - |S22|² + |Δ|²) / (2*|S12*S21|)
    delta = S11*S22 - S12*S21
    """
    K = (1 - abs(S11)**2 - abs(S22)**2 + abs(delta)**2) / (2 * abs(S12 * S21))
    return {'K': K, 'stable': K > 1.0}


def receiver_desense_protection(P_blocker_dBm=0.0, f_blocker_MHz=2100.0,
                                 f_desired_MHz=2140.0, filter_rejection_dB=60.0):
    """
    RF receiver desense from strong blocker.
    """
    delta_f = abs(f_blocker_MHz - f_desired_MHz)
    # Simple frequency-dependent rejection model
    if delta_f < 10.0:
        rejection = 10.0
    else:
        rejection = 20.0 * np.log10(delta_f / 10.0) + filter_rejection_dB
    
    P_at_LNA = P_blocker_dBm - rejection
    desense_dB = max(0, (P_at_LNA + 30) / 3.0)  # approximate desense model
    
    return {
        'P_at_LNA_dBm': P_at_LNA,
        'rejection_dB': rejection,
        'desense_dB': desense_dB,
        'SNR_degradation_dB': desense_dB
    }


def rf_receiver_shielding_requirement(sensitivity_dBm=-100.0,
                                         P_interferer_dBm=-20.0,
                                         margin_dB=6.0):
    """
    Determine shielding SE needed at receiver enclosure.
    P_internal_max = sensitivity + margin
    SE = P_interferer_outside - P_internal_max
    """
    P_internal_max_dBm = sensitivity_dBm + margin_dB
    SE_required = P_interferer_dBm - P_internal_max_dBm
    return {
        'SE_required_dB': max(SE_required, 0),
        'P_internal_max_dBm': P_internal_max_dBm
    }


# ─────────────────────────────────────────────
# 5. EMC Rectification Case Study
# ─────────────────────────────────────────────

def rectification_loop_gain(RF_feedback_dB=30.0, mixer_conversion_loss_dB=8.0,
                              IF_amp_gain_dB=60.0, total_loop_dB=50.0):
    """
    EMC rectification loop gain analysis.
    If loop gain > 1: system can self-oscillate / regenerate EMI.
    Positive feedback: RF feedback + mixer + IF → demodulated baseband → RF
    """
    loop_gain_dB = RF_feedback_dB - mixer_conversion_loss_dB + IF_amp_gain_dB - total_loop_dB
    loop_gain_linear = 10**(loop_gain_dB / 20.0)
    return {
        'loop_gain_dB': loop_gain_dB,
        'loop_gain_linear': loop_gain_linear,
        'stability_margin_dB': 0 - loop_gain_dB if loop_gain_dB < 0 else 0,
        'oscillation_risk': loop_gain_dB > 0
    }


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == '__main__':
    import os
    os.makedirs('/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures', exist_ok=True)
    
    print("=== Chapter 8: Equipment EMC Design & Rectification ===\n")
    
    # 1. Power Supply
    print("--- 1. Power Supply EMI Filter ---")
    ps = power_supply_emc_layout(V_bus_V=28.0, P_load_W=100.0, f_sw_kHz=500)
    print(f"  Bus Z: {ps['Z_bus_ohm']:.1f} Ω, Switching noise: {ps['V_sw_noise_mV']:.2f} mV")
    
    filt = line_filter_design(target_attenuation_dB=40.0)
    print(f"  Pi filter: C1={filt['C1_uF']:.1f} μF, L={filt['L_uH']:.2f} μH, C2={filt['C2_uF']:.1f} μF")
    
    # 2. SMU
    print("\n--- 2. SMU Critical Circuits ---")
    smu = smu_emc_critical_circuits()
    print(f"  Reset pin protection: {smu['reset_pin']['protection']}")
    print(f"  Interrupt filter fc: {smu['interrupt']['filter_fc_kHz']:.0f} kHz")
    
    # 3. SSPA
    print("\n--- 3. SSPA Spurious Emissions ---")
    spurious = sspa_spurious_emissions(Pout_dBm=40.0, OIP3_dBm=50.0)
    print(f"  IM3 level: {spurious['IM3_dBc']:.1f} dBc (below carrier)")
    
    thermal = sspa_heatsink_thermal_noise()
    print(f"  Thermal noise (500 MHz BW, 300K): {thermal['P_noise_dBm']:.2f} dBm")
    
    sspa_filt = sspa_input_filter_design()
    print(f"  Input filter: {sspa_filt['filter_type']}, fc={sspa_filt['waveguide_cutoff_GHz']:.1f} GHz")
    
    # 4. RF Receiver
    print("\n--- 4. RF Receiver Front-End ---")
    rx = rf_receiver_front_end_nf()
    print(f"  Noise floor (1 MHz BW): {rx['noise_floor_dBm']:.1f} dBm, DR={rx['dynamic_range_dB']:.1f} dB")
    
    des = receiver_desense_protection(P_blocker_dBm=0.0, f_blocker_MHz=2100,
                                       f_desired_MHz=2140.0)
    print(f"  Desense @ 10 MHz offset: {des['desense_dB']:.2f} dB")
    
    sh = rf_receiver_shielding_requirement()
    print(f"  Shielding SE required: {sh['SE_required_dB']:.1f} dB")
    
    # 5. Rectification
    print("\n--- 5. Rectification Loop Gain ---")
    loop = rectification_loop_gain()
    print(f"  Loop gain: {loop['loop_gain_dB']:.1f} dB → "
          f"{'OSCILLATION RISK' if loop['oscillation_risk'] else 'STABLE'}")
    
    # Plot SSPA harmonics
    print("\n--- 6. Generating Figures ---")
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # SSPA harmonics
    spurious = sspa_spurious_emissions(Pout_dBm=40.0, n_harm=20)
    n = np.arange(1, 21)
    axes[0,0].bar(n, spurious['harmonic_dBc'], color='steelblue')
    axes[0,0].set_xlabel('Harmonic Number'); axes[0,0].set_ylabel('dBc')
    axes[0,0].set_title('SSPA Harmonic Emissions (Pout=40 dBm)')
    axes[0,0].grid(True, alpha=0.3)
    axes[0,0].set_ylim(-60, 0)
    
    # Line filter attenuation response
    f_range = np.logspace(2, 6, 400)
    fc = 50e3
    IL = np.where(f_range < fc, 0.0, 40 * np.log10(f_range / fc))
    axes[0,1].semilogx(f_range/1e3, IL, 'b-', lw=2)
    axes[0,1].set_xlabel('Frequency (kHz)'); axes[0,1].set_ylabel('Insertion Loss (dB)')
    axes[0,1].set_title('Line Filter Insertion Loss (fc=50 kHz, 40 dB/decade)')
    axes[0,1].grid(True, which='both', alpha=0.3)
    
    # Receiver blocking characteristic
    f_offset = np.linspace(1, 200, 400)
    P_at_LNA = 0.0 - (20 * np.log10(f_offset) + 40)  # rejection model
    axes[1,0].semilogx(f_offset, P_at_LNA, 'r-', lw=2)
    axes[1,0].set_xlabel('Frequency Offset (MHz)'); axes[1,0].set_ylabel('P_blocker at LNA (dBm)')
    axes[1,0].set_title('RF Receiver Blocking Characteristic')
    axes[1,0].grid(True, which='both', alpha=0.3)
    
    # EMI filter comparison (Pi vs T vs LC)
    f_filt = np.logspace(4, 7, 400)
    C_pi = 1e-6
    L_pi = 10e-6
    Z0 = 50.0
    omega = 2 * pi * f_filt
    IL_pi = 20 * np.log10(np.abs(1 + 1j * omega * L_pi / Z0 + 1j * omega * Z0 * C_pi) + 1e-12)
    axes[1,1].semilogx(f_filt/1e6, -np.clip(IL_pi, -80, 0), 'b-', lw=2, label='Pi filter')
    axes[1,1].set_xlabel('Frequency (MHz)'); axes[1,1].set_ylabel('IL (dB)')
    axes[1,1].set_title('Pi Filter Attenuation (L=10 μH, C=1 μF)')
    axes[1,1].grid(True, which='both', alpha=0.3); axes[1,1].legend()
    
    plt.tight_layout()
    out = '/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures/ch8_equipment_emc.png'
    plt.savefig(out, dpi=150, bbox_inches='tight')
    print(f"Figure: {out}")
    plt.close()
    
    print("\n✓ Chapter 8 code complete.")
