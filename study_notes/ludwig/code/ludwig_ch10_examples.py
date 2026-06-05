#!/usr/bin/env python3
"""ludwig_ch10_examples.py — Chapter 10: Oscillators and Mixers"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({'font.family': 'serif', 'font.size': 11, 'figure.dpi': 120})
FIGS_DIR = '/home/ubuntu/.openclaw/workspace/textbooks/ludwig/figures'


def example_10_1():
    """Colpitts oscillator design."""
    print("=" * 60)
    print("Example 10-1: Colpitts oscillator design")
    print("=" * 60)

    f0 = 1e9  # 1 GHz
    L = 2e-9  # 2 nH

    C_eq = 1 / ((2 * np.pi * f0)**2 * L)
    # Colpitts: C1 and C2 in series = C_eq, with C1 < C_eq < C2 typical
    C1 = 20e-12  # 20 pF
    C2 = 1 / (1/C_eq - 1/C1)

    print(f"\n  f0 = {f0/1e9:.1f} GHz")
    print(f"  L  = {L*1e9:.2f} nH")
    print(f"\n  C_eq = 1/(ω²L) = {C_eq*1e12:.2f} pF")
    print(f"  With C1 = {C1*1e12:.1f} pF:")
    C2_computed = 1 / (1/C_eq - 1/C1)
    print(f"    C2 = 1/(1/Ceq - 1/C1) = {C2_computed*1e12:.2f} pF")

    # Loop gain condition
    print(f"\n  Colpitts topology: C1-C2-L resonator with transistor")

    # Oscillation frequency vs C
    C1_range = np.linspace(2e-12, 30e-12, 300)
    C2_val = C2_computed
    f_osc = 1 / (2 * np.pi * np.sqrt(L * (C1_range * C2_computed / (C1_range + C2_computed))))

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(C1_range*1e12, f_osc/1e9, 'b-', linewidth=2)
    ax.axhline(f0/1e9, color='r', linestyle='--', alpha=0.5, label=f'$f_0={f0/1e9:.1f}$ GHz')
    ax.set_xlabel('$C_1$ (pF)')
    ax.set_ylabel('Oscillation Frequency (GHz)')
    ax.set_title('Colpitts Oscillator: $f_{osc}$ vs $C_1$')
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch10_colpitts_tuning.png', dpi=150)
    print(f"  → Saved figure")
    plt.close(fig)


def example_10_5():
    """GaAs FET oscillator with negative resistance."""
    print("\n" + "=" * 60)
    print("Example 10-5: GaAs FET negative resistance oscillator")
    print("=" * 60)

    # S-parameters at instability (source-degenerated FET)
    S = np.array([[1.5+0.3j, 0.05+0.01j],
                  [2.0-1.0j, 0.4-0.2j]])

    S11, S12, S21, S22 = S.flatten()
    Delta = S11*S22 - S12*S21

    K = (1 - abs(S11)**2 - abs(S22)**2 + abs(Delta)**2) / (2*abs(S12*S21))

    print(f"\n  S-parameters at oscillator bias:")
    print(f"    S11 = {S[0,0]:.3f}, S12 = {S[0,1]:.3f}")
    print(f"    S21 = {S[1,0]:.3f}, S22 = {S[1,1]:.3f}")
    print(f"\n  K = {K:.3f} {'< 1 → potentially oscillatory' if K < 1 else '> 1 → stable'}")

    # Output reflection coefficient with load
    Gamma_L = 0.5 + 0.3j  # example load
    Gamma_out = S22 + (S12 * S21 * Gamma_L) / (1 - S11 * Gamma_L)

    print(f"\n  With Γ_L = {Gamma_L:.3f}:")
    print(f"  Γ_out = {Gamma_out:.4f}")
    print(f"  |Γ_out| = {abs(Gamma_out):.4f}")
    print(f"\n  Oscillation condition: |Γ_out·Γ_L| > 1")
    osc_condition = abs(Gamma_out) * abs(Gamma_L)
    print(f"  |Γ_out·Γ_L| = {osc_condition:.4f} {'✅' if osc_condition > 1 else '❌'}")

    # Design load for oscillation
    print(f"\n  For oscillation, choose Γ_L such that |Γ_out·Γ_L| > 1")
    print(f"  Typical load: series resonant circuit (R + jX)")


if __name__ == '__main__':
    import os; os.makedirs(FIGS_DIR, exist_ok=True)
    example_10_1()
    example_10_5()
    print("\n✅ Ch10 examples complete.")
