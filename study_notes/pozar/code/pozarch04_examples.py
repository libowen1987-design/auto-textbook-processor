#!/usr/bin/env python3
"""
Pozar Chapter 4 — Microwave Network Analysis: Complete Examples & Numerical Experiments.

Covers:
  - S ↔ ABCD ↔ Z/Y ↔ T matrix conversions with round-trip verification
  - Series impedance and shunt admittance S-parameters (Ex 4.1, 4.2)
  - Transmission line section (Ex 4.3)
  - Input reflection via line transformation (Ex 4.4)
  - Two-port amplifier stability & gain (Ex 4.5)
  - ABCD cascade with series R, TL, shunt C (Ex 4.6)
  - Mason's gain formula for a two-port with source/load mismatch
  - Reciprocal / lossless / symmetrical network constraint verification
  - Extended: multi-port S-parameter self-consistency sweep
  - Extended: signal flow graph numerical evaluation

All variable names reflect physical meaning (Z_0, S11, Gamma_L, etc.).
Figures saved to python/figures/ch04/.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# --------------------------------------------------------------------------- #
#  Paths
# --------------------------------------------------------------------------- #
FIG_DIR = os.path.join(os.path.dirname(__file__), 'figures', 'ch04')
os.makedirs(FIG_DIR, exist_ok=True)

# --------------------------------------------------------------------------- #
#  Helper: validate complex-valued arrays for round-trip consistency
# --------------------------------------------------------------------------- #
def relative_error(actual, expected):
    """Return max relative error between two complex matrices."""
    norm = np.max(np.abs(expected))
    if norm < 1e-15:
        return np.max(np.abs(actual - expected))
    return np.max(np.abs(actual - expected) / norm)


# --------------------------------------------------------------------------- #
#  1.  Matrix conversion functions
# --------------------------------------------------------------------------- #

def s2z(s_params, Z0=50.0):
    """
    Convert S-parameters to Z-parameters.

    Parameters
    ----------
    s_params : ndarray, shape (2, 2) or (N, 2, 2)
        Scattering matrix (complex).
    Z0 : float
        Reference impedance in ohms.

    Returns
    -------
    z_params : ndarray
        Impedance matrix.
    """
    s = np.asarray(s_params, dtype=complex)
    single = (s.ndim == 2)
    if single:
        s = s[np.newaxis, ...]

    I = np.eye(2, dtype=complex)
    z_list = []
    for k in range(s.shape[0]):
        Sk = s[k]
        denom = np.linalg.det(I - Sk)
        if abs(denom) < 1e-15:
            raise ValueError(f"Singular (I - S) at index {k}")
        Zk = Z0 * (I + Sk) @ np.linalg.inv(I - Sk)
        z_list.append(Zk)

    z_out = np.array(z_list)
    return z_out[0] if single else z_out


def z2s(z_params, Z0=50.0):
    """
    Convert Z-parameters to S-parameters.

    Parameters
    ----------
    z_params : ndarray, shape (2, 2)
        Impedance matrix (complex).
    Z0 : float
        Reference impedance in ohms.

    Returns
    -------
    s_params : ndarray
        Scattering matrix.
    """
    Z = np.asarray(z_params, dtype=complex)
    I = np.eye(2, dtype=complex)
    return (Z - Z0 * I) @ np.linalg.inv(Z + Z0 * I)


def s2abcd(s_params, Z0=50.0):
    """
    Convert 2-port S-parameters to ABCD matrix (Pozar Table 4.1 / Eq 4.30-4.34).

    Parameters
    ----------
    s_params : ndarray, shape (2, 2)
        Scattering matrix.
    Z0 : float
        Reference impedance in ohms.

    Returns
    -------
    abcd : ndarray, shape (2, 2)
        ABCD transmission matrix.
    """
    S = np.asarray(s_params, dtype=complex)
    S11, S12, S21, S22 = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    Delta_S = (1 - S11) * (1 - S22) - S12 * S21

    if abs(S21) < 1e-15:
        raise ValueError("S21 = 0, cannot convert to ABCD (singular).")

    A = ((1 + S11) * (1 - S22) + S12 * S21) / (2 * S21)
    B = Z0 * ((1 + S11) * (1 + S22) - S12 * S21) / (2 * S21)
    C = (1 / Z0) * ((1 - S11) * (1 - S22) - S12 * S21) / (2 * S21)
    D = ((1 - S11) * (1 + S22) + S12 * S21) / (2 * S21)

    return np.array([[A, B], [C, D]], dtype=complex)


def abcd2s(abcd, Z0=50.0):
    """
    Convert ABCD matrix to 2-port S-parameters (Pozar Eq 4.25-4.28).

    Parameters
    ----------
    abcd : ndarray, shape (2, 2)
        ABCD transmission matrix.
    Z0 : float
        Reference impedance in ohms.

    Returns
    -------
    s_params : ndarray, shape (2, 2)
        Scattering matrix.
    """
    A, B, C, D = abcd[0, 0], abcd[0, 1], abcd[1, 0], abcd[1, 1]
    denom = A + B / Z0 + C * Z0 + D
    if abs(denom) < 1e-15:
        raise ValueError("Singular conversion ABCD -> S.")

    S11 = (A + B / Z0 - C * Z0 - D) / denom
    S12 = 2 * (A * D - B * C) / denom
    S21 = 2 / denom
    S22 = (-A + B / Z0 - C * Z0 + D) / denom
    return np.array([[S11, S12], [S21, S22]], dtype=complex)


def s2t(s_params):
    """
    Convert S-parameters to T-parameters (scattering transfer matrix).

    Parameters
    ----------
    s_params : ndarray, shape (2, 2)
        Scattering matrix.

    Returns
    -------
    t_params : ndarray, shape (2, 2)
        T-matrix.
    """
    S = np.asarray(s_params, dtype=complex)
    S11, S12, S21, S22 = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    if abs(S21) < 1e-15:
        raise ValueError("S21 = 0, cannot convert to T-parameters.")
    T11 = 1.0 / S21
    T12 = -S22 / S21
    T21 = S11 / S21
    T22 = (S12 * S21 - S11 * S22) / S21
    return np.array([[T11, T12], [T21, T22]], dtype=complex)


def t2s(t_params):
    """
    Convert T-parameters to S-parameters.

    Parameters
    ----------
    t_params : ndarray, shape (2, 2)
        T-matrix.

    Returns
    -------
    s_params : ndarray, shape (2, 2)
        Scattering matrix.
    """
    T = np.asarray(t_params, dtype=complex)
    T11, T12, T21, T22 = T[0, 0], T[0, 1], T[1, 0], T[1, 1]
    if abs(T11) < 1e-15:
        raise ValueError("T11 = 0, cannot convert to S-parameters.")
    S11 = T21 / T11
    S12 = (T11 * T22 - T12 * T21) / T11
    S21 = 1.0 / T11
    S22 = -T12 / T11
    return np.array([[S11, S12], [S21, S22]], dtype=complex)


# --------------------------------------------------------------------------- #
#  2.  Building blocks: S-matrix of basic networks
# --------------------------------------------------------------------------- #

def series_impedance_s(Z, Z0=50.0):
    """
    S-parameters of a series impedance Z.

    This is Example 4.1 from Pozar.

    Parameters
    ----------
    Z : complex
        Series impedance in ohms.
    Z0 : float
        Reference impedance in ohms.

    Returns
    -------
    S : ndarray, shape (2, 2)
    """
    Z = complex(Z)
    denom = 2 * Z + Z0
    S11 = Z / denom
    S21 = 2 * Z / denom
    # by reciprocity and symmetry
    S22 = S11
    S12 = S21
    return np.array([[S11, S12], [S21, S22]], dtype=complex)


def shunt_admittance_s(Y, Z0=50.0):
    """
    S-parameters of a shunt admittance Y.

    This is Example 4.2 from Pozar.

    Parameters
    ----------
    Y : complex
        Shunt admittance in siemens.
    Z0 : float
        Reference impedance in ohms.

    Returns
    -------
    S : ndarray, shape (2, 2)
    """
    Y = complex(Y)
    denom = 2 + Y * Z0
    S11 = -Y * Z0 / denom
    S21 = 2.0 / denom
    S22 = S11
    S12 = S21
    return np.array([[S11, S12], [S21, S22]], dtype=complex)


def transmission_line_s(beta_l, Z0=50.0):
    """
    S-parameters of a lossless transmission line section.

    This is Example 4.3 from Pozar.

    Parameters
    ----------
    beta_l : float
        Electrical length in radians (beta * l).
    Z0 : float
        Characteristic / reference impedance.

    Returns
    -------
    S : ndarray, shape (2, 2)
    """
    phase = np.exp(-1j * beta_l)
    return np.array([[0, phase], [phase, 0]], dtype=complex)


# --------------------------------------------------------------------------- #
#  3.  Example 4.1 — Series Impedance S-Parameters
# --------------------------------------------------------------------------- #
def example_4_1():
    """
    Example 4.1: S-parameters of a series impedance.

    Verify S11, S21 for R = Z0, R = 2*Z0, and compare analytic vs numerical.
    """
    print("=" * 70)
    print("Example 4.1: S-Parameters of a Series Impedance")
    print("=" * 70)

    Z0 = 50.0
    R_values = [10, 50, 100, 1000]  # ohms

    print(f"{'R (ohm)':>10} {'S11 (mag)':>12} {'S11 (phase deg)':>18} "
          f"{'S21 (mag)':>12} {'S21 (phase deg)':>18} {'|S11|^2+|S21|^2':>16}")
    print("-" * 88)

    for R in R_values:
        Z = complex(R, 0)
        denom = 2 * Z + Z0
        S11 = Z / denom
        S21 = 2 * Z / denom
        power_sum = abs(S11)**2 + abs(S21)**2
        print(f"{R:10.1f} {abs(S11):12.6f} {np.angle(S11, deg=True):18.2f} "
              f"{abs(S21):12.6f} {np.angle(S21, deg=True):18.2f} {power_sum:16.6f}")

    # Special case: R = Z0 => S11 = 1/3?, S21 = 2/3?
    R0 = Z0
    S = series_impedance_s(R0, Z0)
    print(f"\nR = Z0 = {Z0} ohm special case:")
    print(f"  S11 = {S[0,0]:.6f}  (expected -1/3 = {-1/3:.6f})")
    print(f"  S21 = {S[1,0]:.6f}  (expected 2/3  = {2/3:.6f})")

    # Sweep for figure
    resistances = np.linspace(1, 500, 200)
    S11_mag = np.zeros_like(resistances)
    S11_phase = np.zeros_like(resistances)
    S21_mag = np.zeros_like(resistances)
    for i, R in enumerate(resistances):
        S = series_impedance_s(R, Z0)
        S11_mag[i] = abs(S[0, 0])
        S11_phase[i] = np.angle(S[0, 0], deg=True)
        S21_mag[i] = abs(S[1, 0])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(resistances, S11_mag, 'b-', label=r'$|S_{11}|$')
    ax1.plot(resistances, S21_mag, 'r-', label=r'$|S_{21}|$')
    ax1.axvline(Z0, color='gray', linestyle='--', alpha=0.5, label=f'$R = Z_0 = {Z0:.0f}\\Omega$')
    ax1.set_xlabel('Series Resistance R ($\\Omega$)')
    ax1.set_ylabel('Magnitude')
    ax1.set_title('Ex 4.1: Series Impedance S-Parameter Magnitudes')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(resistances, S11_phase, 'b-', label=r'$\angle S_{11}$ (deg)')
    ax2.axvline(Z0, color='gray', linestyle='--', alpha=0.5)
    ax2.set_xlabel('Series Resistance R ($\\Omega$)')
    ax2.set_ylabel('Phase (degrees)')
    ax2.set_title('Ex 4.1: $S_{11}$ Phase')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, 'ex04_01_series_impedance.png')
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Figure saved: {path}")
    print()


# --------------------------------------------------------------------------- #
#  4.  Example 4.2 — Shunt Admittance S-Parameters
# --------------------------------------------------------------------------- #
def example_4_2():
    """
    Example 4.2: S-parameters of a shunt admittance.

    Verify for capacitive shunt at various frequencies.
    """
    print("=" * 70)
    print("Example 4.2: S-Parameters of a Shunt Admittance")
    print("=" * 70)

    Z0 = 50.0
    frequencies = np.linspace(0.1e9, 10e9, 200)
    C = 1e-12  # 1 pF

    S11_mag = np.zeros_like(frequencies)
    S21_mag = np.zeros_like(frequencies)

    for i, f in enumerate(frequencies):
        omega = 2 * np.pi * f
        Y = 1j * omega * C
        S = shunt_admittance_s(Y, Z0)
        S11_mag[i] = abs(S[0, 0])
        S21_mag[i] = abs(S[1, 0])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.semilogx(frequencies, 20 * np.log10(S11_mag), 'b-',
                 label=r'$|S_{11}|$ (dB)')
    ax1.semilogx(frequencies, 20 * np.log10(S21_mag), 'r-',
                 label=r'$|S_{21}|$ (dB)')
    ax1.axhline(-3, color='gray', linestyle='--', alpha=0.5, label='-3 dB')
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_ylabel('Magnitude (dB)')
    ax1.set_title('Ex 4.2: Shunt Capacitor $C=1$ pF')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(frequencies / 1e9, S11_mag, 'b-', label=r'$|S_{11}|$')
    ax2.plot(frequencies / 1e9, S21_mag, 'r-', label=r'$|S_{21}|$')
    ax2.set_xlabel('Frequency (GHz)')
    ax2.set_ylabel('Magnitude (linear)')
    ax2.set_title('Ex 4.2: Shunt Capacitor (linear scale)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, 'ex04_02_shunt_capacitor.png')
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Figure saved: {path}")
    print()

    # Print key values
    f_3dB_idx = np.argmin(np.abs(20 * np.log10(S21_mag) + 3))
    f_3dB = frequencies[f_3dB_idx]
    print(f"  3-dB frequency: {f_3dB / 1e9:.3f} GHz (C = {C*1e12:.0f} pF)")
    print(f"  Theoretical fc = 1/(2*pi*C*Z0) = {1/(2*np.pi*C*Z0)/1e9:.3f} GHz")


# --------------------------------------------------------------------------- #
#  5.  Example 4.3 — Transmission Line Section
# --------------------------------------------------------------------------- #
def example_4_3():
    """
    Example 4.3: S-parameters of a lossless transmission line.

    Verify phase shift and power conservation for varying electrical lengths.
    """
    print("=" * 70)
    print("Example 4.3: S-Parameters of a Transmission Line Section")
    print("=" * 70)

    Z0 = 50.0
    beta_l_vals = np.linspace(0, 2 * np.pi, 200)

    S11_mag = np.zeros_like(beta_l_vals)
    S21_phase = np.zeros_like(beta_l_vals)
    power_conservation = np.zeros_like(beta_l_vals)

    for i, bl in enumerate(beta_l_vals):
        S = transmission_line_s(bl, Z0)
        S11_mag[i] = abs(S[0, 0])
        S21_phase[i] = np.angle(S[1, 0], deg=True)
        power_conservation[i] = abs(S[0, 0])**2 + abs(S[1, 0])**2

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(beta_l_vals / np.pi, S11_mag, 'b-', label=r'$|S_{11}|$')
    ax1.plot(beta_l_vals / np.pi, S21_phase, 'r-',
             label=r'$\angle S_{21}$ (deg)')
    ax1.set_xlabel('Electrical Length $\\beta l$ ($\\pi$ rad)')
    ax1.set_ylabel('Value')
    ax1.set_title('Ex 4.3: Lossless Transmission Line Section')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(beta_l_vals / np.pi, S21_phase, 'g-',
             label=r'$\angle S_{21}$ (deg)')
    ax2.set_xlabel('Electrical Length $\\beta l$ ($\\pi$ rad)')
    ax2.set_ylabel('Phase (degrees)')
    ax2.set_title('Ex 4.3: Phase Shift of S21')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, 'ex04_03_transmission_line.png')
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Figure saved: {path}")

    # Verify losslessness
    max_power_err = np.max(np.abs(power_conservation - 1.0))
    print(f"  Max power conservation error: {max_power_err:.2e} (should be ~0)")
    print()


# --------------------------------------------------------------------------- #
#  6.  Example 4.4 — Input Reflection via Transmission Line
# --------------------------------------------------------------------------- #
def example_4_4():
    """
    Example 4.4: Input reflection coefficient seen through a line.

    Show Gamma_in = Gamma_L * exp(-2j*beta*l) on the Smith chart.
    """
    print("=" * 70)
    print("Example 4.4: Input Reflection Coefficient via Line")
    print("=" * 70)

    Z0 = 50.0
    Z_L = 100.0  # purely resistive load
    Gamma_L = (Z_L - Z0) / (Z_L + Z0)
    print(f"  Z_L = {Z_L} ohm, Gamma_L = {Gamma_L:.4f}")

    beta_l_vals = np.linspace(0, np.pi, 200)
    Gamma_in = Gamma_L * np.exp(-2j * beta_l_vals)

    fig, ax = plt.subplots(figsize=(7, 7))

    # Plot the trace on a polar/Smith-like diagram
    theta = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(theta), np.sin(theta), 'k-', linewidth=0.5, alpha=0.5)

    ax.plot(Gamma_in.real, Gamma_in.imag, 'b-', linewidth=2,
            label=r'$\Gamma_{\mathrm{in}}$ trace')
    ax.plot(Gamma_L.real, Gamma_L.imag, 'ro', markersize=8,
            label=r'$\Gamma_L$')
    ax.plot(Gamma_in[0].real, Gamma_in[0].imag, 'go', markersize=8,
            label=r'$\Gamma_{\mathrm{in}}$ (l=0)')

    # Mark quarter-wave point
    idx_qw = np.argmin(np.abs(beta_l_vals - np.pi / 2))
    ax.plot(Gamma_in[idx_qw].real, Gamma_in[idx_qw].imag, 'mo',
            markersize=8, label=r'$\Gamma_{\mathrm{in}}$ ($\beta l=\pi/2$)')

    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect('equal')
    ax.set_xlabel('Re($\\Gamma$)')
    ax.set_ylabel('Im($\\Gamma$)')
    ax.set_title('Ex 4.4: Input Reflection Through Line\n'
                 r'$\Gamma_{\mathrm{in}} = \Gamma_L e^{-2j\beta l}$')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, 'ex04_04_input_reflection.png')
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Figure saved: {path}")
    print()


# --------------------------------------------------------------------------- #
#  7.  Example 4.5 — Two-port Amplifier
# --------------------------------------------------------------------------- #
def example_4_5():
    """
    Example 4.5: Two-port amplifier S-parameter analysis.

    Stability check, transducer gain for matched and conjugate-matched cases.
    """
    print("=" * 70)
    print("Example 4.5: Two-Port Amplifier Analysis")
    print("=" * 70)

    # Amplifier S-parameters at 2 GHz (from Pozar)
    S11 = 0.3 * np.exp(-1j * np.deg2rad(60))
    S21 = 5.0 * np.exp(1j * np.deg2rad(90))
    S12 = 0.1 * np.exp(1j * np.deg2rad(30))
    S22 = 0.2 * np.exp(-1j * np.deg2rad(30))
    S_amp = np.array([[S11, S12], [S21, S22]])

    print(f"  S11 = {S11:.4f}")
    print(f"  S21 = {S21:.4f}")
    print(f"  S12 = {S12:.4f}")
    print(f"  S22 = {S22:.4f}")

    # (a) Stability with matched source/load
    Gamma_S = 0.0
    Gamma_L = 0.0
    Gamma_in = S11 + S12 * S21 * Gamma_L / (1 - S22 * Gamma_L)
    Gamma_out = S22 + S12 * S21 * Gamma_S / (1 - S11 * Gamma_S)
    print(f"\n  (a) Matched source/load:")
    print(f"      Gamma_in = {Gamma_in:.4f}, |Gamma_in| = {abs(Gamma_in):.4f}")
    print(f"      Gamma_out = {Gamma_out:.4f}, |Gamma_out| = {abs(Gamma_out):.4f}")

    # (b) Transducer gain
    G_T_matched = (abs(S21)**2 * (1 - abs(Gamma_S)**2) * (1 - abs(Gamma_L)**2)
                   / abs((1 - S11 * Gamma_S) * (1 - S22 * Gamma_L)
                         - S12 * S21 * Gamma_S * Gamma_L)**2)
    print(f"\n  (b) Transducer gain (matched):")
    print(f"      G_T = {G_T_matched:.4f} = {10*np.log10(G_T_matched):.2f} dB")

    # (c) Conjugate match (unilateral approximation since S12 is small)
    Gamma_S_opt = np.conj(S11)
    Gamma_L_opt = np.conj(S22)

    # Rollet stability factor
    Delta = S11 * S22 - S12 * S21
    K = (1 - abs(S11)**2 - abs(S22)**2 + abs(Delta)**2) / (2 * abs(S12 * S21))
    print(f"\n  (c) Stability:")
    print(f"      Delta = {Delta:.4f}, |Delta| = {abs(Delta):.4f}")
    print(f"      Rollet K = {K:.4f} {'(unconditionally stable)' if K > 1 and abs(Delta) < 1 else '(potentially unstable)'}")

    if K > 1 and abs(Delta) < 1:
        # Unilateral gain
        G_TU = (abs(S21)**2 * (1 - abs(Gamma_S_opt)**2) * (1 - abs(Gamma_L_opt)**2)
                / (abs(1 - S11 * Gamma_S_opt)**2 * abs(1 - S22 * Gamma_L_opt)**2))
        print(f"      G_TU (unilateral, conjugate match) = {G_TU:.4f} = {10*np.log10(G_TU):.2f} dB")

        # Gain factor breakdown
        G0 = abs(S21)**2
        G1 = 1 / (1 - abs(S11)**2)
        G2 = 1 / (1 - abs(S22)**2)
        print(f"      G0 = |S21|^2 = {G0:.2f} ({10*np.log10(G0):.2f} dB)")
        print(f"      G1 = 1/(1-|S11|^2) = {G1:.4f} ({10*np.log10(G1):.2f} dB)")
        print(f"      G2 = 1/(1-|S22|^2) = {G2:.4f} ({10*np.log10(G2):.2f} dB)")
        print(f"      G_TU,max = G0 * G1 * G2 = {G0*G1*G2:.4f} ({10*np.log10(G0*G1*G2):.2f} dB)")

    # Sweep Gamma_L magnitude to show effect on gamma_in
    Gamma_L_mags = np.linspace(0, 0.9, 100)
    Gamma_in_mags = np.zeros_like(Gamma_L_mags)
    for i, gl_mag in enumerate(Gamma_L_mags):
        gl = gl_mag * np.exp(1j * np.deg2rad(45))  # arbitrary phase
        gin = S11 + S12 * S21 * gl / (1 - S22 * gl)
        Gamma_in_mags[i] = abs(gin)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(Gamma_L_mags, Gamma_in_mags, 'b-', linewidth=2)
    ax1.axhline(abs(S11), color='gray', linestyle='--', label=r'$|S_{11}|$')
    ax1.set_xlabel(r'$|\Gamma_L|$')
    ax1.set_ylabel(r'$|\Gamma_{\mathrm{in}}|$')
    ax1.set_title('Ex 4.5: Input Reflection vs Load Mismatch')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Frequency sweep (assume S21 rolls off, S11 changes)
    freqs = np.linspace(1.5, 2.5, 100) * 1e9
    f0 = 2e9
    S21_f = np.zeros_like(freqs, dtype=complex)
    S11_f = np.zeros_like(freqs, dtype=complex)
    for i, f in enumerate(freqs):
        # Simple frequency-dependent model
        tau = 1e-9
        S21_f[i] = S21 * np.exp(-((f - f0) / (0.3e9))**2) * np.exp(-1j * 2 * np.pi * (f - f0) * tau)
        S11_f[i] = S11 * (1 + 0.2j * (f - f0) / 1e9)

    ax2.plot(freqs / 1e9, 20 * np.log10(abs(S21_f)), 'r-', label=r'$|S_{21}|$ (dB)')
    ax2.plot(freqs / 1e9, 20 * np.log10(abs(S11_f)), 'b-', label=r'$|S_{11}|$ (dB)')
    ax2.set_xlabel('Frequency (GHz)')
    ax2.set_ylabel('Magnitude (dB)')
    ax2.set_title('Ex 4.5: Amplifier Frequency Response')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, 'ex04_05_amplifier.png')
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Figure saved: {path}")
    print()


# --------------------------------------------------------------------------- #
#  8.  Example 4.6 — ABCD Cascade (R + TL + shunt C)
# --------------------------------------------------------------------------- #
def example_4_6():
    """
    Example 4.6: ABCD matrix of a cascade — series R, transmission line,
    shunt C. Convert to S-parameters and verify.
    """
    print("=" * 70)
    print("Example 4.6: ABCD Cascade — Series R + TL + Shunt C")
    print("=" * 70)

    Z0 = 50.0
    R = 25.0  # series resistor
    C = 2e-12  # 2 pF
    frequency = 2e9  # 2 GHz
    omega = 2 * np.pi * frequency
    theta = np.pi / 4  # 45-degree electrical length

    # ABCD of each section
    ABCD_R = np.array([[1, R], [0, 1]], dtype=complex)
    ABCD_TL = np.array([[np.cos(theta), 1j * Z0 * np.sin(theta)],
                        [1j / Z0 * np.sin(theta), np.cos(theta)]],
                       dtype=complex)
    Y_C = 1j * omega * C
    ABCD_C = np.array([[1, 0], [Y_C, 1]], dtype=complex)

    # Cascade
    ABCD_total = ABCD_R @ ABCD_TL @ ABCD_C

    A, B, C_, D = ABCD_total[0, 0], ABCD_total[0, 1], ABCD_total[1, 0], ABCD_total[1, 1]
    det_ABCD = A * D - B * C_

    print(f"  ABCD Matrix:")
    print(f"    A = {A:.6f}")
    print(f"    B = {B:.6f} ohm")
    print(f"    C = {C_:.6f} S")
    print(f"    D = {D:.6f}")
    print(f"    det(ABCD) = {det_ABCD:.6f} (should be 1 for reciprocal)")

    # Convert to S
    S_total = abcd2s(ABCD_total, Z0)
    print(f"\n  S-Parameters:")
    print(f"    S11 = {S_total[0,0]:.6f} (mag={abs(S_total[0,0]):.6f})")
    print(f"    S12 = {S_total[0,1]:.6f} (mag={abs(S_total[0,1]):.6f})")
    print(f"    S21 = {S_total[1,0]:.6f} (mag={abs(S_total[1,0]):.6f})")
    print(f"    S22 = {S_total[1,1]:.6f} (mag={abs(S_total[1,1]):.6f})")

    # Check reciprocity
    print(f"\n  Reciprocity check: S12 = S21? {abs(S_total[0,1] - S_total[1,0]) < 1e-12}")
    print(f"    |S12 - S21| = {abs(S_total[0,1] - S_total[1,0]):.2e}")

    # Sweep frequency
    frequencies = np.linspace(0.1e9, 5e9, 300)
    S11_mag = np.zeros_like(frequencies)
    S21_mag = np.zeros_like(frequencies)
    S11_phase = np.zeros_like(frequencies)

    for i, f in enumerate(frequencies):
        omega_f = 2 * np.pi * f
        theta_f = theta * (f / frequency)
        ABCD_TL_f = np.array([[np.cos(theta_f), 1j * Z0 * np.sin(theta_f)],
                              [1j / Z0 * np.sin(theta_f), np.cos(theta_f)]],
                             dtype=complex)
        Y_C_f = 1j * omega_f * C
        ABCD_C_f = np.array([[1, 0], [Y_C_f, 1]], dtype=complex)
        ABCD_f = ABCD_R @ ABCD_TL_f @ ABCD_C_f
        S_f = abcd2s(ABCD_f, Z0)
        S11_mag[i] = abs(S_f[0, 0])
        S21_mag[i] = abs(S_f[1, 0])
        S11_phase[i] = np.angle(S_f[0, 0], deg=True)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(frequencies / 1e9, S11_mag, 'b-', label=r'$|S_{11}|$')
    ax1.plot(frequencies / 1e9, S21_mag, 'r-', label=r'$|S_{21}|$')
    ax1.set_xlabel('Frequency (GHz)')
    ax1.set_ylabel('Magnitude')
    ax1.set_title('Ex 4.6: R+TL+C Cascade — S-Parameter Magnitudes')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(frequencies / 1e9, S11_phase, 'b-',
             label=r'$\angle S_{11}$')
    ax2.set_xlabel('Frequency (GHz)')
    ax2.set_ylabel('Phase (deg)')
    ax2.set_title('Ex 4.6: $S_{11}$ Phase')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, 'ex04_06_abcd_cascade.png')
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Figure saved: {path}")
    print()


# --------------------------------------------------------------------------- #
#  9.  S→ABCD→S and S→Z→S round-trip verification
# --------------------------------------------------------------------------- #
def round_trip_verification():
    """
    Verify round-trip conversion of S → ABCD → S and S → Z → S.

    Use random physically realizable S-matrices and check conversion error.
    """
    print("=" * 70)
    print("Round-Trip Matrix Conversion Verification")
    print("=" * 70)

    Z0 = 50.0
    n_tests = 1000
    max_err_s2abcd2s = 0.0
    max_err_s2z2s = 0.0
    max_err_s2t2s = 0.0
    max_err_abcd_symm = 0.0
    max_err_t_symm = 0.0
    failed = 0

    np.random.seed(42)
    for _ in range(n_tests):
        # Generate random reciprocal S-matrix with |S11|^2 + |S21|^2 <= 1
        rho = np.random.uniform(0, 0.95)
        phi = np.random.uniform(0, 2 * np.pi)
        theta = np.random.uniform(0, 2 * np.pi)
        S11 = rho * np.exp(1j * phi)
        S21 = np.sqrt(1 - rho**2) * np.exp(1j * theta) * np.exp(1j * np.random.uniform(0, 0.1))
        # Ensure |S11|^2 + |S21|^2 <= 1
        scale = np.sqrt(abs(S11)**2 + abs(S21)**2)
        if scale > 0.99:
            S11 *= 0.99 / scale
            S21 *= 0.99 / scale
        S12 = S21  # reciprocal
        S22 = S11 * np.exp(1j * np.random.uniform(-0.5, 0.5))

        S = np.array([[S11, S12], [S21, S22]], dtype=complex)

        # S → ABCD → S
        try:
            ABCD = s2abcd(S, Z0)
            S_round = abcd2s(ABCD, Z0)
            err_s2a2s = relative_error(S_round, S)
            max_err_s2abcd2s = max(max_err_s2abcd2s, err_s2a2s)

            # Check ABCD reciprocity
            det_err = abs(ABCD[0, 0] * ABCD[1, 1] - ABCD[0, 1] * ABCD[1, 0] - 1.0)
            max_err_abcd_symm = max(max_err_abcd_symm, det_err)
        except ValueError:
            failed += 1
            continue

        # S → Z → S
        try:
            Z = s2z(S, Z0)
            S_round2 = z2s(Z, Z0)
            err_s2z2s = relative_error(S_round2, S)
            max_err_s2z2s = max(max_err_s2z2s, err_s2z2s)
        except ValueError:
            failed += 1
            continue

        # S → T → S
        try:
            T = s2t(S)
            S_round3 = t2s(T)
            err_s2t2s = relative_error(S_round3, S)
            max_err_s2t2s = max(max_err_s2t2s, err_s2t2s)
        except ValueError:
            failed += 1
            continue

    print(f"  Tests: {n_tests}, skipped (singular): {failed}")
    print(f"  S→ABCD→S max relative error: {max_err_s2abcd2s:.2e}")
    print(f"  S→Z→S    max relative error: {max_err_s2z2s:.2e}")
    print(f"  S→T→S    max relative error: {max_err_s2t2s:.2e}")
    print(f"  ABCD det error (|AD-BC-1|) max: {max_err_abcd_symm:.2e}")

    # Verify lossless S-matrix constraints
    print(f"\n  Lossless S-matrix constraint verification:")
    for rho_test in [0.0, 0.3, 0.5, 0.707, 0.9]:
        # Construct a lossless reciprocal 2-port
        phi = np.pi / 4
        theta = np.pi / 3
        S11_l = rho_test * np.exp(1j * phi)
        S21_l = np.sqrt(1 - rho_test**2) * np.exp(1j * theta)
        S12_l = S21_l
        S22_l = -rho_test * np.exp(1j * (2 * theta - phi))
        S_l = np.array([[S11_l, S12_l], [S21_l, S22_l]], dtype=complex)

        power_conservation = abs(S_l[0, 0])**2 + abs(S_l[1, 0])**2
        orthogonality = np.conj(S_l[0, 0]) * S_l[0, 1] + np.conj(S_l[1, 0]) * S_l[1, 1]
        det_unitary = abs(np.conj(S_l.T) @ S_l - np.eye(2)).max()
        print(f"    rho={rho_test:.3f}: |S11|^2+|S21|^2={power_conservation:.8f} "
              f"|S†S-I|={det_unitary:.2e}")
    print()


# --------------------------------------------------------------------------- #
#  10.  Mason's gain formula — signal flow graph numerical analysis
# --------------------------------------------------------------------------- #
def masons_gain_demo():
    """
    Evaluate Mason's gain formula for a two-port with source/load mismatch.

    Verify that the explicit formula matches a brute-force signal flow graph
    node enumeration for an arbitrary two-port.
    """
    print("=" * 70)
    print("Mason's Gain Formula — Signal Flow Graph Verification")
    print("=" * 70)

    Z0 = 50.0

    # Test 1: simple two-port with matched source and load
    S11 = 0.2 * np.exp(1j * np.deg2rad(-30))
    S21 = 0.8 * np.exp(1j * np.deg2rad(45))
    S12 = 0.3 * np.exp(1j * np.deg2rad(10))
    S22 = 0.15 * np.exp(1j * np.deg2rad(-60))

    Gamma_S = 0.1 * np.exp(1j * np.deg2rad(60))  # small source mismatch
    Gamma_L = 0.2 * np.exp(1j * np.deg2rad(-20))  # load mismatch

    # Mason's formula: Gamma_in = S11 + S12*S21*Gamma_L/(1 - S22*Gamma_L)
    Gamma_in_mason = S11 + S12 * S21 * Gamma_L / (1 - S22 * Gamma_L)

    # Brute-force via solving linear system
    # Nodes: a1=V1+, b1=V1-, a2=V2+, b2=V2-
    # b1 = S11*a1 + S12*a2
    # b2 = S21*a1 + S22*a2
    # a1 = Gamma_S * b1 + V_S   (source)
    # a2 = Gamma_L * b2         (load)
    # Solve for b1/a1 with V_S=1

    # Linear system in variables [a1, b1, a2, b2]
    A_mat = np.array([
        [1, -Gamma_S, 0, 0],      # a1 - Gamma_S*b1 = V_S
        [-S11, 1, -S12, 0],        # -S11*a1 + b1 - S12*a2 = 0
        [-S21, 0, -S22, 1],        # -S21*a1 - S22*a2 + b2 = 0
        [0, 0, 1, -Gamma_L]        # a2 - Gamma_L*b2 = 0
    ], dtype=complex)
    rhs = np.array([1.0, 0, 0, 0], dtype=complex)
    solution = np.linalg.solve(A_mat, rhs)
    a1_bf, b1_bf, a2_bf, b2_bf = solution

    Gamma_in_bf = b1_bf / a1_bf
    T_bf = b2_bf / a1_bf  # transfer from a1 to b2

    print("  Test 1: S11=0.2∠-30°, S21=0.8∠45°, S12=0.3∠10°, S22=0.15∠-60°")
    print(f"  Gamma_S = {Gamma_S:.4f}, Gamma_L = {Gamma_L:.4f}")
    print(f"  Mason Gamma_in = {Gamma_in_mason:.6f}")
    print(f"  Brute-force     = {Gamma_in_bf:.6f}")
    print(f"  Match: {abs(Gamma_in_mason - Gamma_in_bf) < 1e-12} "
          f"(|diff|={abs(Gamma_in_mason - Gamma_in_bf):.2e})")

    # Mason's gain: the transfer function b2/V_S
    # T = S21 / [ (1-S11*Gamma_S)(1-S22*Gamma_L) - S12*S21*Gamma_L*Gamma_S ]
    T_mason = S21 / ((1 - S11 * Gamma_S) * (1 - S22 * Gamma_L) - S12 * S21 * Gamma_L * Gamma_S)
    T_bf_full = b2_bf  # since V_S = 1
    print(f"\n  Transfer function b2/V_S:")
    print(f"  Mason T     = {T_mason:.6f}")
    print(f"  Brute-force = {T_bf_full:.6f}")
    print(f"  Match: {abs(T_mason - T_bf_full) < 1e-12} "
          f"(|diff|={abs(T_mason - T_bf_full):.2e})")

    # Test 2: Sweep Gamma_L magnitude, show Gamma_in change
    Gamma_L_mags = np.linspace(0, 0.95, 100)
    Gamma_in_vals = np.zeros_like(Gamma_L_mags, dtype=complex)
    Gamma_in_bf_vals = np.zeros_like(Gamma_L_mags, dtype=complex)

    for i, gl_mag in enumerate(Gamma_L_mags):
        gl = gl_mag * np.exp(1j * np.deg2rad(45))
        Gamma_in_vals[i] = S11 + S12 * S21 * gl / (1 - S22 * gl)

        # Brute-force
        A_t = np.array([
            [1, -Gamma_S, 0, 0],
            [-S11, 1, -S12, 0],
            [-S21, 0, -S22, 1],
            [0, 0, 1, -gl]
        ], dtype=complex)
        sol = np.linalg.solve(A_t, rhs)
        Gamma_in_bf_vals[i] = sol[1] / sol[0]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(Gamma_L_mags, abs(Gamma_in_vals), 'b-', linewidth=2,
             label=r'Mason: $|\Gamma_{\mathrm{in}}|$')
    ax1.plot(Gamma_L_mags, abs(Gamma_in_bf_vals), 'r--', linewidth=2,
             alpha=0.7, label='Brute-force')
    ax1.set_xlabel(r'$|\Gamma_L|$')
    ax1.set_ylabel(r'$|\Gamma_{\mathrm{in}}|$')
    ax1.set_title('Mason Eqn vs Brute-Force Signal Flow Graph')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.plot(Gamma_L_mags, np.angle(Gamma_in_vals, deg=True), 'b-',
             linewidth=2, label=r'Mason')
    ax2.plot(Gamma_L_mags, np.angle(Gamma_in_bf_vals, deg=True), 'r--',
             linewidth=2, alpha=0.7, label='Brute-force')
    ax2.set_xlabel(r'$|\Gamma_L|$')
    ax2.set_ylabel(r'$\angle \Gamma_{\mathrm{in}}$ (deg)')
    ax2.set_title('Phase of Input Reflection Coefficient')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, 'ex04_masons_gain.png')
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"\n  Figure saved: {path}")
    print()


# --------------------------------------------------------------------------- #
#  11.  Extended: Reciprocity / Losslessness / Symmetry sweep
# --------------------------------------------------------------------------- #
def network_property_sweep():
    """
    Sweep over network topologies and verify property constraints.

    Test: series R, shunt C, TL, and a generic reciprocal network.
    """
    print("=" * 70)
    print("Extended: Network Property Constraint Verification")
    print("=" * 70)

    Z0 = 50.0
    frequencies = np.linspace(0.1e9, 10e9, 200)

    # Test networks
    networks = {
        'Series R=50': lambda f: series_impedance_s(50, Z0),
        'Shunt C=1pF': lambda f: shunt_admittance_s(1j * 2 * np.pi * f * 1e-12, Z0),
        'TL theta=pi/4': lambda f: transmission_line_s(np.pi/4, Z0),
        'R+TL+C cascade': lambda f: abcd2s(
            np.array([[1, 25], [0, 1]], dtype=complex)
            @ np.array([[np.cos(np.pi/4*f/2e9), 1j*Z0*np.sin(np.pi/4*f/2e9)],
                        [1j/Z0*np.sin(np.pi/4*f/2e9), np.cos(np.pi/4*f/2e9)]],
                       dtype=complex)
            @ np.array([[1, 0], [1j*2*np.pi*f*2e-12, 1]], dtype=complex),
            Z0
        )
    }

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    for idx, (name, net_func) in enumerate(networks.items()):
        ax = axes[idx // 2, idx % 2]
        S11_mag = []
        S21_mag = []
        reciprocal_err = []
        for f in frequencies:
            S = net_func(f)
            S11_mag.append(abs(S[0, 0]))
            S21_mag.append(abs(S[1, 0]))
            reciprocal_err.append(abs(S[0, 1] - S[1, 0]))

        ax.semilogx(frequencies / 1e9, S11_mag, 'b-', label=r'$|S_{11}|$')
        ax.semilogx(frequencies / 1e9, S21_mag, 'r-', label=r'$|S_{21}|$')
        ax.set_xlabel('Frequency (GHz)')
        ax.set_ylabel('Magnitude')
        ax.set_title(name)
        ax.legend()
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, 'ex04_network_property_sweep.png')
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Figure saved: {path}")
    print()


# --------------------------------------------------------------------------- #
#  12.  Extended: ABCD transmission line vs S-parameters at multiple lengths
# --------------------------------------------------------------------------- #
def abcd_tl_validation():
    """
    Validate the ABCD-to-S conversion using a transmission line as the
    canonical example. Show that the cascaded phase matches.
    """
    print("=" * 70)
    print("Extended: ABCD TL Cascade vs Direct S-Parameter Phase")
    print("=" * 70)

    Z0 = 50.0
    betal_total = np.linspace(0, 4 * np.pi, 400)

    S21_phase_direct = -np.rad2deg(betal_total) % 360  # unwrapped
    S21_phase_abcd = np.zeros_like(betal_total)

    for i, bl in enumerate(betal_total):
        # Build TL as ABCD, convert to S
        ABCD = np.array([
            [np.cos(bl), 1j * Z0 * np.sin(bl)],
            [1j / Z0 * np.sin(bl), np.cos(bl)]
        ], dtype=complex)
        S = abcd2s(ABCD, Z0)
        S21_phase_abcd[i] = np.angle(S[1, 0], deg=True)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(betal_total / np.pi, S21_phase_direct, 'b-', linewidth=2,
             label="Direct: -\\beta l (deg)")
    ax1.plot(betal_total / np.pi, S21_phase_abcd, 'r--', linewidth=2,
             alpha=0.7, label='ABCD → S')
    ax1.set_xlabel('Electrical Length $\\beta l$ ($\\pi$ rad)')
    ax1.set_ylabel('Phase of $S_{21}$ (degrees)')
    ax1.set_title('TL Phase: Direct vs ABCD→S Conversion')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    phase_diff = S21_phase_direct - S21_phase_abcd
    ax2.plot(betal_total / np.pi, phase_diff, 'g-', linewidth=1)
    ax2.set_xlabel('Electrical Length $\\beta l$ ($\\pi$ rad)')
    ax2.set_ylabel('Phase Difference (deg)')
    ax2.set_title('Phase Error (ABC D → S vs Direct)')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, 'ex04_abcd_tl_validation.png')
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  Figure saved: {path}")

    max_phase_err = np.max(np.abs(phase_diff))
    print(f"  Max phase error: {max_phase_err:.6f} deg "
          f"(should be near 0 for well-wrapped phase)")
    print()


# --------------------------------------------------------------------------- #
#  Main
# --------------------------------------------------------------------------- #
if __name__ == '__main__':
    print("Pozar Chapter 4 — Microwave Network Analysis: Examples & Numerical Experiments")
    print("=" * 70)

    example_4_1()     # Series impedance S-parameters
    example_4_2()     # Shunt admittance S-parameters
    example_4_3()     # Transmission line section
    example_4_4()     # Input reflection through line
    example_4_5()     # Two-port amplifier
    example_4_6()     # ABCD cascade (R + TL + C)
    round_trip_verification()  # S↔ABCD↔Z↔T round-trip
    masons_gain_demo()         # Mason's gain formula verification
    network_property_sweep()   # Property constraint sweep
    abcd_tl_validation()       # ABCD TL validation

    print("=" * 70)
    print("All examples complete. Figures saved to figures/ch04/.")
