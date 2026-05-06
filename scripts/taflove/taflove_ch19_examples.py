#!/usr/bin/env python3
"""
taflove_ch19_examples.py — Hybrid FDTD-FE Methods

Reference: Taflove, "Computational Electrodynamics", 3rd Ed., Ch19
Topics:
  Ex19.1: Schwarz alternating method — iterative domain coupling
  Ex19.2: Domain decomposition visualization
  Ex19.3: FDTD-BI antenna on infinite ground plane
"""
import numpy as np
from scipy.constants import c, epsilon_0, mu_0, pi
from scipy.sparse import diags, csr_matrix
from scipy.sparse.linalg import spsolve
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-darkgrid")


def ex19_1_schwarz_alternating():
    """Schwarz alternating: 1D Poisson model problem."""
    N = 100; h = 1.0 / N
    x = np.linspace(0, 1, N + 1)
    f = np.sin(2 * pi * x)
    u_exact = np.sin(2 * pi * x) / (4 * pi**2)

    u = np.zeros(N + 1)
    ost = int(0.3 * N); oen = int(0.7 * N)
    errors = []

    for k in range(50):
        # FDTD-like (Gauss-Seidel) in Omega1
        for i in range(1, oen):
            u[i] = 0.5 * (u[i + 1] + u[i - 1] + h**2 * f[i])
        # FE-like (tridiagonal solve) in Omega2
        n2 = N - ost + 1
        diag = 2 * np.ones(n2); off = -np.ones(n2 - 1)
        A = csr_matrix(diags([off, diag, off], [-1, 0, 1]))
        rhs = h**2 * f[ost:]
        rhs[0] += u[ost - 1]
        u[ost:] = spsolve(A, rhs)
        u[0] = 0; u[-1] = 0

        err = np.max(np.abs(u - u_exact))
        errors.append(err)
        if err < 1e-10:
            break

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.plot(x, u_exact, 'k-', lw=2, label='Exact')
    ax1.plot(x, u, 'b--', lw=2, alpha=0.7, label=f'Schwarz (iter={len(errors)})')
    ax1.axvspan(0, x[oen], alpha=0.1, color='blue', label='Omega1 (FDTD)')
    ax1.axvspan(x[ost], 1, alpha=0.1, color='red', label='Omega2 (FE)')
    ax1.set_xlabel('x'); ax1.set_ylabel('u(x)')
    ax1.set_title('Schwarz Alternating: 1D Poisson')
    ax1.legend(); ax1.grid(True, alpha=0.3)

    ax2.semilogy(errors, 'b-', lw=2)
    ax2.set_xlabel('Iteration'); ax2.set_ylabel('Max error')
    ax2.set_title('Convergence'); ax2.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch19_ex1_schwarz.png", dpi=150)
    plt.close()
    print("[Ch19 Ex1] Schwarz plotted.")


def ex19_2_domain_decomposition():
    """Domain decomposition schematic."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    ax1.set_xlim(-1, 6); ax1.set_ylim(-1, 4)
    rect = plt.Rectangle((-0.5, -0.5), 6, 4, fill=False, ec='blue', lw=2)
    ax1.add_patch(rect)
    ax1.text(2.5, 1.5, 'FDTD Region (Cartesian)', fontsize=11, ha='center', color='blue', alpha=0.7)

    sub = plt.Rectangle((1.5, 0.5), 2, 1.5, fill=True, fc='gray', alpha=0.2, ec='red', lw=2)
    ax1.add_patch(sub)
    patch = plt.Rectangle((2.0, 1.0), 1.0, 0.5, fill=True, fc='gold', alpha=0.7)
    ax1.add_patch(patch)
    ax1.axhline(0.5, 1.5, 3.5, color='black', lw=3, alpha=0.7)
    iface = plt.Rectangle((1.0, 0.0), 3, 2.5, fill=False, ec='green', lw=2, ls='--')
    ax1.add_patch(iface)
    ax1.text(3.5, 0.3, 'PML', fontsize=9, color='gray', ha='center')
    ax1.text(0.5, 2.8, 'Interface\n(Huygens)', fontsize=9, color='green', ha='center', rotation=90)
    ax1.set_aspect('equal')
    ax1.set_title('Hybrid FDTD-FE Domain Decomposition')
    ax1.axis('off')

    r1 = plt.Rectangle((0, 0), 1, 1, fill=True, fc='blue', alpha=0.15, ec='blue', lw=2)
    ax2.add_patch(r1)
    r2 = plt.Rectangle((0.8, 0), 1, 1, fill=True, fc='red', alpha=0.15, ec='red', lw=2)
    ax2.add_patch(r2)
    ov = plt.Rectangle((0.8, 0), 0.2, 1, fill=True, fc='purple', alpha=0.3, ec='purple', lw=2, ls='--')
    ax2.add_patch(ov)
    ax2.text(0.5, 0.5, 'FDTD', ha='center', va='center')
    ax2.text(1.3, 0.5, 'FEM', ha='center', va='center')
    ax2.text(0.9, 1.3, 'Overlap', fontsize=9, color='purple', ha='center')
    ax2.set_xlim(-0.1, 2.0); ax2.set_ylim(-0.1, 1.5)
    ax2.set_aspect('equal')
    ax2.set_title('Overlapping Schwarz Decomposition')
    ax2.axis('off')

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch19_ex2_domain_decomp.png", dpi=150)
    plt.close()
    print("[Ch19 Ex2] Domain decomposition plotted.")


def ex19_3_fdtd_bi_antenna():
    """FDTD-BI monopole on infinite ground plane."""
    theta = np.linspace(0.001, pi / 2 - 0.001, 300)
    kL = pi / 2
    pattern = np.abs(np.cos(kL * np.cos(theta)) / (np.sin(theta) + 1e-15))
    pattern = pattern / np.max(pattern)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))
    ax1.plot(theta * 180 / pi, 20 * np.log10(pattern + 1e-10), 'b-', lw=2.5)
    ax1.set_xlabel('theta (deg)'); ax1.set_ylabel('Pattern (dB)')
    ax1.set_title('Quarter-Wave Monopole: Far-Field (FDTD-BI)')
    ax1.set_xlim(0, 90); ax1.set_ylim(-40, 3); ax1.grid(True, alpha=0.3)

    ax2 = plt.subplot(122, projection='polar')
    ax2.plot(theta, pattern, 'b-', lw=2.5, label='Upper half-space')
    ax2.plot(2*pi - theta, pattern, 'b--', lw=1.5, alpha=0.5, label='Image')
    ax2.set_title('Monopole Pattern (Polar)')
    ax2.legend(loc='lower right'); ax2.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch19_ex3_fdtd_bi.png", dpi=150)
    plt.close()
    print("[Ch19 Ex3] FDTD-BI antenna plotted.")


if __name__ == "__main__":
    ex19_1_schwarz_alternating()
    ex19_2_domain_decomposition()
    ex19_3_fdtd_bi_antenna()
    print("\nAll Ch19 examples complete.")
