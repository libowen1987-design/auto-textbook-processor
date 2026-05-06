#!/usr/bin/env python3
"""
Zhang EMC - Chapter 6: Equipment-Level EMC Design
==================================================
Covers MIL-STD-461 CE/CS/RE/RS test items:
- CE101/CE102 (conducted emission, power leads)
- CS101/CS114 (conducted susceptibility)
- RE101/RE102 (radiated emission)
- RS103 (radiated susceptibility)
- PCB stackup design
- Shielding effectiveness
- Filter design (Pi, T, LC sections)
- ESD protection

Ref: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Ch6
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0, pi
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────
# 1. Conducted Emission Limits (CE101, CE102)
# ─────────────────────────────────────────────

def mil_std_461_ce101_limit(f_kHz_start=30, f_kHz_stop=50e3):
    """
    CE101: Conducted emissions, power leads, 30 Hz to 50 kHz.
    Applies to equipment with input power > 28 VDC.
    Limit varies by current and frequency (Zhang Table 6.1).
    """
    f = np.logspace(np.log10(f_kHz_start), np.log10(f_kHz_stop), 400)
    # Simplified: 120 dBμA quasi-peak for low freq, rolling off
    L1 = 120.0  # dBμA @ 30 Hz
    L2 = 85.0   # dBμA @ 1 kHz
    L3 = 85.0   # dBμA @ 10-50 kHz
    # Interpolate
    limit = np.where(f < 1e3, L1 - 35 * np.log10(f / 30),
                     np.where(f < 10e3, L2 - 0 * np.log10(f / 1e3),
                              L3 - 0 * np.log10(f / 10e3)))
    return f, np.clip(limit, 50.0, 130.0)


def mil_std_461_ce102_limit(f_kHz_start=10e3, f_kHz_stop=10e6):
    """
    CE102: Conducted emissions, power leads, 10 kHz to 10 MHz.
    Typical limit: 60 dBμV quasi-peak (60 Hz power) or 50 dBμV broad.
    """
    f = np.logspace(np.log10(f_kHz_start), np.log10(f_kHz_stop), 500)
    limit = np.where(f < 1e6, 60.0 * np.ones_like(f),
                     60.0 - 20.0 * np.log10(f / 1e6))
    return f, np.clip(limit, 40.0, 70.0)


def mil_std_461_ce106_limit(f_MHz_start=10e6, f_MHz_stop=18e9):
    """
    CE106: Conducted emissions, antenna port, 10 MHz to 40 GHz.
    Limit: 60 dBμV (up to 10 GHz), declining above.
    """
    f = np.logspace(np.log10(f_MHz_start), np.log10(f_MHz_stop), 600)
    limit = np.where(f < 1e9, 60.0 * np.ones_like(f),
                     60.0 - 20.0 * np.log10(f / 1e9))
    return f, np.clip(limit, 30.0, 80.0)


# ─────────────────────────────────────────────
# 2. Conducted Susceptibility Limits (CS101, CS114, CS115)
# ─────────────────────────────────────────────

def mil_std_461_cs101_limit(f_kHz_start=30, f_kHz_stop=400e3):
    """
    CS101: Conducted susceptibility, power leads, 30 Hz to 400 kHz.
    Limit: 85-100 dBμV (varies with frequency).
    """
    f = np.logspace(np.log10(f_kHz_start), np.log10(f_kHz_stop), 400)
    limit = np.where(f < 1e3, 100.0 * np.ones_like(f),
                     100.0 - 20.0 * np.log10(f / 1e3))
    limit = np.where(f < 100e3, limit,
                     100.0 - 40.0 * np.log10(f / 100e3))
    return f, np.clip(limit, 70.0, 110.0)


def mil_std_461_cs114_limit(f_kHz_start=10e3, f_MHz_stop=200e6):
    """
    CS114: Bulk cable injection, 10 kHz to 200 MHz.
    Limit: 77 dBμA (10 kHz to 30 MHz), declining above.
    """
    f = np.logspace(np.log10(f_kHz_start), np.log10(f_MHz_stop), 500)
    limit = np.where(f < 30e6, 77.0 * np.ones_like(f),
                     77.0 - 15.0 * np.log10(f / 30e6))
    return f, np.clip(limit, 60.0, 90.0)


def mil_std_461_cs115_limit():
    """
    CS115: Damped sinusoidal transient, bulk cable injection.
    Peak current: 10 A (or per equipment requirement).
    """
    return {'peak_current_A': 10.0,
            'pulse_width_us': 10.0,
            'fall_time_us': 1.0,
            'repetition_Hz': 1.0}


def mil_std_461_cs116_limit(f_kHz_start=1e3, f_kHz_stop=100e3):
    """
    CS116: Impulse transient susceptibility, 1 kHz to 100 kHz.
    Damped sinusoid: peak 10 A, period 1/frequency, resistance limited.
    """
    f = np.logspace(np.log10(f_kHz_start), np.log10(f_kHz_stop), 200)
    limit = np.where(f < 10e3, 10.0 * np.ones_like(f),
                     10.0 - 3.0 * np.log10(f / 10e3))
    return f, limit


# ─────────────────────────────────────────────
# 3. Radiated Emission Limits (RE101, RE102)
# ─────────────────────────────────────────────

def mil_std_461_re101_limit(f_kHz_start=30, f_MHz_stop=100e3):
    """
    RE101: Magnetic field radiated mission, 30 Hz to 100 kHz.
    Limit: 100 dBμA/m (at 30 Hz) declining to 20 dBμA/m at 100 kHz.
    """
    f = np.logspace(np.log10(f_kHz_start), np.log10(f_MHz_stop * 1e3), 400)
    limit = np.where(f < 100, 100.0 - 20.0 * np.log10(f / 30),
                     100.0 - 50.0 * np.log10(f / 100))
    return f, np.clip(limit, 10.0, 120.0)


def mil_std_461_re102_limit(f_MHz_start=2e3, f_GHz_stop=18e9):
    """
    RE102: Electric field radiated mission, 2 GHz to 18 GHz.
    Army application: 54 dBμV/m at 2 GHz declining to 20 dBμV/m.
    Navy/Air Force have different tables (simplified here).
    """
    f = np.logspace(np.log10(f_MHz_start), np.log10(f_GHz_stop), 500)
    # Army curve: 54 dBμV/m at 2 GHz, -10 dB/decade above 10 MHz
    limit = np.where(f < 10e6, 54.0 * np.ones_like(f),
                     54.0 - 10.0 * np.log10(f / 10e6))
    limit = np.clip(limit, 15.0, 70.0)
    return f, limit


def mil_std_461_re103_limit(f_MHz_start=2e3, f_GHz_stop=40e9):
    """
    RE103: Radiated mission from antenna port, 2 GHz to 40 GHz.
    Limit: 70 dBμV/m (up to 18 GHz), declining above.
    """
    f = np.logspace(np.log10(f_MHz_start), np.log10(f_GHz_stop), 500)
    limit = np.where(f < 18e9, 70.0 * np.ones_like(f),
                     70.0 - 20.0 * np.log10(f / 18e9))
    return f, np.clip(limit, 30.0, 85.0)


# ─────────────────────────────────────────────
# 4. Radiated Susceptibility Limits (RS101, RS103)
# ─────────────────────────────────────────────

def mil_std_461_rs101_limit(f_kHz_start=30, f_MHz_stop=100e3):
    """
    RS101: Radiated susceptibility, magnetic field, 30 Hz to 100 kHz.
    Limit: 85-115 dBμA/m (varies with frequency).
    """
    f = np.logspace(np.log10(f_kHz_start), np.log10(f_MHz_stop * 1e3), 400)
    limit = np.where(f < 1e3, 85.0 * np.ones_like(f),
                     85.0 + 30.0 * np.log10(f / 1e3))
    return f, np.clip(limit, 85.0, 130.0)


def mil_std_461_rs103_limit(f_MHz_start=2e6, f_GHz_stop=40e9, env='spacecraft'):
    """
    RS103: Radiated susceptibility, electric field, 2 MHz to 40 GHz.
    Typical spacecraft level: 5-20 V/m (MIL-STD-461 Table RS103 limits).
    This function returns the test field level.
    """
    f = np.logspace(np.log10(f_MHz_start), np.log10(f_GHz_stop), 500)
    if env == 'spacecraft':
        # Simplified: 20 V/m above 2 MHz for spacecraft
        level = 20.0 * np.ones_like(f)
    else:
        level = 5.0 * np.ones_like(f)
    return f, level


# ─────────────────────────────────────────────
# 5. PCB Stackup Design (Layer Architecture)
# ─────────────────────────────────────────────

def pcb_stackup_impedance(h_mm, w_mm, t_mm, eps_r=4.5, n_layers=4):
    """
    Calculate characteristic impedance for microstrip and stripline.
    h_mm: dielectric thickness (mm)
    w_mm: trace width (mm)
    t_mm: copper thickness (mm)
    eps_r: relative permittivity of substrate
    For microstrip (surface layer):
        Z0 ≈ 87 / sqrt(eps_r + 1.41) * ln(5.98*h / (0.8*w + t))
    For stripline (buried):
        Z0 ≈ 60 / sqrt(eps_r) * ln(2*b / (0.8*w + t))  [b=total thickness]
    """
    h = h_mm * 1e-3
    w = w_mm * 1e-3
    t = t_mm * 1e-3
    
    # Microstrip Z0 (Hammerstad formula)
    Z0_ms = (87.0 / np.sqrt(eps_r + 1.41)) * np.log(5.98 * h / (0.8 * w + t))
    
    # Stripline Z0
    b = h * (n_layers // 2)
    Z0_sl = (60.0 / np.sqrt(eps_r)) * np.log(2 * b / (0.8 * w + t))
    
    return {'Z0_microstrip_ohm': Z0_ms,
            'Z0_stripline_ohm': Z0_sl}


def pcb_cutoff_frequency(eps_r, h_mm, w_mm, d_mm):
    """
    Estimate PCB cavity resonance cutoff frequency.
    Parallel plate waveguide cutoff for stripline:
    f_c ≈ c / (2 * sqrt(eps_r)) * (1/w) for dominant mode.
    Or using经验的 resonance formula for rectangular cavity.
    """
    f_MHz = 7950 * 1e6 / (np.sqrt(eps_r) * d_mm)  # approx for square cavity
    return f_MHz


def via_inductance(h_mm, d_via_mm=0.5e3, pad_diameter_mm=0.6e3):
    """
    Estimate via parasitic inductance.
    L_via ≈ 10 * h_mm * ln(4*h/d)  (nH)  (Szeitz formula)
    """
    h = h_mm * 1e-3
    d = d_via_mm * 1e-3
    pad = pad_diameter_mm * 1e-3
    L = 10e-9 * h * np.log(4 * h / d)  # Henries → nH
    return L * 1e9  # nH


# ─────────────────────────────────────────────
# 6. Shielding Effectiveness
# ─────────────────────────────────────────────

def shielding_effectiveness_electric_field(f_MHz, sigma_cu=5.8e7,
                                           t_mm=1.0, mu_r=1.0):
    """
    Electric field shielding effectiveness for conductive enclosure.
    SE = R + A + B  (reflection + absorption + correction)
    For electric field (E-field): SE_dB ≈ 20*log10(η_s / (4*π*f*μ_r*σ))
    Simplified: SE ≈ 20*log10(1/(2π*f*μ*σ)) for thin shield
    """
    f = f_MHz * 1e6
    t = t_mm * 1e-3
    mu = mu_r * mu_0
    sigma = sigma_cu
    
    # Skin depth
    delta = np.sqrt(1.0 / (pi * f * mu * sigma))
    
    # Absorption loss (A = 8.69 * t / δ  in dB)
    A = 8.69 * t / delta if delta > 0 else 0
    
    # Reflection loss for E-field
    # R_E ≈ 168 - 10*log10(f*μ_r/σ)
    R = 168.0 - 10.0 * np.log10(f * mu_r / sigma)
    
    # Re-reflection correction (B ≈ 20*log10(1 - 10^(-A/20)) + 9.35*A/h)
    # Approximation for thick enough shields: B ≈ 0
    B = 0 if A > 10 else -20 * np.log10(1 - np.exp(-A * np.log(10) / 8.69))
    
    SE = R + A + B
    return {'SE_dB': max(SE, 0.5),
            'skin_depth_m': delta,
            'R_dB': R,
            'A_dB': A}


def multi_thickness_SE(f_MHz, thicknesses_mm, material='aluminum'):
    """
    Compute total SE for multi-layer shielding (e.g., boards, covers).
    """
    params = {
        'aluminum': {'sigma': 3.5e7, 'mu_r': 1.0},
        'copper':   {'sigma': 5.8e7, 'mu_r': 1.0},
        'steel':    {'sigma': 1.5e6, 'mu_r': 200.0},
        'mu-metal': {'sigma': 1.5e6, 'mu_r': 20000.0},
    }
    p = params.get(material.lower(), params['aluminum'])
    total_SE = 0.0
    for t_mm in thicknesses_mm:
        se = shielding_effectiveness_electric_field(f_MHz, sigma_cu=p['sigma'],
                                                   t_mm=t_mm, mu_r=p['mu_r'])
        total_SE += se['SE_dB']
    return total_SE


# ─────────────────────────────────────────────
# 7. EMI Filter Design (Pi, T, LC Sections)
# ─────────────────────────────────────────────

def emi_filter_pi_section(L_uH, C1_uF, C2_uF, f_MHz, Z0=50.0):
    """
    Pi filter: C-L-C section for conducted emission suppression.
    Attenuation at f (Hz): A ≈ 40*log10(f/f_c)  dB/decade above cutoff.
    Cutoff frequency: f_c = 1/(2π*sqrt(L*C_eq))
    """
    L = L_uH * 1e-6
    C1 = C1_uF * 1e-6
    C2 = C2_uF * 1e-6
    f = f_MHz * 1e6
    
    C_eq = C1 + C2  # series combination through L
    f_c = 1.0 / (2 * pi * np.sqrt(L * C_eq))
    X_L = 2 * pi * f * L
    X_C = 1.0 / (2 * pi * f * (C1 + C2) if (C1 + C2) > 0 else 1e-12)
    # Insertion loss approximation
    IL = 20 * np.log10(np.abs((1 + 1j * X_L / Z0) /
                               (1 + 1j * X_L / Z0 + 1j * X_C * Z0)) + 1e-12)
    return {'f_c_MHz': f_c / 1e6, 'IL_dB': min(IL, -60)}


def emi_filter_T_section(C_uF, L1_uH, L2_uH, f_MHz, Z0=50.0):
    """
    T filter: L-C-L section.
    """
    C = C_uF * 1e-6
    L1 = L1_uH * 1e-6
    L2 = L2_uH * 1e-6
    f = f_MHz * 1e6
    
    L_eq = L1 + L2
    f_c = 1.0 / (2 * pi * np.sqrt(L_eq * C))
    X_L = 2 * pi * f * L_eq
    X_C = 1.0 / (2 * pi * f * C)
    IL = 20 * np.log10(np.abs(1 / (1 + 1j * X_L / Z0 + 1j * X_C * Z0)) + 1e-12)
    return {'f_c_MHz': f_c / 1e6, 'IL_dB': min(IL, -60)}


def common_mode_choke(L_cm_uH, L_dm_uH, C_cm_nF, f_MHz, Z0=50.0):
    """
    Common-mode (CM) choke EMI filter.
    CM impedance: Z_cm ≈ jωL_cm + 1/(jωC_cm)
    DM impedance: Z_dm ≈ jωL_dm + 1/(jωC_cm)
    """
    L_cm = L_cm_uH * 1e-6
    L_dm = L_dm_uH * 1e-6
    C_cm = C_cm_nF * 1e-9
    f = f_MHz * 1e6
    
    Z_cm = 1j * 2 * pi * f * L_cm + 1.0 / (1j * 2 * pi * f * C_cm + 1e-12)
    Z_dm = 1j * 2 * pi * f * L_dm + 1.0 / (1j * 2 * pi * f * C_cm + 1e-12)
    # CM rejection ≈ |Z_cm/Z_dm| ratio
    CMRR = 20 * np.log10(np.abs(Z_cm) / (np.abs(Z_dm) + 1e-12))
    return {'Z_cm_ohm': np.abs(Z_cm), 'Z_dm_ohm': np.abs(Z_dm),
            'CMRR_dB': CMRR}


# ─────────────────────────────────────────────
# 8. ESD Protection
# ─────────────────────────────────────────────

def esd_voltage_clamp(V_zener_V, I_esd_A=30e-3, R_shunt_ohm=1.0):
    """
    ESD clamp diode voltage under surge current.
    V_clamped = V_zener + I * R_shunt + V_fwd_leakage
    V_zener: nominal Zener breakdown voltage
    I_esd: surge current (30 mA per MIL-STD-461 CS118)
    """
    V_clamped = V_zener_V + I_esd_A * R_shunt_ohm
    return {'V_clamped_V': V_clamped,
            'V_zener_V': V_zener_V,
            'I_esd_A': I_esd_A}


def esd_filter_cutoff(R_series_ohm, C_parasitic_pF, target_f_GHz=5e9):
    """
    RC-based ESD filter: f_c = 1/(2π*R*C)
    For ESD protection with added filter: f_c should be >> ESD bandwidth.
    """
    C = C_parasitic_pF * 1e-12
    f_c = 1.0 / (2 * pi * R_series_ohm * C)
    return {'f_c_Hz': f_c,
            'target_GHz': target_f_GHz,
            'adequate': f_c > target_f_GHz}


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == '__main__':
    import os
    os.makedirs('/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures', exist_ok=True)
    
    print("=== Chapter 6: Equipment-Level EMC Design ===\n")
    
    # 1. CE limits
    print("--- 1. CE/CE102 Limits ---")
    f, lim = mil_std_461_ce102_limit()
    print(f"  CE102 @ 100 kHz: {lim[0]:.0f} dBμV, @ 1 MHz: {lim[len(f)//2]:.0f} dBμV")
    
    # 2. RE102 limit
    print("\n--- 2. RE102 Radiated Emission (Army) ---")
    f, lim = mil_std_461_re102_limit()
    print(f"  RE102 @ 2 GHz: {lim[0]:.0f} dBμV/m, @ 10 GHz: {lim[len(f)//2]:.0f} dBμV/m")
    
    # 3. PCB impedance
    print("\n--- 3. PCB Impedance (4-layer stackup) ---")
    z = pcb_stackup_impedance(h_mm=0.2, w_mm=0.3, t_mm=0.035, eps_r=4.5)
    print(f"  Microstrip Z0: {z['Z0_microstrip_ohm']:.1f} Ω, Stripline: {z['Z0_stripline_ohm']:.1f} Ω")
    
    via_L = via_inductance(h_mm=3.0)
    print(f"  Via inductance (3mm board): {via_L:.2f} nH")
    
    # 4. Shielding
    print("\n--- 4. Shielding Effectiveness ---")
    se = shielding_effectiveness_electric_field(f_MHz=1000, t_mm=1.0)
    print(f"  Aluminum 1mm @ 1 GHz: SE={se['SE_dB']:.1f} dB (A={se['A_dB']:.1f} dB, R={se['R_dB']:.1f} dB)")
    
    multi_SE = multi_thickness_SE(1000, [0.5, 0.5], 'aluminum')
    print(f"  Double 0.5mm Al: SE={multi_SE:.1f} dB")
    
    # 5. EMI filter
    print("\n--- 5. EMI Pi Filter Design ---")
    filt = emi_filter_pi_section(L_uH=10.0, C1_uF=1.0, C2_uF=1.0, f_MHz=0.5)
    print(f"  Pi filter f_c={filt['f_c_MHz']:.2f} MHz, IL @ 0.5 MHz={filt['IL_dB']:.1f} dB")
    
    cm = common_mode_choke(L_cm_uH=5000, L_dm_uH=5, C_cm_nF=100, f_MHz=1.0)
    print(f"  CM choke: Z_cm={cm['Z_cm_ohm']:.0f} Ω, CMRR={cm['CMRR_dB']:.1f} dB")
    
    # 6. RS103
    print("\n--- 6. RS103 Radiated Susceptibility ---")
    f, level = mil_std_461_rs103_limit()
    print(f"  RS103 spacecraft test level: {level[0]:.0f} V/m")
    
    # 7. ESD
    print("\n--- 7. ESD Clamp Voltage ---")
    clamp = esd_voltage_clamp(V_zener_V=5.0, I_esd_A=0.030, R_shunt_ohm=1.0)
    print(f"  Clamped ESD voltage @ 30 mA surge: {clamp['V_clamped_V']:.2f} V")
    
    # Plot CE102 + RE102
    print("\n--- 8. Generating Figures ---")
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    f_ce, lim_ce = mil_std_461_ce102_limit()
    axes[0,0].semilogx(f_ce/1e3, lim_ce, 'b-', lw=2)
    axes[0,0].set_title('MIL-STD-461 CE102 Conducted Emission')
    axes[0,0].set_xlabel('Frequency (kHz)'); axes[0,0].set_ylabel('dBμV')
    axes[0,0].grid(True, which='both', alpha=0.3)
    
    f_re, lim_re = mil_std_461_re102_limit()
    axes[0,1].semilogx(f_re/1e6, lim_re, 'r-', lw=2)
    axes[0,1].set_title('MIL-STD-461 RE102 Radiated Emission (Army)')
    axes[0,1].set_xlabel('Frequency (MHz)'); axes[0,1].set_ylabel('dBμV/m')
    axes[0,1].grid(True, which='both', alpha=0.3)
    
    f_cs, lim_cs = mil_std_461_cs114_limit()
    axes[1,0].semilogx(f_cs/1e3, lim_cs, 'g-', lw=2)
    axes[1,0].set_title('MIL-STD-461 CS114 Conducted Susceptibility')
    axes[1,0].set_xlabel('Frequency (kHz)'); axes[1,0].set_ylabel('dBμA')
    axes[1,0].grid(True, which='both', alpha=0.3)
    
    f_rs, level_rs = mil_std_461_rs103_limit()
    axes[1,1].semilogx(f_rs/1e6, level_rs, 'm-', lw=2)
    axes[1,1].set_title('MIL-STD-461 RS103 Radiated Susceptibility (Spacecraft)')
    axes[1,1].set_xlabel('Frequency (MHz)'); axes[1,1].set_ylabel('V/m')
    axes[1,1].grid(True, which='both', alpha=0.3)
    
    plt.tight_layout()
    out = '/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures/ch6_mil_std_461_test_limits.png'
    plt.savefig(out, dpi=150, bbox_inches='tight')
    print(f"Figure: {out}")
    plt.close()
    
    print("\n✓ Chapter 6 code complete.")
