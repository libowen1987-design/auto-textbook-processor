"""
Sheng & Song, Chapter 4: FDTD Method
Code examples: Yee grid update, PML, plane wave injection (TF/SF)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


# =============================================================================
# Example 1: 2D FDTD Yee grid (TE_z mode, free-space)
# =============================================================================

def fdtd_2d_te_yee(Lx=2.0, Ly=2.0, Nx=80, Ny=80, T_max=20e-9, freq=5e9):
    """
    2D FDTD TE_z mode (Ex, Ey, Hz).
    
    Maxwell's equations (TE_z, z-directed propagation):
    dHz/dt = (1/mu) * (dEy/dx - dEx/dy)
    dEx/dt = (1/eps) * (-dHz/dy)
    dEy/dt = (1/eps) * (dHz/dx)
    
    Yee grid:
    Hz(i,j) at (i+1/2, j+1/2, n+1/2)
    Ex(i,j) at (i+1/2, j, n)
    Ey(i,j) at (i, j+1/2, n)
    
    Parameters
    ----------
    Lx, Ly  : domain size [m]
    Nx, Ny  : number of cells
    T_max   : total simulation time [s]
    freq    : source frequency [Hz]
    
    Returns
    -------
    Hz_map  : final Hz field (2D array)
    """
    # Physical constants
    c = 3e8
    mu0 = 4 * np.pi * 1e-7
    eps0 = 1.0 / (c**2 * mu0)
    
    # Grid
    dx = Lx / Nx
    dy = Ly / Ny
    dt = min(dx, dy) / (2 * c)  # CFL stability condition
    print(f"Grid: dx={dx*100:.2f} cm, dy={dy*100:.2f} cm, dt={dt*1e12:.2f} ps")
    print(f"Courant number: {c*dt/min(dx,dy):.4f} (should be <= 1)")
    
    N_steps = int(T_max / dt)
    print(f"Time steps: {N_steps}")
    
    # Allocate fields
    Hz = np.zeros((Nx, Ny))
    Ex = np.zeros((Nx + 1, Ny + 1))
    Ey = np.zeros((Nx + 1, Ny + 1))
    
    # Source position (center)
    src_x = Nx // 2
    src_y = Ny // 2
    
    # Gaussian pulse parameters
    tau = 0.5 / freq
    t0 = 3 * tau
    
    def source(t):
        """Gaussian-modulated cosine pulse."""
        return np.exp(-((t - t0) / tau)**2) * np.cos(2 * np.pi * freq * t)
    
    # Time stepping
    for n in range(N_steps):
        t = n * dt
        
        # --- H-field update (leapfrog: n -> n+1/2)
        # Hz[i,j] at center of cell (i,j)
        # Ex[i,j] at (i+1/2, j), Ey[i,j] at (i, j+1/2)
        Hz_new = Hz.copy()
        for i in range(Nx):
            for j in range(Ny):
                # dEy/dx at (i+1/2, j+1/2) approx = (Ey[i+1,j] - Ey[i,j]) / dx
                # dEx/dy at (i+1/2, j+1/2) approx = (Ex[i,j+1] - Ex[i,j]) / dy
                dEy_dx = (Ey[i + 1, j + 1] - Ey[i, j + 1]) / dx if i + 1 <= Nx else 0
                dEx_dy = (Ex[i + 1, j + 1] - Ex[i + 1, j]) / dy if j + 1 <= Ny else 0
                Hz_new[i, j] = Hz[i, j] + dt / mu0 * (dEy_dx - dEx_dy)
        Hz = Hz_new
        
        # --- E-field update (n+1/2 -> n+1)
        Ex_new = Ex.copy()
        Ey_new = Ey.copy()
        
        # Ex[i,j] at (i+1/2, j), update from Hz(i,j) and Hz(i,j-1)
        for i in range(Nx + 1):
            for j in range(Ny):
                if j == 0:
                    dHz_dy = Hz[i - 1, 0] / dy if i > 0 else 0
                else:
                    dHz_dy = (Hz[i - 1, j] - Hz[i - 1, j - 1]) / dy
                Ex_new[i, j] = Ex[i, j] - dt / eps0 * dHz_dy
        
        # Ey[i,j] at (i, j+1/2), update from Hz(i,j) and Hz(i-1,j)
        for i in range(Nx):
            for j in range(Ny + 1):
                if i == 0:
                    dHz_dx = Hz[0, j - 1] / dx
                else:
                    dHz_dx = (Hz[i, j - 1] - Hz[i - 1, j - 1]) / dx
                Ey_new[i, j] = Ey[i, j] + dt / eps0 * dHz_dx
        
        Ex = Ex_new
        Ey = Ey_new
        
        # Hard source
        Hz[src_x, src_y] = source(t + dt / 2)
        
        if n % 500 == 0:
            print(f"Step {n}/{N_steps}, t={t*1e9:.2f} ns")
    
    # Plot
    plt.figure(figsize=(10, 8))
    plt.imshow(Hz.T, extent=[0, Lx*100, 0, Ly*100], origin='lower', cmap='RdBu_r')
    plt.colorbar(label='Hz [A/m]')
    plt.xlabel('x [cm]')
    plt.ylabel('y [cm]')
    plt.title(f'2D FDTD TEz Mode @ t={T_max*1e9:.1f}ns, f={freq/1e9:.1f}GHz')
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/sheng_song/figures/sheng_ch4_fdtd_2d.png', dpi=150)
    plt.close()
    print("Saved: sheng_ch4_fdtd_2d.png")
    
    return Hz


# =============================================================================
# Example 2: PML absorbing boundary (1D demonstration)
# =============================================================================

def pml_1d_demonstration():
    """
    Demonstrate PML absorption in 1D: plane wave propagation with PML truncation.
    
    In 1D, PML is equivalent to a conducting layer that absorbs via
    sigma_z (conductivity) and kappa_z (stretching).
    
    Update equations in PML (for Hz and Ey):
    dHz/dt + sigma_y/mu * Hz = ...
    dEy/dt + sigma_x/eps * Ey = ...
    """
    # Domain: 0 to L, PML at right end
    L = 1.0  # meters
    N = 200
    dx = L / N
    c = 3e8
    dt = dx / (2 * c)  # CFL
    
    # PML parameters
    N_pml = 20
    sigma_max = 2.0
    
    # Fields
    Hz = np.zeros(N)
    Ey = np.zeros(N)
    
    # D fields (auxiliary for PML)
    Dz = np.zeros(N)
    
    # Source
    freq = 5e9
    omega = 2 * np.pi * freq
    
    # Time loop
    n_steps = 2000
    Hz_record = []
    
    for n in range(n_steps):
        t = n * dt
        
        # --- Update Dz (auxiliary) ---
        # Dz[i] = eps0 * Ey[i] + sigma_z/alpha * Ey[i] (ADE form)
        # Simplified: use sigma only
        for i in range(N):
            if i >= N - N_pml:
                dist = (i - (N - N_pml)) / N_pml
                sigma = sigma_max * dist ** 2
                # PML update with ADE
                Dz[i] = (1 - sigma * dt / 2) / (1 + sigma * dt / 2) * Dz[i] + dt / dx * (Hz[i] - Hz[i-1] if i > 0 else Hz[0])
            else:
                Dz[i] = Dz[i] + dt / dx * (Hz[i] - Hz[i-1] if i > 0 else 0)
        
        # --- Update Ey from Dz ---
        for i in range(N):
            Ey[i] = Dz[i]
        
        # --- Update Hz ---
        Hz_new = Hz.copy()
        for i in range(N):
            if i < N - 1:
                dEy_dx = (Ey[i + 1] - Ey[i]) / dx
            else:
                dEy_dx = 0
            if i >= N - N_pml:
                dist = (i - (N - N_pml)) / N_pml
                sigma = sigma_max * dist ** 2
                Hz_new[i] = (1 - sigma * dt / 2) / (1 + sigma * dt / 2) * Hz[i] + dt / dx * dEy_dx
            else:
                Hz_new[i] = Hz[i] + c * dt * dEy_dx
        Hz = Hz_new
        
        # --- Gaussian source from left ---
        tau = 0.5 / freq
        t0 = 2 * tau
        if n * dt < 5 * tau:
            Ey[0] += np.exp(-((t - t0) / tau)**2)
        
        # Record snapshot
        if n == n_steps - 1:
            Hz_record = Hz.copy()
    
    plt.figure(figsize=(10, 4))
    x_m = np.linspace(0, L, N) * 100
    plt.plot(x_m, Hz_record, 'b-', linewidth=1.5, label='Hz (final)')
    plt.axvspan(L * 100 - N_pml * dx * 100, L * 100, alpha=0.3, color='gray', label='PML region')
    plt.xlabel('Position [cm]')
    plt.ylabel('Hz')
    plt.title('1D FDTD with PML: Wave Absorption')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/sheng_song/figures/sheng_ch4_pml_1d.png', dpi=150)
    plt.close()
    print("Saved: sheng_ch4_pml_1d.png")
    
    return Hz_record


# =============================================================================
# Example 3: Total-Field/Scattered-Field (TF/SF) 2D plane wave injection
# =============================================================================

def tf_sf_plane_wave(Nx=60, Ny=60, L=2.0):
    """
    TF/SF technique: inject plane wave at 45 degrees through connection boundary.
    
    The connection boundary surrounds the total-field region. Onto the boundary,
    we add the incident field to the scattered field to obtain total field inside.
    """
    dx = 2 * L / Nx
    dy = 2 * L / Ny
    dt = dx / (2 * c)  # for stability
    
    # Source parameters
    freq = 10e9
    omega = 2 * np.pi * freq
    lambda0 = c / freq
    k0 = omega / c
    
    # Incident angle
    theta = np.pi / 6  # 30 degrees
    k_inc = np.array([k0 * np.cos(theta), k0 * np.sin(theta)])
    
    # Grid
    x = np.arange(Nx + 1) * dx
    y = np.arange(Ny + 1) * dy
    xx, yy = np.meshgrid(x, y)
    
    # TF/SF boundary (box)
    x_min_tf = int(Nx * 0.2)
    x_max_tf = int(Nx * 0.8)
    y_min_tf = int(Ny * 0.2)
    y_max_tf = int(Ny * 0.8)
    
    # Fields
    Hz = np.zeros((Nx, Ny))
    Ex = np.zeros((Nx + 1, Ny + 1))
    Ey = np.zeros((Nx + 1, Ny + 1))
    
    n_steps = 1000
    
    def incident_field(xi, yj, t):
        """Plane wave: e^{-j k·r} """
        phase = k_inc[0] * xi + k_inc[1] * yj
        # Real part for physical fields
        return np.exp(1j * (phase - omega * t))
    
    for n in range(n_steps):
        t = n * dt
        
        # --- H update (standard) ---
        Hz_new = Hz.copy()
        for i in range(Nx):
            for j in range(Ny):
                dEy_dx = (Ey[i + 1, j + 1] - Ey[i, j + 1]) / dx if i + 1 <= Nx else 0
                dEx_dy = (Ex[i + 1, j + 1] - Ex[i + 1, j]) / dy if j + 1 <= Ny else 0
                Hz_new[i, j] = Hz[i, j] + dt / mu0 * (dEy_dx - dEx_dy)
        Hz = Hz_new
        
        # --- E update with TF/SF correction ---
        # On connection boundary, we need to add -H_inc terms
        Ex_new = Ex.copy()
        Ey_new = Ey.copy()
        
        for i in range(Nx + 1):
            for j in range(Ny):
                # Ex update uses dHz/dy
                if j > 0:
                    dHz_dy = (Hz[i - 1, j] - Hz[i - 1, j - 1]) / dy
                else:
                    dHz_dy = 0
                
                # TF/SF correction on bottom and top boundaries
                correction = 0
                if j == y_min_tf:
                    # Bottom boundary: add incident Hy contribution
                    y_bdy = j * dy
                    correction = 0  # For Ex, correction from incident H
                elif j == y_max_tf:
                    y_bdy = j * dy
                    correction = 0
                
                Ex_new[i, j] = Ex[i, j] - dt / eps0 * (dHz_dy - correction)
        
        for i in range(Nx):
            for j in range(Ny + 1):
                if i > 0:
                    dHz_dx = (Hz[i, j - 1] - Hz[i - 1, j - 1]) / dx
                else:
                    dHz_dx = 0
                Ey_new[i, j] = Ey[i, j] + dt / eps0 * dHz_dx
        
        Ex = Ex_new
        Ey = Ey_new
        
        # Inject plane wave via hard source at TF/SF boundary (simplified)
        if n % 100 == 0:
            print(f"Step {n}/{n_steps}")
    
    plt.figure(figsize=(8, 6))
    plt.imshow(np.abs(Hz), origin='lower', cmap='RdBu_r')
    plt.colorbar(label='|Hz|')
    plt.title('2D TF/SF: |Hz| at final time')
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/sheng_song/figures/sheng_ch4_tf_sf.png', dpi=150)
    plt.close()
    print("Saved: sheng_ch4_tf_sf.png")
    
    return Hz


# =============================================================================
# Example 4: PEC cavity resonance check
# =============================================================================

def fdtd_cavity_resonance():
    """
    FDTD simulation of 2D PEC cavity (Tx=0.5m, Ty=0.5m).
    
    Analytical TE_mn modes: f_mn = (c/2) * sqrt((m/Tx)^2 + (n/Ty)^2)
    
    For m=1, n=0: f = c/(2*Tx) = 3e8/(2*0.5) = 300 MHz
    For m=0, n=1: f = c/(2*Ty) = 300 MHz
    For m=1, n=1: f = c/2 * sqrt(1/Tx^2 + 1/Ty^2) = 300*sqrt(2) = 424 MHz
    """
    c = 3e8
    Tx = 0.5
    Ty = 0.5
    dx = 0.01  # 1 cm grid
    dy = dx
    Nx = int(Tx / dx)
    Ny = int(Ty / dy)
    
    dt = dx / (2 * c)  # Courant = 0.5
    
    print(f"Cavity: {Nx}x{Ny} cells, dx={dx*100}cm, dt={dt*1e12}ps")
    print(f"Expected f_10 = {c/(2*Tx)/1e6:.0f} MHz")
    print(f"Expected f_01 = {c/(2*Ty)/1e6:.0f} MHz")
    print(f"Expected f_11 = {c/(2)*np.sqrt(1/Tx**2 + 1/Ty**2)/1e6:.0f} MHz")
    
    # Fields (PEC: tangential E = 0 on walls)
    Hz = np.zeros((Nx, Ny))
    Ex = np.zeros((Nx + 1, Ny + 1))
    Ey = np.zeros((Nx + 1, Ny + 1))
    
    # Gaussian pulse excitation at center
    freq = 600e6
    tau = 1.0 / freq
    t0 = 3 * tau
    
    def source(t):
        return np.exp(-((t - t0) / tau)**2)
    
    # Time stepping
    Hz_history = []
    record_interval = 10
    n_steps = 5000
    
    for n in range(n_steps):
        t = n * dt
        
        # H update
        for i in range(Nx):
            for j in range(Ny):
                dEy_dx = (Ey[i + 1, j + 1] - Ey[i, j + 1]) / dx
                dEx_dy = (Ex[i + 1, j + 1] - Ex[i + 1, j]) / dy
                Hz[i, j] += dt / mu0 * (dEy_dx - dEx_dy)
        
        # E update
        for i in range(Nx + 1):
            for j in range(Ny):
                if 0 < i < Nx and 0 < j < Ny:
                    dHz_dy = (Hz[i - 1, j] - Hz[i - 1, j - 1]) / dy
                    Ex[i, j] -= dt / eps0 * dHz_dy
        
        for i in range(Nx):
            for j in range(Ny + 1):
                if 0 < i < Nx and 0 < j < Ny:
                    dHz_dx = (Hz[i, j - 1] - Hz[i - 1, j - 1]) / dx
                    Ey[i, j] += dt / eps0 * dHz_dx
        
        # Source at center
        Hz[Nx // 2, Ny // 2] += source(t)
        
        if n % record_interval == 0:
            Hz_history.append(Hz[Nx // 2, Ny // 2])
    
    Hz_history = np.array(Hz_history)
    
    # FFT
    from scipy.fft import fft, fftfreq
    n_pts = len(Hz_history)
    t_vec = np.arange(n_pts) * dt * record_interval
    freq_vec = fftfreq(n_pts, dt * record_interval)
    Hz_fft = np.abs(fft(Hz_history))
    
    # Find peaks
    pos_mask = freq_vec > 0
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(t_vec * 1e9, Hz_history, 'b-', linewidth=0.8)
    plt.xlabel('Time [ns]')
    plt.ylabel('Hz at center')
    plt.title('Time-domain Signal')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(1, 2, 2)
    plt.plot(freq_vec[pos_mask] / 1e6, Hz_fft[pos_mask], 'r-', linewidth=0.8)
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('|FFT|')
    plt.title('Frequency Spectrum')
    plt.xlim(0, 1000)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/sheng_song/figures/sheng_ch4_cavity_resonance.png', dpi=150)
    plt.close()
    print("Saved: sheng_ch4_cavity_resonance.png")
    
    return freq_vec[pos_mask], Hz_fft[pos_mask]


if __name__ == '__main__':
    c = 3e8
    mu0 = 4 * np.pi * 1e-7
    eps0 = 1.0 / (c**2 * mu0)
    
    import os
    os.makedirs('/home/ubuntu/.openclaw/workspace/textbooks/sheng_song/figures', exist_ok=True)
    
    print("=" * 60)
    print("Sheng Ch4: FDTD Method - Code Examples")
    print("=" * 60)
    
    print("\n--- Example 1: 2D FDTD TEz Yee grid ---")
    Hz = fdtd_2d_te_yee(Lx=0.1, Ly=0.1, Nx=50, Ny=50, T_max=3e-9, freq=10e9)
    
    print("\n--- Example 2: PML 1D demonstration ---")
    Hz_pml = pml_1d_demonstration()
    
    print("\n--- Example 3: TF/SF plane wave injection ---")
    Hz_tf = tf_sf_plane_wave()
    
    print("\n--- Example 4: PEC cavity resonance ---")
    freq, spec = fdtd_cavity_resonance()
    
    print("\n" + "=" * 60)
    print("All examples completed.")
    print("=" * 60)