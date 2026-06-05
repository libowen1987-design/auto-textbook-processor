#!/usr/bin/env python3
"""
bogatin_ch8_examples.py — Chapter 8: Reflections and Transmission Lines

Concepts demonstrated:
  1. Reflection coefficient vs. terminating impedance (Eq. 8-1, Fig 8-5)
  2. Bounce diagram simulation for unterminated line
  3. Source-series termination effect
  4. Max unterminated line length rule
  5. Discontinuity (stub/neck-down) impact
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
import os

FIGURE_DIR = "/home/ubuntu/.openclaw/workspace/textbooks/bogatin/figures"
os.makedirs(FIGURE_DIR, exist_ok=True)
plt.rcParams['figure.dpi'] = 150


# ============================================================
# Example 1: Reflection Coefficient (Fig 8-5)
# ============================================================
def reflection_coefficient_demo():
    Z1 = 50.0
    Z2 = np.linspace(0, 150, 500)
    rho = (Z2 - Z1) / (Z2 + Z1)
    V_end = 1 + rho  # for 1V incident

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(Z2, rho * 100, 'b-', linewidth=2)
    ax1.axhline(y=0, color='gray', linestyle=':', alpha=0.5)
    ax1.axvline(x=Z1, color='gray', linestyle='--', alpha=0.5, label='Z0=50 Ohm')
    ax1.set_xlabel('Termination Impedance $Z_2$ ($\Omega$)')
    ax1.set_ylabel('Reflection Coefficient $\\rho$ (%)')
    ax1.set_title('Fig 8-5: Reflection Coefficient')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_xlim(0, 150)
    ax1.set_ylim(-110, 110)

    ax2.plot(Z2, V_end, 'r-', linewidth=2)
    ax2.axhline(y=1, color='gray', linestyle=':', alpha=0.5, label='1V incident')
    ax2.axvline(x=Z1, color='gray', linestyle='--', alpha=0.5)
    ax2.set_xlabel('Termination Impedance $Z_2$ ($\Omega$)')
    ax2.set_ylabel('Voltage Across Termination (V)')
    ax2.set_title('Fig 8-6: Voltage at Termination (1V incident)')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_xlim(0, 150)
    ax2.set_ylim(0, 2.1)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch8_reflection_coefficient.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch8_reflection_coefficient.png"))
    plt.close(fig)
    print("[Example 1] Reflection coefficient plots saved.")

    for Z in [0, 25, 50, 75, 100, 1e9]:
        r = (Z - 50) / (Z + 50)
        print(f"  Z_load = {Z:>4.0f} -> rho = {r:+.2f}, V_end = {1+r:.2f}V")

    return Z2, rho


# ============================================================
# Example 2: Bounce Diagram Simulation
# ============================================================
def bounce_simulation():
    """
    Simulate the unterminated line ringing.
    Vs=1V, Rs=10 Ohm, Z0=50 Ohm, open far end, TD=1 nsec
    Manual bounce tracking using reflection coefficients.
    """
    Rs, Z0 = 10.0, 50.0
    TD = 1.0  # nsec
    rho_s = (Rs - Z0) / (Rs + Z0)  # source reflection
    rho_l = 1.0  # open far end

    V_launch = 1.0 * Z0 / (Rs + Z0)
    print(f"\n[Example 2] Bounce Simulation")
    print(f"  Vs=1V, Rs={Rs} Ohm, Z0={Z0} Ohm, open far end")
    print(f"  rho_source = {rho_s:.2f}, rho_load = {rho_l:.1f}")
    print(f"  V_launch = {V_launch:.3f}V")

    # Track bounces for 20 nsec
    t_max = 8.0
    dt = 0.02  # nsec
    n_steps = int(t_max / dt)
    t = np.linspace(0, t_max, n_steps)
    V_source = np.zeros(n_steps)
    V_end = np.zeros(n_steps)

    # Simple bounce tracking
    # Each bounce event: at positions along line
    waves = []  # (time_of_arrival_at_end, voltage)
    V_now = V_launch  # incident wave
    time = 0

    # Add the initial wave heading toward far end
    while time < t_max:
        # Wave arrives at far end
        time += TD
        if time < t_max:
            V_end_val = V_now + V_now * rho_l
            idx = int(time / dt)
            V_end[idx:] += V_end_val

        # Reflected wave from far end heads back to source
        V_wave = V_now * rho_l
        time += TD  # arrives at source
        if time < t_max:
            V_now = V_wave * rho_s  # new wave from source reflection
        else:
            break

    # Simpler: just compute at specified time points
    # Known time points: 
    # t=TD: end=2*V_launch
    # t=3*TD: end=2*V_launch + 2*rho_s*rho_l*V_launch
    # t=5*TD: continue...
    t_points = np.array([TD, 3*TD, 5*TD, 7*TD])
    v_points = []
    V = V_launch
    for i in range(4):
        if i == 0:
            vp = 2 * V
        else:
            vp = v_points[-1] + 2 * V * (rho_s * rho_l)**i
        v_points.append(vp)

    print(f"  Bounce sequence (at far end):")
    for tp, vp in zip(t_points, v_points):
        print(f"    t = {tp:.1f} ns: V = {vp:.2f} V")

    # Plot smoother interpolation
    fig, ax = plt.subplots(figsize=(8, 5))
    t_plot = np.linspace(0, 20, 500)
    V_plot = np.zeros_like(t_plot)
    # Fill in each segment
    for i, (tp, vp) in enumerate(zip(t_points, v_points)):
        mask = t_plot >= tp
        V_plot[mask] = vp

    # Add exponential convergence
    t_conv = t_plot[t_plot > t_points[-1]]
    V_plot[t_plot > t_points[-1]] = 1.0 + (v_points[-1] - 1.0) * \
        np.exp(-(t_plot[t_plot > t_points[-1]] - t_points[-1]) / 5)

    ax.plot(t_plot, V_plot, 'b-', linewidth=2)
    ax.axhline(y=1.0, color='gray', linestyle='--', alpha=0.5, label='Vs = 1V (final)')
    ax.set_xlabel('Time (nsec)')
    ax.set_ylabel('Voltage at Far End (V)')
    ax.set_title('Fig 8-10: Unterminated Line Ringing (Rs=10, Z0=50)')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 2.0)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch8_bounce_simulation.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch8_bounce_simulation.png"))
    plt.close(fig)
    print("[Example 2] Bounce simulation plot saved.")

    return V_launch


# ============================================================
# Example 3: Source-Series Termination Effect
# ============================================================
def source_series_termination():
    """
    Show the effect of source-series termination vs unterminated.
    """
    Rs = 10.0
    Z0 = 50.0
    RT = 40.0  # series resistor

    V_launch_unterm = 1.0 * Z0 / (Rs + Z0)
    V_launch_term = 1.0 * Z0 / (Rs + RT + Z0)

    print(f"\n[Example 3] Source-Series Termination")
    print(f"  Rs={Rs}, RT={RT}, Z0={Z0}")
    print(f"  Rs+RT = {Rs+RT} Ohm (matched to Z0={Z0})")
    print(f"  V_launch (unterm) = {V_launch_unterm:.2f}V")
    print(f"  V_launch (term)   = {V_launch_term:.2f}V")
    print(f"  V at far end (term) = {2*V_launch_term:.2f}V (full voltage)")

    # Simulate waveforms
    t = np.linspace(0, 12, 1000)
    TD = 1.0  # nsec

    # Unterminated: ringing
    V_unterm = np.zeros_like(t)
    for i in range(6):
        delay = (2 * i + 1) * TD
        if i == 0:
            val = 2 * V_launch_unterm
        elif delay < t[-1]:
            val = 2 * V_launch_unterm * (-0.67)**i
        else:
            break
        mask = t >= delay
        V_unterm[mask] += val
    # Make converge
    V_unterm[t > 12] = 1.0

    # Terminated: clean step
    V_term = np.zeros_like(t)
    V_term[t >= TD] = 1.0  # full voltage after one TD

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(t, V_unterm, 'r-', linewidth=2, alpha=0.7, label='Unterminated (ringing)')
    ax.plot(t, V_term, 'b-', linewidth=2, label='Source-series terminated')
    ax.axhline(y=1.0, color='gray', linestyle='--', alpha=0.3)
    ax.set_xlabel('Time (nsec)')
    ax.set_ylabel('Voltage at Far End (V)')
    ax.set_title('Fig 8-18: Effect of Source-Series Termination')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 2.0)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch8_source_series_term.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch8_source_series_term.png"))
    plt.close(fig)
    print("[Example 3] Source-series termination plot saved.")


# ============================================================
# Example 4: Max Unterminated Length Rule
# ============================================================
def max_unterminated_length():
    """
    Len_max = RT (inches when RT in nsec)
    Rule: terminate when TD > 0.2*RT
    """
    RT = np.array([0.1, 0.25, 0.5, 1.0, 2.0, 5.0, 10.0])

    print(f"\n[Example 4] Max Unterminated Length Rule")
    print(f"  {'RT (ns)':>10s}  {'Len_max (in)':>14s}  {'TD_20% (ns)':>12s}  {'Terminate?':>12s}")
    print("  " + "-" * 52)

    for rt in RT:
        len_max = rt  # inches
        td_at_max = len_max / 6.0  # nsec (FR4)
        pct = td_at_max / rt * 100
        need_term = "YES" if td_at_max > 0.2 * rt else "no"
        print(f"  {rt:8.2f}  {len_max:12.1f}  {td_at_max:12.1f}  {need_term:>12s}")

    # Plot
    rt_range = np.logspace(-1, 1, 100)
    len_max_range = rt_range
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.loglog(rt_range, len_max_range, 'b-', linewidth=2)
    ax.fill_between(rt_range, len_max_range, 50, alpha=0.1, color='red',
                     label='Termination needed')
    ax.fill_between(rt_range, 0, len_max_range, alpha=0.1, color='green',
                     label='May be OK without termination')
    ax.set_xlabel('Rise Time (nsec)')
    ax.set_ylabel('Max Unterminated Length (inches)')
    ax.set_title('Rule: $L_{max} \\approx RT$ (inches when RT in nsec)')
    ax.grid(True, which='both', alpha=0.3)
    ax.legend(fontsize=9)
    ax.set_xlim(0.08, 12)
    ax.set_ylim(0.08, 50)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch8_max_unterminated.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch8_max_unterminated.png"))
    plt.close(fig)
    print("[Example 4] Max unterminated length plot saved.")

    return RT, len_max_range


# ============================================================
# Example 5: Stub Impact
# ============================================================
def stub_impact():
    """
    Show stub length impact on signal quality.
    """
    RT = 0.5  # nsec
    v = 6.0  # in/nsec (FR4)
    spatial_extent = RT * v  # 3 inches

    # Maximum acceptable stub
    L_stub_max = RT  # inches
    L_stub_ok = RT * 0.1  # 10% RT - OK
    L_stub_bad = RT * 0.5  # 50% RT - bad

    print(f"\n[Example 5] Stub Length Rule")
    print(f"  RT = {RT} nsec, v = {v} in/nsec")
    print(f"  Spatial extent of edge: {spatial_extent:.1f} inches")
    print(f"  Max acceptable stub: {L_stub_max:.2f} inch")
    print(f"  OK stub length: {L_stub_ok:.2f} inch")
    print(f"  Problematic stub: {L_stub_bad:.2f} inch")

    return


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Bogatin SI/PI 2nd Ed. — Chapter 8 Examples")
    print("=" * 60)

    reflection_coefficient_demo()
    bounce_simulation()
    source_series_termination()
    max_unterminated_length()
    stub_impact()

    print("\n" + "=" * 60)
    print("All Chapter 8 examples complete.")
    print("=" * 60)
