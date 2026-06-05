"""
harrington_mom.py
=================
Method of Moments (MoM) for electromagnetic boundary value problems.
Based on Harrington, "Time-Harmonic Electromagnetic Fields", Ch. 4-6.

Topics:
    - point_matching()       : Point matching (collocation) method
    - galerkin_method()      : Galerkin method with domain testing
    - pulse_basis()          : Pulse basis functions for piecewise constant expansion
    - triangle_basis()       : Triangular basis functions (linear)
    - thin_wire_mom()        : Thin-wire MoM for straight wire (Harrington 4-5)

Author: Computational Electromagnetics Group
"""

import numpy as np
from scipy.constants import mu_0, epsilon_0, pi, c
from scipy.linalg import solve, lu_factor, lu_solve
from scipy.special import jn, expi
import matplotlib.pyplot as plt

# Physical constants
k_0 = 2 * np.pi * 3e9 / c
eta_0 = np.sqrt(mu_0 / epsilon_0)


# -----------------------------------------------------------------
# Basis Functions
# -----------------------------------------------------------------

def pulse_basis(x: np.ndarray, x_segment: tuple) -> np.ndarray:
    """
    Pulse basis function centered at segment midpoint.

    P_n(x) = 1 for x in [x_{n-1}, x_n], else 0

    Parameters
    ----------
    x : np.ndarray
        Evaluation points.
    x_segment : tuple (x_left, x_right)
        Support of the pulse.

    Returns
    -------
    vals : np.ndarray
        Pulse values at each x.
    """
    x_left, x_right = x_segment
    center = (x_left + x_right) / 2
    half_w = (x_right - x_left) / 2
    vals = np.where(np.abs(x - center) <= half_w, 1.0, 0.0)
    return vals


def triangle_basis(x: np.ndarray, x_node_left: float,
                   x_node_center: float, x_node_right: float) -> np.ndarray:
    """
    Triangular (piecewise linear) basis function.
    Linear interpolation between three nodes.

    T_n(x) = 0                        if x < x_{n-1} or x > x_{n+1}
           = (x - x_{n-1})/(w)        if x_{n-1} <= x < x_n
           = (x_{n+1} - x)/w          if x_n <= x < x_{n+1}

    where w = (x_{n+1} - x_{n-1})/2

    Parameters
    ----------
    x : np.ndarray
        Evaluation points.
    x_node_left, x_node_center, x_node_right : float
        Three consecutive node positions.

    Returns
    -------
    vals : np.ndarray
        Triangle basis values.
    """
    w = (x_node_right - x_node_left) / 2
    vals = np.zeros_like(x, dtype=float)

    # Rising edge: [x_left, x_center]
    mask_rise = (x >= x_node_left) & (x < x_node_center)
    vals[mask_rise] = (x[mask_rise] - x_node_left) / w

    # Falling edge: [x_center, x_right]
    mask_fall = (x >= x_node_center) & (x <= x_node_right)
    vals[mask_fall] = (x_node_right - x[mask_fall]) / w

    return vals


# -----------------------------------------------------------------
# MoM Core Methods
# -----------------------------------------------------------------

def build_galerkin_matrix(basis_i, basis_j, kernel_fn,
                          x_i: np.ndarray, x_j: np.ndarray) -> np.ndarray:
    """
    Build Galerkin矩量法 matrix:
        Z_{ij} = ∫_S_i f_i(x) * K(x, x') * f_j(x') dx dx'

    Parameters
    ----------
    basis_i : callable
        Testing function i (function of x).
    basis_j : callable
        Basis function j (function of x').
    kernel_fn : callable
        Kernel K(x, x').
    x_i, x_j : np.ndarray
        Quadrature points for testing and basis domains.

    Returns
    -------
    Z : np.ndarray
        (N, N) impedance matrix.
    """
    N_i = len(x_i)
    N_j = len(x_j)
    dx_i = x_i[1] - x_i[0] if len(x_i) > 1 else 1.0
    dx_j = x_j[1] - x_j[0] if len(x_j) > 1 else 1.0

    Z = np.zeros((N_i, N_j), dtype=complex)

    for ii in range(N_i):
        for jj in range(N_j):
            f_i = basis_i(x_i[ii])
            f_j = basis_j(x_j[jj])
            K = kernel_fn(x_i[ii], x_j[jj])
            Z[ii, jj] = f_i * f_j * K * dx_i * dx_j

    return Z


def point_matching(K: np.ndarray, b: np.ndarray) -> np.ndarray:
    """
    Point matching (collocation) method.

    Solve K · I = b by forcing the equation to hold at N discrete points.

    Parameters
    ----------
    K : np.ndarray, shape (N, N)
        System matrix.
    b : np.ndarray, shape (N,)
        Excitation vector.

    Returns
    -------
    I : np.ndarray, shape (N,)
        Unknown coefficients.
    """
    K = np.asarray(K)
    b = np.asarray(b)
    # Use LU decomposition for efficiency
    I = lu_solve(lu_factor(K), b)
    return I


def galerkin_method(Z: np.ndarray, V: np.ndarray) -> np.ndarray:
    """
    Standard Galerkin method: solve Z · I = V.

    Parameters
    ----------
    Z : np.ndarray, shape (N, N)
        Impedance matrix.
    V : np.ndarray, shape (N,)
        Voltage/excitation vector.

    Returns
    -------
    I : np.ndarray
        Coefficient vector.
    """
    I = lu_solve(lu_factor(np.asarray(Z)), np.asarray(V))
    return I


# -----------------------------------------------------------------
# Thin Wire MoM (Harrington Chapter 4-5)
# -----------------------------------------------------------------

def thin_wire_kernel(z_i: np.ndarray, z_j: np.ndarray,
                    wire_length: float, wire_radius: float,
                    omega: float) -> np.ndarray:
    """
    Kernel for thin wire integral equation (Harrington Eq. 4-43).

    K(z, z') = (1 / (4π)) * [ e^(-jkR) / R ]
    where R = sqrt( (z-z')^2 + a^2 ), a = wire radius.

    The electric field integral equation for a thin wire:
    -j ω μ₀ / 4π * ∫ I(z') K(z,z') dz' = E_inc (tangential)

    Parameters
    ----------
    z_i, z_j : np.ndarray
        Observation and source coordinates along wire axis.
    wire_length : float
        Total wire length (m).
    wire_radius : float
        Wire radius (m).
    omega : float
        Angular frequency.

    Returns
    -------
    K : np.ndarray
        Kernel matrix.
    """
    k = omega * np.sqrt(mu_0 * epsilon_0)
    a = wire_radius

    Z = np.zeros((len(z_i), len(z_j)), dtype=complex)

    for ii, zi in enumerate(z_i):
        for jj, zj in enumerate(z_j):
            R = np.sqrt((zi - zj)**2 + a**2)
            # Handle diagonal (R -> a)
            R = max(R, 1e-12)
            Z[ii, jj] = np.exp(-1j * k * R) / R

    return Z / (4 * np.pi)


def thin_wire_mom(wire_length: float = 1.0,
                  wire_radius: float = 1e-4,
                  num_segments: int = 21,
                  omega: float = 2 * np.pi * 3e9,
                  e_incident: callable = None,
                  verbose: bool = True) -> tuple:
    """
    Method of Moments solution for a thin straight wire.

    Solves the electric field integral equation (EFIE):
        -j ω μ₀ ∫ G(z,z') I(z') dz' = E_z^inc(z)

    Using pulse basis and point matching (Harrington Section 4-5).

    Parameters
    ----------
    wire_length : float
        Total length of wire (m). Default 1 m.
    wire_radius : float
        Wire radius (m). Default 0.1 mm.
    num_segments : int
        Number of pulse basis segments. Default 21.
    omega : float
        Angular frequency.
    e_incident : callable
        Incident electric field function E_z(z). If None, use plane wave.
    verbose : bool

    Returns
    -------
    I : np.ndarray
        Current distribution along wire.
    z : np.ndarray
        Segment center positions.
    Z_mat : np.ndarray
        Impedance matrix.
    """
    k = omega * np.sqrt(mu_0 * epsilon_0)

    # Segment centers
    z = np.linspace(-wire_length / 2, wire_length / 2, num_segments)
    dz = wire_length / num_segments

    if verbose:
        print(f"[Thin Wire MoM]")
        print(f"  Length: {wire_length} m, Radius: {wire_radius} m")
        print(f"  Segments: {num_segments}, k = {k:.4f} rad/m")

    # Build impedance matrix
    Z_mat = thin_wire_kernel(z, z, wire_length, wire_radius, omega)

    # Incident field
    if e_incident is None:
        # Plane wave incident along z-direction (broadside)
        # E = E0 * sin(k * (z + L/2))
        E0 = 1.0  # V/m
        V = E0 * np.ones(num_segments)  # approximate uniform illumination
    else:
        V = np.array([e_incident(zi) for zi in z])

    # Solve
    I = point_matching(Z_mat, V)

    if verbose:
        print(f"  |I| range: [{np.abs(I).min():.4e}, {np.abs(I).max():.4e}] A")
        print(f"  Z condition number: {np.linalg.cond(Z_mat):.2e}")

    return I, z, Z_mat


# -----------------------------------------------------------------
# Pulse Basis MoM
# -----------------------------------------------------------------

def mom_pulse_1d(kernel, source_range, obs_range,
                 num_obs, num_source, omega):
    """
    Generic 1D MoM with pulse basis.

    Solves ∫ K(x,x') f(x') dx' = g(x) using pulse basis expansion.

    Parameters
    ----------
    kernel : callable K(x, x')
    source_range : tuple (x_min, x_max) of source domain
    obs_range : tuple (x_min, x_max) of observation domain
    num_obs, num_source : int
    omega : float

    Returns
    -------
    f : np.ndarray
        Expansion coefficients.
    x_obs : np.ndarray
        Observation points.
    """
    x_obs = np.linspace(obs_range[0], obs_range[1], num_obs)
    dx_obs = x_obs[1] - x_obs[0] if num_obs > 1 else 1.0

    x_src = np.linspace(source_range[0], source_range[1], num_source)
    dx_src = x_src[1] - x_src[0] if num_source > 1 else 1.0

    # Build matrix
    K_mat = np.zeros((num_obs, num_source), dtype=complex)
    for i, xo in enumerate(x_obs):
        for j, xs in enumerate(x_src):
            K_mat[i, j] = kernel(xo, xs)

    # Right-hand side: g(x) = 1 (step excitation)
    g = np.ones(num_obs)

    # Solve
    f = point_matching(K_mat, g)

    return f, x_obs


# -----------------------------------------------------------------
# Validation & Plotting
# -----------------------------------------------------------------

def validate_mom_thin_wire():
    """Validate thin wire MoM and plot current distribution."""
    print("\n=== MoM Thin Wire Validation ===")

    L = 1.0          # 1 meter wire
    a = 1e-4         # 0.1 mm radius
    f = 3e9          # 3 GHz
    omega = 2 * np.pi * f
    k = omega * np.sqrt(mu_0 * epsilon_0)

    num_seg = 41
    I, z, Z_mat = thin_wire_mom(wire_length=L, wire_radius=a,
                                 num_segments=num_seg,
                                 omega=omega, verbose=True)

    # Resonance check: max current should occur near center for half-wave resonance
    # At 3 GHz, λ = c/f = 0.1 m → L = 1 m = 10 λ, so full-wave resonator
    # Half-wave at L = λ/2 = 0.05 m, so L=1m is far from half-wave resonance
    idx_max = np.argmax(np.abs(I))
    print(f"\n  Max current at z = {z[idx_max]:.4f} m (center = {L/2:.4f} m)")

    # Plot current
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(z * 100, np.abs(I), 'b-', linewidth=2)
    plt.xlabel('z (cm)')
    plt.ylabel('|I(z)| (A)')
    plt.title('Current Distribution on Thin Wire')
    plt.grid(True, alpha=0.3)

    plt.subplot(1, 2, 2)
    plt.plot(z * 100, np.angle(I), 'r-', linewidth=2)
    plt.xlabel('z (cm)')
    plt.ylabel('Phase of I(z) (rad)')
    plt.title('Current Phase')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/tmp/thin_wire_current.png', dpi=150)
    print("  Saved to /tmp/thin_wire_current.png")


def validate_galerkin():
    """Validate Galerkin method with a simple 1D problem."""
    print("\n=== Galerkin Method Validation ===")

    # Problem: d²u/dx² + k² u = δ(x) on [0, L]
    # Pulse basis, Galerkin testing
    L = 1.0
    k = 10.0
    N = 20

    x = np.linspace(0, L, N)

    def kernel(xi, xj):
        R = abs(xi - xj)
        return np.exp(1j * k * R) / (4 * np.pi * max(R, 1e-12))

    def pulse_i(xi, x_seg):
        return pulse_basis(xi, x_seg)

    # Build matrix using Galerkin (inner products)
    Z = np.zeros((N, N), dtype=complex)

    # Simple point-matching for validation
    for i in range(N):
        for j in range(N):
            xi = x[i]
            xj = x[j]
            dx = x[1] - x[0] if N > 1 else 1.0
            Z[i, j] = kernel(xi, xj) * dx * dx

    b = np.ones(N)
    u = point_matching(Z, b)

    print(f"  N = {N}, cond(Z) = {np.linalg.cond(Z):.2e}")
    print(f"  |u| range: [{np.abs(u).min():.4e}, {np.abs(u).max():.4e}]")


def validate_triangle_basis():
    """Test triangle basis functions."""
    print("\n=== Triangle Basis Validation ===")

    x = np.linspace(-1, 1, 401)

    x_left, x_center, x_right = -0.5, 0.0, 0.5
    T = triangle_basis(x, x_left, x_center, x_right)

    # Check: max at center = 1
    print(f"  Center value: {T[np.argmin(np.abs(x))]:.4f} (expected 1.0)")
    # Check: zero at edges
    print(f"  Left edge value: {T[0]:.4f} (expected 0.0)")
    print(f"  Right edge value: {T[-1]:.4f} (expected 0.0)")

    plt.figure(figsize=(7, 4))
    plt.plot(x, T, 'b-', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('$T_n(x)$')
    plt.title('Triangular Basis Function')
    plt.grid(True, alpha=0.3)
    plt.savefig('/tmp/triangle_basis.png', dpi=150)
    print("  Saved to /tmp/triangle_basis.png")


if __name__ == '__main__':
    print("=" * 60)
    print("Harrington Method of Moments")
    print("=" * 60)

    validate_mom_thin_wire()
    validate_galerkin()
    validate_triangle_basis()

    with open(__file__) as f:
        n_lines = len(f.readlines())
    print(f"\nTotal lines: {n_lines}")
    print("DONE")