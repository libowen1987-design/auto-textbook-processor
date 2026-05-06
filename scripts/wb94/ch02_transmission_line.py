"""
第二章 传输线理论 - 特性阻抗与输入阻抗
========================================
基于梁昌洪《简明微波》第二章内容

本文件覆盖：
1. 均匀传输线分布参数计算（双导线、同轴线、平行板）
2. 特性阻抗 Z0 计算
3. 传播常数 γ = α + jβ
4. 输入阻抗 Zin(d) 计算
5. 反射系数 Γ(d)
6. 电压驻波比 VSWR
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import matplotlib.patches as mpatches

plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.figsize': (12, 8),
    'axes.grid': True,
    'grid.alpha': 0.3,
})

# ============================================================
# 1. 分布参数计算
# ============================================================

def distributed_params_coaxial(r_inner, r_outer, epsilon_r=1.0, mu_r=1.0,
                                sigma_cond=None, sigma_diel=None):
    """
    计算同轴线单位长度的分布参数
    
    参数:
        r_inner: 内导体半径 [m]
        r_outer: 外导体内半径 [m]
        epsilon_r: 相对介电常数
        mu_r: 相对磁导率
        sigma_cond: 导体电导率 [S/m]，None=铜
        sigma_diel: 介质电导率 [S/m]，None=理想
    
    返回:
        dict: R, L, C, G (单位长度的分布参数)
    """
    if sigma_cond is None:
        sigma_cond = 5.8e7  # 铜
    if sigma_diel is None:
        sigma_diel = 0.0    # 理想介质
    
    mu_0 = 4e-7 * np.pi
    epsilon_0 = 8.854e-12
    
    # 集肤深度
    delta_s = lambda f: np.sqrt(2.0 / (omega(f) * mu_0 * mu_r * sigma_cond))
    
    # 分布电容
    C = 2 * np.pi * epsilon_0 * epsilon_r / np.log(r_outer / r_inner)  # F/m
    
    # 分布电感 (内外导体自感 + 互感)
    L = (mu_0 * mu_r / (2 * np.pi)) * np.log(r_outer / r_inner)  # H/m
    
    # 分布电导
    G = 2 * np.pi * sigma_diel / np.log(r_outer / r_inner)  # S/m
    
    return {'C': C, 'L': L, 'G': G, 'delta_s_func': delta_s}


def distributed_params_twin_lead(d, D, epsilon_r=1.0, mu_r=1.0, sigma_cond=None):
    """
    双导线传输线的分布参数
    d: 导线直径 [m]
    D: 线间距 [m]
    """
    if sigma_cond is None:
        sigma_cond = 5.8e7
    
    mu_0 = 4e-7 * np.pi
    epsilon_0 = 8.854e-12
    
    # 分布电容 (平行导线近似)
    C = np.pi * epsilon_0 * epsilon_r / np.arccosh(D / d)
    
    # 分布电感
    L = (mu_0 * mu_r / np.pi) * np.arccosh(D / d)
    
    return {'C': C, 'L': L, 'G': 0.0}


def distributed_params_parallel_plate(w, h, epsilon_r=1.0, mu_r=1.0, t=None, sigma_cond=None):
    """
    平行板传输线的分布参数
    w: 板宽 [m]
    h: 板间距 [m]
    t: 金属厚度 [m], None则忽略趋肤效应
    """
    if sigma_cond is None:
        sigma_cond = 5.8e7
    
    mu_0 = 4e-7 * np.pi
    epsilon_0 = 8.854e-12
    
    # 准静态参数
    C = epsilon_0 * epsilon_r * w / h
    L = mu_0 * mu_r * h / w
    
    return {'C': C, 'L': L, 'G': 0.0}


# ============================================================
# 2. 特性阻抗与传播常数
# ============================================================

def characteristic_impedance(R, G, L, C, omega):
    """
    传输线特性阻抗 Z0 = sqrt((R+jωL)/(G+jωC))
    """
    Z = complex(R, omega * L)
    Y = complex(G, omega * C)
    Z0 = np.sqrt(Z / Y)
    return Z0


def propagation_constant(R, G, L, C, omega):
    """
    传播常数 γ = sqrt((R+jωL)(G+jωC)) = α + jβ
    """
    Z = complex(R, omega * L)
    Y = complex(G, omega * C)
    gamma = np.sqrt(Z * Y)
    return gamma


def lossless_characteristic_impedance(L, C):
    """
    无耗线的特性阻抗 (R=0, G=0)
    Z0 = sqrt(L/C)
    """
    return np.sqrt(L / C)


# ============================================================
# 3. 输入阻抗、反射系数、VSWR
# ============================================================

def input_impedance(Z0, ZL, gamma, d):
    """
    输入阻抗: Zin(d) = Z0 * (ZL + Z0*tanh(γd)) / (Z0 + ZL*tanh(γd))
    d: 从负载向源方向的距离 [m]
    """
    gamma_d = gamma * d
    tanh_gd = np.tanh(gamma_d)
    Zin = Z0 * (ZL + Z0 * tanh_gd) / (Z0 + ZL * tanh_gd)
    return Zin


def reflection_coefficient_at_distance(Gamma_0, gamma, d):
    """
    距离负载d处的反射系数: Γ(d) = Γ0 * exp(-2γd)
    其中 Γ0 = (ZL - Z0)/(ZL + Z0)
    """
    return Gamma_0 * np.exp(-2 * gamma * d)


def reflection_coefficient_load(ZL, Z0):
    """
    负载处的反射系数
    """
    return (ZL - Z0) / (ZL + Z0)


def vswr(Gamma_0):
    """
    电压驻波比 VSWR = (1 + |Γ|) / (1 - |Γ|)
    """
    return (1 + np.abs(Gamma_0)) / (1 - np.abs(Gamma_0))


def vswr_from_zin(Z_in):
    """
    从归一化输入阻抗的实部计算VSWR
    """
    r = np.real(Z_in)
    if r <= 0:
        return np.inf
    vswr_val = r + np.sqrt(r**2 - 1)
    return vswr_val


# ============================================================
# 4. 无耗线特例
# ============================================================

def input_impedance_lossless(Z0, ZL, beta, d):
    """
    无耗传输线输入阻抗
    Zin = Z0 * (ZL + jZ0*tan(βd)) / (Z0 + jZL*tan(βd))
    """
    tan_bd = np.tan(beta * d)
    Zin = Z0 * (ZL + 1j * Z0 * tan_bd) / (Z0 + 1j * ZL * tan_bd)
    return Zin


def impedance_at_quarter_wavelength(Z0, ZL):
    """
    λ/4 传输线的阻抗变换特性
    Zin = Z0^2 / ZL
    """
    return Z0**2 / ZL


def impedance_at_half_wavelength(Z0, ZL):
    """
    λ/2 传输线的阻抗重复性
    Zin = ZL
    """
    return ZL


# ============================================================
# 例题 2.1: 同轴线特性阻抗计算
# ============================================================

def example_coaxial_Z0():
    """
    例题: 已知同轴线内导体半径 r1 = 1mm, 外导体内半径 r2 = 3.5mm,
    填充空气 (εr=1), 求特性阻抗 Z0
    """
    r1 = 1e-3      # 1 mm
    r2 = 3.5e-3    # 3.5 mm
    epsilon_0 = 8.854e-12
    mu_0 = 4e-7 * np.pi
    
    # 无耗同轴线特性阻抗 (R=0, G=0)
    Z0 = (1 / (2 * np.pi)) * np.sqrt(mu_0 / epsilon_0) * np.log(r2 / r1)
    
    print(f"同轴线特性阻抗 Z0 = {Z0:.4f} Ω")
    print(f"理论值 50 Ω 对应的 r2/r1 比值 = {np.exp(2 * np.pi * 50 * np.sqrt(epsilon_0 / mu_0)):.4f}")
    return Z0


# ============================================================
# 例题 2.2: 有耗线传播常数
# ============================================================

def example_lossy_line():
    """
    例题: 已知传输线参数 R=0.5 Ω/m, L=0.1 μH/m, G=0.01 S/m, C=100 pF/m
    工作频率 f = 1 GHz
    
    计算: 特性阻抗 Z0, 传播常数 γ = α + jβ
    """
    R = 0.5      # Ω/m
    L = 0.1e-6   # H/m
    G = 0.01     # S/m
    C = 100e-12  # F/m
    
    f = 1e9      # 1 GHz
    omega = 2 * np.pi * f
    
    Z0 = characteristic_impedance(R, G, L, C, omega)
    gamma = propagation_constant(R, G, L, C, omega)
    
    print(f"工作频率 f = {f/1e9:.1f} GHz")
    print(f"特性阻抗 Z0 = {Z0:.4f} Ω (幅值={np.abs(Z0):.4f}, 相角={np.angle(Z0)*180/np.pi:.2f}°)")
    print(f"传播常数 γ = {gamma:.6f} 1/m")
    print(f"  衰减常数 α = {np.real(gamma):.6f} Np/m = {np.real(gamma)*8.686:.4f} dB/m")
    print(f"  相位常数 β = {np.imag(gamma):.6f} rad/m")
    
    # 相速度 vp = ω/β
    vp = omega / np.imag(gamma)
    print(f"相速度 vp = {vp:.4e} m/s ({vp/3e8:.4f} c)")
    
    return Z0, gamma


# ============================================================
# 例题 2.3: 负载阻抗与反射系数
# ============================================================

def example_reflection_coefficient():
    """
    例题: 无耗传输线 Z0=50Ω, 负载 ZL=100+j50 Ω, 
    工作频率 f=3 GHz, 求:
    1) 负载处反射系数 Γ
    2) VSWR
    3) 若线长 l=λ/4, 求输入阻抗
    """
    Z0 = 50.0
    ZL = complex(100, 50)
    f = 3e9
    
    # 波长 (空气填充)
    c = 3e8
    lambda_ = c / f
    
    # 负载反射系数
    Gamma = reflection_coefficient_load(ZL, Z0)
    print(f"负载: ZL = {ZL}")
    print(f"负载反射系数 Γ = {Gamma}")
    print(f"  |Γ| = {np.abs(Gamma):.4f}")
    print(f"  ∠Γ = {np.angle(Gamma)*180/np.pi:.2f}°")
    
    # VSWR
    s = vswr(Gamma)
    print(f"VSWR = {s:.4f}")
    
    # λ/4 线的输入阻抗
    # 对于无耗线，β*l = β*λ/4 = π/2
    beta = 2 * np.pi / lambda_
    d = lambda_ / 4
    Zin = input_impedance_lossless(Z0, ZL, beta, d)
    print(f"λ/4 线输入阻抗 Zin = {Zin:.4f} Ω")
    
    # 检验: Zin = Z0^2 / ZL
    Zin_check = Z0**2 / ZL
    print(f"检验: Z0^2/ZL = {Zin_check:.4f}")
    
    return Gamma, s, Zin


# ============================================================
# 例题 2.4: 输入阻抗沿线分布
# ============================================================


    import os
    os.makedirs('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures', exist_ok=True)
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_Zin_along_line.png', dpi=150, bbox_inches='tight')
    print('Figure saved.')
def example_Zin_along_line():
    """
    例题: 绘制无耗传输线沿线输入阻抗的分布
    Z0=75Ω, ZL=50-j30Ω, 频率 f=10GHz
    """
    Z0 = 75.0
    ZL = complex(50, -30)
    f = 10e9
    c = 3e8
    lambda_ = c / f
    beta = 2 * np.pi / lambda_
    
    # 从负载向源计算 d∈[0, λ]
    d_vals = np.linspace(0, lambda_, 1000)
    
    Zin_real = []
    Zin_imag = []
    for d in d_vals:
        z = input_impedance_lossless(Z0, ZL, beta, d)
        Zin_real.append(np.real(z))
        Zin_imag.append(np.imag(z))
    
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    
    # 归一化阻抗
    z_norm_real = np.array(Zin_real) / Z0
    z_norm_imag = np.array(Zin_imag) / Z0
    
    axes[0].plot(d_vals / lambda_, z_norm_real, 'b-', lw=1.5, label='Re{Zin/Z0}')
    axes[0].plot(d_vals / lambda_, z_norm_imag, 'r--', lw=1.5, label='Im{Zin/Z0}')
    axes[0].set_xlabel(r'$d/\lambda$ (distance from load)')
    axes[0].set_ylabel(r'$Z_{in}/Z_0$')
    axes[0].set_title(rf'$Z_0={Z0}\Omega$, $Z_L={ZL.real}+j{ZL.imag}\Omega$, $f={f/1e9:.0f}$ GHz')
    axes[0].legend()
    axes[0].axhline(y=1, color='gray', linestyle=':', alpha=0.5)
    
    # 反射系数幅值沿线不变 (无耗线)
    Gamma_0 = reflection_coefficient_load(ZL, Z0)
    Gamma_mag = np.abs(Gamma_0) * np.ones_like(d_vals)
    
    axes[1].plot(d_vals / lambda_, Gamma_mag, 'g-', lw=2)
    axes[1].set_xlabel(r'$d/\lambda$')
    axes[1].set_ylabel(r'$|\Gamma(d)|$')
    axes[1].set_title(rf'Reflection coefficient magnitude ($|\Gamma_0|={np.abs(Gamma_0):.4f}$)')
    axes[1].set_ylim([0, 1.1])
    
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_transmission_line_Zin.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_transmission_line_Zin.png")
    
    return None


# ============================================================
# 例题 2.5: 双导线特性阻抗计算
# ============================================================

def example_twin_lead():
    """
    例题: 双导线直径 d=1mm, 线间距 D=5mm, 空气填充
    计算特性阻抗 Z0
    """
    d = 1e-3    # 1 mm
    D = 5e-3    # 5 mm
    epsilon_0 = 8.854e-12
    mu_0 = 4e-7 * np.pi
    
    # 无耗双导线特性阻抗
    Z0 = (1 / np.pi) * np.sqrt(mu_0 / epsilon_0) * np.arccosh(D / d)
    
    print(f"双导线: d={d*1e3:.1f}mm, D={D*1e3:.1f}mm")
    print(f"特性阻抗 Z0 = {Z0:.4f} Ω")
    print(f"  D/d = {D/d:.2f}")
    print(f"  arccosh(D/d) = {np.arccosh(D/d):.4f}")
    
    return Z0


# ============================================================
# 例题 2.6: 有耗线衰减常数
# ============================================================

def example_conductor_loss():
    """
    例题: 矩形波导 (a×b) 中的导体衰减
    已知: a=22.86mm, b=10.16mm (X-band), 铜导体, f=10 GHz
    
    对于 TEM 线: α_c = Rs/(2*Z0*b)  [理想导体近似]
    """
    a = 22.86e-3   # X-band broad dimension
    b = 10.16e-3   # X-band narrow dimension
    f = 10e9
    sigma = 5.8e7  # Copper conductivity
    mu_r = 1.0
    
    mu_0 = 4e-7 * np.pi
    epsilon_0 = 8.854e-12
    
    # 集肤深度
    omega = 2 * np.pi * f
    delta = np.sqrt(2 / (omega * mu_0 * mu_r * sigma))
    
    # 表面电阻 Rs = 1/(σδ) = sqrt(πfμ/σ)
    Rs = np.sqrt(np.pi * f * mu_0 * mu_r / sigma)
    
    print(f"X-band 矩形波导: a={a*1e3:.2f}mm, b={b*1e3:.2f}mm")
    print(f"频率 f = {f/1e9:.1f} GHz")
    print(f"集肤深度 δ = {delta*1e6:.4f} μm")
    print(f"表面电阻 Rs = {Rs:.4f} Ω")
    
    # 同轴线导体衰减
    # 对于同轴线: α_c = Rs/(2π) * (1/r1 + 1/r2) / Z0*ln(r2/r1)
    r1 = 1e-3
    r2 = 3.5e-3
    Z0 = (1/(2*np.pi)) * np.sqrt(mu_0/epsilon_0) * np.log(r2/r1)
    
    alpha_c = Rs / (2 * np.pi) * (1/r1 + 1/r2) / Z0 / np.log(r2/r1)
    print(f"\n同轴线导体衰减 (r1={r1*1e3:.1f}mm, r2={r2*1e3:.1f}mm):")
    print(f"  Z0 = {Z0:.4f} Ω")
    print(f"  α_c = {alpha_c:.6f} Np/m = {alpha_c*8.686:.4f} dB/m")
    
    return delta, Rs


if __name__ == '__main__':
    print("=" * 60)
    print(" 梁昌洪《简明微波》第二章 - 传输线理论 例题")
    print("=" * 60)
    
    print("\n--- 例题 2.1: 同轴线特性阻抗 ---")
    example_coaxial_Z0()
    
    print("\n--- 例题 2.2: 有耗线传播常数 ---")
    example_lossy_line()
    
    print("\n--- 例题 2.3: 反射系数与VSWR ---")
    example_reflection_coefficient()
    
    print("\n--- 例题 2.4: 沿线输入阻抗分布 (生成图) ---")
    example_Zin_along_line()
    
    print("\n--- 例题 2.5: 双导线特性阻抗 ---")
    example_twin_lead()
    
    print("\n--- 例题 2.6: 导体衰减与集肤深度 ---")
    example_conductor_loss()