#!/usr/bin/env python3
"""
Bondeson Ch2 Examples — Convergence, Extrapolation, Integration Rules
"""
import numpy as np
import scipy.constants as sc

c_0 = sc.speed_of_light
mu_0 = sc.mu_0
eps_0 = sc.epsilon_0

# === Example 1: Midpoint vs Simpson Convergence ===
print("=" * 60)
print("Example 1: Convergence of Midpoint and Simpson Rules")
print("=" * 60)

def midpoint_integral_2d(z, a, n):
    """
    Compute I(z,a) = ∫₀ᵃ ∫₀ᵃ dx'dy' / sqrt(x'^2 + y'^2 + z^2)
    using midpoint rule with n×n cells.
    """
    h = a / n
    xs = np.linspace(0, a, n, endpoint=False) + h / 2
    ys = xs.copy()
    total = 0.0
    for x in xs:
        for y in ys:
            total += h * h / np.sqrt(x**2 + y**2 + z**2)
    return total

def simpson_integral_2d(z, a, n):
    """
    Compute I(z,a) using Simpson's rule (2D).
    """
    h = a / n
    xs = np.linspace(0, a, n + 1)
    ys = xs.copy()
    total = 0.0
    for i in range(n):
        x1 = xs[i]**2
        x2 = (xs[i] + h/2)**2
        x3 = (xs[i] + h)**2
        for j in range(n):
            y1 = ys[j]**2
            y2 = (ys[j] + h/2)**2
            y3 = (ys[j] + h)**2
            zs = z**2
            total += (
                1/np.sqrt(x1+y1+zs) + 1/np.sqrt(x1+y3+zs)
              + 1/np.sqrt(x3+y1+zs) + 1/np.sqrt(x3+y3+zs)
              + 4/np.sqrt(x2+y1+zs) + 4/np.sqrt(x2+y3+zs)
              + 4/np.sqrt(x1+y2+zs) + 4/np.sqrt(x3+y2+zs)
              + 16/np.sqrt(x2+y2+zs)
            ) * h * h / 36.0
    return total

# Exact value: I(1,1) = π/(2√2) * arctanh(1/√2)... let's use high-res ref
# High-res reference
I_exact = 0.79335912

z, a = 1.0, 1.0
results = []
for n in [5, 10, 20, 40]:
    I_m = midpoint_integral_2d(z, a, n)
    I_s = simpson_integral_2d(z, a, n)
    err_m = abs(I_m - I_exact)
    err_s = abs(I_s - I_exact)
    results.append((n, 1.0/n, I_m, I_s, err_m, err_s))
    print(f"n={n:3d}  h={1/n:.4f}  Imid={I_m:.6f}  Isim={I_s:.6f}  "
          f"Err_m={err_m:.2e}  Err_s={err_s:.2e}")

# Fit convergence order
hs = np.array([r[1] for r in results])
errs_m = np.array([r[4] for r in results])
p_m = np.log(errs_m[0]/errs_m[1]) / np.log(hs[0]/hs[1])
print(f"\nEstimated midpoint convergence order: p ≈ {p_m:.2f} (expect ~2)")
print()

# === Example 2: Extrapolation to Zero Cell Size ===
print("=" * 60)
print("Example 2: Richardson Extrapolation")
print("=" * 60)

def richardson_extrapolate(I_hs, hs, p):
    """
    Richardson extrapolation: I0 ≈ Ih + (Ih - I2h)/(2^p - 1)
    Use first two values.
    """
    I1, I2 = I_hs[0], I_hs[1]
    h1, h2 = hs[0], hs[1]
    ratio = h1 / h2  # typically 2 for uniform refinement
    I0 = I2 + (I2 - I1) / (ratio**p - 1)
    return I0

# Use n=10 and n=20 midpoint results for linear extrapolation in h^2
I_10 = results[1][2]  # n=10
I_20 = results[2][2]  # n=20
I_extrap = richardson_extrapolate([I_10, I_20], [1/10, 1/20], p=2)
print(f"I(h=1/10) = {I_10:.6f}")
print(f"I(h=1/20) = {I_20:.6f}")
print(f"Richardson extrapolated I(0) ≈ {I_extrap:.6f}")
print(f"Exact I(1,1) ≈ {I_exact:.6f}")
print(f"Extrapolation error: {abs(I_extrap - I_exact):.2e}")
print()

# === Example 3: Order of Convergence Estimation ===
print("=" * 60)
print("Example 3: Order of Convergence Estimation (Eq 2.4)")
print("=" * 60)

def estimate_order(I3, I2, I1, h3, h2, h1):
    """Estimate p using three consecutive resolutions."""
    return np.log((I3 - I2)/(I2 - I1)) / np.log(h3/h2)

I_vals = np.array([r[2] for r in results])
h_vals = np.array([r[1] for r in results])

p_est = estimate_order(I_vals[0], I_vals[1], I_vals[2],
                       h_vals[0], h_vals[1], h_vals[2])
print(f"Estimated p from n=5,10,20: {p_est:.3f} (expect ~2.0)")
p_est2 = estimate_order(I_vals[1], I_vals[2], I_vals[3],
                       h_vals[1], h_vals[2], h_vals[3])
print(f"Estimated p from n=10,20,40: {p_est2:.3f} (expect ~2.0)")
print()

# === Example 4: Singular Problem (z=0) ===
print("=" * 60)
print("Example 4: Singular Problem — Convergence at z=0")
print("=" * 60)

z_s = 0.0
I_exact_s = 2.0 * np.log(1.0 + np.sqrt(2.0))  # I(0,1) exact
print(f"Exact I(0,1) = {I_exact_s:.6f}")

results_s = []
for n in [5, 10, 20, 40]:
    I_m = midpoint_integral_2d(z_s, a, n)
    err = abs(I_m - I_exact_s)
    results_s.append((n, I_m, err))
    print(f"n={n:3d}  Imid={I_m:.6f}  Error={err:.2e}")

# Singular problem convergence order
I_vals_s = np.array([r[1] for r in results_s])
h_vals_s = 1.0 / np.array([r[0] for r in results_s])
p_s = estimate_order(I_vals_s[0], I_vals_s[1], I_vals_s[2],
                     h_vals_s[0], h_vals_s[1], h_vals_s[2])
print(f"\nSingular problem convergence order: p ≈ {p_s:.2f} (expect ~1)")
print()

# === Example 5: Capacitance Grid Refinement ===
print("=" * 60)
print("Example 5: Capacitance Convergence — Reentrant Corner")
print("=" * 60)

# Simulated capacitance data from Table 3.1 (Bondeson p.26)
# (n, h, C in pF/m)
cap_data = [
    (10, 0.1000, 92.09715),
    (20, 0.0500, 91.18849),
    (30, 0.0333, 90.94575),
    (40, 0.0250, 90.83912),
    (50, 0.0200, 90.78080),
]
print("Capacitance data (coaxial rectangle):")
for n, h, C in cap_data:
    print(f"  n={n:3d}  h={h:.4f}  C={C:.5f} pF/m")

# Fit C vs h^1.5 (expected p=1.5 for reentrant corner)
hs_cap = np.array([d[1] for d in cap_data])
Cs_cap = np.array([d[2] for d in cap_data])
p_cap = estimate_order(Cs_cap[0], Cs_cap[1], Cs_cap[2],
                       hs_cap[0], hs_cap[1], hs_cap[2])
print(f"\nEstimated convergence order p ≈ {p_cap:.2f} (expect ~1.5 for 270° corner)")
print()

# Extrapolate to h=0
I_extrap_cap = richardson_extrapolate(Cs_cap[:2], hs_cap[:2], p=1.5)
print(f"Extrapolated C(h→0) ≈ {I_extrap_cap:.2f} pF/m")
print()

print("=" * 60)
print("All examples completed successfully.")
print("=" * 60)
