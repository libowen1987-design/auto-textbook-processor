#!/usr/bin/env python3
"""
taflove_ch1_examples.py
Taflove FDTD 3rd Ed. — Chapter 1: Electrodynamics Entering the 21st Century

Three example scripts demonstrating core FDTD concepts:
  1. 1D FDTD simulation — Gaussian pulse propagation in free space
  2. CFL stability condition — stable vs. unstable time-step comparison
  3. Yee lattice visualization — sketch of the 1D staggered grid
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")  # headless
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0

# ============================================================
# Example 1.1: 1D FDTD — Gaussian Pulse Propagation
# ============================================================
def example_1d_fdtd_gaussian():
    """
    Simulate a Gaussian pulse propagating in a 1D free-space FDTD grid.
    Uses the Yee leapfrog scheme for the 1D wave equation (Ez-Hy formulation).
    Mur's first-order ABC at both ends.
    """
    Nz = 400                     # number of spatial cells
    Lz = 1.0                     # domain length [m]
    dz = Lz / Nz                 # cell size
    # CFL number = 0.95 (stable)
    Sc = 0.95                    # Courant number S_c = c * dt / dz
    dt = Sc * dz / c             # time step

    # Field arrays (staggered: Ez at integer nodes, Hy at half-integer nodes)
    Ez = np.zeros(Nz)
    Hy = np.zeros(Nz - 1)

    # Mur's first-order ABC coefficient
    K = (c * dt - dz) / (c * dt + dz)

    # Source parameters
    source_pos = Nz // 4         # pulse center index
    tau = 40 * dt                # pulse width (1/e half-width)
    t0 = 6 * tau                 # time offset for smooth turn-on

    # Storage for snapshots
    snap_times = [0, 100, 200, 300, 400]
    snap_Ez = {}

    Nt = 550
    for n in range(Nt):
        # --- Update H-field (Hy) from E-field (Ez) ---
        # Hy[k] += (c*dt/dz) * (Ez[k+1] - Ez[k])
        for k in range(Nz - 1):
            Hy[k] += Sc * (Ez[k + 1] - Ez[k])

        # --- Update E-field (Ez) from H-field (Hy) ---
        # Ez[k] += (c*dt/dz) * (Hy[k] - Hy[k-1])
        # except at boundaries
        for k in range(1, Nz - 1):
            Ez[k] += Sc * (Hy[k] - Hy[k - 1])

        # --- Hard source ---
        pulse = np.exp(-((n * dt - t0) / tau) ** 2)
        Ez[source_pos] = pulse

        # --- Mur ABC @ left boundary ---
        Ez[0] = Ez[1] + K * (Ez[0] - Ez[1])
        # --- Mur ABC @ right boundary ---
        Ez[-1] = Ez[-2] + K * (Ez[-1] - Ez[-2])

        # Record snapshots
        if n in snap_times:
            snap_Ez[n] = Ez.copy()

    # --- Plotting ---
    fig, axes = plt.subplots(2, 1, figsize=(10, 7))

    ax = axes[0]
    z_axis = np.arange(Nz) * dz * 100  # convert to cm
    for n in snap_times:
        ax.plot(z_axis, snap_Ez[n], label=f"t = {n * dt * 1e9:.1f} ns")
    ax.set_xlabel("z [cm]")
    ax.set_ylabel("E_z [V/m]")
    ax.set_title("1D FDTD: Gaussian Pulse Propagation (Mur ABC)")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Time evolution at a single point
    ax2 = axes[1]
    probe_z = Nz // 2
    Ez_probe = np.zeros(Nt)
    # Re-run for probe
    Ez_p = np.zeros(Nz)
    Hy_p = np.zeros(Nz - 1)
    for n in range(Nt):
        for k in range(Nz - 1):
            Hy_p[k] += Sc * (Ez_p[k + 1] - Ez_p[k])
        for k in range(1, Nz - 1):
            Ez_p[k] += Sc * (Hy_p[k] - Hy_p[k - 1])
        pulse = np.exp(-((n * dt - t0) / tau) ** 2)
        Ez_p[source_pos] = pulse
        Ez_p[0] = Ez_p[1] + K * (Ez_p[0] - Ez_p[1])
        Ez_p[-1] = Ez_p[-2] + K * (Ez_p[-1] - Ez_p[-2])
        Ez_probe[n] = Ez_p[probe_z]

    ax2.plot(np.arange(Nt) * dt * 1e9, Ez_probe)
    ax2.set_xlabel("Time [ns]")
    ax2.set_ylabel("E_z at z=50 cm [V/m]")
    ax2.set_title(f"Time Waveform at Probe (z={probe_z * dz * 100:.1f} cm)")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(
        "/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch1_ex1_gaussian_pulse.png",
        dpi=150,
    )
    plt.close(fig)
    print("[Ch1 Ex1] 1D FDTD Gaussian pulse — figure saved.")
    return


# ============================================================
# Example 1.2: CFL Stability Condition — Stable vs. Unstable
# ============================================================
def example_cfl_stability():
    """
    Compare three Courant numbers:
      Sc = 0.5  (stable, conservative)
      Sc = 0.95 (stable, near limit)
      Sc = 1.2  (unstable, violates CFL)
    CFL condition for 1D FDTD: Sc = c*dt/dz <= 1.
    """
    Nz = 200
    Lz = 1.0
    dz = Lz / Nz
    source_pos = Nz // 4
    tau_steps = 30
    t0_steps = 6 * tau_steps

    Sc_values = [0.5, 0.95, 1.2]
    labels = [r"$S_c = 0.5$ (stable)", r"$S_c = 0.95$ (stable)", r"$S_c = 1.2$ (UNSTABLE)"]
    colors = ["blue", "green", "red"]
    Nt_max = 300

    results = {}
    for Sc, lbl, clr in zip(Sc_values, labels, colors):
        dt = Sc * dz / c
        Ez = np.zeros(Nz)
        Hy = np.zeros(Nz - 1)
        K = (c * dt - dz) / (c * dt + dz) if Sc <= 1 else 0
        Ez_energy = []

        for n in range(Nt_max):
            for k in range(Nz - 1):
                Hy[k] += Sc * (Ez[k + 1] - Ez[k])
            for k in range(1, Nz - 1):
                Ez[k] += Sc * (Hy[k] - Hy[k - 1])
            pulse = np.exp(-((n - t0_steps) / tau_steps) ** 2)
            Ez[source_pos] = pulse
            if Sc <= 0.99:
                Ez[0] = Ez[1] + K * (Ez[0] - Ez[1])
                Ez[-1] = Ez[-2] + K * (Ez[-1] - Ez[-2])

            # Total field energy (sum of squares)
            Ez_energy.append(np.sum(Ez ** 2) * dz)

        results[Sc] = {
            "Ez_final": Ez.copy(),
            "energy": np.array(Ez_energy),
            "label": lbl,
            "color": clr,
            "dt": dt,
        }

    # --- Plotting ---
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Spatial profile at final time
    ax = axes[0]
    z_axis = np.arange(Nz) * dz * 100
    for Sc_val in Sc_values:
        r = results[Sc_val]
        ax.plot(z_axis, r["Ez_final"], label=r["label"], color=r["color"], alpha=0.8)
    ax.set_xlabel("z [cm]")
    ax.set_ylabel("E_z [V/m]")
    ax.set_title(f"Field Profile at t = {Nt_max * dt * 1e9:.1f} ns (or diverged)")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Energy evolution
    ax = axes[1]
    for Sc_val in Sc_values:
        r = results[Sc_val]
        time_ns = np.arange(Nt_max) * r["dt"] * 1e9
        energy_db = 10 * np.log10(r["energy"] / (r["energy"][0] + 1e-30))
        ax.plot(time_ns, energy_db, label=r["label"], color=r["color"], alpha=0.8)
    ax.set_xlabel("Time [ns]")
    ax.set_ylabel("Total Field Energy [dB (rel. to initial)]")
    ax.set_title("Total Field Energy Evolution")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-40, 40)

    plt.tight_layout()
    fig.savefig(
        "/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch1_ex2_cfl_stability.png",
        dpi=150,
    )
    plt.close(fig)
    print("[Ch1 Ex2] CFL stability comparison — figure saved.")
    return


# ============================================================
# Example 1.3: Yee Lattice Concept Visualization
# ============================================================
def example_yee_lattice():
    """
    Create a schematic of the 1D Yee staggered grid showing the
    relative positions of E_z and H_y fields and the leapfrog
    time-stepping relationship.
    """
    fig, axes = plt.subplots(2, 1, figsize=(10, 6))

    # --- Space grid ---
    ax = axes[0]
    N_show = 6
    z_idx = np.arange(N_show)
    dz = 1.0

    # E_z at integer nodes
    ax.plot(z_idx * dz, np.zeros(N_show), "o", markersize=14,
            color="tab:blue", label=r"$E_z$ nodes (integer $i\Delta z$)")
    # H_y at half-integer nodes
    hy_z = np.arange(N_show - 1) + 0.5
    ax.plot(hy_z * dz, np.zeros(N_show - 1), "s", markersize=14,
            color="tab:red", label=r"$H_y$ nodes (half-integer $(i+1/2)\Delta z$)")
    ax.set_xlim(-0.5, N_show - 0.5)
    ax.set_ylim(-0.3, 0.3)
    ax.set_xlabel("Spatial index $i$")
    ax.set_yticks([])
    ax.set_title("1D Yee Staggered Grid", fontsize=14)
    ax.legend(fontsize=10, loc="upper right")
    ax.grid(True, alpha=0.3)

    # Annotations: cell size
    ax.annotate("", xy=(0, 0.05), xytext=(1, 0.05),
                arrowprops=dict(arrowstyle="<->", lw=1.5))
    ax.text(0.5, 0.1, r"$\Delta z$", ha="center", fontsize=12)

    # Annotation: Ez-Hy relationship
    ax.annotate(
        r"$H_y|_{i+1/2}\leftarrow H_y|_{i+1/2} + \frac{c\Delta t}{\Delta z}(E_z|_{i+1} - E_z|_{i})$",
        xy=(1.5, -0.15), fontsize=9, ha="center",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow", alpha=0.8),
    )

    # --- Time grid (leapfrog) ---
    ax = axes[1]
    Nt_show = 5
    Nt_show_h = Nt_show - 1

    t_e = np.arange(Nt_show)  # E at integer time steps
    t_h = np.arange(Nt_show_h) + 0.5  # H at half-integer time steps

    ax.plot(t_e, np.zeros(Nt_show), "o", markersize=14,
            color="tab:blue", label=r"$E_z$ updates (integer $n\Delta t$)")
    ax.plot(t_h, np.zeros(Nt_show_h), "s", markersize=14,
            color="tab:red", label=r"$H_y$ updates ((n+1/2)$\Delta t$)")

    # Arrows showing the dependency
    for n in range(Nt_show_h):
        # E -> H
        ax.annotate("", xy=(t_e[n + 1], 0.05), xytext=(t_h[n], 0.05),
                    arrowprops=dict(arrowstyle="->", color="gray", lw=0.8, alpha=0.6))
        # H -> E
        ax.annotate("", xy=(t_h[n], -0.05), xytext=(t_e[n], -0.05),
                    arrowprops=dict(arrowstyle="->", color="gray", lw=0.8, alpha=0.6))

    ax.set_xlim(-0.5, Nt_show - 0.5)
    ax.set_ylim(-0.3, 0.3)
    ax.set_xlabel("Time step index $n$")
    ax.set_yticks([])
    ax.set_title("Leapfrog Time-Stepping", fontsize=14)
    ax.legend(fontsize=10, loc="upper right")
    ax.grid(True, alpha=0.3)

    # Annotation: CFL condition
    ax.annotate(
        r"CFL condition: $S_c = \frac{c\Delta t}{\Delta z} \leq 1$",
        xy=(2, -0.18), fontsize=10, ha="center",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.8),
    )

    plt.tight_layout()
    fig.savefig(
        "/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch1_ex3_yee_lattice.png",
        dpi=150,
    )
    plt.close(fig)
    print("[Ch1 Ex3] Yee lattice schematic — figure saved.")
    return


# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Taflove Ch.1 — FDTD Overview Examples")
    print("=" * 60)

    example_1d_fdtd_gaussian()
    example_cfl_stability()
    example_yee_lattice()

    print("=" * 60)
    print("All Ch.1 examples completed successfully.")
    print("=" * 60)
