#!/usr/bin/env python3
"""
Jackson Classical Electrodynamics (3rd Ed) — Ch5–Ch8 Examples
=============================================================

Gaussian units throughout, with SI versions noted where helpful.

Topics covered:
  1. Biot–Savart / magnetic field calculations (§5.1–5.3)
  2. Plane-wave polarization / Fresnel / Kramers–Kronig (§7.3–7.5, 6.10)
  3. Waveguide TE/TM modes (§8.3–8.6)
  4. Resonant cavities (§8.8–8.10)

Dependencies: numpy, scipy, matplotlib
"""

import numpy as np
from numpy import pi, sin, cos, sqrt, exp, real, imag, angle
import warnings
from scipy.integrate import trapezoid

# ============================================================
# 1.  BIOT–SAVART / MAGNETIC FIELD CALCULATIONS
# ============================================================


def biot_savart_gaussian(current, loop_points):
    """
    Biot–Savart integral for a current loop (Gaussian units).

    Parameters
    ----------
    current : float
        Current in statamperes (1 A ≈ 3×10⁹ statA).
    loop_points : ndarray, shape (N, 3)
        Ordered points on the current loop [cm].

    Returns
    -------
    field_func : callable
        B(x, y, z) → array of 3 components [G].
    """
    from scipy.interpolate import splprep, splev

    tck, _ = splprep(loop_points.T, s=0, per=True)
    N = 400
    u = np.linspace(0, 1, N)
    pts = np.array(splev(u, tck)).T          # (N, 3)
    d_pts = np.array(splev(u, tck, der=1)).T # (N, 3)
    dl = d_pts / N

    def B_field(x, y, z):
        r0 = np.array([x, y, z])
        B = np.zeros(3)
        for i in range(N):
            r = pts[i]
            dl_vec = dl[i]
            dr = r0 - r
            r_mag = np.linalg.norm(dr)
            if r_mag < 1e-12:
                continue
            B += current * np.cross(dl_vec, dr) / r_mag**3
        return B  # Gaussian: factor 1/c omitted; include as B / (speed_of_light)
    return B_field


def magnetic_dipole_field(m, x, y, z):
    """
    Magnetic dipole field in Gaussian units.

    B = [3 r̂ (r̂·m) - m] / r³   (outside origin)

    Parameters
    ----------
    m : array_like (3,)
        Magnetic dipole moment [erg/G].
    x, y, z : float
        Observation point.

    Returns
    -------
    B : ndarray (3,)
        Magnetic field [G].
    """
    r_vec = np.array([x, y, z])
    r = np.linalg.norm(r_vec)
    if r < 1e-14:
        raise ValueError("Field singular at origin")
    r_hat = r_vec / r
    B = (3 * r_hat * np.dot(r_hat, m) - m) / r**3
    return B


def wire_loop_B_on_axis(I, R, z, unit="gaussian"):
    """
    Magnetic field on the axis of a circular current loop.

    Gaussian:  B(z) = (2π I R² / c) / (R² + z²)^{3/2}
    SI:        B(z) = (μ₀ I R² / 2) / (R² + z²)^{3/2}

    Parameters
    ----------
    I : float
        Current.
    R : float
        Loop radius.
    z : float or ndarray
        Axial position(s).
    unit : str
        'gaussian' or 'si'.

    Returns
    -------
    Bz : float or ndarray
        Axial magnetic field.
    """
    denom = (R**2 + z**2)**1.5
    if unit == "gaussian":
        c = 2.998e10  # cm/s
        return (2 * pi * I * R**2 / c) / denom
    elif unit == "si":
        mu0 = 4 * pi * 1e-7
        return (mu0 * I * R**2 / 2) / denom
    else:
        raise ValueError("unit must be 'gaussian' or 'si'")


# ============================================================
# 2.  PLANE WAVES / POLARIZATION / FRESNEL / KRAMERS-KRONIG
# ============================================================


def fresnel_coefficients(n1, n2, theta_i):
    """
    Fresnel reflection and transmission coefficients.

    Parameters
    ----------
    n1 : float
        Refractive index of incident medium.
    n2 : float
        Refractive index of transmitted medium.
    theta_i : float
        Incident angle [rad].

    Returns
    -------
    dict with keys:
        r_perp, t_perp, r_par, t_par, theta_t, brewster_angle
    """
    theta_t = np.arcsin(n1 / n2 * sin(theta_i)) if n1 * sin(theta_i) / n2 <= 1 else np.nan

    if np.isnan(theta_t):
        # Total internal reflection
        return {
            "r_perp": 1.0, "t_perp": 0.0,
            "r_par": 1.0, "t_par": 0.0,
            "theta_t": np.nan, "brewster_angle": None,
            "tir": True
        }

    c_i, c_t = cos(theta_i), cos(theta_t)
    r_perp = (n1 * c_i - n2 * c_t) / (n1 * c_i + n2 * c_t)
    t_perp = 2 * n1 * c_i / (n1 * c_i + n2 * c_t)
    r_par = (n2 * c_i - n1 * c_t) / (n2 * c_i + n1 * c_t)
    t_par = 2 * n1 * c_i / (n2 * c_i + n1 * c_t)

    theta_B = np.arctan2(n2, n1)  # Brewster angle

    return {
        "r_perp": r_perp, "t_perp": t_perp,
        "r_par": r_par, "t_par": t_par,
        "theta_t": theta_t, "brewster_angle": theta_B,
        "tir": False
    }


def reflectivity_coefficients(n1, n2, theta_i_deg):
    """
    Convenience wrapper: Fresnel coefficients with degrees input.

    Returns R_perp = |r_perp|², R_par = |r_par|², T_perp, T_par.
    """
    theta_i = np.deg2rad(theta_i_deg)
    fres = fresnel_coefficients(n1, n2, theta_i)
    R_perp = abs(fres["r_perp"])**2
    R_par = abs(fres["r_par"])**2
    T_perp = 1 - R_perp
    T_par = 1 - R_par
    return {
        "R_perp": R_perp, "R_par": R_par,
        "T_perp": T_perp, "T_par": T_par,
        **fres
    }


def stokes_parameters(E1, E2):
    """
    Stokes parameters for a plane wave.

    Parameters
    ----------
    E1, E2 : complex
        Complex field amplitudes along two orthogonal axes.

    Returns
    -------
    s : ndarray (4,)
        Stokes parameters (s0, s1, s2, s3).
    """
    s0 = abs(E1)**2 + abs(E2)**2
    s1 = abs(E1)**2 - abs(E2)**2
    s2 = 2 * real(E1.conjugate() * E2)
    s3 = 2 * imag(E1.conjugate() * E2)
    return np.array([s0, s1, s2, s3])


def jones_polarization(psi, delta):
    """
    Jones vector for general elliptical polarization.

    Parameters
    ----------
    psi : float
        Orientation angle [rad] (0 = x-axis).
    delta : float
        Phase difference between y and x components [rad].
        0 = linear at angle psi,
        pi/2 = right elliptical (sin psi, cos psi rotated).

    Returns
    -------
    J : ndarray (2,), complex
        Normalized Jones vector.
    """
    return np.array([cos(psi), sin(psi) * exp(1j * delta)])


def kramers_kronig_epsilon(omega, eps_imag):
    """
    Compute real part of dielectric function from imaginary part
    using Kramers–Kronig relation (principal value integral).

    ε'(ω) - 1 = (2/π) P ∫₀^∞ [ω' ε''(ω')] / [ω'² - ω²] dω'

    Parameters
    ----------
    omega : ndarray
        Frequency array [rad/s].
    eps_imag : ndarray
        Imaginary part of ε at each frequency.

    Returns
    -------
    eps_real : ndarray
        Real part of ε computed via KK.
    """
    n = len(omega)
    eps_real = np.ones_like(omega)
    for i in range(n):
        w0 = omega[i]
        integrand = np.zeros_like(omega)
        for j in range(n):
            if j == i:
                continue
            integrand[j] = omega[j] * eps_imag[j] / (omega[j]**2 - w0**2)
        eps_real[i] = 1.0 + (2.0 / pi) * trapezoid(integrand, omega)
    return eps_real


def lorentz_epsilon(omega, omega_0, omega_p, gamma):
    """
    Dielectric function from Lorentz oscillator model (Gaussian).

    ε(ω) = 1 + ω_p² / (ω₀² - ω² - i γ ω)

    Parameters
    ----------
    omega : ndarray
        Frequencies.
    omega_0 : float
        Resonance frequency.
    omega_p : float
        Plasma frequency.
    gamma : float
        Damping rate.

    Returns
    -------
    eps : ndarray, complex
    """
    return 1.0 + omega_p**2 / (omega_0**2 - omega**2 - 1j * gamma * omega)


def plasma_dispersion(omega, omega_p):
    """
    Dispersion relation for a cold unmagnetized plasma.

    ω² = ω_p² + c² k²   →   k(ω) = (1/c) √(ω² - ω_p²)

    Parameters
    ----------
    omega : ndarray
        Frequencies.
    omega_p : float
        Plasma frequency.

    Returns
    -------
    k : ndarray
        Wave number. Imaginary if ω < ω_p (evanescent).
    """
    c = 2.998e10
    k = np.sqrt(omega**2 - omega_p**2 + 0j) / c
    return k


# ============================================================
# 3.  WAVEGUIDE TE/TM MODES
# ============================================================


def waveguide_cutoff_rectangular(m, n, a, b):
    """
    Cutoff frequency for a rectangular waveguide (Gaussian).

    ω_{mn} = c π √[(m/a)² + (n/b)²]

    Parameters
    ----------
    m, n : int
        Mode indices.
    a, b : float
        Waveguide dimensions [cm].

    Returns
    -------
    omega_c : float [rad/s]
    fc : float [Hz]  (cutoff frequency)
    lambda_c : float [cm]  (cutoff wavelength)
    """
    c = 2.998e10
    kappa = pi * sqrt((m / a)**2 + (n / b)**2)
    omega_c = c * kappa
    fc = omega_c / (2 * pi)
    lambda_c = 2 * pi / kappa
    return omega_c, fc, lambda_c


def waveguide_dispersion_rectangular(m, n, a, b, omega):
    """
    Propagation constant for a rectangular waveguide.

    Parameters
    ----------
    m, n : int
        Mode indices.
    a, b : float
        Dimensions [cm].
    omega : float or ndarray
        Frequency [rad/s].

    Returns
    -------
    k : complex   Propagation constant. Imag when below cutoff.
    """
    c = 2.998e10
    omega_c = c * pi * sqrt((m / a)**2 + (n / b)**2)
    k = np.sqrt((omega / c)**2 - (omega_c / c)**2 + 0j)
    return k


def te10_fields_rectangular(a, b, omega, z, x, y, t=0, E0=1.0):
    """
    TE₁₀ mode fields in a rectangular waveguide (Gaussian units).

    Dimensions: 0 ≤ x ≤ a, 0 ≤ y ≤ b. Propagation along +z.
    Time dependence exp(-iωt) implicit.

    Parameters
    ----------
    a, b : float  Dimensions [cm] (a > b for dominant TE10).
    omega : float  Angular frequency [rad/s].
    z : float or ndarray  Position along guide [cm].
    x, y : float  Transverse position.
    t : float  Time [s].
    E0 : float  Field amplitude.

    Returns
    -------
    dict with E_x, E_y, E_z, B_x, B_y, B_z (real-valued at time t).
    """
    c = 2.998e10
    omega_c = pi * c / a
    if omega <= omega_c:
        warnings.warn(f"ω = {omega:.2e} ≤ ω_c = {omega_c:.2e}; mode is cutoff")
    kz = sqrt(omega**2 / c**2 - (pi / a)**2 + 0j)
    kz = real(kz)  # take the real part for propagating fields

    # Normalization
    kappa = pi / a
    phase = exp(1j * (kz * z - omega * t))

    Ey = E0 * sin(kappa * x) * phase
    Bx = -1j * kz * c / omega * E0 * sin(kappa * x) * phase
    Bz = -1j * pi * c / (omega * a) * E0 * cos(kappa * x) * phase

    return {
        "E_x": 0 * real(Ey),  # Ex = 0 for TE10
        "E_y": real(Ey),
        "E_z": 0 * real(Ey),
        "B_x": real(Bx),
        "B_y": 0 * real(Ey),
        "B_z": real(Bz),
    }


def waveguide_cutoff_circular(radius, mode_type="te", m=0, n=1):
    """
    Cutoff frequency for a circular waveguide.

    TE modes: J_m'(κa) = 0
    TM modes: J_m(κa) = 0

    Parameters
    ----------
    radius : float  [cm]
    mode_type : 'te' or 'tm'
    m, n : int   Mode indices (n ≥ 1).

    Returns
    -------
    omega_c : float [rad/s]
    fc : float [Hz]
    lambda_c : float [cm]
    """
    from scipy.special import jnp_zeros, jn_zeros

    c = 2.998e10
    if mode_type == "te":
        # Roots of J_m'(x) = 0
        roots = jnp_zeros(m, n)
    else:
        # Roots of J_m(x) = 0
        roots = jn_zeros(m, n)

    kappa = roots[-1] / radius
    omega_c = c * kappa
    fc = omega_c / (2 * pi)
    lambda_c = 2 * pi / kappa
    return omega_c, fc, lambda_c


# ============================================================
# 4.  RESONANT CAVITIES
# ============================================================


def cavity_resonant_frequency_rect(m, n, p, a, b, d):
    """
    Resonant frequency of a rectangular cavity (Gaussian).

    ω_{mnp} = c π √[(m/a)² + (n/b)² + (p/d)²]

    Parameters
    ----------
    m, n, p : int
        Mode indices. At most one can be zero for TE modes.
    a, b, d : float
        Cavity dimensions [cm].

    Returns
    -------
    omega_r : float [rad/s]
    fr : float [Hz]
    lambda_r : float [cm]
    """
    c = 2.998e10
    kappa = pi * sqrt((m / a)**2 + (n / b)**2 + (p / d)**2)
    omega_r = c * kappa
    fr = omega_r / (2 * pi)
    lambda_r = 2 * pi / kappa
    return omega_r, fr, lambda_r


def cavity_q_rectangular(m, n, p, a, b, d, sigma, unit="gaussian"):
    """
    Quality factor Q of a rectangular cavity with conducting walls.

    Q = ω₀ U / P_loss

    For highly conductive walls, Q ≈ (2/δ) × V / S
    where δ is the skin depth.

    Parameters
    ----------
    m, n, p : int  Mode indices.
    a, b, d : float  Dimensions [cm].
    sigma : float  Conductivity [(Gaussian) s⁻¹ or (SI) S/m].
    unit : 'gaussian' or 'si'

    Returns
    -------
    Q : float
    """
    c = 2.998e10
    omega_r, _, _ = cavity_resonant_frequency_rect(m, n, p, a, b, d)

    if unit == "gaussian":
        # Skin depth in Gaussian: δ = c / √(2π μ σ ω)
        mu = 1.0  # non-magnetic
        delta = c / sqrt(2 * pi * mu * sigma * omega_r)
    else:  # SI
        mu0 = 4 * pi * 1e-7
        mu_r = 1.0
        epsilon0 = 8.854e-14  # F/cm
        # Convert ω_r (Gaussian) → SI
        delta = sqrt(2 / (mu0 * mu_r * sigma * omega_r))
        # ω_r same in both since c same; need consistent conductivity

    V = a * b * d
    S = 2 * (a * b + a * d + b * d)
    Q = (2 / delta) * (V / S)
    return Q


def te101_fields_rectangular(a, b, d, x, y, z, t=0, E0=1.0):
    """
    TE₁₀₁ mode fields in a rectangular cavity.

    Dimensions: 0 ≤ x ≤ a, 0 ≤ y ≤ b, 0 ≤ z ≤ d.

    Returns dict with real-valued E and B fields.
    """
    c = 2.998e10
    omega_r = c * pi * sqrt((1 / a)**2 + (1 / d)**2)
    phase = exp(-1j * omega_r * t)

    kx = pi / a
    kz = pi / d

    Ey = E0 * sin(kx * x) * sin(kz * z) * phase
    Bx = -1j * kz * c / omega_r * E0 * sin(kx * x) * cos(kz * z) * phase
    Bz = -1j * kx * c / omega_r * E0 * cos(kx * x) * sin(kz * z) * phase

    return {
        "E_x": 0 * real(Ey),
        "E_y": real(Ey),
        "E_z": 0 * real(Ey),
        "B_x": real(Bx),
        "B_y": 0 * real(Ey),
        "B_z": real(Bz),
    }


def cavity_resonant_frequency_cyl(radius, height, mode_type="te", m=0, n=1, p=1):
    """
    Resonant frequency of a cylindrical cavity.

    ω_{mnp} = c √[(κ_{mn}/R)² + (pπ/d)²]

    TE: κ_{mn} a = roots of J_m'(x) = 0
    TM: κ_{mn} a = roots of J_m(x) = 0

    Parameters
    ----------
    radius : float  [cm]
    height : float  [cm]
    mode_type : 'te' or 'tm'
    m, n, p : int

    Returns
    -------
    omega_r : float [rad/s]
    fr : float [Hz]
    """
    from scipy.special import jnp_zeros, jn_zeros

    c = 2.998e10
    if mode_type == "te":
        roots = jnp_zeros(m, n)
    else:
        roots = jn_zeros(m, n)

    kappa = roots[-1] / radius
    omega_r = c * sqrt(kappa**2 + (p * pi / height)**2)
    fr = omega_r / (2 * pi)
    return omega_r, fr


# ============================================================
# 5.  DEMONSTRATION / TEST SUITE
# ============================================================


def demo_all():
    """Run through examples for each of the four topic areas."""
    print("=" * 65)
    print("JACKSON Ch5-Ch8  —  Numerical Examples")
    print("=" * 65)

    # --- 1. Biot-Savart -- wire loop ---
    print("\n" + "-" * 65)
    print("1.  BIOT–SAVART: Field on axis of a current loop")
    print("-" * 65)
    I = 1.0       # statA (3.33e-10 A)
    R = 5.0       # cm
    zs = np.array([0, 5, 10])
    for z in zs:
        B = wire_loop_B_on_axis(I, R, z, unit="gaussian")
        print(f"    z={z:4.1f} cm → Bz = {B:.8e} G")

    print("    (SI equivalent at z=0):")
    B_si = wire_loop_B_on_axis(1.0, 0.05, 0, unit="si")
    print(f"    Bz(SI) = {B_si:.6e} T  (I=1 A, R=5 cm)")

    # --- 2. Fresnel coefficients ---
    print("\n" + "-" * 65)
    print("2.  FRESNEL: Reflection at air–glass interface")
    print("-" * 65)
    n1, n2 = 1.0, 1.5
    thetas = [0, 30, 45, 56.3, 60]
    print(f"    n1={n1}, n2={n2}  (Brewster angle ≈ {np.rad2deg(np.arctan2(n2,n1)):.1f}°)")
    print(f"    {'θ_i(°)':>8}  {'R_perp':>8}  {'R_par':>8}")
    for th in thetas:
        r = reflectivity_coefficients(n1, n2, th)
        print(f"    {th:8.1f}  {r['R_perp']:8.5f}  {r['R_par']:8.5f}")

    # --- 3. Waveguide TE10 mode ---
    print("\n" + "-" * 65)
    print("3.  WAVEGUIDE TE₁₀: Rectangular (a=2 cm, b=1 cm)")
    print("-" * 65)
    a, b = 2.0, 1.0
    wc, fc, lamc = waveguide_cutoff_rectangular(1, 0, a, b)
    print(f"    Cutoff:  fc={fc/1e9:.4f} GHz,  λc={lamc:.3f} cm")
    omega_test = 1.5 * wc  # 50% above cutoff
    kz = waveguide_dispersion_rectangular(1, 0, a, b, omega_test)
    print(f"    At ω=1.5 ω_c:  kz = {real(kz):.4f} rad/cm")
    # Show peak field magnitudes (t such that e^{-iωt} = -i gives real B_x, B_z)
    t_peak = pi / (2 * omega_test)
    fields = te10_fields_rectangular(a, b, omega_test, 0, 0.5, 0.5, t=t_peak)
    print(f"    TE10 E_y magnitude at (a/4,b/4,z=0) = {abs(fields['E_y']):.4f}")
    fields_t0 = te10_fields_rectangular(a, b, omega_test, 0, 0.5, 0.5, t=0)
    print(f"    E_y(t=0) = {fields_t0['E_y']:.4f}  (field snapshot)")

    # Circular waveguide
    wc_circ, _, _ = waveguide_cutoff_circular(1.0, "te", 1, 1)
    print(f"    Circular (R=1cm) TE₁₁ cutoff: {real(wc_circ/1e9):.2f} GHz")

    # --- 4. Resonant cavity ---
    print("\n" + "-" * 65)
    print("4.  RESONANT CAVITY: Rectangular (a=3, b=2, d=5 cm)")
    print("-" * 65)
    a_c, b_c, d_c = 3.0, 2.0, 5.0
    for mode in [(1,0,1), (1,1,1), (2,0,1)]:
        m, n, p = mode
        wr, fr, _ = cavity_resonant_frequency_rect(m, n, p, a_c, b_c, d_c)
        print(f"    TE/TM {m}{n}{p}: fr = {real(fr)/1e9:.3f} GHz")

    # Quality factor (copper: σ ≈ 5.8×10⁷ S/m in SI)
    sigma_cu_gaussian = 5.8e17  # approximate Gaussian equivalent (s⁻¹)
    Q = cavity_q_rectangular(1, 0, 1, a_c, b_c, d_c, sigma_cu_gaussian)
    print(f"    Q (TE101, Cu walls) ≈ {Q:.0f}")

    # Cylindrical cavity
    wr_cyl, fr_cyl = cavity_resonant_frequency_cyl(3.0, 4.0, "te", 1, 1, 1)
    print(f"    Cylindrical (R=3, d=4 cm) TE₁₁₁: fr = {fr_cyl/1e9:.3f} GHz")

    # --- 5. Kramers–Kronig check ---
    print("\n" + "-" * 65)
    print("5.  KRAMERS-KRONIG: Lorentz oscillator consistency check")
    print("-" * 65)
    omega_arr = np.linspace(0.1, 5.0, 200)
    omega_0, om_p, gamma = 2.0, 1.0, 0.2
    eps = lorentz_epsilon(omega_arr, omega_0, om_p, gamma)
    eps_imag = imag(eps)
    eps_real_kk = kramers_kronig_epsilon(omega_arr, eps_imag)
    eps_real_exact = real(eps)
    err = np.mean(abs(eps_real_kk - eps_real_exact))
    print(f"    ω₀={omega_0}, ω_p={om_p}, γ={gamma}")
    print(f"    Mean KK reconstruction error: {err:.4e}")

    print("\n" + "=" * 65)
    print("All demos complete.")
    print("=" * 65)


if __name__ == "__main__":
    demo_all()
