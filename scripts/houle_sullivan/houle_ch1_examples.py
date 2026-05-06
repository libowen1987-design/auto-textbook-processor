"""
houle_ch1_examples.py
=====================
Chapter 1 — 1D FDTD: Free Space, Dielectric, Lossy Media, ABC, CFL Stability

References:
  - Houle & Sullivan, "Electromagnetic Simulation Using the FDTD Method
    with Python", 3rd ed., Ch. 1 (IEEE Press, 2020)
  - Yee (1966), "Numerical solution of initial boundary value problems
    involving Maxwell's equations in isotropic media",
    IEEE Trans. Antennas Propag., vol. 17, pp. 585-589.
  - Taflove & Brodwin (1975), IEEE Trans. Microwave Theory Tech., vol. 23.
  - Mur (1981), IEEE Trans. Electromagn. Compat., vol. 23, pp. 377-384.
  - Cheng (1992), "Field and Wave Electromagnetics", Addison-Wesley.

Dependencies: numpy, matplotlib
"""

import numpy as np
from math import exp
from matplotlib import pyplot as plt
plt.rcParams['font.size'] = 12

# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTS (normalized units: c = 1, eps0 = mu0 = 1)
# ─────────────────────────────────────────────────────────────────────────────
# In normalized units c = 1, so dx = dt. The CFL stability condition
# requires  dt ≤ dx  (i.e. max_stability_factor = 1.0).
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 1.1  fd3d_1_1.py  — Free-space 1D FDTD (Gaussian pulse)
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_1_1(nsteps: int = 100, ke: int = 200,
             kc: int = None, t0: int = 40, spread: float = 12,
             plot: bool = True):
    """
    1D FDTD simulation in free space with a Gaussian pulse source.

    Parameters
    ----------
    nsteps : int   Number of time steps to run.
    ke     : int   Number of FDTD cells (spatial grid size).
    kc     : int   Source position (grid centre if None).
    t0     : int   Centre time index of Gaussian pulse.
    spread : float  Spread parameter (σ) of Gaussian pulse.
    plot   : bool  Whether to display matplotlib output.
    """
    if kc is None:
        kc = ke // 2

    # Field arrays
    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    for time_step in range(1, nsteps + 1):
        # Update Ex (E field on grid nodes k = 1 .. ke-1)
        for k in range(1, ke):
            ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])

        # Inject Gaussian pulse at the centre cell
        pulse = exp(-0.5 * ((t0 - time_step) / spread) ** 2)
        ex[kc] = pulse

        # Update Hy (H field on half-integer positions k = 0 .. ke-2)
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 3.5), sharex=True)
        axes[0].plot(ex, color='k', linewidth=1)
        axes[0].set_ylabel(r'$E_x$', fontsize=14)
        axes[0].set_xticks(np.arange(0, ke + 1, step=20))
        axes[0].set_xlim(0, ke)
        axes[0].set_ylim(-1.2, 1.2)
        axes[0].text(ke / 2, 0.5, f'T = {nsteps}', ha='center')

        axes[1].plot(hy, color='k', linewidth=1)
        axes[1].set_ylabel(r'$H_y$', fontsize=14)
        axes[1].set_xlabel('FDTD cells')
        axes[1].set_xticks(np.arange(0, ke + 1, step=20))
        axes[1].set_xlim(0, ke)
        axes[1].set_ylim(-1.2, 1.2)

        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 1.2  fd3d_1_2.py  — Free-space 1D FDTD with Absorbing Boundary
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_1_2(nsteps: int = 250, ke: int = 200,
             kc: int = None, t0: int = 40, spread: float = 12,
             plot: bool = True):
    """
    1D FDTD in free space with first-order absorbing boundary condition (ABC)
    at both ends.  Mur (1981) first-order ABC:
        ∂E/∂t + c·∂E/∂z = 0   (forward wave)
        ∂E/∂t - c·∂E/∂z = 0   (backward wave)
    """
    if kc is None:
        kc = ke // 2

    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    # ABC coefficients (first-order, c = 1 in normalized units)
    abc_low  = np.zeros(2)   # [prev_ex, prev_hy] at z=0 boundary
    abc_high = np.zeros(2)   # [prev_ex, prev_hy] at z=max boundary

    for time_step in range(1, nsteps + 1):
        # Update Ex interior
        for k in range(1, ke):
            ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])

        # Inject Gaussian pulse
        pulse = exp(-0.5 * ((t0 - time_step) / spread) ** 2)
        ex[kc] = pulse

        # Update Hy interior
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

        # First-order ABC — left boundary (z=0, k=0)
        # Forward-traveling wave: ex[0] = ex_prev + (c*dt-dx)/(c*dt+dx)*(ex[0]-ex_prev)
        # In normalized units c=1, dx=dt → coefficient = 0
        # So ex[0] = ex_prev (perfect first-order ABC)
        ex[0]    = abc_low[0]
        abc_low[0] = ex[1]

        # Right boundary (z=max, k=ke-1)
        ex[ke-1] = abc_high[0]
        abc_high[0] = ex[ke - 2]

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 3.5), sharex=True)
        axes[0].plot(ex, color='k', linewidth=1)
        axes[0].set_ylabel(r'$E_x$', fontsize=14)
        axes[0].set_xticks(np.arange(0, ke + 1, step=20))
        axes[0].set_xlim(0, ke)
        axes[0].set_ylim(-1.2, 1.2)
        axes[0].text(ke / 2, 0.5, f'T = {nsteps}', ha='center')

        axes[1].plot(hy, color='k', linewidth=1)
        axes[1].set_ylabel(r'$H_y$', fontsize=14)
        axes[1].set_xlabel('FDTD cells')
        axes[1].set_xticks(np.arange(0, ke + 1, step=20))
        axes[1].set_xlim(0, ke)
        axes[1].set_ylim(-1.2, 1.2)

        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 1.3  fd3d_1_3.py  — Propagation in a dielectric medium (eps_r)
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_1_3(nsteps: int = 250, ke: int = 200,
             epsilon_r: float = 2.0,
             kc: int = None, t0: int = 40, spread: float = 12,
             plot: bool = True):
    """
    1D FDTD in a homogeneous dielectric medium with permittivity epsilon_r.

    In a dielectric, the update coefficients change:
        Ex[k] = Ex[k] + (dt/eps_k) * (Hy[k-1] - Hy[k]) / dx
             = Ex[k] + (1/eps_r) * (Hy[k-1] - Hy[k])   [normalized units]

    Wave speed in dielectric:  c_dielectric = 1/sqrt(eps_r)
    Wavelength in dielectric: λ_dielectric = λ_0 / sqrt(eps_r)
    """
    if kc is None:
        kc = ke // 2

    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    # dielectric relative permittivity (scalar, homogeneous)
    # eps_r = 1.0 → free space (c = 1)
    inv_eps_r = 1.0 / epsilon_r

    for time_step in range(1, nsteps + 1):
        # Update Ex with dielectric coefficient
        for k in range(1, ke):
            ex[k] = ex[k] + inv_eps_r * (hy[k - 1] - hy[k])

        # Gaussian source at centre
        pulse = exp(-0.5 * ((t0 - time_step) / spread) ** 2)
        ex[kc] = pulse

        # Update Hy
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 3.5), sharex=True)
        axes[0].plot(ex, color='k', linewidth=1)
        axes[0].set_ylabel(r'$E_x$', fontsize=14)
        axes[0].set_xticks(np.arange(0, ke + 1, step=20))
        axes[0].set_xlim(0, ke)
        axes[0].set_ylim(-1.2, 1.2)
        axes[0].text(ke / 2, 0.5, rf'$\epsilon_r$ = {epsilon_r}', ha='center')
        axes[0].set_title(f'T = {nsteps}')

        axes[1].plot(hy, color='k', linewidth=1)
        axes[1].set_ylabel(r'$H_y$', fontsize=14)
        axes[1].set_xlabel('FDTD cells')
        axes[1].set_xticks(np.arange(0, ke + 1, step=20))
        axes[1].set_xlim(0, ke)
        axes[1].set_ylim(-1.2, 1.2)

        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 1.4  fd3d_1_4.py  — Propagation in a lossy dielectric (sigma)
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_1_4(nsteps: int = 250, ke: int = 200,
             epsilon_r: float = 1.0,
             sigma: float = 0.01,
             kc: int = None, t0: int = 40, spread: float = 12,
             plot: bool = True):
    """
    1D FDTD in a lossy dielectric medium (conductivity σ).

    Maxwell's equations with conductivity:
        ∂E/∂t = (1/ε)·∇×H - (σ/ε)·E

    FDTD update for Ex:
        ex[k]_new = decay * ex[k]_old + (1/eps_r) * (hy[k-1] - hy[k])

    where  decay = exp(-sigma * dt / eps0)

    Physical interpretation:
      - σ > 0 → wave attenuates as it propagates
      - Loss tangent: tan(δ) = σ / (ω·ε)
    """
    if kc is None:
        kc = ke // 2

    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    inv_eps_r = 1.0 / epsilon_r
    # Loss decay per time step (dt = dx = 1 in normalized units)
    decay = exp(-sigma)

    for time_step in range(1, nsteps + 1):
        # Update Ex with loss
        for k in range(1, ke):
            ex[k] = decay * ex[k] + inv_eps_r * (hy[k - 1] - hy[k])

        # Gaussian pulse source
        pulse = exp(-0.5 * ((t0 - time_step) / spread) ** 2)
        ex[kc] = pulse

        # Update Hy
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 3.5), sharex=True)
        axes[0].plot(ex, color='k', linewidth=1)
        axes[0].set_ylabel(r'$E_x$', fontsize=14)
        axes[0].set_xticks(np.arange(0, ke + 1, step=20))
        axes[0].set_xlim(0, ke)
        axes[0].text(ke / 2, 0.3, rf'$\epsilon_r$={epsilon_r}, $\sigma$={sigma}', ha='center')
        axes[0].set_title(f'T = {nsteps}')

        axes[1].plot(hy, color='k', linewidth=1)
        axes[1].set_ylabel(r'$H_y$', fontsize=14)
        axes[1].set_xlabel('FDTD cells')
        axes[1].set_xticks(np.arange(0, ke + 1, step=20))
        axes[1].set_xlim(0, ke)

        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# CFL STABILITY CONDITION
# ─────────────────────────────────────────────────────────────────────────────
def cfl_max_dt(dx: float = 1.0, eps_r: float = 1.0, mu_r: float = 1.0) -> float:
    """
    Compute maximum stable time step (CFL condition) for 1D FDTD.

    CFL (Courant–Friedrichs–Lewy) stability criterion:
        c₀ = 1 / √(ε₀·μ₀)   [normalized: c₀ = 1]
        Δt ≤ Δx / (c₀ / √(ε_r·μ_r))

    In normalized units (c₀ = 1):
        Δt_max = Δx / √(ε_r·μ_r) = 1 / √(ε_r·μ_r)   [since Δx = 1]

    Parameters
    ----------
    dx     : float  Spatial cell size (normalized Δx = 1 by convention)
    eps_r  : float  Relative permittivity of medium
    mu_r   : float  Relative permeability of medium

    Returns
    -------
    dt_max : float  Maximum stable time step

    Example
    -------
    >>> cfl_max_dt(dx=0.5, eps_r=2.0)
    0.3535533905932738
    """
    c_normalized = 1.0 / np.sqrt(eps_r * mu_r)   # wave speed in medium
    dt_max = dx / c_normalized
    return dt_max


# ─────────────────────────────────────────────────────────────────────────────
# RUN DEMOS
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print("Houle & Sullivan Ch1 — 1D FDTD Demo Suite")
    print("=" * 60)

    print("\n--- Program 1.1: Free-space 1D FDTD ---")
    fd3d_1_1(nsteps=100, ke=200, t0=40, spread=12, plot=False)
    print("Done. (set plot=True to display figures)")

    print("\n--- CFL Stability Check ---")
    for eps_r in [1.0, 2.0, 4.0, 9.0]:
        dt_max = cfl_max_dt(dx=1.0, eps_r=eps_r)
        print(f"  ε_r = {eps_r:4.1f}  →  Δt_max = {dt_max:.6f}  "
              f"(speed = {1/np.sqrt(eps_r):.4f} c₀)")

    print("\n--- Program 1.3: Dielectric propagation (ε_r=2.0) ---")
    fd3d_1_3(nsteps=250, ke=200, epsilon_r=2.0, t0=40, spread=12, plot=False)
    print("Done.")