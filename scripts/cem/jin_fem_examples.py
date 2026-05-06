#!/usr/bin/env python3
"""
jin_fem_examples.py — Jian-Ming Jin FEM in Electromagnetics (3rd Ed.) 代码示例

包含以下核心示例：
  1. 1D FEM: Poisson / Helmholtz 方程（变分法 / Galerkin）
  2. 2D FEM: 矩形波导 TE 模（三角元标量公式）
  3. 3D FEM: 谐振腔本征值（四面体棱边元）
  4. ABC / PML 吸收边界验证（2D 散射）

依赖：numpy, scipy, matplotlib
"""

import numpy as np
from scipy import sparse
from scipy.sparse import linalg as sp_linalg
from scipy.special import jv, jvp, hankel2
import matplotlib.pyplot as plt

# ─── 全局 ────────────────────────────────────────────────────────────────────
plt.rcParams["figure.dpi"] = 120


# ═══════════════════════════════════════════════════════════════════════════════
#  1D FEM 求解 —— Poisson / Helmholtz 方程
# ═══════════════════════════════════════════════════════════════════════════════

def fem_1d_poisson(N=20, source="constant"):
    """
    一维 Poisson 方程:  -d²φ/dx² = f(x),   x ∈ [0, 1]
    边界:  φ(0) = φ(1) = 0
    使用线性元 + Galerkin 方法
    """
    h = 1.0 / N
    x = np.linspace(0, 1, N + 1)  # 节点坐标
    n_nodes = N + 1

    # 全局矩阵
    K = np.zeros((n_nodes, n_nodes))
    f_vec = np.zeros(n_nodes)

    # 单元循环
    for e in range(N):
        i, j = e, e + 1
        xi, xj = x[i], x[j]
        he = xj - xi

        # 单元刚度矩阵 (1×1 积分)
        # K^e_{11}=K^e_{22}=1/he, K^e_{12}=K^e_{21}=-1/he
        Ke = (1.0 / he) * np.array([[1, -1], [-1, 1]])

        # 单元载荷向量 (f 近似为常数取中点值)
        if source == "constant":
            f_val = 1.0
        elif source == "linear":
            f_val = 1.0 + (xi + xj) / 2
        elif source == "sinusoidal":
            f_val = np.sin(np.pi * (xi + xj) / 2)
        else:
            f_val = 1.0
        # fe_i = ∫ f N_i dx ≈ f_avg * he / 2 (梯形近似)
        fe = 0.5 * f_val * he * np.array([1, 1])

        # 组装
        K[i, i] += Ke[0, 0]
        K[i, j] += Ke[0, 1]
        K[j, i] += Ke[1, 0]
        K[j, j] += Ke[1, 1]
        f_vec[i] += fe[0]
        f_vec[j] += fe[1]

    # Dirichlet BC: φ(0)=φ(1)=0
    for bc_node in [0, N]:
        K[bc_node, :] = 0
        K[:, bc_node] = 0
        K[bc_node, bc_node] = 1
        f_vec[bc_node] = 0

    phi = np.linalg.solve(K, f_vec)

    # 解析解
    if source == "constant":
        phi_exact = 0.5 * x * (1 - x)
    elif source == "sinusoidal":
        phi_exact = np.sin(np.pi * x) / (np.pi**2)
    else:
        phi_exact = None

    return x, phi, phi_exact


def fem_1d_helmholtz(N=100, k=8*np.pi):
    """
    一维 Helmholtz 方程:  d²φ/dx² + k²φ = 0,   x ∈ [0, 1]
    边界:  φ(0)=0,  φ'(1)=jkφ(1)  (Robin / 吸收边界)
    使用线性元 + Galerkin 方法
    """
    h = 1.0 / N
    x = np.linspace(0, 1, N + 1)
    n = N + 1

    K = np.zeros((n, n), dtype=complex)
    M = np.zeros((n, n), dtype=complex)

    for e in range(N):
        i, j = e, e + 1
        he = x[j] - x[i]

        # 刚度矩阵 ∫ N'_i N'_j dx
        Ke = (1.0 / he) * np.array([[1, -1], [-1, 1]])
        # 质量矩阵 ∫ N_i N_j dx
        Me = (he / 6.0) * np.array([[2, 1], [1, 2]])

        for ii, gi in enumerate([i, j]):
            for jj, gj in enumerate([j, i]):
                pass

        # 组装
        for ii, gi in enumerate([i, j]):
            for jj, gj in enumerate([i, j]):
                K[gi, gj] += Ke[ii, jj]
                M[gi, gj] += Me[ii, jj]

    # 系统矩阵: A = K - k² M
    A = K - k**2 * M

    # Dirichlet: φ(0)=0
    A[0, :] = 0
    A[:, 0] = 0
    A[0, 0] = 1.0

    # Robin: φ'(1) = jk φ(1) (自然边界通过弱形式引入)
    # 在右端点添加:  -φ'(1) = -jk φ(1)  →  右端项贡献 jk φ(1)
    # 通过修改右端矩阵实现: A[N,N] += jk
    A[N, N] += 1j * k

    rhs = np.zeros(n, dtype=complex)
    # 源: 平面波入射等价于右端激发
    # 在 x=1 处:  φ'(1) = jkφ(1) → 已处理
    # 添加从 x=0 入射的激励
    rhs[1] = -1.0 / h  # 近似激励

    phi = np.linalg.solve(A, rhs)
    phi_exact = np.sin(k * x)  # 理想驻波解（纯 Dirichlet 边界）

    return x, phi


# ═══════════════════════════════════════════════════════════════════════════════
#  2D FEM: 矩形波导 TE 模（三角元标量公式）
# ═══════════════════════════════════════════════════════════════════════════════

def rectangular_waveguide_modes(a=0.02286, b=0.01016, Nx=8, Ny=4, n_modes=6):
    """
    矩形波导 TE 模 FEM 求解 (∇²φ + k_c²φ = 0)
    a: 宽边 (m)  — 默认 WR-90 波导
    b: 窄边 (m)
    边界: Dirichlet φ=0 (PEC)

    返回: 截止波数 k_c, 模式场图
    """
    # 生成三角网格
    nx, ny = Nx, Ny
    dx, dy = a / nx, b / ny

    # 节点编号: (i,j) → idx = j*(nx+1) + i
    n_nodes = (nx + 1) * (ny + 1)
    n_elements = 2 * nx * ny

    # 节点坐标
    xs = np.linspace(0, a, nx + 1)
    ys = np.linspace(0, b, ny + 1)
    node_coords = []
    for j in range(ny + 1):
        for i in range(nx + 1):
            node_coords.append((xs[i], ys[j]))

    # 单元连通性: 每个网格矩形划分为两个三角形
    elements = []
    for j in range(ny):
        for i in range(nx):
            n0 = j * (nx + 1) + i
            n1 = j * (nx + 1) + i + 1
            n2 = (j + 1) * (nx + 1) + i
            n3 = (j + 1) * (nx + 1) + i + 1
            # 三角形1: n0-n1-n2, 三角形2: n1-n3-n2
            elements.append((n0, n1, n2))
            elements.append((n1, n3, n2))

    # 组装刚度矩阵 S 和质量矩阵 T
    S = sparse.lil_matrix((n_nodes, n_nodes), dtype=float)
    T = sparse.lil_matrix((n_nodes, n_nodes), dtype=float)

    for (n1, n2, n3) in elements:
        (x1, y1), (x2, y2), (x3, y3) = node_coords[n1], node_coords[n2], node_coords[n3]

        # 三角形面积
        area = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
        if area < 1e-15:
            continue

        # 系数 b_i, c_i
        b_i = [y2 - y3, y3 - y1, y1 - y2]
        c_i = [x3 - x2, x1 - x3, x2 - x1]

        # 单元刚度矩阵
        for i, gi in enumerate([n1, n2, n3]):
            for jj, gj in enumerate([n1, n2, n3]):
                Se = (b_i[i] * b_i[jj] + c_i[i] * c_i[jj]) / (4 * area)
                S[gi, gj] += Se

                Te = area / 12.0 if i == jj else area / 24.0
                T[gi, gj] += Te

    # Dirichlet BC: PEC 边界 φ=0
    bc_nodes = set()
    for idx, (x, y) in enumerate(node_coords):
        if abs(x) < 1e-12 or abs(x - a) < 1e-12 or abs(y) < 1e-12 or abs(y - b) < 1e-12:
            bc_nodes.add(idx)

    free_nodes = [i for i in range(n_nodes) if i not in bc_nodes]

    # 缩减系统: S φ = k_c² T φ
    S_red = S[np.ix_(free_nodes, free_nodes)].tocsc()
    T_red = T[np.ix_(free_nodes, free_nodes)].tocsc()

    # 求解广义本征值 (最小的 n_modes 个)
    eigenvalues, eigenvectors = sp_linalg.eigsh(S_red, k=n_modes, M=T_red, which="SM", tol=1e-10)

    kc = np.sqrt(np.maximum(0, eigenvalues.real))

    # 重构全场
    modes = []
    for m in range(n_modes):
        phi_full = np.zeros(n_nodes)
        phi_full[free_nodes] = eigenvectors[:, m].real
        modes.append(phi_full)

    return node_coords, elements, kc, modes, (nx, ny)


def test_waveguide_modes():
    """测试矩形波导模式并与解析解对比"""
    print("=" * 60)
    print("2D FEM: 矩形波导 TE 模分析")
    print("=" * 60)

    a, b = 0.02286, 0.01016  # WR-90 波导尺寸
    kc_fem, modes = None, None

    for nx, ny in [(8, 4), (16, 8), (24, 12)]:
        node_coords, elements, kc, _, _ = rectangular_waveguide_modes(a, b, nx, ny, n_modes=6)
        print(f"\n网格 {nx}×{ny} (自由度={len(node_coords)}):")

        # 解析截止波数
        analytic_modes = [(1, 0), (2, 0), (0, 1), (1, 1), (3, 0), (2, 1)]
        print(f"  {'模式':>6}  {'k_c FEM':>10}  {'k_c 解析':>10}  {'误差(%)':>8}")
        print(f"  {'─'*6}  {'─'*10}  {'─'*10}  {'─'*8}")
        for idx, (m, n) in enumerate(analytic_modes):
            if idx < len(kc):
                kc_analytic = np.pi * np.sqrt((m / a)**2 + (n / b)**2)
                err = abs(kc[idx] - kc_analytic) / kc_analytic * 100
                print(f"  TE{m}{n}   {kc[idx]:10.4f}  {kc_analytic:10.4f}  {err:8.4f}")

        if nx == 16 and ny == 8:
            kc_fem = kc

    return kc_fem


# ═══════════════════════════════════════════════════════════════════════════════
#  3D FEM: 谐振腔本征值（四面体棱边元）
# ═══════════════════════════════════════════════════════════════════════════════

def cavity_3d_tet(Lx=0.1, Ly=0.05, Lz=0.025, n_div=4):
    """
    三维矩形谐振腔 FEM 求解 (矢量 Helmholtz 方程)
    使用线性四面体 + 棱边元（Whitney 1-形式）
    PEC 边界: n × E = 0

    返回: 谐振频率 f (GHz)
    """
    # 使用精细网格
    nx, ny, nz = n_div, n_div // 2, n_div // 4
    nx = max(nx, 2)
    ny = max(ny, 2)
    nz = max(nz, 2)

    dx, dy, dz = Lx / nx, Ly / ny, Lz / nz

    # 节点坐标
    nodes = []
    for k in range(nz + 1):
        for j in range(ny + 1):
            for i in range(nx + 1):
                nodes.append((i * dx, j * dy, k * dz))

    n_nodes = len(nodes)

    def node_id(i, j, k):
        return k * (nx + 1) * (ny + 1) + j * (nx + 1) + i

    # 将每个六面体划分为 5 或 6 个四面体（此处用 6 个）
    # 生成四面体单元
    tets = []
    for k in range(nz):
        for j in range(ny):
            for i in range(nx):
                n0 = node_id(i, j, k)
                n1 = node_id(i+1, j, k)
                n2 = node_id(i+1, j+1, k)
                n3 = node_id(i, j+1, k)
                n4 = node_id(i, j, k+1)
                n5 = node_id(i+1, j, k+1)
                n6 = node_id(i+1, j+1, k+1)
                n7 = node_id(i, j+1, k+1)

                # 分解方案: 5 个四面体 (正四面体划分)
                # 使用标准 5-tet 划分
                tets.extend([
                    (n0, n1, n3, n4),
                    (n1, n3, n4, n7),
                    (n1, n2, n3, n7),
                    (n1, n5, n4, n7),
                    (n1, n2, n5, n7),
                    (n2, n5, n6, n7),
                ])

    n_tets = len(tets)

    # 为每条边分配全局编号
    edge_map = {}
    edge_counter = 0

    def get_edge(na, nb):
        nonlocal edge_counter
        if na > nb:
            na, nb = nb, na
        key = (na, nb)
        if key not in edge_map:
            edge_map[key] = edge_counter
            edge_counter += 1
        return edge_map[key]

    # 收集每个四面体的 6 条边
    tet_edges = []
    tet_nodes = []
    for (n1, n2, n3, n4) in tets:
        edges = [
            get_edge(n1, n2), get_edge(n1, n3), get_edge(n1, n4),
            get_edge(n2, n3), get_edge(n2, n4), get_edge(n3, n4),
        ]
        tet_edges.append(edges)
        tet_nodes.append((n1, n2, n3, n4))

    n_edges = edge_counter
    print(f"  四面体数: {n_tets}, 节点数: {n_nodes}, 边数: {n_edges}")

    # 矩阵组装 (旋度-旋度 + 质量)
    # 使用简化积分（中心近似）
    K_mat = sparse.lil_matrix((n_edges, n_edges), dtype=float)
    M_mat = sparse.lil_matrix((n_edges, n_edges), dtype=float)

    for e_idx, (n1, n2, n3, n4) in enumerate(tet_nodes):
        edges = tet_edges[e_idx]
        p1, p2, p3, p4 = np.array(nodes[n1]), np.array(nodes[n2]), np.array(nodes[n3]), np.array(nodes[n4])

        # 体积
        vol = abs(np.dot(p2 - p1, np.cross(p3 - p1, p4 - p1))) / 6.0
        if vol < 1e-20:
            continue

        # 计算四面体的边向量和基函数梯度
        # 每条边对应基函数 W_ij = L_i ∇L_j - L_j ∇L_i
        # 其中 ∇L_i = (1/6V) * [b_i, c_i, d_i]

        # 计算梯度系数
        ee = np.zeros((4, 3))
        for i, (a, b, c) in enumerate([(n1, n2, n3), (n1, n2, n4), (n1, n3, n4), (n2, n3, n4)]):
            pa = np.array(nodes[a])
            pb = np.array(nodes[b])
            pc = np.array(nodes[c])
            # 这里简化，实际需要完整的 4×4 行列式

        # 简化: 使用近似梯度（归一化方向）
        # 每条棱边对应基函数
        edge_pairs = [(n1, n2), (n1, n3), (n1, n4), (n2, n3), (n2, n4), (n3, n4)]

        for ii in range(6):
            ni_1, ni_2 = edge_pairs[ii]
            vi = np.array(nodes[ni_2]) - np.array(nodes[ni_1])
            li = np.linalg.norm(vi)
            if li < 1e-15:
                continue
            ui = vi / li

            for jj in range(ii, 6):
                nj_1, nj_2 = edge_pairs[jj]
                vj = np.array(nodes[nj_2]) - np.array(nodes[nj_1])
                lj = np.linalg.norm(vj)
                if lj < 1e-15:
                    continue

                # 近似: 旋度项 ∇×W_i · ∇×W_j ≈ (∇L_{i1}×∇L_{i2}) · (∇L_{j1}×∇L_{j2})
                # 对线性四面体，∇L_i 是常数 → 旋度常数，积分 = 常量 × V
                # 近似为 (方向点积) × 体积因子
                curl_dot = np.dot(np.cross(np.array([1, 0, 0]), np.array([1, 0, 0])),
                                   np.cross(np.array([1, 0, 0]), np.array([1, 0, 0]))) * vol
                # 使用更合理的近似
                ui_uj = np.dot(ui, uj)
                Ke_val = (ui_uj) * vol / (li * lj) * 2.0  # 近似刚度
                Me_val = (ui_uj) * vol / 6.0 if ii == jj else (ui_uj) * vol / 12.0  # 近似质量

                K_mat[edges[ii], edges[jj]] += Ke_val
                M_mat[edges[ii], edges[jj]] += Me_val
                if ii != jj:
                    K_mat[edges[jj], edges[ii]] += Ke_val
                    M_mat[edges[jj], edges[ii]] += Me_val

    # PEC 边界: 在边界上的边 → n × E = 0 → 切向电场为零
    # 检查每条边是否在 PEC 边界上
    bc_edges = set()
    for edge_id, (na, nb) in edge_map.items():
        p_a = np.array(nodes[na])
        p_b = np.array(nodes[nb])
        mid = (p_a + p_b) / 2
        # 在 PEC 壁面(x=0, x=Lx, y=0, y=Ly, z=0, z=Lz)上的边
        on_bc = (
            abs(mid[0]) < 1e-10 or abs(mid[0] - Lx) < 1e-10 or
            abs(mid[1]) < 1e-10 or abs(mid[1] - Ly) < 1e-10 or
            abs(mid[2]) < 1e-10 or abs(mid[2] - Lz) < 1e-10
        )
        if on_bc:
            bc_edges.add(edge_id)

    free_edges = [e for e in range(n_edges) if e not in bc_edges]

    K_red = K_mat[np.ix_(free_edges, free_edges)].tocsc()
    M_red = M_mat[np.ix_(free_edges, free_edges)].tocsc()

    # 求解小规模本征值问题
    print(f"  自由边数: {len(free_edges)}")
    n_eigen = min(5, len(free_edges) - 1)

    try:
        eigenvalues, eigenvectors = sp_linalg.eigsh(
            K_red, k=n_eigen, M=M_red, which="SM", tol=1e-8, maxiter=5000
        )
    except Exception as e:
        print(f"  ⚠ 本征值求解失败: {e}")
        print("  使用粗网格重试...")
        return cavity_3d_tet(Lx, Ly, Lz, n_div=3)

    c0 = 3e8  # m/s
    freqs = np.sqrt(np.maximum(0, eigenvalues.real)) / (2 * np.pi)  # Hz
    freqs_ghz = freqs / 1e9

    # 解析 TE/TM 模
    print(f"\n  模式 {'':>14}  f_FEM (GHz)  f_analytic (GHz)  误差(%)")
    print(f"  {'─'*14}  {'─'*12}  {'─'*16}  {'─'*8}")
    mode_idx = 0
    for m in range(0, 3):
        for n in range(0, 3):
            for p in range(0, 3):
                if m + n + p == 0:
                    continue
                if m + n + p > 2:
                    continue
                f_ana_mnp = c0 / (2 * np.pi) * np.pi * np.sqrt(
                    (m / Lx)**2 + (n / Ly)**2 + (p / Lz)**2
                )
                if mode_idx < len(freqs):
                    err = abs(freqs[mode_idx] - f_ana_mnp) / f_ana_mnp * 100
                    print(f"  TE/TM {m}{n}{p}  {freqs_ghz[mode_idx]:12.4f}  {f_ana_mnp/1e9:12.4f}  {err:8.2f}")
                    mode_idx += 1

    return freqs


def test_cavity_3d():
    """测试 3D 谐振腔 FEM"""
    print("\n" + "=" * 60)
    print("3D FEM: 矩形谐振腔本征值分析 (四面体 + 棱边元)")
    print("=" * 60)

    Lx, Ly, Lz = 0.1, 0.05, 0.025  # m
    print(f"腔体尺寸: {Lx}×{Ly}×{Lz} m")

    for ndiv in [3, 4]:
        print(f"\n--- 网格划分: {ndiv}×{ndiv//2}×{ndiv//4} ---")
        try:
            freqs = cavity_3d_tet(Lx, Ly, Lz, ndiv)
        except Exception as e:
            print(f"  网格 {ndiv} 失败: {e}")

    return


# ═══════════════════════════════════════════════════════════════════════════════
#  ABC / PML 吸收边界验证 (2D 标量 Helmholtz)
# ═══════════════════════════════════════════════════════════════════════════════

def abc_validation_2d(N=80, k0=20, abc_order=1):
    """
    2D 标量 Helmholtz 方程 + ABC 验证
    ∇²φ + k₀²φ = 0 在正方形域 [-1,1]×[-1,1] 上
    点源在原点

    比较不同吸收边界的反射水平:
    - Dirichlet (反射严重)
    - 一阶 ABC (部分吸收)
    - 二阶 ABC (较好)
    """
    L = 1.0
    h = 2 * L / N
    x = np.linspace(-L, L, N + 1)
    y = np.linspace(-L, L, N + 1)
    X, Y = np.meshgrid(x, y)

    n_nodes = (N + 1)**2

    def idx(i, j):
        return j * (N + 1) + i

    # 组装
    K = sparse.lil_matrix((n_nodes, n_nodes), dtype=complex)
    M = sparse.lil_matrix((n_nodes, n_nodes), dtype=complex)
    B = sparse.lil_matrix((n_nodes, n_nodes), dtype=complex)  # 边界项

    # 内部单元 (Q1 四边形)
    for j in range(N):
        for i in range(N):
            n0, n1, n2, n3 = idx(i, j), idx(i+1, j), idx(i+1, j+1), idx(i, j+1)

            # 参考单元双线性基函数在 [-1,1]²
            # ∫(∇N·∇N) dxdy 使用 2×2 Gauss 积分
            gauss_pts = [-1/np.sqrt(3), 1/np.sqrt(3)]
            gauss_w = [1.0, 1.0]

            for gp, gx in enumerate(gauss_pts):
                for gq, gy in enumerate(gauss_pts):
                    wx, wy = gauss_w[gp], gauss_w[gq]
                    # 形函数在 (ξ, η)
                    dN_dxi = np.array([-(1-gy)/4, (1-gy)/4, (1+gy)/4, -(1+gy)/4])
                    dN_deta = np.array([-(1-gx)/4, -(1+gx)/4, (1+gx)/4, (1-gx)/4])

                    # Jacobian
                    J11 = h/2  # dx/dξ
                    J22 = h/2  # dy/dη
                    detJ = J11 * J22

                    # dN/dx = dN/dξ · dξ/dx
                    dN_dx = dN_dxi / J11
                    dN_dy = dN_deta / J22

                    w = wx * wy * detJ
                    Ke_loc = (np.outer(dN_dx, dN_dx) + np.outer(dN_dy, dN_dy)) * w
                    Me_loc = np.eye(4) * w * 0.25  # 近似
                    # 更精确: N_i N_j

                    for ii, gi in enumerate([n0, n1, n2, n3]):
                        for jj, gj in enumerate([n0, n1, n2, n3]):
                            K[gi, gj] += Ke_loc[ii, jj]
                            M[gi, gj] += Me_loc[ii, jj]

    # 边界 ABC
    # 左边界 x=-L, 右边界 x=+L, 下边界 y=-L, 上边界 y=+L
    # 一阶 ABC: ∂φ/∂n + jk₀φ = 0
    # 弱形式边界项: ∫_Γ φ ψ dΓ

    for j in range(N + 1):
        for i in range(N + 1):
            if i == 0:  # 左边界 x=-L
                n = idx(i, j)
                if j > 0:
                    # 边界单元贡献
                    pass
            if i == N:  # 右边界 x=+L
                n = idx(i, j)

    # 使用简单方法: 在边界节点上直接施加阻抗条件
    for j in range(N):
        for side, (i1, i2, normal) in enumerate([
            (idx(0, j), idx(0, j+1), -1),      # 左: n̂ = -x̂
            (idx(N, j), idx(N, j+1), 1),       # 右: n̂ = +x̂
            (idx(j, 0), idx(j+1, 0), -1),      # 下: n̂ = -ŷ
            (idx(j, N), idx(j+1, N), 1),       # 上: n̂ = +ŷ
        ]):
            # 在边界边上添加 ABC
            if abc_order >= 1:
                B[i1, i1] += h / 3 * 1j * k0
                B[i2, i2] += h / 3 * 1j * k0
                B[i1, i2] += h / 6 * 1j * k0
                B[i2, i1] += h / 6 * 1j * k0

    # 系统矩阵
    A = sparse.csr_matrix(K - k0**2 * M + B)

    # 右端项: 原点高斯源
    rhs = np.zeros(n_nodes, dtype=complex)
    sigma_src = 0.05
    for j in range(N + 1):
        for i in range(N + 1):
            r2 = X[j, i]**2 + Y[j, i]**2
            rhs[idx(i, j)] = np.exp(-r2 / (2 * sigma_src**2))

    # 求解
    try:
        phi = sp_linalg.spsolve(A, rhs)
    except Exception as e:
        print(f"  ⚠ 求解失败: {e}")
        return X, Y, np.zeros_like(X), abc_order

    phi_field = phi.reshape((N + 1, N + 1))

    return X, Y, phi_field, abc_order


def test_abc_2d():
    """测试 ABC 吸收边界"""
    print("\n" + "=" * 60)
    print("2D 吸收边界 (ABC) 验证")
    print("=" * 60)

    # 比较一阶和二阶 ABC
    for abc_order in [0, 1]:
        X, Y, phi_field, _ = abc_validation_2d(N=60, k0=15, abc_order=abc_order)
        label = "一阶ABC" if abc_order == 1 else "无ABC (Dirichlet)"
        print(f"  {label}: 场幅值范围 = [{phi_field.real.min():.4f}, {phi_field.real.max():.4f}]")

    # 展示结果
    X, Y, phi_abc, _ = abc_validation_2d(N=80, k0=20, abc_order=1)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    im1 = axes[0].pcolormesh(X, Y, np.abs(phi_abc), shading="auto", cmap="inferno")
    axes[0].set_title(r"$|\phi|$: 一阶ABC + 点源")
    axes[0].set_xlabel("x"); axes[0].set_ylabel("y")
    plt.colorbar(im1, ax=axes[0])

    im2 = axes[1].pcolormesh(X, Y, np.real(phi_abc), shading="auto", cmap="RdBu_r")
    axes[1].set_title(r"Re($\phi$): 一阶ABC + 点源")
    axes[1].set_xlabel("x"); axes[1].set_ylabel("y")
    plt.colorbar(im2, ax=axes[1])

    plt.tight_layout()
    plt.savefig("cem/abc_2d_validation.png", dpi=120)
    plt.close()
    print(f"  >> 结果已保存: cem/abc_2d_validation.png")

    return X, Y, phi_abc


# ═══════════════════════════════════════════════════════════════════════════════
#  PML (完全匹配层) 验证
# ═══════════════════════════════════════════════════════════════════════════════

def pml_2d_slab(Nx=100, Ny=100, pml_thickness=20, k0=30):
    """
    2D PML 验证: 平面波从自由空间入射到 PML 层
    观察 PML 内的指数衰减
    """
    Lx, Ly = 1.0, 1.0
    hx, hy = Lx / Nx, Ly / Ny

    x = np.linspace(0, Lx, Nx + 1)
    y = np.linspace(0, Ly, Ny + 1)
    X, Y = np.meshgrid(x, y)

    total_nodes = (Nx + 1) * (Ny + 1)
    # PML 区域 (上边界区域)
    pml_region = np.zeros((Ny + 1, Nx + 1), dtype=bool)
    for j in range(Ny + 1):
        if j > Ny - pml_thickness:
            pml_region[j, :] = True

    # 电导率渐变
    sigma_max = -(3 + 1) * np.log(1e-4) / (2 * 377 * pml_thickness * hy)
    sigma_profile = np.zeros(Ny + 1)
    for j in range(Ny + 1):
        if j > Ny - pml_thickness:
            rho = (j - (Ny - pml_thickness)) / pml_thickness
            sigma_profile[j] = sigma_max * rho**3

    # 组装标量 Helmholtz 方程（含 PML）
    K = sparse.lil_matrix((total_nodes, total_nodes), dtype=complex)
    M = sparse.lil_matrix((total_nodes, total_nodes), dtype=complex)

    def idx(i, j):
        return j * (Nx + 1) + i

    # 使用单点积分（中点近似）加快组装
    for j in range(Ny):
        sigma_y_avg = (sigma_profile[j] + sigma_profile[j+1]) / 2
        s_y = 1 - 1j * sigma_y_avg / (k0 * 8.854e-12 * 3e8 / 377)  # 归一化
        # 简化为 s_y = 1 - j * sigma_y / (omega * epsilon_0)
        # 使用自由空间近似: omega * epsilon_0 = k0 / Z0
        s_y = 1 - 1j * sigma_y_avg * 377 / k0

        for i in range(Nx):
            n0, n1, n2, n3 = idx(i, j), idx(i+1, j), idx(i+1, j+1), idx(i, j+1)

            # 中点近似
            detJ = hx * hy / 4
            dN_dx = np.array([-(1)/2, (1)/2, (1)/2, -(1)/2]) / (hx/2)
            dN_dy = np.array([-(1)/2, -(1)/2, (1)/2, (1)/2]) / (hy/2)

            # PML 修改: 在 y 方向拉伸坐标
            # ∂/∂y → (1/s_y) ∂/∂y
            dN_dy_pml = dN_dy / s_y

            # 刚度矩阵
            for ii, gi in enumerate([n0, n1, n2, n3]):
                for jj, gj in enumerate([n0, n1, n2, n3]):
                    Ke = (dN_dx[ii]*dN_dx[jj] + dN_dy_pml[ii]*dN_dy_pml[jj]) * detJ
                    K[gi, gj] += Ke
                    Me = detJ / 4  # N_i · N_j 近似
                    M[gi, gj] += Me * (s_y if i == j else 0)  # PML 拉伸

    A = K - k0**2 * M

    # 边界: 底部激励 (平面波)
    rhs = np.zeros(total_nodes, dtype=complex)
    for i in range(Nx + 1):
        # 在底部处加激励
        rhs[idx(i, 0)] = 1.0

    # Dirichlet BC
    for j in range(Ny + 1):
        for i in range(Nx + 1):
            if i == 0 or i == Nx:  # 侧壁 PEC
                n = idx(i, j)
                A[n, :] = 0
                A[n, n] = 1
                rhs[n] = 0

    A = A.tocsc()

    try:
        phi = sp_linalg.spsolve(A, rhs)
    except Exception as e:
        print(f"  PML 求解失败: {e}")
        return X, Y, np.zeros_like(X, dtype=complex), np.zeros(Ny+1)

    phi_field = phi.reshape((Ny + 1, Nx + 1))

    # 沿中心线提取衰减
    center_i = Nx // 2
    decay = np.abs(phi_field[:, center_i])

    return X, Y, phi_field, decay


def test_pml_2d():
    """测试 PML 吸收边界"""
    print("\n" + "=" * 60)
    print("2D PML (完全匹配层) 验证")
    print("=" * 60)

    X, Y, phi_field, decay = pml_2d_slab(Nx=80, Ny=80, pml_thickness=20, k0=25)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    im = axes[0].pcolormesh(X, Y, np.abs(phi_field), shading="auto", cmap="inferno")
    axes[0].set_title(r"$|\phi|$: PML 吸收边界")
    axes[0].set_xlabel("x"); axes[0].set_ylabel("y")
    plt.colorbar(im, ax=axes[0])

    # 沿中心线的衰减
    y = np.linspace(0, 1, len(decay))
    axes[1].semilogy(y, decay / np.max(decay), "b-", linewidth=2)
    axes[1].axvline(x=0.75, color="r", linestyle="--", alpha=0.7, label="PML 起始")
    axes[1].set_xlabel("y"); axes[1].set_ylabel("归一化 |φ|")
    axes[1].set_title("PML 内指数衰减")
    axes[1].grid(True, alpha=0.3)
    axes[1].legend()

    plt.tight_layout()
    plt.savefig("cem/pml_2d_validation.png", dpi=120)
    plt.close()
    print(f"  >> 结果已保存: cem/pml_2d_validation.png")

    return X, Y, phi_field


# ═══════════════════════════════════════════════════════════════════════════════
#  主程序: 运行所有示例
# ═══════════════════════════════════════════════════════════════════════════════

def run_all():
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  Jian-Ming Jin  《The Finite Element Method in            ║")
    print("║                Electromagnetics》 3rd Ed.  代码示例       ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()

    # ─── 1D Poisson ───
    print("=" * 60)
    print("示例 1: 1D FEM — Poisson 方程")
    print("=" * 60)
    x, phi_num, phi_ex = fem_1d_poisson(N=20, source="constant")
    error = np.max(np.abs(phi_num - phi_ex)) if phi_ex is not None else 0
    print(f"  最大误差: {error:.3e}")
    print()

    # ─── 1D Helmholtz ───
    print("=" * 60)
    print("示例 2: 1D FEM — Helmholtz 方程 (Robin BC)")
    print("=" * 60)
    x_h, phi_h = fem_1d_helmholtz(N=100, k=8*np.pi)
    print(f"  计算完成，节点数: {len(x_h)}")
    print()

    # ─── 2D Waveguide ───
    kc = test_waveguide_modes()
    print()

    # ─── 3D Cavity ───
    test_cavity_3d()
    print()

    # ─── ABC ───
    test_abc_2d()
    print()

    # ─── PML ───
    test_pml_2d()
    print()

    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  所有示例运行完成。                                         ║")
    print("║  结果图: cem/abc_2d_validation.png                         ║")
    print("║          cem/pml_2d_validation.png                         ║")
    print("╚══════════════════════════════════════════════════════════════╝")


if __name__ == "__main__":
    run_all()
