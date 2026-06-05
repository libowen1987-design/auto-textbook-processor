# Chapter 11: Volume-Surface Integral Equation
# 第十一章：体-面积分方程（Volume-Surface Integral Equation, VSIE）

**Author 作者**: Cai-Cheng Lu

## 11.1 引言 | Introduction

电磁波与材料涂覆目标的相互作用问题广泛存在于雷达散射截面（RCS）预测、印制电路和微带天线分析等领域。该问题的求解可采用微分方程或积分方程方法。混合边界积分方程法与有限元法（FEM）也被用于解决此类问题。

**关键背景**：
- **FDTD方法**：适合宽带建模，但需要额外的吸收边界条件（ABC）网格划分，导致内存和计算成本增加。
- **表面积分方程（SIE）**：适用于均匀材料涂覆，通过自由空间Green函数 formulation，但计算涉及 Sommerfeld 积分，且假设分层介质无限大。
- **体积分方程（VIE）**：将体积分方程应用于介质区域，面积分方程施加于导体表面，形成 **混合体-面积分方程（VSIE）**。

**VSIE 的核心优势**：
1. 涂层材料可以是**非均匀**的，基底可以是**有限尺寸**的
2. VIE 和 SIE 中的 Green 函数形式简单，便于实现快速求解器
3. 通过多层快速多极子算法（MLFMA）克服未知量增加带来的计算负担

---

## 11.2 积分方程的公式化 | Formulation of the Integral Equations

### 11.2.1 体积分方程（VIE）| Volume Integral Equation

在均匀背景介质 $\varepsilon_b$ 中，电流源 $\mathbf{J}$ 产生的电场满足 Ampere 方程：

$$\nabla \times \mathbf{E} = -j\omega\mu_b \mathbf{H} + \mathbf{J} \tag{11.1}$$

电场可以写为源电流的积分形式：

$$\mathbf{E}^i(\mathbf{r}) = \int_{V'} \overline{\mathbf{G}}(\mathbf{r},\mathbf{r}') \cdot \mathbf{J}(\mathbf{r}') \, dV' \tag{11.2}$$

其中 $\overline{\mathbf{G}}$ 是3D并矢Green函数：

$$\overline{\mathbf{G}}(\mathbf{r},\mathbf{r}') = \left(\overline{\mathbf{I}} + \frac{\nabla\nabla}{k_b^2}\right) \frac{e^{-jk_b R}}{4\pi R} \tag{11.3}$$

当引入介电散射体（相对介电常数 $\varepsilon_r$）后，区域内的波数为：

$$k = k_b \sqrt{\varepsilon_r} \quad \text{（目标区域 V）} \tag{11.4}$$

总电场 $\mathbf{E}^{tot}$ 满足：

$$\nabla \times \mathbf{E}^{tot} - j\omega\mu_b \mathbf{H}^{tot} = \mathbf{J} + \mathbf{J}_{ind} \tag{11.5}$$

其中 $\mathbf{J}_{ind} = j\omega(\varepsilon - \varepsilon_b)\mathbf{E}$ 是**感应电流**。

通过叠加原理，总场 = 主场 + 散射场，得到 **电场体积分方程（EF-VIE）**：

$$\mathbf{E}^{tot}(\mathbf{r}) = \mathbf{E}^{inc}(\mathbf{r}) + \int_V \overline{\mathbf{G}}(\mathbf{r},\mathbf{r}') \cdot [\omega^2\mu_0(\varepsilon(\mathbf{r}') - \varepsilon_b)\mathbf{E}^{tot}(\mathbf{r}')] \, dV' \tag{11.8}$$

这是一个 **第二类 Fredholm 积分方程**。

**低介电对比近似（Born近似）**：当 $\varepsilon_r \approx 1$ 时，可近似用 $\mathbf{E}^{inc}$ 替代 $\mathbf{E}^{tot}$ 于积分核中：

$$\mathbf{E}^{tot}(\mathbf{r}) \approx \mathbf{E}^{inc}(\mathbf{r}) + [\varepsilon_r(\mathbf{r}') - 1] \int_V \overline{\mathbf{G}}(\mathbf{r},\mathbf{r}') \cdot \mathbf{E}^{inc}(\mathbf{r}') \, dV' \tag{11.11}$$

**磁性材料扩展**：当介质具有非真空磁导率 $\mu$ 时，还需引入磁流 $\mathbf{M}_{ind}$，形成一对 VIE 方程（电场和磁场体积分方程）。

### 11.2.2 混合体-面积分方程（VSIE）| Hybrid Volume-Surface Integral Equation

当目标同时包含理想导体（PEC）和介质时：

**表面积分方程（施加零切向电场边界条件）**：

$$\hat{t} \cdot \left[ \int_{S_c} \overline{\mathbf{G}} \cdot \mathbf{J}_s \, dS' + \int_V \overline{\mathbf{G}} \cdot \mathbf{J}_{vol} \, dV' \right] = -\hat{t} \cdot \mathbf{E}^{inc} \quad \text{on } S_c \tag{11.16}$$

**体积分方程（总场 = 主场 + 散射场）**：

$$\mathbf{E}^{tot}(\mathbf{r}) = \mathbf{E}^{inc}(\mathbf{r}) + \int_{S_c} \overline{\mathbf{G}} \cdot \mathbf{J}_s \, dS' + \int_V \overline{\mathbf{G}} \cdot \mathbf{J}_{vol} \, dV' \quad \mathbf{r} \in V \tag{11.17}$$

两个方程**联立求解**得到表面电流 $\mathbf{J}_s$ 和体积电流 $\mathbf{J}_{vol}$。

---

## 11.3 VSIE 的数值求解 | Numerical Solution of the Hybrid VSIE

### 11.3.1 网格生成 | Mesh Generating

**表面网格选项**：
1. 平面三角形patch
2. 平面四边形patch
3. 曲三角形patch
4. 曲四边形patch

**体积网格选项**：
1. 平面四面体（flat-faced tetrahedron）
2. 平面六面体（flat-faced hexahedron）
3. 曲四面体
4. 曲六面体

**配对约束**：表面patch和体积单元必须完全重叠或不重叠（不允许部分重叠），以简化奇异积分处理。合法配对包括：
- 三角形表面 + 四面体体积
- 四边形表面 + 六面体体积
- 曲三角形 + 曲四面体
- 曲四边形 + 曲六面体

> **六面体 vs 四面体**：对于相同边长，六面体网格未知量约为四面体的 1/5，但生成难度更高，不易处理尖锐锥形等几何。

### 11.3.2 混合积分方程的离散化 | Discretization of the Hybrid Integral Equation

**混合位势 formulation**：
将散射场用标量Green函数和矢量位势/标量位势表示（$\mathbf{A}$-$\phi$ formulation），从而将方程中出现的梯度算子转移到测试函数上，降低矩阵元素的奇异阶数。

表面电流用 **屋顶函数（roof-top basis）** 展开：

$$\mathbf{J}_s(\mathbf{r}) \approx \sum_{n=1}^{N_s} I_n^s \mathbf{f}_n^s(\mathbf{r}) \tag{11.21}$$

体积电流（通过 $\mathbf{J}_{vol} = j\omega(\varepsilon - \varepsilon_b)\mathbf{P}$，其中 $\mathbf{P}$ 是极化矢量）展开为：

$$\mathbf{P}(\mathbf{r}) \approx \sum_{n=1}^{N_v} I_n^v \mathbf{f}_n^v(\mathbf{r}) \tag{11.22}$$

使用 **Galerkin测试方法**，最终形成矩阵方程：

$$\begin{bmatrix} Z_{ss} & Z_{sv} \\ Z_{vs} & Z_{vv} \end{bmatrix} \begin{bmatrix} I^s \\ I^v \end{bmatrix} = \begin{bmatrix} V^s \\ V^v \end{bmatrix} \tag{11.33}$$

其中 $Z_{ss}$、$Z_{vv}$ 分别是表面-表面、体积-体积 block，$Z_{sv}$ 和 $Z_{vs}$ 是耦合 block。

**矩阵元素的降阶形式**（利用散度定理转移梯度算子）：

$$Z_{mn}^{ss} = \int_{S_m} \mathbf{f}_m^s \cdot \left[ \int_{S_n} \frac{\mathbf{f}_n^s}{R} - \nabla \left( \int_{S_n} \frac{\nabla' \cdot \mathbf{f}_n^s}{R} dS' \right) \right] dS \tag{11.38}$$

这些积分对四边形和六面体单元可通过高斯数值积分直接计算。

### 11.3.3 网格终止 | Mesh Termination

体积单元需划分为**背景单元**和**介质单元**两类。仅保留包含至少一个介质单元的基函数。背景单元作为"辅助单元"，在数值实现中通过取 $\varepsilon_r \to 1$ 的极限来消除（即"半基函数"）。

**电势不连续性处理**：介电常数在单元界面处存在突变时，感应体电流的法向分量不连续，产生**面电荷密度**：

$$\rho_s \propto (\varepsilon_1 - \varepsilon_2) \mathbf{P} \cdot \hat{n} \tag{11.42}$$

这由屋顶函数的性质自动满足。

### 11.3.4 连续性条件的施加 | Enforcing the Continuity Condition

当介质终止于导体表面时，可施加额外约束：$\hat{n} \cdot \mathbf{J}_{vol} = \rho_s$（面电荷密度），从而**减少未知量**（尤其对薄涂层效果显著）。但这增加了快速求解器实现的复杂性；实际中可选择不显式施加该条件，因为共享基函数本身已自动满足连续性。

### 11.3.5 其他单元形状 | Other Cell Shapes

#### 三角形-四面体配对
- 三角形：RWG基函数（定义在共享一条边的两个三角形上）
- 四面体：3D RWG基函数（定义在共享一个面的两个四面体上）

#### 曲四边形和曲六面体
通过 **Lagrange 插值多项式** 构建高阶映射。**二阶曲四边形**使用9个节点定义：

$$\mathbf{r}(u,v) = \sum_{i=1}^{9} L_i^{(2)}(u,v) \mathbf{r}_i \tag{11.48}$$

数值实验表明：相同patch数量下，**二阶网格**比一阶网格具有更高 RCS 计算精度（尤其对弯曲表面的小球、细杆等几何）。

---

## 11.4 组合场积分方程（CFIE）| Combined Field Integral Equation

CFIE 结合 EFIE 和 MFIE，可加速迭代收敛、解决大网格尺度差异和低频breakdown问题：

$$\text{CFIE} = \alpha \cdot \text{EFIE} + (1-\alpha) \cdot \text{MFIE} \tag{11.52}$$

其中 $\alpha \in (0,1)$，通常取 $\alpha = 0.5$。

MFIE（磁场积分方程）形式为：

$$\hat{n} \times \mathbf{H}^{tot} = \hat{n} \times \left[ \mathbf{H}^{inc} + \int_{S_c} \mathbf{J}_s \times \nabla' G \, dS' + \int_V \mathbf{J}_{vol} \times \nabla' G \, dV' \right] \tag{11.55}$$

数值实现中，奇异面积分通过解析处理化为闭式。

---

## 11.5 奇异积分处理 | Singular Integral Treatments

Green函数中 $1/R$ 的奇异性需要特殊处理。

### 11.5.1 奇异提取法（Singularity Extraction Method）

将积分拆分为正则部分和奇异部分：

$$\int_\Omega \frac{f(\mathbf{r}')}{R} d\Omega' = \int_\Omega \frac{f(\mathbf{r}') - f(\mathbf{r})}{R} d\Omega' + f(\mathbf{r}) \int_\Omega \frac{d\Omega'}{R} \tag{11.59}$$

对于平坦多边形或平顶体积单元，第二项可解析计算。

### 11.5.2 Duffy 变换法 | Duffy Transform Method

适用于一般曲面条元和曲面孔面单元。基本思想：

1. 将**正方形**积分区域（在 $u$-$v$ 参数空间）划分为4个**三角形**，共用奇异点 $(u_0, v_0)$
2. 对每个三角形进行变量变换，将其映射到单位正方形
3. 在新变量下，奇异因子被消除，变为可数值积分的形式

对于曲六面体奇异积分：先将参数立方体划分为6个四面体，各自进行两步变换。

---

## 11.6 快速多极子方法求解 VSIE | Solution of VSIE by FMM

VSIE的FMM处理与SIE几乎相同，唯一区别在于体积基函数多了一个材料因子 $[\varepsilon_r(\mathbf{r}') - 1]$。

远区矩阵元素计算（组间非相邻）：

$$Z_{mn} = \frac{\eta}{4\pi} \int \hat{G}(\hat{k}, \mathbf{r}_{m'} \cdot \mathbf{r}_m) \cdot T_L(\hat{k} \cdot \hat{r}_{mm'}) \cdot \hat{G}^*(\hat{k}, \mathbf{r}_{n'} \cdot \mathbf{r}_n) \, d^2\hat{k} \tag{11.77}$$

**MLFMA内存和CPU时间随未知量 $N$ 的增长斜率接近 $O(N)$**，表明算法具有良好的可扩展性。

**收敛加速技术**：
- 使用 CFIE 而非单独 EFIE
- **相位修正初始猜测**（previous solution × phase correction）作为下一频率/角度迭代的初始猜测，平均迭代次数从>50降至6

---

## 11.7 数值算例 | Numerical Examples

### 11.7.1 VIE 结果 | Results by Volume Integral Equation

1. **均匀介电球**：半径0.5m，$\varepsilon_r = 1.63$，频率300 MHz。与Mie级数解高度吻合。
2. **矩形介电盒**：VIE网格收敛速度**远快于SIE**（因为体积电流分布比表面电流分布更平滑）。
3. **结构化立方网格 vs 非结构化六面体网格**：高介电对比（$\varepsilon_r = 8.8$）时，结构化立方网格即使加密也难以收敛到精确解，而非结构化六面体网格仍能准确建模。
4. **双层球形介质壳**：验证多层非均匀介质问题的求解能力。

### 11.7.2 VSIE 结果 | Results by Hybrid VSIE

1. **涂覆导体球**：核心导体半径0.3m，涂层厚度0.05m，$\varepsilon_r = 4.0 - j0.01$，与Mie级数解和纯SIE结果高度一致。
2. **涂覆双锥体（Ogive）**：验证复杂非旋转对称涂覆目标的RCS计算能力。
3. **近场计算**：介电球壳内的近场分布，与Mie级数解析解完全一致。

### 11.8 其他应用 | Other Applications

#### 11.8.1 室内无线电波传播模拟
- 存在小块介质墙结构的偶极子辐射场计算
- 含介质杆的三室结构传播模拟（展示VSIE处理含小特征电大结构的能力）

#### 11.8.2 微波热效应模拟
- 电磁-热传导耦合分析
- 微波腔内介质样品的复温过程模拟

#### 11.8.3 天线罩（Radome）建模
- **三种天线罩形状对比**：tangent ogive、直锥、半球
- 多层半球天线罩（72,900个六面体单元，内存需求约1.1 GB）
- **波束指向误差**分析

---

## 本章小结 | Summary

本章系统介绍了 **体-面积分方程（VSIE）** 的公式化、离散化和数值求解。主要贡献：

1. **公式化**：VIE处理非均匀介质区域，SIE处理导体表面，两者联立形成统一的混合积分方程
2. **网格策略**：支持多种表面-体积配对（四边形/六面体、三角形/四面体、曲形式），通过严格的配对条件确保奇异积分处理和几何表示的准确性
3. **离散化**：使用屋顶函数（roof-top）和 RWG 基函数，通过混合位势 formulation 和 Galerkin 测试，导出稀疏但非对称的矩阵方程
4. **快速求解**：通过 MLFMA/FMM 将内存和计算复杂度降低至 $O(N)$
5. **工程应用**：成功应用于涂覆目标RCS、室内传播、微波热效应、天线罩分析等多个领域

VSIE 的主要局限在于未知量数目比纯 SIE 多（需对整个介质体积进行网格划分），但这一不足可通过 MLFMA 快速求解器有效克服。
