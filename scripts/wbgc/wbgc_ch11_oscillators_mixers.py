#!/usr/bin/env python3
"""
简明微波 (梁昌洪) - 第11章: 振荡器与混频器
Oscillators and Mixers - Chapter 11

Topics covered:
- Oscillator fundamentals (11.1)
- Negative resistance oscillators (11.2)
- Oscillator design (11.3)
- Mixer fundamentals (11.4)
- Conversion loss (11.5)
- Mixer design (11.6)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ============================================================================
# Example 11.1: Negative Resistance Oscillator Condition
# ============================================================================
print("=" * 60)
print("Example 11.1: Negative Resistance Oscillator")
print("=" * 60)

# For oscillation: Z_in + Z_L = 0
# Or: Γ_in * Γ_L = 1 (with proper phase)
# Negative resistance: R_in < 0 for oscillator active region

R_active = -50.0   # ohm (negative resistance of active device)
R_load = 50.0      # ohm (load resistance)
L_react = 20.0    # ohm (reactive part)

Z_in_osc = R_active + 1j * L_react
Z_load = R_load

print(f"Active device impedance: Z_in = {Z_in_osc} Ω")
print(f"Load impedance: Z_L = {Z_load} Ω")
print(f"\nTotal impedance: Z_total = {Z_in_osc + Z_load} Ω")
print(f"  R_total = {np.real(Z_in_osc + Z_load):.1f} Ω")
print(f"  X_total = {np.imag(Z_in_osc + Z_load):.1f} Ω")

# For sustained oscillation: R_total = 0 and X_total = 0
# or equivalently: |Γ_in| > 1 at the desired frequency

Gamma_in = (Z_in_osc - 50) / (Z_in_osc + 50)  # with reference Z0 = 50
print(f"\nReflection coefficient at input: Γ_in = {Gamma_in:.4f}")
print(f"  |Γ_in| = {np.abs(Gamma_in):.4f}")
if np.abs(Gamma_in) > 1:
    print("  → Oscillation condition satisfied (|Γ_in| > 1)")

# ============================================================================
# Example 11.2: Oscillator Frequency Stability
# ============================================================================
print("\n" + "=" * 60)
print("Example 11.2: Oscillator Frequency Stability")
print("=" * 60)

# Loaded Q for oscillator frequency stability
Q_L = 100    # loaded Q
f_osc = 10e9 # oscillation frequency (Hz)
delta_f = f_osc / Q_L  # frequency stability

print(f"Oscillator frequency: f_0 = {f_osc/1e9:.0f} GHz")
print(f"Loaded Q = {Q_L}")
print(f"Frequency stability: Δf = f_0/Q_L = {delta_f/1e6:.1f} MHz")
print(f"Relative stability: Δf/f_0 = {delta_f/f_osc*1e6:.2f} ppm")

# ============================================================================
# Example 11.3: Crystal Oscillator (Reference)
# ============================================================================
print("\n" + "=" * 60)
print("Example 11.3: Crystal Oscillator at 10 MHz")
print("=" * 60)

f_crystal = 10e6   # Hz
Q_crystal = 50000  # very high Q for crystal

print(f"Crystal: f = {f_crystal/1e6:.0f} MHz, Q = {Q_crystal}")
print(f"  Δf/f_0 = 1/Q = {1/Q_crystal:.2e} (≈ {1/Q_crystal*1e6:.2f} ppm)")
print(f"  Excellent frequency stability")

# ============================================================================
# Example 11.4: Diode Mixer Fundamentals
# ============================================================================
print("\n" + "=" * 60)
print("Example 11.4: Diode Mixer")
print("=" * 60)

# Simple diode mixer: RF + LO = IF
f_RF = 10e9    # GHz (RF frequency)
f_LO = 9.7e9   # GHz (LO frequency, 300 MHz below RF)
f_IF = f_RF - f_LO  # = 300 MHz (IF frequency)

print(f"Mixer: RF = {f_RF/1e9:.1f} GHz, LO = {f_LO/1e9:.1f} GHz")
print(f"  IF = f_RF - f_LO = {f_IF/1e6:.0f} MHz (downconversion)")

# Mixer's spurious products
# n*f_RF ± m*f_LO = f_IF
# n=1, m=1: f_RF - f_LO = 300 MHz (desired)
# n=1, m=2: f_RF - 2*f_LO = ... spurious

print(f"\nSpurious products (n*RF - m*LO):")
for n in range(1, 4):
    for m in range(1, 4):
        f_sp = n * f_RF - m * f_LO
        if f_sp > 0 and f_sp < 1e9:
            print(f"  n={n}, m={m}: {f_sp/1e6:.0f} MHz")

# ============================================================================
# Example 11.5: Mixer Conversion Loss
# ============================================================================
print("\n" + "=" * 60)
print("Example 11.5: Mixer Conversion Loss")
print("=" * 60)

# Single-balanced mixer: CL ≈ 4-7 dB (typical)
# Double-balanced mixer: CL ≈ 6-9 dB (typical)
CL_single_dB = 5.5  # dB (single-balanced Schottky diode mixer)
CL_double_dB = 7.0  # dB (double-balanced mixer)

print(f"Single-balanced diode mixer: CL ≈ {CL_single_dB} dB")
print(f"Double-balanced mixer: CL ≈ {CL_double_dB} dB")
print(f"\nConversion loss components:")
print(f"  - Diode resistance (match loss): ~2 dB")
print(f"  - Conversion efficiency: ~2 dB")
print(f"  - LO noise contribution: ~1 dB")

# For image-reject mixer: additional loss due to filter
CL_IR_dB = CL_single_dB + 3  # ~3 dB for image rejection filter
print(f"\nImage-reject mixer: CL ≈ {CL_IR_dB} dB (includes filter loss)")

# ============================================================================
# Example 11.6: Noise Sideband Ratio
# ============================================================================
print("\n" + "=" * 60)
print("Example 11.6: Noise Sideband Ratio (NSR)")
print("=" * 60)

# Noise sideband ratio for mixer
# NSSR = P_LM / P_USB (noise in lower sideband vs upper sideband)
# For single-sideband mixing: image noise adds to total

f_IF_noise = 300e6  # IF frequency
f_LO_mix = 10e9

# Two noise sidebands (upper and lower) folded to IF
# USB: f_RF = f_LO + f_IF = 10.3 GHz
# LSB: f_RF = f_LO - f_IF = 9.7 GHz
f_USB = f_LO_mix + f_IF_noise
f_LSB = f_LO_mix - f_IF_noise

print(f"LO = {f_LO_mix/1e9:.1f} GHz, IF = {f_IF_noise/1e6:.0f} MHz")
print(f"  USB: f_RF = f_LO + f_IF = {f_USB/1e9:.3f} GHz")
print(f"  LSB: f_RF = f_LO - f_IF = {f_LSB/1e9:.3f} GHz")
print(f"\nNoise sideband ratio: NSSR = P_{f_LSB/1e9:.1f} / P_{f_USB/1e9:.1f}")
print(f"  For conversion loss measurement: account for image noise")

# ============================================================================
# Figure: Oscillator and Mixer Characteristics
# ============================================================================
fig = plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.4, wspace=0.35)

# 1. Negative resistance region
ax1 = fig.add_subplot(gs[0, 0])
R_range = np.linspace(-100, 100, 200)
Gamma_mag = np.abs((R_range - 50) / (R_range + 50))
ax1.plot(R_range, Gamma_mag, 'b-', lw=2)
ax1.axvline(x=0, color='gray', ls=':', alpha=0.7)
ax1.axhline(y=1, color='r', ls='--', alpha=0.7, label='|Γ|=1 (oscillation threshold)')
ax1.set_xlabel(r'$R_{in}$ (Ω)', fontsize=11)
ax1.set_ylabel(r'$|\Gamma_{in}|$', fontsize=11)
ax1.set_title('Negative Resistance Oscillator Condition', fontsize=12)
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.set_xlim(-100, 100)
ax1.set_ylim(0, 3)

# 2. Oscillator frequency stability (Q effect)
ax2 = fig.add_subplot(gs[0, 1])
Q_range = np.linspace(10, 1000, 200)
delta_f_stability = 10e9 / Q_range / 1e6  # MHz
ax2.plot(Q_range, delta_f_stability, 'b-', lw=2)
ax2.set_xlabel('Loaded Q', fontsize=11)
ax2.set_ylabel(r'$\Delta f$ (MHz)', fontsize=11)
ax2.set_title('Oscillator Frequency Stability vs Q', fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.set_xlim(10, 1000)

# 3. Mixer spurious products
ax3 = fig.add_subplot(gs[0, 2])
# Show mixing products up to 3rd order
f_RF_plot = np.linspace(9.5, 10.5, 300)
f_LO_fix = 10.0
f_IF_calc = f_RF_plot - f_LO_fix

ax3.plot(f_RF_plot, np.abs(f_IF_calc)/1e6, 'b-', lw=2, label='1st order (f_RF - f_LO)')
ax3.set_xlabel(r'$f_{RF}$ (GHz)', fontsize=11)
ax3.set_ylabel(r'$f_{IF}$ (MHz)', fontsize=11)
ax3.set_title('Mixer Frequency Conversion', fontsize=12)
ax3.legend()
ax3.grid(True, alpha=0.3)
ax3.set_xlim(9.5, 10.5)

# 4. Conversion loss vs LO power
ax4 = fig.add_subplot(gs[1, 0])
P_LO_dBm = np.linspace(0, 15, 200)
CL_vs_LO = 10 - 0.2 * (P_LO_dBm - 5)  # improving with more LO power
CL_vs_LO = np.clip(CL_vs_LO, 4, 12)
ax4.plot(P_LO_dBm, CL_vs_LO, 'b-', lw=2)
ax4.set_xlabel(r'$P_{LO}$ (dBm)', fontsize=11)
ax4.set_ylabel('Conversion Loss (dB)', fontsize=11)
ax4.set_title('Mixer CL vs LO Power', fontsize=12)
ax4.grid(True, alpha=0.3)
ax4.set_ylim(4, 12)

# 5. Double-balanced mixer schematic
ax5 = fig.add_subplot(gs[1, 1])
# Draw ring mixer (Gilbert cell style)
center_x, center_y = 0, 0
# Draw transformer-coupled ring
for i in range(4):
    angle = np.radians(i * 90)
    x = 0.5 * np.cos(angle)
    y = 0.5 * np.sin(angle)
    ax5.plot([0, x], [0, y], 'b-', lw=2)
    
# 4 diodes in ring
ax5.plot([0.3, 0.7], [0.3, 0.7], 'g-', lw=3)  # diode 1
ax5.plot([-0.7, -0.3], [0.3, 0.7], 'g-', lw=3)  # diode 2
ax5.plot([-0.3, -0.7], [-0.7, -0.3], 'g-', lw=3)  # diode 3
ax5.plot([0.3, 0.7], [-0.7, -0.3], 'g-', lw=3)  # diode 4

ax5.set_xlim(-1, 1)
ax5.set_ylim(-1, 1)
ax5.set_title('Double-Balanced Mixer (Ring)', fontsize=12)
ax5.axis('off')
ax5.text(0, 0.8, 'LO', fontsize=10, ha='center')
ax5.text(0, -0.8, 'LO', fontsize=10, ha='center')
ax5.text(0.8, 0, 'RF', fontsize=10)
ax5.text(-0.8, 0, 'IF', fontsize=10)

# 6. Phase noise in oscillators
ax6 = fig.add_subplot(gs[1, 2])
f_offset = np.logspace(1, 6, 200)  # Hz offset from carrier
# Phase noise: L(f) ≈ -100 + 10*log10(f_offset) dBc/Hz (typical X-band)
L_f = -100 + 10 * np.log10(f_offset)
ax6.semilogx(f_offset, L_f, 'b-', lw=2)
ax6.set_xlabel(r'$f_{offset}$ (Hz)', fontsize=11)
ax6.set_ylabel(r'$L(f)$ (dBc/Hz)', fontsize=11)
ax6.set_title('Oscillator Phase Noise', fontsize=12)
ax6.grid(True, alpha=0.3)
ax6.set_xlim(10, 1e6)
ax6.set_ylim(-150, -50)

plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wbgc/code/wbgc_ch11_oscillators_mixers.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("\nSaved: wbgc_ch11_oscillators_mixers.png")

print("\n✅ Chapter 11 examples completed.")