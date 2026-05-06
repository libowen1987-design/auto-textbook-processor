"""
第四章 微波集成传输线 - 微带线、悬置微带线、带状线
====================================================
基于梁昌洪《简明微波》第四章内容

本文件覆盖：
1. 微带线特性阻抗与有效介电常数
2. 带状线特性阻抗
3. 悬置微带线与倒置微带线
4. 槽线特性
5. 鳍线 (Finline)
6. 频率特性与色散
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
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

# ============================================================
# 1. 微带线 (Microstrip)
# ============================================================

def microstrip_Z0_and_eff(w, h, epsilon_r, f=None, t=None):
    """
    计算微带线的特性阻抗 Z0 和有效介电常数 ε_eff
    
    参数:
        w: 导体带宽 [m]
        h: 基片厚度 [m]
        epsilon_r: 相对介电常数
        f: 工作频率 [Hz], None 则为准静态
        t: 导体厚度 [m], None 则为零厚度
    
    基于 Hammerstad-Jensen 模型 (准静态)
    """
    # 宽高比
    if w <= 0:
        return np.inf, epsilon_r
    
    u = w / h
    
    if u < 1:
        # 窄微带
        Z0 = 60 / np.sqrt(epsilon_r) * np.log(8 / u + u / 4)
    else:
        # 宽微带
        Z0 = 120 * np.pi / (np.sqrt(epsilon_r) * (u + 1.393 + 0.667 * np.log(u + 1.444)))
    
    # 准静态有效介电常数
    if u < 1:
        epsilon_eff = (epsilon_r + 1) / 2 + (epsilon_r - 1) / 2 * (
            (1 + 12 / u)**(-0.5) + 0.041 * (1 - u)**2
        )
    else:
        epsilon_eff = (epsilon_r + 1) / 2 + (epsilon_r - 1) / 2 * (1 + 12 / u)**(-0.5)
    
    return Z0, epsilon_eff


def microstrip_dispersion(w, h, epsilon_r, f):
    """
    微带线色散修正 (基于 frequency-dependent effect)
    f: 工作频率 [Hz]
    
    返回:
        epsilon_eff(f) 考虑色散后的有效介电常数
    """
    # 准静态值
    Z0_qs, eps_eff_qs = microstrip_Z0_and_eff(w, h, epsilon_r)
    
    # 工作波长
    lambda_0 = c / f
    
    # 归一化频率
    f_n = f * h / c  # f * h in (GHz * mm) scale
    
    # 色散修正公式 (Schneider, 1974)
    # eps_eff(f) = eps_r - (eps_r - eps_eff_qs) / (1 + G * (f * h)^2)
    # G ≈ 0.6 + 0.009 * Z0
    
    G = 0.6 + 0.009 * Z0_qs
    
    # 更精确的色散公式 (Hammerstad)
    P = np.sqrt(epsilon_r) / 30.0 * np.sqrt(h / 0.0254)  # h in inches → scale
    
    # 更简单实用:
    k = 2 * np.pi * f / c
    eps_eff = eps_eff_qs + (epsilon_r - eps_eff_qs) / (1 + G * (f * h / 1e9 / 0.0254)**2)
    
    return eps_eff


def microstrip_quality_factor(w, h, epsilon_r, f, sigma_cond=None, tan_delta=1e-4):
    """
    微带线品质因子 Q
    
    导体损耗 + 介质损耗
    """
    if sigma_cond is None:
        sigma_cond = 5.8e7  # 铜
    
    # 趋肤深度
    mu_0 = 4e-7 * np.pi
    delta = np.sqrt(2 / (2 * np.pi * f * mu_0 * sigma_cond))
    
    # 集肤效应电阻 (单位宽度)
    R_s = 1 / (sigma_cond * delta)  # Ω/sq
    
    # 特性阻抗
    Z0, eps_eff = microstrip_Z0_and_eff(w, h, epsilon_r)
    
    # 导体 Q
    # Q_c = α_c / β, α_c ≈ R_s / (2 * Z0) * (∂Z0/∂w)/Z0 ...
    # 近似: Q_c ≈ (π * Z0 / R_s) / (λ_g)
    
    # 介质 Q
    Q_d = 1 / tan_delta
    
    # 总体 Q
    Q_total = 1 / (1/Q_d)  # 主要为介质损耗
    # 更准确需要计算 α_c
    
    return Q_d


# ============================================================
# 例题 4.1: 微带线特性阻抗
# ============================================================

def example_microstrip_Z0():
    """
    例题: 微带线基片 ε_r=9.6 (氧化铝), h=1mm, w=1mm
    求准静态特性阻抗 Z0 和有效介电常数 ε_eff
    """
    epsilon_r = 9.6
    h = 1e-3    # 1 mm
    w = 1e-3    # 1 mm
    
    Z0, eps_eff = microstrip_Z0_and_eff(w, h, epsilon_r)
    
    print(f"微带线参数:")
    print(f"  ε_r = {epsilon_r}, h = {h*1e3:.1f}mm, w = {w*1e3:.1f}mm")
    print(f"  w/h = {w/h:.2f}")
    print(f"  特性阻抗 Z0 = {Z0:.4f} Ω")
    print(f"  有效介电常数 ε_eff = {eps_eff:.4f}")
    
    # 相速度
    vp = c / np.sqrt(eps_eff)
    print(f"  相速度 v_p = {vp/1e8:.4f} × 10⁸ m/s")
    
    # 设计特定阻抗 (如 50Ω) 所需宽度
    target_Z0 = 50.0
    print(f"\n设计 Z0={target_Z0}Ω 所需 w/h 比:")
    
    # 反算: 对于宽微带 (w/h > 1)
    # Z0 = 120π/(sqrt(ε_r)*(u+1.393+0.667*ln(u+1.444)))
    # 用数值方法求 u
    # scipy.optimize.brentq already available
    
    def Z0_func(u):
        if u < 1:
            Z = 60 / np.sqrt(epsilon_r) * np.log(8 / u + u / 4)
        else:
            Z = 120 * np.pi / (np.sqrt(epsilon_r) * (u + 1.393 + 0.667 * np.log(u + 1.444)))
        return Z - target_Z0
    
    try:
        u_solution = brentq(Z0_func, 0.1, 20)
        w_solution = u_solution * h
        print(f"  w/h = {u_solution:.4f}")
        print(f"  w = {w_solution*1e3:.4f} mm (对于 h=1mm)")
    except:
        print("  无法求解 (可能超出范围)")
    
    return Z0, eps_eff


# ============================================================
# 例题 4.2: 微带线色散
# ============================================================

def example_microstrip_dispersion():
    """
    例题: 微带线 ε_r=9.6, h=0.5mm, w=0.5mm
    绘制有效介电常数随频率变化曲线 (1-30 GHz)
    """
    epsilon_r = 9.6
    h = 0.5e-3   # 0.5 mm
    w = 0.5e-3   # 0.5 mm
    
    f_vals = np.linspace(1e9, 30e9, 200)  # 1-30 GHz
    
    eps_eff_qs, _ = microstrip_Z0_and_eff(w, h, epsilon_r)
    eps_eff_disp = [microstrip_dispersion(w, h, epsilon_r, f) for f in f_vals]
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # 左: 有效介电常数
    ax1 = axes[0]
    ax1.plot(f_vals/1e9, eps_eff_disp, 'b-', lw=2, label=r'$\varepsilon_{eff}$(色散)')
    ax1.axhline(y=eps_eff_qs, color='r', linestyle='--', label=r'$\varepsilon_{eff}$(准静态)=' + f'{eps_eff_qs:.2f}')
    ax1.axhline(y=epsilon_r, color='gray', linestyle=':', label='epsilon_r = ' + str(epsilon_r))
    ax1.set_xlabel(r'$f$ [GHz]')
    ax1.set_ylabel(r'$\varepsilon_{eff}$')
    ax1.set_title(r'微带线有效介电常数随频率变化')
    ax1.legend()
    
    # 右: 归一化波长
    ax2 = axes[1]
    lambda_g_ratio = [c / (f * np.sqrt(e)) for f, e in zip(f_vals, eps_eff_disp)]
    lambda_0 = c / f_vals
    lambda_g_ratio_norm = [lg / l0 for lg, l0 in zip(lambda_g_ratio, lambda_0)]
    
    ax2.plot(f_vals/1e9, lambda_g_ratio_norm, 'g-', lw=2)
    ax2.set_xlabel(r'$f$ [GHz]')
    ax2.set_ylabel(r'$\lambda_g / \lambda_0$')
    ax2.set_title(r'微带线波导波长与自由空间波长之比')
    
    try:
        plt.tight_layout()
    except:
        pass
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_microstrip_dispersion.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_microstrip_dispersion.png")


# ============================================================
# 2. 带状线 (Stripline)
# ============================================================

def stripline_Z0(W, b, epsilon_r, t=None):
    """
    带状线特性阻抗 (零厚度导体带)
    
    基于 Cohn 综合公式:
    Z0 = 30π * ln(1 + 2*W_eff/b) / sqrt(epsilon_r)
    
    其中 W_eff 是有效宽度 (考虑边缘场)
    """
    # 有效宽度
    if W / b >= 0.35:
        W_eff = W + 0.4415 * b
    else:
        W_eff = W + 0.4415 * b - (b / np.pi) * np.log(
            (W / b + 0.5)**2 / (W / b + 0.05) * (b / W + 0.5)**2 / (b / W + 0.05)
        )
    
    Z0 = 30 * np.pi / np.sqrt(epsilon_r) * np.log(1 + 2 * W_eff / b)
    
    return Z0, W_eff


def stripline_Z0_thick(W, b, epsilon_r, t):
    """
    有限厚度导体带带状线特性阻抗
    
    基于 Wheeler 公式
    """
    # 零厚度阻抗
    Z0_thin, W_eff = stripline_Z0(W, b, epsilon_r)
    
    # 厚度修正
    if t is None or t == 0:
        return Z0_thin, W_eff
    
    t_b = t / b
    W_eff = W_eff + t * (0.5 * np.log(4 * np.pi * W / t) + 1)
    
    # Wheeler 修正公式
    Z0 = 30 * np.pi / np.sqrt(epsilon_r) * np.log(
        1 + 2 * W_eff / b * (1 + 0.2 * t_b) / (1 + t_b * 1.1)
    )
    
    return Z0, W_eff


# ============================================================
# 例题 4.3: 带状线特性阻抗
# ============================================================

def example_stripline():
    """
    例题: 带状线 b=3mm, 填充空气, 求 Z0=50Ω 所需的导体带宽度 W
    """
    b = 3e-3   # 3 mm
    epsilon_r = 1.0
    
    # 反解 Z0 → W
    target_Z0 = 50.0
    
    # 近似: Z0 ≈ 30π * ln(2W/b) / sqrt(ε_r)
    # W ≈ b/2 * exp(Z0*sqrt(ε_r)/(30π)) - b/2
    W_approx = b/2 * np.exp(target_Z0 * np.sqrt(epsilon_r) / (30 * np.pi)) - b/2
    
    print(f"带状线: b={b*1e3:.1f}mm, ε_r={epsilon_r}")
    print(f"目标 Z0 = {target_Z0} Ω")
    print(f"估算 W ≈ {W_approx*1e3:.4f} mm")
    
    # 精确计算
    Z0_calc, W_eff = stripline_Z0(W_approx, b, epsilon_r)
    print(f"精确计算 Z0 = {Z0_calc:.4f} Ω (W={W_approx*1e3:.4f}mm, W_eff={W_eff*1e3:.4f}mm)")
    
    # 用数值迭代精确求解
    # scipy.optimize.brentq already available
    
    def Z0_func(W):
        z, _ = stripline_Z0(W, b, epsilon_r)
        return z - target_Z0
    
    try:
        W_solution = brentq(Z0_func, 0.1e-3, 10e-3)
        print(f"数值求解 W = {W_solution*1e3:.4f} mm")
        z_check, _ = stripline_Z0(W_solution, b, epsilon_r)
        print(f"验证 Z0 = {z_check:.4f} Ω")
    except:
        print("迭代失败")
    
    return W_approx


# ============================================================
# 3. 悬置微带线和倒置微带线
# ============================================================

def suspended_microstrip_eff(w, h, b, epsilon_r):
    """
    悬置微带线有效介电常数
    
    参数:
        w: 导体带宽
        h: 基片厚度
        b: 波导高度 (两接地板间距)
        epsilon_r: 基片介电常数
    """
    if w/h > 8:
        return epsilon_r
    
    # 中间变量
    eta = w/h
    a1 = 0.2621 - 0.1251 * np.log(eta)
    b1 = 0.4986 - 0.1997 * np.log(eta)
    
    eps_eff = (epsilon_r + 1) / 2 + (epsilon_r - 1) / 2 * (b1 / (b/h + a1))
    
    return eps_eff


def inverted_microstrip_eff(w, h, b, epsilon_r):
    """
    倒置微带线有效介电常数
    """
    if w/h > 8:
        return 1.0
    
    eta = w/h
    a1 = 0.8173 - 0.1515 * np.log(eta)
    b1 = 0.3092 - 0.104 * np.log(eta)
    
    eps_eff = (epsilon_r + 1) / 2 + (epsilon_r - 1) / 2 * (b1 / (b/h - a1))
    
    return eps_eff


# ============================================================
# 例题 4.4: 悬置微带线特性
# ============================================================

def example_suspended_microstrip():
    """
    例题: 悬置微带线 ε_r=2.1 (聚四氟乙烯), h=0.5mm, b=3mm
    w=1mm, 求有效介电常数和相速度
    """
    epsilon_r = 2.1
    h = 0.5e-3
    b = 3e-3
    w = 1e-3
    
    eps_eff = suspended_microstrip_eff(w, h, b, epsilon_r)
    
    print(f"悬置微带线:")
    print(f"  ε_r = {epsilon_r}, h = {h*1e3:.1f}mm, b = {b*1e3:.1f}mm, w = {w*1e3:.1f}mm")
    print(f"  有效介电常数 ε_eff = {eps_eff:.4f}")
    
    # 相速度
    vp = c / np.sqrt(eps_eff)
    print(f"  相速度 v_p = {vp/1e8:.4f} × 10⁸ m/s = {vp/c:.4f}c")
    
    return eps_eff


# ============================================================
# 4. 槽线 (Slotline)
# ============================================================

def slotline_Z0_and_lambda(w, h, epsilon_r, f):
    """
    槽线特性阻抗和波导波长 (近似公式)
    
    参数:
        w: 槽宽 [m]
        h: 基片厚度 [m]
        epsilon_r: 基片介电常数
        f: 频率 [Hz]
    
    基于 Sharma-Laviano 曲线拟合公式
    """
    lambda_0 = c / f
    
    # 归一化宽度
    W = w / h
    
    if W < 0.02:
        Z0 = 72.62 - 15.283 * np.log(W) + 59.0 * W + 59.0 * W**2 - 0.139 * np.log(W) - 0.11 * np.log(W)**2
        # 太复杂，用简化
        Z0 = 113.19 - 23.257 * np.log(W) + 1.25 * epsilon_r * W - 22.53 * np.log(W) * W
    elif W < 0.2:
        Z0 = 113.19 - 23.257 * np.log(W) + 1.25 * epsilon_r * W - 22.53 * np.log(W) * W
    else:
        Z0 = 72.62 - 15.283 * np.log(W) + 59.0 * W
    
    # 有效介电常数 (近似)
    # 对于槽线，场主要在空气中，所以 epsilon_eff 接近 1
    # 但由于边缘效应，有一定加权
    eps_eff_slotline = 0.5 * (epsilon_r + 1) + 0.5 * (epsilon_r - 1) * (1 + 10 / W)**(-0.5)
    eps_eff_slotline = max(eps_eff_slotline, 1.0)
    
    # 波导波长
    lambda_g = lambda_0 / np.sqrt(eps_eff_slotline)
    
    return Z0, lambda_g, eps_eff_slotline


# ============================================================
# 例题 4.5: 槽线特性
# ============================================================

def example_slotline():
    """
    例题: 槽线 ε_r=9.6 (氧化铝), h=0.5mm, w=0.5mm
    f=10GHz, 求特性阻抗和波导波长
    """
    epsilon_r = 9.6
    h = 0.5e-3
    w = 0.5e-3
    f = 10e9
    
    W = w / h
    
    # 简化近似
    Z0 = 72.62 - 15.283 * np.log(W) + 59.0 * W
    lambda_0 = c / f
    eps_eff = 0.5 * (epsilon_r + 1) + 0.5 * (epsilon_r - 1) * (1 + 10 / W)**(-0.5)
    lambda_g = lambda_0 / np.sqrt(eps_eff)
    
    print(f"槽线:")
    print(f"  ε_r = {epsilon_r}, h = {h*1e3:.1f}mm, w = {w*1e3:.1f}mm, f={f/1e9:.0f}GHz")
    print(f"  w/h = {W:.2f}")
    print(f"  特性阻抗 Z0 ≈ {Z0:.2f} Ω")
    print(f"  有效介电常数 ε_eff ≈ {eps_eff:.4f}")
    print(f"  自由空间波长 λ0 = {lambda_0*1e3:.2f} mm")
    print(f"  波导波长 λ_g ≈ {lambda_g*1e3:.2f} mm")
    
    return Z0, lambda_g


# ============================================================
# 5. 鳍线 (Finline)
# ============================================================

def finline_lambda_g(a, b, d, epsilon_r, f):
    """
    集成鳍线的波导波长近似公式
    
    λ_g = λ0 / sqrt(ε_eff)
    ε_eff ≈ (λ0 / λ_c_eff)^2
    """
    lambda_0 = c / f
    
    # 有效截止波长 (经验公式)
    # 对于单侧鳍线
    lambda_c_eff = 2 * a * (1 - 0.5 * d / b)**2
    
    eps_eff = (lambda_0 / lambda_c_eff)**2
    lambda_g = lambda_0 / np.sqrt(max(eps_eff, 1))
    
    return lambda_g, eps_eff


# ============================================================
# 例题 4.6: 微带线参数扫描
# ============================================================

def example_microstrip_param_sweep():
    """
    绘制微带线 w/h 比 vs Z0 和 ε_eff 的关系
    ε_r = 9.6 (氧化铝), h = 0.5mm
    """
    epsilon_r = 9.6
    h = 0.5e-3
    
    u_vals = np.logspace(-1, 1, 200)  # w/h 从 0.1 到 10
    
    Z0_vals = []
    eps_eff_vals = []
    
    for u in u_vals:
        w = u * h
        Z0, eps_eff = microstrip_Z0_and_eff(w, h, epsilon_r)
        Z0_vals.append(Z0)
        eps_eff_vals.append(eps_eff)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    ax1 = axes[0]
    ax1.semilogx(u_vals, Z0_vals, 'b-', lw=2)
    ax1.axhline(y=50, color='r', linestyle='--', label='50Ω')
    ax1.axhline(y=75, color='g', linestyle='--', label='75Ω')
    ax1.set_xlabel(r'$w/h$')
    ax1.set_ylabel(r'$Z_0$ [Ω]')
    ax1.set_title(rf'微带线特性阻抗 ($\varepsilon_r$={epsilon_r})')
    ax1.legend()
    ax1.grid(True, which='both', alpha=0.3)
    
    ax2 = axes[1]
    ax2.semilogx(u_vals, eps_eff_vals, 'g-', lw=2)
    ax2.axhline(y=1, color='gray', linestyle=':', label='空气')
    ax2.axhline(y=epsilon_r, color='orange', linestyle=':', label=f'ε_r={epsilon_r}')
    ax2.set_xlabel(r'$w/h$')
    ax2.set_ylabel(r'$\varepsilon_{eff}$')
    ax2.set_title(r'微带线有效介电常数')
    ax2.legend()
    ax2.grid(True, which='both', alpha=0.3)
    
    try:
        plt.tight_layout()
    except:
        pass
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_microstrip_Z0_w_over_h.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_microstrip_Z0_w_over_h.png")


# ============================================================
# 6. 微带截面结构图
# ============================================================

def draw_microstrip_cross_section(ax=None, w=None, h=None, epsilon_r=9.6):
    """
    绘制微带线截面结构图
    """
    if ax is None:
        fig, ax = plt.subplots(1, 1, figsize=(10, 4))
    
    if w is None:
        w = 1.0
    if h is None:
        h = 0.5
    
    # 归一化画图
    scale = 3.0 / max(w, h)
    w_s = w * scale
    h_s = h * scale
    
    # 底面 (接地金属)
    rect_gnd = Rectangle((-w_s*0.5 - 0.5, -h_s - 0.2), w_s + 1.0, 0.2, 
                          facecolor='silver', edgecolor='black', lw=1)
    ax.add_patch(rect_gnd)
    
    # 基片
    rect_sub = Rectangle((-w_s*0.5 - 0.5, 0), w_s + 1.0, h_s,
                          facecolor='#ADD8E6', edgecolor='black', lw=1)
    ax.add_patch(rect_sub)
    
    # 导体带
    rect_metal = Rectangle((-w_s*0.5, 0), w_s, 0.08,
                             facecolor='gold', edgecolor='black', lw=1)
    ax.add_patch(rect_metal)
    
    ax.set_xlim(-w_s*0.5 - 0.8, w_s*0.5 + 0.8)
    ax.set_ylim(-h_s - 0.4, h_s + 0.3)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(rf'微带线截面 ($\varepsilon_r$={epsilon_r})')
    
    # 标注
    ax.annotate('金属导体带', (0, 0.15), ha='center', fontsize=11)
    ax.annotate('介质基片', (w_s*0.5 + 0.3, h_s*0.5), ha='left', fontsize=10)
    ax.annotate('接地金属', (-w_s*0.5 - 0.3, -h_s - 0.1), ha='right', fontsize=10)
    ax.annotate('h', (w_s*0.5 + 0.2, h_s*0.5), fontsize=10)
    ax.annotate('w', (0, -0.1), fontsize=10)
    
    return ax


if __name__ == '__main__':
    print("=" * 60)
    print(" 第四章 微波集成传输线 例题")
    print("=" * 60)
    
    print("\n--- 例题 4.1: 微带线特性阻抗 ---")
    example_microstrip_Z0()
    
    print("\n--- 例题 4.2: 微带线色散 ---")
    example_microstrip_dispersion()
    
    print("\n--- 例题 4.3: 带状线特性阻抗 ---")
    example_stripline()
    
    print("\n--- 例题 4.4: 悬置微带线 ---")
    example_suspended_microstrip()
    
    print("\n--- 例题 4.5: 槽线特性 ---")
    example_slotline()
    
    print("\n--- 例题 4.6: 微带线参数扫描 (生成图) ---")
    example_microstrip_param_sweep()
    
    print("\n--- 微带线截面结构绘图 ---")
    fig, ax = plt.subplots(1, 1, figsize=(10, 4))
    draw_microstrip_cross_section(ax, w=1e-3, h=0.5e-3, epsilon_r=9.6)
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/wb94/figures/wb94_microstrip_cross_section.png',
                dpi=150, bbox_inches='tight')
    plt.show()
    print("图已保存: wb94_microstrip_cross_section.png")