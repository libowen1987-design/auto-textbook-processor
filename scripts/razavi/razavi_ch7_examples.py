#!/usr/bin/env python3
"""
Razavi RF Microelectronics, 2nd Ed. — Ch7: Passive Devices
Examples: Inductor Q, spiral inductor model.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ──────────────────────────────────────────────────────
# Ex 7.1: Inductor Q calculation
# ──────────────────────────────────────────────────────
def example_inductor_q():
    """Q factor of on-chip spiral inductor."""
    L = 5e-9  # 5 nH
    RS = 5.0  # series resistance
    RP = 1000.0  # parallel loss resistance (from substrate)

    f = np.logspace(8, 11, 200)  # 100 MHz to 100 GHz
    omega = 2 * np.pi * f

    Q_series = omega * L / RS
    Q_parallel = RP / (omega * L)
    # Effective Q (from combined model)
    Q_eff = omega * L / RS * RP / (RP + ((omega*L/RS)**2 + 1) * RS)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogx(f/1e9, Q_series, 'b-', alpha=0.5, label='$Q_S = \\omega L/R_S$')
    ax.semilogx(f/1e9, Q_parallel, 'r-', alpha=0.5, label='$Q_P = R_P/(\\omega L)$')
    ax.semilogx(f/1e9, Q_eff, 'g-', linewidth=2, label='Effective $Q$')
    ax.axvline(2.4, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('Frequency (GHz)')
    ax.set_ylabel('Quality Factor $Q$')
    ax.set_title('Spiral Inductor Q ($L=5$ nH, $R_S=5\\Omega$, $R_P=1$ k$\\Omega$)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0.1, 100)
    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/razavi/figures/ch7_inductor_q.png', dpi=150)
    plt.close(fig)

    idx = np.argmin(np.abs(f - 2.4e9))
    print(f"Ex 7.1: At 2.4 GHz: Q_eff = {Q_eff[idx]:.1f} (vs Q_series={Q_series[idx]:.1f})")
    print(f"        Peak Q = {np.max(Q_eff):.1f} at {f[np.argmax(Q_eff)]/1e9:.2f} GHz")
    print("Saved: ch7_inductor_q.png")
    print()

# ──────────────────────────────────────────────────────
# Self-resonant frequency
# ──────────────────────────────────────────────────────
def example_srf():
    """Self-resonant frequency of an inductor with parasitics."""
    L = 5e-9
    Cox = 50e-15  # 50 fF
    Csub = 20e-15  # 20 fF
    C_total = Cox + Csub  # simplified

    f_SR = 1 / (2 * np.pi * np.sqrt(L * C_total))
    print(f"Ex 7.x: L={L*1e9:.1f} nH, C_total={C_total*1e15:.0f} fF")
    print(f"        f_SR = {f_SR/1e9:.1f} GHz (operate at < {0.5*f_SR/1e9:.1f} GHz)")
    print()

# ──────────────────────────────────────────────────────
# Varactor C-V characteristic
# ──────────────────────────────────────────────────────
def example_varactor():
    """MOS varactor C-V curve."""
    V_g = np.linspace(-2, 2, 200)
    V_th = 0.5

    # Accumulation-mode varactor model (simplified)
    C_max = 2e-12  # 2 pF
    C_min = C_max / 3

    C = C_min + (C_max - C_min) / (1 + np.exp(-10*(V_g - V_th)))
    Q = 30  # at 2.4 GHz

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(V_g, C/1e-12, 'b-', linewidth=2)
    ax.set_xlabel('Gate Voltage (V)')
    ax.set_ylabel('Capacitance (pF)')
    ax.set_title('MOS Varactor C-V Characteristic ($C_{\\max}/C_{\\min}=3$)')
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/razavi/figures/ch7_varactor.png', dpi=150)
    plt.close(fig)
    print(f"Ex 7.6: Varactor: Cmax = {C_max/1e-12:.1f} pF, Cmin = {C_min/1e-12:.2f} pF, Q = {Q}")
    print("Saved: ch7_varactor.png")
    print()

# ──────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────
if __name__ == "__main__":
    print("="*60)
    print("Razavi Ch7 — Passive Devices: Example Codes")
    print("="*60)
    print()

    example_inductor_q()
    example_srf()
    example_varactor()

    print("="*60)
    print("All Ch7 examples completed successfully.")
    print("="*60)
