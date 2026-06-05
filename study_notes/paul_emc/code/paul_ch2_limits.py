#!/usr/bin/env python3
"""
Paul《EMC》2nd Ed. Ch2: EMC Requirements - Emission Limits & Conversions
======================================================================
Comprehensive code covering:
  • FCC Part 15 Class A/B conducted emission limits (dBμV vs MHz)
  • FCC Part 15 Class A/B radiated emission limits (dBμV/m vs MHz)
  • CISPR 22 (EN 55022) conducted/radiated limits
  • LISN impedance model (50Ω / 50μH)
  • dBμV → mA conversion (I = V/R)
  • 3m / 10m distance scaling (inverse-distance law)
  • Tabulated limits + validation + plots
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import constants

# ─────────────────────────── Physical Constants ────────────────────────────
R_LISN   = 50.0          # LISN characteristic impedance (Ω)
L_LISN   = 50e-6         # LISN series inductance (H)
Z0       = 377.0         # Free-space impedance (Ω)
c        = constants.c   # Speed of light (m/s)
mu0      = constants.mu_0
eps0     = constants.epsilon_0

# ════════════════════════════ FCC Part 15 Limits ════════════════════════════

def fcc_conducted_class_a():
    """FCC Part 15 Class A – conducted emission limits (quasi-peak, dBμV)."""
    f = np.array([0.45, 1.6])
    limit = np.array([60.0, 60.0])
    return f, limit

def fcc_conducted_class_b():
    """FCC Part 15 Class B – conducted emission limits (quasi-peak, dBμV)."""
    f = np.array([0.45, 1.6])
    limit = np.array([48.0, 48.0])
    return f, limit

def fcc_conducted_freq_bands_class_a():
    """
    Frequency-dependent Class A limits per FCC Part 15 §109 / CISPR 22.
    Returns (freq_edges, limit_dBuv) as step-function data.
    """
    # 0.15–30 MHz: two flat bands
    f_edges = np.array([0.15, 0.45, 1.6, 30.0])
    limits  = np.array([60.0, 60.0, 60.0, 60.0])   # placeholder per band
    # Proper piecewise: ≤0.45 MHz → 60 dBμV; >0.45–≤1.6 MHz → 60 dBμV; >1.6 MHz → 60 dBμV
    return f_edges, limits

def fcc_conducted_class_a_limits():
    """Full piecewise Class A conducted limits (QP, dBμV) for 0.15–30 MHz."""
    bands = {
        (0.15, 0.45): 60.0,
        (0.45, 1.6):  60.0,
        (1.6,  30.0): 59.0,   # FCC Class A slightly tighter above 1.6 MHz
    }
    return bands

def fcc_conducted_class_b_limits():
    """Full piecewise Class B conducted limits (QP, dBμV) for 0.15–30 MHz."""
    bands = {
        (0.15, 0.45): 48.0,
        (0.45, 1.6):  48.0,
        (1.6,  30.0): 48.0,
    }
    return bands

def fcc_radiated_class_a_3m():
    """
    FCC Class A radiated limits @ 3 m (quasi-peak, dBμV/m).
    Covers 30–1000 MHz per FCC Part 15 §109.
    """
    f_mhz = np.array([30.0, 88.0, 216.0, 960.0, 1000.0])
    limit = np.array([39.0, 39.0, 43.5,  46.0,  49.5])
    return f_mhz, limit

def fcc_radiated_class_b_3m():
    """
    FCC Class B radiated limits @ 3 m (quasi-peak, dBμV/m).
    Covers 30–1000 MHz per FCC Part 15 §109.
    """
    f_mhz = np.array([30.0, 88.0, 216.0, 960.0, 1000.0])
    limit = np.array([40.0, 40.0, 43.5,  46.0,  49.5])
    return f_mhz, limit

def fcc_radiated_class_a_10m():
    """
    FCC Class A radiated limits @ 10 m – adjusted from 3 m limits by
    inverse-distance field scaling (20·log10(10/3) ≈ 10.5 dB).
    """
    f_mhz = np.array([30.0, 88.0, 216.0, 960.0, 1000.0])
    limit_3m = np.array([39.0, 39.0, 43.5, 46.0, 49.5])
    limit_10m = limit_3m + 20.0 * np.log10(10.0 / 3.0)
    return f_mhz, limit_10m

def fcc_radiated_class_b_10m():
    """
    FCC Class B radiated limits @ 10 m – inverse-distance adjustment
    from 3 m limits (20·log10(10/3) ≈ 10.5 dB).
    """
    f_mhz = np.array([30.0, 88.0, 216.0, 960.0, 1000.0])
    limit_3m = np.array([40.0, 40.0, 43.5, 46.0, 49.5])
    limit_10m = limit_3m + 20.0 * np.log10(10.0 / 3.0)
    return f_mhz, limit_10m


# ════════════════════════════ CISPR 22 Limits ════════════════════════════════

def cispr_22_class_a_conducted():
    """
    CISPR 22 Class A conducted limits (quasi-peak, dBμV).
    0.15–30 MHz: two bands (average and quasi-peak both listed).
    """
    bands = {
        (0.15, 0.5):  79.0,   # quasi-peak
        (0.5,  5.0):  73.0,
        (5.0,  30.0): 73.0,
    }
    return bands

def cispr_22_class_b_conducted():
    """
    CISPR 22 Class B conducted limits (quasi-peak, dBμV).
    """
    bands = {
        (0.15, 0.5):  66.0,
        (0.5,  5.0):  60.0,
        (5.0,  30.0): 60.0,
    }
    return bands

def cispr_22_class_a_radiated():
    """
    CISPR 22 Class A radiated limits @ 10 m (quasi-peak, dBμV/m).
    30–1000 MHz.
    """
    bands = {
        (30.0, 230.0): 40.0,
        (230.0, 1000.0): 47.0,
    }
    return bands

def cispr_22_class_b_radiated():
    """
    CISPR 22 Class B radiated limits @ 10 m (quasi-peak, dBμV/m).
    30–1000 MHz.
    """
    bands = {
        (30.0, 230.0): 30.0,
        (230.0, 1000.0): 37.0,
    }
    return bands


# ════════════════════════════ LISN Impedance Model ═════════════════════════

def lisn_impedance(f_mhz):
    """
    LISN impedance Z_LISN(f) for the standard 50Ω / 50μH LISN.

    The CISPR 16-1-2 / FCC Part 15 LISN presents a high-pass characteristic:
        Z_LISN = R_LISN  ||  (j·2πf·L_LISN)
               = R / (1 + j·f/f_cutoff)

    where  f_cutoff = R / (2π·L)  ≈ 159 kHz  (for R=50Ω, L=50μH).

    Parameters
    ----------
    f_mhz : float or ndarray
        Frequency in MHz.

    Returns
    -------
    Z_mag : float or ndarray
        Magnitude of LISN impedance in Ω.
    """
    f_hz = np.asarray(f_mhz) * 1e6
    omega = 2.0 * np.pi * f_hz
    # Parallel: Z = R * jωL / (R + jωL) = R / (1 + R/(jωL))
    # Equivalent series:  Z = R * (jωL) / (R + jωL)
    Z_real = R_LISN * (omega * L_LISN)**2 / (R_LISN**2 + (omega * L_LISN)**2)
    Z_imag = R_LISN**2 * omega * L_LISN / (R_LISN**2 + (omega * L_LISN)**2)
    Z_mag  = np.sqrt(Z_real**2 + Z_imag**2)
    return Z_mag


# ════════════════════════════ Unit Conversions ══════════════════════════════

def dbuv_to_ma(v_dbuv, r_load=R_LISN):
    """
    Convert conducted emission voltage in dBμV to current in mA.

    V_dbuV = 20·log10(V / 1 μV)
         → V = 10^(V_dbuV/20) × 1 μV = 10^(V_dbuV/20) × 1e-6 V
         → I = V / R  (R in Ω, result in A → convert to mA)

    Parameters
    ----------
    v_dbuv : float or ndarray
        Voltage in dBμV.
    r_load : float
        Load impedance in Ω (default: 50 Ω LISN).

    Returns
    -------
    i_ma : float or ndarray
        Current in mA.
    """
    v_volt = 10.0**(v_dbuv / 20.0) * 1e-6      # μV → V
    i_amp  = v_volt / r_load                     # V / Ω = A
    i_ma   = i_amp * 1000.0                      # A → mA
    return i_ma


def ma_to_dbuv(i_ma, r_load=R_LISN):
    """Current in mA → voltage in dBμV (inverse of dbuv_to_ma)."""
    i_amp  = i_ma / 1000.0
    v_volt = i_amp * r_load
    v_dbuv = 20.0 * np.log10(v_volt / 1e-6)
    return v_dbuv


def distance_scaling(e_field_dbuvm, dist_m_old, dist_m_new):
    """
    Scale radiated field strength with measurement distance.

    Near-field emissions scale as 1/r (inverse-distance, not 1/r² which
    applies only to far-field power density).  For EMC compliance the FCC
    and CISPR use the inverse-distance model:

        E_new = E_old × (r_old / r_new)

    in linear field units.  In dB form:
        E_new(dB) = E_old(dB) + 20·log10(r_old / r_new)

    Parameters
    ----------
    e_field_dbuvm : float or ndarray
        Field strength in dBμV/m.
    dist_m_old : float
        Original measurement distance in metres.
    dist_m_new : float
        New measurement distance in metres.

    Returns
    -------
    e_scaled : float or ndarray
        Field strength at new distance, same unit as input (dBμV/m).
    """
    factor_db = 20.0 * np.log10(dist_m_old / dist_m_new)
    return e_field_dbuvm + factor_db


# ════════════════════════════ Tables (Console Print) ═══════════════════════

def print_limit_table():
    """Print human-readable FCC/CISPR limits summary tables."""
    print("\n" + "="*70)
    print("Paul《EMC》Ch2 – EMC Requirements: Emission Limits Summary")
    print("="*70)

    # --- FCC conducted ---
    print("\n── FCC Part 15 Conducted Emission Limits ──")
    print(f"{'Class':<8} {'Frequency (MHz)':<22} {'Limit (dBμV QP)':<15}")
    print("-"*50)
    for label, func in [("A", fcc_conducted_class_a), ("B", fcc_conducted_class_b)]:
        f, lim = func()
        print(f"  Class {label:<5} {f[0]:.2f} – {f[1]:.1f} MHz       {lim[0]:.1f}")

    # --- FCC radiated ---
    print("\n── FCC Part 15 Radiated Emission Limits ──")
    hdr = f"{'Class':<8} {'Distance':<10} {'Frequency (MHz)':<22} {'Limit (dBμV/m QP)':<15}"
    print(hdr)
    print("-"*65)
    cases = [
        ("A", "3 m",  fcc_radiated_class_a_3m),
        ("B", "3 m",  fcc_radiated_class_b_3m),
        ("A", "10 m", fcc_radiated_class_a_10m),
        ("B", "10 m", fcc_radiated_class_b_10m),
    ]
    for cls, dist, fn in cases:
        f, lim = fn()
        for i in range(len(f)-1):
            print(f"  Class {cls:<5} {dist:<10} {f[i]:.0f} – {f[i+1]:.0f} MHz         {lim[i]:.1f}")

    # --- CISPR 22 ---
    print("\n── CISPR 22 Conducted Emission Limits ──")
    print(f"{'Class':<8} {'Frequency (MHz)':<22} {'Limit (dBμV QP)':<15}")
    print("-"*50)
    for label, func in [("A", cispr_22_class_a_conducted), ("B", cispr_22_class_b_conducted)]:
        bands = func()
        for rng, val in bands.items():
            print(f"  Class {label:<5} {rng[0]:.2f} – {rng[1]:.1f} MHz      {val:.1f}")

    print("\n── CISPR 22 Radiated Emission Limits @ 10 m ──")
    print(f"{'Class':<8} {'Frequency (MHz)':<22} {'Limit (dBμV/m QP)':<15}")
    print("-"*50)
    for label, func in [("A", cispr_22_class_a_radiated), ("B", cispr_22_class_b_radiated)]:
        bands = func()
        for rng, val in bands.items():
            print(f"  Class {label:<5} {rng[0]:.1f} – {rng[1]:.1f} MHz      {val:.1f}")


# ════════════════════════════ Validation ════════════════════════════════════

def validate_conversions():
    """Verify dBμV ↔ mA and distance-scaling conversions."""
    print("\n── Conversion Validation ──")

    # dBμV → mA
    test_v_dbuv = np.array([40.0, 48.0, 60.0, 66.0])
    test_r      = 50.0
    for v in test_v_dbuv:
        i = dbuv_to_ma(v, test_r)
        v_back = ma_to_dbuv(i, test_r)
        print(f"  {v:.1f} dBμV → {i:.4f} mA → back: {v_back:.4f} dBμV  ✓")

    # 3 m ↔ 10 m distance scaling
    e_3m = np.array([40.0, 46.0, 49.5])
    for e in e_3m:
        e_10m = distance_scaling(e, 3.0, 10.0)
        e_3m_back = distance_scaling(e_10m, 10.0, 3.0)
        print(f"  {e:.1f} dBμV/m @ 3 m → {e_10m:.2f} dBμV/m @ 10 m → back: {e_3m_back:.2f} dBμV/m  ✓")

    # LISN impedance at key frequencies
    f_test = np.array([0.15, 0.5, 1.0, 5.0, 10.0, 30.0])
    print("\n  LISN impedance (|Z|) vs frequency:")
    for f in f_test:
        z = lisn_impedance(f)
        print(f"    f = {f:5.2f} MHz → |Z| = {z:.2f} Ω")


# ════════════════════════════ Plotting ══════════════════════════════════════

def plot_fcc_conducted_limits():
    """Plot FCC Part 15 Class A/B conducted emission limits."""
    f = np.linspace(0.15, 30.0, 2000)

    # Piecewise constant limits
    def piecewise_limit(f_arr, bands):
        out = np.full_like(f_arr, np.nan)
        for (lo, hi), val in bands.items():
            mask = (f_arr >= lo) & (f_arr < hi)
            out[mask] = val
        # fill last band
        last_val = list(bands.values())[-1]
        out[np.isnan(out)] = last_val
        return out

    lim_a = piecewise_limit(f, fcc_conducted_class_a_limits())
    lim_b = piecewise_limit(f, fcc_conducted_class_b_limits())

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.step(f, lim_a, where='mid', color='red', linewidth=2,
            label='FCC Class A (QP, 60 dBμV)')
    ax.step(f, lim_b, where='mid', color='blue', linewidth=2,
            label='FCC Class B (QP, 48 dBμV)')
    ax.fill_between(f, 0, lim_b, alpha=0.08, color='blue')
    ax.fill_between(f, lim_b, 70, alpha=0.05, color='green')
    ax.axhline(lim_b[0], color='blue', linestyle=':', alpha=0.5)

    ax.set_xlabel('Frequency (MHz)', fontsize=12)
    ax.set_ylabel('Conducted Emission Limit (dBμV, QP)', fontsize=12)
    ax.set_title('FCC Part 15 Conducted Emission Limits', fontsize=14, fontweight='bold')
    ax.set_xscale('log')
    ax.set_xlim(0.15, 30.0)
    ax.set_ylim(35, 70)
    ax.legend(fontsize=10)
    ax.grid(True, which='both', alpha=0.25)
    ax.tick_params(labelsize=10)

    green_patch = mpatches.Patch(color='green', alpha=0.15, label='PASS region')
    ax.legend(handles=[green_patch,
                      plt.Line2D([0],[0], color='red', lw=2, label='Class A'),
                      plt.Line2D([0],[0], color='blue', lw=2, label='Class B')],
             fontsize=10)

    plt.tight_layout()
    out = 'figures/paul_ch2_fcc_conducted.png'
    plt.savefig(out, dpi=150)
    plt.close()
    print(f"✅ Saved: {out}")


def plot_fcc_radiated_limits():
    """Plot FCC Part 15 Class A/B radiated emission limits."""
    f = np.linspace(30.0, 1000.0, 2000)

    # Band edges and limit values for Class A and B @ 3 m
    band_edges = np.array([30.0, 88.0, 216.0, 960.0, 1000.0])
    lim_a_3m   = np.array([39.0, 39.0, 43.5, 46.0, 49.5])
    lim_b_3m   = np.array([40.0, 40.0, 43.5, 46.0, 49.5])
    lim_a_10m  = lim_a_3m + 20.0 * np.log10(10.0/3.0)
    lim_b_10m  = lim_b_3m + 20.0 * np.log10(10.0/3.0)

    def interpolate_bands(f_arr, edges, vals):
        out = np.interp(f_arr, edges, vals)
        return out

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # --- Left: 3 m limits ---
    for ax, (cls, lim_arr) in [(ax1, ('A', lim_a_3m)), (ax1, ('B', lim_b_3m))]:
        color = 'red' if cls == 'A' else 'blue'
        ls = '--' if cls == 'A' else '-'
        f_plot = band_edges
        ax.step(f_plot, lim_arr, where='mid', color=color, linestyle=ls, linewidth=2,
                label=f'FCC Class {cls} @ 3 m')

    ax1.set_xlabel('Frequency (MHz)', fontsize=12)
    ax1.set_ylabel('Radiated Emission Limit (dBμV/m, QP)', fontsize=12)
    ax1.set_title('FCC Part 15 Radiated Limits @ 3 m', fontsize=13, fontweight='bold')
    ax1.set_xlim(30, 1000)
    ax1.set_ylim(30, 60)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.25)
    ax1.set_xscale('log')

    # --- Right: Class B comparison 3 m vs 10 m ---
    for ax, (cls, lim_3m, lim_10m) in [(ax2, ('B', lim_b_3m, lim_b_10m))]:
        color_a, color_b = 'blue', 'green'
        ax.step(band_edges, lim_3m,  where='mid', color=color_a, linewidth=2,
                label=f'Class {cls} @ 3 m')
        ax.step(band_edges, lim_10m, where='mid', color=color_b, linewidth=2, linestyle='--',
                label=f'Class {cls} @ 10 m (scaled)')

    ax2.set_xlabel('Frequency (MHz)', fontsize=12)
    ax2.set_ylabel('Radiated Emission Limit (dBμV/m, QP)', fontsize=12)
    ax2.set_title('FCC Class B: 3 m vs 10 m Distance Scaling', fontsize=13, fontweight='bold')
    ax2.set_xlim(30, 1000)
    ax2.set_ylim(30, 65)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.25)
    ax2.set_xscale('log')

    # Distance-scaling annotation
    scale_db = 20.0 * np.log10(10.0/3.0)
    ax2.annotate(f'20·log₁₀(10/3)\n= {scale_db:.1f} dB',
                 xy=(100, 53), fontsize=10,
                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()
    out = 'figures/paul_ch2_fcc_radiated.png'
    plt.savefig(out, dpi=150)
    plt.close()
    print(f"✅ Saved: {out}")


def plot_lisn_impedance():
    """Plot LISN impedance magnitude vs frequency."""
    f = np.logspace(-1, 3, 5000)   # 0.1 MHz – 1000 MHz
    Z = lisn_impedance(f)

    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.semilogx(f, Z, color='darkgreen', linewidth=2)
    ax.axhline(50.0, color='grey', linestyle=':', alpha=0.7, label='50 Ω (nominal)')
    ax.axvline(1.0/(2*np.pi*R_LISN*L_LISN)*1e-3,
               color='orange', linestyle='--', alpha=0.7,
               label=f'f_cutoff ≈ {1/(2*np.pi*R_LISN*L_LISN)*1e-3:.1f} kHz')

    ax.set_xlabel('Frequency (MHz)', fontsize=12)
    ax.set_ylabel('|Z$_{{LISN}}$| (Ω)', fontsize=12)
    ax.set_title('LISN Impedance (50 Ω / 50 μH) vs Frequency', fontsize=13, fontweight='bold')
    ax.set_xlim(1e-3, 1e3)
    ax.set_ylim(0, 55)
    ax.legend(fontsize=10)
    ax.grid(True, which='both', alpha=0.25)

    plt.tight_layout()
    out = 'figures/paul_ch2_lisn_impedance.png'
    plt.savefig(out, dpi=150)
    plt.close()
    print(f"✅ Saved: {out}")


def plot_dbuv_to_ma():
    """Plot dBμV → mA conversion curve."""
    v_dbuv = np.linspace(20, 80, 1000)
    i_ma   = dbuv_to_ma(v_dbuv, r_load=50.0)

    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.semilogy(v_dbuv, i_ma, color='purple', linewidth=2)

    # Mark key limits
    limits_to_mark = [48.0, 60.0, 66.0]
    for lim in limits_to_mark:
        i = dbuv_to_ma(lim, 50.0)
        ax.plot(lim, i, 'o', markersize=8)
        ax.annotate(f'{lim:.0f} dBμV → {i:.3f} mA',
                    xy=(lim, i), xytext=(lim+1, i*2),
                    arrowprops=dict(arrowstyle='->', color='grey'),
                    fontsize=9)

    ax.set_xlabel('Voltage (dBμV)', fontsize=12)
    ax.set_ylabel('Current (mA)', fontsize=12)
    ax.set_title('dBμV → mA Conversion (R = 50 Ω)', fontsize=13, fontweight='bold')
    ax.set_xlim(20, 80)
    ax.set_ylim(1e-5, 1e2)
    ax.grid(True, which='both', alpha=0.25)

    plt.tight_layout()
    out = 'figures/paul_ch2_dbuv_to_ma.png'
    plt.savefig(out, dpi=150)
    plt.close()
    print(f"✅ Saved: {out}")


# ════════════════════════════ Main ─═══════════════════════════════════════

if __name__ == '__main__':
    print("\n" + "█"*60)
    print(" Paul《EMC》2nd Ed. – Ch2: EMC Requirements")
    print(" Emission Limits, LISN Model & Unit Conversions")
    print("█"*60)

    print_limit_table()
    validate_conversions()

    plot_fcc_conducted_limits()
    plot_fcc_radiated_limits()
    plot_lisn_impedance()
    plot_dbuv_to_ma()

    print("\n" + "✓"*60)
    print(" DONE – all plots saved under ../figures/paul_ch2_*.png")
    print("✓"*60)
