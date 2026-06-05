#!/usr/bin/env python3
"""
bogatin_ch1_examples.py — Chapter 1: Signal Integrity Is in Your Future

Concepts demonstrated:
  1. Rise time vs. clock frequency (Eq. 1-1)
  2. Loop self-inductance approximation (Eq. 1-2) vs. measured data
  3. Reflection coefficient / impedance extraction (S11 -> Z)
  4. Intel processor clock frequency trend (historical data)
  5. PDN target impedance trend

All physical variables use meaningful SI-inspired names.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
import os

# Output directory for figures
FIGURE_DIR = "/home/ubuntu/.openclaw/workspace/textbooks/bogatin/figures"
os.makedirs(FIGURE_DIR, exist_ok=True)

# ============================================================
# Example 1: Rise Time vs. Clock Frequency (Eq. 1-1)
# ============================================================
def rise_time_vs_clock():
    """
    RT ~ 1 / (10 * F_clock)
    where RT in nsec, F_clock in GHz.
    """
    f_clock_mhz = np.logspace(1, 4, 100)       # 10 MHz to 10 GHz
    f_clock_ghz = f_clock_mhz / 1000.0
    rise_time_nsec = 1.0 / (10.0 * f_clock_ghz)

    # Markers for known data points
    known_freqs_mhz = np.array([10, 50, 100, 200, 500, 1000, 5000, 10000])
    known_freqs_ghz = known_freqs_mhz / 1000.0
    known_rt_nsec   = 1.0 / (10.0 * known_freqs_ghz)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.loglog(f_clock_mhz, rise_time_nsec, 'b-', linewidth=2, label=r'$RT \approx 1/(10 \cdot F_{clock})$')
    ax.scatter(known_freqs_mhz, known_rt_nsec, color='red', zorder=5, label='Key data points')
    ax.axhline(y=1, color='gray', linestyle='--', alpha=0.5, label='SI threshold (1 ns)')
    ax.axvline(x=100, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('Clock Frequency (MHz)')
    ax.set_ylabel('Rise Time (nsec)')
    ax.set_title('Figure 1-16: Rise Time vs. Clock Frequency')
    ax.grid(True, which='both', alpha=0.3)
    ax.legend()
    ax.set_xlim(8, 12000)
    ax.set_ylim(0.008, 20)

    # Annotate typical regimes
    ax.annotate('SI problems\ntypically arise', xy=(120, 0.8),
                xytext=(300, 3), fontsize=10,
                arrowprops=dict(arrowstyle='->', color='gray'))
    ax.annotate('1 nsec', xy=(95, 1.1), fontsize=9, color='gray')

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch1_rise_time_vs_clock.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch1_rise_time_vs_clock.png"), dpi=150)
    plt.close(fig)
    print("[Example 1] Rise time vs. clock frequency plot saved.")

    # Print a few values
    print(f"\n  F_clock =  10 MHz  -> RT = {1.0/(10*0.010):.2f} nsec")
    print(f"  F_clock = 100 MHz  -> RT = {1.0/(10*0.100):.2f} nsec")
    print(f"  F_clock =   1 GHz  -> RT = {1.0/(10*1.000):.2f} nsec")
    print(f"  F_clock =  10 GHz  -> RT = {1.0/(10*10.00):.2f} nsec")

    return f_clock_mhz, rise_time_nsec


# ============================================================
# Example 2: Loop Self-Inductance Approximation (Eq. 1-2)
# ============================================================
def loop_inductance_approximation(radius_inches, wire_diameter_inches):
    """
    L_self ≈ 32 * R * ln(4R/D)   [nH]
    radius R in inches, wire diameter D in inches.
    Verified to ~2% accuracy against measurements (Fig 1-22).
    """
    R = radius_inches
    D = wire_diameter_inches
    # Protect against unrealistic aspect ratios
    ratio = 4.0 * R / D
    ratio = np.clip(ratio, 1.1, None)
    L_nH = 32.0 * R * np.log(ratio)
    return L_nH


def loop_inductance_demo():
    """
    Replicate Fig 1-22: loop inductance vs. radius.
    Wire diameter fixed at 10 mil (0.010 inch) as in text example.
    """
    wire_diam = 0.010  # inches (10 mil)
    radii = np.linspace(0.05, 1.0, 50)  # 0.05 to 1.0 inch radius
    L_calc = loop_inductance_approximation(radii, wire_diam)

    # "Measured" data points (approximated from Fig 1-22 trend)
    radii_meas = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    L_meas = loop_inductance_approximation(radii_meas, wire_diam) * (1 + 0.02 * np.random.randn(len(radii_meas)))

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(radii, L_calc, 'b-', linewidth=2, label='Approximation: $L = 32R\\ln(4R/D)$')
    ax.scatter(radii_meas, L_meas, color='red', marker='s', zorder=5, label='"Measured" (simulated ±2%)')
    ax.set_xlabel('Loop Radius (inches)')
    ax.set_ylabel('Loop Inductance (nH)')
    ax.set_title('Figure 1-22: Loop Inductance vs. Radius')
    ax.grid(True, alpha=0.3)
    ax.legend()

    # Annotate the 0.5 inch radius example from the text
    R_ex = 0.5
    L_ex = loop_inductance_approximation(R_ex, wire_diam)
    ax.annotate(f'R={R_ex} in → L≈{L_ex:.0f} nH', xy=(R_ex, L_ex),
                xytext=(0.6, L_ex + 30),
                arrowprops=dict(arrowstyle='->', color='gray'), fontsize=10)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch1_loop_inductance.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch1_loop_inductance.png"), dpi=150)
    plt.close(fig)
    print("\n[Example 2] Loop inductance approximation plot saved.")
    print(f"  Example: R=0.5 in, D=10 mil → L ≈ {L_ex:.1f} nH")
    return radii, L_calc


# ============================================================
# Example 3: Reflection Coefficient & Impedance Extraction
# ============================================================
def reflection_coefficient_demo():
    """
    Gamma = (Z_DUT - Z0) / (Z_DUT + Z0)   where Z0 = 50 Ohm
    Show how S11 relates to Z_DUT.
    """
    Z0 = 50.0  # Ohms
    z_dut = np.linspace(1, 200, 500)  # DUT impedance from 1 to 200 Ohm
    gamma = (z_dut - Z0) / (z_dut + Z0)
    z_from_gamma = Z0 * (1 + gamma) / (1 - gamma)  # inverse

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

    # Left: S11 vs Z_DUT
    ax1.plot(z_dut, np.abs(gamma), 'b-', linewidth=2)
    ax1.axvline(x=Z0, color='gray', linestyle='--', alpha=0.5, label=f'Z0 = {Z0} Ω')
    ax1.set_xlabel('$Z_{DUT}$ (Ohms)')
    ax1.set_ylabel('$|S_{11}| = |\\Gamma|$')
    ax1.set_title('Reflection Coefficient Magnitude')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_xlim(0, 200)
    ax1.set_ylim(0, 1.05)

    # Right: Z extraction verification
    ax2.plot(z_dut, z_from_gamma, 'r-', linewidth=2, label='Extracted $Z_{DUT}$')
    ax2.plot(z_dut, z_dut, 'k--', linewidth=1, label='Ideal $Z_{DUT}$ (identity)')
    ax2.set_xlabel('True $Z_{DUT}$ (Ohms)')
    ax2.set_ylabel('Extracted $Z_{DUT}$ (Ohms)')
    ax2.set_title('Impedance Extraction Validation')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_xlim(0, 200)
    ax2.set_ylim(0, 200)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch1_reflection_coefficient.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch1_reflection_coefficient.png"), dpi=150)
    plt.close(fig)
    print("\n[Example 3] Reflection coefficient plots saved.")

    # Key points
    for Z in [25, 50, 75, 100]:
        g = (Z - 50) / (Z + 50)
        print(f"  Z_DUT = {Z:3d} Ω → Gamma = {g:+.3f}")

    return z_dut, gamma


# ============================================================
# Example 4: Intel Processor Clock Frequency Trend
# ============================================================
def intel_clock_trend():
    """
    Replicate Fig 1-13: Intel processor clock frequency trend.
    Also show SIA roadmap projection (Fig 1-14).
    Data approximate from Bogatin's figures.
    """
    years_intel = np.array([1971, 1974, 1978, 1982, 1985, 1989, 1993,
                            1995, 1997, 1999, 2000, 2001, 2002, 2003])
    clock_mhz = np.array([0.108, 2, 5, 6, 8, 16, 25,
                          66, 200, 500, 1000, 1700, 2200, 3200])

    # SIA roadmap projected frequencies (Fig 1-14, post-2000)
    years_sia = np.array([2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015])
    sia_clock_mhz = np.array([1700, 3500, 5000, 6500, 9000, 12000, 16000, 22000])

    # Double-every-2-years reference
    t_double = np.linspace(1971, 2005, 200)
    f_double = 0.108 * 2**((t_double - 1971) / 2.0)

    fig, ax = plt.subplots(figsize=(9, 5.5))

    ax.semilogy(years_intel, clock_mhz, 'bo-', linewidth=2, markersize=5, label='Intel Processors')
    ax.semilogy(t_double, f_double, '--', color='gray', alpha=0.6,
                label='Doubling every 2 years')
    ax.semilogy(years_sia, sia_clock_mhz, 'rs--', linewidth=2, markersize=5,
                label='SIA Roadmap')

    ax.set_xlabel('Year')
    ax.set_ylabel('Clock Frequency (MHz)')
    ax.set_title('Figures 1-13 & 1-14: Clock Frequency Trends')
    ax.grid(True, which='both', alpha=0.3)
    ax.legend()
    ax.set_xlim(1970, 2016)
    ax.set_ylim(0.05, 50000)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch1_intel_clock_trend.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch1_intel_clock_trend.png"), dpi=150)
    plt.close(fig)
    print("\n[Example 4] Intel clock frequency trend plot saved.")

    return years_intel, clock_mhz


# ============================================================
# Example 5: PDN Target Impedance Trend (Fig 1-10)
# ============================================================
def pdn_target_impedance_trend():
    """
    Estimate from Fig 1-10: Sun Microsystems' maximum allowable
    PDN impedance for high-end processors.
    """
    years = np.array([1992, 1994, 1996, 1998, 2000, 2002, 2004])
    z_pdn_ohm = np.array([0.1, 0.04, 0.02, 0.01, 0.005, 0.003, 0.001])

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogy(years, z_pdn_ohm, 'g^-', linewidth=2, markersize=8)
    ax.set_xlabel('Year')
    ax.set_ylabel('Maximum PDN Impedance (Ohms)')
    ax.set_title('Figure 1-10: PDN Target Impedance Trend (Sun Microsystems)')
    ax.grid(True, which='both', alpha=0.3)
    ax.set_xlim(1990, 2006)
    ax.set_ylim(0.0005, 0.5)

    # Annotate 10x per 6 years trend
    ax.annotate('~10× decrease\nper 6 years', xy=(2000, 0.005),
                xytext=(1993, 0.08), fontsize=10,
                arrowprops=dict(arrowstyle='->', color='gray'))

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch1_pdn_impedance_trend.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch1_pdn_impedance_trend.png"), dpi=150)
    plt.close(fig)
    print("\n[Example 5] PDN target impedance trend plot saved.")

    for yr, z in zip(years, z_pdn_ohm):
        print(f"  {yr}: Z_max = {z:.4f} Ω")

    return years, z_pdn_ohm


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Bogatin SI/PI 2nd Ed. — Chapter 1 Examples")
    print("=" * 60)

    # Example 1
    rise_time_vs_clock()

    # Example 2
    loop_inductance_demo()

    # Example 3
    reflection_coefficient_demo()

    # Example 4
    intel_clock_trend()

    # Example 5
    pdn_target_impedance_trend()

    print("\n" + "=" * 60)
    print("All Chapter 1 examples complete.")
    print("=" * 60)
