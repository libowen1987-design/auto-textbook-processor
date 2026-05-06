"""
第八章 微波网络进阶 - 功率增益、插入损耗与信号流图
========================================================
基于梁昌洪《简明微波》第六章微波网络基础部分

本文件覆盖：
1. 功率增益 G, G_A, G_T 的计算
2. 插入损耗与回波损耗
3. 稳定性判据 (S 参数)
4. 阻抗匹配网络设计 (共轭匹配)
5. 信号流图简化与 Mason 规则
6. 双端口网络噪声系数
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch, Circle
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

Z0 = 50.0  # 标准系统阻抗

# ============================================================
# 1. 功率增益计算
# ============================================================

def available_power_gain(S, ZS=None, ZL=None):
    """
    计算资用功率增益 G_A
    G_A = |S21|^2 * (1 - |S11|^2) / (1 - |S22|^2 + |D|^2)
    其中 D = S11*S22 - S12*S21
    """
    if ZS is None:
        ZS = Z0
    if ZL is None:
        ZL = Z0
    
    S11, S12, S21, S22 = S[0,0], S[0,1], S[1,0], S[1,1]
    
    D = S11 * S22 - S12 * S21
    
    numerator = np.abs(S21)**2 * (1 - np.abs(S11)**2)
    denominator = (1 - np.abs(S22)**2) * np.abs(1 - S22 * np.conj(S11))**2
    
    if denominator == 0:
        return np.inf
    
    G_A = numerator / denominator
    return G_A


def transducer_power_gain(S, ZS=None, ZL=None):
    """
    计算换能器功率增益 G_T
    G_T = (1 - |Γ_S|^2) * |S21|^2 * (1 - |Γ_L|^2) 
          / |(1 - S11*Γ_S) * (1 - S22*Γ_L) - S12*S21*Γ_S*Γ_L|^2
    """
    if ZS is None:
        ZS = Z0
    if ZL is None:
        ZL = Z0
    
    Gamma_S = (ZS - Z0) / (ZS + Z0)
    Gamma_L = (ZL - Z0) / (ZL + Z0)
    
    S11, S12, S21, S22 = S[0,0], S[0,1], S[1,0], S[1,1]
    
    denominator = ((1 - S11*Gamma_S) * (1 - S22*Gamma_L) - S12*S21*Gamma_S*Gamma_L)
    
    if np.abs(denominator) < 1e-12:
        return np.inf
    
    G_T = (np.abs(1 - Gamma_S**2) * np.abs(S21)**2 * np.abs(1 - Gamma_L**2)) / (np.abs(denominator)**2)
    
    return G_T


def power_gain_circle(S, which='input'):
    """
    绘制等功率增益圆 (稳定性判据用)
    """
    pass


# ============================================================
# 例题 8.1: 资用功率增益
# ============================================================

def example_power_gain():
    """
    例题: 二端口网络 S = [[0.5, 0.1], [2.0, 0.3]]
    ZS=ZL=50Ω, 计算 G_A 和 G_T
    """
    S = np.array([[0.5, 0.1], [2.0, 0.3]])
    
    print("二端口网络 S 参数:")
    print(f"  S11 = {S[0,0]:.3f}, S12 = {S[0,1]:.3f}")
    print(f"  S21 = {S[1,0]:.3f}, S22 = {S[1,1]:.3f}")
    
    # 计算 D
    D = S[0,0] * S[1,1] - S[0,1] * S[1,0]
    print(f"  D = S11*S22 - S12*S21 = {D:.4f}")
    
    # 稳定性判据
    K = (1 - np.abs(S[0,0])**2 - np.abs(S[1,1])**2 + np.abs(D)**2) / (2 * np.abs(S[0,1] * S[1,0]))
    print(f"\n稳定性因子 K = {K:.4f}")
    if K > 1 and np.abs(D) < 1:
        print("  → 无条件稳定")
    else:
        print("  → 潜在不稳定")
    
    # G_A
    G_A = available_power_gain(S)
    print(f"\n资用功率增益 G_A = {G_A:.4f} ({10*np.log10(G_A):.2f} dB)")
    
    # G_T
    G_T = transducer_power_gain(S)
    print(f"换能器功率增益 G_T = {G_T:.4f} ({10*np.log10(G_T):.2f} dB)")
    
    # 插入损耗
    IL_dB = -10 * np.log10(G_T)
    print(f"插入损耗 IL = {IL_dB:.4f} dB")
    
    return G_A, G_T


# ============================================================
# 2. 插入损耗与回波损耗
# ============================================================

def return_loss(S11):
    """
    回波损耗 RL = -20*log|Γ| dB
    """
    return -20 * np.log10(np.abs(S11))


def insertion_loss_from_S(S21):
    """
    插入损耗 IL = -20*log|S21| dB
    """
    return -20 * np.log10(np.abs(S21))


def vswr_from_reflection(Gamma):
    """
    VSWR = (1 + |Γ|) / (1 - |Γ|)
    """
    return (1 + np.abs(Gamma)) / (1 - np.abs(Gamma))


# ============================================================
# 例题 8.2: 回波损耗与 VSWR
# ============================================================

def example_return_loss():
    """
    例题: 天线端口测得 S11 = 0.3 (反射系数)
    求回波损耗 RL, VSWR, 传输功率百分比
    """
    S11 = 0.3
    
    RL = return_loss(S11)
    VSWR = vswr_from_reflection(S11)
    
    P_refl = np.abs(S11)**2
    P_trans = 1 - P_refl
    
    print(f"S11 = {S11:.3f}:")
    print(f"  回波损耗 RL = {RL:.4f} dB")
    print(f"  VSWR = {VSWR:.4f}")
    print(f"  反射功率比 = {P_refl*100:.2f}%")
    print(f"  传输功率比 = {P_trans*100:.2f}%")
    
    # 带宽内的 RL 变化
    S11_vals = np.linspace(0, 1, 200)
    RL_vals = -20 * np.log10(S11_vals + 1e-12)
    VSWR_vals = (1 + S11_vals) / (1 - S11_vals)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    ax1 = axes[0]
    ax1.plot(S11_vals, RL_vals, 'b-', lw=2)
    ax1.axhline(y=10, color='r', linestyle='--', label='RL=10dB')
    ax1.axhline(y=20, color='g', linestyle='--', label='RL=20dB')
    ax1.set_xlabel(r'$|S_{11}|$')
    ax1.set_ylabel(r'$RL$ [dB]')
    ax1.set_title('回波损耗 vs 反射系数幅值')
    ax1.legend()
    ax1.set_xlim([0, 1])
    
    ax2 = axes[1]
    ax2.plot(S11_vals, VSWR_vals, 'b-', lw=2)
    ax2.axhline(y=2, color='r', linestyle='--', label='VSWR=2')
    ax2.axhline(y=3, color='g', linestyle='--', label='VSWR=3')
    ax2.set_xlabel(r'$|S_{11}|$')
    ax2.set_ylabel('VSWR')
    ax2.set_title('VSWR vs 反射系数幅值')
    ax2.legend()
    ax2.set_ylim([1, 10])
    
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_return_loss_vswr.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_return_loss_vswr.png")
    
    return RL, VSWR


# ============================================================
# 3. 共轭匹配
# ============================================================

def conjugate_match_Z(Z_opt):
    """
    共轭匹配: Γ_S = Γ_L* 的最优源/负载阻抗
    """
    return np.conj(Z_opt)


def gain_circle(S21_mag, K=None, D=None):
    """
    等增益圆参数计算
    """
    pass


# ============================================================
# 例题 8.3: 共轭匹配设计
# ============================================================

def example_conjugate_matching():
    """
    例题: 已知 S11=0.6∠-30°, S22=0.4∠60°, S21=2.0, S12=0.1
    Z0=50Ω, 求使资用功率增益最大的源阻抗和负载阻抗
    """
    S = np.array([[0.6*np.exp(-1j*np.pi/6), 0.1],
                  [2.0, 0.4*np.exp(1j*np.pi/3)]])
    
    # 计算最优源反射系数
    # Γ_opt_S = B1 ± sqrt(B1^2 - 4*C1) / (2*C1)
    # 其中 B1 = 1 + (|S11|^2 - |S22|^2 + |D|^2) / |S21|^2
    # C1 = S11 - D*S22*
    
    D = S[0,0]*S[1,1] - S[0,1]*S[1,0]
    
    B1_num = 1 + (np.abs(S[0,0])**2 - np.abs(S[1,1])**2 + np.abs(D)**2)
    B1 = B1_num / (np.abs(S[1,0])**2)
    
    C1 = S[0,0] - D * np.conj(S[1,1])
    
    # 两个解
    sqrt_term = np.sqrt(B1**2 - 4 * np.abs(C1)**2)
    
    Gamma_S_opt_1 = (B1 + sqrt_term) / (2 * C1)
    Gamma_S_opt_2 = (B1 - sqrt_term) / (2 * C1)
    
    # 选择使 |Γ| < 1 的解
    if np.abs(Gamma_S_opt_1) < 1:
        Gamma_S_opt = Gamma_S_opt_1
    else:
        Gamma_S_opt = Gamma_S_opt_2
    
    # 对应的最优负载反射系数
    Gamma_L_opt = np.conj(Gamma_S_opt)
    
    # 转换为阻抗
    Z_S_opt = Z0 * (1 + Gamma_S_opt) / (1 - Gamma_S_opt)
    Z_L_opt = Z0 * (1 + Gamma_L_opt) / (1 - Gamma_L_opt)
    
    print(f"共轭匹配设计:")
    print(f"  S11 = {S[0,0]:.3f}, S22 = {S[1,1]:.3f}")
    print(f"  S21 = {S[1,0]:.1f}, S12 = {S[0,1]:.1f}")
    print(f"  D = {D:.4f}")
    print(f"\n最优源反射系数 Γ_S = {Gamma_S_opt:.4f}")
    print(f"  |Γ_S| = {np.abs(Gamma_S_opt):.4f}")
    print(f"  最优源阻抗 Z_S = {Z_S_opt:.2f} Ω")
    
    print(f"\n最优负载反射系数 Γ_L = {Gamma_L_opt:.4f}")
    print(f"  |Γ_L| = {np.abs(Gamma_L_opt):.4f}")
    print(f"  最优负载阻抗 Z_L = {Z_L_opt:.2f} Ω")
    
    return Z_S_opt, Z_L_opt


# ============================================================
# 4. 稳定性判据
# ============================================================

def stability_K(S):
    """
    Rollett 稳定性因子 K
    K > 1 且 |D| < 1 为无条件稳定
    """
    S11, S12, S21, S22 = S[0,0], S[0,1], S[1,0], S[1,1]
    D = S11 * S22 - S12 * S21
    
    numerator = 1 - np.abs(S11)**2 - np.abs(S22)**2 + np.abs(D)**2
    denominator = 2 * np.abs(S12 * S21)
    
    if denominator == 0:
        return np.inf
    
    K = numerator / denominator
    return K


def stability_circle(S, which='input'):
    """
    计算稳定性圆的圆心和半径
    
    输入稳定性圆 (Γ_S 平面):
    圆心 C_S = (S11 - D*S22*) / (1 - |S22|^2 + |D|^2)
    半径 R_S = sqrt(1 - |S11|^2 + |D|^2) / |1 - |S22|^2 + |D|^2|
    
    输出稳定性圆 (Γ_L 平面):
    类似
    """
    S11, S12, S21, S22 = S[0,0], S[0,1], S[1,0], S[1,1]
    D = S11 * S22 - S12 * S21
    
    if which == 'input':
        # 输入稳定性圆 (Γ_S 平面)
        center = (S11 - D * np.conj(S22)) / (1 - np.abs(S22)**2 + np.abs(D)**2)
        radius = np.sqrt(1 - np.abs(S11)**2 + np.abs(D)**2) / np.abs(1 - np.abs(S22)**2 + np.abs(D)**2)
    else:
        # 输出稳定性圆 (Γ_L 平面)
        center = (S22 - D * np.conj(S11)) / (1 - np.abs(S11)**2 + np.abs(D)**2)
        radius = np.sqrt(1 - np.abs(S22)**2 + np.abs(D)**2) / np.abs(1 - np.abs(S11)**2 + np.abs(D)**2)
    
    return center, radius


# ============================================================
# 例题 8.4: 稳定性判据
# ============================================================

def example_stability():
    """
    例题: 验证两个二端口网络的稳定性
    网络1: S = [[0.8, 0.1], [2.0, 0.3]] (可能不稳定)
    网络2: S = [[0.2, 0.05], [1.5, 0.4]] (稳定)
    """
    networks = [
        {'name': 'Network 1', 'S': np.array([[0.8, 0.1], [2.0, 0.3]])},
        {'name': 'Network 2', 'S': np.array([[0.2, 0.05], [1.5, 0.4]])},
    ]
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    
    for idx, net in enumerate(networks):
        S = net['S']
        K = stability_K(S)
        D = S[0,0]*S[1,1] - S[0,1]*S[1,0]
        
        print(f"\n{net['name']}:")
        print(f"  S = {S[0,0]:.3f}, {S[0,1]:.3f}")
        print(f"    {S[1,0]:.3f}, {S[1,1]:.3f}")
        print(f"  K = {K:.4f}")
        print(f"  |D| = {np.abs(D):.4f}")
        
        if K > 1 and np.abs(D) < 1:
            print("  → 无条件稳定")
        else:
            print("  → 潜在不稳定")
        
        # 绘制稳定性圆
        ax = axes[idx]
        
        # 单位圆
        theta = np.linspace(0, 2*np.pi, 200)
        ax.plot(np.cos(theta), np.sin(theta), 'k-', lw=1.5, label='单位圆')
        
        # 稳定性圆
        center, radius = stability_circle(S, which='input')
        
        if not np.isnan(center) and not np.isnan(radius) and radius < 10:
            circle = plt.Circle((np.real(center), np.imag(center)), radius, 
                                fill=False, color='blue', lw=1.5, linestyle='--')
            ax.add_patch(circle)
            ax.text(np.real(center), np.imag(center), f'稳定圆\ncenter={center:.2f}\nr={radius:.2f}',
                   fontsize=8, ha='center')
        
        # 标注 S11
        ax.plot(np.real(S[0,0]), np.imag(S[0,0]), 'ro', markersize=10, label=f'S11={S[0,0]:.2f}')
        
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_aspect('equal')
        ax.set_xlabel(r'Re{$\Gamma$}')
        ax.set_ylabel(r'Im{$\Gamma$}')
        ax.set_title(f'{net["name"]} - 输入稳定性 (K={K:.2f})')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_stability_circles.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_stability_circles.png")
    
    return K


# ============================================================
# 5. 噪声系数 (双端口网络)
# ============================================================

def noise_figure(F_dB):
    """
    噪声系数 F (线性) -> F_dB
    F_dB = 10*log10(F)
    """
    return 10 * np.log10(F_dB)


def noise_figure_from_gain(gamma_matched, F_device_dB, G_A_dB):
    """
    级联网络的噪声系数 (Friis 公式)
    F_total = F1 + (F2-1)/G1 + (F3-1)/G1/G2 + ...
    """
    F_lin = 10**(F_device_dB / 10)
    G_lin = 10**(G_A_dB / 10)
    
    return F_lin


# ============================================================
# 例题 8.5: 放大器噪声系数
# ============================================================

def example_noise_figure():
    """
    例题: 两级放大器级联
    第一级: G1=10dB, F1=2dB
    第二级: G2=20dB, F2=5dB
    求总噪声系数
    """
    G1_dB = 10.0
    F1_dB = 2.0
    G2_dB = 20.0
    F2_dB = 5.0
    
    G1 = 10**(G1_dB / 10)
    G2 = 10**(G2_dB / 10)
    F1 = 10**(F1_dB / 10)
    F2 = 10**(F2_dB / 10)
    
    # Friis 公式
    F_total_lin = F1 + (F2 - 1) / G1
    
    F_total_dB = 10 * np.log10(F_total_lin)
    
    print(f"两级放大器级联:")
    print(f"  第1级: G1={G1_dB}dB, F1={F1_dB}dB")
    print(f"  第2级: G2={G2_dB}dB, F2={F2_dB}dB")
    print(f"\n  F1(线性) = {F1:.4f}")
    print(f"  F2(线性) = {F2:.4f}")
    print(f"  G1(线性) = {G1:.4f}")
    print(f"\n  总噪声系数 F = {F_total_lin:.4f} ({F_total_dB:.4f} dB)")
    
    # 带宽效应
    f_vals = np.linspace(0.5e9, 10e9, 200)
    F1_bw = F1 * (1 + 0.1 * (f_vals/1e9 - 1)**2)  # 简化模型
    
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    ax.plot(f_vals/1e9, 10*np.log10(F1_bw), 'b-', lw=2, label='放大器噪声系数')
    ax.set_xlabel(r'$f$ [GHz]')
    ax.set_ylabel(r'$F$ [dB]')
    ax.set_title('放大器噪声系数随频率变化 (示例)')
    ax.legend()
    
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_noise_figure.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_noise_figure.png")
    
    return F_total_dB


# ============================================================
# 6. 双端口匹配网络设计 (简图)
# ============================================================

def draw_matching_network(ax=None, ZL=50.0, ZS=50.0, Z0=50.0):
    """
    绘制简单的阻抗匹配网络框图
    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # 画信号流
    ax.annotate('', xy=(0.9, 0.5), xytext=(0.1, 0.5),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    
    # 源
    circle_S = Circle((0.05, 0.5), 0.03, fill=True, facecolor='gold', edgecolor='black')
    ax.add_patch(circle_S)
    ax.text(0.05, 0.35, f'源\nZs={ZS}Ω', ha='center', fontsize=10)
    
    # 匹配网络
    rect = patches.Rectangle((0.35, 0.35), 0.3, 0.3, fill=True, 
                              facecolor='lightblue', edgecolor='black', lw=2)
    ax.add_patch(rect)
    ax.text(0.5, 0.5, '匹配\n网络', ha='center', va='center', fontsize=11)
    
    # 负载
    rect_L = patches.Rectangle((0.75, 0.35), 0.2, 0.3, fill=True,
                                facecolor='lightgreen', edgecolor='black', lw=2)
    ax.add_patch(rect_L)
    ax.text(0.85, 0.5, f'负载\nZL={ZL}Ω', ha='center', va='center', fontsize=10)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('阻抗匹配网络示意')
    
    return ax


if __name__ == '__main__':
    print("=" * 60)
    print(" 第八章 微波网络进阶 例题")
    print("=" * 60)
    
    print("\n--- 例题 8.1: 功率增益计算 ---")
    example_power_gain()
    
    print("\n--- 例题 8.2: 回波损耗与 VSWR (生成图) ---")
    example_return_loss()
    
    print("\n--- 例题 8.3: 共轭匹配设计 ---")
    example_conjugate_matching()
    
    print("\n--- 例题 8.4: 稳定性判据 (生成图) ---")
    example_stability()
    
    print("\n--- 例题 8.5: 噪声系数 (Friis公式) ---")
    example_noise_figure()
    
    print("\n--- 匹配网络框图 ---")
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    draw_matching_network(ax, ZL=75.0, ZS=50.0)
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_matching_network.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_matching_network.png")