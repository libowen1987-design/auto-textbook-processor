---
chapter: 11
title: "Nonuniform Grids, Nonorthogonal Grids, Unstructured Grids, and Subgrids"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, B. Z. Steinberg, M. Okoniewski, T. Weiland, R. Schuhmann"
raw_size: 109,577 bytes
---

# Chapter 11: Nonuniform Grids, Nonorthogonal Grids, Unstructured Grids, and Subgrids
> **中英双语版**

> 非均匀网格、非正交网格、非结构化网格和子网格

## 11.1 Introduction
> 引言

Structures with fine geometrical features often cannot conform to a uniform orthogonal lattice. Two strategies exist:
> 具有精细几何特征的结构通常无法适应均匀正交网格。存在两种策略：

1. **Global mesh variation**: Nonuniform graded meshes, curvilinear body-fitted coordinate systems, or fully unstructured meshes (tetrahedral/hexahedral). These can conform to arbitrary geometries but may add computational overhead.
   > **全局网格变换**：非均匀渐变网格、曲线贴体坐标系或完全非结构化网格（四面体/六面体），可适配任意几何但增加计算开销。
2. **Local subgridding**: Embed refined subgrids only where needed, leaving the rest of the domain on a coarse Cartesian mesh.
   > **局部子网格**：仅在需要处嵌入细化子网格，其余区域保持在粗笛卡尔网格上。

## 11.2 Nonuniform Orthogonal Grids
> 非均匀正交网格

### 11.2.1 Grid Definition
> 网格定义

Let vertices be defined by general one-dimensional coordinates:
> 顶点由一般一维坐标定义：
$$
\{x_i | i = 1, N_x\},\quad \{y_j | j = 1, N_y\},\quad \{z_k | k = 1, N_z\}
$$

Edge lengths:
> 边长：
$$
\Delta x_i = x_{i+1} - x_i,\quad \Delta y_j = y_{j+1} - y_j,\quad \Delta z_k = z_{k+1} - z_k
$$

Dual edge lengths (distances between edge centers):
> 对偶边长（边中心之间距离）：
$$
h_i^x = \frac{\Delta x_i + \Delta x_{i-1}}{2},\quad
h_j^y = \frac{\Delta y_j + \Delta y_{j-1}}{2},\quad
h_k^z = \frac{\Delta z_k + \Delta z_{k-1}}{2}
$$

### 11.2.2 Update Equations (Integral Form)
> 更新方程（积分形式）

Using Faraday's and Ampère's laws in integral form on the Yee cell.
> 在 Yee 网格上使用积分形式的法拉第定律和安培定律。

### 11.2.3 Supraconvergence
> 超收敛

Although the E-field updates are locally first-order in nonuniform regions, the overall scheme achieves **global second-order accuracy** — a phenomenon known as *supraconvergence* (Monk 1992).
> 尽管在非均匀区域电场更新是局部一阶精度，但整体格式仍能达到**全局二阶精度**——这一现象称为*超收敛*。

### 11.2.4 Stability Criterion
> 稳定性条件
$$
\Delta t < \frac{1}{c \sqrt{(\Delta x_{i,\min})^{-2} + (\Delta y_{j,\min})^{-2} + (\Delta z_{k,\min})^{-2}}}
$$
The time-step is thus limited by the smallest cell in the mesh.
> 时间步长受限于网格中最小的单元。

## 11.3 Locally Conformal Grids, Globally Orthogonal
> 局部共形、全局正交网格

This class uses globally orthogonal grids with only those cells adjacent to curved boundaries deformed to conform (the contour-path approach of Chapter 10, §10.6).
> 此类方法使用全局正交网格，仅将与弯曲边界相邻的网格单元变形以适配（第10章 §10.6 的回路路径法）。

## 11.4 Global Curvilinear Coordinates
> 全局曲线坐标

### 11.4.1 Nonorthogonal Curvilinear FDTD
> 非正交曲线坐标 FDTD

Coordinate system $(u^1, u^2, u^3)$ with unitary vectors $\mathbf{a}_i = \partial\mathbf{r}/\partial u^i$.
> 坐标系 $(u^1, u^2, u^3)$，基矢 $\mathbf{a}_i = \partial\mathbf{r}/\partial u^i$。

Maxwell's equations in covariant/contravariant form:
> 协变/逆变形式的麦克斯韦方程：
$$
-\mu \frac{\partial h^i}{\partial t} = \frac{1}{\sqrt{g}} \left( \frac{\partial e_k}{\partial u^j} - \frac{\partial e_j}{\partial u^k} \right)
$$
$$
\epsilon \frac{\partial e^i}{\partial t} + \sigma e^i = \frac{1}{\sqrt{g}} \left( \frac{\partial h_k}{\partial u^j} - \frac{\partial h_j}{\partial u^k} \right)
$$

### 11.4.4 Stability Criterion
> 稳定性条件
$$
\Delta t \leq \frac{2}{c \sqrt{g^{11} + g^{22} + g^{33}}}
$$
where $g^{ii}$ are diagonal elements of the inverse metric tensor.
> 其中 $g^{ii}$ 为逆变度量张量的对角元。

## 11.5 Irregular Nonorthogonal Structured Grids
> 不规则非正交结构化网格

Follows the same covariant/contravariant formulation as §11.4 but with locally varying metric tensors.
> 遵循与 §11.4 相同的协变/逆变公式，但具有局部变化的度量张量。

## 11.6 Irregular Nonorthogonal Unstructured Grids
> 不规则非正交非结构化网格

### 11.6.1 Generalized Yee Algorithm
> 广义 Yee 算法

Both electric and magnetic fields are represented as **edge-integrated** (or "whirl") quantities:
> 电场和磁场都表示为**边积分量**：
$$
\hat{E}_i = \int_{\text{edge } i} \mathbf{E} \cdot d\mathbf{l}, \quad
\hat{H}_i = \int_{\text{edge } i} \mathbf{H} \cdot d\mathbf{l}
$$

### 11.6.2 The Finite Integration Technique (FIT)
> 有限积分技术

Developed by Weiland (1977), FIT uses the exact matrix representation of the integral Maxwell equations on a dual grid.
> 由 Weiland（1977）提出，FIT 在对偶网格上使用积分麦克斯韦方程的精确矩阵表示。

## 11.8 Cartesian Subgrids
> 笛卡尔子网格

### 11.8.1 Geometry
> 几何结构

Subgrid blocks with 2:1 cell-size reduction from primary grid, shifted by one-quarter of the primary grid cell dimension.
> 子网格块的网格尺寸为主网格的 1:2，偏移四分之一主网格单元尺寸。

### 11.8.2 Time-Stepping Scheme
> 时间步进格式

The subgrid uses $\Delta t/2$ (half the primary grid time-step). The scheme uses **temporal interpolation** (not extrapolation) for better accuracy and stability.
> 子网格使用 $\Delta t/2$（主网格时间步的一半）。该格式使用**时间插值**（而非外推）以获得更好的精度和稳定性。

### 11.8.4 Stability
> 稳定性

Stable beyond 100,000 time-steps at 90% of the Courant limit.
> 在 Courant 极限的 90% 时稳定超过 100,000 时间步。

### 11.8.5 Interface Reflection
> 界面反射

- Single 2:1 subgrid: reflection < -70 dB at $\lambda_0/30$ primary resolution
  > 单个 2:1 子网格：反射 < -70 dB
- Nested subgrids (8:1 to 16:1): worst-case reflection ≈ -70 dB
  > 嵌套子网格（8:1 到 16:1）：最差反射约 -70 dB

## 11.9 Summary and Conclusions
> 总结与结论

| Grid Type | Accuracy | Computational Cost | Ease of Implementation | Stability |
|-----------|----------|-------------------|----------------------|-----------|
| 网格类型 | 精度 | 计算成本 | 实现难度 | 稳定性 |
| Nonuniform orthogonal | 2nd-order globally | Moderate | Easy | CFL-limited |
| 非均匀正交 | 全局二阶 | 中等 | 容易 | 受最小单元 CFL 限制 |
| Locally conformal | Near 2nd-order | Low | Moderate | Good |
| 局部共形 | 近二阶 | 低 | 中等 | 好 |
| Global curvilinear | 2nd-order | High | Difficult | Metric-dependent |
| 全局曲线坐标 | 二阶 | 高 | 困难 | 取决于度量 |
| Unstructured (FIT) | 1st-2nd order | High | Very difficult | Complex |
| 非结构化 (FIT) | 一至二阶 | 高 | 非常困难 | 复杂 |
| Cartesian subgrid | ~2nd-order | Moderate | Moderate | 90% of CFL |
| 笛卡尔子网格 | 约二阶 | 中等 | 中等 | CFL 的 90% |

### Key Takeaways
> 关键要点

1. **Supraconvergence** ensures nonuniform orthogonal FDTD achieves global second-order accuracy.
   > **超收敛**确保非均匀正交 FDTD 达到全局二阶精度。
2. **Nonorthogonal curvilinear FDTD** provides boundary-conforming capability at the cost of metric tensor computations.
   > **非正交曲线坐标 FDTD** 以度量张量计算为代价提供边界适配能力。
3. **Cartesian subgridding** is the most practical approach for localized mesh refinement.
   > **笛卡尔子网格**是局部网格细化的最实用方法。
4. For most applications, a nonuniform orthogonal grid with subgridding offers the best balance.
   > 对大多数应用，带子网格的非均匀正交网格提供了最佳平衡。
