#!/usr/bin/env python3
"""
Bondeson Ch5 Examples — FDTD Method
Chapter 5: 1D/3D FDTD, Yee cell, CFL stability, Dispersion analysis
"""
import numpy as np
import scipy.constants as sc

c_0 = sc.speed_of_light
eps_0 = sc.epsilon_0
mu_0 = sc.mu_0
eta_0 = np.sqrt(mu_0 / eps_0)

# === Example 1: CFL Stability Condition ===
print("=" * 60)
print("Example 1: CFL Stability Condition — 1D vs 3D")
print("=" * 60)

for dx_mm in [0.1, 0.5, 1.0, 2.0]:
    dx = dx_mm * 1e-3
    dt_1d = dx / c_0
    dt_3d = dx / (c_0 * np.sqrt(3))
    print(f"  dx={dx_mm:.1f}mm → dt_1D_max={dt_1d*1e15:.2f}fs  "
          f"dt_3D_max={dt_3d*1e15:.2f}fs")
print()

# === Example 2: Numerical Phase Velocity ===
print("=" * 60)
print("Example 2: Numerical Phase Velocity in 1D FDTD")
print("=" * 60)

def numerical_vp(c, dx, dt, k):
    """
    v_p = c / sqrt(1 - (c*dt/dx)^2 * sin^2(k*dx/2))
    """
    ratio = (c * dt / dx)**2
    sin2 = np.sin(k * dx / 2)**2
    radicand = 1.0 - ratio * sin2
    if radicand <= 0:
        return np.inf
    return c / np.sqrt(radicand)

c = c_0
k_physical = 2*np.pi / 0.03  # λ=30mm
dx = 0.003  # 3mm = λ/10
for CFL in [0.5, 0.8, 0.9, 0.99, 1.0]:
    dt = CFL * dx / c
    vp = numerical_vp(c, dx, dt, k_physical)
    err = (vp/c - 1) * 100
    status = "UNSTABLE" if CFL >= 1.0 else "OK"
    print(f"  CFL={CFL:.2f}  dt={dt*1e15:.2f}fs  "
          f"vp/c={vp/c:.4f}  err={err:+.2f}%  {status}")
print()

# === Example 3: Dispersion Error vs Resolution ===
print("=" * 60)
print("Example 3: Dispersion Error vs Points per Wavelength")
print("=" * 60)

k0 = 1.0  # normalize
freq_error = []
print(f"{'pts/λ':>8} {'k*h':>8} {'freq err (%)':>12} {'Δt_max':>12}")
for pts in [8, 10, 13, 15, 20, 30]:
    h = 2*np.pi / pts
    vp = numerical_vp(c, h, h/c, k0)  # CFL = 1
    err = (vp/c - 1) * 100
    ok = "✓" if err < 1.0 else "✗"
    print(f"{pts:8d} {k0*h:8.4f} {err:12.2f} {h/c*1e15:12.2f}fs {ok}")
print()

# === Example 4: 3D Cubic Cavity Eigenfrequencies ===
print("=" * 60)
print("Example 4: 3D Cubic Cavity Eigenfrequencies")
print("=" * 60)

def cavity_eigenfreq_cubic(a, m, n, p):
    """f_mnp = c/(2a) * sqrt(m² + n² + p²)"""
    return c_0 / (2*a) * np.sqrt(m**2 + n**2 + p**2)

a = 0.01  # 10mm cavity
modes = [(0,1,1,'TE'), (1,0,1,'TE'), (1,1,0,'TE'),
         (1,1,1,'TM'), (0,2,1,'TE'), (2,0,1,'TE'),
         (1,2,0,'TE'), (2,1,0,'TE')]
print(f"Cubic cavity a={a*1e3:.0f}mm")
for m, n, p, mode_type in modes:
    f = cavity_eigenfreq_cubic(a, m, n, p)
    lam = c_0 / f
    print(f"  ({m},{n},{p}) {mode_type}: f={f*1e-9:.4f} GHz  λ={lam*1e3:.2f}mm")
print()

# === Example 5: PML Reflection Estimate ===
print("=" * 60)
print("Example 5: PML Reflection Estimate")
print("=" * 60)

def pml_reflection(ncells, d_pml, kappa_max=1.0):
    """
    Simple PML reflection estimate.
    R ≈ exp(-kappa_max * d_pml / (cells * dx)) * some factor
    """
    # Standard PML: R ≈ exp(-sigma_max * dx * N)
    # For uniform PML: R ≈ exp(-d_pml/skin_depth)
    # skin_depth = 2*dx in well-designed PML
    r = np.exp(-ncells * np.log(10))  # ~10^N per cell reduction
    return r

for ncells in [4, 8, 12, 16]:
    R = pml_reflection(ncells, 1.0)
    print(f"  PML {ncells} cells → R ≈ {R:.2e}")
print()

# === Example 6: FDTD Memory Estimate ===
print("=" * 60)
print("Example 6: FDTD Memory Estimate — 3D Cavity")
print("=" * 60)

def fdtd_memory_unknowns(Nx, Ny, Nz, ncomponents=6):
    """6 E and H components per grid point in 3D Yee."""
    return Nx * Ny * Nz * ncomponents

for grid in [(50,50,50), (100,100,100), (200,200,200)]:
    Nx, Ny, Nz = grid
    unknowns = fdtd_memory_unknowns(Nx, Ny, Nz)
    memory_mb = unknowns * 8 / 1e6
    # FDTD cells in time (2 banks for E, 2 for H)
    total_banks = Nx * Ny * Nz * 4 * 8 / 1e6
    print(f"  Grid {Nx}x{Ny}x{Nz} = {unknowns:,} components ≈ {memory_mb:.2f} MB")
print()

print("=" * 60)
print("All examples completed successfully.")
print("=" * 60)
