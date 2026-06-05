# Chapter 10: Efficient Analysis of Waveguiding Structures
# 波导结构的高效分析

**Authors:** Kaladhar Radhakrishnan and Weng Cho Chew

---

## 10.1 Introduction | 引言

Waveguides are indispensable from radio frequencies to optical frequencies. Numerical characterization of complex waveguide structures is an important research topic.

波导从射频到光学频率都是不可或缺的。复杂波导结构的数值表征是一个重要的研究课题。

Analytic techniques exist only for the simplest waveguide structures; numerical techniques are needed for complicated structures.

解析技术仅适用于最简单波导结构；复杂结构需要数值技术。

This chapter develops numerical schemes to analyze waveguiding structures using 2D finite difference formulation and Krylov subspace methods.

本章使用二维有限差分格式和 Krylov 子空间方法开发分析波导结构的数值格式。

---

## 10.2 Finite Difference Formulation | 有限差分公式

### 10.2.1 Transverse Field Formulation | 横向场公式

The transverse field components are used for the waveguide problem formulation. The electric field is defined as a **fore vector** and the magnetic field as a **back vector**.

横向场分量用于波导问题公式。电场定义为**前向量**，磁场为**后向量**。

In Yee's grid, $\hat{x}$ and $\hat{y}$ components of any fore vector $\mathbf{E}$ and back vector $\mathbf{H}$ are defined at different locations:

在 Yee 网格中，任意前向量 $\mathbf{E}$ 和后向量 $\mathbf{H}$ 的 $\hat{x}$ 和 $\hat{y}$ 分量定义在不同位置：

$$E_x: (i+1/2, j) \Delta x, j\Delta y$$
$$E_y: i\Delta x, (j+1/2)\Delta y$$

The discretized vector wave equation for electric field in inhomogeneous anisotropic medium:

非均匀各向异性介质中电场的离散矢量波动方程：

$$k_0^2 \bar{\bar{\epsilon}} \cdot \mathbf{E} + \nabla \times (\bar{\bar{\mu}}^{-1} \nabla \times \mathbf{E}) = -i\omega \mathbf{J}$$

### 10.2.2 Inhomogeneous Wave Equation | 非均匀波动方程

The inhomogeneous transverse vector wave equation is used as the governing equation:

非均匀横向矢量波动方程用作控制方程：

$$\nabla_t \times (\bar{\bar{\mu}}_t^{-1} \cdot \nabla_t \times \mathbf{E}_t) - k_0^2 \bar{\bar{\epsilon}}_t \cdot \mathbf{E}_t = -i\omega \mathbf{J}_t$$

where $\nabla_t$ is the transverse nabla operator.

其中 $\nabla_t$ 是横向纳布拉算子。

The finite difference formulation results in an **asymmetric sparse matrix equation**:

有限差分格式产生**非对称稀疏矩阵方程**：

$$\bar{\bar{A}} \cdot \mathbf{x} = \mathbf{b}$$

Both matrices for electric and magnetic field formulations are asymmetric and extremely sparse, sharing the same eigenvalues.

电场和磁场公式的两个矩阵都是非对称且极稀疏的，具有相同的特征值。

### 10.2.3 Boundary Conditions | 边界条件

**Metallic waveguides:** Walls approximated as perfect electric conductors (PEC) to truncate computational domain.

**金属波导：** 将壁近似为完美电导体（PEC）以截断计算域。

**Open waveguides (dielectric waveguide, microstrip):** Metallic wall at sufficient distance to artificially truncate domain.

**开波导（介质波导、微带线）：** 在足够距离处设置金属壁以人工截断域。

**Microstrip conducting strip:** Modeled using boundary conditions rather than high conductivity substrate to avoid ill-conditioning.

**微带导体带：** 使用边界条件建模，而非高电导率基底，以避免病态条件。

The tangential electric field is set to zero on the conducting strip surface:

切向电场在导体带表面设置为零：

$$E_{tangential} = 0 \text{ on conducting strip}$$

---

## 10.3 Solution to the Sparse Matrix Equation | 稀疏矩阵方程的求解

### 10.3.1 Bi-Lanczos Algorithm | 双 Lanczos 算法

The **bi-Lanczos algorithm** is used to solve the asymmetric sparse matrix equation iteratively.

**双 Lanczos 算法**用于迭代求解非对称稀疏矩阵方程。

The bi-Lanczos algorithm approximates the original matrix $\bar{\bar{A}}$ of size $N \times N$ with a smaller tridiagonal matrix of size $M \times M$.

双 Lanczos 算法用尺寸 $M \times M$ 的较小三对角矩阵逼近尺寸 $N \times N$ 的原始矩阵 $\bar{\bar{A}}$。

The algorithm generates two sets of biorthogonal iteration vectors $\mathbf{v}_i$ and $\mathbf{w}_i$.

该算法生成两组双正交迭代向量 $\mathbf{v}_i$ 和 $\mathbf{w}_i$。

**Each iteration requires two matrix-vector multiplies.**

**每次迭代需要两次矩阵向量乘法。**

### 10.3.2 Spectral Lanczos Decomposition Method (SLDM) | 谱Lanczos分解法

The solution can be expressed in terms of matrix functions:

解可用矩阵函数表示：

$$\mathbf{x}(z) = e^{i k_z z} \bar{\bar{A}}^{-1} \cdot \mathbf{b}$$

Using SLDM technique:

使用 SLDM 技术：

$$\bar{\bar{A}}^{-1} \mathbf{b} \approx \mathbf{V} (\bar{\bar{T}}^{-1} \cdot \mathbf{V}^\dagger \mathbf{b})$$

where $\bar{\bar{T}}$ is the tridiagonal matrix from bi-Lanczos, and $\mathbf{V}$ contains the iteration vectors.

其中 $\bar{\bar{T}}$ 是来自双 Lanczos 的三对角矩阵，$\mathbf{V}$ 包含迭代向量。

### 10.3.3 Complexity and Storage | 复杂度和存储

**Complexity:** Each bi-Lanczos iteration requires two matrix-vector multiplies, each $O(N)$ for sparse matrices. Number of iterations scales as $O(\sqrt{N})$.

**复杂度：** 每次双 Lanczos 迭代需要两次矩阵向量乘法，稀疏矩阵每次 $O(N)$。迭代次数按 $O(\sqrt{N})$ 缩放。

Overall complexity: $O(N^{3/2})$.

总复杂度：$O(N^{3/2})$。

**Storage bottleneck:** Iteration vectors $\mathbf{V}$ scale as $O(N^{3/2})$.

**存储瓶颈：** 迭代向量 $\mathbf{V}$ 按 $O(N^{3/2})$ 缩放。

**Solution:** Discard and regenerate vectors using the recursive relation:

**解决方案：** 使用递归关系丢弃并重新生成向量：

$$v_{i+1} = \alpha_i v_i + \beta_i v_{i-1} + \bar{\bar{A}}^\dagger w_i$$

This reduces storage to $O(N)$ at cost of extra computation time.

这将存储减少到 $O(N)$，代价是额外的计算时间。

---

## 10.4 Waveguide Discontinuities | 波导不连续性

### 10.4.1 Single Junction Problem | 单结问题

At a waveguide junction, boundary conditions require continuity of transverse electric and magnetic fields.

在波导结处，边界条件要求横向电场和磁场连续。

**Case 1:** Waveguide 2 has more unknowns than Waveguide 1. The rectangular transformation matrix $\mathcal{R}$ pads the input vector with zeros for non-common regions.

**情况1：** 波导 2 的未知数比波导 1 多。矩形变换矩阵 $\mathcal{R}$ 用零填充非公共区域的输入向量。

The boundary conditions at the junction are:

结处的边界条件为：

$$\mathcal{R} \cdot \mathbf{E}^{inc} + \mathcal{R} \cdot \mathbf{E}^{ref} = \mathcal{E}_{common}$$
$$\mathbf{H}^{inc} + \mathbf{H}^{ref} = \mathcal{R}^\dagger \cdot \mathcal{H}_{common}$$

Solving yields reflection and transmission matrices:

求解得到反射和透射矩阵：

$$\mathbf{E}^{ref} = \mathcal{T}_{11} \cdot \mathbf{E}^{inc}$$
$$\mathbf{E}^{trans} = \mathcal{T}_{21} \cdot \mathbf{E}^{inc}$$

### 10.4.2 Implicit Mode Matching | 隐式模式匹配

The formulation uses implicit mode matching by propagating fields analytically along the longitudinal direction.

该格式通过沿纵向解析传播场来使用隐式模式匹配。

The matrices $\mathcal{T}_{11}$ and $\mathcal{T}_{21}$ have eigenvalues clustered around 1, causing rapid convergence.

矩阵 $\mathcal{T}_{11}$ 和 $\mathcal{T}_{21}$ 的特征值聚集在 1 附近，导致快速收敛。

### 10.4.3 N-Junction Problem | N结问题

The single junction formulation generalizes to multiple junctions.

单结公式推广到多结。

The waveguide is divided into $N+1$ sections along $z$. Each section has constant cross-section.

波导沿 $z$ 分为 $N+1$ 段。每段具有恒定横截面。

**Total unknowns:** $2(N+1)$ (forward and backward propagating components in each section).

**总未知数：** $2(N+1)$（每段的前向和后向传播分量）。

Matching boundary conditions at all $N$ junctions yields $2(N+1)$ equations.

在所有 $N$ 个结处匹配边界条件得到 $2(N+1)$ 个方程。

The block matrix structure is:

块矩阵结构为：

$$\begin{pmatrix} \mathcal{M}_{11} & \mathcal{M}_{12} & 0 & \cdots \\ \mathcal{M}_{21} & \mathcal{M}_{22} & \mathcal{M}_{23} & \cdots \\ 0 & \mathcal{M}_{32} & \mathcal{M}_{33} & \cdots \\ \vdots & \vdots & \vdots & \ddots \end{pmatrix}$$

The block matrix is well-conditioned and converges quickly when solved iteratively.

块矩阵是良态的，迭代求解时快速收敛。

---

## 10.5 Numerical Examples | 数值例子

### 10.5.1 Rectangular Dielectric Waveguide | 矩形介质波导

Field intensity plots for propagating modes in a rectangular dielectric waveguide with aspect ratio 2 and dielectric constant 2.25.

宽高比为 2、介电常数为 2.25 的矩形介质波导中传播模式的场强图。

### 10.5.2 Microstrip Step Discontinuity | 微带阶梯不连续性

Results for microstrip step discontinuity agree well with spectral domain approach (Koster and Jansen) and hybrid mode matching method (Meyer).

微带阶梯不连续性的结果与频域方法（Koster 和 Jansen）和混合模式匹配方法（Meyer）良好一致。

Higher-order mode effects visible in reflected field decaying away from boundary.

高阶模式效应在远离边界的反射场中可见。

### 10.5.3 Microstrip Taper | 微带锥形

Analyzed using staircasing approximation with 1, 2, and 4 junctions.

使用 1、2 和 4 个结的阶梯近似分析。

At low frequencies, single step discontinuity adequately models the taper. At higher frequencies, multiple junctions needed.

在低频时，单步不连续性充分模拟锥形。在高频时，需要多个结。

---

## 10.6 Summary | 本章小结

This chapter presented efficient full-wave analysis of waveguiding structures.

本章介绍了波导结构的高效全波分析。

**Key contributions:**

主要贡献：

1. **2D finite difference formulation:** Discretization only along transverse directions allows modeling of arbitrary permittivity profiles without explicit boundary condition matching at dielectric interfaces.

   **二维有限差分格式：** 仅沿横向的离散化允许对任意介电常数分布进行建模，无需在介电界面显式匹配边界条件。

2. **Sparse matrix solution:** Bi-Lanczos algorithm with $O(N^{3/2})$ complexity avoids explicit matrix storage.

   **稀疏矩阵求解：** 具有 $O(N^{3/2})$ 复杂度的双 Lanczos 算法避免显式矩阵存储。

3. **Implicit mode matching:** Boundary conditions at junctions incorporated implicitly through field transformation matrices, avoiding explicit modal expansion.

   **隐式模式匹配：** 结处边界条件通过场变换矩阵隐式合并，避免显式模展开。

4. **Storage reduction:** Iteration vectors regenerated recursively, reducing storage from $O(N^{3/2})$ to $O(N)$.

   **存储减少：** 迭代向量递归重新生成，将存储从 $O(N^{3/2})$ 减少到 $O(N)$。

5. **Multi-junction generalization:** Single junction formulation extends to N-junction problems with well-conditioned block matrix.

   **多结推广：** 单结公式推广到具有良态块矩阵的 N 结问题。

6. **Anisotropic substrate support:** Formulation generalizes to handle anisotropic substrates through tensor permittivity and permeability.

   **各向异性基底支持：** 公式推广以通过张量介电常数和磁导率处理各向异性基底。

7. **Validation:** Results agree well with published results from spectral domain approach and experimental data.

   **验证：** 结果与频域方法和实验数据发表的结果良好一致。