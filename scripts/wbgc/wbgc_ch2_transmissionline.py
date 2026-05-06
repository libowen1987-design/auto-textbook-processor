#!/usr/bin/env python3
"""
简明微波 (梁昌洪) - 第2章: 传输线理论基础
Transmission Line Theory - Chapter 2

Topics covered:
- Telegraph equations (2.1)
- Wave equations and propagation (2.1.1-2.1.2)
- Terminated transmission lines (2.2)
- Quarter-wave transformer (2.3)
- Impedance matching and Smith chart (2.4)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc
from matplotlib.collections import PatchCollection

# Physical constants
c = 2.998e8        # speed of light in vacuum (m/s)
mu_0 = 4 * np.pi * 1e-7  # permeability of free space (H/m)
eps_0 = 1 / (mu_0 * c**2)  # permittivity of free space (F/m)
Z_0 = np.sqrt(mu_0 / eps_0)  # characteristic impedance of free space ~ 377 ohm

# ============================================================================
# Example 2.1: Telegraph Equations and Wave Propagation
# ============================================================================
print("=" * 60)
print("Example 2.1: Telegraph Equations")
print("=" * 60)

# Given: parallel wire transmission line with L=0.5 µH/m, C=200 pF/m
L = 0.5e-6   # H/m
C = 200e-12  # F/m

# Characteristic impedance
Z_0_line = np.sqrt(L / C)
print(f"L = {L*1e6:.1f} µH/m, C = {C*1e12:.0f} pF/m")
print(f"Z0 = sqrt(L/C) = {Z_0_line:.2f} Ω")

# Phase velocity
v_p = 1 / np.sqrt(L * C)
print(f"vp = 1/sqrt(LC) = {v_p/1e6:.2f} × 10⁶ m/s = {v_p/c*100:.1f}% of c")

# Propagation constant at frequency f=2 GHz
f = 2e9  # Hz
omega = 2 * np.pi * f
gamma = 1j * omega * np.sqrt(L * C)
beta = omega * np.sqrt(L * C)
print(f"At f = {f/1e9:.0f} GHz:")
print(f"  β = {beta:.4f} rad/m")
print(f"  λ = {2*np.pi/beta*100:.2f} cm")

# ============================================================================
# Example 2.2: Terminated Transmission Line
# ============================================================================
print("\n" + "=" * 60)
print("Example 2.2: Terminated Transmission Line")
print("=" * 60)

# A transmission line with Z0=50 ohm is terminated in ZL=100+j50 ohm
Z_0_tl = 50.0   # ohm
Z_L = 100 + 1j*50  # ohm

# Reflection coefficient
Gamma = (Z_L - Z_0_tl) / (Z_L + Z_0_tl)
print(f"Z0 = {Z_0_tl} Ω, ZL = {Z_L} Ω")
print(f"Γ = (ZL-Z0)/(ZL+Z0) = {Gamma:.4f}")
print(f"|Γ| = {np.abs(Gamma):.4f}, ∠Γ = {np.angle(Gamma)*180/np.pi:.2f}°")

# VSWR
VSWR = (1 + np.abs(Gamma)) / (1 - np.abs(Gamma))
print(f"VSWR = {VSWR:.3f}")

# Input impedance at distance d=0.1λ from load
d_lambda = 0.1  # in wavelengths
z_d = d_lambda * np.exp(1j * 2 * np.pi * (-d_lambda))
Z_in = Z_0_tl * (Z_L + 1j * Z_0_tl * np.tan(2 * np.pi * (-d_lambda))) / \
       (Z_0_tl + 1j * Z_L * np.tan(2 * np.pi * (-d_lambda)))
print(f"Zin at d=0.1λ from load: Zin = {Z_in:.3f} Ω")

# Power delivered to load
Gamma_dB = 20 * np.log10(np.abs(Gamma))
RL = -20 * np.log10(np.abs(Gamma)) if np.abs(Gamma) > 0 else np.inf
print(f"Return loss = {RL:.2f} dB")

# ============================================================================
# Example 2.3: Quarter-Wave Transformer
# ============================================================================
print("\n" + "=" * 60)
print("Example 2.3: Quarter-Wave Transformer")
print("=" * 60)

# Transformer a 100 ohm load to 50 ohm line
Z_0_qt = 50.0
Z_L_qt = 100.0

# Required characteristic impedance
Z_1 = np.sqrt(Z_0_qt * Z_L_qt)
print(f"Z0 = {Z_0_qt} Ω, ZL = {Z_L_qt} Ω")
print(f"Z1 (quarter-wave transformer) = sqrt(Z0*ZL) = {Z_1:.3f} Ω")

# Reflection coefficient at the transformer input
Gamma_qt = (Z_L_qt - Z_0_qt) / (Z_L_qt + Z_0_qt)
print(f"Original Γ = {Gamma_qt:.4f} (VSWR = {(1+np.abs(Gamma_qt))/(1-np.abs(Gamma_qt)):.2f})")
Gamma_qt_matched = 0  # perfectly matched by quarter-wave transformer
print(f"With quarter-wave transformer: Γ = 0 (VSWR = 1.00)")

# ============================================================================
# Figure 2.x: Transmission Line Input Impedance vs Length
# ============================================================================
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Zin vs d/lambda for different load conditions
ax1 = axes[0, 0]
d_normalized = np.linspace(0, 0.5, 500)

# Case: ZL = 100 + j50 ohm, Z0 = 50
Z_0_case = 50.0
Z_L_case = 100 + 1j*50

Z_in_real = []
Z_in_imag = []
for d in d_normalized:
    gamma_l = (Z_L_case - Z_0_case) / (Z_L_case + Z_0_case)
    z_in = Z_0_case * (Z_L_case + 1j * Z_0_case * np.tan(2*np.pi*(-d))) / \
                  (Z_0_case + 1j * Z_L_case * np.tan(2*np.pi*(-d)))
    Z_in_real.append(np.real(z_in))
    Z_in_imag.append(np.imag(z_in))

ax1.plot(d_normalized, Z_in_real, 'b-', lw=2, label='Re{Zin}')
ax1.plot(d_normalized, Z_in_imag, 'r--', lw=2, label='Im{Zin}')
ax1.set_xlabel(r'$d/\lambda$ (distance from load)', fontsize=11)
ax1.set_ylabel(r'$Z_{in}$ (Ω)', fontsize=11)
ax1.set_title(r'$Z_L = 100 + j50\,\Omega,\; Z_0 = 50\,\Omega$', fontsize=12)
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0, 0.5)
ax1.axhline(y=Z_0_case, color='gray', linestyle=':', alpha=0.7)

# Plot 2: Reflection coefficient locus on complex plane
ax2 = axes[0, 1]
theta = np.linspace(0, 2*np.pi, 500)
gamma_l_case = (Z_L_case - Z_0_case) / (Z_L_case + Z_0_case)
mag = np.abs(gamma_l_case)

# Circle of radius |Gamma|
theta_locus = np.linspace(0, 2*np.pi, 200)
circle = mag * np.exp(1j * theta_locus)
ax2.plot(np.real(circle), np.imag(circle), 'b-', lw=2)
ax2.plot([0, np.real(gamma_l_case)], [0, np.imag(gamma_l_case)], 'r-o', lw=2, markersize=8)
ax2.add_patch(plt.Circle((0, 0), 1, fill=False, color='gray', ls='--', lw=1))
ax2.set_xlim(-1.2, 1.2)
ax2.set_ylim(-1.2, 1.2)
ax2.set_aspect('equal')
ax2.set_xlabel(r'Re{Γ}', fontsize=11)
ax2.set_ylabel(r'Im{Γ}', fontsize=11)
ax2.set_title(r'Reflection Coefficient Locus |Γ|={:.3f}'.format(mag), fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.axhline(y=0, color='gray', lw=0.5)
ax2.axvline(x=0, color='gray', lw=0.5)

# Plot 3: VSWR vs |Gamma|
ax3 = axes[1, 0]
gamma_range = np.linspace(0, 0.999, 200)
vswr_range = (1 + gamma_range) / (1 - gamma_range)
ax3.plot(gamma_range, vswr_range, 'b-', lw=2)
ax3.set_xlabel(r'$|\Gamma|$', fontsize=11)
ax3.set_ylabel('VSWR', fontsize=11)
ax3.set_title('VSWR vs Reflection Coefficient Magnitude', fontsize=12)
ax3.set_ylim(1, 20)
ax3.grid(True, alpha=0.3)
ax3.axhline(y=1, color='gray', ls=':', alpha=0.7)

# Plot 4: Power flow on terminated line
ax4 = axes[1, 1]
z = np.linspace(-1, 0, 500)  # in wavelengths, from -1λ to load at 0
V_plus = 1.0  # normalized incident voltage
Gamma_p = (Z_L_case - Z_0_case) / (Z_L_case + Z_0_case)

P_forward = []
P_reflected = []
P_net = []
for z_val in z:
    V_total = V_plus * (np.exp(-1j*2*np.pi*z_val) + Gamma_p * np.exp(1j*2*np.pi*z_val))
    I_total = V_plus/Z_0_case * (np.exp(-1j*2*np.pi*z_val) - Gamma_p * np.exp(1j*2*np.pi*z_val))
    P_fwd = 0.5 * np.real(V_total * np.conj(I_total))
    P_forward.append(np.real(P_fwd))
    P_net.append(np.real(P_fwd))

ax4.plot(z, P_forward, 'b-', lw=2, label=r'$P_{forward}$')
ax4.plot(z, [-p for p in P_forward], 'r--', lw=2, label=r'$P_{reflected}$')
ax4.plot(z, P_net, 'g-', lw=2, label=r'$P_{net}$')
ax4.set_xlabel(r'$z/\lambda$ (from load at 0 toward generator)', fontsize=11)
ax4.set_ylabel(r'$P$ (normalized)', fontsize=11)
ax4.set_title('Power Flow on Terminated Line', fontsize=12)
ax4.legend()
ax4.grid(True, alpha=0.3)
ax4.set_xlim(-1, 0)

plt.tight_layout()
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wbgc/code/wbgc_ch2_transmissionline.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("\nSaved: wbgc_ch2_transmissionline.png")

# ============================================================================
# Example 2.4: Lossy Transmission Line
# ============================================================================
print("\n" + "=" * 60)
print("Example 2.4: Lossy Transmission Line")
print("=" * 60)

# Given: Z0=50 ohm, α=0.1 Np/m, β=2π/λ, f=10 GHz, length=5 cm
f_loss = 10e9
alpha_loss = 0.1   # Np/m
beta_loss = 2*np.pi / (c/f_loss)  # phase constant
Z_0_loss = 50.0
length = 0.05  # m

# Attenuation in dB
alpha_dB = alpha_loss * 8.686  # Np to dB conversion
total_loss_dB = alpha_dB * length
print(f"α = {alpha_loss} Np/m = {alpha_dB:.3f} dB/m")
print(f"Total loss for {length*100:.0f} cm: {total_loss_dB:.3f} dB")

# Input impedance of lossy line
gamma_loss = alpha_loss + 1j*beta_loss
Z_L_loss = 75 + 1j*30  # ohm
z_norm = -length  # measured from load toward generator

Z_in_loss = Z_0_loss * (Z_L_loss * np.cosh(gamma_loss * length) + 
                        Z_0_loss * np.sinh(gamma_loss * length)) / \
             (Z_0_loss * Z_L_loss * np.sinh(gamma_loss * length) + 
              Z_0_loss * np.cosh(gamma_loss * length))
print(f"Z_L = {Z_L_loss} Ω, length = {length*100:.0f} cm")
print(f"Zin = {Z_in_loss:.3f} Ω")
print(f"|Zin| = {np.abs(Z_in_loss):.3f} Ω")

print("\n✅ Chapter 2 examples completed.")