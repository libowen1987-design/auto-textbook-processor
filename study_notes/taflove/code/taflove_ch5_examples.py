#!/usr/bin/env python3
"""
taflove_ch5_examples.py
Taflove FDTD 3rd Ed. — Chapter 5: Incident Wave Source Conditions

Three examples:
  1. Hard source retroreflection vs. soft source in 1D
  2. TF/SF plane-wave injection in 1D with scatterer
  3. 2D TF/SF plane wave incident on a dielectric cylinder
"""

import numpy as np
from scipy.constants import c, epsilon_0, mu_0
eta_0 = (mu_0 / epsilon_0)**0.5
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-darkgrid")

# ============================================================
# Example 5.1: Hard Source vs. Soft Source — Retroreflection
# ============================================================
def example_5_1_hard_vs_soft_source():
    """
    Compare hard source (Eq. 5.2) vs. soft source (revert to Yee after pulse)
    in a 1D FDTD simulation. Shows retroreflection artifact from hard source.
    """
    Nz = 400
    dz = 1e-3          # 1 mm cell size
    Sc = 0.95           # Courant number
    dt = Sc * dz / c

    # Source parameters
    source_pos = 100
    tau = 60 * dt       # Gaussian 1/e half-width
    n0 = 6 * tau / dt   # Gaussian center

    Ez_hard = np.zeros(Nz)
    Hy_hard = np.zeros(Nz - 1)
    Ez_soft = np.zeros(Nz)
    Hy_soft = np.zeros(Nz - 1)

    # Mur ABC coefficient
    K = (c * dt - dz) / (c * dt + dz)

    Nt = 1000
    snap_Ez_hard = {}
    snap_Ez_soft = {}
    snap_times = [200, 400, 600, 800]

    # PEC reflector at index 300
    pec_pos = 300

    for n in range(Nt):
        # --- H update ---
        for k in range(Nz - 1):
            Hy_hard[k] += Sc * (Ez_hard[k+1] - Ez_hard[k])
            Hy_soft[k] += Sc * (Ez_soft[k+1] - Ez_soft[k])

        # --- E update ---
        for k in range(1, Nz - 1):
            if k == pec_pos:
                Ez_hard[k] = 0.0
                Ez_soft[k] = 0.0
                continue
            Ez_hard[k] += Sc * (Hy_hard[k] - Hy_hard[k-1])
            Ez_soft[k] += Sc * (Hy_soft[k] - Hy_soft[k-1])

        # Hard source
        gaussian_val = np.exp(-((n - n0) / (tau/dt))**2)
        Ez_hard[source_pos] = gaussian_val

        # Soft source: inject then revert
        if n < n0 + 3 * tau/dt:
            Ez_soft[source_pos] = gaussian_val
        # else: normal Yee update already applied above

        # Mur ABC at boundaries
        for arr in [Ez_hard, Ez_soft]:
            arr[0] = arr[1] + K * (arr[0] - arr[1])
            arr[-1] = arr[-2] + K * (arr[-1] - arr[-2])

        if n in snap_times:
            snap_Ez_hard[n] = Ez_hard.copy()
            snap_Ez_soft[n] = Ez_soft.copy()

    # Plot
    fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
    x_axis = np.arange(Nz) * dz * 1e3  # mm

    for n in snap_times:
        label = f"n={n}"
        axes[0].plot(x_axis, snap_Ez_hard[n], label=label)
    axes[0].set_title("Hard Source — Note retroreflection at source point")
    axes[0].set_ylabel("E_z (V/m)")
    axes[0].legend(fontsize=8)
    axes[0].axvline(source_pos*dz*1e3, color='r', ls='--', alpha=0.4, label='Source')
    axes[0].axvline(pec_pos*dz*1e3, color='k', ls=':', alpha=0.4, label='PEC')
    axes[0].legend(fontsize=8)

    for n in snap_times:
        axes[1].plot(x_axis, snap_Ez_soft[n], label=f"n={n}")
    axes[1].set_title("Soft Source — Clean propagation, no retroreflection")
    axes[1].set_xlabel("x (mm)")
    axes[1].set_ylabel("E_z (V/m)")
    axes[1].legend(fontsize=8)
    axes[1].axvline(source_pos*dz*1e3, color='r', ls='--', alpha=0.4, label='Source')
    axes[1].axvline(pec_pos*dz*1e3, color='k', ls=':', alpha=0.4, label='PEC')

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch5_ex1_hard_vs_soft_source.png", dpi=150)
    plt.close()
    print("[Ch5 Ex1] Hard vs. soft source comparison plotted.")


# ============================================================
# Example 5.2: 1D TF/SF Formulation
# ============================================================
def example_5_2_tfsf_1d():
    """
    1D TF/SF simulation with a Gaussian plane wave injected via connecting surface.
    PEC slab at right acts as scatterer. Incident wave confined to total-field region.
    """
    Nz = 400
    dz = 1e-3
    Sc = 0.95
    dt = Sc * dz / c
    K_mur = (c * dt - dz) / (c * dt + dz)

    # Single-field arrays: Ez holds total-field on left, scattered-field on right
    Ez = np.zeros(Nz)
    Hy = np.zeros(Nz - 1)

    # TF/SF interface indices
    i0_left = 80    # start of TF region (incident wave enters here)
    i0_right = 300  # end of TF region (scattered field starts)

    # Incident wave parameters
    tau = 40.0 * dt
    n0 = 6.0 * tau / dt

    # PEC slab position
    pec_start = 250
    pec_end = 280

    Nt = 800
    snap_times = [100, 200, 300, 400, 500]
    snap_Ez = {}

    for n in range(Nt):
        # Incident field values at the connecting surfaces
        # Ez_inc at left interface (i0_left)
        inc_E = np.exp(-((n - n0) / (tau / dt))**2)
        # Hy_inc at left interface (i0_left + 0.5)
        inc_H = np.exp(-((n + 0.5 - n0) / (tau / dt))**2)

        # --- H update ---
        for k in range(Nz - 1):
            Hy[k] += Sc * (Ez[k+1] - Ez[k])

        # TF/SF correction for H at left interface
        # Hy(i0_left - 0.5) is in total-field region, uses Ez(i0_left) which is total
        # Hy(i0_left + 0.5) is in scattered-field region, corrected:
        # Add incident Ez: Hy(i0_left+0.5) += Sc * Ez_inc(i0_left)
        if i0_left < Nz - 1:
            Hy[i0_left] += Sc * inc_E

        # --- E update ---
        for k in range(1, Nz - 1):
            if pec_start <= k <= pec_end:
                Ez[k] = 0.0
                continue
            Ez[k] += Sc * (Hy[k] - Hy[k-1])

        # TF/SF correction for E at left interface
        # Ez(i0_left) is in total-field region, uses Hy(i0_left - 0.5) which is total
        # Ez(i0_left + 1) is in scattered-field region, corrected:
        # Add incident Hy at i0_left+0.5
        if i0_left + 1 < Nz:
            Ez[i0_left + 1] += Sc * inc_H

        # Mur ABC at boundaries
        Ez[0] = Ez[1] + K_mur * (Ez[0] - Ez[1])
        Ez[-1] = Ez[-2] + K_mur * (Ez[-1] - Ez[-2])

        if n in snap_times:
            snap_Ez[n] = Ez.copy()

    # Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    x_axis = np.arange(Nz) * dz * 1e3
    for n in snap_times:
        ax.plot(x_axis, snap_Ez[n], label=f"n={n}")
    ax.axvline(i0_left*dz*1e3, color='r', ls='--', alpha=0.5, label='TF/SF left interface')
    ax.axvline(i0_right*dz*1e3, color='g', ls='--', alpha=0.5, label='TF/SF right interface')
    ax.axvspan(pec_start*dz*1e3, pec_end*dz*1e3, alpha=0.2, color='black', label='PEC slab')
    ax.set_xlabel("x (mm)")
    ax.set_ylabel("E_z (V/m)")
    ax.set_title("1D TF/SF — Plane Wave Incident on PEC Slab")
    ax.legend(fontsize=8)
    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch5_ex2_tfsf_1d.png", dpi=150)
    plt.close()
    print("[Ch5 Ex2] 1D TF/SF example plotted.")


# ============================================================
# Example 5.3: 2D TF/SF — Plane Wave on Dielectric Cylinder
# ============================================================
def example_5_3_tfsf_2d_cylinder():
    """
    Simple 2D TMz FDTD with a total-field region containing a dielectric cylinder.
    Illustrates plane-wave injection via TF/SF interface.
    """
    Nx, Ny = 200, 200
    dx = dy = 1e-3     # 1 mm
    Sc = 0.95
    dt = Sc * dx / c

    # Material parameters
    epsilon_r_cylinder = 4.0
    cylinder_radius = 15 * dx
    cx, cy = Nx // 2, Ny // 2

    # Relative permittivity map
    eps_r = np.ones((Nx, Ny))
    for i in range(Nx):
        for j in range(Ny):
            if np.sqrt((i-cx)**2 + (j-cy)**2) < cylinder_radius / dx:
                eps_r[i, j] = epsilon_r_cylinder

    # TF/SF interface offset from boundaries (10 cells)
    margin = 10
    i0, i1 = margin, Nx - margin
    j0, j1 = margin, Ny - margin

    # Arrays (total-field interior, scattered-field exterior)
    Ez_tot = np.zeros((i1-i0+1, j1-j0+1))
    Ez_scat = np.zeros((Nx, Ny))  # scattered field everywhere
    # For simplicity, use single-field approach with correction injection

    # Use a single-field approach: total-field everywhere, inject at interface
    Ez = np.zeros((Nx, Ny))
    Hx = np.zeros((Nx, Ny - 1))
    Hy = np.zeros((Nx - 1, Ny))

    # Incident plane wave (Gaussian)
    tau = 30.0 * dt
    n0 = 6.0 * tau / dt

    Nt = 500
    source_frozen = None

    for n in range(Nt):
        # Incident field values
        inc = np.exp(-((n - n0) / (tau / dt))**2)
        # Use a simple 1D incident field propagating in +x direction
        # We inject at the left total-field boundary

        # --- Hx update ---
        for i in range(Nx):
            for j in range(Ny - 1):
                Hx[i, j] += Sc * (Ez[i, j] - Ez[i, j+1])

        # --- Hy update ---
        for i in range(Nx - 1):
            for j in range(Ny):
                Hy[i, j] += Sc * (Ez[i+1, j] - Ez[i, j])

        # --- Ez update (with material) ---
        for i in range(1, Nx - 1):
            for j in range(1, Ny - 1):
                # TF/SF correction: inject incident field at left interface
                correction = 0.0
                if i == i0 and j0 <= j <= j1:
                    # Left total-field boundary: add incident Hy
                    correction = Sc * inc * np.exp(-((j - Ny//2) / 30.0)**2)  # soft aperture
                if i == i1 and j0 <= j <= j1:
                    # Right interface: subtract incident Hy
                    correction = -Sc * inc * np.exp(-((j - Ny//2) / 30.0)**2)

                Ez[i, j] += (Sc / eps_r[i, j]) * (Hy[i, j] - Hy[i-1, j]
                                                   - Hx[i, j] + Hx[i, j-1]
                                                   + correction)

        # Mur ABC at outer boundaries (approximate)
        for i in range(Nx):
            Ez[i, 0] = Ez[i, 1] + (c*dt - dy)/(c*dt + dy) * (Ez[i, 0] - Ez[i, 1])
            Ez[i, -1] = Ez[i, -2] + (c*dt - dy)/(c*dt + dy) * (Ez[i, -1] - Ez[i, -2])
        for j in range(Ny):
            Ez[0, j] = Ez[1, j] + (c*dt - dx)/(c*dt + dx) * (Ez[0, j] - Ez[1, j])
            Ez[-1, j] = Ez[-2, j] + (c*dt - dx)/(c*dt + dx) * (Ez[-1, j] - Ez[-2, j])

        # Snapshot at n=400
        if n == 400:
            source_frozen = Ez.copy()

    # Plot
    fig, ax = plt.subplots(figsize=(8, 7))
    extent = [0, Ny*dy*1e3, 0, Nx*dx*1e3]
    im = ax.imshow(source_frozen.T, extent=extent, origin='lower',
                   cmap='RdBu_r', vmin=-0.5, vmax=0.5)
    plt.colorbar(im, ax=ax, label="E_z (V/m)")
    # Draw TF/SF interface
    ax.plot([j0*dy*1e3, j1*dy*1e3, j1*dy*1e3, j0*dy*1e3, j0*dy*1e3],
            [i0*dx*1e3, i0*dx*1e3, i1*dx*1e3, i1*dx*1e3, i0*dx*1e3],
            'g--', lw=1.5, label='TF/SF Interface')
    # Draw cylinder
    circle = plt.Circle((cy*dy*1e3, cx*dx*1e3), cylinder_radius*1e3,
                        fill=False, color='k', lw=2, ls='-', label='Dielectric')
    ax.add_patch(circle)
    ax.set_xlabel("y (mm)")
    ax.set_ylabel("x (mm)")
    ax.set_title("2D TF/SF: Plane Wave on Dielectric Cylinder ($\\epsilon_r=4$)")
    ax.legend()
    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch5_ex3_tfsf_2d_cylinder.png", dpi=150)
    plt.close()
    print("[Ch5 Ex3] 2D TF/SF cylinder example plotted.")


if __name__ == "__main__":
    example_5_1_hard_vs_soft_source()
    example_5_2_tfsf_1d()
    example_5_3_tfsf_2d_cylinder()
