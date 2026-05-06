#!/usr/bin/env python3
"""
bogatin_ch7_examples.py — Chapter 7: Physical Basis of Transmission Lines

Concepts demonstrated:
  1. Signal speed in different dielectrics (Eq. 7-4, 7-5, 7-6)
  2. Spatial extent of the leading edge (Eq. 7-8)
  3. Characteristic impedance from CL (Eq. 7-12, 7-14)
  4. Voltage launched into a TL vs. source resistance (Eq. 7-16, Fig 7-17)
  5. Return-path impedance between planes (Eq. 7-24)
  6. Characteristic impedance of planes (Eq. 7-18)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
import os

FIGURE_DIR = "/home/ubuntu/.openclaw/workspace/textbooks/bogatin/figures"
os.makedirs(FIGURE_DIR, exist_ok=True)
plt.rcParams['figure.dpi'] = 150

C = constants.speed_of_light  # m/s
C_in_per_nsec = C * 1e-9 * 39.37  # inches/nsec


# ============================================================
# Example 1: Signal Speed in Different Dielectrics
# ============================================================
def signal_speed():
    """
    v = c / sqrt(epsilon_r)
    """
    epsilon_r_values = [1, 2.1, 2.3, 4, 4.5, 6, 10]
    v_in_ns = C_in_per_nsec / np.sqrt(epsilon_r_values)
    delay_ps_per_in = 1000.0 / v_in_ns

    print("=" * 60)
    print("[Example 1] Signal Speed in Dielectrics")
    print("=" * 60)
    print(f"  {'Material':>12s}  {'eps_r':>6s}  {'v (in/nsec)':>12s}  {'Delay (ps/in)':>14s}")
    print("  " + "-" * 48)
    materials = ['Air', 'Teflon', 'Polyethylene', 'FR4', 'FR4 (typical)', 'Glass', 'Alumina']
    for mat, er, v, d in zip(materials, epsilon_r_values, v_in_ns, delay_ps_per_in):
        print(f"  {mat:>12s}  {er:6.1f}  {v:12.2f}  {d:14.0f}")

    return epsilon_r_values, v_in_ns


# ============================================================
# Example 2: Spatial Extent of Leading Edge
# ============================================================
def spatial_extent():
    """
    d = RT * v
    """
    epsilon_r = 4.0
    v = C_in_per_nsec / np.sqrt(epsilon_r)
    print(f"\n  Speed in FR4 (eps=4): v = {v:.1f} in/nsec")

    rt_values = np.array([0.05, 0.1, 0.2, 0.5, 1.0, 2.0])  # nsec
    d_inches = rt_values * v

    print(f"  {'RT (ns)':>10s}  {'Spatial Extent (in)':>20s}")
    print("  " + "-" * 32)
    for rt, d in zip(rt_values, d_inches):
        print(f"  {rt:8.2f}  {d:18.1f}")

    # Plot
    rt_plot = np.linspace(0.01, 2.0, 100)
    d_plot = rt_plot * v
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(rt_plot, d_plot, 'b-', linewidth=2)
    ax.set_xlabel('Rise Time (nsec)')
    ax.set_ylabel('Spatial Extent (inches)')
    ax.set_title('Spatial Extent of Leading Edge (FR4, $\\epsilon_r=4$)')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 2.0)
    ax.set_ylim(0, 14)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch7_spatial_extent.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch7_spatial_extent.png"))
    plt.close(fig)
    print("[Example 2] Spatial extent plot saved.")

    return rt_values, d_inches


# ============================================================
# Example 3: Z0 from CL and epsilon_r (Eq. 7-12, 7-14)
# ============================================================
def z0_from_cl():
    """
    Z0 = 83 * sqrt(epsilon_r) / CL   (CL in pF/inch)
    """
    epsilon_r = 4.0
    CL_values = np.linspace(1, 8, 100)  # pF/inch
    Z0 = 83 * np.sqrt(epsilon_r) / CL_values

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(Z0, CL_values, 'r-', linewidth=2)
    ax.axhline(y=3.3, color='blue', linestyle='--', alpha=0.5,
               label='CL = 3.3 pF/in (50 Ohm)')
    ax.axvline(x=50, color='blue', linestyle='--', alpha=0.5)
    ax.set_xlabel('Characteristic Impedance $Z_0$ ($\Omega$)')
    ax.set_ylabel('Capacitance per Length $C_L$ (pF/inch)')
    ax.set_title('$Z_0 = 83 \\cdot \\sqrt{\\epsilon_r} / C_L$ in FR4')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 10)

    # Key points
    for Z in [28, 50, 75, 100]:
        CL = 83 * np.sqrt(epsilon_r) / Z
        ax.scatter([Z], [CL], color='red', s=40, zorder=5)
        ax.annotate(f'$Z_0$={Z}$\\Omega$\n$C_L$={CL:.1f} pF/in',
                    xy=(Z, CL), fontsize=8, ha='center')

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch7_z0_vs_CL.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch7_z0_vs_CL.png"))
    plt.close(fig)
    print("\n[Example 3] Z0 vs. CL plot saved.")

    print(f"\n  Z0 = 50:  CL = {83*np.sqrt(4)/50:.1f} pF/inch")
    print(f"  Z0 = 75:  CL = {83*np.sqrt(4)/75:.1f} pF/inch")
    print(f"  Z0 = 28:  CL = {83*np.sqrt(4)/28:.1f} pF/inch (Rambus)")

    return Z0, CL_values


# ============================================================
# Example 4: Voltage Launch vs. Source Resistance (Fig 7-17)
# ============================================================
def voltage_launch():
    """
    V_launched = V_out * Z0 / (Rs + Z0)
    """
    Z0 = 50.0
    Rs_values = np.linspace(0, 100, 200)
    fraction = Z0 / (Rs_values + Z0)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(Rs_values, fraction * 100, 'b-', linewidth=2)
    ax.axhline(y=50, color='gray', linestyle='--', alpha=0.5,
               label='50% (Rs = Z0)')
    ax.axvline(x=Z0, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('Output Source Impedance $R_s$ ($\Omega$)')
    ax.set_ylabel('Voltage Launched into Line (%)')
    ax.set_title('Fig 7-17: Voltage Launch vs. $R_s$ (50-$\Omega$ Line)')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 105)

    # Annotate key points
    for Rs in [5, 10, 25, 50]:
        frac = Z0 / (Rs + Z0) * 100
        ax.scatter([Rs], [frac], color='red', s=40, zorder=5)
        ax.annotate(f'$R_s$={Rs}$\\Omega$: {frac:.0f}%', xy=(Rs, frac),
                    fontsize=8, xytext=(Rs+3, frac-8),
                    arrowprops=dict(arrowstyle='->', color='red', lw=0.5))

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch7_voltage_launch.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch7_voltage_launch.png"))
    plt.close(fig)
    print("\n[Example 4] Voltage launch plot saved.")

    for Rs in [5, 10, 25, 50, 100]:
        frac = Z0 / (Rs + Z0) * 100
        print(f"  Rs = {Rs:3d} Ohm -> {frac:.0f}% launched")

    return Rs_values, fraction


# ============================================================
# Example 5: Return-Path Impedance Between Planes (Eq. 7-24)
# ============================================================
def return_path_impedance():
    """
    Z(t) = 5 * h / t   (mils, nsec)
    """
    h_mils = np.array([2, 5, 10, 20])
    t_ns = np.logspace(-2, 1, 200)  # 0.01 to 10 nsec

    fig, ax = plt.subplots(figsize=(8, 5))
    colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(h_mils)))

    for idx, h in enumerate(h_mils):
        Z = 5 * h / t_ns
        ax.loglog(t_ns, Z, color=colors[idx], linewidth=2,
                  label=f'h = {h} mils')

    ax.axhline(y=0.5, color='gray', linestyle=':', alpha=0.5,
               label='0.5 Ohm reference')
    ax.set_xlabel('Time (nsec)')
    ax.set_ylabel('Return Path Impedance $Z_{return}$ ($\Omega$)')
    ax.set_title('$Z_{return}(t) \\approx 5h / t$ for Plane Switching')
    ax.grid(True, which='both', alpha=0.3)
    ax.legend(fontsize=9)
    ax.set_xlim(0.008, 15)
    ax.set_ylim(0.01, 100)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch7_return_path_impedance.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch7_return_path_impedance.png"))
    plt.close(fig)
    print("\n[Example 5] Return path impedance plot saved.")

    # Ground bounce example
    print(f"\n  Ground bounce (10 signals, 20 mA each, h=10 mil):")
    for t in [0.1, 0.5, 1.0]:
        Z = 5 * 10 / t
        Vgb = 0.2 * Z * 1000  # mV
        print(f"  t={t:.1f} ns: Z={Z:.2f} Ohm, Vgb={Vgb:.0f} mV")

    return t_ns


# ============================================================
# Example 6: Plane Characteristic Impedance (Eq. 7-18)
# ============================================================
def plane_z0():
    """
    Z0 = (377 / sqrt(epsilon_r)) * h/w
    """
    epsilon_r = 4.0
    h_mils = np.array([2, 5, 10])
    w_range = np.linspace(0.1, 5, 200)  # inches

    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['blue', 'green', 'red']

    for idx, h in enumerate(h_mils):
        Z0 = (377 / np.sqrt(epsilon_r)) * (h / 1000.0) / w_range
        ax.plot(w_range, Z0, color=colors[idx], linewidth=2,
                label=f'h = {h} mils')

    ax.set_xlabel('Plane Width (inches)')
    ax.set_ylabel('Plane Characteristic Impedance $Z_0$ ($\Omega$)')
    ax.set_title('$Z_0 \\approx (377/\\sqrt{\\epsilon_r}) \\cdot h/w$ for Planes')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch7_plane_Z0.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch7_plane_Z0.png"))
    plt.close(fig)
    print("\n[Example 6] Plane characteristic impedance plot saved.")

    # Key values
    for h in [2, 10]:
        for w in [0.5, 2.0]:
            Z = (377 / np.sqrt(4)) * (h/1000) / w
            print(f"  h={h:2d} mil, w={w:.1f} in -> Z0 = {Z:.2f} Ohm")

    return h_mils, w_range


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Bogatin SI/PI 2nd Ed. — Chapter 7 Examples")
    print("=" * 60)

    signal_speed()
    spatial_extent()
    z0_from_cl()
    voltage_launch()
    return_path_impedance()
    plane_z0()

    print("\n" + "=" * 60)
    print("All Chapter 7 examples complete.")
    print("=" * 60)
