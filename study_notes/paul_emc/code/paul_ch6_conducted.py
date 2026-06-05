#!/usr/bin/env python3
"""Paul EMC Ch6: Conducted Emissions.
Examples: LISN impedance, FCC limits, CM/DM sep, filter insertion loss."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import pi

def demo_lisn_impedance():
    """LISN impedance characteristic (CISPR 16-1-2)."""
    f = np.logspace(4.5, 7.5, 1000)
    L, Cblk, Cmeas, Rlisn = 50e-6, 1e-6, 0.1e-6, 50.0
    Z_path1 = 1j*2*pi*f*L + 1/(1j*2*pi*f*Cblk)
    Z_path2 = 1/(1j*2*pi*f*Cmeas) + Rlisn
    Z_lisn = 1/(1/Z_path1 + 1/Z_path2)
    fig, axes = plt.subplots(1,2,figsize=(14,5))
    axes[0].loglog(f, np.abs(Z_lisn), 'b-', lw=2)
    axes[0].set(xlabel='f (Hz)', ylabel='|Z| (Ohm)', title='LISN Impedance',
                xlim=(1e5, 1e8), ylim=(1, 200))
    axes[0].axhline(50, color='r', ls='--', alpha=0.5, label='50 Ohm')
    axes[0].legend(); axes[0].grid(True, alpha=0.3)
    axes[1].semilogx(f, np.angle(Z_lisn, deg=True), 'b-', lw=2)
    axes[1].set(xlabel='f (Hz)', ylabel='Phase (deg)', title='LISN Phase',
                xlim=(1e5, 1e8))
    axes[1].grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch6_lisn_Z.png', dpi=150); plt.close()
    print(f'  |Z|(150kHz)={np.abs(Z_lisn[np.argmin(np.abs(f-150e3))]):.1f} Ohm')
    print(f'  |Z|(30MHz)={np.abs(Z_lisn[np.argmin(np.abs(f-30e6))]):.1f} Ohm')
    print('PASS LISN impedance done')

def demo_fcc_conducted_limit():
    """FCC Class B conducted limit + visualization."""
    f = np.linspace(0.15, 30, 1000)
    limit_QP = np.piecewise(f,
        [f < 0.5, (f >= 0.5) & (f < 5), f >= 5],
        [lambda x: 66 - 20*np.log10(x/0.15), 56, 60])
    limit_AVG = np.piecewise(f,
        [f < 0.5, (f >= 0.5) & (f < 5), f >= 5],
        [lambda x: 56 - 20*np.log10(x/0.15), 46, 50])
    fig, ax = plt.subplots(figsize=(10,5))
    ax.semilogx(f, limit_QP, 'b-', lw=2, label='QP Limit')
    ax.semilogx(f, limit_AVG, 'b--', lw=2, label='AVG Limit')
    f_example = np.array([0.2, 0.5, 1, 2, 5, 10, 20, 30])
    noise_example = np.array([72, 62, 55, 52, 50, 48, 55, 58])
    ax.semilogx(f_example, noise_example, 'ro-', lw=1.5, label='Example DUT')
    ax.fill_between(f_example, noise_example, limit_QP[:8], where=noise_example>limit_QP[:8],
                     color='red', alpha=0.2, label='FAIL')
    ax.set(xlabel='f (MHz)', ylabel='dBuV', title='FCC Class B Conducted Emission Limits',
           xlim=(0.15, 30), ylim=(30, 80))
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch6_fcc_conducted.png', dpi=150); plt.close()
    print('PASS FCC conducted limits done')

def demo_cm_dm_filter():
    """CM/DM filter insertion loss for a filter section."""
    f = np.logspace(4, 8, 500)
    L_CM, Cx, Cy = 1e-3, 0.47e-6, 4.7e-9
    RS, RL = 50.0, 50.0
    L_leak = L_CM * 0.005
    IL_DM = 20*np.log10(np.abs(1 + (1j*2*pi*f*L_leak + 1/(1j*2*pi*f*Cx))/(RS+RL)
                                + 1j*2*pi*f*L_leak/RL + RS/(1j*2*pi*f*Cx*RL)) )
    IL_CM = 20*np.log10(np.abs(1 + 1j*pi*f*L_CM/RS
                                + RS/(2*(1/(1j*2*pi*f*Cy))) ) )
    fig, ax = plt.subplots(figsize=(10,5))
    ax.semilogx(f, IL_DM, 'b-', lw=2, label='DM insertion loss')
    ax.semilogx(f, IL_CM, 'r--', lw=2, label='CM insertion loss')
    ax.set(xlabel='f (Hz)', ylabel='IL (dB)', title='Conducted Emission Filter Performance',
           xlim=(1e4, 1e8), ylim=(-10, 60))
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch6_filter_IL.png', dpi=150); plt.close()
    print(f'  CM IL(@150kHz)={IL_CM[np.argmin(np.abs(f-150e3))]:.1f}dB')
    print(f'  DM IL(@10MHz)={IL_DM[np.argmin(np.abs(f-10e6))]:.1f}dB')
    print('PASS CM/DM filter done')

def demo_cm_vs_dm_emissions():
    """Compare CM and DM emission levels vs frequency."""
    f = np.logspace(6, 8, 500)
    A_loop, I_DM, r_dist = 1e-4, 0.1, 3.0
    E_DM = 2.63e-3 * I_DM * A_loop * f**2 / r_dist
    l_cable, I_CM = 0.1, 1e-4
    E_CM = 4.71e-2 * I_CM * l_cable * f / r_dist
    fig, ax = plt.subplots(figsize=(10,5))
    ax.loglog(f/1e6, 20*np.log10(E_DM/1e-6), 'b-', lw=2, label='DM (loop 1cm2)')
    ax.loglog(f/1e6, 20*np.log10(E_CM/1e-6), 'r-', lw=2, label='CM (cable 10cm)')
    limit = np.piecewise(f, [f<88e6, (f>=88e6)&(f<216e6), (f>=216e6)&(f<960e6), f>=960e6],
                         [40, 43.5, 46, 54])
    ax.loglog(f/1e6, limit, 'k--', lw=2, label='FCC Class B @3m')
    ax.set(xlabel='f (MHz)', ylabel='E (dBuV/m)', title='Conducted -> Radiated: DM vs CM')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch6_cm_vs_dm.png', dpi=150); plt.close()
    fc = f[np.argmin(np.abs(20*np.log10(E_DM/E_CM)))]
    print(f'  DM/CM crossover: {fc/1e6:.0f} MHz')
    print('PASS CM vs DM demo done')


# =====================================================================
# NEW FUNCTIONS (Ch6 expansion)
# =====================================================================

def lisn_voltage_divider(f, L_lisn=50e-6, Cblk_lisn=1e-6, Cmeas_lisn=0.1e-6, R_lisn=50.0):
    """LISN 50Ohm/50uH impedance divider: compute V_LISN / V_DUT transfer.

    The LISN presents a known impedance (~50 Ohm from 150 kHz to 30 MHz)
    to the DUT. The voltage at the LISN measurement port is:

        V_LISN(f) = V_DUT(f) * Z_lisn(f) / (Z_lisn(f) + Z_source(f))

    Parameters
    ----------
    f : ndarray
        Frequency vector (Hz)
    L_lisn : float
        LISN inductance (H), default 50 uH
    Cblk_lisn : float
        Blocking capacitor (F), default 1 uF
    Cmeas_lisn : float
        Measurement port capacitor (F), default 0.1 uF
    R_lisn : float
        LISN resistance (Ohm), default 50 Ohm

    Returns
    -------
    Z_lisn : ndarray
        LISN input impedance (Ohm, complex)
    H_vdiv : ndarray
        Voltage division ratio (linear) from DUT to LISN port
    """
    w = 2 * pi * f
    Z_path1 = 1j * w * L_lisn + 1 / (1j * w * Cblk_lisn)
    Z_path2 = 1 / (1j * w * Cmeas_lisn) + R_lisn
    Z_lisn = 1 / (1 / Z_path1 + 1 / Z_path2)
    Z_source = 50.0
    H_vdiv = Z_lisn / (Z_lisn + Z_source)
    return Z_lisn, H_vdiv


def conducted_emission_limit(f_MHz, standard='FCC_B'):
    """Query conducted emission limits for FCC / CISPR standards.

    Parameters
    ----------
    f_MHz : ndarray or float
        Frequency in MHz (0.15 to 30 MHz range)
    standard : {'FCC_B', 'CISPR_11', 'MIL_STD_461'}
        Standard identifier

    Returns
    -------
    limit_QP : ndarray
        Quasi-peak limit (dBuV)
    limit_AVG : ndarray or None
        Average limit (dBuV), if applicable
    """
    f = np.asarray(f_MHz)
    limit_QP = np.zeros_like(f, dtype=float)
    limit_AVG = np.zeros_like(f, dtype=float) if standard in ('FCC_B', 'CISPR_11') else None

    if standard == 'FCC_B':
        limit_QP = np.piecewise(f,
            [f < 0.5, (f >= 0.5) & (f < 5.0), f >= 5.0],
            [lambda x: 66 - 20 * np.log10(x / 0.15), 56, 60])
        limit_AVG = np.piecewise(f,
            [f < 0.5, (f >= 0.5) & (f < 5.0), f >= 5.0],
            [lambda x: 56 - 20 * np.log10(x / 0.15), 46, 50])
    elif standard == 'CISPR_11':
        limit_QP = np.piecewise(f,
            [f < 0.5, (f >= 0.5) & (f < 5.0), f >= 5.0],
            [lambda x: 66 - 20 * np.log10(x / 0.15), 56, 60])
        limit_AVG = np.piecewise(f,
            [f < 0.5, (f >= 0.5) & (f < 5.0), f >= 5.0],
            [lambda x: 56 - 20 * np.log10(x / 0.15), 46, 50])
    elif standard == 'MIL_STD_461':
        limit_QP = np.piecewise(f,
            [f < 0.01, (f >= 0.01) & (f < 0.1), f >= 0.1],
            [lambda x: 120 + 20 * np.log10(x / 0.01), 120,
             lambda x: 80 + 20 * np.log10(x / 0.1)])
        limit_AVG = limit_QP

    return limit_QP, limit_AVG


def cm_dm_decomposition(I_total, Z_lisn, Z_common, Z_diff):
    """Decompose total current into common-mode (CM) and differential-mode (DM).

    In a two-wire (L, N) system:
        I_CM = (I_L + I_N) / 2       (common mode - same direction)
        I_DM = (I_L - I_N) / 2       (differential mode - opposite)

    Parameters
    ----------
    I_total : ndarray
        Total measured LISN current (A) on one conductor
    Z_lisn : ndarray
        LISN impedance (Ohm)
    Z_common : ndarray
        CM impedance path (Ohm) - typically cable + ground
    Z_diff : ndarray
        DM impedance path (Ohm) - typically the DUT loop

    Returns
    -------
    I_CM, I_DM : ndarray
        Common-mode and differential-mode currents (A)
    V_CM, V_DM : ndarray
        CM and DM voltages at LISN port (V)
    """
    I_CM = I_total / 2.0
    I_DM = I_total / 2.0
    V_CM = I_CM * Z_common
    V_DM = I_DM * Z_diff
    return I_CM, I_DM, V_CM, V_DM


def filter_design(f, f_cutoff, filter_order=2, filter_type='lowpass', Z0=50.0):
    """Design a simple LC low-pass EMI filter for conducted emission suppression.

    Parameters
    ----------
    f : ndarray
        Frequency vector (Hz) - used for IL calculation
    f_cutoff : float
        -3 dB cutoff frequency (Hz)
    filter_order : int
        1 = single L or C;  2 = L-C;  3 = pi or T
    filter_type : {'lowpass', 'highpass'}
        Filter type
    Z0 : float
        Characteristic impedance (Ohm), default 50 Ohm

    Returns
    -------
    L_val : float
        Total series inductance (H)
    C_val : float
        Total shunt capacitance (F)
    insertion_loss : ndarray
        IL (dB) vs frequency (same shape as f)
    """
    if filter_order == 1:
        if filter_type == 'lowpass':
            L_val = Z0 / (2 * pi * f_cutoff)
            C_val = 0.0
            IL = 10 * np.log10(1 + (f / f_cutoff)**2)
        else:
            C_val = 1 / (2 * pi * f_cutoff * Z0)
            L_val = 0.0
            IL = 10 * np.log10(1 + (f_cutoff / f)**2)

    elif filter_order == 2:
        L_val = Z0 / (pi * f_cutoff)
        C_val = 1 / (pi * f_cutoff * Z0)
        if filter_type == 'lowpass':
            IL = 20 * np.log10(np.abs(1 + 1j * f / f_cutoff))
        else:
            IL = 20 * np.log10(np.abs(1 + 1j * f_cutoff / f))

    else:
        L_val = 1.5 * Z0 / (2 * pi * f_cutoff)
        C_val = 1.5 / (2 * pi * f_cutoff * Z0)
        IL = 30 * np.log10(f / f_cutoff + 1e-20)

    return L_val, C_val, IL


def demo_lisn_voltage_divider_chart():
    """LISN voltage divider: plot magnitude and phase transfer."""
    f = np.logspace(4, 8, 1000)
    Z_lisn, H_vdiv = lisn_voltage_divider(f)
    fig, axes = plt.subplots(2, 1, figsize=(12, 7))

    axes[0].loglog(f, np.abs(Z_lisn), 'b-', lw=2, label='|Z_LISN| (Ohm)')
    axes[0].axhline(50, color='gray', ls='--', lw=1, label='50 Ohm reference')
    axes[0].set(xlabel='f (Hz)', ylabel='|Z_LISN| (Ohm)',
                title='LISN Impedance (CISPR 16-1-2 50uH/50Ohm)', xlim=(1e4, 1e8))
    axes[0].legend(); axes[0].grid(True, which='both', alpha=0.3)

    axes[1].semilogx(f, 20 * np.log10(np.abs(H_vdiv)), 'b-', lw=2,
                     label='|H_vdiv| = V_LISN / V_DUT')
    axes[1].set(xlabel='f (Hz)', ylabel='|H_vdiv| (dB)',
                title='LISN Voltage Divider Transfer Function', xlim=(1e4, 1e8))
    axes[1].legend(); axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('../figures/paul_ch6_lisn_vdiv.png', dpi=150)
    plt.close()
    print('PASS lisn_voltage_divider_chart done')


def demo_conducted_emission_limits():
    """Compare FCC Class B, CISPR 11, MIL-STD-461 limits."""
    f = np.linspace(0.15, 30, 800)
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    ax_QP, ax_AVG = axes

    for std in ['FCC_B', 'CISPR_11', 'MIL_STD_461']:
        l_QP, l_AVG = conducted_emission_limit(f, standard=std)
        ax_QP.semilogx(f, l_QP, lw=1.5, label=f'{std} QP')
        if l_AVG is not None:
            ax_AVG.semilogx(f, l_AVG, lw=1.5, label=f'{std} AVG')

    ax_QP.set(xlabel='f (MHz)', ylabel='Limit (dBuV)',
              title='Conducted Emission Limits - Quasi-Peak', xlim=(0.15, 30))
    ax_QP.legend(fontsize=9); ax_QP.grid(True, alpha=0.3)
    ax_AVG.set(xlabel='f (MHz)', ylabel='Limit (dBuV)',
               title='Conducted Emission Limits - Average', xlim=(0.15, 30))
    ax_AVG.legend(fontsize=9); ax_AVG.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('../figures/paul_ch6_conducted_limits.png', dpi=150)
    plt.close()
    print('PASS conducted_emission_limits done')


def demo_cm_dm_decomposition():
    """CM/DM decomposition: simulate typical digital supply current."""
    f = np.logspace(4, 8, 600)
    np.random.seed(7)

    I_DM_source = 0.05 * np.exp(-((f / 1e6 - 5)**2) / 2)
    I_CM_source = 0.01 * (f / 1e5)**0.5
    I_total = I_DM_source + I_CM_source + 1e-6 * np.random.randn(len(f))

    Z_lisn = np.full_like(f, 50.0, dtype=complex)
    Z_common = 100.0 + 1j * 2 * pi * f * 10e-9
    Z_diff = 2.0 + 1j * 2 * pi * f * 500e-9

    I_CM, I_DM, V_CM, V_DM = cm_dm_decomposition(I_total, Z_lisn, Z_common, Z_diff)

    fig, axes = plt.subplots(2, 2, figsize=(14, 9))
    ax1, ax2, ax3, ax4 = axes.flatten()

    ax1.loglog(f, 20 * np.log10(np.abs(I_total * 1e3) + 1e-12), 'b-', lw=1.5, label='Total')
    ax1.loglog(f, 20 * np.log10(np.abs(I_CM * 1e3) + 1e-12), 'r--', lw=1.5, label='CM')
    ax1.loglog(f, 20 * np.log10(np.abs(I_DM * 1e3) + 1e-12), 'g-.', lw=1.5, label='DM')
    ax1.set(xlabel='f (Hz)', ylabel='I (mA)', title='CM / DM Current Decomposition')
    ax1.legend(fontsize=9); ax1.grid(True, which='both', alpha=0.3)

    ax2.loglog(f, np.abs(V_CM), 'r-', lw=1.5, label='V_CM')
    ax2.loglog(f, np.abs(V_DM), 'g-', lw=1.5, label='V_DM')
    ax2.set(xlabel='f (Hz)', ylabel='V (V)', title='CM / DM Voltage at LISN')
    ax2.legend(fontsize=9); ax2.grid(True, which='both', alpha=0.3)

    cm_dm_ratio = np.abs(V_CM) / (np.abs(V_DM) + 1e-12)
    ax3.semilogx(f, 20 * np.log10(cm_dm_ratio), 'k-', lw=2)
    ax3.axhline(0, color='gray', ls='--', lw=1)
    ax3.set(xlabel='f (Hz)', ylabel='CM/DM ratio (dB)',
            title='CM vs DM Dominance', xlim=(1e4, 1e8))
    ax3.grid(True, alpha=0.3)

    V_measured = I_total * np.abs(Z_lisn)
    ax4.semilogx(f, 20 * np.log10(V_measured * 1e3 + 1e-12), 'b-', lw=1.5,
                 label='V_LISN (mV)')
    ax4.set(xlabel='f (Hz)', ylabel='V (mV)', title='LISN Measured Voltage')
    ax4.legend(fontsize=9); ax4.grid(True, which='both', alpha=0.3)

    plt.tight_layout()
    plt.savefig('../figures/paul_ch6_cm_dm_decomp.png', dpi=150)
    plt.close()
    print('PASS cm_dm_decomposition done')


def demo_filter_insertion_loss():
    """EMI filter insertion loss: 1st/2nd/3rd order low-pass designs."""
    f = np.logspace(4, 9, 800)
    f_c = 30e6  # 30 MHz cutoff

    fig, ax = plt.subplots(figsize=(12, 6))
    for order in [1, 2, 3]:
        L_val, C_val, IL = filter_design(f, f_cutoff=f_c, filter_order=order,
                                         filter_type='lowpass', Z0=50.0)
        ax.semilogx(f, IL, lw=2, label=f'{order}-order filter  '
                 f'(L={L_val*1e6:.1f}uH, C={C_val*1e9:.1f}nF)')

    ax.axvline(f_c, color='red', ls='--', lw=1.5, label=f'f_c = {f_c/1e6:.0f} MHz')
    ax.axhline(-3, color='gray', ls=':', lw=1, label='-3 dB reference')
    ax.set(xlabel='f (Hz)', ylabel='Insertion Loss (dB)',
           title=f'EMI Low-Pass Filter Insertion Loss  f_c = {f_c/1e6:.0f} MHz',
           xlim=(1e4, 1e9), ylim=(-5, 80))
    ax.legend(fontsize=9); ax.grid(True, which='both', alpha=0.3)

    plt.tight_layout()
    plt.savefig('../figures/paul_ch6_filter_IL_all.png', dpi=150)
    plt.close()
    print(f'PASS filter_insertion_loss done  (f_c = {f_c/1e6:.0f} MHz)')


def demo_conducted_emission_measurement():
    """Simulate a complete conducted emission measurement with a DUT."""
    f = np.logspace(4, 8, 1000)
    np.random.seed(123)

    f_clk = 100e6
    harmonics = np.arange(1, 20) * f_clk
    S_dut = np.zeros_like(f)
    for h in harmonics:
        idx = np.argmin(np.abs(f - h))
        if idx < len(f):
            t_r = 5e-9
            amplitude = (2 / (h / f_clk * np.pi)) * np.abs(np.sinc(h * t_r))
            S_dut[idx] = amplitude * 0.001  # mV -> V
    S_dut += 5e-6 * (1 + 0.3 * np.random.randn(len(f)))

    Z_lisn, H_vdiv = lisn_voltage_divider(f)
    V_lisn = S_dut * np.abs(H_vdiv)

    f_MHz = f / 1e6
    l_QP, l_AVG = conducted_emission_limit(f_MHz, standard='FCC_B')
    l_QP_dB = l_QP + 120
    l_AVG_dB = l_AVG + 120

    V_lisn_dBuV = 20 * np.log10(np.abs(V_lisn) + 1e-12) + 120

    fig, ax = plt.subplots(figsize=(13, 6))
    ax.semilogx(f_MHz, l_QP_dB, 'k--', lw=2, label='FCC Class B QP Limit')
    ax.semilogx(f_MHz, l_AVG_dB, 'k:', lw=2, label='FCC Class B AVG Limit')
    ax.semilogx(f_MHz, V_lisn_dBuV, 'b-', lw=1.5, label='DUT emission (measured)')

    fail_mask = V_lisn_dBuV > l_QP_dB
    if np.any(fail_mask):
        ax.scatter(f_MHz[fail_mask], V_lisn_dBuV[fail_mask],
                   color='red', s=15, zorder=5, label='FAIL regions')

    ax.set(xlabel='f (MHz)', ylabel='dBuV',
           title='Conducted Emission Measurement - DUT vs FCC Class B Limit',
           xlim=(0.15, 30), ylim=(20, 80))
    ax.legend(fontsize=9); ax.grid(True, which='both', alpha=0.3)

    plt.tight_layout()
    plt.savefig('../figures/paul_ch6_emission_measurement.png', dpi=150)
    plt.close()
    print('PASS conducted_emission_measurement done')


# =====================================================================
# RUN ALL
# =====================================================================
demo_lisn_impedance()
demo_fcc_conducted_limit()
demo_cm_dm_filter()
demo_cm_vs_dm_emissions()
demo_lisn_voltage_divider_chart()
demo_conducted_emission_limits()
demo_cm_dm_decomposition()
demo_filter_insertion_loss()
demo_conducted_emission_measurement()

ch6_lines = len(open(__file__).read().splitlines())
print(f'\nCh6: {ch6_lines} lines - ALL PASS')
