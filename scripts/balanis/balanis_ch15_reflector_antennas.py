#!/usr/bin/env python3
"""
balanis_ch15_reflector_antennas.py
===================================
Balanis 4th Ed., Chapter 15 — Reflector Antennas
Python 复现: Parabolic geometry, aperture distribution patterns,
             feed taper/spillover, Cassegrain equivalence,
             Ruze surface error, total efficiency vs f/D scan.

Author: 二龙虾 (小龙虾编码分身)
Variable naming: focal_length, D_ap, psi_0, f_D, eta_spill,
                 eta_taper, eta_total, rms_error
"""

import numpy as np
from scipy.special import j1 as bessel_j1
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ── 路径配置 ───────────────────────────────────────────────
FIG_DIR = Path(__file__).resolve().parent / 'figures' / 'ch15'
FIG_DIR.mkdir(parents=True, exist_ok=True)

# ── 物理常数 ───────────────────────────────────────────────
C0 = 299792458.0       # speed of light [m/s]
ETA0 = 376.730313      # free-space impedance [Ohm]
PI = np.pi
DEG = PI / 180.0       # degrees → radians


# ═══════════════════════════════════════════════════════════
#  §15.2 — Parabolic Reflector Geometry
# ═══════════════════════════════════════════════════════════

def parabolic_geometry(D_ap, focal_length):
    """
    Compute key parabolic reflector geometry parameters.

    Parameters
    ----------
    D_ap : float
        Aperture diameter [m]
    focal_length : float
        Focal length [m]

    Returns
    -------
    dict with keys: f_D, psi_0_deg, psi_0_rad, a_radius, depth, focal_length, D_ap
    """
    f_D = focal_length / D_ap
    psi_0_rad = 2.0 * np.arctan(D_ap / (4.0 * focal_length))
    psi_0_deg = psi_0_rad / DEG
    a_radius = D_ap / 2.0
    # surface depth at center relative to aperture plane
    depth = D_ap**2 / (16.0 * focal_length)

    return {
        'f_D': f_D,
        'psi_0_deg': psi_0_deg,
        'psi_0_rad': psi_0_rad,
        'a_radius': a_radius,
        'depth': depth,
        'focal_length': focal_length,
        'D_ap': D_ap,
    }


# ═══════════════════════════════════════════════════════════
#  §15.3 — Aperture Distribution → Far-Field Pattern
# ═══════════════════════════════════════════════════════════

def uniform_aperture_pattern(theta, a_radius, wavelength):
    """
    Far-field pattern for a uniformly illuminated circular aperture.
    Uses the Airy pattern: E(theta) ∝ 2 * J1(ka sinθ) / (ka sinθ)

    Parameters
    ----------
    theta : ndarray
        Observation angles [rad]
    a_radius : float
        Aperture radius [m]
    wavelength : float
        Free-space wavelength [m]

    Returns
    -------
    pattern : ndarray — power pattern (linear, normalized to 1 at peak)
    """
    k = 2.0 * PI / wavelength
    u = k * a_radius * np.sin(theta)
    # avoid division by zero at theta=0
    pattern = np.ones_like(u)
    mask = np.abs(u) > 1e-12
    pattern[mask] = (2.0 * bessel_j1(u[mask]) / u[mask])**2
    return pattern


def tapered_aperture_pattern(theta, a_radius, wavelength, taper_coeff=0.2):
    """
    Far-field pattern for a tapered (parabolic-on-pedestal) circular aperture.

    Aperture distribution: E_a(ρ) = C + (1-C)*(1 - (ρ/a)^2)
    where C = edge illumination relative to center.

    Parameters
    ----------
    theta : ndarray
        Observation angles [rad]
    a_radius : float
        Aperture radius [m]
    wavelength : float
        Free-space wavelength [m]
    taper_coeff : float
        Edge illumination coefficient C (0 ≤ C ≤ 1).
        C=1 → uniform; C=0 → full parabolic taper.

    Returns
    -------
    pattern : ndarray — power pattern (linear, normalized to 1 at peak)
    """
    k = 2.0 * PI / wavelength
    u = k * a_radius * np.sin(theta)
    # For parabolic-on-pedestal distribution:
    # F(u) = C * Λ1(2u) + (1-C) * Λ2(u)
    # where Λ1(x) = 2*J1(x)/x, Λ2(u) involves J1 and J2
    # See Balanis Eq. (15-14) and related discussion
    pattern = np.ones_like(u)
    mask = np.abs(u) > 1e-12
    u_m = u[mask]
    # Uniform component contribution: 2J₁(u)/u  where u = ka·sinθ
    F_uniform = 2.0 * bessel_j1(u_m) / u_m
    # Taper component (parabolic) contribution
    # For 1-(ρ/a)^2 taper: F_taper = 8J₂(u)/u²
    from scipy.special import jv as bessel_jv
    F_taper = 8.0 * bessel_jv(2, u_m) / u_m**2

    F_total = taper_coeff * F_uniform + (1.0 - taper_coeff) * F_taper
    pattern[mask] = F_total**2
    pattern[~mask] = 1.0  # normalized peak
    return pattern


# ═══════════════════════════════════════════════════════════
#  §15.4 — Feed Pattern Taper & Spillover Efficiency
# ═══════════════════════════════════════════════════════════

def edge_taper_dB(q, psi_0_rad):
    """
    Edge taper in dB for a cos^q(psi) feed pattern.

    Edge Taper = 20 * log10(cos^q(psi_0))

    Parameters
    ----------
    q : float
        Feed pattern exponent (cos^q)
    psi_0_rad : float
        Subtended half-angle [rad]

    Returns
    -------
    edge_taper : float — edge taper [dB]
    """
    return 20.0 * q * np.log10(np.cos(psi_0_rad))


def feed_pattern_cosq(psi, q):
    """
    Feed power pattern: G_f(psi) = cos^q(psi), clipped to zero for psi > pi/2.

    Parameters
    ----------
    psi : ndarray
        Angles from boresight [rad]
    q : float
        Feed pattern exponent

    Returns
    -------
    pattern : ndarray — power pattern (linear, normalized)
    """
    pattern = np.zeros_like(psi)
    mask = psi <= PI / 2.0
    pattern[mask] = np.cos(psi[mask])**q
    return pattern


def spillover_efficiency(q, psi_0_rad):
    """
    Spillover efficiency for cos^q feed pattern.

    η_spill = 1 - cos^{q+1}(ψ_0)

    Derived analytically from:
      Numerator:   ∫₀^ψ₀ cos^q(ψ) sin(ψ) dψ = [1 - cos^{q+1}(ψ₀)] / (q+1)
      Denominator: ∫₀^(π/2) cos^q(ψ) sin(ψ) dψ = 1 / (q+1)
                   (feed radiates only into forward hemisphere ψ ≤ π/2)
      Ratio = [1 - cos^{q+1}(ψ₀)] / (q+1)  ÷  1/(q+1) = 1 - cos^{q+1}(ψ₀)

    Parameters
    ----------
    q : float
        Feed pattern exponent
    psi_0_rad : float
        Subtended half-angle [rad]

    Returns
    -------
    eta_spill : float — spillover efficiency (0 ≤ η ≤ 1)
    """
    if q <= -1:
        return 0.0
    c = np.cos(psi_0_rad)
    # Handle tiny cos values to avoid numerical issues with large exponent
    if c > 1e-15:
        cos_pow = c**(q + 1.0)
    else:
        cos_pow = 0.0
    eta_spill = 1.0 - cos_pow
    return np.clip(eta_spill, 0.0, 1.0)


def _aperture_distribution(rho_norm, q, psi_0_rad, focal_length):
    """
    Aperture field amplitude distribution from cos^q feed.
    
    Uses exact coordinate mapping: rho = 2*f*tan(psi/2)
    and conservation of power from feed pattern to aperture.

    Parameters
    ----------
    rho_norm : ndarray
        Normalized radial coordinate (0 to 1, where 1 = aperture edge)
    q : float
        Feed pattern exponent
    psi_0_rad : float
        Subtended half-angle [rad]
    focal_length : float
        Focal length [m]

    Returns
    -------
    E_a : ndarray — aperture field amplitude (normalized to 1 at center)
    """
    a_radius = 2.0 * focal_length * np.tan(psi_0_rad / 2.0)
    rho = rho_norm * a_radius
    # psi angle corresponding to radial position rho
    psi = 2.0 * np.arctan(rho / (2.0 * focal_length))
    # Feed amplitude over the dish: sqrt(cos^q(psi)) * (spreading)
    # Aperture field amplitude from GO:
    #   E_a ∝ sqrt(G_f(psi)) / r'  where r' = f / cos^2(psi/2)
    r_prime = focal_length / np.cos(psi / 2.0)**2
    # Protect against cos ≈ 0 at large psi (avoids 0**negative = inf)
    cos_psi = np.maximum(np.cos(psi), 1e-30)
    E_a = cos_psi**(q / 2.0) / r_prime
    # Normalize to center value
    E_a_center = 1.0 / focal_length  # psi=0 -> cos(0)=1, r'=f
    E_a = E_a / E_a_center
    return E_a


def _integrate_trapz(y, x):
    """Trapezoidal integration (compatible with NumPy 1.x and 2.x)."""
    return np.sum((y[:-1] + y[1:]) / 2.0 * np.diff(x))


def taper_efficiency_from_feed(q, psi_0_rad, focal_length=10.0, n_pts=5000):
    """
    Taper (illumination) efficiency for cos^q feed using numerical integration.
    
    η_taper = 2 * [∫₀^a E_a(ρ) ρ dρ]² / [a² * ∫₀^a E_a²(ρ) ρ dρ]
    
    where E_a(ρ) is the aperture field amplitude from the feed pattern.

    Parameters
    ----------
    q : float
        Feed pattern exponent
    psi_0_rad : float
        Subtended half-angle [rad]
    focal_length : float
        Focal length [m] (scales geometry but cancels in ratio for eta_taper)
    n_pts : int
        Number of integration points

    Returns
    -------
    eta_taper : float — taper efficiency (0 ≤ η ≤ 1)
    """
    a_radius = 2.0 * focal_length * np.tan(psi_0_rad / 2.0)
    rho = np.linspace(0, a_radius, n_pts)
    
    E_a = _aperture_distribution(rho / a_radius, q, psi_0_rad, focal_length)
    
    # Numerical integration using trapezoidal rule
    integrand_num = E_a * rho
    integrand_den = E_a**2 * rho
    
    I_num = _integrate_trapz(integrand_num, rho)
    I_den = _integrate_trapz(integrand_den, rho)
    
    if I_den <= 0:
        return 1.0
    
    eta_taper = 2.0 * I_num**2 / (a_radius**2 * I_den)
    return np.clip(eta_taper, 0.0, 1.0)


def q_from_edge_taper(edge_taper_dB, psi_0_rad):
    """
    Compute feed pattern exponent q from specified edge taper.

    Parameters
    ----------
    edge_taper_dB : float
        Desired edge taper [dB] (negative value, e.g. -10)
    psi_0_rad : float
        Subtended half-angle [rad]

    Returns
    -------
    q : float
    """
    # Edge Taper (dB) = 20 * q * log10(cos(psi_0))
    return edge_taper_dB / (20.0 * np.log10(np.cos(psi_0_rad)))


# ═══════════════════════════════════════════════════════════
#  §15.5 — Cassegrain Equivalent f/D
# ═══════════════════════════════════════════════════════════

def cassegrain_equivalent_fD(f_m, D_ap, eccentricity_e):
    """
    Compute Cassegrain equivalent focal length and f/D.

    f_e = e * f_m

    Parameters
    ----------
    f_m : float
        Main reflector focal length [m]
    D_ap : float
        Aperture diameter [m]
    eccentricity_e : float
        Hyperboloid eccentricity (e > 1 for Cassegrain)

    Returns
    -------
    dict with keys: f_e, f_D_equivalent, f_D_actual
    """
    f_e = eccentricity_e * f_m
    f_D_actual = f_m / D_ap
    f_D_equivalent = f_e / D_ap
    return {
        'f_e': f_e,
        'f_D_equivalent': f_D_equivalent,
        'f_D_actual': f_D_actual,
    }


def gregorian_equivalent_fD(f_m, D_ap, eccentricity_e):
    """
    Compute Gregorian equivalent focal length and f/D.

    For Gregorian (ellipsoid), same formula f_e = e * f_m
    but with e < 1.

    Parameters
    ----------
    f_m : float
        Main reflector focal length [m]
    D_ap : float
        Aperture diameter [m]
    eccentricity_e : float
        Ellipsoid eccentricity (e < 1 for Gregorian)

    Returns
    -------
    dict with keys: f_e, f_D_equivalent, f_D_actual
    """
    return cassegrain_equivalent_fD(f_m, D_ap, eccentricity_e)


# ═══════════════════════════════════════════════════════════
#  §15.9 — Ruze Equation (Surface Error Tolerance)
# ═══════════════════════════════════════════════════════════

def ruze_gain_loss(rms_error, wavelength):
    """
    Gain reduction due to random surface errors — Ruze equation.

    G / G_0 = exp[-(4π ε / λ)^2]

    Parameters
    ----------
    rms_error : float
        RMS surface error [m] (normal deviation from ideal paraboloid)
    wavelength : float
        Operating wavelength [m]

    Returns
    -------
    gain_ratio : float — linear gain ratio (G/G_0)
    """
    return np.exp(-(4.0 * PI * rms_error / wavelength)**2)


def ruze_gain_loss_dB(rms_error, wavelength):
    """
    Gain reduction in dB.

    ΔG (dB) = -10 * log10(exp(-(4π ε / λ)^2)) = 686 (ε/λ)^2

    Parameters
    ----------
    rms_error : float
        RMS surface error [m]
    wavelength : float
        Operating wavelength [m]

    Returns
    -------
    delta_G_dB : float — gain loss [dB] (positive value)
    """
    ratio = ruze_gain_loss(rms_error, wavelength)
    if ratio <= 0:
        return 100.0
    return -10.0 * np.log10(ratio)


def ruze_gain_loss_dB_approx(rms_error, wavelength):
    """
    Small-error approximation: ΔG ≈ 686 (ε/λ)^2 [dB].
    Valid when (4π ε / λ) << 1.

    Parameters
    ----------
    rms_error : float
        RMS surface error [m]
    wavelength : float
        Operating wavelength [m]

    Returns
    -------
    delta_G_dB : float — approximate gain loss [dB]
    """
    return 686.0 * (rms_error / wavelength)**2


# ═══════════════════════════════════════════════════════════
#  §15.8 — Total Aperture Efficiency
# ═══════════════════════════════════════════════════════════

def total_efficiency(q, psi_0_rad, focal_length=10.0, eta_blockage=0.95,
                     eta_phase=0.98, eta_surface=1.0, eta_pol=0.98):
    """
    Compute total aperture efficiency as product of all components.

    η_total = η_spill × η_taper × η_phase × η_blockage × η_surface × η_pol

    Parameters
    ----------
    q : float
        Feed pattern exponent
    psi_0_rad : float
        Subtended half-angle [rad]
    focal_length : float
        Focal length [m] (needed for taper integration)
    eta_blockage : float
        Blockage efficiency (0 ≤ η ≤ 1)
    eta_phase : float
        Phase efficiency (0 ≤ η ≤ 1)
    eta_surface : float
        Surface error efficiency (0 ≤ η ≤ 1)
    eta_pol : float
        Cross-pol efficiency (0 ≤ η ≤ 1)

    Returns
    -------
    dict with keys: eta_total, eta_spill, eta_taper, ...
    """
    eta_spill = spillover_efficiency(q, psi_0_rad)
    eta_taper = taper_efficiency_from_feed(q, psi_0_rad, focal_length)
    eta_total = (eta_spill * eta_taper * eta_phase *
                 eta_blockage * eta_surface * eta_pol)
    return {
        'eta_total': eta_total,
        'eta_spill': eta_spill,
        'eta_taper': eta_taper,
        'eta_phase': eta_phase,
        'eta_blockage': eta_blockage,
        'eta_surface': eta_surface,
        'eta_pol': eta_pol,
    }


def total_efficiency_vs_fD(f_D_array, D_ap=10.0, feed_q=8.0, **kwargs):
    """
    Scan total efficiency vs f/D ratio.

    Parameters
    ----------
    f_D_array : ndarray
        Array of f/D values
    D_ap : float
        Aperture diameter [m] (for computing focal_length)
    feed_q : float
        Feed pattern exponent (fixed across scan)
    **kwargs : additional efficiency components passed to total_efficiency()

    Returns
    -------
    results : dict with arrays: f_D, psi_0, eta_spill, eta_taper, eta_total
    """
    psi_0 = 2.0 * np.arctan(1.0 / (4.0 * f_D_array))
    n = len(f_D_array)
    eta_spill = np.zeros(n)
    eta_taper = np.zeros(n)
    eta_total = np.zeros(n)

    for i in range(n):
        f_loc = f_D_array[i] * D_ap
        r = total_efficiency(feed_q, psi_0[i], focal_length=f_loc, **kwargs)
        eta_spill[i] = r['eta_spill']
        eta_taper[i] = r['eta_taper']
        eta_total[i] = r['eta_total']

    return {
        'f_D': f_D_array,
        'psi_0_deg': psi_0 / DEG,
        'eta_spill': eta_spill,
        'eta_taper': eta_taper,
        'eta_total': eta_total,
    }


# ═══════════════════════════════════════════════════════════
#  Demo 1: Parabolic Reflector Geometry
# ═══════════════════════════════════════════════════════════

def demo_parabolic_geometry():
    """Demo 1: Compute geometry for various f/D values."""
    print("=" * 60)
    print("Demo 1: Parabolic Reflector Geometry")
    print("=" * 60)

    D_ap = 10.0   # 10 m aperture diameter
    fD_values = [0.25, 0.3, 0.4, 0.5, 0.7, 1.0]

    print(f"\nAperture diameter D = {D_ap:.1f} m")
    print(f"{'f/D':>6} {'f (m)':>8} {'ψ₀ (deg)':>12} {'Depth (m)':>12}")
    print("-" * 44)

    for f_D in fD_values:
        f = f_D * D_ap
        geo = parabolic_geometry(D_ap, f)
        print(f"{f_D:>6.2f} {geo['focal_length']:>8.2f} "
              f"{geo['psi_0_deg']:>10.2f}° {geo['depth']:>10.3f}")

    # Plot: geometry visualization
    f_D = 0.5
    f = f_D * D_ap
    a = D_ap / 2.0

    # Generate paraboloid cross-section
    rho_pts = np.linspace(0, a, 200)
    z_pts = rho_pts**2 / (4.0 * f)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(rho_pts, z_pts, 'b-', linewidth=2, label=f'f/D = {f_D}')
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    # focus point
    ax.plot(0, f, 'r*', markersize=12, label=f'Focus (f={f:.1f} m)')
    # aperture plane
    ax.axhline(z_pts[-1], color='green', linestyle='--', alpha=0.7,
               label=f'Aperture plane (z={z_pts[-1]:.2f} m)')
    ax.set_xlabel('Radial distance rho [m]')
    ax.set_ylabel('z [m]')
    ax.set_title('Paraboloidal Reflector Cross-Section')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, a * 1.1)
    fig.tight_layout()
    fig.savefig(FIG_DIR / 'fig15_1_parabolic_geometry.png', dpi=150)
    plt.close(fig)
    print(f"\nSaved: fig15_1_parabolic_geometry.png")

    return True


# ═══════════════════════════════════════════════════════════
#  Demo 2: Aperture Distribution → Far-Field Pattern
# ═══════════════════════════════════════════════════════════

def demo_aperture_pattern():
    """Demo 2: Compare uniform vs tapered aperture far-field patterns."""
    print("\n" + "=" * 60)
    print("Demo 2: Aperture Distribution -> Far-Field Pattern")
    print("=" * 60)

    D_ap = 2.0        # 2 m aperture
    frequency = 10e9  # 10 GHz
    wavelength = C0 / frequency
    a_radius = D_ap / 2.0

    print(f"Frequency: {frequency/1e9:.1f} GHz")
    print(f"Wavelength: {wavelength*1e3:.2f} mm")
    print(f"Aperture diameter: {D_ap:.1f} m")
    print(f"ka = {2*PI/wavelength * a_radius:.1f}")

    # theta range: -90 to 90 degrees, dense near boresight
    theta = np.linspace(-PI/2, PI/2, 5001)

    pattern_uniform = uniform_aperture_pattern(theta, a_radius, wavelength)
    pattern_taper_02 = tapered_aperture_pattern(theta, a_radius, wavelength, 0.2)
    pattern_taper_05 = tapered_aperture_pattern(theta, a_radius, wavelength, 0.5)

    # compute HPBW and SLL for uniform pattern
    # HPBW: find angles where pattern drops to 0.5 (-3 dB)
    half_power_mask = theta >= 0
    theta_pos = theta[half_power_mask]
    pu_pos = pattern_uniform[half_power_mask]

    # find -3dB points
    idx_3dB = np.where(pu_pos <= 0.5)[0]
    if len(idx_3dB) > 0:
        hp_half_angle = theta_pos[idx_3dB[0]] / DEG
        hpw_deg = 2.0 * hp_half_angle
    else:
        hpw_deg = 0.0

    # first SLL (first sidelobe peak)
    # find peaks beyond main beam
    zero_crossings = np.where(np.diff(np.sign(np.diff(pu_pos[:-1]))))[0]
    if len(zero_crossings) > 2:
        sl_peaks = pu_pos[zero_crossings[1:]]
        if len(sl_peaks) > 0:
            sll_db = 10.0 * np.log10(np.max(sl_peaks))
        else:
            sll_db = -100
    else:
        sll_db = -100

    print(f"\nUniform aperture:")
    print(f"  HPBW ≈ {hpw_deg:.3f}°")
    print(f"  First SLL ≈ {sll_db:.1f} dB")
    print(f"  Theoretical: HPBW ≈ 1.02 λ/D = {1.02*wavelength/D_ap/DEG:.3f}°")
    print(f"  Theoretical: SLL ≈ -17.6 dB")

    # Plot: radiation patterns
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Linear scale
    ax = axes[0]
    ax.plot(theta / DEG, pattern_uniform, 'b-', label='Uniform (C=1.0)', linewidth=1.5)
    ax.plot(theta / DEG, pattern_taper_05, 'g-', label='Tapered (C=0.5)', linewidth=1.5)
    ax.plot(theta / DEG, pattern_taper_02, 'r-', label='Tapered (C=0.2)', linewidth=1.5)
    ax.set_xlabel('Theta [deg]')
    ax.set_ylabel('Normalized Power')
    ax.set_title('Far-Field Power Pattern (Linear)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-15, 15)

    # dB scale
    ax = axes[1]
    p_u_db = 10.0 * np.log10(np.maximum(pattern_uniform, 1e-12))
    p_t02_db = 10.0 * np.log10(np.maximum(pattern_taper_02, 1e-12))
    p_t05_db = 10.0 * np.log10(np.maximum(pattern_taper_05, 1e-12))

    ax.plot(theta / DEG, p_u_db, 'b-', label='Uniform (C=1.0)', linewidth=1.5)
    ax.plot(theta / DEG, p_t05_db, 'g-', label='Tapered (C=0.5)', linewidth=1.5)
    ax.plot(theta / DEG, p_t02_db, 'r-', label='Tapered (C=0.2)', linewidth=1.5)
    ax.set_xlabel('Theta [deg]')
    ax.set_ylabel('Normalized Power [dB]')
    ax.set_title('Far-Field Power Pattern (dB)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-15, 15)
    ax.set_ylim(-50, 3)

    fig.suptitle(f'Circular Aperture Patterns: D={D_ap}m, f={frequency/1e9}GHz', y=1.02)
    fig.tight_layout()
    fig.savefig(FIG_DIR / 'fig15_2_aperture_patterns.png', dpi=150)
    plt.close(fig)
    print(f"\nSaved: fig15_2_aperture_patterns.png")

    return True


# ═══════════════════════════════════════════════════════════
#  Demo 3: Feed Pattern Taper & Spillover Efficiency
# ═══════════════════════════════════════════════════════════

def demo_feed_taper_spillover():
    """Demo 3: Feed pattern edge taper, spillover efficiency vs q and f/D."""
    print("\n" + "=" * 60)
    print("Demo 3: Feed Pattern Taper & Spillover Efficiency")
    print("=" * 60)

    # Case 1: Fixed f/D = 0.4, sweep q
    D_ap = 10.0
    f_D = 0.4
    focal_length = f_D * D_ap
    geo = parabolic_geometry(D_ap, focal_length)
    psi_0 = geo['psi_0_rad']

    q_values = np.array([2, 4, 6, 8, 10, 12, 16, 20])

    print(f"\nf/D = {f_D:.2f}, ψ₀ = {geo['psi_0_deg']:.2f}°")
    print(f"{'q':>4} {'Edge Taper (dB)':>18} {'η_spill':>10} {'η_taper':>10}")
    print("-" * 46)

    for q in q_values:
        et = edge_taper_dB(q, psi_0)
        eta_s = spillover_efficiency(q, psi_0)
        eta_t = taper_efficiency_from_feed(q, psi_0)
        print(f"{q:>4} {et:>16.2f} {eta_s:>10.4f} {eta_t:>10.4f}")

    # Case 2: contour — spillover vs f/D and q
    fD_range = np.linspace(0.2, 1.2, 50)
    q_range = np.linspace(1, 20, 40)

    eta_spill_2d = np.zeros((len(q_range), len(fD_range)))
    eta_taper_2d = np.zeros((len(q_range), len(fD_range)))
    eta_product_2d = np.zeros((len(q_range), len(fD_range)))

    for iq, q in enumerate(q_range):
        for ifd, fd in enumerate(fD_range):
            psi = 2.0 * np.arctan(1.0 / (4.0 * fd))
            eta_spill_2d[iq, ifd] = spillover_efficiency(q, psi)
            eta_taper_2d[iq, ifd] = taper_efficiency_from_feed(q, psi)
            eta_product_2d[iq, ifd] = eta_spill_2d[iq, ifd] * eta_taper_2d[iq, ifd]

    # Plot: spillover and taper product contour
    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(0.6, 1.0, 17)
    cf = ax.contourf(fD_range, q_range, eta_product_2d, levels=levels,
                     cmap='viridis', extend='both')
    cs = ax.contour(fD_range, q_range, eta_product_2d, levels=levels[::4],
                    colors='white', linewidths=0.8)
    ax.clabel(cs, inline=True, fontsize=8)
    cbar = plt.colorbar(cf, ax=ax, label='$\\eta_{spill} \\times \\eta_{taper}$')
    ax.set_xlabel('f/D')
    ax.set_ylabel('Feed pattern exponent q')
    ax.set_title('Spillover-Taper Product vs f/D and q')
    fig.tight_layout()
    fig.savefig(FIG_DIR / 'fig15_3_spillover_taper_contour.png', dpi=150)
    plt.close(fig)
    print(f"\nSaved: fig15_3_spillover_taper_contour.png")

    # Plot: individual curves for q=8
    fig, ax = plt.subplots(figsize=(8, 5))
    fD_plot = np.linspace(0.2, 1.0, 100)
    eta_s_plot = np.array([spillover_efficiency(8.0, 2*np.arctan(1/(4*fd)))
                           for fd in fD_plot])
    eta_t_plot = np.array([taper_efficiency_from_feed(8.0, 2*np.arctan(1/(4*fd)))
                           for fd in fD_plot])
    eta_p_plot = eta_s_plot * eta_t_plot

    ax.plot(fD_plot, eta_s_plot, 'b-', label='$\\eta_{spill}$', linewidth=2)
    ax.plot(fD_plot, eta_t_plot, 'r-', label='$\\eta_{taper}$', linewidth=2)
    ax.plot(fD_plot, eta_p_plot, 'k--', label='$\\eta_{spill} \\times \\eta_{taper}$',
            linewidth=2)
    idx_max = np.argmax(eta_p_plot)
    ax.plot(fD_plot[idx_max], eta_p_plot[idx_max], 'ko', markersize=8)
    ax.annotate(f'Max at f/D={fD_plot[idx_max]:.2f}',
                xy=(fD_plot[idx_max], eta_p_plot[idx_max]),
                xytext=(fD_plot[idx_max]+0.1, eta_p_plot[idx_max]-0.05),
                arrowprops=dict(arrowstyle='->'))
    ax.set_xlabel('f/D')
    ax.set_ylabel('Efficiency')
    ax.set_title('Spillover and Taper Efficiency vs f/D (q=8)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / 'fig15_3b_spillover_taper_vs_fd.png', dpi=150)
    plt.close(fig)
    print(f"Saved: fig15_3b_spillover_taper_vs_fd.png")

    return True


# ═══════════════════════════════════════════════════════════
#  Demo 4: Cassegrain Equivalent f/D
# ═══════════════════════════════════════════════════════════

def demo_cassegrain_equivalent():
    """Demo 4: Cassegrain equivalent f/D calculation."""
    print("\n" + "=" * 60)
    print("Demo 4: Cassegrain Equivalent f/D")
    print("=" * 60)

    D_ap = 10.0   # 10 m aperture
    f_m = 3.0     # main reflector focal length 3 m -> f/D = 0.3
    eccentricities = [1.2, 1.5, 2.0, 2.5, 3.0]

    print(f"\nMain reflector: D = {D_ap:.1f} m, f_m = {f_m:.1f} m, "
          f"f/D = {f_m/D_ap:.2f}")
    print(f"{'e':>6} {'f_e (m)':>10} {'Eq. f/D':>10} {'f/D ratio':>10}")
    print("-" * 40)

    for e in eccentricities:
        result = cassegrain_equivalent_fD(f_m, D_ap, e)
        ratio = result['f_D_equivalent'] / result['f_D_actual']
        print(f"{e:>6.1f} {result['f_e']:>9.1f} "
              f"{result['f_D_equivalent']:>9.3f} {ratio:>9.2f}x")

    print("\nPhysical interpretation:")
    print("  Cassegrain (e > 1) increases effective f/D.")
    print("  Larger equivalent f/D means:")
    print("    - Lower spillover (narrower feed beam needed)")
    print("    - Feed can be placed behind main reflector")
    print("    - Better for low-noise receivers")

    # Also show Gregorian for comparison
    print("\n  Gregorian (e < 1) comparison:")
    f_m_g = 3.0
    for e in [0.5, 0.7, 0.9]:
        result = gregorian_equivalent_fD(f_m_g, D_ap, e)
        print(f"    e={e:.1f}: f_e={result['f_e']:.2f} m, "
              f"Eq. f/D={result['f_D_equivalent']:.3f}")

    return True


# ═══════════════════════════════════════════════════════════
#  Demo 5: Ruze Equation
# ═══════════════════════════════════════════════════════════

def demo_ruze_equation():
    """Demo 5: Ruze equation — gain loss vs RMS surface error."""
    print("\n" + "=" * 60)
    print("Demo 5: Ruze Equation — Surface Error Tolerance")
    print("=" * 60)

    # Error-to-wavelength ratios
    eps_over_lambda = np.array([1/100, 1/50, 1/30, 1/20, 1/16, 1/10, 1/8, 1/5])
    wavelength = 0.03  # 10 GHz reference wavelength [m]

    print(f"Reference wavelength: {wavelength*1e3:.1f} mm (f = {C0/wavelength/1e9:.1f} GHz)")
    print(f"{'ε/λ':>10} {'ε (mm)':>10} {'G/G₀':>10} {'ΔG (dB) exact':>16} "
          f"{'ΔG (dB) approx':>16}")
    print("-" * 66)

    for ratio in eps_over_lambda:
        eps = ratio * wavelength
        gain_ratio = ruze_gain_loss(eps, wavelength)
        delta_exact = ruze_gain_loss_dB(eps, wavelength)
        delta_approx = ruze_gain_loss_dB_approx(eps, wavelength)
        print(f"{ratio:>10.4f} {eps*1e3:>10.4f} {gain_ratio:>10.6f} "
              f"{delta_exact:>14.4f} {delta_approx:>14.4f}")

    # Plot: Gain loss vs ε/λ
    eps_range = np.logspace(-3, -0.5, 200)
    delta_range = np.array([ruze_gain_loss_dB(e, 1.0) for e in eps_range])
    # note: only ratio matters so set λ=1

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogx(eps_range, delta_range, 'b-', linewidth=2, label='Ruze formula')
    # approximate formula
    delta_approx_range = 686.0 * eps_range**2
    ax.semilogx(eps_range, delta_approx_range, 'r--', linewidth=1.5,
                label='Approx: 686 (ε/λ)²')

    # Mark typical tolerance thresholds
    ax.axvline(1/50, color='green', linestyle=':', alpha=0.7,
               label='ε/λ = 1/50 (0.27 dB loss)')
    ax.axvline(1/30, color='orange', linestyle=':', alpha=0.7,
               label='ε/λ = 1/30 (0.76 dB loss)')
    ax.axvline(1/16, color='red', linestyle=':', alpha=0.7,
               label='ε/λ = 1/16 (engineering limit)')

    ax.set_xlabel('RMS Surface Error / Wavelength (ε/λ)')
    ax.set_ylabel('Gain Loss [dB]')
    ax.set_title('Ruze Equation: Gain Loss vs Surface Error')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 10)
    fig.tight_layout()
    fig.savefig(FIG_DIR / 'fig15_5_ruze_equation.png', dpi=150)
    plt.close(fig)
    print(f"\nSaved: fig15_5_ruze_equation.png")

    # Plot: Frequency dependence for fixed surface error
    freq_range = np.linspace(1e9, 40e9, 200)
    rms_fixed = 0.5e-3  # 0.5 mm RMS error

    fig, ax = plt.subplots(figsize=(8, 5))
    for eps_mm in [0.2, 0.5, 1.0, 2.0]:
        eps_m = eps_mm * 1e-3
        wl_range = C0 / freq_range
        delta_range_f = np.array(
            [ruze_gain_loss_dB(eps_m, wl) for wl in wl_range])
        ax.plot(freq_range / 1e9, delta_range_f, linewidth=1.5,
                label=f'ε = {eps_mm:.1f} mm')

    ax.axhline(1.0, color='gray', linestyle='--', alpha=0.5,
               label='1 dB loss limit')
    ax.set_xlabel('Frequency [GHz]')
    ax.set_ylabel('Gain Loss [dB]')
    ax.set_title('Ruze Gain Loss vs Frequency (Fixed Surface Error)')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / 'fig15_5b_ruze_vs_frequency.png', dpi=150)
    plt.close(fig)
    print("Saved: fig15_5b_ruze_vs_frequency.png")

    return True


# ═══════════════════════════════════════════════════════════
#  Demo 6: Total Efficiency vs f/D Scan
# ═══════════════════════════════════════════════════════════

def demo_total_efficiency_scan():
    """Demo 6: Complete reflector efficiency scan vs f/D."""
    print("\n" + "=" * 60)
    print("Demo 6: Total Reflector Efficiency vs f/D Scan")
    print("=" * 60)

    fD_array = np.linspace(0.2, 1.0, 200)
    q_values = [4, 6, 8, 10, 12]

    fig, ax = plt.subplots(figsize=(10, 6))

    for q in q_values:
        result = total_efficiency_vs_fD(fD_array, feed_q=q,
                                        eta_blockage=0.95,
                                        eta_phase=0.98,
                                        eta_surface=0.99,
                                        eta_pol=0.98)
        ax.plot(result['f_D'], result['eta_total'],
                linewidth=1.5, label=f'q = {q}')
        idx_max = np.argmax(result['eta_total'])
        ax.plot(result['f_D'][idx_max], result['eta_total'][idx_max],
                'o', markersize=6)

    ax.set_xlabel('f / D')
    ax.set_ylabel('Total Aperture Efficiency $\\eta_{total}$')
    ax.set_title('Total Efficiency vs f/D for Various Feed Patterns')
    ax.legend(title='Feed exponent q')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0.3, 0.8)
    fig.tight_layout()
    fig.savefig(FIG_DIR / 'fig15_6_total_efficiency_vs_fD.png', dpi=150)
    plt.close(fig)
    print(f"\nSaved: fig15_6_total_efficiency_vs_fD.png")

    # Print optimal f/D for each q
    print(f"\n{'q':>4} {'Optimal f/D':>14} {'Max η_total':>12} {'ψ₀ (deg)':>12}")
    print("-" * 46)
    for q in q_values:
        result = total_efficiency_vs_fD(fD_array, feed_q=q,
                                        eta_blockage=0.95,
                                        eta_phase=0.98,
                                        eta_surface=0.99,
                                        eta_pol=0.98)
        idx_max = np.argmax(result['eta_total'])
        print(f"{q:>4} {result['f_D'][idx_max]:>13.3f} "
              f"{result['eta_total'][idx_max]:>11.4f} "
              f"{result['psi_0_deg'][idx_max]:>10.2f}°")

    # Breakdown plot for q=8
    fig, ax = plt.subplots(figsize=(10, 6))
    result = total_efficiency_vs_fD(fD_array, feed_q=8.0,
                                    eta_blockage=0.95,
                                    eta_phase=0.98,
                                    eta_surface=0.99,
                                    eta_pol=0.98)

    ax.plot(result['f_D'], result['eta_spill'], 'b-', linewidth=2,
            label='$\\eta_{spill}$')
    ax.plot(result['f_D'], result['eta_taper'], 'r-', linewidth=2,
            label='$\\eta_{taper}$')
    ax.plot(result['f_D'], result['eta_total'], 'k-', linewidth=2.5,
            label='$\\eta_{total}$ (product with blockage/phase/pol/surf)')

    idx_max = np.argmax(result['eta_total'])
    ax.axvline(result['f_D'][idx_max], color='gray', linestyle='--', alpha=0.6)
    ax.annotate(f'Optimal f/D={result["f_D"][idx_max]:.2f}',
                xy=(result['f_D'][idx_max], result['eta_total'][idx_max]),
                xytext=(result['f_D'][idx_max]+0.15, result['eta_total'][idx_max]+0.02),
                arrowprops=dict(arrowstyle='->'))

    ax.set_xlabel('f / D')
    ax.set_ylabel('Efficiency')
    ax.set_title('Efficiency Decomposition vs f/D (Feed q = 8)')
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / 'fig15_6b_efficiency_decomposition.png', dpi=150)
    plt.close(fig)
    print("Saved: fig15_6b_efficiency_decomposition.png")
    print(f"\nOptimal f/D = {result['f_D'][idx_max]:.3f} "
          f"with η_total = {result['eta_total'][idx_max]:.4f}")
    print(f"  η_spill = {result['eta_spill'][idx_max]:.4f}")
    print(f"  η_taper = {result['eta_taper'][idx_max]:.4f}")

    return True


# ═══════════════════════════════════════════════════════════
#  verify_ch15 — Run all demos
# ═══════════════════════════════════════════════════════════

def verify_ch15():
    """
    Run all Chapter 15 demos and produce summary.
    Returns "PASS" on successful completion.
    """
    print("=" * 60)
    print("Balanis Ch15 — Reflector Antennas Verification")
    print("=" * 60)

    all_pass = True

    try:
        all_pass &= demo_parabolic_geometry()
        print("  [PASS] Demo 1: Parabolic Geometry")
    except Exception as e:
        print(f"  [FAIL] Demo 1: {e}")
        all_pass = False

    try:
        all_pass &= demo_aperture_pattern()
        print("  [PASS] Demo 2: Aperture Patterns")
    except Exception as e:
        print(f"  [FAIL] Demo 2: {e}")
        all_pass = False

    try:
        all_pass &= demo_feed_taper_spillover()
        print("  [PASS] Demo 3: Feed Taper & Spillover")
    except Exception as e:
        print(f"  [FAIL] Demo 3: {e}")
        all_pass = False

    try:
        all_pass &= demo_cassegrain_equivalent()
        print("  [PASS] Demo 4: Cassegrain Equivalent f/D")
    except Exception as e:
        print(f"  [FAIL] Demo 4: {e}")
        all_pass = False

    try:
        all_pass &= demo_ruze_equation()
        print("  [PASS] Demo 5: Ruze Equation")
    except Exception as e:
        print(f"  [FAIL] Demo 5: {e}")
        all_pass = False

    try:
        all_pass &= demo_total_efficiency_scan()
        print("  [PASS] Demo 6: Total Efficiency Scan")
    except Exception as e:
        print(f"  [FAIL] Demo 6: {e}")
        all_pass = False

    print("\n" + "=" * 60)
    if all_pass:
        print("Result: PASS — All demos completed successfully.")
    else:
        print("Result: FAIL — Some demos encountered errors.")

    return "PASS" if all_pass else "FAIL"


# ═══════════════════════════════════════════════════════════
#  Main
# ═══════════════════════════════════════════════════════════

if __name__ == '__main__':
    verify_ch15()
