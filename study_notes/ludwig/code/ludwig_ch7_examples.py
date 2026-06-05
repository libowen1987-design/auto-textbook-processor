#!/usr/bin/env python3
"""ludwig_ch7_examples.py — Chapter 7: Active Component Modeling (hybrid-π, Miller, fT)"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({'font.family': 'serif', 'font.size': 11, 'figure.dpi': 120})
FIGS_DIR = '/home/ubuntu/.openclaw/workspace/textbooks/ludwig/figures'


def example_7_6():
    """Hybrid-π parameter extraction and Miller effect."""
    print("=" * 60)
    print("Example 7-6: Hybrid-π parameter extraction")
    print("=" * 60)

    # BJT parameters
    IC = 10e-3  # 10 mA
    beta = 150
    VA = 100  # Early voltage
    VBE = 0.7  # V

    VT = 0.0259  # V at 300K
    gm = IC / VT
    r_pi = beta / gm
    ro = VA / IC

    C_pi = 5e-12  # 5 pF
    C_mu = 0.5e-12  # 0.5 pF
    r_b = 10  # base resistance

    # Miller effect with load RL
    RL = 500
    Av = -gm * (ro * RL / (ro + RL))
    C_miller = C_mu * (1 + abs(Av))

    # fT (unity current gain frequency)
    fT = gm / (2 * np.pi * (C_pi + C_mu))

    print(f"\n  IC = {IC*1e3:.1f} mA, β = {beta}")
    print(f"  gm = IC/VT = {gm*1e3:.1f} mS")
    print(f"  rπ = β/gm = {r_pi:.0f} Ω")
    print(f"  ro = VA/IC = {ro:.0f} Ω")
    print(f"\n  Miller effect (RL={RL} Ω):")
    print(f"    Av = {-abs(Av):.1f}")
    print(f"    C_miller = Cμ×(1+|Av|) = {C_miller*1e12:.2f} pF (from {C_mu*1e12:.1f} pF)")
    print(f"\n  fT = gm/(2π(Cπ+Cμ)) = {fT/1e9:.2f} GHz")

    # Frequency response
    f = np.logspace(6, 11, 500)
    w = 2 * np.pi * f

    # Current gain h21
    h21 = gm * r_pi / (1 + 1j * w * r_pi * (C_pi + C_mu))
    # Transducer gain GT with simple load
    Zin = 1.0 / (1.0/r_pi + 1j*w*(C_pi + C_mu)) + r_b
    ZL = 500
    GT = (abs(gm * ZL / (1 + 1j*w*ZL*C_mu))**2) * 4 * 50 * Zin.real / abs(Zin + 50)**2

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))
    ax1.semilogx(f/1e9, 20*np.log10(abs(h21)), 'b-', linewidth=2)
    ax1.axhline(0, color='gray', linestyle=':', alpha=0.3)
    ax1.axvline(fT/1e9, color='r', linestyle='--', label=f'$f_T$ = {fT/1e9:.2f} GHz')
    ax1.set_xlabel('Frequency (GHz)')
    ax1.set_ylabel('$|h_{21}|$ (dB)')
    ax1.set_title('BJT Current Gain $h_{21}$')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    G_T = abs(gm * ZL / (1 + 1j*w*ZL*C_mu))
    ax2.semilogx(f/1e9, 20*np.log10(G_T/G_T.max()), 'b-', linewidth=2)
    ax2.set_xlabel('Frequency (GHz)')
    ax2.set_ylabel('Normalized Gain (dB)')
    ax2.set_title('Hybrid-π Frequency Response')
    ax2.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch7_hybrid_pi_response.png', dpi=150)
    print(f"  → Saved figure")
    plt.close(fig)


if __name__ == '__main__':
    import os; os.makedirs(FIGS_DIR, exist_ok=True)
    example_7_6()
    print("\n✅ Ch7 examples complete.")
