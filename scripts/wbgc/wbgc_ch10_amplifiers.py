#!/usr/bin/env python3
"""
简明微波 (梁昌洪) - 第10章: 微波放大器
Microwave Amplifiers - Chapter 10

Topics covered:
- Amplifier design fundamentals (10.1)
- Stability and Rollett criterion (10.2)
- Power gain circles (10.3)
- Constant gain and noise circles (10.4-10.5)
- Design examples: low-noise, power amplifiers (10.6-10.7)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ============================================================================
# Example 10.1: Amplifier Stability (Rollett Criterion)
# ============================================================================
print("=" * 60)
print("Example 10.1: Amplifier Stability (Rollett Criterion)")
print("=" * 60)

# Two-port S-parameters of a transistor at 10 GHz
S11 = 0.7 * np.exp(1j * np.radians(150))
S12 = 0.05 * np.exp(1j * np.radians(30))
S21 = 2.5 * np.exp(1j * np.radians(-30))
S22 = 0.6 * np.exp(1j * np.radians(-120))

print("Transistor S-parameters at 10 GHz:")
print(f"  S11 = {S11:.4f}")
print(f"  S12 = {S12:.4f}")
print(f"  S21 = {S21:.4f}")
print(f"  S22 = {S22:.4f}")

# Rollett stability factor: K = (1 - |S11|² - |S22|² + |D|²) / (2|S12||S21|)
D = S11 * S22 - S12 * S21
K = (1 - np.abs(S11)**2 - np.abs(S22)**2 + np.abs(D)**2) / (2 * np.abs(S12) * np.abs(S21))

print(f"\n  D = S11*S22 - S12*S21 = {D:.4f}")
print(f"  |D| = {np.abs(D):.4f}")
print(f"  K (Rollett factor) = {K:.4f}")

if K > 1 and np.abs(D) < 1:
    print("  → Unconditionally stable")
elif K < 1:
    print("  → Potentially unstable (K < 1)")
    # Check |D| < 1 as well
    if np.abs(D) < 1:
        print("  → |D| < 1, but K < 1: conditionally stable")
else:
    print("  → Check potentially unstable region")

# ============================================================================
# Example 10.2: Unilateral Figure of Merit
# ============================================================================
print("\n" + "=" * 60)
print("Example 10.2: Unilateral Figure of Merit")
print("=" * 60)

# |S12| is often small → unilateral approximation
# u = |S12||S21||S11||S22| / (1 - |S11|²)(1 - |S22|²)
u = (np.abs(S12) * np.abs(S21) * np.abs(S11) * np.abs(S22)) / \
    ((1 - np.abs(S11)**2) * (1 - np.abs(S22)**2))

print(f"Unilateral figure of merit u = {u:.4f}")
print(f"  If u << 1, unilateral approximation is valid")
print(f"  Error bound: Δ|S11| < u, etc.")

if u < 0.1:
    print(f"  u = {u:.4f} < 0.1: unilateral approximation reasonable")
else:
    print(f"  u = {u:.4f} > 0.1: unilateral approximation may have significant error")

# ============================================================================
# Example 10.3: Power Gain - Available Power Gain
# ============================================================================
print("\n" + "=" * 60)
print("Example 10.3: Power Gain Calculations")
print("=" * 60)

# For matched condition (no mismatch losses)
# MSG (Maximum Stable Gain) when K < 1: G_max = |S21|/|S12|
MSG = np.abs(S21) / np.abs(S12)
print(f"Maximum Stable Gain (MSG) = |S21|/|S12| = {MSG:.2f} ({20*np.log10(MSG):.1f} dB)")

# When unconditionally stable (K > 1):
# G_max = |S21|/|S12| * (K - √(K² - 1))
G_max_stable = MSG * (K - np.sqrt(K**2 - 1))
print(f"Maximum Gain (unconditionally stable): G_max = {G_max_stable:.3f} ({20*np.log10(G_max_stable):.1f} dB)")

# Unilateral gain (when S12 ≈ 0): G_u = |S21|² / (1 - |S11|²)
G_u = np.abs(S21)**2 / (1 - np.abs(S11)**2)
print(f"Unilateral power gain G_u = {G_u:.2f} ({10*np.log10(G_u):.1f} dB)")

# ============================================================================
# Example 10.4: Input/Output Matching
# ============================================================================
print("\n" + "=" * 60)
print("Example 10.4: Input/Output Matching Networks")
print("=" * 60)

# For maximum gain design, conjugate match
# Γ_in = S11 + S12*Γ_L/(1 - S22*Γ_L)
# Want Γ_in = Γ_S* (conjugate for max transfer)
# Similar for output

# When unconditionally stable, optimal source reflection:
# Γ_S_opt = (B1 ± √(B1² - 4|C1|²)) / (2*C1)
B1 = 1 + np.abs(S11)**2 - np.abs(S22)**2 - np.abs(D)**2
C1 = S11 - D * np.conj(S22)

if K > 1:
    B1_val = np.real(B1)
    C1_val = C1
    discriminant = B1_val**2 - 4*np.abs(C1_val)**2
    if discriminant >= 0:
        gamma_s_mag = (B1_val - np.sqrt(discriminant)) / (2 * np.abs(C1_val))
        gamma_s_opt = gamma_s_mag * np.exp(1j * np.angle(C1_val))
        print(f"Optimal source reflection Γ_S_opt ≈ {gamma_s_opt:.4f}")
        print(f"  |Γ_S_opt| = {np.abs(gamma_s_opt):.4f}")

# ============================================================================
# Example 10.5: Low-Noise Amplifier Design
# ============================================================================
print("\n" + "=" * 60)
print("Example 10.5: Low-Noise Amplifier Design")
print("=" * 60)

# LNA design parameters
F_min_dB = 0.5     # dB (minimum noise figure)
Rn = 5.0           # ohm (noise resistance)
Gamma_opt = 0.5 * np.exp(1j * np.radians(-30))  # optimal source reflection

print(f"LNA design targets:")
print(f"  F_min = {F_min_dB} dB")
print(f"  R_n = {Rn} Ω")
print(f"  Γ_opt = {Gamma_opt:.4f} (|Γ_opt| = {np.abs(Gamma_opt):.4f})")
print(f"  Design approach: match to Γ_opt for minimum noise")
print(f"  Trade-off: gain vs noise figure")

# Noise circles: F = F_min + 4Rn|Y_opt|²/|1+Y_opt|² * |Y_S - Y_opt|² / |Y_S + Y_0|²
# Simplified: show trade-off between noise and source match

# ============================================================================
# Example 10.6: Power Amplifier Design
# ============================================================================
print("\n" + "=" * 60)
print("Example 10.6: Power Amplifier Design")
print("=" * 60)

# Power amplifier at 10 GHz
P_out_dBm = 30.0    # 1 Watt output
V_DS = 10.0         # drain-source voltage (V)
I_DS = 0.5          # drain current (A)
Efficiency = 50      # percent

print(f"Power amplifier design (10 GHz):")
print(f"  Output power: {P_out_dBm} dBm (1 W)")
print(f"  Drain voltage: V_DS = {V_DS} V")
print(f"  Drain current: I_DS = {I_DS} A")
print(f"  Efficiency: {Efficiency}%")
print(f"  PAE = (P_out - P_in) / P_DC ≈ {Efficiency}%")

# Load-pull: find optimal load for maximum power
# For Class A: η_max = 50%
# For Class B: η_max = 78.5%
print(f"\nTheoretical maximum efficiency:")
print(f"  Class A: 50%")
print(f"  Class B: 78.5% (with harmonic tuning)")
print(f"  Class C: < 78.5% (conduction angle < 180°)")

# ============================================================================
# Figure: Amplifier Design Parameters
# ============================================================================
fig = plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.4, wspace=0.35)

# 1. Stability circles on Smith chart
ax1 = fig.add_subplot(gs[0, 0])
# Draw Smith chart
circle_unit = plt.Circle((0, 0), 1, fill=False, color='black', lw=1.5)
ax1.add_patch(circle_unit)
# Constant resistance circles
for r in [0.5, 1.0]:
    center = r / (1 + r)
    radius = 1 / (1 + r)
    ax1.add_patch(plt.Circle((center, 0), radius, fill=False, color='steelblue', lw=0.8, alpha=0.5))

# Input stability circle
# Center: (S11 - D*S22*)*
# Radius: ...
# (Simplified visualization)
ax1.add_patch(plt.Circle((0.5, 0.1), 0.4, fill=False, color='red', lw=2, ls='--'))
ax1.add_patch(plt.Circle((0.7, -0.2), 0.35, fill=False, color='blue', lw=2, ls='--'))
ax1.set_aspect('equal')
ax1.set_xlim(-1.3, 1.3)
ax1.set_ylim(-1.3, 1.3)
ax1.axis('off')
ax1.set_title('Stability Circles on Smith Chart', fontsize=12)
ax1.text(0.5, 0.6, 'Input\nStability', fontsize=9, ha='center', color='red')
ax1.text(0.8, -0.5, 'Output\nStability', fontsize=9, ha='center', color='blue')

# 2. Gain circles
ax2 = fig.add_subplot(gs[0, 1])
# Power gain circles for different gain levels
circle_unit2 = plt.Circle((0, 0), 1, fill=False, color='black', lw=1.5)
ax2.add_patch(circle_unit2)

for g_dB in [5, 10, 15, 20]:
    # Simplified: circles of different radii
    r_circle = 1 - 10**(-g_dB/20)
    ax2.add_patch(plt.Circle((0.2, 0.2), r_circle * 0.5, fill=False, 
                             color='steelblue', lw=1.5, alpha=0.7))
ax2.set_aspect('equal')
ax2.set_xlim(-1.3, 1.3)
ax2.set_ylim(-1.3, 1.3)
ax2.axis('off')
ax2.set_title('Gain Circles (G = constant)', fontsize=12)

# 3. MSG vs frequency
ax3 = fig.add_subplot(gs[0, 2])
f_amp = np.linspace(2, 18, 300)
S21_mag_sim = 3 * np.exp(-((f_amp - 10)/5)**2)  # gain peak at 10 GHz
S12_mag_sim = 0.05 * np.ones_like(f_amp)
MSG_sim = S21_mag_sim / S12_mag_sim
ax3.semilogy(f_amp, MSG_sim, 'b-', lw=2)
ax3.axhline(y=1, color='r', ls='--', alpha=0.7, label='MSG=0 dB (stability boundary)')
ax3.set_xlabel('f (GHz)', fontsize=11)
ax3.set_ylabel('MSG (linear)', fontsize=11)
ax3.set_title('Maximum Stable Gain vs Frequency', fontsize=12)
ax3.legend()
ax3.grid(True, alpha=0.3)
ax3.set_xlim(2, 18)

# 4. Constant gain contours
ax4 = fig.add_subplot(gs[1, 0])
# Draw constant gain circles (simplified)
circle_unit4 = plt.Circle((0, 0), 1, fill=False, color='black', lw=1.5)
ax4.add_patch(circle_unit4)

for i, (gain_db, center) in enumerate([(20, (0.3, 0.2)), (15, (0.2, 0.15)), (10, (0.1, 0.1))]):
    r_g = 10**(-gain_db/20) * 0.5
    ax4.add_patch(plt.Circle(center, r_g, fill=False, color='green', lw=2, alpha=0.7))

ax4.set_aspect('equal')
ax4.set_xlim(-1.3, 1.3)
ax4.set_ylim(-1.3, 1.3)
ax4.axis('off')
ax4.set_title('Constant Gain Circles', fontsize=12)
ax4.text(0.5, 0.5, 'G=20 dB', fontsize=9, color='green')

# 5. LNA noise circles
ax5 = fig.add_subplot(gs[1, 1])
# Draw Smith chart
circle_unit5 = plt.Circle((0, 0), 1, fill=False, color='black', lw=1.5)
ax5.add_patch(circle_unit5)

# Noise circles: centered near Γ_opt
ax5.add_patch(plt.Circle((0.3, -0.2), 0.1, fill=False, color='red', lw=2))
ax5.add_patch(plt.Circle((0.3, -0.2), 0.2, fill=False, color='orange', lw=2))
ax5.add_patch(plt.Circle((0.3, -0.2), 0.3, fill=False, color='yellow', lw=2))
ax5.plot(0.3, -0.2, 'r*', markersize=12)
ax5.set_aspect('equal')
ax5.set_xlim(-1.3, 1.3)
ax5.set_ylim(-1.3, 1.3)
ax5.axis('off')
ax5.set_title('Noise Circles (F = 1, 2, 3 dB from F_min)', fontsize=12)
ax5.text(0.6, 0.4, r'$\Gamma_{opt}$', fontsize=10, color='red')

# 6. Gain vs input power (compression)
ax6 = fig.add_subplot(gs[1, 2])
P_in_amp = np.linspace(-30, 5, 200)
Gain_init = 20.0
P1dB_amp = -5.0

Gain_vs_P = np.zeros_like(P_in_amp)
for i, P in enumerate(P_in_amp):
    if P < P1dB_amp:
        Gain_vs_P[i] = Gain_init
    else:
        comp = (P - P1dB_amp) * 0.5
        Gain_vs_P[i] = max(Gain_init - comp - 3, Gain_init - 10)

ax6.plot(P_in_amp, Gain_vs_P, 'b-', lw=2)
ax6.axhline(y=Gain_init - 1, color='r', ls='--', alpha=0.7, label='G0-1 dB')
ax6.axvline(x=P1dB_amp, color='gray', ls=':', alpha=0.7, label=f'P1dB = {P1dB_amp} dBm')
ax6.set_xlabel(r'$P_{in}$ (dBm)', fontsize=11)
ax6.set_ylabel('Gain (dB)', fontsize=11)
ax6.set_title('Amplifier Gain Compression', fontsize=12)
ax6.legend()
ax6.grid(True, alpha=0.3)
ax6.set_xlim(-30, 5)
ax6.set_ylim(10, 21)

plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wbgc/code/wbgc_ch10_amplifiers.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("\nSaved: wbgc_ch10_amplifiers.png")

print("\n✅ Chapter 10 examples completed.")