#!/usr/bin/env python3
"""
Jackson Classical Electrodynamics, 3rd Ed — Ch9–Ch12 Computational Examples
===========================================================================

Examples covering:
  Ch9  — Electric dipole, magnetic dipole, electric quadrupole radiation
  Ch10 — Rayleigh and Mie scattering cross sections
  Ch11 — Lorentz transformation visualization (Minkowski diagrams)
  Ch12 — Relativistic particle motion (cyclotron, E×B drift, synchrotron)

Requires: numpy, scipy, matplotlib
"""

import numpy as np
from scipy import integrate, special
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

# ---------------------------------------------------------------------------
# Physical constants (SI)
# ---------------------------------------------------------------------------
c = 299_792_458.0           # speed of light [m/s]
eps0 = 8.854187817e-12      # vacuum permittivity [F/m]
mu0 = 4e-7 * np.pi           # vacuum permeability [H/m]
Z0 = np.sqrt(mu0 / eps0)     # vacuum impedance [Ω] ~ 377 Ω
qe = 1.602176634e-19         # elementary charge [C]
me = 9.10938356e-31          # electron mass [kg]
h = 6.62607015e-34           # Planck constant [J·s]
hbar = h / (2 * np.pi)       # reduced Planck constant
alpha = qe**2 / (4 * np.pi * eps0 * hbar * c)  # fine-structure constant ≈ 1/137

r0 = qe**2 / (4 * np.pi * eps0 * me * c**2)    # classical electron radius [m]

# ===================================================================
#  CH9: RADIATING SYSTEMS — MULTIPOLE FIELDS AND RADIATION
# ===================================================================

def ch09_dipole_radiation_pattern():
    """
    Compute and plot the angular radiation pattern of:
      (a) Electric dipole oriented along z
      (b) Magnetic dipole oriented along z
      (c) Electric quadrupole (Q_zz ≠ 0)

    All are normalized to unit maximum.
    """
    theta = np.linspace(0, np.pi, 200)
    phi = 0.0  # plot in xz-plane

    # --- Electric dipole: dP/dΩ ∝ sin²θ ---
    ed_pattern = np.sin(theta)**2

    # --- Magnetic dipole: same sin²θ about dipole axis ---
    md_pattern = np.sin(theta)**2

    # --- Electric quadrupole (Q_zz component only) ---
    eq_pattern = np.sin(theta)**2 * np.cos(theta)**2  # |n × Q(n)|² ~ sin²θ cos²θ

    # Normalize
    ed_pattern /= ed_pattern.max()
    md_pattern /= md_pattern.max()
    eq_pattern /= eq_pattern.max() if eq_pattern.max() > 0 else 1.0

    fig, axes = plt.subplots(1, 3, subplot_kw={'projection': 'polar'},
                             figsize=(12, 4))

    titles = [r'Electric Dipole $\sin^2\theta$',
              r'Magnetic Dipole $\sin^2\theta$',
              r'Electric Quadrupole $\sin^2\theta\cos^2\theta$']

    patterns = [ed_pattern, md_pattern, eq_pattern]
    colors = ['C0', 'C1', 'C2']

    for ax, pat, tit, col in zip(axes, patterns, titles, colors):
        ax.plot(theta, pat, color=col, lw=2)
        ax.fill(theta, pat, alpha=0.2, color=col)
        ax.set_title(tit, pad=15, fontsize=10)
        ax.set_ylim(0, 1.1)
        ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])

    fig.tight_layout()
    fig.savefig('ch09_dipole_radiation_patterns.png', dpi=150)
    plt.close(fig)
    print("[Ch9] Saved: ch09_dipole_radiation_patterns.png")

    return ed_pattern, md_pattern, eq_pattern


def ch09_half_wave_dipole():
    """
    Radiation pattern of a half-wave dipole (l = λ/2).
    Far-field E_θ ∝ cos(π/2 cosθ) / sinθ.
    """
    theta = np.linspace(0.001, np.pi - 0.001, 500)

    # Normalized field pattern
    F = np.cos(np.pi / 2 * np.cos(theta)) / np.sin(theta)
    F /= F.max()

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(6, 6))
    ax.plot(theta, F, 'C3', lw=2)
    ax.fill(theta, F, alpha=0.2, color='C3')
    ax.set_title(r'Half-Wave Dipole $E_\theta \propto \frac{\cos(\pi\cos\theta/2)}{\sin\theta}$',
                 pad=20, fontsize=10)
    ax.set_ylim(0, 1.1)
    fig.tight_layout()
    fig.savefig('ch09_half_wave_dipole.png', dpi=150)
    plt.close(fig)
    print("[Ch9] Saved: ch09_half_wave_dipole.png")
    return F


def ch09_linear_array_factor():
    """
    Array factor for N-element linear array.
    Plots |AF(θ)|² for different phase shifts δ.
    """
    N = 8
    d = 0.5  # wavelength spacing
    theta = np.linspace(0, np.pi, 1000)
    u = np.cos(theta)

    fig, axes = plt.subplots(1, 3, subplot_kw={'projection': 'polar'},
                             figsize=(12, 4))
    deltas = [0, 0.5, 1.0]  # δ in units of π
    labels = ['Broadside (δ=0)', 'δ=π/2', 'δ=π']

    for ax, delta_pi, lab in zip(axes, deltas, labels):
        delta = delta_pi * np.pi
        psi = 2 * np.pi * d * u + delta
        AF = np.sin(N * psi / 2) / np.sin(psi / 2 + 1e-12)
        AF[0] = N  # forward direction
        AF_pow = (AF / N)**2
        ax.plot(theta, AF_pow, lw=2)
        ax.set_title(lab, pad=15, fontsize=10)
        ax.set_ylim(0, 1.1)

    fig.tight_layout()
    fig.savefig('ch09_linear_array_factor.png', dpi=150)
    plt.close(fig)
    print("[Ch9] Saved: ch09_linear_array_factor.png")


def ch09_total_power_comparison():
    """
    Compare total radiated power scaling for ED, MD, EQ as a function
    of source size / wavelength.  Assumes p ~ m/c ~ Q/c so we can compare.
    """
    l_over_lambda = np.logspace(-3, 0, 100)
    k = 2 * np.pi / l_over_lambda  # proportional scaling

    # For a given source scale a, ED ∝ (a/λ)², MD ∝ (a/λ)^4, EQ ∝ (a/λ)^4
    # Relative scaling with size parameter x = 2π a/λ
    x = 2 * np.pi * l_over_lambda

    # Normalize to ED at x=0.01
    scale = x / 0.01
    P_ED = scale**2
    P_MD = scale**4
    P_EQ = scale**4

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.loglog(l_over_lambda, P_ED, 'C0-', lw=2, label='Electric Dipole')
    ax.loglog(l_over_lambda, P_MD, 'C1--', lw=2, label='Magnetic Dipole')
    ax.loglog(l_over_lambda, P_EQ, 'C2:', lw=2, label='Electric Quadrupole')
    ax.axvline(0.1, color='gray', ls='--', alpha=0.5)
    ax.annotate('Small source\n(d ≪ λ)', xy=(0.003, 1e8), fontsize=9)
    ax.set_xlabel('d / λ (source size / wavelength)')
    ax.set_ylabel('Relative Radiated Power (log)')
    ax.set_title('Multipole Radiation Power Scaling')
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig('ch09_power_comparison.png', dpi=150)
    plt.close(fig)
    print("[Ch9] Saved: ch09_power_comparison.png")


# ===================================================================
#  CH10: SCATTERING AND DIFFRACTION
# ===================================================================

def rayleigh_cross_section(wavelength, polarizability=1.0):
    """
    Rayleigh scattering cross section: σ = (8π/3) k⁴ |α|²
    Returns σ [m²] for given wavelength [m] and polarizability α.
    """
    k = 2 * np.pi / np.array(wavelength)
    return (8 * np.pi / 3) * k**4 * np.abs(polarizability)**2


def ch10_rayleigh_scattering():
    """
    Rayleigh scattering cross section vs wavelength.
    Demonstrates σ ∝ λ^{-4} (why the sky is blue).
    """
    lam = np.linspace(380e-9, 780e-9, 200)  # visible spectrum [m]
    sigma = rayleigh_cross_section(lam)

    fig, ax1 = plt.subplots(figsize=(8, 5))

    ax1.plot(lam * 1e9, sigma / sigma.max(), 'C0-', lw=2)
    ax1.set_xlabel('Wavelength λ [nm]')
    ax1.set_ylabel('Normalized Cross Section')
    ax1.set_title(r'Rayleigh Scattering: $\sigma \propto \lambda^{-4}$')
    ax1.grid(True, alpha=0.3)

    # Annotate blue / red
    ax1.axvline(450, color='blue', ls='--', alpha=0.5)
    ax1.axvline(650, color='red', ls='--', alpha=0.5)
    blue_val = sigma[np.argmin(np.abs(lam - 450e-9))] / sigma.max()
    red_val = sigma[np.argmin(np.abs(lam - 650e-9))] / sigma.max()
    ax1.annotate(f'Blue: {blue_val:.2f}',
                 xy=(450, 0.65), fontsize=9, color='blue')
    ax1.annotate(f'Red: {red_val:.2f}',
                 xy=(650, 0.25), fontsize=9, color='red')

    fig.tight_layout()
    fig.savefig('ch10_rayleigh_scattering.png', dpi=150)
    plt.close(fig)
    print("[Ch10] Saved: ch10_rayleigh_scattering.png")


def mie_coefficients(x, m):
    """
    Compute Mie scattering coefficients a_l, b_l for a sphere.
    Uses Ricatti-Bessel functions via scipy.special.

    Parameters:
        x : float — size parameter 2πa/λ
        m : complex — relative refractive index n_sphere / n_medium

    Returns:
        a_l, b_l : ndarray of Mie coefficients for l=1..L_max
    """
    # Number of terms needed (Wiscombe criterion)
    L_max = int(np.round(x + 4 * x**(1/3) + 2))

    # Ricatti-Bessel: ψ_l(ρ) = ρ j_l(ρ),  ξ_l(ρ) = ρ h_l^(1)(ρ) = ρ (j_l + i y_l)
    # Use scipy.special.spherical_jn / spherical_yn
    l_arr = np.arange(1, L_max + 1)

    # Evaluate at ρ = x and ρ = m*x
    j_x = special.spherical_jn(l_arr, x)
    y_x = special.spherical_yn(l_arr, x)
    j_mx = special.spherical_jn(l_arr, m * x)
    y_mx = special.spherical_yn(l_arr, m * x)

    psi_x = x * j_x
    psi_mx = (m * x) * j_mx
    xi_x = x * (j_x + 1j * y_x)

    # Derivatives via recurrence: ψ'_l(ρ) = ψ_{l-1}(ρ) - l/ρ ψ_l(ρ)
    # Need ψ_0, ψ_-1 for start
    j_x_lm1 = special.spherical_jn(l_arr - 1, x)
    j_mx_lm1 = special.spherical_jn(l_arr - 1, m * x)
    y_x_lm1 = special.spherical_yn(l_arr - 1, x)

    psi_x_deriv = x * j_x_lm1 - l_arr * j_x
    psi_mx_deriv = (m * x) * j_mx_lm1 - l_arr * j_mx
    xi_x_deriv = x * (j_x_lm1 + 1j * y_x_lm1) - l_arr * (j_x + 1j * y_x)

    # Mie coefficients
    a_l = (m * psi_mx * psi_x_deriv - psi_x * psi_mx_deriv) / \
          (m * psi_mx * xi_x_deriv - xi_x * psi_mx_deriv)

    b_l = (psi_mx * psi_x_deriv - m * psi_x * psi_mx_deriv) / \
          (psi_mx * xi_x_deriv - m * xi_x * psi_mx_deriv)

    return a_l, b_l


def ch10_mie_scattering():
    """
    Compute and plot Mie extinction efficiency Q_ext = σ_ext / (π a²)
    as a function of size parameter x for a dielectric sphere.
    """
    x_arr = np.logspace(-1, 1.6, 200)

    m_real = 1.5  # glass-like
    Q_ext_arr = []

    for x in x_arr:
        a_l, b_l = mie_coefficients(x, m_real)
        Q_ext = (2 / x**2) * np.sum((2 * np.arange(1, len(a_l) + 1) + 1)
                                     * np.real(a_l + b_l))
        Q_ext_arr.append(Q_ext)

    Q_ext_arr = np.array(Q_ext_arr)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogx(x_arr, Q_ext_arr, 'C0-', lw=2)
    ax.axhline(2.0, color='gray', ls='--', alpha=0.5,
               label=r'$Q_{\rm ext} \to 2$ (extinction paradox)')
    ax.set_xlabel('Size parameter $x = 2\\pi a / \\lambda$')
    ax.set_ylabel('Extinction efficiency $Q_{\\rm ext}$')
    ax.set_title(f'Mie Scattering: Dielectric Sphere ($m = {m_real}$)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig('ch10_mie_extinction.png', dpi=150)
    plt.close(fig)
    print("[Ch10] Saved: ch10_mie_extinction.png")

    # Also show Rayleigh regime (x ≪ 1) vs exact
    x_rayleigh = x_arr[x_arr < 0.3]
    rayleigh_limit = (8/3) * x_rayleigh**4 * ((m_real**2 - 1) / (m_real**2 + 2))**2

    fig2, ax2 = plt.subplots(figsize=(8, 5))
    ax2.loglog(x_arr, Q_ext_arr, 'C0-', lw=2, label='Mie exact')
    ax2.loglog(x_rayleigh, rayleigh_limit, 'C1--', lw=2, label='Rayleigh limit')
    ax2.set_xlabel('Size parameter $x$')
    ax2.set_ylabel('$Q_{\\rm scat}$')
    ax2.set_title('Mie vs Rayleigh: Small-Particle Limit')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    fig2.tight_layout()
    fig2.savefig('ch10_mie_vs_rayleigh.png', dpi=150)
    plt.close(fig2)
    print("[Ch10] Saved: ch10_mie_vs_rayleigh.png")


def ch10_fraunhofer_diffraction():
    """
    Fraunhofer diffraction patterns: rectangular and circular apertures.
    """
    # Rectangular aperture
    u = np.linspace(-5, 5, 500)
    v = np.linspace(-5, 5, 500)
    U, V = np.meshgrid(u, v)
    I_rect = (np.sinc(U / np.pi) * np.sinc(V / np.pi))**2  # sinc(x) = sin(πx)/(πx)

    # Circular aperture (Airy pattern)
    r = np.linspace(0, 10, 500)
    z = r
    J1 = special.jv(1, z)
    I_circ = np.where(r > 0.001, (2 * J1 / z)**2, 1.0)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Rectangular
    im1 = axes[0].imshow(I_rect, extent=[u.min(), u.max(), v.min(), v.max()],
                         cmap='inferno', origin='lower')
    axes[0].set_title(r'Rectangular Aperture: ${\rm sinc}^2(\alpha)\,{\rm sinc}^2(\beta)$')
    axes[0].set_xlabel(r'$ka\,\sin\theta_x / 2$')
    axes[0].set_ylabel(r'$kb\,\sin\theta_y / 2$')
    plt.colorbar(im1, ax=axes[0], shrink=0.8)

    # Circular
    axes[1].plot(r, I_circ, 'C0-', lw=2)
    # First null
    first_null = r[np.where(I_circ < 0.01)[0][0]]
    axes[1].axvline(first_null, color='red', ls='--', alpha=0.7)
    axes[1].annotate(f'First null\n$\\theta = 1.22\\lambda/D$',
                     xy=(first_null, 0.1), fontsize=9, color='red')
    axes[1].set_xlabel(r'$kD\,\sin\theta / 2$')
    axes[1].set_ylabel('Normalized Intensity')
    axes[1].set_title(r'Circular Aperture (Airy Pattern): $[2J_1(z)/z]^2$')
    axes[1].grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig('ch10_fraunhofer_diffraction.png', dpi=150)
    plt.close(fig)
    print("[Ch10] Saved: ch10_fraunhofer_diffraction.png")


# ===================================================================
#  CH11: SPECIAL THEORY OF RELATIVITY
# ===================================================================

def lorentz_boost_matrix(beta):
    """
    Return the 4×4 Lorentz boost matrix for velocity β = v/c along x.
    """
    gamma = 1 / np.sqrt(1 - beta**2)
    L = np.array([
        [gamma, -gamma * beta, 0, 0],
        [-gamma * beta, gamma, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    return L


def ch11_minkowski_diagram():
    """
    Draw a Minkowski spacetime diagram showing:
    - Light cone (45° lines)
    - Two inertial frames (S and S') with relative velocity β
    - Time dilation and length contraction
    """
    fig, ax = plt.subplots(figsize=(7, 7))

    beta = 0.6
    gamma = 1 / np.sqrt(1 - beta**2)

    # Axes
    ax.axhline(0, color='black', lw=0.5)
    ax.axvline(0, color='black', lw=0.5)

    # S axes labels
    ax.annotate('S: $x$', xy=(4, 0), fontsize=11)
    ax.annotate('S: $ct$', xy=(0, 4), fontsize=11)

    # Light cone
    ax.plot([-4, 4], [-4, 4], color='gray', ls='--', alpha=0.5, label='Light cone ($x=ct$)')
    ax.plot([-4, 4], [4, -4], color='gray', ls='--', alpha=0.5)

    # S' axes (boosted)
    slope = beta
    # ct' axis: x = β ct
    ax.plot([-4 * beta, 4 * beta], [-4, 4], 'C0-', lw=2, label=f"$S'$ ($\\beta={beta}$)")
    # x' axis: ct = β x
    ax.plot([-4, 4], [-4 * beta, 4 * beta], 'C0-', lw=2)

    ax.annotate("$S'$: $ct'$", xy=(4 * beta, 4), fontsize=11, color='C0')
    ax.annotate("$S'$: $x'$", xy=(4, 4 * beta), fontsize=11, color='C0')

    # Worldline of a particle at rest in S
    ax.axvline(2, color='C2', ls='-', alpha=0.7, lw=2, label='Particle at rest in S')
    ax.annotate('Worldline', xy=(2, 3.5), fontsize=9, color='C2')

    # Time dilation: proper time in S'
    t_prime = 3.0  # in S' units
    x_prime = 0.0
    # Transform to S
    # (ct', x') → (ct, x) using inverse boost (β → -β)
    L_inv = lorentz_boost_matrix(-beta)
    cosh = gamma
    sinh = gamma * beta
    ct_s = cosh * t_prime + sinh * x_prime
    x_s = sinh * t_prime + cosh * x_prime

    ax.plot([0, x_s], [0, ct_s], 'C3o-', lw=1.5, markersize=4)
    ax.annotate(f'$\\Delta\\tau = {t_prime}$\n$\\Delta t = \\gamma\\Delta\\tau = {ct_s:.1f}$',
                xy=(x_s + 0.2, ct_s), fontsize=9, color='C3')

    # Length contraction: a rod of proper length L0 at rest in S'
    L0 = 2.0
    x1_prime = 0.0
    x2_prime = L0
    # Simultaneous in S' → ct' = constant
    ct_prime_const = 1.0
    L_inv11 = gamma
    # In S coordinates: ct = γ ct' + γβ x' (but these will be at different times in S)
    x1_s = gamma * (x1_prime + beta * ct_prime_const)
    x2_s = gamma * (x2_prime + beta * ct_prime_const)
    ct_s1 = gamma * (ct_prime_const + beta * x1_prime)
    ct_s2 = gamma * (ct_prime_const + beta * x2_prime)

    # Show the rod ends
    ax.plot([x1_s, x2_s], [ct_s1, ct_s2], 'mo-', lw=2, markersize=4)
    ax.annotate(f"Rod $L_0={L0}$ in $S'$\nContracted in $S$",
                xy=((x1_s + x2_s) / 2, (ct_s1 + ct_s2) / 2 + 0.3),
                fontsize=9, color='m')

    ax.set_xlim(-1, 4)
    ax.set_ylim(-1, 4)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$ct$')
    ax.set_title('Minkowski Diagram: Lorentz Transformation')
    ax.legend(loc='upper left', fontsize=9)
    ax.set_aspect('equal')
    fig.tight_layout()
    fig.savefig('ch11_minkowski_diagram.png', dpi=150)
    plt.close(fig)
    print("[Ch11] Saved: ch11_minkowski_diagram.png")


def ch11_headlight_effect():
    """
    Relativistic headlight (beaming) effect:
    An isotropic emitter in its rest frame appears forward-focused
    in the lab frame with dP/dΩ ∝ 1 / [γ²(1 - β cosθ)²].
    """
    theta = np.linspace(0, np.pi, 500)

    fig, axes = plt.subplots(1, 3, subplot_kw={'projection': 'polar'},
                             figsize=(12, 4))
    betas = [0.3, 0.7, 0.9]
    colors = ['C0', 'C1', 'C2']

    for ax, beta, col in zip(axes, betas, colors):
        gamma = 1 / np.sqrt(1 - beta**2)
        intensity = 1 / (gamma**2 * (1 - beta * np.cos(theta))**2)
        intensity /= intensity.max()

        ax.plot(theta, intensity, col, lw=2)
        ax.fill(theta, intensity, alpha=0.2, color=col)
        ax.set_title(f'$\\beta = {beta}$\n$\\gamma = {gamma:.1f}$', pad=15, fontsize=11)
        ax.set_ylim(0, 1.1)

    fig.suptitle('Relativistic Headlight Effect', fontsize=13, y=1.05)
    fig.tight_layout()
    fig.savefig('ch11_headlight_effect.png', dpi=150)
    plt.close(fig)
    print("[Ch11] Saved: ch11_headlight_effect.png")


def ch11_lorentz_contraction_visualization():
    """
    Visualize Lorentz contraction of a moving object (e.g., a grid).
    A square grid in its rest frame is transformed to the lab frame.
    """
    # Grid points in rest frame
    N = 11
    x_rest, y_rest = np.meshgrid(np.linspace(-1, 1, N), np.linspace(-1, 1, N))
    t_rest = np.zeros_like(x_rest)  # simultaneous in rest frame

    beta = 0.8
    gamma = 1 / np.sqrt(1 - beta**2)

    # Transform to lab frame (boost along x)
    x_lab = gamma * (x_rest + beta * c * t_rest)
    # t_lab = gamma * (t_rest + beta * x_rest / c)  # not simultaneous!
    # For a snapshot, we pick events that ARE simultaneous in lab frame.
    # Better approach: take the set of worldlines and intersect with t_lab = 0.
    # For a simple visualization, just show the Lorentz-contracted coordinates
    # (the lines of constant x' map to slanted lines in S).

    # Simpler: just show a contracted shape
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Rest frame: circle
    theta = np.linspace(0, 2 * np.pi, 200)
    R = 1.0
    axes[0].plot(R * np.cos(theta), R * np.sin(theta), 'C0-', lw=2)
    axes[0].set_xlim(-1.5, 1.5)
    axes[0].set_ylim(-1.5, 1.5)
    axes[0].set_aspect('equal')
    axes[0].set_title(f"Rest Frame S': circular object ($R={R}$)")
    axes[0].grid(True, alpha=0.3)

    # Lab frame: contracted along x
    axes[1].plot(R * np.cos(theta) / gamma, R * np.sin(theta), 'C1-', lw=2)
    axes[1].set_xlim(-1.5, 1.5)
    axes[1].set_ylim(-1.5, 1.5)
    axes[1].set_aspect('equal')
    axes[1].set_title(f"Lab Frame S: $\\beta = {beta}$, $\\gamma = {gamma:.1f}$\n"
                      f"Contracted: $R'_\\parallel = R/\\gamma = {R/gamma:.2f}$")
    axes[1].grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig('ch11_lorentz_contraction.png', dpi=150)
    plt.close(fig)
    print("[Ch11] Saved: ch11_lorentz_contraction.png")


# ===================================================================
#  CH12: DYNAMICS OF RELATIVISTIC PARTICLES
# ===================================================================

def ch12_relativistic_cyclotron():
    """
    Relativistic cyclotron motion of an electron in uniform B field.
    Shows that the orbital frequency decreases with energy:
    ω_c = qB / (γ m)
    """
    B = 1.0  # 1 Tesla
    gamma_vals = np.linspace(1, 10, 200)
    omega_c = qe * B / (gamma_vals * me)  # [rad/s]

    fig, ax1 = plt.subplots(figsize=(8, 5))

    ax1.plot(gamma_vals, omega_c / 1e9, 'C0-', lw=2)
    ax1.set_xlabel('Lorentz factor $\\gamma$')
    ax1.set_ylabel('Cyclotron frequency $\\omega_c$ [GHz]')
    ax1.set_title(f'Relativistic Cyclotron Frequency ($B = {B}$ T, electron)')
    ax1.grid(True, alpha=0.3)

    # Also show radius
    ax2 = ax1.twinx()
    v = c * np.sqrt(1 - 1 / gamma_vals**2)
    r = gamma_vals * me * v / (qe * B)  # [m]
    ax2.plot(gamma_vals, r, 'C1--', lw=2)
    ax2.set_ylabel('Orbit radius $r$ [m]', color='C1')
    ax2.tick_params(axis='y', labelcolor='C1')

    fig.tight_layout()
    fig.savefig('ch12_relativistic_cyclotron.png', dpi=150)
    plt.close(fig)
    print("[Ch12] Saved: ch12_relativistic_cyclotron.png")

    return gamma_vals, omega_c, r


def ch12_exb_drift():
    """
    Compute and plot E×B drift trajectories for a charged particle.
    """
    # Parameters
    B0 = np.array([0, 0, 1.0])  # B along z
    E0 = np.array([0.5, 0, 0])  # E along x (E < cB for physical drift)
    q = qe
    m = me

    # Drift velocity
    v_d = np.cross(E0, B0) / np.linalg.norm(B0)**2
    print(f"[Ch12] E×B drift velocity: v_d = ({v_d[0]:.2e}, {v_d[1]:.2e}, {v_d[2]:.2e}) m/s")

    # Initial conditions: particle at rest at origin
    x0 = np.array([0.0, 0.0, 0.0])
    v0 = np.array([0.0, 0.0, 0.0])

    def rhs(t, y):
        """d(y)/dt for a relativistic particle in E+B fields."""
        x = y[0:3]
        v = y[3:6]
        gamma = 1 / np.sqrt(1 - np.dot(v, v) / c**2)
        # Lorentz force
        a = (q / (gamma * m)) * (E0 + np.cross(v, B0))
        return np.concatenate([v, a])

    # Integrate
    t_span = (0, 5e-9)  # 5 ns
    t_eval = np.linspace(*t_span, 5000)
    sol = integrate.solve_ivp(rhs, t_span, np.concatenate([x0, v0]),
                              t_eval=t_eval, method='DOP853',
                              rtol=1e-10, atol=1e-12)

    x = sol.y[0, :]
    y = sol.y[1, :]
    vx = sol.y[3, :]
    vy = sol.y[4, :]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # xy-trajectory
    axes[0].plot(x * 1e3, y * 1e3, 'C0-', lw=1.5)
    axes[0].plot(x[0] * 1e3, y[0] * 1e3, 'go', label='Start')
    # Mark drift direction
    axes[0].annotate(r'E × B drift', xy=(x[-1] * 1e3, y[-1] * 1e3),
                     fontsize=9)
    axes[0].set_xlabel('x [mm]')
    axes[0].set_ylabel('y [mm]')
    axes[0].set_title('E×B Drift: Trochoidal Trajectory')
    axes[0].axis('equal')
    axes[0].grid(True, alpha=0.3)

    # Velocity components
    axes[1].plot(t_eval * 1e9, vx, label='$v_x$', lw=1.5)
    axes[1].plot(t_eval * 1e9, vy, label='$v_y$', lw=1.5)
    axes[1].axhline(v_d[1], color='gray', ls='--', alpha=0.7,
                    label=f'$v_d = {v_d[1]:.2e}$ m/s')
    axes[1].set_xlabel('Time [ns]')
    axes[1].set_ylabel('Velocity [m/s]')
    axes[1].set_title('Velocity Components')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig('ch12_exb_drift.png', dpi=150)
    plt.close(fig)
    print("[Ch12] Saved: ch12_exb_drift.png")


def ch12_synchrotron_spectrum():
    """
    Synchrotron radiation spectrum: universal formula
    dP/dω ∝ F(ω/ω_c) where F(x) = x ∫_x^∞ K_{5/3}(ξ) dξ
    """
    x = np.logspace(-3, 2, 500)

    # F(x) = x * ∫_x^∞ K_{5/3}(ξ) dξ
    # Use scipy's integrate.quad for each point
    def F_of_x(xval):
        result, _ = integrate.quad(lambda xi: special.kv(5/3, xi), xval, np.inf)
        return xval * result

    F_vals = np.array([F_of_x(xv) for xv in x])

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.loglog(x, F_vals, 'C0-', lw=2)
    # Asymptotes
    ax.loglog(x[x < 0.05], 2.15 * x[x < 0.05]**(1/3), 'C1--', lw=1.5,
              alpha=0.7, label=r'$F(x) \propto x^{1/3}$ (low $x$)')
    ax.loglog(x[x > 10], 0.78 * np.sqrt(x[x > 10]) * np.exp(-x[x > 10]),
              'C2--', lw=1.5, alpha=0.7,
              label=r'$F(x) \propto \sqrt{x}\,e^{-x}$ (high $x$)')

    ax.set_xlabel(r'$x = \omega / \omega_c$')
    ax.set_ylabel(r'$F(x) = x \int_x^\infty K_{5/3}(\xi)\,d\xi$')
    ax.set_title('Synchrotron Radiation Universal Spectrum')
    ax.legend()
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig('ch12_synchrotron_spectrum.png', dpi=150)
    plt.close(fig)
    print("[Ch12] Saved: ch12_synchrotron_spectrum.png")


def ch12_Compton_scattering():
    """
    Compare Thomson (classical) vs Klein-Nishina (quantum) cross sections
    as a function of incident photon energy.
    """
    # Photon energy range [eV]
    E_photon = np.logspace(0, 8, 300)  # 1 eV to 100 MeV
    E_photon_J = E_photon * qe

    # Thomson cross section (constant)
    sigma_T = 8 * np.pi * r0**2 / 3

    # Klein-Nishina total cross section
    # σ_KN = σ_T * 3/4 * [ (1+y)/y³ * (2y(1+y)/(1+2y) - ln(1+2y)) + ln(1+2y)/(2y) - (1+3y)/(1+2y)² ]
    # where y = ħω / mc²
    y = E_photon * qe / (me * c**2)
    sigma_KN = np.zeros_like(y)

    for i, yi in enumerate(y):
        if yi < 1e-6:
            sigma_KN[i] = sigma_T
        else:
            term1 = (1 + yi) / yi**3
            term2 = (2 * yi * (1 + yi)) / (1 + 2 * yi)
            term3 = np.log(1 + 2 * yi)
            term4 = term3 / (2 * yi)
            term5 = (1 + 3 * yi) / (1 + 2 * yi)**2
            sigma_KN[i] = sigma_T * 3/4 * (term1 * (term2 - term3) + term4 - term5)

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.loglog(E_photon, sigma_T * np.ones_like(E_photon),
              'C1--', lw=1.5, label='Thomson: $\\sigma_T = 6.65 \\times 10^{-29}$ m²')
    ax.loglog(E_photon, sigma_KN, 'C0-', lw=2, label='Klein-Nishina')
    ax.axvline(me * c**2 / qe, color='gray', ls=':', alpha=0.5,
               label=f'$mc^2 = {me*c**2/qe:.1f}$ eV')

    ax.set_xlabel('Photon Energy [eV]')
    ax.set_ylabel('Cross Section [m²]')
    ax.set_title('Compton Scattering: Thomson vs Klein-Nishina')
    ax.legend()
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig('ch12_compton_scattering.png', dpi=150)
    plt.close(fig)
    print("[Ch12] Saved: ch12_compton_scattering.png")


# ===================================================================
#  MAIN: Run all examples
# ===================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Jackson Ch9–12 Computational Examples")
    print("=" * 60)

    print("\n--- Chapter 9: Radiating Systems ---")
    ch09_dipole_radiation_pattern()
    ch09_half_wave_dipole()
    ch09_linear_array_factor()
    ch09_total_power_comparison()

    print("\n--- Chapter 10: Scattering & Diffraction ---")
    ch10_rayleigh_scattering()
    ch10_mie_scattering()
    ch10_fraunhofer_diffraction()

    print("\n--- Chapter 11: Special Relativity ---")
    ch11_minkowski_diagram()
    ch11_headlight_effect()
    ch11_lorentz_contraction_visualization()

    print("\n--- Chapter 12: Relativistic Particle Dynamics ---")
    ch12_relativistic_cyclotron()
    ch12_exb_drift()
    ch12_synchrotron_spectrum()
    ch12_Compton_scattering()

    print("\n" + "=" * 60)
    print("All examples completed successfully.")
    print("=" * 60)
