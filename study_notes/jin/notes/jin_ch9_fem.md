# Chapter 9: The Finite Element Method | 第九章：有限元法

> **中英双语版**

**Source:** Jin, *Theory and Computation of Electromagnetic Fields*, 2nd Ed., Chapter 9 (pp. 457–528)

---

## 9.1 Basic Formulation | 基本公式

### 9.1.1 Weighted Residual Method | 加权余量法

For a 1D boundary-value problem / 对于一维边值问题：
$$
-\frac{d}{dx}\left(p\frac{du}{dx}\right) + qu = f, \quad 0 < x < L
\tag{9.1.1}
$$

The residual is / 余量为：
$$
r(x) = -\frac{d}{dx}\left(p\frac{du}{dx}\right) + qu - f
$$

Weighted residual / 加权余量：$\int_0^L r(x) w_i(x)\, dx = 0, \quad i = 1,2,\ldots,N$

### 9.1.2 Weak Form (Galerkin's Method) | 弱形式（伽辽金法）

Integration by parts reduces continuity requirements / 分部积分降低连续性要求：

$$
\int_0^L \left(p\frac{dw_i}{dx}\frac{du}{dx} + q w_i u\right) dx = \int_0^L w_i f\, dx + \left[ w_i p\frac{du}{dx}\right]_0^L
\tag{9.1.6}
$$

This is the **weak form** — only first derivatives appear, suitable for linear basis functions / 这是**弱形式**——仅出现一阶导数，适用于线性基函数。

### 9.1.3 Basis Functions | 基函数

For 1D linear elements with nodes at $x_1, x_2, \ldots, x_N$ / 对于节点在 $x_1, x_2, \ldots, x_N$ 的一维线性单元：

$$
u^e(x) = \sum_{j=1}^2 u_j^e N_j^e(x)
\tag{9.1.9}
$$

其中 $N_1^e(\xi) = 1 - \xi$, $N_2^e(\xi) = \xi$，局部坐标 $\xi = (x - x_1^e)/(x_2^e - x_1^e)$。

---

## 9.2 Finite Element Analysis of 1D Problems | 一维问题的有限元分析

### 9.2.1 Element Matrix Assembly | 单元矩阵组装

Element matrix / 单元矩阵：
$$
K_{ij}^e = \int_{x_1^e}^{x_2^e} \left(p\frac{dN_i}{dx}\frac{dN_j}{dx} + q N_i N_j\right) dx
\tag{9.2.1}
$$

Global assembly / 全局组装：$K = \sum_{e=1}^M K^e$, $b = \sum_{e=1}^M b^e$

System / 系统：$K \mathbf{u} = \mathbf{b}$

### 9.2.2 Boundary Conditions | 边界条件

**Dirichlet** (essential / 本质边界条件): $u$ specified → modify RHS / 指定 $u$ → 修改右端项
**Neumann** (natural / 自然边界条件): $du/dx$ specified → included in boundary term / 指定 $du/dx$ → 包含在边界项中
**Mixed** (Robin / 混合): $\alpha u + \beta \frac{du}{dx} = \gamma$

---

## 9.3 2D Scalar FEM | 二维标量有限元法

### 9.3.1 Helmholtz Equation | 亥姆霍兹方程

$$
\nabla^2 u + k^2 u = g
\tag{9.3.1}
$$

Weak form (integrate by parts using Green's identity) / 弱形式（使用格林恒等式分部积分）：

$$
\iint_\Omega (\nabla w_i \cdot \nabla u - k^2 w_i u)\, d\Omega = \iint_\Omega w_i g\, d\Omega - \oint_\Gamma w_i (\hat{\mathbf{n}} \cdot \nabla u)\, d\Gamma
\tag{9.3.2}
$$

### 9.3.2 Triangular Elements | 三角形单元

Linear triangular element with nodes at $(x_1,y_1), (x_2,y_2), (x_3,y_3)$ / 节点在 $(x_1,y_1), (x_2,y_2), (x_3,y_3)$ 的线性三角形单元：

$$
N_i(x,y) = \frac{1}{2\Delta}(a_i + b_i x + c_i y), \quad i = 1,2,3
\tag{9.3.5}
$$

其中 $\Delta$ 是三角形面积，且：

$$
a_i = x_j y_k - x_k y_j, \quad b_i = y_j - y_k, \quad c_i = x_k - x_j
$$

### 9.3.3 Element Matrix (2D) | 单元矩阵（二维）

$$
K_{ij}^e = \iint_{\Omega^e} (\nabla N_i \cdot \nabla N_j - k^2 N_i N_j)\, d\Omega
$$

对于线性三角形，$\nabla N_i$ 在单元内为常数。

---

## 9.4 3D Vector FEM (Edge Elements) | 三维矢量有限元法（棱边元）

### 9.4.1 Edge Elements (Whitney Elements) | 棱边元（惠特尼元）

Instead of nodal basis functions for each field component, edge elements use basis functions associated with element edges / 棱边元使用与单元棱边关联的基函数，而非对每个场分量使用节点基函数：

$$
\mathbf{N}_i = \xi_i \nabla\xi_j - \xi_j \nabla\xi_i
\tag{9.4.1}
$$

Advantages / 优势：
- 跨单元边界的切向连续性
- 本征值问题中无伪模
- 正确建模棱边处的场奇异性

### 9.4.2 Application to Maxwell's Equations | 应用于麦克斯韦方程组

$$
\iiint_V \left[(\nabla \times \mathbf{w}_i) \cdot (\nabla \times \mathbf{E}) - k^2 \mathbf{w}_i \cdot \mathbf{E}\right] dV = \cdots
\tag{9.4.5}
$$

---

## 9.5 Absorbing Boundary Conditions for FEM | 有限元的吸收边界条件

For open-region problems, ABCs are needed to truncate the FEM mesh / 对于开放区域问题，需要ABC来截断有限元网格：
- **First-order ABC / 一阶ABC:** $(\nabla u) \cdot \hat{\mathbf{n}} = -j k u$
- **PML / 完美匹配层:** 与FDTD中的概念相同

---

## 9.6 Adaptive Mesh Refinement | 自适应网格细化

Error estimation using the recovered field gradient / 使用恢复的场梯度进行误差估计：

$$
\eta_e = \|\nabla u^h - \mathbf{Q} u^h\|_{L_2(\Omega^e)}
$$

误差超过阈值的单元被细分。
