#!/usr/bin/env python3
"""
Razavi RF Microelectronics, 2nd Ed. — Ch13: Transceiver Design Example
Receiver link budget calculation.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ──────────────────────────────────────────────────────
# Receiver Link Budget
# ──────────────────────────────────────────────────────
def example_link_budget():
    """Complete receiver link budget calculation."""
    stages = [
        ("BPF", -1.5, 1.5, 100, 100),
        ("LNA", 18, 2.5, -10, -20),
        ("Mixer", 8, 12, 5, -5),
        ("VGA", 40, 20, 10, 0),
    ]

    # Cascaded calculation
    G_lin = 1.0
    F_lin = 1.0
    IIP3_lin_inv = 0.0
    P1dB_lin_inv = 0.0

    print("="*65)
    print(f"{'Stage':<12} {'Gain(dB)':<10} {'NF(dB)':<10} {'IIP3(dBm)':<12} {'P1dB(dBm)':<12}")
    print("="*65)

    results = []
    for name, gain, nf, iip3, p1db in stages:
        g_lin = 10**(gain/10)
        f_lin = 10**(nf/10)
        # Cascaded Friis
        F_casc = F_lin + (f_lin - 1) / G_lin
        # Cascaded IIP3
        iip3_lin = 10**(iip3/10)
        IIP3_casc_inv = IIP3_lin_inv + 1/(G_lin * iip3_lin)
        # Cascaded P1dB (approximate)
        p1db_lin = 10**(p1db/10)
        P1dB_casc_inv = P1dB_lin_inv + 1/(G_lin * p1db_lin)

        NF_casc = 10 * np.log10(F_casc)
        IIP3_casc = 10 * np.log10(1/IIP3_casc_inv) if IIP3_casc_inv > 0 else 100
        P1dB_casc = 10 * np.log10(1/P1dB_casc_inv) if P1dB_casc_inv > 0 else 100

        results.append((name, gain, NF_casc, IIP3_casc, P1dB_casc))
        print(f"{name:<12} {gain:<10.1f} {NF_casc:<10.2f} {IIP3_casc:<12.1f} {P1dB_casc:<12.1f}")

        # Update for next stage
        G_lin *= g_lin
        F_lin = F_casc
        IIP3_lin_inv = IIP3_casc_inv
        P1dB_lin_inv = P1dB_casc_inv

    print("="*65)
    print()

    # Sensitivity
    NF_final = results[-1][2]
    B = 20e6
    for rate, SNR_min, mod in [(6e6, 7, "BPSK"), (54e6, 27, "64QAM")]:
        P_sen = -174 + NF_final + 10*np.log10(B) + SNR_min
        print(f"Sensitivity ({mod}, {rate/1e6:.0f} Mb/s): {P_sen:.1f} dBm")

    # SFDR
    IIP3_final = results[-1][3]
    P_noise_floor = -174 + NF_final + 10*np.log10(B)
    SFDR = (2*(IIP3_final - P_noise_floor))/3 - 7  # for BPSK
    print(f"  Noise floor: {P_noise_floor:.1f} dBm")
    print(f"  SFDR: {SFDR:.0f} dB")
    print()

    # Plot: cumulative gain along the chain
    fig, ax1 = plt.subplots(figsize=(8, 5))
    names = [s[0] for s in results]
    cum_gain = [r[1] for r in results]
    cum_nf = [r[2] for r in results]

    x = np.arange(len(names))
    ax1.bar(x - 0.2, cum_gain, 0.35, label='Cumulative Gain (dB)', color='blue', alpha=0.7)
    ax1.set_ylabel('Gain (dB)', color='blue')

    ax2 = ax1.twinx()
    ax2.plot(x, cum_nf, 'ro-', linewidth=2, label='Cascaded NF (dB)')
    ax2.set_ylabel('NF (dB)', color='red')

    ax1.set_xticks(x)
    ax1.set_xticklabels(names)
    ax1.set_title('Receiver Link Budget: Gain and NF Along Chain')
    ax1.grid(True, alpha=0.3, axis='y')
    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/razavi/figures/ch13_link_budget.png', dpi=150)
    plt.close(fig)
    print("Saved: ch13_link_budget.png")
    print()

# ──────────────────────────────────────────────────────
# OFDM PAR visualization
# ──────────────────────────────────────────────────────
def example_ofdm_par():
    """Show PAR of OFDM signal."""
    N_sub = 52  # 802.11a
    fs = 80e6
    T_sym = 3.2e-6  # 80 samples
    num_sym = 100

    # Generate random 64QAM symbols
    np.random.seed(42)
    symbols = (2*np.random.randint(0, 2, (N_sub, num_sym)) - 1) + \
              1j * (2*np.random.randint(0, 2, (N_sub, num_sym)) - 1)
    symbols *= np.sqrt(1/10)  # normalize (avg power = 1 for 64QAM)

    # IFFT
    ofdm_signal = np.fft.ifft(symbols, n=80, axis=0)
    signal_real = np.real(ofdm_signal).flatten()

    # PAR
    peak_power = np.max(np.abs(signal_real)**2)
    avg_power = np.mean(np.abs(signal_real)**2)
    PAR = 10 * np.log10(peak_power / avg_power)

    print(f"Example: OFDM PAR for {N_sub} subcarriers")
    print(f"  PAR (measured) = {PAR:.1f} dB")
    print(f"  Theoretical ≈ 10*log10(2*ln({N_sub})) = {10*np.log10(2*np.log(N_sub)):.1f} dB")

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(np.abs(signal_real[:800])**2 / avg_power, 'b-', linewidth=0.8)
    ax.axhline(peak_power/avg_power, color='r', linestyle='--', alpha=0.5, label=f'Peak = {PAR:.1f} dB')
    ax.set_xlabel('Sample Index')
    ax.set_ylabel('Normalized Power')
    ax.set_title(f'OFDM Envelope ({N_sub} subcarriers, 64QAM)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/razavi/figures/ch13_ofdm_par.png', dpi=150)
    plt.close(fig)
    print("Saved: ch13_ofdm_par.png")
    print()

# ──────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────
if __name__ == "__main__":
    print("="*60)
    print("Razavi Ch13 — Transceiver Design Example")
    print("="*60)
    print()

    example_link_budget()
    example_ofdm_par()

    print("="*60)
    print("All Ch13 examples completed successfully.")
    print("="*60)
