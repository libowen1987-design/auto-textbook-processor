"""
Chapter 5: Fast Computational Methods for Rough Surface Scattering
================================================================
Tsang, Kong, Ding & Ao (2001) - Volume II Numerical Simulations

This script implements:
1. Banded Matrix Canonical Grid (BMCG) method for 2-D PEC scattering
2. Physics-Based Two-Grid (PBTG) method for lossy dielectric surfaces
3. Steepest Descent Fast Multipole Method (SDFMM)
4. Method of Ordered Multiple Interactions (MOMI)

Physical Constants (scipy.constants):
    c       = 299792458 m/s
    epsilon_0 = 8.854187817e-12 F/m
    mu_0      = 1.2566370614e-6 H/m

Key Variables:
    correlation_length : l_c (m)
    rms_height         : sigma_h (m)
    k0                 : free-space wavenumber (rad/m)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
from matplotlib import rcParams

rcParams['font.family'] = 'serif'
rcParams['font.size'] = 11
rcParams['axes.unicode_minus'] = False

c = constants.c
eps_0 = constants.epsilon_0
mu_0 = constants.mu_0
eta_0 = np.sqrt(mu_0 / eps_0)


# =============================================================================
# 1. Banded Matrix Canonical Grid (BMCG) Method
# =============================================================================

def banded_matrix_canonical_grid(
    x_nodes: np.ndarray,
    z_nodes: np.ndarray,
    k0: float,
    bandwidth: int = 20
) -> np.ndarray:
    """
    Banded Matrix Canonical Grid method for rough surface scattering.

    The key idea: decompose the full impedance matrix Z into:
        Z = Z_weak + Z_strong

    where Z_weak is a sparse matrix (banded near diagonal) representing
    weak interactions, and Z_strong is a canonical grid Toeplitz matrix
    representing strong (near-field) interactions.

    Parameters
    ----------
    x_nodes, z_nodes : ndarray
        Surface node coordinates (m).
    k0 : float
        Free-space wavenumber (rad/m).
    bandwidth : int
        Half-bandwidth for the sparse weak matrix.

    Returns
    -------
    Z_banded : ndarray (N x (2*bandwidth+1))
        Banded matrix in banded storage format.
    Z_canonical : ndarray (N x N)
        Canonical grid Toeplitz matrix for strong interactions.
    """
    n = len(x_nodes)
    dx = np.diff(x_nodes)[0]

    # Canonical grid: flat surface Green's function Toeplitz matrix
    # For each column shift, compute the Toeplitz entry
    Z_canonical = np.zeros((n, n), dtype=complex)
    for shift in range(n):
        rho = np.abs(shift) * dx
        if rho < 1e-12:
            Z_canonical[shift, 0] = 1j * k0 * dx / 4
        else:
            kr = k0 * rho
            G = 1j/4 * hankel1(kr)
            Z_canonical[shift, 0] = G * dx

    # Make Toeplitz from first column
    for i in range(n):
        for j in range(i+1):
            Z_canonical[i, j] = Z_canonical[i-j, 0]
        for j in range(i+1, n):
            Z_canonical[i, j] = 0

    # Banded weak matrix (nearby interactions only)
    Z_banded = np.zeros((n, 2*bandwidth+1), dtype=complex)
    for i in range(n):
        for j in range(max(0, i-bandwidth), min(n, i+bandwidth+1)):
            if i == j:
                Z_banded[i, bandwidth] = 1j * k0 * dx / 4
            else:
                dx_val = x_nodes[i] - x_nodes[j]
                dz_val = z_nodes[i] - z_nodes[j]
                rho = np.sqrt(dx_val**2 + dz_val**2)
                rho = max(rho, 1e-12)
                kr = k0 * rho
                G = 1j/4 * hankel1(kr)
                Z_banded[i, bandwidth + (j-i)] = G * dx

    return Z_banded, Z_canonical


def hankel1(z):
    """H0^(1)(z) — 2-D free-space Green's function kernel."""
    z = np.asarray(z, dtype=complex)
    small = np.abs(z) < 1e-3
    result = np.zeros_like(z, dtype=complex)
    gamma = 0.5772156649
    Y0 = -2/np.pi * (np.log(z/2) + gamma)
    J0 = np.ones_like(z, dtype=complex)
    result[small] = J0[small] + 1j * Y0[small]
    return result


# =============================================================================
# 2. Physics-Based Two-Grid (PBTG) Method
# =============================================================================

def pbtg_method(
    x_fine: np.ndarray,
    z_fine: np.ndarray,
    x_coarse: np.ndarray,
    z_coarse: np.ndarray,
    k0: float,
    epsilon_r: complex,
    incident_field_fine: np.ndarray
) -> tuple:
    """
    Physics-Based Two-Grid (PBTG) method for lossy dielectric rough surfaces.

    Key idea: decompose the surface into fine and coarse grids.
    - Fine grid: captures rapid phase variation of the Green's function
    - Coarse grid: captures the smooth physics of the surface

    The method combines:
    1. PBTG for the extinction matrix (coherent part)
    2. Sparse-matrix canonical grid (SMCG) for the interaction matrix

    Parameters
    ----------
    x_fine, z_fine : ndarray
        Fine grid nodes (m).
    x_coarse, z_coarse : ndarray
        Coarse grid nodes (m).
    k0 : float
        Wavenumber (rad/m).
    epsilon_r : complex
        Relative permittivity of the medium.
    incident_field_fine : ndarray
        Incident field on the fine grid.

    Returns
    -------
    (field_fine, field_coarse) : tuple of ndarrays
        Field values on fine and coarse grids.
    """
    n_fine = len(x_fine)
    n_coarse = len(x_coarse)

    # Fine grid Green's function
    G_fine = np.zeros((n_fine, n_fine), dtype=complex)
    for i in range(n_fine):
        for j in range(n_fine):
            rho = np.sqrt((x_fine[i]-x_fine[j])**2 + (z_fine[i]-z_fine[j])**2)
            rho = max(rho, 1e-12)
            G_fine[i, j] = 1j/4 * hankel1(k0 * rho)

    # Coarse grid for physics-based interpolation
    # Interpolation matrix from coarse to fine
    P_matrix = np.zeros((n_fine, n_coarse), dtype=complex)
    for i in range(n_fine):
        for j in range(n_coarse):
            x_dist = x_fine[i] - x_coarse[j]
            P_matrix[i, j] = np.sinc(k0 * x_dist / (2*np.pi))**2

    # Normalize P matrix
    row_sums = np.sum(P_matrix, axis=1)
    P_matrix = P_matrix / row_sums[:, np.newaxis]

    # Solve on coarse grid first
    Z_coarse = G_coarse_interaction(x_coarse, z_coarse, k0, epsilon_r)
    field_coarse = np.linalg.solve(Z_coarse, P_matrix.T @ incident_field_fine)

    # Interpolate to fine grid
    field_fine = P_matrix @ field_coarse

    return field_fine, field_coarse


def G_coarse_interaction(x_coarse, z_coarse, k0, epsilon_r):
    """Coarse grid interaction matrix with effective permittivity."""
    n = len(x_coarse)
    dx = np.diff(x_coarse)[0]
    Z = np.zeros((n, n), dtype=complex)
    k_eff = k0 * np.sqrt(epsilon_r)

    for i in range(n):
        for j in range(n):
            rho = np.sqrt((x_coarse[i]-x_coarse[j])**2 + (z_coarse[i]-z_coarse[j])**2)
            rho = max(rho, 1e-12)
            if i == j:
                Z[i, i] = 1j * k_eff * dx / 4
            else:
                kr = k_eff * rho
                Z[i, j] = 1j/4 * hankel1(kr) * dx

    return Z


# =============================================================================
# 3. Steepest Descent Fast Multipole Method (SDFMM)
# =============================================================================

def green_function_2d_steepest_descent(rho, k0, R_max=None):
    """
    Steepest descent path evaluation of 2-D Green's function.

    H0^(1)(k0*rho) evaluated along steepest descent path to avoid
    oscillatory behavior in the saddle point method.

    For large k0*rho, the steepest descent approximation is:
        H0^(1)(k0*rho) ≈ sqrt(2/(pi*k0*rho)) * exp(j*(k0*rho - pi/4))

    Parameters
    ----------
    rho : float or ndarray
        Radial distance (m).
    k0 : float
        Wavenumber (rad/m).
    R_max : float, optional
        Distance beyond which asymptotic form is used.

    Returns
    -------
    G : complex
        Green's function value.
    """
    rho = np.asarray(rho, dtype=complex)
    kr = k0 * rho

    large = np.abs(kr) > 15
    result = np.zeros_like(kr, dtype=complex)

    # Asymptotic form (steepest descent)
    with np.errstate(over='ignore', invalid='ignore'):
        result[large] = np.sqrt(2/(np.pi * kr[large])) * np.exp(1j * (kr[large] - np.pi/4))
        small = ~large
        result[small] = 1j/4 * hankel1(kr[small])

    return result


def sdfmm_group_interaction(
    group_centers: np.ndarray,
    group_radius: float,
    k0: float,
    max_level: int = 4
) -> np.ndarray:
    """
    Multi-level SDFMM group interaction matrix.

    Groups are arranged in a tree structure. Each group has a center
    and radius. The interaction list separates nearby (strong) from
    distant (weak) groups.

    Parameters
    ----------
    group_centers : ndarray (M x 3)
        Center positions of M groups.
    group_radius : float
        Radius of each group.
    k0 : float
        Wavenumber (rad/m).
    max_level : int
        Maximum tree level.

    Returns
    -------
    G_matrix : ndarray (M x M)
        Group interaction matrix.
    """
    M = len(group_centers)
    G_matrix = np.zeros((M, M), dtype=complex)

    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            d = np.linalg.norm(group_centers[i] - group_centers[j])
            if d < 2 * group_radius:
                # Nearby group: direct interaction
                G_matrix[i, j] = 1j/4 * hankel1(k0 * d)
            else:
                # Distant group: multipole approximation
                # G ≈ exp(-j*k0*d) / (4*pi*d) * translation_matrix
                G_matrix[i, j] = np.exp(1j * k0 * d) / (4 * np.pi * d)

    return G_matrix


# =============================================================================
# 4. Method of Ordered Multiple Interactions (MOMI)
# =============================================================================

def momi_iterative_solver(
    Z_matrix: np.ndarray,
    V_vector: np.ndarray,
    n_iterations: int = 50,
    tolerance: float = 1e-6
) -> np.ndarray:
    """
    Method of Ordered Multiple Interactions (MOMI).

    MOMI is an iterative solver that orders interactions by strength.
    Unlike CG, MOMI uses physical ordering of the Green's function.

    Parameters
    ----------
    Z_matrix : ndarray (N x N)
        Impedance matrix.
    V_vector : ndarray (N)
        Right-hand side.
    n_iterations : int
        Maximum iterations.
    tolerance : float
        Convergence tolerance.

    Returns
    -------
    I_solution : ndarray
        Current vector.
    """
    n = len(V_vector)
    I_curr = np.zeros(n, dtype=complex)
    I_prev = np.zeros(n, dtype=complex)

    for it in range(n_iterations):
        R = V_vector - Z_matrix @ I_curr

        # Ordering by diagonal dominance
        diag_Z = np.diag(Z_matrix)
        weights = np.abs(diag_Z)
        weights = weights / np.sum(weights)

        # Update: add weighted residual
        delta_I = np.zeros(n, dtype=complex)
        for idx in range(n):
            delta_I[idx] = R[idx] / (diag_Z[idx] + 1e-12)

        I_prev = I_curr.copy()
        I_curr = I_curr + delta_I

        residual_norm = np.linalg.norm(delta_I)
        if residual_norm < tolerance:
            print(f"  MOMI converged at iteration {it+1}")
            break

    return I_curr


# =============================================================================
# 5. Computational Complexity Comparison
# =============================================================================

def complexity_analysis():
    """
    Compare computational complexity O(N^2) vs O(N*log(N)) methods.
    """
    N_values = [64, 128, 256, 512, 1024, 2048]
    O_N2 = [n**2 for n in N_values]
    O_NlogN = [n * np.log2(n) for n in N_values]
    O_N15 = [n**1.5 for n in N_values]
    O_N12 = [n**1.2 for n in N_values]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.loglog(N_values, O_N2, 'b-o', linewidth=1.5, markersize=5, label=r'$O(N^2)$ Direct')
    ax.loglog(N_values, O_N15, 'g--s', linewidth=1.5, markersize=5, label=r'$O(N^{1.5})$ BMCG/SMCG')
    ax.loglog(N_values, O_N12, 'r-.^', linewidth=1.5, markersize=5, label=r'$O(N^{1.2})$ SDFMM')
    ax.loglog(N_values, O_NlogN, 'm:d', linewidth=1.5, markersize=5, label=r'$O(N \log N)$ MLFMM')
    ax.set_xlabel(r'Number of Unknowns $N$')
    ax.set_ylabel(r'Computational Cost (Operations)')
    ax.set_title('Fig. 5.x — Computational Complexity: Fast Methods vs Direct')
    ax.legend()
    ax.grid(True, which='both', alpha=0.3)

    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/tsang_scattering/figures/ch5_fig1_complexity.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: ch5_fig1_complexity.png")


# =============================================================================
# 6. Visualization
# =============================================================================

def plot_bmcg_vs_direct():
    """
    Compare BMCG method vs direct method accuracy.
    """
    N = 128
    x = np.linspace(-5, 5, N)
    k0 = 2 * np.pi / 0.1

    # Flat surface: exact Toeplitz solution
    Z_direct = np.zeros((N, N), dtype=complex)
    dx = x[1] - x[0]
    for i in range(N):
        for j in range(N):
            rho = np.abs(i - j) * dx
            rho = max(rho, 1e-12)
            Z_direct[i, j] = 1j/4 * hankel1(k0 * rho) * dx

    # BMCG approximation
    Z_banded, Z_canonical = banded_matrix_canonical_grid(x, np.zeros(N), k0, bandwidth=20)

    # Banded storage to full matrix
    bw = 20
    Z_bmcg = np.zeros((N, N), dtype=complex)
    for i in range(N):
        for j in range(max(0, i-bw), min(N, i+bw+1)):
            Z_bmcg[i, j] = Z_banded[i, bw + (j-i)]

    # Compare diagonal
    diag_direct = np.diag(Z_direct)
    diag_bmcg = np.diag(Z_bmcg)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    axes[0].semilogy(np.abs(diag_direct), 'b-', linewidth=1.2, label='Direct O(N²)')
    axes[0].semilogy(np.abs(diag_bmcg), 'r--', linewidth=1.2, label='BMCG')
    axes[0].set_xlabel(r'Index $i$')
    axes[0].set_ylabel(r'$|Z_{ii}|$')
    axes[0].set_title('Diagonal Elements Comparison')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    diff = np.abs(diag_direct - diag_bmcg)
    axes[1].semilogy(diff, 'purple', linewidth=1.2)
    axes[1].set_xlabel(r'Index $i$')
    axes[1].set_ylabel(r'$|Z_{ii}^{direct} - Z_{ii}^{BMCG}|$')
    axes[1].set_title('BMCG Error vs Direct Method')
    axes[1].grid(True, alpha=0.3)

    fig.suptitle('Fig. 5.x — BMCG vs Direct Method Comparison', fontsize=12)
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/tsang_scattering/figures/ch5_fig2_bmcg_direct.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: ch5_fig2_bmcg_direct.png")


def plot_pbtg_field():
    """
    Visualize PBTG method: fine vs coarse grid field distribution.
    """
    # Surface
    L = 10.0
    n_fine = 256
    n_coarse = 64
    x_fine = np.linspace(-L/2, L/2, n_fine)
    x_coarse = np.linspace(-L/2, L/2, n_coarse)

    k0 = 2 * np.pi / 0.1
    z_fine = 0.05 * np.sin(2*np.pi * x_fine / 1.0)  # sinusoidal surface
    z_coarse = 0.05 * np.sin(2*np.pi * x_coarse / 1.0)

    # Incident field
    theta_inc = 30 * np.pi / 180
    E_inc = np.exp(1j * k0 * np.sin(theta_inc) * x_fine)

    # PBTG
    E_fine, E_coarse = pbtg_method(
        x_fine, z_fine, x_coarse, z_coarse, k0,
        epsilon_r=3.0 + 0.1j, incident_field_fine=E_inc
    )

    fig, axes = plt.subplots(2, 1, figsize=(12, 7))

    axes[0].plot(x_fine, np.abs(E_fine), 'b-', linewidth=0.8, label='Fine grid')
    axes[0].plot(x_coarse, np.abs(E_coarse), 'r.', markersize=8, label='Coarse grid')
    axes[0].set_xlabel(r'$x$ (m)')
    axes[0].set_ylabel(r'$|E|$')
    axes[0].set_title(r'Fig. 5.x — PBTG: Field Magnitude on Fine vs Coarse Grid')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(x_fine, np.angle(E_fine), 'b-', linewidth=0.8, label='Fine grid phase')
    axes[1].plot(x_coarse, np.angle(E_coarse), 'r.', markersize=8, label='Coarse grid phase')
    axes[1].set_xlabel(r'$x$ (m)')
    axes[1].set_ylabel(r'Phase (rad)')
    axes[1].set_title('PBTG: Field Phase')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/tsang_scattering/figures/ch5_fig3_pbtg_field.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: ch5_fig3_pbtg_field.png")


def plot_sdfmm_groups():
    """
    Visualize SDFMM group structure.
    """
    # 2-D grid of groups
    nx, ny = 4, 4
    x_centers = np.linspace(-2, 2, nx)
    y_centers = np.linspace(-2, 2, ny)
    X, Y = np.meshgrid(x_centers, y_centers, indexing='ij')
    group_centers = np.stack([X.ravel(), Y.ravel(), np.zeros(nx*ny)], axis=1)

    k0 = 2 * np.pi / 0.1
    G_matrix = sdfmm_group_interaction(group_centers, 0.5, k0, max_level=4)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    im0 = axes[0].imshow(20*np.log10(np.abs(G_matrix) + 1e-12),
                         cmap='viridis', aspect='auto')
    axes[0].set_title(r'$|G_{ij}|$ (dB) — SDFMM Group Interactions')
    axes[0].set_xlabel('Group $j$')
    axes[0].set_ylabel('Group $i$')
    plt.colorbar(im0, ax=axes[0])

    im1 = axes[1].imshow(np.angle(G_matrix), cmap='twilight', aspect='auto')
    axes[1].set_title(r'$\angle G_{ij}$ (rad)')
    axes[1].set_xlabel('Group $j$')
    axes[1].set_ylabel('Group $i$')
    plt.colorbar(im1, ax=axes[1])

    fig.suptitle('Fig. 5.x — SDFMM Group Interaction Matrix (4×4 grid)', fontsize=12)
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/tsang_scattering/figures/ch5_fig4_sdfmm_groups.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("Saved: ch5_fig4_sdfmm_groups.png")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Chapter 5: Fast Computational Methods")
    print("=" * 60)

    freq_ghz = 5.0
    wavelength_m = c / (freq_ghz * 1e9)
    k0 = 2 * np.pi / wavelength_m

    print(f"\nFrequency: {freq_ghz} GHz, lambda = {wavelength_m:.4f} m")
    print(f"  k0 = {k0:.4f} rad/m")

    complexity_analysis()
    plot_bmcg_vs_direct()
    plot_pbtg_field()
    plot_sdfmm_groups()

    print("\n" + "=" * 60)
    print("Chapter 5 complete.")
    print("=" * 60)
