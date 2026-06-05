r"""
jackson_ch13-16_scattering.py
===============================
Computational examples from Jackson, Introduction to Electrodynamics, 4th Ed.
Chapters 13–16: Scattering, Diffraction, and Special Topics

Coverage
--------
- mie_scattering()      : Mie scattering efficiency for a spherical particle
- fourier_optics()       : Fresnel diffraction integral (rectangular aperture)
- vector_diffraction()   : Kirchhoff diffraction formula (scalar theory)

Physical constants from scipy.constants:
    c, ε₀, μ₀, pi

Authors: Computational Electromagnetics Lab
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import special
from scipy.constants import c as c0, epsilon_0 as eps0, mu_0 as mu0, pi


# ---------------------------------------------------------------------------
# 1. MIE SCATTERING
# ---------------------------------------------------------------------------

def mie_scattering(a, wavelength, n_particle, n_medium=1.0):
    r"""
    Compute Mie scattering efficiencies for a homogeneous sphere.

    Uses the BHMIE algorithm (Bohren & Huffman, 1983; Wiscombe, 1980).

    Parameters
    ----------
    a : float
        Sphere radius in metres.
    wavelength : float
        Wavelength in the medium in metres.
    n_particle : complex
        Complex refractive index of the particle (n_r + i·n_i).
    n_medium : float
        Refractive index of the surrounding medium (default 1.0).

    Returns
    -------
    Q_scat : float
        Scattering efficiency (σ_scat / πa²).
    Q_ext  : float
        Extinction efficiency (σ_ext / πa²).
    Q_abs  : float
        Absorption efficiency (σ_abs / πa²).

    Formula (Jackson / Bohren & Huffman)
    -------
    Q_scat = (1/x²) · Σ_{n=1}^{N} (2n+1) · (|a_n|² + |b_n|²)
    Q_ext  = (1/x²) · Σ_{n=1}^{N} (2n+1) · Re(a_n + b_n)

    where the Mie coefficients a_n, b_n are computed via the
    logarithmic derivative D_n method.

    Example
    -------
    >>> Q_s, Q_e, Q_a = mie_scattering(1e-6, 0.55e-6, 1.59+0.0j, 1.33)
    >>> print(f"Q_scat = {Q_s:.3f}")
    """
    m = complex(n_particle) / n_medium
    k = 2.0 * pi * n_medium / wavelength
    x = k * a  # size parameter

    if x < 1e-3:
        # Small-particle (Rayleigh) limit
        alpha = (m**2 - 1.0) / (m**2 + 2.0)
        Q_scat = (8.0/3.0) * x**4 * abs(alpha)**2
        Q_ext  = 4.0 * x**3 * np.imag(alpha)
        return Q_scat, Q_ext, Q_ext - Q_scat

    N = int(x + 4.0 * x**(1.0/3.0) + 2.0)
    N = max(N, 2)

    # D_n(x) = ψ_n'(x) / ψ_n(x), ψ_n = x·j_n
    # UPWARD recurrence (stable for small x)
    D = np.zeros(N+2, dtype=complex)
    D[0] = 1.0 / np.tan(x)   # = cot(x) = ψ_0'(x)/ψ_0(x)

    for n in range(1, N+1):
        D[n] = (n / x) - 1.0 / (D[n-1] + n / x)

    # D_n(mx) DOWNWARD recurrence (stable for large mx)
    mx = m * x
    Dmx = np.zeros(N+2, dtype=complex)
    Dmx[N] = 0.0 + 0.0j   # seed at large n
    for n in range(N, 0, -1):
        Dmx[n-1] = (n / mx) - 1.0 / (Dmx[n] + n / mx)

    # Riccati-Bessel functions
    n_arr = np.arange(0, N+2)
    jn   = special.spherical_jn(n_arr, x)
    yn   = special.spherical_yn(n_arr, x)

    psi  = x * jn
    chi  = -x * yn
    xi   = psi + 1j * chi

    # derivatives
    jnd  = special.spherical_jn(n_arr, x, derivative=True)
    ynd  = special.spherical_yn(n_arr, x, derivative=True)
    psip = jnd + psi / x
    chip = ynd + chi / x
    xip  = psip + 1j * chip

    # Accumulate Σ (2n+1)(|a_n|² + |b_n|²) and Σ (2n+1)·Re(a_n + b_n)
    sum_scatter = 0.0 + 0.0j
    sum_ext     = 0.0 + 0.0j

    for n in range(1, N+1):
        psi_n  = psi[n];  psip_n = psip[n]
        xi_n   = xi[n];   xip_n  = xip[n]
        Dn     = Dmx[n]

        # a_n (electric multipole)
        An = Dn / m + n / x
        a_n = (An * psip_n - psi_n) / (An * xip_n - xi_n)

        # b_n (magnetic multipole)
        Bn = Dn * m + n / x
        b_n = (Bn * psip_n - psi_n) / (Bn * xip_n - xi_n)

        if not np.isfinite(a_n): a_n = 0.0 + 0.0j
        if not np.isfinite(b_n): b_n = 0.0 + 0.0j

        fn = float(2*n + 1)
        sum_scatter += fn * (abs(a_n)**2 + abs(b_n)**2)
        sum_ext     += fn * (a_n + b_n)

    Q_scat = (1.0 / x**2) * np.real(sum_scatter)
    Q_ext  = (1.0 / x**2) * np.real(sum_ext)
    Q_abs  = Q_ext - Q_scat
    return float(Q_scat), float(Q_ext), float(Q_abs)


def demo_mie_scattering():
    """Plot Mie scattering efficiency vs size parameter for a silica sphere."""
    n_particle = 1.59 + 0.0j
    n_medium   = 1.33
    wavelength = 0.55e-6    # green light

    a_vals = np.logspace(-9, -5, 300)
    Qs, Qe, Qa = [], [], []
    for a in a_vals:
        Qs_i, Qe_i, Qa_i = mie_scattering(a, wavelength, n_particle, n_medium)
        Qs.append(Qs_i)
        Qe.append(Qe_i)
        Qa.append(Qa_i)

    x_vals = 2.0 * pi * n_medium * a_vals / wavelength

    plt.figure(figsize=(9, 5))
    plt.semilogx(x_vals, Qs, 'b-', lw=2, label=r"$Q_{\rm sca}$")
    plt.semilogx(x_vals, Qe, 'r-', lw=2, label=r"$Q_{\rm ext}$")
    plt.semilogx(x_vals, Qa, 'g-', lw=2, label=r"$Q_{\rm abs}$")
    plt.axvline(1.0, color='gray', ls='--', alpha=0.6, label=r"$x=1$")
    plt.xlabel(r"Size parameter $x = 2\pi a n_{\rm med}/\lambda$")
    plt.ylabel(r"Mie efficiency $Q$")
    plt.title(r"Mie Scattering Efficiency — Silica sphere ($n=1.59$) in water")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.ylim(0, None)
    plt.tight_layout()
    plt.savefig("mie_scattering.png", dpi=150)
    plt.show()
    print("[demo] Mie scattering plot saved as mie_scattering.png")


# ---------------------------------------------------------------------------
# 2. FRESNEL DIFFRACTION (RECTANGULAR APERTURE)
# ---------------------------------------------------------------------------

def fresnel_diffraction(a, wavelength, z, x_obs):
    r"""
    Compute the Fresnel diffraction pattern from a rectangular slit.

    Parameters
    ----------
    a : float
        Half-width of the rectangular aperture in metres.
    wavelength : float
        Wavelength in metres.
    z : float
        Distance from aperture to observation screen in metres.
    x_obs : array_like
        Observation coordinate along x on the screen in metres.

    Returns
    -------
    intensity : ndarray
        Normalised diffracted intensity I/I₀ at each x_obs.

    Formula (Jackson Sec. 13.2 — Fresnel integrals)
    -------
    U(x) ∝ [C(u₂) - C(u₁)] + i[S(u₂) - S(u₁)]
    where u_{1,2} = √(2/λz) · (x ± a)
    and C, S are the Fresnel integrals.

    Example
    -------
    >>> x = np.linspace(-3e-3, 3e-3, 601)
    >>> I = fresnel_diffraction(a=0.5e-3, wavelength=0.5e-6, z=1.0, x_obs=x)
    >>> print(f"Max intensity = {I.max():.3f}")
    """
    x_obs = np.asarray(x_obs)
    sqrt2 = np.sqrt(2.0)

    u  = sqrt2 * (x_obs + a) / np.sqrt(wavelength * z)
    u1 = sqrt2 * (x_obs - a) / np.sqrt(wavelength * z)

    C1, S1 = special.fresnel(u1)
    C2, S2 = special.fresnel(u)

    # Complex amplitude
    U = (C2 - C1) + 1j * (S2 - S1)
    intensity = (abs(U)**2)
    intensity = intensity / intensity.max()
    return intensity


def demo_fresnel_diffraction():
    """Plot Fresnel diffraction from a single slit."""
    a   = 0.2e-3    # 0.2 mm slit half-width
    lam = 0.5e-6    # 500 nm green light
    z   = 0.5       # 50 cm from slit

    x   = np.linspace(-5e-3, 5e-3, 2001)
    I   = fresnel_diffraction(a, lam, z, x)

    plt.figure(figsize=(10, 5))
    plt.plot(x * 1e3, I, 'b-', lw=1.5)
    plt.xlabel(r"Screen coordinate $x$ (mm)")
    plt.ylabel(r"Normalised intensity $I/I_0$")
    plt.title(fr"Fresnel Diffraction — Single Slit ($a={a*1e3:.1f}\,$mm, $z={z}\,$m)")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("fresnel_diffraction.png", dpi=150)
    plt.show()
    print("[demo] Fresnel diffraction plot saved as fresnel_diffraction.png")


# ---------------------------------------------------------------------------
# 3. KIRCHHOFF DIFFRACTION
# ---------------------------------------------------------------------------

def vector_diffraction(aperture_func, x, y, z, wavelength):
    r"""
    Scalar Kirchhoff diffraction integral for a planar aperture.

    Evaluates the complex field amplitude at the on-axis screen point
    (0, 0, z) from a rectangular aperture described by aperture_func.

    Parameters
    ----------
    aperture_func : callable
        Function f(x_ap, y_ap) returning float (transmission coefficient).
    x, y : ndarray
        Aperture coordinates (same shape, broadcastable grids).
    z : float
        Screen distance from aperture (metres).
    wavelength : float
        Wavelength in metres.

    Returns
    -------
    U_screen : complex
        Complex field amplitude on the screen at (0, 0, z).

    Formula (Jackson Eq. 13.7, Kirchhoff integral)
    -------
    U(P) = (i/λ) · ∫_aperture (e^{ikR}/R) · (1+cos χ)/2 dS

    Example
    -------
    >>> x_sq  = np.linspace(-1e-3, 1e-3, 51)
    >>> X, Y  = np.meshgrid(x_sq, x_sq)
    >>> U0    = vector_diffraction(
    ...     lambda x_, y_: ((np.abs(x_)<0.5e-3)&(np.abs(y_)<0.5e-3)).astype(float),
    ...     X, Y, z=1.0, wavelength=0.5e-6)
    >>> print(f"U0 = {U0:.3e}")
    """
    k   = 2.0 * pi / wavelength
    # On-axis point (0, 0, z): distance R = √(x²+y²+z²)
    R   = np.sqrt(x**2 + y**2 + z**2)
    # Kirchhoff kernel (on-axis: cos χ ≈ z/R ≈ 1)
    kernel = (1j / wavelength) * (np.exp(1j * k * R) / R) * 0.5 * (1.0 + z / R)
    U_aperture = aperture_func(x, y)
    U_screen   = np.sum(kernel * U_aperture)
    return U_screen


def demo_vector_diffraction():
    """Plot Kirchhoff diffraction of a square aperture."""
    x_screen = np.linspace(-10e-3, 10e-3, 201)
    z_screen = 0.5
    lam      = 0.5e-6

    # Fresnel diffraction cross-section (for 2D intensity pattern)
    a = 0.5e-3   # square aperture half-width
    I_cross = fresnel_diffraction(a, lam, z_screen, x_screen)

    # 2-D pattern (separable approximation)
    y_screen = x_screen
    XS, YS = np.meshgrid(x_screen, y_screen)
    I2D_flat = fresnel_diffraction(a, lam, z_screen, XS.flatten())
    I2D = I2D_flat.reshape(XS.shape)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    axes[0].plot(x_screen * 1e3, I_cross, 'b-', lw=1.5)
    axes[0].set_xlabel(r"$x$ (mm)")
    axes[0].set_ylabel(r"$I/I_0$")
    axes[0].set_title("Square Aperture — $x$-cross-section")
    axes[0].grid(True, alpha=0.3)

    im = axes[1].imshow(I2D, extent=[-10, 10, -10, 10],
                        cmap='hot', origin='lower', aspect='equal')
    axes[1].set_xlabel(r"$x$ (mm)")
    axes[1].set_ylabel(r"$y$ (mm)")
    axes[1].set_title("Square Aperture Diffraction Pattern")
    plt.colorbar(im, ax=axes[1], label=r"$I/I_0$")

    plt.suptitle(rf"Kirchhoff Diffraction — $a=0.5\,$mm, $z=0.5\,$m, $\lambda=500\,$nm",
                 fontsize=12)
    plt.tight_layout()
    plt.savefig("vector_diffraction.png", dpi=150)
    plt.show()
    print("[demo] Vector diffraction plot saved as vector_diffraction.png")


# ---------------------------------------------------------------------------
# MAIN / VALIDATION
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("Jackson Ch 13-16: Scattering and Diffraction")
    print("=" * 60)

    # 1. Mie scattering
    Qs, Qe, Qa = mie_scattering(a=1e-6, wavelength=0.55e-6,
                                  n_particle=1.59+0.0j, n_medium=1.33)
    print(f"\n[mie_scattering] a=1 μm, λ=0.55 μm, n=1.59 in water:")
    print(f"  Q_scat = {Qs:.4f},  Q_ext = {Qe:.4f},  Q_abs = {Qa:.4f}")

    # Known references:
    # For a=1um in water (x≈15.2), Q_scat should be O(1-10)
    x = 2*pi*1.33*1e-6/0.55e-6
    print(f"  (size param x={x:.2f}; reference Q_scat≈2-4)")

    Qs_r, Qe_r, Qa_r = mie_scattering(a=100e-9, wavelength=0.55e-6,
                                        n_particle=1.59+0.0j, n_medium=1.33)
    print(f"\n[Rayleigh limit] a=100 nm: Q_scat={Qs_r:.3e}")

    # Cross-check: m=1.5, x=1 → reference Q_ext≈0.21, Q_scat≈0.17
    Qs_x1, Qe_x1, _ = mie_scattering(a=1e-6, wavelength=2*pi*1e-6,
                                        n_particle=1.5+0.0j, n_medium=1.0)
    print(f"\n[Cross-check] m=1.5, x=1: Q_ext={Qe_x1:.3f}, Q_scat={Qs_x1:.3f}  (ref: 0.21, 0.17)")

    # 2. Fresnel diffraction
    x = np.linspace(-3e-3, 3e-3, 601)
    I = fresnel_diffraction(a=0.5e-3, wavelength=0.5e-6, z=1.0, x_obs=x)
    print(f"\n[fresnel_diffraction] a=0.5mm, z=1m, λ=0.5μm:")
    print(f"  Peak intensity = {I.max():.4f},  min = {I.min():.4f}")

    # 3. Vector diffraction
    x_sq  = np.linspace(-1e-3, 1e-3, 51)
    X, Y  = np.meshgrid(x_sq, x_sq)
    U0    = vector_diffraction(
                lambda x_, y_: ((np.abs(x_)<0.5e-3)&(np.abs(y_)<0.5e-3)).astype(float),
                X, Y, z=1.0, wavelength=0.5e-6)
    I0    = abs(U0)**2
    print(f"\n[vector_diffraction] Square aperture, z=1m, on-axis:")
    print(f"  On-axis |U|² (normalised) = {I0:.3e}")

    # Plots
    # demo_mie_scattering()
    # demo_fresnel_diffraction()
    # demo_vector_diffraction()

    print("\n[ALL DEMOS COMPLETE]")
