---
title: "Ch3: Finite-Element Method"
book: "Sheng & Song, Essentials of Computational Electromagnetics (2012)"
chapter: 3
pages: "159-213"
weight: 3
topics:
  - Variational formulation
  - Edge element basis functions
  - Waveguide eigenvalue problem
  - 3D discontinuous waveguide
  - 3D scattering
  - Node-edge elements
  - Higher-order elements
  - FETD
notes_version: "1.1"
---

# Chapter 3: Finite-Element Method | 有限元法

> **中英双语版**

The finite-element method (FEM) is a full-wave numerical method that discretizes the **variational formulation of a functional**. It solves two types of problems: **eigenmode problems** (waveguide and cavity) and **boundary-value problems** (closed/open-domain scattering).
有限元法是一种对**泛函的变分公式**进行离散的全波数值方法，解决两类问题：**本征模问题**（波导和腔体）和**边值问题**（封闭/开放域散射）。

---

## 3.1 Eigenmodes Problems of Dielectric-Loaded Waveguides | 介质加载波导的本征模问题

### 3.1.1 Functional Formulation | 泛函公式

The PDE for fields in a dielectric-loaded waveguide:
介质加载波导中场的 PDE：

$$
\nabla \times \frac{1}{\mu_r} \nabla \times \mathbf{E} - k_0^2 \epsilon_r \mathbf{E} = 0 \quad \text{in } S \tag{3.1}
$$

with BCs: $\hat{n} \times \mathbf{E} = 0$ on PEC, $\hat{n} \times \nabla \times \mathbf{E} = 0$ on PMC.
边界条件：PEC 上切向电场为零，PMC 上切向磁场为零。

**Derivation of the functional | 泛函推导：**
Multiplying (3.1) by $\delta\mathbf{E}$ and integrating over $S$, using Green's theorem:
将 (3.1) 乘以 $\delta\mathbf{E}$ 并在 $S$ 上积分，利用格林定理：

$$
F(\mathbf{E}) = \frac{1}{2} \int_S \left[ \frac{1}{\mu_r} (\nabla \times \mathbf{E}) \cdot (\nabla \times \mathbf{E}) - k_0^2 \epsilon_r \mathbf{E} \cdot \mathbf{E} \right] dS \tag{3.9}
$$

The variational problem: $\delta F = 0$, with $\hat{n} \times \mathbf{E} = 0$ on $G_1$.
变分问题：$\delta F = 0$，边界条件 $\hat{n} \times \mathbf{E} = 0$。

**Field decomposition | 场分解：**
For a regular waveguide infinite along $z$:
对于沿 $z$ 方向无限的规则波导：

$$
\mathbf{E}(x,y,z) = \mathbf{E}_t(x,y) + \hat{z} E_z(x,y) \, e^{-j\beta z} \tag{3.11}
$$

### 3.1.2 Choice of Basis Functions | 基函数的选择

**The spurious solution problem | 伪解问题：**
Using nodal values enforces both tangential AND normal continuity — but physically only tangential is required. This over-constraint causes spurious (unphysical) solutions.
使用节点值强制了切向和法向都连续——但物理上只要求切向连续。这种过度约束导致伪解（非物理解）。

**Edge-element basis functions (Whitney forms) | 边元基函数：**
Solution: use edge elements — tangential components at edge midpoints.
解决方案：使用边单元——在边中点定义切向分量。

$$
\mathbf{N}_1 = (L_2 \nabla L_3 - L_3 \nabla L_2) l_1,\quad
\mathbf{N}_2 = (L_3 \nabla L_1 - L_1 \nabla L_3) l_2,\quad
\mathbf{N}_3 = (L_1 \nabla L_2 - L_2 \nabla L_1) l_3 \tag{3.20,3.24,3.25}
$$

**Key property | 关键性质：** On edge $i$, $\hat{e}_i \cdot \mathbf{N}_j = \delta_{ij}$, enforcing only tangential continuity.
只强制切向连续——正确的物理约束。

**Field interpolation | 场插值：**

$$
\mathbf{E}_t = \sum_{i=1}^{3} \mathbf{N}_i E_{ti},\quad
E_z = \sum_{i=1}^{3} L_i E_{zi} \tag{3.26-3.27}
$$

### 3.1.3 Discretization of the Functional | 泛函的离散化

Substituting expansions into (3.15) yields the discrete functional matrix form.
代入得到离散泛函矩阵形式。Element matrices computed using closed-form area coordinate integrals (3.36).
单元矩阵用面积坐标积分的解析形式计算（式 3.36）。

Applying $\delta F = 0$ yields the **generalized eigenvalue equation**:
施加 $\delta F = 0$ 得到**广义特征值方程**：

$$
\begin{pmatrix} \mathbf{A}_{tt} & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} \mathbf{e}_t \\ \mathbf{e}_z \end{pmatrix} = \beta^2 \begin{pmatrix} \mathbf{B}_{tt} & \mathbf{B}_{tz} \\ \mathbf{B}_{zt} & \mathbf{B}_{zz} \end{pmatrix} \begin{pmatrix} \mathbf{e}_t \\ \mathbf{e}_z \end{pmatrix} \tag{3.49}
$$

### 3.1.4-3.1.6 Boundary Conditions and Solution | 边界条件与求解

PEC boundary: set BC rows to $[1,0,\ldots,0]$ and eliminate. Solve using sparse eigenvalue solvers (ARPACK, MATLAB `eigs`).
PEC 边界：设置对应行后消去。使用稀疏特征值求解器求解。

**Sparse storage**: 1D row-indexed scheme — only non-zero entries stored.
**稀疏存储**：一维行索引方案——只存储非零元素。

---

## 3.2 Three-Dimensional Discontinuous Waveguide Problem | 三维非连续波导问题

Joining two waveguides with different cross sections / media. Uses the **penalty function method** to enforce continuity at the discontinuity plane.
连接两个不同截面/介质的波导。使用**罚函数法**在非连续面强制连续性。

---

## 3.3 Three-Dimensional Scattering Problem | 三维散射问题

Domain truncation approaches | 域截断方法：
1. **Global boundary condition (radiation condition)** — more accurate but full matrix（全局边界条件，更精确但满矩阵）
2. **PML (Perfectly Matched Layer)** — lossy material; sparse matrices（PML：有耗材料，稀疏矩阵）

---

## 3.4 Node-Edge Elements | 节点-边元

Standard Whitney edge elements have 6 DOFs per tetrahedron. Node-edge elements add specially constructed node-based functions for better convergence while maintaining sparsity.
标准 Whitney 边元每四面体有 6 个自由度。节点-边元新增节点函数以改善收敛性。

---

## 3.5 Higher-Order Elements | 高阶单元

Hierarchical vector basis functions improve accuracy per DOF compared to linear edge elements, especially for smooth field variations.
层次化矢量基函数改善每自由度的精度，尤其适用于光滑场变化。

---

## 3.6 FETD (Finite Element Time Domain) | 时域有限元

Spatial FEM + time integration (Newmark-beta). Advantages over FDTD:
空间 FEM + 时间积分。相比 FDTD 的优势：
- Unstructured meshes for complex geometry（非结构化网格适应复杂几何）
- Higher-order spatial accuracy（高阶空间精度）
- Anisotropic materials easily handled（各向异性材料易处理）

System results in a matrix ODE: $\mathbf{M} \frac{d^2 \mathbf{u}}{dt^2} + \mathbf{K} \mathbf{u} = 0$.

---

## Key Equations Summary | 关键方程总结

| Equation | Description | 说明 |
|----------|-------------|------|
| (3.1) | PDE for waveguide fields | 波导场 PDE |
| (3.9) | Variational functional | 变分泛函 |
| (3.20) | Edge-element basis $\mathbf{N}_1$ | 边元基函数 |
| (3.30) | Discrete functional matrix | 离散泛函矩阵 |
| (3.49) | Generalized eigenvalue eq. | 广义特征值方程 |
| (3.36) | Area coordinate integration | 面积坐标积分 |
