#!/usr/bin/env python3
"""
Bondeson Ch5: Finite-Difference Time-Domain (FDTD) Method
Maxwell's equations in FDTD, Courant stability, PML absorbing boundary
"""
import numpy as np
import matplotlib.pyplot as plt

# Ch5.1 - 1D FDTD: Plane wave propagation in free space
c = 3e8  # speed of light
dx = 1e-3  # 1 mm cells
dt = 3e-12  # 3 ps time step (Courant: dt <= dx/c)

# 1D FDTD grid
nx = 500
Ez = np.zeros(nx)
Hy = np.zeros(nx)

# Source: Gaussian pulse
def source(t):
    tau = 50e-12
    t0 = 30e-12
    return np.exp(-((t - t0) / tau)**2)

# Record Ez at a point for time domain
Ez_record = []

# Time stepping
n_steps = 400
for n in range(n_steps):
    t = n * dt
    
    # Update Hy (Maxwell-Ampere: dH/dt = -(1/mu) * dE/dx)
    for i in range(nx - 1):
        Hy[i] += (dt / (c * 1e-7 * 4 * np.pi)) * (Ez[i+1] - Ez[i]) / dx
    
    # Update Ez (Maxwell-Faraday: dE/dt = -(1/eps) * dH/dx)
    for i in range(1, nx):
        Ez[i] += (dt / (c * 1e-9 / (36 * np.pi))) * (Hy[i] - Hy[i-1]) / dx
    
    # Add source at cell 50
    Ez[50] += source(t)
    
    if n % 2 == 0:
        Ez_record.append(Ez.copy())

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot Ez field at different times
ax = axes[0, 0]
times = [0, 100, 200, 300]
x = np.arange(nx) * dx * 100  # cm
for t_idx in [0, 50, 150, 300]:
    if t_idx < len(Ez_record):
        ax.plot(x, Ez_record[t_idx], label=f't={t_idx*dt*1e12:.0f} ps', alpha=0.8)
ax.set_xlabel('Position (cm)')
ax.set_ylabel('Ez (V/m)')
ax.set_title('1D FDTD: Gaussian Pulse Propagation')
ax.legend()
ax.grid(True, alpha=0.3)

# Ch5.2 - Courant stability condition
ax = axes[0, 1]
S_values = np.linspace(0.1, 1.0, 100)  # Courant number S = c*dt/dx
dt_range = S_values * dx / c
ax.plot(S_values, dt_range * 1e12, 'b-', lw=2)
ax.axhline(y=dt * 1e12, color='r', ls='--', label=f'Current: dt={dt*1e12:.1f}ps')
ax.axhline(y=dx/c * 1e12, color='g', ls=':', label=f'Max: dx/c={dx/c*1e12:.1f}ps')
ax.set_xlabel('Courant Number S = c·dt/dx')
ax.set_ylabel('dt (ps)')
ax.set_title('Courant Stability Condition')
ax.legend()
ax.grid(True, alpha=0.3)

# Ch5.3 - 2D FDTD: TEz mode (Ez, Hx, Hy)
ax = axes[1, 0]
# Simple 2D FDTD with PEC boundaries
nx, ny = 100, 80
Ez = np.zeros((ny, nx))
Hx = np.zeros((ny, nx))
Hy = np.zeros((ny, nx))
mu = 4e-7 * np.pi
eps = 1e-9 / (36 * np.pi)
dt_2d = dx / (c * np.sqrt(2))  # 2D Courant limit

# Source: sinusoidal at center
f0 = 10e9  # 10 GHz
omega = 2 * np.pi * f0

Ez_snapshot = []
for n in range(300):
    t = n * dt_2d
    
    # Update Hx, Hy
    for i in range(ny):
        for j in range(nx):
            Hx[i, j] += (dt_2d / mu) * (Ez[i+1, j] - Ez[i, j]) / dx if i < ny-1 else Hx[i, j]
            Hy[i, j] += (dt_2d / mu) * (Ez[i, j+1] - Ez[i, j]) / dx if j < nx-1 else Hy[i, j]
    
    # Update Ez
    for i in range(1, ny-1):
        for j in range(1, nx-1):
            Ez[i, j] += (dt_2d / eps) * ((Hy[i, j] - Hy[i-1, j]) / dx - (Hx[i, j] - Hx[i, j-1]) / dx)
    
    # Source at center
    Ez[ny//2, nx//2] += np.sin(omega * t)
    
    if n == 100:
        Ez_snapshot.append(Ez.copy())

if Ez_snapshot:
    im = ax.imshow(Ez_snapshot[0], extent=[0, nx*dx*100, 0, ny*dx*100], 
                   cmap='RdBu', origin='lower', aspect='auto')
    ax.set_xlabel('x (cm)')
    ax.set_ylabel('y (cm)')
    ax.set_title('2D FDTD TEz: Ez field at t=100 steps')
    plt.colorbar(im, ax=ax)

# Ch5.4 - PML absorbing boundary illustration
ax = axes[1, 1]
# Show PML profile
pml_width = 10
nx_pml = 100
sigma_profile = np.zeros(nx_pml)
sigma_profile[-pml_width:] = np.linspace(0, 10, pml_width)**2 * 0.5
ax.plot(np.arange(nx_pml), sigma_profile, 'b-', lw=2)
ax.set_xlabel('Grid index')
ax.set_ylabel(r'$\sigma$ (S/m)')
ax.set_title('PML Conductivity Profile (Quadratic)')
ax.grid(True, alpha=0.3)
ax.fill_between(range(nx_pml-pml_width, nx_pml), 0, sigma_profile[-pml_width:], alpha=0.3, label='PML region')
ax.legend()

plt.tight_layout()
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/bondeson/figures/bondeson_ch5_fdtd.png', dpi=150)
plt.close()
print("bondeson_ch5_fdtd.png saved")

# Ch5.5 - FDTD dispersion
fig, ax = plt.subplots()
k_dx = np.linspace(0.01, np.pi, 200)  # k*dx from 0 to pi
frequencies = np.linspace(1e9, 20e9, 200)  # 1-20 GHz
c0 = 3e8

S = 0.5  # Courant number
# Dispersion relation for 1D FDTD: sin(omega*dt/2) = S * sin(k*dx/2)
omega_dt_2 = np.arcsin(S * np.sin(k_dx / 2))
k_analytical = 2 * np.pi * frequencies / c0

ax.plot(k_dx, omega_dt_2 / k_dx, 'b-', lw=2, label='FDTD numerical')
ax.plot(k_dx, np.ones_like(k_dx), 'r--', lw=2, label='Analytical (c/c0=1)')
ax.set_xlabel(r'$k \cdot dx$ (rad)')
ax.set_ylabel(r'$\omega \cdot dt / 2$ (rad)')
ax.set_title('FDTD Dispersion Relation (S=0.5)')
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_xlim([0, np.pi])
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/bondeson/figures/bondeson_ch5_dispersion.png', dpi=150)
plt.close()
print("bondeson_ch5_dispersion.png saved")

print("bondeson ch5 code complete!")