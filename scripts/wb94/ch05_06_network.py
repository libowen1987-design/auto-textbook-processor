"""
第五章 毫米波介质波导与光波导 / 第六章 微波网络基础
====================================================
基于梁昌洪《简明微波》第五、六章内容

本文件覆盖：
1. 介质波导基本理论
2. 矩形介质波导的马克蒂里近似
3. 微波网络基础 (等效传输线)
4. S 参数定义与散射矩阵
5. 二端口网络 (ABCD矩阵)
6. 介质波导的波阻抗与传播特性
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import warnings
warnings.filterwarnings('ignore')

plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 13,
    'axes.labelsize': 11,
    'figure.figsize': (14, 8),
    'axes.grid': True,
    'grid.alpha': 0.3,
})

c = 3e8
epsilon_0 = 8.854e-12
mu_0 = 4e-7 * np.pi
eta_0 = np.sqrt(mu_0 / epsilon_0)  # 自由空间波阻抗 ≈ 377Ω

# ============================================================
# 1. 介质波导 - 表面波色散
# ============================================================

def dielectric_slab_cutoff(epsilon_r, d, mode='TE0'):
    """
    介质板波导的截止频率 (对称介质板, 周围为空气)
    
    参数:
        epsilon_r: 介质相对介电常数
        d: 介质板厚度 [m]
        mode: 'TE0', 'TM0', 'TE1', 'TM1'
    """
    lambda_0 = c / f
    # 截止条件 (对称介质板)
    # TE0: f_c → 0 (最低模式，无截止)
    # TM0: f_c → 0
    # TE1: 第一个高次模
    pass


def dielectric_waveguide_beta(epsilon_r_core, epsilon_r_clad, a, f):
    """
    介质圆波导 (介质棒) 的传播常数
    
    近似: 弱导条件 (n1 ≈ n2)
    β ≈ k0 * n_clad + (n1 - n2) * k0 * (something)
    """
    k0 = 2 * np.pi * f / c
    n1 = np.sqrt(epsilon_r_core)
    n2 = np.sqrt(epsilon_r_clad)
    
    # 归一化折射率差
    delta = (n1**2 - n2**2) / (2 * n1**2)
    
    # 有效折射率
    n_eff = n2 + delta * (V - 1) / V  # 简化
    # V 参数 (归一化频率)
    V = 2 * np.pi * a / lambda_0 * np.sqrt(n1**2 - n2**2)
    
    beta = k0 * n_eff
    return beta


# ============================================================
# 例题 5.1: 矩形介质波导特性
# ============================================================

def example_dielectric_waveguide():
    """
    例题: 矩形介质波导 ε_r1=12.9 (GaAs), 尺寸 a×b
    工作频率 f=100 GHz, 求各模的截止特性
    """
    epsilon_r = 12.9
    f = 100e9
    
    lambda_0 = c / f
    print(f"f = {f/1e9:.1f} GHz, λ0 = {lambda_0*1e3:.2f} mm")
    
    # 矩形介质波导的马克蒂里近似
    # 截止波长近似
    # 对于 TE_mn 模
    print(f"ε_r = {epsilon_r}, n = {np.sqrt(epsilon_r):.4f}")
    
    # 估算主模 (TE11) 的截止波长
    # λ_c ≈ 2 * a * sqrt(ε_r - 1)
    a_vals = [1e-3, 2e-3, 5e-3]  # mm scale
    for a in a_vals:
        lambda_c_est = 2 * a * np.sqrt(epsilon_r - 1)
        print(f"  a = {a*1e3:.1f} mm: λ_c(est) ≈ {lambda_c_est*1e3:.2f} mm")
    
    return None


# ============================================================
# 2. 微波网络基础 - 波导等效传输线
# ============================================================

def rectangular_waveguide_Z_TE_mn(m, n, a, b, f, epsilon_r=1.0):
    """
    矩形波导 TE_mn 模的等效特性阻抗
    
    基于模式电压和模式电流的定义
    """
    k0 = 2 * np.pi * f * np.sqrt(epsilon_r) / c
    kc = np.pi * np.sqrt((m/a)**2 + (n/b)**2)
    
    if f <= 0:
        return 0.0
    
    # β
    beta = np.sqrt(max(k0**2 - kc**2, 0))
    
    if beta == 0:
        return 0.0
    
    # TE 模波阻抗
    Z_TE = omega * mu_0 / beta
    
    return Z_TE


def rectangular_waveguide_Z_TM_mn(m, n, a, b, f, epsilon_r=1.0):
    """
    矩形波导 TM_mn 模的等效特性阻抗
    """
    k0 = 2 * np.pi * f * np.sqrt(epsilon_r) / c
    kc = np.pi * np.sqrt((m/a)**2 + (n/b)**2)
    
    if f <= 0:
        return 0.0
    
    beta = np.sqrt(max(k0**2 - kc**2, 0))
    
    if beta == 0:
        return 0.0
    
    # TM 模波阻抗
    Z_TM = beta / (omega * epsilon_0 * epsilon_r)
    
    return Z_TM


# ============================================================
# 例题 6.1: 波导等效传输线参数
# ============================================================

def example_waveguide_equivalent_circuit():
    """
    例题: X-band 波导 TE10 模, f=10 GHz
    计算等效传输线的特性阻抗和传播常数
    """
    a = 22.86e-3
    b = 10.16e-3
    f = 10e9
    
    mu_r = 1.0
    epsilon_r = 1.0
    
    omega = 2 * np.pi * f
    k0 = omega * np.sqrt(epsilon_r * epsilon_0 * mu_r * mu_0)
    
    # TE10 截止波数
    m, n = 1, 0
    kc = np.pi / a
    
    # 传播常数
    if k0 > kc:
        beta = np.sqrt(k0**2 - kc**2)
        print(f"k0 = {k0:.4f} rad/m, kc = {kc:.4f} rad/m")
        print(f"β = {beta:.4f} rad/m")
        
        # 相速度
        vp = omega / beta
        print(f"v_p = {vp/1e8:.4f} × 10⁸ m/s = {vp/c:.4f}c")
        
        # 波导波长
        lambda_g = 2 * np.pi / beta
        print(f"λ_g = {lambda_g*1e3:.2f} mm")
        
        # TE 模等效特性阻抗
        Z_TE = omega * mu_0 * mu_r / beta
        print(f"等效特性阻抗 Z_TE = {Z_TE:.2f} Ω")
    else:
        print("截止频率以下，不传输")
    
    return beta, Z_TE


# ============================================================
# 3. S 参数基础
# ============================================================

def S_to_Z(S):
    """
    S 参数转 Z 参数 (二端口)
    """
    pass


def Z_to_S(Z, Z0=50.0):
    """
    Z 参数转 S 参数 (归一化)
    """
    z = Z / Z0
    denom = (z[0,0] + 1) * (z[1,1] + 1) - z[0,1] * z[1,0]
    S11 = ((z[0,0] - 1) * (z[1,1] + 1) - z[0,1] * z[1,0]) / denom
    S12 = 2 * z[0,1] / denom
    S21 = 2 * z[0,1] / denom
    S22 = ((z[0,0] + 1) * (z[1,1] - 1) - z[0,1] * z[1,0]) / denom
    return np.array([[S11, S12], [S21, S22]])


def S_params_to_matching(S11, S21, S12, S22):
    """
    分析二端口网络的S参数特性
    """
    # 回波损耗
    RL_dB = -20 * np.log10(np.abs(S11))
    # 插入损耗
    IL_dB = -20 * np.log10(np.abs(S21))
    # VSWR
    Gamma_in = S11
    VSWR = (1 + np.abs(Gamma_in)) / (1 - np.abs(Gamma_in))
    
    return RL_dB, IL_dB, VSWR


# ============================================================
# 例题 6.2: 理想滤波器网络的S参数
# ============================================================

def example_S_parameters():
    """
    例题: 理想低通滤波器的S参数响应
    绘制频率响应曲线
    """
    # 简化: 理想 Brick Wall 低通
    f_cutoff = 3e9  # 3 GHz
    f_vals = np.linspace(0.1e9, 10e9, 500)
    
    S11_mag = []
    S21_mag = []
    
    for f in f_vals:
        if f < f_cutoff:
            S11 = 0.0  # 理想通带无反射
            S21 = 1.0
        else:
            S11 = 1.0  # 理想阻带全反射
            S21 = 0.0
        S11_mag.append(np.abs(S11))
        S21_mag.append(np.abs(S21))
    
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    
    ax1 = axes[0]
    ax1.plot(f_vals/1e9, S11_mag, 'r-', lw=2, label=r'$|S_{11}|$')
    ax1.plot(f_vals/1e9, S21_mag, 'b-', lw=2, label=r'$|S_{21}|$')
    ax1.axvline(x=f_cutoff/1e9, color='gray', linestyle='--', label=f'{f_cutoff/1e9:.0f} GHz')
    ax1.set_xlabel(r'$f$ [GHz]')
    ax1.set_ylabel(r'$|S_{ij}|$')
    ax1.set_title(r'理想低通滤波器频率响应')
    ax1.legend()
    ax1.set_ylim([-0.05, 1.15])
    
    ax2 = axes[1]
    # 功率传输
    P_trans = np.array(S21_mag)**2
    P_refl = np.array(S11_mag)**2
    ax2.plot(f_vals/1e9, P_trans*100, 'b-', lw=2, label=r'$P_{trans}$ (%)')
    ax2.plot(f_vals/1e9, P_refl*100, 'r--', lw=2, label=r'$P_{refl}$ (%)')
    ax2.axvline(x=f_cutoff/1e9, color='gray', linestyle='--')
    ax2.set_xlabel(r'$f$ [GHz]')
    ax2.set_ylabel(r'Power (%)')
    ax2.set_title('功率传输与反射')
    ax2.legend()
    
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_S_parameter_response.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_S_parameter_response.png")


# ============================================================
# 4. ABCD (传输) 矩阵
# ============================================================

def ABCD_of_series_Z(Z):
    """
    串联阻抗的 ABCD 矩阵
    """
    return np.array([[1, Z], [0, 1]])


def ABCD_of_shunt_Y(Y):
    """
    并联导纳的 ABCD 矩阵
    """
    return np.array([[1, 0], [Y, 1]])


def ABCD_ofTransmissionLine(Z0, gamma, l):
    """
    长度为 l 的传输线的 ABCD 矩阵
    """
    cosh_gl = np.cosh(gamma * l)
    sinh_gl = np.sinh(gamma * l)
    return np.array([[cosh_gl, Z0 * sinh_gl], 
                      [sinh_gl / Z0, cosh_gl]])


def ABCD_of_open_circuit_stub(Z0, beta, l):
    """
    开路短截线的 ABCD 矩阵
    """
    Y = 1j * np.tan(beta * l) / Z0  # 输入导纳
    return np.array([[1, 0], [Y, 1]])


def ABCD_of_short_circuit_stub(Z0, beta, l):
    """
    短路短截线的 ABCD 矩阵
    """
    Y = -1j / (Z0 * np.tan(beta * l))
    return np.array([[1, 0], [Y, 1]])


# ============================================================
# 例题 6.3: 用 ABCD 矩阵分析级联网络
# ============================================================

def example_ABCD_cascade():
    """
    例题: 分析 T 型网络 (串联 Z1, 并联 Y, 串联 Z2)
    计算整体 ABCD 矩阵和 S 参数
    """
    Z0 = 50.0
    
    # T 型网络参数
    Z1 = complex(10, 0)   # 10 Ω 串联
    Y = complex(0, 0.02) # 20 mS 并联
    Z2 = complex(20, 0) # 20 Ω 串联
    
    # 计算整体 ABCD
    ABCD1 = ABCD_of_series_Z(Z1)
    ABCD2 = ABCD_of_shunt_Y(Y)
    ABCD3 = ABCD_of_series_Z(Z2)
    
    # 级联: ABCD_total = ABCD1 @ ABCD2 @ ABCD3
    ABCD_total = ABCD1 @ ABCD2 @ ABCD3
    
    print("T型网络 ABCD 矩阵:")
    print(f"  A = {ABCD_total[0,0]:.4f}")
    print(f"  B = {ABCD_total[0,1]:.4f}")
    print(f"  C = {ABCD_total[1,0]:.6f}")
    print(f"  D = {ABCD_total[1,1]:.4f}")
    
    # 从 ABCD 转换到 S 参数
    # 对于二端口网络
    A, B, C, D = ABCD_total[0,0], ABCD_total[0,1], ABCD_total[1,0], ABCD_total[1,1]
    
    denom = A + B/Z0 + C*Z0 + D
    S11 = (A + B/Z0 - C*Z0 - D) / denom
    S21 = 2 / denom
    S12 = 2 * (A*D - B*C) / denom
    S22 = (-A + B/Z0 - C*Z0 + D) / denom
    
    print("\nS 参数:")
    print(f"  S11 = {S11:.4f}")
    print(f"  S21 = {S21:.4f}")
    print(f"  S12 = {S12:.4f}")
    print(f"  S22 = {S22:.4f}")
    
    print(f"\n|S11| = {np.abs(S11):.4f}, |S21| = {np.abs(S21):.4f}")
    
    return ABCD_total


# ============================================================
# 例题 6.4: 传输线节与 ABCD
# ============================================================

def example_transmission_line_ABCD():
    """
    例题: 一段 50Ω 传输线, 长 l=λ/4, 求其 ABCD 矩阵
    已知 Z0=50Ω, f=10GHz, 无耗
    """
    Z0 = 50.0
    l = 0.25  # λ/4
    f = 10e9
    
    c = 3e8
    lambda_ = c / f
    beta = 2 * np.pi / lambda_
    
    # 无耗线: γ = jβ
    gamma = 1j * beta
    l_m = l * lambda_
    
    ABCD = ABCD_ofTransmissionLine(Z0, gamma, l_m)
    
    print(f"λ/4 传输线 (Z0={Z0}Ω):")
    print(f"  长度 l = {l_m*1e3:.2f} mm")
    print(f"  ABCD 矩阵:")
    print(f"    A = {ABCD[0,0]:.4f}, B = {ABCD[0,1]:.4f}")
    print(f"    C = {ABCD[1,0]:.6f}, D = {ABCD[1,1]:.4f}")
    
    # 验证: 对于 λ/4 线, A=D=0, B=jZ0, C=j/Z0
    print(f"\n验证 (理想 λ/4 线):")
    print(f"  A ≈ 0: {np.abs(ABCD[0,0]):.6f}")
    print(f"  B ≈ jZ0: {ABCD[0,1]/1j:.4f}Ω")
    print(f"  C ≈ j/Z0: {ABCD[1,0]/1j:.4f}S")
    print(f"  D ≈ 0: {np.abs(ABCD[1,1]):.6f}")
    
    return ABCD


# ============================================================
# 5. 功率波与散射矩阵
# ============================================================

def compute_power_from_S(S, Z0=50.0, P_inc=1.0):
    """
    给定 S 参数，计算各端口的反射功率和传输功率
    P_inc: 端口1入射功率
    """
    # 反射波幅度
    b1 = S[0,0] * np.sqrt(P_inc)
    # 传输波幅度
    b2 = S[1,0] * np.sqrt(P_inc)
    
    # 功率
    P_refl = np.abs(b1)**2
    P_trans = np.abs(b2)**2
    
    return P_refl, P_trans


# ============================================================
# 例题 6.5: 二端口网络的功率关系
# ============================================================

def example_power_balance():
    """
    例题: 理想隔离的双端口网络
    S = [[0, 0.9], [0.9, 0]]
    计算功率分配
    """
    S = np.array([[0, 0.9], [0.9, 0]])
    P_inc = 1.0  # 归一化入射功率
    
    P_refl, P_trans = compute_power_from_S(S, P_inc=P_inc)
    
    print("理想双端口 (S21=0.9, S11=0):")
    print(f"  入射功率 P_inc = {P_inc:.2f}")
    print(f"  反射功率 P_refl = {P_refl:.4f}")
    print(f"  传输功率 P_trans = {P_trans:.4f}")
    print(f"  插入损耗 IL = {-10*np.log10(P_trans):.4f} dB")
    
    # 非理想情况
    S_bad = np.array([[0.3, 0.8], [0.8, 0.2]])
    print("\n非理想双端口:")
    print(f"  S11 = {S_bad[0,0]:.2f}, S21 = {S_bad[1,0]:.2f}")
    
    return None


# ============================================================
# 6. 绘制微波网络图示
# ============================================================

def draw_two_port_network(ax=None, S=None, label='2-port'):
    """
    绘制二端口网络示意图
    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    
    # 两个端口框
    rect1 = Rectangle((0.1, 0.3), 0.3, 0.4, fill=True, facecolor='lightblue', edgecolor='black')
    rect2 = Rectangle((0.6, 0.3), 0.3, 0.4, fill=True, facecolor='lightblue', edgecolor='black')
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    
    # 端口标注
    ax.annotate('Port 1', (0.25, 0.2), ha='center', fontsize=12)
    ax.annotate('Port 2', (0.75, 0.2), ha='center', fontsize=12)
    
    # S 参数标注
    if S is not None:
        ax.text(0.25, 0.5, f'S11={S[0,0]:.2f}', ha='center', va='center', fontsize=9)
        ax.text(0.75, 0.5, f'S22={S[1,1]:.2f}', ha='center', va='center', fontsize=9)
        ax.text(0.45, 0.35, f'S21={S[1,0]:.2f}', ha='center', va='center', fontsize=9)
        ax.text(0.45, 0.65, f'S12={S[0,1]:.2f}', ha='center', va='center', fontsize=9)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(label)
    
    return ax


if __name__ == '__main__':
    print("=" * 60)
    print(" 第五章/六章 微波网络与介质波导 例题")
    print("=" * 60)
    
    print("\n--- 例题 5.1: 介质波导 ---")
    example_dielectric_waveguide()
    
    print("\n--- 例题 6.1: 波导等效传输线 ---")
    example_waveguide_equivalent_circuit()
    
    print("\n--- 例题 6.2: S 参数频率响应 (生成图) ---")
    example_S_parameters()
    
    print("\n--- 例题 6.3: ABCD 矩阵分析 ---")
    example_ABCD_cascade()
    
    print("\n--- 例题 6.4: 传输线 ABCD 矩阵 ---")
    example_transmission_line_ABCD()
    
    print("\n--- 例题 6.5: 功率平衡 ---")
    example_power_balance()
    
    print("\n--- 二端口网络示意图 ---")
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    S = np.array([[0.1, 0.9], [0.9, 0.05]])
    draw_two_port_network(ax, S, '二端口网络示例')
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_two_port_network.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_two_port_network.png")