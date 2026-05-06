#!/usr/bin/env python3
"""
郭硕鸿《电动力学》第3版 — Ch1 电磁现象的普遍规律
示例代码：数值验证与可视化

内容：
  1. 点电荷阵列电场（库仑叠加）
  2. Biot-Savart 磁场数值验证（有限长直导线）
  3. 平面波的 Maxwell 方程验证（∇·E=0, ∇×E=-∂B/∂t）
  4. 坡印廷矢量/能流计算（平面波）

依赖：numpy, matplotlib（可选；核心计算不需绘图）
"""

import numpy as np

# ============================================================
# 物理常数
# ============================================================
EPS0 = 8.854187817e-12   # 真空介电常数 [F/m]
MU0  = 4 * np.pi * 1e-7  # 真空磁导率 [N/A^2]
C    = 1.0 / np.sqrt(EPS0 * MU0)  # 光速 [m/s]


# ============================================================
# 例1：点电荷阵列电场（库仑叠加）
# ============================================================

def field_point_charge(q, pos, r):
    """
    单个点电荷在观察点 r 处产生的电场 [V/m]
    使用库仑定律：E = q * (r - r') / (4πε₀ |r-r'|³)

    参数
    ----------
    q  : float      电荷量 [C]
    pos: (3,) array 点电荷位置 [m]
    r  : (3,) array 观察点位置 [m]

    返回
    -------
    (3,) array  电场强度 [V/m]
    """
    dr = np.asarray(r, dtype=float) - np.asarray(pos, dtype=float)
    r_norm = np.linalg.norm(dr)
    if r_norm < 1e-15:
        return np.zeros(3)  # 避免奇点
    return q * dr / (4.0 * np.pi * EPS0 * r_norm**3)


def field_charge_array(charges, positions, r):
    """
    多个点电荷在观察点 r 处的电场叠加

    参数
    ----------
    charges  : (N,) array       各点电荷量 [C]
    positions: (N, 3) array     各点电荷位置 [m]
    r        : (3,) array       观察点位置 [m]

    返回
    -------
    (3,) array  总电场强度 [V/m]
    """
    E_total = np.zeros(3)
    for q, pos in zip(charges, positions):
        E_total += field_point_charge(q, pos, r)
    return E_total


def example_charge_dipole():
    """
    电偶极子电场示例：
    两个等量异号电荷 (±q)，相距 d，沿 x 轴排列
    计算偶极子中垂面上各点的电场并与解析解比较
    """
    q = 1e-9          # 1 nC
    d = 1e-3          # 1 mm
    positions = np.array([[-d/2, 0.0, 0.0], [d/2, 0.0, 0.0]])
    charges = np.array([-q, q])  # 负电荷在左，正电荷在右

    # 在中垂面 (y-z 平面) 上取点，距原点 0.5 cm
    r = np.array([0.0, 5e-3, 0.0])
    E = field_charge_array(charges, positions, r)

    # 解析近似解（偶极矩 p = q*d，中垂面上 |E| ≈ p/(4πε₀ r³)）
    p = q * d                            # 偶极矩 [C·m]
    E_analytic = p / (4.0 * np.pi * EPS0 * np.linalg.norm(r)**3)

    E_numeric = np.linalg.norm(E)
    error = abs(E_numeric - E_analytic)

    print("=" * 60)
    print("例1：电偶极子电场验证")
    print("=" * 60)
    print(f"  观察点: {r}")
    print(f"  数值 |E|: {E_numeric:.6e} V/m")
    print(f"  解析 |E| (远场近似): {E_analytic:.6e} V/m")
    print(f"  相对误差: {error / E_analytic * 100:.4f}%")
    print()

    return E_numeric, E_analytic


# ============================================================
# 例2：Biot-Savart 磁场数值验证（有限长直导线）
# ============================================================

def biot_savart_wire_segment(I, p0, p1, r, N=200):
    """
    有限长直导线电流产生的磁场（Biot-Savart 数值积分）

    参数
    ----------
    I  : float    电流 [A]
    p0 : (3,)     起点 [m]
    p1 : (3,)     终点 [m]
    r  : (3,)     观察点 [m]
    N  : int      分段数（默认 200）

    返回
    -------
    (3,) array 磁感应强度 [T]
    """
    p0 = np.asarray(p0, dtype=float)
    p1 = np.asarray(p1, dtype=float)
    r  = np.asarray(r, dtype=float)

    t_vals = np.linspace(0, 1, N, endpoint=False)
    dt = 1.0 / N
    B = np.zeros(3)

    for t in t_vals:
        # 当前积分点的位置和微分长度
        pos = p0 + t * (p1 - p0)
        dl = (p1 - p0) * dt

        # 从场点到观察点的矢量
        R = r - pos
        R_norm = np.linalg.norm(R)
        if R_norm < 1e-15:
            continue
        # dB = μ₀ I dl × R / (4π |R|³)
        dB = MU0 * I * np.cross(dl, R) / (4.0 * np.pi * R_norm**3)
        B += dB

    return B


def example_biot_savart():
    """
    验证有限长直导线磁场：
    导线沿 z 轴从 (0,0,-L) 到 (0,0,L)，观察点在 x 轴上
    解析解：B = μ₀ I / (2π d) * L / sqrt(L² + d²)  φ方向
    """
    I = 5.0          # 5 A
    L = 0.5          # 半长 0.5 m
    d = 0.1          # 到 x 轴距离 10 cm

    p0 = np.array([0.0, 0.0, -L])
    p1 = np.array([0.0, 0.0,  L])
    r  = np.array([d, 0.0, 0.0])

    B_num = biot_savart_wire_segment(I, p0, p1, r, N=500)

    # 解析解：B = μ₀ I / (4π d) * (sinθ₁ - sinθ₂)
    # 对称情况：θ₁ = arctan(L/d), θ₂ = -θ₁ → sinθ₁ = L/√(L²+d²)
    sin_theta = L / np.sqrt(L**2 + d**2)
    B_analytic = MU0 * I / (4 * np.pi * d) * (sin_theta - (-sin_theta))
    B_analytic = B_analytic  # 正值，方向为 +y 方向（右手定则）

    B_num_mag = np.linalg.norm(B_num)
    # 应指向 +y 方向
    B_direction = B_num / B_num_mag if B_num_mag > 0 else np.zeros(3)
    error = abs(B_num_mag - B_analytic)

    print("=" * 60)
    print("例2：有限长直导线 Biot-Savart 磁场验证")
    print("=" * 60)
    print(f"  电流: {I} A, 半长 L={L} m, 距离 d={d} m")
    print(f"  数值 |B|: {B_num_mag:.6e} T")
    print(f"  解析 |B|: {B_analytic:.6e} T")
    print(f"  相对误差: {error / B_analytic * 100:.4f}%")
    print(f"  数值 B 方向: ({B_direction[0]:.4f}, {B_direction[1]:.4f}, {B_direction[2]:.4f})")
    print()

    return B_num, B_analytic


# ============================================================
# 例3：平面波的 Maxwell 方程数值验证
# ============================================================

def example_plane_wave_maxwell():
    """
    验证平面电磁波满足 Maxwell 方程组：
    E(r,t) = E₀ cos(k·r - ωt) 沿 x 方向偏振，沿 z 方向传播
    B(r,t) = B₀ cos(k·r - ωt) 沿 y 方向偏振

    数值检验 ∇·E = 0, ∇×E = -∂B/∂t
    """
    freq = 1e9       # 1 GHz
    omega = 2 * np.pi * freq
    k_vec = np.array([0.0, 0.0, omega / C])  # 沿 +z 传播
    k = np.linalg.norm(k_vec)
    E0 = np.array([1.0, 0.0, 0.0])           # E 沿 x 方向
    B0 = np.array([0.0, E0[0] / C, 0.0])     # B = E₀/c 沿 y 方向

    t = np.pi / (4 * omega)  # 八分之一周期，此时电场和 ∂B/∂t 均非零
    # 定义一个空间网格（小立方体，中心在原点）
    nx, ny, nz = 20, 20, 20
    L = 3e-3  # 半个边长 3mm ≪ λ≈30cm
    xs = np.linspace(-L, L, nx)
    ys = np.linspace(-L, L, ny)
    zs = np.linspace(-L, L, nz)
    dx = xs[1] - xs[0]
    dy = ys[1] - ys[0]
    dz = zs[1] - zs[0]

    # 中心点在原点
    r0 = np.array([0.0, 0.0, 0.0])

    # 在中心点计算场的值
    phase0 = np.dot(k_vec, r0) - omega * t
    E_center = E0 * np.cos(phase0)
    B_center = B0 * np.cos(phase0)
    # 时间导数 ∂B/∂t
    dBdt_center = B0 * omega * np.sin(phase0)

    # --- ∇·E 数值验证 ---
    # 用有限差分在中心点计算散度
    divE = 0.0
    # 对 x 方向
    r_plus  = r0 + np.array([dx/2, 0, 0])
    r_minus = r0 - np.array([dx/2, 0, 0])
    p_plus  = np.dot(k_vec, r_plus) - omega * t
    p_minus = np.dot(k_vec, r_minus) - omega * t
    Ex_plus  = E0[0] * np.cos(p_plus)
    Ex_minus = E0[0] * np.cos(p_minus)
    divE += (Ex_plus - Ex_minus) / dx

    # 对 y 方向（Ey=0）
    # 对 z 方向
    r_plus  = r0 + np.array([0, 0, dz/2])
    r_minus = r0 - np.array([0, 0, dz/2])
    p_plus  = np.dot(k_vec, r_plus) - omega * t
    p_minus = np.dot(k_vec, r_minus) - omega * t
    Ez_plus  = E0[2] * np.cos(p_plus)   # = 0
    Ez_minus = E0[2] * np.cos(p_minus)  # = 0
    divE += (Ez_plus - Ez_minus) / dz

    # --- ∇×E 数值验证 ---
    # curl_xyz 在中心点，用二阶中心差分
    # (∇×E)_x = ∂Ez/∂y - ∂Ey/∂z
    # (∇×E)_y = ∂Ex/∂z - ∂Ez/∂x
    # (∇×E)_z = ∂Ey/∂x - ∂Ex/∂y

    r_y_plus  = r0 + np.array([0, dy/2, 0])
    r_y_minus = r0 - np.array([0, dy/2, 0])
    r_z_plus  = r0 + np.array([0, 0, dz/2])
    r_z_minus = r0 - np.array([0, 0, dz/2])
    r_x_plus  = r0 + np.array([dx/2, 0, 0])
    r_x_minus = r0 - np.array([dx/2, 0, 0])

    def E_at(r):
        phase = np.dot(k_vec, r) - omega * t
        return E0 * np.cos(phase)

    def B_at(r):
        phase = np.dot(k_vec, r) - omega * t
        return B0 * np.cos(phase)

    curlE = np.zeros(3)
    curlE[0] = (E_at(r_y_plus)[2] - E_at(r_y_minus)[2]) / dy \
             - (E_at(r_z_plus)[1] - E_at(r_z_minus)[1]) / dz
    curlE[1] = (E_at(r_z_plus)[0] - E_at(r_z_minus)[0]) / dz \
             - (E_at(r_x_plus)[2] - E_at(r_x_minus)[2]) / dx
    curlE[2] = (E_at(r_x_plus)[1] - E_at(r_x_minus)[1]) / dx \
             - (E_at(r_y_plus)[0] - E_at(r_y_minus)[0]) / dy

    # -∂B/∂t
    neg_dBdt = -dBdt_center

    neg_dBdt_norm = np.linalg.norm(neg_dBdt)
    curlE_error = np.linalg.norm(curlE - neg_dBdt) / neg_dBdt_norm if neg_dBdt_norm > 0 else 0.0

    print("=" * 60)
    print("例3：平面波 Maxwell 方程组数值验证")
    print("=" * 60)
    print(f"  频率: {freq*1e-9:.1f} GHz 波长: {2*np.pi/k*1e2:.2f} cm")
    print()
    print(f"  1. ∇·E = {divE:.6e} (期望: 0)")
    print(f"     结论: {'✓ ∇·E=0 成立' if abs(divE) < 1e-6 else '✗ 存在偏差'}")
    print()
    print(f"  2. ∇×E = ({curlE[0]:.3e}, {curlE[1]:.3e}, {curlE[2]:.3e})")
    print(f"     -∂B/∂t = ({neg_dBdt[0]:.3e}, {neg_dBdt[1]:.3e}, {neg_dBdt[2]:.3e})")
    print(f"     相对误差: {curlE_error * 100:.4f}%")
    print(f"     结论: {'✓ ∇×E=-∂B/∂t 成立' if curlE_error < 1e-3 else '✗ 存在偏差'}")
    print()

    return divE, curlE, neg_dBdt


# ============================================================
# 例4：坡印廷矢量/能流计算（平面波）
# ============================================================

def example_poynting_vector():
    """
    平面电磁波的坡印廷矢量
    验证：S = E×H = E×B/μ₀

    时均坡印廷矢量（时间平均）：⟨S⟩ = ½ Re(E₀ × H₀*)
    对线偏振波：⟨S⟩ = ½ E₀²/(μ₀c) = ½ ε₀ c E₀²  沿传播方向
    """
    freq = 1e9
    omega = 2 * np.pi * freq
    k = omega / C
    E0_amp = 1.0                    # 电场振幅 [V/m]
    H0_amp = E0_amp / (C * MU0)     # H = E/Z₀, Z₀=μ₀c

    t_vals = np.linspace(0, 1/freq, 1000)  # 一个周期采样
    S_inst_vals = []
    S_avg = np.zeros(3)

    k_vec = np.array([0.0, 0.0, k])
    r = np.array([0.0, 0.0, 0.0])

    for t in t_vals:
        phase = np.dot(k_vec, r) - omega * t
        E = np.array([E0_amp * np.cos(phase), 0.0, 0.0])
        H = np.array([0.0, H0_amp * np.cos(phase), 0.0])
        S_inst = np.cross(E, H)  # 瞬时坡印廷矢量
        S_inst_vals.append(S_inst)
        S_avg += S_inst

    S_avg /= len(t_vals)  # 时均值

    # 解析时均值 ⟨S⟩ = ½ E₀²/(Z₀) = ½ ε₀ c E₀²
    Z0 = C * MU0  # 真空阻抗 ≈ 377 Ω
    S_avg_analytic = 0.5 * E0_amp**2 / Z0
    S_avg_mag = np.linalg.norm(S_avg)
    error = abs(S_avg_mag - S_avg_analytic)

    # 验证能量守恒：S 的大小等于 w*c（能量密度 × 光速）
    w_avg = 0.5 * (0.5 * EPS0 * E0_amp**2 + 0.5 * (E0_amp / C)**2 / MU0) * 2
    # 简化为：⟨w⟩ = ¼ ε₀ E₀² + ¼ B₀²/μ₀ = ½ ε₀ E₀²
    w_avg_simple = 0.5 * EPS0 * E0_amp**2
    S_from_energy = w_avg_simple * C

    print("=" * 60)
    print("例4：平面波坡印廷矢量/能流计算")
    print("=" * 60)
    print(f"  电场振幅 E₀ = {E0_amp} V/m")
    print(f"  磁场振幅 H₀ = {H0_amp:.4e} A/m")
    print(f"  真空阻抗 Z₀ = {Z0:.2f} Ω")
    print()
    print(f"  时均 |⟨S⟩| (数值): {S_avg_mag:.6e} W/m²")
    print(f"  时均 |⟨S⟩| (解析): {S_avg_analytic:.6e} W/m²")
    print(f"  相对误差: {error / S_avg_analytic * 100:.4f}%")
    print(f"  平均能流方向: ({S_avg[0]/S_avg_mag:.4f}, {S_avg[1]/S_avg_mag:.4f}, {S_avg[2]/S_avg_mag:.4f})")
    print()
    print(f"  场能量密度 ⟨w⟩ = {w_avg_simple:.4e} J/m³")
    print(f"  ⟨w⟩ × c = {S_from_energy:.4e} W/m² (应与 S 一致)")
    print(f"  能量-能流一致性误差: {abs(S_avg_mag - S_from_energy) / S_from_energy * 100:.4f}%")
    print()

    return S_avg, S_avg_analytic


# ============================================================
# 综合验收函数
# ============================================================

def verify_guoshuohong_ch01():
    """
    验收函数：运行 Ch1 全部四个数值示例，报告结果
    返回: True（全部通过）/ False
    """
    print()
    print("╔" + "═" * 58 + "╗")
    print("║  郭硕鸿《电动力学》Ch1 数值验证 — 验收报告  ║")
    print("╚" + "═" * 58 + "╝")
    print()

    # 例1
    E_num, E_an = example_charge_dipole()

    # 例2
    B_num, B_an = example_biot_savart()

    # 例3
    divE, curlE, neg_dBdt = example_plane_wave_maxwell()

    # 例4
    S_avg, S_an = example_poynting_vector()

    # 汇总
    passed = True
    checks = []

    # 例1：偶极子误差 < 5%
    err1 = abs(E_num - E_an) / E_an * 100
    checks.append(("例1 偶极子电场", err1 < 5.0, f"误差 {err1:.2f}%"))

    # 例2：Biot-Savart 误差 < 5%
    err2 = abs(np.linalg.norm(B_num) - B_an) / B_an * 100
    checks.append(("例2 Biot-Savart 磁场", err2 < 5.0, f"误差 {err2:.2f}%"))

    # 例3a：∇·E ≈ 0
    checks.append(("例3a ∇·E=0", abs(divE) < 1e-6, f"|divE|={abs(divE):.2e}"))

    # 例3b：∇×E ≈ -∂B/∂t
    neg_dBdt_norm2 = np.linalg.norm(neg_dBdt)
    curlE_err = np.linalg.norm(curlE - neg_dBdt) / neg_dBdt_norm2 * 100 if neg_dBdt_norm2 > 0 else 0.0
    checks.append(("例3b ∇×E=-∂B/∂t", curlE_err < 1.0, f"误差 {curlE_err:.2f}%"))

    # 例4：坡印廷匹配
    err4 = abs(np.linalg.norm(S_avg) - S_an) / S_an * 100
    checks.append(("例4 坡印廷能流", err4 < 1.0, f"误差 {err4:.2f}%"))

    print("-" * 60)
    print("各项目标检查：")
    print("-" * 60)
    for name, ok, detail in checks:
        status = "✓" if ok else "✗"
        print(f"  {status} {name:25s}  {detail}")
        if not ok:
            passed = False

    print()
    if passed:
        print("🎉 全部检查通过！Ch1 代码运行无误。")
    else:
        print("⚠️  部分检查未通过，请参阅上述详细信息。")

    print()
    return passed


# ============================================================
# 主入口
# ============================================================

if __name__ == "__main__":
    verify_guoshuohong_ch01()
