#!/usr/bin/env python3
"""
梁昌洪《简明微波》第二章 - 传输线理论
Chapter 2: Transmission Line Theory
  - Characteristic impedance Z0
  - Reflection coefficient Γ, VSWR
  - Input impedance, electrical length
  - Smith chart
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from scipy import constants

plt.rcParams.update({'font.family': 'DejaVu Sans', 'axes.unicode_minus': False})

c = constants.c  # m/s
mu0 = constants.mu_0
eps0 = constants.epsilon_0

def Z0_LC(R, L, C, G, omega):
    """Characteristic impedance from per-unit-length L,C,R,G."""
    return np.sqrt((R + 1j*omega*L) / (G + 1j*omega*C))

def Z0_from_LC(L_H_m, C_F_m):
    """Lossless Z0 from L and C."""
    return np.sqrt(L_H_m / C_F_m)

def beta_from_LC(L, C, omega):
    """Phase constant for lossless line."""
    return omega * np.sqrt(L * C)

def gamma_lossy(R, G, L, C, omega):
    """Complex propagation constant γ = α + jβ."""
    Y = G + 1j*omega*C
    Z = R + 1j*omega*L
    gamma_sq = Z * Y
    return np.sqrt(gamma_sq)

def reflection_coefficient(ZL, Z0):
    """Γ = (ZL-Z0)/(ZL+Z0)."""
    return (ZL - Z0) / (ZL + Z0)

def vswr_from_gamma(Gamma):
    """VSWR from |Γ|."""
    return (1.0 + np.abs(Gamma)) / (1.0 - np.abs(Gamma))

def input_impedance(ZL, Z0, gamma, d):
    """
    Input impedance at distance d from load (toward source).
    Z_in = Z0 * (ZL + Z0*tanh(γd)) / (Z0 + ZL*tanh(γd))
    For lossless: Z_in = Z0 * (ZL + jZ0*tan(βd)) / (Z0 + jZL*tan(βd))
    """
    th = np.tanh(gamma * d)
    return Z0 * (ZL + Z0*th) / (Z0 + ZL*th)

def input_impedance_lossless(ZL, Z0, beta, d):
    """Lossless input impedance."""
    tz = np.tan(beta * d)
    return Z0 * (ZL + 1j*Z0*tz) / (Z0 + 1j*ZL*tz)

def electrical_length(beta, d):
    """Electrical length in radians."""
    return beta * d

# ---- Smith Chart ----
def smith_grid(ax, R_max=5.0, n_pts=400):
    """Draw Smith chart grid on axes."""
    # Unit circle (Γ locus)
    theta = np.linspace(0, 2*np.pi, 800)
    ax.plot(np.cos(theta), np.sin(theta), 'k-', lw=1.2)
    # Constant resistance circles
    for r in np.arange(0.0, R_MAX := R_max + 0.1, 0.2):
        if r < 1e-3:
            ax.axvline(0, color='k', lw=0.8)
            continue
        center = r / (1 + r)
        radius = 1.0 / (1 + r)
        th = np.linspace(0, 2*np.pi, n_pts)
        x = center + radius * np.cos(th)
        y = radius * np.sin(th)
        mask = (x**2 + y**2) <= 1.01
        ax.plot(x[mask], y[mask], 'steelblue', lw=0.5, alpha=0.6)
    # Constant reactance arcs (positive = upper, negative = lower)
    for x_j in np.arange(0.1, R_max + 0.1, 0.2):
        # positive reactance (upper half)
        cx = 1.0 / x_j
        cy = 1.0
        r_arc = np.abs(1.0 / x_j)
        th = np.linspace(0, np.pi, n_pts)
        x = cx - r_arc * np.cos(th)
        y = r_arc * np.sin(th) + cy
        mask = (x**2 + y**2) <= 1.01
        ax.plot(x[mask], y[mask], 'steelblue', lw=0.5, alpha=0.6)
        # negative reactance (lower half)
        y2 = -r_arc * np.sin(th) + cy
        mask2 = (x**2 + y2**2) <= 1.01
        ax.plot(x[mask2], y2[mask2], 'steelblue', lw=0.5, alpha=0.6)
    ax.set_xlim(-1.05, 1.05)
    ax.set_ylim(-1.05, 1.05)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Smith Chart (Normalized Impedance)', fontsize=11, pad=10)

def plot_point_on_smith(ax, z_norm, color='red', ms=6):
    """Plot normalized impedance point on Smith chart."""
    gamma = (z_norm - 1.0) / (z_norm + 1.0)
    gamma = complex(gamma)
    if np.abs(gamma) <= 1.0:
        ax.plot(gamma.real, gamma.imag, 'o', color=color, ms=ms, zorder=10)

def main():
    # ========== Example 1: Coaxial cable Z0 ==========
    print("=" * 60)
    print("  梁昌洪《简明微波》第二章 - 传输线理论计算")
    print("=" * 60)

    # Example: coaxial cable with polyethylene (ε_r=2.25)
    eps_r = 2.25
    D = 2.3e-3   # outer diameter m
    d = 0.7e-3   # inner diameter m
    Z0_coax = (1e7 / (2*np.pi)) * np.sqrt(mu0/eps0/eps_r) * np.log(D/d)
    print(f"\n[同轴线示例] ε_r={eps_r}, D={D*1e3:.1f}mm, d={d*1e3:.1f}mm")
    print(f"  Z0 = {Z0_coax:.2f} Ω")

    # Example: parallel-wire line
    D_wire = 2e-3  # wire diameter m
    D_sep  = 10e-3 # separation m
    Z0_pp = (1e7 / np.pi) * np.sqrt(mu0/eps0) * np.arccosh(D_sep/D_wire)
    print(f"\n[平行双导线示例] 线径={D_wire*1e3:.1f}mm, 间距={D_sep*1e3:.1f}mm (ε_r=1)")
    print(f"  Z0 = {Z0_pp:.2f} Ω")

    # ========== Example 2: Reflection & VSWR ==========
    print("\n--- 反射系数与驻波比 ---")
    Z0 = 50.0
    ZL_list = [75.0, 25.0, 50.0, 50+30j, 50-40j]
    for ZL in ZL_list:
        Gamma = reflection_coefficient(ZL, Z0)
        VSWR = vswr_from_gamma(Gamma)
        print(f"  ZL={ZL:>10.2f}  Gamma={Gamma:.4f}  |Gamma|={np.abs(Gamma):.4f}  VSWR={VSWR:.3f}")

    # ========== Example 3: Input impedance (lossless) ==========
    print("\n--- 无耗线输入阻抗 (Z0=50Ω, f=3GHz) ---")
    f = 3e9
    v = c / np.sqrt(2.1)   # phase velocity in microstrip substrate
    beta = 2*np.pi*f / v
    Z0 = 50.0
    ZL = 100.0
    d_vals = np.linspace(0, 0.25*c/f, 200)  # up to λ/4
    Zin = np.array([input_impedance_lossless(ZL, Z0, beta, d) for d in d_vals])
    print(f"  d=0 (负载面):     Z_in = {Zin[0]:.2f} Ω")
    print(f"  d=λ/4 (阻抗变换): Z_in = {input_impedance_lossless(ZL, Z0, beta, c/f/4):.2f} Ω")

    # ========== Example 4: Quarter-wave transformer ==========
    print("\n--- λ/4 阻抗变换 (Z0=50Ω, ZL=100Ω) ---")
    Z0_q = np.sqrt(50 * 100)
    print(f"  最佳 Z0_q = √(50×100) = {Z0_q:.2f} Ω")

    # ========== Example 5: lossy line attenuation ==========
    print("\n--- 有耗线衰减 (同轴线, f=10GHz) ---")
    f = 10e9
    omega = 2*np.pi*f
    sigma_cu = 5.8e7
    mu_cu = mu0
    delta = np.sqrt(2.0 / (omega * mu_cu * sigma_cu))
    R_s = 1.0 / (sigma_cu * delta)
    # Simplified α for coaxial: α_c ≈ R_s/(2*Z0) * (1/a + 1/b)
    a = 0.35e-3  # inner radius
    b = 1.15e-3  # outer radius
    Z0_0 = 50.0
    alpha_c = R_s / (2.0 * Z0_0) * (1.0/a + 1.0/b)  # Neper/m
    alpha_dB = alpha_c * 8.686  # dB/m
    print(f"  趋肤深度 δ = {delta*1e6:.3f} μm")
    print(f"  表面电阻 R_s = {R_s:.4f} Ω/sq")
    print(f"  导体衰减 α = {alpha_dB:.3f} dB/m")

    # ========== PLOTS ==========
    fig = plt.figure(figsize=(16, 6))

    # ---- Plot 1: Zin vs d ----
    ax1 = fig.add_subplot(1, 3, 1)
    ax1.plot(d_vals * 1e3, Zin.real, 'b-', label=r'$R_{in}$ (Ω)')
    ax1.plot(d_vals * 1e3, Zin.imag, 'r--', label=r'$X_{in}$ (Ω)')
    ax1.set_xlabel(r'$d$ (mm)', fontsize=11)
    ax1.set_ylabel(r'$Z_{in}$ (Ω)', fontsize=11)
    ax1.set_title(r'$Z_{in}$ vs distance from load ($Z_L=100\Omega, Z_0=50\Omega$)', fontsize=11)
    ax1.legend()
    ax1.grid(True, alpha=0.4)

    # ---- Plot 2: VSWR circle on Smith ----
    ax2 = fig.add_subplot(1, 3, 2, projection='polar')
    ax2 = fig.add_axes([0.38, 0.15, 0.28, 0.75], projection='polar')
    ax2.remove()
    ax2 = fig.add_axes([0.38, 0.15, 0.28, 0.75], projection='polar')
    smith_grid_polar(ax2)
    ax2.set_title('Reflection Coefficient\nPolar Plot', fontsize=10, pad=20)

    # ---- Plot 3: Smith Chart with examples ----
    ax3 = fig.add_axes([0.70, 0.12, 0.28, 0.82])
    smith_grid(ax3)
    z_examples = [0.5, 1.0, 2.0, 0.5+0.5j, 1.0-1.0j, 2.0+1.0j]
    labels = ['ZL=25Ω', 'ZL=50Ω', 'ZL=100Ω', 'ZL=25+25j', 'ZL=50-50j', 'ZL=100+50j']
    colors = ['red','green','blue','orange','purple','brown']
    for z_n, lbl, clr in zip(z_examples, labels, colors):
        gamma = (z_n - 1.0) / (z_n + 1.0)
        gamma = complex(gamma)
        ax3.plot(gamma.real, gamma.imag, 'o', color=clr, ms=7, zorder=10, label=lbl)
    ax3.legend(loc='upper left', fontsize=7)

    fig.suptitle(r'梁昌洪《简明微波》第二章 — 传输线理论', fontsize=14, y=1.02)
    plt.tight_layout()
    out = '/home/ubuntu/.openclaw/workspace/textbooks/liangchanghong/code/ch2_transmission_line.png'
    fig.savefig(out, dpi=150, bbox_inches='tight')
    print(f"\n  [saved] {out}")
    plt.close()

def smith_grid_polar(ax):
    """Draw constant-|Γ| circles on polar axes."""
    thetas = np.linspace(0, 2*np.pi, 400)
    for r_gamma in [0.2, 0.4, 0.6, 0.8, 1.0]:
        ax.plot(thetas, [r_gamma]*len(thetas), 'steelblue', lw=0.5, alpha=0.6)
    ax.set_theta_zero_location('E')
    ax.set_theta_direction(1)
    ax.set_rlim(0, 1.1)

if __name__ == '__main__':
    main()
