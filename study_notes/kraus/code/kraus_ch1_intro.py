"""
Kraus 'Antennas' 2nd Edition — Chapter 1: Introduction
======================================================
Key topics:
- Dimensional analysis and SI unit conventions
- Antenna taxonomy and field regions
- Fundamental antenna parameters (directivity, gain, effective aperture, beam width)
- Physical constants from scipy.constants
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

# ─── Physical Constants ───────────────────────────────────────────────────────
c = constants.c          # speed of light in vacuum (m/s)
eps0 = constants.epsilon_0   # permittivity of free space (F/m)
mu0 = constants.mu_0         # permeability of free space (H/m)
Z0  = np.sqrt(mu0 / eps0)   # intrinsic impedance of free space (~377 Ω)
ETA0 = Z0                    # alias

print("=" * 60)
print("Kraus Chapter 1 — Introduction: Key Constants")
print("=" * 60)
print(f"c  = {c:.4e} m/s")
print(f"ε₀ = {eps0:.4e} F/m")
print(f"μ₀ = {mu0:.4e} H/m")
print(f"Z₀ = {Z0:.4f} Ω")

# ─────────────────────────────────────────────────────────────────────────────
# Example 1: Dimensional Analysis Check
# Kraus p.1403 — Example 1
# D = 200 pC/m² → check that left side M/L² equals right side M/L³·T·I
# ─────────────────────────────────────────────────────────────────────────────
def dimensional_check():
    """
    Dimensional balance check for D = ε₀·E.
    [D] = C/m² = I·T / L²
    [ε₀] = F/m = I²·T⁴ / (L³·M)
    [E] = V/m = M·L / (I·T³)
    Left side: I·T / L²
    Right side: I²·T⁴/(L³·M) · M·L/(I·T³) = I·T / L²  ✓
    """
    print("\n--- Example 1: Dimensional Analysis Check ---")
    print("D = ε₀ · E  →  [C/m²] = [F/m]·[V/m]  ✓  Both sides: I·T/L²")
    print("Flux density D = 200 pC/m² = 2×10⁻¹⁰ C/m²")
    D = 200e-12   # C/m²
    E_field = D / eps0   # V/m
    print(f"Corresponding E-field: E = D/ε₀ = {E_field:.4e} V/m")

dimensional_check()

# ─────────────────────────────────────────────────────────────────────────────
# Example 2: Antenna taxonomy — region names
# ─────────────────────────────────────────────────────────────────────────────
def antenna_regions():
    """
    Kraus Table 1-2 / Sec. 1-5: Antenna field zones
    Reactive near field  : r < 0.1·λ
    Radiating near field (Fresnel): 0.1·λ < r < 2·D²/λ
    Far field (Fraunhofer) : r > 2·D²/λ  (D = maximum antenna dimension)
    """
    print("\n--- Example 2: Antenna Field Regions ---")
    freq = 300e6           # 300 MHz
    lam = c / freq         # wavelength = 1 m
    D   = 0.5 * lam        # largest antenna dimension = λ/2
    r_reactive = 0.1 * lam
    r_fraunhofer = 2 * D**2 / lam
    print(f"f = {freq/1e6} MHz  →  λ = {lam:.3f} m")
    print(f"Reactive near-field boundary:  r = 0.1·λ = {r_reactive:.3f} m")
    print(f"Far-field boundary (Fraunhofer): r > 2·D²/λ = {r_fraunhofer:.3f} m")
    return lam, D, freq

lam, D, freq = antenna_regions()

# ─────────────────────────────────────────────────────────────────────────────
# Example 3: Free-space wavelength and wave number
# ─────────────────────────────────────────────────────────────────────────────
def wavelength_and_k():
    """
    Kraus — given frequency → λ, then k = 2π/λ
    """
    print("\n--- Example 3: λ and k at common frequencies ---")
    freqs_MHz = [30, 300, 3000]   # MHz
    for f in freqs_MHz:
        lam_m = c / (f * 1e6)
        k_rad_m = 2 * np.pi / lam_m
        print(f"  f={f:4d} MHz:  λ={lam_m:.4f} m,  k={k_rad_m:.4f} rad/m")
    return

wavelength_and_k()

# ─────────────────────────────────────────────────────────────────────────────
# Example 4: SI unit prefixes (from Kraus Table inside front cover)
# ─────────────────────────────────────────────────────────────────────────────
def unit_prefixes():
    """
    Kraus Sec 1-6: SI prefixes for conciseness.
    """
    print("\n--- Example 4: SI Prefixes ---")
    prefixes = {
        'p': 1e-12,   # pico
        'n': 1e-9,    # nano
        'µ': 1e-6,    # micro
        'm': 1e-3,    # milli
        'k': 1e3,     # kilo
        'M': 1e6,     # mega
        'G': 1e9,     # giga
    }
    for sym, val in prefixes.items():
        print(f"  {sym:2s} = {val:.0e}")
    return

unit_prefixes()

# ─────────────────────────────────────────────────────────────────────────────
# Example 5: Antenna pattern quantities — HPBW, FBR, null locations
# ─────────────────────────────────────────────────────────────────────────────
def pattern_quantities():
    """
    Kraus Sec 3-1 to 3-16 / Chapter 2:
    HPBW = Half-power beam width  (–3 dB points)
    FBR  = Front-to-back ratio    (dB)
    """
    print("\n--- Example 5: Pattern Quantities ---")
    # A typical cos²(θ) pattern (unidirectional, Sec 3-10)
    theta = np.linspace(0, np.pi, 1000)
    U_relative = np.cos(theta)**2          # radiation intensity pattern
    # HPBW for cos² pattern: cos²(θ) = 0.5 → θ = 45° → HPBW = 90° = π/2 rad
    hp_bw = 2 * np.degrees(np.arccos(np.sqrt(0.5)))
    print(f"  cos²(θ) pattern HPBW = {hp_bw:.1f}°")
    print(f"  Directivity for unidirectional cos² pattern = 3  (D = 2(n+1), n=1)")
    return

pattern_quantities()

# ─────────────────────────────────────────────────────────────────────────────
# Example 6: Plot all six power-pattern types from Sec 3-5 to 3-12
# ─────────────────────────────────────────────────────────────────────────────
def plot_ch1_patterns():
    """
    Kraus Sec 3-5 to 3-12: Six standard power patterns
    1. Hemispheric   (Sec 3-5)
    2. Unidirectional cosine  (Sec 3-6)
    3. Bidirectional cosine    (Sec 3-7)
    4. Sine (doughnut)         (Sec 3-8)
    5. Sine-squared (doughnut) (Sec 3-9)
    6. Unidirectional cosine² (Sec 3-10)
    """
    fig, axes = plt.subplots(2, 3, subplot_kw={'projection': 'polar'}, figsize=(12, 8))
    theta = np.linspace(0, 2*np.pi, 2001)
    patterns = {
        'Hemispheric\n(Sec 3-5)':   (np.where(np.sin(theta) >= 0, 1.0, 0.0), axes[0,0]),
        'Cosine\n(Sec 3-6)':        (np.abs(np.sin(theta)),                  axes[0,1]),
        'Bi-dir cosine\n(Sec 3-7)': (np.abs(np.sin(theta)) + np.abs(np.sin(np.pi - theta)), axes[0,2]),
        'Sine (doughnut)\n(Sec 3-8)':  (np.abs(np.sin(theta)),                  axes[1,0]),
        'Sine² (doughnut)\n(Sec 3-9)': (np.sin(theta)**2,             axes[1,1]),
        'Cosine²\n(Sec 3-10)':    (np.cos(theta)**2 * (np.cos(theta)>=0).astype(float), axes[1,2]),
    }
    fig.suptitle("Kraus Ch1 — Six Standard Power Patterns (Sec 3-5 to 3-12)", fontsize=14)
    for title, (P, ax) in patterns.items():
        ax.plot(theta, P)
        ax.set_title(title, fontsize=9)
        ax.set_ylim(0, 1.2)
    plt.tight_layout()
    out = "/home/ubuntu/.openclaw/workspace/textbooks/kraus/code/kraus_ch1_power_patterns.png"
    plt.savefig(out, dpi=150, bbox_inches='tight')
    print(f"\n✓ Saved: {out}")
    plt.close()
    return

plot_ch1_patterns()

print("\n✓ Chapter 1 complete.")
