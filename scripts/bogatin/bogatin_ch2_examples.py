#!/usr/bin/env python3
"""
bogatin_ch2_examples.py — Chapter 2: Time and Frequency Domains

Concepts demonstrated:
  1. Ideal square wave: time-domain synthesis from harmonic series (Eq. 2-3)
  2. Bandwidth vs. rise time: empirical BW = 0.35 / RT (Eq. 2-4)
  3. Effect of bandwidth truncation on rise time (Figures 2-8, 2-9)
  4. Trapezoidal waveform spectrum vs. ideal square wave (Figure 2-12)
  5. Interconnect bandwidth: rise time degradation (Eq. 2-6, 2-7)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
import os
from numpy.fft import fft, fftfreq
from scipy import signal

FIGURE_DIR = "/home/ubuntu/.openclaw/workspace/textbooks/bogatin/figures"
os.makedirs(FIGURE_DIR, exist_ok=True)

# Global style
plt.rcParams['figure.dpi'] = 150


# ============================================================
# Example 1: Ideal Square Wave Synthesis from Harmonics
# ============================================================
def square_wave_synthesis():
    """
    Synthesize a 1-GHz ideal square wave from odd harmonics.
    A_n = 2/(pi*n)  for odd n. (Eq. 2-3)
    Replicates Figures 2-8 and 2-9 (conceptual).
    """
    f_clock = 1.0  # GHz
    T_period = 1.0 / f_clock  # nsec
    t = np.linspace(0, 2 * T_period, 2000, endpoint=False)  # time in nsec
    dc_offset = 0.5  # zeroth harmonic

    harmonics_to_show = [1, 3, 7, 19, 31]
    colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(harmonics_to_show)))

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Left: partial sums showing progressive synthesis
    ax_left = axes[0]
    for idx, N_max in enumerate(harmonics_to_show[:4]):  # 1, 3, 7, 19
        waveform = dc_offset * np.ones_like(t)
        for n in range(1, N_max + 1, 2):  # odd harmonics only
            A_n = 2.0 / (np.pi * n)
            waveform += A_n * np.sin(2 * np.pi * n * f_clock * t)
        ax_left.plot(t, waveform, label=f'Up to {N_max}th harmonic',
                     color=colors[idx], linewidth=1.5)

    ax_left.axhline(dc_offset, color='gray', linestyle=':', alpha=0.4)
    ax_left.set_xlabel('Time (nsec)')
    ax_left.set_ylabel('Voltage (V)')
    ax_left.set_title('Figure 2-8/9: Square Wave Synthesis from Harmonics')
    ax_left.grid(True, alpha=0.3)
    ax_left.legend(fontsize=9)
    ax_left.set_xlim(0, 1.2)
    ax_left.set_ylim(-0.2, 1.3)

    # Right: full synthesis up to 31st harmonic, show rise time zoom
    ax_right = axes[1]
    waveform_full = dc_offset * np.ones_like(t)
    for n in range(1, 101, 2):
        A_n = 2.0 / (np.pi * n)
        waveform_full += A_n * np.sin(2 * np.pi * n * f_clock * t)

    ax_right.plot(t, waveform_full, 'b-', linewidth=1.5, label='Up to 99th harmonic')
    ax_right.set_xlabel('Time (nsec)')
    ax_right.set_ylabel('Voltage (V)')
    ax_right.set_title('High Harmonic Synthesis (99 harmonics)')
    ax_right.grid(True, alpha=0.3)
    ax_right.legend(fontsize=9)
    ax_right.set_xlim(0.45, 0.65)
    ax_right.set_ylim(-0.1, 1.2)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch2_square_wave_synthesis.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch2_square_wave_synthesis.png"))
    plt.close(fig)
    print("[Example 1] Square wave harmonic synthesis plots saved.")

    return t, waveform_full


# ============================================================
# Example 2: Bandwidth vs. Rise Time (Eq. 2-4) — Replicate Fig 2-11
# ============================================================
def bandwidth_vs_rise_time():
    """
    Measure 10-90 rise time from synthesized waveforms with known bandwidth.
    Plot BW = 0.35 / RT and compare with empirical data.
    Replicates Figure 2-11.
    """
    f_clock = 1.0  # GHz
    T = 1.0 / f_clock  # nsec
    t_fine = np.linspace(0, 2 * T, 500000, endpoint=False)  # very fine for rise time

    # Synthesize with different max harmonics
    max_harmonics = np.arange(1, 101, 2)  # odd harmonics only
    rise_times = []

    for N_max in max_harmonics:
        waveform = 0.5 * np.ones_like(t_fine)
        for n in range(1, N_max + 1, 2):
            A_n = 2.0 / (np.pi * n)
            waveform += A_n * np.sin(2 * np.pi * n * f_clock * t_fine)

        # Find rising edge near t = 0
        rising_mask = (t_fine >= 0) & (t_fine <= 0.5 * T)
        t_rising = t_fine[rising_mask]
        v_rising = waveform[rising_mask]

        # Find 10% and 90% levels
        v_min, v_max = 0, 1.0
        v_10 = v_min + 0.1 * (v_max - v_min)
        v_90 = v_min + 0.9 * (v_max - v_min)

        # Crossings (crude but works with fine resolution)
        idx_10 = np.argmin(np.abs(v_rising - v_10))
        idx_90 = np.argmin(np.abs(v_rising - v_90))

        rt = t_rising[idx_90] - t_rising[idx_10]
        rise_times.append(rt)

    rise_times = np.array(rise_times)
    bandwidths = max_harmonics * f_clock  # GHz

    # Plot: BW vs RT
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.loglog(rise_times, bandwidths, 'o', color='blue', markersize=4,
              label='Extracted from synthesis')

    # Overlay BW = 0.35 / RT
    rt_fit = np.logspace(-4, 2, 100)
    bw_fit = 0.35 / rt_fit
    ax.loglog(rt_fit, bw_fit, 'r-', linewidth=2, label='$BW = 0.35 / RT$')

    ax.set_xlabel('10–90% Rise Time (nsec)')
    ax.set_ylabel('Bandwidth (GHz)')
    ax.set_title('Figure 2-11: Bandwidth vs. Rise Time (Square Wave Synthesis)')
    ax.grid(True, which='both', alpha=0.3)
    ax.legend()
    ax.set_xlim(0.005, 0.5)
    ax.set_ylim(0.5, 100)

    # Annotate key points
    for rt_val in [0.01, 0.035, 0.1, 0.35]:
        bw_val = 0.35 / rt_val
        ax.annotate(f'RT={rt_val:.2f}ns\nBW={bw_val:.1f}GHz',
                    xy=(rt_val, bw_val), fontsize=8,
                    xytext=(rt_val * 1.5, bw_val * 0.7),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=0.5),
                    bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.5))

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch2_bandwidth_vs_rise_time.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch2_bandwidth_vs_rise_time.png"))
    plt.close(fig)
    print("[Example 2] Bandwidth vs. rise time plot saved.")

    # Print a few validation points
    print("\n  Validation:")
    print(f"  RT = 0.10 nsec -> BW = 0.35/0.10 = {0.35/0.10:.2f} GHz")
    print(f"  RT = 0.35 nsec -> BW = 0.35/0.35 = {0.35/0.35:.2f} GHz")
    print(f"  RT = 1.00 nsec -> BW = 0.35/1.00 = {0.35/1.00:.2f} GHz")

    return rise_times, bandwidths


# ============================================================
# Example 3: Trapezoidal Waveform Spectrum vs. Ideal Square Wave (Fig 2-12)
# ============================================================
def trapezoid_spectrum_comparison():
    """
    Compare the frequency-domain spectra of an ideal square wave
    and a trapezoidal wave with finite rise time (8% of period).
    Replicates Figure 2-12.
    """
    f_clock = 1.0  # GHz
    T = 1.0 / f_clock  # nsec
    N_samples = 4096  # power of 2 for FFT
    t = np.linspace(0, T, N_samples, endpoint=False)  # one period

    # Ideal square wave: 50% duty
    square_wave = np.where(t < 0.5 * T, 0.0, 1.0)

    # Trapezoidal wave with rise/fall time = 8% of T
    rt_fraction = 0.08  # 8%
    rt_nsec = rt_fraction * T
    n_rise = int(rt_nsec / (T / N_samples))
    trap_wave = np.zeros_like(t)
    # Rising edge
    trap_wave[:n_rise] = np.linspace(0, 1, n_rise)
    # High state
    high_start = n_rise
    high_end = N_samples // 2
    trap_wave[high_start:high_end] = 1.0
    # Falling edge
    fall_start = high_end
    fall_end = high_end + n_rise
    trap_wave[fall_start:fall_end] = np.linspace(1, 0, n_rise)
    # Remainder at 0

    # Compute FFT
    def get_spectrum(waveform, n_harmonics=53):
        spectrum = fft(waveform) / N_samples
        harm_indices = np.arange(1, n_harmonics + 1)
        amps = 2.0 * np.abs(spectrum[harm_indices])  # peak amplitude
        return harm_indices, amps

    harm_idx, sq_amps = get_spectrum(square_wave, 53)
    _, trap_amps = get_spectrum(trap_wave, 53)

    # Plot: time domain and frequency domain
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Top: time domain
    ax1.plot(t, square_wave, 'b-', linewidth=2, alpha=0.7, label='Ideal square wave')
    ax1.plot(t, trap_wave, 'r-', linewidth=2, alpha=0.7, label=f'Trapezoid (RT={rt_fraction*100:.0f}% T)')
    ax1.set_xlabel('Time (nsec)')
    ax1.set_ylabel('Voltage (V)')
    ax1.set_title('Figure 2-12: Time Domain Waveforms (1 GHz)')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_xlim(0, 1.0)
    ax1.set_ylim(-0.1, 1.2)

    # Bottom: frequency domain (bar chart)
    width = 0.35
    ax2.bar(harm_idx - width/2, sq_amps, width, label='Ideal square wave',
            color='blue', alpha=0.5, edgecolor='blue', linewidth=0.5)
    ax2.bar(harm_idx + width/2, trap_amps, width, label=f'Trapezoid',
            color='red', alpha=0.5, edgecolor='red', linewidth=0.5)

    # Mark the -3 dB line (70% of ideal square wave)
    ax2.axhline(y=0.7 * sq_amps[0], color='gray', linestyle='--', alpha=0.5,
                label='70% of 1st harmonic (significance threshold)')

    ax2.set_xlabel('Harmonic Number (n)')
    ax2.set_ylabel('Amplitude (V)')
    ax2.set_title('Frequency Domain Spectra')
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=9)
    ax2.set_xlim(0, 22)
    ax2.set_ylim(0, 0.7)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch2_trapezoid_spectrum.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch2_trapezoid_spectrum.png"))
    plt.close(fig)
    print("[Example 3] Trapezoid spectrum comparison plot saved.")

    # Print comparison at key harmonics
    print("\n  Spectrum comparison:")
    for h in [1, 3, 5, 7, 9]:
        idx = h - 1
        ratio = trap_amps[idx] / sq_amps[idx] * 100 if sq_amps[idx] > 0 else 0
        print(f"  Harmonic {h:2d}: Square={sq_amps[idx]:.3f}V  "
              f"Trap={trap_amps[idx]:.3f}V  Ratio={ratio:.0f}%")

    return harm_idx, sq_amps, trap_amps


# ============================================================
# Example 4: Interconnect Rise Time Degradation (Eq. 2-6, 2-7)
# ============================================================
def interconnect_rise_time_degradation():
    """
    RT_out = sqrt(RT_in^2 + RT_interconnect^2)
    Demonstrate how interconnect bandwidth affects transmitted rise time.
    """
    rt_ic = 43e-3  # interconnect intrinsic rise time: 43 psec (from 8 GHz BW)
    rt_in_values = np.logspace(np.log10(10e-3), np.log10(2000e-3), 100)  # 10 psec to 2 nsec
    rt_out_values = np.sqrt(rt_in_values**2 + rt_ic**2)
    degradation = (rt_out_values - rt_in_values) / rt_in_values * 100
    ten_pct_threshold = 1.1  # 10% degradation = output is 1.1x input

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Left: input vs output rise time
    ax1.loglog(rt_in_values * 1e3, rt_out_values * 1e3, 'b-', linewidth=2,
               label=f'Interconnect RT_ic = {rt_ic*1e3:.0f} psec')
    ax1.loglog(rt_in_values * 1e3, rt_in_values * 1e3, 'k--', linewidth=1,
               alpha=0.5, label='No degradation (RT_out = RT_in)')
    ax1.axhline(y=rt_ic * 1e3, color='gray', linestyle=':', alpha=0.5,
                label=f'RT_ic = {rt_ic*1e3:.0f} psec')

    ax1.set_xlabel('Input Rise Time (psec)')
    ax1.set_ylabel('Output Rise Time (psec)')
    ax1.set_title('Rise Time Through Interconnect')
    ax1.grid(True, which='both', alpha=0.3)
    ax1.legend(fontsize=8)
    ax1.set_xlim(5, 2000)
    ax1.set_ylim(5, 2000)

    # Right: percentage degradation
    ax2.semilogx(rt_in_values * 1e3, degradation, 'r-', linewidth=2)
    ax2.axhline(y=10, color='gray', linestyle='--', alpha=0.5,
                label='10% degradation threshold')
    ax2.axvline(x=rt_ic * 1e3 * 2, color='green', linestyle=':', alpha=0.5,
                label=f'2 × RT_ic = {rt_ic*1e3*2:.0f} psec')

    ax2.set_xlabel('Input Rise Time (psec)')
    ax2.set_ylabel('Rise Time Increase (%)')
    ax2.set_title('Percentage Degradation')
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=8)
    ax2.set_xlim(5, 2000)
    ax2.set_ylim(0, 100)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch2_rise_time_degradation.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch2_rise_time_degradation.png"))
    plt.close(fig)
    print("[Example 4] Interconnect rise time degradation plots saved.")

    # Key validation: 50 psec input from Eq. 2-7
    rt_in_50ps = 50e-3
    rt_out_50ps = np.sqrt(rt_in_50ps**2 + rt_ic**2)
    print(f"\n  Validation (Eq. 2-7): RT_in=50ps, RT_ic=43ps")
    print(f"  RT_out = sqrt({rt_in_50ps*1e3:.0f}^2 + {rt_ic*1e3:.0f}^2) = {rt_out_50ps*1e3:.0f} psec")
    print(f"  (Text says ~67 psec, agrees well)")

    return rt_in_values, rt_out_values


# ============================================================
# Example 5: BW = 5 × F_clock Relationship (Eq. 2-5 + Fig 2-14 concept)
# ============================================================
def clock_bandwidth_demo():
    """
    Demonstrate that with RT = 7% of period, BW = 0.35/(0.07*T) ≈ 5*F_clock.
    Also show that same clock frequency can produce VERY different BW
    depending on rise time (Fig 2-14 concept).
    """
    f_clock = 1.0  # GHz
    T = 1.0 / f_clock  # nsec
    t = np.linspace(0, T, 1000, endpoint=False)

    # Four waveforms with same clock freq, different rise times (Fig 2-14)
    rt_pcts = [0.25, 0.10, 0.05, 0.01]  # fraction of period
    labels = [f'RT = {p*100:.0f}% T → BW = {0.35/(p*T):.1f} GHz' for p in rt_pcts]
    colors = ['purple', 'blue', 'green', 'red']

    fig, ax = plt.subplots(figsize=(9, 5))

    for idx, (pct, label, color) in enumerate(zip(rt_pcts, labels, colors)):
        rt_ns = pct * T
        n_rise = max(1, int(rt_ns / (T / len(t))))
        trap = np.zeros_like(t)
        trap[:n_rise] = np.linspace(0, 1, n_rise)
        high_end = len(t) // 2
        trap[n_rise:high_end] = 1.0
        fall_end = high_end + n_rise
        trap[high_end:fall_end] = np.linspace(1, 0, n_rise)
        # offset for visibility
        ax.plot(t + idx * 0.02, trap + idx * 0.05, color=color, linewidth=1.5,
                label=label)

    ax.set_xlabel('Time (nsec)')
    ax.set_ylabel('Voltage (V)')
    ax.set_title('Figure 2-14 Concept: Same 1 GHz Clock, Different Rise Times')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8, loc='lower right')
    ax.set_xlim(0, 1.0)
    ax.set_ylim(-0.1, 1.3)

    fig.tight_layout()
    fig.savefig(os.path.join(FIGURE_DIR, "ch2_clock_bw_comparison.pdf"))
    fig.savefig(os.path.join(FIGURE_DIR, "ch2_clock_bw_comparison.png"))
    plt.close(fig)
    print("[Example 5] Clock bandwidth comparison plot saved.")

    # Print BW for each case
    print(f"\n  Clock frequency = {f_clock} GHz")
    for pct, color in zip(rt_pcts, colors):
        bw = 0.35 / (pct * T)
        print(f"  RT = {pct*100:.0f}% T → BW = {bw:.1f} GHz  (BW/F_clock = {bw:.1f})")

    t


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Bogatin SI/PI 2nd Ed. — Chapter 2 Examples")
    print("=" * 60)

    # Example 1
    square_wave_synthesis()

    # Example 2
    bandwidth_vs_rise_time()

    # Example 3
    trapezoid_spectrum_comparison()

    # Example 4
    interconnect_rise_time_degradation()

    # Example 5
    clock_bandwidth_demo()

    print("\n" + "=" * 60)
    print("All Chapter 2 examples complete.")
    print("=" * 60)
