# Chapter 9: Low-Frequency Scattering from Penetrable Bodies
# 穿透性体的低频散射

**Authors:** Siyuan Chen and Weng Cho Chew

---

## 9.1 Introduction | 引言

Computational electromagnetics is important for geophysics and remote sensing applications such as electrical logging tools, interpretation of measurement data, rough-surface scattering, and remotely sensed data.

计算电磁学对于地球物理和遥感应用很重要，如电测井工具、测量数据解释、粗糙表面散射和遥感数据。

A key challenge: **low-frequency operation** where the measurement apparatus or features being probed are much smaller than the wavelength (quasi-static regime). Standard methods like MoM and FEM break down at very low frequencies.

一个关键挑战：**低频工作**，此时测量设备或被探测特征远小于波长（准静态域）。标准方法如 MoM 和 FEM 在低频时失效。

The **low-frequency breakdown problem** is related to the Helmholtz decomposition of Maxwell's equations. At low frequencies, electric and magnetic fields are decoupled, and the current has two components: curl-free and divergence-free.

**低频失效问题**与麦克斯韦方程的亥姆霍兹分解有关。在低频时，电场和磁场解耦，电流有两个分量：无旋部分和无散部分。

The current continuity equation requires that for physically finite charge, the divergence of curl-free current scales as $\omega$ as frequency approaches zero.

电流连续性方程要求，为了物理上有限的电荷，无旋电流的散度在频率趋近于零时按 $\omega$ 缩放。

**Solution:** Use **loop-tree** or **loop-star** basis functions to separate divergence-free and curl-free current contributions.

**解决方案：** 使用**环路-树**或**环路-星**基函数来分离无散和无旋电流贡献。

---

## 9.2 Low-Frequency Scattering from a Single Penetrable Body | 单个穿透性体的低频散射

### 9.2.1 Basis Functions | 基函数

**RWG (Rao-Wilton-Glisson) basis function** associated with the $n$-th interior edge:

与第 $n$ 个内部边缘相关的 RWG（ Rao-Wilton-Glisson）基函数：

$$\mathbf{f}_n(\mathbf{r}) = \frac{l_n}{2A_n^+} \mathbf{\rho}_n^+ + \frac{l_n}{2A_n^-} \mathbf{\rho}_n^-$$

where $\mathbf{\rho}_n^\pm$ are vectors from the free vertex to observation point on triangular patches.

其中 $\mathbf{\rho}_n^\pm$ 是从自由顶点到三角形面片上观察点的向量。

**Loop basis function** is defined on patches attached to the $n$-th interior node:

环路基函数定义在连接到第 $n$ 个内部节点的面片上：

$$\mathbf{\Lambda}_n = \sum_{i=1}^{N_n} \lambda_i^{(n)} \mathbf{f}_i$$

The loop basis function is **divergence-free**, describing current flowing around the interior node.

环路基函数是**无散**的，描述绕内部节点的流动电流。

Loop basis function can be rewritten as:

环路基函数可重写为：

$$\mathbf{\Lambda}_n = \nabla \phi_n$$

where $\phi_n$ is a scalar function with pyramidal shape.

其中 $\phi_n$ 是具有金字塔形状的标量函数。

**Tree basis function** is complementary to loop basis, formed by selecting a subset of RWG basis functions (branches of a tree structure).

**树基函数**是环路基函数的补集，由选择 RWG 基函数的子集（树结构的分支）形成。

**Star basis function** is defined on the $n$-th triangular patch and all patches attached to it.

**星基函数**定义在第 $n$ 个三角形面片及连接到它的所有面片上。

The loop basis functions combined with tree or star basis form a complete set in the RWG space.

环路基函数与树或星基函数组合在 RWG 空间中形成完整集合。

---

### 9.2.2 PMCHWT Formulation for Penetrable Bodies | 穿透性体的PMCHWT公式

For a penetrable scatterer, applying equivalence principle and boundary conditions yields coupled integral equations for electric current $\mathbf{J}$ and magnetic current $\mathbf{M}$:

对于穿透性散射体，应用等效原理和边界条件得到电流 $\mathbf{J}$ 和磁流 $\mathbf{M}$ 的耦合积分方程：

$$\hat{n} \times \mathcal{T}_1 \mathbf{J} + \hat{n} \times \mathcal{L}_1 \mathbf{M} = \mathbf{E}^{inc}_{tan}$$
$$\hat{n} \times \mathcal{T}_2 \mathbf{J} + \hat{n} \times \mathcal{L}_2 \mathbf{M} = -\mathbf{H}^{inc}_{tan}$$

The operators $\mathcal{T}$ and $\mathcal{L}$ involve the Green's function and material parameters.

算子 $\mathcal{T}$ 和 $\mathcal{L}$ 涉及格林函数和材料参数。

Using matrix notation with loop-tree basis expansion:

使用环路-树基展开的矩阵表示：

$$\mathbf{J} = \mathbf{J}_L + \mathbf{J}_T = \sum I_i^{L} \mathbf{\Lambda}_i + \sum I_i^{T} \mathbf{T}_i$$

---

### 9.2.3 Frequency Normalization | 频率归一化

**Key insight:** Matrix elements from different operators scale differently with frequency:

**关键洞察：** 不同算子的矩阵元素随频率的缩放不同：

$$\mathcal{O}(k^2) \sim \omega^2: \text{magnetic field terms}$$
$$\mathcal{O}(k^0) \sim \omega^0: \text{static terms}$$

To avoid low-frequency breakdown, proper frequency normalization is essential:

为避免低频失效，适当的频率归一化至关重要：

$$\bar{Z} = P^\dagger Z P$$
$$\bar{I} = P^{-1} I$$

where $P$ is the frequency normalization matrix containing scaling factors.

其中 $P$ 是包含缩放因子的频率归一化矩阵。

After normalization, the matrix elements scale as $O(1)$ and the condition number remains bounded as $\omega \to 0$.

归一化后，矩阵元素按 $O(1)$ 缩放，条件数在 $\omega \to 0$ 时保持有界。

---

### 9.2.4 Physical Interpretation | 物理理解

At zero frequency, the dynamic problem **decouples** into electrostatic and magnetostatic parts:

在零频率时，动态问题**解耦**为静电和静磁部分：

- First and fourth row equations: **magnetostatic** problem
- Second and third row equations: **electrostatic** problem

- 第一和第四行方程：**静磁**问题
- 第二和第三行方程：**静电**问题

This decoupling is represented in the normalized matrix equation.

此解耦在归一化矩阵方程中表示。

For magnetic dipole excitation, electrostatic terms vanish as $\omega \to 0$.

对于磁偶极子激励，静电项在 $\omega \to 0$ 时消失。

For electric dipole excitation, magnetostatic terms vanish as $\omega \to 0$.

对于电偶极子激励，静磁项在 $\omega \to 0$ 时消失。

The loop-tree basis with proper frequency normalization naturally reduces to static solutions as frequency approaches zero.

适当的频率归一化的环路-树基函数在频率趋近于零时自然地退化为静态解。

---

## 9.3 Scattering from a Multibody | 多体散射

### 9.3.1 PMCHWT for Multibody Problem | 多体问题的PMCHWT

For multiple bodies, boundary conditions must be matched at each interface. The problem involves six unknowns (electric and magnetic currents on each body).

对于多体，必须在每个界面匹配边界条件。问题涉及六个未知数（每个物体上的电流和磁流）。

Surface relations: **contained**, **parallel**, and **isolated** determine sign conventions in cross-block matrices.

表面关系：**包含**、**平行**和**隔离**决定交叉块矩阵中的符号约定。

Self-blocks always have the form corresponding to individual body contributions.

自块总是具有对应于单个物体贡献的形式。

Cross-blocks have sign variations depending on whether the relation is "parallel" or "contained."

交叉块根据关系是"平行"还是"包含"有不同的符号变化。

### 9.3.2 Number-of-Unknowns Reduction (NOUR) Scheme | 未知数减少方案

**Problem:** When bodies touch, unknowns defined on common surfaces become redundant.

**问题：** 当物体接触时，定义在公共表面上的未知数变得冗余。

**Solution:** NOUR scheme performs row and column combinations to eliminate redundant unknowns.

**解决方案：** NOUR 方案执行行和列组合以消除冗余未知数。

For RWG basis: Simple "one-to-one" relation exists—coefficients of shared RWG edges must be equal.

对于 RWG 基：存在简单的"一对一"关系——共享 RWG 边缘的系数必须相等。

NOUR operation $\mathcal{R}$ is equivalent to column combination operator:

NOUR 操作 $\mathcal{R}$ 等价于列组合算子：

$$\mathcal{R}: [Z_1, Z_2] \to [Z_1 + Z_2]$$

The reduced system $\bar{Z} = \mathcal{R}^\dagger Z \mathcal{R}$ is well-conditioned and solved for unknowns.

约化系统 $\bar{Z} = \mathcal{R}^\dagger Z \mathcal{R}$ 是良态的，求解未知数。

### 9.3.3 NOUR for Loop-Tree Basis | 环路-树基函数的NOUR

For loop-tree basis, the support is "nonlocalized," so NOUR is more complicated.

对于环路-树基函数，支集是"非局部"的，因此 NOUR 更复杂。

**Rules for constructing NOUR:**

**构造 NOUR 的规则：**

1. Tree merges into tree: **allowed**
2. Tree merges into loop: **not allowed**
3. Loop merges into loop: **allowed**
4. Loop merges into tree: **allowed**

1. 树合并到树：**允许**
2. 树合并到环路：**不允许**
3. 环路合并到环路：**允许**
4. 环路合并到树：**允许**

The rules preserve the divergence-free property essential for frequency normalization.

规则保留了对频率归一化必不可少的无散特性。

A valid NOUR scheme always exists based on these rules.

基于这些规则，总是存在有效的 NOUR 方案。

---

## 9.4 Applications | 应用

### 9.4.1 RCS Computation | 雷达散射截面计算

Bistatic RCS computed using loop-tree basis agrees well with Mie series solutions even at very low frequencies ($10^4$ Hz).

使用环路-树基函数计算的双站 RCS 即使在非常低的频率（$10^4$ Hz）下也与米级系列解一致。

Standard RWG basis loses accuracy at low frequencies due to low-frequency breakdown.

标准 RWG 基函数由于低频失效在低频时失去准确性。

### 9.4.2 Induction Well Logging | 感应测井

The method is applied to model induction logging tools operating at 20 kHz.

该方法应用于建模在 20 kHz 下工作的感应测井工具。

Apparent conductivity computed for vertical and dipping cases agrees with numerical mode matching (NMM) method.

计算垂直和倾斜情况的表观电导率与数值模式匹配（NMM）方法一致。

---

## 9.5 Summary | 本章小结

This chapter addressed the low-frequency scattering problem for penetrable bodies using loop-tree basis functions and frequency normalization.

本章讨论了使用环路-树基函数和频率归一化的穿透性体低频散射问题。

**Key contributions:**

主要贡献：

1. **Loop-tree basis functions:** Separate divergence-free (loop) and curl-free (tree) current contributions to overcome low-frequency breakdown.

   **环路-树基函数：** 分离无散（环路）和无旋（树）电流贡献以克服低频失效。

2. **Frequency normalization scheme:** Balanced scaling of matrix elements prevents ill-conditioning as $\omega \to 0$.

   **频率归一化方案：** 平衡矩阵元素的缩放，防止 $\omega \to 0$ 时的病态条件。

3. **Natural decoupling at zero frequency:** The formulation naturally reduces to separate electrostatic and magnetostatic problems.

   **零频率时的自然解耦：** 公式自然地退化为分离的静电和静磁问题。

4. **Multibody handling with NOUR:** Systematic approach to eliminate redundant unknowns when bodies touch, preserving frequency normalization.

   **使用 NOUR 的多体处理：** 消除物体接触时冗余未知数的系统方法，保留频率归一化。

5. **Applications in geophysics:** Demonstrated for RCS computation and induction well logging at low frequencies.

   **地球物理应用：** 在低频 RCS 计算和感应测井中演示。

6. **Validation against Mie series:** Loop-tree approach validated against analytical solutions.

   **与米级系列验证：** 环路-树方法通过解析解验证。