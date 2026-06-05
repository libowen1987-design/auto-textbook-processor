#!/usr/bin/env python3
"""
taflove_ch2_examples.py
Taflove FDTD 3rd Ed. — Chapter 2: The One-Dimensional Scalar Wave Equation

Three examples:
  1. 1D scalar wave FDTD — Gaussian pulse at S=1 vs S=0.5
  2. Numerical dispersion — phase velocity vs grid sampling density N_lambda
  3. CFL stability — energy monitor at S=0.5, 1.0, 1.05
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.constants import c

# ============================================================
# Example 2.1: Scalar Wave Equation — Magic Step vs Dispersive
# ============================================================
def example_scalar_wave_pulse():
    """
    Solve ∂²u/∂t² = c² ∂²u/∂x² via central differences.
    Compare S=1 (magic time-step, exact) vs S=0.5 (dispersive).
    """
    Nx = 500
    Lx = 1.0            # m
    dx = Lx / Nx

    # S values
    S_vals = [1.0, 0.5]
    Nt_vals = [350, 700]  # same physical time: t_end = 350*dt for S=1

    results = {}
    for S_val, Nt in zip(S_vals, Nt_vals):
        dt = S_val * dx / c
        u = np.zeros(Nx)
        u_old = np.zeros(Nx)

        # Gaussian pulse initial condition
        x = np.arange(Nx) * dx
        x0 = 0.2
        sigma = 0.01
        u[:] = np.exp(-((x - x0) / sigma) ** 2)
        # u_old same (zero initial velocity)
        u_old[:] = u[:]

        snap_idx = [0, Nt // 4, Nt // 2, 3 * Nt // 4, Nt - 1]
        snap_u = {}

        for n in range(Nt):
            # Update interior points (2.16)
            u_new = np.zeros(Nx)
            for i in range(1, Nx - 1):
                u_new[i] = (2 * u[i] - u_old[i]
                            + S_val ** 2 * (u[i + 1] - 2 * u[i] + u[i - 1]))
            # Mur ABC at boundaries (simple for this scheme)
            K = (c * dt - dx) / (c * dt + dx) if S_val <= 1 else 0
            u_new[0] = u[1] + K * (u[0] - u[1])
            u_new[-1] = u[-2] + K * (u[-1] - u[-2])

            u_old = u.copy()
            u = u_new.copy()

            if n in snap_idx:
                snap_u[n] = u.copy()

        results[S_val] = {"snap": snap_u, "dt": dt, "Nt": Nt, "S": S_val}

    # --- Plot ---
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    x_cm = x * 100

    for idx_S, (S_val, r) in enumerate(results.items()):
        ax = axes[idx_S]
        for n, u_arr in r["snap"].items():
            t_ns = n * r["dt"] * 1e9
            ax.plot(x_cm, u_arr, label=f"t = {t_ns:.2f} ns")
        ax.set_xlabel("x [cm]")
        ax.set_ylabel("u(x,t)")
        ax.set_title(f"Scalar Wave Propagation (S = {S_val})")
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(
        "/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch2_ex1_scalar_wave.png",
        dpi=150,
    )
    plt.close(fig)
    print("[Ch2 Ex1] Scalar wave S=1 vs S=0.5 — figure saved.")
    return


# ============================================================
# Example 2.2: Numerical Phase Velocity vs Grid Sampling
# ============================================================
def example_numerical_dispersion():
    """
    Compute numerical phase velocity v_p/c as function of
    grid sampling density N_lambda = lambda_0 / dx.
    Using Eq. (2.32c) and (2.26) inversion.
    """
    N_lambda_vals = np.linspace(3, 50, 200)
    S = 0.5

    vp_norm = np.zeros_like(N_lambda_vals)
    pct_error = np.zeros_like(N_lambda_vals)

    for idx, N_lambda in enumerate(N_lambda_vals):
        k0_dx = 2 * np.pi / N_lambda           # physical k * dx
        omega_dt = k0_dx * S                    # omega * dt = k*dx * S

        # From (2.26): sin(k_tilde*dx/2) = (1/S) * sin(omega*dt/2)
        # k_tilde_real = (2/dx) * arcsin((1/S)*sin(omega*dt/2))
        arg = (1.0 / S) * np.sin(omega_dt / 2)
        # For N_lambda >= 3, arg <= 1 (real k regime)
        if arg <= 1.0:
            k_tilde_dx = 2 * np.arcsin(arg)
        else:
            k_tilde_dx = np.pi  # Nyquist limit

        vp_norm[idx] = omega_dt / (k_tilde_dx * S)   # v_p/c
        pct_error[idx] = 100 * (1 - vp_norm[idx])     # percentage below c

    # --- Plot ---
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    ax = axes[0]
    ax.plot(N_lambda_vals, vp_norm, "b-", lw=2)
    ax.axhline(1.0, color="gray", ls="--", alpha=0.5)
    ax.set_xlabel(r"Grid Sampling Density $N_\lambda$ (points/$\lambda_0$)")
    ax.set_ylabel(r"$v_p / c$")
    ax.set_title("Numerical Phase Velocity (S = 0.5)")
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.loglog(N_lambda_vals, pct_error, "r-", lw=2)
    # Reference slope: 1/N^2
    ax.loglog(N_lambda_vals, 100 * (1 / N_lambda_vals) ** 2, "k--", alpha=0.5,
              label=r"$1/N_\lambda^2$ slope")
    ax.set_xlabel(r"$N_\lambda$ (points/$\lambda_0$)")
    ax.set_ylabel("Phase Velocity Error [%]")
    ax.set_title("Percent Error in $v_p$ (S = 0.5)")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3, which="both")

    plt.tight_layout()
    fig.savefig(
        "/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch2_ex2_dispersion.png",
        dpi=150,
    )
    plt.close(fig)
    print("[Ch2 Ex2] Numerical dispersion curves — figure saved.")
    return


# ============================================================
# Example 2.3: CFL Stability Monitor
# ============================================================
def example_cfl_stability():
    """
    Observe field energy for S = 0.5 (stable), S = 1.0 (magic), S = 1.05 (unstable).
    """
    Nx = 200
    Lx = 1.0
    dx = Lx / Nx
    x = np.arange(Nx) * dx
    Nt = 500

    S_list = [0.5, 1.0, 1.05]
    colors = ["blue", "green", "red"]
    labels = [r"$S = 0.5$ (stable)", r"$S = 1.0$ (magic)", r"$S = 1.05$ (UNSTABLE)"]

    fig, axes = plt.subplots(2, 1, figsize=(10, 8))

    for S_val, clr, lbl in zip(S_list, colors, labels):
        dt = S_val * dx / c
        u = np.exp(-((x - 0.2) / 0.02) ** 2)
        u_old = u.copy()

        energy = np.zeros(Nt)
        # Probe at x = 0.5 m
        probe_idx = int(Nx // 2)
        probe = np.zeros(Nt)

        K = (c * dt - dx) / (c * dt + dx) if S_val <= 1 else 0

        for n in range(Nt):
            u_new = np.zeros(Nx)
            for i in range(1, Nx - 1):
                u_new[i] = (2 * u[i] - u_old[i]
                            + S_val ** 2 * (u[i + 1] - 2 * u[i] + u[i - 1]))
            if S_val <= 1:
                u_new[0] = u[1] + K * (u[0] - u[1])
                u_new[-1] = u[-2] + K * (u[-1] - u[-2])

            u_old = u.copy()
            u = u_new.copy()

            energy[n] = np.sum(u ** 2) * dx
            probe[n] = u[probe_idx]

        ax = axes[0]
        t_ns = np.arange(Nt) * dt * 1e9
        ax.semilogy(t_ns, energy / energy[0], color=clr, label=lbl)
        ax.set_xlabel("Time [ns]")
        ax.set_ylabel("Normalized Energy $\\int u^2 dx$")
        ax.set_title("Total Field Energy (CFL Stability Monitor)")
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
        ax.set_ylim(1e-5, 1e10)

        # Final snapshot
        ax2 = axes[1]
        ax2.plot(x * 100, u, color=clr, label=lbl + f" (t={Nt*dt*1e9:.2f} ns)", alpha=0.8)

    axes[1].set_xlabel("x [cm]")
    axes[1].set_ylabel("u(x)")
    axes[1].set_title("Final Field Snapshot")
    axes[1].legend(fontsize=8)
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(
        "/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch2_ex3_cfl_monitor.png",
        dpi=150,
    )
    plt.close(fig)
    print("[Ch2 Ex3] CFL stability monitor — figure saved.")
    return


# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Taflove Ch.2 — 1D Scalar Wave Equation Examples")
    print("=" * 60)

    example_scalar_wave_pulse()
    example_numerical_dispersion()
    example_cfl_stability()

    print("=" * 60)
    print("All Ch.2 examples completed successfully.")
    print("=" * 60)
