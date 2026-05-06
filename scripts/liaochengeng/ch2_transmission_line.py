"""
第2章 传输线理论 - 代码复现
廖承恩《微波技术基础》
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, mu_0, epsilon_0, pi

# ============================================================================
# 2.1 传输线方程 - 特性参数计算
# ============================================================================

def Z0_coaxial(D, d, epsilon_r=1.0):
    """同轴线特性阻抗"""
    return 60.0 / np.sqrt(epsilon_r) * np.log(D / d)

def Z0_parallel_wire(D, d, epsilon_r=1.0):
    """平行双导线特性阻抗 (D >> d)"""
    return 120.0 * pi / np.sqrt(epsilon_r) * np.log(2 * D / d)

def Z0_microstrip(w, h, epsilon_r):
    """微带线特性阻抗 (准 TEM) - 简化公式"""
    if w / h > 1.0:
        return (60.0 / np.sqrt(epsilon_r)) * np.log(8 * h / w + w / (4 * h))
    else:
        return (60.0 * pi / np.sqrt(epsilon_r)) * w / h

def propagation_constant(f, epsilon_r=1.0, R_prime=0.0, G_prime=0.0, L_prime=None, C_prime=None):
    """
    传播常数 gamma = alpha + j*beta
    f: 频率 (Hz)
    """
    omega = 2 * pi * f
    if L_prime is not None and C_prime is not None:
        gamma = np.sqrt((R_prime + 1j * omega * L_prime) * (G_prime + 1j * omega * C_prime))
    else:
        # 真空/空气填充
        k0 = omega * np.sqrt(mu_0 * epsilon_0 * epsilon_r)
        gamma = 1j * k0
    return gamma

def alpha_conductor(R_prime, Z0):
    """导体衰减常数 (Np/m)"""
    return R_prime / (2 * Z0)

def alpha_dielectric(G_prime, Y0):
    """介质衰减常数 (Np/m)"""
    return G_prime / (2 * Y0)

def vp_tem(epsilon_r=1.0):
    """TEM 波相速度"""
    return c / np.sqrt(epsilon_r)

def lambda_tem(f, epsilon_r=1.0):
    """TEM 波波长"""
    return vp_tem(epsilon_r) / f

# ============================================================================
# 2.2 分布参数阻抗 & 反射系数
# ============================================================================

def Gamma_L(Z_L, Z_0):
    """终端反射系数"""
    return (Z_L - Z_0) / (Z_L + Z_0)

def Z_in_lossless(Z_0, Z_L, beta, d):
    """
    无耗线输入阻抗
    Z_in(d) = Z_0 * (Z_L + j*Z_0*tan(beta*d)) / (Z_0 + j*Z_L*tan(beta*d))
    d: 从负载向源方向的距离 (m)
    """
    tan_bd = np.tan(beta * d)
    numerator = Z_L + 1j * Z_0 * tan_bd
    denominator = Z_0 + 1j * Z_L * tan_bd
    return Z_0 * numerator / denominator

def Gamma_d(Gamma_L, beta, d):
    """
    无耗线上距离负载 d 处的反射系数
    Gamma(d) = Gamma_L * exp(-j*2*beta*d)
    """
    return Gamma_L * np.exp(-1j * 2 * beta * d)

def VSWR(Gamma):
    """电压驻波比"""
    if isinstance(Gamma, (int, float)):
        Gamma = complex(Gamma)
    gamma_abs = np.abs(Gamma)
    if gamma_abs == 1.0:
        return np.inf
    return (1 + gamma_abs) / (1 - gamma_abs)

def K_standing(Gamma):
    """行波系数"""
    gamma_abs = np.abs(Gamma)
    if gamma_abs == 1.0:
        return 0.0
    return (1 - gamma_abs) / (1 + gamma_abs)

def d_max_position(Gamma_L, beta):
    """第一个电压波腹点位置"""
    phi = np.angle(Gamma_L)
    return phi / (2 * beta)

def d_min_position(Gamma_L, beta):
    """第一个电压波谷点位置"""
    phi = np.angle(Gamma_L)
    return (phi + np.pi) / (2 * beta)

# ============================================================================
# 2.3 无耗线工作状态
# ============================================================================

def Z_in_short_circuit(Z_0, beta, d):
    """终端短路线的输入阻抗"""
    return 1j * Z_0 * np.tan(beta * d)

def Z_in_open_circuit(Z_0, beta, d):
    """终端开路线的输入阻抗"""
    return -1j * Z_0 * np.cot(beta * d)

def voltage_standing_wave(Z_0, Z_L, beta, d, V_plus):
    """
    沿线电压驻波分布
    V(d) = V+ * [1 + Gamma(d)]
    """
    Gamma_d_val = Gamma_d(Gamma_L(Z_L, Z_0), beta, d)
    return V_plus * (1 + Gamma_d_val)

def input_impedance_at_max_min(Z_0, VSWR):
    """电压波腹点和波谷点的输入阻抗"""
    R_max = Z_0 * VSWR      # 波腹点
    R_min = Z_0 / VSWR      # 波谷点
    return R_max, R_min

# ============================================================================
# 2.4 有耗线特性与计算
# ============================================================================

def P_in_lossy(V0, Gamma_0, Z_0, alpha, l):
    """
    有耗线输入功率
    P_in = |V0|^2/(2*Z_0) * (1 - |Gamma|^2 * exp(-2*alpha*l)) / (1 - exp(-2*alpha*l))
    """
    Gamma_abs = np.abs(Gamma_0)
    exp_term = np.exp(-2 * alpha * l)
    numerator = 1 - exp_term
    denominator = 1 - (Gamma_abs ** 2) * exp_term
    return (np.abs(V0) ** 2 / (2 * Z_0)) * (numerator / denominator)

def P_out_lossy(P_in, alpha, l):
    """有耗线输出功率"""
    return P_in * np.exp(-2 * alpha * l)

def efficiency_lossy(alpha, l, Gamma_abs=0.0):
    """有耗线效率"""
    return np.exp(-2 * alpha * l)

# ============================================================================
# 绘图示例
# ============================================================================

if __name__ == "__main__":
    # 示例：同轴线特性阻抗计算
    D = 7.0e-3   # 外导体直径 (m)
    d = 2.0e-3   # 内导体直径 (m)
    epsilon_r = 2.1  # 聚乙烯绝缘

    Z0 = Z0_coaxial(D, d, epsilon_r)
    print(f"同轴线特性阻抗: {Z0:.2f} Ohm")

    # 示例：微带线特性阻抗
    w = 2.0e-3   # 导体带宽度 (m)
    h = 1.27e-3  # 基片厚度 (m)
    epsilon_r_microstrip = 9.6  # 氧化铝

    Z0_ms = Z0_microstrip(w, h, epsilon_r_microstrip)
    print(f"微带线特性阻抗: {Z0_ms:.2f} Ohm")

    # 示例：反射系数与 VSWR
    Z_L = 100.0 + 1j * 50.0  # 负载阻抗
    Z_0 = 50.0              # 特性阻抗

    Gamma = Gamma_L(Z_L, Z_0)
    vswr = VSWR(Gamma)
    K = K_standing(Gamma)

    print(f"\n负载阻抗 Z_L = {Z_L:.1f} Ohm")
    print(f"特性阻抗 Z_0 = {Z_0:.1f} Ohm")
    print(f"反射系数 Γ = {Gamma:.4f} ∠ {np.degrees(np.angle(Gamma)):.1f}°")
    print(f"|Γ| = {np.abs(Gamma):.4f}")
    print(f"VSWR = {vswr:.2f}")
    print(f"行波系数 K = {K:.4f}")

    # 示例：绘制驻波分布
    f = 3.0e9          # 3 GHz
    epsilon_r_plot = 1.0
    lambda_g = lambda_tem(f, epsilon_r_plot)
    beta = 2 * np.pi / lambda_g
    Z_0_plot = 50.0
    Z_L_plot = 100.0 + 1j * 50.0

    d_range = np.linspace(0, 2 * lambda_g, 1000)
    V_list = []
    I_list = []
    Z_in_list = []

    for d_val in d_range:
        V_val = voltage_standing_wave(Z_0_plot, Z_L_plot, beta, d_val, 1.0)
        V_list.append(np.abs(V_val))
        I_val = V_val / Z_in_lossless(Z_0_plot, Z_L_plot, beta, d_val)
        I_list.append(np.abs(I_val))
        Z_in_list.append(np.abs(Z_in_lossless(Z_0_plot, Z_L_plot, beta, d_val)))

    plt.figure(figsize=(10, 6))
    plt.subplot(3, 1, 1)
    plt.plot(d_range / lambda_g, V_list, 'b-', linewidth=1.5)
    plt.ylabel('$|V(z)|$ (V)')
    plt.title('无耗传输线驻波分布 (Z_L = 100+j50 Ohm, Z_0 = 50 Ohm)')
    plt.grid(True, alpha=0.3)
    plt.subplot(3, 1, 2)
    plt.plot(d_range / lambda_g, I_list, 'r-', linewidth=1.5)
    plt.ylabel('$|I(z)|$ (A)')
    plt.grid(True, alpha=0.3)
    plt.subplot(3, 1, 3)
    plt.plot(d_range / lambda_g, Z_in_list, 'g-', linewidth=1.5)
    plt.ylabel('$|Z_{in}(z)|$ (Ohm)')
    plt.xlabel('距离 $d / \lambda_g$')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liaochengeng/figures/ch2_standing_wave.png', dpi=150)
    plt.close()
    print("\n驻波分布图已保存")
