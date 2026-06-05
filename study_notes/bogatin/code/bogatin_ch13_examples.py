#!/usr/bin/env python3
"""
bogatin_ch13_examples.py — Chapter 13: PDN (Power Distribution Network)

Concepts: target impedance, decap impedance, ESL effect, SRF, parallel decaps
"""

import numpy as np
import matplotlib.pyplot as plt
import os

FIGURE_DIR = "/home/ubuntu/.openclaw/workspace/textbooks/bogatin/figures"
os.makedirs(FIGURE_DIR, exist_ok=True)
plt.rcParams['figure.dpi'] = 150

def decoupling_capacitor_impedance():
    """Plot Z vs. f for real capacitors showing SRF and ESL dominance."""
    f = np.logspace(4, 9, 500)  # 10 kHz to 1 GHz
    omega = 2 * np.pi * f

    # Three capacitor values with same ESL
    caps = [
        ('10 nF, ESL=0.5 nH, ESR=0.05', 10e-9, 0.5e-9, 0.05),
        ('100 nF, ESL=0.5 nH, ESR=0.05', 100e-9, 0.5e-9, 0.05),
        ('1 uF, ESL=0.5 nH, ESR=0.05', 1e-6, 0.5e-9, 0.05),
    ]

    fig, ax = plt.subplots(figsize=(9, 5.5))
    for label, C, ESL, ESR in caps:
        Z = np.sqrt(ESR**2 + (omega * ESL - 1.0 / (omega * C))**2)
        ax.loglog(f, Z, linewidth=2, label=label)
        f_srf = 1.0 / (2 * np.pi * np.sqrt(ESL * C))
        ax.scatter([f_srf], [ESR], s=40, zorder=5)

    # Show ideal C and ideal L asymptotes
    C_ref = 100e-9
    Z_C_ideal = 1.0 / (omega * C_ref)
    ax.loglog(f, Z_C_ideal, 'k:', linewidth=1, alpha=0.4, label='Ideal C (100 nF)')
    ESL_ref = 0.5e-9
    Z_L_ideal = omega * ESL_ref
    ax.loglog(f, Z_L_ideal, 'k:', linewidth=1, alpha=0.4, label='Ideal L (0.5 nH)')

    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Impedance $|Z|$ ($\Omega$)')
    ax.set_title('Fig 13-xx: Real Decoupling Capacitor Impedance')
    ax.grid(True, which='both', alpha=0.3)
    ax.legend(fontsize=8)
    ax.set_xlim(1e4, 1e9)
    ax.set_ylim(0.001, 1000)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch13_decap_impedance.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch13_decap_impedance.png"))
    plt.close(fig)
    print("[Ch13] Decoupling capacitor impedance plot saved.")

    for label, C, ESL, ESR in caps:
        f_srf = 1.0 / (2 * np.pi * np.sqrt(ESL * C))
        Z_srf = ESR
        Z_1GHz = 2 * np.pi * 1e9 * ESL
        print(f"  {label}: SRF={f_srf/1e6:.1f} MHz, Z_min={Z_srf:.3f} Ohm, Z_1GHz={Z_1GHz:.3f} Ohm")

def pdn_impedance_profile():
    """Simple PDN impedance profile showing VRM + decaps + planes."""
    f = np.logspace(2, 9, 500)
    omega = 2 * np.pi * f

    # VRM: good at low freq, inductive at high freq
    Z_VRM = 0.001 + omega * 10e-9  # 10 nH series inductance from VRM

    # Bulk caps: 10x 100 uF with 10 nH ESL each (in parallel)
    C_bulk = 10 * 100e-6
    ESL_bulk = 10e-9 / 10
    ESR_bulk = 0.1 / 10
    Z_bulk = np.sqrt(ESR_bulk**2 + (omega * ESL_bulk - 1/(omega * C_bulk))**2)

    # MLCC decaps: 20x 100 nF with 0.5 nH ESL each
    C_mlcc = 20 * 100e-9
    ESL_mlcc = 0.5e-9 / 20
    ESR_mlcc = 0.05 / 20
    Z_mlcc = np.sqrt(ESR_mlcc**2 + (omega * ESL_mlcc - 1/(omega * C_mlcc))**2)

    # On-chip: 10 nF with 0.01 nH ESL
    C_chip = 10e-9
    ESL_chip = 0.01e-9
    ESR_chip = 0.001
    Z_chip = np.sqrt(ESR_chip**2 + (omega * ESL_chip - 1/(omega * C_chip))**2)

    # Combined: parallel combination
    Z_total = 1.0 / (1/Z_VRM + 1/Z_bulk + 1/Z_mlcc + 1/Z_chip)

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.loglog(f, Z_VRM, '--', alpha=0.5, label='VRM')
    ax.loglog(f, Z_bulk, '--', alpha=0.5, label='Bulk caps (10x 100uF)')
    ax.loglog(f, Z_mlcc, '--', alpha=0.5, label='MLCC decaps (20x 100nF)')
    ax.loglog(f, Z_chip, '--', alpha=0.5, label='On-chip cap')
    ax.loglog(f, Z_total, 'k-', linewidth=2.5, label='Total PDN impedance')
    ax.axhline(y=0.01, color='red', linestyle=':', alpha=0.5, label='Target Z = 0.01 Ohm')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Impedance $|Z|$ ($\Omega$)')
    ax.set_title('PDN Impedance Profile (VRM → Bulk → MLCC → Chip)')
    ax.grid(True, which='both', alpha=0.3)
    ax.legend(fontsize=8)
    ax.set_xlim(1e2, 1e9)
    ax.set_ylim(0.0001, 10)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch13_pdn_impedance.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch13_pdn_impedance.png"))
    plt.close(fig)
    print("[Ch13] PDN impedance profile plot saved.")

    Z_max = np.max(Z_total[f < 1e9])
    print(f"  Maximum PDN impedance (DC-1 GHz): {Z_max:.4f} Ohm")

if __name__ == "__main__":
    print("="*60)
    print("Chapter 13: PDN")
    print("="*60)
    decoupling_capacitor_impedance()
    pdn_impedance_profile()
    print("\nAll Ch13 examples complete.")
