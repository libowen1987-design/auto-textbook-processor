#!/usr/bin/env python3
"""
Balanis Antenna Theory — Chapter 2: Fundamental Parameters of Antennas
=====================================================================
Companion Python implementation of key formulas and design examples.

All variable names follow the convention: physical quantities in LaTeX form.
Gain is expressed in dBi (dB relative to isotropic).
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from typing import Tuple, Optional
import os

# ─── Constants ────────────────────────────────────────────────────────────
C_0 = 299_792_458          # speed of light in vacuum [m/s]
ETA_0 = 376.730313         # free-space impedance [Ω]

# ─── Output directory ─────────────────────────────────────────────────────
FIG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "figures", "ch02")
os.makedirs(FIG_DIR, exist_ok=True)


# ═══════════════════════════════════════════════════════════════════════════
#  2.4  Directivity
# ═══════════════════════════════════════════════════════════════════════════

def compute_directivity(aperture_area: float, wavelength: float,
                        efficiency: float = 1.0) -> float:
    """
    Compute directivity D_0 of a planar aperture.

    D_0 = (4π / λ²) * A_em,   where A_em = ε_ap * A_phy.

    Parameters
    ----------
    aperture_area : float
        Physical aperture area A_p [m²].
    wavelength : float
        Free-space wavelength λ [m].
    efficiency : float
        Aperture efficiency ε_ap (0 < ε_ap ≤ 1).

    Returns
    -------
    D_0 : float
        Maximum directivity (linear scale).
    """
    A_em = efficiency * aperture_area
    D_0 = 4.0 * np.pi * A_em / (wavelength ** 2)
    return D_0


# ═══════════════════════════════════════════════════════════════════════════
#  2.5  Gain
# ═══════════════════════════════════════════════════════════════════════════

def compute_gain(directivity: float, efficiency: float) -> Tuple[float, float]:
    """
    Compute gain G_0 from directivity and radiation efficiency.

    G_0 = ε_rad * D_0

    Parameters
    ----------
    directivity : float
        Directivity D_0 (linear scale).
    efficiency : float
        Radiation efficiency ε_rad (0 < ε_rad ≤ 1).

    Returns
    -------
    (G_lin, G_dBi) : Tuple[float, float]
        Gain in linear scale and in dBi.
    """
    G_lin = efficiency * directivity
    G_dBi = 10.0 * np.log10(G_lin)
    return G_lin, G_dBi


# ═══════════════════════════════════════════════════════════════════════════
#  2.8  Polarization Mismatch
# ═══════════════════════════════════════════════════════════════════════════

def polarization_mismatch(pol_type_1: str, pol_type_2: str) -> float:
    """
    Compute Polarization Loss Factor (PLF) between two antennas.

    PLF = |ρ_w · ρ_a|² = cos²(ψ_p)

    Parameters
    ----------
    pol_type_1 : str
        Polarisation of incident wave: 'linear_v', 'linear_h',
        'rhcp', 'lhcp'.
    pol_type_2 : str
        Polarisation of receiving antenna (same options).

    Returns
    -------
    PLF : float
        Polarization loss factor (0 ≤ PLF ≤ 1).
    """
    # Define unit polarisation vectors in (x, y) plane
    pol_vecs = {
        'linear_v':   np.array([0.0, 1.0]),   # vertical
        'linear_h':   np.array([1.0, 0.0]),   # horizontal
        'linear_45':  np.array([1.0, 1.0]) / np.sqrt(2),
        'rhcp':       np.array([1.0, 1.0j]) / np.sqrt(2),
        'lhcp':       np.array([1.0, -1.0j]) / np.sqrt(2),
    }

    try:
        rho_w = pol_vecs[pol_type_1.lower()]
        rho_a = pol_vecs[pol_type_2.lower()]
    except KeyError:
        raise ValueError(
            f"Unknown polarisation type. "
            f"Choose from {list(pol_vecs.keys())}"
        )

    PLF = np.abs(np.dot(rho_w, np.conj(rho_a))) ** 2
    return float(PLF)


# ═══════════════════════════════════════════════════════════════════════════
#  2.11  Friis Transmission Equation
# ═══════════════════════════════════════════════════════════════════════════

def friis_transmission(Pt: float, Gt_dBi: float, Gr_dBi: float,
                       frequency: float, distance: float,
                       PLF: float = 1.0) -> Tuple[float, float, float]:
    """
    Friis transmission equation.

    P_r / P_t = G_t * G_r * (λ / 4πR)² * PLF

    Parameters
    ----------
    Pt : float
        Transmitted power [W].
    Gt_dBi : float
        Transmit antenna gain [dBi].
    Gr_dBi : float
        Receive antenna gain [dBi].
    frequency : float
        Operating frequency [Hz].
    distance : float
        Separation distance [m].
    PLF : float
        Polarization loss factor (0 ≤ PLF ≤ 1, default 1).

    Returns
    -------
    (P_r, PL_dB, FSPL_dB) : Tuple[float, float, float]
        Received power [W], path loss [dB], free-space path loss [dB].
    """
    Gt_lin = 10.0 ** (Gt_dBi / 10.0)
    Gr_lin = 10.0 ** (Gr_dBi / 10.0)
    lambda_0 = C_0 / frequency

    # Free-space path loss
    FSPL = (4.0 * np.pi * distance / lambda_0) ** 2
    FSPL_dB = 10.0 * np.log10(FSPL)

    # Received power
    P_r = Pt * Gt_lin * Gr_lin * PLF / FSPL

    # Path loss (including antenna gains)
    PL_dB = 10.0 * np.log10(Pt / P_r)

    return P_r, PL_dB, FSPL_dB


# ═══════════════════════════════════════════════════════════════════════════
#  2.12  Radar Range Equation
# ═══════════════════════════════════════════════════════════════════════════

def radar_range(Pt: float, Gt_dBi: float, freq: float,
                rcs: float, R: float) -> Tuple[float, float]:
    """
    Monostatic radar range equation.

    P_r = P_t * G_t * G_r * λ² * σ / [(4π)³ * R⁴]

    Parameters
    ----------
    Pt : float
        Peak transmitted power [W].
    Gt_dBi : float
        Antenna gain [dBi] (same for Tx and Rx in monostatic case).
    freq : float
        Operating frequency [Hz].
    rcs : float
        Radar cross section of target σ [m²].
    R : float
        Range to target [m].

    Returns
    -------
    (P_r, P_r_dBm) : Tuple[float, float]
        Received power [W] and [dBm].
    """
    G_lin = 10.0 ** (Gt_dBi / 10.0)
    lambda_0 = C_0 / freq

    P_r = (Pt * (G_lin ** 2) * (lambda_0 ** 2) * rcs
           / ((4.0 * np.pi) ** 3 * R ** 4))
    P_r_dBm = 10.0 * np.log10(P_r * 1000.0)

    return P_r, P_r_dBm


# ═══════════════════════════════════════════════════════════════════════════
#  2.4.3  Kraus Beamwidth → Directivity  (approximate)
# ═══════════════════════════════════════════════════════════════════════════

def beamwidth_to_directivity(theta_HP_d: float, phi_HP_d: float) -> float:
    """
    Kraus approximate formula relating HPBW to directivity.

    D_0 ≈ 4π / (Θ_1r * Θ_2r) = 41253 / (Θ_1d * Θ_2d)

    Parameters
    ----------
    theta_HP_d : float
        Half-power beamwidth in θ-plane [degrees].
    phi_HP_d : float
        Half-power beamwidth in φ-plane [degrees].

    Returns
    -------
    D_0 : float
        Approximate directivity (linear scale).
    """
    D_0 = 41253.0 / (theta_HP_d * phi_HP_d)
    return D_0


# ═══════════════════════════════════════════════════════════════════════════
#  2.13  Antenna Noise Temperature
# ═══════════════════════════════════════════════════════════════════════════

def compute_antenna_temp(Tb_profile_deg: callable,
                         G_pattern: callable,
                         theta: np.ndarray,
                         phi: np.ndarray) -> float:
    """
    Compute antenna noise temperature by numerical integration.

    T_A = (1 / 4π) ∫∫ T_B(Ω) * G(Ω) dΩ

    Parameters
    ----------
    Tb_profile_deg : callable
        Function T_B(theta_deg, phi_deg) returning brightness temp [K].
    G_pattern : callable
        Function G(theta_deg, phi_deg) returning gain pattern (linear).
    theta : np.ndarray
        Polar angles [degrees] for integration grid.
    phi : np.ndarray
        Azimuth angles [degrees] for integration grid.

    Returns
    -------
    T_A : float
        Antenna noise temperature [K].
    """
    THE, PHI = np.meshgrid(np.radians(theta), np.radians(phi), indexing='ij')
    d_theta = np.radians(theta[1] - theta[0]) if len(theta) > 1 else np.pi
    d_phi = np.radians(phi[1] - phi[0]) if len(phi) > 1 else 2 * np.pi

    T_b = Tb_profile_deg(theta[:, None], phi[None, :])
    G = G_pattern(theta[:, None], phi[None, :])

    integrand = T_b * G * np.sin(THE)
    T_A = np.sum(integrand) * d_theta * d_phi / (4.0 * np.pi)

    return float(T_A)


# ═══════════════════════════════════════════════════════════════════════════
#  Plotting Helpers
# ═══════════════════════════════════════════════════════════════════════════

def plot_radiation_pattern(theta: np.ndarray, pattern: np.ndarray,
                           title: str = "Radiation Pattern",
                           filename: Optional[str] = None,
                           normalize: bool = True):
    """
    Plot a radiation pattern in polar coordinates.

    Parameters
    ----------
    theta : np.ndarray
        Angle array [radians], 0 → π.
    pattern : np.ndarray
        Pattern magnitude (linear).
    title : str
        Plot title.
    filename : str or None
        If provided, save figure to this path under FIG_DIR.
    normalize : bool
        Whether to normalise pattern to unit maximum.
    """
    if normalize:
        pattern = pattern / np.max(np.abs(pattern))

    fig, ax = plt.subplots(1, 1, subplot_kw={'projection': 'polar'},
                           figsize=(7, 7))
    # Copy theta to create full 360° pattern
    theta_full = np.concatenate([theta, theta[::-1] + np.pi])
    pattern_full = np.concatenate([pattern, pattern[::-1]])

    ax.plot(theta_full, pattern_full, 'b-', linewidth=2)
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_thetamin(0)
    ax.set_thetamax(360)
    ax.set_rlabel_position(30)
    ax.grid(True, alpha=0.3)
    ax.set_title(title, pad=20, fontsize=13, fontweight='bold')

    plt.tight_layout()
    if filename:
        path = os.path.join(FIG_DIR, filename)
        fig.savefig(path, dpi=150, bbox_inches='tight')
        print(f"  Saved {path}")
    plt.show()
    plt.close(fig)


def _add_style_box(ax, text, loc='upper right', fontsize=9):
    """Add an annotation box to a plot."""
    ax.text(0.95, 0.95, text, transform=ax.transAxes,
            fontsize=fontsize, verticalalignment='top',
            horizontalalignment='right',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='wheat',
                      alpha=0.9))


# ═══════════════════════════════════════════════════════════════════════════
#  Pattern Generators for Common Antennas
# ═══════════════════════════════════════════════════════════════════════════

def isotropic_pattern(theta: np.ndarray, phi: np.ndarray) -> np.ndarray:
    """Isotropic source: uniform radiation."""
    return np.ones_like(theta)


def short_dipole_pattern(theta: np.ndarray, phi: np.ndarray) -> np.ndarray:
    """
    Short dipole (l << λ): sin²θ pattern.
    """
    return np.abs(np.sin(theta))


def half_wave_dipole_pattern(theta: np.ndarray, phi: np.ndarray) -> np.ndarray:
    """
    λ/2 dipole: |cos(π/2 cosθ) / sinθ|  (E-plane).
    """
    denom = np.sin(theta)
    denom = np.where(np.abs(denom) < 1e-15, 1e-15, denom)
    return np.abs(np.cos(np.pi / 2.0 * np.cos(theta)) / denom)


def uniform_array_pattern(theta: np.ndarray, phi: np.ndarray,
                          N: int = 8, d_over_lambda: float = 0.5
                          ) -> np.ndarray:
    """
    Uniform linear array factor (broadside).

    AF(θ) = sin(N ψ / 2) / (N sin(ψ / 2)),  ψ = k d cosθ
    """
    kd = 2.0 * np.pi * d_over_lambda
    psi = kd * np.cos(theta)
    # Use sinc-like formula for numerical stability
    numerator = np.sin(N * psi / 2.0)
    denom = N * np.sin(psi / 2.0)
    denom = np.where(np.abs(denom) < 1e-15, 1e-15, denom)
    return np.abs(numerator / denom)


# ═══════════════════════════════════════════════════════════════════════════
#  Figure 1: Pattern Comparison (Polar)
# ═══════════════════════════════════════════════════════════════════════════

def fig_pattern_compare():
    """Three-antenna polar comparison: isotropic, half-wave dipole, 8-element array."""
    theta = np.linspace(0, np.pi, 721)
    phi = np.array([0.0])

    p_iso = isotropic_pattern(theta, phi)
    p_dip = half_wave_dipole_pattern(theta, phi)
    p_arr = uniform_array_pattern(theta, phi, N=8, d_over_lambda=0.5)

    # Normalise
    p_iso_n = p_iso / np.max(p_iso)
    p_dip_n = p_dip / np.max(p_dip)
    p_arr_n = p_arr / np.max(p_arr)

    fig, axes = plt.subplots(1, 3, subplot_kw={'projection': 'polar'},
                             figsize=(18, 6))
    titles = ['Isotropic Source\n(D₀ = 0 dBi)',
              'λ/2 Dipole\n(D₀ ≈ 2.15 dBi)',
              '8-element Array\n(D₀ ≈ 9.0 dBi)']

    patterns = [p_iso_n, p_dip_n, p_arr_n]

    for ax, pat, ttl in zip(axes, patterns, titles):
        theta_full = np.concatenate([theta, theta[::-1] + np.pi])
        pat_full = np.concatenate([pat, pat[::-1]])
        ax.plot(theta_full, pat_full, 'b-', linewidth=2)
        ax.fill(theta_full, pat_full, alpha=0.15, color='steelblue')
        ax.set_theta_zero_location('N')
        ax.set_theta_direction(-1)
        ax.set_thetamin(0)
        ax.set_thetamax(360)
        ax.grid(True, alpha=0.4)
        ax.set_title(ttl, pad=20, fontsize=13, fontweight='bold')
        ax.set_ylim(0, 1.05)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, 'fig2_1_pattern_compare.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    print(f"  Saved {path}")
    plt.close(fig)


# ═══════════════════════════════════════════════════════════════════════════
#  Figure 2: Friis Path Loss vs Distance
# ═══════════════════════════════════════════════════════════════════════════

def fig_friis_pathloss():
    """Free-space path loss vs distance for several frequencies."""
    distances = np.logspace(0, 5, 200)  # 1 m → 100 km
    freqs_Hz = [900e6, 2.4e9, 5.8e9, 24e9]   # 900 MHz, 2.4, 5.8, 24 GHz
    freq_labels = ["900 MHz", "2.4 GHz", "5.8 GHz", "24 GHz"]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

    fig, ax = plt.subplots(figsize=(10, 6))

    for f, lbl, c in zip(freqs_Hz, freq_labels, colors):
        lambda_0 = C_0 / f
        FSPL = (4.0 * np.pi * distances / lambda_0) ** 2
        FSPL_dB = 10.0 * np.log10(FSPL)
        ax.plot(distances / 1e3, FSPL_dB, color=c, linewidth=2.5,
                label=lbl)

    ax.set_xscale('log')
    ax.set_xlabel('Distance (km)', fontsize=13)
    ax.set_ylabel('Free-space path loss (dB)', fontsize=13)
    ax.set_title('Friis Free-Space Path Loss', fontsize=15, fontweight='bold')
    ax.grid(True, alpha=0.3, which='both')
    ax.legend(fontsize=12)
    ax.set_xlim(0.001, 100)
    ax.set_ylim(20, 200)

    _add_style_box(ax,
                   "FSPL = (4πR/λ)²\n"
                   "  = 20log₁₀(R) + 20log₁₀(f) + const.",
                   loc='upper left')

    plt.tight_layout()
    path = os.path.join(FIG_DIR, 'fig2_2_friis_pathloss.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    print(f"  Saved {path}")
    plt.close(fig)


# ═══════════════════════════════════════════════════════════════════════════
#  Figure 3: Directivity vs Aperture Size
# ═══════════════════════════════════════════════════════════════════════════

def fig_directivity_vs_aperture():
    """Directivity D₀ vs normalised aperture size for several efficiencies."""
    norm_size = np.logspace(-1, 2, 300)  # L/λ from 0.1 to 100
    efficiencies = [1.0, 0.8, 0.6, 0.4]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

    fig, ax = plt.subplots(figsize=(10, 6))

    # Assume square aperture A = L²
    A_p_over_lambda2 = norm_size ** 2

    for eps_ap, c in zip(efficiencies, colors):
        D_0 = 4.0 * np.pi * eps_ap * A_p_over_lambda2
        D_dBi = 10.0 * np.log10(D_0)
        ax.semilogx(norm_size, D_dBi, color=c, linewidth=2.5,
                    label=rf'$\epsilon_{{ap}} = {eps_ap:.1f}$')

    ax.axhline(2.15, color='gray', linestyle='--', linewidth=1.2,
               alpha=0.7, label='λ/2 Dipole (2.15 dBi)')

    ax.set_xlabel(r'Normalised aperture size $L / \lambda$', fontsize=13)
    ax.set_ylabel(r'Directivity $D_0$ (dBi)', fontsize=13)
    ax.set_title(r'Directivity vs Aperture Size (Square Aperture)',
                 fontsize=15, fontweight='bold')
    ax.grid(True, alpha=0.3, which='both')
    ax.legend(fontsize=12)
    ax.set_xlim(0.1, 100)
    ax.set_ylim(-10, 50)

    _add_style_box(ax,
                   r"$D_0 = \frac{4\pi}{\lambda^2} A_{em}$"
                   "\n"
                   r"$A_{em} = \epsilon_{ap} \cdot L^2$",
                   loc='upper left', fontsize=11)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, 'fig2_3_directivity_vs_aperture.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    print(f"  Saved {path}")
    plt.close(fig)


# ═══════════════════════════════════════════════════════════════════════════
#  Balanis Worked Examples
# ═══════════════════════════════════════════════════════════════════════════

def example_2_1():
    """
    Balanis Example 2.1: Compute the directivity of a λ/2 dipole.

    For a half-wave dipole, U(θ) = η₀ |I₀|² cos²(π/2 cosθ) / (8π² sin²θ)
    D₀ = 4π U_max / P_rad

    Analytical result from text: D₀ ≈ 1.643 (2.15 dBi).
    Numerical integration verifies this.
    """
    print("\n" + "=" * 60)
    print("  Balanis Example 2.1: λ/2 Dipole Directivity")
    print("=" * 60)

    # Numerical integration
    N_theta = 2000
    theta = np.linspace(0, np.pi, N_theta)
    d_theta = theta[1] - theta[0]

    # Radiation intensity U(θ) ∝ |F(θ)|²
    F_theta = half_wave_dipole_pattern(theta, np.array([0.0]))
    U_theta = F_theta ** 2                      # normalised radiation intensity
    U_theta = np.squeeze(U_theta)

    # Total radiated power: P_rad = ∫U dΩ = 2π ∫ U sinθ dθ
    integrand = U_theta * np.sin(theta)
    P_rad = 2.0 * np.pi * np.trapezoid(integrand, theta)

    U_max = np.max(U_theta)
    D_0 = 4.0 * np.pi * U_max / P_rad

    print(f"  Numerical D₀ = {D_0:.4f}  ({10*np.log10(D_0):.3f} dBi)")
    print(f"  Text D₀      = 1.643  (2.15 dBi)")
    print(f"  Error         = {abs(D_0 - 1.643)/1.643*100:.2f}%")

    return D_0


def example_2_2():
    """
    Balanis Example 2.2: Friis transmission equation.

    Problem: Two λ/2 dipoles separated by 5 km, f = 400 MHz, G = 2.15 dBi,
    Pt = 100 W. Find Pr.

    Friis: Pr/Pt = Gt Gr (λ/4πR)²
    """
    print("\n" + "=" * 60)
    print("  Balanis Example 2.2: Friis Transmission")
    print("=" * 60)

    Pt = 100.0           # W
    G_dBi = 2.15         # λ/2 dipole gain
    f = 400e6            # Hz
    R = 5e3              # m
    PLF = 1.0            # matched polarisation

    P_r, PL_dB, FSPL_dB = friis_transmission(Pt, G_dBi, G_dBi, f, R, PLF)

    print(f"  Pt  = {Pt:.1f} W")
    print(f"  Gt  = {G_dBi:.2f} dBi  ({10**(G_dBi/10):.4f} linear)")
    print(f"  Gr  = {G_dBi:.2f} dBi")
    print(f"  f   = {f/1e6:.0f} MHz")
    print(f"  λ   = {C_0/f:.3f} m")
    print(f"  R   = {R/1e3:.1f} km")
    print(f"  FSPL= {FSPL_dB:.2f} dB")
    print(f"  Pr  = {P_r*1e6:.4f} μW  ({10*np.log10(P_r*1000):.2f} dBm)")

    # Balanis 4th Ed Ex 2.2: λ/2 dipoles, f=400MHz, R=5km, Pt=100W
    # Note: early editions reference Pr ~O(1 μW) but depend on exact gain values used

    return P_r


def example_2_3():
    """
    Balanis Example 2.3: Radar range equation.

    Monostatic radar: Pt = 150 kW, G = 40 dBi, f = 3 GHz,
    σ = 0.5 m² (bird), R = 100 km. Find Pr.
    """
    print("\n" + "=" * 60)
    print("  Balanis Example 2.3: Radar Range Equation")
    print("=" * 60)

    Pt = 150e3           # W (150 kW)
    G_dBi = 40.0         # dBi
    f = 3e9              # Hz
    rcs = 0.5            # m²  (bird-sized target)
    R = 100e3            # m   (100 km)

    P_r, P_r_dBm = radar_range(Pt, G_dBi, f, rcs, R)

    print(f"  Pt   = {Pt/1e3:.0f} kW")
    print(f"  G    = {G_dBi:.1f} dBi  ({10**(G_dBi/10):.1e} linear)")
    print(f"  f    = {f/1e9:.1f} GHz")
    print(f"  λ    = {C_0/f:.3f} m")
    print(f"  σ    = {rcs:.1f} m²")
    print(f"  R    = {R/1e3:.0f} km")
    print(f"  Pr   = {P_r*1e15:.3f} fW  ({P_r_dBm:.2f} dBm)")

    # Balanis 4th Ed Ex 2.3: G=40dBi, f=3GHz, σ=0.5m², R=100km, Pt=150kW
    # Computed result: Pr ≈ 3.77×10⁻¹³ W (consistent with text order of magnitude)

    return P_r


# ═══════════════════════════════════════════════════════════════════════════
#  Additional Verification: Kraus approximation vs exact
# ═══════════════════════════════════════════════════════════════════════════

def verify_kraus_approximation():
    """
    Compare Kraus beamwidth-based directivity approximation with
    exact numerical integration for uniform square apertures.

    Kraus formula: D₀ ≈ 4π / (Θ₁ᵣ Θ₂ᵣ)
    Valid for pencil-beam antennas where HPBW < 100°.
    """
    print("\n" + "=" * 60)
    print("  Verification: Kraus Approx vs Exact D₀ (Square Aperture)")
    print("=" * 60)

    for side_over_lambda in [2, 5, 10, 20]:
        L = side_over_lambda * 0.1  # keep physical size fixed, vary λ
        lambda_0 = 0.1 / side_over_lambda

        # Exact directivity from aperture formula
        D_exact = compute_directivity(L ** 2, lambda_0, efficiency=1.0)

        # Approximate HPBW for uniform square aperture:
        # HPBW ≈ 0.886 λ / L  (radians)  -> in degrees
        HPBW_rad = 0.886 * lambda_0 / L
        HPBW_deg = np.degrees(HPBW_rad)

        D_Kraus = beamwidth_to_directivity(HPBW_deg, HPBW_deg)

        err = abs(D_Kraus - D_exact) / D_exact * 100
        print(f"  L/λ = {side_over_lambda:2d}:  HPBW ≈ {HPBW_deg:.2f}°,  "
              f"D_Kraus = {D_Kraus:.1f}  ({10*np.log10(D_Kraus):.1f} dBi),  "
              f"D_exact = {D_exact:.1f}  ({10*np.log10(D_exact):.1f} dBi),  "
              f"error = {err:.1f}%")

    print("  Note: Kraus formula assumes ideal rectangular beam; it")
    print("  overestimates D₀ for small apertures and is best used")
    print("  for pencil-beam antennas (HPBW < 100°).")


# ═══════════════════════════════════════════════════════════════════════════
#  Main
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║   Balanis Ch.2 — Antenna Fundamental Parameters             ║")
    print("║   Companion Code & Examples                                 ║")
    print("╚══════════════════════════════════════════════════════════════╝")

    # ── Section 2.4.5: Aperture directivity ──────────────────────────
    print("\n" + "─" * 60)
    print("  [2.4.5] Aperture Directivity (uniform square aperture)")
    print("─" * 60)
    L = 0.5          # m
    lambda_0 = 0.1   # m  (3 GHz)
    A_p = L ** 2
    D_aper = compute_directivity(A_p, lambda_0, efficiency=1.0)
    D_aper_dBi = 10.0 * np.log10(D_aper)
    print(f"  L = {L} m,  λ = {lambda_0} m,  A_p = {A_p} m²")
    print(f"  D₀ = {D_aper:.1f}  ({D_aper_dBi:.2f} dBi)")

    D_aper_80 = compute_directivity(A_p, lambda_0, efficiency=0.8)
    D_aper_80_dBi = 10.0 * np.log10(D_aper_80)
    print(f"  D₀ (ε_ap=0.8) = {D_aper_80:.1f}  ({D_aper_80_dBi:.2f} dBi)")

    # ── Section 2.5: Gain from directivity ──────────────────────────
    print("\n" + "─" * 60)
    print("  [2.5] Gain vs Directivity")
    print("─" * 60)
    D_ref = 1.643
    G_lin, G_dBi = compute_gain(D_ref, efficiency=1.0)
    print(f"  λ/2 dipole: D₀ = {D_ref:.3f}")
    print(f"    ε_rad = 1.0   → G₀ = {G_lin:.3f}  ({G_dBi:.2f} dBi)")
    G_lin95, G_dBi95 = compute_gain(D_ref, efficiency=0.95)
    print(f"    ε_rad = 0.95  → G₀ = {G_lin95:.3f}  ({G_dBi95:.2f} dBi)")

    # ── Section 2.8: Polarisation mismatch ──────────────────────────
    print("\n" + "─" * 60)
    print("  [2.8] Polarisation Mismatch (PLF)")
    print("─" * 60)
    pairs = [
        ('linear_v', 'linear_v'),
        ('linear_v', 'linear_h'),
        ('rhcp', 'rhcp'),
        ('rhcp', 'lhcp'),
        ('linear_v', 'rhcp'),
    ]
    for p1, p2 in pairs:
        plf = polarization_mismatch(p1, p2)
        plf_dB = 10 * np.log10(plf) if plf > 0 else -np.inf
        print(f"  PLF({p1:>10s}, {p2:>10s}) = {plf:.4f}  ({plf_dB:.1f} dB)")

    # ── Examples from Balanis text ───────────────────────────────────
    D_0_dipole = example_2_1()
    P_r_friis = example_2_2()
    P_r_radar = example_2_3()

    # ── Kraus verification ───────────────────────────────────────────
    verify_kraus_approximation()

    # ── Compute directivity from HPBW ────────────────────────────────
    print("\n" + "─" * 60)
    print("  [2.4.3] Kraus: HPBW → Directivity")
    print("─" * 60)
    HPBW_theta = 78.0   # deg (typical λ/2 dipole E-plane)
    HPBW_phi = 78.0     # deg
    D_k = beamwidth_to_directivity(HPBW_theta, HPBW_phi)
    print(f"  HPBW_θ = {HPBW_theta}°, HPBW_φ = {HPBW_phi}°")
    print(f"  D₀ ≈ {D_k:.3f}  ({10*np.log10(D_k):.2f} dBi)")

    # ── Figures ──────────────────────────────────────────────────────
    print("\n" + "─" * 60)
    print("  Generating Figures")
    print("─" * 60)
    fig_pattern_compare()
    fig_friis_pathloss()
    fig_directivity_vs_aperture()

    print("\n" + "─" * 60)
    print("  All examples complete. ✓")
    print("─" * 60)
    print()
