---
chapter: 3
title: Some Theorems and Concepts
source: Roger F. Harrington, Time-Harmonic Electromagnetic Fields, IEEE Press
pages: 95-180
---

# Chapter 3: Some Theorems and Concepts / 一些定理与概念

## Section 3-1: The Source Concept / 源的概念

**English:**

The complex field equations for linear media are:

$$\nabla \times \mathbf{E} = -j\omega\mu\mathbf{H} - \mathbf{M}$$
$$\nabla \times \mathbf{H} = j\omega\epsilon\mathbf{E} + \mathbf{J} \tag{3-1}$$

where $\mathbf{J}$ and $\mathbf{M}$ are **sources** in the most general sense. $\mathbf{J}$ is the **electric current density** (A/m²) and $\mathbf{M}$ is the **magnetic current density** (V/m²) — a mathematical construct that represents magnetic current sources.

$\mathbf{J}$ and $\mathbf{M}$ can represent:
- **Impressed (actual) currents** — physical sources
- **Conduction currents** kept separate from $\sigma\mathbf{E}$ term
- **Magnetic polarization currents** kept separate from $j\omega\mu\mathbf{H}$ term

**Circuit sources in field form:**
- **Current source:** A short filament of impressed electric current $\mathbf{J}_i$ in series with a perfectly conducting wire. The current equals $\mathbf{J}_i$ independent of load (displacement current negligible in surrounding medium).
- **Voltage source:** A small loop of impressed magnetic current $\mathbf{M}_i$ around a gap in a conducting wire.

**Power in terms of sources:**
$$P = -\frac{1}{2}\int_V \mathbf{E} \cdot \mathbf{J}_i^* \, dV - \frac{1}{2}\int_V \mathbf{H} \cdot \mathbf{M}_i^* \, dV \tag{3-5}$$

**Internal impedance of current source:** Infinite (open circuit in field terms).
**Internal impedance of voltage source:** Zero (short circuit in field terms).

**中文：**

线性介质的复场方程为：

$$\nabla \times \mathbf{E} = -j\omega\mu\mathbf{H} - \mathbf{M}$$
$$\nabla \times \mathbf{H} = j\omega\epsilon\mathbf{E} + \mathbf{J} \tag{3-1}$$

其中 $\mathbf{J}$ 和 $\mathbf{M}$ 是最广义的**源**。$\mathbf{J}$ 是**电流密度** (A/m²)，$\mathbf{M}$ 是**磁流密度** (V/m²) —— 一种表示磁流的数学构造。

$\mathbf{J}$ 和 $\mathbf{M}$ 可以表示：
- **外加（实际）电流** — 物理源
- 与 $\sigma\mathbf{E}$ 项分开考虑的**传导电流**
- 与 $j\omega\mu\mathbf{H}$ 项分开考虑的**磁极化电流**

**场形式的电路源：**
- **电流源：** 与完美导电导线串联的短细外加电流丝 $\mathbf{J}_i$。
- **电压源：** 围绕导线间隙的小外加磁流回路 $\mathbf{M}_i$。

---

## Section 3-2: Duality / 对偶性

**English:**

**Duality** is a fundamental symmetry in electromagnetic theory where electric and magnetic quantities play interchangeable roles.

**Maxwell's equations (no sources):**
$$\nabla \times \mathbf{E} = -j\omega\mu\mathbf{H} \quad \Leftrightarrow \quad \nabla \times \mathbf{H} = j\omega\epsilon\mathbf{E}$$

**Duality transformations:**
| Electric Quantity | Magnetic Quantity |
|------------------|------------------|
| $\mathbf{E}$ (electric field) | $\mathbf{H}$ (magnetic field) |
| $\mathbf{H}$ (magnetic field) | $-\mathbf{E}$ (electric field) |
| $\mathbf{J}$ (electric current) | $\mathbf{M}$ (magnetic current) |
| $\epsilon$ (permittivity) | $\mu$ (permeability) |
| $\mu$ (permeability) | $\epsilon$ (permittivity) |
| $q_v$ (electric charge) | $q_m$ (magnetic charge) |

**Duality principle:** If a solution exists for a problem with $(\mathbf{E}, \mathbf{H}, \mathbf{J}, \epsilon, \mu)$, then a dual solution exists for the problem with $(\mathbf{H}, -\mathbf{E}, \mathbf{M}, \mu, \epsilon)$.

**Applications of duality:**
- Wire antenna ↔ Magnetic dipole antenna
- Electric conduction ↔ Magnetic conduction
- Electric circuit theorems ↔ Magnetic circuit theorems

**Perfect electric conductor (PEC):** Boundary condition $\hat{n} \times \mathbf{E} = 0$
**Perfect magnetic conductor (PMC):** Boundary condition $\hat{n} \times \mathbf{H} = 0$

**中文：**

**对偶性**是电磁理论中的基本对称性，电和磁量在其中可以互换角色。

**麦克斯韦方程（无源）：**
$$\nabla \times \mathbf{E} = -j\omega\mu\mathbf{H} \quad \Leftrightarrow \quad \nabla \times \mathbf{H} = j\omega\epsilon\mathbf{E}$$

**对偶变换：**
| 电量 | 磁量 |
|------|------|
| $\mathbf{E}$（电场） | $\mathbf{H}$（磁场） |
| $\mathbf{H}$（磁场） | $-\mathbf{E}$（电场） |
| $\mathbf{J}$（电流） | $\mathbf{M}$（磁流） |
| $\epsilon$（介电常数） | $\mu$（磁导率） |
| $\mu$（磁导率） | $\epsilon$（介电常数） |

---

## Section 3-3: Uniqueness / 唯一性定理

**English:**

The **uniqueness theorem** states that the field in a region is uniquely determined by:
1. Sources within the region, AND
2. Boundary values of tangential $\mathbf{E}$ OR tangential $\mathbf{H}$ on the enclosing surface.

**Proof sketch:** Assume two different fields $\mathbf{E}_1, \mathbf{H}_1$ and $\mathbf{E}_2, \mathbf{H}_2$ both satisfy Maxwell's equations with same sources and same boundary conditions. Let $\mathbf{E}_d = \mathbf{E}_1 - \mathbf{E}_2$, $\mathbf{H}_d = \mathbf{H}_1 - \mathbf{H}_2$. Then the difference fields satisfy source-free Maxwell's equations and have zero tangential components on the boundary.

Using Poynting's theorem for the difference fields:
$$\nabla \cdot (\mathbf{E}_d \times \mathbf{H}_d^*) = -j\omega(\mu|\mathbf{H}_d|^2 - \epsilon|\mathbf{E}_d|^2)$$

Integrating over volume and using divergence theorem:
$$0 = -j\omega\int_V(\mu|\mathbf{H}_d|^2 - \epsilon|\mathbf{E}_d|^2)\, dV$$

This requires $|\mathbf{E}_d| = |\mathbf{H}_d| = 0$ in the volume, proving uniqueness.

**Implications:**
- We can solve boundary value problems uniquely if we specify either $\hat{n} \times \mathbf{E}$ or $\hat{n} \times \mathbf{H}$ on all boundaries.
- This is the basis for **finite element method (FEM)** and **finite difference time domain (FDTD)** numerical methods.

**中文：**

**唯一性定理**指出，区域中的场由以下条件唯一确定：
1. 区域内的源，AND
2. 包围表面上切向 $\mathbf{E}$ 或切向 $\mathbf{H}$ 的边界值。

**意义：**
- 如果我们指定边界上全部的 $\hat{n} \times \mathbf{E}$ 或 $\hat{n} \times \mathbf{H}$，就可以唯一地求解边值问题。
- 这是**有限元法（FEM）**和**时域有限差分法（FDTD）**数值方法的基础。

---

## Section 3-5: The Equivalence Principle / 等效原理

**English:**

The **equivalence principle** allows us to replace actual sources with equivalent sources on a surface enclosing the original source region.

**Surface equivalence theorem:**

1. **Original problem:** Actual sources $\mathbf{J}, \mathbf{M}$ in presence of objects produce fields $\mathbf{E}, \mathbf{H}$.

2. **Equivalent problem:** Remove original sources, keep the same objects, but place equivalent surface currents on an imaginary surface $S$ enclosing the original source region:
$$\mathbf{J}_s = \hat{n} \times \mathbf{H} \quad \text{(equivalent electric surface current)}$$
$$\mathbf{M}_s = -\hat{n} \times \mathbf{E} \quad \text{(equivalent magnetic surface current)}$$

The fields outside $S$ are identical to the original problem. Inside $S$, fields may differ (they are "equivalent" outside only).

**Applications:**
- **Method of Moments (MoM):** Replace wire antennas with equivalent surface currents on wire surface.
- **Physical optics (PO):** Approximate currents on illuminated surfaces as $\mathbf{J}_s \approx 2\hat{n} \times \mathbf{H}^i$.
- **Aperture radiation:** Replace aperture with equivalent magnetic current $\mathbf{M}_s = -2\hat{n} \times \mathbf{E}^\text{inc}$ on the aperture plane.

**Love's equivalence:** For external scattering problems, place PEC behind the surface to terminate interior fields, keeping only exterior equivalent currents.

**中文：**

**等效原理**允许我们将实际源替换为包围原始源区域的表面上上的等效源。

**表面等效定理：**

1. **原始问题：** 实际源 $\mathbf{J}, \mathbf{M}$ 在物体存在时产生场 $\mathbf{E}, \mathbf{H}$。

2. **等效问题：** 移除原始源，保留相同物体，但在包围原始源区域的假想表面 $S$ 上放置等效表面电流：
$$\mathbf{J}_s = \hat{n} \times \mathbf{H} \quad \text{（等效电表面电流）}$$
$$\mathbf{M}_s = -\hat{n} \times \mathbf{E} \quad \text{（等效磁表面电流）}$$

$S$ 外部的场与原始问题相同。$S$ 内部，场可能不同（仅在外部"等效"）。

---

## Section 3-6: Fields in Half-space / 半空间中的场

**English:**

Consider a **half-space** ($z > 0$) with fields generated by sources in the other half ($z < 0$). This is a canonical problem for antenna radiation and scattering.

**Sommerfeld radiation condition (索末菲辐射条件):** For large $r$:
$$\lim_{r \to \infty} r\left(\frac{\partial \psi}{\partial r} + jk\psi\right) = 0$$

This ensures outgoing spherical waves (energy radiating to infinity), not incoming waves.

**Half-space Green's function:** The field at $\mathbf{r}$ due to a point source at $\mathbf{r}'$ in half-space:
$$G(\mathbf{r}, \mathbf{r}') = \frac{e^{-jkr}}{4\pi r} \quad \text{for } z, z' > 0 \text{ and } r \to \infty$$

For a source below the interface and field above:
$$G = \frac{e^{-jkr}}{4\pi r} + \frac{e^{-jkR_1}}{4\pi R_1} \quad \text{(image method)}$$

where $R_1 = \sqrt{(x-x')^2 + (y-y')^2 + (z+z')^2}$ is the distance to the image source.

**Layered media:** For $N$ layers, use transfer matrix method or recursive algorithm (complex but systematic).

**中文：**

考虑**半空间** ($z > 0$) 中的场，由另一半空间 ($z < 0$) 中的源产生。

**索末菲辐射条件：** 对于大的 $r$：
$$\lim_{r \to \infty} r\left(\frac{\partial \psi}{\partial r} + jk\psi\right) = 0$$

这确保是外向球面波（能量辐射到无穷远），而非入射波。

**半空间格林函数：** $\mathbf{r}$ 处点源在 $\mathbf{r}'$ 产生的场：
$$G(\mathbf{r}, \mathbf{r}') = \frac{e^{-jkr}}{4\pi r} \quad \text{（对于 } z, z' > 0 \text{ 和 } r \to \infty \text{）}$$

---

## Section 3-7: The Induction Theorem / 感应定理

**English:**

The **induction theorem** relates the scattered field to the field that would exist if the scatterer were removed.

**Statement:** The scattered field $\mathbf{E}^s, \mathbf{H}^s$ due to an object illuminated by incident field $\mathbf{E}^i, \mathbf{H}^i$ equals the field produced by **equivalent currents** on the object's surface:
$$\mathbf{J}_s = \hat{n} \times (\mathbf{E}^i + \mathbf{E}^s) = \hat{n} \times \mathbf{E}^\text{total}$$
$$\mathbf{M}_s = -\hat{n} \times (\mathbf{H}^i + \mathbf{H}^s) = -\hat{n} \times \mathbf{H}^\text{total}$$

This is essentially the equivalence principle applied to the object surface.

**Optical theorem (光学定理):** Relates forward scattering amplitude to total extinction cross-section:
$$\sigma_\text{ext} = \frac{4\pi}{k}\text{Im}\{f(0)\}$$

where $f(0)$ is the forward scattering amplitude.

**Applications:**
- Radar cross section (RCS) calculations
- Absorption and scattering cross sections
- Inverse scattering problems

**中文：**

**感应定理**将散射场与移除散射体后存在的场联系起来。

**表述：** 物体被入射场 $\mathbf{E}^i, \mathbf{H}^i$ 照射时的散射场 $\mathbf{E}^s, \mathbf{H}^s$ 等于物体表面上**等效电流**产生的场：
$$\mathbf{J}_s = \hat{n} \times \mathbf{E}^\text{total}$$
$$\mathbf{M}_s = -\hat{n} \times \mathbf{H}^\text{total}$$

---

## Section 3-8: Reciprocity / 互易性

**English:**

**Reciprocity theorems** express symmetry relationships between source and field configurations.

**Lorentz reciprocity theorem (洛伦兹互易定理):**

For two sets of sources $(\mathbf{J}_a, \mathbf{M}_a)$ producing fields $(\mathbf{E}_a, \mathbf{H}_a)$ and another set $(\mathbf{J}_b, \mathbf{M}_b)$ producing fields $(\mathbf{E}_b, \mathbf{H}_b)$ in the same linear medium:

$$\int_V (\mathbf{E}_a \cdot \mathbf{J}_b - \mathbf{H}_a \cdot \mathbf{M}_b)\, dV = \int_V (\mathbf{E}_b \cdot \mathbf{J}_a - \mathbf{H}_b \cdot \mathbf{M}_a)\, dV \tag{3-43}$$

This is the most general form of reciprocity in electromagnetics.

**Reaction (反应):** Define the **reaction** of field $a$ with source $b$:
$$\langle a, b \rangle = \int_V (\mathbf{E}_a \cdot \mathbf{J}_b - \mathbf{H}_a \cdot \mathbf{M}_b)\, dV$$

Reciprocity states: $\langle a, b \rangle = \langle b, a \rangle$.

**Implications:**
- Antenna transmit and receive patterns are identical (reciprocal antennas).
- S-parameters are symmetric: $S_{ij} = S_{ji}$ (for passive, linear, time-invariant media).
- Scattering matrix is symmetric for reciprocal media.

**Time-reversal reciprocity:** For lossless media, fields are also symmetric under time-reversal.

**中文：**

**互易定理**表达源与场配置之间的对称关系。

**洛伦兹互易定理：** 对于两套源 $(\mathbf{J}_a, \mathbf{M}_a)$ 和 $(\mathbf{J}_b, \mathbf{M}_b)$ 在同一线性介质中分别产生场 $(\mathbf{E}_a, \mathbf{H}_a)$ 和 $(\mathbf{E}_b, \mathbf{H}_b)$：

$$\int_V (\mathbf{E}_a \cdot \mathbf{J}_b - \mathbf{H}_a \cdot \mathbf{M}_b)\, dV = \int_V (\mathbf{E}_b \cdot \mathbf{J}_a - \mathbf{H}_b \cdot \mathbf{M}_a)\, dV \tag{3-43}$$

**反应（Reaction）：** 定义场 $a$ 与源 $b$ 的**反应**：
$$\langle a, b \rangle = \int_V (\mathbf{E}_a \cdot \mathbf{J}_b - \mathbf{H}_a \cdot \mathbf{M}_b)\, dV$$

互易性表明：$\langle a, b \rangle = \langle b, a \rangle$。

---

## Section 3-10: Tensor Green's Functions / 张量格林函数

**English:**

The **Green's function** for vector fields relates the field at $\mathbf{r}$ to sources at $\mathbf{r}'$.

**Scalar Green's function:** Solution to
$$\nabla^2 G + k^2 G = -\delta(\mathbf{r} - \mathbf{r}')$$

In free space:
$$G(\mathbf{r}, \mathbf{r}') = \frac{e^{-jkR}}{4\pi R}, \quad R = |\mathbf{r} - \mathbf{r}'|$$

**Vector Green's function (并矢格林函数):**

$$\mathbf{G}(\mathbf{r}, \mathbf{r}') = \left(\mathbf{I} + \frac{\nabla\nabla}{k^2}\right)\frac{e^{-jkR}}{4\pi R} \tag{3-69}$$

The electric field due to current distribution $\mathbf{J}(\mathbf{r}')$:

$$\mathbf{E}(\mathbf{r}) = -j\omega\mu\int_V \mathbf{G}(\mathbf{r}, \mathbf{r}')\cdot \mathbf{J}(\mathbf{r}')\, dV'$$

The dyadic Green's function satisfies:
$$(\nabla \times \nabla \times - k^2)\mathbf{G} = \mathbf{I}\delta(\mathbf{r} - \mathbf{r}')$$

**Tensor form for anisotropic media:** $\mathbf{G}$ becomes a $3 \times 3$ tensor when medium is anisotropic ($\epsilon$ and $\mu$ are tensors).

**中文：**

**格林函数**将 $\mathbf{r}$ 处的场与 $\mathbf{r}'$ 处的源联系起来。

**标量格林函数：** 以下方程的解
$$\nabla^2 G + k^2 G = -\delta(\mathbf{r} - \mathbf{r}')$$

在自由空间中：
$$G(\mathbf{r}, \mathbf{r}') = \frac{e^{-jkR}}{4\pi R}, \quad R = |\mathbf{r} - \mathbf{r}'|$$

**矢量格林函数（并矢形式）：**

$$\mathbf{G}(\mathbf{r}, \mathbf{r}') = \left(\mathbf{I} + \frac{\nabla\nabla}{k^2}\right)\frac{e^{-jkR}}{4\pi R} \tag{3-69}$$

电流分布 $\mathbf{J}(\mathbf{r}')$ 产生的电场：
$$\mathbf{E}(\mathbf{r}) = -j\omega\mu\int_V \mathbf{G}(\mathbf{r}, \mathbf{r}')\cdot \mathbf{J}(\mathbf{r}')\, dV'$$

---

## Section 3-11: Integral Equations / 积分方程

**English:**

**Integral equations** arise when we express unknowns (currents, fields) as integrals over unknowns themselves.

**Electric field integral equation (EFIE):** For perfect conductors:
$$\mathbf{E}^\text{inc}(\mathbf{r}) = \frac{j}{\omega\epsilon}\nabla \times \int_S \mathbf{J}_s(\mathbf{r}')\frac{e^{-jkR}}{4\pi R}\, dS' \tag{3-72}$$

Unknown: surface current $\mathbf{J}_s$ on conductor.
Kernel: Green's function convolution.

**Magnetic field integral equation (MFIE):**
$$\mathbf{H}^\text{inc}(\mathbf{r}) = \hat{n} \times \int_S \mathbf{J}_s(\mathbf{r}')\frac{e^{-jkR}}{4\pi R}\, dS' \tag{3-73}$$

**Pocklington's equation (for wires):** Electric field along wire axis due to current distribution:
$$\mathbf{E}^\text{inc}_z = \frac{j}{\omega\epsilon}\int_{-L/2}^{L/2} I(z')\left(\frac{\partial^2}{\partial z^2} + k^2\right)\frac{e^{-jkR}}{4\pi R}\, dz' \tag{3-76}$$

**Solution by Method of Moments (MoM):** Discretize the integral equation into a matrix equation:
$$[Z]\{I\} = \{V\}$$

where $[Z]$ is the **impedance matrix**, $\{I\}$ is the unknown current coefficients, and $\{V\}$ is the **excitation vector**.

**Conditioning:** MoM matrices for electromagnetic problems are typically dense and ill-conditioned, requiring specialized solvers.

**中文：**

**积分方程**源于将未知量（电流、场）表示为对未知量本身的积分。

**电场积分方程（EFIE）：** 对于完美导体：
$$\mathbf{E}^\text{inc}(\mathbf{r}) = \frac{j}{\omega\epsilon}\nabla \times \int_S \mathbf{J}_s(\mathbf{r}')\frac{e^{-jkR}}{4\pi R}\, dS' \tag{3-72}$$

未知量：导体上的表面电流 $\mathbf{J}_s$。
核：格林函数卷积。

**用矩量法（MoM）求解：** 将积分方程离散化为矩阵方程：
$$[Z]\{I\} = \{V\}$$

其中 $[Z]$ 是**阻抗矩阵**，$\{I\}$ 是未知电流系数，$\{V\}$ 是**激励向量**。

---

## Section 3-12: Construction of Solutions / 解的构造

**English:**

**General solution construction** for electromagnetic fields involves:
1. Finding scalar wave function solutions $\psi$ to Helmholtz equation
2. Using vector potential formulations to construct EM fields

**Vector potential approach:**

For source-free regions, define magnetic vector potential $\mathbf{A}$:
$$\mathbf{B} = \nabla \times \mathbf{A}$$

Using Coulomb gauge ($\nabla \cdot \mathbf{A} = 0$):
$$\nabla^2 \mathbf{A} + k^2 \mathbf{A} = 0 \quad \Rightarrow \quad \mathbf{A}(\mathbf{r}) = \frac{1}{4\pi}\int_V \mathbf{J}(\mathbf{r}')\frac{e^{-jkR}}{R}\, dV'$$

Then:
$$\mathbf{E} = -j\omega\mathbf{A} - \frac{j}{\omega\mu\epsilon}\nabla(\nabla \cdot \mathbf{A})$$
$$\mathbf{H} = \frac{1}{\mu}\nabla \times \mathbf{A}$$

**Separation of variables solutions:**

In rectangular coordinates $(x, y, z)$:
$$\psi(x,y,z) = X(x)Y(y)Z(z)$$

Leads to:
$$\frac{1}{X}\frac{d^2X}{dx^2} + \frac{1}{Y}\frac{d^2Y}{dy^2} + \frac{1}{Z}\frac{d^2Z}{dz^2} = -k^2$$

Set each term equal to constant $-k_x^2, -k_y^2, -k_z^2$ where $k_x^2 + k_y^2 + k_z^2 = k^2$.

**General solution in rectangular coordinates:**
$$\psi = (A_+ e^{-jk_x x} + A_- e^{jk_x x})(B_+ e^{-jk_y y} + B_- e^{jk_y y})(C_+ e^{-jk_z z} + C_- e^{jk_z z})$$

**中文：**

**一般解的构造**涉及：
1. 寻找标量波动函数 $\psi$ 解以满足亥姆霍兹方程
2. 使用矢量势公式来构造电磁场

**矢量势方法：**

对于无源区域，定义磁矢势 $\mathbf{A}$：
$$\mathbf{B} = \nabla \times \mathbf{A}$$

使用库仑规范 ($\nabla \cdot \mathbf{A} = 0$)：
$$\nabla^2 \mathbf{A} + k^2 \mathbf{A} = 0 \quad \Rightarrow \quad \mathbf{A}(\mathbf{r}) = \frac{1}{4\pi}\int_V \mathbf{J}(\mathbf{r}')\frac{e^{-jkR}}{R}\, dV'$$

---

## Section 3-13: The Radiation Field / 辐射场

**English:**

The **radiation field** is the field at large distances from a source, dominated by outward-propagating spherical waves.

**Far-field approximation ($r \gg D^2/\lambda$ where $D$ is the source dimension):**

$$R = |\mathbf{r} - \mathbf{r}'| \approx r - \hat{r} \cdot \mathbf{r}'$$

$$\frac{e^{-jkR}}{R} \approx \frac{e^{-jkr}}{r}e^{jk\hat{r} \cdot \mathbf{r}'}$$

**Radiated fields from current distribution:**

For electric current $\mathbf{J}(\mathbf{r}')$:
$$\mathbf{E}(\mathbf{r}) \approx \frac{j\omega\mu}{4\pi r}e^{-jkr}\int_V \mathbf{J}(\mathbf{r}')e^{jk\hat{r} \cdot \mathbf{r}'}\, dV' \times \hat{r}$$
$$\mathbf{H}(\mathbf{r}) \approx \frac{1}{\eta}\hat{r} \times \mathbf{E}(\mathbf{r})$$

The integral $\int_V \mathbf{J}(\mathbf{r}')e^{jk\hat{r} \cdot \mathbf{r}'}\, dV'$ is the **vector radiation pattern** (矢量辐射图).

**Radiation from apertures:** For aperture in infinite ground plane:
$$\mathbf{E}(\mathbf{r}) \approx -\frac{jk}{4\pi r}e^{-jkr}(\hat{\theta}\hat{\theta} + \hat{\phi}\hat{\phi})\cdot \int_S \mathbf{M}_s e^{jk\hat{r} \cdot \mathbf{r}'}\, dS'$$

where $\mathbf{M}_s = -2\hat{n} \times \mathbf{E}^\text{tan}$ on the aperture.

**Power pattern (功率图):**
$$U(\theta, \phi) = \frac{r^2}{2\eta}|\mathbf{E}|^2 \quad \text{W/steradian}$$

**Directivity:**
$$D(\theta, \phi) = \frac{4\pi U(\theta, \phi)}{P_\text{total}}$$

**Total radiated power:**
$$P_\text{rad} = \int_{4\pi} U(\theta, \phi)\, d\Omega$$

**中文：**

**辐射场**是远离源的区域中的场，以外向传播的球面波为主。

**远区近似（$r \gg D^2/\lambda$，其中 $D$ 是源尺寸）：**

$$\frac{e^{-jkR}}{R} \approx \frac{e^{-jkr}}{r}e^{jk\hat{r} \cdot \mathbf{r}'}$$

电流分布的辐射场：
$$\mathbf{E}(\mathbf{r}) \approx \frac{j\omega\mu}{4\pi r}e^{-jkr}\int_V \mathbf{J}(\mathbf{r}')e^{jk\hat{r} \cdot \mathbf{r}'}\, dV' \times \hat{r}$$

积分 $\int_V \mathbf{J}(\mathbf{r}')e^{jk\hat{r} \cdot \mathbf{r}'}\, dV'$ 是**矢量辐射图**。

---

