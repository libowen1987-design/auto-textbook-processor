---
chapter: 7
title: Perfectly Matched Layer Absorbing Boundary Conditions
book: Computational Electrodynamics — The Finite-Difference Time-Domain Method (3rd Ed.)
author: Stephen Gedney
raw_size: 114,254 bytes
sections: 9
---

# Chapter 7: Perfectly Matched Layer (PML) Absorbing Boundary Conditions
> **中英双语版**

> 完美匹配层吸收边界条件

## 7.1 Introduction
> 引言

PML, introduced by Berenger (1994), is an absorbing material ABC that is reflectionless for plane waves of arbitrary incidence, polarization, and frequency. Unlike analytical ABCs (Ch6), PML works for inhomogeneous, dispersive, anisotropic, and nonlinear media.
> PML 由 Berenger（1994）提出，是一种吸收材料型吸收边界条件，对任意入射角、极化和频率的平面波无反射。与分析型吸收边界条件（第6章）不同，PML 适用于非均匀、色散、各向异性和非线性介质。

**Evolution:** Split-field PML → Stretched-coordinate PML → UPML (Uniaxial PML) → CPML (Convolutional PML)
> **发展历程：** 分裂场 PML → 拉伸坐标 PML → 单轴 PML → 卷积 PML

## 7.2 Plane Wave Incident Upon a Lossy Half-Space
> 平面波入射有耗半空间

Conventional lossy materials are matched only for normal incidence. For a plane wave at angle $\theta$:
> 传统有耗材料仅在正入射时匹配。对于入射角 $\theta$ 的平面波：
$$R(\theta) = \frac{\eta_2 \cos\theta - \eta_1 \cos\theta_t}{\eta_2 \cos\theta + \eta_1 \cos\theta_t}$$
where $\eta_1 = \sqrt{\mu_0/\epsilon_0}$ and $\eta_2 = \sqrt{j\omega\mu_0/(\sigma + j\omega\epsilon_0)}$.
> 其中 $\eta_1 = \sqrt{\mu_0/\epsilon_0}$ 为真空波阻抗，$\eta_2 = \sqrt{j\omega\mu_0/(\sigma + j\omega\epsilon_0)}$ 为有耗介质波阻抗。

## 7.3 Berenger's Split-Field PML
> Berenger 分裂场 PML

Berenger split each field component into two orthogonal components:
> Berenger 将每个场分量分裂为两个正交分量：
$$E_z = E_{zx} + E_{zy}, \quad H_z = H_{zx} + H_{zy}$$

### 7.3.1 2D TE$_z$ Case
> 二维 TE$_z$ 情况

Maxwell's equations modified for the split-field PML:
> 针对分裂场 PML 修改的麦克斯韦方程：
$$\epsilon_0 \frac{\partial E_{zx}}{\partial t} + \sigma_x E_{zx} = \frac{\partial H_y}{\partial x}$$
$$\epsilon_0 \frac{\partial E_{zy}}{\partial t} + \sigma_y E_{zy} = -\frac{\partial H_x}{\partial y}$$
$$\mu_0 \frac{\partial H_x}{\partial t} + \sigma_x^* H_x = -\frac{\partial E_z}{\partial x} \quad \text{(split similarly)}$$

**Perfect matching condition:** Loss parameters must satisfy:
> **完美匹配条件：** 损耗参数必须满足：
$$\frac{\sigma_x}{\epsilon_0} = \frac{\sigma_x^*}{\mu_0} \quad \text{and} \quad \frac{\sigma_y}{\epsilon_0} = \frac{\sigma_y^*}{\mu_0} \tag{7.8}$$

When the PML conductivity $\sigma_x$ and magnetic loss $\sigma_x^*$ satisfy (7.8), the PML/vacuum interface has zero reflection for all angles and frequencies.
> 当 PML 电导率 $\sigma_x$ 和磁损耗 $\sigma_x^*$ 满足 (7.8) 时，PML/真空界面对所有角度和频率的反射为零。

Inside the PML, the wave decays as:
> 在 PML 内部，波按如下方式衰减：
$$e^{-\sigma_x \eta \cos\theta \cdot x} \quad \text{where } \eta = \sqrt{\mu_0/\epsilon_0}$$

## 7.4 Stretched-Coordinate Formulation
> 拉伸坐标公式

The PML can be interpreted as a coordinate stretching into complex space:
> PML 可以解释为坐标向复空间的拉伸：
$$\tilde{x} = \int_0^x s_x(x') dx', \quad s_x = 1 + \frac{\sigma_x}{j\omega\epsilon_0}$$

Maxwell's equations in stretched coordinates:
> 拉伸坐标下的麦克斯韦方程：
$$\nabla_s \times \mathbf{H} = j\omega\epsilon_0 \mathbf{E}$$
$$\nabla_s \times \mathbf{E} = -j\omega\mu_0 \mathbf{H}$$
where $\nabla_s = \hat{x}\frac{1}{s_x}\frac{\partial}{\partial x} + \hat{y}\frac{1}{s_y}\frac{\partial}{\partial y} + \hat{z}\frac{1}{s_z}\frac{\partial}{\partial z}$.
> 其中 $\nabla_s$ 为拉伸坐标下的旋度算符。

## 7.5 Uniaxial PML (UPML)
> 单轴 PML

The UPML is a physical anisotropic medium with permittivity and permeability tensors:
> UPML 是一种物理各向异性介质，具有介电常数和磁导率张量：
$$\bar{\bar{\epsilon}} = \epsilon_0 \epsilon_r \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & s_z \end{bmatrix}, \quad
\bar{\bar{\mu}} = \mu_0 \mu_r \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & s_z \end{bmatrix} \tag{7.53}$$
where $s_x = \kappa_x + \frac{\sigma_x}{j\omega\epsilon_0}$, and the matching condition $s_x = s_y = s_z$ ensures zero reflection.
> 其中 $s_x = \kappa_x + \frac{\sigma_x}{j\omega\epsilon_0}$，匹配条件 $s_x = s_y = s_z$ 确保零反射。

### 7.5.1 Perfectly Matched Uniaxial Medium
> 完美匹配单轴介质

The reflection coefficient at a UPML interface is zero when:
> UPML 界面处的反射系数为零的条件：
$$s_x = s_y, \quad \epsilon_1 = \epsilon_2, \quad \mu_1 = \mu_2$$

### 7.5.2 Relation to Berenger's Split-Field PML
> 与 Berenger 分裂场 PML 的关系

The UPML is equivalent to Berenger's split-field formulation when $s_x = 1 + \sigma_x/(j\omega\epsilon_0)$. The key advantage of UPML is avoiding nonphysical field splitting.
> UPML 在 $s_x = 1 + \sigma_x/(j\omega\epsilon_0)$ 时等价于 Berenger 分裂场公式。UPML 的关键优势在于避免了非物理的场分裂。

## 7.6 Theoretical PML Performance
> PML 理论性能

### 7.6.1 Continuous Space
> 连续空间

The theoretical reflection error for a PEC-backed PML of thickness $d$:
> 理想导体衬底 PML 厚度为 $d$ 时的理论反射误差：
$$R(\theta) = e^{-2\sigma \eta d\cos\theta / (m+1)} \tag{7.58}$$

### 7.6.2 Discrete Space — Loss Parameter Grading
> 离散空间——损耗参数渐变

**Polynomial grading:**
> **多项式渐变：**
$$\sigma_x(x) = \left(\frac{x}{d}\right)^m \sigma_{x,\text{max}} \tag{7.60}$$
$$\sigma_{x,\text{max}} \approx -\frac{(m+1) \ln R(0)}{2\eta d} \tag{7.62}$$

**Geometric grading:**
> **几何渐变：**
$$\sigma_x(x) = \sigma_{x,0} g^{x/\Delta} \tag{7.63}$$

## 7.7 Complex Frequency-Shifted (CFS) Tensor
> 复频移张量

Improves PML absorption of evanescent waves and late-time reflections:
> 改善 PML 对倏逝波的吸收和后期反射：
$$s_x = \kappa_x + \frac{\sigma_x}{\alpha_x + j\omega\epsilon_0} \tag{7.55}$$

Typical values: $\kappa_x = 1$–11, $\alpha_x = 0.001$–0.05.
> 典型值范围：$\kappa_x = 1$–11，$\alpha_x = 0.001$–0.05。

## 7.8 UPML Implementation in FDTD
> FDTD 中的 UPML 实现

Using the ADE (Auxiliary Differential Equation) approach:
> 使用辅助微分方程方法：
$$\mathbf{D} = \epsilon_0 \bar{\bar{\epsilon}}_r \mathbf{E}$$

The update equations involve integrating $s_x$ factors via time-domain recursions.
> 更新方程通过时域递归积分 $s_x$ 因子。

For example, the $D_x$ to $E_x$ conversion:
> 例如，$D_x$ 到 $E_x$ 的转换：
$$E_x = \frac{1}{\epsilon_0} \left[ \frac{D_x}{\kappa_x} - \psi_{E_x}^n \right]$$
where $\psi_{E_x}$ is an accumulated convolution term:
> 其中 $\psi_{E_x}$ 是累积的卷积项：
$$\psi_{E_x}^n = b_x \psi_{E_x}^{n-1} + a_x \left( \frac{D_x^{n-1}}{\kappa_x} \right)$$
$$b_x = e^{-(\sigma_x/\kappa_x + \alpha_x)\Delta t/\epsilon_0}, \quad a_x = \frac{\sigma_x}{\kappa_x(\sigma_x + \kappa_x\alpha_x)} (b_x - 1)$$

## 7.9 CPML (Convolutional PML)
> 卷积 PML

Roden & Gedney's CPML applies stretched-coordinate PML via discrete convolution:
> Roden & Gedney 的 CPML 通过离散卷积应用拉伸坐标 PML：
$$\frac{\partial}{\partial\tilde{x}} = \frac{1}{\kappa_x} \frac{\partial}{\partial x} + \zeta_x(t) * \frac{\partial}{\partial x}$$
where $\zeta_x(t) = -\frac{\sigma_x}{\epsilon_0 \kappa_x^2} e^{-(\sigma_x/\kappa_x + \alpha_x)t/\epsilon_0} u(t)$ is implemented recursively.
> 其中 $\zeta_x(t) = -\frac{\sigma_x}{\epsilon_0 \kappa_x^2} e^{-(\sigma_x/\kappa_x + \alpha_x)t/\epsilon_0} u(t)$ 通过递归方式实现。

---

## Example 7.1: 1D FDTD with PML Terminal
> 示例 7.1：带 PML 终端的一维 FDTD

Implement an 8-cell PML to terminate a 1D grid. Compare reflection vs. Mur ABC.
> 实现 8 网格单元的 PML 终端来截断一维网格。与 Mur ABC 进行反射对比。

**Setup:** 200-cell vacuum, PML thickness $d = 8\Delta$, polynomial grading $m=3$, $\sigma_{\text{max}}$ from $R(0) = 10^{-4}$.
> **设置：** 200 网格单元真空，PML 厚度 $d = 8\Delta$，多项式渐变 $m=3$，由 $R(0) = 10^{-4}$ 确定 $\sigma_{\text{max}}$。

**Result:** PML achieves $R < -60$ dB vs. Mur's $-30$ dB.
> **结果：** PML 实现 $R < -60$ dB，而 Mur 仅为 $-30$ dB。

---

## Example 7.2: 2D TM$_z$ UPML — Reflection Error vs. PML Thickness
> 示例 7.2：二维 TM$_z$ UPML——反射误差与 PML 厚度的关系

Compute reflection error for a 2D domain as function of PML thickness $d$ and grading order $m$.
> 计算二维区域中反射误差作为 PML 厚度 $d$ 和渐变阶数 $m$ 的函数。

**Setup:** 80×80 cell grid with UPML on all sides. Point source at center. Measure $E_z$ at probe point near PML interface.
> **设置：** 80×80 网格，四面 UPML。中心点源。在 PML 界面附近的探针点测量 $E_z$。

**Result:** $d=8$, $m=3$ gives $R \approx -60$ dB; $d=16$, $m=4$ gives $R \approx -80$ dB.
> **结果：** $d=8$、$m=3$ 时 $R \approx -60$ dB；$d=16$、$m=4$ 时 $R \approx -80$ dB。

---

## Example 7.3: CFS-CPML Absorption of Evanescent Waves
> 示例 7.3：CFS-CPML 对倏逝波的吸收

Compare standard PML vs. CFS-CPML for termination close to a metallic edge (strong evanescent fields).
> 比较标准 PML 与 CFS-CPML 在靠近金属边缘（强倏逝场）处的截断性能。

**Setup:** Thin wire radiating 0.1$\lambda_0$ from PML boundary. CFS parameters $\kappa_{\text{max}}=5$, $\alpha=0.02$.
> **设置：** 细线辐射源距离 PML 边界 0.1$\lambda_0$。CFS 参数 $\kappa_{\text{max}}=5$、$\alpha=0.02$。

**Result:** CFS-CPML reduces late-time reflections by 20+ dB compared to standard PML.
> **结果：** CFS-CPML 相比标准 PML 将后期反射降低 20 dB 以上。

---

## Audit Table
> 审计表

| Concept | Section | Key Equation | Implementation |
|---------|---------|-------------|----------------|
| 概念 | 章节 | 关键方程 | 实现 |
| Loss half-space matching | 7.2 | — | — |
| 有耗半空间匹配 | 7.2 | — | — |
| Berenger split-field | 7.3 | (7.11) | — |
| Berenger 分裂场 | 7.3 | (7.11) | — |
| Perfect matching condition | 7.3 | (7.8) | — |
| 完美匹配条件 | 7.3 | (7.8) | — |
| Stretched-coordinate PML | 7.4 | (7.26) | — |
| 拉伸坐标 PML | 7.4 | (7.26) | — |
| UPML tensor | 7.5 | (7.53) | Example 7.2 |
| UPML 张量 | 7.5 | (7.53) | 示例 7.2 |
| Reflection error (continuous) | 7.6 | (7.58) | — |
| 反射误差（连续空间） | 7.6 | (7.58) | — |
| Polynomial grading | 7.6 | (7.60)-(7.62) | Example 7.1 |
| 多项式渐变 | 7.6 | (7.60)-(7.62) | 示例 7.1 |
| Geometric grading | 7.6 | (7.63) | — |
| 几何渐变 | 7.6 | (7.63) | — |
| CFS tensor | 7.7 | (7.55) | Example 7.3 |
| CFS 张量 | 7.7 | (7.55) | 示例 7.3 |
| UPML ADE implementation | 7.8 | — | Example 7.2 |
| UPML ADE 实现 | 7.8 | — | 示例 7.2 |
| CPML recursive convolution | 7.9 | — | Example 7.3 |
| CPML 递归卷积 | 7.9 | — | 示例 7.3 |

> **Numerical Intuition:** PML is the gold standard for lattice truncation in FDTD. With $d = 8$–16 cells and $m = 3$–4 polynomial grading, reflection errors below $-80$ dB are routine. The CPML with CFS tensor coefficients is preferred for evanescent fields and dispersive media. PML thickness is one of the key trade-offs: thicker PML → lower reflection but more computational overhead. For most problems, 10 cells of PML with $m=3$ grading is a good starting point.
> **数值直觉：** PML 是 FDTD 网格截断的金标准。使用 $d = 8$–16 个网格单元和 $m = 3$–4 的多项式渐变，反射误差低于 $-80$ dB 是常规水平。带 CFS 张量系数的 CPML 对倏逝场和色散介质效果更优。PML 厚度是关键权衡之一：更厚的 PML 反射更低但计算开销更大。对于大多数问题，10 个网格单元、$m=3$ 渐变的 PML 是良好的起始选择。
