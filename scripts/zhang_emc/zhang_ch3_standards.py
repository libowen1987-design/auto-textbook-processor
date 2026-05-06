#!/usr/bin/env python3
"""
Zhang EMC - Chapter 3: EMC Standards & Management
==================================================
Core topics from Zhang Ch3:
- MIL-STD-461E/F CE101/CS101/RE102/RS103 limits
- FCC Part 15 radiated emission limits (Class A/B)
- CISPR 22 / CISPR 11 conducted & radiated limits
- 6 dB EMC margin requirement
- EMC test program structure
- System-level vs. equipment-level test hierarchy

Ref: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Ch3
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0, pi
import warnings
warnings.filterwarnings('ignore')

# ══════════════════════════════════════════════════════════════════
# 1. MIL-STD-461E/F — Conducted Emission Limits
# ══════════════════════════════════════════════════════════════════

def mil_461_ce101_limit(f_hz):
    """
    MIL-STD-461E CE101: Conducted emissions, power leads, 30 Hz–10 kHz.
    Limit in dBμA.
    Two bands based on MIL-STD-461F Table V:
      30 Hz–1 kHz: flat at ~100 dBμA (varies with current)
      1 kHz–10 kHz: decreasing at -20 dB/decade
    For spacecraft: applies to 28V primary power bus.
    """
    f_khz = f_hz / 1e3
    if f_khz < 0.1:
        return 100.0
    elif f_khz < 1.0:
        # Slight slope from 0.1 to 1 kHz
        return 100.0 + 10.0 * np.log10(f_khz / 0.1)
    else:
        return 80.0 - 20.0 * np.log10(f_khz)


def mil_461_ce102_limit(f_hz):
    """
    MIL-STD-461E CE102: Conducted emissions, 10 kHz–10 MHz.
    Applies to power leads and interconnecting leads.
    Limit ≈ 60–48 dBμV (various levels), reference 1 µV = 0 dBμV.
    Simplified envelope: flat ~ 48–60 dBμV from 10 kHz to ~1 MHz,
    then -20 dB/dec above.
    """
    f_khz = f_hz / 1e3
    if f_khz < 10.0:
        return 60.0
    elif f_khz < 1000.0:
        return 60.0
    else:
        return 60.0 - 20.0 * np.log10(f_khz / 1000.0)


def mil_461_cs101_limit(f_hz):
    """
    MIL-STD-461E CS101: Conducted susceptibility, power leads, 30 Hz–150 kHz.
    Limit in dBμA (current injection threshold).
    """
    f_khz = f_hz / 1e3
    if f_khz < 1.0:
        return 110.0
    else:
        return 110.0 - 20.0 * np.log10(f_khz)


def mil_461_cs114_limit(f_hz):
    """
    MIL-STD-461E CS114: Conducted susceptibility, bulk cable injection, 10 kHz–200 MHz.
    Limit in dBμA (current injection level).
    Reference: typically 100 mA (40 dBμA) for class A equipment.
    """
    f_mhz = f_hz / 1e6
    if f_mhz < 0.01:
        return 100.0
    elif f_mhz < 30.0:
        return 100.0
    else:
        return 100.0


# ══════════════════════════════════════════════════════════════════
# 2. MIL-STD-461E/F — Radiated Emission Limits
# ══════════════════════════════════════════════════════════════════

def mil_461_re102_limit(f_hz):
    """
    MIL-STD-461E RE102: Radiated emissions, electric field, 10 kHz–18 GHz.
    Limit in dBμV/m at measurement distance (typically 1 m or 3 m for spacecraft).
    Envelope (from MIL-STD-461F Table 4):
      10 kHz–10 MHz: rises slowly
      10 MHz– 100 MHz: peaks ~80 dBμV/m
      100 MHz–1 GHz: decreasing, -20 dB/dec
      1–18 GHz: flat ~54–60 dBμV/m
    Simplified for plotting.
    """
    f_mhz = f_hz / 1e6
    if f_mhz < 0.01:
        return 80.0
    elif f_mhz < 10.0:
        # Rises to peak
        return 80.0 + 10.0 * np.log10(f_mhz / 0.01)
    elif f_mhz < 100.0:
        return 90.0
    elif f_mhz < 1000.0:
        return 90.0 - 30.0 * np.log10(f_mhz / 100.0)
    else:
        return 54.0


def mil_461_rs103_limit(f_hz):
    """
    MIL-STD-461E RS103: Radiated susceptibility, 2 MHz–40 GHz.
    E-field level in dBμV/m.
    Typical spacecraft requirement: 87–100 dBμV/m (≈ 1–10 mW/cm²).
    Returns threshold E-field in V/m.
    """
    # Typical: 200 μW/cm² = 2.8 V/m at 1 m (from MIL-STD-461F Table 9)
    P_density = 2e-4   # 200 μW/cm²
    eta0 = np.sqrt(mu_0 / epsilon_0)
    E_threshold = np.sqrt(P_density * 1e4 * 2.0 * eta0)
    return E_threshold


# ══════════════════════════════════════════════════════════════════
# 3. FCC Part 15 — Radiated Emission Limits
# ══════════════════════════════════════════════════════════════════

def fcc_part15_class_a_re(f_hz):
    """
    FCC Part 15 Class A: Radiated emissions for digital devices.
    Measurement at 3 m.
    30 MHz–88 MHz: 30 μV/m = 29.5 dBμV/m
    88–216 MHz: 50 μV/m = 34 dBμV/m
    216–960 MHz: 70 μV/m = 37 dBμV/m
    Above 960 MHz: 70 μV/m at 3 m
    """
    f_mhz = f_hz / 1e6
    if f_mhz < 30.0:
        return 0.0  # below measurement range
    elif f_mhz < 88.0:
        V_uV_m = 30.0
    elif f_mhz < 216.0:
        V_uV_m = 50.0
    elif f_mhz < 960.0:
        V_uV_m = 70.0
    else:
        V_uV_m = 70.0
    return 20.0 * np.log10(V_uV_m)  # dBμV/m


def fcc_part15_class_b_re(f_hz):
    """
    FCC Part 15 Class B: Radiated emissions (personal devices).
    Measurement at 3 m (more stringent than Class A).
    """
    f_mhz = f_hz / 1e6
    if f_mhz < 30.0:
        return 0.0
    elif f_mhz < 88.0:
        V_uV_m = 100.0 / 3.0 * 3.0   # placeholder scaling
        V_uV_m = 100.0
    elif f_mhz < 216.0:
        V_uV_m = 150.0
    elif f_mhz < 960.0:
        V_uV_m = 200.0
    else:
        V_uV_m = 200.0
    return 20.0 * np.log10(V_uV_m)  # dBμV/m


# ══════════════════════════════════════════════════════════════════
# 4. CISPR 11 / CISPR 22 — Conducted & Radiated Limits
# ══════════════════════════════════════════════════════════════════

def cispr_11_class_a_conducted(f_hz):
    """
    CISPR 11: Conducted emission limits for industrial, scientific equipment.
    Class A, 150 kHz–30 MHz.
    Limits in dBμV.
    At 150 kHz–500 kHz: ~60–50 dBμV quasi-peak
    At 500 kHz–5 MHz: decreasing at -20 dB/dec
    At 5–30 MHz: ~50 dBμV
    """
    f_khz = f_hz / 1e3
    if f_khz < 150.0:
        return 0.0
    elif f_khz < 500.0:
        return 60.0
    elif f_khz < 5000.0:
        return 60.0 - 20.0 * np.log10(f_khz / 500.0)
    else:
        return 50.0


def cispr_22_class_b_conducted(f_hz):
    """
    CISPR 22 Class B: Conducted limits for IT equipment, 150 kHz–30 MHz.
    More stringent than Class A.
    At 150–500 kHz: ~45–55 dBμV
    At 500 kHz–5 MHz: decreasing at -20 dB/dec
    At 5–30 MHz: ~45 dBμV
    """
    f_khz = f_hz / 1e3
    if f_khz < 150.0:
        return 0.0
    elif f_khz < 500.0:
        return 55.0 - 10.0 * np.log10(f_khz / 150.0)
    elif f_khz < 5000.0:
        return 55.0 - 20.0 * np.log10(f_khz / 500.0)
    else:
        return 45.0


def cispr_11_class_a_radiated(f_hz):
    """
    CISPR 11 Class A radiated E-field limits at 3 m.
    30–230 MHz: 30 dBμV/m (quasi-peak)
    230–1000 MHz: 37 dBμV/m
    Above 1 GHz: guideline (not mandatory)
    """
    f_mhz = f_hz / 1e6
    if f_mhz < 30.0:
        return 0.0
    elif f_mhz <= 230.0:
        return 30.0
    else:
        return 37.0


# ══════════════════════════════════════════════════════════════════
# 5. EMC MARGIN VERIFICATION
# ══════════════════════════════════════════════════════════════════

def emc_margin_check(emission_dB, susceptibility_limit_dB, required_margin=6.0):
    """
    Standard EMC margin check: margin = susceptibility_limit - emission_level.
    Positive margin >= required_margin (typically 6 dB) = compliant.
    """
    margin = susceptibility_limit_dB - emission_dB
    return {
        'emission_dB': emission_dB,
        'susceptibility_limit_dB': susceptibility_limit_dB,
        'margin_dB': margin,
        'required_margin_dB': required_margin,
        'pass': margin >= required_margin,
    }


def emc_coupling_path_loss(S21_dB, frequency):
    """
    Coupling path loss from S21. Used in system-level EMI budget.
    S21_dB: coupling in dB (negative for attenuation)
    Returns coupling loss in dB.
    """
    return S21_dB  # more negative = more isolation


def emi_budget_analysis(emission_source_dBuV, coupling_path_loss_dB,
                         shielded_enclosure_dB, margin_required=6.0):
    """
    EMI budget: check if design meets margin requirement.
    emission_source: emission at source (dBμV or dBμA)
    coupling_path_loss: isolation between source and victim (dB, positive = loss)
    shielded_enclosure: additional shielding (dB)
    """
    received_level = emission_source_dBuV - coupling_path_loss_dB - shielded_enclosure_dB
    susceptibility_threshold = received_level + margin_required
    # If susceptibility_threshold is achievable → pass
    return {
        'received_level_dBuV': received_level,
        'margin_required_dB': margin_required,
        'shielded_contribution_dB': shielded_enclosure_dB,
    }


# ══════════════════════════════════════════════════════════════════
# 6. EMC TEST HIERARCHY — Equipment / Subsystem / System
# ══════════════════════════════════════════════════════════════════

TEST_HIERARCHY = {
    'Equipment-level': {
        'description': 'Individual equipment tested per MIL-STD-461 / CISPR standards',
        'emission_tests': ['CE101', 'CE102', 'RE102'],
        'susceptibility_tests': ['CS101', 'CS114', 'CS115', 'CS116', 'RS103'],
        'applicable_standards': ['MIL-STD-461E', 'MIL-STD-461F', 'CISPR 11', 'CISPR 22'],
    },
    'Subsystem-level': {
        'description': 'Multiple equipment integrated; tests focus on coupling paths',
        'emission_tests': ['CE (combined)', 'RE (combined)'],
        'susceptibility_tests': ['CS (bulk cable)', 'RS (inter-system)'],
        'applicable_standards': ['MIL-STD-461', 'DEF-STAN 59-411'],
    },
    'System-level': {
        'description': 'Full spacecraft tested; verifies EME compatibility',
        'emission_tests': ['RE (full system)', 'CE (power bus)'],
        'susceptibility_tests': ['RS (worst-case EME envelope)'],
        'applicable_standards': ['MIL-STD-461', 'ECSS-E-ST-20-07'],
    },
}


def test_level_applicability(spacecraft_class='medium'):
    """
    Determine applicable test levels based on spacecraft scale.
    Returns dict of relevant tests per level.
    """
    if spacecraft_class == 'large':
        return TEST_HIERARCHY
    elif spacecraft_class == 'medium':
        return {
            'Equipment-level': TEST_HIERARCHY['Equipment-level'],
            'Subsystem-level': TEST_HIERARCHY['Subsystem-level'],
        }
    else:  # small
        return {'Equipment-level': TEST_HIERARCHY['Equipment-level']}


# ══════════════════════════════════════════════════════════════════
# 7. FREQUENCY PLANNING — ITU / Spacecraft Spectrum Management
# ══════════════════════════════════════════════════════════════════

def frequency_band_allocation_designation(f_hz):
    """
    Identify ITU frequency band designation.
    e.g. VLF = 3–30 kHz, HF = 3–30 MHz, VHF = 30–300 MHz, etc.
    """
    if f_hz < 3e4:
        return 'VLF'
    elif f_hz < 3e5:
        return 'LF'
    elif f_hz < 3e6:
        return 'MF'
    elif f_hz < 3e7:
        return 'HF'
    elif f_hz < 3e8:
        return 'VHF'
    elif f_hz < 3e9:
        return 'UHF'
    elif f_hz < 3e10:
        return 'SHF'
    else:
        return 'EHF'


def intermodulation_product_frequencies(f1, f2, n=2, m=1):
    """
    PIM (Passive InterModulation) product: f_PIM = |n·f1 ± m·f2|
    n, m are integers (typically 1 or 2 for 2nd/3rd order products).
    Returns list of PIM frequencies.
    """
    products = []
    for ni in range(1, n + 1):
        for mi in range(0, m + 1):
            if ni == 0 and mi == 0:
                continue
            products.append(abs(ni * f1 - mi * f2))
            if ni != mi:  # also sum product
                products.append(ni * f1 + mi * f2)
    return sorted(set(products))


def PIM_risk_assessment(f_transmit_dbm, f_receive_mhz, PIM_order=3):
    """
    Simple PIM risk: check if transmit frequency causes PIM products in receive band.
    Returns True if PIM risk exists.
    """
    # For demonstration: 3rd order PIM = 2*f1 - f2 or 2*f2 - f1
    f1 = 14.4e9   # example: 14.4 GHz transponder transmit
    f2 = f_receive_mhz * 1e6
    products = intermodulation_product_frequencies(f1, f2, n=PIM_order, m=PIM_order)
    # Check if any product falls near receive band (e.g. 12–12.5 GHz for receive)
    rx_low, rx_high = 12.0e9, 12.5e9
    risks = [p for p in products if rx_low <= p <= rx_high]
    return len(risks) > 0, products


# ══════════════════════════════════════════════════════════════════
# NUMERICAL EXAMPLES
# ══════════════════════════════════════════════════════════════════

def example_1_mil_461_ce101_margin():
    """Example 1: CE101 conducted emission margin for 28 V power bus."""
    print("\n" + "="*60)
    print("EXAMPLE 1 — MIL-STD-461E CE101 Conducted Emission Margin")
    print("="*60)
    test_frequencies_khz = [1, 5, 10, 50, 100, 500]
    emission_levels_dBuA = {
        'SMPS (switching)': [75, 74, 73, 72, 71, 68],
        'Linear PSU':       [40, 41, 42, 43, 44, 45],
        'Motor drive':      [82, 81, 79, 77, 75, 70],
    }
    print(f"  {'Freq(kHz)':>10} | {'Limit(dBμA)':>12} | {'SMPS':>8} | {'Linear':>8} | {'Motor':>8}")
    print("  " + "-"*58)
    for i, f_khz in enumerate(test_frequencies_khz):
        f_hz = f_khz * 1e3
        limit = mil_461_ce101_limit(f_hz)
        smps = emission_levels_dBuA['SMPS (switching)'][i]
        lin  = emission_levels_dBuA['Linear PSU'][i]
        moto = emission_levels_dBuA['Motor drive'][i]
        smps_m = limit - smps
        lin_m  = limit - lin
        moto_m = limit - moto
        smps_ok = '✓' if smps_m >= 6.0 else '✗'
        lin_ok  = '✓' if lin_m  >= 6.0 else '✗'
        moto_ok = '✓' if moto_m >= 6.0 else '✗'
        print(f"  {f_khz:>10.0f} | {limit:>12.1f} | {smps:>6.1f}{smps_ok} | {lin:>6.1f}{lin_ok} | {moto:>6.1f}{moto_ok}")


def example_2_mil_461_re102_check():
    """Example 2: RE102 radiated emission vs. limit at key frequencies."""
    print("\n" + "="*60)
    print("EXAMPLE 2 — MIL-STD-461E RE102 Radiated Emission vs. Limit")
    print("="*60)
    frequencies_mhz = [1, 10, 30, 100, 300, 1000]
    equipment_levels_dBuVm = {
        'Digital electronics (clock harmonics)': [78, 82, 75, 65, 58, 50],
        'Switching power supply':               [80, 85, 78, 70, 62, 55],
        'RF front-end (spurious)':             [60, 55, 50, 45, 40, 35],
    }
    print(f"  {'Freq(MHz)':>10} | {'Limit':>8} | {'Digital':>12} | {'SMPS':>12} | {'RF':>12}")
    print("  " + "-"*60)
    for i, f_mhz in enumerate(frequencies_mhz):
        f_hz = f_mhz * 1e6
        limit = mil_461_re102_limit(f_hz)
        dig  = equipment_levels_dBuVm['Digital electronics (clock harmonics)'][i]
        smps = equipment_levels_dBuVm['Switching power supply'][i]
        rf   = equipment_levels_dBuVm['RF front-end (spurious)'][i]
        dig_m  = limit - dig
        smps_m = limit - smps
        rf_m   = limit - rf
        dig_s  = '✓' if dig_m  >= 6.0 else '✗'
        smps_s = '✓' if smps_m >= 6.0 else '✗'
        rf_s   = '✓' if rf_m   >= 6.0 else '✗'
        print(f"  {f_mhz:>10.0f} | {limit:>8.1f} | {dig:>10.1f}{dig_s:2s} | {smps:>10.1f}{smps_s:2s} | {rf:>10.1f}{rf_s:2s}")


def example_3_fcc_vs_mil_compare():
    """Example 3: Compare FCC Part 15 Class B vs. MIL-STD-461 RE102 limits."""
    print("\n" + "="*60)
    print("EXAMPLE 3 — FCC Part 15 Class B vs. MIL-STD-461 RE102 Limits")
    print("="*60)
    freqs_mhz = [30, 100, 200, 500, 1000]
    print(f"  {'Freq(MHz)':>10} | {'FCC-ClassB':>12} | {'MIL-RE102':>12} | {'Diff (FCC-MIL)':>14}")
    print("  " + "-"*55)
    for f_mhz in freqs_mhz:
        f_hz = f_mhz * 1e6
        fcc  = fcc_part15_class_b_re(f_hz)
        mil  = mil_461_re102_limit(f_hz)
        diff = fcc - mil
        print(f"  {f_mhz:>10.0f} | {fcc:>12.1f} | {mil:>12.1f} | {diff:>+14.1f} dB")


def example_4_cispr_conducted_analysis():
    """Example 4: CISPR 22 Class B conducted emission compliance check."""
    print("\n" + "="*60)
    print("EXAMPLE 4 — CISPR 22 Class B Conducted Emission Compliance")
    print("="*60)
    freqs_khz = [150, 500, 1000, 5000, 10000, 20000]
    measured_dBuV = [52, 48, 44, 40, 38, 35]
    print(f"  {'Freq(kHz)':>10} | {'Limit(dBμV)':>12} | {'Measured':>10} | {'Margin':>8} | {'Status':>6}")
    print("  " + "-"*55)
    for f_khz, meas in zip(freqs_khz, measured_dBuV):
        limit = cispr_22_class_b_conducted(f_khz * 1e3)
        margin = limit - meas
        status = '✓' if margin >= 6.0 else '✗'
        print(f"  {f_khz:>10.0f} | {limit:>12.1f} | {meas:>10.1f} | {margin:>+8.1f} | {status}")


def example_5_RS103_susceptibility_threshold():
    """Example 5: RS103 radiated susceptibility threshold calculation."""
    print("\n" + "="*60)
    print("EXAMPLE 5 — MIL-STD-461E RS103 Susceptibility Threshold")
    print("="*60)
    # RS103 typically: 87 dBμV/m = 22.4 mV/m at 1 m
    # Or 200 μW/cm² = 1.4 V/m (from MIL-STD-461F Table 9)
    power_densities = [1e-4, 5e-4, 1e-3, 5e-3]  # W/m²
    eta0 = np.sqrt(mu_0 / epsilon_0)
    print(f"  {'P_dens(W/m²)':>14} | {'E_threshold(V/m)':>18} | {'E_dBuV/m@1m':>14}")
    print("  " + "-"*50)
    for P in power_densities:
        E = np.sqrt(P * 2.0 * eta0)
        E_dBuV_m = 20.0 * np.log10(E / 1e-6)
        print(f"  {P:>14.1e} | {E:>18.6f} | {E_dBuV_m:>14.1f}")
    # Compare with MIL limit (typically 87 dBμV/m = 22.4 mV/m)
    E_limit = np.sqrt(1e-4 * 2.0 * eta0)  # 100 μW/cm²
    print(f"\n  Typical MIL-STD-461E RS103 threshold: {20*np.log10(E_limit/1e-6):.1f} dBμV/m")


def example_6_emc_margin_summary():
    """Example 6: System-level EMC margin summary table."""
    print("\n" + "="*60)
    print("EXAMPLE 6 — System EMC Margin Summary (6 dB required)")
    print("="*60)
    interfaces = [
        {'name': 'Primary power bus',      'emission': 75.0, 'limit': 80.0},
        {'name': 'Attitude control data',  'emission': 50.0, 'limit': 58.0},
        {'name': 'Telemetry downlink',     'emission': 60.0, 'limit': 68.0},
        {'name': 'Payload sensor data',    'emission': 45.0, 'limit': 55.0},
        {'name': 'RF transmitter (spurious)', 'emission': 55.0, 'limit': 65.0},
    ]
    print(f"  {'Interface':30s} | {'Emission':>10} | {'Limit':>8} | {'Margin':>8} | {'Pass':>4}")
    print("  " + "-"*70)
    for iface in interfaces:
        margin = iface['limit'] - iface['emission']
        status = '✓' if margin >= 6.0 else '✗'
        print(f"  {iface['name']:30s} | {iface['emission']:>10.1f} | {iface['limit']:>8.1f} | {margin:>+8.1f} | {status}")


def example_7_pim_risk_check():
    """Example 7: Passive Intermodulation risk in S-band transponder."""
    print("\n" + "="*60)
    print("EXAMPLE 7 — Passive Intermodulation (PIM) Risk Assessment")
    print("="*60)
    f_transmit_ghz = 14.4   # S-band transmit frequency (GHz)
    f_transmit = f_transmit_ghz * 1e9
    f_receive_ghz = 12.5    # S-band receive frequency (GHz)
    f_receive = f_receive_ghz * 1e9

    for order in [2, 3]:
        risk, prods = PIM_risk_assessment(40.0, f_receive_ghz, PIM_order=order)
        print(f"  Order {order} PIM products near Rx band ({f_receive_ghz:.2f} GHz):")
        rx_low, rx_high = 12.0e9, 12.5e9
        rx_prods = [p for p in prods if rx_low <= p <= rx_high]
        if rx_prods:
            for pf in rx_prods:
                print(f"    ⚠  PIM product at {pf/1e9:.4f} GHz falls in receive band!")
        else:
            print(f"    ✓ No {order}nd-order PIM products in Rx band.")


# ══════════════════════════════════════════════════════════════════
# FIGURE 1 — MIL-STD-461E CE101 / CE102 Conducted Emission Limits
# ══════════════════════════════════════════════════════════════════

def plot_mil_conducted_limits():
    """
    Plot MIL-STD-461E CE101 and CE102 conducted emission limits.
    CE101: 30 Hz–10 kHz power leads
    CE102: 10 kHz–10 MHz power leads
    """
    f_ce101 = np.logspace(1, 4, 300)   # 10 Hz to 10 kHz
    f_ce102 = np.logspace(4, 7, 300)   # 10 kHz to 10 MHz
    limit_ce101 = np.array([mil_461_ce101_limit(f) for f in f_ce101])
    limit_ce102 = np.array([mil_461_ce102_limit(f) for f in f_ce102])

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.semilogx(f_ce101, limit_ce101, color='C0', linewidth=2.5,
                label='CE101 (30 Hz–10 kHz, power leads)')
    ax.semilogx(f_ce102, limit_ce102, color='C1', linewidth=2.5,
                label='CE102 (10 kHz–10 MHz, power leads)')

    ax.set_xlabel('Frequency (Hz)', fontsize=12)
    ax.set_ylabel('Conducted Emission Limit (dBμA)', fontsize=12)
    ax.set_title(
        'MIL-STD-461E Conducted Emission Limits\n'
        '(Zhang Ch3 — CE101 & CE102 for Spacecraft Power Bus)',
        fontsize=13, fontweight='bold'
    )
    ax.legend(fontsize=10)
    ax.grid(True, which='both', alpha=0.3)
    ax.set_xlim(1e1, 1e7)
    ax.set_ylim(0, 120)

    # Annotations
    ax.axvline(1e3, color='gray', linestyle=':', alpha=0.5)
    ax.text(1.2e3, 105, 'CE101/102 boundary\n1 kHz', fontsize=8, color='gray')

    plt.tight_layout()
    out_path = '/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures/ch3_mil_conducted_limits.png'
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"[FIGURE] ch3_mil_conducted_limits.png saved.")
    return out_path


# ══════════════════════════════════════════════════════════════════
# FIGURE 2 — MIL-STD-461E RE102 Radiated Emission Limits
# ══════════════════════════════════════════════════════════════════

def plot_mil_radiated_limits():
    """
    Plot MIL-STD-461E RE102 radiated emission limit curve.
    Also overlay FCC Part 15 Class A & B for comparison.
    """
    f_range = np.logspace(4, 10, 500)   # 10 kHz to 10 GHz
    mil_limit = np.array([mil_461_re102_limit(f) for f in f_range])
    fcc_a    = np.array([fcc_part15_class_a_re(f) for f in f_range])
    fcc_b    = np.array([fcc_part15_class_b_re(f) for f in f_range])
    cispr_a  = np.array([cispr_11_class_a_radiated(f) for f in f_range])

    fig, ax = plt.subplots(figsize=(12, 7))

    ax.semilogx(f_range, mil_limit, color='C0', linewidth=2.5,
                label='MIL-STD-461E RE102 (spacecraft)')
    ax.semilogx(f_range, fcc_a, color='C1', linewidth=1.8, linestyle='--',
                label='FCC Part 15 Class A (industrial)')
    ax.semilogx(f_range, fcc_b, color='C2', linewidth=1.8, linestyle=':',
                label='FCC Part 15 Class B (consumer)')
    ax.semilogx(f_range, cispr_a, color='C3', linewidth=1.8, linestyle='-.',
                label='CISPR 11 Class A (industrial)')

    ax.set_xlabel('Frequency (Hz)', fontsize=12)
    ax.set_ylabel('Radiated E-field Limit (dBμV/m)', fontsize=12)
    ax.set_title(
        'Radiated Emission Limit Comparison: MIL-STD-461E / FCC / CISPR\n'
        '(Zhang Ch3 — EMC Standards for Spacecraft and Ground Equipment)',
        fontsize=13, fontweight='bold'
    )
    ax.legend(fontsize=10)
    ax.grid(True, which='both', alpha=0.3)
    ax.set_xlim(1e4, 1e10)
    ax.set_ylim(0, 120)

    # Mark key bands
    for f_mark, label in [(90e6, 'VHF'), (230e6, 'UHF'), (1e9, 'L')]:
        ax.axvline(f_mark, color='gray', linestyle=':', alpha=0.4)
        ax.text(f_mark * 1.1, 5, label, fontsize=8, color='gray')

    plt.tight_layout()
    out_path = '/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures/ch3_mil_radiated_limits.png'
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"[FIGURE] ch3_mil_radiated_limits.png saved.")
    return out_path


# ══════════════════════════════════════════════════════════════════
# FIGURE 3 — CISPR 22 Class B Conducted Emission Limits (150 kHz–30 MHz)
# ══════════════════════════════════════════════════════════════════

def plot_cispr_conducted_limits():
    """
    Plot CISPR 22 Class B conducted emission limit curve.
    Show quasi-peak and average limits.
    """
    f_range = np.logspace(5, 7.5, 400)   # 100 kHz to 30 MHz
    qp_limit = np.array([cispr_22_class_b_conducted(f) for f in f_range])
    avg_limit = qp_limit - 10.0  # average limit typically 10 dB below QP

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.semilogx(f_range, qp_limit, color='C0', linewidth=2.5,
                label='CISPR 22 Class B (quasi-peak)')
    ax.semilogx(f_range, avg_limit, color='C1', linewidth=2.0, linestyle='--',
                label='CISPR 22 Class B (average)')

    ax.set_xlabel('Frequency (Hz)', fontsize=12)
    ax.set_ylabel('Conducted Emission Limit (dBμV)', fontsize=12)
    ax.set_title(
        'CISPR 22 Class B Conducted Emission Limits (150 kHz–30 MHz)\n'
        '(Zhang Ch3 — IT Equipment Standards)',
        fontsize=13, fontweight='bold'
    )
    ax.legend(fontsize=10)
    ax.grid(True, which='both', alpha=0.3)
    ax.set_xlim(1e5, 3e7)
    ax.set_ylim(20, 70)
    ax.axvline(0.5e6, color='gray', linestyle=':', alpha=0.5)
    ax.text(0.6e6, 65, '500 kHz', fontsize=8, color='gray')

    plt.tight_layout()
    out_path = '/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures/ch3_cispr_conducted_limits.png'
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"[FIGURE] ch3_cispr_conducted_limits.png saved.")
    return out_path


# ══════════════════════════════════════════════════════════════════
# FIGURE 4 — EMC Test Hierarchy and Margin Requirements
# ══════════════════════════════════════════════════════════════════

def plot_emc_test_hierarchy():
    """
    Visualise EMC test hierarchy: equipment → subsystem → system.
    Show typical test items and limits at each level.
    """
    levels = ['Equipment\nLevel', 'Subsystem\nLevel', 'System\nLevel']
    emission_items  = ['CE101, CE102, RE102', 'Combined CE/RE', 'Full RE + CE (bus)']
    suscept_items   = ['CS101, CS114, RS103', 'CS bulk cable, RS', 'RS (worst-case EME)']
    n_tests         = [8, 5, 3]

    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    colors = ['C0', 'C1', 'C2']
    titles = ['Emission Tests', 'Susceptibility Tests', 'Typical # Test Items']
    data = [emission_items, suscept_items, n_tests]

    for i, (ax, title, col) in enumerate(zip(axes, titles, colors)):
        if i < 2:
            for j, (item, color) in enumerate(zip(data[i], colors)):
                ax.text(0.05, 1.0 - j * 0.4, f'• {item}', fontsize=10,
                        transform=ax.transAxes, color=color, fontweight='bold' if j == 0 else 'normal')
        else:
            bars = ax.bar(levels, data[i], color=colors, alpha=0.7, width=0.6)
            for bar, val in zip(bars, data[i]):
                ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
                        str(val), ha='center', va='bottom', fontsize=14, fontweight='bold')
        ax.set_title(title, fontsize=12, fontweight='bold')
        ax.set_ylim(0, 12 if i < 2 else 10)
        ax.set_xticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    axes[0].set_ylabel('Test Item', fontsize=11)
    axes[2].set_ylabel('Count', fontsize=11)

    fig.suptitle(
        'EMC Test Hierarchy: Equipment → Subsystem → System\n'
        '(Zhang Ch3 — MIL-STD-461 Test Programme Structure)',
        fontsize=13, fontweight='bold', y=1.02
    )
    plt.tight_layout()
    out_path = '/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures/ch3_emc_test_hierarchy.png'
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"[FIGURE] ch3_emc_test_hierarchy.png saved.")
    return out_path


# ──────────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("="*60)
    print("Zhang EMC — Chapter 3: EMC Standards & Management")
    print("Spacecraft Electromagnetic Compatibility Technologies (2020)")
    print("="*60)

    example_1_mil_461_ce101_margin()
    example_2_mil_461_re102_check()
    example_3_fcc_vs_mil_compare()
    example_4_cispr_conducted_analysis()
    example_5_RS103_susceptibility_threshold()
    example_6_emc_margin_summary()
    example_7_pim_risk_check()

    print("\n" + "="*60)
    print("Generating figures...")
    print("="*60)
    plot_mil_conducted_limits()
    plot_mil_radiated_limits()
    plot_cispr_conducted_limits()
    plot_emc_test_hierarchy()
    print("\nAll tasks complete.")