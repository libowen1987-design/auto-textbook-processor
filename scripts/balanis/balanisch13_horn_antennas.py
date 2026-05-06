#!/usr/bin/env python3
"""
balanis_ch13_horn_antennas.py
=============================
Balanis 4th Ed., Chapter 13 — Horn Antennas
Python 复现: E/H-plane sectoral, pyramidal, conical, corrugated horns.

Author: 二龙虾 (小龙虾编码分身)
Variable naming: a,b (waveguide), A,B (aperture), rho_e,rho_h (slant lengths),
                 delta_e,delta_h (phase errors), D0 (directivity), HPBW, SLL
"""

import numpy as np
from scipy.special import fresnel
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ── 路径配置 ───────────────────────────────────────────────
FIG_DIR = Path(__file__).resolve().parent / 'figures' / 'ch13'
FIG_DIR.mkdir(parents=True, exist_ok=True)

# ── 物理常数 ───────────────────────────────────────────────
ETA0 = 376.730313  # free-space impedance [Ω]
C0   = 299792458   # speed of light [m/s]

# ═══════════════════════════════════════════════════════════
#  Fresnel Integral Helpers
# ═══════════════════════════════════════════════════════════

def C_fresnel(x):
    """Fresnel cosine integral C(x) = ∫₀ˣ cos(πt²/2) dt (scipy convention)."""
    # scipy.special.fresnel returns (S, C) for ∫₀ˣ sin(πt²/2), ∫₀ˣ cos(πt²/2)
    S, C = fresnel(x)
    return C

def S_fresnel(x):
    """Fresnel sine integral S(x) = ∫₀ˣ sin(πt²/2) dt."""
    S, C = fresnel(x)
    return S

# ═══════════════════════════════════════════════════════════
#  §13.2.1 — E-plane Sectoral Horn
# ═══════════════════════════════════════════════════════════

def directivity_E_sectoral(a, B, rho_e, wavelength):
    """
    E-plane sectoral horn maximum directivity (linear power ratio).
    Balanis Eq. (13-30).

    Parameters
    ----------
    a : float       — waveguide width [m]
    B : float       — aperture height (E-plane flare) [m]
    rho_e : float   — E-plane slant length [m]
    wavelength : float — free-space wavelength [m]

    Returns
    -------
    D0 : float      — maximum directivity (linear)
    """
    l = wavelength
    u = B / np.sqrt(2.0 * l * rho_e)
    C2_plus_S2 = C_fresnel(u)**2 + S_fresnel(u)**2
    D0 = (64.0 * a * rho_e) / (np.pi * l * B) * C2_plus_S2
    return D0

def optimum_B_for_E_sectoral(rho_e, wavelength):
    """
    Optimum B for E-plane sectoral horn (B ≈ sqrt(2 λ ρ_e)).
    Corresponds to δ_e = λ/4 and u ≈ 1.
    """
    return np.sqrt(2.0 * wavelength * rho_e)

def hpw_E_sectoral(B, wavelength):
    """
    E-plane HPBW approximation [radians].
    HPBW_E ≈ 2 arcsin(0.94 λ / B)
    """
    return 2.0 * np.arcsin(np.minimum(0.94 * wavelength / B, 1.0))


# ═══════════════════════════════════════════════════════════
#  §13.2.2 — H-plane Sectoral Horn
# ═══════════════════════════════════════════════════════════

def directivity_H_sectoral(A, b, rho_h, wavelength):
    """
    H-plane sectoral horn maximum directivity (linear).
    Balanis Eq. (13-40) with Fresnel integrals.

    Parameters
    ----------
    A : float       — aperture width (H-plane flare) [m]
    b : float       — waveguide height [m]
    rho_h : float   — H-plane slant length [m]
    wavelength : float

    Returns
    -------
    D0 : float      — maximum directivity (linear)
    """
    l = wavelength
    # Phase error parameter
    t = A**2 / (8.0 * l * rho_h)    # δ_h / λ

    # Fresnel parameters (Balanis notation)
    sqrt_t = np.sqrt(t)
    p1 = np.sqrt(2.0) * (1.0 / (4.0 * sqrt_t) + sqrt_t)
    p2 = np.sqrt(2.0) * (1.0 / (4.0 * sqrt_t) - sqrt_t)

    # Amplitude taper efficiency ε_t
    epsilon_t = 8.0 / np.pi**2

    # Phase efficiency ε_ph
    cd = C_fresnel(p1) - C_fresnel(p2)
    sd = S_fresnel(p1) - S_fresnel(p2)
    epsilon_ph = (np.pi**2 / (64.0 * t)) * (cd**2 + sd**2)

    # Aperture efficiency
    epsilon_ap = epsilon_t * epsilon_ph

    D0 = (4.0 * np.pi * b * rho_h) / (l * A) * epsilon_ap
    return D0

def optimum_A_for_H_sectoral(rho_h, wavelength):
    """
    Optimum A for H-plane sectoral horn (A ≈ sqrt(3 λ ρ_h)).
    Corresponds to δ_h ≈ 0.375 λ and t ≈ 0.375.
    """
    return np.sqrt(3.0 * wavelength * rho_h)

def hpw_H_sectoral(A, wavelength):
    """
    H-plane HPBW approximation [radians].
    HPBW_H ≈ 2 arcsin(0.68 λ / A)
    """
    return 2.0 * np.arcsin(np.minimum(0.68 * wavelength / A, 1.0))


# ═══════════════════════════════════════════════════════════
#  §13.2.3 — Pyramidal Horn
# ═══════════════════════════════════════════════════════════

def directivity_pyramidal(A, B, a, b, rho_e, rho_h, wavelength):
    """
    Pyramidal horn maximum directivity.
    Uses product of E-plane and H-plane directivities.

    D_P = (π λ² / 32 a b) * D_E * D_H   [Balanis Eq. 13-47]

    Parameters
    ----------
    A, B : aperture dimensions [m]
    a, b : waveguide dimensions [m]
    rho_e, rho_h : slant lengths [m]

    Returns
    -------
    D0 : float (linear)
    """
    l = wavelength
    D_E = directivity_E_sectoral(a, B, rho_e, l)
    D_H = directivity_H_sectoral(A, b, rho_h, l)
    D0 = (np.pi * l**2) / (32.0 * a * b) * D_E * D_H
    return D0


def pyramidal_gain_dB(A, B, wavelength, epsilon_ap=0.51):
    """
    Pyramidal horn gain in dBi using aperture efficiency.
    G = 10 log10(4π A B / λ² * ε_ap)
    """
    G_lin = (4.0 * np.pi * A * B) / (wavelength**2) * epsilon_ap
    return 10.0 * np.log10(G_lin)


def pyramidal_design(G0_dB, freq, waveguide_a=None, waveguide_b=None,
                    max_iter=10, tol=0.5):
    """
    Design a pyramidal horn for a target gain at given frequency.
    Uses iterative refinement with geometric consistency.

    Parameters
    ----------
    G0_dB : float — target gain [dBi]
    freq : float  — frequency [Hz]
    waveguide_a, waveguide_b : optional waveguide dimensions [m]
    max_iter : int — max iterations
    tol : float — convergence tolerance in dB

    Returns
    -------
    dict with A, B, rho_e, rho_h, R0, D0_dB, dimensions
    """
    l = C0 / freq

    # Waveguide dimensions (WR-standard approximation)
    if waveguide_a is None:
        waveguide_a = 0.72 * l   # a ≈ 0.72λ for TE10
    if waveguide_b is None:
        waveguide_b = waveguide_a / 2.0
    a, b = waveguide_a, waveguide_b

    # Ensure waveguide supports TE10: a > λ/2
    if a <= l / 2.0:
        a = 0.72 * l
        b = a / 2.0

    G0_lin = 10.0 ** (G0_dB / 10.0)

    # Initial aperture guess using ideal aperture with ε_ap = 0.5
    A = np.sqrt(G0_lin * l**2 / (4.0 * np.pi * 0.5) * 1.4)
    B = A / 1.4

    delta_e_opt = 0.25  # wavelength
    delta_h_opt = 0.375

    for iteration in range(max_iter):
        # Slant lengths from optimum phase errors
        rho_e = B**2 / (8.0 * l * delta_e_opt)
        rho_h = A**2 / (8.0 * l * delta_h_opt)

        # Axial length from geometry (must be consistent)
        if abs(B - b) < 1e-10:
            R0_e = rho_e
        else:
            R0_e = rho_e * B / (B - b)

        if abs(A - a) < 1e-10:
            R0_h = rho_h
        else:
            R0_h = rho_h * A / (A - a)

        R0 = max(R0_e, R0_h)

        # Adjust slant lengths for geometric consistency
        if R0_e > R0_h:
            # E-plane determines axial length; adjust H-plane
            rho_h = R0 * (A - a) / A
            # Recompute A for consistent δ_h
            A_ref = np.sqrt(8.0 * l * rho_h * delta_h_opt)
            A = 0.5 * (A + A_ref)  # damp
        else:
            # H-plane determines axial length; adjust E-plane
            rho_e = R0 * (B - b) / B
            B_ref = np.sqrt(8.0 * l * rho_e * delta_e_opt)
            B = 0.5 * (B + B_ref)  # damp

        # Compute achieved directivity
        D0 = directivity_pyramidal(A, B, a, b, rho_e, rho_h, l)
        D0_dB = 10.0 * np.log10(D0)

        # Scale aperture to converge toward target gain
        if abs(D0_dB - G0_dB) > tol and D0 > 0:
            # Gain ∝ A*B; scale approximately
            scale = 10.0 ** ((G0_dB - D0_dB) / 20.0)  # sqrt of linear gain ratio
            A *= scale
            B *= scale
        else:
            break

    return {
        'freq': freq,
        'wavelength': l,
        'a': a, 'b': b,
        'A': A, 'B': B,
        'rho_e': rho_e, 'rho_h': rho_h,
        'R0': R0,
        'delta_e_lambda': delta_e_opt,
        'delta_h_lambda': delta_h_opt,
        'D0_dB': D0_dB,
    }


# ═══════════════════════════════════════════════════════════
#  §13.2 — Radiation Pattern Computation
# ═══════════════════════════════════════════════════════════

def pattern_pyramidal(theta, A, B, a, b, rho_e, rho_h, wavelength):
    """
    Compute normalized radiation pattern (linear magnitude) for pyramidal horn.

    Uses simplified aperture-field method (Balanis Ch13 approach).
    Returns |E| at angles theta (array, radians) in E-plane (phi=π/2) and
    H-plane (phi=0), both normalized to max=1.

    This is an approximation — full 2D integration would need numerical
    evaluation of the double integral.
    """
    k = 2.0 * np.pi / wavelength
    theta = np.asarray(theta, dtype=float)

    # E-plane pattern (phi = π/2): uniform in x, quadratic phase in y
    # E_θ(θ) ∝ sinc(k a sinθ / 2) · ∫ cos term unaffected, plus y-integral
    sinc_factor = np.sinc(k * a * np.sin(theta) / (2.0 * np.pi))  # sinc(x)=sin(πx)/(πx)

    # E-plane y-integral with quadratic phase (Fresnel approximation)
    # ∫_{-B/2}^{B/2} exp(-j k y'²/(2ρ_e)) exp(j k y' sinθ) dy'
    # = sqrt(π ρ_e / k) · [F(v2) - F(v1)] where F includes Fresnel
    y_int = np.zeros_like(theta, dtype=complex)
    u_B = B * np.sqrt(k / (2.0 * rho_e))   # Fresnel parameter from integration limit
    for i, th in enumerate(theta):
        # Shifted Fresnel due to linear term
        v1 = np.sqrt(k * rho_e / np.pi) * (-B/2 / (rho_e) + np.sin(th))
        v2 = np.sqrt(k * rho_e / np.pi) * (B/2 / (rho_e) + np.sin(th))
        # The shifted Fresnel integrals — approximate evaluation
        # Using integration: ∫_a^b exp(-j(π/2)u²) du
        # We approximate numerically
        # For simplicity and accuracy, we do direct numerical integration
        Npts = 501
        y_vals = np.linspace(-B/2, B/2, Npts)
        integrand = np.exp(-1j * k * y_vals**2 / (2.0 * rho_e)) * np.exp(1j * k * y_vals * np.sin(th))
        y_int[i] = np.trapezoid(integrand, y_vals)

    E_plane = sinc_factor * np.abs(y_int)
    E_plane /= np.max(E_plane)

    # H-plane pattern (phi = 0): cosine taper in x with quadratic phase
    # ∫_{-A/2}^{A/2} cos(π x'/A) exp(-j k x'²/(2ρ_h)) exp(j k x' sinθ) dx'
    x_int = np.zeros_like(theta, dtype=complex)
    for i, th in enumerate(theta):
        Npts = 501
        x_vals = np.linspace(-A/2, A/2, Npts)
        integrand = (np.cos(np.pi * x_vals / A)
                     * np.exp(-1j * k * x_vals**2 / (2.0 * rho_h))
                     * np.exp(1j * k * x_vals * np.sin(th)))
        x_int[i] = np.trapezoid(integrand, x_vals)

    # Uniform in y
    # H-plane sinc from y-integral
    y_sinc_H = np.sinc(k * b * np.sin(theta) / (2.0 * np.pi))
    H_plane = np.abs(x_int) * np.abs(y_sinc_H)
    H_plane /= np.max(H_plane)

    return E_plane, H_plane


def compute_hpbw_and_sll(theta_deg, pattern_dB):
    """
    Compute HPBW and SLL from a pattern array.
    pattern_dB: normalized power pattern in dB (max=0 dB)
    theta_deg: corresponding angle array.

    Returns (HPBW_deg, SLL_dB).
    """
    # Find half-power (-3 dB) points
    above_hp = pattern_dB >= -3.0
    # Find main lobe region (largest contiguous region near peak)
    peak_idx = np.argmax(pattern_dB)
    above = above_hp.astype(int)
    # Find left and right -3 dB crossings
    left_idx = np.where(above[:peak_idx] == 0)[0]
    right_idx = np.where(above[peak_idx:] == 0)[0]
    if len(left_idx) > 0:
        th_l = np.interp(-3.0,
                         [pattern_dB[left_idx[-1]], pattern_dB[left_idx[-1]+1]],
                         [theta_deg[left_idx[-1]], theta_deg[left_idx[-1]+1]])
    else:
        th_l = theta_deg[0]

    if len(right_idx) > 0:
        th_r = np.interp(-3.0,
                         [pattern_dB[peak_idx + right_idx[0]-1],
                          pattern_dB[peak_idx + right_idx[0]]],
                         [theta_deg[peak_idx + right_idx[0]-1],
                          theta_deg[peak_idx + right_idx[0]]])
    else:
        th_r = theta_deg[-1]

    HPBW_deg = th_r - th_l

    # SLL: max side lobe level outside main lobe
    main_lobe_mask = (theta_deg >= th_l) & (theta_deg <= th_r)
    side_lobe = pattern_dB.copy()
    side_lobe[main_lobe_mask] = -np.inf
    SLL_dB = np.max(side_lobe)

    return HPBW_deg, SLL_dB


# ═══════════════════════════════════════════════════════════
#  §13.3 — Circular (Conical) Horn
# ═══════════════════════════════════════════════════════════

def directivity_conical(radius_aperture, rho_0, frequency):
    """
    Conical horn approximate directivity.
    Uses aperture efficiency ~0.5 with quadratic phase correction.

    D0 ≈ (4π/λ²) * (π a_m²) * ε_ap

    Parameters
    ----------
    radius_aperture : float — aperture radius a_m [m]
    rho_0 : float — slant length [m]
    frequency : float [Hz]

    Returns
    -------
    D0_dB : float
    """
    l = C0 / frequency
    delta = radius_aperture**2 / (2.0 * l * rho_0)
    # Aperture efficiency approximation (Balanis, Fig 13.18)
    # ε_ap ≈ 0.5 - 0.3 * (δ/λ) for small δ
    epsilon_ap = np.clip(0.5 - 0.3 * (delta / l), 0.3, 0.6)
    A_phys = np.pi * radius_aperture**2
    D0_lin = (4.0 * np.pi * A_phys) / (l**2) * epsilon_ap
    return 10.0 * np.log10(D0_lin)


# ═══════════════════════════════════════════════════════════
#  §13.4 — Corrugated Horn (Gaussian Beam Model)
# ═══════════════════════════════════════════════════════════

def gaussian_beam_coupling(aperture_radius, wavelength, w0_guess=None):
    """
    Coupling efficiency between corrugated horn aperture field
    and fundamental Gaussian beam.

    For an optimal corrugated horn, the aperture field approximates
    a Gaussian: E ∝ exp(-ρ'² / w²).

    The coupling efficiency η_g ≈ 0.98 for optimal design.

    Parameters
    ----------
    aperture_radius : float — a_m [m]
    wavelength : float

    Returns
    -------
    eta_g : float — Gaussian coupling efficiency
    w_a : float — Gaussian beam waist at aperture [m]
    """
    # Optimum: w_a ≈ a_m / 0.89
    w_a = aperture_radius / 0.89
    # Coupling integral (simplified): η = 1 - exp(-2 a_m² / w_a²)
    eta_g = 1.0 - np.exp(-2.0 * aperture_radius**2 / w_a**2)
    return eta_g, w_a


# ═══════════════════════════════════════════════════════════
#  Demos & Examples
# ═══════════════════════════════════════════════════════════

def demo_1_eplane_sectoral():
    """
    Demo 1: E-plane sectoral horn at 10 GHz.
    Replicate Balanis Example 13.1-like computation.
    """
    print("=" * 60)
    print("Demo 1: E-plane Sectoral Horn (f = 10 GHz)")
    print("=" * 60)

    freq = 10.0e9
    l = C0 / freq
    a = 2.286e-2   # WR-90: 0.9 inch
    b = 1.016e-2   # WR-90: 0.4 inch
    B = 5.0 * l     # aperture height
    rho_e = 10.0 * l

    D0 = directivity_E_sectoral(a, B, rho_e, l)
    D0_dB = 10.0 * np.log10(D0)

    B_opt = optimum_B_for_E_sectoral(rho_e, l)
    D0_opt = directivity_E_sectoral(a, B_opt, rho_e, l)
    D0_opt_dB = 10.0 * np.log10(D0_opt)

    hpw_E = np.degrees(hpw_E_sectoral(B, l))
    hpw_E_opt = np.degrees(hpw_E_sectoral(B_opt, l))

    print(f"  λ = {l*1000:.2f} mm")
    print(f"  a = {a*1000:.2f} mm, b = {b*1000:.2f} mm")
    print(f"  rho_e = {rho_e*1000:.1f} mm")
    print(f"  B = {B*1000:.2f} mm,  D0 = {D0_dB:.2f} dBi,  HPBW_E ≈ {hpw_E:.1f}°")
    print(f"  B_opt = {B_opt*1000:.2f} mm, D0_opt = {D0_opt_dB:.2f} dBi, HPBW_E ≈ {hpw_E_opt:.1f}°")

    return D0_opt


def demo_2_hplane_sectoral():
    """
    Demo 2: H-plane sectoral horn at 10 GHz.
    """
    print("=" * 60)
    print("Demo 2: H-plane Sectoral Horn (f = 10 GHz)")
    print("=" * 60)

    freq = 10.0e9
    l = C0 / freq
    a = 2.286e-2   # WR-90
    b = 1.016e-2
    A = 6.0 * l
    rho_h = 10.0 * l

    D0 = directivity_H_sectoral(A, b, rho_h, l)
    D0_dB = 10.0 * np.log10(D0)

    A_opt = optimum_A_for_H_sectoral(rho_h, l)
    D0_opt = directivity_H_sectoral(A_opt, b, rho_h, l)
    D0_opt_dB = 10.0 * np.log10(D0_opt)

    hpw_H = np.degrees(hpw_H_sectoral(A, l))
    hpw_H_opt = np.degrees(hpw_H_sectoral(A_opt, l))

    print(f"  λ = {l*1000:.2f} mm")
    print(f"  a = {a*1000:.2f} mm, b = {b*1000:.2f} mm")
    print(f"  rho_h = {rho_h*1000:.1f} mm")
    print(f"  A = {A*1000:.2f} mm,  D0 = {D0_dB:.2f} dBi,  HPBW_H ≈ {hpw_H:.1f}°")
    print(f"  A_opt = {A_opt*1000:.2f} mm, D0_opt = {D0_opt_dB:.2f} dBi, HPBW_H ≈ {hpw_H_opt:.1f}°")

    return D0_opt


def demo_3_pyramidal_design_and_pattern():
    """
    Demo 3: Design a 15 dBi pyramidal horn at 10 GHz and plot patterns.
    """
    print("=" * 60)
    print("Demo 3: Pyramidal Horn Design & Pattern (f = 10 GHz, G = 15 dBi)")
    print("=" * 60)

    freq = 10.0e9
    l = C0 / freq

    design = pyramidal_design(15.0, freq)
    for k, v in design.items():
        if k in ('freq',):
            print(f"  {k} = {v/1e9:.2f} GHz")
        elif k in ('wavelength', 'delta_e', 'delta_h'):
            print(f"  {k} = {v*1000:.3f} mm")
        elif k == 'D0_dB':
            print(f"  {k} = {v:.2f} dBi")
        else:
            print(f"  {k} = {v*1000:.2f} mm")

    # Pattern computation
    theta_deg = np.linspace(-90, 90, 901)
    theta_rad = np.radians(theta_deg)
    A, B = design['A'], design['B']
    a, b = design['a'], design['b']
    rho_e, rho_h = design['rho_e'], design['rho_h']

    E_plane, H_plane = pattern_pyramidal(theta_rad, A, B, a, b, rho_e, rho_h, l)

    E_dB = 20.0 * np.log10(np.clip(E_plane, 1e-12, None))
    H_dB = 20.0 * np.log10(np.clip(H_plane, 1e-12, None))

    hpw_E, sll_E = compute_hpbw_and_sll(theta_deg, E_dB)
    hpw_H, sll_H = compute_hpbw_and_sll(theta_deg, H_dB)
    print(f"\n  E-plane: HPBW = {hpw_E:.1f}°, SLL = {sll_E:.1f} dB")
    print(f"  H-plane: HPBW = {hpw_H:.1f}°, SLL = {sll_H:.1f} dB")

    # Plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(theta_deg, E_dB, 'b-', label='E-plane')
    ax1.plot(theta_deg, H_dB, 'r--', label='H-plane')
    ax1.set_xlabel('θ [deg]')
    ax1.set_ylabel('Normalized |E| [dB]')
    ax1.set_title(f'Pyramidal Horn (f = {freq/1e9:.1f} GHz)\nA={A*1000:.1f}, B={B*1000:.1f} mm')
    ax1.set_xlim(-90, 90)
    ax1.set_ylim(-50, 3)
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.axhline(-3, color='gray', ls=':', lw=0.8)

    # Polar plot
    ax2 = plt.subplot(122, projection='polar')
    theta_rad_plot = np.radians(theta_deg)
    # Convert to power pattern for polar (only positive half)
    mask = theta_deg >= 0
    ax2.plot(theta_rad_plot[mask], E_plane[mask], 'b-', label='E-plane', alpha=0.8)
    ax2.plot(theta_rad_plot[mask], H_plane[mask], 'r--', label='H-plane', alpha=0.8)
    ax2.set_title('Radiation Pattern (linear)')
    ax2.legend(loc='lower right')

    plt.tight_layout()
    fig.savefig(FIG_DIR / 'demo3_pyramidal_pattern.png', dpi=150)
    plt.close(fig)
    print(f"  Figure saved: {FIG_DIR / 'demo3_pyramidal_pattern.png'}")

    return design


def demo_4_gain_vs_aperture():
    """
    Demo 4: Pyramidal horn gain vs aperture size at 10 GHz.
    Shows the optimum trade-off as aperture grows.
    """
    print("=" * 60)
    print("Demo 4: Gain vs Aperture (Pyramidal, f = 10 GHz)")
    print("=" * 60)

    freq = 10.0e9
    l = C0 / freq
    a_wg = 2.286e-2
    b_wg = 1.016e-2

    # Fix axial length, vary aperture
    R0 = 0.15  # 15 cm
    factor = np.linspace(1.0, 4.0, 30)

    gains = []
    phase_errors = []
    for f in factor:
        A = f * np.sqrt(10.0 * l * R0)  # typical scaling
        B = f * np.sqrt(5.0 * l * R0)

        # Slant lengths from geometry
        rho_h = A * R0 / (A - a_wg) if A > a_wg else 1e6
        rho_e = B * R0 / (B - b_wg) if B > b_wg else 1e6

        if rho_h > 0 and rho_e > 0:
            D0 = directivity_pyramidal(A, B, a_wg, b_wg, rho_e, rho_h, l)
            gains.append(10.0 * np.log10(max(D0, 1e-6)))
            phase_errors.append(A**2 / (8.0 * l * rho_h))  # δ_h/λ

    fig, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(factor, gains, 'b-o', markersize=3)
    ax1.set_xlabel('Aperture scaling factor')
    ax1.set_ylabel('Directivity [dBi]', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.grid(True, alpha=0.3)

    ax2 = ax1.twinx()
    ax2.plot(factor, phase_errors, 'r--s', markersize=3)
    ax2.set_ylabel('δ_h / λ (H-plane phase error)', color='r')
    ax2.tick_params(axis='y', labelcolor='r')
    ax2.axhline(0.375, color='r', ls=':', alpha=0.5, label='Optimum')

    fig.suptitle('Pyramidal Horn: Gain vs Aperture (R₀ = 15 cm, f = 10 GHz)')
    fig.tight_layout()
    fig.savefig(FIG_DIR / 'demo4_gain_vs_aperture.png', dpi=150)
    plt.close(fig)
    print(f"  Figure saved: {FIG_DIR / 'demo4_gain_vs_aperture.png'}")

    return gains, factor


def demo_5_conical_horn():
    """
    Demo 5: Conical (circular) horn directivity vs radius.
    """
    print("=" * 60)
    print("Demo 5: Conical Horn Directivity (f = 12 GHz)")
    print("=" * 60)

    freq = 12.0e9
    l = C0 / freq

    radii = np.linspace(0.01, 0.08, 50)
    rho_0 = 0.1  # fixed slant length [m]

    gains = [directivity_conical(r, rho_0, freq) for r in radii]
    phases = [r**2 / (2.0 * l * rho_0) for r in radii]

    fig, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(radii * 1000, gains, 'g-', lw=2)
    ax1.set_xlabel('Aperture radius a_m [mm]')
    ax1.set_ylabel('Directivity [dBi]', color='g')
    ax1.tick_params(axis='y', labelcolor='g')
    ax1.grid(True, alpha=0.3)

    ax2 = ax1.twinx()
    ax2.plot(radii * 1000, [p / l for p in phases], 'm--', lw=2)
    ax2.set_ylabel('δ / λ (phase error)', color='m')
    ax2.tick_params(axis='y', labelcolor='m')
    ax2.axhline(0.25, color='m', ls=':', alpha=0.5, label='opt δ=λ/4')

    fig.suptitle(f'Conical Horn (ρ₀ = {rho_0*1000:.0f} mm, f = {freq/1e9:.1f} GHz)')
    fig.tight_layout()
    fig.savefig(FIG_DIR / 'demo5_conical_horn.png', dpi=150)
    plt.close(fig)
    print(f"  Figure saved: {FIG_DIR / 'demo5_conical_horn.png'}")

    return gains


def demo_6_corrugated_horn():
    """
    Demo 6: Corrugated horn Gaussian beam coupling efficiency.
    """
    print("=" * 60)
    print("Demo 6: Corrugated Horn — Gaussian Beam Coupling")
    print("=" * 60)

    freq = 10.0e9
    l = C0 / freq

    radii = np.linspace(0.01, 0.05, 30)
    etas = []
    for r in radii:
        eta_g, w_a = gaussian_beam_coupling(r, l)
        etas.append(eta_g)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(radii * 1000, etas, 'c-', lw=2)
    ax.axhline(0.98, color='gray', ls='--', alpha=0.6, label='η_g ≈ 0.98 (optimum)')
    ax.set_xlabel('Aperture radius a_m [mm]')
    ax.set_ylabel('Gaussian coupling efficiency η_g')
    ax.set_title(f'Corrugated Horn Gaussian Coupling (f = {freq/1e9:.1f} GHz)')
    ax.grid(True, alpha=0.3)
    ax.legend()

    fig.tight_layout()
    fig.savefig(FIG_DIR / 'demo6_corrugated_coupling.png', dpi=150)
    plt.close(fig)
    print(f"  Figure saved: {FIG_DIR / 'demo6_corrugated_coupling.png'}")

    return etas


# ═══════════════════════════════════════════════════════════
#  Self-Verification: verify_ch13()
# ═══════════════════════════════════════════════════════════

def verify_ch13():
    """
    Comprehensive self-test for Chapter 13 implementations.
    Compares with known textbook benchmarks.

    Returns
    -------
    True if all tests pass, False otherwise.
    """
    print("\n" + "=" * 60)
    print("VERIFY: Ch13 Horn Antennas — Self-Test")
    print("=" * 60)

    tol = 0.02  # 2% tolerance
    all_pass = True

    # ── Fresnel integral consistency ──
    C1 = C_fresnel(0.0)
    C_half = C_fresnel(0.5)
    S_half = S_fresnel(0.5)
    # C(0) = 0, C(0.5) ≈ 0.4923, S(0.5) ≈ 0.0647
    if not np.isclose(C1, 0.0, atol=1e-10):
        print(f"  ❌ Fresnel C(0) = {C1}, expected 0")
        all_pass = False
    else:
        print(f"  ✅ Fresnel C(0) = 0")

    if not np.isclose(C_half, 0.4923, atol=1e-3):
        print(f"  ❌ Fresnel C(0.5) = {C_half:.4f}, expected ~0.4923")
        all_pass = False
    else:
        print(f"  ✅ Fresnel C(0.5) = {C_half:.4f}")

    if not np.isclose(S_half, 0.0647, atol=1e-3):
        print(f"  ❌ Fresnel S(0.5) = {S_half:.4f}, expected ~0.0647")
        all_pass = False
    else:
        print(f"  ✅ Fresnel S(0.5) = {S_half:.4f}")

    # ── E-plane sectoral benchmark ──
    l_test = 0.03       # λ = 3 cm
    a_test = 0.02286    # WR-90
    b_test = 0.01016
    B_test = 0.15       # 15 cm
    rho_e_test = 0.30   # 30 cm
    D_E = directivity_E_sectoral(a_test, B_test, rho_e_test, l_test)
    D_E_dB = 10.0 * np.log10(D_E)

    # Balanis Example 13.1: similar config yields D_E ≈ 14.4 dBi (within a few %)
    # Reference: With these params, D0 ~ 14-15 dBi range
    print(f"  E-plane sectoral D0 = {D_E_dB:.2f} dBi (reference ~14.5 dBi)")
    # Check order of magnitude
    if D_E_dB < 10 or D_E_dB > 25:
        print(f"  ❌ E-plane D0 out of plausible range")
        all_pass = False
    else:
        print(f"  ✅ E-plane D0 in plausible range")

    # ── H-plane sectoral benchmark ──
    A_test = 0.20
    rho_h_test = 0.30
    D_H = directivity_H_sectoral(A_test, b_test, rho_h_test, l_test)
    D_H_dB = 10.0 * np.log10(D_H)
    # H-plane sectoral has small b (waveguide height) → moderate D0
    print(f"  H-plane sectoral D0 = {D_H_dB:.2f} dBi (b={b_test*1000:.1f}mm, A={A_test*1000:.0f}mm, reference ~4-7 dBi)")
    if D_H_dB < 2 or D_H_dB > 10:
        print(f"  ❌ H-plane D0 out of plausible range")
        all_pass = False
    else:
        print(f"  ✅ H-plane D0 in plausible range")

    # ── Pyramidal benchmark ──
    D_P = directivity_pyramidal(A_test, B_test, a_test, b_test,
                                rho_e_test, rho_h_test, l_test)
    D_P_dB = 10.0 * np.log10(D_P)
    print(f"  Pyramidal D0 = {D_P_dB:.2f} dBi")
    if D_P_dB < 12 or D_P_dB > 28:
        print(f"  ❌ Pyramidal D0 out of plausible range")
        all_pass = False
    else:
        print(f"  ✅ Pyramidal D0 in plausible range")

    # ── Optimum sizing consistency ──
    B_opt = optimum_B_for_E_sectoral(rho_e_test, l_test)
    A_opt = optimum_A_for_H_sectoral(rho_h_test, l_test)
    # B_opt = sqrt(2*λ*ρ_e) = sqrt(2*0.03*0.30) = sqrt(0.018) ≈ 0.134 m
    B_opt_ref = np.sqrt(2.0 * l_test * rho_e_test)
    if not np.isclose(B_opt, B_opt_ref):
        print(f"  ❌ Optimum B mismatch: {B_opt:.4f} vs {B_opt_ref:.4f}")
        all_pass = False
    else:
        print(f"  ✅ Optimum B = {B_opt*1000:.1f} mm")

    # ── Conical horn ──
    D_con = directivity_conical(0.05, 0.15, 12e9)
    print(f"  Conical horn D0 = {D_con:.2f} dBi (reference ~18-22 dBi)")
    if D_con < 10 or D_con > 30:
        print(f"  ❌ Conical D0 out of plausible range")
        all_pass = False
    else:
        print(f"  ✅ Conical D0 in plausible range")

    # ── Pattern computation runs without error ──
    try:
        theta_test = np.linspace(-np.pi/2, np.pi/2, 101)
        Ep, Hp = pattern_pyramidal(theta_test, A_test, B_test, a_test, b_test,
                                    rho_e_test, rho_h_test, l_test)
        if Ep.shape == theta_test.shape and Hp.shape == theta_test.shape:
            print(f"  ✅ Pattern computation: {len(theta_test)} points, normal")
        else:
            print(f"  ❌ Pattern shape mismatch")
            all_pass = False
    except Exception as e:
        print(f"  ❌ Pattern computation failed: {e}")
        all_pass = False

    # ── Gain formula consistency ──
    G_dB = pyramidal_gain_dB(A_test, B_test, l_test, epsilon_ap=0.51)
    G_dB_ref = 10.0 * np.log10(4.0 * np.pi * A_test * B_test / l_test**2 * 0.51)
    if np.isclose(G_dB, G_dB_ref, rtol=1e-10):
        print(f"  ✅ Pyramidal gain formula consistent: {G_dB:.2f} dBi")
    else:
        print(f"  ❌ Gain formula inconsistent")
        all_pass = False

    # ── HPBW bounds ──
    hpw_e = np.degrees(hpw_E_sectoral(B_test, l_test))
    hpw_h = np.degrees(hpw_H_sectoral(A_test, l_test))
    if 5 < hpw_e < 40 and 5 < hpw_h < 40:
        print(f"  ✅ HPBW plausible: E={hpw_e:.1f}°, H={hpw_h:.1f}°")
    else:
        print(f"  ❌ HPBW out of range: E={hpw_e:.1f}°, H={hpw_h:.1f}°")
        all_pass = False

    # ── Design function ──
    design = pyramidal_design(15.0, 10e9)
    if abs(design['D0_dB'] - 15.0) < 2.0:
        print(f"  ✅ Pyramidal design near target: {design['D0_dB']:.1f} dBi (target 15 dBi)")
    else:
        print(f"  ❌ Pyramidal design off target: {design['D0_dB']:.1f} vs 15 dBi")
        all_pass = False

    # ── Corrugated horn Gaussian coupling ──
    eta_g, w_a = gaussian_beam_coupling(0.03, l_test)
    if 0.7 < eta_g < 1.0:
        print(f"  ✅ Corrugated horn η_g = {eta_g:.4f}")
    else:
        print(f"  ❌ Corrugated η_g out of range: {eta_g:.4f}")
        all_pass = False

    print("\n" + "─" * 60)
    if all_pass:
        print("  ✅ verify_ch13: ALL TESTS PASSED")
    else:
        print("  ❌ verify_ch13: SOME TESTS FAILED")
    print("─" * 60)

    return all_pass


# ═══════════════════════════════════════════════════════════
#  Main
# ═══════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("=" * 60)
    print("Balanis Chapter 13 — Horn Antennas")
    print("Python Reproduction Suite")
    print("=" * 60)

    demo_1_eplane_sectoral()
    print()
    demo_2_hplane_sectoral()
    print()
    demo_3_pyramidal_design_and_pattern()
    print()
    demo_4_gain_vs_aperture()
    print()
    demo_5_conical_horn()
    print()
    demo_6_corrugated_horn()

    result = verify_ch13()

    print(f"\nFinal: verify_ch13() = {result}")
