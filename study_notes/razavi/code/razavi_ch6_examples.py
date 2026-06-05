#!/usr/bin/env python3
"""
Razavi RF Microelectronics, 2nd Ed. — Ch6: Mixers
Examples: Conversion gain, Gilbert cell design.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ──────────────────────────────────────────────────────
# Ex 6.1: Single-balanced mixer conversion gain
# ──────────────────────────────────────────────────────
def example_single_balanced_cg():
    """CG = (2/π) * gm * RD for single-balanced active mixer."""
    gm_values = np.linspace(1e-3, 100e-3, 100)  # 1 to 100 mS
    RD = 200.0  # Ohms

    CG_linear = (2/np.pi) * gm_values * RD
    CG_db = 20 * np.log10(CG_linear)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(gm_values*1e3, CG_db, 'b-', linewidth=2)
    ax.axhline(0, color='r', linestyle='--', alpha=0.5)
    ax.set_xlabel('$g_{m1}$ (mS)')
    ax.set_ylabel('Conversion Gain (dB)')
    ax.set_title('Single-Balanced Mixer Conversion Gain ($R_D=200\\Omega$)')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/razavi/figures/ch6_mixer_cg.png', dpi=150)
    plt.close(fig)

    print(f"Ex 6.1: gm=20mS, RD=200Ω → CG = {20*np.log10((2/np.pi)*0.02*200):.1f} dB")
    print("Saved: ch6_mixer_cg.png")
    print()

# ──────────────────────────────────────────────────────
# Ex 6.4: Gilbert cell design at 2.4 GHz
# ──────────────────────────────────────────────────────
def example_gilbert_cell():
    """
    Gilbert cell: CG = (2/π) * gm1 * RD
    Noise: NF ≈ 15-18 dB typical
    """
    ISS = 4e-3  # tail current
    RD = 200.0  # load resistor
    V_ov = 0.3  # overdrive
    gm1 = 2 * ISS / V_ov  # total gm of diff pair

    CG_linear = (2/np.pi) * gm1 * RD
    CG_db = 20 * np.log10(CG_linear)

    print("Ex 6.4: Gilbert Cell at 2.4 GHz")
    print(f"  I_SS = {ISS*1e3:.0f} mA, V_ov = {V_ov:.1f} V")
    print(f"  g_m1 = {gm1*1e3:.0f} mS")
    print(f"  R_D = {RD} Ω")
    print(f"  Conversion Gain = {CG_db:.1f} dB")

    # Noise estimate
    gamma = 2.0/3.0
    k = 1.38e-23
    T = 300
    # RF transconductor noise: 4kTγ*gm * (2/π)^2 * RD^2
    vn2_rf = 4*k*T*gamma*gm1 * (2/np.pi)**2 * RD**2
    # Load noise: 2 * 4kT/RD * RD^2 = 8kT*RD
    vn2_load = 8*k*T*RD
    # Total
    vn2_total = vn2_rf + vn2_load
    # Signal gain
    vn2_output_from_source = (CG_linear**2) * 4*k*T*50
    NF_linear = 1 + vn2_total / vn2_output_from_source
    NF_db = 10 * np.log10(NF_linear)
    print(f"  Estimated NF (DSB): {NF_db:.1f} dB")
    print(f"  Estimated NF (SSB): {NF_db+3:.1f} dB (for heterodyne)")
    print()

# ──────────────────────────────────────────────────────
# Passive mixer conversion loss
# ──────────────────────────────────────────────────────
def example_passive_mixer():
    """Passive mixer CG vs switch resistance."""
    R_sw_values = np.linspace(5, 100, 50)  # ohms
    # CG ≈ 2/π * RL/(RL + R_sw)
    RL = 300.0
    CG = (2/np.pi) * RL / (RL + R_sw_values)
    CG_db = 20 * np.log10(CG)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(R_sw_values, CG_db, 'b-', linewidth=2)
    ax.set_xlabel('Switch On-Resistance ($\\Omega$)')
    ax.set_ylabel('Conversion Gain (dB)')
    ax.set_title('Passive Mixer CG vs Switch Resistance ($R_L=300\\Omega$)')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/razavi/figures/ch6_passive_mixer.png', dpi=150)
    plt.close(fig)

    print(f"Ex 6.7: R_sw=10Ω → CG = {20*np.log10((2/np.pi)*300/310):.1f} dB")
    print(f"        R_sw=50Ω → CG = {20*np.log10((2/np.pi)*300/350):.1f} dB")
    print("Saved: ch6_passive_mixer.png")
    print()

# ──────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────
if __name__ == "__main__":
    print("="*60)
    print("Razavi Ch6 — Mixers: Example Codes")
    print("="*60)
    print()

    example_single_balanced_cg()
    example_gilbert_cell()
    example_passive_mixer()

    print("="*60)
    print("All Ch6 examples completed successfully.")
    print("="*60)
