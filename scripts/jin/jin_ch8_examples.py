"""
jin_ch8_examples.py
Jin CEM 2nd Ed., Chapter 8: FDM/FDTD
Examples: 1D FDTD, CFL stability, numerical dispersion.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

epsilon_0 = constants.epsilon_0
mu_0 = constants.mu_0
c_light = constants.c
pi = np.pi


def fdtd_1d():
    """1D FDTD simulation of a Gaussian pulse propagating in free space."""
    nx = 300
    dx = 1e-3
    dt = dx / (2 * c_light)  # CFL = 0.5
    nt = 600
    
    Ez = np.zeros(nx)
    Hy = np.zeros(nx)
    
    # Source (Gaussian)
    source_pos = 50
    t0 = 40
    spread = 12
    
    Ez_history = np.zeros((nt, nx))
    
    for n in range(nt):
        # Update H (magnetic field)
        # Hy^{n+1/2} = Hy^{n-1/2} - dt/(mu*dx) * (Ez^{n}_{i+1} - Ez^{n}_{i})
        for i in range(nx-1):
            Hy[i] = Hy[i] - dt/(mu_0*dx) * (Ez[i+1] - Ez[i])
        
        # Source excitation
        pulse = np.exp(-0.5*((n - t0)/spread)**2)
        Ez[source_pos] += pulse
        
        # Update E (electric field)
        for i in range(1, nx):
            Ez[i] = Ez[i] - dt/(epsilon_0*dx) * (Hy[i] - Hy[i-1])
        
        # Record
        Ez_history[n] = Ez.copy()
    
    # Plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
    snapshots = [100, 300, 500]
    for snap in snapshots:
        ax1.plot(Ez_history[snap], label=f"t={snap*dt*1e9:.2f} ns")
    ax1.set_xlabel("Cell index"); ax1.set_ylabel("E_z (V/m)")
    ax1.set_title("1D FDTD: Gaussian Pulse Propagation"); ax1.legend(); ax1.grid(True,alpha=0.3)
    
    # Space-time plot
    extent = [0, nx, nt*dt*1e9, 0]
    ax2.imshow(Ez_history.T, aspect='auto', cmap='RdBu', extent=extent, vmin=-0.5, vmax=0.5)
    ax2.set_xlabel("Cell index"); ax2.set_ylabel("Time (ns)")
    ax2.set_title("Space-Time Diagram"); ax2.grid(False)
    
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch8_fig_fdtd1d.png",dpi=150)
    plt.close()
    print("[OK] 1D FDTD simulation done.")
    
    # Check propagation speed
    peak_t1 = np.argmax(np.abs(Ez_history[200]))
    peak_t2 = np.argmax(np.abs(Ez_history[400]))
    v_num = (peak_t2 - peak_t1) * dx / (200 * dt)
    print(f"  Numeric velocity: {v_num:.3e} m/s (c = {c_light:.3e})")
    print()


def cfl_stability():
    """Plot allowed time step vs grid size for various CFL numbers."""
    dx = np.logspace(-4, -2, 50)
    dt_cfl1 = dx / (c_light * np.sqrt(3))  # 3D CFL
    dt_cfl2 = dx / (c_light * np.sqrt(2))  # 2D CFL
    dt_cfl1d = dx / c_light                # 1D CFL
    
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.loglog(dx*1e3, dt_cfl1d*1e12, 'b-', lw=1.5, label="1D: dt=dx/c")
    ax.loglog(dx*1e3, dt_cfl2*1e12, 'r--', lw=1.5, label="2D: dt=dx/(c*sqrt(2))")
    ax.loglog(dx*1e3, dt_cfl1*1e12, 'g-.', lw=1.5, label="3D: dt=dx/(c*sqrt(3))")
    ax.set_xlabel("$\\Delta x$ (mm)"); ax.set_ylabel("$\\Delta t_{\\max}$ (ps)")
    ax.set_title("CFL Stability Condition"); ax.legend(); ax.grid(True,alpha=0.3)
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch8_fig_cfl.png",dpi=150)
    plt.close()
    print("[OK] CFL stability plot saved.")


def numerical_dispersion():
    """Plot numerical dispersion error vs grid resolution."""
    res = np.linspace(5, 50, 100)  # points per wavelength
    # For 1D FDTD with CFL = 0.5
    cfl = 0.5
    k_exact = 2*pi
    # Numerical wavenumber from dispersion relation:
    # sin^2(omega*dt/2) = (c*dt/dx)^2 * sin^2(k*dx/2)
    # k_num = 2/dx * arcsin(sin(omega*dt/2) / (cfl))
    # where omega*dt/2 = pi*cfl/res  (since omega = 2*pi*c/lambda, lambda/res=dx)
    
    omega_dt_half = pi * cfl / res
    k_num_dx_half = np.arcsin(np.minimum(np.sin(omega_dt_half)/cfl, 0.999))
    k_num = 2 * k_num_dx_half / (1/res)  # dx = lambda/res, k_num in units of 1/lambda
    
    vp_num = omega_dt_half / (k_num_dx_half) * cfl * c_light  # normalized
    vp_error = np.abs(vp_num - c_light) / c_light * 100
    
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.semilogy(res, vp_error, 'b-', lw=1.5)
    ax.set_xlabel("Points per wavelength"); ax.set_ylabel("Phase velocity error (%)")
    ax.set_title("Numerical Dispersion: 1D FDTD (CFL=0.5)")
    ax.grid(True,alpha=0.3)
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch8_fig_dispersion.png",dpi=150)
    plt.close()
    print("[OK] Numerical dispersion plot saved.")
    print(f"  At 10 ppw: error = {vp_error[np.argmin(np.abs(res-10))]:.3f}%")
    print(f"  At 20 ppw: error = {vp_error[np.argmin(np.abs(res-20))]:.3f}%")
    print()


def main():
    print();print("╔══════════════════════════════════════════╗")
    print("║  Jin CEM 2nd Ed. — Ch8 Code               ║")
    print("╚══════════════════════════════════════════╝");print()
    fdtd_1d()
    cfl_stability()
    numerical_dispersion()
    print("All Ch8 examples done.")

if __name__=="__main__":
    main()
