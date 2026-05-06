#!/usr/bin/env python3
"""
Razavi RF Microelectronics, 2nd Ed. — Ch3: Communication Concepts
Examples: QPSK constellation, GMSK waveform, receiver linearity requirements.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ──────────────────────────────────────────────────────
# Example 3.7: QPSK constellation with phase mismatch
# ──────────────────────────────────────────────────────
def example_qpsk_phase_mismatch():
    """Plot QPSK constellation with phase error theta."""
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))

    for idx, theta_deg in enumerate([0, 10, 30]):
        theta = np.deg2rad(theta_deg)
        ax = axes[idx]

        # Ideal QPSK points
        alpha1_vals = [1, 1, -1, -1]
        alpha2_vals = [1, -1, 1, -1]

        beta1_arr = []
        beta2_arr = []
        for a1, a2 in zip(alpha1_vals, alpha2_vals):
            b1 = a1 * np.cos(theta)
            b2 = a2 - a1 * np.sin(theta)
            beta1_arr.append(b1)
            beta2_arr.append(b2)

        # Plot
        ax.scatter(alpha1_vals, alpha2_vals, c='blue', s=60, label='Ideal', alpha=0.5)
        ax.scatter(beta1_arr, beta2_arr, c='red', s=60, marker='x', label=f'{theta_deg}° error')
        ax.axhline(0, color='gray', lw=0.5)
        ax.axvline(0, color='gray', lw=0.5)
        ax.set_xlim(-1.8, 1.8)
        ax.set_ylim(-1.8, 1.8)
        ax.set_xlabel('I')
        ax.set_ylabel('Q')
        ax.set_title(f'QPSK Constellation ($\\theta={theta_deg}^\\circ$)')
        ax.grid(True, alpha=0.3)
        ax.set_aspect('equal')
        if idx == 0:
            ax.legend()

    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/razavi/figures/ch3_qpsk_phase_error.png', dpi=150)
    plt.close(fig)
    print("Saved: ch3_qpsk_phase_error.png")

# ──────────────────────────────────────────────────────
# Example 3.12/3.13: Receiver linearity requirements
# ──────────────────────────────────────────────────────
def example_receiver_linearity():
    """
    GSM receiver: P1dB and IIP3 requirements from blocker specifications.
    """
    print("Example 3.12: GSM Receiver Linearity")
    print("="*50)

    # GSM specs
    P_sen = -102  # dBm
    NF = 8        # dB
    B = 200e3     # Hz
    SNR_min = 12  # dB

    # Blocker profile (Fig 3.65):
    # 0.6 MHz offset: -33 dBm
    # 1.6 MHz offset: -43 dBm
    # 3.0 MHz offset: -33 dBm
    blockers = [
        (0.6e6, -33),
        (1.6e6, -43),
        (3.0e6, -33),
    ]

    for f_offset, P_block_dbm in blockers:
        # P1dB requirement: blocker + signal < P1dB (rough)
        P1dB_req = P_block_dbm  # blocker must be below P1dB
        print(f"  Blocker @ {f_offset/1e6:.1f} MHz, {P_block_dbm} dBm")
        print(f"    P1dB required: < {P1dB_req + 3:.0f} dBm (some margin)")

    # IIP3 for two blockers at 0.6 and 1.6 MHz spacing
    # IM3 at 1.6+0.6=2.2 MHz offset may fall in band
    P_blk = -33  # dBm, blockers at 0.6 and 3.0 MHz
    P_noise_floor = -174 + NF + 10*np.log10(B)
    # IIP3 such that IM3 < noise floor
    IIP3_req = P_blk + (P_blk - P_noise_floor)/2
    print(f"\n  Noise floor: {P_noise_floor:.0f} dBm")
    print(f"  IIP3 requirement: {IIP3_req:.0f} dBm")

    # Compare with WCDMA
    print("\nExample 3.13: WCDMA Receiver Linearity")
    B_w = 3.84e6
    NF_w = 10
    SNR_w = 7  # dB (processing gain considered)
    P_sen_w = -174 + NF_w + 10*np.log10(B_w) + SNR_w
    print(f"  WCDMA sensitivity: {P_sen_w:.0f} dBm")

    print()

# ──────────────────────────────────────────────────────
# GMSK spectrum visualization
# ──────────────────────────────────────────────────────
def example_gmsk_spectrum():
    """Compare GMSK spectrum (Gaussian pulse) with unfiltered FSK."""
    import scipy.signal as signal

    fs = 100e6  # 100 MHz sampling
    Tb = 1/270e3  # GSM bit period ~3.7 us
    BbTb = 0.3    # GSM BT product

    # Generate random bits
    np.random.seed(42)
    N_bits = 100
    bits = 2 * (np.random.rand(N_bits) > 0.5) - 1  # ±1

    # Gaussian filter
    Bb = BbTb / Tb
    sigma = np.sqrt(np.log(2)) / (2 * np.pi * Bb)
    t_gauss = np.arange(-5*Tb, 5*Tb, 1/fs)
    h_gauss = 1/(np.sqrt(2*np.pi)*sigma) * np.exp(-t_gauss**2/(2*sigma**2))
    h_gauss /= np.sum(h_gauss)

    # Up-sample bits to sample rate
    samples_per_bit = int(Tb * fs)
    # For GMSK, the phase is integrated filtered bits
    bit_stream = np.repeat(bits, samples_per_bit)[:N_bits*samples_per_bit]
    t = np.arange(len(bit_stream)) / fs

    # Filter and integrate for GMSK phase
    filtered = signal.convolve(bit_stream, h_gauss, mode='same')
    phase_gmsk = np.cumsum(filtered) * (2*np.pi*0.5/Tb) / fs  # h=0.5

    # GMSK waveform
    fc = 10e6
    carrier = np.cos(2*np.pi*fc*t + phase_gmsk)

    # Spectrum
    f, Pxx = signal.periodogram(carrier, fs, window='hann', nfft=4096)
    # Normalize
    Pxx_dB = 10*np.log10(Pxx / np.max(Pxx) + 1e-12)

    # Unfiltered FSK
    phase_fsk = np.cumsum(bit_stream) * (2*np.pi*0.5/Tb) / fs
    fsk = np.cos(2*np.pi*fc*t + phase_fsk)
    _, Pxx_fsk = signal.periodogram(fsk, fs, window='hann', nfft=4096)
    Pxx_fsk_dB = 10*np.log10(Pxx_fsk / np.max(Pxx_fsk) + 1e-12)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot((f-fc)/1e6, Pxx_dB, 'b-', linewidth=1.5, label='GMSK (BT=0.3)')
    ax.plot((f-fc)/1e6, Pxx_fsk_dB, 'r-', alpha=0.6, linewidth=1, label='Unfiltered FSK')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-80, 5)
    ax.set_xlabel('Frequency offset (MHz)')
    ax.set_ylabel('PSD (dB)')
    ax.set_title('GMSK vs FSK Spectrum (GSM rate)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/razavi/figures/ch3_gmsk_spectrum.png', dpi=150)
    plt.close(fig)
    print("Saved: ch3_gmsk_spectrum.png")
    print()

# ──────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────
if __name__ == "__main__":
    print("="*60)
    print("Razavi Ch3 — Communication Concepts: Example Codes")
    print("="*60)
    print()

    example_qpsk_phase_mismatch()
    example_receiver_linearity()
    example_gmsk_spectrum()

    print("="*60)
    print("All Ch3 examples completed successfully.")
    print("="*60)
