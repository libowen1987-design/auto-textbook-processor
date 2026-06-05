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
