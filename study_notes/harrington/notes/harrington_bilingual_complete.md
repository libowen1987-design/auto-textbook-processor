# Time-Harmonic Electromagnetic Fields — Bilingual Edition

**Author:** Roger F. Harrington  
**Publisher:** IEEE Press (Classic Reissue)  
**Subject:** Electromagnetic Field Theory  

This bilingual (English/Chinese) version presents Harrington's classic text
with proper LaTeX notation, vector operators, and detailed Chinese annotations.

---

---
chapter: 1
title: Fundamental Concepts
source: Roger F. Harrington, Time-Harmonic Electromagnetic Fields, IEEE Press
pages: 1-60
---

# Chapter 1: Fundamental Concepts / 基本概念

## Section 1-1: Introduction / 引言

**English:**

The topic of this book is the theory and analysis of electromagnetic phenomena that vary sinusoidally in time, henceforth called **a-c (alternating-current) phenomena**. The fundamental concepts which form the basis of our study are presented in this chapter. It is assumed that the reader already has some acquaintance with electromagnetic field theory and with electric circuit theory.

We shall view electromagnetic phenomena from the **"macroscopic" standpoint** — that is, linear dimensions are large compared to atomic dimensions and charge magnitudes are large compared to atomic charges. This allows us to neglect the granular structure of matter and charge. We assume all matter to be stationary with respect to the observer. No treatment of the mechanical forces associated with the electromagnetic field is given.

The **rationalized mksc system of units** is used throughout. In this system:
- Unit of length: **meter** (m)
- Unit of mass: **kilogram** (kg)
- Unit of time: **second** (s)
- Unit of charge: **coulomb** (C)

The mksc system is particularly convenient because the electrical units are identical to those used in practice.

**中文：**

本书主题是正弦时变电磁现象的理论与分析，此后称之为**交流（a-c）现象**。我们研究所依据的基本概念将在本章中呈现。读者应已对电磁场理论和电路理论有所了解。

我们从**"宏观"角度**审视电磁现象——即线性尺寸远大于原子尺寸，电荷量远大于原子电荷。这使我们能够忽略物质和电荷的颗粒结构。假设所有物质相对于观察者均为静止。

全书采用**有理化mksc单位制**：
- 长度单位：**米**（m）
- 质量单位：**千克**（kg）
- 时间单位：**秒**（s）
- 电荷单位：**库仑**（C）

mksc系统特别方便，因为电气单位与实际使用的单位完全一致。

---

## Section 1-2: Basic Equations / 基本方程

**English:**

The electromagnetic field equations are expressed in terms of **six fundamental quantities**:

| Symbol | Name | Units | Physical Meaning |
|--------|------|-------|-----------------|
| $\mathcal{E}$ | Electric intensity (电场强度) | V/m | Force per unit charge |
| $\mathcal{H}$ | Magnetic intensity (磁场强度) | A/m | Magnetomotive force per unit length |
| $\mathcal{D}$ | Electric flux density (电通量密度) | C/m² | Electric flux per unit area |
| $\mathcal{B}$ | Magnetic flux density (磁通量密度) | Wb/m² | Magnetic flux per unit area |
| $\mathcal{J}$ | Electric current density (电流密度) | A/m² | Current per unit area |
| $q_v$ | Electric charge density (电荷密度) | C/m³ | Charge per unit volume |

A quantity is called **well-behaved** wherever it is a continuous function with continuous derivatives.

**Maxwell's Equations (differential form):**

$$\nabla \times \mathcal{E} = -\frac{\partial \mathcal{B}}{\partial t} \tag{1-1a}$$

$$\nabla \times \mathcal{H} = \mathcal{J} + \frac{\partial \mathcal{D}}{\partial t} \tag{1-1b}$$

$$\nabla \cdot \mathcal{D} = q_v \tag{1-1c}$$

$$\nabla \cdot \mathcal{B} = 0 \tag{1-1d}$$

**Equation of Continuity (电荷守恒方程):**

$$\nabla \cdot \mathcal{J} = -\frac{\partial q_v}{\partial t} \tag{1-2}$$

**Maxwell's Equations (integral form):**

$$\oint_C \mathcal{E} \cdot d\mathbf{l} = -\frac{d}{dt}\int_S \mathcal{B} \cdot d\mathbf{s} \tag{1-3a}$$

$$\oint_C \mathcal{H} \cdot d\mathbf{l} = \int_S\left(\mathcal{J} + \frac{\partial \mathcal{D}}{\partial t}\right)\cdot d\mathbf{s} \tag{1-3b}$$

$$\oint_S \mathcal{D} \cdot d\mathbf{s} = \int_V q_v\, dV \tag{1-3c}$$

$$\oint_S \mathcal{B} \cdot d\mathbf{s} = 0 \tag{1-3d}$$

**Circuit Quantities (电路量)与场量的关系:**

| Circuit Quantity | Symbol | Field Relation | Units |
|-----------------|--------|---------------|-------|
| Voltage (电压) | $v$ | $v = \int_a^b \mathcal{E} \cdot d\mathbf{l}$ | V |
| Current (电流) | $i$ | $i = \int_S \mathcal{J} \cdot d\mathbf{s}$ | A |
| Charge (电荷) | $q$ | $q = \int_V q_v\, dV$ | C |
| Magnetic flux (磁通) | $\psi$ | $\psi = \int_S \mathcal{B} \cdot d\mathbf{s}$ | Wb |
| Electric flux (电通) | $\psi^*$ | $\psi^* = \int_S \mathcal{D} \cdot d\mathbf{s}$ | C |
| Magnetomotive force (磁动势) | $u$ | $u = \oint_C \mathcal{H} \cdot d\mathbf{l}$ | A |

**中文：**

电磁场方程用**六个基本量**表示：

| 符号 | 名称 | 单位 | 物理意义 |
|------|------|------|---------|
| $\mathcal{E}$ | 电场强度 | V/m | 单位电荷所受之力 |
| $\mathcal{H}$ | 磁场强度 | A/m | 单位长度磁动势 |
| $\mathcal{D}$ | 电通量密度 | C/m² | 单位面积电通量 |
| $\mathcal{B}$ | 磁通量密度 | Wb/m² | 单位面积磁通量 |
| $\mathcal{J}$ | 电流密度 | A/m² | 单位面积电流 |
| $q_v$ | 电荷密度 | C/m³ | 单位体积电荷 |

**麦克斯韦方程（微分形式）：**

$$\nabla \times \mathcal{E} = -\frac{\partial \mathcal{B}}{\partial t} \tag{1-1a}$$

$$\nabla \times \mathcal{H} = \mathcal{J} + \frac{\partial \mathcal{D}}{\partial t} \tag{1-1b}$$

$$\nabla \cdot \mathcal{D} = q_v \tag{1-1c}$$

$$\nabla \cdot \mathcal{B} = 0 \tag{1-1d}$$

**连续性方程（电荷守恒）：**

$$\nabla \cdot \mathcal{J} = -\frac{\partial q_v}{\partial t} \tag{1-2}$$

**麦克斯韦方程（积分形式）：**

$$\oint_C \mathcal{E} \cdot d\mathbf{l} = -\frac{d}{dt}\int_S \mathcal{B} \cdot d\mathbf{s} \tag{1-3a}$$

$$\oint_C \mathcal{H} \cdot d\mathbf{l} = \int_S\left(\mathcal{J} + \frac{\partial \mathcal{D}}{\partial t}\right)\cdot d\mathbf{s} \tag{1-3b}$$

$$\oint_S \mathcal{D} \cdot d\mathbf{s} = \int_V q_v\, dV \tag{1-3c}$$

$$\oint_S \mathcal{B} \cdot d\mathbf{s} = 0 \tag{1-3d}$$

---

## Section 1-3: Constitutive Relationships / 本构关系

**English:**

In addition to the field equations, we need **constitutive relationships** that specify the characteristics of the medium:

$$\mathcal{D} = \mathcal{D}(\mathcal{E}, \mathcal{H}), \quad \mathcal{B} = \mathcal{B}(\mathcal{E}, \mathcal{H}), \quad \mathcal{J} = \mathcal{J}(\mathcal{E}, \mathcal{H}) \tag{1-10}$$

**Free Space (真空 / 自由空间):**

$$\mathcal{D} = \epsilon_0 \mathcal{E}, \quad \mathcal{B} = \mu_0 \mathcal{H}, \quad \mathcal{J} = 0 \tag{1-11}$$

where:
- $\epsilon_0 = 8.854 \times 10^{-12}$ F/m (permittivity of free space)
- $\mu_0 = 4\pi \times 10^{-7}$ H/m (permeability of free space)

The velocity of light in free space:
$$c = \frac{1}{\sqrt{\epsilon_0 \mu_0}} = 2.998 \times 10^8 \text{ m/s} \approx 3 \times 10^8 \text{ m/s} \tag{1-12}$$

**Simple Matter (简单物质):** Linear relationships

$$\mathcal{D} = \epsilon \mathcal{E}, \quad \mathcal{B} = \mu \mathcal{H}, \quad \mathcal{J} = \sigma \mathcal{E} \tag{1-15}$$

where:
- $\epsilon$ = capacitivity (电容率) [F/m]
- $\mu$ = inductivity (磁导率) [H/m]
- $\sigma$ = conductivity (电导率) [S/m]

**Relative parameters:**
$$\epsilon_r = \frac{\epsilon}{\epsilon_0}, \quad \mu_r = \frac{\mu}{\mu_0}$$

**Material classification:**
- **Conductors** (导体): large $\sigma$
- **Insulators/Dielectrics** (绝缘体/电介质): small $\sigma$
- **Perfect conductor**: $\sigma \to \infty$
- **Perfect dielectric**: $\sigma = 0$
- **Nonmagnetic materials**: $\mu_r \approx 1$ (diamagnetic, paramagnetic)
- **Ferromagnetic materials**: $\mu_r \gg 1$ (nonlinear)

**中文：**

除场方程外，我们还需要描述介质特性的**本构关系**：

$$\mathcal{D} = \mathcal{D}(\mathcal{E}, \mathcal{H}), \quad \mathcal{B} = \mathcal{B}(\mathcal{E}, \mathcal{H}), \quad \mathcal{J} = \mathcal{J}(\mathcal{E}, \mathcal{H}) \tag{1-10}$$

**自由空间：**

$$\mathcal{D} = \epsilon_0 \mathcal{E}, \quad \mathcal{B} = \mu_0 \mathcal{H}, \quad \mathcal{J} = 0 \tag{1-11}$$

其中：
- $\epsilon_0 = 8.854 \times 10^{-12}$ F/m（真空介电常数）
- $\mu_0 = 4\pi \times 10^{-7}$ H/m（真空磁导率）

自由空间中的光速：
$$c = \frac{1}{\sqrt{\epsilon_0 \mu_0}} = 2.998 \times 10^8 \text{ m/s} \approx 3 \times 10^8 \text{ m/s} \tag{1-12}$$

**简单物质：** 线性关系

$$\mathcal{D} = \epsilon \mathcal{E}, \quad \mathcal{B} = \mu \mathcal{H}, \quad \mathcal{J} = \sigma \mathcal{E} \tag{1-15}$$

其中：
- $\epsilon$ = 电容率 [F/m]
- $\mu$ = 磁导率 [H/m]
- $\sigma$ = 电导率 [S/m]

**相对参数：**
$$\epsilon_r = \frac{\epsilon}{\epsilon_0}, \quad \mu_r = \frac{\mu}{\mu_0}$$

---

## Section 1-4: The Generalized Current Concept / 广义电流概念

**English:**

The **generalized current concept** extends the notion of current to include both real conduction currents and displacement currents.

In Ampère-Maxwell's law:
$$\nabla \times \mathcal{H} = \mathcal{J} + \frac{\partial \mathcal{D}}{\partial t}$$

The term $\frac{\partial \mathcal{D}}{\partial t}$ is the **displacement current density**, while $\mathcal{J}$ is the **conduction current density**.

**Total current (总电流):**
$$\mathcal{J}_\text{total} = \mathcal{J}_\text{conduction} + \mathcal{J}_\text{displacement} = \sigma \mathcal{E} + \epsilon \frac{\partial \mathcal{E}}{\partial t}$$

This unified treatment of conduction and displacement currents is essential for:
- Analysis of conducting media under time-varying fields
- Capacitor behavior at high frequencies
- Electromagnetic wave propagation in dielectrics

**中文：**

**广义电流概念**将电流的概念扩展到包括真实的传导电流和位移电流。

在安培-麦克斯韦定律中：
$$\nabla \times \mathcal{H} = \mathcal{J} + \frac{\partial \mathcal{D}}{\partial t}$$

其中 $\frac{\partial \mathcal{D}}{\partial t}$ 是**位移电流密度**，而 $\mathcal{J}$ 是**传导电流密度**。

**总电流：**
$$\mathcal{J}_\text{total} = \mathcal{J}_\text{conduction} + \mathcal{J}_\text{displacement} = \sigma \mathcal{E} + \epsilon \frac{\partial \mathcal{E}}{\partial t}$$

这种对传导电流和位移电流的统一处理对于以下方面至关重要：
- 变化场中导电介质的研究
- 高频下电容器的行为
- 电介质中电磁波的传播

---

## Section 1-5: Energy and Power / 能量与功率

**English:**

**Poynting's theorem** expresses the conservation of electromagnetic power:

$$\nabla \cdot \mathbf{S} + \frac{\partial w}{\partial t} = -\mathcal{J} \cdot \mathcal{E} \tag{1-24}$$

where:
- $\mathbf{S} = \mathcal{E} \times \mathcal{H}$ is the **Poynting vector** (power flux density)
- $w = \frac{1}{2}(\mathcal{E} \cdot \mathcal{D} + \mathcal{H} \cdot \mathcal{B})$ is the **electromagnetic energy density**

**Instantaneous power balance:**
$$\frac{d}{dt} \int_V w\, dV + \oint_S \mathbf{S} \cdot d\mathbf{s} = -\int_V \mathcal{J} \cdot \mathcal{E}\, dV$$

**Time-average power in sinusoidal steady state:**
$$P_\text{avg} = \frac{1}{2} \text{Re}\{\int_V \mathcal{E} \cdot \mathcal{J}^*\, dV\} = \frac{1}{2} \text{Re}\{\oint_S (\mathcal{E} \times \mathcal{H}^*) \cdot d\mathbf{s}\}$$

**Power loss density (功率损耗密度):**
$$p_\text{loss} = \mathcal{J} \cdot \mathcal{E} = \sigma |\mathcal{E}|^2$$ (in conductors)

**Energy densities:**
$$w_\text{e} = \frac{1}{2} \mathcal{E} \cdot \mathcal{D} = \frac{1}{2} \epsilon |\mathcal{E}|^2 \quad \text{(electric energy)}$$
$$w_\text{m} = \frac{1}{2} \mathcal{H} \cdot \mathcal{B} = \frac{1}{2} \mu |\mathcal{H}|^2 \quad \text{(magnetic energy)}$$

**中文：**

**坡印廷定理**表达了电磁功率的守恒：

$$\nabla \cdot \mathbf{S} + \frac{\partial w}{\partial t} = -\mathcal{J} \cdot \mathcal{E} \tag{1-24}$$

其中：
- $\mathbf{S} = \mathcal{E} \times \mathcal{H}$ 是**坡印廷矢量**（功率通量密度）
- $w = \frac{1}{2}(\mathcal{E} \cdot \mathcal{D} + \mathcal{H} \cdot \mathcal{B})$ 是**电磁能量密度**

**瞬时功率平衡：**
$$\frac{d}{dt} \int_V w\, dV + \oint_S \mathbf{S} \cdot d\mathbf{s} = -\int_V \mathcal{J} \cdot \mathcal{E}\, dV$$

**正弦稳态下的时间平均功率：**
$$P_\text{avg} = \frac{1}{2} \text{Re}\{\int_V \mathcal{E} \cdot \mathcal{J}^*\, dV\} = \frac{1}{2} \text{Re}\{\oint_S (\mathcal{E} \times \mathcal{H}^*) \cdot d\mathbf{s}\}$$

**功率损耗密度（导体中）：**
$$p_\text{loss} = \mathcal{J} \cdot \mathcal{E} = \sigma |\mathcal{E}|^2$$

**能量密度：**
$$w_\text{e} = \frac{1}{2} \mathcal{E} \cdot \mathcal{D} = \frac{1}{2} \epsilon |\mathcal{E}|^2 \quad \text{（电场能）}$$
$$w_\text{m} = \frac{1}{2} \mathcal{H} \cdot \mathcal{B} = \frac{1}{2} \mu |\mathcal{H}|^2 \quad \text{（磁场能）}$$

---

## Section 1-6: Circuit Concepts / 电路概念

**English:**

Circuit theory is a **specialization of field theory**. Kirchhoff's laws are generalizations of Maxwell's equations applied to lumped circuit elements.

**Kirchhoff's Current Law (KCL):** From conservation of charge / 源自电荷守恒
$$\sum_{k} i_k = 0 \quad \text{(at a junction)}$$

**Kirchhoff's Voltage Law (KVL):** From Faraday's law / 源自法拉第定律
$$\sum_{k} v_k = 0 \quad \text{(around a closed loop)}$$

**Element laws:**
- Resistor: $v = Ri$ (Ohm's law, from $\mathcal{J} = \sigma \mathcal{E}$)
- Capacitor: $i = C\frac{dv}{dt}$ (from $\mathcal{D} = \epsilon \mathcal{E}$)
- Inductor: $v = L\frac{di}{dt}$ (from $\mathcal{B} = \mu \mathcal{H}$)

**Energy in circuit elements:**
- Resistor: $W_R = \int p\, dt = \int i^2 R\, dt$
- Capacitor: $W_C = \frac{1}{2}CV^2 = \frac{1}{2}\int \mathcal{E} \cdot \mathcal{D}\, dV$
- Inductor: $W_L = \frac{1}{2}LI^2 = \frac{1}{2}\int \mathcal{H} \cdot \mathcal{B}\, dV$

**中文：**

电路理论是场理论的**简化形式**。基尔霍夫定律是应用于集总电路元件的麦克斯韦方程的推广。

**基尔霍夫电流定律（KCL）：** 源自电荷守恒
$$\sum_{k} i_k = 0 \quad \text{（在节点处）}$$

**基尔霍夫电压定律（KVL）：** 源自法拉第定律
$$\sum_{k} v_k = 0 \quad \text{（沿闭合回路）}$$

**元件定律：**
- 电阻：$v = Ri$（欧姆定律，源自 $\mathcal{J} = \sigma \mathcal{E}$）
- 电容：$i = C\frac{dv}{dt}$（源自 $\mathcal{D} = \epsilon \mathcal{E}$）
- 电感：$v = L\frac{di}{dt}$（源自 $\mathcal{B} = \mu \mathcal{H}$）

**电路元件中的能量：**
- 电阻：$W_R = \int p\, dt = \int i^2 R\, dt$
- 电容：$W_C = \frac{1}{2}CV^2 = \frac{1}{2}\int \mathcal{E} \cdot \mathcal{D}\, dV$
- 电感：$W_L = \frac{1}{2}LI^2 = \frac{1}{2}\int \mathcal{H} \cdot \mathcal{B}\, dV$

---

## Section 1-7: Complex Quantities / 复量

**English:**

For **sinusoidal steady-state** analysis, we use **complex phasors** (phasor notation) to simplify differential equations into algebraic equations.

**Euler's identity:**
$$e^{j\phi} = \cos\phi + j\sin\phi$$

**Phasor representation:**
$$v(t) = \sqrt{2}|V|\cos(\omega t + \phi) = \sqrt{2}\text{Re}\{Ve^{j\omega t}\}$$
where $V = |V|e^{j\phi}$ is the **complex voltage** (phasor).

Note: Harrington uses **script letters** ($\mathcal{E}, \mathcal{H}$) for instantaneous (time-domain) field quantities, and **roman letters** ($E, H$) for complex (phasor) quantities.

**Phasor relationships:**
- $\frac{\partial}{\partial t} \leftrightarrow j\omega$
- $\int \cdot dt \leftrightarrow \frac{1}{j\omega}$

**Complex field vectors:**
$$\tilde{\mathcal{E}}(\mathbf{r}, t) = \sqrt{2}\text{Re}\{ \mathbf{E}(\mathbf{r}) e^{j\omega t} \}$$
where $\mathbf{E}(\mathbf{r})$ is the complex electric intensity (time-independent).

**中文：**

对于**正弦稳态**分析，我们使用**复相量**（相量表示法）将微分方程简化为代数方程。

**欧拉公式：**
$$e^{j\phi} = \cos\phi + j\sin\phi$$

**相量表示：**
$$v(t) = \sqrt{2}|V|\cos(\omega t + \phi) = \sqrt{2}\text{Re}\{Ve^{j\omega t}\}$$
其中 $V = |V|e^{j\phi}$ 是**复电压**（相量）。

注意：Harrington使用**手写体字母** ($\mathcal{E}, \mathcal{H}$) 表示瞬时（时域）场量，而使用**罗马字母** ($E, H$) 表示复（相量）量。

**相量关系：**
- $\frac{\partial}{\partial t} \leftrightarrow j\omega$
- $\int \cdot dt \leftrightarrow \frac{1}{j\omega}$

---

## Section 1-8: Complex Equations / 复方程

**English:**

With phasor notation, Maxwell's equations become **time-independent algebraic equations**:

$$\nabla \times \mathbf{E} = -j\omega \mathbf{B} \tag{1-54a}$$
$$\nabla \times \mathbf{H} = \mathbf{J} + j\omega \mathbf{D} \tag{1-54b}$$
$$\nabla \cdot \mathbf{D} = q_v \tag{1-54c}$$
$$\nabla \cdot \mathbf{B} = 0 \tag{1-54d}$$

For **source-free** regions ($\mathbf{J} = 0, q_v = 0$):
$$\nabla \times \mathbf{E} = -j\omega \mu \mathbf{H}$$
$$\nabla \times \mathbf{H} = j\omega \epsilon \mathbf{E}$$

Taking the curl of the first and substituting:
$$\nabla \times \nabla \times \mathbf{E} = -j\omega \mu (\nabla \times \mathbf{H}) = -j\omega \mu (j\omega \epsilon \mathbf{E}) = \omega^2 \mu \epsilon \mathbf{E}$$

Using the vector identity $\nabla \times \nabla \times \mathbf{E} = \nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E}$ and $\nabla \cdot \mathbf{E} = 0$ for source-free:
$$\nabla^2 \mathbf{E} + k^2 \mathbf{E} = 0 \quad \text{(Helmholtz equation)}$$

where the **wave number** $k = \omega\sqrt{\mu\epsilon}$.

**中文：**

使用相量表示法，麦克斯韦方程变为**时间无关的代数方程**：

$$\nabla \times \mathbf{E} = -j\omega \mathbf{B} \tag{1-54a}$$
$$\nabla \times \mathbf{H} = \mathbf{J} + j\omega \mathbf{D} \tag{1-54b}$$
$$\nabla \cdot \mathbf{D} = q_v \tag{1-54c}$$
$$\nabla \cdot \mathbf{B} = 0 \tag{1-54d}$$

对于**无源**区域 ($\mathbf{J} = 0, q_v = 0$)：
$$\nabla \times \mathbf{E} = -j\omega \mu \mathbf{H}$$
$$\nabla \times \mathbf{H} = j\omega \epsilon \mathbf{E}$$

取第一个方程的旋度并代入：
$$\nabla \times \nabla \times \mathbf{E} = -j\omega \mu (\nabla \times \mathbf{H}) = -j\omega \mu (j\omega \epsilon \mathbf{E}) = \omega^2 \mu \epsilon \mathbf{E}$$

利用向量恒等式 $\nabla \times \nabla \times \mathbf{E} = \nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E}$，以及无源条件下 $\nabla \cdot \mathbf{E} = 0$：
$$\nabla^2 \mathbf{E} + k^2 \mathbf{E} = 0 \quad \text{（亥姆霍兹方程）}$$

其中**波数** $k = \omega\sqrt{\mu\epsilon}$。

---

## Section 1-9: Complex Constitutive Parameters / 复本构参数

**English:**

For **lossy media**, we generalize permittivity and permeability to **complex quantities**:

$$\epsilon = \epsilon' - j\epsilon'' \quad \text{(complex permittivity)}$$
$$\mu = \mu' - j\mu'' \quad \text{(complex permeability)}$$
$$\sigma = \sigma' + j\sigma'' \quad \text{(complex conductivity)}$$

**Loss tangent (损耗角正切):**
$$\tan\delta_e = \frac{\epsilon''}{\epsilon'} \quad \text{(electric loss tangent)}$$
$$\tan\delta_m = \frac{\mu''}{\mu'} \quad \text{(magnetic loss tangent)}$$

**Intrinsic impedance of lossy medium:**
$$\eta = \sqrt{\frac{j\omega\mu}{j\omega\epsilon + \sigma}} = \sqrt{\frac{\mu}{\epsilon}}\sqrt{\frac{j\omega\mu}{\sigma + j\omega\epsilon}}$$

For a **low-loss dielectric** where $\sigma \ll \omega\epsilon$:
$$\eta \approx \sqrt{\frac{\mu}{\epsilon}}\left(1 + \frac{j\omega\epsilon''}{2(\sigma + j\omega\epsilon')}\right)$$

**Propagation constant in lossy media:**
$$\gamma = \alpha + j\beta = \sqrt{j\omega\mu(\sigma + j\omega\epsilon)}$$

For good conductors: $\gamma = (1+j)\sqrt{\frac{\omega\mu\sigma}{2}} = (1+j)/\delta_s$
where $\delta_s = \sqrt{2/(\omega\mu\sigma)}$ is the **skin depth**.

**中文：**

对于**有损耗介质**，我们将介电常数和磁导率推广为**复量**：

$$\epsilon = \epsilon' - j\epsilon'' \quad \text{（复介电常数）}$$
$$\mu = \mu' - j\mu'' \quad \text{（复磁导率）}$$
$$\sigma = \sigma' + j\sigma'' \quad \text{（复电导率）}$$

**损耗角正切：**
$$\tan\delta_e = \frac{\epsilon''}{\epsilon'} \quad \text{（电损耗角正切）}$$
$$\tan\delta_m = \frac{\mu''}{\mu'} \quad \text{（磁损耗角正切）}$$

**有损耗介质的本征阻抗：**
$$\eta = \sqrt{\frac{j\omega\mu}{j\omega\epsilon + \sigma}} = \sqrt{\frac{\mu}{\epsilon}}\sqrt{\frac{j\omega\mu}{\sigma + j\omega\epsilon}}$$

对于**低损耗电介质**（$\sigma \ll \omega\epsilon$）：
$$\eta \approx \sqrt{\frac{\mu}{\epsilon}}\left(1 + \frac{j\omega\epsilon''}{2(\sigma + j\omega\epsilon')}\right)$$

**有损耗介质中的传播常数：**
$$\gamma = \alpha + j\beta = \sqrt{j\omega\mu(\sigma + j\omega\epsilon)}$$

对于良导体：$\gamma = (1+j)\sqrt{\frac{\omega\mu\sigma}{2}} = (1+j)/\delta_s$
其中 $\delta_s = \sqrt{2/(\omega\mu\sigma)}$ 是**皮肤深度**。

---

## Section 1-10: Complex Power / 复功率

**English:**

For sinusoidal steady-state, we define **complex power** $S$ to handle reactive (stored) power:

$$S = P + jQ = \frac{1}{2}\mathbf{E} \cdot \mathbf{H}^* \quad \text{(power density)}$$

where:
- $P = \text{Re}\{S\}$ = **real power** (dissipated as heat)
- $Q = \text{Im}\{S\}$ = **reactive power** (stored in fields)

**Total complex power:**
$$P + jQ = \frac{1}{2}\int_V \mathbf{E} \cdot \mathbf{J}^*\, dV - \frac{1}{2}\oint_S (\mathbf{E} \times \mathbf{H}^*)\cdot d\mathbf{s}$$

**Power loss in conductors:**
$$\mathbf{E} \cdot \mathbf{J}^* = \sigma |\mathbf{E}|^2 \quad \text{(conduction loss density)}$$

**Quality factor Q:**
$$Q = \frac{\omega \times \text{stored energy}}{\text{dissipated power}} = \frac{\omega W_\text{stored}}{P_\text{loss}}$$

**For resonant cavities:** $Q = \omega W_\text{stored} / P_\text{loss}$

**中文：**

对于正弦稳态，我们定义**复功率** $S$ 来处理无功（储能）功率：

$$S = P + jQ = \frac{1}{2}\mathbf{E} \cdot \mathbf{H}^* \quad \text{（功率密度）}$$

其中：
- $P = \text{Re}\{S\}$ = **有功功率**（以热的形式耗散）
- $Q = \text{Im}\{S\}$ = **无功功率**（存储在场中）

**总复功率：**
$$P + jQ = \frac{1}{2}\int_V \mathbf{E} \cdot \mathbf{J}^*\, dV - \frac{1}{2}\oint_S (\mathbf{E} \times \mathbf{H}^*)\cdot d\mathbf{s}$$

**导体中的功率损耗：**
$$\mathbf{E} \cdot \mathbf{J}^* = \sigma |\mathbf{E}|^2 \quad \text{（传导损耗密度）}$$

**品质因数 Q：**
$$Q = \frac{\omega \times \text{储能}}{\text{耗散功率}} = \frac{\omega W_\text{stored}}{P_\text{loss}}$$

**对于谐振腔：** $Q = \omega W_\text{stored} / P_\text{loss}$

---

## Section 1-11: A-C Characteristics of Matter / 物质的交流特性

**English:**

The electromagnetic properties of materials depend on **frequency** due to polarization mechanisms:

**Debye model** for dielectric relaxation:
$$\epsilon(\omega) = \epsilon_\infty + \frac{\epsilon_s - \epsilon_\infty}{1 + j\omega\tau}$$

where:
- $\epsilon_s$ = static (low-frequency) permittivity
- $\epsilon_\infty$ = optical (high-frequency) permittivity
- $\tau$ = relaxation time

**Dispersion** occurs when $\epsilon$ varies with $\omega$. Different frequency ranges exhibit different behavior:

| Frequency Range | Behavior |
|-----------------|----------|
| Static ($\omega \tau \ll 1$) | $\epsilon \approx \epsilon_s$ |
| Relaxation region | $\epsilon''$ peaks at $\omega \approx 1/\tau$ |
| High frequency ($\omega\tau \gg 1$) | $\epsilon \approx \epsilon_\infty$ |

**Complex refractive index:**
$$n = n' - jn'' = \sqrt{\epsilon_r \mu_r}$$

**Absorption coefficient:**
$$\alpha = \frac{2\omega n''}{c} = \frac{4\pi n''}{\lambda_0}$$

**Drude model** for conduction electrons in metals (at high frequencies):
$$\epsilon(\omega) = \epsilon_0\left(1 - \frac{\omega_p^2}{\omega^2 + j\gamma\omega}\right)$$

where $\omega_p = \sqrt{n_e e^2/(\epsilon_0 m)}$ is the **plasma frequency**.

**中文：**

材料的电磁特性随**频率**变化，这是由于极化机制：

**电介质的德拜模型：**
$$\epsilon(\omega) = \epsilon_\infty + \frac{\epsilon_s - \epsilon_\infty}{1 + j\omega\tau}$$

其中：
- $\epsilon_s$ = 静态（低频）介电常数
- $\epsilon_\infty$ = 光学（高频）介电常数
- $\tau$ = 弛豫时间

**色散**发生在 $\epsilon$ 随 $\omega$ 变化时。不同的频率范围表现出不同的行为：

| 频率范围 | 行为 |
|---------|------|
| 静态 ($\omega\tau \ll 1$) | $\epsilon \approx \epsilon_s$ |
| 弛豫区域 | $\epsilon''$ 在 $\omega \approx 1/\tau$ 处达到峰值 |
| 高频 ($\omega\tau \gg 1$) | $\epsilon \approx \epsilon_\infty$ |

**复折射率：**
$$n = n' - jn'' = \sqrt{\epsilon_r \mu_r}$$

**吸收系数：**
$$\alpha = \frac{2\omega n''}{c} = \frac{4\pi n''}{\lambda_0}$$

**金属中导电电子的Drude模型（高频）：**
$$\epsilon(\omega) = \epsilon_0\left(1 - \frac{\omega_p^2}{\omega^2 + j\gamma\omega}\right)$$

其中 $\omega_p = \sqrt{n_e e^2/(\epsilon_0 m)}$ 是**等离子体频率**。


---

---
chapter: 2
title: Introduction to Waves
source: Roger F. Harrington, Time-Harmonic Electromagnetic Fields, IEEE Press
pages: 37-150
---

# Chapter 2: Introduction to Waves / 波动学引论

## Section 2-1: The Wave Equation / 波动方程

**English:**

A field that is a function of both time and space coordinates can be called a wave. More precisely, we use the term **wave** to denote a solution to a **wave equation** — a particular type of differential equation that electromagnetic fields obey.

For **source-free** ($\mathbf{J} = 0$), **linear**, **homogeneous**, **isotropic** regions, Maxwell's equations in phasor form are:

$$\nabla \times \mathbf{E} = -j\omega\mu\mathbf{H} \tag{2-1a}$$

$$\nabla \times \mathbf{H} = j\omega\epsilon\mathbf{E} \tag{2-1b}$$

Taking the curl of (2-1a) and substituting from (2-1b):

$$\nabla \times \nabla \times \mathbf{E} = -j\omega\mu(\nabla \times \mathbf{H}) = -j\omega\mu(j\omega\epsilon\mathbf{E}) = \omega^2\mu\epsilon\mathbf{E}$$

Using the vector identity $\nabla \times \nabla \times \mathbf{A} = \nabla(\nabla \cdot \mathbf{A}) - \nabla^2\mathbf{A}$ and noting that $\nabla \cdot \mathbf{E} = 0$ for source-free regions:

$$\nabla^2\mathbf{E} + k^2\mathbf{E} = 0 \tag{2-3}$$

where the **wave number** (相位常数) is:

$$k = \omega\sqrt{\mu\epsilon} \tag{2-2}$$

Similarly for $\mathbf{H}$:

$$\nabla^2\mathbf{H} + k^2\mathbf{H} = 0 \tag{2-4}$$

Equations (2-3) and (2-4) are called the **vector Helmholtz equation** (矢量亥姆霍兹方程). The rectangular components satisfy the **scalar Helmholtz equation**:

$$\nabla^2\psi + k^2\psi = 0 \tag{2-7}$$

---

**Example: Uniform Plane Wave in Perfect Dielectric / 完美电介质中的均匀平面波**

For a perfect dielectric where $\sigma = 0$, $k = \omega\sqrt{\mu\epsilon}$ is real.

Consider a wave propagating in the $z$-direction with only $x$-component of $\mathbf{E}$:

$$E_x = E_0 e^{-jkz} \tag{2-9}$$

This satisfies $\nabla \cdot \mathbf{E} = 0$ and is therefore a valid EM field.

The associated magnetic field from Faraday's law:

$$j\omega\mu H_y = -\frac{\partial E_x}{\partial z} = jk E_x \Rightarrow H_y = \frac{k}{\omega\mu}E_x = \frac{E_x}{\eta} \tag{2-10}$$

where the **intrinsic impedance** (本征阻抗) of the medium is:

$$\eta = \sqrt{\frac{\mu}{\epsilon}} \tag{2-11}$$

In vacuum: $\eta_0 = \sqrt{\mu_0/\epsilon_0} \approx 120\pi \approx 377\ \Omega$ (2-12)

**Instantaneous fields (瞬时场):**

$$\mathcal{E}_x = \sqrt{2}E_0\cos(\omega t - kz)$$
$$\mathcal{H}_y = \frac{\sqrt{2}E_0}{\eta}\cos(\omega t - kz)$$

These represent a **uniform plane wave** traveling in the $+z$ direction with **phase velocity** $v_p = \omega/k = 1/\sqrt{\mu\epsilon}$.

In vacuum: $v_p = c = 3 \times 10^8$ m/s.

**中文：**

场是时间和空间坐标的函数，可以称为波。更准确地说，我们用**波**这个术语来表示一类特殊微分方程——**波动方程**——的解，电磁场服从波动方程。

对于**无源** ($\mathbf{J} = 0$)、**线性**、**均匀**、**各向同性**区域，相量形式的麦克斯韦方程为：

$$\nabla \times \mathbf{E} = -j\omega\mu\mathbf{H} \tag{2-1a}$$

$$\nabla \times \mathbf{H} = j\omega\epsilon\mathbf{E} \tag{2-1b}$$

取(2-1a)的旋度并代入(2-1b)：

$$\nabla \times \nabla \times \mathbf{E} = -j\omega\mu(\nabla \times \mathbf{H}) = -j\omega\mu(j\omega\epsilon\mathbf{E}) = \omega^2\mu\epsilon\mathbf{E}$$

利用向量恒等式 $\nabla \times \nabla \times \mathbf{A} = \nabla(\nabla \cdot \mathbf{A}) - \nabla^2\mathbf{A}$，并注意无源区域 $\nabla \cdot \mathbf{E} = 0$：

$$\nabla^2\mathbf{E} + k^2\mathbf{E} = 0 \tag{2-3}$$

其中**波数**为：

$$k = \omega\sqrt{\mu\epsilon} \tag{2-2}$$

对 $\mathbf{H}$ 类似：

$$\nabla^2\mathbf{H} + k^2\mathbf{H} = 0 \tag{2-4}$$

方程(2-3)和(2-4)称为**矢量亥姆霍兹方程**。直角分量满足**标量亥姆霍兹方程**：

$$\nabla^2\psi + k^2\psi = 0 \tag{2-7}$$

---

## Section 2-2: Waves in Perfect Dielectrics / 完美电介质中的波

**English:**

**Uniform plane wave** propagation in a perfect dielectric:

The wave propagates without attenuation ($\alpha = 0$) with **propagation constant**:

$$\gamma = j\beta = j\omega\sqrt{\mu\epsilon} \tag{in perfect dielectric}$$

**Phase velocity (相速度):**

$$v_p = \frac{\omega}{\beta} = \frac{1}{\sqrt{\mu\epsilon}}$$

**Wavelength (波长):**

$$\lambda = \frac{2\pi}{\beta} = \frac{v_p}{f}$$

**Intrinsic impedance (本征阻抗):**

$$\eta = \sqrt{\frac{\mu}{\epsilon}} = \eta_0\sqrt{\frac{\mu_r}{\epsilon_r}}$$

**Wave impedance** between $\mathcal{E}$ and $\mathcal{H}$ components is $\eta$ for a plane wave propagating in $+z$.

**Energy densities:**
$$w_e = \frac{1}{2}\epsilon|E|^2 \quad w_m = \frac{1}{2}\mu|H|^2$$

For a perfect plane wave: $w_e = w_m$ (equal electric and magnetic energy densities).

**Time-average Poynting vector (时间平均坡印廷矢量):**

$$\mathbf{S}_\text{avg} = \frac{1}{2}\text{Re}\{\mathbf{E} \times \mathbf{H}^*\} = \frac{|E|^2}{2\eta}\hat{\mathbf{z}} \quad \text{W/m}^2$$

**中文：**

**均匀平面波**在完美电介质中的传播：

波在传播过程中无衰减 ($\alpha = 0$)，**传播常数**为：

$$\gamma = j\beta = j\omega\sqrt{\mu\epsilon}$$

**相速度：**

$$v_p = \frac{\omega}{\beta} = \frac{1}{\sqrt{\mu\epsilon}}$$

**波长：**

$$\lambda = \frac{2\pi}{\beta} = \frac{v_p}{f}$$

**本征阻抗：**

$$\eta = \sqrt{\frac{\mu}{\epsilon}} = \eta_0\sqrt{\frac{\mu_r}{\epsilon_r}}$$

$\mathcal{E}$ 和 $\mathcal{H}$ 分量之间的波阻抗在沿 $+z$ 方向传播的平面波中为 $\eta$。

**能量密度：**
$$w_e = \frac{1}{2}\epsilon|E|^2 \quad w_m = \frac{1}{2}\mu|H|^2$$

对于完美平面波：$w_e = w_m$（电场能和磁场能密度相等）。

---

## Section 2-3: Intrinsic Wave Constants / 本征波常数

**English:**

The **intrinsic wave constants** characterize wave propagation in a medium:

$$\gamma = \sqrt{j\omega\mu(\sigma + j\omega\epsilon)}$$

For **lossless media** ($\sigma = 0$):
$$\gamma = j\omega\sqrt{\mu\epsilon} = j\beta, \quad \alpha = 0$$

For **low-loss dielectrics** ($\sigma \ll \omega\epsilon$):
$$\alpha \approx \frac{\sigma}{2}\sqrt{\frac{\mu}{\epsilon}} \quad \text{(attenuation constant)}$$
$$\beta \approx \omega\sqrt{\mu\epsilon} \quad \text{(phase constant)}$$

For **good conductors** ($\sigma \gg \omega\epsilon$):
$$\gamma = (1+j)\sqrt{\frac{\omega\mu\sigma}{2}} = \frac{1+j}{\delta_s}$$

where **skin depth** (皮肤深度) $\delta_s = \sqrt{2/(\omega\mu\sigma)}$.

**Intrinsic impedance:**

$$\eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\epsilon}}$$

For lossless media: $\eta$ is real and equal to $\sqrt{\mu/\epsilon}$.

For lossy media: $\eta = |\eta|e^{j\theta_\eta}$ with phase shift.

**Dispersion** occurs when $\gamma$ (and thus $v_p$) depends on frequency. This happens in:
- Conductors at all frequencies
- Dielectrics near absorption resonances
- Plasmas (electron gas)

**Group velocity (群速度):**

$$v_g = \frac{d\omega}{d\beta}$$

In nondispersive media ($v_p$ constant): $v_g = v_p$.
In dispersive media: $v_g \neq v_p$.

**中文：**

**本征波常数**表征波在介质中的传播特性：

$$\gamma = \sqrt{j\omega\mu(\sigma + j\omega\epsilon)}$$

对于**无损介质** ($\sigma = 0$)：
$$\gamma = j\omega\sqrt{\mu\epsilon} = j\beta, \quad \alpha = 0$$

对于**低损耗电介质** ($\sigma \ll \omega\epsilon$)：
$$\alpha \approx \frac{\sigma}{2}\sqrt{\frac{\mu}{\epsilon}} \quad \text{（衰减常数）}$$
$$\beta \approx \omega\sqrt{\mu\epsilon} \quad \text{（相位常数）}$$

对于**良导体** ($\sigma \gg \omega\epsilon$)：
$$\gamma = (1+j)\sqrt{\frac{\omega\mu\sigma}{2}} = \frac{1+j}{\delta_s}$$

其中**皮肤深度** $\delta_s = \sqrt{2/(\omega\mu\sigma)}$。

**本征阻抗：**

$$\eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\epsilon}}$$

对于无损介质：$\eta$ 为实数，等于 $\sqrt{\mu/\epsilon}$。

对于有损耗介质：$\eta = |\eta|e^{j\theta_\eta}$，存在相位偏移。

---

## Section 2-4: Waves in Lossy Matter / 有损耗物质中的波

**English:**

For **general lossy media**, the propagation constant $\gamma = \alpha + j\beta$:

$$\alpha = \omega\sqrt{\frac{\mu\epsilon}{2}\left(\sqrt{1 + \left(\frac{\sigma}{\omega\epsilon}\right)^2} - 1\right)}$$

$$\beta = \omega\sqrt{\frac{\mu\epsilon}{2}\left(\sqrt{1 + \left(\frac{\sigma}{\omega\epsilon}\right)^2} + 1\right)}$$

Define **loss tangent** (损耗角正切) $\tan\delta = \sigma/(\omega\epsilon)$:

$$\gamma = j\omega\sqrt{\mu\epsilon}\sqrt{1 - j\tan\delta}$$

For $\tan\delta \ll 1$ (low loss):
$$\alpha \approx \frac{\omega\sqrt{\mu\epsilon}}{2}\tan\delta$$
$$\beta \approx \omega\sqrt{\mu\epsilon}\left(1 + \frac{\tan^2\delta}{8}\right)$$

**Complex permittivity representation:**

$$\epsilon_c = \epsilon' - j\epsilon'' = \epsilon'\left(1 - j\tan\delta\right)$$

where $\epsilon' = \epsilon$ and $\epsilon'' = \sigma/\omega$.

The field in a lossy medium decays as $e^{-\alpha z}$ while oscillating as $e^{-j\beta z}$.

**Penetration depth (穿透深度):**

$$\delta = \frac{1}{\alpha} \quad \text{(distance for field to decay to } 1/e \text{)}$$

**Complex wave impedance:**

$$\eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\epsilon}} = |\eta|e^{j\phi}$$

where $\phi = \tan^{-1}\left(\frac{\sigma}{\omega\epsilon}\right)/2$ for low-loss media.

**Phase difference between E and H:**
In lossy media, $\mathbf{E}$ and $\mathbf{H}$ are not in phase. The phase difference is $\phi$, where $\tan(2\phi) = \sigma/(\omega\epsilon)$.

**中文：**

对于**一般有损耗介质**，传播常数 $\gamma = \alpha + j\beta$：

$$\alpha = \omega\sqrt{\frac{\mu\epsilon}{2}\left(\sqrt{1 + \left(\frac{\sigma}{\omega\epsilon}\right)^2} - 1\right)}$$

$$\beta = \omega\sqrt{\frac{\mu\epsilon}{2}\left(\sqrt{1 + \left(\frac{\sigma}{\omega\epsilon}\right)^2} + 1\right)}$$

定义**损耗角正切** $\tan\delta = \sigma/(\omega\epsilon)$：

$$\gamma = j\omega\sqrt{\mu\epsilon}\sqrt{1 - j\tan\delta}$$

对于 $\tan\delta \ll 1$（低损耗）：
$$\alpha \approx \frac{\omega\sqrt{\mu\epsilon}}{2}\tan\delta$$
$$\beta \approx \omega\sqrt{\mu\epsilon}\left(1 + \frac{\tan^2\delta}{8}\right)$$

**复介电常数表示：**

$$\epsilon_c = \epsilon' - j\epsilon'' = \epsilon'\left(1 - j\tan\delta\right)$$

其中 $\epsilon' = \epsilon$，$\epsilon'' = \sigma/\omega$。

场在有损耗介质中以 $e^{-\alpha z}$ 衰减，同时以 $e^{-j\beta z}$ 振荡。

---

## Section 2-5: Reflection of Waves / 波的反射

**English:**

When a plane wave encounters an **interface** between two media, part is reflected and part is transmitted.

Consider a plane wave normally incident on a planar boundary at $z = 0$ between medium 1 ($z < 0$) and medium 2 ($z > 0$).

**Reflection coefficient (反射系数):**

$$\Gamma = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1} \tag{2-44}$$

**Transmission coefficient (透射系数):**

$$T = \frac{2\eta_2}{\eta_2 + \eta_1} = 1 + \Gamma \tag{2-45}$$

The total field in medium 1:
$$E_1 = E_i e^{-j\beta_1 z} + \Gamma E_i e^{+j\beta_1 z}$$

The transmitted field in medium 2:
$$E_2 = T E_i e^{-j\beta_2 z}$$

**Standing wave (驻波):**

When $|\Gamma| = 1$ (e.g., perfect conductor), the incident and reflected waves combine to form a standing wave pattern:

$$|E| = |E_i||1 + \Gamma e^{j2\beta_1 z}|$$

**Standing wave ratio (驻波比):**

$$SWR = \frac{1 + |\Gamma|}{1 - |\Gamma|} \tag{2-47}$$

**Power flow (功率流):**

$$P_\text{avg} = \frac{|E_i|^2}{2\eta_1}(1 - |\Gamma|^2) \quad \text{(in +z direction)}$$

**Oblique incidence (斜入射):** For oblique incidence at angle $\theta_i$:

**Snell's law:**
$$\frac{\sin\theta_i}{\sin\theta_t} = \frac{k_2}{k_1} = \frac{n_2}{n_1}$$

**Fresnel reflection coefficients (for parallel/perp polarization):**
$$\Gamma_\perp = \frac{\eta_2\cos\theta_i - \eta_1\cos\theta_t}{\eta_2\cos\theta_i + \eta_1\cos\theta_t}$$
$$\Gamma_\parallel = \frac{\eta_2\cos\theta_t - \eta_1\cos\theta_i}{\eta_2\cos\theta_t + \eta_1\cos\theta_i}$$

**Brewster angle (布鲁斯特角):** For $\Gamma_\parallel = 0$:
$$\theta_B = \tan^{-1}\sqrt{\frac{\epsilon_2\mu_1}{\epsilon_1\mu_2}}$$

**Critical angle (临界角):** For total internal reflection when propagating from higher to lower index:
$$\theta_c = \sin^{-1}\sqrt{\frac{\epsilon_2\mu_1}{\epsilon_1\mu_2}}$$

**中文：**

当平面波遇到两种介质之间的**界面**时，部分反射，部分透射。

考虑在 $z = 0$ 处平面边界上的法向入射波，边界两侧分别为介质1 ($z < 0$) 和介质2 ($z > 0$)。

**反射系数：**

$$\Gamma = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1} \tag{2-44}$$

**透射系数：**

$$T = \frac{2\eta_2}{\eta_2 + \eta_1} = 1 + \Gamma \tag{2-45}$$

介质1中的总场：
$$E_1 = E_i e^{-j\beta_1 z} + \Gamma E_i e^{+j\beta_1 z}$$

介质2中的透射场：
$$E_2 = T E_i e^{-j\beta_2 z}$$

**驻波比：**

$$SWR = \frac{1 + |\Gamma|}{1 - |\Gamma|} \tag{2-47}$$

---

## Section 2-6: Transmission-line Concepts / 传输线概念

**English:**

Transmission lines are **distributed parameter** circuits characterized by per-unit-length parameters $R, L, G, C$.

**Telegrapher's equations (电报员方程):**

$$\frac{\partial V}{\partial z} = -RI - L\frac{\partial I}{\partial t}$$
$$\frac{\partial I}{\partial z} = -GV - C\frac{\partial V}{\partial t}$$

In sinusoidal steady state ($j\omega$):

$$\frac{dV}{dz} = -\gamma V \quad \frac{dI}{dz} = -\gamma I$$

where:
- $\gamma = \sqrt{(R + j\omega L)(G + j\omega C)}$ (propagation constant)
- $Z_0 = \sqrt{(R + j\omega L)/(G + j\omega C)}$ (characteristic impedance)

**Wave propagation on transmission lines:**

$$V(z) = V^+ e^{-\gamma z} + V^- e^{+\gamma z}$$
$$I(z) = \frac{V^+}{Z_0}e^{-\gamma z} - \frac{V^-}{Z_0}e^{+\gamma z}$$

**Reflection coefficient at load:**
$$\Gamma_L = \frac{V^-}{V^+} = \frac{Z_L - Z_0}{Z_L + Z_0}$$

**Input impedance at distance $l$ from load:**
$$Z_in(l) = Z_0 \frac{1 + \Gamma_L e^{-2\gamma l}}{1 - \Gamma_L e^{-2\gamma l}}$$

**Special cases:**
- **Lossless line** ($R = G = 0$): $\gamma = j\beta$, $Z_0$ real
- **Matched line** ($\Gamma_L = 0$): No reflections, $Z_in = Z_0$
- **Short circuit** ($Z_L = 0$): $\Gamma_L = -1$, $Z_in = Z_0 \tanh(\gamma l)$
- **Open circuit** ($Z_L = \infty$): $\Gamma_L = +1$, $Z_in = Z_0 \coth(\gamma l)$

**Power on transmission line:**
$$P(z) = \frac{|V^+|^2}{2Z_0}e^{-2\alpha z}(1 - |\Gamma|^2)$$

**中文：**

传输线是具有**分布参数**的电路，以单位长度参数 $R, L, G, C$ 为特征。

**电报员方程：**

$$\frac{\partial V}{\partial z} = -RI - L\frac{\partial I}{\partial t}$$
$$\frac{\partial I}{\partial z} = -GV - C\frac{\partial V}{\partial t}$$

正弦稳态下 ($j\omega$)：

$$\frac{dV}{dz} = -\gamma V \quad \frac{dI}{dz} = -\gamma I$$

其中：
- $\gamma = \sqrt{(R + j\omega L)(G + j\omega C)}$（传播常数）
- $Z_0 = \sqrt{(R + j\omega L)/(G + j\omega C)}$（特性阻抗）

**负载处反射系数：**
$$\Gamma_L = \frac{V^-}{V^+} = \frac{Z_L - Z_0}{Z_L + Z_0}$$

---

## Section 2-7: Waveguide Concepts / 波导概念

**English:**

Waveguides are **hollow conducting structures** that guide electromagnetic waves at microwave frequencies.

**Parallel-plate waveguide:** Two parallel conducting plates.

For **TEM mode** (Transverse ElectroMagnetic — requires $\epsilon$ and $\mu$ uniform and finite, not possible in hollow waveguide):

$$E_z = 0, \quad H_z = 0, \quad \gamma = j\beta = j\omega\sqrt{\mu\epsilon}$$

**TE/TM modes:** Higher order modes with $E_z$ or $H_z$ nonzero.

**Rectangular waveguide:** Cross-section $a \times b$ with $a > b$.

**TE$_{mn}$ modes** have $H_z \neq 0$, $E_z = 0$:
$$h_z = H_0 \sin\left(\frac{m\pi x}{a}\right)\sin\left(\frac{n\pi y}{b}\right)e^{-\gamma z}$$

**Cutoff frequency (截止频率):**

$$f_c = \frac{c}{2}\sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}$$

Only frequencies $f > f_c$ propagate; below $f_c$, the mode is **evanescent** with real $\alpha$ and $\beta = 0$.

**Dominant mode (主模):** Lowest cutoff frequency mode.
- For rectangular waveguide: **TE$_{10}$** mode with $f_c = c/(2a)$.

**Phase velocity:** $v_p = \omega/\beta > c$ (above cutoff)
**Group velocity:** $v_g = d\omega/d\beta < c$
**Wave impedance:**
$$\eta_{TE} = \frac{\eta}{\cos\theta_g}, \quad \eta_{TM} = \eta\cos\theta_g$$
where $\sin\theta_g = f_c/f$ and $\eta = \sqrt{\mu/\epsilon}$.

**Attenuation in waveguides:**
- Conductor losses: power dissipated in waveguide walls
- Dielectric losses: power dissipated in filling medium

**中文：**

波导是**空心导电结构**，在微波频率下引导电磁波。

**矩形波导：** 截面 $a \times b$，其中 $a > b$。

**TE$_{mn}$ 模式** 具有 $H_z \neq 0$, $E_z = 0$：
$$h_z = H_0 \sin\left(\frac{m\pi x}{a}\right)\sin\left(\frac{n\pi y}{b}\right)e^{-\gamma z}$$

**截止频率：**

$$f_c = \frac{c}{2}\sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}$$

只有 $f > f_c$ 的频率才能传播；低于 $f_c$ 时，模式为**倏逝波**，具有实数 $\alpha$ 和 $\beta = 0$。

**主模：** 最低截止频率模式。
- 对于矩形波导：**TE$_{10}$** 模式，$f_c = c/(2a)$。

---

## Section 2-9: Radiation / 辐射

**English:**

**Radiation** is the process by which electromagnetic energy is converted to energy that propagates freely in space (far field).

**Hertzian dipole (赫兹偶极子):** A short current element of length $l$ carrying current $I$.

**Far-field radiation pattern:**
$$E_\theta = \frac{j\eta I_0 l}{2\pi r}e^{-jkr}\sin\theta$$
$$H_\phi = \frac{j I_0 l}{2\pi r}e^{-jkr}\sin\theta$$

The fields are **transverse** ($\mathbf{E} \perp \mathbf{H} \perp \hat{r}$).

**Radiation resistance (辐射电阻):**
$$R_\text{rad} = \frac{2\pi}{3}\left(\frac{Il}{\lambda}\right)^2 \quad \Omega$$

Power radiated: $P_\text{rad} = \frac{1}{2}|I|^2 R_\text{rad}$

**Directivity (方向性):**
$$D = \frac{4\pi}{\Omega_\text{rad}}$$

where $\Omega_\text{rad}$ is the radiation solid angle.

For Hertzian dipole: $D = 1.5$ (maximum)

**Antenna gain:**
$$G = \eta_e D$$
where $\eta_e$ is the radiation efficiency.

**Array factor (阵列因子):** For $N$ isotropic elements with spacing $d$ and phase shift $\psi$:

$$AF = \frac{\sin(N\psi/2)}{\sin(\psi/2)}$$

where $\psi = kd\cos\theta + \beta_\text{elem}$.

**中文：**

**辐射**是电磁能量转换为在空间中自由传播的能量（远区场）的过程。

**赫兹偶极子：** 长度为 $l$、电流为 $I$ 的短电流元。

**远区辐射场：**
$$E_\theta = \frac{j\eta I_0 l}{2\pi r}e^{-jkr}\sin\theta$$
$$H_\phi = \frac{j I_0 l}{2\pi r}e^{-jkr}\sin\theta$$

场是**横向**的 ($\mathbf{E} \perp \mathbf{H} \perp \hat{r}$)。

**辐射电阻：**
$$R_\text{rad} = \frac{2\pi}{3}\left(\frac{Il}{\lambda}\right)^2 \quad \Omega$$

---

## Section 2-10: Antenna Concepts / 天线概念

**English:**

An **antenna** is a structure that couples guided waves (transmission lines) to free-space waves and vice versa.

**Antenna parameters:**
- **Input impedance:** $Z_A = R_A + jX_A$
- **Radiation efficiency:** $\eta_e = R_\text{rad}/(R_\text{rad} + R_\text{loss})$
- **Bandwidth:** frequency range over which VSWR < specified value
- **Polarization:** orientation of $\mathbf{E}$ field vector

**Reciprocity theorem:** An antenna has the same radiation pattern and impedance when used for transmitting or receiving.

**Linear wire antennas:**
- **Hertzian dipole:** $l \ll \lambda$ (short dipole)
- **Half-wave dipole:** $l = \lambda/2$ (resonant, $R \approx 73\ \Omega$)
- **Full-wave dipole:** $l = \lambda$ ($R \approx 90\ \Omega$)
- **Yagi-Uda antenna:** parasitic directors and reflectors

**Moment method (MoM) analysis:** Used to solve for current distribution on wire antennas by converting integral equation to matrix equation.

**Frill (周线) current:** Current distribution on dipole arms found by solving Pocklington's integral equation.

**Folded dipole:** $R \approx 4 \times$ that of simple dipole ($\approx 300\ \Omega$).

**Aperture antennas:** Horn antennas, parabolic reflectors, microstrip patches.

**Array theory:** Multiple antenna elements arranged to achieve:
- Higher directivity (narrower beam)
- Electronic beam steering (phased arrays)

**Phased array:** Elements with variable phase shifters for beam steering without mechanical movement.

**中文：**

**天线**是将在传输线中传输的导波与自由空间波相互耦合的结构。

**天线参数：**
- **输入阻抗：** $Z_A = R_A + jX_A$
- **辐射效率：** $\eta_e = R_\text{rad}/(R_\text{rad} + R_\text{loss})$
- **带宽：** VSWR < 规定值的频率范围
- **极化：** $\mathbf{E}$ 场矢量的方向

**互易定理：** 天线在发射和接收时具有相同的辐射图和阻抗。

**线性导线天线：**
- **赫兹偶极子：** $l \ll \lambda$（短偶极子）
- **半波偶极子：** $l = \lambda/2$（谐振，$R \approx 73\ \Omega$）

---

## Section 2-11: On Waves in General / 波的一般性质

**English:**

The wave equation $\nabla^2\psi + k^2\psi = 0$ admits **plane wave** solutions:

$$\psi(\mathbf{r}) = \psi_0 e^{-j\mathbf{k} \cdot \mathbf{r}}$$

where $\mathbf{k}$ is the **wave vector** with $|\mathbf{k}| = k = \omega\sqrt{\mu\epsilon}$.

**Dispersion relations:**
- Non-dispersive: $v_p = \omega/k$ constant (vacuum, air at STP)
- Dispersive: $v_p$ varies with $\omega$ (waveguides, plasmas, dielectrics near resonance)

**Phase velocity:** $v_p = \omega/k$
**Group velocity:** $v_g = d\omega/dk$

**Wave types:**
- **Uniform plane wave:** constant amplitude and phase over equiphase planes
- **Non-uniform plane wave:** amplitude varies over equiphase planes
- **Evanescent wave:** decaying (not propagating) solution, $\beta = 0$, real $\alpha$
- **Surface wave:** bound to interface, decays exponentially away from surface
- **Leaky wave:** partially radiative, complex $\beta$

**Wave packet:** A localized group of waves in space, travels at group velocity.

**Phase front:** Surface of constant phase, propagates at phase velocity.

**Boundary conditions (边界条件):**
For perfect electric conductors (PEC):
$$\hat{n} \times \mathbf{E} = 0, \quad \hat{n} \cdot \mathbf{D} = \rho_s$$

For perfect magnetic conductors (PMC):
$$\hat{n} \times \mathbf{H} = 0, \quad \hat{n} \cdot \mathbf{B} = 0$$

**Uniqueness theorem:** A field in a region is uniquely determined by:
- Boundary values of tangential $\mathbf{E}$ or $\mathbf{H}$, OR
- Values at interior sources

**中文：**

波动方程 $\nabla^2\psi + k^2\psi = 0$ 的**平面波**解：

$$\psi(\mathbf{r}) = \psi_0 e^{-j\mathbf{k} \cdot \mathbf{r}}$$

其中 $\mathbf{k}$ 是**波矢量**，$|\mathbf{k}| = k = \omega\sqrt{\mu\epsilon}$。

**色散关系：**
- 非色散：$v_p = \omega/k$ 为常数（真空、STP下的空气）
- 色散：$v_p$ 随 $\omega$ 变化（波导、等离子体、谐振附近的电介质）

**相速度：** $v_p = \omega/k$
**群速度：** $v_g = d\omega/dk$

**波的类型：**
- **均匀平面波：** 等相位面上振幅和相位恒定
- **非均匀平面波：** 等相位面上振幅变化
- **倏逝波：** 衰减（非传播）解，$\beta = 0$，实数 $\alpha$
- **表面波：** 束缚于界面，沿界面传播，远离界面指数衰减
- **泄漏波：** 部分辐射，$\beta$ 为复数

---



---

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



---

---
chapter: 4
title: Plane Wave Functions
source: Roger F. Harrington, Time-Harmonic Electromagnetic Fields, IEEE Press
pages: 144-230
---

# Chapter 4: Plane Wave Functions / 平面波函数

## Section 4-1: The Wave Functions / 波动函数

**English:**

**Separation of variables** is a technique to solve the scalar Helmholtz equation $\nabla^2\psi + k^2\psi = 0$ in various coordinate systems.

In **rectangular coordinates** $(x, y, z)$, we seek solutions of the form:
$$\psi(x,y,z) = X(x)Y(y)Z(z)$$

Substituting into the Helmholtz equation and dividing by $\psi$:
$$\frac{1}{X}\frac{d^2X}{dx^2} + \frac{1}{Y}\frac{d^2Y}{dy^2} + \frac{1}{Z}\frac{d^2Z}{dz^2} = -k^2$$

Since each term depends on only one coordinate, they must each equal a constant. Let:
$$\frac{d^2X}{dx^2} + k_x^2 X = 0 \quad \Rightarrow \quad X = A_+ e^{-jk_x x} + A_- e^{jk_x x}$$
$$\frac{d^2Y}{dy^2} + k_y^2 Y = 0 \quad \Rightarrow \quad Y = B_+ e^{-jk_y y} + B_- e^{jk_y y}$$
$$\frac{d^2Z}{dz^2} + k_z^2 Z = 0 \quad \Rightarrow \quad Z = C_+ e^{-jk_z z} + C_- e^{jk_z z}$$

The **separation equation** relates the separation constants:
$$k_x^2 + k_y^2 + k_z^2 = k^2 \tag{4-5}$$

The elementary wave functions are:
$$\psi_{mnp} = h_m(k_x x)h_n(k_y y)h_p(k_z z) \tag{4-7}$$

where $h$ denotes harmonic functions (sine, cosine, exponential).

**Linear combinations** of elementary wave functions form general solutions:
$$\psi = \sum_{k_x, k_y} B_{k_x k_y} h(k_x x)h(k_y y)h(k_z z) \tag{4-8}$$

**Eigenvalues** $k_x, k_y, k_z$ are determined by boundary conditions.
**Eigenfunctions** are the elementary wave functions corresponding to specific eigenvalues.

**中文：**

**分离变量法**是求解标量亥姆霍兹方程 $\nabla^2\psi + k^2\psi = 0$ 在各种坐标系中的技术。

在**直角坐标系** $(x, y, z)$ 中，我们寻求如下形式解：
$$\psi(x,y,z) = X(x)Y(y)Z(z)$$

代入亥姆霍兹方程并除以 $\psi$：
$$\frac{1}{X}\frac{d^2X}{dx^2} + \frac{1}{Y}\frac{d^2Y}{dy^2} + \frac{1}{Z}\frac{d^2Z}{dz^2} = -k^2$$

由于每一项仅依赖于一个坐标，它们必须各等于一个常数。令：
$$\frac{d^2X}{dx^2} + k_x^2 X = 0 \quad \Rightarrow \quad X = A_+ e^{-jk_x x} + A_- e^{jk_x x}$$

**分离方程**将分离常数联系起来：
$$k_x^2 + k_y^2 + k_z^2 = k^2 \tag{4-5}$$

---

## Section 4-2: Rectangular Waveguides / 矩形波导

**English:**

A **rectangular waveguide** has conducting walls at $x = 0, a$ and $y = 0, b$ with $a > b$.

**TE modes** ($E_z = 0$, $H_z \neq 0$):

$$H_z = H_0 \cos\left(\frac{m\pi x}{a}\right)\cos\left(\frac{n\pi y}{b}\right)e^{-\gamma z}$$

**TM modes** ($H_z = 0$, $E_z \neq 0$):

$$E_z = E_0 \sin\left(\frac{m\pi x}{a}\right)\sin\left(\frac{n\pi y}{b}\right)e^{-\gamma z}$$

**Cutoff wavenumbers:**
$$k_c^2 = \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2$$

**Propagation constant:**
$$\gamma = \sqrt{k_c^2 - k^2} = \alpha + j\beta$$

- If $k > k_c$: $\gamma = j\beta$ (propagating)
- If $k < k_c$: $\gamma = \alpha$ (evanescent, no propagation)

**Cutoff frequency:**
$$f_c = \frac{v}{2}\sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}$$

**Dominant mode (TE10):** $m=1, n=0$, $f_c = c/(2a)$.

**Phase velocity:** $v_p = \omega/\beta > c$
**Group velocity:** $v_g = d\omega/d\beta = c^2/v_p < c$

**Wave impedances:**
$$\eta_{TE} = \frac{\eta}{\sqrt{1 - (f_c/f)^2}} = \eta / \cos\theta_g$$
$$\eta_{TM} = \eta \sqrt{1 - (f_c/f)^2} = \eta \cos\theta_g$$

where $\sin\theta_g = f_c/f$.

**Attenuation in rectangular waveguides:**

Due to conductor losses ($\alpha_c$):
$$\alpha_c \approx \frac{R_s}{b\eta}\frac{1 + \frac{2b}{a}(f_c/f)^2}{\sqrt{1-(f_c/f)^2}}$$

Due to dielectric losses ($\alpha_d$):
$$\alpha_d = \frac{k\tan\delta}{2\sqrt{1-(f_c/f)^2}}$$

**中文：**

**矩形波导**在 $x = 0, a$ 和 $y = 0, b$ 处有导电壁，其中 $a > b$。

**TE模式** ($E_z = 0$, $H_z \neq 0$)：

$$H_z = H_0 \cos\left(\frac{m\pi x}{a}\right)\cos\left(\frac{n\pi y}{b}\right)e^{-\gamma z}$$

**TM模式** ($H_z = 0$, $E_z \neq 0$)：

$$E_z = E_0 \sin\left(\frac{m\pi x}{a}\right)\sin\left(\frac{n\pi y}{b}\right)e^{-\gamma z}$$

**截止波数：**
$$k_c^2 = \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2$$

**主模（TE10）：** $m=1, n=0$, $f_c = c/(2a)$。

---

## Section 4-3: Circular Waveguides / 圆形波导

**English:**

A **circular waveguide** has radius $a$ in cylindrical coordinates $(\rho, \phi, z)$.

**TE modes** ($E_z = 0$, $H_z \neq 0$):
$$H_z = H_0 J_n\left(\frac{p_{nm}\rho}{a}\right)e^{jn\phi}e^{-\gamma z}$$

where $p_{nm}$ is the $m$-th root of $J_n'(x) = 0$ (derivative of Bessel function) for TE modes.

**TM modes** ($H_z = 0$, $E_z \neq 0$):
$$E_z = E_0 J_n\left(\frac{p_{nm}\rho}{a}\right)e^{jn\phi}e^{-\gamma z}$$

where $p_{nm}$ is the $m$-th root of $J_n(x) = 0$ for TM modes.

**Cutoff frequencies for circular waveguide:**

$$f_c = \frac{p_{nm}}{2\pi a\sqrt{\mu\epsilon}}$$

**Dominant TE mode (TE11):** $p_{11} \approx 1.841$ (lowest cutoff for TE modes).

**Attenuation in circular waveguides:**

For TE modes:
$$\alpha_c \approx \frac{R_s}{a\eta}\left(1 + \frac{n^2}{p_{nm}^2 - n^2}\right)$$

For TM modes:
$$\alpha_c \approx \frac{R_s}{a\eta}$$

**Polarization:** Circular waveguide can support two orthogonal polarizations ($e^{j\phi}$ and $e^{-j\phi}$) for the same mode.

**中文：**

**圆形波导**在圆柱坐标系 $(\rho, \phi, z)$ 中半径为 $a$。

**TE模式** ($E_z = 0$, $H_z \neq 0$)：
$$H_z = H_0 J_n\left(\frac{p_{nm}\rho}{a}\right)e^{jn\phi}e^{-\gamma z}$$

其中 $p_{nm}$ 是 $J_n'(x) = 0$ 的第 $m$ 个根（TE模式）。

**主TE模式（TE11）：** $p_{11} \approx 1.841$。

---

## Section 4-4: Waveguide Discontinuities / 波导不连续性

**English:**

Waveguide **discontinuities** occur at junctions, bends, posts, irises, etc. They create reflected and transmitted waves.

**E-plane T-junction:** Series junction where branch couples in E-plane.

**H-plane T-junction:** Shunt junction where branch couples in H-plane.

**E面T形结：** 串联结，分支在E面耦合。
**H面T形结：** 并联结，分支在H面耦合。

**Waveguide irises:** Thin obstacles perpendicular to propagation direction.

**Reactive irises:** Inductive or capacitive posts that create frequency-selective behavior.

**Mode matching:** Discontinuity excites higher-order modes near junction. Far from junction, only propagating modes matter.

**S-matrix formulation:** For a junction between waveguides:
$$[b] = [S][a]$$

where $a$ are incident waves, $b$ are reflected/transmitted waves.

For lossless junction: $[S]$ is unitary ($[S][S]^\dagger = [I]$).

**Step discontinuity:** Junction between waveguides of different cross-sections. Handled by expanding fields in both waveguides in terms of modes and matching boundary conditions.

**中文：**

波导**不连续性**出现在接头、弯头、柱、虹膜等处。它们产生反射和透射波。

**膜片：** 垂直于传播方向的薄障碍物。
**电抗性膜片：** 产生频率选择行为的感性或容性柱。

**模式匹配：** 不连续性在接头附近激发高阶模式。

**S矩阵公式：** 对于波导接头：
$$[b] = [S][a]$$

对于无损耗接头：$[S]$ 是酉矩阵（$[S][S]^\dagger = [I]$）。

---

## Section 4-5: Dielectric Waveguides / 介质波导

**English:**

**Dielectric waveguides** guide waves using total internal reflection at dielectric boundaries, without conducting walls.

**Planar dielectric slab waveguide:** Core of thickness $2d$ with permittivity $\epsilon_1$, surrounded by cladding with $\epsilon_2 < \epsilon_1$.

**Symmetric slab:** Same cladding on both sides.

**Mode condition for symmetric slab (TE modes):**

$$\tan(2k_x d) = \frac{2k_x \alpha}{k_x^2 - \alpha^2}$$

where:
- $k_x = \sqrt{k_1^2 - \beta^2}$ (propagating in core)
- $\alpha = \sqrt{\beta^2 - k_2^2}$ (evanescent in cladding)

**Guided modes exist** when $\beta$ satisfies $k_2 < \beta < k_1$.

**Number of guided modes:**
$$N \approx \left\lfloor \frac{4d}{\lambda_1}\sqrt{n_1^2 - n_2^2} \right\rfloor$$

**Metal-insulator-semiconductor (MIS) waveguides:** Used in integrated optics.

**Optical fibers:** Cylindrical dielectric waveguides for optical communication.

**Step-index fiber:** Core $n_1$, cladding $n_2 < n_1$.

**V-number (归一化频率):**
$$V = k_0 a \sqrt{n_1^2 - n_2^2}$$

**Single-mode condition:** $V < 2.405$ (like step-index fiber with NA and core radius $a$).

**Modal dispersion:** Different modes travel at different velocities.

**中文：**

**介质波导**使用全内反射来导波，无需导电壁。

**平面介质 slab 波导：** 厚度 $2d$ 的芯，介电常数 $\epsilon_1$，被 $\epsilon_2 < \epsilon_1$ 的包层包围。

**对称 slab：** 两面包层相同。

**模式条件（TE模式）：**

$$\tan(2k_x d) = \frac{2k_x \alpha}{k_x^2 - \alpha^2}$$

**导模存在条件：** $\beta$ 满足 $k_2 < \beta < k_1$。

**导模数量：**
$$N \approx \left\lfloor \frac{4d}{\lambda_1}\sqrt{n_1^2 - n_2^2} \right\rfloor$$

---


---

## Section 4-6: Mode Orthogonality / 模式正交性

**English:**

Waveguide modes satisfy **orthogonality** relations that are essential for mode matching and power calculations.

**Orthogonality of TE/TM modes in rectangular waveguide:**

$$\int_0^a \\int_0^b \\mathbf{E}_m \\cdot \\mathbf{E}_n^* \\, dx\\, dy = 0 \\quad \\text{for } m \\neq n$$

$$\int_0^a \\int_0^b \\mathbf{H}_m \\cdot \\mathbf{H}_n^* \\, dx\\, dy = 0 \\quad \\text{for } m \\neq n$$

**Normalization:** Each mode is normalized so that the time-average power crossing any cross-section is unity:

$$\\int_S \\mathbf{S}_m \\cdot \\hat{\\mathbf{z}}\\, dS = 1 \\text{ W}$$

For the **TE$_{mn}$** mode in rectangular waveguide:
$$P_{mn} = \\frac{\\beta_{mn}}{2\\omega\\mu}\\left(\\frac{k_c^2}{k_c^2}\\|\\right) H_0^2 \\cdot \\frac{ab}{4}$$

where $k_c^2 = (m\\pi/a)^2 + (n\\pi/b)^2$.

**Orthogonality integral for modes:**

$$\\int_S (\\mathbf{E}_m \\times \\mathbf{H}_n^*) \\cdot \\hat{\\mathbf{z}}\\, dS = \\delta_{mn}$$

This is critical for the **modal expansion theorem** — any field in a waveguide can be expressed as a sum of orthogonal waveguide modes:

$$\\mathbf{E}_t(x,y,z) = \\sum_n V_n(z)\\mathbf{e}_n(x,y)$$

$$\\mathbf{H}_t(x,y,z) = \\sum_n I_n(z)\\mathbf{h}_n(x,y)$$

where $\\mathbf{e}_n, \\mathbf{h}_n$ are the transverse modal distributions.

**Power orthogonality:** Modes carrying power in different directions are orthogonal with a minus sign:

$$\\int_S (\\mathbf{E}_m \\times \\mathbf{H}_n^*) \\cdot \\hat{\\mathbf{z}}\\, dS = \\begin{cases} +1 & m = n \\text{ (forward)} \\\\ -1 & m = n \\text{ (backward)} \\\\ 0 & m \\neq n \\end{cases}$$

**中文：**

波导模式满足**正交性**关系，这对模式匹配和功率计算至关重要。

**矩形波导中TE/TM模式的正交性：**

$$\\int_0^a \\int_0^b \\mathbf{E}_m \\cdot \\mathbf{E}_n^* \\, dx\\, dy = 0 \\quad (m \\neq n)$$

$$\\int_0^a \\int_0^b \\mathbf{H}_m \\cdot \\mathbf{H}_n^* \\, dx\\, dy = 0 \\quad (m \\neq n)$$

**归一化：** 每个模式归一化，使穿过任何横截面的时间平均功率为1：

$$\\int_S \\mathbf{S}_m \\cdot \\hat{\\mathbf{z}}\\, dS = 1 \\text{ W}$$

这对于**模展开定理**至关重要——波导中的任何场都可以表示为正交波导模式的和：

$$\\mathbf{E}_t(x,y,z) = \\sum_n V_n(z)\\mathbf{e}_n(x,y)$$

---

## Section 4-7: Waveguide Excitation and Coupling / 波导激励与耦合

**English:**

**Waveguide excitation** occurs when a source or discontinuity creates fields in the waveguide.

**Probe excitation:** A coaxial probe extends into the waveguide, exciting primarily the dominant TE10 mode.

**Loop excitation:** A small loop in the waveguide wall couples to the magnetic field.

**Aperture coupling:** A small hole in the waveguide wall couples to another waveguide or cavity.

**Waveguide-to-coaxial transition:** Often implemented as a probe or loop coupler.

**Coupling coefficient for aperture:** For a small circular aperture of radius $r_0$ in a thin conducting wall:

$$C = \\frac{j\\omega\\mu r_0^2}{2}\\left[\\frac{\\partial H_z}{\\partial x} - \\frac{\\partial H_x}{\\partial z}\\right]$$

**E-plane tee junction:** Series junction where signal splits in the E-plane. S-matrix is approximately:

$$[S] = \\begin{pmatrix} 0 & \\frac{1}{\\sqrt{2}} & \\frac{1}{\\sqrt{2}} \\\\ \\frac{1}{\\sqrt{2}} & -\\frac{1}{2} & \\frac{1}{2} \\\\ \\frac{1}{\\sqrt{2}} & \\frac{1}{2} & -\\frac{1}{2} \\end{pmatrix}$$

**H-plane tee junction:** Shunt junction where signal splits in the H-plane. S-matrix is approximately:

$$[S] = \\begin{pmatrix} -\\frac{1}{2} & \\frac{1}{\\sqrt{2}} & \\frac{1}{\\sqrt{2}} \\\\ \\frac{1}{\\sqrt{2}} & 0 & 0 \\\\ \\frac{1}{\\sqrt{2}} & 0 & 0 \\end{pmatrix}$$

**Magic-T (E-H tee):** A 4-port hybrid with complete isolation between E-arm and H-arm. Used in monopulse radar, balanced mixers, and power dividers.

**Cross-guide junction:** 4-port where two waveguides cross at 90°. Mode conversion occurs at the junction.

**Matched load:** Distributed resistive material or vane absorber that absorbs power with low VSWR.

**Short circuit:** Conducting plate. Reflection coefficient $\\Gamma = -1$.

**Rotary joint:** Allows mechanical rotation while maintaining electrical continuity through the waveguide run.

**中文：**

**波导激励**发生在源或不连续性在波导中产生场时。

**探针激励：** 同轴探针伸入波导，主要激励主模TE10。

**环激励：** 波导壁上的小环与磁场耦合。

**孔耦合：** 波导壁上的小孔耦合到另一个波导或腔体。

**E面T形结：** 串联结，信号在E面分开。

**H面T形结：** 并联结，信号在H面分开。

**魔T（E-H T形结）：** 具有E臂和H臂之间完全隔离的4端口混合接头。

---

## Section 4-8: Stripline and Microstrip / 带状线与微带线

**English:**

**Stripline** is a planar transmission line where a conductor is embedded between two ground planes, separated by dielectric.

**Characteristic impedance** of symmetric stripline:

$$Z_0 = \\frac{30\\pi}{\\sqrt{\\epsilon_r}}\\frac{b}{w + 0.441b}$$

where $w$ is the strip width and $b$ is the spacing between ground planes.

For $w/b > 0.35$:
$$Z_0 \\approx \\frac{30\\pi}{\\sqrt{\\epsilon_r}(w/b + 1.441)}$$

**Effective dielectric constant:**
$$\\epsilon_\\text{eff} = \\frac{\\epsilon_r + 1}{2} + \\frac{\\epsilon_r - 1}{2}\\frac{1}{\\sqrt{1 + 12b/w}}$$

**Velocity of propagation:**
$$v = \\frac{c}{\\sqrt{\\epsilon_\\text{eff}}}$$

**Dispersion:** Stripline is relatively dispersion-free for moderate frequencies.

**Microstrip** is a planar line with a conductor on top of a dielectric substrate over a ground plane.

**Characteristic impedance** (quasi-static approximation):
$$Z_0 = \\frac{60}{\\sqrt{\\epsilon_\\text{eff}}}\\ln\\left(\\frac{8h}{w} + \\frac{w}{4h}\\right) \\quad (w/h \\leq 1)$$
$$Z_0 = \\frac{120\\pi}{\\sqrt{\\epsilon_\\text{eff}}}\\frac{1}{w/h + 1.88} \\quad (w/h \\geq 1)$$

**Effective permittivity** (frequency-dependent for microstrip):
$$\\epsilon_\\text{eff}(f) = \\epsilon_r - \\frac{\\epsilon_r - \\epsilon_\\text{eff}(0)}{1 + G(f/f_n)^2}$$

where $f_n = c/(2h\\sqrt{\\epsilon_r - 1})$.

**Microstrip discontinuity effects:**
- Open end: Fringing field equivalent to capacitive load
- Step in width: Equivalent to series capacitance
- Gap: Equivalent to parallel capacitance (coupling)
- Bend: Radiation and current crowding

**Quarter-wave transformer:** Used for matching microstrip to other impedances. Length $\\lambda/4$, characteristic impedance $Z_t = \\sqrt{Z_0 Z_L}$.

**Via holes:** Connect microstrip conductor to ground plane. Equivalent to inductance at high frequencies.

**中文：**

**带状线**是一种平面传输线，导体嵌入两个接地平面之间，被电介质隔开。

**特性阻抗**（对称带状线）：

$$Z_0 = \\frac{30\\pi}{\\sqrt{\\epsilon_r}}\\frac{b}{w + 0.441b}$$

**有效介电常数：**
$$\\epsilon_\\text{eff} = \\frac{\\epsilon_r + 1}{2} + \\frac{\\epsilon_r - 1}{2}\\frac{1}{\\sqrt{1 + 12b/w}}$$

**微带线**是导体在电介质基板上、基板在接地平面上的平面线。

**特性阻抗（准静态近似）：**
$$Z_0 = \\frac{60}{\\sqrt{\\epsilon_\\text{eff}}}\\ln\\left(\\frac{8h}{w} + \\frac{w}{4h}\\right) \\quad (w/h \\leq 1)$$

**微带不连续性效应：**
- 开路端：等效于电容负载的边缘场
- 宽度阶梯：等效于串联电容
- 间隙：等效于并联电容（耦合）

---



---

---
chapter: 5
title: Cylindrical Wave Functions
source: Roger F. Harrington, Time-Harmonic Electromagnetic Fields, IEEE Press
pages: 199-290
---

# Chapter 5: Cylindrical Wave Functions / 柱面波函数

## Section 5-1: The Wave Functions / 波动函数

**English:**

In **cylindrical coordinates** $(\rho, \phi, z)$, the scalar Helmholtz equation is:

$$\frac{1}{\rho}\frac{\partial}{\partial\rho}\left(\rho\frac{\partial\psi}{\partial\rho}\right) + \frac{1}{\rho^2}\frac{\partial^2\psi}{\partial\phi^2} + \frac{\partial^2\psi}{\partial z^2} + k^2\psi = 0 \tag{5-1}$$

Using **separation of variables** $\psi(\rho, \phi, z) = R(\rho)\Phi(\phi)Z(z)$:

$$\frac{1}{R}\frac{d}{d\rho}\left(\rho\frac{dR}{d\rho}\right) + \frac{1}{\rho^2\Phi}\frac{d^2\Phi}{d\phi^2} + \frac{1}{Z}\frac{d^2Z}{dz^2} + k^2 = 0$$

This yields three equations:
1. **Z-equation:** $\frac{d^2Z}{dz^2} + k_z^2 Z = 0$ → $Z = e^{\pm jk_z z}$
2. **$\Phi$-equation:** $\frac{d^2\Phi}{d\phi^2} + n^2\Phi = 0$ → $\Phi = e^{jn\phi}$ ($n$ integer for single-valuedness)
3. **R-equation:** $\frac{d^2R}{d\rho^2} + \frac{1}{\rho}\frac{dR}{d\rho} + (k_\rho^2 - \frac{n^2}{\rho^2})R = 0$ → **Bessel's equation**

**Bessel's equation** of order $n$:
$$\rho^2\frac{d^2R}{d\rho^2} + \rho\frac{dR}{d\rho} + (k_\rho^2\rho^2 - n^2)R = 0 \tag{5-5}$$

**Solutions to Bessel's equation:**
$$R = B_1 J_n(k_\rho\rho) + B_2 N_n(k_\rho\rho) \quad \text{(bounded at origin)}$$
$$R = B_3 H_n^{(1)}(k_\rho\rho) + B_4 H_n^{(2)}(k_\rho\rho) \quad \text{(radiation condition)}$$

where:
- $J_n$ = **Bessel function of first kind** (finite at $\rho = 0$)
- $N_n$ = **Bessel function of second kind** (singular at $\rho = 0$)
- $H_n^{(1)}$ = **Hankel function of first kind** (outgoing waves as $\rho \to \infty$)
- $H_n^{(2)}$ = **Hankel function of second kind** (incoming waves as $\rho \to \infty$)

**Separation constant relation:**
$$k_\rho^2 + k_z^2 = k^2 \tag{5-6}$$

**Elementary wave functions:**
$$\psi_{nmp}(\rho, \phi, z) = B_n(k_\rho\rho)e^{jn\phi}h_p(k_z z) \tag{5-9}$$

**Modified Bessel functions** for evanescent ($\gamma$) waves:
$$I_n(x) = j^{-n} J_n(jx) \quad K_n(x) = \text{modified } N_n(x)$$

**Asymptotic behavior:**

For large $x$:
$$J_n(x) \approx \sqrt{\frac{2}{\pi x}}\cos\left(x - \frac{n\pi}{2} - \frac{\pi}{4}\right)$$
$$H_n^{(2)}(x) \approx \sqrt{\frac{2}{\pi x}}e^{-j\left(x - \frac{n\pi}{2} - \frac{\pi}{4}\right)}$$

**Bessel function identities:**
$$J_{-n}(x) = (-1)^n J_n(x)$$
$$H_{-n}^{(2)}(x) = (-1)^n H_n^{(2)}(x)$$

**中文：**

在**圆柱坐标系** $(\rho, \phi, z)$ 中，标量亥姆霍兹方程为：
$$\frac{1}{\rho}\frac{\partial}{\partial\rho}\left(\rho\frac{\partial\psi}{\partial\rho}\right) + \frac{1}{\rho^2}\frac{\partial^2\psi}{\partial\phi^2} + \frac{\partial^2\psi}{\partial z^2} + k^2\psi = 0 \tag{5-1}$$

分离变量 $\psi(\rho, \phi, z) = R(\rho)\Phi(\phi)Z(z)$ 得到三个方程，其中 $R$-方程为**贝塞尔方程**：
$$\rho^2\frac{d^2R}{d\rho^2} + \rho\frac{dR}{d\rho} + (k_\rho^2\rho^2 - n^2)R = 0 \tag{5-5}$$

**贝塞尔方程的解：**
$$R = B_1 J_n(k_\rho\rho) + B_2 N_n(k_\rho\rho) \quad \text{（有界于原点）}$$

其中：
- $J_n$ = **第一类贝塞尔函数**（在 $\rho = 0$ 处有限）
- $N_n$ = **第二类贝塞尔函数**（在 $\rho = 0$ 处奇异）
- $H_n^{(1)}$ = **第一类汉克尔函数**（外向波）
- $H_n^{(2)}$ = **第二类汉克尔函数**（内向波）

---

## Section 5-2: Circular Waveguides (Cylindrical) / 圆形波导（柱面）

**English:**

**Circular cylindrical waveguide** of radius $a$ supports TE and TM modes.

**TE modes** ($E_z = 0$, $H_z \neq 0$):
$$H_z = H_0 J_n\left(\frac{p_{nm}\rho}{a}\right)e^{jn\phi}e^{-\gamma z}$$

where $p_{nm}$ is the $m$-th root of $J_n'(x) = 0$.

**TM modes** ($H_z = 0$, $E_z \neq 0$):
$$E_z = E_0 J_n\left(\frac{p_{nm}\rho}{a}\right)e^{jn\phi}e^{-\gamma z}$$

where $p_{nm}$ is the $m$-th root of $J_n(x) = 0$.

**Characteristic roots:**

| Mode | Root equation | $p_{nm}$ example |
|------|-------------|-----------------|
| TE$_{nm}$ | $J_n'(p_{nm}) = 0$ | $p_{01} = 3.832$ |
| TM$_{nm}$ | $J_n(p_{nm}) = 0$ | $p_{01} = 2.405$ |

**Dominant circular waveguide mode:** TE11 ($p_{11} = 1.841$)

**Cutoff frequency:**
$$f_c = \frac{p_{nm}}{2\pi a\sqrt{\mu\epsilon}}$$

**Attenuation constants:**
$$\alpha_c \approx \frac{R_s}{a\eta}\left(1 + \frac{n^2}{p_{nm}^2 - n^2}\right) \quad \text{(TE)}$$
$$\alpha_c \approx \frac{R_s}{a\eta} \quad \text{(TM)}$$

**Polarization degeneracy:** For circular waveguide with $n \neq 0$, modes have two orthogonal polarizations ($\cos n\phi$ and $\sin n\phi$) with same cutoff.

**中文：**

半径为 $a$ 的**圆形柱面波导**支持 TE 和 TM 模式。

**TE模式** ($E_z = 0$, $H_z \neq 0$)：
$$H_z = H_0 J_n\left(\frac{p_{nm}\rho}{a}\right)e^{jn\phi}e^{-\gamma z}$$

其中 $p_{nm}$ 是 $J_n'(x) = 0$ 的第 $m$ 个根。

**主圆形波导模式：** TE11 ($p_{11} = 1.841$)

**极化简并：** 对于 $n \neq 0$，模式具有两个正交极化（$\cos n\phi$ 和 $\sin n\phi$），截止频率相同。

---

## Section 5-3: Circular Cavity Resonators / 圆形腔体谐振器

**English:**

A **circular cylindrical cavity** of radius $a$ and height $d$ has resonant modes.

**Resonant frequencies:**
$$f_{nmp} = \frac{1}{2\pi\sqrt{\mu\epsilon}}\sqrt{\left(\frac{p_{nm}}{a}\right)^2 + \left(\frac{q\pi}{d}\right)^2}$$

where $p_{nm}$ is the root of Bessel function (TM or TE), and $q$ is the axial mode number.

**TM modes in circular cavity:**
$$E_z = E_0 J_n\left(\frac{p_{nm}\rho}{a}\right)\cos\left(\frac{q\pi z}{d}\right)e^{jn\phi}$$

**TE modes in circular cavity:**
$$H_z = H_0 J_n\left(\frac{p_{nm}'\rho}{a}\right)\sin\left(\frac{q\pi z}{d}\right)e^{jn\phi}$$

where $p_{nm}'$ is the root of $J_n'(x) = 0$.

**Quality factor Q:**

For conducting walls with conductivity $\sigma$:
$$Q = \frac{\omega W}{P_\text{loss}}$$

where $W$ is stored energy and $P_\text{loss}$ is power dissipated in walls.

For circular cavity TM modes:
$$Q_{nmq} \approx \frac{(p_{nm})^2 a}{2R_s\delta_s\left(p_{nm}^2 + \left(\frac{n\pi a}{d}\right)^2\right)}$$

where $R_s = \sqrt{\omega\mu/(2\sigma)}$ is the surface resistance and $\delta_s = \sqrt{2/(\omega\mu\sigma)}$ is the skin depth.

**Dominant mode of circular cavity:** TM010 ($f \approx 1.203c/(2a)$, $Q \approx 2.05a/\delta_s$)

**TM011:** Useful for dielectric resonator measurements (high Q, electric field concentrated in dielectric sample).

**中文：**

半径 $a$ 和高度 $d$ 的**圆形柱面腔体**具有谐振模式。

**谐振频率：**
$$f_{nmp} = \frac{1}{2\pi\sqrt{\mu\epsilon}}\sqrt{\left(\frac{p_{nm}}{a}\right)^2 + \left(\frac{q\pi}{d}\right)^2}$$

**品质因数 Q：**

对于导电壁：
$$Q = \frac{\omega W}{P_\text{loss}}$$

**圆形腔的主模式：** TM010 ($f \approx 1.203c/(2a)$)

---

## Section 5-4: Aperture Coupling and Slot Antennas / 孔耦合与缝隙天线

**English:**

**Aperture coupling** through a small hole in a conducting wall can be analyzed using **equivalence principle**.

**Babinet principle:** The fields from a complementary screen (aperture replaced by obstacle and vice versa) are related.

For a slot of length $L$ in a conducting plane, the complementary structure is a thin dipole of length $L$.

**Radiation from narrow slot:**
For a narrow slot of width $w \ll L$ and length $L \approx \lambda/2$:
$$E_z \approx \frac{V}{w} \sin\left(\frac{\pi z}{L}\right) \quad (|z| < L/2)$$

The magnetic current on the slot is:
$$M_s = -2\hat{n} \times E_\text{slot}$$

**Half-wave slot antenna:** $L = \lambda/2$, radiation pattern similar to dipole but with orthogonal polarization.

**Resonant slot:** At resonance, input conductance $G \approx 0.32$ S for narrow transverse slots in X-band waveguide.

**Radiating waveguide slots:** Slots cut in waveguide walls to couple power. Condition for radiation: slot must cut current path on waveguide surface.

**Longitudinal shunt slot:** Equivalent to series R-L branch.
**Transverse shunt slot:** Equivalent to shunt R-L branch.

**中文：**

**孔耦合**通过导电壁上的小孔，可以使用**等效原理**分析。

**巴比涅原理：** 互补屏幕（孔与障碍物互换）的场相互关联。

对于长度为 $L$ 的缝隙，互补结构是长度为 $L$ 的细偶极子。

**窄缝辐射：**
$$E_z \approx \frac{V}{w} \sin\left(\frac{\pi z}{L}\right) \quad (|z| < L/2)$$

---


---

## Section 5-5: Dielectric Rod Waveguide / 介质杆波导

**English:**

A **dielectric rod** can guide waves using total internal reflection, similar to optical fibers.

**Step-index circular rod:** Core of radius $a$, index $n_1$, surrounded by cladding $n_2 < n_1$.

**Guided modes:** For weak guidance ($n_1 \\approx n_2$), HE modes with approximate field distributions.

**Scalar wave equation** for the rod:
$$\\frac{d^2\\psi}{dr^2} + \\frac{1}{r}\\frac{d\\psi}{dr} + (k_0^2 n^2(r) - \\beta^2 - \\frac{n^2}{r^2})\\psi = 0$$

**V-number** for step-index fiber:
$$V = k_0 a \\sqrt{n_1^2 - n_2^2} = \\frac{2\\pi a}{\\lambda_0}\\sqrt{n_1^2 - n_2^2}$$

**Number of guided modes:**
- Single-mode condition: $V < 2.405$
- Multi-mode: approximately $M \\approx V^2/2$ for large $V$

**Hybrid modes in circular fiber:**
- **HE$_{nm}$**: Predominantly electric field axial component
- **EH$_{nm}$**: Predominantly magnetic field axial component
- **TE$_{0m}$**, **TM$_{0m}$**: Circularly symmetric modes

**Bessel function solutions:** Inside the rod, $J_n(u\\rho/a)$ is used. Outside, modified Bessel $K_n(w\\rho/a)$ for evanescent decay.

**Characteristic equation** for HE modes:
$$\\frac{uJ_{n-1}(u)}{J_n(u)} = \\frac{w K_{n-1}(w)}{K_n(w)}$$

where:
$$u^2 = a^2(k_0^2 n_1^2 - \\beta^2)$$
$$w^2 = a^2(\\beta^2 - k_0^2 n_2^2)$$

**Attenuation in dielectric waveguides:** Due to dielectric loss ($\\tan\\delta$):

$$\\alpha_d = \\frac{k_0 n_1 \\sin^2\\theta_m}{2\\beta}\\tan\\delta$$

where $\\theta_m$ is the mode angle with respect to the axis.

**中文：**

**介质杆**可以使用全内反射导波，类似于光纤。

**阶跃折射率圆杆：** 半径 $a$，折射率 $n_1$，被 $n_2 < n_1$ 的包层包围。

**导模：** 对于弱导 ($n_1 \\approx n_2$)，使用 HE 模式。

**V数**（阶跃光纤）：
$$V = k_0 a \\sqrt{n_1^2 - n_2^2} = \\frac{2\\pi a}{\\lambda_0}\\sqrt{n_1^2 - n_2^2}$$

**导模数量：**
- 单模条件：$V < 2.405$
- 多模：大约 $M \\approx V^2/2$

**特征方程（HE模式）：**
$$\\frac{uJ_{n-1}(u)}{J_n(u)} = \\frac{w K_{n-1}(w)}{K_n(w)}$$

---

## Section 5-6: Cylindrical Waveguide Coupling / 柱面波导耦合

**English:**

**Mode coupling** in cylindrical waveguides occurs at discontinuities and bends.

**Coupled-mode theory:** For two weakly coupled waveguides:

$$\\frac{da_1}{dz} = -j\\beta_1 a_1 + jC_{12} a_2$$
$$\\frac{da_2}{dz} = -j\\beta_2 a_2 + jC_{21} a_1$$

where $C_{ij}$ is the coupling coefficient.

**Synchronous coupling:** When $\\beta_1 = \\beta_2$, maximum power exchange occurs over the **coupling length**:
$$L_c = \\frac{\\pi}{2|C|}$$

**Directional coupler:** Two parallel waveguides coupled over a length $L$. Power transfer:

$$P_2(L) = P_1(0)\\sin^2(|C|L)$$

**Straight directional coupler:** For weak coupling, $P_2/P_1 = (\\pi/2)(L/L_c)^2$ when $L \\ll L_c$.

**Overcoupled regime:** Maximum coupling occurs at $L = L_c/2$, where complete power transfer is possible.

**Bend coupling:** In curved waveguides, mode conversion occurs due to curvature. Power radiates at a rate:

$$\\alpha_\\text{bend} \\approx \\frac{1}{2R}\\left(\\frac{\\lambda}{a}\\right)^2$$

for $a \\gg \\lambda$ and radius $R$.

**Transition radiation:** Due to gradual or sudden changes in waveguide dimensions.

**中文：**

**模式耦合**发生在不连续性和弯头处。

**耦合模理论：** 对于两个弱耦合波导：

$$\\frac{da_1}{dz} = -j\\beta_1 a_1 + jC_{12} a_2$$
$$\\frac{da_2}{dz} = -j\\beta_2 a_2 + jC_{21} a_1$$

**同步耦合：** 当 $\\beta_1 = \\beta_2$ 时，最大功率交换发生在**耦合长度**：
$$L_c = \\frac{\\pi}{2|C|}$$

**定向耦合器：** 两个平行波导在长度 $L$ 上耦合。

---

## Section 5-7: Cylindrical Cavity Filters / 柱面腔体滤波器

**English:**

**Cylindrical cavity filters** use resonant modes in cylindrical cavities to create band-pass or band-stop filters.

**TM010 mode** in circular waveguide (closed at both ends):
$$f_c = \\frac{1.203c}{2\\pi a} = \\frac{1.203}{2\\pi a\\sqrt{\\mu\\epsilon}}$$

**Iris-coupled cylindrical cavities:** Coupling iris between cavities controls coupling coefficient.

**Coupling coefficient for iris:**
$$k = \\frac{\\omega L}{2} \\quad \\text{(for inductive iris)}$$

where $L$ is the normalized iris reactance.

**Filter synthesis using cylindrical cavities:**

1. **Chebyshev filter:** Equal ripple passband, specified return loss
2. **Cavity Q:** $Q_c = \\omega W/P_\\text{loss}$ (conductor dominated)
3. **External Q:** $Q_e = g_0 g_1/FBW$ for input/output coupling

**Dual-mode cylindrical cavities:** Each cavity supports two orthogonal modes that can be coupled to form a 4-pole filter without extra cavities.

**Tuning:** Cylindrical cavities have screw tuners for fine adjustment of resonant frequency.

**Temperature stability:** Cavity filters have excellent temperature stability when made of low-expansion materials (Invar, superinvar).

**中文：**

**柱面腔体滤波器**使用柱面腔中的谐振模式来创建带通或带阻滤波器。

**TM010模式**在圆波导中（两端封闭）：
$$f_c = \\frac{1.203c}{2\\pi a}$$

**iris耦合柱面腔体：** 腔体之间的耦合iris控制耦合系数。

**滤波器综合：** 
1. **切比雪夫滤波器：** 等纹波通带，指定回波损耗
2. **腔体Q：** $Q_c = \\omega W/P_\\text{loss}$（由导体损耗主导）
3. **外部Q：** $Q_e = g_0 g_1/FBW$ 用于输入/输出耦合

---



---

---
chapter: 6
title: Spherical Wave Functions
source: Roger F. Harrington, Time-Harmonic Electromagnetic Fields, IEEE Press
pages: 299-380
---

# Chapter 6: Spherical Wave Functions / 球面波函数

## Section 6-1: The Wave Functions / 波动函数

**English:**

In **spherical coordinates** $(r, \theta, \phi)$, the scalar Helmholtz equation is:

$$\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial\psi}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial\psi}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2\psi}{\partial\phi^2} + k^2\psi = 0$$

Using **separation of variables** $\psi(r, \theta, \phi) = R(r)\Theta(\theta)\Phi(\phi)$:

**Spherical Bessel equation** for $R(r)$:
$$r^2\frac{d^2R}{dr^2} + 2r\frac{dR}{dr} + [k^2r^2 - n(n+1)]R = 0$$

**Solutions — Spherical Bessel functions:**
$$j_n(kr) = \sqrt{\frac{\pi}{2kr}} J_{n+1/2}(kr) \quad \text{(spherical Bessel of 1st kind)}$$
$$n_n(kr) = \sqrt{\frac{\pi}{2kr}} N_{n+1/2}(kr) \quad \text{(spherical Bessel of 2nd kind)}$$
$$h_n^{(1)}(kr) = j_n(kr) + jn_n(kr) \quad \text{(spherical Hankel of 1st kind)}$$
$$h_n^{(2)}(kr) = j_n(kr) - jn_n(kr) \quad \text{(spherical Hankel of 2nd kind)}$$

**Associated Legendre equation** for $\Theta(\theta)$:
$$\frac{1}{\sin\theta}\frac{d}{d\theta}\left(\sin\theta\frac{d\Theta}{d\theta}\right) + \left[n(n+1) - \frac{m^2}{\sin^2\theta}\right]\Theta = 0$$

**Solutions — Associated Legendre functions:**
$$\Theta = P_n^m(\cos\theta), \quad \Phi = e^{jm\phi}$$

where $P_n^m$ is the **associated Legendre function** of degree $n$ and order $m$.

**Elementary spherical wave functions:**
$$\psi_{emn}(r, \theta, \phi) = h_n^{(1)}(kr)Y_n^m(\theta, \phi) \quad \text{(outgoing spherical wave)}$$
$$\psi_{smn}(r, \theta, \phi) = j_n(kr)Y_n^m(\theta, \phi) \quad \text{(standing spherical wave)}$$

where $Y_n^m(\theta, \phi) = P_n^m(\cos\theta)e^{jm\phi}$ is the **spherical harmonic**.

**Spherical wave expansion of plane wave:**
$$e^{-jkz} = \sum_{n=0}^{\infty} (-1)^n (2n+1) j_n(kr) P_n(\cos\theta)$$

**中文：**

在**球坐标系** $(r, \theta, \phi)$ 中，标量亥姆霍兹方程分离变量得到：

**球贝塞尔方程**：
$$r^2\frac{d^2R}{dr^2} + 2r\frac{dR}{dr} + [k^2r^2 - n(n+1)]R = 0$$

**解 — 球贝塞尔函数：**
$$j_n(kr) = \sqrt{\frac{\pi}{2kr}} J_{n+1/2}(kr) \quad \text{（第一类球贝塞尔）}$$
$$n_n(kr) = \sqrt{\frac{\pi}{2kr}} N_{n+1/2}(kr) \quad \text{（第二类球贝塞尔）}$$
$$h_n^{(1)}(kr) = j_n(kr) + jn_n(kr) \quad \text{（第一类球汉克尔）}$$

**球谐函数**：
$$Y_n^m(\theta, \phi) = P_n^m(\cos\theta)e^{jm\phi}$$

---

## Section 6-2: Spherical Waveguide / 球面波导

**English:**

**Spherical waveguides** have boundaries at $r = a$ (concentric spherical shells).

**Field representations:**

For TM modes ($E_r \neq 0$, $H_r = 0$):
$$E_r = \frac{1}{r^2}\frac{d}{dr}[rh_n^{(1)}(kr)]\Theta(\theta)\Phi(\phi)$$

For TE modes ($H_r \neq 0$, $E_r = 0$):
$$H_r = \frac{n(n+1)}{r^2} h_n^{(1)}(kr) P_n^m(\cos\theta)e^{jm\phi}$$

**Boundary condition** at perfectly conducting spherical shell $r = a$:
- TE modes: $\frac{\partial}{\partial r}[rh_n^{(1)}(kr)] = 0$ at $r = a$
- TM modes: $h_n^{(1)}(ka) = 0$ at $r = a$

**Spherical cavity resonator:** Conducting spherical shell at $r = a$.

TM mode resonances:
$$j_n(k_{nm}a) = 0 \Rightarrow k_{nm}a = p_{nm} \quad (p_{nm} = \text{zero of } J_{n+1/2})$$

TE mode resonances:
$$\frac{d}{dr}[rh_n^{(1)}(kr)] = 0 \text{ at } r = a$$

**Quality factor of spherical cavity:**
$$Q_{nmp} \approx \frac{\delta_s}{a} \frac{n(n+1)}{2n+1}$$

**Dominant mode (TE101-like spherical):** Lowest Q mode.

**TE modes** have no field singularities at $r = 0$ (finite for all $n \geq 1$).
**TM modes** have $E_r \to \infty$ at $r = 0$ for $n \geq 1$ (except $n=0$).

**中文：**

**球面波导**在 $r = a$ 处有边界（同心球壳）。

**球形腔体谐振器：** 导电球壳在 $r = a$ 处。

TM模式谐振：
$$j_n(k_{nm}a) = 0 \Rightarrow k_{nm}a = p_{nm}$$

---

## Section 6-3: Spherical Cavities and Mie Scattering / 球形腔体与米氏散射

**English:**

**Mie scattering** is the exact solution for scattering by a homogeneous sphere of radius $a$.

**Total field decomposition:**

**Incident field** (plane wave along $z$-axis):
$$\mathbf{E}^i = \hat{x}E_0 e^{-jkr\cos\theta} = E_0 \sum_{n=1}^{\infty} \frac{2n+1}{n(n+1)}[j_n(kr)\hat{\theta} \cdot \mathbf{M}_{o1n} - \frac{1}{k}\frac{d}{dr}(kr j_n(kr))\hat{\phi} \cdot \mathbf{N}_{e1n}]$$

**Scattered field** (outgoing spherical waves):
$$\mathbf{E}^s = E_0 \sum_{n=1}^{\infty} \frac{2n+1}{n(n+1)}[a_n j_n(kr) + b_n h_n^{(1)}(kr)]\mathbf{M}_{o1n} + [b_n j_n(kr) + a_n h_n^{(1)}(kr)]\mathbf{N}_{e1n}$$

**Internal field** (inside sphere):
$$\mathbf{E}^\text{int} = E_0 \sum_{n=1}^{\infty} c_n j_n(k_1 r)\mathbf{M}_{o1n} + d_n j_n(k_1 r)\mathbf{N}_{e1n}$$

where $k_1 = \omega\sqrt{\mu_1\epsilon_1}$.

**Scattering coefficients $a_n, b_n$:**

For a sphere with refractive index $m = n_1/n_2$:
$$a_n = \frac{jn_n(x) - mx h_n^{(2)}(mx)}{jn_n(x) - mx h_n^{(2)}(mx)} \quad \text{(TM modes)}$$
$$b_n = \frac{[mx j_n(mx)]' - nj_n(x)}{[mx h_n^{(2)}(mx)]' - nh_n^{(2)}(x)} \quad \text{(TE modes)}$$

where $x = ka$ is the **size parameter**.

**Optical efficiency factors:**

**Extinction efficiency:**
$$Q_\text{ext} = \frac{2}{x^2}\sum_{n=1}^{\infty}(2n+1)\text{Re}\{a_n + b_n\}$$

**Scattering efficiency:**
$$Q_\text{sca} = \frac{2}{x^2}\sum_{n=1}^{\infty}(2n+1)(|a_n|^2 + |b_n|^2)$$

**Absorption efficiency:**
$$Q_\text{abs} = Q_\text{ext} - Q_\text{sca}$$

**Asymptotic limits:**

- **Rayleigh scattering** ($x \ll 1$): $Q_\text{sca} \propto x^4$, $\sigma \propto 1/\lambda^4$
- **Mie regime** ($x \sim 1$): Complex resonance structure
- **Geometric optics** ($x \gg 1$): $Q_\text{sca} \to 2$ (extinction = 2 × geometric cross-section due to shadow)

**Forward scattering (Mie):** Sharp forward peak at large $x$.

**Rainbow angle:** For water droplets ($n \approx 1.333$), rainbow occurs at $\theta \approx 138°$.

**Resonant modes (Mie resonances):** Sphere acts as a dielectric resonator, supporting resonances at specific $x$ values.

**中文：**

**米氏散射**是球形均匀散射体的精确解。

**总场分解：**

**入射场**（沿 $z$ 轴的平面波）：
$$\mathbf{E}^i = E_0 e^{-jkz}\hat{x}$$

**散射场**（外向球面波）：
$$\mathbf{E}^s = E_0 \sum_{n=1}^{\infty} \frac{2n+1}{n(n+1)}[a_n \mathbf{M}_{o1n} + b_n \mathbf{N}_{e1n}]h_n^{(1)}(kr)$$

**散射系数 $a_n, b_n$：**

对于折射率 $m = n_1/n_2$ 的球体：
$$a_n = \frac{jn_n(x) - mx h_n^{(2)}(mx)}{...} \quad \text{（TM模式）}$$

其中 $x = ka$ 是**尺寸参数**。

**光学效率因子：**

**消光效率：**
$$Q_\text{ext} = \frac{2}{x^2}\sum_{n=1}^{\infty}(2n+1)\text{Re}\{a_n + b_n\}$$

**散射效率：**
$$Q_\text{sca} = \frac{2}{x^2}\sum_{n=1}^{\infty}(2n+1)(|a_n|^2 + |b_n|^2)$$

**极限情况：**

- **瑞利散射** ($x \ll 1$): $Q_\text{sca} \propto x^4$
- **米氏区** ($x \sim 1$): 复杂共振结构
- **几何光学** ($x \gg 1$): $Q_\text{sca} \to 2$

---


---

## Section 6-4: Spherical Antenna Theory / 球面天线理论

**English:**

**Spherical waves** are the natural solution for radiation and scattering problems involving spherical geometry.

**Expansion of plane wave in spherical waves:**
$$e^{-jk\\hat{r}\\cdot\\mathbf{r}_0} = \\sum_{n=0}^{\\infty} (2n+1)(-j)^n j_n(kr_0) P_n(\\cos\\theta)$$

where $r_0$ is the distance from origin to source point.

**Dipole radiation patterns:**
For a small dipole (Hertzian dipole) of length $l$ and current $I_0$:

$$\\mathbf{E}_\\theta = \\frac{j\\omega\\mu_0 I_0 l}{4\\pi r}\\sin\\theta\\, e^{-jkr}$$
$$\\mathbf{H}_\\phi = \\frac{j k I_0 l}{4\\pi r}\\sin\\theta\\, e^{-jkr}$$

**Total radiated power:**
$$P_\\text{rad} = \\frac{\\eta_0 k^2 |I_0 l|^2}{12\\pi} = \\frac{\\pi}{3}\\left(\\frac{l}{\\lambda}\\right)^2 |I_0|^2 R_\\text{rad}$$

**Radiation resistance:**
$$R_\\text{rad} = 20\\pi^2 \\left(\\frac{l}{\\lambda}\\right)^2 \\quad \\Omega$$

**Multipole expansion:** Any radiation pattern can be expanded in spherical wave functions:
$$\\mathbf{E} = \\sum_{n=1}^{\\infty} \\sum_{m=-n}^{n} \\left[ a_{mn} \\mathbf{M}_{mn} + b_{mn} \\mathbf{N}_{mn} \\right]$$

where $\\mathbf{M}_{mn}$ and $\\mathbf{N}_{mn}$ are vector spherical wave functions.

**Spherical mode amplitudes** determine directivity pattern.

**Antenna Q factor** for small spherical antenna:
$$Q = \\frac{1}{k a}^3 \\quad (\\text{for } ka \\ll 1)$$

where $a$ is the antenna radius.

**Active sourcing:** For active antenna analysis, add source term $\\mathbf{J}_\\text{source}$.

**Chinese:**

**球面波**是涉及球面几何的辐射和散射问题的自然解。

**平面波的球面波展开：**
$$e^{-jk\\hat{r}\\cdot\\mathbf{r}_0} = \\sum_{n=0}^{\\infty} (2n+1)(-j)^n j_n(kr_0) P_n(\\cos\\theta)$$

**偶极子辐射方向图：**
对于长度为 $l$、电流为 $I_0$ 的小偶极子：

$$\\mathbf{E}_\\theta = \\frac{j\\omega\\mu_0 I_0 l}{4\\pi r}\\sin\\theta\\, e^{-jkr}$$

**辐射电阻：**
$$R_\\text{rad} = 20\\pi^2 \\left(\\frac{l}{\\lambda}\\right)^2 \\quad \\Omega$$

---

## Section 6-5: Spherical Scatterers and Radar Cross Section / 球面散射体与雷达截面

**English:**

**Radar cross section (RCS)** of a sphere is the canonical scattering problem.

**Mie scattering solution:**
$$\\sigma_\\text{back} = \\frac{\\lambda^2}{\\pi}\\left| \\sum_{n=1}^{\\infty} (-1)^n (2n+1)(a_n - b_n) \\right|^2$$

**Backscatter RCS:**
$$\\sigma = \\pi a^2 |\\Gamma|^2$$

where $\\Gamma$ is the reflection coefficient.

**Forward scatter:** $\\sigma_\\text{forward} = 4\\pi a^2$ at large $ka$.

**Optical theorem:** Relates extinction cross section to forward scattering amplitude:
$$\\sigma_\\text{ext} = \\frac{4\\pi}{k} \\text{Im}\\{f(0)\\}$$

**Low-frequency limit (Rayleigh scattering):** For $ka \\ll 1$:
$$\\sigma = \\frac{9\\pi a^2}{(ka)^4}|\\epsilon_r - 1|^2$$

**Resonant region:** $ka \\sim 1$, complex modal interaction.

**Physical optics approximation:** For large spheres ($ka \\gg 1$):
$$\\sigma \\approx \\pi a^2$$

**Shadow sector:** The forward scatter exceeds geometric cross section by factor of 4 (optical cross section = 4 times geometric).

**Bistatic radar:** RCS at angles other than backscatter.

**Chinese:**

**雷达截面（RCS）**的球体是典型的散射问题。

**米氏散射解：**
$$\\sigma_\\text{back} = \\frac{\\lambda^2}{\\pi}\\left| \\sum_{n=1}^{\\infty} (-1)^n (2n+1)(a_n - b_n) \\right|^2$$

**后向散射RCS：**
$$\\sigma = \\pi a^2 |\\Gamma|^2$$

**光学定理：** 消光截面与前向散射振幅相关：
$$\\sigma_\\text{ext} = \\frac{4\\pi}{k} \\text{Im}\\{f(0)\\}$$

**低频极限（瑞利散射）：** 对于 $ka \\ll 1$：
$$\\sigma = \\frac{9\\pi a^2}{(ka)^4}|\\epsilon_r - 1|^2$$

---

## Section 6-6: Spherical Cavity Resonators / 球面腔体谐振器

**English:**

**Spherical cavity** with conducting walls at radius $a$.

**Resonant modes:**

**TM modes** ($H_r = 0$): $j_n(k_{nm}a) = 0$ → $k_{nm}a = p_{nm}$
**TE modes** ($E_r = 0$): $[kj_n(k a)]' = 0$ → $k_{nm}a = p'_{nm}$

**TM$_{nmp}$ modes:**
$$f_{nmp} = \\frac{c}{2\\pi a}\\sqrt{p_{nm}^2 + \\left(\\frac{p\\pi a}{d}\\right)^2}$$

**TE$_{nmp}$ modes:**
$$f_{nmp} = \\frac{c}{2\\pi a}\\sqrt{p'_{nm}^2 + \\left(\\frac{p\\pi a}{d}\\right)^2}$$

where $p$ is the radial mode number.

**Quality factor** for spherical cavity:
$$Q_{nmp} = \\frac{\\omega_{nmp} W}{P_\\text{loss}} \\approx \\frac{\\eta_0}{R_s}(ka)$$

for the dominant TE mode with $ka \\gg 1$.

**Spherical reflector antennas:** Use spherical wave expansion to analyze feed radiation and reflector interaction.

**Spherical harmonic functions** are also used in global wave propagation, ionospheric modeling, and seismic wave analysis.

**Chinese:**

**球形腔体**在半径 $a$ 处有导电壁。

**谐振模式：**

**TM模式** ($H_r = 0$): $j_n(k_{nm}a) = 0$ → $k_{nm}a = p_{nm}$
**TE模式** ($E_r = 0$): $[kj_n(k a)]' = 0$ → $k_{nm}a = p'_{nm}$

**球形反射器天线：** 使用球面波展开来分析馈源辐射和反射器相互作用。

---



---

---
chapter: 7
title: Perturbational and Variational Techniques
source: Roger F. Harrington, Time-Harmonic Electromagnetic Fields, IEEE Press
pages: 401-500
---

# Chapter 7: Perturbational and Variational Techniques / 微扰法与变分法

## Section 7-1: Introduction / 引言

**English:**

Many practical problems cannot be solved exactly. **Perturbational** and **variational** techniques provide approximate solutions.

**Perturbation theory:** Start with a known exact solution (unperturbed problem), then apply small changes (perturbations).

**Variational methods:** Express a quantity of interest as a functional that is stationary (first-order variation = 0) with respect to small changes in the field.

Both methods are essential for:
- Waveguide imperfections and losses
- Cavity perturbation for material measurement
- Variational solutions for transmission lines and antennas

**中文：**

许多实际问题无法精确求解。**微扰法**和**变分法**提供近似解。

**微扰理论：** 从已知的精确解（未微扰问题）出发，然后施加小的变化（微扰）。

**变分法：** 将感兴趣量表示为泛函，该泛函对场的小变化是稳定的（一次变分 = 0）。

---

## Section 7-2: Degenerate Perturbation / 简并微扰

**English:**

**Perturbation of degenerate states** occurs when the unperturbed problem has multiple solutions with the same eigenvalue.

Example: Two orthogonal modes with same cutoff frequency $f_c$. When perturbed (e.g., slight asymmetry), they split into two distinct frequencies.

**Method:** Form matrix representation of perturbation operator in basis of degenerate unperturbed modes. Diagonalize to find perturbed eigenvalues.

**For 2 × 2 degenerate basis:**
$$[H] = [H_0] + \lambda[V]$$

If $[H_0]$ has eigenvalue $E_0$ with eigenvectors $\mathbf{e}_1, \mathbf{e}_2$, then in the degenerate subspace:
$$E^{(1)} = E_0 + \lambda\langle\mathbf{e}_i|V|\mathbf{e}_j\rangle$$

**Solved by:** Diagonalize the matrix $\langle\mathbf{e}_i|V|\mathbf{e}_j\rangle$.

**Application:** Coupled-mode theory for parallel waveguides, directional couplers.

**中文：**

**简并态的微扰**发生在未微扰问题有多个相同特征值的解时。

例如：两个正交模式具有相同的截止频率 $f_c$。当微扰（如轻微不对称）时，它们分裂成两个不同的频率。

**方法：** 在简并未微扰模的基中形成微扰算子的矩阵表示。对角化以找到微扰后的特征值。

**应用：** 耦合模理论，用于平行波导和定向耦合器。

---

## Section 7-3: Non-degenerate Perturbation / 非简并微扰

**English:**

**Non-degenerate perturbation** applies when the unperturbed states have distinct eigenvalues.

**First-order correction** to eigenvalue $E_n$:
$$E_n^{(1)} = \langle\mathbf{e}_n|V|\mathbf{e}_n\rangle \tag{7-12}$$

**First-order correction** to eigenvector $\mathbf{e}_n$:
$$\mathbf{e}_n^{(1)} = \sum_{m \neq n} \frac{\langle\mathbf{e}_m|V|\mathbf{e}_n\rangle}{E_n - E_m}\mathbf{e}_m \tag{7-14}$$

**Application: Waveguide wall roughness**

For a rectangular waveguide with slight wall roughness $\Delta(x,y)$:
$$\alpha_\text{rough} \approx \frac{k^2}{2\beta}\left(\frac{\Delta}{a}\right)^2 \quad \text{(for TE10 mode)}$$

The perturbation increases attenuation.

**Application: Waveguide irises**

Small capacitive or inductive irises cause perturbation in cutoff wavenumber:
$$\Delta k_c \approx -\frac{\omega\epsilon_0 A}{a b}$$

where $A$ is the iris area.

**中文：**

**非简并微扰**适用于未微扰态具有不同特征值的情况。

**特征值 $E_n$ 的一阶修正：**
$$E_n^{(1)} = \langle\mathbf{e}_n|V|\mathbf{e}_n\rangle \tag{7-12}$$

**特征向量 $\mathbf{e}_n$ 的一阶修正：**
$$\mathbf{e}_n^{(1)} = \sum_{m \neq n} \frac{\langle\mathbf{e}_m|V|\mathbf{e}_n\rangle}{E_n - E_m}\mathbf{e}_m \tag{7-14}$$

**应用：波导壁粗糙度**

对于轻微粗糙度的矩形波导：
$$\alpha_\text{rough} \approx \frac{k^2}{2\beta}\left(\frac{\Delta}{a}\right)^2$$

---

## Section 7-4: Variational Methods / 变分法

**English:**

**Variational methods** express a functional $F[\psi]$ that is stationary (extremum) at the true solution.

**Stationarity condition:**
$$\delta F = 0 \quad \text{(first-order variation vanishes)}$$

**Ritz method:** Assume trial solution $\psi = \sum_i a_i f_i$ where $f_i$ are known basis functions. Minimize $F$ with respect to coefficients $a_i$:

$$\frac{\partial F}{\partial a_i} = 0 \Rightarrow \text{solve for } a_i$$

**Example: Transmission line impedance**

$$Z = \frac{\int_S \mathbf{E} \times \mathbf{H}^* \cdot d\mathbf{s}}{I^2}$$

This is stationary with respect to small errors in $\mathbf{E}$ and $\mathbf{H}$.

**Example: Cavity resonance frequency**

$$f - f_0 = \frac{\delta W}{\omega W}$$

where $W$ is stored energy and $\delta W$ is perturbation in energy due to material loading.

**For admittance function:**
$$Y = \frac{I^2}{\int_V \mathbf{E} \cdot \mathbf{J}^*\, dV}$$

**Reciprocity variational method:** Express S-matrix elements as functionals that are stationary.

**中文：**

**变分法**将泛函 $F[\psi]$ 表达为在真实解处是稳定的（极值）。

**稳定性条件：**
$$\delta F = 0 \quad \text{（一次变分消失）}$$

**里茨法：** 假设试探解 $\psi = \sum_i a_i f_i$，其中 $f_i$ 是已知的基函数。对系数 $a_i$ 最小化 $F$：

$$\frac{\partial F}{\partial a_i} = 0 \Rightarrow \text{求解 } a_i$$

---

## Section 7-5: Method of Moments (MoM) / 矩量法

**English:**

**Method of Moments (MoM)** converts integral equations to matrix equations by expanding the unknown in a set of basis functions and testing with weighting functions.

**General procedure:**

1. **Choose basis functions** $\{f_n(\mathbf{r})\}$ to expand unknown $J(\mathbf{r})$:
$$J(\mathbf{r}) = \sum_n I_n f_n(\mathbf{r})$$

2. **Choose weighting (testing) functions** $\{w_m(\mathbf{r})\}$ and form inner products:
$$\langle w_m, \mathcal{L}J \rangle = \langle w_m, V \rangle$$

where $\mathcal{L}$ is the integral operator and $V$ is the known excitation.

3. **Form matrix equation:**
$$[Z]\{I\} = \{V\}$$

where $Z_{mn} = \langle w_m, \mathcal{L}f_n \rangle$ is the **impedance matrix**.

**Galerkin's method:** Use same functions for basis and weighting ($w_m = f_m$). Most common for electromagnetic problems.

**Pulse basis functions:** Piecewise constant on small intervals. Simple but requires many elements for smooth solutions.

**Sinusoidal basis functions:** Match current distribution better for wire antennas. Used in NEC (Numerical Electromagnetics Code).

**Convergence:** MoM solution converges to exact solution as number of basis functions increases, provided basis is complete.

**Ill-conditioned matrices:** EM MoM matrices are typically dense and ill-conditioned. Preconditioning techniques (e.g., iterative solvers, multilevel methods) are needed for large problems.

**Application: Wire antennas**

Pocklington's equation for thin wire:
$$\int_{-L/2}^{L/2} I(z')\left(\frac{\partial^2}{\partial z^2} + k^2\right)\frac{e^{-jkR}}{4\pi R}\, dz' = \frac{V}{Z_s}$$

where $Z_s$ is the surface impedance.

**Application: Microstrip lines**

Green's function for layered media. Basis functions with singular behavior at edges.

**Application: Scattering from conducting bodies**

EFIE or MFIE discretized on conducting surface. Dense matrix solved by direct or iterative methods.

**中文：**

**矩量法（MoM）**通过将未知量展开为一组基函数，并用权函数进行测试，将积分方程转换为矩阵方程。

**一般步骤：**

1. **选择基函数** $\{f_n(\mathbf{r})\}$ 展开未知量 $J(\mathbf{r})$：
$$J(\mathbf{r}) = \sum_n I_n f_n(\mathbf{r})$$

2. **选择权（测试）函数** $\{w_m(\mathbf{r})\}$ 并形成内积：
$$\langle w_m, \mathcal{L}J \rangle = \langle w_m, V \rangle$$

3. **形成矩阵方程：**
$$[Z]\{I\} = \{V\}$$

其中 $Z_{mn} = \langle w_m, \mathcal{L}f_n \rangle$ 是**阻抗矩阵**。

**应用：线天线**

Pocklington方程：
$$\int_{-L/2}^{L/2} I(z')\left(\frac{\partial^2}{\partial z^2} + k^2\right)\frac{e^{-jkR}}{4\pi R}\, dz' = \frac{V}{Z_s}$$

---

## Section 7-6: Hallén's Integral Equation / 哈伦积分方程

**English:**

**Hallén's integral equation** is an alternative to Pocklington for thin wire antennas.

For a symmetric cylindrical dipole of length $L$:
$$\int_{-L/2}^{L/2} I(z')\frac{e^{-jkR}}{4\pi R}\, dz' = A\cos(kz) + B\sin(kz) + \frac{V}{2Z_0}\sin(k|z|)$$

where $A$ and $B$ are determined by boundary conditions:
- $I(0) = 0$ (center of dipole)
- $I(\pm L/2) = 0$ (end conditions)

**Solution by MoM:** Expand $I(z) = \sum_n I_n f_n(z)$ and form matrix equation.

**Basis functions for dipole:**
- Triangular functions (piecewise linear) — common in NEC
- Sinusoidal functions — match current distribution

**Current distribution approximation:**
For a half-wave dipole, $I(z) = I_0 \sin(k(|z| - L/2))$ (sinusoidal approximation)

**Input admittance:**
$$Y_\text{in} = Y_c \frac{2\sin^2(kL/2)}{2\cos^2(kL/2) - jZ_0 Y_c\sin^2(kL/2)}$$

At resonance ($L = \lambda/2$): $Y_\text{in} \approx 1/73$ S, $R_\text{in} \approx 73\ \Omega$.

**中文：**

**Hallén积分方程**是细线天线的另一种方法（替代Pocklington）。

对于长度为 $L$ 的对称圆柱偶极子：
$$\int_{-L/2}^{L/2} I(z')\frac{e^{-jkR}}{4\pi R}\, dz' = A\cos(kz) + B\sin(kz) + \frac{V}{2Z_0}\sin(k|z|)$$

**用MoM求解：** 展开 $I(z) = \sum_n I_n f_n(z)$ 并形成矩阵方程。

**输入导纳：**
$$Y_\text{in} = Y_c \frac{2\sin^2(kL/2)}{2\cos^2(kL/2) - jZ_0 Y_c\sin^2(kL/2)}$$

在谐振时（$L = \lambda/2$）：$R_\text{in} \approx 73\ \Omega$。

---


---

## Section 7-7: Variational Principles for S-Parameters / S参数的变分原理

**English:**

**Variational expressions** for S-parameters provide stable approximations that are first-order accurate.

**Reflection coefficient variational:**
$$\\Gamma = \\frac{\\langle \\mathbf{E}_t, \\mathbf{Z}_0 \\mathbf{H}_t \\times \\hat{n} \\rangle}{\\langle \\mathbf{E}_t, \\mathbf{H}_t \\times \\hat{n} \\rangle}$$

This is stationary with respect to small errors in $\\mathbf{E}_t, \\mathbf{H}_t$.

**Impedance matrix elements:**
$$Z_{ij} = \\frac{\\langle \\mathbf{E}_i, \\mathbf{J}_j \\rangle}{I_i I_j}$$

where $\\mathbf{E}_i$ is the field due to port $i$ current and $\\mathbf{J}_j$ is the current distribution at port $j$.

**Admittance matrix elements:**
$$Y_{ij} = \\frac{\\langle \\mathbf{H}_i, \\mathbf{E}_j \\rangle}{V_i V_j}$$

**Reaction formulation for S-matrix:**
$$S_{ij} = \\frac{2\\langle a, b \\rangle}{\\sqrt{P_i P_j}}$$

where $a$ is the wave amplitude at port $i$ with port $j$ matched, and $b$ is the wave leaving port $j$.

**Perturbation of resonant cavities:**

For a cavity with small perturbation $\\Delta\\epsilon, \\Delta\\mu$:
$$\\frac{\\Delta f}{f} = \\frac{\\langle \\Delta\\epsilon |\\mathbf{E}|^2 + \\Delta\\mu |\\mathbf{H}|^2 \\rangle}{2\\langle \\epsilon |\\mathbf{E}|^2 + \\mu |\\mathbf{H}|^2 \\rangle}$$

This is the **cavity perturbation formula** used for material measurement.

**Dielectric constant measurement:** Insert sample into cavity, measure resonant frequency shift, compute permittivity from perturbation formula.

**Quality factor perturbation:**
$$\\frac{1}{Q} = \\frac{1}{Q_0} + \\tan\\delta_\\text{sample} \\cdot \\frac{\\text{stored energy in sample}}{\\text{total stored energy}}$$

**Chinese:**

**S参数的变分表达式**提供稳定的第一阶精确近似。

**阻抗矩阵元素：**
$$Z_{ij} = \\frac{\\langle \\mathbf{E}_i, \\mathbf{J}_j \\rangle}{I_i I_j}$$

**谐振腔微扰：**

对于具有小微扰 $\\Delta\\epsilon, \\Delta\\mu$ 的腔体：
$$\\frac{\\Delta f}{f} = \\frac{\\langle \\Delta\\epsilon |\\mathbf{E}|^2 + \\Delta\\mu |\\mathbf{H}|^2 \\rangle}{2\\langle \\epsilon |\\mathbf{E}|^2 + \\mu |\\mathbf{H}|^2 \\rangle}$$

这是用于材料测量的**腔体微扰公式**。

---

## Section 7-8: Mode Matching Method / 模式匹配法

**English:**

**Mode matching** solves waveguide discontinuities by expanding fields in terms of complete sets of waveguide modes.

**Procedure:**

1. **Expand fields** in region 1 as sum of modes with unknown amplitudes $A_n$:
$$\\mathbf{E}_1 = \\sum_n A_n \\mathbf{E}_n^{(1)}$$
$$\\mathbf{H}_1 = \\sum_n A_n \\mathbf{H}_n^{(1)}$$

2. **Expand fields** in region 2 as sum of modes with unknown amplitudes $B_n$:
$$\\mathbf{E}_2 = \\sum_n B_n \\mathbf{E}_n^{(2)}$$
$$\\mathbf{H}_2 = \\sum_n B_n \\mathbf{H}_n^{(2)}$$

3. **Match boundary conditions** at the interface $S$:
$$\\hat{n} \\times (\\mathbf{E}_1 - \\mathbf{E}_2) = 0 \\quad \\text{(tangential E continuous)}$$
$$\\hat{n} \\times (\\mathbf{H}_1 - \\mathbf{H}_2) = 0 \\quad \\text{(tangential H continuous)}$$

4. **Project onto each mode** to obtain matrix equation:
$$[T]\\{A\\} = [U]\\{B\\}$$

where $[T]$ and $[U]$ contain mode overlap integrals.

**Eigenfunctions** are complete for representing any field in the guide.

**Truncation:** Keep $N_1$ modes in region 1 and $N_2$ modes in region 2. Accuracy increases with $N_1, N_2$.

**Singular value decomposition:** Used to solve ill-conditioned mode matching matrices.

**Application: Step discontinuity in rectangular waveguide**

For step from guide $a \\times b$ to guide $a \\times b'$:
$$\\begin{pmatrix} b_1 \\\\ b_2 \\end{pmatrix} = \\begin{pmatrix} S_{11} & S_{12} \\\\ S_{21} & S_{22} \\end{pmatrix} \\begin{pmatrix} a_1 \\\\ a_2 \\end{pmatrix}$$

where modes in narrower guide are evanescent (below cutoff).

**Chinese:**

**模式匹配**通过用完整波导模式集展开场来求解波导不连续性。

**步骤：**

1. **展开**区域1中的场为模的和，包含未知振幅 $A_n$：
$$\\mathbf{E}_1 = \\sum_n A_n \\mathbf{E}_n^{(1)}$$

2. **展开**区域2中的场为模的和，包含未知振幅 $B_n$：
$$\\mathbf{E}_2 = \\sum_n B_n \\mathbf{E}_n^{(2)}$$

3. **匹配**界面 $S$ 处的边界条件：
$$\\hat{n} \\times (\\mathbf{E}_1 - \\mathbf{E}_2) = 0$$
$$\\hat{n} \\times (\\mathbf{H}_1 - \\mathbf{H}_2) = 0$$

4. **投影到每个模**以获得矩阵方程。

---

## Section 7-9: Finite Element Method Basics / 有限元法基础

**English:**

**Finite Element Method (FEM)** discretizes space into small elements and solves for fields at element nodes.

**Weak form** of Maxwell's equations:
$$\\int_V \\left((\\nabla \\times \\mathbf{E}) \\cdot (\\nabla \\times \\mathbf{E}_t) - k^2 \\mathbf{E} \\cdot \\mathbf{E}_t\\right) dV = 0$$

where $\\mathbf{E}_t$ are test (weighting) functions.

**Triangular or tetrahedral elements** for 2D or 3D discretization.

**Basis functions** are piecewise polynomials defined on each element.

**Assembly:** Form global matrix by summing element contributions.

**Sparse matrix** results from FEM — amenable to efficient sparse solvers.

**PML absorbing boundary conditions** simulate open regions.

**Application to waveguides:** Complex propagation constants found by solving eigenvalue problem:
$$[K]\\{\\mathbf{E}\\} = k_z^2 [M]\\{\\mathbf{E}\\}$$

**Application to cavities:** Find resonant frequencies by solving:
$$\\text{det}([K] - \\omega^2 [M]) = 0$$

**Commercial FEM tools:** HFSS, COMSOL, ANSYS Maxwell.

**Chinese:**

**有限元法（FEM）**将空间离散为小单元，并求解单元节点处的场。

**弱形式**的麦克斯韦方程：
$$\\int_V \\left((\\nabla \\times \\mathbf{E}) \\cdot (\\nabla \\times \\mathbf{E}_t) - k^2 \\mathbf{E} \\cdot \\mathbf{E}_t\\right) dV = 0$$

**三角或四面体单元**用于2D或3D离散化。

**组装：** 通过求和单元贡献形成全局矩阵。

**稀疏矩阵**源自FEM——适用于高效稀疏求解器。

---



---

---
chapter: 8
title: Microwave Networks
source: Roger F. Harrington, Time-Harmonic Electromagnetic Fields, IEEE Press
pages: 501-600
---

# Chapter 8: Microwave Networks / 微波网络

## Section 8-1: Network Theorems / 网络定理

**English:**

**Microwave networks** are an extension of low-frequency circuit theory to waveguide and transmission-line systems at microwave frequencies.

**Multi-conductor systems** support multiple propagating modes. Each mode at each frequency is a "transmission line channel."

**Network parameters:**

| Parameter | Definition | Used for |
|-----------|-----------|----------|
| **Z-parameters** (impedance) | $V_n = \sum_m Z_{nm} I_m$ | Open-circuit conditions |
| **Y-parameters** (admittance) | $I_n = \sum_m Y_{nm} V_m$ | Short-circuit conditions |
| **S-parameters** (scattering) | $b_n = \sum_m S_{nm} a_m$ | Traveling waves, matched systems |
| **T-parameters** (transfer) | Relates waves at two ports | Cascade analysis |

**S-parameters** are most commonly used in microwave engineering:

$$b_1 = S_{11}a_1 + S_{12}a_2$$
$$b_2 = S_{21}a_1 + S_{22}a_2$$

or in matrix form: $[b] = [S][a]$

where $a_n$ is the normalized incident wave and $b_n$ is the normalized reflected wave.

**Normalization:**
$$a_n = \frac{V_n^+}{\sqrt{Z_0}} \quad b_n = \frac{V_n^-}{\sqrt{Z_0}}$$

so that $|a_n|^2$ and $|b_n|^2$ represent power.

**S-parameter properties:**

- **Symmetry** for reciprocal networks: $[S]^T = [S]$, so $S_{ij} = S_{ji}$
- **Unitarity** for lossless networks: $[S][S]^* = [I]$, so $\sum_k S_{ik}S_{jk}^* = \delta_{ij}$
- **Lossless**: $|S_{11}|^2 + |S_{21}|^2 = 1$ for 2-port

**Power relationships:**
$$P_\text{incident} = \sum_n |a_n|^2$$
$$P_\text{reflected} = \sum_n |b_n|^2$$
$$P_\text{absorbed} = \sum_n (|a_n|^2 - |b_n|^2)$$

**中文：**

**微波网络**是将低频电路理论扩展到微波频率的波导和传输线系统。

**网络参数：**

| 参数 | 定义 | 用途 |
|------|------|------|
| **Z参数**（阻抗） | $V_n = \sum_m Z_{nm} I_m$ | 开路条件 |
| **Y参数**（导纳） | $I_n = \sum_m Y_{nm} V_m$ | 短路条件 |
| **S参数**（散射） | $b_n = \sum_m S_{nm} a_m$ | 行波、匹配系统 |
| **T参数**（转移） | 关联两端口处的波 | 级联分析 |

**S参数**在微波工程中最常用：

$$[b] = [S][a]$$

**性质：**
- 互易网络：**对称性** $[S]^T = [S]$
- 无耗网络：**酉性** $[S][S]^* = [I]$

---

## Section 8-2: Waveguide Junctions / 波导接头

**English:**

**Waveguide junctions** are discontinuities where modes convert between different waveguide sections or to other transmission structures.

**Two-port junction:** Waveguide of cross-section $A$ connected to waveguide of cross-section $B$.

**Mode matching:** Expand fields in each guide in terms of modal functions. Match tangential fields at the junction. This gives infinite matrix, truncated for numerical solution.

**Discontinuity capacitance:** For E-plane step in rectangular waveguide.

**H-plane iris:** Reactive obstacle with inductive characteristic.

**E-plane iris:** Reactive obstacle with capacitive characteristic.

**Resonant iris:** Series R-L-C at resonance.

**Equivalent circuit models:**

| Discontinuity | Equivalent Circuit |
|---------------|------------------|
| H-plane step | shunt inductor |
| E-plane step | series capacitor |
| Thin inductive post | shunt inductor |
| Thin capacitive post | series capacitor |
| Iris (symmetric) | parallel resonant circuit |

**Multi-port junctions:** $N$-port junction described by $N \times N$ S-matrix.

For $N$-port with all ports matched: $[S]$ has $S_{ii} = 0$.

**T-junction:** 3-port. Can be characterized by E-plane (series) or H-plane (shunt) configuration.

**Cross junction:** 4-port. Used in magic-T and hybrid coupling.

**Magic-T (hybrid tee):** 4-port with special properties:
- $S_{12} = S_{34} = 0$ (ports 1 and 2 are isolated)
- $S_{14} = S_{23} = 1/\sqrt{2}$ (E-arm to H-arm coupling)

**中文：**

**波导接头**是模式在不同波导段之间或与其他传输结构之间转换的不连续性。

**模式匹配：** 将每个波导中的场展开为模函数。在接头处匹配切向场。

**等效电路模型：**

| 不连续性 | 等效电路 |
|---------|---------|
| H面阶梯 | 并联电感 |
| E面阶梯 | 串联电容 |
| 感性膜片 | 并联电感 |
| 容性膜片 | 串联电容 |

---

## Section 8-3: Apertures and Irises / 孔径与膜片

**English:**

**Apertures** and **irises** in waveguides create reactive discontinuities.

**Thin iris (window):** Conductive diaphragm across waveguide aperture.

**Inductive iris (H-plane):** Iris with opening in narrow dimension. Equivalent to shunt inductance.

$$X_L \approx -\frac{\omega\mu a}{2\pi}\ln\left(\sin\frac{\pi d}{a}\right) \quad \text{(for narrow iris)}$$

where $d$ is the iris opening.

**Capacitive iris (E-plane):** Iris with opening in wide dimension. Equivalent to shunt capacitance.

$$X_C \approx \frac{\lambda_g}{2\pi b}\ln\left(\csc\frac{\pi d}{b}\right) \quad \text{(for narrow iris)}$$

**Symmetric iris:** Both broad walls present, opening in center. Equivalent to parallel resonant circuit.

**Resonant iris:** At certain dimensions, iris becomes resonant (match condition $X = 0$). Used for matching and filter的设计.

**Narrow coupling aperture:** Used to couple two waveguides. Equivalent to series transformer.

**Cross-coupling iris:** Creates coupling between non-adjacent cavities in filter structures.

**Filter design:** Iris-coupled waveguide filters use cascaded irises to create band-pass response.

**中文：**

波导中的**孔径**和**膜片**产生电抗性不连续性。

**感性膜片（H面）：** 在窄边有开口。等效为并联电感。

$$X_L \approx -\frac{\omega\mu a}{2\pi}\ln\left(\sin\frac{\pi d}{a}\right)$$

**容性膜片（E面）：** 在宽边有开口。等效为串联电容。

$$X_C \approx \frac{\lambda_g}{2\pi b}\ln\left(\csc\frac{\pi d}{b}\right)$$

**谐振膜片：** 在特定尺寸下，膜片变得谐振（匹配条件 $X = 0$）。

---

## Section 8-4: Coupling Slots / 耦合缝隙

**English:**

**Coupling slots** in waveguides are used for power coupling to other waveguides, antennas, or cavities.

**Radiating slot in waveguide wall:** Cuts in broad wall of rectangular waveguide.

**Broad-wall longitudinal slot:** Induces radiating current, equivalent to shunt conductance.

**Broad-wall transverse slot:** Equivalent to series resistance.

**Resonant slot:** At $L = \lambda/2$, input resistance matches waveguide characteristic impedance for maximum power transfer.

**Condition for resonance:**
$$\frac{G}{Y_0} = 2.09\left(\frac{\lambda_g}{\lambda}\right)^2 \frac{d}{a}\sin^2\frac{\pi x_0}{a}$$

where $d$ is slot width, $a$ is waveguide width, $x_0$ is slot offset from center.

**Non-radiating slots:** Slots that do not interrupt surface currents — no power coupled.

**Endfire slot array:** Series-fed array of slots on broad wall of waveguide, designed for endfire radiation pattern.

**Sidewall coupling:** Coupling to smaller waveguides or cavities through narrow wall slots.

**Slot-fed dipole:** Slot as feed for printed dipole antenna, used in microstrip array design.

**中文：**

波导中的**耦合缝隙**用于功率耦合到其他波导、天线或腔体。

**宽壁纵向缝隙：** 感应辐射电流，等效为并联电导。

**谐振缝隙：** 在 $L = \lambda/2$ 时，输入电阻与波导特性阻抗匹配以获得最大功率传输。

**谐振条件：**
$$\frac{G}{Y_0} = 2.09\left(\frac{\lambda_g}{\lambda}\right)^2 \frac{d}{a}\sin^2\frac{\pi x_0}{a}$$

其中 $d$ 是缝隙宽度，$a$ 是波导宽度，$x_0$ 是缝隙偏离中心的距离。

---

## Section 8-5: Network Analysis of Multi-port Junctions / 多端口接头的网络分析

**English:**

**Multi-port junctions** generalize the 2-port case to $N$ ports.

**General S-matrix formulation:**

For $N$-port junction, the S-matrix relates incident waves $[a]$ to reflected waves $[b]$:

$$[b] = [S][a]$$

**Properties:**
- For **lossless** junction: $[S]$ is unitary ($[S][S]^* = [I]$)
- For **reciprocal** junction: $[S]^T = [S]$ (symmetric)
- For **lossless and reciprocal**: $[S]$ is symmetric and unitary

**Port reference impedances** are arbitrary but conventionally chosen as real ($Z_0 = 50\ \Omega$ standard for microwave).

**Reference plane shift:** Moving reference plane by distance $l$ on port $n$ multiplies $S_{nm}$ by $e^{-j2\beta_n l}$ for $m = n$ (diagonal) and $e^{-j\beta_n l}$ for $m \neq n$ (off-diagonal).

**Cascade connection of 2-ports:**

Use T-parameters (ABCD-like):
$$\begin{bmatrix} b_1 \\ a_1 \end{bmatrix} = [T] \begin{bmatrix} a_2 \\ b_2 \end{bmatrix}$$

$$[T] = \begin{bmatrix} T_{11} & T_{12} \\ T_{21} & T_{22} \end{bmatrix}$$

Cascade: $[T_\text{total}] = [T_1][T_2]$

**Generalized scattering matrix (GSM):** For multi-mode, multi-port junctions with different modal impedances at each port.

**Network graph methods:** Mason's rule for signal flow graph analysis of microwave networks.

**Signal flow graph:** Nodes represent waves at ports. Branches represent S-parameters.

**Cut-set analysis:** For finding network eigenvalues and resonant conditions.

**Coupling matrix for filters:** Modern filter synthesis uses coupling matrix representation of coupled-resonator filters.

**Nonreciprocal devices** (circulators, isolators) require modified network theory since they violate reciprocity.

**中文：**

**多端口接头**将2端口情况推广到 $N$ 端口。

**一般S矩阵公式：**

对于 $N$ 端口接头，S矩阵将入射波 $[a]$ 与反射波 $[b]$ 关联：

$$[b] = [S][a]$$

**性质：**
- 对于**无耗**接头：$[S]$ 是酉矩阵 ($[S][S]^* = [I]$)
- 对于**互易**接头：$[S]^T = [S]$（对称）
- 对于**无耗且互易**：$[S]$ 是对称且酉的

**级联连接：**

使用T参数（类似于ABCD）：
$$[T_\text{total}] = [T_1][T_2]$$

**耦合矩阵用于滤波器：** 现代滤波器合成使用耦合矩阵表示耦合谐振器滤波器。

---

## Section 8-6: General Network Properties / 一般网络性质

**English:**

**Tellegen's theorem** applies to any lumped network (including microwave networks):

$$\sum_{n=1}^{N} V_n I_n^* = 0$$

This is a consequence of conservation of power in any network.

**Reciprocity** in networks: For reciprocal networks, the transfer function from port $i$ to port $j$ equals that from port $j$ to port $i$.

**Lossless networks:** Power is conserved. The S-matrix is unitary:
$$\sum_{k=1}^{N} S_{ik}S_{jk}^* = \delta_{ij}$$

This implies that:
- $\sum_i |S_{ij}|^2 = 1$ (all power incident at port $j$ is reflected or transmitted)
- $\sum_j |S_{ij}|^2 = 1$ (all power incident at port $i$ is reflected or transmitted)

**Passivity:** For passive networks, the sum of absorbed powers must be non-negative:
$$\sum_{n=1}^{N} \frac{|b_n|^2 - |a_n|^2}{2} \geq 0$$

which implies that $[I] - [S]^+[S]$ is positive semi-definite.

**Stability:** A network is stable if all traveling waves decay with time. Requires eigenvalues of $[S]$ to have magnitude $\leq 1$.

**Impedance matching:** Minimize reflections at ports. Common matching networks: stub tuners, quarter-wave transformers, multisection transformers.

**Smith chart:** Graphical representation of complex reflection coefficient and impedance for transmission line calculations.

**Broadband matching:** Requires careful design of matching network to achieve wide bandwidth with low VSWR.

**Synthesis:** Given desired S-parameters, synthesize network using Darlington synthesis or other techniques.

**中文：**

**Tellegen定理**适用于任何集总网络（包括微波网络）：

$$\sum_{n=1}^{N} V_n I_n^* = 0$$

这是功率守恒的结果。

**互易性：** 互易网络中，从端口 $i$ 到端口 $j$ 的传递函数等于从端口 $j$ 到端口 $i$ 的传递函数。

**无耗网络：** 功率守恒。S矩阵是酉矩阵：
$$\sum_{k=1}^{N} S_{ik}S_{jk}^* = \delta_{ij}$$

**被动性：** 对于被动网络，吸收功率之和必须非负：
$$\sum_{n=1}^{N} \frac{|b_n|^2 - |a_n|^2}{2} \geq 0$$

这意味着 $[I] - [S]^+[S]$ 是半正定的。

---



---

