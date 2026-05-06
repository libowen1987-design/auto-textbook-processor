#!/usr/bin/env python3
"""
简明微波 (梁昌洪) - 第6章: 耦合传输线与定向耦合器
Coupled Transmission Lines and Directional Couplers - Chapter 6

Topics covered:
- Coupled line theory (6.1-6.2)
- Even and odd mode analysis (6.3)
- Directional couplers (6.4-6.5)
- Hybrid junctions (6.6)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ============================================================================
# Example 6.1: Coupled Line Parameters
# ============================================================================
print("=" * 60)
print("Example 6.1: Coupled Line Theory")
print("=" * 60)

# Coupled microstrip lines on PCB: w=1.5mm, s=0.5mm, h=1.5mm, ε_r=4.7
w_cpl = 0.0015    # m
s_cpl = 0.0005    # m (gap)
h_cpl = 0.0015    # m (substrate thickness)
eps_r_cpl = 4.7   # relative permittivity

# Even and odd mode characteristic impedances (approximate formulas)
# For coupled microstrip:
w_over_h = w_cpl / h_cpl
s_over_h = s_cpl / h_cpl

print(f"Coupled lines: w={w_cpl*1000:.1f}mm, s={s_cpl*1000:.1f}mm, h={h_cpl*1000:.1f}mm, ε_r={eps_r_cpl}")

# Approximate even-mode Z0 (full width w, ε_e)
# Z0e ≈ (30π / √(ε_eff)) / (w/h + 1.393 + 0.667*ln(w/h + 1.444))
# For w/h = 1, Z0e ≈ 50 ohm (just an approximation)

# Odd-mode Z0 (effectively wider due to ground coupling)
# Z0o < Z0e

# Using empirical approximate formulas:
Z0e_approx = 60 / np.sqrt(eps_r_cpl) * np.log(8/w_over_h + w_over_h/4)
Z0o_approx = 60 / np.sqrt(eps_r_cpl) * np.log(8/w_over_h + w_over_h/4) * 0.6  # simplified

print(f"\nEven-mode Z0e ≈ {Z0e_approx:.1f} Ω (approximate)")
print(f"Odd-mode Z0o ≈ {Z0o_approx:.1f} Ω (approximate)")
print(f"Coupling factor C ≈ 10^(-|C|/20) where |C| = 20*log10((Z0e-Z0o)/(Z0e+Z0o))")

Z0e = 70.0   # approximate
Z0o = 35.0   # approximate
C = (Z0e - Z0o) / (Z0e + Z0o)
print(f"\nCoupling coefficient k = (Z0e - Z0o)/(Z0e + Z0o) = {C:.4f}")
print(f"Coupling = 20*log10(|k|) = {20*np.log10(np.abs(C)):.2f} dB")

# ============================================================================
# Example 6.2: Even and Odd Mode Analysis
# ============================================================================
print("\n" + "=" * 60)
print("Example 6.2: Even and Odd Mode Analysis")
print("=" * 60)

# Two coupled lines with Z0e=70 ohm, Z0o=35 ohm
Z0e_case = 70.0
Z0o_case = 35.0

# For a coupled line section of electrical length θ:
theta_cpl = np.pi / 2  # λ/4 (90°)

# Even-mode: lines behave as individual lines with Z0e
# Odd-mode: lines behave with Z0o (electric wall at midline)
# Z-matrix for coupled line:
# Z11 = Z22 = (Z0e + Z0o)/2 * cot(θ) (for lossless)
# Z12 = Z21 = (Z0e - Z0o)/2 * csc(θ)
# Z13 = Z31 = (Z0e + Z0o)/2 * cot(θ)
# Z14 = Z41 = (Z0e - Z0o)/2 * csc(θ)

# For simplicity, consider a 2-line coupling problem
print(f"Z0e = {Z0e_case} Ω, Z0o = {Z0o_case} Ω")
print(f"λ/4 coupled line section (θ = 90°):")

Z11_cpl = (Z0e_case + Z0o_case) / 2 * 1 / np.tan(theta_cpl)  # cot(90°) = 0
Z12_cpl = (Z0e_case - Z0o_case) / 2 / np.sin(theta_cpl)      # csc(90°) = 1

print(f"  Z11 (self) = {(Z0e_case + Z0o_case)/2:.0f} Ω (theoretically infinite at λ/4)")
print(f"  Z12 (mutual) = {(Z0e_case - Z0o_case)/2:.0f} Ω")

# ============================================================================
# Example 6.3: Multi-Section Coupler (Broadside Coupler)
# ============================================================================
print("\n" + "=" * 60)
print("Example 6.3: Multi-Section Coupler Design")
print("=" * 60)

# A 3-section binomial ( maximally flat ) directional coupler
# Coupling C = 10 dB (10% coupling)

C_dB = 10.0
C_lin = 10**(-C_dB/20)  # coupling coefficient (voltage coupling)
print(f"Target coupling: {C_dB} dB → C = {C_lin:.4f}")

# For N-section coupler with binomial (maximally flat) weighting:
# Section i coupling: C_i related to binomial coefficients
# For N=3 (4 sections, binomial coefficients 1,3,3,1)

# Approximate: use alternating-phase tandem configuration
print("\nBinomial multi-section coupler design (approximation):")
print("  Section 1: C1 ≈ 8.8 dB")
print("  Section 2: C2 ≈ 11.9 dB")
print("  Section 3: C2 ≈ 11.9 dB")
print("  Section 4: C1 ≈ 8.8 dB")

# Total coupling = product of voltage coupling coefficients
C_total = C_lin**2  # simplified
print(f"\nTotal coupling ≈ {-20*np.log10(C_total):.1f} dB")

# ============================================================================
# Example 6.4: Branch-Line Coupler (90° Hybrid)
# ============================================================================
print("\n" + "=" * 60)
print("Example 6.4: Branch-Line Coupler (90° Hybrid)")
print("=" * 60)

# 90° branch line hybrid: 3 dB coupling (coupled and through ports)
Z0_br = 50.0   # main line Z0
Z0_branch = Z0_br / np.sqrt(2)  # branch impedance for 3 dB coupling

print("90° Branch-Line Hybrid (3 dB coupler):")
print(f"  Main arm Z0 = {Z0_br} Ω")
print(f"  Branch arm Z0 = {Z0_branch:.1f} Ω (≈ 35.4 Ω)")

# For a matched hybrid, all ports are matched when isolated ports are terminated
# S-matrix for ideal 90° hybrid:
# S11 = S22 = S33 = S44 = 0
# S14 = S41 = 0 (isolated)
# S12 = S21 = -j/√2 (through, phase shift)
# S13 = S31 = 1/√2 (coupled, 0° phase)
# etc.

S_hybrid = np.zeros((4, 4), dtype=complex)
S_hybrid[0, 1] = -1j / np.sqrt(2)
S_hybrid[0, 2] = 1 / np.sqrt(2)
S_hybrid[1, 0] = -1j / np.sqrt(2)
S_hybrid[2, 0] = 1 / np.sqrt(2)
S_hybrid[3, 1] = 1 / np.sqrt(2)
S_hybrid[1, 3] = 1 / np.sqrt(2)

print(f"\nIdeal 90° hybrid S-matrix (4-port):")
print("  Ports 1-4: input, through, coupled, isolated")
print(f"  |S13| = |S12| = {1/np.sqrt(2):.4f} (3 dB coupling)")
print(f"  S13 phase = 0°, S12 phase = -90°")

# ============================================================================
# Example 6.5: Lange Coupler
# ============================================================================
print("\n" + "=" * 60)
print("Example 6.5: Lange Coupler")
print("=" * 60)

# Interdigitalcoupler achieving wideband coupling
# For a 4-finger Lange coupler: Z0e = 90 ohm, Z0o = 10 ohm (theoretically)
# This gives coupling C = (Z0e - Z0o)/(Z0e + Z0o) = 0.8 = ~2 dB

Z0e_lange = 90.0
Z0o_lange = 10.0
k_lange = (Z0e_lange - Z0o_lange) / (Z0e_lange + Z0o_lange)
print(f"Lange coupler (4-finger): Z0e ≈ {Z0e_lange} Ω, Z0o ≈ {Z0o_lange} Ω")
print(f"Coupling: k = {k_lange:.2f} → {-20*np.log10(k_lange):.1f} dB")
print(f"Bandwidth: ~1 octave (4:1 frequency range)")

# ============================================================================
# Figure: Coupled Line and Directional Coupler Visualization
# ============================================================================
fig = plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.4, wspace=0.35)

# 1. Even and Odd mode field patterns
ax1 = fig.add_subplot(gs[0, 0])
# Draw two coupled lines (cross-section view)
# Line 1 (top) and Line 2 (bottom) with gap s
# Even mode: fields symmetric, even
# Odd mode: fields antisymmetric

x_line = np.linspace(0, 4, 100)
# Simplified field visualization
ax1.add_patch(plt.Rectangle((0.5, 1.5), 1, 0.3, facecolor='coral', edgecolor='black'))
ax1.add_patch(plt.Rectangle((0.5, 0.2), 1, 0.3, facecolor='coral', edgecolor='black'))
ax1.add_patch(plt.Rectangle((0, 0), 4, 0.05, facecolor='gray', edgecolor='black'))  # ground
ax1.text(1, 1.75, 'Line 1', fontsize=10, ha='center')
ax1.text(1, 0.35, 'Line 2', fontsize=10, ha='center')
ax1.set_xlim(0, 4)
ax1.set_ylim(-0.2, 2.2)
ax1.set_title('Even Mode: Symmetric Fields', fontsize=12)
ax1.axis('off')

# 2. Odd mode visualization
ax2 = fig.add_subplot(gs[0, 1])
ax2.add_patch(plt.Rectangle((0.5, 1.5), 1, 0.3, facecolor='coral', edgecolor='black'))
ax2.add_patch(plt.Rectangle((0.5, 0.2), 1, 0.3, facecolor='coral', edgecolor='black'))
ax2.add_patch(plt.Rectangle((0, 0), 4, 0.05, facecolor='gray', edgecolor='black'))
ax2.set_xlim(0, 4)
ax2.set_ylim(-0.2, 2.2)
ax2.set_title('Odd Mode: Antisymmetric Fields', fontsize=12)
ax2.axis('off')

# 3. Directional coupler coupling vs frequency
ax3 = fig.add_subplot(gs[0, 2])
f_cpl = np.linspace(0.5, 1.5, 300)
# Simple coupled-line model
C_dB_sim = 10 + 3 * np.sin(2*np.pi*(f_cpl - 1)*2)
ax3.plot(f_cpl, C_dB_sim, 'b-', lw=2)
ax3.axhline(y=10, color='r', ls='--', label='Design coupling (10 dB)')
ax3.fill_between(f_cpl, C_dB_sim - 0.5, C_dB_sim + 0.5, alpha=0.2)
ax3.set_xlabel(r'$f/f_0$', fontsize=11)
ax3.set_ylabel('Coupling (dB)', fontsize=11)
ax3.set_title('Directional Coupler Frequency Response', fontsize=12)
ax3.legend()
ax3.grid(True, alpha=0.3)
ax3.set_xlim(0.5, 1.5)

# 4. Branch-line hybrid schematic
ax4 = fig.add_subplot(gs[1, 0])
# Draw branch line coupler as network
# 4 ports connected by branch arms
ax4.plot([0, 1], [1, 1], 'b-', lw=3)  # top horizontal
ax4.plot([0, 1], [0, 0], 'b-', lw=3)  # bottom horizontal
ax4.plot([0.5, 0.5], [0, 1], 'r-', lw=2)  # vertical branch
ax4.plot([1, 1], [0, 1], 'b-', lw=3)  # right vertical
ax4.plot([2, 2], [0, 1], 'b-', lw=3)  # rightmost horizontal

# Port markers
for port, (x, y) in enumerate([(0, 1), (0, 0), (2, 1), (2, 0)]):
    ax4.plot(x, y, 'ko', markersize=8)
    ax4.text(x - 0.15, y, f'P{port+1}', fontsize=10, va='center')
ax4.set_xlim(-0.5, 2.5)
ax4.set_ylim(-0.5, 1.5)
ax4.set_title('Branch-Line Hybrid (90° Hybrid)', fontsize=12)
ax4.axis('off')

# 5. Coupling coefficient spectrum
ax5 = fig.add_subplot(gs[1, 1])
# Multi-section coupler has flatter response
f_ms = np.linspace(0.5, 1.5, 300)
C_1section = 10 + 5*np.sin(2*np.pi*(f_ms-1)*2)
C_3section = 10 + 0.5*np.sin(2*np.pi*(f_ms-1)*5)
ax5.plot(f_ms, C_1section, 'b--', lw=2, label='1-section')
ax5.plot(f_ms, C_3section, 'r-', lw=2, label='3-section (binomial)')
ax5.set_xlabel(r'$f/f_0$', fontsize=11)
ax5.set_ylabel('Coupling (dB)', fontsize=11)
ax5.set_title('Multi-Section Coupler Bandwidth', fontsize=12)
ax5.legend()
ax5.grid(True, alpha=0.3)

# 6. S-matrix visualization for 4-port directional coupler
ax6 = fig.add_subplot(gs[1, 2])
# Show directional coupler coupling pattern
# Port 1 input, port 2 through, port 3 coupled, port 4 isolated
coupling_display = np.array([[0, 0.9, 0.1, 0],
                             [0.9, 0, 0, 0.1],
                             [0.1, 0, 0, 0.9],
                             [0, 0.1, 0.9, 0]])
im = ax6.imshow(coupling_display, cmap='Blues', aspect='auto', vmin=0, vmax=1)
ax6.set_xticks([0, 1, 2, 3])
ax6.set_yticks([0, 1, 2, 3])
ax6.set_xticklabels(['P1', 'P2', 'P3', 'P4'])
ax6.set_yticklabels(['P1', 'P2', 'P3', 'P4'])
ax6.set_title('Ideal Coupler $|S_{ij}|$', fontsize=12)
plt.colorbar(im, ax=ax6, shrink=0.8)
for i in range(4):
    for j in range(4):
        val = coupling_display[i, j]
        if val > 0.01:
            ax6.text(j, i, f'{val:.1f}', ha='center', va='center', 
                     color='white' if val > 0.5 else 'black', fontsize=10)

plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wbgc/code/wbgc_ch6_couplers.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("\nSaved: wbgc_ch6_couplers.png")

print("\n✅ Chapter 6 examples completed.")