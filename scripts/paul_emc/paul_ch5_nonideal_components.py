#!/usr/bin/env python3
"""Paul EMC Ch5: Nonideal Behavior of Components.
Examples: skin effect, capacitor SRF, ferrite bead, resistor HF model."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import pi, mu_0, epsilon_0

SIGMA_CU = 5.8e7

def demo_skin_effect():
    """Skin depth vs frequency (Example 5.1 style)."""
    f = np.logspace(2, 10, 500)
    delta = 1 / np.sqrt(pi * f * mu_0 * SIGMA_CU)
    rw_gauges = {'20 AWG': 16e-3*25.4e-3, '24 AWG': 20.1e-3*25.4e-3, '30 AWG': 10e-3*25.4e-3}
    fig, ax = plt.subplots(figsize=(10,5))
    ax.loglog(f, delta*1e3, 'b-', lw=2, label='Skin depth δ (mm)')
    for name, rw in rw_gauges.items():
        ax.axhline(rw*1e3, ls='--', alpha=0.5, label=f'{name} r_w={rw*1e3:.2f}mm')
    ax.set(xlabel='f (Hz)', ylabel='δ (mm)', title='Skin Depth in Copper',
           xlim=(100, 1e10), ylim=(1e-4, 10))
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch5_skin_depth.png', dpi=150); plt.close()
    print(f'  δ(1MHz)={delta[np.argmin(np.abs(f-1e6))]*1e3:.3f}mm')
    print(f'  δ(100MHz)={delta[np.argmin(np.abs(f-1e8))]*1e3:.3f}mm')
    print('✅ Skin effect done')

def demo_wire_resistance():
    """Wire AC resistance vs frequency for different gauges."""
    f = np.logspace(5, 9, 500)
    gauges = {'20 AWG': 16e-3*25.4e-3, '24 AWG': 20.1e-3*25.4e-3, '28 AWG': 7.5e-3*25.4e-3}
    fig, ax = plt.subplots(figsize=(10,5))
    for name, rw in gauges.items():
        delta = 1 / np.sqrt(pi * f * mu_0 * SIGMA_CU)
        R_dc = 1/(SIGMA_CU * pi * rw**2)
        R_hf = 1/(2 * rw * SIGMA_CU * delta)
        R_eff = np.where(rw/delta > 3, R_hf, R_dc)
        ax.loglog(f, R_eff, lw=2, label=name)
    ax.set(xlabel='f (Hz)', ylabel='R (Ω/m)', title='Wire AC Resistance per-meter',
           xlim=(1e5, 1e9), ylim=(1e-3, 100))
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch5_wire_Rac.png', dpi=150); plt.close()
    print('✅ Wire resistance done')

def demo_capacitor_impedance():
    """Capacitor impedance: below/at/above SRF."""
    f = np.logspace(4, 9, 1000)
    caps = [
        ('10μF + ESL=5nH', 10e-6, 5e-9, 0.1),
        ('0.1μF + ESL=1nH', 0.1e-6, 1e-9, 0.05),
        ('1nF + ESL=0.5nH', 1e-9, 0.5e-9, 0.02),
        ('100pF + ESL=0.3nH', 100e-12, 0.3e-9, 0.01),
    ]
    fig, ax = plt.subplots(figsize=(10,5))
    for name, C, ESL, ESR in caps:
        Z = np.sqrt(ESR**2 + (2*pi*f*ESL - 1/(2*pi*f*C))**2)
        SRF = 1/(2*pi*np.sqrt(ESL*C))
        ax.loglog(f, Z, lw=2, label=f'{name} (SRF={SRF/1e6:.1f}MHz)')
    ax.set(xlabel='f (Hz)', ylabel='|Z| (Ω)', title='Capacitor Impedance vs Frequency',
           xlim=(1e4, 1e9), ylim=(1e-3, 1e5))
    ax.legend(fontsize=9); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch5_cap_Z.png', dpi=150); plt.close()
    print('✅ Capacitor impedance done')

def demo_ferrite_bead():
    """Ferrite bead impedance: R, X, and |Z|."""
    f = np.logspace(5, 9, 500)
    L0, R0, f0 = 300e-9, 600, 100e6
    L_eff = L0 / (1 + (f/f0)**2)
    R_eff = R0 * (f/f0) / (1 + (f/f0)**2)
    Z = np.sqrt(R_eff**2 + (2*pi*f*L_eff)**2)
    fig, ax = plt.subplots(figsize=(10,5))
    ax.loglog(f, Z, 'b-', lw=2, label='|Z|')
    ax.loglog(f, R_eff, 'r--', lw=1.5, label='R (loss)')
    ax.loglog(f, 2*pi*f*L_eff, 'g--', lw=1.5, label='X (inductive)')
    ax.set(xlabel='f (Hz)', ylabel='Impedance (Ω)', title='Ferrite Bead Impedance (Typical 300Ω @ 100MHz)',
           xlim=(1e5, 1e9), ylim=(1, 1000))
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch5_ferrite_bead.png', dpi=150); plt.close()
    print(f'  |Z|(@100MHz)={Z[np.argmin(np.abs(f-100e6))]:.0f}Ω')
    print('✅ Ferrite bead done')

def demo_resistor_hf():
    """Resistor high-frequency model: Z vs f for different types."""
    f = np.logspace(6, 10, 500)
    resistors = [
        ('SMD 0402 100Ω', 100, 0.3e-12, 0.3e-9),
        ('SMD 0603 1kΩ', 1000, 0.5e-12, 0.5e-9),
        ('Leaded 10kΩ', 10000, 0.5e-12, 5e-9),
        ('Wirewound 10Ω', 10, 1e-12, 20e-9),
    ]
    fig, ax = plt.subplots(figsize=(10,5))
    for name, R, Cp, Ls in resistors:
        Z = np.sqrt(R**2 + (2*pi*f*Ls - 1/(2*pi*f*Cp))**2) / np.sqrt(1 + (2*pi*f*Cp*R)**2)
        ax.loglog(f, Z, lw=2, label=f'{name}')
        SRF = 1/(2*pi*np.sqrt(Ls*Cp))
        ax.axvline(SRF, ls=':', alpha=0.3)
    ax.set(xlabel='f (Hz)', ylabel='|Z| (Ω)', title='Resistor HF Model Impedance',
           xlim=(1e6, 1e10), ylim=(1, 1e5))
    ax.legend(fontsize=9); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch5_resistor_HF.png', dpi=150); plt.close()
    print('✅ Resistor HF model done')

demo_skin_effect(); demo_wire_resistance(); demo_capacitor_impedance()
demo_ferrite_bead(); demo_resistor_hf()
print('\nCh5: 5/5 ALL PASS')
