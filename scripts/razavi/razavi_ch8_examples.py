#!/usr/bin/env python3
"""
Razavi RF Microelectronics, 2nd Ed. — Ch8: Oscillators
Examples: Phase noise (Lesson), VCO design, tuning range.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ──────────────────────────────────────────────────────
# Lesson's Phase Noise Model
# ──────────────────────────────────────────────────────
def example_phase_noise():
    """Lesson's phase noise model."""
    f0 = 2.4e9
    Psig_dbm = 0  # dBm
    Psig_W = 10**(Psig_dbm/10) * 1e-3
    Q = 10
    F = 4  # excess noise factor
    fc_1f3 = 100e3  # 1/f^3 corner = 100 kHz

    k = 1.38e-23
    T = 300

    df = np.logspace(1, 7, 200)  # 10 Hz to 10 MHz

    # Lesson: L(df) = 10*log10[2FkT/Psig * (1 + (f0/(2Q*df))^2) * (1 + fc_1f3/|df|)]
    PN = 10 * np.log10(
        2 * F * k * T / Psig_W *
        (1 + (f0 / (2 * Q * df))**2) *
        (1 + fc_1f3 / np.abs(df))
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogx(df, PN, 'b-', linewidth=2)
    ax.axvline(fc_1f3, color='r', linestyle='--', alpha=0.5, label=f'$f_{{1/f^3}}$ = {fc_1f3/1e3:.0f} kHz')
    ax.axvline(f0/(2*Q), color='g', linestyle='--', alpha=0.5, label=f'$f_0/(2Q)$ = {f0/(2*Q)/1e6:.1f} MHz')
    ax.set_xlabel('Frequency Offset (Hz)')
    ax.set_ylabel('Phase Noise (dBc/Hz)')
    ax.set_title('VCO Phase Noise (Lesson Model)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(10, 10e6)
    ax.set_ylim(-170, -40)
    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/razavi/figures/ch8_phase_noise.png', dpi=150)
    plt.close(fig)

    idx_1MHz = np.argmin(np.abs(df - 1e6))
    print(f"Ex 8.12: PN at 1 MHz: {PN[idx_1MHz]:.0f} dBc/Hz")
    print(f"         f0/(2Q) = {f0/(2*Q)/1e6:.1f} MHz (transition to 1/f²)")
    print("Saved: ch8_phase_noise.png")
    print()

# ──────────────────────────────────────────────────────
# VCO Tuning Range
# ──────────────────────────────────────────────────────
def example_vco_tuning():
    """VCO frequency vs tuning voltage."""
    L = 5e-9
    C_fixed = 1e-12  # 1 pF
    C_max = 2e-12  # 2 pF
    C_min = 0.5e-12  # 0.5 pF

    V_tune = np.linspace(0, 2, 200)
    V_th = 1.0
    C_var = C_min + (C_max - C_min) / (1 + np.exp(-10*(V_tune - V_th)))
    C_tot = C_fixed + C_var
    f0 = 1 / (2 * np.pi * np.sqrt(L * C_tot))

    # KVCO (MHz/V) = df/dV ≈ compute numerically
    K_vco = np.gradient(f0, V_tune) / 1e6  # MHz/V

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

    ax1.plot(V_tune, f0/1e9, 'b-', linewidth=2)
    ax1.set_xlabel('Tune Voltage (V)')
    ax1.set_ylabel('Frequency (GHz)')
    ax1.set_title('VCO Tuning Curve')
    ax1.grid(True, alpha=0.3)

    ax2.plot(V_tune, K_vco, 'r-', linewidth=2)
    ax2.set_xlabel('Tune Voltage (V)')
    ax2.set_ylabel('$K_{VCO}$ (MHz/V)')
    ax2.set_title('VCO Gain vs Tune Voltage')
    ax2.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/razavi/figures/ch8_vco_tuning.png', dpi=150)
    plt.close(fig)

    print(f"Ex 8.8: Tuning range: {np.min(f0)/1e9:.2f} to {np.max(f0)/1e9:.2f} GHz")
    print(f"        Ratio: {np.max(f0)/np.min(f0):.2f}x ({100*(np.max(f0)/np.min(f0)-1):.0f}%)")
    print(f"        Max KVCO: {np.max(K_vco):.0f} MHz/V")
    print("Saved: ch8_vco_tuning.png")
    print()

# ──────────────────────────────────────────────────────
# VCO Design Example 8.18
# ──────────────────────────────────────────────────────
def example_vco_design():
    """2.4 GHz VCO design."""
    f0 = 2.4e9
    L = 4e-9
    Q = 12
    Rp = Q * 2 * np.pi * f0 * L
    I_tail = 2e-3

    C_tot = 1 / ((2*np.pi*f0)**2 * L)
    V0 = I_tail * Rp  # voltage-limited or current-limited

    print("Ex 8.18: 2.4 GHz VCO Design")
    print(f"  L = {L*1e9:.1f} nH, Q = {Q}")
    print(f"  R_p = Q·ω₀L = {Rp:.0f} Ω")
    print(f"  C_tot = {C_tot*1e15:.0f} fF")
    print(f"  I_tail = {I_tail*1e3:.0f} mA")
    print(f"  Oscillation amplitude V₀ = I·R_p = {V0:.2f} V")
    print(f"  Startup condition: g_m > 1/R_p = {1/Rp*1e3:.1f} mS")
    print()

# ──────────────────────────────────────────────────────
# Injection Locking
# ──────────────────────────────────────────────────────
def example_injection_locking():
    """Injection locking range."""
    f0 = 5e9
    Q = 10
    Iinj_Iosc_ratio = np.logspace(-3, 0, 50)

    omega_L = (2*np.pi*f0/(2*Q)) * Iinj_Iosc_ratio
    f_L = omega_L / (2*np.pi)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.loglog(Iinj_Iosc_ratio, f_L/1e6, 'b-', linewidth=2)
    ax.set_xlabel('$I_{\\mathrm{inj}}/I_{\\mathrm{osc}}$')
    ax.set_ylabel('Locking Range (MHz)')
    ax.set_title('Injection Locking Range ($f_0=5$ GHz, $Q=10$)')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/razavi/figures/ch8_injection_locking.png', dpi=150)
    plt.close(fig)

    print(f"Ex 8.22: For I_inj/I_osc = 0.1: Δf_L = {f_L[np.argmin(np.abs(Iinj_Iosc_ratio-0.1))]:.1f} MHz")
    print("Saved: ch8_injection_locking.png")
    print()

# ──────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────
if __name__ == "__main__":
    print("="*60)
    print("Razavi Ch8 — Oscillators: Example Codes")
    print("="*60)
    print()

    example_phase_noise()
    example_vco_tuning()
    example_vco_design()
    example_injection_locking()

    print("="*60)
    print("All Ch8 examples completed successfully.")
    print("="*60)
