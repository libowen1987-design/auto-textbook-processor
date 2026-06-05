r"""
jackson_ch01-04_computational.py
==================================
Computational examples from Jackson, Introduction to Electrodynamics, 4th Ed.
Chapters 1–4: Electrostatics and Magnetostatics

Coverage
--------
- coulomb_field()         : Point-charge Coulomb field E = k_e * q * r̂ / r²
- gauss_law()             : Verify ∮ E·dA = Q/ε₀ for spherical surfaces
- boundary_conditions()   : Conductor surface: E⊥ = σ/ε₀, E∥ = 0
- method_of_images()      : Infinite grounded plane + point charge (image method)
- multipole_expansion()   : Electric potential multipole expansion for r >> r'

Physical constants from scipy.constants:
    ε₀, μ₀, c, e, k = 1/(4π·ε₀)

Authors: Computational Electromagnetics Lab
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate, special
from scipy.constants import epsilon_0 as eps0, pi

# Convenience constant: Coulomb constant k_e = 1/(4π·ε₀)
k_e = 1.0 / (4.0 * pi * eps0)


# ---------------------------------------------------------------------------
# 1. COULOMB FIELD
# ---------------------------------------------------------------------------

def coulomb_field(q, r_obs, r_source=(0.0, 0.0, 0.0)):
    r"""
    Electric field of a point charge at position r_source evaluated at r_obs.

    Parameters
    ----------
    q : float
        Point charge in coulombs.
    r_obs : array_like, shape (3,)
        Observation position [x, y, z] in metres.
    r_source : array_like, shape (3,)
        Source charge position [x, y, z] in metres.

    Returns
    -------
    E : ndarray, shape (3,)
        Electric field vector in V/m.

    Formula
    -------
    \mathbf{E} = k_e · q · \mathbf{r̂} / r²
    where \mathbf{r} = r_obs - r_source.

    Example
    -------
    >>> E = coulomb_field(1e-9, np.array([1.0, 0.0, 0.0]))
    >>> print(f"|E| = {np.linalg.norm(E):.4e} V/m")
    """
    r_vec = np.asarray(r_obs) - np.asarray(r_source)
    r_mag = np.linalg.norm(r_vec)
    if r_mag == 0:
        raise ValueError("Observation point cannot coincide with source charge.")
    r_hat = r_vec / r_mag
    E_mag = k_e * abs(q) / r_mag**2
    # Direction: outward for positive q, inward for negative q
    sign = 1 if q > 0 else -1
    E = sign * E_mag * r_hat
    return E


def demo_coulomb_field():
    """Plot the Coulomb field of a point charge in the x–y plane."""
    q = 1e-9          # 1 nC
    x = np.linspace(-2, 2, 21)
    y = np.linspace(-2, 2, 21)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)

    Ex = np.zeros_like(X)
    Ey = np.zeros_like(Y)

    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            E = coulomb_field(q, np.array([X[i, j], Y[i, j], 0.0]))
            Ex[i, j] = E[0]
            Ey[i, j] = E[1]

    plt.figure(figsize=(7, 6))
    plt.streamplot(x, y, Ex, Ey, color=np.sqrt(Ex**2 + Ey**2),
                   cmap='plasma', density=1.5)
    plt.gca().add_patch(plt.Circle((0, 0), 0.08, color='red', zorder=5))
    plt.text(0, 0, '+q', ha='center', va='center', fontsize=12,
             color='white', fontweight='bold')
    plt.title(r"Electric field of a point charge ($q = 1\,$nC)")
    plt.xlabel(r"$x$ (m)")
    plt.ylabel(r"$y$ (m)")
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig("coulomb_field.png", dpi=150)
    plt.show()
    print("[demo] Coulomb field plot saved as coulomb_field.png")


# ---------------------------------------------------------------------------
# 2. GAUSS'S LAW
# ---------------------------------------------------------------------------

def gauss_law(q_enclosed, R_sphere):
    r"""
    Verify Gauss's law: \oint \mathbf{E}·d\mathbf{A} = Q_enclosed / ε₀.

    For a point charge q at the origin, the exact field on a spherical
    surface of radius R is E = k_e·q·r̂/R², so the integral is trivial.
    Here we demonstrate numerical integration over the sphere surface.

    Parameters
    ----------
    q_enclosed : float
        Charge enclosed in coulombs.
    R_sphere : float
        Radius of the spherical Gaussian surface in metres.

    Returns
    -------
    integral : float
        Numerical value of \oint \mathbf{E}·d\mathbf{A} in V·m ( = J/C·m )
    theoretical : float
        Exact value Q_enclosed / ε₀.

    Formula
    -------
    \oint_S \mathbf{E}·d\mathbf{A} = \frac{Q_{\text{enc}}}{\varepsilon_0}
    """
    # Parametric sphere: θ ∈ [0,π], φ ∈ [0,2π]
    n_theta = 30
    n_phi   = 60
    theta = np.linspace(0, np.pi, n_theta)
    phi   = np.linspace(0, 2*np.pi, n_phi)
    TH, PH = np.meshgrid(theta, phi, indexing='ij')

    # Surface element: dA = R² sinθ dθ dφ r̂
    x = R_sphere * np.sin(TH) * np.cos(PH)
    y = R_sphere * np.sin(TH) * np.sin(PH)
    z = R_sphere * np.cos(TH)

    # Field at each surface point
    r_surf = np.stack([x, y, z], axis=-1)          # (nθ, nφ, 3)
    r_mag  = np.linalg.norm(r_surf, axis=-1)        # (nθ, n_phi)
    E_surf = (k_e * q_enclosed / r_mag**2)[:, :, None] * (r_surf / r_mag[:, :, None])

    # Normal vector is r̂, dA = R² sinθ dθ dφ
    dA_mag = R_sphere**2 * np.sin(TH)
    n_hat  = r_surf / r_mag[:, :, None]

    # Dot product E·n
    E_dot_n = np.sum(E_surf * n_hat, axis=-1)       # (nθ, n_phi)

    # Numerical integration over sphere
    integrand = E_dot_n * dA_mag
    # Integrate over theta using Simpson's rule via trapezoid on dense grid
    theta_dense = np.linspace(0, np.pi, 200)
    f_dense = np.interp(theta_dense, theta, np.trapezoid(integrand, phi, axis=1))
    integral = integrate.simpson(f_dense, theta_dense)

    theoretical = q_enclosed / eps0
    return integral, theoretical


def demo_gauss_law():
    q = 5e-9    # 5 nC
    R = 0.5     # 50 cm sphere
    num, exact = gauss_law(q, R)
    print(f"Gauss's law verification:")
    print(f"  Q_enc = {q*1e9:.1f} nC,  R = {R*100:.0f} cm")
    print(f"  Numerical ∮E·dA = {num:.6e} V·m")
    print(f"  Theoretical Q/ε₀ = {exact:.6e} V·m")
    print(f"  Relative error  = {abs(num-exact)/abs(exact):.2e}")
    return abs(num - exact) / abs(exact)


# ---------------------------------------------------------------------------
# 3. BOUNDARY CONDITIONS AT A CONDUCTOR SURFACE
# ---------------------------------------------------------------------------

def boundary_conditions(sigma, eps=eps0):
    r"""
    Compute the boundary conditions at the surface of a perfect conductor.

    Parameters
    ----------
    sigma : float
        Surface charge density on the conductor in C/m².
    eps : float
        Permittivity of the medium (default: ε₀).

    Returns
    -------
    E_normal : float
        Normal component of E just outside: E_⊥ = σ/ε.
    E_tangential : float
        Tangential component (zero for a perfect conductor).

    Formula
    -------
    E_⊥ = σ / ε₀     (just outside conductor surface)
    E_∥ = 0           (perfect conductor, no tangential field)

    Example
    -------
    >>> E_n, E_t = boundary_conditions(sigma=1e-5)
    >>> print(f"E_normal = {E_n:.3e} V/m")
    """
    E_normal     = sigma / eps
    E_tangential = 0.0
    return E_normal, E_tangential


def demo_boundary_conditions():
    sigmas = np.linspace(1e-7, 1e-4, 50)   # C/m²
    E_normals = sigma / eps0

    plt.figure(figsize=(8, 4))
    plt.plot(sigmas * 1e6, E_normals, 'b-', lw=2)
    plt.xlabel(r"Surface charge density $\sigma$ (μC/m²)")
    plt.ylabel(r"$E_\perp$ just outside (V/m)")
    plt.title(r"Boundary condition: $E_\perp = \sigma / \varepsilon_0$")
    plt.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.savefig("boundary_condition.png", dpi=150)
    plt.show()
    print("[demo] Boundary condition plot saved as boundary_condition.png")


# ---------------------------------------------------------------------------
# 4. METHOD OF IMAGES — Infinite Grounded Plane
# ---------------------------------------------------------------------------

def method_of_images(q, d, x_obs, y_obs):
    r"""
    Method of images for a point charge q at (0, 0, d) above an infinite
    grounded conducting plane at z = 0.

    The image charge q' = -q is placed at (0, 0, -d).
    The potential at (x_obs, y_obs, z_obs) is computed from both charges.

    Parameters
    ----------
    q : float
        Real point charge in coulombs.
    d : float
        Height above the conducting plane in metres.
    x_obs, y_obs : array_like
        Observation coordinates in the plane z = 0.

    Returns
    -------
    phi : ndarray
        Electric potential in volts at each observation point.

    Formula
    -------
    \phi(x,y,0) = k_e·q / √(x²+y²+d²)  +  k_e·q' / √(x²+y²+d²)

    Example
    -------
    >>> phi = method_of_images(1e-9, 0.5, np.linspace(-2,2,50), 0.0)
    """
    # Ensure arrays
    x_obs = np.asarray(x_obs)
    y_obs = np.asarray(y_obs)

    # Grid
    shape = np.broadcast(x_obs, y_obs).shape
    x = np.broadcast_to(x_obs, shape).astype(float)
    y = np.broadcast_to(y_obs, shape).astype(float)
    z = np.zeros_like(x)

    # Distance from real charge (0, 0, d)
    r_real = np.sqrt(x**2 + y**2 + d**2)
    # Distance from image charge (0, 0, -d)
    r_img  = np.sqrt(x**2 + y**2 + d**2)   # same z-coordinate magnitude

    phi = k_e * q / r_real + k_e * (-q) / r_img
    return phi


def demo_method_of_images():
    q = 1e-9
    d = 0.5

    x = np.linspace(-2, 2, 101)
    y = np.linspace(-2, 2, 101)
    X, Y = np.meshgrid(x, y)
    PHI = method_of_images(q, d, X, Y)

    plt.figure(figsize=(7, 6))
    levels = np.linspace(-500, 500, 41)
    cs = plt.contourf(X, Y, PHI * 1e9, levels=levels, cmap='RdBu_r')
    plt.colorbar(cs, label=r"Potential $\phi$ (mV)")
    # Ground plane edge
    plt.axhline(0, color='black', lw=2, label='Grounded plane (z=0)')
    plt.text(0.05, 0.02, r'Conducting plane', transform=plt.gca().transAxes)
    plt.plot(0, d, 'r*', markersize=14, label=r'+q at $z=d$')
    plt.plot(0, -d, 'b*', markersize=14, label=r'Image $-q$ at $z=-d$')
    plt.xlabel(r"$x$ (m)")
    plt.ylabel(r"$y$ (m)")
    plt.title("Method of Images: Point Charge above Grounded Plane")
    plt.legend()
    plt.tight_layout()
    plt.savefig("method_of_images.png", dpi=150)
    plt.show()
    print("[demo] Method of images plot saved as method_of_images.png")


# ---------------------------------------------------------------------------
# 5. MULTIPOLE EXPANSION OF THE ELECTRIC POTENTIAL
# ---------------------------------------------------------------------------

def multipole_expansion(r, charges, positions):
    r"""
    Compute the multipole expansion of the electric potential φ(r) for a
    charge distribution at observation distance |r|.

    The expansion to leading (monopole) order is:
        φ(r) ≈ k_e · Q_total / r

    The dipole term:
        φ_dipole ≈ k_e · \mathbf{p}·\mathbf{r̂} / r²
    where \mathbf{p} = Σ q_i·\mathbf{r}_i

    Parameters
    ----------
    r : ndarray, shape (3,)
        Observation position (far-field, |r| >> all source positions).
    charges : array_like
        Array of charges in coulombs.
    positions : ndarray, shape (n,3)
        Positions of each charge.

    Returns
    -------
    phi_monopole : float
        Monopole term: k_e · Q_total / |r|
    phi_dipole : float
        Dipole term: k_e · \mathbf{p}·\mathbf{r̂} / r²
    p_vec : ndarray
        Dipole moment vector.

    Example
    -------
    >>> q1, q2 = 1e-9, -1e-9
    >>> r1 = np.array([0.0, 0.0, 0.01])
    >>> r2 = np.array([0.0, 0.0, -0.01])
    >>> phi_m, phi_d, p = multipole_expansion(
    ...     np.array([1.0, 0.0, 0.0]), [q1, q2], [r1, r2])
    >>> print(f"Monopole: {phi_m:.3e}, Dipole: {phi_d:.3e} V")
    """
    charges   = np.asarray(charges)
    positions = np.asarray(positions)

    r_vec  = np.asarray(r)
    r_mag  = np.linalg.norm(r_vec)
    r_hat  = r_vec / r_mag

    # Monopole
    Q_total = np.sum(charges)
    phi_monopole = k_e * Q_total / r_mag

    # Dipole moment p = Σ q_i r_i
    p_vec = np.sum(charges[:, None] * positions, axis=0)
    phi_dipole = k_e * np.dot(p_vec, r_hat) / r_mag**2

    return phi_monopole, phi_dipole, p_vec


def demo_multipole_expansion():
    # Two equal-and-opposite charges separated by 1 mm → pure dipole
    q  = 1e-12       # 1 pC
    d  = 0.0005      # 0.5 mm each side from origin
    charges   = np.array([q, -q])
    positions = np.array([[0.0, 0.0, d], [0.0, 0.0, -d]])

    # Evaluate along x-axis
    x_vals = np.linspace(0.1, 5.0, 50)   # 10 cm to 5 m
    r_obs = np.stack([x_vals, np.zeros_like(x_vals), np.zeros_like(x_vals)], axis=1)

    phi_m = np.zeros_like(x_vals)
    phi_d = np.zeros_like(x_vals)
    for i, r in enumerate(r_obs):
        m, d, _ = multipole_expansion(r, charges, positions)
        phi_m[i] = m
        phi_d[i] = d

    phi_total = phi_m + phi_d

    plt.figure(figsize=(9, 5))
    plt.plot(x_vals, phi_total * 1e9, 'b-', lw=2, label=r'Full $\phi$ (mono+dipole)')
    plt.plot(x_vals, phi_m * 1e9, 'g--', lw=1.5, label=r'Monopole only')
    plt.plot(x_vals, phi_d * 1e9, 'r:', lw=1.5, label=r'Dipole only')
    plt.xlabel(r"Observation distance $r$ (m)")
    plt.ylabel(r"Potential $\phi$ (mV)")
    plt.title("Multipole Expansion: Pure Dipole Along $x$-Axis")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("multipole_expansion.png", dpi=150)
    plt.show()
    print("[demo] Multipolar expansion plot saved as multipole_expansion.png")


# ---------------------------------------------------------------------------
# MAIN / VALIDATION
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("Jackson Ch 01-04: Computational Electrostatics")
    print("=" * 60)

    # 1. Coulomb field
    E = coulomb_field(1e-9, np.array([1.0, 0.0, 0.0]))
    print(f"\n[coulomb_field] q=1nC at (1,0,0)m: E = {E}")

    # Verify E = kq/r² = 8.989e9 * 1e-9 / 1² = 8.989 V/m
    E_exact = k_e * 1e-9 / 1.0**2
    print(f"[coulomb_field] expected |E| = {E_exact:.3f} V/m,  got {np.linalg.norm(E):.3f} V/m")

    # 2. Gauss's law
    err = demo_gauss_law()
    print(f"\n[gauss_law] relative error: {err:.2e}  (target < 1e-6)")

    # 3. Boundary conditions
    E_n, E_t = boundary_conditions(sigma=1e-5)
    print(f"\n[boundary_conditions] σ=1e-5 C/m²:")
    print(f"  E_normal = {E_n:.3e} V/m,  E_tangential = {E_t:.1f} V/m")

    # 4. Method of images
    phi0 = method_of_images(1e-9, 0.5, 0.0, 0.0)
    # At (0,0) the potential is infinite (singular), but at a small offset:
    phi_pt = method_of_images(1e-9, 0.5, 0.1, 0.0)
    print(f"\n[method_of_images] φ at (0.1,0,0)m: {phi_pt*1e3:.3f} mV")

    # 5. Multipolar expansion
    charges   = np.array([1e-12, -1e-12])
    positions = np.array([[0.0, 0.0, 5e-4], [0.0, 0.0, -5e-4]])
    r_far     = np.array([1.0, 0.0, 0.0])
    phi_m, phi_d, p = multipole_expansion(r_far, charges, positions)
    print(f"\n[multipole_expansion] p = {p} C·m")
    print(f"  φ_monopole = {phi_m:.3e} V,  φ_dipole = {phi_d:.3e} V")

    # Plots (suppressed in headless CI, but callable)
    # demo_coulomb_field()
    # demo_boundary_conditions()
    # demo_method_of_images()
    # demo_multipole_expansion()

    print("\n[ALL DEMOS COMPLETE]")
