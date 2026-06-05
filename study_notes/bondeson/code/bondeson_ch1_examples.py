#!/usr/bin/env python3
"""
Bondeson Ch1 Examples — Computational Electromagnetics
Chapter 1: Introduction to CEM and Maxwell's Equations

Physical constants (SI units)
"""
import numpy as np
import scipy.constants as sc

# === Physical Constants ===
c_0 = sc.speed_of_light          # m/s, free-space speed of light
mu_0 = sc.mu_0                    # H/m, free-space permeability
eps_0 = sc.epsilon_0              # F/m, free-space permittivity
eta_0 = np.sqrt(mu_0 / eps_0)     # ohm, free-space intrinsic impedance

print("=" * 60)
print("Bondeson Ch1 — Physical Constants Verification")
print("=" * 60)
print(f"c_0   = {c_0:.6e} m/s")
print(f"mu_0  = {mu_0:.6e} H/m")
print(f"eps_0 = {eps_0:.6e} F/m")
print(f"eta_0 = {eta_0:.6e} ohm")
print()

# === Example 1: CFL Stability Condition (3D) ===
print("=" * 60)
print("Example 1: CFL Stability Condition")
print("=" * 60)
dx = 1e-3   # m, spatial grid spacing in x
dy = 1e-3   # m, spatial grid spacing in y
dz = 1e-3   # m, spatial grid spacing in z

dh = min(dx, dy, dz)
cfl_max = dh / (c_0 * np.sqrt(3))
print(f"Grid spacing dh = {dh*1e3:.3f} mm")
print(f"CFL maximum dt   = {cfl_max*1e15:.4f} fs")
print(f"  → For stability: dt <= {cfl_max*1e15:.4f} fs")

# Check: if we use dt = 0.9 * cfl_max (90% of limit)
dt = 0.9 * cfl_max
courant = c_0 * dt * np.sqrt(1/dx**2 + 1/dy**2 + 1/dz**2)
print(f"  Courant number (with dt=0.9*dt_max) = {courant:.4f} (< 1 required)")
print()

# === Example 2: Numerical Dispersion in 1D ===
print("=" * 60)
print("Example 2: Numerical Dispersion in 1D")
print("=" * 60)

def numerical_phase_velocity(dx, dt, frequency, epsilon_r=1.0, mu_r=1.0):
    """
    Compute the numerical phase velocity for 1D FDTD dispersion.
    v_p = c / sqrt(1 - (c*dt/dx)^2 * sin^2(phi/2))
    where phi = k*dx is the phase angle per grid spacing.
    """
    c = c_0 / np.sqrt(epsilon_r * mu_r)
    phi = 2 * np.pi * frequency * dx / c  # phase angle per cell
    sin2 = np.sin(phi / 2) ** 2
    ratio = (c * dt / dx) ** 2
    # Avoid negative radicand
    radicand = 1.0 - ratio * sin2
    if radicand <= 0:
        return np.inf
    v_p = c / np.sqrt(radicand)
    return v_p

frequency = 5e9    # Hz, operating frequency
dx = c_0 / frequency / 20  # lambda/20 sampling
dt = dx / (c_0 * np.sqrt(3))  # use max CFL dt

v_p = numerical_phase_velocity(dx, dt, frequency)
c = c_0
print(f"Frequency          = {frequency*1e-9:.1f} GHz")
print(f"Spatial step dx   = {dx*1e3:.4f} mm (lambda/20)")
print(f"Time step dt      = {dt*1e15:.4f} fs")
print(f"Physical c        = {c*1e-6:.6f} Mm/s")
print(f"Numerical v_p     = {v_p*1e-6:.6f} Mm/s")
print(f"Dispersion error  = {(v_p/c - 1)*100:.4f} %")
print()

# === Example 3: Sampling Criterion (Resolution) ===
print("=" * 60)
print("Example 3: Sampling Criterion")
print("=" * 60)

def min_sampling_grid(lambda_min_mm, points_per_wavelength=20):
    """Return max grid spacing for given sampling criterion."""
    return lambda_min_mm * 1e-3 / points_per_wavelength

for ppw in [10, 15, 20]:
    dh = min_sampling_grid(10.0, ppw)  # lambda_min = 10 mm
    print(f"  {ppw} pts/wavelength → dx_max = {dh*1e3:.4f} mm")

# 3D total unknowns estimate
Nx, Ny, Nz = 100, 100, 100
total_unknowns = Nx * Ny * Nz
memory_mb = total_unknowns * 8 / 1e6  # 8 bytes per double
print(f"\nEstimated 3D grid: {Nx}x{Ny}x{Nz} = {total_unknowns:,} nodes")
print(f"Memory (double)   ≈ {memory_mb:.2f} MB")
print()

# === Example 4: Wave impedance and Poynting vector ===
print("=" * 60)
print("Example 4: Plane Wave in Free Space")
print("=" * 60)

E_rms = 100.0   # V/m, RMS electric field
H_rms = E_rms / eta_0
S = E_rms * H_rms   # time-averaged Poynting vector magnitude
print(f"E_rms = {E_rms:.2f} V/m")
print(f"H_rms = {H_rms:.4f} A/m  (eta_0 = {eta_0:.2f} ohm)")
print(f"Poynting S = {S:.4f} W/m²")
print()

# === Example 5: Curl-curl operator eigenvalue (1D) ===
print("=" * 60)
print("Example 5: 1D Eigenfrequencies (Helmholtz)")
print("=" * 60)

L = 1.0           # m, waveguide length
eps_r = 1.0
mu_r = 1.0
c = c_0 / np.sqrt(eps_r * mu_r)

for m in range(1, 6):
    f_m = m * c / (2 * L)
    lambda_m = c / f_m
    print(f"  Mode m={m}: f={f_m*1e-9:.4f} GHz, lambda={lambda_m*1e3:.4f} mm")

print()
print("=" * 60)
print("All examples completed successfully.")
print("=" * 60)
