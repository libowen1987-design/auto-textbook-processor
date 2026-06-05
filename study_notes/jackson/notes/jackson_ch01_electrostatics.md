# Jackson《Classical Electrodynamics》Ch1 — Introduction to Electrostatics / 静电学简介

> **Sections:** §1.1–§1.17 | **Book:** John David Jackson, 3rd Ed, Wiley 1999

---

## Coulomb's Law & Superposition / 库仑定律与叠加原理

### Coulomb's Law (point charges) / Coulomb's Law (point charges)

$$
\mathbf{F}_{12} = \frac{1}{4\pi\epsilon_0} \frac{q_1 q_2}{|\mathbf{x}_1 - \mathbf{x}_2|^3} (\mathbf{x}_1 - \mathbf{x}_2)
$$

- Force on $q_1$ due to $q_2$, inverse-square, along the line connecting charges
- $\epsilon_0 = 8.854 \times 10^{-12} \, \mathrm{C^2 / (N \cdot m^2)}$ (permittivity of free space)

### Superposition / Superposition

Total force on a test charge $q$ from a collection $\{q_i\}$:

$$
\mathbf{F} = \frac{q}{4\pi\epsilon_0} \sum_{i=1}^n \frac{q_i (\mathbf{x} - \mathbf{x}_i)}{|\mathbf{x} - \mathbf{x}_i|^3}
$$

### Electric Field / Electric Field

$$
\mathbf{E}(\mathbf{x}) = \frac{1}{4\pi\epsilon_0} \sum_{i=1}^n \frac{q_i (\mathbf{x} - \mathbf{x}_i)}{|\mathbf{x} - \mathbf{x}_i|^3}
$$

**Continuous charge distributions:**
- Line charge: $\mathbf{E}(\mathbf{x}) = \frac{1}{4\pi\epsilon_0} \int \frac{\lambda(\mathbf{x}') (\mathbf{x} - \mathbf{x}')}{|\mathbf{x} - \mathbf{x}'|^3} \, dl'$
- Surface charge: $\mathbf{E}(\mathbf{x}) = \frac{1}{4\pi\epsilon_0} \int \frac{\sigma(\mathbf{x}') (\mathbf{x} - \mathbf{x}')}{|\mathbf{x} - \mathbf{x}'|^3} \, da'$
- Volume charge: $\mathbf{E}(\mathbf{x}) = \frac{1}{4\pi\epsilon_0} \int \frac{\rho(\mathbf{x}') (\mathbf{x} - \mathbf{x}')}{|\mathbf{x} - \mathbf{x}'|^3} \, d^3 x'$

---

## Gauss's Law & Scalar Potential / 高斯定律与标量势

### Gauss's Law (integral form) / Gauss's Law (integral form)

$$
\oint_S \mathbf{E} \cdot \mathbf{n} \, da = \frac{Q_{\text{enc}}}{\epsilon_0}
$$

### Differential form / Differential form

$$
\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}
$$

### Scalar Potential $\Phi$ / Scalar Potential $\Phi$

Since $\nabla \times \mathbf{E} = 0$ in electrostatics, $\mathbf{E}$ is conservative:

$$
\mathbf{E} = -\nabla \Phi
$$

For a point charge: $\Phi(\mathbf{x}) = \frac{1}{4\pi\epsilon_0} \frac{q}{|\mathbf{x} - \mathbf{x}'|}$

### Poisson & Laplace Equations / Poisson与Laplace Equations

$$
\nabla^2 \Phi = -\frac{\rho}{\epsilon_0} \quad \text{(Poisson)}
$$
$$
\nabla^2 \Phi = 0 \quad \text{(Laplace, in charge-free regions)}
$$

---

## Surface Distributions & Discontinuities / 面分布与不连续性

### Surface Charge Boundary Condition / Surface Charge Boundary Condition

Across a surface charge layer:

$$
\mathbf{E}_{\text{above}} - \mathbf{E}_{\text{below}} = \frac{\sigma}{\epsilon_0} \hat{\mathbf{n}}
$$

### Tangential component continuous / Tangential component continuous

$$
\mathbf{E}_{\parallel}^{\text{above}} = \mathbf{E}_{\parallel}^{\text{below}}
$$

### Normal component jumps / Normal component jumps

$$
E_n^{\text{above}} - E_n^{\text{below}} = \frac{\sigma}{\epsilon_0}
$$

---

## Dirac Delta Function / 狄拉克δ函数

### Point charge density / Point charge density

$$
\rho(\mathbf{x}) = q \, \delta^{(3)}(\mathbf{x} - \mathbf{x}')
$$

### Key properties / Key properties

- $\int_V f(\mathbf{x}) \delta^{(3)}(\mathbf{x} - \mathbf{x}') \, d^3x = f(\mathbf{x}')$ if $\mathbf{x}' \in V$, zero otherwise
- $\nabla^2 \left(\frac{1}{|\mathbf{x} - \mathbf{x}'|}\right) = -4\pi \delta^{(3)}(\mathbf{x} - \mathbf{x}')$
- $\nabla \cdot \left(\frac{\mathbf{x} - \mathbf{x}'}{|\mathbf{x} - \mathbf{x}'|^3}\right) = 4\pi \delta^{(3)}(\mathbf{x} - \mathbf{x}')$

---

## Green's Theorem & Formal Solution / 格林定理与形式解

### Green's Identity (2nd) / Green's Identity (2nd)

$$
\int_V (\phi \nabla^2 \psi - \psi \nabla^2 \phi) \, d^3x = \oint_S \left(\phi \frac{\partial \psi}{\partial n} - \psi \frac{\partial \phi}{\partial n}\right) da
$$

### Poisson Equation Solution (Green function) / Poisson Equation Solution (Green function)

$$
\nabla'^2 G(\mathbf{x}, \mathbf{x}') = -4\pi \delta^{(3)}(\mathbf{x} - \mathbf{x}')
$$

The **free-space Green function**:

$$
G_0(\mathbf{x}, \mathbf{x}') = \frac{1}{|\mathbf{x} - \mathbf{x}'|}
$$

### Formal solution to Poisson / Formal solution to Poisson

$$
\Phi(\mathbf{x}) = \frac{1}{4\pi\epsilon_0} \int_V \frac{\rho(\mathbf{x}')}{|\mathbf{x} - \mathbf{x}'|} d^3x' + \frac{1}{4\pi} \oint_S \left \frac{1}{|\mathbf{x} — \mathbf{x}'|} \frac{\partial \Phi}{\partial n'} — \Phi(\mathbf{x}') \frac{\partial}{\partial n'} \left(\frac{1}{|\mathbf{x} — \mathbf{x}'|}\right) \right da'
$$

### Dirichlet vs Neumann Green functions / Dirichlet vs Neumann Green functions

- **Dirichlet BC:** $G_D(\mathbf{x}, \mathbf{x}') = 0$ for $\mathbf{x}' \in S$
- **Neumann BC:** $\partial G_N / \partial n' = -4\pi/S$ on $S$ (simplest choice)

---

## Potential Energy & Energy Density / 势能与能量密度

### Energy of a charge distribution / Energy of a charge distribution

$$
W = \frac{1}{2} \int \rho(\mathbf{x}) \Phi(\mathbf{x}) \, d^3x
$$

### For discrete charges / For discrete charges

$$
W = \frac{1}{4\pi\epsilon_0} \frac{1}{2} \sum_{i \neq j} \frac{q_i q_j}{|\mathbf{x}_i - \mathbf{x}_j|}
$$

### Energy in terms of fields / Energy in terms of fields

$$
W = \frac{\epsilon_0}{2} \int_{\text{all space}} |\mathbf{E}|^2 \, d^3x
$$

### Energy density / Energy density

$$
u = \frac{\epsilon_0}{2} |\mathbf{E}|^2
$$

---

## Conductors & Capacitance / 导体与电容

### Properties of conductors in electrostatics / Properties of conductors in electrostatics

- $\mathbf{E} = 0$ inside conductor
- All charge resides on surface
- Surface is equipotential
- $\mathbf{E}$ normal to surface: $\mathbf{E} = (\sigma/\epsilon_0) \hat{\mathbf{n}}$

### Capacitance / Capacitance

$$
C = \frac{Q}{\Phi_2 - \Phi_1}
$$

For a conductor pair: $Q = CV$
- Isolated sphere radius $R$: $C = 4\pi\epsilon_0 R$
- Parallel plates (area $A$, separation $d$): $C = \epsilon_0 A/d$

### Capacitance matrix (multiple conductors) / Capacitance matrix (multiple conductors)

$$
Q_i = \sum_{j} C_{ij} V_j
$$

---

## Electrostatic Fields in Matter / 介质中的静电场

### Polarization / Polarization

Electric dipole moment per unit volume: $\mathbf{P}(\mathbf{x})$

### Bound charge densities / Bound charge densities

- Bound volume charge: $\rho_b = -\nabla \cdot \mathbf{P}$
- Bound surface charge: $\sigma_b = \mathbf{P} \cdot \hat{\mathbf{n}}$

### Electric displacement / Electric displacement

$$
\mathbf{D} = \epsilon_0 \mathbf{E} + \mathbf{P}
$$

### Gauss's law in dielectrics / Gauss's law in dielectrics

$$
\nabla \cdot \mathbf{D} = \rho_f \quad \text{(free charge only)}
$$

### Linear dielectrics / Linear dielectrics

$$
\mathbf{P} = \epsilon_0 \chi_e \mathbf{E}, \quad \mathbf{D} = \epsilon \mathbf{E}
$$

- $\epsilon = \epsilon_0(1 + \chi_e) = \epsilon_0 \epsilon_r$
- $\chi_e$ = electric susceptibility

---

## Boundary Conditions & Images / 边界条件与镜像法

### BCs at dielectric interface / BCs at dielectric interface

$$
(\mathbf{D}_2 - \mathbf{D}_1) \cdot \hat{\mathbf{n}} = \sigma_f
$$
$$
(\mathbf{E}_2 - \mathbf{E}_1) \times \hat{\mathbf{n}} = 0
$$

### Method of Images (conductor) / Method of Images (conductor)

A point charge $q$ at distance $d$ above an infinite grounded conducting plane: image charge $-q$ at distance $d$ below plane.

---

## Key Formulas Summary / 重要公式汇总

| Concept | Formula |
|---|---|
| Coulomb's Law | $\mathbf{F}_{12} = \frac{1}{4\pi\epsilon_0} \frac{q_1 q_2}{r^2} \hat{\mathbf{r}}_{12}$ |
| Electric field | $\mathbf{E} = -\nabla \Phi$ |
| Gauss's law (differential) | $\nabla \cdot \mathbf{E} = \rho/\epsilon_0$ |
| Poisson equation | $\nabla^2 \Phi = -\rho/\epsilon_0$ |
| Green function identity | $\nabla^2 (1/|\mathbf{x}-\mathbf{x}'|) = -4\pi\delta(\mathbf{x}-\mathbf{x}')$ |
| Energy density | $u = \tfrac{1}{2}\epsilon_0 E^2$ |
| Bound charge | $\rho_b = -\nabla\cdot\mathbf{P}$ |
| D-field relation | $\mathbf{D} = \epsilon_0\mathbf{E} + \mathbf{P}$ |

---

## Key Problems / 典型习题

- **Problem 1.1** — Line charge + point charge superposition (Coulomb force balance)
- **Problem 1.5** — Potential of a circular disk (elliptic integrals)
- **Problem 1.7** — Energy of a uniformly charged sphere
- **Problem 1.10** — Capacitance of two conducting spheres
- **Problem 1.14** — Green function for a half-space
