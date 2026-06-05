"""
第8章 阻抗匹配 (Impedance Matching)
基于廖承恩《微波技术基础》第2.6节

内容：
- 负载与传输线匹配（λ/4 阻抗变换器）
- 双支节调配器
- 渐变线匹配
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, pi

# ============================================================
# 基本公式
# ============================================================

def reflection_coefficient(ZL, Z0):
    """反射系数 Γ = (ZL - Z0) / (ZL + Z0)"""
    return (ZL - Z0) / (ZL + Z0)

def input_impedance(ZL, Z0, beta, l):
    """
    传输线输入阻抗 Z_in(l) = Z0 * (ZL + jZ0 tan(βl)) / (Z0 + jZL tan(βl))
    l: 距离负载的长度
    """
    tan_bl = np.tan(beta * l)
    return Z0 * (ZL + 1j * Z0 * tan_bl) / (Z0 + 1j * ZL * tan_bl)

def vswr(Gamma):
    """电压驻波比 VSWR = (1 + |Γ|) / (1 - |Γ|)"""
    return (1 + np.abs(Gamma)) / (1 - np.abs(Gamma))

def quarter_wave_transformer(ZL, Z0_desired):
    """
    λ/4 阻抗变换器设计
    变换器特性阻抗 Z01 = √(ZL * Z0_desired)
    """
    return np.sqrt(ZL * Z0_desired)

def single_stub_matching(ZL, Z0, f, length_only=True):
    """
    单支节匹配 - 求支节长度
    返回并联支节的归一化电纳值和长度
    l_stub: 短路线长度 (m)
    """
    Gamma = reflection_coefficient(ZL, Z0)
    mag = np.abs(Gamma)
    ang = np.angle(Gamma)

    # 归一化负载
    zl = ZL / Z0
    r = zl.real
    x = zl.imag

    # 史密斯圆图法
    # 先将负载绕圆图旋转到 r=1 的圆上
    # 需要求解位置 l1 使得输入导纳 Y_in 的实部为 1

    # Γ = |Γ|e^(jθ), d = l/lmbda
    # Y_in/Y0 = (1 - Γ e^(-j2βd)) / (1 + Γ e^(-j2βd))
    # 令 Re{Y_in/Y0} = 1 求解

    wavelength = c / f

    # 数值求解
    def real_part_condition(d):
        # Γ e^(-j2βd) = |Γ| e^(j(θ - 4πd/λ))
        beta_d = 2 * np.pi * d / wavelength
        Ge_j2bd = mag * np.exp(1j * (ang - beta_d))
        Yin_over_Y0 = (1 - Ge_j2bd) / (1 + Ge_j2bd)
        return Yin_over_Y0.real - 1.0

    # 尝试在 0 到 0.5 波长范围内找解
    d_solutions = []
    from scipy.optimize import brentq
    for start in np.arange(0, 0.5, 0.01):
        try:
            sol = brentq(real_part_condition, start, start + 0.01)
            if 0 < sol < 0.5:
                d_solutions.append(sol)
        except:
            pass

    results = []
    for d1 in d_solutions:
        l1 = d1 * wavelength

        # 计算该位置的输入导纳
        beta_d = 2 * np.pi * d1
        Ge_j2bd = mag * np.exp(1j * (ang - beta_d))
        Yin_Y0 = (1 - Ge_j2bd) / (1 + Ge_j2bd)
        Yin = Yin_Y0 * (1/Z0)

        B = Yin.imag  # 电纳
        # 并联短路支节提供的电纳应该为 -B
        # 短路支节的输入导纳 jB_stub = j * tan(βl) / Z0_stub
        # 设 Z0_stub = Z0, 则 B_stub = tan(βl) / Z0
        # 所以 tan(βl) = -B * Z0

        if abs(B) > 0:
            # 短路线 (Y_in = -j/Y0 * cot(βl) 或 j/Y0 * tan(βl))
            # 并联短路支节: Y_stub = j * B_target
            # 短路支节 Y = j * tan(βl) / Z0
            B_target = -B  # 需要提供的电纳
            tan_bl = B_target * Z0

            # 取正切值在 -π/2 到 π/2 之间的解
            if abs(tan_bl) < 1e10:
                bl = np.arctan(tan_bl)
                if bl < 0:
                    bl += np.pi  # 变为正长度
                l_stub = bl / (2 * np.pi / wavelength)
                results.append((l1, l_stub, B))

    return results

# ============================================================
# 例题计算
# ============================================================

def example_matching():
    """阻抗匹配例题"""
    Z0 = 50  # 特性阻抗
    ZL = 75 + 1j * 50  # 负载阻抗
    f = 3e9  # 3 GHz

    print("=" * 60)
    print("阻抗匹配例题")
    print(f"Z0 = {Z0} Ω, ZL = {ZL} Ω")
    print(f"频率 f = {f/1e9:.1f} GHz")
    print()

    # 反射系数
    Gamma = reflection_coefficient(ZL, Z0)
    print(f"反射系数 Γ = {Gamma:.4f}")
    print(f"|Γ| = {np.abs(Gamma):.4f}")
    print(f"VSWR = {vswr(Gamma):.2f}")
    print()

    # λ/4 变换器
    Z01 = quarter_wave_transformer(ZL.real, Z0)
    print(f"λ/4 变换器设计:")
    print(f"  对于纯电阻负载 R={ZL.real} Ω")
    print(f"  所需特性阻抗 Z01 = √(R * Z0) = √({ZL.real} * {Z0}) = {Z01:.2f} Ω")
    print()

    # 双支节匹配 (示意)
    wavelength = c / f
    print(f"波长 λ = {wavelength*100:.2f} cm")
    print()
    print("双支节调配器示意:")
    print(f"  支节间距通常取 λ/8, λ/4, 3λ/8 等")
    print(f"  通过选择两个短路支节的长度达到匹配")

# ============================================================
# 史密斯圆图可视化 (用 matplotlib 简化实现)
# ============================================================

def smith_chart_with_load(ZL, Z0=50):
    """在史密斯圆图上标注负载点"""
    Gamma = reflection_coefficient(ZL, Z0)
    gam_real = Gamma.real
    gam_imag = Gamma.imag

    fig, ax = plt.subplots(figsize=(8, 8))

    # 画史密斯圆图单位圆
    theta = np.linspace(0, 2*pi, 200)
    ax.plot(np.cos(theta), np.sin(theta), 'k-', linewidth=2)

    # 画等电阻圆 (r = const)
    for r in [0, 0.2, 0.5, 1, 2, 5]:
        center = r / (1 + r)
        radius = 1 / (1 + r)
        circle = plt.Circle((center, 0), radius, fill=False, color='steelblue', linewidth=1)
        ax.add_patch(circle)

    # 画等电抗圆 (x = const)
    for x in [0.2, 0.5, 1, 2, 5]:
        # 正电抗
        center = 1 / (1 + 1/x**2)
        radius = 1 / x / (1 + 1/x**2)
        circle = plt.Circle((center, 1/x/(1+1/x**2)), radius, fill=False, color='coral', linewidth=1)
        ax.add_patch(circle)
        # 负电抗
        circle = plt.Circle((center, -1/x/(1+1/x**2)), radius, fill=False, color='coral', linewidth=1)
        ax.add_patch(circle)

    # 画实轴
    ax.axhline(y=0, color='black', linewidth=0.5)
    ax.axvline(x=0, color='black', linewidth=0.5)

    # 负载点
    ax.plot(gam_real, gam_imag, 'ro', markersize=15, label=f'负载 Z_L={ZL}')

    # 画到原点的连线 (表示 Γ)
    ax.plot([0, gam_real], [0, gam_imag], 'r--', linewidth=1)

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect('equal')
    ax.set_title('史密斯圆图与负载阻抗')
    ax.legend(loc='upper right')
    ax.set_xlabel('Re{Γ}')
    ax.set_ylabel('Im{Γ}')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liaochengeng/code/ch8_smith_chart.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("已保存 ch8_smith_chart.png")

# ============================================================
# λ/4 变换器带宽特性
# ============================================================

def plot_qtr_transformer_bandwidth():
    """λ/4 阻抗变换器的带宽特性"""
    Z0 = 50
    R1, R2 = 25, 100  # 低频和高频负载
    Z01 = np.sqrt(R1 * R2)

    f_center = 3e9
    f_range = np.linspace(2.0e9, 4.0e9, 200)
    wavelength_center = c / f_center

    VSWR1 = []
    VSWR2 = []

    for f in f_range:
        wavelength = c / f
        beta = 2 * pi / wavelength

        # 输入阻抗 (忽略损耗)
        ZL = R1
        Gamma_in = (ZL - Z01) / (ZL + Z01)  # 简化
        Z_in = Z01 * (ZL + 1j*Z01*np.tan(beta*wavelength_center/4)) / (Z01 + 1j*ZL*np.tan(beta*wavelength_center/4))
        Gamma = (Z_in - Z0) / (Z_in + Z0)
        VSWR1.append(vswr(Gamma))

        ZL = R2
        Z_in = Z01 * (ZL + 1j*Z01*np.tan(beta*wavelength_center/4)) / (Z01 + 1j*ZL*np.tan(beta*wavelength_center/4))
        Gamma = (Z_in - Z0) / (Z_in + Z0)
        VSWR2.append(vswr(Gamma))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(f_range/1e9, VSWR1, 'b-', linewidth=2, label=f'R={R1} Ω')
    ax1.axhline(y=1.5, color='red', linestyle='--', label='VSWR=1.5')
    ax1.set_xlabel('频率 (GHz)')
    ax1.set_ylabel('VSWR')
    ax1.set_title(r'$\lambda/4$ 变换器带宽 (R1=25$\Omega$)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim(1, 5)

    ax2.plot(f_range/1e9, VSWR2, 'b-', linewidth=2, label=f'R={R2} Ω')
    ax2.axhline(y=1.5, color='red', linestyle='--', label='VSWR=1.5')
    ax2.set_xlabel('频率 (GHz)')
    ax2.set_ylabel('VSWR')
    ax2.set_title(r'$\lambda/4$ 变换器带宽 (R2=100$\Omega$)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(1, 5)

    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liaochengeng/code/ch8_transformer_bandwidth.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("已保存 ch8_transformer_bandwidth.png")

# ============================================================
# 双支节调配器示意图
# ============================================================

def plot_dual_stub_matcher():
    """双支节调配器示意图"""
    fig, ax = plt.subplots(figsize=(12, 5))

    # 主线
    ax.plot([0, 10], [0, 0], 'b-', linewidth=4)

    # 负载
    ax.plot([10, 10.5], [0, 0], 'k-', linewidth=6, label='负载')

    # 输入
    ax.plot([-0.5, 0], [0, 0], 'b-', linewidth=4, label='输入')

    # 支节1 (位置 d1)
    ax.plot([3, 3], [0, 1.5], 'r-', linewidth=3)
    ax.plot([3-0.2, 3+0.2], [1.5, 1.5], 'k-', linewidth=2)
    ax.text(3, 1.8, '短路支节1', ha='center', fontsize=10)
    ax.text(3, -0.3, r'$d_1$', ha='center', fontsize=10)

    # 支节2 (位置 d1 + λ/8)
    ax.plot([5, 5], [0, 1.5], 'r-', linewidth=3)
    ax.plot([5-0.2, 5+0.2], [1.5, 1.5], 'k-', linewidth=2)
    ax.text(5, 1.8, '短路支节2', ha='center', fontsize=10)
    ax.text(5, -0.3, r'$d_1 + \lambda/8$', ha='center', fontsize=10)

    # 标注
    ax.annotate('', xy=(10, 0.2), xytext=(7, 0.2),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(8.5, 0.5, '主传输线', fontsize=11, color='green')

    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 3)
    ax.set_title('双支节调配器示意图')
    ax.axis('off')
    ax.legend(loc='upper right')

    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liaochengeng/code/ch8_dual_stub.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("已保存 ch8_dual_stub.png")

if __name__ == '__main__':
    print("阻抗匹配 - 廖承恩《微波技术基础》第2.6节")
    print()

    example_matching()
    smith_chart_with_load(75 + 1j*50, 50)
    plot_qtr_transformer_bandwidth()
    plot_dual_stub_matcher()