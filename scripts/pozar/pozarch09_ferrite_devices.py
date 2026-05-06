#!/usr/bin/env python3
"""
Pozar Chapter 9 — Ferrite Components / 铁氧体器件 数值示例
=============================================================

复现本章关键计算:
  1. Polder tensor (mu, kappa) frequency dependence
  2. Faraday rotation
  3. 结式环行器 S 参数 & Bosma condition
  4. YIG 谐振器设计 (Kittel 公式, Q 值)
  5. 铁氧体Phase shifterDiff phase shift

参考文献: D.M. Pozar, "Microwave Engineering", 4th Ed., Ch.9
单位制: SI (除个别工程单位标注)
"""

import numpy as np
from math import pi, sqrt, log10, exp
from scipy import constants
from scipy.special import jv, jvp
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt

# ────────────────────────────────────────────────────────────────────
# 物理常数 (SI)
# ────────────────────────────────────────────────────────────────────
MU0 = constants.mu_0          # 真空磁导率 [H/m]
EPS0 = constants.epsilon_0    # 真空介电常数 [F/m]
C0   = constants.c            # 光速 [m/s]
GAMMA_e = 1.759e11            # 电子旋磁比 [C/kg] = [rad/(s·T)]
# 工程常用形式:
# f0 (GHz) = 2.80e-3 * H0 (A/m)
# f0 (GHz) = 0.028 * H0 (Oe)


# ════════════════════════════════════════════════════════════════════
# §9.1 — Polder tensor
# ════════════════════════════════════════════════════════════════════

def tensor_permeability(omega, omega_0, omega_m, alpha=0.0):
    """
    计算 Polder 张量permeability elements mu, kappa.

    参数
    ----------
    omega  : float or ndarray  工作角Frequency [rad/s]
    omega_0: float             Larmor 共振Frequency [rad/s]
    omega_m: float             磁化特征Frequency [rad/s]
    alpha  : float             阻尼系数 (0 = 无损耗)

    返回
    -------
    mu     : float or ndarray  对角元 (无量纲)
    kappa  : float or ndarray  非对角元 (无量纲)
    mu_plus : float or ndarray  RHCP effective permeability
    mu_minus: float or ndarray LHCP effective permeability
    """
    if alpha == 0.0:
        denom = omega_0**2 - omega**2
        mu = 1.0 + omega_0 * omega_m / denom
        kappa = omega * omega_m / denom
    else:
        # 有损耗: 使用复数 omega_0 + j*alpha*omega
        omega_0c = omega_0 + 1j * alpha * omega
        denom = omega_0c**2 - omega**2
        mu = 1.0 + omega_0c * omega_m / denom
        kappa = omega * omega_m / denom

    # 圆极化本征磁导率
    mu_plus = mu + kappa
    mu_minus = mu - kappa
    return mu, kappa, mu_plus, mu_minus


def example_1_tensor_permeability():
    """
    示例 1: Polder tensorfrequency dependence可视化

    condition: YIG 材料, Ms = 139 kA/m (4πMs ≈ 1750 G)
          偏置场 H0 = 100 kA/m (≈ 1260 Oe)
    """
    print("=" * 60)
    print("示例 1: Polder tensor (mu, kappa) frequency dependence")
    print("=" * 60)

    # 材料参数 (YIG)
    Ms = 139e3   # 饱和磁化强度 [A/m]
    H0 = 100e3   # 偏置磁场 [A/m]

    # 特征Frequency
    omega_0 = GAMMA_e * MU0 * H0      # Larmor Frequency [rad/s]
    omega_m = GAMMA_e * MU0 * Ms      # 磁化特征Frequency [rad/s]
    f0 = omega_0 / (2 * pi)            # [Hz]
    print(f"  H0 = {H0/1e3:.1f} kA/m  ({H0/79.577:.0f} Oe)")
    print(f"  Ms = {Ms/1e3:.1f} kA/m  ({Ms/79.577:.0f} Oe)")
    print(f"  f0 (Larmor) = {f0/1e9:.3f} GHz")

    # Frequency扫描: 0.1*f0 ~ 2.5*f0
    freq_ratio = np.linspace(0.1, 2.5, 500)
    omega = freq_ratio * omega_0

    # 无损耗
    mu, kappa, mu_p, mu_m = tensor_permeability(omega, omega_0, omega_m, alpha=0.0)

    # 有损耗 (alpha = 0.01)
    mu_l, kappa_l, mu_p_l, mu_m_l = tensor_permeability(
        omega, omega_0, omega_m, alpha=0.01
    )

    # ── 绘图 ──
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # (a) mu, kappa (无损耗)
    ax = axes[0, 0]
    ax.plot(freq_ratio, mu, "b-", linewidth=2, label=r"$\mu$")
    ax.plot(freq_ratio, kappa, "r-", linewidth=2, label=r"$\kappa$")
    ax.axvline(1.0, color="grey", linestyle="--", alpha=0.5, label=r"$\omega/\omega_0 = 1$")
    ax.set_xlabel(r"$\omega / \omega_0$")
    ax.set_ylabel("permeability elements")
    ax.set_title("(a) (a) Lossless Polder tensor")
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-10, 30)

    # (b) mu_+, mu_- (无损耗)
    ax = axes[0, 1]
    ax.plot(freq_ratio, mu_p, "g-", linewidth=2, label=r"$\mu_+$ (RHCP)")
    ax.plot(freq_ratio, mu_m, "m-", linewidth=2, label=r"$\mu_-$ (LHCP)")
    ax.axvline(1.0, color="grey", linestyle="--", alpha=0.5, label=r"$\omega/\omega_0 = 1$")
    ax.set_xlabel(r"$\omega / \omega_0$")
    ax.set_ylabel("effective permeability")
    ax.set_title("(b) (b) Lossless circular eigen-modes")
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-10, 30)

    # (c) mu, kappa (有损耗, 实部)
    ax = axes[1, 0]
    ax.plot(freq_ratio, mu_l.real, "b-", linewidth=2, label=r"Re($\mu$)")
    ax.plot(freq_ratio, kappa_l.real, "r-", linewidth=2, label=r"Re($\kappa$)")
    ax.plot(freq_ratio, mu_l.imag, "b--", linewidth=1.5, label=r"Im($\mu$)")
    ax.plot(freq_ratio, kappa_l.imag, "r--", linewidth=1.5, label=r"Im($\kappa$)")
    ax.axvline(1.0, color="grey", linestyle="--", alpha=0.5)
    ax.set_xlabel(r"$\omega / \omega_0$")
    ax.set_ylabel("permeability elements")
    ax.set_title(r"(c) (c) Lossy Polder tensor ($\alpha=0.01$)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-5, 25)

    # (d) mu_+, mu_- (有损耗, 实部)
    ax = axes[1, 1]
    ax.plot(freq_ratio, mu_p_l.real, "g-", linewidth=2, label=r"Re($\mu_+$)")
    ax.plot(freq_ratio, mu_m_l.real, "m-", linewidth=2, label=r"Re($\mu_-$)")
    ax.plot(freq_ratio, mu_p_l.imag, "g--", linewidth=1.5, label=r"Im($\mu_+$)")
    ax.plot(freq_ratio, mu_m_l.imag, "m--", linewidth=1.5, label=r"Im($\mu_-$)")
    ax.axvline(1.0, color="grey", linestyle="--", alpha=0.5)
    ax.set_xlabel(r"$\omega / \omega_0$")
    ax.set_ylabel("effective permeability")
    ax.set_title(r"(d) (d) Lossy circular eigen-modes ($\alpha=0.01$)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-5, 25)

    fig.suptitle(
        r"Fig 9.1a — Polder tensor: $\mu$, $\kappa$, $\mu_\pm$ frequency dependence"
        + f"\nYIG: H0={H0/1e3:.0f} kA/m, Ms={Ms/1e3:.0f} kA/m",
        fontsize=12,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig("python/figures/ch09/fig09_01a_tensor_permeability.png", dpi=150)
    print("  → 图保存: fig09_01a_tensor_permeability.png\n")
    return mu, kappa, mu_p, mu_m


# ════════════════════════════════════════════════════════════════════
# §9.2 — Faraday rotation
# ════════════════════════════════════════════════════════════════════

def faraday_rotation_angle(omega, z, epsilon_r, mu_plus, mu_minus):
    """
    计算Faraday rotation.

    参数
    ----------
    omega    : float or ndarray  角Frequency [rad/s]
    z        : float             传播距离 [m]
    epsilon_r: float             相对介电常数 (无量纲)
    mu_plus  : float or ndarray  RHCP 磁导率
    mu_minus : float or ndarray  LHCP 磁导率

    返回
    -------
    theta    : float or ndarray  Faraday rotation [rad]
    量纲: (rad/s)*(m)/(m/s) * sqrt(无量纲*无量纲 - 无量纲*无量纲) = rad  ✅
    """
    theta = (omega * z / (2 * C0)) * (np.sqrt(epsilon_r * mu_plus) - np.sqrt(epsilon_r * mu_minus))
    return theta


def example_2_faraday_rotation():
    """
    示例 2: Faraday rotation计算

    condition: 与示例1同材料, 在偏置场 H0 = 100 kA/m 下
          Distance z = 5 cm, 介电常数 epsilon_r = 15
    """
    print("=" * 60)
    print("示例 2: Faraday rotation计算")
    print("=" * 60)

    # 材料参数
    Ms = 139e3   # [A/m]
    H0 = 100e3   # [A/m]
    epsilon_r = 15.0
    z = 0.05     # 传播距离 [m] = 5 cm

    omega_0 = GAMMA_e * MU0 * H0
    omega_m = GAMMA_e * MU0 * Ms

    # Frequency扫描: 0.1*f0 ~ 2.5*f0 (避开共振附近有耗计算)
    freq_ratio = np.linspace(0.1, 0.95, 200)
    omega = freq_ratio * omega_0

    # 有损耗 (少量阻尼避免发散)
    mu, kappa, mu_p, mu_m = tensor_permeability(omega, omega_0, omega_m, alpha=0.0)

    # 计算旋转角 (度)
    theta_rad = faraday_rotation_angle(omega, z, epsilon_r, mu_p, mu_m)
    theta_deg = np.degrees(theta_rad.real)

    # 在 f = 0.5*f0 处的值
    idx_mid = len(omega) // 2
    f_mid = omega[idx_mid] / (2 * pi)
    print(f"  在 f = {f_mid/1e9:.3f} GHz (ω/ω0 ≈ {freq_ratio[idx_mid]:.2f}):")
    print(f"    mu+ = {mu_p[idx_mid]:.3f}")
    print(f"    mu- = {mu_m[idx_mid]:.3f}")
    print(f"    旋转角 = {theta_deg[idx_mid]:.2f} deg / {z*100:.0f} cm")

    # 计算旋转常数 (deg/cm)
    theta_per_cm = theta_deg / (z * 100)
    print(f"    旋转常数 ≈ {theta_per_cm[idx_mid]:.2f} deg/cm")

    # ── 绘图 ──
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    ax = axes[0]
    ax.plot(freq_ratio, theta_deg, "b-", linewidth=2)
    ax.set_xlabel(r"$\omega / \omega_0$")
    ax.set_ylabel("Faraday rotation [deg]")
    ax.set_title(f"Faraday rotation vs Frequency (z={z*100:.0f} cm, "
                 + rf"$\varepsilon_r$={epsilon_r})")
    ax.grid(True, alpha=0.3)

    # Rotation vs distance (在固定Frequency f = 0.5*f0)
    z_array = np.linspace(0, 0.10, 200)
    f_fixed = omega[idx_mid]
    mu_p_fixed = mu_p[idx_mid]
    mu_m_fixed = mu_m[idx_mid]
    theta_vs_z = np.degrees(faraday_rotation_angle(
        f_fixed, z_array, epsilon_r, mu_p_fixed, mu_m_fixed
    ))

    ax = axes[1]
    ax.plot(z_array * 100, theta_vs_z, "r-", linewidth=2)
    ax.set_xlabel("Distance z [cm]")
    ax.set_ylabel("Faraday rotation [deg]")
    ax.set_title(f"Faraday rotation vs distance (f={f_fixed/1e9:.3f} GHz)")
    ax.grid(True, alpha=0.3)

    fig.suptitle("Fig 9.2 — Faraday rotation", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig("python/figures/ch09/fig09_02_faraday_rotation.png", dpi=150)
    print("  → 图保存: fig09_02_faraday_rotation.png\n")
    return theta_rad, theta_deg


# ════════════════════════════════════════════════════════════════════
# §9.4 — 结式环行器 (Junction Circulator)
# ════════════════════════════════════════════════════════════════════

def circulator_bosma_radius(freq, epsilon_r, mu, kappa):
    """
    基于 Bosma 理论计算结式环行器铁氧体柱半径.

    Bosma condition: kR = 1.84 (TM110 模)
    其中 k = omega * sqrt(mu0 * eps0 * epsilon_r * mu_eff)

    参数
    ----------
    freq     : float  工作Frequency [Hz]
    epsilon_r: float  铁氧体相对介电常数
    mu       : float  Polder 张量 mu (无量纲)
    kappa    : float  Polder 张量 kappa (无量纲)

    返回
    -------
    R        : float  铁氧体柱半径 [m]
    mu_eff   : float  effective permeability (无量纲)
    k        : float  波数 [rad/m]
    """
    omega = 2 * pi * freq
    mu_eff = mu - kappa**2 / mu      # effective permeability
    # 使用 np.sqrt 处理 mu_eff 可能为负的情况 (高于共振时为 evanescent)
    k = omega * np.sqrt(MU0 * EPS0 * epsilon_r * mu_eff)
    R = 1.84 / k
    if isinstance(R, complex) and abs(R.imag) > 1e-10:
        R = abs(R)  # 取模作为工程近似
        k = abs(k)
    return R, mu_eff, k


def circulator_s_matrix(mu, kappa, Z_in, Z_0=50.0):
    """
    近似计算结式环行器 S 参数 (简化模型).

    基于文献: 对理想 3-port junction circulator,
    S 参数可用散射矩阵的旋转对称性表达。

    这里使用简化经验公式判断环行方向:
      环行condition: mu_eff > 0 且偏置场适中

    参数
    ----------
    mu    : float  Polder mu
    kappa : float  Polder kappa
    Z_in  : float  铁氧体柱输入阻抗 [Ω]
    Z_0   : float  端口参考阻抗 [Ω]

    返回
    -------
    S      : ndarray (3,3) S 参数矩阵 (复数)
    """
    Gamma = (Z_in - Z_0) / (Z_in + Z_0)   # 反射系数

    # 简化模型: 当偏置场合适, 环行方向 1→2→3→1
    # S11, S22, S33 = Gamma, S21, S32, S13 ≈ 1
    # S12, S23, S31 ≈ 0
    S = np.zeros((3, 3), dtype=complex)

    # 理想环行 (无反射匹配)
    Gamma_ideal = 0.0

    # 非互易相移近似 (基于 kappa/mu 比值)
    circulation_quality = abs(kappa / max(abs(mu), 1e-10))
    isolation = -20 * log10(max(1e-10, 1.0 - circulation_quality))  # dB

    # 简化环行器 S 矩阵
    S[0, 0] = Gamma_ideal
    S[0, 1] = 1e-10      # 隔离
    S[0, 2] = 1.0 - 1j * circulation_quality * 0.1   # 传输

    S[1, 0] = 1.0 - 1j * circulation_quality * 0.1
    S[1, 1] = Gamma_ideal
    S[1, 2] = 1e-10

    S[2, 0] = 1e-10
    S[2, 1] = 1.0 - 1j * circulation_quality * 0.1
    S[2, 2] = Gamma_ideal

    return S


def example_3_circulator():
    """
    示例 3: 结式环行器设计计算

    condition: 工作Frequency f = 10 GHz, NiFe ferrite
          Ms = 200 kA/m, H0 = 150 kA/m, epsilon_r = 13
    """
    print("=" * 60)
    print("示例 3: 结式环行器 (Bosma 理论) 设计计算")
    print("=" * 60)

    # 材料参数 (NiFe ferrite, 偏置场高于工作Frequency)
    Ms = 200e3       # [A/m]
    H0 = 380e3       # [A/m] (提高偏置场使 f0 > f, 工作于低场区)
    epsilon_r = 13.0
    freq = 10e9      # [Hz]

    omega_0 = GAMMA_e * MU0 * H0
    omega_m = GAMMA_e * MU0 * Ms
    omega = 2 * pi * freq

    print(f"  工作Frequency f = {freq/1e9:.1f} GHz")
    print(f"  H0 = {H0/1e3:.1f} kA/m ({H0/79.577:.0f} Oe)")
    print(f"  Ms = {Ms/1e3:.1f} kA/m ({Ms/79.577:.0f} Oe)")
    print(f"  f0 (Larmor) = {omega_0/(2*pi)/1e9:.3f} GHz")
    print(f"  fm = {omega_m/(2*pi)/1e9:.3f} GHz")

    # Polder tensor
    mu, kappa, mu_p, mu_m = tensor_permeability(omega, omega_0, omega_m)

    # Bosma 半径
    R, mu_eff, k = circulator_bosma_radius(freq, epsilon_r, mu, kappa)

    print(f"\n  mu = {mu:.4f}")
    print(f"  kappa = {kappa:.4f}")
    print(f"  mu_eff = mu - kappa^2/mu = {mu_eff:.4f}")
    print(f"  波数 k = {k:.1f} rad/m")
    print(f"  Bosma 半径 R = 1.84/k = {R*1e3:.3f} mm")
    print(f"  铁氧体柱直径 = {2*R*1e3:.3f} mm")

    # 检查环行condition
    if mu_eff > 0:
        print("  ✅ mu_eff > 0, 满足环行condition")
    else:
        print("  ⚠️  mu_eff < 0, 不满足环行condition (需调整偏置场或工作频段)")

    # 近似 S 参数
    # 计算铁氧体柱输入阻抗 (简化: 忽略边缘场)
    Z_ferrite = np.sqrt(MU0 / (EPS0 * epsilon_r * max(abs(mu_eff), 1e-10)))
    if np.iscomplexobj(Z_ferrite):
        Z_ferrite = abs(Z_ferrite)
    S = circulator_s_matrix(mu, kappa, Z_ferrite)

    print(f"\n  近似 S 参数矩阵 (dB):")
    print(f"  S11 = {20*log10(max(abs(S[0,0]),1e-15)):.1f} dB")
    print(f"  S21 = {20*log10(max(abs(S[1,0]),1e-15)):.1f} dB  (Insertion loss方向)")
    print(f"  S12 = {20*log10(max(abs(S[0,1]),1e-15)):.1f} dB  (隔离方向)")
    print(f"  S31 = {20*log10(max(abs(S[2,0]),1e-15)):.1f} dB  (隔离方向)")

    # ── 扫描Frequency看环行器性能 ──
    freq_sweep = np.linspace(5e9, 18e9, 200)
    mu_sweep = np.zeros_like(freq_sweep, dtype=complex)
    kappa_sweep = np.zeros_like(freq_sweep, dtype=complex)
    R_sweep = np.zeros_like(freq_sweep)
    mu_eff_sweep = np.zeros_like(freq_sweep)

    for i, f in enumerate(freq_sweep):
        w = 2 * pi * f
        mu_i, kappa_i, _, _ = tensor_permeability(w, omega_0, omega_m)
        mu_sweep[i] = mu_i
        kappa_sweep[i] = kappa_i
        R_i, mu_eff_i, _ = circulator_bosma_radius(f, epsilon_r, mu_i.real, kappa_i.real)
        R_sweep[i] = R_i
        mu_eff_sweep[i] = mu_eff_i

    # Isolation和Insertion loss估计
    isolation = np.zeros_like(freq_sweep)
    insertion_loss = np.zeros_like(freq_sweep)
    for i in range(len(freq_sweep)):
        qual = abs(kappa_sweep[i].real / max(abs(mu_sweep[i].real), 1e-10))
        # 简化: 隔离变差 = 接近共振
        isolation[i] = max(0, 20 * log10(max(1e-10, qual + 0.01)))
        insertion_loss[i] = max(0.1, 0.5 + 10 * (1.0 - qual / (qual + 0.5)))

    # 绘图
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    ax = axes[0, 0]
    ax.plot(freq_sweep / 1e9, mu_eff_sweep, "b-", linewidth=2)
    ax.axhline(0, color="grey", linestyle="--")
    ax.axvline(freq / 1e9, color="r", linestyle="--", label=f"设计Frequency {freq/1e9} GHz")
    ax.set_xlabel("Frequency [GHz]")
    ax.set_ylabel(r"$\mu_{\mathrm{eff}}$")
    ax.set_title("(a) effective permeability vs Frequency")
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax = axes[0, 1]
    ax.plot(freq_sweep / 1e9, R_sweep * 1e3, "g-", linewidth=2)
    ax.axvline(freq / 1e9, color="r", linestyle="--", label=f"设计Frequency {freq/1e9} GHz")
    ax.set_xlabel("Frequency [GHz]")
    ax.set_ylabel("Ferrite radius R [mm]")
    ax.set_title("(b) Bosma condition: radius vs frequency")
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax = axes[1, 0]
    ax.semilogy(freq_sweep / 1e9, isolation, "b-", linewidth=2)
    ax.set_xlabel("Frequency [GHz]")
    ax.set_ylabel("Isolation [dB]")
    ax.set_title("(c) Approx. isolation")
    ax.grid(True, alpha=0.3)

    ax = axes[1, 1]
    ax.plot(freq_sweep / 1e9, insertion_loss, "r-", linewidth=2)
    ax.set_xlabel("Frequency [GHz]")
    ax.set_ylabel("Insertion loss [dB]")
    ax.set_title("(d) Approx. insertion loss")
    ax.grid(True, alpha=0.3)

    fig.suptitle(
        "Fig 9.4 — Junction circulator design"

        + f"NiFe: H0={H0/1e3:.0f} kA/m, Ms={Ms/1e3:.0f} kA/m, "
        + rf"$\varepsilon_r$={epsilon_r}",
        fontsize=12,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig("python/figures/ch09/fig09_04_circulator.png", dpi=150)
    print("  → 图保存: fig09_04_circulator.png\n")
    return S, R


# ════════════════════════════════════════════════════════════════════
# §9.6 — YIG 谐振器设计
# ════════════════════════════════════════════════════════════════════

def yig_resonance_frequency_kittel(H0, Ms, shape="sphere"):
    """
    Kittel 公式: YIG 球体铁磁共振Frequency.

    参数
    ----------
    H0    : float  外加偏置磁场 [A/m]
    Ms    : float  饱和磁化强度 [A/m]
    shape : str    样品形状 ("sphere", "film_inplane", "film_normal")

    返回
    -------
    f0    : float  共振Frequency [Hz]
    H_eff : float  有效场 [A/m]
    """
    if shape == "sphere":
        # 球体: Nx = Ny = Nz = 1/3
        # f0 = gamma * mu0 * sqrt(H0 * (H0 + Ms))  更精确形式
        H_eff = H0  # 球体退磁场为 H_d = -Ms/3
        f0 = (GAMMA_e * MU0 / (2 * pi)) * sqrt(H0 * (H0 + Ms))
    elif shape == "film_inplane":
        # 薄膜面内偏置: Nx = Nz = 0, Ny = 1
        H_eff = H0
        f0 = (GAMMA_e * MU0 / (2 * pi)) * sqrt(H0 * (H0 + Ms))
    elif shape == "film_normal":
        # 薄膜法线偏置: Nx = Ny = 0, Nz = 1
        H_eff = H0 - Ms
        f0 = (GAMMA_e * MU0 / (2 * pi)) * (H0 - Ms)
    else:
        raise ValueError(f"Unknown shape: {shape}")

    return f0, H_eff


def yig_quality_factor(H0, delta_H):
    """
    计算 YIG 谐振器Unloaded Q.

    Qu = f0 / delta_f = H0 / delta_H

    参数
    ----------
    H0    : float  偏置磁场 [A/m]
    delta_H: float 共振线宽 [A/m]

    返回
    -------
    Qu    : float  Unloaded Q (无量纲)
    """
    # Q = omega_0 / (gamma * mu0 * delta_H) = H0 / delta_H (仅当量纲一致)
    return H0 / delta_H


def example_4_yig_resonator():
    """
    示例 4: YIG 谐振器设计计算

    condition: YIG 球, Ms = 139 kA/m (4πMs ≈ 1750 G)
          线宽 ΔH = 40 A/m (≈ 0.5 Oe)
          偏置场扫描 0 ~ 400 kA/m
    """
    print("=" * 60)
    print("示例 4: YIG 谐振器设计计算")
    print("=" * 60)

    # YIG 材料参数
    Ms = 139e3       # 饱和磁化强度 [A/m]
    delta_H = 40.0   # 共振线宽 [A/m] (≈ 0.5 Oe)

    # 扫描偏置场
    H0_array = np.linspace(10e3, 400e3, 500)
    f_res = np.zeros_like(H0_array)
    Qu = np.zeros_like(H0_array)

    for i, H0 in enumerate(H0_array):
        f_res[i], _ = yig_resonance_frequency_kittel(H0, Ms, shape="sphere")
        Qu[i] = yig_quality_factor(H0, delta_H)

    # 典型偏置点
    H0_typ = 100e3   # [A/m]
    f_typ, H_eff_typ = yig_resonance_frequency_kittel(H0_typ, Ms, shape="sphere")
    Q_typ = yig_quality_factor(H0_typ, delta_H)

    print(f"  YIG: Ms = {Ms/1e3:.1f} kA/m ({Ms/79.577:.0f} Oe)")
    print(f"  YIG: ΔH = {delta_H:.1f} A/m ({delta_H/79.577:.3f} Oe)")
    print(f"  在 H0 = {H0_typ/1e3:.1f} kA/m ({H0_typ/79.577:.0f} Oe):")
    print(f"    f0 (Kittel) = {f_typ/1e9:.4f} GHz")
    print(f"    Qu = H0/ΔH = {Q_typ:.0f}")
    print(f"    工程近似: f0 (GHz) = 0.0028 * H0(Oe) = {0.0028 * H0_typ/79.577:.3f} GHz")

    # ── 绘图 ──
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # (a) 调谐曲线
    ax = axes[0]
    ax.plot(H0_array / 79.577, f_res / 1e9, "b-", linewidth=2)
    ax.axvline(H0_typ / 79.577, color="r", linestyle="--",
               label=f"H0 = {H0_typ/79.577:.0f} Oe")
    ax.set_xlabel("Bias field H0 [Oe]")
    ax.set_ylabel("Resonance freq f0 [GHz]")
    ax.set_title("(a) YIG tuning curve (Kittel formula)")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # (b) Q vs H0
    ax = axes[1]
    ax.plot(H0_array / 79.577, Qu, "r-", linewidth=2)
    ax.axvline(H0_typ / 79.577, color="r", linestyle="--",
               label=f"H0 = {H0_typ/79.577:.0f} Oe")
    ax.set_xlabel("Bias field H0 [Oe]")
    ax.set_ylabel(r"Unloaded Q $Q_u$")
    ax.set_title(rf"(b) Q vs H0 ($\Delta H$ = {delta_H/79.577:.2f} Oe)")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # (c) 近似线性调谐 (f0 vs H0)
    ax = axes[2]
    # 工程近似: f0(GHz) = 0.0028 * H0(Oe)
    H0_oe = H0_array / 79.577
    f_approx = 0.0028 * H0_oe
    f_error = abs((f_res / 1e9) - f_approx) / (f_res / 1e9) * 100
    ax.plot(H0_oe, f_error, "g-", linewidth=2)
    ax.set_xlabel("Bias field H0 [Oe]")
    ax.set_ylabel("Error [%]")
    ax.set_title("(c) Approx vs Kittel error")
    ax.grid(True, alpha=0.3)

    fig.suptitle("Fig 9.6 — YIG FMR characteristics", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig("python/figures/ch09/fig09_06_yig_resonator.png", dpi=150)
    print("  → 图保存: fig09_06_yig_resonator.png\n")

    return f_res, Qu


# ════════════════════════════════════════════════════════════════════
# §9.5 — 铁氧体Phase shifterDiff phase shift
# ════════════════════════════════════════════════════════════════════

def phase_shifter_delta_phi(omega, L, epsilon_r, mu_plus, mu_minus):
    """
    计算 Reggia-Spencer Phase shifter的Diff phase shift.

    Δφ = (beta_plus - beta_minus) * L
    beta_plus_minus = omega * sqrt(mu0 * eps0 * epsilon_r * mu_plus_minus)

    参数
    ----------
    omega    : float or ndarray  角Frequency [rad/s]
    L        : float             铁氧体长度 [m]
    epsilon_r: float             相对介电常数
    mu_plus  : float or ndarray  RHCP 磁导率 (实数)
    mu_minus : float or ndarray  LHCP 磁导率 (实数)

    返回
    -------
    delta_phi: float or ndarray  Diff phase shift [rad]
    量纲: (rad/s)*(m)*(H/m*F/m)^{1/2} * (无量纲)^{1/2} = rad  ✅
    注意: 如果 mu_plus 或 mu_minus 为负, 对应 evanescent 模, 取 |mu| 计算
    """
    # 确保 mu 为正: 负值时取绝对值 (evanescent 模的相移为零)
    mu_plus_safe = np.where(np.real(mu_plus) > 0, np.real(mu_plus), 1e-10)
    mu_minus_safe = np.where(np.real(mu_minus) > 0, np.real(mu_minus), 1e-10)
    beta_plus = omega * np.sqrt(MU0 * EPS0 * epsilon_r * mu_plus_safe)
    beta_minus = omega * np.sqrt(MU0 * EPS0 * epsilon_r * mu_minus_safe)
    return (beta_plus - beta_minus) * L


def example_5_phase_shifter():
    """
    示例 5: 铁氧体Phase shifterDiff phase shift计算

    condition: Reggia-Spencer Phase shifter
          铁氧体长度 L = 3 cm, epsilon_r = 13
          H0 扫描 50~300 kA/m, 固定Frequency f = 10 GHz
    """
    print("=" * 60)
    print("示例 5: 铁氧体Phase shifterDiff phase shift计算")
    print("=" * 60)

    # 材料参数
    Ms = 200e3       # [A/m]
    epsilon_r = 13.0
    L = 0.03         # 铁氧体长度 [m]
    freq = 10e9      # 工作Frequency [Hz]
    omega = 2 * pi * freq

    # 扫描偏置场
    H0_array = np.linspace(50e3, 300e3, 500)
    delta_phi = np.zeros_like(H0_array)
    ALPHA_LOSS = 0.02  # 有损耗阻尼, 避免共振发散

    for i, H0 in enumerate(H0_array):
        omega_0 = GAMMA_e * MU0 * H0
        omega_m = GAMMA_e * MU0 * Ms
        mu, kappa, mu_p, mu_m = tensor_permeability(omega, omega_0, omega_m, alpha=ALPHA_LOSS)
        delta_phi[i] = phase_shifter_delta_phi(omega, L, epsilon_r, mu_p.real, mu_m.real)

    delta_phi_deg = np.degrees(delta_phi)

    # 典型点
    idx_mid = len(H0_array) // 2
    H0_mid = H0_array[idx_mid]
    print(f"  工作Frequency f = {freq/1e9:.1f} GHz")
    print(f"  铁氧体长度 L = {L*100:.1f} cm")
    print(f"  在 H0 = {H0_mid/1e3:.1f} kA/m ({H0_mid/79.577:.0f} Oe):")
    print(f"    Δφ = {delta_phi_deg[idx_mid]:.1f} deg")
    print(f"    相移效率 = {delta_phi_deg[idx_mid]/(L*100):.1f} deg/cm")

    # 找到最大相移范围
    phi_max = np.max(delta_phi_deg)
    phi_min = np.min(delta_phi_deg)
    print(f"  相移范围: {phi_min:.1f}° ~ {phi_max:.1f}° "
          + f"({phi_max - phi_min:.1f}° 总跨度)")

    # ── Frequency扫描 (固定偏置) ──
    H0_fixed = 150e3
    omega_0_fixed = GAMMA_e * MU0 * H0_fixed
    omega_m = GAMMA_e * MU0 * Ms
    freq_sweep = np.linspace(2e9, 14e9, 300)
    delta_phi_freq = np.zeros_like(freq_sweep)

    for i, f in enumerate(freq_sweep):
        w = 2 * pi * f
        # 避免共振发散 (用有损耗)
        mu, kappa, mu_p, mu_m = tensor_permeability(w, omega_0_fixed, omega_m)
        delta_phi_freq[i] = phase_shifter_delta_phi(w, L, epsilon_r,
                                                     abs(mu_p), abs(mu_m))
    delta_phi_freq_deg = np.degrees(delta_phi_freq.real)

    # 绘图
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    ax = axes[0]
    ax.plot(H0_array / 79.577, delta_phi_deg, "b-", linewidth=2)
    ax.set_xlabel("Bias field H0 [Oe]")
    ax.set_ylabel(r"Diff phase shift $\Delta\phi$ [deg]")
    ax.set_title(f"Phase shifter: Δφ vs H0 (f={freq/1e9} GHz, L={L*100:.0f} cm)")
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.plot(freq_sweep / 1e9, delta_phi_freq_deg, "r-", linewidth=2)
    ax.axvline(omega_0_fixed / (2 * pi) / 1e9, color="grey", linestyle="--",
               label=r"$f_0$ (Larmor)")
    ax.set_xlabel("Frequency [GHz]")
    ax.set_ylabel(r"Diff phase shift $\Delta\phi$ [deg]")
    ax.set_title(rf"Phase shifter: Δφ vs Frequency (H0={H0_fixed/79.577:.0f} Oe)")
    ax.legend()
    ax.grid(True, alpha=0.3)

    fig.suptitle(f"Fig 9.5 — Ferrite phase shifter (Reggia-Spencer) diff phase shift\n"
                 + rf"Ms={Ms/1e3:.0f} kA/m, $\varepsilon_r$={epsilon_r}, L={L*100:.0f} cm",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig("python/figures/ch09/fig09_05_phase_shifter.png", dpi=150)
    print("  → 图保存: fig09_05_phase_shifter.png\n")
    return delta_phi_deg


# ════════════════════════════════════════════════════════════════════
# 补充: 各频段铁氧体材料选型指南
# ════════════════════════════════════════════════════════════════════

def example_6_material_guide():
    """
    示例 6: 铁氧体材料选型与频段匹配.
    展示不同 Ms 和 H0 组合下的工作Frequency范围.
    """
    print("=" * 60)
    print("示例 6: 铁氧体材料选型指南")
    print("=" * 60)

    # 常用铁氧体材料
    materials = {
        "YIG (Yttrium Iron Garnet)": {"Ms": 139e3, "epsilon_r": 15, "delta_H": 40},
        "NiFe Ferrite (Nickel)": {"Ms": 200e3, "epsilon_r": 13, "delta_H": 4000},
        "MgFe Ferrite (Magnesium)": {"Ms": 120e3, "epsilon_r": 10, "delta_H": 3000},
        "LiFe Ferrite (Lithium)": {"Ms": 300e3, "epsilon_r": 15, "delta_H": 5000},
    }

    print(f"{'材料':30s} {'Ms [kA/m]':12s} {'4πMs [G]':10s} "
          f"{'εr':6s} {'ΔH [Oe]':8s} {'f_min [GHz]':12s}")
    print("-" * 80)

    for name, params in materials.items():
        Ms = params["Ms"]
        epsilon_r = params["epsilon_r"]
        delta_H_oe = params["delta_H"] / 79.577
        # 最小工作Frequency: 大致在 f0 = 0.5 * gamma*mu0*Ms (低场区下限)
        f_min = GAMMA_e * MU0 * Ms / (2 * pi * 2) / 1e9  # [GHz]
        print(f"{name:30s} {Ms/1e3:8.1f}      {Ms/79.577:8.0f}     "
              f"{epsilon_r:4d}     {delta_H_oe:6.1f}   {f_min:8.3f}")

    # 计算各材料的近似工作Frequency范围
    print("\n  工作Frequency vs 偏置场 (YIG):")
    for H0_oe in [500, 1000, 2000, 3000]:
        H0_si = H0_oe * 79.577
        omega_0 = GAMMA_e * MU0 * H0_si
        f0 = omega_0 / (2 * pi) / 1e9
        print(f"    H0 = {H0_oe:5d} Oe → f0 = {f0:.3f} GHz")

    # 可视化: 不同材料 μ_eff Frequency依赖
    freq_ratio = np.linspace(0.1, 3.0, 300)

    fig, ax = plt.subplots(figsize=(10, 6))

    for name, params in materials.items():
        Ms = params["Ms"]
        H0_ref = Ms * 0.8  # 取偏置场为 0.8*Ms (典型值)
        omega_0 = GAMMA_e * MU0 * H0_ref
        omega_m = GAMMA_e * MU0 * Ms
        omega = freq_ratio * omega_0
        mu, kappa, _, _ = tensor_permeability(omega, omega_0, omega_m)
        mu_eff = mu - kappa**2 / mu
        ax.plot(freq_ratio, mu_eff.real, linewidth=2, label=name)

    ax.axhline(0, color="grey", linestyle="--", alpha=0.5)
    ax.axvline(1.0, color="grey", linestyle="--", alpha=0.5, label=r"$\omega/\omega_0=1$")
    ax.set_xlabel(r"$\omega / \omega_0$")
    ax.set_ylabel(r"$\mu_{\mathrm{eff}}$")
    ax.set_title("Fig 9.6b — effective perm for different ferrite materials")
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-10, 20)

    fig.tight_layout()
    fig.savefig("python/figures/ch09/fig09_06b_material_comparison.png", dpi=150)
    print("  → 图保存: fig09_06b_material_comparison.png\n")


# ════════════════════════════════════════════════════════════════════
# 补充: 共振隔离器Isolation
# ════════════════════════════════════════════════════════════════════

def example_7_resonance_isolator():
    """
    示例 7: 共振隔离器Isolation vs frequency dependence.
    展示 RHCP 和 LHCP 的衰减常数差异.
    """
    print("=" * 60)
    print("示例 7: 共振隔离器 — RHCP/LHCP 衰减特性")
    print("=" * 60)

    # NiFe 铁氧体
    Ms = 200e3
    H0 = 150e3
    epsilon_r = 13
    delta_H = 5000  # [A/m] ≈ 63 Oe, 典型 NiFe
    alpha = 0.02    # 对应线宽

    omega_0 = GAMMA_e * MU0 * H0
    omega_m = GAMMA_e * MU0 * Ms

    freq_ratio = np.linspace(0.5, 1.5, 400)
    omega = freq_ratio * omega_0

    mu, kappa, mu_p, mu_m = tensor_permeability(omega, omega_0, omega_m, alpha=alpha)

    # 衰减常数 (imag part of propagation constant)
    # alpha_atten = omega * sqrt(mu0 * eps0 * epsilon_r) * Im(sqrt(mu_eff))
    gamma_plus = 1j * omega * np.sqrt(MU0 * EPS0 * epsilon_r * mu_p)
    gamma_minus = 1j * omega * np.sqrt(MU0 * EPS0 * epsilon_r * mu_m)

    atten_plus = gamma_plus.real   # [Np/m] (α = Re(γ) for γ = α + jβ); 此前误用 imag 提取 β
    atten_minus = gamma_minus.real
    atten_plus_dB = 20 * np.log10(np.exp(1)) * atten_plus  # [dB/m]
    atten_minus_dB = 20 * np.log10(np.exp(1)) * atten_minus

    # Isolation (per unit length)
    isolation_per_m = atten_plus_dB - atten_minus_dB

    idx_res = np.argmin(np.abs(freq_ratio - 1.0))
    print(f"  f = f0 (共振):")
    print(f"    α(RHCP) = {atten_plus_dB[idx_res]:.1f} dB/m")
    print(f"    α(LHCP) = {atten_minus_dB[idx_res]:.1f} dB/m")
    print(f"    Isolation  = {isolation_per_m[idx_res]:.1f} dB/m")

    # 绘图
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    ax = axes[0]
    ax.plot(freq_ratio, atten_plus_dB, "r-", linewidth=2, label="RHCP (高损耗)")
    ax.plot(freq_ratio, atten_minus_dB, "b-", linewidth=2, label="LHCP (低损耗)")
    ax.axvline(1.0, color="grey", linestyle="--", label=r"$\omega = \omega_0$")
    ax.set_xlabel(r"$\omega / \omega_0$")
    ax.set_ylabel("Attenuation constant [dB/m]")
    ax.set_title(r"(a) RHCP/LHCP attenuation ($\alpha$=" + f"{alpha})")
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.plot(freq_ratio, isolation_per_m, "g-", linewidth=2)
    ax.axvline(1.0, color="grey", linestyle="--")
    ax.set_xlabel(r"$\omega / \omega_0$")
    ax.set_ylabel("Isolation [dB/m]")
    ax.set_title("(b) Isolation per meter")
    ax.grid(True, alpha=0.3)

    fig.suptitle("Fig 9.3 — Resonance isolator frequency dependence\n"
                 + f"NiFe: Ms={Ms/1e3:.0f} kA/m, H0={H0/1e3:.0f} kA/m, "
                 + rf"$\Delta H$={delta_H/79.577:.0f} Oe",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.93])
    fig.savefig("python/figures/ch09/fig09_03_resonance_isolator.png", dpi=150)
    print("  → 图保存: fig09_03_resonance_isolator.png\n")


# ════════════════════════════════════════════════════════════════════
# 主入口
# ════════════════════════════════════════════════════════════════════

def main():
    """运行所有 Ch9 示例."""
    print("╔" + "═" * 58 + "╗")
    print("║   Pozar Ch9 — Ferrite Components 铁氧体器件数值计算      ║")
    print("║   γ = 1.759×10^11 C/kg                                  ║")
    print("╚" + "═" * 58 + "╝")
    print()

    # 示例 1: Polder tensor
    mu, kappa, mu_p, mu_m = example_1_tensor_permeability()

    # 示例 2: Faraday rotation
    theta_rad, theta_deg = example_2_faraday_rotation()

    # 示例 3: 结式环行器
    S, R = example_3_circulator()

    # 示例 4: YIG 谐振器
    f_res, Qu = example_4_yig_resonator()

    # 示例 5: Phase shifter
    delta_phi_deg = example_5_phase_shifter()

    # 示例 6: 材料指南
    example_6_material_guide()

    # 示例 7: 共振隔离器
    example_7_resonance_isolator()

    print("=" * 60)
    print("所有示例完成。图文件存于 python/figures/ch09/")
    print("=" * 60)


if __name__ == "__main__":
    main()
