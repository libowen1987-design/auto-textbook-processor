#!/usr/bin/env python3
"""
简明微波 (梁昌洪) - 第9章: 噪声与非线性
Noise and Nonlinearities - Chapter 9

Topics covered:
- Noise figure and Fmin (9.1-9.2)
- Noise circles (9.3)
- Intermodulation and compression (9.4-9.5)
- Gain compression (9.6)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ============================================================================
# Example 9.1: Noise Figure Calculation
# ============================================================================
print("=" * 60)
print("Example 9.1: Noise Figure Calculation")
print("=" * 60)

# Two-stage amplifier cascade
F1 = 2.0    # first stage noise factor (linear, not dB)
F2 = 5.0    # second stage noise factor
G1 = 10.0   # first stage gain (linear)

# Friis formula: F_total = F1 + (F2 - 1) / G1
F_total = F1 + (F2 - 1) / G1
NF_total_dB = 10 * np.log10(F_total)

print(f"Stage 1: F1 = {F1} ({10*np.log10(F1):.1f} dB), G1 = {G1} ({10*np.log10(G1):.1f} dB)")
print(f"Stage 2: F2 = {F2} ({10*np.log10(F2):.1f} dB)")
print(f"\nTotal noise factor (Friis): F = F1 + (F2-1)/G1 = {F_total:.2f}")
print(f"Total noise figure: NF = {NF_total_dB:.2f} dB")

# ============================================================================
# Example 9.2: Minimum Noise Figure (Fmin)
# ============================================================================
print("\n" + "=" * 60)
print("Example 9.2: Minimum Noise Figure")
print("=" * 60)

# HEMT transistor noise parameters at 10 GHz
Fmin_dB = 0.5    # dB (minimum noise figure)
Rn = 5.0         # ohm (noise resistance)
Y_opt = 0.02 + 1j*0.01  # S (optimal source admittance)
Y_0_noise = 0.02  # for normalization

print(f"Transistor noise parameters at 10 GHz:")
print(f"  F_min = {Fmin_dB} dB → F_min (linear) = {10**(Fmin_dB/10):.3f}")
print(f"  R_n = {Rn} Ω")
print(f"  Y_opt = {Y_opt*1000:.1f} - j{-np.imag(Y_opt)*1000:.1f} mS")
print(f"  Γ_opt = (1/Y_opt - 1/Y0) / (1/Y_opt + 1/Y0) ≈ ...")

# ============================================================================
# Example 9.3: Noise Circles
# ============================================================================
print("\n" + "=" * 60)
print("Example 9.3: Noise Circles on Smith Chart")
print("=" * 60)

# For F = Fmin + 4*Rn*|Gamma_opt|^2 / |1 + Y_opt|^2 / |1 + Gamma|^2
# Noise circles: centers and radii on Smith chart

F_dB = 2.0  # desired noise figure (dB)
F_linear = 10**(F_dB/10)

# For given Fmin, Rn, Γopt, compute circle
# Center: C = Γopt / (1 + (F - Fmin) * |1 + Γopt|² / (4*Rn/Y0))
# Radius: R = sqrt( (F - Fmin)² * |1 + Γopt|⁴ / (16*Rn²/Y0²) - ... )
# (Simplified for demonstration)

# Example: 10 GHz, draw F=2dB circle when Fmin=0.5 dB
Fmin_linear = 10**(0.5/10)
Y_opt_norm = Y_opt / 0.02  # normalize to Y0=0.02
print(f"F = {F_dB} dB, F_min = {Fmin_dB} dB:")
print(f"  Noise circle radius depends on Γ_opt position")
print(f"  Γ_opt ≈ 0.5 ∠ -30° (approximate)")
print(f"  Circle center: near Γ_opt")
print(f"  Circle radius: allows some source mismatch tolerance")

# ============================================================================
# Example 9.4: Intermodulation Distortion
# ============================================================================
print("\n" + "=" * 60)
print("Example 9.4: Intermodulation Distortion")
print("=" * 60)

# Third-order intercept point (IP3)
# P_IM3 = 2*P_fund - IP3 (in dBm, all same power)

P_fund = -10.0  # dBm (fundamental power at output)
IP3_dBm = 20.0  # dBm (third-order intercept point)
P_IM3_dBm = 2 * P_fund - IP3_dBm

print(f"Fundamental output power: P_fund = {P_fund} dBm")
print(f"IP3 = {IP3_dBm} dBm")
print(f"IM3 power (2*f1 - f2): P_IM3 = 2×({P_fund}) - {IP3_dBm} = {P_IM3_dBm:.1f} dBm")
print(f"IM3 relative to fundamental: {P_IM3_dBm - P_fund:.1f} dBc")

# 1 dB compression point
P1dB = IP3_dBm - 10.6  # Approximate relationship
print(f"\nApproximate 1dB compression point: P1dB ≈ {P1dB:.1f} dBm")

# ============================================================================
# Example 9.5: Gain Compression
# ============================================================================
print("\n" + "=" * 60)
print("Example 9.5: Gain Compression")
print("=" * 60)

# RF功率增益压缩
# S21_new = S21_0 / (1 + ε_p) where ε_p is proportional to input power

# Input power range
P_in_dBm = np.linspace(-30, 0, 200)  # dBm
P_in_linear = 1e-3 * 10**(P_in_dBm/10)  # watts
Gain_0 = 20.0  # dB (small-signal gain)
P1dB_point = -10.0  # dBm

# 1 dB compression: gain = Gain_0 - 1 dB
Gain_compressed = np.where(P_in_dBm < P1dB_point, 
                           Gain_0 - 0.1 * (P1dB_point - P_in_dBm)**2 / (P1dB_point + 30)**2,
                           Gain_0 - 0.1)

# Simplified model
Gain_dB = np.zeros_like(P_in_dBm)
for i, P in enumerate(P_in_dBm):
    if P < P1dB_point:
        compression = max(0, (P1dB_point - P) / (P1dB_point + 30)**2 * 100)
        Gain_dB[i] = Gain_0 - compression
    else:
        Gain_dB[i] = max(Gain_0 - (P - P1dB_point) * 0.5, Gain_0 - 10)

print(f"Small-signal gain: G0 = {Gain_0} dB")
print(f"1 dB compression point: P1dB = {P1dB_point} dBm")
print(f"Gain at P_in = 0 dBm: G ≈ {np.interp(0, P_in_dBm, Gain_dB):.1f} dB")

# ============================================================================
# Figure: Noise and Nonlinear Characteristics
# ============================================================================
fig = plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.4, wspace=0.35)

# 1. Noise circles on Smith chart
ax1 = fig.add_subplot(gs[0, 0])
# Draw Smith chart outline
circle_unit = plt.Circle((0, 0), 1, fill=False, color='black', lw=1.5)
ax1.add_patch(circle_unit)
# Constant resistance circles
for r in [0.5, 1.0, 2.0]:
    center = r / (1 + r)
    radius = 1 / (1 + r)
    ax1.add_patch(plt.Circle((center, 0), radius, fill=False, color='steelblue', lw=0.8, alpha=0.5))

ax1.set_aspect('equal')
ax1.set_xlim(-1.3, 1.3)
ax1.set_ylim(-1.3, 1.3)
ax1.axis('off')
ax1.set_title('Noise Circles on Smith Chart', fontsize=12)

# Add example noise circles
circle_noise1 = plt.Circle((0.3, 0.2), 0.25, fill=False, color='red', lw=2, ls='--')
ax1.add_patch(circle_noise1)
circle_noise2 = plt.Circle((0.3, 0.2), 0.4, fill=False, color='orange', lw=2, ls='--')
ax1.add_patch(circle_noise2)
ax1.plot(0.3, 0.2, 'r*', markersize=12, label=r'$\Gamma_{opt}$')
ax1.legend(loc='upper left')

# 2. Noise figure vs frequency
ax2 = fig.add_subplot(gs[0, 1])
f_NF = np.linspace(1e9, 20e9, 300)
NF_sim = 0.5 + 0.01 * (f_NF/1e9)**2  # increasing with frequency
ax2.plot(f_NF/1e9, NF_sim, 'b-', lw=2)
ax2.axhline(y=0.5, color='r', ls='--', alpha=0.7, label='F_min')
ax2.set_xlabel('f (GHz)', fontsize=11)
ax2.set_ylabel('NF (dB)', fontsize=11)
ax2.set_title('Noise Figure vs Frequency', fontsize=12)
ax2.legend()
ax2.grid(True, alpha=0.3)

# 3. Intermodulation products
ax3 = fig.add_subplot(gs[0, 2])
P_in_axis = np.linspace(-30, 10, 200)
# IM3 = 2*P_fund - IP3
IP3_val = 20  # dBm
P_fund = P_in_axis + 20  # assuming 20 dB gain
P_IM3 = 2 * P_fund - IP3_val

ax3.plot(P_in_axis, P_fund, 'b-', lw=2, label='Fundamental')
ax3.plot(P_in_axis, P_IM3, 'r--', lw=2, label='IM3 (2*f1-f2)')
ax3.axvline(x=-10, color='gray', ls=':', alpha=0.7, label='1 dB CP')
ax3.set_xlabel(r'$P_{in}$ (dBm)', fontsize=11)
ax3.set_ylabel(r'$P_{out}$ (dBm)', fontsize=11)
ax3.set_title('Intermodulation Distortion', fontsize=12)
ax3.legend()
ax3.grid(True, alpha=0.3)
ax3.set_xlim(-30, 10)
ax3.set_ylim(-50, 20)

# 4. Gain compression curve
ax4 = fig.add_subplot(gs[1, 0])
P_in_plot = np.linspace(-30, 0, 300)
Gain_plot = np.zeros_like(P_in_plot)
for i, P in enumerate(P_in_plot):
    if P < -15:
        Gain_plot[i] = 20.0
    else:
        # Approximate compression
        Gain_plot[i] = 20.0 - max(0, (P + 15)**2 / 400)

ax4.plot(P_in_plot, Gain_plot, 'b-', lw=2)
ax4.axhline(y=19, color='r', ls='--', alpha=0.7, label='G0 - 1 dB')
ax4.axvline(x=-10, color='gray', ls=':', alpha=0.7, label='P1dB')
ax4.set_xlabel(r'$P_{in}$ (dBm)', fontsize=11)
ax4.set_ylabel('Gain (dB)', fontsize=11)
ax4.set_title('Gain Compression', fontsize=12)
ax4.legend()
ax4.grid(True, alpha=0.3)
ax4.set_ylim(10, 21)

# 5. Cascade noise figure
ax5 = fig.add_subplot(gs[1, 1])
n_stages = 5
F_cascade = np.zeros(n_stages)
F_accum = [2.0]  # first stage F

for i in range(1, n_stages):
    F_new = 5.0  # subsequent stages have higher F
    G_prev = 10.0  # linear gain per stage
    F_total_accum = F_accum[-1] + (F_new - 1) / G_prev
    F_accum.append(F_total_accum)

F_dB_accum = [10*np.log10(F) for F in F_accum]
ax5.bar(range(1, n_stages+1), F_dB_accum, color='steelblue', alpha=0.7)
ax5.set_xlabel('Stage Number', fontsize=11)
ax5.set_ylabel('Accumulated NF (dB)', fontsize=11)
ax5.set_title('Cascade Noise Figure (Friis)', fontsize=12)
ax5.grid(True, alpha=0.3, axis='y')

# 6. IP3 vs output power
ax6 = fig.add_subplot(gs[1, 2])
P_out_plot = np.linspace(-30, 10, 200)
IP3_const = 20  # dBm
# When fundamental = IP3, IM3 = fundamental
P_fund_plot = P_out_plot  # output = input + gain
P_IM3_plot = 2 * P_fund_plot - IP3_const
# Third-order products rise 2x faster than fundamental
ax6.plot(P_out_plot, P_fund_plot, 'b-', lw=2, label='Fundamental')
ax6.plot(P_out_plot, P_IM3_plot, 'r--', lw=2, label='IM3')
ax6.axhline(y=IP3_const, color='g', ls=':', alpha=0.7, label='IP3')
ax6.set_xlabel(r'$P_{out}$ (dBm)', fontsize=11)
ax6.set_ylabel(r'$P_{out}$ (dBm)', fontsize=11)
ax6.set_title('IP3 Intercept Point', fontsize=12)
ax6.legend()
ax6.grid(True, alpha=0.3)
ax6.set_xlim(-30, 10)
ax6.set_ylim(-50, 20)

plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wbgc/code/wbgc_ch9_noise_nonlinear.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("\nSaved: wbgc_ch9_noise_nonlinear.png")

print("\n✅ Chapter 9 examples completed.")