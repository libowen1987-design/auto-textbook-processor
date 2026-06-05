"""
Balanis Ch6 — Arrays: Linear, Planar, Circular

Key features:
  - Uniform Linear Array (ULA) analysis
  - Beam scanning, HPBW, directivity
  - Amplitude tapering (Dolph-Chebyshev, Taylor, cosine, etc.)
  - Planar array pattern (separable)
  - Circular array
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from typing import Optional

PI = np.pi
ETA_0 = 376.7303
C0 = 3e8
FIG_DIR = 'figures/ch06'
os.makedirs(FIG_DIR, exist_ok=True)


# =========================================================================
# Array Factor — Uniform Linear Array
# =========================================================================

def ula_af(theta: np.ndarray, N: int, d: float = 0.5,
           beta: float = 0.0, k: float = 2*PI) -> np.ndarray:
    """Uniform Linear Array factor.
    
    Parameters
    ----------
    theta : ndarray
        Observation angles from array axis (rad)
    N : int
        Number of elements
    d : float
        Element spacing in wavelengths
    beta : float
        Progressive phase shift (rad)
    k : float
        Wavenumber
    
    Returns
    -------
    AF_n : ndarray
        Normalized array factor (linear)
    """
    psi = k * d * np.cos(theta) + beta
    psi_safe = psi.copy()
    # Avoid division by zero at psi = 0
    mask = np.abs(np.sin(psi_safe / 2)) > 1e-10
    AF = np.ones_like(psi, dtype=float)
    AF[mask] = np.abs(np.sin(N * psi_safe[mask] / 2) /
                      (N * np.sin(psi_safe[mask] / 2)))
    return AF


def ula_directivity(N: int, d: float = 0.5, beta: float = 0.0) -> float:
    """Compute ULA directivity via numerical integration."""
    theta = np.linspace(0.001, PI - 0.001, 10000)
    AF = ula_af(theta, N, d, beta)
    # U_max = 1 (normalized AF)
    U_int = AF**2 * np.sin(theta)
    P_rad = 2 * PI * np.trapezoid(U_int, theta)
    D = 4 * PI / P_rad if P_rad > 0 else 1.0
    return D


def ula_hpbw(N: int, d: float = 0.5, beta: float = 0.0) -> float:
    """Compute ULA HPBW in degrees (broadside)."""
    theta = np.linspace(0, PI, 20001)
    AF = ula_af(theta, N, d, beta)
    AF_pow = AF**2
    half_power = 0.5
    # Find -3dB points by scanning from the peak (pi/2 for broadside)
    peak_idx = np.argmax(AF_pow)
    theta_deg = np.degrees(theta)
    
    # Find left -3dB point
    left_3dB = 0.0
    for i in range(peak_idx, 0, -1):
        if AF_pow[i] <= half_power:
            left_3dB = np.interp(half_power, 
                                  [AF_pow[i], AF_pow[i+1]],
                                  [theta_deg[i], theta_deg[i+1]])
            break
    
    # Find right -3dB point
    right_3dB = 180.0
    for i in range(peak_idx, len(theta)-1):
        if AF_pow[i] <= half_power:
            right_3dB = np.interp(half_power,
                                   [AF_pow[i], AF_pow[i-1]],
                                   [theta_deg[i], theta_deg[i-1]])
            break
    
    return right_3dB - left_3dB


# =========================================================================
# Amplitude Tapering
# =========================================================================

def chebyshev_poly(m: int, x: np.ndarray) -> np.ndarray:
    """Chebyshev polynomial T_m(x)."""
    if m == 0:
        return np.ones_like(x)
    if m == 1:
        return x.copy()
    return 2 * x * chebyshev_poly(m - 1, x) - chebyshev_poly(m - 2, x)


def dolph_chebyshev_weights(N: int, sidelobe_dB: float) -> np.ndarray:
    """Compute Dolph-Chebyshev current weights.
    
    Parameters
    ----------
    N : int
        Number of elements (even or odd)
    sidelobe_dB : float
        Desired sidelobe level in dB (e.g., -30)
    
    Returns
    -------
    w : ndarray
        Current weights
    """
    R = 10**(-sidelobe_dB / 20)  # voltage ratio
    x0 = np.cosh(np.arccosh(R) / (N - 1))
    
    # Compute weights via IDFT of Chebyshev polynomial
    # For N elements, sample T_{N-1}(x0*cos(psi/2))
    M = 512
    # Must sample symmetric about psi=0 for correct IFT (ψ ∈ [-π, π])
    psi = np.linspace(-PI, PI, M)
    x = x0 * np.cos(psi / 2)
    with np.errstate(invalid='ignore', divide='ignore'):
        AF_desired = np.where(np.abs(x) <= 1,
                              np.cos((N-1) * np.arccos(x)),
                              np.cosh((N-1) * np.arccosh(np.abs(x))))
    AF_desired = np.nan_to_num(AF_desired)
    AF_desired /= np.max(AF_desired)  # normalize
    
    # IDFT to get weights
    w = np.fft.fftshift(np.fft.ifft(np.fft.ifftshift(AF_desired)))
    # Take N central elements
    start = (M - N) // 2
    w = np.real(w[start:start+N])
    # Ensure symmetry
    w = (w + w[::-1]) / 2
    w /= np.max(w)
    return w


def tapered_af(theta: np.ndarray, w: np.ndarray, d: float = 0.5,
               beta: float = 0.0, k: float = 2*PI) -> np.ndarray:
    """Array factor for arbitrary weights."""
    N = len(w)
    n = np.arange(N) - (N - 1) / 2
    psi = k * d * np.cos(theta) + beta
    AF = np.zeros(len(theta), dtype=complex)
    for i, w_i in enumerate(w):
        AF += w_i * np.exp(1j * n[i] * psi)
    return np.abs(AF) / np.max(np.abs(AF))


# =========================================================================
# Planar Array
# =========================================================================

def planar_af(theta: np.ndarray, phi: np.ndarray,
              Nx: int, Ny: int, dx: float = 0.5, dy: float = 0.5,
              theta0: float = 0.0, phi0: float = 0.0) -> np.ndarray:
    """Planar rectangular array factor.
    
    Returns AF(phi, theta) matrix.
    """
    Phi, Theta = np.meshgrid(phi, theta, indexing='ij')
    
    # Steering phase
    beta_x = -2*PI * dx * np.sin(theta0) * np.cos(phi0)
    beta_y = -2*PI * dy * np.sin(theta0) * np.sin(phi0)
    
    # AF_x
    nx = np.arange(Nx) - (Nx - 1) / 2
    psi_x = 2*PI * dx * np.sin(Theta) * np.cos(Phi) + beta_x
    AF_x = np.zeros_like(Theta, dtype=complex)
    for n in nx:
        AF_x += np.exp(1j * n * psi_x)
    
    # AF_y
    ny = np.arange(Ny) - (Ny - 1) / 2
    psi_y = 2*PI * dy * np.sin(Theta) * np.sin(Phi) + beta_y
    AF_y = np.zeros_like(Theta, dtype=complex)
    for m in ny:
        AF_y += np.exp(1j * m * psi_y)
    
    AF = np.abs(AF_x * AF_y)
    return AF / np.max(AF)


# =========================================================================
# Circular Array
# =========================================================================

def circular_af(theta: np.ndarray, phi: np.ndarray,
                N: int, a: float = 1.0) -> np.ndarray:
    """Circular array factor.
    
    N elements equally spaced on a circle of radius a (in wavelengths).
    """
    phi_n = 2 * PI * np.arange(N) / N
    Phi, Theta = np.meshgrid(phi, theta, indexing='ij')
    
    AF = np.zeros_like(Theta, dtype=complex)
    for phin in phi_n:
        AF += np.exp(1j * 2*PI * a * np.sin(Theta) * np.cos(Phi - phin))
    
    return np.abs(AF) / np.max(np.abs(AF))


# =========================================================================
# Plotting
# =========================================================================

def plot_ula_patterns():
    """Fig 6.1: ULA patterns for various N and d."""
    theta = np.linspace(0.001, PI-0.001, 2000)
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 9))
    
    # Row 1: Broadside, varying N
    Ns = [5, 10, 20]
    for idx, (N, ax) in enumerate(zip(Ns, axes[0])):
        AF = ula_af(theta, N, d=0.5)
        ax.plot(np.degrees(theta), 20*np.log10(AF+1e-10), lw=1.5)
        ax.set_title(f'ULA Broadside, N={N}', fontsize=12)
        ax.set_xlim(0, 180); ax.set_ylim(-40, 3)
        ax.set_xlabel('θ [deg]'); ax.set_ylabel('AF [dB]')
        ax.grid(True, alpha=0.3)
        D = ula_directivity(N)
        ax.text(0.95, 0.95, f'D={D:.1f} ({10*np.log10(D):.1f}dBi)',
                transform=ax.transAxes, va='top', ha='right', fontsize=10)
    
    # Row 2: Scanning
    scans = [0, 30, 60]
    for idx, (scan, ax) in enumerate(zip(scans, axes[1])):
        beta_scan = -2*PI * 0.5 * np.cos(np.radians(scan))
        # For broadside (scan=0): beta=0
        if scan == 0:
            beta_scan = 0.0
        # For endfire (scan=90):
        elif scan == 60:
            beta_scan = -2*PI * 0.5 * np.cos(np.radians(90))  
        AF = ula_af(theta, N=20, d=0.5, beta=-2*PI*0.5*np.cos(np.radians(scan)))
        ax.plot(np.degrees(theta), 20*np.log10(AF+1e-10), lw=1.5)
        ax.set_title(f'Beam Scanning θ₀={scan}°', fontsize=12)
        ax.set_xlim(0, 180); ax.set_ylim(-40, 3)
        ax.set_xlabel('θ [deg]'); ax.set_ylabel('AF [dB]')
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig6_1_ula_patterns.png', dpi=150)
    plt.close()
    print("  fig6_1 done", flush=True)


def plot_tapered_patterns():
    """Fig 6.2: Comparison of tapered amplitude distributions."""
    theta = np.linspace(0.001, PI-0.001, 2000)
    N = 20
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Compare tapers
    tapers = {
        'Uniform': np.ones(N),
        'Cosine': np.cos(np.pi * (np.arange(N) - (N-1)/2) / N),
        'Hamming': 0.54 + 0.46 * np.cos(2*np.pi * (np.arange(N) - (N-1)/2) / N),
        'Chebyshev -30dB': dolph_chebyshev_weights(N, -30),
    }
    
    for name, w in tapers.items():
        AF = tapered_af(theta, w)
        axes[0].plot(np.degrees(theta), 20*np.log10(AF+1e-10), lw=1.5, label=name)
    
    axes[0].set_xlim(0, 180); axes[0].set_ylim(-50, 3)
    axes[0].set_xlabel('θ [deg]'); axes[0].set_ylabel('AF [dB]')
    axes[0].set_title('Taper Comparison (N=20)', fontsize=13)
    axes[0].grid(True, alpha=0.3); axes[0].legend(fontsize=9)
    
    # Chebyshev SLL sweep
    slls = [-20, -30, -40]
    for sll in slls:
        w = dolph_chebyshev_weights(N, sll)
        AF = tapered_af(theta, w)
        axes[1].plot(np.degrees(theta), 20*np.log10(AF+1e-10), lw=1.5,
                     label=f'Cheb SLL={sll}dB')
    
    axes[1].set_xlim(0, 180); axes[1].set_ylim(-60, 3)
    axes[1].set_xlabel('θ [deg]'); axes[1].set_ylabel('AF [dB]')
    axes[1].set_title('Dolph-Chebyshev (N=20)', fontsize=13)
    axes[1].grid(True, alpha=0.3); axes[1].legend(fontsize=9)
    
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig6_2_tapered.png', dpi=150)
    plt.close()
    print("  fig6_2 done", flush=True)


def plot_planar_pattern():
    """Fig 6.3: Planar array patterns — u-v map + pattern cuts."""
    theta = np.linspace(0.01, PI-0.01, 500)
    phi = np.linspace(0, 2*PI, 360)
    
    AF = planar_af(theta, phi, Nx=8, Ny=8, dx=0.5, dy=0.5)
    Phi_g, Theta_g = np.meshgrid(phi, theta, indexing='ij')
    
    u = np.sin(Theta_g) * np.cos(Phi_g)
    v = np.sin(Theta_g) * np.sin(Phi_g)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # u-v map
    im = axes[0].pcolormesh(u, v, 20*np.log10(AF+5e-10),
                             cmap='viridis', shading='auto')
    axes[0].set_xlabel('u = sinθ cosφ', fontsize=12)
    axes[0].set_ylabel('v = sinθ sinφ', fontsize=12)
    axes[0].set_title('Planar 8×8 Array — u-v Pattern [dB]', fontsize=13)
    axes[0].set_aspect('equal')
    axes[0].set_xlim(-1, 1); axes[0].set_ylim(-1, 1)
    plt.colorbar(im, ax=axes[0], shrink=0.8)
    
    # Pattern cuts
    for pname, pval in [('φ=0° (E-plane)', 0), ('φ=45°', PI/4), ('φ=90° (H-plane)', PI/2)]:
        Phi_cut = Theta_g[:, 0] * 0 + pval
        AF_cut = planar_af(theta, np.array([pval]), Nx=8, Ny=8).ravel()
        axes[1].plot(np.degrees(theta), 20*np.log10(AF_cut+1e-10),
                     lw=1.5, label=pname)
    axes[1].set_xlabel('θ [deg]', fontsize=12)
    axes[1].set_ylabel('AF [dB]', fontsize=12)
    axes[1].set_title('Pattern Cuts', fontsize=13)
    axes[1].set_xlim(0, 90); axes[1].set_ylim(-40, 3)
    axes[1].grid(True, alpha=0.3); axes[1].legend(fontsize=9)
    
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig6_3_planar.png', dpi=150)
    plt.close()
    print("  fig6_3 done", flush=True)


def plot_directivity_vs_nd():
    """Fig 6.4: Directivity vs array size."""
    Nd = np.linspace(1, 20, 100)
    D_bs = 2 * Nd  # broadside
    D_ef = 4 * Nd  # endfire (Hansen-Woodyard)
    
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.plot(Nd, 10*np.log10(D_bs), 'b-', lw=2, label='Broadside: D≈2Nd/λ')
    ax.plot(Nd, 10*np.log10(D_ef), 'r--', lw=2, label='Endfire: D≈4Nd/λ')
    ax.set_xlabel('Nd/λ (Array Length)', fontsize=13)
    ax.set_ylabel('Directivity [dBi]', fontsize=13)
    ax.set_title('Directivity vs Array Length', fontsize=14)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=12)
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig6_4_directivity.png', dpi=150)
    plt.close()
    print("  fig6_4 done", flush=True)


# =========================================================================
# Main
# =========================================================================

if __name__ == '__main__':
    print("=" * 60, flush=True)
    print("  Balanis Ch6: Arrays", flush=True)
    print("=" * 60, flush=True)
    
    print("[1/4] ULA patterns...", flush=True)
    plot_ula_patterns()
    
    print("[2/4] Tapered patterns...", flush=True)
    plot_tapered_patterns()
    
    print("[3/4] Planar array...", flush=True)
    plot_planar_pattern()
    
    print("[4/4] Directivity vs size...", flush=True)
    plot_directivity_vs_nd()
    
    # Compute key values
    print("\n--- Key Results ---", flush=True)
    N = 10
    D = ula_directivity(N, d=0.5)
    print(f"ULA N={N}, d=0.5λ: D={D:.2f} ({10*np.log10(D):.1f} dBi)", flush=True)
    HP = ula_hpbw(N)
    print(f"ULA N={N}: HPBW ≈ {HP:.2f}° (expected ~{0.886/(N*0.5):.1f} rad = {np.degrees(0.886/(N*0.5)):.1f}°)", flush=True)
    
    w = dolph_chebyshev_weights(20, -30)
    print(f"Dolph-Chebyshev N=20, SLL=-30dB: weights OK ({len(w)} elements)", flush=True)
    
    print(f"\n✅ Ch6 done. Figures in {FIG_DIR}/", flush=True)
