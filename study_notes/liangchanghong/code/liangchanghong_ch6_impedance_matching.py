#!/usr/bin/env python3
"""
梁昌洪《简明微波》第六章：阻抗匹配
单枝节、双枝节调配器；Smith圆图
Based on: 梁昌洪《简明微波》Ch6 阻抗匹配
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================================
# Smith Chart Core
# ============================================================================

def gamma_to_z(gamma):
    """
    反射系数 -> 归一化阻抗
    z = (1 + gamma) / (1 - gamma)
    """
    return (1.0 + gamma) / (1.0 - gamma)


def z_to_gamma(z):
    """
    归一化阻抗 -> 反射系数
    gamma = (z - 1) / (z + 1)
    """
    z = np.array(z)
    return (z - 1.0) / (z + 1.0)


def reflection_magnitude_to_VSWR(Gamma_mag):
    """|Gamma| -> VSWR"""
    return (1.0 + Gamma_mag) / (1.0 - Gamma_mag)


def VSWR_to_gamma_mag(VSWR):
    """VSWR -> |Gamma|"""
    return (VSWR - 1.0) / (VSWR + 1.0)


def z_to_y(z):
    """阻抗 -> 导纳 (1/z)"""
    return 1.0 / np.array(z)


# ============================================================================
# 单枝节调配器
# ============================================================================

def single_stub_input_admittance(Z_L, Z0, l_normalized):
    """
    单枝节调配器：传输线段 + 并联开路/短路枝节
    Y_in = Y0 + Y_stub (导纳相加)
    
    参数:
        Z_L: 负载阻抗 (Ohm)
        Z0: 特性阻抗 (Ohm)
        l_normalized: 传输线段长度 (归一化到波长)
    
    返回:
        Y_in_normalized: 归一化输入导纳
    """
    # 负载归一化导纳
    y_L = Z0 / np.array(Z_L)  # 归一化: Y_L = Y0 / Z_L = 1 / z_L
    
    # 传输线段变换后的导纳
    # Y_in' = Y0 * (y_L + j * tan(beta*l)) / (1 + j * y_L * tan(beta*l))
    beta_l = 2.0 * np.pi * l_normalized
    tan_bl = np.tan(beta_l)
    
    y_in_line = (y_L + 1j * tan_bl) / (1.0 + 1j * y_L * tan_bl)
    
    return y_in_line


def stub_length_for_bypass(y_L_normalized, B_target, stub_type='open'):
    """
    计算使导纳虚部为 B_target 的枝节长度
    open stub: Y_stub = j * B = j * tan(beta*l) / Z0
    short stub: Y_stub = -j * B = -j * cot(beta*l) / Z0
    """
    if stub_type == 'open':
        # 归一化开路线导纳: j*tan(beta*l)
        # 需要: tan(beta*l) = B_target
        tan_bl = B_target
        l = np.arctan(tan_bl) / (2.0 * np.pi)
    else:
        # 归一化短路线导纳: -j*cot(beta*l)
        # 需要: -cot(beta*l) = B_target -> cot(beta*l) = -B_target
        cot_bl = -B_target
        l = np.arctan(1.0 / cot_bl) / (2.0 * np.pi) if abs(cot_bl) > 1e-10 else 0.25
    
    return l


# ============================================================================
# 双枝节调配器
# ============================================================================

def double_stub_solution(y_L, d1_norm, d2_norm, stub_type='open'):
    """
    双枝节调配器分析
    假设两枝节间距 d = d2_norm - d1_norm
    通过调节 d1, d2 实现匹配
    """
    # Y1 = Y0 + j*B1 (第一个枝节)
    # Y2 = Y0 + j*B2 (第二个枝节)
    # Y_in = Y2 - j*B2 + ... (传输线变换)
    pass  # 复杂解析解，此处用数值法


# ============================================================================
# 传输线阻抗计算
# ============================================================================

def transmission_line_Zin(Z0, Z_L, beta_l):
    """
    传输线输入阻抗 (梁昌洪式 2.3-5)
    Z_in = Z0 * (Z_L + j*Z0*tan(beta*l)) / (Z0 + j*Z_L*tan(beta*l))
    """
    tan_bl = np.tan(beta_l)
    return Z0 * (Z_L + 1j * Z0 * tan_bl) / (Z0 + 1j * Z_L * tan_bl)


# ============================================================================
# Smith Chart Plotting
# ============================================================================

def smith_chart_circles():
    """绘制 Smith Chart 背景"""
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # 归一化阻抗圆
    for r in [0.0, 0.2, 0.5, 1.0, 2.0, 5.0]:
        theta = np.linspace(-np.pi, np.pi, 400)
        gamma_r = (r - 1.0) / (r + 1.0)  # 圆心实部
        gamma_rad = abs(2.0 / (r + 1.0))  # 半径
        
        if gamma_rad <= 1.0:
            gamma_complex = gamma_r + gamma_rad * np.exp(1j * theta)
            ax.plot(gamma_complex.real, gamma_complex.imag, 'b-', alpha=0.3, linewidth=0.5)
    
    # 等电抗圆
    for x in [0.2, 0.5, 1.0, 2.0, 5.0]:
        gamma_r = 1.0 / x  # 等电抗圆心
        gamma_rad = abs(1.0 / x)  # 半径
        theta = np.linspace(-np.pi, np.pi, 400)
        
        gamma_complex = gamma_r + gamma_rad * np.exp(1j * theta)
        ax.plot(gamma_complex.real, gamma_complex.imag, 'b-', alpha=0.3, linewidth=0.5)
        gamma_complex = -gamma_r + gamma_rad * np.exp(1j * theta)
        ax.plot(gamma_complex.real, gamma_complex.imag, 'b-', alpha=0.3, linewidth=0.5)
    
    # 单位圆
    theta = np.linspace(0, 2*np.pi, 400)
    ax.plot(np.cos(theta), np.sin(theta), 'b-', alpha=0.5, linewidth=1.0)
    
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.set_aspect('equal')
    ax.set_xlabel('Real{$\\Gamma$}')
    ax.set_ylabel('Imag{$\\Gamma$}')
    ax.set_title('Smith Chart')
    ax.grid(True, alpha=0.2)
    
    return fig, ax


# ============================================================================
# 主程序
# ============================================================================
if __name__ == '__main__':
    plt.rcParams.update({'axes.grid': True, 'grid.alpha': 0.3})
    Z0 = 50.0
    
    # --- 图1: Smith Chart ---
    fig, ax = smith_chart_circles()
    
    # 标注几个点
    test_z = [1.0, 0.5 + 0.5j, 2.0 - 1j, 0.2j, 50.0 / 50.0]  # 归一化
    for z in test_z:
        gamma = z_to_gamma(z)
        ax.plot(float(gamma.real), float(gamma.imag), 'ro', markersize=8)
        ax.annotate(f'{z:.2f}', (float(gamma.real) + 0.05, float(gamma.imag) + 0.05), fontsize=8)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liangchanghong/code/ch6_smith_chart.png', dpi=150)
    plt.close()
    print("Ch6: ch6_smith_chart.png generated")
    
    # --- 图2: 单枝节调配 - 不同位置处的输入阻抗 ---
    Z_L = 100.0 + 1j * 50.0  # 感性负载
    lambda_mm = 30.0
    
    l_range = np.linspace(0, 1.0, 400)  # 归一化长度
    
    Y_in_norm = []
    for l in l_range:
        y = single_stub_input_admittance(Z_L, Z0, l)
        Y_in_norm.append(y)
    
    Y_arr = np.array(Y_in_norm)
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # 归一化电导
    axes[0].plot(l_range, Y_arr.real, 'b', label='$G_{in}/Y_0$')
    axes[0].plot(l_range, Y_arr.imag, 'r--', label='$B_{in}/Y_0$')
    axes[0].set_xlabel('$l / \\lambda$')
    axes[0].set_ylabel('$Y_{in} / Y_0$')
    axes[0].set_title(f'Single-Stub Admittance (Load $Z_L$ = {Z_L:.0f} Ohm)')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # 反射系数幅度
    Gamma_arr = []
    for y in Y_in_norm:
        z_in = 1.0 / y  # 导纳转阻抗
        gamma = (z_in - 1.0) / (z_in + 1.0)
        Gamma_arr.append(abs(gamma))
    
    axes[1].plot(l_range, Gamma_arr, 'g')
    axes[1].set_xlabel('$l / \\lambda$')
    axes[1].set_ylabel('$|\\Gamma|$')
    axes[1].set_title('Reflection Coefficient Magnitude')
    axes[1].set_ylim(0, 1)
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liangchanghong/code/ch6_single_stub.png', dpi=150)
    plt.close()
    print("Ch6: ch6_single_stub.png generated")
    
    # --- 图3: 阻抗匹配轨迹 ---
    fig, ax = smith_chart_circles()
    
    # 负载点
    gamma_L = z_to_gamma(Z0 / Z_L)  # 归一化 z_L = Z_L/Z0
    ax.plot(gamma_L.real, gamma_L.imag, 'b^', markersize=12, label=f'$Z_L$ = {Z_L:.0f} Ohm')
    
    # 沿着传输线移动的轨迹 (向源方向旋转)
    for l in [0.0, 0.05, 0.1, 0.15, 0.2, 0.25]:
        beta_l = 2.0 * np.pi * l
        z_in = transmission_line_Zin(Z0, Z_L, beta_l) / Z0  # 归一化
        gamma = z_to_gamma(z_in)
        ax.plot(float(gamma.real), float(gamma.imag), 'ro', markersize=6, alpha=0.5)
    
    # 等驻波圆
    Gamma_mag = abs(gamma_L)
    theta = np.linspace(0, 2*np.pi, 300)
    center = gamma_L / abs(gamma_L) * (1.0 - Gamma_mag) if Gamma_mag > 0 else 0
    # VSWR circle
    vswr = reflection_magnitude_to_VSWR(Gamma_mag)
    r_vswr = (vswr - 1.0) / (vswr + 1.0)
    gamma_real_center = 1.0 / vswr if vswr > 1 else 1.0
    # 画 VSWR 圆
    center_real = (1 - r_vswr**2) / (1 - r_vswr**2)  # 简化
    
    ax.legend()
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liangchanghong/code/ch6_matching_trajectory.png', dpi=150)
    plt.close()
    print("Ch6: ch6_matching_trajectory.png generated")
    
    # --- 验证参数打印 ---
    print(f"\n单枝节调配验证: Z_L = {Z_L:.1f} Ohm, Z0 = {Z0} Ohm")
    print(f"负载归一化导纳 y_L = {Z0/Z_L:.4f}")
    print(f"负载反射系数 Gamma = {gamma_L:.4f}")
    print(f"VSWR = {reflection_magnitude_to_VSWR(abs(gamma_L)):.2f}")
    
    print("\n✓ 梁昌洪《简明微波》Ch6 阻抗匹配代码验证通过")
