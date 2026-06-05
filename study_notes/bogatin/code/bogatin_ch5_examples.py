#!/usr/bin/env python3
"""
bogatin_ch5_examples.py — Chapter 5: Physical Basis of Capacitance

Concepts demonstrated:
  1. Sphere capacitance vs. radius (rule: 1-inch sphere ~2 pF)
  2. Parallel plate approximation (Eq. 5-5)
  3. Coax cable capacitance per length (Eq. 5-10, 5-11)
  4. Power/ground plane decoupling capacitance and time (Eq. 5-7, 5-8)
  5. Microstrip capacitance per length vs. line width (IPC approx, Eq. 5-16)
  6. Capacitance per area vs. spacing for different Dk (Fig 5-4)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
import os

FIGURE_DIR = "/home/ubuntu/.openclaw/workspace/textbooks/bogatin/figures"
os.makedirs(FIGURE_DIR, exist_ok=True)
plt.rcParams['figure.dpi'] = 150

# Physical constants (using scipy for rigor)
EPSILON_0 = constants.epsilon_0  # F/m
EPS_0_pF_per_cm = EPSILON_0 * 1e12 / 100.0  # pF/cm: 8.854e-12 F/m * 1e12 pF/F / 100 cm/m = 0.0885 pF/cm
EPS_0_pF_per_inch = EPS_0_pF_per_cm * 2.54  # pF/inch

print(f"  epsilon_0 = {EPS_0_pF_per_cm:.4f} pF/cm (text: 0.089)")
print(f"  epsilon_0 = {EPS_0_pF_per_inch:.4f} pF/inch (text: 0.225)")


# ============================================================
# Example 1: Sphere Capacitance (Eq. 5-3, 5-4)
# ============================================================
def sphere_capacitance():
    """
    Isolated sphere: C = 4*pi*epsilon*r
    """
    radii_inch = np.array([0.1, 0.25, 0.5, 0.75, 1.0, 2.0])
    radii_cm = radii_inch * 2.54
    C_pF = 4 * np.pi * EPS_0_pF_per_cm * radii_cm

    print("\n" + "=" * 60)
    print("[Example 1] Isolated Sphere Capacitance")
    print("=" * 60)
    print(f"  {'Radius (in)':>12s}  {'C (pF)':>10s}")
    print("  " + "-" * 24)
    for r, C in zip(radii_inch, C_pF):
        print(f"  {r:10.2f}  {C:10.2f}")

    # 1-inch diameter sphere (0.5 inch radius)
    r_1in = 0.5 * 2.54  # cm
    C_1in_sphere = 4 * np.pi * EPS_0_pF_per_cm * r_1in
    print(f"\n  1-inch diameter sphere: C = {C_1in_sphere:.1f} pF (rule: ~2 pF)")

    return radii_inch, C_pF


# ============================================================
# Example 2: Parallel Plate Capacitance (Eq. 5-5)
# ============================================================
def parallel_plate_demo():
    """
    C = epsilon_0 * epsilon_r * A / h
    """
    # Penny-sized: 1 cm^2, 1 mm gap
    A_cm2 = 1.0
    h_cm = 0.1
    C_penny = EPS_0_pF_per_cm * A_cm2 / h_cm
    print("\n" + "=" * 60)
    print("[Example 2] Parallel Plate Capacitance")
    print("=" * 60)
    print(f"  Penny-sized (1 cm^2, 1 mm gap): C = {C_penny:.1f} pF (rule: ~0.9 pF)")

    # Show effect of fringing: compare with correction for finite plates
    # For square plates w=h, true C ~ 2x parallel plate approx
    print(f"  With fringing (w=h, typical): C ≈ {C_penny * 2:.1f} pF")

    return C_penny


# ============================================================
# Example 3: Coax Capacitance per Length (Eq. 5-10, 5-11)
# ============================================================
def coax_capacitance():
    """
    RG58 coax: b/a = 3, epsilon_r = 2.3 (polyethylene)
    CL = 2*pi*epsilon*epsilon_r / ln(b/a)
    """
    b_over_a = 3.0
    epsilon_r = 2.3

    CL_pF_per_inch = 2 * np.pi * EPS_0_pF_per_inch * epsilon_r / np.log(b_over_a)
    CL_pF_per_cm = 2 * np.pi * EPS_0_pF_per_cm * epsilon_r / np.log(b_over_a)

    print("\n" + "=" * 60)
    print("[Example 3] Coax Capacitance per Length (RG58)")
    print("=" * 60)
    print(f"  b/a = {b_over_a:}, epsilon_r = {epsilon_r}")
    print(f"  CL = {CL_pF_per_inch:.2f} pF/inch (text: 2.9)")
    print(f"  CL = {CL_pF_per_cm:.2f} pF/cm")

    # Sweep b/a ratio and show CL variation
    ba_ratios = np.linspace(2, 10, 100)
    CL_ba = 2 * np.pi * EPS_0_pF_per_inch * epsilon_r / np.log(ba_ratios)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(ba_ratios, CL_ba, 'b-', linewidth=2)
    ax.axvline(x=3.0, color='red', linestyle='--', alpha=0.5,
               label=f'RG58: b/a=3, CL={CL_pF_per_inch:.1f} pF/inch')
    ax.set_xlabel('Outer/Inner Radius Ratio (b/a)')
    ax.set_ylabel('Capacitance per Length (pF/inch)')
    ax.set_title('Coax: $C_L = 2\\pi\\epsilon_0\\epsilon_r / \\ln(b/a)$')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim(1.5, 10)
    ax.set_ylim(0, 8)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch5_coax_capacitance.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch5_coax_capacitance.png"))
    plt.close(fig)
    print("[Example 3] Coax capacitance plot saved.")

    return CL_pF_per_inch


# ============================================================
# Example 4: Power/Ground Plane Decoupling (Eq. 5-7, 5-8, Fig 5-4)
# ============================================================
def plane_decoupling():
    """
    Replicate Fig 5-4 and compute decoupling time.
    """
    # Part A: Fig 5-4 — Capacitance per area vs. spacing
    h_mils = np.logspace(-2, 2, 100)  # 0.01 to 100 mils
    dk_values = [1, 4, 10, 20]
    colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(dk_values)))

    fig, ax = plt.subplots(figsize=(9, 5.5))

    for idx, dk in enumerate(dk_values):
        # C/A = epsilon_0 * epsilon_r / h  [pF/inch^2]
        C_per_area_nF = EPS_0_pF_per_inch * dk / h_mils / 1000  # nF/in^2
        ax.loglog(h_mils, C_per_area_nF, color=colors[idx], linewidth=2,
                  label=f'$\\epsilon_r$ = {dk}')

    # Mark C-Ply (8 um ~ 0.33 mil, Dk=20)
    ax.scatter([0.33], [14], s=100, color='red', zorder=5, marker='*')
    ax.annotate('3M C-Ply\n(8 um, Dk=20)\n14 nF/in²', xy=(0.33, 14),
                xytext=(1, 20), fontsize=9, fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='red'))

    # Mark typical FR4: 10 mil, Dk=4
    ax.scatter([10], [EPS_0_pF_per_inch * 4 / 10 / 1000], s=80,
               color='blue', zorder=5, marker='s')
    ax.annotate('Standard FR4\n10 mil, Dk=4\n0.09 nF/in²', xy=(10, 0.09),
                xytext=(3, 0.3), fontsize=9,
                arrowprops=dict(arrowstyle='->', color='blue'))

    ax.set_xlabel('Dielectric Thickness (mils)')
    ax.set_ylabel('Capacitance per Area (nF/in²)')
    ax.set_title('Figure 5-4: Power/Ground Plane Capacitance')
    ax.grid(True, which='both', alpha=0.3)
    ax.legend(fontsize=9)
    ax.set_xlim(0.008, 120)
    ax.set_ylim(0.002, 200)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch5_plane_capacitance.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch5_plane_capacitance.png"))
    plt.close(fig)
    print("\n[Example 4] Plane capacitance vs. spacing plot saved.")

    # Part B: Decoupling time calculation
    # dt = C * 0.05 * V^2 / P
    print(f"\n  Decoupling time examples (5% droop, V=3.3V, P=1W):")
    cases = [
        ("4 in² FR4, 10 mil", 0.4e-9),
        ("4 in² FR4, 2 mil", 2e-9),
        ("4 in² C-Ply (8 um)", 56e-9),
        ("10 uF bulk cap", 10e-6),
    ]
    for desc, C_farad in cases:
        dt = C_farad * 0.05 * 3.3**2 / 1.0
        print(f"  {desc:25s}: C={C_farad*1e9:.1f} nF -> dt={dt*1e9:.1f} nsec")

    return h_mils


# ============================================================
# Example 5: Microstrip CL vs. Line Width (IPC approx, Eq. 5-16)
# ============================================================
def microstrip_CL_vs_width():
    """
    IPC approximation for CL of microstrip:
    CL = 0.67*(1.41 + epsilon_r) / ln(5.98*h/(0.8*w + t))
    """
    epsilon_r = 4.0
    h = 5.0  # mils
    t = 0.7  # mils (1/2 oz copper)
    widths_mil = np.linspace(1, 30, 100)

    CL = 0.67 * (1.41 + epsilon_r) / np.log(5.98 * h / (0.8 * widths_mil + t))

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(widths_mil, CL, 'b-', linewidth=2,
            label=f'$\epsilon_r$={epsilon_r}, h={h} mil, t={t} mil')
    ax.axhline(y=3.5, color='gray', linestyle='--', alpha=0.5,
               label='50-$\Omega$ line rule: ~3.5 pF/in')
    ax.set_xlabel('Line Width (mils)')
    ax.set_ylabel('Capacitance per Length (pF/inch)')
    ax.set_title('Microstrip: $C_L$ vs. Line Width (IPC Approximation)')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 10)

    # Find width for ~50 Ohm (CL ~ 3.5 pF/inch)
    w_50_idx = np.argmin(np.abs(CL - 3.5))
    w_50 = widths_mil[w_50_idx]
    ax.scatter([w_50], [3.5], color='red', s=60, zorder=5)
    ax.annotate(f'50-$\Omega$: w≈{w_50:.0f} mil\n$C_L$≈{CL[w_50_idx]:.1f} pF/inch',
                xy=(w_50, 3.5), fontsize=9,
                xytext=(w_50 + 5, 4.5),
                arrowprops=dict(arrowstyle='->', color='red'))

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch5_microstrip_CL.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch5_microstrip_CL.png"))
    plt.close(fig)
    print("\n[Example 5] Microstrip CL vs. width plot saved.")
    print(f"  Width for CL=3.5 pF/in: {w_50:.0f} mils")

    return widths_mil, CL


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Bogatin SI/PI 2nd Ed. — Chapter 5 Examples")
    print("=" * 60)

    sphere_capacitance()
    parallel_plate_demo()
    coax_capacitance()
    plane_decoupling()
    microstrip_CL_vs_width()

    print("\n" + "=" * 60)
    print("All Chapter 5 examples complete.")
    print("=" * 60)
