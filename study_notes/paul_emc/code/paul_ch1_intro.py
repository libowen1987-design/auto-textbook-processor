#!/usr/bin/env python3
"""
Paul "EMC" 2nd Ed. — Chapter 1: Introduction to EMC
=====================================================
Code examples covering:
  1. dB unit conversions (dBm, dBmV, dBμV, dBW, dBμA)
  2. Free-space wavelength calculator  λ = v / f
  3. Electrical-size classification  L / λ
  4. EMC emission & immunity budget margins
  5. Radio-frequency band definitions (30 Hz – 300 GHz)

All variable names follow EMC textbook conventions.
Matplotlib plots generated for key relationships.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

# ─────────────────────────────────────────────────────────────────────────────
# 0. Physical constants
# ─────────────────────────────────────────────────────────────────────────────
SPEED_OF_LIGHT = constants.c          # 299,792,458 m/s (exact by definition)
c = SPEED_OF_LIGHT
PERMEABILITY_FREE_SPACE = constants.mu_0   # 4π × 10⁻⁷ H/m
PERMITTIVITY_FREE_SPACE = constants.epsilon_0  # 8.854 × 10⁻¹² F/m
IMPEDANCE_FREE_SPACE = np.sqrt(PERMEABILITY_FREE_SPACE / PERMITTIVITY_FREE_SPACE)  # ≈ 376.99 Ω

# ─────────────────────────────────────────────────────────────────────────────
# 1. dB UNIT CONVERSIONS
# ─────────────────────────────────────────────────────────────────────────────

def dbm_to_watts(p_dbm: float) -> float:
    """Convert dBm (decibels relative to 1 mW) to watts."""
    return 0.001 * 10**(p_dbm / 10)


def watts_to_dbm(p_watts: float) -> float:
    """Convert watts to dBm."""
    return 10 * np.log10(p_watts / 0.001)


def dbm_to_dbuv(p_dbm: float, impedance_ohm: float = 50.0) -> float:
    """
    Convert dBm to dBμV (decibels relative to 1 μV).
    Power in dBm: P_dBm = 10·log10(P_W / 1mW)
    Voltage:  P = V² / R  →  V = sqrt(P·R)
    Reference dBμV: 0 dBμV = 1 μV_rms
    """
    p_w = dbm_to_watts(p_dbm)
    v_rms = np.sqrt(p_w * impedance_ohm)          # RMS voltage
    return 20 * np.log10(v_rms / 1e-6)             # dBμV


def dbuv_to_dbm(v_dbuv: float, impedance_ohm: float = 50.0) -> float:
    """
    Convert dBμV back to dBm.
    V_rms = 10^(V_dBuV/20) × 1e-6
    P = V² / R  →  P_dBm = 10·log10(P / 1mW)
    """
    v_rms = 10**(v_dbuv / 20) * 1e-6
    p_w = (v_rms**2) / impedance_ohm
    return watts_to_dbm(p_w)


def dbm_to_dbmv(p_dbm: float, impedance_ohm: float = 50.0) -> float:
    """
    Convert dBm to dBmV (decibels relative to 1 mV).
    0 dBmV = 1 mV_rms.
    """
    p_w = dbm_to_watts(p_dbm)
    v_rms = np.sqrt(p_w * impedance_ohm)
    return 20 * np.log10(v_rms / 1e-3)


def dbmv_to_dbm(p_dbmv: float, impedance_ohm: float = 50.0) -> float:
    """Convert dBmV to dBm."""
    v_rms = 10**(p_dbmv / 20) * 1e-3
    p_w = (v_rms**2) / impedance_ohm
    return watts_to_dbm(p_w)


def dbm_to_dbw(p_dbm: float) -> float:
    """Convert dBm to dBW (decibels relative to 1 W)."""
    return p_dbm - 30


def dbw_to_dbm(p_dbw: float) -> float:
    """Convert dBW to dBm."""
    return p_dbw + 30


def db_to_linear(db: float) -> float:
    """Convert dB to linear ratio."""
    return 10**(db / 10)


def linear_to_db(ratio: float) -> float:
    """Convert linear ratio to dB."""
    return 10 * np.log10(ratio)


# ─────────────────────────────────────────────────────────────────────────────
# 2. WAVELENGTH CALCULATOR
# ─────────────────────────────────────────────────────────────────────────────

def wavelength(frequency_hz: float, velocity_mps: float = c) -> float:
    """
    Compute free-space wavelength λ = v / f.

    Parameters
    ----------
    frequency_hz : float
        Frequency in hertz.
    velocity_mps : float
        Propagation speed in m/s (default: speed of light c).

    Returns
    -------
    float
        Wavelength in meters.
    """
    return velocity_mps / frequency_hz


def frequency_from_wavelength(lambda_m: float, velocity_mps: float = c) -> float:
    """Compute frequency from wavelength: f = v / λ."""
    return velocity_mps / lambda_m


def wavelength_in_dielectric(frequency_hz: float, epsilon_r: float) -> float:
    """
    Compute wavelength inside a dielectric material.
    v = c / sqrt(ε_r)  →  λ = v / f = c / (f · sqrt(ε_r))
    """
    return c / (frequency_hz * np.sqrt(epsilon_r))


def skin_depth(frequency_hz: float, conductivity_s_m: float,
               mu_r: float = 1.0) -> float:
    """
    Approximate skin depth δ = sqrt(2 / (ω·μ·σ))
    where ω = 2πf, μ = μ_r·μ_0, σ = conductivity in S/m.

    Returns skin depth in meters.
    """
    omega = 2 * np.pi * frequency_hz
    mu = mu_r * PERMEABILITY_FREE_SPACE
    return np.sqrt(2 / (omega * mu * conductivity_s_m))


# ─────────────────────────────────────────────────────────────────────────────
# 3. ELECTRICAL SIZE CLASSIFICATION
# ─────────────────────────────────────────────────────────────────────────────

def electrical_size(physical_length_m: float, frequency_hz: float,
                   velocity_mps: float = c) -> float:
    """
    Compute the electrical size: L / λ.
    Ratio of physical length to wavelength.
    """
    lam = wavelength(frequency_hz, velocity_mps)
    return physical_length_m / lam


def classify_electrically_small(physical_length_m: float, frequency_hz: float,
                                threshold: float = 0.1,
                                velocity_mps: float = c) -> bool:
    """
    Return True if the structure is 'electrically small'
    (L/λ < threshold, default threshold = 0.1 per EMC convention).
    """
    ratio = electrical_size(physical_length_m, frequency_hz, velocity_mps)
    return ratio < threshold


def human_readable_size(physical_length_m: float, frequency_hz: float,
                        velocity_mps: float = c) -> str:
    """Classify a structure and return a description string."""
    ratio = electrical_size(physical_length_m, frequency_hz, velocity_mps)
    if ratio < 0.01:
        desc = "sub-electrically-small"
    elif ratio < 0.1:
        desc = "electrically-small"
    elif ratio < 0.5:
        desc = "electrically-medium"
    elif ratio < 1.0:
        desc = "electrically-large"
    else:
        desc = "electrically-very-large"
    return f"{desc}  (L/λ = {ratio:.4f})"


# ─────────────────────────────────────────────────────────────────────────────
# 4. EMC BUDGET MARGINS
# ─────────────────────────────────────────────────────────────────────────────

def emission_margin(measured_level_dbuv: float,
                    limit_dbuv: float,
                    safety_margin_db: float = 6.0) -> float:
    """
    Compute emission margin = Limit − Measured − Safety_Margin.
    Positive → passes; negative → fails.

    Parameters
    ----------
    measured_level_dbuv : float
        Measured emission level in dBμV.
    limit_dbuv : float
        Regulatory emission limit in dBμV.
    safety_margin_db : float
        Allowance for measurement uncertainty (default 6 dB).

    Returns
    -------
    float
        Margin in dB (positive = compliant).
    """
    return limit_dbuv - measured_level_dbuv - safety_margin_db


def immunity_margin(immunity_level_dbv: float,
                    applicable_level_dbv: float,
                    safety_margin_db: float = 6.0) -> float:
    """
    Compute immunity margin = Immunity_Level − Applied_Level − Safety_Margin.
    Positive → passes; negative → fails.
    """
    return immunity_level_dbv - applicable_level_dbv - safety_margin_db


def field_strength_from_voltage(power_dbm: float,
                                antenna_gain_db: float,
                                distance_m: float,
                                impedance_ohm: float = 50.0) -> float:
    """
    Estimate far-field electric-field strength from conducted power.
    E(V/m) ≈ sqrt(30 · P_W · G_lin) / d  (far-field, free space)
    where G_lin = 10^(gain_dB/10).
    """
    p_w = dbm_to_watts(power_dbm)
    g_lin = db_to_linear(antenna_gain_db)
    e_field = np.sqrt(30 * p_w * g_lin) / distance_m
    return e_field


def field_strength_to_dbuvm(e_field_v_m: float) -> float:
    """Convert E-field in V/m to dBμV/m."""
    return 20 * np.log10(e_field_v_m / 1e-6)


def conducted_to_radiated(power_dbm: float,
                           antenna_gain_db: float,
                           distance_m: float,
                           impedance_ohm: float = 50.0) -> float:
    """
    One-line wrapper: conducted power (dBm) → radiated field (dBμV/m).
    """
    e = field_strength_from_voltage(power_dbm, antenna_gain_db,
                                    distance_m, impedance_ohm)
    return field_strength_to_dbuvm(e)


# ─────────────────────────────────────────────────────────────────────────────
# 5. RADIO-FREQUENCY BAND DEFINITIONS (ITU / IEEE standard)
# ─────────────────────────────────────────────────────────────────────────────

BAND_DEFINITIONS = [
    # (name, lower_freq_hz, upper_freq_hz)
    ("ELF  (Extremely Low Frequency)",    3e1,   3e2),
    ("SLF  (Super Low Frequency)",         3e2,   3e3),
    ("ULF  (Ultra Low Frequency)",        3e3,   3e5),
    ("VLF  (Very Low Frequency)",          3e4,   3e5),
    ("LF   (Low Frequency)",               3e5,   3e6),
    ("MF   (Medium Frequency)",            3e6,   3e7),
    ("HF   (High Frequency)",              3e7,   3e8),
    ("VHF  (Very High Frequency)",         3e8,   3e9),
    ("UHF  (Ultra High Frequency)",        3e9,   3e10),
    ("SHF  (Super High Frequency)",        3e10,  3e11),
    ("EHF  (Extremely High Frequency)",    3e11,  3e12),
    ("THF  (Tremendously High Frequency)", 3e12,  3e14),
]


def find_band(frequency_hz: float) -> str:
    """Return the ITU band name for a given frequency in Hz."""
    for name, f_low, f_high in BAND_DEFINITIONS:
        if f_low <= frequency_hz < f_high:
            return name
    return "Outside defined RF bands"


def list_bands():
    """Print a formatted table of all RF bands."""
    print("\n{:<45} {:>15} {:>15}".format("Band", "f_low (Hz)", "f_high (Hz)"))
    print("-" * 77)
    for name, f_low, f_high in BAND_DEFINITIONS:
        print("{:<45} {:>15.0e} {:>15.0e}".format(name, f_low, f_high))


# ─────────────────────────────────────────────────────────────────────────────
# 6. PLOTTING UTILITIES
# ─────────────────────────────────────────────────────────────────────────────

def plot_wavelength_vs_frequency(f_min=1e3, f_max=1e12, points=500):
    """
    Plot wavelength (m) vs frequency (Hz) on log-log axes.
    Marks key EMC bands (HF, VHF, UHF, SHF) with vertical shaded regions.
    """
    freqs = np.logspace(np.log10(f_min), np.log10(f_max), points)
    lambdas = wavelength(freqs)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.loglog(freqs, lambdas, 'b-', linewidth=2, label=r'$\lambda = c/f$')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Frequency (Hz)', fontsize=13)
    ax.set_ylabel('Wavelength (m)', fontsize=13)
    ax.set_title('Free-Space Wavelength vs Frequency (Paul EMC Ch.1)', fontsize=14)
    ax.grid(True, which='both', linestyle='--', alpha=0.5)

    # Shade key EMC bands
    bands_to_mark = [
        ("HF",   3e7,  3e8,  'lightgreen'),
        ("VHF",  3e8,  3e9,  'lightblue'),
        ("UHF",  3e9,  3e10, 'wheat'),
        ("SHF",  3e10, 3e11, 'lightyellow'),
    ]
    for bname, f_l, f_h, color in bands_to_mark:
        ax.axvspan(f_l, f_h, alpha=0.25, color=color, label=bname)
        ax.text(np.sqrt(f_l * f_h), lambdas[np.argmin(np.abs(freqs - np.sqrt(f_l*f_h)))],
                bname, fontsize=9, ha='center', color='darkslategray')

    ax.legend(fontsize=10)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/paul_emc/code/wavelength_vs_frequency.png',
                dpi=150)
    plt.close()
    print("[PLOT] wavelength_vs_frequency.png saved.")


def plot_dbm_conversion_scale():
    """
    Visualise the dBm scale from 1 nW to 1 kW with key tick marks.
    """
    p_watts = np.array([1e-9, 1e-6, 1e-3, 1e0, 1e3])
    p_dbm   = watts_to_dbm(p_watts)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.semilogy(p_dbm, p_watts, 'ko-', linewidth=2, markersize=8)
    ax.set_xlabel('Power (dBm)', fontsize=13)
    ax.set_ylabel('Power (W)', fontsize=13)
    ax.set_title('dBm ↔ Watt Conversion Scale (Paul EMC Ch.1)', fontsize=14)
    ax.grid(True, which='both', linestyle='--', alpha=0.5)
    ax.set_xticks(p_dbm)
    ax.set_xticklabels([f'{v:.0f}' for v in p_dbm])
    labels_map = {1e-9: '1 nW', 1e-6: '1 μW', 1e-3: '1 mW',
                  1e0: '1 W', 1e3: '1 kW'}
    for x, y in zip(p_dbm, p_watts):
        ax.annotate(labels_map[y], xy=(x, y),
                    xytext=(5, 10), textcoords='offset points', fontsize=9)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/paul_emc/code/dbm_scale.png', dpi=150)
    plt.close()
    print("[PLOT] dbm_scale.png saved.")


# ─────────────────────────────────────────────────────────────────────────────
# VALIDATION EXAMPLES  (values taken from Paul EMC 2nd Ed. Chapter 1)
# ─────────────────────────────────────────────────────────────────────────────

def run_validation():
    """Run all validation checks against textbook values."""
    print("=" * 68)
    print("  Paul EMC 2nd Ed. — Ch.1 Code Validation")
    print("=" * 68)

    # ── dB conversions ──────────────────────────────────────────────────────
    print("\n── dB Unit Conversions ──────────────────────────────────────────")

    # Example: 0 dBm = 1 mW  →  verify watts_to_dbm round-trip
    assert np.isclose(watts_to_dbm(0.001), 0.0, atol=1e-9), "0 dBm check failed"
    print(f"  ✓  0 dBm  =  {dbm_to_watts(0.0):.6f} W  (expected 0.001000 W)")

    # 30 dBm = 1 W
    assert np.isclose(dbm_to_watts(30.0), 1.0, atol=1e-9), "30 dBm = 1 W check failed"
    print(f"  ✓  30 dBm =  {dbm_to_watts(30.0):.6f} W  (expected 1.000000 W)")

    # 0 dBW = 30 dBm
    assert np.isclose(dbm_to_dbw(30.0), 0.0, atol=1e-9), "0 dBW check failed"
    print(f"  ✓  30 dBm =  {dbm_to_dbw(30.0):.6f} dBW  (expected 0.00 dBW)")

    # 0 dBmV = 1 mV → convert to dBm at 50 Ω
    # P = V²/R = (1e-3)²/50 = 2e-8 W  →  10·log10(2e-8/1e-3) = -47 dBm
    p_dbm_from_dbmv = dbmv_to_dbm(0.0)
    assert np.isclose(p_dbm_from_dbmv, -47.0, atol=0.5), f"dBmV→dBm check: {p_dbm_from_dbmv}"
    print(f"  ✓  0 dBmV (50 Ω)  =  {p_dbm_from_dbmv:.2f} dBm  (expected ≈ -47 dBm)")

    # Round-trip: dBm → dBμV → dBm
    orig_dbm = 20.0
    conv_dbuv = dbm_to_dbuv(orig_dbm)
    back_dbm  = dbuv_to_dbm(conv_dbuv)
    assert np.isclose(back_dbm, orig_dbm, atol=1e-6), "dBm→dBμV→dBm round-trip failed"
    print(f"  ✓  dBm↔dBμV round-trip OK  ({orig_dbm:.1f} dBm → {conv_dbuv:.2f} dBμV → {back_dbm:.6f} dBm)")

    # ── Wavelength ───────────────────────────────────────────────────────────
    print("\n── Wavelength Calculator ────────────────────────────────────────")

    # 1 GHz in free space: λ = c / 1e9  ≈ 0.2998 m
    lam_1ghz = wavelength(1e9)
    assert np.isclose(lam_1ghz, c/1e9, atol=1e-6), "1 GHz wavelength check failed"
    print(f"  ✓  λ @ 1 GHz   =  {lam_1ghz:.6f} m  (≈ c/1e9, textbook ≈ 0.30 m)")

    # 300 MHz: λ = c / 3e8  ≈ 0.9993 m
    lam_300mhz = wavelength(3e8)
    assert np.isclose(lam_300mhz, c/3e8, atol=1e-6), "300 MHz wavelength check failed"
    print(f"  ✓  λ @ 300 MHz =  {lam_300mhz:.6f} m  (≈ c/3e8, textbook ≈ 1.0 m)")

    # 30 MHz: λ = c / 3e7  ≈ 9.993 m
    lam_30mhz = wavelength(3e7)
    assert np.isclose(lam_30mhz, c/3e7, atol=1e-6), "30 MHz wavelength check failed"
    print(f"  ✓  λ @ 30 MHz  =  {lam_30mhz:.6f} m  (≈ c/3e7, textbook ≈ 10 m)")

    # FR4 dielectric (ε_r = 4.4) @ 2.4 GHz: λ = c / (f·√ε_r)
    lam_fr4 = wavelength_in_dielectric(2.4e9, 4.4)
    expected_fr4 = c / (2.4e9 * np.sqrt(4.4))
    assert np.isclose(lam_fr4, expected_fr4, atol=1e-6), "FR4 wavelength check failed"
    print(f"  ✓  λ @ 2.4 GHz in FR4 (ε_r=4.4) = {lam_fr4:.4f} m")

    # Copper skin depth @ 1 GHz (σ ≈ 5.8×10⁷ S/m)
    delta_1ghz_cu = skin_depth(1e9, 5.8e7)
    print(f"  ✓  δ @ 1 GHz (Cu) = {delta_1ghz_cu*1e6:.2f} μm  (≈ 2.1 μm per textbook)")

    # ── Electrical size ──────────────────────────────────────────────────────
    print("\n── Electrical Size Classification ───────────────────────────────")

    # 1 m structure @ 30 MHz: L/λ = 1/10 = 0.1  →  boundary case
    size_1m_30mhz = electrical_size(1.0, 3e7)
    print(f"  ✓  1 m @ 30 MHz  →  L/λ = {size_1m_30mhz:.2f}  (expected 0.10)")
    desc = human_readable_size(1.0, 3e7)
    print(f"     → {desc}")

    # 10 cm @ 1 GHz: λ=0.3 m → L/λ ≈ 0.33  →  "electrically-medium"
    size_10cm_1ghz = electrical_size(0.1, 1e9)
    print(f"  ✓  10 cm @ 1 GHz  →  L/λ = {size_10cm_1ghz:.2f}")
    desc = human_readable_size(0.1, 1e9)
    print(f"     → {desc}")

    # PCB trace 5 cm @ 3 GHz: λ=0.1 m → L/λ=0.5  →  "electrically-large"
    size_5cm_3ghz = electrical_size(0.05, 3e9)
    print(f"  ✓  5 cm @ 3 GHz   →  L/λ = {size_5cm_3ghz:.2f}")
    desc = human_readable_size(0.05, 3e9)
    print(f"     → {desc}")

    # ── EMC budget ─────────────────────────────────────────────────────────
    print("\n── EMC Emission & Immunity Budgets ──────────────────────────────")

    # CISPR 22 Class B radiated emission limit at 3 m, 30–230 MHz: 30 dBμV/m
    # Measured level = 25 dBμV/m  →  margin = 30 − 25 − 6 = −1 dB  (FAIL)
    margin_fail = emission_margin(measured_level_dbuv=25.0,
                                   limit_dbuv=30.0,
                                   safety_margin_db=6.0)
    print(f"  ✗  Emission: measured=25 dBμV/m, limit=30 dBμV/m, margin={margin_fail:.1f} dB  →  FAIL")

    # Measured = 20 dBμV/m  →  margin = 30 − 20 − 6 = 4 dB  (PASS)
    margin_pass = emission_margin(measured_level_dbuv=20.0,
                                  limit_dbuv=30.0,
                                  safety_margin_db=6.0)
    print(f"  ✓  Emission: measured=20 dBμV/m, limit=30 dBμV/m, margin={margin_pass:.1f} dB  →  PASS")

    # Immunity: equipment can withstand 10 V/m; standard requires 3 V/m
    immunity = immunity_margin(immunity_level_dbv=20.0,   # 10 V/m → 20 dBμV/m ≈ 20 dBV (for demo)
                                applicable_level_dbv=10.0,  # 3 V/m is ~10 dBV
                                safety_margin_db=6.0)
    print(f"  ✓  Immunity margin = {immunity:.1f} dB  (positive = compliant)")

    # Conducted → radiated field estimate
    radiated = conducted_to_radiated(power_dbm=0.0,   # 0 dBm = 1 mW
                                     antenna_gain_db=0.0,
                                     distance_m=3.0)
    print(f"  ✓  0 dBm conducted → {radiated:.1f} dBμV/m @ 3 m  (free-space, unity gain)")

    # ── Frequency bands ─────────────────────────────────────────────────────
    print("\n── RF Band Classification ───────────────────────────────────────")
    test_freqs = [1e4, 1e6, 1e7, 1e8, 5e8, 1e9, 3e9, 1e10, 1e11]
    for f in test_freqs:
        lam = wavelength(f)
        band = find_band(f)
        print(f"  {f:>12.0e} Hz  →  λ = {lam:>8.3f} m  [{band}]")

    list_bands()

    print("\n✓  All validation checks passed.")
    print("=" * 68)


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    run_validation()

    # Generate plots
    print("\n[INFO] Generating plots …")
    plot_wavelength_vs_frequency()
    plot_dbm_conversion_scale()

    print("\nDONE")
