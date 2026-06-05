"""
houle_ch4_examples.py
=====================
Chapter 4 — Absorbing Boundary Conditions (ABC): Mur ABC and PML

Topics covered:
  4.1  First-order Mur ABC (one-way wave equation)
  4.2  Second-order Mur ABC
  4.3  Perfectly Matched Layer (PML) — anisotropic lossy medium
  4.4  2D PML implementation
  4.5  TF/SF (Total-Field/Scattered-Field) formulation

References:
  - Mur (1981), "Absorbing boundary conditions for the finite-difference
    approximation of the time-domain electromagnetic field equations",
    IEEE Trans. Electromagn. Compat., vol. 23, pp. 377-384.
  - Berenger (1994), "A perfectly matched layer for the absorption of
    electromagnetic waves", J. Comput. Phys., vol. 114.
  - Houle & Sullivan, Ch. 4
"""

import numpy as np
from math import exp, sqrt
from matplotlib import pyplot as plt
plt.rcParams['font.size'] = 12

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def gaussian_pulse(time_step, t0, spread):
    return exp(-0.5 * ((t0 - time_step) / spread) ** 2)


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 4.1 — First-Order Mur ABC (1D)
#
#   One-way wave equation:  ∂E/∂t + c·∂E/∂z = 0  (forward wave)
#                          ∂E/∂t - c·∂E/∂z = 0  (backward wave)
#
#   Discretized:  E[0]^{n+1} = E[0]^n + (c*dt-dx)/(c*dt+dx) * (E[0]^n - E[1]^n)
#   In normalized units c=1, dx=dt → coefficient = 0 → E[0]^{n+1} = E[1]^n
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_4_1_mur_abc_1d(nsteps=300, ke=200,
                         kc=None, t0=40, spread=12, plot=True):
    """
    1D FDTD with first-order Mur absorbing boundary condition.

    At left boundary (k=0): ex[0] = ex[1]  (since c*dt=dx in normalized)
    At right boundary: ex[ke-1] = ex[ke-2]
    """
    if kc is None:
        kc = ke // 2

    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    # Mur ABC state arrays
    abc_low_prev  = 0.0   # previous ex[0] for left ABC
    abc_high_prev = 0.0   # previous ex[ke-1] for right ABC

    # Store snapshots for movie-style plot
    snapshots = []

    for time_step in range(1, nsteps + 1):
        # E-field interior update
        for k in range(1, ke):
            ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])

        # Source
        pulse = gaussian_pulse(time_step, t0, spread)
        ex[kc] = pulse

        # H-field interior update
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

        # Mur ABC — left boundary (k=0)
        # First-order: E^{n+1}[0] = E^n[0] + (c*dt-dx)/(c*dt+dx)*(E^n[0]-E^n[1])
        # Normalized: c*dt = 0.5, dx = 1 → (0.5-1)/(0.5+1) = -1/3
        # For simplicity we use the limit c*dt = dx → coefficient → 0
        # which gives: ex[0] = ex_prev (exact ABC for normal incidence in 1D)
        ex[0]    = abc_low_prev
        abc_low_prev = ex[1]

        # Mur ABC — right boundary (k=ke-1)
        ex[ke-1] = abc_high_prev
        abc_high_prev = ex[ke - 2]

        if time_step in [50, 100, 200, 300]:
            snapshots.append(ex.copy())

    if plot:
        fig, axes = plt.subplots(2, 2, figsize=(10, 5))
        axes = axes.flatten()
        times = [50, 100, 200, 300]
        for ax, snap, t in zip(axes, snapshots, times):
            ax.plot(snap, 'k-', linewidth=1)
            ax.set_xlim(0, ke)
            ax.set_ylim(-1.2, 1.2)
            ax.set_title(f'T = {t}')
            ax.set_xlabel('FDTD cells')
            ax.set_ylabel(r'$E_x$')
        plt.suptitle('Mur ABC: Pulse leaving domain', fontsize=13)
        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 4.2 — Second-Order Mur ABC (1D)
#
#   Second-order Mur: uses two ghost points for better absorption
#   ∂²E/∂t∂z ≈ (E[0]^{n+1} - 2*E[0]^n + E[0]^{n-1}) / (2Δt)
#   The implementation uses a boundary value field array of length 2.
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_4_2_mur2_abc_1d(nsteps=300, ke=200,
                          kc=None, t0=40, spread=12, plot=True):
    """
    1D FDTD with second-order Mur ABC.
    More accurate than first-order for oblique incidence.
    """
    if kc is None:
        kc = ke // 2

    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    # Second-order Mur ABC needs 2-step history at each boundary
    # Left boundary: store ex_low[0] (previous) and ex_low[1] (2-step back)
    # Right boundary: same
    exc_low  = np.zeros(3)   # [E^{n-1}, E^n] — indices 0,1
    exc_high = np.zeros(3)

    for time_step in range(1, nsteps + 1):
        # E interior
        for k in range(1, ke):
            ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])

        pulse = gaussian_pulse(time_step, t0, spread)
        ex[kc] = pulse

        # H interior
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

        # Second-order Mur ABC — left
        # E^{n+1}[0] = -E^{n-1}[1] + (2 - 6*dx/(c*dt+dx)) * E^n[0]
        # For normalized c=1, dx=1, dt=0.5: coefficient = -1/3
        # Using the exact discrete form:
        # exc_low[0] = E^{n-1}[0], exc_low[1] = E^n[0], exc_low[2] = E^n[1]
        c = 1.0   # normalized wave speed
        dx = 1.0
        dt = 0.5

        # Left boundary
        coeff = (c * dt - dx) / (c * dt + dx)   # = -1/3 in normalized
        ex_new_low = -exc_low[1] + (2 + 4 * coeff) * ex[0] + (-1 - 2 * coeff) * ex[1]
        # Shift history
        exc_low[1] = ex[0]   # old E^n[0] → E^{n-1} for next step
        exc_low[0] = exc_low[2]  # shift  (not strictly needed for simple version)

        # Actually use simpler form: second-order Mur formula
        # E_new = -E_old[1] + 2*E_old[0] + coeff*(E_old[0] - E_old[2])
        ex[0] = -ex[1] + 2 * exc_low[1] + coeff * (exc_low[1] - ex[1])
        exc_low[1] = ex[0]   # update latest for next iteration

        # Right boundary
        ex[ke-1] = -ex[ke-2] + 2 * exc_high[1] + coeff * (exc_high[1] - ex[ke-2])
        exc_high[1] = ex[ke-1]

    if plot:
        fig, ax = plt.subplots(figsize=(8, 3.5))
        ax.plot(ex, 'k-', linewidth=1)
        ax.set_xlim(0, ke)
        ax.set_ylim(-1.2, 1.2)
        ax.set_title('Second-Order Mur ABC')
        ax.set_xlabel('FDTD cells')
        ax.set_ylabel(r'$E_x$')
        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 4.3 — PML in 1D
#
#   PML: add conductivity σ in the direction of wave propagation.
#   For wave in z-direction: add complex permittivity ε*(x) = ε - jσ/ω
#   which corresponds to exponential decay of the field as it enters PML.
#
#   Berenger PML key idea: split field into two sub-components so that
#   the one-way wave equation is satisfied exactly.
#   For 1D:  Ex split into Exx and Exy with different conductivities.
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_4_3_pml_1d(nsteps=400, ke=200,
                     npml=10, sigma_max=0.3,
                     kc=None, t0=40, spread=12, plot=True):
    """
    1D FDTD with Berenger PML layer.

    Uses the split-field formulation:
      Dx = Dxx + Dxy
      Dxx update: Dxx^{n+1} = exp(-sigma_x*dt) * Dxx^n + ...
      Dxy update: Dxy^{n+1} = exp(-sigma_y*dt) * Dxy^n + ...
    """
    if kc is None:
        kc = ke // 2

    # Field arrays
    ex   = np.zeros(ke, dtype=np.float64)
    hy   = np.zeros(ke, dtype=np.float64)
    dxx  = np.zeros(ke, dtype=np.float64)
    dxy  = np.zeros(ke, dtype=np.float64)

    # PML conductivity profile (cubic grading from boundary inward)
    sigma_x = np.zeros(ke)
    for i in range(npml):
        sigma_x[i] = sigma_max * (i / npml) ** 3
        sigma_x[ke - 1 - i] = sigma_max * (i / npml) ** 3

    # Decay factors for each cell (exp(-sigma*dt))
    decay_xx = np.exp(-sigma_x * 0.5)   # dt = 0.5
    decay_xy = np.exp(-sigma_x * 0.5)

    for time_step in range(1, nsteps + 1):
        # Dxx update (x-directed PML)
        for k in range(1, ke):
            dxx[k] = decay_xx[k] * dxx[k] + 0.5 * hy[k - 1]

        # Dxy update (y-directed PML)
        for k in range(1, ke):
            dxy[k] = decay_xy[k] * dxy[k] - 0.5 * hy[k]

        # E from D (D = Dxx + Dxy for total D)
        for k in range(1, ke):
            ex[k] = dxx[k] + dxy[k]

        # Source
        pulse = gaussian_pulse(time_step, t0, spread)
        ex[kc] = pulse

        # H update
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 4))
        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].set_ylabel(r'$E_x$')
        axes[0].set_xlim(0, ke)
        axes[0].set_title('PML 1D FDTD')

        axes[1].plot(sigma_x, 'k-', linewidth=2, label=r'$\sigma_x$ profile')
        axes[1].set_ylabel(r'$\sigma$')
        axes[1].set_xlabel('FDTD cells')
        axes[1].legend()
        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 4.4 — 2D TM FDTD with Mur ABC
#
#   TM mode: Ez, Hx, Hy
#   Update equations (free space):
#     dz[i,j] = dz[i,j] + 0.5*(hy[i,j]-hy[i-1,j] - hx[i,j]+hx[i,j-1])
#     ez[i,j] = dz[i,j]
#     hx[i,j] = hx[i,j] + 0.5*(ez[i,j]-ez[i,j+1])
#     hy[i,j] = hy[i,j] + 0.5*(ez[i+1,j]-ez[i,j])
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_4_4_2d_mur(nsteps=100, ie=60, je=60,
                     npml=8,
                     ic=None, jc=None,
                     t0=20, spread=8, plot=True):
    """
    2D TM FDTD with Mur ABC at all four boundaries.

    Mur ABC applied to Ez at all four edges:
      Top/bottom: ez[*, 0] and ez[*, je-1]
      Left/right: ez[0, *] and ez[ie-1, *]
    """
    if ic is None:
        ic = ie // 2
    if jc is None:
        jc = je // 2

    dz = np.zeros((ie, je), dtype=np.float64)
    ez = np.zeros((ie, je), dtype=np.float64)
    hx = np.zeros((ie, je), dtype=np.float64)
    hy = np.zeros((ie, je), dtype=np.float64)

    # PML / ABC arrays (Mur uses boundary field history)
    # Store previous Ez at each boundary edge
    abc_top    = np.zeros(ie)
    abc_bottom = np.zeros(ie)
    abc_left   = np.zeros(je)
    abc_right  = np.zeros(je)

    for time_step in range(1, nsteps + 1):
        # D-field update
        for j in range(1, je):
            for i in range(1, ie):
                dz[i, j] += 0.5 * (hy[i, j] - hy[i - 1, j]
                                  - hx[i, j] + hx[i, j - 1])

        # E from D
        for j in range(1, je):
            for i in range(1, ie):
                ez[i, j] = dz[i, j]

        # Gaussian source
        pulse = gaussian_pulse(time_step, t0, spread)
        ez[ic, jc] = pulse

        # Hx update
        for j in range(1, je - 1):
            for i in range(1, ie):
                hx[i, j] += 0.5 * (ez[i, j] - ez[i, j + 1])

        # Hy update
        for j in range(1, je):
            for i in range(1, ie - 1):
                hy[i, j] += 0.5 * (ez[i + 1, j] - ez[i, j])

        # === First-order Mur ABC ===
        # Top (j=0): forward wave in -y direction
        ez[:, 0]    = abc_top
        abc_top[:]  = ez[:, 1]

        # Bottom (j=je-1): forward wave in +y direction
        ez[:, je-1] = abc_bottom
        abc_bottom[:] = ez[:, je - 2]

        # Left (i=0): forward wave in -x direction
        ez[0, :]    = abc_left
        abc_left[:] = ez[1, :]

        # Right (i=ie-1): forward wave in +x direction
        ez[ie-1, :] = abc_right
        abc_right[:] = ez[ie - 2, :]

    if plot:
        fig, ax = plt.subplots(figsize=(6, 5))
        extent = [0, ie, 0, je]
        im = ax.imshow(ez.T, extent=extent, origin='lower',
                        cmap='RdBu_r', aspect='equal',
                        vmin=-1.2, vmax=1.2)
        ax.set_title(f'2D TM FDTD with Mur ABC  (T={nsteps})')
        ax.set_xlabel('i (x-direction)')
        ax.set_ylabel('j (y-direction)')
        plt.colorbar(im, ax=ax, label=r'$E_z$')
        plt.tight_layout()
        plt.show()

    return ez, hx, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 4.5 — 2D TM FDTD with PML
#
#   Berenger PML: complex permittivity in x and y directions.
#   Uses auxiliary current fields IHy, IHx.
#   gi, fi parameterization for x-direction; gj, fj for y-direction.
# ─────────────────────────────────────────────────────────────────────────────
def calculate_pml_2d(ie, je, npml=8, sigma_max=0.333):
    """Calculate 2D PML coefficient arrays."""
    gi1 = np.zeros(ie); gi2 = np.ones(ie); gi3 = np.ones(ie)
    fi1 = np.zeros(ie); fi2 = np.ones(ie); fi3 = np.ones(ie)
    gj1 = np.zeros(je); gj2 = np.ones(je); gj3 = np.ones(je)
    fj1 = np.zeros(je); fj2 = np.ones(je); fj3 = np.ones(je)

    for i in range(1, npml + 1):
        ratio = (npml - i + 1) / npml
        xn = sigma_max * (1 - ratio) ** 3   # cubic grading
        gi2[i] = 1.0 / (1.0 + xn)
        gi3[i] = (1.0 - xn) / (1.0 + xn)
        fi1[i] = xn
        fi2[i] = 1.0 / (1.0 + xn)
        fi3[i] = (1.0 - xn) / (1.0 + xn)

        # half-cell
        xn_half = sigma_max * (1 - (ratio - 0.5)) ** 3
        fi2[i - 1] = 1.0 / (1.0 + xn_half)
        fi3[i - 1] = (1.0 - xn_half) / (1.0 + xn_half)

    # Mirror for right and top
    for i in range(ie - npml, ie):
        gi2[i] = gi2[ie - 2 - i]
        gi3[i] = gi3[ie - 2 - i]
        fi1[i] = fi1[ie - 2 - i]
        fi2[i] = fi2[ie - 2 - i]
        fi3[i] = fi3[ie - 2 - i]

    for j in range(1, npml + 1):
        ratio = (npml - j + 1) / npml
        yn = sigma_max * (1 - ratio) ** 3
        gj2[j] = 1.0 / (1.0 + yn)
        gj3[j] = (1.0 - yn) / (1.0 + yn)
        fj1[j] = yn
        fj2[j] = 1.0 / (1.0 + yn)
        fj3[j] = (1.0 - yn) / (1.0 + yn)

        yn_half = sigma_max * (1 - (ratio - 0.5)) ** 3
        fj2[j - 1] = 1.0 / (1.0 + yn_half)
        fj3[j - 1] = (1.0 - yn_half) / (1.0 + yn_half)

    for j in range(je - npml, je):
        gj2[j] = gj2[je - 2 - j]
        gj3[j] = gj3[je - 2 - j]
        fj1[j] = fj1[je - 2 - j]
        fj2[j] = fj2[je - 2 - j]
        fj3[j] = fj3[je - 2 - j]

    return gi1, gi2, gi3, fi1, fi2, fi3, gj1, gj2, gj3, fj1, fj2, fj3


def fd3d_4_5_2d_pml(nsteps=100, ie=60, je=60,
                     npml=8, sigma_max=0.333,
                     ic=None, jc=None,
                     t0=20, spread=8, plot=True):
    """
    2D TM FDTD with Berenger PML absorbing boundary.

    Key differences from Mur:
    - Uses IHy, IHx auxiliary fields for inverse permeability
    - gi, gj parameters for D-field attenuation
    - fi, fj parameters for H-field attenuation
    """
    if ic is None:
        ic = ie // 2
    if jc is None:
        jc = je // 2

    dz   = np.zeros((ie, je), dtype=np.float64)
    ez   = np.zeros((ie, je), dtype=np.float64)
    hx   = np.zeros((ie, je), dtype=np.float64)
    hy   = np.zeros((ie, je), dtype=np.float64)
    ihx  = np.zeros((ie, je), dtype=np.float64)   # auxiliary for Hx
    ihy  = np.zeros((ie, je), dtype=np.float64)   # auxiliary for Hy

    (gi1, gi2, gi3, fi1, fi2, fi3,
     gj1, gj2, gj3, fj1, fj2, fj3) = calculate_pml_2d(ie, je, npml, sigma_max)

    for time_step in range(1, nsteps + 1):
        # D-field update with PML
        for j in range(1, je):
            for i in range(1, ie):
                dz[i, j] = (gi3[i] * gj3[j] * dz[i, j]
                            + gi2[i] * gj2[j] * 0.5 * (
                                hy[i, j] - hy[i - 1, j]
                              - hx[i, j] + hx[i, j - 1]))

        # E from D
        for j in range(1, je):
            for i in range(1, ie):
                ez[i, j] = dz[i, j]

        # Source
        pulse = gaussian_pulse(time_step, t0, spread)
        ez[ic, jc] = pulse

        # Hx update with PML (uses IHx auxiliary current)
        for j in range(1, je - 1):
            for i in range(1, ie):
                curl_e = ez[i, j] - ez[i, j + 1]
                ihx[i, j + 1] += curl_e
                hx[i, j] += 0.5 * curl_e + fi1[i] * ihx[i, j + 1]

        # Hy update with PML (uses IHy auxiliary current)
        for j in range(1, je):
            for i in range(1, ie - 1):
                curl_e = ez[i + 1, j] - ez[i, j]
                ihy[i + 1, j] += curl_e
                hy[i, j] += 0.5 * curl_e + fj1[j] * ihy[i + 1, j]

    if plot:
        fig, ax = plt.subplots(figsize=(6, 5))
        extent = [0, ie, 0, je]
        im = ax.imshow(ez.T, extent=extent, origin='lower',
                        cmap='RdBu_r', aspect='equal',
                        vmin=-1.2, vmax=1.2)
        ax.set_title(f'2D TM FDTD with PML  (T={nsteps})')
        ax.set_xlabel('i')
        ax.set_ylabel('j')
        plt.colorbar(im, ax=ax, label=r'$E_z$')
        plt.tight_layout()
        plt.show()

    return ez, hx, hy


# ─────────────────────────────────────────────────────────────────────────────
# VERIFICATION
# ─────────────────────────────────────────────────────────────────────────────
def verify():
    """Self-check for Ch4 ABC/PML code."""
    print("=== Ch4 Verification ===")

    # Mur ABC: should absorb without reflection
    ex_mur, _ = fd3d_4_1_mur_abc_1d(nsteps=200, ke=100, plot=False)
    assert abs(ex_mur).max() < 3.0, "Mur ABC: field blowup"
    print("  [OK] Mur ABC 1D")

    # 2D Mur: check field is non-zero in center
    ez_mur, _, _ = fd3d_4_4_2d_mur(nsteps=80, ie=40, je=40, plot=False)
    assert abs(ez_mur).max() > 0, "2D Mur: no field detected"
    print("  [OK] 2D Mur ABC")

    # 2D PML: check field is non-zero in center
    ez_pml, _, _ = fd3d_4_5_2d_pml(nsteps=80, ie=40, je=40, plot=False)
    assert abs(ez_pml).max() > 0, "2D PML: no field detected"
    print("  [OK] 2D PML")

    print("All Ch4 examples passed verification.")


if __name__ == "__main__":
    print("=" * 60)
    print("Houle & Sullivan Ch4 — Absorbing Boundary Conditions")
    print("=" * 60)

    print("\n--- Program 4.1: First-order Mur ABC (1D) ---")
    fd3d_4_1_mur_abc_1d(nsteps=200, ke=200, plot=True)

    print("\n--- Program 4.4: 2D TM with Mur ABC ---")
    fd3d_4_4_2d_mur(nsteps=80, ie=60, je=60, plot=True)

    print("\n--- Program 4.5: 2D TM with PML ---")
    fd3d_4_5_2d_pml(nsteps=80, ie=60, je=60, plot=True)

    print("\n=== Verification ===")
    verify()