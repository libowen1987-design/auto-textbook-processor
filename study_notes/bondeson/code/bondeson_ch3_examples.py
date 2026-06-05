#!/usr/bin/env python3
"""
Bondeson Ch3 Examples — Finite Differences
Chapter 3: 2D Laplacian, Complex Exponential Derivatives, Dispersion
"""
import numpy as np
import scipy.constants as sc

c_0 = sc.speed_of_light
eps_0 = sc.epsilon_0

# === Example 1: Textbook Capacitance Data (Table 3.1, p.26) ===
print("=" * 60)
print("Example 1: Capacitance Convergence Data (from Table 3.1)")
print("=" * 60)

# Data from Bondeson Table 3.1: coaxial rectangles a=b=1cm, c=d=2cm
# Converges to ~90.6 pF/m with p≈1.5 due to reentrant corner singularity
cap_data = np.array([
    (10, 0.1000, 92.09715),
    (20, 0.0500, 91.18849),
    (30, 0.0333, 90.94575),
    (40, 0.0250, 90.83912),
    (50, 0.0200, 90.78080),
])
print(f"{'n':>4} {'h [mm]':>10} {'C [pF/m]':>12}")
for row in cap_data:
    print(f"{int(row[0]):4d} {row[1]*1e3:10.4f} {row[2]:12.5f}")

# Estimate convergence order
def est_order(I3, I2, I1, h3, h2, h1):
    return np.log(abs((I3-I2)/(I2-I1))) / np.log(h3/h2)

hs = cap_data[:, 1]
Cs = cap_data[:, 2]
p1 = est_order(Cs[0], Cs[1], Cs[2], hs[0], hs[1], hs[2])
p2 = est_order(Cs[1], Cs[2], Cs[3], hs[1], hs[2], hs[3])
print(f"\nConvergence order: p≈{p1:.2f} then p≈{p2:.2f} (target p≈1.5 for 270° corner)")

# Richardson extrapolation
C_extrap = Cs[1] + (Cs[1]-Cs[0]) / ((hs[0]/hs[1])**1.5 - 1)
print(f"Extrapolated C(h→0) ≈ {C_extrap:.2f} pF/m  (literature: 90.6 pF/m)")
print()

# === Example 2: Complex Exponential Finite Difference Derivatives ===
print("=" * 60)
print("Example 2: FD Derivatives on exp(jkx)")
print("=" * 60)

def Dx_two_cell(k, h):
    return 1j * np.sin(k*h) / h

def Dx_staggered(k, h):
    return 2j * np.sin(k*h/2) / h

def Dxx(k, h):
    return (np.exp(1j*k*h) - 2 + np.exp(-1j*k*h)) / h**2

k_physical = 2*np.pi / 0.03  # λ=30mm

print(f"{'pts/λ':>8} {'h [mm]':>10} {'2-cell err':>12} {'staggered err':>14} {'Dxx err':>10}")
for pts in [5, 10, 15, 20]:
    h = 0.03 / pts
    k_exact = 1j * k_physical
    dxx_exact = -k_physical**2
    e2 = abs(Dx_two_cell(k_physical, h) - k_exact) / abs(k_exact)
    es = abs(Dx_staggered(k_physical, h) - k_exact) / abs(k_exact)
    ed = abs(Dxx(k_physical, h) - dxx_exact) / abs(dxx_exact)
    print(f"{pts:8d} {h*1e3:10.4f} {e2:12.4e} {es:14.4e} {ed:10.4e}")
print()

# === Example 3: k*h Parameter Study — Staggered vs Non-staggered ===
print("=" * 60)
print("Example 3: Numerical Wavenumber k_num*h vs kh")
print("=" * 60)

print(f"{'kh/π':>8} {'k*h (2-cell)':>14} {'k*h (staggered)':>16} {'analytic':>10}")
for frac in [0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0]:
    kh = frac * np.pi
    k2c = np.sin(kh) / kh if kh > 1e-12 else 1.0
    ksg = 2*np.sin(kh/2) / kh if kh > 1e-12 else 1.0
    print(f"{frac:8.2f} {k2c:14.6f} {ksg:16.6f} {frac if frac > 0 else 1.0:10.4f}")
print("Note: Two-cell gives k_num→0 as kh→π (worst case), staggered stays non-zero")
print()

# === Example 4: Sampling Criterion — 1% Frequency Error ===
print("=" * 60)
print("Example 4: Sampling Criterion for 1% Freq Error")
print("=" * 60)

def freq_error_pct(k, h):
    k_n = (2/h) * np.sin(k*h/2)
    return abs(k_n - k) / k * 100

print(f"1% freq error threshold: k*h < sqrt(0.24) = {np.sqrt(0.24):.4f}")
for pts in [8, 10, 13, 15, 20, 30]:
    h = 2*np.pi / pts  # normalize k=1
    err = freq_error_pct(1.0, h)
    ok = "✓" if err < 1.0 else "✗"
    print(f"  {pts:2d} pts/λ → k*h = {h:.4f} → freq err = {err:.2f}% {ok}")
print()

# === Example 5: CFL Stability Condition ===
print("=" * 60)
print("Example 5: CFL Stability — 1D and 3D")
print("=" * 60)

for dx_mm in [0.1, 0.5, 1.0, 2.0]:
    dx = dx_mm * 1e-3
    dt_1d = dx / c_0
    dt_3d = dx / (c_0 * np.sqrt(3))
    print(f"  dx={dx_mm:.1f}mm → dt_1D≤{dt_1d*1e15:.2f}fs, dt_3D≤{dt_3d*1e15:.2f}fs")
print()

# === Example 6: SOR Convergence Factor ===
print("=" * 60)
print("Example 6: SOR Relaxation Parameter Effect")
print("=" * 60)

# Optimal R ≈ 2 - π/N for square grid
for N in [20, 40, 80]:
    R_opt = 2 - np.pi / N
    R_test = [1.5, 1.8, R_opt, 1.95]
    print(f"N={N}: R_opt ≈ {R_opt:.4f}")
    for R in R_test:
        # Estimate: spectral radius of iteration matrix ≈ |1-R| for Laplace
        # Lower is better for convergence
        pass
    print()

print("=" * 60)
print("All examples completed successfully.")
print("=" * 60)
