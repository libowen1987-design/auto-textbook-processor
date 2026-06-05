"""
houale_fdtd_2d.py - 2D FDTD Implementation
Based on Houle & Sullivan, "EM Simulation Using FDTD"
Author: 小龙虾 (Crawfish)
Features: TM/TE modes, waveguide modes, dielectric scattering
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import warnings
warnings.filterwarnings('ignore')


def maxwell_2d_TM(Nx=200, Ny=200, Lx=1.0, Ly=1.0, T_max=2e-9,
                 epsilon_r=1.0, mu_r=1.0, sigma=0.0):
    """
    2D TM mode FDTD (E_z, H_x, H_y).
    
    TM mode equations (z-directed propagation):
        dH_x/dt = -(1/mu)*dE_z/dy
        dH_y/dt = (1/mu)*dE_z/dx
        dE_z/dt = (1/epsilon)*[dH_y/dx - dH_x/dy] - (sigma/epsilon)*E_z
    
    Parameters
    ----------
    Nx, Ny : int
        Grid points in x, y
    Lx, Ly : float
        Domain size (m)
    T_max : float
        Simulation time (s)
    epsilon_r : float
        Relative permittivity
    mu_r : float
        Relative permeability
    sigma : float
        Conductivity (S/m)
    
    Returns
    -------
    x_grid, y_grid : ndarray
        Spatial grids
    Ez : ndarray
        E_z field snapshot [Nx x Ny]
    t : ndarray
        Time array
    """
    c = 3e8
    eps0 = 8.854e-12
    mu0 = 4 * np.pi * 1e-7
    
    dx = Lx / (Nx - 1)
    dy = Ly / (Ny - 1)
    
    c_numerical = c / np.sqrt(epsilon_r * mu_r)
    # CFL: dt <= 2*dx*dy / sqrt(dx^2 + dy^2) / c_numerical
    dt = 0.99 * 2 * dx * dy / (np.sqrt(dx**2 + dy**2) * c_numerical)
    Nt = int(T_max / dt)
    
    epsilon = epsilon_r * eps0
    mu = mu_r * mu0
    
    # Initialize fields (Yee lattice)
    # Ez at (i, j), Hx at (i, j+0.5), Hy at (i+0.5, j)
    Ez = np.zeros((Nx, Ny))
    Hx = np.zeros((Nx, Ny - 1))  # staggered in y
    Hy = np.zeros((Nx - 1, Ny))  # staggered in x
    
    # Update coefficients
    # For H fields (half-step)
    Chx = dt / (mu * dy)
    Chry = dt / (mu * dx)
    # For E field (full-step)
    Cez = (2*epsilon - sigma*dt) / (2*epsilon + sigma*dt)
    Dez = (2*dt) / (dy * (2*epsilon + sigma*dt))
    Dey = (2*dt) / (dx * (2*epsilon + sigma*dt))
    
    # Source
    source_x = Nx // 4
    source_y = Ny // 4
    
    def source_t(n):
        t_n = n * dt
        tau = 30 * dt
        t0 = 80 * dt
        return np.exp(-((t_n - t0) / tau)**2)
    
    t = np.arange(Nt) * dt
    
    print(f"[2D TM] Grid: {Nx}x{Ny}, dx={dx*1e3:.3f} mm, dy={dy*1e3:.3f} mm")
    print(f"[2D TM] dt: {dt:.3e} s, Nt: {Nt}, CFL: {dt * c_numerical / (2*dx):.4f}")
    
    # FDTD loop
    for n in range(Nt):
        # Update Hx (dH_x/dt = -dE_z/dy)
        for i in range(Nx):
            for j in range(Ny - 1):
                Hx[i, j] -= Chx * (Ez[i, j + 1] - Ez[i, j])
        
        # Update Hy (dH_y/dt = dE_z/dx)
        for i in range(Nx - 1):
            for j in range(Ny):
                Hy[i, j] += Chry * (Ez[i + 1, j] - Ez[i, j])
        
        # Update Ez (dE_z/dt = dH_y/dx - dH_x/dy)
        for i in range(1, Nx - 1):
            for j in range(1, Ny - 1):
                Ez[i, j] = Cez * Ez[i, j] + Dey * (Hy[i, j] - Hy[i-1, j]) - Dez * (Hx[i, j] - Hx[i, j-1])
        
        # Source injection
        Ez[source_x, source_y] = source_t(n)
        
        # Absorbing boundary (first-order Mur)
        # Left
        Ez[0, :] = Ez[1, :] + (c_numerical * dt - dx) / (c_numerical * dt + dx) * (Ez[1, :] - Ez[0, :])
        # Right
        Ez[-1, :] = Ez[-2, :] + (c_numerical * dt - dx) / (c_numerical * dt + dx) * (Ez[-2, :] - Ez[-1, :])
        # Bottom
        Ez[:, 0] = Ez[:, 1] + (c_numerical * dt - dy) / (c_numerical * dt + dy) * (Ez[:, 1] - Ez[:, 0])
        # Top
        Ez[:, -1] = Ez[:, -2] + (c_numerical * dt - dy) / (c_numerical * dt + dy) * (Ez[:, -2] - Ez[:, -1])
    
    x_grid = np.linspace(0, Lx, Nx)
    y_grid = np.linspace(0, Ly, Ny)
    
    return x_grid, y_grid, Ez, t


def maxwell_2d_TE(Nx=200, Ny=200, Lx=1.0, Ly=1.0, T_max=2e-9,
                 epsilon_r=1.0, mu_r=1.0):
    """
    2D TE mode FDTD (E_x, E_y, H_z).
    
    TE mode equations:
        dH_z/dt = (1/mu)*[dE_y/dx - dE_x/dy]
        dE_x/dt = (1/epsilon)*dH_z/dy
        dE_y/dt = -(1/epsilon)*dH_z/dx
    
    Parameters
    ----------
    Nx, Ny : int
        Grid points
    Lx, Ly : float
        Domain size (m)
    T_max : float
        Simulation time (s)
    epsilon_r : float
        Relative permittivity
    mu_r : float
        Relative permeability
    
    Returns
    -------
    x_grid, y_grid : ndarray
        Spatial grids
    Ez : ndarray
        H_z field (note: TE has H_z as primary)
    """
    c = 3e8
    eps0 = 8.854e-12
    mu0 = 4 * np.pi * 1e-7
    
    dx = Lx / (Nx - 1)
    dy = Ly / (Ny - 1)
    
    c_numerical = c / np.sqrt(epsilon_r * mu_r)
    dt = 0.99 * 2 * dx * dy / (np.sqrt(dx**2 + dy**2) * c_numerical)
    Nt = int(T_max / dt)
    
    epsilon = epsilon_r * eps0
    mu = mu_r * mu0
    
    # TE fields: H_z at (i+0.5, j+0.5), E_x at (i, j+0.5), E_y at (i+0.5, j)
    Hz = np.zeros((Nx - 1, Ny - 1))
    Ex = np.zeros((Nx, Ny - 1))
    Ey = np.zeros((Nx - 1, Ny))
    
    # Update coefficients
    Chz_dx = dt / (mu * dx)
    Chz_dy = dt / (mu * dy)
    Cex = dt / (epsilon * dy)
    Cey = dt / (epsilon * dx)
    
    source_x = Nx // 4
    source_y = Ny // 4
    
    def source_t(n):
        t_n = n * dt
        tau = 30 * dt
        t0 = 80 * dt
        return np.exp(-((t_n - t0) / tau)**2)
    
    print(f"[2D TE] Grid: {Nx}x{Ny}, dt: {dt:.3e} s")
    
    for n in range(Nt):
        # Update H_z
        for i in range(Nx - 1):
            for j in range(Ny - 1):
                Hz[i, j] += Chz_dx * (Ey[i + 1, j] - Ey[i, j]) - Chz_dy * (Ex[i, j + 1] - Ex[i, j])
        
        # Update E_x
        for i in range(Nx):
            for j in range(Ny - 1):
                Ex[i, j] -= Cex * (Hz[i, j] - Hz[i - 1, j] if i > 0 else Hz[i, j])
        
        # Update E_y
        for i in range(Nx - 1):
            for j in range(Ny):
                Ey[i, j] += Cey * (Hz[i, j] - Hz[i, j - 1] if j > 0 else Hz[i, j])
        
        # Source
        if source_x > 0 and source_x < Nx - 1 and source_y > 0 and source_y < Ny - 1:
            Hz[source_x, source_y] = source_t(n)
    
    x_grid = np.linspace(0, Lx, Nx)
    y_grid = np.linspace(0, Ly, Ny)
    
    return x_grid, y_grid, Hz, Ex, Ey


def waveguide_2d(Nx=300, Ny=100, Lx=2.0, Ly=0.6,
                  f_cutoff=10e9, T_max=5e-9):
    """
    Rectangular waveguide mode validation using 2D FDTD.
    
    For a rectangular waveguide (a x b), TE_mn cutoffs:
        f_c = (c/2) * sqrt((m/a)^2 + (n/b)^2)
    
    Parameters
    ----------
    Nx, Ny : int
        Grid points
    Lx, Ly : float
        Waveguide dimensions (m)
    f_cutoff : float
        Source frequency (Hz)
    T_max : float
        Simulation time (s)
    
    Returns
    -------
    x_grid, y_grid : ndarray
        Spatial grids
    Ez : ndarray
        E_z field for TM modes
    """
    c = 3e8
    eps0 = 8.854e-12
    mu0 = 4 * np.pi * 1e-7
    
    # Waveguide parameters
    a, b = Lx, Ly  # broad wall, narrow wall
    epsilon_r = 1.0  # air-filled
    mu_r = 1.0
    
    dx = a / (Nx - 1)
    dy = b / (Ny - 1)
    
    c_numerical = c / np.sqrt(epsilon_r * mu_r)
    dt = 0.99 * 2 * dx * dy / (np.sqrt(dx**2 + dy**2) * c_numerical)
    Nt = int(T_max / dt)
    
    epsilon = epsilon_r * eps0
    mu = mu_r * mu0
    
    # Fields
    Ez = np.zeros((Nx, Ny))
    Hx = np.zeros((Nx, Ny - 1))
    Hy = np.zeros((Nx - 1, Ny))
    
    # Update coefficients
    Chx = dt / (mu * dy)
    Chry = dt / (mu * dx)
    Cez = 1.0  # lossless
    Dey = 2 * dt / (dx * (2*epsilon))
    Dez = 2 * dt / (dy * (2*epsilon))
    
    # Source at one end
    source_x = 10
    
    def source_t(n):
        omega = 2 * np.pi * f_cutoff
        return np.sin(omega * n * dt)
    
    print(f"[Waveguide 2D] Dimensions: {a*1e3:.1f} x {b*1e3:.1f} mm")
    print(f"[Waveguide 2D] Source freq: {f_cutoff/1e9:.1f} GHz")
    
    # TE10 cutoff
    f_c_TE10 = c / 2 * np.sqrt((1/a)**2)
    print(f"[Waveguide 2D] TE10 cutoff: {f_c_TE10/1e9:.2f} GHz")
    
    t = np.arange(Nt) * dt
    
    for n in range(Nt):
        # Update Hx
        for i in range(Nx):
            for j in range(Ny - 1):
                Hx[i, j] -= Chx * (Ez[i, j + 1] - Ez[i, j])
        
        # Update Hy
        for i in range(Nx - 1):
            for j in range(Ny):
                Hy[i, j] += Chry * (Ez[i + 1, j] - Ez[i, j])
        
        # Update Ez
        for i in range(1, Nx - 1):
            for j in range(1, Ny - 1):
                Ez[i, j] = Cez * Ez[i, j] + Dey * (Hy[i, j] - Hy[i-1, j]) - Dez * (Hx[i, j] - Hx[i, j-1])
        
        # Inject source (waveguide port)
        for j in range(Ny):
            Ez[source_x, j] = source_t(n) * np.sin(np.pi * j * dy / b)
    
    x_grid = np.linspace(0, a, Nx)
    y_grid = np.linspace(0, b, Ny)
    
    return x_grid, y_grid, Ez


def dielectric_scatterer(Nx=250, Ny=250, L=1.5, radius=0.1,
                         epsilon_r_diel=4.0, f_source=10e9, T_max=3e-9):
    """
    Dielectric cylinder scattering simulation.
    
    A plane wave incident on a dielectric cylinder creates
    complex scattering patterns (Mie scattering).
    
    Parameters
    ----------
    Nx, Ny : int
        Grid points
    L : float
        Domain size (m)
    radius : float
        Cylinder radius (m)
    epsilon_r_diel : float
        Relative permittivity of cylinder
    f_source : float
        Source frequency (Hz)
    T_max : float
        Simulation time (s)
    
    Returns
    -------
    x_grid, y_grid : ndarray
        Spatial grids
    Ez : ndarray
        Total E_z field
    """
    c = 3e8
    eps0 = 8.854e-12
    mu0 = 4 * np.pi * 1e-7
    
    dx = L / (Nx - 1)
    dy = L / (Ny - 1)
    
    center_x = Nx // 2
    center_y = Ny // 2
    
    c_numerical = c  # free space
    dt = 0.99 * 2 * dx * dy / (np.sqrt(dx**2 + dy**2) * c_numerical)
    Nt = int(T_max / dt)
    
    # Field arrays
    Ez = np.zeros((Nx, Ny))
    Hx = np.zeros((Nx, Ny - 1))
    Hy = np.zeros((Nx - 1, Ny))
    
    # Create material map
    # epsilon_r[i,j] = 1.0 for air, = epsilon_r_diel inside cylinder
    epsilon_r_map = np.ones((Nx, Ny))
    for i in range(Nx):
        for j in range(Ny):
            r = np.sqrt((i - center_x)**2 * dx**2 + (j - center_y)**2 * dy**2)
            if r < radius:
                epsilon_r_map[i, j] = epsilon_r_diel
    
    # Source plane (left edge)
    source_x = 20
    
    omega = 2 * np.pi * f_source
    wavelength = c / f_source
    
    print(f"[Dielectric Scatterer] Domain: {L*1e3:.1f} mm x {L*1e3:.1f} mm")
    print(f"[Dielectric Scatterer] Cylinder radius: {radius*1e3:.1f} mm")
    print(f"[Dielectric Scatterer] ε_r: {epsilon_r_diel}, f: {f_source/1e9:.1f} GHz")
    print(f"[Dielectric Scatterer] λ: {wavelength*1e3:.2f} mm")
    
    def source_t(n):
        return np.sin(omega * n * dt)
    
    t = np.arange(Nt) * dt
    
    for n in range(Nt):
        # Update Hx
        for i in range(Nx):
            for j in range(Ny - 1):
                eps_ij = epsilon_r_map[i, j]
                mu_ij = 1.0
                Chx_ij = dt / (mu_ij * mu0 * dy)
                Hx[i, j] -= Chx_ij * (Ez[i, j + 1] - Ez[i, j])
        
        # Update Hy
        for i in range(Nx - 1):
            for j in range(Ny):
                eps_ij = epsilon_r_map[i, j]
                mu_ij = 1.0
                Chry_ij = dt / (mu_ij * mu0 * dx)
                Hy[i, j] += Chry_ij * (Ez[i + 1, j] - Ez[i, j])
        
        # Update Ez
        for i in range(1, Nx - 1):
            for j in range(1, Ny - 1):
                eps_ij = epsilon_r_map[i, j]
                epsilon = eps_ij * eps0
                Dey = 2 * dt / (dx * (2*epsilon))
                Dez = 2 * dt / (dy * (2*epsilon))
                Ez[i, j] = Ez[i, j] + Dey * (Hy[i, j] - Hy[i-1, j]) - Dez * (Hx[i, j] - Hx[i, j-1])
        
        # Plane wave source (from left)
        for j in range(Ny):
            Ez[source_x, j] = source_t(n)
        
        # ABC boundaries
        for j in range(Ny):
            Ez[0, j] = Ez[1, j]
            Ez[-1, j] = Ez[-2, j]
        for i in range(Nx):
            Ez[i, 0] = Ez[i, 1]
            Ez[i, -1] = Ez[i, -2]
    
    x_grid = np.linspace(0, L, Nx)
    y_grid = np.linspace(0, L, Ny)
    
    return x_grid, y_grid, Ez


def plot_field_2d(x_grid, y_grid, field, title, filename, cmap='RdBu_r'):
    """Plot and save 2D field snapshot."""
    fig, ax = plt.subplots(figsize=(10, 8))
    
    X, Y = np.meshgrid(x_grid * 1e3, y_grid * 1e3, indexing='ij')
    
    vmax = np.max(np.abs(field))
    levels = np.linspace(-vmax, vmax, 50)
    
    cf = ax.contourf(X, Y, field, levels=levels, cmap=cmap)
    ax.set_xlabel('x (mm)')
    ax.set_ylabel('y (mm)')
    ax.set_title(title)
    ax.set_aspect('equal')
    
    cbar = plt.colorbar(cf, ax=ax)
    cbar.set_label('Field (V/m)')
    
    plt.tight_layout()
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"Saved: {filename}")
    plt.close()


if __name__ == "__main__":
    print("=" * 60)
    print("Houle & Sullivan FDTD - 2D Implementation")
    print("=" * 60)
    
    # TM mode test
    print("\nRunning 2D TM mode...")
    x, y, Ez_tm, t = maxwell_2d_TM(
        Nx=150, Ny=150, Lx=0.75, Ly=0.75, T_max=1.5e-9,
        epsilon_r=1.0, mu_r=1.0
    )
    plot_field_2d(x, y, Ez_tm, '2D TM Mode: E_z Field',
                  '/home/ubuntu/.openclaw/workspace/textbooks/houle_sullivan/code/tm_mode_2d.png')
    
    # Waveguide mode
    print("\nRunning waveguide mode...")
    x_wg, y_wg, Ez_wg = waveguide_2d(
        Nx=200, Ny=80, Lx=1.5, Ly=0.4,
        f_cutoff=8e9, T_max=3e-9
    )
    plot_field_2d(x_wg, y_wg, Ez_wg, 'Rectangular Waveguide: TE10 Mode',
                  '/home/ubuntu/.openclaw/workspace/textbooks/houle_sullivan/code/waveguide_2d.png')
    
    # Dielectric scatterer
    print("\nRunning dielectric scatterer...")
    x_ds, y_ds, Ez_ds = dielectric_scatterer(
        Nx=200, Ny=200, L=1.0, radius=0.08,
        epsilon_r_diel=4.0, f_source=8e9, T_max=2e-9
    )
    plot_field_2d(x_ds, y_ds, Ez_ds, 'Dielectric Cylinder Scattering (ε_r=4)',
                  '/home/ubuntu/.openclaw/workspace/textbooks/houle_sullivan/code/dielectric_scatter.png', 'hot')
    
    # Print file info
    import os
    filepath = os.path.abspath(__file__)
    with open(filepath, 'r') as f:
        lines = len(f.readlines())
    print(f"\n[DONE] {filepath}")
    print(f"       Lines: {lines}")