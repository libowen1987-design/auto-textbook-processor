# Tsang《Scattering of Electromagnetic Waves: Numerical Simulations》
Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao  
Wiley, 2001 — 3 Volumes

> **⚠️ OCR 说明 (IMPORTANT):** 本笔记基于 tesseract OCR 识别原文扫描页面后洗稿。OCR 识别率约 85-90%，部分数学符号和公式可能有误，读时请与原书核对。**严禁仅凭本笔记内容进行学术引用。**

---

## 目录结构 | Table of Contents

- **Volume I: Numerical Simulations** — 本卷主要数值方法
- **Volume II: Advanced Topics** — 增强绕射公式、波传播理论
- **Volume III: Microwave Interaction** — 亮温与被动遥感

---

## 第 1 章：Monte Carlo Simulations of Layered Media
**Source:** Tsang et al., Chapter 1, pp. 1-12 (from OCR)

### 1.1 连续随机介质 (Continuous Random Medium)

**物理背景：**
真实介质并非均匀的，其介电常数 $\varepsilon(\mathbf{r})$ 在空间上存在随机起伏。在遥感应用中，这种起伏对于理解波的散射和热辐射至关重要。

**两种分层模型：**
1. **连续随机介质（Continuous Random Medium）**：介电常数 $\varepsilon(z)$ 是位置 $z$ 的连续随机函数
2. **离散随机分层（Discrete Random Layering）**：层与层之间存在介电常数的突变

**分层介质的物理意义（Fig. 1.1.1）：**
想象一层层叠放的介质板，每层的介电常数 $\varepsilon_i$ 是随机变量。这种模型适用于描述沉积层、冰层、土壤等自然介质。

> **关键洞察：** 连续随机介质和离散随机介质在热辐射（亮度温度）特性上有显著差异——这在反演算法中至关重要。

### 1.2 一维高斯随机介质的生成 (Generation of 1-D Gaussian Random Medium)

**高斯随机过程：**
介电常数的起伏 $\delta\varepsilon(z) = \varepsilon(z) - \langle\varepsilon\rangle$ 服从高斯分布，其统计特性由**自相关函数（autocorrelation function）**描述：

$$R(z - z') = \langle \delta\varepsilon(z) \delta\varepsilon(z') \rangle$$

**谱表示方法（Spectral Representation）：**
利用傅里叶变换生成具有特定谱特性的随机介质：
$$\delta\varepsilon(z) = \int_{-\infty}^{\infty} e^{ik_0 z} \sqrt{S(k_0)} dW(k_0)$$

其中 $S(k_0)$ 是功率谱密度（Power Spectral Density），$dW$ 是维纳过程（Wiener process）的增量。

### 1.3 数值结果与南极应用 (Numerical Results and Applications to Antarctica)

**模型验证：**
蒙特卡洛方法的数值结果与解析理论进行了对比验证，用于确认算法的正确性。

**南极亮温应用：**
- 连续随机介质模型和离散分层模型预测的亮度温度 $T_B$ 有显著差异
- 为匹配实际观测的南极亮温，两种模型需要使用**截然不同的物理参数**
- 这说明：在遥感反演中，介质的**随机结构假设**对结果影响巨大

**物理洞察：** 连续随机介质模型与离散分层模型的不一致性，表明我们在建立散射模型时必须谨慎选择介质的统计描述方式。

---

## 第 2 章：Integral Equation Formulations and Basic Numerical Methods
**Source:** Tsang et al., Chapter 2, pp. 13-57 (from OCR)

### 2.1 积分方程形式 (Integral Equation Formulation)

**表面电流积分方程：**
对于粗糙表面散射问题，表面电流密度 $\mathbf{J}(\mathbf{r})$ 满足：

$$\oint_S G(\mathbf{r}, \mathbf{r}') \mathbf{J}(\mathbf{r}') ds' = \mathbf{E}^{\text{inc}}(\mathbf{r})$$

其中 $G(\mathbf{r}, \mathbf{r}')$ 是**格林函数（Green's function）**：

$$G(\mathbf{r}, \mathbf{r}') = \frac{e^{jk|\mathbf{r} - \mathbf{r}'|}}{4\pi |\mathbf{r} - \mathbf{r}'|}$$

### 2.2 矩量法 (Method of Moments / MoM)

**离散化步骤：**
1. **基函数展开：** $\mathbf{J} \approx \sum_{n=1}^{N} I_n \mathbf{f}_n(\mathbf{r})$
2. **配置点法（Point Matching）或 Galerkin 法** 构造矩阵方程
3. 形成 $N \times N$ 阻抗矩阵 $Z_{mn} = \langle \mathbf{f}_m, \mathcal{L}\mathbf{f}_n \rangle$
4. 求解 $Z \cdot \mathbf{I} = \mathbf{V}$

**计算复杂度：** $O(N^2)$ — 每次矩阵-向量乘法需要 $N^2$ 次操作，$N$ 通常为 $10^3$ 到 $10^6$

### 2.3 快速方法 (Fast Methods)

| 方法 | 复杂度 | 原理 |
|------|--------|------|
| **SMCG** (Sparse-Matrix Canonical Grid) | $O(N)$ | 稀疏矩阵 + 规则网格 |
| **FMM** (Fast Multipole Method) | $O(N \log N)$ | 多极展开 |
| **MLFMA** (多层快速多极子) | $O(N \log N)$ | 分层多极子 |

### 2.4 离散偶极子近似 (Discrete Dipole Approximation, DDA)

**物理模型：**
将目标离散为 $N$ 个小立方体，每个立方体具有电极化率 $\alpha_i$。偶极子极化 $\mathbf{P}_i = \alpha_i \mathbf{E}_i$。

**辐射修正（Radiative Corrections）：**
包含自相互作用（self-interaction）的修正项，确保结果符合光学定理（forward scattering = total scattering - backscattering）。

---

## 第 3 章：Scattering and Emission by a Periodic Rough Surface
**Source:** Tsang et al., Chapter 3, pp. 58-112 (from OCR)

### 3.1 弗洛凯定理与布洛赫条件 (Floquet's Theorem and Bloch Condition)

**周期性边界条件：**
对于周期粗糙表面，设周期为 $d$，则表面高度满足 $h(x + d) = h(x)$。

弗洛凯定理给出准平面波解：
$$\psi(x + d, z) = \psi(x, z) e^{-jk_x d}$$

其中 $k_x$ 是 $x$ 方向的准波数（quasi-wave number）。

### 3.2 双站散射系数 (Bistatic Scattering Coefficients)

**定义：**
$$\sigma_{pq}(\theta_s, \phi_s; \theta_i, \phi_i) = \lim_{r\to\infty} \frac{4\pi r^2 |E_{ps}|^2}{|E_{qi}|^2 \cos\theta_i A}$$

其中 $p,q \in \{h, v\}$ 表示极化状态，$\theta_i$ 是入射角，$\theta_s$ 是散射角，$A$ 是照射面积。

### 3.3 T矩阵法 (T-Matrix Method)

对于介质周期表面，使用T矩阵法求解。T矩阵建立了入射场展开系数与散射场展开系数之间的线性关系：

$$\begin{pmatrix} a^s \\ b^s \end{pmatrix} = \begin{pmatrix} T^{11} & T^{12} \\ T^{21} & T^{22} \end{pmatrix} \begin{pmatrix} a^i \\ b^i \end{pmatrix}$$

### 3.4 Ewald 方法 (Ewald's Method)

**目的：** 加速计算周期格林函数的收敛性。

将格林函数分解为两个快速收敛的部分：
$$G(\mathbf{r}) = G_{\text{real}}(\mathbf{r}) + G_{\text{rec}}(\mathbf{r})$$

- $G_{\text{real}}$: 实空间贡献，短程作用
- $G_{\text{rec}}$: 倒空间贡献，由晶格求和得到

---

## 第 4 章：Random Rough Surface Simulations
**Source:** Tsang et al., Chapter 4, pp. 111-158 (from OCR)

### 4.1 粗糙度统计描述

**高度起伏的统计量：**
- **均方根高度（RMS height）：** $\sigma_h = \sqrt{\langle h^2 \rangle - \langle h \rangle^2}$
- **相关长度（Correlation length）：** $l_c$，定义为自相关函数 $R(\rho) = \langle h(\mathbf{r}) h(\mathbf{r}+\boldsymbol{\rho}) \rangle$ 下降到 $R(0)/e$ 时的距离

**高斯相关函数：**
$$R(\rho) = \sigma_h^2 \exp\left(-\frac{\rho^2}{l_c^2}\right)$$

### 4.2 小扰动法 (Small Perturbation Method, SPM)

**适用条件：** $\sigma_h < \lambda/10$ 且 $l_c > \lambda$

**散射强度的一阶SPM结果：**
$$\sigma_{\text{spm}} \propto \sigma_h^2 k^4 |V(k_x)|^2$$

其中 $k = 2\pi/\lambda$ 是波数，$V(k_x)$ 是表面高度功率谱。

### 4.3 数值方法比较

| 方法 | 适用条件 | 计算量 |
|------|---------|--------|
| SPM | $\sigma_h \ll \lambda$ | 小 |
| MoM | 任意粗糙度 | $O(N^2)$ |
| FDTD | 3D问题 | 大 |
| BIE | 2D问题 | 中 |

---

## 第 5 章：Fast Computational Methods
**Source:** Tsang et al., Chapter 5, pp. 159-240 (from OCR)

### 5.1 稀疏矩阵 Canonical Grid (SMCG) 方法

**核心思想：** 将远距离相互作用矩阵稀疏化，通过**规则网格（canonical grid）**近似。

**计算步骤：**
1. 将目标区域划分为规则网格
2. 在网格上进行 FFT
3. 利用稀疏近似计算矩阵-向量乘积

### 5.2 共轭梯度法 (Conjugate Gradient Method)

**迭代求解：** 对于大型线性系统 $Ax = b$，共轭梯度法（CG）在 $A$ 为对称正定时最多 $N$ 步收敛。

**收敛条件：** 
- 误差范数按 $|\mathbf{r}_k|^2 / |\mathbf{r}_0|^2 \leq \varepsilon^2$ 控制
- 每步计算量 $O(N)$（矩阵-向量乘积）

---

## 第 6 章：Three-Dimensional Wave Scattering
**Source:** Tsang et al., Chapter 6, pp. 241-310 (from OCR)

### 6.1 矢量积分方程

三维粗糙表面散射需同时考虑电场和磁场的边界条件，形成**耦合的积分方程组**：

$$\hat{n} \times \mathbf{E}^{\text{inc}} = \hat{n} \times \left[ \oint_S G \mathbf{J} ds' + \nabla \times \oint_S G \mathbf{M} ds' \right]$$

$$\hat{n} \times \mathbf{H}^{\text{inc}} = \hat{n} \times \left[ -\nabla \times \oint_S G \mathbf{J} ds' + \oint_S G \mathbf{M} ds' \right]$$

其中 $\mathbf{J}$ 是电流密度，$\mathbf{M}$ 是磁流密度。

### 6.2 极化散射矩阵 (Polarimetric Scattering Matrix)

** Sinclair 矩阵：**
$$\begin{pmatrix} E_v^s \\ E_h^s \end{pmatrix} = \begin{pmatrix} S_{vv} & S_{vh} \\ S_{hv} & S_{hh} \end{pmatrix} \begin{pmatrix} E_v^i \\ E_h^i \end{pmatrix}$$

**极化相位模式（Polarimetric Phase Difference）：**
$$\delta = \arg(S_{vv}) - \arg(S_{hh})$$
该相位差与介质特性（如土壤水分）有强相关。

---

## 第 7 章：Volume Scattering Simulations
**Source:** Tsang et al., Chapter 7, pp. 311-370 (from OCR)

### 7.1 体积散射的物理机制

体积散射发生在介质内部，如云层、植被、积雪、雪层中。入射波在介质体内的随机不均匀性上发生多次散射。

**相函数（Phase Function）：**
$$p(\theta, \phi; \theta', \phi') = \frac{4\pi}{\sigma_s} \frac{d\sigma}{d\Omega}$$

描述散射方向的概率分布。

### 7.2 辐射传输方程 (Radiative Transfer Equation, RTE)

$$\frac{dI}{ds} = -\kappa_e I + \kappa_s \int_{4\pi} p(\Omega, \Omega') I(\Omega') d\Omega'$$

其中：
- $\kappa_e = \kappa_a + \kappa_s$：消光系数（extinction coefficient）
- $\kappa_a$：吸收系数
- $\kappa_s$：散射系数
- $I$：辐射强度（radiance）

---

## 第 8-13 章：高密度介质与相关函数
**Source:** Tsang et al., Chapters 8-13 (from OCR)

### 8-13 核心概念

**密集介质模型（Dense Media）：**
当散射体密度增大时，**多散射效应（multiple scattering）** 变得显著，单次散射近似不再成立。

**准晶格近似（Quasi Crystalline Approximation, QCA）：**
考虑散射体之间的相关效应，对密集介质中波传播进行近似分析。

**角度相关函数（Angular Correlation Function, ACF）：**
$$C(\theta_1, \phi_1; \theta_2, \phi_2) = \langle S^*(\theta_1, \phi_1) S(\theta_2, \phi_2) \rangle$$
描述散射场在不同方向之间的相关性。

---

## 附录：Tsang 三卷本体系

| 卷 | 主题 | 核心方法 |
|----|------|---------|
| Volume I | Numerical Simulations | Monte Carlo, MoM, DDA, SMCG, MLFMA |
| Volume II | Advanced Topics | Enhanced Diffraction, Wave Propagation |
| Volume III | Microwave Interaction | Brightness Temperature, Passive Remote Sensing |

---

## 笔记说明

本笔记基于 tesseract OCR 对原书扫描页的识别结果洗稿整理。由于 OCR 识别率限制，笔记中**可能存在错误**，请以原书为准。