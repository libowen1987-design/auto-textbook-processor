r"""
jackson_ch09-12_radiation.py
==============================
Computational examples from Jackson, Introduction to Electrodynamics, 4th Ed.
Chapters 9–12: Radiation, Antennas, and Electromagnetic Radiation

Coverage
--------
- hertzian_dipole()       : Fields of an infinitesimal electric dipole
- half_wave_dipole()      : Radiation pattern of a half-wave linear antenna
- radiation_pressure()    : Radiation pressure of an EM wave on a surface
- multipole_radiation()   : Electric dipole and quadrupole radiation power

Physical constants from scipy.constants:
    c, ε₀, μ₀, pi, sqrt

Authors: Computational Electromagnetics Lab
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c as c0, epsilon_0 as eps0, mu_0 as mu0, pi


# ---------------------------------------------------------------------------
# 1. HERTZIAN (INFINITESIMAL) DIPOLE
# ---------------------------------------------------------------------------

def hertzian_dipole(I, L, f, r_obs, theta, phi=0.0):
    r"""
    Compute the far-field E and H of a Hertzian (infinitesimal) dipole.

    The dipole is oriented along the z-axis, centred at the origin.

    Parameters
    ----------
    I : float
        Current amplitude in amperes.
    L : float
        Effective length of the dipole in metres.
    f : float
        Frequency in Hz.
    r_obs : float
        Distance from dipole to observation point in metres.
    theta : float
        Polar angle (from +z axis) in radians.
    phi : float
        Azimuthal angle in radians (default 0).

    Returns
    -------
    E_theta : complex
        θ-component of far-field E in V/m.
    H_phi   : complex
        φ-component of far-field H in A/m.
    power_density : float
        Time-averaged Poynting vector magnitude S = |E|²/(2·η) in W/m².

    Formula (Jackson Eq. 9.19)
    -------
    E_θ = i·η·(k·I·L / 4πr) · sinθ · e^{-ikr}
    H_φ = i·(k·I·L / 4πr) · sinθ · e^{-ikr}

    where k = ω/c,  η = √(μ₀/ε₀) ≈ 377 Ω.

    Example
    -------
    >>> E, H, S = hertzian_dipole(1.0, 0.01, 300e6, 100.0, pi/2)
    >>> print(f"S = {S:.3e} W/m² at r=100m")
    """
    omega = 2.0 * pi * f
    k     = omega / c0
    eta   = np.sqrt(mu0 / eps0)

    # Current phasor: I·e^{-iωt}
    # Far-field terms ∝ 1/r
    sin_theta = np.sin(theta)

    E_theta = 1j * eta * (k * I * L / (4.0 * pi * r_obs)) * sin_theta
    H_phi   = 1j *     (k * I * L / (4.0 * pi * r_obs)) * sin_theta

    # Time-averaged Poynting vector in far field
    # S = (1/2)·Re{E × H*} = (1/2)·|E_θ|²/η
    power_density = 0.5 * abs(E_theta)**2 / eta

    return E_theta, H_phi, power_density


def demo_hertzian_dipole():
    """Plot the 3-D radiation pattern of a Hertzian dipole (sin²θ)."""
    theta_vals = np.linspace(0, pi, 181)
    phi_vals   = np.linspace(0, 2*pi, 361)

    TH, PH = np.meshgrid(theta_vals, phi_vals, indexing='ij')

    I, L, f, r = 1.0, 0.01, 300e6, 100.0
    S = np.zeros_like(TH)
    for i, th in enumerate(theta_vals):
        for j, ph in enumerate(phi_vals):
            _, _, S[i, j] = hertzian_dipole(I, L, f, r, th, ph)

    # Normalise
    S_max = S.max()
    S_norm = S / S_max

    # Spherical to Cartesian
    X = S_norm * np.sin(TH) * np.cos(PH)
    Y = S_norm * np.sin(TH) * np.sin(PH)
    Z = S_norm * np.cos(TH)

    fig = plt.figure(figsize=(8, 6))
    ax  = fig.add_subplot(111, projection='3d')
    # Subsample for clarity
    stride = 4
    ax.plot_surface(X[::stride, ::stride], Y[::stride, ::stride],
                    Z[::stride, ::stride], facecolors=plt.cm.plasma(S_norm[::stride, ::stride]),
                    rstride=1, cstride=1, alpha=0.85, shade=False)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$")
    ax.set_zlabel(r"$z$")
    ax.set_title(r"Hertzian Dipole Radiation Pattern  ($r=100\,$m, $f=300\,$MHz)")
    plt.tight_layout()
    plt.savefig("hertzian_dipole_3d.png", dpi=150)
    plt.show()
    print("[demo] Hertzian dipole 3-D pattern saved as hertzian_dipole_3d.png")

    # 2-D polar pattern (E-plane, φ=0)
    theta_p = np.linspace(0, pi, 361)
    S_p = np.array([hertzian_dipole(I, L, f, r, th)[2] for th in theta_p])

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(7, 6))
    ax.plot(theta_p, S_p / S_p.max(), 'b-', lw=2)
    ax.fill(theta_p, S_p / S_p.max(), alpha=0.3)
    ax.set_title(r"Hertzian Dipole — E-plane ($\phi=0$)")
    ax.set_theta_zero_location("N")
    plt.tight_layout()
    plt.savefig("hertzian_dipole_2d.png", dpi=150)
    plt.show()
    print("[demo] Hertzian dipole 2-D polar plot saved as hertzian_dipole_2d.png")


# ---------------------------------------------------------------------------
# 2. HALF-WAVE DIPOLE ANTENNA
# ---------------------------------------------------------------------------

def half_wave_dipole(I0, f, theta, r=100.0):
    r"""
    Compute the far-field radiation of a centre-fed half-wave dipole.

    The half-wave dipole (length ≈ λ/2) has a sinusoidal current distribution:
        I(z) = I₀ · sin(k·(L/2 - |z|))  for |z| ≤ L/2
    with L = λ/2.

    Parameters
    ----------
    I0 : float
        Peak current at the feed point in amperes.
    f : float
        Frequency in Hz.
    theta : array_like
        Polar angle (from dipole axis) in radians.
    r : float
        Observation distance in metres (default 100 m).

    Returns
    -------
    E_theta : ndarray
        Far-field θ-component of E (V/m).
    power_density : ndarray
        Time-averaged Poynting vector magnitude (W/m²).

    Formula (Jackson Eq. 9.29)
    -------
    E_θ = i·η·(I₀ / 2πr) · [cos(π/2·cosθ) / sinθ] · e^{-ikr}
    S_r = (1/2·η) · |E_θ|²

    Example
    -------
    >>> S = half_wave_dipole(1.0, 300e6, np.linspace(0, pi, 181))
    >>> print(f"Max S = {S.max():.3e} W/m²")
    """
    k    = 2.0 * pi * f / c0
    eta  = np.sqrt(mu0 / eps0)
    theta = np.asarray(theta)

    # Antenna pattern factor (Jackson Eq. 9.29)
    with np.errstate(divide='ignore', invalid='ignore'):
        F = np.cos(0.5 * pi * np.cos(theta)) / np.sin(theta)
        F = np.where(np.sin(theta) < 1e-12, 0.0, F)

    E_theta = eta * (I0 / (2.0 * pi * r)) * F * np.exp(-1j * k * r)
    power_density = 0.5 * abs(E_theta)**2 / eta
    return E_theta, power_density


def demo_half_wave_dipole():
    """Plot the radiation pattern of a half-wave dipole."""
    f     = 300e6           # 300 MHz  (λ = 1 m)
    theta = np.linspace(0, pi, 721)
    I0    = 1.0

    _, S = half_wave_dipole(I0, f, theta)
    S_norm = S / S.max()

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # 2-D polar
    ax0 = axes[0]
    ax0 = plt.subplot(121, projection='polar')
    ax0.plot(theta, S_norm, 'b-', lw=2)
    ax0.fill(theta, S_norm, alpha=0.25)
    ax0.set_title(r"Half-wave Dipole — Radiation Pattern")
    ax0.set_theta_zero_location("N")

    # Cartesian
    axes[1].plot(np.rad2deg(theta), S_norm, 'b-', lw=2)
    axes[1].set_xlabel(r"Polar angle $\theta$ (deg)")
    axes[1].set_ylabel(r"Normalised power density $S/S_{\max}$")
    axes[1].set_title("Half-wave Dipole — Linear Scale")
    axes[1].set_xlim(0, 180)
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("half_wave_dipole.png", dpi=150)
    plt.show()
    print("[demo] Half-wave dipole pattern saved as half_wave_dipole.png")


# ---------------------------------------------------------------------------
# 3. RADIATION PRESSURE
# ---------------------------------------------------------------------------

def radiation_pressure(S, R=0.0, n=1.0):
    r"""
    Compute radiation pressure on a surface.

    Parameters
    ----------
    S : float
        Incident power flux density in W/m² (time-averaged).
    R : float
        Reflectance of the surface (0 for perfectly absorbing,
        1 for perfectly reflecting).
    n : float
        Refractive index of the medium on the incidence side.

    Returns
    -------
    p : float
        Radiation pressure in Pa (N/m²).

    Formula (Jackson Sec. 9.3)
    -------
    Perfect absorber (R=0):   p = S / c
    Perfect reflector (R=1):  p = 2S / c
    General case:             p = (1 + R) · S / c

    Example
    -------
    >>> p = radiation_pressure(1000.0, R=1.0)   # 1 kW/m² on mirror
    >>> print(f"p = {p:.3e} Pa")
    """
    c = c0 / n
    p = (1.0 + R) * S / c
    return p


def demo_radiation_pressure():
    """Plot radiation pressure vs incident power flux."""
    S_vals = np.linspace(1e1, 1e5, 500)   # 10 W/m² → 100 kW/m²

    p_abs  = radiation_pressure(S_vals, R=0.0)   # black surface
    p_refl = radiation_pressure(S_vals, R=1.0)   # perfect mirror

    plt.figure(figsize=(9, 5))
    plt.loglog(S_vals, p_abs * 1e9,  'b-', lw=2, label='Perfect absorber (R=0)')
    plt.loglog(S_vals, p_refl * 1e9, 'r-', lw=2, label='Perfect reflector (R=1)')
    plt.xlabel(r"Incident power flux $S$ (W/m²)")
    plt.ylabel(r"Radiation pressure $p$ (nPa)")
    plt.title("Radiation Pressure vs Incident Power Flux")
    plt.legend()
    plt.grid(True, which='both', alpha=0.3)
    plt.tight_layout()
    plt.savefig("radiation_pressure.png", dpi=150)
    plt.show()
    print("[demo] Radiation pressure plot saved as radiation_pressure.png")

    # Numerical example: solar constant ~1361 W/m²
    S_sun = 1361.0
    p_sun = radiation_pressure(S_sun, R=0.0)
    print(f"\n[radiation_pressure] Solar constant: S = {S_sun} W/m²")
    print(f"  p_absorbing = {p_sun:.3e} Pa")
    print(f"  p_reflecting = {radiation_pressure(S_sun, R=1.0):.3e} Pa")


# ---------------------------------------------------------------------------
# 4. MULTIPOLE RADIATION POWER
# ---------------------------------------------------------------------------

def multipole_radiation(p_vec, q_vec, f, r=100.0):
    r"""
    Compute the radiated power from electric dipole and quadrupole moments.

    Parameters
    ----------
    p_vec : ndarray, shape (3,)
        Electric dipole moment \mathbf{p} in C·m.
    q_vec : ndarray, shape (3, 3)
        Electric quadrupole moment tensor Q_{ij} in C·m².
        Note: Jackson uses a traceless tensor.
    f : float
        Frequency in Hz.
    r : float
        Observation distance (only used for field normalisation).

    Returns
    -------
    P_dipole : float
        Total power radiated by the electric dipole (W).
    P_quad   : float
        Total power radiated by the electric quadrupole (W).

    Formula (Jackson Eq. 9.42, 9.57)
    -------
    P_elec_dipole = (μ₀·ω⁴·|p|²) / (12π·c)

    P_elec_quad   = (μ₀·ω⁶·|Q_{ij}²|) / (720π·c)

    where Q_{ij} = Σ q_n (3x_i·x_j - r_n²·δ_{ij}) and ω = 2πf.

    Example
    -------
    >>> p = np.array([0.0, 0.0, 1e-12])   # 1 pC·m
    >>> Pd, Pq = multipole_radiation(p, np.zeros((3,3)), 300e6)
    >>> print(f"P_dipole = {Pd:.3e} W")
    """
    omega = 2.0 * pi * f
    mu0_  = mu0

    # Dipole power
    p_mag = np.linalg.norm(p_vec)
    P_dipole = (mu0_ * omega**4 * p_mag**2) / (12.0 * pi * c0)

    # Quadrupole power: trace of Q²
    Q = np.asarray(q_vec)
    Q_sq_trace = np.trace(Q @ Q)   # Σ_{ij} Q_{ij}·Q_{ji} = Σ Q_{ij}²
    P_quad    = (mu0_ * omega**6 * Q_sq_trace) / (720.0 * pi * c0)

    return P_dipole, P_quad


def demo_multipole_radiation():
    """Compare dipole and quadrupole radiation power vs frequency."""
    f_vals = np.linspace(1e6, 10e9, 300)   # 1 MHz → 10 GHz

    # Example dipole moment
    p0 = 1e-12       # 1 pC·m
    p_vec = np.array([0.0, 0.0, p0])

    # Example quadrupole moment (a simple zz component)
    q0 = 1e-24       # 1e-24 C·m²
    Q_mat = np.diag([0.0, 0.0, q0])   # traceless: Q_zz = q0, others 0

    P_d = np.array([multipole_radiation(p_vec, Q_mat, f)[0] for f in f_vals])
    P_q = np.array([multipole_radiation(p_vec, Q_mat, f)[1] for f in f_vals])

    plt.figure(figsize=(9, 5))
    plt.loglog(f_vals/1e9, P_d * 1e12, 'b-', lw=2, label=r'Electric dipole $|p|=1\,$pC·m')
    plt.loglog(f_vals/1e9, P_q * 1e12, 'r-', lw=2, label=r'Electric quadrupole $Q_{zz}=10^{-24}\,$C·m²')
    plt.xlabel(r"Frequency $f$ (GHz)")
    plt.ylabel(r"Radiated power $P$ (pW)")
    plt.title("Multipole Radiation Power vs Frequency")
    plt.legend()
    plt.grid(True, which='both', alpha=0.3)
    plt.tight_layout()
    plt.savefig("multipole_radiation.png", dpi=150)
    plt.show()
    print("[demo] Multipole radiation plot saved as multipipole_radiation.png")


# ---------------------------------------------------------------------------
# MAIN / VALIDATION
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("Jackson Ch 09-12: Radiation and Antennas")
    print("=" * 60)

    # 1. Hertzian dipole
    E, H, S = hertzian_dipole(I=1.0, L=0.01, f=300e6, r_obs=100.0, theta=pi/2)
    print(f"\n[hertzian_dipole] I=1A, L=1cm, f=300MHz, r=100m, θ=90°:")
    print(f"  |E_θ| = {abs(E):.3f} V/m,  |H_φ| = {abs(H):.3f} A/m")
    print(f"  S = {S:.3e} W/m²")

    # 2. Half-wave dipole
    _, S_hw = half_wave_dipole(I0=1.0, f=300e6, theta=np.array([pi/2]))
    print(f"\n[half_wave_dipole] I₀=1A, f=300MHz, broadside θ=90°:")
    print(f"  S = {S_hw[0]:.3e} W/m²")

    # 3. Radiation pressure
    p = radiation_pressure(1361.0, R=1.0)
    print(f"\n[radiation_pressure] Solar on perfect mirror: p = {p:.3e} Pa")
    print(f"  → Equivalent to {p/9.81*1e6:.2f} mg/m²")

    # 4. Multipole radiation
    p_vec = np.array([0.0, 0.0, 1e-12])
    Q_mat = np.zeros((3, 3))
    Q_mat[2, 2] = 1e-24
    Pd, Pq = multipole_radiation(p_vec, Q_mat, 300e6)
    print(f"\n[multipole_radiation] f=300MHz:")
    print(f"  P_dipole  = {Pd:.3e} W")
    print(f"  P_quad    = {Pq:.3e} W")

    # Plots
    # demo_hertzian_dipole()
    # demo_half_wave_dipole()
    # demo_radiation_pressure()
    # demo_multipole_radiation()

    print("\n[ALL DEMOS COMPLETE]")
