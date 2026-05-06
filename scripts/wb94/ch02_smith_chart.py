"""
第二章 传输线理论 - 史密斯圆图与阻抗匹配
=========================================
基于梁昌洪《简明微波》第二章第6节

本文件覆盖：
1. 史密斯圆图绘制 (scikit-rf)
2. 阻抗匹配网络设计 (λ/4 变换器、渐进线匹配)
3. 负载匹配计算
4. 驻波与失配损耗
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Arc, Wedge
import skrf as rf
from skrf.data import materials
import warnings
warnings.filterwarnings('ignore')

plt.rcParams.update({
    'font.size': 12,
    'axes.titlesize': 13,
    'axes.labelsize': 11,
    'figure.figsize': (14, 7),
    'axes.grid': True,
    'grid.alpha': 0.3,
})

# ============================================================
# 1. 史密斯圆图基础
# ============================================================

def draw_smith_chart(ax=None, label_z=True, label_Y=False, 
                     chart_type='zy', n_pts=500):
    """
    绘制史密斯圆图 (阻抗版或导纳版)
    
    参数:
        ax: matplotlib Axes 对象
        chart_type: 'zy' (阻抗) 或 'yy' (导纳) 或 'zyyy' (双端口)
    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(9, 9))
    
    # 圆图背景
    ax.set_aspect('equal')
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    
    # 圆图边框
    circle_border = Circle((0, 0), 1, fill=False, 
                           edgecolor='black', linewidth=2)
    ax.add_patch(circle_border)
    
    # 归一化阻抗圆 (r = const)
    if chart_type in ['zy', 'zyyy']:
        for r_val in [0, 0.2, 0.5, 1, 2, 5]:
            # 等电阻圆: (u - r/(1+r))^2 + v^2 = 1/(1+r)^2
            center_x = r_val / (1 + r_val)
            radius = 1 / (1 + r_val)
            theta = np.linspace(0, 2*np.pi, n_pts)
            # 只画单位圆内的部分
            u = center_x + radius * np.cos(theta)
            v = radius * np.sin(theta)
            # 过滤掉圆外的点
            mask = (u**2 + v**2) <= 1.0
            u = u[mask]
            v = v[mask]
            ax.plot(u, v, 'gray', lw=0.8, alpha=0.6)
            if label_z and r_val > 0:
                # 在圆图边缘标注
                angle = np.arctan2(0.5, center_x - 0.5)
                px = center_x + radius * np.cos(angle)
                py = radius * np.sin(angle)
                if px**2 + py**2 < 0.95:
                    ax.text(px, py, f'{r_val}', fontsize=8, 
                           ha='center', va='bottom', color='blue', alpha=0.8)
    
    # 等电抗圆 (x = const) - 阻抗圆
    if chart_type in ['zy', 'zyyy']:
        for x_val in [0.2, 0.5, 1, 2, 5]:
            for sign in [1, -1]:
                # 等电抗圆: (u - 1/(2x))^2 + (v - sign/(2x))^2 = 1/(2x)^2
                x = x_val * sign
                center_x = 1 / (2 * x)
                center_y = sign / (2 * x)
                radius = abs(1 / (2 * x))
                theta = np.linspace(0, 2*np.pi, n_pts)
                u = center_x + radius * np.cos(theta)
                v = center_y + radius * np.sin(theta)
                # 只画单位圆内的部分
                mask = (u**2 + v**2) <= 1.0
                if mask.sum() > 2:
                    u = u[mask]
                    v = v[mask]
                    ax.plot(u, v, 'gray', lw=0.6, alpha=0.5)
                if label_z and x_val > 0:
                    # 在圆图外标注
                    angles = np.linspace(-np.pi/2, np.pi/2, 100)
                    u_edge = 1.05 * np.cos(angles)
                    v_edge = 1.05 * np.sin(angles)
    
    # 导纳圆 (g = const, b = const)
    if chart_type in ['yy', 'zyyy']:
        for g_val in [0.5, 1, 2]:
            center_x = -g_val / (1 + g_val)
            radius = 1 / (1 + g_val)
            theta = np.linspace(0, 2*np.pi, n_pts)
            u = center_x + radius * np.cos(theta)
            v = radius * np.sin(theta)
            mask = (u**2 + v**2) <= 1.0
            u = u[mask]
            v = v[mask]
            ax.plot(u, v, 'lightblue', lw=0.8, alpha=0.6)
    
    # 主刻度线
    # 水平线 (实部轴)
    ax.axhline(0, color='black', lw=1.2, alpha=0.7)
    # 垂直线 (虚部轴)
    ax.axvline(0, color='black', lw=1.2, alpha=0.7)
    
    # 标记特殊点
    special_points = [
        (1, 0, '1'),          # 匹配点 (中心)
        (-1, 0, '-1'),         # 开路点
        (0, 1, 'j1'),         # 感性
        (0, -1, '-j1'),       # 容性
        (0, 0, '0'),          # 短路点
    ]
    
    for px, py, label in special_points:
        ax.plot(px, py, 'k.', markersize=5)
        # ax.text(px * 1.15, py * 1.15, label, fontsize=9, ha='center', va='center')
    
    # 角度刻度 (外向)
    for deg in np.arange(0, 360, 10):
        rad = np.deg2rad(deg)
        x1 = 1.02 * np.cos(rad)
        y1 = 1.02 * np.sin(rad)
        x2 = 1.08 * np.cos(rad)
        y2 = 1.08 * np.sin(rad)
        ax.plot([x1, x2], [y1, y2], 'k-', lw=0.8)
        if deg % 45 == 0:
            ax.text(x2 * 1.12, y2 * 1.12, f'{deg}°', fontsize=8, ha='center', va='center')
    
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_title('Smith Chart (归一化阻抗 Z)', fontsize=14, pad=10)
    
    # 添加标签
    ax.text(0, 1.18, '感性 (+jX)', ha='center', va='bottom', fontsize=10, color='red')
    ax.text(0, -1.18, '容性 (-jX)', ha='center', va='top', fontsize=10, color='blue')
    ax.text(1.18, 0, '电阻性 (>1)', ha='left', va='center', fontsize=10, color='green')
    ax.text(-1.18, 0, '电阻性 (<1)', ha='right', va='center', fontsize=10, color='purple')
    
    return ax


def normalize_impedance(Z, Z0):
    """归一化阻抗 z = Z / Z0"""
    return Z / Z0


def denormalize_impedance(z, Z0):
    """反归一化"""
    return z * Z0


def gamma_to_z(gamma):
    """
    反射系数 Γ → 归一化阻抗 z
    z = (1 + Γ) / (1 - Γ)
    """
    return (1 + gamma) / (1 - gamma)


def z_to_gamma(z):
    """
    归一化阻抗 z → 反射系数 Γ
    Γ = (z - 1) / (z + 1)
    """
    return (z - 1) / (z + 1)


# ============================================================
# 例题 2.7: 史密斯圆图定位
# ============================================================


import os
os.makedirs('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures', exist_ok=True)
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_smith_chart.png', dpi=150, bbox_inches='tight')
print('Figure saved.')
def example_smith_chart_basic():
    """
    例题: 在史密斯圆图上标出以下归一化阻抗值
    z1 = 1 + j1 (匹配点右上方)
    z2 = 0.5 - j0.5 (下左)
    z3 = 2 + j0 (右实轴)
    z4 = 0 - j1 (下纯虚轴)
    """
    z_points = [
        complex(1, 1),
        complex(0.5, -0.5),
        complex(2, 0),
        complex(0, -1),
        complex(0, 0),  # 短路
        complex(1, 0),  # 匹配点
    ]
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    
    # 左: 自制圆图
    ax1 = axes[0]
    draw_smith_chart(ax1)
    
    colors = ['red', 'blue', 'green', 'orange', 'black', 'purple']
    labels = ['z₁=1+j1', 'z₂=0.5-j0.5', 'z₃=2+j0', 'z₄=-j1', '短路', '匹配']
    
    for i, z in enumerate(z_points):
        gamma = z_to_gamma(z)
        u = np.real(gamma)
        v = np.imag(gamma)
        ax1.plot(u, v, 'o', color=colors[i], markersize=10)
        ax1.annotate(labels[i], (u, v), xytext=(5, 5), 
                    textcoords='offset points', fontsize=10, color=colors[i])
    
    ax1.set_title('手绘史密斯圆图 - 阻抗定位', fontsize=13)
    
    # 右: scikit-rf 的 Smith Chart
    ax2 = axes[1]
    
    # 创建 Network 用 skrf 画
    try:
        # 使用 skrf 画圆图
        freq = rf.Frequency(1, 10, 10, 'GHz')
        gamma_vals = np.array([z_to_gamma(z) for z in z_points])
        
        # 绘制复平面上散点
        ax2.set_aspect('equal')
        ax2.set_xlim(-1.5, 1.5)
        ax2.set_ylim(-1.5, 1.5)
        
        # 圆图边框
        circle = Circle((0, 0), 1, fill=False, edgecolor='black', lw=2)
        ax2.add_patch(circle)
        ax2.axhline(0, color='k', lw=0.8)
        ax2.axvline(0, color='k', lw=0.8)
        
        for i, (z, gamma) in enumerate(zip(z_points, gamma_vals)):
            ax2.plot(np.real(gamma), np.imag(gamma), 'o', 
                    color=colors[i], markersize=10)
            ax2.annotate(labels[i], (np.real(gamma), np.imag(gamma)),
                       xytext=(5, 5), textcoords='offset points', fontsize=10)
        
        ax2.set_title('复平面反射系数 Γ', fontsize=13)
        ax2.set_xlabel('Re{Γ}')
        ax2.set_ylabel('Im{Γ}')
    except Exception as e:
        ax2.text(0, 0, f'skrf unavailable\n{e}', ha='center', va='center')
    
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_smith_chart_basic.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_smith_chart_basic.png")
    
    return None


# ============================================================
# 例题 2.8: 负载在圆图上的轨迹
# ============================================================

def example_load_trajectory():
    """
    例题: 负载 ZL = 50 - j30 Ω, Z0 = 50Ω
    从负载向源移动 λ/8, λ/4, 3λ/8, 求相应的 Γ 和 Zin
    在圆图上标出轨迹
    """
    Z0 = 50.0
    ZL = complex(50, -30)
    
    z_norm = normalize_impedance(ZL, Z0)
    gamma_0 = z_to_gamma(z_norm)
    
    print(f"Z0 = {Z0} Ω, ZL = {ZL} Ω")
    print(f"归一化阻抗 z = {z_norm}")
    print(f"负载反射系数 Γ0 = {gamma_0}")
    print(f"|Γ0| = {np.abs(gamma_0):.4f}, ∠Γ0 = {np.angle(gamma_0)*180/np.pi:.2f}°")
    
    # 无耗线相位常数
    beta = 1.0  # 归一化 β=1 rad/m
    distances = [0, 0.125, 0.25, 0.375]  # λ 单位
    distance_names = ['负载处', 'λ/8', 'λ/4', '3λ/8']
    
    results = []
    for d, name in zip(distances, distance_names):
        gamma_d = gamma_0 * np.exp(-2j * np.pi * d)  # β*d = 2π/λ * d
        z_d = gamma_to_z(gamma_d)
        Zin_d = z_d * Z0
        results.append({
            'name': name,
            'd_lambda': d,
            'gamma': gamma_d,
            'z': z_d,
            'Zin': Zin_d
        })
        print(f"\n{d}: {name}")
        print(f"  Γ(d) = {gamma_d}")
        print(f"  z(d) = {z_d}")
        print(f"  Zin(d) = {Zin_d}")
    
    # 画图
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    
    # 左: 圆图轨迹
    ax1 = axes[0]
    draw_smith_chart(ax1)
    
    # 画出 Γ 轨迹 (顺时针旋转)
    theta_vals = np.linspace(0, -2*np.pi*0.375, 100)
    gamma_traj = gamma_0 * np.exp(1j * theta_vals)
    ax1.plot(np.real(gamma_traj), np.imag(gamma_traj), 'g--', lw=1.5, alpha=0.7)
    
    colors_p = ['red', 'blue', 'green', 'orange']
    for i, r in enumerate(results):
        ax1.plot(np.real(r['gamma']), np.imag(r['gamma']), 'o',
                color=colors_p[i], markersize=12)
        ax1.annotate(r['name'], 
                    (np.real(r['gamma']), np.imag(r['gamma'])),
                    xytext=(8, 8), textcoords='offset points',
                    fontsize=10, color=colors_p[i])
    
    ax1.set_title(f'负载轨迹: Z_L={ZL.real}-j{abs(ZL.imag):.0f}Ω, Z_0={Z0}Ω', fontsize=12)
    
    # 右: 阻抗变化
    ax2 = axes[1]
    d_lambda = [r['d_lambda'] for r in results]
    Zin_real = [np.real(r['Zin']) for r in results]
    Zin_imag = [np.imag(r['Zin']) for r in results]
    
    ax2.plot(d_lambda, Zin_real, 'b-o', lw=2, markersize=8, label=r'Re{$Z_{in}$}')
    ax2.plot(d_lambda, Zin_imag, 'r--s', lw=2, markersize=8, label=r'Im{$Z_{in}$}')
    ax2.axhline(y=Z0, color='gray', linestyle=':', label=f'Z0={Z0}Ω')
    ax2.set_xlabel(r'$d/\lambda$ (distance from load)')
    ax2.set_ylabel(r'$Z_{in}$ [Ω]')
    ax2.set_title('Input Impedance vs Distance')
    ax2.legend()
    
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_load_trajectory.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("\n图已保存: wb94_load_trajectory.png")
    
    return results


# ============================================================
# 例题 2.9: λ/4 阻抗变换器
# ============================================================

def example_quarter_wave_transformer():
    """
    例题: 设计 λ/4 阻抗匹配器
    负载 ZL = 100 Ω, 源阻抗 ZS = 50 Ω
    求变换器特性阻抗 Zm
    """
    ZL = 100.0
    ZS = 50.0
    
    # λ/4 变换器: Zm = sqrt(ZS * ZL)
    Zm = np.sqrt(ZS * ZL)
    
    print(f"λ/4 阻抗变换器设计:")
    print(f"  ZS = {ZS} Ω, ZL = {ZL} Ω")
    print(f"  Zm = sqrt({ZS} × {ZL}) = {Zm:.4f} Ω")
    
    # 验证: 输入阻抗 = ZS
    Zin_check = Zm**2 / ZL
    print(f"  验证: Zin = Zm²/ZL = {Zin_check:.4f} Ω")
    
    return Zm


def example_quarter_wave_transformer_broadband():
    """
    例题: 多节 λ/4 阶梯变换器 (切比雪夫设计)
    设计 3 节 λ/4 变换器，匹配 50Ω 到 100Ω
    """
    ZS = 50.0
    ZL = 100.0
    N = 3  # 节数
    
    # 等效阶梯阻抗 (算术平均近似)
    ratios = [np.power(ZL / ZS, k / (N + 1)) for k in range(1, N + 1)]
    
    Z_inter = [ZS * ratios[k] for k in range(N)]
    
    print(f"{N} 节 λ/4 阶梯变换器:")
    print(f"  输入阻抗 ZS = {ZS} Ω")
    for i, Z in enumerate(Z_inter):
        print(f"  第 {i+1} 节: Z = {Z:.4f} Ω")
    print(f"  输出阻抗 ZL = {ZL} Ω")
    
    return Z_inter


# ============================================================
# 例题 2.10: 单支节调配器
# ============================================================

def example_single_stub_matcher():
    """
    例题: 设计单支节调配器
    负载 ZL = 50 - j30 Ω, Z0 = 50 Ω
    用并联开路线或短路线进行匹配
    
    图解法: 在圆图上找到 YL，然后旋转到g=1的等电导圆
    """
    Y0 = 1.0 / 50.0  # 归一化导纳
    YL = 1.0 / complex(50, -30)
    
    print(f"归一化导纳:")
    print(f"  Y0 = {Y0:.6f} S (归一化)")
    print(f"  YL = {YL:.6f} S")
    print(f"  负载导纳 YL = {np.real(YL):.4f} + j{np.imag(YL):.4f}")
    
    # 对应于 zL 在圆图上的位置
    zL = 1.0 / YL
    gamma = z_to_gamma(zL)
    
    print(f"  归一化阻抗 zL = {zL}")
    print(f"  反射系数 Γ = {gamma}")
    
    # 计算并联短截线的位置和长度
    # 需要找到从负载向源移动 d1，使得归一化导纳的实部为 1
    # 即: Y(d1) = 1 + jB
    # 然后并联一个短截线提供 -jB 的电纳
    
    print("\n调配步骤:")
    print("  1) 将负载导纳 YL 转换到圆图上")
    print("  2) 沿等反射系数圆旋转至 g=1 等实部圆")
    print("  3) 确定 d1 和短截线长度")
    print("  4) 用解析法计算具体数值")
    
    return YL


# ============================================================
# 例题 2.11: VSWR 与回波损耗
# ============================================================

def example_vswr_return_loss():
    """
    例题: 已知 VSWR = 2.5, 求 |Γ|, 回波损耗 RL, 传输功率百分比
    """
    VSWR = 2.5
    
    # |Γ| = (VSWR - 1) / (VSWR + 1)
    Gamma_mag = (VSWR - 1) / (VSWR + 1)
    
    # 回波损耗 RL = -20*log|Γ| dB
    RL = -20 * np.log10(Gamma_mag)
    
    # 传输功率 (相对于最大功率)
    # P_trans / P_inc = 1 - |Γ|²
    power_trans_ratio = 1 - Gamma_mag**2
    power_trans_dB = 10 * np.log10(power_trans_ratio)
    
    print(f"VSWR = {VSWR}:")
    print(f"  |Γ| = {Gamma_mag:.6f}")
    print(f"  回波损耗 RL = {RL:.4f} dB")
    print(f"  传输功率比 = {power_trans_ratio:.6f} ({power_trans_dB:.4f} dB)")
    print(f"  反射功率比 = {Gamma_mag**2:.6f}")
    
    return Gamma_mag, RL, power_trans_ratio


# ============================================================
# 例题 2.12: 双支节调配器图解
# ============================================================

def example_double_stub_matcher():
    """
    例题: 双支节调配器设计
    Z0 = 50 Ω, ZL = 30 - j20 Ω
    支节间距 l1 = λ/8, 求支节长度
    
    步骤:
    1) 找到负载导纳 YL
    2) 将 YL 旋转到第一个支节位置 (加上传输线长度 l1)
    3) 用图解法确定两个支节的电纳值
    4) 计算支节长度
    """
    Z0 = 50.0
    ZL = complex(30, -20)
    
    # 归一化
    zL = ZL / Z0
    yL = 1 / zL
    
    print(f"Z0 = {Z0} Ω, ZL = {ZL} Ω")
    print(f"归一化导纳 yL = {yL}")
    
    # 第一个支节位置: 旋转 l1 = λ/8 对应的电长度
    # Γ旋转: Γ(l1) = Γ0 * exp(-2j*β*l1) = Γ0 * exp(-j*π/2) = -j*Γ0
    # 对应导纳: Y' = yL / (1 - Γ旋转的某些关系)
    
    # 解析: Y(d) = Y0 * (1 + Γ(d)) / (1 - Γ(d))
    # 其中 Γ(d) = Γ0 * exp(-2jβd)
    gamma_0 = z_to_gamma(zL)
    
    l1 = 0.125  # λ/8
    beta_l1 = 2 * np.pi * l1
    gamma_at_l1 = gamma_0 * np.exp(-2j * beta_l1)
    y_at_l1 = gamma_to_z(gamma_at_l1)  # 这其实是归一化阻抗
    
    # y = 1/z
    y_at_l1 = 1 / gamma_to_z(gamma_at_l1)  # 正确
    y_at_l1 = gamma_to_z(gamma_at_l1)
    # 重新计算
    gamma_at_l1 = gamma_0 * np.exp(-2j * np.pi * l1)  # β=2π/λ
    z_rotated = gamma_to_z(gamma_at_l1)
    y_rotated = 1 / z_rotated
    
    print(f"\n旋转 l1 = {l1}λ 后的导纳:")
    print(f"  y = {y_rotated}")
    print(f"  g = {np.real(y_rotated):.4f}, b = {np.imag(y_rotated):.4f}")
    
    # 双支节: 目标是将导纳变换到 Z0 (匹配)
    # 需要两个支节提供恰当的电纳
    
    print("\n双支节调配需要:")
    print("  支节1位置: d1 处提供电纳 B1")
    print("  支节2位置: d2 处提供电纳 B2")
    print("  两个支节间距 l = λ/8")
    
    return y_rotated


if __name__ == '__main__':
    print("=" * 60)
    print(" 史密斯圆图与阻抗匹配 例题")
    print("=" * 60)
    
    print("\n--- 例题 2.7: 史密斯圆图定位 ---")
    example_smith_chart_basic()
    
    print("\n--- 例题 2.8: 负载轨迹 ---")
    example_load_trajectory()
    
    print("\n--- 例题 2.9: λ/4 变换器 ---")
    example_quarter_wave_transformer()
    
    print("\n--- 例题 2.9b: 多节 λ/4 变换器 ---")
    example_quarter_wave_transformer_broadband()
    
    print("\n--- 例题 2.10: 单支节调配 ---")
    example_single_stub_matcher()
    
    print("\n--- 例题 2.11: VSWR 与回波损耗 ---")
    example_vswr_return_loss()
    
    print("\n--- 例题 2.12: 双支节调配 ---")
    example_double_stub_matcher()