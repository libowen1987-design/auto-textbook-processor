---
chapter: 7
title: Electrodynamics
source: Griffiths, Introduction to Electrodynamics, 4th Edition
pages: 296-374
---

# Chapter 7: Electrodynamics

## 7.1 Electromotive Force (pp. 296-311)

### 7.1.1 Ohm's Law

For most materials, current density is proportional to force per unit charge:

$$\mathbf{J} = \sigma \mathbf{f}$$

(7.1)

where $\sigma$ = **conductivity** (resistivity $\rho = 1/\sigma$). For electromagnetic forces:

$$\mathbf{J} = \sigma(\mathbf{E} + \mathbf{v} \times \mathbf{B}) \approx \sigma\mathbf{E}$$

(7.2-7.3)

**Ohm's law** in circuit form:

$$V = IR, \quad R = \frac{L}{\sigma A}$$

(7.4)

| Material | Resistivity ($\Omega\!\cdot\!$m) |
|----------|--------------------------|
| Copper | $1.68\times10^{-8}$ |
| Aluminum | $2.65\times10^{-8}$ |
| Iron | $9.61\times10^{-8}$ |
| Seawater | $0.2$ |
| Glass | $10^9$-$10^{14}$ |

**Example 7.1** (p. 297): Cylindrical resistor. $I = \sigma A V/L$, $R = L/\sigma A$.

**Example 7.2** (p. 298): Coaxial cylinders. $R = \ln(b/a)/2\pi\sigma L$.

**Example 7.3** (p. 299): Proof that field is uniform in the cylindrical resistor — Laplace's equation with mixed boundary conditions gives $V = V_0 z/L$.

### 7.1.2 Electromotive Force

**Electromotive force (emf):**

$$\mathcal{E} = \oint \mathbf{f} \cdot d\mathbf{l} = \oint (\mathbf{E} + \mathbf{v}\times\mathbf{B})\cdot d\mathbf{l}$$

(7.9)

For electrostatic fields $\oint \mathbf{E}\cdot d\mathbf{l} = 0$, so emf must come from other sources (chemical, magnetic, thermal).

### 7.1.3 Motional emf

When a conductor moves through a magnetic field, the Lorentz force drives charges:

$$\mathcal{E} = \oint (\mathbf{v} \times \mathbf{B})\cdot d\mathbf{l}$$

(7.11)

For a sliding bar of length $l$ moving at speed $v$ in field $B$:

$$\mathcal{E} = Blv$$

**Example 7.4** (p. 309): **Faraday disk dynamo.** Rotating metal disk ($\omega$) in uniform $\mathbf{B}$. Force per unit charge $\mathbf{f} = \mathbf{v}\times\mathbf{B} = \omega s B\,\hat{\mathbf{s}}$, giving $\mathcal{E} = \omega B a^2/2$. This emf cannot be calculated from the flux rule because the current path is not well-defined.

---

## 7.2 Electromagnetic Induction (pp. 311-332)

### 7.2.1 Faraday's Law

**Faraday's law** (integral form):

$$\oint \mathbf{E}\cdot d\mathbf{l} = -\frac{d}{dt}\int \mathbf{B}\cdot d\mathbf{a}$$

(7.14)

**Differential form:**

$$\boxed{\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}}$$

(7.16)

**Universal flux rule:**

$$\mathcal{E} = -\frac{d\Phi}{dt}$$

(7.17)

where $\Phi = \int \mathbf{B}\cdot d\mathbf{a}$ is the magnetic flux through the loop.

**Lenz's law:** The induced current flows in such a direction as to oppose the change in flux.

**Example 7.5** (p. 314): Magnet passing through a wire ring. Flux builds then drops; emf has two spikes (positive and negative).

**Example 7.6** (p. 316): Jumping ring. When solenoid is turned on, Lenz's law induces opposite current in ring → repulsion → ring jumps.

### 7.2.2 The Induced Electric Field

The induced electric field from Faraday's law is **non-conservative** ($\nabla\times\mathbf{E} \neq 0$). It can be expressed as:

$$\mathbf{E} = -\frac{\partial\mathbf{A}}{\partial t}$$

(7.66)

where $\mathbf{A}$ is the vector potential, valid when $\partial\mathbf{A}/\partial t$ accounts for the induction field.

**Example 7.7** (p. 334): Charging capacitor $\rightarrow$ displacement current $\rightarrow$ magnetic field.

**Example 7.8** (p. 335): Induced $\mathbf{E}$ from an infinite solenoid with changing current:

$$E(s) = \begin{cases} -\frac{s}{2}\frac{dB}{dt}\hat{\boldsymbol{\phi}} & s < R \\ -\frac{R^2}{2s}\frac{dB}{dt}\hat{\boldsymbol{\phi}} & s > R \end{cases}$$

### 7.2.3 Inductance

**Mutual inductance:** $M$ relates flux in loop 2 due to current in loop 1:

$$\Phi_2 = M_{21} I_1, \quad \mathcal{E}_2 = -M\frac{dI_1}{dt}$$

(7.22-7.23)

**Neumann's formula:**

$$M_{21} = \frac{\mu_0}{4\pi}\oint\oint\frac{d\mathbf{l}_2\cdot d\mathbf{l}_1}{\mathscr{r}}$$

(7.24)

**Self-inductance:**

$$\Phi = LI, \quad \mathcal{E} = -L\frac{dI}{dt}$$

(7.26-7.27)

Energy stored in an inductor:

$$W = \frac{1}{2}LI^2$$

(7.29)

**Example 7.10** (p. 338): Self-inductance of a toroidal coil: $L = \mu_0 N^2 h \ln(b/a)/2\pi$.

**Example 7.11** (p. 340): Self-inductance of a long solenoid: $L = \mu_0 n^2 \pi R^2 l$.

### 7.2.4 Energy in Magnetic Fields

General expression for energy stored in magnetic fields:

$$W = \frac{1}{2}\int (\mathbf{A}\cdot\mathbf{J})\,d\tau = \frac{1}{2\mu_0}\int B^2\,d\tau$$

(7.31-7.34)

**物理直觉：** 能量定域在场中，$B^2/2\mu_0$ 是磁能密度，与电场的 $\epsilon_0 E^2/2$ 对偶。

---

## 7.3 Maxwell's Equations (pp. 332-374)

### 7.3.1 The Problem with Ampère's Law

For non-steady currents, Ampère's law $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$ is inconsistent with charge conservation:

$$\nabla\cdot(\nabla\times\mathbf{B}) = 0 = \mu_0\nabla\cdot\mathbf{J} = -\mu_0\frac{\partial\rho}{\partial t} \neq 0$$

The paradox of the charging capacitor: $\oint \mathbf{B}\cdot d\mathbf{l}$ depends on which surface you choose (flat vs. balloon-shaped), because $I_{\text{enc}}$ is ill-defined.

### 7.3.2 Maxwell's Correction — Displacement Current

Maxwell added the **displacement current** term:

$$\boxed{\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\epsilon_0\frac{\partial\mathbf{E}}{\partial t}}$$

(7.37)

$$\mathbf{J}_d \equiv \epsilon_0\frac{\partial\mathbf{E}}{\partial t}$$

(7.38)

**Example 7.14** (p. 335): Two concentric spherical shells with Ohmic material between. Surprisingly, $B=0$ everywhere — the displacement current exactly cancels the conduction current.

### 7.3.3 Maxwell's Equations — Final Form

$$\boxed{\begin{aligned}
&\text{(I)}\quad \nabla\cdot\mathbf{E} = \frac{\rho}{\epsilon_0} &\quad&\text{(Gauss's law)}\\
&\text{(II)}\quad \nabla\cdot\mathbf{B} = 0 &\quad&\text{(No magnetic monopoles)}\\
&\text{(III)}\quad \nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t} &\quad&\text{(Faraday's law)}\\
&\text{(IV)}\quad \nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\epsilon_0\frac{\partial\mathbf{E}}{\partial t} &\quad&\text{(Ampère-Maxwell law)}
\end{aligned}}$$

(7.40)

Together with $\mathbf{F} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$ (7.41), these equations summarize **all of classical electrodynamics**.

### Maxwell's Equations in Matter

Using $\mathbf{D} = \epsilon_0\mathbf{E} + \mathbf{P}$ and $\mathbf{H} = \frac{1}{\mu_0}\mathbf{B} - \mathbf{M}$:

$$\boxed{\begin{aligned}
\text{(I)}\quad &\nabla\cdot\mathbf{D} = \rho_f\\
\text{(II)}\quad &\nabla\cdot\mathbf{B} = 0\\
\text{(III)}\quad &\nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t}\\
\text{(IV)}\quad &\nabla\times\mathbf{H} = \mathbf{J}_f + \frac{\partial\mathbf{D}}{\partial t}
\end{aligned}}$$

(7.56)

### Boundary Conditions for Electrodynamics

| Field | Perpendicular component | Parallel component |
|-------|------------------------|--------------------|
| $\mathbf{D}$ | $D_1^\perp - D_2^\perp = \sigma_f$ (7.60) | — |
| $\mathbf{B}$ | $B_1^\perp - B_2^\perp = 0$ (7.61) | — |
| $\mathbf{E}$ | — | $E_1^\parallel - E_2^\parallel = 0$ (7.62) |
| $\mathbf{H}$ | — | $H_1^\parallel - H_2^\parallel = \mathbf{K}_f \times \hat{\mathbf{n}}$ (7.63) |

---

### Chapter Summary: Maxwell Equation Table

| Law | Differential form | Integral form |
|-----|------------------|---------------|
| Gauss (electric) | $\nabla\cdot\mathbf{E} = \rho/\epsilon_0$ | $\oint\mathbf{E}\cdot d\mathbf{a} = Q_{\text{enc}}/\epsilon_0$ |
| Gauss (magnetic) | $\nabla\cdot\mathbf{B} = 0$ | $\oint\mathbf{B}\cdot d\mathbf{a} = 0$ |
| Faraday | $\nabla\times\mathbf{E} = -\partial\mathbf{B}/\partial t$ | $\oint\mathbf{E}\cdot d\mathbf{l} = -d\Phi/dt$ |
| Ampère-Maxwell | $\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\epsilon_0\partial\mathbf{E}/\partial t$ | $\oint\mathbf{B}\cdot d\mathbf{l} = \mu_0 I_{\text{enc}} + \mu_0\epsilon_0 d\Phi_E/dt$ |

**物理直觉（全章回顾）：** 第七章是电磁理论的巅峰。三大支柱——Ohm 定律（电流与电场的关系）、Faraday 感应定律（变化磁场产生电场）、位移电流（Maxwell 补全 Ampère 定律使电荷守恒自洽）——共同构成了 Maxwell 方程组。这组方程不仅统一了电学与磁学，还预言了电磁波的存在。从微观来看，所有电磁场的最终源头只有电荷与电流（$\rho$, $\mathbf{J}$）；变化的场只是"传递消息"的中间人。
