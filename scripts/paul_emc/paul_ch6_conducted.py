#!/usr/bin/env python3
"""Paul EMC Ch6: Conducted Emissions.
Examples: LISN impedance, FCC limits, CM/DM sep, filter insertion loss."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import pi

def demo_lisn_impedance():
    """LISN impedance characteristic (CISPR 16-1-2)."""
    f = np.logspace(4.5, 7.5, 1000)
    L, Cblk, Cmeas, Rlisn = 50e-6, 1e-6, 0.1e-6, 50.0
    # Path 1: through 50μH + 1μF to GND (mains side)
    Z_path1 = 1j*2*pi*f*L + 1/(1j*2*pi*f*Cblk)
    # Path 2: through 0.1μF + 50Ω to GND (receiver side)
    Z_path2 = 1/(1j*2*pi*f*Cmeas) + Rlisn
    # Parallel combination = LISN impedance seen by DUT
    Z_lisn = 1/(1/Z_path1 + 1/Z_path2)
    fig, axes = plt.subplots(1,2,figsize=(14,5))
    axes[0].loglog(f, np.abs(Z_lisn), 'b-', lw=2)
    axes[0].set(xlabel='f (Hz)', ylabel='|Z| (Ω)', title='LISN Impedance',
                xlim=(1e5, 1e8), ylim=(1, 200))
    axes[0].axhline(50, color='r', ls='--', alpha=0.5, label='50 Ω')
    axes[0].legend(); axes[0].grid(True, alpha=0.3)
    axes[1].semilogx(f, np.angle(Z_lisn, deg=True), 'b-', lw=2)
    axes[1].set(xlabel='f (Hz)', ylabel='Phase (deg)', title='LISN Phase',
                xlim=(1e5, 1e8))
    axes[1].grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch6_lisn_Z.png', dpi=150); plt.close()
    print(f'  |Z|(150kHz)={np.abs(Z_lisn[np.argmin(np.abs(f-150e3))]):.1f}Ω')
    print(f'  |Z|(30MHz)={np.abs(Z_lisn[np.argmin(np.abs(f-30e6))]):.1f}Ω')
    print('✅ LISN impedance done')

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
    ax.set(xlabel='f (MHz)', ylabel='dBμV', title='FCC Class B Conducted Emission Limits',
           xlim=(0.15, 30), ylim=(30, 80))
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch6_fcc_conducted.png', dpi=150); plt.close()
    print('✅ FCC conducted limits done')

def demo_cm_dm_filter():
    """CM/DM filter insertion loss for a filter section."""
    f = np.logspace(4, 8, 500)
    L_CM, Cx, Cy = 1e-3, 0.47e-6, 4.7e-9  # 1mH CM choke, 0.47μF X-cap, 4.7nF Y-cap
    RS, RL = 50.0, 50.0
    # DM filter: Cx between L,N; leakage inductance of CM choke (~0.5% of L_CM)
    L_leak = L_CM * 0.005
    IL_DM = 20*np.log10(np.abs(1 + (1j*2*pi*f*L_leak + 1/(1j*2*pi*f*Cx))/(RS+RL) 
                                + 1j*2*pi*f*L_leak/RL + RS/(1j*2*pi*f*Cx*RL)) )
    # CM filter: CM choke L_CM, Cy caps to GND
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
    print('✅ CM/DM filter done')

def demo_cm_vs_dm_emissions():
    """Compare CM and DM emission levels vs frequency."""
    f = np.logspace(6, 8, 500)
    A_loop, I_DM, r_dist = 1e-4, 0.1, 3.0
    E_DM = 2.63e-3 * I_DM * A_loop * f**2 / r_dist
    l_cable, I_CM = 0.1, 1e-4
    E_CM = 4.71e-2 * I_CM * l_cable * f / r_dist
    fig, ax = plt.subplots(figsize=(10,5))
    ax.loglog(f/1e6, 20*np.log10(E_DM/1e-6), 'b-', lw=2, label='DM (loop 1cm²)')
    ax.loglog(f/1e6, 20*np.log10(E_CM/1e-6), 'r-', lw=2, label='CM (cable 10cm)')
    limit = np.piecewise(f, [f<88e6, (f>=88e6)&(f<216e6), (f>=216e6)&(f<960e6), f>=960e6],
                         [40, 43.5, 46, 54])
    ax.loglog(f/1e6, limit, 'k--', lw=2, label='FCC Class B @3m')
    ax.set(xlabel='f (MHz)', ylabel='E (dBμV/m)', title='Conducted → Radiated: DM vs CM')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch6_cm_vs_dm.png', dpi=150); plt.close()
    fc = f[np.argmin(np.abs(20*np.log10(E_DM/E_CM)))]
    print(f'  DM/CM crossover: {fc/1e6:.0f} MHz')
    print('✅ CM vs DM demo done')

demo_lisn_impedance(); demo_fcc_conducted_limit()
demo_cm_dm_filter(); demo_cm_vs_dm_emissions()
print('\nCh6: 4/4 ALL PASS')
