#!/usr/bin/env python3
"""
简明微波 (梁昌洪) - 第13章: 铁氧体与环形器
Ferrite and Non-Reciprocal Components - Chapter 13

Topics covered:
- Ferrite materials and magnetization (13.1)
- Gyromagnetic effect and tensor permeability (13.2)
- Non-reciprocal phase shift (NRPS) (13.3)
- Circulators (13.4)
- Isolators (13.5)
- Faraday rotator (13.6)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ============================================================================
# Example 13.1: Ferrite Material Properties
# ============================================================================
print("=" * 60)
print("Example 13.1: Ferrite Material Properties")
print("=" * 60)

# YIG (Yttrium Iron Garnet) - commonly used ferrite
# Saturation magnetization 4πMs = 1780 Gauss
# Dielectric constant ε_r ≈ 14-16
# Loss tangent tan δ ≈ 0.0002 at microwave frequencies

mu_0 = 4 * np.pi * 1e-7  # H/m
four_pi_Ms = 1780  # Gauss
Ms = four_pi_Ms / (4 * np.pi * 1e3)  # A/m (convert)
# Ms = four_pi_Ms / (4 * np.pi * 1e3)  # A/m (convert)
gamma = 2.8e6  # Hz/Oe (gyromagnetic ratio)
H_applied = 2000  # Oe (applied magnetic field)

print("YIG Ferrite properties:")
print(f"  Saturation magnetization 4πMs = {four_pi_Ms} G")
print(f"  Permeability µ = µ0*(µ' - jµ'')")
print(f"  Gyromagnetic ratio γ = {gamma/1e6:.1f} MHz/Oe")
print(f"  Applied field H = {H_applied} Oe")

# ============================================================================
# Example 13.2: Gyromagnetic Tensor Permeability
# ============================================================================
print("\n" + "=" * 60)
print("Example 13.2: Gyromagnetic Tensor Permeability")
print("=" * 60)

# Polder tensor for ferrite under bias field H0:
# [µ] = [ µ   jκ   0  ]
#       [ -jκ  µ   0  ]
#       [ 0    0   µ_z ]

# Components:
# µ = 1 + (γ * 4πMs * H0) / (H0² - (ω/γ)² + j*α*ω*H0/γ)  
# Simplified form:
omega = 2 * np.pi * 10e9  # 10 GHz
gamma_val = 2.8e6  # Hz/Oe
H_0 = 3000  # Oe (bias field)

# Resonance frequency: ω_r = γ * H_0
omega_r = gamma_val * H_0
print(f"Gyromagnetic resonance at ω_r = γ*H = {omega_r/1e9:.2f} GHz")
print(f"  (This corresponds to H = {omega/(gamma_val*2*np.pi):.0f} Oe at 10 GHz)")

# Precession equation: ω_0 = γ * H_0
# Tensor permeability components:
# µ = 1 + j*ω*γ*Ms/(ω_r² - ω² + j*ω*Δω)

# ============================================================================
# Example 13.3: Non-Reciprocal Phase Shift (NRPS)
# ============================================================================
print("\n" + "=" * 60)
print("Example 13.3: Non-Reciprocal Phase Shift (NRPS)")
print("=" * 60)

# For a ferrite slab in waveguide:
# Forward wave: phase shift φ_fwd = β * L
# Reverse wave: phase shift φ_rev = β * L + Δφ
# NRPS = Δφ = φ_rev - φ_fwd

# Simplified calculation for partially magnetized ferrite
length_f = 0.05  # m (5 cm ferrite section)
beta_0 = 200  # rad/m (waveguide phase constant)

# NRPS depends on magnetization direction
# For typical waveguide ferrite phase shifter:
# NRPS ≈ (0.5 to 2) * γ * 4πMs * L for full saturation

NRPS_deg = 45  # degrees (typical for 5cm ferrite at X-band)
print(f"Ferrite phase shifter: L = {length_f*100:.0f} cm")
print(f"  NRPS = {NRPS_deg}° at X-band")
print(f"  Forward: 0° phase shift reference")
print(f"  Reverse: +{NRPS_deg}° additional phase shift")

# Application: switchable phase shifter (0° vs 45°)
# 1-bit digital phase shifter: 0 or 45°

# ============================================================================
# Example 13.4: Junction Circulator
# ============================================================================
print("\n" + "=" * 60)
print("Example 13.4: Junction Circulator")
print("=" * 60)

# Three-port circulator: port 1 → port 2 → port 3 → port 1
# Ideal S-matrix (non-reciprocal):
S_circ = np.zeros((3, 3), dtype=complex)
S_circ[0, 1] = 1  # port 1 → port 2
S_circ[1, 2] = 1  # port 2 → port 3
S_circ[2, 0] = 1  # port 3 → port 1
# All other: 0 (isolated)

print("Three-port circulator S-matrix:")
print(f"  S = [[0, 1, 0],")
print(f"       [0, 0, 1],")
print(f"       [1, 0, 0]]")
print(f"\nNon-reciprocal: power flows 1→2→3→1 (cyclic)")
print(f"  Isolation: |S_ij| = 0 for i≠j+1 (mod 3)")
print(f"  Insertion loss: ideally 0 dB (perfect circulation)")

# Practical circulator: isolation ~ 20 dB, IL ~ 0.5 dB
print(f"\nPractical junction circulator:")
print(f"  Isolation: ~20-30 dB")
print(f"  Insertion loss: ~0.5-1 dB")
print(f"  VSWR: < 1.2:1")

# ============================================================================
# Example 13.5: Ferrite Isolator
# ============================================================================
print("\n" + "=" * 60)
print("Example 13.5: Ferrite Isolator")
print("=" * 60)

# Resonance isolator: uses gyromagnetic resonance absorption
# Forward: low loss (below resonance)
# Reverse: high loss (at resonance, power absorbed)

print("Resonance isolator:")
print(f"  Forward (below resonance): < 1 dB insertion loss")
print(f"  Reverse (at resonance): > 20 dB isolation")
print(f"  Operating band: 8-12 GHz (X-band)")
print(f"  Magnetic bias: H_0 ≈ 3000 Oe (for resonance at f)")

# Faraday rotation isolator: uses Faraday effect
# Rotation of polarization plane in ferrite under bias
print(f"\nFaraday rotation isolator:")
print(f"  45° rotation in ferrite rod")
print(f"  Input/output polarizers at 45° to each other")
print(f"  Forward: passes through, rotated to align")
print(f"  Reverse: blocked by polarizer")

# ============================================================================
# Example 13.6: Edge-guided Isolator
# ============================================================================
print("\n" + "=" * 60)
print("Example 13.6: Edge-Guided Mode Isolator")
print("=" * 60)

# Edge-guided mode isolator: uses magnetic field concentration at ferrite edge
# Non-reciprocal edge mode: fields concentrated at one edge

print("Edge-guided mode (EGM) isolator:")
print(f"  Ferrite loaded waveguide with magnetized ferrite")
print(f"  Forward: edge-guided mode at one edge (low loss)")
print(f"  Reverse: mode displaced to lossy region (high attenuation)")
print(f"  Advantage: wide bandwidth (~20%)")
print(f"  Application: high-power TWT amplifier protection")

# ============================================================================
# Figure: Ferrite and Non-Reciprocal Components
# ============================================================================
fig = plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.4, wspace=0.35)

# 1. Ferrite magnetization curve
ax1 = fig.add_subplot(gs[0, 0])
H_axis = np.linspace(0, 5000, 300)
# Simplified B-H curve for ferrite
M_sat = 1780  # G
M_axis = M_sat * (1 - np.exp(-H_axis/500))
ax1.plot(H_axis, M_axis, 'b-', lw=2)
ax1.axhline(y=M_sat, color='r', ls='--', alpha=0.7, label=r'$M_s$ (saturation)')
ax1.set_xlabel(r'$H$ (Oe)', fontsize=11)
ax1.set_ylabel(r'$M$ (G)', fontsize=11)
ax1.set_title('Ferrite Magnetization Curve', fontsize=12)
ax1.legend()
ax1.grid(True, alpha=0.3)

# 2. Gyromagnetic tensor visualization
ax2 = fig.add_subplot(gs[0, 1])
# Show tensor structure
ax2.text(0.5, 0.8, 'μ = μ\' - jμ\'\'  (diagonal)', fontsize=12, ha='center', va='center', transform=ax2.transAxes)
ax2.text(0.5, 0.5, 'κ = κ\' - jκ\'\'  (off-diagonal)', fontsize=12, ha='center', va='center', transform=ax2.transAxes)
ax2.text(0.5, 0.2, r'$\mu, \kappa$ are complex tensors', fontsize=12, ha='center', va='center')
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.axis('off')
ax2.set_title('Polder Permeability Tensor', fontsize=12)

# 3. NRPS vs applied field
ax3 = fig.add_subplot(gs[0, 2])
H_NRPS = np.linspace(1000, 5000, 200)
NRPS_sim = 30 * (1 - np.exp(-(H_NRPS - 1000)/3000))
ax3.plot(H_NRPS/1000, NRPS_sim, 'b-', lw=2)
ax3.set_xlabel(r'$H_0$ (kOe)', fontsize=11)
ax3.set_ylabel('NRPS (degrees)', fontsize=11)
ax3.set_title('NRPS vs Magnetic Field', fontsize=12)
ax3.grid(True, alpha=0.3)

# 4. Circulator schematic
ax4 = fig.add_subplot(gs[1, 0])
# Draw 3-port circulator
angles = [0, 120, 240]
for i, angle in enumerate(angles):
    theta = np.radians(angle - 90)
    x = 0.8 * np.cos(theta)
    y = 0.8 * np.sin(theta)
    ax4.plot(x, y, 'ko', markersize=10)
    label_pos = 1.1 * np.array([x, y])
    ax4.text(label_pos[0], label_pos[1], f'Port {i+1}', fontsize=10, ha='center')
    # Draw arrows
    next_angle = np.radians(angles[(i+1)%3] - 90)
    ax4.annotate('', xy=(0.5*np.cos(next_angle), 0.5*np.sin(next_angle)),
                 xytext=(0.8*np.cos(theta), 0.8*np.sin(theta)),
                 arrowprops=dict(arrowstyle='->', color='blue', lw=2))

ax4.set_xlim(-1.5, 1.5)
ax4.set_ylim(-1.5, 1.5)
ax4.set_title('3-Port Circulator', fontsize=12)
ax4.axis('off')
ax4.text(0, 0, 'Ferrite\nMagnet', fontsize=9, ha='center', va='center')

# 5. Isolator frequency response
ax5 = fig.add_subplot(gs[1, 1])
f_iso = np.linspace(8, 12, 300)
# Resonance isolator response
IL_fwd = 0.5 + 0.2 * np.sin(2*np.pi*(f_iso - 10))  # low in band
IL_rev = 30 - (f_iso - 10)**2 * 5  # high in band
ax5.plot(f_iso, IL_fwd, 'b-', lw=2, label='Forward (IL)')
ax5.plot(f_iso, IL_rev, 'r--', lw=2, label='Reverse (isolation)')
ax5.set_xlabel('f (GHz)', fontsize=11)
ax5.set_ylabel('Loss (dB)', fontsize=11)
ax5.set_title('Isolator Frequency Response', fontsize=12)
ax5.legend()
ax5.grid(True, alpha=0.3)
ax5.set_xlim(8, 12)
ax5.set_ylim(0, 35)

# 6. Faraday rotation isolator schematic
ax6 = fig.add_subplot(gs[1, 2])
# Draw ferrite rod with rotation
ax6.add_patch(plt.Rectangle((0.2, 0.3), 1.5, 0.4, facecolor='coral', edgecolor='black', lw=2))
# Input polarizer
ax6.plot([0, 0.2], [0.3, 0.3], 'k-', lw=3)
ax6.plot([0, 0.2], [0.7, 0.7], 'k-', lw=3)
ax6.text(0, 0.5, '0°', fontsize=10, ha='right', va='center')
# Output polarizer
ax6.plot([1.7, 2], [0.3, 0.3], 'k-', lw=3)
ax6.plot([1.7, 2], [0.7, 0.7], 'k-', lw=3)
ax6.text(2.1, 0.5, '45°', fontsize=10, ha='left', va='center')
ax6.set_xlim(-0.3, 2.3)
ax6.set_ylim(0.1, 0.9)
ax6.set_title('Faraday Rotation Isolator', fontsize=12)
ax6.axis('off')
ax6.text(1.0, 0.15, 'Ferrite Rod', fontsize=9, ha='center')

plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wbgc/code/wbgc_ch13_ferrite.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("\nSaved: wbgc_ch13_ferrite.png")

print("\n✅ Chapter 13 examples completed.")
print("\n" + "=" * 60)
print("ALL CHAPTERS COMPLETED")
print("=" * 60)
print(f"\nGenerated files in /home/ubuntu/.openclaw/workspace/textbooks/wbgc/code/")
print("  wbgc_ch2_transmissionline.py  - Ch2: Transmission Line Theory")
print("  wbgc_ch3_waveguide.py         - Ch3: Waveguide & Resonator")
print("  wbgc_ch4_smith_matching.py    - Ch4: Smith Chart & Matching")
print("  wbgc_ch5_sparameters.py       - Ch5: S-Parameters")
print("  wbgc_ch6_couplers.py          - Ch6: Coupled Lines & Couplers")
print("  wbgc_ch7_power_dividers.py    - Ch7: Power Dividers")
print("  wbgc_ch8_filters.py           - Ch8: Filters")
print("  wbgc_ch9_noise_nonlinear.py   - Ch9: Noise & Nonlinearity")
print("  wbgc_ch10_amplifiers.py       - Ch10: Microwave Amplifiers")
print("  wbgc_ch11_oscillators_mixers.py - Ch11: Oscillators & Mixers")
print("  wbgc_ch12_systems.py          - Ch12: Systems & Measurements")
print("  wbgc_ch13_ferrite.py          - Ch13: Ferrite Components")
print("\nGenerated figures in PNG format")
print("Total: 12 Python files + 12 figures")