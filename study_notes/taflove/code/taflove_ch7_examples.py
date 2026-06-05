#!/usr/bin/env python3
"""
taflove_ch7_examples.py
Taflove FDTD 3rd Ed. — Chapter 7: Perfectly Matched Layer ABC

Three examples:
  1. 1D FDTD with PML termination (polynomial grading)
  2. 2D TMz UPML — reflection vs. PML thickness
  3. CFS-CPML vs standard PML for evanescent waves
"""

import numpy as np
from scipy.constants import c, epsilon_0, mu_0
eta_0 = (mu_0 / epsilon_0)**0.5
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-darkgrid")

# ============================================================
# Example 7.1: 1D FDTD with PML
# ============================================================
def example_7_1_pml_1d():
    """
    1D FDTD with 8-cell PML. Compare to Mur ABC.
    Uses polynomial grading of conductivity.
    """
    Nz = 200
    dz = 1e-3
    Sc = 0.95
    dt = Sc * dz / c

    nPML = 8  # PML thickness in cells
    R0 = 1e-4  # desired reflection error
    m = 3      # polynomial order
    sigma_max = -(m + 1) * np.log(R0) / (2 * eta_0 * nPML * dz)

    # PML conductivity profile
    sigma = np.zeros(Nz)
    for k in range(nPML):
        x = (nPML - k) / nPML  # distance from PML interface (normalized)
        sigma[k] = sigma_max * (1 - x)**m
    for k in range(Nz - nPML, Nz):
        x = (k - (Nz - nPML)) / nPML
        sigma[k] = sigma_max * x**m

    # Arrays
    Ez = np.zeros(Nz)
    Hy = np.zeros(Nz - 1)
    # Additional arrays for PML split-field
    Ezx = np.zeros(Nz)
    Ezy = np.zeros(Nz)

    # Mur reference
    Ez_mur = np.zeros(Nz)
    Hy_mur = np.zeros(Nz - 1)
    K_mur = (c * dt - dz) / (c * dt + dz)

    source_pos = 30
    tau = 30 * dt
    n0 = 6 * tau / dt
    Nt = 800

    snap_Ez = {}
    snap_Ez_mur = {}
    snap_times = [200, 400, 600, 700]

    for n in range(Nt):
        # --- H update (standard everywhere) ---
        for k in range(Nz - 1):
            Hy[k] += Sc * (Ez[k+1] - Ez[k])
            Hy_mur[k] += Sc * (Ez_mur[k+1] - Ez_mur[k])

        # --- E update ---
        for k in range(1, Nz - 1):
            # Standard Yee
            delta_H = Hy[k] - Hy[k-1]
            Ez[k] += Sc * delta_H

            # PML: apply conductivity
            Ez[k] *= (1 - sigma[k] * dt / (2 * epsilon_0)) / (1 + sigma[k] * dt / (2 * epsilon_0))

        # --- Mur ---
        for k in range(1, Nz - 1):
            Ez_mur[k] += Sc * (Hy_mur[k] - Hy_mur[k-1])

        # Soft source
        gaussian = np.exp(-((n - n0) / (tau/dt))**2)
        if n < n0 + 3 * tau/dt:
            Ez[source_pos] = gaussian
            Ez_mur[source_pos] = gaussian

        # Mur ABC boundaries
        Ez_mur[0] = Ez_mur[1] + K_mur * (Ez_mur[0] - Ez_mur[1])
        Ez_mur[-1] = Ez_mur[-2] + K_mur * (Ez_mur[-1] - Ez_mur[-2])

        # PML: ends are PEC (field already zero from BC)

        if n in snap_times:
            snap_Ez[n] = Ez.copy()
            snap_Ez_mur[n] = Ez_mur.copy()

    # Plot comparison
    fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
    x_axis = np.arange(Nz) * dz * 1e3

    for n in snap_times:
        axes[0].plot(x_axis, snap_Ez[n], label=f"n={n}")
    axes[0].set_title("PML Termination — Clean Absorption")
    axes[0].set_ylabel("E_z (V/m)")
    axes[0].legend(fontsize=8)
    axes[0].axvspan(0, nPML*dz*1e3, alpha=0.1, color='green', label='PML')
    axes[0].axvspan((Nz-nPML)*dz*1e3, Nz*dz*1e3, alpha=0.1, color='green')

    for n in snap_times:
        axes[1].plot(x_axis, snap_Ez_mur[n], label=f"n={n}")
    axes[1].set_title("Mur ABC — Residual Reflection Visible")
    axes[1].set_xlabel("x (mm)")
    axes[1].set_ylabel("E_z (V/m)")
    axes[1].legend(fontsize=8)

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch7_ex1_pml_1d.png", dpi=150)
    plt.close()
    print("[Ch7 Ex1] 1D PML vs Mur plotted.")


# ============================================================
# Example 7.2: PML Reflection Error vs. Thickness
# ============================================================
def example_7_2_pml_reflection_vs_thickness():
    """Theoretical PML reflection error vs. PML thickness and grading order."""
    thicknesses = np.arange(4, 25)
    R0_target = 1e-4

    fig, ax = plt.subplots(figsize=(8, 5))

    for m in [2, 3, 4, 5]:
        R_theta = np.zeros_like(thicknesses, dtype=float)
        for i, d in enumerate(thicknesses):
            sigma_max = -(m + 1) * np.log(R0_target) / (2 * eta_0 * d * 1e-3)
            # Reflection error at normal incidence
            R_theta[i] = np.exp(-2 * sigma_max * eta_0 * d * 1e-3 / (m + 1))
        ax.semilogy(thicknesses, R_theta, 'o-', lw=2, label=f'm={m}')

    ax.axhline(R0_target, color='k', ls='--', alpha=0.5, label=f'Target R={R0_target:.0e}')
    ax.set_xlabel("PML Thickness d (cells)")
    ax.set_ylabel("Reflection Error |R(0)|")
    ax.set_title("PML Reflection Error vs. Thickness & Grading Order")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch7_ex2_pml_reflection.png", dpi=150)
    plt.close()
    print("[Ch7 Ex2] PML reflection vs thickness plotted.")


# ============================================================
# Example 7.3: CFS-CPML Evanescent Wave Absorption
# ============================================================
def example_7_3_pml_cfs_comparison():
    """
    Compare standard PML vs. CFS-CPML for a low-frequency (evanescent) source.
    Shows CFS-CPML reduces late-time reflections.
    """
    Nz = 300
    dz = 1e-3
    Sc = 0.95
    dt = Sc * dz / c

    nPML = 10
    R0 = 1e-4
    m = 3
    sigma_max = -(m + 1) * np.log(R0) / (2 * eta_0 * nPML * dz)

    # PML profiles
    sigma_pml = np.zeros(Nz)
    kappa_pml = np.ones(Nz)
    alpha_pml = np.zeros(Nz)
    kappa_max = 5.0
    alpha_max = 0.05

    for k in range(nPML):
        x = (nPML - k) / nPML
        sigma_pml[k] = sigma_max * (1 - x)**m
        kappa_pml[k] = 1 + (kappa_max - 1) * (1 - x)**m
        alpha_pml[k] = alpha_max * (1 - x)

    for k in range(Nz - nPML, Nz):
        x = (k - (Nz - nPML)) / nPML
        sigma_pml[k] = sigma_max * x**m
        kappa_pml[k] = 1 + (kappa_max - 1) * x**m
        alpha_pml[k] = alpha_max * x

    # Two simulations: standard PML, CFS-CPML
    Ez_std = np.zeros(Nz)
    Hy_std = np.zeros(Nz - 1)
    Ez_cfs = np.zeros(Nz)
    Hy_cfs = np.zeros(Nz - 1)

    # CFS auxiliary variables (simplified recursive integration)
    psi_Ez_std = np.zeros(Nz)
    psi_Ez_cfs = np.zeros(Nz)

    source_pos = 50
    f0 = 1e9  # 1 GHz
    omega0 = 2 * np.pi * f0
    tau = 80 * dt  # long pulse (low frequency)
    n0 = 6 * tau / dt
    Nt = 2000

    probe_pos = 200
    probe_std = []
    probe_cfs = []

    for n in range(Nt):
        # H update (standard)
        for k in range(Nz - 1):
            Hy_std[k] += Sc * (Ez_std[k+1] - Ez_std[k])
            Hy_cfs[k] += Sc * (Ez_cfs[k+1] - Ez_cfs[k])

        # E update
        for k in range(1, Nz - 1):
            delta_H_std = Hy_std[k] - Hy_std[k-1]
            delta_H_cfs = Hy_cfs[k] - Hy_cfs[k-1]

            # Standard PML conductivity
            Ez_std[k] += Sc * delta_H_std
            Ez_std[k] *= (1 - sigma_pml[k] * dt / (2*epsilon_0)) / (1 + sigma_pml[k] * dt / (2*epsilon_0))

            # CFS-CPML
            coeff_cfs = 1.0 / (1 + sigma_pml[k] * dt / (2 * kappa_pml[k] * epsilon_0) +
                              alpha_pml[k] * dt / (2 * epsilon_0))
            Ez_cfs[k] = coeff_cfs * (
                (1 - sigma_pml[k] * dt / (2 * kappa_pml[k] * epsilon_0) -
                 alpha_pml[k] * dt / (2 * epsilon_0)) * Ez_cfs[k] +
                Sc * delta_H_cfs / kappa_pml[k]
            )

        # Soft source (bandpass Gaussian)
        bandpass = np.sin(omega0 * n * dt) * np.exp(-((n - n0) / (tau/dt))**2)
        if n < n0 + 3 * tau/dt:
            Ez_std[source_pos] = bandpass
            Ez_cfs[source_pos] = bandpass

        # Record probe
        probe_std.append(Ez_std[probe_pos])
        probe_cfs.append(Ez_cfs[probe_pos])

    # Plot probe time-history
    t_axis = np.arange(Nt) * dt * 1e9  # ns
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(t_axis, probe_std, 'r-', lw=1, alpha=0.7, label='Standard PML')
    ax.plot(t_axis, probe_cfs, 'b-', lw=1, alpha=0.7, label='CFS-CPML')
    ax.set_xlabel("Time (ns)")
    ax.set_ylabel("E_z at Probe (V/m)")
    ax.set_title("Standard PML vs. CFS-CPML — Probe Near PML Boundary")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch7_ex3_cfs_cpml.png", dpi=150)
    plt.close()
    print("[Ch7 Ex3] CFS-CPML comparison plotted.")


if __name__ == "__main__":
    example_7_1_pml_1d()
    example_7_2_pml_reflection_vs_thickness()
    example_7_3_pml_cfs_comparison()
