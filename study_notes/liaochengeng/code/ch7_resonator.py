"""
第7章 微波谐振器 - 代码复现
廖承恩《微波技术基础》

串联/并联谐振电路、腔体谐振器、品质因数
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, mu_0, epsilon_0, pi

# ============================================================================
# 7.2 串联和并联谐振电路
# ============================================================================

def f_resonance_series(L, C):
    """串联谐振频率"""
    return 1 / (2 * pi * np.sqrt(L * C))

def f_resonance_parallel(L, C):
    """并联谐振频率"""
    return 1 / (2 * pi * np.sqrt(L * C))

def Q_series(L, R, omega_0):
    """串联谐振电路品质因数"""
    return omega_0 * L / R

def Q_parallel(C, G, omega_0):
    """并联谐振电路品质因数 (G=1/R)"""
    return omega_0 * C / G

def Z_series(f, L, R, C):
    """
    串联谐振电路阻抗
    Z = R + j*(omega*L - 1/(omega*C))
    """
    omega = 2 * pi * f
    X = omega * L - 1 / (omega * C)
    return R + 1j * X

def Y_parallel(f, L, R, C):
    """
    并联谐振电路导纳
    Y = G + j*(omega*C - 1/(omega*L))
    """
    G = 1.0 / R
    omega = 2 * pi * f
    B = omega * C - 1 / (omega * L)
    return G + 1j * B

def bandwidth(Q, f_0):
    """带宽"""
    return f_0 / Q

def VSWR_at_resonance(Q_L, delta_f, f_0):
    """
    谐振器附近 VSWR 频率响应
    delta_f: 频率偏移
    """
    delta_omega = 2 * pi * delta_f
    omega_0 = 2 * pi * f_0
    Q_factor = Q_L
    return np.sqrt(1 + Q_factor**2 * (delta_omega / omega_0)**2)

# ============================================================================
# 7.3 金属波导谐振腔
# ============================================================================

def f_resonator_rectangular(m, n, p, a, b, d, epsilon_r=1.0):
    """
    矩形谐振腔谐振频率
    TE_mnp 或 TM_mnp
    f_mnp = (c/2) * sqrt((m/a)^2 + (n/b)^2 + (p/d)^2) / sqrt(epsilon_r)
    """
    return (c / (2 * np.sqrt(epsilon_r))) * np.sqrt((m/a)**2 + (n/b)**2 + (p/d)**2)

def lambda_resonator_rectangular(m, n, p, a, b, d, epsilon_r=1.0):
    """矩形谐振腔谐振波长"""
    f_0 = f_resonator_rectangular(m, n, p, a, b, d, epsilon_r)
    return c / (f_0 * np.sqrt(epsilon_r))

def Q_conductor_rectangular(a, b, d, f_0, sigma=None, mu_r=1.0):
    """
    矩形谐振腔导体损耗品质因数 (近似)
    Q ~ (1/delta_s) * (V/S)  关系
    简化: Q ~ (1/alpha_c) * (2*pi/lambda_g)
    delta_s: 趋肤深度
    """
    if sigma is None:
        sigma = 5.8e7  # 铜

    mu = mu_r * mu_0
    delta_s = np.sqrt(2 / (2 * pi * f_0 * mu * sigma))

    # 表面积和体积
    V = a * b * d
    S = 2 * (a*b + a*d + b*d)
    return (1 / delta_s) * (V / S) * 2  # 经验系数

def f_resonator_coaxial(m, n, l, a, b, epsilon_r=1.0):
    """
    同轴谐振腔谐振频率
    TE_mn 模式
    m: 角向模式数
    n: 径向模式数
    l: 纵向半波长数
    """
    # 同轴线 TEM 模
    if m == 0 and n == 0:
        # TEM 模 (主模)
        return c / (2 * np.sqrt(epsilon_r) * l)  # l/2 波长谐振

    # TE/TM 模近似
    chi = 3.0  # 近似根值
    lambda_c = 2 * np.pi * (a - b) / chi  # 近似
    # 简化: 用矩形波导近似
    return c / (2 * np.sqrt(epsilon_r)) * chi / (a - b)

# ============================================================================
# 7.4 介质谐振器
# ============================================================================

def f_DRO_TE01delta(epsilon_r, D, l, mu_r=1.0):
    """
    圆柱介质谐振器 TE01delta 模式
    D: 介质圆柱直径
    l: 高度
    近似公式:
    f_GHz = 67 / (D_mm * sqrt(epsilon_r))
    """
    D_mm = D * 1e3
    return 67.0 / (D_mm * np.sqrt(epsilon_r)) * 1e9  # Hz

def Q_DRO(epsilon_r, tan_delta=1e-4):
    """
    介质谐振器无载 Q (近似)
    TE01delta 模式 Q 可达 10^4 量级
    """
    return 1 / tan_delta

def f_DRO_cylindrical(m, epsilon_r, D, l, mode='TE01delta'):
    """
    圆柱介质谐振器谐振频率 (准静态近似)
    """
    D_mm = D * 1e3
    l_mm = l * 1e3

    if mode == 'TE01delta':
        # 经验公式
        return 34.0 * (c / 1e9) / (D_mm * np.sqrt(epsilon_r))
    elif mode == 'TM01delta':
        return 50.0 * (c / 1e9) / (D_mm * np.sqrt(epsilon_r))
    else:
        return 34.0 * (c / 1e9) / (D_mm * np.sqrt(epsilon_r))

# ============================================================================
# 7.5 品质因数计算
# ============================================================================

def Q_unloaded(f_0, P_loss, W_stored):
    """
    无载品质因数
    Q_U = omega_0 * W_stored / P_loss
    """
    omega_0 = 2 * pi * f_0
    return omega_0 * W_stored / P_loss

def Q_external(f_0, P_forward):
    """外部品质因数"""
    omega_0 = 2 * pi * f_0
    return omega_0 / (2 * pi * f_0)  # 简化

def Q_loaded(Q_U, Q_e):
    """
    有载品质因数
    1/Q_L = 1/Q_U + 1/Q_e
    """
    return 1 / (1/Q_U + 1/Q_e)

def coupling_coefficient(Q_U, Q_e):
    """耦合系数"""
    return Q_U / Q_e

def VSWR_from_Q(Q_L, delta_f, f_0):
    """有载谐振器 VSWR 响应"""
    delta_omega = 2 * pi * delta_f
    omega_0 = 2 * pi * f_0
    return np.sqrt(1 + Q_L**2 * (delta_omega / omega_0)**2)

def reflection_coefficient_near_resonance(f, f_0, Q_L, Gamma_max=0.9):
    """
    谐振器附近反射系数 (一阶近似)
    """
    delta_f = f - f_0
    denom = 1 + 2j * Q_L * delta_f / f_0
    return Gamma_max * (denom - 1) / (denom + 1)

# ============================================================================
# 绘图
# ============================================================================

if __name__ == "__main__":
    # 示例: 串联谐振电路
    L = 1.0e-9   # 1 nH
    C = 1.0e-12  # 1 pF
    R = 5.0      # 5 Ohm
    f_0 = f_resonance_series(L, C)
    Q = Q_series(L, R, 2 * pi * f_0)
    BW = bandwidth(Q, f_0)

    print(f"串联谐振电路:")
    print(f"f_0 = {f_0*1e-9:.2f} GHz")
    print(f"Q = {Q:.1f}")
    print(f"带宽 BW = {BW*1e-6:.2f} MHz")

    # 频率扫描
    f_range = np.linspace(f_0 * 0.95, f_0 * 1.05, 1000)
    Z_range = [Z_series(fi, L, R, C) for fi in f_range]
    Z_abs_range = [np.abs(z) for z in Z_range]

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.semilogy(f_range * 1e-9, Z_abs_range, 'b-', linewidth=2)
    plt.axvline(f_0 * 1e-9, color='r', linestyle='--', label=f'$f_0$={f_0*1e-9:.2f} GHz')
    plt.xlabel('频率 (GHz)')
    plt.ylabel('|$Z$| (Ohm)')
    plt.title('串联谐振电路阻抗响应')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # 矩形谐振腔
    a = 22.86e-3   # WR-90 波导尺寸
    b = 10.16e-3
    d = 19.05e-3   # 腔长
    modes = [(1,0,1), (1,0,2), (2,0,1)]
    print(f"\n矩形谐振腔 (a={a*1e3:.2f}mm, b={b*1e3:.2f}mm, d={d*1e3:.2f}mm):")
    print(f"{'模式':<10} {'f_0 (GHz)':<15}")
    for (m,n,p) in modes:
        f_0_val = f_resonator_rectangular(m, n, p, a, b, d)
        print(f"TE{m}{n}{p:<3} {f_0_val*1e-9:<15.3f}")

    plt.subplot(1, 2, 2)
    f_vals = [f_resonator_rectangular(m, n, p, a, b, d) * 1e-9 for (m, n, p) in modes]
    plt.bar([f'{m}{n}{p}' for (m,n,p) in modes], f_vals, color='steelblue')
    plt.xlabel('模式')
    plt.ylabel('谐振频率 (GHz)')
    plt.title('矩形谐振腔模式')
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liaochengeng/figures/ch7_resonator.png', dpi=150)
    plt.close()
    print("\n谐振器图已保存")
