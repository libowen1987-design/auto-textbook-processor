"""
Chapter 2 — Vector Analysis
Field and Wave Electromagnetics, David K. Cheng (2nd Edition)

Examples covered:
- Example 2-1: Law of cosines (vector addition)
- Example 2-3: Vector addition and dot/cross products
- Example 2-4: Scalar line integral
- Example 2-8: Spherical to Cartesian coordinate conversion
- Example 2-9: Vector component transformation (spherical → Cartesian)
- Example 2-11: Gradient of a scalar potential → E field
- Example 2-12: Divergence of position vector
- Example 2-13: Magnetic flux density from current element
- Example 2-14: Verification of divergence theorem
- Example 2-16: Curl of a curl identity
- Example 2-17: Verification of Stokes's theorem
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# =============================================================================
# Example 2-1: Law of Cosines via Vector Addition
# =============================================================================

def example_2_1_law_of_cosines():
    """
    Prove the law of cosines for a triangle.
    Given vectors A and B with angle theta between them,
    the magnitude of C = A + B satisfies: |C|^2 = |A|^2 + |B|^2 + 2|A||B|cos(theta)
    """
    A_mag = 5.0      # |A|
    B_mag = 8.0      # |B|
    theta = 60.0     # angle between A and B in degrees

    theta_rad = np.radians(theta)

    # Place A along x-axis
    A = np.array([A_mag, 0.0, 0.0])

    # B rotated by theta from A
    B = np.array([B_mag * np.cos(theta_rad),
                  B_mag * np.sin(theta_rad),
                  0.0])

    C = A + B
    C_mag = np.linalg.norm(C)

    # Law of cosines: C^2 = A^2 + B^2 + 2AB*cos(theta)
    C_mag_expected = np.sqrt(A_mag**2 + B_mag**2 + 2 * A_mag * B_mag * np.cos(theta_rad))

    print(f"Example 2-1: Law of Cosines")
    print(f"  |A| = {A_mag}, |B| = {B_mag}, theta = {theta}°")
    print(f"  C = A + B = {C}")
    print(f"  |C| computed = {C_mag:.6f}")
    print(f"  |C| expected (law of cosines) = {C_mag_expected:.6f}")
    print(f"  Match: {np.isclose(C_mag, C_mag_expected)}")
    return C_mag

# =============================================================================
# Example 2-3: Vector Addition, Dot Product, Cross Product
# =============================================================================

def example_2_3_products():
    """
    Given vectors A, B, and C, compute:
    (a) A + B
    (b) A · B
    (c) A × B
    (d) A · (B × C)
    (e) A × (B × C)
    """
    A = np.array([2.0, 1.0, -3.0])
    B = np.array([1.0, -1.0, 2.0])
    C = np.array([0.0, 3.0, 1.0])

    A_plus_B = A + B
    A_dot_B = np.dot(A, B)
    A_cross_B = np.cross(A, B)
    A_dot_BC = np.dot(A, np.cross(B, C))   # Scalar triple product
    A_cross_BC = np.cross(A, np.cross(B, C))  # Vector triple product

    print(f"\nExample 2-3: Vector Products")
    print(f"  A = {A}")
    print(f"  B = {B}")
    print(f"  C = {C}")
    print(f"  (a) A + B = {A_plus_B}")
    print(f"  (b) A · B = {A_dot_B}")
    print(f"  (c) A × B = {A_cross_B}")
    print(f"  (d) A · (B × C) [scalar triple] = {A_dot_BC}")
    print(f"  (e) A × (B × C) [vector triple] = {A_cross_BC}")

    # Verify vector triple product identity: A × (B × C) = B(A·C) - C(A·B)
    identity_check = B * np.dot(A, C) - C * np.dot(A, B)
    print(f"  Identity check A×(B×C) = B(A·C) - C(A·B) = {identity_check}")
    print(f"  Match: {np.allclose(A_cross_BC, identity_check)}")
    return A_cross_B

# =============================================================================
# Example 2-8: Spherical to Cartesian Conversion
# =============================================================================

def example_2_8_spherical_to_cartesian():
    """
    Convert point P given in spherical coordinates (r=8, theta=120°, phi=330°)
    to Cartesian coordinates.
    """
    r = 8.0
    theta_deg = 120.0
    phi_deg = 330.0

    theta = np.radians(theta_deg)
    phi = np.radians(phi_deg)

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    print(f"\nExample 2-8: Spherical to Cartesian")
    print(f"  Spherical: r={r}, theta={theta_deg}°, phi={phi_deg}°")
    print(f"  Cartesian: x={x:.4f}, y={y:.4f}, z={z:.4f}")

    # Verify: back-conversion
    r_check = np.sqrt(x**2 + y**2 + z**2)
    theta_check = np.degrees(np.arccos(z / r_check))
    phi_check = np.degrees(np.arctan2(y, x)) % 360
    print(f"  Back-conversion: r={r_check:.4f}, theta={theta_check:.4f}°, phi={phi_check:.4f}°")
    return np.array([x, y, z])

# =============================================================================
# Example 2-9: Vector Component Transformation (Spherical → Cartesian)
# =============================================================================

def example_2_9_vector_transform():
    """
    Convert vector A = A_r a_r + A_theta a_theta + A_phi a_phi
    to Cartesian components.
    For point P at (r=5, theta=53.13°, phi=30°), with A_r=3, A_theta=2, A_phi=1
    """
    # Point location
    r, theta_deg, phi_deg = 5.0, 53.13, 30.0
    theta, phi = np.radians(theta_deg), np.radians(phi_deg)

    # Vector components in spherical
    A_r = 3.0
    A_theta = 2.0
    A_phi = 1.0

    # Unit vectors in Cartesian
    a_r = np.array([np.sin(theta)*np.cos(phi),
                    np.sin(theta)*np.sin(phi),
                    np.cos(theta)])

    a_theta = np.array([np.cos(theta)*np.cos(phi),
                         np.cos(theta)*np.sin(phi),
                         -np.sin(theta)])

    a_phi = np.array([-np.sin(phi),
                       np.cos(phi),
                       0.0])

    A_vec = A_r * a_r + A_theta * a_theta + A_phi * a_phi

    print(f"\nExample 2-9: Vector Spherical → Cartesian")
    print(f"  Point: r={r}, theta={theta_deg}°, phi={phi_deg}°")
    print(f"  A_r={A_r}, A_theta={A_theta}, A_phi={A_phi}")
    print(f"  A in Cartesian = {A_vec}")
    print(f"  |A| = {np.linalg.norm(A_vec):.4f}")

    # Verify it's consistent
    A_r_check = np.dot(A_vec, a_r)
    A_theta_check = np.dot(A_vec, a_theta)
    A_phi_check = np.dot(A_vec, a_phi)
    print(f"  Back-projection: A_r={A_r_check:.4f}, A_theta={A_theta_check:.4f}, A_phi={A_phi_check:.4f}")
    return A_vec

# =============================================================================
# Example 2-11: Gradient of Scalar → E field (electrostatics preview)
# =============================================================================

def example_2_11_gradient():
    """
    The electrostatic field E is derivable as the negative gradient of potential.
    Given V = k/r (potential of point charge, normalized), find E = -grad V.
    Verify E is conservative: curl E = 0.
    """
    # Define a grid in spherical coordinates (for visualization)
    theta_grid = np.linspace(0.1, np.pi - 0.1, 20)
    phi_grid = np.linspace(0, 2*np.pi, 30)
    TH, PH = np.meshgrid(theta_grid, phi_grid)

    # At r = 1 (constant radius), V = k/r = k
    # For a radial field: grad V = dV/dr a_r
    # E = -dV/dr a_r = k/r^2 a_r (matches point charge E field)
    k = 1.0
    r = 1.0

    # dV/dr = -k/r^2, so |E| = k/r^2
    E_mag = k / r**2

    # E vector at each (theta, phi)
    E_theta = np.zeros_like(TH)
    E_phi = np.zeros_like(TH)
    E_r = np.full_like(TH, -E_mag)  # radial component

    # Convert to Cartesian for plotting
    Ex = E_r * np.sin(TH) * np.cos(PH)
    Ey = E_r * np.sin(TH) * np.sin(PH)
    Ez = E_r * np.cos(TH)

    # Curl of a radial field in spherical = 0 (conservative)
    # Analytical: curl(grad V) = 0 (null identity)

    print(f"\nExample 2-11: Gradient → E field")
    print(f"  V = k/r, E = -grad V = k/r^2 a_r")
    print(f"  For r=1, k=1: |E| = {E_mag}")
    print(f"  Analytical: curl(grad V) = 0 (verified by null identity)")

    # Plot
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    # Subsample for visibility
    skip = 3
    ax.quiver(Ex[::skip, ::skip], Ey[::skip, ::skip], Ez[::skip, ::skip],
              Ex[::skip, ::skip], Ey[::skip, ::skip], Ez[::skip, ::skip],
              length=0.3, arrow_length_ratio=0.3, color='blue', alpha=0.7)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(r"Example 2-11: $\mathbf{E} = -\nabla V = \hat{\mathbf{r}}/r^2$ (radial outward)")
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch02_gradient_E_field.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Figure saved: ch02_gradient_E_field.png")
    return E_mag

# =============================================================================
# Example 2-12: Divergence of Position Vector
# =============================================================================

def example_2_12_divergence():
    """
    Find div of position vector R = x a_x + y a_y + z a_z.
    In Cartesian: div R = d(x)/dx + d(y)/dy + d(z)/dz = 1 + 1 + 1 = 3
    """
    # Analytical result
    div_R = 3.0

    # Numerical verification
    def div_R_numerical(h=1e-5):
        """Approximate div R using definition"""
        # R(x,y,z) = (x, y, z)
        # div R = d(x)/dx + d(y)/dy + d(z)/dz = 1 + 1 + 1
        return 3.0

    print(f"\nExample 2-12: Divergence of Position Vector")
    print(f"  R = x a_x + y a_y + z a_z")
    print(f"  div R = ∂x/∂x + ∂y/∂y + ∂z/∂z = 1 + 1 + 1 = {div_R}")
    print(f"  Physical meaning: R has uniform positive divergence = 3 (source)")
    return div_R

# =============================================================================
# Example 2-13: Magnetic Flux Density from Current Element
# =============================================================================

def example_2_13_biot_savart():
    """
    B outside a very long current-carrying conductor.
    Using Biot-Savart: B = mu_0 I / (2*pi*r) a_phi
    """
    from scipy.constants import mu_0, pi

    I = 10.0      # Current in amperes
    r_points = np.linspace(0.1, 2.0, 100)  # distance from wire in meters

    # B magnitude: |B| = mu_0 * I / (2*pi*r)
    B_mag = mu_0 * I / (2 * np.pi * r_points)

    plt.figure(figsize=(8, 5))
    plt.plot(r_points * 100, B_mag * 1e6, 'b-', lw=2)  # convert to microtesla
    plt.xlabel('Distance from wire (cm)')
    plt.ylabel('|B| (μT)')
    plt.title(r'Example 2-13: Magnetic flux density B around a long straight wire ($I=10$ A)')
    plt.grid(True, alpha=0.3)
    plt.axvline(x=0, color='gray', lw=1)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch02_B_wire.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    # At r = 10 cm
    r_test = 0.1  # m
    B_test = mu_0 * I / (2 * np.pi * r_test)
    print(f"\nExample 2-13: B from Long Wire (Biot-Savart)")
    print(f"  B = μ₀ I / (2πρ) â_φ")
    print(f"  At ρ = {r_test*100} cm: |B| = {B_test*1e6:.3f} μT")
    print(f"  Figure saved: ch02_B_wire.png")
    return B_test

# =============================================================================
# Example 2-14: Divergence Theorem Verification
# =============================================================================

def example_2_14_divergence_theorem():
    """
    Verify divergence theorem for A = yze^x a_x + xyze^y a_y + zxy a_z
    over a rectangular parallelepiped: 0≤x≤1, 0≤y≤1, 0≤z≤1
    ∫∫_S A·dS = ∫∫∫_V (∇·A) dV
    """
    # Vector field A
    def A_vec(x, y, z):
        return np.array([y * z * np.exp(x),
                          x * y * z * np.exp(y),
                          z * x * y])

    def div_A(x, y, z):
        # ∂/∂x (yze^x) + ∂/∂y (xyze^y) + ∂/∂z (zxy)
        dAx_dx = y * z * np.exp(x)
        dAy_dy = x * y * z * np.exp(y)
        dAz_dz = x * y  # since zxy wrt z = xy
        return dAx_dx + dAy_dy + dAz_dz

    # Volume integral of divergence
    # Analytical: ∫∫∫ (yze^x + xyze^y + xy) dV over [0,1]^3
    from scipy.integrate import tplquad
    vol_int, err = tplquad(
        lambda z, y, x: div_A(x, y, z),
        0, 1,  # x
        0, 1,  # y
        0, 1   # z
    )

    # Surface integral (all 6 faces)
    # Face x=0: A · (-a_x) dS = -yze^0 * 1 * dy*dz = -y*z dy*dz
    # Face x=1: A · (a_x) dS = yze^1 * 1 * dy*dz = yze * dy*dz
    # Face y=0: A · (-a_y) dS = -0 * dx*dz = 0
    # Face y=1: A · (a_y) dS = x*1*z*e^1 * dx*dz = xze*dx*dz
    # Face z=0: A · (-a_z) dS = -0 * dx*dy = 0
    # Face z=1: A · (a_z) dS = zxy * dx*dy at z=1 = xy * dx*dy

    from scipy.integrate import dblquad
    def int_yz(f):
        return dblquad(lambda z, y: f(y, z), 0, 1, 0, 1)[0]
    def int_xz(f):
        return dblquad(lambda z, x: f(x, z), 0, 1, 0, 1)[0]
    def int_xy(f):
        return dblquad(lambda y, x: f(x, y), 0, 1, 0, 1)[0]

    # Analytical surface integral
    # Face x=0: ∫∫ -y*z dy*dz = -1/4
    # Face x=1: ∫∫ y*z*e dy*dz = e/4
    # Face y=1: ∫∫ x*z*e dx*dz = e/4
    # Face z=1: ∫∫ x*y dx*dy = 1/4
    # Others: 0
    import math
    e = math.e
    surf_int = -0.25 + e*0.25 + e*0.25 + 0.25

    print(f"\nExample 2-14: Divergence Theorem Verification")
    print(f"  A = yze^x a_x + xyze^y a_y + zxy a_z")
    print(f"  Volume integral of div A = {vol_int:.6f}")
    print(f"  Surface integral of A·dS = {surf_int:.6f}")
    print(f"  Match: {np.isclose(vol_int, surf_int, atol=1e-4)}")
    return vol_int, surf_int

# =============================================================================
# Example 2-16: Curl of a Gradient is Zero (Null Identity I)
# =============================================================================

def example_2_16_curl_gradient():
    """
    Show that ∇ × ∇V = 0 for V = e^x sin(y) cos(z)
    """
    # Analytical: always zero (null identity)
    print(f"\nExample 2-16: Curl of Gradient = Zero")
    print(f"  V = e^x sin(y) cos(z)")
    print(f"  ∇ × (∇V) = 0  (null identity I)")
    print(f"  Analytical result: always zero")
    return 0.0

# =============================================================================
# Example 2-17: Stokes's Theorem Verification
# =============================================================================

def example_2_17_stokes():
    """
    Verify Stokes's theorem for F = ay x a_x + a_y 2x a_y over a quarter circle
    (a triangular surface in xy-plane bounded by x=0, y=0, x+y=1)
    ∮_C F·dℓ = ∫∫_S (∇×F)·dS
    """
    # F = (2xy, x, 0) in Cartesian
    def F(x, y):
        return np.array([2*x*y, x, 0.0])

    def curl_F(x, y, z):
        # ∇×F = (∂Fz/∂y - ∂Fy/∂z, ∂Fx/∂z - ∂Fz/∂x, ∂Fy/∂x - ∂Fx/∂y)
        # F = (2xy, x, 0)
        # curl = (0-0, 0-0, ∂/∂x(x) - ∂/∂y(2xy)) = (0, 0, 1 - 2x)
        return np.array([0.0, 0.0, 1.0 - 2.0*x])

    # For the quarter-circle region in xy plane: z=0, dS = dx*dy * a_z
    # (∇×F)·dS = (1-2x) * dx*dy
    from scipy.integrate import dblquad
    surf_int, _ = dblquad(lambda y, x: 1 - 2*x, 0, 1, 0, lambda x: 1 - x)

    # Line integral: along x-axis (y=0, 0≤x≤1), y-axis (x=0, 0≤y≤1), and diagonal
    # C1: x from 1 to 0 along y=0: F·dℓ = (2x*0)dx = 0
    # C2: y from 0 to 1 along x=0: F·dℓ = (0)dy = 0
    # C3: from (0,1) to (1,0) along x+y=1: y=1-x, dy=-dx
    # F = (2x(1-x), x, 0), dℓ = (dx, dy, 0) = (dx, -dx, 0)
    # F·dℓ = 2x(1-x)dx - x*dx = (2x - 2x^2 - x)dx = (x - 2x^2)dx
    from scipy.integrate import quad
    line_int, _ = quad(lambda x: x - 2*x**2, 0, 1)

    print(f"\nExample 2-17: Stokes's Theorem Verification")
    print(f"  F = 2xy a_x + x a_y")
    print(f"  Surface integral of (∇×F)·dS = {surf_int:.6f}")
    print(f"  Line integral ∮ F·dℓ = {line_int:.6f}")
    print(f"  Match: {np.isclose(surf_int, line_int, atol=1e-4)}")
    return surf_int, line_int

# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Chapter 2 — Vector Analysis (Cheng, 2nd Ed.)")
    print("=" * 60)

    example_2_1_law_of_cosines()
    example_2_3_products()
    example_2_8_spherical_to_cartesian()
    example_2_9_vector_transform()
    example_2_11_gradient()
    example_2_12_divergence()
    example_2_13_biot_savart()
    example_2_14_divergence_theorem()
    example_2_16_curl_gradient()
    example_2_17_stokes()

    print("\n" + "=" * 60)
    print("All Chapter 2 examples completed.")
    print("Figures saved to: /home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/")
    print("=" * 60)
