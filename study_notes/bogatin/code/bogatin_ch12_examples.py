#!/usr/bin/env python3
"""
bogatin_ch12_examples.py — Chapter 12: S-Parameters

Concepts: S11, S21, insertion loss, return loss, mixed-mode S-params
"""

import numpy as np
import matplotlib.pyplot as plt
import os

FIGURE_DIR = "/home/ubuntu/.openclaw/workspace/textbooks/bogatin/figures"
os.makedirs(FIGURE_DIR, exist_ok=True)
plt.rcParams['figure.dpi'] = 150

def sparameter_demo():
    """Plot S11 and S21 for a simple interconnect model."""
    f = np.linspace(0.01, 20, 1000)  # GHz

    # Model a 4-inch FR4 microstrip: Z0=50, some loss
    # S21: insertion loss increases with frequency
    alpha_cond = 0.1 * np.sqrt(f)  # dB/inch, skin effect
    alpha_diel = 0.05 * f  # dB/inch, dielectric loss
    length = 4  # inches
    IL_db = (alpha_cond + alpha_diel) * length
    S21_mag = 10**(-IL_db / 20)

    # S11: return loss, assume decent match
    S11_mag = 0.1 * np.ones_like(f)  # -20 dB return loss
    S11_mag[:10] = 0.01  # very good at low freq
    RL_db = -20 * np.log10(S11_mag)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.semilogy(f, S21_mag, 'b-', linewidth=2, label='$|S_{21}|$ (insertion loss)')
    ax1.semilogy(f, S11_mag, 'r-', linewidth=2, label='$|S_{11}|$ (reflection)')
    ax1.axhline(y=10**(-3/20), color='gray', linestyle='--', alpha=0.5, label='-3 dB point')
    ax1.set_xlabel('Frequency (GHz)')
    ax1.set_ylabel('Magnitude')
    ax1.set_title('S-Parameters of 4-inch FR4 Microstrip')
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=9)
    ax1.set_xlim(0, 20)
    ax1.set_ylim(0.001, 1)

    ax2.plot(f, -IL_db, 'b-', linewidth=2, label='Insertion Loss (dB)')
    ax2.plot(f, RL_db, 'r-', linewidth=2, label='Return Loss (dB)')
    ax2.axhline(y=-3, color='gray', linestyle='--', alpha=0.5, label='-3 dB')
    ax2.set_xlabel('Frequency (GHz)')
    ax2.set_ylabel('dB')
    ax2.set_title('S-Parameters in dB')
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=9)
    ax2.set_xlim(0, 20)
    ax2.set_ylim(-40, 0)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch12_sparameters.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch12_sparameters.png"))
    plt.close(fig)
    print("[Ch12] S-parameter plots saved.")

    # Find -3 dB bandwidth
    idx_3db = np.argmin(np.abs(S21_mag - 10**(-3/20)))
    print(f"  -3 dB bandwidth: ~{f[idx_3db]:.2f} GHz")
    print(f"  |S21| at 1 GHz: {np.interp(1, f, S21_mag):.3f} ({20*np.log10(np.interp(1, f, S21_mag)):.1f} dB)")
    print(f"  |S21| at 10 GHz: {np.interp(10, f, S21_mag):.3f} ({20*np.log10(np.interp(10, f, S21_mag)):.1f} dB)")
    print(f"  Return Loss: {np.interp(1, f, RL_db):.1f} dB")

if __name__ == "__main__":
    print("="*60)
    print("Chapter 12: S-Parameters")
    print("="*60)
    sparameter_demo()
    print("\nAll Ch12 examples complete.")
