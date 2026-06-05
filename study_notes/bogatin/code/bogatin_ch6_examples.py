#!/usr/bin/env python3
"""
bogatin_ch6_examples.py — Chapter 6: Physical Basis of Inductance

Concepts demonstrated:
  1. Partial self-inductance of a round rod (Eq. 6-6) vs. rule of thumb (25 nH/inch)
  2. Partial mutual inductance vs. spacing (Eq. 6-8, 6-9, Fig 6-8)
  3. Effective inductance and ground bounce (Fig 6-10)
  4. Loop inductance of planes vs. dielectric spacing (Eq. 6-23)
  5. Skin depth vs. frequency in copper
  6. Decoupling capacitor requirements (Eq. 6-21)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
import os

FIGURE_DIR = "/home/ubuntu/.openclaw/workspace/textbooks/bogatin/figures"
os.makedirs(FIGURE_DIR, exist_ok=True)
plt.rcParams['figure.dpi'] = 150


# ============================================================
# Example 1: Partial Self-Inductance of Round Rod (Eq. 6-6)
# ============================================================
def partial_self_inductance():
    """
    L = 5*d*(ln(2*d/r) - 3/4)  [nH]
    d in inches, r in inches
    """
    r = 0.0005  # 1 mil diameter -> 0.5 mil radius
    lengths_inch = np.logspace(-2, 0, 50)  # 0.01 to 1 inch

    L_approx = 5 * lengths_inch * (np.log(2 * lengths_inch / r) - 0.75)
    L_rule = 25 * lengths_inch  # 25 nH/inch

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.loglog(lengths_inch, L_approx, 'b-', linewidth=2, label='Approximation (Eq. 6-6)')
    ax.loglog(lengths_inch, L_rule, 'r--', linewidth=2, label='Rule of thumb: 25 nH/inch')
    ax.set_xlabel('Length (inches)')
    ax.set_ylabel('Partial Self-Inductance (nH)')
    ax.set_title('Fig 6-7: Partial Self-Inductance of Round Rod (1-mil diameter)')
    ax.grid(True, which='both', alpha=0.3)
    ax.legend()
    ax.set_xlim(0.008, 1.2)
    ax.set_ylim(0.001, 50)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch6_partial_self_L.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch6_partial_self_L.png"))
    plt.close(fig)
    print("[Example 1] Partial self-inductance plot saved.")

    # Validate: 1 inch, 0.5 mil radius
    L_1in = 5 * 1.0 * (np.log(2 * 1.0 / 0.0005) - 0.75)
    print(f"\n  1-inch wire (1 mil diam): L ≈ {L_1in:.1f} nH (Eq. 6-6 says ~26 nH)")
    print(f"  Rule of thumb: 25 nH/inch")

    return lengths_inch, L_approx


# ============================================================
# Example 2: Partial Mutual Inductance vs. Spacing (Fig 6-8)
# ============================================================
def partial_mutual_inductance():
    """
    Two rods: d=0.1 inch, r=0.0005 inch (1 mil diam)
    M = 5*d*(ln(2*d/s) - 1 + s/d - (s/2d)^2)  -- second order
    M_simple = 5*d*(ln(2*d/s) - 1)            -- first order
    """
    d = 0.1  # inches (100 mils)
    r = 0.0005  # inches (1 mil diam)
    spacing = np.linspace(0.002, 0.2, 200)  # 2 to 200 mils

    # Second order (Eq. 6-8)
    ratio = 2 * d / spacing
    M_2nd = 5 * d * (np.log(ratio) - 1 + spacing/d - (spacing/(2*d))**2)

    # First order (Eq. 6-9) — valid for s << d
    M_1st = 5 * d * (np.log(ratio) - 1)

    # Rule of thumb: s > d -> M < 10% of self
    L_self = 5 * d * (np.log(2 * d / r) - 0.75)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(spacing * 1000, M_2nd, 'b-', linewidth=2, label='Second-order approximation')
    ax.plot(spacing * 1000, M_1st, 'r--', linewidth=2, alpha=0.7, label='First-order approximation')
    ax.axhline(y=0.1 * L_self, color='gray', linestyle=':', alpha=0.5,
               label=f'10% of self-L = {0.1*L_self:.3f} nH')
    ax.axvline(x=d * 1000, color='green', linestyle=':', alpha=0.5,
               label=f's = d = {d*1000:.0f} mils')

    ax.set_xlabel('Center-to-Center Spacing (mils)')
    ax.set_ylabel('Partial Mutual Inductance (nH)')
    ax.set_title('Fig 6-8: Mutual Inductance of Two 100-mil Wire Bonds')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8)
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 1.2 * M_2nd[0])

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch6_mutual_inductance.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch6_mutual_inductance.png"))
    plt.close(fig)
    print("\n[Example 2] Mutual inductance vs. spacing plot saved.")

    # 5 mil pitch example
    s_5mil = 0.005  # inches
    M_5mil = 5 * d * (np.log(2*d/s_5mil) - 1 + s_5mil/d - (s_5mil/(2*d))**2)
    print(f"\n  s=5 mils: M = {M_5mil:.3f} nH (text: ~1.3 nH)")
    print(f"  s={d*1000:.0f} mils (=d): M = 0.1*L_self = {0.1*L_self:.3f} nH (text: 10% rule)")

    return spacing, M_2nd, M_1st


# ============================================================
# Example 3: Effective Inductance and Ground Bounce (Fig 6-10)
# ============================================================
def effective_inductance_ground_bounce():
    """
    Replicate Fig 6-10: effective inductance of one wire bond
    when adjacent wire carries same or opposite current.
    """
    d = 0.1  # inches (100 mils)
    r = 0.0005  # inches (1 mil diam)
    L_self = 5 * d * (np.log(2 * d / r) - 0.75)

    s_mils = np.linspace(1, 100, 200)
    spacing = s_mils / 1000.0  # inches

    # Mutual inductance at each spacing
    ratio = 2 * d / spacing
    M = 5 * d * (np.log(ratio) - 1 + spacing/d - (spacing/(2*d))**2)

    L_same = L_self + M  # currents in same direction
    L_opposite = L_self - M  # currents in opposite direction

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot(s_mils, L_same, 'r-', linewidth=2, label='Same direction (power+power)')
    ax.plot(s_mils, L_opposite, 'b-', linewidth=2, label='Opposite direction (signal+return)')
    ax.axhline(y=L_self, color='k', linestyle='--', alpha=0.5, label=f'Partial self-L = {L_self:.2f} nH')
    ax.plot(s_mils, M, 'g:', linewidth=1.5, alpha=0.7, label='Mutual inductance M')

    ax.set_xlabel('Center-to-Center Spacing (mils)')
    ax.set_ylabel('Effective Inductance (nH)')
    ax.set_title('Fig 6-10: Effective Inductance of 100-mil Wire Bond')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 5)

    # Ground bounce calculation
    I_switch = 0.1  # 100 mA
    dt = 1e-9  # 1 nsec
    dIdt = I_switch / dt
    L_opp_5mil = L_self - np.interp(5, s_mils, M)
    Vgb_5mil = L_opp_5mil * 1e-9 * dIdt
    Vgb_far = L_self * 1e-9 * dIdt
    print(f"\n  Ground bounce (I=100mA, dt=1ns):")
    print(f"  s >> d: Vgb = {Vgb_far*1000:.0f} mV (text: 250 mV)")
    print(f"  s=5 mils: Vgb = {Vgb_5mil*1000:.0f} mV (text: 130 mV)")

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch6_effective_inductance.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch6_effective_inductance.png"))
    plt.close(fig)
    print("\n[Example 3] Effective inductance and ground bounce plot saved.")

    return s_mils, L_same, L_opposite


# ============================================================
# Example 4: Loop Inductance per Square of Planes (Eq. 6-23)
# ============================================================
def plane_loop_inductance():
    """
    L_loop = mu_0 * h * Len/w   for w >> h
    mu_0 = 4*pi*1e-7 H/m = 32 pH/mil
    Loop inductance per square: L_sq = mu_0 * h
    """
    mu_0_pH_per_mil = 4 * np.pi * 1e-7 * 1e12 / 39370.0  # ~32 pH/mil = 4*pi*1e5 / 39370

    h_mils = np.array([1, 2, 3, 5, 10, 20])
    L_sq_pH = mu_0_pH_per_mil * h_mils

    print("\n" + "=" * 60)
    print("[Example 4] Loop Inductance per Square of Planes")
    print("=" * 60)
    print(f"  mu_0 = {mu_0_pH_per_mil:.1f} pH/mil (target: 32)")
    print(f"  {'h (mils)':>10s}  {'L/sq (pH)':>12s}")
    print("  " + "-" * 24)
    for h, L in zip(h_mils, L_sq_pH):
        print(f"  {h:8d}  {L:12.1f}")

    # Via contact demonstration
    print(f"\n  Edge-contact (uniform current): L = {L_sq_pH[1]:.0f} pH (text: 62-64 pH)")
    print(f"  Via-contact (point contacts): ~4x higher: ~{4*L_sq_pH[1]:.0f} pH (text: 252 pH)")
    print(f"  With 50% clearance holes: +25% -> ~{1.25*4*L_sq_pH[1]:.0f} pH (text: 243 pH)")

    return h_mils, L_sq_pH


# ============================================================
# Example 5: Skin Depth in Copper
# ============================================================
def skin_depth_calculation():
    """
    delta = sqrt(1/(pi*f*mu*sigma))
    For copper: sigma = 5.8e7 S/m, mu_r = 1
    delta (um) = 66 / sqrt(f_MHz)
    """
    f_mhz = np.logspace(0, 5, 200)  # 1 MHz to 100 GHz
    f_hz = f_mhz * 1e6

    sigma_Cu = 5.8e7  # S/m
    mu_0 = 4 * np.pi * 1e-7
    delta_m = 1.0 / np.sqrt(np.pi * f_hz * mu_0 * sigma_Cu)
    delta_um = delta_m * 1e6

    # Copper thickness lines
    t_1oz = 35  # um
    t_halfoz = 17.5  # um

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.loglog(f_mhz, delta_um, 'b-', linewidth=2, label='Skin depth in copper')
    ax.axhline(y=t_1oz, color='orange', linestyle='--', alpha=0.7, label='1-oz Cu (35 um)')
    ax.axhline(y=t_halfoz, color='green', linestyle='--', alpha=0.7, label='1/2-oz Cu (17.5 um)')
    ax.axvline(x=10, color='red', linestyle=':', alpha=0.5, label='~10 MHz: skin depth = 1-oz Cu thickness')
    ax.set_xlabel('Frequency (MHz)')
    ax.set_ylabel('Skin Depth (microns)')
    ax.set_title('Fig 6-23: Skin Depth in Copper vs. Frequency')
    ax.grid(True, which='both', alpha=0.3)
    ax.legend(fontsize=9)
    ax.set_xlim(0.8, 100000)
    ax.set_ylim(0.5, 200)

    # Annotate key frequencies
    for f_key, label in [(1, '1 MHz\n66 um'), (100, '100 MHz\n6.6 um'),
                         (1000, '1 GHz\n2.1 um'), (10000, '10 GHz\n0.66 um')]:
        ax.annotate(label, xy=(f_key, 66/np.sqrt(f_key)),
                    fontsize=7, ha='center')

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch6_skin_depth.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch6_skin_depth.png"))
    plt.close(fig)
    print("\n[Example 5] Skin depth plot saved.")

    for f in [1, 10, 100, 1000]:
        d = 66 / np.sqrt(f)
        print(f"  {f:5d} MHz: skin depth = {d:5.1f} um")

    return f_mhz, delta_um


# ============================================================
# Example 6: Decoupling Capacitor Requirements (Eq. 6-21)
# ============================================================
def decoupling_requirements():
    """
    C = (1/0.05) * P/V^2 * dt   or dt = C * 0.05 * V^2 / P
    """
    print("\n" + "=" * 60)
    print("[Example 6] Decoupling Capacitance Requirements")
    print("=" * 60)

    V_supply = 3.3  # volts
    P_chip = 1.0  # watt

    # Required C for various decoupling times
    dt_targets = [0.01e-6, 0.1e-6, 1e-6, 10e-6]  # 10 ns to 10 us
    print(f"  V_supply = {V_supply} V, P_chip = {P_chip} W")
    print(f"  Allowed droop = 5%")
    print(f"  {'Decoupling time':>18s}  {'Required C':>14s}")
    print("  " + "-" * 34)
    for dt in dt_targets:
        C_req = (1.0 / 0.05) * P_chip / V_supply**2 * dt
        print(f"  {dt*1e6:10.0f} us  {C_req*1e6:14.2f} uF")

    # Given C, how long it decouples
    C_values = [0.1e-9, 1e-9, 10e-9, 100e-9, 1e-6, 10e-6]  # nF to uF
    print(f"\n  Given capacitor -> decoupling time:")
    for C in C_values:
        dt = C * 0.05 * V_supply**2 / P_chip
        print(f"  {C*1e9:8.1f} nF decouples for {dt*1e9:8.1f} nsec")

    return


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Bogatin SI/PI 2nd Ed. — Chapter 6 Examples")
    print("=" * 60)

    partial_self_inductance()
    partial_mutual_inductance()
    effective_inductance_ground_bounce()
    plane_loop_inductance()
    skin_depth_calculation()
    decoupling_requirements()

    print("\n" + "=" * 60)
    print("All Chapter 6 examples complete.")
    print("=" * 60)
