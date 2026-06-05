# David K. Cheng《Field and Wave Electromagnetics》2nd Ed Chapter 3

> 本笔记基于 OCR 文本清洗整理，100% 来源于原书内容。

## Chapter 3 — Static Electric Fields

### 3-1. Introduction

Electrostatics is the study of the effects of **stationary (static) electric charges** in free space or in materials. This chapter develops the fundamental postulates and applies them to solve electrostatic problems.

### 3-2. Fundamental Postulates of Electrostatics in Free Space

#### Postulate 1: Coulomb's Law

The force between two point charges $q_1$ and $q_2$ separated by distance $R$ is:

$$\mathbf{F}_{12} = \frac{q_1 q_2}{4\pi\varepsilon_0 R^2}\hat{\mathbf{R}}_{12} = \frac{q_1 q_2}{4\pi\varepsilon_0}\frac{\mathbf{R}_{12}}{R^3}$$

where $\hat{\mathbf{R}}_{12}$ is the unit vector pointing from charge 1 to charge 2. This is the **inverse-square law**.

#### Postulate 2: Conservation of Charge

Electric charge is conserved — it can neither be created nor destroyed.

#### Electric Field Intensity $\mathbf{E}$

The electric field intensity at a point is defined as the force per unit charge on a vanishing small test charge:

$$\mathbf{E} = \lim_{q \to 0} \frac{\mathbf{F}}{q} \quad \text{(V/m)}$$

For a point charge $q$ at the origin, the field at $\mathbf{r}$ is:
$$\mathbf{E} = \frac{q}{4\pi\varepsilon_0}\frac{\hat{\mathbf{r}}}{r^2} = \frac{q}{4\pi\varepsilon_0}\frac{\mathbf{r}}{r^3}$$

**Electric field due to a system of discrete charges** (superposition):
$$\mathbf{E} = \frac{1}{4\pi\varepsilon_0}\sum_{i=1}^{N} \frac{q_i (\mathbf{r} - \mathbf{r}_i)}{|\mathbf{r} - \mathbf{r}_i|^3}$$

**Electric field due to a continuous charge distribution:**
- Volume: $\displaystyle \mathbf{E} = \frac{1}{4\pi\varepsilon_0}\int_v \frac{\rho(\mathbf{r}')(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^3}\,dv'$
- Surface: $\displaystyle \mathbf{E} = \frac{1}{4\pi\varepsilon_0}\int_S \frac{\rho_s(\mathbf{r}')(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^3}\,dS'$
- Line: $\displaystyle \mathbf{E} = \frac{1}{4\pi\varepsilon_0}\int_\ell \frac{\rho_\ell(\mathbf{r}')(\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^3}\,d\ell'$

### 3-4. Gauss's Law and Applications

**Gauss's law (integral form):** The total electric flux leaving any closed surface equals the total charge enclosed:

$$\oint_S \mathbf{E} \cdot d\mathbf{S} = \frac{Q_{\text{enc}}}{\varepsilon_0}$$

**Differential form** (from divergence theorem):
$$\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}$$

This is one of Maxwell's equations for static fields.

**Applications of Gauss's Law:**

| Charge Configuration | Electric Field | Location |
|---|---|---|
| Infinite planar sheet ($\rho_s$) | $\mathbf{E} = \frac{\rho_s}{2\varepsilon_0}\hat{\mathbf{n}}$ | Both sides |
| Infinitely long straight line ($\rho_\ell$) | $\mathbf{E} = \frac{\rho_\ell}{2\pi\varepsilon_0 \rho}\hat{\boldsymbol{\rho}}$ | Radial outward |
| Spherical shell ($Q$, radius $R$) | Inside: $\mathbf{E} = \mathbf{0}$ | $r < R$ |
| | Outside: $\mathbf{E} = \frac{Q}{4\pi\varepsilon_0 r^2}\hat{\mathbf{r}}$ | $r > R$ |
| Solid sphere ($\rho$, radius $R$) | Inside: $\mathbf{E} = \frac{\rho r}{3\varepsilon_0}\hat{\mathbf{r}}$ | $r < R$ |
| | Outside: $\mathbf{E} = \frac{\rho R^3}{3\varepsilon_0 r^2}\hat{\mathbf{r}}$ | $r > R$ |

### 3-5. Electric Potential

Since $\nabla \times \mathbf{E} = \mathbf{0}$ (electrostatic field is conservative), we can define a scalar potential $V$:

$$\mathbf{E} = -\nabla V$$

The **electric potential** at a point due to a point charge $q$:
$$V = \frac{q}{4\pi\varepsilon_0 R} + V_0$$

where $V_0$ is a reference potential.

**Potential difference** between two points:
$$V_{12} = V_1 - V_2 = \int_1^2 \mathbf{E} \cdot d\boldsymbol{\ell}$$

**Potential due to a continuous charge distribution:**
$$V = \frac{1}{4\pi\varepsilon_0}\int_v \frac{\rho\,dv'}{R} \quad \text{(volume)}$$

**Example — Potential of an electric dipole:**
For a dipole with charges $\pm q$ separated by distance $d$, on the axis at distance $r \gg d$:
$$V \approx \frac{q d \cos\theta}{4\pi\varepsilon_0 r^2}$$

where $\theta$ is the angle from the dipole axis.

### 3-6. Conductors in Static Electric Field

In electrostatics, a **perfect conductor** has the following properties:
1. Inside a conductor: $\mathbf{E} = \mathbf{0}$ (all charges reside on the surface).
2. The conductor surface is an **equipotential surface** ($V = \text{constant}$).
3. At the surface: $\mathbf{E}$ is perpendicular to the surface (tangential component is zero).
4. Just outside: $\mathbf{E} = \frac{\rho_s}{\varepsilon_0}\hat{\mathbf{n}}$ (normal component).

### 3-7. Dielectrics in Static Electric Field

When a dielectric is placed in an electric field, it becomes **polarized**. The polarization vector $\mathbf{P}$ (dipole moment per unit volume) relates to the bound charge densities:

$$\rho_b = -\nabla \cdot \mathbf{P} \quad \text{(bound volume charge)}$$
$$\rho_{sb} = \mathbf{P} \cdot \hat{\mathbf{n}} \quad \text{(bound surface charge)}$$

For **linear, isotropic, homogeneous (LIH) dielectrics**:
$$\mathbf{P} = \chi_e \varepsilon_0 \mathbf{E}$$

The **electric flux density** (electric displacement):
$$\mathbf{D} = \varepsilon_0 \mathbf{E} + \mathbf{P} = \varepsilon_0 \varepsilon_r \mathbf{E} = \varepsilon \mathbf{E}$$

where $\varepsilon_r = 1 + \chi_e$ is the **relative permittivity** (dielectric constant).

**Differential form of Gauss's law in dielectrics:**
$$\nabla \cdot \mathbf{D} = \rho_f$$
where $\rho_f$ is the **free charge density** (not the bound charge).

### 3-8. Electric Flux Density and Dielectric Constant

$$\mathbf{D} = \varepsilon \mathbf{E} = \varepsilon_r \varepsilon_0 \mathbf{E}$$

**Dielectric strength:** The maximum electric field before breakdown occurs (typically $10^6$ to $10^8$ V/m).

### 3-9. Boundary Conditions for Electrostatic Fields

At the interface between two media:

**Boundary condition for $\mathbf{D}$:**
$$\hat{\mathbf{n}} \cdot (\mathbf{D}_2 - \mathbf{D}_1) = \rho_s$$
For no surface free charge ($\rho_s = 0$): $\hat{\mathbf{n}} \cdot \mathbf{D}_2 = \hat{\mathbf{n}} \cdot \mathbf{D}_1$

**Boundary condition for $\mathbf{E}$:**
$$\hat{\mathbf{n}} \times (\mathbf{E}_2 - \mathbf{E}_1) = \mathbf{0} \implies \hat{\mathbf{n}} \times \mathbf{E}_2 = \hat{\mathbf{n}} \times \mathbf{E}_1$$
(Tangential component of $\mathbf{E}$ is continuous.)

At a conductor-dielectric interface (conductor = medium 1):
$$\hat{\mathbf{n}} \cdot \mathbf{D}_2 = \rho_s, \quad \hat{\mathbf{n}} \times \mathbf{E}_2 = \mathbf{0}$$

### 3-10. Capacitance and Capacitors

**Capacitance** $C$ is defined as the ratio of charge $Q$ on a conductor to its potential $V$:
$$C = \frac{Q}{V} \quad \text{(farads, F)}$$

| Configuration | Capacitance |
|---|---|
| Parallel-plate | $C = \frac{\varepsilon_0 \varepsilon_r S}{d}$ |
| Coaxial cable (inner radius $a$, outer $b$, length $\ell$) | $C = \frac{2\pi\varepsilon_0 \varepsilon_r \ell}{\ln(b/a)}$ |
| Spherical (inner radius $a$, outer $b$) | $C = \frac{4\pi\varepsilon_0 \varepsilon_r ab}{b-a}$ |
| Two parallel wires (radius $a$, separation $D$) | $C \approx \frac{\pi\varepsilon_0 \ell}{\ln(D/a)}$ |

**Series combination:**
$$\frac{1}{C_{\text{eq}}} = \sum_{i=1}^{N} \frac{1}{C_i}$$

**Parallel combination:**
$$C_{\text{eq}} = \sum_{i=1}^{N} C_i$$

### 3-11. Electrostatic Energy and Forces

**Energy stored in a capacitor:**
$$W_e = \frac{1}{2}CV^2 = \frac{Q^2}{2C} = \frac{1}{2}QV \quad \text{(joules)}$$

**Energy in terms of field quantities:**
$$W_e = \frac{1}{2}\int_v \mathbf{D} \cdot \mathbf{E}\,dv = \frac{1}{2}\int_v \varepsilon |\mathbf{E}|^2\,dv$$

**Energy density:**
$$w_e = \frac{1}{2}\mathbf{D} \cdot \mathbf{E} = \frac{1}{2}\varepsilon |\mathbf{E}|^2 \quad \text{(J/m}^3\text{)}$$

**Electrostatic force** on a conductor surface:
$$\mathbf{F} = \frac{1}{2}\oint_S \varepsilon |\mathbf{E}|^2 \hat{\mathbf{n}}\,dS$$

For a parallel-plate capacitor with plate area $S$ and separation $d$:
$$F = \frac{1}{2}\frac{\varepsilon_0 \varepsilon_r S E^2}{2} = \frac{\varepsilon_0 \varepsilon_r S V^2}{2d^2}$$
This is the attractive force between the plates (equal and opposite on each plate).

### Review Questions (Chapter 3)

1. State and explain Coulomb's law.
2. What is the relationship between electric field intensity and electric potential?
3. State Gauss's law in both integral and differential forms.
4. What are the boundary conditions for $\mathbf{E}$ and $\mathbf{D}$ at a dielectric interface?
5. Define capacitance. Derive the capacitance of a parallel-plate capacitor.
6. What is the energy density in an electrostatic field?

---

