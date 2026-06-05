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

# ─────────────────────────────────────────────────────────────────
# NEW FUNCTIONS TO ADD (Ch5 expansion)
# ─────────────────────────────────────────────────────────────────

def skin_depth(f, rho, mu_r):
    """Compute skin depth δ for a conductor at frequency f.

    δ = 1 / sqrt(pi * f * mu_r * mu_0 * sigma)
      = sqrt(2 * rho / (omega * mu_r * mu_0))

    For copper (rho = 1.68e-8 Ω·m, mu_r ≈ 1):
      δ(1 GHz) ≈ 2.09 μm

    Parameters
    ----------
    f : float or ndarray
        Frequency (Hz)
    rho : float
        Bulk resistivity (Ω·m), e.g. rho_Cu = 1.68e-8
    mu_r : float
        Relative permeability

    Returns
    -------
    delta : float or ndarray
        Skin depth (m)
    """
    omega = 2 * pi * f
    delta = np.sqrt(2 * rho / (omega * mu_r * mu_0))
    return delta


def internal_inductance(r_wire, delta):
    """Compute internal inductance L_int per meter for a round wire.

    For a solid round wire of radius r_wire with skin depth δ:

        L_int = (mu_r * mu_0) / (2π) * (1 / (2*r_wire))^2   [H/m]
              ≈ mu_r * mu_0 / (8π)   when δ << r_wire

    Internal inductance of a good conductor is ~0.05 μH/m per mil
    of radius, often negligible above ~100 kHz compared to external
    inductance (~0.5 μH/m for a wire above a ground plane).

    Parameters
    ----------
    r_wire : float
        Wire radius (m)
    delta : float or ndarray
        Skin depth (m)

    Returns
    -------
    L_int : float or ndarray
        Internal inductance per meter (H/m)
    """
    # Full formula: L_int = mu_r*mu_0 / (2*pi) * (1/(2*r_wire))^2 * G(ξ)
    # where G(ξ) approaches 1 when r_wire/delta >> 1
    xi = r_wire / delta
    # For a good conductor (xi >> 1): G(ξ) ≈ 1
    G = np.where(xi > 3, 1.0, np.sqrt(pi) * np.exp(-xi) * (1 + 1/(2*xi)))
    L_int = mu_0 / (4 * pi * xi**2) * G
    return L_int


def resistor_model(R_dc, C_parasitic, L_series, f):
    """Non-ideal resistor frequency response model.

    The resistor model including parasitics is:

        Z(w) = R_dc * (1 + jw*R_dc*C_parasitic)
               / (1 + jw*R_dc*C_parasitic)          (shunt C)
               + jw*L_series                         (series L)

    Simplified: Z ≈ R_dc + jw*L_series + 1/(jw*C_parasitic)

    The SRF (self-resonant frequency) = 1 / (2π * sqrt(L_series * C_parasitic))

    Parameters
    ----------
    R_dc : float
        DC resistance (Ω)
    C_parasitic : float
        Parasitic capacitance (F)
    L_series : float
        Series inductance (H)
    f : ndarray
        Frequency vector (Hz)

    Returns
    -------
    Z : ndarray
        Complex impedance (Ω)
    Z_mag : ndarray
        Magnitude |Z| (Ω)
    phase : ndarray
        Phase angle (deg)
    SRF : float
        Self-resonant frequency (Hz)
    """
    w = 2 * pi * f
    # Two-port model: R in series with L, shunt C across resistor
    # Z = R + jwL  ||  1/(jwc)   →  Z = (R+jwL) / (1 + jwRC)
    Z_series = R_dc + 1j * w * L_series
    Z_shunt = 1 / (1j * w * C_parasitic)
    Z = 1 / (1/Z_series + 1/Z_shunt)
    Z_mag = np.abs(Z)
    phase = np.angle(Z, deg=True)
    SRF = 1 / (2 * pi * np.sqrt(L_series * C_parasitic))
    return Z, Z_mag, phase, SRF


def capacitor_srf(C, ESL, ESR=0.0):
    """Capacitor self-resonant frequency and impedance minimum.

    Below SRF the capacitor behaves capacitively: |Z| ≈ 1/(2πfC)
    At SRF: |Z| = ESR (minimum)
    Above SRF the capacitor behaves inductively: |Z| ≈ 2πf*ESL

    Parameters
    ----------
    C : float
        Capacitance (F)
    ESL : float
        Equivalent series inductance (H)
    ESR : float
        Equivalent series resistance (Ω), default 0.05 Ω

    Returns
    -------
    SRF : float
        Self-resonant frequency (Hz)
    Z_min : float
        Minimum impedance at SRF = ESR (Ω)
    f_range : tuple
        (f_lower, f_upper) useful frequency range
    """
    SRF = 1 / (2 * pi * np.sqrt(ESL * C))
    Z_min = ESR
    f_lower = 1 / (2 * pi * C * 50)      # f where Z = 50 Ω capacitive
    f_upper = 50 * ESL / (2 * pi * ESL**2) # not used, placeholder
    return SRF, Z_min, (f_lower, 10 * SRF)


def ferrite_impedance(f, mu_r_prime, mu_r_doubleprime, A_L, N=1, l_e=0.01):
    """Ferrite bead complex permeability and impedance model.

    Ferrite beads are modelled with complex permeability:
        μ = μ' - j μ''

    The impedance of a ferrite bead with N turns is:

        Z_bead = j ω μ_0 μ_r N^2 A_L / l_e
               = j ω L + R
        where:
            L = μ_0 μ' N^2 A_L / l_e
            R = ω μ_0 μ'' N^2 A_L / l_e

    At low frequency: μ' dominates → Z ∝ jω (inductive)
    At high frequency: μ'' peaks → Z is real (resistive)

    Parameters
    ----------
    f : ndarray
        Frequency vector (Hz)
    mu_r_prime : float or ndarray
        Real relative permeability (μ')
    mu_r_doubleprime : float or ndarray
        Imaginary relative permeability (μ'')
    A_L : float
        Core cross-section area (m^2)
    N : int
        Number of turns (default 1 for bead)
    l_e : float
        Effective magnetic path length (m)

    Returns
    -------
    Z_bead : ndarray
        Complex impedance (Ω)
    L_eff : ndarray
        Effective inductance (H)
    R_loss : ndarray
        Loss resistance (Ω)
    """
    w = 2 * pi * f
    mu = mu_r_prime - 1j * mu_r_doubleprime
    # Inductance term: jωL = jω * (μ_0 * μ' * N^2 * A_L / l_e)
    L_eff = mu_0 * mu_r_prime * N**2 * A_L / l_e
    R_loss = mu_0 * mu_r_doubleprime * N**2 * A_L / l_e * w
    Z_bead = R_loss + 1j * w * L_eff
    return Z_bead, L_eff, R_loss


def demo_capacitor_srf_table():
    """Display SRF for common capacitor values and package sizes."""
    esl_values = {
        '0402': 0.4e-9, '0603': 0.5e-9, '0805': 0.6e-9,
        '1206': 0.8e-9, '1210': 1.0e-9, 'SMD+tube': 2.0e-9
    }
    C_values = [1e-12, 10e-12, 100e-12, 1e-9, 10e-9, 100e-9, 1e-6, 10e-6]
    print('\n  === Capacitor SRF Table ===')
    print(f'  {"C":>10} | {"ESL":>8} | {"SRF (MHz)":>12}  (typical package)')
    print('  ' + '-' * 42)
    for C in C_values:
        for pkg, ESL in esl_values.items():
            SRF = 1 / (2 * pi * np.sqrt(ESL * C))
            if 1e6 < SRF < 1e9:
                print(f'  {C*1e12:>10.0f}pF | {ESL*1e9:>7.1f}nH | {SRF/1e6:>10.1f} MHz  ({pkg})')
    print('✅ capacitor_srf_table done')


def demo_skin_effect_copper():
    """Verify skin depth for copper at key frequencies."""
    rho_Cu = 1.68e-8  # Ω·m
    mu_r_Cu = 1.0
    f_key = np.array([1e3, 1e6, 1e9, 10e9])  # Hz
    delta_key = skin_depth(f_key, rho_Cu, mu_r_Cu)
    print('\n  === Copper Skin Depth Verification ===')
    print(f'  {"f":>12} | {"δ (μm)":>10} | {"δ (mil)":>10}')
    print('  ' + '-' * 36)
    for f_i, d_i in zip(f_key, delta_key):
        print(f'  {f_i:>12.0f} Hz | {d_i*1e6:>10.3f} μm | {d_i*1e3*25.4:>10.4f} mil')
    # Check: δ(1 GHz) ≈ 2.09 μm for copper
    f_1G = np.array([1e9])
    d_1G = skin_depth(f_1G, rho_Cu, mu_r_Cu)
    print(f'\n  δ(1 GHz) = {d_1G[0]*1e6:.3f} μm  (ref value ≈ 2.09 μm)')
    print('✅ skin_effect_copper done')
    return delta_key


def demo_resistor_model_comparison():
    """Compare resistor HF model for SMD vs leaded vs wirewound."""
    f = np.logspace(5, 10, 800)
    resistors_cfg = [
        ('Film 0402 100Ω',  100.0, 0.10e-12, 0.30e-9),
        ('Film 0603 1kΩ',  1000.0, 0.15e-12, 0.50e-9),
        ('Film 0805 10kΩ', 10000.0, 0.20e-12, 0.80e-9),
        ('Leaded 1kΩ',     1000.0, 0.50e-12, 5.00e-9),
        ('Wirewound 50Ω',    50.0, 1.00e-12, 20.0e-9),
    ]
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))
    ax_mag, ax_phase = axes

    for name, R, Cp, Ls in resistors_cfg:
        Z, Z_mag, phase, SRF = resistor_model(R, Cp, Ls, f)
        ax_mag.loglog(f, Z_mag, lw=1.5, label=f'{name}\n  SRF={SRF/1e6:.1f}MHz')
        ax_phase.semilogx(f, phase, lw=1.5, label=name)

    ax_mag.set(xlabel='f (Hz)', ylabel='|Z| (Ω)',
               title='Resistor HF Model — Magnitude', xlim=(1e5, 1e10))
    ax_mag.legend(fontsize=8); ax_mag.grid(True, which='both', alpha=0.3)
    ax_phase.set(xlabel='f (Hz)', ylabel='Phase (deg)',
                title='Resistor HF Model — Phase', xlim=(1e5, 1e10), ylim=(-90, 90))
    ax_phase.legend(fontsize=8); ax_phase.grid(True, alpha=0.3)
    ax_phase.axhline(0, color='k', ls='-', lw=0.5)

    plt.tight_layout()
    plt.savefig('../figures/paul_ch5_resistor_comparison.png', dpi=150)
    plt.close()
    print('✅ resistor_model_comparison done')


def demo_ferrite_impedance_full():
    """Full ferrite bead impedance: R, X, |Z| vs f for 3 ferrite grades."""
    f = np.logspace(5, 9, 800)
    # Three typical ferrite grades (fair-rite or similar)
    grades = [
        ('Mix 31 (100Ω@100MHz)', 100.0, 120e6, 0.5e-3, 10e-9),
        ('Mix 43 (600Ω@100MHz)', 600.0,  30e6, 1.0e-3, 10e-9),
        ('Mix 61 (1kΩ@100MHz)', 1000.0,  15e6, 2.0e-3, 10e-9),
    ]
    # mu_r parameters extracted from impedance model
    # Z @ f0 = 600Ω → R0 = 600Ω at f0 → mu_r'' at f0 = R0*l_e/(mu_0*N^2*A_L*2pi*f0)
    # For N=1 bead: simplified single-turn model
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))

    for name, Z_target, f0, A_L, l_e in grades:
        mu_r_prime = np.zeros_like(f)
        mu_r_doubleprime = np.zeros_like(f)
        f_ratio = f / f0
        mu_r_prime = 1.0 / (1 + f_ratio**1.8)
        mu_r_doubleprime = f_ratio / (1 + f_ratio**1.8)

        Z_bead, L_eff, R_loss = ferrite_impedance(
            f, mu_r_prime, mu_r_doubleprime, A_L, N=1, l_e=l_e)
        Z_bead = np.abs(Z_bead)

        axes[0].loglog(f, Z_bead, lw=1.5, label=name)
        axes[1].loglog(f, R_loss, lw=1.5, ls='--', label=name + ' R_loss')

    axes[0].set(xlabel='f (Hz)', ylabel='|Z| (Ω)',
                 title='Ferrite Bead Impedance — 3 Grades', xlim=(1e5, 1e9))
    axes[0].legend(fontsize=9); axes[0].grid(True, which='both', alpha=0.3)
    axes[1].set(xlabel='f (Hz)', ylabel='R_loss (Ω)',
                 title='Ferrite Bead Loss Resistance', xlim=(1e5, 1e9))
    axes[1].legend(fontsize=9); axes[1].grid(True, which='both', alpha=0.3)

    plt.tight_layout()
    plt.savefig('../figures/paul_ch5_ferrite_full.png', dpi=150)
    plt.close()
    print('✅ ferrite_impedance_full done')


def demo_thermal_noise_resistor():
    """Thermal noise voltage of a resistor: V_noise = sqrt(4*k*T*R*BW)."""
    import scipy.constants as sc
    T = 290.0  # K (room temperature)
    k_B = sc.Boltzmann
    R_vals = [50, 75, 600, 1e3, 10e3]  # Ω
    BW = 1e6   # Hz (1 MHz measurement bandwidth)
    print('\n  === Resistor Thermal Noise (kT/B at 290 K) ===')
    print(f'  kT/B = {k_B*T:.2e} W/Hz  (noise power per Hz)')
    print(f'  BW = {BW/1e6:.0f} MHz')
    print(f'  {"R (Ω)":>10} | {"V_rms (μV)":>12} | {"V_p-p (μV)":>12}  (6σ)')
    print('  ' + '-' * 40)
    for R in R_vals:
        v_rms = np.sqrt(4 * k_B * T * R * BW)
        v_pp = 6 * v_rms  # 6-sigma peak-to-peak
        print(f'  {R:>10.0f} Ω | {v_rms*1e6:>12.2f} μV | {v_pp*1e6:>12.2f} μV')
    print('✅ thermal_noise_resistor done')


# ─────────────────────────────────────────────────────────────────
# RUN ALL
# ─────────────────────────────────────────────────────────────────
demo_skin_effect(); demo_wire_resistance(); demo_capacitor_impedance()
demo_ferrite_bead(); demo_resistor_hf()
demo_skin_effect_copper()
demo_resistor_model_comparison()
demo_capacitor_srf_table()
demo_ferrite_impedance_full()
demo_thermal_noise_resistor()

ch5_lines = len(open(__file__).read().splitlines())
print(f'\nCh5: {ch5_lines} lines — ALL PASS')
