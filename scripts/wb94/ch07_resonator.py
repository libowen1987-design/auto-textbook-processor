"""
第七章 微波谐振器
================================================
基于梁昌洪《简明微波》第七章内容

本文件覆盖：
1. 传输线型谐振器 (λ/4 短路谐振器、λ/2 开路谐振器)
2. 同轴线谐振器
3. 矩形波导谐振腔 (RE_{mnp} 模)
4. 品质因数 Q 的计算 (导体损耗、介质损耗)
5. 谐振频率与空腔尺寸设计
6. 微带线谐振器
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc, Wedge
from scipy.optimize import brentq, minimize_scalar
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
eta_0 = np.sqrt(mu_0 / epsilon_0)

# ============================================================
# 1. 传输线型谐振器
# ============================================================

def resonator_frequency_from_length(l, epsilon_r=1.0, mode='lambda/2'):
    """
    根据谐振器长度计算谐振频率
    
    参数:
        l: 谐振器长度 [m]
        epsilon_r: 相对介电常数
        mode: 'lambda/2' (半波长) 或 'lambda/4' (四分之一波长)
    """
    if mode == 'lambda/2':
        lambda_g = 2 * l
    elif mode == 'lambda/4':
        lambda_g = 4 * l
    else:
        lambda_g = 2 * l
    
    f_res = c / (lambda_g / np.sqrt(epsilon_r))
    return f_res


def Q_from_conductor_loss(resonator_type, f_res, sigma_cond=None, 
                           Z0=None, length=None, a=None, b=None,
                           delta_s=None, R_s=None):
    """
    计算导体损耗品质因数 Q_c
    
    参数:
        resonator_type: 'coaxial', 'microstrip', 'rectangular_cavity', 'waveguide'
        f_res: 谐振频率 [Hz]
    """
    if sigma_cond is None:
        sigma_cond = 5.8e7  # 铜
    
    omega = 2 * np.pi * f_res
    mu_0 = 4e-7 * np.pi
    
    # 集肤深度
    if delta_s is None:
        delta_s = np.sqrt(2 / (omega * mu_0 * sigma_cond))
    
    # 表面电阻
    if R_s is None:
        R_s = 1 / (sigma_cond * delta_s)
    
    if resonator_type == 'coaxial' and Z0 is not None and length is not None:
        # 同轴线谐振器 (λ/2 开路或 λ/4 短路)
        # α_c = R_s/(2π) * (1/r1 + 1/r2) / (Z0 * ln(r2/r1))
        # Q_c = β / (2 * α_c) = π / (α_c * λ_g)
        alpha_c = 0.01  # placeholder - need geometric info
        Q_c = np.pi / (alpha_c * (c / f_res))
    
    elif resonator_type == 'microstrip':
        # 微带线谐振器 Q
        # Q_c ≈ (π * Z0 / R_s) / (λ_g)
        if Z0 is None:
            Z0 = 50.0
        lambda_g = c / f_res
        Q_c = np.pi * Z0 / (R_s * lambda_g)
    
    elif resonator_type == 'rectangular_cavity' and a is not None and b is not None:
        # 矩形空腔 Q 值 (TE_mnp 模)
        # Q ≈ (k * a * b * l) / (2 * R_s) * (工作模式相关因子)
        # 对于 TE101 模 (立方体 a=b=l):
        l_cav = a  # 假设立方体
        volume = a * b * l_cav
        surface_area = 2 * (a*b + b*l_cav + a*l_cav)
        
        # TE101 Q 近似
        k = 2 * np.pi * f_res * np.sqrt(epsilon_0 * mu_0)
        Q_c = k * volume / (R_s * surface_area) * 0.7  # 经验因子
        
    else:
        Q_c = 1e4  # 默认值
    
    return Q_c, delta_s, R_s


def Q_from_dielectric_loss(tan_delta):
    """
    介质损耗品质因数
    Q_d = 1 / tan_delta
    """
    return 1 / tan_delta if tan_delta > 0 else np.inf


# ============================================================
# 例题 7.1: λ/4 短路传输线谐振器
# ============================================================

def example_lambda_quarter_resonator():
    """
    例题: 同轴线 λ/4 短路谐振器, Z0=50Ω, f_res=5GHz
    计算所需长度 l (空气填充)
    """
    f_res = 5e9
    Z0 = 50.0
    
    # λ/4 长度
    lambda_0 = c / f_res
    l = lambda_0 / 4
    
    print(f"λ/4 短路同轴线谐振器:")
    print(f"  谐振频率 f_res = {f_res/1e9:.1f} GHz")
    print(f"  自由空间波长 λ0 = {lambda_0*1e3:.2f} mm")
    print(f"  谐振长度 l = λ0/4 = {l*1e3:.2f} mm")
    
    # 验证
    beta = 2 * np.pi / lambda_0
    Zin = 1j * Z0 * np.tan(beta * l)
    print(f"  短路输入阻抗 Zin = {Zin:.4f} Ω (应→∞)")
    
    # 计算等效并联 RLC 参数
    # R = Z0 / (2 * α_c * l) etc.
    
    return l


# ============================================================
# 例题 7.2: 同轴线谐振器 (半波长)
# ============================================================

def example_coaxial_resonator():
    """
    例题: 同轴线 λ/2 谐振器
    内导体半径 r1 = 1mm, 外导体内半径 r2 = 3.5mm
    空气填充, 求 f_res = 3 GHz 时的所需长度
    """
    global mu_0, epsilon_0
    r1 = 1e-3   # 1 mm
    r2 = 3.5e-3 # 3.5 mm
    f_res = 3e9
    
    lambda_0 = c / f_res
    l = lambda_0 / 2  # 半波长
    
    # 特性阻抗
    Z0 = (1 / (2 * np.pi)) * np.sqrt(mu_0 / epsilon_0) * np.log(r2 / r1)
    
    print(f"同轴线 λ/2 谐振器:")
    print(f"  r1 = {r1*1e3:.1f} mm, r2 = {r2*1e3:.1f} mm")
    print(f"  特性阻抗 Z0 = {Z0:.4f} Ω")
    print(f"  f_res = {f_res/1e9:.1f} GHz, λ0 = {lambda_0*1e3:.2f} mm")
    print(f"  λ/2 长度 l = {l*1e3:.2f} mm")
    
    # 导体衰减 (趋肤效应)
    sigma_cu = 5.8e7
    mu_r = 1.0
    mu_0 = 4e-7 * np.pi
    omega = 2 * np.pi * f_res
    delta = np.sqrt(2 / (omega * mu_0 * mu_r * sigma_cu))
    Rs = 1 / (sigma_cu * delta)
    
    # 同轴线导体衰减常数
    alpha_c = Rs / (2 * np.pi) * (1/r1 + 1/r2) / (Z0 * np.log(r2/r1))
    
    print(f"\n导体损耗:")
    print(f"  集肤深度 δ = {delta*1e6:.4f} μm")
    print(f"  表面电阻 Rs = {Rs:.4f} Ω")
    print(f"  衰减常数 α_c = {alpha_c:.6f} Np/m = {alpha_c*8.686:.4f} dB/m")
    
    # Q 值
    beta = 2 * np.pi / lambda_0
    Q_c = beta / (2 * alpha_c)
    print(f"  导体 Q 值 Q_c ≈ {Q_c:.0f}")
    
    return l, Z0, Q_c


# ============================================================
# 例题 7.3: 矩形波导谐振腔 (TE101 模)
# ============================================================

def example_rectangular_cavity():
    """
    例题: 矩形空腔谐振器, 设计 TE101 模在 f=10GHz 谐振
    X-band 波导尺寸 a×b, 求腔长度 d
    """
    f_res = 10e9
    
    # X-band 尺寸
    a = 22.86e-3   # 2.286 cm
    b = 10.16e-3   # 1.016 cm
    
    # TE_mnp 模的谐振频率
    # f_mnp = (c/2) * sqrt((m/a)^2 + (n/b)^2 + (p/d)^2)
    
    # 对于 TE101 模 (m=1, n=0, p=1)
    m, n, p = 1, 0, 1
    
    # 求 d
    # f_res = (c/2) * sqrt((m/a)^2 + (n/b)^2 + (p/d)^2)
    # (2*f_res/c)^2 = (m/a)^2 + (p/d)^2
    # (p/d)^2 = (2*f_res/c)^2 - (m/a)^2
    k_res = 2 * f_res / c
    
    term_mn = (m / a)**2
    d_squared = p**2 / (k_res**2 - term_mn)
    d = np.sqrt(d_squared)
    
    print(f"矩形空腔 TE{m}{n}{p} 模设计:")
    print(f"  谐振频率 f_res = {f_res/1e9:.1f} GHz")
    print(f"  波导尺寸 a = {a*1e3:.2f} mm, b = {b*1e3:.2f} mm")
    print(f"  腔长度 d = {d*1e3:.2f} mm")
    
    # 验证
    f_check = (c/2) * np.sqrt((m/a)**2 + (n/b)**2 + (p/d)**2)
    print(f"  验证 f_res = {f_check/1e9:.4f} GHz")
    
    # 立方体空腔 (a=b=d) 的 TE101 谐振频率
    a_cube = c / (f_res * np.sqrt(2))  # f = c/(a*sqrt(2)) for TE101 cube
    print(f"\n若为立方体空腔 (a=b=d):")
    print(f"  边长 a = {a_cube*1e3:.2f} mm")
    print(f"  体积 V = {a_cube**3*1e6:.2f} cm³")
    
    # Q 值计算 (导体损耗)
    sigma_cu = 5.8e7
    mu_r = 1.0
    omega = 2 * np.pi * f_res
    delta = np.sqrt(2 / (omega * mu_0 * mu_r * sigma_cu))
    Rs = 1 / (sigma_cu * delta)
    
    # 表面面积
    S = 2 * (a*b + b*d + a*d)
    V = a * b * d
    
    # TE101 Q 值 (近似)
    k = 2 * np.pi * f_res / c
    Q_c = k * V / (Rs * S) * 0.5  # 经验系数
    
    print(f"\n品质因数估算:")
    print(f"  集肤深度 δ = {delta*1e6:.4f} μm")
    print(f"  表面电阻 Rs = {Rs:.4f} Ω")
    print(f"  Q_c ≈ {Q_c:.0f}")
    
    return a, b, d, Q_c


# ============================================================
# 例题 7.4: 微带线谐振器 Q 值
# ============================================================

def example_microstrip_resonator():
    """
    例题: 微带线谐振器 ε_r=9.6, h=0.5mm, Z0=50Ω
    f=5GHz, tanδ=0.001, 计算 Q 值
    """
    epsilon_r = 9.6
    h = 0.5e-3
    f_res = 5e9
    tan_delta = 0.001
    
    # 特性阻抗 Z0=50Ω 对应的 w/h 比
    # 近似: 对于高介电常数基片, w/h ≈ 1 对应 Z0 ≈ 50Ω
    w_h_ratio = 1.0  # 近似
    w = w_h_ratio * h
    
    # 相速度
    eps_eff = (epsilon_r + 1) / 2  # 近似
    vp = c / np.sqrt(eps_eff)
    
    # λ/2 长度
    lambda_g = vp / f_res
    l = lambda_g / 2
    
    print(f"微带线 λ/2 谐振器:")
    print(f"  ε_r = {epsilon_r}, h = {h*1e3:.1f} mm")
    print(f"  f_res = {f_res/1e9:.1f} GHz")
    print(f"  w/h ≈ {w_h_ratio:.2f}, w ≈ {w*1e3:.2f} mm")
    print(f"  有效介电常数 ε_eff ≈ {eps_eff:.2f}")
    print(f"  相速度 v_p = {vp/1e8:.4f} × 10⁸ m/s")
    print(f"  λ/2 长度 l = {l*1e3:.2f} mm")
    
    # 介质 Q
    Q_d = 1 / tan_delta
    print(f"\n介质品质因数 Q_d = 1/tanδ = {Q_d:.0f}")
    
    # 导体 Q (近似)
    sigma_cu = 5.8e7
    omega = 2 * np.pi * f_res
    mu_0 = 4e-7 * np.pi
    delta = np.sqrt(2 / (omega * mu_0 * sigma_cu))
    Rs = 1 / (sigma_cu * delta)
    
    Z0_est = 50.0  # 目标阻抗
    lambda_g_m = lambda_g
    Q_c = np.pi * Z0_est / (Rs * lambda_g_m)
    
    print(f"导体品质因数 Q_c ≈ {Q_c:.0f}")
    
    # 总 Q (导体 + 介质)
    Q_total = 1 / (1/Q_c + 1/Q_d)
    print(f"总 Q ≈ {Q_total:.0f}")
    
    return l, Q_total


# ============================================================
# 例题 7.5: 圆形波导谐振腔 (TE011 模)
# ============================================================

def example_circular_cavity():
    """
    例题: 圆形空腔, TE011 模, f=10GHz
    设计腔半径 R 和长度 d
    """
    f_res = 10e9
    
    # TE011 模的截止波数
    # 对于圆波导, TE0n 的根值为 χ₀₁ = 3.83171
    chi_01 = 3.83171
    
    # TE011 谐振: f_res = (c/2π) * sqrt(k_c^2 + (pπ/d)^2)
    # k_c = χ₀₁ / R
    # 当 p=0 (TE011), f_res = (c/2π) * χ₀₁ / R
    # R = χ₀₁ * c / (2π * f_res)
    
    R = chi_01 * c / (2 * np.pi * f_res)
    
    print(f"圆形空腔 TE011 模设计:")
    print(f"  谐振频率 f_res = {f_res/1e9:.1f} GHz")
    print(f"  χ₀₁ (TE01 根) = {chi_01:.5f}")
    print(f"  腔半径 R = {R*1e3:.2f} mm")
    
    # 对于 TE011, 可以选择任意 d (只要支持 p 方向模式)
    # 选择 d 使得只有一个模式
    d = 2 * R  # 长度 = 2R
    
    # 验证
    k_c = chi_01 / R
    k_res = 2 * np.pi * f_res / c
    
    # TE011: p=0, 所以 β=0, k_res = k_c
    f_check = (c / (2 * np.pi)) * k_c
    print(f"  腔长度 d = {d*1e3:.2f} mm (选择 d=2R)")
    print(f"  验证 f_res = {f_check/1e9:.4f} GHz")
    
    # Q 值 (TE011 是高 Q 模式, 无壁电流的轴向分量)
    sigma_cu = 5.8e7
    omega = 2 * np.pi * f_res
    mu_0 = 4e-7 * np.pi
    delta = np.sqrt(2 / (omega * mu_0 * sigma_cu))
    Rs = 1 / (sigma_cu * delta)
    
    volume = np.pi * R**2 * d
    surface = 2 * np.pi * R * d + 2 * np.pi * R**2
    
    Q_c = (k_c * volume) / (Rs * surface) * 0.7
    
    print(f"\n品质因数:")
    print(f"  Q_c ≈ {Q_c:.0f}")
    
    return R, d, Q_c


# ============================================================
# 绘图: 谐振器频率 vs 尺寸
# ============================================================

def plot_resonator_frequency():
    """
    绘制: 同轴线 λ/2 谐振器长度 vs 谐振频率
    """
    f_vals = np.linspace(1e9, 20e9, 300)  # 1-20 GHz
    lambda_0 = c / f_vals
    l_half = lambda_0 / 2  # 半波长
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    ax1 = axes[0]
    ax1.plot(f_vals/1e9, l_half*1e3, 'b-', lw=2)
    ax1.set_xlabel(r'$f_{res}$ [GHz]')
    ax1.set_ylabel(r'$l$ [mm]')
    ax1.set_title(r'同轴线 $\lambda/2$ 谐振器长度 vs 频率')
    ax1.grid(True)
    
    # 标注几个点
    for f_mark in [5, 10, 15]:
        l_mark = c / (2 * f_mark*1e9) * 1e3
        ax1.annotate(f'{f_mark}GHz: {l_mark:.1f}mm', 
                     (f_mark, l_mark), xytext=(f_mark+0.5, l_mark+2),
                     arrowprops=dict(arrowstyle='->', color='red'),
                     fontsize=9)
    
    # 右: 不同模式对比
    ax2 = axes[1]
    
    l_half_vals = lambda_0 / 2
    l_quarter_vals = lambda_0 / 4
    
    ax2.plot(f_vals/1e9, l_half_vals*1e3, 'b-', lw=2, label=r'$\lambda/2$ 模式')
    ax2.plot(f_vals/1e9, l_quarter_vals*1e3, 'r--', lw=2, label=r'$\lambda/4$ 模式')
    ax2.set_xlabel(r'$f_{res}$ [GHz]')
    ax2.set_ylabel(r'$l$ [mm]')
    ax2.set_title('传输线谐振器长度对比')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_resonator_frequency.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_resonator_frequency.png")


# ============================================================
# 绘图: 矩形空腔 TE101 模场结构
# ============================================================

def plot_rectangular_cavity_fields():
    """
    绘制矩形空腔 TE101 模的场分布示意图
    """
    fig = plt.figure(figsize=(12, 5))
    
    # 3D 场分布示意
    ax1 = fig.add_subplot(121, projection='3d')
    
    # 简化的场分布 (沿 x,z 方向)
    x = np.linspace(0, 1, 20)
    z = np.linspace(0, 1, 20)
    X, Z = np.meshgrid(x, z)
    
    # TE101: Ey ~ sin(πx) * sin(πz)
    Ey = np.sin(np.pi * X) * np.sin(np.pi * Z)
    
    ax1.plot_surface(X, Z, Ey, cmap='hot', alpha=0.8)
    ax1.set_xlabel(r'$x/a$')
    ax1.set_ylabel(r'$z/d$')
    ax1.set_zlabel(r'$E_y$')
    ax1.set_title(r'TE101 模电场分布 $E_y \propto \sin(\pi x)\sin(\pi z)$')
    
    # 俯视图 (截面场线)
    ax2 = fig.add_subplot(122)
    
    # 画矩形腔
    rect = Rectangle((0, 0), 1, 0.5, fill=False, edgecolor='black', lw=2)
    ax2.add_patch(rect)
    
    # 电场强度热图
    x2 = np.linspace(0, 1, 50)
    z2 = np.linspace(0, 1, 50)
    X2, Z2 = np.meshgrid(x2, z2)
    Ey2 = np.abs(np.sin(np.pi * X2) * np.sin(np.pi * Z2))
    
    contour = ax2.contourf(X2, Z2, Ey2, levels=15, cmap='hot')
    plt.colorbar(contour, ax=ax2, label=r'$|E_y|$')
    ax2.set_xlabel(r'$x/a$')
    ax2.set_ylabel(r'$z/d$')
    ax2.set_title(r'TE101 模 $|E_y|$ 分布 (俯视图)')
    
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_rect_cavity_te101.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_rect_cavity_te101.png")


if __name__ == '__main__':
    print("=" * 60)
    print(" 第七章 微波谐振器 例题")
    print("=" * 60)
    
    print("\n--- 例题 7.1: λ/4 短路传输线谐振器 ---")
    example_lambda_quarter_resonator()
    
    print("\n--- 例题 7.2: 同轴线 λ/2 谐振器 ---")
    example_coaxial_resonator()
    
    print("\n--- 例题 7.3: 矩形空腔 TE101 模 ---")
    example_rectangular_cavity()
    
    print("\n--- 例题 7.4: 微带线谐振器 ---")
    example_microstrip_resonator()
    
    print("\n--- 例题 7.5: 圆形空腔 TE011 模 ---")
    example_circular_cavity()
    
    print("\n--- 谐振器长度 vs 频率 (生成图) ---")
    plot_resonator_frequency()
    
    print("\n--- 矩形空腔 TE101 场结构 (生成图) ---")
    plot_rectangular_cavity_fields()