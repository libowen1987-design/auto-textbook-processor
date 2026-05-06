#!/usr/bin/env python3
"""
简明微波 (梁昌洪) - 第5章: S参数与网络分析
S-Parameters and Network Analysis - Chapter 5

Topics covered:
- Scattering matrix fundamentals (5.1)
- S-parameter properties and conversions (5.2)
- Network analysis (5.3)
- Mason's rule / signal flow graphs (5.4)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ============================================================================
# Example 5.1: S-Parameter Definition and Interpretation
# ============================================================================
print("=" * 60)
print("Example 5.1: S-Parameter Fundamentals")
print("=" * 60)

# Two-port network example: ideal matched attenuator
# S11 = 0 (input is matched), S22 = 0 (output is matched)
# S21 = √(1 - Γ²) for lossless case; for lossy: S21 = √(10^(-IL/10)) where IL = insertion loss in dB

# Case: 10 dB matched attenuator
IL_dB = 10.0
S21_mag = 10**(-IL_dB/20)  # voltage gain magnitude
print(f"10 dB matched attenuator:")
print(f"  S11 = 0 (input matched)")
print(f"  S22 = 0 (output matched)")
print(f"  |S21| = 10^(-10/20) = {S21_mag:.4f}")
print(f"  |S12| = {S21_mag:.4f} (reciprocal)")

# S-parameter matrix for this network
S_atten = np.array([[0, S21_mag], [S21_mag, 0]], dtype=complex)
print(f"\nS = [[{S_atten[0,0]:.4f}, {S_atten[0,1]:.4f}],")
print(f"     [{S_atten[1,0]:.4f}, {S_atten[1,1]:.4f}]]")

# Verify reciprocity: S12 = S21
print(f"\nReciprocity check: S12 = S21? {np.isclose(S_atten[1,0], S_atten[0,1])}")

# ============================================================================
# Example 5.2: S-Parameter to Z-Parameter Conversion
# ============================================================================
print("\n" + "=" * 60)
print("Example 5.2: S-Parameter Conversions")
print("=" * 60)

def S_to_Z(S, Z_0=50):
    """Convert S-parameters to Z-parameters"""
    n = S.shape[0]
    I = np.eye(n)
    Z = Z_0 * (I - S) @ np.linalg.inv(I + S)
    return Z

def Z_to_S(Z, Z_0=50):
    """Convert Z-parameters to S-parameters"""
    n = Z.shape[0]
    I = np.eye(n)
    S = np.linalg.inv(Z/Z_0 + I) @ (Z/Z_0 - I)
    return S

# Example: S-parameters of a series impedance
# Z = j*100 ohm (inductor at 10 GHz)
# S11 = S22 = Z/(Z + 2*Z0)
# S21 = S12 = 2*Z0/(Z + 2*Z0)
Z_series = 1j * 100  # ohm
S_series = np.array([[Z_series/(Z_series + 2*50), 2*50/(Z_series + 2*50)],
                     [2*50/(Z_series + 2*50), Z_series/(Z_series + 2*50)]], dtype=complex)
print(f"Series inductor Z = j100 Ω:")
print(f"  S = [[{S_series[0,0]:.4f}, {S_series[0,1]:.4f}],")
print(f"       [{S_series[1,0]:.4f}, {S_series[1,1]:.4f}]]")

# Convert back to Z
Z_back = S_to_Z(S_series)
print(f"\nZ from S:")
print(f"  Z = [[{Z_back[0,0]:.3f}, {Z_back[0,1]:.3f}],")
print(f"       [{Z_back[1,0]:.3f}, {Z_back[1,1]:.3f}]]")

# ============================================================================
# Example 5.3: Two-Port Network Cascade (ABCD Matrix)
# ============================================================================
print("\n" + "=" * 60)
print("Example 5.3: Network Cascade with ABCD Parameters")
print("=" * 60)

def S_to_ABCD(S, Z_0=50):
    """Convert S-parameters to ABCD parameters"""
    A = ((1 + S[0,0]) * (1 - S[1,1]) + S[0,1] * S[1,0]) / (2 * S[0,1])
    B = ((1 + S[0,0]) * (1 + S[1,1]) - S[0,1] * S[1,0]) / (2 * S[0,1]) * Z_0
    C = ((1 - S[0,0]) * (1 - S[1,1]) - S[0,1] * S[1,0]) / (2 * S[0,1]) / Z_0
    D = ((1 - S[0,0]) * (1 + S[1,1]) + S[0,1] * S[1,0]) / (2 * S[0,1])
    return np.array([[A, B], [C, D]], dtype=complex)

def ABCD_to_S(ABCD, Z_0=50):
    """Convert ABCD parameters to S-parameters"""
    A, B, C, D = ABCD[0,0], ABCD[0,1], ABCD[1,0], ABCD[1,1]
    denom = A + B/Z_0 + C*Z_0 + D
    S11 = (A + B/Z_0 - C*Z_0 - D) / denom
    S12 = 2 * (A*D - B*C) / denom
    S21 = 2 / denom
    S22 = (-A + B/Z_0 - C*Z_0 + D) / denom
    return np.array([[S11, S12], [S21, S22]], dtype=complex)

# Example: cascade of two 10 dB attenuators
S_att = np.array([[0, S21_mag], [S21_mag, 0]], dtype=complex)
ABCD1 = S_to_ABCD(S_att, 50)
ABCD2 = S_to_ABCD(S_att, 50)

# Cascade: ABCD_total = ABCD1 @ ABCD2
ABCD_total = ABCD1 @ ABCD2
S_total = ABCD_to_S(ABCD_total, 50)

print(f"Cascade of two 10 dB attenuators:")
print(f"  |S21| total = {np.abs(S_total[1,0]):.4f}")
print(f"  Combined loss = {-20*np.log10(np.abs(S_total[1,0])):.2f} dB (expected 20 dB)")

# ============================================================================
# Example 5.4: Return Loss and Insertion Loss
# ============================================================================
print("\n" + "=" * 60)
print("Example 5.4: Return Loss and Insertion Loss")
print("=" * 60)

# Measured S-parameters of a mismatched network
S_meas = np.array([[0.3*np.exp(1j*np.radians(140)), 0.9*np.exp(1j*np.radians(-20))],
                   [0.85*np.exp(1j*np.radians(-15)), 0.25*np.exp(1j*np.radians(180))]], dtype=complex)

print("Measured S-parameters:")
for i in range(2):
    for j in range(2):
        mag = np.abs(S_meas[i,j])
        phase = np.angle(S_meas[i,j]) * 180/np.pi
        print(f"  S{i+1}{j+1} = {mag:.4f} ∠ {phase:.1f}°")

# Return loss
RL = -20 * np.log10(np.abs(S_meas[0,0]))
print(f"\nInput return loss (S11): {RL:.2f} dB")

# Insertion loss
IL = -20 * np.log10(np.abs(S_meas[1,0]))
print(f"Insertion loss (S21): {IL:.2f} dB")

# ============================================================================
# Example 5.5: Unbalanced to Balanced Port (Balun Example)
# ============================================================================
print("\n" + "=" * 60)
print("Example 5.5: Three-Port Network (Unbalanced to Balanced)")
print("=" * 60)

# Simple balun example: ideal 3-port with S = [[0, 1/√2, 1/√2], ...]
# This is a symmetric 3-port (E-plane or H-plane T-junction)
# For a lossless 3-port, S-matrix must be unitary

# T-junction (E-plane) - simplified model
# Port 1: input (unbalanced), Port 2 & 3: outputs (balanced)
# S11 = 0 (matched), S22 = S33 = 0, S12 = S13 = 1/√2 (equal split, in-phase)
# S21 = S31 = 1/√2

S_balun = np.array([[0, 0.7071, 0.7071],
                    [0.7071, 0, 0],
                    [0.7071, 0, 0]], dtype=complex)

print("3-port balun S-matrix (theoretical):")
print(f"  S = {S_balun}")

# Check unitary: S^dagger @ S = I?
S_dag = np.conj(S_balun).T
unitary_check = S_dag @ S_balun
print(f"\nUnitarity check (S†S should be identity):")
print(f"  Max deviation: {np.max(np.abs(unitary_check - np.eye(3))):.6f}")

# ============================================================================
# Figure: S-Parameter Visualization
# ============================================================================
fig = plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.4, wspace=0.35)

# 1. S11 on Smith chart
ax1 = fig.add_subplot(gs[0, 0])
theta_s11 = np.linspace(0, 2*np.pi, 200)
circle_unit = plt.Circle((0, 0), 1, fill=False, color='black', lw=1.5)
ax1.add_patch(circle_unit)
ax1.set_aspect('equal')
ax1.set_xlim(-1.3, 1.3)
ax1.set_ylim(-1.3, 1.3)
ax1.axis('off')
ax1.set_title('S11 on Smith Chart', fontsize=12)

# Plot S11 for our example
for Z_L in [40-1j*30, 100, 10+1j*50, 0]:  # various loads
    S11_val = (Z_L - 50) / (Z_L + 50)
    ax1.plot(np.real(S11_val), np.imag(S11_val), 'o', markersize=8)
ax1.text(0.2, 0.8, 'Various\nLoads', fontsize=10)

# 2. Magnitude of S21 and S11 vs frequency (simulated)
ax2 = fig.add_subplot(gs[0, 1])
f_norm = np.linspace(0.1, 2.0, 300)
# Simple model: bandpass behavior
S21_mag_sim = np.abs(1 / (1 + 1j*(f_norm - 1)*3))
S11_mag_sim = np.abs(1 - S21_mag_sim**2)

ax2.plot(f_norm, 20*np.log10(S21_mag_sim), 'b-', lw=2, label=r'$|S_{21}|$ (transmission)')
ax2.plot(f_norm, 20*np.log10(S11_mag_sim + 1e-10), 'r--', lw=2, label=r'$|S_{11}|$ (reflection)')
ax2.set_xlabel(r'$f/f_0$', fontsize=11)
ax2.set_ylabel(r'$|S|$ (dB)', fontsize=11)
ax2.set_title('Bandpass Filter Response (Simulated)', fontsize=12)
ax2.legend()
ax2.grid(True, alpha=0.3)
ax2.set_ylim(-40, 5)

# 3. Network cascade visualization
ax3 = fig.add_subplot(gs[0, 2])
# Draw network blocks
for i, (label, S_ex) in enumerate([('Block 1\n10dB atten', S_atten), 
                                    ('Block 2\n10dB atten', S_atten)]):
    rect = plt.Rectangle((i*2, 0), 1.5, 1, fill=True, facecolor='lightblue', edgecolor='black')
    ax3.add_patch(rect)
    ax3.text(i*2 + 0.75, 0.5, label, ha='center', va='center', fontsize=9)
    
# Input and output arrows
ax3.annotate('', xy=(-0.5, 0.5), xytext=(-1.5, 0.5),
             arrowprops=dict(arrowstyle='->', color='green', lw=2))
ax3.text(-1, 0.7, 'Port 1', fontsize=10)
ax3.annotate('', xy=(4, 0.5), xytext=(3.5, 0.5),
             arrowprops=dict(arrowstyle='->', color='green', lw=2))
ax3.text(3.7, 0.7, 'Port 2', fontsize=10)

ax3.set_xlim(-2, 4.5)
ax3.set_ylim(-0.5, 1.5)
ax3.axis('off')
ax3.set_title('Cascaded Two-Port Network', fontsize=12)

# 4. Return loss vs VSWR
ax4 = fig.add_subplot(gs[1, 0])
RL_range = np.linspace(0.1, 30, 200)
VSWR_from_RL = (10**(RL_range/20) + 1) / (10**(RL_range/20) - 1)
ax4.semilogx(RL_range, VSWR_from_RL, 'b-', lw=2)
ax4.set_xlabel('Return Loss (dB)', fontsize=11)
ax4.set_ylabel('VSWR', fontsize=11)
ax4.set_title('VSWR from Return Loss', fontsize=12)
ax4.grid(True, alpha=0.3)
ax4.axhline(y=2, color='r', ls='--', alpha=0.7, label='VSWR=2')
ax4.axhline(y=1.5, color='g', ls='--', alpha=0.7, label='VSWR=1.5')
ax4.legend()

# 5. Insertion loss vs frequency
ax5 = fig.add_subplot(gs[1, 1])
f_il = np.linspace(0.5, 1.5, 300)
IL_sim = -10 * np.log10(1 / (1 + ((f_il - 1)/0.1)**4) + 1e-10)
ax5.plot(f_il, IL_sim, 'b-', lw=2)
ax5.set_xlabel(r'$f/f_0$', fontsize=11)
ax5.set_ylabel('Insertion Loss (dB)', fontsize=11)
ax5.set_title('Low-Pass Filter Response (Simulated)', fontsize=12)
ax5.grid(True, alpha=0.3)
ax5.set_ylim(0, 30)

# 6. S-matrix heatmap
ax6 = fig.add_subplot(gs[1, 2])
S_display = np.array([[0.3, 0.9], [0.85, 0.25]])
im = ax6.imshow(np.abs(S_display), cmap='viridis', aspect='auto', vmin=0, vmax=1)
ax6.set_xticks([0, 1])
ax6.set_yticks([0, 1])
ax6.set_xticklabels(['Port 1', 'Port 2'])
ax6.set_yticklabels(['Port 1', 'Port 2'])
ax6.set_title(r'$|S|$ Magnitude (dB-scale example)', fontsize=12)
plt.colorbar(im, ax=ax6, shrink=0.8)
for i in range(2):
    for j in range(2):
        ax6.text(j, i, f'{np.abs(S_display[i,j]):.2f}', ha='center', va='center', 
                 color='white', fontsize=12, fontweight='bold')

plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wbgc/code/wbgc_ch5_sparameters.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("\nSaved: wbgc_ch5_sparameters.png")

print("\n✅ Chapter 5 examples completed.")