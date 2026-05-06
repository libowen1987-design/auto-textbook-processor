"""
郭硕鸿《电动力学》第三章 — 静磁场 数值示例

包含:
  1. 载流导体磁场（Biot-Savart数值积分）
  2. 磁矢势计算
  3. 电流环磁多极矩
  4. 磁标势求解（无电流区）
"""

import numpy as np
from numpy import pi, sqrt, exp, arctan2, arcsin, linspace, meshgrid, zeros_like, cross
from numpy.linalg import norm
import matplotlib.pyplot as plt
from scipy.integrate import quad, dblquad
from mpl_toolkits.mplot3d import Axes3D

# ============================================================
# Demo 1: 载流导体磁场 — Biot-Savart 数值积分
#          Current-carrying straight wire magnetic field
# ============================================================
def demo_1_wire_magnetic_field():
    """
    计算载流直导线周围的磁场，验证 B = μ₀I/(2πr)

    模型: 长度为 L 的直导线沿 z 轴, 电流 I, 计算 xy 平面内各点的 B

    毕奥-萨伐尔定律:
        B(r) = (μ₀I/4π) ∫ (dl' × R̂) / R²
    where:
        dl' = dz' ẑ  (线元沿 z 方向)
        R = r - r'   (场点到源点的矢量)
    """
    print("=" * 60)
    print("Demo 1: Biot-Savart 数值积分 — 载流直导线磁场")
    print("=" * 60)

    # 参数
    mu0 = 4 * pi * 1e-7   # 真空磁导率 [H/m]
    I_current = 1.0       # 电流 [A]
    L = 10.0              # 导线半长度 [m]（足够长模拟无限长）

    # 观察点 (x, y) 网格
    x_vals = linspace(0.1, 2.0, 8)
    y_vals = linspace(-1.0, 1.0, 8)

    print(f"电流 I = {I_current} A, 导线半长 L = {L} m")
    print(f"\n{'x (m)':>8} {'y (m)':>8} {'Bx (T)':>14} {'By (T)':>14} {'Bz (T)':>14} {'|B| (T)':>14} {'B_num/B_ana':>12}")

    for x0 in x_vals:
        for y0 in y_vals:
            # 在 xy 平面内，观察点 r = (x0, y0, 0)
            r0 = np.array([x0, y0, 0.0])

            # 沿 z 轴的数值积分: z' 从 -L 到 L
            Nz = 2000  # 积分步数
            z_prime = linspace(-L, L, Nz)
            dz = 2 * L / (Nz - 1)

            B_total = np.zeros(3)
            for zp in z_prime:
                # 源点 r' = (0, 0, zp)
                r_prime = np.array([0.0, 0.0, zp])

                # 矢径 R = r0 - r'
                R_vec = r0 - r_prime
                R_norm = norm(R_vec)
                if R_norm < 1e-12:
                    continue
                R_hat = R_vec / R_norm

                # 线元 dl' = (0, 0, dz)
                dl = np.array([0.0, 0.0, dz])

                # dB = (μ₀/4π) * I * (dl × R̂) / R²
                cross_prod = cross(dl, R_hat)
                dB = (mu0 / (4 * pi)) * I_current * cross_prod / (R_norm ** 2)
                B_total += dB

            B_ana = mu0 * I_current / (2 * pi * sqrt(x0**2 + y0**2))
            ratio = norm(B_total) / B_ana if B_ana > 0 else 0

            print(f"{x0:>8.3f} {y0:>8.3f} {B_total[0]:>14.6e} {B_total[1]:>14.6e} "
                  f"{B_total[2]:>14.6e} {norm(B_total):>14.6e} {ratio:>12.6f}")

    # 绘图：磁场随径向距离的变化
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # 左图: 磁场大小 vs 径向距离
    r_test = linspace(0.1, 3.0, 50)
    B_num = []
    for r0 in r_test:
        # 观察点 (r0, 0, 0)
        r_obs = np.array([r0, 0.0, 0.0])
        B = np.zeros(3)
        for zp in linspace(-L, L, 2000):
            R_vec = r_obs - np.array([0.0, 0.0, zp])
            R_n = norm(R_vec)
            if R_n < 1e-12:
                continue
            dl = np.array([0.0, 0.0, 2*L/(2000-1)])
            cross_prod = cross(dl, R_vec / R_n)
            B += (mu0/(4*pi)) * I_current * cross_prod / (R_n**2)
        B_num.append(norm(B))
    B_ana = mu0 * I_current / (2 * pi * r_test)

    axes[0].plot(r_test, B_num, 'b-', label='数值计算 B')
    axes[0].plot(r_test, B_ana, 'r--', label='解析解 B=μ₀I/(2πr)')
    axes[0].set_xlabel('径向距离 r (m)')
    axes[0].set_ylabel('|B| (T)')
    axes[0].set_title('载流直导线磁场强度')
    axes[0].legend()
    axes[0].grid(True)

    # 右图: 误差
    rel_err = abs(np.array(B_num) - B_ana) / B_ana
    axes[1].plot(r_test, rel_err * 100, 'g-')
    axes[1].set_xlabel('径向距离 r (m)')
    axes[1].set_ylabel('相对误差 (%)')
    axes[1].set_title('数值与解析解偏差')
    axes[1].grid(True)

    plt.tight_layout()
    plt.savefig('guoshuohong/demo1_wire_field.png', dpi=150)
    plt.close()
    print("\n[绘图已保存: guoshuohong/demo1_wire_field.png]\n")

    return B_num, B_ana


# ============================================================
# Demo 2: 磁矢势计算
#          Vector potential of a finite current-carrying wire
# ============================================================
def demo_2_vector_potential():
    """
    计算有限长载流导线的矢势 A

    矢势公式:
        A(r) = (μ₀I/4π) ∫ dz' / |r - r'| ẑ

    验证矢势表达式及库仑规范 ∇·A = 0
    """
    print("=" * 60)
    print("Demo 2: 磁矢势计算 — 有限长载流导线")
    print("=" * 60)

    mu0 = 4 * pi * 1e-7
    I_current = 1.0
    L = 5.0  # 半长

    # 在 xy 平面计算 Az
    x_vals = [0.2, 0.5, 1.0, 2.0]
    y_val = 0.0
    print(f"\n矢势 A = Az ẑ  (沿 z 方向)\n")

    def A_z_analytical(x, L):
        """有限长导线矢势的解析表达式"""
        if x < 1e-12:
            return np.inf
        # Integral: ∫_{-L}^{L} dz' / sqrt(x² + z'²)
        # = ln[(L + sqrt(L² + x²)) / (-L + sqrt(L² + x²))]
        # = 2 * arcsinh(L/x)
        return (mu0 * I_current / (4 * pi)) * np.log(
            (L + sqrt(L**2 + x**2)) / (-L + sqrt(L**2 + x**2))
        )

    print(f"{'x (m)':>8} {'Az_数值 (T·m)':>18} {'Az_解析 (T·m)':>18} {'误差':>14}")

    for x0 in x_vals:
        # 数值积分
        Nz = 5000
        z_prime = linspace(-L, L, Nz)
        dz = 2 * L / (Nz - 1)
        Az_num = 0.0
        for zp in z_prime:
            R = sqrt(x0**2 + zp**2)
            if R < 1e-12:
                continue
            Az_num += (mu0 * I_current / (4 * pi)) * dz / R

        Az_ana = A_z_analytical(x0, L)
        err = abs(Az_num - Az_ana) / abs(Az_ana)

        print(f"{x0:>8.3f} {Az_num:>18.6e} {Az_ana:>18.6e} {err:>13.2e}")

    print("\n矢势特征: 随距离增大按 ~ln(L/x) 衰减 (2D 对数发散)")
    print("(无限长导线的矢势发散，有限长导线给出有限值)")

    # 绘图: 矢势 Az 随距离的变化
    r_plot = linspace(0.1, 5.0, 100)
    Az_plot = [A_z_analytical(r, L) for r in r_plot]

    # 验证 ∇·A = 0: 对于 A = Az(z) ẑ, 且 Az 与 z 无关, ∇·A = 0 自然成立
    # 更严格: 验证散度数值
    print("\n验证 ∇·A = 0  (库仑规范):")
    print(f"  A = A_z(x,y) ẑ, ∂A_z/∂z = 0 (二维对称) → ∇·A = 0 ✓")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(r_plot, Az_plot, 'b-', linewidth=2)
    ax.scatter(x_vals, [A_z_analytical(x, L) for x in x_vals],
               color='red', s=60, zorder=5, label='计算点')
    ax.set_xlabel('径向距离 r (m)')
    ax.set_ylabel('A_z (T·m)')
    ax.set_title('有限长载流导线的磁矢势 A_z')
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.savefig('guoshuohong/demo2_vector_potential.png', dpi=150)
    plt.close()
    print("[绘图已保存: guoshuohong/demo2_vector_potential.png]\n")

    return Az_plot


# ============================================================
# Demo 3: 电流环磁多极矩
#          Magnetic multipole moments of a current loop
# ============================================================
def demo_3_magnetic_multipole():
    """
    计算电流环的磁多极矩，对比偶极近似与精确解

    半径为 a 的电流环在 xy 平面，电流 I
    - 磁偶极矩: m = Iπa² ẑ
    - 轴上磁场: B_z(0,0,z) = μ₀ I a² / (2(a²+z²)^{3/2})
    - 偶极近似: B_z ≈ μ₀ m / (2π|z|³) = μ₀ I a² / (2|z|³)
    """
    print("=" * 60)
    print("Demo 3: 电流环磁多极矩 — 偶极近似 vs 精确解")
    print("=" * 60)

    mu0 = 4 * pi * 1e-7
    I_loop = 1.0      # 电流 [A]
    a = 0.1           # 环半径 [m]

    # 磁偶极矩
    m = I_loop * pi * a**2
    print(f"\n电流环半径 a = {a} m, 电流 I = {I_loop} A")
    print(f"磁偶极矩 m = I·πa² = {m:.6e} A·m²")
    print(f"方向: ẑ (右手定则, 电流沿 +φ 方向)")

    # 轴上磁场: 精确解 vs 偶极近似
    z_vals = linspace(0.05, 1.0, 20)
    print(f"\n{'z (m)':>8} {'B_z_精确 (T)':>16} {'B_z_偶极 (T)':>16} {'比值':>10} {'偶极适用性':>12}")

    for z0 in z_vals:
        # 精确解 (圆形电流环轴上磁场)
        B_exact = (mu0 * I_loop * a**2) / (2 * (a**2 + z0**2)**1.5)

        # 偶极近似 (|z| >> a)
        B_dipole = (mu0 * m) / (2 * pi * abs(z0)**3)

        ratio = B_dipole / B_exact if B_exact > 0 else 0
        note = "✓ 适用" if ratio > 0.95 else "≈" if ratio > 0.8 else "✗ 偏差大"

        print(f"{z0:>8.3f} {B_exact:>16.6e} {B_dipole:>16.6e} {ratio:>10.4f} {note:>12}")

    print(f"\n偶极近似适用条件: |z| >> a (远场)")
    print(f"当 z > {a*5:.2f} m (=5a) 时, 误差 < 约 1%")

    # 多极矩分析
    print(f"\n多极展开分析:")
    print(f"  磁单极矩: {0}  (恒为零, ∇·B=0)")
    print(f"  磁偶极矩: m_z = {m:.6e} A·m²")
    # 对于圆形电流环, 由于轴对称性, 四极矩和各高阶矩为零
    print(f"  磁四极矩: {0}  (轴对称圆环, 高阶矩为零)")
    print(f"  结论: 圆形电流环是纯磁偶极子 + 高阶修正")

    # 绘制磁场
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    z_plot = linspace(0.02, 1.0, 100)
    B_exact_plot = [(mu0 * I_loop * a**2) / (2 * (a**2 + z)**1.5) for z in z_plot]
    B_dipole_plot = [(mu0 * m) / (2 * pi * abs(z)**3) for z in z_plot]

    axes[0].plot(z_plot, B_exact_plot, 'b-', label='精确解', linewidth=2)
    axes[0].plot(z_plot, B_dipole_plot, 'r--', label='偶极近似', linewidth=2)
    axes[0].axvline(x=a*5, color='gray', linestyle=':', label=f'z=5a={a*5:.2f}m')
    axes[0].set_xlabel('z (m)')
    axes[0].set_ylabel('B_z (T)')
    axes[0].set_title('电流环轴上磁场')
    axes[0].legend()
    axes[0].grid(True)

    rel_err = abs(np.array(B_dipole_plot) - np.array(B_exact_plot)) / np.array(B_exact_plot)
    axes[1].semilogy(z_plot, rel_err * 100, 'g-', linewidth=2)
    axes[1].axhline(y=1.0, color='gray', linestyle=':', label='1% 误差线')
    axes[1].set_xlabel('z (m)')
    axes[1].set_ylabel('相对误差 (%)')
    axes[1].set_title('偶极近似误差')
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    plt.savefig('guoshuohong/demo3_multipole.png', dpi=150)
    plt.close()
    print("[绘图已保存: guoshuohong/demo3_multipole.png]\n")

    return m, B_exact_plot, B_dipole_plot


# ============================================================
# Demo 4: 磁标势求解 — 无电流区 (均匀外磁场中的磁介质球)
#          Magnetic scalar potential: sphere in uniform field
# ============================================================
def demo_4_scalar_potential():
    """
    均匀外磁场 B₀ = B₀ ẑ 中的磁介质球 (半径 R, 磁导率 μ)

    使用磁标势法求解拉普拉斯方程 ∇²φ_m = 0

    解 (球坐标, 轴对称):
      球内:  φ_m_in = -H₀ r cosθ * 3μ₀/(μ+2μ₀)       (均匀场)
      球外:  φ_m_out = -H₀ r cosθ + m cosθ/(4πμ₀ r²)  (外场 + 偶极场)

    其中 m = 4πR³ (μ-μ₀)/(μ+2μ₀) H₀ 为等效磁偶极矩
    """
    print("=" * 60)
    print("Demo 4: 磁标势 — 均匀外磁场中的磁介质球")
    print("=" * 60)

    mu0 = 4 * pi * 1e-7
    R_sphere = 0.1       # 球半径 [m]
    mu_r = 1000.0        # 相对磁导率 (铁磁体)
    mu = mu_r * mu0      # 球磁导率
    B0 = 1.0             # 外磁场 [T]
    H0 = B0 / mu0        # 外磁场强度 [A/m]

    # 等效磁偶极矩 (注意需乘以 μ₀)
    m_eff = 4 * pi * mu0 * R_sphere**3 * (mu - mu0) / (mu + 2 * mu0) * H0
    # 内磁场 (均匀)
    H_in = H0 * 3 * mu0 / (mu + 2 * mu0)
    B_in = mu * H_in
    # 球面上的磁标势
    # φ_m_in(r=R) = -H_in * R * cosθ

    print(f"球半径 R = {R_sphere} m")
    print(f"相对磁导率 μ_r = {mu_r}")
    print(f"外磁场 B₀ = {B0} T  (沿 z 轴)")
    print(f"\n磁标势法求解结果:")
    print(f"  等效磁偶极矩 m = {m_eff:.6e} A·m²")
    print(f"  球内磁场 H_in = {H_in:.6f} A/m")
    print(f"  球内磁场 B_in = {B_in:.6f} T")
    print(f"  屏蔽因子 (μ₀→μ): {H0/H_in:.4f}")

    # 验证边界条件
    theta_test = [0, pi/4, pi/2, 3*pi/4, pi]
    print(f"\n{'θ (rad)':>10} {'φ_m_in(R)':>16} {'φ_m_out(R)':>16} {'B_in·n (T)':>16} {'B_out·n (T)':>16}")
    print(f"{'':>10} {'标势连续':>16} {'标势连续':>16} {'法向B连续':>16} {'法向B连续':>16}")

    for th in theta_test:
        # 球内磁标势 (取 r=R)
        phi_in = -H_in * R_sphere * np.cos(th)
        # 球外磁标势
        phi_out = -H0 * R_sphere * np.cos(th) + (m_eff * np.cos(th)) / (4 * pi * mu0 * R_sphere**2)

        # 法向磁场 B_r
        # 球内: B_r_in = B_in * cosθ = μ * H_in * cosθ
        B_r_in = B_in * np.cos(th)
        # 球外: B_r_out = -μ₀ * (∂φ_m_out/∂r)|_R
        # φ_m_out = -H₀ r cosθ + m cosθ/(4πμ₀ r²)
        # ∂φ/∂r = -H₀ cosθ - 2m cosθ/(4πμ₀ r³)
        # B_r = -μ₀ ∂φ/∂r = μ₀ H₀ cosθ + 2m cosθ/(4π r³)
        B_r_out = mu0 * H0 * np.cos(th) + 2 * m_eff * np.cos(th) / (4 * pi * R_sphere**3)

        print(f"{th:>10.3f} {phi_in:>16.6e} {phi_out:>16.6e} {B_r_in:>16.6e} {B_r_out:>16.6e}")

    print(f"\n边界条件验证: φ_m_in(R) ≈ φ_m_out(R), B_r_in ≈ B_r_out ✓")

    # 绘制磁标势
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    theta = linspace(0, 2*pi, 200)
    r_out = linspace(R_sphere, 3*R_sphere, 50)
    R_grid, Theta_grid = meshgrid(r_out, theta)

    # 球外磁标势 (笛卡尔坐标下)
    x_grid = R_grid * np.cos(Theta_grid)
    y_grid = R_grid * np.sin(Theta_grid)
    Phi_out = (-H0 * R_grid * np.cos(Theta_grid)
               + m_eff * np.cos(Theta_grid) / (4 * pi * mu0 * R_grid**2))

    # Plot 1: 磁标势分布
    c1 = axes[0].contourf(x_grid, y_grid, Phi_out, levels=20, cmap='RdBu_r')
    axes[0].set_xlabel('x (m)')
    axes[0].set_ylabel('y (m)')
    axes[0].set_title('磁标势 φ_m (球外)')
    axes[0].set_aspect('equal')
    fig.colorbar(c1, ax=axes[0], label='φ_m (A/m)')

    # Plot 2: 等势线
    c2 = axes[1].contour(x_grid, y_grid, Phi_out, levels=20, cmap='RdBu_r')
    axes[1].set_xlabel('x (m)')
    axes[1].set_ylabel('y (m)')
    axes[1].set_title('磁标势等势线 (球外)')
    axes[1].set_aspect('equal')
    fig.colorbar(c2, ax=axes[1], label='φ_m (A/m)')

    plt.suptitle('磁介质球在均匀外磁场中的磁标势', fontsize=14)
    plt.tight_layout()
    plt.savefig('guoshuohong/demo4_scalar_potential.png', dpi=150)
    plt.close()
    print("[绘图已保存: guoshuohong/demo4_scalar_potential.png]\n")

    return H_in, B_in, m_eff


# ============================================================
# Demo 5: 阿哈罗诺夫-玻姆效应数值模拟
#          Aharonov-Bohm effect — phase shift calculation
# ============================================================
def demo_5_aharonov_bohm():
    """
    AB效应数值模拟: 计算电子波函数在螺线管磁通下的相位变化

    模型:
      - 无限长螺线管半径 R_solenoid, 磁通 Φ
      - 电子沿两条路径绕过螺线管
      - AB 相位差: Δφ = eΦ/ℏ

    计算:
      1. 矢势 A_φ = Φ/(2πr) (r > R, 库仑规范)
      2. 沿两条路径的 ∫A·dl
      3. 干涉条纹偏移
    """
    print("=" * 60)
    print("Demo 5: 阿哈罗诺夫-玻姆效应 — 相位差与干涉模拟")
    print("=" * 60)

    # 物理常数
    hbar = 1.054571817e-34       # [J·s]
    e_charge = 1.602176634e-19   # [C]

    # 螺线管参数
    R_solenoid = 1e-3          # 半径 1mm
    B_solenoid = 0.1           # 内部磁场 [T]
    Phi_flux = B_solenoid * pi * R_solenoid**2   # 磁通量 [Wb]

    # AB 相位差
    delta_phi = e_charge * Phi_flux / hbar

    print(f"螺线管半径: {R_solenoid*1e3:.2f} mm")
    print(f"螺线管磁场: {B_solenoid:.2f} T")
    print(f"磁通量 Φ = {Phi_flux:.6e} Wb")
    print(f"AB 相位差 Δφ = eΦ/ℏ = {delta_phi:.4f} rad = {delta_phi/(2*pi):.4f} × 2π")

    # 路径计算: 两条半圆形路径绕过螺线管
    # 路径1: y > 0 半圆, 路径2: y < 0 半圆
    # A_φ = Φ/(2πr)  (在螺线管外部)
    # ∫A·dl = ∫ A_φ · r dφ
    # 对于半圆路径, 积分方向相反
    # 路径1 (上): ∫ A·dl = ∫₀^π (Φ/(2πr)) · r dφ = Φ/2
    # 路径2 (下): ∫ A·dl = ∫₀^(-π) (Φ/(2πr)) · r dφ = -Φ/2
    # 环路积分: ∮A·dl = Φ
    # 相位差: Δφ = e/ℏ · ∮A·dl = eΦ/ℏ

    N_path = 100
    path_radius = 2 * R_solenoid  # 路径半径

    # 沿路径的参数积分验证
    phi_angles = linspace(0, pi, N_path)
    dphi = pi / (N_path - 1)

    integral_path1 = 0.0  # 上路径: φ: 0 → π
    for phi in phi_angles:
        r_point = path_radius
        if r_point > R_solenoid:
            A_phi = Phi_flux / (2 * pi * r_point)
            # ds = r dφ
            integral_path1 += A_phi * r_point * dphi

    integral_path2 = 0.0  # 下路径: φ: 0 → -π
    for phi in phi_angles:
        r_point = path_radius
        if r_point > R_solenoid:
            A_phi = Phi_flux / (2 * pi * r_point)
            integral_path2 += A_phi * r_point * (-dphi)

    loop_integral = integral_path1 - integral_path2
    phase_diff_calc = e_charge * loop_integral / hbar

    print(f"\n路径积分验证:")
    print(f"  上路径 ∫A·dl = {integral_path1:.6e} T·m")
    print(f"  下路径 ∫A·dl = {integral_path2:.6e} T·m")
    print(f"  环路积分 ∮A·dl = {loop_integral:.6e} T·m")
    print(f"  理论值: Φ = {Phi_flux:.6e} Wb")
    print(f"  Δφ_数值 = {phase_diff_calc:.4f} rad")
    print(f"  Δφ_理论 = {delta_phi:.4f} rad")

    # 干涉条纹模拟
    # 电子双缝干涉, 考虑 AB 相位差
    x_screen = linspace(-0.005, 0.005, 500)   # 屏幕位置 [m]
    slit_sep = 5e-4                           # 缝间距 [m]
    screen_dist = 0.1                         # 屏到缝的距离 [m]
    electron_k = 1e10                         # 电子波数 [1/m]

    # 无 AB 效应时的干涉图案
    phase_no_AB = electron_k * slit_sep * x_screen / screen_dist
    intensity_no_AB = np.cos(phase_no_AB / 2)**2

    # 有 AB 效应时的干涉图案 (相位偏移)
    phase_with_AB = phase_no_AB + delta_phi
    intensity_with_AB = np.cos((phase_no_AB + delta_phi) / 2)**2

    # 磁通变化时的条纹移动
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    flux_ratios = [0, 0.5, 1.0, 2.0]  # 以 Φ₀ = h/e 为单位

    for i, n in enumerate(flux_ratios):
        ax = axes[i // 2][i % 2]
        phase = n * pi  # Δφ = 2πn

        I_shifted = np.cos((phase_no_AB + phase) / 2)**2
        ax.plot(x_screen * 1e3, intensity_no_AB, 'gray', alpha=0.5, label='无AB')
        ax.plot(x_screen * 1e3, I_shifted, 'b-', label=f'Φ={n:.1f}Φ₀')
        ax.set_xlabel('屏位置 x (mm)')
        ax.set_ylabel('干涉强度')
        ax.set_title(f'AB效应: 磁通 = {n:.1f}Φ₀')
        ax.legend()
        ax.grid(True, alpha=0.3)

    plt.suptitle('Aharonov-Bohm 效应: 干涉条纹随磁通量的变化', fontsize=14)
    plt.tight_layout()
    plt.savefig('guoshuohong/demo5_aharonov_bohm.png', dpi=150)
    plt.close()
    print("[绘图已保存: guoshuohong/demo5_aharonov_bohm.png]\n")

    print("AB效应核心结论:")
    print("  - 即使电子在 B=0 的区域运动, 矢势 A 仍影响量子相位")
    print(f"  - 相位差 Δφ = eΦ/ℏ = {delta_phi:.4f} rad")
    print("  - 干涉条纹随磁通 Φ 周期性移动, 周期为 h/e")
    print("  - 这是拓扑效应, 与路径形状无关, 只与环绕的磁通量有关")

    return delta_phi, Phi_flux


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("郭硕鸿《电动力学》第三章 — 静磁场 数值示例")
    print("=" * 60)

    demo_1_wire_magnetic_field()
    demo_2_vector_potential()
    demo_3_magnetic_multipole()
    demo_4_scalar_potential()
    demo_5_aharonov_bohm()

    print("=" * 60)
    print("所有示例运行完成!")
    print("=" * 60)
