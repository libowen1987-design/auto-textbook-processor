#!/usr/bin/env python3
"""
ludwig_ch3_examples.py — Chapter 3: The Smith Chart
RF Circuit Design, 2nd Ed., Ludwig & Bogdanov

Examples covered:
  Ex3-1: Reflection coefficient representations
  Ex3-2: Input impedance via reflection coefficient
  Ex3-4: Γ, VSWR, and return loss for various loads
  Ex3-5: Open-circuit stub lengths for capacitor/inductor
  Bonus: Smith Chart visualization with r/x circles
  Bonus: T-network impedance calculation
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
    'figure.dpi': 120,
})

FIGS_DIR = '/home/ubuntu/.openclaw/workspace/textbooks/ludwig/figures'
Zf = np.sqrt(const.mu_0 / const.epsilon_0)  # 376.7 Ω


# ======================================================================
# Smith Chart plotting utility
# ======================================================================
def plot_smith_chart(ax, draw_labels=True):
    """Draw a Smith Chart on the given axes."""
    # Unit circle
    theta = np.linspace(0, 2*np.pi, 500)
    ax.plot(np.cos(theta), np.sin(theta), 'k-', linewidth=1.0)

    # Constant resistance circles (r = 0, 0.2, 0.5, 1, 2, 5)
    r_vals = [0, 0.2, 0.5, 1, 2, 5]
    for r in r_vals:
        center = r / (r + 1)
        radius = 1 / (r + 1)
        theta_c = np.linspace(-np.pi, np.pi, 200)
        xc = center + radius * np.cos(theta_c)
        yc = radius * np.sin(theta_c)
        # Clip to unit circle
        mask = xc**2 + yc**2 <= 1.0
        ax.plot(xc[mask], yc[mask], 'b-', linewidth=0.5, alpha=0.6)
        if draw_labels and r > 0:
            ax.annotate(f'{r}', (center + radius - 0.02, 0.02), fontsize=7, color='b')

    # Constant reactance circles (x = 0.2, 0.5, 1, 2, 5, -0.2, -0.5, -1, -2, -5)
    x_vals = [0.2, 0.5, 1, 2, 5, -0.2, -0.5, -1, -2, -5]
    for x in x_vals:
        center_x = 1
        center_y = 1 / x
        radius = 1 / abs(x)
        theta_c = np.linspace(0, 2*np.pi, 300)
        xc = center_x + radius * np.cos(theta_c)
        yc = center_y + radius * np.sin(theta_c)
        mask = xc**2 + yc**2 <= 1.0
        color = 'r' if x > 0 else 'g'
        ax.plot(xc[mask], yc[mask], '--', linewidth=0.5, alpha=0.5, color=color)

    # Axes
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)

    # Labels for key points
    if draw_labels:
        ax.annotate('Open\n($\\Gamma=1$)', xy=(1, 0), fontsize=8,
                    xytext=(1.05, -0.05))
        ax.annotate('Short\n($\\Gamma=-1$)', xy=(-1, 0), fontsize=8,
                    xytext=(-1.25, -0.05))
        ax.annotate('Match\n($\\Gamma=0$)', xy=(0, 0), fontsize=8,
                    xytext=(0.02, -0.05))

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect('equal')
    ax.axis('off')


# ======================================================================
# Example 3-1: Reflection coefficient representations
# ======================================================================
def example_3_1():
    """
    Z0=50 Ω. Compute Γ for various ZL values.
    """
    print("=" * 60)
    print("Example 3-1: Reflection coefficient representations")
    print("=" * 60)

    Z0 = 50.0
    loads = {
        '(a) Short': 0 + 0j,
        '(b) Open': 1e12 + 0j,
        '(c) Matched': 50 + 0j,
        '(d) ZL=16.67-j16.67': 16.67 - 16.67j,
        '(e) ZL=50+j150': 50 + 150j,
    }

    fig, ax = plt.subplots(figsize=(7, 7))
    plot_smith_chart(ax)

    colors = ['k', 'm', 'b', 'r', 'g']
    markers = ['s', '^', 'o', 'D', 'v']

    results = {}
    for (label, ZL), c, m in zip(loads.items(), colors, markers):
        Gamma = (ZL - Z0) / (ZL + Z0)
        mag = abs(Gamma)
        phase = np.angle(Gamma, deg=True)
        results[label] = {'Gamma': Gamma, 'mag': mag, 'phase': phase}
        print(f"  {label:30s}: Γ = {mag:.3f}∠{phase:.1f}°  "
              f"({Gamma.real:.3f}{Gamma.imag:+.3f}j)")

        ax.plot(Gamma.real, Gamma.imag, marker=m, color=c, markersize=8,
                label=f'{label.split(":")[0]}: |Γ|={mag:.2f}')
        ax.annotate(label.split(':')[0], xy=(Gamma.real, Gamma.imag),
                    xytext=(Gamma.real + 0.05, Gamma.imag + 0.05),
                    fontsize=8, color=c)

    ax.legend(loc='upper right', fontsize=8)
    ax.set_title('Ex3-1: Reflection Coefficient in $\\Gamma$-plane')
    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch3_ex3_1_Gamma_points.png', dpi=150)
    print(f"  → Saved figure to {FIGS_DIR}/ch3_ex3_1_Gamma_points.png")
    plt.close(fig)

    return results


# ======================================================================
# Example 3-2: Input impedance via reflection coefficient
# ======================================================================
def example_3_2():
    """
    Z0=50, ZL=30+j60, l=2cm, f=2GHz, vp=0.5c.
    """
    print("\n" + "=" * 60)
    print("Example 3-2: Input impedance via reflection coefficient")
    print("=" * 60)

    Z0 = 50.0
    ZL = 30 + 60j
    l = 0.02
    f = 2e9
    vp = 0.5 * const.c

    Gamma_0 = (ZL - Z0) / (ZL + Z0)
    beta = 2 * np.pi * f / vp
    Gamma_in = Gamma_0 * np.exp(-2j * beta * l)
    Zin = Z0 * (1 + Gamma_in) / (1 - Gamma_in)

    print(f"\n  Z0 = {Z0} Ω")
    print(f"  ZL = {ZL} Ω")
    print(f"  Γ0 = {abs(Gamma_0):.4f}∠{np.angle(Gamma_0, deg=True):.2f}°"
          f" = {Gamma_0.real:.4f}{Gamma_0.imag:+.4f}j")
    print(f"  β = {beta:.2f} rad/m, βl = {beta*l:.4f} rad = {beta*l*180/np.pi:.2f}°")
    print(f"  2βl = {2*beta*l*180/np.pi:.2f}°")
    print(f"  Γin = {abs(Gamma_in):.4f}∠{np.angle(Gamma_in, deg=True):.2f}°")
    print(f"  Zin = ({Zin.real:.2f}{Zin.imag:+.2f}j) Ω  ← 匹配书本(14.7-j26.7)Ω")

    # Sweep frequency and plot on Smith Chart
    fig, ax = plt.subplots(figsize=(7, 7))
    plot_smith_chart(ax)

    f_sweep = np.linspace(0.1e9, 3e9, 200)
    Gamma_sweep = Gamma_0 * np.exp(-2j * (2 * np.pi * f_sweep / vp) * l)
    ax.plot(Gamma_sweep.real, Gamma_sweep.imag, 'b-', linewidth=1.5, alpha=0.7,
            label='f: 0.1 → 3 GHz')
    ax.plot(Gamma_0.real, Gamma_0.imag, 'ro', markersize=6, label='$\\Gamma_0$ (load)')
    ax.plot(Gamma_in.real, Gamma_in.imag, 'go', markersize=6, label='$\\Gamma_{in}$ @ 2 GHz')
    ax.legend(loc='upper right', fontsize=8)
    ax.set_title('Ex3-2: Impedance Sweep on Smith Chart')
    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch3_ex3_2_freq_sweep.png', dpi=150)
    print(f"  → Saved figure to {FIGS_DIR}/ch3_ex3_2_freq_sweep.png")
    plt.close(fig)

    return Gamma_0, Gamma_in, Zin


# ======================================================================
# Example 3-4: Γ, VSWR, RL for various loads
# ======================================================================
def example_3_4():
    """
    Four loads on Z0=50 Ω. Compute Γ, RL(dB), VSWR.
    """
    print("\n" + "=" * 60)
    print("Example 3-4: Γ, VSWR, RL for various loads")
    print("=" * 60)

    Z0 = 50.0
    loads = [
        ('(a) ZL=50 Ω', 50 + 0j),
        ('(b) ZL=48.5 Ω', 48.5 + 0j),
        ('(c) ZL=75+j25 Ω', 75 + 25j),
        ('(d) ZL=10-j5 Ω', 10 - 5j),
    ]

    print(f"\n  {'Load':20s} | {'zL':15s} | {'Γ':15s} | {'RL(dB)':8s} | {'SWR':6s}")
    print('-' * 70)

    fig, ax = plt.subplots(figsize=(7, 7))
    plot_smith_chart(ax)

    results = []
    colors = ['g', 'b', 'r', 'm']
    for (label, ZL), c in zip(loads, colors):
        zL = ZL / Z0
        Gamma = (ZL - Z0) / (ZL + Z0)
        mag = abs(Gamma)
        RL_dB = -20 * np.log10(mag) if mag > 0 else float('inf')
        SWR = (1 + mag) / (1 - mag) if mag < 1 else float('inf')

        results.append((label, zL, Gamma, RL_dB, SWR))
        print(f"  {label:20s} | {zL.real:+.2f}{zL.imag:+.2f}j       | "
              f"{mag:.3f}∠{np.angle(Gamma, deg=True):.1f}° | "
              f"{RL_dB:>6.1f} | {SWR:>5.2f}")

        # Plot SWR circle
        theta = np.linspace(0, 2*np.pi, 200)
        ax.plot(mag * np.cos(theta), mag * np.sin(theta),
                '--', color=c, linewidth=0.8, alpha=0.5)
        ax.plot(Gamma.real, Gamma.imag, marker='o', color=c, markersize=7,
                label=label.split(':')[0])

    ax.legend(loc='upper right', fontsize=8)
    ax.set_title('Ex3-4: SWR Circles in $\\Gamma$-plane')
    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch3_ex3_4_SWR_circles.png', dpi=150)
    print(f"  → Saved figure to {FIGS_DIR}/ch3_ex3_4_SWR_circles.png")
    plt.close(fig)

    return results


# ======================================================================
# Example 3-5: Open-circuit stub for capacitor/inductor
# ======================================================================
def example_3_5():
    """
    Open-circuit 50 Ω line at 3 GHz, vp=0.77c.
    Find lengths for 2 pF capacitor and 5.3 nH inductor.
    """
    print("\n" + "=" * 60)
    print("Example 3-5: Open-circuit stub design")
    print("=" * 60)

    Z0 = 50.0
    f = 3e9
    vp = 0.77 * const.c
    beta = 2 * np.pi * f / vp
    lam = vp / f

    # Capacitor: 2 pF
    C_val = 2e-12
    XC = 1.0 / (2 * np.pi * f * C_val)
    d_cap = (1.0 / beta) * np.arctan(Z0 / XC)  # from Eq (3.16): cot^{-1}(X/Z0)
    # Wait, (3.16) is d = (1/β) * cot⁻¹(X/Z0)
    # cot⁻¹(X/Z0) = tan⁻¹(Z0/X) for positive values
    # Actually: d1 = (1/β) * cot⁻¹(X_C/Z_0) — let me check the book
    # The book says d1 = (1/β) * cot⁻¹(X_C/Z_0) for open-circuit capacitive stub
    # cot⁻¹(u) = π/2 - tan⁻¹(u) for u>0
    # So d1 = (1/β) * cot⁻¹(X_C/Z0)
    # Hmm, but the book computed d_cap = 13.27 mm
    # Let me verify: 
    # λ = vp/f = 0.77*3e8/3e9 = 0.077 m = 77 mm
    # β = 2π/λ = 81.58 rad/m
    # X_C = 1/(2π*3e9*2e-12) = 26.53 Ω
    # cot⁻¹(26.53/50) = cot⁻¹(0.5306) = tan⁻¹(1/0.5306) = tan⁻¹(1.8846) = 62.05°
    # 62.05° in radians = 1.083 rad
    # d = 1.083/81.58 = 0.01328 m = 13.28 mm ✓

    d_cap = (1.0 / beta) * (np.pi/2 - np.arctan(XC / Z0))
    # Actually: cot⁻¹(u) = π/2 - tan⁻¹(u) for u>0
    # So d = (1/β) * (π/2 - arctan(X/Z0))

    # Let me double check with the book's formula (3.16):
    # d1 = (1/β) * cot⁻¹(X_C/Z_0)
    # But my python gives... let me just use arctan directly
    # Actually, the book formula says d1 = (1/β)·cot⁻¹(X_C/Z_0)
    # And X_C = 26.53 Ω, so X_C/Z_0 = 0.5306
    # cot⁻¹(0.5306) = atan(1/0.5306) = atan(1.8846) = 62.05° = 1.083 rad
    # d1 = 1.083/81.58 = 0.01328 m = 13.28 mm ✓

    d_cap = (1.0 / beta) * np.arctan(Z0 / XC)

    # Inductor: 5.3 nH
    L_val = 5.3e-9
    XL = 2 * np.pi * f * L_val
    # For open-circuit stub: z(d) = -j*cot(βd)
    # For inductive: -j*cot(βd) = +jXL/Z0 → cot(βd) = -XL/Z0
    # cot is negative in 2nd quadrant → βd = π - atan(Z0/XL)
    d_ind = (1.0 / beta) * (np.pi - np.arctan(Z0 / XL))

    d_cap_mm = d_cap * 1e3
    d_ind_mm = d_ind * 1e3
    lam_mm = lam * 1e3

    print(f"\n  f = {f/1e9:.1f} GHz")
    print(f"  λ = {lam_mm:.2f} mm")
    print(f"  β = {beta:.4f} rad/m")
    print(f"\n  Capacitor (2 pF): Xc = {XC:.2f} Ω")
    print(f"    Stub length d1 = {d_cap_mm:.2f} + n×{lam_mm/2:.2f} mm "
          f"(book: 13.27 + n×38.5 mm)")
    print(f"\n  Inductor (5.3 nH): XL = {XL:.1f} Ω")
    print(f"    Stub length d2 = {d_ind_mm:.2f} + n×{lam_mm/2:.2f} mm "
          f"(book: 32.81 + n×38.5 mm)")

    # Verification via Smith Chart-like plot
    fig, ax = plt.subplots(figsize=(7, 7))
    plot_smith_chart(ax)

    # Open circuit point
    ax.plot(1, 0, 'ko', markersize=6, label='Open ($z_L=\\infty$)')

    # Trace the stub on the chart (along r=0 circle)
    theta = np.linspace(0, -2 * beta * d_cap, 100)
    Gamma_stub_cap = np.exp(1j * theta)
    ax.plot(Gamma_stub_cap.real, Gamma_stub_cap.imag, 'r-', linewidth=2, alpha=0.7,
            label=f'Cap stub: $d_1={d_cap_mm:.2f}$ mm')

    theta = np.linspace(0, -2 * beta * d_ind, 100)
    Gamma_stub_ind = np.exp(1j * theta)
    ax.plot(Gamma_stub_ind.real, Gamma_stub_ind.imag, 'b-', linewidth=2, alpha=0.7,
            label=f'Ind stub: $d_2={d_ind_mm:.2f}$ mm')

    ax.legend(loc='upper right', fontsize=8)
    ax.set_title('Ex3-5: Open-Circuit Stub on Smith Chart')
    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch3_ex3_5_open_stubs.png', dpi=150)
    print(f"  → Saved figure to {FIGS_DIR}/ch3_ex3_5_open_stubs.png")
    plt.close(fig)

    return d_cap, d_ind


# ======================================================================
# Bonus: T-network impedance (Figure 3-17/18)
# ======================================================================
def bonus_t_network():
    """
    T-network with:
      L1 = 4.38 nH (series)
      RL = 31.25 Ω, CL = 1.91 pF (parallel, transistor input)
      C  = 2.39 pF (shunt)
      L2 = 3.98 nH (series)
    Compute Zin at f = 2 GHz.
    """
    print("\n" + "=" * 60)
    print("Bonus: T-network impedance calculation")
    print("=" * 60)

    f = 2e9
    w = 2 * np.pi * f
    Z0 = 50.0

    L1 = 4.38e-9   # series
    RL = 31.25
    CL = 1.91e-12
    C = 2.39e-12   # shunt
    L2 = 3.98e-9   # series

    # Step 1: RL in parallel with CL
    Z_RC = 1.0 / (1.0/RL + 1j * w * CL)
    z_RC = Z_RC / Z0
    print(f"\n  Step 1: Z(RL||CL) = ({Z_RC.real:.2f}{Z_RC.imag:+.2f}j) Ω"
          f" → z = {z_RC.real:.3f}{z_RC.imag:+.3f}j (should be ~0.4-j0.3)")

    # Step 2: Add L1 in series
    Z_L1 = Z_RC + 1j * w * L1
    z_L1 = Z_L1 / Z0
    print(f"  Step 2: + L1     → Z = ({Z_L1.real:.2f}{Z_L1.imag:+.2f}j) Ω"
          f" → z = {z_L1.real:.3f}{z_L1.imag:+.3f}j")

    # Step 3: Convert to admittance, add C in shunt
    Y_before_C = 1.0 / Z_L1
    Y_C = Y_before_C + 1j * w * C
    Z_C = 1.0 / Y_C
    z_C = Z_C / Z0
    print(f"  Step 3: + C shunt → Z = ({Z_C.real:.2f}{Z_C.imag:+.2f}j) Ω"
          f" → z = {z_C.real:.3f}{z_C.imag:+.3f}j (should be ~1-j1)")

    # Step 4: Add L2 in series
    Z_in = Z_C + 1j * w * L2
    z_in = Z_in / Z0
    print(f"  Step 4: + L2     → Zin = ({Z_in.real:.2f}{Z_in.imag:+.2f}j) Ω"
          f" → zin = {z_in.real:.3f}{z_in.imag:+.3f}j (should be ~1.0+j0)")

    SWR = (1 + abs(Z_in - Z0) / (Z_in + Z0)) / (1 - abs(Z_in - Z0) / (Z_in + Z0))
    print(f"\n  VSWR (w.r.t. 50 Ω) = {SWR:.6f}")
    print(f"  Zin matches Z0 = 50 Ω at 2 GHz: {'✅' if abs(SWR-1) < 0.01 else '❌'}")

    # Frequency sweep
    f_sweep = np.linspace(0.5e9, 4e9, 500)
    w_sweep = 2 * np.pi * f_sweep

    Zin_sweep = []
    for w_i in w_sweep:
        Z_RC = 1.0 / (1.0/RL + 1j * w_i * CL)
        Z_after_L1 = Z_RC + 1j * w_i * L1
        Y_after_C = 1.0 / Z_after_L1 + 1j * w_i * C
        Z_after_C = 1.0 / Y_after_C
        Z_in_i = Z_after_C + 1j * w_i * L2
        Zin_sweep.append(Z_in_i)
    Zin_sweep = np.array(Zin_sweep)

    fig, ax = plt.subplots(figsize=(7, 7))
    plot_smith_chart(ax)

    Gamma_sweep = (Zin_sweep - Z0) / (Zin_sweep + Z0)
    ax.plot(Gamma_sweep.real, Gamma_sweep.imag, 'b-', linewidth=1.5, alpha=0.7)
    ax.plot(0, 0, 'ro', markersize=6, label='Match @ 2 GHz')
    ax.legend(loc='upper right', fontsize=8)
    ax.set_title('T-Network Input Impedance (0.5-4 GHz)')
    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch3_t_network_smith.png', dpi=150)
    print(f"  → Saved figure to {FIGS_DIR}/ch3_t_network_smith.png")
    plt.close(fig)

    # Also plot |Zin| and phase vs freq
    fig2, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    ax1.plot(f_sweep/1e9, np.abs(Zin_sweep), 'b-', linewidth=1.5)
    ax1.axvline(2, color='r', linestyle='--', alpha=0.5)
    ax1.set_ylabel('$|Z_{in}|$  ($\\Omega$)')
    ax1.grid(True, alpha=0.3)
    ax1.set_title('T-Network: $|Z_{in}|$ and Phase vs Frequency')

    ax2.plot(f_sweep/1e9, np.angle(Zin_sweep, deg=True), 'b-', linewidth=1.5)
    ax2.axvline(2, color='r', linestyle='--', alpha=0.5, label='2 GHz')
    ax2.axhline(0, color='gray', linestyle=':', alpha=0.3)
    ax2.set_xlabel('Frequency (GHz)')
    ax2.set_ylabel('$\\angle Z_{in}$ (deg)')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    fig2.tight_layout()
    fig2.savefig(f'{FIGS_DIR}/ch3_t_network_Zin.png', dpi=150)
    print(f"  → Saved figure to {FIGS_DIR}/ch3_t_network_Zin.png")
    plt.close(fig2)

    return Z_in


# ======================================================================
# Main
# ======================================================================
if __name__ == '__main__':
    import os
    os.makedirs(FIGS_DIR, exist_ok=True)

    r1 = example_3_1()
    Gamma0, Gammain, Zin = example_3_2()
    r4 = example_3_4()
    d_cap, d_ind = example_3_5()
    Zin_T = bonus_t_network()

    print("\n" + "=" * 60)
    print("✅ Ch3 all examples complete.")
    print("=" * 60)
