#!/usr/bin/env python3
"""
Razavi RF Microelectronics, 2nd Ed. — Ch2: Basic Concepts in RF Design
Example codes: dBm/voltage, P1dB/IIP3, cascaded IP3, NF, sensitivity.

Requires: numpy, matplotlib
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import constants

# ──────────────────────────────────────────────────────
# Example 2.1 / 2.2:  dBm ↔ Peak-to-Peak Voltage
# ──────────────────────────────────────────────────────
def example_dbm_to_voltage():
    """
    Convert between dBm and peak-to-peak voltage in a Z0 system.
    Eq: Vpp^2 / (8*R) = P_mW,  P_dBm = 10*log10(P_mW)
    """
    Z0 = 50.0  # Ohm

    # Ex 2.1: 0 dBm -> Vpp
    P_dbm_0 = 0.0
    P_mW = 10**(P_dbm_0 / 10.0)
    Vpp_0 = np.sqrt(8 * Z0 * P_mW * 1e-3)
    print(f"Ex 2.1:  0 dBm in {Z0} Ω -> Vpp = {Vpp_0*1e3:.1f} mVpp")

    # Ex 2.2: GSM signal at -100 dBm
    P_dbm_gsm = -100.0
    P_mW_gsm = 10**(P_dbm_gsm / 10.0)
    Vpp_gsm_in = np.sqrt(8 * Z0 * P_mW_gsm * 1e-3)
    print(f"Ex 2.2: -100 dBm in {Z0} Ω -> Vpp = {Vpp_gsm_in*1e6:.3f} µVpp")

    # After 15 dB voltage gain
    gain_db = 15.0
    gain_linear = 10**(gain_db / 20.0)
    Vpp_gsm_out = Vpp_gsm_in * gain_linear
    print(f"        After {gain_db} dB gain -> Vpp_out = {Vpp_gsm_out*1e6:.2f} µVpp")
    print()

    return Vpp_0, Vpp_gsm_in, Vpp_gsm_out

# ──────────────────────────────────────────────────────
# Example 2.10 + 2.11:  P1dB / IIP3 relationship
# ──────────────────────────────────────────────────────
def example_p1dB_iip3():
    """
    P1dB = sqrt(0.145 * |alpha1/alpha3|)
    IIP3 = sqrt(4/3 * |alpha1/alpha3|)
    Ratio IIP3/P1dB = sqrt(4/3/0.145) ~ 9.6 dB
    """
    # Ex 2.10: LNA gain=10, P1dB=-30 dBm
    alpha1 = 10.0
    P1dB_dbm = -30.0
    Z0 = 50.0

    # Convert P1dB to peak voltage
    P1dB_mW = 10**(P1dB_dbm / 10.0)
    A_in_1dB_Vp = np.sqrt(2 * Z0 * P1dB_mW * 1e-3)  # Vp (peak), not Vpp
    # Actually from Eq: 0 dBm -> 632 mVpp = 316 mVp. Vpp^2/(8R)=P.
    # P1dB_dbm -> P_mW. Vpp = sqrt(8*R*P_mW*1e-3). Vp = Vpp/2
    Vpp_1dB = np.sqrt(8 * Z0 * P1dB_mW * 1e-3)
    A_in_1dB_Vp = Vpp_1dB / 2.0

    # alpha3 from P1dB formula: A_in_1dB = sqrt(0.145 * |alpha1/alpha3|)
    alpha3_mag = 0.145 * alpha1 / (A_in_1dB_Vp**2)

    # IIP3
    A_iip3 = np.sqrt(4.0 / 3.0 * alpha1 / alpha3_mag)
    IIP3_dbm = 20 * np.log10(A_iip3) + 10  # P(dBm) = 20*log(Vp) + 10  (for 50Ω)
    # More precisely: P(dBm) = 20*log10(Vpp/2) + 10 = 20*log10(Vp) + 10

    ratio_db = 20 * np.log10(A_iip3 / A_in_1dB_Vp)
    print(f"Ex 2.10: alpha1={alpha1}, P1dB={P1dB_dbm} dBm")
    print(f"         A_in_1dB = {A_in_1dB_Vp*1e3:.2f} mVp")
    print(f"         Computed |alpha3| = {alpha3_mag:.2f}")
    print(f"         IIP3 = {IIP3_dbm:.1f} dBm (should be -20.4 dBm)")
    print(f"         Ratio IIP3/P1dB = {ratio_db:.1f} dB (expected ~9.6 dB)")
    print()

    # Ex 2.11: signal=-80dBm, interferers=-20dBm
    # Need IM3 20dB below signal
    P_sig_dbm = -80.0
    P_int_dbm = -20.0
    delta_db = 20.0

    P_sig_mW = 10**(P_sig_dbm/10.0)
    P_int_mW = 10**(P_int_dbm/10.0)
    Vp_sig = np.sqrt(2*Z0*P_sig_mW*1e-3)
    Vp_int = np.sqrt(2*Z0*P_int_mW*1e-3)

    # alpha1 * Vp_sig = 10 * (30*alpha3/4) * Vp_int^3  (actually |alpha1*Asig| = |30/4*alpha3*Aint^3|)
    # IIP3 = sqrt(4/3 * |alpha1/alpha3|)
    # From the constraint: |alpha1*Asig| = 10^(delta_dB/20) * |3/4*alpha3*Aint^3| (wait, re-derive)
    # Ex 2.11 says: |alpha1*Asig| = |30/4 * alpha3 * Aint^3|
    # Because the IM3 at 2w1-w2 from (2.41) is 3*alpha3*A1^2*A2/4 where A1=A2=Aint (interferers)
    # With signal at Asig:
    # signal output: |alpha1*Asig|
    # IM3 output: |3/4*alpha3*Aint^3| (since A1=A2=Aint)
    # Condition: |alpha1*Asig| / |3/4*alpha3*Aint^3| = 10^(delta_dB/20)
    # So |alpha1/alpha3| = (3/4) * 10^(delta_dB/20) * Aint^3 / Asig

    # But Ex 2.11 says: 20log|alpha1*Asig| - 20 = 20log|3/4*alpha3*Aint^3|
    # So: |alpha1*Asig| = 10 * |3/4*alpha3*Aint^3|  (10 = 10^(20/20))
    #            wait, 20dB means 10x in voltage.
    # Actually: 20log|alpha1*Asig| - 20dB = 20log|3/4*alpha3*Aint^3|
    # So: 20log|alpha1*Asig| = 20log(10*|3/4*alpha3*Aint^3|)
    # |alpha1*Asig| = 10 * |3/4*alpha3*Aint^3| -> |alpha1/alpha3| = 10 * (3/4) * Aint^3 / Asig
    # Hmm but the book says |alpha1*Asig| = |30/4*alpha3*Aint^3| which is 7.5 * alpha3 * Aint^3
    # Let me just use the book's equation: |alpha1*Asig| = |30/4 * alpha3 * Aint^3|

    ratio_alpha = (30.0/4.0) * Vp_int**3 / Vp_sig
    A_iip3_calc = np.sqrt(4.0/3.0 * ratio_alpha)
    IIP3_calc_dbm = 20*np.log10(A_iip3_calc) + 10
    print(f"Ex 2.11: P_sig={P_sig_dbm} dBm, P_int={P_int_dbm} dBm, IM3 requirement: {delta_db} dB below signal")
    print(f"         Computed IIP3 = {IIP3_calc_dbm:.1f} dBm (book: +15.2 dBm)")
    print()

    # Plot: fundamental and IM3 vs input power
    A_in_range = np.logspace(np.log10(A_in_1dB_Vp/1000), np.log10(A_in_1dB_Vp*3), 200)
    fund_out = alpha1 * A_in_range
    im3_out = (3.0/4.0) * alpha3_mag * A_in_range**3

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.loglog(A_in_range, fund_out, 'b-', label='Fundamental (slope 1)')
    ax.loglog(A_in_range, im3_out, 'r-', label='IM3 (slope 3)')
    ax.axvline(A_in_1dB_Vp, color='gray', linestyle='--', alpha=0.5, label=f'P1dB = {P1dB_dbm:.0f} dBm')
    ax.axvline(A_iip3, color='green', linestyle='--', alpha=0.5, label=f'IIP3 = {IIP3_dbm:.1f} dBm')

    ax.set_xlabel('Input Amplitude (V, peak)')
    ax.set_ylabel('Output Amplitude (V, peak)')
    ax.set_title('P1dB and IIP3 for a 3rd-Order Nonlinear System')
    ax.legend()
    ax.grid(True, which='both', alpha=0.3)
    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/razavi/figures/ch2_p1db_iip3.png', dpi=150)
    plt.close(fig)
    print("Saved: ch2_p1db_iip3.png")
    print()

    return alpha3_mag, A_iip3

# ──────────────────────────────────────────────────────
# Example 2.13: Cascaded IP3 (LNA + Mixer)
# ──────────────────────────────────────────────────────
def example_cascaded_ip3():
    """
    LNA: IIP3=-10 dBm, gain=20 dB
    Mixer: IIP3=+4 dBm
    Which limits more?
    Eq: 1/A_IP3^2 = 1/A_IP3_1^2 + alpha1^2/A_IP3_2^2
    """
    Z0 = 50.0
    # LNA
    IIP3_1_dbm = -10.0
    gain_1_db = 20.0
    alpha1 = 10**(gain_1_db / 20.0)

    # Mixer
    IIP3_2_dbm = 4.0

    # Convert dBm to Vp
    def dbm_to_vp(dbm):
        PmW = 10**(dbm/10.0)
        Vpp = np.sqrt(8*Z0*PmW*1e-3)
        return Vpp/2.0

    A_iip3_1 = dbm_to_vp(IIP3_1_dbm)
    A_iip3_2 = dbm_to_vp(IIP3_2_dbm)

    # Scaled IIP3 of mixer referred to input
    A_iip3_2_scaled = A_iip3_2 / alpha1
    IIP3_2_scaled_dbm = 20*np.log10(A_iip3_2_scaled) + 10

    print(f"Ex 2.13: Cascaded IP3 analysis")
    print(f"         LNA:  IIP3 = {IIP3_1_dbm} dBm, gain = {gain_1_db} dB")
    print(f"         Mixer: IIP3 = {IIP3_2_dbm} dBm")
    print(f"         Mixer IIP3 referred to input: {IIP3_2_scaled_dbm:.1f} dBm")
    print(f"         → Mixer limits IP3 more (lower referred IIP3)")
    print()

    # Overall
    A_iip3_tot = 1 / np.sqrt(1/A_iip3_1**2 + alpha1**2/A_iip3_2**2)
    IIP3_tot_dbm = 20*np.log10(A_iip3_tot) + 10
    print(f"         Overall IIP3 = {IIP3_tot_dbm:.1f} dBm")
    print()

    return IIP3_tot_dbm

# ──────────────────────────────────────────────────────
# Example 2.21: NF of CS stage
# ──────────────────────────────────────────────────────
def example_cs_nf():
    """
    CS stage (Fig 2.50): NF = 1 + gamma/(gm*RS)
    """
    gamma = 2.0/3.0  # long-channel excess noise factor
    gm_values = np.logspace(-3, 0, 100)  # 1 mS to 1 S
    RS = 50.0

    NF_linear = 1 + gamma / (gm_values * RS)
    NF_db = 10 * np.log10(NF_linear)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogx(gm_values, NF_db, 'b-', linewidth=2)
    ax.axhline(3, color='red', linestyle='--', alpha=0.5, label='3 dB floor')
    ax.set_xlabel('$g_m$ (S)')
    ax.set_ylabel('NF (dB)')
    ax.set_title('CS Stage NF vs Transconductance ($R_S=50\\,\\Omega$)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/razavi/figures/ch2_cs_nf.png', dpi=150)
    plt.close(fig)
    print("Saved: ch2_cs_nf.png")

    # Key point: NF improves as gm increases
    print(f"Ex 2.21: At gm=10mS -> NF = {10*np.log10(1+gamma/(0.01*50)):.2f} dB")
    print(f"         At gm=100mS -> NF = {10*np.log10(1+gamma/(0.1*50)):.2f} dB")
    print()

# ──────────────────────────────────────────────────────
# Example 2.25: Sensitivity comparison GSM vs WLAN
# ──────────────────────────────────────────────────────
def example_sensitivity():
    """
    P_sen = -174 dBm/Hz + NF + 10*log10(B) + SNR_min
    """
    NF = 7.0  # dB

    # GSM
    B_gsm = 200e3  # 200 kHz
    SNR_min_gsm = 12.0  # dB
    P_sen_gsm = -174 + NF + 10*np.log10(B_gsm) + SNR_min_gsm
    print(f"Ex 2.25: Sensitivity comparison (NF = {NF} dB)")
    print(f"         GSM:   B={B_gsm/1e3:.0f} kHz, SNR_min={SNR_min_gsm} dB")
    print(f"                P_sen = {P_sen_gsm:.0f} dBm")

    # WLAN
    B_wlan = 20e6  # 20 MHz
    SNR_min_wlan = 23.0  # dB
    P_sen_wlan = -174 + NF + 10*np.log10(B_wlan) + SNR_min_wlan
    print(f"         WLAN:  B={B_wlan/1e6:.0f} MHz, SNR_min={SNR_min_wlan} dB")
    print(f"                P_sen = {P_sen_wlan:.0f} dBm")
    print(f"         Note: WLAN has 200x data rate of GSM, so higher P_sen acceptable")
    print()

# ──────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────
if __name__ == "__main__":
    print("="*60)
    print("Razavi Ch2 — RF Basic Concepts: Example Codes")
    print("="*60)
    print()

    example_dbm_to_voltage()
    alpha3_mag, A_iip3 = example_p1dB_iip3()
    example_cascaded_ip3()
    example_cs_nf()
    example_sensitivity()

    print("="*60)
    print("All Ch2 examples completed successfully.")
    print("="*60)
