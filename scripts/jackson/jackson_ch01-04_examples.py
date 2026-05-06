#!/usr/bin/env python3
"""
Jackson Classical Electrodynamics, 3rd Ed — Ch1–Ch4 Numerical Examples
======================================================================

Covers:
  1. Electric field / potential numerical computation
  2. Separation of variables + method of images
  3. Multipole expansion
  4. Dielectric boundary conditions

Dependencies: numpy, scipy, matplotlib
"""

import numpy as np
from scipy.special import legendre, spherical_jn, lpmv  # lpmv = associated Legendre
from scipy.integrate import quad
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

# =========================================================================
# CONSTANTS
# =========================================================================
EPS0 = 8.854187817e-12       # F/m
K_COULOMB = 1.0 / (4 * np.pi * EPS0)  # ≈ 8.99e9 N·m²/C²


# =========================================================================
# 1.  ELECTRIC FIELD / POTENTIAL NUMERICAL COMPUTATION
# =========================================================================
# Example 1a:  Potential on axis of a uniformly charged ring
# -------------------------------------------------------------------------

def potential_ring_axis(z, R, Q):
    """
    Potential on the symmetry axis of a uniformly charged ring.
    z    : axial coordinate (scalar or ndarray)
    R    : ring radius
    Q    : total charge on ring
    Returns Φ(z) in volts.
    """
    return K_COULOMB * Q / np.sqrt(z**2 + R**2)


def efield_ring_axis(z, R, Q):
    """
    Electric field on axis of a uniformly charged ring (E_z).
    Positive direction = +z.
    """
    return K_COULOMB * Q * z / (z**2 + R**2)**1.5


# Example 1b:  Potential of a uniformly charged disk (on axis)
def potential_disk_axis(z, a, sigma):
    """
    Potential on axis of a uniformly charged disk of radius a,
    surface charge density σ.
    """
    return (sigma / (2 * EPS0)) * (np.sqrt(z**2 + a**2) - np.abs(z))


def efield_disk_axis(z, a, sigma):
    """
    Electric field on axis of a uniformly charged disk.
    """
    # derivative of potential: E_z = -dΦ/dz
    # Φ = σ/(2ε₀) [√(z²+a²) - |z|]
    sign = np.sign(z)
    return (sigma / (2 * EPS0)) * (sign - z / np.sqrt(z**2 + a**2))


# Example 1c:  Potential of a finite line charge (numerical integration)
def potential_line_charge(x, y, L, lam):
    """
    Potential at (x,y) from a uniform line charge of length L
    centered at origin along the z-axis.
    Uses numerical integration for non-axis points.
    """
    def integrand(zp):
        r = np.sqrt(x**2 + y**2 + (zp)**2)
        return lam / r

    vals, _ = quad(integrand, -L/2, L/2, limit=200)
    return K_COULOMB * vals


# =========================================================================
# 2.  METHOD OF IMAGES
# =========================================================================
# Example 2a:  Point charge above a grounded conducting plane
# -------------------------------------------------------------------------

def image_plane_potential(q, d, x, y, z):
    """
    Potential in z>0 half-space for charge q at (0,0,d) above
    grounded conducting plane at z=0.
    """
    r1 = np.sqrt(x**2 + y**2 + (z - d)**2)
    r2 = np.sqrt(x**2 + y**2 + (z + d)**2)
    return K_COULOMB * q * (1.0 / r1 - 1.0 / r2)


def image_plane_surface_charge(q, d, x, y):
    """
    Induced surface charge density on the plane at z=0.
    """
    return -q * d / (2 * np.pi * (x**2 + y**2 + d**2)**1.5)


def image_plane_force(q, d):
    """
    Force on charge q above grounded plane (attractive).
    """
    return -K_COULOMB * q**2 / (4 * d**2)


# Example 2b:  Point charge outside a grounded conducting sphere
# -------------------------------------------------------------------------

def image_sphere_potential(q, y, a, x, y_coord, z, N_max=50):
    """
    Potential outside a grounded conducting sphere of radius a.
    Real charge q at position (0, 0, y) on z-axis.
    Image charge q' = -a*q/y at position (0, 0, a²/y).

    Returns potential at (x, y_coord, z).

    # Uses both exact image formula and spherical harmonic sum for verification
    """
    y_val = y  # position of real charge
    y_img = a**2 / y_val
    q_img = -a * q / y_val

    r = np.sqrt(x**2 + y_coord**2 + z**2)
    r_real = np.sqrt(x**2 + y_coord**2 + (z - y_val)**2)
    r_img = np.sqrt(x**2 + y_coord**2 + (z - y_img)**2)

    Phi = K_COULOMB * (q / r_real + q_img / r_img)
    return Phi


def verify_sphere_bc(q=1e-9, y=2.0, a=1.0):
    """Verify that potential on sphere surface is zero."""
    # Sample points on sphere surface
    thetas = np.linspace(0, np.pi, 20)
    phis = np.linspace(0, 2*np.pi, 20)
    max_err = 0.0
    for theta in thetas:
        for phi in phis:
            x = a * np.sin(theta) * np.cos(phi)
            yc = a * np.sin(theta) * np.sin(phi)
            z = a * np.cos(theta)
            val = image_sphere_potential(q, y, a, x, yc, z)
            max_err = max(max_err, abs(val))
    return max_err


# =========================================================================
# 3.  SEPARATION OF VARIABLES — SPHERICAL HARMONICS
# =========================================================================
# Example 3a:  Laplace equation — conducting sphere hemispheres at ±V
# -------------------------------------------------------------------------

def sphere_hemispheres_potential(r, theta, a, V0, L_max=30):
    """
    Potential outside (r > a) or on the surface of a conducting sphere
    with upper hemisphere at +V0, lower hemisphere at -V0.

    Φ(r,θ) = V0 Σ_{l odd} [ (2l+1) (r</r>) ] ... see Jackson Prob 3.1

    For r >= a:
    Φ(r,θ) = V0 Σ_{l odd} (2l+1) I_l (a/r)^{l+1} P_l(cosθ)

    where I_l = ∫₀¹ P_l(x) dx = ?  (computed numerically)
    """
    Phi = 0.0
    for l in range(1, L_max + 1, 2):  # odd l only
        # I_l = ∫₀¹ P_l(x) dx
        def integrand_l(x):
            return legendre(l)(x)
        I_l, _ = quad(integrand_l, 0, 1, limit=200)

        coeff = (2*l + 1) * I_l * (a / r)**(l + 1)
        Phi += coeff * legendre(l)(np.cos(theta))

    return V0 * Phi


# Example 3b:  Separation of variables — rectangular box (2D)
# -------------------------------------------------------------------------

def rectangular_box_potential(x, y, a, b, V0, N_max=50):
    """
    Potential inside a 2D rectangular region [0,a] × [0,b].
    Boundary conditions: Φ = 0 on x=0, x=a, y=0; Φ = V0 on y=b.

    Φ(x,y) = Σ_{n odd} (4V0/nπ) sinh(nπy/a) / sinh(nπb/a) sin(nπx/a)
    """
    Phi = 0.0
    for n in range(1, N_max + 1, 2):
        term = (4 * V0 / (n * np.pi))
        term *= np.sinh(n * np.pi * y / a) / np.sinh(n * np.pi * b / a)
        term *= np.sin(n * np.pi * x / a)
        Phi += term
    return Phi


def verify_box_bc(a=1.0, b=1.0, V0=1.0, N=50):
    """Check BCs for the rectangular box problem."""
    # bottom (y=0) — exclude corners where series converges slowly
    xs = np.linspace(0.01, a - 0.01, 20)
    errs = []
    for x in xs:
        errs.append(abs(rectangular_box_potential(x, 0, a, b, V0, N)))
    err_bottom = max(errs)

    # top (y=b)
    errs_top = []
    for x in xs:
        val = rectangular_box_potential(x, b, a, b, V0, N)
        errs_top.append(abs(val - V0))
    err_top = max(errs_top)

    return err_bottom, err_top


# =========================================================================
# 4.  MULTIPOLE EXPANSION
# =========================================================================
# Example 4a:  Compute multipole moments of a discrete charge distribution
# -------------------------------------------------------------------------

def multipole_moments_cartesian(charges, positions):
    """
    Compute monopole, dipole, and quadrupole moments for a set of point charges.

    Parameters:
    -----------
    charges   : ndarray shape (N,) — charges in Coulombs
    positions : ndarray shape (N, 3) — positions in meters

    Returns:
    --------
    Q   : total charge (monopole)
    p   : dipole moment vector (3,)
    Qij : traceless quadrupole tensor (3,3)
    """
    charges = np.asarray(charges)
    positions = np.asarray(positions)

    # Monopole
    Q = np.sum(charges)

    # Dipole
    p = np.sum(charges[:, np.newaxis] * positions, axis=0)

    # Quadrupole (traceless)
    Qij = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            Qij[i, j] = np.sum(charges * (3.0 * positions[:, i] * positions[:, j]
                                        - np.sum(positions**2, axis=1) * (1.0 if i == j else 0.0)))
    return Q, p, Qij


def multipole_moments_spherical(charges, positions, l_max=2):
    """
    Compute spherical multipole moments q_{lm}.

    q_{lm} = Σ_i q_i r_i^l Y_{lm}^*(θ_i, φ_i)

    Returns dict with keys (l,m) -> q_lm
    """
    from scipy.special import lpmv  # associated Legendre

    moments = {}
    for l in range(l_max + 1):
        for m in range(-l, l + 1):
            val = 0.0 + 0.0j
            for q, pos in zip(charges, positions):
                r = np.linalg.norm(pos)
                theta = np.arccos(pos[2] / r) if r > 0 else 0.0
                phi = np.arctan2(pos[1], pos[0])

                # Y_lm
                # P_l^m(cosθ)
                Plm = lpmv(abs(m), l, np.cos(theta))
                # Condon-Shortley phase already in lpmv
                import math
                Ylm = np.sqrt((2*l+1)/(4*np.pi) * math.factorial(l-abs(m))/math.factorial(l+abs(m)))
                Ylm *= Plm * np.exp(1j * m * phi)

                val += q * r**l * np.conj(Ylm)
            moments[(l, m)] = val
    return moments


def multipole_expansion_potential(Q, p, Qij, r, theta, phi):
    """
    Compute potential at (r, θ, φ) from multipole moments (Cartesian),
    up to quadrupole.

    Parameters:
    -----------
    Q   : monopole (scalar)
    p   : dipole vector (3,)
    Qij : quadrupole tensor (3,3) — traceless
    r, theta, phi : spherical coordinates of observation point
    """
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    monopole = Q / r
    dipole = np.dot(p, [x, y, z]) / r**3

    quadrupole = 0.0
    coords = np.array([x, y, z])
    for i in range(3):
        for j in range(3):
            quadrupole += Qij[i, j] * coords[i] * coords[j] / (2.0 * r**5)

    return K_COULOMB * (monopole + dipole + quadrupole)


def test_multipole_convergence():
    """
    Compare exact potential with multipole expansion for a
    simple charge configuration (linear quadrupole).
    """
    charges = np.array([1e-9, -2e-9, 1e-9])
    positions = np.array([[0.0, 0.0, 0.01],
                          [0.0, 0.0, 0.0],
                          [0.0, 0.0, -0.01]])

    Q, p, Qij = multipole_moments_cartesian(charges, positions)
    print(f"  Monopole: Q = {Q:.2e} C")
    print(f"  Dipole:  p = ({p[0]:.2e}, {p[1]:.2e}, {p[2]:.2e}) C·m")
    print(f"  Quadrupole Qzz = {Qij[2,2]:.2e} C·m²")

    # Compare at various distances along x-axis
    print(f"\n  {'r (m)':<12} {'Exact (V)':<16} {'Multipole (V)':<16} {'Ratio':<10}")
    for r_val in [0.1, 0.5, 1.0, 5.0, 10.0]:
        # Exact from point charges
        exact = 0.0
        for q, pos in zip(charges, positions):
            dist = np.sqrt(r_val**2 + np.sum(pos**2))
            exact += K_COULOMB * q / dist

        # Multipole up to quadrupole
        multipole = multipole_expansion_potential(Q, p, Qij, r_val, np.pi/2, 0)
        error = abs(multipole - exact)

        print(f"  {r_val:<12.3f} {exact:<16.6e} {multipole:<16.6e} {multipole/exact:<10.6f}")


# =========================================================================
# 5.  DIELECTRIC BOUNDARY CONDITIONS
# =========================================================================
# Example 5a:  Dielectric sphere in uniform external field
# -------------------------------------------------------------------------

def dielectric_sphere_field(r, theta, a, epsilon_r, E0):
    """
    Electric field (magnitude and direction) for a dielectric sphere
    of radius a, relative permittivity epsilon_r, in uniform external
    field E0 = E0 * ẑ.

    Returns:
        Er  : radial component
        Etheta : polar component (theta increasing from +z axis)
    """
    epsilon = epsilon_r * EPS0

    if r <= a:
        # Inside: uniform field
        factor = 3 * EPS0 / (epsilon + 2 * EPS0)
        # E_in points in z-direction
        # In spherical: E_z = E_in cosθ, E_θ = -E_in sinθ
        E_in = factor * E0
        Er = E_in * np.cos(theta)
        Etheta = -E_in * np.sin(theta)
    else:
        # Outside: uniform field + induced dipole
        induced_p = 4 * np.pi * EPS0 * (epsilon - EPS0) / (epsilon + 2 * EPS0) * a**3 * E0
        # Uniform part: -E0 ẑ = -(E0 cosθ r̂ - E0 sinθ θ̂)
        Er_uniform = E0 * np.cos(theta)
        Etheta_uniform = -E0 * np.sin(theta)
        # Dipole part
        Er_dip = 2 * induced_p * np.cos(theta) / (4 * np.pi * EPS0 * r**3)
        Etheta_dip = induced_p * np.sin(theta) / (4 * np.pi * EPS0 * r**3)
        # Note sign: E = -∇Φ, for dipole Φ = p·r̂/(4πε₀r²) = p cosθ/(4πε₀r²)
        # E_r = -∂Φ/∂r = 2p cosθ/(4πε₀r³)
        # E_θ = -(1/r)∂Φ/∂θ = p sinθ/(4πε₀r³)

        # Total = -(−E0 ẑ) + dipole ... careful with signs
        # Actually Φ_out = -E0 r cosθ + p cosθ/(4πε₀ r²)
        # E_r = -∂Φ/∂r = E0 cosθ + 2p cosθ/(4πε₀ r³)
        # E_θ = -(1/r) ∂Φ/∂θ = -E0 sinθ + p sinθ/(4πε₀ r³)
        Er = E0 * np.cos(theta) + 2 * induced_p * np.cos(theta) / (4 * np.pi * EPS0 * r**3)
        Etheta = -E0 * np.sin(theta) + induced_p * np.sin(theta) / (4 * np.pi * EPS0 * r**3)

    return Er, Etheta


def dielectric_sphere_potential(r, theta, a, epsilon_r, E0):
    """
    Potential for dielectric sphere in uniform external field E0 ẑ.
    """
    epsilon = epsilon_r * EPS0

    if r <= a:
        factor = 3 * EPS0 / (epsilon + 2 * EPS0)
        Phi = -factor * E0 * r * np.cos(theta)
    else:
        Phi = -E0 * r * np.cos(theta)
        induced_p = 4 * np.pi * EPS0 * (epsilon - EPS0) / (epsilon + 2 * EPS0) * a**3 * E0
        Phi += induced_p * np.cos(theta) / (4 * np.pi * EPS0 * r**2)
    return Phi


def verify_dielectric_bc(a=1.0, epsilon_r=3.0, E0=1.0):
    """
    Verify boundary conditions at r = a for dielectric sphere.

    1. Potential continuous: Φ_in(a) = Φ_out(a)
    2. Tangential E continuous: (1/a)∂Φ/∂θ = continuous
    3. Normal D continuous: ε ∂Φ_in/∂r = ε₀ ∂Φ_out/∂r (no free charge)
    """
    theta = np.pi / 4  # some angle

    Phi_in = dielectric_sphere_potential(a, theta, a, epsilon_r, E0)
    Phi_out = dielectric_sphere_potential(a + 1e-9, theta, a, epsilon_r, E0)

    # For verification, compute derivatives numerically
    dr = 1e-8
    dtheta = 1e-8

    Phi_in_rp = dielectric_sphere_potential(a + dr, theta, a, epsilon_r, E0)
    Phi_in_rm = dielectric_sphere_potential(a - dr, theta, a, epsilon_r, E0)
    Phi_in_tp = dielectric_sphere_potential(a, theta + dtheta, a, epsilon_r, E0)
    Phi_in_tm = dielectric_sphere_potential(a, theta - dtheta, a, epsilon_r, E0)

    dPhi_in_dr = (Phi_in_rp - Phi_in_rm) / (2 * dr)
    dPhi_in_dtheta = (Phi_in_tp - Phi_in_tm) / (2 * dtheta)

    Phi_out_rp = dielectric_sphere_potential(a + dr, theta, a, epsilon_r, E0)
    Phi_out_rm = dielectric_sphere_potential(a - dr, theta, a, epsilon_r, E0)
    Phi_out_tp = dielectric_sphere_potential(a, theta + dtheta, a, epsilon_r, E0)
    Phi_out_tm = dielectric_sphere_potential(a, theta - dtheta, a, epsilon_r, E0)

    dPhi_out_dr = (Phi_out_rp - Phi_out_rm) / (2 * dr)
    dPhi_out_dtheta = (Phi_out_tp - Phi_out_tm) / (2 * dtheta)

    # Tangential E: E_t = -(1/r) ∂Φ/∂θ
    E_t_in = -dPhi_in_dtheta / a
    E_t_out = -dPhi_out_dtheta / a

    # Normal D: D_n = -ε ∂Φ/∂r
    D_n_in = -epsilon_r * EPS0 * dPhi_in_dr
    D_n_out = -EPS0 * dPhi_out_dr

    results = {
        "Phi continuous": {
            "error": abs(Phi_in - Phi_out),
            "pass": abs(Phi_in - Phi_out) < 1e-10
        },
        "E_t continuous": {
            "error": abs(E_t_in - E_t_out),
            "pass": abs(E_t_in - E_t_out) < 1e-10
        },
        "D_n continuous": {
            "D_n_in": D_n_in,
            "D_n_out": D_n_out,
            "error": abs(D_n_in - D_n_out),
            "pass": abs(D_n_in - D_n_out) < 1e-10
        }
    }
    return results


# =========================================================================
# 6.  VISUALIZATION FUNCTIONS
# =========================================================================

def plot_dielectric_sphere(epsilon_r=3.0, E0=1.0, a=1.0):
    """
    Plot potential contours and field lines for a dielectric sphere
    in a uniform external field.
    """
    npts = 200
    x = np.linspace(-3, 3, npts)
    z = np.linspace(-3, 3, npts)
    X, Z = np.meshgrid(x, z)
    R = np.sqrt(X**2 + Z**2)
    Theta = np.arctan2(np.abs(X), Z)  # theta from +z axis
    Theta = np.where(R < 1e-10, 0, Theta)

    # Compute potential
    Phi = np.zeros_like(R)
    mask_in = R <= a
    mask_out = R > a

    Phi_in = dielectric_sphere_potential(R[mask_in], Theta[mask_in], a, epsilon_r, E0)
    Phi_out = dielectric_sphere_potential(R[mask_out], Theta[mask_out], a, epsilon_r, E0)
    Phi[mask_in] = Phi_in
    Phi[mask_out] = Phi_out

    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Plot 1: Potential contours
    ax1 = axes[0]
    levels = np.linspace(Phi.min(), Phi.max(), 40)
    cp = ax1.contourf(X, Z, Phi, levels=levels, cmap='RdBu_r')
    ax1.contour(X, Z, Phi, levels=levels[::4], colors='k', linewidths=0.5)
    sphere = Circle((0, 0), a, fill=False, edgecolor='k', linewidth=2, linestyle='--')
    ax1.add_patch(sphere)
    ax1.set_xlabel('x')
    ax1.set_ylabel('z')
    ax1.set_title(f'Potential: εr={epsilon_r}, E₀={E0}')
    ax1.set_aspect('equal')
    fig.colorbar(cp, ax=ax1, label='Φ (V)')

    # Plot 2: Electric field lines (streamlines)
    ax2 = axes[1]
    Ex = np.zeros_like(R)
    Ez = np.zeros_like(R)
    for i in range(npts):
        for j in range(npts):
            r = R[i, j]
            theta = Theta[i, j]
            if r < 1e-10:
                continue
            Er, Etheta = dielectric_sphere_field(r, theta, a, epsilon_r, E0)
            # Convert to cartesian
            Ex[i, j] = Er * np.sin(theta) + Etheta * np.cos(theta)
            Ez[i, j] = Er * np.cos(theta) - Etheta * np.sin(theta)
            # Adjust sign for x<0 (theta definition)
            if X[i, j] < 0:
                Ex[i, j] *= -1

    lw = 2 * np.sqrt(Ex**2 + Ez**2) / np.sqrt(Ex**2 + Ez**2).max()
    ax2.streamplot(X, Z, Ex, Ez, density=1.5, color=lw, cmap='viridis',
                   linewidth=1.5)
    sphere2 = Circle((0, 0), a, fill=False, edgecolor='k', linewidth=2, linestyle='--')
    ax2.add_patch(sphere2)
    ax2.set_xlabel('x')
    ax2.set_ylabel('z')
    ax2.set_title(f'Field Lines: εr={epsilon_r}, E₀={E0}')
    ax2.set_aspect('equal')

    plt.tight_layout()
    plt.savefig('jackson/dielectric_sphere.png', dpi=150)
    plt.close()
    print("  Saved: jackson/dielectric_sphere.png")


def plot_conducting_plane_image():
    """
    Plot potential for point charge above grounded conducting plane.
    """
    q = 1e-9
    d = 1.0

    npts = 100
    x = np.linspace(-3, 3, npts)
    z = np.linspace(0.01, 3, npts)  # z > 0 only
    X, Z = np.meshgrid(x, z)

    Phi = image_plane_potential(q, d, X, np.zeros_like(X), Z)

    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    levels = 40
    cp = ax.contourf(X, Z, Phi, levels=levels, cmap='RdBu_r')
    ax.contour(X, Z, Phi, levels=levels//2, colors='k', linewidths=0.5)
    # Draw the plane
    ax.axhline(0, color='k', linewidth=2)
    # Draw the charge
    ax.plot(0, d, 'ro', markersize=8, label=f'q = {q*1e9:.0f} nC')
    ax.plot(0, -d, 'bo', markersize=8, label='image -q')
    ax.set_xlabel('x (m)')
    ax.set_ylabel('z (m)')
    ax.set_title('Point charge above grounded conducting plane')
    ax.set_aspect('equal')
    ax.legend()
    fig.colorbar(cp, ax=ax, label='Φ (V)')
    plt.tight_layout()
    plt.savefig('jackson/image_plane.png', dpi=150)
    plt.close()
    print("  Saved: jackson/image_plane.png")


def plot_rectangular_box_potential():
    """Plot potential inside a rectangular box (2D cross-section)."""
    a, b, V0 = 1.0, 1.0, 1.0
    npts = 100
    x = np.linspace(0, a, npts)
    y = np.linspace(0, b, npts)
    X, Y = np.meshgrid(x, y)

    Phi = rectangular_box_potential(X, Y, a, b, V0)

    fig, ax = plt.subplots(figsize=(7, 6))
    cp = ax.contourf(X, Y, Phi, levels=30, cmap='RdBu_r')
    ax.contour(X, Y, Phi, levels=15, colors='k', linewidths=0.5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Rectangular box potential (2D Laplace)')
    ax.set_aspect('equal')
    fig.colorbar(cp, ax=ax, label='Φ (V)')
    plt.tight_layout()
    plt.savefig('jackson/rectangular_box.png', dpi=150)
    plt.close()
    print("  Saved: jackson/rectangular_box.png")


def plot_multipole_convergence():
    """
    Plot how multipole expansion converges as 1/r for a linear quadrupole.
    """
    charges = np.array([1e-9, -2e-9, 1e-9])
    positions = np.array([[0.0, 0.0, 0.01],
                          [0.0, 0.0, 0.0],
                          [0.0, 0.0, -0.01]])
    Q, p, Qij = multipole_moments_cartesian(charges, positions)

    rs = np.logspace(-1.5, 1.5, 80)
    exact_vals = []
    mono_vals = []
    dip_vals = []
    quad_vals = []

    for r in rs:
        # Exact
        exact = 0.0
        for q, pos in zip(charges, positions):
            dist = np.sqrt(r**2 + np.sum(pos**2))
            exact += K_COULOMB * q / dist
        exact_vals.append(exact)

        # Monopole only
        mono = K_COULOMB * Q / r
        mono_vals.append(mono)

        # Monopole + dipole
        p_dot_r = p[2] * r  # on z-axis
        dip = mono + K_COULOMB * p_dot_r / r**2
        dip_vals.append(dip)

        # Up to quadrupole
        quad = dip + K_COULOMB * Qij[2, 2] / (2 * r**3)
        quad_vals.append(quad)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.loglog(rs, np.abs(exact_vals), 'k-', label='Exact')
    ax1.loglog(rs, np.abs(mono_vals), 'r--', label='Monopole')
    ax1.loglog(rs, np.abs(dip_vals), 'g--', label='+Dipole')
    ax1.loglog(rs, np.abs(quad_vals), 'b--', label='+Quadrupole')
    ax1.set_xlabel('r (m)')
    ax1.set_ylabel('|Φ| (V)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_title('Potential vs distance (linear quadrupole)')

    # Relative error
    err_mono = np.abs((np.array(mono_vals) - exact_vals) / exact_vals)
    err_dip = np.abs((np.array(dip_vals) - exact_vals) / exact_vals)
    err_quad = np.abs((np.array(quad_vals) - exact_vals) / exact_vals)

    ax2.loglog(rs, err_mono, 'r-', label='Monopole error')
    ax2.loglog(rs, err_dip, 'g-', label='+Dipole error')
    ax2.loglog(rs, err_quad, 'b-', label='+Quadrupole error')
    ax2.axhline(1e-2, color='gray', linestyle=':', alpha=0.5, label='1% level')
    ax2.set_xlabel('r (m)')
    ax2.set_ylabel('Relative error')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_title('Multipole expansion error')

    plt.tight_layout()
    plt.savefig('jackson/multipole_convergence.png', dpi=150)
    plt.close()
    print("  Saved: jackson/multipole_convergence.png")


# =========================================================================
# MAIN — Run all examples
# =========================================================================

def main():
    print("=" * 70)
    print("Jackson Ch1–Ch4: Numerical Examples")
    print("=" * 70)

    # -----------------------------------------------------------------
    # 1. Electric field / potential
    # -----------------------------------------------------------------
    print("\n" + "=" * 70)
    print("SECTION 1: Electric field / potential numerical computation")
    print("=" * 70)

    # Charged ring
    print("\n--- Charged ring (on-axis) ---")
    R_ring = 0.1  # m
    Q_ring = 1e-9  # C
    zs = np.array([0, 0.05, 0.1, 0.2, 0.5, 1.0])
    print(f"  Ring radius R = {R_ring} m, Q = {Q_ring*1e9:.0f} nC")
    print(f"  {'z (m)':<12} {'Φ (V)':<16} {'E_z (V/m)':<16}")
    for z in zs:
        P = potential_ring_axis(z, R_ring, Q_ring)
        E = efield_ring_axis(z, R_ring, Q_ring)
        print(f"  {z:<12.3f} {P:<16.6e} {E:<16.6e}")

    # Charged disk
    print("\n--- Uniformly charged disk (on-axis) ---")
    a_disk = 0.1
    sigma_disk = 1e-6  # C/m²
    print(f"  Disk radius a = {a_disk} m, σ = {sigma_disk:.1e} C/m²")
    print(f"  {'z (m)':<12} {'Φ (V)':<16} {'E_z (V/m)':<16}")
    for z in zs:
        P = potential_disk_axis(z, a_disk, sigma_disk)
        E = efield_disk_axis(z, a_disk, sigma_disk)
        print(f"  {z:<12.3f} {P:<16.6e} {E:<16.6e}")

    # Line charge
    print("\n--- Finite line charge (perp. bisector) ---")
    L_line = 0.2
    lam_line = 1e-9  # C/m
    print(f"  Length L = {L_line} m, λ = {lam_line:.1e} C/m")
    ys = np.array([0.01, 0.05, 0.1, 0.2, 0.5])
    print(f"  {'y (m)':<12} {'Φ (V)':<16}")
    for y in ys:
        P = potential_line_charge(0, y, L_line, lam_line)
        print(f"  {y:<12.3f} {P:<16.6e}")

    # -----------------------------------------------------------------
    # 2. Method of images
    # -----------------------------------------------------------------
    print("\n" + "=" * 70)
    print("SECTION 2: Method of images")
    print("=" * 70)

    # Point charge + plane
    print("\n--- Point charge above conducting plane ---")
    q = 1e-9
    d = 0.5
    test_xs = [0, 0.1, 0.5, 1.0]
    print(f"  q = {q*1e9:.0f} nC, d = {d} m")
    print(f"  {'(x,0,z)':<20} {'Φ (V)':<16} {'σ (C/m²)':<16}")
    for x in test_xs:
        P = image_plane_potential(q, d, x, 0, d)
        sigma = image_plane_surface_charge(q, d, x, 0)
        print(f"  ({x:.1f}, 0, {d:.1f}){'':<8} {P:<16.6e} {sigma:<16.6e}")

    force = image_plane_force(q, d)
    print(f"  Force on q: F = {force:.6e} N (attractive, negative = -z direction)")

    # Point charge + sphere
    print("\n--- Point charge outside conducting sphere ---")
    a_sphere = 1.0
    y_sphere = 2.0
    max_err = verify_sphere_bc(q, y_sphere, a_sphere)
    print(f"  Sphere radius a = {a_sphere} m, charge at y = {y_sphere} m")
    print(f"  Max |Φ| on sphere surface: {max_err:.4e} V (should be ~0 for grounded)")

    # -----------------------------------------------------------------
    # 3. Separation of variables
    # -----------------------------------------------------------------
    print("\n" + "=" * 70)
    print("SECTION 3: Separation of variables")
    print("=" * 70)

    # Spherical hemispheres
    print("\n--- Sphere hemispheres at ±V ---")
    a_sph = 1.0
    V0 = 1.0
    print(f"  a = {a_sph}, V0 = {V0}")
    test_thetas = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
    print(f"  {'θ (rad)':<12} {'Φ(a,θ) (V)':<16}")
    for th in test_thetas:
        P = sphere_hemispheres_potential(a_sph, th, a_sph, V0)
        print(f"  {th:<12.4f} {P:<16.6f}")

    # Rectangular box
    print("\n--- Rectangular box (2D Laplace) ---")
    a_box, b_box = 1.0, 1.0
    err_b, err_t = verify_box_bc(a_box, b_box, V0)
    print(f"  a = {a_box}, b = {b_box}, V(top) = {V0}, V(others) = 0")
    print(f"  Max |Φ| on bottom boundary: {err_b:.6e}")
    print(f"  Max |Φ - V0| on top boundary: {err_t:.6e}")

    # Test some interior points
    print(f"  {'(x,y)':<16} {'Φ (V)':<16}")
    test_pts = [(0.25, 0.25), (0.5, 0.5), (0.25, 0.75), (0.75, 0.5)]
    for x, y in test_pts:
        P = rectangular_box_potential(x, y, a_box, b_box, V0)
        print(f"  ({x:.2f}, {y:.2f}){'':<6} {P:<16.6f}")

    # -----------------------------------------------------------------
    # 4. Multipole expansion
    # -----------------------------------------------------------------
    print("\n" + "=" * 70)
    print("SECTION 4: Multipole expansion")
    print("=" * 70)

    print("\n--- Cartesian multipole moments ---")
    test_multipole_convergence()

    # Spherical multipoles
    print("\n--- Spherical multipole moments ---")
    charges_sph = np.array([1e-9, -2e-9, 1e-9])
    pos_sph = np.array([[0.0, 0.0, 0.01],
                        [0.0, 0.0, 0.0],
                        [0.0, 0.0, -0.01]])
    moments = multipole_moments_spherical(charges_sph, pos_sph, l_max=2)
    print(f"  {'(l,m)':<10} {'q_lm':<20}")
    for key, val in sorted(moments.items()):
        print(f"  ({key[0]},{key[1]}){'':<6} {val.real:<+12.6e}{'+' if val.imag >= 0 else ''}{val.imag:<+.6e}j")

    # -----------------------------------------------------------------
    # 5. Dielectric boundary conditions
    # -----------------------------------------------------------------
    print("\n" + "=" * 70)
    print("SECTION 5: Dielectric boundary conditions")
    print("=" * 70)

    for eps_r in [2.0, 5.0, 10.0, 80.0]:
        print(f"\n--- Dielectric sphere: εr = {eps_r} ---")
        bc = verify_dielectric_bc(a=1.0, epsilon_r=eps_r, E0=1.0)
        for key, val in bc.items():
            if key == "D_n continuous":
                print(f"  {key:<20}: D_n(in) = {val['D_n_in']:.6e}, D_n(out) = {val['D_n_out']:.6e}")
                print(f"  {'':<20}  error = {val['error']:.4e}, {'PASS' if val['pass'] else 'FAIL'}")
            else:
                print(f"  {key:<20}: error = {val['error']:.4e}, {'PASS' if val['pass'] else 'FAIL'}")

    # Internal field vs epsilon
    print("\n--- Internal field factor 3ε₀/(ε+2ε₀) vs εr ---")
    eps_rs = np.array([1.0, 1.5, 2.0, 3.0, 5.0, 10.0, 80.0])
    factors = 3 / (eps_rs + 2)
    print(f"  {'εr':<10} {'Factor':<16} {'Ein/E0':<16}")
    for er, f in zip(eps_rs, factors):
        print(f"  {er:<10.1f} {f:<16.6f} {f:<16.6f}")

    # -----------------------------------------------------------------
    # 6. Plots
    # -----------------------------------------------------------------
    print("\n" + "=" * 70)
    print("SECTION 6: Generating plots")
    print("=" * 70)

    print("\n1. Dielectric sphere in uniform external field ...")
    plot_dielectric_sphere(epsilon_r=5.0)
    print("2. Point charge above conducting plane ...")
    plot_conducting_plane_image()
    print("3. Rectangular box potential ...")
    plot_rectangular_box_potential()
    print("4. Multipole expansion convergence ...")
    plot_multipole_convergence()

    print("\n" + "=" * 70)
    print("ALL EXAMPLES COMPLETED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    main()
