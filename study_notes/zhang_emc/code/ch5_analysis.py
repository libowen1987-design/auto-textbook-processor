#!/usr/bin/env python3
"""
Zhang EMC - Chapter 5: Spacecraft System-Level EMC Analysis
============================================================
Core topics:
- EMI margin determination
- Inter-system EMC analysis (spacecraft + launch vehicle, multi-satellite)
- Cable crosstalk analysis
- Field-cable coupling analysis
- Passive Intermodulation (PIM) analysis
- RF compatibility analysis
- HERP/HERF hazard analysis

Ref: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Ch5
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0, pi
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────
# 1. EMI Margin Determination
# ─────────────────────────────────────────────

def emi_margin(emission_dBm, path_loss_dB, coupling_dB, immunity_dBm, margin_req_dB=6.0):
    """
    Standard EMI margin calculation per MIL-STD-461 / Zhang Ch5.
    EMI Margin = Immunity - (Emission - Path Loss - Coupling)
    Returns margin in dB. Positive = adequate margin.
    """
    received = emission_dBm - path_loss_dB - coupling_dB
    margin = immunity_dBm - received
    return {
        'emission_dBm': emission_dBm,
        'received_dBm': received,
        'immunity_dBm': immunity_dBm,
        'margin_dB': margin,
        'path_loss_dB': path_loss_dB,
        'coupling_dB': coupling_dB,
        'pass': margin >= margin_req_dB
    }


def worst_case_emi_margin(emission_p_dBm, path_loss_p_dB, coupling_p_dB,
                           immunity_p_dBm, p_confidence=95):
    """
    Statistical worst-case EMI margin at given confidence percentile.
    Uses Gaussian superposition of uncertainties.
    p_confidence: percentile (e.g. 95 = 95th percentile worst case)
    """
    # Emission uncertainty ±3σ → effectively ±3 dB for uniform distribution
    # Path loss uncertainty (model accuracy ±1 dB per 20 dB path)
    # Coupling uncertainty (±2 dB for manufacturing variation)
    # Immunity uncertainty (±1.5 dB)
    emission_var = 3.0**2
    path_var = 1.0**2
    coupl_var = 2.0**2
    immun_var = 1.5**2
    total_var = emission_var + path_var + coupl_var + immun_var
    sigma_total = np.sqrt(total_var)
    
    # Scale factor for p_confidence (z-score)
    z = {90: 1.28, 95: 1.645, 99: 2.33}.get(p_confidence, 1.645)
    
    emission_mean = emission_p_dBm
    path_mean = path_loss_p_dB
    coupl_mean = coupling_p_dB
    immun_mean = immunity_p_dBm
    
    # Worst-case (95th percentile of margin = immunity - received)
    # Received worst-case = emission + |coupling| + path loss (all negative contributions)
    emission_wc = emission_mean + z * np.sqrt(emission_var)
    coupling_wc = coupling_p_dB - z * np.sqrt(coupl_var)  # more coupling loss = smaller magnitude
    immun_wc = immun_mean - z * np.sqrt(immun_var)       # reduced immunity
    
    received_wc = emission_wc - path_mean - coupling_wc  # worst-case received
    margin_wc = immun_wc - received_wc
    return margin_wc


# ─────────────────────────────────────────────
# 2. Inter-System EMC: Spacecraft + Launch Vehicle
# ─────────────────────────────────────────────

def launch_vehicle_emc_separation(frequency_MHz, transmit_power_dBm,
                                   transmit_gain_dBi, receive_gain_dBi,
                                   required_isolation_dB=100):
    """
    Calculate required minimum separation between spacecraft and launch vehicle
    based on transmit power, antenna gains, and required isolation.
    frequency_MHz: transmit frequency (MHz)
    transmit_power_dBm: TX output power (dBm)
    transmit_gain_dBi: TX antenna gain (dBi)
    receive_gain_dBi: RX antenna gain on victim system (dBi)
    required_isolation_dB: needed isolation (dB)
    
    Free-space path loss: L_fs(dB) = 20*log10(4πd/λ)
    Solve for d: d = λ * 10^(isolation/20) / (4π)
    """
    lambda_m = 3e8 / (frequency_MHz * 1e6)
    # Total loss = transmit_power + transmit_gain + receive_gain - isolation
    # Path loss must provide the rest
    # isolation_needed = transmit_power + transmit_gain + receive_gain - L_fs
    # L_fs = transmit_power + transmit_gain + receive_gain - isolation
    L_fs_required = transmit_power_dBm + transmit_gain_dBi + receive_gain_dBi - required_isolation_dB - 30  # dB (30 converts dBm to dB ref 1mW)
    # Actually all in dB scale properly:
    # isolation = EIRP(dB) + G_receive - L_fs
    # L_fs = EIRP + G_receive - isolation
    EIRP_dB = transmit_power_dBm - 30 + transmit_gain_dBi  # EIRP wrt 1 mW
    
    # Solve d from L_fs = 20*log10(4πd/λ)
    d_m = lambda_m / (4 * pi) * 10**(L_fs_required / 20.0)
    return max(d_m, 0.01)  # at least 1 cm


def multipath_fade_margin(frequency_MHz, distance_m, n_reflections=2,
                           reflectivity=0.5):
    """
    Estimate multipath fade margin for spacecraft link.
    Simple two-ray (direct + ground reflection) model.
    Returns fade margin in dB.
    """
    lambda_m = 3e8 / (frequency_MHz * 1e6)
    h_tx = 1.0   # transmitter height (m)
    h_rx = 1.0   # receiver height (m)
    d = distance_m
    # Path difference between direct and reflected ray
    d_direct = np.sqrt(d**2 + (h_rx - h_tx)**2)
    d_reflected = np.sqrt(d**2 + (h_rx + h_tx)**2)
    delta_d = d_reflected - d_direct
    # Phase difference
    Delta_phi = 2 * pi * delta_d / lambda_m
    # Amplitude of reflected relative to direct
    rho = reflectivity * np.exp(1j * Delta_phi)
    # Composite received field
    E_total = 1 + rho
    fade_margin_dB = 20 * np.log10(np.abs(E_total) + 1e-12)
    return min(fade_margin_dB, 0.0)


def emc_margin_launch_vehicle(f_tx_dBm=70.0, G_tx_dBi=3.0, G_rx_dBi=0.0,
                                f_MHz=2000.0, d_sep_m=10.0,
                                immunity_dBm=-40.0):
    """
    Check spacecraft-vs-launch-vehicle EMC margin.
    """
    lambda_m = 3e8 / (f_MHz * 1e6)
    # Free-space path loss
    L_fs = 20 * np.log10(4 * pi * d_sep_m / lambda_m)
    EIRP_dB = f_tx_dBm - 30 + G_tx_dBi
    P_rx_dBm = EIRP_dB - L_fs + G_rx_dBi - 30  # reference 1 mW
    margin = immunity_dBm - P_rx_dBm
    return {'L_fs_dB': L_fs, 'EIRP_dBm': EIRP_dB + 30,
            'P_rx_dBm': P_rx_dBm, 'margin_dB': margin,
            'pass': margin > 6.0}


# ─────────────────────────────────────────────
# 3. Cable Crosstalk Analysis
# ─────────────────────────────────────────────

def crosstalk_parallel_cable(l_coupling_m, s_mm, h_mm, d_both_mm,
                             V_aggressor=5.0, Z0=50.0, f=100e6):
    """
    Near-end (NEXT) and far-end (FEXT) crosstalk for parallel cables.
    Simplified Agrawal model for horizontal wires above ground plane.
    l_coupling_m:  coupling length (m)
    s_mm:           separation between aggressor and victim (mm)
    h_mm:           height above ground (mm)
    d_both_mm:      if both wires above ground, reference separation (mm)
    V_aggressor:    aggressor signal voltage (V)
    Z0:             cable characteristic impedance (Ω)
    f:              frequency (Hz)
    Returns (NEXT_V, FEXT_V) in volts.
    """
    s = s_mm * 1e-3
    h = h_mm * 1e-3
    k0 = 2 * pi * f / c
    lambda_m = c / f
    beta = 2 * pi / lambda_m
    
    # Mutual inductance and capacitance per unit length (parallel wires over ground)
    # L_m ≈ (μ0/π) * arccosh(d/2a) for wires radius a
    a = 0.5e-3   # wire radius ~1mm dia
    d_ref = max(s, d_both_mm * 1e-3)
    # Simplified: C_m ≈ ε0 * π * h / s  (horizontal strip approximation)
    # L_m ≈ μ0 * s / (π * h)
    C_m = epsilon_0 * pi * h / s  # F/m
    L_m = mu_0 * s / (pi * h)     # H/m
    Z_c = np.sqrt(L_m / C_m)      # coupling mode impedance
    
    # Coupling coefficient (common-mode)
    gamma = (pi * h / lambda_m) * (l_coupling_m / lambda_m) * (V_aggressor / Z0)
    k = k0 * l_coupling_m
    # NEXT ≈ (V * l * πh) / (λ * s)
    NEXT = V_aggressor * (pi * h) * l_coupling_m / (lambda_m * s) if s > 0 else 0
    FEXT = NEXT * np.sin(k) / k if k > 0 else 0
    return abs(NEXT), abs(FEXT)


def twisted_pair_crosstalk_reduction(s_mm, n_twists_per_m=40,
                                      l_coupling_m=1.0, f=10e6):
    """
    Estimate crosstalk reduction from twisting.
    Twist electrically cancels common-mode coupling.
    """
    # With twist, differential mode coupling is reduced by ~1/(|k*l|) for k*l >> 1
    k0 = 2 * pi * f / c
    twist_period = 1.0 / n_twists_per_m  # m
    N_twists = int(l_coupling_m / twist_period)
    # Effective coupling cancellation factor
    cancellation = 1.0 / (k0 * twist_period * N_twists + 1)
    return cancellation


# ─────────────────────────────────────────────
# 4. Field-to-Cable Coupling
# ─────────────────────────────────────────────

def field_cable_coupling(E_inc_V_m, f_MHz, cable_length_m, orientation='broadside'):
    """
    Field-to-cable coupling: external field induces voltage on cable.
    Based on transmission line theory (Akao-Hayami model).
    E_inc_V_m:     incident field strength (V/m)
    f_MHz:         frequency (MHz)
    cable_length_m: cable exposed length (m)
    orientation:   'broadside' or 'end-on'
    Returns induced voltage on cable (V).
    """
    f = f_MHz * 1e6
    lambda_m = 3e8 / f
    k0 = 2 * pi / lambda_m
    l = cable_length_m
    theta = pi / 2 if orientation == 'broadside' else 0
    
    # Effective height of wire antenna
    h_eff = (2 * l / pi) * np.sin(k0 * l / 2) * np.cos(theta)
    V_induced = E_inc_V_m * h_eff
    
    # Alternative: using "antenna factor" approach
    # For short dipole: h_eff ≈ l/2
    h_short = l / 2
    V_short = E_inc_V_m * h_short
    
    return abs(V_induced), abs(V_short)


def cable_shielding_effectiveness(f_MHz, shield_type='braided', d_mm=5.0):
    """
    Estimate cable shielding effectiveness.
    d_mm: shield diameter (mm)
    f_MHz: frequency (MHz)
    """
    # Approximate SE for common shield types (dB)
    f = f_MHz
    d = d_mm
    if shield_type == 'braided':
        # Braided shield: SE ≈ 40 - 20*log10(f) for typical coverage
        SE = 40.0 - 20.0 * np.log10(f + 0.1)
    elif shield_type == 'solid':
        SE = 80.0 - 20.0 * np.log10(f + 0.1)
    elif shield_type == 'foil':
        SE = 60.0 - 20.0 * np.log10(f + 0.1)
    else:
        SE = 20.0 - 10.0 * np.log10(f + 0.1)
    return max(SE, 10.0)


# ─────────────────────────────────────────────
# 5. Passive Intermodulation (PIM)
# ─────────────────────────────────────────────

def pim_frequency(f1_MHz, f2_MHz, n=3, m=3):
    """
    PIM frequency: f_PIM = |n*f1 - m*f2| or n*f1 + m*f2.
    Common PIM products: 3rd order (2*f1 - f2, 2*f2 - f1).
    """
    f1 = f1_MHz * 1e6
    f2 = f2_MHz * 1e6
    # 3rd order products
    f_pim1 = abs(2*f1 - f2) / 1e6  # MHz
    f_pim2 = abs(2*f2 - f1) / 1e6
    f_pim3 = (2*f1 + f2) / 1e6
    return {'f_pim_2f1_f2_MHz': f_pim1, 'f_pim_2f2_f1_MHz': f_pim2,
            'f_pim_2f1p2f2_MHz': f_pim3}


def pim_power_estimate(P1_dBm, P2_dBm, IIP3_dBm=50.0):
    """
    Estimate PIM power from two-tone input.
    3rd order PIM intercept point: PIM3 = 2*P1 + 2*P2 - 2*IIP3  (dBc below each carrier)
    Or: PIM_level = 3*P_in - 2*IIP3  relative to carrier
    """
    P1_W = 1e-3 * 10**(P1_dBm / 10)
    P2_W = 1e-3 * 10**(P2_dBm / 10)
    P_in = P1_W + P2_W
    P_in_dBm = 10 * np.log10(P_in * 1000)
    # PIM3 level relative to each carrier
    PIM3_dBc = 2 * (P_in_dBm - IIP3_dBm)
    PIM3_dBm = P_in_dBm + PIM3_dBc
    return {
        'PIM3_dBc': PIM3_dBc,
        'PIM3_dBm': PIM3_dBm,
        'IIP3_dBm': IIP3_dBm
    }


# ─────────────────────────────────────────────
# 6. RF Compatibility Analysis
# ─────────────────────────────────────────────

def intermodulation_free_dynamic_range(OP1dB_sat, IIP3_dBm):
    """
    IFDR (Intermodulation-Free Dynamic Range) for RF receivers.
    IFDR ≈ (2/3) * (IIP3 - OP1dB_sat)
    """
    IFDR = (2.0 / 3.0) * (IIP3_dBm - OP1dB_sat)
    return IFDR


def receiver_desense(P_interferer_dBm, coupling_dB, noise_floor_dBm=-100.0,
                     IIP3_dBm=30.0):
    """
    Receiver desensitization due to strong out-of-band interferer.
    The interferer is filtered but some energy leaks through (coupling).
    """
    P_rx = P_interferer_dBm - abs(coupling_dB)
    # Blocker causes gain compression - increase in noise floor
    # Approximation: noise floor rises by approx (P_rx - IIP3)/3 dB
    # if P_rx exceeds IIP3 by X dB, desense ≈ X/3 dB
    if P_rx > IIP3_dBm:
        desense_dB = (P_rx - IIP3_dBm) / 3.0
    else:
        desense_dB = 0.0
    effective_nf = noise_floor_dBm + desense_dB
    return {
        'P_interferer_at_RX_dBm': P_rx,
        'desense_dB': desense_dB,
        'effective_noise_floor_dBm': effective_nf
    }


def rf_compatibility_check(f_signal_MHz, signal_bw_kHz, P_signal_dBm,
                            f_interferer_MHz, P_interferer_dBm,
                            IIP3_dBm, adjacent_channel_rejection_dB=60.0):
    """
    Check RF compatibility between wanted signal and interferer.
    """
    # Frequency separation
    delta_f = abs(f_signal_MHz - f_interferer_MHz)
    
    # Adjacent channel rejection
    if delta_f < 1.0:  # same channel
        ACI = 0.0
    else:
        # Simple model: 20 dB/decade rolloff
        ACI = min(adjacent_channel_rejection_dB + 20 * np.log10(delta_f / 1.0), 80.0)
    
    interferer_at_RX = P_interferer_dBm - ACI
    SINR_required = 10.0  # dB typical for digital comms
    noise_floor = -100.0
    signal_interferer_ratio = P_signal_dBm - interferer_at_RX
    
    return {
        'delta_f_MHz': delta_f,
        'ACI_dB': ACI,
        'interferer_at_RX_dBm': interferer_at_RX,
        'signal_interferer_ratio_dB': signal_interferer_ratio,
        'pass': signal_interferer_ratio > SINR_required
    }


# ─────────────────────────────────────────────
# 7. HERP / HERF Hazard Analysis
# ─────────────────────────────────────────────

def herp_hazard_range(P_tx_W, G_tx_dBi, frequency_MHz,
                       threshold_W_m2=0.1, H_field_threshold_A_m=80.0):
    """
    HERP (Human Exposure to RF Radiation) hazard distance.
    For far-field: power density S = (P_tx * G) / (4πr²)
    threshold for whole-body exposure: 10 W/m² (ANSI C95.1)
    But for HERP (personnel): use 100 W/m² peak.
    
    Also calculates H-field hazard distance for near-field.
    """
    P_tx = P_tx_W
    G = 10**(G_tx_dBi / 10)
    f = frequency_MHz * 1e6
    lambda_m = c / f
    
    # Far-field condition: r > 0.62 * sqrt(D³/λ)
    # Equivalent: use plane-wave approximation above this
    
    # Power density hazard distance
    r_S = np.sqrt(P_tx * G / (4 * pi * threshold_W_m2))
    # H-field in far-field: H = sqrt(S/377)
    H_S = np.sqrt(threshold_W_m2 / 377.0)
    # H-field hazard distance (for loop antenna near-field H = I*A/(2πr³))
    # Approximate: r_H = (G * P_tx / (2π * H_threshold))^(1/3)
    # Using plane-wave equivalent: r_H = sqrt(P_tx * G / (4π * Z0 * H_threshold²))
    Z0 = 377.0
    r_H = np.sqrt(P_tx * G / (4 * pi * Z0 * (H_field_threshold_A_m / np.sqrt(377.0))**2))
    
    return {
        'power_density_hazard_dist_m': r_S,
        'H_field_hazard_dist_m': r_H,
        'lambda_m': lambda_m
    }


def herf_hazard_check(P_tx_W, G_tx_dBi, separation_m, f_MHz,
                       EED_threshold_V_m=200.0):
    """
    HERF (Hazards of Electromagnetic Radiation to Fuel/Energetics).
    Check whether EM radiation can ignite fuel or damage EEDs.
    EED threshold: typically 200 V/m for firing
    """
    P_tx = P_tx_W
    G = 10**(G_tx_dBi / 10)
    f = f_MHz * 1e6
    lambda_m = c / f
    
    # Far-field electric field
    S = P_tx * G / (4 * pi * separation_m**2)
    E = np.sqrt(S * 377.0)
    
    return {
        'E_field_V_m': E,
        'EED_threshold_V_m': EED_threshold_V_m,
        'hazard': E > EED_threshold_V_m,
        'safety_factor_dB': 20 * np.log10(EED_threshold_V_m / E) if E > 0 else 99
    }


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

if __name__ == '__main__':
    import os
    os.makedirs('/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures', exist_ok=True)
    
    print("=== Chapter 5: System-Level EMC Analysis ===\n")
    
    # 1. EMI Margin
    print("--- 1. EMI Margin ---")
    m = emi_margin(emission_dBm=-20, path_loss_dB=40, coupling_dB=-30,
                   immunity_dBm=-50, margin_req_dB=6)
    print(f"  Margin: {m['margin_dB']:.1f} dB → {'PASS' if m['pass'] else 'FAIL'}")
    
    wc_margin = worst_case_emi_margin(-20, 40, -30, -50, p_confidence=95)
    print(f"  95th-percentile worst-case margin: {wc_margin:.2f} dB")
    
    # 2. Launch Vehicle separation
    print("\n--- 2. Launch Vehicle Separation ---")
    d_sep = launch_vehicle_emc_separation(2000, 70, 3, 0, required_isolation_dB=100)
    print(f"  Required separation at 2 GHz, 70 dBm TX: {d_sep:.2f} m")
    
    lv = emc_margin_launch_vehicle()
    print(f"  LV EMC margin at 10 m: {lv['margin_dB']:.1f} dB → {'PASS' if lv['pass'] else 'FAIL'}")
    
    # 3. Crosstalk
    print("\n--- 3. Cable Crosstalk ---")
    NEXT, FEXT = crosstalk_parallel_cable(l_coupling_m=1.0, s_mm=5.0,
                                           h_mm=10.0, d_both_mm=10.0, f=100e6)
    print(f"  NEXT: {NEXT*1000:.3f} mV, FEXT: {FEXT*1000:.3f} mV (100 MHz, 1m pair, 5mm sep)")
    
    # 4. Field-cable coupling
    print("\n--- 4. Field-to-Cable Coupling ---")
    V1, V2 = field_cable_coupling(E_inc_V_m=10.0, f_MHz=100.0,
                                   cable_length_m=3.0, orientation='broadside')
    print(f"  Induced voltage (broadside): {V1:.3f} V")
    print(f"  Induced voltage (end-on approx): {V2:.3f} V")
    SE = cable_shielding_effectiveness(100.0, 'braided')
    print(f"  Braided shield SE @ 100 MHz: {SE:.1f} dB")
    
    # 5. PIM
    print("\n--- 5. Passive Intermodulation ---")
    pim = pim_frequency(2110, 1930, n=3, m=3)
    print(f"  PIM products for f1=2110, f2=1930 MHz:")
    print(f"    2f1-f2 = {pim['f_pim_2f1_f2_MHz']:.0f} MHz, 2f2-f1 = {pim['f_pim_2f2_f1_MHz']:.0f} MHz")
    pim_pwr = pim_power_estimate(43, 43, IIP3_dBm=50)
    print(f"  PIM3 level: {pim_pwr['PIM3_dBc']:.1f} dBc ({pim_pwr['PIM3_dBm']:.1f} dBm)")
    
    # 6. RF compatibility
    print("\n--- 6. RF Compatibility ---")
    rf = rf_compatibility_check(f_signal_MHz=2140, signal_bw_kHz=5000, P_signal_dBm=-70,
                                 f_interferer_MHz=2150, P_interferer_dBm=-20,
                                 IIP3_dBm=30)
    print(f"  SIR @ 2150 MHz: {rf['signal_interferer_ratio_dB']:.1f} dB → {'PASS' if rf['pass'] else 'FAIL'}")
    
    # 7. HERP/HERF
    print("\n--- 7. HERP/HERF ---")
    herp = herp_hazard_range(100, 40, 3000)
    print(f"  Power density hazard dist: {herp['power_density_hazard_dist_m']:.1f} m")
    print(f"  H-field hazard dist: {herp['H_field_hazard_dist_m']:.1f} m")
    
    herf = herf_hazard_check(10, 30, 5.0, 3000)
    print(f"  HERF E-field @ 5m from 10W TX: {herf['E_field_V_m']:.1f} V/m → "
          f"{'HAZARD' if herf['hazard'] else 'SAFE'}")
    
    # Plot crosstalk vs frequency
    print("\n--- 8. Generating Figures ---")
    freqs = np.logspace(5, 8, 300)  # 100 kHz to 1 GHz
    NEXTs = []
    FEXTs = []
    for f in freqs:
        NEXT, FEXT = crosstalk_parallel_cable(l_coupling_m=1.0, s_mm=5.0,
                                                h_mm=10.0, d_both_mm=10.0, f=f)
        NEXTs.append(NEXT * 1000)
        FEXTs.append(FEXT * 1000)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.semilogx(freqs / 1e6, 20 * np.log10(np.array(NEXTs) + 1e-12),
                'b-', label='NEXT (mV)')
    ax.semilogx(freqs / 1e6, 20 * np.log10(np.array(FEXTs) + 1e-12),
                'r-', label='FEXT (mV)')
    ax.set_xlabel('Frequency (MHz)')
    ax.set_ylabel('Crosstalk Level (dB ref 1 mV)')
    ax.set_title('Cable Crosstalk vs Frequency (1 m parallel, 5 mm separation)')
    ax.legend()
    ax.grid(True, which='both', alpha=0.3)
    plt.tight_layout()
    out = '/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures/ch5_crosstalk_vs_freq.png'
    plt.savefig(out, dpi=150, bbox_inches='tight')
    print(f"Figure saved: {out}")
    plt.close()
    
    print("\n✓ Chapter 5 code complete.")
