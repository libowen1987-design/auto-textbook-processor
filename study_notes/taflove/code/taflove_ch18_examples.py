#!/usr/bin/env python3
"""
taflove_ch18_examples.py — Unconditionally Stable FDTD (ADI / CN / LOD)

Reference: Taflove, "Computational Electrodynamics", 3rd Ed., Ch18
Topics:
  Ex18.1: ADI-FDTD — 2D waveguide with Sc=5
  Ex18.2: Stability comparison — FDTD vs ADI vs CN
  Ex18.3: Numerical dispersion vs Courant number
"""
import numpy as np
from scipy.constants import c, epsilon_0, mu_0, pi
from scipy.sparse import diags, csr_matrix
from scipy.sparse.linalg import spsolve
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-darkgrid")


def ex18_1_adi_2d():
    """ADI-FDTD 2D waveguide with Sc=5."""
    Nx, Ny = 100, 80
    dx = dy = 0.01
    Sc = 5.0
    dt = Sc * dx / (c * np.sqrt(2))
    Nt = int(200 / Sc) + 1

    Ez = np.zeros((Nx, Ny))
    Hx = np.zeros((Nx, Ny - 1))
    Hy = np.zeros((Nx - 1, Ny))
    ae = dt / (2 * epsilon_0); ah = dt / (2 * mu_0)

    sx, sy = Nx // 4, Ny // 2
    ox, oy = 3 * Nx // 4, Ny // 2
    obs = []

    alpha = ae * ah / dx**2

    for n in range(Nt):
        Hx += ah * (Ez[:, 1:] - Ez[:, :-1]) / dy
        Hy -= ah * (Ez[1:, :] - Ez[:-1, :]) / dx

        dHy_dx = np.zeros_like(Ez)
        dHy_dx[1:-1, :] = (Hy[1:, :] - Hy[:-1, :]) / dx
        dHx_dy = np.zeros_like(Ez)
        dHx_dy[:, 1:-1] = (Hx[:, 1:] - Hx[:, :-1]) / dy
        rhs = Ez + ae * (dHy_dx - dHx_dy)

        # Step 1: implicit in x (for each y)
        diag_x = (1 + 2 * alpha) * np.ones(Nx)
        diag_x[0] = 1 + alpha; diag_x[-1] = 1 + alpha
        off_x = -alpha * np.ones(Nx - 1)
        Ax = csr_matrix(diags([off_x, diag_x, off_x], [-1, 0, 1]))
        for j in range(Ny):
            Ez[:, j] = spsolve(Ax, rhs[:, j])

        # Step 2: implicit in y (for each x)
        beta = ae * ah / dy**2
        diag_y = (1 + 2 * beta) * np.ones(Ny)
        diag_y[0] = 1 + beta; diag_y[-1] = 1 + beta
        off_y = -beta * np.ones(Ny - 1)
        Ay = csr_matrix(diags([off_y, diag_y, off_y], [-1, 0, 1]))
        for i in range(Nx):
            Ez[i, :] = spsolve(Ay, Ez[i, :])

        pulse = np.exp(-((n - Nt / 4) / (Nt / 12))**2)
        Ez[sx, sy] += pulse * 0.01
        obs.append(Ez[ox, oy])

    time = np.arange(len(obs)) * dt * 1e9
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    ax1.plot(time, obs, 'b-', lw=1.5)
    ax1.set_xlabel('Time (ns)'); ax1.set_ylabel('Ez (V/m)')
    ax1.set_title(f'ADI-FDTD 2D (Sc={Sc})'); ax1.grid(True, alpha=0.3)

    ax2.imshow(Ez.T, origin='lower', cmap='RdBu_r', aspect='auto')
    ax2.set_xlabel('x'); ax2.set_ylabel('y')
    ax2.set_title(f'Ez Snapshot')
    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch18_ex1_adi_2d.png", dpi=150)
    plt.close()
    print("[Ch18 Ex1] ADI-FDTD 2D done.")


def ex18_2_stability_comparison():
    """Growth factor vs CFL for FDTD, ADI, CN."""
    Sc = np.logspace(-1, 2, 200)
    g_fdtd = np.sqrt(np.maximum(1 - Sc**2, 0))
    g_adi = np.where(Sc <= 1, np.sqrt((1 - Sc**2) / (1 + Sc**2 + 1e-10)),
                     np.sqrt((Sc**2 - 1) / (Sc**2 + 1)))
    g_cn = np.sqrt(np.abs((1 - Sc**2 / 4) / (1 + Sc**2 / 4)))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.semilogx(Sc, g_fdtd, 'b-', lw=2.5, label='Standard FDTD')
    ax1.semilogx(Sc, g_adi, 'r-', lw=2.5, label='ADI-FDTD')
    ax1.semilogx(Sc, g_cn, 'g-', lw=2.5, label='CN-FDTD')
    ax1.axhline(1, color='gray', ls='--', alpha=0.5)
    ax1.axvline(1, color='gray', ls=':', alpha=0.4)
    ax1.set_xlabel('Courant number Sc'); ax1.set_ylabel('|g|')
    ax1.set_title('Growth Factor vs Sc')
    ax1.legend(); ax1.grid(True, alpha=0.3, which='both')

    ax2.semilogx(Sc, g_fdtd, 'b-', lw=2, label='FDTD')
    ax2.semilogx(Sc, np.ones_like(Sc), 'b--', lw=1, alpha=0.5, label='Stable bound')
    ax2.semilogx(Sc, g_adi, 'r-', lw=2, label='ADI-FDTD')
    ax2.axvspan(1, 100, alpha=0.1, color='red', label='ADI/CN stable region')
    ax2.set_xlabel('Sc'); ax2.set_ylabel('|g|')
    ax2.set_title('Stability Regions')
    ax2.legend(loc='lower left', fontsize=9); ax2.grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch18_ex2_stability.png", dpi=150)
    plt.close()
    print("[Ch18 Ex2] Stability plotted.")


def ex18_3_dispersion():
    """Phase velocity error vs Courant number."""
    Sc = np.logspace(0, 2, 100)
    N_lam = 20.0
    err_fdtd = np.where(Sc <= 1, np.pi**2 / (6 * (N_lam * Sc)**2) * 100, np.nan)
    err_adi = Sc**2 * np.pi**2 / (12 * N_lam**2) * 100
    err_cn = Sc**2 * np.pi**2 / (24 * N_lam**2) * 100

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.loglog(Sc, err_fdtd, 'b-', lw=2.5, label='Standard FDTD')
    ax.loglog(Sc, err_adi, 'r-', lw=2.5, label='ADI-FDTD')
    ax.loglog(Sc, err_cn, 'g-', lw=2.5, label='CN-FDTD')
    ax.axvline(1, color='gray', ls='--', alpha=0.5)
    ax.axhline(1, color='gray', ls=':', alpha=0.4, label='1% error')
    ax.set_xlabel('Courant number Sc'); ax.set_ylabel('Phase error (%)')
    ax.set_title('Numerical Dispersion (20 cells/lambda)')
    ax.legend(); ax.grid(True, alpha=0.3, which='both')
    ax.set_xlim(1, 100); ax.set_ylim(0.01, 100)

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch18_ex3_dispersion.png", dpi=150)
    plt.close()
    print("[Ch18 Ex3] Dispersion plotted.")


if __name__ == "__main__":
    ex18_1_adi_2d()
    ex18_2_stability_comparison()
    ex18_3_dispersion()
    print("\nAll Ch18 examples complete.")
