#!/usr/bin/env python3
"""
梁昌洪《简明微波》第一章 - 微波波段频率对照与衰减计算
Chapter 1: Microwave Bands, Frequency-Wavelength Conversion, and Attenuation
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.unicode_minus': False,
})
# ---- Microwave Band Definitions ----
# (Band name, frequency_GHz_range, wavelength_cm_range)
BANDS = [
    ("L",    1.0,   2.0,   30.0,  15.0),
    ("S",    2.0,   4.0,   15.0,  7.5),
    ("C",    4.0,   8.0,   7.5,   3.75),
    ("X",    8.0,   12.0,  3.75,  2.5),
    ("Ku",   12.0,  18.0,  2.5,   1.67),
    ("K",    18.0,  26.5,  1.67,  1.13),
    ("Ka",   26.5,  40.0,  1.13,  0.75),
    ("U",    40.0,  60.0,  0.75,  0.5),
    ("V",    60.0,  80.0,  0.5,   0.375),
    ("W",    80.0,  100.0, 0.375, 0.3),
    ("mm",   100.0, 300.0, 0.3,   0.1),
    ("THz",  300.0, 3000.0, 0.1,  0.01),
]

def freq_to_wavelength(f_GHz):
    """Convert frequency (GHz) to wavelength (cm)."""
    c_cm = constants.c * 100  # cm/s
    return c_cm / (f_GHz * 1e9)

def wavelength_to_freq(lambda_cm):
    """Convert wavelength (cm) to frequency (GHz)."""
    c_cm = constants.c * 100
    return c_cm / (lambda_cm * 1e-2) / 1e9

def attenuation_dB_per_100m(f_GHz, conductivity=5.8e7, mu_r=1.0):
    """
    Estimate conductor attenuation for a parallel-wire transmission line.
    Alpha = (R/2*Z0)**0.5  [Neper/m]
    R ~ sqrt(pi*f*mu/mu_r*sigma) * (1/a + 1/b) for two parallel cylinders.
    Returns dB/100m approximation for a standard coaxial approximation.
    """
    skin_depth = np.sqrt(2.0 / (2*np.pi * f_GHz * 1e9 * mu_r * 4*np.pi*1e-7 * conductivity))
    # Simplified conductor loss for a representative copper line (dB/100m)
    alpha_cu = 2.3e-6 * (f_GHz**0.5) * 1e4  # dB/m, empirical scaling
    return alpha_cu * 100  # dB/100m

def main():
    # ---- 1. Print microwave band table ----
    print("=" * 72)
    print("  梁昌洪《简明微波》第一章 - 微波波段频率对照表")
    print("=" * 72)
    print(f"  {'Band':<6} {'f_min(GHz)':<13} {'f_max(GHz)':<13} {'λ_min(cm)':<12} {'λ_max(cm)':<12}")
    print("-" * 72)
    for row in BANDS:
        band, f1, f2, l2, l1 = row
        print(f"  {band:<6} {f1:<13.2f} {f2:<13.2f} {l1:<12.3f} {l2:<12.3f}")
    print("-" * 72)
    c = constants.c * 100  # cm/s
    print(f"\n  光速 c = {c:.4e} cm/s")

    # ---- 2. Frequency-wavelength converter ----
    print("\n  频率-波长对照 (示例频率点):")
    print(f"  {'f(GHz)':<12} {'λ(cm)':<12} {'λ(mm)':<12}")
    print("-" * 40)
    for f in [0.3, 1, 3, 10, 30, 94, 140, 300, 700, 2000]:
        lam = freq_to_wavelength(f)
        print(f"  {f:<12.2f} {lam:<12.4f} {lam*10:<12.4f}")

    # ---- 3. Attenuation plot ----
    freqs = np.linspace(0.3, 300, 500)
    atten = np.array([attenuation_dB_per_100m(f) for f in freqs])

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Left: wavelength vs frequency
    ax = axes[0]
    f_plot = np.logspace(np.log10(0.3), np.log10(300), 400)
    lam_plot = freq_to_wavelength(f_plot)
    ax.loglog(f_plot, lam_plot, 'b-', linewidth=2)
    ax.set_xlim(0.3, 300)
    ax.set_ylim(0.01, 100)
    ax.set_xlabel(r'$f$ (GHz)', fontsize=12)
    ax.set_ylabel(r'$\lambda$ (cm)', fontsize=12)
    ax.set_title('Microwave Frequency vs Wavelength', fontsize=13)
    ax.grid(True, which='both', alpha=0.4)
    # Band annotations
    band_colors = {'L':'C0','S':'C1','C':'C2','X':'C3','Ku':'C4','K':'C5','Ka':'C6','U':'C7','V':'C8','W':'C9','mm':'gold','THz':'red'}
    for band, f1, f2, l2, l1 in BANDS:
        ax.axvspan(f1, f2, alpha=0.08, color=band_colors.get(band,'gray'), label=band)
    ax.legend(loc='upper right', fontsize=8, ncol=2)

    # Right: attenuation vs frequency
    ax2 = axes[1]
    ax2.semilogx(freqs, atten, 'r-', linewidth=2)
    ax2.set_xlabel(r'$f$ (GHz)', fontsize=12)
    ax2.set_ylabel(r'Attenuation (dB/100m)', fontsize=12)
    ax2.set_title('Estimated Conductor Attenuation vs Frequency', fontsize=13)
    ax2.grid(True, which='both', alpha=0.4)
    ax2.set_xlim(0.3, 300)

    fig.suptitle(r'梁昌洪《简明微波》第一章 — 微波波段与频率-波长关系', fontsize=14, y=1.02)
    plt.tight_layout()
    out = '/home/ubuntu/.openclaw/workspace/textbooks/liangchanghong/code/ch1_microwave_bands.png'
    fig.savefig(out, dpi=150, bbox_inches='tight')
    print(f"\n  [saved] {out}")
    plt.close()

if __name__ == '__main__':
    main()
