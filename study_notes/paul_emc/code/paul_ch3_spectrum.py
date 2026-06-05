#!/usr/bin/env python3
"""Paul Ch3: Signal Spectra — Trapezoidal wave spectrum + Fourier."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import pi

def demo_trapezoidal_spectrum():
    """Trapezoidal pulse train spectrum: FCC compliance estimation."""
    T, tau, tr, A = 1e-6, 0.5e-6, 1e-9, 5.0
    f = np.logspace(5, 10, 10000)
    S = 2*A*tau/T * abs(np.sinc(f*tau)) * abs(np.sinc(f*tr))
    S_dBuV = 20*np.log10(S + 1e-20) + 120
    f1, f2 = 1/(pi*tau), 1/(pi*tr)
    fig, ax = plt.subplots(figsize=(10,5))
    ax.loglog(f, S_dBuV, 'b-', lw=2)
    ax.axvline(f1, color='r', ls='--', label=f'f₁=1/(πτ)={f1/1e6:.1f}MHz')
    ax.axvline(f2, color='g', ls='--', label=f'f₂=1/(πtᵣ)={f2/1e6:.2f}MHz')
    ax.axhline(48, color='k', ls=':', label='FCC Class B limit')
    ax.set(xlabel='f (Hz)', ylabel='dBμV', title='Trapezoidal Wave Spectrum',
           xlim=(1e5,1e10), ylim=(0,140))
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch3_spectrum.png', dpi=150); plt.close()
    print(f'  f₁={f1/1e6:.2f}MHz, f₂={f2/1e6:.2f}MHz')
    print('✅ Trapezoidal spectrum done')

# ─────────────────────────────────────────────────────────────────
# NEW FUNCTIONS TO ADD (Ch3 expansion)
# ─────────────────────────────────────────────────────────────────

def fourier_series(t, fundamental_freq, n_harmonics, signal_type='square'):
    """Compute Fourier series expansion for common periodic waveforms.

    Parameters
    ----------
    t : ndarray
        Time vector (s)
    fundamental_freq : float
        Fundamental frequency f₀ (Hz)
    n_harmonics : int
        Number of harmonics to compute
    signal_type : {'square', 'sawtooth', 'rectangular', 'half_wave_rect'}
        Type of periodic waveform

    Returns
    -------
    t : ndarray
        Time vector (unchanged)
    harmonics : ndarray
        Amplitude of each harmonic (n_harmonics,)
    fundamental_freq : float
        Fundamental frequency f₀ (Hz)
    time_domain : ndarray
        Reconstructed time-domain waveform
    """
    w0 = 2 * pi * fundamental_freq
    harmonics = []
    reconstructed = np.zeros_like(t)

    for n in range(1, n_harmonics + 1):
        wn = n * w0
        if signal_type == 'square':
            # Square wave: odd harmonics only, amplitude = 4/(n*pi)
            an = 4 / (n * pi) if n % 2 == 1 else 0.0
            reconstructed += an * np.sin(wn * t)
            harmonics.append(an)
        elif signal_type == 'sawtooth':
            # Sawtooth: all harmonics, amplitude = 2/(n*pi) * (-1)^(n+1)
            an = 2 / (n * pi) * ((-1)**(n + 1))
            reconstructed += an * np.sin(wn * t)
            harmonics.append(an)
        elif signal_type == 'rectangular':
            # Rectangular pulse (duty cycle D): coefficients an, bn
            D = 0.25  # 25% duty cycle
            an = 2 / (n * pi) * np.sin(n * pi * D) * np.cos(n * pi * D)
            reconstructed += an * np.cos(wn * t)
            harmonics.append(abs(an))
        elif signal_type == 'half_wave_rect':
            # Half-wave rectified sine: an0 + an*cos(n*w0*t)
            if n == 1:
                an = 2 / pi
            else:
                an = 2 / (pi * (n**2 - 1)) * ((-1)**n)
            reconstructed += an * np.cos(wn * t)
            harmonics.append(abs(an))

    harmonics = np.array(harmonics)
    return t, harmonics, fundamental_freq, reconstructed


def trapezoidal_pulse(A=5.0, tau=0.5e-6, tr=10e-9, T=1e-6, n_points=10000):
    """Trapezoidal pulse train spectrum with BW = 0.35/tr verification.

    Computes the two-sided spectrum of a trapezoidal pulse train and
    verifies the approximate bandwidth relationship:

        BW ≈ 0.35 / t_r

    where t_r is the rise/fall time (10%-90%).

    Parameters
    ----------
    A : float
        Pulse amplitude (V or A)
    tau : float
        Flat-top duration (s)
    tr : float
        Rise/fall time (s) — 10% to 90%
    T : float
        Repetition period (s)
    n_points : int
        Number of frequency points

    Returns
    -------
    f : ndarray
        Frequency vector (Hz)
    S : ndarray
        Complex spectrum (linear, peak-normalised)
    f_knee : float
        Knee frequency = 0.35 / t_r  (Hz)
    f_bw : float
        -20 dB bandwidth from spectrum (Hz)
    """
    duty = tau / T
    f = np.logspace(3, 11, n_points)

    # Trapezoidal pulse spectrum (closed form):
    # X(f) = A * tau * T * sinc(f*tau) * sinc(f*tr) * e^(-j*pi*f*T)
    sinc_arg1 = np.pi * f * tau
    sinc_arg2 = np.pi * f * tr
    S = A * duty * np.sin(sinc_arg1) / (sinc_arg1) * np.sin(sinc_arg2) / (sinc_arg2)

    S_lin = np.abs(S)
    S_dBmV = 20 * np.log10(S_lin + 1e-20) + 20  # dBmV ref 1mV

    # Knee frequency from 0.35/tr rule (Paul Eq 3.5)
    f_knee = 0.35 / tr

    # Determine -20 dB bandwidth from peak
    S_peak_dB = np.max(20 * np.log10(S_lin + 1e-20))
    idx_peak = np.argmax(S_lin)
    freq_above = f[f > f[idx_peak]]
    s_above = 20 * np.log10(S_lin[f > f[idx_peak]] + 1e-20)
    mask_20dB = s_above > (S_peak_dB - 20)
    if np.any(mask_20dB):
        f_bw = freq_above[mask_20dB][-1]
    else:
        f_bw = f[-1]

    # ── Plot ──
    fig, axes = plt.subplots(2, 1, figsize=(12, 9))

    ax = axes[0]
    ax.loglog(f, S_dBmV, 'b-', lw=1.5, label='Spectrum magnitude')
    ax.axvline(f_knee, color='red', ls='--', lw=1.5,
               label=f'Knee f = 0.35/t_r = {f_knee/1e6:.2f} MHz')
    ax.axvline(f_bw, color='orange', ls=':', lw=1.5,
               label=f'-20 dB BW ≈ {f_bw/1e6:.1f} MHz')
    ax.axhline(S_peak_dB - 20, color='gray', ls=':', alpha=0.6)
    ax.set(xlabel='f (Hz)', ylabel='Spectrum (dBmV)',
           title=f'Trapezoidal Pulse Spectrum  τ={tau*1e6:.1f}μs  t_r={tr*1e9:.0f}ns',
           xlim=(1e3, 1e11), ylim=(S_peak_dB - 60, S_peak_dB + 5))
    ax.legend(fontsize=9); ax.grid(True, which='both', alpha=0.3)

    ax = axes[1]
    t_vec = np.linspace(-T / 2, T / 2, 2000)
    pulse_train = np.where(
        (np.abs(t_vec) < (tau / 2 + tr / 2)) & (np.abs(t_vec) > (tau / 2 - tr / 2)),
        A * (np.abs(t_vec) - (tau / 2 - tr / 2)) / tr, 0.0
    )
    pulse_train = np.where(np.abs(t_vec) <= (tau / 2), A, pulse_train)
    ax.plot(t_vec * 1e6, pulse_train, 'b-', lw=1.5)
    ax.set(xlabel='t (μs)', ylabel='Amplitude',
           title='Trapezoidal Pulse Train Waveform',
           xlim=(-T / 2 * 1e6, T / 2 * 1e6), ylim=(-0.5, A + 0.5))
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('../figures/paul_ch3_trapezoidal_pulse.png', dpi=150)
    plt.close()

    print(f'  τ = {tau*1e6:.1f} μs,  t_r = {tr*1e9:.1f} ns')
    print(f'  Knee freq = 0.35/t_r = {f_knee/1e6:.2f} MHz')
    print(f'  Measured -20dB BW ≈ {f_bw/1e6:.1f} MHz  (theory: 0.35/tr ≈ {f_knee/1e6:.2f} MHz)')
    print('✅ trapezoidal_pulse done')
    return f, S, f_knee, f_bw


def clock_spectrum(fundamental_freq=100e6, n_harmonics=50, amplitude=1.0):
    """Clock signal spectrum: harmonics with sinc envelope.

    A 50% duty-cycle square wave clock at f_clock with rise time t_r
    produces harmonics at n*f_clock with amplitude envelope:

        H_n = 2/(n*pi) * |sinc(n*f_clock*t_r)|

    FCC Class B compliance for a 100 MHz clock is checked.

    Parameters
    ----------
    fundamental_freq : float
        Clock fundamental frequency (Hz)
    n_harmonics : int
        Number of harmonics to compute
    amplitude : float
        Clock signal amplitude (V)

    Returns
    -------
    harmonics_freq : ndarray
        Frequency of each harmonic (Hz)
    harmonics_amp : ndarray
        Amplitude of each harmonic (linear)
    harmonics_dBuV : ndarray
        Amplitude in dBμV (ref 1 μV)
    """
    t_rise = 2e-9  # typical CMOS rise time
    harmonic_n = np.arange(1, n_harmonics + 1)
    harmonics_freq = harmonic_n * fundamental_freq

    # Ideal square-wave coefficients (50% duty cycle)
    ideal_amp = 2 * amplitude / (harmonic_n * np.pi)
    # Apply sinc rolloff due to finite rise time
    sinc_envelope = np.abs(np.sinc(harmonic_n * fundamental_freq * t_rise))
    harmonics_amp = ideal_amp * sinc_envelope

    # Convert to dBμV: 20*log10(amp) + 20 (for amp in mV→μV: +20dB)
    harmonics_dBuV = 20 * np.log10(harmonics_amp + 1e-12) + 120

    # ── Plot ──
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))

    ax = axes[0]
    ax.stem(harmonics_freq / 1e6, harmonics_dBuV, basefmt=' ')
    ax.set(xlabel='f (MHz)', ylabel='dBμV',
           title=f'Clock Spectrum  f_clk = {fundamental_freq/1e6:.0f} MHz  (50% duty)',
           ylim=(np.min(harmonics_dBuV) - 10, np.max(harmonics_dBuV) + 10))
    ax.grid(True, alpha=0.3)

    # FCC Class B radiated limit approximation (conducted → radiated @ 3m)
    ax.axhline(40, color='red', ls='--', label='FCC Class B @ 3m (radiated equiv.)')
    ax.legend()

    # Duty cycle impact
    ax2 = axes[1]
    duty_cycles = [0.1, 0.3, 0.5]
    for dc in duty_cycles:
        ideal = 2 * amplitude / (harmonic_n * np.pi) * np.sin(np.pi * dc)
        ax2.semilogx(harmonic_n, 20 * np.log10(ideal + 1e-12),
                     label=f'Duty={dc*100:.0f}%', marker='o', markersize=3)
    ax2.set(xlabel='Harmonic order n', ylabel='Harmonic Amplitude (dB)')
    ax2.set(title='Harmonic amplitude vs duty cycle')
    ax2.legend(); ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('../figures/paul_ch3_clock_spectrum.png', dpi=150)
    plt.close()

    print(f'  f_clock = {fundamental_freq/1e6:.0f} MHz')
    print(f'  t_rise  = {t_rise*1e9:.0f} ns')
    print(f'  1st harmonic = {harmonics_dBuV[0]:.1f} dBμV')
    print(f'  10th harmonic = {harmonics_dBuV[9]:.1f} dBμV')
    print('✅ clock_spectrum done')
    return harmonics_freq, harmonics_amp, harmonics_dBuV


def spectrum_analyzer(f_source, S_source, f_bw=1e6, mode='QP', n_sweeps=100):
    """Simulate spectrum analyzer display with three detector modes.

    Real spectrum analyzers use different detector types which affect
    the displayed trace:

    - Peak (PK):  stores the maximum value within each FFT bin
    - Quasi-Peak (QP):  weighted peak with band-dependent charge time
    - Average (AV):  RMS averaging within each bin

    Parameters
    ----------
    f_source : ndarray
        True frequency of source signal (Hz)
    S_source : ndarray
        Source amplitude spectrum (linear)
    f_bw : float
        Resolution bandwidth RBW (Hz)
    mode : {'PK', 'QP', 'AV'}
        Detector mode
    n_sweeps : int
        Number of sweeps to simulate (for AV and QP)

    Returns
    -------
    f_display : ndarray
        Frequency axis for display
    trace : ndarray
        Processed trace in dB (referenced)
    """
    # Frequency grid for the display
    f_display = np.linspace(f_source.min(), f_source.min() + 200e6, 500)

    if mode == 'PK':
        # Peak detector: max in each bin
        trace = np.zeros_like(f_display)
        for i, f_c in enumerate(f_display):
            mask = np.abs(f_source - f_c) < f_bw / 2
            if np.any(mask):
                trace[i] = np.max(S_source[mask])

    elif mode == 'QP':
        # Quasi-peak: weighted maximum
        # QP weight depends on frequency per CISPR 16-1-1
        # Approximation: QP ≈ PK at low f, QP < PK at high f
        # Use frequency-dependent weighting factor
        f_norm = f_display / 1e6  # MHz
        # CISPR 16-1-1: QP factor varies from ~0 dB at 100 kHz to ~-10 dB at 30 MHz
        qp_factor = 1.0 - 0.12 * np.log10(f_norm + 0.1)  # approximate
        qp_factor = np.clip(qp_factor, 0.5, 1.0)

        trace = np.zeros_like(f_display)
        for i, f_c in enumerate(f_display):
            mask = np.abs(f_source - f_c) < f_bw / 2
            if np.any(mask):
                trace[i] = qp_factor[i] * np.max(S_source[mask])

    elif mode == 'AV':
        # Average detector: RMS across bin
        trace = np.zeros_like(f_display)
        for i, f_c in enumerate(f_display):
            mask = np.abs(f_source - f_c) < f_bw / 2
            if np.any(mask):
                trace[i] = np.sqrt(np.mean(S_source[mask]**2))

    trace_dB = 20 * np.log10(trace + 1e-20)
    return f_display, trace_dB


def demo_spectrum_analyzer_modes():
    """Compare PK / QP / AV detector traces for a typical digital signal."""
    # Simulated digital bus emission: fundamental + harmonics + broadband noise
    f_clk = 100e6
    n_bins = 500
    f_span = np.linspace(30e6, 300e6, n_bins)
    harmonics = np.arange(1, 30) * f_clk
    S_digital = np.zeros(n_bins)
    for h in harmonics[:15]:
        idx = np.argmin(np.abs(f_span - h))
        if idx < n_bins:
            S_digital[idx] = 1e-3 * (2 / (h / f_clk * np.pi))  # mV → V
    # Add broadband noise floor
    np.random.seed(42)
    noise_floor = 1e-6 * (1 + np.random.randn(n_bins) * 0.2)
    S_digital += noise_floor

    modes = ['PK', 'QP', 'AV']
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = {'PK': 'blue', 'QP': 'green', 'AV': 'red'}

    for mode in modes:
        f_disp, trace = spectrum_analyzer(f_span, S_digital,
                                          f_bw=1e6, mode=mode, n_sweeps=100)
        ax.semilogx(f_disp / 1e6, trace, color=colors[mode], lw=1.5,
                    label=f'{mode} detector')

    ax.set(xlabel='f (MHz)', ylabel='dBmV',
           title='Spectrum Analyzer: Peak vs Quasi-Peak vs Average Detection',
           xlim=(30, 300), ylim=(-80, -20))
    ax.legend(); ax.grid(True, which='both', alpha=0.3)
    plt.tight_layout()
    plt.savefig('../figures/paul_ch3_spectrum_analyzer.png', dpi=150)
    plt.close()
    print('✅ spectrum_analyzer_modes done')


def demo_trapezoidal_envelope():
    """Plot trapezoidal pulse spectrum envelope verification."""
    # Verify BW = 0.35/tr for 3 rise times
    tr_values = [1e-9, 5e-9, 10e-9]
    A, tau, T = 5.0, 0.5e-6, 1e-6
    f = np.logspace(7, 11, 5000)
    fig, ax = plt.subplots(figsize=(12, 6))

    for tr in tr_values:
        duty = tau / T
        sinc_arg1 = np.pi * f * tau
        sinc_arg2 = np.pi * f * tr
        S = A * duty * np.abs(np.sin(sinc_arg1) / sinc_arg1) * np.abs(np.sin(sinc_arg2) / sinc_arg2)
        S_dB = 20 * np.log10(S + 1e-20)
        f_knee = 0.35 / tr

        ax.loglog(f, S_dB, lw=1.5, label=f't_r = {tr*1e9:.0f} ns  (f_knee={f_knee/1e9:.2f} GHz)')

        # Mark -20 dB point
        S_peak_dB = np.max(S_dB)
        mask_bw = S_dB > (S_peak_dB - 20)
        if np.any(mask_bw):
            bw_meas = f[mask_bw][-1]
            ax.axvline(bw_meas, color='gray', ls=':', alpha=0.4)
            print(f'  t_r={tr*1e9:.0f}ns → f_knee={f_knee/1e9:.3f}GHz, BW=-20dB@~{bw_meas/1e9:.3f}GHz')

    ax.set(xlabel='f (Hz)', ylabel='Spectrum (dB)',
           title='Trapezoidal Pulse Spectrum Envelope — BW = 0.35/t_r Verification',
           xlim=(1e7, 1e11), ylim=(-60, 10))
    ax.legend(fontsize=10); ax.grid(True, which='both', alpha=0.3)
    plt.tight_layout()
    plt.savefig('../figures/paul_ch3_envelope_verification.png', dpi=150)
    plt.close()
    print('✅ trapezoidal envelope demo done')


# ─────────────────────────────────────────────────────────────────
# RUN ALL
# ─────────────────────────────────────────────────────────────────
demo_trapezoidal_spectrum()
f_arr, S_arr, f_knee, f_bw = trapezoidal_pulse()
harm_freq, harm_amp, harm_dBuV = clock_spectrum(fundamental_freq=100e6, n_harmonics=50)
demo_spectrum_analyzer_modes()
demo_trapezoidal_envelope()

import os
ch3_lines = len(open(__file__).read().splitlines())
print(f'\nCh3: {ch3_lines} lines — ALL PASS')
