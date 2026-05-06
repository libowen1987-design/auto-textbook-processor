#!/usr/bin/env python3
"""
Razavi RF Microelectronics, 2nd Ed. — Ch5: Low-Noise Amplifiers
Examples: CS inductively-degenerated LNA design, NF calculation.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import constants

# ──────────────────────────────────────────────────────
# Ex 5.7: LNA NF from ωT
# ──────────────────────────────────────────────────────
def example_lna_nf_from_omegaT():
    """NF ≈ 1 + (γ/α)·(ω₀/ω_T) for inductively-degenerated CS LNA."""
    gamma = 2.0/3.0  # long-channel
    alpha = 1.0

    f0 = 5e9
    fT_values = np.linspace(20e9, 200e9, 100)

    NF_linear = 1 + (gamma/alpha) * f0 / fT_values
    NF_db = 10 * np.log10(NF_linear)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(fT_values/1e9, NF_db, 'b-', linewidth=2)
    ax.axhline(3, color='r', linestyle='--', alpha=0.5, label='3 dB floor')
    ax.set_xlabel('$f_T$ (GHz)')
    ax.set_ylabel('NF (dB)')
    ax.set_title('LNA NF vs $f_T$ ($f_0 = 5$ GHz, inductively-degenerated CS)')
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/razavi/figures/ch5_lna_nf_vs_ft.png', dpi=150)
    plt.close(fig)

    print(f"Ex 5.7: At fT=80 GHz, NF = {10*np.log10(1+(gamma/alpha)*5/80):.2f} dB")
    print(f"        At fT=150 GHz, NF = {10*np.log10(1+(gamma/alpha)*5/150):.2f} dB")
    print("Saved: ch5_lna_nf_vs_ft.png")
    print()

# ──────────────────────────────────────────────────────
# Ex 5.8: Inductively-degenerated CS LNA Design
# ──────────────────────────────────────────────────────
def example_cs_lna_design():
    """
    Design a 5 GHz inductively-degenerated CS LNA.
    Given: f0 = 5 GHz, VDD = 1.8V, ID = 5 mA,
    Technology: C_ox = 8 fF/μm², μnCox = 200 μA/V², L_min = 0.18 μm
    """
    f0 = 5e9
    omega0 = 2 * np.pi * f0
    RS = 50.0
    VDD = 1.8
    I_D = 5e-3
    L_min = 0.18e-6
    mu_n_Cox = 200e-6  # A/V²
    C_ox = 8e-3  # F/m² (8 fF/μm² → 8e-15 F/μm² × 1e12 μm²/m² = 8e-3 F/m²)

    # Step 1: Choose V_GS - V_TH ≈ 0.3V (reasonable)
    V_ov = 0.3
    gm = 2 * I_D / V_ov
    gm_target = 1/RS  # 20 mS for matching... but we'll design properly

    print(f"Ex 5.8: 5 GHz Inductively-Degenerated CS LNA Design")
    print(f"  V_ov = {V_ov:.2f} V, I_D = {I_D*1e3:.1f} mA")
    print(f"  g_m = {gm*1e3:.1f} mS")

    # Device width for given gm
    # gm = mu_n_Cox * (W/L) * V_ov
    W = gm * L_min / (mu_n_Cox * V_ov)
    # C_GS = (2/3) * W * L * C_ox
    C_GS = (2.0/3.0) * W * L_min * C_ox
    omega_T = gm / C_GS

    print(f"  W = {W*1e6:.0f} μm")
    print(f"  C_GS = {C_GS*1e15:.1f} fF")
    print(f"  ω_T = {omega_T/(2*np.pi)/1e9:.1f} GHz")

    # Source degeneration inductor
    # Re{Zin} = ω_T * L_S = RS
    L_S = RS / omega_T
    # Gate inductor for resonance: ω₀² = 1/((L_S + L_G) * C_GS)
    L_G = 1/(omega0**2 * C_GS) - L_S

    print(f"  L_S = {L_S*1e9:.2f} nH")
    print(f"  L_G = {L_G*1e9:.2f} nH")
    print(f"  Resonance check: 1/√((L_S+L_G)·C_GS) = {1/(2*np.pi*np.sqrt((L_S+L_G)*C_GS))/1e9:.1f} GHz")

    # NF estimate
    gamma = 2.0/3.0
    NF_linear = 1 + gamma * omega0 / omega_T
    NF_db = 10 * np.log10(NF_linear)
    print(f"  Estimated NF: {NF_db:.2f} dB (idealized, no CG noise)")

    # S11 calculation
    f_range = np.linspace(4e9, 6e9, 200)
    omega = 2 * np.pi * f_range
    Z_in = (gm*L_S/C_GS) + 1j*(omega*(L_S+L_G) - 1/(omega*C_GS))
    Gamma_in = (Z_in - RS) / (Z_in + RS)
    S11_db = 20 * np.log10(np.abs(Gamma_in))

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(f_range/1e9, S11_db, 'b-', linewidth=2)
    ax.axhline(-10, color='r', linestyle='--', alpha=0.5, label='-10 dB')
    ax.set_xlabel('Frequency (GHz)')
    ax.set_ylabel('$S_{11}$ (dB)')
    ax.set_title('Input Return Loss of Inductively-Degenerated CS LNA')
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/razavi/figures/ch5_s11_lna.png', dpi=150)
    plt.close(fig)
    print("Saved: ch5_s11_lna.png")
    print()

# ──────────────────────────────────────────────────────
# CG LNA NF comparison
# ──────────────────────────────────────────────────────
def example_cg_lna():
    """NF of CG LNA: NF = 1 + γ + RS/RD (for matching gm = 1/RS)."""
    RS = 50.0
    gamma = 2.0/3.0
    # For matching: gm = 1/RS = 20 mS
    gm = 1/RS

    # Add load resistor noise
    RD_values = np.array([50, 100, 200, 500])
    Av_values = gm * RD_values
    NF_values = 1 + gamma + RS/RD_values
    NF_db = 10 * np.log10(NF_values)

    print(f"Ex 5.16: CG LNA NF (gm = {gm*1e3:.0f} mS)")
    for i, (RD, Av, NF) in enumerate(zip(RD_values, Av_values, NF_values)):
        print(f"  R_D = {RD} Ω, A_v = {Av:.1f}, NF = {10*np.log10(NF):.2f} dB")

    # Compare CS vs CG LNA NF
    f0 = 5e9
    fT_values = np.linspace(30e9, 200e9, 100)
    NF_cs = 10*np.log10(1 + gamma * f0 / fT_values)
    NF_cg = 10*np.log10(1 + gamma + RS/RD_values[2])  # RD = 200

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(fT_values/1e9, NF_cs, 'b-', linewidth=2, label='CS (ind. deg.)')
    ax.axhline(NF_cg, color='r', linestyle='--', linewidth=2, label=f'CG (NF={NF_cg:.1f} dB)')
    ax.set_xlabel('$f_T$ (GHz)')
    ax.set_ylabel('NF (dB)')
    ax.set_title('CS vs CG LNA NF Comparison at $f_0 = 5$ GHz')
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/razavi/figures/ch5_cs_vs_cg_lna.png', dpi=150)
    plt.close(fig)
    print("Saved: ch5_cs_vs_cg_lna.png")
    print()

# ──────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────
if __name__ == "__main__":
    print("="*60)
    print("Razavi Ch5 — Low-Noise Amplifiers: Example Codes")
    print("="*60)
    print()

    example_lna_nf_from_omegaT()
    example_cs_lna_design()
    example_cg_lna()

    print("="*60)
    print("All Ch5 examples completed successfully.")
    print("="*60)
