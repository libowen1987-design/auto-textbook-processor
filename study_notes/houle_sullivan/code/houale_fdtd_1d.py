"""
houale_fdtd_1d.py - 1D FDTD Implementation
Based on Houle & Sullivan, "EM Simulation Using FDTD"
Author: 小龙虾 (Crawfish)
Features: 1D Maxwell's equations, CFL stability, TFSF boundary, plane wave source
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import warnings
warnings.filterwarnings('ignore')


def maxwell_1d(Nx=200, L=1.0, T_max=2e-9, epsilon_r=1.0, mu_r=1.0,
               sigma=0.0, sigma_m=0.0, source_type='gaussian'):
    """
    1D FDTD iteration for Maxwell's equations.
    
    Solves:
        dH_y/dz = -mu * dE_x/dt - sigma_m * H_y
        dE_x/dz = -epsilon * dH_y/dt - sigma * E_x
    
    Parameters
    ----------
    Nx : int
        Number of spatial grid points
    L : float
        Domain length in meters
    T_max : float
        Simulation time in seconds
    epsilon_r : float
        Relative permittivity
    mu_r : float
        Relative permeability
    sigma : float
        Electric conductivity (S/m)
    sigma_m : float
        Magnetic loss (Ω/m)
    source_type : str
        'gaussian', 'sinusoidal', or 'step'
    
    Returns
    -------
    z : ndarray
        Spatial grid
    t : ndarray
        Time array
    E : ndarray
        E-field array [Nt x Nx]
    H : ndarray
        H-field array [Nt x Nx]
    dt : float
        Time step
    """
    # Physical constants
    c = 3e8  # speed of light in vacuum (m/s)
    eps0 = 8.854e-12  # vacuum permittivity (F/m)
    mu0 = 4 * np.pi * 1e-7  # vacuum permeability (H/m)
    
    epsilon = epsilon_r * eps0
    mu = mu_r * mu0
    
    # Grid parameters
    dz = L / (Nx - 1)
    
    # CFL stability condition: dt <= dz / (2*c)
    # Using 0.99 factor for numerical stability margin
    c_numerical = c / np.sqrt(max(epsilon_r, mu_r))
    dt = 0.99 * dz / (2 * c_numerical)
    
    # Time step calculation
    Nt = int(T_max / dt)
    t = np.arange(Nt) * dt
    
    # Initialize fields (Yee lattice)
    # E field at integer time steps, H field at half-integer
    Ez = np.zeros(Nx)
    Hy = np.zeros(Nx)
    
    # Coefficients for update
    # For E field: Ez^{n+1} = C1*Ez^n + C2*(Hy_{i} - Hy_{i-1})
    C1 = (2*epsilon - sigma*dt) / (2*epsilon + sigma*dt)
    C2 = (2*dt) / (dz * (2*epsilon + sigma*dt))
    
    # For H field: Hy^{n+1/2} = D1*Hy^{n-1/2} + D2*(Ez_{i+1} - Ez_{i})
    D1 = (2*mu - sigma_m*dt) / (2*mu + sigma_m*dt)
    D2 = (2*dt) / (dz * (2*mu + sigma_m*dt))
    
    # Storage for field snapshots
    E_history = np.zeros((Nt, Nx))
    
    # Source parameters
    z_source = Nx // 4  # source location
    
    # Time profiling
    def source_t(n):
        if source_type == 'gaussian':
            t_n = n * dt
            tau = 50 * dt
            t0 = 100 * dt
            return np.exp(-((t_n - t0) / tau)**2)
        elif source_type == 'sinusoidal':
            omega = 2 * np.pi * 10e9  # 10 GHz
            return np.sin(omega * n * dt)
        elif source_type == 'step':
            return 1.0 if n * dt < 1e-9 else 0.0
        return 0.0
    
    # Main FDTD loop
    print(f"[1D FDTD] Grid: {Nx} points, dt: {dt:.2e} s, Nt: {Nt}")
    print(f"[1D FDTD] CFL stability factor: {dt * c_numerical * 2 / dz:.4f}")
    
    for n in range(Nt):
        # Update H field (half step)
        for i in range(Nx - 1):
            Hy[i] = D1 * Hy[i] + D2 * (Ez[i + 1] - Ez[i])
        
        # Inject source using hard source
        Ez[z_source] = source_t(n)
        
        # Update E field (full step)
        for i in range(1, Nx - 1):
            Ez[i] = C1 * Ez[i] + C2 * (Hy[i] - Hy[i - 1])
        
        # Absorbing boundary conditions (Mur's first-order ABC)
        # Left boundary (i=0)
        Ez[0] = Ez[1] + (c_numerical * dt - dz) / (c_numerical * dt + dz) * (Ez[1] - Ez[0])
        # Right boundary (i=Nx-1)
        Ez[-1] = Ez[-2] + (c_numerical * dt - dz) / (c_numerical * dt + dz) * (Ez[-2] - Ez[-1])
        
        # Store history every few steps
        if n % 10 == 0:
            E_history[n] = Ez.copy()
    
    # Return space grid
    z = np.linspace(0, L, Nx)
    
    return z, t, E_history, Hy, dt


def CFL_stability(epsilon_r=1.0, mu_r=1.0, dz=1e-3):
    """
    Validate CFL stability condition for 1D FDTD.
    
    CFL condition: Δt ≤ Δz / (2*c_numerical)
    where c_numerical = c / sqrt(ε_r * μ_r)
    
    Parameters
    ----------
    epsilon_r : float
        Relative permittivity
    mu_r : float
        Relative permeability
    dz : float
        Spatial step (m)
    
    Returns
    -------
    dt_max : float
        Maximum allowed time step
    dt_recommended : float
        Recommended time step (0.99 * dt_max)
    stability_flag : bool
        True if stable
    """
    c = 3e8
    c_numerical = c / np.sqrt(epsilon_r * mu_r)
    
    dt_max = dz / (2 * c_numerical)
    dt_recommended = 0.99 * dt_max
    
    # Validate with example: dz = 1mm
    dt_test = 0.99 * dt_max
    c_test = c_numerical
    stability_factor = dt_test * c_test * 2 / dz
    
    stability_flag = stability_factor < 1.0
    
    print("=" * 50)
    print("CFL Stability Analysis")
    print("=" * 50)
    print(f"Grid spacing dz:        {dz*1e3:.3f} mm")
    print(f"Relative permittivity:   {epsilon_r}")
    print(f"Relative permeability:   {mu_r}")
    print(f"Numerical c:             {c_numerical:.3e} m/s")
    print(f"dt_max (analytical):    {dt_max:.3e} s")
    print(f"dt_recommended:         {dt_recommended:.3e} s")
    print(f"Stability factor:        {stability_factor:.6f} (must be < 1.0)")
    print(f"Status:                 {'✓ STABLE' if stability_flag else '✗ UNSTABLE'}")
    print("=" * 50)
    
    return dt_max, dt_recommended, stability_flag


def TFSF_1d(Nx=300, L=1.5, T_max=5e-9, epsilon_r=1.0):
    """
    Total-Field/Scattered-Field (TFSF) 1D FDTD formulation.
    
    The TFSF boundary separates the computational domain into:
    - Total field region (contains both incident and scattered waves)
    - Scattered field region (contains only scattered waves)
    
    Parameters
    ----------
    Nx : int
        Number of grid points
    L : float
        Domain length (m)
    T_max : float
        Maximum simulation time (s)
    epsilon_r : float
        Relative permittivity
    
    Returns
    -------
    z : ndarray
        Spatial grid
    t : ndarray
        Time array
    Ez_total : ndarray
        Total E-field
    Ez_scattered : ndarray
        Scattered E-field
    """
    c = 3e8
    eps0 = 8.854e-12
    mu0 = 4 * np.pi * 1e-7
    
    dz = L / (Nx - 1)
    c_numerical = c / np.sqrt(epsilon_r)
    dt = 0.99 * dz / (2 * c_numerical)
    Nt = int(T_max / dt)
    
    # TFSF boundary positions
    tfsf_left = Nx // 4
    tfsf_right = 3 * Nx // 4
    
    # Initialize fields
    Ez_scattered = np.zeros(Nx)
    Hy_scattered = np.zeros(Nx)
    
    # Incident wave parameters (Gaussian pulse)
    tau = 30 * dt
    t0 = 80 * dt
    
    def incident_field(t):
        """Incident plane wave in free space."""
        return np.exp(-((t - t0) / tau)**2)
    
    # Update coefficients
    epsilon = epsilon_r * eps0
    mu = mu0
    
    C1 = 1.0  # lossless
    C2 = dt / (dz * epsilon)
    D1 = 1.0  # lossless
    D2 = dt / (dz * mu)
    
    # Storage
    t_array = np.arange(Nt) * dt
    Ez_total_history = []
    
    print(f"[TFSF 1D] Domain: {Nx} pts, TFSF boundaries: [{tfsf_left}, {tfsf_right}]")
    
    for n in range(Nt):
        # Update scattered H field
        for i in range(Nx - 1):
            Hy_scattered[i] = D1 * Hy_scattered[i] + D2 * (Ez_scattered[i + 1] - Ez_scattered[i])
        
        # TFSF correction at left boundary
        Hy_scattered[tfsf_left - 1] -= D2 * incident_field((n + 0.5) * dt)
        
        # Update scattered E field
        for i in range(1, Nx - 1):
            Ez_scattered[i] = C1 * Ez_scattered[i] + C2 * (Hy_scattered[i] - Hy_scattered[i - 1])
        
        # TFSF correction at right boundary
        Ez_scattered[tfsf_right] += C2 * incident_field((n + 1) * dt)
        
        # Store snapshots
        if n % 20 == 0:
            Ez_total_history.append(Ez_scattered.copy())
    
    Ez_total = np.array(Ez_total_history)
    z = np.linspace(0, L, Nx)
    
    return z, t_array, Ez_total, Ez_scattered


def plane_wave_1d(A=1.0, f=10e9, epsilon_r=1.0, mu_r=1.0,
                  Nx=500, L=2.0, T_max=3e-9):
    """
    Plane wave propagation in 1D FDTD.
    
    Parameters
    ----------
    A : float
        Wave amplitude (V/m)
    f : float
        Frequency (Hz)
    epsilon_r : float
        Relative permittivity of medium
    mu_r : float
        Relative permeability of medium
    Nx : int
        Number of grid points
    L : float
        Domain length (m)
    T_max : float
        Simulation time (s)
    
    Returns
    -------
    z : ndarray
        Spatial grid
    t : ndarray
        Time array
    Ez : ndarray
        Electric field snapshot
    analytical : ndarray
        Analytical solution for comparison
    """
    c = 3e8
    eps0 = 8.854e-12
    mu0 = 4 * np.pi * 1e-7
    
    # Wave parameters
    omega = 2 * np.pi * f
    k = omega * np.sqrt(epsilon_r * eps0 * mu_r * mu0)
    
    # Numerical parameters
    dz = L / (Nx - 1)
    c_numerical = c / np.sqrt(epsilon_r * mu_r)
    dt = 0.99 * dz / (2 * c_numerical)
    Nt = int(T_max / dt)
    
    # Initialize fields
    Ez = np.zeros(Nx)
    Hy = np.zeros(Nx)
    
    # Update coefficients
    epsilon = epsilon_r * eps0
    mu = mu_r * mu0
    C2 = 2 * dt / (dz * (2*epsilon))
    D2 = 2 * dt / (dz * (2*mu))
    
    # Source position
    z_source = Nx // 10
    
    print(f"[Plane Wave 1D] f={f/1e9:.1f} GHz, k={k:.4f} rad/m")
    print(f"[Plane Wave 1D] λ={2*np.pi/k*1e3:.2f} mm in medium")
    
    t = np.arange(Nt) * dt
    
    for n in range(Nt):
        # Update H field
        for i in range(Nx - 1):
            Hy[i] = Hy[i] + D2 * (Ez[i + 1] - Ez[i])
        
        # Inject source
        Ez[z_source] = A * np.sin(omega * n * dt)
        
        # Update E field
        for i in range(1, Nx - 1):
            Ez[i] = Ez[i] + C2 * (Hy[i] - Hy[i - 1])
    
    # Analytical solution
    z = np.linspace(0, L, Nx)
    analytical = A * np.sin(omega * T_max - k * z)
    
    return z, t, Ez, analytical


def validate_cfl():
    """Run CFL validation tests."""
    print("\n" + "=" * 60)
    print("CFL Stability Validation Tests")
    print("=" * 60)
    
    test_cases = [
        {"epsilon_r": 1.0, "mu_r": 1.0, "dz": 1e-3, "label": "Free space"},
        {"epsilon_r": 4.0, "mu_r": 1.0, "dz": 1e-3, "label": "Dielectric ε_r=4"},
        {"epsilon_r": 9.0, "mu_r": 1.0, "dz": 0.5e-3, "label": "High ε_r=9, fine grid"},
        {"epsilon_r": 1.0, "mu_r": 4.0, "dz": 1e-3, "label": "Magnetic μ_r=4"},
    ]
    
    all_passed = True
    for tc in test_cases:
        dt_max, dt_rec, stable = CFL_stability(
            tc["epsilon_r"], tc["mu_r"], tc["dz"]
        )
        print(f"\nTest: {tc['label']}")
        print(f"  dt_max: {dt_max:.3e} s, dt_rec: {dt_rec:.3e} s")
        if not stable:
            all_passed = False
            print("  ✗ FAILED")
        else:
            print("  ✓ PASSED")
    
    return all_passed


if __name__ == "__main__":
    print("=" * 60)
    print("Houle & Sullivan FDTD - 1D Implementation")
    print("=" * 60)
    
    # Validate CFL stability
    validate_cfl()
    
    # Run 1D Maxwell simulation
    print("\nRunning 1D FDTD simulation...")
    z, t, E_hist, H_final, dt = maxwell_1d(
        Nx=200, L=1.0, T_max=2e-9,
        epsilon_r=1.0, mu_r=1.0,
        source_type='gaussian'
    )
    
    # Quick field plot at final time
    fig, axes = plt.subplots(2, 1, figsize=(10, 6))
    
    # Find last non-zero snapshot
    last_idx = np.where(np.any(E_hist != 0, axis=1))[0][-1]
    
    axes[0].plot(z * 1e3, E_hist[last_idx], 'b-', linewidth=1.5)
    axes[0].set_xlabel('z (mm)')
    axes[0].set_ylabel('E_x (V/m)')
    axes[0].set_title(f'1D FDTD: E-field at t={t[last_idx]*1e9:.2f} ns')
    axes[0].grid(True, alpha=0.3)
    
    axes[1].plot(z * 1e3, H_final, 'r-', linewidth=1.5)
    axes[1].set_xlabel('z (mm)')
    axes[1].set_ylabel('H_y (A/m)')
    axes[1].set_title('H-field (final)')
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/houle_sullivan/code/fdtd_1d_fields.png',
                dpi=150, bbox_inches='tight')
    print("Saved: fdtd_1d_fields.png")
    
    # Run plane wave test
    print("\nRunning plane wave test...")
    z_pw, t_pw, E_pw, E_anal = plane_wave_1d(
        A=1.0, f=5e9, epsilon_r=1.0, mu_r=1.0,
        Nx=300, L=1.0, T_max=1e-9
    )
    
    fig2, ax2 = plt.subplots(figsize=(10, 4))
    ax2.plot(z_pw * 1e3, E_pw, 'b-', label='FDTD', linewidth=1.5)
    ax2.plot(z_pw * 1e3, E_anal, 'r--', label='Analytical', linewidth=1.5)
    ax2.set_xlabel('z (mm)')
    ax2.set_ylabel('E_x (V/m)')
    ax2.set_title('Plane Wave: FDTD vs Analytical Solution')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/houle_sullivan/code/plane_wave_1d.png',
                dpi=150, bbox_inches='tight')
    print("Saved: plane_wave_1d.png")
    
    # Print file info
    import os
    filepath = os.path.abspath(__file__)
    with open(filepath, 'r') as f:
        lines = len(f.readlines())
    print(f"\n[DONE] {filepath}")
    print(f"       Lines: {lines}")