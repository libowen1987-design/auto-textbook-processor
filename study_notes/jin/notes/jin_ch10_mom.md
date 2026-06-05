---
chapter: 10
title: The Method of Moments (MoM)
source: Jin, Theory and Computation of Electromagnetic Fields, 2nd Ed., pp. 529–598
sections: 9
examples: 5
---

# Chapter 10: The Method of Moments (MoM) | 第十章：矩量法

> **中英双语版**

## 10.1 Introduction to MoM | 矩量法简介 (pp. 506–510)

MoM converts integral equations into matrix equations / 矩量法将积分方程转化为矩阵方程。Starting point: operator equation / 出发点：算子方程

$$
L f = g \tag{10.1.1}
$$

其中 $L$ 是线性算子（如带有格林函数核的积分算子）。

**Procedure / 步骤**:
1. Expand $f \approx \sum_{n=1}^N a_n f_n$ (basis functions / 基函数)
2. Test with $w_m$ / 用 $w_m$ 检验：$\sum_{n=1}^N a_n \langle w_m, L f_n \rangle = \langle w_m, g \rangle$ (testing functions / 检验函数)
3. Solve / 求解 $[Z_{mn}][a_n] = [V_m]$

**Example / 示例**: 静电容问题：

$$
\Phi = \iint_S \frac{\rho_s(\mathbf{r}')}{4\pi\epsilon|\mathbf{r}-\mathbf{r}'|} dS' \tag{10.1.3}
$$

将表面离散为小块 → 脉冲基 → 矩阵方程 → 求解 $\rho_s$。

## 10.2 Basis and Testing Functions | 基函数与检验函数 (pp. 510–516)

### 10.2.1 Basis Function Types | 基函数类型

| Type / 类型 | Description / 描述 | Use Case / 应用 |
|------|:-----------:|:---------|
| **Pulse / 脉冲** | 分段常数 | 简单几何 |
| **Rooftop / 屋顶** | 分段线性 | 更高精度 |
| **RWG** (Rao-Wilton-Glisson) | 三角形贴片基 | 三维表面 |
| **Entire-domain / 全域基** | 全局函数（正弦、余弦） | 规则形状 |
| **Wire basis / 线基** | 细线（正弦） | 线天线 |

### 10.2.2 Testing (Weighting) Methods | 检验（加权）方法

| Method / 方法 | $w_m$ | Properties / 性质 |
|--------|:-----:|:-----------|
| **Point matching / 点匹配** | $\delta(\mathbf{r}-\mathbf{r}_m)$ | 最简单，$O(N)$ 建立 |
| **Galerkin / 伽辽金法** | $w_m = f_m$ | 对称矩阵（对自伴算子） |
| **Least squares / 最小二乘** | $w_m = L f_m$ | 正定矩阵 |

### 10.2.3 MoM Matrix Properties | 矩量法矩阵性质

- **Full matrix / 满阵**: 由于全局格林函数耦合
- **Symmetric / 对称**: 对EFIE配伽辽金检验
- **Complex-valued / 复值**:（对时谐问题）
- **Poorly conditioned / 病态**: 对EFIE（第一类弗雷德霍姆方程）

## 10.3 2D Scattering — TM Polarization | 二维散射——TM极化 (pp. 516–534)

### 10.3.1 EFIE for PEC Cylinder (TM$_z$) | PEC柱的EFIE

Integral equation for surface current $J_z$ / 面电流 $J_z$ 的积分方程：

$$
\frac{k_0 Z_0}{4} \int_\Gamma J_z(\boldsymbol{\rho}') H_0^{(2)}(k_0|\boldsymbol{\rho}-\boldsymbol{\rho}'|) d\Gamma' = E_z^{\text{inc}}(\boldsymbol{\rho}) \tag{10.3.15}
$$

**MoM solution / 矩量法解**: pulse basis + point matching / 脉冲基 + 点匹配：

$$
Z_{mn} = \frac{k_0 Z_0}{4} \int_{\Gamma_n} H_0^{(2)}(k_0|\boldsymbol{\rho}_m - \boldsymbol{\rho}'|) d\Gamma' \tag{10.3.16}
$$
$$
V_m = E_z^{\text{inc}}(\boldsymbol{\rho}_m) \tag{10.3.17}
$$

**Example 10.1 / 例10.1** (p. 522): 导体带，TM$_z$，宽度 $2\lambda$，$N=100$ 段。电流分布显示边缘奇异性。

### 10.3.2 MFIE for PEC Cylinder (TM$_z$) | PEC柱的MFIE

$$
\frac{1}{2} J_z(\boldsymbol{\rho}) - \frac{1}{4j} \int_\Gamma J_z(\boldsymbol{\rho}') \frac{\partial H_0^{(2)}(k_0|\boldsymbol{\rho}-\boldsymbol{\rho}'|)}{\partial n'} d\Gamma' = -\hat{z}\cdot(\hat{n}\times\mathbf{H}^{\text{inc}}) \tag{10.3.21}
$$

MFIE是第二类弗雷德霍姆方程——条件性更好，但对细薄结构精度较低。

### 10.3.3 CFIE for Closed Bodies | 封闭体的CFIE

$$
\text{CFIE} = \alpha\,\text{EFIE} + (1-\alpha)\eta\,\text{MFIE},\quad 0\le\alpha\le 1 \tag{10.3.22}
$$

Typical $\alpha = 0.5$ eliminates interior resonance, gives well-conditioned system / 典型 $\alpha = 0.5$ 消除内部谐振，给出良态系统。

**Example 10.2 / 例10.2** (p. 528): 圆形PEC柱，$ka=5$，CFIE 取 $\alpha=0.5$ 在30次CG迭代收敛，纯EFIE需200+次。

## 10.4 3D Scattering — PEC Bodies | 三维散射——PEC体 (pp. 534–552)

### 10.4.1 EFIE for 3D PEC | 三维PEC的EFIE

$$
\hat{n}\times\left[jk_0 Z_0 \iint_S \mathbf{J}_s(\mathbf{r}') G_0(\mathbf{r},\mathbf{r}') dS' + \frac{Z_0}{jk_0}\nabla\iint_S \nabla'\cdot\mathbf{J}_s(\mathbf{r}') G_0(\mathbf{r},\mathbf{r}') dS'\right] = \hat{n}\times\mathbf{E}^{\text{inc}} \tag{10.3.45}
$$

### 10.4.2 MFIE for 3D PEC | 三维PEC的MFIE

$$
\frac{1}{2}\mathbf{J}_s(\mathbf{r}) - \hat{n}\times\iint_S \mathbf{J}_s(\mathbf{r}')\times\nabla' G_0(\mathbf{r},\mathbf{r}') dS' = \hat{n}\times\mathbf{H}^{\text{inc}} \tag{10.3.46}
$$

### 10.4.3 CFIE for 3D PEC | 三维PEC的CFIE

$$
\text{CFIE} = \alpha\,\text{EFIE} + (1-\alpha)\eta\,\text{MFIE} \tag{10.3.47}
$$

### 10.4.4 RWG Basis Functions | RWG基函数 (p. 540)

Rao-Wilton-Glisson basis defined on triangular patches / 在三角形贴片上定义的RWG基：

$$
\mathbf{f}_n(\mathbf{r}) = 
\begin{cases}
\frac{L_n}{2A_n^+}\boldsymbol{\rho}_n^+, & \mathbf{r}\in T_n^+ \\
\frac{L_n}{2A_n^-}\boldsymbol{\rho}_n^-, & \mathbf{r}\in T_n^- \\
0, & \text{otherwise}
\end{cases} \tag{10.4.1}
$$

其中 $L_n$ 是公共边长度，$A_n^\pm$ 是三角形面积，$\boldsymbol{\rho}_n^\pm$ 是从自由顶点出发/指向自由顶点的矢量。

**Properties / 性质**:
- 散度相容：$\nabla\cdot\mathbf{f}_n = \pm L_n/A_n^\pm$（在每个三角形上为常数）
- 跨边界的法向连续性（无人造线电荷）
- 表示 $\mathbf{J}_s$ 而无虚假电荷

### 10.4.5 Singularity Treatment | 奇异性处理 (p. 546)

自作用积分由于 $1/R$ 格林函数奇异性需要仔细评估：
- 减量法
- 达菲变换
- 解析积分

## 10.5 Scattering by Dielectric Objects | 介质体的散射 (pp. 552–564)

### 10.5.1 Surface Integral Equations for Dielectrics | 介质的面积分方程

For homogeneous dielectric body $(\epsilon_d, \mu_d)$, use PMCHWT formulation / 对均匀介质体，使用PMCHWT公式：

$$
\begin{bmatrix}
\mathcal{L}_0 + \mathcal{L}_d & \mathcal{K}_0 + \mathcal{K}_d \\
\mathcal{H}_0 + \mathcal{H}_d & -\frac{1}{\eta_0^2}\mathcal{L}_0 - \frac{1}{\eta_d^2}\mathcal{L}_d
\end{bmatrix}
\begin{Bmatrix}
\mathbf{J}_s \\
\mathbf{M}_s
\end{Bmatrix}
= \begin{Bmatrix}
-\mathbf{E}^{\text{inc}} \\
-\mathbf{H}^{\text{inc}}
\end{Bmatrix} \tag{10.3.29}
$$

where $\mathbf{M}_s = \mathbf{E}\times\hat{n}$ is the equivalent magnetic current / $\mathbf{M}_s = \mathbf{E}\times\hat{n}$ 是等效磁流。

### 10.5.2 Volume Integral Equation | 体积分方程 (p. 558)

For inhomogeneous dielectrics / 对非均匀介质：

$$
\mathbf{E}(\mathbf{r}) = \mathbf{E}^{\text{inc}}(\mathbf{r}) + k_0^2\iiint_V (\epsilon_r(\mathbf{r}')-1)\mathbf{E}(\mathbf{r}') G_0(\mathbf{r},\mathbf{r}') dV' + \nabla\iiint_V \frac{(\epsilon_r(\mathbf{r}')-1)\nabla'\cdot\mathbf{E}(\mathbf{r}')}{k_0^2} G_0(\mathbf{r},\mathbf{r}') dV'
$$

**Example 10.3 / 例10.3** (p. 560): 介质球（$\epsilon_r = 4$, $ka=1$）。PMCHWT解与米氏级数吻合。

## 10.6 Periodic Structures | 周期结构 (pp. 564–576)

### 10.6.1 Planar Periodic Green's Function | 平面周期格林函数

For infinite periodic array / 对无限周期阵列：

$$
G_{\text{per}}(\mathbf{r},\mathbf{r}') = \sum_{m=-\infty}^\infty \sum_{n=-\infty}^\infty e^{-j(k_{x0} m D_x + k_{y0} n D_y)} G_0(\mathbf{r},\mathbf{r}' - m D_x\hat{x} - n D_y\hat{y})
$$

Floquet mode expansion in spectral domain / 谱域的弗洛凯模展开。

**Example 10.4 / 例10.4** (p. 570): 微带贴片阵列，$Z_{\text{in}}$ 随频率变化。

## 10.7 Microstrip Antennas and Circuits | 微带天线与电路 (pp. 576–586)

Using layered medium Green's function (SDA — Spectral Domain Approach) / 使用分层媒质格林函数（谱域法）：

$$
\tilde{G}(k_x, k_y) = \frac{1}{k_{z0} + k_{z1}\coth(jk_{z1}h)}
$$

MoM with rooftop basis functions on rectangular cells / 在矩形单元上使用屋顶基函数的矩量法。

**Example 10.5 / 例10.5** (p. 582): 矩形微带贴片天线，输入阻抗随频率变化。

## 10.8 Time-Domain Integral Equations | 时域积分方程 (pp. 586–598)

### 10.8.1 TD-EFIE | 时域EFIE

$$
\hat{n}\times\left[\frac{\mu_0}{4\pi}\iint_S \frac{\partial_t\mathbf{J}_s(\mathbf{r}', t-R/c)}{R} dS' - \frac{1}{4\pi\epsilon_0}\nabla\iint_S \frac{\nabla'\cdot\mathbf{J}_s(\mathbf{r}', t-R/c)}{R} dS'\right] = \hat{n}\times\mathbf{E}^{\text{inc}}
$$

### 10.8.2 Marching-on-in-Time (MoT) | 时间步进法

Lagrange interpolation for temporal basis, spatial basis as in frequency domain / 时间基使用拉格朗日插值，空间基与频域相同。滞后时间积分需要仔细求积。

**Stability / 稳定性**: late-time instability is a known issue, addressed by implicit schemes and averaging / 晚期不稳定性是已知问题，通过隐式格式和平均化处理。

## **Physical Intuition / 物理直觉**
- MoM直接求解等效面电流——可在任意位置通过辐射积分计算场。
- EFIE施加 $\mathbf{E}$ 的边界条件，MFIE施加 $\mathbf{H}$ 的边界条件——它们给出不同的收敛性质。
- CFIE将两者结合，是封闭PEC体的首选方法。
- RWG基确保无人造电荷积累——对精确的电荷/电流表示至关重要。
- 对于介质体，电和磁电流（$\mathbf{J}_s$, $\mathbf{M}_s$）都需要——未知量加倍。

## **Numerical Intuition / 数值直觉**
- MoM矩阵条件数 $\kappa \sim O(1)$ 对MFIE, $\kappa \sim O(1/h)$ 对EFIE（精细网格更差）。
- 介质的PMCHWT比单方程公式条件性更好。
- $N \approx 10(S/\lambda^2)$ 对RWG基，边长为 $\lambda/10$。
- FMM将矩量法矩阵–矢量积从 $O(N^2)$ 加速到 $O(N^{1.5})$（单层）或 $O(N\log N)$（MLFMA）。

## **Audit Table / 审计表**
| Section / 节 | Pages / 页 | Key Formulas / 关键公式 | Verified / 验证 |
|---------|-------|:------------:|:--------:|
| 10.1 | 506–510 | (10.1.1)–(10.1.4) | ✓ |
| 10.2 | 510–516 | 基/检验函数 | ✓ |
| 10.3 | 516–534 | (10.3.15)–(10.3.47) | ✓ |
| 10.4 | 534–552 | RWG, 3D EFIE/MFIE/CFIE | ✓ |
| 10.5 | 552–564 | PMCHWT, VIE | ✓ |
| 10.6 | 564–576 | 周期格林函数 | ✓ |
| 10.7 | 576–586 | 微带分析 | ✓ |
| 10.8 | 586–598 | TD-EFIE, MoT | ✓ |
