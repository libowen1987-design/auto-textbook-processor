#!/usr/bin/env python3
"""
Zhang EMC - Chapter 7: Component Selection & Module EMC Design
==============================================================
Core topics:
- DC/DC converter EMI analysis (CM/DM noise, filter design)
- 1553B / RS-422 / CSB bus interface circuit EMC design
- RF circuit shielding, filter grounding, and layout
- High-speed digital PCB design (multilayer stackup, crosstalk, PI)
- Processor module EMI characteristics

Ref: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Ch7
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0, pi
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────
# 1. DC/DC Converter EMI Analysis
# ─────────────────────────────────────────────

def dcdc_noise_spectrum(V_out_V=5.0, I_out_A=2.0, f_sw_kHz=500,
                        duty_cycle=0.5, ESR_cap_uF=100.0):
    """
    DC/DC converter EMI noise components:
    - DM (differential-mode) noise: V_dm ≈ L * di/dt
    - CM (common-mode) noise: I_cm ≈ C_parasitic * dv/dt
    - Harmonic content of switching waveform
    
    Returns noise spectrum at harmonics.
    """
    f_sw = f_sw_kHz * 1e3
    n_max = 50
    n = np.arange(1, n_max + 1)
    
    # Switching ripple amplitude
    # Square wave: amplitude at n-th harmonic = (2*V_out/nπ)*|sin(nπ*δ)|
    V_noise = (2 * V_out_V / (n * pi)) * np.abs(np.sin(n * pi * duty_cycle))
    # Decay factor (实际波形有一定斜率)
    tau_rise = 0.1e-6  # 100 ns rise time
    decay = np.exp(-2 * pi * n * f_sw * tau_rise)
    V_noise *= decay
    
    # DM noise current in output stage: I_dm ≈ V_noise / Z_out
    Z_out = V_out_V / I_out_A
    I_noise = V_noise / Z_out
    
    # CM noise estimate (parasitic C ~ 10-50 pF)
    C_parasitic = 20e-12  # 20 pF
    dv_dt = V_out_V / tau_rise
    I_cm = C_parasitic * dv_dt  # A
    
    return {
        'n': n,
        'f_harmonics_Hz': n * f_sw,
        'V_noise_V': V_noise,
        'I_noise_A': I_noise,
        'I_cm_A': I_cm
    }


def dcdc_input_filter_design(V_in_V=28.0, I_in_A=2.0, f_sw_kHz=500,
                              V_out_V=5.0, ripple_target_V=0.05,
                              Z_target_ohm=10.0):
    """
    Design a simple Pi filter for DC/DC input:
    L_min = V_in * D / (f_sw * ΔI)
    C_min = ΔI / (8 * f_sw * ΔV)
    Where ΔI is inductor current ripple, ΔV is output voltage ripple.
    """
    f_sw = f_sw_kHz * 1e3
    duty = V_out_V / V_in_V
    Delta_I = 0.3 * I_in_A  # 30% ripple
    Delta_V = ripple_target_V
    
    # Pi filter: L-C-L sections
    # L: from ripple requirement
    L_min = V_in_V * duty / (f_sw * Delta_I)
    # C: from ripple voltage requirement
    C_min = Delta_I / (8 * f_sw * Delta_V)
    
    # Second stage (for conducted emission compliance)
    L2 = 2.0e-6   # 2 μH
    C_feed = 10.0e-6  # 10 μF feedthrough
    
    return {
        'L_stage1_uH': L_min * 1e6,
        'C_stage1_uF': C_min * 1e6,
        'L_stage2_uH': L2 * 1e6,
        'C_feed_uF': C_feed * 1e6,
        'Delta_I_A': Delta_I,
        'Delta_V_V': Delta_V
    }


# ─────────────────────────────────────────────
# 2. Bus Interface Circuits (1553B, RS-422, CSB)
# ─────────────────────────────────────────────

def mil_std_1553b_characteristic_impedance(V_diff=1.0, R_load_ohm=100.0):
    """
    MIL-STD-1553B is a differential Manchester-encoded bus.
    Nominal characteristic impedance: 78 Ω (twisted pair)
    Data rate: 1 Mbps (10 μs bit time)
    """
    Z0_nominal = 78.0  # ohm
    V_out_diff_peak = V_diff  # V
    return {
        'Z0_ohm': Z0_nominal,
        'data_rate_Mbps': 1.0,
        'bit_time_us': 1.0,
        'max_length_m': 300.0,  # bus length
        'stub_length_m': 1.0     # max stub length
    }


def rs422_common_mode_range(V_cm_V=0.5, R_term_ohm=120.0):
    """
    RS-422 differential bus characteristics.
    Common-mode voltage range: ±7 V (relative to ground)
    Z0 ≈ 120 Ω (typical twisted pair)
    Maximum data rate: 10 Mbps
    """
    Z0_nominal = 120.0
    V_diff_max = 10.0  # V differential
    return {
        'Z0_ohm': Z0_nominal,
        'V_cm_range_V': 7.0,
        'V_diff_max_V': V_diff_max,
        'data_rate_Mbps': 10.0,
        'max_length_m': 1200.0
    }


def bus_crosstalk_reduction(d_sep_mm, l_bus_m, v_mbps=1.0,
                             n_twists_per_m=25):
    """
    Estimate bus crosstalk given:
    - d_sep_mm: wire separation (mm)
    - l_bus_m: parallel run length (m)
    - v_mbps: data rate (Mbps)
    - Twisting reduces coupling by cancellation factor
    """
    # Coupling coefficient (simplified)
    k0 = 2 * pi * v_mbps * 1e6 / c
    lambda_bus = c / (v_mbps * 1e6)
    Coupling_factor = (d_sep_mm * 1e-3) / lambda_bus * (l_bus_m / lambda_bus)
    
    # Twist cancellation: coupling_reduction = 1/(k0*l_twist) for k0*l_twist>>1
    twist_period = 1.0 / n_twists_per_m
    N_twists = int(l_bus_m * n_twists_per_m)
    cancellation = 1.0 / (k0 * twist_period * N_twists + 1)
    
    return {
        'coupling_factor': Coupling_factor,
        'twist_cancellation': cancellation,
        'effective_crosstalk': Coupling_factor * cancellation
    }


# ─────────────────────────────────────────────
# 3. RF Circuit Design (filter, shielding, layout)
# ─────────────────────────────────────────────

def microstrip_impedance(eps_r, h_mm, w_mm, t_mm=0.035e3):
    """
    Microstrip characteristic impedance (Hammerstad, Wheeler).
    eps_r: substrate relative permittivity
    h_mm: substrate height (mm)
    w_mm: trace width (mm)
    t_mm: copper thickness (mm)
    """
    h = h_mm * 1e-3
    w = w_mm * 1e-3
    t = t_mm * 1e-3
    
    if w/h >= 1:
        Z0 = (63.0 / np.sqrt(eps_r + 1.0)) * np.log(8 * h / w + w / (4 * h))
    else:
        Z0 = (31.5 / np.sqrt(eps_r + 1.0)) * np.log(8 * h / w + 0.25)
    
    return Z0


def coax_shielding_effectiveness(f_MHz, d_inner_mm, sigma_norm=5.8e7):
    """
    Coaxial cable shielding effectiveness.
    SE ≈ 20*log10(1/(2*pi*f*mu*sigma)) + 10*log10(d/t)  for braid.
    """
    f = f_MHz * 1e6
    mu = mu_0
    delta = np.sqrt(1.0 / (pi * f * mu * sigma_norm))
    t = d_inner_mm * 1e-3 * 0.1  # braid coverage ~10% of effective thickness
    SE_abs = 8.69 * t / delta if delta > 0 else 0
    SE_braid = 20.0 * np.log10(d_inner_mm / (t + 1e-6)) if t > 0 else 0
    return {'SE_total_dB': SE_abs + SE_braid,
            'skin_depth_m': delta}


def rf_filter_attenuation(fc_MHz, f_MHz, order=3, filter_type='low'):
    """
    RF filter attenuation using Butterworth prototype.
    order: filter order (3 = 18 dB/octave rolloff)
    fc_MHz: cutoff frequency
    """
    fc = fc_MHz * 1e6
    f = f_MHz * 1e6
    
    if filter_type == 'low':
        ratio = f / fc
        if ratio <= 1:
            return 0.0
        # Butterworth magnitude
        H = 1.0 / np.sqrt(1 + ratio**(2*order))
        atten = -20 * np.log10(H + 1e-12)
    else:
        ratio = fc / f
        H = 1.0 / np.sqrt(1 + ratio**(2*order))
        atten = -20 * np.log10(H + 1e-12)
    
    return max(atten, 0.0)


def cavity_resonance_frequency(a_mm, b_mm, d_mm, mode='TE101'):
    """
    Rectangular cavity resonance frequency.
    f_mnp = (c/2)*sqrt((m/a)² + (n/b)² + (p/d)²) / sqrt(eps_r)
    mode: 'TE101', 'TM110', etc.
    """
    a = a_mm * 1e-3
    b = b_mm * 1e-3
    d = d_mm * 1e-3
    
    # Parse mode
    if mode.startswith('TE'):
        m, n, p = 1, 0, 1 if '101' in mode else (1, 1, 0)
    elif mode.startswith('TM'):
        m, n, p = 1, 1, 0
    else:
        m, n, p = 1, 0, 1
    
    eps_r = 1.0  # air-filled cavity
    
    f = (c / 2.0) * np.sqrt((m / a)**2 + (n / b)**2 + (p / d)**2) / np.sqrt(eps_r)
    return f / 1e9  # GHz


# ─────────────────────────────────────────────
# 4. High-Speed Digital PCB Design
# ─────────────────────────────────────────────

def multilayer_pcb_stackup(eps_r=4.5, h_core_mm=1.5, h_prepreg_mm=0.2):
    """
    Standard 4-layer PCB stackup for spacecraft electronics.
    Layer 1: Signal (top)
    Layer 2: Ground plane
    Layer 3: Power plane
    Layer 4: Signal (bottom)
    """
    layers = [
        {'name': 'Layer 1 (Signal)', 'type': 'signal', 'z_m': 0.0},
        {'name': 'Layer 2 (Ground)', 'type': 'ground', 'z_m': h_prepreg_mm * 1e-3},
        {'name': 'Layer 3 (Power)', 'type': 'power', 'z_m': (h_prepreg_mm + h_core_mm) * 1e-3},
        {'name': 'Layer 4 (Signal)', 'type': 'signal', 'z_m': (h_prepreg_mm + h_core_mm + h_prepreg_mm) * 1e-3},
    ]
    
    # Characteristic impedance for microstrip
    h = h_prepreg_mm * 1e-3
    w = 0.3e-3  # trace width 0.3mm
    Z0 = microstrip_impedance(eps_r, h_prepreg_mm, w * 1e3, t_mm=0.035)
    
    return {'layers': layers, 'Z0_microstrip_ohm': Z0,
            'eps_r': eps_r, 'h_core_mm': h_core_mm}


def stripline_impedance(Z0_target, eps_r, b_total_mm, w_mm, t_mm=0.035):
    """
    Stripline impedance design (buried between two ground planes).
    Z0 ≈ 60*arccosh(b/(2w)) / sqrt(eps_r)   (for thin strip)
    b_total: total distance between ground planes
    """
    b = b_total_mm * 1e-3
    w = w_mm * 1e-3
    Z0_calc = (60.0 / np.sqrt(eps_r)) * np.arccosh(b / (2 * w) + 1e-12)
    return Z0_calc


def signal_crosstalk_near_end(d_sep_mm, l_coupling_m, h_mm,
                               V_aggressor=3.3, f_signal_MHz=100):
    """
    Near-end crosstalk (NEXT) for coupled microstrip lines.
    Agrawal model for 2-conductor system.
    """
    s = d_sep_mm * 1e-3
    h = h_mm * 1e-3
    l = l_coupling_m
    f = f_signal_MHz * 1e6
    lambda_m = c / f
    k0 = 2 * pi / lambda_m
    
    # Coupling coefficient
    k = (pi * h / lambda_m) * (l / lambda_m) * (V_aggressor / 50.0)
    NEXT = V_aggressor * (pi * h * l) / (lambda_m * s) if s > 1e-6 else 0
    FEXT = NEXT * np.sin(k0 * l) / (k0 * l)
    
    return {'NEXT_V': abs(NEXT), 'FEXT_V': abs(FEXT)}


def power_integrity_decoupling_capacitance(Z_target_ohm, f_target_MHz,
                                           V_ripple_V=0.05, I_load_A=2.0):
    """
    Power integrity: required decoupling capacitance.
    Z_target: target PDN impedance
    f_target: frequency at which Z_target must be maintained
    C_required ≈ 1/(2π*f_target*Z_target)
    """
    Z_target = Z_target_ohm
    f_target = f_target_MHz * 1e6
    
    C_min = 1.0 / (2 * pi * f_target * Z_target)
    # PDN budget: V_ripple / I_load = Z_target
    Z_budget = V_ripple_V / I_load_A
    
    return {
        'C_required_uF': C_min * 1e6,
        'Z_target_ohm': Z_target,
        'Z_budget_ohm': Z_budget,
        'adequate': Z_target <= Z_budget
    }


# ─────────────────────────────────────────────
# 5. Processor Module EMI Characteristics
# ─────────────────────────────────────────────

def clock_harmonic_radiation(V_clock=3.3, f_clock_MHz=100,
                               t_rise_ns=2.0, n_harmonics=30):
    """
    Clock harmonic radiated emission estimation.
    Radiated E-field at 3m for a small loop/dipole:
    E ≈ 1.316 * 10^-14 * V_clock * f_clock^2 * A_eff / r
    
    Simplified: harmonic amplitude at n*f_clock ≈ V_clock / n
    Risetime-controlled spectral rolloff above f_rt = 1/(pi*t_rise)
    """
    t_rise = t_rise_ns * 1e-9
    f_rt = 1.0 / (pi * t_rise)  # corner frequency
    
    n = np.arange(1, n_harmonics + 1)
    f_n = n * f_clock_MHz * 1e6
    f_rt_MHz = f_rt / 1e6
    
    # Base harmonic amplitude (square wave)
    V_n = V_clock / (n * pi)
    
    # Risetime rolloff
    rolloff = np.where(f_n < f_rt, 1.0, f_rt_MHz / f_n)
    V_n_actual = V_n * rolloff
    
    return {'n': n, 'f_MHz': f_n / 1e6, 'V_n_V': V_n_actual}


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == '__main__':
    import os
    os.makedirs('/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures', exist_ok=True)
    
    print("=== Chapter 7: Component & Module EMC Design ===\n")
    
    # 1. DC/DC EMI
    print("--- 1. DC/DC Noise Spectrum ---")
    noise = dcdc_noise_spectrum(V_out_V=5.0, I_out_A=2.0, f_sw_kHz=500)
    print(f"  CM noise current (parasitic): {noise['I_cm_A']*1e6:.3f} μA")
    print(f"  DM noise @ 1st harmonic: {noise['V_noise_V'][0]*1000:.3f} mV")
    
    filt = dcdc_input_filter_design()
    print(f"  Filter stage 1: L={filt['L_stage1_uH']:.2f} μH, C={filt['C_stage1_uF']:.2f} μF")
    
    # 2. Bus
    print("\n--- 2. Bus Interface (1553B / RS-422) ---")
    b1553 = mil_std_1553b_characteristic_impedance()
    print(f"  1553B Z0={b1553['Z0_ohm']:.0f} Ω, rate={b1553['data_rate_Mbps']:.0f} Mbps")
    b422 = rs422_common_mode_range()
    print(f"  RS-422 Z0={b422['Z0_ohm']:.0f} Ω, CM range=±{b422['V_cm_range_V']:.0f} V")
    
    # 3. RF
    print("\n--- 3. RF Microstrip Impedance ---")
    Z0 = microstrip_impedance(eps_r=4.5, h_mm=0.5, w_mm=0.8)
    print(f"  Rogers RO4003 (h=0.5mm, w=0.8mm): Z0={Z0:.1f} Ω")
    
    se_coax = coax_shielding_effectiveness(1000, 2.2)
    print(f"  RG-214 SE @ 1 GHz: {se_coax['SE_total_dB']:.1f} dB")
    
    # Cavity resonance
    f_res = cavity_resonance_frequency(100, 60, 10, 'TE101')
    print(f"  Cavity TE101 resonance (100×60×10mm): {f_res:.3f} GHz")
    
    # 4. PCB
    print("\n--- 4. PCB Stackup & Crosstalk ---")
    stackup = multilayer_pcb_stackup()
    print(f"  4-layer Z0 (microstrip): {stackup['Z0_microstrip_ohm']:.1f} Ω")
    
    crosstalk = signal_crosstalk_near_end(d_sep_mm=0.3, l_coupling_m=0.1,
                                          h_mm=0.2, f_signal_MHz=200)
    print(f"  NEXT @ 200 MHz, 10cm trace: {crosstalk['NEXT_V']*1000:.3f} mV")
    
    # 5. Power integrity
    print("\n--- 5. Power Integrity Decoupling ---")
    pi_result = power_integrity_decoupling_capacitance(Z_target_ohm=0.1, f_target_MHz=100,
                                                 V_ripple_V=0.05, I_load_A=2.0)
    print(f"  Required C @ 100 MHz target: {pi_result['C_required_uF']:.2f} μF")
    print(f"  PDN budget: Z < {pi_result['Z_budget_ohm']:.3f} Ω → {'OK' if pi_result['adequate'] else 'FAIL'}")
    
    # 6. Clock harmonics
    print("\n--- 6. Clock Harmonic Radiation ---")
    clock = clock_harmonic_radiation(f_clock_MHz=100, t_rise_ns=2.0)
    print(f"  Harmonic 3 (300 MHz): {clock['V_n_V'][2]:.4f} V (3rd harmonic)")
    print(f"  Harmonic 10 (1 GHz): {clock['V_n_V'][9]:.4f} V (10th)")
    
    # Plot DC/DC noise spectrum
    print("\n--- 7. Generating Figures ---")
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    noise = dcdc_noise_spectrum()
    ax = axes[0,0]
    ax.semilogx(noise['f_harmonics_Hz']/1e6, 20*np.log10(noise['V_noise_V']+1e-12),
                'bo-', ms=4)
    ax.set_xlabel('Frequency (MHz)'); ax.set_ylabel('V_noise (dBV)')
    ax.set_title('DC/DC Converter Noise Spectrum')
    ax.grid(True, which='both', alpha=0.3)
    
    # RF filter attenuation
    freqs = np.logspace(1, 4, 400)  # 10 MHz to 10 GHz
    fc = 1000  # 1 GHz cutoff
    atten = [rf_filter_attenuation(fc, f/1e6, order=3) for f in freqs]
    axes[0,1].semilogx(freqs, atten, 'g-', lw=2)
    axes[0,1].set_xlabel('Frequency (MHz)'); axes[0,1].set_ylabel('Attenuation (dB)')
    axes[0,1].set_title(f'3rd Order Low-Pass Filter (fc={fc} MHz)')
    axes[0,1].grid(True, which='both', alpha=0.3)
    
    # Clock harmonics
    clock = clock_harmonic_radiation()
    axes[1,0].stem(clock['f_MHz'], 20*np.log10(clock['V_n_V']+1e-12),
                   basefmt=' ')
    axes[1,0].set_xlabel('Harmonic Freq (MHz)'); axes[1,0].set_ylabel('dBV')
    axes[1,0].set_title('Clock Harmonic Radiation (100 MHz, tr=2ns)')
    axes[1,0].grid(True, which='both', alpha=0.3)
    
    # PDN impedance
    f_pdn = np.logspace(3, 9, 400)
    C_test = 4.7e-6  # 4.7 μF ceramic
    Z_pdn = 1.0 / (2 * pi * f_pdn * C_test)
    axes[1,1].loglog(f_pdn/1e6, Z_pdn*1e3, 'r-', lw=2)
    axes[1,1].axhline(y=0.1*1e3, color='k', linestyle='--', label='0.1 Ω target')
    axes[1,1].set_xlabel('Frequency (MHz)'); axes[1,1].set_ylabel('PDN Z (mΩ)')
    axes[1,1].set_title('PDN Impedance (4.7 μF Decoupling)')
    axes[1,1].legend(); axes[1,1].grid(True)
    
    plt.tight_layout()
    out = '/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures/ch7_pcb_dcdc.png'
    plt.savefig(out, dpi=150, bbox_inches='tight')
    print(f"Figure: {out}")
    plt.close()
    
    print("\n✓ Chapter 7 code complete.")
