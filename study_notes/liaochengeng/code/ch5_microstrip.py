"""
第5章 微波集成传输线 / 第3章微带部分 - 代码复现
廖承恩《微波技术基础》

微带线特性参数计算
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, mu_0, epsilon_0, pi

# ============================================================================
# 微带线特性参数
# ============================================================================

def epsilon_effective(w, h, epsilon_r):
    """
    微带线有效介电常数 (Hammerstad 公式)
    w: 导体带宽度
    h: 基片厚度
    epsilon_r: 介质相对介电常数
    """
    u = w / h
    # 宽导体带 (u >= 1)
    term1 = (epsilon_r + 1) / 2
    term2 = (epsilon_r - 1) / 2 * (1 + 10/u)**(-0.555 * np.sqrt(epsilon_r) * u)
    return term1 * term2

def Z0_microstrip_full(w, h, epsilon_r):
    """
    微带线特性阻抗 (完整公式, 适用于任意 w/h)
    基于准静态解
    """
    u = w / h
    eps_e = epsilon_effective(w, h, epsilon_r)

    if u < 1.0:
        # 窄带 (u < 1)
        Z0_val = 60.0 / np.sqrt(eps_e) * np.log(8/u + u/4)
    else:
        # 宽带 (u >= 1)
        Z0_val = (60.0 * pi / np.sqrt(eps_e)) / (u + 1.5 + 2/u)
    return Z0_val

def Z0_microstrip_narrow(w, h, epsilon_r):
    """微带线特性阻抗 (窄带公式, w/h < 1)"""
    eps_e = epsilon_effective(w, h, epsilon_r)
    u = w / h
    return (60.0 / np.sqrt(eps_e)) * np.log(8/u + u/4)

def Z0_microstrip_wide(w, h, epsilon_r):
    """微带线特性阻抗 (宽带公式, w/h >= 2)"""
    eps_e = epsilon_effective(w, h, epsilon_r)
    u = w / h
    return (60.0 * pi / np.sqrt(eps_e)) / (u + 1.5 + 2/u)

def lambda_microstrip(f, w, h, epsilon_r):
    """微带线工作波长"""
    eps_e = epsilon_effective(w, h, epsilon_r)
    lambda_0 = c / f
    return lambda_0 / np.sqrt(eps_e)

def vp_microstrip(w, h, epsilon_r):
    """微带线相速度"""
    eps_e = epsilon_effective(w, h, epsilon_r)
    return c / np.sqrt(eps_e)

def beta_microstrip(f, w, h, epsilon_r):
    """微带线相位常数"""
    lambda_g = lambda_microstrip(f, w, h, epsilon_r)
    return 2 * pi / lambda_g

def w_for_Z0_target(Z0_target, h, epsilon_r, tol=0.1):
    """
    已知目标特性阻抗, 求解所需微带线导体带宽度
    用数值迭代
    """
    def objective(w):
        return Z0_microstrip_full(w, h, epsilon_r) - Z0_target

    # 初始猜测
    if Z0_target > 50:
        w_guess = h * 2.0
    else:
        w_guess = h * 1.0

    # 简单二分法
    w_low = h * 0.01
    w_high = h * 10.0

    for _ in range(50):
        w_mid = (w_low + w_high) / 2
        Z0_mid = Z0_microstrip_full(w_mid, h, epsilon_r)
        if abs(Z0_mid - Z0_target) < tol:
            return w_mid
        if Z0_mid > Z0_target:
            w_low = w_mid
        else:
            w_high = w_mid

    return w_mid

# ============================================================================
# 微带不连续性补偿
# ============================================================================

def delta_w_microstrip(w, h, epsilon_r):
    """
    微带线宽度增量补偿 (窄导体带)
    由于边缘电容效应, 电气宽度比物理宽度大
    """
    u = w / h
    term1 = (epsilon_r + 1) / 2
    term2 = epsilon_r / (epsilon_r + 1)
    term3 = np.log(2) / np.pi
    term4 = 1 / (2 * u**2)
    return h * term1 * term2 * term3 * term4

# ============================================================================
# 损耗计算
# ============================================================================

def alpha_c_microstrip(f, w, h, sigma=None, rho_r=1.0):
    """
    微带线导体损耗 (Np/m)
    sigma: 导体电导率 (S/m), 默认用铜
    rho_r: 相对于铜的电阻率
    """
    if sigma is None:
        sigma = 5.8e7  # 铜的电导率
    if rho_r != 1.0:
        sigma = sigma / rho_r

    mu = mu_0
    delta_s = np.sqrt(2 / (omega(f) * mu * sigma))  # 趋肤深度
    # 简化公式
    R_s = 1 / (sigma * delta_s)
    # 单位长度电阻 (简化)
    alpha_c_val = R_s / (2 * 50.0)  # 近似
    return alpha_c_val

def alpha_d_microstrip(f, epsilon_r, tan_delta=1e-4):
    """
    微带线介质损耗 (Np/m)
    tan_delta: 损耗角正切
    """
    omega_val = omega(f)
    eps_e = epsilon_r  # 近似
    alpha_d_val = (omega_val * np.sqrt(mu_0 * epsilon_0 * epsilon_r) * tan_delta) / (2)
    return alpha_d_val

def omega(f):
    """角频率"""
    return 2 * pi * f

# ============================================================================
# 绘图
# ============================================================================

if __name__ == "__main__":
    # 示例: 氧化铝微带线 (epsilon_r = 9.6)
    h = 1.27e-3  # 1.27 mm 基片
    epsilon_r = 9.6

    print("微带线特性阻抗计算示例:")
    print(f"基片厚度 h = {h*1e3:.2f} mm, epsilon_r = {epsilon_r}")

    widths = [0.5e-3, 1.0e-3, 2.0e-3, 3.0e-3]  # 不同宽度
    print(f"\n{'w (mm)':<10} {'w/h':<8} {'eps_e':<10} {'Z0 (Ohm)':<12} {'v_p (m/s)':<14}")
    print("-" * 60)

    for w in widths:
        u = w / h
        eps_e = epsilon_effective(w, h, epsilon_r)
        Z0_val = Z0_microstrip_full(w, h, epsilon_r)
        vp_val = vp_microstrip(w, h, epsilon_r)
        print(f"{w*1e3:<10.2f} {u:<8.2f} {eps_e:<10.3f} {Z0_val:<12.2f} {vp_val*1e-6:<14.4f}")

    # 绘图: Z0 vs w/h
    w_range = np.linspace(h * 0.1, h * 5, 100)
    u_range = w_range / h
    Z0_range = [Z0_microstrip_full(wi, h, epsilon_r) for wi in w_range]

    plt.figure(figsize=(8, 5))
    plt.plot(u_range, Z0_range, 'b-', linewidth=2)
    plt.axhline(y=50, color='r', linestyle='--', label='50 Ohm')
    plt.axhline(y=75, color='g', linestyle='--', label='75 Ohm')
    plt.xlabel('$w/h$')
    plt.ylabel('$Z_0$ (Ohm)')
    plt.title('微带线特性阻抗 vs 宽高比 (氧化铝基片, $\\epsilon_r=9.6$)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liaochengeng/figures/ch5_microstrip_Z0.png', dpi=150)
    plt.close()
    print("\n微带线阻抗曲线已保存")
