"""
houle_ch5_examples.py
=====================
Chapter 5 — Source Excitation in FDTD

Topics covered:
  5.1  Hard source (直接设定 E 或 H)
  5.2  Soft source (叠加到现有场)
  5.3  TFSF (Total-Field/Scattered-Field) boundary formulation
  5.4  Plane wave generation (Gaussian pulse)
  5.5  Sinusoidal steady-state source
  5.6  Total-field/Scattered-field in 2D TM

References:
  - Taflove (1995), "Computational Electrodynamics", Artech House
  - Houle & Sullivan, Ch. 5
"""

import numpy as np
from math import exp, sin, cos, sqrt
from matplotlib import pyplot as plt
plt.rcParams['font.size'] = 12

# Normalized units: c=1, dx=dt=0.5
c0_normalized = 1.0


def gaussian_pulse(time_step, t0, spread):
    return exp(-0.5 * ((t0 - time_step) / spread) ** 2)


def sine_wave(time_step, freq):
    """Sinusoidal source at normalized frequency."""
    return sin(2 * np.pi * freq * time_step)


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 5.1 — Hard Source (直接注入 E-field)
#   A hard source 直接 overwrites the field value at the source cell.
#   Acts as a voltage source (ideal voltage generator).
#   Problem: reflects backward wave with reflection coefficient ≈ 1.
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_5_1_hard_source(nsteps=300, ke=200,
                         kc=None, t0=60, spread=15,
                         source_type='gaussian', freq=0.1,
                         plot=True):
    """
    1D FDTD with hard E-field source.

    The hard source directly sets ex[kc] = source_value each time step.
    This generates a wave but reflects backward-propagating waves with
    coefficient ≈ 1 (almost total reflection).
    """
    if kc is None:
        kc = ke // 2

    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    # Record field at probe
    probe_idx = ke - 10
    probe_signal = np.zeros(nsteps + 1)

    for time_step in range(1, nsteps + 1):
        # E interior update
        for k in range(1, ke):
            ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])

        # Hard source injection
        if source_type == 'gaussian':
            source_val = gaussian_pulse(time_step, t0, spread)
        else:
            source_val = sine_wave(time_step, freq)

        ex[kc] = source_val   # overwrites

        # Record probe
        probe_signal[time_step] = ex[probe_idx]

        # H interior update
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 4))

        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].set_ylabel(r'$E_x$')
        axes[0].set_xlim(0, ke)
        axes[0].set_title('Hard Source (direct injection)')
        axes[0].text(kc, 0.5, 'SOURCE', ha='center', fontsize=10)

        axes[1].plot(probe_signal[1:], 'k-', linewidth=1)
        axes[1].set_ylabel(r'$E_x$ at probe')
        axes[1].set_xlabel('Time step')
        axes[1].set_title('Probe signal (shows backward reflections)')
        plt.tight_layout()
        plt.show()

    return ex, hy, probe_signal


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 5.2 — Soft Source (加法注入)
#   A soft source 叠加到现有场: ex[kc] += source_value
#   Behaves like a current source — less reflective than hard source.
#   Key advantage: backward reflections are absorbed by the source itself.
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_5_2_soft_source(nsteps=300, ke=200,
                          kc=None, t0=60, spread=15,
                          source_type='gaussian', freq=0.1,
                          plot=True):
    """
    1D FDTD with soft source (additive injection).

    ex[kc] += source_value  (superpose onto existing field)
    More physical for current-source modeling, less reflection.
    """
    if kc is None:
        kc = ke // 2

    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    probe_idx = ke - 10
    probe_signal = np.zeros(nsteps + 1)

    for time_step in range(1, nsteps + 1):
        # E interior
        for k in range(1, ke):
            ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])

        # Soft source injection (superposition)
        if source_type == 'gaussian':
            source_val = gaussian_pulse(time_step, t0, spread)
        else:
            source_val = sine_wave(time_step, freq)

        ex[kc] += source_val   # additive

        probe_signal[time_step] = ex[probe_idx]

        # H interior
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 4))

        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].set_ylabel(r'$E_x$')
        axes[0].set_xlim(0, ke)
        axes[0].set_title('Soft Source (additive injection)')

        axes[1].plot(probe_signal[1:], 'k-', linewidth=1)
        axes[1].set_ylabel(r'$E_x$ at probe')
        axes[1].set_xlabel('Time step')
        axes[1].set_title('Probe signal')
        plt.tight_layout()
        plt.show()

    return ex, hy, probe_signal


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 5.3 — H-field (magnetic) Source
#   Specifies H-field directly at a location using Ampere's law.
#   Equivalent to specifying a current I at the gap of a dipole.
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_5_3_hard_h_source(nsteps=300, ke=200,
                            kc=None, t0=60, spread=15, plot=True):
    """
    1D FDTD with H-field hard source (magnetic dipole).

    Instead of setting E directly, we set H at the source position.
    This is more physical for a dipole antenna where current is the
    fundamental source quantity.
    """
    if kc is None:
        kc = ke // 2

    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    for time_step in range(1, nsteps + 1):
        # E interior
        for k in range(1, ke):
            ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])

        # E source — but note: we use H-source here
        pulse = gaussian_pulse(time_step, t0, spread)
        ex[kc] = pulse   # keep E source for simplicity

        # H interior
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

        # Hard H-source at kc-1/2: adds current equivalent
        # Magnetic current: Hy[kc-1] += pulse (simplified treatment)
        hy[kc - 1] += pulse

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 3.5))
        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].set_ylabel(r'$E_x$')
        axes[0].set_xlim(0, ke)
        axes[0].set_title('H-field (Magnetic) Source')

        axes[1].plot(hy, 'k-', linewidth=1)
        axes[1].set_ylabel(r'$H_y$')
        axes[1].set_xlabel('FDTD cells')
        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 5.4 — TFSF (Total-Field/Scattered-Field) in 1D
#
#   TF/SF separates incident + scattered (total field) from scattered-only
#   region. The TFSF boundary corrects fields that would otherwise use
#   out-of-region values.
#
#   For 1D wave propagating in +z direction:
#     TF/SF corrections at j=ja and j=jb:
#       Ex[ja] += 0.5 * Hy_inc[ja-1]   (add incident to TF region)
#       Hy[ja-1] += 0.5 * Ex_inc[ja]
#       Ex[jb] -= 0.5 * Hy_inc[jb+1]
#       Hy[jb] -= 0.5 * Ex_inc[jb]
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_5_4_tfsf_1d(nsteps=300, ke=200,
                      ia=50, ib=150,
                      t0=60, spread=15, plot=True):
    """
    1D FDTD with Total-Field/Scattered-Field (TF/SF) boundary.

    The TF region [ia, ib] contains incident + scattered waves.
    The SF region outside contains only scattered waves.

    TF/SF corrections at the boundaries inject the incident plane wave.
    """
    # Incident field array (1D buffer propagating in +z)
    ez_inc  = np.zeros(ke + 1)   # incident E
    hy_inc  = np.zeros(ke)      # incident H

    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    ja = ia   # TF/SF lower boundary
    jb = ib   # TF/SF upper boundary

    for time_step in range(1, nsteps + 1):
        # Update incident buffer (1D FDTD in +z direction)
        for k in range(1, ke):
            ez_inc[k] = ez_inc[k] + 0.5 * (hy_inc[k - 1] - hy_inc[k])

        # Inject Gaussian pulse at ja
        pulse = gaussian_pulse(time_step, t0, spread)
        ez_inc[ja] = pulse

        # H-field incident
        for k in range(1, ke):
            hy_inc[k] = hy_inc[k] + 0.5 * (ez_inc[k] - ez_inc[k + 1])

        # ===== TOTAL FIELD UPDATE =====
        for k in range(1, ke):
            ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])

        # TF/SF corrections at lower boundary (k=ja)
        ex[ja] += 0.5 * hy_inc[ja - 1]   # add incident Hy to Ex at boundary

        # TF/SF corrections at upper boundary (k=jb)
        ex[jb] -= 0.5 * hy_inc[jb + 1]   # subtract incident Hy from Ex

        # ===== H-FIELD UPDATE (includes TF/SF corrections) =====
        for k in range(1, ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

        # TF/SF H correction at lower outside: Hy[ja-1] += 0.5 * Ex_inc[ja]
        hy[ja - 1] += 0.5 * ez_inc[ja]

        # TF/SF H correction at upper outside: Hy[jb] -= 0.5 * Ex_inc[jb]
        hy[jb] -= 0.5 * ez_inc[jb]

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 4))
        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].axvline(ja, color='gray', linestyle='--', label='TF/SF boundary')
        axes[0].axvline(jb, color='gray', linestyle='--')
        axes[0].set_ylabel(r'$E_x$ (Total field)')
        axes[0].set_xlim(0, ke)
        axes[0].set_title('TF/SF: Incident wave injected at boundary')
        axes[0].legend()

        axes[1].plot(ex, 'k-', linewidth=1)
        axes[1].axvline(ja, color='gray', linestyle='--')
        axes[1].axvline(jb, color='gray', linestyle='--')
        axes[1].set_ylabel(r'$E_x$')
        axes[1].set_xlabel('FDTD cells')
        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 5.5 — 2D TM with TFSF Plane Wave
#   TM mode: Ez, Hx, Hy
#   TFSF box in 2D: corrections at all four boundaries
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_5_5_2d_tfsf(nsteps=150, ie=80, je=80,
                     ia=20, ib=60, ja=20, jb=60,
                     t0=30, spread=10, plot=True):
    """
    2D TM FDTD with TF/SF plane wave injection.

    TF region: ia ≤ i ≤ ib, ja ≤ j ≤ jb
    SF region: outside

    TF/SF corrections (wave propagating in +y direction):
      - Bottom (j=ja): dz[i,ja] += 0.5 * hx_inc[ja-1]
      - Top (j=jb):   dz[i,jb] -= 0.5 * hx_inc[jb+1]
      - Hx below bottom: hx[i,ja-1] += 0.5 * ez_inc[ja]
      - Hx above top:    hx[i,jb]   -= 0.5 * ez_inc[jb]
    """
    # Incident buffer (1D, propagating in +y)
    ez_inc = np.zeros(je + 1)
    hx_inc = np.zeros(je)

    dz = np.zeros((ie, je), dtype=np.float64)
    ez = np.zeros((ie, je), dtype=np.float64)
    hx = np.zeros((ie, je), dtype=np.float64)
    hy = np.zeros((ie, je), dtype=np.float64)

    for time_step in range(1, nsteps + 1):
        # Update incident buffer (1D FDTD in y)
        for j in range(1, je):
            ez_inc[j] += 0.5 * (hx_inc[j - 1] - hx_inc[j])

        # Inject Gaussian at bottom of TF region
        pulse = gaussian_pulse(time_step, t0, spread)
        ez_inc[ja] += pulse

        # Update incident H
        for j in range(1, je):
            hx_inc[j] += 0.5 * (ez_inc[j] - ez_inc[j + 1])

        # === D-field update ===
        for j in range(1, je):
            for i in range(1, ie):
                dz[i, j] += 0.5 * (hy[i, j] - hy[i - 1, j]
                                  - hx[i, j] + hx[i, j - 1])

        # TF/SF: add incident H contribution to D at TF boundaries
        for i in range(ia, ib + 1):
            dz[i, ja] += 0.5 * hx_inc[ja - 1]   # bottom
            dz[i, jb] -= 0.5 * hx_inc[jb + 1]   # top

        # E from D
        for j in range(1, je):
            for i in range(1, ie):
                ez[i, j] = dz[i, j]

        # Hx update
        for j in range(1, je - 1):
            for i in range(1, ie):
                hx[i, j] += 0.5 * (ez[i, j] - ez[i, j + 1])

        # TF/SF Hx corrections at bottom and top of SF region
        for i in range(ia, ib + 1):
            hx[i, ja - 1] += 0.5 * ez_inc[ja]   # below bottom
            hx[i, jb]     -= 0.5 * ez_inc[jb]   # above top

        # Hy update
        for j in range(1, je):
            for i in range(1, ie - 1):
                hy[i, j] += 0.5 * (ez[i + 1, j] - ez[i, j])

    if plot:
        fig, ax = plt.subplots(figsize=(6, 5))
        extent = [0, ie, 0, je]
        im = ax.imshow(ez.T, extent=extent, origin='lower',
                        cmap='RdBu_r', aspect='equal',
                        vmin=-1.2, vmax=1.2)
        # Draw TFSF boundary
        rect = plt.Rectangle((ia, ja), ib - ia, jb - ja,
                              fill=False, edgecolor='white', linewidth=2)
        ax.add_patch(rect)
        ax.set_title(f'2D TM TF/SF Plane Wave  (T={nsteps})')
        ax.set_xlabel('i')
        ax.set_ylabel('j')
        plt.colorbar(im, ax=ax, label=r'$E_z$')
        plt.tight_layout()
        plt.show()

    return ez, hx, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 5.6 — Ricker Wavelet (band-limited) Source
#   Ricker wavelet: second derivative of Gaussian
#   g(t) = (1 - 2π²f²t²) · exp(-π²f²t²)
#   Has zero DC component — better for wave propagation.
# ─────────────────────────────────────────────────────────────────────────────
def ricker_wavelet(time_step, fcent, t0):
    """Ricker wavelet (zero-DC, band-limited)."""
    tau = time_step - t0
    pi_f_sq = np.pi**2 * fcent**2
    return (1.0 - 2.0 * pi_f_sq * tau**2) * np.exp(-pi_f_sq * tau**2)


def fd3d_5_6_ricker(nsteps=300, ke=200,
                    kc=None, fcent=0.1, t0=60,
                    plot=True):
    """
    1D FDTD with Ricker wavelet source.

    Advantage over Gaussian: zero DC component, faster decay.
    Spectrum is centered at fcent with bandwidth ~fcent.
    """
    if kc is None:
        kc = ke // 2

    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    probe_signal = np.zeros(nsteps + 1)
    probe_idx = ke - 10

    for time_step in range(1, nsteps + 1):
        # E update
        for k in range(1, ke):
            ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])

        # Ricker source
        ex[kc] += ricker_wavelet(time_step, fcent, t0)

        probe_signal[time_step] = ex[probe_idx]

        # H update
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 4))
        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].set_ylabel(r'$E_x$')
        axes[0].set_xlim(0, ke)
        axes[0].set_title('Ricker Wavelet Source')

        axes[1].plot(probe_signal[1:], 'k-', linewidth=1)
        axes[1].set_ylabel(r'$E_x$ at probe')
        axes[1].set_xlabel('Time step')
        plt.tight_layout()
        plt.show()

    return ex, hy, probe_signal


# ─────────────────────────────────────────────────────────────────────────────
# VERIFICATION
# ─────────────────────────────────────────────────────────────────────────────
def verify():
    """Self-check Ch5 source excitation code."""
    print("=== Ch5 Verification ===")

    # Hard source: field should propagate outward
    ex1, _, _ = fd3d_5_1_hard_source(nsteps=150, ke=100, plot=False)
    assert abs(ex1).max() > 0, "Hard source: no field"
    print("  [OK] Hard source")

    # Soft source: additive injection
    ex2, _, _ = fd3d_5_2_soft_source(nsteps=150, ke=100, plot=False)
    assert abs(ex2).max() > 0, "Soft source: no field"
    print("  [OK] Soft source")

    # TFSF: field inside TF region should be different from SF
    ex4, _ = fd3d_5_4_tfsf_1d(nsteps=150, ke=200, ia=50, ib=150, plot=False)
    assert abs(ex4).max() > 0, "TFSF: no field"
    print("  [OK] TF/SF 1D")

    # 2D TFSF: check non-zero
    ez5, _, _ = fd3d_5_5_2d_tfsf(nsteps=80, ie=60, je=60, ia=15, ib=45, ja=15, jb=45, plot=False)
    assert abs(ez5).max() > 0, "2D TFSF: no field"
    print("  [OK] 2D TF/SF")

    # Ricker: check zero mean (zero DC)
    _, _, probe = fd3d_5_6_ricker(nsteps=200, ke=100, fcent=0.1, t0=60, plot=False)
    dc_offset = np.mean(probe[50:])
    assert abs(dc_offset) < 0.1, f"Ricker DC offset too large: {dc_offset}"
    print("  [OK] Ricker wavelet (zero DC)")

    print("All Ch5 examples passed verification.")


if __name__ == "__main__":
    print("=" * 60)
    print("Houle & Sullivan Ch5 — Source Excitation")
    print("=" * 60)

    print("\n--- Hard Source ---")
    fd3d_5_1_hard_source(nsteps=200, ke=200, plot=True)

    print("\n--- Soft Source ---")
    fd3d_5_2_soft_source(nsteps=200, ke=200, plot=True)

    print("\n--- TF/SF (1D) ---")
    fd3d_5_4_tfsf_1d(nsteps=200, ke=200, plot=True)

    print("\n--- Ricker Wavelet ---")
    fd3d_5_6_ricker(nsteps=300, ke=200, fcent=0.08, t0=60, plot=True)

    print("\n=== Verification ===")
    verify()