#!/usr/bin/env python3
"""
bogatin_ch10_examples.py — Chapter 10: Cross Talk

Concepts: NEXT and FEXT coupling, saturation length, spacing effect
"""

import numpy as np
import matplotlib.pyplot as plt
import os

FIGURE_DIR = "/home/ubuntu/.openclaw/workspace/textbooks/bogatin/figures"
os.makedirs(FIGURE_DIR, exist_ok=True)
plt.rcParams['figure.dpi'] = 150

def next_fext_saturation():
    # NEXT grows linearly with len until saturation
    RT = 0.5  # nsec
    v = 6.0  # in/nsec (FR4)
    L_sat = RT * v / 2  # saturation length = 1.5 inches

    coupled_length = np.linspace(0, 10, 200)
    NEXT = np.minimum(coupled_length / L_sat, 1.0) * 0.1  # saturates at 10%
    FEXT = (coupled_length / (RT * v)) * 0.08  # grows linearly, no saturation

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(coupled_length, NEXT * 100, 'b-', linewidth=2, label='NEXT (saturates)')
    ax.plot(coupled_length, FEXT * 100, 'r-', linewidth=2, label='FEXT (linear)')
    ax.axvline(x=L_sat, color='gray', linestyle='--', alpha=0.5,
               label=f'Saturation length = {L_sat:.1f} in')
    ax.set_xlabel('Coupled Length (inches)')
    ax.set_ylabel('Cross Talk Noise (% of signal)')
    ax.set_title('NEXT and FEXT vs. Coupled Length (RT=0.5ns, FR4)')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch10_next_fext.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch10_next_fext.png"))
    plt.close(fig)

    print("[Ch10] NEXT/FEXT vs. length plot saved.")
    print(f"  Saturation length (RT={RT}ns): {L_sat:.1f} inches")
    print(f"  At L={L_sat:.1f}in: NEXT ~ {0.1*100:.0f}%")
    print(f"  At L=6in: FEXT ~ {0.08*6/(RT*v)*100:.1f}%")

if __name__ == "__main__":
    print("="*60)
    print("Chapter 10: Cross Talk")
    print("="*60)
    next_fext_saturation()
    print("\nAll Ch10 examples complete.")
