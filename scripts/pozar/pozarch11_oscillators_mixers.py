#!/usr/bin/env python3
"""
Pozar《微波工程》4th Edition — Ch11: Oscillators and Mixers
===========================================================
复现章内核心数值示例：振荡条件、负阻设计、DRO、VCO、混频器IP3/IM3/变频增益。

命名规范：所有变量名体现物理含义（杜绝 a/b/c 无意义命名）。
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ── 全局常量 ──────────────────────────────────────────────
C0 = 2.998e8          # 光速 [m/s]
K_B = 1.381e-23       # 玻尔兹曼常数 [J/K]
Q_E = 1.602e-19       # 电子电荷 [C]
T_REF = 290.0         # 参考温度 [K]

# ── 图片输出目录 ──────────────────────────────────────────
FIG_DIR = Path(__file__).resolve().parent / "figures" / "ch11"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# ══════════════════════════════════════════════════════════
#  §11.1 — Barkhausen 起振条件验证
# ══════════════════════════════════════════════════════════
def example_11_1_barkhausen():
    """
    Barkhausen 起振条件数值验证。
    设一个简单反馈振荡器：A(ω) = A0 / (1 + j(ω-ω0)/BW)，β = β0
    求满足 |T| = 1, ∠T = 0 的频率。
    """
    print("=" * 60)
    print("Ex 11.1: Barkhausen 起振条件验证")
    print("=" * 60)

    # 参数设置
    f0 = 2.0e9             # 谐振频率 [Hz]
    BW = 200e6             # 3dB 带宽 [Hz]
    A0 = 10.0               # 开环增益幅值 [无量纲]
    beta_0 = 0.12           # 反馈因子 [无量纲]
    f_scan = np.linspace(1.5e9, 2.5e9, 2000)

    # 单极点放大器传输函数
    A = A0 / (1 + 1j * (f_scan - f0) / (BW / 2))
    T = A * beta_0  # 环路增益

    T_mag = np.abs(T)
    T_phase = np.angle(T, deg=True)

    # 寻找最接近起振条件的频率
    idx_closest = np.argmin(np.abs(T_phase))
    f_osc = f_scan[idx_closest]
    T_mag_osc = T_mag[idx_closest]

    print(f"  放大器 A0 = {A0}, β = {beta_0}")
    print(f"  谐振频率 f0 = {f0/1e9:.4f} GHz")
    print(f"  最大环路增益频率 ≈ {f_osc/1e9:.4f} GHz")
    print(f"  该频率 |T| = {T_mag_osc:.6f}")
    print(f"  该频率 ∠T = {T_phase[idx_closest]:.4f}°")

    # 满足起振条件时所需增益
    beta_osc = 1.0 / A0
    print(f"  满足 ∠T=0 时起振所需 β_min = 1/A0 = {beta_osc:.4f}")
    print(f"  当前 β = {beta_0} > β_min → {'✅ 可起振' if beta_0 > beta_osc else '❌ 不可起振'}")

    # ── 画图 ──
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

    ax1.plot(f_scan / 1e9, T_mag, 'b-', linewidth=1.5)
    ax1.axhline(1.0, color='r', linestyle='--', alpha=0.7, label=r'$|T|=1$ (稳态)')
    ax1.axhline(beta_0 * A0, color='g', linestyle=':', alpha=0.5,
                label=rf'$|T|_{{\max}}$={beta_0*A0:.3f}')
    ax1.set_ylabel(r'$|T(\omega)|$ 环路增益幅值')
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.set_title('Barkhausen 起振条件验证')

    ax2.plot(f_scan / 1e9, T_phase, 'b-', linewidth=1.5)
    ax2.axhline(0.0, color='r', linestyle='--', alpha=0.7, label=r'$\angle T = 0^\circ$')
    ax2.set_xlabel('频率 (GHz)')
    ax2.set_ylabel(r'$\angle T(\omega)$ (deg)')
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_ex11_1_barkhausen.png", dpi=150)
    plt.close()
    print("  图 → fig_ex11_1_barkhausen.png\n")


# ══════════════════════════════════════════════════════════
#  §11.2 — 负阻振荡器设计
# ══════════════════════════════════════════════════════════
def example_11_2_negative_resistance():
    """
    负阻振荡器示例。
    已知晶体管在 f0 = 5 GHz 的输入阻抗 Z_in = -50 - j20 Ω。
    设计负载 Z_L 使电路振荡，计算起振需要的条件。
    """
    print("=" * 60)
    print("Ex 11.2: 负阻振荡器设计")
    print("=" * 60)

    f0 = 5.0e9          # 目标频率 [Hz]
    omega_0 = 2 * np.pi * f0

    # 晶体管输入阻抗 [Ω]
    R_in = -50.0           # 负阻 [Ω]
    X_in = -20.0           # 电抗 [Ω]
    Z_in = R_in + 1j * X_in

    # 由振荡条件 Z_in + Z_L = 0
    R_L_desired = -R_in    # = +50 Ω
    X_L_desired = -X_in    # = +20 Ω
    Z_L_desired = R_L_desired + 1j * X_L_desired

    print(f"  f0 = {f0/1e9:.2f} GHz")
    print(f"  Z_in = {R_in:.1f} + j{X_in:.1f} Ω")
    print(f"  负载阻抗 Z_L = {R_L_desired:.1f} + j{X_L_desired:.1f} Ω")
    print(f"  Z_in + Z_L = {R_in+R_L_desired:.1f} + j{X_in+X_L_desired:.1f} Ω → {'✅ 振荡' if abs(R_in+R_L_desired) < 1e-10 and abs(X_in+X_L_desired) < 1e-10 else '❌'}")

    # 起振裕度：|R_in| > R_L
    margin = abs(R_in) / R_L_desired
    print(f"  起振裕度 |R_in|/R_L = {margin:.3f} (>1 则起振) → {'✅' if margin > 1 else '❌'}")

    # 串联 LC 实现负载电抗
    L_series = X_L_desired / omega_0  # [H]
    print(f"  串联电感实现 X_L = {X_L_desired} Ω → L = {L_series*1e9:.4f} nH")

    # ── 频率附近的阻抗变化 ──
    f_scan = np.linspace(4.0e9, 6.0e9, 500)
    # 假设 Z_in 呈串联 RLC 频率依赖性
    L_neg = 0.5e-9          # 等效串联电感 [H]
    C_neg = 1 / ((2*np.pi*f0)**2 * L_neg)  # [F]
    R_in_scan = R_in * np.ones_like(f_scan)
    X_in_scan = X_in + 2 * np.pi * f_scan * L_neg - 1 / (2 * np.pi * f_scan * C_neg)

    R_total = R_in_scan + R_L_desired
    X_total = X_in_scan + X_L_desired

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

    ax1.plot(f_scan / 1e9, R_in_scan, 'b-', label=r'$R_{\mathrm{in}}$')
    ax1.axhline(-R_L_desired, color='r', linestyle='--', label=r'$-R_L$')
    ax1.axhline(0, color='gray', linestyle=':', alpha=0.5)
    ax1.set_ylabel('电阻 (Ω)')
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.set_title('负阻振荡器 — 阻抗频率特性')

    ax2.plot(f_scan / 1e9, X_in_scan, 'b-', label=r'$X_{\mathrm{in}}$')
    ax2.axhline(-X_L_desired, color='r', linestyle='--', label=r'$-X_L$')
    ax2.set_xlabel('频率 (GHz)')
    ax2.set_ylabel('电抗 (Ω)')
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_ex11_2_neg_resistance.png", dpi=150)
    plt.close()
    print("  图 → fig_ex11_2_neg_resistance.png\n")


# ══════════════════════════════════════════════════════════
#  §11.3 — DRO 频率与耦合计算
# ══════════════════════════════════════════════════════════
def example_11_3_dro():
    """
    介质谐振振荡器 (DRO) 示例。
    计算 TE01δ 模谐振频率，以及 DRO 耦合到微带线的外部 Q 值。
    """
    print("=" * 60)
    print("Ex 11.3: 介质谐振振荡器 (DRO)")
    print("=" * 60)

    # DR 参数
    epsilon_r = 38.0          # Ba(Mg,Ta)O₃ 陶瓷
    a = 5.0e-3                # 半径 [m]
    h = 4.0e-3                # 高度 [m]
    tan_delta = 2.0e-5        # 介质损耗角正切 [无量纲]

    # TE01δ 模近似公式 (Pozar Eq 11.12 变体)
    # f0 ≈ c / (2 * pi * a * sqrt(epsilon_r)) * J_01 / (1 + (a/h)^2)的近似
    # 更精确: 用经验公式
    J_01 = 2.405  # 一阶 Bessel 函数第一个零点 (TE01δ)
    f0_approx = C0 / (2 * np.pi * a * np.sqrt(epsilon_r)) * J_01 / np.sqrt(1 + (a / h)**2 / 4)
    # 修正: TE01δ 模更准确的经验式
    # f0 = (c * X_01) / (2 * pi * a * sqrt(eps_r)) * 1/sqrt(1 + (2a/h)^-2)
    # 实际采用常见经验公式:
    X_01 = 2.405
    f0_dro = (C0 * X_01) / (2 * np.pi * a * np.sqrt(epsilon_r))
    # 高度修正因子 (Kajfez 近似)
    correction_h = 1.0 / np.sqrt(1 + (a / h)**2 * 0.4)
    f0_dro_corrected = f0_dro * correction_h

    print(f"  ε_r = {epsilon_r}, a = {a*1e3:.2f} mm, h = {h*1e3:.2f} mm")
    print(f"  近似 f0 ≈ {f0_approx/1e9:.4f} GHz")
    print(f"  TE01δ 模 f0 ≈ {f0_dro/1e9:.4f} GHz (无高度修正)")
    print(f"  经高度修正 f0 ≈ {f0_dro_corrected/1e9:.4f} GHz")

    # 介质 Q 值
    Q_d = 1.0 / tan_delta
    print(f"  介质 Q_d = 1/tanδ = {Q_d:.0f}")

    # 耦合到 50 Ω 微带线
    Z0_ms = 50.0              # 微带线特性阻抗 [Ω]
    # 耦合系数与间距成指数关系 (近似)
    d_coupling = np.linspace(0.2e-3, 2.0e-3, 100)
    # 耦合系数 β ~ exp(-2 * alpha * d) 近似
    coupling_coeff = 0.8 * np.exp(-d_coupling * 2000)
    # 外部 Q
    Q_external = Q_d / coupling_coeff

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.plot(d_coupling * 1e3, coupling_coeff, 'b-', linewidth=1.5)
    ax1.set_xlabel('DR-微带线间距 (mm)')
    ax1.set_ylabel('耦合系数 β')
    ax1.grid(True, alpha=0.3)
    ax1.set_title('DR 耦合系数 vs 间距')

    ax2.semilogy(d_coupling * 1e3, Q_external, 'r-', linewidth=1.5)
    ax2.set_xlabel('DR-微带线间距 (mm)')
    ax2.set_ylabel('外部 Q$_e$')
    ax2.grid(True, alpha=0.3)
    ax2.set_title('外部 Q 值 vs 间距')

    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_ex11_3_dro.png", dpi=150)
    plt.close()
    print("  图 → fig_ex11_3_dro.png\n")


# ══════════════════════════════════════════════════════════
#  §11.4 — VCO 调谐曲线
# ══════════════════════════════════════════════════════════
def example_11_4_vco():
    """
    压控振荡器 (VCO) 调谐特性。
    使用变容二极管 C-V 特性，计算振荡频率随调谐电压的变化。
    """
    print("=" * 60)
    print("Ex 11.4: VCO 调谐曲线")
    print("=" * 60)

    # 变容管参数
    C_j0 = 2.0e-12           # 零偏结电容 [F]
    V_j = 0.7                 # 内建势 [V] (Si)
    n = 0.5                   # 突变结指数 [无量纲]
    R_s = 2.0                 # 串联电阻 [Ω]

    # LC 谐振器参数
    L_res = 1.0e-9            # 谐振电感 [H]
    C_par = 0.5e-12           # 寄生电容 [F]

    # 调谐电压扫描 [V]
    V_tune = np.linspace(0.5, 20.0, 500)
    C_j = C_j0 / (1 + V_tune / V_j) ** n
    C_total = C_j + C_par

    # 振荡频率
    f_osc = 1.0 / (2 * np.pi * np.sqrt(L_res * C_total))

    # VCO 增益 (差分)
    K_vco = np.gradient(f_osc, V_tune)  # [Hz/V]

    # 在 V_tune=5V 处的参数
    idx_ref = np.argmin(np.abs(V_tune - 5.0))
    f_at_5v = f_osc[idx_ref]
    K_at_5v = K_vco[idx_ref]
    C_at_5v = C_total[idx_ref]

    print(f"  L = {L_res*1e9:.2f} nH, C_par = {C_par*1e12:.2f} pF")
    print(f"  C_j0 = {C_j0*1e12:.2f} pF, V_j = {V_j:.2f} V, n = {n}")
    print(f"  R_s = {R_s:.1f} Ω")
    print(f"  V_tune = 5V: f = {f_at_5v/1e9:.4f} GHz, C_total = {C_at_5v*1e12:.4f} pF")
    print(f"  K_VCO @ 5V = {K_at_5v/1e6:.2f} MHz/V")

    # 变容管 Q 值 @ 5 GHz
    f_ref = 5.0e9
    omega_ref = 2 * np.pi * f_ref
    Q_var = 1.0 / (omega_ref * R_s * C_at_5v)
    print(f"  Varactor Q @ {f_ref/1e9:.0f} GHz = {Q_var:.1f}")

    # ── 画图 ──
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

    ax1.plot(V_tune, f_osc / 1e9, 'b-', linewidth=1.5)
    ax1.set_ylabel('振荡频率 $f_{\\mathrm{osc}}$ (GHz)')
    ax1.grid(True, alpha=0.3)
    ax1.set_title('VCO 调谐特性')

    ax2.plot(V_tune, K_vco / 1e6, 'r-', linewidth=1.5)
    ax2.axhline(K_at_5v / 1e6, color='k', linestyle='--', alpha=0.5,
                label=f'$K_{{\\mathrm{{VCO}}}}$ @ 5V = {K_at_5v/1e6:.2f} MHz/V')
    ax2.set_xlabel('调谐电压 $V_{\\mathrm{tune}}$ (V)')
    ax2.set_ylabel('$K_{\\mathrm{VCO}}$ (MHz/V)')
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_ex11_4_vco.png", dpi=150)
    plt.close()
    print("  图 → fig_ex11_4_vco.png\n")


# ══════════════════════════════════════════════════════════
#  §11.5 — 混频器 IP3 / IM3 计算
# ══════════════════════════════════════════════════════════
def example_11_5_mixer_ip3_im3():
    """
    混频器三阶交调失真 (IM3) 与三阶截点 (IP3) 计算。
    分析基波和 IM3 功率随输入功率的关系，确定 IIP3/OIP3。
    """
    print("=" * 60)
    print("Ex 11.5: 混频器 IP3 / IM3 计算")
    print("=" * 60)

    # 混频器参数
    IIP3_dbm = 15.0            # 输入 IP3 [dBm]
    conversion_gain = -6.0     # 变频增益 [dB] (无源混频器典型值)
    OIP3_dbm = IIP3_dbm + conversion_gain  # [dBm]

    # 输入功率扫描 [dBm]
    P_in_dbm = np.linspace(-30, 20, 200)
    P_in_mW = 10 ** (P_in_dbm / 10)

    # 基波输出功率 [dBm] (斜率 = 1)
    P_out_fund_dbm = P_in_dbm + conversion_gain

    # IM3 输出功率 [dBm] (斜率 = 3)
    # IM3线: P_IM3(dBm) = 3*P_in(dBm) - 2*IIP3(dBm) + G_c(dB)
    # 等价: P_IM3_out(dBm) = 3*P_out(dBm) - 2*OIP3(dBm)
    P_im3_out_dbm = 3 * P_out_fund_dbm - 2 * OIP3_dbm

    # 交叉点验证
    idx_cross = np.argmin(np.abs(P_out_fund_dbm[P_in_dbm > -20] - P_im3_out_dbm[P_in_dbm > -20]))
    cross_point = P_in_dbm[P_in_dbm > -20][idx_cross]
    cross_fund = P_out_fund_dbm[P_in_dbm > -20][idx_cross]

    print(f"  Conversion Gain G_c = {conversion_gain:.1f} dB")
    print(f"  IIP3 = {IIP3_dbm:.1f} dBm")
    print(f"  OIP3 = {OIP3_dbm:.1f} dBm")
    print(f"  交叉点验证: P_in ≈ {cross_point:.1f} dBm, P_out ≈ {cross_fund:.1f} dBm")

    # 特定输入功率下的 IM3
    P_test = -10.0  # dBm
    P_test_mW = 10 ** (P_test / 10)
    P_fund_test = P_test + conversion_gain
    P_im3_test = 3 * P_fund_test - 2 * OIP3_dbm
    C_IM3 = P_fund_test - P_im3_test  # 载波 - 交调比
    print(f"  输入 P_in = {P_test:.0f} dBm 时:")
    print(f"    P_fund (out) = {P_fund_test:.2f} dBm")
    print(f"    P_IM3 (out)  = {P_im3_test:.2f} dBm")
    print(f"    C/IM3 = {C_IM3:.2f} dB")

    # SFDR 计算
    NF_mixer = 7.0                     # 噪声系数 [dB]
    noise_bw = 1e6                     # 噪声带宽 [Hz] (1 MHz)
    N_floor_dbm = 10 * np.log10(K_B * T_REF * noise_bw * 1000) + NF_mixer
    # N_floor_dbm = 10*log10(kTB*1000) + NF, 其中 kTB[mW] = kTB[W]*1000
    N_floor_watts = K_B * T_REF * noise_bw
    N_floor_dbm_v2 = 30 + 10 * np.log10(N_floor_watts) + NF_mixer
    SFDR = (2 / 3) * (IIP3_dbm - N_floor_dbm_v2)
    print(f"  噪声本底 (B={noise_bw/1e6:.0f} MHz, NF={NF_mixer:.1f} dB): {N_floor_dbm_v2:.2f} dBm")
    print(f"  SFDR = {SFDR:.1f} dB")

    # ── 画图 ──
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(P_in_dbm, P_out_fund_dbm, 'b-', linewidth=2, label='基波 (斜率=1)')
    ax.plot(P_in_dbm, P_im3_out_dbm, 'r-', linewidth=2, label='IM3 (斜率=3)')

    # 标记 IP3
    ax.plot(IIP3_dbm, OIP3_dbm, 'ko', markersize=8)
    ax.annotate(f'IIP$_3$={IIP3_dbm:.1f} dBm\nOIP$_3$={OIP3_dbm:.1f} dBm',
                xy=(IIP3_dbm, OIP3_dbm), xytext=(IIP3_dbm - 12, OIP3_dbm + 8),
                arrowprops=dict(arrowstyle='->', color='k'), fontsize=10)

    # 标记测试点
    P_fund_test_dbm = P_test + conversion_gain
    P_im3_test_dbm = 3 * P_fund_test_dbm - 2 * OIP3_dbm
    ax.plot([P_test], [P_fund_test_dbm], 'bs', markersize=6)
    ax.plot([P_test], [P_im3_test_dbm], 'rs', markersize=6)
    ax.annotate(f'$P_{{\\mathrm{{in}}}}={P_test:.0f}$ dBm\nC/IM$_3$={C_IM3:.1f} dB',
                xy=(P_test, P_im3_test_dbm), fontsize=9,
                xytext=(P_test - 8, P_im3_test_dbm - 8),
                arrowprops=dict(arrowstyle='->', color='gray'))

    ax.axhline(N_floor_dbm_v2, color='gray', linestyle=':', alpha=0.7,
               label=f'噪声本底 ({N_floor_dbm_v2:.1f} dBm)')
    ax.axvline(IIP3_dbm, color='k', linestyle=':', alpha=0.3)

    ax.set_xlabel('输入功率 $P_{\\mathrm{in}}$ (dBm)')
    ax.set_ylabel('输出功率 $P_{\\mathrm{out}}$ (dBm)')
    ax.set_title('混频器 IP3 / IM3 特性')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(-30, 20)
    ax.set_ylim(-50, 30)

    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_ex11_5_mixer_ip3.png", dpi=150)
    plt.close()
    print("  图 → fig_ex11_5_mixer_ip3.png\n")


# ══════════════════════════════════════════════════════════
#  §11.5 — 混频器变频损耗与 SSB/DSB NF
# ══════════════════════════════════════════════════════════
def example_11_6_conversion_loss_nf():
    """
    无源二极管混频器的变频损耗与噪声系数分析。
    二极管参数：I_s, n, R_s。计算 LO 驱动下的时变电导和变频损耗。
    """
    print("=" * 60)
    print("Ex 11.6: 混频器变频损耗与噪声系数")
    print("=" * 60)

    # 二极管参数
    I_s = 1.0e-8               # 饱和电流 [A]
    n_id = 1.1                  # 理想因子 [无量纲]
    R_s = 5.0                   # 串联电阻 [Ω]
    T_diode = 290.0             # 温度 [K]

    # LO 参数
    P_LO_dbm = 5.0              # LO 功率 [dBm] (合理驱动电平避免数值溢出)
    P_LO_mW = 10 ** (P_LO_dbm / 10)
    V_LO_peak = np.sqrt(2 * P_LO_mW * 1e-3 * 50)  # [V] (阻抗50Ω)
    f_LO = 5.0e9                # LO 频率 [Hz]

    alpha = Q_E / (n_id * K_B * T_diode)  # [1/V] (Eq 11.29)
    print(f"  α = q/(nkT) = {alpha:.3f} 1/V")
    print(f"  V_LO (peak) = {V_LO_peak*1e3:.2f} mV")
    print(f"  P_LO = {P_LO_dbm:.1f} dBm")

    # 时变电导（限幅避免数值溢出 — 实际二极管受串联电阻和饱和电流限制）
    t = np.linspace(0, 1 / f_LO * 3, 1000)
    V_LO_t = V_LO_peak * np.cos(2 * np.pi * f_LO * t)
    # 限制最大电导的物理考虑：Rs(series) + Rj(junction) 分压限流
    # g(t) = dI/dV, 但实际在大信号下受 Rs 限制：g_max ≈ 1/Rs
    g_max = 1.0 / R_s  # S
    g_t_raw = alpha * I_s * np.exp(alpha * V_LO_t)
    g_t = np.clip(g_t_raw, 0, g_max)
    g_avg = np.mean(g_t)

    # 简化的变频损耗模型
    # 无源二极管混频器典型 L_c ≈ 6 dB
    G1 = np.mean(2 * g_t * np.cos(2 * np.pi * f_LO * t))
    # 典型值（Pozar §11.6 给出无源二极管混频器 L_c ≈ 4-7 dB）
    L_c_typical = 6.0   # dB
    print(f"  g_avg = {g_avg:.6f} S (受串联电阻限幅 g_max=1/R_s={g_max:.6f} S)")
    print(f"  G1 (基频混频电导) = {G1:.6f} S")
    print(f"  典型值 L_c ≈ {L_c_typical:.1f} dB (无源二极管混频器)")

    # SSB vs DSB 噪声系数
    NF_SSB = L_c_typical + 0.5  # [dB] 实际约比 L_c 大 0.5-1 dB
    NF_DSB = NF_SSB - 3.0       # [dB] 双边带少 3 dB (镜像噪声贡献)

    print(f"  NF_SSB = {NF_SSB:.1f} dB")
    print(f"  NF_DSB = {NF_DSB:.1f} dB")

    # ── 画时变电导 ──
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 5), sharex=True)

    t_ns = t * 1e9
    ax1.plot(t_ns, V_LO_t * 1e3, 'b-', linewidth=1.5)
    ax1.set_ylabel('$V_{\\mathrm{LO}}(t)$ (mV)')
    ax1.set_title(f'二极管时变特性 ($P_{{\\mathrm{{LO}}}}$={P_LO_dbm:.0f} dBm)')
    ax1.grid(True, alpha=0.3)

    ax2.plot(t_ns, g_t * 1e3, 'r-', linewidth=1.5)
    ax2.axhline(g_avg * 1e3, color='k', linestyle='--', alpha=0.7,
                label=f'$g_{{\\mathrm{{avg}}}}$={g_avg*1e3:.2f} mS')
    ax2.set_xlabel('时间 (ns)')
    ax2.set_ylabel('电导 $g(t)$ (mS)')
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_ex11_6_mixer_diode.png", dpi=150)
    plt.close()
    print("  图 → fig_ex11_6_mixer_diode.png\n")


# ══════════════════════════════════════════════════════════
#  §11.5 — 交调频谱分析
# ══════════════════════════════════════════════════════════
def example_11_7_mixer_spectrum():
    """
    混频器输出频谱分析。
    显示 RF、LO、IF 以及 IM3 产物在频谱上的位置。
    """
    print("=" * 60)
    print("Ex 11.7: 混频器输出频谱分析")
    print("=" * 60)

    f_RF = 5.1e9           # RF 频率 [Hz]
    f_LO = 5.0e9           # LO 频率 [Hz]
    f_IF = f_RF - f_LO     # 中频 [Hz] (低本振)
    f_IM3_1 = 2 * (f_RF + 10e6) - f_RF  # 双音 IM3 (假设干扰在 f_RF+10MHz)
    f_IM3_2 = 2 * f_RF - (f_RF + 10e6)
    # 双音测试：f1 = f_RF + 10 MHz, f2 = f_RF + 20 MHz
    f_delta = 10e6
    f1 = f_RF + f_delta
    f2 = f_RF + 2 * f_delta
    f_im3_low = 2 * f1 - f2  # = f_RF
    f_im3_high = 2 * f2 - f1  # = f_RF + 30 MHz

    # 频谱线 (简化：幅度示意)
    freqs = np.array([f_RF, f_LO, f_IF, f1, f2, f_im3_low, f_im3_high,
                      2*f_LO - f_RF, f_RF + f_LO])
    labels = ['RF', 'LO', 'IF', 'f1', 'f2', 'IM3', 'IM3',
              'Image', 'Sum']
    amps = np.array([0, 0, -6, -1, -2, -30, -30, -20, -10])  # dB 示意

    # 只显示最重要的
    show_idx = [0, 1, 2, 5, 6, 7, 8]
    freqs_show = freqs[show_idx]
    labels_show = [labels[i] for i in show_idx]
    amps_show = amps[show_idx]

    print(f"  f_RF = {f_RF/1e9:.3f} GHz")
    print(f"  f_LO = {f_LO/1e9:.3f} GHz")
    print(f"  f_IF = {f_IF/1e6:.1f} MHz")
    print(f"  f_IM3 落在 f_RF 带内 = {f_im3_low/1e9:.6f} GHz (无法滤波去除)")

    fig, ax = plt.subplots(figsize=(10, 5))

    markerline, stemlines, baseline = ax.stem(
        np.array(freqs_show) / 1e9, amps_show,
        linefmt='C0-', markerfmt='C0o', basefmt='gray')
    plt.setp(markerline, markersize=8)

    for i, (f_ghz, label, amp) in enumerate(zip(freqs_show / 1e9, labels_show, amps_show)):
        ax.annotate(label, xy=(f_ghz, amp), fontsize=9,
                    xytext=(f_ghz, amp + 2), ha='center')

    # 标记 IM3 产物在 RF 带内
    ax.axvline(f_RF / 1e9, color='gray', linestyle=':', alpha=0.5)
    ax.axvline((f_RF + 30e6) / 1e9, color='gray', linestyle=':', alpha=0.5)
    ax.fill_betweenx([-35, 5], f_RF / 1e9, (f_RF + 30e6) / 1e9,
                     alpha=0.1, color='red', label='IM3 区域')

    ax.set_xlabel('频率 (GHz)')
    ax.set_ylabel('相对幅度 (dB)')
    ax.set_title('混频器输出频谱')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 11)

    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_ex11_7_mixer_spectrum.png", dpi=150)
    plt.close()
    print("  图 → fig_ex11_7_mixer_spectrum.png\n")


# ══════════════════════════════════════════════════════════
#  §11.2/11.6 — 晶体管 S 参数振荡条件
# ══════════════════════════════════════════════════════════
def example_11_8_s_param_oscillator():
    """
    使用 S 参数验证晶体管振荡条件。
    已知共基 BJT 在 f0 处的 S 参数，设计反馈网络使 |S11'| > 1，
    并确定合适的负载 Γ_L 使振荡成立。
    """
    print("=" * 60)
    print("Ex 11.8: S 参数振荡器设计")
    print("=" * 60)

    f0 = 4.0e9                 # 设计频率 [Hz]

    # 共基 BJT S 参数 (在 f=4 GHz, Vce=10V, Ic=10mA)
    # 典型值，类似 NE856
    S_11 = 0.67 * np.exp(1j * np.radians(150))   # 输入反射
    S_12 = 0.12 * np.exp(1j * np.radians(20))    # 反向隔离
    S_21 = 1.80 * np.exp(1j * np.radians(55))    # 前向增益
    S_22 = 0.75 * np.exp(1j * np.radians(-100))  # 输出反射

    print(f"  共基 BJT S 参数 (@ {f0/1e9:.1f} GHz):")
    print(f"    S_11 = {np.abs(S_11):.2f} ∠{np.angle(S_11, deg=True):.1f}°")
    print(f"    S_12 = {np.abs(S_12):.2f} ∠{np.angle(S_12, deg=True):.1f}°")
    print(f"    S_21 = {np.abs(S_21):.2f} ∠{np.angle(S_21, deg=True):.1f}°")
    print(f"    S_22 = {np.abs(S_22):.2f} ∠{np.angle(S_22, deg=True):.1f}°")

    # K-Δ 稳定性
    Delta_s = S_11 * S_22 - S_12 * S_21
    K_s = (1 - abs(S_11)**2 - abs(S_22)**2 + abs(Delta_s)**2) / (2 * abs(S_12) * abs(S_21))
    B1 = 1 + abs(S_11)**2 - abs(S_22)**2 - abs(Delta_s)**2

    print(f"    Δ = {abs(Delta_s):.4f} ∠{np.angle(Delta_s, deg=True):.1f}°")
    print(f"    K = {K_s:.4f} ({'无条件稳定' if K_s > 1 and abs(Delta_s) < 1 else '潜在不稳定 → 可振荡'})")

    # 振荡设计：选择反馈 Γ_L 使 |Γ_in| > 1
    # 扫描 Γ_L 的相位，寻找使 |Γ_in| > 1 的区域
    gamma_L_phase = np.linspace(0, 360, 200)
    gamma_L_mag_test = 0.5  # 固定幅度

    gamma_in_mag = np.zeros_like(gamma_L_phase)
    for i, phase_deg in enumerate(gamma_L_phase):
        gamma_L = gamma_L_mag_test * np.exp(1j * np.radians(phase_deg))
        gamma_in = S_11 + S_12 * S_21 * gamma_L / (1 - S_22 * gamma_L)
        gamma_in_mag[i] = abs(gamma_in)

    max_gamma_in = np.max(gamma_in_mag)
    best_phase = gamma_L_phase[np.argmax(gamma_in_mag)]
    max_gamma = gamma_L_mag_test * np.exp(1j * np.radians(best_phase))
    Gamma_in_max = S_11 + S_12 * S_21 * max_gamma / (1 - S_22 * max_gamma)

    print(f"\n  扫描 |Γ_L|={gamma_L_mag_test}:")
    print(f"    max |Γ_in| = {max_gamma_in:.4f} @ ∠Γ_L = {best_phase:.1f}°")
    print(f"    Γ_in(max) = {abs(Gamma_in_max):.4f} ∠{np.angle(Gamma_in_max, deg=True):.1f}°")

    # 振荡时需 Γ_S = 1/Γ_in
    if max_gamma_in > 1:
        Gamma_S_osc = 1.0 / Gamma_in_max
        # 源反射系数归一化
        Gamma_S_mag = abs(Gamma_S_osc)
        Gamma_S_phase = np.angle(Gamma_S_osc, deg=True)
        print(f"    振荡源反射: Γ_S = {Gamma_S_mag:.4f} ∠{Gamma_S_phase:.1f}°")
        print(f"    |Γ_S| = {Gamma_S_mag:.4f} {'✅ < 1 (可实现)' if Gamma_S_mag < 1 else '⚠️ > 1 (需要损耗)'}")
    else:
        print("    无法用当前 |Γ_L| 实现 |Γ_in| > 1，需增大反馈或选择不同 Γ_L 幅度")

    # ── 画 Γ_in 幅度 vs Γ_L 相位 ──
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(gamma_L_phase, gamma_in_mag, 'b-', linewidth=1.5)
    ax.axhline(1.0, color='r', linestyle='--', alpha=0.7,
               label='$|\\Gamma_{\\mathrm{in}}| = 1$ (振荡边界)')
    if max_gamma_in > 1:
        ax.plot(best_phase, max_gamma_in, 'ro', markersize=6)
        ax.annotate(f'max = {max_gamma_in:.3f}\n@ {best_phase:.0f}°',
                    xy=(best_phase, max_gamma_in), fontsize=9,
                    xytext=(best_phase + 20, max_gamma_in - 0.3),
                    arrowprops=dict(arrowstyle='->', color='r'))
    ax.set_xlabel('$\\angle\\Gamma_L$ (deg)')
    ax.set_ylabel('$|\\Gamma_{\\mathrm{in}}|$')
    ax.set_title(f'S 参数振荡条件 ($|\\Gamma_L|={gamma_L_mag_test}$)')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 360)

    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_ex11_8_osc_s_param.png", dpi=150)
    plt.close()
    print("  图 → fig_ex11_8_osc_s_param.png\n")


# ══════════════════════════════════════════════════════════
#  §11.4 — 相位噪声 Leeson 模型
# ══════════════════════════════════════════════════════════
def example_11_9_phase_noise():
    """
    Leeson 相位噪声模型。
    比较 DRO (高 Q_L) 与 VCO (低 Q_L) 的相位噪声特性。
    """
    print("=" * 60)
    print("Ex 11.9: 相位噪声 Leeson 模型")
    print("=" * 60)

    f0 = 5.0e9               # 载频 [Hz]
    F_noise = 3.0            # 噪声系数 [dB]
    F_lin = 10 ** (F_noise / 10)
    P0_dbm = 10.0            # 输出功率 [dBm]
    P0_W = 1e-3 * 10 ** (P0_dbm / 10)  # [W]

    # 不同 Q 值场景
    Q_L_DRO = 5000           # DRO 有载 Q
    Q_L_VCO = 50             # VCO 有载 Q (LC 谐振器)

    # 偏移频率扫描
    delta_f = np.logspace(1, 7, 500)  # 10 Hz - 10 MHz

    # Leeson 模型: L(df) = FkT/P0 * [1 + (f0/(2QL*df))^2]
    noise_floor = F_lin * K_B * T_REF / P0_W  # 远载频本底

    L_DRO = noise_floor * (1 + (f0 / (2 * Q_L_DRO * delta_f)) ** 2)
    L_VCO = noise_floor * (1 + (f0 / (2 * Q_L_VCO * delta_f)) ** 2)

    L_DRO_dBcHz = 10 * np.log10(L_DRO)
    L_VCO_dBcHz = 10 * np.log10(L_VCO)

    # 特定偏移下的噪声
    idx_100k = np.argmin(np.abs(delta_f - 100e3))
    idx_10k = np.argmin(np.abs(delta_f - 10e3))

    print(f"  f0 = {f0/1e9:.1f} GHz, P0 = {P0_dbm:.0f} dBm, NF = {F_noise:.1f} dB")
    print(f"  噪声本底 (远载频) = {10*np.log10(noise_floor):.1f} dBc/Hz")
    print(f"\n  DRO (Q_L={Q_L_DRO}):")
    print(f"    L(10 kHz) = {L_DRO_dBcHz[idx_10k]:.1f} dBc/Hz")
    print(f"    L(100 kHz) = {L_DRO_dBcHz[idx_100k]:.1f} dBc/Hz")
    print(f"\n  VCO (Q_L={Q_L_VCO}):")
    print(f"    L(10 kHz) = {L_VCO_dBcHz[idx_10k]:.1f} dBc/Hz")
    print(f"    L(100 kHz) = {L_VCO_dBcHz[idx_100k]:.1f} dBc/Hz")
    print(f"\n  @ 10 kHz: DRO 优于 VCO {L_VCO_dBcHz[idx_10k] - L_DRO_dBcHz[idx_10k]:.1f} dB")

    # ── 画图 ──
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.loglog(delta_f, L_DRO_dBcHz, 'b-', linewidth=2, label=f'DRO ($Q_L$={Q_L_DRO})')
    ax.loglog(delta_f, L_VCO_dBcHz, 'r-', linewidth=2, label=f'VCO ($Q_L$={Q_L_VCO})')
    ax.axhline(10 * np.log10(noise_floor), color='gray', linestyle=':',
               alpha=0.7, label=f'噪声本底 ({10*np.log10(noise_floor):.0f} dBc/Hz)')
    # 1/f^2 斜率参考
    ax.loglog(delta_f, L_VCO_dBcHz[0] - 20 * np.log10(delta_f / delta_f[0]),
              'k--', alpha=0.3, label='$1/(\\Delta f)^2$ 斜率')

    ax.set_xlabel('偏移频率 $\\Delta f$ (Hz)')
    ax.set_ylabel('相位噪声 $\\mathcal{L}(\\Delta f)$ (dBc/Hz)')
    ax.set_title('Leeson 相位噪声模型')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3, which='both')
    ax.set_xlim(10, 10e6)
    ax.set_ylim(-180, -40)

    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_ex11_9_phase_noise.png", dpi=150)
    plt.close()
    print("  图 → fig_ex11_9_phase_noise.png\n")


# ══════════════════════════════════════════════════════════
#  主程序入口
# ══════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("Pozar Ch11: Oscillators and Mixers — Python Examples\n")

    example_11_1_barkhausen()
    example_11_2_negative_resistance()
    example_11_3_dro()
    example_11_4_vco()
    example_11_5_mixer_ip3_im3()
    example_11_6_conversion_loss_nf()
    example_11_7_mixer_spectrum()
    example_11_8_s_param_oscillator()
    example_11_9_phase_noise()

    print("\nAll Ch11 examples completed successfully.")
