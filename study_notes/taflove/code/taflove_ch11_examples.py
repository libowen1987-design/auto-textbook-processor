#!/usr/bin/env python3
"""
taflove_ch11_examples.py — Nonuniform Grids, Subgrids

Examples:
  1. Nonuniform graded mesh: waveguide with fine resolution at the center
  2. Subgridding: 2:1 nested subgrid for a resonant cavity with fine feature
  3. Stability comparison: uniform vs. nonuniform grid CFL limits
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.constants import c, mu_0, epsilon_0, pi

# =====================================================================
# Example 1: Nonuniform Graded Mesh for a Waveguide
# =====================================================================
def example_1_nonuniform_mesh():
    """
    Construct a nonuniform (graded) mesh for a waveguide problem.
    Finer cells near the center (where the field varies rapidly),
    coarser cells near the boundaries. Compare with uniform mesh.
    """
    print("=" * 72)
    print("Example 1: Nonuniform Graded Mesh for Waveguide")
    print("=" * 72)

    # Domain: waveguide cross-section 20 mm × 10 mm
    Lx = 20e-3  # 20 mm width
    Ly = 10e-3  # 10 mm height
    frequency = 15e9  # 15 GHz
    lambda_0 = c / frequency

    # Graded mesh: refinement factor
    # Fine region in center (0.4L to 0.6L), coarse near edges
    def graded_coordinates(L, N_total, refinement_ratio=3.0):
        """Create graded coordinates with finer cells in the center."""
        # Generate nodes using a hyperbolic tangent stretching function
        xi = np.linspace(-1, 1, N_total)
        # Tanh stretching for grading
        beta = np.arctanh(1.0 / refinement_ratio)
        s = np.tanh(beta * xi) / np.tanh(beta)
        # Map to [0, L]
        x = L * (s + 1) / 2
        return x

    Nx_uniform = 40
    Ny_uniform = 20
    Nx_graded = 40
    Ny_graded = 20

    x_uniform = np.linspace(0, Lx, Nx_uniform)
    y_uniform = np.linspace(0, Ly, Ny_uniform)
    x_graded = graded_coordinates(Lx, Nx_graded)
    y_graded = graded_coordinates(Ly, Ny_graded)

    # Cell sizes
    dx_uniform = np.diff(x_uniform)
    dy_uniform = np.diff(y_uniform)
    dx_graded = np.diff(x_graded)
    dy_graded = np.diff(y_graded)

    # Profile of cell sizes
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))

    # Cell size vs. position
    x_center_uniform = (x_uniform[:-1] + x_uniform[1:]) / 2
    x_center_graded = (x_graded[:-1] + x_graded[1:]) / 2

    ax1.plot(x_center_uniform * 1e3, dx_uniform * 1e3, 'b.-', label='Uniform')
    ax1.plot(x_center_graded * 1e3, dx_graded * 1e3, 'r.-', label='Graded (tanh)')
    ax1.set_xlabel('x [mm]')
    ax1.set_ylabel(r'$\Delta x$ [mm]')
    ax1.set_title('Cell Size Distribution (x-direction)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # 2D mesh visualization
    Xg, Yg = np.meshgrid(x_graded, y_graded)

    ax2.plot(Xg, Yg, 'k-', linewidth=0.5, alpha=0.5)
    ax2.plot(Xg.T, Yg.T, 'k-', linewidth=0.5, alpha=0.5)
    ax2.set_xlabel('x [mm]')
    ax2.set_ylabel('y [mm]')
    ax2.set_title('Graded Mesh (2D View)')
    ax2.set_aspect('equal')
    ax2.set_xlim([0, Lx * 1e3])
    ax2.set_ylim([0, Ly * 1e3])

    # CFL time-step comparison
    dx_min_uniform = np.min(dx_uniform)
    dy_min_uniform = np.min(dy_uniform)
    dx_min_graded = np.min(dx_graded)
    dy_min_graded = np.min(dy_graded)

    dt_uniform = 0.99 / (c * np.sqrt(1/dx_min_uniform**2 + 1/dy_min_uniform**2))
    dt_graded = 0.99 / (c * np.sqrt(1/dx_min_graded**2 + 1/dy_min_graded**2))

    # Number of cells
    N_cells_uniform = len(dx_uniform) * len(dy_uniform)
    N_cells_graded = len(dx_graded) * len(dy_graded)

    # Display comparison
    metrics = [
        ("Number of cells", N_cells_uniform, N_cells_graded),
        ("Min Δx [mm]", np.min(dx_uniform)*1e3, np.min(dx_graded)*1e3),
        ("Min Δy [mm]", np.min(dy_uniform)*1e3, np.min(dy_graded)*1e3),
        ("Max Δx [mm]", np.max(dx_uniform)*1e3, np.max(dx_graded)*1e3),
        ("Max Δy [mm]", np.max(dy_uniform)*1e3, np.max(dy_graded)*1e3),
        ("Max-to-min ratio", 1.0, np.max(dx_graded)/np.min(dx_graded)),
        ("CFL time-step [ps]", dt_uniform*1e12, dt_graded*1e12),
    ]

    print(f"  {'Metric':<25s} {'Uniform':>15s} {'Graded':>15s}")
    print(f"  {'-'*55}")
    for name, u, g in metrics:
        if isinstance(u, float):
            print(f"  {name:<25s} {u:15.4f} {g:15.4f}")
        else:
            print(f"  {name:<25s} {u:>15d} {g:>15d}")

    # Bar chart comparing cell-size distribution
    ax3.hist(dx_graded * 1e3, bins=20, alpha=0.7, color='red', label='Graded')
    ax3.axvline(np.min(dx_uniform)*1e3, color='blue', linestyle='--', label=f'Uniform min ({np.min(dx_uniform)*1e3:.3f} mm)')
    ax3.set_xlabel(r'$\Delta x$ [mm]')
    ax3.set_ylabel('Count')
    ax3.set_title('Cell Size Distribution Histogram')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    # Supraconvergence: accuracy vs. mesh resolution
    cells_per_wavelength = np.array([8, 12, 16, 24, 32, 48, 64])
    error_uniform = 5.0 * (cells_per_wavelength[0] / cells_per_wavelength)**2  # O(h^2)
    error_nongraded = 5.0 * (cells_per_wavelength[0] / cells_per_wavelength)**1.0  # O(h) worst-case
    error_supra = 5.0 * (cells_per_wavelength[0] / cells_per_wavelength)**1.8  # nearly O(h^2)

    ax4.loglog(cells_per_wavelength, error_uniform, 'bs-', label='Uniform (O(h²))')
    ax4.loglog(cells_per_wavelength, error_nongraded, 'r--', label='Nonuniform, no supraconv. (O(h))')
    ax4.loglog(cells_per_wavelength, error_supra, 'g^-', label='Nonuniform with supraconv. (~O(h^1.8))')
    ax4.set_xlabel('Cells per Wavelength')
    ax4.set_ylabel('Normalized Error')
    ax4.set_title('Supraconvergence Effect')
    ax4.legend()
    ax4.grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    plt.savefig('/tmp/taflove_ch11_ex1_nonuniform_mesh.png', dpi=150)
    plt.close()
    print(f"\n  Saved /tmp/taflove_ch11_ex1_nonuniform_mesh.png")
    print()

    return x_graded, y_graded, dx_graded, dy_graded


# =====================================================================
# Example 2: 2:1 Subgrid for Resonant Cavity with Fine Post
# =====================================================================
def example_2_subgrid_cavity():
    """
    Model a rectangular cavity with a small cylindrical post using
    a 2:1 subgrid refinement around the post.
    Compute resonant frequency shift due to the post.
    """
    print("=" * 72)
    print("Example 2: Subgridded Cavity with Fine Post")
    print("=" * 72)

    # Cavity dimensions (WR-90 waveguide, shorted at both ends)
    a_width = 22.86e-3  # 22.86 mm
    b_height = 10.16e-3  # 10.16 mm
    L_length = 30.0e-3  # 30 mm
    mode_TE101 = (1, 0, 1)

    # TE101 resonant frequency (empty cavity)
    # Rectangular cavity resonant frequency: f_mnp = (c/2)*sqrt((m/a)² + (n/b)² + (p/L)²)
    f_TE101 = (c / 2) * np.sqrt((mode_TE101[0]/a_width)**2 +
                                (mode_TE101[1]/b_height)**2 +
                                (mode_TE101[2]/L_length)**2)
    print(f"  Empty cavity TE101: {f_TE101/1e9:.4f} GHz")

    # Small cylindrical post at center
    post_radius = 0.5e-3  # 0.5 mm radius
    post_height = b_height  # Full height
    post_epsilon_r = 10.0  # Dielectric post

    # Primary grid: 20 cells/wavelength at f_TE101
    # This is coarse — the post would be poorly resolved
    lambda_TE101 = c / f_TE101
    primary_cells_per_lambda = 20
    delta_primary = lambda_TE101 / primary_cells_per_lambda

    Nx_primary = int(np.ceil(a_width / delta_primary)) + 1
    Ny_primary = int(np.ceil(b_height / delta_primary)) + 1
    Nz_primary = int(np.ceil(L_length / delta_primary)) + 1

    print(f"  Primary cell size: {delta_primary*1e3:.3f} mm")
    print(f"  Primary grid: {Nx_primary} × {Ny_primary} × {Nz_primary}")

    # Subgrid: 2:1 refinement around the post
    delta_sub = delta_primary / 2
    print(f"  Subgrid cell size: {delta_sub*1e3:.3f} mm")

    # Post resolved in subgrid
    post_cells_sub = int(post_radius / delta_sub)
    print(f"  Post radius in subgrid cells: {post_cells_sub}")

    # Resonant frequency perturbation
    # Slater perturbation formula:
    # Δf/f0 = -(epsilon_r - 1) * (∫_V_post E·E0 dV) / (2 * ∫_V_cavity |E0|^2 dV)
    # For TE101 mode, E = E0 * sin(pi*x/a) * sin(pi*z/L)
    # At center (x=a/2, z=L/2): E is maximum

    # Normalize to peak E-field at center = 1 V/m
    # Volume integral of |E|^2 over cavity
    # ∫_V sin²(pi*x/a) * sin²(pi*z/L) dx dy dz
    # = (a/2) * b * (L/2) = a*b*L/4
    V_cavity = a_width * b_height * L_length
    integral_E2_cavity = V_cavity / 4

    # Volume integral over post (cylindrical, radius r, height b)
    # ∫_V_post sin²(pi*x/a) * sin²(pi*z/L) dV
    # For small post at center, sin² terms ≈ 1
    V_post = pi * post_radius**2 * b_height
    integral_E2_post = V_post * 1.0  # Approximate (sin² ≈ 1 at center)

    # Frequency shift
    delta_f = -(post_epsilon_r - 1) * integral_E2_post / (2 * integral_E2_cavity) * f_TE101
    f_perturbed = f_TE101 + delta_f

    print(f"  Post volume fraction: {V_post/V_cavity*100:.4f}%")
    print(f"  Frequency shift: {delta_f/1e6:.4f} MHz")
    print(f"  Perturbed frequency: {f_perturbed/1e9:.4f} GHz")

    # Visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Subgrid geometry
    center_x, center_z = a_width/2, L_length/2

    # Primary grid outline
    x_primary = np.linspace(0, a_width, int(Nx_primary))
    z_primary = np.linspace(0, L_length, int(Nz_primary))
    Xp, Zp = np.meshgrid(x_primary, z_primary)

    ax1.plot(Xp, Zp, 'b-', linewidth=0.3, alpha=0.3)
    ax1.plot(Xp.T, Zp.T, 'b-', linewidth=0.3, alpha=0.3)

    # Subgrid region (2:1 around post)
    subgrid_half = 3 * delta_primary  # 3 primary cells in each direction
    x_sub = np.linspace(center_x - subgrid_half, center_x + subgrid_half,
                        int(2*subgrid_half/delta_sub) + 1)
    z_sub = np.linspace(center_z - subgrid_half, center_z + subgrid_half,
                        int(2*subgrid_half/delta_sub) + 1)
    Xs, Zs = np.meshgrid(x_sub, z_sub)

    ax1.plot(Xs, Zs, 'r-', linewidth=0.5, alpha=0.7)
    ax1.plot(Xs.T, Zs.T, 'r-', linewidth=0.5, alpha=0.7)

    # Post (circle)
    theta = np.linspace(0, 2*pi, 100)
    ax1.plot(center_x + post_radius * np.cos(theta),
             center_z + post_radius * np.sin(theta),
             'k-', linewidth=2, label=f'Post (r={post_radius*1e3:.1f} mm)')

    ax1.set_xlabel('x [m]')
    ax1.set_ylabel('z [m]')
    ax1.set_title('Subgrid Geometry (xz-plane)')
    ax1.legend()
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)

    # Frequency shift vs. post permittivity
    epsilon_r_range = np.linspace(1, 50, 100)
    delta_f_range = -(epsilon_r_range - 1) * integral_E2_post / (2 * integral_E2_cavity) * f_TE101

    ax2.plot(epsilon_r_range, delta_f_range/1e6, 'g-', linewidth=2)
    ax2.axvline(post_epsilon_r, color='r', linestyle='--', alpha=0.5,
                label=f'Selected ε_r = {post_epsilon_r}')
    ax2.set_xlabel('Post Relative Permittivity $\\varepsilon_r$')
    ax2.set_ylabel('Frequency Shift $\\Delta f$ [MHz]')
    ax2.set_title('Resonant Frequency Shift vs. Post Permittivity')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/tmp/taflove_ch11_ex2_subgrid_cavity.png', dpi=150)
    plt.close()
    print(f"\n  Saved /tmp/taflove_ch11_ex2_subgrid_cavity.png")
    print()

    return f_TE101, f_perturbed, post_radius


# =====================================================================
# Example 3: Curvilinear Coordinate Mapping
# =====================================================================
def example_3_curvilinear_mapping():
    """
    Demonstrate a nonorthogonal curvilinear coordinate mapping from
    a Cartesian computational space to a physical space with curved boundaries.
    Compute the metric tensor elements.
    """
    print("=" * 72)
    print("Example 3: Curvilinear Coordinate Mapping")
    print("=" * 72)

    # Physical domain: a cosine-modulated waveguide
    # y(x) = h0 + A * cos(2*pi*x/L)
    # This creates a smoothly varying curved wall

    L = 1.0  # Length
    h0 = 0.3  # Mean height
    A_amplitude = 0.1  # Wall modulation amplitude

    # Computational grid (uniform in (u,v) space)
    Nu, Nv = 30, 15
    u = np.linspace(0, L, Nu)
    v = np.linspace(0, 1, Nv)

    U, V = np.meshgrid(u, v)

    # Mapping from (u,v) to (x,y)
    # x = u
    # y = v * (h0 + A * cos(2*pi*u/L))
    y_wall = h0 + A_amplitude * np.cos(2 * pi * U / L)
    X_phys = U.copy()
    Y_phys = V * y_wall

    # Compute metric tensor elements numerically
    # g_ij = dr/du^i · dr/du^j
    # r = [x, y]^T = [u, v*(h0 + A*cos(2*pi*u/L))]^T

    du = u[1] - u[0]
    dv = v[1] - v[0]

    # Partial derivatives via central differences
    dX_du = np.ones_like(X_phys)
    dX_dv = np.zeros_like(X_phys)

    dY_du = np.zeros_like(Y_phys)
    dY_dv = np.zeros_like(Y_phys)

    for i in range(1, Nu-1):
        for j in range(1, Nv-1):
            dY_du[j, i] = (Y_phys[j, i+1] - Y_phys[j, i-1]) / (2*du)
            dY_dv[j, i] = (Y_phys[j+1, i] - Y_phys[j-1, i]) / (2*dv)

    # Metric tensor elements
    g_11 = dX_du**2 + dY_du**2
    g_12 = dX_du * dX_dv + dY_du * dY_dv
    g_22 = dX_dv**2 + dY_dv**2

    # Determinant
    g = g_11 * g_22 - g_12**2

    # CFL condition: dt <= 2/(c*sqrt(g^11 + g^22))
    # For 2D: g^11 = g_22/g, g^22 = g_11/g
    g_11_inv = g_22 / g
    g_22_inv = g_11 / g
    dt_cfl = 2.0 / (np.sqrt(g_11_inv + g_22_inv))

    print(f"  Physical domain: L={L}, h0={h0}, A={A_amplitude}")
    print(f"  Computational grid: {Nu}x{Nv}")
    print(f"  Metric tensor ranges:")
    print(f"    g_11: [{np.min(g_11):.4f}, {np.max(g_11):.4f}]")
    print(f"    g_22: [{np.min(g_22):.4f}, {np.max(g_22):.4f}]")
    print(f"    g_12: [{np.min(g_12):.4f}, {np.max(g_12):.4f}]")
    print(f"  g (determinant): [{np.min(g):.4f}, {np.max(g):.4f}]")
    print(f"  CFL time-step factor (relative to uniform):")
    print(f"    Min: {np.min(dt_cfl):.4f}, Max: {np.max(dt_cfl):.4f}")

    # Create visualization
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

    # Physical grid
    ax1.plot(X_phys, Y_phys, 'b-', linewidth=0.5)
    ax1.plot(X_phys.T, Y_phys.T, 'b-', linewidth=0.5)
    # Wall boundary
    ax1.plot(X_phys[0, :], y_wall[0, :], 'r-', linewidth=2, label='Curved wall')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('Physical Grid (Curved Wall)')
    ax1.legend()
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)

    # g_11 (metric element)
    im2 = ax2.contourf(X_phys, Y_phys, g_11, levels=20, cmap='viridis')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_title('Metric Element $g_{11}$')
    plt.colorbar(im2, ax=ax2)

    # g (determinant)
    im3 = ax3.contourf(X_phys, Y_phys, g, levels=20, cmap='plasma')
    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    ax3.set_title('Metric Determinant $g = \\det(g_{ij})$')
    plt.colorbar(im3, ax=ax3)

    # CFL time-step map
    im4 = ax4.contourf(X_phys, Y_phys, dt_cfl, levels=20, cmap='coolwarm')
    ax4.set_xlabel('x')
    ax4.set_ylabel('y')
    ax4.set_title('Normalized CFL Time-Step Limit')
    plt.colorbar(im4, ax=ax4)

    plt.tight_layout()
    plt.savefig('/tmp/taflove_ch11_ex3_curvilinear_mapping.png', dpi=150)
    plt.close()
    print(f"\n  Saved /tmp/taflove_ch11_ex3_curvilinear_mapping.png")
    print()

    return X_phys, Y_phys, g_11, g_22, g_12, g


# =====================================================================
if __name__ == "__main__":
    print()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  Taflove Ch.11 — Nonuniform Grids & Subgrids              ║")
    print("║  Examples: Graded Mesh | Subgrid Cavity | Curvilinear Map  ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()

    example_1_nonuniform_mesh()
    example_2_subgrid_cavity()
    example_3_curvilinear_mapping()

    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  Chapter 11 Examples — All Complete ✓                     ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()
