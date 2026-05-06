#!/usr/bin/env python3
"""
chew_mlfma_examples.py
========================
MLFMA 教学示例 — 基于 Chew, Jin, Michielssen, Song
《Fast and Efficient Algorithms in CEM》(Artech House, 2001)

包含:
  1. 格林函数多极展开验证
  2. FMM 1D 聚合-转移-配置演示
  3. 迭代求解(GMRES) vs 直接求解对比
  4. 复杂度分析 (O(N²) vs O(N log N))

依赖: numpy, scipy, matplotlib
"""

import math
import numpy as np
from numpy.linalg import norm
from scipy.special import spherical_jn, spherical_yn, lpmv, eval_legendre, jv, yv
from scipy.sparse.linalg import gmres as scipy_gmres
from scipy.linalg import solve
import time
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ──────────────────────────────────────────────
#  全局样式
# ──────────────────────────────────────────────

plt.rcParams.update({
    "figure.dpi": 120,
    "figure.figsize": (10, 6),
    "font.size": 11,
})

# ──────────────────────────────────────────────
#  工具函数: 球谐函数 + 汉克尔/贝塞尔
# ──────────────────────────────────────────────

def sph_harm(l, m, theta, phi):
    """球谐函数 Y_lm(θ, φ) — 实数归一化版本"""
    if m < 0:
        y = np.sqrt(2) * ((-1)**m) * lpmv(-m, l, np.cos(theta)) * np.sin(-m * phi)
    elif m == 0:
        y = lpmv(0, l, np.cos(theta))
    else:
        y = np.sqrt(2) * ((-1)**m) * lpmv(m, l, np.cos(theta)) * np.cos(m * phi)
    # 归一化因子
    normf = np.sqrt((2 * l + 1) / (4 * np.pi) * math.factorial(l - abs(m)) / math.factorial(l + abs(m)))
    return normf * y


def h2(l, z):
    """第二类球汉克尔函数 h_l^(2)(z) = j_l(z) - j y_l(z)"""
    return spherical_jn(l, z) - 1j * spherical_yn(l, z, derivative=False)


# ──────────────────────────────────────────────
#  示例 1: 格林函数多极展开验证
# ──────────────────────────────────────────────

def example_1_green_multipole():
    """
    验证格林函数的加法定理 (Addition Theorem) 多极展开.

    对于 |r| > |r'|:
        G(r, r') = -jk Σ_l Σ_m h_l^(2)(kr) j_l(kr') Y_lm(θ,φ) Y_lm*(θ',φ')

    比较直接格林函数值与多极展开近似值。
    """
    print("=" * 65)
    print("示例 1: 格林函数多极展开验证")
    print("=" * 65)

    k = 2 * np.pi  # 波长 λ=1
    r_source = np.array([0.3, 0.4, 0.0])  # 源点 (近原点)
    r_field  = np.array([2.0, 1.5, 0.0])  # 场点 (远场)

    # 极坐标
    def cart2sph(v):
        r = norm(v)
        theta = np.arccos(v[2] / r) if r > 0 else 0.0
        phi = np.arctan2(v[1], v[0])
        return r, theta, phi

    rs, ts, ps = cart2sph(r_source)
    rf, tf, pf = cart2sph(r_field)

    # 直接格林函数
    R_vec = r_field - r_source
    R = norm(R_vec)
    G_direct = np.exp(-1j * k * R) / (4 * np.pi * R)

    print(f"  源点   r' = ({r_source[0]:.2f}, {r_source[1]:.2f}, {r_source[2]:.2f})")
    print(f"  场点   r  = ({r_field[0]:.2f}, {r_field[1]:.2f}, {r_field[2]:.2f})")
    print(f"  距离   |r - r'| = {R:.4f}")
    print(f"  直接 G = {G_direct:.6f}")

    print()
    print("  截断阶数 L |  多极展开近似      | 相对误差")
    print("  " + "-" * 55)

    for L in [1, 2, 3, 5, 7, 10, 15, 20]:
        G_mp = 0.0
        for l in range(L + 1):
            for m in range(-l, l + 1):
                term = (h2(l, k * rf) *
                        spherical_jn(l, k * rs) *
                        sph_harm(l, m, tf, pf) *
                        sph_harm(l, m, ts, ps))
                G_mp += term
        G_mp *= -1j * k

        err = abs(G_mp - G_direct) / abs(G_direct)
        print(f"       {L:3d}      |  {G_mp:.6f}     |  {err:.2e}")

    print()
    print("  → 随着 L 增加, 多极展开收敛到精确格林函数值.")
    print()

    return G_direct


# ──────────────────────────────────────────────
#  示例 2: FMM 1D 聚合-转移-配置演示
# ──────────────────────────────────────────────

def example_2_fmm_1d():
    """
    FMM 1D 演示: 使用 Sommerfeld 恒等式作为谱展开,
    通过分组 → 聚合 → 转移 → 配置加速矩阵-向量乘.

    核函数: H_0^(2)(k|x - x'|)  (2D Helmholtz 格林函数在直线上)

    基本恒等式 (Sommerfeld 恒等式):
        H_0^(2)(k|x - x'|) = (1/π) ∫_{-π}^{π} e^{jk cosθ (x - x')} dθ

    FMM 分组策略:
        e^{jk cosθ (x_i - x_j)} =
          e^{jk cosθ (x_i - X_g)}          (配置相位)
        · e^{jk cosθ (X_g - X_{g'})}      (组间转移)
        · e^{jk cosθ (X_{g'} - x_j)}      (聚合相位)
    """
    from scipy.special import hankel2

    print("=" * 65)
    print("示例 2: FMM 1D 聚合-转移-配置演示 (Sommerfeld 恒等式)")
    print("=" * 65)

    # --- 参数 ---
    k = 2 * np.pi          # 波数 (λ=1)
    group_size = 16        # 每组点数
    n_source = 256         # 总源点数
    n_field = n_source
    assert n_source % group_size == 0

    # --- 几何 ---
    x_min, x_max = -5.0, 5.0
    xs = np.linspace(x_min, x_max, n_source)
    xf = np.linspace(x_min, x_max, n_field)

    # --- 源权重 (随机) ---
    np.random.seed(42)
    weights = np.random.randn(n_source) + 0.5j * np.random.randn(n_source)

    # --- 参照: 直接 O(N²) 计算 ---
    print("  计算直接 O(N²) 相互作用 (参照)...")
    t0 = time.perf_counter()
    ref = np.zeros(n_field, dtype=complex)
    for i in range(n_field):
        for j in range(n_source):
            r = abs(xf[i] - xs[j])
            if r > 1e-14:
                ref[i] += hankel2(0, k * r) * weights[j]
    t_direct = time.perf_counter() - t0
    print(f"    耗时: {t_direct:.3f}s")

    # --- 分组 ---
    n_groups = n_source // group_size
    group_centers = np.array([
        xs[g * group_size: (g + 1) * group_size].mean()
        for g in range(n_groups)
    ])

    # --- 角向采样 (用于谱展开) ---
    # 使用高斯-勒让德积分近似 Sommerfeld 积分
    # 对于 1D 无限域, 用梯形法则在 [0, π] 就足够
    n_theta = max(32, 2 * int(1.5 * k * (x_max - x_min) / n_groups) + 4)
    # 使用梯形法则在 [0, π] 上采样
    thetas = np.linspace(0, np.pi, n_theta)
    w_theta = (np.pi / n_theta) * np.ones(n_theta)  # 梯形权重
    # 第一个和最后一个采样的权重减半 (梯形法则)
    w_theta[0] *= 0.5
    w_theta[-1] *= 0.5

    # 预计算所有角度对应的 k_p = k cosθ
    kp_vec = k * np.cos(thetas)

    def fmm_spectral():
        """
        基于 Sommerfeld 谱展开的 FMM 近似.

        将 H_0^(2)(k|x_i - x_j|) 分解为:
            ∫ e^{jk cosθ (x_i - X_g)} · e^{jk cosθ (X_g - X_{g'})}
              · e^{jk cosθ (X_{g'} - x_j)} dθ
        """
        result = np.zeros(n_field, dtype=complex)
        far_threshold = 2.0 * (x_max - x_min) / n_groups

        # ---- 聚合 (Aggregation) ----
        # V_{g'}(θ_p) = Σ_{j∈G_{g'}} w_j · e^{jk cosθ_p (X_{g'} - x_j)}
        V_agg = np.zeros((n_groups, n_theta), dtype=complex)
        for g in range(n_groups):
            j_start = g * group_size
            j_end = (g + 1) * group_size
            Xc = group_centers[g]
            dx = Xc - xs[j_start:j_end]
            for p in range(n_theta):
                phase = np.exp(1j * kp_vec[p] * dx)
                V_agg[g, p] = np.sum(weights[j_start:j_end] * phase)

        # ---- 转移 (Transfer) ----
        # V_g(θ_p) = Σ_{g'}(w_θ_p / π) · e^{jk cosθ_p (X_g - X_{g'})} · V_{g'}(θ_p)
        V_trans = np.zeros_like(V_agg)
        for g_f in range(n_groups):
            for g_s in range(n_groups):
                d = group_centers[g_f] - group_centers[g_s]
                if abs(d) < far_threshold:
                    continue
                for p in range(n_theta):
                    T = (w_theta[p] / np.pi) * np.exp(1j * kp_vec[p] * d)
                    V_trans[g_f, p] += T * V_agg[g_s, p]

        # ---- 配置 (Disaggregation) ----
        # f_i = Σ_p e^{jk cosθ_p (x_i - X_g)} · V_g(θ_p)
        for g in range(n_groups):
            i_start = g * group_size
            i_end = (g + 1) * group_size
            Xc = group_centers[g]
            dx = xf[i_start:i_end] - Xc
            for p in range(n_theta):
                phase = np.exp(1j * kp_vec[p] * dx)
                result[i_start:i_end] += phase * V_trans[g, p]

        # ---- 近场直接修正 ----
        # 对近距离组对 (距离 < far_threshold), 用直接计算替换
        for g_f in range(n_groups):
            for g_s in range(n_groups):
                d = abs(group_centers[g_f] - group_centers[g_s])
                if d >= far_threshold:
                    continue
                i_start = g_f * group_size
                i_end = (g_f + 1) * group_size
                j_start = g_s * group_size
                j_end = (g_s + 1) * group_size
                for i in range(i_start, i_end):
                    # 减去 FMM 近场贡献 (由谱项近似)
                    for p in range(n_theta):
                        T = (w_theta[p] / np.pi) * np.exp(1j * kp_vec[p] * (group_centers[g_f] - group_centers[g_s]))
                        agg = np.sum(weights[j_start:j_end] * np.exp(1j * kp_vec[p] * (group_centers[g_s] - xs[j_start:j_end])))
                        result[i] -= (w_theta[p] / np.pi) * np.exp(1j * kp_vec[p] * (xf[i] - group_centers[g_f])) * T * agg
                    # 加上精确近场
                    for j in range(j_start, j_end):
                        r = abs(xf[i] - xs[j])
                        if r > 1e-14:
                            result[i] += hankel2(0, k * r) * weights[j]

        return result

    print("  执行 Sommerfeld 谱 FMM (聚合-转移-配置)...")
    t0 = time.perf_counter()
    fmm_result = fmm_spectral()
    t_fmm = time.perf_counter() - t0
    print(f"    耗时: {t_fmm:.3f}s")

    # 比较
    rel_err = norm(fmm_result - ref) / norm(ref)
    speedup = t_direct / t_fmm

    print()
    print(f"  直接 O(N²) 误差 (参照): 与自身比较 = 0")
    print(f"  FMM 相对误差:          {rel_err:.4e}")
    print(f"  加速比:                {speedup:.1f}x")
    print(f"  N = {n_source}, 分组 = {n_groups}, 每组 = {group_size}")

    # 可视化
    fig, axes = plt.subplots(2, 1, figsize=(10, 7))

    ax = axes[0]
    ax.plot(xf, ref.real, label="Direct (ref)", lw=1.5, alpha=0.8)
    ax.plot(xf, fmm_result.real, "--", label=f"FMM (ε={rel_err:.2e})", lw=1.5)
    ax.set_xlabel("x")
    ax.set_ylabel("Re[field]")
    ax.set_title("直接计算 vs FMM 近似 (1D Helmholtz 核)")
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    diff = np.abs(ref - fmm_result)
    ax.semilogy(xf, diff, label="|直接 - FMM|", lw=1)
    ax.set_xlabel("x")
    ax.set_ylabel("绝对差")
    ax.set_title(f"误差分布 (相对误差 = {rel_err:.2e})")
    ax.legend()
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig("cem/fig_fmm_1d.png", dpi=150)
    plt.close(fig)
    print("\n  图像: cem/fig_fmm_1d.png\n")

    return rel_err, speedup


# ──────────────────────────────────────────────
#  示例 3: 迭代求解 vs 直接求解
# ──────────────────────────────────────────────

def example_3_iterative_vs_direct():
    """
    对比直接求解 (LU) 与迭代求解 (GMRES) 在
    电场积分方程 (EFIE) 离散化矩阵上的表现.

    构造一个简化模型:
      - 1D PEC 线 (thin wire) 在平面波照射下
      - 使用脉冲基函数 + 点匹配
      - 系统: Z I = V
      - 比较直接求解和 GMRES 的精度和耗时
    """
    from scipy.special import hankel2
    from scipy.linalg import solve as lu_solve
    from scipy.sparse import csr_matrix
    from scipy.sparse.linalg import gmres

    print("=" * 65)
    print("示例 3: 迭代求解 (GMRES) vs 直接求解对比")
    print("=" * 65)

    for N in [64, 128, 256]:
        print(f"\n  --- N = {N} ---")

        # 几何: 沿 x 轴的 PEC 线, 长度 = 2λ
        lam = 1.0
        k = 2 * np.pi  # /lam
        L_wire = 2.0   # 波长
        a = 0.01       # 线半径

        z = np.linspace(-L_wire/2, L_wire/2, N)
        dz = z[1] - z[0]

        # 阻抗矩阵: 脉冲基 + 点匹配 (简化 EFIE 1D 模型)
        Z = np.zeros((N, N), dtype=complex)
        for i in range(N):
            for j in range(N):
                R = np.sqrt((z[i] - z[j])**2 + a**2)
                Z[i, j] = dz * (1 + (1j / (k * R)) * (1 - 1j * k * R)) * \
                          np.exp(-1j * k * R) / (4 * np.pi * R)

        # 激励: 平面波沿 -z 方向
        V = np.exp(1j * k * z)

        # --- 直接求解 ---
        t0 = time.perf_counter()
        I_direct = lu_solve(Z, V)
        t_direct = time.perf_counter() - t0

        # --- GMRES ---
        Z_sparse = csr_matrix(Z)  # 用稀疏矩阵包装 (实际 Z 满, 仅演示)
        t0 = time.perf_counter()
        I_gmres, info = gmres(Z_sparse, V, atol=1e-10, maxiter=500)
        t_gmres = time.perf_counter() - t0

        # 结果
        if info == 0:
            gmres_norm_err = norm(I_gmres - I_direct) / norm(I_direct)
            speedup = t_direct / t_gmres
            print(f"    直接求解: {t_direct:.4f}s | GMRES: {t_gmres:.4f}s")
            print(f"    相对误差: {gmres_norm_err:.2e} | 加速比: {speedup:.1f}x")
        else:
            print(f"    GMRES 未收敛 (info={info})")
            print(f"    直接求解: {t_direct:.4f}s")

    # 大矩阵对比 (N=512 仅矩阵填充, 评估复杂度趋势)
    print(f"\n  --- N = 512 (仅矩阵构建耗时, 不求解) ---")
    N_test = 512
    z = np.linspace(-1, 1, N_test)
    dz = z[1] - z[0]
    a = 0.01
    k = 2 * np.pi

    t0 = time.perf_counter()
    Z_big = np.zeros((N_test, N_test), dtype=complex)
    for i in range(N_test):
        for j in range(N_test):
            R = np.sqrt((z[i] - z[j])**2 + a**2)
            Z_big[i, j] = dz * (1 + (1j / (k * R)) * (1 - 1j * k * R)) * \
                          np.exp(-1j * k * R) / (4 * np.pi * R)
    t_fill = time.perf_counter() - t0
    print(f"    矩阵填充耗时: {t_fill:.3f}s (O(N²))")
    print(f"    矩阵内存: {Z_big.nbytes / 1e6:.1f} MB")

    print()
    print("  结论:")
    print("    • 迭代求解 (GMRES) 避免 O(N³) 的 LU 分解")
    print("    • 大 N 时迭代法的存储和运算量远小于直接法")
    print("    • MLFMA 结合迭代法: 每步 O(N log N) 的矩阵-向量乘")
    print()

    return True


# ──────────────────────────────────────────────
#  示例 4: 复杂度分析
# ──────────────────────────────────────────────

def example_4_complexity():
    """
    MLFMA 复杂度分析: O(N²) vs O(N log N).

    对 2D 散射问题 (简化), 分别测量:
      - 直接 MoM (O(N²) 矩阵填充 + O(N³) 求解)
      - MLFMA 风格: 分组, 每步 O(N log N) 矩阵-向量乘

    通过变化 N, 拟合实际复杂度曲线.
    """
    from scipy.special import hankel2

    print("=" * 65)
    print("示例 4: 复杂度分析 (O(N²) vs O(N log N))")
    print("=" * 65)

    # 设计问题: 2D TMz 散射
    # 圆形 PEC 柱面, 脉冲基 + 点匹配
    # 以此测量矩阵-向量乘的复杂度

    Ns = np.array([32, 64, 128, 256, 512, 1024])
    t_direct = []
    t_fmm_style = []

    k = 2 * np.pi  # λ=1
    a_cyl = 1.0    # 圆柱半径

    for N in Ns:
        # --- 建立几何 ---
        thetas = np.linspace(0, 2*np.pi, N, endpoint=False)
        pts = a_cyl * np.array([np.cos(thetas), np.sin(thetas)]).T

        # --- 直接矩阵-向量乘 O(N²) ---
        # 构造一个随机向量
        np.random.seed(7)
        x = np.random.randn(N) + 1j * np.random.randn(N)

        # 测量一次完整的 MV 时间 (2D EFIE 核)
        # 使用优化的全矩阵 (示意, 不做完整填充)
        if N <= 512:  # N=1024 可能太慢
            t0 = time.perf_counter()
            y_direct = np.zeros(N, dtype=complex)
            for i in range(N):
                for j in range(N):
                    R = norm(pts[i] - pts[j])
                    if R > 1e-14:
                        y_direct[i] += hankel2(0, k * R) * x[j]
            elapsed = time.perf_counter() - t0
            t_direct.append(elapsed)
            print(f"  N={N:5d}  直接 MV: {elapsed:.4f}s")
        else:
            # 对 N=1024 用部分采样推断
            sample_n = 256
            t0 = time.perf_counter()
            for _ in range(3):
                i0 = np.random.randint(0, N)
                for j in range(N):
                    R = norm(pts[i0] - pts[j])
                    if R > 1e-14:
                        _ = hankel2(0, k * R) * x[j]
            elapsed = time.perf_counter() - t0
            scale = (N - 1) / (3 * sample_n)  # 粗估
            # 省略列维估计, 谨慎插值
            est = elapsed * N / 3
            t_direct.append(est)
            print(f"  N={N:5d}  直接 MV: ~{est:.2f}s (外推)")

        # --- FMM 风格: 分组 + 远场近似 O(N log N) ---
        # 分组
        M = int(np.sqrt(N))  # 分 √N 组, 每组 ~√N 点
        M = max(M, 2)
        if M > N:
            M = N
        group_size = N // M
        if group_size < 1:
            group_size = 1
            M = N
        if M * group_size != N:
            # 调整
            M = int(np.ceil(np.sqrt(N)))
            group_size = max(1, N // M)
            M = N // group_size
            if M * group_size != N:
                group_size = max(1, N // 10)
                M = N // group_size

        groups = np.array_split(np.arange(N), M)
        centers = np.array([pts[grp].mean(axis=0) for grp in groups])
        L_modes = max(4, int(5 + np.sqrt(N)))  # 模式数

        # FMM 单步 (简化实现: 聚合 → 转移 → 配置)
        t0 = time.perf_counter()
        y_fmm = np.zeros(N, dtype=complex)

        # Aggregation
        V_agg = np.zeros((M, L_modes), dtype=complex)
        for g in range(M):
            idx = groups[g]
            for p in range(L_modes):
                # 简化: 近似方向
                theta_p = 2 * np.pi * p / L_modes
                k_vec = k * np.array([np.cos(theta_p), np.sin(theta_p)])
                phase = np.exp(1j * (pts[idx] @ k_vec))
                V_agg[g, p] = np.sum(x[idx] * phase)

        # Transfer
        V_trans = np.zeros_like(V_agg)
        far_threshold = 3 * a_cyl / np.sqrt(M)  # 自适应阈值
        for g_f in range(M):
            for g_s in range(M):
                d_ij = norm(centers[g_f] - centers[g_s])
                if d_ij < far_threshold:
                    continue
                # 简化平移算子
                T_val = hankel2(0, k * d_ij)
                for p in range(L_modes):
                    V_trans[g_f, p] += T_val * V_agg[g_s, p]

        # Disaggregation
        for g in range(M):
            idx = groups[g]
            cf = centers[g]
            for p in range(L_modes):
                theta_p = 2 * np.pi * p / L_modes
                k_vec = k * np.array([np.cos(theta_p), np.sin(theta_p)])
                phase = np.exp(-1j * (pts[idx] @ k_vec))
                y_fmm[idx] += V_trans[g, p] * phase

        # 近场 (同组 + 相邻组)
        for g_f in range(M):
            for g_s in range(M):
                d_ij = norm(centers[g_f] - centers[g_s])
                if d_ij >= far_threshold:
                    continue
                i_idx = groups[g_f]
                j_idx = groups[g_s]
                for ii in i_idx:
                    for jj in j_idx:
                        R = norm(pts[ii] - pts[jj])
                        if R > 1e-14:
                            y_fmm[ii] += hankel2(0, k * R) * x[jj]

        elapsed_fmm = time.perf_counter() - t0
        t_fmm_style.append(elapsed_fmm)
        print(f"       FMM 风格 MV: {elapsed_fmm:.4f}s")

    print()
    print("  复杂度拟合:")

    # 只对 N ≤ 256 做直接法的准确拟合
    valid_direct = [(n, t) for n, t in zip(Ns, t_direct) if n <= 512]
    if len(valid_direct) >= 3:
        ns_d, ts_d = zip(*valid_direct)
        coeff_n2 = np.polyfit(np.log(ns_d), np.log(ts_d), 1)
        print(f"    直接法斜率系数: {coeff_n2[0]:.2f} (理论 O(N²): 2.0)")

    valid_fmm = [(n, t) for n, t in zip(Ns, t_fmm_style) if n <= 1024]
    if len(valid_fmm) >= 3:
        ns_f, ts_f = zip(*valid_fmm)
        coeff_nlogn = np.polyfit(np.log(ns_f), np.log(ts_f), 1)
        print(f"    FMM 风格斜率系数: {coeff_nlogn[0]:.2f} (理论 O(N log N): ~1.0-1.1)")

    # 可视化
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    ns_plot = [n for n in Ns]
    ts_d_plot = [t for n, t in zip(Ns, t_direct)]
    ts_f_plot = [t for n, t in zip(Ns, t_fmm_style)]

    ax.loglog(ns_plot[:len(ts_d_plot)], ts_d_plot, "o-", lw=2,
              label="Direct MV (O(N²))")
    ax.loglog(ns_plot, ts_f_plot, "s-", lw=2,
              label="FMM-style MV (O(N log N))")

    # 理论线
    n_theory = np.logspace(np.log10(30), np.log10(1100), 100)
    # O(N²) reference
    if ts_d_plot:
        c_n2 = ts_d_plot[0] / (ns_plot[0] ** 2)
        ax.loglog(n_theory, c_n2 * n_theory ** 2, ":", color="gray",
                  alpha=0.5, label="O(N²) ref")
    # O(N log N) reference
    if ts_f_plot:
        c_nlogn = ts_f_plot[0] / (ns_plot[0] * np.log(ns_plot[0]))
        ax.loglog(n_theory, c_nlogn * n_theory * np.log(n_theory), "--",
                  color="gray", alpha=0.5, label="O(N log N) ref")

    ax.set_xlabel("N (未知数)")
    ax.set_ylabel("矩阵-向量乘耗时 (s)")
    ax.set_title("复杂度对比: 直接 MoM vs MLFMA 风格 MV")
    ax.legend()
    ax.grid(True, which="both", alpha=0.3)

    fig.tight_layout()
    fig.savefig("cem/fig_complexity.png", dpi=150)
    plt.close(fig)
    print("  图像: cem/fig_complexity.png")

    # 总结表
    print()
    print("  复杂度总结:")
    print("  " + "-" * 55)
    print(f"  {'方法':<20} {'复杂度':<15} {'N=1000':<20}")
    print("  " + "-" * 55)
    print(f"  {'直接 MoM (填充)':<20} {'O(N²)':<15} {'~1e6':<20}")
    print(f"  {'直接 MoM (求解)':<20} {'O(N³)':<15} {'~1e9':<20}")
    print(f"  {'FMM单层':<20} {'O(N¹·⁵)':<15} {'~3e4':<20}")
    print(f"  {'MLFMA多层':<20} {'O(N log N)':<15} {'~3e3':<20}")
    print("  " + "-" * 55)
    print()

    return True


# ──────────────────────────────────────────────
#  main
# ──────────────────────────────────────────────

def main():
    print()
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║   Chew, Jin, Michielssen, Song — MLFMA 教学演示          ║")
    print("║   《Fast and Efficient Algorithms in CEM》               ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    print()

    example_1_green_multipole()
    example_2_fmm_1d()
    example_3_iterative_vs_direct()
    example_4_complexity()

    print("=" * 65)
    print("所有示例完成.")
    print("输出图像: cem/fig_fmm_1d.png, cem/fig_complexity.png")
    print("=" * 65)


if __name__ == "__main__":
    main()
