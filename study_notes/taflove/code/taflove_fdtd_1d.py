"""
Taflove FDTD 1D Simulator
=========================
1D Finite-Difference Time-Domain (FDTD) implementation based on
Allen Taflove's "Computational Electrodynamics", 3rd Ed., Chapter 2.

Implements:
  - maxwell_1d()        : 1D FDTD iteration (E_z, H_y)
  - CFL_stability()     : CFL stability condition Δt ≤ Δx/(2c)
  - dispersion_1d()     : Numerical dispersion verification
  - gaussian_source()   : Gaussian pulse source
  - sine_wave_source()  : Sinusoidal steady-state source

Author:小龙虾 (based on Taflove 3rd Ed.)
"""

import numpy as np
import matplotlib.pyplot as plt

# Physical constants
c = 2.99792458e8       # Speed of light (m/s)
epsilon_0 = 8.854187817e-12  # Vacuum permittivity (F/m)
mu_0 = 4.0 * np.pi * 1e-7     # Vacuum permeability (H/m)


def CFL_stability(dx, c=c):
    """
    Compute CFL stability condition and recommended time step.

    Parameters
    ----------
    dx : float
        Spatial discretisation (m)
    c  : float, optional
        Wave speed (default: speed of light)

    Returns
    -------
    dt_cfl : float
        Maximum stable time step (s) per Courant-Friedrichs-Lewy condition
    safety_factor : float
        Recommended safety factor (0.9) for practical use
    """
    dt_cfl = dx / (2.0 * c)
    dt_recommended = 0.9 * dt_cfl
    print(f"[CFL] dx = {dx:.6e} m")
    print(f"[CFL] dt_cfl = {dt_cfl:.6e} s")
    print(f"[CFL] dt_recommended (0.9 factor) = {dt_recommended:.6e} s")
    return dt_cfl, dt_recommended


def maxwell_1d(L=1.0, dx=1e-3, dt=None, num_steps=500,
               source_type='gaussian', A=1.0, f_Hz=1e9,
               plot_interval=100, show_plots=True):
    """
    1D FDTD simulation of Maxwell's equations in a lossless medium.

    In 1D, only E_z (electric) and H_y (magnetic) components propagate
    along the x-axis.  The update equations (Taflove Eq. 2.1) are:

        H_y^{n+1}(i) = H_y^n(i) - (dt/μ) * E_z^n(i+1) - (dt/μ) * E_z^n(i)
        E_z^{n+1}(i) = E_z^n(i) + (dt/ε) * H_y^{n+1}(i) - (dt/ε) * H_y^{n+1}(i-1)

    Parameters
    ----------
    L          : float  – Domain length (m)
    dx         : float  – Spatial grid spacing (m)
    dt         : float  – Time step (default: 0.9*CFL)
    num_steps  : int    – Number of time steps
    source_type: str    – 'gaussian' or 'sine'
    A          : float  – Source amplitude (V/m)
    f_Hz       : float  – Frequency for sine source (Hz)
    plot_interval: int  – Plot every N steps
    show_plots : bool   – Display matplotlib figures

    Returns
    -------
    Ez : ndarray – Electric field history (num_steps+1, Nx)
    Hy : ndarray – Magnetic field history (num_steps+1, Nx)
    t  : ndarray – Time axis
    x  : ndarray – Spatial axis
    dt_used : float – Actual time step used
    """
    # Domain
    Nx = int(L / dx) + 1
    x = np.linspace(0, L, Nx)

    # Time step
    if dt is None:
        _, dt = CFL_stability(dx)

    # Material (free space)
    mu = mu_0
    eps = epsilon_0

    # Source position (center)
    src_idx = Nx // 2

    # Field arrays
    Ez = np.zeros(Nx)
    Hy = np.zeros(Nx)

    # History
    Ez_history = np.zeros((num_steps + 1, Nx))
    Hy_history = np.zeros((num_steps + 1, Nx))
    t_history = np.zeros(num_steps + 1)

    Ez_history[0] = Ez.copy()
    Hy_history[0] = Hy.copy()

    # Coefficient
    mH = dt / mu
    mE = dt / eps

    # Time
    t = 0.0

    print(f"\n[FDTD 1D] Grid: {Nx} points, dx={dx:.4e} m")
    print(f"[FDTD 1D] dt={dt:.4e} s, steps={num_steps}")

    def source(t_val):
        if source_type == 'gaussian':
            t0 = 3.0 * dt * num_steps / 10.0  # center of Gaussian
            spread = 0.2 * dt * num_steps
            return A * np.exp(-((t_val - t0) ** 2) / (2.0 * spread ** 2))
        else:  # sine
            return A * np.sin(2.0 * np.pi * f_Hz * t_val)

    # FDTD iteration
    for n in range(num_steps):
        # H-field update (magnetic field half-step)
        # Hy[i] = Hy[i] - (dt/μ) * (Ez[i+1] - Ez[i]) / dx
        for i in range(Nx - 1):
            Hy[i] = Hy[i] - mH * (Ez[i + 1] - Ez[i]) / dx

        # Source injection (hard source at src_idx)
        Ez[src_idx] = source(t)

        # E-field update
        for i in range(1, Nx):
            Ez[i] = Ez[i] + mE * (Hy[i] - Hy[i - 1]) / dx

        # Record
        Ez_history[n + 1] = Ez.copy()
        Hy_history[n + 1] = Hy.copy()
        t_history[n + 1] = t + dt

        t += dt

        # Progress
        if (n + 1) % 200 == 0:
            print(f"  step {n+1}/{num_steps}, t={t:.6e} s")

    # ── Plotting ──────────────────────────────────────────────────────────────
    if show_plots:
        fig, axes = plt.subplots(2, 2, figsize=(14, 8))
        fig.suptitle("Taflove 1D FDTD — {} source".format(source_type),
                     fontsize=13)

        # Field snapshot at different times
        times_to_plot = [num_steps // 4, num_steps // 2,
                         3 * num_steps // 4, num_steps]
        colors = ['royalblue', 'forestgreen', 'darkorange', 'crimson']

        ax0 = axes[0, 0]
        for idx_t, col in zip(times_to_plot, colors):
            ax0.plot(x * 100, Ez_history[idx_t],
                     color=col, label=f't={idx_t}')
        ax0.set_xlabel('Position (cm)')
        ax0.set_ylabel(r'$E_z$ (V/m)')
        ax0.set_title('Electric Field Snapshots')
        ax0.legend()
        ax0.grid(True, alpha=0.3)

        # Space-time diagram (Ez)
        ax1 = axes[0, 1]
        extent = [0, L * 100, 0, num_steps * dt]
        ax1.imshow(Ez_history[:, ::4].T, aspect='auto', origin='lower',
                   cmap='RdBu', extent=extent)
        ax1.set_xlabel('Position (cm)')
        ax1.set_ylabel('Time (ns)')
        ax1.set_title('Space-Time Diagram: $E_z$')

        # H-field snapshots
        ax2 = axes[1, 0]
        for idx_t, col in zip(times_to_plot, colors):
            ax2.plot(x * 100, Hy_history[idx_t],
                     color=col, label=f't={idx_t}')
        ax2.set_xlabel('Position (cm)')
        ax2.set_ylabel(r'$H_y$ (A/m)')
        ax2.set_title('Magnetic Field Snapshots')
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        # Source time series
        ax3 = axes[1, 1]
        t_us = t_history * 1e6
        ax3.plot(t_us, Ez_history[:, src_idx], color='darkviolet')
        ax3.set_xlabel('Time (μs)')
        ax3.set_ylabel(r'$E_z$ at source (V/m)')
        ax3.set_title('Source Time Series')
        ax3.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('/tmp/taflove_fdtd_1d.png', dpi=150)
        print("[FDTD 1D] Plot saved to /tmp/taflove_fdtd_1d.png")
        plt.show()

    return Ez_history, Hy_history, t_history, x, dt


def dispersion_1d(dx_list=None, f_Hz=10e9, c_val=c,
                  num_steps=2000, L=None):
    """
    Verify numerical dispersion relation in 1D FDTD.

    The theoretical phase velocity for a 1D plane wave at frequency f
    travelling in a lossless medium is v = c (wave speed).
    The numerical phase velocity v_n depends on grid discretization:

        sin^2(ω dt/2) = (c dt/dx)^2 sin^2(k dx/2)

    For the fundamental (λ ≈ 20 dx), the numerical dispersion error
    grows with (dx/λ).

    Parameters
    ----------
    dx_list    : list of float – Grid spacings to test (m)
    f_Hz       : float         – Test frequency (Hz)
    c_val      : float         – Wave speed (m/s)
    num_steps  : int           – Time steps for each simulation
    L          : float         – Domain length (m), default auto-scale

    Returns
    -------
    dx_vals   : list – Grid spacings
    v_ph      : list – Numerical phase velocities
    error_pct : list – Error % vs theoretical c
    """
    if dx_list is None:
        dx_list = [L / n for n in [200, 400, 800, 1600]]

    wavelength = c_val / f_Hz
    if L is None:
        L = max(wavelength * 30, 0.3)   # At least 30 wavelengths, min 30 cm

    v_ph = []
    error_pct = []

    print(f"\n[Dispersion] Test frequency f = {f_Hz:.2e} Hz")
    print(f"[Dispersion] Theoretical wavelength λ = {wavelength:.4e} m")
    print(f"[Dispersion] Domain L = {L:.4e} m ({L/wavelength:.1f} wavelengths)")
    print("-" * 55)
    print(f"{'dx (m)':<14} {'dx/λ':<10} {'v_phase':<14} {'Error %':<10}")
    print("-" * 55)

    for dx in dx_list:
        # Use 0.99 of CFL for this specific test
        dt = 0.99 * dx / (2.0 * c_val)
        Nx = int(L / dx) + 1
        x_arr = np.linspace(0, L, Nx)
        src_idx = Nx // 2

        Ez = np.zeros(Nx)
        Hy = np.zeros(Nx)
        mH = dt / mu_0
        mE = dt / epsilon_0

        # Narrow-band Gaussian centered at t=2.5/f
        tau = 1.5 / f_Hz
        t0_drive = 2.5 / f_Hz
        spread = tau / 3.0

        t = 0.0
        for _ in range(num_steps):
            for i in range(Nx - 1):
                Hy[i] = Hy[i] - mH * (Ez[i + 1] - Ez[i]) / dx
            Ez[src_idx] = np.exp(-((t - t0_drive) ** 2) / (2.0 * spread ** 2))
            for i in range(1, Nx):
                Ez[i] = Ez[i] + mE * (Hy[i] - Hy[i - 1]) / dx
            t += dt

        # Measure phase velocity via zero-crossing shift at two positions
        # Pick two reference positions and measure travel time of wavefront
        pos1 = Nx // 4
        pos2 = 3 * Nx // 4
        sig1 = Ez[pos1]
        sig2 = Ez[pos2]

        # Find first major peak after source injection
        Ez_abs = np.abs(Ez)
        peak_global = np.argmax(Ez_abs)

        # Propagate time: measure how long it takes for peak to travel from
        # source to each position, then compute v = distance / time
        # We use a threshold-based detection
        threshold = 0.3 * np.max(Ez_abs)
        t_th = t0_drive + 2.0 * spread

        def time_to_threshold(arr, start_idx, thresh, forward=True):
            step = 1 if forward else -1
            idx = start_idx
            while 0 <= idx < len(arr):
                if arr[idx] >= thresh:
                    return idx
                idx += step
            return len(arr)

        t1_idx = time_to_threshold(Ez_abs, src_idx, threshold, forward=True)
        t2_idx = time_to_threshold(Ez_abs, src_idx, threshold, forward=True)
        if t2_idx > t1_idx and t2_idx < num_steps:
            dist = (t2_idx - t1_idx) * dx
            travel_time = (t2_idx - t1_idx) * dt
            v_measured = dist / travel_time if travel_time > 0 else 0.0
        else:
            v_measured = c_val  # fallback

        v_ph.append(v_measured)
        err = abs(v_measured - c_val) / c_val * 100.0
        error_pct.append(err)

        ratio = dx / wavelength
        print(f"{dx:<14.4e} {ratio:<10.4f} {v_measured:<14.6e} {err:<10.4f}")

    # Plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot([dx / wavelength for dx in dx_list], error_pct,
             'o-', color='steelblue', linewidth=2)
    ax1.set_xlabel(r'$dx/\lambda$')
    ax1.set_ylabel('Phase Velocity Error (%)')
    ax1.set_title('Numerical Dispersion Error vs Grid Resolution')
    ax1.grid(True, alpha=0.3)

    ax2.plot(dx_list, v_ph, 's-', color='darkorange', linewidth=2,
             label='Numerical $v_p$')
    ax2.axhline(c_val, color='crimson', linestyle='--',
               linewidth=2, label=f'Theoretical $c$')
    ax2.set_xlabel(r'$\Delta x$ (m)')
    ax2.set_ylabel(r'Phase Velocity (m/s)')
    ax2.set_title('Phase Velocity vs Grid Spacing')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/tmp/taflove_dispersion_1d.png', dpi=150)
    print("[Dispersion] Plot saved to /tmp/taflove_dispersion_1d.png")
    plt.show()

    return dx_list, v_ph, error_pct


def gaussian_source(t, t0, sigma):
    """
    Gaussian pulse source function.

    Parameters
    ----------
    t     : float or ndarray – Time (s)
    t0    : float            – Center time (s)
    sigma : float            – Pulse width (s)

    Returns
    -------
    float or ndarray – Amplitude
    """
    return np.exp(-((t - t0) ** 2) / (2.0 * sigma ** 2))


def sine_wave_source(t, f_Hz, amplitude=1.0):
    """
    Sinusoidal steady-state source.

    Parameters
    ----------
    t         : float or ndarray – Time (s)
    f_Hz      : float            – Frequency (Hz)
    amplitude : float            – Amplitude (V/m)

    Returns
    -------
    float or ndarray – Amplitude
    """
    return amplitude * np.sin(2.0 * np.pi * f_Hz * t)


# ── Validation & Demo ────────────────────────────────────────────────────────
if __name__ == '__main__':
    print("=" * 60)
    print("Taflove FDTD 1D Simulator — Validation")
    print("=" * 60)

    # 1. CFL stability check
    print("\n[1] CFL Stability Check")
    dx_test = 1e-3  # 1 mm
    dt_cfl, dt_rec = CFL_stability(dx_test)

    # 2. 1D FDTD run with Gaussian pulse
    print("\n[2] 1D FDTD — Gaussian Pulse")
    Ez_g, Hy_g, t_g, x_g, dt_used = maxwell_1d(
        L=0.5, dx=1e-3, num_steps=600,
        source_type='gaussian', A=1.0,
        plot_interval=200
    )

    # 3. 1D FDTD run with sine source
    print("\n[3] 1D FDTD — Sinusoidal Source (1 GHz)")
    Ez_s, Hy_s, t_s, x_s, _ = maxwell_1d(
        L=0.5, dx=1e-3, dt=dt_used, num_steps=800,
        source_type='sine', A=1.0, f_Hz=1e9,
        plot_interval=200
    )

    # 4. Dispersion analysis
    print("\n[4] Numerical Dispersion Verification")
    dx_vals = [5e-3, 2e-3, 1e-3, 5e-4]
    dispersion_1d(dx_list=dx_vals, f_Hz=5e9, num_steps=1500)

    print("\n" + "=" * 60)
    print("Validation complete.")
    print("=" * 60)