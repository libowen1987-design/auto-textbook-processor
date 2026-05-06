#!/usr/bin/env python3
"""
taflove_ch4_examples.py
Taflove FDTD 3rd Ed. — Chapter 4: Numerical Dispersion and Stability

Three examples:
  1. v_p/c vs N_lambda for axis/diagonal propagation
  2. 2D TMz cylindrical wave showing anisotropy
  3. CFL stability growth factor
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0

# ============================================================
# Example 4.1: Numerical Phase Velocity Curves
# ============================================================
def example_phase_velocity():
    """Compute v_p/c vs N_lambda for axis and diagonal directions."""
    N_lambda = np.linspace(3, 50, 500)
    S = 0.5

    # Axis propagation: Eq (4.14b)
    arg_axis = (1.0 / S) * np.sin(np.pi * S / N_lambda)
    # Clip to valid domain
    arg_axis = np.clip(arg_axis, -1, 1)
    vp_axis = (np.pi / (N_lambda * S)) / np.arcsin(arg_axis)

    # Diagonal propagation: Eq (4.15b)
    arg_diag = (1.0 / (S * np.sqrt(2))) * np.sin(np.pi * S / N_lambda)
    arg_diag = np.clip(arg_diag, -1, 1)
    vp_diag = (np.pi / (N_lambda * S)) / (np.sqrt(2) * np.arcsin(arg_diag))

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(N_lambda, vp_axis / c, "b-", lw=2, label=r"$\phi = 0^\circ$ (axis)")
    ax.plot(N_lambda, vp_diag / c, "r--", lw=2, label=r"$\phi = 45^\circ$ (diagonal)")
    ax.axhline(1.0, color="gray", ls=":", alpha=0.5)
    ax.set_xlabel(r"Grid Sampling Density $N_\lambda$ (points/$\lambda$)")
    ax.set_ylabel(r"$v_p / c$")
    ax.set_title(f"Numerical Phase Velocity (S = {S})")
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(
        "/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch4_ex1_phase_velocity.png",
        dpi=150,
    )
    plt.close(fig)
    print("[Ch4 Ex1] Phase velocity curves — saved.")
    return


# ============================================================
# Example 4.2: 2D TMz Cylindrical Wave (Anisotropy)
# ============================================================
def example_anisotropy():
    """Visualize anisotropic wavefront from a point source in 2D TMz."""
    N = 300
    L = 2.0
    dx = L / N
    Sc = 0.5
    dt = Sc * dx / c

    eps = epsilon_0
    mu = mu_0
    C_be = dt / eps
    C_bh = dt / mu

    Ez = np.zeros((N, N))
    Hx = np.zeros((N, N - 1))
    Hy = np.zeros((N - 1, N))

    src = N // 2
    freq = 2e9  # 2 GHz
    omega = 2 * np.pi * freq
    N_lambda = c / (freq * dx)
    print(f"  N_lambda = {N_lambda:.1f}")

    Nt = int(1.0 / (freq * dt))  # ~1 period
    t0 = 3.0 / freq

    for n in range(Nt):
        for i in range(N):
            for j in range(N - 1):
                Hx[i, j] += C_bh * (Ez[i, j + 1] - Ez[i, j]) / dx
        for i in range(N - 1):
            for j in range(N):
                Hy[i, j] -= C_bh * (Ez[i + 1, j] - Ez[i, j]) / dx
        for i in range(1, N - 1):
            for j in range(1, N - 1):
                Ez[i, j] += C_be * ((Hy[i, j] - Hy[i - 1, j]) / dx
                                    - (Hx[i, j] - Hx[i, j - 1]) / dx)

        t = n * dt
        source = np.sin(omega * t) * np.exp(-((t - t0) / (0.5 / freq)) ** 2)
        Ez[src, src] = source

    fig, ax = plt.subplots(figsize=(7, 7))
    extent = [-L / 2 * 100, L / 2 * 100, -L / 2 * 100, L / 2 * 100]
    im = ax.imshow(Ez.T, extent=extent, origin="lower", cmap="RdBu_r", vmin=-0.3, vmax=0.3)
    ax.set_xlabel("x [cm]")
    ax.set_ylabel("y [cm]")
    ax.set_title(f"2D TMz Cylindrical Wave (S={Sc}, N_lambda~{N_lambda:.0f})")
    plt.colorbar(im, ax=ax, shrink=0.85)
    plt.tight_layout()
    fig.savefig(
        "/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch4_ex2_anisotropy.png",
        dpi=150,
    )
    plt.close(fig)
    print("[Ch4 Ex2] Anisotropy visualization — saved.")
    return


# ============================================================
# Example 4.3: CFL Growth Factor
# ============================================================
def example_cfl_growth():
    """Plot the growth factor vs k*dx for various S.
    
    For 3D cubic grid, from Eq (4.51b):
    xi = c*dt*sqrt(3*sin^2(k*dx/2)/dx^2) = S*sqrt(3)*|sin(k*dx/2)|
    where S = c*dt/dx for cubic cell (but actual CFL limit is 1/sqrt(3)).
    Here we use the 3D Courant number S_3D = c*dt*sqrt(3)/dx for convenience.
    """
    kdx = np.linspace(0, np.pi, 500)

    S_vals = [0.5, 0.9, 1.0, 1.1]
    labels = [r"$S_{3D}=0.5$ (stable)", r"$S_{3D}=0.9$ (stable)", 
              r"$S_{3D}=1.0$ (CFL limit)", r"$S_{3D}=1.1$ (UNSTABLE)"]

    fig, ax = plt.subplots(figsize=(8, 5))

    for S_val, lbl in zip(S_vals, labels):
        # For 3D cubic grid: xi = S_3D * |sin(k*dx/2)|
        # where S_3D = c*dt*sqrt(1/dx^2+1/dy^2+1/dz^2)
        # The CFL limit is S_3D <= 1
        xi = S_val * np.abs(np.sin(kdx / 2))
        growth = np.where(xi > 1, xi + np.sqrt(xi ** 2 - 1), 1.0)
        ax.plot(kdx / np.pi, growth, lw=2, label=lbl)

    ax.set_xlabel(r"$k\Delta x / \pi$")
    ax.set_ylabel("Growth factor per time-step")
    ax.set_title("CFL Stability Growth Factor (3D cubic grid)")
    ax.legend()
    ax.set_yscale("log")
    ax.set_ylim(1, 1e6)
    ax.axhline(1, color="gray", ls="--", alpha=0.3)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(
        "/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch4_ex3_cfl_growth.png",
        dpi=150,
    )
    plt.close(fig)
    print("[Ch4 Ex3] CFL growth factor — saved.")
    return


# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Taflove Ch.4 — Numerical Dispersion & Stability")
    print("=" * 60)
    example_phase_velocity()
    example_anisotropy()
    example_cfl_growth()
    print("=" * 60)
    print("All Ch.4 examples completed.")
    print("=" * 60)
