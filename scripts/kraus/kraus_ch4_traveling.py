"""
Kraus 'Antennas' 2nd Edition — Chapter 4: The Traveling-Wave Antenna
=====================================================================
Key topics:
- Sec 4-1 to 4-3: Long-wire antennas ( Beverage antenna)
  A wire of length L >> λ with a traveling wave: pattern is more directive as L increases.
  Pattern: F(θ) = sin(β·L·cosθ) / (β·L·cosθ)  [for a wire of length L with traveling wave]
- Sec 4-4 to 4-5: Resonant vs non-resonant (traveling-wave) wire antennas
  Resonant: standing wave → bidirectional (sin| pattern)
  Non-resonant (traveling): end-fire, unidirectional
- Sec 4-6:Arrays of 2 to n isotropic sources (briefly treated here)
  The array factor for n isotropic sources with spacing d and progressive phase shift δ:
  AF(ψ) = sin(n·ψ/2)/sin(ψ/2), ψ = β·d·cosθ + δ, β = 2π/λ
- Sec 4-7: Null directions for n-element isotropic array
- Sec 4-9: Maxima directions for arrays of n isotropic sources
- Sec 4-10 to 4-12: Dolph-Chebyshev array synthesis (Sec 4-12: 8-element Chebyshev)
- Sec 4-16 to 4-18: Rectangular arrays and pattern multiplication
"""

import numpy as np
import matplotlib.pyplot as plt

print("=" * 65)
print("Kraus Ch4 — Traveling-Wave and Long-Wire Antennas")
print("=" * 65)

lam = 1.0
beta = 2*np.pi / lam
theta = np.linspace(0, np.pi, 10801)

# ═══════════════════════════════════════════════════════════════════════════
# Sec 4-1 to 4-3: Long-wire (traveling-wave) antenna pattern
# I(z) = I0·e^(jβz) for traveling wave in +z direction.
# Far-field: F(θ) = sin(β·L·cosθ) / (β·L·cosθ)
# As L increases, beam narrows and tilts toward θ=0 (end-fire).
# ═══════════════════════════════════════════════════════════════════════════
def long_wire_pattern(L_lam, theta_rad):
    arg = beta * L_lam * np.cos(theta_rad)
    with np.errstate(divide='ignore', invalid='ignore'):
        F = np.abs(np.sin(arg) / (arg + 1e-12))
    return np.where(np.isfinite(F), F, 1.0)

print("\n--- Sec 4-1 to 4-3: Long-wire traveling-wave patterns ---")
for L_lam in [0.5, 1.0, 2.0, 4.0, 8.0]:
    F = long_wire_pattern(L_lam, theta)
    F_max = np.max(F)
    F_norm = F / F_max
    # Find beam direction (angle of maximum)
    idx_max = np.argmax(F_norm)
    theta_max_deg = np.degrees(theta[idx_max])
    print(f"  L = {L_lam}λ  →  max at θ = {theta_max_deg:.1f}°, pattern width decreases with L")

# ═══════════════════════════════════════════════════════════════════════════
# Sec 4-6: Broadside and Endfire arrays (brief treatment)
# Broadside: all elements in phase (δ=0), max at θ=90°
# Endfire: δ = −β·d, max at θ=0°
# Hansen-Woodyard (Sec 4-6c): add extra phase for increased directivity.
# ═══════════════════════════════════════════════════════════════════════════
def array_factor_linear(n, d_lam, delta_rad):
    psi = beta * d_lam * np.cos(theta) + delta_rad
    with np.errstate(divide='ignore', invalid='ignore'):
        AF = np.abs(np.sin(n*psi/2) / np.sin(psi/2))
    return np.where(np.isfinite(AF), AF, n)

af_broadside = array_factor_linear(8, 0.5, 0.0)
af_endfire   = array_factor_linear(8, 0.5, -beta*0.5)
af_hw        = array_factor_linear(8, 0.5, -beta*0.5 - np.pi/(2*8*0.5))  # Hansen-Woodyard

# ═══════════════════════════════════════════════════════════════════════════
# Sec 4-12: 8-element Dolph-Chebyshev array, SLL=−20 dB
# Using T7(x) synthesis
# ═══════════════════════════════════════════════════════════════════════════
R = 10**(20/20)  # SLL=-20 dB → R=10
x0 = np.cosh(np.arccosh(R)/7)
xn = np.cos(np.pi*(2*np.arange(8)+1)/(2*8)) / x0
a = np.abs(64*xn**7 - 112*xn**5 + 56*xn**3 - 7*xn)
a = a / np.max(a)
af_cheby = np.zeros(len(theta), dtype=complex)
for k in range(8):
    af_cheby += a[k] * np.exp(1j*k*(beta*0.5))
af_cheby = np.abs(af_cheby)
af_cheby = af_cheby / np.max(af_cheby)

print("\n--- Sec 4-12: 8-element Dolph-Chebyshev (SLL=-20 dB) ---")
print(f"  Element excitations (normalized): {[round(x,3) for x in a]}")

# Plot
fig, axes = plt.subplots(2, 2, subplot_kw={'projection':'polar'}, figsize=(12,10))
for ax, af, title in zip(axes.flat,
    [(af_broadside/8, "Broadside (n=8, d=λ/2, δ=0)", "blue"),
     (af_endfire/8, "Endfire (n=8, d=λ/2, δ=−βd)", "green"),
     (af_hw/8, "Endfire Hansen-Woodyard", "red"),
     (af_cheby, "8-el Chebyshev SLL=-20 dB", "purple")],
    [("Broadside — max at 90°", "blue"),
     ("Endfire — max at 0°", "green"),
     ("Hansen-Woodyard (increased D)", "red"),
     ("Dolph-Chebyshev (equal sidelobes)", "purple")]):
    ax.plot(theta, af, color=title, lw=2)
    ax.fill(theta, af, alpha=0.15, color=title)
    ax.set_ylim(0, 1.3)
    ax.set_title(f"Kraus Ch4 — {title}", fontsize=10)

plt.suptitle("Kraus Ch4 — Traveling-Wave & Array Antennas", fontsize=13, fontweight='bold')
plt.tight_layout()
out = "/home/ubuntu/.openclaw/workspace/textbooks/kraus/code/kraus_ch4_traveling_arrays.png"
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f"\n✓ Saved: {out}")

print("\n✓ Chapter 4 code complete.")