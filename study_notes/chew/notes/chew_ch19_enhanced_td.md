# 第 19 章：平面波时域算法增强型时域积分方程求解器
# Chapter 19: Plane-Wave Time-Domain Algorithm Enhanced Time-Domain Integral Equation Solvers

---

## 19.1 引言 | Introduction

瞬态电磁现象数值分析在从宽带散射分析到现代天线设计再到非线性现象研究等广泛工程应用中发挥重要作用。

Numerical methods for analyzing electromagnetic transients find widespread engineering applications ranging from the analysis of broadband scattering to the design of modern antennas to the study of nonlinear phenomena and more.

### 19.1.1 时域积分方程（TDIE）vs 微分方程（DE）方法 | TDIE vs DE Methods

**积分方程方法的优势 | Advantages of IE Methods:**

1. **维度降低**: IE求解器仅需离散散射体表面而非包围它的体积，相比DE方法大幅减少未知数数量。
   IE solvers only require a discretization of the scatterer surface rather than a volume enclosing the latter, resulting in a sharp decrease in the number of unknowns when compared to DE methods.

2. **自动满足辐射条件**: IE技术自动施加辐射条件，无需DE方法所需的（近似局部）吸收边界条件来截断有限网格。
   IE techniques automatically impose the radiation condition, hence there is no need for (approximate local) absorbing boundary conditions that are required in the truncation of finite grids used by DE methods.

**时域积分方程的挑战 | Challenges of TDIE:**

1. **晚期不稳定 | Late-time instability**: 许多MOT方案已被证明易于晚期不稳定。
   Many MOT schemes have been shown prone to late time instabilities.

2. **计算复杂度 | Computational complexity**: 经典MOT方案的成本与问题规模的平方成正比。
   The cost associated with classical MOT schemes scales unfavorably with problem size.

### 19.1.2 本章目标 | Chapter Objectives

1. **开发CFIE**: 证明使用此方程分析来自封闭体的瞬态散射可获得准确解。
   To develop a CFIE and demonstrate that using this equation to analyze transient scattering from closed bodies yields an accurate solution.

2. **阐述PWTD方案**: 将PWTD方案应用于矢量波动方程的求解，并将其纳入现有MOT方案。
   To elucidate the PWTD-scheme as it applies to the solution of the vector wave equations, cast it into a framework wherein it can be incorporated into existing MOT schemes.

---

## 19.2 公式 | Formulation

### 19.2.1 积分方程 | Integral Equations

考虑位于自由空间中、表面为 $S$ 的封闭PEC物体。

Consider a closed PEC body with surface $S$ residing in free space.

**电场积分方程（EFIE）| Electric Field Integral Equation:**

$$\hat{n} \times \mathcal{L}(\mathbf{J}) = -\hat{n} \times \mathbf{E}^i \tag{19.4a}$$

其中算子 $\mathcal{L}$ 定义为：

where the operator $\mathcal{L}$ is defined as:

$$\mathcal{L}(\mathbf{J}) = j\omega\mu_0 \int_S \frac{e^{-jk|\mathbf{r}-\mathbf{r}'|}}{4\pi|\mathbf{r}-\mathbf{r}'|} \mathbf{J}(\mathbf{r}') dS' + \frac{1}{j\omega\varepsilon_0} \nabla \int_S \frac{e^{-jk|\mathbf{r}-\mathbf{r}'|}}{4\pi|\mathbf{r}-\mathbf{r}'|} \nabla' \cdot \mathbf{J}(\mathbf{r}') dS' \tag{19.4b}$$

**磁场积分方程（MFIE）| Magnetic Field Integral Equation:**

$$\hat{n} \times \left( \frac{\mathbf{J}}{2} - \mathcal{K}(\mathbf{J}) \right) = -\hat{n} \times \mathbf{H}^i \tag{19.7a}$$

其中 $\mathcal{K}$ 是磁场算子。

where $\mathcal{K}$ is the magnetic field operator.

**组合场积分方程（CFIE）| Combined Field Integral Equation:**

$$\hat{n} \times \left( \alpha \mathcal{L}(\mathbf{J}) + \beta \eta_0 \mathcal{K}(\mathbf{J}) \right) = -\hat{n} \times \left( \alpha \mathbf{E}^i + \beta \eta_0 \mathbf{H}^i \right) \tag{19.9a}$$

### 19.2.2 共振问题 | Resonance Problem

**EFIE和MFIE的共振 | Resonance in EFIE and MFIE:**

齐次时间域EFIE和MFIE的解由 $\mathcal{L}$ 和 $\mathcal{K}$ 预解式的极点表征。

Solutions to the homogeneous time domain EFIE and MFIE are characterized by the poles of the resolvent of $\mathcal{L}$ and $\mathcal{K}$.

- 位于虚轴上的极点对应于EFIE和MFIE支持的内部空腔模式的频率。
  Poles on the imaginary axis correspond to the frequencies of the interior cavity modes that the EFIE and MFIE support.

- 虽然理论上入射场不与内部模式耦合，但数值方案会导致入射场与这些扰动内部模式耦合。
  In theory the incident field does not couple to the interior modes. Unfortunately, because of numerical approximations, the incident field does couple to the perturbed interior modes.

**CFIE消除共振 | CFIE Eliminates Resonance:**

CFIE的解在所有测试结构中均无空腔模式。

Our numerical results indicate that, for all structures tested, the solution to the CFIE is free of cavity modes.

### 19.2.3 时间步进（MOT）公式 | Marching-On-in-Time (MOT) Formulation

**基函数选择 | Basis Function Choice:**

Rao-Wilton-Glisson（RWG）函数用于模拟电流的空间变化。

Rao-Wilton-Glisson functions are chosen to model the spatial variation of the current.

**时间基函数 | Temporal Basis Functions:**

使用线性插值（三角）函数表示电流的时间变化。

Linearly interpolating (triangular) functions are used to represent the temporal variation of the current.

**MOT矩阵方程 | MOT Matrix Equation:**

$$[Z] \{I\}^{n+1} = \{V\}^n - \sum_{l=1}^{n} [Z] \{I\}^l \tag{19.13a}$$

### 19.2.4 稳定性考虑 | Stability Considerations

**隐式时间步进 | Implicit Time Stepping:**

- 使用七点高斯求积规则评估所有内积。
  Seven-point Gaussian quadrature rules are used for computing all inner products.
  
- 时间步长选择为 $\Delta t = \frac{1}{50c}$（与空间离散无关）。
  Time step size chosen as $\Delta t = \frac{1}{50c}$ (independent of spatial discretization).

- 得到的方案是隐式的，因为 $[Z]$ 不是对角的。
  The resulting scheme is termed implicit because $[Z]$ is not diagonal.

**求解策略 | Solution Strategy:**

由于该矩阵非常稀疏，可使用QMR（准最小残差）等非定常迭代求解器有效求解。

Since this matrix is highly sparse, a nonstationary iterative solver such as QMR can be used to efficiently solve for $[Z]$.

---

## 19.3 平面波时域算法 | Plane-Wave Time-Domain Algorithm

### 19.3.1 平面波表示 | Plane Wave Representations

**分组策略 | Grouping Strategy:**

假设散射体可被封闭在虚构立方体中，进一步细分为等尺寸的小立方体或盒子。

Assume that the scatterer can be enclosed in a fictitious cubical box, which is further subdivided in many smaller equal-sized cubes or boxes.

**远场vs近场 | Far Field vs Near Field:**

- **近场对**: 盒子中心距离小于 $\alpha R_{box}$（$\alpha \approx 3-6$）
  Near field pairs: box center distance less than $\alpha R_{box}$

- **远场对**: 使用PWTD算法以组方式计算
  Far field pairs: computed in a group-wise manner using PWTD algorithm

### 19.3.2 三阶段PWTD算法（矢量情况）| Three-Stage PWTD Algorithm (Vector Case)

**第一阶段：出射射线构建（聚合）| Stage 1: Outgoing Ray Construction (Aggregation)**

$$[\mathbf{\alpha}]_m(\hat{k}, t) = \int_S \mathbf{f}_m(\mathbf{r}') \frac{\delta(t - \hat{k} \cdot \mathbf{r}'/c)}{|\mathbf{r}-\mathbf{r}'|} dS' \tag{19.20a}$$

将源分布映射到一组沿方向 $\hat{k}$ 传播的平面波（"出射射线"）。

Maps the source distribution onto a set of plane waves propagating along direction $\hat{k}$ ("outgoing rays").

**第二阶段：平移 | Stage 2: Translation**

$$[\mathbf{\beta}]_n(\hat{k}, t) = \int_{-\infty}^{\infty} \mathbf{T}(\hat{k}, \hat{k}_0, \tau) [\mathbf{\alpha}]_m(\hat{k}_0, t-\tau) d\tau \tag{19.22a}$$

平移算子 $\mathbf{T}(\hat{k}, \hat{k}_0, \tau)$ 将出射射线转换为"入射射线"。

The translation operator $\mathbf{T}(\hat{k}, \hat{k}_0, \tau)$ converts outgoing rays to "incoming rays".

**第三阶段：投影（解聚）| Stage 3: Projection (Disaggregation)**

$$f_{mn} = \int_{4\pi} \int_{-\infty}^{\infty} \mathbf{D}(\hat{k}, \mathbf{r}, \tau) \cdot [\mathbf{\beta}]_n(\hat{k}, t-\tau) d\tau d\Omega_k \tag{19.27a}$$

将入射射线投影到观察者。

Projects incoming rays onto observers.

### 19.3.3 平移函数 | Translation Function

**平移函数表达式 | Translation Function Expression:**

$$T_{ll'}(\hat{k}, \hat{k}_0, t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \frac{e^{j\omega t}}{k^2 R_s} \sum_{n=|l-l'|}^{l+l'} (2n+1) j^n \frac{n(n+1)}{kR_s} P_n^{l,l'}(\hat{k} \cdot \hat{k}_0) dk \tag{19.26}$$

### 19.3.4 双层PWTD增强MOT求解器实现 | Implementation of Two-Level PWTD-Enhanced MOT Solver

**近场评估 | Near Field Evaluation:**

在每个时间步，计算所有近场相互作用对的贡献：

At each time step, compute contributions for all near field interaction pairs:

$$[Z]_{mn} = \sum_{\text{near } (\alpha, \beta)} [\mathbf{f}_m]_\alpha [\mathbf{Z}]_{\alpha\beta} [\mathbf{f}_n]^T_\beta \tag{19.33}$$

**远场评估 | Far Field Evaluation:**

**(a) 出射射线构建 | Outgoing Ray Construction:**

为所有盒子构建出射射线：计算所有射线方向的基本持续时间 $T_s$ 的子信号的射线。

Construct outgoing rays for all boxes: compute rays for subsignals of fundamental duration $T_s$ for all ray directions.

**(b) 平移 | Translation:**

每 $m_{\alpha\beta}$ 个时间步将出射射线从源组 $\alpha$ 平移到观察组 $\beta$。

Translate outgoing rays from source group $\alpha$ to observer group $\beta$ every $m_{\alpha\beta}$ time steps.

**(c) 入射射线投影 | Projection of Incoming Rays:**

将进入所有球的射线投影到观察者。

Project rays entering all spheres onto observers.

### 19.3.5 复杂度分析 | Complexity Analysis

**总成本估计 | Total Cost Estimate:**

$$C_{total} = C_{near} + C_{far} = O(N_t N_s^{1.5}) \tag{19.36}$$

通过优化每个组的未知数（$N_{unknowns per group} \propto \sqrt{N_s}$），总成本最小化为 $O(N_t N_s^{1.5})$。

By optimizing the number of unknowns per group (proportional to $\sqrt{N_s}$), total cost is minimized to $O(N_t N_s^{1.5})$.

---

## 19.4 数值结果 | Numerical Results

### 19.4.1 CFIE有效性验证 | Validation of CFIE

**立方体散射 | Cube Scattering:**

- 尺寸：$1\text{m} \times 1\text{m} \times 1\text{m}$
- 入射波：$\hat{k} = -\hat{z}$，$\hat{E} = \hat{x}$
- 中心频率：$f_0 = 300\text{ MHz}$，带宽：$BW = 100\text{ MHz}$

| 方程类型 | 观察结果 |
|----------|----------|
| MFIE | 特征性 ringing |
| EFIE | 晚期稳定但有残余共振 |
| CFIE | 平滑衰减，无共振 |

| Equation Type | Observation |
|---------------|-------------|
| MFIE | Characteristic ringing |
| EFIE | Late-time stabilized but with residual resonance |
| CFIE | Smooth decay, no resonance |

**球体散射（RCS比较）| Sphere Scattering (RCS Comparison):**

| 频率 | CFIE vs FISC | MFIE vs FISC | EFIE vs FISC |
|------|--------------|--------------|--------------|
| 120 MHz | 良好一致 | 显著偏差 | 显著偏差 |
| 240 MHz | 良好一致 | 显著偏差 | N/A |

- TM(1,1)、TE(1,1) 和 TM(3,1) 模式被激发
  TM(1,1), TE(1,1), and TM(3,1) modes are excited

### 19.4.2 PWTD增强MOT求解器验证 | Validation of PWTD-Enhanced MOT Solver

**矩形板散射 | Rectangular Plate Scattering:**

- 尺寸：$2\text{m} \times 15\text{m}$
- 未知数：2,170
- 极化：$\hat{E} = \hat{x}$，$\hat{k} = -\hat{z}$

**验证结果 | Validation Results:**

PWTD增强MOT求解器与经典方案的结果非常一致。

PWTD-enhanced MOT solver yields results that agree very well with those obtained using the classical scheme.

**准确性证明 | Accuracy Demonstration:**

- 电流比较：在板上一点，PWTD和直接MOT计算结果一致
  Current comparison: at a point on the plate, PWTD and direct MOT calculations agree

- 远场签名比较：后向散射远场时间签名一致
  Far field signature comparison: backscattered far field time signatures agree

---

## 19.5 本章小结 | Summary

### 19.5.1 主要贡献 | Main Contributions

1. **时域CFIE开发 | Development of Time-Domain CFIE**
   
   - CFIE消除了封闭体瞬态散射分析中的空腔共振模式
     CFIE eliminates cavity resonance modes in transient scattering analysis from closed bodies
   
   - 与EFIE/MFIE相比，CFIE解与解析解和FISC一致
     CFIE solution agrees with analytical solutions and FISC, unlike EFIE/MFIE

2. **PWTD算法扩展 | Extension of PWTD Algorithm**
   
   - 从标量情况扩展到矢量Maxwell方程情况
     Extension from scalar to vector Maxwell's equations case
   
   - 使用横向分量矢量势表示场
     Field representation using transverse components of vector potential

3. **计算复杂度降低 | Computational Complexity Reduction**
   
   - 从 $O(N_t N_s^2)$ 降低到 $O(N_t N_s^{1.5})$
     Reduction from $O(N_t N_s^2)$ to $O(N_t N_s^{1.5})$

4. **稳定性保证 | Stability Guarantee**
   
   - 隐式时间步进确保实际稳定
     Implicit time stepping ensures practical stability
   
   - 七点高斯求积规则确保空间积分精度
     Seven-point Gaussian quadrature rules ensure spatial integration accuracy

### 19.5.2 数值验证总结 | Numerical Validation Summary

| 测试案例 | 结构 | 未知数 | 验证方法 |
|----------|------|--------|----------|
| Test Case | Structure | Unknowns | Validation |
| 立方体 | Cube | 450 | 与EFIE/MFIE比较 |
| 球体 | Sphere | 2,793 | Mie级数, FISC |
| 锥-球 | Cone-sphere | 1,656 | FISC |
| 杏仁形 | Almond | 1,104 | FISC |
| 矩形板 | Plate | 2,170 | 直接MOT |

### 19.5.3 实际应用 | Practical Applications

- **宽带散射分析**: 利用时间域方法天然产生宽带数据的能力
  Broadband scattering analysis: leveraging the natural ability of time-domain methods to produce broadband data

- **大型散射体**: PWTD使电大尺寸问题的瞬态分析在计算上可行
  Large scatterers: PWTD makes transient analysis of electrically large problems computationally feasible

- **共振分析**: CFIE避免空腔共振问题，提供准确解
  Resonance analysis: CFIE avoids cavity resonance problems, providing accurate solutions
