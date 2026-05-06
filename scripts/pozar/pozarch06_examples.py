#!/usr/bin/env python3
"""
Pozar《Microwave Engineering》4th Ed., Chapter 6 — Microwave Resonators
示例代码复现 (Examples 6.1–6.7+)

涵盖:
  §6.1  RLC 谐振电路 (f0, Q0, BW)
  §6.2  λ/2 短路传输线谐振器
  §6.3  矩形波导腔 (f_mnp, Q_c)
  §6.4  圆形波导腔 (f_mnp, Bessel 零点表)
  §6.5  介质谐振器 (TE01δ 模近似)
  §6.6  铁氧体谐振器 (FMR 频率, 张量磁导率)
  §6.7  耦合系数提取 (S11 → β)

Author: 二龙虾 (subagent for 🦞)
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.special import jn_zeros, jnp_zeros
from pathlib import Path

# ─── 全局常量 ────────────────────────────────────────────────────────
C0   = 299_792_458          # 真空光速 [m/s]
MU0  = 4e-7 * np.pi         # 真空磁导率 [H/m]
EPS0 = 8.854187817e-12      # 真空介电常数 [F/m]
ETA0 = np.sqrt(MU0 / EPS0)  # 真空波阻抗 ≈ 377 Ω
GAMMA_OVER_2PI = 28.0e9     # 旋磁比 γ/(2π) [Hz/T] = 28 GHz/T

FIG_DIR = Path(__file__).resolve().parent / "figures" / "ch06"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# ─── 辅助函数 ────────────────────────────────────────────────────────

def skin_depth(f, sigma, mu_r=1.0):
    """趋肤深度 δ_s [m]"""
    return np.sqrt(1.0 / (np.pi * f * MU0 * mu_r * sigma))

def surface_resistance(f, sigma):
    """表面电阻 R_s [Ω/sq]"""
    return 1.0 / (sigma * skin_depth(f, sigma))

# =====================================================================
# §6.1  RLC 谐振电路
# =====================================================================

def example_6_1_series_rlc():
    """串联 RLC 谐振电路: 计算 f₀, Q₀, BW"""
    print("=" * 65)
    print("§6.1 Ex 6.1a (扩展): 串联 RLC 谐振")
    print("=" * 65)

    L = 10e-9          # [H]
    C = 1e-12           # [F]
    R = 0.5             # [Ω]

    f0 = 1 / (2 * np.pi * np.sqrt(L * C))
    omega0 = 2 * np.pi * f0
    Q0 = omega0 * L / R
    BW = f0 / Q0

    print(f"  L = {L/1e-9:.1f} nH,  C = {C/1e-12:.1f} pF,  R = {R:.2f} Ω")
    print(f"  f₀ = {f0/1e6:.3f} MHz    Q₀ = {Q0:.1f}    BW = {BW/1e3:.3f} kHz")
    print(f"  ✓ ω₀L/R = Ω·s·H⁻¹·H/Ω → 无量纲")
    print()
    return {"f0": f0, "Q0": Q0, "BW": BW}


def example_6_1_parallel_rlc():
    """并联 RLC 谐振电路"""
    print("-" * 65)
    print("§6.1 Ex 6.1b (扩展): 并联 RLC 谐振")
    print("-" * 65)

    L = 10e-9
    C = 1e-12
    R_par = 20e3        # [Ω]

    f0 = 1 / (2 * np.pi * np.sqrt(L * C))
    omega0 = 2 * np.pi * f0
    Q0 = omega0 * R_par * C
    BW = f0 / Q0

    print(f"  L = {L/1e-9:.1f} nH,  C = {C/1e-12:.1f} pF,  R_par = {R_par/1e3:.1f} kΩ")
    print(f"  f₀ = {f0/1e6:.3f} MHz    Q₀ = {Q0:.1f}    BW = {BW/1e3:.3f} kHz")
    print(f"  ✓ ω₀RC 无量纲")
    print()

# =====================================================================
# §6.2  传输线谐振器 — Pozar Ex 6.1
# =====================================================================

def example_6_2_transmission_line_resonator():
    """
    Pozar Ex 6.1: λ/2 短路同轴线谐振器
    50Ω 空气填充铜同轴线, f₀=5 GHz:
      a=0.889 mm, b=2.692 mm, σ=5.8×10⁷ S/m
    计算: 衰减常数 α_c, 长度 l, Q₀
    """
    print("=" * 65)
    print("§6.2 Ex 6.1 (Pozar): λ/2 短路同轴线谐振器")
    print("=" * 65)

    f0   = 5e9
    a    = 0.889e-3      # [m]
    b    = 2.692e-3      # [m]
    Z0   = 50.0          # [Ω]
    sigma = 5.8e7         # [S/m]

    beta  = 2 * np.pi * f0 / C0
    Rs    = surface_resistance(f0, sigma)
    delta = skin_depth(f0, sigma)

    # 同轴线导体衰减常数 (Pozar §2.7 / Eq 2.119)
    # α_c = Rs/(2·η·Z₀) · (1/a + 1/b) / π ... — 不对, 标准公式:
    # α_c = Rs/(η) · (1/a + 1/b) / (4π · ln(b/a)/π)... 
    # 正确公式 (同轴线 TEM, 内外导体同材料):
    # α_c = (Rs / (2 * Z0)) * (1/a + 1/b) / (2 * np.pi)
    # 但更准确的:
    # α_c = Rs/(2*η) * (1/a + 1/b) / ln(b/a)
    alpha_c = (Rs / (2 * ETA0)) * (1/a + 1/b) / np.log(b/a)

    l = np.pi / beta           # λ/2 (n=1)
    Q0 = beta / (2 * alpha_c)

    print(f"  a={a*1e3:.3f} mm, b={b*1e3:.3f} mm, σ={sigma:.1e} S/m")
    print(f"  f₀={f0/1e9:.2f} GHz, Z₀={Z0:.1f} Ω")
    print(f"  δ = {delta*1e6:.3f} μm")
    print(f"  R_s = {Rs*1e3:.4f} mΩ/sq")
    print(f"  α_c = {alpha_c:.6f} Np/m  (= {alpha_c*8.686:.4f} dB/m)")
    print(f"  l = {l*1e3:.4f} mm  (λ/2 @ {f0/1e9:.2f} GHz)")
    print(f"  Q₀ = β/(2α) = {Q0:.1f}")
    print(f"  ✓ [Q] = (rad/m)/(Np/m) → 1")
    print()

# =====================================================================
# §6.3  矩形波导腔 — Pozar Ex 6.2, 6.3
# =====================================================================

def rect_cavity_f(a, b, d, m, n, p):
    """矩形腔 f_{mnp} [Hz]"""
    k = np.sqrt((np.pi*m/a)**2 + (np.pi*n/b)**2 + (np.pi*p/d)**2)
    return k * C0 / (2*np.pi)

def rect_TE10p_Qc(a, b, d, p, f0, sigma):
    """
    矩形腔 TE₁₀ₚ 导体 Q (Pozar Eq 6.57–6.59)
    Q_c = (k₀ad)³ b η / (2π² R_s) · 1/N
    N = 2b(a³ + (pd)³) + a(pd)(a² + (pd)²)
    """
    k0 = 2 * np.pi * f0 / C0
    Rs = surface_resistance(f0, sigma)
    pd = p * d
    k0ad = k0 * a * d        # 使用物理长度 d, 而非 pd
    N = 2.0 * b * (a**3 + pd**3) + a * pd * (a**2 + pd**2)
    return (k0ad**3 * b * ETA0) / (2 * np.pi**2 * Rs * N)


def example_6_3_rectangular_cavity():
    """
    Pozar Ex 6.2 & 6.3: 矩形腔谐振频率 + Q
    WR-90: a=2.286 cm, b=1.016 cm, d=3.0 cm, 铜 σ=5.8e7 S/m
    """
    print("=" * 65)
    print("§6.3 Ex 6.2-6.3 (Pozar): 矩形波导腔")
    print("=" * 65)

    a = 2.286e-2; b = 1.016e-2; d = 3.0e-2
    sigma = 5.8e7

    print(f"  腔体: a={a*100:.3f} cm, b={b*100:.3f} cm, d={d*100:.2f} cm")
    print(f"  材料: 铜 σ={sigma:.1e} S/m\n")

    modes_f = [("TE₁₀₁", 1,0,1), ("TE₁₀₂", 1,0,2),
               ("TE₁₁₁", 1,1,1), ("TE₁₀₃", 1,0,3)]
    print(f"  {'Mode':8s}  {'f [GHz]':>10s}  {'Q_c':>8s}")
    print(f"  { '-'*28 }")
    for label, m, n, p in modes_f:
        f = rect_cavity_f(a, b, d, m, n, p)
        Qc = rect_TE10p_Qc(a, b, d, p, f, sigma) if n == 0 else 0
        qstr = f"{Qc:.0f}" if Qc > 0 else "  —  "
        print(f"  {label:8s}  {f/1e9:10.4f}  {qstr:>8s}")

    # TE101 详细
    f101 = rect_cavity_f(a, b, d, 1, 0, 1)
    Qc101 = rect_TE10p_Qc(a, b, d, 1, f101, sigma)

    # 对照: Poza 教材不同 d 的 Qc 变化
    d_ref = 2.54e-2
    f_ref = rect_cavity_f(a, b, d_ref, 1, 0, 1)
    Qc_ref = rect_TE10p_Qc(a, b, d_ref, 1, f_ref, sigma)
    print(f"\n  TE₁₀₁ 详细:")
    print(f"    d={d*100:.1f} cm:  f={f101/1e9:.4f} GHz,  Q_c={Qc101:.0f}")
    print(f"    d=2.54 cm:  f={f_ref/1e9:.4f} GHz,  Q_c={Qc_ref:.0f}")
    print(f"    (教材值 ~ 10000-12000 视铜纯度而定)")
    print()

    # 扫描 d
    d_vals = np.linspace(1.5, 5.0, 60) * 1e-2
    f_sweep = np.array([rect_cavity_f(a, b, d, 1, 0, 1) for d in d_vals])
    Q_sweep = np.array([rect_TE10p_Qc(a, b, d, 1, f, sigma)
                        for d, f in zip(d_vals, f_sweep)])

    fig, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(d_vals*100, f_sweep/1e9, 'b-', lw=2, label='f₁₀₁')
    ax1.set_xlabel('Cavity length d [cm]')
    ax1.set_ylabel('f₁₀₁ [GHz]', color='b')
    ax1.tick_params(axis='y', labelcolor='b')
    ax2 = ax1.twinx()
    ax2.plot(d_vals*100, Q_sweep, 'r--', lw=2, label='Q_c')
    ax2.set_ylabel('Q_c', color='r')
    ax2.tick_params(axis='y', labelcolor='r')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    ax1.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "ex6_3_rect_cavity.png", dpi=120)
    plt.close()
    print(f"  →  saved ex6_3_rect_cavity.png\n")


# =====================================================================
# §6.4  圆形波导腔 — Pozar Ex 6.4
# =====================================================================

def circ_cavity_f_TE(a, d, n, m, p):
    """圆形腔 TE_{nmp} 谐振频率"""
    p_prime = jnp_zeros(n, m)[m-1]
    k = np.sqrt((p_prime / a)**2 + (p * np.pi / d)**2)
    return k * C0 / (2*np.pi), p_prime

def circ_cavity_f_TM(a, d, n, m, p):
    """圆形腔 TM_{nmp} 谐振频率"""
    p_root = jn_zeros(n, m)[m-1]
    k = np.sqrt((p_root / a)**2 + (p * np.pi / d)**2)
    return k * C0 / (2*np.pi), p_root


def example_6_4_circular_cavity():
    """
    Pozar Ex 6.4: 圆形腔谐振频率
    a=2 cm, d=3 cm, 空气填充
    """
    print("=" * 65)
    print("§6.4 Ex 6.4 (Pozar): 圆形波导腔")
    print("=" * 65)

    a = 2e-2; d = 3e-2
    print(f"  半径 a={a*100:.1f} cm, 长度 d={d*100:.1f} cm\n")

    print("  Bessel 零点 (scipy 验证):")
    for n in [0, 1, 2]:
        jz = [f"{x:.4f}" for x in jn_zeros(n, 2)]
        jpz = [f"{x:.4f}" for x in jnp_zeros(n, 2)]
        print(f"    J_{n}(x): {', '.join(jz)}   J'_{n}(x): {', '.join(jpz)}")
    print()

    print(f"  {'TE模':12s}  {'p\'_nm':>8s}  {'f [GHz]':>10s}")
    print(f"  {'-'*32}")
    te_modes = [(0,1,1), (1,1,1), (0,1,2), (1,2,1)]
    for n, m, p in te_modes:
        f, pp = circ_cavity_f_TE(a, d, n, m, p)
        print(f"  TE{'{}{}{}'.format(n,m,p):10s}  {pp:8.4f}  {f/1e9:10.4f}")

    print(f"\n  {'TM模':12s}  {'p_nm':>8s}  {'f [GHz]':>10s}")
    print(f"  {'-'*32}")
    tm_modes = [(0,1,1), (1,1,1), (0,2,1), (1,2,1)]
    for n, m, p in tm_modes:
        f, pn = circ_cavity_f_TM(a, d, n, m, p)
        print(f"  TM{'{}{}{}'.format(n,m,p):10s}  {pn:8.4f}  {f/1e9:10.4f}")

    # TE011 vs TM111 简并扫描
    print("\n  TE₀₁₁ vs TM₁₁₁ 模式关系 (a 扫描):")
    a_vals = np.linspace(1.0, 4.0, 80) * 1e-2
    f_TE011 = np.array([circ_cavity_f_TE(aa, d, 0, 1, 1)[0] for aa in a_vals])
    f_TM111 = np.array([circ_cavity_f_TM(aa, d, 1, 1, 1)[0] for aa in a_vals])

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(a_vals*100, f_TE011/1e9, 'b-', lw=2, label='TE₀₁₁')
    ax.plot(a_vals*100, f_TM111/1e9, 'r--', lw=2, label='TM₁₁₁')
    ax.axvline(2, color='gray', ls=':', alpha=0.5, label=f'a=2 cm')
    ax.set_xlabel('Radius a [cm]')
    ax.set_ylabel('f [GHz]')
    ax.set_title('Circular Cavity: TE₀₁₁ vs TM₁₁₁')
    ax.legend(); ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "ex6_4_circular_cavity.png", dpi=120)
    plt.close()
    print(f"  →  saved ex6_4_circular_cavity.png\n")


# =====================================================================
# §6.5  介质谐振器 — Pozar Ex 6.5
# =====================================================================

def example_6_5_dielectric_resonator():
    """
    Pozar Ex 6.5: 圆柱介质谐振器 TE₀₁δ 模
    ε_r=38, a=5 mm, h=4 mm
    """
    print("=" * 65)
    print("§6.5 Ex 6.5 (Pozar): 介质谐振器")
    print("=" * 65)

    eps_r = 38.0; a_mm = 5.0; h_mm = 4.0
    a = a_mm * 1e-3; h = h_mm * 1e-3

    print(f"  ε_r={eps_r}, a={a_mm:.1f} mm, h={h_mm:.1f} mm\n")

    # 方法1: Itoh-Rudokas 公式 (宽高比经验式)
    f1_GHz = 34.0 / (a_mm * np.sqrt(eps_r)) * (a_mm/h_mm + 3.45)**-1
    print(f"  ① Itoh-Rudokas:    f₀ ≈ {f1_GHz:.3f} GHz")
    print(f"     34/(a√ε)·(a/h+3.45)⁻¹  量纲: mm·GHz/mm → GHz ✓")

    # 方法2: 磁壁圆柱腔近似 (TE₀₁δ)
    p_01 = 2.405  # J₀ 的第一个零点
    f2_GHz = C0 / (2*np.pi * np.sqrt(eps_r)) * \
             np.sqrt((np.pi/h)**2 + (p_01/a)**2) / 1e9
    print(f"  ② 磁壁近似:         f₀ ≈ {f2_GHz:.3f} GHz")
    print(f"     c/(2π√ε)·√((π/h)²+(2.405/a)²)  量纲: m/s·m⁻¹=Hz ✓")

    # 方法3: Kajfez-Guillon 修正
    term = (0.43 / (1 + (eps_r - 1) * (a/h)**2))
    k_corr = 2.405 * np.sqrt(1 + term)
    f3_GHz = C0 / (2*np.pi * np.sqrt(eps_r)) * \
             np.sqrt((np.pi/h)**2 + (k_corr/a)**2) / 1e9
    print(f"  ③ Kajfez-Guillon:   f₀ ≈ {f3_GHz:.3f} GHz")
    print(f"     修正横向波数, 计入边缘场\n")

    tan_delta = 1e-4
    Qd = 1.0 / tan_delta
    print(f"  Q_d ≈ 1/tanδ = {Qd:.0f}  (tanδ={tan_delta})")
    print(f"  实际 Q₀ 略低于 Q_d (部分能量在空气中)\n")


# =====================================================================
# §6.6  铁氧体谐振器 — Pozar Ex 6.6
# =====================================================================

def example_6_6_ferrite_resonator():
    """
    Pozar Ex 6.6: YIG 球 FMR 频率
    B₀=0.35 T, γ/(2π)=28 GHz/T
    计算 f₀, 扫描磁场, 张量磁导率
    """
    print("=" * 65)
    print("§6.6 Ex 6.6 (Pozar): 铁氧体谐振器 (FMR)")
    print("=" * 65)

    B0 = 0.35                    # [T]
    gamma = GAMMA_OVER_2PI * 2 * np.pi   # [rad/(s·T)]
    f0 = GAMMA_OVER_2PI * B0     # [Hz]
    omega0 = 2 * np.pi * f0

    print(f"  B₀ = {B0:.3f} T")
    print(f"  f₀ = γ/(2π)·B₀ = {f0/1e9:.4f} GHz")
    print(f"  ✓ 量纲: Hz/T·T = Hz\n")

    # 扫描 B₀
    B_scan = np.linspace(0.05, 1.0, 200)
    f_scan = GAMMA_OVER_2PI * B_scan

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(B_scan, f_scan/1e9, 'b-', lw=2)
    ax.axvline(B0, color='r', ls='--', alpha=0.6, label=f'B₀={B0:.2f}T→{f0/1e9:.2f}GHz')
    ax.set_xlabel('Bias field B₀ [T]'); ax.set_ylabel('FMR frequency [GHz]')
    ax.set_title('Ferromagnetic Resonance: f₀ vs B₀')
    ax.legend(); ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "ex6_6_fmr.png", dpi=120)
    plt.close()
    print("  →  saved ex6_6_fmr.png\n")

    # 张量磁导率 (ω_m 使用典型 YIG 饱和磁化强度)
    Ms = 1.4e5  # [A/m]
    omega_m = gamma * MU0 * Ms
    print(f"  ω_m = γ·μ₀M_s = {omega_m/1e9:.3f} Grad/s")
    print(f"\n  张量磁导率 (在 f₀ 附近, 无阻尼近似):")
    print(f"  {'f/f₀':>7s}  {'μ':>10s}  {'κ':>10s}")
    print(f"  {'-'*29}")

    # 避开精确 f/f₀=1.0 (奇异)
    ratios = [0.90, 0.95, 0.99, 0.999, 1.001, 1.01, 1.05, 1.10]
    for r in ratios:
        omega = r * omega0
        mu_val  = 1 + omega0 * omega_m / (omega0**2 - omega**2)
        kap_val = omega   * omega_m / (omega0**2 - omega**2)
        print(f"  {r:7.3f}  {mu_val:10.3f}  {kap_val:10.3f}")

    print(f"\n  (ω→ω₀ 时 μ,κ → ±∞; 实际有阻尼限制)\n")


# =====================================================================
# §6.7  谐振器耦合 — Pozar Ex 6.7
# =====================================================================

def example_6_7_coupling():
    """
    Pozar Ex 6.7: 从 S₁₁ 提取耦合系数 β
    |S₁₁| = -15 dB → S₁₁_mag → β
    并联谐振: S₁₁ = (β-1)/(β+1)
    """
    print("=" * 65)
    print("§6.7 Ex 6.7 (Pozar): 耦合系数提取")
    print("=" * 65)

    S11_dB = -15.0
    S11_mag = 10**(S11_dB / 20)

    beta_over  = (1 + S11_mag) / (1 - S11_mag)   # β > 1
    beta_under = (1 - S11_mag) / (1 + S11_mag)   # β < 1

    print(f"  |S₁₁| = {S11_dB:.1f} dB  →  |S₁₁|_lin = {S11_mag:.5f}")
    print(f"  β (过耦合, >1):  {beta_over:.4f}")
    print(f"  β (欠耦合, <1):  {beta_under:.4f}")
    print(f"  判断: 看 Smith 圆图低频端走向\n")

    # 曲线: β → RL
    beta_vals = np.logspace(-2, 2, 300)
    S11_beta  = np.abs((beta_vals - 1) / (beta_vals + 1))
    RL_beta   = -20 * np.log10(S11_beta)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))
    ax1.semilogx(beta_vals, RL_beta, 'b-', lw=2)
    ax1.axvline(1, color='r', ls='--', label='$\\beta=1$ (critical)')
    ax1.axhline(-S11_dB, color='g', ls=':', alpha=0.7, label=f'RL={-S11_dB:.0f}dB')
    ax1.set_xlabel('$\\beta$'); ax1.set_ylabel('Return Loss [dB]')
    ax1.set_title('RL vs $\\beta$'); ax1.legend(); ax1.grid(alpha=0.3)
    ax1.set_xlim(0.01, 100)

    ax2.semilogx(beta_vals, S11_beta, 'b-', lw=2)
    ax2.axvline(1, color='r', ls='--', label='$\\beta=1$')
    ax2.axhline(S11_mag, color='g', ls=':', alpha=0.7, label=f'$|S_{{11}}|={S11_mag:.4f}$')
    ax2.set_xlabel('$\\beta$'); ax2.set_ylabel('$|S_{11}|$')
    ax2.set_title('$|S_{11}|$ vs $\\beta$'); ax2.legend(); ax2.grid(alpha=0.3)
    ax2.set_xlim(0.01, 100)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "ex6_7_coupling.png", dpi=120)
    plt.close()
    print(f"  →  saved ex6_7_coupling.png\n")


# =====================================================================
# 附加: RLC 谐振器频率响应曲线
# =====================================================================

def bonus_rlc_response():
    """串联/并联 RLC 的 |Z| 和相位"""
    print("-" * 65)
    print("附加: RLC 谐振器频率响应")
    print("-" * 65)

    f0 = 5e9; L = 10e-9
    C = 1 / ((2*np.pi*f0)**2 * L)
    R = 0.5; G = 5e-5

    f = np.linspace(4.5, 5.5, 1001) * 1e9
    w = 2 * np.pi * f

    Z_ser = R + 1j*(w*L - 1/(w*C))
    Z_par = 1.0 / (G + 1j*(w*C - 1/(w*L)))

    fig, ((a1,a2),(a3,a4)) = plt.subplots(2, 2, figsize=(11, 7))
    a1.plot(f/1e9, np.abs(Z_ser), 'b-', lw=1.5); a1.axvline(f0/1e9, color='r', ls='--')
    a1.set(ylabel='|Z| [Ω]', title='Series RLC'); a1.grid(alpha=0.3)
    a2.plot(f/1e9, np.angle(Z_ser, deg=True), 'b-', lw=1.5); a2.axvline(f0/1e9, color='r', ls='--')
    a2.axhline(0, color='gray', ls=':'); a2.set(ylabel='Phase [deg]', title='Series RLC Phase'); a2.grid(alpha=0.3)
    a3.plot(f/1e9, np.abs(Z_par), 'b-', lw=1.5); a3.axvline(f0/1e9, color='r', ls='--')
    a3.set(xlabel='f [GHz]', ylabel='|Z| [Ω]', title='Parallel RLC'); a3.grid(alpha=0.3)
    a4.plot(f/1e9, np.angle(Z_par, deg=True), 'b-', lw=1.5); a4.axvline(f0/1e9, color='r', ls='--')
    a4.axhline(0, color='gray', ls=':'); a4.set(xlabel='f [GHz]', ylabel='Phase [deg]', title='Parallel RLC Phase'); a4.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "rlc_response.png", dpi=120)
    plt.close()
    print(f"  →  saved rlc_response.png\n")


# =====================================================================
# 主程序
# =====================================================================

if __name__ == "__main__":
    print()
    print("╔" + "═" * 63 + "╗")
    print("║  Pozar Ch6 — Microwave Resonators  例题复现            ║")
    print("╚" + "═" * 63 + "╝\n")

    example_6_1_series_rlc()
    example_6_1_parallel_rlc()
    example_6_2_transmission_line_resonator()
    example_6_3_rectangular_cavity()
    example_6_4_circular_cavity()
    example_6_5_dielectric_resonator()
    example_6_6_ferrite_resonator()
    example_6_7_coupling()
    bonus_rlc_response()

    print("=" * 65)
    print("✅ 全部示例执行完成")
    print("=" * 65)
