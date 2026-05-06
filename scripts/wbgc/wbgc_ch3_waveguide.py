#!/usr/bin/env python3
"""
简明微波 (梁昌洪) - 第3章: 波导与谐振器
Waveguide and Resonator - Chapter 3

Topics covered:
- TEM, TE, TM modes (3.1)
- Rectangular waveguide (3.2)
- Circular waveguide (3.3)
- Cavity resonators (3.4-3.5)
- Microstrip lines (3.6)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Wedge, FancyArrowPatch
from matplotlib.collections import PatchCollection
import matplotlib.gridspec as gridspec

c = 2.998e8        # speed of light (m/s)
mu_0 = 4 * np.pi * 1e-7
eps_0 = 1 / (mu_0 * c**2)
Z_0 = np.sqrt(mu_0 / eps_0)  # ~377 ohm

# ============================================================================
# Example 3.1: Rectangular Waveguide - TE10 Mode
# ============================================================================
print("=" * 60)
print("Example 3.1: Rectangular Waveguide TE10 Mode")
print("=" * 60)

# WR-90 waveguide: a=0.09 m (9 cm), b=0.04 m (4 cm)
a_wg = 0.09    # broad dimension (m)
b_wg = 0.04    # narrow dimension (m)

# Operating frequency f=10 GHz
f_wg = 10e9    # Hz
omega_wg = 2 * np.pi * f_wg

# Wave number in free space
k_0 = omega_wg * np.sqrt(mu_0 * eps_0)
print(f"f = {f_wg/1e9:.0f} GHz, λ0 = {c/f_wg*100:.2f} cm")
print(f"Waveguide dimensions: a={a_wg*100:.1f} cm, b={b_wg*100:.1f} cm")

# Cutoff frequencies for TE and TM modes
def cutoff_freq_TE(m, n, a, b, v_p=c):
    """Cutoff frequency for TE_mn or TM_mn mode"""
    k_c = np.pi * np.sqrt((m/a)**2 + (n/b)**2)
    f_c = k_c * v_p / (2*np.pi)
    return f_c, k_c

f_c_10, k_c_10 = cutoff_freq_TE(1, 0, a_wg, b_wg)
print(f"\nTE10 mode: f_c = {f_c_10/1e9:.3f} GHz, λ_c = {2*a_wg*100:.2f} cm")

f_c_20, k_c_20 = cutoff_freq_TE(2, 0, a_wg, b_wg)
f_c_01, k_c_01 = cutoff_freq_TE(0, 1, a_wg, b_wg)
f_c_11, k_c_11 = cutoff_freq_TE(1, 1, a_wg, b_wg)
print(f"TE20 mode: f_c = {f_c_20/1e9:.3f} GHz")
print(f"TE01 mode: f_c = {f_c_01/1e9:.3f} GHz")
print(f"TE11/TM11 mode: f_c = {f_c_11/1e9:.3f} GHz")

# Single-mode operation (TE10) range: f_c10 < f < f_c20
print(f"\nSingle-mode (TE10) range: {f_c_10/1e9:.3f} ~ {f_c_20/1e9:.3f} GHz")

# Propagation constant for TE10 at f=10 GHz
k_c = k_c_10
k_0_val = 2*np.pi * f_wg / c
beta_10 = np.sqrt(k_0_val**2 - k_c**2)
print(f"\nAt f={f_wg/1e9:.0f} GHz, TE10:")
print(f"  β = {beta_10:.4f} rad/m")
print(f"  λg = {2*np.pi/beta_10*100:.2f} cm")
print(f"  λ_c = {2*np.pi/k_c*100:.2f} cm")

# Phase velocity and group velocity
v_p_wg = omega_wg / beta_10
v_g_wg = 1 / np.sqrt(mu_0 * eps_0) / beta_10 * omega_wg  # dω/dβ
print(f"  v_p = {v_p_wg/1e6:.2f} × 10⁶ m/s = {v_p_wg/c*100:.2f}% c")
print(f"  v_g = {v_g_wg/1e6:.2f} × 10⁶ m/s = {v_g_wg/c*100:.2f}% c")

# Wave impedance for TE10
eta_TE = Z_0 * k_0_val / beta_10
print(f"  η_TE10 = {eta_TE:.2f} Ω")

# ============================================================================
# Example 3.2: Circular Waveguide
# ============================================================================
print("\n" + "=" * 60)
print("Example 3.2: Circular Waveguide")
print("=" * 60)

# Circular waveguide radius a_circ = 5 cm
a_circ = 0.05  # m
f_circ = 10e9  # Hz

# Bessel function zeros for TE modes
# J0'(x) zeros: ~1.8412 (TE11), ~3.0542 (TE21), ~4.2012 (TE01)
# J1'(x) zeros: ~3.8317 (TM11), ~7.0156 (TM21), ...
TE11_zero = 1.8412
TE01_zero = 3.0542

# Cutoff frequency for TE11 (dominant mode)
f_c_TE11_circ = TE11_zero * c / (2 * np.pi * a_circ)
print(f"Circular waveguide radius a = {a_circ*100:.0f} cm")
print(f"TE11 mode: f_c = {f_c_TE11_circ/1e9:.3f} GHz")

f_c_TE01_circ = TE01_zero * c / (2 * np.pi * a_circ)
print(f"TE01 mode: f_c = {f_c_TE01_circ/1e9:.3f} GHz")

# At f=15 GHz, check propagation
f_circ_test = 15e9
k_0_circ = 2*np.pi * f_circ_test / c
k_c_TE11 = TE11_zero / a_circ
if k_0_circ > k_c_TE11:
    beta_TE11 = np.sqrt(k_0_circ**2 - k_c_TE11**2)
    print(f"\nAt f={f_circ_test/1e9:.0f} GHz, TE11 propagates:")
    print(f"  β = {beta_TE11:.4f} rad/m")
else:
    print(f"\nAt f={f_circ_test/1e9:.0f} GHz, TE11 is evanescent (below cutoff)")

# ============================================================================
# Example 3.3: Rectangular Cavity Resonator
# ============================================================================
print("\n" + "=" * 60)
print("Example 3.3: Rectangular Cavity Resonator")
print("=" * 60)

# Cavity dimensions: a=3 cm, b=2 cm, d=4 cm
a_cav = 0.03
b_cav = 0.02
d_cav = 0.04

def cavity_resonant_freq(m, n, p, a, b, d, v_p=c):
    """Resonant frequency for TE_mnp or TM_mnp mode"""
    k_mnp = np.pi * np.sqrt((m/a)**2 + (n/b)**2 + (p/d)**2)
    f_mnp = k_mnp * v_p / (2*np.pi)
    return f_mnp, k_mnp

f_101, k_101 = cavity_resonant_freq(1, 0, 1, a_cav, b_cav, d_cav)
print(f"Cavity: {a_cav*100:.0f}×{b_cav*100:.0f}×{d_cav*100:.0f} cm")
print(f"TE101 mode: f_r = {f_101/1e9:.3f} GHz")
print(f"TE102 mode: f_r = {cavity_resonant_freq(1,0,2,a_cav,b_cav,d_cav)[0]/1e9:.3f} GHz")
print(f"TE111 mode: f_r = {cavity_resonant_freq(1,1,1,a_cav,b_cav,d_cav)[0]/1e9:.3f} GHz")

# Q-factor for TE101 (using conductor quality factor)
# Q ~ (3.012 * a + b) * d / (2 * (a + b) * delta_s)
# where delta_s = skin depth
sigma_cu = 5.8e7  # S/m (copper)
mu_cu = mu_0
delta_s = np.sqrt(2 / (omega_wg * mu_cu * sigma_cu))
print(f"\nSkin depth at f=10 GHz: δ_s = {delta_s*1e6:.3f} µm")

# Rough Q estimate for TE101
# Q = k_0 * a * b * d / (2 * delta_s * (a + b) * (2*d + b))
Q_101 = (k_101 * a_cav * b_cav * d_cav) / (2 * delta_s * (a_cav + b_cav) * (2*d_cav + b_cav))
print(f"Estimated Q for TE101: Q ≈ {Q_101:.0f}")

# ============================================================================
# Example 3.4: Microstrip Line - Characteristic Impedance
# ============================================================================
print("\n" + "=" * 60)
print("Example 3.4: Microstrip Line")
print("=" * 60)

# Given: Z0=50 ohm, w=3 mm, h=1.5 mm, ε_r=4.7 (PCB substrate)
w_ms = 0.003     # m
h_ms = 0.0015    # m
eps_r_ms = 4.7   # relative permittivity

# Calculate effective permittivity (simplified)
w_over_h = w_ms / h_ms
if w_over_h < 1:
    eps_eff = (eps_r_ms + 1)/2 + (eps_r_ms - 1)/2 * (1/np.sqrt(1 + 12/w_over_h))
else:
    eps_eff = (eps_r_ms + 1)/2 + (eps_r_ms - 1)/2 * (1/np.sqrt(1 + 12/w_over_h))

# Effective width accounting for thickness
if w_over_h < 2:
    w_eff = w_ms + 0.4 * h_ms
else:
    w_eff = w_ms + 0.4 * h_ms

print(f"w/h = {w_over_h:.2f}")
print(f"Effective permittivity: ε_eff = {eps_eff:.3f}")
print(f"Effective width: w_eff = {w_eff*1000:.3f} mm")

# Phase velocity
v_p_ms = c / np.sqrt(eps_eff)
print(f"Phase velocity: v_p = {v_p_ms/1e6:.2f} × 10⁶ m/s")

# Guided wavelength at f=5 GHz
f_ms = 5e9
lambda_g_ms = v_p_ms / f_ms
print(f"λ_g at f={f_ms/1e9:.0f} GHz: {lambda_g_ms*100:.2f} cm")

# ============================================================================
# Figure: Rectangular Waveguide Field Patterns
# ============================================================================
fig = plt.figure(figsize=(16, 10))
gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.4, wspace=0.4)

# 1. TE10 mode electric field pattern
ax1 = fig.add_subplot(gs[0, 0])
x_vals = np.linspace(0, a_wg, 200)
Ey_TE10 = np.cos(np.pi * x_vals / a_wg)
ax1.plot(x_vals*100, Ey_TE10, 'b-', lw=2)
ax1.fill_between(x_vals*100, 0, Ey_TE10, alpha=0.3)
ax1.set_xlabel('x (cm)', fontsize=11)
ax1.set_ylabel(r'$E_y$ (normalized)', fontsize=11)
ax1.set_title(r'TE10: $E_y(x) = E_0 \cos(\pi x/a)$', fontsize=12)
ax1.set_xlim(0, a_wg*100)
ax1.grid(True, alpha=0.3)
ax1.axhline(y=0, color='k', lw=0.5)

# 2. TE10 magnetic field components
ax2 = fig.add_subplot(gs[0, 1])
z_vals = np.linspace(0, lambda_g_ms*2, 200) if 'lambda_g_ms' in dir() else np.linspace(0, 0.05, 200)
# H_x component (out of phase with E_y)
Hx_TE10 = -np.sin(np.pi * 0.5 * a_wg / a_wg) * np.sin(2*np.pi*z_vals/0.03)  # simplified
ax2.plot(z_vals*100, np.zeros_like(z_vals), 'b-', lw=2, label=r'$H_x$')
ax2.set_xlabel(r'$z$ (cm)', fontsize=11)
ax2.set_title(r'TE10: Magnetic Field Components', fontsize=12)
ax2.legend()
ax2.grid(True, alpha=0.3)

# 3. Dispersion diagram (β vs f)
ax3 = fig.add_subplot(gs[0, 2])
f_range = np.linspace(5e9, 15e9, 300)
k_0_range = 2*np.pi * f_range / c
k_c_val = k_c_10
beta_vals = np.sqrt(k_0_range**2 - k_c_val**2)
beta_vals = np.where(k_0_range > k_c_val, beta_vals, 0)

ax3.plot(f_range/1e9, beta_vals, 'b-', lw=2)
ax3.axhline(y=k_c_val, color='r', ls='--', label=r'$k_c$ (cutoff)')
ax3.set_xlabel('f (GHz)', fontsize=11)
ax3.set_ylabel(r'β (rad/m)', fontsize=11)
ax3.set_title('TE10 Dispersion Relation', fontsize=12)
ax3.legend()
ax3.grid(True, alpha=0.3)
ax3.set_xlim(5, 15)
ax3.set_ylim(0, 250)

# 4. Circular waveguide - mode chart
ax4 = fig.add_subplot(gs[1, 0])
modes = ['TE11', 'TM11', 'TE21', 'TE01', 'TM01']
zeros = [1.8412, 1.8412, 3.0542, 3.0542, 3.8317]
f_c_modes = [z * c / (2*np.pi*a_circ) / 1e9 for z in zeros]
colors = ['blue', 'green', 'red', 'orange', 'purple']

bars = ax4.barh(modes, f_c_modes, color=colors, alpha=0.7)
ax4.set_xlabel(r'$f_c$ (GHz)', fontsize=11)
ax4.set_title('Circular Waveguide: Mode Cutoff Frequencies', fontsize=12)
ax4.grid(True, alpha=0.3, axis='x')
for bar, f_c in zip(bars, f_c_modes):
    ax4.text(f_c + 0.1, bar.get_y() + bar.get_height()/2, 
             f'{f_c:.2f} GHz', va='center', fontsize=10)

# 5. Cavity resonator - resonant frequencies
ax5 = fig.add_subplot(gs[1, 1])
modes_cav = ['TE101', 'TE102', 'TE111', 'TE201', 'TM111']
f_r_modes = [cavity_resonant_freq(1,0,1,a_cav,b_cav,d_cav)[0]/1e9,
             cavity_resonant_freq(1,0,2,a_cav,b_cav,d_cav)[0]/1e9,
             cavity_resonant_freq(1,1,1,a_cav,b_cav,d_cav)[0]/1e9,
             cavity_resonant_freq(2,0,1,a_cav,b_cav,d_cav)[0]/1e9,
             cavity_resonant_freq(1,1,1,a_cav,b_cav,d_cav)[0]/1e9]
ax5.bar(modes_cav, f_r_modes, color='steelblue', alpha=0.8)
ax5.set_ylabel(r'$f_r$ (GHz)', fontsize=11)
ax5.set_title('Rectangular Cavity Resonant Modes', fontsize=12)
ax5.grid(True, alpha=0.3, axis='y')
for i, f_r in enumerate(f_r_modes):
    ax5.text(i, f_r + 0.05, f'{f_r:.2f}', ha='center', fontsize=10)

# 6. Microstrip - Z0 vs w/h for different ε_r
ax6 = fig.add_subplot(gs[1, 2])
w_h_range = np.logspace(-1, 1, 200)  # 0.1 to 10

def microstrip_Z0(w_h, eps_r):
    """Approximate characteristic impedance of microstrip"""
    if w_h < 1:
        return (30 / np.sqrt(eps_r)) * np.log(8/w_h + w_h/4)
    else:
        return (120 * np.pi / np.sqrt(eps_r)) / (w_h + 1.393 + 0.667 * np.log(w_h + 1.444))

eps_r_values = [2.2, 4.7, 9.8]
for eps_r_val in eps_r_values:
    Z0_vals = [microstrip_Z0(w_h, eps_r_val) for w_h in w_h_range]
    ax6.semilogx(w_h_range, Z0_vals, lw=2, label=f'ε_r={eps_r_val}')
ax6.axhline(y=50, color='k', ls=':', alpha=0.7, label='50 Ω')
ax6.set_xlabel(r'$w/h$', fontsize=11)
ax6.set_ylabel(r'$Z_0$ (Ω)', fontsize=11)
ax6.set_title('Microstrip: Characteristic Impedance', fontsize=12)
ax6.legend()
ax6.grid(True, alpha=0.3, which='both')
ax6.set_ylim(20, 150)

plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wbgc/code/wbgc_ch3_waveguide.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("\nSaved: wbgc_ch3_waveguide.png")

print("\n✅ Chapter 3 examples completed.")