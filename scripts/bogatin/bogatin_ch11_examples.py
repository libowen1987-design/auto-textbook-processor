#!/usr/bin/env python3
"""
bogatin_ch11_examples.py — Chapter 11: Differential Pairs

Concepts: Zodd, Zeven, Zdiff, effect of coupling
"""

import numpy as np
import matplotlib.pyplot as plt
import os

FIGURE_DIR = "/home/ubuntu/.openclaw/workspace/textbooks/bogatin/figures"
os.makedirs(FIGURE_DIR, exist_ok=True)
plt.rcParams['figure.dpi'] = 150

def differential_impedance():
    """Show Zodd, Zeven, Zdiff vs. coupling coefficient k"""
    Z0 = 50.0  # single-ended Z0
    k = np.linspace(0, 0.6, 100)  # coupling coefficient

    # Simplified: assume kL = kC = k (true for stripline)
    Z_odd = Z0 * np.sqrt((1 - k) / (1 + k))
    Z_even = Z0 * np.sqrt((1 + k) / (1 - k))
    Z_diff = 2 * Z_odd
    Z_comm = Z_even / 2

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.plot(k, Z_diff, 'b-', linewidth=2, label='$Z_{diff} = 2 \\cdot Z_{odd}$')
    ax.plot(k, Z_odd, 'g-', linewidth=2, label='$Z_{odd}$ (one line, odd mode)')
    ax.plot(k, Z_even, 'r-', linewidth=2, label='$Z_{even}$ (one line, even mode)')
    ax.plot(k, Z_comm, 'm-', linewidth=2, label='$Z_{common} = Z_{even} / 2$')
    ax.axhline(y=Z0, color='gray', linestyle=':', alpha=0.4, label=f'$Z_0$ (single ended)={Z0}$\\Omega$')
    ax.set_xlabel('Coupling Coefficient $k$')
    ax.set_ylabel('Impedance ($\Omega$)')
    ax.set_title('Differential Pair Impedances vs. Coupling')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8)
    ax.set_xlim(0, 0.6)
    ax.set_ylim(0, 100)

    # Annotate typical values
    for k_val in [0.1, 0.3, 0.5]:
        zd = 2 * Z0 * np.sqrt((1 - k_val) / (1 + k_val))
        ax.scatter([k_val], [zd], color='red', s=40, zorder=5)
        ax.annotate(f'k={k_val:.1f}\n$Z_{{diff}}$={zd:.0f}$\\Omega$',
                    xy=(k_val, zd), fontsize=8,
                    xytext=(k_val - 0.15, zd + 12),
                    arrowprops=dict(arrowstyle='->', color='red', lw=0.5))

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch11_differential_impedance.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch11_differential_impedance.png"))
    plt.close(fig)
    print("[Ch11] Differential impedance plot saved.")

    for k_val in [0, 0.1, 0.2, 0.5]:
        Zodd = Z0 * np.sqrt((1 - k_val) / (1 + k_val))
        Zeven = Z0 * np.sqrt((1 + k_val) / (1 - k_val))
        print(f"  k={k_val:.1f}: Zodd={Zodd:.1f}, Zeven={Zeven:.1f}, Zdiff={2*Zodd:.1f}")

if __name__ == "__main__":
    print("="*60)
    print("Chapter 11: Differential Pairs")
    print("="*60)
    differential_impedance()
    print("\nAll Ch11 examples complete.")
