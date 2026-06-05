#!/usr/bin/env python3
"""
Pozar Ch13 (4e Ch10) — Noise & Nonlinear Distortion
========================================================
Comprehensive example code covering:
  10.1 Noise (thermal noise, noise figure, noise temp, Friis cascade,
              two-port NF, minimum NF, optimum source impedance)
  10.2 Nonlinear distortion (gain compression, harmonic distortion,
              intermodulation, IIP3/OIP3, cross modulation)
  10.3 Dynamic range (linear DR, SFDR, receiver DR considerations)

All variables follow physical-meaning naming conventions.
Figures saved to: figures/ch13/
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Optional
import os

# ---------- Physical Constants ----------
C0: float = 2.998e8           # Speed of light [m/s]
K_B: float = 1.380649e-23     # Boltzmann constant [J/K]
ETA_0: float = 376.7303       # Free-space impedance [Ohm]
T0: float = 290.0             # Standard noise temperature [K]

# Output directory
FIG_DIR = os.path.join(os.path.dirname(__file__), "figures", "ch13")
os.makedirs(FIG_DIR, exist_ok=True)


# ============================================================
# §10.1 — NOISE
# ============================================================

def thermal_noise_power(T: float, B: float) -> float:
    """
    Available thermal noise power from a matched termination.

    P_n = k * T * B

    Parameters
    ----------
    T : float
        Physical temperature [K].
    B : float
        Bandwidth [Hz].

    Returns
    -------
    P_n : float
        Available noise power [W].
    """
    return K_B * T * B


def thermal_noise_power_dbm(T: float, B: float) -> float:
    """
    Thermal noise power in dBm.

    Parameters
    ----------
    T : float
        Physical temperature [K].
    B : float
        Bandwidth [Hz].

    Returns
    -------
    P_n_dbm : float
        Noise power [dBm].
    """
    return 10.0 * np.log10(thermal_noise_power(T, B) * 1000.0)


def noise_power_density_dbm_per_hz(T: float) -> float:
    """
    Noise power spectral density in dBm/Hz.

    N_0 = 10*log10(kT * 1000) [dBm/Hz]
    At T0=290K: N_0 = -174 dBm/Hz.

    Parameters
    ----------
    T : float
        Temperature [K].

    Returns
    -------
    N_0_dbm_hz : float
        Noise PSD [dBm/Hz].
    """
    return 10.0 * np.log10(K_B * T * 1000.0)


def noise_figure_to_noise_temp(F_linear: float) -> float:
    """
    Convert noise figure (linear) to equivalent noise temperature.

    T_e = (F - 1) * T0

    Parameters
    ----------
    F_linear : float
        Noise figure (linear ratio), F >= 1.

    Returns
    -------
    T_e : float
        Equivalent noise temperature [K].
    """
    return (F_linear - 1.0) * T0


def noise_temp_to_noise_figure(T_e: float) -> float:
    """
    Convert equivalent noise temperature to noise figure (linear).

    F = 1 + T_e / T0

    Parameters
    ----------
    T_e : float
        Equivalent noise temperature [K].

    Returns
    -------
    F_linear : float
        Noise figure (linear ratio).
    """
    return 1.0 + T_e / T0


def db_to_linear(x_db: np.ndarray) -> np.ndarray:
    """Convert dB to linear."""
    return 10.0 ** (x_db / 10.0)


def linear_to_db(x_lin: np.ndarray) -> np.ndarray:
    """Convert linear to dB."""
    return 10.0 * np.log10(x_lin)


def cascaded_noise_figure(F_db: np.ndarray, G_db: np.ndarray) -> float:
    """
    Total noise figure of a cascaded system (Friis formula).

    F_total = F1 + (F2-1)/G1 + (F3-1)/(G1*G2) + ...

    Parameters
    ----------
    F_db : np.ndarray
        Noise figures of each stage [dB].
    G_db : np.ndarray
        Gains of each stage [dB].

    Returns
    -------
    F_total_db : float
        Total noise figure [dB].
    """
    F_lin = db_to_linear(F_db)
    G_lin = db_to_linear(G_db)
    F_total: float = F_lin[0]
    G_cum: float = G_lin[0]
    for i in range(1, len(F_lin)):
        F_total += (F_lin[i] - 1.0) / G_cum
        G_cum *= G_lin[i]
    return linear_to_db(F_total)


def passive_loss_noise_figure(L_db: float) -> float:
    """
    Noise figure of a passive lossy component.

    For a matched passive component at thermal equilibrium,
    F (linear) = L (linear), i.e. F_dB = L_dB.

    Parameters
    ----------
    L_db : float
        Loss [dB] (positive).

    Returns
    -------
    F_db : float
        Noise figure [dB], equal to L_db.
    """
    return L_db


def two_port_noise_figure(F_min_db: float, R_n: float, G_s: float,
                          B_s: float, G_opt: float, B_opt: float) -> float:
    """
    Noise figure of a two-port as function of source admittance.

    F(Y_s) = F_min + (R_n / G_s) * |Y_s - Y_opt|^2

    Parameters
    ----------
    F_min_db : float
        Minimum noise figure [dB].
    R_n : float
        Equivalent noise resistance [Ohm].
    G_s : float
        Source conductance [S].
    B_s : float
        Source susceptance [S].
    G_opt : float
        Optimum source conductance [S].
    B_opt : float
        Optimum source susceptance [S].

    Returns
    -------
    F_db : float
        Noise figure at given source admittance [dB].
    """
    F_min_lin = db_to_linear(F_min_db)
    Y_s_minus_Y_opt_mag2 = (G_s - G_opt) ** 2 + (B_s - B_opt) ** 2
    F_lin = F_min_lin + (R_n / G_s) * Y_s_minus_Y_opt_mag2
    return linear_to_db(F_lin)


def noise_figure_from_reflection_coefficient(
    F_min_db: float,
    R_n: float,
    Gamma_s_mag: float,
    Gamma_s_phase_deg: float,
    Gamma_opt_mag: float,
    Gamma_opt_phase_deg: float,
    Z0: float = 50.0
) -> float:
    """
    Noise figure from source reflection coefficient (smith-chart form).

    F = F_min + (4*R_n/Z0) * |Gamma_s - Gamma_opt|^2
                  / ((1 - |Gamma_s|^2) * |1 + Gamma_opt|^2)

    Parameters
    ----------
    F_min_db : float
        Minimum noise figure [dB].
    R_n : float
        Equivalent noise resistance [Ohm].
    Gamma_s_mag : float
        Source reflection coefficient magnitude.
    Gamma_s_phase_deg : float
        Source reflection coefficient phase [deg].
    Gamma_opt_mag : float
        Optimum reflection coefficient magnitude.
    Gamma_opt_phase_deg : float
        Optimum reflection coefficient phase [deg].
    Z0 : float
        Reference impedance [Ohm], default 50.

    Returns
    -------
    F_db : float
        Noise figure at given Gamma_s [dB].
    """
    Gamma_s = Gamma_s_mag * np.exp(1j * np.deg2rad(Gamma_s_phase_deg))
    Gamma_opt = Gamma_opt_mag * np.exp(1j * np.deg2rad(Gamma_opt_phase_deg))
    F_min_lin = db_to_linear(F_min_db)
    num = (4.0 * R_n / Z0) * abs(Gamma_s - Gamma_opt) ** 2
    den = (1.0 - Gamma_s_mag ** 2) * abs(1.0 + Gamma_opt) ** 2
    F_lin = F_min_lin + num / den
    return linear_to_db(F_lin)


def system_noise_temperature(
    T_ant: float,
    F_db: np.ndarray,
    G_db: np.ndarray
) -> float:
    """
    System noise temperature referred to receiver input.

    T_sys = T_A + T_rec
    T_rec = Friis summation of stage noise temps.

    Parameters
    ----------
    T_ant : float
        Antenna noise temperature [K].
    F_db : np.ndarray
        Stage noise figures [dB].
    G_db : np.ndarray
        Stage gains [dB].

    Returns
    -------
    T_sys : float
        System noise temperature [K].
    """
    F_lin = db_to_linear(F_db)
    G_lin = db_to_linear(G_db)
    # First stage equivalent noise temp
    T_rec: float = noise_figure_to_noise_temp(F_lin[0])
    G_cum: float = G_lin[0]
    for i in range(1, len(F_lin)):
        T_rec += noise_figure_to_noise_temp(F_lin[i]) / G_cum
        G_cum *= G_lin[i]
    return T_ant + T_rec


# ============================================================
# §10.2 — NONLINEAR DISTORTION
# ============================================================

def power_series_output(
    a1: float, a2: float, a3: float,
    V0: float, omega: float, t: np.ndarray
) -> np.ndarray:
    """
    Memoryless nonlinear amplifier output for single-tone input.

    v_out = a1 * v_in + a2 * v_in^2 + a3 * v_in^3

    where v_in = V0 * cos(omega * t).

    Parameters
    ----------
    a1 : float
        Linear gain coefficient.
    a2 : float
        Second-order coefficient.
    a3 : float
        Third-order coefficient (typically negative for compression).
    V0 : float
        Input amplitude [V].
    omega : float
        Angular frequency [rad/s].
    t : np.ndarray
        Time array [s].

    Returns
    -------
    v_out : np.ndarray
        Output voltage [V].
    """
    v_in = V0 * np.cos(omega * t)
    return a1 * v_in + a2 * v_in ** 2 + a3 * v_in ** 3


def fundamental_amplitude(a1: float, a3: float, V0: float) -> float:
    """
    Fundamental output amplitude from power series (single tone).

    V_1 = a1 * V0 + (3/4) * a3 * V0^3

    Parameters
    ----------
    a1 : float
        Linear gain coefficient.
    a3 : float
        Third-order coefficient.
    V0 : float
        Input amplitude [V].

    Returns
    -------
    V_1 : float
        Fundamental output amplitude [V].
    """
    return a1 * V0 + 0.75 * a3 * V0 ** 3


def input_p1db_voltage(a1: float, a3: float) -> float:
    """
    Input voltage at 1 dB compression point.

    V_0,1dB = sqrt(0.108 * |4*a1 / (3*a3)|)  for a3 < 0

    Parameters
    ----------
    a1 : float
        Linear gain coefficient.
    a3 : float
        Third-order coefficient (must be < 0).

    Returns
    -------
    V0_1dB : float
        Input amplitude at 1 dB compression [V].
    """
    return np.sqrt(0.108 * abs(4.0 * a1 / (3.0 * a3)))


def input_p1db_dbm(
    a1: float, a3: float, R_in: float = 50.0
) -> float:
    """
    Input 1 dB compression point in dBm (available power).

    Parameters
    ----------
    a1 : float
        Linear gain coefficient.
    a3 : float
        Third-order coefficient (must be < 0).
    R_in : float
        Input impedance [Ohm], default 50.

    Returns
    -------
    P1dB_in_dbm : float
        Input power at 1 dB compression [dBm].
    """
    V0_1dB = input_p1db_voltage(a1, a3)
    # Available power from source: P = V0^2 / (2 * R_in) for peak amplitude V0
    P_in_watts = V0_1dB ** 2 / (2.0 * R_in)
    return 10.0 * np.log10(P_in_watts * 1000.0)


def output_p1db_dbm(
    a1: float, a3: float, R_in: float = 50.0, R_out: float = 50.0
) -> float:
    """
    Output 1 dB compression point in dBm.

    Parameters
    ----------
    a1 : float
        Linear gain coefficient.
    a3 : float
        Third-order coefficient.
    R_in : float
        Input impedance [Ohm], default 50.
    R_out : float
        Output impedance [Ohm], default 50.

    Returns
    -------
    P1dB_out_dbm : float
        Output power at 1 dB compression [dBm].
    """
    V0_1dB = input_p1db_voltage(a1, a3)
    V1_1dB = fundamental_amplitude(a1, a3, V0_1dB)
    P_out_watts = V1_1dB ** 2 / (2.0 * R_out)
    return 10.0 * np.log10(P_out_watts * 1000.0)


def harmonic_distortion_ratio_2(a2: float, a1: float, V0: float) -> float:
    """
    Second harmonic distortion ratio.

    HD2 = (1/2) * |a2 / a1| * V0

    Parameters
    ----------
    a2 : float
        Second-order coefficient.
    a1 : float
        Linear gain coefficient.
    V0 : float
        Input amplitude [V].

    Returns
    -------
    HD2 : float
        HD2 ratio (linear, 0 = none).
    """
    return 0.5 * abs(a2 / a1) * V0


def harmonic_distortion_ratio_3(a3: float, a1: float, V0: float) -> float:
    """
    Third harmonic distortion ratio.

    HD3 = (1/4) * |a3 / a1| * V0^2

    Parameters
    ----------
    a3 : float
        Third-order coefficient.
    a1 : float
        Linear gain coefficient.
    V0 : float
        Input amplitude [V].

    Returns
    -------
    HD3 : float
        HD3 ratio (linear, 0 = none).
    """
    return 0.25 * abs(a3 / a1) * V0 ** 2


def total_harmonic_distortion(
    a1: float, a2: float, a3: float, V0: float
) -> float:
    """
    Total harmonic distortion (THD) from 2nd and 3rd harmonics.

    THD = sqrt(HD2^2 + HD3^2)

    Parameters
    ----------
    a1, a2, a3 : float
        Power series coefficients.
    V0 : float
        Input amplitude [V].

    Returns
    -------
    THD : float
        THD ratio (linear, 0 = none).
    """
    hd2 = harmonic_distortion_ratio_2(a2, a1, V0)
    hd3 = harmonic_distortion_ratio_3(a3, a1, V0)
    return np.sqrt(hd2 ** 2 + hd3 ** 2)


def intermod_ratio_3_db(
    a1: float, a3: float, V0: float
) -> float:
    """
    Third-order intermodulation ratio (IMR3) in dB for two-tone test.

    The fundamental output amplitude: a1*V0 (approx)
    The IM3 output amplitude: (3/4) * a3 * V0^3
    IMR3 (dB) = 20 * log10(fundamental / IM3_amplitude)

    Parameters
    ----------
    a1 : float
        Linear gain coefficient.
    a3 : float
        Third-order coefficient.
    V0 : float
        Per-tone input amplitude [V].

    Returns
    -------
    IMR3_db : float
        IMR3 [dB].
    """
    V_fund = abs(a1 * V0)
    V_im3 = abs(0.75 * a3 * V0 ** 3)
    if V_im3 == 0:
        return np.inf
    return 20.0 * np.log10(V_fund / V_im3)


def iip3_from_coefficients(
    a1: float, a3: float, R: float = 50.0
) -> float:
    """
    IIP3 from power series coefficients.

    IIP3 (linear power) = |2*a1 / (3*a3)|   (for equally spaced tones)
    IIP3 input voltage: V_IIP3 = sqrt(|4*a1 / (3*a3)|)

    Parameters
    ----------
    a1 : float
        Linear gain coefficient.
    a3 : float
        Third-order coefficient.
    R : float
        Impedance [Ohm], default 50.

    Returns
    -------
    IIP3_dbm : float
        Third-order intercept point (input) [dBm].
    """
    V_iip3 = np.sqrt(abs(4.0 * a1 / (3.0 * a3)))
    P_iip3_watts = V_iip3 ** 2 / (2.0 * R)
    return 10.0 * np.log10(P_iip3_watts * 1000.0)


def oip3_from_coefficients(
    a1: float, a3: float, R_in: float = 50.0, R_out: float = 50.0
) -> float:
    """
    OIP3 from power series coefficients.

    OIP3 = IIP3 + G (in dBm and dB)

    Parameters
    ----------
    a1 : float
        Linear gain coefficient.
    a3 : float
        Third-order coefficient.
    R_in : float
        Input impedance [Ohm], default 50.
    R_out : float
        Output impedance [Ohm], default 50.

    Returns
    -------
    OIP3_dbm : float
        Third-order intercept point (output) [dBm].
    """
    iip3_dbm = iip3_from_coefficients(a1, a3, R_in)
    # Voltage gain in dB: power gain = (a1 * sqrt(R_in/R_out))^2
    G_linear = (a1 ** 2) * (R_in / R_out)
    G_db = linear_to_db(G_linear)
    return iip3_dbm + G_db


def cascaded_iip3(IIP3_dbm: np.ndarray, G_db: np.ndarray) -> float:
    """
    Cascaded IIP3 for a chain of stages.

    1/IIP3_total = 1/IIP3_1 + G_1/IIP3_2 + G_1*G_2/IIP3_3 + ...

    Parameters
    ----------
    IIP3_dbm : np.ndarray
        IIP3 of each stage [dBm].
    G_db : np.ndarray
        Gain of each stage [dB].

    Returns
    -------
    IIP3_total_dbm : float
        Cascaded IIP3 [dBm].
    """
    # Convert dBm to mW linear, and dB to linear
    IIP3_mw = db_to_linear(IIP3_dbm)  # dBm -> mW
    G_lin = db_to_linear(G_db)        # dB -> linear
    inv_sum: float = 1.0 / IIP3_mw[0]
    G_cum: float = G_lin[0]
    for i in range(1, len(IIP3_mw)):
        inv_sum += G_cum / IIP3_mw[i]
        G_cum *= G_lin[i]
    return linear_to_db(1.0 / inv_sum)


def iip3_from_imr3(P_in_dbm: float, IMR3_db: float) -> float:
    """
    IIP3 from measured IMR3 at a given input power.

    IIP3 (dBm) = P_in (dBm) + IMR3 (dB) / 2

    Parameters
    ----------
    P_in_dbm : float
        Per-tone input power [dBm].
    IMR3_db : float
        Third-order IM ratio [dB].

    Returns
    -------
    IIP3_dbm : float
        Extrapolated IIP3 [dBm].
    """
    return P_in_dbm + IMR3_db / 2.0


def cross_modulation_depth(a1: float, a3: float, V_interferer: float) -> float:
    """
    Cross-modulation depth from a strong interferer.

    The gain of the desired signal is modulated as:
    G' = a1 * (1 + (3*a3)/(4*a1) * V_interferer^2)

    The depth is the fractional change relative to small-signal gain.

    Parameters
    ----------
    a1 : float
        Linear gain coefficient.
    a3 : float
        Third-order coefficient (negative for compression).
    V_interferer : float
        Interfering signal amplitude [V].

    Returns
    -------
    delta_G_fraction : float
        Fractional gain modulation depth (positive = compression).
    """
    return -0.75 * (a3 / a1) * V_interferer ** 2


# ============================================================
# §10.3 — DYNAMIC RANGE
# ============================================================

def input_noise_floor_dbm(F_db: float, B: float) -> float:
    """
    Input-referred noise floor.

    P_n,in (dBm) = -174 + F_dB + 10*log10(B)

    Parameters
    ----------
    F_db : float
        System noise figure [dB].
    B : float
        Bandwidth [Hz].

    Returns
    -------
    P_n_dbm : float
        Input noise floor [dBm].
    """
    return -174.0 + F_db + 10.0 * np.log10(B)


def linear_dynamic_range_dB(P1dB_in_dbm: float, F_db: float, B: float) -> float:
    """
    Linear dynamic range (DR = P1dB_in / P_n,in).

    Parameters
    ----------
    P1dB_in_dbm : float
        Input 1 dB compression point [dBm].
    F_db : float
        System noise figure [dB].
    B : float
        Bandwidth [Hz].

    Returns
    -------
    DR_db : float
        Linear dynamic range [dB].
    """
    P_n = input_noise_floor_dbm(F_db, B)
    return P1dB_in_dbm - P_n


def sfdr(IIP3_dbm: float, F_db: float, B: float) -> float:
    """
    Spurious-free dynamic range.

    SFDR = (2/3) * (IIP3 - P_n,in)   [dB]
         = (2/3) * (IIP3 + 174 - F_dB - 10*log10(B))  [dB]

    Parameters
    ----------
    IIP3_dbm : float
        Input third-order intercept point [dBm].
    F_db : float
        System noise figure [dB].
    B : float
        Bandwidth [Hz].

    Returns
    -------
    SFDR_db : float
        Spurious-free dynamic range [dB].
    """
    P_n = input_noise_floor_dbm(F_db, B)
    return (2.0 / 3.0) * (IIP3_dbm - P_n)


# ============================================================
# PLOTTING FUNCTIONS
# ============================================================

def plot_noise_power() -> None:
    """Plot thermal noise power vs bandwidth for various temperatures."""
    B_hz = np.logspace(3, 10, 200)  # 1 kHz to 10 GHz bandwidth
    temps_k = [50, 290, 600, 1000]

    fig, ax = plt.subplots(figsize=(10, 6))

    for T_k in temps_k:
        P_n = thermal_noise_power(T_k, B_hz)
        P_n_dbm = 10.0 * np.log10(P_n * 1000.0)
        ax.loglog(B_hz, P_n, linewidth=2,
                  label=f"$T$ = {T_k} K")

    for B_val, label in [(1e3, "1 kHz"), (1e6, "1 MHz"), (1e9, "1 GHz")]:
        idx = np.argmin(np.abs(B_hz - B_val))
        ax.plot(B_hz[idx], thermal_noise_power(290, B_hz[idx]),
                'ko', markersize=5)

    ax.set_xlabel("Bandwidth $B$ [Hz]")
    ax.set_ylabel("Noise Power $P_n$ [W]")
    ax.set_title("Thermal Noise Power vs Bandwidth")
    ax.grid(True, alpha=0.3, which='both')
    ax.legend()
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "noise_power_vs_bandwidth.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


def plot_noise_figure_and_temp() -> None:
    """Show relationship between NF and T_e."""
    F_db_vals = np.linspace(0.1, 10, 200)
    F_lin = db_to_linear(F_db_vals)
    T_e = noise_figure_to_noise_temp(F_lin)

    fig, ax1 = plt.subplots(figsize=(10, 6))

    color1 = '#1a73e8'
    ax1.semilogy(F_db_vals, T_e, color=color1, linewidth=2)
    ax1.set_xlabel("Noise Figure $F$ [dB]")
    ax1.set_ylabel("Equivalent Noise Temp $T_e$ [K]", color=color1)
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.grid(True, alpha=0.3)
    ax1.set_title("Noise Figure vs Equivalent Noise Temperature")

    # Second y-axis: T_e / T0 ratio
    ax2 = ax1.twinx()
    color2 = '#e8710a'
    ax2.semilogy(F_db_vals, T_e / T0, color=color2, linewidth=1.5,
                 linestyle='--', alpha=0.6)
    ax2.set_ylabel("$T_e / T_0$", color=color2)
    ax2.tick_params(axis='y', labelcolor=color2)

    # Annotations for typical devices
    annotations = [
        (0.3, 25, "Cryogenic LNA"),
        (0.5, 40, "LNA"),
        (1.5, 120, "GaAs FET"),
        (5, 700, "Mixer"),
    ]
    for F_d, Te, label in annotations:
        ax1.annotate(label, xy=(F_d, Te),
                     fontsize=8, ha='center', va='bottom',
                     bbox=dict(boxstyle='round,pad=0.3', fc='lightyellow',
                               ec='gray', alpha=0.8))

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "noise_figure_vs_temp.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


def plot_cascaded_noise_chain() -> None:
    """Illustrate Friis formula — effect of first-stage gain on total NF."""
    F_db_chain = np.array([1.5, 6.0, 8.0])  # LNA, mixer, IF amp NF [dB]
    G1_vals = np.linspace(5, 25, 100)  # Sweep LNA gain [dB]

    F_tot_db = []
    F_tot_no_lna = cascaded_noise_figure(F_db_chain[1:], np.array([20.0, 20.0]))

    for G1 in G1_vals:
        G_db_chain = np.array([G1, 20.0, 20.0])
        F_tot_db.append(cascaded_noise_figure(F_db_chain, G_db_chain))

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(G1_vals, F_tot_db, 'b-', linewidth=2,
            label="Cascaded NF (Friis)")
    ax.axhline(F_db_chain[0], color='green', linestyle='--', alpha=0.7,
               label=f"LNA NF = {F_db_chain[0]:.1f} dB (limit)")
    ax.axhline(F_tot_no_lna, color='red', linestyle=':', alpha=0.7,
               label="No LNA (mixer + IF only)")

    ax.fill_between(G1_vals, F_db_chain[0], F_tot_db,
                    alpha=0.1, color='blue',
                    label=f"Penalty from following stages")

    ax.set_xlabel("LNA Gain $G_1$ [dB]")
    ax.set_ylabel("Total Noise Figure $F_{\\text{total}}$ [dB]")
    ax.set_title("Friis Cascade: Total NF vs First-Stage Gain")
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_ylim(F_db_chain[0] - 0.3, max(F_tot_db) + 1)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "cascaded_noise_figure.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


def plot_gain_compression() -> None:
    """Plot gain compression and identify P1dB."""
    a1 = 10.0      # Linear voltage gain (20 dB)
    a3 = -1.5      # Negative: compression
    P_in_dbm = np.linspace(-30, 10, 200)
    R = 50.0

    P_in_watts = db_to_linear(P_in_dbm) / 1000.0
    V0 = np.sqrt(2.0 * R * P_in_watts)  # Peak amplitude per tone (single-tone case)

    # Fundamental output power
    V_fund = np.abs(fundamental_amplitude(a1, a3, V0))
    P_out_fund = V_fund ** 2 / (2.0 * R)
    P_out_fund_dbm = linear_to_db(P_out_fund * 1000.0)

    # Ideal linear output
    P_out_linear = (a1 ** 2) * P_in_watts
    P_out_linear_dbm = linear_to_db(P_out_linear * 1000.0)

    # Gain (dB)
    G_small_signal = linear_to_db(a1 ** 2)
    G_actual = P_out_fund_dbm - P_in_dbm

    # Find P1dB
    V0_1dB = input_p1db_voltage(a1, a3)
    P1dB_in = linear_to_db(V0_1dB ** 2 / (2.0 * R) * 1000.0)
    P1dB_out = P1dB_in + G_small_signal - 1.0  # dB

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # --- Left: Pout vs Pin ---
    ax1.plot(P_in_dbm, P_out_fund_dbm, 'b-', linewidth=2, label="Actual")
    ax1.plot(P_in_dbm, P_out_linear_dbm, 'g--', linewidth=2,
             label="Ideal (linear)")
    ax1.axvline(P1dB_in, color='red', linestyle=':', alpha=0.7,
                label=f"$P_{{1\\,\\text{{dB,in}}}}$ = {P1dB_in:.1f} dBm")
    ax1.axhline(P1dB_out, color='red', linestyle=':', alpha=0.7,
                label=f"$P_{{1\\,\\text{{dB,out}}}}$ = {P1dB_out:.1f} dBm")

    ax1.set_xlabel("Input Power $P_{\\text{in}}$ [dBm]")
    ax1.set_ylabel("Output Power $P_{\\text{out}}$ [dBm]")
    ax1.set_title("Gain Compression ($G_0$ = {:.1f} dB)".format(G_small_signal))
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=8)
    ax1.set_xlim(P_in_dbm[0], P_in_dbm[-1])

    # --- Right: Gain vs Pin ---
    ax2.plot(P_in_dbm, G_actual, 'b-', linewidth=2)
    ax2.axhline(G_small_signal, color='green', linestyle='--', alpha=0.7,
                label=f"SS gain $G_0$ = {G_small_signal:.1f} dB")
    ax2.axhline(G_small_signal - 1.0, color='red', linestyle=':', alpha=0.7,
                label="Gain $-$ 1 dB")
    ax2.axvline(P1dB_in, color='red', linestyle=':', alpha=0.7,
                label=f"$P_{{1\\,\\text{{dB,in}}}}$ = {P1dB_in:.1f} dBm")

    ax2.set_xlabel("Input Power $P_{\\text{in}}$ [dBm]")
    ax2.set_ylabel("Gain [dB]")
    ax2.set_title("Gain vs Input Power")
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=8)
    ax2.set_xlim(P_in_dbm[0], P_in_dbm[-1])

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "gain_compression.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


def plot_intermodulation() -> None:
    """Plot fundamental and IM3 output vs input power; show IIP3."""
    a1 = 10.0
    a3 = -1.5
    R = 50.0

    P_in_dbm = np.linspace(-30, 20, 300)
    P_in_watts = db_to_linear(P_in_dbm) / 1000.0
    V0 = np.sqrt(R * P_in_watts)  # Per-tone RMS = sqrt(P*R) for equal tones
    # Actually for two-tone with equal amplitude, peak per tone = sqrt(2*P_RMS*R)
    V0_peak = np.sqrt(2.0 * R * P_in_watts)

    # Fundamental output (power in one tone)
    V_fund = np.abs(fundamental_amplitude(a1, a3, V0_peak))
    P_out_fund = V_fund ** 2 / (2.0 * R)
    P_out_fund_dbm = linear_to_db(P_out_fund * 1000.0)

    # IM3 output power (per IM product)
    V_im3 = np.abs(0.75 * a3 * V0_peak ** 3)
    P_im3 = V_im3 ** 2 / (2.0 * R)
    P_im3_dbm = linear_to_db(P_im3 * 1000.0)

    # IIP3 and OIP3 from coefficients
    iip3_dbm = iip3_from_coefficients(a1, a3, R)
    G_db = linear_to_db(a1 ** 2)
    oip3_dbm = iip3_dbm + G_db

    # Ideal fundamental (slope 1)
    P_out_ideal = (a1 ** 2) * P_in_watts
    P_out_ideal_dbm = linear_to_db(P_out_ideal * 1000.0)

    # Ideal IM3 (slope 3)
    P_im3_ideal = ((0.75 * abs(a3)) ** 2) * (2.0 * R * P_in_watts) ** 3 / (2.0 * R)
    P_im3_ideal_dbm = linear_to_db(P_im3_ideal * 1000.0)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(P_in_dbm, P_out_fund_dbm, 'b-', linewidth=2, label="Fundamental")
    ax.plot(P_in_dbm, P_out_ideal_dbm, 'b--', linewidth=1.5, alpha=0.5,
            label="Fundamental (ideal, slope 1)")
    ax.plot(P_in_dbm, P_im3_dbm, 'r-', linewidth=2, label="IM3 ($2\\omega_1 - \\omega_2$)")
    ax.plot(P_in_dbm, P_im3_ideal_dbm, 'r--', linewidth=1.5, alpha=0.5,
            label="IM3 (ideal, slope 3)")

    # Mark IIP3
    ax.plot(iip3_dbm, oip3_dbm, 'ko', markersize=8, zorder=5)
    ax.annotate(f"IIP3 = {iip3_dbm:.1f} dBm\nOIP3 = {oip3_dbm:.1f} dBm",
                xy=(iip3_dbm, oip3_dbm), fontsize=9,
                xytext=(iip3_dbm - 15, oip3_dbm - 15),
                arrowprops=dict(arrowstyle='->', color='black'),
                bbox=dict(boxstyle='round,pad=0.3', fc='lightyellow',
                          ec='gray', alpha=0.8))

    # Mark P1dB
    P1dB_in = input_p1db_dbm(a1, a3, R)
    P1dB_out = output_p1db_dbm(a1, a3, R, R)
    ax.plot(P1dB_in, P1dB_out, 'ms', markersize=8, zorder=5)
    ax.annotate(f"$P_{{1\\,\\text{{dB,in}}}}$ = {P1dB_in:.1f} dBm",
                xy=(P1dB_in, P1dB_out), fontsize=8,
                xytext=(P1dB_in - 12, P1dB_out - 8),
                arrowprops=dict(arrowstyle='->', color='magenta'))

    ax.set_xlabel("Input Power Per Tone $P_{\\text{in}}$ [dBm]")
    ax.set_ylabel("Output Power [dBm]")
    ax.set_title("Two-Tone Intermodulation: Fundamental and IM3 vs Input Power")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9)
    ax.set_xlim(P_in_dbm[0], P_in_dbm[-1])
    ax.set_ylim(-100, max(P_out_fund_dbm) + 10)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "intermodulation_iip3.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


def plot_cascaded_iip3() -> None:
    """Show IIP3 degradation with increasing first-stage gain."""
    IIP3_dbm_chain = np.array([15.0, 10.0, 30.0])  # LNA, mixer, IF amp [dBm]
    G_fixed = np.array([20.0, 10.0])                 # Mixer gain, IF amp gain [dB]
    G1_vals = np.linspace(5, 25, 100)                # Sweep LNA gain [dB]

    IIP3_total_db = []
    for G1 in G1_vals:
        G_db = np.array([G1, G_fixed[0], G_fixed[1]])
        IIP3_total_db.append(cascaded_iip3(IIP3_dbm_chain, G_db))

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(G1_vals, IIP3_total_db, 'r-', linewidth=2,
            label="Cascaded IIP3")
    # Stage contributions
    for i, (IIP3_s, G_s, label) in enumerate([
        (IIP3_dbm_chain[0], 0, f"LNA IIP3 = {IIP3_dbm_chain[0]} dBm"),
        (IIP3_dbm_chain[1], G_fixed[0], f"Mixer IIP3 = {IIP3_dbm_chain[1]} dBm"),
        (IIP3_dbm_chain[2], G_fixed[0] + G_fixed[1],
         f"IF Amp IIP3 = {IIP3_dbm_chain[2]} dBm"),
    ]):
        ax.axhline(IIP3_s, color=['green', 'orange', 'purple'][i],
                   linestyle='--', alpha=0.5, label=label)

    ax.set_xlabel("LNA Gain $G_1$ [dB]")
    ax.set_ylabel("Cascaded IIP3 [dBm]")
    ax.set_title("Cascaded IIP3 vs First-Stage Gain")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8)
    ax.set_ylim(min(IIP3_total_db) - 1, max(IIP3_dbm_chain) + 2)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "cascaded_iip3.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


def plot_sfdr_and_dynamic_range() -> None:
    """Plot SFDR as function of bandwidth for various receiver quality."""
    B_vals = np.logspace(4, 9, 200)  # 10 kHz to 1 GHz

    # Three receiver quality tiers
    receivers = [
        {"label": "High-end Rx", "IIP3_dbm": 15, "F_db": 1.0},
        {"label": "Medium Rx",   "IIP3_dbm": 5,  "F_db": 3.0},
        {"label": "Low-cost Rx", "IIP3_dbm": -5, "F_db": 6.0},
    ]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    for rx in receivers:
        sfdr_vals = np.array([sfdr(rx["IIP3_dbm"], rx["F_db"], B)
                              for B in B_vals])
        ax1.semilogx(B_vals, sfdr_vals, linewidth=2, label=rx["label"])

        # Also show noise floor
        P_n = np.array([input_noise_floor_dbm(rx["F_db"], B)
                        for B in B_vals])
        ax2.semilogx(B_vals, P_n, linewidth=2, label=rx["label"])

    ax1.set_xlabel("Bandwidth $B$ [Hz]")
    ax1.set_ylabel("SFDR [dB]")
    ax1.set_title("Spurious-Free Dynamic Range vs Bandwidth")
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_ylim(0, 80)

    ax2.set_xlabel("Bandwidth $B$ [Hz]")
    ax2.set_ylabel("Input Noise Floor [dBm]")
    ax2.set_title("Input-Referred Noise Floor vs Bandwidth")
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    # Annotate -174 dBm/Hz
    ax2.axhline(-174, color='gray', linestyle=':', alpha=0.5,
                label="$-174$ dBm/Hz limit")
    ax2.legend()

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "sfdr_and_noise_floor.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


def plot_two_port_noise_circles() -> None:
    """Illustrate noise figure vs source reflection coefficient."""
    # Typical LNA parameters
    F_min_db = 0.5
    R_n = 4.0        # Equivalent noise resistance [Ohm]
    Gamma_opt_mag = 0.3
    Gamma_opt_phase_deg = 45.0

    # Sweep Gamma_s magnitude at fixed phase
    Gamma_mag_vals = np.linspace(0, 0.8, 100)
    phases_to_plot = [0, 45, 90, 180]

    fig, ax = plt.subplots(figsize=(10, 6))

    for phase_deg in phases_to_plot:
        F_db_vals = []
        for g_mag in Gamma_mag_vals:
            F_db_vals.append(
                noise_figure_from_reflection_coefficient(
                    F_min_db, R_n, g_mag, phase_deg,
                    Gamma_opt_mag, Gamma_opt_phase_deg
                )
            )
        ax.plot(Gamma_mag_vals, F_db_vals, linewidth=2,
                label=f"$\\Gamma_s$ phase = {phase_deg}$^\\circ$")

    ax.axhline(F_min_db, color='gray', linestyle=':', alpha=0.6,
               label=f"$F_{{\\min}}$ = {F_min_db} dB")

    ax.set_xlabel("Source Reflection Coefficient Magnitude $|\\Gamma_s|$")
    ax.set_ylabel("Noise Figure $F$ [dB]")
    ax.set_title("Two-Port Noise Figure vs Source Reflection Coefficient")
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim(0, 0.8)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "two_port_noise_figure.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


def plot_harmonic_distortion() -> None:
    """Show HD2, HD3, THD vs input amplitude."""
    a1 = 10.0
    a2 = 0.3
    a3 = -1.5
    V0_vals = np.logspace(-3, 0, 200)  # 1 mV to 1 V

    HD2_vals = np.array([harmonic_distortion_ratio_2(a2, a1, V) for V in V0_vals])
    HD3_vals = np.array([harmonic_distortion_ratio_3(a3, a1, V) for V in V0_vals])
    THD_vals = np.array([total_harmonic_distortion(a1, a2, a3, V) for V in V0_vals])

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.loglog(V0_vals, HD2_vals, 'g-', linewidth=2, label="HD2 (slope 1)")
    ax.loglog(V0_vals, HD3_vals, 'r-', linewidth=2, label="HD3 (slope 2)")
    ax.loglog(V0_vals, THD_vals, 'b--', linewidth=2, label="THD")

    # Annotate slopes
    ax.annotate("Slope 1 (HD2 $\\propto V_0$)", xy=(3e-3, 3e-4), fontsize=9,
                rotation=20, color='green')
    ax.annotate("Slope 2 (HD3 $\\propto V_0^2$)", xy=(3e-3, 3e-5), fontsize=9,
                rotation=30, color='red')

    ax.set_xlabel("Input Amplitude $V_0$ [V]")
    ax.set_ylabel("Harmonic Distortion Ratio (linear)")
    ax.set_title("Harmonic Distortion vs Input Amplitude")
    ax.grid(True, alpha=0.3, which='both')
    ax.legend()

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "harmonic_distortion.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


# ============================================================
# EXAMPLE CALCULATIONS
# ============================================================

def run_examples() -> None:
    """Print numeric examples for all major concepts."""
    print("=" * 72)
    print("Pozar Ch13 (4e Ch10) — Numerical Examples")
    print("=" * 72)

    # ---- §10.1 Noise Examples ----
    print("\n" + "=" * 50)
    print("  Section 10.1 — Noise")
    print("=" * 50)

    # 10.1.1 Thermal noise power
    print("\n  --- Thermal Noise ---")
    for B_MHz, label in [(1, "1 MHz"), (20, "20 MHz"), (100, "100 MHz")]:
        B = B_MHz * 1e6
        P_n = thermal_noise_power(T0, B)
        P_n_dbm = thermal_noise_power_dbm(T0, B)
        print(f"    P_n @ {label}, T0=290K: {P_n:.3e} W = {P_n_dbm:.1f} dBm")

    print(f"\n    Noise PSD @ T0: {noise_power_density_dbm_per_hz(T0):.1f} dBm/Hz")
    print(f"    Noise PSD @ 50 K: {noise_power_density_dbm_per_hz(50):.1f} dBm/Hz")

    # 10.1.2 NF <=> Te
    print("\n  --- Noise Figure <-> Noise Temperature ---")
    for F_d in [0.5, 1.0, 3.0, 6.0]:
        F_lin = db_to_linear(F_d)
        T_e = noise_figure_to_noise_temp(F_lin)
        print(f"    F = {F_d:.1f} dB  =>  T_e = {T_e:.1f} K")

    for T_e in [50, 150, 500]:
        F_lin = noise_temp_to_noise_figure(T_e)
        F_db = linear_to_db(F_lin)
        print(f"    T_e = {T_e:.0f} K  =>  F = {F_db:.2f} dB")

    # 10.1.3 Friis cascade
    print("\n  --- Friis Cascaded Noise Figure ---")
    # Scenario 1: LNA + Mixer + IF Amp
    F_db = np.array([1.5, 6.0, 8.0])
    G_db = np.array([12.0, -6.0, 20.0])
    F_total = cascaded_noise_figure(F_db, G_db)
    print(f"    Chain: LNA (F=1.5dB, G=12dB) + Mixer (F=6dB, G=-6dB)"
          f" + IF Amp (F=8dB, G=20dB)")
    print(f"    F_total = {F_total:.2f} dB")

    # Scenario 2: Without LNA (mixer directly)
    F_no_lna = cascaded_noise_figure(np.array([6.0, 8.0]),
                                     np.array([-6.0, 20.0]))
    print(f"    Without LNA: F_total = {F_no_lna:.2f} dB")

    # Scenario 3: Passive component
    L_db = 3.0  # 2:1 splitter or 3 dB pad
    print(f"\n    Passive attenuator ({L_db} dB loss):")
    print(f"    NF = loss = {L_db} dB")

    # 10.1.5 System noise temp
    print("\n  --- System Noise Temperature ---")
    T_ant = 30.0  # Antenna noise temperature [K]
    F_db_sys = np.array([1.5, 6.0])
    G_db_sys = np.array([12.0, -6.0])
    T_sys = system_noise_temperature(T_ant, F_db_sys, G_db_sys)
    print(f"    T_ant = {T_ant:.0f} K")
    print(f"    Receiver chain: F = {F_db_sys} dB, G = {G_db_sys} dB")
    print(f"    T_sys = {T_sys:.1f} K")

    # ---- §10.2 Nonlinear Distortion Examples ----
    print("\n" + "=" * 50)
    print("  Section 10.2 — Nonlinear Distortion")
    print("=" * 50)

    a1 = 10.0
    a2 = 0.3
    a3 = -1.5
    R = 50.0

    # 10.2.2 Gain compression
    print("\n  --- Gain Compression ---")
    V0_1dB = input_p1db_voltage(a1, a3)
    P1dB_in = input_p1db_dbm(a1, a3, R)
    P1dB_out = output_p1db_dbm(a1, a3, R, R)
    G_small = linear_to_db(a1 ** 2)
    print(f"    a1 = {a1}, a3 = {a3}")
    print(f"    Small-signal gain: {G_small:.1f} dB")
    print(f"    P_1dB,in  = {P1dB_in:.2f} dBm")
    print(f"    P_1dB,out = {P1dB_out:.2f} dBm")

    # 10.2.3 Harmonic distortion
    print("\n  --- Harmonic Distortion ---")
    for V0_test in [0.01, 0.05, 0.1]:
        hd2 = harmonic_distortion_ratio_2(a2, a1, V0_test)
        hd3 = harmonic_distortion_ratio_3(a3, a1, V0_test)
        thd = total_harmonic_distortion(a1, a2, a3, V0_test)
        print(f"    V0 = {V0_test*1000:.0f} mV:  HD2 = {hd2:.2e}"
              f" ({20*np.log10(hd2):.1f} dBc),"
              f"  HD3 = {hd3:.2e} ({20*np.log10(hd3):.1f} dBc),"
              f"  THD = {thd:.2e}")

    # 10.2.4-5 Intermodulation and IIP3
    print("\n  --- Third-Order Intercept ---")
    iip3_dbm = iip3_from_coefficients(a1, a3, R)
    oip3_dbm = oip3_from_coefficients(a1, a3, R, R)
    g_db = linear_to_db(a1 ** 2)
    IMR3_at_P1dB = intermod_ratio_3_db(a1, a3, V0_1dB)
    print(f"    IIP3 = {iip3_dbm:.2f} dBm")
    print(f"    OIP3 = {oip3_dbm:.2f} dBm")
    print(f"    IIP3 - P1dB = {iip3_dbm - P1dB_in:.1f} dB"
          f" (rule-of-thumb: 9-12 dB)")
    print(f"    IMR3 @ P1dB_in = {IMR3_at_P1dB:.1f} dB")

    # From measurement
    P_test = -15.0  # dBm input power
    IMR3 = intermod_ratio_3_db(a1, a3,
                                np.sqrt(2 * R * db_to_linear(P_test) / 1000))
    IIP3_meas = iip3_from_imr3(P_test, IMR3)
    print(f"\n    Measured: P_in = {P_test:.1f} dBm,"
          f" IMR3 = {IMR3:.1f} dB")
    print(f"    Extrapolated IIP3 = {IIP3_meas:.2f} dBm")

    # Cascaded IIP3
    print("\n  --- Cascaded IIP3 ---")
    IIP3_stages = np.array([15.0, 10.0, 30.0])  # dBm
    G_stages = np.array([12.0, -6.0, 20.0])      # dB
    IIP3_tot = cascaded_iip3(IIP3_stages, G_stages)
    print(f"    Stages: IIP3 = {IIP3_stages} dBm")
    print(f"    Gains:  G = {G_stages} dB")
    print(f"    Cascaded IIP3 = {IIP3_tot:.2f} dBm")

    # 10.2.7 Cross modulation
    print("\n  --- Cross Modulation ---")
    V_interf = 0.3  # Strong interferer amplitude [V]
    delta_G = cross_modulation_depth(a1, a3, V_interf)
    print(f"    Interferer amplitude = {V_interf*1000:.0f} mV")
    print(f"    Gain modulation depth = {delta_G:.3f}"
          f" ({(1 - delta_G)*100:.1f}% of original gain)")

    # ---- §10.3 Dynamic Range Examples ----
    print("\n" + "=" * 50)
    print("  Section 10.3 — Dynamic Range")
    print("=" * 50)

    B_ex = 20e6  # 20 MHz typical

    # High-end receiver
    F_rx = 1.0   # dB
    IIP3_rx = 15.0  # dBm
    P1dB_rx = IIP3_rx - 10  # ~10 dB below IIP3

    P_n = input_noise_floor_dbm(F_rx, B_ex)
    DR = linear_dynamic_range_dB(P1dB_rx, F_rx, B_ex)
    SFDR_val = sfdr(IIP3_rx, F_rx, B_ex)

    print(f"\n  --- High-End Receiver ---")
    print(f"    NF = {F_rx:.1f} dB, IIP3 = {IIP3_rx:.0f} dBm,"
          f" B = {B_ex/1e6:.0f} MHz")
    print(f"    Noise floor (input) = {P_n:.1f} dBm")
    print(f"    Linear DR = {DR:.1f} dB")
    print(f"    SFDR = {SFDR_val:.1f} dB")

    # Low-cost receiver
    F_rx2 = 6.0
    IIP3_rx2 = -5.0
    P1dB_rx2 = IIP3_rx2 - 10

    P_n2 = input_noise_floor_dbm(F_rx2, B_ex)
    DR2 = linear_dynamic_range_dB(P1dB_rx2, F_rx2, B_ex)
    SFDR_val2 = sfdr(IIP3_rx2, F_rx2, B_ex)

    print(f"\n  --- Low-Cost Receiver ---")
    print(f"    NF = {F_rx2:.1f} dB, IIP3 = {IIP3_rx2:.0f} dBm,"
          f" B = {B_ex/1e6:.0f} MHz")
    print(f"    Noise floor (input) = {P_n2:.1f} dBm")
    print(f"    Linear DR = {DR2:.1f} dB")
    print(f"    SFDR = {SFDR_val2:.1f} dB")

    # Bandwidth dependence
    print("\n  --- SFDR vs Bandwidth ---")
    for B_test in [1e6, 20e6, 100e6]:
        sfdr_test = sfdr(IIP3_rx, F_rx, B_test)
        print(f"    B = {B_test/1e6:.0f} MHz: SFDR = {sfdr_test:.1f} dB"
              f" (high-end)")
        sfdr_test2 = sfdr(IIP3_rx2, F_rx2, B_test)
        print(f"                         SFDR = {sfdr_test2:.1f} dB"
              f" (low-cost)")

    print("\n" + "=" * 72)
    print("  All numerical examples complete.")
    print("=" * 72)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("Generating figures for Pozar Ch13 (4e Ch10)...\n")

    # §10.1 — Noise
    print("[10.1] Noise figures...")
    plot_noise_power()
    plot_noise_figure_and_temp()
    plot_cascaded_noise_chain()
    plot_two_port_noise_circles()

    # §10.2 — Nonlinear Distortion
    print("[10.2] Nonlinear distortion figures...")
    plot_gain_compression()
    plot_intermodulation()
    plot_cascaded_iip3()
    plot_harmonic_distortion()

    # §10.3 — Dynamic Range
    print("[10.3] Dynamic range figures...")
    plot_sfdr_and_dynamic_range()

    # Numerical examples
    run_examples()

    print("\n" + "=" * 72)
    print("All outputs complete.")
    print(f"Figures saved to: {FIG_DIR}/")
    print("=" * 72)
