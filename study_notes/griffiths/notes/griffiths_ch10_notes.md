---
chapter: 10
title: Potentials and Fields
source: Griffiths, Introduction to Electrodynamics, 4th Edition
pages: 436-484
---

# Chapter 10: Potentials and Fields

## 10.1 The Potential Formulation (pp. 436-444)

### 10.1.1 Scalar and Vector Potentials

From $\nabla\cdot\mathbf{B} = 0$, we can still write $\mathbf{B} = \nabla\times\mathbf{A}$. From Faraday's law:

$$\nabla\times\mathbf{E} = -\frac{\partial}{\partial t}(\nabla\times\mathbf{A}) \;\Rightarrow\; \nabla\times\left(\mathbf{E} + \frac{\partial\mathbf{A}}{\partial t}\right) = 0$$

Thus:

$$\mathbf{E} = -\nabla V - \frac{\partial\mathbf{A}}{\partial t}$$

(10.3)

This replaces $\mathbf{E} = -\nabla V$ in electrostatics. Substituting into Gauss's law and Ampère-Maxwell:

$$\nabla^2 V + \frac{\partial}{\partial t}(\nabla\cdot\mathbf{A}) = -\frac{1}{\epsilon_0}\rho$$

(10.4)

$$\left(\nabla^2\mathbf{A} - \mu_0\epsilon_0\frac{\partial^2\mathbf{A}}{\partial t^2}\right) - \nabla\left(\nabla\cdot\mathbf{A} + \mu_0\epsilon_0\frac{\partial V}{\partial t}\right) = -\mu_0\mathbf{J}$$

(10.5)

### 10.1.2 Gauge Transformations

The potentials are not unique. If we change:

$$\mathbf{A}' = \mathbf{A} + \nabla\lambda, \quad V' = V - \frac{\partial\lambda}{\partial t}$$

(10.7)

the fields $\mathbf{E}$ and $\mathbf{B}$ remain unchanged.

**Coulomb gauge:** $\nabla\cdot\mathbf{A} = 0$ (10.9). Then $V$ satisfies Poisson's equation:

$$\nabla^2 V = -\frac{\rho}{\epsilon_0} \;\Rightarrow\; V(\mathbf{r},t) = \frac{1}{4\pi\epsilon_0}\int\frac{\rho(\mathbf{r}',t)}{\mathscr{r}}\,d\tau'$$

(10.10)

This is "acausal" — $V$ responds instantaneously to charge changes, but $\mathbf{E}$ does not because $\mathbf{A}$ corrects for it.

**Lorenz gauge:** $\nabla\cdot\mathbf{A} = -\mu_0\epsilon_0\frac{\partial V}{\partial t}$ (10.12). Then:

$$\Box^2 V = -\frac{\rho}{\epsilon_0}, \quad \Box^2\mathbf{A} = -\mu_0\mathbf{J}$$

(10.16)

where $\Box^2 \equiv \nabla^2 - \mu_0\epsilon_0\partial^2/\partial t^2$ is the **d'Alembertian** operator. In Lorenz gauge, $V$ and $\mathbf{A}$ are treated symmetrically.

### 10.1.3 Lorentz Force Law in Potential Form

$$F = q(\mathbf{E} + \mathbf{v}\times\mathbf{B}) = -q\left(\nabla V + \frac{\partial\mathbf{A}}{\partial t}\right) + q\mathbf{v}\times(\nabla\times\mathbf{A})$$

(10.17)

This can be written as:

$$\frac{d}{dt}(\mathbf{p} + q\mathbf{A}) = -\nabla[q(V - \mathbf{v}\cdot\mathbf{A})]$$

(10.20)

The **canonical momentum**: $\mathbf{p}_{\text{can}} = \mathbf{p} + q\mathbf{A}$ (10.21).

---

## 10.2 Continuous Distributions (pp. 444-454)

### 10.2.1 Retarded Potentials

Electromagnetic news travels at speed $c$. The potentials at field point $\mathbf{r}$ at time $t$ depend on source conditions at the **retarded time**:

$$t_r \equiv t - \frac{\mathscr{r}}{c}$$

(10.25)

**Retarded potentials:**

$$V(\mathbf{r},t) = \frac{1}{4\pi\epsilon_0}\int\frac{\rho(\mathbf{r}', t_r)}{\mathscr{r}}\,d\tau'$$

(10.26)

$$\mathbf{A}(\mathbf{r},t) = \frac{\mu_0}{4\pi}\int\frac{\mathbf{J}(\mathbf{r}', t_r)}{\mathscr{r}}\,d\tau'$$

(10.26)

These satisfy the inhomogeneous wave equation and the Lorenz condition. **Advanced potentials** ($t_a = t + \mathscr{r}/c$) also satisfy the equations but violate causality.

### 10.2.2 Jefimenko's Equations

The fields derived from retarded potentials give **Jefimenko's equations**:

$$\mathbf{E}(\mathbf{r},t) = \frac{1}{4\pi\epsilon_0}\int\left[\frac{\hat{\boldsymbol{\mathscr{r}}}}{\mathscr{r}^2}\rho(\mathbf{r}',t_r) + \frac{\hat{\boldsymbol{\mathscr{r}}}}{\mathscr{r}c}\frac{\partial\rho}{\partial t}(\mathbf{r}',t_r) - \frac{1}{\mathscr{r}c^2}\frac{\partial\mathbf{J}}{\partial t}(\mathbf{r}',t_r)\right]d\tau'$$

(10.36)

$$\mathbf{B}(\mathbf{r},t) = \frac{\mu_0}{4\pi}\int\left[\frac{\mathbf{J}(\mathbf{r}',t_r)}{\mathscr{r}^2} + \frac{1}{\mathscr{r}c}\frac{\partial\mathbf{J}}{\partial t}(\mathbf{r}',t_r)\right]\times\hat{\boldsymbol{\mathscr{r}}}\,d\tau'$$

(10.37)

These are the time-dependent generalizations of Coulomb's law and the Biot-Savart law.

---

## 10.3 Point Charges (pp. 454-484)

### 10.3.1 Liénard-Wiechert Potentials

For a point charge $q$ moving along trajectory $\mathbf{w}(t)$:

$$V(\mathbf{r},t) = \frac{1}{4\pi\epsilon_0}\frac{qc}{(\mathscr{r}c - \boldsymbol{\mathscr{r}}\cdot\mathbf{v})}$$

(10.46)

$$\mathbf{A}(\mathbf{r},t) = \frac{\mathbf{v}}{c^2}V(\mathbf{r},t) = \frac{\mu_0}{4\pi}\frac{qc\mathbf{v}}{(\mathscr{r}c - \boldsymbol{\mathscr{r}}\cdot\mathbf{v})}$$

(10.47)

where $\boldsymbol{\mathscr{r}} = \mathbf{r} - \mathbf{w}(t_r)$ and $\mathbf{v} = \dot{\mathbf{w}}(t_r)$ are evaluated at the retarded time.

For a charge moving with **constant velocity** $\mathbf{v}$:

$$V(\mathbf{r},t) = \frac{1}{4\pi\epsilon_0}\frac{q}{R\sqrt{1 - v^2\sin^2\theta/c^2}}$$

(10.51)

where $\mathbf{R} = \mathbf{r} - \mathbf{v}t$ is the vector from the **present** position and $\theta$ is the angle between $\mathbf{R}$ and $\mathbf{v}$.

### 10.3.2 Fields of a Moving Point Charge

From the Liénard-Wiechert potentials, the electric field of a point charge in arbitrary motion (the **Heaviside-Feynman formula**):

$$\mathbf{E}(\mathbf{r},t) = \frac{q}{4\pi\epsilon_0}\frac{\mathscr{r}}{(\boldsymbol{\mathscr{r}}\cdot\mathbf{u})^3}\left[(c^2 - v^2)\mathbf{u} + \boldsymbol{\mathscr{r}}\times(\mathbf{u}\times\mathbf{a})\right]$$

(10.65)

where $\mathbf{u} \equiv c\hat{\boldsymbol{\mathscr{r}}} - \mathbf{v}$ and quantities are evaluated at the retarded time.

**Velocity field** ($\mathbf{a}=0$):

$$\mathbf{E} = \frac{q}{4\pi\epsilon_0}\frac{1-v^2/c^2}{(1-v^2\sin^2\theta/c^2)^{3/2}}\frac{\hat{\mathbf{R}}}{R^2}$$

(10.68)

This is Coulomb's law modified by relativistic factors. The field is compressed in the transverse direction — Lorentz contraction of the field lines.

**Acceleration field** ($\propto 1/\mathscr{r}$, responsible for radiation):

$$\mathbf{E}_{\text{rad}} = \frac{q}{4\pi\epsilon_0}\frac{\mathscr{r}}{(\boldsymbol{\mathscr{r}}\cdot\mathbf{u})^3}\boldsymbol{\mathscr{r}}\times(\mathbf{u}\times\mathbf{a})$$

(10.66)

Magnetic field: $\displaystyle \mathbf{B} = \frac{1}{c}\hat{\boldsymbol{\mathscr{r}}}\times\mathbf{E}$.

---

### Chapter Summary

| Concept | Formula |
|---------|---------|
| Fields from potentials | $\mathbf{E} = -\nabla V - \partial\mathbf{A}/\partial t$, $\mathbf{B} = \nabla\times\mathbf{A}$ |
| Gauge transformation | $\mathbf{A}' = \mathbf{A} + \nabla\lambda$, $V' = V - \partial\lambda/\partial t$ |
| Lorenz gauge condition | $\nabla\cdot\mathbf{A} = -\mu_0\epsilon_0\partial V/\partial t$ |
| Retarded time | $t_r = t - \mathscr{r}/c$ |
| Retarded potentials | $V = \frac{1}{4\pi\epsilon_0}\int\frac{\rho(t_r)}{\mathscr{r}}d\tau'$, $\mathbf{A} = \frac{\mu_0}{4\pi}\int\frac{\mathbf{J}(t_r)}{\mathscr{r}}d\tau'$ |
| Liénard-Wiechert potentials | $V = \frac{qc}{4\pi\epsilon_0(\mathscr{r}c - \boldsymbol{\mathscr{r}}\cdot\mathbf{v})}$, $\mathbf{A} = \mathbf{v}V/c^2$ |
| Constant velocity field | $E = \frac{q}{4\pi\epsilon_0}\frac{1-v^2/c^2}{(1-v^2\sin^2\theta/c^2)^{3/2}}\frac{\hat{R}}{R^2}$ |

**物理直觉（全章回顾）：** 势的表述将 Maxwell 方程组的六个分量（$\mathbf{E}$, $\mathbf{B}$）简化为四个（$V$, $\mathbf{A}$），并提供了规范自由度。推迟势是因果律的体现——远方源的信息以光速传播。Liénard-Wiechert 势给出了任意运动点电荷产生的场，其中速度场携带"该电荷的 Coulomb 场在运动下的畸变"，加速度场则对应辐射。
