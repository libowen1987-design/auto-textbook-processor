#!/usr/bin/env python3
"""
Collins Ch.3 Examples — Transmission Lines and Waveguides
============================================================
Source: Robert E. Collin, "Foundations for Microwave Engineering", 2nd Ed.,
        IEEE Press, 2000, Ch. 3 (§3.1–§3.6), pp. 71–140.

Demos:
  1. Z₀, Γ, VSWR, Z_in for terminated transmission line
  2. Rectangular waveguide TE₁₀ mode fields and cutoff
  3. Coax attenuation vs frequency
  4. Rectangular waveguide dispersion curves (β, λ_g, v_p, v_g)
  5. Microstrip Z₀ vs w/h
"""

import numpy as np
import warnings

# Suppress expectable divide-by-zero for open/short circuit VSWR
warnings.filterwarnings("ignore", category=RuntimeWarning, message=".*divide by zero.*")

# Physical constants (Collin §2.2)
C0 = 299792458.0       # speed of light in vacuum [m/s]
MU0 = 4.0 * np.pi * 1e-7  # permeability of free space [H/m]
EPS0 = 8.8541878176e-12   # permittivity of free space [F/m]
ETA0 = np.sqrt(MU0 / EPS0)  # intrinsic impedance [Ω]

print("=" * 72)
print("FOUNDATIONS FOR MICROWAVE ENGINEERING — Ch.3  Examples")
print("Robert E. Collin, 2nd Ed., IEEE Press, 2000, pp. 71–140")
print("=" * 72)


# =============================================================
# Demo 1: Z₀, Γ, VSWR, Z_in for a terminated line (§3.1)
# =============================================================
print("\n" + "=" * 72)
print("Demo 1: Terminated Transmission Line (§3.1, pp. 72–79)")
print("=" * 72)

def terminated_line(f, L, C, Z_L, ell, R=0.0, G=0.0):
    """
    Compute propagation parameters for a terminated transmission line.

    Parameters
    ----------
    f : float   — frequency [Hz]
    L : float   — inductance per unit length [H/m]
    C : float   — capacitance per unit length [F/m]
    Z_L : complex — load impedance [Ω]
    ell : float — line length [m]
    R, G : float — loss parameters (default 0 for lossless)

    Returns
    -------
    dict with Z0, gamma, beta, alpha, Gamma, VSWR, Z_in
    """
    omega = 2.0 * np.pi * f
    Z_series = R + 1j * omega * L
    Y_shunt = G + 1j * omega * C

    gamma = np.sqrt(Z_series * Y_shunt)
    Z0 = np.sqrt(Z_series / Y_shunt)
    alpha = gamma.real
    beta = gamma.imag

    # Reflection coefficient at load
    Gamma = (Z_L - Z0) / (Z_L + Z0)

    # VSWR
    absG = abs(Gamma)
    VSWR = (1.0 + absG) / (1.0 - absG)

    # Input impedance
    tanh_gamma_l = np.tanh(gamma * ell)
    Z_in = Z0 * (Z_L + Z0 * tanh_gamma_l) / (Z0 + Z_L * tanh_gamma_l)

    return {
        "Z0": Z0,
        "gamma": gamma,
        "alpha": alpha,
        "beta": beta,
        "Gamma": Gamma,
        "VSWR": VSWR,
        "Z_in": Z_in,
    }

# Typical 50-Ω coax parameters at 2 GHz
L_coax = 2.5e-7   # H/m (~250 nH/m)
C_coax = 1.0e-10  # F/m (~100 pF/m)
Z0_check = np.sqrt(L_coax / C_coax)
freq_d1 = 2.0e9

# Load cases
loads = [
    ("Matched load", 50.0 + 0j),
    ("Short circuit", 0.0 + 0j),
    ("Open circuit", 1e10 + 0j),
    ("1/4-wave transform", 100.0 + 0j),
    ("General mismatch", 25.0 + 20j),
]

# Line length: λ/4 at 2 GHz on this transmission line
# v_p = 1/sqrt(LC), λ_line = v_p/f
vp_line = 1.0 / np.sqrt(L_coax * C_coax)
lam_line = vp_line / freq_d1
lam_fs = C0 / freq_d1
ell_qw = lam_line / 4.0

print(f"\nLine: Z0 = {Z0_check:.1f} Ω,  L = {L_coax*1e6:.2f} μH/m,  "
      f"C = {C_coax*1e12:.1f} pF/m")
print(f"f = {freq_d1/1e9:.2f} GHz")
print(f"  Free-space λ = {lam_fs*100:.2f} cm")
print(f"  Line λ = v_p/f = {lam_line*100:.2f} cm  (v_p = {vp_line:.2e} m/s)")
print(f"  ℓ = λ/4 = {ell_qw*100:.2f} cm")
print(f"\n{'Load Case':<25}  {'Z_L [Ω]':<18}  {'Γ':<18}  {'VSWR':<8}  "
      f"{'Z_in [Ω]':<18}")
print("-" * 90)

for label, ZL in loads:
    r = terminated_line(freq_d1, L_coax, C_coax, ZL, ell_qw)
    print(f"{label:<25}  {ZL.real:>7.1f}{ZL.imag:>+6.1f}j  "
          f"{r['Gamma'].real:>7.4f}{r['Gamma'].imag:>+7.4f}j  "
          f"{r['VSWR']:<8.3f}  "
          f"{r['Z_in'].real:>7.1f}{r['Z_in'].imag:>+6.1f}j")

# Verify λ/4 transformer match
print(f"\n--- λ/4 Transformer Verification (§3.1, pp. 82–84) ---")
ZL_match = 100.0
Z0T = np.sqrt(50.0 * ZL_match)
print(f"To match Z_L = {ZL_match:.0f} Ω to Z_S = 50 Ω:")
print(f"  Required Z0,T = sqrt({50} × {ZL_match:.0f}) = {Z0T:.2f} Ω")
r_qw = terminated_line(freq_d1, L_coax, C_coax, ZL_match + 0j, ell_qw)
print(f"  Z_in after λ/4 section = {r_qw['Z_in'].real:.2f} Ω  "
      f"(should be 50.00 Ω — actual Z0 line needed for match)")
print(f"  Using Z0_line = {Z0T:.2f} Ω gives exact match at ℓ = λ/4")


# =============================================================
# Demo 2: Rectangular Waveguide TE₁₀ mode (§3.3)
# =============================================================
print("\n" + "=" * 72)
print("Demo 2: Rectangular Waveguide — TE₁₀ Mode (§3.3, pp. 108–123)")
print("=" * 72)

# Standard X-band waveguide: WR-90 (a = 2.286 cm, b = 1.016 cm)
a_wg = 22.86e-3   # m
b_wg = 10.16e-3   # m

# TE10 cutoff
fc_TE10 = C0 / (2.0 * a_wg)
print(f"\nWaveguide WR-90: a = {a_wg*1e3:.3f} mm, b = {b_wg*1e3:.3f} mm")
print(f"TE₁₀ cutoff frequency f_c = c/(2a) = {fc_TE10/1e9:.3f} GHz")

# Mode cutoff table (first few modes)
print(f"\nMode Cutoff Frequencies for WR-90:")
print(f"{'Mode':<10}  {'m':>3}  {'n':>3}  {'f_c [GHz]':>12}")
print("-" * 32)
modes = [(1,0), (2,0), (0,1), (1,1), (2,1), (3,0)]
for m, n in modes:
    if m == 0 and n == 0:
        continue
    fc = C0 / 2.0 * np.sqrt((m/a_wg)**2 + (n/b_wg)**2)
    print(f"{'TE' + str(m) + str(n):<10}  {m:>3}  {n:>3}  {fc/1e9:>12.3f}")

# TE10 field at 10 GHz
f_wg = 10.0e9
k0 = 2.0 * np.pi * f_wg / C0
kc = np.pi / a_wg  # TE10 cutoff wavenumber
beta_g = np.sqrt(k0**2 - kc**2) if f_wg > fc_TE10 else 0
lam_g = 2.0 * np.pi / beta_g
vp = C0 / np.sqrt(1.0 - (fc_TE10 / f_wg)**2)
vg = C0 * np.sqrt(1.0 - (fc_TE10 / f_wg)**2)

print(f"\nTE₁₀ at f = {f_wg/1e9:.1f} GHz:")
print(f"  Propagation constant β = {beta_g:.2f} rad/m")
print(f"  Guide wavelength λ_g = {lam_g*100:.2f} cm  (free-space λ = {C0/f_wg*100:.2f} cm)")
print(f"  Phase velocity v_p = {vp/C0:.4f} × c  ({vp:.2e} m/s)")
print(f"  Group velocity v_g = {vg/C0:.4f} × c  ({vg:.2e} m/s)")
print(f"  Wave impedance Z_TE = {ETA0 * k0 / beta_g:.1f} Ω")

# Field distribution across waveguide cross-section
x_pts = np.linspace(0, a_wg, 7)
y_pt = b_wg / 2  # center of narrow wall
H0 = 1.0  # normalization

Ey_mag = [np.abs(np.sin(np.pi * x / a_wg)) for x in x_pts]
print(f"\n  Normalized |E_y| across waveguide width (y = b/2):")
print(f"  x/a:  ", end="")
for x in x_pts:
    print(f"  {x/a_wg:.3f}", end="  ")
print()
print(f"  |E_y|: ", end="")
for val in Ey_mag:
    print(f"  {val:.3f}", end="    ")
print()


# =============================================================
# Demo 3: Coax Attenuation vs Frequency (§3.2, pp. 99–103)
# =============================================================
print("\n" + "=" * 72)
print("Demo 3: Coaxial Line Attenuation vs Frequency (§3.2)")
print("=" * 72)

# Standard RG-58 coax parameters
a_coax = 0.45e-3     # inner conductor radius [m]
b_coax = 1.475e-3    # outer conductor radius [m]
er_coax = 2.3         # PTFE dielectric
tand_coax = 0.0002    # loss tangent
sigma_coax = 5.8e7    # copper conductivity [S/m]

Z0_coax = 60.0 / np.sqrt(er_coax) * np.log(b_coax / a_coax)
print(f"\nCoax: a = {a_coax*1e3:.3f} mm, b = {b_coax*1e3:.3f} mm")
print(f"  ε_r = {er_coax}, tan δ = {tand_coax}")
print(f"  Theoretical Z₀ = {Z0_coax:.1f} Ω")

freqs_coax = np.logspace(7, 11, 20)  # 10 MHz to 100 GHz

print(f"\n{'f [GHz]':>10}  {'α_c [dB/m]':>12}  {'α_d [dB/m]':>12}  "
      f"{'α_total [dB/m]':>15}  {'δ_s [μm]':>10}")
print("-" * 62)

# Conversion: α [Np/m] to α [dB/m] = α * 20 * log10(e) = α * 8.686
Np_to_dB = 20.0 * np.log10(np.e)

for f in freqs_coax:
    omega = 2.0 * np.pi * f
    # Skin depth
    delta_s = 1.0 / np.sqrt(np.pi * f * MU0 * sigma_coax)
    # Surface resistance
    Rs = 1.0 / (sigma_coax * delta_s)

    # Conductor attenuation [Np/m] (Eq. 3.73)
    alpha_c = Rs / (2.0 * Z0_coax) * (1.0 / a_coax + 1.0 / b_coax)

    # Dielectric attenuation [Np/m]
    alpha_d = np.pi * f * np.sqrt(er_coax) * tand_coax / C0

    # Total in dB/m
    alpha_c_dB = alpha_c * Np_to_dB
    alpha_d_dB = alpha_d * Np_to_dB
    alpha_total_dB = (alpha_c + alpha_d) * Np_to_dB

    print(f"{f/1e9:>10.3f}  {alpha_c_dB:>12.4f}  {alpha_d_dB:>12.6f}  "
          f"{alpha_total_dB:>15.4f}  {delta_s*1e6:>10.3f}")

# Optimal b/a ratio for minimum α_c (b/a ≈ 3.59 for air-filled)
ratio_opt = np.exp(1.0 / 3.0 + (a_coax / b_coax))  # approximate
print(f"\n  Note: Minimum conductor loss occurs when b/a ≈ 3.59 "
      f"(here b/a = {b_coax/a_coax:.3f})")


# =============================================================
# Demo 4: Rectangular Waveguide Dispersion (§3.3, pp. 116–119)
# =============================================================
print("\n" + "=" * 72)
print("Demo 4: Rectangular Waveguide Dispersion Curves (§3.3)")
print("=" * 72)

# WR-90 waveguide
freqs_disp = np.linspace(fc_TE10 * 1.01, fc_TE10 * 3.0, 50)

beta_vals = []
lam_g_vals = []
vp_vals = []
vg_vals = []

for f in freqs_disp:
    k = 2.0 * np.pi * f / C0
    beta = np.sqrt(k**2 - kc**2)
    beta_vals.append(beta)
    lam_g_vals.append(2.0 * np.pi / beta)
    vp_vals.append(C0 / np.sqrt(1.0 - (fc_TE10/f)**2))
    vg_vals.append(C0 * np.sqrt(1.0 - (fc_TE10/f)**2))

# Print at selected frequencies
print(f"\nWaveguide: WR-90, f_c(TE₁₀) = {fc_TE10/1e9:.3f} GHz")
print(f"\n{'f/f_c':>8}  {'f [GHz]':>10}  {'β [rad/m]':>12}  "
      f"{'λ_g [cm]':>10}  {'v_p/c':>8}  {'v_g/c':>8}")
print("-" * 62)

select_f = np.array([1.1, 1.25, 1.5, 2.0, 2.5, 3.0]) * fc_TE10
for f in select_f:
    k = 2.0 * np.pi * f / C0
    beta = np.sqrt(k**2 - kc**2)
    lam_g = 2.0 * np.pi / beta
    vp_c = C0 / np.sqrt(1.0 - (fc_TE10/f)**2) / C0
    vg_c = C0 * np.sqrt(1.0 - (fc_TE10/f)**2) / C0
    print(f"{f/fc_TE10:>8.3f}  {f/1e9:>10.3f}  {beta:>12.3f}  "
          f"{lam_g*100:>10.2f}  {vp_c:>8.4f}  {vg_c:>8.4f}")

print()
print("Dispersion characteristics:")
print("  • Near cutoff: v_p → ∞, v_g → 0 (no power propagation)")
print("  • Far above cutoff: v_p → c, v_g → c (TEM-like)")
print("  • λ_g > λ (guide wavelength exceeds free-space wavelength)")


# =============================================================
# Demo 5: Microstrip Z₀ vs w/h (§3.6, pp. 134–137)
# =============================================================
print("\n" + "=" * 72)
print("Demo 5: Microstrip Characteristic Impedance vs w/h (§3.6)")
print("=" * 72)

def microstrip_Z0(w_over_h, epsilon_r):
    """
    Compute microstrip characteristic impedance.

    Uses the closed-form expressions from §3.6 (pp. 135–137).

    Parameters
    ----------
    w_over_h : float — strip width / substrate height ratio
    epsilon_r : float — substrate relative permittivity

    Returns
    -------
    (Z0, eps_eff) tuple
    """
    # Effective dielectric constant (p. 135)
    eps_eff = (epsilon_r + 1.0) / 2.0 + (epsilon_r - 1.0) / 2.0 \
              * 1.0 / np.sqrt(1.0 + 12.0 / w_over_h)

    if w_over_h <= 1.0:
        Z0 = 60.0 / np.sqrt(eps_eff) * np.log(8.0 / w_over_h + w_over_h / 4.0)
    else:
        Z0 = 120.0 * np.pi / np.sqrt(eps_eff) \
             / (w_over_h + 1.393 + 0.667 * np.log(w_over_h + 1.444))

    return Z0, eps_eff

# Substrates
substrates = {
    "Alumina (99.6%)": 9.8,
    "FR4": 4.5,
    "RT/Duroid 5880": 2.2,
    "RT/Duroid 6010": 10.2,
}

w_over_h_vals = np.logspace(-1, 1, 30)  # 0.1 to 10

print(f"\n{'Substrate':<22}  {'w/h':>5}  {'Z₀ [Ω]':>10}  {'ε_eff':>8}")
print("-" * 50)

for sub_name, er in substrates.items():
    for wh in [0.2, 0.5, 1.0, 2.0, 5.0]:
        Z0_ms, eps_eff = microstrip_Z0(wh, er)
        print(f"{sub_name:<22}  {wh:>5.2f}  {Z0_ms:>10.2f}  {eps_eff:>8.4f}")

# Show eps_eff vs w/h for common substrates
print(f"\nε_eff vs w/h (for RT/Duroid 5880, ε_r = 2.2):")
print(f"{'w/h':>8}  {'ε_eff':>8}  {'Z₀ [Ω]':>10}")
print("-" * 30)
er_5880 = 2.2
for wh in [0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]:
    Z0_ms, eps_eff = microstrip_Z0(wh, er_5880)
    print(f"{wh:>8.2f}  {eps_eff:>8.4f}  {Z0_ms:>10.2f}")

print(f"\n  ε_eff ranges from ~{(er_5880+1)/2:.2f} (wide strip, mostly in substrate)")
print(f"  to ~{(er_5880+1)/2:.2f} + {(er_5880-1)/2:.2f} = {er_5880:.2f} "
      f"(narrow strip: all field in substrate)")
print(f"  Note: Microstrip supports quasi-TEM mode, not pure TEM (§3.6, p. 134)")


# =============================================================
# Verify Ch.3
# =============================================================
def verify_collins_ch03():
    """Self-check: verify key numerical values from Collin Ch.3."""
    errors = []

    # Demo 1: Lossless 50-Ω line, matched load → VSWR = 1
    r1 = terminated_line(2e9, L_coax, C_coax, 50.0+0j, 0.1)
    if abs(r1["VSWR"] - 1.0) > 1e-6:
        errors.append(f"Matched load VSWR = {r1['VSWR']}, expected 1.0")

    # Demo 1: Short circuit, λ/4 at free-space = 3.75 cm
    # On this line λ_line = 1/(f*sqrt(LC)) = 10 cm, so ℓ=3.75 cm is actually 0.375 λ
    # ℓ=2.5 cm (= λ/4 on this line) gives high impedance
    ell_actual_qw = 1.0 / (2e9 * np.sqrt(L_coax * C_coax)) / 4.0  # λ/4 on this line
    r_sc = terminated_line(2e9, L_coax, C_coax, 0.0+0j, ell_actual_qw)
    if abs(r_sc["Z_in"]) < 1e4:
        errors.append(f"SC λ/4 Z_in magnitude = {abs(r_sc['Z_in']):.1f}, expected >> 10⁴")

    # Demo 2: WR-90 TE10 cutoff ~6.557 GHz (c/(2a) with a=22.86mm)
    fc_expected = C0 / (2.0 * 22.86e-3)
    if not np.isclose(fc_TE10, fc_expected, rtol=1e-6):
        errors.append(f"WR-90 TE10 fc = {fc_TE10/1e9:.3f} GHz, expected {fc_expected/1e9:.3f} GHz")

    # Demo 2: TE10 at 10 GHz, β should be ~158 rad/m
    k0 = 2.0 * np.pi * 10e9 / C0
    kc = np.pi / 22.86e-3
    beta_expected = np.sqrt(k0**2 - kc**2)
    if not np.isclose(beta_g, beta_expected, rtol=1e-3):
        errors.append(f"TE10 β at 10 GHz = {beta_g:.2f}, expected {beta_expected:.2f} rad/m")

    # Demo 3: Coax Z0 should be ~50 Ω
    if not np.isclose(Z0_coax, 50.0, rtol=0.3):
        errors.append(f"Coax Z0 = {Z0_coax:.1f} Ω, expected ~50 Ω")

    # Demo 5: Microstrip Z0 for w/h=1, ε_r=4.5 should be ~70 Ω (Collin §3.6)
    Z0_test, _ = microstrip_Z0(1.0, 4.5)
    if not np.isclose(Z0_test, 70.4, rtol=0.05):
        errors.append(f"Microstrip Z0(w/h=1, εr=4.5) = {Z0_test:.1f} Ω, expected ~70.4 Ω")

    if errors:
        print("\n❌ VERIFY FAILED:")
        for e in errors:
            print(f"   {e}")
        return False
    else:
        print("\n✅ VERIFY: All Ch.3 numerical checks passed.")
        return True

verify_collins_ch03()
print("\n✅ Collins Ch.3 examples complete.")
