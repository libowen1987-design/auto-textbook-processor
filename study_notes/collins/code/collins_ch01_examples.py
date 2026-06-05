#!/usr/bin/env python3
"""
Collins Ch.1 Examples — Frequency Bands, Wavelength, and Skin Effect
=====================================================================
Source: Robert E. Collin, "Foundations for Microwave Engineering", 2nd Ed.,
        IEEE Press, 2000, Ch. 1 (§1.1–§1.3), pp. 1–16.

All numerical values are from Collin Ch. 1 or computed from standard physical
constants given in the book (c0, mu0, eps0, eta0).
"""

import numpy as np

# ============================================================
# Physical Constants (from Collin §2.2, p. 23)
# ============================================================
C0 = 299792458.0       # speed of light in vacuum [m/s]
MU0 = 4.0 * np.pi * 1e-7  # permeability of free space [H/m]
EPS0 = 8.8541878176e-12   # permittivity of free space [F/m]
ETA0 = np.sqrt(MU0 / EPS0)  # intrinsic impedance of free space [Ω]

print("=" * 70)
print("FOUNDATIONS FOR MICROWAVE ENGINEERING — Ch.1  Examples")
print("Robert E. Collin, 2nd Ed., IEEE Press, 2000")
print("=" * 70)

# -----------------------------------------------------------
# §1.1: Frequency Band Designations (Table 1.1)
# -----------------------------------------------------------
print("\n" + "=" * 70)
print("§1.1: Standard Microwave Frequency Band Designations")
print("=" * 70)

bands = [
    ("VHF",  30e6,   300e6),
    ("UHF",  300e6,  1e9),
    ("L",    1e9,    2e9),
    ("S",    2e9,    4e9),
    ("C",    4e9,    8e9),
    ("X",    8e9,    12e9),
    ("Ku",   12e9,   18e9),
    ("K",    18e9,   27e9),
    ("Ka",   27e9,   40e9),
    ("U",    40e9,   300e9),  # EHF
]

print(f"{'Band':>6}  {'f_low [GHz]':>10}  {'f_high [GHz]':>11}  "
      f"{'λ_low [cm]':>10}  {'λ_high [cm]':>11}")
print("-" * 60)
for name, f_low, f_high in bands:
    lam_high = C0 / f_low * 100   # cm
    lam_low  = C0 / f_high * 100  # cm
    print(f"{name:>6}  {f_low/1e9:>10.3f}  {f_high/1e9:>11.3f}  "
          f"{lam_low:>10.2f}  {lam_high:>11.2f}")

# -----------------------------------------------------------
# §1.2: Wavelength at common microwave frequencies
# -----------------------------------------------------------
print("\n" + "=" * 70)
print("§1.2: Wavelength at Common Microwave Frequencies")
print("=" * 70)

freqs = np.array([0.915e9, 1.575e9, 2.45e9, 5.8e9, 10e9, 24e9, 77e9])
labels = ["ISM 915 MHz", "GPS L1", "ISM 2.45 GHz", "ISM 5.8 GHz",
          "X-band 10 GHz", "K-band 24 GHz", "W-band 77 GHz"]

print(f"{'Application':>20}  {'f [GHz]':>8}  {'λ [mm]':>8}")
print("-" * 42)
for label, f in zip(labels, freqs):
    lam = C0 / f * 1000  # mm
    print(f"{label:>20}  {f/1e9:>8.3f}  {lam:>8.2f}")

# -----------------------------------------------------------
# §1.3: Skin Effect — Skin Depth vs. Frequency
# -----------------------------------------------------------
print("\n" + "=" * 70)
print("§1.3: Skin Depth in Common Conductors (§1.3, Eq. 1.1 reference)")
print("       δ_s = 1 / sqrt(π f μ σ)")
print("=" * 70)

conductors = {
    "Silver (Ag)": 6.17e7,
    "Copper (Cu)": 5.80e7,
    "Gold (Au)":  4.10e7,
    "Aluminum":   3.72e7,
}

freqs_skin = np.array([1e9, 2.45e9, 5.8e9, 10e9, 24e9, 100e9])

print(f"{'Material':>15}  ", end="")
for f in freqs_skin:
    print(f"{f/1e9:>5.1f} GHz", end="    ")
print()
print("-" * 70)

for mat, sigma in conductors.items():
    print(f"{mat:>15}  ", end="")
    for f in freqs_skin:
        mu = MU0  # non-magnetic conductors
        delta_s = 1.0 / np.sqrt(np.pi * f * mu * sigma) * 1e6  # μm
        print(f"{delta_s:>8.3f} μm", end="  ")
    print()

# -----------------------------------------------------------
# §1.3: Surface Resistance vs. Frequency for Copper
# -----------------------------------------------------------
print("\n" + "=" * 70)
print("§1.3: Surface Resistance for Copper (§1.3)")
print("       R_s = 1 / (σ δ_s) = sqrt(π f μ / σ)  [Ω/□]")
print("=" * 70)

sigma_Cu = 5.80e7

print(f"{'f [GHz]':>8}  {'δ_s [μm]':>10}  {'R_s [mΩ/□]':>12}")
print("-" * 35)
for f in freqs_skin:
    delta_s = 1.0 / np.sqrt(np.pi * f * MU0 * sigma_Cu)
    R_s = 1.0 / (sigma_Cu * delta_s) * 1000  # mΩ/□
    print(f"{f/1e9:>8.3f}  {delta_s*1e6:>10.3f}  {R_s:>12.3f}")

# -----------------------------------------------------------
# §1.3: When do we need microwave analysis? (dimension vs λ)
# -----------------------------------------------------------
print("\n" + "=" * 70)
print("§1.3: Analysis Regime — Circuit Dimension vs Wavelength")
print("       Rule of thumb: distributed effects matter when L > λ/10")
print("=" * 70)

# Example: 10 cm circuit board trace
L_trace = 0.10  # m
freqs_regime = np.array([1e6, 100e6, 1e9, 2.45e9, 10e9, 24e9])

print(f"{'f':>10}  {'λ':>10}  {'L/λ':>8}  {'Regime':>20}")
print("-" * 50)
for f in freqs_regime:
    lam = C0 / f
    ratio = L_trace / lam
    if ratio < 0.01:
        regime = "Lumped"
    elif ratio < 0.1:
        regime = "Quasi-static"
    else:
        regime = "Distributed (MW)"
    print(f"{f/1e6:>8.2f} MHz  {lam*100:>8.2f} cm  {ratio:>8.3f}  {regime:>20}")

# ============================================================
# Verify Ch.1
# ============================================================
def verify_collins_ch01():
    """Self-check: verify key numerical values from Collin Ch.1."""
    errors = []

    # Fundamental constants (Collin §2.2)
    c0_check = 1.0 / np.sqrt(MU0 * EPS0)
    eta0_check = np.sqrt(MU0 / EPS0)

    if not np.isclose(c0_check, C0, rtol=1e-10):
        errors.append(f"c0 mismatch: {c0_check} vs {C0} (rel diff = {abs(c0_check-C0)/C0:.2e})")
    if not np.isclose(eta0_check, 376.7303, rtol=1e-4):
        errors.append(f"η0 mismatch: {eta0_check} vs 376.73")

    # Wavelength at 10 GHz should be ~3 cm
    lam_10ghz = C0 / 10e9
    if not np.isclose(lam_10ghz, 0.03, rtol=0.02):
        errors.append(f"λ(10 GHz) = {lam_10ghz} m, expected ~0.03 m")

    # Skin depth in Cu at 10 GHz (Collin §1.3: ~0.66 μm)
    delta_Cu_10G = 1.0 / np.sqrt(np.pi * 10e9 * MU0 * sigma_Cu)
    if not np.isclose(delta_Cu_10G, 0.66e-6, rtol=0.05):
        errors.append(f"δ_s(Cu, 10 GHz) = {delta_Cu_10G*1e6:.3f} μm, expected ~0.66 μm")

    # Surface resistance check
    Rs_Cu_10G = 1.0 / (sigma_Cu * delta_Cu_10G)
    if not np.isclose(Rs_Cu_10G, 0.026, rtol=0.1):
        errors.append(f"R_s(Cu, 10 GHz) = {Rs_Cu_10G*1000:.3f} mΩ, expected ~26 mΩ")

    if errors:
        print("\n❌ VERIFY FAILED:")
        for e in errors:
            print(f"   {e}")
        return False
    else:
        print("\n✅ VERIFY: All Ch.1 numerical checks passed.")
        return True

verify_collins_ch01()
print("\n✅ Collins Ch.1 examples complete.")
