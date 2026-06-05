---
chapter: 5
title: Magnetostatics
source: Griffiths, Introduction to Electrodynamics, 4th Edition
pages: 210-284
---

# Chapter 5: Magnetostatics

## 5.1 The Lorentz Force Law (pp. 210-222)

### 5.1.1-5.1.2 Magnetic Fields and Forces

A moving charge $Q$ with velocity $\mathbf{v}$ experiences a **magnetic force** in a magnetic field $\mathbf{B}$:

$$\mathbf{F}_{\text{mag}} = Q(\mathbf{v} \times \mathbf{B})$$

(5.1)

The **Lorentz force law** combines electric and magnetic forces:

$$\mathbf{F} = Q[\mathbf{E} + (\mathbf{v} \times \mathbf{B})]$$

(5.2)

Key experimental observations:
- Parallel currents attract, antiparallel currents repel (Fig. 5.2)
- $\mathbf{B}$ circles around a wire (right-hand rule, Fig. 5.3)
- Magnetic forces are perpendicular to velocity → do no work

**Example 5.1** (p. 212): **Cyclotron motion.** A charged particle moves in a circle in a uniform $\mathbf{B}$ field. The magnetic force provides centripetal acceleration:

$$QvB = m\frac{v^2}{R} \quad\Rightarrow\quad p = QBR$$

(5.3)

If there is a velocity component parallel to $\mathbf{B}$, the particle follows a helix (Fig. 5.6).

**Example 5.2** (p. 213): **Cycloid motion.** With perpendicular $\mathbf{E}$ and $\mathbf{B}$ fields ($\mathbf{B}=B\hat{\mathbf{x}}$, $\mathbf{E}=E\hat{\mathbf{z}}$), the particle executes cycloidal motion. Define $\omega \equiv QB/m$ (cyclotron frequency). The trajectory is:

$$y(t) = \frac{E}{\omega B}(\omega t - \sin\omega t), \quad z(t) = \frac{E}{\omega B}(1 - \cos\omega t)$$

(5.7-5.8)

### 5.1.3 Currents

**Current** $I = \lambda v$ where $\lambda$ is charge per unit length. For volume currents:

$$\mathbf{J} = \rho\mathbf{v} \quad\text{(volume current density, A/m}^2\text{)}$$

(5.13)

$$I = \int \mathbf{J}\cdot d\mathbf{a}$$

(5.14)

For surface currents: $\mathbf{K} = \sigma\mathbf{v}$ (A/m).

**Continuity equation** (charge conservation):

$$\nabla\cdot\mathbf{J} = -\frac{\partial\rho}{\partial t}$$

(5.29)

For **steady currents**: $\nabla\cdot\mathbf{J} = 0$ (5.33).

**Force on a current:**
- Line current: $\mathbf{F} = I\int (d\mathbf{l} \times \mathbf{B})$ (5.17)
- Volume current: $\mathbf{F} = \int (\mathbf{J} \times \mathbf{B})\,d\tau$ (5.16)

**Example 5.3** (p. 219): Force on a triangular loop near a straight wire.

**Example 5.4** (p. 220): Net force on a current loop in a uniform field is zero, but there is a torque: $\mathbf{N} = \mathbf{m} \times \mathbf{B}$ where $\mathbf{m} = I\mathbf{a}$ is the **magnetic dipole moment**.

---

## 5.2 The Biot-Savart Law (pp. 223-242)

### 5.2.1-5.2.2 Magnetic Field of a Steady Current

**Biot-Savart law** — the fundamental law for magnetic fields from steady currents:

$$\mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi} I \int \frac{d\mathbf{l}' \times \hat{\mathscr{r}}}{\mathscr{r}^2}$$

(5.34)

For volume currents: $\displaystyle \mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi} \int \frac{\mathbf{J}(\mathbf{r}') \times \hat{\mathscr{r}}}{\mathscr{r}^2}\,d\tau'$ (5.47)

$\mu_0 = 4\pi \times 10^{-7}$ N/A$^2$ is the **permeability of free space**.

**Example 5.5** (p. 225): **Long straight wire.** Field at distance $s$:

$$B = \frac{\mu_0 I}{2\pi s}$$

(5.38)

In cylindrical coordinates: $\displaystyle \mathbf{B} = \frac{\mu_0 I}{2\pi s}\hat{\boldsymbol{\phi}}$ (5.39)

**Example 5.6** (p. 227): **Force between parallel wires.** Force per unit length:

$$f = \frac{\mu_0}{2\pi}\frac{I_1 I_2}{d}$$

(5.40)

Parallel currents attract; antiparallel currents repel. This formula **defines** the ampere.

**Example 5.7** (p. 228): Magnetic field of a circular loop (radius $R$, current $I$) on axis:

$$B(z) = \frac{\mu_0 I}{2}\frac{R^2}{(R^2+z^2)^{3/2}}$$

(5.41)

At center: $B(0) = \mu_0 I/2R$.

**Example 5.8** (p. 229): Magnetic field of a rotating charged disk — treat as surface current $\mathbf{K} = \sigma\mathbf{v}$.

---

## 5.3 The Divergence and Curl of B (pp. 242-272)

### 5.3.1-5.3.2 Fundamental Theorems

**Divergence:** $\nabla\cdot\mathbf{B} = 0$ (5.50)

This is a universal law — there are no magnetic monopoles. In integral form:

$$\oint \mathbf{B}\cdot d\mathbf{a} = 0$$

(5.48)

**Curl — Ampère's law:**

$$\nabla\times\mathbf{B} = \mu_0\mathbf{J}$$

(5.46)

In integral form:

$$\oint \mathbf{B}\cdot d\mathbf{l} = \mu_0 I_{\text{enc}}$$

(5.57)

where $I_{\text{enc}}$ is the total current passing through the loop.

### 5.3.3 Applications of Ampère's Law

**Example 5.9** (p. 265): Magnetic field inside a long straight wire (radius $a$, uniform current):

$$B = \frac{\mu_0 I}{2\pi}\frac{s}{a^2} \quad (s \le a)$$

$$B = \frac{\mu_0 I}{2\pi s} \quad (s \ge a)$$

**Example 5.10** (p. 266): **Solenoid** (n turns per unit length, current $I$):

$$B = \mu_0 n I \quad\text{(inside)}$$

$$B = 0 \quad\text{(outside)}$$

**Toroid** (N total turns):

$$B = \frac{\mu_0 N I}{2\pi s} \quad\text{(inside)}$$

### 5.3.4 Comparison of Magnetostatics and Electrostatics

| | Electrostatics | Magnetostatics |
|---|---|---|
| Sources | $\rho$ (charges) | $\mathbf{J}$ (currents) |
| Fundamental law | Coulomb: $\mathbf{E} = \frac{1}{4\pi\epsilon_0}\int\frac{\hat{\mathscr{r}}}{\mathscr{r}^2}\rho\,d\tau'$ | Biot-Savart: $\mathbf{B} = \frac{\mu_0}{4\pi}\int\frac{\mathbf{J}\times\hat{\mathscr{r}}}{\mathscr{r}^2}d\tau'$ |
| Divergence | $\nabla\cdot\mathbf{E} = \rho/\epsilon_0$ | $\nabla\cdot\mathbf{B} = 0$ |
| Curl | $\nabla\times\mathbf{E} = 0$ | $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$ |
| Potential | $E = -\nabla V$ | $B = \nabla\times A$ |
| Poisson's eq. | $\nabla^2 V = -\rho/\epsilon_0$ | $\nabla^2 A = -\mu_0\mathbf{J}$ (Coulomb gauge) |

**物理直觉：** 静磁和静电的本质区别在于源的性质。电荷是标量源（产生发散场），电流是矢量源（产生旋涡场）。因此 $\mathbf{B}$ 线永远是闭合的——不像 $\mathbf{E}$ 线起始和终止于电荷。

---

## 5.4 Magnetic Vector Potential (pp. 272-284)

### 5.4.1 The Vector Potential

Since $\nabla\cdot\mathbf{B}=0$, we can write $\mathbf{B} = \nabla\times\mathbf{A}$, where $\mathbf{A}$ is the **vector potential**.

In **Coulomb gauge** ($\nabla\cdot\mathbf{A}=0$), Ampère's law becomes:

$$\nabla^2\mathbf{A} = -\mu_0\mathbf{J}$$

(5.64)

For localized currents:

$$\mathbf{A}(\mathbf{r}) = \frac{\mu_0}{4\pi}\int \frac{\mathbf{J}(\mathbf{r}')}{\mathscr{r}}\,d\tau'$$

(5.65)

For line and surface currents:

$$\mathbf{A} = \frac{\mu_0 I}{4\pi}\int \frac{1}{\mathscr{r}}\,d\mathbf{l}', \qquad \mathbf{A} = \frac{\mu_0}{4\pi}\int \frac{\mathbf{K}}{\mathscr{r}}\,da'$$

(5.66)

**Flux through a loop:**

$$\oint \mathbf{A}\cdot d\mathbf{l} = \int \mathbf{B}\cdot d\mathbf{a} = \Phi$$

(5.71)

**Example 5.11** (p. 245): Spherical shell (radius $R$, surface charge $\sigma$) spinning at angular velocity $\omega$:

$$\mathbf{A}(r,\theta,\phi) = \begin{cases} \frac{\mu_0 R\omega\sigma}{3}r\sin\theta\,\hat{\boldsymbol{\phi}} & (r\le R) \\ \frac{\mu_0 R^4\omega\sigma}{3}\frac{\sin\theta}{r^2}\hat{\boldsymbol{\phi}} & (r\ge R) \end{cases}$$

(5.69)

Inside field is uniform: $\mathbf{B} = \frac{2}{3}\mu_0\sigma R\boldsymbol{\omega}$ (5.70).

**Example 5.12** (p. 247): Solenoid (n turns/m, radius R, current I):

$$\mathbf{A} = \begin{cases} \frac{\mu_0 n I}{2}s\,\hat{\boldsymbol{\phi}} & (s \le R) \\ \frac{\mu_0 n I R^2}{2}\frac{1}{s}\hat{\boldsymbol{\phi}} & (s \ge R) \end{cases}$$

(5.72-5.73)

### 5.4.2 Multipole Expansion of the Vector Potential

For a localized current distribution at large distances:

$$\mathbf{A}(\mathbf{r}) = \frac{\mu_0}{4\pi}\left[\frac{1}{r}\int \mathbf{J}\,d\tau' + \frac{1}{r^2}\int \mathbf{J}(\hat{\mathbf{r}}\cdot\mathbf{r}')\,d\tau' + \cdots\right]$$

The **magnetic dipole moment** is:

$$\mathbf{m} = \frac{1}{2}\int (\mathbf{r}' \times \mathbf{J})\,d\tau'$$

(5.84)

The dipole term:

$$\mathbf{A}_{\text{dip}}(\mathbf{r}) = \frac{\mu_0}{4\pi}\frac{\mathbf{m}\times\hat{\mathbf{r}}}{r^2}$$

(5.85)

Field of a magnetic dipole:

$$\mathbf{B}_{\text{dip}}(\mathbf{r}) = \frac{\mu_0}{4\pi}\frac{1}{r^3}[3(\mathbf{m}\cdot\hat{\mathbf{r}})\hat{\mathbf{r}} - \mathbf{m}]$$

(5.86)

This is mathematically identical to the electric dipole field (Eq. 3.104)!

For a planar loop: $\mathbf{m} = I\mathbf{a}$ where $\mathbf{a}$ is the area vector.

---

### Chapter Summary: Key Formula Table

| Concept | Formula | Eq. |
|---------|---------|-----|
| Lorentz force | $\mathbf{F} = Q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$ | (5.2) |
| Biot-Savart law | $\mathbf{B} = \frac{\mu_0 I}{4\pi}\int\frac{d\mathbf{l}'\times\hat{\mathscr{r}}}{\mathscr{r}^2}$ | (5.34) |
| Ampère's law (integral) | $\oint\mathbf{B}\cdot d\mathbf{l} = \mu_0 I_{\text{enc}}$ | (5.57) |
| Ampère's law (differential) | $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$ | (5.46) |
| Vector potential | $\mathbf{B} = \nabla\times\mathbf{A}$ | (5.61) |
| $\mathbf{A}$ for localized currents | $\mathbf{A} = \frac{\mu_0}{4\pi}\int\frac{\mathbf{J}}{\mathscr{r}}d\tau'$ | (5.65) |
| Magnetic dipole moment | $\mathbf{m} = \frac{1}{2}\int(\mathbf{r}'\times\mathbf{J})d\tau'$ | (5.84) |
| Field of magnetic dipole | $\mathbf{B}_{\text{dip}} = \frac{\mu_0}{4\pi r^3}[3(\mathbf{m}\cdot\hat{\mathbf{r}})\hat{\mathbf{r}}-\mathbf{m}]$ | (5.86) |
| Solenoid field | $B = \mu_0 n I$ (inside) | |
| Force between parallel wires | $f = \frac{\mu_0}{2\pi}\frac{I_1 I_2}{d}$ | (5.40) |

**物理直觉（全章回顾）：** 静磁学与静电学的对偶关系至关重要。静电场由电荷产生（发散源），静磁场由电流产生（旋涡源）。$\mathbf{B}$ 线无头无尾（$\nabla\cdot\mathbf{B}=0$），安培环路定理是求解高对称性问题的利器。矢势 $\mathbf{A}$ 是 $\mathbf{B}$ 的积分形式的体现，其多极展开揭示远场总是由最低阶非零极矩主导。
