"""
第三章 规则金属波导 - 矩形波导与圆波导传输特性
================================================
基于梁昌洪《简明微波》第三章内容

本文件覆盖：
1. 矩形波导 TE/TM 模的截止波长和截止频率
2. 场分量计算与场结构绘图
3. 圆波导 TE/TM 模
4. 导体衰减与介质衰减
5. 传输功率与功率容量
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D
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

c = 3e8  # 光速 m/s

# ============================================================
# 1. 矩形波导基本参数
# ============================================================

def rectangular_waveguide_dimensions(band='X'):
    """
    常用标准矩形波导尺寸
    
    参数:
        band: 波段代号 ('X', 'Ku', 'Ka', 'K', 'Q', 'U')
    
    返回:
        dict: a, b (单位: m)
    """
    specs = {
        'X':   {'a': 22.86e-3, 'b': 10.16e-3},  # X-band
        'Ku':  {'a': 15.799e-3, 'b': 7.899e-3},  # Ku-band
        'Ka':  {'a': 10.668e-3, 'b': 4.318e-3},  # Ka-band
        'K':   {'a': 9.525e-3, 'b': 4.763e-3},   # K-band
        'Q':   {'a': 7.214e-3, 'b': 3.404e-3},   # Q-band
        'U':   {'a': 5.132e-3, 'b': 2.565e-3},   # U-band
    }
    return specs.get(band.upper(), specs['X'])


def cutoff_frequency_rect(m, n, a, b, epsilon_r=1.0):
    """
    矩形波导 TE_mn / TM_mn 模的截止频率
    
    f_c = (c / (2 * sqrt(epsilon_r))) * sqrt((m/a)^2 + (n/b)^2)
    
    参数:
        m, n: 模指数
        a, b: 波导宽边和窄边尺寸 [m]
        epsilon_r: 相对介电常数
    """
    fc = (c / (2 * np.sqrt(epsilon_r))) * np.sqrt((m / a)**2 + (n / b)**2)
    return fc


def cutoff_wavelength_rect(m, n, a, b):
    """
    矩形波导模的截止波长
    
    lambda_c = 2 / sqrt((m/a)^2 + (n/b)^2)
    """
    return 2.0 / np.sqrt((m / a)**2 + (n / b)**2)


def guide_wavelength(f, m, n, a, b, epsilon_r=1.0):
    """
    波导波长 (在波导中测量的波长)
    
    lambda_g = lambda / sqrt(1 - (f_c/f)^2)
    其中 lambda 是自由空间波长
    """
    lambda_0 = c / f
    fc = cutoff_frequency_rect(m, n, a, b, epsilon_r)
    
    if f <= fc:
        return np.inf  # 截止以下不传输
    
    lambda_g = lambda_0 / np.sqrt(1 - (fc / f)**2)
    return lambda_g


def phase_constant_beta(f, m, n, a, b, epsilon_r=1.0):
    """
    相位常数 β = 2π / lambda_g
    β = k * sqrt(1 - (f_c/f)^2) = k * sqrt(1 - (lambda_0/lambda_c)^2)
    """
    k = 2 * np.pi * f * np.sqrt(epsilon_r) / c  # 自由空间波数
    fc = cutoff_frequency_rect(m, n, a, b, epsilon_r)
    
    if f <= fc:
        return 0.0
    
    beta = k * np.sqrt(1 - (fc / f)**2)
    return beta


def propagation_constant_gamma(f, m, n, a, b, epsilon_r=1.0, alpha_loss=0.0):
    """
    传播常数 γ = α + jβ
    """
    fc = cutoff_frequency_rect(m, n, a, b, epsilon_r)
    
    if f <= fc:
        return complex(alpha_loss, 0.0)  # 截止，非传播
    
    beta = phase_constant_beta(f, m, n, a, b, epsilon_r)
    return complex(alpha_loss, beta)


# ============================================================
# 例题 3.1: X-band 波导截止频率
# ============================================================

def example_rect_waveguide_cutoff():
    """
    例题: X-band 空气铜制矩形波导 a=22.86mm, b=10.16mm
    求前四个导模的截止频率
    工作频率 f=10 GHz 时 1m 长波导的 dB 衰减
    """
    a = 22.86e-3   # 2.286 cm
    b = 10.16e-3   # 1.016 cm
    
    print(f"X-band 矩形波导: a={a*1e3:.2f}mm, b={b*1e3:.2f}mm")
    
    # TE 模截止频率
    modes = [
        (0, 1, 'TE01'),
        (1, 0, 'TE10'),
        (1, 1, 'TE11/TM11'),
        (0, 2, 'TE02'),
        (2, 0, 'TE20'),
    ]
    
    print("\n导模截止频率:")
    for m, n, name in modes:
        fc = cutoff_frequency_rect(m, n, a, b)
        lambda_c = cutoff_wavelength_rect(m, n, a, b)
        print(f"  {name}: f_c = {fc/1e9:.4f} GHz, λ_c = {lambda_c*1e3:.4f} mm")
    
    # 判断单模传输
    f = 10e9  # 10 GHz
    print(f"\nf = {f/1e9:.1f} GHz (自由空间 λ = {c/f*1e3:.2f} mm)")
    
    # 找主模
    fc01 = cutoff_frequency_rect(0, 1, a, b)
    fc10 = cutoff_frequency_rect(1, 0, a, b)
    
    print(f"TE01: f_c = {fc01/1e9:.4f} GHz")
    print(f"TE10: f_c = {fc10/1e9:.4f} GHz")
    
    # 确定单模带宽
    print(f"\n单模传输: TE01 (f_c={fc01/1e9:.3f}GHz) 为主模")
    print(f"  单模带宽: {fc01/1e9:.3f} GHz < f < {fc10/1e9:.3f} GHz")
    
    # 衰减计算 (导体衰减)
    sigma_cu = 5.8e7  # 铜电导率
    mu_r = 1.0
    mu_0 = 4e-7 * np.pi
    
    # 集肤深度 delta
    omega = 2 * np.pi * f
    delta = np.sqrt(2 / (omega * mu_0 * mu_r * sigma_cu))
    
    # 表面电阻 Rs
    Rs = 1 / (sigma_cu * delta)
    
    print(f"\n导体损耗计算 (f={f/1e9:.0f}GHz):")
    print(f"  集肤深度 δ = {delta*1e6:.4f} μm")
    print(f"  表面电阻 Rs = {Rs:.4f} Ω")
    
    # TE01 模的导体衰减 (近似公式)
    # α_c ≈ Rs / (b * Z0) * (1 + (2b/a) * (f_c/f)^2) / sqrt(1 - (f_c/f)^2)
    # 先计算波导波长
    lambda_g = guide_wavelength(f, 0, 1, a, b)
    beta = 2 * np.pi / lambda_g
    
    # 特性导纳
    Z0_TE = 377 / np.sqrt(1.0)  # 近似 TEM 特性阻抗
    
    # 精确公式需要用场分量积分，这里用近似
    # α_c (Np/m) for TE_m0: Rs/(a*Z0*sqrt(1-(fc/f)^2)) * (1 + m^2 * (f_c/f)^2)
    f_c = fc01
    ratio = f_c / f if f > 0 else 0.0
    
    # TE01 衰减 (精确公式)
    alpha_c = (Rs / (2 * b * Z0_TE)) * (1 + (2 * b / a) * ratio**2) / np.sqrt(1 - ratio**2)
    alpha_c_dB = alpha_c * 8.686  # Np/m → dB/m
    
    print(f"\nTE01 衰减 (导体损耗):")
    print(f"  α_c = {alpha_c:.6f} Np/m = {alpha_c_dB:.4f} dB/m")
    print(f"  1m 波导衰减: {alpha_c_dB:.4f} dB")
    
    return {
        'a': a, 'b': b, 'modes': modes,
        'delta': delta, 'Rs': Rs, 'alpha_c_dB': alpha_c_dB
    }


# ============================================================
# 例题 3.2: 矩形波导场结构绘图
# ============================================================

def plot_te10_field_structure():
    """
    绘制 TE10 模的场结构图 (电场线 + 磁场线)
    TE10: Ex=0, Ey≠0, Ez=0
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    a, b = 22.86e-3, 10.16e-3
    # 归一化坐标
    x_norm = np.linspace(0, 1, 50)
    y_norm = np.linspace(0, 1, 30)
    X, Y = np.meshgrid(x_norm, y_norm)
    
    # TE10: Ey ~ sin(π*x/a) * cos(π*y/b) ... actually for TE10:
    # Ey = E0 * sin(π*x/a)  (only m=1, n=0)
    # 电场在宽边中央最大，两侧为零
    Ey = np.sin(np.pi * X)  # TE10
    
    # 磁场分量 Hx, Hz
    Hx = -np.cos(np.pi * X)  # Hx ~ cos(π*x/a)
    Hz = np.zeros_like(X)   # TE10 has no Hz
    
    # 电场线 (电场方向为 Ey direction, 即 y-direction)
    ax1 = axes[0]
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, b/a)
    ax1.set_xlabel(r'$x/a$')
    ax1.set_ylabel(r'$y/b$')
    ax1.set_title(r'TE10 模 - 电场 $|E_y|$ 分布')
    ax1.set_aspect('equal')
    
    # 画波导截面
    rect = Rectangle((0, 0), 1, b/a, fill=False, edgecolor='black', lw=2)
    ax1.add_patch(rect)
    
    # 电场强度热图
    contour = ax1.contourf(X, Y * (b/a), np.abs(Ey), levels=20, cmap='hot')
    plt.colorbar(contour, ax=ax1, label=r'$|E_y|$')
    
    # 磁场线 (磁力线沿 x 方向)
    ax2 = axes[1]
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, b/a)
    ax2.set_xlabel(r'$x/a$')
    ax2.set_ylabel(r'$y/b$')
    ax2.set_title(r'TE10 模 - 磁场 $|H_x|$ 分布')
    ax2.set_aspect('equal')
    
    rect2 = Rectangle((0, 0), 1, b/a, fill=False, edgecolor='black', lw=2)
    ax2.add_patch(rect2)
    
    contour2 = ax2.contourf(X, Y * (b/a), np.abs(Hx), levels=20, cmap='coolwarm')
    plt.colorbar(contour2, ax=ax2, label=r'$|H_x|$')
    
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_rect_te10_field.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_rect_te10_field.png")


# ============================================================
# 例题 3.3: 波导波长与相速度
# ============================================================

def example_guide_wavelength():
    """
    例题: X-band 波导 a=22.86mm, f=10 GHz
    计算 TE10 模的波导波长、相速度和群速度
    """
    a = 22.86e-3
    b = 10.16e-3
    f = 10e9
    
    # 自由空间波长
    lambda_0 = c / f
    print(f"f = {f/1e9:.1f} GHz, λ0 = {lambda_0*1e3:.2f} mm")
    
    # TE10 截止频率
    fc = cutoff_frequency_rect(1, 0, a, b)
    lambda_c = cutoff_wavelength_rect(1, 0, a, b)
    print(f"TE10: f_c = {fc/1e9:.4f} GHz, λ_c = {lambda_c*1e3:.2f} mm")
    
    # 波导波长
    lg = guide_wavelength(f, 1, 0, a, b)
    print(f"波导波长 λ_g = {lg*1e3:.2f} mm")
    
    # 相速度 v_p = c / sqrt(1 - (f_c/f)^2)
    vp = c / np.sqrt(1 - (fc / f)**2)
    print(f"相速度 v_p = {vp/1e8:.4f} × 10⁸ m/s = {vp/1e6:.2f} Mm/s")
    print(f"         v_p / c = {vp/c:.4f}")
    
    # 群速度 v_g = c * sqrt(1 - (f_c/f)^2)
    vg = c * np.sqrt(1 - (fc / f)**2)
    print(f"群速度 v_g = {vg/1e8:.4f} × 10⁸ m/s = {vg/1e6:.2f} Mm/s")
    print(f"         v_g / c = {vg/c:.4f}")
    
    # 检验: v_p * v_g = c²
    print(f"验证: v_p × v_g / c² = {vp * vg / c**2:.4f}")
    
    return {'lambda_0': lambda_0, 'lambda_g': lg, 'vp': vp, 'vg': vg}


# ============================================================
# 2. 圆波导
# ============================================================

def cutoff_frequency_circular(m, n_p, R, epsilon_r=1.0):
    """
    圆波导 TE_mn / TM_mn 模的截止频率
    
    f_c = (χ_mn * c) / (2π * R * sqrt(epsilon_r))
    其中 χ_mn 是 m 阶贝塞尔函数 (或其导数) 的第 n 个根
    
    TE: χ_mn 是 J_m 的第 n 个根
    TM: χ_mn 是 J_m' 的第 n 个根
    """
    # 贝塞尔函数根
    # TE_mn: χ_mn = J_m 的第 n 个根 (径向零值)
    # TM_mn: χ_mn = J_m' 的第 n 个根 (径向导数零值)
    pass  # 需要 scipy


def bessel_zeros(m, n):
    """返回 m 阶贝塞尔函数 J_m 的第 n 个正零值"""
    # 近似值表 (用于 TE_mn)
    table = {
        (0, 1): 2.40483,
        (0, 2): 5.52008,
        (0, 3): 8.65373,
        (1, 1): 3.83171,
        (1, 2): 7.01559,
        (1, 3): 10.1735,
        (2, 1): 5.13562,
        (2, 2): 8.41724,
        (3, 1): 6.38016,
    }
    return table.get((m, n), 5.0)  # 默认值


def bessel_derivative_zeros(m, n):
    """返回 m 阶贝塞尔函数导数 J_m' 的第 n 个正零值"""
    # 用于 TM_mn
    table = {
        (0, 1): 0.0,          # J_0' = -J_1
        (0, 2): 3.83171,
        (0, 3): 7.01559,
        (1, 1): 1.84118,
        (1, 2): 5.33144,
        (1, 3): 8.53632,
        (2, 1): 3.05424,
        (2, 2): 6.70613,
        (3, 1): 4.20119,
    }
    return table.get((m, n), 3.8)


def example_circular_waveguide():
    """
    例题: 圆波导半径 R=5cm, 求 TE11, TM01, TE01 模的截止频率
    """
    R = 5e-2  # 5 cm
    
    modes = [
        ('TE', 1, 1),
        ('TM', 0, 1),
        ('TE', 0, 1),
        ('TE', 2, 1),
    ]
    
    print(f"圆波导: R = {R*1e2:.1f} cm")
    
    for mode_type, m, n in modes:
        if mode_type == 'TE':
            chi = bessel_zeros(m, n)
        else:  # TM
            chi = bessel_derivative_zeros(m, n)
        
        lambda_c = 2 * np.pi * R / chi
        fc = c / lambda_c
        
        print(f"  {mode_type}{m}{n}: χ={chi:.5f}, λ_c={lambda_c*1e2:.2f} cm, f_c={fc/1e9:.4f} GHz")
    
    return None


# ============================================================
# 例题 3.4: 圆波导 TE11 模场结构
# ============================================================

def plot_circular_te11_field():
    """
    绘制圆波导 TE11 模的场结构
    """
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    
    R = 1.0  # 归一化半径
    r = np.linspace(0, 1, 100)
    theta = np.linspace(0, 2*np.pi, 100)
    R_grid, THETA = np.meshgrid(r, theta)
    
    # TE11: Ez ~ J1(k_r*r) * cos(theta)
    # k_r = χ11 / R, χ11 ≈ 1.84118
    chi = 1.84118
    k_r = chi / R
    
    # TE11 电场幅值 (简化)
    Ez = np.sin(chi * R_grid) * np.cos(THETA)  # 简化近似
    
    X = R_grid * np.cos(THETA)
    Y = R_grid * np.sin(THETA)
    
    # 波导截面圆
    circle = Circle((0, 0), 1, fill=False, edgecolor='black', lw=2)
    ax.add_patch(circle)
    
    # 电场分布
    contour = ax.contourf(X, Y, Ez, levels=20, cmap='RdBu_r', alpha=0.8)
    plt.colorbar(contour, ax=ax, label=r'$E_z$')
    
    ax.set_aspect('equal')
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_xlabel(r'$x/R$')
    ax.set_ylabel(r'$y/R$')
    ax.set_title(r'圆波导 TE11 模 - 电场 $E_z$ 分布')
    
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_circular_te11_field.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_circular_te11_field.png")


# ============================================================
# 例题 3.5: 波导传输功率与功率容量
# ============================================================

def example_waveguide_power():
    """
    例题: X-band 波导 TE10 模, f=10 GHz
    求最大安全传输功率 (空气击穿场强 ~ 30 kV/cm)
    
    P_max = (1/2) * (E_max^2 / Z0_TE) * a * b * (这里需要精确公式)
    """
    a = 22.86e-3
    b = 10.16e-3
    f = 10e9
    
    # 空气击穿场强 (峰值)
    E_br = 30e3  # 30 kV/cm = 3e6 V/m
    
    # TE10 模电场幅值与传输功率的关系
    # P = (1/2) * (ab/4) * (E_y_max^2 / Z_TE)
    # 其中 Z_TE =377 / sqrt(1 - (fc/f)^2)
    
    fc = cutoff_frequency_rect(1, 0, a, b)
    Z_TE = 377 / np.sqrt(1 - (fc/f)**2)
    
    # 峰值电场
    E_peak = E_br
    P_peak = (1/2) * (a * b / 2) * (E_peak**2) / Z_TE
    
    print(f"TE10 波导功率容量:")
    print(f"  波导尺寸: a={a*1e3:.2f}mm, b={b*1e3:.2f}mm")
    print(f"  工作频率: f={f/1e9:.1f}GHz")
    print(f"  截止频率: f_c={fc/1e9:.4f}GHz")
    print(f"  TE模特性阻抗: Z_TE={Z_TE:.2f}Ω")
    print(f"  空气击穿场强: E_br={E_br/1e6:.1f}MV/m")
    print(f"  峰值功率容量: P_max≈{P_peak/1e6:.2f} MW")
    
    # 实际安全工作功率 (取 1/3 安全性)
    P_safe = P_peak / 3
    print(f"  安全工作功率 (1/3): P≈{P_safe/1e6:.2f} MW")
    
    return P_peak


# ============================================================
# 例题 3.6: 多模传输特性对比
# ============================================================

def example_multi_mode_comparison():
    """
    比较矩形波导中 TE10, TE01, TE11 模的传输特性随频率变化
    """
    a = 22.86e-3
    b = 10.16e-3
    
    f_vals = np.linspace(5e9, 20e9, 200)  # 5-20 GHz
    
    modes = [
        (1, 0, 'TE10'),
        (0, 1, 'TE01'),
        (1, 1, 'TE11'),
        (2, 0, 'TE20'),
    ]
    
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    
    ax1, ax2 = axes
    
    for m, n, name in modes:
        fc = cutoff_frequency_rect(m, n, a, b)
        lg_vals = [guide_wavelength(f, m, n, a, b) for f in f_vals]
        
        # β 值
        beta_vals = np.array([phase_constant_beta(f, m, n, a, b) for f in f_vals])
        
        # 归一化: f/fc
        f_norm = f_vals / fc
        
        ax1.plot(f_norm, np.array(lg_vals)*1e3, label=name, lw=1.5)
        ax2.plot(f_norm, beta_vals / 1e3, label=name, lw=1.5)
    
    ax1.axvline(x=1, color='gray', linestyle='--', alpha=0.5, label='f=f_c')
    ax1.set_xlabel(r'$f/f_c$')
    ax1.set_ylabel(r'$\lambda_g$ [mm]')
    ax1.set_title(r'波导波长 $\lambda_g$ vs $f/f_c$ (X-band)')
    ax1.legend()
    
    ax2.axvline(x=1, color='gray', linestyle='--', alpha=0.5)
    ax2.set_xlabel(r'$f/f_c$')
    ax2.set_ylabel(r'$\beta$ [rad/mm]')
    ax2.set_title(r'相位常数 $\beta$ vs $f/f_c$ (X-band)')
    ax2.legend()
    
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_multi_mode_comparison.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_multi_mode_comparison.png")


# ============================================================
# 例题 3.7: 矩形波导场分量 (完整公式)
# ============================================================

def te_mn_fields(x, y, z, m, n, a, b, f, E0=1.0, epsilon_r=1.0):
    """
    计算 TE_mn 模的场分量
    
    x, y, z: 位置坐标 (m)
    m, n: 模指数
    a, b: 波导尺寸 (m)
    f: 工作频率 (Hz)
    E0: 振幅常数
    """
    k0 = 2 * np.pi * f * np.sqrt(epsilon_r) / c
    fc = cutoff_frequency_rect(m, n, a, b, epsilon_r)
    
    if f <= fc:
        return {comp: 0.0 for comp in ['Ex','Ey','Ez','Hx','Hy','Hz']}
    
    kc = np.pi * np.sqrt((m/a)**2 + (n/b)**2)
    beta = np.sqrt(k0**2 - kc**2)
    
    # 传播方向相位
    beta_z = beta * z
    
    # TE 模: Ez = 0, Hz ≠ 0
    # 使用 sin/cos 组合
    if m == 0:
        f_x = lambda x: np.cos(m * np.pi * x / a)
    else:
        f_x = lambda x: np.sin(m * np.pi * x / a)
    
    if n == 0:
        f_y = lambda y: np.cos(n * np.pi * y / b)
    else:
        f_y = lambda y: np.sin(n * np.pi * y / b)
    
    # TE_mn 场分量 (简化)
    # E_x ∝ (jωμ / kc^2) * (nπ/b) * H0 * sin(mπx/a) * cos(nπy/b)
    # E_y ∝ -(jωμ / kc^2) * (mπ/a) * H0 * cos(mπx/a) * sin(nπy/b)
    # E_z = 0
    
    freq_const = 2e-7 * np.pi * f  # ωμ / kc^2 的简化
    
    Ex = freq_const * (n / b) * np.sin(m * np.pi * x / a) * np.cos(n * np.pi * y / b) * np.exp(-1j * beta_z)
    Ey = -freq_const * (m / a) * np.cos(m * np.pi * x / a) * np.sin(n * np.pi * y / b) * np.exp(-1j * beta_z)
    Ez = 0.0
    
    Hx = freq_const * (m / a) * np.cos(m * np.pi * x / a) * np.sin(n * np.pi * y / b) * np.exp(-1j * beta_z)
    Hy = freq_const * (n / b) * np.sin(m * np.pi * x / a) * np.cos(n * np.pi * y / b) * np.exp(-1j * beta_z)
    Hz = 1j * freq_const * E0 * np.cos(m * np.pi * x / a) * np.cos(n * np.pi * y / b) * np.exp(-1j * beta_z)
    
    return {'Ex': Ex, 'Ey': Ey, 'Ez': Ez,
            'Hx': Hx, 'Hy': Hy, 'Hz': Hz}


if __name__ == '__main__':
    print("=" * 60)
    print(" 第三章 规则金属波导 例题")
    print("=" * 60)
    
    print("\n--- 例题 3.1: X-band 矩形波导截止频率 ---")
    example_rect_waveguide_cutoff()
    
    print("\n--- 例题 3.2: TE10 场结构绘图 ---")
    plot_te10_field_structure()
    
    print("\n--- 例题 3.3: 波导波长与相速度 ---")
    example_guide_wavelength()
    
    print("\n--- 例题 3.4: 圆波导 TE11 场结构 ---")
    plot_circular_te11_field()
    
    print("\n--- 例题 3.5: 波导功率容量 ---")
    example_waveguide_power()
    
    print("\n--- 例题 3.6: 多模传输特性对比 ---")
    example_multi_mode_comparison()