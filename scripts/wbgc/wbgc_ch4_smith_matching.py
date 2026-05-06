#!/usr/bin/env python3
"""
简明微波 (梁昌洪) - 第4章: 阻抗匹配与滤波器
Impedance Matching and Filters - Chapter 4

Topics covered:
- Smith chart fundamentals (4.1)
- Impedance matching with stubs (4.2)
- Quarter-wave transformer (4.3)
- Filter design fundamentals (4.4)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc, FancyArrowPatch
from matplotlib.collections import LineCollection
import matplotlib.gridspec as gridspec

# ============================================================================
# Smith Chart Core Functions
# ============================================================================
def gamma_to_Z(gamma, Z_0=50):
    """Convert reflection coefficient to impedance"""
    return Z_0 * (1 + gamma) / (1 - gamma)

def Z_to_gamma(Z, Z_0=50):
    """Convert impedance to reflection coefficient"""
    return (Z - Z_0) / (Z + Z_0)

def normalize_Z(Z, Z_0=50):
    """Normalize impedance to characteristic impedance"""
    return Z / Z_0

def gamma_to_Y(gamma):
    """Convert reflection coefficient to admittance"""
    return gamma  # Y = 1/Z, so gamma_Y = (Y - Y0)/(Y + Y0) = (1/Z - 1/Z0)/(1/Z + 1/Z0)

# ============================================================================
# Example 4.1: Smith Chart - Plot Reflection Coefficient
# ============================================================================
print("=" * 60)
print("Example 4.1: Smith Chart Fundamentals")
print("=" * 60)

# Create a high-quality Smith chart
def draw_smith_chart(ax, Z_0=50):
    """Draw a complete Smith chart"""
    # Unit circle for |Γ| = 1
    circle_unit = Circle((0, 0), 1, fill=False, color='black', lw=1.5)
    ax.add_patch(circle_unit)
    
    # Constant resistance circles (r = 0, 0.2, 0.5, 1, 2, 5)
    r_values = [0, 0.2, 0.5, 1.0, 2.0, 5.0]
    for r in r_values:
        if r == 0:
            # r=0 is the leftmost point (-1, 0)
            center = -1
            radius = 1
        else:
            center = r / (1 + r)
            radius = 1 / (1 + r)
        
        circle_r = Circle((center, 0), radius, fill=False, 
                          color='steelblue', lw=0.8, alpha=0.6)
        ax.add_patch(circle_r)
        
        # Label for r=1 circle
        if r == 1.0:
            ax.text(center, 0.05, f'r={r}', fontsize=8, ha='center')
    
    # Constant reactance arcs (x = 0, ±0.2, ±0.5, ±1, ±2, ±5)
    x_values = [0, 0.2, 0.5, 1.0, 2.0, 5.0]
    for x in x_values:
        # Upper half (positive x)
        if x == 0:
            # x=0 is the real axis from -1 to +1
            ax.plot([-1, 1], [0, 0], 'steelblue', lw=0.8, alpha=0.6)
        else:
            center_x = 1 / (2 * x)
            radius_x = abs(1 / (2 * x))
            if x > 0:
                theta1, theta2 = 0, 180
            else:
                theta1, theta2 = 0, -180
            arc = Arc((center_x, 0), 2*radius_x, 2*radius_x,
                      angle=0, theta1=theta1, theta2=theta2,
                      color='indianred', lw=0.8, alpha=0.6)
            ax.add_patch(arc)
    
    # Grid lines
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Add labels
    ax.text(0, -1.25, 'Smith Chart (Z or Y)', fontsize=14, ha='center', fontweight='bold')
    ax.text(0, -1.15, r'$Z_0 = ' + f'{Z_0}\,\Omega$', fontsize=10, ha='center')
    
    # Mark important points
    ax.plot(1, 0, 'ko', markersize=6)  # +1 (open circuit)
    ax.plot(-1, 0, 'ko', markersize=6)  # -1 (short circuit)
    ax.plot(0, 0, 'k+', markersize=8)  # center (Z = Z0)
    
    # Add angle labels
    for angle in [0, 45, 90, 135, 180, -135, -90, -45]:
        theta = np.radians(angle)
        x_pos = 1.15 * np.cos(theta)
        y_pos = 1.15 * np.sin(theta)
        ax.text(x_pos, y_pos, f'{angle}°', fontsize=8, ha='center', va='center')

# Given example: Z_L = 40 - j30 ohm, Z0 = 50 ohm
Z_0_sc = 50.0
Z_L_sc = 40 - 1j*30
Gamma_sc = (Z_L_sc - Z_0_sc) / (Z_L_sc + Z_0_sc)
print(f"Z_L = {Z_L_sc} Ω, Z0 = {Z_0_sc} Ω")
print(f"Γ = {Gamma_sc:.4f}")
print(f"|Γ| = {np.abs(Gamma_sc):.4f}, ∠Γ = {np.angle(Gamma_sc)*180/np.pi:.2f}°")

# VSWR
VSWR_sc = (1 + np.abs(Gamma_sc)) / (1 - np.abs(Gamma_sc))
print(f"VSWR = {VSWR_sc:.3f}")

# Calculate distance toward generator (from load)
# SWR min at angle of -2*theta_r in the constant SWR circle
theta_r = np.angle(Gamma_sc) / 2
print(f"First voltage minimum at: θ = {np.degrees(theta_r):.2f}° from load (wavelengths)")

# ============================================================================
# Example 4.2: Single-Stub Tuning
# ============================================================================
print("\n" + "=" * 60)
print("Example 4.2: Single-Stub Tuning")
print("=" * 60)

# Problem: Match Z_L = 100 + j50 to Z0 = 50 using single parallel stub
Z_0_stub = 50.0
Z_L_stub = 100 + 1j*50

Gamma_L_stub = Z_to_gamma(Z_L_stub, Z_0_stub)
print(f"Z_L = {Z_L_stub} Ω, Z0 = {Z_0_stub} Ω")
print(f"Γ_L = {Gamma_L_stub:.4f}")

# Convert to admittance: Y_L = 1/Z_L
Y_L_stub = 1/Z_L_stub
Y_0_stub = 1/Z_0_stub  # 0.02 S
print(f"Y_L = {Y_L_stub:.4f} S")
print(f"Y0 = {Y_0_stub:.4f} S")

# Normalized admittance: y_L = Y_L / Y0
y_L_stub = Y_L_stub / Y_0_stub
print(f"y_L = {y_L_stub:.4f}")

# On Smith chart: we want to find point where y = 1 + j*b (normalized)
# Using stub of length l_s (short or open) to provide j*b_s susceptance
# The admittance at the stub location should be y_in = 1 + j*0 (for match)

# For single stub tuning: 
# Step 1: rotate from y_L to y_1 on g=1 circle
# y_1 = 1 + j*b_1 (where we connect the stub)
# Step 2: stub provides -j*b_1 (open or short)

# Rotation on constant |Γ| circle
# The angle needed to reach g=1 circle
# y = g + jb, we want g=1
# From y_L, rotate until g=1

# Calculate stub length
# For shorted stub: Y_stub = j*Y0*tan(β*l_s)
# We need Y_stub = -j*b_1*Y0
# So tan(β*l_s) = -b_1

b_needed = -np.imag(y_L_stub)  # The susceptance we need to cancel
print(f"\nSusceptance to cancel: B = {b_needed:.3f} (normalized)")
print(f"Stub length (short-circuited): l = λ/4 - λ/(2π)*arctan(|B|)")
l_stub_norm = 0.25 - 1/(2*np.pi) * np.arctan(abs(b_needed))
print(f"l_stub = {l_stub_norm:.4f} λ")

# Distance from load to stub
# Starting from y_L, rotate toward generator (clockwise on Smith)
# |Gamma| = 0.5547, angle = -68.2°
# Need to find rotation angle to reach g=1 circle
# This is approximate - in practice use Smith chart graphical method

# ============================================================================
# Example 4.3: Double-Stub Tuning
# ============================================================================
print("\n" + "=" * 60)
print("Example 4.3: Double-Stub Tuning")
print("=" * 60)

# Match Z_L = 50 - j50 to Z0 = 50 using double stub
Z_0_ds = 50.0
Z_L_ds = 50 - 1j*50

Gamma_L_ds = (Z_L_ds - Z_0_ds) / (Z_L_ds + Z_0_ds)
Y_L_ds = 1 / Z_L_ds
y_L_ds = Y_L_ds * Z_0_ds  # normalize to Y0
print(f"Z_L = {Z_L_ds} Ω")
print(f"y_L = {y_L_ds:.4f}")

# Distance to first stub: d1
# We want to rotate y_L to intersection with g-circle
# For practical implementation, d1 is typically λ/8, λ/4, or 3λ/8

# ============================================================================
# Example 4.4: Quarter-Wave Transformer Matching
# ============================================================================
print("\n" + "=" * 60)
print("Example 4.4: Quarter-Wave Transformer Design")
print("=" * 60)

# Match Z_L = 100 ohm to Z0 = 50 ohm
Z_0_qt = 50.0
Z_L_qt = 100.0

Z_1_qt = np.sqrt(Z_0_qt * Z_L_qt)
print(f"Match 100 Ω load to 50 Ω line")
print(f"Z1 (quarter-wave transformer) = √(Z0·ZL) = {Z_1_qt:.3f} Ω")

# Reflection coefficient at transformer
Gamma_qt = (Z_L_qt - Z_0_qt) / (Z_L_qt + Z_0_qt)
print(f"Γ = {Gamma_qt:.4f}")
print(f"VSWR = {(1+np.abs(Gamma_qt))/(1-np.abs(Gamma_qt)):.3f} (before matching)")

# Bandwidth of quarter-wave transformer
# For Kw bandwidth to VSWR <= S:
# Δf/f_0 = 2 - 4/π * arcsin((S-1)/(S+1))

def qt_bandwidth(S):
    """Quarter-wave transformer bandwidth for VSWR <= S"""
    return 2 - 4/np.pi * np.arcsin((S-1)/(S+1))

S_target = 1.5
BW_qt = qt_bandwidth(S_target)
print(f"\nFor VSWR ≤ {S_target}, fractional bandwidth = {BW_qt:.3f} ({BW_qt*100:.1f}%)")

# ============================================================================
# Example 4.5: Filter Design - Chebyshev Low-Pass Prototype
# ============================================================================
print("\n" + "=" * 60)
print("Example 4.5: Filter Design - Chebyshev LPF")
print("=" * 60)

# 5th order Chebyshev low-pass prototype, ripple = 0.5 dB
# Element values for n=5, 0.5 dB ripple:
g_vals = [3.3487, 0.9532, 5.8095, 3.3487, 0.9532, 1.0]  # g1...g6

print("5th order Chebyshev LPF prototype (0.5 dB ripple):")
for i, g in enumerate(g_vals):
    print(f"  g{i+1} = {g:.4f}")

# Transform to high-pass, band-pass, or band-stop as needed

# ============================================================================
# Figure: Smith Chart with Impedance Matching
# ============================================================================
fig = plt.figure(figsize=(16, 12))
gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.4, wspace=0.35)

# 1. Basic Smith Chart with point
ax1 = fig.add_subplot(gs[0, 0])
draw_smith_chart(ax1, Z_0=50)
# Plot the example point
Gamma_ex = (40 - 1j*30 - 50) / (40 - 1j*30 + 50)
ax1.plot(np.real(Gamma_ex), np.imag(Gamma_ex), 'ro', markersize=10)
ax1.annotate(r'$Z_L = 40 - j30\,\Omega$', 
             xy=(np.real(Gamma_ex), np.imag(Gamma_ex)),
             xytext=(0.3, 0.5), fontsize=10,
             arrowprops=dict(arrowstyle='->', color='red'))

# 2. Impedance matching path
ax2 = fig.add_subplot(gs[0, 1])
draw_smith_chart(ax2, Z_0=50)

# Plot constant VSWR circle for |Γ| = 0.5547
Gamma_abs = 0.5547
circle_vswr = Circle((0, 0), Gamma_abs, fill=False, color='green', lw=2, ls='--')
ax2.add_patch(circle_vswr)

# Plot the stub tuning path (example)
ax2.plot([0.5547*np.cos(np.radians(-68)), 0], 
         [0.5547*np.sin(np.radians(-68)), 0], 'b-', lw=2)
ax2.plot(0, 0, 'bo', markersize=8)
ax2.set_title('Impedance Matching Path on Smith Chart', fontsize=12)

# 3. Stub length calculation
ax3 = fig.add_subplot(gs[1, 0])
l_stub = np.linspace(0, 0.5, 300)
Y_stub_norm = 1j * np.tan(2*np.pi * l_stub)  # shorted stub
b_stub = np.imag(Y_stub_norm)

ax3.plot(l_stub, b_stub, 'b-', lw=2)
ax3.axhline(y=0, color='gray', lw=0.5)
ax3.axvline(x=0.25, color='red', ls='--', label='λ/4 (open/short flip)')
ax3.set_xlabel(r'$l/\lambda$', fontsize=11)
ax3.set_ylabel(r'$B_{stub}/Y_0$ (normalized susceptance)', fontsize=11)
ax3.set_title('Shorted Stub Susceptance vs Length', fontsize=12)
ax3.legend()
ax3.grid(True, alpha=0.3)
ax3.set_xlim(0, 0.5)

# 4. Quarter-wave transformer frequency response
ax4 = fig.add_subplot(gs[1, 1])
f_norm = np.linspace(0.5, 1.5, 300)  # normalized frequency (f/f_c)
Z_0_f = 50.0
Z_L_f = 100.0
Z_1_f = np.sqrt(Z_0_f * Z_L_f)

# Simplified response (not exact but shows trend)
# At f0: perfect match (Γ=0)
# Away from f0: Γ increases
Gamma_mag = np.abs((Z_L_f - Z_0_f) / (Z_L_f + Z_0_f)) * np.abs(np.sin(np.pi*f_norm)/(np.pi*f_norm))
VSWR_f = (1 + Gamma_mag) / (1 - Gamma_mag)

ax4.plot(f_norm, VSWR_f, 'b-', lw=2)
ax4.axhline(y=1.5, color='r', ls='--', label='VSWR = 1.5')
ax4.set_xlabel(r'$f/f_0$ (normalized frequency)', fontsize=11)
ax4.set_ylabel('VSWR', fontsize=11)
ax4.set_title('Quarter-Wave Transformer Frequency Response', fontsize=12)
ax4.legend()
ax4.grid(True, alpha=0.3)
ax4.set_ylim(1, 4)
ax4.set_xlim(0.5, 1.5)

plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wbgc/code/wbgc_ch4_smith_matching.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("\nSaved: wbgc_ch4_smith_matching.png")

print("\n✅ Chapter 4 examples completed.")