#!/usr/bin/env python3
"""
Collins Ch.6 — Passive Microwave Devices 示例代码
================================================
涵盖：Magic-T, Bethe 小孔耦合, 多孔耦合器方向性,
Polder 张量 + Faraday 旋转角, 结环行器 S 参数, YIG 调谐频率

物理量命名遵循 Collins 惯例：
    epsilon_r, mu_r, sigma, mu_0, eta_0, k_0, Polder, Beta, Gamma
"""

import numpy as np

# ─────────────── 物理常数 ───────────────
c = 299_792_458           # m/s
mu_0 = 4 * np.pi * 1e-7   # H/m
epsilon_0 = 1 / (mu_0 * c ** 2)  # F/m ≈ 8.854e-12
eta_0 = np.sqrt(mu_0 / epsilon_0)  # ≈ 376.73 Ω
gamma_e = 1.759e11        # 电子旋磁比 rad/(s·T)

# ──────────────────────────────────────────────
# §6.2.3 — Magic-T S 参数矩阵
# ──────────────────────────────────────────────
def magic_t_s_matrix():
    """
    理想 Magic-T S 参数矩阵 (Collin §6.2.3, p. 395)
    端口定义: 1=H臂(Σ), 2=E臂(Δ), 3,4=共线臂
    """
    S = (1 / np.sqrt(2)) * np.array([
        [0, 0,  1,  1],
        [0, 0,  1, -1],
        [1, 1,  0,  0],
        [1, -1, 0,  0],
    ])
    return S


# ──────────────────────────────────────────────
# §6.4.2 — Bethe 小孔耦合系数
# ──────────────────────────────────────────────
def bethe_hole_coupling(r=2e-3, freq=10e9, x_offset=None):
    """
    Bethe 小孔耦合系数 (Collin §6.4.2)

    基于 Collin 的 Bethe 小孔理论，计算波导公共壁小圆孔的耦合度。
    耦合系数通过归一化 TE10 模的等效电压 / 电流表示。

    参数
    ----------
    r : float
        圆孔半径 [m]
    freq : float
        工作频率 [Hz]
    x_offset : float or None
        孔中心距波导侧壁偏移 [m]；None 表示宽边中心 (a/2)

    返回
    --------
    dict
    """
    # 标准 X 波段波导 WR-90: a = 22.86 mm, b = 10.16 mm
    a = 22.86e-3
    b = 10.16e-3

    omega = 2 * np.pi * freq
    k0 = omega / c

    # TE10 模截止波数
    kc = np.pi / a
    if k0 <= kc:
        raise ValueError(f"f={freq/1e9:.1f} GHz 低于 WR-90 截止频率 (~6.56 GHz)")
    kz = np.sqrt(k0 ** 2 - kc ** 2)
    lambda_g = 2 * np.pi / kz

    # Bethe 小孔极化率 (圆孔)
    alpha_e = (2 / 3) * r ** 3
    alpha_m = (4 / 3) * r ** 3

    if x_offset is None:
        x_offset = a / 2

    # TE10 模归一化等效电压幅值 (V0=1)
    V0 = 1.0
    # 等效特性阻抗 (TE10 波阻抗 * b/a 几何因子)
    Z_TE10 = (kz / k0) * eta_0
    Z0_wg = Z_TE10 * (2 * b / a)  # 电压-电流定义阻抗

    # 横向场 (TE10, 归一化)
    # Ey = V0 * sqrt(2/(a*b)) * sin(pi*x/a) * e^{-j*kz*z}  [V/m] 功率归一化
    # Hx = -Ey / Z_TE10
    # Hz = j * (pi/(a*kz)) * V0 * sqrt(2/(a*b)) * cos(pi*x/a) * e^{-j*kz*z}

    norm_field = np.sqrt(2.0 / (a * b))

    E_y = V0 * norm_field * np.sin(np.pi * x_offset / a)
    H_x = -E_y / Z_TE10
    H_z = 1j * (np.pi / (a * kz)) * V0 * norm_field * np.cos(np.pi * x_offset / a)

    # Bethe 耦合幅值 (Collin eq. 6.69) — 含正负号干涉
    #
    # 电偶极矩: p = ε₀αₑ E_y ŷ → 在正反向激励同相等幅
    # 磁偶极矩: m = αₘ H_x x̂ → 在正反向激励符号相反
    #
    # 正向 (port 4): A_fwd ∝ ε₀αₑ|E_y|² + μ₀αₘ|H_x|²  (同号相加)
    # 反向 (port 3): A_rev ∝ ε₀αₑ|E_y|² - μ₀αₘ|H_x|²  (异号相消)
    #
    # 当磁偶极项占优时 (如孔在宽边中心 H_x 大):
    #   反向相消 → 正向优势 → 正向定向耦合器
    # 当磁偶极项较弱时 (孔靠近侧壁 H_x→0):
    #   正反向趋于对称 → 方向性降低

    A_fwd = (epsilon_0 * alpha_e * abs(E_y)**2
             + mu_0 * alpha_m * abs(H_x)**2)
    A_rev = (epsilon_0 * alpha_e * abs(E_y)**2
             - mu_0 * alpha_m * abs(H_x)**2)

    # 反向幅值可能相消为负值，取绝对值
    S13_amplitude = abs(omega * A_rev / 2.0)  # 反向耦合
    S14_amplitude = abs(omega * A_fwd / 2.0)  # 正向耦合

    coupling_dB = -20 * np.log10(max(abs(S13_amplitude), 1e-15))
    directivity_dB = 20 * np.log10(abs(S14_amplitude) / max(abs(S13_amplitude), 1e-15))

    return {
        "coupling_dB": coupling_dB,
        "directivity_dB": directivity_dB,
        "alpha_e": alpha_e,
        "alpha_m": alpha_m,
        "lambda_g": lambda_g,
        "r": r,
        "freq_GHz": freq / 1e9,
        "x_offset_mm": x_offset * 1e3,
    }


# ──────────────────────────────────────────────
# §6.4.3 — 多孔定向耦合器方向性
# ──────────────────────────────────────────────
def multi_hole_coupler_directivity(n_holes=4, freq=10e9, f0=10e9):
    """
    多孔定向耦合器方向性 (Collin §6.4.3)

    N 个等间距 λ_g0/4 小孔，位于波导公共宽壁。
    端口定义:
      Port 1 — 主波导入射 (z=0)
      Port 2 — 主波导直通 (z=L)
      Port 3 — 副波导背面 (z=0) "反向耦合端口"
      Port 4 — 副波导远端 (z=L) "正向耦合端口"

    物理: 反向耦合波路径差 2βd = π → 对偶数孔相消，
          正向耦合波相位相同 → 总加强。

    Parameters
    ----------
    n_holes : int
        孔数 (推荐偶数)
    freq : float
        工作频率 [Hz]
    f0 : float
        设计中心频率 [Hz]

    Returns
    --------
    dict
    """
    a = 22.86e-3
    kc = np.pi / a

    omega = 2 * np.pi * freq
    omega_0 = 2 * np.pi * f0
    k0 = omega / c
    k0_0 = omega_0 / c

    if k0 <= kc or k0_0 <= kc:
        raise ValueError("频率低于截止")

    kz = np.sqrt(k0 ** 2 - kc ** 2)
    kz_0 = np.sqrt(k0_0 ** 2 - kc ** 2)
    lambda_g = 2 * np.pi / kz
    lambda_g0 = 2 * np.pi / kz_0

    # 孔间距 = λ_g0/4
    d = lambda_g0 / 4
    beta = 2 * np.pi / lambda_g

    # 反向耦合波 (Port 3) 的阵列因子
    # 路径: 主路 i*d + 副路回到 z=0 i*d = 2*i*d
    i_idx = np.arange(n_holes)
    A_rev = np.sum(np.exp(-1j * 2 * beta * d * i_idx))

    # 正向耦合波 (Port 4) 的阵列因子
    # 路径: 主路 i*d + 副路到 z=L (N-1-i)*d = (N-1)*d (常数)
    A_fwd = n_holes * np.exp(-1j * beta * (n_holes - 1) * d)

    # 归一化阵列因子
    S13 = A_rev / n_holes  # 反向耦合系数
    S14 = A_fwd / n_holes  # 正向耦合系数

    coupling_to_port3_dB = -20 * np.log10(max(abs(S13), 1e-15))
    coupling_to_port4_dB = -20 * np.log10(max(abs(S14), 1e-15))
    directivity_dB = 20 * np.log10(abs(S14) / max(abs(S13), 1e-15))

    return {
        "n_holes": n_holes,
        "freq_GHz": freq / 1e9,
        "f0_GHz": f0 / 1e9,
        "S13_rev": S13,
        "S14_fwd": S14,
        "directivity_dB": directivity_dB,
        "coupling_port3_dB": coupling_to_port3_dB,
        "coupling_port4_dB": coupling_to_port4_dB,
        "d_mm": d * 1e3,
    }


# ──────────────────────────────────────────────
# §6.5.1 — Polder 张量
# ──────────────────────────────────────────────
def polder_tensor(H0=2000, Ms=1750, freq=10e9):
    """
    Polder 磁导率张量 (Collin §6.5.1, eq. 6.101)

    参数
    ----------
    H0 : float
        偏置磁场 [Oe] (1 Oe = 1000/(4π) A/m ≈ 79.577 A/m)
    Ms : float
        饱和磁化强度 [G] (1 G = 1000/(4π) A/m)
    freq : float
        工作频率 [Hz]

    返回
    --------
    mu_tensor : (3,3) ndarray
        Polder 张量 [H/m]
    mu_eff : float
        等效标量磁导率
    mu_plus, mu_minus : float
        右旋/左旋圆极化波磁导率
    """
    # 单位转换: Oe → A/m, G → A/m
    H0_Apm = H0 * 1000 / (4 * np.pi)  # 1 Oe = 1000/(4π) A/m
    Ms_Apm = Ms * 1000 / (4 * np.pi)

    omega = 2 * np.pi * freq
    omega_0 = gamma_e * mu_0 * H0_Apm      # 拉莫尔频率
    omega_m = gamma_e * mu_0 * Ms_Apm       # 磁化频率

    # Polder 张量分量
    mu_val = 1 + omega_0 * omega_m / (omega_0 ** 2 - omega ** 2)
    kappa_val = omega * omega_m / (omega_0 ** 2 - omega ** 2)

    mu_tensor = mu_0 * np.array([
        [mu_val, -1j * kappa_val, 0],
        [1j * kappa_val, mu_val, 0],
        [0, 0, 1]
    ])

    # 等效标量磁导率
    mu_eff = (mu_val ** 2 - kappa_val ** 2) / mu_val

    # 圆极化波磁导率
    mu_plus = mu_val + kappa_val      # 右旋 (RHCP)
    mu_minus = mu_val - kappa_val     # 左旋 (LHCP)

    return {
        "mu_tensor": mu_tensor,
        "mu_val": mu_val,
        "kappa_val": kappa_val,
        "mu_eff": mu_eff,
        "mu_plus": mu_plus,
        "mu_minus": mu_minus,
        "omega_0": omega_0,
        "omega_m": omega_m,
    }


# ──────────────────────────────────────────────
# §6.5.2 — Faraday 旋转角
# ──────────────────────────────────────────────
def faraday_rotation_angle(H0=500, Ms=1750, freq=15e9, length=0.03):
    """
    Faraday 旋转角 (Collin §6.5.2)

    需确保 ω > ω₀ 以避免铁磁共振区 (μ₊ 为负导致无物理传播).
    默认参数: f=15 GHz, H0=500 Oe → ω₀/2π≈1.40 GHz, 远低于工作频.

    参数
    ----------
    H0 : float
        偏置磁场 [Oe]
    Ms : float
        饱和磁化 [G]
    freq : float
        频率 [Hz] (需大于 ferromagnetic resonance)
    length : float
        铁氧体长度 [m]

    返回
    --------
    dict
    """
    polder = polder_tensor(H0, Ms, freq)
    mu_plus = polder["mu_plus"]
    mu_minus = polder["mu_minus"]

    omega = 2 * np.pi * freq
    k0 = omega / c

    # 铁氧体通常 epsilon_r ≈ 12-16
    epsilon_f = 14.0

    # 传播常数 for RHCP / LHCP
    # 需要 mu_plus > 0 和 mu_minus > 0
    if mu_plus <= 0 or mu_minus <= 0:
        raise ValueError(
            f"mu_plus={mu_plus:.3f} 或 mu_minus={mu_minus:.3f} <= 0, "
            f"工作在铁磁共振区不可传播。"
        )

    beta_plus = k0 * np.sqrt(mu_plus * epsilon_f)
    beta_minus = k0 * np.sqrt(mu_minus * epsilon_f)

    # 法拉第旋转角
    theta_rad = 0.5 * (beta_plus - beta_minus) * length
    theta_deg = np.degrees(theta_rad)

    return {
        "theta_deg": theta_deg,
        "theta_rad": theta_rad,
        "mu_plus": mu_plus,
        "mu_minus": mu_minus,
        "beta_plus": beta_plus,
        "beta_minus": beta_minus,
        "epsilon_f": epsilon_f,
        "length_m": length,
    }


# ──────────────────────────────────────────────
# §6.5.5 — 结环行器 S 参数
# ──────────────────────────────────────────────
def junction_circulator_s_matrix(isolation_db=25, insertion_loss_db=0.3):
    """
    理想结环行器 S 参数矩阵 (Collin §6.5.5)

    S 矩阵 (理想): 信号沿 1→2→3→1 循环
    非理想情况加入隔离度与插损

    Parameters
    ----------
    isolation_db : float
        隔离度 [dB] (越大越好)
    insertion_loss_db : float
        插入损耗 [dB] (越小越好)

    Returns
    --------
    S : (3,3) ndarray
    """
    # 理想环行器
    S_ideal = np.array([
        [0,        0,       1],
        [1,        0,       0],
        [0,        1,       0]
    ], dtype=complex)

    # 考虑非理想性
    T_linear = 10 ** (-insertion_loss_db / 20)
    I_linear = 10 ** (-isolation_db / 20)

    S_nonideal = S_ideal * T_linear
    # 对角线(隔离)用隔离度填充
    S_nonideal[0, 0] = I_linear
    S_nonideal[1, 1] = I_linear
    S_nonideal[2, 2] = I_linear

    return S_nonideal


# ──────────────────────────────────────────────
# §6.5.6 — YIG 调谐频率
# ──────────────────────────────────────────────
def yig_tuned_frequency(H0_min=500, H0_max=5000, steps=10):
    """
    YIG 调谐频率计算 (Collin §6.5.6)
    f0 (MHz) = 2.8 × H0 (Oe)

    参数
    ----------
    H0_min : float
        最小偏置磁场 [Oe]
    H0_max : float
        最大偏置磁场 [Oe]
    steps : int
        采样点数

    返回
    --------
    list of dicts: {H0_Oe, f0_GHz, f0_MHz}
    """
    H_values = np.linspace(H0_min, H0_max, steps)
    results = []
    for H in H_values:
        f_MHz = 2.8 * H             # Collin 公式 (6.135)
        f_GHz = f_MHz / 1000
        results.append({
            "H0_Oe": H,
            "f0_MHz": f_MHz,
            "f0_GHz": f_GHz,
        })
    return results


# ──────────────────────────────────────────────
# §6.2.4 — 混合环 (Rat-Race) S 参数
# ──────────────────────────────────────────────
def hybrid_ring_s_matrix():
    """
    理想混合环 (Rat-Race) S 参数 (Collin §6.2.4)
    端口定义: 1=输入, 2=直通, 3=隔离, 4=耦合
    """
    S = -1j / np.sqrt(2) * np.array([
        [0,  0,  1,  1],
        [0,  0, -1,  1],
        [1, -1,  0,  0],
        [1,  1,  0,  0],
    ])
    return S


# ──────────────────────────────────────────────
# §6.4.4 — 3-dB 分支线耦合器 S 参数
# ──────────────────────────────────────────────
def branch_line_coupler_s_matrix():
    """
    3-dB 分支线耦合器 S 参数 (Collin §6.4.4)
    """
    S = -1 / np.sqrt(2) * np.array([
        [0,  1j, 1,  0],
        [1j, 0,  0,  1],
        [1,  0,  0,  1j],
        [0,  1,  1j, 0],
    ])
    return S


# ──────────────────────────────────────────────
# §6.5.1 — Polder 张量色散曲线 (辅助)
# ──────────────────────────────────────────────
def polder_dispersion_curve(H0=2000, Ms=1750, freq_range=(1e9, 20e9), n_pts=200):
    """
    计算 Polder 张量 μ 和 κ 随频率的变化
    用于分析铁磁共振 (FMR) 特征
    """
    freqs = np.linspace(freq_range[0], freq_range[1], n_pts)
    mu_vals = []
    kappa_vals = []
    mu_eff_vals = []

    for f in freqs:
        p = polder_tensor(H0, Ms, f)
        mu_vals.append(p["mu_val"])
        kappa_vals.append(p["kappa_val"])
        mu_eff_vals.append(p["mu_eff"])

    return {
        "freqs_Hz": freqs,
        "mu": np.array(mu_vals),
        "kappa": np.array(kappa_vals),
        "mu_eff": np.array(mu_eff_vals),
    }


# ──────────────────────────────────────────────
# §6.4.3 — 多孔耦合器频率扫描
# ──────────────────────────────────────────────
def multi_hole_freq_scan(n_holes=5, f0=10e9, bw=2e9, n_pts=101):
    """
    多孔定向耦合器频率扫描
    """
    freqs = np.linspace(f0 - bw / 2, f0 + bw / 2, n_pts)
    directivities = []
    couplings = []

    for f in freqs:
        res = multi_hole_coupler_directivity(n_holes, f, f0)
        directivities.append(res["directivity_dB"])
        couplings.append(res["coupling_dB"])

    return {
        "freqs_Hz": freqs,
        "directivity_dB": np.array(directivities),
        "coupling_dB": np.array(couplings),
    }


# ══════════════════════════════════════════════
#  自检验证函数
# ══════════════════════════════════════════════
def verify_collins_ch06():
    """
    综合自检 — 验证 §6.2–§6.6 各关键计算

    检查项:
    1. Magic-T S 参数矩阵 unitary 性
    2. Magic-T 隔离端口
    3. Magic-T H 臂等分同相
    4. Bethe 小孔极化率 α_e
    5. Bethe 小孔极化率 α_m
    6. Bethe 小孔正向方向性 (干涉修正后)
    7. 多孔耦合器方向性 (偶数孔, f=f0)
    8. 多孔耦合器偏频方向性
    9. Polder 张量 Hermiticity
    10. Polder μ,κ 非零
    11. Faraday 旋转角合理 (ω > ω₀)
    12. Faraday 零长度零旋转
    13. 结环行器传输系数
    14. 结环行器隔离度
    15. YIG 调谐斜率
    """
    passed = 0
    failed = 0
    details = []
    tol = 1e-10

    # ── 1. Magic-T unitary ──
    S_mt = magic_t_s_matrix()
    S_dag = S_mt.conj().T
    check = S_dag @ S_mt - np.eye(4)
    nrm = np.linalg.norm(check)
    ok = nrm < tol
    passed += 1 if ok else 0
    failed += 0 if ok else 1
    details.append({
        "test": "Magic-T unitary check",
        "status": "PASS" if ok else "FAIL",
        "detail": f"||S† S - I|| = {nrm:.2e} (tol={tol:.0e})",
    })

    # ── 2. Magic-T 隔离端口 ──
    ok = (abs(S_mt[0, 1]) < tol and abs(S_mt[1, 0]) < tol
          and abs(S_mt[2, 3]) < tol and abs(S_mt[3, 2]) < tol)
    passed += 1 if ok else 0
    failed += 0 if ok else 1
    details.append({
        "test": "Magic-T port isolation (S12=S21=S34=S43=0)",
        "status": "PASS" if ok else "FAIL",
        "detail": f"S12={S_mt[0,1]:.3f}, S34={S_mt[2,3]:.3f}",
    })

    # ── 3. Magic-T H 臂等分 ──
    p3 = S_mt[2, 0]
    p4 = S_mt[3, 0]
    ok = (abs(abs(p3) - abs(p4)) < tol
          and abs(np.angle(p3) - np.angle(p4)) < tol)
    passed += 1 if ok else 0
    failed += 0 if ok else 1
    details.append({
        "test": "Magic-T H-arm equal-split in-phase",
        "status": "PASS" if ok else "FAIL",
        "detail": f"S31={p3:.3f}, S41={p4:.3f}",
    })

    # ── 4-5. Bethe 极化率 ──
    bethe = bethe_hole_coupling(r=2e-3, freq=10e9)
    ok = abs(bethe["alpha_e"] - 2/3 * (2e-3)**3) < 1e-15
    passed += 1 if ok else 0
    failed += 0 if ok else 1
    details.append({
        "test": "Bethe alpha_e = 2/3 r^3",
        "status": "PASS" if ok else "FAIL",
        "detail": f"α_e = {bethe['alpha_e']:.3e} (expected {2/3*(2e-3)**3:.3e})",
    })

    ok = abs(bethe["alpha_m"] - 4/3 * (2e-3)**3) < 1e-15
    passed += 1 if ok else 0
    failed += 0 if ok else 1
    details.append({
        "test": "Bethe alpha_m = 4/3 r^3",
        "status": "PASS" if ok else "FAIL",
        "detail": f"α_m = {bethe['alpha_m']:.3e} (expected {4/3*(2e-3)**3:.3e})",
    })

    # ── 6. Bethe 方向性: 修正模型后, 中心孔正向优势 ~5dB ──
    ok = bethe["directivity_dB"] > 0 and bethe["directivity_dB"] < 15  # 正向优势, 约 5 dB
    passed += 1 if ok else 0
    failed += 0 if ok else 1
    details.append({
        "test": "Bethe hole forward directivity (correct sign interference)",
        "status": "PASS" if ok else "FAIL",
        "detail": f"D = {bethe['directivity_dB']:.1f} dB (x={bethe['x_offset_mm']:.2f} mm, Freq={bethe['freq_GHz']:.1f} GHz)",
    })

    # ── 7. 多孔方向性 (N=4 偶数, f=f0 — 反向完全相消) ──
    mh = multi_hole_coupler_directivity(n_holes=4, freq=10e9, f0=10e9)
    ok = abs(mh["S13_rev"]) < 1e-12
    passed += 1 if ok else 0
    failed += 0 if ok else 1
    details.append({
        "test": "Multi-hole (N=4) rev cancellation at f0",
        "status": "PASS" if ok else "FAIL",
        "detail": f"|S13_rev| = {abs(mh['S13_rev']):.3e}",
    })

    # ── 8. 偏频方向性仍为正 ──
    mh_off = multi_hole_coupler_directivity(n_holes=4, freq=10.5e9, f0=10e9)
    ok = mh_off["directivity_dB"] > 5
    passed += 1 if ok else 0
    failed += 0 if ok else 1
    details.append({
        "test": "Multi-hole (N=4) directivity off-center",
        "status": "PASS" if ok else "FAIL",
        "detail": f"D = {mh_off['directivity_dB']:.1f} dB (f={mh_off['freq_GHz']:.1f} GHz)",
    })

    # ── 9. Polder Hermiticity: M[0,1] = conj(M[1,0]) ──
    polder = polder_tensor(H0=2000, Ms=1750, freq=15e9)
    M = polder["mu_tensor"]
    # Hermitian: M = M† → M[0,1] - conj(M[1,0]) = 0
    ok = abs(M[0, 1] - np.conj(M[1, 0])) < tol
    passed += 1 if ok else 0
    failed += 0 if ok else 1
    details.append({
        "test": "Polder tensor Hermiticity (M[0,1]=conj(M[1,0]))",
        "status": "PASS" if ok else "FAIL",
        "detail": f"M[0,1]={M[0,1]:.4f}, conj(M[1,0])={np.conj(M[1,0]):.4f}, diff={abs(M[0,1]-np.conj(M[1,0])):.2e}",
    })

    # ── 10. Polder μ,κ ≠ 0 ──
    ok = polder["mu_val"] > 0 and abs(polder["kappa_val"]) > 0
    passed += 1 if ok else 0
    failed += 0 if ok else 1
    details.append({
        "test": "Polder mu>0, kappa!=0 valid",
        "status": "PASS" if ok else "FAIL",
        "detail": f"μ={polder['mu_val']:.4f}, κ={polder['kappa_val']:.4f}",
    })

    # ── 11. Faraday 旋转 (f=15 GHz, ω > ω₀, L=3 mm 得小角度) ──
    fr = faraday_rotation_angle(H0=500, Ms=1750, freq=15e9, length=0.003)
    ok = 0 < abs(fr["theta_deg"]) < 90
    passed += 1 if ok else 0
    failed += 0 if ok else 1
    details.append({
        "test": "Faraday rotation angle range (ω > ω₀)",
        "status": "PASS" if ok else "FAIL",
        "detail": f"θ = {fr['theta_deg']:.2f}° (L={fr['length_m']*1e3:.1f} mm)",
    })

    # ── 12. 零长度零旋转 ──
    fr_zero = faraday_rotation_angle(H0=500, Ms=1750, freq=15e9, length=0)
    ok = abs(fr_zero["theta_deg"]) < tol
    passed += 1 if ok else 0
    failed += 0 if ok else 1
    details.append({
        "test": "Faraday rotation zero-length = 0",
        "status": "PASS" if ok else "FAIL",
        "detail": f"θ(L=0) = {fr_zero['theta_deg']:.6e}°",
    })

    # ── 13. 结环行器传输 ──
    S_circ = junction_circulator_s_matrix(isolation_db=25, insertion_loss_db=0.3)
    T_lin = 10 ** (-0.3 / 20)
    ok = (abs(abs(S_circ[1, 0]) - T_lin) < 1e-10
          and abs(abs(S_circ[2, 1]) - T_lin) < 1e-10)
    passed += 1 if ok else 0
    failed += 0 if ok else 1
    details.append({
        "test": "Junction circulator transmission",
        "status": "PASS" if ok else "FAIL",
        "detail": f"|S21|={abs(S_circ[1,0]):.4f} (exp={T_lin:.4f}), |S32|={abs(S_circ[2,1]):.4f}",
    })

    # ── 14. 隔离度 ──
    I_lin = 10 ** (-25 / 20)
    ok = abs(abs(S_circ[0, 0]) - I_lin) < 1e-10
    passed += 1 if ok else 0
    failed += 0 if ok else 1
    details.append({
        "test": "Junction circulator isolation",
        "status": "PASS" if ok else "FAIL",
        "detail": f"|S11|={abs(S_circ[0,0]):.4f} (I=25 dB → {I_lin:.4f})",
    })

    # ── 15. YIG 调谐斜率 ──
    yig = yig_tuned_frequency(H0_min=500, H0_max=5000, steps=5)
    f_ratio = yig[-1]["f0_MHz"] / yig[-1]["H0_Oe"]
    ok = abs(f_ratio - 2.8) < 1e-3
    passed += 1 if ok else 0
    failed += 0 if ok else 1
    details.append({
        "test": "YIG tuning slope f(MHz) = 2.8 H(Oe)",
        "status": "PASS" if ok else "FAIL",
        "detail": f"f/H = {f_ratio:.4f} MHz/Oe, range {yig[0]['f0_GHz']:.2f}–{yig[-1]['f0_GHz']:.2f} GHz",
    })

    # ── 汇总 ──
    total = passed + failed
    print("=" * 60)
    print(f"  Collins Ch.6 验证结果: {passed}/{total} 通过")
    print("=" * 60)
    for d in details:
        marker = "✓" if d["status"] == "PASS" else "✗"
        print(f"  {marker} {d['test']}")
        print(f"       {d['detail']}")
    print("=" * 60)

    return passed, failed, details


# ══════════════════════════════════════════════
#  主程序
# ══════════════════════════════════════════════
if __name__ == "__main__":
    print("Collins Ch.6 — Passive Microwave Devices 示例\n")
    print("-" * 50)

    # 1. Magic-T S 参数
    print("\n1. §6.2.3 Magic-T S 参数矩阵:")
    S_mt = magic_t_s_matrix()
    print(np.array_str(S_mt, precision=3, suppress_small=True))

    # 2. 混合环 S 参数
    print("\n2. §6.2.4 混合环 (Rat-Race) S 参数矩阵:")
    S_hybrid = hybrid_ring_s_matrix()
    print(np.array_str(S_hybrid, precision=3, suppress_small=True))

    # 3. 分支线耦合器
    print("\n3. §6.4.4 3-dB 分支线耦合器 S 参数:")
    S_bl = branch_line_coupler_s_matrix()
    print(np.array_str(S_bl, precision=3, suppress_small=True))

    # 4. Bethe 小孔
    print(f"\n4. §6.4.2 Bethe 小孔耦合 (r=2.0 mm, 10 GHz, x=a/2):")
    bethe = bethe_hole_coupling(r=2e-3, freq=10e9)
    print(f"   电极化率 α_e  = {bethe['alpha_e']:.3e} m³")
    print(f"   磁极化率 α_m  = {bethe['alpha_m']:.3e} m³")
    print(f"   导波波长 λ_g  = {bethe['lambda_g']*1e3:.2f} mm")
    print(f"   反向耦幅(port3) = {bethe['coupling_dB']:.1f} dB")
    print(f"   方向性 (port4/port3) = {bethe['directivity_dB']:.1f} dB (正数→正向优势)")
    print(f"   孔偏移 x     = {bethe['x_offset_mm']:.2f} mm (宽边中心)")

    # 5. 多孔方向性
    print(f"\n5. §6.4.3 多孔定向耦合器 (N=4, f₀=10 GHz):")
    mh = multi_hole_coupler_directivity(n_holes=4, freq=10e9, f0=10e9)
    print(f"   孔间距 d      = {mh['d_mm']:.3f} mm")
    print(f"   反向耦合 (port3) = {mh['coupling_port3_dB']:.1f} dB")
    print(f"   正向耦合 (port4) = {mh['coupling_port4_dB']:.1f} dB")
    print(f"   方向性 D       = {mh['directivity_dB']:.1f} dB")

    mh_off = multi_hole_coupler_directivity(n_holes=4, freq=10.5e9, f0=10e9)
    print(f"   偏频 (10.5 GHz) D = {mh_off['directivity_dB']:.1f} dB")

    # 6. Polder 张量 (用 15 GHz 避开铁磁共振)
    print(f"\n6. §6.5.1 Polder 张量 (H₀=2000 Oe, Mₛ=1750 G, f=15 GHz):")
    polder = polder_tensor(H0=2000, Ms=1750, freq=15e9)
    print(f"   张量 (×μ₀):")
    print(np.array_str(polder["mu_tensor"] / mu_0, precision=4, suppress_small=True))
    print(f"   μ     = {polder['mu_val']:.4f}")
    print(f"   κ     = {polder['kappa_val']:.4f}")
    print(f"   μ_eff = {polder['mu_eff']:.4f}")
    print(f"   μ₊    = {polder['mu_plus']:.4f}")
    print(f"   μ₋    = {polder['mu_minus']:.4f}")
    print(f"   ω₀/2π = {polder['omega_0']/(2*np.pi)/1e9:.3f} GHz")
    print(f"   ωₘ/2π = {polder['omega_m']/(2*np.pi)/1e9:.3f} GHz")
    print(f"   (ω > ω₀ → 可传播区)")

    # 7. Faraday 旋转 (f=15 GHz, ω > ω₀)
    print(f"\n7. §6.5.2 Faraday 旋转 (H₀=500 Oe, f=15 GHz, L=5 mm):")
    fr = faraday_rotation_angle(H0=500, Ms=1750, freq=15e9, length=0.005)
    print(f"   旋转角 θ   = {fr['theta_deg']:.2f}°")
    print(f"   μ₊        = {fr['mu_plus']:.4f}")
    print(f"   μ₋        = {fr['mu_minus']:.4f}")
    print(f"   β₊        = {fr['beta_plus']:.2f} rad/m")
    print(f"   β₋        = {fr['beta_minus']:.2f} rad/m")

    # 8. 结环行器
    print(f"\n8. §6.5.5 结环行器 S 参数 (隔离=25 dB, 插损=0.3 dB):")
    S_circ = junction_circulator_s_matrix(25, 0.3)
    print(np.array_str(S_circ, precision=4, suppress_small=True))

    # 9. YIG 调谐
    print(f"\n9. §6.5.6 YIG 调谐频率:")
    yig_results = yig_tuned_frequency(500, 5000, 5)
    for yr in yig_results:
        print(f"   H₀ = {yr['H0_Oe']:5.0f} Oe → f₀ = {yr['f0_MHz']:7.0f} MHz = {yr['f0_GHz']:.3f} GHz")

    # 10. 运行自检
    print("\n" + "=" * 60)
    print("  运行自检验证...")
    print("=" * 60)
    p, f, _ = verify_collins_ch06()
    print(f"\n结果: {p} 通过, {f} 失败 / 总计 {p+f}")
