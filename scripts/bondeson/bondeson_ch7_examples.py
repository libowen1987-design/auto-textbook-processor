#!/usr/bin/env python3
"""
Bondeson Ch7 Examples — Method of Moments
Chapter 7: MoM, Green function, EFIE/MFIE/CFIE, Hallen equation
"""
import numpy as np
import scipy.constants as sc

c_0 = sc.speed_of_light
eps_0 = sc.epsilon_0
mu_0 = sc.mu_0
eta_0 = np.sqrt(mu_0 / eps_0)

# === Example 1: 3D Green Function (Static) ===
print("=" * 60)
print("Example 1: 3D Green Function — Potential from Point Charge")
print("=" * 60)

def green_3d_static(r, r_prime):
    """G(r,r') = 1/(4πϵ₀) * 1/|r-r'|"""
    R = np.linalg.norm(r - r_prime)
    if R < 1e-12:
        return np.inf
    return 1.0 / (4 * np.pi * eps_0 * R)

q = 1e-9  # 1 nC
for d_mm in [1, 5, 10, 50, 100]:
    d = d_mm * 1e-3
    phi = green_3d_static(np.array([d, 0, 0]), np.zeros(3)) * q
    print(f"  r={d_mm:4d}mm  φ={phi*1e3:.4f} mV")
print()

# === Example 2: 2D Green Function (Logarithmic) ===
print("=" * 60)
print("Example 2: 2D Green Function (Static) — ln|G|")
print("=" * 60)

def green_2d_static(r, r_prime, R0=1.0):
    """G = (1/2πϵ₀) * ln(R0/|r-r'|)"""
    R = np.linalg.norm(r - r_prime)
    if R < 1e-12:
        return -np.inf
    return np.log(R0 / R) / (2 * np.pi * eps_0)

for d_mm in [1, 5, 10, 50]:
    d = d_mm * 1e-3
    G = green_2d_static(np.array([d, 0]), np.zeros(2))
    print(f"  d={d_mm:4d}mm  G={G:.4e}")
print()

# === Example 3: MoM Matrix Fill — Self and Mutual Impedance ===
print("=" * 60)
print("Example 3: MoM — Self and Mutual Impedance")
print("=" * 60)

def mom_mutual_Z(d, l, omega, epsilon_r=1.0):
    """
    Mutual impedance between two parallel wire segments
    Z ≈ j*ω*μ₀/(2π) * ln(d/l) for short wires at large separation.
    """
    if d < 1e-12:
        return 0.0
    # Simplified static mutual capacitance
    return 1j * omega * mu_0 / (2*np.pi) * np.log(d / l)

l = 0.01  # 10mm wire segment
for sep_mm in [1, 5, 10, 50]:
    d = sep_mm * 1e-3
    Z = mom_mutual_Z(d, l, 2*np.pi*1e9)
    print(f"  sep={sep_mm:4d}mm  Z≈{Z:.4e} ohm")
print()

# === Example 4: MoM Dense Matrix Complexity ===
print("=" * 60)
print("Example 4: MoM Dense Matrix — O(N²) Complexity")
print("=" * 60)

for N in [100, 1000, 10000, 100000]:
    mem_bytes = N * N * 8  # 8 bytes per complex128
    mem_mb = mem_bytes / 1e6
    print(f"  N={N:>7,d} unknowns → matrix = {N}x{N} → {mem_mb:.2f} MB")
print()

# === Example 5: Wire Antenna — Hallen Equation ===
print("=" * 60)
print("Example 5: Wire Antenna — Hallen Equation")
print("=" * 60)

def hallen_current_pulse(L, a, V0, freq, N=50):
    """
    Approximate current distribution on a center-fed dipole
    using pulse basis functions.
    Returns I (N vector) in amps.
    """
    k = 2 * np.pi * freq / c_0
    z = np.linspace(-L/2, L/2, N+1)
    dz = L / N
    # Simplified: triangular-like current for half-wave dipole
    I = np.zeros(N+1)
    for i in range(N+1):
        if abs(z[i]) < L/2:
            sin_arg = k * L/2 * np.cos(k * z[i])
            I[i] = V0 / (eta_0 / 2 * np.cos(k * z[i]) + 1j * 1e-10)
    return z, I

freq = 300e6  # 300 MHz
L = c_0 / freq / 2  # half-wave dipole
V0 = 1.0
z, I = hallen_current_pulse(L, 0.001, V0, freq, N=40)
print(f"  f={freq*1e-6:.0f} MHz  L={L:.4f}m (half-wave)")
print(f"  max |I| = {np.max(np.abs(I)):.4f} A at feed point")
print()

# === Example 6: Radar Cross Section (RCS) ===
print("=" * 60)
print("Example 6: Radar Cross Section (RCS) Estimate")
print("=" * 60)

def rcs_sphere(a, freq):
    """RCS of a perfectly conducting sphere (Mie series, high freq limit)."""
    k = 2 * np.pi * freq / c_0
    sigma_optical = np.pi * a**2  # optical cross section
    return sigma_optical

def rcs_plate(w, h, freq):
    """Physical optics RCS of a rectangular plate."""
    k = 2 * np.pi * freq / c_0
    sigma = 4 * np.pi * (w * h)**2 / (c_0 / freq)**2
    return sigma

a = 0.1  # 10cm sphere
freq = 10e9  # 10 GHz
sigma_sph = rcs_sphere(a, freq)
sigma_plate = rcs_plate(0.1, 0.1, freq)
print(f"  Sphere r={a*100:.0f}cm at 10 GHz:")
print(f"    σ_optical = {sigma_sph:.4f} m² = {sigma_sph*1e6:.2f} cm²")
print(f"  Plate 10x10cm at 10 GHz:")
print(f"    σ ≈ {sigma_plate:.4f} m² = {sigma_plate*1e6:.2f} cm²")
print()

# === Example 7: FMM Complexity Reduction ===
print("=" * 60)
print("Example 7: FMM — O(N log N) vs O(N²)")
print("=" * 60)

for N in [100, 1000, 10000, 100000]:
    cost_mom = N**2
    cost_fmm = N * np.log2(N)
    ratio = cost_mom / cost_fmm
    print(f"  N={N:>7,d}: MoM={cost_mom:>12,d}, FMM≈{cost_fmm:>8,.0f}, speedup≈{ratio:.0f}x")
print()

print("=" * 60)
print("All examples completed successfully.")
print("=" * 60)
