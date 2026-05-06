#!/usr/bin/env python3
"""
bogatin_ch3_examples.py — Chapter 3: Impedance and Electrical Models

Concepts demonstrated:
  1. Impedance of ideal R, C, L elements in frequency domain
  2. Series RLC impedance (magnitude + phase) — decoupling capacitor model
  3. Self-resonant frequency (SRF) extraction
  4. Resistor technology bandwidth comparison (Fig 3-16 concept)
  5. Transmission line model vs. lumped LC model bandwidth
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
import os

FIGURE_DIR = "/home/ubuntu/.openclaw/workspace/textbooks/bogatin/figures"
os.makedirs(FIGURE_DIR, exist_ok=True)

plt.rcParams['figure.dpi'] = 150


# ============================================================
# Example 1: Impedance of Ideal R, C, L vs. Frequency
# ============================================================
def ideal_element_impedance():
    """
    Plot |Z| vs. frequency for ideal R, C, L elements.
    Replicates concept of Fig 3-10 (right panel).
    """
    f = np.logspace(6, 10, 500)  # 1 MHz to 10 GHz
    omega = 2 * np.pi * f

    R_val = 10.0   # Ohms
    C_val = 5e-12  # 5 pF
    L_val = 7e-9   # 7 nH

    Z_R = R_val * np.ones_like(f)
    Z_C = 1.0 / (omega * C_val)
    Z_L = omega * L_val

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.loglog(f, Z_R, 'k-', linewidth=2, label=f'R = {R_val} $\Omega$')
    ax.loglog(f, Z_C, 'b-', linewidth=2, label=f'C = {C_val*1e12:.0f} pF')
    ax.loglog(f, Z_L, 'r-', linewidth=2, label=f'L = {L_val*1e9:.0f} nH')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Impedance $|Z|$ ($\Omega$)')
    ax.set_title('Fig 3-10 Concept: Impedance of Ideal R, C, L Elements')
    ax.grid(True, which='both', alpha=0.3)
    ax.legend()
    ax.set_xlim(1e6, 1e10)
    ax.set_ylim(0.1, 1e4)

    # Annotate slopes
    ax.annotate('$|Z_C| \\propto 1/f$', xy=(3e7, 1e3),
                fontsize=10, color='blue', fontweight='bold')
    ax.annotate('$|Z_L| \\propto f$', xy=(3e9, 1e2),
                fontsize=10, color='red', fontweight='bold')

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch3_ideal_RLC_impedance.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch3_ideal_RLC_impedance.png"))
    plt.close(fig)
    print("[Example 1] Ideal R, C, L impedance plots saved.")

    # Print sample values
    print(f"\n  At 1 GHz:")
    print(f"  Z_R = {np.interp(1e9, f, Z_R):.1f} Ω")
    print(f"  Z_C = {np.interp(1e9, f, Z_C):.3f} Ω")
    print(f"  Z_L = {np.interp(1e9, f, Z_L):.1f} Ω")

    return f, Z_R, Z_C, Z_L


# ============================================================
# Example 2: Series RLC — Decoupling Capacitor Model (Fig 3-11)
# ============================================================
def series_rlc_impedance():
    """
    Compute Z_mag and Z_phase for a series RLC circuit.
    Model for a real decoupling capacitor.
    C = 0.67 nF, R = 0.5 Ohm, L = 1.78 nH
    Replicates Fig 3-8 and Fig 3-11.
    """
    C_val = 0.67e-9   # 0.67 nF
    R_val = 0.5        # Ohms
    L_val = 1.78e-9    # 1.78 nH

    f_min, f_max = 1e6, 5e9  # 1 MHz to 5 GHz, like Fig 3-8
    f = np.logspace(np.log10(f_min), np.log10(f_max), 1000)
    omega = 2 * np.pi * f

    Z_complex = R_val + 1j * omega * L_val + 1.0 / (1j * omega * C_val)
    Z_mag = np.abs(Z_complex)
    Z_phase = np.angle(Z_complex, deg=True)

    # SRF
    f_srf = 1.0 / (2 * np.pi * np.sqrt(L_val * C_val))

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7), sharex=True)

    # Top: magnitude
    ax1.loglog(f, Z_mag, 'b-', linewidth=2, label=f'RLC: C={C_val*1e9:.2f}nF, R={R_val:.2f}$\Omega$, L={L_val*1e9:.2f}nH')
    # Ideal C for comparison
    Z_C_only = 1.0 / (omega * C_val)
    ax1.loglog(f, Z_C_only, '--', color='gray', alpha=0.5, label='Ideal C only')
    # Ideal L for comparison
    Z_L_only = omega * L_val
    ax1.loglog(f, Z_L_only, ':', color='gray', alpha=0.5, label='Ideal L only')

    ax1.axvline(x=f_srf, color='red', linestyle='--', alpha=0.5,
                label=f'SRF = {f_srf/1e6:.1f} MHz')
    ax1.axhline(y=R_val, color='green', linestyle=':', alpha=0.5,
                label=f'R = {R_val} $\Omega$ (min impedance)')

    ax1.set_ylabel('Impedance $|Z|$ ($\Omega$)')
    ax1.set_title('Fig 3-8/3-11: Series RLC — Decoupling Capacitor Model')
    ax1.grid(True, which='both', alpha=0.3)
    ax1.legend(fontsize=8)
    ax1.set_ylim(0.01, 1e4)

    # Bottom: phase
    ax2.semilogx(f, Z_phase, 'r-', linewidth=2)
    ax2.axhline(y=0, color='gray', linestyle=':', alpha=0.5)
    ax2.axhline(y=-90, color='gray', linestyle=':', alpha=0.3)
    ax2.axhline(y=90, color='gray', linestyle=':', alpha=0.3)
    ax2.axvline(x=f_srf, color='red', linestyle='--', alpha=0.5)
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('Phase (degrees)')
    ax2.grid(True, which='both', alpha=0.3)
    ax2.set_ylim(-100, 100)

    # Annotate regions
    ax2.annotate('Capacitive\n($Z \\propto 1/f$)', xy=(5e6, -60),
                 fontsize=9, color='blue', ha='center')
    ax2.annotate('Inductive\n($Z \\propto f$)', xy=(2e9, 60),
                 fontsize=9, color='red', ha='center')

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch3_series_RLC_capacitor.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch3_series_RLC_capacitor.png"))
    plt.close(fig)
    print("[Example 2] Series RLC capacitor model plots saved.")

    print(f"\n  SRF = {f_srf/1e6:.1f} MHz")
    print(f"  |Z| at SRF = {R_val:.3f} Ω (minimum)")
    print(f"  |Z_C| at SRF = {1/(2*np.pi*f_srf*C_val):.3f} Ω")
    print(f"  |Z_L| at SRF = {2*np.pi*f_srf*L_val:.3f} Ω")

    return f, Z_mag, Z_phase, f_srf


# ============================================================
# Example 3: Model Bandwidth — 1st vs 2nd Order (Fig 3-14 concept)
# ============================================================
def model_bandwidth_comparison():
    """
    Compare a 1st-order (single C) and 2nd-order (LC series) model
    against a simulated "real" 1-inch microstrip trace.
    Replicates Fig 3-14 concept.
    """
    f = np.logspace(7, 10, 500)  # 10 MHz to 10 GHz
    omega = 2 * np.pi * f

    # "Real" 1-inch trace: modeled as a short transmission line with Z0=50 Ohms
    # For a very short line, approximate as series LC with small loss
    # Characteristic: C_total ~ 3.3 pF/inch, L_total ~ 8.3 nH/inch
    C_trace = 3.3e-12   # 3.3 pF
    L_trace = 8.3e-9    # 8.3 nH
    R_trace = 0.1       # small loss

    # "Real" impedance
    Z_real = R_trace + 1j * omega * L_trace + 1.0 / (1j * omega * C_trace)
    Z_real_mag = np.abs(Z_real)

    # 1st-order model: just C
    Z_C_model = 1.0 / (1j * omega * C_trace)
    Z_C_mag = np.abs(Z_C_model)

    # 2nd-order model: LC series
    Z_LC_model = 1j * omega * L_trace + 1.0 / (1j * omega * C_trace)
    Z_LC_mag = np.abs(Z_LC_model)

    # Find bandwidths: frequency where model deviates >10% from real
    bw_C_idx = np.argmin(np.abs(Z_C_mag / Z_real_mag - 1.0 - 0.1))
    bw_C = f[bw_C_idx] if bw_C_idx < len(f) else f[-1]

    bw_LC_idx = np.argmin(np.abs(Z_LC_mag / Z_real_mag - 1.0 - 0.1))
    bw_LC = f[bw_LC_idx] if bw_LC_idx < len(f) else f[-1]

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.loglog(f, Z_real_mag, 'k-', linewidth=2.5, label='"Real" 1-inch microstrip')
    ax.loglog(f, Z_C_mag, 'b--', linewidth=2, alpha=0.7,
              label=f'1st-order (C only) — BW ≈ {bw_C/1e6:.0f} MHz')
    ax.loglog(f, Z_LC_mag, 'r--', linewidth=2, alpha=0.7,
              label=f'2nd-order (LC series) — BW ≈ {bw_LC/1e6:.0f} MHz')
    ax.axvline(x=bw_C, color='blue', linestyle=':', alpha=0.5)
    ax.axvline(x=bw_LC, color='red', linestyle=':', alpha=0.5)
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Impedance $|Z|$ ($\Omega$)')
    ax.set_title('Fig 3-14 Concept: Model Bandwidth Comparison')
    ax.grid(True, which='both', alpha=0.3)
    ax.legend(fontsize=9)
    ax.set_xlim(1e7, 1e10)
    ax.set_ylim(1, 1e5)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch3_model_bandwidth.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch3_model_bandwidth.png"))
    plt.close(fig)
    print("[Example 3] Model bandwidth comparison plot saved.")
    print(f"\n  1st-order (C only)  bandwidth: {bw_C/1e6:.0f} MHz")
    print(f"  2nd-order (LC)      bandwidth: {bw_LC/1e6:.0f} MHz")

    return f, Z_real_mag, bw_C, bw_LC


# ============================================================
# Example 4: Self-Resonant Frequency Parametric Sweep
# ============================================================
def srf_parametric_sweep():
    """
    Show how SRF changes with different L and C values.
    SRF = 1 / (2*pi*sqrt(L*C))
    """
    L_values = np.array([0.5, 1.0, 2.0, 5.0])  # nH
    C_values = np.logspace(-1, 1, 50)  # 0.1 nF to 10 nF

    fig, ax = plt.subplots(figsize=(9, 5.5))

    colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(L_values)))
    for idx, L_nH in enumerate(L_values):
        L_H = L_nH * 1e-9
        f_srf = 1.0 / (2 * np.pi * np.sqrt(L_H * C_values * 1e-9))
        ax.loglog(C_values, f_srf / 1e6, color=colors[idx], linewidth=2,
                  label=f'L = {L_nH:.1f} nH')

    # Annotate typical region for decoupling caps
    ax.fill_between([0.1, 10], [100, 100], [10, 10],
                    color='yellow', alpha=0.15, label='Typical cap range')

    ax.set_xlabel('Capacitance (nF)')
    ax.set_ylabel('Self-Resonant Frequency (MHz)')
    ax.set_title('Self-Resonant Frequency: $f_{SR} = 1/(2\\pi\\sqrt{LC})$')
    ax.grid(True, which='both', alpha=0.3)
    ax.legend(fontsize=9)
    ax.set_xlim(0.08, 12)
    ax.set_ylim(1, 10000)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch3_srf_sweep.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch3_srf_sweep.png"))
    plt.close(fig)
    print("\n[Example 4] SRF parametric sweep plot saved.")

    # Key values
    for L_nH in [0.5, 2.0]:
        f_srf_1nF = 1.0 / (2 * np.pi * np.sqrt(L_nH * 1e-9 * 1e-9))
        print(f"  L = {L_nH:.1f} nH, C = 1 nF => SRF = {f_srf_1nF/1e6:.0f} MHz")

    return L_values, C_values


# ============================================================
# Example 5: Resistor Technology Effect (Fig 3-16 concept)
# ============================================================
def resistor_technology_comparison():
    """
    Compare axial-lead, SMT, and IPD resistor impedance behavior.
    Model each as R + L_parasitic.
    """
    f = np.logspace(6, 10, 500)  # 1 MHz to 10 GHz
    omega = 2 * np.pi * f

    # Nominal R = 50 Ohms
    R_nom = 50.0

    # Parasitic inductance models (approximate from Fig 3-16)
    # Axial lead: ~5 nH, SMT 0805: ~1 nH, IPD: ~0.1 nH
    L_axial = 5.0e-9
    L_smt = 1.0e-9
    L_ipd = 0.1e-9

    Z_axial = np.sqrt(R_nom**2 + (omega * L_axial)**2)
    Z_smt = np.sqrt(R_nom**2 + (omega * L_smt)**2)
    Z_ipd = np.sqrt(R_nom**2 + (omega * L_ipd)**2)

    # Bandwidth: frequency where |Z| exceeds 1.1*R (10% deviation from ideal)
    bw_axial = f[np.argmin(np.abs(Z_axial / R_nom - 1.1))]
    bw_smt = f[np.argmin(np.abs(Z_smt / R_nom - 1.1))]
    bw_ipd = f[np.argmin(np.abs(Z_ipd / R_nom - 1.1))]

    fig, ax = plt.subplots(figsize=(9, 5.5))

    ax.loglog(f, Z_axial, 'r-', linewidth=2, label=f'Axial lead (L≈{L_axial*1e9:.0f}nH) — BW≈{bw_axial/1e6:.0f}MHz')
    ax.loglog(f, Z_smt, 'b-', linewidth=2, label=f'SMT 0805 (L≈{L_smt*1e9:.0f}nH) — BW≈{bw_smt/1e6:.0f}MHz')
    ax.loglog(f, Z_ipd, 'g-', linewidth=2, label=f'IPD (L≈{L_ipd*1e9:.1f}nH) — BW≈{bw_ipd/1e6:.0f}MHz')
    ax.axhline(y=R_nom, color='k', linestyle='--', alpha=0.5, label=f'Ideal R = {R_nom} $\Omega$')

    # Mark bandwidth points
    ax.scatter([bw_axial, bw_smt, bw_ipd],
               [np.interp(bw_axial, f, Z_axial),
                np.interp(bw_smt, f, Z_smt),
                np.interp(bw_ipd, f, Z_ipd)],
               c=['red', 'blue', 'green'], s=60, zorder=5)

    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Impedance $|Z|$ ($\Omega$)')
    ax.set_title('Fig 3-16 Concept: Resistor Technology Bandwidth')
    ax.grid(True, which='both', alpha=0.3)
    ax.legend(fontsize=8)
    ax.set_xlim(1e6, 1e10)
    ax.set_ylim(10, 1000)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch3_resistor_technology.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch3_resistor_technology.png"))
    plt.close(fig)
    print("\n[Example 5] Resistor technology comparison plot saved.")
    print(f"  Axial lead BW:  {bw_axial/1e6:.0f} MHz")
    print(f"  SMT 0805 BW:   {bw_smt/1e6:.0f} MHz")
    print(f"  IPD BW:         {bw_ipd/1e6:.0f} MHz")

    return f, Z_axial, Z_smt, Z_ipd


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Bogatin SI/PI 2nd Ed. — Chapter 3 Examples")
    print("=" * 60)

    # Example 1
    ideal_element_impedance()

    # Example 2
    series_rlc_impedance()

    # Example 3
    model_bandwidth_comparison()

    # Example 4
    srf_parametric_sweep()

    # Example 5
    resistor_technology_comparison()

    print("\n" + "=" * 60)
    print("All Chapter 3 examples complete.")
    print("=" * 60)
