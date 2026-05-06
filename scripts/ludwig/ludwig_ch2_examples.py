#!/usr/bin/env python3
"""
ludwig_ch2_examples.py — Chapter 2: Transmission Line Analysis
RF Circuit Design, 2nd Ed., Ludwig & Bogdanov

Examples covered:
  Ex2-3: Line parameters of parallel-plate transmission line
  Ex2-5: Microstrip line design (synthesis and analysis)
  Ex2-6: Short-circuit transmission line impedance vs frequency
  Ex2-7: Open-circuit transmission line impedance vs frequency
  Ex2-8: Quarter-wave transformer matching
  Ex2-10: Power considerations for sourced/loaded TL
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
    'legend.fontsize': 10,
    'figure.dpi': 120,
})

FIGS_DIR = '/home/ubuntu/.openclaw/workspace/textbooks/ludwig/figures'
mu0 = const.mu_0
eps0 = const.epsilon_0
c0 = const.c


def skin_depth(f, sigma):
    """Skin depth δ = 1 / sqrt(π f μ0 σ) [m]."""
    return 1.0 / np.sqrt(np.pi * f * mu0 * sigma)


# ======================================================================
# Example 2-3: Line parameters of parallel-plate transmission line
# ======================================================================
def example_2_3():
    """
    Parallel copper-plate line at f=1 GHz.
    w=6 mm, d=1 mm, εr=2.25, σ_diel=0.125 mS/m
    """
    print("=" * 60)
    print("Example 2-3: Line parameters of parallel-plate TL")
    print("=" * 60)

    sigma_Cu = 64.516e6
    f = 1e9
    w = 6e-3
    d = 1e-3
    eps_r = 2.25
    sigma_diel = 0.125e-3

    delta = skin_depth(f, sigma_Cu)
    R_per_m = 2.0 / (w * sigma_Cu * delta)
    L_s_per_m = 2.0 / (w * sigma_Cu * (2 * np.pi * f) * delta)  # skin inductance
    L_per_m = mu0 * d / w  # mutual inductance
    C_per_m = eps0 * eps_r * w / d
    G_per_m = sigma_diel * w / d

    print(f"\n  δ = {delta*1e6:.2f} μm")
    print(f"  R  = {R_per_m:.3f} Ω/m")
    print(f"  Ls = {L_s_per_m*1e9:.3f} nH/m  (skin inductance, negligible)")
    print(f"  L  = {L_per_m*1e9:.1f} nH/m  (mutual inductance)")
    print(f"  C  = {C_per_m*1e12:.1f} pF/m")
    print(f"  G  = {G_per_m*1e3:.3f} mS/m")
    print(f"  Z0 = {np.sqrt(L_per_m/C_per_m):.2f} Ω")

    return {'R': R_per_m, 'L': L_per_m, 'C': C_per_m, 'G': G_per_m,
            'Z0': np.sqrt(L_per_m/C_per_m)}


# ======================================================================
# Example 2-5: Microstrip line design
# ======================================================================
def example_2_5():
    """
    Design a 50 Ω microstrip on FR-4.
    εr=4.6, h=40 mil. Find w, εeff, vp, λ at 2 GHz.
    """
    print("\n" + "=" * 60)
    print("Example 2-5: Microstrip line design")
    print("=" * 60)

    Z0_target = 50.0
    eps_r = 4.6
    h = 40e-3 * 0.0254  # 40 mil → m
    f = 2e9

    # Synthesis: compute w/h
    A = (Z0_target / 60.0) * np.sqrt((eps_r + 1.0) / 2.0) \
        + ((eps_r - 1.0) / (eps_r + 1.0)) * (0.23 + 0.11 / eps_r)
    w_h = 8 * np.exp(A) / (np.exp(2 * A) - 2)  # assume w/h ≤ 2

    # Analysis: compute εeff
    eps_eff = (eps_r + 1.0) / 2.0 + (eps_r - 1.0) / 2.0 * 1.0 / np.sqrt(1 + 12 * h / (w_h * h))

    # Check which formula to use
    if w_h <= 1:
        Z0_calc = (np.sqrt(mu0/eps0) / (2 * np.pi * np.sqrt(eps_eff))) \
                  * np.log(8 / w_h + w_h / 4)
    else:
        Z0_calc = (np.sqrt(mu0/eps0) / np.sqrt(eps_eff)) / \
                  (w_h + 1.393 + 0.667 * np.log(w_h + 1.444))

    w = w_h * h
    vp = c0 / np.sqrt(eps_eff)
    lam = vp / f

    print(f"\n  Given: Z0_target = {Z0_target} Ω")
    print(f"         εr = {eps_r}, h = {h*1e3:.4f} mm")
    print(f"\n  Results:")
    print(f"    w/h    = {w_h:.4f}")
    print(f"    w      = {w*1e3:.4f} mm ({w/25.4e-6:.1f} mil)")
    print(f"    εeff   = {eps_eff:.4f}")
    print(f"    Z0_calc= {Z0_calc:.3f} Ω")
    print(f"    vp     = {vp:.4e} m/s")
    print(f"    λ @ 2G = {lam*1e3:.2f} mm")

    # Plot Z0 vs w/h for this substrate
    w_h_range = np.logspace(-1, 1.5, 200)
    eps_eff_range = (eps_r + 1.0) / 2.0 + (eps_r - 1.0) / 2.0 * 1.0 / np.sqrt(1 + 12 / w_h_range)

    Z0_narrow = (np.sqrt(mu0/eps0) / (2 * np.pi * np.sqrt(eps_eff_range))) \
                * np.log(8 / w_h_range + w_h_range / 4)
    Z0_wide = (np.sqrt(mu0/eps0) / np.sqrt(eps_eff_range)) / \
              (w_h_range + 1.393 + 0.667 * np.log(w_h_range + 1.444))

    # Combine: use narrow for w/h <= 1, wide for w/h >= 1
    Z0_all = np.where(w_h_range <= 1, Z0_narrow, Z0_wide)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogx(w_h_range, Z0_all, 'b-', linewidth=2)
    ax.axhline(Z0_target, color='r', linestyle='--', alpha=0.5,
               label=f'$Z_0 = {Z0_target}\\ \\Omega$')
    ax.axvline(w_h, color='g', linestyle=':', alpha=0.5,
               label=f'$w/h = {w_h:.2f}$ (design)')
    ax.plot(w_h, Z0_calc, 'ro', markersize=6)
    ax.set_xlabel('$w/h$')
    ax.set_ylabel('$Z_0$  ($\\Omega$)')
    ax.set_title(f'Microstrip $Z_0$ vs $w/h$ ($\\varepsilon_r={eps_r}$)')
    ax.legend()
    ax.grid(True, which='both', alpha=0.3)
    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch2_microstrip_Z0.png', dpi=150)
    print(f"\n  → Saved figure to {FIGS_DIR}/ch2_microstrip_Z0.png")
    plt.close(fig)

    return {'Z0': Z0_calc, 'w': w, 'eps_eff': eps_eff, 'vp': vp, 'lambda': lam}


# ======================================================================
# Helper: TL input impedance
# ======================================================================
def zin_terminated(Z0, ZL, beta_d):
    """Input impedance of terminated lossless line at electrical length βd."""
    t = np.tan(beta_d)
    return Z0 * (ZL + 1j * Z0 * t) / (Z0 + 1j * ZL * t)


# ======================================================================
# Examples 2-6 and 2-7: Short and open circuit TL vs frequency
# ======================================================================
def examples_2_6_7():
    """
    l=10 cm TL with L=209.4 nH/m, C=119.5 pF/m.
    Plot |Zin| for short and open termination, f=1-4 GHz.
    """
    print("\n" + "=" * 60)
    print("Examples 2-6/7: Short/Open circuit TL impedance vs freq")
    print("=" * 60)

    L = 209.4e-9
    C = 119.5e-12
    Z0 = np.sqrt(L / C)
    vp = 1.0 / np.sqrt(L * C)
    l = 0.10  # m

    print(f"  Z0 = {Z0:.2f} Ω")
    print(f"  vp = {vp:.4e} m/s")

    f = np.linspace(1e9, 4e9, 2000)
    beta = 2 * np.pi * f / vp
    beta_d = beta * l

    Z_short = zin_terminated(Z0, 0, beta_d)
    Z_open = zin_terminated(Z0, 1e12, beta_d)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

    ax1.plot(f / 1e9, np.abs(Z_short), 'b-', linewidth=1.5)
    ax1.axhline(0, color='gray', alpha=0.3)
    ax1.set_xlabel('Frequency (GHz)')
    ax1.set_ylabel('$|Z_{in}|$  ($\\Omega$)')
    ax1.set_title('Short-Circuit Line')
    ax1.grid(True, alpha=0.3)

    # Mark resonance points
    for f_res in [1.0, 2.0, 3.0, 4.0]:
        ax1.axvline(f_res, color='r', linestyle='--', alpha=0.2)
    ax1.annotate('short', xy=(2.0, 10), fontsize=9, color='r')
    ax1.annotate('open', xy=(1.5, 500), fontsize=9, color='r')

    ax2.plot(f / 1e9, np.abs(Z_open), 'b-', linewidth=1.5)
    ax2.axhline(0, color='gray', alpha=0.3)
    ax2.set_xlabel('Frequency (GHz)')
    ax2.set_ylabel('$|Z_{in}|$  ($\\Omega$)')
    ax2.set_title('Open-Circuit Line')
    ax2.grid(True, alpha=0.3)

    for f_res in [1.0, 2.0, 3.0, 4.0]:
        ax2.axvline(f_res, color='r', linestyle='--', alpha=0.2)
    ax2.annotate('open', xy=(2.0, 500), fontsize=9, color='r')
    ax2.annotate('short', xy=(1.5, 10), fontsize=9, color='r')

    fig.suptitle(f'Ex2-6/7: $l=10$ cm, $Z_0={Z0:.1f}\\ \\Omega$, $v_p={vp:.2e}$ m/s')
    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch2_short_open_TL.png', dpi=150)
    print(f"  → Saved figure to {FIGS_DIR}/ch2_short_open_TL.png")
    plt.close(fig)

    return Z0, vp


# ======================================================================
# Example 2-8: Quarter-wave transformer
# ======================================================================
def example_2_8():
    """
    Match ZL=25 Ω transistor to 50 Ω line at 500 MHz.
    Parallel-plate: d=1 mm, εr=4.
    """
    print("\n" + "=" * 60)
    print("Example 2-8: λ/4 transformer matching")
    print("=" * 60)

    ZL = 25.0
    Zin = 50.0       # desired input impedance (same as source line)
    f0 = 500e6

    # Quarter-wave transformer impedance
    Z0_qw = np.sqrt(ZL * Zin)
    print(f"\n  Z0_qw = √({ZL} × {Zin}) = {Z0_qw:.3f} Ω")

    # Parallel-plate design
    d = 1e-3
    eps_r = 4.0
    eps = eps0 * eps_r
    mu = mu0

    # Z0 = (d/w) * sqrt(μ/ε) → w = d * sqrt(μ/ε) / Z0
    w = d * np.sqrt(mu / eps) / Z0_qw
    L = mu * d / w
    C_val = eps * w / d

    # Length: λ/4
    vp = 1.0 / np.sqrt(L * C_val)
    lam = vp / f0
    l_qw = lam / 4

    print(f"  w = {w*1e3:.3f} mm")
    print(f"  L = {L*1e9:.1f} nH/m")
    print(f"  C = {C_val*1e12:.1f} pF/m")
    print(f"  vp = {vp:.4e} m/s")
    print(f"  l_qw = {l_qw*1e3:.3f} mm  (= λ/4 @ 500 MHz)")

    # Plot |Zin| vs frequency
    f = np.linspace(10e6, 2e9, 2000)
    beta = 2 * np.pi * f / vp
    Zin_f = zin_terminated(Z0_qw, ZL, beta * l_qw)

    # Reflection coefficient magnitude
    Gamma_in = (Zin_f - Z0_qw) / (Zin_f + Z0_qw)
    # Actually, we need the overall Γ seen from the source line (Z0_source = Zin = 50 Ω)
    # The transformer Z0_qw is between source (Zin=50) and load (ZL=25).
    # Looking into the transformer + load from the source side:
    Gamma_total = (Zin_f - Zin) / (Zin_f + Zin)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

    ax1.plot(f / 1e9, np.abs(Zin_f), 'b-', linewidth=1.5)
    ax1.axhline(Zin, color='r', linestyle='--', alpha=0.5,
                label=f'$Z_{{in}} = {Zin}\\ \\Omega$ (target)')
    ax1.axvline(f0 / 1e9, color='g', linestyle=':', alpha=0.5,
                label=f'$f_0 = {f0/1e9:.1f}$ GHz')
    ax1.set_xlabel('Frequency (GHz)')
    ax1.set_ylabel('$|Z_{in}|$  ($\\Omega$)')
    ax1.set_title('$\\lambda/4$ Transformer: $|Z_{in}|$ vs $f$')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(f / 1e9, np.abs(Gamma_total), 'b-', linewidth=1.5)
    ax2.axvline(f0 / 1e9, color='g', linestyle=':', alpha=0.5)
    ax2.set_xlabel('Frequency (GHz)')
    ax2.set_ylabel('$|\\Gamma_{in}|$')
    ax2.set_title('$\\lambda/4$ Transformer: Reflection Coefficient')
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch2_quarter_wave_transformer.png', dpi=150)
    print(f"  → Saved figure to {FIGS_DIR}/ch2_quarter_wave_transformer.png")
    plt.close(fig)

    # VSWR at design frequency
    Gamma0 = (ZL - Z0_qw) / (ZL + Z0_qw)
    VSWR_at_load = (1 + abs(Gamma0)) / (1 - abs(Gamma0))
    print(f"\n  VSWR (load side) = {VSWR_at_load:.4f}")
    print(f"  VSWR (source, @ f0) = 1.0 (perfect match)")

    return Z0_qw, w, l_qw


# ======================================================================
# Example 2-10: Power considerations
# ======================================================================
def example_2_10():
    """
    Lossless line: Z0=75 Ω, ZG=50 Ω, ZL=40 Ω, l=λ/2, VG=5 V.
    Compute Pin and PL in W and dBm.
    """
    print("\n" + "=" * 60)
    print("Example 2-10: Power considerations")
    print("=" * 60)

    Z0 = 75.0
    ZG = 50.0
    ZL = 40.0
    VG = 5.0

    # For l = λ/2, tan(βl) = 0 → Z_in = Z_L (λ/2 invariance)
    Z_in = ZL  # half-wave line: Z_in = Z_L

    # Direct lumped power calculation:
    # P_in = (1/2) * Re(V_in * I_in*) = (|V_G|²/2) * R_in / |Z_in + Z_G|²
    Pin = (VG**2 / 2.0) * Z_in / ((Z_in + ZG)**2)

    # Maximum available power from generator (conjugate match: Z_in = Z_G*)
    Pavs = VG**2 / (8 * ZG)

    print(f"\n  Z_in (λ/2 line) = Z_L = {Z_in} Ω")
    print(f"  Pin = PL = {Pin*1e3:.2f} mW = {10*np.log10(Pin/1e-3):.2f} dBm")
    print(f"  Pavs = {Pavs*1e3:.2f} mW (conjugate match)")
    print(f"  Pin/Pavs = {Pin/Pavs:.4f} = {10*np.log10(Pin/Pavs):.2f} dB")

    # Sweep load impedance
    ZL_range = np.linspace(10, 200, 500)
    PL_range = (VG**2 / 2.0) * ZL_range / ((ZL_range + ZG)**2)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(ZL_range, PL_range * 1e3, 'b-', linewidth=2)
    ax.axvline(Z0, color='r', linestyle='--', alpha=0.5,
               label=f'$Z_L = Z_0 = {Z0}\\ \\Omega$')
    ax.axhline(Pavs * 1e3, color='g', linestyle=':', alpha=0.5,
               label=f'$P_{{avs}} = {Pavs*1e3:.2f}$ mW')
    ax.plot(ZL, Pin * 1e3, 'ro', markersize=6,
            label=f'$Z_L={ZL}\\ \\Omega$ (Ex2-10)')
    ax.set_xlabel('$Z_L$ ($\\Omega$)')
    ax.set_ylabel('$P_L$ (mW)')
    ax.set_title(f'Load Power vs $Z_L$ ($Z_0={Z0}\\ \\Omega$, $Z_G={ZG}\\ \\Omega$)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch2_power_vs_ZL.png', dpi=150)
    print(f"  → Saved figure to {FIGS_DIR}/ch2_power_vs_ZL.png")
    plt.close(fig)

    return {'Pin_W': Pin, 'Pin_dBm': 10*np.log10(Pin/1e-3), 'Pavs_W': Pavs}


# ======================================================================
# Bonus: VSWR and Return Loss vs Γ
# ======================================================================
def bonus_vswr_rl():
    """Plot VSWR and Return Loss vs |Γ|."""
    print("\n" + "=" * 60)
    print("Bonus: VSWR and Return Loss vs |Γ|")
    print("=" * 60)

    Gamma_mag = np.linspace(0.001, 0.999, 500)
    VSWR = (1 + Gamma_mag) / (1 - Gamma_mag)
    RL = -20 * np.log10(Gamma_mag)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

    ax1.plot(Gamma_mag, VSWR, 'b-', linewidth=2)
    ax1.set_xlabel('$|\\Gamma|$')
    ax1.set_ylabel('VSWR')
    ax1.set_title('VSWR vs $|\\Gamma|$')
    ax1.grid(True, alpha=0.3)

    ax2.semilogy(RL, VSWR, 'b-', linewidth=2)
    ax2.set_xlabel('Return Loss (dB)')
    ax2.set_ylabel('VSWR')
    ax2.set_title('VSWR vs Return Loss')
    ax2.grid(True, alpha=0.3)

    # Add common points
    common_points = [
        (0.1, 'RL=20dB, VSWR=1.22'),
        (0.2, 'RL=14dB, VSWR=1.5'),
        (0.33, 'RL=9.6dB, VSWR=2.0'),
        (0.5, 'RL=6dB, VSWR=3.0'),
    ]
    for gm, label in common_points:
        vswr_val = (1+gm)/(1-gm)
        rl_val = -20*np.log10(gm)
        ax1.plot(gm, vswr_val, 'ro', markersize=4)
        ax1.annotate(label, xy=(gm, vswr_val), fontsize=8,
                     xytext=(gm+0.05, vswr_val*0.9))
        ax2.plot(rl_val, vswr_val, 'ro', markersize=4)

    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch2_VSWR_RL.png', dpi=150)
    print(f"  → Saved figure to {FIGS_DIR}/ch2_VSWR_RL.png")
    plt.close(fig)


# ======================================================================
# Main
# ======================================================================
if __name__ == '__main__':
    import os
    os.makedirs(FIGS_DIR, exist_ok=True)

    params = example_2_3()
    ms_design = example_2_5()
    Z0_tl, vp_tl = examples_2_6_7()
    qw_result = example_2_8()
    power = example_2_10()
    bonus_vswr_rl()

    print("\n" + "=" * 60)
    print("✅ Ch2 all examples complete.")
    print("=" * 60)
