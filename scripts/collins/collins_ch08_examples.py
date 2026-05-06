#!/usr/bin/env python3
"""
Collins Ch8 (2nd Ed. Ch9) — Microwave Tubes
Examples & Demos

Sections:
  1. Klystron gain / bandwidth / efficiency
  2. TWT gain interaction (Pierce small-signal theory)
  3. Magnetron dispersion relation (Hull cutoff + Hartree condition)
  4. Beam focusing simulation (Brillouin flow / confined flow)

References:
  R. E. Collin, Foundations for Microwave Engineering, 2nd ed.,
  IEEE Press, 2001, Ch. 9, pp. 648–712.
"""

import numpy as np
from scipy.special import jv as jn  # Bessel J_n
import matplotlib
matplotlib.use("Agg")  # non-interactive backend for headless env
import matplotlib.pyplot as plt
import os

OUT = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(OUT, exist_ok=True)

# Constants
C0 = 299792458         # speed of light [m/s]
ME = 9.10938356e-31    # electron mass [kg]
QE = 1.60217662e-19    # electron charge [C]
EPS0 = 8.85418782e-12  # vacuum permittivity [F/m]
ETA = QE / ME          # charge-to-mass ratio [C/kg]


# ============================================================
# Demo 1: Klystron Gain / Bandwidth / Efficiency
# ============================================================
def demo_klystron():
    """
    Two-cavity klystron amplifier analysis (Collin §9.7, pp. 678–686).

    Key formulas:
      - Beam coupling coefficient β_i = sin(θ_g/2) / (θ_g/2)    [Eq. 9.16]
      - Bunching parameter X = β_i V_1 θ_0 / (2 V_0)           [Eq. 9.17]
      - Convection current (fundamental): I_2 = 2I_0 β_i J₁(X) [Eq. 9.19]
      - Output power: P_out = I_ind² R_sh / 2                  [Eq. 9.22]
      - Efficiency η = P_out / (I_0 V_0)                      [Eq. 9.25]
    """
    print("=" * 60)
    print("Demo 1: Two-Cavity Klystron — Gain / BW / Efficiency")
    print("=" * 60)

    # --- Parameters (typical X-band klystron) ---
    V0 = 20e3          # beam voltage [V]
    I0 = 2.0           # beam current [A]
    f0 = 10e9          # operating frequency [Hz]
    d_gap = 1e-3       # gap length [m]
    L_drift = 5e-2     # drift space length [m]
    Rsh = 30e3         # output cavity shunt resistance [Ω]
    R_in = 10e3        # input cavity shunt resistance [Ω]

    # DC electron velocity (non-relativistic)
    v0 = np.sqrt(2 * QE * V0 / ME)
    print(f"  DC electron velocity v0 = {v0:.3e} m/s  (v0/c = {v0/C0:.3f})")

    # Gap transit angle
    theta_g = 2 * np.pi * f0 * d_gap / v0
    print(f"  Gap transit angle θ_g = {theta_g:.3f} rad ({np.degrees(theta_g):.1f}°)")

    # Beam coupling coefficient (Eq. 9.16, p. 671)
    beta_i = np.sin(theta_g / 2) / (theta_g / 2) if theta_g != 0 else 1.0
    print(f"  Beam coupling coefficient β_i = {beta_i:.4f}")

    # DC transit angle in drift space
    theta_0 = 2 * np.pi * f0 * L_drift / v0
    print(f"  Drift transit angle θ_0 = {theta_0:.1f} rad")

    # --- Small-signal (low drive, X ≪ 1) ---
    Pin_ss = 1e-3      # input power [W] (0 dBm)
    V1_ss = np.sqrt(2 * Pin_ss * R_in)
    X_ss = beta_i * V1_ss * theta_0 / (2 * V0)  # bunching param (Eq. 9.17, p. 672)
    J1_ss = jn(1, X_ss)
    I2_ss = 2 * I0 * beta_i * J1_ss              # (Eq. 9.19, p. 675)
    Iind_ss = beta_i * I2_ss
    Pout_ss = Iind_ss**2 * Rsh / 2               # (Eq. 9.22, p. 684)
    G_ss = 10 * np.log10(Pout_ss / Pin_ss)
    eta_ss = Pout_ss / (I0 * V0) * 100           # (Eq. 9.25, p. 685)

    print(f"\n  --- Small-Signal (Pin = {Pin_ss*1e3:.1f} mW) ---")
    print(f"  V₁ = {V1_ss:.3f} V, X = {X_ss:.5f}")
    print(f"  P_out = {Pout_ss:.3f} W, Gain = {G_ss:.1f} dB, η = {eta_ss:.4f}%")

    # --- Moderate signal (X ~ 0.5) ---
    X_mod = 0.5
    V1_mod = X_mod * 2 * V0 / (beta_i * theta_0)
    Pin_mod = V1_mod**2 / (2 * R_in)
    J1_mod = jn(1, X_mod)
    I2_mod = 2 * I0 * beta_i * J1_mod
    Iind_mod = beta_i * I2_mod
    Pout_mod = Iind_mod**2 * Rsh / 2
    G_mod = 10 * np.log10(Pout_mod / Pin_mod)
    eta_mod = Pout_mod / (I0 * V0) * 100

    print(f"\n  --- Moderate Signal (X = {X_mod}) ---")
    print(f"  Pin = {Pin_mod:.1f} W, Pout = {Pout_mod/1e3:.2f} kW")
    print(f"  Gain = {G_mod:.1f} dB, η = {eta_mod:.1f}%")

    # --- Bandwidth estimate (cavity loaded Q) ---
    QL = 500
    BW_3dB = f0 / QL
    print(f"\n  3-dB bandwidth (Q_L = {QL}) ≈ {BW_3dB/1e6:.1f} MHz")

    # --- Sweep drive level to find optimum ---
    X_vals = np.linspace(0.05, 5.0, 300)
    J1_X_vals = jn(1, X_vals)
    Pout_sweep = 2 * I0**2 * beta_i**4 * J1_X_vals**2 * Rsh
    Pin_sweep = (X_vals * 2 * V0 / (beta_i * theta_0))**2 / (2 * R_in)
    eta_sweep = np.minimum(Pout_sweep / (I0 * V0) * 100, 60)  # cap at 60%
    Gain_sweep = np.where(Pin_sweep > 0,
                          10 * np.log10(Pout_sweep / Pin_sweep), 0)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(X_vals, eta_sweep, "b-", linewidth=2)
    ax1.axvline(1.841, color="r", ls="--", alpha=0.6,
                label="J₁(X) max @ X=1.841")
    ax1.set_xlabel("Bunching parameter X")
    ax1.set_ylabel("Efficiency (%)")
    ax1.set_title("Klystron Electronic Efficiency")
    ax1.grid(alpha=0.3)
    ax1.legend()

    ax2.plot(X_vals, Gain_sweep, "g-", linewidth=2)
    ax2.set_xlabel("Bunching parameter X")
    ax2.set_ylabel("Power gain (dB)")
    ax2.set_title("Klystron Power Gain vs Drive Level")
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, "ch08_klystron_gain.png"), dpi=150)
    plt.close()
    print("\n  → Saved figures/ch08_klystron_gain.png")

    return {
        "v0": v0, "beta_i": beta_i, "X_ss": X_ss,
        "G_ss": G_ss, "eta_ss": eta_ss
    }


# ============================================================
# Demo 2: TWT Gain Interaction (Pierce Small-Signal Theory)
# ============================================================
def demo_twt():
    """
    Traveling-Wave Tube — Pierce small-signal gain analysis (Collin §9.10, pp. 692–699).

    Key formulas:
      - Pierce gain parameter: C³ = K I₀ / (4 V₀)               [Eq. 9.33]
      - Interaction impedance: K = |E_z|² / (2 β_e² P)         [Eq. 9.34]
      - Space-charge param: QC = ω_q² / (4 ω² C²)              [Eq. 9.35]
      - Detune parameter: b = v₀ / v_p - 1                     [Eq. 9.36]
      - Loss parameter: d = α / (β_e C)                        [Eq. 9.37]
      - Pierce dispersion: (δ² + 4QC)(jδ + b - jd) = -1        [Eq. 9.38]
      - Gain: G = -9.54 + 47.3 C N   (dB)                     [Eq. 9.40]
    """
    print("\n" + "=" * 60)
    print("Demo 2: TWT — Pierce Small-Signal Gain ")
    print("=" * 60)

    # --- Parameters (typical helix TWT, C-band) ---
    V0 = 6e3            # beam voltage [V]
    I0 = 0.5            # beam current [A]
    f0 = 5e9            # operating frequency [Hz]
    K = 50.0            # interaction impedance [Ω] (typical helix)
    L = 0.3             # tube length [m]

    v0 = np.sqrt(2 * QE * V0 / ME)
    beta_e = 2 * np.pi * f0 / v0
    lambda_e = 2 * np.pi / beta_e
    N = L / lambda_e     # electrical length in beam wavelengths

    print(f"  DC beam velocity v0 = {v0:.3e} m/s")
    print(f"  β_e = {beta_e:.2f} rad/m, λ_e = {lambda_e:.3f} m")
    print(f"  Tube length N = {N:.1f} λ_e")

    # Pierce gain parameter C (Eq. 9.33, p. 693)
    C = (K * I0 / (4 * V0))**(1/3)
    print(f"  Pierce gain parameter C = {C:.5f}")

    # Gain (Eq. 9.40, p. 696, synchronous lossless QC=0)
    G_db = -9.54 + 47.3 * C * N
    print(f"  Small-signal gain G = {G_db:.1f} dB")

    # --- Space-charge parameter QC ---
    # Estimate plasma frequency for beam radius a = 1 mm
    a_beam = 1e-3
    rho0 = I0 / (np.pi * a_beam**2 * v0)
    omega_p = np.sqrt(QE * rho0 / (ME * EPS0))      # (Eq. 9.6, p. 655)
    R_factor = 0.5                                    # typical reduction factor
    omega_q = R_factor * omega_p                      # (Eq. 9.7, p. 656)
    omega = 2 * np.pi * f0
    QC = omega_q**2 / (4 * omega**2 * C**2)           # (Eq. 9.35, p. 694)
    print(f"  Beam radius a = {a_beam*1e3:.2f} mm")
    print(f"  Plasma freq f_p = {omega_p/(2*np.pi)/1e9:.2f} GHz")
    print(f"  Reduced plasma freq f_q = {omega_q/(2*np.pi)/1e9:.2f} GHz")
    print(f"  Space-charge parameter QC = {QC:.4f}")

    # --- Pierce dispersion solution: growth factor vs detuning ---
    # Solve (δ² + 4QC)(jδ + b - jd) = -1 for the growing-wave root
    b_vals = np.linspace(-3, 3, 500)
    growth = np.zeros_like(b_vals)
    for i, b in enumerate(b_vals):
        coeffs = [1, 1j * b, 4 * QC, 1j * b * 4 * QC + 1]
        roots = np.roots(coeffs)
        growth[i] = np.max(np.real(roots))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(b_vals, growth, "b-", linewidth=2)
    ax1.axvline(0, color="r", ls="--", alpha=0.4, label="b = 0 (synchronous)")
    ax1.set_xlabel("Detune parameter b")
    ax1.set_ylabel("Growth factor Re(δ)")
    ax1.set_title(f"Pierce TWT: Growth vs Detune\n(QC = {QC:.3f})")
    ax1.grid(alpha=0.3)
    ax1.legend()

    # --- Frequency response via detuning model ---
    freq_vals = np.linspace(3e9, 8e9, 200)
    G_freq = np.zeros_like(freq_vals)
    omega_f = 2 * np.pi * freq_vals
    # Phase velocity variation modeled as linear detuning
    # v_p/v_0 - 1 ≈ s * (f - f₀)/f₀ with empirical slope
    s = 2.0
    for i, f in enumerate(freq_vals):
        beta_f = 2 * np.pi * f / v0
        N_f = L / (2 * np.pi / beta_f)
        b_f = s * (f - f0) / f0
        C_f = C * (f / f0)**0.3  # mild frequency dependence of K
        # Look up growth factor for this detuning
        idx = np.argmin(np.abs(b_vals - b_f))
        G_freq[i] = -9.54 + 47.3 * C_f * N_f * growth[idx]

    ax2.plot(freq_vals / 1e9, G_freq, "g-", linewidth=2)
    ax2.axvline(f0 / 1e9, color="r", ls="--", alpha=0.4,
                label=f"f₀ = {f0/1e9:.0f} GHz")
    ax2.set_xlabel("Frequency (GHz)")
    ax2.set_ylabel("Gain (dB)")
    ax2.set_title("TWT Gain vs Frequency")
    ax2.grid(alpha=0.3)
    ax2.legend()

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, "ch08_twt_gain.png"), dpi=150)
    plt.close()
    print("  → Saved figures/ch08_twt_gain.png")

    return {"C": C, "N": N, "G_db": G_db, "QC": QC, "v0": v0}


# ============================================================
# Demo 3: Magnetron Dispersion Relation
# ============================================================
def demo_magnetron():
    """
    Magnetron — Hull cutoff and Hartree threshold (Collin §9.9, pp. 690–692).

    Key formulas:
      - Hull cutoff field: B_c0 = sqrt(2mV₀/e) / [r_a (1 - (r_c/r_a)²)] [Eq. 9.30]
      - Hartree condition: V₀ expressed as function of B, ω, r_a, n     [Eq. 9.31]
      - Inter-cavity phase shift: φ = 2πm/N                            [Eq. 9.32]
      - π-mode corresponds to n = N/2
    """
    print("\n" + "=" * 60)
    print("Demo 3: Magnetron — Hull Cutoff, Hartree Threshold")
    print("=" * 60)

    # --- Parameters (S-band magnetron) ---
    V0 = 12e3           # anode voltage [V]
    r_c = 3e-3          # cathode radius [m]
    r_a = 10e-3         # anode radius [m]
    N_cav = 8           # number of cavities
    f0 = 2.45e9         # operating frequency [Hz]

    omega = 2 * np.pi * f0
    n_pi = N_cav // 2   # π-mode index

    # Hull cutoff field (Eq. 9.30, p. 691)
    B_hull = (np.sqrt(2 * ME * V0 / QE) /
              (r_a * (1 - (r_c / r_a)**2)))
    print(f"  V₀ = {V0/1e3:.0f} kV, r_a = {r_a*1e3:.1f} mm, r_c = {r_c*1e3:.1f} mm")
    print(f"  N_cav = {N_cav}, π-mode n = {n_pi}")
    print(f"  Hull cutoff field B_c0 = {B_hull:.4f} T")

    # Hull cutoff: V vs B
    B_vals = np.linspace(0.01, 0.4, 300)
    V_hull = (QE * B_vals**2 * r_a**2 / (2 * ME)) * (1 - (r_c / r_a)**2)**2

    # Hartree condition (Eq. 9.31, p. 691)
    term1 = (QE * B_vals**2 * r_a**2 / (2 * ME)) * (1 - (r_c / r_a)**2)**2
    term2 = (ME * omega**2 * r_a**2 / (2 * QE * n_pi**2)) * (1 - (r_c / r_a)**2)
    V_hartree = term1 - term2

    # Operating point (find B where Hartree gives our V0)
    B_oper = np.interp(V0, V_hartree, B_vals)
    print(f"  Operating B (π-mode) = {B_oper:.4f} T")
    print(f"  Hull cutoff at same V₀: {np.interp(V0, V_hull, B_vals):.4f} T")

    # Additional mode: n = n_pi - 1 (nearest neighbor)
    n_alt = n_pi - 1
    term2_alt = (ME * omega**2 * r_a**2 / (2 * QE * n_alt**2)) * \
                (1 - (r_c / r_a)**2)
    V_hartree_alt = term1 - term2_alt

    # --- Plot magnetron operating diagram ---
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.fill_between(B_vals * 1e3, V_hull / 1e3, alpha=0.12, color="red",
                    label="Hull cutoff (no anode current)")
    ax.plot(B_vals * 1e3, V_hull / 1e3, "r-", linewidth=2)
    ax.plot(B_vals * 1e3, V_hartree / 1e3, "b-", linewidth=2,
            label=f"Hartree threshold (π-mode, n={n_pi})")
    ax.plot(B_vals * 1e3, V_hartree_alt / 1e3, "g--", linewidth=1.5,
            label=f"Adjacent mode (n={n_alt})")
    ax.plot(B_oper * 1e3, V0 / 1e3, "ko", markersize=10,
            label=f"Operating point ({B_oper*1e3:.1f} mT, {V0/1e3:.0f} kV)")
    ax.set_xlabel("Magnetic field B (mT)")
    ax.set_ylabel("Anode voltage V₀ (kV)")
    ax.set_title(f"Magnetron: Hull & Hartree Conditions\n"
                 f"f₀ = {f0/1e9:.2f} GHz, N = {N_cav}")
    ax.legend(loc="upper left")
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig(os.path.join(OUT, "ch08_magnetron_dispersion.png"), dpi=150)
    plt.close()
    print("  → Saved figures/ch08_magnetron_dispersion.png")

    return {"B_hull": B_hull, "B_oper": B_oper, "n_pi": n_pi}


# ============================================================
# Demo 4: Beam Focusing Simulation
# ============================================================
def demo_beam_focusing():
    """
    Electron beam focusing — Brillouin flow (Collin §9.2, pp. 650–654).

    Simulates trajectories of electrons launched from a cathode under:
      (a) No magnetic field → beam diverges
      (b) Weak focusing → partial confinement
      (c) Strong focusing (B >> B_b) → confined beam
    """
    print("\n" + "=" * 60)
    print("Demo 4: Electron Beam Focusing")
    print("=" * 60)

    # --- Beam parameters ---
    V0 = 6e3            # beam voltage [V]
    I0 = 0.075          # beam current [A]
    a_beam = 0.5e-3     # beam radius [m]

    v0 = np.sqrt(2 * QE * V0 / ME)
    rho0 = I0 / (np.pi * a_beam**2 * v0)
    omega_p = np.sqrt(QE * rho0 / (ME * EPS0))
    perveance = I0 / V0**1.5 * 1e6  # µP

    print(f"  V₀ = {V0/1e3:.1f} kV, I₀ = {I0*1e3:.1f} mA")
    print(f"  Beam radius a = {a_beam*1e3:.2f} mm")
    print(f"  Perveance = {perveance:.2f} µP")
    print(f"  Plasma freq f_p = {omega_p/(2*np.pi)/1e6:.2f} MHz")

    # --- Brillouin field (derived from radial force balance) ---
    # For a uniform beam in Brillouin flow:
    # eB²/(4m) = eE_r/r = eρ₀/(2ε₀) → B = sqrt(2mρ₀/(eε₀))
    B_brill = np.sqrt(ME * rho0 / (QE * EPS0))
    print(f"\n  Brillouin field B_b = {B_brill:.4f} T")
    f_Larmor = QE * B_brill / (4 * np.pi * ME) / 1e6
    print(f"  Larmor frequency = {f_Larmor:.1f} MHz")

    # --- Radial electron trajectory simulation ---
    def simulate_trajectories(B0, n_particles=8, L_sim=0.15):
        """
        Single-particle model: radial equation of motion
        including space-charge field and magnetic focusing.
        """
        N_steps = 2000
        dt = L_sim / (v0 * N_steps)
        omega_c = QE * B0 / ME     # cyclotron frequency

        # Initial radii (uniform across beam cross-section)
        r0 = np.linspace(0.1 * a_beam, a_beam, n_particles)
        r = r0.copy()
        vr = np.zeros(n_particles)   # no initial radial velocity
        vtheta = np.zeros(n_particles)
        z = np.linspace(0, L_sim, N_steps)
        r_traj = np.zeros((N_steps, n_particles))

        for i in range(N_steps):
            r_traj[i, :] = r
            # Radial space-charge field (Gauss's law, uniform beam)
            Er = rho0 * r / (2 * EPS0)       # inside beam
            # Radial acceleration:
            # d²r/dt² = η*Er + vθ²/r - vθ*ω_c
            r_safe = np.maximum(r, 1e-12)
            ar = ETA * Er + vtheta**2 / r_safe - vtheta * omega_c
            a_theta = -vr * vtheta / r_safe - vr * omega_c

            # Euler update with clipping for stability
            vr = np.clip(vr + ar * dt, -1e8, 1e8)
            vtheta = vtheta + a_theta * dt
            r = np.clip(r + vr * dt, 1e-9, 5e-3)

        return z * 1e3, r_traj * 1e3  # [mm]

    # Run for three cases
    cases = [
        ("B = 0 (unfocused)", 0.0, "red"),
        ("B = 0.1 T (partial)", 0.1, "blue"),
        ("B = 0.3 T (strong)", 0.3, "green"),
    ]

    fig, axes = plt.subplots(3, 1, figsize=(10, 9), sharex=True)

    for idx, (label, B0, color) in enumerate(cases):
        z_mm, r_mm = simulate_trajectories(B0)
        ax = axes[idx]
        for p in range(r_mm.shape[1]):
            ax.plot(z_mm, r_mm[:, p], color=color, alpha=0.5, linewidth=0.8)
        ax.axhline(a_beam * 1e3, color="k", ls=":", alpha=0.4,
                   label=f"Initial radius ({a_beam*1e3:.1f} mm)")
        ax.set_ylabel("Radius r (mm)")
        ax.set_title(f"{label}  (B = {B0:.2f} T)")
        ax.grid(alpha=0.3)
        ax.set_ylim(0, 4.5)
        ax.legend(loc="upper right")

    axes[-1].set_xlabel("Axial distance z (mm)")
    plt.tight_layout()
    plt.savefig(os.path.join(OUT, "ch08_beam_focusing.png"), dpi=150)
    plt.close()
    print("\n  → Saved figures/ch08_beam_focusing.png")

    return {"B_brill": B_brill, "rho0": rho0}


# ============================================================
# Verification Function
# ============================================================
def verify_collins_ch08():
    """
    Run all demos and verify key results against expected ranges.
    """
    print("\n" + "#" * 70)
    print("# Collins Ch8 Verification — Microwave Tubes")
    print("#" * 70)

    all_ok = True

    # --- Klystron ---
    print("\n--- Klystron Verification ---")
    kly = demo_klystron()
    checks = [
        ("β_i between 0.5 and 1.0", 0.5 < kly["beta_i"] < 1.0),
        ("Small-signal gain > 0 dB", kly["G_ss"] > 0),
        ("Efficiency < 100%", kly["eta_ss"] < 100),
    ]
    for desc, ok in checks:
        status = "✅" if ok else "❌"
        print(f"  {status} {desc}")
        all_ok &= ok

    # --- TWT ---
    print("\n--- TWT Verification ---")
    twt = demo_twt()
    checks_twt = [
        ("Pierce C between 0.001 and 0.5", 0.001 < twt["C"] < 0.5),
        ("N > 0", twt["N"] > 0),
        ("Gain > 0 dB", twt["G_db"] > 0),
        ("QC >= 0", twt["QC"] >= 0),
    ]
    for desc, ok in checks_twt:
        status = "✅" if ok else "❌"
        print(f"  {status} {desc}")
        all_ok &= ok

    # --- Magnetron ---
    print("\n--- Magnetron Verification ---")
    mag = demo_magnetron()
    checks_mag = [
        ("B_hull > 0 T", mag["B_hull"] > 0),
        ("B_oper > 0 T", mag["B_oper"] > 0),
        ("n_pi >= 1", mag["n_pi"] >= 1),
    ]
    for desc, ok in checks_mag:
        status = "✅" if ok else "❌"
        print(f"  {status} {desc}")
        all_ok &= ok

    # --- Beam focusing ---
    print("\n--- Beam Focusing Verification ---")
    bf = demo_beam_focusing()
    checks_bf = [
        ("B_brill > 0 T", bf["B_brill"] > 0),
        ("rho0 > 0", bf["rho0"] > 0),
    ]
    for desc, ok in checks_bf:
        status = "✅" if ok else "❌"
        print(f"  {status} {desc}")
        all_ok &= ok

    print("\n" + "=" * 70)
    if all_ok:
        print("✅ ALL VERIFICATIONS PASSED")
    else:
        print("❌ SOME VERIFICATIONS FAILED")
    print("=" * 70 + "\n")

    return all_ok


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    verify_collins_ch08()
