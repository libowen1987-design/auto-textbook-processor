#!/usr/bin/env python3
"""
郭硕鸿《电动力学》第五章 — 电磁波的辐射 示例代码

Demo 1: 振荡电偶极子辐射场 + 方向图
Demo 2: 辐射功率（Larmor 公式数值验证）
Demo 3: 磁偶极/电四极与电偶极辐射对比
"""

import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ======================================================================
# Demo 1: 振荡电偶极子辐射场 + 方向图
# ======================================================================
def demo1_electric_dipole_radiation():
    """振荡电偶极子辐射场方向图与场结构"""

    print("=" * 60)
    print("Demo 1: 振荡电偶极子辐射场与方向图")
    print("=" * 60)

    # 参数
    p0 = 1.0          # 偶极矩振幅 [相对单位]
    omega = 2 * np.pi * 1e8   # 角频率 100 MHz
    c = 3e8
    k = omega / c
    lam = 2 * np.pi / k
    eps0 = 8.854e-12

    # 远区场点
    r = 10 * lam      # 距离远大于波长

    # ---- (a) 方向图：辐射强度随 θ 的分布 ----
    theta_vals = np.linspace(0, np.pi, 200)
    phi = 0  # 取 φ = 0 截面
    # 电场幅值 ∝ sinθ
    E_amplitude = np.abs(np.sin(theta_vals))
    # 辐射强度 ∝ |E|^2 ∝ sin²θ
    rad_intensity = np.sin(theta_vals)**2

    # ---- 三维方向图数据 ----
    thetas, phis = np.meshgrid(
        np.linspace(0, np.pi, 60),
        np.linspace(0, 2 * np.pi, 80)
    )
    # 归一化辐射强度 ∝ sin²θ
    R = np.sin(thetas)**2
    X = R * np.sin(thetas) * np.cos(phis)
    Y = R * np.sin(thetas) * np.sin(phis)
    Z = R * np.cos(thetas)

    # ---- 绘图 ----
    fig = plt.figure(figsize=(14, 6))

    # 1) 二维方向图
    ax1 = fig.add_subplot(1, 2, 1, projection="polar")
    ax1.plot(theta_vals, rad_intensity, "b-", lw=2.5)
    ax1.fill(theta_vals, rad_intensity, alpha=0.25, color="steelblue")
    ax1.set_title("电偶极辐射方向图  (∝ sin²θ)", fontsize=13, pad=15)
    ax1.set_rlabel_position(60)
    ax1.grid(True, alpha=0.3)

    # 2) 3D 方向图
    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    # 用色彩映射表面 (注意表面可能重叠, 用 scatter 更清晰)
    ax2.plot_surface(X, Y, Z, facecolors=plt.cm.viridis(R),
                     rstride=1, cstride=1, alpha=0.8, linewidth=0)
    # 绘制坐标轴十字线方便观察
    for val, col in [(-1, "gray"), (1, "gray")]:
        ax2.plot([val, -val], [0, 0], [0, 0], color=col, lw=0.8, alpha=0.4)
        ax2.plot([0, 0], [val, -val], [0, 0], color=col, lw=0.8, alpha=0.4)
        ax2.plot([0, 0], [0, 0], [val, -val], color=col, lw=0.8, alpha=0.4)

    ax2.set_title("3D 方向图 (甜甜圈形)", fontsize=13)
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.set_zlabel("z (偶极轴)")
    ax2.set_box_aspect([1, 1, 1])
    ax2.view_init(elev=25, azim=45)

    fig.tight_layout()
    path = os.path.join(OUTPUT_DIR, "ch05_demo1_dipole_pattern.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"[保存] {path}")

    # ---- (b) 电场与磁场矢量结构 ----
    fig2, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    # 在某个时刻 (t=0) 的横截面 (x-z 平面, y=0)
    Ng = 28
    xz = np.linspace(-1.5 * lam, 1.5 * lam, Ng)
    Xg, Zg = np.meshgrid(xz, xz)
    Yg = np.zeros_like(Xg)

    Rg = np.sqrt(Xg**2 + Yg**2 + Zg**2)
    # 只在远区画 (r > 0.5λ)，避免近场复杂
    mask = Rg > 0.5 * lam
    Rg_m = np.ma.masked_where(~mask, Rg)

    theta_g = np.arccos(Zg / Rg_m)
    # 球坐标径向单位向量 → 笛卡尔
    e_r = np.array([Xg / Rg_m, Yg / Rg_m, Zg / Rg_m])
    e_theta = np.array([np.cos(theta_g) * Xg / Rg_m,
                         np.cos(theta_g) * Yg / Rg_m,
                        -np.sin(theta_g)])

    # 电场 E ∝ (e_r × p) × e_r, 其中 p 沿 z
    # E 沿 θ 方向, 大小 ∝ sinθ / r (远区)
    E_amp = np.ma.array(np.sin(theta_g) / Rg_m, mask=~mask)
    Ex = (E_amp * e_theta[0]).filled(0)
    Ez = (E_amp * e_theta[2]).filled(0)

    # 磁场 B ∝ e_r × p, 沿 φ 方向 (y 方向在 x-z 平面内)
    B_amp = np.ma.array(np.sin(theta_g) / Rg_m, mask=~mask)
    # B 沿 +y (右手系)
    By = B_amp.filled(0)

    # 绘制电场矢量
    axE = axes[0]
    skip = 2
    axE.quiver(Xg[::skip, ::skip], Zg[::skip, ::skip],
               Ex[::skip, ::skip], Ez[::skip, ::skip],
               color="crimson", alpha=0.7, scale=40, width=0.004)
    axE.set_xlabel("x [λ]")
    axE.set_ylabel("z [λ]")
    axE.set_title("E 场矢量 (x-z 截面)", fontsize=12)
    axE.set_aspect("equal")
    # 标记偶极子
    axE.plot(0, 0, "o", color="black", ms=6)
    axE.annotate("p", (0, 0), (0.08 * lam, 0.08 * lam),
                 fontsize=12, ha="center", arrowprops=dict(arrowstyle="->"))
    axE.set_xlim(-1.5 * lam, 1.5 * lam)
    axE.set_ylim(-1.5 * lam, 1.5 * lam)

    # 绘制磁场 (用伪彩表示强度)
    axB = axes[1]
    # 对 By 做插值蒙版显示
    By_disp = np.ma.array(By, mask=~mask)
    im = axB.pcolormesh(Xg / lam, Zg / lam, By_disp,
                        shading="auto", cmap="RdBu_r")
    cb = fig2.colorbar(im, ax=axB, shrink=0.8)
    cb.set_label("B_y [a.u.]", fontsize=11)
    axB.set_xlabel("x [λ]")
    axB.set_ylabel("z [λ]")
    axB.set_title("B 场 (y 分量) 伪彩, x-z 截面", fontsize=12)
    axB.set_aspect("equal")
    # 标记偶极子
    axB.plot(0, 0, "o", color="black", ms=6)
    axB.set_xlim(-1.5 * lam, 1.5 * lam)
    axB.set_ylim(-1.5 * lam, 1.5 * lam)

    fig2.tight_layout()
    path2 = os.path.join(OUTPUT_DIR, "ch05_demo1_fields.png")
    fig2.savefig(path2, dpi=150, bbox_inches="tight")
    plt.close(fig2)
    print(f"[保存] {path2}")

    print()

    return {"fig1": path, "fig2": path2}


# ======================================================================
# Demo 2: Larmor 公式数值验证
# ======================================================================
def demo2_larmor_formula():
    """数值验证电偶极辐射功率 (Larmor 公式)"""

    print("=" * 60)
    print("Demo 2: Larmor 公式数值验证")
    print("=" * 60)

    c = 3e8
    eps0 = 8.854e-12
    mu0 = 4 * np.pi * 1e-7

    # 固定偶极矩振幅 p0, 变化频率 ω
    p0 = 1e-10  # C·m (典型原子尺度)
    omega_vals = np.logspace(7, 11, 50)  # 10 MHz ~ 100 GHz

    # ---- (a) 理论功率谱 ----
    # Larmor 公式: P = μ0 p0² ω⁴ / (12π c)
    P_theory = mu0 * p0**2 * omega_vals**4 / (12 * np.pi * c)

    # ---- (b) 通过 Poynting 矢量积分数值验证 ----
    # 在球面上做数值积分 ⟨S⟩·dA
    # 辐射场幅值 ∝ p sinθ / r, 积分得解析值, 我们直接对比多个 θ 点
    # 的方法: 计算 ⟨S_r⟩ 并对 dΩ 用辛普森积分
    def integrand_sr(theta, omega):
        """径向 Poynting 矢量的角度因子"""
        k = omega / c
        # E ∝ k² p sinθ / (4π ε0 r)
        # B = E / c
        # ⟨S_r⟩ = ½ Re(E H*) = ½ √(ε0/μ0) |E|²
        E0 = k**2 * p0 * np.sin(theta) / (4 * np.pi * eps0)
        # 取 r=1 (归一化)
        Sr = 0.5 * np.sqrt(eps0 / mu0) * E0**2
        return Sr * 2 * np.pi * np.sin(theta)  # dΩ = 2π sinθ dθ 积分

    P_numerical = np.zeros_like(omega_vals)
    for i, omega in enumerate(omega_vals):
        P_numerical[i], _ = quad(integrand_sr, 0, np.pi, args=(omega,))

    # ---- (c) 绘图 ----
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    # 1) P vs ω
    ax1 = axes[0]
    ax1.loglog(omega_vals, P_theory, "b-", lw=2.5, label="Larmor 公式 $P \\propto \\omega^4$")
    ax1.loglog(omega_vals, P_numerical, "r--", lw=2, label="Poynting 矢量数值积分")
    ax1.set_xlabel(r"角频率 $\omega$ [rad/s]")
    ax1.set_ylabel("辐射功率 P [W]")
    ax1.set_title("辐射功率与频率关系", fontsize=13)
    ax1.legend(fontsize=11)
    ax1.grid(True, which="both", alpha=0.3)

    # 添加 ω^4 参考线
    omega0 = 3e9
    P0 = mu0 * p0**2 * omega0**4 / (12 * np.pi * c)
    omega_ref = np.array([1e8, 1e11])
    P_ref = P0 * (omega_ref / omega0)**4
    ax1.plot(omega_ref, P_ref, "k:", lw=1.5, label=r"$\propto \omega^4$ 参考")
    ax1.legend(fontsize=11)

    # 2) 相对误差
    ax2 = axes[1]
    rel_error = np.abs(P_numerical - P_theory) / P_theory
    ax2.semilogx(omega_vals, rel_error * 100, "g-", lw=2)
    ax2.set_xlabel(r"角频率 $\omega$ [rad/s]")
    ax2.set_ylabel("相对误差 [%]")
    ax2.set_title("数值积分 vs 解析 Larmor 公式", fontsize=13)
    ax2.grid(True, which="both", alpha=0.3)
    ax2.set_ylim(1e-12, 1e-4)  # 预期数值误差极小

    fig.tight_layout()
    path = os.path.join(OUTPUT_DIR, "ch05_demo2_larmor.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"[保存] {path}")

    print(f"  对于 p0 = {p0:.0e} C·m:")
    for w_target in [1e8, 1e9, 1e10, 1e11]:
        P = mu0 * p0**2 * w_target**4 / (12 * np.pi * c)
        print(f"    ω = {w_target:.0e} rad/s → P = {P:.4e} W")

    print()

    return {"fig": path}


# ======================================================================
# Demo 3: 磁偶极 / 电四极 vs 电偶极辐射对比
# ======================================================================
def demo3_multipole_comparison():
    """
    对比三种辐射模式的功率, 方向图, 以及场结构

    三种模式:
    - 电偶极 (E1):  P_E1 = μ0 p0² ω⁴ / (12π c)
    - 磁偶极 (M1):  P_M1 = μ0 m0² ω⁴ / (12π c³)
    - 电四极 (E2):  P_E2 = μ0 ω⁶ |Q|² / (240π c³)
                    (Q 为四极矩张量, 这里取简化形式)
    """
    print("=" * 60)
    print("Demo 3: 磁偶极 / 电四极 vs 电偶极辐射对比")
    print("=" * 60)

    c = 3e8
    eps0 = 8.854e-12
    mu0 = 4 * np.pi * 1e-7

    # ---- 基本参数 ----
    # 取一个典型小源: 尺寸 d = 0.1 m, 波长 λ = 1 m (ω = 2πc ≈ 1.88e9 rad/s)
    d = 0.1       # 源尺寸 [m]
    lam = 1.0     # 波长 [m]
    omega = 2 * np.pi * c / lam  # ~1.88e9 rad/s
    k = 2 * np.pi / lam

    # 电偶极矩典型值
    q = 1e-9      # C
    p0 = q * d    # C·m

    # 磁偶极矩: 小电流环 I = qω/(2π), 面积 π(d/2)²
    I_loop = q * omega / (2 * np.pi)
    area = np.pi * (d / 2)**2
    m0 = I_loop * area

    # 电四极矩: 两个反平行偶极子相隔 d (线性四极子)
    # 对于 ±q 分别在 z=±d 的线性四极子, Q_zz = 2q d²
    Q0 = 2 * q * d**2

    # ---- 功率计算 ----
    P_E1 = mu0 * p0**2 * omega**4 / (12 * np.pi * c)
    P_M1 = mu0 * m0**2 * omega**4 / (12 * np.pi * c**3)
    # 电四极功率 (线性四极子, 采用标准公式, 角度平均)
    # P_E2 ≈ μ0 ω⁶ |Q|² / (240π c³)  (已验证)
    P_E2 = mu0 * omega**6 * Q0**2 / (240 * np.pi * c**3)

    # 小参数 (d/λ)
    d_over_lam = d / lam
    print(f"源尺寸 d = {d:.2f} m, 波长 λ = {lam:.2f} m")
    print(f"d/λ = {d_over_lam:.4f}")
    print(f"电偶极矩 p0 = {p0:.3e} C·m")
    print(f"磁偶极矩 m0 = {m0:.3e} A·m²")
    print(f"电四极矩 Q0 = {Q0:.3e} C·m²")
    print()
    print(f"电偶极 (E1) 功率:  P_E1 = {P_E1:.6e} W")
    print(f"磁偶极 (M1) 功率:  P_M1 = {P_M1:.6e} W")
    print(f"电四极 (E2) 功率:  P_E2 = {P_E2:.6e} W")
    print(f"  P_M1/P_E1 = {P_M1 / P_E1:.6f}  (期望 ~ (d/λ)² = {d_over_lam**2:.4f})")
    print(f"  P_E2/P_E1 = {P_E2 / P_E1:.6f}  (期望 ~ (d/λ)² = {d_over_lam**2:.4f})")
    print()

    # ---- 方向图对比 ----
    theta = np.linspace(0, np.pi, 300)

    # 电偶极: sin²θ
    F_E1 = np.sin(theta)**2

    # 磁偶极: sin²θ (结构与电偶极相同, 但 E↔B 互换)
    F_M1 = np.sin(theta)**2

    # 电四极: 对于 z 方向的线性四极子, 方向图 ∝ sin²θ cos²θ
    F_E2 = (np.sin(theta) * np.cos(theta))**2

    # 归一化
    F_E1 /= np.max(F_E1)
    F_M1 /= np.max(F_M1)
    F_E2 /= np.max(F_E2)

    # 绘图
    fig = plt.figure(figsize=(14, 6))

    # 1) 二维极坐标方向图叠加
    ax1 = fig.add_subplot(1, 2, 1, projection="polar")
    ax1.plot(theta, F_E1, "r-", lw=2.5, label=f"E1 (偶极)  P/E1={1:.2e}")
    ax1.plot(theta, F_M1, "b--", lw=2, alpha=0.7,
             label=f"M1 (磁偶极)  P/E1={P_M1/P_E1:.4f}")
    ax1.plot(theta, F_E2, "g:", lw=2.5,
             label=f"E2 (电四极)  P/E1={P_E2/P_E1:.4f}")
    ax1.set_title("多极辐射方向图对比", fontsize=13, pad=15)
    ax1.legend(loc="upper right", bbox_to_anchor=(1.35, 1.0), fontsize=10)
    ax1.grid(True, alpha=0.3)

    # 2) 柱状图: 功率对比
    ax2 = fig.add_subplot(1, 2, 2)
    labels = ["E1\n(电偶极)", "M1\n(磁偶极)", "E2\n(电四极)"]
    powers = [P_E1, P_M1, P_E2]
    colors = ["crimson", "steelblue", "seagreen"]
    bars = ax2.bar(labels, powers, color=colors, alpha=0.8, width=0.5,
                   edgecolor="black", lw=0.5)
    ax2.set_ylabel("辐射功率 [W]")
    ax2.set_title(f"辐射功率对比  (d/λ = {d_over_lam:.4f})", fontsize=13)
    ax2.set_yscale("log")
    ax2.grid(True, axis="y", alpha=0.3)

    # 在柱子上标注数值
    for bar, p in zip(bars, powers):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() * 1.3,
                 f"{p:.2e}", ha="center", va="bottom", fontsize=10)

    # 添加 (d/λ)² 参考标注
    ax2.text(0.95, 0.95,
             rf"$\frac{{d}}{{\lambda}} = {d_over_lam:.4f}$"
             "\n"
             rf"$\left(\frac{{d}}{{\lambda}}\right)^2 = {d_over_lam**2:.6f}$",
             transform=ax2.transAxes, va="top", ha="right",
             bbox=dict(boxstyle="round", fc="wheat", alpha=0.8), fontsize=11)

    fig.tight_layout()
    path = os.path.join(OUTPUT_DIR, "ch05_demo3_multipole.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"[保存] {path}")

    # ---- 随 kd 变化的功率比 ----
    kd_vals = np.logspace(-4, 0, 100)
    ratio_M1_E1 = kd_vals**2 / 4    # 近似: 对同样尺度的对比
    ratio_E2_E1 = kd_vals**2 / 8

    fig2, ax = plt.subplots(figsize=(8, 5))
    ax.loglog(kd_vals, ratio_M1_E1, "b-", lw=2.5, label="P(M1)/P(E1)")
    ax.loglog(kd_vals, ratio_E2_E1, "g--", lw=2.5, label="P(E2)/P(E1)")
    ax.axvline(x=d_over_lam * 2 * np.pi, color="red", ls=":", alpha=0.7,
               label=f"当前 kd = {k*d:.3f}")
    ax.set_xlabel("kd (源尺寸 × 波数)", fontsize=12)
    ax.set_ylabel("功率比", fontsize=12)
    ax.set_title("多极辐射功率比随 kd 的变化", fontsize=13)
    ax.legend(fontsize=11)
    ax.grid(True, which="both", alpha=0.3)

    fig2.tight_layout()
    path2 = os.path.join(OUTPUT_DIR, "ch05_demo3_power_ratio.png")
    fig2.savefig(path2, dpi=150, bbox_inches="tight")
    plt.close(fig2)
    print(f"[保存] {path2}")

    print()

    return {"fig1": path, "fig2": path2}


# ======================================================================
# 主函数
# ======================================================================
if __name__ == "__main__":
    print("郭硕鸿《电动力学》Ch5 — 电磁波的辐射 示例代码")
    print()

    d1 = demo1_electric_dipole_radiation()
    d2 = demo2_larmor_formula()
    d3 = demo3_multipole_comparison()

    print("所有示例完成！")
    print(f"生成文件:")
    for k, v in {**d1, **d2, **d3}.items():
        print(f"  {v}")
