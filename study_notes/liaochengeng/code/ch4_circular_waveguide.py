"""
第4章 圆波导 (Circular Waveguide)
基于廖承恩《微波技术基础》第3章圆波导部分

内容：
- TE_mn 和 TM_mn 模的截止波长/频率
- 场分量表达式
- 主模 TE11 的极化简并
- 传输功率与衰减计算
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, pi, mu_0, epsilon_0

# ============================================================
# 圆波导参数计算
# ============================================================

def bessel_zeros(m, n):
    """返回 m 阶贝塞尔函数第 n 个根 (J_m(x)=0 的根)"""
    # 对于 TM 模，使用 J_m 的根
    table = {
        (0,1): 2.4048, (0,2): 5.5201, (0,3): 8.6537,
        (1,1): 3.8317, (1,2): 7.0156, (1,3): 10.1735,
        (2,1): 5.1356, (2,2): 8.4172,
        (3,1): 6.3802,
    }
    return table.get((m,n), None)

def bessel_prime_zeros(m, n):
    """返回 m 阶贝塞尔函数导数第 n 个根 (J'_m(x)=0 的根)"""
    table = {
        (0,1): 3.8317, (0,2): 7.0156, (0,3): 10.1735,
        (1,1): 1.8412, (1,2): 5.3314, (1,3): 8.5363,
        (2,1): 3.0542, (2,2): 6.7061,
        (3,1): 4.2012,
    }
    return table.get((m,n), None)

def te_mode_cutoff(a, m, n):
    """
    TE_mn 模的截止波长
    a: 波导半径 (m)
    m: 场沿圆周分布的整波数 (m>=0)
    n: 场沿半径分布的最大值个数
    截止波长 λ_c = 2π a / χ'_mn
    """
    chi = bessel_prime_zeros(m, n)
    if chi is None:
        return np.inf
    return 2 * pi * a / chi

def tm_mode_cutoff(a, m, n):
    """
    TM_mn 模的截止波长
    λ_c = 2π a / χ_mn
    """
    chi = bessel_zeros(m, n)
    if chi is None:
        return np.inf
    return 2 * pi * a / chi

def te_mode_cutoff_freq(a, m, n):
    """TE_mn 模的截止频率 f_c = c / λ_c"""
    lam_c = te_mode_cutoff(a, m, n)
    if lam_c == np.inf:
        return 0.0
    return c / lam_c

def tm_mode_cutoff_freq(a, m, n):
    """TM_mn 模的截止频率"""
    lam_c = tm_mode_cutoff(a, m, n)
    if lam_c == np.inf:
        return 0.0
    return c / lam_c

def te_mode_propagation_constant(f, a, m, n, epsilon_r=1.0):
    """
    TE_mn 模的传播常数 β
    f: 工作频率 (Hz)
    a: 波导半径 (m)
    k = 2π√(ε_r)/λ, β = √(k² - k_c²)
    """
    k = 2 * pi * f * np.sqrt(epsilon_r * epsilon_0 * mu_0)  # 自由空间波数
    chi = bessel_prime_zeros(m, n)
    if chi is None:
        return None
    k_c = chi / a  # 截止波数
    if k <= k_c:
        return None  # 截止，消失模
    return np.sqrt(k**2 - k_c**2)

def te_mode_wave_impedance(f, a, m, n, epsilon_r=1.0):
    """
    TE_mn 模的波阻抗 Z_TE = ωμ / β
    """
    beta = te_mode_propagation_constant(f, a, m, n, epsilon_r)
    if beta is None:
        return None
    omega = 2 * pi * f
    return omega * mu_0 / beta

# ============================================================
# 例题 3.2-1: 半径 0.5cm，填充 ε_r=2.25 的圆波导
# ============================================================

def example_3_2_1():
    a = 0.005  # 5mm radius
    eps_r = 2.25
    tan_delta = 0.001
    f = 13.0e9  # 13 GHz

    print("=" * 60)
    print("例题 3.2-1: 圆波导传输特性计算")
    print(f"半径 a = {a*100:.1f} cm")
    print(f"相对介电常数 ε_r = {eps_r}")
    print(f"损耗角正切 tanδ = {tan_delta}")
    print(f"工作频率 f = {f/1e9:.1f} GHz")
    print()

    # 前两个传输模: TE11 和 TM01
    modes = [('TE', 1, 1), ('TM', 0, 1)]
    for mode_type, m, n in modes:
        if mode_type == 'TE':
            lam_c = te_mode_cutoff(a, m, n)
            f_c = te_mode_cutoff_freq(a, m, n)
        else:
            lam_c = tm_mode_cutoff(a, m, n)
            f_c = tm_mode_cutoff_freq(a, m, n)
        print(f"{mode_type}{m}{n} 模:")
        print(f"  截止波长 λ_c = {lam_c*100:.4f} cm")
        print(f"  截止频率 f_c = {f_c/1e9:.4f} GHz")

        if f > f_c:
            print(f"  在 f={f/1e9:.1f} GHz 可传输")
            if mode_type == 'TE':
                beta = te_mode_propagation_constant(f, a, m, n, eps_r)
                omega = 2 * pi * f
                # 介质衰减
                alpha_d = omega * np.sqrt(epsilon_0 * mu_0) * (tan_delta / 2) * np.sqrt(eps_r)
                # 导体衰减 (镀银, σ=6.17e7 S/m)
                sigma = 6.17e7
                delta_s = np.sqrt(2 / (omega * mu_0 * sigma))
                R_s = 1 / (sigma * delta_s)
                # 简化: alpha_c ≈ R_s / (a * η) * (1 + (f_c/f)^2) 类型的近似
                # 这里用工程近似
                k = 2 * pi * f * np.sqrt(eps_r) / c
                k_c = 2 * pi / lam_c
                alpha_c = R_s / (a * 377) * (1 + 0.5*(k_c/k)**2)
                alpha_total = alpha_c + alpha_d
                L = 0.5  # 50 cm
                loss_dB = 20 * np.log10(np.exp(alpha_total * L))
                print(f"  介质衰减常数 α_d ≈ {alpha_d*1000:.4f} Np/m")
                print(f"  导体衰减常数 α_c ≈ {alpha_c*1000:.4f} Np/m")
                print(f"  总衰减常数 α ≈ {alpha_total*1000:.4f} Np/m")
                print(f"  50cm 长度损耗 ≈ {loss_dB:.2f} dB")
        else:
            print(f"  在 f={f/1e9:.1f} GHz 已截止，不可传输")
        print()

# ============================================================
# 主模 TE11 场结构图
# ============================================================

def plot_te11_field_structure():
    """绘制 TE11 模的场结构示意"""
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    fig.suptitle(r"圆波导 TE$_{11}$ 模场结构", fontsize=14)

    # 横向截面场线
    ax = axes[0]
    theta = np.linspace(0, 2*pi, 100)
    r = np.linspace(0, 1, 20)
    R, TH = np.meshgrid(r, theta)
    # 简化的场线: E_r ∝ J_1(χ'11 r/a) cos(θ)
    chi_11 = 1.8412
    E_r = np.cos(TH) * np.sin(pi * R * chi_11)
    ax.contour(R*np.cos(TH), R*np.sin(TH), E_r, levels=10, colors='red')
    ax.contour(R*np.cos(TH), R*np.sin(TH), -E_r, levels=10, colors='blue', linestyles='--')
    circle = plt.Circle((0,0), 1, fill=False, color='black', linewidth=2)
    ax.add_patch(circle)
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect('equal')
    ax.set_title(r'$E_r$ 电力线 (横向截面)')
    ax.axis('off')

    # 轴向截面 Ez 分布
    ax = axes[1]
    x = np.linspace(-1, 1, 100)
    z = np.linspace(0, 2, 50)
    X, Z = np.meshgrid(x, z)
    # 简化的 Ez 分布
    Ez = np.cos(pi * X) * np.sin(0.5 * pi * Z)
    ax.contour(X, Z, Ez, levels=10, colors='red')
    ax.contour(X, Z, -Ez, levels=10, colors='blue', linestyles='--')
    ax.axvline(x=0, color='black', linewidth=2, linestyle='-')
    ax.axhline(y=0, color='black', linewidth=1)
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, 2)
    ax.set_aspect('equal')
    ax.set_title(r'$E_z$ 电场分布 (轴向截面)')
    ax.set_xlabel('r/a')
    ax.set_ylabel('z/λ')

    # 磁场 H_φ 分布
    ax = axes[2]
    RHO = np.linspace(0, 1, 50)
    THETA = np.linspace(0, 2*pi, 50)
    RHO_M, TH_M = np.meshgrid(RHO, THETA)
    # H_φ ∝ -χ'11 J_1'(χ'11 ρ) cos(θ)
    H_phi = -np.cos(TH_M) * np.cos(pi/2 * RHO_M)
    ax.contour(RHO_M*np.cos(TH_M), RHO_M*np.sin(TH_M), H_phi,
               levels=10, colors='green')
    circle = plt.Circle((0,0), 1, fill=False, color='black', linewidth=2)
    ax.add_patch(circle)
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_aspect('equal')
    ax.set_title(r'$H_\phi$ 磁力线 (横向截面)')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liaochengeng/code/ch4_te11_field.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("已保存 ch4_te11_field.png")

# ============================================================
# 主模 TE11 和 TM01 截止波长比较
# ============================================================

def plot_cutoff_comparison():
    """比较不同模式的截止波长"""
    a = 0.025  # 半径 2.5 cm
    modes = [
        ('TE', 1, 1, r'TE$_{11}$ (主模)'),
        ('TM', 0, 1, r'TM$_{01}$'),
        ('TE', 0, 1, r'TE$_{01}$ (高次模)'),
        ('TM', 1, 1, r'TM$_{11}$'),
        ('TE', 2, 1, r'TE$_{21}$'),
    ]
    lam_c = []
    labels = []
    for mode_type, m, n, label in modes:
        if mode_type == 'TE':
            lc = te_mode_cutoff(a, m, n)
        else:
            lc = tm_mode_cutoff(a, m, n)
        lam_c.append(lc * 100)  # cm
        labels.append(label)

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.barh(labels, lam_c, color=['steelblue', 'coral', 'seagreen', 'orange', 'mediumpurple'])
    ax.set_xlabel(r'截止波长 $\lambda_c$ (cm)')
    ax.set_title(f'圆波导 (a={a*100:.1f} cm) 各模式截止波长比较')
    for bar, val in zip(bars, lam_c):
        ax.text(val + 0.1, bar.get_y() + bar.get_height()/2,
                f'{val:.2f} cm', va='center', fontsize=10)
    ax.set_xlim(0, max(lam_c) * 1.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liaochengeng/code/ch4_cutoff_comparison.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("已保存 ch4_cutoff_comparison.png")

# ============================================================
# TE11 模的衰减随频率变化
# ============================================================

def plot_te11_attenuation():
    """绘制 TE11 模导体衰减随频率变化"""
    a = 0.025  # 半径
    sigma = 6.17e7  # 银的导电率
    f_c = te_mode_cutoff_freq(a, 1, 1)
    f_range = np.linspace(f_c * 1.01, 30e9, 200)

    alpha_c = []
    for f in f_range:
        omega = 2 * pi * f
        delta_s = np.sqrt(2 / (omega * mu_0 * sigma))
        R_s = 1 / (sigma * delta_s)
        # 近似公式
        beta = te_mode_propagation_constant(f, a, 1, 1)
        if beta is not None:
            k = 2 * pi * f / c
            k_c = 2 * pi / te_mode_cutoff(a, 1, 1)
            # 导体衰减近似
            alpha = (R_s / (a * 377)) * (1 + 0.5 * (k_c/k)**2) * 1000  # dB/m
            alpha_c.append(alpha)
        else:
            alpha_c.append(np.nan)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(f_range/1e9, alpha_c, 'b-', linewidth=2)
    ax.axvline(x=f_c/1e9, color='red', linestyle='--', label=f'f_c={f_c/1e9:.2f} GHz')
    ax.set_xlabel('频率 f (GHz)')
    ax.set_ylabel(r'导体衰减 $\alpha_c$ (dB/m)')
    ax.set_title(r'圆波导 TE$_{11}$ 模导体衰减随频率变化 (a=2.5cm, 镀银)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liaochengeng/code/ch4_te11_attenuation.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("已保存 ch4_te11_attenuation.png")

if __name__ == '__main__':
    print("圆波导分析 - 廖承恩《微波技术基础》第4章")
    print()

    example_3_2_1()
    plot_te11_field_structure()
    plot_cutoff_comparison()
    plot_te11_attenuation()