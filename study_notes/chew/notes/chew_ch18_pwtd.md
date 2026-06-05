# 第 18 章：平面波时域算法
# Chapter 18: Plane-Wave Time-Domain Algorithms

---

## 18.1 引言 | Introduction

线性瞬态波现象的计算机模拟涉及位于无界介质中的结构，在声学、电磁学和地球物理学等领域具有重要的广泛应用。

Computer simulation of linear transient wave phenomena involving structures that reside in an unbounded medium to generate broadband data is of paramount importance in such disciplines as acoustics, electromagnetics, and geophysics.

**核心挑战 | Core Challenge:**

数值技术需要对推迟时间边界积分（RTBIs）进行评估，这些积分将已知瞬态源分布与它们辐射的场联系起来。

Numerical techniques call for the evaluation of retarded-time boundary integrals (RTBIs), which relate known transient source distributions to the fields they radiate.

**传统技术的局限 | Limitations of Classical Techniques:**

使用经典技术评估RTBIs是计算代价高昂的程序，限制了数值瞬态分析技术对小型问题的适用性。

Evaluation of RTBIs using classical techniques is a computationally expensive procedure limiting the applicability of numerical transient analysis techniques to a small number of problems.

**PWTD算法 | PWTD Algorithm:**

本章介绍两种显著降低RTBIs评估成本的PWTD算法，通过使用平面波基函数。

This chapter introduces two PWTD algorithms that considerably reduce the cost of evaluating RTBIs by using plane wave bases.

### 18.1.1 两种PWTD算法 | Two PWTD Algorithms

**第一种PWTD算法（非窗口化）| First PWTD Algorithm (Non-Windowed):**

基于Whittaker类型场展开（即用向所有方向传播的平面波表示辐射场的表示）。

Based on a Whittaker-type field expansion (i.e., a representation of the radiated field in terms of plane waves that propagate in all directions).

在双层和多层设置中使用此PWTD算法加速MOT方案，分别将散射分析的 $O(N_t N_s^2)$ 计算复杂度降低到 $O(N_t N_s^{1.5})$ 和 $O(N_t N_s \log N_s)$。

Using this PWTD algorithm in two-level and multilevel settings reduces the computational complexity of scattering analysis from $O(N_t N_s^2)$ to $O(N_t N_s^{1.5})$ and $O(N_t N_s \log N_s)$ respectively.

**第二种PWTD算法（窗口化）| Second PWTD Algorithm (Windowed):**

基于有限锥表示，其中仅使用观察域所含锥内的平面波来表示辐射场。

Relies on a finite-cone representation in which only plane waves whose propagation directions fall within a cone encompassing the observation domain are used.

计算复杂度可分别降低到 $O(N_t N_s^{1.33})$ 和 $O(N_t N_s)$。

Computational costs can scale as low as $O(N_t N_s^{1.33})$ and $O(N_t N_s)$ respectively.

---

## 18.2 时间步进法（MOT）| The Marching-On-in-Time Method

### 18.2.1 问题描述 | Problem Description

考虑入射场 $\mathbf{E}^i(\mathbf{r}, t)$ 入射到表面为 $S$ 的散射体上。

Consider a field $\mathbf{E}^i(\mathbf{r}, t)$ that is incident on a scatterer bounded by a surface $S$.

总场 $\mathbf{E}^{tot} = \mathbf{E}^i + \mathbf{E}^s$ 在 $S$ 上满足Dirichlet边界条件。

The total field $\mathbf{E}^{tot} = \mathbf{E}^i + \mathbf{E}^s$ satisfies the homogeneous Dirichlet condition on $S$.

### 18.2.2 积分方程 | Integral Equation

未知源密度 $\mathbf{J}(\mathbf{r}, t)$ 可通过在 $S$ 上施加边界条件与已知入射场关联：

The unknown source density $\mathbf{J}(\mathbf{r}, t)$ can be related to the known incident field by enforcing the boundary condition:

$$\hat{n} \times \mathbf{E}^i(\mathbf{r}, t) = \hat{n} \times \int_S \frac{\mathbf{J}(\mathbf{r}', t_R)}{4\pi |\mathbf{r}-\mathbf{r}'|} dS' \tag{18.3}$$

其中 $t_R = t - |\mathbf{r}-\mathbf{r}'|/c$ 是推迟时间。

where $t_R = t - |\mathbf{r}-\mathbf{r}'|/c$ is the retarded time.

### 18.2.3 MOT离散 | MOT Discretization

**空间基函数 | Spatial Basis Functions:**

$$\mathbf{J}(\mathbf{r}, t) = \sum_{n=1}^{N_s} \sum_{m=0}^{M_t-1} I_n^m \mathbf{f}_n(\mathbf{r}) T_m(t) \tag{18.4}$$

**MOT矩阵方程 | MOT Matrix Equation:**

$$[Z] \{I\}^{n+1} = \{V\}^n - \sum_{l=1}^{n-1} [Z] \{I\}^l \tag{18.5}$$

### 18.2.4 传统MOT复杂度 | Classical MOT Complexity

评估右侧求和涉及在 $S$ 上 $N_s$ 个点处评估所有过去源产生的场。

The evaluation of the summation on the right-hand side entails the evaluation of the field $\mathbf{E}^s(\mathbf{r}_i, t_n)$ at $N_s$ points on $S$ due to all past sources.

**计算复杂度 | Computational Complexity:**
- 每次时间步：$O(N_s^2)$
- 总共 $N_t$ 步：$O(N_t N_s^2)$

---

## 18.3 平面波时域算法 | The Plane-Wave Time-Domain Algorithm

### 18.3.1 平面波分解 | Plane Wave Decomposition

**Whittaker型表示 | Whittaker-Type Representation:**

$$\phi(\mathbf{r}, t) = \int_{4\pi} \int_{-\infty}^{\infty} \delta(t - \hat{k} \cdot \mathbf{r}/c) \cdot [\text{radial integration}] d\omega d\Omega_k \tag{18.10}$$

### 18.3.2 三阶段PWTD算法 | Three-Stage PWTD Algorithm

**第一阶段：出射射线构建（斜堆变换 SST）**

$$\psi(\hat{k}, t) = \int_\Omega \frac{\delta(t - \hat{k} \cdot \mathbf{r}'/c)}{|\mathbf{r}-\mathbf{r}'|} s(\mathbf{r}') d\Omega' \tag{18.17}$$

$\psi(\hat{k}, t)$ 可解释为沿方向 $\hat{k}$ 传播的出射射线。

**第二阶段：平移**

$$u(\hat{k}, t) = \int_{-\infty}^{\infty} T(\hat{k}, \hat{k}_0, \tau) \psi(\hat{k}_0, t-\tau) d\tau \tag{18.18}$$

$T(\hat{k}, \hat{k}_0, \tau)$ 是平移函数，将出射射线从源球转换到观察球。

$T(\hat{k}, \hat{k}_0, \tau)$ is the translation function that translates each outgoing ray from the source sphere to the observer sphere.

**第三阶段：投影**

$$f(\mathbf{r}, t) = \int_{4\pi} D(\hat{k}, \mathbf{r}, \tau) u(\hat{k}, t-\tau) d\Omega_k \tag{18.19}$$

### 18.3.3 鬼信号问题与时间门控 | Ghost Signal Problem and Time Gating

Naive应用平面波分解会导致鬼信号——在源信号存在之前就出现在观察者的反因果信号。

Naive application of the plane wave decomposition results in a ghost signal—an anticausal signal that appears at the observer before the source signal exists.

**时间门控条件 | Time Gating Condition:**

$$T_s > \frac{R_s + R_c}{c} \tag{18.20}$$

通过选择子信号持续时间 $T_s$ 大于此值，可利用时间门控消除鬼信号。

By choosing subsignal duration $T_s$ greater than this value, the ghost signal can be time-gated out.

### 18.3.4 实现细节 | Implementation Issues

**1. 空间积分 | Spatial Integration:**

使用适当求积规则执行源域上的积分。

The integration over the source domain should be carried out using appropriate quadrature rules.

**2. 谱积分 | Spectral Integration:**

利用三个基本观察：

Three basic observations permit achieving arbitrary accuracy when numerically evaluating the spectral integration:

a) 排除平移函数的被积函数可解释为封闭在半径为 $R_s$ 的球内的源分布的时间依赖辐射模式。
   The integrand excluding the translation function can be interpreted as the time-dependent radiation pattern of a source distribution enclosed in a sphere of radius $R_s$.

b) 平移函数仅是 $\hat{k}$ 和 $\hat{k}_0$ 之间角度的函数，可用Legendre多项式表示。
   The translation function is only a function of the angle between $\hat{k}$ and $\hat{k}_0$.

c) 由于球面谐函数的正交性，高阶项不对最终结果有贡献。
   Due to the orthogonality of the spherical harmonics, higher-order terms do not contribute to the final result.

**3. 子信号时域表示 | Subsignal Temporal Representation:**

使用带限近似时间受限函数（如近似扁椭球函数APS）进行局部插值。

Local interpolation using bandlimited and approximately time-limited functions (such as approximate prolate spheroidal functions).

$$s_l(\mathbf{r}, t) = \sum_p s(\mathbf{r}, t_p) \phi_p(t) \tag{18.26}$$

---

## 18.4 PWTD增强MOT方案的实现 | Implementation of the PWTD-Enhanced MOT Schemes

### 18.4.1 双层PWTD增强MOT算法 | Two-Level PWTD-Enhanced MOT Algorithm

**基本思想 | Basic Idea:**

将散射体细分为大量子散射体。所有来自附近子散射体的贡献使用经典MOT直接评估。所有其他贡献使用PWTD方案评估。

Divide the scatterer into a large number of subscatterers. All contributions from nearby subscatterers are evaluated directly using the classical MOT. All other contributions are evaluated using the PWTD scheme.

**分组策略 | Grouping Strategy:**

将散射体封闭在虚构立方体中，细分为等尺寸的小盒子。

Enclose the scatterer in a fictitious cubical volume subdivided into many equally sized smaller boxes.

**近场 vs 远场 | Near Field vs Far Field:**

根据其组中心距离是小于还是大于预设距离 $R_{sep} = \eta R_{box}$ 来识别"近场"或"远场"对。

Each group pair is identified as either a "near field" or a "far field" pair depending on whether their group centers are separated by less than or more than a preset distance $R_{sep} = \eta R_{box}$.

### 18.4.2 三步远场评估 | Three-Step Far-Field Evaluation

**(a) 出射射线构建 | Outgoing Ray Construction:**

对于每个组，每隔 $M$ 个时间步构建描述由基本持续时间 $T_s$ 的子信号生成的瞬态远场的出射射线集。

For each group, a set of outgoing rays describing transient far fields that are generated by subsignals of fundamental duration $T_s$ is constructed every $M$ time steps.

**(b) 平移 | Translation:**

对于每个远场对 $(\alpha, \beta)$，出射射线每 $m_{\alpha\beta}$ 个时间步从组 $\alpha$ 平移到组 $\beta$。

For each far field pair $(\alpha, \beta)$, outgoing rays are translated from group $\alpha$ to group $\beta$ every $m_{\alpha\beta}$ time steps.

**(c) 入射射线投影 | Projection of Incoming Rays:**

在每个时间步，通过将入射射线与投影函数卷积并将它们在球面上求和来形成第 $n$ 个观察者处的场。

At each time step, the field at the nth observer is formed by convolving the incoming rays with the projection function and by performing the spherical integration.

### 18.4.3 多层PWTD增强MOT算法 | Multilevel PWTD-Enhanced MOT Algorithm

**层次细分 | Hierarchical Subdivision:**

通过递归细分封闭散射体的虚构立方体来实现散射体的层次细分。

Achieved by recursively subdividing a fictitious cubical box that encloses the scatterer.

**四级操作 | Four-Level Operations:**

1. **射线插值 | Ray Interpolation**: 增加采样率并填充多余的球面谱
   Increases sampling rate and zero-pads excess spherical spectrum

2. **射线拼接 | Ray Splicing**: 将插值的子射线组装成单个父组射线
   Assembles interpolated child rays into a single parent group ray

3. **射线切除 | Ray Resection**: 从父盒子的入射射线构建子的入射射线
   Constructs incoming rays of a child from those of its parent

4. **射线逆插值 | Ray Anterpolation**: 截断球面谐波含量并降低球面采样率
   Truncates spherical harmonic content and lowers sampling rate

### 18.4.4 复杂度比较 | Complexity Comparison

| 方法 | 复杂度 |
|------|--------|
| Method | Complexity |
| Classical MOT | $O(N_t N_s^2)$ |
| Two-Level PWTD-MOT | $O(N_t N_s^{1.5})$ |
| Multilevel PWTD-MOT | $O(N_t N_s \log N_s)$ |
| Two-Level Windowed PWTD-MOT | $O(N_t N_s^{1.33})$ |
| Multilevel Windowed PWTD-MOT | $O(N_t N_s)$ |

---

## 18.5 窗口化平面波时域算法 | The Windowed Plane-Wave Time-Domain Algorithm

### 18.5.1 窗口化平面波分解 | Windowed Plane-Wave Decomposition

**关键观察 | Key Observation:**

如果平移函数的时间跨度可以缩短，则对于足够远的源和观察组，需要平移的射线数量会缩小到与组大小无关的常数。

If the time span of the translation functions can be shortened, the number of rays that need to be translated for the evaluation of the observed field shrinks to a constant independent of the group size.

**窗口化策略 | Windowing Strategy:**

通过平滑地锥削（窗口化）高于 $l > L$ 的项而不是硬截断来构造更短的平移函数。

Construct shorter translation functions by smoothly tapering off, or windowing, the terms for $l > L$ instead of truncating them at $L$.

### 18.5.2 约束条件 | Constraints

从几何考虑，推导了两个约束条件：

From geometric considerations, two constraint equations are derived:

$$\frac{m_s R_s}{c} > R_{s\alpha} + R_{c\beta} \tag{18.43}$$

$$\frac{m_s R_s}{c} > \frac{R_{s\alpha} R_{c\beta}}{R_s} (1 - \cos\theta_{int}) \tag{18.44}$$

这些约束确保真实信号和鬼信号在时间上不重叠。

These constraints ensure that the true and ghost signals do not overlap in time.

### 18.5.3 平移函数性质 | Properties of Translation Function

**平移函数表达式 | Translation Function Expression:**

$$T_l(\hat{k}, \hat{k}_0, t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \frac{e^{j\omega t}}{k_s R_s} \frac{(2l+1) j^l}{k_s R_s} P_l(\hat{k} \cdot \hat{k}_0) dk_s \tag{18.63}$$

---

## 18.6 计算复杂度 | Computational Complexity

### 18.6.1 双层窗口化PWTD-MOT | Two-Level Windowed PWTD-MOT

**总成本 | Total Cost:**

$$C_{total} = O(N_t N_s^{1.33}) \tag{estimated}$$

### 18.6.2 多层窗口化PWTD-MOT | Multilevel Windowed PWTD-MOT

**总成本 | Total Cost:**

$$C_{total} = O(N_t N_s) \tag{estimated}$$

---

## 18.7 本章小结 | Summary

本章介绍了PWTD算法的基础知识，这是一种使用平面波基函数加速瞬态场评估的方法。

This chapter introduced the plane-wave time-domain (PWTD) algorithm, which considerably reduces the cost of evaluating retarded-time boundary integrals by using plane wave bases.

**主要贡献 | Main Contributions:**

1. **三阶段PWTD算法 | Three-Stage PWTD Algorithm**:
   - 出射射线构建（斜堆变换）| Outgoing ray construction (SST)
   - 平移 | Translation
   - 投影 | Projection

2. **时间门控消除鬼信号 | Time Gating to Eliminate Ghost Signals**:
   通过适当选择子信号持续时间确保真实信号和鬼信号在时间上分离。
   By appropriately choosing subsignal duration, true and ghost signals are separated in time.

3. **复杂度降低 | Complexity Reduction**:

| 方法 | 复杂度 |
|------|--------|
| Classical MOT | $O(N_t N_s^2)$ |
| Multilevel PWTD-MOT | $O(N_t N_s \log N_s)$ |
| Multilevel Windowed PWTD-MOT | $O(N_t N_s)$ |

4. **准确性保证 | Accuracy Guarantee**:
   PWTD算法的准确性可通过选择适当的过采样率和带宽来控制到任意精度。
   The accuracy of the PWTD algorithm can be controlled to arbitrary precision by choosing appropriate oversampling ratios and bandwidth.
