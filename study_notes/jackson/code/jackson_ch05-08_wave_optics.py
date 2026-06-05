r"""
jackson_ch05-08_wave_optics.py
================================
Computational examples from Jackson, Introduction to Electrodynamics, 4th Ed.
Chapters 5–8: Electromagnetic Waves and Optics

Coverage
--------
- plane_wave()             : Plane wave E = E₀·e^(i(k·r - ωt))
- fresnel_reflection()     : Fresnel reflection coefficients (s/p polarisation)
- waveguide_modes()        : Parallel-plate waveguide TE/TM mode fields
- skin_depth()             : Conductor skin depth δ = √(2/ωμσ)

Physical constants from scipy.constants:
    c, ε₀, μ₀, pi, sqrt

Authors: Computational Electromagnetics Lab
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from scipy.constants import c as c0, epsilon_0 as eps0, mu_0 as mu0, pi


# ---------------------------------------------------------------------------
# 1. PLANE WAVE PROPAGATION
# ---------------------------------------------------------------------------

def plane_wave(E0, f, k_dir, r_obs, t, pol='x'):
    r"""
    Compute the electric and magnetic fields of a monochromatic plane wave.

    Parameters
    ----------
    E0 : float
        Amplitude of the electric field in V/m.
    f : float
        Frequency in Hz.
    k_dir : array_like, shape (3,)
        Direction of propagation (unit vector).  The wave vector is
        \mathbf{k} = k·k_dir where k = ω/c = 2πf/c.
    r_obs : array_like, shape (3,)
        Observation position [x, y, z] in metres.
    t : float
        Time in seconds.
    pol : str
        Polarisation: 'x', 'y', or 'xy' (circular).

    Returns
    -------
    E : ndarray, shape (3,)
        Electric field vector at (r_obs, t) in V/m.
    H : ndarray, shape (3,)
        Magnetic field vector at (r_obs, t) in A/m.

    Formula
    -------
    \mathbf{E} = E₀ · \mathbf{ε̂} · e^{i(\mathbf{k}·\mathbf{r} - ωt)}
    \mathbf{H} = (1/η) · \mathbf{Ĥ} × \mathbf{E}   (η = √(μ/ε))

    where η ≈ 377 Ω for free space.
    """
    omega = 2.0 * pi * f
    k_mag = omega / c0
    k_vec = k_mag * np.asarray(k_dir) / np.linalg.norm(k_dir)

    r = np.asarray(r_obs)
    phase = np.dot(k_vec, r) - omega * t
    eta   = np.sqrt(mu0 / eps0)          # ~377 Ω free-space impedance

    # Polarisation vector
    if pol == 'x':
        epsilon_hat = np.array([1.0, 0.0, 0.0])
    elif pol == 'y':
        epsilon_hat = np.array([0.0, 1.0, 0.0])
    elif pol == 'xy':
        epsilon_hat = (np.array([1.0, 1.0j, 0.0]) / sqrt(2)).real
    else:
        raise ValueError("pol must be 'x', 'y', or 'xy'")

    E = E0 * epsilon_hat * np.exp(1j * phase)
    # H from E: H = k̂ × E / η
    k_hat = k_vec / k_mag
    H = np.cross(k_hat, E) / eta

    return E.real, H.real


def demo_plane_wave():
    """Visualise a plane wave propagating in the +z direction."""
    f   = 3e9      # 3 GHz
    E0  = 100.0    # V/m
    z   = np.linspace(0, 0.1, 501)   # 10 cm
    t   = 0.0

    Ez = np.zeros_like(z)
    for i, zi in enumerate(z):
        E, _ = plane_wave(E0, f, [0, 0, 1], [0, 0, zi], t, pol='x')
        Ez[i] = E[0]

    plt.figure(figsize=(9, 4))
    plt.plot(z * 100, Ez, 'b-', lw=1.5)
    plt.axhline(0, color='k', lw=0.5)
    plt.axvline(0, color='k', lw=0.5)
    plt.xlabel(r"$z$ (cm)")
    plt.ylabel(r"$E_x$ (V/m)")
    plt.title(r"Plane wave at $f=3\,$GHz, $t=0$, propagating in $+\hat{z}$")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("plane_wave.png", dpi=150)
    plt.show()
    print("[demo] Plane wave plot saved as plane_wave.png")


# ---------------------------------------------------------------------------
# 2. FRESNEL REFLECTION COEFFICIENTS
# ---------------------------------------------------------------------------

def fresnel_reflection(n1, n2, theta_i, pol='s'):
    r"""
    Compute the Fresnel reflection coefficients for a planar dielectric
    interface.

    Parameters
    ----------
    n1 : float
        Refractive index of incident medium.
    n2 : float
        Refractive index of transmitted medium.
    theta_i : float
        Angle of incidence in radians.
    pol : str
        's' for TE (perpendicular) polarisation,
        'p' for TM (parallel) polarisation.

    Returns
    -------
    r : complex
        Reflection coefficient (amplitude).
    t : complex
        Transmission coefficient (amplitude).
    R : float
        Power reflectance |r|².

    Formula (Jackson Eq. 4.19 / 4.20)
    -------
    r_s = (n1·cosθ_i - n2·cosθ_t) / (n1·cosθ_i + n2·cosθ_t)
    r_p = (n2·cosθ_i - n1·cosθ_t) / (n2·cosθ_i + n1·cosθ_t)

    where cosθ_t is found from Snell's law:
    n1·sinθ_i = n2·sinθ_t  →  cosθ_t = √(1 - (n1/n2·sinθ_i)²)

    Example
    -------
    >>> r, t, R = fresnel_reflection(1.0, 1.5, np.deg2rad(30), 'p')
    >>> print(f"R = {R:.4f}")
    """
    sin_i = np.sin(theta_i)
    # Snell's law: n1 sinθi = n2 sinθt
    sin_t = (n1 / n2) * sin_i
    if abs(sin_t) > 1.0:
        # Total internal reflection
        cos_t = 0.0
    else:
        cos_t = np.sqrt(1.0 - sin_t**2)

    if pol == 's':
        r = (n1 * np.cos(theta_i) - n2 * cos_t) / (n1 * np.cos(theta_i) + n2 * cos_t)
        t = 2.0 * n1 * np.cos(theta_i) / (n1 * np.cos(theta_i) + n2 * cos_t)
    elif pol == 'p':
        r = (n2 * np.cos(theta_i) - n1 * cos_t) / (n2 * np.cos(theta_i) + n1 * cos_t)
        t = 2.0 * n1 * np.cos(theta_i) / (n2 * np.cos(theta_i) + n1 * cos_t)
    else:
        raise ValueError("pol must be 's' or 'p'")

    R = abs(r)**2
    return r, t, R


def demo_fresnel_reflection():
    """Plot reflectance vs incidence angle for air→glass (n=1.5)."""
    n1, n2 = 1.0, 1.5
    theta_i = np.linspace(0, pi/2 - 0.001, 500)

    Rs = np.array([fresnel_reflection(n1, n2, th, 's')[2] for th in theta_i])
    Rp = np.array([fresnel_reflection(n1, n2, th, 'p')[2] for th in theta_i])

    plt.figure(figsize=(9, 5))
    plt.plot(np.rad2deg(theta_i), Rs, 'b-', lw=2, label=r'$R_s$ (TE)')
    plt.plot(np.rad2deg(theta_i), Rp, 'r-', lw=2, label=r'$R_p$ (TM)')
    plt.axvline(np.rad2deg(np.arctan(n2/n1)), color='gray', ls='--',
                label=r"Brewster angle $\theta_B = \arctan(n_2/n_1)$")
    plt.xlabel(r"Angle of incidence $\theta_i$ (deg)")
    plt.ylabel(r"Reflectance $R$")
    plt.title(r"Fresnel Reflectance: Air ($n_1=1$) → Glass ($n_2=1.5$)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("fresnel_reflection.png", dpi=150)
    plt.show()
    print("[demo] Fresnel reflectance plot saved as fresnel_reflection.png")


# ---------------------------------------------------------------------------
# 3. PARALLEL-PLATE WAVEGUIDE MODES
# ---------------------------------------------------------------------------

def waveguide_modes(a, b, f, mode_type='TE', n_mode=1, num_points=200):
    r"""
    Compute the field distribution of TE/TM modes in a parallel-plate
    waveguide.

    The waveguide has plates at y = 0 and y = b, width a in x-direction,
    and infinite extent in z.  Fields vary as e^{i(k_z·z - ωt)}.

    Parameters
    ----------
    a : float
        Plate separation (height) in metres  — the gap between plates.
    b : float
        Width of plates in x-direction (used only for plotting range).
    f : float
        Operating frequency in Hz.
    mode_type : str
        'TE' or 'TM'.
    n_mode : int
        Mode index (m for TE_mn / TM_mn, here n=0).
    num_points : int
        Number of spatial points for field plots.

    Returns
    -------
    y_grid : ndarray
        y-coordinates across the gap.
    E_y    : ndarray
        Transverse E-field (V/m) across the gap.
    H_x    : ndarray
        Transverse H-field (A/m) across the gap.

    Formulas (Jackson Ch. 8)
    -------
    TE modes:
      E_y = E₀ · sin(mπy/a) · e^{i(k_z·z - ωt)}
      H_x = -(ωμ/mπ) · E₀ · cos(mπy/a) · e^{i(k_z·z - ωt)}
      k_z = √(k² - (mπ/a)²)

    TM modes:
      E_y = E₀ · cos(mπy/a) · e^{i(k_z·z - ωt)}
      H_x = (iωε/mπ) · E₀ · sin(mπy/a) · e^{i(k_z·z - ωt)}

    Example
    -------
    >>> y, Ey, Hx = waveguide_modes(a=0.01, b=0.05, f=15e9, mode_type='TE', n_mode=1)
    """
    m     = n_mode
    omega = 2.0 * pi * f
    k     = omega * np.sqrt(eps0 * mu0)

    # Cut-off wave number
    kc = m * pi / a

    # Phase constant
    if k > kc:
        beta = np.sqrt(k**2 - kc**2)
    else:
        beta = 0.0
        print(f"[WARNING] Mode TE_{m} is below cut-off at f={f*1e-9:.1f} GHz")

    # Normalised transverse coordinate
    y_grid = np.linspace(0, a, num_points)

    if mode_type == 'TE':
        # E_y field
        E_y = np.sin(m * pi * y_grid / a)
        # H_x field (up to a constant factor)
        H_x = - (omega * mu0 / (m * pi / a)) * np.cos(m * pi * y_grid / a)
    elif mode_type == 'TM':
        E_y = np.cos(m * pi * y_grid / a) if m > 0 else np.ones_like(y_grid)
        H_x =   (omega * eps0 / (m * pi / a)) * np.sin(m * pi * y_grid / a)
    else:
        raise ValueError("mode_type must be 'TE' or 'TM'")

    return y_grid, E_y, H_x


def demo_waveguide_modes():
    a   = 0.01    # 10 mm plate gap
    f   = 15e9    # 15 GHz
    b   = 5 * a  # plate width

    y_TE, Ey_TE, Hx_TE = waveguide_modes(a, b, f, mode_type='TE', n_mode=1)
    y_TM, Ey_TM, Hx_TM = waveguide_modes(a, b, f, mode_type='TM', n_mode=1)

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    axes[0, 0].plot(Ey_TE, y_TE * 1000, 'b-', lw=2)
    axes[0, 0].set_xlabel(r"$E_y$ (normalised)")
    axes[0, 0].set_ylabel(r"$y$ (mm)")
    axes[0, 0].set_title(r"TE$_1$ mode: $E_y$ field")
    axes[0, 0].grid(True, alpha=0.3)

    axes[0, 1].plot(Hx_TE, y_TE * 1000, 'r-', lw=2)
    axes[0, 1].set_xlabel(r"$H_x$ (normalised)")
    axes[0, 1].set_ylabel(r"$y$ (mm)")
    axes[0, 1].set_title(r"TE$_1$ mode: $H_x$ field")
    axes[0, 1].grid(True, alpha=0.3)

    axes[1, 0].plot(Ey_TM, y_TM * 1000, 'b-', lw=2)
    axes[1, 0].set_xlabel(r"$E_y$ (normalised)")
    axes[1, 0].set_ylabel(r"$y$ (mm)")
    axes[1, 0].set_title(r"TM$_1$ mode: $E_y$ field")
    axes[1, 0].grid(True, alpha=0.3)

    axes[1, 1].plot(Hx_TM, y_TM * 1000, 'r-', lw=2)
    axes[1, 1].set_xlabel(r"$H_x$ (normalised)")
    axes[1, 1].set_ylabel(r"$y$ (mm)")
    axes[1, 1].set_title(r"TM$_1$ mode: $H_x$ field")
    axes[1, 1].grid(True, alpha=0.3)

    fig.suptitle(rf"Parallel-plate waveguide, $a=10\,$mm, $f={f*1e-9:.0f}\,$GHz",
                 fontsize=13)
    plt.tight_layout()
    plt.savefig("waveguide_modes.png", dpi=150)
    plt.show()
    print("[demo] Waveguide modes plot saved as waveguide_modes.png")


# ---------------------------------------------------------------------------
# 4. SKIN DEPTH
# ---------------------------------------------------------------------------

def skin_depth(sigma, f, mu=mu0):
    r"""
    Compute the electromagnetic skin depth in a good conductor.

    Parameters
    ----------
    sigma : float
        Electrical conductivity in S/m.
    f : float
        Frequency in Hz.
    mu : float
        Magnetic permeability in H/m (default: μ₀ for non-magnetic conductors).

    Returns
    -------
    delta : float
        Skin depth in metres.

    Formula (Jackson Eq. 5.60)
    -------
    δ = √( 2 / ω·μ·σ ) = √( 1 / π·f·μ·σ )

    Example
    -------
    >>> d = skin_depth(sigma=5.8e7, f=1e9)   # Copper at 1 GHz
    >>> print(f"δ = {d*1e6:.2f} μm")
    """
    omega = 2.0 * pi * f
    delta = np.sqrt(2.0 / (omega * mu * sigma))
    return delta


def demo_skin_depth():
    """Plot skin depth vs frequency for copper and aluminium."""
    sigma_Cu = 5.8e7    # S/m
    sigma_Al = 3.5e7    # S/m

    f_vals = np.logspace(6, 12, 300)   # 1 MHz → 1 THz

    delta_Cu = np.array([skin_depth(sigma_Cu, f) for f in f_vals])
    delta_Al = np.array([skin_depth(sigma_Al, f) for f in f_vals])

    plt.figure(figsize=(9, 5))
    plt.loglog(f_vals, delta_Cu * 1e6, 'b-', lw=2, label='Copper (σ=5.8×10⁷ S/m)')
    plt.loglog(f_vals, delta_Al * 1e6, 'r-', lw=2, label='Aluminium (σ=3.5×10⁷ S/m)')
    plt.xlabel(r"Frequency $f$ (Hz)")
    plt.ylabel(r"Skin depth $\delta$ (μm)")
    plt.title("Skin Depth vs Frequency in Good Conductors")
    plt.legend()
    plt.grid(True, which='both', alpha=0.3)
    plt.tight_layout()
    plt.savefig("skin_depth.png", dpi=150)
    plt.show()
    print("[demo] Skin depth plot saved as skin_depth.png")

    # Numerical verification at 1 GHz for copper
    d_1GHz = skin_depth(sigma_Cu, 1e9)
    print(f"\n[skin_depth] Copper at 1 GHz: δ = {d_1GHz*1e6:.3f} μm  (literature ≈ 2.1 μm)")


# ---------------------------------------------------------------------------
# MAIN / VALIDATION
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("Jackson Ch 05-08: Wave Optics and Electromagnetics")
    print("=" * 60)

    # 1. Plane wave
    E, H = plane_wave(100.0, 3e9, [0, 0, 1], [0, 0, 0], 0.0, pol='x')
    print(f"\n[plane_wave] E = {E},  H = {H}")
    print(f"[plane_wave] |E|/|H| = {np.linalg.norm(E)/np.linalg.norm(H):.1f} Ω  (η₀≈377 Ω)")

    # 2. Fresnel reflection
    r_s, t_s, R_s = fresnel_reflection(1.0, 1.5, np.deg2rad(30), 's')
    r_p, t_p, R_p = fresnel_reflection(1.0, 1.5, np.deg2rad(30), 'p')
    print(f"\n[fresnel] Air→Glass at 30°:")
    print(f"  R_s (TE) = {R_s:.4f},  R_p (TM) = {R_p:.4f}")
    # Check energy conservation: T = n2·cosθt / (n1·cosθi) · |t|²  (skip for brevity)
    print(f"  r_s = {r_s:.4f},  t_s = {t_s:.4f}")

    # 3. Waveguide modes
    y, Ey, Hx = waveguide_modes(a=0.01, b=0.05, f=15e9, mode_type='TE', n_mode=1)
    print(f"\n[waveguide] TE1 mode, a=10mm, f=15GHz:")
    print(f"  E_y range: [{Ey.min():.2f}, {Ey.max():.2f}]")
    print(f"  H_x range: [{Hx.min():.2e}, {Hx.max():.2e}]")

    # 4. Skin depth
    delta = skin_depth(5.8e7, 1e9)
    print(f"\n[skin_depth] Copper σ=5.8e7 S/m at 1 GHz: δ = {delta*1e6:.3f} μm")

    # Plots (comment out for headless CI)
    # demo_plane_wave()
    # demo_fresnel_reflection()
    # demo_waveguide_modes()
    # demo_skin_depth()

    print("\n[ALL DEMOS COMPLETE]")
