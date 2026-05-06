#!/usr/bin/env python3
"""
taflove_ch3_examples.py
Taflove FDTD 3rd Ed. — Chapter 3: Maxwell's Equations & Yee Algorithm

Three examples:
  1. 1D FDTD (Ez, Hy) — TEM wave in free space and lossy medium
  2. 2D TMz FDTD — point source radiation
  3. Yee cell 3D visualization schematic
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0

# ============================================================
# Example 3.1: 1D FDTD — TEM (Ez, Hy) in free space and lossy
# ============================================================
def example_1d_yee_tem():
    """
    Solve 1D Maxwell's equations for Ez, Hy (x-directed, z-polarized TEM).
    - Yee grid: Ez at integer nodes, Hy at half-integer nodes
    - Leapfrog: Hy updated at integer + 0.5 time-steps
    - Compare free-space vs lossy (sigma = 0.01 S/m)
    """
    Nx = 400
    Lx = 1.0
    dx = Lx / Nx
    Sc = 0.95                # Courant number
    dt = Sc * dx / c

    # Material
    epsilon_r = 1.0
    sigma_vals = [0.0, 0.01]  # S/m
    mu_r = 1.0
    sigma_star = 0.0

    eps = epsilon_r * epsilon_0
    mu = mu_r * mu_0

    # Coefficients
    def get_coeffs(sigma):
        C_ae = (1 - sigma * dt / (2 * eps)) / (1 + sigma * dt / (2 * eps))
        C_be = (dt / eps) / (1 + sigma * dt / (2 * eps))
        C_ah = (1 - sigma_star * dt / (2 * mu)) / (1 + sigma_star * dt / (2 * mu))
        C_bh = (dt / mu) / (1 + sigma_star * dt / (2 * mu))
        return C_ae, C_be, C_ah, C_bh

    Nt = 500
    source_idx = Nx // 4
    probe_idx = Nx // 2
    tau = 30 * dt
    t0 = 6 * tau

    results = {}
    for sigma in sigma_vals:
        C_ae, C_be, C_ah, C_bh = get_coeffs(sigma)

        Ez = np.zeros(Nx)
        Hy = np.zeros(Nx - 1)

        Ez_probe = np.zeros(Nt)

        # Mur ABC coefficient
        K = (c * dt - dx) / (c * dt + dx)

        for n in range(Nt):
            # Update Hy: dHy/dt = (1/mu) * dEz/dx
            for i in range(Nx - 1):
                Hy[i] = C_ah * Hy[i] + C_bh * (Ez[i + 1] - Ez[i]) / dx

            # Update Ez (interior)
            for i in range(1, Nx - 1):
                Ez[i] = C_ae * Ez[i] + C_be * (Hy[i] - Hy[i - 1]) / dx

            # Hard source
            pulse = np.exp(-((n * dt - t0) / tau) ** 2)
            Ez[source_idx] = pulse

            # Mur ABC
            Ez[0] = Ez[1] + K * (Ez[0] - Ez[1])
            Ez[-1] = Ez[-2] + K * (Ez[-1] - Ez[-2])

            Ez_probe[n] = Ez[probe_idx]

        results[sigma] = {"Ez_probe": Ez_probe, "Ez_final": Ez.copy()}

    # --- Plot ---
    fig, axes = plt.subplots(2, 1, figsize=(10, 7))

    x_cm = np.arange(Nx) * dx * 100
    ax = axes[0]
    for sigma in sigma_vals:
        label = f"$\\sigma$ = {sigma} S/m (free space)" if sigma == 0 else f"$\\sigma$ = {sigma} S/m (lossy)"
        ax.plot(x_cm, results[sigma]["Ez_final"], label=label)
    ax.set_xlabel("x [cm]")
    ax.set_ylabel("E_z [V/m]")
    ax.set_title("1D TEM FDTD: Ez Snapshot (t = final)")
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    for sigma in sigma_vals:
        label = f"$\\sigma$ = {sigma} S/m"
        t_ns = np.arange(Nt) * dt * 1e9
        ax.plot(t_ns, results[sigma]["Ez_probe"], label=label)
    ax.set_xlabel("Time [ns]")
    ax.set_ylabel("E_z at probe [V/m]")
    ax.set_title("Time Waveform at x = 50 cm")
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(
        "/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch3_ex1_1d_tem.png",
        dpi=150,
    )
    plt.close(fig)
    print("[Ch3 Ex1] 1D TEM FDTD — figure saved.")
    return


# ============================================================
# Example 3.2: 2D TMz FDTD — Point Source Radiation
# ============================================================
def example_2d_tmz():
    """
    Solve 2D TMz Maxwell's equations:
    Ez, Hx, Hy. Point source at center. Mur ABC.
    """
    Nx, Ny = 150, 150
    L = 1.0
    dx = L / Nx
    dy = L / Ny
    Sc = 0.95
    dt = Sc / (c * np.sqrt(1 / dx ** 2 + 1 / dy ** 2))

    eps = epsilon_0
    mu = mu_0

    C_ae = 1.0
    C_be = dt / eps
    C_ah = 1.0
    C_bh = dt / mu

    Ez = np.zeros((Nx, Ny))
    Hx = np.zeros((Nx, Ny - 1))
    Hy = np.zeros((Nx - 1, Ny))

    Nt = 300
    src_x, src_y = Nx // 2, Ny // 2
    tau = 20 * dt
    t0 = 6 * tau

    # Store snapshots
    snap_t = [0, 100, 200, 299]
    snap_Ez = {}

    for n in range(Nt):
        # Update Hx: Hx[i,j] += (dt/mu) * (Ez[i,j+1] - Ez[i,j]) / dy
        for i in range(Nx):
            for j in range(Ny - 1):
                Hx[i, j] = C_ah * Hx[i, j] - C_bh * (Ez[i, j + 1] - Ez[i, j]) / dy

        # Update Hy: Hy[i,j] -= (dt/mu) * (Ez[i+1,j] - Ez[i,j]) / dx
        for i in range(Nx - 1):
            for j in range(Ny):
                Hy[i, j] = C_ah * Hy[i, j] + C_bh * (Ez[i + 1, j] - Ez[i, j]) / dx

        # Update Ez (interior)
        for i in range(1, Nx - 1):
            for j in range(1, Ny - 1):
                Ez[i, j] = C_ae * Ez[i, j] + C_be * (
                    (Hy[i, j] - Hy[i - 1, j]) / dx
                    - (Hx[i, j] - Hx[i, j - 1]) / dy
                )

        # Hard source
        pulse = np.exp(-((n * dt - t0) / tau) ** 2)
        Ez[src_x, src_y] = pulse

        # Mur ABC (1st order)
        K_x = (c * dt - dx) / (c * dt + dx)
        K_y = (c * dt - dy) / (c * dt + dy)
        Ez[0, :] = Ez[1, :] + K_x * (Ez[0, :] - Ez[1, :])
        Ez[-1, :] = Ez[-2, :] + K_x * (Ez[-1, :] - Ez[-2, :])
        Ez[:, 0] = Ez[:, 1] + K_y * (Ez[:, 0] - Ez[:, 1])
        Ez[:, -1] = Ez[:, -2] + K_y * (Ez[:, -1] - Ez[:, -2])

        if n in snap_t:
            snap_Ez[n] = Ez.copy()

    # --- Plot ---
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
    extent = [0, L * 100, 0, L * 100]

    for idx, n in enumerate(snap_t):
        ax = axes[idx // 2, idx % 2]
        im = ax.imshow(
            snap_Ez[n].T,
            extent=extent,
            origin="lower",
            cmap="RdBu_r",
            vmin=-0.5,
            vmax=0.5,
        )
        ax.set_xlabel("x [cm]")
        ax.set_ylabel("y [cm]")
        ax.set_title(f"Ez at t = {n * dt * 1e9:.2f} ns")
        plt.colorbar(im, ax=ax, shrink=0.8)

    plt.tight_layout()
    fig.savefig(
        "/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch3_ex2_2d_tmz.png",
        dpi=150,
    )
    plt.close(fig)
    print("[Ch3 Ex2] 2D TMz FDTD — figure saved.")
    return


# ============================================================
# Example 3.3: Yee Cell 3D Schematic
# ============================================================
def example_yee_cell_schematic():
    """
    Draw a 3D Yee unit cell showing the staggered E and H components.
    """
    from mpl_toolkits.mplot3d import Axes3D
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")

    # Unit cell corners: (0,0,0) to (1,1,1)
    w = 1.0

    # Draw the cube edges
    corners = [
        [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
        [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1],
    ]
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7),
    ]
    for e in edges:
        ax.plot3D(
            [corners[e[0]][0], corners[e[1]][0]],
            [corners[e[0]][1], corners[e[1]][1]],
            [corners[e[0]][2], corners[e[1]][2]],
            "gray", alpha=0.4,
        )

    # E-field components (edge centers)
    # Ex at (0.5, 0, 0), (0.5, 1, 0), (0.5, 0, 1), (0.5, 1, 1)
    Ex_pos = [[0.5, 0, 0], [0.5, 1, 0], [0.5, 0, 1], [0.5, 1, 1]]
    for p in Ex_pos:
        ax.quiver(p[0], p[1], p[2], 1, 0, 0, color="tab:blue", length=0.3, arrow_length_ratio=0.2)

    # Ey at (0, 0.5, 0), (1, 0.5, 0), (0, 0.5, 1), (1, 0.5, 1)
    Ey_pos = [[0, 0.5, 0], [1, 0.5, 0], [0, 0.5, 1], [1, 0.5, 1]]
    for p in Ey_pos:
        ax.quiver(p[0], p[1], p[2], 0, 1, 0, color="tab:blue", length=0.3, arrow_length_ratio=0.2)

    # Ez at (0, 0, 0.5), (1, 0, 0.5), (0, 1, 0.5), (1, 1, 0.5)
    Ez_pos = [[0, 0, 0.5], [1, 0, 0.5], [0, 1, 0.5], [1, 1, 0.5]]
    for p in Ez_pos:
        ax.quiver(p[0], p[1], p[2], 0, 0, 1, color="tab:blue", length=0.3, arrow_length_ratio=0.2)

    # H-field components (face centers)
    # Hx at (0.5, 0.5, 0), (0.5, 0.5, 1)
    Hx_pos = [[0.5, 0.5, 0], [0.5, 0.5, 1]]
    for p in Hx_pos:
        ax.quiver(p[0], p[1], p[2], 1, 0, 0, color="tab:red", length=0.3, arrow_length_ratio=0.2)

    # Hy at (0.5, 0, 0.5), (0.5, 1, 0.5)
    Hy_pos = [[0.5, 0, 0.5], [0.5, 1, 0.5]]
    for p in Hy_pos:
        ax.quiver(p[0], p[1], p[2], 0, 1, 0, color="tab:red", length=0.3, arrow_length_ratio=0.2)

    # Hz at (0, 0.5, 0.5), (1, 0.5, 0.5)
    Hz_pos = [[0, 0.5, 0.5], [1, 0.5, 0.5]]
    for p in Hz_pos:
        ax.quiver(p[0], p[1], p[2], 0, 0, 1, color="tab:red", length=0.3, arrow_length_ratio=0.2)

    # Axis labels
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    ax.set_title("Yee Unit Cell — E (blue) and H (red)", fontsize=12)

    # Remove tick labels
    ax.set_xticks([0, 0.5, 1])
    ax.set_yticks([0, 0.5, 1])
    ax.set_zticks([0, 0.5, 1])

    # Legend
    ax.quiver([100], [100], [100], 0, 0, 1, color="tab:blue", length=0.3,
              label="E-field components")  # Dummy vector
    ax.quiver([100], [100], [100], 0, 0, 1, color="tab:red", length=0.3,
              label="H-field components")
    ax.legend(loc="upper right", fontsize=9)

    plt.tight_layout()
    fig.savefig(
        "/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch3_ex3_yee_cell.png",
        dpi=150,
    )
    plt.close(fig)
    print("[Ch3 Ex3] Yee cell schematic — figure saved.")
    return


# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Taflove Ch.3 — Maxwell's Eqs. & Yee Algorithm Examples")
    print("=" * 60)

    example_1d_yee_tem()
    example_2d_tmz()
    example_yee_cell_schematic()

    print("=" * 60)
    print("All Ch.3 examples completed successfully.")
    print("=" * 60)
