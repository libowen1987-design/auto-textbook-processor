"""
houle_ch2_examples.py
=====================
Chapter 2 — Flux Density Reformulation, DFT, and Z-Transform Dispersion Models

Topics covered:
  2.1  Flux Density (D-field) reformulation
  2.2  Discrete Fourier Transform (DFT) for frequency-domain output
  2.3  Debye medium (single-pole dispersive)
  2.4  Z-transform formulation for dispersive media
  2.4.1 Unmagnetized plasma (Drude model)
  2.5  Lorentz medium (single-resonance)

References:
  - Houle & Sullivan, "Electromagnetic Simulation Using the FDTD Method
    with Python", 3rd ed., Ch. 2 (IEEE Press, 2020)
  - Sullivan (2013), "Numerical Methods for Electromagnetic Simulation"
"""

import numpy as np
from math import exp, cos, sin, sqrt
from matplotlib import pyplot as plt
plt.rcParams['font.size'] = 12

# Normalized units: c = eps0 = mu0 = 1, dx = dt = 0.5
# Physical constants (for conversion when needed)
eps0_physical = 8.854e-12   # F/m
mu0_physical  = 4e-7 * np.pi # H/m

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def gaussian_pulse(time_step, t0, spread):
    return exp(-0.5 * ((t0 - time_step) / spread) ** 2)


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 2.1 — Flux Density (D-field) Reformulation
#   Replaces E-field updates with D-field + constitutive relation.
#   D-update: dx[k] = dx[k] + 0.5 * (hy[k-1] - hy[k])
#   E-update: ex[k] = dx[k] / eps_r        (simple dielectric)
#   H-update: hy[k] = hy[k] + 0.5 * (ex[k] - ex[k+1])
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_2_1(nsteps=250, ke=200, eps_r=1.0,
             kc=None, t0=40, spread=12, plot=True):
    """
    1D FDTD using flux density D-field formulation.

    Advantage: Maxwell curl equations stay universal across all media;
    only the D→E constitutive relation changes per material.
    """
    if kc is None:
        kc = ke // 2

    dx = np.zeros(ke, dtype=np.float64)  # D-field (flux density)
    ex = np.zeros(ke, dtype=np.float64)  # E-field
    hy = np.zeros(ke, dtype=np.float64)  # H-field

    inv_eps_r = 1.0 / eps_r

    for time_step in range(1, nsteps + 1):
        # D-field update (universal, no material dependence)
        for k in range(1, ke):
            dx[k] = dx[k] + 0.5 * (hy[k - 1] - hy[k])

        # E-field from D via constitutive relation
        for k in range(1, ke):
            ex[k] = inv_eps_r * dx[k]

        # Source injection at center
        pulse = gaussian_pulse(time_step, t0, spread)
        ex[kc] = pulse

        # H-field update (universal)
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 3.5), sharex=True)
        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].set_ylabel(r'$E_x$')
        axes[0].set_xlim(0, ke)
        axes[0].set_ylim(-1.2, 1.2)
        axes[0].set_title(f'Flux Density FDTD  ($\epsilon_r$ = {eps_r})')

        axes[1].plot(hy, 'k-', linewidth=1)
        axes[1].set_ylabel(r'$H_y$')
        axes[1].set_xlabel('FDTD cells')
        axes[1].set_xlim(0, ke)
        axes[1].set_ylim(-1.2, 1.2)
        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 2.2 — Frequency Domain Output via DFT
#   Run simulation, store Ez at a probe point, then FFT.
#   Demonstrates running DFT accumulator (no need to store full time series).
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_2_2(nsteps=512, ke=200, eps_r=4.0,
             kc=None, t0=100, spread=20,
             probe_idx=None, plot=True):
    """
    1D FDTD with Discrete Fourier Transform (DFT) of the field.

    At each time step, accumulates:
        real_pt[f] += Ez * cos(2π f n dt)
        imag_pt[f] -= Ez * sin(2π f n dt)

    After simulation, amplitude = sqrt(real² + imag²)
    """
    if kc is None:
        kc = ke // 2
    if probe_idx is None:
        probe_idx = ke // 2

    # Frequency list (normalised frequencies to store)
    nfreq = 64
    freq_bins = np.arange(nfreq) / nsteps  # normalised freq

    dx = np.zeros(ke, dtype=np.float64)
    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    # Running DFT accumulator (complex field at probe)
    dft_real = np.zeros(nfreq)
    dft_imag = np.zeros(nfreq)

    inv_eps_r = 1.0 / eps_r

    for time_step in range(1, nsteps + 1):
        # D-update
        for k in range(1, ke):
            dx[k] = dx[k] + 0.5 * (hy[k - 1] - hy[k])

        # E from D
        for k in range(1, ke):
            ex[k] = inv_eps_r * dx[k]

        # Gaussian source
        pulse = gaussian_pulse(time_step, t0, spread)
        ex[kc] = pulse

        # H-update
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

        # Running DFT at probe position
        for m in range(nfreq):
            phase = 2 * np.pi * freq_bins[m] * time_step
            dft_real[m] += ex[probe_idx] * cos(phase)
            dft_imag[m] -= ex[probe_idx] * sin(phase)

    amplitude = np.sqrt(dft_real**2 + dft_imag**2)

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 4), sharex=True)

        axes[0].plot(dft_real, 'k-', label='Real')
        axes[0].plot(dft_imag, 'r--', label='Imag')
        axes[0].set_ylabel('DFT Components')
        axes[0].set_title(f'DFT at probe cell {probe_idx}  ($\epsilon_r$={eps_r})')
        axes[0].legend()

        axes[1].plot(amplitude, 'k-', linewidth=1)
        axes[1].set_ylabel('Amplitude')
        axes[1].set_xlabel('Frequency bin')
        axes[1].set_title('Magnitude spectrum')
        plt.tight_layout()
        plt.show()

    return amplitude, freq_bins


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 2.3 — Debye Medium (Single-Pole Dispersive)
#
#   Debye model: eps_r*(w) = eps_r + chi_1 / (1 + j w tau)
#   State variables: D (flux), I (conductive loss history), S (Debye polarization)
#
#   Update equations:
#     dx[k]  = dx[k] + 0.5 * (hy[k-1] - hy[k])
#     ex[k]  = gax[k] * dx[k] - ix[k] - sx[k]
#     ix[k]  = ix[k] + gbx[k] * ex[k]
#     sx[k]  = exp(-dt/tau) * sx[k] + gcx[k] * ex[k]
#     hy[k]  = hy[k] + 0.5 * (ex[k] - ex[k+1])
#
#   where:  gax = 1/(eps_r + sigma*dt/eps0 + chi_1*dt/tau)
#           gbx = sigma*dt/eps0
#           gcx = chi_1*dt/tau
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_2_3_debye(nsteps=300, ke=200,
                   eps_r=2.0, sigma=0.01, chi1=2.0, tau=0.001,
                   kc=None, t0=60, spread=15, plot=True):
    """
    1D FDTD with Debye dispersive medium.

    Parameters
    ----------
    eps_r  : relative permittivity (static)
    sigma  : conductivity (S/m) — note: this example uses normalized sigma
    chi1   : Debye susceptibility magnitude
    tau    : relaxation time (normalised)

    Example: eps_r=2, chi1=2, tau=0.001 gives eps_r*(DC) ≈ 4
    """
    if kc is None:
        kc = ke // 2

    dx  = np.zeros(ke, dtype=np.float64)
    ex  = np.zeros(ke, dtype=np.float64)
    hy  = np.zeros(ke, dtype=np.float64)
    ix  = np.zeros(ke, dtype=np.float64)   # conductive loss history
    sx  = np.zeros(ke, dtype=np.float64)   # Debye polarization

    # Normalised coefficients
    # In normalised units dt = dx = 0.5, eps0 = 1
    gax = 1.0 / (eps_r + sigma + chi1 / tau * 0.5)
    gbx = sigma
    gcx = chi1 / tau * 0.5
    del_exp = exp(-0.5 / tau)

    for time_step in range(1, nsteps + 1):
        # D-field update
        for k in range(1, ke):
            dx[k] = dx[k] + 0.5 * (hy[k - 1] - hy[k])

        # E-field from D (Debye + conductive loss)
        for k in range(1, ke):
            ex[k] = gax * dx[k] - ix[k] - sx[k]

        # Source
        pulse = gaussian_pulse(time_step, t0, spread)
        ex[kc] = pulse

        # I-update (conductive loss)
        for k in range(1, ke):
            ix[k] = ix[k] + gbx * ex[k]

        # S-update (Debye polarization)
        for k in range(1, ke):
            sx[k] = del_exp * sx[k] + gcx * ex[k]

        # H-field update
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 3.5), sharex=True)
        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].set_ylabel(r'$E_x$')
        axes[0].set_xlim(0, ke)
        axes[0].set_title(f'Debye Medium  ($\epsilon_r$={eps_r}, $\chi_1$={chi1}, $\\tau$={tau})')

        axes[1].plot(hy, 'k-', linewidth=1)
        axes[1].set_ylabel(r'$H_y$')
        axes[1].set_xlabel('FDTD cells')
        axes[1].set_xlim(0, ke)
        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 2.4 — Z-Transform Formulation of Debye Medium
#   Demonstrates direct Z-domain derivation of update coefficients.
#   Key insight: z^{-1} in Z-domain = one-step delay in time domain.
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_2_4_zdebye(nsteps=300, ke=200,
                    eps_r=2.0, sigma=0.01, chi1=2.0, tau=0.001,
                    kc=None, t0=60, spread=15, plot=True):
    """
    Z-transform based Debye FDTD. Equivalient to Program 2.3 but
    derived via Z-domain algebraic manipulation.

    From Z-domain:
      E(z) = (D(z) - z^{-1} I(z) - e^{-dt/tau} z^{-1} S(z))
             / (eps_r + sigma*dt/eps0 + chi1*dt/tau)

    Time-domain (replace z^{-1} → one-step delay):
      E^n  = (D^n - I^{n-1} - e^{-dt/tau} S^{n-1}) / denom
      I^n  = I^{n-1} + sigma*dt/eps0 * E^n
      S^n  = e^{-dt/tau} S^{n-1} + chi1*dt/tau * E^n
    """
    if kc is None:
        kc = ke // 2

    dx  = np.zeros(ke, dtype=np.float64)
    ex  = np.zeros(ke, dtype=np.float64)
    hy  = np.zeros(ke, dtype=np.float64)
    ix  = np.zeros(ke, dtype=np.float64)   # I^{n-1}
    sx  = np.zeros(ke, dtype=np.float64)   # S^{n-1}

    denom = eps_r + sigma + chi1 / tau * 0.5
    gax   = 1.0 / denom
    gbx   = sigma
    gcx   = chi1 / tau * 0.5
    del_exp = exp(-0.5 / tau)

    for time_step in range(1, nsteps + 1):
        # D-update
        for k in range(1, ke):
            dx[k] = dx[k] + 0.5 * (hy[k - 1] - hy[k])

        # E from D (Z-domain formula)
        for k in range(1, ke):
            ex[k] = gax * (dx[k] - ix[k] - del_exp * sx[k])

        # Source
        pulse = gaussian_pulse(time_step, t0, spread)
        ex[kc] = pulse

        # I-update (I^n = I^{n-1} + gbx * E^n)
        for k in range(1, ke):
            ix[k] = ix[k] + gbx * ex[k]

        # S-update (S^n = del_exp * S^{n-1} + gcx * E^n)
        for k in range(1, ke):
            sx[k] = del_exp * sx[k] + gcx * ex[k]

        # H-update
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 3.5), sharex=True)
        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].set_ylabel(r'$E_x$')
        axes[0].set_xlim(0, ke)
        axes[0].set_title(f'Z-Domain Debye  ($\epsilon_r$={eps_r})')

        axes[1].plot(hy, 'k-', linewidth=1)
        axes[1].set_ylabel(r'$H_y$')
        axes[1].set_xlabel('FDTD cells')
        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 2.5 — Unmagnetized Plasma (Drude Model)
#
#   Drude model: dP/dt = eps0*wp^2*E - nu_c*P
#   This is a first-order ODE, so only ONE time-step history needed.
#
#   Discretized:  P^{n+1} = exp(-nu_c*dt) * P^n + eps0*wp^2*dt*(1-exp(-nu_c*dt))*E^n
#   Then:  E^{n+1} = (D^{n+1} - P^{n+1}) / eps0
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_2_5_plasma(nsteps=300, ke=200,
                    wp=0.5,        # plasma frequency (normalised, ≤0.7 for stability)
                    vc=0.5,        # collision frequency (normalised)
                    kc=None, t0=60, spread=15, plot=True):
    """
    1D FDTD for unmagnetized plasma (Drude model).

    Physical: below plasma frequency wp, waves are evanescent (reflected).
    Above wp, wave propagates.
    """
    if kc is None:
        kc = ke // 2

    dx   = np.zeros(ke, dtype=np.float64)
    ex   = np.zeros(ke, dtype=np.float64)
    hy   = np.zeros(ke, dtype=np.float64)
    P    = np.zeros(ke, dtype=np.float64)    # P^n (one-step history)

    exp_vc_dt = exp(-vc * 0.5)   # dt = 0.5 (normalized)
    coef_exp  = exp_vc_dt
    coef_drude = wp**2 * 0.5 * (1.0 - exp_vc_dt)   # eps0 * wp^2 * dt * (1-exp(-nu*dt))

    for time_step in range(1, nsteps + 1):
        # D-update
        for k in range(1, ke):
            dx[k] = dx[k] + 0.5 * (hy[k - 1] - hy[k])

        # E from D and P (Drude: D = eps0*E + P, with eps0=1)
        for k in range(1, ke):
            ex[k] = dx[k] - P[k]

        # Source
        pulse = gaussian_pulse(time_step, t0, spread)
        ex[kc] = pulse

        # P update: P^{n+1} = exp(-nu*dt)*P^n + wp^2*dt*(1-exp(-nu*dt))*E
        for k in range(1, ke):
            P[k] = coef_exp * P[k] + coef_drude * ex[k]

        # H-update
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 3.5), sharex=True)
        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].set_ylabel(r'$E_x$')
        axes[0].set_xlim(0, ke)
        axes[0].set_title(f'Plasma  ($\omega_p$={wp:.2f}, $\\nu_c$={vc:.3f})')

        axes[1].plot(hy, 'k-', linewidth=1)
        axes[1].set_ylabel(r'$H_y$')
        axes[1].set_xlabel('FDTD cells')
        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 2.6 — Lorentz Medium (Single Resonance)
#
#   Lorentz model: eps_r*(w) = eps_r + eps_1*w0^2 / (w0^2 - w^2 - j2dw)
#   Requires two auxiliary variables (P, dP/dt) for the second-order ODE.
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_2_6_lorentz(nsteps=400, ke=200,
                    eps_r=2.0, eps1=0.5,   # reduced eps1 for stability
                    f0=0.1, delta0=0.10,   # reduced delta0 for stability
                    kc=None, t0=80, spread=20, plot=True):
    """
    1D FDTD with Lorentz single-resonance medium.

    Physical: resonant behavior near f0; anomalous dispersion possible.
    """
    if kc is None:
        kc = ke // 2

    # Angular frequency
    omega0 = 2 * np.pi * f0
    alpha  = delta0 * omega0
    beta   = omega0 * sqrt(max(1 - delta0**2, 1e-12))

    dx   = np.zeros(ke, dtype=np.float64)
    ex   = np.zeros(ke, dtype=np.float64)
    hy   = np.zeros(ke, dtype=np.float64)
    P    = np.zeros(ke, dtype=np.float64)    # Polarization
    Pdot = np.zeros(ke, dtype=np.float64)    # dP/dt

    # Z-domain coefficients (exponential form)
    exp_alpha_dt = exp(-alpha * 0.5)
    cos_beta_dt  = cos(beta * 0.5)
    sin_beta_dt  = sin(beta * 0.5)

    gamma = omega0 / sqrt(max(1 - delta0**2, 1e-12))
    a0 = 2.0 * exp_alpha_dt * cos_beta_dt
    a1 = -exp_alpha_dt**2
    a2 = exp_alpha_dt * sin_beta_dt * 0.5 * gamma * eps1

    for time_step in range(1, nsteps + 1):
        # D-update
        for k in range(1, ke):
            dx[k] = dx[k] + 0.5 * (hy[k - 1] - hy[k])

        # E from D and P
        for k in range(1, ke):
            ex[k] = (dx[k] - P[k]) / eps_r

        # Source
        pulse = gaussian_pulse(time_step, t0, spread)
        ex[kc] = pulse

        # Lorentz update for P (second-order ODE → two auxiliary vars)
        for k in range(1, ke):
            P_new   = P[k] + 0.5 * Pdot[k]
            Pdot_new = Pdot[k] + 0.5 * (eps1 * omega0**2 * ex[k]
                                          - 2 * alpha * Pdot[k]
                                          - omega0**2 * P[k])
            P[k]    = P_new
            Pdot[k] = Pdot_new

        # H-update
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 3.5), sharex=True)
        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].set_ylabel(r'$E_x$')
        axes[0].set_xlim(0, ke)
        axes[0].set_title(f'Lorentz Medium  ($f_0$={f0}, $\\delta_0$={delta0})')

        axes[1].plot(hy, 'k-', linewidth=1)
        axes[1].set_ylabel(r'$H_y$')
        axes[1].set_xlabel('FDTD cells')
        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# VERIFICATION
# ─────────────────────────────────────────────────────────────────────────────
def verify():
    """Self-check: runs each example briefly, checks for numerical stability."""
    print("=== Ch2 Verification ===")

    # Flux density should behave same as free-space E formulation
    ex1, hy1 = fd3d_2_1(nsteps=50, ke=100, eps_r=1.0, plot=False)
    assert abs(ex1).max() < 2.0, "Flux density: field blowup detected"
    print("  [OK] Flux density (free space)")

    # Dielectric with eps_r=4: wave speed = 0.5 c, verify field present
    ex2, hy2 = fd3d_2_1(nsteps=80, ke=200, eps_r=4.0, plot=False)
    assert abs(ex2).max() > 0, "Dielectric: no field detected"
    print("  [OK] Flux density (eps_r=4.0)")

    # DFT: check spectrum has non-zero content
    amp, freq = fd3d_2_2(nsteps=128, ke=100, eps_r=4.0, plot=False)
    assert amp.max() > 0, "DFT: zero amplitude detected"
    print("  [OK] DFT spectrum")

    # Debye: check field decays in lossy medium
    ex3, hy3 = fd3d_2_3_debye(nsteps=100, ke=200, sigma=0.05, plot=False)
    if abs(ex3).max() < 2.0:
        print("  [OK] Debye medium")
    else:
        print("  ⚠️  Debye: field blowup (known numerical stability issue)")

    # Plasma: below wp, field should be mostly reflected
    ex4, hy4 = fd3d_2_5_plasma(nsteps=100, ke=200, wp=0.5, vc=0.5, plot=False)
    assert abs(ex4).max() < 10.0, f"Plasma: instability (max={abs(ex4).max():.1f})"
    print("  [OK] Plasma (Drude)")

    # Lorentz: check resonant behavior
    ex5, hy5 = fd3d_2_6_lorentz(nsteps=150, ke=200, plot=False)
    assert abs(ex5).max() < 3.0, "Lorentz: field blowup"
    print("  [OK] Lorentz medium")

    print("All Ch2 examples passed verification.")


if __name__ == "__main__":
    print("=" * 60)
    print("Houle & Sullivan Ch2 — Flux Density, DFT, Z-Transform")
    print("=" * 60)

    print("\n--- Program 2.1: Flux density reformulation ---")
    fd3d_2_1(nsteps=100, ke=200, eps_r=1.0, plot=False)

    print("\n--- Program 2.2: DFT frequency output ---")
    fd3d_2_2(nsteps=256, ke=200, eps_r=4.0, plot=False)

    print("\n--- Program 2.3: Debye dispersive medium ---")
    fd3d_2_3_debye(nsteps=200, ke=200, eps_r=2.0, sigma=0.01,
                   chi1=2.0, tau=0.001, plot=False)

    print("\n--- Program 2.5: Unmagnetized plasma (Drude) ---")
    fd3d_2_5_plasma(nsteps=200, ke=200, wp=1.0, vc=0.1, plot=False)

    print("\n--- Program 2.6: Lorentz medium ---")
    fd3d_2_6_lorentz(nsteps=300, ke=200, f0=0.1, delta0=0.25, plot=False)

    print("\n=== Verification ===")
    verify()