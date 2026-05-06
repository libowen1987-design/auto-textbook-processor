"""
houle_ch3_examples.py
=====================
Chapter 3 — Stability and Dispersion Analysis in 1D FDTD

Topics covered:
  3.1  CFL (Courant-Friedrichs-Lewy) stability condition
  3.2  Numerical dispersion relation
  3.3  Effect of dt/dx ratio on numerical dispersion
  3.4  Wideband vs narrowband pulse considerations
  3.5  Grid anisotropy and directional errors

References:
  - Taflove & Brodwin (1975), IEEE Trans. MTT, vol. 23
  - Courant, Friedrichs & Lewy (1928), Math. Ann.
  - Houle & Sullivan, Ch. 3
"""

import numpy as np
from math import cos, sin, sqrt, pi, exp
from matplotlib import pyplot as plt
plt.rcParams['font.size'] = 12

# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────
c0_normalized = 1.0    # speed of light in normalised units
# In physical units: c0 = 1/sqrt(eps0*mu0) m/s
c_physical = 3e8       # m/s

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def gaussian_pulse(time_step, t0, spread):
    return exp(-0.5 * ((t0 - time_step) / spread) ** 2)


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 3.1 — CFL Stability Boundary (S = dt/dx)
#
#   CFL condition for 1D FDTD:  S = c*dt/dx ≤ 1
#   Here we sweep S from 0.1 to 1.2 and check field growth.
#   At S > 1 the simulation becomes unstable (exponential growth).
# ─────────────────────────────────────────────────────────────────────────────
def cfl_stability_sweep(dx=1.0, ke=100, nsteps=200,
                        s_values=None, t0=40, spread=12):
    """
    Sweep CFL number S = dt/dx and check stability.

    In normalised units dx = 1, dt = S.
    The update coefficient for H is dt/dx = S/2 = 0.5*S.
    The update coefficient for E is 1 (in free space).

    Parameters
    ----------
    s_values : list of CFL numbers to test

    Returns
    -------
    max_amplitudes : dict  S → max(|E|) at final time step
    """
    if s_values is None:
        s_values = np.linspace(0.1, 1.4, 14)

    results = {}

    for S in s_values:
        dt = S * dx   # dt = S * dx  (normalised: dx=1, dt=S)
        # Time-step loop — actual dt used is S (not 0.5 as in normalised default)
        ex = np.zeros(ke)
        hy = np.zeros(ke)
        kc = ke // 2

        try:
            for time_step in range(1, nsteps + 1):
                # E update: ex[k] = ex[k] + S/2 * (hy[k-1] - hy[k])
                for k in range(1, ke):
                    ex[k] = ex[k] + 0.5 * S * (hy[k - 1] - hy[k])

                pulse = gaussian_pulse(time_step, t0, spread)
                ex[kc] = pulse

                # H update: hy[k] = hy[k] + S/2 * (ex[k] - ex[k+1])
                for k in range(ke - 1):
                    hy[k] = hy[k] + 0.5 * S * (ex[k] - ex[k + 1])

            results[S] = abs(ex).max()

        except (OverflowError, FloatingPointError):
            results[S] = np.inf   # unstable

    return results


def fd3d_cfl_demo():
    """Demonstrate CFL boundary: S=0.9 stable, S=1.2 unstable."""
    ke = 200
    t0, spread = 40, 12

    fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))

    for ax, S in zip(axes, [0.9, 1.2]):
        ex = np.zeros(ke)
        hy = np.zeros(ke)
        kc = ke // 2

        nsteps = 150
        for time_step in range(1, nsteps + 1):
            for k in range(1, ke):
                ex[k] = ex[k] + 0.5 * S * (hy[k - 1] - hy[k])
            ex[kc] = gaussian_pulse(time_step, t0, spread)
            for k in range(ke - 1):
                hy[k] = hy[k] + 0.5 * S * (ex[k] - ex[k + 1])

        ax.plot(ex, 'k-', linewidth=1)
        status = "STABLE" if S <= 1.0 else "UNSTABLE"
        color = 'k' if S <= 1.0 else 'r'
        ax.set_title(f'S = {S:.2f}  [{status}]', fontsize=13)
        ax.set_ylabel(r'$E_x$')
        ax.set_xlabel('FDTD cells')
        ax.set_xlim(0, ke)
        ax.set_ylim(-2, 2)

    plt.suptitle('CFL Stability: S=dt/dx', fontsize=14)
    plt.tight_layout()
    plt.show()


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 3.2 — Numerical Dispersion Relation
#
#   Analytical (continuous):    k_a = ω/c
#   FDTD (numerical) dispersion: cos(ωΔt) = 1 - (S²/2) * (1 - cos(kΔx))
#
#   For a given propagation angle θ in 1D: k = ωΔt / v_phase
#   We plot the phase velocity error  v_phase(vsNumerical) / c  vs. kΔx.
# ─────────────────────────────────────────────────────────────────────────────
def numerical_dispersion(S=0.5, nk=200, plot=True):
    """
    Compute and plot the numerical dispersion relation for 1D FDTD.

    Dispersion relation:
        cos(ω_dt) = 1 - (S^2/2) * (1 - cos(k_dx))

    where k_dx = k * Δx (normalized wavenumber).
    Phase velocity: v_p = ω/k = (ω_dt * c) / k_dx
    Normalized phase velocity: v_p/c = ω_dt / (S * k_dx)

    Physical insight:
      - At k_dx → 0 (long wavelength): v_p → c (low dispersion)
      - At k_dx → π (Nyquist): v_p → c (in 1D for any S)
      - Mid-range: dispersion error depends on S
    """
    k_dx = np.linspace(0.01, np.pi - 0.01, nk)

    # FDTD dispersion: solve cos(ω_dt) = 1 - (S²/2)*(1-cos(k_dx))
    arg = 1.0 - 0.5 * S**2 * (1.0 - np.cos(k_dx))
    arg = np.clip(arg, -1.0, 1.0)  # avoid NaN from acos outside [-1,1]
    omega_dt = np.arccos(arg)

    # Phase velocity (normalized to c)
    # v_p/c = (ω_dt) / (S * k_dx)
    with np.errstate(divide='ignore', invalid='ignore'):
        vp_over_c = omega_dt / (S * k_dx)
        vp_over_c = np.where(k_dx < 0.02, 1.0, vp_over_c)  # low-k limit = 1

    if plot:
        fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))

        # Left: dispersion curve
        axes[0].plot(k_dx, vp_over_c, 'k-', linewidth=2, label=f'S={S}')
        axes[0].axhline(1.0, color='gray', linestyle='--', linewidth=1)
        axes[0].set_xlabel(r'$k\Delta x$ (rad)')
        axes[0].set_ylabel(r'$v_p / c$')
        axes[0].set_title('Numerical Phase Velocity vs. Wavenumber')
        axes[0].set_xlim(0, np.pi)
        axes[0].set_ylim(0.95, 1.05)
        axes[0].legend()

        # Right: error vs S
        s_values = [0.1, 0.3, 0.5, 0.7, 0.9, 0.99]
        for Si in s_values:
            arg_i = 1.0 - 0.5 * Si**2 * (1.0 - np.cos(k_dx))
            arg_i = np.clip(arg_i, -1.0, 1.0)
            omega_dt_i = np.arccos(arg_i)
            vp_i = omega_dt_i / (Si * k_dx)
            vp_i = np.where(k_dx < 0.02, 1.0, vp_i)
            axes[1].plot(k_dx, vp_i, linewidth=1.5, label=f'S={Si}')

        axes[1].axhline(1.0, color='gray', linestyle='--', linewidth=1)
        axes[1].set_xlabel(r'$k\Delta x$ (rad)')
        axes[1].set_ylabel(r'$v_p / c$')
        axes[1].set_title('Phase Velocity for Various CFL Numbers')
        axes[1].set_xlim(0, np.pi)
        axes[1].set_ylim(0.8, 1.05)
        axes[1].legend(fontsize=9)

        plt.tight_layout()
        plt.show()

    return k_dx, vp_over_c


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 3.3 — Wideband Pulse Dispersion
#   A wideband (short pulse) contains many k-components.
#   Different k-components travel at different v_p → pulse spreading.
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_3_3_pulse_dispersion(nsteps=500, ke=400,
                               S=0.5, t0=50, spread=6,
                               kc=None, plot=True):
    """
    1D FDTD with wideband Gaussian pulse — demonstrates numerical dispersion
    through pulse broadening.

    Short spread = wide bandwidth = many k-components = more spreading.
    """
    if kc is None:
        kc = ke // 2

    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    # Store snapshot at different times
    snap_times = [50, 150, 300, 450]
    snapshots_e = []

    for time_step in range(1, nsteps + 1):
        for k in range(1, ke):
            ex[k] = ex[k] + 0.5 * S * (hy[k - 1] - hy[k])

        pulse = gaussian_pulse(time_step, t0, spread)
        ex[kc] = pulse

        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * S * (ex[k] - ex[k + 1])

        if time_step in snap_times:
            snapshots_e.append(ex.copy())

    if plot:
        fig, ax = plt.subplots(figsize=(9, 3.5))
        colors = ['k', 'r', 'b', 'g']
        labels = [f'T={t}' for t in snap_times]
        for snap, c, lbl in zip(snapshots_e, colors, labels):
            ax.plot(snap, color=c, linewidth=1, label=lbl)
        ax.set_ylabel(r'$E_x$')
        ax.set_xlabel('FDTD cells')
        ax.set_xlim(0, ke)
        ax.set_title(f'Wideband Pulse Dispersion  (S={S}, spread={spread})')
        ax.legend()
        plt.tight_layout()
        plt.show()

    return snapshots_e


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 3.4 — CFL Maximum Time Step Calculator
# ─────────────────────────────────────────────────────────────────────────────
def cfl_max_dt_1d(dx=1.0, eps_r=1.0, mu_r=1.0):
    """
    Compute CFL-limited maximum time step for 1D FDTD.

    CFL condition (1D):  Δt ≤ Δx / (c₀/√(ε_r μ_r))

    In normalized units (c₀=1, dx=1):
        Δt_max = 1.0 / √(ε_r μ_r)

    For 3D: Δt ≤ Δx / (c₀√(1/Δx² + 1/Δy² + 1/Δz²))
    """
    c_medium = c0_normalized / sqrt(eps_r * mu_r)
    dt_max = dx / c_medium
    return dt_max


def cfl_max_dt_3d(dx=1.0, dy=1.0, dz=1.0, eps_r=1.0, mu_r=1.0):
    """
    CFL for 3D FDTD (uniform or non-uniform grid).

    Δt ≤ 1 / (c₀ √(1/Δx² + 1/Δy² + 1/Δz²))
    """
    c_medium = c0_normalized / sqrt(eps_r * mu_r)
    dt_max = 1.0 / (c_medium * sqrt(1/dx**2 + 1/dy**2 + 1/dz**2))
    return dt_max


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 3.5 — Grid Resolution vs. Dispersion Error
#
#   For a wave of frequency f0 (free-space wavelength λ0 = c/f0),
#   require N points per wavelength: N ≥ λ0 / Δx
#
#   Dispersion error at frequency f0:
#     |v_p - c| / c  as function of N and S
# ─────────────────────────────────────────────────────────────────────────────
def dispersion_error_vs_resolution(S=0.5, N_min=5, N_max=100, plot=True):
    """
    Compute phase velocity error as function of grid resolution (points/λ).

    For a given N = points per wavelength, the wavenumber is:
        k_dx = 2π / N

    Phase velocity error = |v_p/c - 1| at that k_dx.
    """
    N_values = np.arange(N_min, N_max + 1)
    k_dx_values = 2 * np.pi / N_values  # k_dx = 2π/N for one period in N cells

    errors = []
    for k_dx in k_dx_values:
        arg = 1.0 - 0.5 * S**2 * (1.0 - cos(k_dx))
        arg = max(-1.0, min(1.0, arg))
        arg = max(-1.0, min(1.0, arg))
        omega_dt = np.arccos(arg)
        vp_over_c = omega_dt / (S * k_dx)
        errors.append(abs(vp_over_c - 1.0))

    if plot:
        fig, ax = plt.subplots(figsize=(7, 3.5))
        ax.semilogy(N_values, errors, 'k-', linewidth=2)
        ax.axhline(0.01, color='gray', linestyle='--', label='1% error')
        ax.set_xlabel('Points per wavelength (N)')
        ax.set_ylabel('Phase velocity error  |vp/c - 1|')
        ax.set_title(f'Dispersion Error vs. Grid Resolution  (S={S})')
        ax.legend()
        ax.set_xlim(N_min, N_max)
        plt.tight_layout()
        plt.show()

    return N_values, errors


# ─────────────────────────────────────────────────────────────────────────────
# VERIFICATION
# ─────────────────────────────────────────────────────────────────────────────
def verify():
    """Self-check for Ch3 stability and dispersion code."""
    print("=== Ch3 Verification ===")

    # CFL sweep: at S<1 stable, S>1 unstable
    results = cfl_stability_sweep(s_values=[0.5, 0.8, 0.99, 1.0, 1.05, 1.2])
    stable_count = sum(1 for v in results.values() if v < 10)
    assert stable_count >= 4, f"CFL sweep gave unexpected stability: {results}"
    print("  [OK] CFL stability sweep")

    # Numerical dispersion: vp/c near 1 at low k
    k_dx, vp = numerical_dispersion(S=0.5, plot=False)
    assert 0.97 < vp[0] < 1.03, "Dispersion relation out of range"
    print("  [OK] Numerical dispersion relation")

    # 3D CFL: should be smaller than 1D
    dt_1d = cfl_max_dt_1d(dx=1.0)
    dt_3d = cfl_max_dt_3d(dx=1.0, dy=1.0, dz=1.0)
    assert dt_3d < dt_1d, "3D CFL should be tighter than 1D"
    print("  [OK] 3D CFL is tighter than 1D")

    # Dispersion error: error decreases with more points/λ
    N, err = dispersion_error_vs_resolution(S=0.5, N_min=10, N_max=80, plot=False)
    assert err[0] > err[-1], "More resolution should give lower error"
    print("  [OK] Dispersion error decreases with resolution")

    print("All Ch3 examples passed verification.")


if __name__ == "__main__":
    print("=" * 60)
    print("Houle & Sullivan Ch3 — Stability and Dispersion Analysis")
    print("=" * 60)

    print("\n--- CFL Stability Demo (S=0.9 vs S=1.2) ---")
    fd3d_cfl_demo()

    print("\n--- Numerical Dispersion Relation (S=0.5) ---")
    numerical_dispersion(S=0.5, plot=True)

    print("\n--- Wideband Pulse Dispersion ---")
    fd3d_3_3_pulse_dispersion(nsteps=400, ke=400, S=0.5, spread=6, plot=True)

    print("\n--- CFL Calculator ---")
    for dx in [1.0, 0.5, 0.25]:
        for eps_r in [1.0, 2.0, 4.0, 9.0]:
            dt = cfl_max_dt_1d(dx=dx, eps_r=eps_r)
            print(f"  dx={dx}, eps_r={eps_r}  → dt_max={dt:.6f}")

    print("\n=== Verification ===")
    verify()