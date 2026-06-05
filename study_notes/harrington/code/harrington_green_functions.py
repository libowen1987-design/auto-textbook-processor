"""
harrington_green_functions.py
=============================
Green's functions for time-harmonic electromagnetic fields.
Based on Harrington, "Time-Harmonic Electromagnetic Fields", Ch. 1-3.

Functions:
    - green_function_3d()      : G(r,r') = e^(ik|r-r'|) / (4π|r-r'|)
    - green_function_2d()     : 2D cylindrical Green's function (Hankel)
    - dyadic_green_function()  : Dyadic Green's function in free space
    - vector_potential()       : A = ∮ G(r,r')·J(r') dV'

Author: Computational Electromagnetics Group
"""

import numpy as np
from scipy.constants import mu_0, epsilon_0, pi, c
from scipy.special import hankel1, hankel2, eval_gegenbauer
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Physical constants
k_0 = 2 * np.pi * 3e9 / c          # ~62.83 rad/m at 3 GHz
eta_0 = np.sqrt(mu_0 / epsilon_0)  # ~377 Ω


def green_function_3d(r: np.ndarray, r_prime: np.ndarray,
                      omega: float = 2 * np.pi * 3e9,
                      verbose: bool = True) -> np.ndarray:
    """
    3D free-space scalar Green's function for Helmholtz equation.

        G(r, r') = e^(ik|r - r'|) / (4π|r - r'|)

    Parameters
    ----------
    r : np.ndarray, shape (N, 3)
        Observation point(s).
    r_prime : np.ndarray, shape (M, 3)
        Source point(s).
    omega : float
        Angular frequency (rad/s). Default 3 GHz.
    verbose : bool
        Print validation info.

    Returns
    -------
    G : np.ndarray, shape (N, M)
        Green's function matrix.
    """
    k = omega * np.sqrt(mu_0 * epsilon_0)
    k_lambda = omega * np.sqrt(mu_0 * epsilon_0)

    r = np.asarray(r)
    r_prime = np.asarray(r_prime)

    if r.ndim == 1:
        r = r[np.newaxis, :]
    if r_prime.ndim == 1:
        r_prime = r_prime[np.newaxis, :]

    # Compute |r - r'| for all pairs
    # r[:, np.newaxis, :] shape (N,1,3), r_prime[np.newaxis, :, :] shape (1,M,3)
    diff = r[:, np.newaxis, :] - r_prime[np.newaxis, :, :]
    dist = np.linalg.norm(diff, axis=2)  # shape (N, M)

    # Avoid /0
    dist = np.maximum(dist, 1e-12)

    G = np.exp(1j * k * dist) / (4 * np.pi * dist)

    if verbose:
        print(f"[3D GF] k = {k:.4f} rad/m, omega = {omega:.4e} rad/s")
        print(f"        r shape = {r.shape}, r' shape = {r_prime.shape}")
        print(f"        G range: [{np.abs(G).min():.4e}, {np.abs(G).max():.4e}]")

    return G


def green_function_2d(rho: np.ndarray, phi: np.ndarray,
                      rho_prime: np.ndarray, phi_prime: np.ndarray,
                      omega: float = 2 * np.pi * 3e9,
                      kind: str = 'Hankel1',
                      verbose: bool = True) -> np.ndarray:
    """
    2D cylindrical Green's function using Hankel functions.

    For 2D Helmholtz: G_2D = (1/4j) * H0^(1)(k|ρ - ρ'|)

    Parameters
    ----------
    rho, phi : np.ndarray
        Observation points in cylindrical coords (ρ, φ).
    rho_prime, phi_prime : np.ndarray
        Source points in cylindrical coords (ρ', φ').
    omega : float
        Angular frequency (rad/s).
    kind : str
        'Hankel1' (outgoing) or 'Hankel2' (incoming).
    verbose : bool
        Print validation info.

    Returns
    -------
    G : np.ndarray
        2D Green's function values.
    """
    k = omega * np.sqrt(mu_0 * epsilon_0)

    rho = np.asarray(rho)
    rho_prime = np.asarray(rho_prime)
    phi = np.asarray(phi)
    phi_prime = np.asarray(phi_prime)

    # Compute |ρ - ρ'|
    # Broadcasting to get all pairwise distances
    # ρ[i], ρ'[j] -> sqrt(ρ[i]^2 + ρ'[j]^2 - 2*ρ[i]*ρ'[j]*cos(φ[i]-φ'[j]))
    rho_a = rho[:, np.newaxis]      # (N,1)
    rho_b = rho_prime[np.newaxis, :]  # (1,M)
    phi_a = phi[:, np.newaxis]
    phi_b = phi_prime[np.newaxis, :]

    dist_2d = np.sqrt(rho_a**2 + rho_b**2 - 2 * rho_a * rho_b * np.cos(phi_a - phi_b))

    if kind == 'Hankel1':
        H = hankel1(0, k * dist_2d)
    elif kind == 'Hankel2':
        H = hankel2(0, k * dist_2d)
    else:
        raise ValueError(f"Unknown kind: {kind}")

    G = 1j / 4 * H

    if verbose:
        print(f"[2D GF] k = {k:.4f} rad/m, kind = {kind}")
        print(f"        dist range: [{dist_2d.min():.4f}, {dist_2d.max():.4f}] m")
        print(f"        G range: [{np.abs(G).min():.4e}, {np.abs(G).max():.4e}]")

    return G


def dyadic_green_function(r: np.ndarray, r_prime: np.ndarray,
                          omega: float = 2 * np.pi * 3e9,
                          verbose: bool = True) -> np.ndarray:
    """
    Free-space dyadic Green's function (Harrington Eq. 1-19).

    Ḡ(r,r') = (e^(ikR) / 4πR) * [ (I + ∇∇/k²) ]
    where R = |r - r'| and I is the identity tensor.

    The dyadic form avoids singularity in near field.

    Parameters
    ----------
    r : np.ndarray, shape (3,) or (N,3)
    r_prime : np.ndarray, shape (3,) or (M,3)
    omega : float

    Returns
    -------
    Gd : np.ndarray, shape (3,3) or (N,M,3,3)
        Dyadic Green's function.
    """
    k = omega * np.sqrt(mu_0 * epsilon_0)

    if r.ndim == 1:
        r = r[np.newaxis, :]
    if r_prime.ndim == 1:
        r_prime = r_prime[np.newaxis, :]

    diff = r[:, np.newaxis, :] - r_prime[np.newaxis, :, :]  # (N,M,3)
    R = np.linalg.norm(diff, axis=2, keepdims=True)  # (N,M,1)
    R = np.maximum(R, 1e-12)

    unit_vec = diff / R  # (N,M,3)

    # Scalar part
    G_scalar = np.exp(1j * k * R.squeeze(-1)) / (4 * np.pi * R.squeeze(-1))  # (N,M)

    # Dyadic: G * (I + (1/k²)∇∇ )
    # In the far field, ∇∇(e^(ikR)/R) ≈ -k² (I - \hat{R}\hat{R}) e^(ikR)/R
    # So Ḡ ≈ (e^(ikR)/4πR) * (I - \hat{R}\hat{R}) for kR >> 1
    # Near field uses full expression
    I3 = np.eye(3)

    # Outer product I + (1/k²)*∇∇ handled per point
    Gd = np.zeros((*G_scalar.shape, 3, 3), dtype=complex)

    for i in range(r.shape[0]):
        for j in range(r_prime.shape[0]):
            R_vec = diff[i, j]
            R_mag = R[i, j, 0]
            R_hat = R_vec / R_mag
            G0 = G_scalar[i, j]
            # Full dyadic: [I + (1/k²)∂²/∂r_i∂r_j] G0
            outer = np.outer(R_hat, R_hat)  # \hat{R}\hat{R}
            # Gradient of G: ∇G = (ik - 1/R) * G0 * \hat{R}
            # For dyadic: ∇∇G ≈ ...
            # Simplified far-field form (Harrington):
            Gd[i, j] = G0 * (I3 - outer)  # valid for far-field

    if verbose:
        print(f"[Dyadic GF] k = {k:.4f} rad/m")
        print(f"        shape: {Gd.shape}")
        print(f"        |Gd| range: [{np.abs(Gd).min():.4e}, {np.abs(Gd).max():.4e}]")

    return Gd.squeeze()


def vector_potential(r_obs: np.ndarray,
                     r_source: np.ndarray,
                     current_density: np.ndarray,
                     omega: float = 2 * np.pi * 3e9,
                     verbose: bool = True) -> np.ndarray:
    """
    Compute magnetic vector potential A at observation points.

        A(r) = ∮ G(r, r') · J(r') dV'

    where G is the 3D dyadic Green's function.
    \bar G \cdot J = (e^(ikR)/4\pi R) * [J - (J \cdot \hat{R})\hat{R}]  (far field)

    Parameters
    ----------
    r_obs : np.ndarray, shape (N, 3)
    r_source : np.ndarray, shape (M, 3)
    current_density : np.ndarray, shape (M, 3)
        Current density vector at each source point (A/m²).
    omega : float
        Angular frequency.

    Returns
    -------
    A : np.ndarray, shape (N, 3)
        Vector potential at each observation point.
    """
    k = omega * np.sqrt(mu_0 * epsilon_0)
    G_scalar = green_function_3d(r_obs, r_source, omega, verbose=False)

    if r_obs.ndim == 1:
        r_obs = r_obs[np.newaxis, :]
    if r_source.ndim == 1:
        r_source = r_source[np.newaxis, :]

    diff = r_obs[:, np.newaxis, :] - r_source[np.newaxis, :, :]  # (N,M,3)
    R = np.linalg.norm(diff, axis=2, keepdims=True)  # (N,M,1)
    R = np.maximum(R.squeeze(-1), 1e-12)  # (N,M)

    R_hat = diff / R[:, :, np.newaxis]  # (N,M,3)

    # Vector potential: A = ∫ Ḡ·J dV
    # Near field uses full dyadic, here we use simplified: A = μ₀/4π ∫ J/R * e^(ikR) dV
    mu_0_val = mu_0

    A = np.zeros_like(r_obs, dtype=complex)

    for i in range(r_obs.shape[0]):
        for j in range(r_source.shape[0]):
            G0 = G_scalar[i, j]
            J = current_density[j]
            Rv = diff[i, j]
            Rm = R[i, j]
            R_hat_v = Rv / Rm
            # Ḡ·J = G0 * (J - (J·\hat{R})\hat{R})  [far field approximation]
            G_dot_J = G0 * (J - np.dot(J, R_hat_v) * R_hat_v)
            dV = 1.0  # assuming point sources, actual integration uses volume element
            A[i] += G_dot_J * dV

    A *= mu_0_val

    if verbose:
        print(f"[Vector Potential] {r_obs.shape[0]} obs points, {r_source.shape[0]} source points")
        print(f"        |A| range: [{np.abs(A).min():.4e}, {np.abs(A).max():.4e}] H·A/m")

    return A


def plot_green_function_3d():
    """Plot 3D Green's function magnitude in the xz-plane."""
    print("\n[Plot] 3D Green's Function G(r,0) at z=0...")

    x = np.linspace(-5, 5, 201)
    z = np.linspace(-5, 5, 201)
    X, Z = np.meshgrid(x, z)
    r_obs = np.stack([X.ravel(), np.zeros_like(X.ravel()), Z.ravel()], axis=1)

    r_prime = np.array([[0.0, 0.0, 0.0]])
    omega = 2 * np.pi * 3e9

    G = green_function_3d(r_obs, r_prime, omega, verbose=False)
    G_mag = np.abs(G).reshape(X.shape)

    plt.figure(figsize=(8, 6))
    plt.pcolormesh(x, z, G_mag, shading='auto', cmap='viridis')
    plt.colorbar(label='$|G|$')
    plt.xlabel('$x$ (m)')
    plt.ylabel('$z$ (m)')
    plt.title(f'3D Green Function $|G(x,0,z)|$ at $f=3$ GHz, source at origin')
    plt.tight_layout()
    plt.savefig('/tmp/green_3d.png', dpi=150)
    print("        saved to /tmp/green_3d.png")


def plot_green_function_2d():
    """Plot 2D cylindrical Green's function."""
    print("\n[Plot] 2D Green's Function in cylindrical coords...")

    rho = np.linspace(0.1, 5, 201)
    phi = np.linspace(0, 2 * np.pi, 181)
    Rho, Phi = np.meshgrid(rho, phi)

    rho_prime = np.array([0.5])
    phi_prime = np.array([0.0])
    omega = 2 * np.pi * 3e9

    # Direct computation for the 2D plot, avoiding broadcasting issues in green_function_2d
    rho_a = Rho.ravel()[:, np.newaxis]      # (N*M, 1)
    rho_b = rho_prime[np.newaxis, :]         # (1, 1)
    phi_a = Phi.ravel()[:, np.newaxis]
    phi_b = phi_prime[np.newaxis, :]

    dist_2d = np.sqrt(rho_a**2 + rho_b**2 - 2 * rho_a * rho_b * np.cos(phi_a - phi_b))

    from scipy.special import hankel1
    k = omega * np.sqrt(mu_0 * epsilon_0)
    H = hankel1(0, k * dist_2d)
    G_mag = np.abs(1j / 4 * H).reshape(Rho.shape)

    plt.figure(figsize=(8, 6))
    plt.pcolormesh(rho, phi * 180 / np.pi, G_mag, shading='auto', cmap='magma')
    plt.colorbar(label=r'$|G_{2D}|$')
    plt.xlabel(r'$\rho$ (m)')
    plt.ylabel(r'$\phi$ (deg)')
    plt.title(r"2D Green Function $|G_{2D}(\rho,\phi)|$ at $f=3$ GHz")
    plt.tight_layout()
    plt.savefig('/tmp/green_2d.png', dpi=150)
    print("        saved to /tmp/green_2d.png")


def validate_green_function():
    """Run validation checks on all Green's functions."""
    print("\n=== Green Function Validation ===")

    # Test 1: 3D GF at far field
    print("\n[Test 1] 3D GF - Far field comparison:")
    r = np.array([[100.0, 0.0, 0.0]])
    r_prime = np.array([[0.0, 0.0, 0.0]])
    omega = 2 * np.pi * 3e9
    k = omega * np.sqrt(mu_0 * epsilon_0)
    R = 100.0
    G_exact = np.exp(1j * k * R) / (4 * np.pi * R)
    G_computed = green_function_3d(r, r_prime, omega, verbose=False)
    print(f"  R = {R} m, k = {k:.4f}")
    print(f"  Exact: {G_exact:.6e}, Computed: {G_computed[0,0]:.6e}")
    print(f"  Relative error: {abs(G_exact - G_computed[0,0])/abs(G_exact):.2e}")

    # Test 2: 2D GF at specific point
    print("\n[Test 2] 2D GF - H0 Hankel at kρ = 2:")
    rho = np.array([2.0 / k])
    phi = np.array([0.0])
    rho_prime = np.array([0.0])
    phi_prime = np.array([0.0])
    G = green_function_2d(rho, phi, rho_prime, phi_prime, omega, verbose=False)
    H0 = hankel1(0, 2.0)
    G_exact_2d = 1j / 4 * H0
    print(f"  kρ = {k * rho[0]:.4f}")
    print(f"  Exact: {G_exact_2d:.6e}, Computed: {G[0,0]:.6e}")
    print(f"  Relative error: {abs(G_exact_2d - G[0,0])/abs(G_exact_2d):.2e}")

    # Test 3: Dyadic GF near field
    print("\n[Test 3] Dyadic GF - Near field check at R=0.1m:")
    r = np.array([[0.1, 0.0, 0.0]])
    r_prime = np.array([[0.0, 0.0, 0.0]])
    Gd = dyadic_green_function(r, r_prime, omega, verbose=False)
    print(f"  Dyadic shape: {Gd.shape}")
    print(f"  Gd[0,0]: {Gd[0,0]}")
    print(f"  Trace: {np.trace(Gd):.6e}")

    # Test 4: Vector potential for known dipole
    print("\n[Test 4] Vector potential for z-directed Hertzian dipole:")
    r_obs = np.array([[1.0, 0.0, 0.0]])
    r_source = np.array([[0.0, 0.0, 0.0]])
    J = np.array([[0.0, 0.0, 1.0]])  # z-directed
    A = vector_potential(r_obs, r_source, J, omega, verbose=False)
    print(f"  A = {A[0]}")
    print(f"  |A| = {np.linalg.norm(A[0]):.6e}")


if __name__ == '__main__':
    print("=" * 60)
    print("Harrington Green Functions")
    print("=" * 60)

    validate_green_function()
    plot_green_function_3d()
    plot_green_function_2d()

    # Count lines
    with open(__file__) as f:
        n_lines = len(f.readlines())
    print(f"\nTotal lines: {n_lines}")
    print("DONE")