#!/usr/bin/env python3
"""
Jackson Classical Electrodynamics (3rd Ed) — Ch13–Ch16 Examples
==============================================================

Numerical demonstrations of key formulas from Chapters 13–16:

  1. Charged particle energy loss (Bethe-Bloch)
  2. Radiation fields of a moving charge (Lienard-Wiechert)
  3. Bremsstrahlung spectrum
  4. Radiation damping simulation (Abraham-Lorentz)

Dependencies: numpy, scipy, matplotlib
"""

import numpy as np
from scipy.constants import (e, m_e, m_p, c, epsilon_0, pi, hbar)
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ---------------------------------------------------------------------------
# Physical constants (SI units)
# ---------------------------------------------------------------------------
r_e = e**2 / (4 * pi * epsilon_0 * m_e * c**2)  # classical electron radius [m]
N_A = 6.02214076e23                               # Avogadro's number [1/mol]


# ===========================================================================
# EXAMPLE 1: Bethe-Bloch Stopping Power
# ===========================================================================

def bethe_bloch(material="Si", projectile="p", T_MeV=1.0):
    """
    Compute stopping power −dE/dx [MeV/cm] using the relativistic Bethe-Bloch
    formula (Jackson §13.2).

    Parameters
    ----------
    material : str
        'Si' (silicon), 'Pb' (lead), 'H2O' (water), 'Ar' (argon gas)
    projectile : str
        'p' (proton), 'alpha' (alpha particle), 'mu' (muon), 'pi' (pion)
    T_MeV : float
        Kinetic energy of projectile in MeV.

    Returns
    -------
    dict with keys: dedx_MeV_per_cm, beta, gamma, beta_gamma
    """
    # --- Material properties (Z, A [g/mol], density rho [g/cm^3], I [eV]) ---
    materials = {
        "Si":   {"Z": 14, "A": 28.09, "rho": 2.329, "I": 173.0},
        "Pb":   {"Z": 82, "A": 207.2, "rho": 11.34, "I": 823.0},
        "H2O":  {"Z": 10, "A": 18.015, "rho": 1.000, "I": 75.0},
        "Ar":   {"Z": 18, "A": 39.95, "rho": 0.001782, "I": 188.0},
    }
    if material not in materials:
        raise ValueError(f"Unknown material '{material}'")
    mat = materials[material]

    # --- Projectile masses [MeV/c^2] ---
    masses = {
        "p":    938.272,
        "alpha": 3727.379,   # ~4 * 938.272 — binding ~28 MeV
        "mu":   105.658,
        "pi":   139.570,
    }
    if projectile not in masses:
        raise ValueError(f"Unknown projectile '{projectile}'")
    M_MeV = masses[projectile]

    # --- Projectile charge (in units of e) ---
    z = {"p": 1, "alpha": 2, "mu": 1, "pi": 1}[projectile]

    # Kinematics
    gamma = 1.0 + T_MeV / M_MeV
    beta = np.sqrt(1.0 - 1.0 / gamma**2)
    bg = beta * gamma

    # Maximum energy transfer to a free electron (§13.1)
    # T_max = 2 m_e c^2 bg^2 / (1 + 2 gamma m_e/M + (m_e/M)^2)
    r = m_e * c**2 / (M_MeV * 1e6)  # m_e c^2 in J divided by M in J, but using MeV:
    # Actually let's work in MeV consistently.
    m_e_MeV = 0.511
    T_max = (2.0 * m_e_MeV * bg**2
             / (1.0 + 2.0 * gamma * m_e_MeV / M_MeV + (m_e_MeV / M_MeV)**2))

    # Bethe-Bloch constant K [MeV cm^2 mol^-1]
    # K = 4 pi N_A r_e^2 m_e c^2
    # r_e must be in cm: r_e (m) * 100
    r_e_cm = r_e * 100.0
    K_MeV = (4 * pi * N_A * r_e_cm**2 * m_e * c**2) / 1.602176634e-13

    # The formula:
    # −dE/dx = K * z^2 * Z/A * rho * [ ... ]   [MeV/cm]
    # (K is in MeV cm^2/g, rho in g/cm^3, so −dE/dx in MeV/cm)
    bracket = 0.5 * np.log(2.0 * m_e_MeV * c**2 * bg**2 * T_max
                           / (mat["I"]**2)) - beta**2

    # Density effect δ (Fermi plateau) — simplified parametrization
    # Rough estimate: δ ≈ ln(bg^2) + ln(I/(hbar ω_p)) - 1 for bg ≫ 1
    # ℏω_p ≈ 28.816 * sqrt(rho * Z/A) eV  (plasma energy)
    hbar_wp_eV = 28.816 * np.sqrt(mat["rho"] * mat["Z"] / mat["A"])  # eV
    if bg > 1.0:
        delta = np.log(bg**2) + np.log(mat["I"] / hbar_wp_eV) - 1.0
        delta = max(0.0, delta)
    else:
        delta = 0.0
    bracket -= 0.5 * delta

    # Final stopping power
    dedx = K_MeV * z**2 * mat["Z"] / mat["A"] * mat["rho"] / beta**2 * bracket

    return {
        "dedx": dedx,
        "dedx_label": f"−dE/dx = {dedx:.3f} MeV/cm",
        "beta": beta,
        "gamma": gamma,
        "bg": bg,
        "T_max_MeV": T_max,
        "material": material,
        "projectile": projectile,
        "T_MeV": T_MeV,
    }


def plot_bethe_bloch():
    """Plot stopping power vs. kinetic energy for several materials."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # --- Panel (a): proton in Si, H2O, Pb ---
    ax = axes[0]
    T_range = np.logspace(-2, 4, 300)  # 0.01 MeV to 10 GeV
    for mat, color, ls in zip(["Si", "H2O", "Pb"], ["C0", "C1", "C2"], ["-", "--", ":"]):
        dedx = []
        for T in T_range:
            result = bethe_bloch(material=mat, projectile="p", T_MeV=T)
            dedx.append(result["dedx"])
        ax.loglog(T_range, dedx, color=color, ls=ls, label=mat)
    ax.set_xlabel("Kinetic energy T [MeV]")
    ax.set_ylabel("−dE/dx [MeV/cm]")
    ax.set_title("Bethe-Bloch: proton in various materials")
    ax.legend()
    ax.grid(True, which="both", alpha=0.3)

    # --- Panel (b): different projectiles in Si ---
    ax = axes[1]
    for proj, color, ls in zip(["p", "alpha", "mu"], ["C0", "C3", "C4"],
                                ["-", "-.", ":"]):
        dedx = []
        for T in T_range:
            result = bethe_bloch(material="Si", projectile=proj, T_MeV=T)
            dedx.append(result["dedx"])
        ax.loglog(T_range, dedx, color=color, ls=ls,
                  label=f"{'proton' if proj=='p' else proj}")
    ax.set_xlabel("Kinetic energy T [MeV]")
    ax.set_ylabel("−dE/dx [MeV/cm]")
    ax.set_title("Bethe-Bloch: various projectiles in Si")
    ax.legend()
    ax.grid(True, which="both", alpha=0.3)

    fig.tight_layout()
    # fig.savefig("bethe_bloch.pdf")
    plt.show()
    print("[Example 1] Bethe-Bloch plot generated.\n")


# ===========================================================================
# EXAMPLE 2: Lienard-Wiechert Radiation Fields
# ===========================================================================

def lw_radiation_field(q, v0, a0, t_obs, obs_pos, gamma=2.0):
    """
    Compute the Lienard-Wiechert radiation (acceleration) field at one
    observation point for a simplified scenario:
      - Particle at origin at retarded time t_ret = 0
      - Velocity v = v0 * x̂, acceleration a = a0 * x̂ (collinear case)
      - Particle moves relativistically with given gamma

    This computes E_rad (the 1/R term) using Jackson §14.2.

    Parameters
    ----------
    q : float         Charge [C]
    v0 : float        Speed at retarded time, in units of c (beta)
    a0 : float        Acceleration at retarded time [m/s^2]
    t_obs : float     Observation time [s] — not directly used for the
                      instantaneous field (we compute field at one instant)
    obs_pos : ndarray Observation position [x, y, z] in meters
    gamma : float     Lorentz factor

    Returns
    -------
    E_rad : ndarray   Radiation electric field vector [V/m] at obs_pos
    B_rad : ndarray   Radiation magnetic field vector [T]
    n_hat : ndarray   Unit vector in direction of observation from source
    """
    beta_vec = np.array([v0, 0.0, 0.0], dtype=float)
    beta_dot_vec = np.array([a0 / c, 0.0, 0.0], dtype=float)  # β̇ [1/s]

    pos_ret = np.zeros(3)  # particle at origin at retarded time

    R_vec = obs_pos - pos_ret
    R = np.linalg.norm(R_vec)
    n_hat = R_vec / R

    beta_dot_n = np.dot(beta_dot_vec, n_hat)  # β̇·n
    beta_n = np.dot(beta_vec, n_hat)          # β·n
    denom = 1.0 - beta_n

    # Safety check — if denom ≈ 0 (observation directly along v), clip
    if abs(denom) < 1e-12:
        denom = np.sign(denom) * 1e-12
    denom_sq = denom**2

    # Acceleration (radiation) field: E ∝ n × [(n − β) × β̇] / (1 − β·n)^3
    # Jackson Eq. (14.14)
    n_minus_beta = n_hat - beta_vec
    cross1 = np.cross(n_minus_beta, beta_dot_vec)  # (n − β) × β̇
    cross2 = np.cross(n_hat, cross1)               # n × (...)

    prefactor = q / (4 * pi * epsilon_0 * c) * 1.0 / (R * denom**3)
    E_rad = prefactor * cross2

    # B = n × E / c
    B_rad = np.cross(n_hat, E_rad) / c

    return E_rad, B_rad, n_hat


def field_map_2d(q, v0, a0, gamma, obs_distance=1e-6):
    """
    Compute and display the 2D radiation field pattern in the x–y plane.

    Uses non-relativistic Larmor dipole pattern for simplicity when β ≪ 1,
    or the beaming pattern of §14.6 for β → 1.
    """
    # Create a grid of observation points in the x-y plane
    nx = 40
    angles = np.linspace(0, 2 * pi, nx, endpoint=False)
    # observation radius
    r_obs = obs_distance  # meters

    Ex_grid = np.zeros(nx)
    Ey_grid = np.zeros(nx)
    E_mag_grid = np.zeros(nx)

    for i, theta in enumerate(angles):
        obs = np.array([r_obs * np.cos(theta), r_obs * np.sin(theta), 0.0])
        E, B, n = lw_radiation_field(
            q, v0, a0, t_obs=0.0, obs_pos=obs, gamma=gamma
        )
        Ex_grid[i] = E[0]
        Ey_grid[i] = E[1]
        E_mag_grid[i] = np.linalg.norm(E)

    # Normalize
    E_max = E_mag_grid.max() if E_mag_grid.max() > 0 else 1.0
    E_norm = E_mag_grid / E_max

    # Polar plot
    fig, ax = plt.subplots(1, 2, figsize=(12, 5),
                           subplot_kw={'projection': 'polar'})

    # Panel (a): collinear v ∥ a
    ax[0].plot(angles, E_norm, 'b-', lw=2)
    ax[0].fill(angles, E_norm, alpha=0.2)
    ax[0].set_title(f"v ∥ a, β = {v0:.2f}, γ = {gamma:.1f}",
                    va='bottom')
    ax[0].set_ylim(0, 1.1)

    # Panel (b): perpendicular acceleration (v ⟂ a)
    # For v ⟂ a, use the transverse formula from Jackson §14.3
    # Angular distribution dP/dΩ ∝ [1 - (β·n)² sin²θ cos²φ / (1-β·n)³] ...
    # Simplified: P ∝ |n × (n × β̇)|² / (1-β·n)^5
    E_perp_norm = np.zeros(nx)
    beta = v0
    for i, theta in enumerate(angles):
        n = np.array([np.cos(theta), np.sin(theta), 0.0])
        beta_vec = np.array([beta, 0.0, 0.0])
        beta_dot = np.array([0.0, a0 / c, 0.0])  # ⟂ to v
        num = np.cross(n, np.cross(n, beta_dot))
        denom = (1.0 - np.dot(beta_vec, n))
        if abs(denom) < 1e-14:
            denom = 1e-14
        val = np.linalg.norm(num) / denom**3
        E_perp_norm[i] = val
    E_perp_norm /= E_perp_norm.max() if E_perp_norm.max() > 0 else 1.0

    ax[1].plot(angles, E_perp_norm, 'r-', lw=2)
    ax[1].fill(angles, E_perp_norm, alpha=0.2)
    ax[1].set_title(f"v ⟂ a, β = {beta:.2f}, γ = {gamma:.1f}",
                    va='bottom')
    ax[1].set_ylim(0, 1.1)

    fig.tight_layout()
    plt.show()
    print("[Example 2] Lienard-Wiechert radiation pattern plotted.\n")


# ===========================================================================
# EXAMPLE 3: Bremsstrahlung Spectrum
# ===========================================================================

def bethe_heitler_cross_section(E_eV, omega_eV, Z=82, screening="complete"):
    """
    Differential cross section dσ/dω for bremsstrahlung (Bethe-Heitler)
    for an electron of energy E (eV) radiating a photon of energy ħω (eV)
    in a Coulomb field of a nucleus with charge Ze.

    Jackson §15.2.

    Parameters
    ----------
    E_eV : float      Incident electron total energy [eV] (kinetic + rest)
    omega_eV : float  Photon energy [eV]
    Z : int           Nuclear charge of target
    screening : str   "none", "complete", or "intermediate"

    Returns
    -------
    dsigma_domega : Differential cross section [cm² / (eV/s)]
    """
    # Constants
    r_e_cm = r_e * 100  # classical electron radius in cm
    alpha_f = e**2 / (4 * pi * epsilon_0 * hbar * c)  # fine structure
    m_e_eV = m_e * c**2 / e  # electron rest mass [eV]

    # Kinematics
    E1 = E_eV
    E2 = E1 - omega_eV  # outgoing electron total energy
    if E2 <= m_e_eV:
        return 0.0  # below threshold

    gamma1 = E1 / m_e_eV
    gamma2 = E2 / m_e_eV

    p1c = np.sqrt(E1**2 - m_e_eV**2)  # p c in eV
    p2c = np.sqrt(E2**2 - m_e_eV**2)

    # Bethe-Heitler unscreened (Jackson Eq. 15.5 in modern form)
    # dσ = 4 α_f Z² r_e² dω/ω (p2/p1) [ ... ]
    # For extreme relativistic: p2/p1 ≈ E2/E1

    # Screening variable: ξ = 100 m_e c² ħω / (E1 E2 Z^{1/3})
    xi = 100.0 * m_e_eV * omega_eV / (E1 * E2 * Z**(1/3))

    # Bethe-Heitler factor
    factor_p = 1.0 + (E2 / E1)**2 - (2.0 / 3.0) * (E2 / E1)

    if screening == "none" or xi > 1e3:
        # Unscreened Bethe-Heitler logarithm
        L = np.log(2.0 * E1 * E2 / (m_e_eV * omega_eV)) - 0.5
    elif screening == "complete" or xi < 1e-3:
        # Complete screening
        L = np.log(183.0 / Z**(1/3)) - 0.0  # f(Z) omitted for simplicity
    else:
        # Intermediate (approximate interpolation)
        L_uns = np.log(2.0 * E1 * E2 / (m_e_eV * omega_eV)) - 0.5
        L_scr = np.log(183.0 / Z**(1/3))
        # Smooth step
        w = np.exp(-xi)
        L = w * L_scr + (1 - w) * L_uns

    # dσ/dω = 4 α Z² r_e² / ω * factor_p * L
    dsigma_domega = (4.0 * alpha_f * Z**2 * r_e_cm**2
                     / omega_eV * factor_p * L)

    # Convert to per-hbar: dσ/d(ħω) = (1/ħ) dσ/dω
    # We keep units in per-eV (assuming ħω in eV)
    # Actually the formula is per d(ħω), so we need factor 1 in eV^{-1}
    # Already normalized per unit ħω.

    return max(0.0, dsigma_domega)


def plot_bremsstrahlung_spectrum():
    """Plot bremsstrahlung cross section for several electron energies."""
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    m_e_eV = m_e * c**2 / e
    energies_MeV = [10, 50, 100, 500]  # MeV

    for E_MeV in energies_MeV:
        E_eV = E_MeV * 1e6
        omega_max = E_eV - m_e_eV  # max photon energy
        if omega_max <= 0:
            continue
        # Logarithmic grid in photon energy
        n_points = 200
        omega = np.logspace(
            np.log10(0.001 * omega_max),
            np.log10(0.95 * omega_max),
            n_points
        )
        dsigma = np.array([
            bethe_heitler_cross_section(E_eV, w, Z=82) for w in omega
        ])

        # Energy-weighted spectrum: ω dσ/dω (dimensionless)
        omega_dsigma = omega * dsigma

        ax.loglog(omega / 1e6, omega_dsigma,
                  label=f"E$_e$ = {E_MeV} MeV, Z=Pb")

    ax.set_xlabel("Photon energy ℏω [MeV]")
    ax.set_ylabel("ω dσ/dω [cm²/eV · eV = cm²]")
    ax.set_title("Bremsstrahlung spectrum (Bethe-Heitler, complete screening)")
    ax.legend()
    ax.grid(True, which="both", alpha=0.3)

    # Add annotation about characteristic shape
    ax.text(0.98, 0.15,
            "Flat ω dσ/dω → 1/ω spectrum\n"
            "at low ω (infrared divergence)\n"
            "Cutoff near E$_e$ − m$_e$c²",
            transform=ax.transAxes, ha="right", va="bottom",
            bbox=dict(facecolor="white", alpha=0.8))

    fig.tight_layout()
    plt.show()
    print("[Example 3] Bremsstrahlung spectrum plotted.\n")


# ===========================================================================
# EXAMPLE 4: Radiation Damping Simulation
# ===========================================================================

def damped_oscillator_with_radiation(t, y, omega0, tau0):
    """
    ODE system for a 1D damped harmonic oscillator with Abraham-Lorentz
    radiation reaction (§16.2, §16.6).

    The AL equation is: qdd + omega0^2 q = tau0 * qdddot
    where τ0 = 2/3 * r_e / c ≈ 6.2×10^(-24) s for an electron.

    Using the "reduced" Landau trick: replace qdddot ≈ -omega0^2 qdot,
    valid when τ0 << 1/omega0 (weak damping).

    State vector y = [x, v]  →  dy/dt = [v, -omega0^2 x - gamma_eff v]
    """
    x, v = y
    # Reduced Abraham-Lorentz: gamma_eff = tau0 * omega0^2
    gamma_eff = tau0 * omega0**2
    a = -omega0**2 * x - gamma_eff * v
    return [v, a]


def full_ald_oscillator(t, y, omega0, tau0):
    """
    3rd-order Abraham-Lorentz-Dirac equation for a harmonic oscillator:
    dx/dt = v
    dv/dt = a
    da/dt = (a + omega0^2 x) / tau0    [from a = -omega0^2 x + tau0 * dddx]

    WARNING: This is the full (unreduced) AL equation and exhibits
    runaway solutions. Used here to illustrate the pathology.
    """
    x, v, a = y
    # From: m a = -m omega0^2 x + m tau0 * dddx
    # → dddx = (a + omega0^2 x) / tau0
    dddx = (a + omega0**2 * x) / tau0
    return [v, a, dddx]


def plot_radiation_damping():
    """
    Compare:
      (a) Underdamped classical oscillator (no radiation)
      (b) Reduced Abraham-Lorentz (physical damping)
      (c) Full ALD equation (runaway)
    """
    # Parameters
    # Use optical frequency: λ = 500 nm → ω0 ≈ 3.77×10^15 rad/s
    lambda_nm = 500.0
    omega0 = 2 * pi * c / (lambda_nm * 1e-9)  # [rad/s]
    period = 2 * pi / omega0
    tau0 = 2.0 / 3.0 * r_e / c  # ≈ 6.24×10^(-24) s

    # Classical damping constant
    Gamma = tau0 * omega0**2
    decay_time = 1.0 / Gamma

    print(f"  ω0 = {omega0:.3e} rad/s")
    print(f"  T0 = {period:.3e} s")
    print(f"  τ0 = {tau0:.3e} s")
    print(f"  Γ  = {Gamma:.3e} rad/s")
    print(f"  τ_decay = {decay_time:.3e} s ≈ {decay_time*1e9:.3f} ns")

    # --- (a) Underdamped oscillator vs. (b) radiation-damped oscillator ---

    # Time window: a few periods + show damping
    t_max = min(5 * period, 20 * decay_time)
    n_points = 2000
    t_span = (0, t_max)
    t_eval = np.linspace(0, t_max, n_points)

    # Initial conditions: x(0) = x0, v(0) = 0
    x0 = 1e-10  # 1 Å initial displacement

    # Undamped
    def undamped_ode(t, y):
        x, v = y
        return [v, -omega0**2 * x]

    sol_und = solve_ivp(undamped_ode, t_span, [x0, 0.0],
                         t_eval=t_eval, method="RK45", rtol=1e-9, atol=1e-12)

    # Radiation-damped (reduced AL)
    sol_damped = solve_ivp(damped_oscillator_with_radiation,
                           t_span, [x0, 0.0],
                           args=(omega0, tau0),
                           t_eval=t_eval, method="RK45", rtol=1e-9, atol=1e-12)

    # --- (c) Full ALD (note: this is pathological) ---
    # Reduced time window to see runaway
    t_runaway_max = min(1.5 * period, 10 * tau0 * 1e10)  # adjusted
    t_ra = np.linspace(0, t_runaway_max, 500)
    sol_ald = solve_ivp(full_ald_oscillator, (0, t_runaway_max),
                         [x0, 0.0, 0.0],  # x0, v0=0, a0=0
                         args=(omega0, tau0),
                         t_eval=t_ra, method="RK45", rtol=1e-9, atol=1e-12)

    # ---- Plot ----
    fig, axes = plt.subplots(2, 2, figsize=(14, 8))

    # (a) Undamped
    ax = axes[0, 0]
    ax.plot(sol_und.t * 1e15, sol_und.y[0] * 1e10, 'b-')
    ax.set_xlabel("Time [fs]")
    ax.set_ylabel("x [Å]")
    ax.set_title("(a) Undamped oscillator (no radiation)")
    ax.grid(alpha=0.3)

    # (b) Damped (reduced AL)
    ax = axes[0, 1]
    ax.plot(sol_damped.t * 1e15, sol_damped.y[0] * 1e10, 'r-',
            label=f"Γ = {Gamma:.2e} rad/s")
    # Exponential envelope
    env = x0 * np.exp(-0.5 * Gamma * sol_damped.t) * 1e10
    ax.plot(sol_damped.t * 1e15, env, 'k--', alpha=0.5, label="envelope")
    ax.plot(sol_damped.t * 1e15, -env, 'k--', alpha=0.5)
    ax.set_xlabel("Time [fs]")
    ax.set_ylabel("x [Å]")
    ax.set_title("(b) Radiation-damped (reduced AL)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (c) Full ALD — show runaway
    ax = axes[1, 0]
    x_ald = sol_ald.y[0] * 1e10
    # Clamp for plotting
    x_ald_plot = np.clip(x_ald, -10 * x0 * 1e10, 10 * x0 * 1e10)
    ax.plot(sol_ald.t * 1e15, x_ald_plot, 'g-')
    ax.set_xlabel("Time [fs]")
    ax.set_ylabel("x [Å]")
    ax.set_title("(c) Full ALD equation (runaway!)")
    ax.axhline(y=0, color="gray", ls=":", lw=0.5)
    if np.any(np.abs(x_ald) > 10 * x0 * 1e10):
        ax.text(0.95, 0.9, "⚠ Runaway", transform=ax.transAxes,
                ha="right", color="red", fontweight="bold")
    ax.grid(alpha=0.3)

    # (d) Lorenzian line shape
    ax = axes[1, 1]
    dw = omega0 * 0.2
    omega_range = np.linspace(omega0 - dw, omega0 + dw, 500)
    lorentz = (Gamma / (2 * pi)
               / ((omega_range - omega0)**2 + (Gamma / 2)**2))
    lorentz /= lorentz.max()
    ax.plot(omega_range / omega0 - 1, lorentz, 'm-', lw=2)
    ax.axvline(x=0, color='gray', ls=':', alpha=0.5)
    ax.set_xlabel("(ω − ω₀) / ω₀")
    ax.set_ylabel("Normalized intensity")
    ax.set_title("(d) Natural line shape (Lorentzian)")
    ax.set_xlim(-0.1, 0.1)
    ax.grid(alpha=0.3)

    fig.suptitle("Radiation Damping: Classical Electron Oscillator",
                 fontsize=14)
    fig.tight_layout()
    plt.show()
    print("[Example 4] Radiation damping simulation complete.\n")


# ===========================================================================
# MAIN
# ===========================================================================

if __name__ == "__main__":
    print("=" * 72)
    print("Jackson Ch13–Ch16: Numerical Examples")
    print("=" * 72)
    print()

    # ---- Example 0: Table of stopping powers ----
    print("[Example 0] Bethe-Bloch stopping power at selected energies")
    print("-" * 72)
    for proj in ["p", "α", "μ"]:
        for mat in ["Si", "Pb"]:
            for T in [1.0, 10.0, 100.0, 1000.0]:
                r = bethe_bloch(material=mat, projectile="p" if proj != "α" else "alpha",
                                T_MeV=T)
                print(f"  {proj:3s} in {mat:3s} @ T={T:8.1f} MeV:  "
                      f"−dE/dx = {r['dedx']:10.3f} MeV/cm  "
                      f"(βγ={r['bg']:.1f})")
    print()

    # ---- Example 1: Bethe-Bloch plot ----
    print("[Example 1] Plotting Bethe-Bloch curves...")
    plot_bethe_bloch()

    # ---- Example 2: Lienard-Wiechert radiation fields ----
    print("[Example 2] Lienard-Wiechert radiation fields...")
    q = 1.6e-19  # unit charge
    v_beta = 0.8
    a_val = 1e16  # m/s^2
    E_rad, B_rad, n_hat = lw_radiation_field(
        q, v_beta, a_val, t_obs=0.0, obs_pos=np.array([1e-6, 1e-6, 0.0]),
        gamma=1.0 / np.sqrt(1 - v_beta**2)
    )
    print(f"  At r=(1,1,0) µm:")
    print(f"    E_rad = ({E_rad[0]:.3e}, {E_rad[1]:.3e}, {E_rad[2]:.3e}) V/m")
    print(f"    |E_rad| = {np.linalg.norm(E_rad):.3e} V/m")
    # Radiation pattern
    field_map_2d(q, v_beta, a_val, gamma=2.0)
    field_map_2d(q, v_beta, a_val, gamma=5.0)

    # ---- Example 3: Bremsstrahlung ----
    print("[Example 3] Bremsstrahlung...")
    plot_bremsstrahlung_spectrum()

    # ---- Example 4: Radiation damping ----
    print("[Example 4] Radiation damping...")
    plot_radiation_damping()

    print("=" * 72)
    print("All examples complete.")
    print("=" * 72)
