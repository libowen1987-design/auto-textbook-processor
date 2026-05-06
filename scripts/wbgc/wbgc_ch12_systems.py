#!/usr/bin/env python3
"""
简明微波 (梁昌洪) - 第12章: 微波系统与测量
Microwave Systems and Measurements - Chapter 12

Topics covered:
- Network analyzer fundamentals (12.1)
- S-parameter measurement (12.2)
- Time-domain reflectometry (TDR) (12.3)
- Power measurements (12.4)
- Noise measurement (12.5)
- System examples: radar, communication links (12.6)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ============================================================================
# Example 12.1: Network Analyzer Basics
# ============================================================================
print("=" * 60)
print("Example 12.1: Network Analyzer Fundamentals")
print("=" * 60)

# VNA (Vector Network Analyzer) measures S-parameters
# Key specifications: frequency range, dynamic range, measurement speed

f_VNA = 10e9   # Hz
dynamic_range = 100  # dB
trace_noise = 0.01  # dB (RMS)

print(f"VNA at f = {f_VNA/1e9:.0f} GHz:")
print(f"  Dynamic range: {dynamic_range} dB")
print(f"  Trace noise: {trace_noise} dB RMS")
print(f"  Measurement: S11, S21, S12, S22 (2-port)")
print(f"  Or: S11, S22, S21, S12, S33, S34, ... (multi-port)")

# ============================================================================
# Example 12.2: S-Parameter Measurement Accuracy
# ============================================================================
print("\n" + "=" * 60)
print("Example 12.2: S-Parameter Measurement Uncertainty")
print("=" * 60)

# Directivity, source match, load match, reflection tracking
# Keys: E, F, G, H for error terms in 12-term error model

E_D = 0.01      # directivity (linear)
E_S = 0.02      # source match (linear)
E_L = 0.02      # load match (linear)
E_R = 0.98      # reflection tracking (linear)

print("12-term error model coefficients (linear):")
print(f"  E_D (directivity): {E_D:.4f} → {20*np.log10(E_D):.1f} dB")
print(f"  E_S (source match): {E_S:.4f} → {20*np.log10(E_S):.1f} dB")
print(f"  E_L (load match): {E_L:.4f} → {20*np.log10(E_L):.1f} dB")
print(f"  E_R (reflection tracking): {E_R:.4f} → {20*np.log10(E_R):.1f} dB")

# For S11 measurement accuracy:
# σ_S11 ≈ E_D + E_R * E_S
sigma_S11 = E_D + E_R * E_S
print(f"\nS11 measurement uncertainty: σ ≈ {sigma_S11:.4f} ({20*np.log10(sigma_S11):.1f} dB)")

# ============================================================================
# Example 12.3: Time-Domain Reflectometry (TDR)
# ============================================================================
print("\n" + "=" * 60)
print("Example 12.3: Time-Domain Reflectometry (TDR)")
print("=" * 60)

# TDR: impulse → reflections reveal impedance discontinuities
# Resolution: Δz = v_p * Δt / 2 (round trip)
v_p_tdr = 2e8   # m/s (in stripline)
delta_t = 0.1e-9  # s (100 ps resolution)

delta_z = v_p_tdr * delta_t / 2
print(f"TDR resolution:")
print(f"  v_p = {v_p_tdr/1e6:.0f} km/s, Δt = {delta_t*1e12:.0f} ps")
print(f"  Δz = v_p * Δt / 2 = {delta_z*100:.2f} cm (spatial resolution)")

# Fault location: z = v_p * t / 2
t_reflect = 2e-9  # reflection at t = 2 ns
z_fault = v_p_tdr * t_reflect / 2
print(f"\nFault at t = {t_reflect*1e9:.0f} ns: z = {z_fault*100:.0f} cm")

# ============================================================================
# Example 12.4: Power Measurement
# ============================================================================
print("\n" + "=" * 60)
print("Example 12.4: Power Measurement")
print("=" * 60)

# Power sensor types: thermistor, diode, thermocouple
# Power meter calibration: 0 dBm = 1 mW

P_ref_dBm = 0.0   # reference: 0 dBm
P_ref_W = 1e-3    # 1 mW

# Measurement range
P_min_dBm = -70.0  # dBm (thermal noise limited)
P_max_dBm = 20.0   # dBm (damage threshold)

print(f"Power measurement range:")
print(f"  Minimum: {P_min_dBm} dBm = {10**(P_min_dBm/10)*1000:.2f} µW")
print(f"  Maximum: {P_max_dBm} dBm = {10**(P_max_dBm/10)*1000:.2f} mW")

# Sensor types and characteristics
print(f"\nPower sensor types:")
print(f"  Thermistor: 0.1-10 mW, accurate, slow")
print(f"  Diode detector: -60 to -10 dBm, fast, less accurate")
print(f"  Thermocouple: -30 to +10 dBm, moderate speed/accuracy")

# ============================================================================
# Example 12.5: Noise Measurement
# ============================================================================
print("\n" + "=" * 60)
print("Example 12.5: Noise Figure Measurement (Y-factor Method)")
print("=" * 60)

# Y-factor method: hot load vs cold load
T_cold = 290    # K (cold, room temperature)
T_hot = 29000   # K (hot load, e.g., noise tube)
Y = 10.0        # ratio (linear)

# Noise figure: F = (T_hot - Y * T_cold) / (Y - 1) / T_cold + 1
F_Y = (T_hot - Y * T_cold) / ((Y - 1) * T_cold) + 1
NF_Y_dB = 10 * np.log10(F_Y)

print(f"Y-factor method:")
print(f"  T_cold = {T_cold} K, T_hot = {T_hot/1000:.0f} kK")
print(f"  Y = {Y} (linear ratio)")
print(f"  F = {F_Y:.2f} (linear) → NF = {NF_Y_dB:.2f} dB")

# ENR (Excess Noise Ratio) of hot load
ENR = (T_hot - T_cold) / T_cold
print(f"\nHot load ENR = {ENR:.1f} = {10*np.log10(ENR):.1f} dB")

# ============================================================================
# Example 12.6: Radar Range Equation
# ============================================================================
print("\n" + "=" * 60)
print("Example 12.6: Radar Range Equation")
print("=" * 60)

# Radar range: R_max = (P_t * G * σ * λ²)^(1/4) / (4³π³ * k * T * B * SNR_min)^(1/4)
P_t = 1e6        # W (1 MW peak)
G = 40           # dB (antenna gain)
G_linear = 10**(G/10)  # 10000
sigma_rcs = 1.0   # m² (Radar cross-section of target)
lambda_radar = 0.03  # m (10 GHz, λ = 3 cm)
k_B = 1.38e-23   # Boltzmann constant
T_noise = 290     # K
B_radar = 1e6     # Hz (1 MHz IF bandwidth)
SNR_min = 10.0    # minimum detectable SNR (linear)

# Constants
const = 16 * np.pi**3 * k_B * T_noise * B_radar * SNR_min
numerator = P_t * G_linear * sigma_rcs * lambda_radar**2

R_max = (numerator / const)**(0.25)
print(f"Radar system parameters:")
print(f"  P_t = {P_t/1e6:.0f} MW (peak power)")
print(f"  G = {G} dB ({G_linear:.0f} linear)")
print(f"  λ = {lambda_radar*100:.0f} cm")
print(f"  σ = {sigma_rcs:.1f} m²")
print(f"  B = {B_radar/1e6:.0f} MHz")
print(f"  SNR_min = {SNR_min:.0f}")
print(f"\nMaximum range: R_max ≈ {R_max/1000:.1f} km")

# ============================================================================
# Figure: Network Analysis and Measurement Systems
# ============================================================================
fig = plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.4, wspace=0.35)

# 1. VNA block diagram (simplified)
ax1 = fig.add_subplot(gs[0, 0])
# Source
ax1.add_patch(plt.Rectangle((0, 0.4), 0.8, 0.2, facecolor='lightblue', edgecolor='black'))
ax1.text(0.4, 0.5, 'Source', fontsize=9, ha='center', va='center')
# DUT
ax1.add_patch(plt.Rectangle((1.5, 0.35), 1.0, 0.3, facecolor='coral', edgecolor='black'))
ax1.text(2.0, 0.5, 'DUT', fontsize=9, ha='center', va='center')
# Reference and test receivers
ax1.add_patch(plt.Rectangle((3.0, 0.1), 0.8, 0.2, facecolor='lightgreen', edgecolor='black'))
ax1.text(3.4, 0.2, 'Ref Rcv', fontsize=8, ha='center', va='center')
ax1.add_patch(plt.Rectangle((3.0, 0.6), 0.8, 0.2, facecolor='lightgreen', edgecolor='black'))
ax1.text(3.4, 0.7, 'Test Rcv', fontsize=8, ha='center', va='center')
# Lines
ax1.plot([0.8, 1.5], [0.55, 0.5], 'k-', lw=2)
ax1.plot([2.5, 3.0], [0.55, 0.6], 'k-', lw=2)
ax1.plot([2.5, 3.0], [0.45, 0.3], 'k-', lw=2)
ax1.plot([0, 0.4], [0.55, 0.55], 'k-', lw=2)
ax1.set_xlim(-0.5, 4)
ax1.set_ylim(-0.1, 1.0)
ax1.set_title('VNA Block Diagram', fontsize=12)
ax1.axis('off')

# 2. Error model visualization
ax2 = fig.add_subplot(gs[0, 1])
# Draw 12-term error model as 2-port network
ax2.add_patch(plt.Rectangle((0.5, 0.3), 1.0, 0.4, facecolor='coral', edgecolor='black'))
ax2.text(1.0, 0.5, 'DUT', fontsize=10, ha='center', va='center')
# Error boxes
ax2.text(0.1, 0.7, 'Forward\nErrors', fontsize=8, ha='center', color='blue')
ax2.text(2.5, 0.7, 'Reverse\nErrors', fontsize=8, ha='center', color='red')
ax2.set_xlim(-0.5, 3.5)
ax2.set_ylim(0, 1)
ax2.set_title('12-Term Error Model', fontsize=12)
ax2.axis('off')

# 3. TDR response
ax3 = fig.add_subplot(gs[0, 2])
t_tdr = np.linspace(0, 5, 500)  # ns
# TDR with impedance discontinuity
V_tdr = np.ones_like(t_tdr)
# At t=1.5ns: 50 ohm to 75 ohm (positive step)
V_tdr = np.where(t_tdr < 1.5, 0.5, 
                 np.where(t_tdr < 2.5, 0.5 + 0.5*(1 - np.exp(-(t_tdr - 1.5)*10)) * 0.2, 0.7))
# Add some oscillation
V_tdr = V_tdr + 0.02 * np.sin(2*np.pi*3*t_tdr) * np.exp(-t_tdr*0.5)

ax3.plot(t_tdr, V_tdr, 'b-', lw=2)
ax3.set_xlabel('Time (ns)', fontsize=11)
ax3.set_ylabel('V (normalized)', fontsize=11)
ax3.set_title('TDR Response (50Ω to 75Ω Step)', fontsize=12)
ax3.grid(True, alpha=0.3)
ax3.set_xlim(0, 5)

# 4. Power meter calibration curve
ax4 = fig.add_subplot(gs[1, 0])
P_in_dBm_cal = np.linspace(-60, 0, 300)
V_output = 10**((P_in_dBm_cal + 60)/20)  # simplified diode detector
ax4.semilogy(P_in_dBm_cal, V_output, 'b-', lw=2)
ax4.set_xlabel(r'$P_{in}$ (dBm)', fontsize=11)
ax4.set_ylabel('Detector Output (V)', fontsize=11)
ax4.set_title('Diode Detector Response', fontsize=12)
ax4.grid(True, alpha=0.3)

# 5. Noise figure measurement setup
ax5 = fig.add_subplot(gs[1, 1])
# Y-factor method diagram
ax5.add_patch(plt.Rectangle((0.5, 0.5), 1, 0.3, facecolor='lightgray', edgecolor='black'))
ax5.text(1, 0.65, 'Noise\nSource', fontsize=8, ha='center', va='center')
ax5.add_patch(plt.Rectangle((2.0, 0.45), 0.8, 0.4, facecolor='coral', edgecolor='black'))
ax5.text(2.4, 0.65, 'DUT', fontsize=8, ha='center', va='center')
ax5.add_patch(plt.Rectangle((3.2, 0.5), 1, 0.3, facecolor='lightblue', edgecolor='black'))
ax5.text(3.7, 0.65, 'Power\nMeter', fontsize=8, ha='center', va='center')
ax5.annotate('', xy=(1.5, 0.65), xytext=(0.5, 0.65), arrowprops=dict(arrowstyle='->', lw=2))
ax5.annotate('', xy=(2.8, 0.65), xytext=(2.0, 0.65), arrowprops=dict(arrowstyle='->', lw=2))
ax5.annotate('', xy=(4.2, 0.65), xytext=(3.2, 0.65), arrowprops=dict(arrowstyle='->', lw=2))
ax5.set_xlim(0, 5)
ax5.set_ylim(0.2, 1)
ax5.set_title('NF Measurement (Y-factor Method)', fontsize=12)
ax5.axis('off')

# 6. Radar range vs SNR
ax6 = fig.add_subplot(gs[1, 2])
R_range = np.linspace(1, 100, 300)  # km
SNR_radar = 10 * np.log10((R_range/100)**-4 * 1000)  # simplified
ax6.plot(R_range, SNR_radar, 'b-', lw=2)
ax6.axhline(y=10, color='r', ls='--', alpha=0.7, label='SNR_min = 10 dB')
ax6.set_xlabel('Range (km)', fontsize=11)
ax6.set_ylabel('SNR (dB)', fontsize=11)
ax6.set_title('Radar Range vs SNR', fontsize=12)
ax6.legend()
ax6.grid(True, alpha=0.3)
ax6.set_xlim(1, 100)

plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wbgc/code/wbgc_ch12_systems.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("\nSaved: wbgc_ch12_systems.png")

print("\n✅ Chapter 12 examples completed.")