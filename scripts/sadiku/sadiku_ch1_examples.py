#!/usr/bin/env python3
"""
Chapter 1: Vector Algebra — Examples and Visualizations
Sadiku, Elements of Electromagnetics, 7th Ed.

This script reproduces the textbook examples and provides 3D vector visualizations.
All variable names carry physical meaning as per electromagnetic conventions.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import os

# Output directory for figures
FIG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures')
os.makedirs(FIG_DIR, exist_ok=True)


# ============================================================
# Helper: 3D arrow class for matplotlib
# ============================================================
class Arrow3D(FancyArrowPatch):
    """A 3D arrow patch for matplotlib."""
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)


def plot_3d_vector(ax, origin, vector, color='b', label=None, arrowstyle='-|>',
                  lw=2, mutation_scale=20):
    """Draw a 3D vector from origin in direction of vector."""
    x, y, z = origin
    u, v, w = vector
    a = Arrow3D([x, x + u], [y, y + v], [z, z + w],
                mutation_scale=mutation_scale, lw=lw,
                arrowstyle=arrowstyle, color=color)
    ax.add_artist(a)
    if label:
        ax.text(x + u * 1.1, y + v * 1.1, z + w * 1.1, label, color=color, fontsize=12)


def setup_3d_ax(ax, title="", xlim=(-1, 1), ylim=(-1, 1), zlim=(-1, 1)):
    """Configure a 3D axis with labels and limits."""
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_zlim(zlim)
    ax.set_title(title, fontsize=14)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.grid(True, alpha=0.3)


# ============================================================
# Basic vector operations — Example 1.1
# ============================================================
def example_1_1():
    """Reproduce Example 1.1:
    A = 10a_x - 4a_y + 6a_z, B = 2a_x + a_y
    Find: (a) component of A along a_y, (b) |3A - B|, (c) unit vector along A + 2B.
    """
    print("=" * 60)
    print("EXAMPLE 1.1: Basic Vector Operations")
    print("=" * 60)

    A = np.array([10, -4, 6])
    B = np.array([2, 1, 0])

    # (a) Component of A along a_y
    Ay_component = A[1]
    print(f"(a) Component of A along a_y: {Ay_component}")

    # (b) |3A - B|
    C = 3 * A - B
    mag_C = np.linalg.norm(C)
    print(f"(b) 3A - B = {C}")
    print(f"    |3A - B| = {mag_C:.2f}")

    # (c) Unit vector along A + 2B
    D = A + 2 * B
    unit_D = D / np.linalg.norm(D)
    print(f"(c) A + 2B = {D}")
    print(f"    Unit vector a_c = ({unit_D[0]:.4f}, {unit_D[1]:.4f}, {unit_D[2]:.4f})")
    print(f"    Check |a_c| = {np.linalg.norm(unit_D):.6f}")

    # --- Visualization ---
    fig = plt.figure(figsize=(14, 6))

    # Plot 1: Vectors A, B, and A+2B
    ax1 = fig.add_subplot(121, projection='3d')
    setup_3d_ax(ax1, "Vectors A, B, A+2B (Ex. 1.1)", xlim=(-2, 18), ylim=(-6, 4), zlim=(-2, 14))

    origin = np.array([0, 0, 0])
    plot_3d_vector(ax1, origin, A, color='red', label='A')
    plot_3d_vector(ax1, origin, B, color='blue', label='B')
    plot_3d_vector(ax1, origin, D, color='green', label='A+2B')

    # Unit vectors along axes
    for i, (c, lbl) in enumerate(zip(['orange', 'purple', 'brown'],
                                     ['a_x', 'a_y', 'a_z'])):
        vec = np.zeros(3)
        vec[i] = 1
        plot_3d_vector(ax1, origin, vec, color=c, label=lbl, lw=1, mutation_scale=15)
    ax1.legend(loc='upper left', fontsize=10)

    # Plot 2: 3A - B
    ax2 = fig.add_subplot(122, projection='3d')
    setup_3d_ax(ax2, "3A - B (Ex. 1.1)", xlim=(-2, 35), ylim=(-15, 5), zlim=(-5, 25))

    plot_3d_vector(ax2, origin, A, color='red', label='A', lw=1)
    plot_3d_vector(ax2, origin, B, color='blue', label='B', lw=1)
    plot_3d_vector(ax2, origin, 3*A, color='orange', label='3A', lw=1.5)
    plot_3d_vector(ax2, origin, C, color='magenta', label='3A-B')
    ax2.legend(loc='upper left', fontsize=10)

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'ch1_ex1_1_vector_ops.png'), dpi=150)
    plt.close()
    print("    Figure saved: ch1_ex1_1_vector_ops.png\n")

    return A, B


# ============================================================
# Position and Distance Vectors — Example 1.2
# ============================================================
def example_1_2():
    """Reproduce Example 1.2:
    Points P(0,2,4) and Q(-3,1,5).
    Find: position vector of P, distance vector PQ, distance, vector parallel to PQ of magnitude 10.
    """
    print("=" * 60)
    print("EXAMPLE 1.2: Position and Distance Vectors")
    print("=" * 60)

    P = np.array([0, 2, 4])
    Q = np.array([-3, 1, 5])

    # (a) Position vector of P
    r_P = P
    print(f"(a) Position vector r_P = {r_P} = {r_P[0]}a_x + {r_P[1]}a_y + {r_P[2]}a_z")

    # (b) Distance vector from P to Q
    r_PQ = Q - P
    print(f"(b) Distance vector r_PQ = Q - P = {r_PQ}")

    # (c) Distance between P and Q
    d = np.linalg.norm(r_PQ)
    print(f"(c) Distance |r_PQ| = {d:.3f}")

    # (d) Vector parallel to PQ with magnitude 10
    A_mag = 10.0
    A = A_mag * r_PQ / np.linalg.norm(r_PQ)
    print(f"(d) Vector A (mag=10, parallel to PQ) = ({A[0]:.3f}, {A[1]:.3f}, {A[2]:.3f})")
    print(f"    Check |A| = {np.linalg.norm(A):.3f}")

    # --- Visualization ---
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    setup_3d_ax(ax, "Position & Distance Vectors (Ex. 1.2)",
                xlim=(-5, 3), ylim=(0, 5), zlim=(0, 8))

    origin = np.array([0, 0, 0])
    # Position vectors
    plot_3d_vector(ax, origin, r_P, color='blue', label='r_P', arrowstyle='-|>')
    plot_3d_vector(ax, origin, Q, color='green', label='r_Q', arrowstyle='-|>')
    # Distance vector at P
    plot_3d_vector(ax, P, r_PQ, color='red', label='r_PQ', arrowstyle='-|>')
    # Vector A
    plot_3d_vector(ax, origin, A, color='magenta', label='A (|| PQ, |A|=10)', arrowstyle='-|>')

    # Mark points
    ax.scatter(*P, color='blue', s=80, marker='o')
    ax.scatter(*Q, color='green', s=80, marker='o')
    ax.text(*P, ' P(0,2,4)', color='blue', fontsize=11)
    ax.text(*Q, ' Q(-3,1,5)', color='green', fontsize=11)

    ax.legend(loc='upper left', fontsize=9)
    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'ch1_ex1_2_position_vectors.png'), dpi=150)
    plt.close()
    print("    Figure saved: ch1_ex1_2_position_vectors.png\n")

    return P, Q, r_PQ


# ============================================================
# Angle Between Vectors — Example 1.4
# ============================================================
def example_1_4():
    """Reproduce Example 1.4:
    A = 3a_x + 4a_y + a_z, B = 2a_y - 5a_z.
    Find the angle between A and B using dot product and cross product.
    """
    print("=" * 60)
    print("EXAMPLE 1.4: Angle Between Vectors")
    print("=" * 60)

    A = np.array([3, 4, 1])
    B = np.array([0, 2, -5])

    dot_AB = np.dot(A, B)
    mag_A = np.linalg.norm(A)
    mag_B = np.linalg.norm(B)

    # Using dot product
    cos_theta = dot_AB / (mag_A * mag_B)
    theta_dot = np.degrees(np.arccos(cos_theta))
    print(f"A · B = {dot_AB}")
    print(f"|A| = sqrt({mag_A**2:.0f}) = {mag_A:.4f}")
    print(f"|B| = sqrt({mag_B**2:.0f}) = {mag_B:.4f}")
    print(f"cos θ = A·B/(|A||B|) = {cos_theta:.4f}")
    print(f"θ (dot) = {theta_dot:.2f}°")

    # Using cross product
    cross_AB = np.cross(A, B)
    mag_cross = np.linalg.norm(cross_AB)
    sin_theta = mag_cross / (mag_A * mag_B)
    theta_cross = np.degrees(np.arcsin(sin_theta))
    print(f"\nA × B = {cross_AB}")
    print(f"|A × B| = {mag_cross:.4f}")
    print(f"sin θ = |A×B|/(|A||B|) = {sin_theta:.4f}")
    print(f"θ (cross) = {theta_cross:.2f}°")

    # --- Visualization ---
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    setup_3d_ax(ax, f"Angle between A and B = {theta_dot:.2f}° (Ex. 1.4)",
                xlim=(-1, 6), ylim=(-6, 6), zlim=(-6, 4))

    origin = np.array([0, 0, 0])
    plot_3d_vector(ax, origin, A, color='red', label='A = (3,4,1)')
    plot_3d_vector(ax, origin, B, color='blue', label='B = (0,2,-5)')
    plot_3d_vector(ax, origin, cross_AB, color='green', label='A×B = (-22,15,6)', lw=1.5)

    # Add arc to show angle (approximate)
    theta_rad = np.radians(theta_dot)
    arc_points = 30
    t = np.linspace(0, theta_rad, arc_points)
    # Rotation in the plane of A and B
    radius = 1.5
    # Create a orthonormal basis in the A-B plane
    a_hat = A / mag_A
    # Component of B perpendicular to A
    b_perp = B - np.dot(B, a_hat) * a_hat
    b_hat = b_perp / np.linalg.norm(b_perp)
    arc_pts = np.outer(np.cos(t), a_hat) * radius + np.outer(np.sin(t), b_hat) * radius
    ax.plot(arc_pts[:, 0], arc_pts[:, 1], arc_pts[:, 2], 'k-', lw=2, alpha=0.7)

    ax.legend(loc='upper left', fontsize=9)
    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'ch1_ex1_4_angle_between_vectors.png'), dpi=150)
    plt.close()
    print("    Figure saved: ch1_ex1_4_angle_between_vectors.png\n")

    return A, B


# ============================================================
# Multiple Vector Operations — Example 1.5
# ============================================================
def example_1_5():
    """Reproduce Example 1.5:
    P = 2a_x - a_z, Q = 2a_x - a_y + 2a_z, R = 2a_x - 3a_y + a_z
    """
    print("=" * 60)
    print("EXAMPLE 1.5: Multiple Vector Operations")
    print("=" * 60)

    P = np.array([2, 0, -1])
    Q = np.array([2, -1, 2])
    R = np.array([2, -3, 1])

    # (a) (P+Q) × (P-Q) = 2(Q×P)
    P_plus_Q = P + Q
    P_minus_Q = P - Q
    cross_a = np.cross(P_plus_Q, P_minus_Q)
    print(f"(a) (P+Q) × (P-Q) = {cross_a}")
    # Should equal 2(Q×P)
    check_a = 2 * np.cross(Q, P)
    print(f"    2(Q×P) = {check_a}  [CHECK]")

    # (b) Q · R × P = 14
    scalar_triple_b = np.dot(Q, np.cross(R, P))
    print(f"(b) Q · (R × P) = {scalar_triple_b}")
    # Determinant check
    det_check = np.linalg.det(np.column_stack([Q, R, P]))
    print(f"    det([Q,R,P]) = {det_check:.0f}  [CHECK]")

    # (c) P · Q × R = 14 (cyclic permutation)
    scalar_triple_c = np.dot(P, np.cross(Q, R))
    print(f"(c) P · (Q × R) = {scalar_triple_c}")

    # (d) sin(θ_QR)
    cross_QR = np.cross(Q, R)
    sin_QR = np.linalg.norm(cross_QR) / (np.linalg.norm(Q) * np.linalg.norm(R))
    theta_QR = np.degrees(np.arcsin(sin_QR))
    print(f"(d) |Q×R| = {np.linalg.norm(cross_QR):.4f}")
    print(f"    |Q| = {np.linalg.norm(Q):.4f}, |R| = {np.linalg.norm(R):.4f}")
    print(f"    sin(θ_QR) = {sin_QR:.4f}")
    print(f"    θ_QR = {theta_QR:.2f}°")

    # (e) P × (Q × R) using bac-cab
    vec_triple_e = np.cross(P, cross_QR)
    # bac-cab: B(A·C) - C(A·B)
    P_dot_R = np.dot(P, R)
    P_dot_Q = np.dot(P, Q)
    bac_cab = P_dot_R * Q - P_dot_Q * R
    print(f"(e) P × (Q × R) = {vec_triple_e}")
    print(f"    Bac-cab: Q(P·R)-R(P·Q) = {bac_cab}  [CHECK]")

    # (f) Unit vector perpendicular to Q and R
    a_perp = cross_QR / np.linalg.norm(cross_QR)
    print(f"(f) Unit vector ⊥ Q,R: a = ±({a_perp[0]:.4f}, {a_perp[1]:.4f}, {a_perp[2]:.4f})")
    print(f"    |a| = {np.linalg.norm(a_perp):.4f}")
    print(f"    a·Q = {np.dot(a_perp, Q):.6f}  [⊥ check]")
    print(f"    a·R = {np.dot(a_perp, R):.6f}  [⊥ check]")

    # (g) Component of P along Q
    P_along_Q = (np.dot(P, Q) / np.linalg.norm(Q)**2) * Q
    print(f"(g) Component of P along Q = {P_along_Q}")
    print(f"    = ({P_along_Q[0]:.4f}, {P_along_Q[1]:.4f}, {P_along_Q[2]:.4f})")

    # --- Visualization: three vectors ---
    fig = plt.figure(figsize=(12, 5))

    ax1 = fig.add_subplot(121, projection='3d')
    setup_3d_ax(ax1, "Vectors P, Q, R (Ex. 1.5)",
                xlim=(-1, 5), ylim=(-5, 3), zlim=(-3, 4))
    origin = np.array([0, 0, 0])
    plot_3d_vector(ax1, origin, P, color='red', label='P=(2,0,-1)')
    plot_3d_vector(ax1, origin, Q, color='blue', label='Q=(2,-1,2)')
    plot_3d_vector(ax1, origin, R, color='green', label='R=(2,-3,1)')
    plot_3d_vector(ax1, origin, cross_QR, color='purple', label='Q×R', lw=1.5)
    ax1.legend(loc='upper left', fontsize=8)

    ax2 = fig.add_subplot(122, projection='3d')
    setup_3d_ax(ax2, "Scalar Triple Product: Vol = |P·(Q×R)| = 14",
                xlim=(-1, 5), ylim=(-5, 3), zlim=(-3, 4))
    plot_3d_vector(ax2, origin, P, color='red', lw=1.5)
    plot_3d_vector(ax2, origin, Q, color='blue', lw=1.5)
    plot_3d_vector(ax2, origin, R, color='green', lw=1.5)
    # Draw parallelepiped edges
    for vec1, vec2, c in [(P, Q, 'gray'), (P, R, 'gray'), (Q, R, 'gray')]:
        # Edge from vec1 tip parallel to vec2
        ax2.plot([vec1[0], vec1[0]+vec2[0]],
                 [vec1[1], vec1[1]+vec2[1]],
                 [vec1[2], vec1[2]+vec2[2]], 'gray', lw=0.8)
        # Edge from vec2 tip parallel to vec1
        ax2.plot([vec2[0], vec2[0]+vec1[0]],
                 [vec2[1], vec2[1]+vec1[1]],
                 [vec2[2], vec2[2]+vec1[2]], 'gray', lw=0.8)
    # Top face
    top = P + Q + R
    ax2.plot([top[0]-P[0], top[0]], [top[1]-P[1], top[1]], [top[2]-P[2], top[2]], 'gray', lw=0.8)
    ax2.plot([top[0]-Q[0], top[0]], [top[1]-Q[1], top[1]], [top[2]-Q[2], top[2]], 'gray', lw=0.8)
    ax2.scatter(*top, color='orange', s=60)
    ax2.text(*top, ' P+Q+R', color='orange', fontsize=9)
    ax2.legend(loc='upper left', fontsize=8)

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'ch1_ex1_5_vector_products.png'), dpi=150)
    plt.close()
    print("    Figure saved: ch1_ex1_5_vector_products.png\n")

    return P, Q, R


# ============================================================
# Cosine and Sine Formulas — Example 1.6
# ============================================================
def example_1_6():
    """Demonstrate the cosine and sine formulas using vectors."""
    print("=" * 60)
    print("EXAMPLE 1.6: Cosine and Sine Laws via Vectors")
    print("=" * 60)

    # Create a triangle
    A_pt = np.array([0, 0, 0])
    B_pt = np.array([4, 0, 0])
    C_pt = np.array([1, 3, 0])

    # Sides as vectors
    b = C_pt - A_pt  # side from A to C (opposite B)
    c = B_pt - A_pt  # side from A to B (opposite C)
    a_vec = B_pt - C_pt  # side from C to B (opposite A)

    a = np.linalg.norm(a_vec)
    b_len = np.linalg.norm(b)
    c_len = np.linalg.norm(c)

    # Law of cosines: a² = b² + c² - 2bc cos(A)
    cos_A = (b_len**2 + c_len**2 - a**2) / (2 * b_len * c_len)
    A_angle = np.degrees(np.arccos(cos_A))
    print(f"Triangle sides: a={a:.3f}, b={b_len:.3f}, c={c_len:.3f}")
    print(f"Law of Cosines: a² = b² + c² - 2bc·cos(A)")
    print(f"  LHS: a² = {a**2:.3f}")
    print(f"  RHS: b² + c² - 2bc·cos(A) = {b_len**2:.3f} + {c_len**2:.3f}"
          f" - 2*{b_len:.3f}*{c_len:.3f}*{cos_A:.4f} = {a**2:.3f}")

    # Law of sines: sin(A)/a = sin(B)/b = sin(C)/c
    B_angle = np.degrees(np.arccos((a**2 + c_len**2 - b_len**2) / (2 * a * c_len)))
    C_angle = 180 - A_angle - B_angle
    sin_A_by_a = np.sin(np.radians(A_angle)) / a
    sin_B_by_b = np.sin(np.radians(B_angle)) / b_len
    sin_C_by_c = np.sin(np.radians(C_angle)) / c_len
    print(f"\nLaw of Sines: sin(A)/a = sin(B)/b = sin(C)/c")
    print(f"  sin(A)/a = {sin_A_by_a:.4f}")
    print(f"  sin(B)/b = {sin_B_by_b:.4f}")
    print(f"  sin(C)/c = {sin_C_by_c:.4f}")
    print(f"  Angles: A={A_angle:.2f}°, B={B_angle:.2f}°, C={C_angle:.2f}°")
    print(f"  Sum = {A_angle + B_angle + C_angle:.2f}°")

    # --- Visualization ---
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_aspect('equal')

    triangle = np.column_stack([A_pt, B_pt, C_pt, A_pt])
    ax.plot(triangle[0], triangle[1], 'b-o', lw=2, markersize=8)
    ax.text(A_pt[0], A_pt[1], ' A', fontsize=14, weight='bold')
    ax.text(B_pt[0], B_pt[1], ' B', fontsize=14, weight='bold')
    ax.text(C_pt[0], C_pt[1], ' C', fontsize=14, weight='bold')

    # Side labels
    ax.text((A_pt[0]+C_pt[0])/2 - 0.3, (A_pt[1]+C_pt[1])/2 + 0.2, f'b={b_len:.1f}', fontsize=12)
    ax.text((A_pt[0]+B_pt[0])/2, (A_pt[1]+B_pt[1])/2 - 0.4, f'c={c_len:.1f}', fontsize=12)
    ax.text((B_pt[0]+C_pt[0])/2 + 0.2, (B_pt[1]+C_pt[1])/2, f'a={a:.1f}', fontsize=12)

    # Angle labels
    ax.text(A_pt[0]+0.5, A_pt[1]+0.3, f'A={A_angle:.0f}°', fontsize=11, color='red')
    ax.text(B_pt[0]-1.2, B_pt[1]+0.3, f'B={B_angle:.0f}°', fontsize=11, color='red')
    ax.text(C_pt[0]-0.1, C_pt[1]-0.4, f'C={C_angle:.0f}°', fontsize=11, color='red')

    ax.set_xlim(-0.5, 5)
    ax.set_ylim(-0.5, 4)
    ax.grid(True, alpha=0.3)
    ax.set_title("Triangle: Law of Cosines & Law of Sines (Ex. 1.6)", fontsize=13)
    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'ch1_ex1_6_triangle_laws.png'), dpi=150)
    plt.close()
    print("    Figure saved: ch1_ex1_6_triangle_laws.png\n")


# ============================================================
# Collinearity and Distance to Line — Example 1.7
# ============================================================
def example_1_7():
    """Reproduce Example 1.7:
    Points P1(5,2,-4), P2(1,1,-2), P3(-3,0,8) — check collinearity.
    Shortest distance from P4(3,-1,0) to the line.
    """
    print("=" * 60)
    print("EXAMPLE 1.7: Collinearity & Distance to Line")
    print("=" * 60)

    P1 = np.array([5, 2, -4])
    P2 = np.array([1, 1, 2])
    P3 = np.array([-3, 0, 8])
    P4 = np.array([3, -1, 0])

    # Distance vectors
    r_P1P2 = P2 - P1
    r_P1P3 = P3 - P1
    r_P1P4 = P4 - P1

    print(f"r_P1P2 = {r_P1P2}")
    print(f"r_P1P3 = {r_P1P3}")
    print(f"r_P1P4 = {r_P1P4}")

    # Check collinearity: cross product should be zero
    cross_check = np.cross(r_P1P2, r_P1P3)
    print(f"\nr_P1P2 × r_P1P3 = {cross_check}")
    if np.allclose(cross_check, 0):
        print("→ P1, P2, P3 are COLLINEAR (cross product = 0)")
    else:
        print("→ P1, P2, P3 are NOT collinear")

    # Check if P3 lies on the line: r_P3 = P1 + λ*r_P1P2
    for lam in np.linspace(-3, 3, 7):
        test_pt = P1 + lam * r_P1P2
        if np.allclose(test_pt, P3):
            print(f"→ P3 is on the line with λ = {lam}")
            break

    # Shortest distance from P4 to line
    d = np.linalg.norm(np.cross(r_P1P4, r_P1P2)) / np.linalg.norm(r_P1P2)
    print(f"\nShortest distance from P4 to line = {d:.3f}")

    # Alternative using unit vector
    a_P1P2 = r_P1P2 / np.linalg.norm(r_P1P2)
    d_alt = np.linalg.norm(np.cross(r_P1P4, a_P1P2))
    print(f"Alt. method (cross with unit vector) = {d_alt:.3f}")

    # Find the foot of perpendicular
    t = np.dot(P4 - P1, a_P1P2)
    foot = P1 + t * a_P1P2
    print(f"Foot of perpendicular from P4 to line: {foot}")
    print(f"Distance foot-P4: {np.linalg.norm(P4 - foot):.3f}")

    # --- Visualization ---
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    setup_3d_ax(ax, "Collinearity & Distance to Line (Ex. 1.7)",
                xlim=(-5, 8), ylim=(-3, 5), zlim=(-8, 12))

    # Line P1-P2
    line_pts = np.column_stack([P1 + lam * r_P1P2 for lam in np.linspace(0, 2, 10)])
    ax.plot(line_pts[0], line_pts[1], line_pts[2], 'gray', lw=1, alpha=0.5, label='Line P1-P2')

    # Points
    for pt, label, color in [(P1, 'P1', 'red'), (P2, 'P2', 'blue'),
                              (P3, 'P3', 'green'), (P4, 'P4', 'magenta')]:
        ax.scatter(*pt, color=color, s=80)
        ax.text(*pt, f'  {label}', color=color, fontsize=12, weight='bold')

    # Vectors from P1
    plot_3d_vector(ax, P1, r_P1P2, color='red', lw=1.5, label='r_P1P2')
    plot_3d_vector(ax, P1, r_P1P3, color='green', lw=1.5, label='r_P1P3')
    plot_3d_vector(ax, P1, r_P1P4, color='magenta', lw=1.5, label='r_P1P4')

    # Perpendicular distance
    plot_3d_vector(ax, P4, foot - P4, color='orange', lw=2,
                   label=f'⊥ distance = {d:.3f}', arrowstyle='-')
    ax.scatter(*foot, color='orange', s=60, marker='x')

    ax.legend(loc='upper left', fontsize=9)
    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'ch1_ex1_7_collinearity_distance.png'), dpi=150)
    plt.close()
    print("    Figure saved: ch1_ex1_7_collinearity_distance.png\n")


# ============================================================
# Vector Projection Visualization
# ============================================================
def vector_projection_visualization():
    """Visualize scalar and vector projection of A onto B."""
    print("=" * 60)
    print("VECTOR PROJECTION VISUALIZATION (Section 1.8)")
    print("=" * 60)

    A = np.array([4, 3, 0])
    B = np.array([5, 1, 0])

    a_B = B / np.linalg.norm(B)
    A_B_scalar = np.dot(A, a_B)
    A_B_vector = A_B_scalar * a_B
    A_perp = A - A_B_vector

    print(f"A = {A}")
    print(f"B = {B}")
    print(f"Scalar component of A along B: A·a_B = {A_B_scalar:.3f}")
    print(f"Vector component of A along B: A_B = {A_B_vector}")
    print(f"Component of A ⊥ B: {A_perp}")
    print(f"Check: A_B + A_perp = {A_B_vector + A_perp}")
    print(f"Check A⊥·B = {np.dot(A_perp, B):.6f}")

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_aspect('equal')

    ox, oy = 0, 0

    # Draw vectors (2D only)
    ax.quiver(ox, oy, A[0], A[1], angles='xy', scale_units='xy', scale=1, color='red',
              width=0.03, label='A')
    ax.quiver(ox, oy, B[0], B[1], angles='xy', scale_units='xy', scale=1, color='blue',
              width=0.03, label='B')
    ax.quiver(ox, oy, A_B_vector[0], A_B_vector[1], angles='xy', scale_units='xy', scale=1,
              color='green', width=0.04, label='A_B (projection)')
    ax.quiver(A_B_vector[0], A_B_vector[1], A_perp[0], A_perp[1], angles='xy',
              scale_units='xy', scale=1, color='orange', width=0.03, label='A_⊥ (perp)')

    # Dotted line from A tip to projection
    ax.plot([A[0], A_B_vector[0]], [A[1], A_B_vector[1]], 'k--', lw=1)

    # Angle arc
    theta = np.arctan2(A[1], A[0]) - np.arctan2(B[1], B[0])
    theta_deg = np.degrees(theta)
    arc = np.linspace(0, theta, 30)
    r = 0.5
    ax.plot(r * np.cos(arc), r * np.sin(arc), 'k-', lw=1.5)
    ax.text(0.7, 0.3, f'θ={theta_deg:.1f}°', fontsize=11)

    ax.set_xlim(-0.5, 6)
    ax.set_ylim(-0.5, 5)
    ax.grid(True, alpha=0.3)
    ax.set_title("Vector Projection: A = A_B + A_⊥ (Section 1.8)", fontsize=13)
    ax.legend(fontsize=11)
    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'ch1_vector_projection.png'), dpi=150)
    plt.close()
    print("    Figure saved: ch1_vector_projection.png\n")


# ============================================================
# 3D Vector Field Visualization (quiver & streamplot concepts)
# ============================================================
def vector_field_visualization():
    """Visualize a simple 3D vector field and scalar field contours."""
    print("=" * 60)
    print("VECTOR/S CALAR FIELD VISUALIZATION (Section 1.3)")
    print("=" * 60)

    # Create a simple vector field: A = x*a_x + y*a_y (2D radial field)
    x = np.linspace(-2, 2, 10)
    y = np.linspace(-2, 2, 10)
    X, Y = np.meshgrid(x, y)
    U = X
    V = Y
    W = np.sqrt(X**2 + Y**2)  # magnitude as z

    fig = plt.figure(figsize=(12, 5))

    # Plot 1: Quiver (vector field)
    ax1 = fig.add_subplot(121)
    q = ax1.quiver(X, Y, U, V, W, cmap='viridis', scale=5, width=0.008)
    ax1.streamplot(X, Y, U, V, color='gray', density=0.8, linewidth=0.5)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('Vector Field: A = x·a_x + y·a_y')
    ax1.set_aspect('equal')
    plt.colorbar(q, ax=ax1, label='|A|')

    # Plot 2: Scalar field contours (magnitude)
    ax2 = fig.add_subplot(122)
    contour = ax2.contourf(X, Y, W, levels=15, cmap='plasma')
    ax2.contour(X, Y, W, levels=10, colors='white', linewidths=0.5)
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_title('Scalar Field: |A| = sqrt(x² + y²)')
    ax2.set_aspect('equal')
    plt.colorbar(contour, ax=ax2, label='|A|')

    plt.tight_layout()
    fig.savefig(os.path.join(FIG_DIR, 'ch1_vector_field_demo.png'), dpi=150)
    plt.close()
    print("    Figure saved: ch1_vector_field_demo.png\n")


# ============================================================
# Practice Exercise 1.1
# ============================================================
def practice_1_1():
    """Practice Exercise 1.1:
    A = a_x + 3a_z, B = 5a_x + 2a_y - 6a_z
    (a) |A + B|, (b) 5A - B, (c) component of A along a_y, (d) unit vector ∥ 3A + B
    """
    print("=" * 60)
    print("PRACTICE EXERCISE 1.1")
    print("=" * 60)

    A = np.array([1, 0, 3])
    B = np.array([5, 2, -6])

    A_plus_B = A + B
    print(f"(a) |A+B| = {np.linalg.norm(A_plus_B)}  (expected: 7)")

    five_A_minus_B = 5 * A - B
    print(f"(b) 5A - B = {five_A_minus_B}  (expected: (0, -2, 21))")

    print(f"(c) Component of A along a_y = {A[1]}  (expected: 0)")

    vec_3A_plus_B = 3 * A + B
    unit = vec_3A_plus_B / np.linalg.norm(vec_3A_plus_B)
    print(f"(d) Unit vector ∥ 3A+B = ({unit[0]:.4f}, {unit[1]:.4f}, {unit[2]:.4f})")
    print(f"    Expected: ±(0.9117, 0.2279, 0.3419)")
    print()


# ============================================================
# Practice Exercise 1.2
# ============================================================
def practice_1_2():
    """Practice Exercise 1.2:
    P(1,-3,5), Q(2,4,6), R(0,3,8)
    """
    print("=" * 60)
    print("PRACTICE EXERCISE 1.2")
    print("=" * 60)

    P = np.array([1, -3, 5])
    Q = np.array([2, 4, 6])
    R = np.array([0, 3, 8])

    r_P = P
    r_R = R
    print(f"(a) r_P = {r_P}")
    print(f"    r_R = {r_R}")

    r_QR = R - Q
    print(f"(b) r_QR = {r_QR}")

    dist_QR = np.linalg.norm(r_QR)
    print(f"(c) Distance Q-R = {dist_QR}  (expected: 3)")
    print()


# ============================================================
# Practice Exercise 1.3 — Airplane vector problem
# ============================================================
def practice_1_3():
    """Practice Exercise 1.3:
    Ground speed 350 km/hr due west, wind 40 km/hr northwest.
    Find true air speed and heading.
    """
    print("=" * 60)
    print("PRACTICE EXERCISE 1.3: Airplane Heading")
    print("=" * 60)

    # Ground velocity vector (due west = negative x)
    v_ground = np.array([-350.0, 0.0])

    # Wind velocity (northwest = 135° from positive x)
    v_wind = np.array([40 * np.cos(np.radians(315)), 40 * np.sin(np.radians(315))])
    print(f"Wind vector: ({v_wind[0]:.3f}, {v_wind[1]:.3f}) km/hr")

    # v_ground = v_air + v_wind → v_air = v_ground - v_wind
    v_air = v_ground - v_wind
    air_speed = np.linalg.norm(v_air)
    # Heading angle: angle of v_air from due west
    # v_air_x is negative, v_air_y is positive (north of west)
    # Heading: angle north of west
    north_of_west = np.degrees(np.arctan2(abs(v_air[1]), abs(v_air[0])))

    print(f"Air speed = {air_speed:.1f} km/hr  (expected: 379.3)")
    print(f"Heading = {north_of_west:.3f}° north of west  (expected: 4.275°)")
    print()


# ============================================================
# Practice Exercise 1.4
# ============================================================
def practice_1_4():
    """Practice Exercise 1.4:
    A = a_x + 3a_z, B = 5a_x + 2a_y - 6a_z. Find θ_AB.
    """
    print("=" * 60)
    print("PRACTICE EXERCISE 1.4: Angle between A and B")
    print("=" * 60)

    A = np.array([1, 0, 3])
    B = np.array([5, 2, -6])

    cos_theta = np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))
    theta = np.degrees(np.arccos(cos_theta))
    print(f"θ_AB = {theta:.1f}°  (expected: 120.6°)")
    print()


# ============================================================
# Main execution
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("CHAPTER 1: VECTOR ALGEBRA — SADIKU 7th Ed.")
    print("Example Code & Visualizations")
    print("=" * 60)

    example_1_1()
    example_1_2()
    example_1_4()
    example_1_5()
    example_1_6()
    example_1_7()
    vector_projection_visualization()
    vector_field_visualization()

    practice_1_1()
    practice_1_2()
    practice_1_3()
    practice_1_4()

    print("=" * 60)
    print("ALL EXAMPLES COMPLETED SUCCESSFULLY")
    print("=" * 60)
