---
title: "Ch1: Mathematical Formulations for Electromagnetic Fields"
book: "Sheng & Song, Essentials of Computational Electromagnetics (2012)"
chapter: 1
pages: "1-28"
weight: 1
topics:
  - Maxwell's equations
  - Constitutive relations
  - Boundary conditions
  - Vector wave equation
  - Vector integral equation
  - Green's function
  - Layered medium
notes_version: "1.1"
---

# Chapter 1: Mathematical Formulations for Electromagnetic Fields | 电磁场数学公式

> **中英双语版**

## 1.1 Deterministic Vector Partial Differential System of the Electromagnetic Fields

电磁场的确定型矢量偏微分方程组

A complete system of vector partial differential equations for EM fields comprises three parts:
一个完整的电磁场矢量偏微分方程组由三部分构成：

1. **Maxwell's equations** — the fundamental field equations
   **麦克斯韦方程组**——基本场方程
2. **Constitutive relations** — material responses (D, B to E, H)
   **本构关系**——材料响应（D、B 与 E、H 的关系）
3. **Boundary conditions** — field behavior at interfaces
   **边界条件**——界面上场的行为

### 1.1.1 Maxwell's Equations

麦克斯韦方程组

In differential form (time domain):
微分形式（时域）：

$$
\nabla \times \mathbf{E} + \frac{\partial \mathbf{B}}{\partial t} = \mathbf{0} \quad \text{(Faraday's law)} \tag{1.1}
$$

$$
\nabla \times \mathbf{H} - \frac{\partial \mathbf{D}}{\partial t} = \mathbf{J} \quad \text{(Ampere's law with displacement current)} \tag{1.2}
$$

$$
\nabla \cdot \mathbf{D} = \rho \quad \text{(Gauss' law for electric fields)} \tag{1.3}
$$

$$
\nabla \cdot \mathbf{B} = 0 \quad \text{(Gauss' law for magnetic fields)} \tag{1.4}
$$

**Physical field quantities** (LHS):
物理场量（左边）：
- $\mathbf{E}$: electric field intensity $[\mathrm{V/m}]$（电场强度）
- $\mathbf{D}$: electric flux density $[\mathrm{C/m^2}]$（电通量密度）
- $\mathbf{H}$: magnetic field intensity $[\mathrm{A/m}]$（磁场强度）
- $\mathbf{B}$: magnetic flux density $[\mathrm{Wb/m^2}]$（磁通量密度）

**Source quantities** (RHS):
源量（右边）：
- $\mathbf{J}$: volume current density $[\mathrm{A/m^2}]$（体电流密度）
- $\rho$: free volume charge density $[\mathrm{C/m^3}]$（自由体电荷密度）

**Charge conservation** (continuity equation):
电荷守恒（连续性方程）：

$$
\nabla \cdot \mathbf{J} = -\frac{\partial \rho}{\partial t} \tag{1.5}
$$

**Key observation**: Only 3 of the 5 equations are independent. Applying $\nabla \cdot$ to (1.1) yields (1.4); applying $\nabla \cdot$ to (1.2) and using (1.5) yields (1.3).
**关键点**：5 个方程中只有 3 个是独立的。对 (1.1) 取散度得到 (1.4)；对 (1.2) 取散度并利用 (1.5) 得到 (1.3)。

**Practical selection**:
**实际选择**：
- Electrostatics: use (1.1) and (1.3) only（静电学：仅使用 (1.1) 和 (1.3)）
- Magnetostatics: use (1.2) and (1.3) only（静磁学：仅使用 (1.2) 和 (1.3)）
- Time-varying EM waves: use (1.1) and (1.2) only（时变电磁波：仅使用 (1.1) 和 (1.2)）

### 1.1.2 Constitutive Relations

本构关系

For linear, isotropic materials:
对于线性各向同性材料：

$$
\mathbf{D} = \epsilon \mathbf{E} \tag{1.6}
$$

$$
\mathbf{B} = \mu \mathbf{H} \tag{1.7}
$$

$$
\mathbf{J} = \sigma \mathbf{E} \tag{1.8}
$$

Where:
其中：
- $\epsilon$ [F/m]: permittivity（介电常数）
- $\mu$ [H/m]: permeability（磁导率）
- $\sigma$ [S/m]: electrical conductivity（电导率）

**Classification**:
**分类**：
| Property | Homogeneous | Non-homogeneous |
|----------|-------------|------------------|
| Definition | $\epsilon, \mu, \sigma$ constant in space | vary with position |
| 含义 | 空间常数 | 随位置变化 |
| Classification | Dispersive if parameters are frequency-dependent |
| 分类 | 参数频变时为色散介质 |

**Dispersive media examples**: plasma, water, biological tissues, wave-absorbing materials. In dispersive media, $\epsilon(\omega)$, $\mu(\omega)$ vary with frequency.
**色散介质示例**：等离子体、水、生物组织、吸波材料。在色散介质中，$\epsilon(\omega)$、$\mu(\omega)$ 随频率变化。

### 1.1.3 Boundary Conditions

边界条件

At an interface between two media, the electromagnetic fields must satisfy:
在两种介质的界面上，电磁场必须满足：

**Tangential component continuity** (from Faraday's and Ampere's laws):
**切向分量连续性**（由法拉第定律和安培定律导出）：

$$
\hat{n} \times (\mathbf{E}_2 - \mathbf{E}_1) = \mathbf{0} \quad \Rightarrow \quad E_{t2} = E_{t1} \tag{1.9}
$$

$$
\hat{n} \times (\mathbf{H}_2 - \mathbf{H}_1) = \mathbf{J}_s \quad \Rightarrow \quad H_{t2} - H_{t1} = J_s \tag{1.10}
$$

**Normal component discontinuity** (from Gauss' laws):
**法向分量不连续性**（由高斯定律导出）：

$$
\hat{n} \cdot (\mathbf{D}_2 - \mathbf{D}_1) = \rho_s \quad \Rightarrow \quad D_{n2} - D_{n1} = \rho_s \tag{1.11}
$$

$$
\hat{n} \cdot (\mathbf{B}_2 - \mathbf{B}_1) = 0 \quad \Rightarrow \quad B_{n2} = B_{n1} \tag{1.12}
$$

Where $\rho_s$ is surface charge density and $\mathbf{J}_s$ is surface current density.
其中 $\rho_s$ 为面电荷密度，$\mathbf{J}_s$ 为面电流密度。

**Special cases**:
**特殊情况**：

1. **Perfect Electric Conductor (PEC)**: $\mathbf{E} = \mathbf{0}$, $\hat{n} \times \mathbf{H} = \mathbf{J}_s$（理想电导体）
2. **Perfect Magnetic Conductor (PMC)**: $\mathbf{H} = \mathbf{0}$, $\hat{n} \times \mathbf{E} = -\mathbf{M}_s$（理想磁导体）

### 1.1.4 Maxwell's Equations in the Frequency Domain

频域麦克斯韦方程组

Using phasor representation $\mathbf{E}(\mathbf{r}, t) = \mathrm{Re}\{\tilde{\mathbf{E}}(\mathbf{r}) e^{j\omega t}\}$, we obtain:
使用相量表示 $\mathbf{E}(\mathbf{r}, t) = \mathrm{Re}\{\tilde{\mathbf{E}}(\mathbf{r}) e^{j\omega t}\}$，得到：

$$
\nabla \times \tilde{\mathbf{E}} = -j\omega \tilde{\mathbf{B}} \tag{1.107}
$$

$$
\nabla \times \tilde{\mathbf{H}} = \tilde{\mathbf{J}} + j\omega \tilde{\mathbf{D}} \tag{1.108}
$$

$$
\nabla \cdot \tilde{\mathbf{D}} = \tilde{\rho} \tag{1.109}
$$

$$
\nabla \cdot \tilde{\mathbf{B}} = 0 \tag{1.110}
$$

**Physical insight**: The $j\omega$ terms represent the displacement current — Maxwell's key addition to Ampere's law that enables wave propagation.
**物理洞察**：$j\omega$ 项代表位移电流——麦克斯韦对安培定律的关键补充，使波的传播成为可能。

### 1.1.5 Uniqueness Theorem

唯一性定理

**Theorem**: The electromagnetic field in a lossless region is uniquely determined by specifying either:
**定理**：无耗区域中的电磁场由以下任一边界条件唯一确定：
- The tangential electric field $\mathbf{E}_t$ on the boundary (Dirichlet condition), or（边界上的切向电场（Dirichlet 条件））
- The tangential magnetic field $\mathbf{H}_t$ on the boundary (Neumann condition)（边界上的切向磁场（Neumann 条件））

**Implication for computational electromagnetics**: Knowing the boundary condition is sufficient to determine the field uniquely inside the domain. This forms the theoretical foundation for all numerical methods (MoM, FEM, FDTD).
**对计算电磁学的意义**：知道边界条件即可唯一确定域内场分布。这构成了所有数值方法（MoM、FEM、FDTD）的理论基础。

---

## 1.2 Vector Wave Equation

矢量波动方程

From Maxwell's equations and constitutive relations, the electric field satisfies:
由麦克斯韦方程组和本构关系，电场满足：

$$
\nabla \times \nabla \times \mathbf{E} - k^2 \mathbf{E} = -j\omega\mu \mathbf{J} \tag{1.41}
$$

where $k = \omega\sqrt{\mu\epsilon}$ is the wavenumber. This is the **vector Helmholtz equation**.
其中 $k = \omega\sqrt{\mu\epsilon}$ 为波数。这就是**矢量亥姆霍兹方程**。

For a source-free region ($\mathbf{J} = 0$):
对于无源区域（$\mathbf{J} = 0$）：

$$
\nabla \times \nabla \times \mathbf{E} - k^2 \mathbf{E} = \mathbf{0} \tag{1.42}
$$

Using the vector identity $\nabla \times \nabla \times \mathbf{E} = \nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E}$ and Coulomb gauge $\nabla \cdot \mathbf{E} = 0$ (source-free):
利用矢量恒等式 $\nabla \times \nabla \times \mathbf{E} = \nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E}$ 和库仑规范 $\nabla \cdot \mathbf{E} = 0$（无源）：

$$
\nabla^2 \mathbf{E} + k^2 \mathbf{E} = \mathbf{0} \tag{1.43}
$$

---

## 1.3 Vector Integral Equations

矢量积分方程

The integral equation formulation provides an alternative to partial differential equations, naturally satisfying the Sommerfeld radiation condition at infinity.
积分方程公式是偏微分方程的替代方案，天然满足无穷远处的索末菲辐射条件。

### 1.3.1 Equivalence Principle

等效原理

**First form of equivalence** (exterior equivalent problem):
**第一种等效形式**（外部等效问题）：
- Replace the original scatterer with PEC of the same shape（用相同形状的 PEC 替代原散射体）
- Keep the same external field（保持相同的外部场）
- Introduce equivalent surface current $\mathbf{J}_s = \hat{n} \times \mathbf{H}$ and magnetic current $\mathbf{M}_s = -\hat{n} \times \mathbf{E}$（引入等效面电流 $\mathbf{J}_s = \hat{n} \times \mathbf{H}$ 和磁流 $\mathbf{M}_s = -\hat{n} \times \mathbf{E}$）

**Huygens' principle**: Fields in a source-free region can be expressed as integrals of tangential field components on a closed surface.
**惠更斯原理**：无源区域中的场可以表示为封闭面上切向场分量的积分。

**Second form of equivalence** (interior equivalent problem):
**第二种等效形式**（内部等效问题）：
- Replace interior region with the same medium as exterior（用与外部相同的介质替换内部区域）
- Use equivalent currents $\mathbf{J} = -\hat{n} \times \mathbf{H}$, $\mathbf{M} = \hat{n} \times \mathbf{E}$（使用等效电流 $\mathbf{J} = -\hat{n} \times \mathbf{H}$，等效磁流 $\mathbf{M} = \hat{n} \times \mathbf{E}$）
- Field inside equals original field; field outside is zero（内部场等于原始场；外部场为零）

### 1.3.2 Solution of Maxwell's Equation in Free Space

自由空间中的麦克斯韦方程解

**Scalar Green's function** in free space (3D Helmholtz):
**自由空间标量格林函数**（三维亥姆霍兹）：

$$
G(\mathbf{r}, \mathbf{r}') = \frac{e^{-jk|\mathbf{r}-\mathbf{r}'|}}{4\pi|\mathbf{r}-\mathbf{r}'|} \tag{1.52}
$$

**Dyadic Green's function** for electric field:
**电场并矢格林函数**：

$$
\overline{\overline{G}}_e(\mathbf{r}, \mathbf{r}') = \left(\overline{\overline{I}} + \frac{\nabla \nabla}{k^2}\right) G \tag{1.59}
$$

The electric field due to current distribution $\mathbf{J}$ in free space:
自由空间中电流分布 $\mathbf{J}$ 产生的电场：

$$
\mathbf{E} = -j\omega\mu \int_V \overline{\overline{G}}_e \cdot \mathbf{J} \, dV' \tag{1.61}
$$

**Physical meaning**: The Green's function describes the field from a point source. The integral equation formulation sums contributions from all equivalent sources on the surface.
**物理含义**：格林函数描述点源产生的场。积分方程公式将所有等效源在表面上的贡献求和。

### 1.3.3 Integral Equations of Metallic Scattering Problems

金属散射问题的积分方程

For a PEC scatterer under plane wave incidence $\mathbf{E}^i$, the **Electric Field Integral Equation (EFIE)**:
对于平面波入射 $\mathbf{E}^i$ 下的 PEC 散射体，**电场积分方程（EFIE）**：

$$
\mathbf{E}^i + \mathcal{L}(\mathbf{J}) = 0 \quad \text{on } S \tag{1.77}
$$

Where the operator $\mathcal{L}$ is:
其中算子 $\mathcal{L}$ 为：

$$
\mathcal{L}(\mathbf{J}) = j\omega\mu \int_S \left[ \mathbf{J} G + \frac{1}{k^2} \nabla \cdot \mathbf{J} \nabla G \right] dS' \tag{1.78}
$$

The **Magnetic Field Integral Equation (MFIE)**:
**磁场积分方程（MFIE）**：

$$
\mathbf{J} - \hat{n} \times \mathcal{K}(\mathbf{J}) = \hat{n} \times \mathbf{H}^i \quad \text{on } S \tag{1.79}
$$

Where $\mathcal{K}$ is:
其中 $\mathcal{K}$ 为：

$$
\mathcal{K}(\mathbf{J}) = \int_S \mathbf{J} \times \nabla' G \, dS' \tag{1.80}
$$

**Numerical behavior**:
**数值特性**：
- EFIE: Fredholm integral equation of the **first kind** — ill-conditioned but accurate（**第一类** Fredholm 积分方程——病态但精确）
- MFIE: Fredholm integral equation of the **second kind** — better conditioned, faster convergence in iterative solvers（**第二类** Fredholm 积分方程——条件数更好，迭代求解收敛更快）

### 1.3.4 Integral Equation of Homogeneous Dielectric Scattering Problems

均匀介质散射问题的积分方程

For a homogeneous dielectric body with permittivity $\epsilon_1$ inside, $\epsilon_2$ outside, the PMCHW formulation (Peterson, Chew, Harrington, Wu, Chen) is widely used:
对于内部介电常数为 $\epsilon_1$、外部为 $\epsilon_2$ 的均匀介质体，广泛使用 PMCHW 公式（Peterson, Chew, Harrington, Wu, Chen）：

$$
\mathcal{L}_1(\mathbf{J}) + \mathcal{L}_2(-\mathbf{J}) + \mathcal{K}_1(\mathbf{M}) + \mathcal{K}_2(-\mathbf{M}) = -\mathbf{E}^i \tag{1.186}
$$

$$
\mathcal{K}_1(\mathbf{J}) + \mathcal{K}_2(-\mathbf{J}) - \frac{1}{Z_1}\mathcal{L}_1(\mathbf{M}) - \frac{1}{Z_2}\mathcal{L}_2(-\mathbf{M}) = -\mathbf{H}^i \tag{1.187}
$$

Where $Z_1 = \sqrt{\mu/\epsilon_1}$, $Z_2 = \sqrt{\mu/\epsilon_2}$ are wave impedances.
其中 $Z_1 = \sqrt{\mu/\epsilon_1}$, $Z_2 = \sqrt{\mu/\epsilon_2}$ 为波阻抗。

**Key insight**: The PMCHW system combines both interior and exterior operators in each equation, eliminating the interior resonance problem that affects single-equation formulations.
**关键洞察**：PMCHW 系统在每个方程中同时组合了内外部算子，消除了单方程公式中的内部谐振问题。

### 1.3.5 Integral Equation of Inhomogeneous Dielectric Scattering Problems

非均匀介质散射问题的积分方程

For inhomogeneous media, the **Volume Integral Equation (VIE)** is required:
对于非均匀介质，需要使用**体积分方程（VIE）**：

$$
\mathbf{E}^i(\mathbf{r}) = \mathbf{E}(\mathbf{r}) - k_0^2 \int_V \overline{\overline{G}}(\mathbf{r}, \mathbf{r}') \cdot \chi(\mathbf{r}') \mathbf{E}(\mathbf{r}') \, dV' \tag{1.200}
$$

Where $\chi(\mathbf{r}) = \epsilon_r(\mathbf{r}) - 1$ is the contrast ratio.
其中 $\chi(\mathbf{r}) = \epsilon_r(\mathbf{r}) - 1$ 为对比度。

### 1.3.6 Integral Equations of Scattering in Layered Medium

层状介质散射问题的积分方程

For a PEC scatterer embedded in a layered medium, the Green's function becomes more complex.
对于嵌入层状介质中的 PEC 散射体，格林函数变得更加复杂。

**Sommerfeld integration** (1D integral form):
**索末菲积分**（一维积分形式）：

$$
f(\mathbf{r}) = \frac{1}{2\pi} \int_0^\infty \tilde{f}(k_\rho) J_0(k_\rho \rho) k_\rho \, dk_\rho \tag{1.115}
$$

The **mixed-potential expression** for the electric field:
电场的**混合位表达式**：

$$
\mathbf{E} = -j\omega\mu \int_V \overline{\overline{G}}_A \cdot \mathbf{J} \, dV + \frac{1}{j\omega\epsilon} \nabla \int_V K \nabla' \cdot \mathbf{J} \, dV' + \int_V C \mathbf{J}_z \, dV' \tag{1.162}
$$

**Physical meaning**: The layered medium Green's function accounts for multiple reflections between interfaces. The Sommerfeld integration represents a spectral decomposition into cylindrical waves.
**物理含义**：层状介质格林函数考虑了界面间的多次反射。索末菲积分表示对柱面波的谱分解。

**Numerical challenge**: Direct evaluation of Sommerfeld integrals is computationally expensive. Special techniques (e.g., fast far-field approximation, discrete complex image method) are required for efficient evaluation.
**数值挑战**：直接计算索末菲积分计算量巨大。需要使用特殊技术（如快速远场近似、离散复镜像法）进行高效求值。

---

## Key Equations Summary

关键方程总结

| Equation | Type | Physical Meaning | 物理含义 |
|----------|-------|------------------|----------|
| (1.1)-(1.4) | PDE system | Maxwell's equations in time domain | 时域麦克斯韦方程组 |
| (1.6)-(1.8) | Constitutive | Material response (D, B to E, H) | 本构关系 |
| (1.9)-(1.12) | BC | Field discontinuity at interfaces | 界面场不连续性 |
| (1.77) | Integral | EFIE for PEC scatterer | PEC 散射体 EFIE |
| (1.79) | Integral | MFIE for PEC scatterer | PEC 散射体 MFIE |
| (1.115) | Integral | Sommerfeld integration (layered medium) | 索末菲积分（层状介质） |

---

## Problems

1.6 Prove the relation $\nabla_t = -j\mathbf{k}_\rho$ used in deriving (1.116)–(1.119).

1.7 Prove the reciprocity relations (1.134) for the transmission-line equations.

---

## References

1. Senior, T.B.A. (1960) "Impedance boundary conditions for imperfectly conducting surface." Applied Scientific Research, Section B, 8, 418–436.
2. Peterson, A.F., Ray, S.L., and Mittra, R. (1998) Computational Methods for Electromagnetics, IEEE Press, New York.
3. Ise, K., Inoue, K., and Koshiba, M. (1990) "Three-dimensional finite-element solution of dielectric scattering obstacles in a rectangular waveguide." IEEE Transactions on Antennas and Propagation, 38(9), 1352–1359.
4. Stratton, J.A. (1941) Electromagnetic Theory, McGraw-Hill, New York.
5. Harrington, R.F. (1961) Time-Harmonic Electromagnetic Fields, McGraw-Hill, New York.
6. Tai, C.T. (1971) Dyadic Green's Functions in Electromagnetic Theory, International Textbook Company.
7. Michalski, K.A. and Mosig, J.R. (1997) "Multilayered media Green's functions in integral equation formulations." IEEE Transactions on Antennas and Propagation, 45(3), 508–519.
8. Aksun, M.I. (1996) "A Robust Approach for the Derivation of Closed-form Green's Functions." IEEE Transactions on Microwave Theory and Techniques, 44(5), 651–658.