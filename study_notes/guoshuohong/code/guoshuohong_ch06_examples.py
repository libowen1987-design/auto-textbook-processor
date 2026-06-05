#!/usr/bin/env python3
"""
郭硕鸿《电动力学》Ch6 — 狭义相对论：示例代码
============================================

Demos:
1. Lorentz 变换可视化 — 时空图 / 尺缩 / 钟慢
2. 电磁场张量变换 — 匀速运动点电荷的场
3. 相对论多普勒效应 + 光行差

依赖: numpy, matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
import os

# ─────────────────────────────────────────────
# 全局设置
# ─────────────────────────────────────────────
c = 299_792_458.0  # m/s
plt.rcParams.update({
    'figure.dpi': 150,
    'font.size': 10,
    'axes.grid': True,
    'grid.alpha': 0.3,
})

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# =====================================================================
# Demo 1: Lorentz 变换可视化
# =====================================================================
def demo_lorentz_transformation():
    """
    Lorentz 变换核心视觉：
      (a) 时空图（Minkowski 图）
          固定 S 系 (ct, x)，画出 S' 系的坐标轴
          某个事件的坐标在两个系中的不同读数
      (b) 尺缩效应 — 运动杆长度随 β 的变化
      (c) 钟慢效应 — 运动时钟周期随 β 的变化
    """
    print("=" * 60)
    print("Demo 1: Lorentz 变换可视化")
    print("=" * 60)

    # ── 图 (a) 时空图 ──
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    # ---- 图(a): Minkowski 时空图 ----
    ax = axes[0]
    beta = 0.6
    gamma = 1 / np.sqrt(1 - beta**2)

    # S 系坐标轴
    ax.axhline(0, color='gray', lw=0.5)
    ax.axvline(0, color='gray', lw=0.5)
    ax.annotate('x', xy=(1.02, 0), fontsize=11, color='C0')
    ax.annotate('ct', xy=(0, 1.02), fontsize=11, color='C0')

    # S' 系坐标轴（Rapidity: θ = arctanh(β)）
    theta = np.arctanh(beta)
    # ct' 轴：ct = x / β  → 斜率 1/β
    x_vals = np.linspace(0, 1.2, 100)
    ct_axis = x_vals / beta
    ax.plot(x_vals, ct_axis, '--', color='C1', lw=1.5, label="ct' axis")
    # x' 轴：ct = β x  → 斜率 β
    xp_axis = beta * x_vals
    ax.plot(x_vals, xp_axis, ':', color='C1', lw=1.5, label="x' axis")
    ax.annotate("x'", xy=(1.15, 1.15*beta), fontsize=11, color='C1')
    ax.annotate("ct'", xy=(1.15/beta, 1.15), fontsize=11, color='C1')

    # 一个事件 P: (ct, x) = (1.0, 0.8)
    ct_P, x_P = 1.0, 0.8
    ax.plot(x_P, ct_P, 'o', color='red', markersize=6, zorder=5)
    ax.annotate('P', xy=(x_P+0.03, ct_P+0.05), fontsize=11, color='red')

    # 投影到 S 轴
    ax.plot([0, x_P], [ct_P, ct_P], ':', color='gray', lw=0.8)
    ax.plot([x_P, x_P], [0, ct_P], ':', color='gray', lw=0.8)

    # 投影到 S' 轴（通过逆变换求坐标）
    ct_Pp = gamma * (ct_P - beta * x_P)
    x_Pp = gamma * (x_P - beta * ct_P)
    # 沿 S' 轴方向的投影
    # 平行于 x' 轴画线 → ct 方向斜率 beta
    # 平行于 ct' 轴画线 → ct 方向斜率 1/beta
    # 从 P 到 ct' 轴的平行于 x' 轴的线
    t_cline = np.linspace(-0.3, ct_P, 50)
    x_along_ctp = x_Pp + beta * t_cline  # x'(ct') + β·ct 在 S 坐标
    ax.plot(x_along_ctp, t_cline, ':', color='C1', lw=0.8, alpha=0.7)
    # 从 P 到 x' 轴的平行于 ct' 轴的线
    x_cline = np.linspace(-0.3, x_P, 50)
    ct_along_xp = ct_Pp + beta * x_cline
    ax.plot(x_cline, ct_along_xp, ':', color='C1', lw=0.8, alpha=0.7)

    # 光锥
    x_cone = np.linspace(0, 1.3, 100)
    ax.plot(x_cone, x_cone, 'k-', lw=0.8, alpha=0.3)
    ax.plot(x_cone, -x_cone, 'k-', lw=0.8, alpha=0.3)
    ax.annotate('light cone', xy=(1.2, 1.15), fontsize=8, alpha=0.5)

    ax.set_xlim(-0.2, 1.3)
    ax.set_ylim(-0.2, 1.3)
    ax.set_xlabel('x')
    ax.set_ylabel('ct')
    ax.set_title(f'(a) Minkowski 时空图  β={beta}')
    ax.set_aspect('equal')
    ax.legend(fontsize=8, loc='upper left')

    # ---- 图(b): 尺缩效应 ----
    ax = axes[1]
    betas = np.linspace(0, 0.99, 200)
    gammas = 1 / np.sqrt(1 - betas**2)
    lengths = 1.0 / gammas  # L = L0/γ, L0 = 1
    ax.plot(betas, lengths, 'b-', lw=2)
    ax.axhline(1.0, color='k', ls='--', alpha=0.3, label='L₀ (静止长度)')
    ax.fill_between(betas, 0, lengths, alpha=0.2)
    ax.set_xlabel('β = v/c')
    ax.set_ylabel('L / L₀')
    ax.set_title('(b) 长度收缩  L = L₀ / γ')
    ax.set_ylim(0, 1.05)
    ax.legend(fontsize=8)
    # 标注几个点
    for b in [0.5, 0.8, 0.95]:
        g = 1 / np.sqrt(1 - b**2)
        ax.plot(b, 1/g, 'ro', markersize=4)
        ax.annotate(f'β={b}\nL={1/g:.3f}L₀',
                     xy=(b, 1/g), xytext=(b+0.08, 1/g+0.05),
                     fontsize=7, arrowprops=dict(arrowstyle='->', lw=0.5))

    # ---- 图(c): 钟慢效应 ----
    ax = axes[2]
    times = gammas  # Δt = γ Δτ, Δτ = 1
    ax.plot(betas, times, 'r-', lw=2)
    ax.axhline(1.0, color='k', ls='--', alpha=0.3, label='Δτ (固有时间)')
    ax.fill_between(betas, 1, times, alpha=0.2, color='red')
    ax.set_xlabel('β = v/c')
    ax.set_ylabel('Δt / Δτ')
    ax.set_title('(c) 时间膨胀  Δt = γ Δτ')
    ax.set_ylim(0.5, 8)
    ax.legend(fontsize=8)
    for b in [0.5, 0.8, 0.95]:
        g = 1 / np.sqrt(1 - b**2)
        ax.plot(b, g, 'bo', markersize=4)
        ax.annotate(f'β={b}\nΔt={g:.2f}Δτ',
                     xy=(b, g), xytext=(b+0.08, g+0.3),
                     fontsize=7, arrowprops=dict(arrowstyle='->', lw=0.5))

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, 'demo1_lorentz.png')
    fig.savefig(path, dpi=150)
    print(f"  → 保存: {path}")
    plt.close(fig)


# =====================================================================
# Demo 2: 电磁场张量变换 — 运动点电荷的场
# =====================================================================
def demo_moving_charge_field():
    """
    匀速运动点电荷 q 在实验室系中的电磁场分布。

    物理：
      - 在电荷静止系 S0 中，只有 Coulomb 电场 E0（球对称）
      - 经 Lorentz 变换到实验室系 S（电荷以 v 沿 x 运动），
        得到电场被"压缩"（沿运动方向缩短）且出现磁场

    显示：
      (a) 电场 E 的等势线/幅度分布（静止 vs 运动）
      (b) 磁场 B 的幅度分布
      (c) 电场在 x 和 y 方向上的分量曲线
    """
    print("\n" + "=" * 60)
    print("Demo 2: 运动点电荷的电磁场")
    print("=" * 60)

    beta = 0.8          # v/c
    gamma = 1 / np.sqrt(1 - beta**2)
    q = 1.0             # 任意单位

    # 空间网格（在运动平面 z=0 上）
    nx, ny = 200, 200
    x_vals = np.linspace(-3, 3, nx)
    y_vals = np.linspace(-3, 3, ny)
    X, Y = np.meshgrid(x_vals, y_vals)

    # ── 静止系 S0 中的电场（Coulomb）──
    # 在 S0 中，电荷静止在原点
    R0 = np.sqrt(X**2 + Y**2)
    # 避免原点发散
    R0_safe = np.maximum(R0, 0.05)
    E0x = q * X / R0_safe**3
    E0y = q * Y / R0_safe**3

    # ── 变换到实验室系 S ──
    # Lorentz 变换 (x 方向): E_x' = E_x (平行分量不变)
    # E_y' = γ(E_y - v B_z), B=0 在 S0 中
    # 所以 S 系中的场:
    Ex = E0x  # 平行分量不变
    Ey = gamma * E0y  # 垂直分量放大 γ 倍

    # 磁场：B_z = γ(v/c²) E_y  (在 S0 中 B=0)
    Bz = gamma * (beta / c) * E0y

    # 电场幅值
    E_mag = np.sqrt(Ex**2 + Ey**2)
    B_mag = np.abs(Bz)

    # ── 绘图 ──
    fig, axes = plt.subplots(2, 3, figsize=(15, 9))

    # Strato 函数：等势图
    def _field_plot(ax, X, Y, Ex, Ey, title, cmap='viridis',
                    skip=8, stream=True):
        """场幅值云图 + 流线"""
        E = np.sqrt(Ex**2 + Ey**2)
        im = ax.pcolormesh(X, Y, E, shading='auto', cmap=cmap)
        if stream:
            ax.streamplot(X, Y, Ex, Ey, color='w', linewidth=0.6,
                          density=1.2, arrowsize=0.6)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title(title)
        ax.set_aspect('equal')
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)
        return im

    # (a1) 静止 Coulomb 场
    ax = axes[0, 0]
    im1 = _field_plot(ax, X, Y, E0x, E0y,
                      f'(a1) 静止电荷 E 场\n(Coulomb, 球对称)', 'viridis')
    plt.colorbar(im1, ax=ax, shrink=0.8)

    # (a2) 运动电荷 E 场
    ax = axes[0, 1]
    im2 = _field_plot(ax, X, Y, Ex, Ey,
                      f'(a2) 运动电荷 E 场\n(v = {beta}c, 纵向压缩)', 'plasma')
    plt.colorbar(im2, ax=ax, shrink=0.8)

    # (a3) E 场幅值沿 x 轴的切面
    ax = axes[0, 2]
    mid = ny // 2
    # 沿 x 轴 (y=0)
    line_E_static = np.sqrt(E0x[mid, :]**2 + E0y[mid, :]**2)
    line_E_moving = np.sqrt(Ex[mid, :]**2 + Ey[mid, :]**2)
    ax.plot(x_vals, line_E_static, 'b-', lw=1.5, label='静止')
    ax.plot(x_vals, line_E_moving, 'r-', lw=1.5, label=f'v={beta}c')
    ax.set_xlabel('x')
    ax.set_ylabel('|E|')
    ax.set_title('(a3) E 场沿 x 轴切面')
    ax.legend(fontsize=8)
    ax.set_yscale('log')
    ax.set_ylim(1e-2, 1e2)

    # (b1) 运动电荷 B 场（幅值云图）
    ax = axes[1, 0]
    # B 场没有"方向"流线（只有 z 分量），显示幅值
    im3 = ax.pcolormesh(X, Y, B_mag, shading='auto', cmap='Reds')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'(b1) 运动电荷 |B| 场\n(v={beta}c)')
    ax.set_aspect('equal')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    plt.colorbar(im3, ax=ax, shrink=0.8)
    # 等高线辅助
    levels = np.logspace(-1, 1, 9)
    ax.contour(X, Y, B_mag, levels=levels, colors='k', linewidths=0.4, alpha=0.4)

    # (b2) B 场 + 一些 E 场矢量叠加
    ax = axes[1, 1]
    ax.pcolormesh(X, Y, B_mag, shading='auto', cmap='Reds', alpha=0.5)
    # 缩放到原始范围的 1/3 显示
    scale = (nx // 3)
    skip = 10
    ax.quiver(X[::skip, ::skip], Y[::skip, ::skip],
              Ex[::skip, ::skip], Ey[::skip, ::skip],
              color='blue', alpha=0.6, scale=scale, width=0.004,
              label='E 方向')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f'(b2) B 场云图 + E 矢量')
    ax.set_aspect('equal')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)

    # (b3) E 在 y 方向的增强
    ax = axes[1, 2]
    Ey0_static = E0y[mid, :]
    Ey0_moving = Ey[mid, :]
    ax.plot(x_vals, Ey0_static, 'b-', lw=1.5, label='静止 E_y')
    ax.plot(x_vals, Ey0_moving, 'r-', lw=1.5,
            label=f'运动 E_y (×{gamma:.1f})')
    ax.set_xlabel('x')
    ax.set_ylabel('E_y')
    ax.set_title('(b3) E_y 沿 x 轴切面')
    ax.legend(fontsize=8)
    ax.axhline(0, color='gray', lw=0.5)

    plt.suptitle('Demo 2: 匀速运动点电荷（$\mathbf{v}=v\hat{x}$）的电磁场',
                 fontsize=13, y=1.02)
    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, 'demo2_moving_charge.png')
    fig.savefig(path, dpi=150, bbox_inches='tight')
    print(f"  → 保存: {path}")
    plt.close(fig)

    # ── 输出一些数值作参考 ──
    x_test = np.array([-2.0, -1.0, 0.5, 1.0, 2.0])
    y_test = np.array([1.5, 0.5, 1.0, 0.0, 2.0])
    print("\n  采样点场值 (beta=0.8, gamma={:.2f}):".format(gamma))
    print("  " + "-" * 60)
    print(f"  {'x':>6} {'y':>6} {'E_x':>10} {'E_y':>10} {'|E|':>10} {'B_z':>10}")
    print("  " + "-" * 60)
    for xi, yi in zip(x_test, y_test):
        ri = np.sqrt(xi**2 + yi**2)
        ri_s = max(ri, 0.05)
        E0xi = q * xi / ri_s**3
        E0yi = q * yi / ri_s**3
        ex = E0xi
        ey = gamma * E0yi
        bz = gamma * (beta / c) * E0yi
        em = np.sqrt(ex**2 + ey**2)
        print(f"  {xi:6.2f} {yi:6.2f} {ex:10.4f} {ey:10.4f} {em:10.4f} {bz:10.2e}")
    print()


# =====================================================================
# Demo 3: 相对论多普勒效应 + 光行差
# =====================================================================
def demo_doppler_aberration():
    """
    相对论多普勒效应与光行差。

    多普勒效应：
      光源以速度 v 相对于观测者运动，观测到的频率
        ω' = ω₀ · γ(1 - β cos θ)
      其中 θ 是光源运动方向与观测方向之间的夹角。

      纵向多普勒 (θ=0):
        ω' = ω₀ · √[(1-β)/(1+β)]  (光源远离)
        ω' = ω₀ · √[(1+β)/(1-β)]  (光源接近)
    
    光行差：
      星光的视方向因观测者运动而偏移
        tan θ' = sin θ / [γ(cos θ - β)]
    
    显示：
      (a) 多普勒频移 vs β (多个角度)
      (b) 光行差 — 入射角变换
      (c) 连续光谱的 Doppler 位移示意图
    """
    print("=" * 60)
    print("Demo 3: 相对论多普勒效应 + 光行差")
    print("=" * 60)

    betas = np.linspace(0, 0.95, 300)

    # ── 图(a): 多普勒频移 ──
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    ax = axes[0]
    for theta_deg, ls, color in [(0, '-', 'r'), (45, '--', 'orange'),
                                  (90, '-.', 'g'), (135, '--', 'b'),
                                  (180, '-', 'purple')]:
        theta = np.deg2rad(theta_deg)
        gamma_arr = 1 / np.sqrt(1 - betas**2)
        freq_ratio = gamma_arr * (1 - betas * np.cos(theta))
        ax.plot(betas, freq_ratio, ls=ls, color=color, lw=1.5,
                label=f'θ={theta_deg}°')

    ax.axhline(1.0, color='k', ls=':', alpha=0.3)
    ax.set_xlabel('β = v/c')
    ax.set_ylabel("ω' / ω₀")
    ax.set_title('(a) 相对论多普勒效应')
    ax.legend(fontsize=7, loc='upper right')
    ax.set_ylim(0, 4)

    # ── 图(b): 横向多普勒（θ = 90° 的奇异性）──
    ax = axes[1]
    ax.plot(betas, 1/np.sqrt(1 - betas**2), 'g-', lw=2, label='横向 (θ=90°)')
    ax.plot(betas, np.sqrt((1 - betas)/(1 + betas)), 'b--', lw=1.5,
            label='远离 (θ=0°)')
    ax.plot(betas, np.sqrt((1 + betas)/(1 - betas)), 'r--', lw=1.5,
            label='接近 (θ=180°)')
    ax.set_xlabel('β = v/c')
    ax.set_ylabel("ω' / ω₀")
    ax.set_title('(b) 纵向 vs 横向多普勒')
    ax.legend(fontsize=8)
    ax.set_yscale('log')
    ax.set_ylim(1e-1, 1e1)
    ax.axhline(1.0, color='k', ls=':', alpha=0.3)

    # ── 图(c): 光行差 ──
    ax = axes[2]
    # 固定 β = 0.8, γ = 1.6667
    beta_val = 0.8
    gamma_val = 1 / np.sqrt(1 - beta_val**2)

    theta_source = np.linspace(0, np.pi, 200)  # 光源系中的角度
    # 光行差公式 (观测者在 S 系中向 x 正方向运动)
    # tan θ' = sin θ / [γ(cos θ - β)]
    # 要小心分母为零的情况
    denom = gamma_val * (np.cos(theta_source) - beta_val)
    tan_theta_obs = np.sin(theta_source) / denom
    # 注意象限
    theta_obs = np.arctan2(np.sin(theta_source), denom)
    theta_obs = np.where(theta_obs < 0, theta_obs + 2*np.pi, theta_obs)

    ax.plot(np.rad2deg(theta_source), np.rad2deg(theta_obs), 'b-', lw=2)
    ax.plot(np.rad2deg(theta_source), np.rad2deg(theta_source),
            'k--', lw=1, alpha=0.4, label='无光行差')
    ax.set_xlabel('θ_src (光源系) [度]')
    ax.set_ylabel("θ'_obs (观测系) [度]")
    ax.set_title(f'(c) 光行差  β={beta_val}')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 180)
    ax.set_ylim(0, 180)
    # 标记特殊区域
    ax.axhline(0, color='gray', lw=0.5)
    ax.axvline(0, color='gray', lw=0.5)
    ax.annotate('向前聚焦', xy=(30, 10), fontsize=8,
                arrowprops=dict(arrowstyle='->', color='green'))
    ax.annotate('向后分散', xy=(150, 170), fontsize=8,
                arrowprops=dict(arrowstyle='->', color='green'))

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, 'demo3_doppler_aberration.png')
    fig.savefig(path, dpi=150)
    print(f"  → 保存: {path}")
    plt.close(fig)

    # ── 额外：多普勒效应与光谱位移可视化 ──
    fig, ax = plt.subplots(1, 1, figsize=(10, 4))

    # 模拟观察者向光源运动 (β=0.4) 时谱线的紫移
    beta_view = 0.4
    gamma_view = 1 / np.sqrt(1 - beta_view**2)
    # 假设静止系中的谱线 (归一化坐标)
    lambda0 = np.array([4861.3, 5893.0, 6562.8])  # Hβ, Na D, Hα in Å
    # 光源运动方向相对于观测者的角度
    angles = [0, 60, 90, 120, 180]  # 度
    angles_rad = np.deg2rad(angles)

    colors_angle = plt.cm.RdYlBu_r(np.linspace(0, 1, 5))
    y_offset = 0

    for i, (a_deg, a_rad) in enumerate(zip(angles, angles_rad)):
        doppler_factor = gamma_view * (1 - beta_view * np.cos(a_rad))
        lambda_shift = lambda0 / doppler_factor  # 波长 = c/ν，所以 λ' = λ₀/因子
        y_offset = i * 0.8

        for j, (l0, ls) in enumerate(zip(lambda0, lambda_shift)):
            # 画线
            ax.plot([ls, ls], [y_offset - 0.2, y_offset + 0.2],
                    color=colors_angle[i], lw=2)
            # 标记起始位置（小点）
            ax.plot(l0, y_offset + 0.2, 'o', color='gray', markersize=2)

        direction = "远离" if a_deg <= 90 else "接近" if a_deg >= 180 else "侧向"
        ax.text(4000, y_offset,
                f"θ={a_deg}° ({'远离' if a_deg < 90 else '接近' if a_deg > 90 else '横向'})",
                fontsize=8, va='center')

    # 参考线（静止波长）
    for l0 in lambda0:
        ax.axvline(l0, color='gray', ls=':', alpha=0.4)

    ax.set_xlabel('波长 [Å]')
    ax.set_ylabel('观测者视角')
    ax.set_title(f'相对论多普勒效应 — 谱线位移 (β={beta_view}, 观测者运动)')
    ax.set_xlim(3000, 7500)
    ax.set_yticks([])
    ax.annotate('紫移 ←', xy=(4700, -0.8), fontsize=9, color='blue')
    ax.annotate('→ 红移', xy=(6200, -0.8), fontsize=9, color='red')
    # 标注静止波长
    for l0 in lambda0:
        label = {4861.3: 'Hβ', 5893.0: 'Na D', 6562.8: 'Hα'}
        ax.annotate(f'{label[l0]} ({l0:.0f}Å)',
                    xy=(l0, -0.3), fontsize=7, ha='center', alpha=0.6)
    plt.tight_layout()
    path2 = os.path.join(OUTPUT_DIR, 'demo3_spectral_shift.png')
    fig.savefig(path2, dpi=150)
    print(f"  → 保存: {path2}")
    plt.close(fig)

    # ── 打印一些数值结果 ──
    print("\n  相对论多普勒效应数值示例 (β=0.8):")
    beta_d = 0.8
    gamma_d = 1 / np.sqrt(1 - beta_d**2)
    print(f"  γ = {gamma_d:.4f}")
    print(f"  {'角度 θ':>10} {'ω/ω₀':>10}")
    print("  " + "-" * 22)
    for th in [0, 45, 90, 135, 180]:
        th_r = np.deg2rad(th)
        ratio = gamma_d * (1 - beta_d * np.cos(th_r))
        print(f"  {th:>7}°  {ratio:10.4f}")
    print()


# ─────────────────────────────────────────────
# 主入口
# ─────────────────────────────────────────────
if __name__ == '__main__':
    print("=" * 60)
    print("郭硕鸿《电动力学》Ch6 — 狭义相对论 示例代码")
    print("=" * 60)

    demo_lorentz_transformation()
    demo_moving_charge_field()
    demo_doppler_aberration()

    print("所有 Demo 完成。")
    print(f"图片保存至: {OUTPUT_DIR}/")
    print(f"  ├─ demo1_lorentz.png")
    print(f"  ├─ demo2_moving_charge.png")
    print(f"  ├─ demo3_doppler_aberration.png")
    print(f"  └─ demo3_spectral_shift.png")
