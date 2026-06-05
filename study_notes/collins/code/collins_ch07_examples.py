#!/usr/bin/env python3
"""
Collins Ch7 (2nd Ed. Ch8) — Periodic Structures and Microwave Filters
Examples & Demos

Sections:
  1. Periodic structure dispersion (k-β diagram)
  2. Butterworth prototype g-values + response
  3. Chebyshev prototype g-values + ripple comparison
  4. Filter transformations (LP→BP/HP/BS)
  5. Stepped-impedance LPF design
  6. Coupled-line BPF design
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")  # non-interactive backend for headless env
import matplotlib.pyplot as plt
from scipy.special import factorial  # not actually used but kept for completeness
import os

OUT = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(OUT, exist_ok=True)


# ============================================================
# Demo 1: Periodic Structure Dispersion (k-β Diagram)
# ============================================================
def demo_periodic_dispersion():
    """
    Capacitively loaded transmission line: compute and plot k-β diagram.

    Unit cell: TL length d, shunt capacitor C_s.
    Dispersion: cos(βd) = cos(k₀d) - (ω C_s Z₀ / 2) sin(k₀d)
    where k₀ = ω / v_p, v_p = c / sqrt(ε_r).
    """
    print("=" * 60)
    print("Demo 1: Periodic Structure Dispersion (k-β Diagram)")
    print("=" * 60)

    c0 = 3e8          # speed of light
    eps_r = 2.2       # substrate permittivity (e.g., RT/Duroid 5880)
    vp = c0 / np.sqrt(eps_r)

    d = 10e-3         # unit cell length = 10 mm
    Z0 = 50.0         # line characteristic impedance
    Cs = 1e-12        # shunt capacitance = 1 pF

    # Frequency sweep
    f = np.linspace(0.1e9, 12e9, 2000)
    omega = 2 * np.pi * f
    k0 = omega / vp

    # Dispersion equation: cos(beta*d) = cos(k0*d) - (omega*Cs*Z0/2)*sin(k0*d)
    rhs = np.cos(k0 * d) - (omega * Cs * Z0 / 2.0) * np.sin(k0 * d)
    rhs = np.clip(rhs, -1.0, 1.0)  # clamp for numerical stability

    beta_d = np.arccos(rhs)
    beta = beta_d / d

    # Identify passbands (|rhs| <= 1)
    passband = np.abs(rhs) <= 1.0

    # Plot
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))

    # Color passband / stopband regions
    ax.fill_between(f / 1e9, beta_d, 0,
                    where=passband, color='lightgreen', alpha=0.4, label='Passband')
    ax.fill_between(f / 1e9, beta_d, 0,
                    where=~passband, color='lightcoral', alpha=0.4, label='Stopband')

    ax.plot(f / 1e9, beta_d, 'b-', linewidth=2, label=r'$\beta d$')
    ax.plot(f / 1e9, k0 * d, 'k--', linewidth=1, label=r'$k_0 d$ (unloaded)')

    ax.set_xlabel('Frequency (GHz)')
    ax.set_ylabel(r'$\beta d$ (rad)')
    ax.set_title(f'Periodic Structure k-β Diagram\n'
                 f'$d={d*1e3:.0f}$ mm, $C_s={Cs*1e12:.0f}$ pF, $Z_0={Z0:.0f}\\ \\Omega$')
    ax.set_ylim(0, np.pi + 0.2)
    ax.axhline(np.pi, color='gray', ls=':', lw=0.8, label=r'$\pi$ boundary')
    ax.legend(loc='lower right')
    ax.grid(True, alpha=0.3)

    path = os.path.join(OUT, "ch07_demo1_periodic_dispersion.png")
    fig.savefig(path, dpi=120, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {path}")
    print(f"  First stopband centered near "
          f"{f[np.argmax(np.abs(rhs) > 1.0)]/1e9:.2f} GHz\n")
    return f, beta_d, k0


# ============================================================
# Demo 2: Butterworth Prototype g-values + Response
# ============================================================
def butterworth_g(N):
    """Compute Butterworth low-pass prototype g-values."""
    g = np.zeros(N + 2)
    g[0] = 1.0
    for k in range(1, N + 1):
        g[k] = 2.0 * np.sin((2 * k - 1) * np.pi / (2 * N))
    g[N + 1] = 1.0
    return g


def butterworth_response(g, omega_n):
    """
    Compute insertion loss for Butterworth LPF prototype.
    omega_n: normalized frequency array (ω/ω_c).
    """
    N = len(g) - 2
    # For a doubly-terminated ladder network, the insertion loss is
    #   P_LR = 1 + |Γ|^2, where |Γ|^2 is derived from the reflection coefficient.
    # The exact Butterworth response is P_LR = 1 + ω_n^(2N).
    p_lr = 1.0 + omega_n ** (2 * N)
    il_db = 10.0 * np.log10(p_lr)
    return il_db, p_lr


def demo_butterworth():
    """Butterworth prototype g-values and magnitude response."""
    print("=" * 60)
    print("Demo 2: Butterworth Prototype g-values + Response")
    print("=" * 60)

    g5 = butterworth_g(5)
    print(f"  N=5 g-values: g0={g5[0]:.4f}, g1={g5[1]:.4f}, g2={g5[2]:.4f}, "
          f"g3={g5[3]:.4f}, g4={g5[4]:.4f}, g5={g5[5]:.4f}, g6={g5[6]:.4f}")

    # Plot response for various N
    omega_n = np.logspace(-1, 1, 500)
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))

    for N in [3, 5, 7]:
        g = butterworth_g(N)
        il_db, _ = butterworth_response(g, omega_n)
        ax.plot(omega_n, il_db, label=f'N={N}')

    ax.axvline(1.0, color='gray', ls='--', lw=0.8, alpha=0.5)
    ax.set_xscale('log')
    ax.set_xlabel(r'Normalized frequency $\omega/\omega_c$')
    ax.set_ylabel('Insertion Loss (dB)')
    ax.set_title('Butterworth Low-Pass Filter Response')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 40)

    path = os.path.join(OUT, "ch07_demo2_butterworth.png")
    fig.savefig(path, dpi=120, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {path}\n")
    return g5


# ============================================================
# Demo 3: Chebyshev Prototype g-values + Ripple Comparison
# ============================================================
def chebyshev_g(N, ripple_db):
    """Compute Chebyshev low-pass prototype g-values (ripple in dB)."""
    eps = np.sqrt(10 ** (ripple_db / 10) - 1.0)  # ripple factor k
    # beta = ln(coth(L_Ar/17.37)) = 2 * asinh(1/eps)
    beta = 2.0 * np.arcsinh(1.0 / eps)
    gamma = np.sinh(beta / (2.0 * N))

    g = np.zeros(N + 2)
    g[0] = 1.0
    g[1] = 2.0 * np.sin(np.pi / (2.0 * N)) / gamma

    for k in range(2, N + 1):
        num = 4.0 * np.sin((2 * k - 1) * np.pi / (2 * N)) * np.sin((2 * k - 3) * np.pi / (2 * N))
        den = g[k - 1] * (gamma ** 2 + np.sin((k - 1) * np.pi / N) ** 2)
        g[k] = num / den

    if N % 2 == 0:
        g[N + 1] = 1.0 / (np.tanh(beta / 4.0) ** 2)
    else:
        g[N + 1] = 1.0

    return g


def chebyshev_response(g, omega_n):
    """Insertion loss for Chebyshev prototype using P_LR = 1 + k^2 T_N^2(ω_n)."""
    N = len(g) - 2
    # Determine k from the first prototype value:
    # g1 = 2 sin(π/2N) / γ, and γ = sinh((1/N) asinh(1/k))
    # We can compute k from the ripple level:
    # P_LR(ω=1) = 1 + k^2 * T_N^2(1) = 1 + k^2 = 10^(L_Ar/10)
    # So k = sqrt(10^(L_Ar/10) - 1)
    # We don't know L_Ar from g values, so estimate:
    # For most common prototypes, ripple = 0.01, 0.1, 0.5, 3 dB
    # Let's determine from the ratio pattern
    # Simpler: iterate T_N
    def Tn(x, n):
        return np.cos(n * np.arccos(x))

    # Infer ripple dB from g1
    # Not reliable; let the caller provide it
    return None


def chebyshev_response_from_ripple(N, ripple_db, omega_n):
    """Chebyshev response directly from N and ripple."""
    k2 = 10 ** (ripple_db / 10) - 1.0

    def Tn(x):
        return np.cos(N * np.arccos(np.clip(x, -1, 1)))

    p_lr = 1.0 + k2 * Tn(omega_n) ** 2
    il_db = 10.0 * np.log10(p_lr)
    return il_db, p_lr


def demo_chebyshev():
    """Chebyshev prototype g-values and ripple comparison."""
    print("=" * 60)
    print("Demo 3: Chebyshev Prototype g-values + Ripple Comparison")
    print("=" * 60)

    # Compute g-values for 0.5 dB ripple, N=3
    g3_05 = chebyshev_g(3, 0.5)
    print(f"  Chebyshev 0.5 dB N=3: g1={g3_05[1]:.4f}, g2={g3_05[2]:.4f}, "
          f"g3={g3_05[3]:.4f}, g4={g3_05[4]:.4f}")

    g3_01 = chebyshev_g(3, 0.1)
    print(f"  Chebyshev 0.1 dB N=3: g1={g3_01[1]:.4f}, g2={g3_01[2]:.4f}, "
          f"g3={g3_01[3]:.4f}, g4={g3_01[4]:.4f}")

    g5_05 = chebyshev_g(5, 0.5)
    print(f"  Chebyshev 0.5 dB N=5: g1={g5_05[1]:.4f}, g2={g5_05[2]:.4f}, "
          f"g3={g5_05[3]:.4f}, g4={g5_05[4]:.4f}, g5={g5_05[5]:.4f}, "
          f"g6={g5_05[6]:.4f}")

    # Plot response comparison
    omega_n = np.linspace(0, 2, 1000)
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))

    for ripple in [0.01, 0.1, 0.5]:
        il_db, _ = chebyshev_response_from_ripple(5, ripple, omega_n)
        ax.plot(omega_n, il_db, label=f'{ripple} dB ripple, N=5')

    # Add Butterworth for comparison
    g5 = butterworth_g(5)
    il_bw, _ = butterworth_response(g5, omega_n)
    ax.plot(omega_n, il_bw, 'k--', label='Butterworth N=5')

    ax.axvline(1.0, color='gray', ls=':', lw=0.8)
    ax.set_xlabel(r'Normalized frequency $\omega/\omega_c$')
    ax.set_ylabel('Insertion Loss (dB)')
    ax.set_title('Chebyshev vs Butterworth Low-Pass Response')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 40)

    # Inset: zoom into passband to show ripple
    ax_inset = fig.add_axes([0.55, 0.45, 0.32, 0.32])
    for ripple in [0.01, 0.1, 0.5]:
        il_db, _ = chebyshev_response_from_ripple(5, ripple, omega_n)
        ax_inset.plot(omega_n, il_db, label=f'{ripple} dB')
    ax_inset.set_xlim(0, 1)
    ax_inset.set_ylim(0, max(0.6, 0.5 + 0.1))
    ax_inset.grid(True, alpha=0.3)
    ax_inset.set_title('Passband ripple (zoom)')

    path = os.path.join(OUT, "ch07_demo3_chebyshev.png")
    fig.savefig(path, dpi=120, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {path}\n")
    return g3_05


# ============================================================
# Demo 4: Filter Transformations (LP → BP / HP / BS)
# ============================================================
def demo_filter_transforms():
    """
    Demonstrate low-pass to bandpass / high-pass / bandstop
    frequency transformations on a prototype response.
    """
    print("=" * 60)
    print("Demo 4: Filter Transformations (LP → BP / HP / BS)")
    print("=" * 60)

    # Prototype: Butterworth N=5
    N = 5
    omega_n = np.linspace(0, 3, 2000)
    _, p_lr = butterworth_response(butterworth_g(N), omega_n)
    il_lp = 10 * np.log10(p_lr)

    # Design parameters
    fc = 1.0   # normalized cutoff
    f0 = 2.0   # BP center frequency
    delta = 0.4  # fractional bandwidth

    # Frequency mapping:
    # LP (Ω) → BP (ω):  Ω → (ω₀/Δ)(ω/ω₀ - ω₀/ω)
    # LP (Ω) → HP (ω):  Ω → -ω_c/ω
    # LP (Ω) → BS (ω):  Ω → -(Δ ω₀) / (ω/ω₀ - ω₀/ω)

    f_bp = np.linspace(0.5 * f0, 2.0 * f0, 5000)

    # Bandpass mapping: transform frequency axis
    Omega_bp = (f0 / delta) * (f_bp / f0 - f0 / f_bp)
    Omega_bp_abs = np.abs(Omega_bp)

    # Compute IL at mapped frequencies (interpolation)
    il_bp = np.interp(Omega_bp_abs, omega_n, il_lp)

    # High-pass
    f_hp = np.linspace(0.1, 3, 2000)
    Omega_hp = -fc / f_hp
    Omega_hp_abs = np.abs(Omega_hp)
    il_hp = np.interp(Omega_hp_abs, omega_n, il_lp)

    # Bandstop
    # Ω = -(Δ ω₀) / (ω/ω₀ - ω₀/ω)
    omega_bs = f_bp.copy()
    Omega_bs = -(delta * f0) / (omega_bs / f0 - f0 / omega_bs)
    Omega_bs_abs = np.abs(Omega_bs)
    il_bs = np.interp(Omega_bs_abs, omega_n, il_lp)

    # Plot
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    ax = axes[0, 0]
    ax.plot(omega_n, il_lp, 'b-')
    ax.axvline(fc, color='gray', ls='--')
    ax.set_xlabel(r'Normalized frequency $\Omega$')
    ax.set_ylabel('Insertion Loss (dB)')
    ax.set_title('Low-Pass Prototype')
    ax.set_ylim(0, 40)
    ax.grid(True, alpha=0.3)

    ax = axes[0, 1]
    ax.plot(f_bp, il_bp, 'r-')
    ax.axvline(f0 * (1 - delta / 2), color='gray', ls='--', alpha=0.5)
    ax.axvline(f0 * (1 + delta / 2), color='gray', ls='--', alpha=0.5)
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Insertion Loss (dB)')
    ax.set_title(f'Bandpass ($f_0={f0}$, Delta={delta})')
    ax.set_ylim(0, 40)
    ax.grid(True, alpha=0.3)

    ax = axes[1, 0]
    ax.plot(f_hp, il_hp, 'g-')
    ax.axvline(fc, color='gray', ls='--')
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Insertion Loss (dB)')
    ax.set_title(f'High-Pass ($f_c={fc}$)')
    ax.set_ylim(0, 40)
    ax.grid(True, alpha=0.3)

    ax = axes[1, 1]
    ax.plot(omega_bs, il_bs, 'm-')
    ax.axvline(f0 * (1 - delta / 2), color='gray', ls='--', alpha=0.5)
    ax.axvline(f0 * (1 + delta / 2), color='gray', ls='--', alpha=0.5)
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Insertion Loss (dB)')
    ax.set_title(f'Bandstop ($f_0={f0}$, Delta={delta})')
    ax.set_ylim(0, 40)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(OUT, "ch07_demo4_filter_transforms.png")
    fig.savefig(path, dpi=120, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {path}\n")


# ============================================================
# Demo 5: Stepped-Impedance Low-Pass Filter Design
# ============================================================
def demo_stepped_impedance_lpf():
    """
    Design a stepped-impedance low-pass filter using the g-values
    from a Chebyshev prototype. Calculate physical lengths of
    high/low impedance line sections.
    """
    print("=" * 60)
    print("Demo 5: Stepped-Impedance Low-Pass Filter Design")
    print("=" * 60)

    # Design specs
    fc = 2.0e9        # cutoff = 2 GHz
    N = 5
    ripple_db = 0.5
    Z0 = 50.0         # reference impedance
    Zh = 120.0        # high impedance (inductive sections)
    Zl = 15.0         # low impedance (capacitive sections)

    # Substrate parameters (microstrip)
    eps_r = 4.5       # FR-4 like
    c0 = 3e8
    vp = c0 / np.sqrt(eps_r)

    g = chebyshev_g(N, ripple_db)
    print(f"  Prototype g-values (N={N}, ripple={ripple_db} dB):")
    for i in range(N + 2):
        print(f"    g[{i}] = {g[i]:.6f}")

    # Inductive sections (series) → high-Z lines
    L_vals = []
    l_inductive = []
    for k in range(1, N + 1, 2):  # odd indices = series inductors
        L = g[k] * Z0 / (2 * np.pi * fc)
        L_vals.append(L)
        # Electrical length
        beta_l = L * vp / Zh  # rad
        l_inductive.append(beta_l * vp / (2 * np.pi * fc))

    # Capacitive sections (shunt) → low-Z lines
    C_vals = []
    l_capacitive = []
    for k in range(2, N + 1, 2):  # even indices = shunt capacitors
        C = g[k] / (Z0 * 2 * np.pi * fc)
        C_vals.append(C)
        # Electrical length
        beta_l = C * Zl * vp
        l_capacitive.append(beta_l * vp / (2 * np.pi * fc))

    # For N=5, sections: L1-C2-L3-C4-L5
    print(f"\n  Component values:")
    for i, L in enumerate(L_vals):
        idx = 2 * i + 1
        print(f"    L{idx} = {L*1e9:.3f} nH  →  high-Z line (Zh={Zh:.0f} Ω): "
              f"βl = {l_inductive[i]/vp*2*np.pi*fc:.4f} rad, "
              f"l = {l_inductive[i]*1e3:.2f} mm")

    for i, C in enumerate(C_vals):
        idx = 2 * i + 2
        print(f"    C{idx} = {C*1e12:.3f} pF  →  low-Z line (Zl={Zl:.0f} Ω): "
              f"βl = {l_capacitive[i]/vp*2*np.pi*fc:.4f} rad, "
              f"l = {l_capacitive[i]*1e3:.2f} mm")

    # Plot the ideal transmission line model (ABCD cascade)
    # Construct the filter response via ABCD matrices
    f_sweep = np.linspace(0.1e9, 5e9, 1000)
    omega = 2 * np.pi * f_sweep
    s11_dB = np.zeros_like(f_sweep)
    s21_dB = np.zeros_like(f_sweep)

    for idx, f0_ in enumerate(f_sweep):
        w = omega[idx]
        # Build cascade ABCD
        T_total = np.eye(2)
        for k in range(1, N + 1):
            if k % 2 == 1:  # series inductor
                jXL = 1j * w * L_vals[(k - 1) // 2]
                # Series ABCD: [1, jXL; 0, 1]
                Tk = np.array([[1.0, jXL], [0.0, 1.0]], dtype=complex)
            else:  # shunt capacitor
                jBC = 1j * w * C_vals[(k // 2) - 1]
                # Shunt ABCD: [1, 0; jBC, 1]
                Tk = np.array([[1.0, 0.0], [jBC, 1.0]], dtype=complex)
            T_total = T_total @ Tk

        # Convert ABCD to S-parameters (Z0-terminated)
        A = T_total[0, 0]
        B = T_total[0, 1]
        C = T_total[1, 0]
        D = T_total[1, 1]

        # S11
        num = A + B / Z0 - C * Z0 - D
        den = A + B / Z0 + C * Z0 + D
        s11 = num / den
        s21 = 2.0 / (A + B / Z0 + C * Z0 + D)

        s11_dB[idx] = 20 * np.log10(np.abs(s11) + 1e-15)
        s21_dB[idx] = 20 * np.log10(np.abs(s21) + 1e-15)

    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    ax.plot(f_sweep / 1e9, s21_dB, 'b-', label='$S_{21}$ (Insertion Loss)')
    ax.plot(f_sweep / 1e9, s11_dB, 'r-', label='$S_{11}$ (Return Loss)')
    ax.axvline(fc / 1e9, color='gray', ls='--', label=f'$f_c={fc/1e9:.1f}$ GHz')
    ax.set_xlabel('Frequency (GHz)')
    ax.set_ylabel('|S| (dB)')
    ax.set_title(f'Stepped-Impedance LPF Response (N={N}, {ripple_db} dB ripple)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-40, 2)

    path = os.path.join(OUT, "ch07_demo5_stepped_imp_lpf.png")
    fig.savefig(path, dpi=120, bbox_inches='tight')
    plt.close(fig)
    print(f"\n  Saved: {path}\n")


# ============================================================
# Demo 6: Coupled-Line Bandpass Filter Design
# ============================================================
def demo_coupled_line_bpf():
    """
    Design a microstrip parallel-coupled λ/4 resonator bandpass filter.
    Uses Chebyshev prototype and J-inverter coupling coefficients.
    """
    print("=" * 60)
    print("Demo 6: Coupled-Line Bandpass Filter Design")
    print("=" * 60)

    # Design specs
    N = 3              # number of resonators
    ripple_db = 0.1    # passband ripple
    f0 = 5.0e9         # center frequency = 5 GHz
    delta = 0.1        # 10% fractional bandwidth
    Z0 = 50.0          # port impedance

    g = chebyshev_g(N, ripple_db)
    print(f"  Prototype g-values (N={N}, ripple={ripple_db} dB):")
    for i in range(N + 2):
        print(f"    g[{i}] = {g[i]:.6f}")

    # J-inverter parameters (Collin Eqs. 8.x, p. 626+)
    J = np.zeros(N + 1)

    # End sections
    J[0] = np.sqrt(np.pi * delta / (2.0 * g[0] * g[1]))
    J[N] = np.sqrt(np.pi * delta / (2.0 * g[N] * g[N + 1]))

    # Internal couplings
    for i in range(1, N):
        J[i] = (np.pi * delta / 2.0) * (1.0 / np.sqrt(g[i] * g[i + 1]))

    print(f"\n  J-inverter values:")
    for i in range(N + 1):
        print(f"    J[{i},{i+1}] = {J[i]:.6f}")

    # Even/odd-mode impedances for each coupling section
    Z0e = np.zeros(N + 1)
    Z0o = np.zeros(N + 1)

    for i in range(N + 1):
        J_norm = J[i] * Z0
        Z0e[i] = Z0 * (1.0 + J_norm + J_norm ** 2)
        Z0o[i] = Z0 * (1.0 - J_norm + J_norm ** 2)

    print(f"\n  Even/Odd-mode impedances:")
    for i in range(N + 1):
        print(f"    Section {i}: Z0e={Z0e[i]:.2f} Ω, Z0o={Z0o[i]:.2f} Ω, "
              f"Coupling C={((Z0e[i]-Z0o[i])/(Z0e[i]+Z0o[i]))*100:.2f}%")

    # Synthesize physical dimensions for microstrip
    eps_r = 10.8   # alumina substrate
    h = 0.635e-3    # substrate height

    print(f"\n  Physical parameters (microstrip on εr={eps_r}, h={h*1e3:.2f} mm):")
    print(f"  (Note: full synthesis requires numerical solution of Z0e,Z0o → W,S)")
    print(f"  Using approximate parallel-coupled line formulas.")

    # Approximate synthesis: Using the relationships from Collin Ch3/App III
    def coupled_microstrip_dimensions(Z0e_val, Z0o_val, eps_r, h):
        """
        Approximate W/h and S/h from even/odd mode impedances.
        Simplified: assumes quasi-TEM, gives reasonable estimates.
        """
        Z0 = np.sqrt(Z0e_val * Z0o_val)
        # Single microstrip width estimate (Hammerstad)
        A = Z0 / 60.0 * np.sqrt((eps_r + 1) / 2.0) + (eps_r - 1) / (eps_r + 1) * (0.23 + 0.11 / eps_r)
        W_h = 8.0 * np.exp(A) / (np.exp(2 * A) - 2)

        # Approximate spacing from coupling coefficient
        C = (Z0e_val - Z0o_val) / (Z0e_val + Z0o_val)
        # Loose coupling: S/h ~ exp(-π/2 * (1/C - 1)) (approximate)
        S_h = max(0.05, np.exp(-np.pi / 2.0 * (1.0 / C - 1.0)))
        return W_h, S_h, Z0

    for i in range(N + 1):
        W_h, S_h, Zc = coupled_microstrip_dimensions(Z0e[i], Z0o[i], eps_r, h)
        print(f"    Section {i}: W/h={W_h:.3f}, S/h={S_h:.3f}, "
              f"W={W_h*h*1e3:.3f} mm, S={S_h*h*1e3:.3f} mm")

    # Plot synthesized filter response (ideal J-inverter model)
    # Simplified: use cascaded J-inverters and λ/4 lines
    f_sweep = np.linspace(4e9, 6e9, 2000)
    omega = 2 * np.pi * f_sweep
    beta = omega * np.sqrt(eps_r) / 3e8
    d = 3e8 / (4 * f0 * np.sqrt(eps_r))  # λ/4 at f0

    s21_dB = np.zeros_like(f_sweep)
    s11_dB = np.zeros_like(f_sweep)

    for idx, f_ in enumerate(f_sweep):
        beta_d = beta[idx] * d

        # Build cascaded ABCD: J01 - TL - J12 - TL - J23 - TL - J34
        # Where TL is a λ/4 line at f0
        # J-inverter ABCD = [0, -j/J; -jJ, 0]
        # TL ABCD = [cosθ, jZ0 sinθ; jY0 sinθ, cosθ]

        T_total = np.eye(2, dtype=complex)

        for stage in range(2 * N + 1):
            if stage % 2 == 0:  # J-inverter
                i_j = stage // 2
                J_inv = J[i_j]
                Tj = np.array([[0.0, -1j / J_inv], [-1j * J_inv, 0.0]], dtype=complex)
                T_total = T_total @ Tj
            else:  # λ/4 line (resonator)
                Tl = np.array([
                    [np.cos(beta_d), 1j * Z0 * np.sin(beta_d)],
                    [1j / Z0 * np.sin(beta_d), np.cos(beta_d)]
                ], dtype=complex)
                T_total = T_total @ Tl

        A = T_total[0, 0]
        B = T_total[0, 1]
        C = T_total[1, 0]
        D = T_total[1, 1]

        s11 = (A + B / Z0 - C * Z0 - D) / (A + B / Z0 + C * Z0 + D)
        s21 = 2.0 / (A + B / Z0 + C * Z0 + D)

        s11_dB[idx] = 20 * np.log10(np.abs(s11) + 1e-15)
        s21_dB[idx] = 20 * np.log10(np.abs(s21) + 1e-15)

    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    ax.plot(f_sweep / 1e9, s21_dB, 'b-', label='$S_{21}$ (Insertion Loss)')
    ax.plot(f_sweep / 1e9, s11_dB, 'r-', label='$S_{11}$ (Return Loss)')
    ax.axvline(f0 / 1e9, color='gray', ls='--', alpha=0.5, label=f'$f_0={f0/1e9:.1f}$ GHz')
    ax.set_xlabel('Frequency (GHz)')
    ax.set_ylabel('|S| (dB)')
    ax.set_title(f'Coupled-Line BPF Response (N={N}, Δ={delta*100:.0f}%, ripple={ripple_db} dB)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-40, 2)

    path = os.path.join(OUT, "ch07_demo6_coupled_bpf.png")
    fig.savefig(path, dpi=120, bbox_inches='tight')
    plt.close(fig)
    print(f"\n  Saved: {path}\n")


# ============================================================
# Verification Function
# ============================================================
def verify_collins_ch07():
    """
    Verify key prototype g-values from Collins Ch7.

    Known values:
      - Butterworth N=5: g0=1, g1=0.618, g2=1.618, g3=2.0, g4=1.618, g5=0.618, g6=1.0
      - Chebyshev 0.5dB N=3: g1=1.5963, g2=1.0967, g3=1.5963, g4=1.0
    """
    print("=" * 60)
    print("Verify: Collins Ch7 Prototype g-values")
    print("=" * 60)

    tol = 1e-4
    all_pass = True

    # ---- Butterworth N=5 ----
    expected_bw5 = [1.0, 0.618, 1.618, 2.0, 1.618, 0.618, 1.0]
    g_bw5 = butterworth_g(5)
    print(f"\n  Butterworth N=5:")
    for k in range(7):
        v = g_bw5[k]
        e = expected_bw5[k]
        ok = abs(v - e) < tol
        status = "✓" if ok else "✗"
        print(f"    g{k} = {v:.6f}  (expected {e})  {status}")
        if not ok:
            all_pass = False

    # ---- Chebyshev 0.5 dB N=3 ----
    expected_ch3 = [1.0, 1.5963, 1.0967, 1.5963, 1.0]
    g_ch3_05 = chebyshev_g(3, 0.5)
    print(f"\n  Chebyshev 0.5 dB N=3:")
    for k in range(5):
        v = g_ch3_05[k]
        e = expected_ch3[k]
        ok = abs(v - e) < tol
        status = "✓" if ok else "✗"
        print(f"    g{k} = {v:.6f}  (expected {e})  {status}")
        if not ok:
            all_pass = False

    # ---- Additional: Chebyshev 0.5 dB N=5 ----
    g_ch5_05 = chebyshev_g(5, 0.5)
    print(f"\n  Chebyshev 0.5 dB N=5:")
    for k in range(7):
        print(f"    g{k} = {g_ch5_05[k]:.6f}")

    # ---- Richardson ----
    print(f"\n  Summary:")
    if all_pass:
        print("  All verification tests PASSED ✓")
    else:
        print("  Some verification tests FAILED ✗")

    return all_pass


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("Collins Ch7 — Periodic Structures and Microwave Filters")
    print("Examples and Demonstrations\n")

    demo_periodic_dispersion()
    demo_butterworth()
    demo_chebyshev()
    demo_filter_transforms()
    demo_stepped_impedance_lpf()
    demo_coupled_line_bpf()

    print("\n" + "=" * 60)
    verify_collins_ch07()
    print("\nAll figures saved to:", OUT)
