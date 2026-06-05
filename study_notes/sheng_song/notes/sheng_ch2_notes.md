---
title: "Ch2: Method of Moments"
book: "Sheng & Song, Essentials of Computational Electromagnetics (2012)"
chapter: 2
pages: "29-150"
weight: 2
topics:
  - Method of Moments (MoM)
  - 3D PEC scattering
  - EFIE and MFIE
  - RWG basis functions
  - Singularity handling
  - Fast Multipole Method (FMM)
  - MLFMA
  - Parallel computing
  - Homogeneous dielectric scattering
  - Inhomogeneous dielectric (VIE)
  - 2D and periodic problems
notes_version: "1.1"
---

# Chapter 2: Method of Moments | 矩量法

> **中英双语版**

## Outline | 内容大纲

| § | Topic | Topic (中文) | Page |
|:-:|-------|--------------|:----:|
| 2.1 | Scattering from 3D PEC Objects | 三维 PEC 目标散射 | 29 |
| 2.2 | Scattering from 3D Homogeneous Dielectric Objects | 三维均匀介质目标散射 | 109 |
| 2.3 | Scattering from 3D Inhomogeneous Dielectric Objects | 三维非均匀介质目标散射 | 128 |
| 2.4 | Essential Points in MoM for Solving Other Problems | 矩量法求解其他问题的要点 | 136 |

---

## 2.1 Scattering from 3D PEC Objects | 三维 PEC 目标散射

The method of moments (MoM) is a full-wave numerical method that discretizes the integral equations of electromagnetic fields. Since integral equations automatically satisfy the Sommerfeld radiation condition, MoM is especially suitable for **open problems** — scattering and radiation.
矩量法是一种全波数值方法，通过对电磁场积分方程进行离散来求解。由于积分方程自动满足 Sommerfeld 辐射条件，MoM 特别适用于**开放问题**——散射和辐射。

The four essential aspects of MoM:
MoM 的四个基本要素：
1. **Choice of basis and testing functions**（基函数和测试函数的选择）
2. **Handling of singularities**（奇异性的处理）
3. **Relationship between discretized forms and numerical performance**（离散形式与数值性能的关系）
4. **Accelerating the solution of discretized matrix equations**（加速离散矩阵方程的求解）

### 2.1.1 Formulation of the Problem | 问题公式化

For radar scattering from metallic targets (aircraft, ships, etc.), the incident wave is approximated by a plane wave:
对于金属目标（飞机、舰船等）的雷达散射，入射波近似为平面波：

$$
\mathbf{E}^i(\mathbf{r}) = (\cos\alpha\,\hat{\boldsymbol{\theta}} + \sin\alpha\,\hat{\boldsymbol{\phi}})\,e^{-j\mathbf{k}^i\cdot\mathbf{r}}
\tag{2.1}
$$

$$
\mathbf{H}^i(\mathbf{r}) = \frac{1}{\eta}\,\hat{\mathbf{k}}^i \times \mathbf{E}^i(\mathbf{r})
\tag{2.2}
$$

where $\alpha$ is the polarization angle, $\eta$ is the wave impedance.
其中 $\alpha$ 为极化角，$\eta$ 为波阻抗。

From §1.3.3, the **Electric Field Integral Equation (EFIE)** on the PEC surface is:
由 §1.3.3，PEC 表面上的**电场积分方程**为：

$$
\bigl[\mathbf{E}^i + \eta\,\mathcal{L}(\mathbf{J})\bigr]_{\text{tan}} = 0 \tag{2.4}
$$

and the **Magnetic Field Integral Equation (MFIE)**:
**磁场积分方程**为：

$$
\mathbf{J} - \hat{\mathbf{n}} \times \mathcal{K}(\mathbf{J}) = \hat{\mathbf{n}} \times \mathbf{H}^i \tag{2.5}
$$

### 2.1.2 Discretization in MoM | MoM 的离散化

A general integral equation can be written as $\mathcal{L}f = g$.
一般积分方程可写为 $\mathcal{L}f = g$。

Expand $f$ in basis functions $\{f_j\}$: $f \approx \sum_{j=1}^N a_j f_j$ → substitute and test with $\{\omega_i\}$ → matrix form:
将 $f$ 用基函数展开，代入并用测试函数测试，得到矩阵形式：

$$
[\mathbf{A}]\,\{\mathbf{a}\} = \{\mathbf{g}\} \tag{2.10}
$$

### 2.1.3 Choice of Basis and Testing Functions | 基函数与测试函数的选择

The choice of basis and testing functions is **the most critical** decision in MoM.
基函数和测试函数的选择是 MoM 中**最关键**的决策。

#### RWG Basis Functions (Most Common for 3D PEC) | RWG 基函数

The Rao-Wilton-Glisson (RWG) basis function is defined on a pair of adjacent triangles sharing a common edge:
Rao-Wilton-Glisson (RWG) 基函数定义在一对共享公共边的相邻三角形上：

$$
\mathbf{f}_n(\mathbf{r}) = 
\begin{cases}
\dfrac{l_n}{2A_n^+}\,\boldsymbol{\rho}_n^+(\mathbf{r}), & \mathbf{r} \in T_n^+ \\[6pt]
\dfrac{l_n}{2A_n^-}\,\boldsymbol{\rho}_n^-(\mathbf{r}), & \mathbf{r} \in T_n^- \\[6pt]
0, & \text{otherwise}
\end{cases}
\tag{2.14}
$$

**Key properties | 关键性质：**
- Normal component across the shared edge is continuous（穿过共享边的法向分量连续）
- Divergence is constant（散度恒定）
- Total charge on each pair is zero（每对基函数总电荷为零）

#### Testing Functions: Galerkin's Method | 测试函数：伽辽金法

Galerkin's method uses the **same functions for testing** as for basis:
伽辽金法使用和基函数**相同的函数**作为测试函数：

$$
\omega_i(\mathbf{r}) = \mathbf{f}_i(\mathbf{r}) \tag{2.15}
$$

### 2.1.4 Discretized Integral Equation (DIE) and Numerical Behavior | 离散积分方程与数值行为

#### Numerical Behavior of EFIE vs. MFIE | EFIE 与 MFIE 数值性能对比

| Property | EFIE | MFIE |
|----------|------|------|
| Operator type | Fredholm 1st kind | Fredholm 2nd kind |
| Conditioning | Poor at low frequencies | Better |
| Accuracy | More accurate | Less accurate |
| Resonance | Interior resonance | Interior resonance |
| Closed surfaces | Open and closed | Closed only |

#### Combined Field Integral Equation (CFIE) | 组合场积分方程

$$
\text{CFIE} = \alpha\,\text{EFIE} + (1-\alpha)\,\eta\,\text{MFIE} \tag{2.19}
$$

Eliminates the interior resonance problem. Typically $\alpha = 0.5$.
消除内谐振问题，通常 $\alpha = 0.5$。

### 2.1.5 Handling of Singularity | 奇异性处理

When source and testing triangles overlap ($R \to 0$), the Green's function $G(R) = e^{-jkR}/(4\pi R)$ has a $1/R$ singularity.
当源三角形和测试三角形重叠时，格林函数具有 $1/R$ 奇异性。

**Singularity Extraction | 奇异性提取：**

$$
\frac{e^{-jkR}}{4\pi R} = \frac{1}{4\pi R} - \frac{jk}{4\pi} - \frac{k^2 R}{8\pi} + \cdots \tag{2.20}
$$

The $1/R$ term is integrated analytically using the formula for a triangle:
$1/R$ 项用三角形积分公式分析求解：

$$
I = \int_T \frac{1}{R}\,dS = \sum_{i=1}^3 p_i \ln\frac{R_i^+ + R_i^- + l_i}{R_i^+ + R_i^- - l_i} \tag{2.21}
$$

**Duffy transformation** for near-singular integrals (nearby triangles) | 用于近奇异积分的 Duffy 变换。

### 2.1.6 Comparison of EFIE and MFIE | EFIE 与 MFIE 对比

| Metric | EFIE | MFIE |
|--------|------|------|
| Condition $\kappa$ | $O(N)$ | $O(1)$ |
| Unknowns/$\lambda^2$ | ~100-200 | ~200-300 |
| RMS error (coarse) | 1-3% | 3-5% |
| Convergence (iterative) | Slow | Fast |

### 2.1.7 Interior Resonance Problem | 内谐振问题

At interior resonant frequencies, both EFIE and MFIE have **non-unique solutions**. CFIE resolves this.
在内谐振频率下，EFIE 和 MFIE 均有**非唯一解**。CFIE 解决此问题。

### 2.1.8 Fast Multipole Method (FMM) | 快速多极子方法

Direct MoM: $O(N^2)$ complexity. FMM reduces to $O(N^{1.5})$ for matrix-vector products.
直接 MoM 的复杂度为 $O(N^2)$。FMM 将矩阵-向量乘积降至 $O(N^{1.5})$。

**FMM Algorithm Summary | FMM 算法小结：**
```
1. Build octree for all unknowns（构建八叉树）
2. Multipole expansion from sources in each box（源到多极子展开）
3. Upward pass: aggregate children to parents（向上聚合并传递）
4. Downward pass: multipole-to-local translation（多极子到局域展开）
5. Evaluate far-field at each observation（在每个观测点计算远场）
6. Add near-field directly（直接计算近场项）
```

### 2.1.9-2.1.14 Scattered Fields, Programming, Parallel Computing | 散射场、编程与并行计算

The far-field RCS is computed from the surface current $\mathbf{J}$:
从表面电流计算远场 RCS：

$$
\sigma = \lim_{r\to\infty} 4\pi r^2 \frac{|\mathbf{E}^s|^2}{|\mathbf{E}^i|^2} \tag{2.28}
$$

MoM matrix filling is **embarrassingly parallel** (near-linear speedup).
MoM 矩阵填充是**高度可并行**的（近线性加速）。

---

## 2.2 Scattering from 3D Homogeneous Dielectric Objects | 三维均匀介质目标散射

### 2.2.1 Mathematical Formulation | 数学公式

Two formulations | 两种公式：

1. **Volume Equivalence Principle (VEP) | 体等效原理**: $\mathbf{J}_v(\mathbf{r}) = j\omega(\varepsilon - \varepsilon_0)\mathbf{E}(\mathbf{r})$ (Volume Integral Equation)（体电流，体积分方程）
2. **Surface Equivalence Principle (PMCHWT) | 面等效原理**: Equivalent surface currents on both sides of the dielectric boundary（介质界面上两面的等效面电流）

### 2.2.2 Discretized Forms and Numerical Performance | 离散形式与数值性能

| Formulation | Condition $\kappa$ | Iterations | Accuracy |
|-------------|:------------------:|:----------:|:--------:|
| PMCHWT | ~10-30 | Fast | Excellent |
| EFIE-only | ~100-1000 | Moderate | Depends |
| Müller | ~1-5 | Very fast | Good (low contrast) |

---

## 2.3 Scattering from 3D Inhomogeneous Dielectric Objects | 三维非均匀介质目标散射

For $\varepsilon(\mathbf{r})$ varying within the volume, use the **Volume Integral Equation (VIE)**:
对于体积内 $\varepsilon(\mathbf{r})$ 变化的情况，使用**体积分方程**：

$$
\frac{\mathbf{D}(\mathbf{r})}{\varepsilon(\mathbf{r})} + \frac{k_0^2}{\varepsilon_0}\int_V \overline{\mathbf{G}}(\mathbf{r},\mathbf{r}') \cdot [\varepsilon(\mathbf{r}') - \varepsilon_0]\mathbf{E}(\mathbf{r}')\,dV' = \mathbf{E}^i(\mathbf{r}) \tag{2.35}
$$

SWG basis: volume analog of RWG on tetrahedral mesh — normal continuity across faces.
SWG 基函数：四面体网格上的 RWG 体模拟——法向分量在面上连续。

The VIE has a **weaker singularity** ($1/R^2$) compared to surface EFIE ($1/R$).
VIE 的奇异性 ($1/R^2$) 弱于面 EFIE ($1/R$)。

---

## 2.4 Essential Points in MoM for Solving Other Problems | MoM 求解其他问题的要点

### 2.4.1 Scattering from 2D Objects (TM$_z$ and TE$_z$) | 二维目标散射

**TM$_z$ Polarization**: $E_z^i(\boldsymbol{\rho}) = \frac{k\eta}{4}\int_C J_z(\boldsymbol{\rho}') H_0^{(2)}(k|\boldsymbol{\rho}-\boldsymbol{\rho}'|)\,dl'$ (2.39)
Pulse basis + point matching (collocation). 脉冲基 + 点匹配。

### 2.4.2 Periodic Structures (FSS / Metamaterials) | 周期结构

**Floquet's theorem**: $\mathbf{J}(\boldsymbol{\rho} + \mathbf{p}) = \mathbf{J}(\boldsymbol{\rho})\,e^{-j\mathbf{k}_t\cdot\mathbf{p}}$ (2.41)
Floquet 定理描述周期结构上的电流分布。

### 2.4.3 Body of Revolution (BOR) | 旋转体

Azimuthal Fourier expansion reduces 3D to 2D per mode.
方位角 Fourier 展开将每个模式的 3D 问题降为 2D。

### 2.4.4 Radiation Problems | 辐射问题

Input impedance computed from | 输入阻抗计算：
$$
Z_{\text{in}} = -\frac{1}{I_0^2}\int_{S_{\text{feed}}} \mathbf{J}\cdot\mathbf{E}^i\,dS \tag{2.44}
$$

---

## Key Equations Summary | 关键方程总结

| Eq. | Description | 说明 |
|:---:|-------------|------|
| (2.4) | EFIE for PEC | PEC 电场积分方程 |
| (2.5) | MFIE for PEC | PEC 磁场积分方程 |
| (2.14) | RWG basis functions | RWG 基函数 |
| (2.19) | CFIE combination | CFIE 组合 |
| (2.21) | Analytical singularity treatment | 奇异性分析处理 |
| (2.23)-(2.26) | Fast Multipole Method | 快速多极子方法 |
| (2.33) | PMCHWT for dielectrics | 介质 PMCHWT 公式 |
| (2.35) | Volume Integral Equation | 体积分方程 |
| (2.39)-(2.40) | 2D MoM (TM/TE) | 二维 MoM |
