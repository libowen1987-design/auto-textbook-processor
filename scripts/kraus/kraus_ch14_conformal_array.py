"""
Kraus 'Antennas' 2nd Edition — Chapter 14: Conformal Array Theory
==================================================================
Key topics:
- Sec 14-2 to 14-4: Array theory on curved surfaces (cylindrical, spherical)
  Element factor E_n(θ,φ) and array factor AF(θ,φ) for N-element conformal array.
  For a cylindrical array of N elements uniformly spaced around circumference:
    AF(θ,φ) = Σ_{n=0}^{N-1} I_n·e^(jn·ψ),  ψ = β·a·sinθ·cos(φ-φ_n) + δ_n
  where a = cylinder radius, φ_n = 2πn/N are element positions.
- Sec 14-5 to 14-8: Pattern multiplication for conformal arrays:
  F(θ,φ) = element_pattern(θ,φ) × AF(θ,φ)
  For small cylinder radius (a << λ): pattern close to flat array.
  For large radius (a >> λ): beam squint toward scan direction.
- Sec 14-9 to 14-11: Scan blindness and surface-wave effects in conformal arrays
  ψ_n = β·a·sinθ_s·cos(φ_s-φ_n) → when ψ_n = ±π → grating lobe or scan blind spot.
- Sec 14-12/14-13: Practical cylindrical arrays (example: N=12 elements, a=5λ)
  Directivity D ≈ N·D_element·η_ar (array efficiency η_ar ≈ 0.7 to 0.9)
- Sec 14-14/14-15: Spherical and hemispherical conformal arrays
  Full-coverage hemispherical array — scan 0° ≤ θ ≤ 90°, 0° ≤ φ < 360°
  Example: N=20 elements on hemisphere, radius a=3λ → D≈N·η_ar·D_iso ≈ 20×0.8×1.5 ≈ 24 (13.8 dBi)
- Sec 14-16: Active phased array modules (T/R modules)
  Phase shift per element: Δφ = β·d·sinθ_s (scan direction θ_s, φ_s)
- Sec 14-17: Conformal arrays for missiles and aircraft (low-profile integration)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
c = constants.c;  Z0 = np.sqrt(constants.mu_0/constants.epsilon_0)

print("=" * 60)
print("Kraus Ch14 — Conformal Array Theory")
print("=" * 60)

lam = 1.0;  beta = 2*np.pi/lam

# ═══════════════════════════════════════════════════════════════════════════
# Sec 14-3/14-4: Cylindrical conformal array — array factor
# N elements uniformly spaced around cylinder of radius a.
# ═══════════════════════════════════════════════════════════════════════════
def cylindrical_array_AF(N, a_lam, theta_deg, phi_deg):
    """
    Cylindrical array of N isotropic elements, uniformly spaced around circumference.
    a_lam = cylinder radius in wavelengths.
    """
    theta = np.deg2rad(theta_deg)
    phi   = np.deg2rad(phi_deg)
    AF = np.zeros(len(theta), dtype=complex)
    for n in range(N):
        phi_n = 2*np.pi*n/N
        psi = beta*a_lam*np.sin(theta)*np.cos(phi - phi_n)
        AF += np.exp(1j*psi)
    return np.abs(AF)/N

theta_deg = np.linspace(0, 180, 10801)
phi_deg = 0.0   # phi-plane cut

# Plot for different N values and cylinder radii
print("\n--- Sec 14-3/14-4: Cylindrical array pattern ---")
for N in [4, 8, 12]:
    AF = cylindrical_array_AF(N, 2.0, theta_deg, phi_deg)
    max_val = np.max(AF)
    print(f"  N={N}, a=2λ → max AF/N = {max_val:.3f}")

fig, axes = plt.subplots(1, 3, subplot_kw={'projection':'polar'}, figsize=(15, 5))
for ax, (N, a_lam) in zip(axes, [(4, 2.0), (8, 2.0), (12, 2.0)]):
    AF = cylindrical_array_AF(N, a_lam, theta_deg, phi_deg)
    ax.plot(np.deg2rad(theta_deg), AF, 'b-', lw=2)
    ax.fill(np.deg2rad(theta_deg), AF, alpha=0.15)
    ax.set_ylim(0, 1.3)
    ax.set_title(f"Kraus Ch14 — Cylindrical Array\nN={N}, a={a_lam}λ  (Sec 14-4)", fontsize=10)
plt.suptitle("Kraus Ch14 — Conformal Cylindrical Array Patterns", fontsize=12, fontweight='bold')
plt.tight_layout()
out = "/home/ubuntu/.openclaw/workspace/textbooks/kraus/code/kraus_ch14_cylindrical_array.png"
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f"\n✓ Saved: {out}")

# ═══════════════════════════════════════════════════════════════════════════
# Sec 14-5/14-6: Beam scanning in cylindrical array
# Scan direction (θ_s, φ_s) → progressive phase δ_n = -β·a·sinθ_s·cos(φ_s-φ_n)
# ═══════════════════════════════════════════════════════════════════════════
def cylindrical_array_scan(N, a_lam, theta_s, phi_s, theta_deg):
    theta = np.deg2rad(theta_deg)
    phi   = np.deg2rad(phi_s)
    AF = np.zeros(len(theta), dtype=complex)
    for n in range(N):
        phi_n = 2*np.pi*n/N
        psi = beta*a_lam*np.sin(theta)*np.cos(np.deg2rad(theta_deg) - phi_n)
        delta = -beta*a_lam*np.sin(np.deg2rad(theta_s))*np.cos(phi_s - phi_n)
        AF += np.exp(1j*(psi + delta))
    return np.abs(AF)/N

fig, axes = plt.subplots(1, 3, subplot_kw={'projection':'polar'}, figsize=(15, 5))
for ax, (theta_s, phi_s, label) in zip(axes, [
    (0, 0, "Broadside (θ_s=0°)"),
    (30, 0, "Scan 30°"),
    (60, 0, "Scan 60°")]):
    AF = cylindrical_array_scan(12, 2.0, theta_s, phi_s, theta_deg)
    ax.plot(np.deg2rad(theta_deg), AF, 'b-', lw=2)
    ax.fill(np.deg2rad(theta_deg), AF, alpha=0.15)
    ax.set_ylim(0, 1.3)
    ax.set_title(f"Kraus Ch14 — {label}\n(N=12, a=2λ)", fontsize=10)
plt.suptitle("Kraus Ch14 — Cylindrical Array Scanning (Sec 14-5/14-6)", fontsize=12, fontweight='bold')
plt.tight_layout()
out2 = "/home/ubuntu/.openclaw/workspace/textbooks/kraus/code/kraus_ch14_cylindrical_scan.png"
plt.savefig(out2, dpi=150, bbox_inches='tight')
plt.close()
print(f"✓ Saved: {out2}")

# ═══════════════════════════════════════════════════════════════════════════
# Sec 14-7/14-8: Scan blindness — when ψ_n = ±π leads to zero in array factor
# Blind spot condition: β·a·sinθ_s·cos(φ_s-φ_n) = ±π  (mod 2π)
# For a=2λ, β·a=4π → sinθ_s = ±1/(2) → θ_s = 30° or 150° (for φ aligned)
# ═══════════════════════════════════════════════════════════════════════════
def scan_blindness(N=12, a_lam=2.0):
    print(f"\n--- Sec 14-9/14-10: Scan blindness condition ---")
    print(f"  For a={a_lam}λ, N={N}: scan blindness occurs at:")
    print(f"  ψ_n = β·a·sinθ_s·cos(φ_s-φ_n) = π (mod 2π)")
    for theta_s in [20, 30, 45, 60]:
        sin_theta = np.sin(np.deg2rad(theta_s))
        # For phi_s=0 (principal plane):
        # The first blind spot occurs at sinθ_s = 1/(β·a) = 1/(4π) → θ_s ≈ 4.6°
        # More precisely: for N elements, grating lobe condition:
        print(f"  θ_s={theta_s}° → β·a·sinθ_s = {beta*a_lam*np.sin(np.deg2rad(theta_s)):.2f} rad")
    print(f"  When β·a·sinθ_s ≈ π → θ_s ≈ {np.degrees(np.arcsin(1/(beta*a_lam+1e-12))):.1f}° (blind spot)")

scan_blindness(12, 2.0)

# ═══════════════════════════════════════════════════════════════════════════
# Sec 14-14/14-15: Spherical conformal array (hemispherical, N=20 elements)
# D ≈ N·η_ar·D_iso for isotropic coverage
# ═══════════════════════════════════════════════════════════════════════════
def spherical_array():
    print(f"\n--- Sec 14-14/14-15: Hemispherical array directivity ---")
    for N in [8, 12, 20, 32]:
        eta_ar = 0.8    # array efficiency (typical)
        D_iso = 1.5     # bidirectional element (sin²θ pattern)
        D = N * eta_ar * D_iso
        print(f"  N={N:2d} elements → D≈{D:.1f} ({10*np.log10(D+1e-12):.1f} dBi)")
    return

spherical_array()

print("\n✓ Chapter 14 code complete.")