---
chapter: 8
title: Conservation Laws
source: Griffiths, Introduction to Electrodynamics, 4th Edition
pages: 356-400
---

# Chapter 8: Conservation Laws

## 8.1 Charge and Energy (pp. 356-360)

### 8.1.1 Continuity Equation

$$\frac{\partial\rho}{\partial t} = -\nabla\cdot\mathbf{J}$$

(8.4)

Local conservation of charge — charge cannot be created or destroyed.

### 8.1.2 Poynting's Theorem

**Electromagnetic energy density:**

$$u = \frac{1}{2}\left(\epsilon_0 E^2 + \frac{1}{\mu_0} B^2\right)$$

(8.5)

**Poynting vector** — energy flux density (energy per unit area per unit time):

$$\mathbf{S} \equiv \frac{1}{\mu_0}(\mathbf{E} \times \mathbf{B})$$

(8.10)

**Poynting's theorem** (work-energy theorem of electrodynamics):

$$\frac{dW}{dt} = -\frac{d}{dt}\int_{\mathcal{V}} u\,d\tau - \oint_S \mathbf{S}\cdot d\mathbf{a}$$

(8.11)

In differential form:

$$-\frac{\partial u}{\partial t} = \nabla\cdot\mathbf{S} + \mathbf{E}\cdot\mathbf{J}$$

(8.12 + 8.6)

Interpretation: Work done on charges = decrease in field energy - energy flowing out through surface.

**Example 8.1** (p. 359): Power flow in a current-carrying wire. The Poynting vector points radially inward along the wire, delivering energy (Joule heating) from the fields to the wire. $P = IV = \oint \mathbf{S}\cdot d\mathbf{a}$.

---

## 8.2 Momentum (pp. 360-400)

### 8.2.1 Newton's Third Law in Electrodynamics

Two moving charges do **not** exert equal and opposite forces on each other (Fig. 8.3). Momentum is conserved only when the momentum stored in the electromagnetic fields is included.

### 8.2.2 Maxwell Stress Tensor

Define the **Maxwell stress tensor**:

$$T_{ij} \equiv \epsilon_0\left(E_i E_j - \frac{1}{2}\delta_{ij}E^2\right) + \frac{1}{\mu_0}\left(B_i B_j - \frac{1}{2}\delta_{ij}B^2\right)$$

(8.17)

The electromagnetic force per unit volume:

$$\mathbf{f} = \nabla\cdot\overleftrightarrow{\mathbf{T}} - \epsilon_0\mu_0\frac{\partial\mathbf{S}}{\partial t}$$

(8.19)

Total force on charges in volume $\mathcal{V}$:

$$\mathbf{F} = \oint_S \overleftrightarrow{\mathbf{T}}\cdot d\mathbf{a} - \epsilon_0\mu_0\frac{d}{dt}\int_{\mathcal{V}} \mathbf{S}\,d\tau$$

(8.20)

In the static case:

$$\mathbf{F} = \oint_S \overleftrightarrow{\mathbf{T}}\cdot d\mathbf{a}$$

(8.21)

$T_{ij}$ = force per unit area in $i$-direction on surface oriented in $j$-direction. Diagonal elements = pressures; off-diagonal = shears.

**Example 8.2** (p. 364): Force on northern hemisphere of uniformly charged sphere. Using stress tensor: $F = Q^2/32\pi\epsilon_0 R^2$ (matches Prob. 2.47 result).

**Example 8.3** (p. 368): Coaxial cable carries charge $\lambda$ and current $I$. The fields store electromagnetic momentum:

$$\mathbf{p} = \mu_0\epsilon_0\int \mathbf{S}\,d\tau = \frac{\mu_0\lambda I l}{2\pi}\ln(b/a)\,\hat{\mathbf{z}} = \frac{I V l}{c^2}\hat{\mathbf{z}}$$

When current drops to zero, the induced electric field delivers this momentum to the cable.

### 8.2.3 Conservation of Momentum

**Momentum density** in the electromagnetic field:

$$\boldsymbol{\mathcal{P}} = \mu_0\epsilon_0\mathbf{S} = \frac{1}{c^2}\mathbf{S}$$

(8.32)

**Angular momentum density:**

$$\boldsymbol{\mathcal{L}} = \mathbf{r} \times \boldsymbol{\mathcal{P}} = \mu_0\epsilon_0\mathbf{r}\times\mathbf{S}$$

(8.33)

**Example 8.4** (p. 376): A long solenoid (radius $R$, field $B$) and a charged cylindrical shell ($\sigma$) produce electromagnetic angular momentum:

$$L_{\text{em}} = \frac{\mu_0 \pi R^4 \sigma I}{2}\hat{\mathbf{z}}$$

When the current is turned off, Faraday induction delivers mechanical torque to the cylinder, converting field angular momentum to mechanical angular momentum.

### 8.2.4 Magnetic Forces Do No Work

$$\mathbf{F}_{\text{mag}} = q(\mathbf{v}\times\mathbf{B}) \perp \mathbf{v} \quad\Rightarrow\quad dW_{\text{mag}} = 0$$

However, magnetic fields **can** store and transfer energy through the Poynting vector, and store momentum and angular momentum.

---

### 8.2.5 Angular Momentum (continued)

The electromagnetic angular momentum density is:

$$\boldsymbol{\mathcal{L}}_{\text{em}} = \mathbf{r} \times \boldsymbol{\mathcal{P}} = \mu_0\epsilon_0\, \mathbf{r} \times \mathbf{S}$$

(8.33)

**Example 8.4** (p. 376): A long solenoid (radius $R$, magnetic field $\mathbf{B} = \mu_0 n I \hat{\mathbf{z}}$ inside) and a charged cylindrical shell (radius $R \le s \le b$, surface charge $\sigma$) produce an extraordinary result: the system carries electromagnetic angular momentum even though nothing is moving mechanically:

$$L_{\text{em}} = \frac{\mu_0 \pi R^4 \sigma I}{2} \hat{\mathbf{z}}$$

When the solenoid current is turned off, Faraday induction produces a torque on the cylindrical shell, converting field angular momentum into mechanical rotation. This brilliantly demonstrates that field angular momentum is real and measurable.

**Magnetic forces do no work** — $\mathbf{F}_{\text{mag}} = q(\mathbf{v}\times\mathbf{B})$ is always perpendicular to $\mathbf{v}$. Yet magnetic fields can store and transfer energy (via the Poynting vector) and store momentum and angular momentum, which can later be extracted as mechanical work.

---

### Chapter Summary: Conservation Laws in Electrodynamics

| Quantity | Density | Flux / Current | Continuity Equation |
|----------|---------|----------------|---------------------|
| Charge | $\rho$ (charge density) | $\mathbf{J}$ | $\partial\rho/\partial t = -\nabla\cdot\mathbf{J}$ (8.4) |
| Energy | $u = \frac{1}{2}(\epsilon_0 E^2 + B^2/\mu_0)$ (8.5) | $\mathbf{S} = \frac{1}{\mu_0}\mathbf{E}\times\mathbf{B}$ (8.10) | $\partial u/\partial t = -\nabla\cdot\mathbf{S} - \mathbf{E}\cdot\mathbf{J}$ (8.12) |
| Momentum | $\boldsymbol{\mathcal{P}} = \mu_0\epsilon_0\mathbf{S} = \mathbf{S}/c^2$ (8.32) | $\overleftrightarrow{\mathbf{T}}$ (stress tensor) (8.17) | $\partial\boldsymbol{\mathcal{P}}/\partial t = \nabla\cdot\overleftrightarrow{\mathbf{T}} - \mathbf{f}$ (8.19) |
| Angular momentum | $\boldsymbol{\mathcal{L}} = \mathbf{r}\times\boldsymbol{\mathcal{P}}$ (8.33) | — | — |

### Maxwell Stress Tensor Elements

$$T_{ij} = \epsilon_0\left(E_i E_j - \frac{1}{2}\delta_{ij} E^2\right) + \frac{1}{\mu_0}\left(B_i B_j - \frac{1}{2}\delta_{ij} B^2\right)$$

(8.17)

In matrix form for a field $\mathbf{E} = E\hat{\mathbf{z}}$ (between capacitor plates):

$$\overleftrightarrow{\mathbf{T}} = \frac{\epsilon_0 E^2}{2}\begin{pmatrix} -1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & +1 \end{pmatrix}$$

The $T_{zz}$ component gives the tension along field lines ($+\epsilon_0 E^2/2$, pulling), while $T_{xx}$ and $T_{yy}$ give the lateral pressure ($-\epsilon_0 E^2/2$, pushing outward).

**物理直觉（全章回顾）：** 场不是数学虚构——它携带能量、动量和角动量。Poynting 定理是能量守恒的电动力学表述，Maxwell 应力张量将电磁力转化为边界上的应力。电磁场的动量和角动量在看似静态的系统中也可能存在（如同轴电缆），并在变化过程中转移为机械动量或被提取。电场线像橡皮筋一样有张力（彼此吸引、沿场线方向收缩、横向排斥），Maxwell 应力张量精确量化了这种直觉。
