#!/usr/bin/env python3
"""
Griffiths Chapter 1: Vector Analysis - Example Implementations

This script implements key examples from Chapter 1 of Griffiths'
Introduction to Electrodynamics (4th Edition), demonstrating vector
analysis, gradient, divergence, curl, and the fundamental theorems.

Author: 小龙虾 (Crayfish)
Date: 2026-05-03
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import constants

# Use a clean style
plt.style.use('seaborn-v0_8')

# Physical constants (from scipy)
c = constants.c            # speed of light
epsilon_0 = constants.epsilon_0  # vacuum permittivity
mu_0 = constants.mu_0           # vacuum permeability


# ============================================================
# Example 1.2: Angle between face diagonals of a cube (p. 6)
# ============================================================
def example_1_2_face_diagonals():
    """
    Find the angle between the face diagonals of a cube.
    Cube of side 1, placed with one corner at origin.
    Face diagonal A: from (0,0,0) to (1,0,1)
    Face diagonal B: from (0,0,0) to (0,1,1)
    
    Returns: angle in degrees
    """
    print("=" * 60)
    print("Example 1.2: Angle between face diagonals of a cube")
    print("=" * 60)

    # Face diagonals
    A = np.array([1.0, 0.0, 1.0])
    B = np.array([0.0, 1.0, 1.0])

    # Dot product in component form
    A_dot_B = np.dot(A, B)
    A_mag = np.linalg.norm(A)
    B_mag = np.linalg.norm(B)

    # Abstract form: A.B = AB cos(theta)
    cos_theta = A_dot_B / (A_mag * B_mag)
    theta_rad = np.arccos(cos_theta)
    theta_deg = np.degrees(theta_rad)

    print(f"\nVector A (face diagonal 1): {A}")
    print(f"Vector B (face diagonal 2): {B}")
    print(f"|A| = sqrt(2) = {A_mag:.6f}")
    print(f"|B| = sqrt(2) = {B_mag:.6f}")
    print(f"A . B = {A_dot_B:.6f}")
    print(f"cos(theta) = {cos_theta:.6f}")
    print(f"theta = {theta_deg:.2f} deg  (expected: 60 deg)")

    # 3D visualization
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Draw cube edges
    for x in [0, 1]:
        for y in [0, 1]:
            ax.plot([x, x], [y, y], [0, 1], 'gray', lw=0.5)
    for x in [0, 1]:
        for z in [0, 1]:
            ax.plot([x, x], [0, 1], [z, z], 'gray', lw=0.5)
    for y in [0, 1]:
        for z in [0, 1]:
            ax.plot([0, 1], [y, y], [z, z], 'gray', lw=0.5)

    # Draw face diagonals
    origin = np.array([0., 0., 0.])
    for vec, color, label in zip([A, B], ['red', 'blue'], ['A', 'B']):
        ax.quiver(*origin, *vec, color=color, arrow_length_ratio=0.1,
                  linewidth=3, label=label)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_xlim(0, 1.2)
    ax.set_ylim(0, 1.2)
    ax.set_zlim(0, 1.2)
    ax.set_title(f'Face Diagonals of a Cube (theta = {theta_deg:.1f})')
    ax.legend()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch1_ex2_cube_diagonals.png',
                dpi=150, bbox_inches='tight')
    print(f"\nFigure saved: griffiths_ch1_ex2_cube_diagonals.png")
    plt.close(fig)

    return theta_deg


# ============================================================
# Example 1.6: Line integral (p. 25)
# ============================================================
def example_1_6_line_integral():
    """
    Calculate line integral of v = y^2 x_hat + 2x(y+1) y_hat
    from a = (1,1,0) to b = (2,2,0) along two paths.
    
    Path 1: horizontal then vertical
    Path 2: diagonal y = x
    
    Returns: integral values for each path
    """
    print("\n" + "=" * 60)
    print("Example 1.6: Line integral")
    print("=" * 60)

    def v_func(x, y):
        """Vector field v(x,y) = y^2 x_hat + 2x(y+1) y_hat"""
        vx = y**2
        vy = 2.0 * x * (y + 1.0)
        return vx, vy

    # Path 1: Horizontal from (1,1) to (2,1), then vertical from (2,1) to (2,2)
    N_steps = 1000
    # Horizontal segment: y=1, x: 1->2, dy=0, v.dl = y^2 dx = 1 dx
    x_vals_h = np.linspace(1.0, 2.0, N_steps)
    y_const = 1.0 * np.ones_like(x_vals_h)
    vx_h, _ = v_func(x_vals_h, y_const)
    integral_horizontal = np.trapezoid(vx_h, x_vals_h)

    # Vertical segment: x=2, y: 1->2, dx=0, v.dl = 2x(y+1) dy
    y_vals_v = np.linspace(1.0, 2.0, N_steps)
    x_const = 2.0 * np.ones_like(y_vals_v)
    _, vy_v = v_func(x_const, y_vals_v)
    integral_vertical = np.trapezoid(vy_v, y_vals_v)

    integral_path1 = integral_horizontal + integral_vertical

    print(f"\nPath 1 (horizontal then vertical):")
    print(f"  Horizontal segment: int y^2 dx = {integral_horizontal:.6f}")
    print(f"  Vertical segment:   int 2x(y+1) dy = {integral_vertical:.6f}")
    print(f"  Total: int v.dl = {integral_path1:.6f}")

    # Path 2: Diagonal y = x, x: 1->2
    # v.dl = y^2 dx + 2x(y+1) dy = x^2 dx + 2x(x+1) dx = (3x^2 + 2x) dx
    x_vals_d = np.linspace(1.0, 2.0, N_steps)
    y_vals_d = x_vals_d
    vx_d, vy_d = v_func(x_vals_d, y_vals_d)
    # dy = dx for y=x, so v.dl = vx*dx + vy*dx = (vx+vy) dx
    integrand_d = vx_d + vy_d
    integral_path2 = np.trapezoid(integrand_d, x_vals_d)

    print(f"\nPath 2 (diagonal y = x):")
    print(f"  int (3x^2 + 2x) dx = {integral_path2:.6f}")

    # Closed loop: path1 out, path2 back
    closed_loop = integral_path1 - integral_path2
    print(f"\nClosed loop: contour v.dl = {closed_loop:.6f} (expected: 1)")

    # Plot the paths with vector field
    fig, ax = plt.subplots(figsize=(8, 6))

    # Path 1
    ax.plot([1, 2], [1, 1], 'b-', linewidth=3, label='Path 1 (horizontal)')
    ax.plot([2, 2], [1, 2], 'b-', linewidth=3)
    # Path 2
    ax.plot([1, 2], [1, 2], 'r--', linewidth=3, label='Path 2 (diagonal y=x)')

    # Vector field quiver
    Xg, Yg = np.meshgrid(np.linspace(0.8, 2.2, 6), np.linspace(0.8, 2.2, 6))
    Ug, Vg = v_func(Xg, Yg)
    ax.quiver(Xg, Yg, Ug, Vg, alpha=0.5, width=0.005)

    ax.scatter([1, 2], [1, 2], color='black', s=100, zorder=5)
    ax.annotate('a (1,1)', (1, 1), xytext=(0.8, 0.8), fontsize=12)
    ax.annotate('b (2,2)', (2, 2), xytext=(2.1, 2.1), fontsize=12)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Line integral paths for v = y^2 x_hat + 2x(y+1) y_hat')
    ax.legend()
    ax.set_xlim(0.8, 2.3)
    ax.set_ylim(0.8, 2.3)
    ax.grid(True, alpha=0.3)
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch1_ex6_line_integral.png',
                dpi=150, bbox_inches='tight')
    print(f"\nFigure saved: griffiths_ch1_ex6_line_integral.png")
    plt.close(fig)

    return integral_path1, integral_path2, closed_loop


# ============================================================
# Example 1.9: Gradient theorem verification (p. 30)
# ============================================================
def example_1_9_gradient_theorem():
    """
    Check the fundamental theorem for gradients using T = xy^2.
    From a = (0,0,0) to b = (2,1,0).
    
    LHS: int(grad T).dl along path
    RHS: T(b) - T(a)
    """
    print("\n" + "=" * 60)
    print("Example 1.9: Gradient theorem (Fundamental theorem for gradients)")
    print("=" * 60)

    def T_func(x, y):
        """Scalar function T = xy^2"""
        return x * y**2

    def grad_T(x, y):
        """Gradient of T: grad T = y^2 x_hat + 2xy y_hat"""
        gx = y**2
        gy = 2.0 * x * y
        return gx, gy

    N_steps = 1000

    # Segment (i): y=0, x: 0->2, grad T.dl = y^2 dx = 0
    x_i = np.linspace(0.0, 2.0, N_steps)
    y_i_const = 0.0 * np.ones_like(x_i)
    gx_i, _ = grad_T(x_i, y_i_const)
    int_i = np.trapezoid(gx_i, x_i)

    # Segment (ii): x=2, y: 0->1, grad T.dl = 2xy dy = 4y dy
    y_ii = np.linspace(0.0, 1.0, N_steps)
    x_ii_const = 2.0 * np.ones_like(y_ii)
    _, gy_ii = grad_T(x_ii_const, y_ii)
    int_ii = np.trapezoid(gy_ii, y_ii)

    lhs_path1 = int_i + int_ii

    # Path 2: straight line y = x/2, x: 0->2
    # v.dl = y^2 dx + 2xy dy = (x/2)^2 dx + 2x(x/2)(dx/2) = x^2/4 dx + x^2/2 dx = 3x^2/4 dx
    x_iii = np.linspace(0.0, 2.0, N_steps)
    y_iii = x_iii / 2.0
    gx_iii, gy_iii = grad_T(x_iii, y_iii)
    # dy = dx/2 for y=x/2, so v.dl = gx*dx + gy*(dx/2) = (gx + gy/2)*dx
    integrand_iii = gx_iii + gy_iii / 2.0
    lhs_path2 = np.trapezoid(integrand_iii, x_iii)

    # RHS: T(b) - T(a)
    T_a = T_func(0.0, 0.0)
    T_b = T_func(2.0, 1.0)
    rhs = T_b - T_a

    print(f"\nT(x,y) = xy^2")
    print(f"grad T = y^2 x_hat + 2xy y_hat")
    print(f"a = (0,0,0), b = (2,1,0)")
    print(f"T(a) = {T_a:.6f}")
    print(f"T(b) = {T_b:.6f}")
    print(f"RHS: T(b) - T(a) = {rhs:.6f}")
    print(f"\nLHS along path 1 (x-axis then y-axis):")
    print(f"  Segment (i): int y^2 dx = {int_i:.6f}")
    print(f"  Segment (ii): int 2xy dy = {int_ii:.6f}")
    print(f"  Total = {lhs_path1:.6f}")
    print(f"\nLHS along path 2 (diagonal y=x/2):")
    print(f"  int grad T.dl = {lhs_path2:.6f}")
    print(f"\nGradient theorem verified: LHS = RHS = {rhs:.6f}")

    return lhs_path1, lhs_path2, rhs


# ============================================================
# Example 1.10: Divergence theorem (p. 32)
# ============================================================
def example_1_10_divergence_theorem():
    """
    Check the divergence theorem for v = y^2 x_hat + (2xy+z^2) y_hat + 2yz z_hat
    over a unit cube at the origin.
    
    LHS: int(div v) dtau
    RHS: contour v.da
    """
    print("\n" + "=" * 60)
    print("Example 1.10: Divergence theorem (Gauss' theorem)")
    print("=" * 60)

    def div_v(x, y, z):
        """Divergence of v: div v = 2(x+y)"""
        return 2.0 * (x + y)

    # LHS: Volume integral of divergence
    N = 200
    x_vals = np.linspace(0.0, 1.0, N)
    y_vals = np.linspace(0.0, 1.0, N)
    z_vals = np.linspace(0.0, 1.0, N)
    X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals, indexing='ij')
    dV = (1.0 / (N - 1))**3

    lhs = np.sum(div_v(X, Y, Z)) * dV

    # RHS: Surface integral over 6 faces
    # Face (i): x=1, da = dy dz x_hat, v.da = y^2 dy dz
    rhs_i = np.trapezoid(y_vals**2, y_vals) * np.trapezoid(np.ones_like(z_vals), z_vals)

    # Face (ii): x=0, da = -dy dz x_hat, v.da = -y^2 dy dz
    rhs_ii = -rhs_i

    # Face (iii): y=1, da = dx dz y_hat, v.da = (2x+z^2) dx dz
    x_ints = np.linspace(0.0, 1.0, N)
    z_ints = np.linspace(0.0, 1.0, N)
    integrand_iii = 2.0 * x_ints[:, np.newaxis] + z_ints[np.newaxis, :]**2
    rhs_iii = np.trapezoid(np.trapezoid(integrand_iii, x_ints, axis=0), z_ints)

    # Face (iv): y=0, da = -dx dz y_hat, v.da = -(0+z^2) dx dz = -z^2 dx dz
    integrand_iv = z_ints[np.newaxis, :]**2 * np.ones((N, 1))
    rhs_iv = -np.trapezoid(np.trapezoid(integrand_iv, x_ints, axis=0), z_ints)

    # Face (v): z=1, da = dx dy z_hat, v.da = 2yz dx dy = 2y dx dy
    integrand_v = 2.0 * y_vals[np.newaxis, :] * np.ones((N, 1))
    rhs_v = np.trapezoid(np.trapezoid(integrand_v, x_ints, axis=0), y_vals)

    # Face (vi): z=0, da = -dx dy z_hat, v.da = 0
    rhs_vi = 0.0

    rhs = rhs_i + rhs_ii + rhs_iii + rhs_iv + rhs_v + rhs_vi

    print(f"\nv = y^2 x_hat + (2xy+z^2) y_hat + 2yz z_hat")
    print(f"div v = 2(x+y)")
    print(f"Volume: unit cube at origin [0,1]x[0,1]x[0,1]")
    print(f"\nLHS: int(div v) dtau = {lhs:.6f}")
    print(f"\nRHS: contour v.da = {rhs:.6f}")
    print(f"  Face (i) x=1, +x:    {rhs_i:.6f}")
    print(f"  Face (ii) x=0, -x:   {rhs_ii:.6f}")
    print(f"  Face (iii) y=1, +y:  {rhs_iii:.6f}")
    print(f"  Face (iv) y=0, -y:   {rhs_iv:.6f}")
    print(f"  Face (v) z=1, +z:    {rhs_v:.6f}")
    print(f"  Face (vi) z=0, -z:   {rhs_vi:.6f}")
    print(f"\nDivergence theorem verified: LHS approx = RHS approx")

    return lhs, rhs


# ============================================================
# Example 1.11: Stokes' theorem (p. 35)
# ============================================================
def example_1_11_stokes_theorem():
    """
    Check Stokes' theorem for v = (2xz+3y^2)y_hat + 4yz^2 z_hat
    over the square surface x=0, 0<=y<=1, 0<=z<=1.
    
    LHS: int(curl v).da over surface
    RHS: contour v.dl around boundary
    """
    print("\n" + "=" * 60)
    print("Example 1.11: Stokes' theorem")
    print("=" * 60)

    # curl v = (4z^2 - 2x) x_hat + 2z z_hat
    # At x=0: curl v = 4z^2 x_hat + 2z z_hat
    # da = dy dz x_hat, so (curl v).da = 4z^2 dy dz

    # LHS: Surface integral
    N = 1000
    y_vals = np.linspace(0.0, 1.0, N)
    z_vals = np.linspace(0.0, 1.0, N)
    integrand_lhs = 4.0 * z_vals**2
    lhs = np.trapezoid(np.trapezoid(
        integrand_lhs[np.newaxis, :] * np.ones((N, 1)),
        y_vals, axis=0), z_vals)

    print(f"\nv = (2xz+3y^2)y_hat + 4yz^2 z_hat")
    print(f"Surface: square at x=0, 0<=y<=1, 0<=z<=1")
    print(f"curl v = 4z^2 x_hat + 2z z_hat (at x=0)")
    print(f"da = dy dz x_hat")
    print(f"\nLHS: int(curl v).da = int int 4z^2 dy dz = {lhs:.6f}")

    # RHS: Line integral around 4 edges
    N_e = 1000
    # Edge (i): x=0, z=0, y: 0->1, v.dl = 3y^2 dy
    y_e = np.linspace(0.0, 1.0, N_e)
    rhs_i = np.trapezoid(3.0 * y_e**2, y_e)

    # Edge (ii): x=0, y=1, z: 0->1, v.dl = 4z^2 dz
    z_e = np.linspace(0.0, 1.0, N_e)
    rhs_ii = np.trapezoid(4.0 * z_e**2, z_e)

    # Edge (iii): x=0, z=1, y: 1->0, v.dl = 3y^2 dy (backwards)
    rhs_iii = -np.trapezoid(3.0 * y_e**2, y_e)

    # Edge (iv): x=0, y=0, z: 1->0, v.dl = 0 (vz=0 when y=0)
    rhs_iv = 0.0

    rhs = rhs_i + rhs_ii + rhs_iii + rhs_iv

    print(f"\nRHS: contour v.dl = {rhs:.6f}")
    print(f"  Edge (i) z=0, y:0->1: 3y^2 dy = {rhs_i:.6f}")
    print(f"  Edge (ii) y=1, z:0->1: 4z^2 dz = {rhs_ii:.6f}")
    print(f"  Edge (iii) z=1, y:1->0: 3y^2 dy = {rhs_iii:.6f}")
    print(f"  Edge (iv) y=0, z:1->0: 0 dz = {rhs_iv:.6f}")
    print(f"\nStokes' theorem verified: LHS = RHS = {lhs:.6f}")

    return lhs, rhs


# ============================================================
# Example 1.13: Volume of a sphere (p. 41)
# ============================================================
def example_1_13_volume_of_sphere():
    """
    Find the volume of a sphere of radius R using spherical coordinates.
    V = int dtau = int_0^R int_0^pi int_0^{2pi} r^2 sin(theta) dr dtheta dphi
      = (4/3)pi R^3
    """
    print("\n" + "=" * 60)
    print("Example 1.13: Volume of a sphere")
    print("=" * 60)

    R = 1.0  # unit sphere
    N_r = int(200)
    N_theta = int(200)

    r_vals = np.linspace(0.0, R, N_r)
    theta_vals = np.linspace(0.0, np.pi, N_theta)

    # Vectorized: V = int_0^R int_0^pi r^2 sin(theta) dr dtheta * 2pi
    rr, tt = np.meshgrid(r_vals, theta_vals, indexing='ij')
    integrand = rr**2 * np.sin(tt)
    volume_numerical = np.trapezoid(np.trapezoid(integrand, r_vals, axis=0), theta_vals) * 2.0 * np.pi

    volume_analytic = (4.0 / 3.0) * np.pi * R**3

    print(f"\nSphere radius R = {R}")
    print(f"Numerical volume = {volume_numerical:.6f}")
    print(f"Analytic volume = (4/3)pi R^3 = {volume_analytic:.6f}")
    print(f"Relative error = {abs(volume_numerical - volume_analytic) / volume_analytic * 100:.6f}%")

    return volume_numerical, volume_analytic


# ============================================================
# Extra: Problem 1.1 - Law of cosines via dot product (p. 2)
# ============================================================
def problem_1_1_law_of_cosines():
    """
    Demo of the law of cosines.
    Given two vectors A and B with angle theta between them,
    C = A - B, compute C^2 = A^2 + B^2 - 2AB cos(theta).
    """
    print("\n" + "=" * 60)
    print("Problem 1.1: Law of cosines (via dot product)")
    print("=" * 60)

    A = np.array([3.0, 0.0, 0.0])
    B = np.array([1.0, 2.0, 0.0])
    C = A - B

    A_mag = np.linalg.norm(A)
    B_mag = np.linalg.norm(B)
    C_mag = np.linalg.norm(C)
    cos_theta = np.dot(A, B) / (A_mag * B_mag)

    C_sq_from_components = C_mag**2

    # From law of cosines: C^2 = A^2 + B^2 - 2AB cos(theta)
    C_sq_from_law = A_mag**2 + B_mag**2 - 2.0 * A_mag * B_mag * cos_theta

    print(f"\nA = {A}")
    print(f"B = {B}")
    print(f"C = A - B = {C}")
    print(f"theta = {np.degrees(np.arccos(cos_theta)):.2f} deg")
    print(f"\n|C|^2 from components = {C_sq_from_components:.6f}")
    print(f"|C|^2 from law of cosines = {C_sq_from_law:.6f}")
    print(f"Match: {np.isclose(C_sq_from_components, C_sq_from_law)}")

    return C_sq_from_components, C_sq_from_law


# ============================================================
# Main execution
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Griffiths Ch.1: Vector Analysis - Examples")
    print("Using scipy.constants for physical constants")
    print(f"  c = {c:.4e} m/s")
    print(f"  epsilon_0 = {epsilon_0:.4e} F/m")
    print(f"  mu_0 = {mu_0:.4e} N/A^2")
    print("=" * 60)

    # Run all examples
    theta_deg = example_1_2_face_diagonals()
    assert np.isclose(theta_deg, 60.0, atol=1e-10), "Example 1.2 failed!"

    int_path1, int_path2, closed = example_1_6_line_integral()
    assert np.isclose(int_path1, 11.0, atol=1e-2), "Example 1.6 path1 failed!"
    assert np.isclose(int_path2, 10.0, atol=1e-2), "Example 1.6 path2 failed!"
    assert np.isclose(closed, 1.0, atol=1e-2), "Example 1.6 loop failed!"

    lhs1, lhs2, rhs = example_1_9_gradient_theorem()
    assert np.isclose(lhs1, rhs, atol=1e-6), "Example 1.9 gradient theorem failed!"
    assert np.isclose(lhs2, rhs, atol=1e-6), "Example 1.9 path independence failed!"

    lhs_div, rhs_div = example_1_10_divergence_theorem()
    assert np.isclose(lhs_div, rhs_div, atol=0.1), "Example 1.10 divergence theorem failed!"

    lhs_stokes, rhs_stokes = example_1_11_stokes_theorem()
    assert np.isclose(lhs_stokes, rhs_stokes, atol=1e-4), "Example 1.11 Stokes failed!"

    vol_num, vol_ana = example_1_13_volume_of_sphere()
    assert np.isclose(vol_num, vol_ana, rtol=0.05), "Example 1.13 sphere volume failed!"

    C_sq_c, C_sq_l = problem_1_1_law_of_cosines()
    assert np.isclose(C_sq_c, C_sq_l, atol=1e-10), "Law of cosines failed!"

    print("\n" + "=" * 60)
    print("ALL Chapter 1 examples verified successfully!")
    print("=" * 60)
