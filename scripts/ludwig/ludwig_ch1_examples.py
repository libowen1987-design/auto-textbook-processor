#!/usr/bin/env python3
"""
ludwig_ch1_examples.py — Chapter 1: Introduction
RF Circuit Design, 2nd Ed., Ludwig & Bogdanov

Examples covered:
  Ex1-1: Intrinsic impedance, phase velocity, wavelength
  Ex1-2: AWG wire diameter to metric conversion
  Ex1-3: RF impedance of a 500 Ω metal-film resistor
  Ex1-4: RF impedance of a 47 pF capacitor
  Ex1-5: RF impedance of an RFC (air-core coil)

Author: Subagent (Ludwig digitization pipeline)
Dependencies: numpy, scipy, matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as const

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'legend.fontsize': 10,
    'figure.dpi': 120,
})

FIGS_DIR = '/home/ubuntu/.openclaw/workspace/textbooks/ludwig/figures'

# ──────────────────────────────────────────────────────
# Physical constants
# ──────────────────────────────────────────────────────
mu0 = const.mu_0          # 4π × 1e-7 H/m
eps0 = const.epsilon_0    # 8.854e-12 F/m
c0 = const.c              # speed of light


# ======================================================================
# Example 1-1: Intrinsic impedance, phase velocity, wavelengths
# ======================================================================
def example_1_1():
    """
    Compute intrinsic wave impedance, phase velocity, and wavelength
    in free space for f = 30 MHz, 300 MHz, 30 GHz.
    """
    print("=" * 60)
    print("Example 1-1: Intrinsic impedance, phase velocity, wavelengths")
    print("=" * 60)

    frequencies = np.array([30e6, 300e6, 30e9])  # Hz
    labels = ['30 MHz', '300 MHz', '30 GHz']

    # Free space → μr = 1, εr = 1
    mu_r = 1.0
    eps_r = 1.0
    Z0_free = np.sqrt(mu0 * mu_r / (eps0 * eps_r))
    vp_free = 1.0 / np.sqrt(mu0 * mu_r * eps0 * eps_r)

    print(f"\nFree-space intrinsic impedance Z0 = {Z0_free:.1f} Ω")
    print(f"Free-space phase velocity vp = {vp_free:.3e} m/s (≈ c)\n")

    wavelengths = vp_free / frequencies
    for f_label, f_val, lam in zip(labels, frequencies, wavelengths):
        print(f"  f = {f_label:>10s} → λ = {lam:.4e} m = {lam:.4f} m")

    # Table output
    print("\n  Frequency   | Wavelength")
    print("  ------------+-----------")
    for f_label, lam in zip(labels, wavelengths):
        unit = 'm' if lam >= 1 else 'cm'
        val = lam if lam >= 1 else lam * 100
        print(f"  {f_label:>10s} | {val:.4g} {unit}")

    return Z0_free, vp_free, frequencies, wavelengths


# ======================================================================
# Example 1-2: AWG wire diameter
# ======================================================================
def example_1_2():
    """
    Determine radius of AWG 26 wire given AWG 50 diameter = 1 mil.
    Rule: diameter doubles every 6 gauges.
    """
    print("\n" + "=" * 60)
    print("Example 1-2: AWG wire diameter conversion")
    print("=" * 60)

    gauge_start = 50
    d_start_mil = 1.0  # mil
    gauge_target = 26

    # Number of 6-gauge steps from 50 to 26
    num_steps = (gauge_start - gauge_target) // 6
    d_target_mil = d_start_mil * (2 ** num_steps)

    mil_to_mm = 0.0254  # 1 mil = 0.0254 mm
    d_target_mm = d_target_mil * mil_to_mm
    r_target_mm = d_target_mm / 2.0
    r_target_m = r_target_mm * 1e-3

    print(f"\n  AWG {gauge_target}:")
    print(f"    Diameter = {d_target_mil} mil")
    print(f"    Diameter = {d_target_mm:.4f} mm")
    print(f"    Radius   = {r_target_mm:.4f} mm")
    print(f"    Radius   = {r_target_m:.4e} m")

    return r_target_m


# ======================================================================
# Helper: skin depth
# ======================================================================
def skin_depth(f, sigma):
    """Skin depth δ = 1 / sqrt(π f μ0 σ)  [m]."""
    return 1.0 / np.sqrt(np.pi * f * mu0 * sigma)


# ======================================================================
# Example 1-3: RF impedance of a 500 Ω metal-film resistor
# ======================================================================
def example_1_3():
    """
    500 Ω metal-film resistor with:
      - 2.5 cm copper wire leads, AWG 26
      - stray capacitance Ca = 5 pF
    Plot |Z| vs frequency.
    """
    print("\n" + "=" * 60)
    print("Example 1-3: RF impedance of 500 Ω metal-film resistor")
    print("=" * 60)

    sigma_Cu = 64.516e6       # Ω⁻¹·m⁻¹
    R_nominal = 500.0          # Ω
    Ca = 5e-12                 # F (stray capacitance)
    l_lead = 2.5e-2            # m (each lead)
    l_total = 2 * l_lead       # total lead length
    a = 0.2032e-3              # m (AWG 26 radius, from Ex1-2)

    f = np.logspace(3, 11, 2000)  # 1 kHz to 100 GHz

    # Skin depth
    delta = skin_depth(f, sigma_Cu)

    # Validity condition: delta << a
    f_min_valid = 1.0 / (np.pi * mu0 * sigma_Cu * a**2)
    print(f"  Validity threshold (δ << a): f >> {f_min_valid/1e3:.1f} kHz")
    print(f"  At 10 MHz: δ = {np.interp(10e6, f, delta)*1e6:.2f} μm")
    print(f"  At 1 GHz : δ = {np.interp(1e9, f, delta)*1e6:.2f} μm")

    # Lead inductance at high frequency (eqns from text)
    # R_lead ≈ l_total / (σ * 2πaδ)
    R_lead = l_total / (sigma_Cu * 2 * np.pi * a * delta)
    # L_lead ≈ R_lead * (a / (2δ)) / ω  — rewritten from (1.10)
    # Actually: ωL/R_DC ≈ a/(2δ) → L ≈ R_DC * a / (2δ * ω)
    R_DC_lead = l_total / (sigma_Cu * np.pi * a**2)
    L_lead = R_DC_lead * a / (2 * delta * (2 * np.pi * f))  # verified against text method

    # Impedance of circuit (lead R + L in series, then parallel with Ca)
    Z_lead = R_lead + 1j * 2 * np.pi * f * L_lead
    Z_total = 1.0 / (1.0 / (R_nominal + Z_lead) + 1j * 2 * np.pi * f * Ca)
    Z_mag = np.abs(Z_total)

    # ── Plot ──
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.loglog(f, Z_mag, linewidth=2, color='C0')
    ax.axhline(R_nominal, color='gray', linestyle='--', alpha=0.5,
               label=f'$R = {R_nominal}\\,\\Omega$ (DC)')

    # Mark resonance
    idx_min = np.argmin(Z_mag)
    f_res = f[idx_min]
    Z_res = Z_mag[idx_min]
    ax.plot(f_res, Z_res, 'ro', markersize=6)
    f_res_GHz = f_res / 1e9
    ax.annotate(f'$f_{{\\text{{res}}}} \\approx {f_res_GHz:.2f}$ GHz',
                xy=(f_res, Z_res), xytext=(f_res * 2, Z_res * 5),
                arrowprops=dict(arrowstyle='->'), fontsize=10)

    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('$|Z|$  ($\\Omega$)')
    ax.set_title('Ex1-3: Impedance of 500 $\\Omega$ Metal-Film Resistor')
    ax.legend()
    ax.grid(True, which='both', alpha=0.3)
    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch1_resistor_impedance.png', dpi=150)
    print(f"  → Saved figure to {FIGS_DIR}/ch1_resistor_impedance.png")
    plt.close(fig)

    # Key values
    print(f"\n  f_res ≈ {f_res_GHz:.3f} GHz")
    print(f"  |Z| at f_res ≈ {Z_res:.2f} Ω")

    return f, Z_mag


# ======================================================================
# Example 1-4: RF impedance of a 47 pF capacitor
# ======================================================================
def example_1_4():
    """
    47 pF capacitor with:
      - Al₂O₃ dielectric, loss tangent = 1e-4
      - 1.25 cm AWG 26 copper wire leads
    Plot |Z| vs frequency.
    """
    print("\n" + "=" * 60)
    print("Example 1-4: RF impedance of 47 pF capacitor")
    print("=" * 60)

    sigma_Cu = 64.516e6
    C_nom = 47e-12                  # F
    tandelta = 1e-4                 # loss tangent (assumed freq-independent)
    l_lead = 1.25e-2                # m (each lead)
    l_total = 2 * l_lead
    a = 0.2032e-3                   # m (AWG 26 radius)

    f = np.logspace(3, 11, 2000)

    # Skin depth and lead parasitics
    delta = skin_depth(f, sigma_Cu)
    R_DC_lead = l_total / (sigma_Cu * np.pi * a**2)

    # When δ < a, use high-freq approximation
    cond_hf = delta < a
    R_lead = np.where(cond_hf,
                      l_total / (sigma_Cu * 2 * np.pi * a * delta),
                      R_DC_lead * np.ones_like(f))
    L_lead = np.where(cond_hf,
                      R_DC_lead * a / (2 * delta * (2 * np.pi * f)),
                      np.zeros_like(f))

    # Dielectric loss resistance
    G_e = 2 * np.pi * f * C_nom * tandelta
    R_e = 1.0 / G_e

    # Lead impedance
    Z_lead = R_lead + 1j * 2 * np.pi * f * L_lead

    # Total: lead impedance in series with parallel (C || R_e)
    Z_cap = 1.0 / (1j * 2 * np.pi * f * C_nom + 1.0 / R_e)
    Z_total = Z_lead + Z_cap
    Z_mag = np.abs(Z_total)

    # ── Plot ──
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.loglog(f, Z_mag, linewidth=2, color='C1')

    # Ideal capacitor line
    Z_ideal = 1.0 / (2 * np.pi * f * C_nom)
    ax.loglog(f, Z_ideal, '--', color='gray', alpha=0.5,
              label='Ideal $1/(\\omega C)$')

    # Mark resonance
    idx_min = np.argmin(Z_mag)
    f_res = f[idx_min]
    ax.plot(f_res, Z_mag[idx_min], 'ro', markersize=6)
    f_res_GHz = f_res / 1e9
    ax.annotate(f'$f_{{\\text{{res}}}} \\approx {f_res_GHz:.2f}$ GHz',
                xy=(f_res, Z_mag[idx_min]),
                xytext=(f_res * 2, Z_mag[idx_min] * 2),
                arrowprops=dict(arrowstyle='->'), fontsize=10)

    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('$|Z|$  ($\\Omega$)')
    ax.set_title('Ex1-4: Impedance of 47 pF Capacitor')
    ax.legend()
    ax.grid(True, which='both', alpha=0.3)
    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch1_capacitor_impedance.png', dpi=150)
    print(f"  → Saved figure to {FIGS_DIR}/ch1_capacitor_impedance.png")
    plt.close(fig)

    # ESR at 1 MHz
    ESR_1MHz = tandelta / (2 * np.pi * 1e6 * C_nom)
    print(f"\n  ESR @ 1 MHz = {ESR_1MHz:.2f} Ω")
    print(f"  R_e @ 1 MHz = {np.interp(1e6, f, R_e):.2e} Ω")
    print(f"  f_res ≈ {f_res_GHz:.3f} GHz")

    return f, Z_mag


# ======================================================================
# Example 1-5: RF impedance of an RFC (air-core coil)
# ======================================================================
def example_1_5():
    """
    Air-core RFC: N=3.5 turns, AWG 36, 0.1 inch core diameter, 0.05 inch length.
    Plot |Z| vs frequency, compute Q.
    """
    print("\n" + "=" * 60)
    print("Example 1-5: RFC (air-core coil) frequency response")
    print("=" * 60)

    sigma_Cu = 64.516e6
    N = 3.5
    r_coil = 50e-3 * 0.0254      # 50 mil → m
    l_coil = 50e-3 * 0.0254      # 50 mil → m
    a_wire = 2.5e-3 * 0.0254     # AWG 36 → 2.5 mil → m

    f = np.logspace(6, 11, 2000)

    # Inductance: solenoid formula (Eq 1.18, approximate)
    A_core = np.pi * r_coil**2
    L_nominal = mu0 * N**2 * A_core / l_coil
    print(f"  L ≈ {L_nominal*1e9:.1f} nH (solenoid approximation)")

    # Parasitic capacitance: parallel-plate between adjacent turns
    d_turns = l_coil / N          # separation between turns
    l_wire = 2 * np.pi * r_coil * N  # total wire length
    A_plates = l_wire * l_wire    # rough area (text uses 2π * a_wire * l_wire)
    # Following text: A ≈ 2πa_wire * l_wire (area of wire surface)
    A_plates = 2 * np.pi * a_wire * l_wire
    eps_r_air = 1.0
    C_parasitic = eps0 * eps_r_air * A_plates / d_turns
    print(f"  C_parasitic ≈ {C_parasitic*1e12:.2f} pF")

    # Series resistance (DC, since δ >> a_wire at moderate f)
    # Check skin depth relative to wire radius
    delta = skin_depth(f, sigma_Cu)
    R_DC = l_wire / (sigma_Cu * np.pi * a_wire**2)
    print(f"  R_DC = {R_DC:.3f} Ω")
    print(f"  a_wire = {a_wire*1e6:.1f} μm")
    print(f"  δ @ 1 MHz = {np.interp(1e6, f, delta)*1e6:.1f} μm")
    print(f"  δ @ 1 GHz = {np.interp(1e9, f, delta)*1e6:.1f} μm")

    # Use AC resistance when δ < a_wire
    cond_hf = delta < a_wire
    R_s = np.where(cond_hf,
                   l_wire / (sigma_Cu * 2 * np.pi * a_wire * delta),
                   R_DC * np.ones_like(f))

    # Impedance of the inductor model
    # Z = (R_s + jωL) || (1/jωCs)
    Z_L = R_s + 1j * 2 * np.pi * f * L_nominal
    Z_Cs = 1.0 / (1j * 2 * np.pi * f * C_parasitic)
    Z_total = 1.0 / (1.0 / Z_L + 1.0 / Z_Cs)
    Z_mag = np.abs(Z_total)

    # Quality factor (before resonance)
    Q = (2 * np.pi * f * L_nominal) / R_s

    # ── Plot: |Z| ──
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.loglog(f, Z_mag, linewidth=2, color='C2')

    # Ideal inductor line
    Z_ideal = 2 * np.pi * f * L_nominal
    ax.loglog(f, Z_ideal, '--', color='gray', alpha=0.5,
              label=f'Ideal $\\omega L$ ({L_nominal*1e9:.1f} nH)')
    # Ideal capacitor line (parasitic)
    Z_Cs_line = 1.0 / (2 * np.pi * f * C_parasitic)
    ax.loglog(f, Z_Cs_line, ':', color='gray', alpha=0.5,
              label=f'$1/(\\omega C_s)$ ({C_parasitic*1e3:.1f} fF)')

    # Mark peak impedance (self-resonance)
    idx_max = np.argmax(Z_mag)
    f_res = f[idx_max]
    Z_peak = Z_mag[idx_max]
    ax.plot(f_res, Z_peak, 'ro', markersize=6)
    f_res_GHz = f_res / 1e9
    ax.annotate(f'$f_{{\\text{{res}}}} \\approx {f_res_GHz:.2f}$ GHz',
                xy=(f_res, Z_peak), xytext=(f_res * 2, Z_peak / 3),
                arrowprops=dict(arrowstyle='->'), fontsize=10)

    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('$|Z|$  ($\\Omega$)')
    ax.set_title(f'Ex1-5: RFC Impedance ($L={L_nominal*1e9:.1f}$ nH, $N={N}$)')
    ax.legend()
    ax.grid(True, which='both', alpha=0.3)
    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch1_rfc_impedance.png', dpi=150)
    print(f"  → Saved figure to {FIGS_DIR}/ch1_rfc_impedance.png")
    plt.close(fig)

    # ── Plot: Q factor ──
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    # Only plot Q up to resonance
    idx_up_to_res = np.searchsorted(f, f_res)
    ax2.semilogx(f[:idx_up_to_res], Q[:idx_up_to_res],
                 linewidth=2, color='C3')
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('$Q = \\omega L / R_s$')
    ax2.set_title('RFC Quality Factor vs Frequency')
    ax2.grid(True, alpha=0.3)
    fig2.tight_layout()
    fig2.savefig(f'{FIGS_DIR}/ch1_rfc_Q.png', dpi=150)
    print(f"  → Saved figure to {FIGS_DIR}/ch1_rfc_Q.png")
    plt.close(fig2)

    print(f"\n  f_res  ≈ {f_res_GHz:.3f} GHz")
    print(f"  |Z|_peak ≈ {Z_peak:.1f} Ω")
    print(f"  Q @ 100 MHz ≈ {np.interp(100e6, f, Q):.1f}")
    print(f"  Q @ 1 GHz   ≈ {np.interp(1e9, f, Q):.1f}")

    return f, Z_mag, Q


# ======================================================================
# Bonus: Skin depth plot (Fig 1-4 reproduction)
# ======================================================================
def plot_skin_depth():
    """
    Reproduce Fig 1-4: Skin depth vs frequency for Cu, Al, Au.
    """
    print("\n" + "=" * 60)
    print("Bonus: Skin depth vs frequency (Cu, Al, Au)")
    print("=" * 60)

    sigma_Cu = 64.516e6
    sigma_Al = 40.0e6
    sigma_Au = 48.544e6

    f = np.logspace(1, 12, 500)  # 10 Hz to 1 THz

    delta_Cu = skin_depth(f, sigma_Cu)
    delta_Al = skin_depth(f, sigma_Al)
    delta_Au = skin_depth(f, sigma_Au)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.loglog(f, delta_Cu * 1e6, linewidth=2, label='Copper')
    ax.loglog(f, delta_Al * 1e6, linewidth=2, label='Aluminum')
    ax.loglog(f, delta_Au * 1e6, linewidth=2, label='Gold')
    ax.axvline(1e6, color='gray', linestyle='--', alpha=0.3)
    ax.axvline(1e9, color='gray', linestyle='--', alpha=0.3)

    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Skin depth $\\delta$  ($\\mu$m)')
    ax.set_title('Skin Depth vs Frequency for Common Conductors')
    ax.legend()
    ax.grid(True, which='both', alpha=0.3)
    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch1_skin_depth.png', dpi=150)
    print(f"  → Saved figure to {FIGS_DIR}/ch1_skin_depth.png")
    plt.close(fig)

    # Key values
    print(f"\n  δ(Cu) @ 1 MHz = {np.interp(1e6, f, delta_Cu)*1e6:.2f} μm")
    print(f"  δ(Cu) @ 1 GHz = {np.interp(1e9, f, delta_Cu)*1e6:.2f} μm")
    print(f"  δ(Cu) @ 10 GHz = {np.interp(1e10, f, delta_Cu)*1e6:.2f} μm")

    return f, delta_Cu, delta_Al, delta_Au


# ======================================================================
# Main
# ======================================================================
if __name__ == '__main__':
    import os
    os.makedirs(FIGS_DIR, exist_ok=True)

    Z0, vp, freqs, lambdas = example_1_1()
    r_awg26 = example_1_2()
    f3, Z3 = example_1_3()
    f4, Z4 = example_1_4()
    f5, Z5, Q5 = example_1_5()
    f_bonus, dCu, dAl, dAu = plot_skin_depth()

    print("\n" + "=" * 60)
    print("✅ Ch1 all examples complete. All figures saved.")
    print("=" * 60)
