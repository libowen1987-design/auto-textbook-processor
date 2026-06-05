#!/usr/bin/env python3
"""
Bondeson Ch8 Examples — Summary and Overview
Chapter 8: Method comparison, complexity, multigrid, iterative solvers
"""
import numpy as np
import scipy.constants as sc

c_0 = sc.speed_of_light

# === Example 1: Method Comparison — Unknown Count ===
print("=" * 60)
print("Example 1: Computational Cost — FDTD vs FEM vs MoM")
print("=" * 60)

def fdtd_unknowns(Nx, Ny, Nz):
    """6 components per Yee cell."""
    return Nx * Ny * Nz * 6

def fem_unknowns_nodes(Nx, Ny, Nz, nodes_per_cell=8):
    """Tetrahedral FEM: ~8 nodes per cell."""
    ncells = Nx * Ny * Nz
    return ncells * nodes_per_cell

def fem_unknowns_edges(Nx, Ny, Nz):
    """Edge elements: more DOFs than nodes but divergence-free."""
    return Nx * Ny * Nz * 12  # ~12 edge DOFs per cell

def mom_unknowns(Npanels):
    """MoM: one unknown per panel (surface discretization)."""
    return Npanels

print(f"  {'Grid':>12}  {'FDTD':>10}  {'FEM(node)':>12}  {'FEM(edge)':>11}  {'MoM':>9}")
for grid in [(20,20,20), (50,50,50), (100,100,100)]:
    Nx, Ny, Nz = grid
    total = Nx*Ny*Nz
    fdd = fdtd_unknowns(Nx,Ny,Nz)
    fe_n = fem_unknowns_nodes(Nx,Ny,Nz)
    fe_e = fem_unknowns_edges(Nx,Ny,Nz)
    print(f"  {total:>12,}  {fdd:>10,}  {fe_n:>12,}  {fe_e:>11,}  {'Npanels':>9}")
print()

# === Example 2: Multigrid Complexity ===
print("=" * 60)
print("Example 2: Multigrid — O(N) vs Iterative O(N²)")
print("=" * 60)

def multigrid_complexity(N):
    """MG: ~5N per V-cycle (coarse grid correction + smoothing)."""
    return 5 * N

def gauss_seidel_complexity(N, iterations=100):
    """GS: O(N) per iter × 100 iters."""
    return 100 * N**2

for N in [100, 1000, 10000, 100000]:
    mg_ops = multigrid_complexity(N)
    gs_ops = gauss_seidel_complexity(N)
    ratio = gs_ops / mg_ops
    print(f"  N={N:>7,} → MG ops≈{mg_ops:>12,}  GS ops≈{gs_ops:>12,}  ratio≈{ratio:.0f}x")
print()

# === Example 3: CFL Limit Impact ===
print("=" * 60)
print("Example 3: FDTD CFL Limit — Impact on Long-Time Simulation")
print("=" * 60)

freq_low = 1e6    # 1 MHz (long wave)
freq_mid = 1e9   # 1 GHz (microwave)
freq_high = 10e9 # 10 GHz

dx = 1e-3  # 1mm grid
dt_cfl = dx / (c_0 * np.sqrt(3))
T_sim = 1e-3  # 1ms simulation (interesting physics timescale)

for freq in [freq_low, freq_mid, freq_high]:
    T_wave = 1.0 / freq
    n_steps = int(T_sim / dt_cfl)
    time_per_step_us = 1e-6  # estimated FDTD time per step
    total_time_s = n_steps * time_per_step_us
    print(f"  f={freq*1e-6:.0f}MHz  T_wave={T_wave:.0e}s  "
          f"steps={n_steps:>12,}  walltime={total_time_s:.2f}s")
print()

# === Example 4: Memory Scaling ===
print("=" * 60)
print("Example 4: Memory Scaling — Sparse vs Dense")
print("=" * 60)

for N in [1000, 10000, 100000, 1000000]:
    # Sparse FDTD/FEM: ~7N nonzero entries (3D Yee)
    sparse_entries = 7 * N
    sparse_mb = sparse_entries * 8 / 1e6
    # Dense MoM: N×N complex
    dense_mb = (N**2) * 16 / 1e6  # 16 bytes per complex
    print(f"  N={N:>8,} → sparse={sparse_mb:>8.2f}MB  dense={dense_mb:>10.2f}MB")
print()

# === Example 5: FMM Speedup ===
print("=" * 60)
print("Example 5: FMM/MLFMA Speedup for MoM")
print("=" * 60)

for N in [100, 1000, 10000, 50000, 100000]:
    mom = N**2 / 2  # approximate LU solve cost
    mlfma = N * np.log2(N) * 20  # 20NlogN estimate
    speedup = mom / mlfma
    print(f"  N={N:>7,} → MoM={mom:>15,.0f}  MLFMA≈{mlfma:>10,.0f}  speedup={speedup:>7,.0f}x")
print()

# === Example 6: Method Selection Guide ===
print("=" * 60)
print("Example 6: Method Selection Guide")
print("=" * 60)

cases = [
    ("Open region, wire antenna", "MoM"),
    ("Closed cavity, complex geometry", "FEM (edge)"),
    ("Wideband microwave scattering", "FDTD"),
    ("Low-frequency eddy currents", "FEM (implicit)"),
    (" electrically large, smooth", "FDTD / Hybrid"),
    ("Dense mesh, singular fields", "FEM (adaptive)"),
]
for problem, method in cases:
    print(f"  {problem:<35} → {method}")
print()

print("=" * 60)
print("All examples completed successfully.")
print("=" * 60)
