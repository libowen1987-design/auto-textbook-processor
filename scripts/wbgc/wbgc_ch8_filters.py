#!/usr/bin/env python3
"""
简明微波 (梁昌洪) - 第8章: 微波滤波器
Microwave Filters - Chapter 8

Topics covered:
- Filter fundamentals and prototypes (8.1)
- Insertion loss method (8.2)
- Stepped-impedance low-pass filters (8.3)
- Coupled-line filters (8.4)
- Bandpass filter design (8.5-8.8)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ============================================================================
# Example 8.1: Low-Pass Filter Prototype (Butterworth)
# ============================================================================
print("=" * 60)
print("Example 8.1: Low-Pass Filter Prototype (Butterworth)")
print("=" * 60)

# 5th order Butterworth LPF (maximally flat passband)
# Element values for n=5 Butterworth:
g_butter = [1.0000, 1.6180, 1.6180, 1.6180, 1.0000, 1.0000]
print("5th order Butterworth LPF prototype:")
for i, g in enumerate(g_butter):
    if i == 0:
        print(f"  g{i+1} = {g:.4f} (series L)")
    elif i == len(g_butter) - 1:
        print(f"  g{i+1} = {g:.4f} (load)")
    else:
        print(f"  g{i+1} = {g:.4f}")

# For 50 ohm system, L1 = g1 * Z0 / (2π f_c) but we work in normalized freq

# ============================================================================
# Example 8.2: Chebyshev Low-Pass Filter
# ============================================================================
print("\n" + "=" * 60)
print("Example 8.2: Chebyshev Low-Pass Filter")
print("=" * 60)

# 5th order Chebyshev, 0.5 dB ripple
g_cheb = [3.3487, 0.9532, 5.8095, 3.3487, 0.9532, 1.0000]
print("5th order Chebyshev LPF (0.5 dB ripple) prototype:")
for i, g in enumerate(g_cheb):
    print(f"  g{i+1} = {g:.4f}")

# Compare passband ripple
print("\nButterworth at ω=1: |S21|² = 0.5 (0 dB)")
print("Chebyshev at ω=1: |S21|² = 10^(-0.5/10) = 0.891 (-0.5 dB ripple)")

# ============================================================================
# Example 8.3: Stepped-Impedance (Distributed) LPF
# ============================================================================
print("\n" + "=" * 60)
print("Example 8.3: Stepped-Impedance Low-Pass Filter")
print("=" * 60)

# Convert LPF prototype to stepped-impedance (high-low Z lines)
# Series L → high-Z line (electrical length θ at ω=1: θ_L = (g_i * Z0) / (Z_high * some_factor))
# Shunt C → low-Z line

Z_0_filt = 50.0   # ohm
Z_h = 100.0       # high impedance line (ohm)
Z_l = 20.0        # low impedance line (ohm)
f_c_filt = 5e9    # Hz (cutoff frequency)

print(f"Stepped-impedance LPF: Z0 = {Z_0_filt} Ω, f_c = {f_c_filt/1e9:.0f} GHz")
print(f"Z_high = {Z_h} Ω, Z_low = {Z_l} Ω")

# For Chebyshev 0.5 dB, n=5:
# Series elements → high-Z lines of length θ_i
# Shunt elements → low-Z lines of length θ_i

# Line lengths in wavelengths at ω=1 (f_c)
# Simplified calculation:
# Series L: L_i = g_i * Z0 / (ω_c * Z_high) [in Henries]
# For distributed: θ_L = π/2 * (L_i / L_physical)...

# Physical implementation (approximate):
print("\nApproximate line lengths (at f_c):")
print("  Series stubs: θ ≈ 30°-60° (high-Z lines)")
print("  Shunt stubs: θ ≈ 30°-60° (low-Z lines)")

# Example: 5th order Chebyshev stepped-impedance filter
# Section 1 (series): θ = 60° at Z = 100 Ω
# Section 2 (shunt): θ = 50° at Z = 20 Ω
# etc.
print("\n  Section 1 (series): Z_h = 100 Ω, θ = 60°")
print("  Section 2 (shunt):  Z_l = 20 Ω,  θ = 50°")
print("  Section 3 (series): Z_h = 100 Ω, θ = 40°")
print("  ...")

# ============================================================================
# Example 8.4: Coupled-Line Bandpass Filter
# ============================================================================
print("\n" + "=" * 60)
print("Example 8.4: Coupled-Line Bandpass Filter")
print("=" * 60)

# 4-section coupled-line BPF at f0=5 GHz, BW=500 MHz (10%)
f_0_bpf = 5e9
BW_bpf = 500e6
N_bpf = 4  # number of sections

FBW = BW_bpf / f_0_bpf
print(f"Bandpass filter: f0 = {f_0_bpf/1e9:.0f} GHz, FBW = {FBW:.3f}")

# For n-section BPF, coupling matrix:
# M_ij = coupling between resonator i and j
# For 0.5 dB Chebyshev:

# Bandwidth-limited prototype values
# C_o = 2*sin((2i-1)*π/(2N)) for i = 1, 2, ... N
N_cpl = 4
C_o_vals = [2 * np.sin((2*i - 1) * np.pi / (2 * N_cpl)) for i in range(1, N_cpl + 1)]
print(f"\nCoupled-line coefficients C_o: {C_o_vals}")

# Approximate coupling coefficient:
# k_ij ≈ FBW * C_o_i * C_o_j / 2 for i≠j
print("\nCoupling coefficients (approximate):")
for i in range(N_cpl):
    for j in range(i+1, N_cpl):
        k = FBW * C_o_vals[i-1] * C_o_vals[j-1] / 2
        print(f"  k_{i+1},{j+1} ≈ {k:.4f}")

# Section lengths (λ/4 at f0)
c = 2.998e8
lambda_g_bpf = c / f_0_bpf / np.sqrt(4.7)  # assuming ε_r ~ 4.7
l_section = lambda_g_bpf / 4
print(f"\nSection length (λ/4 at f0): {l_section*100:.2f} cm")

# ============================================================================
# Example 8.5: Hairpin-Line Filter
# ============================================================================
print("\n" + "=" * 60)
print("Example 8.5: Hairpin-Line Resonator Filter")
print("=" * 60)

# Hairpin filter: coupled resonators folded into U-shape
# At f0=2 GHz, using λ/4 resonators on ε_r=10 substrate

f_0_hairpin = 2e9
eps_r_hairpin = 10.0
h_hairpin = 0.001  # substrate thickness (m)
Z0_hairpin = 50.0  # feed line Z0

# λ/4 resonator length (microstrip on ε_r=10)
v_p_hairpin = c / np.sqrt(eps_r_hairpin)
lambda_g_hairpin = v_p_hairpin / f_0_hairpin
l_resonator = lambda_g_hairpin / 4

print(f"Hairpin filter at f0 = {f_0_hairpin/1e9:.0f} GHz")
print(f"Substrate ε_r = {eps_r_hairpin}")
print(f"λ_g/4 resonator length ≈ {l_resonator*100:.2f} cm")
print(f"Coupling gap: 0.5-2 line widths for coupling strength")

# ============================================================================
# Example 8.6: Capacitive Iris Waveguide Filter
# ============================================================================
print("\n" + "=" * 60)
print("Example 8.6: Capacitive Iris Coupled Cavity Filter")
print("=" * 60)

# WR-90 waveguide (a=9cm, b=4cm) filter at 10 GHz
a_wg_filt = 0.09
b_wg_filt = 0.04
f_0_wgfilt = 10e9

# TE101 cavity dimensions for resonance at f0
# For circular iris: iris diameter controls coupling
# For capacitive iris: iris width controls coupling

print(f"Waveguide filter: WR-90, f0 = {f_0_wgfilt/1e9:.0f} GHz")
print(f"Cavity: a×b×d = {a_wg_filt*100:.0f}×{b_wg_filt*100:.0f}×5 cm (example)")
print(f"Iris: capacitive (narrowing in H-plane)")
print(f"Coupling controlled by iris width b' < b")
print(f"  b' = 0.2b → strong coupling")
print(f"  b' = 0.8b → weak coupling")

# ============================================================================
# Figure: Filter Responses and Structures
# ============================================================================
fig = plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.4, wspace=0.35)

# 1. Butterworth vs Chebyshev comparison
ax1 = fig.add_subplot(gs[0, 0])
omega_norm = np.linspace(0.01, 3, 500)

# Butterworth |S21|^2 = 1 / (1 + ω^2n)
S21_butt = 1 / np.sqrt(1 + omega_norm**10)
# Chebyshev (0.5 dB ripple): approximated
S21_cheb = 1 / np.sqrt(1 + 0.3493 * (np.cos(5 * np.arccos(np.clip(omega_norm, -1, 1))))**2)
S21_cheb = np.where(omega_norm > 1, 1 / np.sqrt(1 + 0.3493 * np.cosh(5 * np.arccosh(omega_norm))**2),
                     np.where(np.abs(omega_norm) < 1, 1 / np.sqrt(1 + 0.3493 * np.cos(5 * np.arccos(omega_norm))**2), 0))

# Simplified display
S21_butt_dB = 10 * np.log10(S21_butter := 1 / (1 + omega_norm**10) + 1e-10)
S21_cheb_dB = -0.5 - 10 * np.log10(1 + 0.3493 * (np.where(omega_norm <= 1, 
                              np.cos(5*np.arccos(omega_norm)), 
                              np.cosh(5*np.arccosh(omega_norm)))**2) + 1e-10)

ax1.plot(omega_norm, np.clip(S21_butt_dB, -40, 5), 'b-', lw=2, label='Butterworth')
ax1.plot(omega_norm, np.clip(S21_cheb_dB, -40, 5), 'r--', lw=2, label='Chebyshev (0.5 dB)')
ax1.axvline(x=1, color='gray', ls=':', alpha=0.7)
ax1.set_xlabel(r'$\omega/\omega_c$', fontsize=11)
ax1.set_ylabel(r'$|S_{21}|$ (dB)', fontsize=11)
ax1.set_title('LPF Response Comparison', fontsize=12)
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.set_ylim(-40, 5)
ax1.set_xlim(0, 3)

# 2. Stepped-impedance filter structure
ax2 = fig.add_subplot(gs[0, 1])
# Draw alternating high-low impedance lines
heights = [0.3, 0.15, 0.3, 0.15, 0.3, 0.15, 0.3]
x_pos = 0
for i, h in enumerate(heights):
    width = 0.15 if h > 0.2 else 0.2  # high Z = narrow, low Z = wide
    rect = plt.Rectangle((x_pos, 0), width, h, facecolor='steelblue', edgecolor='black')
    ax2.add_patch(rect)
    x_pos += width + 0.02

ax2.set_xlim(0, x_pos + 0.1)
ax2.set_ylim(0, 0.5)
ax2.set_title('Stepped-Impedance LPF', fontsize=12)
ax2.axis('off')

# 3. Coupled-line BPF schematic
ax3 = fig.add_subplot(gs[0, 2])
# Draw 4 coupled lines
n_cpl = 4
for i in range(n_cpl):
    ax3.plot([i, i], [0, 1], 'b-', lw=10)
    ax3.plot([i, i], [0, 1], 'r-', lw=1, alpha=0.5)  # coupling indication
    if i < n_cpl - 1:
        ax3.plot([i+0.5, i+0.5], [0, 1], 'g--', lw=1, alpha=0.5)

ax3.set_xlim(-0.5, n_cpl - 0.5)
ax3.set_ylim(-0.1, 1.1)
ax3.set_title('Coupled-Line BPF (4 sections)', fontsize=12)
ax3.axis('off')

# 4. Hairpin filter schematic
ax4 = fig.add_subplot(gs[1, 0])
# Draw U-shaped resonators
n_hair = 4
for i in range(n_hair):
    x = i * 0.8
    # Draw hairpin: down, across, up
    ax4.plot([x, x], [0, 0.4], 'b-', lw=3)
    ax4.plot([x, x+0.6], [0.4, 0.4], 'b-', lw=3)
    ax4.plot([x+0.6, x+0.6], [0.4, 0], 'b-', lw=3)
    # Coupling gap
    if i < n_hair - 1:
        ax4.plot([x+0.6, x+0.8], [0.2, 0.2], 'g--', lw=1)

ax4.set_xlim(-0.3, (n_hair-1)*0.8 + 1)
ax4.set_ylim(-0.1, 0.6)
ax4.set_title('Hairpin-Line Filter', fontsize=12)
ax4.axis('off')

# 5. Bandstop filter response
ax5 = fig.add_subplot(gs[1, 1])
f_bsf = np.linspace(0.5, 1.5, 300)
# Bandstop response
S21_bsf = 1 - 1/(1 + 1j*(f_bsf - 1)/0.05)**2
S21_bsf_mag = np.abs(S21_bsf)
ax5.plot(f_bsf, 20*np.log10(S21_bsf_mag + 1e-10), 'b-', lw=2)
ax5.axhline(y=-3, color='r', ls='--', alpha=0.7)
ax5.set_xlabel(r'$f/f_0$', fontsize=11)
ax5.set_ylabel(r'$|S_{21}|$ (dB)', fontsize=11)
ax5.set_title('Bandstop Filter Response (Simulated)', fontsize=12)
ax5.grid(True, alpha=0.3)
ax5.set_ylim(-40, 5)

# 6. Group delay
ax6 = fig.add_subplot(gs[1, 2])
# Linear phase (constant group delay) in passband
f_gd = np.linspace(0, 0.8, 200)
group_delay = np.ones_like(f_gd) * 2.0  # constant ~2 ns
ax6.plot(f_gd, group_delay, 'b-', lw=2)
ax6.set_xlabel(r'$f/f_0$', fontsize=11)
ax6.set_ylabel('Group Delay (ns)', fontsize=11)
ax6.set_title('Filter Group Delay (Linear Phase)', fontsize=12)
ax6.grid(True, alpha=0.3)
ax6.set_ylim(0, 5)

plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wbgc/code/wbgc_ch8_filters.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("\nSaved: wbgc_ch8_filters.png")

print("\n✅ Chapter 8 examples completed.")