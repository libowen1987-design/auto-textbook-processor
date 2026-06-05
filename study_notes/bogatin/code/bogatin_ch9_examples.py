#!/usr/bin/env python3
"""
bogatin_ch9_examples.py — Chapter 9: Lossy Lines

Concepts: skin effect resistance, dielectric loss, ISI, eye diagram
"""

import numpy as np
import matplotlib.pyplot as plt
import os

FIGURE_DIR = "/home/ubuntu/.openclaw/workspace/textbooks/bogatin/figures"
os.makedirs(FIGURE_DIR, exist_ok=True)
plt.rcParams['figure.dpi'] = 150

def skin_effect_resistance():
    f = np.logspace(5, 10, 200)  # 100 kHz to 10 GHz
    f_mhz = f / 1e6
    delta_um = 66 / np.sqrt(f_mhz)

    # Resistance: assume 5-mil wide, 1-oz Cu trace
    rho = 1.72e-8  # Ohm-m
    w = 5 * 25.4e-6  # 5 mil in m
    # DC resistance (per inch)
    R_DC = rho / (w * 35e-6) * 0.0254  # Ohm/inch
    # HF resistance
    R_AC = rho / (w * delta_um * 1e-6) * 0.0254

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.loglog(f, R_DC * np.ones_like(f), 'k--', label='DC resistance (no skin effect)')
    ax.loglog(f, R_AC, 'b-', linewidth=2, label='Skin-effect resistance')
    ax.axvline(x=10e6, color='red', linestyle=':', alpha=0.5, label='~10 MHz: skin limit begins')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Resistance per inch (Ohm/inch)')
    ax.set_title('Skin Effect: Resistance vs. Frequency (5-mil trace, 1oz Cu)')
    ax.grid(True, which='both', alpha=0.3)
    ax.legend(fontsize=9)
    ax.set_xlim(1e5, 1e10)
    ax.set_ylim(0.05, 10)
    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch9_skin_effect_resistance.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch9_skin_effect_resistance.png"))
    plt.close(fig)
    print("[Ch9] Skin effect resistance plot saved.")

    for fm in [1, 10, 100, 1000, 10000]:
        d = 66 / np.sqrt(fm)
        ratio = 35 / d
        print(f"  {fm:6d} MHz: delta={d:5.1f} um, R_AC/R_DC = {ratio:.1f}x")

def dielectric_loss():
    f_ghz = np.linspace(0.1, 10, 100)
    epsilon_r = 4.0
    tans = {'FR4': 0.02, 'Rogers 4350B': 0.0037, 'Megtron 6': 0.002, 'PTFE': 0.0002}

    fig, ax = plt.subplots(figsize=(8, 5))
    for name, td in tans.items():
        alpha = 2.3 * f_ghz * td * np.sqrt(epsilon_r)  # dB/inch approx
        ax.plot(f_ghz, alpha, linewidth=2, label=f'{name} (tanδ={td})')
    ax.set_xlabel('Frequency (GHz)')
    ax.set_ylabel('Dielectric Attenuation (dB/inch)')
    ax.set_title('Dielectric Loss for Common Laminates')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1.0)
    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch9_dielectric_loss.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch9_dielectric_loss.png"))
    plt.close(fig)
    print("[Ch9] Dielectric loss plot saved.")

if __name__ == "__main__":
    print("="*60)
    print("Chapter 9: Lossy Lines")
    print("="*60)
    skin_effect_resistance()
    dielectric_loss()
    print("\nAll Ch9 examples complete.")
