#!/usr/bin/env python3
"""
Bondeson Ch4 Examples — Eigenvalues
Chapter 4: Eigenvalue problems, Von Neumann stability, Padé approximation
"""
import numpy as np
import scipy.constants as sc
from scipy.linalg import eigh
from scipy.sparse import diags
from scipy.sparse.linalg import eigs

c_0 = sc.speed_of_light
eps_0 = sc.epsilon_0
mu_0 = sc.mu_0

# === Example 1: 1D Helmholtz — Analytical vs FD Eigenvalues ===
print("=" * 60)
print("Example 1: 1D Helmholtz — Analytical vs FD Eigenvalues")
print("=" * 60)

def helmholtz_fd_eigenvalues(a, N):
    """
    Solve d²f/dx² = -k²f on [0,a] with f(0)=f(a)=0
    using finite differences. Returns sorted k values.
    """
    h = a / N
    # Tridiagonal matrix
    diag = -2.0 / h**2 * np.ones(N - 1)
    off = 1.0 / h**2 * np.ones(N - 2)
    A = diags([off, diag, off], [-1, 0, 1], format='csr')
    lambdas = eigs(A, k=min(6, N-1), which='SM', return_eigenvectors=False)
    k = np.sqrt(np.sort(-np.real(lambdas)))
    return k

a = np.pi  # analytical: k_m = mπ/a = 1, 2, 3, ...
for N in [10, 20, 40, 80]:
    k_num = helmholtz_fd_eigenvalues(a, N)
    print(f"N={N:3d}  h={np.pi/N:.5f}")
    for m in range(min(3, len(k_num))):
        err = abs(k_num[m] - (m+1)) / (m+1) * 100
        print(f"  k_{m+1} = {k_num[m]:.8f}  (exact {m+1:.1f})  err={err:.4f}%")
    print()

# === Example 2: Convergence Order — FD Eigenvalues ===
print("=" * 60)
print("Example 2: FD Eigenvalue Convergence Order")
print("=" * 60)

a = np.pi
N_list = [10, 20, 40, 80, 160]
k1_vals = []
for N in N_list:
    k_num = helmholtz_fd_eigenvalues(a, N)
    k1_vals.append(k_num[0])

hs = np.pi / np.array(N_list)
k1_exact = 1.0

def est_order(v3, v2, v1, h3, h2, h1):
    return np.log(abs((v3-v2)/(v2-v1))) / np.log(h3/h2)

p = est_order(k1_vals[0], k1_vals[1], k1_vals[2], hs[0], hs[1], hs[2])
print(f"Convergence order p ≈ {p:.4f} (expect 2.0)")
print()

# === Example 3: Von Neumann Stability Analysis ===
print("=" * 60)
print("Example 3: Von Neumann Stability — Amplification Factor")
print("=" * 60)

def amplification_factor(omega_dt):
    """
    Roots of ρ² - [2-(ωΔt)²]ρ + 1 = 0
    Returns both roots and their magnitudes.
    """
    a = 1.0
    b = -(2 - omega_dt**2)
    c = 1.0
    disc = b**2 - 4*a*c
    if disc >= 0:
        r1 = (-b + np.sqrt(disc)) / (2*a)
        r2 = (-b - np.sqrt(disc)) / (2*a)
    else:
        r1 = (-b + 1j*np.sqrt(-disc)) / (2*a)
        r2 = np.conj(r1)
    return r1, r2

print(f"{'ωΔt':>8} {'|ρ₁|':>10} {'|ρ₂|':>10} {'status':>10}")
print("-" * 40)
for omega_dt in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
    r1, r2 = amplification_factor(omega_dt)
    mag1, mag2 = abs(r1), abs(r2)
    status = "STABLE" if mag1 <= 1.0 and mag2 <= 1.0 else "UNSTABLE"
    print(f"{omega_dt:8.2f} {mag1:10.6f} {mag2:10.6f} {status:>10}")
print()

# === Example 4: Dispersion Relation (leap-frog) ===
print("=" * 60)
print("Example 4: Leap-frog Dispersion Relation (Eq 4.17)")
print("=" * 60)

def numerical_omega(omega_true, dt):
    """
    From (4.17): 4/Δt² * sin²(ΩΔt/2) = ω²
    Solve for Ω given ω and dt.
    """
    rhs = omega_true**2 * dt**2
    if rhs > 4:
        return np.nan  # unstable
    sin_arg = 0.5 * np.sqrt(rhs)
    Omega = (2.0 / dt) * np.arcsin(sin_arg)
    return Omega

omega_true = 2*np.pi * 1e9  # 1 GHz
for dx in [0.1e-3, 0.5e-3, 1.0e-3]:
    h = dx
    dt = 0.9 * h / c_0  # 90% of CFL limit
    Omega = numerical_omega(omega_true, dt)
    err = abs(Omega - omega_true) / omega_true * 100
    print(f"  dx={dx*1e3:.2f}mm  dt={dt*1e15:.2f}fs  freq_err={err:.4f}%")
print()

# === Example 5: Quality Factor from Padé ===
print("=" * 60)
print("Example 5: Resonance Q-factor from Pole Analysis")
print("=" * 60)

def resonance_Q(omega_imag):
    """Q = ω_re / (2*|ω_imag|) for complex pole ω = ω_re + j*ω_imag"""
    return abs(omega_imag) / (2 * abs(omega_imag).real) if omega_imag != 0 else np.inf

# Simulate complex poles for a lossy cavity
omega_re = 2*np.pi * 5e9  # 5 GHz resonance
for Q in [100, 500, 1000, 5000]:
    gamma = omega_re / (2*Q)  # loss rate
    omega_complex = omega_re - 1j * gamma
    Q_check = abs(omega_complex) / (2 * abs(gamma))
    print(f"  Q={Q:5d} → γ={gamma:.2e} rad/s → Q_check={Q_check:.0f}")
print()

print("=" * 60)
print("All examples completed successfully.")
print("=" * 60)
