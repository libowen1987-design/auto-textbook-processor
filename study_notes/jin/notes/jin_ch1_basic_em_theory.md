# Chapter 1: Basic Electromagnetic Theory | 第一章：基本电磁理论

> **中英双语版**

**Source:** Jin, *Theory and Computation of Electromagnetic Fields*, 2nd Ed., Chapter 1 (pp. 27–76)

---

## 1.1 Review of Vector Analysis | 矢量分析回顾

### 1.1.1 Vector Operations and Integral Theorems | 矢量运算与积分定理

**Divergence / 散度:**

$$
\nabla \cdot \mathbf{f} = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \oint_{s} \mathbf{f} \cdot d\mathbf{s}
\tag{1.1.1}
$$

散度衡量矢量场从某点流出的净通量密度。

- Rectangular: $\nabla \cdot \mathbf{f} = \frac{\partial f_x}{\partial x} + \frac{\partial f_y}{\partial y} + \frac{\partial f_z}{\partial z}$ (1.1.2)
- Cylindrical: $\nabla \cdot \mathbf{f} = \frac{1}{\rho}\frac{\partial(\rho f_\rho)}{\partial \rho} + \frac{\partial f_\phi}{\rho \partial \phi} + \frac{\partial f_z}{\partial z}$ (1.1.3)
- Spherical: $\nabla \cdot \mathbf{f} = \frac{1}{r^2}\frac{\partial}{\partial r}(r^2 f_r) + \frac{1}{r\sin\theta}\frac{\partial}{\partial \theta}(f_\theta\sin\theta) + \frac{1}{r\sin\theta}\frac{\partial f_\phi}{\partial \phi}$ (1.1.4)

**Divergence Theorem (Gauss' Theorem) / 散度定理（高斯定理）:**

$$
\iiint_V \nabla \cdot \mathbf{f} \, dV = \oint_{S} \mathbf{f} \cdot d\mathbf{S}
\tag{1.1.5}
$$

体积分与封闭曲面积分的桥梁，将散度的体积分转化为通量的面积分。

**Curl / 旋度:**

$$
\nabla \times \mathbf{f} = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \oint_{s} d\mathbf{s} \times \mathbf{f}
\tag{1.1.6}
$$

旋度衡量矢量场在某点的旋转强度与方向。

- Rectangular: $\nabla \times \mathbf{f} = \hat{x}\left(\frac{\partial f_z}{\partial y} - \frac{\partial f_y}{\partial z}\right) + \hat{y}\left(\frac{\partial f_x}{\partial z} - \frac{\partial f_z}{\partial x}\right) + \hat{z}\left(\frac{\partial f_y}{\partial x} - \frac{\partial f_x}{\partial y}\right)$ (1.1.7)
- Cylindrical: $\nabla \times \mathbf{f} = \hat{\rho}\left(\frac{\partial f_z}{\rho\partial\phi} - \frac{\partial f_\phi}{\partial z}\right) + \hat{\phi}\left(\frac{\partial f_\rho}{\partial z} - \frac{\partial f_z}{\partial \rho}\right) + \hat{z}\frac{1}{\rho}\left[\frac{\partial (\rho f_\phi)}{\partial \rho} - \frac{\partial f_\rho}{\partial \phi}\right]$ (1.1.8)
- Spherical: $\nabla \times \mathbf{f} = \hat{r}\frac{1}{r\sin\theta}\left[\frac{\partial}{\partial\theta}(f_\phi\sin\theta) - \frac{\partial f_\theta}{\partial\phi}\right] + \hat{\theta}\frac{1}{r}\left[\frac{1}{\sin\theta}\frac{\partial f_r}{\partial\phi} - \frac{\partial}{\partial r}(rf_\phi)\right] + \hat{\phi}\frac{1}{r}\left[\frac{\partial}{\partial r}(rf_\theta) - \frac{\partial f_r}{\partial\theta}\right]$ (1.1.9)

**Alternative definition / 旋度的另一种定义** (curl in a given direction $\hat{a}$):

$$
\hat{a} \cdot (\nabla \times \mathbf{f}) = \lim_{\Delta s \to 0} \frac{1}{\Delta s} \oint_c \mathbf{f} \cdot d\mathbf{l}
\tag{1.1.10}
$$

**Stokes' Theorem / 斯托克斯定理:**

$$
\iint_S (\nabla \times \mathbf{f}) \cdot d\mathbf{S} = \oint_C \mathbf{f} \cdot d\mathbf{l}
\tag{1.1.11}
$$

将旋度的面积分转化为环量线积分，是散度定理在旋度上的类比。

**Gradient / 梯度:**

$$
\nabla f = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \oint_s f \, d\mathbf{s}
\tag{1.1.12}
$$

$$
\hat{a} \cdot \nabla f = \frac{\partial f}{\partial a}
\tag{1.1.13}
$$

梯度给出标量函数变化最快的方向和速率。

- Rectangular: $\nabla f = \hat{x}\frac{\partial f}{\partial x} + \hat{y}\frac{\partial f}{\partial y} + \hat{z}\frac{\partial f}{\partial z}$ (1.1.14)
- Cylindrical: $\nabla f = \hat{\rho}\frac{\partial f}{\partial \rho} + \hat{\phi}\frac{\partial f}{\rho\partial\phi} + \hat{z}\frac{\partial f}{\partial z}$ (1.1.15)
- Spherical: $\nabla f = \hat{r}\frac{\partial f}{\partial r} + \hat{\theta}\frac{\partial f}{r\partial\theta} + \hat{\phi}\frac{1}{r\sin\theta}\frac{\partial f}{\partial \phi}$ (1.1.16)

**Laplacian / 拉普拉斯算子:**

$$
\nabla^2 f = \nabla \cdot (\nabla f)
\tag{1.1.17}
$$

标量函数的梯度的散度，在电磁场中出现在泊松方程和亥姆霍兹方程中。

- Rectangular: $\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}$ (1.1.18)
- Cylindrical: $\nabla^2 f = \frac{1}{\rho}\frac{\partial}{\partial \rho}\left(\rho\frac{\partial f}{\partial \rho}\right) + \frac{1}{\rho^2}\frac{\partial^2 f}{\partial \phi^2} + \frac{\partial^2 f}{\partial z^2}$ (1.1.19)
- Spherical: $\nabla^2 f = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial f}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial \theta}\left(\sin\theta\frac{\partial f}{\partial \theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2 f}{\partial \phi^2}$ (1.1.20)

### 1.1.2 Symbolic Vector Method | 符号矢量法

定义符号矢量 $\tilde{\nabla}$ 使得：

$$
T(\tilde{\nabla}) = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \oint_s T(\hat{n}) \, ds
\tag{1.1.21}
$$

符号矢量法将 $\nabla$ 视为普通矢量，避免分量级推导。

Properties / 性质:
- $\tilde{\nabla} \cdot \mathbf{f} = \mathbf{f} \cdot \tilde{\nabla} = \nabla \cdot \mathbf{f}$
- $\tilde{\nabla} \times \mathbf{f} = -\mathbf{f} \times \tilde{\nabla} = \nabla \times \mathbf{f}$
- $\tilde{\nabla} f = f \tilde{\nabla} = \nabla f$

**Generalized Gauss' Theorem / 广义高斯定理:**

$$
\iiint_V T(\tilde{\nabla}) \, dV = \oint_S T(\hat{n}) \, dS
\tag{1.1.37}
$$

**Key identities derived / 导出的关键恒等式:**
- $\nabla \times (\nabla \times \mathbf{f}) = \nabla(\nabla \cdot \mathbf{f}) - \nabla^2 \mathbf{f}$ (1.1.27)
- $\nabla \cdot (a\mathbf{b}) = \mathbf{b} \cdot (\nabla a) + a\nabla \cdot \mathbf{b}$ (1.1.31)
- $\nabla \times (a\mathbf{b}) = -\mathbf{b} \times \nabla a + a\nabla \times \mathbf{b}$ (1.1.33)
- $\nabla \times (\mathbf{a} \times \mathbf{b}) = (\mathbf{b} \cdot \nabla)\mathbf{a} - \mathbf{b}\nabla \cdot \mathbf{a} + \mathbf{a}\nabla \cdot \mathbf{b} - (\mathbf{a} \cdot \nabla)\mathbf{b}$ (1.1.36)

**Curl Theorem / 旋度定理:**

$$
\iiint_V \nabla \times \mathbf{f} \, dV = \oint_S d\mathbf{S} \times \mathbf{f}
\tag{1.1.38}
$$

---

### 1.1.3 Helmholtz Decomposition Theorem | 亥姆霍兹分解定理

Any smooth vector function $\mathbf{F}$ that vanishes at infinity can be decomposed / 任意在无穷远处衰减的光滑矢量函数可分解为：

$$
\mathbf{F} = \mathbf{F}_i + \mathbf{F}_s
\tag{1.1.43}
$$

- **Irrotational** (curl-free, 无旋) part: $\nabla \times \mathbf{F}_i = 0$, $\nabla \cdot \mathbf{F}_i \neq 0$
- **Solenoidal** (divergence-free, 无散) part: $\nabla \cdot \mathbf{F}_s = 0$, $\nabla \times \mathbf{F}_s \neq 0$

**Key identities / 关键恒等式:**
- $\nabla \times (\nabla \phi) = 0$ (标量梯度的旋度恒为零) (1.1.41)
- $\nabla \cdot (\nabla \times \mathbf{A}) = 0$ (矢量旋度的散度恒为零) (1.1.42)

> **核心洞见：** 一旦矢量的散度和旋度都被指定，该矢量就被完全确定。这是引入标量势和矢量势的数学基础。

### 1.1.4 Green's Theorems | 格林定理

**First Scalar Green's Theorem / 第一标量格林定理:**

$$
\iiint_V (a\nabla^2 b + \nabla a \cdot \nabla b) \, dV = \oint_S a\frac{\partial b}{\partial n} \, dS
\tag{1.1.45}
$$

由散度定理在 $\mathbf{f} = a\nabla b$ 下导出。

**Second Scalar Green's Theorem / 第二标量格林定理:**

$$
\iiint_V (a\nabla^2 b - b\nabla^2 a) \, dV = \oint_S \left(a\frac{\partial b}{\partial n} - b\frac{\partial a}{\partial n}\right) dS
\tag{1.1.46}
$$

**First Vector Green's Theorem / 第一矢量格林定理:**

$$
\iiint_V [(\nabla \times \mathbf{a}) \cdot (\nabla \times \mathbf{b}) - \mathbf{a} \cdot (\nabla \times \nabla \times \mathbf{b})] \, dV = \oint_S (\mathbf{a} \times \nabla \times \mathbf{b}) \cdot d\mathbf{S}
\tag{1.1.47}
$$

**Second Vector Green's Theorem / 第二矢量格林定理:**

$$
\iiint_V [\mathbf{b} \cdot (\nabla \times \nabla \times \mathbf{a}) - \mathbf{a} \cdot (\nabla \times \nabla \times \mathbf{b})] \, dV = \oint_S (\mathbf{a} \times \nabla \times \mathbf{b} - \mathbf{b} \times \nabla \times \mathbf{a}) \cdot d\mathbf{S}
\tag{1.1.48}
$$

**Scalar–Vector Green's Theorem / 标量–矢量格林定理:**

$$
\iiint_V [b(\nabla \times \nabla \times \mathbf{a}) + \mathbf{a}\nabla^2 b + (\nabla \cdot \mathbf{a})\nabla b] \, dV
= \oint_S [(\hat{n} \cdot \mathbf{a})\nabla b + (\hat{n} \times \mathbf{a}) \times \nabla b + (\hat{n} \times \nabla \times \mathbf{a})b] \, dS
\tag{1.1.49}
$$

这些格林定理是边界元法和积分方程公式推演的数学基石。

---

## 1.2 Maxwell's Equations in Terms of Total Charges and Currents | 以总电荷和总电流表述的麦克斯韦方程组

### 1.2.1 Maxwell's Equations in Integral Form | 麦克斯韦方程组积分形式

**Faraday's Induction Law / 法拉第感应定律:**

$$
\oint_C \mathbf{E}(\mathbf{r}, t) \cdot d\mathbf{l} = -\frac{d}{dt} \iint_S \mathbf{B}(\mathbf{r}, t) \cdot d\mathbf{S}
\tag{1.2.1}
$$

电场沿闭合回路的环量等于穿过回路的磁通量变化率的负值。

**Maxwell–Ampère Law / 麦克斯韦–安培定律:**

$$
\oint_C \mathbf{B}(\mathbf{r}, t) \cdot d\mathbf{l} = \epsilon_0\mu_0 \frac{d}{dt} \iint_S \mathbf{E}(\mathbf{r}, t) \cdot d\mathbf{S} + \mu_0 \iint_S \mathbf{J}_{\text{total}}(\mathbf{r}, t) \cdot d\mathbf{S}
\tag{1.2.2}
$$

磁场沿闭合回路的环量等于穿过回路的电场通量变化率与电流之和。

**Gauss' Law (Electric) / 高斯定律（电场）:**

$$
\oint_S \mathbf{E}(\mathbf{r}, t) \cdot d\mathbf{S} = \frac{1}{\epsilon_0} \iiint_V \varrho_{e,\text{total}}(\mathbf{r}, t) \, dV
\tag{1.2.8}
$$

**Gauss' Law (Magnetic) / 高斯定律（磁场）:**

$$
\oint_S \mathbf{B}(\mathbf{r}, t) \cdot d\mathbf{S} = 0
\tag{1.2.9}
$$

**Physical constants / 物理常数:**
- $\epsilon_0 = 8.854 \times 10^{-12}$ F/m $\approx 1/(36\pi) \times 10^{-9}$ F/m (真空介电常数)
- $\mu_0 = 4\pi \times 10^{-7}$ H/m (真空磁导率)

### 1.2.2 Maxwell's Equations in Differential Form | 麦克斯韦方程组微分形式

Applying Stokes' and Gauss' theorems to a continuous medium / 在连续介质中应用斯托克斯和高斯定理：

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
\tag{1.2.12}
$$

$$
\nabla \times \mathbf{B} = \epsilon_0\mu_0 \frac{\partial \mathbf{E}}{\partial t} + \mu_0 \mathbf{J}_{\text{total}}
\tag{1.2.13}
$$

$$
\nabla \cdot \mathbf{E} = \frac{\varrho_{e,\text{total}}}{\epsilon_0}
\tag{1.2.14}
$$

$$
\nabla \cdot \mathbf{B} = 0
\tag{1.2.15}
$$

### 1.2.3 Current Continuity Equation | 电流连续性方程

$$
\nabla \cdot \mathbf{J}_{\text{total}} = -\frac{\partial \varrho_{e,\text{total}}}{\partial t}
\tag{1.2.16}
$$

**Integral form / 积分形式:**

$$
\oint_S \mathbf{J}_{\text{total}} \cdot d\mathbf{S} = -\frac{d}{dt} \iiint_V \varrho_{e,\text{total}} \, dV
\tag{1.2.17}
$$

> 四个麦克斯韦方程对于时变场并非独立——连续性方程将它们联系在一起。

### 1.2.4 The Lorentz Force Law | 洛伦兹力定律

$$
\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})
\tag{1.2.18}
$$

---

## 1.3 Constitutive Relations | 本构关系

### 1.3.1 Electric Polarization | 电极化

- **Dipole moment / 电偶极矩:** $\mathbf{p} = q\mathbf{l}$ (1.3.1)
- **Polarization vector / 极化矢量:** $\mathbf{P} = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \sum_{i=1}^{n_p} \mathbf{p}_i$ (1.3.2)
- **Bound charge density / 束缚电荷密度:** $\varrho_{e,b} = -\nabla \cdot \mathbf{P}$ (1.3.3)
- **Total charge density / 总电荷密度:** $\varrho_{e,\text{total}} = \varrho_{e,f} + \varrho_{e,b}$ (1.3.4)

**Electric flux density / 电通量密度:**

$$
\mathbf{D} = \epsilon_0\mathbf{E} + \mathbf{P}
\tag{1.3.6}
$$

**Gauss' law in terms of free charges / 以自由电荷表述的高斯定律:**

$$
\nabla \cdot \mathbf{D} = \varrho_{e,f}
\tag{1.3.7}
$$

**Linear dielectric / 线性电介质:**

$$
\mathbf{P} = \epsilon_0\chi_e\mathbf{E}, \quad \mathbf{D} = \epsilon_0(1 + \chi_e)\mathbf{E} = \epsilon\mathbf{E}
\tag{1.3.9–1.3.10}
$$

- $\chi_e$ = 电极化率, $\epsilon = \epsilon_0(1 + \chi_e)$ = 介电常数, $\epsilon_r = \epsilon/\epsilon_0$ = 相对介电常数

### 1.3.2 Magnetization | 磁化

- **Magnetic dipole moment / 磁偶极矩:** $\mathbf{m} = I\mathbf{s}$ (1.3.12)
- **Magnetization vector / 磁化矢量:** $\mathbf{M} = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \sum_{i=1}^{n_m} \mathbf{m}_i$ (1.3.13)
- **Magnetization current density / 磁化电流密度:** $\mathbf{J}_m = \nabla \times \mathbf{M}$ (1.3.14)

**Magnetic field intensity / 磁场强度:**

$$
\mathbf{H} = \frac{\mathbf{B}}{\mu_0} - \mathbf{M}
\tag{1.3.17}
$$

$$
\mathbf{B} = \mu_0(\mathbf{H} + \mathbf{M})
\tag{1.3.19}
$$

**Linear magnetic material / 线性磁性材料:**

$$
\mathbf{M} = \chi_m\mathbf{H}, \quad \mathbf{B} = \mu_0(1 + \chi_m)\mathbf{H} = \mu\mathbf{H}
\tag{1.3.20–1.3.21}
$$

- $\chi_m$ = 磁化率, $\mu = \mu_0(1 + \chi_m)$ = 磁导率, $\mu_r = \mu/\mu_0$ = 相对磁导率

### 1.3.3 Electric Conduction | 电导

**Ohm's law (local form) / 欧姆定律（局部形式）:**

$$
\mathbf{J}_c = \sigma \mathbf{E}
\tag{1.3.23}
$$

- $\sigma$ = 电导率 (S/m)

### 1.3.4 Classification of Media | 媒质分类

| Classification / 分类 | Criterion / 判据 |
|---|---|
| **Homogeneous vs inhomogeneous / 均匀 vs 非均匀** | $\epsilon, \mu, \sigma$ 是否依赖于位置 |
| **Stationary vs nonstationary / 稳态 vs 非稳态** | $\epsilon, \mu, \sigma$ 是否依赖于时间 |
| **Isotropic vs anisotropic / 各向同性 vs 各向异性** | $\mathbf{D} \parallel \mathbf{E}$, $\mathbf{B} \parallel \mathbf{H}$? |
| **Linear vs nonlinear / 线性 vs 非线性** | $\epsilon, \mu, \sigma$ 是否依赖于场强 |
| **Dispersive vs nondispersive / 色散 vs 非色散** | $\epsilon, \mu$ 是否依赖于频率 |
| **Dielectric, lossy, conductor / 介质、有损耗、导体** | $\sigma$ 的数值 |
| **Diamagnetic/paramagnetic/ferromagnetic / 抗磁/顺磁/铁磁** | $\mu$ 的数值 |

**Anisotropic constitutive relations (tensor form) / 各向异性本构关系（张量形式）:**

$$
\begin{bmatrix} D_x \\ D_y \\ D_z \end{bmatrix} =
\begin{bmatrix} \epsilon_{xx} & \epsilon_{xy} & \epsilon_{xz} \\ \epsilon_{yx} & \epsilon_{yy} & \epsilon_{yz} \\ \epsilon_{zx} & \epsilon_{zy} & \epsilon_{zz} \end{bmatrix}
\begin{bmatrix} E_x \\ E_y \\ E_z \end{bmatrix}
\tag{1.3.25}
$$

**Bianisotropic (most general linear form) / 双各向异性（最一般线性形式）:**

$$
\mathbf{D} = \boldsymbol{\epsilon} \cdot \mathbf{E} + \boldsymbol{\xi} \cdot \mathbf{H}
$$
$$
\mathbf{B} = \boldsymbol{\mu} \cdot \mathbf{H} + \boldsymbol{\zeta} \cdot \mathbf{E}
\tag{1.3.28}
$$

**Dispersive media (convolution form) / 色散媒质（卷积形式）:**

$$
\mathbf{D} = \epsilon_0\mathbf{E} + \epsilon_0 \int_{-\infty}^{t} \chi_e(t - \tau)\mathbf{E}(\tau) \, d\tau
\tag{1.3.29}
$$

$$
\mathbf{B} = \mu_0\mathbf{H} + \mu_0 \int_{-\infty}^{t} \chi_m(t - \tau)\mathbf{H}(\tau) \, d\tau
\tag{1.3.30}
$$

---

## 1.4 Maxwell's Equations in Terms of Free Charges and Currents | 以自由电荷和自由电流表述的麦克斯韦方程组

**Integral form / 积分形式:**

$$
\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \iint_S \mathbf{B} \cdot d\mathbf{S}
\tag{1.4.1}
$$

$$
\oint_C \mathbf{H} \cdot d\mathbf{l} = \frac{d}{dt} \iint_S \mathbf{D} \cdot d\mathbf{S} + \iint_S \mathbf{J}_f \cdot d\mathbf{S}
\tag{1.4.2}
$$

$$
\oint_S \mathbf{D} \cdot d\mathbf{S} = \iiint_V \varrho_{e,f} \, dV
\tag{1.4.3}
$$

$$
\oint_S \mathbf{B} \cdot d\mathbf{S} = 0
\tag{1.4.4}
$$

**With magnetic sources (symmetrized form) / 引入磁流源（对称化形式）:**

$$
\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \iint_S \mathbf{B} \cdot d\mathbf{S} - \iint_S \mathbf{M}_f \cdot d\mathbf{S}
\tag{1.4.5}
$$

$$
\oint_S \mathbf{B} \cdot d\mathbf{S} = \iiint_V \varrho_{m,f} \, dV
\tag{1.4.6}
$$

引入虚构的磁流 $\mathbf{M}_f$ 和磁荷 $\varrho_{m,f}$ 是为了数学对称性，便于用等效原理处理问题。

**Differential form / 微分形式:**

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} - \mathbf{M}_f
\tag{1.4.7}
$$

$$
\nabla \times \mathbf{H} = \frac{\partial \mathbf{D}}{\partial t} + \mathbf{J}_f
\tag{1.4.8}
$$

$$
\nabla \cdot \mathbf{D} = \varrho_{e,f}
\tag{1.4.9}
$$

$$
\nabla \cdot \mathbf{B} = \varrho_{m,f}
\tag{1.4.10}
$$

**Continuity equations / 连续性方程:**

$$
\nabla \cdot \mathbf{J}_f = -\frac{\partial \varrho_{e,f}}{\partial t}
\tag{1.4.11}
$$

$$
\nabla \cdot \mathbf{M}_f = -\frac{\partial \varrho_{m,f}}{\partial t}
\tag{1.4.12}
$$

---

## 1.5 Boundary Conditions | 边界条件

从积分形式在矩形回路和药片盒模型上取极限导出。

**Tangential $\mathbf{H}$ / $\mathbf{H}$ 的切向分量:**

$$
\hat{n} \times (\mathbf{H}_2 - \mathbf{H}_1) = \mathbf{J}_s
\tag{1.5.4}
$$

**Tangential $\mathbf{E}$ / $\mathbf{E}$ 的切向分量:**

$$
\hat{n} \times (\mathbf{E}_2 - \mathbf{E}_1) = -\mathbf{M}_s
\tag{1.5.5}
$$

**Normal $\mathbf{D}$ / $\mathbf{D}$ 的法向分量:**

$$
\hat{n} \cdot (\mathbf{D}_2 - \mathbf{D}_1) = \varrho_{e,s}
\tag{1.5.7}
$$

**Normal $\mathbf{B}$ / $\mathbf{B}$ 的法向分量:**

$$
\hat{n} \cdot (\mathbf{B}_2 - \mathbf{B}_1) = \varrho_{m,s}
\tag{1.5.8}
$$

**PEC (Perfect Electric Conductor) boundary / 理想电导体边界:**

$$
\hat{n} \times \mathbf{E} = 0
\tag{1.5.9}
$$

$$
\hat{n} \times \mathbf{H} = \mathbf{J}_s
\tag{1.5.10}
$$

$$
\hat{n} \cdot \mathbf{D} = \varrho_{e,s}
\tag{1.5.11}
$$

$$
\hat{n} \cdot \mathbf{B} = 0
\tag{1.5.12}
$$

PEC上切向电场为零，法向磁场为零——自由电荷在表面瞬间移动以抵消内部场。

---

## 1.6 Energy, Power, and Poynting's Theorem | 能量、功率与坡印廷定理

从含外加源 $\mathbf{J}_i$, $\mathbf{M}_i$ 的麦克斯韦方程组出发：

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} - \mathbf{M}_i
\tag{1.6.1}
$$

$$
\nabla \times \mathbf{H} = \frac{\partial \mathbf{D}}{\partial t} + \sigma\mathbf{E} + \mathbf{J}_i
\tag{1.6.2}
$$

Derived power balance / 导出的功率平衡关系：

$$
\nabla \cdot (\mathbf{E} \times \mathbf{H}) + \mathbf{E} \cdot \frac{\partial \mathbf{D}}{\partial t} + \mathbf{H} \cdot \frac{\partial \mathbf{B}}{\partial t} + \sigma \mathbf{E} \cdot \mathbf{E} + \mathbf{E} \cdot \mathbf{J}_i + \mathbf{H} \cdot \mathbf{M}_i = 0
\tag{1.6.4}
$$

**Poynting vector (power flux density) / 坡印廷矢量（功率流密度）:**

$$
\mathbf{S} = \mathbf{E} \times \mathbf{H}
\tag{1.6.17}
$$

**Energy densities / 能量密度:**
- Electric: $\mathcal{w}_e = \frac{1}{2}\epsilon E^2$ (J/m³)
- Magnetic: $\mathcal{w}_m = \frac{1}{2}\mu H^2$ (J/m³)

**Poynting's theorem (global form) / 坡印廷定理（全局形式）:**

$$
P_s = P_e + P_d + \frac{d}{dt}(W_e + W_m)
\tag{1.6.14}
$$

其中：
- $P_s = -\iiint_V (\mathbf{E} \cdot \mathbf{J}_i + \mathbf{H} \cdot \mathbf{M}_i) \, dV$ — 供给功率
- $P_e = \oint_S (\mathbf{E} \times \mathbf{H}) \cdot \hat{n} \, dS$ — 流出的功率
- $P_d = \iiint_V \sigma E^2 \, dV$ — 耗散功率
- $W_e = \frac{1}{2}\iiint_V \epsilon E^2 \, dV$ — 电场储能
- $W_m = \frac{1}{2}\iiint_V \mu H^2 \, dV$ — 磁场储能

这是电磁场中的能量守恒定律——理解功率流、耗散和无功功率的基石。

---

## 1.7 Time-Harmonic Fields | 时谐场

### 1.7.1 Phasor Representation | 相量表示

For time-harmonic fields at angular frequency $\omega$ / 对于角频率 $\omega$ 的时谐场：

$$
\mathbf{E}(\mathbf{r}, t) = \text{Re}[\mathbf{E}(\mathbf{r}) e^{j\omega t}]
\tag{1.7.4}
$$

**Replacement rule / 替换规则:** $\partial/\partial t \to j\omega$

**Maxwell's equations in phasor form / 麦克斯韦方程组相量形式:**

$$
\nabla \times \mathbf{E} = -j\omega\mathbf{B} - \mathbf{M}_f
\tag{1.7.6}
$$

$$
\nabla \times \mathbf{H} = j\omega\mathbf{D} + \mathbf{J}_f
\tag{1.7.7}
$$

$$
\nabla \cdot \mathbf{D} = \varrho_{e,f}
\tag{1.7.8}
$$

$$
\nabla \cdot \mathbf{B} = \varrho_{m,f}
\tag{1.7.9}
$$

$$
\nabla \cdot \mathbf{J}_f = -j\omega\varrho_{e,f}
\tag{1.7.10}
$$

$$
\nabla \cdot \mathbf{M}_f = -j\omega\varrho_{m,f}
\tag{1.7.11}
$$

### 1.7.2 Fourier Transforms | 傅里叶变换

An arbitrary time-domain field can be represented as / 任意时域场可表示为：

$$
\mathbf{E}(\mathbf{r}, t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \mathbf{E}(\mathbf{r}, \omega) e^{j\omega t} \, d\omega
\tag{1.7.14}
$$

Fourier-transformed Maxwell's equations are identical to the phasor form, with $\omega$ now as a continuous variable / 傅里叶变换后的麦克斯韦方程组与相量形式完全相同，此时 $\omega$ 是连续变量。

### 1.7.3 Complex Power | 复功率

**Time-average of product of two phasors / 两个相量乘积的时间平均:**

$$
\overline{\mathbf{A}(t) \circ \mathbf{B}(t)} = \frac{1}{2}\text{Re}[\mathbf{A} \circ \mathbf{B}^*]
\tag{1.7.22}
$$

**Complex Poynting vector / 复坡印廷矢量:**

$$
\mathbf{S} = \frac{1}{2} \mathbf{E} \times \mathbf{H}^*
\tag{1.7.24}
$$

**Time-average Poynting vector / 时间平均坡印廷矢量:** $\overline{\mathbf{S}} = \text{Re}(\mathbf{S})$

**Time-average energy densities / 时间平均能量密度:**
- Electric: $w_e = \frac{1}{4}\epsilon|\mathbf{E}|^2$
- Magnetic: $w_m = \frac{1}{4}\mu|\mathbf{H}|^2$

**Poynting's theorem for complex phasors (differential form) / 复相量坡印廷定理（微分形式）:**

$$
p_s = p_e + p_d + j2\omega(w_m - w_e)
\tag{1.7.39}
$$

**Integral form / 积分形式:**

$$
P_s = P_e + P_d + j2\omega(W_m - W_e)
\tag{1.7.40}
$$

- $\text{Re}(P_s) = \text{Re}(P_e) + P_d$ — 有功功率平衡
- $\text{Im}(P_s) = \text{Im}(P_e) + 2\omega(W_m - W_e)$ — 无功功率平衡

实部给出时间平均功率平衡；虚部与电场和磁场储能之差相关（无功功率）。

### 1.7.4 Complex Permittivity and Permeability | 复介电常数和复磁导率

**Complex constitutive parameters / 复本构参数:**

$$
\epsilon_r = \epsilon'_r - j\epsilon''_r, \quad \mu_r = \mu'_r - j\mu''_r
\tag{1.7.56}
$$

虚部代表损耗——$\epsilon''_r > 0$ 表示介质损耗，$\mu''_r > 0$ 表示磁损耗。

**Loss tangents / 损耗角正切:**

$$
\tan\delta_e = \frac{\epsilon''_r}{\epsilon'_r}, \quad \tan\delta_m = \frac{\mu''_r}{\mu'_r}
\tag{1.7.57}
$$

**Kramers–Krönig relations (causality condition) / 克拉默斯–克勒尼希关系（因果性条件）:**

$$
\epsilon'(\omega) = \epsilon_\infty + \frac{2}{\pi} \mathcal{P}\!\!\int_{0}^{\infty} \frac{z\epsilon''(z)}{z^2 - \omega^2} \, dz
$$
$$
\epsilon''(\omega) = -\frac{2\omega}{\pi} \mathcal{P}\!\!\int_{0}^{\infty} \frac{\epsilon'(z) - \epsilon_\infty}{z^2 - \omega^2} \, dz
\tag{1.7.58}
$$

因果关系强制要求色散和损耗相关联——因果媒质不能只有其一而无其二。

**Combined conduction and dielectric loss / 合并的电导和介质损耗:**

$$
\nabla \times \mathbf{H} = j\omega\epsilon_0\left[\epsilon'_r - j\left(\epsilon''_r + \frac{\sigma}{\omega\epsilon_0}\right)\right] \mathbf{E} + \mathbf{J}_i
\tag{1.7.59}
$$

**Effective loss tangent / 等效损耗角正切:**

$$
\tan\delta_e = \frac{\epsilon''_r}{\epsilon'_r} + \frac{\sigma}{\omega\epsilon'_r\epsilon_0}
\tag{1.7.60}
$$

---

## Examples | 例题

### Example 1.1 — Generalized Gauss' Theorem Application | 广义高斯定理应用
Derive $\iiint_V (\mathbf{b}\nabla\cdot\mathbf{a} + \mathbf{a}\cdot\nabla\mathbf{b}) \, dV = \oint_S (\hat{n}\cdot\mathbf{a})\mathbf{b} \, dS$ from the generalized Gauss' theorem.
从广义高斯定理推导该体积分与面积分关系。

### Example 1.2 — Derivation of Scalar–Vector Green's Theorem | 标量–矢量格林定理推导
From the second vector Green's theorem with $\mathbf{b} = \hat{b}b$, derive the scalar–vector Green's theorem.
从第二矢量格林定理推导标量–矢量格林定理。

### Example 1.3 — Kirchhoff's Voltage Law from Faraday's Law | 从法拉第定律推导基尔霍夫电压定律
Applying $\oint \mathbf{E} \cdot d\mathbf{l} = -d/dt \iint \mathbf{B} \cdot d\mathbf{S}$ to an RLC circuit yields $\sum_{i=1}^{N} V_i = 0$.
将法拉第定律应用于RLC电路得到基尔霍夫电压定律。

### Example 1.4 — Kirchhoff's Current Law from Continuity | 从连续性方程推导基尔霍夫电流定律
Applying $\oint_S \mathbf{J} \cdot d\mathbf{S} = -d/dt \iiint \varrho \, dV$ to a circuit node yields $\sum_{i=1}^{N} I_i = 0$.
将连续性方程应用于电路节点得到基尔霍夫电流定律。

### Example 1.5 — Boundary Conditions for Total vs Free Quantities | 总电荷量与自由电荷量的边界条件
磁化产生面电流 $\mathbf{J}_{m,s} = -\hat{n} \times \mathbf{M}$，极化产生束缚面电荷 $\varrho_{e,s,b} = \hat{n} \cdot \mathbf{P}$。

### Example 1.6 — Lorentz Model of Dielectric Permittivity | 介电常数的洛伦兹模型
For a classical electron oscillator model / 经典电子振子模型：
$$
\epsilon_r(\omega) = 1 + \frac{N_e q_e^2}{\epsilon_0 m_e(\omega_0^2 - \omega^2 + j\omega\delta)}
$$

### Example 1.7 — Power Dissipation in a Slotted Metallic Box | 开槽金属盒中的功率耗散
时均耗散功率: $P_d = \sqrt{3} w l E_0^2 / (8\eta)$
能量差: $W_e - W_m = w l E_0^2 / (16\omega\eta)$

### Example 1.8 — Drude Model of Plasma Permittivity | 等离子体介电常数的德鲁德模型
$$
\epsilon_{\text{eff}} = \epsilon_0 + \frac{\epsilon_0\omega_p^2}{j\omega(\nu + j\omega)}, \quad \omega_p = \sqrt{\frac{N_e q_e^2}{\epsilon_0 m_e}}
$$

### Example 1.9 — Kramers–Krönig Relations | 克拉默斯–克勒尼希关系
通过对复极化率的柯西积分定理证明。

---

## Problems (Ch1, 25 problems) | 习题（第1章，25题）

| # | Topic / 主题 |
|---|---|
| 1.1–1.3 | 散度、旋度、梯度的定义推导 |
| 1.4–1.5 | $\nabla(1/R)$ 和 $\nabla^2(1/R)$ — 狄拉克$\delta$函数 |
| 1.6–1.7 | 通过符号矢量法推导矢量恒等式 |
| 1.8 | 无限薄表面上的格林定理 |
| 1.9 | 亥姆霍兹分解定理证明 |
| 1.10 | 导电柱的电阻 |
| 1.11–1.12 | 静电场和静磁场边值问题 |
| 1.13–1.14 | 含介质板的电容器——力 |
| 1.15 | 柱对称电荷分布——场和面电荷 |
| 1.16 | 平行板波导——场和电流 |
| 1.17 | 总电荷与自由电荷表述的等价性 |
| 1.18 | 从微分方程+边界条件回到积分形式 |
| 1.19 | 薄电阻片的边界条件 |
| 1.20 | 洛伦兹和德鲁德模型的时域极化率 |
| 1.21–1.24 | 波导功率耗散问题 |
| 1.25 | 洛伦兹和德鲁德模型的克拉默斯–克勒尼希关系 |
