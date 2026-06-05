# Jackson《Classical Electrodynamics》Ch4 — Dielectrics / 介质

> **Sections:** §4.1–§4.9 | **Book:** John David Jackson, 3rd Ed, Wiley 1999

---

## Multipole Expansion / Multipole Expansion

### Goal: approximate $\Phi(\mathbf{x})$ for a localized charge distribution at large distances / Goal: approximate $\Phi(\mathbf{x})$ for a localized charge distribution at large distances

$$
\Phi(\mathbf{x}) = \frac{1}{4\pi\epsilon_0} \int \frac{\rho(\mathbf{x}')}{|\mathbf{x} - \mathbf{x}'|} d^3x'
$$

For $|\mathbf{x}| \gg |\mathbf{x}'|$, expand in powers of $1/r$:

### Taylor expansion of $1/|\mathbf{x} - \mathbf{x}'|$ / Taylor expansion of $1/|\mathbf{x} — \mathbf{x}'|$

$$
\frac{1}{|\mathbf{x} - \mathbf{x}'|} = \frac{1}{r} + \frac{\mathbf{x} \cdot \mathbf{x}'}{r^3} + \frac{3(\mathbf{x} \cdot \mathbf{x}')^2 - r^2 r'^2}{2r^5} + \cdots
$$

### Multipole expansion / Multipole expansion

$$
\Phi(\mathbf{x}) = \frac{1}{4\pi\epsilon_0} \left \frac{Q}{r} + \frac{\mathbf{p} \cdot \hat{\mathbf{x}}}{r^2} + \frac{1}{2} \sum_{i,j} Q_{ij} \frac{x_i x_j}{r^5} + \cdots \right
$$

---

## Monopole Moment / 单极矩

$$
Q = \int \rho(\mathbf{x}') \, d^3x'
$$

- Total charge (scalar, invariant under translation)
- Leading term, decays as $1/r$

---

## Dipole Moment / 偶极矩

$$
\mathbf{p} = \int \mathbf{x}' \rho(\mathbf{x}') \, d^3x'
$$

- Vector quantity
- For point dipoles: $\mathbf{p} = q\mathbf{d}$ (two charges $\pm q$ separated by $\mathbf{d}$)

### Potential of a dipole / Potential of a dipole

$$
\Phi_{\text{dip}}(\mathbf{x}) = \frac{1}{4\pi\epsilon_0} \frac{\mathbf{p} \cdot \hat{\mathbf{x}}}{r^2}
$$

### Electric field of a dipole (outside) / Electric field of a dipole (outside)

$$
\mathbf{E}_{\text{dip}}(\mathbf{x}) = \frac{1}{4\pi\epsilon_0} \left \frac{3(\mathbf{p} \cdot \hat{\mathbf{x}})\hat{\mathbf{x}} — \mathbf{p}}{r^3} \right
$$

### At the origin (contact term for a point dipole) / At the origin (contact term for a point dipole)

$$
\mathbf{E}_{\text{dip}}(\mathbf{x}) = \frac{1}{4\pi\epsilon_0} \left \frac{3(\mathbf{p} \cdot \hat{\mathbf{x}})\hat{\mathbf{x}} — \mathbf{p}}{r^3} — \frac{4\pi}{3} \mathbf{p} \, \delta^{(3)}(\mathbf{x}) \right
$$

### Dipole moment is origin-dependent unless $Q = 0$ / Dipole moment is origin—dependent unless $Q = 0$

Under translation $\mathbf{x}' \to \mathbf{x}' + \mathbf{a}$:

$$
\mathbf{p}' = \mathbf{p} + Q\mathbf{a}
$$

Only well-defined independent of origin if $Q = 0$.

---

## Quadrupole Moment / 四极矩

### Quadrupole tensor (traceless) / Quadrupole tensor (traceless)

$$
Q_{ij} = \int (3x_i' x_j' - r'^2 \delta_{ij}) \rho(\mathbf{x}') \, d^3x'
$$

### Properties / Properties

- Symmetric: $Q_{ij} = Q_{ji}$
- Traceless: $\sum_i Q_{ii} = 0$
- 5 independent components
- Decays as $1/r^3$

### Potential / Potential

$$
\Phi_{\text{quad}}(\mathbf{x}) = \frac{1}{4\pi\epsilon_0} \frac{1}{2} \sum_{i,j} Q_{ij} \frac{x_i x_j}{r^5}
$$

### Examples / Examples

- **Linear quadrupole** ($+q$ at $\pm a$, $-2q$ at 0 on $z$-axis): $Q_{zz} = 4qa^2$, $Q_{xx} = Q_{yy} = -2qa^2$
- **Square quadrupole** ($\pm q$ at corners of square): $Q_{xy} = Q_{yx} = 3qa^2$ (depends on configuration)

---

## Spherical Multipoles / 球多极矩

### Expansion in spherical harmonics / Expansion in spherical harmonics

$$
\frac{1}{|\mathbf{x} - \mathbf{x}'|} = 4\pi \sum_{l=0}^\infty \sum_{m=-l}^l \frac{1}{2l+1} \frac{r_<^{\,l}}{r_>^{\,l+1}} Y_{lm}^*(\theta',\phi') Y_{lm}(\theta,\phi)
$$

### Multipole moments in spherical form / Multipole moments in spherical form

$$
q_{lm} = \int r'^{\,l} Y_{lm}^*(\theta',\phi') \rho(\mathbf{x}') \, d^3x'
$$

### Potential / Potential

$$
\Phi(\mathbf{x}) = \frac{1}{\epsilon_0} \sum_{l=0}^\infty \sum_{m=-l}^l \frac{q_{lm}}{2l+1} \frac{Y_{lm}(\theta,\phi)}{r^{l+1}}
$$

### Relation to Cartesian moments / Relation to Cartesian moments

- $q_{00} = \frac{1}{\sqrt{4\pi}} Q$ (monopole)
- $q_{1,\pm1} = \mp \sqrt{\frac{3}{8\pi}} (p_x \mp ip_y)$, $q_{10} = \sqrt{\frac{3}{4\pi}} p_z$ (dipole)
- $q_{2m}$ relates to traceless quadrupole tensor components

---

## Energy and Force in Multipole Expansion / 多极展开中的能量与力

### Energy of charge distribution in external potential / Energy of charge distribution in external potential

$$
W = \int \rho(\mathbf{x}) \Phi_{\text{ext}}(\mathbf{x}) \, d^3x
$$

### Multipole expansion of energy / Multipole expansion of energy

Expand $\Phi_{\text{ext}}(\mathbf{x})$ around origin:

$$
W = Q \Phi_{\text{ext}}(0) - \mathbf{p} \cdot \mathbf{E}_{\text{ext}}(0) - \frac{1}{6} \sum_{i,j} Q_{ij} \frac{\partial E_j}{\partial x_i}(0) + \cdots
$$

### Force on multipole in external field / Force on multipole in external field

$$
\mathbf{F} = Q \mathbf{E}_{\text{ext}} + (\mathbf{p} \cdot \nabla) \mathbf{E}_{\text{ext}} + \frac{1}{6} \sum_{i,j} Q_{ij} \nabla \frac{\partial E_j}{\partial x_i} + \cdots
$$

### Torque on a dipole / Torque on a dipole

$$
\boldsymbol{\tau} = \mathbf{p} \times \mathbf{E}_{\text{ext}}
$$

### Force on a dipole / Force on a dipole

$$
\mathbf{F} = (\mathbf{p} \cdot \nabla) \mathbf{E}_{\text{ext}}
$$

---

## Dielectrics — Macroscopic Description / 介质——宏观描述

### Polarization and bound charges / Polarization与bound charges

$$
\rho_b = -\nabla \cdot \mathbf{P}, \quad \sigma_b = \mathbf{P} \cdot \hat{\mathbf{n}}
$$

### Macroscopic electric field / Macroscopic electric field

Average over microscopic fluctuations. The $D$ field:

$$
\mathbf{D} = \epsilon_0 \mathbf{E} + \mathbf{P}
$$

### Gauss's law / Gauss's law

$$
\nabla \cdot \mathbf{D} = \rho_f
$$

### Linear isotropic dielectrics / Linear isotropic dielectrics

$$
\mathbf{D} = \epsilon \mathbf{E}, \quad \epsilon = \epsilon_0 \epsilon_r
$$

### Boundary conditions at dielectric interfaces / Boundary conditions at dielectric interfaces

- Normal $D$: $(\mathbf{D}_2 - \mathbf{D}_1) \cdot \hat{\mathbf{n}} = \sigma_f$
- Tangential $E$: $(\mathbf{E}_2 - \mathbf{E}_1) \times \hat{\mathbf{n}} = 0$

### In terms of potential / In terms of potential

$$
\Phi_1 = \Phi_2 \quad \text{(continuous)}
$$
$$
\epsilon_1 \frac{\partial \Phi_1}{\partial n} = \epsilon_2 \frac{\partial \Phi_2}{\partial n}
$$

---

## Boundary-Value Problems with Dielectrics / 含介质的边界值问题

### Dielectric sphere in uniform external field $\mathbf{E}_0$ / Dielectric sphere in uniform external field $\mathbf{E}_0$

**Sphere radius $a$, permittivity $\epsilon$, in vacuum ($\epsilon_0$).**

**Inside $(r < a)$:**

$$
\Phi_{\text{in}}(r,\theta) = -\frac{3\epsilon_0}{\epsilon + 2\epsilon_0} E_0 r \cos\theta
$$

So internal field is uniform: $\mathbf{E}_{\text{in}} = \frac{3\epsilon_0}{\epsilon + 2\epsilon_0} \mathbf{E}_0$

**Outside $(r > a)$:**

$$
\Phi_{\text{out}}(r,\theta) = -E_0 r \cos\theta + \frac{\epsilon - \epsilon_0}{\epsilon + 2\epsilon_0} \frac{a^3 E_0}{r^2} \cos\theta
$$

Equivalent to induced dipole moment:

$$
\mathbf{p} = 4\pi\epsilon_0 \frac{\epsilon - \epsilon_0}{\epsilon + 2\epsilon_0} a^3 \mathbf{E}_0
$$

### Polarization charge densities / Polarization charge densities

- Surface: $\sigma_p = \mathbf{P} \cdot \hat{\mathbf{n}} = 3\epsilon_0 \frac{\epsilon - \epsilon_0}{\epsilon + 2\epsilon_0} E_0 \cos\theta$
- Volume: $\rho_p = -\nabla \cdot \mathbf{P} = 0$ (uniform polarization inside)

### Dielectric cylinder in uniform transverse field / Dielectric cylinder in uniform transverse field

$$
\mathbf{E}_{\text{in}} = \frac{2\epsilon_0}{\epsilon + \epsilon_0} \mathbf{E}_0
$$

### Claussius-Mossotti relation / Claussius—Mossotti relation

Relates macroscopic $\epsilon$ to microscopic polarizability $\alpha$:

$$
\frac{\epsilon - \epsilon_0}{\epsilon + 2\epsilon_0} = \frac{N\alpha}{3\epsilon_0}
$$

where $N$ is number density of molecules.

---

## Key Formulas Summary / 重要公式汇总

| Concept | Formula |
|---|---|
| Multipole expansion | $\Phi = \frac{1}{4\pi\epsilon_0} \left \frac{Q}{r} + \frac{\mathbf{p}\cdot\hat{\mathbf{x}}}{r^2} + \frac{1}{2}\sum Q_{ij} \frac{x_i x_j}{r^5} + \cdots \right$ |
| Dipole potential | $\Phi_{\text{dip}} = \frac{1}{4\pi\epsilon_0} \frac{\mathbf{p}\cdot\hat{\mathbf{x}}}{r^2}$ |
| Dipole field (outside) | $\mathbf{E} = \frac{1}{4\pi\epsilon_0} \frac{3(\mathbf{p}\cdot\hat{\mathbf{x}})\hat{\mathbf{x}} - \mathbf{p}}{r^3}$ |
| Quadrupole tensor | $Q_{ij} = \int (3x_i x_j - r^2\delta_{ij})\rho \, d^3x$ |
| Spherical multipole | $q_{lm} = \int r^l Y_{lm}^* \rho \, d^3x$ |
| Energy in ext. field | $W = Q\Phi(0) - \mathbf{p}\cdot\mathbf{E}(0) - \frac{1}{6}\sum Q_{ij} \partial_j E_i(0) + \cdots$ |
| Dielectric sphere inside | $\mathbf{E}_{\text{in}} = \frac{3\epsilon_0}{\epsilon + 2\epsilon_0} \mathbf{E}_0$ |
| Dielectric sphere (induced p) | $\mathbf{p} = 4\pi\epsilon_0 \frac{\epsilon - \epsilon_0}{\epsilon + 2\epsilon_0} a^3 \mathbf{E}_0$ |
| Claussius-Mossotti | $\frac{\epsilon - \epsilon_0}{\epsilon + 2\epsilon_0} = \frac{N\alpha}{3\epsilon_0}$ |

---

## Key Problems / 典型习题

- **Problem 4.1** — Multipole moments of a charge distribution (Cartesian and spherical)
- **Problem 4.3** — Electric field of a dipole (including contact term)
- **Problem 4.7** — Dielectric sphere in uniform field (bound charges and energy)
- **Problem 4.9** — Point charge near a dielectric sphere (image method for dielectrics)
- **Problem 4.13** — Dielectric slab in a parallel-plate capacitor
