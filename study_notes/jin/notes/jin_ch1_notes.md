---
title: "Chapter 1 — Basic Electromagnetic Theory"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Vector analysis (div, curl, gradient, symbolic vector method)
  - Helmholtz decomposition & Green's theorems
  - Maxwell's equations (integral & differential)
  - Constitutive relations & classification of media
  - Boundary conditions at interfaces & PEC/PMC
  - Poynting's theorem & energy conservation
  - Time-harmonic fields & complex power
---

# Chapter 1: Basic Electromagnetic Theory | 第一章：基本电磁理论

> **中英双语版**

## 1.1 Review of Vector Analysis | 矢量分析回顾

### 1.1.1 Vector Operations and Integral Theorems | 矢量运算与积分定理

**Divergence / 散度** — the net outward flux per unit volume / 单位体积的净向外通量：

$$
\nabla \cdot \mathbf{f} = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \oint_s \mathbf{f} \cdot d\mathbf{s}
\tag{1.1.1}
$$

In rectangular coordinates / 直角坐标系中：

$$
\nabla \cdot \mathbf{f} = \frac{\partial f_x}{\partial x} + \frac{\partial f_y}{\partial y} + \frac{\partial f_z}{\partial z}
\tag{1.1.2}
$$

In cylindrical coordinates / 柱坐标系中：

$$
\nabla \cdot \mathbf{f} = \frac{1}{\rho} \frac{\partial (\rho f_\rho)}{\partial \rho} + \frac{1}{\rho} \frac{\partial f_\phi}{\partial \phi} + \frac{\partial f_z}{\partial z}
\tag{1.1.3}
$$

In spherical coordinates / 球坐标系中：

$$
\nabla \cdot \mathbf{f} = \frac{1}{r^2} \frac{\partial}{\partial r} (r^2 f_r) + \frac{1}{r\sin\theta} \frac{\partial}{\partial \theta} (f_\theta \sin\theta) + \frac{1}{r\sin\theta} \frac{\partial f_\phi}{\partial \phi}
\tag{1.1.4}
$$

**Divergence Theorem (Gauss' Theorem) / 散度定理（高斯定理）:**

$$
\iiint_V \nabla \cdot \mathbf{f} \, dV = \oiint_S \mathbf{f} \cdot d\mathbf{S}
\tag{1.1.5}
$$

**Curl / 旋度** — the circulation per unit area / 单位面积上的环量：

$$
\nabla \times \mathbf{f} = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \oint_s d\mathbf{s} \times \mathbf{f}
\tag{1.1.6}
$$

Rectangular form / 直角坐标形式：

$$
\nabla \times \mathbf{f} = \hat{x} \left( \frac{\partial f_z}{\partial y} - \frac{\partial f_y}{\partial z} \right)
+ \hat{y} \left( \frac{\partial f_x}{\partial z} - \frac{\partial f_z}{\partial x} \right)
+ \hat{z} \left( \frac{\partial f_y}{\partial x} - \frac{\partial f_x}{\partial y} \right)
\tag{1.1.7}
$$

**Stokes' Theorem / 斯托克斯定理:**

$$
\iint_S (\nabla \times \mathbf{f}) \cdot d\mathbf{S} = \oint_C \mathbf{f} \cdot d\mathbf{l}
\tag{1.1.11}
$$

**Gradient / 梯度** of a scalar function / 标量函数的梯度：

$$
\nabla f = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \oint_s f \, d\mathbf{s}
\tag{1.1.12}
$$

**Laplacian / 拉普拉斯算子:**

$$
\nabla^2 f = \nabla \cdot (\nabla f)
\tag{1.1.17}
$$

### 1.1.2 Symbolic Vector Method | 符号矢量法

The symbolic vector $\tilde{\nabla}$ is defined such that / 符号矢量 $\tilde{\nabla}$ 定义为：

$$
T(\tilde{\nabla}) = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \oint_s T(\hat{n}) \, ds
\tag{1.1.21}
$$

Key relations / 关键关系：

| Operation / 运算 | Relationship / 关系 |
|-----------|-------------|
| Divergence / 散度 | $\nabla \cdot \mathbf{f} = \tilde{\nabla} \cdot \mathbf{f} = \mathbf{f} \cdot \tilde{\nabla}$ |
| Curl / 旋度 | $\nabla \times \mathbf{f} = \tilde{\nabla} \times \mathbf{f} = -\mathbf{f} \times \tilde{\nabla}$ |
| Gradient / 梯度 | $\nabla f = \tilde{\nabla} f = f \tilde{\nabla}$ |

Given two functions $a$ and $b$, the chain rule applies / 对两个函数 $a$, $b$ 应用链式法则：

$$
T(\tilde{\nabla}, a, b) = T(\tilde{\nabla}_a, a, b) + T(\tilde{\nabla}_b, a, b)
\tag{1.1.28}
$$

**Generalized Gauss' Theorem / 广义高斯定理:**

$$
\iiint_V T(\tilde{\nabla}) \, dV = \oiint_S T(\hat{n}) \, dS
\tag{1.1.37}
$$

**Useful vector identities derived via symbolic method / 用符号矢量法导出的常用矢量恒等式:**

$$
\nabla \times (\nabla \times \mathbf{f}) = \nabla(\nabla \cdot \mathbf{f}) - \nabla^2 \mathbf{f}
\tag{1.1.27}
$$

$$
\nabla \cdot (a\mathbf{b}) = \mathbf{b} \cdot (\nabla a) + a \nabla \cdot \mathbf{b}
\tag{1.1.31}
$$

$$
\nabla \times (a\mathbf{b}) = -\mathbf{b} \times \nabla a + a \nabla \times \mathbf{b}
\tag{1.1.33}
$$

$$
\nabla \times (\mathbf{a} \times \mathbf{b}) = (\mathbf{b} \cdot \nabla)\mathbf{a} - \mathbf{b} \nabla \cdot \mathbf{a} + \mathbf{a} \nabla \cdot \mathbf{b} - (\mathbf{a} \cdot \nabla)\mathbf{b}
\tag{1.1.36}
$$

**Example 1.1 / 例1.1** — 用广义高斯定理推导 $\iiint_V (\mathbf{b} \nabla \cdot \mathbf{a} + \mathbf{a} \cdot \nabla \mathbf{b}) dV = \oiint_S (\hat{n} \cdot \mathbf{a})\mathbf{b} \, dS$。

### 1.1.3 Helmholtz Decomposition Theorem | 亥姆霍兹分解定理

Any smooth vector function $\mathbf{F}$ vanishing at infinity can be decomposed into **irrotational** and **solenoidal** parts / 任意在无穷远处消失的光滑矢量函数可分解为**无旋**和**无散**两部分：

$$
\mathbf{F} = \mathbf{F}_i + \mathbf{F}_s
\tag{1.1.43}
$$

其中：

$$
\nabla \times \mathbf{F}_i = 0, \quad \nabla \cdot \mathbf{F}_i \ne 0
\qquad
\nabla \cdot \mathbf{F}_s = 0, \quad \nabla \times \mathbf{F}_s \ne 0
$$

**Key insight / 核心洞见：** 一旦 $\nabla \cdot \mathbf{F}$ 和 $\nabla \times \mathbf{F}$ 都被指定，$\mathbf{F}$ 就被完全确定。这是使用矢量和标量势的数学基础。

**Vector identities / 矢量恒等式:**

$$
\nabla \times (\nabla \varphi) = 0 \quad \text{(标量梯度为无旋场)}
\tag{1.1.41}
$$

$$
\nabla \cdot (\nabla \times \mathbf{A}) = 0 \quad \text{(矢量旋度为无散场)}
\tag{1.1.42}
$$

### 1.1.4 Green's Theorems | 格林定理

**First scalar Green's theorem / 第一标量格林定理** (in divergence theorem with $\mathbf{f} = a \nabla b$):

$$
\iiint_V (a \nabla^2 b + \nabla a \cdot \nabla b) \, dV = \oiint_S a \frac{\partial b}{\partial n} \, dS
\tag{1.1.45}
$$

**Second scalar Green's theorem / 第二标量格林定理:**

$$
\iiint_V (a \nabla^2 b - b \nabla^2 a) \, dV = \oiint_S \left( a \frac{\partial b}{\partial n} - b \frac{\partial a}{\partial n} \right) dS
\tag{1.1.46}
$$

**First vector Green's theorem / 第一矢量格林定理** (with $\mathbf{f} = \mathbf{a} \times \nabla \times \mathbf{b}$):

$$
\iiint_V [(\nabla \times \mathbf{a}) \cdot (\nabla \times \mathbf{b}) - \mathbf{a} \cdot (\nabla \times \nabla \times \mathbf{b})] dV
= \oiint_S (\mathbf{a} \times \nabla \times \mathbf{b}) \cdot d\mathbf{S}
\tag{1.1.47}
$$

**Second vector Green's theorem / 第二矢量格林定理:**

$$
\iiint_V [\mathbf{b} \cdot (\nabla \times \nabla \times \mathbf{a}) - \mathbf{a} \cdot (\nabla \times \nabla \times \mathbf{b})] dV
= \oiint_S (\mathbf{a} \times \nabla \times \mathbf{b} - \mathbf{b} \times \nabla \times \mathbf{a}) \cdot d\mathbf{S}
\tag{1.1.48}
$$

**Scalar-vector Green's theorem / 标量–矢量格林定理** (with $\mathbf{b} = \hat{b} b$):

$$
\iiint_V [b (\nabla \times \nabla \times \mathbf{a}) + \mathbf{a} \nabla^2 b + (\nabla \cdot \mathbf{a}) \nabla b] dV
= \oiint_S [(\hat{n} \cdot \mathbf{a}) \nabla b + (\hat{n} \times \mathbf{a}) \times \nabla b + (\hat{n} \times \nabla \times \mathbf{a}) b] dS
\tag{1.1.49}
$$

---

## 1.2 Maxwell's Equations in Terms of Total Charges and Currents | 以总电荷和总电流表述的麦克斯韦方程组

### 1.2.1 Integral Form | 积分形式

| Law / 定律 | Equation / 方程 |
|-----|----------|
| **Faraday's induction law / 法拉第感应定律** | $\displaystyle \oint_C \mathbf{E}(\mathbf{r}, t) \cdot d\mathbf{l} = -\frac{d}{dt} \iint_S \mathbf{B}(\mathbf{r}, t) \cdot d\mathbf{S}$ |
| **Maxwell–Ampère law / 麦克斯韦–安培定律** | $\displaystyle \oint_C \mathbf{B}(\mathbf{r}, t) \cdot d\mathbf{l} = \epsilon_0 \mu_0 \frac{d}{dt} \iint_S \mathbf{E}(\mathbf{r}, t) \cdot d\mathbf{S} + \mu_0 \iint_S \mathbf{J}_{\text{total}}(\mathbf{r}, t) \cdot d\mathbf{S}$ |
| **Gauss' law / 高斯定律** | $\displaystyle \oiint_S \mathbf{E}(\mathbf{r}, t) \cdot d\mathbf{S} = \frac{1}{\epsilon_0} \iiint_V \varrho_{e,\text{total}}(\mathbf{r}, t) \, dV$ |
| **Gauss' law (magnetic) / 高斯磁定律** | $\displaystyle \oiint_S \mathbf{B}(\mathbf{r}, t) \cdot d\mathbf{S} = 0$ |

**Free-space constants / 真空常数:**

$$
\epsilon_0 = 8.854 \times 10^{-12} \ \text{F/m} \approx \frac{1}{36\pi} \times 10^{-9} \ \text{F/m}
\qquad
\mu_0 = 4\pi \times 10^{-7} \ \text{H/m}
$$

**Example 1.3 / 例1.3** — 从法拉第定律推导含源RLC电路的基尔霍夫电压定律。

### 1.2.2 Differential Form | 微分形式

Using Stokes' and Gauss' theorems (valid in a continuous medium) / 由斯托克斯和高斯定理导出（在连续媒质内有效）：

| Law / 定律 | Equation / 方程 |
|-----|----------|
| **Faraday / 法拉第** | $\displaystyle \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$ |
| **Maxwell–Ampère / 麦克斯韦–安培** | $\displaystyle \nabla \times \mathbf{B} = \epsilon_0 \mu_0 \frac{\partial \mathbf{E}}{\partial t} + \mu_0 \mathbf{J}_{\text{total}}$ |
| **Gauss / 高斯** | $\displaystyle \nabla \cdot \mathbf{E} = \frac{\varrho_{e,\text{total}}}{\epsilon_0}$ |
| **Gauss (magnetic) / 高斯磁** | $\displaystyle \nabla \cdot \mathbf{B} = 0$ |

### 1.2.3 Current Continuity Equation | 电流连续性方程

From taking the divergence of the Maxwell–Ampère law / 对麦克斯韦–安培定律取散度获得：

$$
\nabla \cdot \mathbf{J}_{\text{total}} = -\frac{\partial \varrho_{e,\text{total}}}{\partial t}
\tag{1.2.16}
$$

Which yields the conservation of charge in integral form / 积分形式的电荷守恒：

$$
\oiint_S \mathbf{J}_{\text{total}} \cdot d\mathbf{S} = -\frac{d}{dt} \iiint_V \varrho_{e,\text{total}} \, dV
\tag{1.2.17}
$$

**Example 1.4 / 例1.4** — 从连续性方程推导节点电流定律 $\sum_{i=1}^N I_i = 0$。

### 1.2.4 The Lorentz Force Law | 洛伦兹力定律

$$
\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})
\tag{1.2.18}
$$

---

## 1.3 Constitutive Relations | 本构关系

### 1.3.1 Electric Polarization | 电极化

Electric dipole moment / 电偶极矩: $\mathbf{p} = q \boldsymbol{\ell}$。

Polarization vector / 极化矢量: $\mathbf{P} = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \sum_{i=1}^{n_p} \mathbf{p}_i$。

**Bound charge density / 束缚电荷密度:** $\varrho_{e,b} = -\nabla \cdot \mathbf{P}$。

Electric flux density / 电通量密度: $\mathbf{D} = \epsilon_0 \mathbf{E} + \mathbf{P}$。

**Linear dielectric / 线性电介质:** $\mathbf{D} = \epsilon \mathbf{E}$，其中 $\epsilon = \epsilon_0 (1 + \chi_e)$。

### 1.3.2 Magnetization | 磁化

Magnetic dipole moment / 磁偶极矩: $\mathbf{m} = I \mathbf{s}$。

Magnetization vector / 磁化矢量: $\mathbf{M} = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \sum_{i=1}^{n_m} \mathbf{m}_i$。

**Bound current density / 束缚电流密度:** $\mathbf{J}_m = \nabla \times \mathbf{M}$。

Magnetic field intensity / 磁场强度: $\mathbf{H} = \frac{\mathbf{B}}{\mu_0} - \mathbf{M}$。

**Linear magnetic material / 线性磁性材料:** $\mathbf{B} = \mu \mathbf{H}$，其中 $\mu = \mu_0 (1 + \chi_m)$。

### 1.3.3 Electric Conduction | 电导

**Ohm's law / 欧姆定律:** $\mathbf{J}_c = \sigma \mathbf{E}$。

### 1.3.4 Classification of Media | 媒质分类

| Criterion / 分类标准 | Types / 类型 |
|-----------|-------|
| Spatial / 空间 | homogeneous / 均匀, inhomogeneous / 非均匀 |
| Temporal / 时间 | stationary / 稳态, nonstationary / 非稳态 |
| Directional / 方向 | isotropic / 各向同性, anisotropic / 各向异性, bi-anisotropic / 双各向异性 |
| Linearity / 线性 | linear / 线性, nonlinear / 非线性 |
| Frequency / 频率 | dispersive / 色散, nondispersive / 非色散 |
| Conductivity / 电导率 | dielectric ($\sigma=0$), lossy ($0<\sigma<\infty$), PEC ($\sigma\to\infty$) |
| Permeability / 磁导率 | diamagnetic / 抗磁 ($\mu_r \lesssim 1$), paramagnetic / 顺磁 ($\mu_r \gtrsim 1$), ferromagnetic / 铁磁 ($\mu_r \gg 1$) |

---

## 1.4 Maxwell's Equations in Terms of Free Charges and Currents | 以自由电荷和自由电流表述的麦克斯韦方程组

**Differential form / 微分形式:**

| Law / 定律 | Equation / 方程 |
|-----|----------|
| **Faraday / 法拉第** | $\displaystyle \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} - \mathbf{M}_f$ |
| **Maxwell–Ampère / 麦克斯韦–安培** | $\displaystyle \nabla \times \mathbf{H} = \frac{\partial \mathbf{D}}{\partial t} + \mathbf{J}_f$ |
| **Gauss / 高斯** | $\displaystyle \nabla \cdot \mathbf{D} = \varrho_{e,f}$ |
| **Gauss (magnetic) / 高斯磁** | $\displaystyle \nabla \cdot \mathbf{B} = \varrho_{m,f}$ |

---

## 1.5 Boundary Conditions | 边界条件

### General Interface / 一般界面

From the integral form with a rectangular frame and pillbox / 从积分形式用矩形回路和药片盒模型导出：

| Condition / 条件 | Equation / 方程 |
|-----------|----------|
| Tangential $\mathbf{H}$ / $\mathbf{H}$ 切向 | $\hat{n} \times (\mathbf{H}_2 - \mathbf{H}_1) = \mathbf{J}_s$ |
| Tangential $\mathbf{E}$ / $\mathbf{E}$ 切向 | $\hat{n} \times (\mathbf{E}_2 - \mathbf{E}_1) = -\mathbf{M}_s$ |
| Normal $\mathbf{D}$ / $\mathbf{D}$ 法向 | $\hat{n} \cdot (\mathbf{D}_2 - \mathbf{D}_1) = \varrho_{e,s}$ |
| Normal $\mathbf{B}$ / $\mathbf{B}$ 法向 | $\hat{n} \cdot (\mathbf{B}_2 - \mathbf{B}_1) = \varrho_{m,s}$ |

### Perfect Electric Conductor (PEC) / 理想电导体 (PEC)

$$
\hat{n} \times \mathbf{E} = 0, \quad
\hat{n} \times \mathbf{H} = \mathbf{J}_s, \quad
\hat{n} \cdot \mathbf{D} = \varrho_{e,s}, \quad
\hat{n} \cdot \mathbf{B} = 0
$$

**物理直觉：** 在PEC中，自由电荷瞬间移动以抵消内部场，产生表面电流和电荷。切向电场在PEC表面必为零；否则将产生无限大电流。

**Example 1.5 / 例1.5** — 关联总电荷边界条件与自由电荷边界条件，识别出磁化产生面电流 $\mathbf{J}_{m,s} = -\hat{n} \times \mathbf{M}$，极化产生束缚面电荷 $\varrho_{e,b,s} = \hat{n} \cdot \mathbf{P}$。

---

## 1.6 Energy, Power, and Poynting's Theorem | 能量、功率与坡印廷定理

**Poynting vector / 坡印廷矢量** (instantaneous power flux density / 瞬时功率流密度):

$$
\mathbf{S}(\mathbf{r}, t) = \mathbf{E}(\mathbf{r}, t) \times \mathbf{H}(\mathbf{r}, t)
\tag{1.6.17}
$$

**Poynting's theorem (integral form) / 坡印廷定理（积分形式）** — conservation of electromagnetic energy / 电磁能量守恒：

$$
P_s = P_e + P_d + \frac{d}{dt} (W_e + W_m)
\tag{1.6.14}
$$

其中：

| Quantity / 物理量 | Expression / 表达式 | Meaning / 含义 |
|----------|------------|---------|
| $P_s$ | $-\iiint_V (\mathbf{E} \cdot \mathbf{J}_i + \mathbf{H} \cdot \mathbf{M}_i) dV$ | 供给功率 |
| $P_e$ | $\oiint_S (\mathbf{E} \times \mathbf{H}) \cdot \hat{n} \, dS$ | 流出功率 |
| $P_d$ | $\iiint_V \sigma |\mathbf{E}|^2 dV$ | 耗散功率 |
| $W_e$ | $\frac{1}{2} \iiint_V \epsilon |\mathbf{E}|^2 dV$ | 电场储能 |
| $W_m$ | $\frac{1}{2} \iiint_V \mu |\mathbf{H}|^2 dV$ | 磁场储能 |

---

## 1.7 Time-Harmonic Fields | 时谐场

### 1.7.1 Phasor Representation | 相量表示

For a time-harmonic field at angular frequency $\omega$ / 对于角频率 $\omega$ 的时谐场：

$$
\mathbf{E}(\mathbf{r}, t) = \text{Re}\left[\mathbf{E}(\mathbf{r}) e^{j\omega t}\right]
$$

The time derivative $\partial/\partial t \mapsto j\omega$ / 时间导数替换 $\partial/\partial t \mapsto j\omega$：

$$
\nabla \times \mathbf{E} = -j\omega \mathbf{B} - \mathbf{M}_f, \quad
\nabla \times \mathbf{H} = j\omega \mathbf{D} + \mathbf{J}_f
$$

### 1.7.2 Fourier Transforms | 傅里叶变换

For arbitrary time dependence, the Fourier transform yields the same frequency-domain equations / 任意时间依赖通过傅里叶变换得到相同的频域方程。

### 1.7.3 Complex Power | 复功率

**Time-average Poynting vector / 时间平均坡印廷矢量:**

$$
\langle \mathbf{S}(\mathbf{r}, t) \rangle = \frac{1}{2} \text{Re}[\mathbf{E} \times \mathbf{H}^*]
\tag{1.7.23}
$$

**Complex Poynting theorem / 复坡印廷定理:**

$$
P_s = P_e + P_d + j 2\omega (W_m - W_e)
\tag{1.7.40}
$$

其中 $P_e = \frac{1}{2} \oiint_S (\mathbf{E} \times \mathbf{H}^*) \cdot d\mathbf{S}$, $P_d = \frac{1}{2} \iiint_V \sigma |\mathbf{E}|^2 dV$, $W_e = \frac{1}{4} \iiint_V \epsilon |\mathbf{E}|^2 dV$, $W_m = \frac{1}{4} \iiint_V \mu |\mathbf{H}|^2 dV$。

**物理解释：** 实部给出时间平均功率平衡；虚部与电场和磁场平均储能之差相关（无功功率）。

### 1.7.4 Complex Permittivity and Permeability | 复介电常数和复磁导率

$$
\epsilon_r = \epsilon_r' - j \epsilon_r'', \quad
\mu_r = \mu_r' - j \mu_r''
$$

**Loss tangent / 损耗角正切:**

$$
\tan\delta_e = \frac{\epsilon_r''}{\epsilon_r'}, \quad
\tan\delta_m = \frac{\mu_r''}{\mu_r'}
$$

**Kramers–Krönig relations / 克拉默斯–克勒尼希关系** — causality requires that dispersion implies loss / 因果关系强制要求色散必然伴随损耗：

$$
\epsilon'(\omega) = \epsilon_\infty + \frac{2}{\pi} \,\text{P}\!\!\int_0^\infty \frac{z \epsilon''(z)}{z^2 - \omega^2} dz
$$

$$
\epsilon''(\omega) = -\frac{2\omega}{\pi} \,\text{P}\!\!\int_0^\infty \frac{\epsilon'(z) - \epsilon_\infty}{z^2 - \omega^2} dz
$$

---

## Key Physical Intuition | 关键物理直觉

1. **符号矢量法** 将 $\nabla$ 视为普通矢量，优雅地推导矢量恒等式，避免了分量级推演。
2. **亥姆霍兹分解** 是使用矢量和标量势的数学基础：任何场由其散度和旋度完全确定。
3. **坡印廷定理** 是电磁场的能量守恒定律——理解功率流、耗散和无功功率的基石。
4. **复相量形式** 将4D（时空）问题降为3D，坡印廷定理的虚部揭示了与电场和磁场储能差相关的无功功率。
5. **克拉默斯–克勒尼希关系** 强制色散与损耗的关联——因果媒质不能只有其一而无其二。

---

## Original Examples in This Chapter / 本章原始例题

| Example / 例题 | Topic / 主题 | Section / 节 |
|---------|-------|---------|
| 1.1 | 用广义高斯定理推导积分定理 | 1.1.2 |
| 1.2 | 推导标量–矢量格林定理 | 1.1.4 |
| 1.3 | 法拉第定律 → 基尔霍夫电压定律 | 1.2.1 |
| 1.4 | 连续性方程 → 基尔霍夫电流定律 | 1.2.3 |
| 1.5 | 总电荷量与自由电荷量的边界条件 | 1.5 |
| 1.6 | 洛伦兹介电模型（频率相关$\epsilon_r$） | 1.7.2 |
| 1.7 | 金属盒开槽的复功率 | 1.7.3 |
| 1.8 | 等离子体介电常数的德鲁德模型 | 1.7.4 |
| 1.9 | 色散媒质的克拉默斯–克勒尼希关系 | 1.7.4 |

---

## Audit / 审计

| Section / 节 | Content Coverage / 内容覆盖 | Notes Alignment / 笔记对应 |
|---------|-----------------|-----------------|
| 1.1 | 矢量分析、恒等式、定理 | 完整覆盖 |
| 1.2 | 麦克斯韦方程组（总电荷） | 完整覆盖 |
| 1.3 | 本构关系 | 完整覆盖 |
| 1.4 | 麦克斯韦方程组（自由电荷） | 完整覆盖 |
| 1.5 | 边界条件 | 完整覆盖 |
| 1.6 | 坡印廷定理 | 完整覆盖 |
| 1.7 | 时谐场、复功率 | 完整覆盖 |
| Examples / 例题 | 全部9个例题 | 标注原始编号 |
