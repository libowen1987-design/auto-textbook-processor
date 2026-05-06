#!/usr/bin/env python3
"""
taflove_ch6_examples.py
Taflove FDTD 3rd Ed. — Chapter 6: Analytical Absorbing Boundary Conditions

Three examples:
  1. 1D FDTD — Mur 1st-order ABC vs PEC reflection
  2. 2D TMz — Mur 2nd-order ABC reflection coefficient vs angle
  3. Higdon ABC — optimized angle absorption
"""

import numpy as np
from scipy.constants import c, epsilon_0, mu_0
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-darkgrid")

# ============================================================
# Example 6.1: 1D Mur 1st-Order ABC vs PEC
# ============================================================
def example_6_1_mur_1d():
    """Compare Mur 1st-order ABC with PEC termination in 1D FDTD."""
    Nz = 200
    dz = 1e-3
    Sc = 0.95
    dt = Sc * dz / c

    # Mur coefficient
    K_mur = (c * dt - dz) / (c * dt + dz)

    Ez_mur = np.zeros(Nz)
    Hy_mur = np.zeros(Nz - 1)
    Ez_pec = np.zeros(Nz)
    Hy_pec = np.zeros(Nz - 1)

    source_pos = 50
    tau = 30 * dt
    n0 = 6 * tau / dt

    Nt = 600
    snap_mur = {}
    snap_pec = {}
    snap_times = [100, 200, 300, 400]

    for n in range(Nt):
        for k in range(Nz - 1):
            Hy_mur[k] += Sc * (Ez_mur[k+1] - Ez_mur[k])
            Hy_pec[k] += Sc * (Ez_pec[k+1] - Ez_pec[k])

        for k in range(1, Nz - 1):
            Ez_mur[k] += Sc * (Hy_mur[k] - Hy_mur[k-1])
            Ez_pec[k] += Sc * (Hy_pec[k] - Hy_pec[k-1])

        # Soft source
        gaussian = np.exp(-((n - n0) / (tau/dt))**2)
        if n < n0 + 3 * tau/dt:
            Ez_mur[source_pos] = gaussian
            Ez_pec[source_pos] = gaussian

        # Mur ABC boundary
        Ez_mur[0] = Ez_mur[1] + K_mur * (Ez_mur[0] - Ez_mur[1])
        Ez_mur[-1] = Ez_mur[-2] + K_mur * (Ez_mur[-1] - Ez_mur[-2])
        # PEC boundaries
        Ez_pec[0] = 0.0
        Ez_pec[-1] = 0.0

        if n in snap_times:
            snap_mur[n] = Ez_mur.copy()
            snap_pec[n] = Ez_pec.copy()

    # Energy in domain
    energy_mur = [np.sum(snap_mur[n]**2) for n in snap_times]
    energy_pec = [np.sum(snap_pec[n]**2) for n in snap_times]

    fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
    x_axis = np.arange(Nz) * dz * 1e3

    for n in snap_times:
        axes[0].plot(x_axis, snap_mur[n], label=f"n={n}")
    axes[0].set_title("Mur 1st-Order ABC — Clean Absorption")
    axes[0].set_ylabel("E_z (V/m)")
    axes[0].legend(fontsize=8)
    axes[0].set_ylim(-0.5, 1.1)

    for n in snap_times:
        axes[1].plot(x_axis, snap_pec[n], label=f"n={n}")
    axes[1].set_title("PEC Boundaries — Full Reflection")
    axes[1].set_xlabel("x (mm)")
    axes[1].set_ylabel("E_z (V/m)")
    axes[1].legend(fontsize=8)
    axes[1].set_ylim(-0.5, 1.1)

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch6_ex1_mur_1d.png", dpi=150)
    plt.close()
    print("[Ch6 Ex1] Mur 1D comparison plotted.")


# ============================================================
# Example 6.2: Mur 2nd-Order ABC Reflection vs Angle (2D TMz)
# ============================================================
def example_6_2_mur_reflection_vs_angle():
    """Compute theoretical reflection coefficient for Mur 2nd-order ABC."""
    angles = np.linspace(0, 89, 200)
    theta_rad = np.deg2rad(angles)

    # 1st-order Mur: R = |(cosθ - 1)/(cosθ + 1)|
    R1 = np.abs((np.cos(theta_rad) - 1) / (np.cos(theta_rad) + 1))

    # 2nd-order Mur (Padé (2,0)): R = |(cosθ - (1 - 0.5*sin²θ))/(cosθ + (1 - 0.5*sin²θ))|²
    num = np.cos(theta_rad) - (1 - 0.5 * np.sin(theta_rad)**2)
    den = np.cos(theta_rad) + (1 - 0.5 * np.sin(theta_rad)**2)
    R2_mur = (num / den)**2

    # 3rd-order Higdon with angles [0, 45°]
    R3 = np.abs((np.cos(theta_rad) - np.cos(np.deg2rad(0))) / (np.cos(theta_rad) + np.cos(np.deg2rad(0))))
    R3 *= np.abs((np.cos(theta_rad) - np.cos(np.deg2rad(45))) / (np.cos(theta_rad) + np.cos(np.deg2rad(45))))
    R3 *= np.abs((np.cos(theta_rad) - np.cos(np.deg2rad(60))) / (np.cos(theta_rad) + np.cos(np.deg2rad(60))))

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.semilogy(angles, R1, 'b-', lw=2, label='Mur 1st-order')
    ax.semilogy(angles, R2_mur, 'r-', lw=2, label='Mur 2nd-order')
    ax.semilogy(angles, R3, 'g-', lw=2, label='Higdon 3rd-order [0°,45°,60°]')
    ax.axhline(1e-2, color='gray', ls=':', alpha=0.5)
    ax.axhline(1e-4, color='gray', ls=':', alpha=0.5)
    ax.set_xlabel("Incidence Angle θ (deg)")
    ax.set_ylabel("Reflection Coefficient |R|")
    ax.set_title("Theoretical ABC Reflection Coefficients vs. Incidence Angle")
    ax.set_ylim(1e-6, 1)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch6_ex2_reflection_coefficient.png", dpi=150)
    plt.close()
    print("[Ch6 Ex2] Reflection coefficient plotted.")


# ============================================================
# Example 6.3: 2D Mur ABC — Point Source at Center
# ============================================================
def example_6_3_mur_2d_point_source():
    """2D TMz with Mur 2nd-order ABC and point source at center."""
    Nx = Ny = 100
    dx = dy = 1e-3
    Sc = 0.95
    dt = Sc * dx / c

    Ez = np.zeros((Nx, Ny))
    Hx = np.zeros((Nx, Ny - 1))
    Hy = np.zeros((Nx - 1, Ny))

    K_mur = (c * dt - dx) / (c * dt + dx)

    cx, cy = Nx // 2, Ny // 2
    tau = 20 * dt
    n0 = 6 * tau / dt

    Nt = 400

    for n in range(Nt):
        # Hx update
        for i in range(Nx):
            for j in range(Ny - 1):
                Hx[i, j] += Sc * (Ez[i, j] - Ez[i, j+1])

        # Hy update
        for i in range(Nx - 1):
            for j in range(Ny):
                Hy[i, j] += Sc * (Ez[i+1, j] - Ez[i, j])

        # Ez update
        for i in range(1, Nx - 1):
            for j in range(1, Ny - 1):
                Ez[i, j] += Sc * (Hy[i, j] - Hy[i-1, j] - Hx[i, j] + Hx[i, j-1])

        # Soft source
        gaussian = np.exp(-((n - n0) / (tau/dt))**2)
        if n < n0 + 3 * tau/dt:
            Ez[cx, cy] += gaussian

        # Mur 1st-order ABC at boundaries
        Ez[0, :] = Ez[1, :] + K_mur * (Ez[0, :] - Ez[1, :])
        Ez[-1, :] = Ez[-2, :] + K_mur * (Ez[-1, :] - Ez[-2, :])
        Ez[:, 0] = Ez[:, 1] + K_mur * (Ez[:, 0] - Ez[:, 1])
        Ez[:, -1] = Ez[:, -2] + K_mur * (Ez[:, -1] - Ez[:, -2])

    # Plot final snapshot
    fig, ax = plt.subplots(figsize=(7, 6))
    extent = [0, Ny*dy*1e3, 0, Nx*dx*1e3]
    im = ax.imshow(Ez.T, extent=extent, origin='lower', cmap='RdBu_r', vmin=-0.3, vmax=0.3)
    plt.colorbar(im, ax=ax, label='E_z (V/m)')
    ax.set_xlabel("y (mm)")
    ax.set_ylabel("x (mm)")
    ax.set_title("2D TMz: Point Source with Mur ABC (n=400)")
    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch6_ex3_mur_2d.png", dpi=150)
    plt.close()
    print("[Ch6 Ex3] 2D Mur ABC plotted.")


if __name__ == "__main__":
    example_6_1_mur_1d()
    example_6_2_mur_reflection_vs_angle()
    example_6_3_mur_2d_point_source()
