#!/usr/bin/env python3
"""
collins_ch11_examples.py — Chapter 11: Microwave Integrated Circuits and Antennas

Demonstrates core computations from Collin "Foundations for Microwave Engineering" 2nd Ed.
Topics:
  1. Microstrip line: W/h → ε_reff, Z₀ (Hammerstad-Jensen formulas)
  2. Coplanar waveguide (CPW) characteristic impedance
  3. Microstrip patch antenna: resonant frequency, fringing correction, input impedance
  4. Rectangular patch antenna: far-field radiation pattern (E-plane)
  5. Waveguide slot array: conductance vs offset, array pattern
  6. Spiral inductor: inductance via Wheeler's formula
  7. MIM capacitor: capacitance and self-resonant frequency

Generates figures → collins/figures/ch11_*.png
Run self-test: verify_collins_ch11()
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import ellipk
import os

# ─── Physical Constants ───────────────────────────────────────────────
EPS0 = 8.854187817e-12      # F/m
MU0  = 1.256637061e-6       # H/m
C0   = 2.99792458e8         # m/s

# Output directory for figures
FIG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(FIG_DIR, exist_ok=True)

# ═══════════════════════════════════════════════════════════════════════
#  1. MICROSTRIP LINE — ε_reff and Z₀ (Hammerstad–Jensen, 1980)
# ═══════════════════════════════════════════════════════════════════════

def microstrip_eps_reff(eps_r, W_over_h):
    """
    Effective relative permittivity for a microstrip line.
    Uses the Hammerstad-Jensen formula.
    
    Parameters
    ----------
    eps_r : float
        Substrate relative permittivity.
    W_over_h : float or ndarray
        Ratio of strip width to substrate thickness.
    
    Returns
    -------
    eps_reff : float or ndarray
        Effective relative permittivity.
    """
    u = W_over_h
    # Base term used for both narrow and wide
    term = 1.0 / np.sqrt(1.0 + 12.0 / u)
    
    if np.isscalar(u):
        if u <= 1.0:
            # Narrow strip correction
            term += 0.04 * (1.0 - u)**2
    else:
        narrow = u <= 1.0
        if np.any(narrow):
            term[narrow] += 0.04 * (1.0 - u[narrow])**2
    
    eps_reff = (eps_r + 1.0) / 2.0 + (eps_r - 1.0) / 2.0 * term
    return eps_reff


def microstrip_Z0(eps_r, W_over_h):
    """
    Characteristic impedance of a microstrip line.
    
    Parameters
    ----------
    eps_r : float
        Substrate relative permittivity.
    W_over_h : float or ndarray
        Ratio of strip width to substrate thickness.
    
    Returns
    -------
    Z0 : float or ndarray
        Characteristic impedance in Ohms.
    """
    u = W_over_h
    eps_reff = microstrip_eps_reff(eps_r, u)
    sqrt_ere = np.sqrt(eps_reff)
    
    if np.isscalar(u):
        if u <= 1.0:
            Z0 = 60.0 / sqrt_ere * np.log(8.0 / u + u / 4.0)
        else:
            Z0 = (120.0 * np.pi / sqrt_ere) / (u + 1.393 + 0.667 * np.log(u + 1.444))
        return Z0
    else:
        Z0 = np.empty_like(u)
        narrow = u <= 1.0
        wide = ~narrow
        Z0[narrow] = 60.0 / sqrt_ere[narrow] * np.log(8.0 / u[narrow] + u[narrow] / 4.0)
        Z0[wide] = (120.0 * np.pi / sqrt_ere[wide]) / (u[wide] + 1.393 + 0.667 * np.log(u[wide] + 1.444))
        return Z0


def fig_microstrip_parameters():
    """Plot ε_reff and Z₀ vs W/h for several ε_r values."""
    u = np.logspace(-1, 1, 200)  # W/h from 0.1 to 10
    eps_r_vals = [2.2, 4.5, 6.15, 9.8, 12.9]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    colors = plt.cm.viridis(np.linspace(0.1, 0.9, len(eps_r_vals)))
    
    for eps_r, c in zip(eps_r_vals, colors):
        ere = microstrip_eps_reff(eps_r, u)
        Z0 = microstrip_Z0(eps_r, u)
        ax1.semilogx(u, ere, color=c, lw=2, label=f"εᵣ = {eps_r}")
        ax2.semilogx(u, Z0, color=c, lw=2, label=f"εᵣ = {eps_r}")
    
    # Reference markers: εr=10, W/h=1 → verify ~36 Ω, ε_reff ~6.75
    u_ref = np.array([1.0])
    ere_ref = microstrip_eps_reff(10.0, u_ref)[0]
    Z0_ref = microstrip_Z0(10.0, u_ref)[0]
    ax1.plot(1.0, ere_ref, 'ko', ms=8)
    ax2.plot(1.0, Z0_ref, 'ko', ms=8)
    ax1.annotate(f"ε_reff≈{ere_ref:.2f}", xy=(1, ere_ref), xytext=(1.5, ere_ref+0.3),
                 arrowprops=dict(arrowstyle="->"), fontsize=10)
    ax2.annotate(f"Z₀≈{Z0_ref:.1f} Ω", xy=(1, Z0_ref), xytext=(1.8, Z0_ref+2),
                 arrowprops=dict(arrowstyle="->"), fontsize=10)
    
    ax1.set_xlabel("W / h")
    ax1.set_ylabel("ε_reff")
    ax1.set_title("Effective Permittivity vs W/h")
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=9)
    
    ax2.set_xlabel("W / h")
    ax2.set_ylabel("Z₀ [Ω]")
    ax2.set_title("Characteristic Impedance vs W/h")
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=9)
    
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "ch11_microstrip_params.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  Saved: {path}")


# ═══════════════════════════════════════════════════════════════════════
#  2. COPLANAR WAVEGUIDE — CPW characteristic impedance
# ═══════════════════════════════════════════════════════════════════════

def cpw_Z0(eps_r, S, W, h=1e9):
    """
    Quasi-static characteristic impedance of a CPW on a substrate of
    finite thickness h. Conformal mapping based.
    
    Parameters
    ----------
    eps_r : float
        Substrate permittivity.
    S : float
        Centre conductor width (same units as W).
    W : float
        Gap width (same units as S).
    h : float
        Substrate thickness (>> S+W for thick approximation).
    
    Returns
    -------
    Z0 : float
        Characteristic impedance in Ohms.
    """
    a = S / 2.0
    b = a + W
    k = a / b
    k_prime = np.sqrt(1.0 - k**2)
    
    # Thin substrate correction factor
    if h < 1e3 * (S + 2*W):
        # Use finite-thickness formula
        t = np.tanh(np.pi * a / (2.0 * h)) / np.tanh(np.pi * b / (2.0 * h))
        k_eff = t
        K_k  = ellipk(k_eff**2)
        K_kp = ellipk(np.sqrt(1.0 - k_eff**2))
    else:
        K_k  = ellipk(k**2)
        K_kp = ellipk(k_prime**2)
    
    # Effective permittivity (thick substrate: roughly (eps_r+1)/2)
    eps_eff = 1.0 + (eps_r - 1.0) / 2.0 * ellipk(k_prime**2) / ellipk(k**2) * K_k / K_kp
    # Use simpler approx for thick substrate
    if h > 1e3 * (S + 2*W):
        eps_eff = (eps_r + 1.0) / 2.0
    
    Z0 = 30.0 * np.pi / np.sqrt(eps_eff) * K_kp / K_k
    return Z0


def fig_cpw_impedance():
    """Plot CPW Z₀ vs gap W for various ε_r and centre strip widths."""
    W_gaps = np.linspace(5, 200, 100)  # gap in μm
    S_vals = [50, 100, 150]  # centre conductor widths in μm
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    for S in S_vals:
        Z = [cpw_Z0(12.9, S, w) for w in W_gaps]  # GaAs substrate
        ax.plot(W_gaps, Z, lw=2, label=f"S = {S} μm (GaAs, εᵣ=12.9)")
    
    for S in S_vals:
        Z = [cpw_Z0(9.8, S, w) for w in W_gaps]  # Alumina
        ax.plot(W_gaps, Z, '--', lw=1.5, label=f"S = {S} μm (Al₂O₃, εᵣ=9.8)")
    
    ax.set_xlabel("Gap W [μm]")
    ax.set_ylabel("Z₀ [Ω]")
    ax.set_title("CPW Characteristic Impedance")
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8, ncol=2)
    
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "ch11_cpw_impedance.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  Saved: {path}")


# ═══════════════════════════════════════════════════════════════════════
#  3. MICROSTRIP PATCH ANTENNA
# ═══════════════════════════════════════════════════════════════════════

def patch_fringing_delta(eps_reff, W, h):
    """
    Fringing field extension ΔL (Hammerstad formula).
    
    Parameters
    ----------
    eps_reff : float
        Effective permittivity.
    W : float
        Patch width [m].
    h : float
        Substrate thickness [m].
    
    Returns
    -------
    delta_L : float
        Fringing extension [m].
    """
    num = (eps_reff + 0.3) * (W / h + 0.264)
    den = (eps_reff - 0.258) * (W / h + 0.8)
    return 0.412 * h * num / den


def patch_resonant_length(f_r, eps_r, h):
    """
    Compute patch length L for a given resonant frequency.
    
    Parameters
    ----------
    f_r : float
        Desired resonant frequency [Hz].
    eps_r : float
        Substrate relative permittivity.
    h : float
        Substrate thickness [m].
    
    Returns
    -------
    L : float
        Patch length [m].
    epsilon_reff : float
        Effective permittivity.
    delta_L : float
        Fringing extension [m].
    """
    # Initial guess: W ≈ λ0/(2f_r sqrt(eps_r)), assume W/L ≈ 1.5
    W_guess = 1.5 * C0 / (2.0 * f_r * np.sqrt(eps_r))
    
    # Use W = C0/(2*f_r) * sqrt(2/(eps_r+1)) — a common starting point
    W = C0 / (2.0 * f_r) * np.sqrt(2.0 / (eps_r + 1.0))
    
    eps_reff = microstrip_eps_reff(eps_r, W / h)
    delta_L = patch_fringing_delta(eps_reff, W, h)
    
    L = C0 / (2.0 * f_r * np.sqrt(eps_reff)) - 2.0 * delta_L
    return L, eps_reff, delta_L, W


def patch_resonant_frequency(L, eps_r, h, W=None):
    """
    Compute resonant frequency of a rectangular patch.
    """
    if W is None:
        W = 1.5 * L  # typical aspect ratio
    eps_reff = microstrip_eps_reff(eps_r, W / h)
    delta_L = patch_fringing_delta(eps_reff, W, h)
    f_r = C0 / (2.0 * (L + 2.0 * delta_L) * np.sqrt(eps_reff))
    return f_r, eps_reff, delta_L


def fig_patch_design():
    """
    Plot patch resonant length vs frequency for several substrates.
    """
    f_vals = np.linspace(1e9, 20e9, 100)
    substrates = [
        (2.2, 0.508e-3, "Duroid 5880"),
        (4.5, 1.0e-3, "FR-4-like"),
        (10.2, 0.635e-3, "Duroid 6010"),
    ]
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    for eps_r, h, label in substrates:
        L_vals = []
        for f in f_vals:
            L, _, _, _ = patch_resonant_length(f, eps_r, h)
            L_vals.append(L * 1e3)
        ax.plot(f_vals / 1e9, L_vals, lw=2, label=f"{label} (εᵣ={eps_r}, h={h*1e3:.1f}mm)")
    
    ax.set_xlabel("Frequency [GHz]")
    ax.set_ylabel("Patch Length L [mm]")
    ax.set_title("Rectangular Patch: Resonant Length vs Frequency")
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "ch11_patch_length.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  Saved: {path}")


def fig_patch_radiation():
    """
    Compute and plot the E-plane and H-plane radiation patterns
    of a rectangular patch antenna at 5.8 GHz on Duroid 5880.
    """
    f_r = 5.8e9
    eps_r = 2.2
    h = 0.508e-3
    
    L, eps_reff, delta_L, W = patch_resonant_length(f_r, eps_r, h)
    Leff = L + 2 * delta_L
    
    k0 = 2.0 * np.pi * f_r / C0
    
    theta = np.linspace(0, np.pi, 361)
    
    # E-plane (phi=0): xz-plane — pattern from two slots separated by L_eff
    # E_phi ∝ cos(k0 * L_eff/2 * sinθ)
    E_plane = np.abs(np.cos(0.5 * k0 * L * np.sin(theta)))
    E_plane = E_plane / np.max(E_plane)
    
    # H-plane (phi=pi/2): yz-plane
    # E_theta ∝ sinθ * sin(k0*W/2 * sinθ) / (k0*W/2 * sinθ)
    u = 0.5 * k0 * W * np.sin(theta)
    H_plane = np.abs(np.sin(theta) * np.sin(u) / (u + 1e-15))
    H_plane[theta == 0] = 1.0
    H_plane = H_plane / np.max(H_plane)
    
    # Convert to dB
    E_dB = 20.0 * np.log10(np.maximum(E_plane, 1e-6))
    H_dB = 20.0 * np.log10(np.maximum(H_plane, 1e-6))
    
    fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw={'projection': 'polar'}, figsize=(12, 5.5))
    
    ax1.plot(theta, E_dB, 'b-', lw=2)
    ax1.set_ylim(-40, 0)
    ax1.set_title(f"E-Plane (φ=0)\nL = {L*1e3:.2f} mm, ε_reff = {eps_reff:.3f}", va='bottom')
    
    ax2.plot(theta, H_dB, 'r-', lw=2)
    ax2.set_ylim(-40, 0)
    ax2.set_title("H-Plane (φ=90°)", va='bottom')
    
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "ch11_patch_radiation.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  Saved: {path}")
    
    return L, eps_reff, W


# ═══════════════════════════════════════════════════════════════════════
#  4. WAVEGUIDE SLOT ARRAY
# ═══════════════════════════════════════════════════════════════════════

def slot_normalized_conductance(d_over_a, a, b, f, waveguide_mode="TE10"):
    """
    Normalised shunt conductance of a longitudinal slot in the broad wall
    of a rectangular waveguide.
    
    Uses Stevenson's formula (Collin Eq. ~11.XX).
    
    G = 2.09 * (a/b) * (λg/λ0) * sin²(π d/a) * cos²(π λ0 / (2 λg))
    
    Parameters
    ----------
    d_over_a : float or ndarray
        Slot offset from centreline, normalised to waveguide width a.
    a : float
        Waveguide broad wall dimension [m].
    b : float
        Waveguide narrow wall dimension [m].
    f : float
        Operating frequency [Hz].
    
    Returns
    -------
    G : float or ndarray
        Normalised shunt conductance.
    """
    lam0 = C0 / f
    # TE10 cutoff
    lam_c = 2.0 * a
    if f <= C0 / lam_c:
        raise ValueError(f"Frequency {f/1e9:.2f} GHz below waveguide cutoff {C0/lam_c/1e9:.2f} GHz")
    
    lam_g = lam0 / np.sqrt(1.0 - (lam0 / lam_c)**2)
    
    G = 2.09 * (a / b) * (lam_g / lam0) * np.sin(np.pi * d_over_a)**2 * np.cos(np.pi * lam0 / (2.0 * lam_g))**2
    return G


def array_factor(N, d, lam, theta, beta=0.0):
    """
    Array factor for a uniform linear array.
    
    Parameters
    ----------
    N : int
        Number of elements.
    d : float
        Inter-element spacing [m].
    lam : float
        Free-space wavelength [m].
    theta : ndarray
        Observation angles [rad] (0 = broadside along array normal).
    beta : float
        Progressive phase shift [rad] (negative for forward beam steering).
    
    Returns
    -------
    AF : ndarray
        Normalised array factor magnitude (linear, max=1).
    """
    # Standard AF: AF = Σ exp[j n (kd sinθ + β)]
    # theta measured from broadside (normal to array axis)
    psi = (2.0 * np.pi * d / lam) * np.sin(theta) + beta
    # Use limiting form at psi=0
    AF = np.ones_like(theta)
    mask = np.abs(np.sin(psi / 2.0)) > 1e-12
    AF[mask] = np.abs(np.sin(N * psi[mask] / 2.0) / (N * np.sin(psi[mask] / 2.0)))
    return AF


def fig_slot_array():
    """Slot conductance vs offset, and array factor for a 10-element slot array."""
    # Waveguide: WR-90 (X-band, 8.2-12.4 GHz)
    a = 22.86e-3   # m
    b = 10.16e-3   # m
    f = 10.0e9     # Hz
    lam0 = C0 / f
    
    # Fig 1: slot conductance vs offset
    d_over_a_vals = np.linspace(0.01, 0.45, 100)
    G_vals = slot_normalized_conductance(d_over_a_vals, a, b, f)
    
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(d_over_a_vals, G_vals, 'b-', lw=2)
    ax1.set_xlabel("d / a (normalised offset)")
    ax1.set_ylabel("Normalised shunt conductance G")
    ax1.set_title(f"Longitudinal Slot in WR-90 at {f/1e9:.1f} GHz")
    ax1.grid(True, alpha=0.3)
    
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "ch11_slot_conductance.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  Saved: {path}")
    
    # Fig 2: array factor for 10-element slot array
    N = 10
    d = 0.5 * lam0  # half-wavelength spacing
    
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    theta = np.linspace(-np.pi / 2, np.pi / 2, 361)
    
    kd = 2.0 * np.pi * d / lam0
    for beta, lbl in [(0.0, "Broadside (β=0)"),
                       (-kd * np.sin(np.pi / 6), "Steered 30°"),
                       (-kd * np.sin(np.pi / 3), "Steered 60°")]:
        AF = array_factor(N, d, lam0, theta, beta)
        AF_dB = 20.0 * np.log10(np.maximum(AF, 1e-6))
        ax2.plot(theta * 180 / np.pi, AF_dB, lw=2, label=lbl)
    
    ax2.set_xlabel("θ [deg]")
    ax2.set_ylabel("|AF| [dB]")
    ax2.set_title(f"Uniform Linear Array Factor (N={N}, d=λ/2)")
    ax2.set_xlim(-90, 90)
    ax2.set_ylim(-40, 0)
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "ch11_slot_array_factor.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  Saved: {path}")


# ═══════════════════════════════════════════════════════════════════════
#  5. SPIRAL INDUCTOR — Wheeler's formula
# ═══════════════════════════════════════════════════════════════════════

def spiral_inductor_wheeler(D_out, D_in, N, shape="circular"):
    """
    Spiral inductor inductance using Wheeler's formula.
    
    Parameters
    ----------
    D_out : float
        Outer diameter [m].
    D_in : float
        Inner diameter [m].
    N : int
        Number of turns.
    shape : str
        "circular" or "square" or "octagonal".
    
    Returns
    -------
    L : float
        Inductance [H].
    """
    d_avg = (D_out + D_in) / 2.0
    rho = (D_out - D_in) / (D_out + D_in)
    
    if shape == "circular":
        # Wheeler's circular formula
        c1, c2, c3, c4 = 2.46, 0.0, 0.20, 0.40
    elif shape == "square":
        c1, c2, c3, c4 = 2.07, 0.18, 0.13, 0.42
    elif shape == "octagonal":
        c1, c2, c3, c4 = 2.23, 0.0, 0.17, 0.41
    else:
        raise ValueError(f"Unknown shape: {shape}")
    
    L_nH = c1 * MU0 * N**2 * d_avg * 1e9 / 2.0 * (np.log(c2 + c3 / rho) + c4 * rho**2)
    # MU0 * d_avg in H; convert to nH via 1e9 factor and the c1*... structure
    # Wheeler's original: L = mu0 * N^2 * d_avg / 2 * [ln(2.46/rho) + 0.2*rho^2]  (circular)
    # Return in Henries
    if shape == "circular":
        L = MU0 * N**2 * d_avg / 2.0 * (np.log(2.46 / rho) + 0.20 * rho**2)
    elif shape == "square":
        L = MU0 * N**2 * d_avg / 2.0 * (np.log(2.07 / rho) + 0.18 * rho + 0.13 * rho**2)
    else:
        L = MU0 * N**2 * d_avg / 2.0 * (np.log(2.23 / rho) + 0.17 * rho**2)
    
    return L


def fig_spiral_inductor():
    """Plot spiral inductance vs number of turns for several diameters."""
    turns = np.arange(1, 11)
    D_vals = [(200e-6, 60e-6), (300e-6, 80e-6), (400e-6, 100e-6)]
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    for D_out, D_in in D_vals:
        L_vals = [spiral_inductor_wheeler(D_out, D_in, N, "circular") * 1e9 for N in turns]
        ax.plot(turns, L_vals, 'o-', lw=2, label=f"Dₒᵤₜ={D_out*1e6:.0f}μm, Dᵢₙ={D_in*1e6:.0f}μm")
    
    ax.set_xlabel("Number of Turns N")
    ax.set_ylabel("Inductance [nH]")
    ax.set_title("Spiral Inductor: Wheeler's Formula")
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "ch11_spiral_inductor.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  Saved: {path}")


# ═══════════════════════════════════════════════════════════════════════
#  6. MIM CAPACITOR
# ═══════════════════════════════════════════════════════════════════════

def mim_capacitor(A, d, eps_r=7.0):
    """
    MIM capacitor capacitance.
    
    Parameters
    ----------
    A : float
        Plate area [m²].
    d : float
        Insulator thickness [m].
    eps_r : float
        Relative permittivity of insulator.
    
    Returns
    -------
    C : float
        Capacitance [F].
    """
    return EPS0 * eps_r * A / d


def mim_self_resonant_freq(C, L_parasitic=50e-12):
    """
    Self-resonant frequency of a MIM capacitor, limited by
    parasitic series inductance of the plate geometry.
    
    Parameters
    ----------
    C : float
        Capacitance [F].
    L_parasitic : float
        Parasitic series inductance [H] (~50 pH typical for small MMIC MIM).
    
    Returns
    -------
    f_sr : float
        Self-resonant frequency [Hz].
    """
    return 1.0 / (2.0 * np.pi * np.sqrt(L_parasitic * C))


def fig_mim_capacitor():
    """Plot MIM capacitance and SRF vs area for several dielectric thicknesses."""
    areas = np.logspace(-12, -8, 50)  # 1 μm² to 10⁴ μm²
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    d_vals = [0.1e-6, 0.2e-6, 0.5e-6]  # 0.1-0.5 μm
    for d in d_vals:
        C = [mim_capacitor(A, d) * 1e12 for A in areas]
        ax1.loglog(areas * 1e12, C, lw=2, label=f"d = {d*1e6:.1f} μm")
        
        f_sr = [mim_self_resonant_freq(mim_capacitor(A, d)) / 1e9 for A in areas]
        ax2.loglog(areas * 1e12, f_sr, lw=2, label=f"d = {d*1e6:.1f} μm")
    
    ax1.set_xlabel("Plate Area [μm²]")
    ax1.set_ylabel("Capacitance C [pF]")
    ax1.set_title("MIM Capacitor (εᵣ=7, Si₃N₄)")
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    ax2.set_xlabel("Plate Area [μm²]")
    ax2.set_ylabel("Self-Resonant Frequency [GHz]")
    ax2.set_title("MIM Capacitor SRF (L_parasitic=50pH)")
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    path = os.path.join(FIG_DIR, "ch11_mim_capacitor.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  Saved: {path}")


# ═══════════════════════════════════════════════════════════════════════
#  SELF-TEST / VERIFICATION
# ═══════════════════════════════════════════════════════════════════════

def verify_collins_ch11():
    """
    Run assertions to verify correctness of key computations.
    Based on known values from the text.
    """
    print("\n" + "=" * 60)
    print("VERIFYING key computations for Collin Ch11...")
    print("=" * 60)
    
    # --- 1. Microstrip: ε_reff for εr=10, W/h=1 → ~6.5-7.0 ---
    ere = microstrip_eps_reff(10.0, 1.0)
    print(f"  ε_reff (εr=10, W/h=1): {ere:.4f}")
    assert 6.5 <= ere <= 7.2, f"ε_reff={ere} outside expected range [6.5, 7.2]"
    
    # --- 2. Microstrip: Z0 for εr=10, W/h=1 → ~36 Ω ---
    Z0 = microstrip_Z0(10.0, 1.0)
    print(f"  Z₀ (εr=10, W/h=1): {Z0:.2f} Ω")
    assert 30 <= Z0 <= 50, f"Z0={Z0} outside expected range [30, 50]"
    
    # --- 3. Microstrip: Z0 for εr=10, W/h=0.5 → ~55-65 Ω (narrower strip → higher Z0) ---
    Z0_narrow = microstrip_Z0(10.0, 0.5)
    print(f"  Z₀ (εr=10, W/h=0.5): {Z0_narrow:.2f} Ω")
    assert Z0_narrow > Z0, f"Narrower strip should give higher Z₀: {Z0_narrow} vs {Z0}"
    assert 50 <= Z0_narrow <= 70, f"Z0={Z0_narrow} outside range [50, 70]"
    
    # --- 4. Patch antenna: 5.8 GHz on Duroid 5880 ---
    L, ere_patch, dL, W = patch_resonant_length(5.8e9, 2.2, 0.508e-3)
    print(f"  Patch @ 5.8 GHz (εr=2.2, h=0.508mm): L={L*1e3:.3f} mm, ΔL={dL*1e3:.4f} mm")
    # Verify: fringing correction ~0.2-0.5 mm for 0.508 mm substrate
    assert 0.1e-3 <= dL <= 1.0e-3, f"ΔL={dL*1e6:.1f} μm outside expected [0.1, 1.0] mm"
    # Patch length should be slightly less than λ0/(2√εr) = 299.8/(2*5.8*1.483) = 17.4 mm
    # Actually λ0/2 = 25.9 mm, divided by sqrt(εr)=1.48 → 17.4 mm
    # With fringing, L should be 17.4 - 2*ΔL ≈ 16-17 mm
    assert 15e-3 <= L <= 18e-3, f"L={L*1e3:.1f} mm outside expected [15, 18] mm"
    
    # Verify round-trip: compute f_r from L and verify it matches
    f_r_back, ere_back, dL_back = patch_resonant_frequency(L, 2.2, 0.508e-3, W)
    print(f"  Round-trip f_r: {f_r_back/1e9:.4f} GHz (target 5.8 GHz)")
    assert abs(f_r_back - 5.8e9) / 5.8e9 < 0.01, \
        f"Round-trip error: {abs(f_r_back - 5.8e9) / 5.8e9 * 100:.2f}%"
    
    # --- 5. Slot conductance: should be 0 < G < 2 for d/a < 0.45 ---
    G_slot = slot_normalized_conductance(0.2, 22.86e-3, 10.16e-3, 10e9)
    print(f"  Slot G (d/a=0.2, WR-90, 10 GHz): {G_slot:.4f}")
    assert 0 < G_slot < 5, f"Slot conductance {G_slot} outside expected range"
    
    G_slot_max = slot_normalized_conductance(0.25, 22.86e-3, 10.16e-3, 10e9)
    print(f"  Slot G (d/a=0.25, near max): {G_slot_max:.4f}")
    assert G_slot_max > G_slot, "Conductance should increase near centre"
    
    # --- 6. Array factor: broadside peak at θ=0 ---
    lam = C0 / 10e9
    theta_test = np.array([0.0, np.pi/6, np.pi/3])
    AF = array_factor(10, lam/2, lam, theta_test)
    print(f"  Array factor (10 el, λ/2 spacing, broadside): θ=0: {AF[0]:.4f}, θ=60°: {AF[2]:.4f}")
    assert AF[0] >= AF[1], "Broadside should have highest AF"
    assert abs(AF[0] - 1.0) < 1e-10, f"Peak AF should be 1.0, got {AF[0]}"
    
    # --- 7. Spiral inductor: typical values 1-10 nH ---
    L_spiral = spiral_inductor_wheeler(300e-6, 80e-6, 4, "circular")
    print(f"  Spiral inductor (D_out=300μm, D_in=80μm, N=4): {L_spiral*1e9:.3f} nH")
    assert 0.5e-9 <= L_spiral <= 15e-9, f"L={L_spiral*1e9:.2f} nH outside [0.5, 15] nH"
    
    L_spiral_sq = spiral_inductor_wheeler(300e-6, 80e-6, 4, "square")
    print(f"  Spiral inductor, square (same dims): {L_spiral_sq*1e9:.3f} nH")
    assert 0.5e-9 <= L_spiral_sq <= 15e-9
    
    # --- 8. MIM capacitor: 0.1-100 pF typical, area 10-10⁴ μm², d=0.2 μm ---
    C_mim = mim_capacitor(50e-6 * 50e-6, 0.2e-6)  # 50×50 μm, 0.2 μm Si3N4
    print(f"  MIM cap (50×50 μm, d=0.2 μm, εr=7): {C_mim*1e12:.3f} pF")
    assert 0.1e-12 <= C_mim <= 100e-12, f"C={C_mim*1e12:.2f} pF outside [0.1, 100] pF"
    
    # SRF should be in GHz for typical MMIC dimensions
    f_sr = mim_self_resonant_freq(C_mim)
    print(f"  SRF: {f_sr/1e9:.2f} GHz")
    assert 1e9 <= f_sr <= 500e9, f"SRF={f_sr/1e9:.2f} GHz unrealistic"
    
    # Capacitance density check
    C_density = C_mim / (50e-6 * 50e-6)
    print(f"  Capacitance density: {C_density*1e4:.3f} fF/μm²")
    assert 0.1e-15/1e-12 <= C_density <= 10e-15/1e-12, f"Density unrealistic"
    
    print("\n✅ ALL ASSERTIONS PASSED — Collin Ch11 verification complete.")
    return True


# ═══════════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("Collin Ch11 — Microwave ICs and Antennas")
    print("=" * 60)
    
    print("\n--- Generating Figures ---")
    fig_microstrip_parameters()
    fig_cpw_impedance()
    fig_patch_design()
    fig_patch_radiation()
    fig_slot_array()
    fig_spiral_inductor()
    fig_mim_capacitor()
    
    print("\n--- Key Numerical Results ---")
    print(f"  Microstrip (εr=10, W/h=1): ε_reff={microstrip_eps_reff(10.0, 1.0):.3f}, "
          f"Z₀={microstrip_Z0(10.0, 1.0):.1f} Ω")
    print(f"  Microstrip (εr=10, W/h=0.5): Z₀={microstrip_Z0(10.0, 0.5):.1f} Ω")
    print(f"  CPW on GaAs (S=50μm, W=30μm): Z₀={cpw_Z0(12.9, 50e-6, 30e-6):.1f} Ω")
    
    L_patch, ere_p, dL_p, W_p = patch_resonant_length(5.8e9, 2.2, 0.508e-3)
    print(f"  Patch 5.8 GHz (εr=2.2): L={L_patch*1e3:.2f} mm, "
          f"W={W_p*1e3:.2f} mm, ε_reff={ere_p:.4f}")
    
    L_sp = spiral_inductor_wheeler(300e-6, 80e-6, 5, "circular")
    print(f"  Spiral inductor (D_out=300μm, N=5): L={L_sp*1e9:.2f} nH")
    
    C_mim = mim_capacitor(100e-6 * 100e-6, 0.2e-6)
    f_sr = mim_self_resonant_freq(C_mim)
    print(f"  MIM cap (100×100μm, d=0.2μm): C={C_mim*1e12:.2f} pF, SRF={f_sr/1e9:.1f} GHz")
    
    # Verification
    verify_collins_ch11()
    
    print("\n" + "=" * 60)
    print("DONE — All figures and verification complete.")
    print(f"Figures saved to: {FIG_DIR}")
    print("=" * 60)
