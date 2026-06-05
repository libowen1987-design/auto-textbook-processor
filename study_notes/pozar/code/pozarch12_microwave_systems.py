#!/usr/bin/env python3
"""
Pozar Ch12 (4e Ch14) — Introduction to Microwave Systems
============================================================
Comprehensive example code covering:
  14.1 Antenna system aspects (patterns, gain, G/T)
  14.2 Wireless communications (Friis, link budget, BER)
  14.3 Radar systems (radar equation, RCS, max range)
  14.4 Radiometer systems (sensitivity, NEP)
  14.5 Microwave propagation (atmospheric/rain attenuation)
  14.6 Other applications (heating, WPT, SAR)

All variables follow physical-meaning naming conventions.
Figures saved to: figures/ch12/
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from scipy.special import erfc
from typing import Tuple, Optional
import os

# ---------- Constants ----------
C0: float = 2.998e8          # Speed of light [m/s]
K_B: float = 1.380649e-23    # Boltzmann constant [J/K]
ETA_0: float = 376.7303      # Free-space impedance [Ohm]
T0: float = 290.0            # Standard noise temperature [K]

# Output directory
FIG_DIR = os.path.join(os.path.dirname(__file__), "figures", "ch12")
os.makedirs(FIG_DIR, exist_ok=True)


# ============================================================
# 14.1 — ANTENNA SYSTEM ASPECTS
# ============================================================

def antenna_directivity(
    theta_deg: float,
    phi_deg: float,
    n: int = 2
) -> float:
    """
    Directivity of a simple cos^n(θ) pattern.

    Parameters
    ----------
    theta_deg : float
        Elevation angle [degrees].
    phi_deg : float
        Azimuth angle [degrees] (unused for this isotropic-azimuth pattern).
    n : int
        Pattern exponent (n=1 for dipole-like, n=2 for slightly sharper).

    Returns
    -------
    D : float
        Directivity [linear].
    """
    theta = np.deg2rad(theta_deg)
    # Normalized power pattern: cos^n(theta)
    P_n = np.cos(theta) ** n
    # Directivity: D = 4π / Ω_A  where Ω_A = ∫∫ P_n sinθ dθ dφ
    # For cos^n: Ω_A = 2π / (n+1)
    omega_A = 2.0 * np.pi / (n + 1)
    D = 4.0 * np.pi / omega_A  # for isotropic azimuth
    return D * P_n  # directive gain


def effective_aperture(gain_linear: float, freq_hz: float) -> float:
    """
    Effective aperture from gain.

    A_e = (λ^2 / 4π) * G

    Parameters
    ----------
    gain_linear : float
        Antenna gain [linear].
    freq_hz : float
        Frequency [Hz].

    Returns
    -------
    A_e : float
        Effective aperture [m²].
    """
    lam = C0 / freq_hz
    return lam**2 / (4.0 * np.pi) * gain_linear


def compute_g_over_t(
    gain_ant_dbi: float,
    T_ant: float,
    T_rec: float
) -> float:
    """
    Compute G/T figure of merit for a receiving system.

    G/T = G_ant / T_sys  [dB/K]

    Parameters
    ----------
    gain_ant_dbi : float
        Antenna gain [dBi].
    T_ant : float
        Antenna noise temperature [K].
    T_rec : float
        Receiver noise temperature [K].

    Returns
    -------
    g_over_t_dbk : float
        G/T [dB/K].
    """
    G_lin = 10.0 ** (gain_ant_dbi / 10.0)
    T_sys = T_ant + T_rec
    return 10.0 * np.log10(G_lin / T_sys)


def plot_antenna_patterns() -> None:
    """Plot normalized radiation patterns for various exponents."""
    theta = np.linspace(0, 360, 721)
    theta_rad = np.deg2rad(theta)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5),
                             subplot_kw={'projection': 'polar'})

    for n, color, label in zip(
        [1, 2, 4, 8],
        ['blue', 'red', 'green', 'purple'],
        [f'n={1} (D≈{4/(2/2):.1f})',
         f'n={2} (D≈{4/(2/3):.1f})',
         f'n={4} (D≈{4/(2/5):.1f})',
         f'n={8} (D≈{4/(2/9):.1f})']
    ):
        pattern = np.cos(theta_rad) ** n
        pattern[theta_rad > np.pi / 2] = 0  # no backlobe for simple model
        for ax in axes:
            ax.plot(theta_rad, pattern, color=color, label=label, linewidth=1.5)

    axes[0].set_title("Normalized Power Pattern (linear)", va='bottom')
    axes[1].set_title("Power Pattern (dB scale)")
    axes[1].set_ylim(-40, 0)

    # Convert to dB for second subplot
    axes[1].clear()
    for n, color, label in zip(
        [1, 2, 4, 8],
        ['blue', 'red', 'green', 'purple'],
        [f'n={1}', f'n={2}', f'n={4}', f'n={8}']
    ):
        pattern = np.cos(theta_rad) ** n
        pattern[theta_rad > np.pi / 2] = 0
        pat_db = 10.0 * np.log10(np.maximum(pattern, 1e-6))
        axes[1].plot(theta_rad, pat_db, color=color, label=label, linewidth=1.5)

    axes[1].set_title("Power Pattern (dB scale)")
    axes[1].set_ylim(-40, 0)
    axes[1].legend(loc='lower right')

    axes[0].set_title("Normalized Power Pattern (linear)", va='bottom')
    axes[0].legend(loc='upper right')

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "antenna_patterns.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [✓] Saved {path}")


def plot_effective_aperture() -> None:
    """Plot effective aperture vs frequency for various gains."""
    freq_ghz = np.linspace(0.5, 100, 500)
    freq_hz = freq_ghz * 1e9

    fig, ax = plt.subplots(figsize=(10, 6))

    for G_dbi in [10, 20, 30, 40]:
        G_lin = 10.0 ** (G_dbi / 10.0)
        A_e = effective_aperture(G_lin, freq_hz)
        ax.loglog(freq_ghz, A_e, label=f"G = {G_dbi} dBi", linewidth=2)

    ax.set_xlabel("Frequency [GHz]")
    ax.set_ylabel("Effective Aperture $A_e$ [m²]")
    ax.set_title("Effective Aperture vs Frequency")
    ax.grid(True, which='both', alpha=0.3)
    ax.legend()

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "effective_aperture.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [✓] Saved {path}")


# ============================================================
# 14.2 — WIRELESS COMMUNICATIONS
# ============================================================

def friis_link(
    P_t_dbm: float,
    G_t_dbi: float,
    G_r_dbi: float,
    freq_hz: float,
    R: float,
    L_atm_db: float = 0.0,
    L_pol_db: float = 0.0
) -> float:
    """
    Friis transmission formula with additional losses.

    P_r [dBm] = P_t + G_t + G_r - 20*log10(4πR/λ) - L_atm - L_pol

    Parameters
    ----------
    P_t_dbm : float
        Transmit power [dBm].
    G_t_dbi : float
        Transmit antenna gain [dBi].
    G_r_dbi : float
        Receive antenna gain [dBi].
    freq_hz : float
        Frequency [Hz].
    R : float
        Distance [m].
    L_atm_db : float
        Atmospheric attenuation [dB].
    L_pol_db : float
        Polarization mismatch loss [dB].

    Returns
    -------
    P_r_dbm : float
        Received power [dBm].
    """
    lam = C0 / freq_hz
    fspl_db = 20.0 * np.log10(4.0 * np.pi * R / lam)
    return P_t_dbm + G_t_dbi + G_r_dbi - fspl_db - L_atm_db - L_pol_db


def friis_linear(
    P_t: float,
    G_t: float,
    G_r: float,
    lam: float,
    R: float
) -> float:
    """
    Friis formula in linear units.

    P_r = P_t * G_t * G_r * (λ / (4πR))^2

    Parameters
    ----------
    P_t : float
        Transmit power [W].
    G_t : float
        Transmit gain [linear].
    G_r : float
        Receive gain [linear].
    lam : float
        Wavelength [m].
    R : float
        Distance [m].

    Returns
    -------
    P_r : float
        Received power [W].
    """
    return P_t * G_t * G_r * (lam / (4.0 * np.pi * R))**2


def cascaded_noise_figure(F_db: np.ndarray, G_db: np.ndarray) -> float:
    """
    Total noise figure of a cascaded system (Friis formula).

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
    F_lin = 10.0 ** (F_db / 10.0)
    G_lin = 10.0 ** (G_db / 10.0)
    F_total = F_lin[0]
    G_cum = G_lin[0]
    for i in range(1, len(F_lin)):
        F_total += (F_lin[i] - 1.0) / G_cum
        G_cum *= G_lin[i]
    return 10.0 * np.log10(F_total)


def ber_bpsk(EbN0_db: np.ndarray) -> np.ndarray:
    """BER for BPSK: P_e = 0.5 * erfc(sqrt(Eb/N0))."""
    EbN0_lin = 10.0 ** (EbN0_db / 10.0)
    return 0.5 * erfc(np.sqrt(EbN0_lin))


def ber_qam(M: int, EbN0_db: np.ndarray) -> np.ndarray:
    """
    Approximate BER for M-QAM (rectangular constellation, Gray coding).

    P_e ≈ (4/√M) * (1 - 1/√M) * Q(√(3*Eb/N0/(M-1)))
    """
    from scipy.stats import norm
    EbN0_lin = 10.0 ** (EbN0_db / 10.0)
    sqrtM = int(np.sqrt(M))
    Pe = (4.0 / sqrtM) * (1.0 - 1.0 / sqrtM) * \
         norm.sf(np.sqrt(3.0 * EbN0_lin / (M - 1.0)))
    return Pe


def plot_link_budget() -> None:
    """Plot received power vs distance for various link scenarios."""
    freq_ghz = 2.45
    freq_hz = freq_ghz * 1e9
    P_t_dbm = 20.0         # 100 mW
    G_t_dbi = 6.0
    G_r_dbi = 3.0

    R_km = np.logspace(-2, 3, 300)  # 10 m to 1000 km
    R_m = R_km * 1e3

    # Free-space
    P_r_fs = friis_link(P_t_dbm, G_t_dbi, G_r_dbi, freq_hz, R_m)

    # With atmospheric loss (0.1 dB/km typical at 2.45 GHz)
    L_atm = 0.1 * R_km
    P_r_atm = friis_link(P_t_dbm, G_t_dbi, G_r_dbi, freq_hz, R_m,
                         L_atm_db=L_atm)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.semilogx(R_km, P_r_fs, 'b-', linewidth=2, label="Free space")
    ax.semilogx(R_km, P_r_atm, 'r--', linewidth=2,
                label="With atm. attenuation (0.1 dB/km)")

    # Typical receiver sensitivity for -90 dBm
    ax.axhline(-90, color='gray', linestyle=':', alpha=0.7,
               label="Rx sensitivity (−90 dBm)")

    ax.set_xlabel("Distance [km]")
    ax.set_ylabel("Received Power $P_r$ [dBm]")
    ax.set_title(
        f"Link Budget: Friis Transmission at {freq_ghz} GHz\n"
        f"($P_t$={P_t_dbm} dBm, $G_t$={G_t_dbi} dBi, $G_r$={G_r_dbi} dBi)"
    )
    ax.grid(True, alpha=0.3)
    ax.legend()

    # Annotate FSPL at key distances
    for d_km, label in [(0.1, "100 m"), (1, "1 km"), (100, "100 km")]:
        d_m = d_km * 1e3
        Pr = friis_link(P_t_dbm, G_t_dbi, G_r_dbi, freq_hz, d_m)
        ax.annotate(f"{label}\n{Pr:.0f} dBm",
                    xy=(d_km, Pr), fontsize=8,
                    ha='center', va='bottom')

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "link_budget.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [✓] Saved {path}")


def plot_ber_curves() -> None:
    """Plot BER vs Eb/N0 for various modulation schemes."""
    EbN0_db = np.linspace(0, 20, 200)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.semilogy(EbN0_db, ber_bpsk(EbN0_db), 'b-', linewidth=2,
                label="BPSK")
    ax.semilogy(EbN0_db, ber_qam(4, EbN0_db), 'g--', linewidth=2,
                label="QPSK (= 4-QAM)")
    ax.semilogy(EbN0_db, ber_qam(16, EbN0_db), 'r-.', linewidth=2,
                label="16-QAM")
    ax.semilogy(EbN0_db, ber_qam(64, EbN0_db), 'm:', linewidth=2,
                label="64-QAM")

    # Reference lines
    for ber_target, color in [(1e-3, 'gray'), (1e-6, 'gray')]:
        ax.axhline(ber_target, color=color, linestyle=':', alpha=0.5)
        ax.text(20.5, ber_target, f"BER = {ber_target:.0e}",
                color=color, fontsize=9, va='center')

    ax.set_xlabel("$E_b/N_0$ [dB]")
    ax.set_ylabel("Bit Error Rate (BER)")
    ax.set_title("BER vs $E_b/N_0$ for Digital Modulation Schemes")
    ax.set_ylim(1e-7, 1)
    ax.grid(True, alpha=0.3)
    ax.legend()

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "ber_curves.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [✓] Saved {path}")


# ============================================================
# 14.3 — RADAR SYSTEMS
# ============================================================

def radar_max_range(
    P_t: float,
    G_lin: float,
    freq_hz: float,
    sigma_rcs: float,
    P_r_min: float
) -> float:
    """
    Maximum radar range from the radar equation.

    R_max = [P_t * G^2 * λ^2 * σ / ((4π)^3 * P_r_min)]^(1/4)

    Parameters
    ----------
    P_t : float
        Peak transmit power [W].
    G_lin : float
        Antenna gain [linear].
    freq_hz : float
        Operating frequency [Hz].
    sigma_rcs : float
        Radar cross section [m²].
    P_r_min : float
        Minimum detectable signal [W].

    Returns
    -------
    R_max : float
        Maximum range [m].
    """
    lam = C0 / freq_hz
    numerator = P_t * G_lin**2 * lam**2 * sigma_rcs
    denominator = (4.0 * np.pi)**3 * P_r_min
    return (numerator / denominator)**0.25


def radar_snr(
    P_avg: float,
    G_lin: float,
    freq_hz: float,
    sigma_rcs: float,
    R: float,
    T_sys: float,
    B: float,
    N_pulses: int = 1
) -> float:
    """
    Radar SNR after pulse integration.

    SNR = P_avg * G^2 * λ^2 * σ * N / ((4π)^3 * R^4 * k * T_sys * B)

    Parameters
    ----------
    P_avg : float
        Average transmit power [W].
    G_lin : float
        Antenna gain [linear].
    freq_hz : float
        Frequency [Hz].
    sigma_rcs : float
        RCS [m²].
    R : float
        Range [m].
    T_sys : float
        System noise temperature [K].
    B : float
        Receiver bandwidth [Hz].
    N_pulses : int
        Number of pulses integrated.

    Returns
    -------
    snr_lin : float
        SNR [linear].
    """
    lam = C0 / freq_hz
    numerator = P_avg * G_lin**2 * lam**2 * sigma_rcs * N_pulses
    denominator = (4.0 * np.pi)**3 * R**4 * K_B * T_sys * B
    return numerator / denominator


def plot_radar_range_rcs_sweep() -> None:
    """Plot max radar range vs RCS and vs frequency."""
    # Scenario: Typical pulsed radar
    P_t = 1e6       # 1 MW peak
    G_dbi = 30.0    # 30 dBi
    G_lin = 10.0 ** (G_dbi / 10.0)
    P_r_min = 1e-13  # −100 dBm

    freq_ghz = 10.0   # X-band
    freq_hz = freq_ghz * 1e9

    # Sweep RCS
    sigma_range = np.logspace(-4, 2, 200)  # 0.0001 to 100 m²

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # --- Left: R_max vs RCS ---
    R_max = radar_max_range(P_t, G_lin, freq_hz, sigma_range, P_r_min)
    axes[0].loglog(sigma_range, R_max / 1e3, 'b-', linewidth=2)
    axes[0].set_xlabel("Radar Cross Section $\\sigma$ [m²]")
    axes[0].set_ylabel("Maximum Range $R_{\\max}$ [km]")
    axes[0].set_title(
        f"R_max vs RCS\n"
        f"($P_t$=1 MW, G={G_dbi} dBi, f={freq_ghz} GHz)"
    )
    axes[0].grid(True, which='both', alpha=0.3)

    # Annotate key targets
    targets = [
        (0.01, "Bird"),
        (1.0, "Person"),
        (5.0, "Fighter"),
        (0.001, "Stealth"),
    ]
    for sig, name in targets:
        r_max = radar_max_range(P_t, G_lin, freq_hz, sig, P_r_min)
        axes[0].plot(sig, r_max / 1e3, 'ro', markersize=5)
        axes[0].annotate(name, xy=(sig, r_max / 1e3),
                         fontsize=8, ha='center', va='bottom')

    # --- Right: R_max vs Frequency ---
    sigma_target = 1.0  # m²
    freq_range = np.logspace(0, 2, 200)  # 1 to 100 GHz
    R_max_f = radar_max_range(P_t, G_lin, freq_range * 1e9, sigma_target, P_r_min)
    axes[1].loglog(freq_range, R_max_f / 1e3, 'r-', linewidth=2)
    axes[1].set_xlabel("Frequency [GHz]")
    axes[1].set_ylabel("Maximum Range $R_{\\max}$ [km]")
    axes[1].set_title(
        f"R_max vs Frequency\n"
        f"($\\sigma$={sigma_target} m², G={G_dbi} dBi)"
    )
    axes[1].grid(True, which='both', alpha=0.3)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "radar_range.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [✓] Saved {path}")


def plot_radar_snr_vs_range() -> None:
    """Plot SNR vs range, with and without pulse integration."""
    P_avg = 100.0      # 100 W average
    G_dbi = 35.0       # 35 dBi
    G_lin = 10.0 ** (G_dbi / 10.0)
    freq_ghz = 5.0      # C-band
    freq_hz = freq_ghz * 1e9
    sigma_rcs = 1.0     # 1 m²
    T_sys = 500.0       # System noise temp [K]
    B = 1e6             # 1 MHz bandwidth

    R = np.logspace(2, 5.5, 300)  # 100 m to ~300 km

    fig, ax = plt.subplots(figsize=(10, 6))

    for N_pulses, style, label in [
        (1, 'b-', "Single pulse"),
        (10, 'g--', "10 pulses integrated"),
        (100, 'r-.', "100 pulses integrated"),
        (1000, 'm:', "1000 pulses integrated"),
    ]:
        snr = radar_snr(P_avg, G_lin, freq_hz, sigma_rcs, R, T_sys, B, N_pulses)
        snr_db = 10.0 * np.log10(np.maximum(snr, 1e-20))
        ax.loglog(R / 1e3, snr_db, style, linewidth=1.5, label=label)

    ax.axhline(13.0, color='gray', linestyle=':', alpha=0.5)
    ax.text(0.2, 14, "SNR = 13 dB (typical detection threshold)",
            color='gray', fontsize=9)

    ax.set_xlabel("Range [km]")
    ax.set_ylabel("SNR [dB]")
    ax.set_title(
        f"Radar SNR vs Range\n"
        f"($P_{{avg}}$={P_avg} W, G={G_dbi} dBi, f={freq_ghz} GHz, "
        f"$\\sigma$={sigma_rcs} m²)"
    )
    ax.grid(True, which='both', alpha=0.3)
    ax.legend()

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "radar_snr.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [✓] Saved {path}")


# ============================================================
# 14.4 — RADIOMETER SYSTEMS
# ============================================================

def radiometer_sensitivity_total_power(
    T_sys: float,
    B: float,
    tau: float
) -> float:
    """
    Total-power radiometer sensitivity.

    ΔT_min = T_sys / sqrt(B * τ)

    Parameters
    ----------
    T_sys : float
        System noise temperature [K].
    B : float
        Pre-detection bandwidth [Hz].
    tau : float
        Integration time [s].

    Returns
    -------
    delta_T : float
        Minimum detectable temperature [K].
    """
    return T_sys / np.sqrt(B * tau)


def radiometer_sensitivity_dicke(
    T_sys: float,
    B: float,
    tau: float
) -> float:
    """
    Dicke-switched radiometer sensitivity.

    ΔT_min = 2 * T_sys / sqrt(B * τ)

    Parameters
    ----------
    T_sys : float
        System noise temperature [K].
    B : float
        Pre-detection bandwidth [Hz].
    tau : float
        Integration time [s].

    Returns
    -------
    delta_T : float
        Minimum detectable temperature [K].
    """
    return 2.0 * T_sys / np.sqrt(B * tau)


def radiometer_nep(T_sys: float, B: float, tau: float) -> float:
    """
    Noise Equivalent Power of a radiometer.

    NEP = k * T_sys * sqrt(2 / (B * τ))  [W/√Hz]

    Parameters
    ----------
    T_sys : float
        System noise temperature [K].
    B : float
        Bandwidth [Hz].
    tau : float
        Integration time [s].

    Returns
    -------
    nep : float
        NEP [W/√Hz].
    """
    return K_B * T_sys * np.sqrt(2.0 / (B * tau))


def plot_radiometer_sensitivity() -> None:
    """Plot radiometer sensitivity vs bandwidth and integration time."""
    B = np.logspace(5, 9, 200)  # 100 kHz to 1 GHz
    T_sys = 100.0  # 100 K system temp

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # --- Left: ΔT vs Bandwidth ---
    for tau, style, label in [
        (0.001, 'b-', "τ = 1 ms"),
        (0.01, 'g--', "τ = 10 ms"),
        (0.1, 'r-.', "τ = 100 ms"),
        (1.0, 'm:', "τ = 1 s"),
    ]:
        dT_tp = radiometer_sensitivity_total_power(T_sys, B, tau)
        dT_dk = radiometer_sensitivity_dicke(T_sys, B, tau)
        axes[0].loglog(B, dT_tp, style, linewidth=1.5, label=f"{label} (TP)")
        axes[0].loglog(B, dT_dk, style, linewidth=1.5, alpha=0.5,
                       label=f"{label} (Dicke)")

    axes[0].set_xlabel("Bandwidth B [Hz]")
    axes[0].set_ylabel("ΔT_min [K]")
    axes[0].set_title(
        f"Radiometer Sensitivity\n($T_{{sys}}$ = {T_sys} K)"
    )
    axes[0].grid(True, which='both', alpha=0.3)
    axes[0].legend(fontsize=8)

    # --- Right: NEP vs Bandwidth ---
    for tau, style, label in [
        (0.001, 'b-', "τ = 1 ms"),
        (0.01, 'g--', "τ = 10 ms"),
        (0.1, 'r-.', "τ = 100 ms"),
        (1.0, 'm:', "τ = 1 s"),
    ]:
        nep = radiometer_nep(T_sys, B, tau)
        axes[1].loglog(B, nep, style, linewidth=1.5, label=label)

    axes[1].set_xlabel("Bandwidth B [Hz]")
    axes[1].set_ylabel("NEP [W/√Hz]")
    axes[1].set_title("Noise Equivalent Power (NEP)")
    axes[1].grid(True, which='both', alpha=0.3)
    axes[1].legend(fontsize=8)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "radiometer_sensitivity.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [✓] Saved {path}")


# ============================================================
# 14.5 — MICROWAVE PROPAGATION
# ============================================================

def rain_attenuation(
    freq_ghz: float,
    rain_rate_mmh: float,
    polarization: str = 'H'
) -> float:
    """
    Specific rain attenuation using power-law ITU-R model.

    γ_R = k * R^α  [dB/km]

    Coefficients from ITU-R P.838 (approximate interpolation).

    Parameters
    ----------
    freq_ghz : float
        Frequency [GHz].
    rain_rate_mmh : float
        Rain rate [mm/h].
    polarization : str
        'H' for horizontal, 'V' for vertical.

    Returns
    -------
    gamma_R : float
        Specific attenuation [dB/km].
    """
    # ITU-R P.838 coefficients (approximate table values)
    freq_table = np.array([1, 2, 4, 6, 8, 10, 15, 20, 30, 40, 50, 60, 70, 80, 100])
    if polarization == 'H':
        k_table = np.array([
            0.0000259, 0.000134, 0.000591, 0.00180, 0.00454,
            0.0101, 0.0367, 0.0751, 0.167, 0.289, 0.427,
            0.564, 0.711, 0.866, 1.13
        ])
        alpha_table = np.array([
            0.969, 0.923, 1.075, 1.308, 1.354,
            1.276, 1.139, 1.065, 1.090, 1.067, 0.951,
            0.889, 0.859, 0.843, 0.754
        ])
    else:
        k_table = np.array([
            0.0000246, 0.000128, 0.000563, 0.00168, 0.00371,
            0.00887, 0.0335, 0.0691, 0.151, 0.256, 0.370,
            0.486, 0.613, 0.753, 1.11
        ])
        alpha_table = np.array([
            0.966, 0.913, 1.066, 1.292, 1.330,
            1.264, 1.136, 1.064, 1.062, 1.013, 0.879,
            0.841, 0.829, 0.825, 0.744
        ])

    # Interpolate
    k = np.interp(freq_ghz, freq_table, k_table)
    alpha = np.interp(freq_ghz, freq_table, alpha_table)
    return k * (rain_rate_mmh ** alpha)


def plot_propagation() -> None:
    """Plot rain attenuation and atmospheric absorption."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # --- Left: Rain attenuation vs frequency ---
    freq_ghz = np.linspace(1, 100, 200)
    rain_rates = [5, 10, 25, 50, 100]

    for rr, style, label in [
        (5, 'b-', "5 mm/h (light)"),
        (25, 'g--', "25 mm/h (moderate)"),
        (100, 'r-.', "100 mm/h (heavy)"),
    ]:
        gamma = rain_attenuation(freq_ghz, rr, 'H')
        axes[0].semilogy(freq_ghz, gamma, style, linewidth=1.5, label=label)

    axes[0].set_xlabel("Frequency [GHz]")
    axes[0].set_ylabel("Specific Attenuation γ_R [dB/km]")
    axes[0].set_title("Rain Attenuation (ITU-R P.838, Horizontal Pol.)")
    axes[0].grid(True, alpha=0.3)
    axes[0].legend()

    # --- Right: Cumulative attenuation vs distance ---
    d_km = np.linspace(0, 50, 200)
    freq_ghz = 10.0

    for rr, style, label in [
        (5, 'b-', "5 mm/h"),
        (25, 'g--', "25 mm/h"),
        (100, 'r-.', "100 mm/h"),
    ]:
        gamma = rain_attenuation(freq_ghz, rr, 'H')
        atten = gamma * d_km
        axes[1].plot(d_km, atten, style, linewidth=1.5, label=label)

    axes[1].set_xlabel("Path Length [km]")
    axes[1].set_ylabel("Cumulative Rain Attenuation [dB]")
    axes[1].set_title(f"Rain Attenuation at {freq_ghz} GHz")
    axes[1].grid(True, alpha=0.3)
    axes[1].legend()

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "propagation.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [✓] Saved {path}")


# ============================================================
# 14.6 — OTHER APPLICATIONS
# ============================================================

def power_dissipation_density(
    E_field: float,
    freq_hz: float,
    conductivity: float,
    epsilon_r_prime: float,
    epsilon_r_doubleprime: float
) -> Tuple[float, float, float]:
    """
    Power dissipation density in lossy dielectric.

    P_d = (1/2) * σ * |E|^2 + π * f * ε0 * εr'' * |E|^2  [W/m³]

    Parameters
    ----------
    E_field : float
        Electric field magnitude [V/m].
    freq_hz : float
        Frequency [Hz].
    conductivity : float
        Conductivity [S/m].
    epsilon_r_prime : float
        Real permittivity.
    epsilon_r_doubleprime : float
        Imaginary permittivity (loss factor).

    Returns
    -------
    P_ohmic : float
        Ohmic loss density [W/m³].
    P_dielectric : float
        Dielectric loss density [W/m³].
    P_total : float
        Total power dissipation density [W/m³].
    """
    eps0 = 8.854187817e-12  # Vacuum permittivity [F/m]
    omega = 2.0 * np.pi * freq_hz

    P_ohmic = 0.5 * conductivity * E_field**2
    P_dielectric = 0.5 * omega * eps0 * epsilon_r_doubleprime * E_field**2
    P_total = P_ohmic + P_dielectric

    return P_ohmic, P_dielectric, P_total


def penetration_depth(
    freq_hz: float,
    mu_r: float,
    epsilon_r_prime: float,
    tangent_delta: float
) -> float:
    """
    Penetration (skin) depth in a lossy dielectric.

    δ_p = 1 / α, where α is the attenuation constant.

    Parameters
    ----------
    freq_hz : float
        Frequency [Hz].
    mu_r : float
        Relative permeability.
    epsilon_r_prime : float
        Real part of relative permittivity.
    tangent_delta : float
        Loss tangent tan δ = εr'' / εr'.

    Returns
    -------
    delta_p : float
        Penetration depth [m].
    """
    mu0 = 4.0 * np.pi * 1e-7
    eps0 = 8.854187817e-12
    omega = 2.0 * np.pi * freq_hz

    mu = mu_r * mu0
    eps_prime = epsilon_r_prime * eps0

    # Attenuation constant
    # For tanδ << 1: α ≈ (ω / 2) * sqrt(μ ε') * tanδ
    # Full formula: α = ω * sqrt(με'/2 * (√(1+tan²δ) - 1))
    inner = np.sqrt(1.0 + tangent_delta**2) - 1.0
    alpha = omega * np.sqrt(np.maximum(mu * eps_prime / 2.0 * inner, 0))

    # Use small-angle approximation where valid (cleaner numerical behavior)
    small_td = tangent_delta < 0.1
    alpha_small = (omega / 2.0) * np.sqrt(mu * eps_prime) * tangent_delta
    alpha = np.where(small_td, alpha_small, alpha)

    alpha = np.maximum(alpha, 1e-30)  # avoid division by zero
    return 1.0 / alpha


def sar_from_e_field(
    E_field: float,
    conductivity: float,
    density: float
) -> float:
    """
    Specific Absorption Rate.

    SAR = σ * |E|^2 / (2ρ)  [W/kg]

    Parameters
    ----------
    E_field : float
        RMS electric field [V/m].
    conductivity : float
        Tissue conductivity [S/m].
    density : float
        Tissue density [kg/m³].

    Returns
    -------
    sar : float
        SAR [W/kg].
    """
    return conductivity * E_field**2 / (2.0 * density)


def wireless_power_efficiency(
    D_t: float,
    D_r: float,
    R: float,
    lam: float
) -> float:
    """
    Wireless power transmission beam efficiency (circular apertures).

    η_b ≈ 1 - exp(-τ²/2)  where τ = D_t * D_r / (λ * R)

    Parameters
    ----------
    D_t : float
        Transmit aperture diameter [m].
    D_r : float
        Receive aperture diameter [m].
    R : float
        Distance [m].
    lam : float
        Wavelength [m].

    Returns
    -------
    eta : float
        Beam efficiency (0 to 1).
    """
    tau = D_t * D_r / (lam * R)
    return 1.0 - np.exp(-tau**2 / 2.0)


def plot_microwave_applications() -> None:
    """Plot microwave heating, penetration depth, and WPT efficiency."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # --- (0,0): Power dissipation in water ---
    E_field = 1000.0  # 1 kV/m
    freq_hz_range = np.logspace(8, 10, 200)  # 100 MHz to 10 GHz

    # Water properties (approximate, at 25°C)
    # f [GHz], εr', εr''
    water_data = {
        'f_ghz': np.array([0.1, 0.3, 0.5, 0.915, 1.0, 1.5, 2.0, 2.45, 3.0, 5.0, 10.0]),
        'eps_p': np.array([80.0, 80.0, 79.5, 78.5, 78.0, 77.0, 76.0, 74.0, 72.0, 68.0, 55.0]),
        'eps_pp': np.array([5.0, 3.5, 3.0, 4.0, 5.0, 8.0, 10.0, 13.0, 15.0, 18.0, 12.0]),
    }

    f_hz = water_data['f_ghz'] * 1e9
    sigma_water = 0.01  # S/m, approximate
    _, P_diel, P_tot = power_dissipation_density(
        E_field, f_hz, sigma_water,
        water_data['eps_p'], water_data['eps_pp']
    )

    axes[0, 0].semilogy(water_data['f_ghz'], P_tot, 'b-o', linewidth=2,
                         label="Total dissipation")
    axes[0, 0].semilogy(water_data['f_ghz'], P_diel, 'r--s', linewidth=2,
                         label="Dielectric loss only")
    axes[0, 0].axvline(2.45, color='gray', linestyle=':', alpha=0.7,
                        label="2.45 GHz (ISM)")
    axes[0, 0].set_xlabel("Frequency [GHz]")
    axes[0, 0].set_ylabel("Power Dissipation Density [W/m³]")
    axes[0, 0].set_title(
        f"Power Dissipation in Water\n($|E|$ = {E_field} V/m)"
    )
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].legend()

    # --- (0,1): Penetration depth ---
    freq_ghz_pen = np.linspace(0.1, 10, 200)
    freq_hz_pen = freq_ghz_pen * 1e9

    # Water: εr' ≈ 78 at 0.1 GHz, decreasing to ~55 at 10 GHz
    eps_r_pen = 80.0 - 2.5 * freq_ghz_pen
    tan_d_water = np.interp(freq_ghz_pen, water_data['f_ghz'],
                            water_data['eps_pp'] / water_data['eps_p'])

    delta_p = penetration_depth(freq_hz_pen, 1.0, eps_r_pen, tan_d_water)

    axes[0, 1].loglog(freq_ghz_pen, delta_p * 100, 'g-', linewidth=2)  # cm
    axes[0, 1].axvline(2.45, color='gray', linestyle=':', alpha=0.7,
                        label="2.45 GHz")
    axes[0, 1].axhline(1.0, color='gray', linestyle=':', alpha=0.5)  # 1 cm
    axes[0, 1].set_xlabel("Frequency [GHz]")
    axes[0, 1].set_ylabel("Penetration Depth [cm]")
    axes[0, 1].set_title("Penetration Depth in Water")
    axes[0, 1].grid(True, which='both', alpha=0.3)
    axes[0, 1].legend()

    # --- (1,0): WPT efficiency ---
    D_t = 1.0  # 1 m Tx aperture
    D_r = 1.0  # 1 m Rx aperture
    R_range = np.logspace(0, 4, 300)  # 1 m to 10 km

    for freq_ghz, color, style in [(2.45, 'b', '-'), (5.8, 'g', '--'),
                                     (24.0, 'r', '-.'), (77.0, 'm', ':')]:
        lam = C0 / (freq_ghz * 1e9)
        eta = wireless_power_efficiency(D_t, D_r, R_range, lam)
        axes[1, 0].semilogx(R_range, eta * 100, color=color, linestyle=style,
                             linewidth=1.5, label=f"{freq_ghz} GHz")

    axes[1, 0].set_xlabel("Distance R [m]")
    axes[1, 0].set_ylabel("Beam Efficiency [%]")
    axes[1, 0].set_title("WPT Beam Efficiency\n($D_t = D_r$ = 1 m)")
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].legend()
    axes[1, 0].set_ylim(0, 105)

    # --- (1,1): SAR example ---
    freq_sar = np.array([0.1, 0.3, 0.5, 0.9, 1.8, 2.4, 3.0, 5.0])
    # Typical muscle tissue properties
    sigma_tissue = np.array([0.7, 0.8, 0.9, 1.0, 1.2, 1.4, 1.6, 2.0])
    density_tissue = 1050.0  # kg/m³

    E_sar = 50.0  # 50 V/m (below public limit)
    sar_values = sar_from_e_field(E_sar, sigma_tissue, density_tissue)

    axes[1, 1].bar(freq_sar.astype(str), sar_values * 1e3,
                   color='coral', alpha=0.7, width=0.6)
    axes[1, 1].axhline(2000, color='red', linestyle='--', linewidth=1.5,
                        label="IEEE C95.1 limit (2 W/kg, 10g)")
    axes[1, 1].set_xlabel("Frequency [GHz]")
    axes[1, 1].set_ylabel("SAR [mW/kg]")
    axes[1, 1].set_title(
        f"SAR in Muscle Tissue\n($|E|$ = {E_sar} V/m)"
    )
    axes[1, 1].grid(True, alpha=0.3, axis='y')
    axes[1, 1].legend()

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "microwave_applications.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [✓] Saved {path}")


# ============================================================
# EXAMPLE CALCULATIONS (text output)
# ============================================================

def run_examples() -> None:
    """Run example calculations matching Pozar's text style."""
    print("=" * 70)
    print("Pozar Ch12 (4e Ch14) — Microwave Systems Examples")
    print("=" * 70)

    # --- 14.1: Antenna example ---
    print("\n" + "─" * 50)
    print("§14.1 — Antenna System Aspects")
    print("─" * 50)

    freq_ex = 10e9  # 10 GHz
    G_ant_dbi = 35.0
    G_ant_lin = 10.0 ** (G_ant_dbi / 10.0)
    A_e = effective_aperture(G_ant_lin, freq_ex)
    print(f"  Effective aperture @ {freq_ex/1e9} GHz, G={G_ant_dbi} dBi:")
    print(f"    A_e = {A_e:.4f} m² (≈ {A_e*1e4:.1f} cm²)")

    T_ant = 30.0
    T_rec = 50.0
    gt = compute_g_over_t(G_ant_dbi, T_ant, T_rec)
    print(f"  G/T with T_ant={T_ant} K, T_rec={T_rec} K:")
    print(f"    G/T = {gt:.2f} dB/K")

    # --- 14.2: Wireless comms example ---
    print("\n" + "─" * 50)
    print("§14.2 — Wireless Communications")
    print("─" * 50)

    P_t = 1.0     # 1 W
    G_t = 100.0   # 20 dBi
    G_r = 10.0    # 10 dBi
    lam = C0 / 10e9  # λ at 10 GHz
    R = 50e3      # 50 km
    P_r = friis_linear(P_t, G_t, G_r, lam, R)
    print(f"  Friis link @ {R/1e3} km, 10 GHz:")
    print(f"    P_t = {P_t} W, G_t = 20 dBi, G_r = 10 dBi")
    print(f"    P_r = {P_r:.2e} W ({10*np.log10(P_r*1e3):.1f} dBm)")

    # Link budget in dB
    P_t_dbm = 30.0  # 1 W
    G_t_dbi = 20.0
    G_r_dbi = 10.0
    freq = 10e9
    P_r_db = friis_link(P_t_dbm, G_t_dbi, G_r_dbi, freq, R, L_atm_db=0.5)
    print(f"  Link budget (dB): P_r = {P_r_db:.1f} dBm")
    print(f"  Free-space path loss: {20*np.log10(4*np.pi*R/lam):.1f} dB")

    # Cascaded noise figure example
    F_db = np.array([2.0, 6.0, 3.0])
    G_db = np.array([15.0, 20.0, 10.0])
    F_total = cascaded_noise_figure(F_db, G_db)
    print(f"  Cascaded NF: stages {F_db} dB, gains {G_db} dB")
    print(f"    F_total = {F_total:.2f} dB")
    print(f"    T_e = {(10**(F_total/10)-1)*290:.1f} K")

    # BER example
    EbN0_req = 10.5
    ber_bpsk_val = ber_bpsk(np.array([EbN0_req]))
    print(f"  BPSK BER @ Eb/N0 = {EbN0_req} dB: {ber_bpsk_val[0]:.2e}")

    # --- 14.3: Radar example ---
    print("\n" + "─" * 50)
    print("§14.3 — Radar Systems")
    print("─" * 50)

    P_t_rad = 1e6
    G_lin = 10.0 ** (35.0 / 10.0)
    freq_rad = 5e9
    sigma_target = 1.0
    P_r_min = 1e-13
    R_max = radar_max_range(P_t_rad, G_lin, freq_rad, sigma_target, P_r_min)
    print(f"  Radar range equation:")
    print(f"    P_t = {P_t_rad/1e6} MW, G = 35 dBi, f = {freq_rad/1e9} GHz")
    print(f"    σ = {sigma_target} m², P_r_min = {P_r_min:.0e} W")
    print(f"    R_max = {R_max/1e3:.1f} km")

    # RCS sweep
    for sig, name in [(0.01, "Bird"), (0.001, "Stealth"), (5.0, "Fighter")]:
        R_max_s = radar_max_range(P_t_rad, G_lin, freq_rad, sig, P_r_min)
        print(f"    R_max ({name}, σ={sig} m²) = {R_max_s/1e3:.1f} km")

    # SNR example
    P_avg = 100.0
    T_sys = 500.0
    B = 1e6
    R_test = 100e3
    snr_test = radar_snr(P_avg, G_lin, freq_rad, sigma_target, R_test, T_sys, B)
    print(f"  SNR at {R_test/1e3} km: {10*np.log10(snr_test):.1f} dB")
    snr_test_100 = radar_snr(P_avg, G_lin, freq_rad, sigma_target, R_test,
                             T_sys, B, N_pulses=100)
    print(f"  SNR with 100 pulse integration: "
          f"{10*np.log10(snr_test_100):.1f} dB")

    # --- 14.4: Radiometer example ---
    print("\n" + "─" * 50)
    print("§14.4 — Radiometer Systems")
    print("─" * 50)

    T_sys_rad = 100.0
    B_rad = 500e6  # 500 MHz
    tau_rad = 0.1  # 100 ms

    dT_tp = radiometer_sensitivity_total_power(T_sys_rad, B_rad, tau_rad)
    dT_dk = radiometer_sensitivity_dicke(T_sys_rad, B_rad, tau_rad)
    nep_val = radiometer_nep(T_sys_rad, B_rad, tau_rad)

    print(f"  Radiometer (T_sys = {T_sys_rad} K, B = {B_rad/1e6:.0f} MHz,"
          f" τ = {tau_rad} s):")
    print(f"    ΔT_min (total power) = {dT_tp:.4f} K")
    print(f"    ΔT_min (Dicke)       = {dT_dk:.4f} K")
    print(f"    NEP                  = {nep_val:.2e} W/√Hz")

    # --- 14.5: Propagation example ---
    print("\n" + "─" * 50)
    print("§14.5 — Microwave Propagation")
    print("─" * 50)

    for freq_g in [2.45, 10, 30, 100]:
        for rr, label in [(5, "Light"), (25, "Moderate"), (100, "Heavy")]:
            gamma = rain_attenuation(freq_g, rr, 'H')
            print(f"  {freq_g} GHz, {label} rain ({rr} mm/h): γ_R = "
                  f"{gamma:.3f} dB/km")

    # --- 14.6: Applications example ---
    print("\n" + "─" * 50)
    print("§14.6 — Other Applications")
    print("─" * 50)

    # Microwave heating
    E = 1000.0
    f_245 = 2.45e9
    sigma_muscle = 1.5
    eps_r = 52.0
    eps_r_pp = 14.0
    _, _, P_tot = power_dissipation_density(
        E, f_245, sigma_muscle, eps_r, eps_r_pp
    )
    print(f"  Microwave heating @ 2.45 GHz, |E| = {E} V/m:")
    print(f"    P_d = {P_tot:.1f} W/m³ in muscle tissue")

    # Penetration depth
    delta_p_water = penetration_depth(f_245, 1.0, 74.0, 13.0/74.0)
    print(f"    δ_p (water) = {delta_p_water*100:.2f} cm")

    # WPT
    eta_wpt = wireless_power_efficiency(5.0, 5.0, 1000.0, C0 / 2.45e9)
    print(f"  WPT (D_t = D_r = 5 m, R = 1 km, 2.45 GHz):")
    print(f"    η_b = {eta_wpt*100:.1f}%")

    eta_wpt_hf = wireless_power_efficiency(5.0, 5.0, 1000.0, C0 / 24e9)
    print(f"    η_b @ 24 GHz = {eta_wpt_hf*100:.1f}%")

    # SAR
    E_sar = 50.0
    sar_val = sar_from_e_field(E_sar, 1.4, 1050.0)
    print(f"  SAR for |E| = {E_sar} V/m in muscle:")
    print(f"    SAR = {sar_val*1e3:.1f} mW/kg (IEEE limit: 2 W/kg)")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("Generating figures for Pozar Ch12 (4e Ch14)...\n")

    # 14.1 — Antenna aspects
    print("[14.1] Antenna patterns & aperture...")
    plot_antenna_patterns()
    plot_effective_aperture()

    # 14.2 — Wireless communications
    print("[14.2] Link budget & BER...")
    plot_link_budget()
    plot_ber_curves()

    # 14.3 — Radar systems
    print("[14.3] Radar equations...")
    plot_radar_range_rcs_sweep()
    plot_radar_snr_vs_range()

    # 14.4 — Radiometer systems
    print("[14.4] Radiometer sensitivity...")
    plot_radiometer_sensitivity()

    # 14.5 — Propagation
    print("[14.5] Propagation effects...")
    plot_propagation()

    # 14.6 — Other applications
    print("[14.6] Microwave applications...")
    plot_microwave_applications()

    # Example calculations
    run_examples()

    print("\n" + "=" * 70)
    print("All outputs complete.")
    print(f"Figures saved to: {FIG_DIR}/")
    print("=" * 70)
