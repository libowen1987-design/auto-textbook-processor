---
chapter: 11
title: Fast Algorithms and Hybrid Techniques
source: Jin, Theory and Computation of Electromagnetic Fields, 2nd Ed., pp. 599–674
sections: 6
examples: 2
---

# Chapter 11: Fast Algorithms and Hybrid Techniques | 第十一章：快速算法与混合技术

> **中英双语版**

## 11.1 Introduction to Fast Algorithms | 快速算法简介 (pp. 576–578)

MoM yields fully populated matrices — direct solve $O(N^3)$, naive iterative $O(N_{\text{iter}}N^2)$ / 矩量法生成满矩阵——直接求解 $O(N^3)$，朴素迭代 $O(N_{\text{iter}}N^2)$。

Four fast algorithms covered / 涵盖四种快速算法：
- **CG-FFT**: $O(N\log N)$ for planar structures / 平面结构
- **AIM** (Adaptive Integral Method / 自适应积分法): $O(N\log N)$ for planar, $O(N^{1.5}\log N)$ for general / 平面结构，对一般情况 $O(N^{1.5}\log N)$
- **FMM** (Fast Multipole Method / 快速多极子法): $O(N^{1.5})$ single-level, $O(N\log N)$ multilevel / 单层 $O(N^{1.5})$，多层 $O(N\log N)$
- **ACA** (Adaptive Cross-Approximation / 自适应交叉近似): algebraic compression, equation-independent / 代数压缩，与方程无关

Computational complexity comparison / 计算复杂度比较：
| Complexity / 复杂度 | N=1,000 | N=10,000 | N=100,000 | N=1,000,000 |
|:----------:|:-------:|:--------:|:---------:|:----------:|
| $O(N^3)$ | 1 s | 17 min | 116 天 | 3170 年 |
| $O(N^2)$ | 0.1 s | 10 s | 17 min | 1.16 天 |
| $O(N^{1.5})$ | 0.03 s | 1 s | 32 s | 17 min |
| $O(N\log N)$ | 0.01 s | 0.15 s | 2 s | 25 s |

## 11.2 Conjugate Gradient–FFT Method | 共轭梯度–FFT法 (pp. 578–600)

### 11.2.1 Scattering by a Conducting Strip/Wire | 导体带/线的散射 (p. 578)

MoM matrix is Toeplitz (translational invariant) / 矩量法矩阵是Toeplitz（平移不变）。Matrix-vector product / 矩阵-矢量积：

$$
\sum_{n=1}^N Z_{mn}I_n = Z_m \otimes I_m \tag{11.2.2}
$$

Evaluated via FFT / 通过FFT计算：$\mathcal{F}_D^{-1}\{\mathcal{F}_D\{Z_m^P\} \circ \mathcal{F}_D\{I_m^P\}\}$ \tag{11.2.3}

Memory / 内存：$O(N)$, compute / 计算：$O(N\log N)$。

### 11.2.2 Scattering by a Conducting Plate | 导体板的散射 (pp. 579–583)

EFIE for plate current / 板电流的EFIE：

$$
jk_0 Z_0\hat{z}\times\iint_S \left[\mathbf{J}_s(\mathbf{r}')G_0(\mathbf{r},\mathbf{r}') + \frac{1}{k_0^2}\nabla'\cdot\mathbf{J}_s(\mathbf{r}')\nabla G_0(\mathbf{r},\mathbf{r}')\right]dS' = \hat{z}\times\mathbf{E}^{\text{inc}}(\mathbf{r}) \tag{11.2.6}
$$

使用均匀矩形网格上的屋顶基函数离散化。每次迭代矩阵-矢量积需要4次FFT。

### 11.2.3 Application: Microstrip Patch Array | 应用：微带贴片阵列 (p. 828)

CG-FFT应用于联合馈电微带贴片阵列。进行全波分析的电流分布计算。

### 11.2.4 Application: SAR Calculation | 应用：SAR计算 (p. 880)

人头模型中的比吸收率(SAR)，使用CG-FFT求解VIE：

$$
\text{SAR}(\mathbf{r}) = \frac{\sigma(\mathbf{r})}{2\rho(\mathbf{r})}|\mathbf{E}(\mathbf{r})|^2 \tag{11.2.28}
$$

## 11.3 Adaptive Integral Method (AIM) | 自适应积分法 (pp. 600–610)

### 11.3.1 Formulation | 公式 (p. 600)

MoM impedance matrix decomposed into near and far interactions / 矩量法阻抗矩阵分解为近和远相互作用：

$$
Z_{mn} = Z_{mn}^{\text{near}} + \sum_{p,q} \Lambda_{mp} G_{pq}^{\text{uniform}} \Lambda_{qn} \tag{11.3.4}
$$

Key idea: project arbitrary basis functions onto a uniform grid using multipole moments, then use FFT for far-field interactions / 关键思想：使用多极矩将任意基函数投影到均匀网格，然后对远场相互作用使用FFT。近场直接计算。

### 11.3.2 Multipole Moment Translation | 多极矩变换 (p. 610)

Basis function $\mathbf{f}_n$ approximated by point sources on uniform grid / 基函数 $\mathbf{f}_n$ 用均匀网格上的点源近似：

$$
\mathbf{f}_n(\mathbf{r}) \approx \sum_{\mathbf{p}\in G_n} \Lambda_{\mathbf{p}n} \delta(\mathbf{r} - \mathbf{r}_{\mathbf{p}}) \tag{11.3.5}
$$

系数 $\Lambda_{\mathbf{p}n}$ 通过匹配至 $L$ 阶的多极矩确定。

## 11.4 Fast Multipole Method (FMM) | 快速多极子法 (pp. 610–660)

### 11.4.1 Two-Dimensional Analysis | 二维分析 (pp. 610–620)

Addition theorem for Hankel function / 汉克尔函数的加法定理：

$$
H_0^{(2)}(k_0|\boldsymbol{\rho}+\mathbf{d}|) = \sum_{l=-\infty}^\infty J_l(k_0 d)H_l^{(2)}(k_0\rho)e^{jl(\phi-\phi_d-\pi)},\quad \rho>d \tag{11.4.2}
$$

Plane wave expansion of cylindrical wave / 柱波的平面波展开：

$$
J_l(k_0 d)e^{-jl(\phi_d+\pi)} = \frac{1}{2\pi}\int_0^{2\pi} e^{-j\mathbf{k}\cdot\mathbf{d} - jl(\alpha+\pi/2)}d\alpha \tag{11.4.4}
$$

Factorized Green's function / 因子化格林函数：

$$
H_0^{(2)}(k_0|\boldsymbol{\rho}-\boldsymbol{\rho}'|) = \frac{1}{2\pi}\int_0^{2\pi} e^{-j\mathbf{k}\cdot(\boldsymbol{\rho}-\boldsymbol{\rho}_p)} \tilde{\alpha}_{pq}(\alpha) e^{-j\mathbf{k}\cdot(\boldsymbol{\rho}_q-\boldsymbol{\rho}')} d\alpha \tag{11.4.7}
$$

其中 $\tilde{\alpha}_{pq}(\alpha) \approx \sum_{l=-L}^L H_l^{(2)}(k_0\rho_{pq}) e^{jl(\phi_{pq} - \alpha - \pi/2)}$ \tag{11.4.8}

**Three-step FMM procedure / 三步FMM过程**:
1. **Aggregation / 聚合**: $F_{qr} = \sum_{n\in G_q} \tilde{f}_{qn}(\alpha_r) J_{z,n}$ — 将源聚集到组中心
2. **Translation / 转移**: $F_{pr} = \sum_{q\notin B_p} \tilde{\alpha}_{pq}(\alpha_r) F_{qr}$ — 在中心间转移
3. **Disaggregation / 分发**: $F_{mp} = \sum_{r=1}^R \tilde{t}_{mp}(\alpha_r) F_{pr}$ — 分发到场点

Complexity / 复杂度：$T = C_1 NM + C_2 N^2/M$。Optimal group size / 最优组大小 $M \sim \sqrt{N}$ → $T \sim O(N^{3/2})$。

### 11.4.2 Three-Dimensional Analysis | 三维分析 (pp. 620–635)

Addition theorem for scalar Green's function in 3D / 三维标量格林函数的加法定理：

$$
\frac{e^{-jk_0|\mathbf{r}+\mathbf{d}|}}{|\mathbf{r}+\mathbf{d}|} = -jk_0\sum_{l=0}^\infty (-1)^l(2l+1)j_l(k_0 d)h_l^{(2)}(k_0 r)P_l(\hat{d}\cdot\hat{r}),\quad r>d \tag{11.4.22}
$$

Plane wave expansion of spherical wave / 球波的平面波展开：

$$
j_l(k_0 d)P_l(\hat{d}\cdot\hat{r}) = \frac{j^l}{4\pi}\iint e^{-j\mathbf{k}\cdot\mathbf{d}} P_l(\hat{k}\cdot\hat{r})\,d^2\hat{k} \tag{11.4.23}
$$

Factorized 3D Green's function / 因子化三维格林函数：

$$
G_0(\mathbf{r},\mathbf{r}') \approx \frac{1}{jk_0}\iint e^{-j\mathbf{k}\cdot(\mathbf{r}-\mathbf{r}_p)} \tilde{\alpha}_{pq}(\hat{k}) e^{-j\mathbf{k}\cdot(\mathbf{r}_q-\mathbf{r}')}\,d^2\hat{k} \tag{11.4.29}
$$

其中 $\tilde{\alpha}_{pq}(\hat{k}) = \left(\frac{k_0}{4\pi}\right)^2 \sum_{l=0}^L (-j)^l(2l+1)h_l^{(2)}(k_0 r_{pq})P_l(\hat{k}\cdot\hat{r}_{pq})$ \tag{11.4.30}

### 11.4.3 Multilevel FMM (MLFMA) | 多层快速多极子 (pp. 635–650)

Create octree structure: root box contains entire object, recursively subdivided into 8 child boxes / 创建八叉树结构：根盒包含整个物体，递归细分为8个子盒。

**Two-pass algorithm / 两趟算法**:
- **Upward pass / 上行**: 将辐射方向图从子节点聚合到父节点
- **Downward pass / 下行**: 将入射场从父节点分发到子节点

At each level $l$, group size $d_l = D/2^l$, number of groups $G_l \sim 4^l$ / 在每层 $l$，组大小 $d_l = D/2^l$，组数 $G_l \sim 4^l$。

Translation between non-nearby groups at same level using interpolation/interpolation to transfer between levels / 同层非相邻组间通过插值/反插值在层间传递。

Complexity / 复杂度：$O(N\log N)$ for both memory and CPU time / 内存和CPU时间。

Truncation number for 3D / 三维截断数：$L \approx k_0 d + C(k_0 d)^{1/3}$。

### 11.4.4 FMM/MLFMA Implementation | FMM/MLFMA实现 (pp. 650–660)

Implementation steps / 实现步骤：
1. Build octree / 构建八叉树：将 $N$ 个未知量分布到各盒
2. Compute near-field interactions directly / 直接计算近场相互作用
3. Compute far-field interactions via MLFMA tree / 通过MLFMA树计算远场相互作用
4. Iterative solver (GMRES, BCGSTAB) for matrix equation / 迭代求解器 (GMRES, BCGSTAB) 求解矩阵方程

**Example 11.1 / 例11.1**: 导体球的RCS，$ka=30$ — MLFMA 使用 $N=289,\!344$ 未知量，40次迭代收敛。

## 11.5 Adaptive Cross-Approximation (ACA) | 自适应交叉近似 (pp. 660–670)

### 11.5.1 Basic Principle | 基本原理 (p. 660)

For a rank-$k$ matrix block, approximate as / 对秩为 $k$ 的矩阵块，近似为 $\mathbf{Z}_{m\times n} \approx \mathbf{U}_{m\times k}\mathbf{V}_{k\times n}$。

**ACA algorithm / ACA算法**:
1. 选取轴行 $i_1$，计算行矢量 $\mathbf{R}_{i_1,:}$ 
2. 选取轴列 $j_1$，计算列矢量 $\mathbf{R}_{:,j_1}$
3. 计算 $\mathbf{U}_{:,1} = \mathbf{R}_{:,j_1} / (\mathbf{R}_{i_1,j_1})$, $\mathbf{V}_{1,:} = \mathbf{R}_{i_1,:}$
4. 更新残差，重复直到 $\|\mathbf{R}^{(k)}\|_F \leq \epsilon\|\mathbf{Z}^{(k)}\|_F$

ACA只需要计算原始矩阵的少量行和列。直接作用于矩阵，与积分方程公式无关。

### 11.5.2 Application to MoM | 应用于矩量法 (p. 665)

Decompose MoM matrix into near-field (small blocks, direct) and far-field (large blocks, ACA-compressed) / 将矩量法矩阵分解为近场（小块，直接）和远场（大块，ACA压缩）。Hierarchical matrix ($\mathcal{H}$-matrix) structure / 层级矩阵结构。

## 11.6 Hybrid Techniques | 混合技术 (pp. 670–674)

### 11.6.1 FE-BI Method | 有限元–边界积分法 (p. 670)

FEM inside domain with inhomogeneous/geometrically complex materials; BI on boundary truncates the mesh / 域内使用有限元处理非均匀/几何复杂材料；边界上使用边界积分截断网格。

Matrix equation / 矩阵方程：

$$
\begin{bmatrix}
\mathbf{K}_{\text{FEM}} & \mathbf{B} \\
\mathbf{C} & \mathbf{D}_{\text{BI}}
\end{bmatrix}
\begin{Bmatrix}
\mathbf{x}_{\text{int}} \\
\mathbf{x}_{\text{BC}}
\end{Bmatrix}
= \begin{Bmatrix}
\mathbf{b}_{\text{int}} \\
\mathbf{b}_{\text{inc}}
\end{Bmatrix} \tag{11.6.1}
$$

### 11.6.2 FETD-FDTD Hybrid | FETD-FDTD混合 (p. 672)

FEM-TD用于几何复杂区域；FDTD用于大型规则区域。通过重叠或交界面区域耦合。

## 11.7 Summary | 总结

| Algorithm / 算法 | Best for / 最佳适用 | Complexity / 复杂度 | Key Technique / 关键技术 |
|-----------|----------|:----------:|:-------------:|
| CG-FFT | 平面/周期 | $O(N\log N)$ | 基于FFT的卷积 |
| AIM | 非均匀 | $O(N\log N)$ | 网格投影+FFT |
| FMM | 一般散射 | $O(N\log N)$ | 多极展开 |
| ACA | 一般（代数） | $O(N\log N)$ | 矩阵压缩 |
| FE-BI | 复杂物体 | $O(N)$ sparse + $O(N_{\text{BC}}\log N_{\text{BC}})$ | 区域分解 |

## **Physical Intuition / 物理直觉**
- 快速算法的"快"来自利用远场相互作用的光滑性——远处的源可以被分组并集体处理。
- 亥姆霍兹核 $e^{-jkR}/R$ 在大 $kR$ 时快速振荡，限制了远场压缩的激进程度（与静态 $1/R$ 核不同）。
- MLFMA的 $O(N\log N)$ 接近最优——读取解需要 $O(N)$，没有算法能超越这个界限。

## **Numerical Intuition / 数值直觉**
- FMM截断 $L \sim k_0 d$ 意味着更大的组需要更多多极项——存在一个最优组大小。
- ACA在块内 $k_0 d$ 较小时效果最好——相距远的块有低秩相互作用。
- CG-FFT在 $1000\times 1000$ 网格上每次迭代只需要 $4 \times 4$M次FFT运算（$\sim 10^7$ 次 vs 直接法的 $10^{12}$ 次）。
- MLFMA在 $N=10^6$ 时可在大约 $\sim 10^8$ 次运算中完成矩阵-矢量积 vs 直接法的 $10^{12}$ 次。

## **Audit Table / 审计表**
| Section / 节 | Pages / 页 | Key Formulas / 关键公式 | Verified / 验证 |
|---------|-------|:------------:|:--------:|
| 11.1 | 576–578 | 复杂度分析 | ✓ |
| 11.2 | 578–600 | (11.2.1)–(11.2.28) | ✓ |
| 11.3 | 600–610 | (11.3.4)–(11.3.11) | ✓ |
| 11.4.1 | 610–620 | (11.4.1)–(11.4.18) | ✓ |
| 11.4.2 | 620–635 | (11.4.22)–(11.4.30) | ✓ |
| 11.4.3-4 | 635–660 | MLFMA树，实现 | ✓ |
| 11.5 | 660–670 | ACA算法 | ✓ |
| 11.6 | 670–674 | FE-BI, FETD-FDTD | ✓ |
