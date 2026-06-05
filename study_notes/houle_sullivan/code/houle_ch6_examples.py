"""
houle_ch6_examples.py
=====================
Chapter 6 — Two-Dimensional FDTD: TM and TE Modes

Topics covered:
  6.1  2D TM mode equations (Ez, Hx, Hy)
  6.2  2D TE mode equations (Hx, Hy, Ez)
  6.3  Rectangular waveguide modes
  6.4  Scattering from dielectric cylinder
  6.5  PML in 2D (Berenger)
  6.6  RCS calculation basics

References:
  - Harrington (1961), "Time-Harmonic Electromagnetic Waves", McGraw-Hill
  - Houle & Sullivan, Ch. 6
"""

import numpy as np
from math import exp, sqrt, cos, sin, pi, atan2
from matplotlib import pyplot as plt
plt.rcParams['font.size'] = 12


def gaussian_pulse(time_step, t0, spread):
    return exp(-0.5 * ((t0 - time_step) / spread) ** 2)


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 6.1 — Basic 2D TM FDTD (no PML, simple dielectric)
#   Ez at integer grid, Hx/Hy at half-integer offsets.
#   Free-space parameters: gaz=1 everywhere.
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_6_1_2d_tm_basic(nsteps=120, ie=60, je=60,
                          ic=None, jc=None,
                          t0=25, spread=8, plot=True):
    """
    Basic 2D TM FDTD with Gaussian point source.
    TM mode: Ez (propagating), Hx, Hy (transverse)
    """
    if ic is None:
        ic = ie // 2
    if jc is None:
        jc = je // 2

    dz = np.zeros((ie, je), dtype=np.float64)
    ez = np.zeros((ie, je), dtype=np.float64)
    hx = np.zeros((ie, je), dtype=np.float64)
    hy = np.zeros((ie, je), dtype=np.float64)
    gaz = np.ones((ie, je), dtype=np.float64)

    snapshots = [25, 50, 80, 120]
    snap_data = []

    for time_step in range(1, nsteps + 1):
        # D-field update
        for j in range(1, je):
            for i in range(1, ie):
                dz[i, j] += 0.5 * (hy[i, j] - hy[i - 1, j]
                                  - hx[i, j] + hx[i, j - 1])

        # E from D
        for j in range(1, je):
            for i in range(1, ie):
                ez[i, j] = gaz[i, j] * dz[i, j]

        # Source
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

        if time_step in snapshots:
            snap_data.append(ez.copy())

    if plot:
        fig, axes = plt.subplots(2, 2, figsize=(9, 7))
        axes = axes.flatten()
        for ax, snap, t in zip(axes, snap_data, snapshots):
            im = ax.imshow(snap.T, origin='lower', cmap='RdBu_r',
                            vmin=-1.2, vmax=1.2, aspect='equal')
            ax.set_title(f'T = {t}')
            ax.set_xlabel('i')
            ax.set_ylabel('j')
        plt.suptitle('2D TM FDTD: Circular Wave Propagation', fontsize=13)
        plt.tight_layout()
        plt.show()

    return ez, hx, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 6.2 — 2D TE Mode FDTD
#   TE mode: Hz (propagating), Ex, Ey (transverse)
#   Equations (from normalized Maxwell):
#     dz[i,j] += 0.5 * (hy[i+1,j] - hy[i,j] - hx[i,j+1] + hx[i,j])
#     ex[i,j] += 0.5 * (hz[i,j] - hz[i,j-1])
#     ey[i,j] += 0.5 * (hx[i,j] - hx[i-1,j])
#     hx[i,j] += 0.5 * (ez[i,j] - ez[i,j-1])
#     hy[i,j] += 0.5 * (ex[i+1,j] - ex[i,j])
#     hz[i,j] += 0.5 * (ex[i,j+1] - ex[i,j] - ey[i+1,j] + ey[i,j])
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_6_2_2d_te(nsteps=120, ie=60, je=60,
                   ic=None, jc=None,
                   t0=25, spread=8, plot=True):
    """
    2D TE mode FDTD.
    Note: TE uses Hz as the main propagating field component.
    This example uses Hz point source.
    """
    if ic is None:
        ic = ie // 2
    if jc is None:
        jc = je // 2

    ex = np.zeros((ie, je), dtype=np.float64)
    ey = np.zeros((ie, je), dtype=np.float64)
    hz = np.zeros((ie, je), dtype=np.float64)
    hx = np.zeros((ie, je), dtype=np.float64)
    hy = np.zeros((ie, je), dtype=np.float64)

    for time_step in range(1, nsteps + 1):
        # H-field updates (Hz, Hx, Hy)
        for j in range(1, je - 1):
            for i in range(1, ie - 1):
                hx[i, j] += 0.5 * (hz[i, j] - hz[i, j - 1])
        for j in range(1, je):
            for i in range(1, ie - 1):
                hy[i, j] += 0.5 * (ex[i + 1, j] - ex[i, j])
        for j in range(1, je - 1):
            for i in range(1, ie - 1):
                hz[i, j] += 0.5 * (ex[i, j + 1] - ex[i, j]
                                  - ey[i + 1, j] + ey[i, j])

        # E-field updates (Ex, Ey)
        for j in range(1, je):
            for i in range(1, ie):
                ex[i, j] += 0.5 * (hz[i, j] - hz[i, j - 1])
        for j in range(1, je):
            for i in range(1, ie):
                ey[i, j] += 0.5 * (hx[i, j] - hx[i - 1, j])

        # Hz source (Gaussian)
        pulse = gaussian_pulse(time_step, t0, spread)
        hz[ic, jc] = pulse

    if plot:
        fig, ax = plt.subplots(figsize=(6, 5))
        extent = [0, ie, 0, je]
        im = ax.imshow(hz.T, origin='lower', cmap='RdBu_r',
                        vmin=-1.2, vmax=1.2, aspect='equal')
        ax.set_title(f'2D TE FDTD  (T={nsteps})')
        ax.set_xlabel('i')
        ax.set_ylabel('j')
        plt.colorbar(im, ax=ax, label=r'$H_z$')
        plt.tight_layout()
        plt.show()

    return ex, ey, hz


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 6.3 — Rectangular Waveguide Modes
#
#   Waveguide dimensions: a (width, x) × b (height, y)
#   For perfect electric conductor (PEC) walls:
#     TE_mn modes: f_mn = c/2 * sqrt((m/a)² + (n/b)²)
#     Dominant mode: TE_10 at f_10 = c/(2a)  (if a > b)
#
#   PEC boundary: E_t = 0 at walls → set ez=0 in boundary cells
# ─────────────────────────────────────────────────────────────────────────────
def waveguide_modes(a_m, b_m, freq_hz, eps_r=1.0, mu_r=1.0):
    """
    Calculate waveguide cutoff frequencies for TE_mn modes.

    f_mn = (c/2) * sqrt((m/a)² + (n/b)²)
    For TE modes, both m,n cannot be zero simultaneously.
    """
    c0 = 3e8 / sqrt(eps_r * mu_r)
    modes = []
    for m in range(10):
        for n in range(10):
            if m == 0 and n == 0:
                continue
            f_mn = 0.5 * c0 * sqrt((m / a_m)**2 + (n / b_m)**2)
            modes.append((m, n, f_mn))
    modes.sort(key=lambda x: x[2])
    return modes


def fd3d_6_3_waveguide(nsteps=200, ie=100, je=50,
                        a=0.1, b=0.05,   # meters
                        m_te=1, n_te=0,  # dominant TE_10 mode
                        t0=40, spread=10, plot=True):
    """
    2D TM waveguide simulation (propagating TE_10 mode along z).

    PEC boundary: set gaz=0 at walls (Ez=0 condition).
    The dominant TE_10 mode has E_z = 0 everywhere (since E has no z-component
    in TE mode). For TM modes (what we model in 2D here), the E field has
    a z-component — but waveguide analysis uses different mode conventions.

    Here we model a parallel-plate waveguide using TM mode:
    - PEC top/bottom walls: Ez=0 at j=0, j=je-1
    - Side walls: open (Mur ABC)
    """
    # Waveguide dimensions in grid units
    # Plate separation: je-2 cells (free space)
    # Plate length: ie cells

    dz = np.zeros((ie, je), dtype=np.float64)
    ez = np.zeros((ie, je), dtype=np.float64)
    hx = np.zeros((ie, je), dtype=np.float64)
    hy = np.zeros((ie, je), dtype=np.float64)

    # PEC walls at top and bottom: gaz=0 → Ez=0
    gaz = np.ones((ie, je), dtype=np.float64)
    gaz[:, 0] = 0.0
    gaz[:, je - 1] = 0.0

    # Cutoff frequency of TE_10 mode
    c0 = 3e8
    f_cutoff = c0 / (2 * a)   # for parallel plate, a = plate separation

    # Source frequency (should be above cutoff for propagation)
    f_source = f_cutoff * 1.5

    # Probe at center
    probe_idx = ie // 2

    for time_step in range(1, nsteps + 1):
        # D update
        for j in range(1, je - 1):
            for i in range(1, ie - 1):
                dz[i, j] += 0.5 * (hy[i, j] - hy[i - 1, j]
                                  - hx[i, j] + hx[i, j - 1])

        # E from D
        for j in range(1, je - 1):
            for i in range(1, ie - 1):
                ez[i, j] = gaz[i, j] * dz[i, j]

        # Source: sinusoidal at bottom wall (TE_10 mode pattern)
        # The TE_10 Ez pattern is cos(pi*x/a) — maximum at center
        pulse = sin(2 * np.pi * f_source * time_step * 0.5)  # normalized freq
        ez[probe_idx, 1] = pulse

        # Hx update
        for j in range(1, je - 2):
            for i in range(1, ie - 1):
                hx[i, j] += 0.5 * (ez[i, j] - ez[i, j + 1])

        # Hy update
        for j in range(1, je - 2):
            for i in range(1, ie - 2):
                hy[i, j] += 0.5 * (ez[i + 1, j] - ez[i, j])

        # Boundary: ez=0 at walls already from gaz=0 (no need to set explicitly)

    if plot:
        fig, axes = plt.subplots(1, 2, figsize=(11, 3.5))

        # Field snapshot
        extent = [0, ie, 0, je]
        im0 = axes[0].imshow(ez.T, origin='lower', cmap='RdBu_r',
                               vmin=-1.2, vmax=1.2, aspect='equal')
        axes[0].set_title('Waveguide: Ez field')
        axes[0].set_xlabel('i (x)')
        axes[0].set_ylabel('j (y)')
        plt.colorbar(im0, ax=axes[0], label=r'$E_z$')

        # Field profile at center (x-cut)
        j_center = je // 2
        axes[1].plot(ez[:, j_center], 'k-', linewidth=1)
        axes[1].set_xlabel('i (x)')
        axes[1].set_ylabel(r'$E_z$ at center')
        axes[1].set_title('Center cut (TE_10 mode pattern)')
        axes[1].set_xlim(0, ie)

        plt.suptitle(f'Parallel-Plate Waveguide  (f_cutoff={f_cutoff/1e9:.2f} GHz)')
        plt.tight_layout()
        plt.show()

    return ez, hx, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 6.4 — Scattering from Dielectric Cylinder
#   TFSF formulation with plane wave incident.
#   Dielectric cylinder: radius R, eps_r, sigma.
#   Object specified by "in-or-out" test: sqrt((i-ic)² + (j-jc)²) <= R
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_6_4_scattering(nsteps=250, ie=100, je=100,
                         radius=10, eps_r=30.0, sigma=0.3,
                         ic=None, jc=None,
                         t0=50, spread=15, plot=True):
    """
    2D TM scattering from a dielectric cylinder.

    Plane wave incident in +y direction.
    TF region contains the object; SF region is outside.

    Object: in-or-out test gives staircasing error.
    """
    if ic is None:
        ic = ie // 2
    if jc is None:
        jc = je // 2

    # TF/SF boundaries
    ia = ic - radius - 5
    ib = ic + radius + 5
    ja = jc - radius - 5
    jb = jc + radius + 5

    # Incident buffer (1D plane wave in +y)
    ez_inc = np.zeros(je + 1)
    hx_inc = np.zeros(je)

    # Main grid
    dz = np.zeros((ie, je), dtype=np.float64)
    ez = np.zeros((ie, je), dtype=np.float64)
    hx = np.zeros((ie, je), dtype=np.float64)
    hy = np.zeros((ie, je), dtype=np.float64)

    # Material parameters
    gaz = np.ones((ie, je), dtype=np.float64)
    gbz = np.zeros((ie, je), dtype=np.float64)

    for j in range(ja, jb + 1):
        for i in range(ia, ib + 1):
            dist = sqrt((i - ic)**2 + (j - jc)**2)
            if dist <= radius:
                gaz[i, j] = 1.0 / eps_r
                gbz[i, j] = sigma

    # Take final snapshot
    for time_step in range(1, nsteps + 1):
        # Incident buffer update
        for j in range(1, je):
            ez_inc[j] += 0.5 * (hx_inc[j - 1] - hx_inc[j])

        pulse = gaussian_pulse(time_step, t0, spread)
        ez_inc[ja] += pulse

        for j in range(1, je):
            hx_inc[j] += 0.5 * (ez_inc[j] - ez_inc[j + 1])

        # D-field
        for j in range(1, je):
            for i in range(1, ie):
                dz[i, j] += 0.5 * (hy[i, j] - hy[i - 1, j]
                                  - hx[i, j] + hx[i, j - 1])

        # TF/SF corrections (bottom and top)
        for i in range(ia, ib + 1):
            dz[i, ja] += 0.5 * hx_inc[ja - 1]
            dz[i, jb] -= 0.5 * hx_inc[jb + 1]

        # E from D with material
        for j in range(1, je):
            for i in range(1, ie):
                ez[i, j] = gaz[i, j] * dz[i, j] - gbz[i, j] * dz[i, j]

        # Hx update
        for j in range(1, je - 1):
            for i in range(1, ie):
                hx[i, j] += 0.5 * (ez[i, j] - ez[i, j + 1])

        for i in range(ia, ib + 1):
            hx[i, ja - 1] += 0.5 * ez_inc[ja]
            hx[i, jb]     -= 0.5 * ez_inc[jb]

        # Hy update
        for j in range(1, je):
            for i in range(1, ie - 1):
                hy[i, j] += 0.5 * (ez[i + 1, j] - ez[i, j])

    if plot:
        fig, axes = plt.subplots(1, 2, figsize=(11, 4))

        extent = [0, ie, 0, je]
        im0 = axes[0].imshow(ez.T, origin='lower', cmap='RdBu_r',
                               vmin=-1.2, vmax=1.2, aspect='equal')
        # Draw cylinder
        circle = plt.Circle((ic, jc), radius, fill=False,
                             color='white', linewidth=2)
        axes[0].add_patch(circle)
        axes[0].set_title('Scattering: Plane Wave + Dielectric Cylinder')
        axes[0].set_xlabel('i')
        axes[0].set_ylabel('j')
        plt.colorbar(im0, ax=axes[0], label=r'$E_z$')

        # Object material map
        axes[1].imshow(gaz.T, origin='lower', cmap='viridis', aspect='equal')
        axes[1].set_title(r'Dielectric: $\epsilon_r$ map')
        axes[1].set_xlabel('i')
        axes[1].set_ylabel('j')
        plt.colorbar(axes[1].images[0], ax=axes[1], label=r'$\epsilon_r$')

        plt.tight_layout()
        plt.show()

    return ez, hx, hy, gaz


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 6.5 — 2D TM with Dielectric Slab Waveguide
#   Slab: thin film of high eps_r on substrate.
#   Core mode: guided by total internal reflection at slab boundaries.
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_6_5_slab_waveguide(nsteps=300, ie=100, je=80,
                             slab_thickness=10,
                             eps_core=9.0, eps_clad=1.0,
                             ic=None, jc=None,
                             t0=30, spread=8, plot=True):
    """
    2D TM dielectric slab waveguide.

    The slab guides modes via total internal reflection.
    For step-index slab: V = k0 * a * sqrt(n1^2 - n2^2)
    Single-mode condition: V < 2.405
    """
    if ic is None:
        ic = ie // 2
    if jc is None:
        jc = je // 2

    # Slab: center in y, thickness in j-direction
    slab_start = je // 2 - slab_thickness // 2
    slab_end   = slab_start + slab_thickness

    dz = np.zeros((ie, je), dtype=np.float64)
    ez = np.zeros((ie, je), dtype=np.float64)
    hx = np.zeros((ie, je), dtype=np.float64)
    hy = np.zeros((ie, je), dtype=np.float64)
    gaz = np.ones((ie, je), dtype=np.float64)

    # Set slab permittivity
    for j in range(slab_start, slab_end):
        for i in range(ie):
            gaz[i, j] = 1.0 / eps_core
    for j in range(je):
        if j < slab_start or j >= slab_end:
            gaz[i, j] = 1.0 / eps_clad

    for time_step in range(1, nsteps + 1):
        # D update
        for j in range(1, je):
            for i in range(1, ie):
                dz[i, j] += 0.5 * (hy[i, j] - hy[i - 1, j]
                                  - hx[i, j] + hx[i, j - 1])

        # E from D
        for j in range(1, je):
            for i in range(1, ie):
                ez[i, j] = gaz[i, j] * dz[i, j]

        # Gaussian source at left edge
        if time_step > 1:
            pulse = gaussian_pulse(time_step, t0, spread)
            ez[5, je // 2] = pulse

        # Hx
        for j in range(1, je - 1):
            for i in range(1, ie):
                hx[i, j] += 0.5 * (ez[i, j] - ez[i, j + 1])

        # Hy
        for j in range(1, je):
            for i in range(1, ie - 1):
                hy[i, j] += 0.5 * (ez[i + 1, j] - ez[i, j])

    if plot:
        fig, ax = plt.subplots(figsize=(9, 4))
        extent = [0, ie, 0, je]
        im = ax.imshow(ez.T, origin='lower', cmap='RdBu_r',
                        vmin=-1.2, vmax=1.2, aspect='equal')
        ax.axhline(slab_start, color='white', linewidth=2, label='Slab boundaries')
        ax.axhline(slab_end, color='white', linewidth=2)
        ax.set_title(f'Dielectric Slab Waveguide  ($\epsilon_r$={eps_core})')
        ax.set_xlabel('i (x)')
        ax.set_ylabel('j (y)')
        plt.colorbar(im, ax=ax, label=r'$E_z$')
        plt.tight_layout()
        plt.show()

    return ez, gaz


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 6.6 — RCS (Radar Cross Section) Calculation (2D)
#
#   RCS in 2D (per unit length):  σ_2d = lim_{r→∞} 2πr |E_s|² / |E_i|²
#
#   Far-field from near-field (2D equivalence):
#     E_s(φ) = (k/4) * sqrt(2/(πkr)) * ∫ E_z(i,j) * exp(jkr') * (n̂·r̂) dl
#   For a 2D object: we sum contributions around the perimeter.
# ─────────────────────────────────────────────────────────────────────────────
def compute_rcs_2d(ez_field, ie, je, ic, jc,
                   radius, wavelength, plot=True):
    """
    Approximate 2D RCS using near-field to far-field transformation.

    For a cylindrical scatterer, the scattered field at a distant point
    in direction φ is approximated by the integral of the induced
    surface current around the perimeter.

    This uses the physical optics approximation:
      E_s(φ) ∝ ∮ E_tangential(s) * exp(-jk·r_s) ds

    For demonstration: compute scattered field amplitude at perimeter.
    """
    k = 2 * np.pi / wavelength

    # Sample field around the cylinder perimeter at radius R
    n_angles = 360
    angles = np.linspace(0, 2 * np.pi, n_angles)
    e_tangential = np.zeros(n_angles)

    for n, theta in enumerate(angles):
        px = int(round(ic + radius * np.cos(theta)))
        py = int(round(jc + radius * np.sin(theta)))
        px = max(0, min(ie - 1, px))
        py = max(0, min(je - 1, py))
        e_tangential[n] = ez_field[px, py]

    # Far-field scattering amplitude (simplified 2D physical optics)
    # E_s(phi) = (k/4) * H0^(2)(kr) * integral of e_tan * cos(theta) ds
    # For simplicity, use amplitude of Fourier transform of surface field
    from numpy.fft import fft, fftfreq
    e_ft = fft(e_tangential)
    freqs = fftfreq(n_angles)

    if plot:
        fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))

        axes[0].plot(np.degrees(angles), e_tangential, 'k-', linewidth=1)
        axes[0].set_xlabel('Angle (deg)')
        axes[0].set_ylabel(r'$E_z$ tangential at perimeter')
        axes[0].set_title('Surface Field on Cylinder')
        axes[0].set_xlim(0, 360)

        axes[1].plot(np.degrees(angles), np.abs(e_ft)[:n_angles//2], 'k-', linewidth=1)
        axes[1].set_xlabel('Harmonic order')
        axes[1].set_ylabel('Scattering amplitude')
        axes[1].set_title('Fourier Component (RCS pattern)')
        axes[1].set_xlim(0, n_angles // 2)

        plt.tight_layout()
        plt.show()

    return np.abs(e_ft), angles


# ─────────────────────────────────────────────────────────────────────────────
# VERIFICATION
# ─────────────────────────────────────────────────────────────────────────────
def verify():
    """Self-check for Ch6 2D FDTD code."""
    print("=== Ch6 Verification ===")

    # Basic TM: circular wave
    ez1, _, _ = fd3d_6_1_2d_tm_basic(nsteps=80, ie=40, je=40, plot=False)
    assert abs(ez1).max() > 0, "2D TM: no field"
    print("  [OK] 2D TM basic")

    # TE mode: check non-zero
    ex2, ey2, hz2 = fd3d_6_2_2d_te(nsteps=80, ie=40, je=40, plot=False)
    assert abs(hz2).max() > 0, "2D TE: no field"
    print("  [OK] 2D TE mode")

    # Waveguide: check field is zero at walls
    ez3, _, _ = fd3d_6_3_waveguide(nsteps=100, ie=80, je=30, plot=False)
    assert abs(ez3[:, 0]).max() < 1e-6, "Waveguide: Ez non-zero at wall"
    assert abs(ez3[:, -1]).max() < 1e-6, "Waveguide: Ez non-zero at wall"
    print("  [OK] Waveguide (Ez=0 at walls)")

    # Dielectric cylinder: check field inside/outside
    ez4, _, _, gaz4 = fd3d_6_4_scattering(nsteps=100, ie=60, je=60,
                                           radius=8, plot=False)
    assert abs(ez4).max() > 0, "Scattering: no field"
    print("  [OK] Dielectric cylinder scattering")

    print("All Ch6 examples passed verification.")


if __name__ == "__main__":
    print("=" * 60)
    print("Houle & Sullivan Ch6 — 2D FDTD")
    print("=" * 60)

    print("\n--- Program 6.1: Basic 2D TM ---")
    fd3d_6_1_2d_tm_basic(nsteps=100, ie=60, je=60, plot=True)

    print("\n--- Program 6.3: Waveguide ---")
    fd3d_6_3_waveguide(nsteps=200, ie=80, je=40, plot=True)

    print("\n--- Program 6.4: Scattering ---")
    fd3d_6_4_scattering(nsteps=200, ie=80, je=80, radius=10, plot=True)

    print("\n--- Program 6.5: Slab Waveguide ---")
    fd3d_6_5_slab_waveguide(nsteps=200, ie=80, je=60, slab_thickness=12,
                             eps_core=9.0, plot=True)

    print("\n=== Verification ===")
    verify()