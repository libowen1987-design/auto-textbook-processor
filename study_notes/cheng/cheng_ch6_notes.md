# David K. Cheng《Field and Wave Electromagnetics》2nd Ed Chapter 6

> 本笔记基于 OCR 文本清洗整理，100% 来源于原书内容。

## Chapter 6 — Static Magnetic Fields

### 6-1. Introduction

Magnetostatics is the study of the effects of **steady (time-independent) electric currents** in free space or in materials.

### 6-2. Fundamental Postulates of Magnetostatics in Free Space

**Postulate 1: Magnetic flux density (B) due to steady currents**

From experiments by Biot and Savart (and Gauss's law for magnetism):

$$\nabla \cdot \mathbf{B} = 0 \quad \text{(no magnetic monopoles)}$$

**Postulate 2: The curl of B**

The source of $\mathbf{B}$ is the current density $\mathbf{J}$:
$$\nabla \times \mathbf{B} = \mu_0 \mathbf{J}$$

These two equations, together with the Lorentz force law, fully characterize the magnetic field due to steady currents.

### 6-3. Vector Magnetic Potential

Since $\nabla \cdot \mathbf{B} = 0$, we can define a **vector potential** $\mathbf{A}$:
$$\mathbf{B} = \nabla \times \mathbf{A}$$

In magnetostatics, we typically set $\nabla \cdot \mathbf{A} = 0$ (Coulomb gauge for magnetostatics).

### 6-4. Biot-Savart's Law and Applications

**Biot-Savart's law** gives the magnetic flux density $\mathbf{B}$ at a point due to a current element $I\,d\boldsymbol{\ell}$:

$$d\mathbf{B} = \frac{\mu_0}{4\pi}\frac{I\,d\boldsymbol{\ell} \times \hat{\mathbf{R}}}{R^2} = \frac{\mu_0}{4\pi}\frac{I\,d\boldsymbol{\ell} \times \mathbf{R}}{R^3}$$

For a complete circuit:
$$\mathbf{B}(\mathbf{r}) = \frac{\mu_0 I}{4\pi}\oint_C \frac{d\boldsymbol{\ell}' \times (\mathbf{r} - \mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|^3}$$

**Applications:**

| Current Configuration | Magnetic Field | Location |
|---|---|---|
| Infinitely long straight wire ($I$) | $\mathbf{B} = \frac{\mu_0 I}{2\pi\rho}\hat{\boldsymbol{\phi}}$ | Azimuthal |
| Circular loop (axis, at center) | $\mathbf{B} = \frac{\mu_0 I}{2R}\hat{\mathbf{z}}$ | Center |
| Circular loop (axis, at distance $z$) | $\mathbf{B} = \frac{\mu_0 I R^2}{2(R^2+z^2)^{3/2}}\hat{\mathbf{z}}$ | On axis |
| Solenoid (closely wound, $n$ turns/m) | $\mathbf{B} = \mu_0 n I \hat{\mathbf{z}}$ | Inside ideal solenoid |

### 6-5. The Magnetic Dipole

A small current loop of area $S$ carrying current $I$ has a **magnetic dipole moment**:
$$\mathbf{m} = I S \,\hat{\mathbf{n}}$$

The vector potential at distance $r \gg \sqrt{S}$:
$$\mathbf{A} = \frac{\mu_0}{4\pi}\frac{\mathbf{m} \times \hat{\mathbf{r}}}{r^2}$$

The magnetic field in the far zone (analogous to electric dipole):
$$\mathbf{B} = \frac{\mu_0}{4\pi}\frac{1}{r^3}[3(\mathbf{m}\cdot\hat{\mathbf{r}})\hat{\mathbf{r}} - \mathbf{m}]$$

### 6-6. Magnetization and Equivalent Current Densities

When a magnetic material is magnetized by an applied field, it develops **magnetization** $\mathbf{M}$ (magnetic dipole moment per unit volume). Equivalent current densities:

$$\mathbf{J}_b = \nabla \times \mathbf{M} \quad \text{(bound volume current)}$$
$$\mathbf{J}_{sb} = \mathbf{M} \times \hat{\mathbf{n}} \quad \text{(bound surface current)}$$

### 6-7. Magnetic Field Intensity and Relative Permeability

**Magnetic field intensity** $\mathbf{H}$:
$$\mathbf{B} = \mu_0 (\mathbf{H} + \mathbf{M}) = \mu_0 \mu_r \mathbf{H} = \mu \mathbf{H}$$

For linear, isotropic, homogeneous (LIH) magnetic materials:
$$\mathbf{M} = \chi_m \mathbf{H}$$
$$\mu_r = 1 + \chi_m$$
$$\mathbf{B} = \mu_0(1+\chi_m)\mathbf{H}$$

**Classification:**
- Diamagnetic: $\chi_m < 0$, $\mu_r < 1$ (e.g., bismuth, copper)
- Paramagnetic: $\chi_m > 0$, $\mu_r > 1$ (e.g., aluminum, platinum)
- Ferromagnetic: $\chi_m \gg 0$, $\mu_r \gg 1$ (e.g., iron, nickel) — non-linear (hysteresis)

### 6-8. Magnetic Circuits

In magnetic circuits, $\mathbf{H}$ plays the role of "magnetomotive force" (MMF), analogous to voltage in electric circuits:

$$\mathcal{F} = \oint \mathbf{H} \cdot d\boldsymbol{\ell} = NI \quad \text{(Magnetomotive Force)}$$
$$R_m = \frac{\ell}{\mu A} \quad \text{(Magnetic reluctance)}$$
$$\Phi = \frac{\mathcal{F}}{R_m} \quad \text{(Magnetic flux)}$$

This is analogous to Ohm's law: $V = RI$, $\mathcal{F} = R_m \Phi$.

### 6-9. Behavior of Magnetic Materials

- **Ferromagnetic materials** exhibit hysteresis — B vs H is non-linear and history-dependent.
- **Saturation:** At high fields, $\mathbf{M}$ saturates, and $\mathbf{B} \approx \mu_0 \mathbf{H}$.
- **Remanence:** Residual magnetization when the applied field is removed (used in permanent magnets).
- **Coercivity:** The field required to reduce B to zero after saturation.

### 6-10. Boundary Conditions for Magnetostatic Fields

At the interface between two media:

**For $\mathbf{B}$:**
$$\hat{\mathbf{n}} \cdot (\mathbf{B}_2 - \mathbf{B}_1) = 0 \implies B_{2n} = B_{1n}$$
(Normal component of $\mathbf{B}$ is continuous — no magnetic monopoles.)

**For $\mathbf{H}$:**
$$\hat{\mathbf{n}} \times (\mathbf{H}_2 - \mathbf{H}_1) = \mathbf{J}_s$$
If no surface current $\mathbf{J}_s = \mathbf{0}$: $\hat{\mathbf{n}} \times \mathbf{H}_2 = \hat{\mathbf{n}} \times \mathbf{H}_1$
(Tangential $\mathbf{H}$ is continuous when there's no surface current.)

For linear magnetic materials: $\frac{\tan\alpha_1}{\tan\alpha_2} = \frac{\mu_1}{\mu_2}$ where $\alpha$ is the angle from the normal.

### 6-11. Inductances and Inductors

**Self-inductance** $L$ is defined as the ratio of total magnetic flux linkage to the current producing it:
$$L = \frac{N\Phi}{I} = \frac{\lambda}{I} \quad \text{(henrys, H)}$$

where $\lambda = N\Phi$ is the total flux linkage.

**Mutual inductance** between two circuits:
$$M = \frac{N_2 \Phi_{12}}{I_1} = \frac{\mu_0}{4\pi}\oint_{C_1}\oint_{C_2}\frac{d\boldsymbol{\ell}_1 \cdot d\boldsymbol{\ell}_2}{R}$$

**Inductance per unit length** for common configurations:

| Configuration | Inductance per unit length |
|---|---|
| Coaxial cable ($a$, $b$) | $L' = \frac{\mu_0}{2\pi}\ln(b/a)$ |
| Parallel wires (separation $D$, radius $a$) | $L' = \frac{\mu_0}{\pi}\ln(D/a)$ |
| Solenoid (closely wound, $n$ turns/m) | $L' = \mu_0 n^2 S$ |

### 6-12. Magnetic Energy

**Energy stored in an inductor:**
$$W_m = \frac{1}{2}LI^2 = \frac{1}{2}\lambda I \quad \text{(joules)}$$

**Energy in terms of field quantities:**
$$W_m = \frac{1}{2}\int_v \mathbf{B} \cdot \mathbf{H}\,dv = \frac{1}{2}\int_v \frac{|\mathbf{B}|^2}{\mu}\,dv$$

**Magnetic energy density:**
$$w_m = \frac{1}{2}\mathbf{B} \cdot \mathbf{H} = \frac{|\mathbf{B}|^2}{2\mu} \quad \text{(J/m}^3\text{)}$$

### Review Questions (Chapter 6)

1. State the two fundamental postulates of magnetostatics.
2. Write and explain Biot-Savart's law.
3. What is the magnetic dipole moment of a current loop?
4. State the boundary conditions for $\mathbf{B}$ and $\mathbf{H}$ at a magnetic interface.
5. Define self-inductance and mutual inductance.
6. What is the magnetic energy density?

---

