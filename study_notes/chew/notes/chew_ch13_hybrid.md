# Chapter 13: Hybridization in Computational Electromagnetics
# 第十三章：计算电磁学中的混合方法

**Author 作者**: Jian-Ming Jin and Jian Liu

## 13.1 引言 | Introduction

**混合化（Hybridization）**：将两种或以上不同数值方法或渐近方法结合，以扩展能力、提升处理大规模复杂电磁问题的效率。

### 为什么需要混合化？

以飞机 RCS 预测为例：
- 飞机是**电大尺寸**目标 → 高频渐近方法可高效计算
- 飞机同时包含**许多小特征**（天线罩、缝隙阵列、发动机入口、RAMS 涂层）→ 这些小特征对后向 RCS 有显著贡献，渐近方法精度不足
- 用纯数值方法计算整个飞机 → 即使最强大的超算也过于耗时

**解决思路**：
1. 将小特征全部移除（天线罩→完美导体，缝隙→导体填充，天线→移除）→ 大型简单导体目标 → 用高频渐近方法高效计算
2. 分别用数值方法计算每个小特征的散射 → 叠加到大型目标的散射上

### 两类混合技术

**第一类：不同数值方法的混合**
- 典型代表：**FEM + MOM**
- FEM：稀疏矩阵，适合建模任意几何和非均匀材料，但处理开放区域需近似边界条件
- MOM：Green函数天然满足辐射条件，只需对目标表面或体积离散，但产生稠密矩阵

**第二类：数值方法 + 渐近方法的混合**
- 渐近方法：从几何光学（GO）、物理光学（PO）到 GTD、UTD、PTD、UAT
- 实用方法：**SBR（Shooting and Bouncing Ray）**：结合 GO、PO 和 GTD/UTD 的特点
- 处理问题：
  1. 大型体带小特征（缝隙、腔体、共形天线）
  2. 大型体带小突出物

### 本章覆盖的混合技术

| 混合方法 | 描述 |
|---------|------|
| FEM/ABC | FEM + 吸收边界条件（近似方法）|
| FEM/BIE | FEM + 边界积分方程（精确方法）|
| FEM/AABC | FEM + 自适应吸收边界条件（改进的BIE推导）|
| FEM/SBR | FEM + SBR（大目标 + 小凹陷特征）|
| MOM/SBR | MOM + SBR（大目标 + 小突出特征）|

---

## 13.2 混合 FEM/ABC 技术 | Hybrid FEM/ABC Technique

### 13.2.1 问题陈述

自由空间任意形状散射体（相对介电常数 $\varepsilon_r$，相对磁导率 $\mu_r$）。

引入人工表面 $S$ 包围散射体，内部区域用 FEM 求解。

**二阶矢量波动方程**：

$$\nabla \times \nabla \times \mathbf{E} - k^2 \mathbf{E} = -j\omega \mathbf{J}_{ext} \quad \text{in } V \tag{13.1}$$

**Sommerfeld 辐射条件**（近似施加于截断表面 $S$）：

$$\hat{n} \times (\nabla \times \mathbf{E}^{scat}) + jk \hat{n} \times (\hat{n} \times \mathbf{E}^{scat}) = \mathbf{U} \quad \text{on } S \tag{13.3}$$

### 13.2.2 FEM 分析

**变分原理**：泛函 $\mathcal{F}(\mathbf{E})$ 的平稳点等价于原边界值问题。

$$\mathcal{F}(\mathbf{E}) = \frac{1}{2} \int_V \left[ \frac{1}{\mu_r}|\nabla \times \mathbf{E}|^2 - k^2 \varepsilon_r |\mathbf{E}|^2 \right] dV + \frac{jk}{2} \int_S (\hat{n} \times \mathbf{E}) \cdot (\hat{n} \times \mathbf{E}) \, dS - \int_S \mathbf{E} \cdot \mathbf{U} \, dS \tag{13.5}$$

**FEM 优势**：
- 可建模任意几何（理论上无限制）
- 易于处理非均匀和各向异性材料
- 矩阵**对称且稀疏**（$O(N)$ 存储和计算复杂度）

**FEM/ABC 局限性**：
- ABC 是**近似**的，精度不可预测
- 截断表面必须足够远且形状凸起 → **计算域大**
- 需更细网格来压制色散误差

---

## 13.3 混合 FEM/BIE 技术 | Hybrid FEM/BIE Technique

### 13.3.1 公式化

**核心思想**：用精确的边界积分方程（BIE）替代近似 ABC，使截断表面可任意形状、可紧靠目标放置。

**问题设置**：任意形状非均匀体，相对参数 $\varepsilon_r(\mathbf{r})$，$\mu_r(\mathbf{r})$。引入人工表面 $S$（可与物体表面重合），将问题分为内外两部分。

**FEM 部分**：在 $V$ 内求解矢量波动方程，在 $S$ 上施加边界条件：

$$\hat{n} \times (\nabla \times \mathbf{E}) = -jk \eta \hat{n} \times \mathbf{H} \quad \text{on } S \tag{13.19}$$

**BIE 部分**：在 $S$ 上建立外域场的积分方程。通过**矢量-并矢 Green 第二恒等式**推导：

$$\mathbf{E}(\mathbf{r}) = \mathbf{E}^{inc}(\mathbf{r}) + \int_S \left[ \mathbf{G}_m \cdot (\hat{n} \times \mathbf{E}) + jk \mathbf{G}_e \cdot (\hat{n} \times \mathbf{H}) \right] dS' \quad \mathbf{r} \in V_{ext} \tag{13.28}$$

其中 $\mathbf{G}_e$ 和 $\mathbf{G}_m$ 分别是电型和磁型并矢 Green 函数。

**EFIE 和 MFIE**：从边界上场的关系推导出场积分方程（EFIE）和磁场合积方程（MFIE）。为消除内谐振问题，采用**组合场积分方程（CFIE）**：

$$\text{CFIE} = \alpha \cdot \text{EFIE} + (1-\alpha) \cdot \text{MFIE} \tag{13.40}$$

$\alpha$ 通常取 0.2~0.8。

**最终矩阵方程**（联立 FEM 和 BIE）：

$$\begin{bmatrix} K_{VV} & K_{VS} \\ K_{SV} & K_{SS} + P_{SS} \end{bmatrix} \begin{bmatrix} E_V \\ E_S \end{bmatrix} + \begin{bmatrix} 0 & 0 \\ 0 & Q_{SS} \end{bmatrix} \begin{bmatrix} 0 \\ H_S \end{bmatrix} = \begin{bmatrix} 0 \\ b_S \end{bmatrix} \tag{13.50}$$

这是一个**部分稀疏、部分稠密**的矩阵方程，且**不对称**。

### 13.3.2 MLFMA 的应用

BIE 产生的稠密矩阵是 FEM/BIE 方法的瓶颈：
- 内存需求：$O(N_S^2)$
- 每次矩阵-向量乘法：$O(N_S^2)$

**MLFMA 加速**：
- 通过多层次分组、聚合、转移、解聚，将复杂度降至 $O(N_S \log N_S)$
- 对非相邻组之间的相互作用使用多极子展开近似

**公式**：聚合 → 转移 → 接收

$$\mathbf{V}_{jm} = \int_S e^{jk\hat{k} \cdot \mathbf{r}_{jm}} \mathbf{g}_j \, dS \quad \text{（辐射分量）}$$
$$T_{mm'} = \sum_l (2l+1) h_l^{(2)}(kr_{mm'}) P_l(\hat{k} \cdot \hat{r}_{mm'}) \quad \text{（转移分量）}$$
$$\mathbf{V}_{im'} = \int_S e^{-jk\hat{k} \cdot \mathbf{r}_{im'}} \mathbf{g}_i \, dS \quad \text{（接收分量）}$$

### 13.3.3 数值结果

**涂覆导体球**（单层和双层介质）：
- 与 Mie 级数解高度吻合
- 6 $\lambda$ 直径球（187,202 未知量）：内存 522.5 MB，单次迭代 87.84 秒，总 CPU 时间 130,501 秒

---

## 13.4 混合 FEM/AABC 技术 | Hybrid FEM/AABC Technique

### 13.4.1 核心思想

同时继承 FEM/ABC 和 FEM/BIE 的优点，克服两者的缺点：

| 特性 | FEM/ABC | FEM/BIE | FEM/AABC |
|------|---------|---------|---------|
| 矩阵稀疏性 | ✓ 完全稀疏 | ✗ 部分稠密 | ✓ 完全稀疏 |
| 截断表面形状 | 需凸形 | 任意 | 任意 |
| 表面放置位置 | 需远离目标 | 可紧靠 | 可紧靠 |
| 误差控制 | 不可预测 | 可系统性 | ✓ 可系统性 |
| 内谐振问题 | 无 | 需处理 | ✓ 自然消除 |

### 13.4.2 公式化

**关键创新**：从 BIE 迭代推导出**自适应吸收边界条件（AABC）**，而非直接使用 BIE。

**两层递归嵌入结构**：物体递归嵌入于两个域 $V_1$ 和 $V_2$（边界曲面 $S_1$ 和 $S_2$）。

**$V_2$ 中的方程**：使用电场 formulation（E-equation）
$$\nabla \times \nabla \times \mathbf{E} - k^2 \mathbf{E} = -j\omega \mathbf{J}_{ext} \tag{13.59}$$

**$V_1$ 中的方程**：使用磁场 formulation（H-equation）
$$\nabla \times \nabla \times \mathbf{H} - k^2 \mathbf{H} = \nabla \times \mathbf{J}_{ext} \tag{13.61}$$

**$S_1$ 上的边界条件**（AABC）：

$$\hat{n}_1 \times (\nabla \times \mathbf{H}) + jk \hat{n}_1 \times (\hat{n}_1 \times \mathbf{H}) = \mathbf{V}(\mathbf{r}) \tag{13.62}$$

其中 $\mathbf{V}(\mathbf{r})$ 是从 $S_2$ 上的场值通过 BIE 计算得到的。

**迭代过程**（保证指数收敛）：
1. 令 $\mathbf{R} = 0$，计算激励向量并求解 FEM 方程得到 $S_2$ 上的场值
2. 使用 $S_2$ 上的场值计算 $\mathbf{R}$ 和新的激励向量
3. 重复直至收敛

**最终系统**（完全稀疏且对称）：

$$\begin{bmatrix} K_{V_2 V_2} & K_{V_2 S_2} \\ K_{S_2 V_2} & K_{S_2 S_2} + B_{S_2 S_2} \end{bmatrix} + \begin{bmatrix} 0 & 0 \\ 0 & L_{S_2 S_2} \end{bmatrix} + \cdots = \{b\} \tag{13.77}$$

### 13.4.3 数值结果

**立方体验证**：
- 完整立方体：5次迭代即可收敛
- 凹角立方体：仍快速收敛
- 腔体结构（多 bounce）：使用凸形 $S_1$ 将腔体交由 FEM 处理，收敛性大幅改善

**涂覆介质球**：
- 6 $\lambda$ 直径球，双层涂层 → Mie 解，RMS 误差仅 0.08 dB
- 12 $\lambda$ 直径球，单层涂层 → Mie 解，RMS 误差仅 0.12 dB

**EMCC 基准目标**：金属板边缘涂覆介质层（设计用于测试介电复合材料 RCS 计算精度），在 x-y 平面的单站 RCS 与参考解吻合良好。

---

## 13.5 混合 FEM/SBR 技术 | Hybrid FEM/SBR Technique

### 适用场景

大型散射体 + 小凹陷特征（裂缝、缝隙、腔体、天线等）

### 公式化

大型目标用 SBR（射线光学）处理，凹陷区域用 FEM 处理。

**基本思想**：
1. 用 SBR 计算入射射线打到凹陷区域时的等效入射场
2. 用 FEM 计算凹陷区域在该入射场激励下的散射
3. 将 FEM 解得的散射叠加到 SBR 的总散射上

---

## 13.6 混合 MOM/SBR 技术 | Hybrid MOM/SBR Technique

### 适用场景

大型散射体 + 小突出特征

### 公式化

大型目标用 SBR（MOM 中的 PO/GTD）处理，突出物用 MOM 处理。

**基本思想**：
1. 用 SBR 计算突出物位置的等效入射场
2. 用 MOM 计算每个突出物的散射
3. 包括突出物与大型目标之间的主要相互作用

---

## 本章小结 | Summary

本章系统介绍了计算电磁学中的五类混合技术：

| 方法 | 核心结合 | 主要优势 | 主要应用 |
|------|---------|---------|---------|
| FEM/ABC | FEM + 近似ABC | 矩阵完全稀疏 | 不需高精度的开放区域散射 |
| FEM/BIE | FEM + 精确BIE | 任意截断表面，紧靠目标 | 复杂非均匀目标 |
| FEM/AABC | FEM + 自适应BC | 稀疏+精确+误差可控 | 高精度复杂目标 |
| FEM/SBR | FEM + 射线追踪 | 处理小凹陷+电大目标 | 缝隙、腔体、共形天线 |
| MOM/SBR | MOM + 射线追踪 | 处理小突出+电大目标 | 表面突起、天线安装 |

**数值方法混合（FEM/MOM）的核心洞察**：
- FEM 适合内域（材料非均匀、几何复杂）→ 稀疏矩阵
- MOM 适合外域（开放、辐射条件通过 Green 函数自动满足）→ 只需表面离散
- 两者结合兼得稀疏性和辐射条件精确性

**渐近-数值混合的核心洞察**：
- 电大光滑目标 → 高频渐近方法足够精确
- 小特征处局部非均匀/非光滑 → 数值方法精确建模
- 通过叠加原理组合两者 → 在精度和效率间取得平衡

**FEM/AABC 的迭代误差控制** 展示了如何通过反复修正边界条件，将 BIE 的精确性与 FEM 稀疏矩阵的效率有机结合。
