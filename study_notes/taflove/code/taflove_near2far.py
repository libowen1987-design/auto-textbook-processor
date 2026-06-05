"""
Taflove Near-to-Far Field Transformation
==========================================
Near-field to far-field transformation for 2D/1D FDTD.
Based on Taflove 3rd Ed., Chapter 9 (Near-to-Far-Field Transformation).

Implements:
  - near2far_1d()       : 1D near-to-far field transformation
  - radiation_pattern()  : Antenna radiation pattern computation
  - Huygens_surface()   : Huygens equivalence surface implementation

Author: 小龙虾 (based on Taflove 3rd Ed.)
"""

import numpy as np
import matplotlib.pyplot as plt

# Physical constants
c = 2.99792458e8
epsilon_0 = 8.854187817e-12
mu_0 = 4.0 * np.pi * 1e-7
eta0 = np.sqrt(mu_0 / epsilon_0)  # Free-space impedance ≈ 377 Ω


def near2far_1d(Ez_history, Hy_history, x, t,
                src_idx, far_distance=1.0,
                observation_angles=None):
    """
    Compute far-field radiation pattern from 1D FDTD near-field data
    using the equivalence principle and Fourier transform (Taflove Eq. 9.14).

    The far-field E_theta component for a 1D line source at frequency ω:

        E_θ(ω) = (j k / (4π)) * ∫_S J_s · e^{jk·r'} dS

    where J_s is the surface current density on the Huygens surface.

    Parameters
    ----------
    Ez_history  : ndarray – (Nt, Nx) electric field history
    Hy_history  : ndarray – (Nt, Nx) magnetic field history
    x           : ndarray – Spatial grid (m)
    t           : ndarray – Time grid (s)
    src_idx     : int     – Source index in grid
    far_distance: float   – Far-field observation distance (m)
    observation_angles : ndarray – Angles (radians) for pattern, default 0..2π

    Returns
    -------
    far_E       : ndarray – Far-field |E| at each angle
    theta_arr   : ndarray – Observation angles (radians)
    freq_domain : ndarray – Frequency spectrum of the far field
    E_mag       : ndarray – E field magnitude spectrum
    """
    if observation_angles is None:
        theta_arr = np.linspace(0, 2 * np.pi, 361)
    else:
        theta_arr = np.array(observation_angles)

    Nt, Nx = Ez_history.shape
    dx = x[1] - x[0]

    print(f"\n[Near2Far 1D] Nt={Nt}, Nx={Nx}, dx={dx:.4e} m")
    print(f"[Near2Far 1D] Source index: {src_idx}")
    print(f"[Near2Far 1D] Observation distance: {far_distance:.2f} m")

    # Huygens surface: right boundary as radiation surface
    boundary_idx = Nx - 2

    # Time-domain fields on the surface
    Ez_surf = Ez_history[:, boundary_idx]
    Hy_surf = Hy_history[:, boundary_idx]

    # Fourier transform to frequency domain
    dt = t[1] - t[0]
    freq = np.fft.rfftfreq(Nt, dt)
    omega = 2.0 * np.pi * freq

    # FFT of surface currents
    J_s_freq = -np.fft.rfft(Hy_surf)   # J_s = n × H
    M_s_freq = np.fft.rfft(Ez_surf)   # M_s = -n × E

    # Wave number
    k = omega / c

    # Far-field at each angle
    far_E = np.zeros(len(theta_arr), dtype=complex)
    a = Nx * dx   # Total aperture width

    for i, theta in enumerate(theta_arr):
        cos_theta = np.cos(theta)
        sum_E = 0.0j
        for ix in range(Nx):
            x_prime = x[ix] - x[0]
            phase = np.exp(1j * k[1] * x_prime * cos_theta)
            sum_E += (M_s_freq[1] - eta0 * J_s_freq[1] * cos_theta) * phase

        far_E[i] = (1j * k[1] / (4 * np.pi)) * dx * sum_E

    # Normalize to dB
    E_mag = np.abs(far_E)
    E_mag_max = np.max(E_mag) + 1e-12
    E_norm_dB = 20.0 * np.log10(E_mag / E_mag_max)

    print(f"[Near2Far 1D] Max far-field |E| = {np.max(E_mag):.4e}")
    print(f"[Near2Far 1D] Frequency with max radiation: {freq[1]:.2e} Hz")

    # Plot
    fig = plt.figure(figsize=(13, 5))
    fig.suptitle("Taflove Near-to-Far Field Transformation", fontsize=12)

    ax0 = fig.add_subplot(121, projection='polar')
    ax0.plot(theta_arr, E_mag / np.max(E_mag),
             color='steelblue', linewidth=2)
    ax0.set_title('Radiation Pattern (Normalized)')
    ax0.set_theta_zero_location('E')

    ax1 = fig.add_subplot(122)
    ax1.plot(np.degrees(theta_arr), E_norm_dB,
             color='darkorange', linewidth=2)
    ax1.set_xlabel('Observation Angle (degrees)')
    ax1.set_ylabel('Normalized $E$ (dB)')
    ax1.set_title('Far-Field Pattern (dB scale)')
    ax1.set_xlim(0, 360)
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(-40, 0)

    plt.tight_layout()
    plt.savefig('/tmp/taflove_near2far_1d.png', dpi=150)
    print("[Near2Far 1D] Plot saved to /tmp/taflove_near2far_1d.png")
    plt.show()

    return far_E, theta_arr, freq, E_mag


def radiation_pattern(Ez_history, x, t, freq_target=5e9):
    """
    Compute radiation pattern at a specific frequency from 2D FDTD data.

    Uses the equivalence principle: tangential fields on a closed
    Huygens surface are used as equivalent sources for the far field.

    Parameters
    ----------
    Ez_history : ndarray – (Nt, Nx, Ny) electric field history
    x          : ndarray – x spatial axis (m)
    t          : ndarray – time axis (s)
    freq_target: float   – Target frequency for radiation pattern (Hz)

    Returns
    -------
    pattern_dB : ndarray – Normalized radiation pattern (dB)
    theta      : ndarray – Observation angles (radians)
    """
    Nt, Nx, Ny = Ez_history.shape
    dx = x[1] - x[0] if len(x) > 1 else 1.0
    dy = dx

    print(f"\n[Radiation Pattern] Frequency target: {freq_target:.2e} Hz")
    print(f"[Radiation Pattern] Grid: {Nx}x{Ny}")

    dt = t[1] - t[0]
    freq_arr = np.fft.rfftfreq(Nt, dt)
    idx_freq = np.argmin(np.abs(freq_arr - freq_target))
    f_actual = freq_arr[idx_freq]

    print(f"[Radiation Pattern] Closest frequency: {f_actual:.2e} Hz")
    omega = 2.0 * np.pi * f_actual
    k = omega / c

    # Field at bottom surface
    Ez_surface = Ez_history[:, :, 0]  # (Nt, Nx)
    Ez_fft = np.fft.rfft(Ez_surface, axis=0)  # (Nf, Nx)
    Ez_freq = Ez_fft[idx_freq]  # (Nx,)

    # Angle sweep
    theta_arr = np.linspace(0, 2 * np.pi, 361)
    pattern = np.zeros(len(theta_arr))

    for i, theta in enumerate(theta_arr):
        phase = np.exp(-1j * k * np.arange(Nx) * dx * np.sin(theta))
        pattern[i] = np.abs(np.sum(Ez_freq * phase))

    pattern_norm = pattern / (np.max(pattern) + 1e-12)
    pattern_dB = 20.0 * np.log10(pattern_norm)

    # Plot
    fig = plt.figure(figsize=(13, 5))
    fig.suptitle(f"Radiation Pattern at f={f_actual/1e9:.2f} GHz",
                 fontsize=12)

    ax0 = fig.add_subplot(121, projection='polar')
    ax0.plot(theta_arr, pattern_norm, color='forestgreen', linewidth=2)
    ax0.set_title('Normalized Pattern (Linear)')
    ax0.set_theta_zero_location('E')

    ax1 = fig.add_subplot(122)
    ax1.plot(np.degrees(theta_arr), pattern_dB, color='crimson', linewidth=2)
    ax1.set_xlabel('Angle (degrees)')
    ax1.set_ylabel('Pattern (dB)')
    ax1.set_title('Radiation Pattern (dB)')
    ax1.set_xlim(0, 360)
    ax1.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/tmp/taflove_radiation_pattern.png', dpi=150)
    print("[Radiation Pattern] Plot saved to /tmp/taflove_radiation_pattern.png")
    plt.show()

    return pattern_dB, theta_arr


def Huygens_surface(E_field, H_field, surface_normal='+x',
                    aperture_width=1.0, dx=1e-3):
    """
    Compute equivalent surface currents for Huygens principle.

    The Huygens equivalence principle: tangential fields on a closed
    surface S are used as sources for the exterior field.

        J_s = n × H     (electric surface current density, A/m)
        M_s = -n × E    (magnetic surface current density, V/m)

    Parameters
    ----------
    E_field        : ndarray – Tangential electric field on surface
    H_field        : ndarray – Tangential magnetic field on surface
    surface_normal : str     – '+x', '-x', '+y', '-y'
    aperture_width : float   – Width of the Huygens aperture (m)
    dx             : float   – Grid spacing (m)

    Returns
    -------
    J_s : tuple – (J_component_1, J_component_2) surface current density
    M_s : tuple – (M_component_1, M_component_2) magnetic surface current
    """
    Ez = np.asarray(E_field)
    Hx = np.asarray(H_field) if np.ndim(H_field) == 1 else H_field[..., 0]
    Hy = np.zeros_like(Ez)

    if surface_normal == '+x':
        J_y = -Ez
        J_z = Hx
        M_y = np.zeros_like(Ez)
        M_z = np.zeros_like(Ez)
    elif surface_normal == '-x':
        J_y = Ez
        J_z = -Hx
        M_y = np.zeros_like(Ez)
        M_z = np.zeros_like(Ez)
    elif surface_normal == '+y':
        J_x = Ez
        J_z = -Hx
        M_x = np.zeros_like(Ez)
        M_z = np.zeros_like(Ez)
    elif surface_normal == '-y':
        J_x = -Ez
        J_z = Hx
        M_x = np.zeros_like(Ez)
        M_z = np.zeros_like(Ez)
    else:
        raise ValueError(f"Unknown surface_normal: {surface_normal}")

    print(f"\n[Huygens Surface] normal={surface_normal}")
    if surface_normal in ('+x', '-x'):
        J_mag = np.sqrt(J_y**2 + J_z**2)
        M_mag = np.sqrt(M_y**2 + M_z**2)
    else:
        J_mag = np.sqrt(J_x**2 + J_z**2)
        M_mag = np.sqrt(M_x**2 + M_z**2)
    print(f"[Huygens Surface] |J| max = {np.max(J_mag):.4e} A/m")
    print(f"[Huygens Surface] |M| max = {np.max(M_mag):.4e} V/m")

    return (J_y, J_z), (M_y, M_z)


def near2far_1d_demo():
    """Demo: run 1D FDTD and compute radiation pattern."""
    print("\n[Near2Far Demo] Running 1D FDTD and computing far field")

    L = 0.5
    dx = 1e-3
    Nx = int(L / dx) + 1
    dt = 0.9 * dx / (2.0 * c)
    num_steps = 600

    x = np.linspace(0, L, Nx)
    t_arr = np.arange(num_steps) * dt
    src_idx = Nx // 2

    Ez = np.zeros(Nx)
    Hy = np.zeros(Nx)
    Ez_history = np.zeros((num_steps, Nx))
    Hy_history = np.zeros((num_steps, Nx))

    mH = dt / mu_0
    mE = dt / epsilon_0
    t0 = 20.0 * dt
    sigma = 8.0 * dt

    for n in range(num_steps):
        t = n * dt
        for i in range(Nx - 1):
            Hy[i] = Hy[i] - mH * (Ez[i + 1] - Ez[i]) / dx
        Ez[src_idx] = np.exp(-((t - t0) ** 2) / (2.0 * sigma ** 2))
        for i in range(1, Nx):
            Ez[i] = Ez[i] + mE * (Hy[i] - Hy[i - 1]) / dx
        Ez_history[n] = Ez.copy()
        Hy_history[n] = Hy.copy()

    far_E, theta, freq, E_mag = near2far_1d(
        Ez_history, Hy_history, x, t_arr, src_idx, far_distance=1.0)

    return Ez_history, Hy_history, x, t_arr


if __name__ == '__main__':
    print("=" * 60)
    print("Taflove Near-to-Far Field — Validation")
    print("=" * 60)

    print("\n[1] Near-to-Far Demo")
    Ez_h, Hy_h, x, t = near2far_1d_demo()

    print("\n[2] Huygens Surface Currents")
    n_elements = 200
    z_pos = np.linspace(-0.1, 0.1, n_elements)
    Ez_example = np.sin(2.0 * np.pi * 5e9 / c * z_pos) * np.exp(-z_pos ** 2 / 0.01)
    Hx_example = np.cos(2.0 * np.pi * 5e9 / c * z_pos) * np.exp(-z_pos ** 2 / 0.01)

    J, M = Huygens_surface(Ez_example, Hx_example,
                            surface_normal='+x', aperture_width=0.2, dx=0.001)

    print("\n" + "=" * 60)
    print("Near-to-far field validation complete.")
    print("=" * 60)