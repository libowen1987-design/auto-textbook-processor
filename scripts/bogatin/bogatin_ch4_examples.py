#!/usr/bin/env python3
"""
bogatin_ch4_examples.py — Chapter 4: Physical Basis of Resistance

Concepts demonstrated:
  1. Wire bond resistance calculation (Eq. 4-1, 4-2)
  2. Sheet resistance and resistance per length (Eq. 4-6, 4-7)
  3. Trace resistance vs. line width for 1-oz and 1/2-oz Cu (Fig 4-7)
  4. AWG wire resistance per length
  5. PQFP lead resistance estimation (tapered lead from Eq. 4-3)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
import os

FIGURE_DIR = "/home/ubuntu/.openclaw/workspace/textbooks/bogatin/figures"
os.makedirs(FIGURE_DIR, exist_ok=True)
plt.rcParams['figure.dpi'] = 150


# ============================================================
# Example 1: Wire Bond Resistance (Eq. 4-1, 4-2)
# ============================================================
def wire_bond_resistance():
    """
    R = rho * length / area
    Gold wire bond: length=0.2cm (80 mils), diam=0.0025cm (1 mil)
    rho_gold = 2.5 uOhm-cm
    """
    rho_gold = 2.5e-6  # Ohm-cm
    diameter_cm = 0.0025  # 1 mil
    length_cm = 0.2  # 80 mils
    area_cm2 = np.pi / 4 * diameter_cm**2
    R = rho_gold * length_cm / area_cm2
    print("=" * 60)
    print("[Example 1] Wire Bond Resistance")
    print("=" * 60)
    print(f"  Gold wire bond: d={length_cm*10:.1f} mm, diam={diameter_cm*10000:.0f} um ({diameter_cm*1000*1000/25.4:.0f} mil)")
    print(f"  Cross-section area: {area_cm2*1e8:.2f} um^2")
    print(f"  R = {R:.4f} Ohm (target: ~0.1 Ohm)")

    # Resistance per length
    R_per_inch = rho_gold / area_cm2 * 2.54  # Ohm/inch
    print(f"  R_per_length: {R_per_inch:.2f} Ohm/inch (rule: ~1 Ohm/inch)")

    return R


# ============================================================
# Example 2: Sheet Resistance and Trace Resistance
# ============================================================
def sheet_resistance_calculations():
    """
    Rsq = rho / t
    1-oz Cu: t = 1.4 mil = 35 um, rho_Cu ~ 1.72 uOhm-cm
    1/2-oz Cu: t = 0.7 mil = 17.5 um
    """
    rho_Cu = 1.72e-6  # Ohm-cm (typical annealed copper)

    # Copper thicknesses
    t_1oz_cm = 35e-4  # 35 um -> cm
    t_halfoz_cm = 17.5e-4

    Rsq_1oz = rho_Cu / t_1oz_cm
    Rsq_halfoz = rho_Cu / t_halfoz_cm

    print("\n" + "=" * 60)
    print("[Example 2] Sheet Resistance")
    print("=" * 60)
    print(f"  1-oz Cu:    Rsq = {Rsq_1oz*1000:.2f} mOhm/sq  (target: 0.5 mOhm/sq)")
    print(f"  1/2-oz Cu:  Rsq = {Rsq_halfoz*1000:.2f} mOhm/sq  (target: 1.0 mOhm/sq)")

    # Trace resistance: 5-mil wide, 5-inch long
    w_mil = 5
    d_mil = 5000  # 5 inches
    n_sq = d_mil / w_mil
    R_5mil_halfoz = Rsq_halfoz * n_sq
    R_5mil_1oz = Rsq_1oz * n_sq
    print(f"\n  5-mil wide, 5-inch trace:")
    print(f"    n = {n_sq:.0f} squares")
    print(f"    1/2-oz Cu: R = {R_5mil_halfoz:.3f} Ohm  (target: 1 Ohm)")
    print(f"    1-oz Cu:   R = {R_5mil_1oz:.4f} Ohm  (target: 0.5 Ohm)")

    return Rsq_1oz, Rsq_halfoz


# ============================================================
# Example 3: Trace Resistance vs. Line Width (Fig 4-7)
# ============================================================
def trace_resistance_vs_width():
    """
    Replicate Fig 4-7: resistance per length for different line widths.
    """
    widths_mil = np.linspace(1, 30, 200)
    widths_cm = widths_mil * 25.4e-4  # mil -> cm
    rho_Cu = 1.72e-6

    t_1oz_cm = 35e-4
    t_halfoz_cm = 17.5e-4

    RL_1oz = rho_Cu / (widths_cm * t_1oz_cm)      # Ohm/cm
    RL_halfoz = rho_Cu / (widths_cm * t_halfoz_cm)  # Ohm/cm

    # Convert to Ohm/inch
    RL_1oz_inch = RL_1oz * 2.54
    RL_halfoz_inch = RL_halfoz * 2.54

    fig, ax = plt.subplots(figsize=(9, 5.5))

    ax.plot(widths_mil, RL_halfoz_inch, 'r-', linewidth=2,
            label='1/2-oz copper (Rsq ≈ 1 mOhm/sq)')
    ax.plot(widths_mil, RL_1oz_inch, 'b-', linewidth=2,
            label='1-oz copper (Rsq ≈ 0.5 mOhm/sq)')

    ax.set_xlabel('Line Width (mils)')
    ax.set_ylabel('Resistance per Length (Ohms/inch)')
    ax.set_title('Figure 4-7: Trace Resistance per Length vs. Line Width')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 0.55)

    # Annotate 5-mil point
    ax.scatter([5, 5], [np.interp(5, widths_mil, RL_halfoz_inch),
                       np.interp(5, widths_mil, RL_1oz_inch)],
               c=['red', 'blue'], s=50, zorder=5)
    ax.annotate('5 mil width', xy=(5.5, 0.2), fontsize=9,
                fontweight='bold')

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch4_trace_resistance.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch4_trace_resistance.png"))
    plt.close(fig)
    print("\n[Example 3] Trace resistance vs. width plot saved.")

    print(f"  At 5-mil width:")
    print(f"    1-oz Cu:    RL = {np.interp(5, widths_mil, RL_1oz_inch):.3f} Ohm/inch")
    print(f"    1/2-oz Cu:  RL = {np.interp(5, widths_mil, RL_halfoz_inch):.3f} Ohm/inch")

    return widths_mil, RL_1oz_inch, RL_halfoz_inch


# ============================================================
# Example 4: AWG Wire Table
# ============================================================
def awg_wire_table():
    """
    Generate AWG wire table like Fig 4-4.
    """
    awg_sizes = np.array([24, 22, 20, 18, 16, 14, 12, 10])
    # Diameter formula: d = 92^((36-AWG)/39) * 0.005 inch for AWG 36 = 0.005 in
    diameters_inch = 0.005 * 92**((36 - awg_sizes) / 39.0)
    diameters_cm = diameters_inch * 2.54

    rho_Cu = 1.74e-6  # Ohm-cm (text uses 1.74 for this table)
    R_per_1000ft = rho_Cu / (np.pi/4 * diameters_cm**2) * (1000 * 12 * 2.54)

    print("\n" + "=" * 60)
    print("[Example 4] AWG Wire Resistance (Fig 4-4)")
    print("=" * 60)
    print(f"  {'AWG':>4s}  {'Diam (in)':>10s}  {'R/1000ft (Ohm)':>14s}")
    print("  " + "-" * 32)

    for awg, d_in, R in zip(awg_sizes, diameters_inch, R_per_1000ft):
        print(f"  {awg:4d}  {d_in:10.4f}  {R:14.2f}")

    return awg_sizes, diameters_inch, R_per_1000ft


# ============================================================
# Example 5: PQFP Lead Resistance (Eq. 4-3)
# ============================================================
def pqfp_lead_resistance():
    """
    PQFP lead: 0.5 inch long, 3 mil thick, 10-20 mil wide taper.
    Use average width = 15 mil. Copper rho = 1.8 uOhm-cm.
    """
    rho_Cu = 1.8e-6  # Ohm-cm
    d_cm = 0.5 * 2.54  # 0.5 inch to cm
    t_cm = 0.003 * 2.54  # 3 mil to cm
    w_avg_cm = 0.015 * 2.54  # 15 mil to cm (average)
    A_cm2 = t_cm * w_avg_cm

    R = rho_Cu * d_cm / A_cm2

    print("\n" + "=" * 60)
    print("[Example 5] PQFP Lead Resistance (Eq. 4-3)")
    print("=" * 60)
    print(f"  Lead: d={0.5:.1f} inch, t=3 mil, w_avg=15 mil")
    print(f"  R = {R*1000:.1f} mOhm  (target: ~8 mOhm)")

    return R


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    wire_bond_resistance()
    sheet_resistance_calculations()
    trace_resistance_vs_width()
    awg_wire_table()
    pqfp_lead_resistance()

    print("\n" + "=" * 60)
    print("All Chapter 4 examples complete.")
    print("=" * 60)
