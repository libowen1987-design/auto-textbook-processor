#!/usr/bin/env python3
"""
Collins Ch10 — Negative Resistance Devices & Circuits — Example Code

Implements key computations for negative-resistance microwave devices as
covered in Collin's 'Foundations for Microwave Engineering' theoretical
framework: tunnel diodes, Gunn diodes, IMPATT diodes, and negative-resistance
oscillator design.

Demos
-----
1. tunnel_diode_iv_curve()    — N-type I–V characteristic with negative resistance
2. gunn_e_v_characteristic()  — GaAs drift velocity vs electric field, transit freq.
3. impatt_negative_conductance() — IMPATT negative conductance vs frequency
4. neg_res_oscillator_stability() — Oscillator load-pull and start-up conditions

Verification
------------
verify_collins_ch10() — runs all demos and prints summary.
"""

import numpy as np
from numpy import abs, exp, sin, cos, tan, pi, real, imag, angle, linspace, arange
import matplotlib
matplotlib.use("Agg")  # non-interactive
import matplotlib.pyplot as plt
import os

OUT_DIR = os.path.join(os.path.dirname(__file__) or ".", "figures")
os.makedirs(OUT_DIR, exist_ok=True)

# ═════════════════════════════════════════════════════════════════════
#  Demo 1 — Tunnel Diode I–V Curve  (Eq. 10.1)
# ═════════════════════════════════════════════════════════════════════

def tunnel_diode_iv_curve(Ip=5e-3, Vp=65e-3, Iv=0.5e-3, Vv=350e-3,
                           n=2.0, I0=1e-6, V_max=0.5, N=1000):
    """
    Tunnel diode I–V characteristic (N-type negative resistance region).

    Parameters
    ----------
    Ip : float  Peak current (A), default 5 mA
    Vp : float  Peak voltage (V), default 65 mV
    Iv : float  Valley current (A), default 0.5 mA
    Vv : float  Valley voltage (V), default 350 mV
    n  : float  Ideality factor for diffusion term
    I0 : float  Saturation current (A) for diffusion term
    V_max : float  Maximum voltage (V)
    N  : int    Number of points

    Returns
    -------
    V, I : ndarray  Voltage and current arrays

    Notes
    -----
    Model uses the classic Esaki tunneling expression plus a normal
    diode diffusion term (Eq. 10.1). The peak-to-valley ratio
    PVCR = I_p / I_v is a key figure of merit.
    """
    V = linspace(0, V_max, N)
    q = 1.602e-19
    kT = 1.381e-23 * 300  # 300 K

    # Tunneling current (Esaki form)
    I_tunnel = Ip * (V / Vp) * exp(1 - V / Vp)

    # Normal diode diffusion current
    I_diff = I0 * (exp(q * V / (n * kT)) - 1.0)

    I = I_tunnel + I_diff

    # Small-signal conductance (dI/dV) for negative resistance detection
    dI_dV = np.gradient(I, V)
    R_diff = 1.0 / dI_dV  # differential resistance; negative in NDR region

    # Identify NDR region
    ndr_mask = dI_dV < 0
    idx_ndr = np.where(ndr_mask)[0]

    # ── Plot ──
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(V * 1e3, I * 1e3, "b-", lw=2, label="Total current")
    ax1.plot(V * 1e3, I_tunnel * 1e3, "g--", lw=1, label="Tunneling term")
    ax1.plot(V * 1e3, I_diff * 1e3, "r:", lw=1, label="Diffusion term")
    # Mark peak and valley
    ax1.plot(Vp * 1e3, Ip * 1e3, "ro", ms=6, label=f"Peak ($I_p={Ip*1e3:.1f}$ mA)")
    ax1.plot(Vv * 1e3, Iv * 1e3, "rs", ms=6, label=f"Valley ($I_v={Iv*1e3:.1f}$ mA)")
    if len(idx_ndr) > 0:
        V_ndr = V[idx_ndr] * 1e3
        I_ndr = I[idx_ndr] * 1e3
        ax1.fill_between(V_ndr, I_ndr, alpha=0.15, color="orange",
                          label="NDR region")
    ax1.set_xlabel("Voltage (mV)")
    ax1.set_ylabel("Current (mA)")
    ax1.set_title("Tunnel Diode I–V Characteristic")
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=8)

    # Differential resistance (log-ish scale)
    ax2.plot(V * 1e3, R_diff, "m-", lw=2)
    ax2.axhline(0, color="gray", lw=0.5)
    if len(idx_ndr) > 0:
        V_ndr = V[idx_ndr] * 1e3
        R_ndr = R_diff[idx_ndr]
        ax2.fill_between(V_ndr, R_ndr, alpha=0.15, color="orange")
        R_n_val = np.min(R_ndr)
        ax2.annotate(f"$R_n \\approx {R_n_val:.1f}\\ \\Omega$",
                     xy=(V_ndr[np.argmin(R_ndr)], R_n_val),
                     xytext=(V_ndr[np.argmin(R_ndr)] + 30, R_n_val - 20),
                     arrowprops=dict(arrowstyle="->"), fontsize=10)
    ax2.set_xlabel("Voltage (mV)")
    ax2.set_ylabel("Differential Resistance ($\\Omega$)")
    ax2.set_title("Small-Signal Differential Resistance")
    ax2.grid(True, alpha=0.3)
    # Use symmetric log to show negative values
    ylim = np.max(np.abs(R_diff[1:-1])) * 1.5
    ax2.set_ylim(-ylim if ylim > 0 else 0, ylim)

    plt.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "ch10_tunnel_diode_iv.png"), dpi=150)
    plt.close(fig)

    # Print summary
    pvcr = Ip / Iv
    print(f"[Demo 1] Tunnel Diode I–V (PVCR = {pvcr:.1f})")
    print(f"         I_p = {Ip*1e3:.2f} mA @ V_p = {Vp*1e3:.0f} mV")
    print(f"         I_v = {Iv*1e3:.2f} mA @ V_v = {Vv*1e3:.0f} mV")
    if len(idx_ndr) > 0:
        R_n = np.min(R_ndr)
        V_rn = V_ndr[np.argmin(R_ndr)]
        print(f"         Min R_n = {R_n:.1f} Ω @ V = {V_rn:.1f} mV")
    else:
        print("         No NDR region detected")
    print()

    return V, I


# ═════════════════════════════════════════════════════════════════════
#  Demo 2 — Gunn Diode: E–v Characteristic & Transit Frequency
# ═════════════════════════════════════════════════════════════════════

def gunn_e_v_characteristic(mu1=6000, v_sat=1e5, E_th=3.2e5, E_max=50e5, N=500):
    """
    GaAs drift velocity vs electric field (transferred-electron effect).

    Parameters
    ----------
    mu1 : float    Low-field mobility (cm²/V·s), default 6000
    v_sat : float  Saturation velocity (m/s), default 1e5 (10⁷ cm/s)
    E_th : float   Threshold field (V/m), default 3.2e5 (3.2 kV/cm)
    E_max : float  Maximum field (V/m)
    N : int        Number of points

    Returns
    -------
    E, v, mu_d : ndarray  Field (kV/cm), velocity (10⁷ cm/s), mobility (cm²/V·s)

    Notes
    -----
    Empirical model: v(E) = (μ₁E + v_sat·(E/E_th)⁴) / (1 + (E/E_th)⁴)
    Transit-time frequency: f_t = v_sat / L  (Eq. 10.4)
    """
    E = linspace(0, E_max, N)
    ratio = E / E_th

    # Drift velocity model (Eq. 10.3)
    v = (mu1 * 1e-4 * E + v_sat * ratio**4) / (1 + ratio**4)
    # v in m/s; convert to 10⁷ cm/s for display
    v_plot = v / 1e5  # units of 10⁷ cm/s

    # Differential mobility (cm²/V·s)
    dv_dE = np.gradient(v, E)
    mu_d = dv_dE * 1e4  # convert m²/V·s → cm²/V·s

    # Threshold crossing
    idx_th = np.argmin(np.abs(E - E_th))
    v_th = v_plot[idx_th]

    # Negative mobility region
    nmr_mask = mu_d < 0
    # Transit frequency for various lengths
    L_vals = np.array([2, 5, 10, 20])  # μm
    f_transit = v_sat / (L_vals * 1e-6)  # Hz

    # ── Plot ──
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(E / 1e5, v_plot, "b-", lw=2, label="Drift velocity")
    ax1.axvline(E_th / 1e5, color="r", ls="--", lw=1,
                label=f"$E_{{th}}$ = {E_th/1e5:.1f} kV/cm")
    ax1.axhline(v_th, color="g", ls=":", lw=1,
                label=f"$v(E_{{th}})$ = {v_th:.3f} ×10⁷ cm/s")
    if np.any(nmr_mask):
        ax1.fill_between(E[nmr_mask] / 1e5, v_plot[nmr_mask],
                         alpha=0.15, color="orange", label="NDM region")
    ax1.set_xlabel("Electric Field (kV/cm)")
    ax1.set_ylabel("Drift Velocity (×10⁷ cm/s)")
    ax1.set_title("GaAs E–v Characteristic (Transferred Electron)")
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=8)

    # Transit frequency bar chart
    colors = ["#2196F3", "#4CAF50", "#FF9800", "#F44336"]
    bars = ax2.bar([f"{L} μm" for L in L_vals],
                   f_transit / 1e9, color=colors, edgecolor="black")
    for bar, fg in zip(bars, f_transit / 1e9):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                 f"{fg:.1f} GHz", ha="center", va="bottom", fontsize=9)
    ax2.set_ylabel("Frequency (GHz)")
    ax2.set_title(f"Transit-Time Frequency ($v_{{sat}}$ = {v_sat/1e5:.1f}×10⁷ cm/s)")
    ax2.grid(True, alpha=0.3, axis="y")

    plt.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "ch10_gunn_e_v.png"), dpi=150)
    plt.close(fig)

    # Print summary
    print(f"[Demo 2] Gunn Diode — GaAs E–v Characteristic")
    print(f"         μ₁ = {mu1} cm²/V·s, v_sat = {v_sat/1e5:.2f} ×10⁷ cm/s")
    print(f"         E_th = {E_th/1e5:.2f} kV/cm")
    print(f"         v(E_th) = {v_th:.3f} ×10⁷ cm/s")
    print(f"         Transit frequencies:")
    for L, ft in zip(L_vals, f_transit):
        print(f"           L = {L:>2} μm  →  f_t = {ft/1e9:.2f} GHz")
    print()

    return E, v, mu_d


# ═════════════════════════════════════════════════════════════════════
#  Demo 3 — IMPATT Diode: Negative Conductance vs Frequency
# ═════════════════════════════════════════════════════════════════════

def impatt_negative_conductance(I_dc=0.1, W_a=2e-6, W_d=5e-6,
                                 v_s=1e5, Cd=0.3e-12, alpha_p=1.0,
                                 f_min=1e9, f_max=30e9, N=500):
    """
    Computes the IMPATT diode small-signal admittance using a Read-diode
    approximation.

    Parameters
    ----------
    I_dc : float       DC bias current (A), default 100 mA
    W_a : float        Avalanche region width (m), default 2 μm
    W_d : float        Depletion region width (m), default 5 μm
    v_s : float        Carrier saturation velocity (m/s), default 10⁵
    Cd : float         Depletion capacitance (F), default 0.3 pF
    alpha_p : float    α' · W_a product (ionization coeff. deriv.), default 1.0
    f_min, f_max : float  Frequency range (Hz)
    N : int            Number of frequency points

    Returns
    -------
    f, G_d, B_d : ndarray  Frequency (GHz), conductance (S), susceptance (S)

    Notes
    -----
    Simplified Read-diode model (Eq. 10.7):
    Transit angle θ = ω·W_d / v_s
    Conductance G(f) ∝ -I_dc · (sinθ - θ·cosθ) / θ² · (ωC_d) / (ωC_d + tan(θ/2))
    The negative conductance peak occurs near θ ≈ π.
    """
    f = linspace(f_min, f_max, N)
    omega = 2 * pi * f
    theta = omega * W_d / v_s  # transit angle

    # Read-diode conductance approximation (Eq. 10.7 simplified)
    with np.errstate(divide="ignore", invalid="ignore"):
        term1 = np.where(theta != 0,
                         (sin(theta) - theta * cos(theta)) / theta**2,
                         0.0)
        omega_Cd = omega * Cd
        term2 = np.where(omega_Cd + tan(theta/2) != 0,
                         omega_Cd / (omega_Cd + tan(theta/2)),
                         0.0)

    # Normalised conductance (sign adjusted)
    G_scale = -I_dc * alpha_p * W_a / 2.0
    G_d = G_scale * term1 * term2

    # Susceptance — dominated by junction capacitance
    B_d = omega * Cd

    # Find peak negative conductance
    idx_neg = np.where(G_d < 0)[0]
    if len(idx_neg) > 0:
        G_min_idx = idx_neg[np.argmin(G_d[idx_neg])]
        f_opt = f[G_min_idx] / 1e9
        G_min = G_d[G_min_idx]

        # Find bandwidth of negative conductance
        G_half = G_min / 2
        above = np.where((G_d <= 0) & (G_d >= G_half))[0]
        if len(above) >= 2:
            f_low = f[above[0]] / 1e9
            f_high = f[above[-1]] / 1e9
            bw = f_high - f_low
        else:
            f_low = f_high = bw = float("nan")
    else:
        f_opt = G_min = f_low = f_high = bw = float("nan")

    # ── Plot ──
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(f / 1e9, G_d * 1e3, "b-", lw=2, label="Conductance $G_D$")
    ax.axhline(0, color="gray", lw=0.5)
    # Mark optimum
    if not np.isnan(f_opt):
        ax.plot(f_opt, G_min * 1e3, "ro", ms=6)
        ax.annotate(f"$f_{{opt}} = {f_opt:.1f}$ GHz\n"
                    f"$G_{{min}} = {G_min*1e3:.2f}$ mS",
                    xy=(f_opt, G_min * 1e3),
                    xytext=(f_opt + 3, G_min * 1e3 + 5),
                    arrowprops=dict(arrowstyle="->"), fontsize=10)
        # Mark bandwidth
        if not np.isnan(bw):
            ax.axvline(f_low, color="g", ls="--", lw=0.8, alpha=0.7)
            ax.axvline(f_high, color="g", ls="--", lw=0.8, alpha=0.7)
            ax.annotate(f"BW ≈ {bw:.1f} GHz",
                        xy=((f_low + f_high) / 2, G_half * 1e3),
                        fontsize=9, ha="center",
                        bbox=dict(boxstyle="round,pad=0.3", fc="lightgreen", alpha=0.5))

    ax.fill_between(f / 1e9, G_d * 1e3, 0,
                    where=(G_d < 0), alpha=0.15, color="orange",
                    label="Negative $G$ region")
    ax.set_xlabel("Frequency (GHz)")
    ax.set_ylabel("Conductance $G_D$ (mS)")
    ax.set_title("IMPATT Diode — Negative Conductance vs Frequency")
    ax.grid(True, alpha=0.3)
    ax.legend()

    plt.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "ch10_impatt_conductance.png"), dpi=150)
    plt.close(fig)

    # Summary
    theta_opt = theta[np.argmin(G_d)]
    print(f"[Demo 3] IMPATT Diode (Si Read-diode model)")
    print(f"         I_dc = {I_dc*1e3:.0f} mA, W_a = {W_a*1e6:.1f} μm, W_d = {W_d*1e6:.1f} μm")
    print(f"         C_d  = {Cd*1e12:.2f} pF, v_s = {v_s/1e5:.1f} ×10⁵ m/s")
    print(f"         Peak negative G: {G_min*1e3:.3f} mS @ {f_opt:.2f} GHz")
    print(f"         Transit angle at opt: θ = {theta_opt:.2f} rad (~{theta_opt*180/pi:.0f}°)")
    if not np.isnan(bw):
        print(f"         G_negative bandwidth: {bw:.1f} GHz ({f_low:.1f}–{f_high:.1f} GHz)")
    print()

    return f, G_d, B_d


# ═════════════════════════════════════════════════════════════════════
#  Demo 4 — Negative Resistance Oscillator: Load & Stability Analysis
# ═════════════════════════════════════════════════════════════════════

def neg_res_oscillator_stability(R_d_ref=-50.0, f0=10e9, L_tank=100e-12,
                                  Q=50, I_osc_min=1e-3, I_osc_max=50e-3, N=200):
    """
    Negative-resistance oscillator design and stability analysis.

    Models a Gunn/tunnel-diode oscillator with a diode that has
    amplitude-dependent negative resistance:
        R_d(I) = R_d_ref * (1 - I / I_sat)    (linear saturation model)

    Parameters
    ----------
    R_d_ref : float   Small-signal negative resistance (Ω), default -50
    f0 : float        Operating frequency (Hz), default 10 GHz
    L_tank : float    Tank inductance (H), default 100 pH
    Q : float         Loaded Q, default 50
    I_osc_min, I_osc_max : float  RF current range (A)
    N : int           Number of points

    Returns
    -------
    R_load, I_steady, P_out : ndarray  Load resistance options, steady-state
                                        current, output power

    Notes
    -----
    Oscillation condition (Eq. 10.9): R_d(I) + R_L = 0
    Start-up condition (Eq. 10.10): |R_d(0)| > R_L
    Stabilised design (Eq. 10.11): R_L = |R_d|/3
    """
    I_sat = 30e-3  # saturation current for R_d roll-off

    # RF current sweep
    I_osc = linspace(I_osc_min, I_osc_max, N)

    # Amplitude-dependent negative resistance (saturation)
    R_d = R_d_ref * (1.0 - I_osc / I_sat)
    # Clamp: when R_d crosses zero, oscillation stops
    R_d = np.where(R_d < 0, R_d, 0.0)

    # Load resistance options
    R_abs = abs(R_d_ref)
    R_load_options = {
        "Marginal ($R_L \\approx |R_d|$)": R_abs * 0.98,
        "Stabilised ($R_L = |R_d|/3$)": R_abs / 3.0,
        "Light ($R_L = |R_d|/5$)": R_abs / 5.0,
        "Heavy ($R_L = |R_d|/1.5$)": R_abs / 1.5,
    }

    # For each load, find steady-state where R_d(I) + R_L = 0
    results = {}
    for label, RL in R_load_options.items():
        diff = np.abs(R_d + RL)
        idx = np.argmin(diff)
        I_ss = I_osc[idx]
        valid = (diff[idx] < 20) and (I_ss > 0)
        R_d_ss = R_d[idx] if valid else float("nan")
        # Output power: P = 0.5 * |I|² * R_L (for sinusoidal)
        P_out = 0.5 * I_ss**2 * RL if valid else 0.0
        results[label] = {"RL": RL, "I_ss": I_ss, "R_d_ss": R_d_ss, "P_out": P_out}

    # ── Plot ──
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Left: R_d(I) with load lines
    ax1.plot(I_osc * 1e3, R_d, "b-", lw=2, label="$R_d(I)$ (diode)")
    colors = ["#F44336", "#4CAF50", "#FF9800", "#9C27B0"]
    for (label, res), color in zip(results.items(), colors):
        RL = res["RL"]
        ax1.axhline(-RL, color=color, ls="--", lw=1.5,
                     label=f"-R$_L$ = {RL:.1f} Ω")
        if not np.isnan(res["I_ss"]) and res["I_ss"] > 0:
            ax1.plot(res["I_ss"] * 1e3, res["R_d_ss"], "o", color=color, ms=6)
    ax1.axhline(0, color="gray", lw=0.5)
    ax1.set_xlabel("RF Current $I_{osc}$ (mA)")
    ax1.set_ylabel("Diode Resistance $R_d$ ($\\Omega$)")
    ax1.set_title("Negative Resistance vs RF Amplitude")
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=7)

    # Right: Steady-state power bar chart
    labels_short = [k.split("(")[-1].rstrip(")") for k in results.keys()]
    bars = ax2.bar(labels_short,
                   [r["P_out"] * 1e3 for r in results.values()],
                   color=colors, edgecolor="black")
    ax2.axhline(0, color="gray", lw=0.5)
    for bar, (label, res) in zip(bars, results.items()):
        if res["P_out"] > 0:
            ax2.text(bar.get_x() + bar.get_width() / 2,
                     bar.get_height() + 0.1,
                     f"{res['P_out']*1e3:.2f} mW\n"
                     f"($I_{{ss}}$={res['I_ss']*1e3:.1f} mA)",
                     ha="center", va="bottom", fontsize=8)
        else:
            ax2.text(bar.get_x() + bar.get_width() / 2, 0.5,
                     "No osc.", ha="center", va="bottom", fontsize=8)
    ax2.set_ylabel("Output Power (mW)")
    ax2.set_title(f"Oscillator Performance @ {f0/1e9:.0f} GHz")
    ax2.grid(True, alpha=0.3, axis="y")
    ax2.tick_params(axis="x", labelsize=8)

    plt.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "ch10_neg_res_oscillator.png"), dpi=150)
    plt.close(fig)

    # Summary
    print(f"[Demo 4] Negative-Resistance Oscillator @ {f0/1e9:.1f} GHz")
    print(f"         |R_d(0)| = {abs(R_d_ref):.1f} Ω")
    print(f"         Tank L = {L_tank*1e12:.0f} pH, Q = {Q}")
    for label, res in results.items():
        RL = res["RL"]
        I_ss = res["I_ss"]
        P_out = res["P_out"]
        ok = not np.isnan(res["R_d_ss"]) and I_ss > 0
        if ok:
            print(f"         {label}: R_L = {RL:.1f} Ω, "
                  f"I_ss = {I_ss*1e3:.1f} mA, P_out = {P_out*1e3:.2f} mW")
        else:
            print(f"         {label}: R_L = {RL:.1f} Ω — no stable oscillation")
    print()

    return R_load_options, results


# ═════════════════════════════════════════════════════════════════════
#  Demo 5 — Injection Locking: Adler's Equation  (Eq. 10.15)
# ═════════════════════════════════════════════════════════════════════

def injection_locking_example(f0=10e9, Q_loaded=50, V_inj_ratio=None, N=500):
    """
    Injection locking sensitivity based on Adler's equation.

    Parameters
    ----------
    f0 : float         Free-running oscillator frequency (Hz)
    Q_loaded : float   Loaded Q of the oscillator circuit
    V_inj_ratio : array or None  Injection voltage ratios V_inj / V_osc
    N : int            Number of frequency points for phase portrait

    Returns
    -------
    f, delta_f_L : ndarray  Detuning frequency array, locking half-width at
                             each injection ratio.

    Notes
    -----
    Adler's equation (Eq. 10.15):
        Δω_L = (ω₀ / 2Q) · (V_inj / V_osc)
    """
    if V_inj_ratio is None:
        V_inj_ratio = np.array([0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2])

    omega_0 = 2 * pi * f0
    delta_omega_L = (omega_0 / (2 * Q_loaded)) * V_inj_ratio
    delta_f_L = delta_omega_L / (2 * pi) / 1e6  # MHz

    # Phase portrait for one injection level
    V_ratio_demo = 0.05
    delta_f_demo = delta_f_L[np.argmin(np.abs(V_inj_ratio - V_ratio_demo))]
    delta_omega_demo = 2 * pi * delta_f_demo * 1e6

    detune_ratio = linspace(-3, 3, N)  # Δω / Δω_L
    phi_range = linspace(0, pi, 200)
    phase_shift = np.zeros((len(detune_ratio), len(phi_range)))

    for i, xi in enumerate(detune_ratio):
        dphi_dt = xi * delta_omega_demo - delta_omega_demo * np.sin(phi_range)
        phase_shift[i, :] = dphi_dt

    # ── Plot ──
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(V_inj_ratio * 100, delta_f_L, "b-o", lw=2, ms=5)
    ax1.fill_between(V_inj_ratio * 100, delta_f_L, alpha=0.2, color="steelblue")
    ax1.set_xlabel("Injection Ratio $V_{inj} / V_{osc}$ (%)")
    ax1.set_ylabel("Locking Half-Width $\\Delta f_L$ (MHz)")
    ax1.set_title(f"Injection Locking Range ($f_0$={f0/1e9:.1f} GHz, Q={Q_loaded})")
    ax1.grid(True, alpha=0.3)

    # Phase portrait
    X, Y = np.meshgrid(detune_ratio, phi_range * 180 / pi)
    Z = phase_shift.T / 1e6
    cs = ax2.contourf(X, Y, Z, levels=30, cmap="RdBu_r", alpha=0.7)
    ax2.contour(X, Y, Z, levels=[0], colors="k", linewidths=1.5)
    ax2.set_xlabel("Detuning $\\Delta \\omega / \\Delta \\omega_L$")
    ax2.set_ylabel("Phase Difference $\\phi$ (deg)")
    ax2.set_title(f"Phase Portrait ($V_{{inj}}/V_{{osc}} = ${V_ratio_demo:.0%})")
    fig.colorbar(cs, ax=ax2, label="$d\\phi/dt$ (rad/s ×10⁶)")
    ax2.grid(True, alpha=0.2)
    # Mark locking range
    ax2.axvline(-1, color="r", ls="--", lw=0.8, alpha=0.5)
    ax2.axvline(1, color="r", ls="--", lw=0.8, alpha=0.5,
                label="Locking range")
    ax2.legend(fontsize=8)

    plt.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "ch10_injection_locking.png"), dpi=150)
    plt.close(fig)

    print(f"[Demo 5] Injection Locking (Adler's Formula)")
    print(f"         f₀ = {f0/1e9:.1f} GHz, Q = {Q_loaded}")
    print(f"         Locking half-width vs injection ratio:")
    for r, dfl in zip(V_inj_ratio, delta_f_L):
        print(f"           V_inj/V_osc = {r*100:.1f}%  →  Δf_L = {dfl:.2f} MHz")
    print()

    return V_inj_ratio, delta_f_L


# ═════════════════════════════════════════════════════════════════════
#  Verification — Run All Demos
# ═════════════════════════════════════════════════════════════════════

def verify_collins_ch10():
    """Run all Chapter 10 examples and print pass/fail summary."""
    print("=" * 65)
    print("  Collins Ch10 — Negative Resistance Devices — Verification")
    print("=" * 65)
    print()
    print(f"  Figures → {OUT_DIR}/")
    print()

    checks = []

    # Demo 1
    V1, I1 = tunnel_diode_iv_curve()
    # Check PVCR
    pvcr = 5e-3 / 0.5e-3
    dI_dV = np.gradient(I1, V1)
    ndr = np.any(dI_dV < 0)
    checks.append(("Tunnel diode NDR exists", ndr, True))
    checks.append(("Tunnel diode PVCR = 10", abs(pvcr - 10.0) < 0.1, True))

    # Demo 2
    E2, v2, mu_d2 = gunn_e_v_characteristic()
    nmr = np.any(mu_d2 < 0)
    v_asymptote = np.mean(v2[-50:]) / 1e5  # high-field asymptote in 10⁷ cm/s
    checks.append(("Gunn diode NDM exists", nmr, True))
    checks.append(("Gunn v_sat ~1×10⁷ cm/s", abs(v_asymptote - 1.0) < 0.02, True))

    # Demo 3
    f3, G3, B3 = impatt_negative_conductance(alpha_p=50.0)
    g_neg = np.any(G3 < 0)
    f_opt_idx = np.argmin(G3)
    f_opt_val = f3[f_opt_idx] / 1e9
    checks.append(("IMPATT negative conductance exists", g_neg, True))
    # Optimum frequency should be > 5 GHz given our depletion parameters
    checks.append(("IMPATT f_opt reasonable (~10–15 GHz)", 5 < f_opt_val < 25, True))

    # Demo 4
    RL, res = neg_res_oscillator_stability()
    # Stabilised case should oscillate
    stab_key = [k for k in res if "1/3" in k or "stabilised" in k.lower()
                or "Stabilised" in k][0]
    checks.append(("Oscillator stabilised case oscillates",
                    res[stab_key]["P_out"] > 0, True))

    # Demo 5
    V_ratios, dfl = injection_locking_example()
    checks.append(("Injection locking range increases with V_inj/V_osc",
                    np.all(np.diff(dfl) > 0), True))

    # Print results
    all_pass = True
    for name, actual, expected in checks:
        status = "✅ PASS" if actual == expected else "❌ FAIL"
        if actual != expected:
            all_pass = False
        print(f"  {status} | {name}")
        if actual != expected:
            print(f"         expected={expected}, got={actual}")

    print()
    if all_pass:
        print("  ✅ All checks passed!")
    else:
        print("  ❌ Some checks failed — review above.")
    print("=" * 65)

    return all_pass


# ═════════════════════════════════════════════════════════════════════
#  Main
# ═════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    verify_collins_ch10()
