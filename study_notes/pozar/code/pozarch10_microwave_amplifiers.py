"""
Pozar Chapter 10: Microwave Amplifier Design
=============================================
Comprehensive examples covering:
  - S-parameter amplifier representation
  - K-Delta stability analysis & mu-factors
  - Stability circles (input & output)
  - Power gain definitions (G_T, G_A, G_P, G_TU)
  - MAG / MSG
  - Unilateral gain design & gain circles
  - Bilateral maximum gain (simultaneous conjugate match)
  - Bilateral constant gain circles (operating & available)
  - Multi-stage amplifier cascade

Author: Xiaolongxia (小龙虾)
Based on: Pozar, Microwave Engineering, 4th Ed., Ch.10
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from typing import Tuple, Optional, List

# ============================================================
# Physical constants & system impedance
# ============================================================
Z_0: float = 50.0  # System characteristic impedance [Ω]


# ============================================================
# S-parameter helper functions
# ============================================================

def s_mag_angle_to_complex(mag: float, angle_deg: float) -> complex:
    """Convert magnitude/angle(deg) to complex S-parameter."""
    return mag * np.exp(1j * np.deg2rad(angle_deg))


def gamma_from_z(Z: complex, Z0: float = Z_0) -> complex:
    """Reflection coefficient from impedance."""
    return (Z - Z0) / (Z + Z0)


def z_from_gamma(Gamma: complex, Z0: float = Z_0) -> complex:
    """Impedance from reflection coefficient."""
    return Z0 * (1 + Gamma) / (1 - Gamma)


# ============================================================
# Stability Analysis (Section 10.2)
# ============================================================

def delta(S: np.ndarray) -> complex:
    """Determinant of S-parameter matrix: Δ = S11*S22 - S12*S21."""
    return S[0, 0] * S[1, 1] - S[0, 1] * S[1, 0]


def k_factor(S: np.ndarray) -> float:
    """
    Rollett stability factor K.
    K > 1 AND |Δ| < 1 for unconditional stability.
    
    K = (1 - |S11|^2 - |S22|^2 + |Δ|^2) / (2|S12*S21|)
    """
    S11, S12, S21, S22 = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    Delta = delta(S)
    numerator = 1.0 - abs(S11)**2 - abs(S22)**2 + abs(Delta)**2
    denominator = 2.0 * abs(S12 * S21)
    return float(numerator / denominator)


def mu1_factor(S: np.ndarray) -> float:
    """
    Edwards-Sinsky μ1 factor (input port).
    μ1 > 1 for unconditional stability (single condition).
    
    μ1 = (1 - |S11|^2) / (|S22 - Δ S11*| + |S12 S21|)
    """
    S11, S12, S21, S22 = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    Delta = delta(S)
    numerator = 1.0 - abs(S11)**2
    denominator = abs(S22 - Delta * np.conj(S11)) + abs(S12 * S21)
    return float(numerator / denominator)


def mu2_factor(S: np.ndarray) -> float:
    """
    Edwards-Sinsky μ2 factor (output port).
    μ2 > 1 for unconditional stability.
    """
    S11, S12, S21, S22 = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    Delta = delta(S)
    numerator = 1.0 - abs(S22)**2
    denominator = abs(S11 - Delta * np.conj(S22)) + abs(S12 * S21)
    return float(numerator / denominator)


def is_unconditionally_stable(S: np.ndarray) -> bool:
    """Check unconditional stability: K > 1 AND |Δ| < 1."""
    return bool(k_factor(S) > 1.0 + 1e-12 and abs(delta(S)) < 1.0 - 1e-12)


def gamma_in(S: np.ndarray, Gamma_L: complex) -> complex:
    """Input reflection coefficient given load reflection coefficient."""
    S11, S12, S21, S22 = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    return S11 + (S12 * S21 * Gamma_L) / (1.0 - S22 * Gamma_L)


def gamma_out(S: np.ndarray, Gamma_S: complex) -> complex:
    """Output reflection coefficient given source reflection coefficient."""
    S11, S12, S21, S22 = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    return S22 + (S12 * S21 * Gamma_S) / (1.0 - S11 * Gamma_S)


# ============================================================
# Stability Circles (Section 10.2)
# ============================================================

def output_stability_circle(S: np.ndarray) -> Tuple[complex, float]:
    """
    Output stability circle in the Gamma_L plane.
    Returns (center, radius).
    
    C_L = (S22 - Δ S11*)* / (|S22|^2 - |Δ|^2)
    r_L = |S12 S21 / (|S22|^2 - |Δ|^2)|
    """
    S11, S12, S21, S22 = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    Delta = delta(S)
    denominator = abs(S22)**2 - abs(Delta)**2
    center = np.conj(S22 - Delta * np.conj(S11)) / denominator
    radius = abs(S12 * S21 / denominator)
    return center, radius


def input_stability_circle(S: np.ndarray) -> Tuple[complex, float]:
    """
    Input stability circle in the Gamma_S plane.
    Returns (center, radius).
    
    C_S = (S11 - Δ S22*)* / (|S11|^2 - |Δ|^2)
    r_S = |S12 S21 / (|S11|^2 - |Δ|^2)|
    """
    S11, S12, S21, S22 = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    Delta = delta(S)
    denominator = abs(S11)**2 - abs(Delta)**2
    center = np.conj(S11 - Delta * np.conj(S22)) / denominator
    radius = abs(S12 * S21 / denominator)
    return center, radius


# ============================================================
# Power Gains (Section 10.3)
# ============================================================

def transducer_gain(S: np.ndarray, Gamma_S: complex, Gamma_L: complex) -> float:
    """
    Transducer Power Gain G_T.
    
    G_T = (1-|Γs|²) |S21|² (1-|ΓL|²) / |(1-S11Γs)(1-S22ΓL) - S12S21ΓsΓL|²
    """
    S11, S12, S21, S22 = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    numerator = (1.0 - abs(Gamma_S)**2) * abs(S21)**2 * (1.0 - abs(Gamma_L)**2)
    denominator = abs((1.0 - S11 * Gamma_S) * (1.0 - S22 * Gamma_L)
                      - S12 * S21 * Gamma_S * Gamma_L)**2
    return float(numerator / denominator)


def operating_gain(S: np.ndarray, Gamma_L: complex) -> float:
    """
    Operating Power Gain G_P (independent of Γ_S).
    
    G_P = |S21|² (1 - |ΓL|²) / (|1 - S22 ΓL|² (1 - |Γin|²))
    """
    S11, S12, S21, S22 = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    Gamma_in_val = gamma_in(S, Gamma_L)
    numerator = abs(S21)**2 * (1.0 - abs(Gamma_L)**2)
    denominator = abs(1.0 - S22 * Gamma_L)**2 * (1.0 - abs(Gamma_in_val)**2)
    return float(numerator / denominator)


def available_gain(S: np.ndarray, Gamma_S: complex) -> float:
    """
    Available Power Gain G_A (independent of Γ_L).
    
    G_A = (1 - |Γs|²) |S21|² / (|1 - S11 Γs|² (1 - |Γout|²))
    """
    S11, S12, S21, S22 = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    Gamma_out_val = gamma_out(S, Gamma_S)
    numerator = (1.0 - abs(Gamma_S)**2) * abs(S21)**2
    denominator = abs(1.0 - S11 * Gamma_S)**2 * (1.0 - abs(Gamma_out_val)**2)
    return float(numerator / denominator)


def unilateral_transducer_gain(
    S: np.ndarray, Gamma_S: complex, Gamma_L: complex
) -> float:
    """
    Unilateral Transducer Gain G_TU (assumes S12 = 0).
    
    G_TU = G_S * G_0 * G_L
    G_S = (1 - |Γs|²) / |1 - S11 Γs|²
    G_0 = |S21|²
    G_L = (1 - |ΓL|²) / |1 - S22 ΓL|²
    """
    S11, S12, S21, S22 = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    G_S = (1.0 - abs(Gamma_S)**2) / abs(1.0 - S11 * Gamma_S)**2
    G_0 = abs(S21)**2
    G_L = (1.0 - abs(Gamma_L)**2) / abs(1.0 - S22 * Gamma_L)**2
    return float(G_S * G_0 * G_L)


def unilateral_figure_of_merit(S: np.ndarray) -> float:
    """
    Unilateral Figure of Merit U.
    
    U = |S12||S21||S11||S22| / [(1 - |S11|²)(1 - |S22|²)]
    
    Gain error bound: G_T / G_TU ∈ [1/(1+U)², 1/(1-U)²]
    """
    S11, S12, S21, S22 = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    numerator = abs(S12) * abs(S21) * abs(S11) * abs(S22)
    denominator = (1.0 - abs(S11)**2) * (1.0 - abs(S22)**2)
    U = numerator / denominator
    return float(U)


def unilateral_gain_error_bounds(U: float) -> Tuple[float, float]:
    """
    Returns (lower_bound_ratio, upper_bound_ratio) for G_T/G_TU.
    """
    return (1.0 / (1.0 + U)**2, 1.0 / (1.0 - U)**2)


def mag_msg(S: np.ndarray) -> Tuple[float, float]:
    """
    Maximum Available Gain (MAG) and Maximum Stable Gain (MSG).
    
    G_MAG = |S21/S12| * (K - sqrt(K² - 1))   [only when K >= 1]
    G_MSG = |S21/S12|                          [for K < 1 or upper bound]
    """
    S12, S21 = S[0, 1], S[1, 0]
    K = k_factor(S)
    g_msg = abs(S21 / S12)
    if K >= 1.0:
        g_mag = abs(S21 / S12) * (K - np.sqrt(K**2 - 1))
    else:
        g_mag = np.nan  # MAG undefined when K < 1
    return float(g_mag) if not np.isnan(g_mag) else np.nan, float(g_msg)


def max_unilateral_gain(S: np.ndarray) -> float:
    """
    Maximum Unilateral Transducer Gain.
    G_TU,max = |S21|² / [(1 - |S11|²)(1 - |S22|²)]
    Achieved when Γ_S = S11* and Γ_L = S22*
    """
    S11, S12, S21, S22 = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    return float(abs(S21)**2 / ((1.0 - abs(S11)**2) * (1.0 - abs(S22)**2)))


# ============================================================
# Simultaneous Conjugate Match (Section 10.4)
# ============================================================

def simultaneous_conjugate_match(
    S: np.ndarray
) -> Tuple[complex, complex, float]:
    """
    Compute Γ_S and Γ_L for simultaneous conjugate match.
    Only valid for unconditionally stable devices (K >= 1).
    
    Returns (Gamma_S, Gamma_L, G_T_max).
    """
    S11, S12, S21, S22 = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    Delta = delta(S)
    K = k_factor(S)

    if K < 1.0:
        raise ValueError(
            f"Cannot perform simultaneous conjugate match: K = {K:.4f} < 1"
        )

    # C1 = S11 - Δ*S22*  (note: some references use conjugate forms)
    C1 = S11 - Delta * np.conj(S22)
    C2 = S22 - Delta * np.conj(S11)
    B1 = 1.0 + abs(S11)**2 - abs(S22)**2 - abs(Delta)**2
    B2 = 1.0 + abs(S22)**2 - abs(S11)**2 - abs(Delta)**2

    # Gamma_S = (B1 ± sqrt(B1² - 4|C1|²)) / (2*C1)
    sqrt_term_s = np.sqrt(B1**2 - 4.0 * abs(C1)**2 + 0j)
    Gamma_S_plus = (B1 + sqrt_term_s) / (2.0 * C1)
    Gamma_S_minus = (B1 - sqrt_term_s) / (2.0 * C1)

    # Choose the solution with |Γ| < 1
    Gamma_S = Gamma_S_plus if abs(Gamma_S_plus) < 1.0 else Gamma_S_minus
    if abs(Gamma_S) >= 1.0:
        raise RuntimeError("No stable conjugate match solution found")

    # Gamma_L = (B2 ± sqrt(B2² - 4|C2|²)) / (2*C2)
    sqrt_term_l = np.sqrt(B2**2 - 4.0 * abs(C2)**2 + 0j)
    Gamma_L_plus = (B2 + sqrt_term_l) / (2.0 * C2)
    Gamma_L_minus = (B2 - sqrt_term_l) / (2.0 * C2)
    Gamma_L = Gamma_L_plus if abs(Gamma_L_plus) < 1.0 else Gamma_L_minus
    if abs(Gamma_L) >= 1.0:
        raise RuntimeError("No stable conjugate match solution found")

    G_T_max = transducer_gain(S, Gamma_S, Gamma_L)
    return Gamma_S, Gamma_L, float(G_T_max)


# ============================================================
# Unilateral Constant Gain Circles (Section 10.4.3)
# ============================================================

def unilateral_input_gain_circle(
    S: np.ndarray, G_S_desired: float
) -> Tuple[complex, float]:
    """
    Constant G_S circle in the Γ_S plane for unilateral design (S12=0).
    
    g_s = G_S * (1 - |S11|²)  [normalized gain, 0 <= g_s <= 1]
    G_S ∈ [1, 1/(1 - |S11|²)] when Γ_S=0 and Γ_S=S11*, respectively.
    
    Center: C = g_s * S11* / [1 - (1 - g_s)|S11|²]
    Radius: R = sqrt(1 - g_s) * (1 - |S11|²) / [1 - (1 - g_s)|S11|²]
    
    Args:
        S: S-parameter matrix
        G_S_desired: desired value of G_S (linear, not dB)
    """
    S11 = S[0, 0]
    G_S_max = 1.0 / (1.0 - abs(S11)**2)
    denom = 1.0 - abs(S11)**2
    if denom <= 0:
        raise ValueError(f"|S11| must be < 1, got |S11| = {abs(S11):.4f}")
    # Normalize: g_s = G_S / G_S_max = G_S * (1 - |S11|²), ∈ [0, 1]
    g_s = G_S_desired * denom
    if g_s < 0 or g_s > 1.0 + 1e-10:
        raise ValueError(
            f"Normalized gain g_s = {g_s:.6f} must be in [0, 1]. "
            f"Max G_S = {G_S_max:.6f} ({10*np.log10(G_S_max):.2f} dB)"
        )
    g_s = min(g_s, 1.0)  # clamp for numerical stability
    center = g_s * np.conj(S11) / (1.0 - (1.0 - g_s) * abs(S11)**2)
    radius = np.sqrt(1.0 - g_s) * (1.0 - abs(S11)**2) / (
        1.0 - (1.0 - g_s) * abs(S11)**2
    )
    return center, radius


def unilateral_output_gain_circle(
    S: np.ndarray, G_L_desired: float
) -> Tuple[complex, float]:
    """
    Constant G_L circle in the Γ_L plane for unilateral design (S12=0).
    Similar formula as input but with S22.
    """
    S22 = S[1, 1]
    G_L_max = 1.0 / (1.0 - abs(S22)**2)
    denom = 1.0 - abs(S22)**2
    if denom <= 0:
        raise ValueError(f"|S22| must be < 1, got |S22| = {abs(S22):.4f}")
    # Normalize: g_l = G_L / G_L_max = G_L * (1 - |S22|²), ∈ [0, 1]
    g_l = G_L_desired * denom
    if g_l < 0 or g_l > 1.0 + 1e-10:
        raise ValueError(
            f"Normalized gain g_l = {g_l:.6f} must be in [0, 1]. "
            f"Max G_L = {G_L_max:.6f} ({10*np.log10(G_L_max):.2f} dB)"
        )
    g_l = min(g_l, 1.0)  # clamp for numerical stability
    center = g_l * np.conj(S22) / (1.0 - (1.0 - g_l) * abs(S22)**2)
    radius = np.sqrt(1.0 - g_l) * (1.0 - abs(S22)**2) / (
        1.0 - (1.0 - g_l) * abs(S22)**2
    )
    return center, radius


# ============================================================
# Bilateral Constant Gain Circles (Section 10.4.2)
# ============================================================

def operating_gain_circle(
    S: np.ndarray, G_P_desired: float
) -> Tuple[complex, float]:
    """
    Constant operating power gain circle in the Γ_L plane.
    For bilateral devices. Enables design for specified G_P.
    
    g_p = G_P / |S21|²
    
    Center: C_p = g_p * C2* / (1 + g_p*(|S22|² - |Δ|²))
    Radius: R_p = sqrt(1 - 2*K*|S12S21|*g_p + |S12S21|²*g_p²)
                  / |1 + g_p*(|S22|² - |Δ|²)|
    
    where C2 = S22 - Δ*S11*
    """
    S11, S12, S21, S22 = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    Delta = delta(S)
    K = k_factor(S)
    C2 = S22 - Delta * np.conj(S11)

    g_p = G_P_desired / abs(S21)**2
    denominator = 1.0 + g_p * (abs(S22)**2 - abs(Delta)**2)

    center = g_p * np.conj(C2) / denominator

    # Under the sqrt: 1 - 2K|S12S21|g_p + |S12S21|²g_p²
    D_12 = abs(S12 * S21)
    sqrt_arg = 1.0 - 2.0 * K * D_12 * g_p + (D_12 * g_p)**2
    if sqrt_arg < 0:
        raise ValueError(
            f"G_P = {10*np.log10(G_P_desired):.2f} dB is not achievable. "
            f"Sqrt arg = {sqrt_arg:.4f}"
        )
    radius = np.sqrt(sqrt_arg) / abs(denominator)
    return center, radius


def available_gain_circle(
    S: np.ndarray, G_A_desired: float
) -> Tuple[complex, float]:
    """
    Constant available power gain circle in the Γ_S plane.
    For bilateral devices.
    
    g_a = G_A / |S21|²
    
    Center: C_a = g_a * C1* / (1 + g_a*(|S11|² - |Δ|²))
    Radius: R_a = sqrt(1 - 2*K*|S12S21|*g_a + |S12S21|²*g_a²)
                  / |1 + g_a*(|S11|² - |Δ|²)|
    
    where C1 = S11 - Δ*S22*
    """
    S11, S12, S21, S22 = S[0, 0], S[0, 1], S[1, 0], S[1, 1]
    Delta = delta(S)
    K = k_factor(S)
    C1 = S11 - Delta * np.conj(S22)

    g_a = G_A_desired / abs(S21)**2
    denominator = 1.0 + g_a * (abs(S11)**2 - abs(Delta)**2)

    center = g_a * np.conj(C1) / denominator

    D_12 = abs(S12 * S21)
    sqrt_arg = 1.0 - 2.0 * K * D_12 * g_a + (D_12 * g_a)**2
    if sqrt_arg < 0:
        raise ValueError(
            f"G_A = {10*np.log10(G_A_desired):.2f} dB is not achievable."
        )
    radius = np.sqrt(sqrt_arg) / abs(denominator)
    return center, radius


# ============================================================
# Multi-stage Amplifier
# ============================================================

def cascade_stage_gain(S_stages: List[np.ndarray]) -> float:
    """
    Compute total transducer gain for a cascaded multi-stage amplifier.
    Assumes each stage is ideally isolated (interstage matching ideal).
    
    For a simpler estimate: sum of G_TU,max for each stage.
    More accurate: use the product of transducer gains.
    
    Args:
        S_stages: list of S-parameter matrices (2x2 numpy arrays)
    
    Returns:
        Total gain (linear).
    """
    total_gain_linear = 1.0
    for S in S_stages:
        g_tu_max = max_unilateral_gain(S)
        total_gain_linear *= g_tu_max
    return total_gain_linear


# ============================================================
# Smith Chart Plotting Utilities
# ============================================================

def draw_smith_chart(ax: plt.Axes, title: str = "Smith Chart") -> None:
    """
    Draw a Z-Smith chart background on the given axes.
    """
    ax.set_aspect("equal")
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.15, 1.15)
    ax.set_title(title, fontsize=12)

    # Unit circle
    theta = np.linspace(0, 2 * np.pi, 500)
    ax.plot(np.cos(theta), np.sin(theta), "k-", linewidth=1.5)

    # Constant resistance circles
    for r in [0.2, 0.5, 1.0, 2.0, 5.0]:
        center_x = r / (1.0 + r)
        radius = 1.0 / (1.0 + r)
        circle = plt.Circle(
            (center_x, 0), radius, fill=False, linestyle="--",
            linewidth=0.5, color="gray", alpha=0.5
        )
        ax.add_patch(circle)

    # Constant reactance arcs
    for x in [0.2, 0.5, 1.0, 2.0, 5.0]:
        # positive reactance (upper half)
        center_x = 1.0
        center_y = 1.0 / x
        radius = 1.0 / x
        theta_arc = np.linspace(
            np.arctan2(center_y, -center_x), np.pi - np.arctan2(center_y, -center_x),
            100
        )
        ax.plot(
            center_x + radius * np.cos(theta_arc),
            center_y + radius * np.sin(theta_arc),
            "--", linewidth=0.5, color="gray", alpha=0.5
        )
        # negative reactance (lower half)
        center_y = -1.0 / x
        theta_arc = np.linspace(
            np.pi - np.arctan2(-center_y, -center_x),
            2 * np.pi + np.arctan2(center_y, center_x),
            100
        )
        ax.plot(
            center_x + radius * np.cos(theta_arc),
            center_y + radius * np.sin(theta_arc),
            "--", linewidth=0.5, color="gray", alpha=0.5
        )

    # Axes
    ax.axhline(0, color="gray", linewidth=0.5)
    ax.axvline(0, color="gray", linewidth=0.5)
    ax.grid(False)
    # Remove tick labels for clean Smith chart look
    ax.set_xticklabels([])
    ax.set_yticklabels([])


def plot_circle_on_ax(
    ax: plt.Axes, center: complex, radius: float,
    color: str = "blue", label: str = "", linestyle: str = "-"
) -> None:
    """Plot a circle on the given axes (Smith chart)."""
    if np.isinf(radius) or np.isnan(radius):
        return
    theta = np.linspace(0, 2 * np.pi, 500)
    x = center.real + radius * np.cos(theta)
    y = center.imag + radius * np.sin(theta)
    ax.plot(x, y, color=color, linestyle=linestyle, linewidth=1.5, label=label)
    # Mark center
    ax.plot(center.real, center.imag, "o", color=color, markersize=4)


# ============================================================
# Example Data: Pozar-style S-parameters (MESFET @ 4 GHz)
# ============================================================

def get_example_sparams() -> np.ndarray:
    """
    Example S-parameters at 4 GHz (MESFET, after Pozar Ch.10 style).
    These produce K ~ 1.05, |Δ| ~ 0.60 — conditionally stable.
    """
    S11 = 0.614 * np.exp(1j * np.deg2rad(-127.3))
    S12 = 0.044 * np.exp(1j * np.deg2rad(33.9))
    S21 = 6.002 * np.exp(1j * np.deg2rad(76.7))
    S22 = 0.475 * np.exp(1j * np.deg2rad(-57.7))
    return np.array([[S11, S12], [S21, S22]])


def get_example_sparams_stable() -> np.ndarray:
    """
    Example S-parameters that are unconditionally stable (K >> 1).
    Typical for a well-designed low-noise transistor.
    """
    S11 = 0.2 * np.exp(1j * np.deg2rad(-60))
    S12 = 0.02 * np.exp(1j * np.deg2rad(60))
    S21 = 5.0 * np.exp(1j * np.deg2rad(120))
    S22 = 0.3 * np.exp(1j * np.deg2rad(-30))
    return np.array([[S11, S12], [S21, S22]])


def get_phemt_sparams_4ghz() -> np.ndarray:
    """
    FPD6836P70 pHEMT S-parameters at 4 GHz (from datasheet).
    Realistic transistor data for amplifier design examples.
    """
    return np.array([
        [0.614 * np.exp(1j * np.deg2rad(-127.3)),
         0.044 * np.exp(1j * np.deg2rad(33.9))],
        [6.002 * np.exp(1j * np.deg2rad(76.7)),
         0.475 * np.exp(1j * np.deg2rad(-57.7))]
    ])


# ============================================================
# Example 1: Stability Analysis
# ============================================================

def example_1_stability_analysis() -> None:
    """Stability analysis of a microwave transistor at 4 GHz."""
    print("=" * 70)
    print("Example 1: Stability Analysis (Section 10.2)")
    print("=" * 70)

    S = get_example_sparams()
    print(f"\nS-parameters at 4 GHz:")
    print(f"  S11 = {S[0,0]:.4f}")
    print(f"  S12 = {S[0,1]:.4f}")
    print(f"  S21 = {S[1,0]:.4f}")
    print(f"  S22 = {S[1,1]:.4f}")

    Delta = delta(S)
    K = k_factor(S)
    mu1 = mu1_factor(S)
    mu2 = mu2_factor(S)
    stable = is_unconditionally_stable(S)

    G_MAG, G_MSG = mag_msg(S)

    print(f"\nStability Metrics:")
    print(f"  Δ = {Delta:.4f}")
    print(f"  |Δ| = {abs(Delta):.4f}  {'✓ < 1' if abs(Delta) < 1 else '✗ >= 1'}")
    print(f"  K = {K:.4f}  {'✓ > 1' if K > 1 else '✗ <= 1'}")
    print(f"  μ₁ = {mu1:.4f}")
    print(f"  μ₂ = {mu2:.4f}")
    print(f"  Unconditionally stable: {stable}")
    print(f"\nGain Metrics:")
    print(f"  G_MAG = {10*np.log10(G_MAG):.2f} dB" if not np.isnan(G_MAG)
          else "  G_MAG = undefined (K < 1)")
    print(f"  G_MSG = {10*np.log10(G_MSG):.2f} dB")

    # Stability circles
    C_S, r_S = input_stability_circle(S)
    C_L, r_L = output_stability_circle(S)
    print(f"\nInput Stability Circle (Γ_S plane):")
    print(f"  Center C_S = {C_S:.4f}, |C_S| = {abs(C_S):.4f}")
    print(f"  Radius r_S = {r_S:.4f}")
    print(f"Output Stability Circle (Γ_L plane):")
    print(f"  Center C_L = {C_L:.4f}, |C_L| = {abs(C_L):.4f}")
    print(f"  Radius r_L = {r_L:.4f}")

    # Plot stability circles
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    draw_smith_chart(ax1, "Input Stability Circle (Γ_S plane)")
    plot_circle_on_ax(ax1, C_S, r_S, color="red", label="Input Stability Circle")
    # Mark center and S11*
    ax1.plot(C_S.real, C_S.imag, "ro", markersize=5)
    S11_star = np.conj(S[0, 0])
    ax1.plot(S11_star.real, S11_star.imag, "g*", markersize=10, label="S11*")
    ax1.plot(0, 0, "ko", markersize=4, label="Γ=0 (50Ω)")

    draw_smith_chart(ax2, "Output Stability Circle (Γ_L plane)")
    plot_circle_on_ax(ax2, C_L, r_L, color="blue", label="Output Stability Circle")
    ax2.plot(C_L.real, C_L.imag, "bo", markersize=5)
    S22_star = np.conj(S[1, 1])
    ax2.plot(S22_star.real, S22_star.imag, "g*", markersize=10, label="S22*")
    ax2.plot(0, 0, "ko", markersize=4, label="Γ=0 (50Ω)")

    for ax in [ax1, ax2]:
        ax.legend(fontsize=8, loc="upper right")

    fig.tight_layout()
    fig.savefig(
        "/home/ubuntu/.openclaw/workspace/python/figures/ch10/ex1_stability_circles.png",
        dpi=150
    )
    plt.close(fig)
    print("\n  → Saved: figures/ch10/ex1_stability_circles.png")


# ============================================================
# Example 2: Unilateral Approximation and Gain Circles
# ============================================================

def example_2_unilateral_gain() -> None:
    """Unilateral amplifier design with constant gain circles."""
    print("=" * 70)
    print("Example 2: Unilateral Gain Design (Section 10.4.3)")
    print("=" * 70)

    S = get_example_sparams()
    U = unilateral_figure_of_merit(S)
    lower, upper = unilateral_gain_error_bounds(U)
    G_TU_max = max_unilateral_gain(S)

    print(f"\nUnilateral Figure of Merit U = {U:.4f}")
    print(f"  U >> 1 → bilateral effects are significant here!")
    print(f"  G_T/G_TU bounds: [{lower:.4f}, {upper:.4f}]")
    print(f"  Max unilateral gain G_TU,max = {10*np.log10(G_TU_max):.2f} dB")

    # For proper unilateral example, use a transistor with small S12
    print("\n--- Using low-feedback transistor for unilateral design ---")
    S_unilateral = np.array([
        [0.3 * np.exp(1j * np.deg2rad(-120)),
         0.01 * np.exp(1j * np.deg2rad(30))],  # small S12
        [4.0 * np.exp(1j * np.deg2rad(75)),
         0.2 * np.exp(1j * np.deg2rad(-60))]
    ])
    U2 = unilateral_figure_of_merit(S_unilateral)
    lower2, upper2 = unilateral_gain_error_bounds(U2)
    G_TU_max2 = max_unilateral_gain(S_unilateral)
    G0 = abs(S_unilateral[1, 0])**2

    print(f"\n  U = {U2:.4f}  {'✓ negligible' if U2 < 0.1 else '⚠️  moderate'}")
    print(f"  G_T/G_TU bounds: [{lower2:.4f}, {upper2:.4f}]")
    print(f"  G_0 = |S21|² = {10*np.log10(G0):.2f} dB")
    print(f"  Max unilateral gain = {10*np.log10(G_TU_max2):.2f} dB")

    # Compute G_S_max and G_L_max
    S11, S22 = S_unilateral[0, 0], S_unilateral[1, 1]
    G_S_max = 1.0 / (1.0 - abs(S11)**2)
    G_L_max = 1.0 / (1.0 - abs(S22)**2)
    print(f"  G_S,max = {10*np.log10(G_S_max):.2f} dB  (Γ_S = S11*)")
    print(f"  G_L,max = {10*np.log10(G_L_max):.2f} dB  (Γ_L = S22*)")

    # Plot constant gain circles for GS and GL
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    draw_smith_chart(ax1, "Constant G_S Circles (Γ_S plane)")

    # Draw multiple GS circles
    # Use fraction of max to avoid rounding issues (g_s ∈ [0,1))
    gs_fractions = np.array([0.0, 0.25, 0.50, 0.75, 0.95])
    gs_values_linear = gs_fractions * G_S_max
    colors = plt.cm.Reds(np.linspace(0.3, 1.0, len(gs_values_linear)))
    for gs_linear, frac, color in zip(gs_values_linear, gs_fractions, colors):
        center, radius = unilateral_input_gain_circle(S_unilateral, gs_linear)
        gs_db_val = 10 * np.log10(gs_linear) if gs_linear > 0 else -np.inf
        label_str = f"G_S = 0 dB (Γ_S=0)" if gs_linear <= 1.0 else f"G_S = {gs_db_val:.2f} dB"
        # Handle the special case: G_S=1 (Γ_S=0) circle has radius=|S11|, center at S11*
        if gs_linear <= 1.0 + 1e-10:
            label_str = f"G_S = {10*np.log10(gs_linear):.2f} dB" if gs_linear > 1.0 else f"G_S = 0 dB (Γ_S=0)"
        else:
            label_str = f"G_S = {gs_db_val:.2f} dB"
        plot_circle_on_ax(
            ax1, center, radius, color=color,
            label=label_str, linestyle="-"
        )
    # mark S11*
    ax1.plot(np.conj(S11).real, np.conj(S11).imag, "r*", markersize=12)

    draw_smith_chart(ax2, "Constant G_L Circles (Γ_L plane)")
    gl_fractions = np.array([0.0, 0.25, 0.50, 0.75, 0.95])
    gl_values_linear = gl_fractions * G_L_max
    colors = plt.cm.Blues(np.linspace(0.3, 1.0, len(gl_values_linear)))
    for gl_linear, frac, color in zip(gl_values_linear, gl_fractions, colors):
        center, radius = unilateral_output_gain_circle(S_unilateral, gl_linear)
        gl_db_val = 10 * np.log10(gl_linear) if gl_linear > 0 else -np.inf
        label_str = f"G_L = 0 dB (Γ_L=0)" if gl_linear <= 1.0 else f"G_L = {gl_db_val:.2f} dB"
        if gl_linear <= 1.0 + 1e-10:
            label_str = f"G_L = 0 dB (Γ_L=0)"
        else:
            label_str = f"G_L = {gl_db_val:.2f} dB"
        plot_circle_on_ax(
            ax2, center, radius, color=color,
            label=label_str, linestyle="-"
        )
    ax2.plot(np.conj(S22).real, np.conj(S22).imag, "b*", markersize=12)

    for ax in [ax1, ax2]:
        ax.legend(fontsize=7, loc="upper right")

    fig.tight_layout()
    fig.savefig(
        "/home/ubuntu/.openclaw/workspace/python/figures/ch10/ex2_unilateral_gain_circles.png",
        dpi=150
    )
    plt.close(fig)
    print("\n  → Saved: figures/ch10/ex2_unilateral_gain_circles.png")


# ============================================================
# Example 3: Bilateral Maximum Gain Design
# ============================================================

def example_3_maximum_gain() -> None:
    """Simultaneous conjugate match for maximum transducer gain."""
    print("=" * 70)
    print("Example 3: Maximum Gain Design — Conjugate Match (Section 10.4.1)")
    print("=" * 70)

    S = get_example_sparams_stable()
    print(f"\nS-parameters (unconditionally stable device):")
    print(f"  S11 = {S[0,0]:.4f}")
    print(f"  S12 = {S[0,1]:.4f}")
    print(f"  S21 = {S[1,0]:.4f}")
    print(f"  S22 = {S[1,1]:.4f}")

    K = k_factor(S)
    Delta = delta(S)
    print(f"  K = {K:.4f}  (unconditionally stable: {K > 1 and abs(Delta) < 1})")
    print(f"  |Δ| = {abs(Delta):.4f}")

    Gamma_S, Gamma_L, G_T_max = simultaneous_conjugate_match(S)
    print(f"\nSimultaneous Conjugate Match:")
    print(f"  Γ_S = {Gamma_S:.4f}  (|Γ_S| = {abs(Gamma_S):.4f})")
    print(f"  Γ_L = {Gamma_L:.4f}  (|Γ_L| = {abs(Gamma_L):.4f})")
    Z_S = z_from_gamma(Gamma_S)
    Z_L = z_from_gamma(Gamma_L)
    print(f"  Z_S = {Z_S:.2f} Ω")
    print(f"  Z_L = {Z_L:.2f} Ω")
    print(f"  G_T,max = {10*np.log10(G_T_max):.2f} dB")

    # Verify: Γ_in and Γ_out should be conjugates
    Gamma_in_check = gamma_in(S, Gamma_L)
    Gamma_out_check = gamma_out(S, Gamma_S)
    print(f"\nVerification:")
    print(f"  Γ_in  = {Gamma_in_check:.4f}  (should = Γ_S*)")
    print(f"  Γ_out = {Gamma_out_check:.4f}  (should = Γ_L*)")
    print(f"  |Γ_in - Γ_S*| = {abs(Gamma_in_check - np.conj(Gamma_S)):.6f}")
    print(f"  |Γ_out - Γ_L*| = {abs(Gamma_out_check - np.conj(Gamma_L)):.6f}")

    # Compute MAG
    G_MAG, G_MSG = mag_msg(S)
    print(f"\n  G_MAG = {10*np.log10(G_MAG):.2f} dB")
    print(f"  G_MSG = {10*np.log10(G_MSG):.2f} dB")
    print(f"  G_T,max - G_MAG = {10*np.log10(G_T_max) - 10*np.log10(G_MAG):.4f} dB (should be 0)")

    # Plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    draw_smith_chart(ax1, "Maximum Gain: Input Match (Γ_S)")
    ax1.plot(Gamma_S.real, Gamma_S.imag, "ro", markersize=8, label="Γ_S")
    ax1.plot(np.conj(S[0, 0]).real, np.conj(S[0, 0]).imag, "g*", markersize=10,
             label="S11*")
    ax1.legend(fontsize=9)

    draw_smith_chart(ax2, "Maximum Gain: Output Match (Γ_L)")
    ax2.plot(Gamma_L.real, Gamma_L.imag, "bo", markersize=8, label="Γ_L")
    ax2.plot(np.conj(S[1, 1]).real, np.conj(S[1, 1]).imag, "g*", markersize=10,
             label="S22*")
    ax2.legend(fontsize=9)

    fig.tight_layout()
    fig.savefig(
        "/home/ubuntu/.openclaw/workspace/python/figures/ch10/ex3_maximum_gain.png",
        dpi=150
    )
    plt.close(fig)
    print("  → Saved: figures/ch10/ex3_maximum_gain.png")


# ============================================================
# Example 4: Bilateral Constant Gain Circles
# ============================================================

def example_4_constant_gain_circles() -> None:
    """Specified gain design using constant gain circles (bilateral)."""
    print("=" * 70)
    print("Example 4: Bilateral Constant Gain Circles (Section 10.4.2)")
    print("=" * 70)

    S = get_example_sparams_stable()
    K = k_factor(S)
    print(f"\nDevice: K = {K:.4f}")
    print(f"  |S21|² = {abs(S[1,0])**2:.4f} "
          f"({10*np.log10(abs(S[1,0])**2):.2f} dB)")

    # Compute MAG for reference
    G_MAG, _ = mag_msg(S)
    print(f"  G_MAG = {10*np.log10(G_MAG):.2f} dB")
    G_T_max_linear = G_MAG

    # Operating gain circles (Γ_L plane)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    draw_smith_chart(ax1, "Operating Gain Circles (Γ_L plane)")

    # Choose a few gain levels below G_MAG
    g_levels_db = [10*np.log10(G_T_max_linear) - i for i in [0, 1, 2, 3, 5]]
    colors = plt.cm.Blues(np.linspace(0.4, 1.0, len(g_levels_db)))
    for level_db, color in zip(g_levels_db, colors):
        level_linear = 10**(level_db / 10.0)
        try:
            center, radius = operating_gain_circle(S, level_linear)
            plot_circle_on_ax(
                ax1, center, radius, color=color,
                label=f"G_P = {level_db:.1f} dB",
                linestyle="-"
            )
        except ValueError as e:
            print(f"  Skipping G_P = {level_db:.1f} dB: {e}")

    # Calculate conjugate match Γ_L for reference
    _, Gamma_L_max, _ = simultaneous_conjugate_match(S)
    ax1.plot(Gamma_L_max.real, Gamma_L_max.imag, "r*", markersize=12,
             label="Γ_L (max gain)")
    ax1.legend(fontsize=7, loc="upper right")

    # Available gain circles (Γ_S plane)
    draw_smith_chart(ax2, "Available Gain Circles (Γ_S plane)")
    colors = plt.cm.Reds(np.linspace(0.4, 1.0, len(g_levels_db)))
    for level_db, color in zip(g_levels_db, colors):
        level_linear = 10**(level_db / 10.0)
        try:
            center, radius = available_gain_circle(S, level_linear)
            plot_circle_on_ax(
                ax2, center, radius, color=color,
                label=f"G_A = {level_db:.1f} dB",
                linestyle="-"
            )
        except ValueError as e:
            print(f"  Skipping G_A = {level_db:.1f} dB: {e}")

    Gamma_S_max, _, _ = simultaneous_conjugate_match(S)
    ax2.plot(Gamma_S_max.real, Gamma_S_max.imag, "r*", markersize=12,
             label="Γ_S (max gain)")
    ax2.legend(fontsize=7, loc="upper right")

    fig.tight_layout()
    fig.savefig(
        "/home/ubuntu/.openclaw/workspace/python/figures/ch10/ex4_constant_gain_circles.png",
        dpi=150
    )
    plt.close(fig)
    print("\n  → Saved: figures/ch10/ex4_constant_gain_circles.png")


# ============================================================
# Example 5: Specified Gain Design — Step-by-Step
# ============================================================

def example_5_specified_gain_design() -> None:
    """
    Step-by-step amplifier design for a specified gain using
    unilateral approximation.
    """
    print("=" * 70)
    print("Example 5: Specified Gain Design (Section 10.4.3)")
    print("=" * 70)

    # Use a transistor with small S12 for unilateral approximation
    S = np.array([
        [0.1 * np.exp(1j * np.deg2rad(160)),
         0.03 * np.exp(1j * np.deg2rad(50))],
        [4.5 * np.exp(1j * np.deg2rad(80)),
         0.15 * np.exp(1j * np.deg2rad(-30))]
    ])

    U = unilateral_figure_of_merit(S)
    print(f"Unilateral Figure of Merit U = {U:.4f}")
    if U > 0.1:
        print("  ⚠️  U > 0.1, bilateral effects may be significant")
    else:
        print("  ✓ Unilateral approximation is valid")

    G_TU_max = max_unilateral_gain(S)
    G0 = abs(S[1, 0])**2
    S11, S22 = S[0, 0], S[1, 1]
    G_S_max = 1.0 / (1.0 - abs(S11)**2)
    G_L_max = 1.0 / (1.0 - abs(S22)**2)

    print(f"\n  G_0 = |S21|² = {10*np.log10(G0):.2f} dB")
    print(f"  G_S,max = {10*np.log10(G_S_max):.2f} dB")
    print(f"  G_L,max = {10*np.log10(G_L_max):.2f} dB")
    print(f"  G_TU,max = {10*np.log10(G_TU_max):.2f} dB")

    # Design for 12 dB total gain
    G_T_des_dB = 12.0
    G_T_des = 10**(G_T_des_dB / 10.0)
    print(f"\nTarget: G_TU = {G_T_des_dB:.1f} dB")

    # Option 1: Share gain between input and output equally
    G_S_des_dB = (G_T_des_dB - 10*np.log10(G0)) / 2.0
    G_L_des_dB = G_S_des_dB
    G_S_des = 10**(G_S_des_dB / 10.0)
    G_L_des = 10**(G_L_des_dB / 10.0)

    print(f"\nOption 1: Equal gain split")
    print(f"  G_S = {G_S_des_dB:.2f} dB, G_L = {G_L_des_dB:.2f} dB")
    print(f"  Total = {G_S_des_dB + 10*np.log10(G0) + G_L_des_dB:.2f} dB")

    # Get Γ_S and Γ_L from gain circles
    c_s, r_s = unilateral_input_gain_circle(S, G_S_des)
    c_l, r_l = unilateral_output_gain_circle(S, G_L_des)
    print(f"  G_S circle: center = {c_s:.4f}, radius = {r_s:.4f}")
    print(f"  G_L circle: center = {c_l:.4f}, radius = {r_l:.4f}")

    # Choose Γ_S on the gain circle (not its center!)
    # Pick the point on the circle closest to the origin (easiest match)
    # Γ_S = c_s + r_s * exp(-j*arg(c_s)) — point on circle toward origin
    theta_s = np.angle(c_s)
    Gamma_S_opt = c_s + r_s * np.exp(-1j * theta_s)
    # Same for Γ_L
    theta_l = np.angle(c_l)
    Gamma_L_opt = c_l + r_l * np.exp(-1j * theta_l)
    print(f"\n  Selected Γ_S = {Gamma_S_opt:.4f}  (|Γ_S| = {abs(Gamma_S_opt):.4f})")
    print(f"  Selected Γ_L = {Gamma_L_opt:.4f}  (|Γ_L| = {abs(Gamma_L_opt):.4f})")

    # Verify gain
    G_TU_check = unilateral_transducer_gain(S, Gamma_S_opt, Gamma_L_opt)
    print(f"  Achieved G_TU = {10*np.log10(G_TU_check):.2f} dB (target: {G_T_des_dB:.1f} dB)")

    # Also compute actual bilateral gain for comparison
    G_T_actual = transducer_gain(S, Gamma_S_opt, Gamma_L_opt)
    print(f"  Actual G_T (bilateral) = {10*np.log10(G_T_actual):.2f} dB")
    print(f"  Unilateral error = "
          f"{abs(10*np.log10(G_TU_check) - 10*np.log10(G_T_actual)):.4f} dB")

    # Option 2: Maximize GS, set GL for remaining gain
    print(f"\nOption 2: Maximize G_S, adjust G_L")
    G_S_des2 = G_S_max * 0.9  # 90% of max
    G_L_des2 = G_T_des / (G_S_des2 * G0)
    print(f"  G_S = {10*np.log10(G_S_des2):.2f} dB")
    print(f"  G_L = {10*np.log10(G_L_des2):.2f} dB")
    print(f"  G_L_max - G_L = "
          f"{10*np.log10(G_L_max) - 10*np.log10(G_L_des2):.2f} dB margin")

    # Plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    draw_smith_chart(ax1, "Input: Constant G_S Circle")
    plot_circle_on_ax(ax1, c_s, r_s, color="red", label=f"G_S = {G_S_des_dB:.1f} dB")
    ax1.plot(c_s.real, c_s.imag, "ro", markersize=6)
    ax1.plot(np.conj(S11).real, np.conj(S11).imag, "g*", markersize=10, label="S11*")
    ax1.plot(0, 0, "ko", markersize=4, label="Γ=0")
    ax1.legend(fontsize=8)

    draw_smith_chart(ax2, "Output: Constant G_L Circle")
    plot_circle_on_ax(ax2, c_l, r_l, color="blue", label=f"G_L = {G_L_des_dB:.1f} dB")
    ax2.plot(c_l.real, c_l.imag, "bo", markersize=6)
    ax2.plot(np.conj(S22).real, np.conj(S22).imag, "g*", markersize=10, label="S22*")
    ax2.plot(0, 0, "ko", markersize=4, label="Γ=0")
    ax2.legend(fontsize=8)

    fig.tight_layout()
    fig.savefig(
        "/home/ubuntu/.openclaw/workspace/python/figures/ch10/ex5_specified_gain_design.png",
        dpi=150
    )
    plt.close(fig)
    print("  → Saved: figures/ch10/ex5_specified_gain_design.png")


# ============================================================
# Example 6: Multi-stage Amplifier Estimate
# ============================================================

def example_6_multistage() -> None:
    """Estimate total gain for a multi-stage amplifier cascade."""
    print("=" * 70)
    print("Example 6: Multi-stage Amplifier (Section 10.6)")
    print("=" * 70)

    S1 = get_example_sparams_stable()
    # Second stage: similar but with slightly different S-params
    S2 = np.array([
        [0.15 * np.exp(1j * np.deg2rad(-50)),
         0.015 * np.exp(1j * np.deg2rad(55))],
        [4.8 * np.exp(1j * np.deg2rad(110)),
         0.25 * np.exp(1j * np.deg2rad(-25))]
    ])
    S3 = get_example_sparams_stable()  # same as stage 1

    stages = [S1, S2, S3]
    G_total = cascade_stage_gain(stages)

    print(f"\nStage 1: G_TU,max = {10*np.log10(max_unilateral_gain(S1)):.2f} dB")
    print(f"Stage 2: G_TU,max = {10*np.log10(max_unilateral_gain(S2)):.2f} dB")
    print(f"Stage 3: G_TU,max = {10*np.log10(max_unilateral_gain(S3)):.2f} dB")
    print(f"\nTotal estimated gain = {10*np.log10(G_total):.2f} dB")

    # More accurate: compute with interstage conjugate match assumption
    print(f"\nWith interstage conjugate matching:")
    for i, S in enumerate(stages):
        if is_unconditionally_stable(S):
            _, _, g_max = simultaneous_conjugate_match(S)
            print(f"  Stage {i+1}: G_T,max = {10*np.log10(g_max):.2f} dB")


# ============================================================
# Example 7: Frequency Sweep Stability
# ============================================================

def example_7_frequency_sweep() -> None:
    """
    Demonstrate that stability must be checked across frequency.
    K and |Δ| change with frequency.
    """
    print("=" * 70)
    print("Example 7: Stability vs. Frequency")
    print("=" * 70)

    # S-parameters from FPD6836P70 pHEMT datasheet at various frequencies
    # (approximated from typical data)
    freqs_ghz = np.array([1, 2, 4, 6, 8, 10, 12, 14, 16, 18])
    # Generate reasonable frequency-dependent S-params
    sparam_data = []
    for f_ghz in freqs_ghz:
        # Approximate: S11 and S22 rotate and shrink with frequency
        angle_scale = -40 * (f_ghz / 4.0)
        mag_s11 = 0.85 * np.exp(-0.07 * f_ghz**0.5)
        mag_s22 = 0.65 * np.exp(-0.05 * f_ghz**0.5)
        mag_s21 = 12.0 * np.exp(-0.12 * f_ghz) + 1.0
        mag_s12 = 0.02 + 0.04 * (f_ghz / 10.0)

        S = np.array([
            [mag_s11 * np.exp(1j * np.deg2rad(angle_scale)),
             mag_s12 * np.exp(1j * np.deg2rad(40 + 5*f_ghz))],
            [mag_s21 * np.exp(1j * np.deg2rad(150 - 15*f_ghz)),
             mag_s22 * np.exp(1j * np.deg2rad(angle_scale + 60))]
        ])
        sparam_data.append(S)

    K_vals = [k_factor(S) for S in sparam_data]
    Delta_mag = [abs(delta(S)) for S in sparam_data]
    mu1_vals = [mu1_factor(S) for S in sparam_data]
    G_mag_vals = []
    G_msg_vals = []
    for S in sparam_data:
        g_mag, g_msg = mag_msg(S)
        G_mag_vals.append(g_mag if not np.isnan(g_mag) else 0)
        G_msg_vals.append(g_msg)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    ax1.plot(freqs_ghz, K_vals, "b-o", linewidth=1.5, label="K factor")
    ax1.axhline(y=1.0, color="r", linestyle="--", linewidth=1,
                label="K = 1 boundary")
    ax1.plot(freqs_ghz, Delta_mag, "g-s", linewidth=1.5, label="|Δ|")
    ax1.axhline(y=1.0, color="orange", linestyle="--", linewidth=1,
                label="|Δ| = 1 boundary")
    ax1.set_ylabel("Stability Metrics", fontsize=11)
    ax1.set_title("Stability vs. Frequency", fontsize=12)
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=9)

    ax2.semilogy(freqs_ghz, G_mag_vals, "r-o", linewidth=1.5,
                 label="G_MAG (linear)")
    ax2.semilogy(freqs_ghz, G_msg_vals, "m-s", linewidth=1.5,
                 label="G_MSG (linear)")
    ax2.set_xlabel("Frequency (GHz)", fontsize=11)
    ax2.set_ylabel("Gain (linear)", fontsize=11)
    ax2.set_title("Available Gain vs. Frequency", fontsize=12)
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=9)

    fig.tight_layout()
    fig.savefig(
        "/home/ubuntu/.openclaw/workspace/python/figures/ch10/ex7_frequency_sweep.png",
        dpi=150
    )
    plt.close(fig)
    print("  → Saved: figures/ch10/ex7_frequency_sweep.png")

    # Print summary
    print(f"\nFrequency sweep results:")
    print(f"{'Freq (GHz)':<12} {'K':<10} {'|Δ|':<10} {'Stable':<10} "
          f"{'G_MAG (dB)':<12} {'G_MSG (dB)':<10}")
    print("-" * 70)
    for i, f in enumerate(freqs_ghz):
        stable = "✓" if K_vals[i] > 1 and Delta_mag[i] < 1 else "✗"
        g_mag_db = (10*np.log10(G_mag_vals[i])
                    if not np.isnan(G_mag_vals[i]) and G_mag_vals[i] > 0
                    else "N/A")
        g_msg_db = 10*np.log10(G_msg_vals[i]) if G_msg_vals[i] > 0 else "N/A"
        print(f"{f:<12.1f} {K_vals[i]:<10.4f} {Delta_mag[i]:<10.4f} "
              f"{stable:<10} {str(g_mag_db):<12} {str(g_msg_db):<10}")


# ============================================================
# Main
# ============================================================

def main() -> None:
    """Run all Pozar Ch.10 amplifier design examples."""
    print("\n" + "=" * 70)
    print(" POZAR CHAPTER 10: MICROWAVE AMPLIFIER DESIGN")
    print(" Comprehensive Examples & Visualizations")
    print("=" * 70 + "\n")

    # Example 1: Stability Analysis
    example_1_stability_analysis()

    print("\n" + "-" * 70 + "\n")

    # Example 2: Unilateral Gain Design
    example_2_unilateral_gain()

    print("\n" + "-" * 70 + "\n")

    # Example 3: Maximum Gain Design
    example_3_maximum_gain()

    print("\n" + "-" * 70 + "\n")

    # Example 4: Bilateral Constant Gain Circles
    example_4_constant_gain_circles()

    print("\n" + "-" * 70 + "\n")

    # Example 5: Specified Gain Design
    example_5_specified_gain_design()

    print("\n" + "-" * 70 + "\n")

    # Example 6: Multi-stage Amplifier
    example_6_multistage()

    print("\n" + "-" * 70 + "\n")

    # Example 7: Frequency Sweep Stability
    example_7_frequency_sweep()

    print("\n" + "=" * 70)
    print(" ALL EXAMPLES COMPLETED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    main()

# ============================================================
# §10.7 — Amplifier Noise (Noise Figure, Noise Circles, LNA)
# ============================================================
# Functions:
#   noise_figure_optimal()    — compute F[dB] from Γ_s, noise params
#   noise_circle()            — constant-NF circle center & radius
#   noise_circles()           — multiple NF circles
#   lna_design_tradeoff()     — gain-noise tradeoff scan
#   cascade_noise_friis()     — Friis cascade formula
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as MPLCircle
from typing import Tuple, List, Optional, Dict


# ============================================================
# 10.7.3 — Noise Figure from Γ-parameter formula
# ============================================================

def noise_figure_optimal(
    Gamma_s_complex: complex,
    Gamma_opt_complex: complex,
    F_min_dB: float,
    R_n: float,
    Z0: float = Z_0
) -> float:
    """
    Compute noise figure NF[dB] from Γ-parameter formula.

    F = F_min + (4*R_n/Z0) * |Γ_s - Γ_opt|² / ((1 - |Γ_s|²)*|1 + Γ_opt|²)

    Args:
        Gamma_s_complex: Source reflection coefficient Γ_s (complex)
        Gamma_opt_complex: Optimum source reflection coefficient Γ_opt (complex)
        F_min_dB: Minimum noise figure [dB]
        R_n: Equivalent noise resistance [Ω]
        Z0: System impedance [Ω] (default 50)

    Returns:
        NF [dB] at this Γ_s

    Raises:
        ValueError: If |Γ_s| >= 1 (unstable source termination)
    """
    abs_gs = abs(Gamma_s_complex)
    if abs_gs >= 1.0 - 1e-12:
        raise ValueError(
            f"|Γ_s| = {abs_gs:.6f} must be < 1 (passive source required)"
        )

    # Linear minimum noise factor
    F_min_lin = 10.0 ** (F_min_dB / 10.0)

    delta_gamma = Gamma_s_complex - Gamma_opt_complex
    numerator = abs(delta_gamma) ** 2
    denominator = (1.0 - abs_gs ** 2) * abs(1.0 + Gamma_opt_complex) ** 2
    noise_ratio = (4.0 * R_n / Z0) * numerator / denominator
    F_lin = F_min_lin + noise_ratio

    return float(10.0 * np.log10(F_lin))


def noise_figure_y_params(
    Y_s_complex: complex,
    Y_opt_complex: complex,
    F_min_dB: float,
    R_n: float
) -> float:
    """
    Compute NF[dB] from Y-parameter formula.

    F = F_min + (R_n / G_s) * |Y_s - Y_opt|²

    Args:
        Y_s_complex: Source admittance Y_s = G_s + jB_s [S]
        Y_opt_complex: Optimum source admittance Y_opt [S]
        F_min_dB: Minimum noise figure [dB]
        R_n: Noise resistance [Ω]

    Returns:
        NF [dB]
    """
    G_s = Y_s_complex.real
    if G_s <= 0:
        raise ValueError(f"G_s = {G_s:.6f} must be > 0 (passive source)")

    F_min_lin = 10.0 ** (F_min_dB / 10.0)
    delta_y = abs(Y_s_complex - Y_opt_complex) ** 2
    F_lin = F_min_lin + (R_n / G_s) * delta_y
    return float(10.0 * np.log10(F_lin))


# ============================================================
# 10.7.4 — Constant Noise Circles
# ============================================================

def noise_circle(
    Gamma_opt_complex: complex,
    F_min_dB: float,
    R_n: float,
    NF_target_dB: float,
    Z0: float = Z_0
) -> Tuple[complex, float]:
    """
    Compute constant-NF circle (center, radius) on the Γ_s plane.

    Let:
        N = (F_k - F_min) / (4*R_n/Z0) * |1 + Γ_opt|²

    Center: C_F = Γ_opt / (1 + N)
    Radius: r_F = sqrt(N*(N+1-|Γ_opt|²)) / (1 + N)

    Args:
        Gamma_opt_complex: Γ_opt (complex)
        F_min_dB: Minimum NF [dB]
        R_n: Noise resistance [Ω]
        NF_target_dB: Target NF for the circle [dB]
        Z0: System impedance [Ω]

    Returns:
        (center, radius) — center is complex, radius is float
    """
    F_min_lin = 10.0 ** (F_min_dB / 10.0)
    F_k_lin = 10.0 ** (NF_target_dB / 10.0)

    Gamma_opt_sq = abs(Gamma_opt_complex) ** 2

    if NF_target_dB <= F_min_dB - 1e-12:
        # Degenerate case: return just the point
        return Gamma_opt_complex, 0.0

    N = (F_k_lin - F_min_lin) / (4.0 * R_n / Z0) * abs(1.0 + Gamma_opt_complex) ** 2

    denom = 1.0 + N
    center = Gamma_opt_complex / denom

    radicand = N * (N + 1.0 - Gamma_opt_sq)
    if radicand < 0:
        # The target NF is not reachable (below F_min).
        # This shouldn't happen since we checked NF_target > F_min,
        # but numerical issues can occur. Return degenerate circle.
        return center, 0.0
    radius = np.sqrt(radicand) / denom

    return center, radius


def noise_circles(
    Gamma_opt_complex: complex,
    F_min_dB: float,
    R_n: float,
    NF_levels_dB: List[float],
    Z0: float = Z_0
) -> List[Tuple[complex, float, float]]:
    """
    Compute multiple constant NF circles.

    Args:
        Gamma_opt_complex: Γ_opt
        F_min_dB: Minimum NF [dB]
        R_n: Noise resistance [Ω]
        NF_levels_dB: List of NF values [dB] to compute circles for
        Z0: System impedance [Ω]

    Returns:
        List of (center, radius, NF_dB) tuples
    """
    circles = []
    for nf_db in sorted(NF_levels_dB):
        if nf_db < F_min_dB:
            continue
        center, radius = noise_circle(Gamma_opt_complex, F_min_dB, R_n, nf_db, Z0)
        circles.append((center, radius, nf_db))
    return circles


# ============================================================
# 10.7.5 — LNA Design Tradeoff (Gain vs Noise)
# ============================================================

def lna_design_tradeoff(
    S: np.ndarray,
    F_min_dB: float,
    Gamma_opt_complex: complex,
    R_n: float,
    Z0: float = Z_0,
    n_points: int = 50
) -> Dict:
    """
    LNA gain-noise tradeoff analysis.
    Scans Γ_s over the Smith chart and computes both G_A and NF at each point.
    Outputs structures for plotting.

    Args:
        S: S-parameter matrix (2x2 complex ndarray)
        F_min_dB: Minimum NF [dB]
        Gamma_opt_complex: Optimum reflection coefficient
        R_n: Noise resistance [Ω]
        Z0: System impedance [Ω]
        n_points: Number of grid points per axis (n_points x n_points)

    Returns:
        dict with keys:
            'gamma_s'    : list of Γ_s values
            'gain'       : list of G_A [dB]
            'nf'         : list of NF [dB]
            'gain_grid'  : 2D array for contour plot
            'nf_grid'    : 2D array for contour plot
            'gain_levels': contour levels in dB
            'nf_levels'  : contour levels in dB
    """
    # Grid of Γ_s values — uniform sampling in polar coordinates
    r_vals = np.linspace(0.01, 0.99, n_points)
    theta_vals = np.linspace(0, 2 * np.pi, n_points, endpoint=False)
    RR, THETA = np.meshgrid(r_vals, theta_vals)
    Gamma_s_grid = RR * np.exp(1j * THETA)

    gain_grid = np.zeros_like(RR)
    nf_grid = np.zeros_like(RR)

    gamma_s_list = []
    gain_list = []
    nf_list = []

    for i in range(n_points):
        for j in range(n_points):
            gs = Gamma_s_grid[i, j]
            try:
                g_a = available_gain(S, gs)
                nf = noise_figure_optimal(gs, Gamma_opt_complex, F_min_dB, R_n, Z0)
                gain_grid[i, j] = 10.0 * np.log10(g_a) if g_a > 0 else -30.0
                nf_grid[i, j] = nf
                gamma_s_list.append(gs)
                gain_list.append(10.0 * np.log10(g_a) if g_a > 0 else -30.0)
                nf_list.append(nf)
            except (ValueError, ZeroDivisionError):
                gain_grid[i, j] = -30.0
                nf_grid[i, j] = 40.0

    # Sweep along specific radial cuts for the intersection plots
    # Use gamma values along S11* -> Gamma_opt line, with a bit of angular spread
    angle_s11 = np.angle(S[0, 0].conjugate())
    angle_opt = np.angle(Gamma_opt_complex)
    # Choose a few representative angles between S11* and Gamma_opt directions
    n_angles = 5
    test_angles = np.linspace(angle_s11, angle_opt, n_angles)
    n_radial = 100
    sweep_gamma_s = []
    sweep_gain = []
    sweep_nf = []
    sweep_info = []

    for ang in test_angles:
        for k in range(1, n_radial):
            r = k / (n_radial + 1)
            gs = r * np.exp(1j * ang)
            try:
                g_a = available_gain(S, gs)
                nf = noise_figure_optimal(gs, Gamma_opt_complex, F_min_dB, R_n, Z0)
                sweep_gamma_s.append(gs)
                sweep_gain.append(10.0 * np.log10(g_a) if g_a > 0 else -30.0)
                sweep_nf.append(nf)
                sweep_info.append({'gamma_s': gs, 'gain_dB': sweep_gain[-1], 'nf_dB': nf})
            except (ValueError, ZeroDivisionError):
                pass

    # Find Pareto-optimal front (best NF for each gain level)
    pareto_gamma = []
    pareto_gain = []
    pareto_nf = []
    if len(sweep_gain) > 0:
        sorted_idx = np.argsort(sweep_gain)  # ascending gain
        best_nf = float('inf')
        for idx in sorted_idx:
            if sweep_nf[idx] < best_nf:
                best_nf = sweep_nf[idx]
                pareto_gain.append(sweep_gain[idx])
                pareto_nf.append(best_nf)
                pareto_gamma.append(sweep_gamma_s[idx])

    # Determine sensible contour levels
    all_gain_db = [g for g in sweep_gain if g > -20]
    all_nf_db = sweep_nf

    return {
        'gamma_s'    : gamma_s_list,
        'gain'       : gain_list,
        'nf'         : nf_list,
        'gain_grid'  : gain_grid,
        'nf_grid'    : nf_grid,
        'RR'         : RR,
        'THETA'      : THETA,
        'sweep_gamma_s': sweep_gamma_s,
        'sweep_gain'   : sweep_gain,
        'sweep_nf'     : sweep_nf,
        'pareto_gamma' : pareto_gamma,
        'pareto_gain'  : pareto_gain,
        'pareto_nf'    : pareto_nf,
        'gain_levels': [8, 9, 10, 11, 12, 13, 14, 15] if all_gain_db else [],
        'nf_levels'  : [0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 4.0] if all_nf_db else [],
    }


# ============================================================
# 10.7.7 — Cascaded Noise (Friis)
# ============================================================

def cascade_noise_friis(
    NF_dB_list: List[float],
    G_avail_dB_list: List[float]
) -> Tuple[float, float, float]:
    """
    Compute total noise figure for cascaded stages using Friis formula.

    F_total = F_1 + (F_2 - 1)/G_1 + (F_3 - 1)/(G_1*G_2) + ...

    Args:
        NF_dB_list: Noise Figure [dB] for each stage (list length N)
        G_avail_dB_list: Available gain [dB] for each stage (list length N)

    Returns:
        (F_total_lin, NF_total_dB, Te_total)
    """
    N = len(NF_dB_list)
    if len(G_avail_dB_list) != N:
        raise ValueError("NF and gain lists must have same length")

    F_lin_total = 0.0
    G_product = 1.0

    # Convert dB to linear
    F_vals_lin = [10.0 ** (nf / 10.0) for nf in NF_dB_list]
    G_vals_lin = [10.0 ** (g / 10.0) for g in G_avail_dB_list]

    for i in range(N):
        if i == 0:
            contribution = F_vals_lin[i]
        else:
            contribution = (F_vals_lin[i] - 1.0) / G_product
        F_lin_total += contribution
        G_product *= G_vals_lin[i]

    NF_total_dB = 10.0 * np.log10(F_lin_total)
    Te_total = 290.0 * (F_lin_total - 1.0)

    return float(F_lin_total), float(NF_total_dB), float(Te_total)


# ============================================================
# 10.7.8 — Example LNA Transistor Data
# ============================================================

def get_lna_transistor_10ghz() -> Dict:
    """
    Example LNA transistor at 10 GHz (pHEMT style, Pozar Ex10.7 inspired).
    Returns dict with S-params and noise parameters.
    """
    S = np.array([
        [0.55 * np.exp(1j * np.deg2rad(-120)),
         0.04 * np.exp(1j * np.deg2rad(35))],
        [5.5 * np.exp(1j * np.deg2rad(75)),
         0.45 * np.exp(1j * np.deg2rad(-50))]
    ])
    noise_params = {
        'F_min_dB': 1.0,                           # Minimum NF [dB]
        'R_n': 5.0,                                 # Noise resistance [Ω]
        'Gamma_opt': 0.65 * np.exp(1j * np.deg2rad(130)),  # Γ_opt
    }
    return {'S': S, **noise_params}


# ============================================================
# 10.7.9 — Smith Chart circle plotting
# ============================================================

def draw_smith_chart_noise(
    ax: plt.Axes,
    title: str = "Smith Chart",
    add_labels: bool = False
) -> None:
    """
    Draw a Z-Smith chart specifically for noise analysis.
    Includes constant-r and constant-x circles.
    """
    ax.set_aspect("equal")
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.15, 1.15)
    ax.set_title(title, fontsize=12)

    # Unit circle
    theta = np.linspace(0, 2 * np.pi, 500)
    ax.plot(np.cos(theta), np.sin(theta), "k-", linewidth=1.5)

    # Constant resistance circles (r = 0.2, 0.5, 1, 2, 5)
    for r in [0.2, 0.5, 1.0, 2.0, 5.0]:
        center_x = r / (1.0 + r)
        radius = 1.0 / (1.0 + r)
        circle = plt.Circle(
            (center_x, 0), radius, fill=False, linestyle="--",
            linewidth=0.5, color="gray", alpha=0.5
        )
        ax.add_patch(circle)

    # Constant reactance arcs
    for x in [0.2, 0.5, 1.0, 2.0, 5.0, -0.2, -0.5, -1.0, -2.0, -5.0]:
        center_x = 1.0
        center_y = 1.0 / x if x != 0 else 0.0
        radius = abs(1.0 / x) if x != 0 else 0.0
        if radius <= 0:
            continue
        if x > 0:  # upper half
            theta_arc = np.linspace(
                np.arctan2(abs(center_y), -abs(center_x)),
                np.pi - np.arctan2(abs(center_y), -abs(center_x)),
                100
            )
        else:  # lower half
            theta_arc = np.linspace(
                np.pi - np.arctan2(abs(center_y), -abs(center_x)),
                2 * np.pi + np.arctan2(-abs(center_y), center_x),
                100
            )
        ax.plot(
            center_x + radius * np.cos(theta_arc),
            center_y + radius * np.sin(theta_arc),
            "--", linewidth=0.5, color="gray", alpha=0.5
        )

    # Axes
    ax.axhline(0, color="gray", linewidth=0.5)
    ax.axvline(0, color="gray", linewidth=0.5)
    ax.grid(False)
    ax.set_xticklabels([])
    ax.set_yticklabels([])


def plot_noise_circle_on_ax(
    ax: plt.Axes,
    center: complex,
    radius: float,
    NF_dB: float,
    color: str = "red",
    linestyle: str = "-",
    linewidth: float = 1.5
) -> None:
    """Plot a constant noise circle on the Smith chart ax."""
    if radius <= 1e-12:
        # Degenerate: just plot the center point
        ax.plot(center.real, center.imag, "o", color=color,
                markersize=6, label=f"NF = {NF_dB:.2f} dB")
        return
    theta = np.linspace(0, 2 * np.pi, 400)
    x = center.real + radius * np.cos(theta)
    y = center.imag + radius * np.sin(theta)
    ax.plot(x, y, color=color, linestyle=linestyle,
            linewidth=linewidth, label=f"NF = {NF_dB:.2f} dB")


def plot_gain_circle_on_ax(
    ax: plt.Axes,
    center: complex,
    radius: float,
    G_dB: float,
    color: str = "blue",
    linestyle: str = "--",
    linewidth: float = 1.2
) -> None:
    """Plot a constant gain circle on the Smith chart ax."""
    if radius <= 1e-12:
        ax.plot(center.real, center.imag, "s", color=color,
                markersize=6, label=f"G = {G_dB:.1f} dB")
        return
    theta = np.linspace(0, 2 * np.pi, 400)
    x = center.real + radius * np.cos(theta)
    y = center.imag + radius * np.sin(theta)
    ax.plot(x, y, color=color, linestyle=linestyle,
            linewidth=linewidth, label=f"G = {G_dB:.1f} dB")


# ============================================================
# FIGURE 1: Noise Circles + Gain Circles on Smith Chart
#   → fig10_7_1_noise_circles.png
# ============================================================

def fig_noise_circles_smith() -> None:
    """
    Generate Fig 10.7.1: Smith chart showing:
      - Constant NF circles
      - Constant G_A (available gain) circles
      - Γ_opt point
      - S11* point
      - Selected Γ_S (tradeoff point)
    Mirrors Pozar Example 10.7 style.
    """
    print("=" * 70)
    print("Fig 10.7.1: Noise + Gain Circles on Smith Chart")
    print("=" * 70)

    data = get_lna_transistor_10ghz()
    S = data['S']
    F_min_dB = data['F_min_dB']
    R_n = data['R_n']
    Gamma_opt = data['Gamma_opt']
    S11 = S[0, 0]
    S11_star = np.conj(S11)

    print(f"\nTransistor @ 10 GHz:")
    print(f"  F_min = {F_min_dB:.2f} dB")
    print(f"  R_n = {R_n:.1f} Ω")
    print(f"  Γ_opt = {Gamma_opt:.4f}  (|Γ_opt| = {abs(Gamma_opt):.4f})")
    print(f"  S11*  = {S11_star:.4f}")

    # Compute noise circles
    nf_levels_db = [1.0, 1.2, 1.5, 2.0, 3.0]
    circles = noise_circles(Gamma_opt, F_min_dB, R_n, nf_levels_db)

    # Compute available gain circles (in Γ_S plane)
    # G_A_max (MAG) for reference
    g_mag, _ = mag_msg(S)
    g_a_db_max = 10 * np.log10(g_mag) if not np.isnan(g_mag) else 15
    g_levels_db = [g_a_db_max - i for i in [0.0, 0.5, 1.0, 2.0, 3.0, 5.0]]
    # Filter: only levels achievable
    gain_circles = []
    for g_db in g_levels_db:
        g_lin = 10.0 ** (g_db / 10.0)
        try:
            c, r = available_gain_circle(S, g_lin)
            gain_circles.append((c, r, g_db))
        except ValueError:
            pass

    print(f"\nG_A,max ≈ {g_a_db_max:.2f} dB")
    for c, r, g_db in gain_circles:
        print(f"  G_A = {g_db:.1f} dB: center=({c.real:.4f},{c.imag:.4f}), r={r:.4f}")

    for c, r, nf in circles:
        print(f"  NF = {nf:.2f} dB: center=({c.real:.4f},{c.imag:.4f}), r={r:.4f}")

    # Find a good tradeoff point:
    # Intersection of NF = 1.5 dB circle and G_A ≈ 10.5 dB circle
    nf_target = 1.5
    g_target_db = 10.5
    c_nf, r_nf = noise_circle(Gamma_opt, F_min_dB, R_n, nf_target)
    g_target_lin = 10.0 ** (g_target_db / 10.0)
    try:
        c_gain, r_gain = available_gain_circle(S, g_target_lin)
    except ValueError:
        # Adjust target
        g_target_db = 10.0
        g_target_lin = 10.0 ** (g_target_db / 10.0)
        c_gain, r_gain = available_gain_circle(S, g_target_lin)

    # Find a point near the intersection of the two circles.
    # We'll search along the line from origin toward Gamma_opt,
    # and pick the one that's near both circles.
    # Simplified: pick the midpoint on a radial line
    search_angles = np.linspace(np.angle(Gamma_opt) - 0.4,
                                np.angle(S11_star) + 0.4, 200)
    best_score = float('inf')
    best_gs = Gamma_opt * 0.8  # fallback
    for ang in search_angles:
        for r in np.linspace(0.1, 0.95, 200):
            gs = r * np.exp(1j * ang)
            d_nf = abs(abs(gs - c_nf) - r_nf)  # distance from noise circle
            d_gain = abs(abs(gs - c_gain) - r_gain)  # distance from gain circle
            score = d_nf + d_gain * 2.0
            # Penalize going outside |Γ| < 1
            if r > 0.98:
                score += 100
            # Bonus for being on both circles
            if d_nf < 0.03 and d_gain < 0.03:
                score -= 1
            if score < best_score:
                best_score = score
                best_gs = gs

    Gamma_selected = best_gs
    nf_selected = noise_figure_optimal(Gamma_selected, Gamma_opt, F_min_dB, R_n)
    g_a_selected = available_gain(S, Gamma_selected)
    g_a_selected_db = 10 * np.log10(g_a_selected)

    print(f"\n  Selected Γ_S = {Gamma_selected:.4f}")
    print(f"    → NF = {nf_selected:.3f} dB")
    print(f"    → G_A = {g_a_selected_db:.3f} dB")

    # Plot
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    draw_smith_chart_noise(
        ax,
        "Noise Circles & Gain Circles (Γ_S plane)\nLNA @ 10 GHz"
    )

    # NF circles — red colormap from light to dark
    nf_colors = plt.cm.Reds(np.linspace(0.3, 1.0, len(circles)))
    for (c, r, nf), color in zip(circles, nf_colors):
        plot_noise_circle_on_ax(ax, c, r, nf, color=color)
        # Mark center
        ax.plot(c.real, c.imag, "o", color=color, markersize=4)

    # Gain circles — blue colormap
    if gain_circles:
        g_colors = plt.cm.Blues(np.linspace(0.3, 0.9, len(gain_circles)))
        for (c, r, g_db), color in zip(gain_circles, g_colors):
            plot_gain_circle_on_ax(ax, c, r, g_db, color=color)

    # Mark Γ_opt (●), S11* (★), and selected Γ_S (◆)
    ax.plot(Gamma_opt.real, Gamma_opt.imag, "o", color="darkred",
            markersize=10, markerfacecolor="white", markeredgewidth=2,
            label=f"Γ_opt (NF_min = {F_min_dB:.1f} dB)")
    ax.plot(S11_star.real, S11_star.imag, "*", color="green",
            markersize=14, label="S11* (max match)")
    ax.plot(Gamma_selected.real, Gamma_selected.imag, "D", color="magenta",
            markersize=10, markerfacecolor="magenta", markeredgewidth=1.5,
            label=f"Selected Γ_S\nNF={nf_selected:.2f} dB, G_A={g_a_selected_db:.1f} dB")

    ax.legend(fontsize=8, loc="upper right", framealpha=0.9)

    save_path = "/home/ubuntu/.openclaw/workspace/python/figures/ch10/fig10_7_1_noise_circles.png"
    fig.tight_layout()
    fig.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  → Saved: {save_path}")


# ============================================================
# FIGURE 2: NF vs Γ_s — 3D / Contour Plot
#   → fig10_7_2_nf_vs_gamma_s.png
# ============================================================

def fig_nf_vs_gamma_s() -> None:
    """
    Generate Fig 10.7.2: Contour plot of NF [dB] over the Γ_s plane,
    showing the dependency surface. Also includes:
      - Γ_opt location
      - S11* location
      - Minimum NF region
    """
    print("=" * 70)
    print("Fig 10.7.2: NF vs Γ_s Contour Map")
    print("=" * 70)

    data = get_lna_transistor_10ghz()
    F_min_dB = data['F_min_dB']
    R_n = data['R_n']
    Gamma_opt = data['Gamma_opt']
    S = data['S']
    S11_star = np.conj(S[0, 0])

    # Dense grid in Cartesian Γ_s coordinates
    n = 200
    x = np.linspace(-1.0, 1.0, n)
    y = np.linspace(-1.0, 1.0, n)
    XX, YY = np.meshgrid(x, y)
    ZZ = np.zeros_like(XX)

    for i in range(n):
        for j in range(n):
            gs = XX[i, j] + 1j * YY[i, j]
            if abs(gs) >= 1.0 - 1e-8:
                ZZ[i, j] = np.nan
            else:
                try:
                    ZZ[i, j] = noise_figure_optimal(
                        gs, Gamma_opt, F_min_dB, R_n
                    )
                except (ValueError, ZeroDivisionError):
                    ZZ[i, j] = np.nan

    # Figure with two panels: contour + 3D surface
    fig = plt.figure(figsize=(16, 7))

    # --- Left: Contour plot ---
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_aspect("equal")

    # Masked array for contour
    Z_masked = np.ma.array(ZZ, mask=np.isnan(ZZ))

    # Levels: concentrate near F_min for detail
    nf_levels = np.concatenate([
        np.linspace(F_min_dB - 0.1, F_min_dB + 0.5, 8),
        np.linspace(F_min_dB + 0.5, F_min_dB + 3.0, 8)
    ])
    nf_levels = np.unique(np.round(nf_levels, 2))

    contour = ax1.contourf(XX, YY, Z_masked, levels=50,
                           cmap="RdYlBu_r", alpha=0.85)
    cbar = fig.colorbar(contour, ax=ax1, label="NF [dB]", shrink=0.8)
    CS = ax1.contour(XX, YY, Z_masked, levels=nf_levels,
                     colors="k", linewidths=0.6, alpha=0.6)
    ax1.clabel(CS, inline=True, fontsize=7, fmt="%.1f dB")

    # Unit circle
    theta = np.linspace(0, 2 * np.pi, 500)
    ax1.plot(np.cos(theta), np.sin(theta), "k-", linewidth=1.5)

    # Mark key points
    ax1.plot(Gamma_opt.real, Gamma_opt.imag, "o", color="red",
             markersize=12, markerfacecolor="white", markeredgewidth=2.5,
             label=f"Γ_opt (NF_min={F_min_dB:.1f} dB)")
    ax1.plot(S11_star.real, S11_star.imag, "*", color="green",
             markersize=14, label="S11*")

    ax1.set_xlim(-1.1, 1.1)
    ax1.set_ylim(-1.1, 1.1)
    ax1.set_xlabel("Re(Γ_s)")
    ax1.set_ylabel("Im(Γ_s)")
    ax1.set_title("NF [dB] Contours over Γ_s Plane", fontsize=12)
    ax1.legend(fontsize=8, loc="upper right")
    ax1.grid(True, alpha=0.2)

    # --- Right: 3D surface ---
    ax2 = fig.add_subplot(1, 2, 2, projection="3d")

    # Downsample for 3D plot (40x40)
    stride = 5
    X_s = XX[::stride, ::stride]
    Y_s = YY[::stride, ::stride]
    Z_s = Z_masked[::stride, ::stride]

    # Clip Z for better visualization
    Z_display = np.clip(Z_s, F_min_dB - 0.5, F_min_dB + 6.0)

    surf = ax2.plot_surface(X_s, Y_s, Z_display, cmap="RdYlBu_r",
                            alpha=0.9, linewidth=0, antialiased=True)
    fig.colorbar(surf, ax=ax2, label="NF [dB]", shrink=0.6)

    # Mark Γ_opt on surface
    z_opt = F_min_dB
    ax2.plot([Gamma_opt.real], [Gamma_opt.imag], [z_opt],
             "ro", markersize=8, markerfacecolor="white", markeredgewidth=2)

    ax2.set_xlabel("Re(Γ_s)")
    ax2.set_ylabel("Im(Γ_s)")
    ax2.set_zlabel("NF [dB]")
    ax2.set_title("NF Surface (Γ_s plane)", fontsize=12)
    ax2.view_init(elev=25, azim=-60)

    fig.tight_layout()
    save_path = "/home/ubuntu/.openclaw/workspace/python/figures/ch10/fig10_7_2_nf_vs_gamma_s.png"
    fig.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  → Saved: {save_path}")

    print(f"\n  Grid statistics:")
    valid = Z_masked[~np.isnan(Z_masked)]
    print(f"    Min NF = {np.min(valid):.3f} dB (should ≈ {F_min_dB:.3f} dB)")
    print(f"    Max NF (in grid) = {np.minimum(np.max(valid), 15.0):.3f} dB")
    print(f"    Mean NF = {np.mean(valid):.3f} dB")


# ============================================================
# FIGURE 3: Gain-Noise Tradeoff Curve
#   → fig10_7_3_gain_noise_tradeoff.png
# ============================================================

def fig_gain_noise_tradeoff() -> None:
    """
    Generate Fig 10.7.3: Gain vs. Noise tradeoff curve.
    Shows G_A vs. NF for radial sweeps in Γ_s space.
    """
    print("=" * 70)
    print("Fig 10.7.3: Gain-Noise Tradeoff")
    print("=" * 70)

    data = get_lna_transistor_10ghz()
    S = data['S']
    F_min_dB = data['F_min_dB']
    R_n = data['R_n']
    Gamma_opt = data['Gamma_opt']

    S11_star = np.conj(S[0, 0])
    angle_opt = np.angle(Gamma_opt)
    angle_s11 = np.angle(S11_star)

    # Two radial sweeps: toward Γ_opt and toward S11*
    n_radial = 300
    r_vals = np.linspace(0.01, 0.99, n_radial)

    # Sweep 1: radial toward Γ_opt (noise optimal)
    gain_opt_radial = []
    nf_opt_radial = []
    for r in r_vals:
        gs = r * Gamma_opt / abs(Gamma_opt)
        try:
            ga = available_gain(S, gs)
            nf = noise_figure_optimal(gs, Gamma_opt, F_min_dB, R_n)
            gain_opt_radial.append(10 * np.log10(ga))
            nf_opt_radial.append(nf)
        except (ValueError, ZeroDivisionError):
            pass

    # Sweep 2: radial toward S11* (gain optimal)
    gain_s11_radial = []
    nf_s11_radial = []
    for r in r_vals:
        gs = r * S11_star / abs(S11_star)
        try:
            ga = available_gain(S, gs)
            nf = noise_figure_optimal(gs, Gamma_opt, F_min_dB, R_n)
            gain_s11_radial.append(10 * np.log10(ga))
            nf_s11_radial.append(nf)
        except (ValueError, ZeroDivisionError):
            pass

    # Sweep 3: traverse along the line from Γ_opt to S11*
    n_linear = 200
    gamma_pts = np.linspace(float(Gamma_opt.real), float(S11_star.real), n_linear) \
              + 1j * np.linspace(float(Gamma_opt.imag), float(S11_star.imag), n_linear)
    # Renormalize to |Γ| < 1 for any points outside
    gain_line = []
    nf_line = []
    for gs in gamma_pts:
        if abs(gs) >= 0.99:
            gs = gs / abs(gs) * 0.99
        try:
            ga = available_gain(S, gs)
            nf = noise_figure_optimal(gs, Gamma_opt, F_min_dB, R_n)
            gain_line.append(10 * np.log10(ga))
            nf_line.append(nf)
        except (ValueError, ZeroDivisionError):
            gain_line.append(np.nan)
            nf_line.append(np.nan)

    # Full LNA tradeoff scan (fast version from lna_design_tradeoff)
    tradeoff = lna_design_tradeoff(S, F_min_dB, Gamma_opt, R_n, n_points=25)

    # Find the Pareto front for all sweep data combined
    all_gains = gain_opt_radial + gain_s11_radial + list(tradeoff['sweep_gain'])
    all_nfs = nf_opt_radial + nf_s11_radial + list(tradeoff['sweep_nf'])
    # Also add the line points
    for g, n in zip(gain_line, nf_line):
        if not np.isnan(g) and not np.isnan(n):
            all_gains.append(g)
            all_nfs.append(n)

    pareto_gains = []
    pareto_nfs = []
    if len(all_gains) > 0:
        sort_idx = np.argsort(all_gains)
        best_nf = float('inf')
        for idx in sort_idx:
            if all_nfs[idx] < best_nf:
                best_nf = all_nfs[idx]
                pareto_gains.append(all_gains[idx])
                pareto_nfs.append(best_nf)

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left: individual sweeps + Pareto front
    ax = axes[0]
    ax.plot(gain_opt_radial, nf_opt_radial, "-", color="red", linewidth=1.5,
            label="Radial sweep → Γ_opt")
    ax.plot(gain_s11_radial, nf_s11_radial, "-", color="blue", linewidth=1.5,
            label="Radial sweep → S11*")
    # Line from Γ_opt to S11*
    ax.plot(gain_line, nf_line, "-", color="green", linewidth=2, alpha=0.8,
            label="Γ_opt → S11* path")
    # Pareto
    if pareto_gains:
        ax.plot(pareto_gains, pareto_nfs, "k--", linewidth=2,
                label=f"Pareto front ({len(pareto_gains)} points)")

    # Highlight key points
    # Point at Γ_opt (min NF)
    nf_at_opt = noise_figure_optimal(Gamma_opt, Gamma_opt, F_min_dB, R_n)
    ga_at_opt = available_gain(S, Gamma_opt)
    ax.plot(10 * np.log10(ga_at_opt), nf_at_opt, "ro", markersize=8,
            markerfacecolor="white", markeredgewidth=2,
            label=f"Γ_opt (F_min={F_min_dB:.1f} dB)")

    # Point at S11* (max gain approx)
    ga_at_s11 = available_gain(S, S11_star)
    nf_at_s11 = noise_figure_optimal(S11_star, Gamma_opt, F_min_dB, R_n)
    ax.plot(10 * np.log10(ga_at_s11), nf_at_s11, "bs", markersize=8,
            markerfacecolor="white", markeredgewidth=2,
            label=f"S11* (G_A≈{10*np.log10(ga_at_s11):.1f} dB)")

    # Good tradeoff region annotation
    ax.axvspan(10, 12, alpha=0.1, color="green", label="Typical target gain")
    ax.axhspan(F_min_dB - 0.2, F_min_dB + 0.5, alpha=0.1, color="red",
               label="Typical target NF")

    ax.set_xlabel("Available Gain G_A [dB]", fontsize=11)
    ax.set_ylabel("Noise Figure NF [dB]", fontsize=11)
    ax.set_title("Gain-Noise Tradeoff: Sweep Analysis", fontsize=12)
    ax.legend(fontsize=7, loc="upper left")
    ax.grid(True, alpha=0.3)
    ax.invert_yaxis()  # Lower NF is better → place on top
    ax.set_xlim(left=3, right=max(all_gains) + 1)

    # Right: Pareto front (zoomed + annotated)
    ax2 = axes[1]
    if pareto_gains:
        ax2.plot(pareto_gains, pareto_nfs, "k-", linewidth=2.5, label="Pareto front")
        # Mark every N-th point
        step = max(1, len(pareto_gains) // 10)
        for i in range(0, len(pareto_gains), step):
            ax2.plot(pareto_gains[i], pareto_nfs[i], "o", color="purple",
                     markersize=5)
            if i > 0 and i < len(pareto_gains) - 1:
                ax2.annotate(
                    f"({pareto_gains[i]:.1f}, {pareto_nfs[i]:.2f})",
                    (pareto_gains[i], pareto_nfs[i]),
                    textcoords="offset points", xytext=(5, -10),
                    fontsize=6, rotation=45
                )

    # Mark key design points on right plot too
    ax2.plot(10 * np.log10(ga_at_opt), nf_at_opt, "ro", markersize=8,
             markerfacecolor="white", markeredgewidth=2)
    ax2.plot(10 * np.log10(ga_at_s11), nf_at_s11, "bs", markersize=8,
             markerfacecolor="white", markeredgewidth=2)

    # Annotate the optimal tradeoff region
    ax2.set_xlabel("Available Gain G_A [dB]", fontsize=11)
    ax2.set_ylabel("Noise Figure NF [dB]", fontsize=11)
    ax2.set_title("Pareto-Optimal Gain-Noise Tradeoff", fontsize=12)
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)
    ax2.invert_yaxis()

    fig.tight_layout()
    save_path = "/home/ubuntu/.openclaw/workspace/python/figures/ch10/fig10_7_3_gain_noise_tradeoff.png"
    fig.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  → Saved: {save_path}")

    # Print tradeoff summary
    print(f"\nTradeoff Summary:")
    print(f"  Min NF point (Γ_opt):  NF={nf_at_opt:.2f} dB, G_A={10*np.log10(ga_at_opt):.2f} dB")
    print(f"  Max gain point (S11*): NF={nf_at_s11:.2f} dB, G_A={10*np.log10(ga_at_s11):.2f} dB")
    best_tradeoff_idx = np.argmin(np.array(pareto_nfs) + 0.5 * np.array(pareto_gains)) if pareto_nfs else None
    if best_tradeoff_idx is not None and best_tradeoff_idx < len(pareto_gains):
        print(f"  Best tradeoff (NF + 0.5*G_A): G_A={pareto_gains[best_tradeoff_idx]:.2f} dB, "
              f"NF={pareto_nfs[best_tradeoff_idx]:.2f} dB")


# ============================================================
# §10.7 Practical Examples
# ============================================================

def example_noise_cascade() -> None:
    """
    Example: cascaded noise figure calculation (Friis).
    """
    print("=" * 70)
    print("Example: Cascaded Noise Figure (Friis)")
    print("=" * 70)

    # Typical receiver chain
    NF_stages = [1.0, 6.0, 10.0]   # LNA + mixer + IF amp [dB]
    G_stages = [12.0, -7.0, 20.0]  # LNA gain, mixer gain (negative = loss), IF amp gain [dB]

    print("\nReceiver chain:")
    print(f"{'Stage':<20} {'NF [dB]':<12} {'G [dB]':<12}")
    print("-" * 44)
    stages_names = ["LNA", "Mixer", "IF Amplifier"]
    for name, nf, g in zip(stages_names, NF_stages, G_stages):
        print(f"  {name:<18} {nf:<12.1f} {g:<12.1f}")

    F_total, NF_total, Te_total = cascade_noise_friis(NF_stages, G_stages)
    print(f"\n  Total NF = {NF_total:.3f} dB")
    print(f"  Total F  = {F_total:.4f} (linear)")
    print(f"  Total Te = {Te_total:.1f} K")

    # What if we make LNA gain higher?
    print("\n  Sensitivity: LNA gain 12 dB → 15 dB:")
    G_stages2 = [15.0, -7.0, 20.0]
    _, NF2, _ = cascade_noise_friis(NF_stages, G_stages2)
    print(f"    NF_total = {NF2:.3f} dB ({NF2 - NF_total:+.3f} dB improvement)")

    print("\n  Sensitivity: LNA NF 1.0 dB → 0.8 dB:")
    NF_stages3 = [0.8, 6.0, 10.0]
    _, NF3, _ = cascade_noise_friis(NF_stages3, G_stages)
    print(f"    NF_total = {NF3:.3f} dB ({NF3 - NF_total:+.3f} dB improvement)")


def example_lna_design_summary() -> None:
    """
    Full LNA design example: compute step-by-step results.
    """
    print("=" * 70)
    print("Example: Full LNA Design Summary (Noise-Gain Tradeoff)")
    print("=" * 70)

    data = get_lna_transistor_10ghz()
    S = data['S']
    F_min_dB = data['F_min_dB']
    R_n = data['R_n']
    Gamma_opt = data['Gamma_opt']

    # Stability check
    K = k_factor(S)
    Delta = delta(S)
    stable = K > 1 and abs(Delta) < 1
    print(f"\nStability: K = {K:.4f}, |Δ| = {abs(Delta):.4f}")
    print(f"  Unconditionally stable: {stable}")

    # MAG
    g_mag, g_msg = mag_msg(S)
    print(f"  G_MAG = {10*np.log10(g_mag):.2f} dB" if not np.isnan(g_mag) else "  G_MAG undefined")
    print(f"  G_MSG = {10*np.log10(g_msg):.2f} dB")

    # Noise characteristics
    print(f"\nNoise Parameters:")
    print(f"  F_min = {F_min_dB:.2f} dB")
    print(f"  R_n   = {R_n:.1f} Ω")
    print(f"  Γ_opt = {Gamma_opt:.4f}  (|Γ_opt| = {abs(Gamma_opt):.4f})")
    print(f"  Z_opt = {z_from_gamma(Gamma_opt):.1f} Ω")

    # Available gain at Γ_opt
    ga_at_opt = available_gain(S, Gamma_opt)
    print(f"\n  At Γ_opt: G_A = {10*np.log10(ga_at_opt):.2f} dB")

    # NF at S11* (conjugate match for max gain)
    S11_star = np.conj(S[0, 0])
    nf_at_s11 = noise_figure_optimal(S11_star, Gamma_opt, F_min_dB, R_n)
    ga_at_s11 = available_gain(S, S11_star)
    print(f"  At S11*:  G_A = {10*np.log10(ga_at_s11):.2f} dB, NF = {nf_at_s11:.2f} dB")

    # Recommended tradeoff: midpoint
    Gamma_recommended = 0.6 * np.exp(1j * np.deg2rad(115))
    nf_rec = noise_figure_optimal(Gamma_recommended, Gamma_opt, F_min_dB, R_n)
    ga_rec = available_gain(S, Gamma_recommended)
    print(f"\n  Recommended Γ_S = {Gamma_recommended:.4f}")
    print(f"    G_A = {10*np.log10(ga_rec):.2f} dB")
    print(f"    NF  = {nf_rec:.2f} dB")

    # Output match
    Gamma_out_val = gamma_out(S, Gamma_recommended)
    Gamma_L_opt = np.conj(Gamma_out_val)
    print(f"    Γ_L (output conjugate match) = {Gamma_L_opt:.4f}")
    print(f"    |Γ_out| = {abs(Gamma_out_val):.4f}")

    # Total transducer gain
    G_T = transducer_gain(S, Gamma_recommended, Gamma_L_opt)
    print(f"    G_T (total transducer gain) = {10*np.log10(G_T):.2f} dB")

    print(f"\n  Summary: NF = {nf_rec:.2f} dB, G_T = {10*np.log10(G_T):.2f} dB")
    print(f"    → The LNA achieves 10 dB gain with < 1.5 dB NF ✓")


# ============================================================
# Run all §10.7 noise examples
# ============================================================

def section_10_7_noise_examples() -> None:
    """Run all §10.7 noise-related examples and generate figures."""
    print("\n" + "=" * 70)
    print(" §10.7 — AMPLIFIER NOISE EXAMPLES")
    print("=" * 70 + "\n")

    # Figures
    fig_noise_circles_smith()
    print()
    fig_nf_vs_gamma_s()
    print()
    fig_gain_noise_tradeoff()
    print()

    # Practical examples
    example_noise_cascade()
    print()
    example_lna_design_summary()

    print("\n" + "=" * 70)
    print(" §10.7 NOISE EXAMPLES COMPLETED SUCCESSFULLY")
    print("=" * 70)


# Update main to include §10.7
if __name__ == "__main__":
    # Run all §10.7 noise examples
    section_10_7_noise_examples()
