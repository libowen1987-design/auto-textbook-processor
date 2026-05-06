"""
Balanis Ch11 — Frequency Independent Antennas, Antenna Miniaturization & Fractal Antennas

Implements:
  - Equiangular spiral antenna geometry and radiation pattern
  - Archimedean spiral antenna geometry
  - Log-Periodic Dipole Array (LPDA) full design (Carrel procedure)
  - LPDA directivity contours (τ vs σ)
  - Spiral active-region radiation pattern approximation
  - Koch fractal dipole geometry

References: Balanis 4E Ch.11, Carrel (1961), DuHamel & Isbell (1957), Rumsey (1957)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from typing import Tuple, Optional, Dict
import os

# Physical constants
C0: float = 299792458        # speed of light [m/s]
ETA_0: float = 120.0 * np.pi  # free-space impedance [Ω] ≈ 376.99
PI: float = np.pi

# Output directory
FIG_DIR = 'figures/ch11'
os.makedirs(FIG_DIR, exist_ok=True)


# =========================================================================
# 11.3 Equiangular Spiral Antenna
# =========================================================================

def equiangular_spiral_arm(
    r0: float,
    a: float,
    phi_start: float,
    phi_end: float,
    n_points: int = 2000
) -> Tuple[np.ndarray, np.ndarray]:
    """Generate the (x, y) coordinates of one equiangular spiral arm.

    r(ϕ) = r0 · exp(a · ϕ)

    Parameters
    ----------
    r0 : float
        Initial radius at ϕ = 0 [m]
    a : float
        Spiral growth rate: a = 1 / tan(ψ₀)
    phi_start : float
        Starting angle [rad]
    phi_end : float
        Ending angle [rad]  (positive = counter-clockwise)
    n_points : int
        Number of sample points

    Returns
    -------
    x, y : ndarray
        Cartesian coordinates of the spiral arm
    """
    phi: np.ndarray = np.linspace(phi_start, phi_end, n_points)
    r: np.ndarray = r0 * np.exp(a * phi)
    x: np.ndarray = r * np.cos(phi)
    y: np.ndarray = r * np.sin(phi)
    return x, y


def equiangular_spiral_geometry(
    r0: float = 0.001,
    a: float = 0.22,
    n_turns: float = 5.0,
    n_points: int = 2000
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Generate both arms of a planar equiangular spiral antenna.

    Arm 1: ϕ ∈ [0, 2π · n_turns]
    Arm 2: ϕ ∈ [π, π + 2π · n_turns]   (shifted by π)

    Parameters
    ----------
    r0 : float
        Inner radius at ϕ = 0 [m]
    a : float
        Spiral growth rate (typical: 0.15–0.35)
    n_turns : float
        Number of turns
    n_points : int

    Returns
    -------
    x1, y1, x2, y2 : ndarray
        Coordinates of the two spiral arms
    """
    phi_end: float = 2.0 * PI * n_turns

    x1, y1 = equiangular_spiral_arm(r0, a, 0.0, phi_end, n_points)
    x2, y2 = equiangular_spiral_arm(r0, a, PI, PI + phi_end, n_points)

    return x1, y1, x2, y2


def equiangular_spiral_lowest_frequency(
    r_outer: float
) -> float:
    """Lowest operating frequency of an equiangular spiral antenna [Hz].

    f_low ≈ c / (2π · r_outer)   when λ ≈ circumference of outer ring

    Parameters
    ----------
    r_outer : float
        Outer radius of the spiral [m]

    Returns
    -------
    f_low : float
        Approximate lowest frequency [Hz]
    """
    return C0 / (2.0 * PI * r_outer)


def equiangular_spiral_self_impedance(is_self_complementary: bool = True) -> float:
    """Input impedance of an equiangular spiral antenna.

    For strictly self-complementary structure: Z_in = η₀ / 2 ≈ 188.5 Ω

    Parameters
    ----------
    is_self_complementary : bool
        Whether the structure is self-complementary

    Returns
    -------
    Z_in : float
        Input impedance [Ω]
    """
    if is_self_complementary:
        return ETA_0 / 2.0   # ≈ 188.5 Ω
    else:
        return ETA_0 / 2.0   # practical designs use ~150–200 Ω


def plot_equiangular_spiral() -> None:
    """Fig 11.1: Equiangular spiral geometry visualization."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # --- Panel (a): Standard spiral (a = 0.22, r0 = 0.001) ---
    x1, y1, x2, y2 = equiangular_spiral_geometry(
        r0=0.001, a=0.22, n_turns=4.0
    )
    ax = axes[0]
    ax.plot(x1, y1, 'b-', linewidth=1.2, label='Arm 1')
    ax.plot(x2, y2, 'r-', linewidth=1.2, label='Arm 2')
    ax.set_aspect('equal')
    ax.set_title(r'Equiangular Spiral: $a=0.22$, $r_0=0.001$')
    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # --- Panel (b): Different growth rates ---
    ax = axes[1]
    for a_val, color, label in zip(
        [0.1, 0.22, 0.35],
        ['green', 'blue', 'orange'],
        [r'$a=0.10$', r'$a=0.22$', r'$a=0.35$']
    ):
        x1, y1, _, _ = equiangular_spiral_geometry(
            r0=0.001, a=a_val, n_turns=3.0
        )
        ax.plot(x1, y1, '-', color=color, linewidth=1.0, label=label)
    ax.set_aspect('equal')
    ax.set_title('Growth Rate Comparison')
    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig11_1_equiangular_spiral.png', dpi=150)
    plt.close()
    print(f"  Saved fig11_1_equiangular_spiral.png")


# =========================================================================
# 11.3 Archimedean Spiral Antenna
# =========================================================================

def archimedean_spiral_arm(
    r0: float,
    a: float,
    phi_start: float,
    phi_end: float,
    n_points: int = 2000
) -> Tuple[np.ndarray, np.ndarray]:
    """Generate the (x, y) coordinates of one Archimedean spiral arm.

    r(ϕ) = r₀ + a · ϕ

    Parameters
    ----------
    r0 : float
        Initial radius at ϕ = 0 [m]
    a : float
        Spiral spacing parameter [m/rad]
    phi_start : float
        Starting angle [rad]
    phi_end : float
        Ending angle [rad]
    n_points : int

    Returns
    -------
    x, y : ndarray
    """
    phi: np.ndarray = np.linspace(phi_start, phi_end, n_points)
    r: np.ndarray = r0 + a * phi
    x: np.ndarray = r * np.cos(phi)
    y: np.ndarray = r * np.sin(phi)
    return x, y


def archimedean_spiral_geometry(
    r0: float = 0.001,
    a: float = 0.001,
    n_turns: float = 5.0,
    n_points: int = 2000
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Generate both arms of a planar Archimedean spiral.

    Parameters
    ----------
    r0 : float
        Inner radius [m]
    a : float
        Spacing per radian [m/rad]
    n_turns : float
        Number of turns
    n_points : int

    Returns
    -------
    x1, y1, x2, y2 : ndarray
    """
    phi_end: float = 2.0 * PI * n_turns

    x1, y1 = archimedean_spiral_arm(r0, a, 0.0, phi_end, n_points)
    x2, y2 = archimedean_spiral_arm(r0, a, PI, PI + phi_end, n_points)

    return x1, y1, x2, y2


def plot_spiral_comparison() -> None:
    """Fig 11.2: Compare equiangular vs Archimedean spiral geometry."""
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Equiangular
    x1, y1, x2, y2 = equiangular_spiral_geometry(
        r0=0.002, a=0.22, n_turns=4.0
    )
    ax = axes[0]
    ax.plot(x1, y1, 'b-', linewidth=1.2)
    ax.plot(x2, y2, 'r-', linewidth=1.2)
    ax.set_aspect('equal')
    ax.set_title('Equiangular Spiral\n(r ∝ e^{aφ})')
    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.grid(True, alpha=0.3)

    # Archimedean (adjusted a for visual comparison)
    x1a, y1a, x2a, y2a = archimedean_spiral_geometry(
        r0=0.002, a=0.002, n_turns=4.0
    )
    ax = axes[1]
    ax.plot(x1a, y1a, 'b-', linewidth=1.2)
    ax.plot(x2a, y2a, 'r-', linewidth=1.2)
    ax.set_aspect('equal')
    ax.set_title('Archimedean Spiral\n(r ∝ r₀ + aφ)')
    ax.set_xlabel('x [m]')
    ax.set_ylabel('y [m]')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig11_2_spiral_comparison.png', dpi=150)
    plt.close()
    print(f"  Saved fig11_2_spiral_comparison.png")


# =========================================================================
# Spiral Radiation Pattern (Active Region Approximation)
# =========================================================================

def spiral_active_region_pattern(
    theta: np.ndarray,
    n_loops: int = 3,
    d_loop: float = 0.5
) -> np.ndarray:
    """Approximate broadside radiation pattern of a planar spiral antenna.

    The spiral is approximated as N concentric current loops radiating
    in the far field.  The active region (circumference ≈ λ) dominates.

    Each small loop of radius a has pattern: sinθ.
    N loops at slightly different radii → combined broadside pattern.

    Parameters
    ----------
    theta : ndarray
        Observation angles [rad], 0 = zenith (broadside)
    n_loops : int
        Number of active-region current loops
    d_loop : float
        Effective spacing between active current loops [wavelengths]

    Returns
    -------
    E_theta : ndarray
        Normalized far-field magnitude |E_θ|
    """
    # Each loop has pattern ~ sinθ. Sum with phase from position.
    pattern: np.ndarray = np.zeros_like(theta, dtype=complex)
    k_d: float = 2.0 * PI * d_loop

    for n in range(n_loops):
        # Amplitude decays along spiral
        amplitude: float = np.exp(-0.5 * n)
        # Phase center at z = n * d_loop * lambda
        phase: float = k_d * n * np.cos(theta)
        pattern += amplitude * np.sin(theta) * np.exp(1j * phase)

    return np.abs(pattern) / np.max(np.abs(pattern))


def plot_spiral_radiation_pattern() -> None:
    """Fig 11.3: Approximate spiral antenna radiation pattern."""
    theta: np.ndarray = np.linspace(0.01, PI - 0.01, 361)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Panel (a): Polar plot — broadside pattern
    ax = plt.subplot(121, projection='polar')
    for n_loops, style, label in zip(
        [1, 3, 6],
        ['--', '-', ':'],
        ['1 loop', '3 loops', '6 loops']
    ):
        pattern: np.ndarray = spiral_active_region_pattern(
            theta, n_loops=n_loops, d_loop=0.3
        )
        ax.plot(theta, pattern, style, linewidth=1.2, label=label)
    ax.set_theta_zero_location('N')
    ax.set_thetamin(0)
    ax.set_thetamax(180)
    ax.set_title('Spiral Broadside Pattern', va='bottom')
    ax.legend(loc='lower right', fontsize=8)

    # Panel (b): Cartesian
    ax = axes[1]
    for n_loops, style, label in zip(
        [1, 3, 6],
        ['--', '-', ':'],
        ['1 loop', '3 loops', '6 loops']
    ):
        pattern = spiral_active_region_pattern(
            theta, n_loops=n_loops, d_loop=0.3
        )
        ax.plot(np.degrees(theta), 20 * np.log10(pattern + 1e-12),
                style, linewidth=1.2, label=label)
    ax.set_xlabel('θ [deg]')
    ax.set_ylabel('Normalized Pattern [dB]')
    ax.set_ylim(-30, 3)
    ax.set_xlim(0, 180)
    ax.set_title('Spiral Pattern (dB)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig11_3_spiral_pattern.png', dpi=150)
    plt.close()
    print(f"  Saved fig11_3_spiral_pattern.png")


# =========================================================================
# 11.4 LPDA — Full Design (Carrel Procedure)
# =========================================================================

def lpda_sigma_optimal(tau: float) -> float:
    """Optimal relative spacing σ_opt for a given τ.

    σ_opt = 0.243 · τ − 0.051

    Parameters
    ----------
    tau : float
        Scaling factor (0.8 ≤ τ ≤ 0.98)

    Returns
    -------
    sigma_opt : float
        Optimal relative spacing
    """
    return 0.243 * tau - 0.051


def lpda_design(
    tau: float,
    sigma: float,
    f_min: float,
    f_max: float,
    l_over_d: float = 125.0,
    z_in_target: float = 50.0
) -> Dict:
    """Complete LPDA design using Carrel's procedure.

    Steps:
      1. Apex half-angle: α = arctan[(1-τ) / (4σ)]
      2. Active-region bandwidth: B_ar
      3. Structure bandwidth: B_s = B · B_ar
      4. Number of elements N
      5. Element lengths: l₁ = λ_max / 2
      6. Element positions: R_n
      7. Feed-line characteristic impedance

    Parameters
    ----------
    tau : float
        Scaling factor (0.8–0.98)
    sigma : float
        Relative spacing (0.03–σ_opt)
    f_min : float
        Lowest operating frequency [Hz]
    f_max : float
        Highest operating frequency [Hz]
    l_over_d : float
        Length-to-diameter ratio for elements (≈125 typical)
    z_in_target : float
        Target input impedance [Ω]

    Returns
    -------
    design : dict
        Complete design parameters with arrays for each element
    """
    B: float = f_max / f_min                            # operating bandwidth
    cot_alpha: float = 4.0 * sigma / (1.0 - tau)        # cot(α)
    alpha_rad: float = np.arctan(1.0 / cot_alpha)       # apex half-angle [rad]

    # Active-region bandwidth (Carrel)
    B_ar: float = 1.1 + 7.7 * (1.0 - tau)**2.0 * cot_alpha

    # Structure bandwidth
    B_s: float = B * B_ar

    # Number of elements
    N_raw: float = 1.0 + np.log(B_s) / np.log(1.0 / tau)
    N: int = int(round(N_raw))

    # Element design (longest → shortest)
    lambda_max: float = C0 / f_min
    lambda_min: float = C0 / f_max

    ell: np.ndarray = np.zeros(N)       # element lengths [m]
    R: np.ndarray = np.zeros(N)         # distance from apex [m]
    d_element: np.ndarray = np.ones(N) * lambda_max / l_over_d  # element diameters

    # Longest element (index 0)
    ell[0] = lambda_max / 2.0
    R[0] = ell[0] / 2.0 * cot_alpha

    # Scaling
    for n in range(1, N):
        ell[n] = ell[n-1] * tau
        R[n] = R[n-1] * tau
        d_element[n] = ell[n] / l_over_d

    # Element spacing (edge-to-edge)
    spacing: np.ndarray = np.zeros(N - 1)
    for n in range(N - 1):
        spacing[n] = 2.0 * sigma * ell[n]

    # Boom length
    L_boom: float = np.sum(spacing)

    # Average characteristic impedance of elements (Carrel)
    Z_a_avg: float = np.mean([
        120.0 * (np.log(ell[n] / d_element[n]) - 2.25)
        for n in range(N)
    ])

    # Feed-line impedance
    sigma_prime: float = sigma / np.sqrt(tau)
    term: float = z_in_target / (8.0 * sigma_prime * Z_a_avg)
    Z_feed: float = z_in_target * term + z_in_target * np.sqrt(term**2.0 + 1.0)

    # Terminating stub length (λ₁/8)
    stub_length: float = lambda_max / 8.0

    # Gain estimation from Carrel curves (interpolation)
    # Linearized fit: G [dBi] ≈ 5.5 + 18 * (τ - 0.80) for near-optimal σ
    gain_est_dBi: float = 5.5 + 18.0 * (tau - 0.80)
    gain_est_dBi = min(max(gain_est_dBi, 3.0), 12.0)

    # Active region location (approximate)
    # The active region is where element length ≈ λ/2
    n_active_start: int = max(0, N // 4)
    n_active_end: int = min(N, N * 3 // 4)

    return {
        'tau': tau,
        'sigma': sigma,
        'sigma_opt': lpda_sigma_optimal(tau),
        'alpha_rad': alpha_rad,
        'alpha_deg': np.degrees(alpha_rad),
        'cot_alpha': cot_alpha,
        'B': B,
        'B_ar': B_ar,
        'B_s': B_s,
        'N': N,
        'N_raw': N_raw,
        'ell': ell,                    # [m]
        'R': R,                        # [m]
        'd_element': d_element,        # [m]
        'spacing': spacing,            # [m]
        'L_boom': L_boom,              # [m]
        'Z_a_avg': Z_a_avg,            # [Ω]
        'Z_feed': Z_feed,              # [Ω]
        'Z_in_target': z_in_target,    # [Ω]
        'stub_length': stub_length,    # [m]
        'gain_est_dBi': gain_est_dBi,  # [dBi]
        'f_min': f_min,
        'f_max': f_max,
        'n_active_start': n_active_start,
        'n_active_end': n_active_end,
    }


def lpda_directivity_contours() -> Dict:
    """Generate LPDA directivity data over (τ, σ) grid.

    Uses Carrel's empirical relationship.

    Returns
    -------
    data : dict
        tau_grid, sigma_grid, D_grid for contour plotting
    """
    tau_vals: np.ndarray = np.linspace(0.80, 0.98, 37)
    sigma_vals: np.ndarray = np.linspace(0.03, 0.20, 35)
    tau_grid, sigma_grid = np.meshgrid(tau_vals, sigma_vals)

    # Directivity (dBi) approximated from Carrel curves
    # Fit: D = 3.5 + 25*(τ - 0.78)² + 15*σ  (for τ > 0.82)
    D_grid: np.ndarray = np.zeros_like(tau_grid)
    for i in range(len(sigma_vals)):
        for j in range(len(tau_vals)):
            t: float = tau_vals[j]
            s: float = sigma_vals[i]
            s_opt: float = lpda_sigma_optimal(t)
            # Penalize deviation from optimal sigma
            dev: float = (s - s_opt) ** 2 / 0.002
            D_grid[i, j] = 4.5 + 22.0 * (t - 0.78) + 12.0 * s - 80.0 * dev
            D_grid[i, j] = max(D_grid[i, j], 3.0)

    return {
        'tau': tau_vals,
        'sigma': sigma_vals,
        'D_dBi': D_grid,
    }


def plot_lpda_geometry() -> None:
    """Fig 11.4: LPDA geometry visualization with element positions."""
    design: Dict = lpda_design(
        tau=0.90, sigma=0.05,
        f_min=0.5e9, f_max=5.0e9,
        l_over_d=125.0, z_in_target=50.0
    )

    N: int = design['N']
    ell: np.ndarray = design['ell']
    R: np.ndarray = design['R']
    spacing: np.ndarray = design['spacing']

    # Cumulative x-position
    x_pos: np.ndarray = np.zeros(N)
    for n in range(1, N):
        x_pos[n] = x_pos[n-1] + spacing[n-1]

    fig, ax = plt.subplots(figsize=(10, 4))

    # Draw each dipole (horizontal lines — criss-cross feed not shown)
    for n in range(N):
        y_center: float = 0.0
        half_l: float = ell[n] / 2.0
        # Alternate color to indicate phase reversal
        color: str = 'blue' if n % 2 == 0 else 'red'
        ax.plot([x_pos[n], x_pos[n]], [-half_l, half_l],
                '-', color=color, linewidth=1.5, alpha=0.8)
        # Feed point dot
        ax.plot(x_pos[n], y_center, 'ko', markersize=2)

    # Transmission line (feed line)
    ax.plot([x_pos[0], x_pos[-1]], [0, 0], 'k-', linewidth=0.8, alpha=0.4)

    ax.set_xlabel('Boom position [m]')
    ax.set_ylabel('Element length [m]')
    ax.set_title(
        f'LPDA Geometry: τ={design["tau"]}, σ={design["sigma"]}, '
        f'N={N}, α={design["alpha_deg"]:.1f}°'
    )
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig11_4_lpda_geometry.png', dpi=150)
    plt.close()
    print(f"  Saved fig11_4_lpda_geometry.png")

    # Print design summary
    print(f"\n  LPDA Design Summary:")
    print(f"    τ = {design['tau']}, σ = {design['sigma']}")
    print(f"    σ_opt = {design['sigma_opt']:.4f}")
    print(f"    α = {design['alpha_deg']:.2f}°")
    print(f"    B = {design['B']:.1f}, B_ar = {design['B_ar']:.2f}, B_s = {design['B_s']:.1f}")
    print(f"    N = {design['N']}, L_boom = {design['L_boom']:.3f} m")
    print(f"    Gain ≈ {design['gain_est_dBi']:.1f} dBi")
    print(f"    Z_feed ≈ {design['Z_feed']:.1f} Ω")
    print(f"    l₁ = {ell[0]*100:.1f} cm, l_N = {ell[-1]*100:.1f} cm")


def plot_lpda_directivity_contours() -> None:
    """Fig 11.5: LPDA directivity contours (τ vs σ) from Carrel."""
    data: Dict = lpda_directivity_contours()
    tau_vals: np.ndarray = data['tau']
    sigma_vals: np.ndarray = data['sigma']
    D_dBi: np.ndarray = data['D_dBi']

    fig, ax = plt.subplots(figsize=(8, 6))

    levels: np.ndarray = np.arange(3.0, 12.5, 0.5)
    contour = ax.contourf(tau_vals, sigma_vals, D_dBi,
                          levels=levels, cmap='viridis', extend='both')
    cbar = plt.colorbar(contour, ax=ax, label='Directivity [dBi]')

    # Overlay σ_opt curve
    tau_dense: np.ndarray = np.linspace(0.80, 0.98, 100)
    sigma_opt_dense: np.ndarray = lpda_sigma_optimal(tau_dense)
    ax.plot(tau_dense, sigma_opt_dense, 'r--', linewidth=2, label=r'$\sigma_{\mathrm{opt}}$')
    ax.legend(fontsize=10)

    ax.set_xlabel('Scaling factor τ')
    ax.set_ylabel('Relative spacing σ')
    ax.set_title('LPDA Directivity Contours (Carrel)')
    ax.set_xlim(0.80, 0.98)
    ax.set_ylim(0.03, 0.20)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig11_5_lpda_directivity_contours.png', dpi=150)
    plt.close()
    print(f"  Saved fig11_5_lpda_directivity_contours.png")


# =========================================================================
# LPDA Radiation Pattern (Active Region Model)
# =========================================================================

def lpda_radiation_pattern(
    theta: np.ndarray,
    design: Dict,
    f_operation: float
) -> np.ndarray:
    """Compute LPDA far-field radiation pattern at a given frequency.

    Model: only elements near resonance (active region) contribute.
    Active region elements have length ≈ λ/2.

    Parameters
    ----------
    theta : ndarray
        Observation angles [rad], 0 = toward apex (end-fire)
    design : Dict
        LPDA design from lpda_design()
    f_operation : float
        Operating frequency [Hz]

    Returns
    -------
    E_theta : ndarray
        Normalized pattern magnitude |E_θ|
    """
    lambda_op: float = C0 / f_operation
    k: float = 2.0 * PI / lambda_op
    ell_half: float = lambda_op / 2.0  # resonant length

    N: int = design['N']
    ell: np.ndarray = design['ell']
    R: np.ndarray = design['R']

    # Gaussian amplitude weighting centered on resonance
    sigma_weight: float = 0.15  # width of active region in log(length)
    weights: np.ndarray = np.exp(
        -((np.log(ell) - np.log(ell_half)) / sigma_weight) ** 2
    )

    # Phase: dipole element factor + array factor + criss-cross reversal
    pattern: np.ndarray = np.zeros_like(theta, dtype=complex)

    for n in range(N):
        w: float = weights[n]
        if w < 0.01:
            continue

        # Element factor: dipole pattern
        kl: float = k * ell[n]
        element_factor: np.ndarray = np.zeros_like(theta)
        mask: np.ndarray = np.abs(np.sin(theta)) > 1e-10
        element_factor[mask] = np.abs(
            (np.cos(kl / 2.0 * np.cos(theta[mask])) - np.cos(kl / 2.0))
            / np.sin(theta[mask])
        )

        # Array factor phase + 180° criss-cross reversal
        phase: float = k * R[n] * np.cos(theta) + n * PI  # n*PI = reversal

        pattern += w * element_factor * np.exp(1j * phase)

    return np.abs(pattern) / np.max(np.abs(pattern))


def plot_lpda_radiation_pattern() -> None:
    """Fig 11.6: LPDA radiation pattern at multiple frequencies."""
    design: Dict = lpda_design(
        tau=0.90, sigma=0.05,
        f_min=0.5e9, f_max=5.0e9
    )

    # Frequencies for pattern evaluation
    freqs: np.ndarray = np.array([0.5, 1.0, 2.0, 4.0]) * 1e9

    theta: np.ndarray = np.linspace(0.01, PI - 0.01, 361)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Panel (a): Cartesian
    ax = axes[0]
    for f_op, style in zip(freqs, ['-', '--', '-.', ':']):
        pattern: np.ndarray = lpda_radiation_pattern(theta, design, f_op)
        pattern_dB: np.ndarray = 20 * np.log10(pattern + 1e-12)
        ax.plot(np.degrees(theta), pattern_dB,
                style, linewidth=1.2,
                label=f'{f_op/1e9:.1f} GHz')
    ax.set_xlabel('θ [deg]')
    ax.set_ylabel('Normalized Pattern [dB]')
    ax.set_ylim(-30, 3)
    ax.set_xlim(0, 180)
    ax.set_title('LPDA Radiation Pattern')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (b): Polar (end-fire)
    ax = plt.subplot(122, projection='polar')
    for f_op, style in zip(freqs, ['-', '--', '-.', ':']):
        pattern = lpda_radiation_pattern(theta, design, f_op)
        ax.plot(theta, pattern, style, linewidth=1.2,
                label=f'{f_op/1e9:.1f} GHz')
    ax.set_theta_zero_location('E')
    ax.set_thetamin(0)
    ax.set_thetamax(180)
    ax.set_title('LPDA Polar Pattern (end-fire)', va='bottom')
    ax.legend(loc='lower right', fontsize=8)

    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig11_6_lpda_pattern.png', dpi=150)
    plt.close()
    print(f"  Saved fig11_6_lpda_pattern.png")


# =========================================================================
# LPDA Design Parametric Sweep
# =========================================================================

def plot_lpda_param_sweep() -> None:
    """Fig 11.7: Parametric study of LPDA performance vs τ and σ."""
    tau_vals: np.ndarray = np.array([0.82, 0.88, 0.92, 0.96])
    sigma_vals: np.ndarray = np.linspace(0.03, 0.10, 30)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Panel (a): N vs σ for various τ
    ax = axes[0]
    for tau_v in tau_vals:
        N_list: list = []
        for sigma_v in sigma_vals:
            d: Dict = lpda_design(
                tau=tau_v, sigma=sigma_v,
                f_min=0.5e9, f_max=5.0e9
            )
            N_list.append(d['N'])
        ax.plot(sigma_vals, N_list, linewidth=1.5,
                label=rf'τ = {tau_v:.2f}')
    ax.set_xlabel('σ')
    ax.set_ylabel('Number of Elements N')
    ax.set_title('N vs σ')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (b): L_boom vs σ for various τ
    ax = axes[1]
    for tau_v in tau_vals:
        L_list: list = []
        for sigma_v in sigma_vals:
            d = lpda_design(
                tau=tau_v, sigma=sigma_v,
                f_min=0.5e9, f_max=5.0e9
            )
            L_list.append(d['L_boom'])
        ax.plot(sigma_vals, L_list, linewidth=1.5,
                label=rf'τ = {tau_v:.2f}')
    ax.set_xlabel('σ')
    ax.set_ylabel('Boom Length [m]')
    ax.set_title('L_boom vs σ')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig11_7_lpda_param_sweep.png', dpi=150)
    plt.close()
    print(f"  Saved fig11_7_lpda_param_sweep.png")


# =========================================================================
# 11.7 Fractal Antennas — Koch Dipole
# =========================================================================

def koch_snowflake_segment(
    p1: np.ndarray,
    p2: np.ndarray,
    iteration: int
) -> np.ndarray:
    """Recursively generate Koch curve from point p1 to p2.

    Parameters
    ----------
    p1, p2 : ndarray (2,)
        Start and end points
    iteration : int
        Recursion depth

    Returns
    -------
    points : ndarray (N, 2)
        Vertices of the Koch curve
    """
    if iteration == 0:
        return np.array([p1, p2])

    v: np.ndarray = p2 - p1
    length: float = np.linalg.norm(v) / 3.0
    unit: np.ndarray = v / np.linalg.norm(v)

    # Three equal segments
    a: np.ndarray = p1
    b: np.ndarray = p1 + unit * length
    d: np.ndarray = p1 + unit * 2.0 * length

    # Tip of the triangle (rotate by 60°)
    angle: float = PI / 3.0
    rot: np.ndarray = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])
    c: np.ndarray = b + rot @ (unit * length)

    # Recursively generate each sub-segment
    seg1: np.ndarray = koch_snowflake_segment(a, b, iteration - 1)
    seg2: np.ndarray = koch_snowflake_segment(b, c, iteration - 1)
    seg3: np.ndarray = koch_snowflake_segment(c, d, iteration - 1)
    seg4: np.ndarray = koch_snowflake_segment(d, p2, iteration - 1)

    # Merge (remove duplicate endpoints)
    return np.vstack([seg1[:-1], seg2[:-1], seg3[:-1], seg4])


def koch_dipole(iteration: int = 3, base_length: float = 1.0) -> np.ndarray:
    """Generate a Koch fractal dipole antenna.

    The dipole is aligned along the x-axis, centered at origin.
    Total physical length grows as (4/3)^iteration.

    Parameters
    ----------
    iteration : int
        Fractal iteration depth (0 = straight dipole)
    base_length : float
        Physical base length (end-to-end) [m]

    Returns
    -------
    points : ndarray (N, 2)
        (x, y) vertices of the Koch dipole
    """
    p_left: np.ndarray = np.array([-base_length / 2.0, 0.0])
    p_right: np.ndarray = np.array([base_length / 2.0, 0.0])
    return koch_snowflake_segment(p_left, p_right, iteration)


def plot_koch_dipole() -> None:
    """Fig 11.8: Koch fractal dipole at different iterations."""
    fig, axes = plt.subplots(4, 1, figsize=(8, 8))

    for it in range(4):
        ax = axes[it]
        points: np.ndarray = koch_dipole(iteration=it, base_length=1.0)

        # Total physical length
        total_length: float = (4.0 / 3.0) ** it

        ax.plot(points[:, 0], points[:, 1], 'b-', linewidth=1.2)
        ax.set_aspect('equal')
        ax.set_title(f'Koch Dipole — Iteration {it}'
                      f'  (L/L₀ = {total_length:.2f})')
        ax.set_xlabel('x [m]')
        ax.set_ylabel('y [m]')
        ax.set_xlim(-0.7, 0.7)
        ax.set_ylim(-0.4, 0.4)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig11_8_koch_dipole.png', dpi=150)
    plt.close()
    print(f"  Saved fig11_8_koch_dipole.png")


# =========================================================================
# Spiral vs LPDA Parameter Summary Table
# =========================================================================

def print_frequency_independent_comparison() -> None:
    """Print comparison table of frequency independent antenna types."""
    print("\n" + "=" * 60)
    print("Comparison of Frequency-Independent Antenna Types")
    print("=" * 60)
    print(f"{'Type':<22} {'BW Ratio':<10} {'Gain [dBi]':<12} {'Polarization':<14}")
    print("-" * 60)
    print(f"{'Equiangular Spiral':<22} {'>10:1':<10} {'3–6':<12} {'Circular':<14}")
    print(f"{'Archimedean Spiral':<22} {'4–10:1':<10} {'3–5':<12} {'Circular':<14}")
    print(f"{'LPDA':<22} {'2–30:1':<10} {'6–11':<12} {'Linear':<14}")
    print(f"{'Conical Spiral':<22} {'>10:1':<10} {'4–7':<12} {'Circular':<14}")
    print("=" * 60)


# =========================================================================
# Main
# =========================================================================

def main() -> None:
    """Run all Ch11 examples."""
    print("=" * 55)
    print("Balanis Ch11 — Frequency Independent Antennas Examples")
    print("=" * 55)

    # 1. Equiangular spiral geometry
    print("\n[1/7] Equiangular spiral geometry...", flush=True)
    f_low: float = equiangular_spiral_lowest_frequency(r_outer=0.1)
    print(f"  Spiral (r_outer=0.1 m): f_low ≈ {f_low/1e6:.1f} MHz")
    print(f"  Self-complementary Z_in = {equiangular_spiral_self_impedance():.1f} Ω")
    plot_equiangular_spiral()

    # 2. Spiral comparison
    print("\n[2/7] Spiral comparison...", flush=True)
    plot_spiral_comparison()

    # 3. Spiral radiation pattern
    print("\n[3/7] Spiral radiation pattern...", flush=True)
    plot_spiral_radiation_pattern()

    # 4. LPDA design
    print("\n[4/7] LPDA design (Carrel procedure)...", flush=True)
    plot_lpda_geometry()

    # 5. LPDA directivity contours
    print("\n[5/7] LPDA directivity contours...", flush=True)
    plot_lpda_directivity_contours()

    # 6. LPDA radiation pattern
    print("\n[6/7] LPDA radiation pattern...", flush=True)
    plot_lpda_radiation_pattern()

    # 7. LPDA parametric sweep
    print("\n[7/7] LPDA parametric sweep...", flush=True)
    plot_lpda_param_sweep()

    # 8. Koch fractal dipole
    print("\n[8/8] Koch fractal dipole...", flush=True)
    plot_koch_dipole()

    # Summary
    print_frequency_independent_comparison()

    print("\n✅ All Ch11 examples complete.")


if __name__ == '__main__':
    main()
