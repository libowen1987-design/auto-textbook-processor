"""
第3章 规则金属波导 - 代码复现
廖承恩《微波技术基础》

矩形波导、圆波导的模式分析
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, mu_0, epsilon_0, pi

ETA_0 = np.sqrt(mu_0 / epsilon_0)

# ============================================================================
# 3.1 矩形波导
# ============================================================================

def k0(f, epsilon_r=1.0):
    """自由空间波数"""
    omega = 2 * pi * f
    return omega * np.sqrt(mu_0 * epsilon_0 * epsilon_r)

def lambda_c_rectangular(m, n, a, b):
    """
    矩形波导截止波长
    m, n: 模式指数
    a, b: 波导尺寸 (a > b)
    """
    if m == 0 and n == 0:
        return np.inf
    return 2.0 / np.sqrt((m / a)**2 + (n / b)**2)

def f_c_rectangular(m, n, a, b, epsilon_r=1.0):
    """矩形波导截止频率"""
    return c / (2 * np.sqrt(epsilon_r)) * np.sqrt((m / a)**2 + (n / b)**2)

def beta_rectangular(f, m, n, a, b, epsilon_r=1.0):
    """
    矩形波导传播常数 (TE/TM)
    f: 工作频率
    m, n: 模式指数
    """
    k = k0(f, epsilon_r)
    k_c = 2 * pi / lambda_c_rectangular(m, n, a, b)
    if k > k_c:
        return np.sqrt(k**2 - k_c**2)  # 传播
    else:
        return 1j * np.sqrt(k_c**2 - k**2)  # 截止

def lambda_g_rectangular(f, m, n, a, b, epsilon_r=1.0):
    """波导波长"""
    beta = np.real(beta_rectangular(f, m, n, a, b, epsilon_r))
    if beta > 0:
        return 2 * pi / beta
    else:
        return np.inf  # 截止

def vp_rectangular(f, m, n, a, b, epsilon_r=1.0):
    """相速度"""
    beta = np.real(beta_rectangular(f, m, n, a, b, epsilon_r))
    omega = 2 * pi * f
    if beta > 0:
        return omega / beta
    else:
        return np.inf

def vg_rectangular(f, m, n, a, b, epsilon_r=1.0):
    """群速度"""
    beta = np.real(beta_rectangular(f, m, n, a, b, epsilon_r))
    k = k0(f, epsilon_r)
    k_c = 2 * pi / lambda_c_rectangular(m, n, a, b)
    if k > k_c:
        v_p = vp_rectangular(f, m, n, a, b, epsilon_r)
        return v_p * np.sqrt(1 - (k_c / k)**2)
    else:
        return 0.0

def Z_TE(f, m, n, a, b, epsilon_r=1.0):
    """
    TE 模波阻抗
    Z_TE = eta / sqrt(1 - (lambda/lambda_c)^2)
    """
    k = k0(f, epsilon_r)
    k_c = 2 * pi / lambda_c_rectangular(m, n, a, b)
    lambda_0 = 2 * pi / k
    lambda_c = 2 * pi / k_c
    if k > k_c:
        return ETA_0 / np.sqrt(epsilon_r) / np.sqrt(1 - (lambda_0 / lambda_c)**2)
    else:
        return 1j * ETA_0 / np.sqrt(epsilon_r) / np.sqrt(1 - (lambda_0 / lambda_c)**2)

def Z_TM(f, m, n, a, b, epsilon_r=1.0):
    """TM 模波阻抗"""
    k = k0(f, epsilon_r)
    k_c = 2 * pi / lambda_c_rectangular(m, n, a, b)
    lambda_0 = 2 * pi / k
    lambda_c = 2 * pi / k_c
    if k > k_c:
        return ETA_0 / np.sqrt(epsilon_r) * np.sqrt(1 - (lambda_0 / lambda_c)**2)
    else:
        return 1j * ETA_0 / np.sqrt(epsilon_r) * np.sqrt(1 - (lambda_0 / lambda_c)**2)

def power_rectangular_TE(f, m, n, a, b, H_0, epsilon_r=1.0):
    """
    TE_mn 模传输功率
    P = (a*b/(4*Z_TE)) * |H_0|^2 * (1+delta_m0) * (1+delta_n0)
    """
    Z_TE_val = np.real(Z_TE(f, m, n, a, b, epsilon_r))
    delta_m0 = 1.0 if m == 0 else 0.0
    delta_n0 = 1.0 if n == 0 else 0.0
    return (a * b / (4 * Z_TE_val)) * (np.abs(H_0)**2) * (1 + delta_m0) * (1 + delta_n0)

# ============================================================================
# 3.2 圆波导
# ============================================================================

def lambda_c_circular(m, n, a, mode_type='TE'):
    """
    圆波导截止波长
    m, n: 模式指数
    a: 圆波导半径
    mode_type: 'TE' 或 'TM'
    """
    # TE 模根值 (chi'_mn)
    TE_roots = {
        (0,1): 3.8317, (1,1): 1.8412, (2,1): 3.0542, (0,2): 7.0156,
        (1,2): 5.3314, (2,2): 6.7061, (0,3): 10.1735, (3,1): 4.2012,
        (1,3): 8.5361, (0,1): 3.8317, (0,2): 7.0156, (1,0): 3.8317  # TE_01
    }
    # TM 模根值 (chi_mn)
    TM_roots = {
        (0,1): 2.4048, (1,1): 3.8317, (2,1): 5.1356, (0,2): 5.5201,
        (1,2): 7.0156, (0,3): 8.6537, (1,0): 2.4048, (0,1): 2.4048
    }

    if mode_type == 'TE':
        chi = TE_roots.get((m, n), 3.8317)
    else:
        chi = TM_roots.get((m, n), 2.4048)

    return 2 * pi * a / chi

def f_c_circular(m, n, a, mode_type='TE', epsilon_r=1.0):
    """圆波导截止频率"""
    lambda_c = lambda_c_circular(m, n, a, mode_type)
    return c / (lambda_c * np.sqrt(epsilon_r))

# ============================================================================
# 绘图: 矩形波导不同模式的截止波长
# ============================================================================

if __name__ == "__main__":
    # 示例: WR-90 波导 (X波段)
    a = 22.86e-3   # 宽边 (m)
    b = 10.16e-3   # 窄边 (m)
    f = 10.0e9     # 10 GHz

    print(f"WR-90 波导尺寸: a={a*1e3:.2f} mm, b={b*1e3:.2f} mm")

    # 主模 TE10
    m, n = 1, 0
    fc = f_c_rectangular(m, n, a, b)
    lambda_c = lambda_c_rectangular(m, n, a, b)
    beta = beta_rectangular(f, m, n, a, b)
    lambda_g = lambda_g_rectangular(f, m, n, a, b)
    vp = vp_rectangular(f, m, n, a, b)
    vg = vg_rectangular(f, m, n, a, b)
    Z_TE_val = Z_TE(f, m, n, a, b)

    print(f"\nTE{m}{n} 模:")
    print(f"  截止频率 f_c = {fc*1e-9:.3f} GHz")
    print(f"  截止波长 lambda_c = {lambda_c*1e3:.2f} mm")
    print(f"  波导波长 lambda_g = {lambda_g*1e3:.2f} mm")
    print(f"  相速度 v_p = {vp*1e-6:.2f} x 10^6 m/s")
    print(f"  群速度 v_g = {vg*1e-6:.2f} x 10^6 m/s")
    print(f"  波阻抗 Z_TE = {Z_TE_val:.1f} Ohm")

    # 低阶模式列表
    modes = [(1,0), (0,1), (1,1), (2,0), (0,2), (2,1), (1,2), (2,2)]
    print("\n低阶模式截止波长:")
    print(f"{'模式':<8} {'lambda_c (mm)':<15} {'f_c (GHz)':<12} {'类型'}")
    for (m_i, n_i) in modes:
        lc = lambda_c_rectangular(m_i, n_i, a, b)
        fc_val = c / lc
        if m_i == 0 or n_i == 0:
            mode_type = "TE"
        else:
            mode_type = "TE"
        print(f"TE{m_i}{n_i:<3} {lc*1e3:<15.2f} {fc_val*1e-9:<12.2f} {mode_type}")

    # 绘图: TE10 模场结构
    x = np.linspace(0, a, 50)
    y = np.linspace(0, b, 25)
    X, Y = np.meshgrid(x, y)

    # TE10 模 Hz 场分布
    H_z = np.cos(pi * X / a)

    plt.figure(figsize=(10, 4))
    plt.pcolormesh(X * 1e3, Y * 1e3, H_z, cmap='RdBu_r', shading='auto')
    plt.colorbar(label='$H_z$')
    plt.title('矩形波导 TE$_{10}$ 模 $H_z$ 场分布')
    plt.xlabel('x (mm)')
    plt.ylabel('y (mm)')
    plt.gca().set_aspect('equal')
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liaochengeng/figures/ch3_TE10_field.png', dpi=150)
    plt.close()
    print("\nTE10 模场分布图已保存")
