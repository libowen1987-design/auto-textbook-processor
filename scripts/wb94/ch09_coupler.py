"""
第九章 铁氧体与定向耦合器 - 耦合微带线、威尔金森功分器、定向耦合器
========================================================================
基于梁昌洪《简明微波》第八章常用微波元件

本文件覆盖：
1. 耦合微带线的奇偶模分析
2. 耦合线定向耦合器 (3dB, 10dB, 20dB)
3. 威尔金森功率分配器
4. 双 T (Magic T)
5. 铁氧体隔离器
6. 混合电桥
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc, FancyArrowPatch
from matplotlib.collections import LineCollection
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

Z0 = 50.0
c = 3e8

# ============================================================
# 1. 耦合微带线的奇偶模分析
# ============================================================

def coupled_microstrip_even_odd(Z0e, Z0o, epsilon_r, f):
    """
    耦合微带线的奇偶模特性阻抗与相速度
    
    Z0e: 偶模特性阻抗
    Z0o: 奇模特性阻抗
    epsilon_r: 相对介电常数
    
    返回:
        vpe, vpo: 偶模和奇模相速度
        betae, betao: 偶模和奇模相位常数
    """
    # 简化的奇偶模相速度差异
    # 偶模: 场集中在介质中, vpe ≈ c/sqrt(epsilon_eff_even)
    # 奇模: 场集中在空气中, vpo ≈ c
    
    # 有效介电常数 (简化)
    eps_eff_even = (1 + epsilon_r) / 2 + 0.5 * (epsilon_r - 1) * 0.7  # 近似
    eps_eff_odd = (1 + epsilon_r) / 2 + 0.5 * (epsilon_r - 1) * 0.3
    
    vpe = c / np.sqrt(eps_eff_even)
    vpo = c / np.sqrt(eps_eff_odd)
    
    beta_e = 2 * np.pi * f / vpe
    beta_o = 2 * np.pi * f / vpo
    
    return vpe, vpo, beta_e, beta_o


def coupling_factor_from_Z(Z0e, Z0o, Z0=50.0):
    """
    耦合系数 C = (Z0e - Z0o) / (Z0e + Z0o)
    
    耦合度 = -20*log10(C)
    """
    C = (Z0e - Z0o) / (Z0e + Z0o)
    return C


def even_odd_impedance_from_coupling(C, Z0=50.0):
    """
    从耦合系数 C 和奇模阻抗求偶模阻抗
    Z0e = Z0o * (1+C)/(1-C)
    
    对于对称耦合线, Z0 = sqrt(Z0e * Z0o)
    所以 Z0o = Z0 * sqrt((1-C)/(1+C))
    Z0e = Z0 * sqrt((1+C)/(1-C))
    """
    Z0o = Z0 * np.sqrt((1 - C) / (1 + C))
    Z0e = Z0 * np.sqrt((1 + C) / (1 - C))
    
    return Z0e, Z0o


# ============================================================
# 例题 9.1: 耦合线定向耦合器
# ============================================================

def example_coupled_line_coupler():
    """
    例题: 设计 -20dB 耦合线定向耦合器
    Z0=50Ω, f=4GHz, ε_r=2.55
    
    耦合度 C = 10^(-20/20) = 0.1
    Z0e = 50 * sqrt((1+C)/(1-C)) = 50 * sqrt(1.222) = 55.4 Ω
    Z0o = 50 * sqrt((1-C)/(1+C)) = 50 * sqrt(0.818) = 45.2 Ω
    
    电长度 θ = 90° (λ/4)
    """
    Z0 = 50.0
    C_dB = -20
    epsilon_r = 2.55
    f = 4e9
    
    # 耦合系数
    C = 10**(C_dB / 20)
    
    # 奇偶模阻抗
    Z0e, Z0o = even_odd_impedance_from_coupling(C, Z0)
    
    print(f"-20dB 耦合线定向耦合器设计:")
    print(f"  耦合度: {C_dB} dB, C = {C:.4f}")
    print(f"  Z0e = {Z0e:.2f} Ω")
    print(f"  Z0o = {Z0o:.2f} Ω")
    
    # 验证
    Z0_check = np.sqrt(Z0e * Z0o)
    print(f"  验证: sqrt(Z0e * Z0o) = {Z0_check:.2f} Ω (应为 50Ω)")
    
    # 波导波长
    lambda_g = c / (f * np.sqrt(epsilon_r))
    l = lambda_g / 4
    
    print(f"\n  工作频率 f = {f/1e9:.1f} GHz")
    print(f"  λ_g = {lambda_g*1e3:.2f} mm")
    print(f"  λ/4 长度 l = {l*1e3:.2f} mm")
    
    # 方向性
    # 由于奇偶模相速度不同, 方向性有限
    vpe, vpo, beta_e, beta_o = coupled_microstrip_even_odd(Z0e, Z0o, epsilon_r, f)
    
    print(f"\n  偶模相速度 vpe = {vpe/1e8:.4f}×10⁸ m/s")
    print(f"  奇模相速度 vpo = {vpo/1e8:.4f}×10⁸ m/s")
    print(f"  相速度差 Δv/v ≈ {(vpe-vpo)/vpe*100:.2f}%")
    
    return Z0e, Z0o, l


# ============================================================
# 例题 9.2: 3dB 耦合器
# ============================================================

def example_3dB_coupler():
    """
    例题: 3dB (功率平分) 耦合线定向耦合器
    C = 10^(-3/20) = 0.707
    Z0e = 50 * sqrt((1+0.707)/(1-0.707)) = 50 * sqrt(5.828) = 120.6 Ω
    Z0o = 50 * sqrt((1-0.707)/(1+0.707)) = 50 * sqrt(0.171) = 20.7 Ω
    """
    Z0 = 50.0
    C_dB = -3
    C = 10**(C_dB / 20)
    
    Z0e, Z0o = even_odd_impedance_from_coupling(C, Z0)
    
    print(f"3dB 耦合线定向耦合器:")
    print(f"  耦合度: {C_dB} dB, C = {C:.4f}")
    print(f"  Z0e = {Z0e:.2f} Ω")
    print(f"  Z0o = {Z0o:.2f} Ω")
    
    # 检验
    print(f"  验证: Z0e/Z0o = {Z0e/Z0o:.2f} (应为 (1+C)/(1-C) = {(1+C)/(1-C):.4f})")
    
    return Z0e, Z0o


# ============================================================
# 例题 9.3: 威尔金森功率分配器
# ============================================================

def example_wilkinson_divider():
    """
    例题: 等分威尔金森功率分配器 (2:1 分配)
    Z0=50Ω, f=5GHz
    
    端口阻抗: Z_in = 2*Z0 = 100 Ω (输入)
    输出阻抗: Z2 = Z3 = sqrt(2)*Z0 = 70.7 Ω (输出)
    隔离电阻: R = 2*Z0 = 100 Ω
    """
    Z0 = 50.0
    
    # 等分
    k = 1.0  # 功率分配比 P2/P3 = k^2
    
    # 输入阻抗
    Z_in = Z0 * (1 + k**2) / (2 * k**2)  # Z_in = 2*Z0 for k=1
    Z_in_check = 2 * Z0
    
    # 输出阻抗
    Z2 = Z0 * np.sqrt(1 + 1/k**2) * (1 + k) / (2*k)
    Z2_check = Z0 * np.sqrt(2)  # = 70.7Ω for k=1
    
    # 隔离电阻
    R = Z0 * (1 + 1/k**2)  # = 2*Z0 for k=1
    R_check = 2 * Z0
    
    print(f"等分威尔金森功率分配器:")
    print(f"  系统阻抗 Z0 = {Z0} Ω")
    print(f"\n  等分 (k=1, 3dB):")
    print(f"    输入阻抗 Z_in = {Z_in_check:.2f} Ω")
    print(f"    输出阻抗 Z2 = Z3 = {Z2_check:.2f} Ω")
    print(f"    隔离电阻 R = {R_check:.2f} Ω")
    
    # 绘制结构图
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # 输入端口
    ax.annotate('', xy=(0.2, 0.5), xytext=(0.05, 0.5),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    ax.text(0.05, 0.45, 'Port 1\n(Z_in=100Ω)', ha='center', fontsize=10)
    
    # T 型结
    ax.plot([0.2, 0.4], [0.5, 0.5], 'b-', lw=3)
    ax.plot([0.3, 0.3], [0.35, 0.65], 'k-', lw=2)
    
    # 上支路
    ax.plot([0.3, 0.3], [0.65, 0.75], 'b-', lw=2)
    ax.plot([0.3, 0.7], [0.75, 0.75], 'b-', lw=2)
    ax.annotate('', xy=(0.75, 0.5), xytext=(0.3, 0.75),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    
    # 下支路
    ax.plot([0.3, 0.3], [0.35, 0.25], 'b-', lw=2)
    ax.plot([0.3, 0.7], [0.25, 0.25], 'b-', lw=2)
    ax.annotate('', xy=(0.75, 0.5), xytext=(0.3, 0.25),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    
    # 隔离电阻
    ax.plot([0.3, 0.3], [0.65, 0.35], 'r--', lw=2)
    ax.text(0.22, 0.5, 'R=100Ω', ha='right', fontsize=9, color='red')
    
    # 输出端口标注
    ax.text(0.75, 0.45, 'Port 2\n(70.7Ω)', ha='center', fontsize=10)
    ax.text(0.75, 0.75, 'Port 3\n(70.7Ω)', ha='center', fontsize=10)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('威尔金森功率分配器 (等分) 结构示意')
    
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_wilkinson_divider.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_wilkinson_divider.png")
    
    return Z_in_check, Z2_check, R_check


# ============================================================
# 例题 9.4: 双 T (Magic T)
# ============================================================

def example_magic_T():
    """
    例题: Magic T (双 T) 的 S 参数特性
    
    特性:
    - 端口 1 (E 面) 和端口 2 (H 面) 匹配
    - 端口 3 和端口 4 隔离 (S34 = 0)
    - E 面输入功率到端口 1, 从端口 3 和 4 同相输出
    - H 面输入功率到端口 2, 从端口 3 和 4 反相输出
    """
    print("Magic T (双 T) 特性:")
    print("  端口定义:")
    print("    端口1: E-arm (E面 T)")
    print("    端口2: H-arm (H面 T)")
    print("    端口3,4: 侧臂 (隔离)")
    print("\n  S 矩阵性质 (对于理想 Magic T):")
    print("    S11 = S22 = 0 (匹配)")
    print("    S33 = S44 = 0 (匹配)")
    print("    S34 = 0 (隔离)")
    print("    S13 = S14 = 1/√2 (E面激励)")
    print("    S23 = -S24 = 1/√2 (H面激励, 反相)")
    
    # 简化 S 矩阵
    S_magicT = np.zeros((4, 4), dtype=complex)
    
    # 端口 1 (E) → 端口 3,4 同相
    S_magicT[0, 2] = 1/np.sqrt(2)
    S_magicT[0, 3] = 1/np.sqrt(2)
    
    # 端口 2 (H) → 端口 3,4 反相
    S_magicT[1, 2] = 1/np.sqrt(2)
    S_magicT[1, 3] = -1/np.sqrt(2)
    
    # 隔离
    S_magicT[2, 3] = 0
    S_magicT[3, 2] = 0
    
    print("\n  简化 S 矩阵 (部分):")
    print(f"    S13 = {S_magicT[0,2]:.4f}")
    print(f"    S14 = {S_magicT[0,3]:.4f}")
    print(f"    S23 = {S_magicT[1,2]:.4f}")
    print(f"    S24 = {S_magicT[1,3]:.4f}")
    
    return S_magicT


# ============================================================
# 例题 9.5: 定向耦合器的方向性
# ============================================================

def example_coupler_directivity():
    """
    例题: 耦合微带线的方向性分析
    
    方向性 D = 20*log10(|S41/S31|)
    由于奇偶模相速度不同, 方向性受限
    
    假设 βe ≠ βo, 计算方向性
    """
    f = 10e9
    lambda_g = c / f
    
    # 奇偶模相位差
    # 对于 λ/4 耦合线, 方向性取决于 (βe - βo) * l
    l = lambda_g / 4
    
    # 假设相位差 Δβ*l = 0.1 rad
    delta_beta_l = 0.1  # rad
    
    # 方向性 (近似)
    D = 20 * np.log10(np.abs(delta_beta_l / 2))  # 简化估计
    
    print(f"耦合线方向性分析:")
    print(f"  工作频率 f = {f/1e9:.1f} GHz")
    print(f"  耦合线长度 l = {l*1e3:.2f} mm (λ/4)")
    print(f"  奇偶模相位差 Δβ·l ≈ {delta_beta_l:.2f} rad")
    print(f"  方向性 D ≈ {D:.2f} dB (理论极限)")
    
    # 实际方向性通常在 20-40 dB
    return D


# ============================================================
# 例题 9.6: 铁氧体隔离器
# ============================================================

def example_ferrite_isolator():
    """
    例题: 铁氧体隔离器的工作原理
    隔离器: 正向衰减很小, 反向衰减很大
    
    基于 YIG (钇铁石榴石) 或锂铁氧体
    
    关键参数:
    - 饱和磁化强度 4πM_s
    - 介电损耗角正切 tanδ
    - 铁磁共振线宽 ΔH
    """
    print("铁氧体隔离器:")
    print("\n  特性:")
    print("    正向传输: 衰减 < 1 dB")
    print("    反向隔离: 衰减 > 20 dB")
    print("    反射系数: < -20 dB")
    
    # 典型参数
    epsilon_r_ferrite = 13  # 镁铁氧体
    saturation_4piMs = 500  # Gauss (典型值)
    delta_H = 500  # Oe (线宽)
    
    print(f"\n  典型铁氧体参数:")
    print(f"    介电常数 ε_r ≈ {epsilon_r_ferrite}")
    print(f"    饱和磁化 4πM_s ≈ {saturation_4piMs} Gauss")
    print(f"    线宽 ΔH ≈ {delta_H} Oe")
    
    # 隔离比
    forward_loss_dB = 0.5  # 正向损耗
    reverse_loss_dB = 30   # 反向隔离
    isolation_ratio_dB = reverse_loss_dB - forward_loss_dB
    
    print(f"\n  隔离比: {isolation_ratio_dB} dB")
    
    return None


# ============================================================
# 绘图: 耦合线截面与场分布
# ============================================================

def draw_coupled_microstrip(ax=None, w=None, s=None, h=None):
    """
    绘制耦合微带线截面结构
    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    
    if w is None:
        w = 1.0
    if s is None:
        s = 0.5
    if h is None:
        h = 0.5
    
    # 归一化
    scale = 2.0 / max(w*2 + s, h)
    w_s = w * scale
    s_s = s * scale
    h_s = h * scale
    
    # 接地金属
    rect_gnd = Rectangle((-w_s - s_s/2 - 0.3, -h_s - 0.1), 
                          2*w_s + s_s + 0.6, 0.1,
                          facecolor='silver', edgecolor='black', lw=1)
    ax.add_patch(rect_gnd)
    
    # 介质基片
    rect_sub = Rectangle((-w_s - s_s/2 - 0.3, 0), 
                           2*w_s + s_s + 0.6, h_s,
                           facecolor='#ADD8E6', edgecolor='black', lw=1)
    ax.add_patch(rect_sub)
    
    # 上导体带
    rect_m1 = Rectangle((-w_s/2, 0), w_s, 0.08,
                          facecolor='gold', edgecolor='black', lw=1)
    ax.add_patch(rect_m1)
    
    # 下导体带
    rect_m2 = Rectangle((s_s/2, 0), w_s, 0.08,
                          facecolor='gold', edgecolor='black', lw=1)
    ax.add_patch(rect_m2)
    
    ax.set_xlim(-w_s - s_s/2 - 0.5, w_s + s_s/2 + 0.5)
    ax.set_ylim(-h_s - 0.2, h_s + 0.3)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('耦合微带线截面结构')
    
    # 标注
    ax.annotate(f'w={w*1e3:.1f}mm', (0, 0.15), ha='center', fontsize=9)
    ax.annotate(f's={s*1e3:.1f}mm', (0, -0.1), ha='center', fontsize=9)
    ax.annotate(f'h={h*1e3:.1f}mm', (w_s + s_s/2 + 0.15, h_s/2), fontsize=9)
    
    return ax


# ============================================================
# 绘图: 定向耦合器符号图
# ============================================================

def draw_directional_coupler(ax=None):
    """
    绘制定向耦合器符号图
    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    
    # 主线
    ax.plot([0.1, 0.5], [0.75, 0.75], 'b-', lw=3)
    ax.plot([0.5, 0.9], [0.25, 0.25], 'b-', lw=3)
    
    # 耦合线 (虚线)
    ax.plot([0.1, 0.5], [0.25, 0.25], 'b--', lw=2)
    ax.plot([0.5, 0.9], [0.75, 0.75], 'b--', lw=2)
    
    # 耦合节点
    ax.plot([0.5, 0.5], [0.25, 0.75], 'k-', lw=2)
    
    # 端口标注
    ax.text(0.05, 0.75, '输入', ha='center', va='bottom', fontsize=11)
    ax.text(0.95, 0.25, '直通', ha='center', va='bottom', fontsize=11)
    ax.text(0.05, 0.25, '耦合', ha='center', va='top', fontsize=11)
    ax.text(0.95, 0.75, '隔离', ha='center', va='top', fontsize=11)
    
    # 标注
    ax.annotate('耦合线', (0.3, 0.35), fontsize=9, color='gray')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('定向耦合器符号图')
    
    return ax


# ============================================================
# 绘图: 耦合器频率响应
# ============================================================

def plot_coupler_frequency_response():
    """
    绘制理想耦合器的频率响应
    """
    f_vals = np.linspace(2e9, 8e9, 300)
    f_center = 5e9
    bandwidth = 2e9  # 10% 带宽
    
    # 简化模型: 理想 λ/4 耦合器在中心频率有理想耦合
    # 偏离中心频率时, 耦合度下降
    
    coupling_dB = -3  # 3dB 耦合器
    C_center = 10**(coupling_dB / 20)
    
    # 频率响应 (简化)
    coupling_response = C_center * np.sinc((f_vals - f_center) / bandwidth * np.pi)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    ax1 = axes[0]
    ax1.plot(f_vals/1e9, 20*np.log10(np.abs(coupling_response) + 1e-12), 'b-', lw=2)
    ax1.axhline(y=coupling_dB, color='r', linestyle='--', label=f'{coupling_dB}dB 耦合度')
    ax1.axvline(x=f_center/1e9, color='gray', linestyle=':', label=f'{f_center/1e9:.0f}GHz')
    ax1.set_xlabel(r'$f$ [GHz]')
    ax1.set_ylabel(r'耦合度 [dB]')
    ax1.set_title(r'3dB 耦合线定向耦合器频率响应 (理想)')
    ax1.legend()
    ax1.set_ylim([-6, 0])
    
    # 隔离度响应
    ax2 = axes[1]
    # 理想隔离度在中心频率无穷大, 偏离时下降
    isolation_dB = 40 * np.ones_like(f_vals)
    delta_f = np.abs(f_vals - f_center) / bandwidth
    isolation_dB = isolation_dB - 30 * delta_f**2
    isolation_dB = np.maximum(isolation_dB, 10)
    
    ax2.plot(f_vals/1e9, isolation_dB, 'r-', lw=2, label='隔离度')
    ax2.axvline(x=f_center/1e9, color='gray', linestyle=':')
    ax2.set_xlabel(r'$f$ [GHz]')
    ax2.set_ylabel(r'隔离度 [dB]')
    ax2.set_title('隔离端口 (端口4) 隔离度频率响应 (理想)')
    ax2.legend()
    
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_coupler_frequency_response.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_coupler_frequency_response.png")


if __name__ == '__main__':
    print("=" * 60)
    print(" 第九章 铁氧体与定向耦合器 例题")
    print("=" * 60)
    
    print("\n--- 例题 9.1: -20dB 耦合线定向耦合器 ---")
    example_coupled_line_coupler()
    
    print("\n--- 例题 9.2: 3dB 耦合器 ---")
    example_3dB_coupler()
    
    print("\n--- 例题 9.3: 威尔金森功率分配器 ---")
    example_wilkinson_divider()
    
    print("\n--- 例题 9.4: Magic T 双T ---")
    example_magic_T()
    
    print("\n--- 例题 9.5: 耦合器方向性 ---")
    example_coupler_directivity()
    
    print("\n--- 例题 9.6: 铁氧体隔离器 ---")
    example_ferrite_isolator()
    
    print("\n--- 耦合微带线截面结构图 ---")
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    draw_coupled_microstrip(ax, w=1e-3, s=0.5e-3, h=0.5e-3)
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_coupled_microstrip.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_coupled_microstrip.png")
    
    print("\n--- 定向耦合器符号图 ---")
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    draw_directional_coupler(ax)
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_directional_coupler_symbol.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_directional_coupler_symbol.png")
    
    print("\n--- 耦合器频率响应 (生成图) ---")
    plot_coupler_frequency_response()