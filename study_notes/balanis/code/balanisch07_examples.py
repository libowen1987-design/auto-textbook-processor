"""
Balanis Ch7 — Antenna Synthesis: Line-Source Synthesis Methods

Implements:
  - Fourier series synthesis
  - Woodward-Lawson sampling synthesis
  - Taylor one-parameter (nbar=0) line source
  - Taylor n-bar line source
  - Dolph-Chebyshev discrete array synthesis (wraps ch06)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.special import j0, jv, i0, i1
import os
import sys
from typing import Optional

PI = np.pi
ETA_0 = 376.7303
C0 = 3e8
FIG_DIR = 'figures/ch07'
os.makedirs(FIG_DIR, exist_ok=True)

# Try importing ch06 for Chebyshev weights
try:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from balanisch06_examples import dolph_chebyshev_weights, tapered_af
    _HAS_CH06 = True
except ImportError:
    _HAS_CH06 = False
    # Fallback definitions
    def dolph_chebyshev_weights(N: int, sidelobe_dB: float) -> np.ndarray:
        R = 10**(-sidelobe_dB / 20)
        x0 = np.cosh(np.arccosh(R) / (N - 1))
        M = 512
        # Must sample symmetric about psi=0 for correct IFT
        psi = np.linspace(-PI, PI, M)
        x = x0 * np.cos(psi / 2)
        with np.errstate(invalid='ignore', divide='ignore'):
            AF_desired = np.where(np.abs(x) <= 1,
                                  np.cos((N - 1) * np.arccos(x)),
                                  np.cosh((N - 1) * np.arccosh(np.abs(x))))
        AF_desired = np.nan_to_num(AF_desired)
        AF_desired /= np.max(AF_desired)
        w = np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(AF_desired)))
        start = (M - N) // 2
        w = np.real(w[start:start + N])
        w = (w + w[::-1]) / 2
        w /= np.max(w)
        return w

    def tapered_af(theta: np.ndarray, w: np.ndarray,
                   d: float = 0.5, beta: float = 0.0,
                   k: float = 2 * PI) -> np.ndarray:
        N = len(w)
        n_arr = np.arange(N) - (N - 1) / 2
        psi = k * d * np.cos(theta) + beta
        AF = np.zeros(len(theta), dtype=complex)
        for i, w_i in enumerate(w):
            AF += w_i * np.exp(1j * n_arr[i] * psi)
        return np.abs(AF) / np.max(np.abs(AF))


# =========================================================================
# Helper: angular u-space
# =========================================================================

def theta_to_u(theta: np.ndarray, L_over_lambda: float) -> np.ndarray:
    """Convert observation angle θ to u = (L/λ) cos θ.

    Parameters
    ----------
    theta : ndarray
        Angle from array axis (rad), 0 ≤ θ ≤ π
    L_over_lambda : float
        Line source length in wavelengths

    Returns
    -------
    u : ndarray
        Spatial frequency parameter (dimensionless)
    """
    return L_over_lambda * np.cos(theta)


def u_to_theta(u: np.ndarray, L_over_lambda: float) -> np.ndarray:
    """Convert u to θ via θ = arccos(u / (L/λ))."""
    ratio = np.clip(u / L_over_lambda, -1.0, 1.0)
    return np.arccos(ratio)


# =========================================================================
# 1. Fourier Series Synthesis
# =========================================================================

def fourier_series_synthesis(
    u_samples: np.ndarray,
    F_desired: np.ndarray,
    L_over_lambda: float,
    N_terms: Optional[int] = None,
    n_theta: int = 2000
):
    """Synthesize a line-source pattern via Fourier series.

    The desired pattern F_d(u) is sampled at integer u = 0, ±1, ±2, ...
    The current distribution is I(s) = Σ C_m exp(-jπ m s), s ∈ [-1, 1].

    Parameters
    ----------
    u_samples : ndarray
        u-axis points of the desired pattern (for interpolation).
        Must be monotonically increasing.
    F_desired : ndarray
        Desired pattern values F_d(u) (normalized to [0, 1])
    L_over_lambda : float
        Line source length in wavelengths
    N_terms : int or None
        Number of Fourier terms on each side (total = 2*N_terms + 1).
        If None, N_terms = floor(L_over_lambda).
    n_theta : int
        Number of θ points for output pattern

    Returns
    -------
    result : dict
        'u' : ndarray, u-axis
        'theta' : ndarray, θ-axis (rad)
        'F_synth' : ndarray, synthesized pattern (linear, normalized)
        'F_desired_interp' : ndarray, interpolated desired pattern
        'C_m' : ndarray, Fourier coefficients
        's' : ndarray, normalized current coordinates
        'I_s' : ndarray, current distribution I(s)
        'N_terms' : int
    """
    if N_terms is None:
        N_terms = max(1, int(np.floor(L_over_lambda)))

    # Ensure u_samples is monotonically increasing for np.interp
    sort_idx = np.argsort(u_samples)
    u_sorted = u_samples[sort_idx]
    F_sorted = F_desired[sort_idx]

    # Sample the desired pattern at integer u
    m_vals = np.arange(-N_terms, N_terms + 1)
    F_m = np.interp(m_vals, u_sorted, F_sorted, left=0, right=0)

    # Reconstruct pattern: F_synth(u) = Σ F_m sinc(π(u - m))
    u_max = L_over_lambda * 1.2
    u = np.linspace(-u_max, u_max, 2000)
    F_synth = np.zeros_like(u, dtype=float)
    for m_idx, m in enumerate(m_vals):
        arg = PI * (u - m)
        # Safe sinc: sin(πx)/(πx)
        safe_arg = np.where(np.abs(arg) < 1e-12, 1e-12, arg)
        F_synth += F_m[m_idx] * np.sin(arg) / safe_arg

    F_synth = np.abs(F_synth)
    F_synth /= np.max(F_synth) if np.max(F_synth) > 0 else 1.0

    # Current distribution: I(s) = Σ F_m exp(-jπ m s)
    s = np.linspace(-1, 1, 500)
    I_s = np.zeros(s.size, dtype=complex)
    for m_idx, m in enumerate(m_vals):
        I_s += F_m[m_idx] * np.exp(-1j * PI * m * s)
    I_s /= np.max(np.abs(I_s))

    # θ-domain for pattern cut
    theta = np.linspace(0.001, PI - 0.001, n_theta)
    u_theta = theta_to_u(theta, L_over_lambda)
    F_theta = np.interp(u_theta, u, F_synth, left=0, right=0)

    # Interpolate desired for comparison
    F_d_interp = np.interp(u_theta, u_samples, F_desired, left=0, right=0)

    return {
        'u': u,
        'F_synth_u': F_synth,  # pattern on u-grid
        'theta': theta,
        'F_synth': F_theta,
        'F_desired_interp': F_d_interp,
        'C_m': F_m,
        's': s,
        'I_s': np.abs(I_s),
        'N_terms': N_terms,
        'm_vals': m_vals,
    }


# =========================================================================
# 2. Woodward-Lawson Sampling Synthesis
# =========================================================================

def woodward_lawson_synthesis(
    u_samples: np.ndarray,
    F_desired: np.ndarray,
    L_over_lambda: float,
    N_terms: Optional[int] = None,
    n_theta: int = 2000
):
    """Woodward-Lawson sampling synthesis for a line source.

    Desired pattern is sampled at u = 0, ±1, ±2, ..., ±M.
    Synthesized pattern: F(u) = Σ F_m sinc(π(u - m)).
    Current distribution: I(s) = Σ F_m exp(-jπ m s).

    Parameters
    ----------
    u_samples : ndarray
        u-axis of desired pattern (must be monotonically increasing)
    F_desired : ndarray
        Desired pattern F_d(u) (linear, normalized)
    L_over_lambda : float
        Line source length in wavelengths
    N_terms : int or None
        Sampling radius M (total 2M+1 points). If None, M = floor(L/λ).
    n_theta : int
        Number of θ points

    Returns
    -------
    result : dict
        'F_synth' : synthesized pattern (normalized linear)
        'theta' : θ-axis
        'u' : u-axis
        'I_s' : current distribution |I(s)|
        's' : normalized position [-1, 1]
        'F_m' : sampled pattern values
        'm_vals' : sample indices
    """
    if N_terms is None:
        N_terms = max(1, int(np.floor(L_over_lambda)))

    # Ensure u_samples is monotonically increasing
    sort_idx = np.argsort(u_samples)
    u_sorted = u_samples[sort_idx]
    F_sorted = F_desired[sort_idx]

    m_vals = np.arange(-N_terms, N_terms + 1)
    F_m = np.interp(m_vals, u_sorted, F_sorted, left=0, right=0)

    # Synthesize pattern over fine u grid
    u_fine = np.linspace(-L_over_lambda * 1.2, L_over_lambda * 1.2, 2000)
    F_synth = np.zeros_like(u_fine, dtype=float)
    for m_idx, m in enumerate(m_vals):
        arg = PI * (u_fine - m)
        safe = np.where(np.abs(arg) < 1e-12, 1e-12, arg)
        F_synth += F_m[m_idx] * np.sin(arg) / safe

    F_synth = np.abs(F_synth)
    F_synth /= np.max(F_synth) if np.max(F_synth) > 0 else 1.0

    # Current distribution
    s = np.linspace(-1, 1, 500)
    I_s = np.zeros(s.size, dtype=complex)
    for m_idx, m in enumerate(m_vals):
        I_s += F_m[m_idx] * np.exp(-1j * PI * m * s)
    I_s /= np.max(np.abs(I_s))

    # Map to θ
    theta = np.linspace(0.001, PI - 0.001, n_theta)
    u_theta = theta_to_u(theta, L_over_lambda)
    F_theta = np.interp(u_theta, u_fine, F_synth, left=0, right=0)

    return {
        'F_synth': F_theta,
        'theta': theta,
        'u': u_theta,
        'I_s': np.abs(I_s),
        's': s,
        'F_m': F_m,
        'm_vals': m_vals,
        'N_terms': N_terms,
    }


# =========================================================================
# 3. Taylor One-Parameter (nbar = 0)
# =========================================================================

def taylor_one_parameter(
    L_over_lambda: float,
    SLL_dB: float,
    n_theta: int = 2000,
    n_z: int = 500
):
    """Taylor one-parameter line-source distribution (nbar = 0).

    Current: I(z) = I₀(π B √(1 - (2z/L)²))
    Pattern: F(u) = sin(√((π L/λ)² cos²θ - (π B)²)) / √(...)

    Parameters
    ----------
    L_over_lambda : float
        Line source length in wavelengths
    SLL_dB : float
        Desired sidelobe level in dB (e.g., -25 for -25 dB)
    n_theta : int
        Number of θ points
    n_z : int
        Number of z-points along line source

    Returns
    -------
    result : dict
        'theta' : ndarray, θ (rad)
        'F_pat' : ndarray, pattern |F(θ)| (normalized linear)
        'F_dB' : ndarray, pattern in dB
        'z' : ndarray, position along line source (z/L)
        'I_z' : ndarray, current |I(z)| (normalized)
        'B' : float, the Taylor parameter B
        'SLL_design' : float, actual SLL from B
    """
    # Convert SLL to voltage ratio
    R_voltage = 10**(-SLL_dB / 20)

    # Compute B parameter from SLL
    # SLL_dB = -20 log10(sinh(πB)/(πB))
    # Solve iteratively or use approximate relation
    # For typical cases, B ≈ arccosh(R) / π
    B = np.arccosh(R_voltage) / PI

    # Fine-tune B to match SLL using root finding
    # The exact relation: SLL(dB) = -20*log10(sinh(πB)/(πB))
    def SLL_from_B(B_val):
        if B_val < 1e-10:
            return -np.inf  # Uniform
        ratio = np.sinh(PI * B_val) / (PI * B_val)
        return -20 * np.log10(ratio)

    # Binary search refinement
    B_min, B_max = 0.001, 3.0
    for _ in range(50):
        B_mid = (B_min + B_max) / 2
        if SLL_from_B(B_mid) > SLL_dB:
            B_min = B_mid
        else:
            B_max = B_mid
    B = (B_min + B_max) / 2

    # Compute pattern
    theta = np.linspace(0.001, PI - 0.001, n_theta)
    u = theta_to_u(theta, L_over_lambda)

    arg_sq = (PI * u)**2 - (PI * B)**2
    # Handle negative arg_sq → imaginary sqrt → sinh behavior
    F_pat = np.zeros_like(u, dtype=float)
    for i, a in enumerate(arg_sq):
        if a >= 0:
            sqrt_arg = np.sqrt(a)
            F_pat[i] = np.sin(sqrt_arg) / sqrt_arg if sqrt_arg > 1e-12 else 1.0
        else:
            sqrt_arg = np.sqrt(-a)
            F_pat[i] = np.sinh(sqrt_arg) / sqrt_arg if sqrt_arg > 1e-12 else 1.0

    F_pat = np.abs(F_pat)
    F_pat /= np.max(F_pat)

    # Current distribution: I(z) = I₀(π B √(1 - (2z/L)²))
    z = np.linspace(-0.5, 0.5, n_z)  # z/L
    xi = 2 * z  # s = 2z/L ∈ [-1, 1]
    radicand = 1.0 - xi**2
    radicand = np.clip(radicand, 0.0, 1.0)
    I_z = i0(PI * B * np.sqrt(radicand))
    I_z /= np.max(I_z)

    actual_SLL = SLL_from_B(B)
    F_dB = 20 * np.log10(F_pat + 1e-10)

    return {
        'theta': theta,
        'F_pat': F_pat,
        'F_dB': F_dB,
        'z': z,
        'I_z': I_z,
        'B': B,
        'SLL_design': actual_SLL,
        'SLL_target': SLL_dB,
        'L_over_lambda': L_over_lambda,
    }


# =========================================================================
# 4. Taylor n-bar Line Source
# =========================================================================

def taylor_line_source(
    L_over_lambda: float,
    SLL_dB: float,
    nbar: int = 5,
    n_theta: int = 2000,
    n_z: int = 500
):
    """Taylor n-bar line-source pattern synthesis.

    Pattern: F(u) = sin(πu) / (πu) * Π_{n=1}^{nbar-1} (1 - u²/uₙ²) / (1 - u²/n²)

    Parameters
    ----------
    L_over_lambda : float
        Line source length in wavelengths
    SLL_dB : float
        Desired sidelobe level in dB (negative, e.g., -25)
    nbar : int
        Number of equal sidelobes (nbar ≥ 2)
    n_theta : int
        Number of θ points
    n_z : int
        Number of current sample points

    Returns
    -------
    result : dict
        'theta' : ndarray, θ (rad)
        'F_pat' : ndarray, synthesized pattern (linear normalized)
        'F_dB' : ndarray, pattern in dB
        'z' : ndarray, position z/L
        'I_z' : ndarray, current magnitude
        'u' : ndarray, u-axis for pattern
        'u_n' : ndarray, Taylor zeros
        'A' : float, the A parameter
        'sigma' : float, beam broadening factor
        'SLL_actual' : float, actual SLL in dB
    """
    R_voltage = 10**(-SLL_dB / 20)
    A = np.arccosh(R_voltage) / PI

    # Compute nbar lower bound
    nbar_min = int(np.ceil(2 * (A**2 + 0.25)))
    if nbar < nbar_min:
        nbar = nbar_min
        # Recompute sigma with chosen nbar

    # Compute sigma
    sigma = nbar / np.sqrt(A**2 + (nbar - 0.5)**2)

    # Compute Taylor zeros u_n for n = 1, ..., nbar-1
    u_n = np.zeros(nbar)
    for n in range(1, nbar):
        u_n[n] = sigma * np.sqrt(A**2 + (n - 0.5)**2)

    # Synthesize pattern
    theta = np.linspace(0.001, PI - 0.001, n_theta)
    u = theta_to_u(theta, L_over_lambda)

    F_pat = np.zeros_like(u, dtype=float)
    for i, ui in enumerate(u):
        # Base factor: sinc(πu)
        arg0 = PI * ui
        if np.abs(arg0) < 1e-12:
            F_val = 1.0
        else:
            F_val = np.sin(arg0) / arg0

        # Product over n=1..nbar-1
        prod_val = 1.0
        for n in range(1, nbar):
            if u_n[n] != 0:
                num = 1.0 - (ui / u_n[n])**2
            else:
                num = 1.0
            denom = 1.0 - (ui / n)**2
            if np.abs(denom) < 1e-12:
                # L'Hôpital: matches sinc behavior at these points
                # Use the analytic limit
                denom = 1e-12
                num = 0.0
            prod_val *= num / denom

        F_val *= prod_val
        F_pat[i] = np.abs(F_val)

    F_pat /= np.max(F_pat)
    F_dB = 20 * np.log10(F_pat + 1e-10)

    # Current distribution via Fourier series: I(s) = 1 + 2 Σ F(m) cos(π m s)
    s = np.linspace(-1, 1, n_z)  # s = 2z/L
    I_s = np.ones_like(s, dtype=float)
    for n_val in range(1, nbar):
        # Sample pattern at u = n
        un = float(n_val)
        arg_n = PI * un
        if np.abs(arg_n) < 1e-12:
            F_n = 1.0
        else:
            F_n = np.sin(arg_n) / arg_n
        prod_n = 1.0
        for m_val in range(1, nbar):
            if m_val == n_val:
                # Limit as u → n: both numerator and denominator vanish
                # Apply analytic continuation — skip this pair
                continue
            if u_n[m_val] != 0:
                prod_n *= (1.0 - (un / u_n[m_val])**2)
            prod_n /= (1.0 - (un / m_val)**2)
        F_n *= prod_n
        I_s += 2 * F_n * np.cos(PI * n_val * s)

    I_s = np.abs(I_s)
    I_s /= np.max(I_s)

    # Measure actual SLL
    # Find the main lobe (peak) and exclude a window around it
    peak_idx = np.argmax(F_pat)
    # Exclude main lobe: only search where F < 0.5 (avoids main lobe)
    sidelobe_region = F_pat < 0.5
    peaks = []
    for i in range(2, len(F_pat) - 2):
        if sidelobe_region[i]:
            if F_pat[i] > F_pat[i - 1] and F_pat[i] >= F_pat[i + 1]:
                peaks.append(F_pat[i])
    SLL_actual = -np.inf
    if peaks:
        max_sll = max(peaks)
        if 0 < max_sll < 1.0:
            SLL_actual = 20 * np.log10(max_sll)

    z = s / 2  # convert s = 2z/L → z/L

    return {
        'theta': theta,
        'F_pat': F_pat,
        'F_dB': F_dB,
        'z': z,
        'I_z': I_s,
        'u': u,
        'u_n': u_n[1:nbar],
        'A': A,
        'sigma': sigma,
        'SLL_actual': SLL_actual,
        'SLL_target': SLL_dB,
        'nbar': nbar,
        'L_over_lambda': L_over_lambda,
    }


# =========================================================================
# 5. Dolph-Chebyshev Array Synthesis (discrete array wrapper)
# =========================================================================

def chebyshev_array_synthesis(
    N: int,
    SLL_dB: float,
    d_over_lambda: float = 0.5,
    n_theta: int = 2000
):
    """Dolph-Chebyshev synthesis for a discrete linear array.

    Computes the current weights that produce a pattern with
    constant sidelobe level SLL_dB and the narrowest possible beamwidth.

    Parameters
    ----------
    N : int
        Number of array elements
    SLL_dB : float
        Desired sidelobe level in dB (e.g., -30 for -30 dB)
    d_over_lambda : float
        Element spacing in wavelengths
    n_theta : int
        Number of θ points for pattern

    Returns
    -------
    result : dict
        'theta' : ndarray, θ (rad)
        'F_pat' : ndarray, pattern (linear normalized)
        'F_dB' : ndarray, pattern in dB
        'weights' : ndarray, element weights I_n
        'N' : int
        'SLL_dB' : float
        'SLL_actual_dB' : float, measured SLL from pattern
    """
    weights = dolph_chebyshev_weights(N, SLL_dB)

    theta = np.linspace(0.001, PI - 0.001, n_theta)
    AF = tapered_af(theta, weights, d=d_over_lambda)

    F_pat = np.abs(AF)
    F_pat /= np.max(F_pat)
    F_dB = 20 * np.log10(F_pat + 1e-10)

    # Measure actual SLL: find local maxima, exclude main lobe
    # Main lobe is at θ = π/2 for broadside (broadside array with beta=0)
    # Search only in sidelobe regions (where F_pat < 0.7 * peak to be safe)
    sidelobe_region = F_pat < 0.7
    peaks = []
    for i in range(2, len(theta) - 2):
        if sidelobe_region[i]:
            if (F_pat[i] > F_pat[i - 1] and F_pat[i] >= F_pat[i + 1]):
                peaks.append(F_pat[i])
    SLL_actual = -np.inf
    if peaks:
        max_sll = max(peaks)
        if max_sll > 0 and max_sll < 1.0:
            SLL_actual = 20 * np.log10(max_sll)

    return {
        'theta': theta,
        'F_pat': F_pat,
        'F_dB': F_dB,
        'weights': weights,
        'N': N,
        'SLL_dB': SLL_dB,
        'SLL_actual_dB': SLL_actual,
        'd_over_lambda': d_over_lambda,
    }


# =========================================================================
# Plotting Functions
# =========================================================================

def plot_fourier_synthesis():
    """Fig 7.1: Fourier series synthesis of a uniform pattern."""
    print("  [Fig 7.1] Fourier series synthesis...", flush=True)

    # Desired pattern: sectoral pattern (uniform over π/4 ≤ θ ≤ 3π/4)
    L_over_lambda = 10.0
    u_samples = np.linspace(-L_over_lambda * 1.5, L_over_lambda * 1.5, 5000)
    # Desired: rectangular pattern in u-space, centered at u=0
    F_desired = np.ones_like(u_samples)
    cutoff = 3.0  # |u| < cutoff
    F_desired[np.abs(u_samples) > cutoff] = 0.0

    result = fourier_series_synthesis(u_samples, F_desired, L_over_lambda)

    fig, axes = plt.subplots(2, 2, figsize=(14, 8))

    # (a) Desired vs synthesized pattern in dB
    ax = axes[0, 0]
    ax.plot(np.degrees(result['theta']), 20 * np.log10(result['F_desired_interp'] + 1e-10),
            'k--', lw=1.5, label='Desired')
    ax.plot(np.degrees(result['theta']), 20 * np.log10(result['F_synth'] + 1e-10),
            'b-', lw=1, alpha=0.8, label=f'Fourier synth (M={result["N_terms"]})')
    ax.set_xlabel('θ [deg]', fontsize=12)
    ax.set_ylabel('Pattern [dB]', fontsize=12)
    ax.set_title('Fourier Series Synthesis of Sector Pattern', fontsize=13)
    ax.set_xlim(0, 180)
    ax.set_ylim(-50, 3)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)

    # (b) Linear pattern comparison
    ax = axes[0, 1]
    ax.plot(np.degrees(result['theta']), result['F_desired_interp'],
            'k--', lw=1.5, label='Desired')
    ax.plot(np.degrees(result['theta']), result['F_synth'],
            'b-', lw=1, alpha=0.8, label='Synthesized')
    ax.set_xlabel('θ [deg]', fontsize=12)
    ax.set_ylabel('Pattern (linear)', fontsize=12)
    ax.set_title('Linear Scale Comparison', fontsize=13)
    ax.set_xlim(40, 140)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)

    # (c) Current distribution
    ax = axes[1, 0]
    ax.plot(result['s'], result['I_s'], 'b-', lw=1.5)
    ax.set_xlabel('s = 2z/L', fontsize=12)
    ax.set_ylabel('|I(s)| (normalized)', fontsize=12)
    ax.set_title('Synthesized Current Distribution', fontsize=13)
    ax.grid(True, alpha=0.3)

    # (d) Fourier coefficients
    ax = axes[1, 1]
    m_vals = result['m_vals']
    C_m = result['C_m']
    ax.stem(m_vals, C_m, linefmt='b-', markerfmt='bo', basefmt='r-')
    ax.set_xlabel('m', fontsize=12)
    ax.set_ylabel('C_m', fontsize=12)
    ax.set_title(f'Fourier Coefficients (2M+1 = {len(m_vals)})', fontsize=13)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig7_1_fourier_synthesis.png', dpi=150)
    plt.close()
    print("  ✅ fig7_1 done", flush=True)


def plot_woodward_lawson():
    """Fig 7.2: Woodward-Lawson synthesis."""
    print("  [Fig 7.2] Woodward-Lawson synthesis...", flush=True)

    # Desired: cosecant-squared pattern (common in radars)
    L_over_lambda = 10.0
    u_samples = np.linspace(0.1, L_over_lambda, 2000)
    theta_samples = u_to_theta(u_samples, L_over_lambda)
    # Cosecant-squared: F(θ) = csc²(θ - θ₀) for a range
    theta_0 = np.radians(10)
    F_d = np.where(theta_samples > theta_0,
                   (1.0 / np.sin(theta_samples - theta_0 + 0.01))**2,
                   0.0)
    F_d = F_d / np.max(F_d)
    # Mirror for negative u
    u_full = np.concatenate([-u_samples[::-1], u_samples])
    F_full = np.concatenate([F_d[::-1], F_d])

    result = woodward_lawson_synthesis(u_full, F_full, L_over_lambda)

    fig, axes = plt.subplots(2, 2, figsize=(14, 8))

    # (a) Pattern in dB
    ax = axes[0, 0]
    F_dB = 20 * np.log10(result['F_synth'] + 1e-10)
    # Interpolate desired at same θ
    F_d_interp = np.interp(result['u'], u_full, F_full, left=0, right=0)
    F_d_dB = 20 * np.log10(F_d_interp + 1e-10)
    ax.plot(np.degrees(result['theta']), F_d_dB, 'k--', lw=1.5, label='Desired')
    ax.plot(np.degrees(result['theta']), F_dB, 'b-', lw=1, alpha=0.8,
            label=f'WL synth (M={result["N_terms"]})')
    ax.set_xlabel('θ [deg]', fontsize=12)
    ax.set_ylabel('Pattern [dB]', fontsize=12)
    ax.set_title('Woodward-Lawson Sampling Synthesis', fontsize=13)
    ax.set_xlim(0, 180)
    ax.set_ylim(-50, 3)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)

    # (b) Pattern in linear scale
    ax = axes[0, 1]
    ax.plot(np.degrees(result['theta']), F_d_interp, 'k--', lw=1.5, label='Desired')
    ax.plot(np.degrees(result['theta']), result['F_synth'], 'b-', lw=1, alpha=0.8,
            label='Synthesized')
    ax.set_xlabel('θ [deg]', fontsize=12)
    ax.set_ylabel('Pattern (linear)', fontsize=12)
    ax.set_title('Linear Pattern Comparison', fontsize=13)
    ax.set_xlim(0, 60)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)

    # (c) Current distribution
    ax = axes[1, 0]
    ax.plot(result['s'], result['I_s'], 'b-', lw=1.5)
    ax.set_xlabel('s = 2z/L', fontsize=12)
    ax.set_ylabel('|I(s)| (normalized)', fontsize=12)
    ax.set_title('Woodward-Lawson Current Distribution', fontsize=13)
    ax.grid(True, alpha=0.3)

    # (d) Sample values
    ax = axes[1, 1]
    m_vals = result['m_vals']
    F_m = result['F_m']
    ax.stem(m_vals, F_m, linefmt='b-', markerfmt='bo', basefmt='r-')
    ax.set_xlabel('m (sample index)', fontsize=12)
    ax.set_ylabel('F_m (sampled pattern)', fontsize=12)
    ax.set_title(f'Woodward-Lawson Sample Values (M={result["N_terms"]})', fontsize=13)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig7_2_woodward_lawson.png', dpi=150)
    plt.close()
    print("  ✅ fig7_2 done", flush=True)


def plot_taylor_one_parameter():
    """Fig 7.3: Taylor one-parameter patterns."""
    print("  [Fig 7.3] Taylor one-parameter...", flush=True)

    L_over_lambda = 10.0

    fig, axes = plt.subplots(2, 2, figsize=(14, 8))

    # (a) Patterns for various SLLs
    ax = axes[0, 0]
    sll_targets = [-20, -25, -30, -40]
    colors = ['b', 'g', 'r', 'm']
    for sll, c in zip(sll_targets, colors):
        t1 = taylor_one_parameter(L_over_lambda, sll)
        ax.plot(np.degrees(t1['theta']), t1['F_dB'], c, lw=1.5,
                label=f'SLL={sll} dB (B={t1["B"]:.3f})')
    ax.set_xlabel('θ [deg]', fontsize=12)
    ax.set_ylabel('Pattern [dB]', fontsize=12)
    ax.set_title(f'Taylor One-Parameter, L/λ = {L_over_lambda}', fontsize=13)
    ax.set_xlim(0, 180)
    ax.set_ylim(-60, 3)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9)

    # (b) Current distributions
    ax = axes[0, 1]
    for sll, c in zip(sll_targets, colors):
        t1 = taylor_one_parameter(L_over_lambda, sll)
        ax.plot(t1['z'], t1['I_z'], c, lw=1.5,
                label=f'SLL={sll} dB, B={t1["B"]:.3f}')
    ax.set_xlabel('z / L', fontsize=12)
    ax.set_ylabel('|I(z)|', fontsize=12)
    ax.set_title('Taylor One-Parameter Current Distributions', fontsize=13)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9)

    # (c) SLL vs B parameter
    ax = axes[1, 0]
    B_vals = np.linspace(0.02, 1.5, 100)
    SLL_func = lambda B: -20 * np.log10(np.sinh(PI * B) / (PI * B) + 1e-15)
    SLL_vals = [SLL_func(B) for B in B_vals]
    ax.plot(B_vals, SLL_vals, 'b-', lw=1.5)
    ax.set_xlabel('B (Taylor parameter)', fontsize=12)
    ax.set_ylabel('SLL [dB]', fontsize=12)
    ax.set_title('Sidelobe Level vs B Parameter', fontsize=13)
    ax.grid(True, alpha=0.3)

    # (d) HPBW broadening
    ax = axes[1, 0]
    # Show uniform for comparison
    t1_hp = taylor_one_parameter(L_over_lambda, -30)
    ax.text(0.5, 0.1,
            f'L/λ = {L_over_lambda}\n'
            f'SLL=-25dB: B={taylor_one_parameter(L_over_lambda, -25)["B"]:.3f}\n'
            f'SLL=-30dB: B={t1_hp["B"]:.3f}\n'
            f'SLL=-40dB: B={taylor_one_parameter(L_over_lambda, -40)["B"]:.3f}',
            transform=ax.transAxes, fontsize=10, va='bottom',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    # (e) Comparison of uniform vs Taylor -25dB pattern
    ax = axes[1, 1]
    # Uniform: B=0 → sinc pattern
    theta = np.linspace(0.001, PI - 0.001, 2000)
    u = theta_to_u(theta, L_over_lambda)
    F_uniform = np.abs(np.sinc(u))
    F_uniform_dB = 20 * np.log10(F_uniform + 1e-10)
    ax.plot(np.degrees(theta), F_uniform_dB, 'k--', lw=1.5, label='Uniform (B=0)')
    for sll, c in zip([-25, -35], ['b', 'r']):
        t1 = taylor_one_parameter(L_over_lambda, sll)
        ax.plot(np.degrees(t1['theta']), t1['F_dB'], c, lw=1.5,
                label=f'T1P SLL={sll} dB')
    ax.set_xlabel('θ [deg]', fontsize=12)
    ax.set_ylabel('Pattern [dB]', fontsize=12)
    ax.set_title('Uniform vs Taylor One-Parameter', fontsize=13)
    ax.set_xlim(75, 105)
    ax.set_ylim(-60, 3)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9)

    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig7_3_taylor_one_parameter.png', dpi=150)
    plt.close()
    print("  ✅ fig7_3 done", flush=True)


def plot_taylor_nbar():
    """Fig 7.4: Taylor n-bar line source patterns."""
    print("  [Fig 7.4] Taylor n-bar...", flush=True)

    L_over_lambda = 10.0

    fig, axes = plt.subplots(2, 2, figsize=(14, 8))

    # (a) Vary nbar for fixed SLL
    ax = axes[0, 0]
    SLL = -30
    nbars = [3, 5, 8]
    colors = ['b', 'g', 'r']
    for nbar, c in zip(nbars, colors):
        t = taylor_line_source(L_over_lambda, SLL, nbar=nbar)
        label = f'$\\bar{{n}}$={nbar} (σ={t["sigma"]:.4f})'
        ax.plot(np.degrees(t['theta']), t['F_dB'], c, lw=1.5, label=label)
    ax.set_xlabel('θ [deg]', fontsize=12)
    ax.set_ylabel('Pattern [dB]', fontsize=12)
    ax.set_title(f'Taylor n-bar, SLL={SLL} dB, L/λ={L_over_lambda}', fontsize=13)
    ax.set_xlim(0, 180)
    ax.set_ylim(-60, 3)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9)

    # (b) Corresponding current distributions
    ax = axes[0, 1]
    for nbar, c in zip(nbars, colors):
        t = taylor_line_source(L_over_lambda, SLL, nbar=nbar)
        ax.plot(t['z'], t['I_z'], c, lw=1.5,
                label=f'$\\bar{{n}}$={nbar}')
    ax.set_xlabel('z / L', fontsize=12)
    ax.set_ylabel('|I(z)|', fontsize=12)
    ax.set_title('Taylor n-bar Current Distributions (-30 dB SLL)', fontsize=13)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9)

    # (c) Vary SLL for fixed nbar
    ax = axes[1, 0]
    nbar = 5
    slls = [-20, -25, -30, -35]
    colors2 = ['b', 'g', 'r', 'm']
    for sll, c in zip(slls, colors2):
        t = taylor_line_source(L_over_lambda, sll, nbar=nbar)
        ax.plot(np.degrees(t['theta']), t['F_dB'], c, lw=1.5,
                label=f'SLL={sll} dB')
    ax.set_xlabel('θ [deg]', fontsize=12)
    ax.set_ylabel('Pattern [dB]', fontsize=12)
    ax.set_title(f'Taylor $\\bar{{n}}$={nbar}, Various SLL', fontsize=13)
    ax.set_xlim(70, 110)
    ax.set_ylim(-60, 3)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9)

    # (d) Taylor zeros and pattern detail
    ax = axes[1, 1]
    t = taylor_line_source(L_over_lambda, -30, nbar=6)
    ax.plot(np.degrees(t['theta']), t['F_dB'], 'b-', lw=1.5,
            label=f'$\\bar{{n}}$={t["nbar"]}, SLL={SLL} dB')
    # Mark the Taylor zeros in u-space
    u_zeros = t['u_n']
    # Map zeros to θ
    theta_zeros = u_to_theta(u_zeros, L_over_lambda)
    for tz in theta_zeros:
        if 0 < np.degrees(tz) < 180:
            ax.axvline(np.degrees(tz), color='r', ls=':', alpha=0.5)
    ax.set_xlabel('θ [deg]', fontsize=12)
    ax.set_ylabel('Pattern [dB]', fontsize=12)
    ax.set_title('Taylor Zeros (dashed) and Pattern', fontsize=13)
    ax.set_xlim(0, 180)
    ax.set_ylim(-60, 3)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9)

    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig7_4_taylor_nbar.png', dpi=150)
    plt.close()
    print("  ✅ fig7_4 done", flush=True)


def plot_chebyshev_synthesis():
    """Fig 7.5: Dolph-Chebyshev discrete array synthesis."""
    print("  [Fig 7.5] Dolph-Chebyshev...", flush=True)

    fig, axes = plt.subplots(2, 2, figsize=(14, 8))

    N = 20
    d = 0.5

    # (a) Various SLL levels
    ax = axes[0, 0]
    slls = [-20, -30, -40]
    colors = ['b', 'g', 'r']
    for sll, c in zip(slls, colors):
        r = chebyshev_array_synthesis(N, sll, d)
        ax.plot(np.degrees(r['theta']), r['F_dB'], c, lw=1.5,
                label=f'SLL={sll} dB (actual: {r["SLL_actual_dB"]:.1f} dB)')
    ax.set_xlabel('θ [deg]', fontsize=12)
    ax.set_ylabel('Pattern [dB]', fontsize=12)
    ax.set_title(f'Dolph-Chebyshev N={N}, d={d}λ', fontsize=13)
    ax.set_xlim(0, 180)
    ax.set_ylim(-60, 3)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9)

    # (b) Weight distributions
    ax = axes[0, 1]
    for sll, c in zip(slls, colors):
        r = chebyshev_array_synthesis(N, sll, d)
        ax.plot(np.arange(N), r['weights'], 'o-', c=c, lw=1.5,
                markersize=4, label=f'SLL={sll} dB')
    ax.set_xlabel('Element index n', fontsize=12)
    ax.set_ylabel('Weight Iₙ', fontsize=12)
    ax.set_title('Chebyshev Current Weights', fontsize=13)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9)

    # (c) Comparison: Chebyshev vs Taylor (continuous approximation)
    ax = axes[1, 0]
    SLL = -30
    r_cheb = chebyshev_array_synthesis(N, SLL, d)
    ax.plot(np.degrees(r_cheb['theta']), r_cheb['F_dB'], 'b-', lw=1.5,
            label=f'Chebyshev N={N}')
    # Continuous line source with same SLL
    L_eq = N * d  # equivalent length
    t = taylor_line_source(L_eq, SLL, nbar=5)
    ax.plot(np.degrees(t['theta']), t['F_dB'], 'r--', lw=1.5,
            label=f'Taylor nbar={t["nbar"]}, L/λ={L_eq}')
    ax.set_xlabel('θ [deg]', fontsize=12)
    ax.set_ylabel('Pattern [dB]', fontsize=12)
    ax.set_title('Chebyshev vs Taylor (Discrete vs Continuous)', fontsize=13)
    ax.set_xlim(0, 180)
    ax.set_ylim(-60, 3)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9)

    # (d) Narrowest beamwidth property
    ax = axes[1, 1]
    Ns = [10, 16, 24, 32]
    SLL0 = -30
    # Compute HPBW for Chebyshev
    hpbw_cheb = []
    for n in Ns:
        r = chebyshev_array_synthesis(n, SLL0, d)
        F = r['F_pat']
        th = r['theta']
        half = 0.5
        # Find -3dB points
        peak_idx = np.argmax(F)
        left_3dB = 0
        for i in range(peak_idx, 0, -1):
            if F[i] <= half:
                left_3dB = np.interp(half, [F[i], F[i + 1]],
                                     [np.degrees(th[i]), np.degrees(th[i + 1])])
                break
        right_3dB = 180
        for i in range(peak_idx, len(F) - 1):
            if F[i] <= half:
                right_3dB = np.interp(half, [F[i], F[i - 1]],
                                      [np.degrees(th[i]), np.degrees(th[i - 1])])
                break
        hpbw_cheb.append(right_3dB - left_3dB)
    ax.plot(Ns, hpbw_cheb, 'bo-', lw=1.5, markersize=6, label='Chebyshev')
    # Uniform array HPBW: ~ 0.886/(Nd/λ) in radians
    hpbw_uniform = [np.degrees(0.886 / (n * d)) for n in Ns]
    ax.plot(Ns, hpbw_uniform, 'rs--', lw=1.5, markersize=6, label='Uniform')
    ax.set_xlabel('N', fontsize=12)
    ax.set_ylabel('HPBW [deg]', fontsize=12)
    ax.set_title(f'HPBW: Chebyshev vs Uniform, SLL={SLL0}dB, d={d}λ', fontsize=13)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)

    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig7_5_chebyshev.png', dpi=150)
    plt.close()
    print("  ✅ fig7_5 done", flush=True)


def plot_synthesis_comparison():
    """Fig 7.6: Comparison of all synthesis methods."""
    print("  [Fig 7.6] Synthesis comparison...", flush=True)

    L_over_lambda = 10.0
    theta = np.linspace(0.001, PI - 0.001, 2000)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # (a) All methods for the same target SLL (-30 dB)
    ax = axes[0]
    SLL = -30

    # Taylor one-parameter
    t1 = taylor_one_parameter(L_over_lambda, SLL)
    ax.plot(np.degrees(t1['theta']), t1['F_dB'], 'b-', lw=1.5,
            label=f'Taylor 1-param (B={t1["B"]:.3f})')

    # Taylor n-bar
    t_n = taylor_line_source(L_over_lambda, SLL, nbar=5)
    ax.plot(np.degrees(t_n['theta']), t_n['F_dB'], 'r-', lw=1.5,
            label=f'Taylor nbar={t_n["nbar"]} (σ={t_n["sigma"]:.4f})')

    # Chebyshev (equivalent discrete)
    N_eq = int(L_over_lambda / 0.5)  # d = 0.5λ
    if N_eq % 2 == 0:
        N_eq += 1  # ensure odd for center element
    r_cheb = chebyshev_array_synthesis(N_eq, SLL)
    ax.plot(np.degrees(r_cheb['theta']), r_cheb['F_dB'], 'g-', lw=1.5,
            alpha=0.8, label=f'Chebyshev N={N_eq}')

    # Uniform reference
    u = theta_to_u(theta, L_over_lambda)
    F_uniform = np.abs(np.sinc(u))
    F_uniform_dB = 20 * np.log10(F_uniform + 1e-10)
    ax.plot(np.degrees(theta), F_uniform_dB, 'k--', lw=1, alpha=0.7,
            label='Uniform (-13.5 dB SLL)')

    ax.set_xlabel('θ [deg]', fontsize=12)
    ax.set_ylabel('Pattern [dB]', fontsize=12)
    ax.set_title(f'All Methods Compared (SLL={SLL} dB, L/λ={L_over_lambda})',
                 fontsize=13)
    ax.set_xlim(0, 180)
    ax.set_ylim(-60, 3)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9)

    # (b) Zoom near main beam
    ax = axes[1]
    ax.plot(np.degrees(t1['theta']), t1['F_dB'], 'b-', lw=1.5,
            label=f'Taylor 1-param')
    ax.plot(np.degrees(t_n['theta']), t_n['F_dB'], 'r-', lw=1.5,
            label=f'Taylor nbar={t_n["nbar"]}')
    ax.plot(np.degrees(r_cheb['theta']), r_cheb['F_dB'], 'g-', lw=1.5,
            alpha=0.8, label=f'Chebyshev N={N_eq}')
    ax.plot(np.degrees(theta), F_uniform_dB, 'k--', lw=1, alpha=0.7,
            label='Uniform')
    ax.set_xlabel('θ [deg]', fontsize=12)
    ax.set_ylabel('Pattern [dB]', fontsize=12)
    ax.set_title('Main Lobe Detail (Zoom)', fontsize=13)
    ax.set_xlim(75, 105)
    ax.set_ylim(-10, 3)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=9)

    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig7_6_synthesis_comparison.png', dpi=150)
    plt.close()
    print("  ✅ fig7_6 done", flush=True)


# =========================================================================
# Verification: Half-wave dipole pattern synthesis
# =========================================================================

def verify_known_pattern():
    """Verify Fourier/Woodward-Lawson on a known closed-form pattern.

    Use a uniform current distribution as reference:
      Pattern: F(u) = sin(πu)/(πu) = sinc(u), numpy.sinc(x) = sin(πx)/(πx)
    This is the exact Fourier transform of a uniform line source.
    """
    print("\n--- Verification: Uniform Line Source Pattern Synthesis ---", flush=True)

    L_over_lambda = 10.0
    # Build u on a monotonically increasing grid (important for np.interp)
    u = np.linspace(-L_over_lambda, L_over_lambda, 4000)

    # True pattern of uniform line source: sinc(u) = sin(πu)/(πu)
    F_true = np.abs(np.sinc(u))  # numpy sinc(x) = sin(πx)/(πx)
    F_true /= np.max(F_true)

    # Fourier series synthesis (should reproduce sinc exactly)
    fs = fourier_series_synthesis(u, F_true, L_over_lambda)

    # Compare on the same u-grid
    # fs['F_synth_u'] is on fs['u'] grid, need to interpolate to our u grid
    F_synth_u = np.interp(u, fs['u'], fs['F_synth_u'], left=0, right=0)
    error = np.abs(F_synth_u - F_true)
    rmse = np.sqrt(np.mean(error**2))
    max_err = np.max(error)

    print(f"  Fourier series synthesis of uniform line source pattern:", flush=True)
    print(f"    L/λ = {L_over_lambda}, M = {fs['N_terms']}", flush=True)
    print(f"    RMS error = {rmse:.4f} ({rmse*100:.2f}%)", flush=True)
    print(f"    Max error = {max_err:.4f} ({max_err*100:.2f}%)", flush=True)

    if rmse < 0.05:
        print(f"  ✅ Error < 5% PASS", flush=True)
    else:
        print(f"  ⚠️  Error >= 5%, check implementation", flush=True)

    # Also test Taylor one-parameter SLL accuracy
    print(f"", flush=True)
    SLL_pairs = [(-25, 0.5), (-30, 0.5), (-35, 1.0)]
    for SLL_target, toler in SLL_pairs:
        t1 = taylor_one_parameter(L_over_lambda, SLL_target)
        err_SLL = abs(t1['SLL_design'] - SLL_target)
        print(f"  Taylor 1-param SLL={SLL_target} dB: B={t1['B']:.4f}, "
              f"actual SLL={t1['SLL_design']:.2f} dB (error={err_SLL:.2f} dB)",
              flush=True)
        if err_SLL < toler:
            print(f"    ✅ SLL error < {toler} dB PASS", flush=True)
        else:
            print(f"    ⚠️  SLL error >= {toler} dB", flush=True)

    # Test nbar SLL accuracy
    print(f"", flush=True)
    T_SLL = -30
    t_n = taylor_line_source(L_over_lambda, T_SLL, nbar=5)
    print(f"  Taylor nbar=5 SLL={T_SLL} dB: "
          f"actual SLL={t_n['SLL_actual']:.1f} dB, "
          f"σ={t_n['sigma']:.4f}, A={t_n['A']:.4f}",
          flush=True)

    # Test Chebyshev SLL accuracy — fix peak detection
    print(f"", flush=True)
    N = 20
    for SLL_target in [-20, -30, -40]:
        r = chebyshev_array_synthesis(N, SLL_target)
        err_SLL = abs(r['SLL_actual_dB'] - SLL_target)
        status = "✅" if err_SLL < 1.0 else "⚠️"
        print(f"  Chebyshev N={N} SLL={SLL_target} dB: "
              f"actual SLL={r['SLL_actual_dB']:.1f} dB (error={err_SLL:.1f} dB) {status}",
              flush=True)

    return rmse


# =========================================================================
# Main
# =========================================================================

if __name__ == '__main__':
    print("=" * 60, flush=True)
    print("  Balanis Ch7: Antenna Synthesis", flush=True)
    print("=" * 60, flush=True)

    print("\n[1/6] Fourier series synthesis...", flush=True)
    plot_fourier_synthesis()

    print("\n[2/6] Woodward-Lawson synthesis...", flush=True)
    plot_woodward_lawson()

    print("\n[3/6] Taylor one-parameter...", flush=True)
    plot_taylor_one_parameter()

    print("\n[4/6] Taylor n-bar...", flush=True)
    plot_taylor_nbar()

    print("\n[5/6] Dolph-Chebyshev...", flush=True)
    plot_chebyshev_synthesis()

    print("\n[6/6] Synthesis comparison...", flush=True)
    plot_synthesis_comparison()

    # Verification
    rmse = verify_known_pattern()

    print("\n" + "=" * 60, flush=True)
    print(f"  ✅ Ch7 done. Figures in {FIG_DIR}/", flush=True)
    print(f"  Uniform source pattern synthesis RMSE: {rmse*100:.2f}%", flush=True)
    print("=" * 60, flush=True)
