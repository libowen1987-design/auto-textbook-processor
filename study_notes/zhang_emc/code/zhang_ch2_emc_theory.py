#!/usr/bin/env python3
"""
Zhang EMC - Chapter 2: EMI Interface Control Methods
=====================================================
Core topics from Zhang Ch2:
- Electrical bonding classes: C / H / R / S (per NASA-STD-4003A)
- Bonding resistance requirements (0.1 mΩ to 1 Ω depending on class)
- Grounding modes: SPG, MPG, hybrid grounding
- Cable EMC classification (Cat I–V, per MIL-HDBK-83575)
- Conducted emission / susceptibility analysis
- Radiated coupling and crosstalk
- Shielding effectiveness (absorption + reflection)
- Ground loop analysis

Ref: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Ch2
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0, pi
import warnings
warnings.filterwarnings('ignore')

# ══════════════════════════════════════════════════════════════════
# 1. ELECTRICAL BONDING — Resistance & Impedance
# ══════════════════════════════════════════════════════════════════

# Bonding class parameters (NASA-STD-4003A)
BOND_CLASS = {
    'ClassC': {
        'purpose': 'Current return path (reduce power & voltage losses)',
        'DC_resistance_mohm': 0.1,       # < 0.1 mΩ
        'inductance': 'low',
        'frequency': 'low',
        'current': 'high',
    },
    'ClassH': {
        'purpose': 'Electric shock hazard / fault protection',
        'DC_resistance_mohm': 2.5,       # < 2.5 mΩ
        'inductance': 'low',
        'frequency': 'low',
        'current': 'high',
    },
    'ClassR': {
        'purpose': 'RF equipment bonding / EMI suppression',
        'DC_resistance_mohm': 2.5,       # < 2.5 mΩ
        'inductance': 'moderate',
        'frequency': 'high',
        'current': 'low',
    },
    'ClassS': {
        'purpose': 'Electrostatic discharge (ESD) control',
        'DC_resistance_mohm': 1000.0,   # < 1 Ω = 1000 mΩ
        'inductance': 'low',
        'frequency': 'low',
        'current': 'low',
    },
}


def bonding_resistance_check(R_measured_mohm, bond_class):
    """
    Verify bonding resistance compliance for given class.
    R_measured_mohm: measured DC bonding resistance in milliohms
    bond_class     : 'ClassC', 'ClassH', 'ClassR', or 'ClassS'
    Returns dict with pass/fail and margin.
    """
    limit = BOND_CLASS[bond_class]['DC_resistance_mohm']
    margin_mohm = limit - R_measured_mohm
    return {
        'measured_mohm': R_measured_mohm,
        'limit_mohm': limit,
        'margin_mohm': margin_mohm,
        'pass': R_measured_mohm <= limit,
        'class': bond_class,
        'purpose': BOND_CLASS[bond_class]['purpose'],
    }


def bonding_jumper_impedance(f, L_jumper, w=5e-3, t=1e-3):
    """
    Inductance of a flat bonding jumper strap.
    L_jumper: length (m)
    w       : width (m)
    t       : thickness (m)
    Returns L_jumper in nH.
    L ≈ 2e-7 * l * [ln(2l/(w+t)) + 0.5 + (w+t)/(3l)]  (per MIL-HDBK-1857)
    """
    # Simplified: L ≈ 2e-7 * l * (ln(2l/w) + 0.5)
    term = np.log(2.0 * L_jumper / (w + t)) + 0.5
    L_self = 2e-7 * L_jumper * term
    return L_self


def bonding_jumper_aspect_ratio(L_jumper, w):
    """
    Aspect ratio = L / w. Class R requirement: L/w ≤ 5 (per NASA-STD-4003A).
    """
    return L_jumper / w


# ══════════════════════════════════════════════════════════════════
# 2. GROUNDING MODES — SPG, MPG, Hybrid
# ══════════════════════════════════════════════════════════════════

def ground_impedance_SPG(f, Z_gnd_trace):
    """
    Single-point grounding: impedance grows with frequency
    due to trace inductance. Z_total = Z_DC + jωL.
    f          : frequency (Hz)
    Z_gnd_trace: trace impedance at low freq (ohms)
    Returns total impedance magnitude in ohms.
    """
    L_trace = Z_gnd_trace / (2.0 * pi * 100.0)  # assume reference @ 100 Hz
    Z_total = np.sqrt(Z_gnd_trace**2 + (2.0 * pi * f * L_trace)**2)
    return Z_total


def ground_impedance_MPG(f, Z_gnd_trace, n_parallel=4):
    """
    Multi-point grounding: each parallel path reduces effective inductance.
    L_eff = L_single / n_parallel
    n_parallel : number of ground points
    """
    L_single = Z_gnd_trace / (2.0 * pi * 100.0)
    L_eff = L_single / n_parallel
    Z_total = np.sqrt(Z_gnd_trace**2 + (2.0 * pi * f * L_eff)**2)
    return Z_total


def ground_loop_current(V_diff, Z_loop):
    """
    Ground loop current: I_loop = V_diff / Z_loop.
    V_diff   : voltage difference between two ground references (V)
    Z_loop   : loop impedance (ohms)
    Returns current in amperes.
    """
    return V_diff / Z_loop


def hybrid_grounding_cutoff(f_LF_limit=1e5, f_HF_start=10e6):
    """
    Hybrid grounding: SPG below f_LF_limit, MPG above f_HF_start.
    Returns recommended ground mode for a given frequency.
    """
    def mode(f):
        if f < f_LF_limit:
            return 'SPG (single-point)'
        elif f > f_HF_start:
            return 'MPG (multi-point)'
        else:
            return 'Hybrid (SPG+MPG transition band)'
    return mode


# ══════════════════════════════════════════════════════════════════
# 3. CABLE EMC CLASSIFICATION & SHIELDING
# ══════════════════════════════════════════════════════════════════

CABLE_CATEGORY = {
    'CatI': {
        'description': 'High-power, high-voltage circuits',
        'V_DC': '>10V', 'f_AC': '<100 kHz',
        'shielding': 'twisted pairs + braid shield',
        'bundle_shield': True,
    },
    'CatII': {
        'description': 'Medium-level digital/analog signals',
        'V_DC': '5–25V', 'f_AC': '100 kHz–1 MHz',
        'shielding': 'twisted pairs + individual shield',
        'bundle_shield': True,
    },
    'CatIII': {
        'description': 'Low-level sensitive signals',
        'V_DC': '<10V', 'I': '<5A',
        'shielding': 'twisted pairs + bulk shield',
        'bundle_shield': True,
    },
    'CatIV': {
        'description': 'EED (electro-explosive device) circuits',
        'V_DC': 'any', 'I': 'ignition current',
        'shielding': 'twisted pairs + individual shield',
        'bundle_shield': True,
    },
    'CatV': {
        'description': 'Strong HF / RF signals, f > 1 MHz',
        'f_AC': '>1 MHz',
        'shielding': 'coaxial or balanced shielded, Z ≤ 50Ω',
        'bundle_shield': False,
    },
}


def cable_category_from_params(V_DC, I_load, f_AC, pulse_Vmax=None):
    """
    Classify cable category based on signal parameters.
    Returns cat string.
    """
    if pulse_Vmax is not None and pulse_Vmax > 25.0:
        return 'CatI'
    if V_DC > 10.0:
        return 'CatI'
    if f_AC < 100e3 and V_DC >= 5.0:
        return 'CatI'
    if f_AC < 100e3 and V_DC < 10.0 and I_load < 5.0:
        return 'CatIII'
    if f_AC > 1e6 or pulse_Vmax is not None:
        return 'CatV'
    return 'CatII'


def shielding_effectiveness_m编织(S_coverage, f, t_shield, sigma_shield):
    """
    Approximate braided shield SE using transfer impedance.
    S_coverage : braid coverage (%) e.g. 90%
    f          : frequency (Hz)
    t_shield   : shield thickness (m)
    sigma_shield: conductivity (S/m)

    Transfer impedance Z_t ≈ R_s * (1 - S_coverage/100) + jωL_m
    where R_s = 1/(σ·t·skin_per_nibble) ...
    Simplified model: SE ≈ 20*log10(1/Z_t) dB.
    """
    mu = mu_0
    delta = np.sqrt(1.0 / (pi * f * mu * sigma_shield))
    # Aperture term (coverage loss)
    alpha_aperture = 1.0 - S_coverage / 100.0  # fraction of open area
    # Transfer impedance approximation (Ohm/m)
    R_s = 1.0 / (sigma_shield * t_shield * delta)
    L_m = mu * delta / (2.0 * pi)
    Z_t = np.sqrt(R_s**2 + (2.0 * pi * f * L_m)**2)
    # SE from transfer impedance (simplified, for 1 m run)
    SE_linear = 1.0 / (Z_t + 1e-12)
    SE_dB = 20.0 * np.log10(SE_linear)
    return SE_dB


# ══════════════════════════════════════════════════════════════════
# 4. CONDUCTED EMISSION / SUSCEPTIBILITY ANALYSIS
# ══════════════════════════════════════════════════════════════════

def ce_limit_mil_461(f_hz):
    """
    MIL-STD-461E CE101 conducted emission limit for power leads (30 Hz–10 kHz).
    Approximate envelope values (from MIL-STD-461F Table V).
    Returns limit in dBμA.
    """
    f_khz = f_hz / 1e3
    if f_khz < 0.1:
        return 100.0   # ~100 dBμA
    elif f_khz < 1.0:
        return 100.0 - 20.0 * np.log10(f_khz / 0.1)
    else:
        return 80.0 - 20.0 * np.log10(f_khz)


def cs_limit_mil_461(f_hz):
    """
    MIL-STD-461E CS101 conducted susceptibility limit (30 Hz–150 kHz).
    Returns susceptibility threshold in dBμA.
    """
    f_khz = f_hz / 1e3
    if f_khz < 1.0:
        return 110.0   # high limit at very low freq
    else:
        return 110.0 - 20.0 * np.log10(f_khz)


def conducted_emi_margin(emission_dBuA, f_hz):
    """
    Conducted EMI margin vs. MIL-STD-461 limit.
    """
    limit = ce_limit_mil_461(f_hz)
    margin = limit - emission_dBuA
    return margin, limit


def impedance_power_bus(Z_source, Z_load, Z_filter=None):
    """
    Insertion loss of a filter on power bus.
    Returns voltage transfer ratio |V_load/V_source| and insertion loss dB.
    """
    if Z_filter is None:
        Z_filter = 0.0
    Z_total = Z_source + Z_load + Z_filter
    H = Z_load / Z_total
    return np.abs(H), -20.0 * np.log10(np.abs(H) + 1e-12)


# ══════════════════════════════════════════════════════════════════
# 5. RADIATED COUPLING & CROSSTALK
# ══════════════════════════════════════════════════════════════════

def mutual_inductance_parallel_cables(l_coupling, d_sep, r_wire=1e-3):
    """
    Mutual inductance between two parallel conductors (long coupling length).
    M = (μ0 / 2π) · l · [ln(d/r) + 1]   [H]
    l_coupling: coupling length (m)
    d_sep     : separation between conductors (m)
    r_wire    : wire radius (m)
    """
    return (mu_0 / (2.0 * pi)) * l_coupling * (np.log(d_sep / r_wire) + 1.0)


def crosstalk_voltage_Victim(V_aggressor, f, M, Z_victim):
    """
    Inductive crosstalk coupling.
    V_crosstalk = 2π · f · M · I_aggressor
    I_aggressor = V_aggressor / Z_source (assumed 50Ω typical)
    """
    I_agg = V_aggressor / 50.0  # assume 50Ω aggressor source
    V_ct = 2.0 * pi * f * M * I_agg
    return V_ct


def electric_field_coupling(E_interference, h_coupling, l_coupling):
    """
    Electric field coupling to a cable segment.
    V_coupled ≈ E · h_coupling · (l_coupling / λ)  (electrically short)
    h_coupling: cable height above ground plane (m)
    l_coupling: exposed cable length (m)
    λ         : wavelength (m)
    """
    lam = c / 1e9  # placeholder frequency at 1 GHz; pass frequency
    return E_interference * h_coupling * (l_coupling / lam)


def radiated_coupling_NF_to_ff(R_sensitivity_dBuV, f, d_distance_m, E_interference):
    """
    Near-field to far-field radiated coupling.
    R_sensitivity: equipment susceptibility threshold (dBμV/m at 1 m)
    Returns field strength at equipment and margin.
    """
    # Far-field: E ∝ 1/r (inverse distance)
    E_at_equipment = E_interference * (1.0 / (d_distance_m + 1e-9))
    E_dBuV_m = 20.0 * np.log10(E_at_equipment / 1e-6)
    margin = R_sensitivity_dBuV - E_dBuV_m
    return E_dBuV_m, margin


# ══════════════════════════════════════════════════════════════════
# 6. SHIELDING EFFECTIVENESS — Full SE Model
# ══════════════════════════════════════════════════════════════════

def SE_reflection_loss(sigma, mu_r, f):
    """
    Reflection loss for plane wave on thick conductive shield.
    R_dB ≈ 168 + 10·log10(σ_r·μ_r/f_r)  [dB]
    sigma: conductivity (S/m)
    mu_r : relative permeability
    f    : frequency (Hz)
    """
    sigma_r = sigma / 5.8e7   # normalised to copper
    f_mhz = f / 1e6
    R_dB = 168.0 + 10.0 * np.log10(sigma_r * mu_r / f_mhz)
    return R_dB


def SE_absorption_loss(delta, t):
    """
    Absorption loss: A_dB = 8.686 · t / δ
    delta: skin depth (m)
    t    : shield thickness (m)
    """
    return 8.686 * t / delta


def SE_total(R_dB, A_dB, B_dB=0.0):
    """
    Total shielding effectiveness: SE = R + A + B (dB)
    B correction term: for thin shields, near-field, etc.
    """
    return R_dB + A_dB + B_dB


def shield_design_target(SE_target_dB, f, sigma, mu_r, t_existing=0.0):
    """
    Determine required shield thickness given target SE.
    Iteratively find t such that SE_total >= SE_target.
    Returns required t in mm.
    """
    delta = np.sqrt(1.0 / (pi * f * mu_0 * mu_r * sigma))
    # Solve: R_dB + 8.686*t/delta >= SE_target
    # R_dB = 168 + 10*log10(σ_r*μ_r/f_MHz) (constant for fixed f)
    R_dB = SE_reflection_loss(sigma, mu_r, f)
    A_needed = SE_target_dB - R_dB
    if A_needed <= 0:
        return 0.0  # reflection alone exceeds target
    t_required = A_needed * delta / 8.686
    return t_required * 1e3  # mm


# ══════════════════════════════════════════════════════════════════
# 7. GROUND LOOP ANALYSIS
# ══════════════════════════════════════════════════════════════════

def ground_loop_rejection_ratio(Z_common_mode, Z_signal_return, CMRR_amplifier_dB):
    """
    Ground loop rejection: how well amplifier rejects common-mode interference.
    Returns voltage at amplifier input due to ground potential difference.
    """
    V_gpd = 0.05  # 50 mV ground potential difference (typical)
    Z_cm = Z_common_mode
    CMRR_linear = 10**(CMRR_amplifier_dB / 20.0)
    V_rejected = V_gpd / CMRR_linear
    return V_rejected


# ══════════════════════════════════════════════════════════════════
# 8. BONDING DESIGN — Contact Impedance
# ══════════════════════════════════════════════════════════════════

def contact_impedance_at_f(R_contact_mohm, L_contact_nH, f):
    """
    Bonding contact impedance: Z = R + jωL (frequency-dependent).
    R_contact_mohm: DC contact resistance (milliohms)
    L_contact_nH  : contact loop inductance (nH)
    f             : frequency (Hz)
    Returns impedance in milliohms.
    """
    R = R_contact_mohm
    L_H = L_contact_nH * 1e-9
    Z_mohm = np.sqrt(R**2 + (2.0 * pi * f * L_H * 1e3)**2)
    return Z_mohm


def bond_class_impedance_check(Z_mohm, bond_class, f):
    """
    Check if bonding impedance meets class requirement at frequency f.
    """
    limit = BOND_CLASS[bond_class]['DC_resistance_mohm']
    # At high freq, allow 100 mΩ for Class R per NASA-STD-4003A
    if bond_class == 'ClassR' and f > 1e6:
        limit_impedance = 100.0  # mΩ at 1 MHz
    else:
        limit_impedance = limit
    return {
        'measured_mohm': Z_mohm,
        'limit_mohm': limit_impedance,
        'pass': Z_mohm <= limit_impedance,
        'frequency_hz': f,
    }


# ══════════════════════════════════════════════════════════════════
# NUMERICAL EXAMPLES
# ══════════════════════════════════════════════════════════════════

def example_1_bond_class_compliance():
    """Example 1: Verify bonding resistance for Class R (RF equipment)."""
    print("\n" + "="*60)
    print("EXAMPLE 1 — Electrical Bonding Resistance Compliance")
    print("="*60)
    measurements = {
        'Chassis bonding strap': 1.8,   # mΩ
        'Antenna feedthrough': 2.1,      # mΩ
        'Filter housing bond': 2.4,      # mΩ
        'PCB mounting screws': 0.08,     # mΩ (Class C requirement)
    }
    for name, R_mohm in measurements.items():
        result = bonding_resistance_check(R_mohm, 'ClassR')
        status = 'PASS ✓' if result['pass'] else 'FAIL ✗'
        print(f"  {name:30s}: {R_mohm:.2f} mΩ | limit {result['limit_mohm']:.1f} mΩ | {status}")


def example_2_bonding_jumper_inductance():
    """Example 2: Class R bonding jumper aspect ratio and HF impedance."""
    print("\n" + "="*60)
    print("EXAMPLE 2 — Bonding Jumper Inductance & Aspect Ratio")
    print("="*60)
    # Flat copper strap: 50 mm × 5 mm × 1 mm
    L_j = 50e-3   # 50 mm
    w = 5e-3      # 5 mm
    t = 1e-3      # 1 mm
    ar = bonding_jumper_aspect_ratio(L_j, w)
    print(f"  Jumper dimensions: {L_j*1e3:.0f} mm × {w*1e3:.0f} mm × {t*1e3:.0f} mm")
    print(f"  Aspect ratio L/w = {ar:.1f} (limit: ≤5 for Class R) — {'PASS ✓' if ar <= 5 else 'FAIL ✗'}")
    for f_mhz in [1, 10, 100]:
        f = f_mhz * 1e6
        L_nH = bonding_jumper_impedance(f, L_j, w, t) * 1e9
        # Z = jωL
        Z_mohm = 2.0 * pi * f * (L_nH * 1e-9) * 1e3
        print(f"  At {f_mhz:3d} MHz: L = {L_nH:.1f} nH, Z = {Z_mohm:.1f} mΩ")


def example_3_cable_classification():
    """Example 3: Classify cable based on signal characteristics."""
    print("\n" + "="*60)
    print("EXAMPLE 3 — Cable EMC Category Classification")
    print("="*60)
    cables = [
        {'name': 'Primary power bus',        'V_DC': 28.0, 'f_AC': 0.0,      'I_load': 5.0},
        {'name': 'Attitude sensor data',      'V_DC': 5.0,  'f_AC': 400e3,   'I_load': 0.1},
        {'name': 'RF transmitter feed',       'V_DC': 12.0, 'f_AC': 2.4e9,   'I_load': 2.0},
        {'name': 'EED firing circuit',         'V_DC': 5.0,  'f_AC': 0.0,      'I_load': 0.0, 'pulse_Vmax': 30.0},
        {'name': 'Low-level analog sensor',   'V_DC': 3.3,  'f_AC': 1e3,     'I_load': 0.01},
    ]
    for cable in cables:
        cat = cable_category_from_params(
            cable['V_DC'], cable['I_load'], cable['f_AC'],
            pulse_Vmax=cable.get('pulse_Vmax')
        )
        print(f"  {cable['name']:30s}: {cat} — {CABLE_CATEGORY[cat]['description']}")


def example_4_shielding_effectiveness():
    """Example 4: Aluminum chassis shielding effectiveness at multiple frequencies."""
    print("\n" + "="*60)
    print("EXAMPLE 4 — Aluminum Chassis Shielding Effectiveness (0.5 mm Al)")
    print("="*60)
    sigma_Al = 3.5e7   # S/m
    mu_r = 1.0
    t_mm = 0.5         # 0.5 mm aluminum
    t = t_mm * 1e-3
    for f_mhz in [1, 10, 100, 1000]:
        f = f_mhz * 1e6
        delta = np.sqrt(1.0 / (pi * f * mu_0 * mu_r * sigma_Al))
        R = SE_reflection_loss(sigma_Al, mu_r, f)
        A = SE_absorption_loss(delta, t)
        SE = SE_total(R, A)
        print(f"  f = {f_mhz:4d} MHz: δ = {delta*1e6:.2f} μm | R = {R:.1f} dB | A = {A:.1f} dB | SE = {SE:.1f} dB")


def example_5_conducted_emission_margin():
    """Example 5: CE margin analysis for 28 V power bus at 50 kHz."""
    print("\n" + "="*60)
    print("EXAMPLE 5 — Conducted Emission Margin vs. MIL-STD-461")
    print("="*60)
    f_hz = 50e3
    emission_levels = {
        'Switching converter (SMPS)': 75.0,   # dBμA
        'Linear regulator': 45.0,              # dBμA
        'Motor drive PWM': 82.0,               # dBμA
    }
    limit = ce_limit_mil_461(f_hz)
    print(f"  MIL-STD-461E CE101 limit at {f_hz/1e3:.0f} kHz: {limit:.1f} dBμA")
    for name, emission in emission_levels.items():
        margin = limit - emission
        status = 'PASS ✓' if margin >= 6.0 else 'FAIL ✗'
        print(f"  {name:30s}: emission = {emission:.1f} dBμA | margin = {margin:.1f} dB | {status}")


def example_6_ground_loop_current():
    """Example 6: Ground loop current in spacecraft payload with 50 mV GPD."""
    print("\n" + "="*60)
    print("EXAMPLE 6 — Ground Loop Current Analysis")
    print("="*60)
    V_gpd = 0.050       # 50 mV ground potential difference
    Z_loop_choices = [0.1, 1.0, 10.0]  # ohms (wire + contact resistance)
    for Z in Z_loop_choices:
        I_loop = ground_loop_current(V_gpd, Z)
        print(f"  Z_loop = {Z:.1f} Ω → I_loop = {I_loop*1e3:.2f} mA")
    # With 10 mΩ loop (good bonding), only 5 mA flows
    # This is usually below threshold for causing interference


def example_7_crosstalk_between_cables():
    """Example 7: Mutual inductance and crosstalk between parallel cable runs."""
    print("\n" + "="*60)
    print("EXAMPLE 7 — Mutual Inductance & Crosstalk Between Parallel Cables")
    print("="*60)
    l_coup = 0.5       # 0.5 m coupling length
    d_sep_mm = 10.0    # 10 mm separation
    d_sep = d_sep_mm * 1e-3
    M = mutual_inductance_parallel_cables(l_coup, d_sep)
    print(f"  Coupling length = {l_coup*1e3:.0f} mm, separation = {d_sep_mm:.0f} mm")
    print(f"  Mutual inductance M = {M*1e9:.2f} nH")
    V_agg = 3.3    # 3.3 V clock signal
    for f_mhz in [10, 50, 100]:
        f = f_mhz * 1e6
        V_ct = crosstalk_voltage_Victim(V_agg, f, M, Z_victim=50.0)
        print(f"  At {f_mhz:3d} MHz: crosstalk V = {V_ct*1e3:.3f} mV")


def example_8_shield_design_iteration():
    """Example 8: Determine required aluminum thickness for 60 dB SE at 1 GHz."""
    print("\n" + "="*60)
    print("EXAMPLE 8 — Shield Thickness Design for Target SE")
    print("="*60)
    SE_target = 60.0   # dB
    f = 1e9            # 1 GHz
    sigma_Al = 3.5e7
    mu_r = 1.0
    t_required_mm = shield_design_target(SE_target, f, sigma_Al, mu_r)
    print(f"  Target SE = {SE_target:.0f} dB at {f/1e9:.0f} GHz")
    print(f"  Required Al thickness: {t_required_mm:.2f} mm")
    # Verify
    delta = np.sqrt(1.0 / (pi * f * mu_0 * mu_r * sigma_Al))
    R = SE_reflection_loss(sigma_Al, mu_r, f)
    A = SE_absorption_loss(delta, t_required_mm * 1e-3)
    SE_actual = SE_total(R, A)
    print(f"  Verification: R = {R:.1f} dB, A = {A:.1f} dB, SE = {SE_actual:.1f} dB")


# ══════════════════════════════════════════════════════════════════
# FIGURE 1 — Bonding Impedance vs. Frequency for SPG vs MPG
# ══════════════════════════════════════════════════════════════════

def plot_ground_impedance_comparison():
    """
    Compare SPG vs MPG ground impedance vs. frequency.
    Shows how MPG reduces impedance above ~1 MHz.
    """
    f_range = np.logspace(2, 8, 400)  # 100 Hz to 100 MHz
    Z_trace = 0.01   # 10 mΩ trace DC resistance

    Z_SPG = np.array([ground_impedance_SPG(fi, Z_trace) for fi in f_range])
    Z_MPG = np.array([ground_impedance_MPG(fi, Z_trace, 4) for fi in f_range])
    Z_MPG_8 = np.array([ground_impedance_MPG(fi, Z_trace, 8) for fi in f_range])

    fig, axes = plt.subplots(2, 1, figsize=(11, 8))

    axes[0].semilogx(f_range, Z_SPG * 1e3, label='SPG (single-point)', color='C0', linewidth=2.0)
    axes[0].semilogx(f_range, Z_MPG * 1e3, label='MPG (4 points)', color='C1', linewidth=2.0)
    axes[0].semilogx(f_range, Z_MPG_8 * 1e3, label='MPG (8 points)', color='C2', linewidth=2.0)
    axes[0].set_ylabel('Ground Impedance (mΩ)', fontsize=11)
    axes[0].set_title('Ground Impedance vs. Frequency — SPG vs MPG\n(Zhang Ch2 — Grounding Design)', fontsize=12, fontweight='bold')
    axes[0].legend(fontsize=10)
    axes[0].grid(True, which='both', alpha=0.3)
    axes[0].axvline(1e5, color='red', linestyle='--', alpha=0.5, label='SPG/MPG cutoff ~100 kHz')

    # Phase: SPG vs MPG
    # Impedance phase = arctan(X/R) where X=ωL_eff
    L_SPG = Z_trace / (2.0 * pi * 100.0)
    L_MPG_4 = L_SPG / 4.0
    phase_SPG = np.arctan2(2.0 * np.pi * f_range * L_SPG, Z_trace) * 180.0 / np.pi
    phase_MPG = np.arctan2(2.0 * np.pi * f_range * L_MPG_4, Z_trace) * 180.0 / np.pi
    axes[1].semilogx(f_range, phase_SPG, label='SPG', color='C0', linewidth=2.0)
    axes[1].semilogx(f_range, phase_MPG, label='MPG (4 pts)', color='C1', linewidth=2.0)
    axes[1].set_xlabel('Frequency (Hz)', fontsize=11)
    axes[1].set_ylabel('Impedance Phase (°)', fontsize=11)
    axes[1].set_title('Phase of Ground Impedance')
    axes[1].legend(fontsize=10)
    axes[1].grid(True, which='both', alpha=0.3)

    plt.tight_layout()
    out_path = '/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures/ch2_ground_impedance.png'
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"[FIGURE] ch2_ground_impedance.png saved.")
    return out_path


# ══════════════════════════════════════════════════════════════════
# FIGURE 2 — Shielding Effectiveness: SE vs. Frequency (Al, Cu, Steel)
# ══════════════════════════════════════════════════════════════════

def plot_shielding_effectiveness():
    """
    Total SE vs. frequency for 0.5 mm Al, Cu, and 1 mm steel.
    Shows R, A, and total SE components.
    """
    f_range = np.logspace(4, 10, 400)  # 10 kHz to 10 GHz
    materials = {
        'Al (0.5 mm)': {'sigma': 3.5e7, 'mu_r': 1.0, 't_mm': 0.5},
        'Cu (0.5 mm)': {'sigma': 5.8e7, 'mu_r': 1.0, 't_mm': 0.5},
        'Steel (1.0 mm)': {'sigma': 1.5e6, 'mu_r': 100.0, 't_mm': 1.0},
    }

    fig, axes = plt.subplots(2, 1, figsize=(11, 8))

    for label, mat in materials.items():
        sigma, mu_r, t_mm = mat['sigma'], mat['mu_r'], mat['t_mm']
        t = t_mm * 1e-3
        R_arr = np.array([SE_reflection_loss(sigma, mu_r, f) for f in f_range])
        A_arr = np.array([SE_absorption_loss(
            np.sqrt(1.0 / (pi * f * mu_0 * mu_r * sigma)), t) for f in f_range])
        SE_arr = R_arr + A_arr

        axes[0].semilogx(f_range, R_arr, label=f'{label} — R', linestyle='--', linewidth=1.5, alpha=0.7)
        axes[0].semilogx(f_range, A_arr, label=f'{label} — A', linestyle=':', linewidth=1.5, alpha=0.7)
        axes[1].semilogx(f_range, SE_arr, label=label, linewidth=2.0)

    axes[0].set_ylabel('Loss Component (dB)', fontsize=11)
    axes[0].set_title('Shielding Effectiveness Components — Reflection (R) & Absorption (A)\n(Zhang Ch2 — Shielding Design)', fontsize=12, fontweight='bold')
    axes[0].legend(fontsize=8, ncol=2)
    axes[0].grid(True, which='both', alpha=0.3)

    axes[1].set_xlabel('Frequency (Hz)', fontsize=11)
    axes[1].set_ylabel('Total SE (dB)', fontsize=11)
    axes[1].set_title('Total Shielding Effectiveness (SE = R + A)')
    axes[1].legend(fontsize=10)
    axes[1].grid(True, which='both', alpha=0.3)
    # 60 dB target line
    axes[1].axhline(60, color='red', linestyle='--', alpha=0.5, label='Typical 60 dB target')

    plt.tight_layout()
    out_path = '/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures/ch2_shielding_effectiveness.png'
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"[FIGURE] ch2_shielding_effectiveness.png saved.")
    return out_path


# ──────────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("="*60)
    print("Zhang EMC — Chapter 2: EMI Interface Control Methods")
    print("Spacecraft Electromagnetic Compatibility Technologies (2020)")
    print("="*60)

    example_1_bond_class_compliance()
    example_2_bonding_jumper_inductance()
    example_3_cable_classification()
    example_4_shielding_effectiveness()
    example_5_conducted_emission_margin()
    example_6_ground_loop_current()
    example_7_crosstalk_between_cables()
    example_8_shield_design_iteration()

    print("\n" + "="*60)
    print("Generating figures...")
    print("="*60)
    plot_ground_impedance_comparison()
    plot_shielding_effectiveness()
    print("\nAll tasks complete.")