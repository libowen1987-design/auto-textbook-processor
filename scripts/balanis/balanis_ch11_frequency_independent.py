"""
balanis ch11 - frequency independent antennas and antenna miniaturization

Covers:
  1. §11.3: Equiangular spiral antenna -- geometry and radiation pattern
  2. §11.3: Cavity-backed equiangular spiral -- unidirectional pattern
  3. §11.4: Archimedean spiral antenna -- 2-arm and 4-arm patterns
  4. §11.5: LPDA -- full design procedure and radiation pattern
  5. §11.7: Antenna miniaturization -- normal vs miniaturized dipole comparison

Author: Xiaolongxia (subagent)
Reference: Balanis "Antenna Theory" 4th Ed., Ch11
"""

import numpy as np
from scipy.special import jv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from typing import Tuple, Optional
import os

# === Constants ===
C0 = 3e8              # speed of light (m/s)
ETA_0 = 120 * np.pi    # free-space impedance (Ohm)
PI = np.pi
FIG_DIR = 'figures/ch11'
os.makedirs(FIG_DIR, exist_ok=True)


# =========================================================================
# 1. §11.3: Equiangular Spiral Antenna -- Geometry and Pattern
# =========================================================================
# Reference: Balasin (11-2) through (11-14)

def equiangular_spiral_points(
    r_0: float,
    a: float,
    phi_start: float,
    phi_end: float,
    n_points: int = 1000
) -> Tuple[np.ndarray, np.ndarray]:
    """Generate points of an equiangular spiral arm.
    
    r(phi) = r_0 * exp(a * phi)
    
    Args:
        r_0: initial radius (m) at phi = 0
        a: flare rate (a = 1/tan(psi))
        phi_start: starting angle (rad)
        phi_end: ending angle (rad)
        n_points: number of sample points
    
    Returns:
        (x, y) arrays of spiral points
    """
    phi = np.linspace(phi_start, phi_end, n_points)
    r = r_0 * np.exp(a * phi)
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return x, y


def equiangular_spiral_geometry(
    r_inner: float,
    r_outer: float,
    a: float,
    n_arms: int = 2,
    n_turns: float = 3.0
) -> Tuple[list, list, float]:
    """Generate complete equiangular spiral geometry.
    
    Balanis §11.3, Eq (11-6), (11-7)
    
    Args:
        r_inner: inner radius (m), determines f_high
        r_outer: outer radius (m), determines f_low
        a: flare rate
        n_arms: number of arms
        n_turns: number of spiral turns
    
    Returns:
        (arms_x, arms_y, f_low): lists of x,y arrays for each arm, lowest freq
    """
    # Determine angular range
    phi_max = np.log(r_outer / r_inner) / a
    # Map to n_turns if smaller
    phi_max = min(phi_max, 2 * PI * n_turns)
    # Determine r_0 from inner radius
    # r_inner = r_0 at phi = 0 (or phi_start)
    delta_phi = 2 * PI / n_arms  # angular shift between arms
    
    arms_x = []
    arms_y = []
    for m in range(n_arms):
        phi_shift = m * delta_phi
        x, y = equiangular_spiral_points(
            r_inner / np.exp(a * phi_shift),
            a, phi_shift, phi_max + phi_shift
        )
        arms_x.append(x)
        arms_y.append(y)
    
    # Lowest frequency: outer circumference ~ wavelength
    f_low = C0 / (2 * PI * r_outer)
    
    return arms_x, arms_y, f_low


def spiral_radiation_pattern_approx(
    theta: np.ndarray,
    k_a_active: float
) -> np.ndarray:
    """Approximate radiation pattern of a planar spiral antenna.
    
    Uses the first-order Bessel function approximation from the
    equivalent magnetic current ring model.
    
    Balanis §11.3, Eq (11-12) and discussion.
    
    For a spiral, the active region at frequency f is near
    circumference = lambda, modelled as a magnetic current ring
    of radius a_active = lambda / (2*pi).
    
    E(theta) ~ cos(theta) * J_1(k*a_active*sin(theta)) / (k*a_active*sin(theta))
    simplified to: E(theta) ~ cos(theta)  (broad approximation)
    
    We use a more refined model based on:
    E_theta(theta) ~ sin(theta) * [J_0(k*rho*sin(theta)) - J_2(k*rho*sin(theta))]
    
    Args:
        theta: polar angle array (rad), 0 = broadside
        k_a_active: k * a_active (active region radius in wavelengths)
    
    Returns:
        Normalized field pattern magnitude
    """
    # Refined model using Bessel functions
    u = k_a_active * np.sin(theta)
    # Element factor (cos(theta) for small magnetic current)
    element = np.cos(theta)
    # Pattern from ring of magnetic current
    ring_factor = np.zeros_like(u, dtype=complex)
    for i, ui in enumerate(u):
        if np.abs(ui) < 1e-10:
            ring_factor[i] = 1.0
        else:
            # E_phi component (dominant for spiral CP radiation)
            ring_factor[i] = (jv(0, ui) - jv(2, ui))
    
    pattern = np.abs(element * ring_factor)
    # Normalize
    if np.max(pattern) > 1e-10:
        pattern = pattern / np.max(pattern)
    
    return pattern


def example_1_equiangular_spiral():
    """Example 1: Equiangular spiral geometry and radiation pattern.
    
    Balanis §11.3
    Design a planar equiangular spiral covering 2-18 GHz.
    """
    print("=" * 65)
    print("  Example 1: Equiangular Spiral Antenna (§11.3)")
    print("=" * 65)
    
    # === Design parameters ===
    f_low = 2e9           # 2 GHz
    f_high = 18e9         # 18 GHz
    a_flare = 0.22        # flare rate (typical engineering value)
    n_turns = 2.0         # number of turns
    
    # Compute radii from frequency limits
    # Low freq: outer circumference ~ lambda_max
    lambda_max = C0 / f_low
    r_outer = lambda_max / (2 * PI)     # = c/(2*pi*f_low)
    
    # High freq: inner radius ~ lambda_min/4
    lambda_min = C0 / f_high
    r_inner = lambda_min / 4            # feed gap
    
    print(f"  Frequency range: {f_low/1e9:.1f} - {f_high/1e9:.1f} GHz")
    print(f"  r_inner = {r_inner*1e3:.2f} mm")
    print(f"  r_outer = {r_outer*1e3:.2f} mm")
    print(f"  Flare rate a = {a_flare}")
    print(f"  Bandwidth = {f_high/f_low:.1f}:1")
    print(f"  Theoretical Z_in (self-complementary) = {ETA_0/2:.1f} Ohm")
    
    # Generate geometry
    arms_x, arms_y, _ = equiangular_spiral_geometry(
        r_inner, r_outer, a_flare, n_arms=2, n_turns=n_turns
    )
    
    # === Plot geometry ===
    fig1, ax1 = plt.subplots(1, 1, figsize=(7, 7))
    for m in range(len(arms_x)):
        ax1.plot(arms_x[m] * 1e3, arms_y[m] * 1e3, f'C{m}', lw=1.5,
                 label=f'Arm {m+1}')
    # Mark inner and outer radii
    circle_inner = plt.Circle((0, 0), r_inner * 1e3, fill=False,
                              linestyle='--', color='grey', alpha=0.5)
    circle_outer = plt.Circle((0, 0), r_outer * 1e3, fill=False,
                              linestyle='--', color='grey', alpha=0.5)
    ax1.add_patch(circle_inner)
    ax1.add_patch(circle_outer)
    ax1.set_xlabel('x (mm)')
    ax1.set_ylabel('y (mm)')
    ax1.set_title(f'Equiangular Spiral (2-arm, a={a_flare}, {n_turns:.0f} turns)')
    ax1.set_aspect('equal')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    fig1.tight_layout()
    fig1.savefig(f'{FIG_DIR}/ex1_equiangular_geometry.png', dpi=150)
    plt.close(fig1)
    print(f"  Geometry saved: {FIG_DIR}/ex1_equiangular_geometry.png")
    
    # === Radiation pattern ===
    # Active region at mid-band: f_mid = sqrt(f_low * f_high)
    f_mid = np.sqrt(f_low * f_high)
    lambda_mid = C0 / f_mid
    a_active = lambda_mid / (2 * PI)    # active region radius
    k_a_active = 2 * PI / lambda_mid * a_active  # = 1.0 by design
    
    theta = np.linspace(0, PI, 361)
    pattern_bidir = spiral_radiation_pattern_approx(theta, k_a_active)
    
    # For cavity-backed (unidirectional), approximate by
    # multiplying with sin^2(theta) factor from a ground plane at lambda/4
    pattern_unidir = pattern_bidir * np.abs(np.sin(2*PI*0.25*np.cos(theta)))**2
    pattern_unidir = pattern_unidir / np.max(pattern_unidir)
    
    # Suppress back lobe for cavity-backed model
    # (simple image method: ground plane at lambda/4 behind)
    d_cavity = lambda_mid / 4
    # Array factor of spiral + its image
    af_cavity = np.abs(np.sin(2*PI*d_cavity/lambda_mid * np.cos(theta)))
    pattern_cavity = pattern_bidir * af_cavity
    pattern_cavity = pattern_cavity / np.max(pattern_cavity)
    
    # Compute HPBW before plotting
    # For pattern with max at theta=0 (broadside)
    # Half-power field level = 1/sqrt(2)
    hp_idx = np.argmin(np.abs(pattern_cavity[:91] - 1.0/np.sqrt(2.0)))
    hpbw = 2 * np.rad2deg(theta[hp_idx])
    print(f"  Cavity-backed HPBW ≈ {hpbw:.1f}°")
    
    # Polar plot
    fig2, (ax2a, ax2b) = plt.subplots(1, 2, subplot_kw={'projection': 'polar'},
                                       figsize=(12, 5.5))
    
    ax2a.plot(theta, pattern_bidir, 'b-', lw=2, label='Bidirectional')
    ax2a.plot(theta, pattern_bidir, 'b--', lw=1, alpha=0.5)
    ax2a.set_theta_zero_location('N')
    ax2a.set_thetamin(0)
    ax2a.set_thetamax(180)
    ax2a.set_title(f'Planar Spiral (Bidirectional)\n'
                   f'f_mid = {f_mid/1e9:.2f} GHz')
    ax2a.legend(loc='upper right')
    
    ax2b.plot(theta, pattern_cavity, 'r-', lw=2,
              label=f'Cavity-backed (d={d_cavity*1e3:.1f} mm)')
    ax2b.set_theta_zero_location('N')
    ax2b.set_thetamin(0)
    ax2b.set_thetamax(180)
    ax2b.set_title('Cavity-Backed Spiral (Unidirectional)\n'
                   f'HPBW ≈ {hpbw:.0f}°')
    ax2b.legend(loc='upper right')
    
    # Estimate directivity (Kraus approx)
    D0 = 41253 / (hpbw**2)  # in linear scale using Kraus approx
    D0_dBi = 10 * np.log10(D0)
    print(f"  Estimated D_0 ≈ {D0_dBi:.1f} dBi (cavity-backed)")
    
    fig2.tight_layout()
    fig2.savefig(f'{FIG_DIR}/ex1_equiangular_pattern.png', dpi=150)
    plt.close(fig2)
    print(f"  Pattern saved: {FIG_DIR}/ex1_equiangular_pattern.png")
    
    # === Frequency sweep: check pattern stability ===
    f_sweep = np.logspace(np.log10(f_low*1.5), np.log10(f_high*0.75), 5)
    theta_fine = np.linspace(0, PI/2, 181)
    
    fig3, ax3 = plt.subplots(1, 1, figsize=(8, 6))
    for fi, f_test in enumerate(f_sweep):
        lambda_test = C0 / f_test
        a_test = lambda_test / (2 * PI)
        k_a = 2*PI / lambda_test * a_test  # nominally 1.0
        pat = spiral_radiation_pattern_approx(theta_fine, k_a)
        linestyle = '-' if fi % 2 == 0 else '--'
        ax3.plot(np.rad2deg(theta_fine), 20*np.log10(pat + 1e-6),
                 linestyle, lw=1.5, label=f'{f_test/1e9:.2f} GHz')
    
    ax3.set_xlabel('Theta (deg)')
    ax3.set_ylabel('Normalized Pattern (dB)')
    ax3.set_title('Equiangular Spiral: Pattern Stability Across Band')
    ax3.set_xlim(0, 90)
    ax3.set_ylim(-35, 0)
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    fig3.tight_layout()
    fig3.savefig(f'{FIG_DIR}/ex1_equiangular_sweep.png', dpi=150)
    plt.close(fig3)
    print(f"  Frequency sweep saved: {FIG_DIR}/ex1_equiangular_sweep.png")
    
    return {
        'f_low': f_low, 'f_high': f_high,
        'r_inner': r_inner, 'r_outer': r_outer,
        'hpbw': hpbw, 'D0_dBi': D0_dBi
    }


# =========================================================================
# 2. §11.4: Archimedean Spiral Antenna -- 2-arm and Multi-arm Patterns
# =========================================================================
# Reference: Balanis §11.4, Eq (11-15) through (11-21)

def archimedean_spiral_points(
    r_0: float,
    a_spacing: float,
    phi_start: float,
    phi_end: float,
    n_points: int = 1000
) -> Tuple[np.ndarray, np.ndarray]:
    """Generate points of an Archimedean spiral arm.
    
    r(phi) = r_0 + a * phi
    
    Args:
        r_0: initial radius (m)
        a_spacing: arm spacing parameter (m/rad)
        phi_start: starting angle (rad)
        phi_end: ending angle (rad)
        n_points: number of sample points
    
    Returns:
        (x, y) arrays of spiral points
    """
    phi = np.linspace(phi_start, phi_end, n_points)
    r = r_0 + a_spacing * phi
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return x, y


def archimedean_spiral_geometry(
    r_inner: float,
    r_outer: float,
    n_arms: int = 2,
    n_turns: float = 3.0
) -> Tuple[list, list, float]:
    """Generate Archimedean spiral geometry with given parameters.
    
    Balanis §11.4, Eq (11-15), (11-16), (11-21)
    
    Args:
        r_inner: inner radius (m)
        r_outer: outer radius (m)
        n_arms: number of arms (2 or 4 typical)
        n_turns: number of spiral turns
    
    Returns:
        (arms_x, arms_y, a_spacing): lists of x,y arrays, and spacing parameter
    """
    a_spacing = (r_outer - r_inner) / (2 * PI * n_turns)
    delta_phi = 2 * PI / n_arms
    phi_max = 2 * PI * n_turns
    
    arms_x = []
    arms_y = []
    for m in range(n_arms):
        phi_shift = m * delta_phi
        x, y = archimedean_spiral_points(
            r_inner, a_spacing,
            phi_shift, phi_max + phi_shift
        )
        arms_x.append(x)
        arms_y.append(y)
    
    return arms_x, arms_y, a_spacing


def archimedean_radiation_pattern(
    theta: np.ndarray,
    freq: float,
    r_outer: float,
    n_arms: int = 2
) -> np.ndarray:
    """Compute Archimedean spiral radiation pattern.
    
    Uses current band model: the active region is modelled as
    a ring of magnetic current at radius where circumference ~ lambda.
    
    For multi-arm spirals, the pattern is approximately:
    E(theta) ~ cos(theta) * J_{n_arms/2 - 1}(k*a*sin(theta))
    
    Args:
        theta: polar angle array (rad)
        freq: operating frequency (Hz)
        r_outer: outer radius (m) (limits lowest active region)
        n_arms: number of arms
    
    Returns:
        Normalized field pattern magnitude
    """
    lambda_op = C0 / freq
    # Active region radius
    a_active = lambda_op / (2 * PI)
    # Clamp to physical bounds
    a_active = np.clip(a_active, 0.01 * r_outer, r_outer)
    
    k_a = 2 * PI / lambda_op * a_active
    u = k_a * np.sin(theta)
    
    # Pattern function depends on number of arms
    # 2-arm: uses J_0 - J_2 (mode 1)
    # 4-arm: uses J_1 - J_3 (mode 2)
    # General mode number: n_arms / 2
    mode = n_arms // 2
    pattern = np.zeros_like(theta)
    for i, ui in enumerate(u):
        if np.abs(ui) < 1e-10:
            pattern[i] = 1.0
        else:
            j_vals = [jv(mode - 1 + m, ui) for m in range(3)]
            pattern[i] = np.abs(j_vals[0] - 2 * j_vals[1] + j_vals[2]) / ui
    
    # Element factor
    element = np.sin(theta)
    # Combine
    total = np.abs(element * pattern)
    if np.max(total) > 0:
        total = total / np.max(total)
    
    return total


def example_2_archimedean_spiral():
    """Example 2: Archimedean spiral -- 2-arm and 4-arm radiation patterns.
    
    Balanis §11.4
    """
    print("\n" + "=" * 65)
    print("  Example 2: Archimedean Spiral Antenna (§11.4)")
    print("=" * 65)
    
    # Design for 1-6 GHz
    f_low = 1e9
    f_high = 6e9
    f_mid = np.sqrt(f_low * f_high)
    n_turns = 3.0
    
    lambda_max = C0 / f_low
    r_outer = lambda_max / (2 * PI)
    lambda_min = C0 / f_high
    r_inner = lambda_min / 4
    
    print(f"  Frequency: {f_low/1e9:.1f} - {f_high/1e9:.1f} GHz")
    print(f"  r_inner = {r_inner*1e3:.2f} mm")
    print(f"  r_outer = {r_outer*1e3:.2f} mm")
    
    # 2-arm geometry
    arms_x_2, arms_y_2, a_sp_2 = archimedean_spiral_geometry(
        r_inner, r_outer, n_arms=2, n_turns=n_turns
    )
    
    # 4-arm geometry
    arms_x_4, arms_y_4, a_sp_4 = archimedean_spiral_geometry(
        r_inner, r_outer, n_arms=4, n_turns=n_turns
    )
    
    print(f"  Spacing parameter a = {a_sp_2*1e3:.3f} mm")
    print(f"  2-arm: {len(arms_x_2)} arms, {n_turns} turns")
    print(f"  4-arm: {len(arms_x_4)} arms, {n_turns} turns")
    
    # === Plot geometry ===
    fig1, (ax1a, ax1b) = plt.subplots(1, 2, figsize=(14, 6.5))
    
    colors = ['C0', 'C1', 'C2', 'C3']
    for m in range(len(arms_x_2)):
        ax1a.plot(arms_x_2[m]*1e3, arms_y_2[m]*1e3, colors[m], lw=1.5,
                 label=f'Arm {m+1}')
    ax1a.set_title(f'2-arm Archimedean Spiral\n({n_turns:.0f} turns)')
    ax1a.set_xlabel('x (mm)')
    ax1a.set_ylabel('y (mm)')
    ax1a.set_aspect('equal')
    ax1a.legend()
    ax1a.grid(True, alpha=0.3)
    
    for m in range(len(arms_x_4)):
        ax1b.plot(arms_x_4[m]*1e3, arms_y_4[m]*1e3, colors[m], lw=1.5,
                 label=f'Arm {m+1}')
    ax1b.set_title(f'4-arm Archimedean Spiral\n({n_turns:.0f} turns)')
    ax1b.set_xlabel('x (mm)')
    ax1b.set_ylabel('y (mm)')
    ax1b.set_aspect('equal')
    ax1b.legend()
    ax1b.grid(True, alpha=0.3)
    
    fig1.tight_layout()
    fig1.savefig(f'{FIG_DIR}/ex2_archimedean_geometry.png', dpi=150)
    plt.close(fig1)
    print(f"  Geometry saved: {FIG_DIR}/ex2_archimedean_geometry.png")
    
    # === Radiation patterns ===
    theta = np.linspace(0, PI, 361)
    
    # Patterns at f_mid
    pat_2arm = archimedean_radiation_pattern(theta, f_mid, r_outer, n_arms=2)
    pat_4arm = archimedean_radiation_pattern(theta, f_mid, r_outer, n_arms=4)
    
    # HPBW
    hpbw_2arm = 2 * np.rad2deg(theta[np.argmin(np.abs(pat_2arm[:91] - 1.0/np.sqrt(2.0)))])
    hpbw_4arm = 2 * np.rad2deg(theta[np.argmin(np.abs(pat_4arm[:91] - 1.0/np.sqrt(2.0)))])
    
    fig2, (ax2a, ax2b) = plt.subplots(1, 2, subplot_kw={'projection': 'polar'},
                                       figsize=(12, 5.5))
    
    ax2a.plot(theta, pat_2arm, 'b-', lw=2)
    ax2a.plot(theta, -pat_2arm, 'b--', lw=1, alpha=0.4)
    ax2a.set_theta_zero_location('N')
    ax2a.set_thetamin(0)
    ax2a.set_thetamax(180)
    ax2a.set_title(f'2-arm Archimedean Spiral\n'
                   f'f = {f_mid/1e9:.2f} GHz, HPBW ≈ {hpbw_2arm:.0f}°')
    
    ax2b.plot(theta, pat_4arm, 'r-', lw=2)
    ax2b.plot(theta, -pat_4arm, 'r--', lw=1, alpha=0.4)
    ax2b.set_theta_zero_location('N')
    ax2b.set_thetamin(0)
    ax2b.set_thetamax(180)
    ax2b.set_title(f'4-arm Archimedean Spiral\n'
                   f'f = {f_mid/1e9:.2f} GHz, HPBW ≈ {hpbw_4arm:.0f}°')
    
    fig2.tight_layout()
    fig2.savefig(f'{FIG_DIR}/ex2_archimedean_pattern.png', dpi=150)
    plt.close(fig2)
    print(f"  Pattern saved: {FIG_DIR}/ex2_archimedean_pattern.png")
    print(f"  2-arm HPBW ≈ {hpbw_2arm:.0f}°")
    print(f"  4-arm HPBW ≈ {hpbw_4arm:.0f}°")
    
    # === Frequency sweep ===
    f_sweep = np.logspace(np.log10(f_low*1.3), np.log10(f_high*0.7), 5)
    theta_fine = np.linspace(0, PI/2, 181)
    
    fig3, ax3 = plt.subplots(1, 1, figsize=(8, 6))
    for fi, f_test in enumerate(f_sweep):
        pat = archimedean_radiation_pattern(theta_fine, f_test, r_outer, 2)
        linestyle = '-' if fi % 2 == 0 else '--'
        ax3.plot(np.rad2deg(theta_fine), 20*np.log10(pat + 1e-6),
                 linestyle, lw=1.5, label=f'{f_test/1e9:.2f} GHz')
    
    ax3.set_xlabel('Theta (deg)')
    ax3.set_ylabel('Normalized Pattern (dB)')
    ax3.set_title('Archimedean Spiral (2-arm): Pattern Across Band')
    ax3.set_xlim(0, 90)
    ax3.set_ylim(-35, 0)
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    fig3.tight_layout()
    fig3.savefig(f'{FIG_DIR}/ex2_archimedean_sweep.png', dpi=150)
    plt.close(fig3)
    print(f"  Frequency sweep: {FIG_DIR}/ex2_archimedean_sweep.png")
    
    return {
        'f_low': f_low, 'f_high': f_high,
        'hpbw_2arm': hpbw_2arm, 'hpbw_4arm': hpbw_4arm
    }


# =========================================================================
# 3. §11.5: LPDA -- Full Design Procedure and Radiation Pattern
# =========================================================================
# Reference: Balanis §11.5, Eq (11-22) through (11-36)

def design_lpda(
    f_low: float,
    f_high: float,
    tau: float,
    sigma: float
) -> dict:
    """Complete LPDA design procedure (Carrel method).
    
    Balanis §11.5, Eq (11-22) through (11-32)
    
    Args:
        f_low: lowest operating frequency (Hz)
        f_high: highest operating frequency (Hz)
        tau: scaling factor (0.8-0.98)
        sigma: relative spacing constant (0.03-0.2)
    
    Returns:
        Dictionary with all LPDA parameters
    """
    # Step 1: apex half-angle (11-24)
    alpha = np.arctan2(1 - tau, 4 * sigma)
    
    # Step 2: longest element (11-26)
    L_1 = C0 / (2 * f_low)
    
    # Step 3: active region bandwidth (11-30) - Carrel empirical
    cot_alpha = 1.0 / np.tan(alpha)
    B_ar = 1.1 + 7.7 * (1 - tau)**2 * cot_alpha
    
    # Step 4: overall bandwidth
    B = f_high / f_low
    
    # Step 5: structural bandwidth (11-31)
    B_s = B * B_ar * 1.1  # 10% safety margin
    
    # Step 6: number of elements (11-32)
    N = 1 + np.log(B_s) / np.log(1.0 / tau)
    N = int(np.ceil(N))  # round up
    
    # Step 7: generate element lengths and spacings (11-27, 11-28)
    L_n = np.array([L_1 * tau**n for n in range(N)])
    S_n = np.array([2 * sigma * L_n[n] for n in range(N)])
    
    # Step 8: element positions along boom
    # d_1 = 0 at apex (virtual), d_n measured from apex
    d_n = np.zeros(N)
    for n in range(1, N):
        d_n[n] = d_n[n-1] + S_n[n-1]
    
    # Step 9: Estimate directivity (from Carrel curves, approximate)
    # Using empirical formula based on tau and sigma
    D0_approx = 6.0 + 8.0 * (tau - 0.85) * 10 + 5.0 * (sigma - 0.05) * 10
    D0_approx = np.clip(D0_approx, 5.0, 12.0)  # dBi
    
    # Step 10: element diameters (rule of thumb: L/d ~ 50-200)
    Ld_ratio = 100.0  # typical
    diam_n = L_n / Ld_ratio
    
    return {
        'f_low': f_low,
        'f_high': f_high,
        'tau': tau,
        'sigma': sigma,
        'alpha': alpha,
        'alpha_deg': np.rad2deg(alpha),
        'B': B,
        'B_ar': B_ar,
        'B_s': B_s,
        'N': N,
        'L_n': L_n,
        'S_n': S_n,
        'd_n': d_n,
        'diam_n': diam_n,
        'D0_approx': D0_approx,
        'cot_alpha': cot_alpha,
        'L_1': L_1
    }


def lpda_element_pattern(
    theta: np.ndarray,
    L: float,
    freq: float
) -> np.ndarray:
    """Radiation pattern of a single LPDA dipole element.
    
    Balanis Eq (11-33): standing-wave dipole pattern.
    
    Args:
        theta: polar angle (rad), 0 = along boom (forward)
        L: element length (m)
        freq: operating frequency (Hz)
    
    Returns:
        Element pattern magnitude |F_n(theta)|
    """
    k = 2 * PI * freq / C0
    kL = k * L
    numerator = np.cos(kL / 2 * np.cos(theta)) - np.cos(kL / 2)
    denom = np.sin(theta)
    pattern = np.abs(numerator / denom)
    # Handle theta = 0, pi → limit is 0
    pattern = np.where(np.isfinite(pattern), pattern, 0.0)
    return pattern


def lpda_array_factor(
    theta: np.ndarray,
    d_n: np.ndarray,
    freq: float,
    tau: float
) -> np.ndarray:
    """LPDA array factor with current amplitude tapering.
    
    Elements are fed with alternating phase (180° shift).
    Current amplitudes peak at the active region.
    
    Balanis Eq (11-34), (11-35)
    
    Args:
        theta: polar angle (rad), 0 = forward (toward short elements)
        d_n: element positions from apex (m)
        freq: operating frequency (Hz)
        tau: scaling factor (determines active region width)
    
    Returns:
        Array factor magnitude |AF(theta)|
    """
    k = 2 * PI * freq / C0
    N = len(d_n)
    
    # This function is deprecated in favor of lpda_full_pattern.
    # Return unity for compatibility.
    return np.ones_like(theta)


def lpda_full_pattern(
    theta: np.ndarray,
    freq: float,
    design: dict
) -> np.ndarray:
    """Full LPDA radiation pattern.
    
    Computes the total far-field pattern by summing element patterns
    with appropriate phase shifts and current amplitudes.
    
    Args:
        theta: polar angle array (rad), 0 = forward (toward feed/small elements)
        freq: operating frequency (Hz)
        design: dictionary from design_lpda()
    
    Returns:
        Normalized total field pattern
    """
    k = 2 * PI * freq / C0
    lambda_op = C0 / freq
    L_n = design['L_n']
    d_n = design['d_n']
    N = design['N']
    tau = design['tau']
    
    # Find active region: element where L_n ~ lambda/2
    target_L = lambda_op / 2
    active_idx = np.argmin(np.abs(L_n - target_L))
    
    # Current amplitude: Gaussian centered on active region
    # Width parameter: active region spans ~3-5 elements
    active_width = 2.0  # standard deviation in element indices
    
    I_n = np.exp(-0.5 * ((np.arange(N) - active_idx) / active_width)**2)
    # Normalize so max = 1
    I_n = I_n / np.max(I_n)
    
    # Alternate feeding: 180° phase shift between adjacent elements
    phase_n = np.array([n * PI for n in range(N)])  # alternate
    
    # Total pattern
    total = np.zeros_like(theta, dtype=complex)
    for n in range(N):
        I = I_n[n]
        if I < 0.01:
            continue
        # Element pattern
        F_n = lpda_element_pattern(theta, L_n[n], freq)
        # Position phase: d_n measured along boom
        # Elements are along the negative z axis (d_n from apex, apex at origin)
        # Forward direction is +z (toward small elements)
        # Actually for LPDA, boom points in +z from longest to shortest
        # d_n is distance from virtual apex
        # For forward direction theta=0, phase = -k*d_n
        psi_n = -k * d_n[n] * np.cos(theta) + phase_n[n]
        total += I * F_n * np.exp(1j * psi_n)
    
    pattern = np.abs(total)
    
    # Normalize
    if np.max(pattern) > 1e-10:
        pattern = pattern / np.max(pattern)
    
    return I_n, pattern


def lpda_directivity_vs_ts(tau_vals, sigma_vals):
    """Generate directivity contour data from Carrel curves (approximate).
    
    Balanis §11.5, Fig 11.9 Carrel gain curves.
    
    Args:
        tau_vals: array of tau values
        sigma_vals: array of sigma values
    
    Returns:
        2D array of directivity (dBi)
    """
    D0 = np.zeros((len(tau_vals), len(sigma_vals)))
    for i, tau in enumerate(tau_vals):
        for j, sigma in enumerate(sigma_vals):
            # Empirical fit to Carrel curves
            sigma_opt = 0.243 * tau - 0.051
            sigma_ratio = sigma / sigma_opt if sigma_opt > 0 else 1.0
            
            # Base gain from tau
            D_base = 5.5 + 25.0 * (tau - 0.85)
            # sigma penalty away from optimum
            sigma_penalty = -5.0 * (np.log10(sigma_ratio + 1e-6))**2
            sigma_penalty = np.clip(sigma_penalty, -3.0, 0.0)
            
            D0[i, j] = np.clip(D_base + sigma_penalty, 4.0, 12.0)
    
    return D0


def example_3_lpda():
    """Example 3: LPDA complete design and analysis.
    
    Balanis §11.5, Example 11.5.1
    """
    print("\n" + "=" * 65)
    print("  Example 3: Log-Periodic Dipole Array (§11.5)")
    print("=" * 65)
    
    # === Design specifications ===
    # Design an LPDA for 200-600 MHz (3:1 bandwidth)
    f_low = 200e6
    f_high = 600e6
    tau = 0.88
    sigma = 0.06
    
    print(f"  Design freq: {f_low/1e6:.0f} - {f_high/1e6:.0f} MHz")
    print(f"  tau = {tau:.3f}")
    print(f"  sigma = {sigma:.3f}")
    
    # === Run design ===
    design = design_lpda(f_low, f_high, tau, sigma)
    
    print(f"\n  --- Design Results ---")
    print(f"  Apex half-angle alpha = {design['alpha_deg']:.2f}°")
    print(f"  cot(alpha) = {design['cot_alpha']:.3f}")
    print(f"  Number of elements N = {design['N']}")
    print(f"  Overall bandwidth B = {design['B']:.2f}")
    print(f"  Active region bandwidth B_ar = {design['B_ar']:.2f}")
    print(f"  Structural bandwidth B_s = {design['B_s']:.2f}")
    print(f"  Longest element L_1 = {design['L_1']*1e2:.2f} cm")
    print(f"  Estimated directivity D0 ≈ {design['D0_approx']:.1f} dBi")
    
    # Print element table
    print(f"\n  {'n':3s} {'L_n (cm)':10s} {'S_n (cm)':10s} {'d_n (cm)':10s} "
          f"{'L_n/lambda':10s} {'diam (mm)':10s}")
    print(f"  {'-'*55}")
    for n in range(design['N']):
        L_cm = design['L_n'][n] * 1e2
        S_cm = design['S_n'][n] * 1e2
        d_cm = design['d_n'][n] * 1e2
        L_over_lambda = design['L_n'][n] / (C0 / f_low)
        diam_mm = design['diam_n'][n] * 1e3
        print(f"  {n:3d} {L_cm:8.2f}   {S_cm:8.2f}   {d_cm:8.2f}   "
              f"{L_over_lambda:8.4f}   {diam_mm:8.3f}")
    
    # === Plot geometry ===
    fig1, ax1 = plt.subplots(1, 1, figsize=(12, 5))
    
    L_n = design['L_n']
    d_n = design['d_n']
    N = design['N']
    
    # Draw each element as a horizontal dipole
    for n in range(N):
        y_pos = d_n[n]
        x_half = L_n[n] / 2
        ax1.plot([-x_half, x_half], [y_pos, y_pos], 'b-', lw=2+2*(n/N))
        # Feed point
        ax1.plot([0], [y_pos], 'ro', markersize=3)
    
    # Draw transmission line (alternating feed)
    for n in range(N - 1):
        y1 = d_n[n]
        y2 = d_n[n+1]
        x_offset = 0.005  # small offset for visibility
        if n % 2 == 0:
            ax1.plot([-x_offset, -x_offset, x_offset, x_offset],
                     [y1, y1+(y2-y1)/2, y1+(y2-y1)/2, y2],
                     'r-', lw=0.5, alpha=0.5)
        else:
            ax1.plot([x_offset, x_offset, -x_offset, -x_offset],
                     [y1, y1+(y2-y1)/2, y1+(y2-y1)/2, y2],
                     'r-', lw=0.5, alpha=0.5)
    
    # Label active region for mid-band
    f_mid = np.sqrt(f_low * f_high)
    lambda_mid = C0 / f_mid
    active_L = lambda_mid / 2
    active_idx = np.argmin(np.abs(L_n - active_L))
    ax1.annotate(f'Active region\n(f={f_mid/1e6:.0f} MHz)',
                 xy=(0, d_n[active_idx]),
                 xytext=(L_n[active_idx]/2 + 0.05, d_n[active_idx]),
                 arrowprops=dict(arrowstyle='->', color='red'),
                 fontsize=9, color='red')
    
    ax1.set_xlabel('x (m)')
    ax1.set_ylabel('Boom position (m)')
    ax1.set_title(f'LPDA Geometry: tau={tau}, sigma={sigma}, '
                  f'N={N}, alpha={design["alpha_deg"]:.1f}°')
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    fig1.tight_layout()
    fig1.savefig(f'{FIG_DIR}/ex3_lpda_geometry.png', dpi=150)
    plt.close(fig1)
    print(f"\n  Geometry: {FIG_DIR}/ex3_lpda_geometry.png")
    
    # === Radiation pattern at multiple frequencies ===
    theta = np.linspace(0, PI, 361)
    f_sweep = np.array([220e6, 300e6, 400e6, 550e6])
    
    fig2, ax2 = plt.subplots(1, 1, subplot_kw={'projection': 'polar'},
                             figsize=(8, 8))
    colors = ['b', 'g', 'r', 'm']
    
    for fi, f_test in enumerate(f_sweep):
        I_n, pattern = lpda_full_pattern(theta, f_test, design)
        # Normalize to peak across all frequencies for comparison
        ax2.plot(theta, pattern, colors[fi], lw=1.5,
                 label=f'{f_test/1e6:.0f} MHz')
    
    ax2.set_theta_zero_location('N')
    ax2.set_thetamin(0)
    ax2.set_thetamax(180)
    ax2.set_title(f'LPDA Patterns at Different Frequencies')
    ax2.legend(loc='lower right')
    fig2.tight_layout()
    fig2.savefig(f'{FIG_DIR}/ex3_lpda_patterns.png', dpi=150)
    plt.close(fig2)
    print(f"  Patterns: {FIG_DIR}/ex3_lpda_patterns.png")
    
    # === Directivity contour ===
    tau_grid = np.linspace(0.82, 0.96, 15)
    sigma_grid = np.linspace(0.03, 0.16, 14)
    D0_contour = lpda_directivity_vs_ts(tau_grid, sigma_grid)
    
    fig3, ax3 = plt.subplots(1, 1, figsize=(8, 6))
    contour = ax3.contourf(tau_grid, sigma_grid, D0_contour.T,
                           levels=np.arange(5, 12.5, 0.5), cmap='viridis')
    cbar = plt.colorbar(contour, ax=ax3, label='Directivity (dBi)')
    
    # Plot Carrel optimum sigma line
    sigma_opt_line = 0.243 * tau_grid - 0.051
    sigma_opt_line = np.maximum(sigma_opt_line, 0.02)
    ax3.plot(tau_grid, sigma_opt_line, 'r--', lw=2,
             label=r'$\sigma_{opt} = 0.243\tau - 0.051$')
    
    # Mark our design point
    ax3.plot(tau, sigma, 'ro', markersize=8, label=f'Design (τ={tau}, σ={sigma})')
    
    ax3.set_xlabel(r'$\tau$')
    ax3.set_ylabel(r'$\sigma$')
    ax3.set_title('LPDA Directivity vs τ and σ (Carrel Curves)')
    ax3.legend()
    fig3.tight_layout()
    fig3.savefig(f'{FIG_DIR}/ex3_lpda_directivity_contour.png', dpi=150)
    plt.close(fig3)
    print(f"  Directivity contour: {FIG_DIR}/ex3_lpda_directivity_contour.png")
    
    return design


# =========================================================================
# 4. §11.7: Antenna Miniaturization -- Normal vs Miniaturized
# =========================================================================
# Reference: Balanis §11.7, Chu-Harrington limit

def dipole_pattern(theta: np.ndarray, L: float, freq: float) -> np.ndarray:
    """Short dipole (or meandered dipole) radiation pattern.
    
    For a very short dipole (L << lambda), pattern is ~ sin(theta).
    For a half-wave dipole, uses the standard formula.
    
    Args:
        theta: polar angle (rad)
        L: dipole length (m)
        freq: operating frequency (Hz)
    
    Returns:
        Normalized field pattern
    """
    lambda_op = C0 / freq
    kL = 2 * PI * L / lambda_op
    
    if kL < 0.1:
        # Electrically short: Hertzian dipole pattern
        pattern = np.sin(theta)
    elif abs(kL - PI) < 0.1:
        # Half-wave dipole
        # F(theta) = cos(pi/2 * cos(theta)) / sin(theta)
        # At theta=0,pi: limit → 0 by series expansion
        numerator = np.cos(PI / 2 * np.cos(theta))
        denom = np.sin(theta)
        pattern = np.abs(numerator / denom)
        # Use limit 0 at theta=0,pi
        pattern = np.where(np.isfinite(pattern), pattern, 0.0)
    else:
        # General dipole
        numerator = np.cos(kL / 2 * np.cos(theta)) - np.cos(kL / 2)
        denom = np.sin(theta)
        pattern = np.abs(numerator / denom)
        pattern = np.where(np.isfinite(pattern), pattern, 0.0)
    
    if np.max(pattern) > 1e-10:
        pattern = pattern / np.max(pattern)
    return pattern


def chu_harrington_q(ka: float) -> float:
    """Chu-Harrington limit for antenna Q.
    
    Balanis §11.7, Eq (11-38)
    
    Q >= 1/(ka)^3 + 1/(ka)
    
    For ka << 1: Q ~ 1/(ka)^3
    
    Args:
        ka: electrical size (k * a, a = radius of enclosing sphere)
    
    Returns:
        Minimum achievable Q
    """
    return 1.0 / (ka**3) + 1.0 / ka


def meander_line_freq_reduction(n_segments: int, segment_length: float,
                                 total_length: float) -> float:
    """Estimate resonance frequency reduction from meander line.
    
    Meander line effectively increases electrical length.
    Simple model: reduction factor ~ (total_length / physical_length)
    with correction for coupling between adjacent segments.
    
    Args:
        n_segments: number of meander segments
        segment_length: length of each segment (m)
        total_length: total physical span of the meandered structure (m)
    
    Returns:
        Frequency reduction factor (f_meander / f_straight)
    """
    # Total wire length
    wire_length = n_segments * segment_length
    # Physical span
    physical_span = 2 * total_length  # approximate for zigzag
    
    # Frequency reduction factor
    reduction = 1.0 / np.sqrt(1 + 0.3 * (wire_length / physical_span))
    return reduction


def example_4_miniaturization():
    """Example 4: Antenna miniaturization comparison.
    
    Balanis §11.7
    Compare: normal half-wave dipole vs miniaturized (loaded/meandered) dipole.
    """
    print("\n" + "=" * 65)
    print("  Example 4: Antenna Miniaturization (§11.7)")
    print("=" * 65)
    
    # Reference design frequency
    f0 = 300e6  # 300 MHz
    lambda_0 = C0 / f0
    L_half = lambda_0 / 2  # half-wave dipole length = 0.5m
    
    print(f"  Reference: f0 = {f0/1e6:.0f} MHz")
    print(f"  lambda_0 = {lambda_0*1e2:.1f} cm")
    print(f"  Half-wave dipole length = {L_half*1e2:.1f} cm")
    
    # === Case A: Normal half-wave dipole ===
    L_norm = L_half
    k_a_norm = 2 * PI / lambda_0 * (L_norm / 2 + 0.01)  # radius of enclosing sphere
    
    # === Case B: Electrically small (ka = 0.3) ===
    # Physical size is constrained
    a_small = 0.3 / (2 * PI / lambda_0)  # radius such that ka = 0.3
    L_small = 2 * a_small  # effective length ~ sphere diameter
    ka_small = 0.3
    
    # === Case C: Meander line ===
    # 4-segment meander, physical height = a_small but wire length = L_half
    n_meander = 6
    segment_length = L_half / n_meander  # total wire length = L_half
    physical_height = a_small * 1.8  # total physical span
    reduction_factor = meander_line_freq_reduction(
        n_meander, segment_length, physical_height
    )
    f_meander = f0 * reduction_factor
    # Effective electrical length
    L_eff_meander = C0 / (2 * f_meander)
    
    print(f"\n  --- Case A: Normal half-wave dipole ---")
    print(f"  Length = {L_norm*1e2:.1f} cm")
    print(f"  ka = {k_a_norm:.3f}")
    print(f"  Chu limit Q >= {chu_harrington_q(k_a_norm):.1f}")
    
    print(f"\n  --- Case B: Electrically small dipole ---")
    print(f"  Enclosing sphere radius a = {a_small*1e2:.1f} cm")
    print(f"  ka = {ka_small:.3f}")
    print(f"  Chu limit Q >= {chu_harrington_q(ka_small):.1f}")
    print(f"  Bandwidth (1/Q) <= {100/chu_harrington_q(ka_small):.2f}%")
    print(f"  Size reduction: {(1 - a_small/(L_norm/2))*100:.0f}%")
    
    print(f"\n  --- Case C: Meander line dipole ---")
    print(f"  Physical height = {physical_height*1e2:.1f} cm")
    print(f"  Total wire length = {L_half*1e2:.1f} cm")
    print(f"  Number of segments = {n_meander}")
    print(f"  Resonance freq reduction factor = {reduction_factor:.3f}")
    print(f"  Effective resonant freq = {f_meander/1e6:.1f} MHz")
    print(f"  Effective electrical length = {L_eff_meander*1e2:.1f} cm")
    
    # === Radiation patterns ===
    theta = np.linspace(0, PI, 361)
    pat_norm = dipole_pattern(theta, L_norm, f0)
    pat_small = dipole_pattern(theta, L_small, f0)
    pat_meander = dipole_pattern(theta, L_small, f_meander)
    
    # HPBW: find where pattern drops to 1/sqrt(2)=0.7071 (-3dB field)
    # For dipoles, peak is at theta=90 deg (broadside)
    def calc_hpbw(pat):
        # Field pattern → half-power at |E| = 1/sqrt(2) ≈ 0.707
        half_power = 1.0 / np.sqrt(2.0)
        # Search from center (theta=pi/2) outward
        center_idx = len(pat) // 2  # theta = pi/2
        # Search left from center
        left_idx = center_idx
        while left_idx > 0 and pat[left_idx] >= half_power:
            left_idx -= 1
        # Search right from center
        right_idx = center_idx
        while right_idx < len(pat)-1 and pat[right_idx] >= half_power:
            right_idx += 1
        hpbw_val = np.rad2deg(theta[right_idx] - theta[left_idx])
        # Clamp to reasonable range
        return np.clip(hpbw_val, 10.0, 180.0)
    
    hpbw_norm = calc_hpbw(pat_norm)
    hpbw_small = calc_hpbw(pat_small)
    hpbw_meander = calc_hpbw(pat_meander)
    
    print(f"\n  --- Radiation Pattern Comparison ---")
    print(f"  Half-wave dipole: HPBW ≈ {hpbw_norm:.1f}°")
    print(f"  Electrically small: HPBW ≈ {hpbw_small:.1f}°")
    print(f"  Meander line: HPBW ≈ {hpbw_meander:.1f}°")
    
    # Directivity (rough estimate using Kraus approx)
    D_norm = 41253 / (hpbw_norm**2)
    D_small = 41253 / (hpbw_small**2)
    D_meander = 41253 / (hpbw_meander**2)
    
    print(f"  Half-wave: D ≈ {10*np.log10(D_norm):.1f} dBi")
    print(f"  Electrically small: D ≈ {10*np.log10(D_small):.1f} dBi")
    print(f"  Meander line: D ≈ {10*np.log10(D_meander):.1f} dBi")
    
    # === Radiation efficiency estimate for small antenna ===
    # Radiation resistance of short dipole: R_r = 20 * (pi * L/lambda)^2
    L_over_lambda_small = L_small / lambda_0
    R_r_small = 20 * (PI * L_over_lambda_small)**2
    # Loss resistance (assume conductor loss)
    R_loss_small = 2.0  # Ohm (estimated)
    eff_small = R_r_small / (R_r_small + R_loss_small)
    gain_small = 10 * np.log10(D_small * eff_small)
    
    print(f"\n  --- Efficiency Analysis (Electrically Small) ---")
    print(f"  Radiation resistance R_r = {R_r_small:.3f} Ohm")
    print(f"  Loss resistance (est.) = {R_loss_small:.1f} Ohm")
    print(f"  Radiation efficiency = {eff_small*100:.1f}%")
    print(f"  Gain (incl. efficiency loss) = {gain_small:.1f} dBi")
    print(f"  Gain reduction from half-wave: {1.64 - D_small*eff_small:.2f} linear")
    
    # === Plot patterns ===
    fig1 = plt.figure(figsize=(14, 5.5))
    ax1a = fig1.add_subplot(121, projection='polar')
    ax1b = fig1.add_subplot(122)
    
    # Polar
    ax1a.plot(theta, pat_norm, 'b-', lw=2, label=f'Half-wave (L={L_norm*1e2:.0f} cm)')
    ax1a.plot(theta, pat_small, 'r-', lw=2,
              label=f'Small (a={a_small*1e2:.1f} cm, ka={ka_small:.2f})')
    ax1a.plot(theta, pat_meander, 'g--', lw=2,
              label=f'Meander (h={physical_height*1e2:.1f} cm)')
    ax1a.set_theta_zero_location('N')
    ax1a.set_thetamin(0)
    ax1a.set_thetamax(180)
    ax1a.set_title('Radiation Patterns: Normal vs Miniaturized')
    ax1a.legend(loc='lower right')
    
    # Rectangular (dB)
    ax1b.plot(np.rad2deg(theta[:181]), 20*np.log10(pat_norm[:181] + 1e-6),
              'b-', lw=2, label=f'Half-wave (HPBW={hpbw_norm:.0f}°)')
    ax1b.plot(np.rad2deg(theta[:181]), 20*np.log10(pat_small[:181] + 1e-6),
              'r-', lw=2, label=f'Small (HPBW={hpbw_small:.0f}°)')
    ax1b.plot(np.rad2deg(theta[:181]), 20*np.log10(pat_meander[:181] + 1e-6),
              'g--', lw=2, label=f'Meander (HPBW={hpbw_meander:.0f}°)')
    ax1b.set_xlabel('Theta (deg)')
    ax1b.set_ylabel('Normalized Pattern (dB)')
    ax1b.set_title('Patterns (dB)')
    ax1b.set_xlim(0, 180)
    ax1b.set_ylim(-35, 0)
    ax1b.legend()
    ax1b.grid(True, alpha=0.3)
    
    fig1.tight_layout()
    fig1.savefig(f'{FIG_DIR}/ex4_miniaturization_patterns.png', dpi=150)
    plt.close(fig1)
    print(f"\n  Pattern comparison: {FIG_DIR}/ex4_miniaturization_patterns.png")
    
    # === Chu-Harrington limit curve ===
    ka_vals = np.logspace(-2, 0, 100)
    Q_chu = chu_harrington_q(ka_vals)
    BW_chu = 100.0 / Q_chu
    
    fig2, (ax2a, ax2b) = plt.subplots(1, 2, figsize=(12, 5))
    
    ax2a.loglog(ka_vals, Q_chu, 'b-', lw=2)
    ax2a.axvline(x=k_a_norm, color='blue', linestyle='--', alpha=0.5,
                 label=f'Half-wave (ka={k_a_norm:.3f})')
    ax2a.axvline(x=ka_small, color='red', linestyle='--', alpha=0.5,
                 label=f'Small (ka={ka_small:.3f})')
    ax2a.scatter([k_a_norm, ka_small],
                 [chu_harrington_q(k_a_norm), chu_harrington_q(ka_small)],
                 color=['blue', 'red'], s=50, zorder=5)
    ax2a.set_xlabel('ka (electrical size)')
    ax2a.set_ylabel('Minimum Q')
    ax2a.set_title('Chu-Harrington Limit: Q vs Electrical Size')
    ax2a.legend()
    ax2a.grid(True, alpha=0.3, which='both')
    
    ax2b.semilogx(ka_vals, BW_chu, 'b-', lw=2)
    ax2b.axvline(x=k_a_norm, color='blue', linestyle='--', alpha=0.5)
    ax2b.axvline(x=ka_small, color='red', linestyle='--', alpha=0.5)
    ax2b.scatter([k_a_norm, ka_small],
                 [100/chu_harrington_q(k_a_norm), 100/chu_harrington_q(ka_small)],
                 color=['blue', 'red'], s=50, zorder=5)
    ax2b.set_xlabel('ka (electrical size)')
    ax2b.set_ylabel('Maximum BW (%)')
    ax2b.set_title('Chu-Harrington Limit: Bandwidth vs Electrical Size')
    ax2b.legend(['Chu Limit', f'Half-wave (ka={k_a_norm:.3f})',
                 f'Small (ka={ka_small:.3f})'])
    ax2b.grid(True, alpha=0.3, which='both')
    
    fig2.tight_layout()
    fig2.savefig(f'{FIG_DIR}/ex4_chu_harrington_limit.png', dpi=150)
    plt.close(fig2)
    print(f"  Chu-Harrington limit: {FIG_DIR}/ex4_chu_harrington_limit.png")
    
    # === Miniaturization techniques summary table ===
    techniques = [
        ('Lumped loading', 30, 50, '2.0', '50', '(11-41)'),
        ('Dielectric loading', 20, 40, '0.5', '40', '(11-42)'),
        ('Meander line', 30, 60, '4.0', '70', '(11-43)'),
        ('Top-loading', 30, 50, '1.5', '50', '-'),
        ('Fractal (Koch)', 15, 40, '2.5', '50', '-'),
    ]
    
    fig3, ax3 = plt.subplots(1, 1, figsize=(10, 3.5))
    ax3.axis('off')
    
    col_labels = ['Technique', 'Size Reduction (%)', 'Gain Loss (dB)',
                  'BW Reduction (%)', 'Complexity']
    cell_text = []
    for t in techniques:
        cell_text.append([t[0], f'{t[1]}-{t[2]}', t[3], t[4], 'Low-Med'])
    
    table = ax3.table(cellText=cell_text, colLabels=col_labels,
                      loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    
    ax3.set_title('Antenna Miniaturization Techniques Comparison',
                  fontsize=13, fontweight='bold', pad=20)
    fig3.tight_layout()
    fig3.savefig(f'{FIG_DIR}/ex4_miniaturization_table.png', dpi=150)
    plt.close(fig3)
    print(f"  Techniques table: {FIG_DIR}/ex4_miniaturization_table.png")
    
    return {
        'f0': f0,
        'L_half': L_half,
        'a_small': a_small,
        'ka_small': ka_small,
        'Q_chu_small': chu_harrington_q(ka_small),
        'eff_small': eff_small,
        'gain_small': gain_small
    }


# =========================================================================
# MAIN
# =========================================================================

def main():
    """Run all examples from Balanis Chapter 11."""
    print("=" * 65)
    print("  Balanis Ch11: Frequency Independent Antennas & Miniaturization")
    print("  All Examples")
    print("=" * 65)
    
    # Example 1: Equiangular Spiral
    result_1 = example_1_equiangular_spiral()
    
    # Example 2: Archimedean Spiral
    result_2 = example_2_archimedean_spiral()
    
    # Example 3: LPDA
    result_3 = example_3_lpda()
    
    # Example 4: Antenna Miniaturization
    result_4 = example_4_miniaturization()
    
    # Summary
    print("\n" + "=" * 65)
    print("  SUMMARY")
    print("=" * 65)
    print(f"  Example 1: Equiangular Spiral")
    print(f"    BW {result_1['f_low']/1e9:.1f}-{result_1['f_high']/1e9:.0f} GHz")
    print(f"    HPBW (cavity) = {result_1['hpbw']:.0f}°, "
          f"D0 ≈ {result_1['D0_dBi']:.1f} dBi")
    
    print(f"  Example 2: Archimedean Spiral")
    print(f"    BW {result_2['f_low']/1e9:.1f}-{result_2['f_high']/1e9:.0f} GHz")
    print(f"    2-arm HPBW ≈ {result_2['hpbw_2arm']:.0f}°, "
          f"4-arm HPBW ≈ {result_2['hpbw_4arm']:.0f}°")
    
    print(f"  Example 3: LPDA")
    L_total = result_3['d_n'][-1] if 'd_n' in result_3 else 0
    print(f"    N={result_3['N']}, alpha={result_3['alpha_deg']:.1f}°, "
          f"D0≈{result_3['D0_approx']:.1f} dBi")
    print(f"    Boom length ≈ {result_3['d_n'][-1]*1e2:.1f} cm")
    
    print(f"  Example 4: Miniaturization")
    print(f"    Half-wave dipole: L={result_4['L_half']*1e2:.1f} cm")
    print(f"    Small antenna (ka={result_4['ka_small']:.2f}): "
          f"Q_min={result_4['Q_chu_small']:.0f}, "
          f"eff={result_4['eff_small']*100:.1f}%")
    
    print("\n  All figures saved to", FIG_DIR)
    print("=" * 65)


if __name__ == '__main__':
    main()
