# 第 17 章：最速下降快速多极子方法
# Chapter 17: The Steepest-Descent Fast Multipole Method

---

## 17.1 引言 | Introduction

准平面结构（Quasi-planar structures）是指横向尺寸远大于高度的结构。分析这类结构与电磁波的相互作用对于许多实际应用至关重要，包括：

Quasi-planar structures are those whose transverse dimensions are much larger than their height. Efficient and accurate algorithms for analyzing electromagnetic interactions with such structures are important since they permit the characterization of several real-world electromagnetic analysis problems, including:

- 粗糙表面散射 | Rough surface scattering
- 微带贴片天线辐射 | Radiation from microstrip patch antennas
- 光栅结构设计 | Grating structure design
- 衍射光学元件分析 | Analysis of diffractive optical elements

**SDFMM的提出 | Introduction of SDFMM:**

本章开发了一种复杂度为 $O(N)$ 的FMM变体，称为最速下降快速多极子方法（SDFMM）。

In this chapter, an FMM variant with $O(N)$ complexity is developed that permits the rapid full-wave electromagnetic analysis of general quasi-planar structures.

SDFMM加速多区域组合场积分方程（CFIE）的求解。SDFMM依赖于3D Green函数的最速下降积分表示结合2D FMM-like非均匀平面波展开。

SDFMM accelerates the solution of multiregion combined field integral equations (CFIEs). SDFMM relies on a representation of the 3D Green's function in terms of a steepest-descent integral coupled with a 2D FMM-like multilevel inhomogeneous plane-wave expansion.

---

## 17.2 准平面表面的场评估 | Field Evaluation on Quasi-Planar Surfaces

### 17.2.1 标量情况 | The Scalar Case

考虑位于均匀介质中、高度轮廓为 $z = h(x,y)$ 的准平面表面 $\Omega$。

Consider a quasi-planar surface $\Omega$ residing in a homogeneous medium, and characterized by a height profile $h(x,y)$.

目标：计算"测试"场

Objective: Compute the "tested" fields:

$$f_n = \int_\Omega \phi_m(\mathbf{r}') G(\mathbf{r}, \mathbf{r}') d\Omega' \tag{17.1a}$$

其中 $G(\mathbf{r}, \mathbf{r}') = e^{-jk|\mathbf{r}-\mathbf{r}'|}/(4\pi|\mathbf{r}-\mathbf{r}'|)$ 是动态标量Green函数。

where $G(\mathbf{r}, \mathbf{r}')$ is the homogeneous scalar Green's function.

**Sommerfeld恒等式 | Sommerfeld Identity:**

$$G(\mathbf{r}, \mathbf{r}') = \frac{j}{2\pi} \int_{-\infty}^{\infty} \frac{e^{-j k_z z}}{k_z} H_0^{(2)}(k_\rho \rho) dk_\rho \tag{17.2}$$

### 17.2.2 三阶段SDFMM算法 | Three-Stage SDFMM Algorithm

**第一阶段：出射射线构建（ slant stack transform, SST）**

Stage 1: Outgoing Ray Construction (Slant Stack Transform):

$$\psi(\hat{k}, t) = \int_\Omega \frac{e^{-jk|\mathbf{r}-\mathbf{r}'|}}{|\mathbf{r}-\mathbf{r}'|} \delta(t - \hat{k} \cdot \mathbf{r}'/c) s(\mathbf{r}') d\Omega' \tag{17.17}$$

$\psi(\hat{k}, t)$ 可解释为沿方向 $\hat{k}$ 传播的出射射线。

$\psi(\hat{k}, t)$ can be interpreted as outgoing rays (rays that leave the source sphere in the direction $\hat{k}$).

**第二阶段：平移**

Stage 2: Translation:

$$u(\hat{k}, t) = \int_{-\infty}^{\infty} T(\hat{k}, \hat{k}_0, \tau) \psi(\hat{k}_0, t-\tau) d\tau \tag{18.18}$$

平移算子 $T(\hat{k}, \hat{k}_0, \tau)$ 将出射射线从源球转换到观察球。

The operator $T(\hat{k}, \hat{k}_0, \tau)$ translates each outgoing ray from the source sphere to the observer sphere.

**第三阶段：投影**

Stage 3: Projection:

$$f(\mathbf{r}, t) = \int_{4\pi} D(\hat{k}, \mathbf{r}, \tau) u(\hat{k}, t-\tau) d\Omega_k \tag{18.19}$$

**鬼信号问题 | Ghost Signal Problem:**

Naive应用（17.10）会导致真实场和反因果鬼信号同时出现。

Naive application of (18.10) results in both the true observed field and an anticausal ghost field.

通过选择适当长度的子信号，可利用时间门控消除鬼信号。

By choosing subsignal duration appropriately, the ghost signal can be time-gated out.

$$\Delta T_s > \frac{R_s + R_c}{c} \tag{18.20}$$

### 17.2.3 矢量情况 | The Vector Case

在标量情况结果的基础上，SDFMM可用于加速涉及矢量Green函数和源的Green函数计算。

By building on the results obtained for the scalar case, SDFMM can be used to accelerate Green's functions computations involving vector Green's functions and sources.

多层级SDFMM遍历将与标准FMM完全相同的方式进行，区别在于使用两个远场矢量非均匀平面波谱代替标量谱。

The multilevel SDFMM traversal will proceed exactly in the same manner as for the scalar case, with the distinction that two far-field components of the vector inhomogeneous plane-wave spectra are used in place of scalar spectra.

---

## 17.3 计算复杂度估计 | Computational Complexity Estimates

### 17.3.1 复杂度分析 | Complexity Analysis

**关键参数 | Key Parameters:**

- $L$：SDFMM级别数 | Number of SDFMM levels
- $N_b(l)$：级别 $l$ 的块数 | Number of blocks at level $l$
- $N_p(l)$：级别 $l$ 每个块的SDP积分点数 | Number of SDP integration points at level $l$
- $N_\theta(l)$：级别 $l$ 的谱角数 | Number of spectral angles at level $l$

**总成本估计 | Total Cost Estimate:**

$$C_{total} = C_{near} + C_{far} = O(N) + O(N) = O(N) \tag{17.19c}$$

不仅每个矩阵-向量乘积的成本为 $O(N)$，而且总内存需求（存储所有级别的近场交互和入射/出射谱）也是 $O(N)$。

Not only is the cost of each matrix-vector product of $O(N)$, but the total memory requirements (storing near-field interactions and incoming-outgoing spectra at all levels) are also of $O(N)$.

### 17.3.2 复杂度直觉解释 | Intuitive Explanation of Complexity

**SDP积分点数 | Number of SDP Integration Points:**

在给定级别 $l$ 执行SDP积分所需的非均匀平面波分量 $N_p(l)$ 与观察区域相对于源区域所对的角度成正比。

The number of inhomogeneous plane-wave components $N_p(l)$ needed to perform the SDP integration at a given level $l$ is proportional to the angle which the observation region subtends as seen from the source region.

由于粗糙表面，电大尺寸不影响所需的SDP积分点数。

Increasing the size of the rough surface, while keeping surface roughness and finest-level block sizes constant, will not increase the required number of SDP integration points.

---

## 17.4 随机粗糙表面散射 | Scattering from Random Rough Surfaces

### 17.4.1 模型开发 | Model Development

**粗糙表面生成 | Rough Surface Generation:**

使用两步过程生成分布为高斯分布的随机粗糙表面：

Random rough surfaces with a Gaussian distribution are generated using a two-step process:

1. 在离散2D规则网格上组装不相关高斯分布。
   Assemble an uncorrelated Gaussian distribution on a discrete two-dimensional regular grid.

2. 在频域中滤波该分布；使用的滤波器也具有高斯轮廓。
   Filter this distribution in the spectral domain; the filter used also has a Gaussian profile.

**统计特性 | Statistical Properties:**

$$\langle h(\mathbf{r}) \rangle = 0 \tag{17.20a}$$
$$\langle h(\mathbf{r}) h(\mathbf{r}') \rangle = \sigma^2 e^{-|\mathbf{r}-\mathbf{r}'|^2 / l_c^2} \tag{17.20b}$$

其中 $\sigma^2$ 是方差，$l_c$ 是相关长度。

where $\sigma^2$ is the variance and $l_c$ is the correlation length.

### 17.4.2 积分方程公式 | Integral Equation Formulations

**理想导体表面 | Perfectly Conducting Surfaces:**

使用电场积分方程（EFIE）分析表面散射：

An electric field integral equation (EFIE) is utilized to analyze the field scattered by the surface $\Omega$ when excited by $\mathbf{E}^{inc}$:

$$\hat{t} \cdot \mathbf{E}^{inc} = \hat{t} \cdot \mathcal{L}(\mathbf{J}) \tag{17.23a}$$

**介质粗糙表面 | Dielectric Rough Surfaces:**

使用PMCHWT公式（Papoulis-MacCormack-Chen-Harrington-Wait-TTem）

The PMCHWT formulation enforces the continuity of the tangential electric and magnetic field components across $\Omega$.

### 17.4.3 SDFMM求解 | SDFMM-Based Solutions

**迭代求解 | Iterative Solution:**

使用TFQMR（转置自由准最小残差）求解器迭代重建表面电流。

A transpose-free quasi-minimal residual (TFQMR) solver is used to iteratively reconstruct the surface currents.

**验证结果 | Validation Results:**

- 粗糙度 $\sigma = 0.1\lambda$，相关长度 $l_c = 0.5\lambda$
- 表面尺寸 $20\lambda \times 20\lambda$
- 离散密度为每波长10个节点
- SDFMM与经典MOM的结果在 $0.1\%$ 以内一致

Roughness $\sigma = 0.1\lambda$, correlation length $l_c = 0.5\lambda$
Surface size $20\lambda \times 20\lambda$
Discretization density of 10 nodes per wavelength
SDFMM agrees to within $0.1\%$ with classical MOM results

### 17.4.4 Monte Carlo模拟 | Monte Carlo Simulation

对50个完美导体粗糙表面的集合进行Monte Carlo模拟。

A Monte Carlo simulation is carried out for an ensemble of 50 perfectly conducting rough surfaces.

**非相干双站散射系数 | Noncoherent Bistatic Scattering Coefficient:**

- 共极化和交叉极化情况均观察到后向散射增强。
  Backscattering enhancement is clearly observed for both co- and cross-polarized cases.

**CPU时间和内存要求 | CPU Time and Memory Requirements:**

对于 $N = 191,530$ 未知数的巨大问题：
- 经典MOM需要325 GB内存
- SDFMM只需1.8 GB内存
- 每次矩阵-向量乘积：经典MOM约80分钟，SDFMM约14分钟
- 总设置时间：SDFMM约3小时

For the large problem with $N = 191,530$ unknowns:
- Classical MOM would require 325 GB of memory
- SDFMM requires only 1.8 GB of memory
- Matrix-vector product: ~80 minutes for classical MOM, ~14 minutes for SDFMM
- Total setup time: ~3 hours for SDFMM

---

## 17.5 量子阱光栅分析 | Quantum Well Grating Analysis

### 17.5.1 量子阱红外探测器（QWIPs）| Quantum Well Infrared Photodetectors

具有AlGaAs/GaAs量子阱的QWIPs在大型成像阵列中作为传感器显示出巨大潜力。

Quantum well infrared photodetectors (QWIPs) with AlGaAs/GaAs quantum wells have shown great potential as sensors in large imaging arrays.

由于量子力学选择规则，大多数应变n型QWIPs仅响应光学电场的纵向分量（即沿生长方向的分量）。

Owing to quantum-mechanical selection rules, most unstrained n-type QWIPs respond only to the longitudinal component of the optical electrical field.

**光栅耦合器 | Grating Couplers:**

对于这种器件感测正常入射辐射，需要光栅耦合器将光学场散射到有利于子带吸收的方向。

For such devices to sense normally incident radiation, optical grating couplers are needed to scatter the optical field in directions favorable to inter-subband absorption.

### 17.5.2 周期和准随机光栅 | Periodic and Quasi-Random Gratings

**三种光栅类型 | Three Types of Gratings:**

1. **P-光栅**：双重周期光栅（Doubly periodic grating）
2. **D-光栅**：位移光栅（通过在横向方向上移动凸起部分生成）
   Displaced grating (generated by displacing raised portions in lateral directions)
3. **S-光栅**：缩放光栅（通过沿对角线缩放凸起部分生成）
   Scaled grating (generated by scaling raised portions along their diagonal)

**光栅性能比较 | Grating Performance Comparison:**

| 光栅类型 | 最大/最小IFS比 |
|----------|---------------|
| P-grating | 3.83 |
| D-grating | 1.75 |
| S-grating | 1.70 |

- P-光栅在更大波长处吸收迅速减小。
  For the P-grating, the absorption diminishes rapidly at larger wavelengths.

- D-和S-光栅在感兴趣频率范围内表现出更平滑的光谱行为。
  The D- and S-gratings exhibit a much smoother spectral behavior over the frequency range of interest.

### 17.5.3 随机粗糙表面耦合器 | Random Rough Surface Couplers

SDFMM可分析一大类光栅和耦合结构，包括粗糙表面光栅。

SDFMM can be used to analyze a far larger class of grating and coupling structures than have been analyzed or tested in the past.

粗糙表面光栅被提议作为QWIP应用的合适候选者。

Rough surface gratings are proposed here as suitable candidates for QWIP applications.

**结果 | Results:**

- 三种粗糙表面光栅实现（均方根高度分别为0.2λ、0.4λ和0.6λ）
- 所有三种光栅在整个感兴趣波长带（8-12 μm）表现出极其平滑的IFS
- 最大/最小IFS比对于所有三种粗糙表面均小于1.2
- 这与周期光栅的3.83形成鲜明对比

Three rough surface grating realizations (RMS heights of 0.2λ, 0.4λ, and 0.6λ respectively)
All three gratings exhibit an extremely smooth IFS over the entire wavelength band of interest (8-12 μm in free space)
The ratio of maximum to minimum IFS is less than 1.2 for all three rough surfaces
This is in sharp contrast to the periodic grating's ratio of 3.83

---

## 17.6 有限基板微带天线阵列分析 | Analysis of Microstrip Antenna Arrays on Finite Substrates

### 17.6.1 引言 | Introduction

准确分析来自现实微带结构的辐射和散射工具对于许多现代天线系统的设计至关重要。

Accurate tools for analyzing radiation and scattering from realistic microstrip structures are essential in the design of many modern antenna systems.

MOM对有限基板和地平面截断效应的评估仍然是一项计算挑战性任务，因为这些结构的精确全波建模需要大量MOM基函数。

The MOM-based assessment of finite-substrate and ground-plane-truncation effects remains a computationally challenging task.

### 17.6.2 积分方程公式和SDFMM求解 | Integral Equation Formulation and SDFMM Solution

**多区域方法 | Multi-Region Approach:**

假设研究结构与任意数量的区域相关联，每个区域的介电常数和磁导率表示为 $\varepsilon_i$ 和 $\mu_i$。

The structure under study is associated with an arbitrary number of regions.

**PMCHW方程 | PMCHW Equations:**

通过在所有区域间的界面上施加适当的边界条件来获得。

The PMCHW equations are obtained by enforcing appropriate boundary conditions on the electric and magnetic fields at the interfaces between all regions.

### 17.6.3 MOM公式 | MOM Formulation

**基函数 | Basis Functions:**

- 表面电流：RWG函数 | Surface currents: RWG functions
- 探针电流：分段线性基函数 | Probe currents: Piecewise linear basis functions

### 17.6.4 数值结果 | Numerical Results

**辐射模式验证 | Radiation Pattern Validation:**

- 贴片尺寸：$0.259\lambda \times 0.258\lambda$
- 基板厚度：$0.02\lambda$
- 相对介电常数：$\varepsilon_r = 2.33$

**大规模阵列 | Large-Scale Array:**

$8 \times 8$ 阵列使用 $N = 63,504$ 个基函数

---

## 17.7 本章小结 | Summary

本章介绍了SDFMM的综述，这是一种类似FMM的方案，用于快速评估与准平面结构散射和辐射相关的矩阵-向量乘积。

This chapter presented a review of SDFMM, an FMM-like scheme for rapidly evaluating matrix-vector products that arise in the analysis of scattering and radiation from quasi-planar structures.

**主要贡献 | Main Contributions:**

1. **复杂度 | Complexity**: SDFMM的CPU时间和内存需求与 $O(N)$ 成比例。
   CPU time and memory requirements of SDFMM scale as $O(N)$.

2. **应用 | Applications**: 
   - 粗糙表面散射 | Scattering from rough surfaces
   - 量子阱光栅 | Quantum-well gratings
   - 微带天线阵列辐射 | Radiation from microstrip antenna arrays

3. **性能提升 | Performance Improvement**:
   - 对于 $N = 191,530$ 未知数，SDFMM相比经典MOM节省超过180倍内存
   - 每次矩阵-向量乘积加速约5.7倍
   - For $N = 191,530$ unknowns, SDFMM saves over 180× memory compared to classical MOM
   - Matrix-vector product speedup of approximately 5.7×
