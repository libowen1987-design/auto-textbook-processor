"""
Balanis Ch4 — Linear Wire Antennas

Models and examples for:
  - Infinitesimal / small / finite-length dipoles
  - Half-wave dipole
  - Mutual impedance (two parallel dipoles)
  - Yagi-Uda array (simplified)
  - LPDA design

Author: Xiaolongxia
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from scipy.special import sici
from typing import Tuple

# Constants
ETA_0: float = 376.7303  # free-space impedance [Ω]
C0: float = 3e8
PI = np.pi

FIG_DIR = 'figures/ch04'
os.makedirs(FIG_DIR, exist_ok=True)

# =========================================================================
# Dipole Pattern Functions
# =========================================================================

def infinitesimal_dipole(theta: np.ndarray, I0: float = 1.0,
                         l: float = 1e-3, k: float = 2*PI) -> np.ndarray:
    """Far-field E_theta of an infinitesimal dipole (l << lambda)."""
    return 1j * ETA_0 * k * I0 * l * np.exp(-1j*k*1) / (4*PI * 1) * np.sin(theta)


def small_dipole(theta: np.ndarray, I0: float = 1.0,
                 l: float = 0.05, k: float = 2*PI) -> np.ndarray:
    """Far-field E_theta of a small dipole (l < lambda/10)."""
    return 1j * ETA_0 * k * I0 * l * np.exp(-1j*k*1) / (8*PI * 1) * np.sin(theta)


def finite_dipole_pattern(theta: np.ndarray, l: float, k: float = 2*PI) -> np.ndarray:
    """Normalized far-field pattern of a finite-length dipole.
    
    Parameters
    ----------
    theta : ndarray
        Observation angles (rad), 0 = zenith
    l : float
        Dipole total length (m)
    k : float
        Wavenumber (rad/m)
    
    Returns
    -------
    F : ndarray
        Normalized field pattern |E_theta|
    """
    kl2 = k * l / 2
    cos_theta = np.cos(theta)
    num = np.cos(kl2 * cos_theta) - np.cos(kl2)
    den = np.sin(theta)
    # Avoid division by zero at theta=0, pi
    F = np.zeros_like(theta)
    mask = np.abs(den) > 1e-10
    F[mask] = np.abs(num[mask] / den[mask])
    # Limit at theta -> 0, pi
    # Use L'Hospital: F(0) = 0 (for most lengths)
    return F / np.max(F) if np.max(F) > 0 else F


def half_wave_dipole_pattern(theta: np.ndarray) -> np.ndarray:
    """Normalized far-field pattern of a half-wave dipole."""
    F = np.zeros_like(theta)
    mask = np.abs(np.sin(theta)) > 1e-10
    F[mask] = np.abs(np.cos(PI/2 * np.cos(theta[mask])) / np.sin(theta[mask]))
    return F / np.max(F)


def dipole_directivity(l: float, k: float = 2*PI) -> float:
    """Compute directivity of a center-fed dipole of length l.
    
    Using numerical integration of the pattern function.
    """
    def F2(t):
        kl2 = k * l / 2
        num = np.cos(kl2 * np.cos(t)) - np.cos(kl2)
        den = np.sin(t)
        if abs(den) < 1e-10:
            return 0.0
        return (num / den)**2 * np.sin(t)
    
    N = 20000
    t = np.linspace(0, PI, N)
    vals = np.array([F2(ti) for ti in t])
    # Max at theta = pi/2 (typically)
    U_max = F2(PI/2) if abs(np.sin(PI/2)) > 1e-10 else 1.0
    P_rad = 2 * PI * np.trapezoid(vals, t)  # phi integral = 2*pi
    return 4 * PI * U_max / P_rad if P_rad > 0 else 0.0


# =========================================================================
# Impedance
# =========================================================================

def Ci(x: float) -> float:
    """Cosine integral Ci(x) = -∫_x^∞ cos(t)/t dt."""
    si, ci = sici(x)
    return ci


def Si(x: float) -> float:
    """Sine integral Si(x) = ∫_0^x sin(t)/t dt."""
    si, ci = sici(x)
    return si


def half_wave_self_impedance() -> Tuple[float, float]:
    """Self-impedance of half-wave dipole via induced EMF method.

    Returns (R, X) in Ohms.

    For l=λ/2 (kl=π), induced EMF method simplifies to:
      R = (η/4π) · Cin(2π) ≈ 73.1 Ω
      X = (η/4π) · Si(2π)  ≈ 42.5 Ω
    """
    gamma = 0.57721566
    si2, ci2 = sici(2*PI)
    Cin_2pi = gamma + np.log(2*PI) - ci2
    R = ETA_0 / (4*PI) * Cin_2pi  # = 30 * Cin(2π) ≈ 73.1
    X = ETA_0 / (4*PI) * si2      # = 30 * Si(2π) ≈ 42.5
    return R, X


def mutual_impedance_parallel(d: float, l: float = 0.5,
                              k: float = 2*PI) -> Tuple[float, float]:
    """Mutual impedance between two parallel dipoles.
    
    Parameters
    ----------
    d : float
        Separation in wavelengths
    l : float
        Dipole length in wavelengths
    k : float
        Wavenumber
    
    Returns (R21, X21) mutual impedance in Ohms.
    """
    kd = k * d
    h = k * l / 2  # electrical half-length
    
    # Using formulas from Balanis Ch4 for half-wave dipoles
    if abs(l - 0.5) < 0.01:
        # Half-wave dipoles
        u0 = kd
        u1 = k * (np.sqrt(d**2 + (l/2 + l/2)**2) - l)
        u2 = k * (np.sqrt(d**2 + (l/2 + l/2)**2) + l)
        
        R21 = ETA_0 / (4*PI) * (2*Ci(u0) - Ci(u1) - Ci(u2))
        X21 = -ETA_0 / (4*PI) * (2*Si(u0) - Si(u1) - Si(u2))
        return R21, X21
    else:
        # General length - simplified model
        R21 = ETA_0 / (2*PI) * (Ci(kd) - 0.5*Ci(kd + h) - 0.5*Ci(kd - h))
        X21 = -ETA_0 / (2*PI) * (Si(kd) - 0.5*Si(kd + h) - 0.5*Si(kd - h))
        return R21, X21


# =========================================================================
# Yagi-Uda (simplified)
# =========================================================================

def yagi_pattern(theta: np.ndarray, num_elements: int = 3,
                 d_ref: float = 0.25, d_dir: float = 0.34,
                 l_ref: float = 0.5, l_drv: float = 0.47,
                 l_dir: float = 0.43) -> np.ndarray:
    """Simplified Yagi-Uda far-field pattern (element factor × array factor).
    
    All elements are assumed as half-wave dipoles along z-axis.
    Elements are along the x-axis (endfire direction = theta=pi/2, phi=0).
    
    Parameters
    ----------
    theta : ndarray
        Elevation angles (rad)
    num_elements : int
        Total number including reflector + driver + directors
    d_ref : float
        Reflector spacing (lambda)
    d_dir : float
        Director spacing (lambda)
    l_ref / l_drv / l_dir : float
        Element lengths (lambda)
    
    Returns
    -------
    pattern : ndarray
        Normalized power pattern
    """
    k = 2 * PI
    n_ref = 1
    n_dir = num_elements - 2
    
    # Element positions along x-axis (lambda)
    x = np.zeros(num_elements)
    x[0] = -d_ref  # reflector
    # drivers at origin
    for i in range(n_dir):
        x[2 + i] = (i + 1) * d_dir  # directors
    
    # Element factor (half-wave dipole along z)
    ef = np.zeros_like(theta)
    mask = np.abs(np.sin(theta)) > 1e-10
    ef[mask] = np.abs(np.cos(PI/2 * np.cos(theta[mask])) / np.sin(theta[mask]))
    ef[~mask] = 0.0
    
    # Array factor (endfire along x, phi = 0)
    # For theta measured from z-axis, the projection onto x is sin(theta)*cos(phi)
    # For phi=0 (x-axis): projection = sin(theta)
    af = np.zeros(len(theta), dtype=complex)
    for i in range(num_elements):
        phase = k * x[i] * np.sin(theta)
        # Current amplitude ~ 1 for driver, ~0.8 for reflector, ~0.7 for directors
        amp = 1.0
        if i == 0:
            amp = 0.8  # reflector
        elif i >= 2:
            amp = 0.7  # directors
        af += amp * np.exp(1j * phase)
    
    pattern = np.abs(ef * af)**2
    return pattern / np.max(pattern) if np.max(pattern) > 0 else pattern


# =========================================================================
# LPDA Design
# =========================================================================

def lpda_design(tau: float, sigma: float, f_min: float, f_max: float) -> dict:
    """Design a Log-Periodic Dipole Array.
    
    Parameters
    ----------
    tau : float
        Scale factor (0.8-0.95)
    sigma : float
        Spacing factor (0.03-0.2)
    f_min : float
        Minimum frequency [Hz]
    f_max : float
        Maximum frequency [Hz]
    
    Returns
    -------
    dict with element lengths, spacings, estimated gain
    """
    # Apex half-angle
    alpha = 2 * np.arctan((1 - tau) / (4 * sigma))
    
    # Longest and shortest elements
    l_max = 0.5 * C0 / f_min
    l_min = 0.5 * C0 / f_max
    
    # Number of elements
    N = int(np.ceil(np.log(l_max / l_min) / np.log(1/tau))) + 1
    
    # Element lengths
    lengths = np.array([l_max * tau**n for n in range(N)])
    
    # Element positions (from apex)
    spacing = np.array([sigma * 2 * lengths[n] for n in range(N-1)])
    positions = np.zeros(N)
    for n in range(1, N):
        positions[n] = positions[n-1] + spacing[n-1]
    
    # Estimated directivity (Carrel's formula)
    B = 0.5 * (1 + tau) / (1 - tau)
    Lambda = 1.1 + 30.7 * (1 - tau) * sigma  # empirical
    D_est = 10 * np.log10(B * Lambda) if B * Lambda > 0 else 6.0
    
    return {
        'tau': tau, 'sigma': sigma, 'alpha_deg': np.degrees(alpha),
        'N': N, 'lengths': lengths, 'positions': positions,
        'gain_est_dBi': D_est,
        'f_min_Hz': f_min, 'f_max_Hz': f_max
    }


# =========================================================================
# Visualization
# =========================================================================

def plot_pattern_comparison() -> None:
    """Fig 4.1: Pattern comparison for various dipole lengths."""
    theta = np.linspace(0, PI, 361)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), 
                              subplot_kw={'projection': 'polar'})
    
    lengths = [0.001, 0.1, 0.5, 1.0, 1.5]
    labels = ['Infinitesimal', 'Small (l=0.1λ)', 'λ/2', 'λ', '1.5λ']
    colors = ['b', 'g', 'r', 'm', 'orange']
    
    for ax in axes:
        for l, lab, c in zip(lengths, labels, colors):
            if l == 0.001:
                pat = infinitesimal_dipole(theta)
                pat = np.abs(pat) / np.max(np.abs(pat))
            elif l == 0.1:
                pat = small_dipole(theta)
                pat = np.abs(pat) / np.max(np.abs(pat))
            else:
                pat = finite_dipole_pattern(theta, l)
            ax.plot(theta, pat, c, lw=1.5, label=lab)
        ax.set_theta_zero_location('N')
        ax.set_thetamin(0)
        ax.set_thetamax(180)
    
    axes[0].set_title('E-Plane Pattern (Linear)', va='bottom')
    axes[0].legend(loc='upper right', fontsize=8)
    
    # dB scale
    for l, lab, c in zip(lengths, labels, colors):
        if l == 0.001:
            pat = infinitesimal_dipole(theta)
            pat_db = 20 * np.log10(np.abs(pat) / np.max(np.abs(pat)) + 1e-15)
            pat_db = np.clip(pat_db, -40, 0)
            axes[1].plot(theta, pat_db + 40, c, lw=1.5, label=lab + ' (dB)')
        elif l == 0.1:
            pat = small_dipole(theta)
            pat_db = 20 * np.log10(np.abs(pat) / np.max(np.abs(pat)) + 1e-15)
            pat_db = np.clip(pat_db, -40, 0)
            axes[1].plot(theta, pat_db + 40, c, lw=1.5, label=lab + ' (dB)')
        else:
            pat = finite_dipole_pattern(theta, l)
            pat_db = 20 * np.log10(np.abs(pat) / np.max(np.abs(pat)) + 1e-15)
            pat_db = np.clip(pat_db, -40, 0)
            axes[1].plot(theta, pat_db + 40, c, lw=1.5, label=lab + ' (dB)')
    
    axes[1].set_title('Pattern (dB, 0–40dB range)', va='bottom')
    axes[1].legend(loc='upper right', fontsize=8)
    
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig4_1_dipole_patterns.png', dpi=150)
    plt.close()
    print("  fig4_1 done", flush=True)


def plot_mutual_impedance() -> None:
    """Fig 4.2: Mutual impedance vs spacing for parallel half-wave dipoles."""
    d_lambda = np.linspace(0.1, 2.0, 200)
    k = 2 * PI
    
    R21 = np.zeros_like(d_lambda)
    X21 = np.zeros_like(d_lambda)
    
    for i, d in enumerate(d_lambda):
        R21[i], X21[i] = mutual_impedance_parallel(d, l=0.5, k=k)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(d_lambda, R21, 'b-', lw=2, label='$R_{21}$')
    ax.plot(d_lambda, X21, 'r--', lw=2, label='$X_{21}$')
    ax.axhline(y=0, color='gray', ls=':', alpha=0.5)
    ax.set_xlabel('Spacing d/λ', fontsize=13)
    ax.set_ylabel('Mutual Impedance [Ω]', fontsize=13)
    ax.set_title('Mutual Impedance: Two Parallel Half-Wave Dipoles', fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=12)
    ax.set_xlim(0, 2)
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig4_2_mutual_impedance.png', dpi=150)
    plt.close()
    print("  fig4_2 done", flush=True)


def plot_yagi_pattern() -> None:
    """Fig 4.3: Yagi-Uda pattern for 3 and 5 elements."""
    theta = np.linspace(0.01, PI - 0.01, 360)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6),
                              subplot_kw={'projection': 'polar'})
    
    for n_elem, ax, title in [(3, axes[0], '3-Element Yagi (~7 dBi)'),
                               (5, axes[1], '5-Element Yagi (~10 dBi)')]:
        pat = yagi_pattern(theta, num_elements=n_elem)
        pat_db = 10 * np.log10(pat + 1e-15)
        pat_db = np.clip(pat_db, -30, 0)
        
        ax.plot(theta, pat_db + 30, 'b-', lw=2)
        ax.set_title(title, va='bottom')
        ax.set_theta_zero_location('N')
        ax.set_thetamin(0)
        ax.set_thetamax(180)
    
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig4_3_yagi_pattern.png', dpi=150)
    plt.close()
    print("  fig4_3 done", flush=True)


def plot_lpda_design() -> None:
    """Fig 4.4: LPDA geometry visualization."""
    design = lpda_design(tau=0.9, sigma=0.08, f_min=0.5e9, f_max=3e9)
    
    fig, ax = plt.subplots(figsize=(12, 4))
    
    lengths = design['lengths']
    pos = design['positions']
    
    for i in range(design['N']):
        # Draw each dipole element
        ax.plot([pos[i], pos[i]], [-lengths[i]/2, lengths[i]/2],
                'b-', lw=2)
        # Feed line connections
        if i < design['N'] - 1:
            ax.plot([pos[i], pos[i+1]], [0, 0], 'r-', lw=1, alpha=0.5)
    
    # Apex
    ax.plot(0, 0, 'rv', markersize=8, label='Apex')
    ax.set_xlabel('Distance from apex [m]', fontsize=13)
    ax.set_ylabel('Element length [m]', fontsize=13)
    ax.set_title(f'LPDA Design: τ={design["tau"]}, σ={design["sigma"]}, '
                 f'N={design["N"]}, G≈{design["gain_est_dBi"]:.1f} dBi',
                 fontsize=14)
    ax.set_xlim(0, max(pos) * 1.1)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig4_4_lpda_design.png', dpi=150)
    plt.close()
    print("  fig4_4 done", flush=True)


# =========================================================================
# Main
# =========================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("  Balanis Ch4: Linear Wire Antennas")
    print("=" * 60, flush=True)
    
    # 1. Pattern comparison
    print("\n[1/4] Plotting dipole pattern comparison...", flush=True)
    plot_pattern_comparison()
    
    # 2. Mutual impedance
    print("\n[2/4] Plotting mutual impedance...", flush=True)
    plot_mutual_impedance()
    
    # 3. Yagi patterns
    print("\n[3/4] Plotting Yagi-Uda patterns...", flush=True)
    plot_yagi_pattern()
    
    # 4. LPDA
    print("\n[4/4] LPDA design...", flush=True)
    plot_lpda_design()
    
    # Compute key parameters
    print("\n--- Key Parameters ---", flush=True)
    
    # λ/2 dipole directivity
    D_half = dipole_directivity(0.5)
    print(f"λ/2 dipole D₀ = {D_half:.3f} ({10*np.log10(D_half):.2f} dBi)", flush=True)
    
    # λ/2 dipole impedance
    R, X = half_wave_self_impedance()
    print(f"λ/2 dipole Z_in = {R:.1f} + j{X:.1f} Ω", flush=True)
    
    # Mutual impedance at d = 0.5λ
    R21, X21 = mutual_impedance_parallel(0.5)
    print(f"Mutual Z at d=0.5λ: Z₂₁ = {R21:.1f} + j{X21:.1f} Ω", flush=True)
    
    # LPDA design
    lpda = lpda_design(tau=0.9, sigma=0.08, f_min=0.5e9, f_max=3e9)
    print(f"LPDA: N={lpda['N']}, G≈{lpda['gain_est_dBi']:.1f} dBi, "
          f"α={lpda['alpha_deg']:.1f}°", flush=True)
    
    print("\n✅ Ch4 complete. Figures in", FIG_DIR, flush=True)
