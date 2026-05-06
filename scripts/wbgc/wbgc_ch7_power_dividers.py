#!/usr/bin/env python3
"""
简明微波 (梁昌洪) - 第7章: 功率分配器与微波管
Power Dividers and Microwave Tubes - Chapter 7

Topics covered:
- N-way power dividers (7.1)
- Resonant iris coupled cavity (7.2)
- E-plane and H-plane tees (7.3)
- Magic-T (7.4)
- Ferrite components (7.5-7.6)
- Waveguide bends and twists (7.7)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ============================================================================
# Example 7.1: N-Way Power Divider (Wilkinson Divider)
# ============================================================================
print("=" * 60)
print("Example 7.1: N-Way Power Divider")
print("=" * 60)

# N=2 Wilkinson divider (simple case)
N = 2
Z_0_wil = 50.0  # system impedance

# For equal-split 2-way Wilkinson:
# Z02 = Z03 = √2 * Z0 = 70.7 ohm (for equal split)
# The isolation resistor R = Z0 * √2 = 50 * 1.414 = 70.7 ohm

Z_0_branch_wil = Z_0_wil * np.sqrt(N)  # = 70.7 ohm
R_isolation = Z_0_wil * np.sqrt(N)      # = 70.7 ohm

print("2-way equal-split Wilkinson divider:")
print(f"  Z01 = Z02 = {Z_0_wil} Ω (input/output lines)")
print(f"  Z_branch = Z0·√N = {Z_0_branch_wil:.1f} Ω")
print(f"  Isolation resistor R = {R_isolation:.1f} Ω")

# For N-way (general case): Z_i = Z_0 * √N
print(f"\nGeneral N-way Wilkinson: Z_i = Z_0 × √N")

# 4-way Wilkinson: each branch Z = 50 * √4 = 100 ohm
N_4 = 4
Z_0_4way = Z_0_wil * np.sqrt(N_4)
print(f"\n4-way Wilkinson divider:")
print(f"  Each branch Z = {Z_0_4way:.0f} Ω")

# ============================================================================
# Example 7.2: Resonant Iris Coupled Cavity
# ============================================================================
print("\n" + "=" * 60)
print("Example 7.2: Resonant Iris Coupled Cavity Filter")
print("=" * 60)

# Coupled cavity filter with iris coupling
# For a 2-pole filter at f0=10 GHz, bandwidth=100 MHz

f_0_filt = 10e9      # Hz
BW_filt = 100e6      # Hz (100 MHz)
Q_u = 5000           # unloaded Q (copper)
Q_ext = 2000          # external Q

# Coupling coefficients
k_12 = BW_filt / f_0_filt  # coupling between resonators
print(f"2-pole filter at f0={f_0_filt/1e9:.0f} GHz, BW={BW_filt/1e6:.0f} MHz:")
print(f"  Coupling k12 = {k_12:.4f}")
print(f"  Unloaded Q = {Q_u}")
print(f"  External Q = {Q_ext}")

# Return loss at center frequency (for Chebyshev)
# RL = -10*log10(10^( -RL_dB/10) - 1) + more
# For 0.1 dB ripple, in-band RL ≈ 20 dB

# ============================================================================
# Example 7.3: E-plane and H-plane Tees
# ============================================================================
print("\n" + "=" * 60)
print("Example 7.3: E-plane and H-plane T-junctions")
print("=" * 60)

# E-plane tee (H-plane tee in rectangular waveguide terminology)
# For H-plane tee: the E-field is in the plane of the junction

print("H-plane waveguide tee:")
print("  All three ports are on the broad wall of the waveguide")
print("  E-field is perpendicular to the junction plane")
print("  Ports 2 and 3 are symmetrically placed")
print("")
print("E-plane waveguide tee:")
print("  All three ports are on the narrow wall of the waveguide")
print("  H-field is perpendicular to the junction plane")

# S-matrix for E-plane tee (ideal, lossless)
# S11 = 0 (can be matched with iris)
# S22 = S33 = 0
# S12 = S13 = 1/√2
# S23 = -1/√2 (180° phase difference due to E-field direction)

S_tee = np.zeros((3, 3), dtype=complex)
S_tee[0, 1] = 1/np.sqrt(2)
S_tee[0, 2] = 1/np.sqrt(2)
S_tee[1, 0] = 1/np.sqrt(2)
S_tee[2, 0] = 1/np.sqrt(2)
S_tee[1, 2] = -1/np.sqrt(2)
S_tee[2, 1] = -1/np.sqrt(2)

print(f"\nH-plane tee S-matrix (port 1: input, ports 2,3: output):")
print(f"  S12 = S13 = {1/np.sqrt(2):.4f} (in-phase)")
print(f"  S23 = {-1/np.sqrt(2):.4f} (180° out-of-phase)")

# ============================================================================
# Example 7.4: Magic-T (E-H Plane Tee)
# ============================================================================
print("\n" + "=" * 60)
print("Example 7.4: Magic-T (E-H Plane Tee)")
print("=" * 60)

# Magic-T combines E-plane and H-plane tees
# Port 1: H-arm (sum port)
# Port 2: E-arm (difference port)
# Port 3: coupled port
# Port 4: through port

print("Magic-T (E-H Tee):")
print("  Port 1 (H-arm): sum port, even mode excitation")
print("  Port 2 (E-arm): difference port, odd mode excitation")
print("  Ports 3 and 4: when Port 1 excited, power splits equally to 3 & 4 (in phase)")
print("                 when Port 2 excited, power splits equally to 3 & 4 (180° out of phase)")

# S-matrix for ideal magic-T (4-port)
S_magic = np.zeros((4, 4), dtype=complex)
# Port 1 (H-arm, sum port)
S_magic[0, 2] = 1/np.sqrt(2)  # to coupled port
S_magic[0, 3] = 1/np.sqrt(2)  # to through port
# Port 2 (E-arm, difference port)
S_magic[1, 2] = 1/np.sqrt(2)   # to coupled port
S_magic[1, 3] = -1/np.sqrt(2)  # to through port (180°)
# Isolation between arms
S_magic[0, 1] = 0  # isolated
S_magic[1, 0] = 0

print(f"\nIdeal magic-T S-matrix:")
print(f"  S13 = S14 = S23 = 1/√2 = {1/np.sqrt(2):.4f} (amplitude)")
print(f"  S24 = -S23 = {-1/np.sqrt(2):.4f} (phase difference)")
print(f"  S12 = S21 = 0 (H and E arms isolated)")

# Application: phase comparator
print(f"\nApplication: phase comparator (difference port output = V3 - V4)")

# ============================================================================
# Example 7.5: Ferrite Isolator
# ============================================================================
print("\n" + "=" * 60)
print("Example 7.5: Ferrite Isolator")
print("=" * 60)

# Ferrite isolator: uses Faraday rotation in biased ferrite
# Forward: low loss, Reverse: high loss (circulator with load)

# Gyromagnetic ratio for ferrite: γ = 2.8 MHz/Oe = 35 GHz/T
gamma_ferrite = 2.8e6  # Hz/Oe
mu_0_ferrite = 4*np.pi*1e-7

# Magnetization 4πM for typical ferrite: 500-5000 Gauss
four_pi_M = 2000  # Gauss (typical)
Ms_four_pi = four_pi_M  # for naming consistency
Ms = four_pi_M / (4 * np.pi * 1e3)  # A/m (convert)
# Saturation magnetization 4πMs = 2000 G
Ms = 2000 / (4*np.pi)  # in A/m (equivalent)

# Non-reciprocal phase shift (NRPS)
# For length L in biased ferrite:
L_ferrite = 0.01  # m (1 cm)
# Phase shift difference between forward and reverse
delta_beta_NRPS = 0.5 * gamma_ferrite * four_pi_M * 1e-3 * L_ferrite  # simplified
print(f"Ferrite isolator parameters:")
print(f"  Saturation magnetization 4πMs = {four_pi_M} G")
print(f"  Length L = {L_ferrite*100:.0f} cm")
print(f"  Forward: phase shift φ")
print(f"  Reverse: phase shift φ + Δβ·L")
print(f"  Isolation ≈ 20-30 dB, Insertion loss ≈ 0.5-1 dB")

# ============================================================================
# Example 7.6: Waveguide Bend and Twist
# ============================================================================
print("\n" + "=" * 60)
print("Example 7.6: Waveguide Bends")
print("=" * 60)

# E-plane bend (90°): sharpest radius for minimum VSWR
# Recommended bend radius R ≥ 1.5λ for E-plane
# Recommended bend radius R ≥ λ for H-plane

lambda_wg = 3.0  # cm (at 10 GHz, WR-90)
print(f"WR-90 waveguide at 10 GHz: λ = {lambda_wg:.1f} cm")
print(f"\nE-plane 90° bend: R ≥ 1.5λ = {1.5*lambda_wg:.1f} cm")
print(f"H-plane 90° bend: R ≥ λ = {lambda_wg:.1f} cm")
print(f"Mitered bend: offset = 0.5a for reduced VSWR")

# For mitered bend: step height = 0.5 * a
a_WG = 9.0  # cm (WR-90 broad dimension)
print(f"\nMitered 90° bend: miter depth ≈ {a_WG/2:.1f} cm")

# ============================================================================
# Figure: Power Dividers and Junction Devices
# ============================================================================
fig = plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.4, wspace=0.35)

# 1. N-way power divider structure
ax1 = fig.add_subplot(gs[0, 0])
# Draw 4-way power divider
# Input at center, outputs at 4 corners
ax1.add_patch(plt.Circle((0, 0), 0.2, facecolor='lightblue', edgecolor='black'))
for i in range(4):
    angle = np.radians(45 + i*90)
    x_out = 1.5 * np.cos(angle)
    y_out = 1.5 * np.sin(angle)
    ax1.plot([0, x_out], [0, y_out], 'b-', lw=3)
    ax1.add_patch(plt.Circle((x_out, y_out), 0.15, facecolor='coral', edgecolor='black'))
    ax1.text(x_out*1.15, y_out*1.15, f'P{i+1}', fontsize=10, va='center')
ax1.text(0, 0, 'N', fontsize=10, fontweight='bold')
ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 2)
ax1.set_title('N-Way Power Divider', fontsize=12)
ax1.axis('off')

# 2. Wilkinson divider with isolation resistor
ax2 = fig.add_subplot(gs[0, 1])
# Input T-junction splitting to two arms
ax2.plot([0, 0.5], [0, 0], 'b-', lw=3)
ax2.plot([0.5, 1], [0, 0.5], 'b-', lw=3)  # upper arm
ax2.plot([0.5, 1], [0, -0.5], 'b-', lw=3)  # lower arm
ax2.plot([1, 1.5], [0.5, 0.5], 'r-', lw=2)  # upper output
ax2.plot([1, 1.5], [-0.5, -0.5], 'r-', lw=2)  # lower output
# Isolation resistor between the two arms
ax2.plot([1, 1], [-0.5, 0.5], 'g-', lw=4)
ax2.text(1.1, 0, 'R', fontsize=12, va='center')
ax2.text(-0.3, 0, 'In', fontsize=10)
ax2.text(1.7, 0.5, 'Out1', fontsize=10)
ax2.text(1.7, -0.5, 'Out2', fontsize=10)
ax2.set_xlim(-0.5, 2)
ax2.set_ylim(-1, 1)
ax2.set_title('Wilkinson Divider (2-way)', fontsize=12)
ax2.axis('off')

# 3. E-plane/H-plane tee S-matrix heatmap
ax3 = fig.add_subplot(gs[0, 2])
S_display_3port = np.array([[0, 0.707, 0.707],
                             [0.707, 0, -0.707],
                             [0.707, -0.707, 0]])
im = ax3.imshow(np.abs(S_display_3port), cmap='Blues', aspect='auto', vmin=0, vmax=1)
ax3.set_xticks([0, 1, 2])
ax3.set_yticks([0, 1, 2])
ax3.set_xticklabels(['Port1', 'Port2', 'Port3'])
ax3.set_yticklabels(['Port1', 'Port2', 'Port3'])
ax3.set_title('H-plane Tee $|S_{ij}|$', fontsize=12)
plt.colorbar(im, ax=ax3, shrink=0.8)
for i in range(3):
    for j in range(3):
        val = S_display_3port[i, j]
        if abs(val) > 0.01:
            ax3.text(j, i, f'{val:.2f}', ha='center', va='center',
                     color='white' if abs(val) > 0.5 else 'black', fontsize=10)

# 4. Magic-T schematic
ax4 = fig.add_subplot(gs[1, 0])
# Draw magic-T as two tees combined
# E-arm vertical (port 2), H-arm horizontal (port 1)
# Through port (4) and coupled port (3) on the right
ax4.plot([0, 1], [0, 0], 'b-', lw=3)   # H-arm (port 1 to right)
ax4.plot([0.5, 0.5], [0, 1], 'r-', lw=3)  # E-arm (port 2 up)
ax4.plot([1, 1.5], [0.5, 0.5], 'b-', lw=3)  # to port 4
ax4.plot([1, 1.5], [-0.5, -0.5], 'b-', lw=3)  # to port 3

ax4.plot(0, 0, 'ko', markersize=8)
ax4.plot(0.5, 1, 'ko', markersize=8)
ax4.plot(1, 0.5, 'ko', markersize=8)
ax4.plot(1, -0.5, 'ko', markersize=8)
ax4.text(0, 0.2, 'P1\n(H)', fontsize=9, ha='center')
ax4.text(0.5, 1.2, 'P2\n(E)', fontsize=9, ha='center')
ax4.text(1.2, 0.5, 'P4', fontsize=9, ha='center')
ax4.text(1.2, -0.5, 'P3', fontsize=9, ha='center')
ax4.set_xlim(-0.5, 2)
ax4.set_ylim(-1, 1.5)
ax4.set_title('Magic-T (E-H Tee)', fontsize=12)
ax4.axis('off')

# 5. Ferrite isolator schematic
ax5 = fig.add_subplot(gs[1, 1])
ax5.add_patch(plt.Rectangle((0, 0.3), 2, 0.4, facecolor='lightblue', edgecolor='black', lw=2))
ax5.annotate('', xy=(0.5, 0.3), xytext=(-0.3, 0.3),
             arrowprops=dict(arrowstyle='->', color='green', lw=2))
ax5.annotate('', xy=(-0.3, 0.5), xytext=(0.5, 0.5),
             arrowprops=dict(arrowstyle='->', color='red', lw=2))
ax5.text(-0.3, 0.6, '→ Forward (low loss)', fontsize=9, color='green')
ax5.text(0.6, 0.6, '← Reverse (high loss)', fontsize=9, color='red')
ax5.text(1, 0, 'Ferrite\n(dielectric)', fontsize=9, ha='center', va='center')
ax5.set_xlim(-1, 3)
ax5.set_ylim(-0.5, 1.5)
ax5.set_title('Ferrite Isolator', fontsize=12)
ax5.axis('off')

# 6. Waveguide bend types
ax6 = fig.add_subplot(gs[1, 2])
# E-plane bend (mitered)
ax6.add_patch(plt.Rectangle((0, 0), 0.5, 0.3, facecolor='lightgray', edgecolor='black'))
ax6.add_patch(plt.Rectangle((0.5, 0), 0.3, 0.3, facecolor='lightgray', edgecolor='black', angle=45))
ax6.set_xlim(0, 1)
ax6.set_ylim(-0.3, 0.8)
ax6.set_title('Mitered E-plane Bend', fontsize=12)
ax6.axis('off')

plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wbgc/code/wbgc_ch7_power_dividers.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("\nSaved: wbgc_ch7_power_dividers.png")

print("\n✅ Chapter 7 examples completed.")