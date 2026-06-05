---
title: "Chapter 2 — Electromagnetic Radiation in Free Space"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Scalar & vector potentials (static and time-harmonic)
  - Lorenz gauge condition
  - Free-space Green's function
  - Dyadic Green's functions
  - Hertzian dipole radiation
  - Far-field approximation, directivity, radiation resistance
  - Finite dipole, current loop, surface current, phased arrays
  - Sommerfeld radiation condition
---

# Chapter 2: Electromagnetic Radiation in Free Space
> **中英双语版**

> 自由空间中的电磁辐射

## 2.1 Scalar and Vector Potentials
> 标量和矢量势

### 2.1.1 Static Fields / 静态场

**Electrostatics / 静电场：**
$$\mathbf{E} = -\nabla \varphi, \quad \nabla^2 \varphi = -\frac{\varrho_e}{\epsilon}$$

**Magnetostatics / 静磁场：**
$$\mathbf{B} = \nabla \times \mathbf{A}, \quad \nabla^2 \mathbf{A} = -\mu \mathbf{J}$$

**Coulomb gauge / 库仑规范：** $\nabla \cdot \mathbf{A} = 0$

### 2.1.2 Time-Harmonic Fields and Lorenz Gauge
> 时谐场与 Lorenz 规范

**Magnetic vector potential / 磁矢量势：**
$$\mathbf{B}_e = \nabla \times \mathbf{A}, \quad \mathbf{E}_e = -j\omega\mathbf{A} + \frac{1}{j\omega\mu\epsilon} \nabla(\nabla \cdot \mathbf{A})$$

**Lorenz gauge / Lorenz 规范：**
$$\nabla \cdot \mathbf{A} = -j\omega\mu\epsilon \varphi$$

**Electric vector potential / 电矢量势：**
$$\mathbf{D}_m = -\nabla \times \mathbf{F}, \quad \mathbf{H}_m = -j\omega\mathbf{F} + \frac{1}{j\omega\mu\epsilon} \nabla(\nabla \cdot \mathbf{F})$$

**Total field / 总场：**
$$\mathbf{E} = -j\omega\mathbf{A} + \frac{1}{j\omega\mu\epsilon} \nabla(\nabla \cdot \mathbf{A}) - \frac{1}{\epsilon} \nabla \times \mathbf{F}$$
$$\mathbf{H} = \frac{1}{\mu} \nabla \times \mathbf{A} - j\omega\mathbf{F} + \frac{1}{j\omega\mu\epsilon} \nabla(\nabla \cdot \mathbf{F})$$

---

## 2.2 Solution of Vector Potentials in Free Space
> 自由空间中矢量势的解

**Free-space scalar Green's function / 自由空间标量格林函数：**
$$G_0(\mathbf{r}, \mathbf{r}') = \frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{4\pi |\mathbf{r} - \mathbf{r}'|}$$

**Field–Source Relations / 场源关系：**
$$\mathbf{A}(\mathbf{r}) = \frac{\mu}{4\pi} \iiint_V \mathbf{J}(\mathbf{r}') \frac{e^{-jkR}}{R} dV'$$
$$\mathbf{F}(\mathbf{r}) = \frac{\epsilon}{4\pi} \iiint_V \mathbf{M}(\mathbf{r}') \frac{e^{-jkR}}{R} dV'$$

**Dyadic Green's Functions / 并矢格林函数：**
$$\overline{\mathbf{G}}_{e0}(\mathbf{r}, \mathbf{r}') = \left( \overline{\mathbf{I}} + \frac{1}{k^2} \nabla\nabla \right) G_0(\mathbf{r}, \mathbf{r}')$$
$$\overline{\mathbf{G}}_{m0}(\mathbf{r}, \mathbf{r}') = \nabla G_0(\mathbf{r}, \mathbf{r}') \times \overline{\mathbf{I}}$$

---

## 2.3 Electromagnetic Radiation in Free Space
> 自由空间中的电磁辐射

### Hertzian Dipole / 赫兹偶极子

**Vector potential / 矢量势：**
$$\mathbf{A}(\mathbf{r}) = \hat{z} \frac{\mu I l}{4\pi r} e^{-jkr}$$

**Far-field / 远场：**
$$E_\theta \approx \frac{jk\eta Il \sin\theta}{4\pi r} e^{-jkr}, \quad H_\phi \approx \frac{jk Il \sin\theta}{4\pi r} e^{-jkr}$$

**Directivity / 方向性系数：** $D_0 = 1.5$
**Radiation resistance / 辐射电阻：** $R_r = 80\pi^2 (l/\lambda)^2$

### Finite Dipole / 有限长偶极子

**Half-wave dipole / 半波偶极子：** directivity $D_0 \approx 1.64$, $R_{\text{in}} \approx 73~\Omega$。

## Key Physical Intuition / 关键物理直觉

1. **The Lorenz gauge** decouples $\mathbf{A}$ and $\varphi$, yielding two independent Helmholtz equations.
   > Lorenz 规范解耦了 $\mathbf{A}$ 和 $\varphi$，得到两个独立的 Helmholtz 方程。
2. **$G_0 = e^{-jkR}/(4\pi R)$ represents an outgoing spherical wave** — the building block for any source distribution.
   > 代表出射球面波——任何源分布的基本构建块。
3. **The Hertzian dipole is the elementary radiator.** Any antenna can be modeled as a superposition of infinitesimal dipoles.
   > 赫兹偶极子是基本辐射元。任何天线可建模为无穷小偶极子的叠加。
