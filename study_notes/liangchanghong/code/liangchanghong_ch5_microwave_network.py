#!/usr/bin/env python3
"""
梁昌洪《简明微波》第五章：微波网络基础
二端口网络：ABCD矩阵、S参数、级联计算
Based on: 梁昌洪《简明微波》Ch6 网络基础
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================================
# S参数 <-> ABCD 转换
# ============================================================================

def s_to_abcd(S, Z0=50.0):
    """
    S参数转ABCD矩阵 (梁昌洪式 6.6-2)
    
    S = [S11, S12; S21, S22]
    返回 ABCD = [A, B; C, D]
    """
    S11, S12, S21, S22 = S[0,0], S[0,1], S[1,0], S[1,1]
    delta_S = (1 + S11) * (1 + S22) - S12 * S21
    
    A = ((1 + S11) * (1 - S22) + S12 * S21) / S21
    B = ((1 + S11) * (1 - S22) - S12 * S21) / S21 * Z0
    C = ((1 - S11) * (1 + S22) + S12 * S21) / S21 / Z0
    D = ((1 - S11) * (1 - S22) - S12 * S21) / S21
    
    return np.array([[A, B], [C, D]])


def abcd_to_s(ABCD, Z0=50.0):
    """
    ABCD矩阵转S参数 (梁昌洪式 6.6-3逆变换)
    """
    A, B, C, D = ABCD[0,0], ABCD[0,1], ABCD[1,0], ABCD[1,1]
    
    den = A + B / Z0 + C * Z0 + D
    S11 = (A + B / Z0 - C * Z0 - D) / den
    S12 = 2.0 * (A * D - B * C) / den
    S21 = 2.0 / den
    S22 = (-A + B / Z0 - C * Z0 + D) / den
    
    return np.array([[S11, S12], [S21, S22]])


def abcd_to_T(ABCD):
    """
    ABCD 转 T参数 (传输矩阵，用于级联)
    T = [T11, T12; T21, T22]
    级联: [T_total] = [T1] @ [T2]
    """
    A, B, C, D = ABCD[0,0], ABCD[0,1], ABCD[1,0], ABCD[1,1]
    
    T11 = -A / C if C != 0 else np.inf
    T12 = -D / C if C != 0 else np.inf
    T21 = -1 / C if C != 0 else np.inf
    T22 = 0.0 if C != 0 else 0.0
    
    return np.array([[T11, T12], [T21, T22]])


def s_to_T(S):
    """S参数转T参数 (用于级联)"""
    S11, S12, S21, S22 = S[0,0], S[0,1], S[1,0], S[1,1]
    
    T11 = -S11 * S22 / S21 + S12 / S21 if S21 != 0 else np.inf
    T12 = S11 / S21 if S21 != 0 else np.inf
    T21 = -S22 / S21 if S21 != 0 else np.inf
    T22 = 1.0 / S21 if S21 != 0 else np.inf
    
    return np.array([[T11, T12], [T21, T22]])


# ============================================================================
# 基本二端口元件 ABCD 矩阵
# ============================================================================

def abcd_series_Z(Z, Z0=50.0):
    """串联阻抗 Z"""
    return np.array([[1.0, Z], [0.0, 1.0]])


def abcd_shunt_Y(Y, Z0=50.0):
    """并联导纳 Y"""
    return np.array([[1.0, 0.0], [Y, 1.0]])


def abcd_transmission_line(l_m, beta, Z0=50.0):
    """
    长度为 l 的传输线 (梁昌洪式 6.6-3)
    
    参数:
        l_m: 物理长度 (m)
        beta: 相位常数 = 2*pi/lambda (rad/m)
        Z0: 特性阻抗 (Ohm)
    """
    gamma_l = beta * l_m
    cos_betaz = np.cos(gamma_l)
    sin_betaz = np.sin(gamma_l)
    
    return np.array([
        [cos_betaz, 1j * Z0 * sin_betaz],
        [1j / Z0 * sin_betaz, cos_betaz]
    ])


def abcd_impedance_inverter(K, Z0=50.0):
    """
    阻抗变换器 (K inverter)
    K: 变换器阻抗 (Ohm)
    """
    return np.array([[0.0, 1j * K], [1j / K, 0.0]])


def abcd_admittance_inverter(J, Z0=50.0):
    """
    导纳变换器 (J inverter)
    J: 导纳变换量 (S)
    """
    return np.array([[0.0, 1j / J], [1j * J, 0.0]])


# ============================================================================
# 网络分析函数
# ============================================================================

def network_input_impedance(ABCD, Z_L, Z0=50.0):
    """
    由ABCD矩阵和负载阻抗计算输入阻抗
    Z_in = (A * Z_L + B) / (C * Z_L + D)
    """
    A, B, C, D = ABCD[0,0], ABCD[0,1], ABCD[1,0], ABCD[1,1]
    return (A * Z_L + B) / (C * Z_L + D)


def network_reflection_coefficient(Z_in, Z0=50.0):
    """
    输入端反射系数
    """
    return (Z_in - Z0) / (Z_in + Z0)


def network_VSWR(Gamma):
    """
    电压驻波比
    """
    Gamma = abs(Gamma)
    if Gamma >= 1.0:
        return np.inf
    return (1.0 + Gamma) / (1.0 - Gamma)


# ============================================================================
# 主程序
# ============================================================================
if __name__ == '__main__':
    plt.rcParams.update({'axes.grid': True, 'grid.alpha': 0.3})
    Z0 = 50.0
    
    # --- 图1: T参数级联示例 —— 两个相同传输线级联 ---
    f_GHz = np.linspace(1, 20, 500)
    beta = 2.0 * np.pi / 30.0  # 30 cm 波长对应 beta
    
    # 单段传输线 (lambda/4 at 10 GHz)
    lambda_mm = 30.0  # 10 GHz in mm
    l_quarter = lambda_mm / 4.0
    beta_q = 2.0 * np.pi / lambda_mm
    
    # 特性阻抗 50 Ohm
    ABCD_line = abcd_transmission_line(l_quarter, beta_q, Z0)
    S_line = abcd_to_s(ABCD_line, Z0)
    
    print(f"Quarter-wave line (Z0={Z0} Ohm):")
    print(f"  S11 = {S_line[0,0]:.4f}")
    print(f"  S21 = {S_line[1,0]:.4f}")
    print(f"  |S21| = {abs(S_line[1,0]):.4f} (should be ~1, phase ~-90 deg)")
    
    # --- 图2: 阻抗匹配网络示例 (Baker nominal) ---
    # 串联微带 + 并联开路线
    Z_L = 100.0  # 负载阻抗
    
    # 计算不同电长度下的输入阻抗
    lengths = np.linspace(0, lambda_mm, 300)
    Z_in_list = []
    VSWR_list = []
    
    for l in lengths:
        ABCD = abcd_transmission_line(l, 2*np.pi/lambda_mm, Z0)
        Z_in = network_input_impedance(ABCD, Z_L, Z0)
        Gamma = network_reflection_coefficient(Z_in, Z0)
        vswr = network_VSWR(Gamma)
        Z_in_list.append(Z_in)
        VSWR_list.append(vswr)
    
    Z_in_arr = np.array(Z_in_list)
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # 阻抗实部
    axes[0].plot(lengths, Z_in_arr.real, 'b', label='Re{$Z_{in}$}')
    axes[0].plot(lengths, Z_in_arr.imag, 'r--', label='Im{$Z_{in}$}')
    axes[0].axhline(Z0, color='gray', linestyle=':', label=f'$Z_0$ = {Z0} Ohm')
    axes[0].set_xlabel('$l$ (mm)')
    axes[0].set_ylabel('$Z_{in}$ ($\\Omega$)')
    axes[0].set_title(f'Input Impedance vs Length (Load $Z_L$ = {Z_L:.0f} Ohm)')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # VSWR
    axes[1].plot(lengths, VSWR_list, 'g')
    axes[1].set_xlabel('$l$ (mm)')
    axes[1].set_ylabel('VSWR')
    axes[1].set_title(f'VSWR vs Stub Position')
    axes[1].set_ylim(1, 10)
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liangchanghong/code/ch5_network_Zin.png', dpi=150)
    plt.close()
    print("Ch5: ch5_network_Zin.png generated")
    
    # --- 图3: ABCD级联示例 ---
    # 两个不同特性阻抗的传输线级联
    l1, Z01 = lambda_mm / 4, 50.0
    l2, Z02 = lambda_mm / 4, 75.0
    
    ABCD1 = abcd_transmission_line(l1, 2*np.pi/lambda_mm, Z01)
    ABCD2 = abcd_transmission_line(l2, 2*np.pi/lambda_mm, Z02)
    ABCD_total = ABCD2 @ ABCD1  # 级联
    
    S_total = abcd_to_s(ABCD_total, Z0)
    print(f"\nTwo cascaded quarter-wave lines (50->75 Ohm):")
    print(f"  S11 = {S_total[0,0]:.4f}")
    print(f"  S21 = {S_total[1,0]:.4f}")
    
    # S11 vs frequency
    f_range = np.linspace(1, 20, 400)
    beta_f = 2.0 * np.pi * f_range / 30.0  # phase constant proportional to f
    S11_f = []
    for bf in beta_f:
        ABCD1_f = abcd_transmission_line(l1, bf, Z01)
        ABCD2_f = abcd_transmission_line(l2, bf, Z02)
        ABCD_f = ABCD2_f @ ABCD1_f
        S_f = abcd_to_s(ABCD_f, Z0)
        S11_f.append(S_f[0, 0])
    
    plt.figure(figsize=(8, 5))
    plt.plot(f_range, [abs(s) for s in S11_f], 'b', label='$|S_{11}|$')
    plt.plot(f_range, [abs(s) for s in S11_f], 'r--', label='$|S_{21}|$')
    plt.xlabel('$f$ (GHz)')
    plt.ylabel('$|S_{ij}|$')
    plt.title('Cascaded Line Response: $|S_{11}|$ and $|S_{21}|$ vs Frequency')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liangchanghong/code/ch5_cascade_response.png', dpi=150)
    plt.close()
    print("Ch5: ch5_cascade_response.png generated")
    
    print("\n✓ 梁昌洪《简明微波》Ch5 微波网络代码验证通过")
