#!/usr/bin/env python3
"""ludwig_ch6_examples.py — Chapter 6: Active Components (pn junction, Schottky, PIN)"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as const

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({'font.family': 'serif', 'font.size': 11, 'figure.dpi': 120})
FIGS_DIR = '/home/ubuntu/.openclaw/workspace/textbooks/ludwig/figures'

q = const.e  # 1.602e-19 C
k = const.k  # 1.381e-23 J/K
eps0 = const.epsilon_0


def example_6_3():
    """pn junction capacitance at 300K."""
    print("=" * 60)
    print("Example 6-3: pn junction capacitance")
    print("=" * 60)

    eps_r_Si = 11.7
    NA = 1e17  # cm⁻³
    ND = 1e15  # cm⁻³
    ni = 1.45e10  # cm⁻³

    VT = k * 300 / q
    V0 = VT * np.log(NA * ND / ni**2)

    Cj0 = 50e-12 / 50  # ~1 pF normalized
    V = np.linspace(-10, 0.5, 500)

    m = 0.5  # abrupt junction
    Cj = Cj0 / (1 - V / V0)**m

    print(f"\n  V0 (built-in) = {V0:.3f} V")
    print(f"  Cj0 = {Cj0*1e12:.2f} pF")
    print(f"  Cj @ -5V = {np.interp(-5, V, Cj)*1e12:.2f} pF")
    print(f"  Cj @ 0V  = {np.interp(0, V, Cj)*1e12:.2f} pF")

    fig, ax = plt.subplots()
    ax.plot(V, Cj*1e12, 'b-', linewidth=2)
    ax.axvline(0, color='gray', linestyle=':', alpha=0.3)
    ax.set_xlabel('Bias Voltage V (V)')
    ax.set_ylabel('Junction Capacitance (pF)')
    ax.set_title('pn Junction Capacitance vs Bias')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch6_pn_capacitance.png', dpi=150)
    print(f"  → Saved figure")
    plt.close(fig)


def example_6_7():
    """BJT forward current."""
    print("\n" + "=" * 60)
    print("Example 6-7: BJT I-V characteristics")
    print("=" * 60)

    IS = 1e-15
    beta = 100
    VBE = np.linspace(0.4, 0.8, 200)
    IC = IS * np.exp(VBE / (k * 300 / q))
    IB = IC / beta

    fig, ax = plt.subplots()
    ax.semilogy(VBE, IC*1e3, 'b-', linewidth=2, label='$I_C$')
    ax.semilogy(VBE, IB*1e3, 'r--', linewidth=2, label='$I_B$')
    ax.set_xlabel('$V_{BE}$ (V)')
    ax.set_ylabel('Current (mA)')
    ax.set_title('BJT $I_C$ and $I_B$ vs $V_{BE}$ ($\\beta=100$)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch6_bjt_iv.png', dpi=150)
    print(f"  → Saved figure")
    plt.close(fig)

    print(f"\n  IS = {IS:.0e} A, β = {beta}")
    print(f"  IC @ 0.6V = {np.interp(0.6, VBE, IC)*1e3:.2f} mA")
    print(f"  IC @ 0.7V = {np.interp(0.7, VBE, IC)*1e3:.2f} mA")


if __name__ == '__main__':
    import os; os.makedirs(FIGS_DIR, exist_ok=True)
    example_6_3()
    example_6_7()
    print("\n✅ Ch6 examples complete.")
