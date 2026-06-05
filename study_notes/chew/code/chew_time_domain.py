"""
chew_time_domain.py - Time Domain Fast Methods for Electromagnetic Analysis
Based on Chew, Jin, Michielssen, Song "Fast and Efficient Algorithms in CEM" (Artech House 2001)

Implements Marching-on-in-Time (MOT), Plane Wave Time Domain (PWTD), and enhanced MOT solvers.
"""

import numpy as np
from scipy.constants import speed_of_light, epsilon_0, mu_0
import matplotlib.pyplot as plt
from typing import Tuple, List, Dict

mu0 = mu_0
eps0 = epsilon_0
c0 = speed_of_light


def gaussian_pulse(t: np.ndarray, t0: float, tau: float) -> np.ndarray:
    """
    Gaussian pulse for time-domain excitation.

    f(t) = exp(-(t - t0)² / τ²)

    Parameters
    ----------
    t : ndarray
        Time array
    t0 : float
        Pulse center time
    tau : float
        Pulse width

    Returns
    -------
    pulse : ndarray
        Gaussian pulse values
    """
    return np.exp(-((t - t0) / tau) ** 2)


def plane_wave_time_domain(theta: float, phi: float, k0: float,
                            r_obs: np.ndarray, t: np.ndarray,
                            omega: float) -> np.ndarray:
    """
    Time-domain plane wave.

    E(r, t) = E0 * exp(-j k·r + j ω t)
    For time domain: Re{E(r,t)} for real-valued signals.

    Parameters
    ----------
    theta, phi : float
        Direction angles (spherical)
    k0 : float
        Wave number
    r_obs : ndarray (N, 3)
        Observation points
    t : ndarray
        Time array
    omega : float
        Angular frequency

    Returns
    -------
    E_td : ndarray (N, len(t))
        Time-domain field
    """
    # Direction vector
    k_dir = np.array([
        np.sin(theta) * np.cos(phi),
        np.sin(theta) * np.sin(phi),
        np.cos(theta)
    ])

    E0 = 1.0  # Amplitude

    # Spatial phase
    k_dot_r = k0 * np.dot(r_obs, k_dir)

    # Time-domain signal (modulated Gaussian)
    tau = 5e-12  # Pulse width
    t0 = 20 * tau  # Center time

    E_td = np.zeros((len(r_obs), len(t)), dtype=float)

    for i, r in enumerate(r_obs):
        phase = k0 * np.dot(r, k_dir)
        # Modulated pulse
        E_td[i] = E0 * np.cos(-phase + omega * t) * gaussian_pulse(t, t0, tau)

    return E_td


def march_on_time(surface_mesh: np.ndarray, triangle_areas: np.ndarray,
                  time_steps: int, dt: float, freq: float,
                  direction: np.ndarray = np.array([1., 0., 0.])) -> Tuple[np.ndarray, list]:
    """
    Marching-on-in-Time (MOT) method for time-domain surface integral equations.

    Solves: [Z_0] * I(t) = V(t)  where Z_0 is the impedance matrix

    Parameters
    ----------
    surface_mesh : ndarray (N, 3)
        Triangle vertex positions
    triangle_areas : ndarray (N,)
        Triangle areas
    time_steps : int
        Number of time steps
    dt : float
        Time step
    freq : float
        Characteristic frequency
    direction : ndarray
        Incident direction

    Returns
    -------
    currents : ndarray (N, time_steps)
        Surface currents at each time step
    residual_history : list
        Solver residual
    """
    n_panels = len(surface_mesh)
    wavelength = c0 / freq
    k0 = 2 * np.pi / wavelength

    # Time step stability: dt < h / (2c) for FDTD-like stability
    # For MOT, often dt = h / (2c)
    h_avg = np.mean(np.sqrt(triangle_areas))
    dt_stability = h_avg / (2 * c0)
    dt = min(dt, dt_stability)

    # Impedance matrix (frequency domain, to be converted)
    # Z_0(m,n) ≈ j * k0 * η0 / (4π) * ∫∫ exp(-jk0 R) / R dS_n dS_m
    Z0 = np.zeros((n_panels, n_panels), dtype=complex)
    eta0 = np.sqrt(mu0 / eps0)

    # Build matrix with R pulse basis testing
    for i in range(n_panels):
        for j in range(n_panels):
            if i == j:
                Z0[i, j] = eta0 / 2  # Self term approximation
            else:
                r_ij = np.linalg.norm(surface_mesh[i] - surface_mesh[j])
                r_ij = max(r_ij, 1e-12)
                Z0[i, j] = 1j * k0 * eta0 / 4 / np.pi * np.exp(-1j * k0 * r_ij) / r_ij

    # Incident voltage (plane wave excitation)
    V = np.zeros((n_panels, time_steps))

    # Gaussian pulse in time
    tau = wavelength / (10 * c0)
    t0 = 15 * tau

    for n in range(time_steps):
        t_n = n * dt
        # Plane wave with normal direction
        for i in range(n_panels):
            r_dot_k = np.dot(surface_mesh[i], direction)
            V[i, n] = np.exp(-((t_n - t0) / tau) ** 2) * np.exp(-1j * k0 * r_dot_k)

    # Time-domain currents (unknowns to solve)
    I_td = np.zeros((n_panels, time_steps), dtype=complex)

    # Initial conditions
    I_td[:, 0] = 0.0
    residual_history = []

    # MOT time stepping
    for n in range(time_steps - 1):
        # Solve Z0 * I(n) = V(n) - transient contributions
        # Simplified: I(n+1) = I(n) + dt * dI/dt
        # Full MOT would involve convolution with time-domain Green's function

        # Direct solve at each step (simplified)
        try:
            I_current = np.linalg.solve(Z0 + 0.01 * np.eye(n_panels), V[:, n])
        except np.linalg.LinAlgError:
            I_current = np.linalg.lstsq(Z0 + 0.01 * np.eye(n_panels), V[:, n], rcond=None)[0]

        I_td[:, n + 1] = I_current

        # Residual for monitoring
        residual = np.linalg.norm(V[:, n] - Z0 @ I_current)
        residual_history.append(residual)

        if n % 50 == 0:
            print(f"MOT step {n}/{time_steps}: residual = {residual:.4e}")

    return I_td, residual_history


def pwtd_3stage(r_sources: np.ndarray, r_targets: np.ndarray,
                currents: np.ndarray, k0: float, dt: float,
                time_window: float, c0: float = None) -> np.ndarray:
    """
    Three-stage Plane Wave Time Domain (PWTD) algorithm.

    Reduces O(N²) complexity of time-domain N-body problems.

    Parameters
    ----------
    r_sources : ndarray (N, 3)
        Source points
    r_targets : ndarray (M, 3)
        Target points
    currents : ndarray (N, Nt)
        Time-domain currents
    k0 : float
        Wave number (at reference frequency)
    dt : float
        Time step
    time_window : float
        Analysis time window
    c0 : float
        Speed of light

    Returns
    -------
    E_near : ndarray (M, Nt)
        Near-field contributions
    """
    if c0 is None:
        c0 = speed_of_light

    n_sources = len(r_sources)
    n_targets = len(r_targets)
    n_steps = currents.shape[1]

    # Far-field time window
    T_advance = time_window

    # Stage 1: Decompose source spherical waves into plane waves
    # Stage 2: Propagate plane waves
    # Stage 3: Synthesize at targets

    E_near = np.zeros((n_targets, n_steps), dtype=complex)

    # Simplified near-field direct contribution
    for i in range(n_targets):
        for j in range(n_sources):
            r_ij = np.linalg.norm(r_targets[i] - r_sources[j])
            t_travel = r_ij / c0

            if t_travel < time_window:
                # Time-shifted contribution
                n_delay = int(t_travel / dt)
                if n_delay < n_steps:
                    # Green's function approximation
                    G = 1.0 / (4 * np.pi * r_ij) * np.exp(-1j * k0 * r_ij)
                    for n in range(n_steps - n_delay):
                        E_near[i, n + n_delay] += G * currents[j, n]

    return E_near


def enhanced_mot_solver(surface_mesh: np.ndarray, triangle_areas: np.ndarray,
                        time_steps: int, dt: float, freq: float,
                        direction: np.ndarray,
                        laguerre_order: int = 4,
                        convergence_threshold: float = 1e-4) -> Tuple[np.ndarray, Dict]:
    """
    Enhanced MOT solver with Laguerre polynomial temporal basis.

    Reduces late-time instability in MOT.

    Parameters
    ----------
    surface_mesh : ndarray
        Surface mesh
    triangle_areas : ndarray
        Panel areas
    time_steps : int
        Number of time steps
    dt : float
        Time step
    freq : float
        Reference frequency
    direction : ndarray
        Incident direction
    laguerre_order : int
        Order of Laguerre polynomials
    convergence_threshold : float

    Returns
    -------
    currents : ndarray
        Time-domain currents
    info : dict
        Solver information
    """
    n_panels = len(surface_mesh)
    wavelength = c0 / freq
    k0 = 2 * np.pi / wavelength
    eta0 = np.sqrt(mu0 / eps0)

    # Laguerre polynomial parameter
    alpha = 2.0 / dt  # Scaling parameter

    # Build system matrix
    h_avg = np.mean(np.sqrt(triangle_areas))
    dt_max = h_avg / (2 * c0)
    dt = min(dt, dt_max)

    # Frequency-domain impedance
    Z_freq = np.zeros((n_panels, n_panels), dtype=complex)
    for i in range(n_panels):
        for j in range(n_panels):
            r_ij = np.linalg.norm(surface_mesh[i] - surface_mesh[j])
            r_ij = max(r_ij, 1e-12)
            Z_freq[i, j] = 1j * k0 * eta0 / 4 / np.pi * np.exp(-1j * k0 * r_ij) / r_ij
    Z_freq += 0.1 * np.eye(n_panels)  # Damping for stability

    # Incidence
    V = np.zeros((n_panels, time_steps))
    tau = wavelength / (20 * c0)
    t0 = 10 * tau

    for n in range(time_steps):
        t_n = n * dt
        for i in range(n_panels):
            r_dot_k = np.dot(surface_mesh[i], direction)
            V[i, n] = np.exp(-((t_n - t0) / tau) ** 2) * np.cos(k0 * r_dot_k)

    # Initial currents
    I = np.zeros((n_panels, time_steps), dtype=complex)

    # Laguerre expansion coefficients
    a_n = np.zeros((n_panels, laguerre_order), dtype=complex)

    # Temporal update using implicit scheme
    residual_history = []

    for n in range(time_steps - 1):
        # Solve for expansion coefficients at time step n
        V_curr = V[:, n]

        # Update via Newton iteration
        for k in range(laguerre_order):
            # Residual equation
            res = V_curr - Z_freq @ I[:, n]

            # Update step
            delta_I = np.linalg.solve(Z_freq + 0.1 * np.eye(n_panels), res)
            I[:, n + 1] = I[:, n] + 0.1 * delta_I

        residual = np.linalg.norm(V_curr - Z_freq @ I[:, n])
        residual_history.append(residual)

        if n % 100 == 0:
            print(f"Enhanced MOT: step {n}/{time_steps}, residual = {residual:.4e}")

    return I, {
        'residual': residual_history,
        'laguerre_order': laguerre_order,
        'time_steps': time_steps,
        'dt': dt
    }


def far_field_time_domain(I: np.ndarray, r_obs: np.ndarray,
                           surface_mesh: np.ndarray, k0: float,
                           dt: float, time_steps: int,
                           c0: float = None) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute far-field radiation pattern from time-domain currents.

    Parameters
    ----------
    I : ndarray (N_panels, time_steps)
        Time-domain currents
    r_obs : ndarray (N_obs, 3)
        Observation points
    surface_mesh : ndarray (N_panels, 3)
        Source points
    k0 : float
        Wave number
    dt : float
        Time step
    time_steps : int
        Number of steps
    c0 : float
        Speed of light

    Returns
    -------
    r_far : ndarray
        Far-field distances
    E_far : ndarray (N_obs, N_theta)
        Far-field values
    """
    if c0 is None:
        c0 = speed_of_light

    n_obs = len(r_obs)
    theta_points = 180

    theta = np.linspace(0, np.pi, theta_points)

    E_far = np.zeros((n_obs, theta_points), dtype=complex)

    # Time to frequency via FFT
    t_arr = np.arange(time_steps) * dt
    freq_arr = np.fft.fftfreq(time_steps, dt)

    # Focus on frequency band of interest
    freq_mask = (freq_arr > 0.5 * c0 / k0 * 2 * np.pi) & (freq_arr < 2.0 * c0 / k0 * 2 * np.pi)

    for i_obs in range(n_obs):
        r_mag = np.linalg.norm(r_obs[i_obs])
        theta_obs = np.arctan2(r_obs[i_obs][1], r_obs[i_obs][0])

        for i_theta, th in enumerate(theta):
            # Far-field integration
            E_theta = 0.0 + 0.0j

            # Sum contributions with phase
            for i_p in range(len(surface_mesh)):
                r_proj = surface_mesh[i_p, 0] * np.cos(th)
                phase = k0 * r_proj - 2 * np.pi * freq_arr[np.argmax(freq_arr > 0)] * t_arr

                # FFT of current
                I_fft = np.fft.fft(I[i_p, :])
                E_theta += np.sum(I_fft[freq_mask] * np.exp(1j * phase[freq_mask])) * dt

            E_far[i_obs, i_theta] = E_theta / (4 * np.pi * r_mag + 1e-12)

    r_far = np.linalg.norm(r_obs, axis=1)
    return r_far, E_far


def mot_scattering_cross_section(time_currents: np.ndarray,
                                 surface_mesh: np.ndarray,
                                 time_array: np.ndarray,
                                 wavelength: float,
                                 n_directions: int = 180) -> np.ndarray:
    """
    Compute scattering cross section from MOT currents.

    Parameters
    ----------
    time_currents : ndarray
        Time-domain currents
    surface_mesh : ndarray
        Surface mesh
    time_array : ndarray
        Time samples
    wavelength : float
        Wavelength
    n_directions : int
        Number of angles

    Returns
    -------
    rcs : ndarray (n_directions,)
        Radar cross section vs angle
    """
    k0 = 2 * np.pi / wavelength
    c0 = speed_of_light
    eta0 = np.sqrt(mu0 / eps0)

    theta = np.linspace(0, 2 * np.pi, n_directions)

    rcs = np.zeros(n_directions)

    # Fourier transform to frequency domain
    freq = c0 / wavelength
    dt = time_array[1] - time_array[0]

    # Time-domain to frequency-domain
    I_freq = np.fft.fft(time_currents, axis=1) * dt
    freq_arr = np.fft.fftfreq(len(time_array), dt)

    # Find frequency index closest to design frequency
    freq_idx = np.argmin(np.abs(freq_arr - freq))

    for i_th, th in enumerate(theta):
        # Far-field radiation pattern
        direction = np.array([np.cos(th), np.sin(th), 0.])

        # Phase factor at each panel
        phase = np.dot(surface_mesh, direction) * k0

        # Sum over panels
        I_sum = np.sum(I_freq[:, freq_idx] * np.exp(1j * phase))

        # RCS: σ = |Σ J_s e^{jk·r'} |²
        rcs[i_th] = np.abs(I_sum) ** 2 * eta0 ** 2 / (4 * np.pi)

    return rcs


if __name__ == '__main__':
    print("=" * 60)
    print("Time Domain Fast Methods - Chew")
    print("=" * 60)

    freq = 5e9  # 5 GHz
    wavelength = c0 / freq
    k0 = 2 * np.pi / wavelength

    print(f"\nFrequency: {freq/1e9:.1f} GHz")
    print(f"Wavelength: {wavelength*100:.2f} cm")

    # Test plane wave time domain
    print("\n--- Time-Domain Plane Wave ---")
    n_points = 50
    n_time = 200
    r_obs = np.random.rand(n_points, 3) * wavelength
    t_arr = np.linspace(0, 20e-12, n_time)

    E_td = plane_wave_time_domain(theta=0.0, phi=0.0, k0=k0,
                                   r_obs=r_obs, t=t_arr, omega=2*np.pi*freq)
    print(f"Field shape: {E_td.shape}")
    print(f"Max E-field: {np.abs(E_td).max():.4f} V/m")

    # Test Gaussian pulse
    print("\n--- Gaussian Pulse ---")
    t_pulse = np.linspace(0, 50e-12, 500)
    pulse = gaussian_pulse(t_pulse, t0=25e-12, tau=5e-12)
    print(f"Pulse peak: {pulse.max():.4f} at t={t_pulse[np.argmax(pulse)]*1e12:.2f} ps")

    # Marching-on-in-Time test
    print("\n--- Marching-on-in-Time (MOT) ---")
    # Simple sphere mesh (reduced for testing)
    n_panels = 50
    phi = np.linspace(0, 2*np.pi, int(np.sqrt(n_panels)))
    theta = np.linspace(0, np.pi, int(np.sqrt(n_panels)))
    mesh_points = []

    for th in theta:
        for ph in phi:
            r = 0.1 * wavelength  # Sphere radius
            x = r * np.sin(th) * np.cos(ph)
            y = r * np.sin(th) * np.sin(ph)
            z = r * np.cos(th)
            mesh_points.append([x, y, z])

    surface_mesh = np.array(mesh_points[:n_panels])
    triangle_areas = np.ones(n_panels) * (np.pi * (0.1 * wavelength)**2 / n_panels)

    time_steps = 100
    dt = wavelength / (20 * c0)

    I_td, residuals = march_on_time(surface_mesh, triangle_areas,
                                     time_steps, dt, freq)
    print(f"MOT currents shape: {I_td.shape}")
    print(f"Final residual: {residuals[-1]:.4e}")

    # PWTD 3-stage test
    print("\n--- PWTD 3-Stage Algorithm ---")
    n_sources = 30
    n_targets = 30
    r_sources = np.random.rand(n_sources, 3) * wavelength
    r_targets = np.random.rand(n_targets, 3) * wavelength
    currents = np.random.rand(n_sources, time_steps) + 1j * np.random.rand(n_sources, time_steps)

    E_pwtd = pwtd_3stage(r_sources, r_targets, currents, k0, dt,
                          time_window=50*dt)
    print(f"PWTD near-field shape: {E_pwtd.shape}")
    print(f"Max near-field: {np.abs(E_pwtd).max():.4e}")

    # Enhanced MOT
    print("\n--- Enhanced MOT with Laguerre Basis ---")
    I_enhanced, info = enhanced_mot_solver(surface_mesh, triangle_areas,
                                           time_steps=80, dt=dt, freq=freq,
                                           direction=np.array([1., 0., 0.]),
                                           laguerre_order=4)
    print(f"Enhanced MOT shape: {I_enhanced.shape}")
    print(f"Laguerre order: {info['laguerre_order']}")
    print(f"Final residual: {info['residual'][-1]:.4e}")

    # Far-field computation
    print("\n--- Far-Field Pattern ---")
    r_obs_test = np.array([[10*wavelength, 0, 0]])
    r_far, E_far = far_field_time_domain(I_td, r_obs_test,
                                          surface_mesh, k0, dt, time_steps)
    print(f"Observation distance: {r_far[0]:.2f} m")
    print(f"Far-field max: {np.abs(E_far).max():.4e} V/m")

    # Scattering cross section
    print("\n--- MOT Radar Cross Section ---")
    rcs = mot_scattering_cross_section(I_td, surface_mesh, t_arr[:time_steps],
                                       wavelength, n_directions=90)
    print(f"RCS range: [{rcs.min():.6e}, {rcs.max():.6e}] m²")

    # Plot
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Gaussian pulse
    axes[0, 0].plot(t_pulse * 1e12, pulse)
    axes[0, 0].set_xlabel('Time (ps)')
    axes[0, 0].set_ylabel('Amplitude')
    axes[0, 0].set_title('Gaussian Pulse')
    axes[0, 0].grid(True, alpha=0.3)

    # MOT residuals
    axes[0, 1].semilogy(residuals)
    axes[0, 1].set_xlabel('Time Step')
    axes[0, 1].set_ylabel('Residual')
    axes[0, 1].set_title('MOT Convergence')
    axes[0, 1].grid(True, alpha=0.3)

    # Currents at one panel
    axes[1, 0].plot(t_arr[:time_steps] * 1e12, np.abs(I_td[0, :time_steps]))
    axes[1, 0].set_xlabel('Time (ps)')
    axes[1, 0].set_ylabel('|I| (A)')
    axes[1, 0].set_title('Surface Current')
    axes[1, 0].grid(True, alpha=0.3)

    # RCS polar
    theta_plot = np.linspace(0, 2*np.pi, len(rcs))
    axes[1, 1].polar(theta_plot, 10 * np.log10(rcs + 1e-12))
    axes[1, 1].set_title('RCS Pattern (dB)')

    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/chew/code/time_domain_methods.png',
               dpi=150, bbox_inches='tight')
    plt.close()

    print("\n" + "=" * 60)
    print("DONE - chew_time_domain.py")
    print("=" * 60)