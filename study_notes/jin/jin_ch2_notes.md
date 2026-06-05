---
title: "Chapter 2 — Electromagnetic Radiation in Free Space"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Scalar & vector potentials (static and time-harmonic)
  - Lorenz gauge condition
  - Free-space Green's function
  - Dyadic Green's functions
  - Hertzian dipole radiation
  - Far-field approximation, directivity, radiation resistance
  - Finite dipole, current loop, surface current, phased arrays
  - Sommerfeld radiation condition
---

# Chapter 2: Electromagnetic Radiation in Free Space

## 2.1 Scalar and Vector Potentials

### 2.1.1 Static Fields

**Electrostatics** — irrotational $\mathbf{E}$:

$$
\mathbf{E} = -\nabla \varphi, \quad \nabla^2 \varphi = -\frac{\varrho_e}{\epsilon}
\tag{2.1.8, 2.1.10}
$$

Solution (Poisson):

$$
\varphi(\mathbf{r}) = \frac{1}{4\pi\epsilon} \iiint_V \frac{\varrho_e(\mathbf{r}')}{R} dV', \quad R = |\mathbf{r} - \mathbf{r}'|
\tag{2.1.11}
$$

**Magnetostatics** — solenoidal $\mathbf{B}$:

$$
\mathbf{B} = \nabla \times \mathbf{A}, \quad \nabla^2 \mathbf{A} = -\mu \mathbf{J}
\tag{2.1.13, 2.1.17}
$$

**Coulomb gauge:** $\nabla \cdot \mathbf{A} = 0$ (simplifies the vector Poisson equation).

**Example 2.1** — Potential of a static electric dipole $\mathbf{p} = q\mathbf{l}$ at $\mathbf{r}'$:

$$
\varphi(\mathbf{r}) = \frac{\mathbf{p} \cdot (\mathbf{r} - \mathbf{r}')}{4\pi\epsilon_0 |\mathbf{r} - \mathbf{r}'|^3}
$$

For a polarized dielectric $\mathbf{P}(\mathbf{r})$: equivalent volume charge $\varrho_{e,b} = -\nabla \cdot \mathbf{P}$ and surface charge $\varrho_{e,b,s} = \hat{n} \cdot \mathbf{P}$.

**Example 2.2** — Vector potential of a magnetic dipole $\mathbf{m} = I\mathbf{s}$:

$$
\mathbf{A}(\mathbf{r}) = \frac{\mu_0 \mathbf{m} \times (\mathbf{r} - \mathbf{r}')}{4\pi |\mathbf{r} - \mathbf{r}'|^3}
$$

For a magnetized medium $\mathbf{M}(\mathbf{r})$: equivalent volume current $\mathbf{J}_m = \nabla \times \mathbf{M}$ and surface current $\mathbf{J}_{m,s} = -\hat{n} \times \mathbf{M}$.

**Example 2.3** — Magnetic scalar potential $\varphi_m$ for source-free regions: $\mathbf{H} = -\nabla\varphi_m$, $\nabla^2\varphi_m = 0$.

### 2.1.2 Time-Harmonic Fields and Lorenz Gauge

Decompose fields into electric-source ($\mathbf{E}_e, \mathbf{H}_e$) and magnetic-source ($\mathbf{E}_m, \mathbf{H}_m$) contributions.

**Magnetic vector potential $\mathbf{A}$** (from electric current $\mathbf{J}$):

$$
\mathbf{B}_e = \nabla \times \mathbf{A}, \quad \mathbf{E}_e = -j\omega\mathbf{A} + \frac{1}{j\omega\mu\epsilon} \nabla(\nabla \cdot \mathbf{A})
$$

**Lorenz gauge:**

$$
\nabla \cdot \mathbf{A} = -j\omega\mu\epsilon \varphi
\tag{2.1.29}
$$

**Vector Helmholtz equation:**

$$
\nabla^2 \mathbf{A} + k^2 \mathbf{A} = -\mu \mathbf{J}
\tag{2.1.30}
$$

**Electric vector potential $\mathbf{F}$** (from magnetic current $\mathbf{M}$):

$$
\mathbf{D}_m = -\nabla \times \mathbf{F}, \quad \mathbf{H}_m = -j\omega\mathbf{F} + \frac{1}{j\omega\mu\epsilon} \nabla(\nabla \cdot \mathbf{F})
$$

$$
\nabla^2 \mathbf{F} + k^2 \mathbf{F} = -\epsilon \mathbf{M}
\tag{2.1.36}
$$

**Total field:**

$$
\mathbf{E} = -j\omega\mathbf{A} + \frac{1}{j\omega\mu\epsilon} \nabla(\nabla \cdot \mathbf{A}) - \frac{1}{\epsilon} \nabla \times \mathbf{F}
\tag{2.1.37}
$$

$$
\mathbf{H} = \frac{1}{\mu} \nabla \times \mathbf{A} - j\omega\mathbf{F} + \frac{1}{j\omega\mu\epsilon} \nabla(\nabla \cdot \mathbf{F})
\tag{2.1.38}
$$

## 2.2 Solution of Vector Potentials in Free Space

### 2.2.1-2.2.2 Green's Function

**Free-space scalar Green's function:**

$$
G_0(\mathbf{r}, \mathbf{r}') = \frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{4\pi |\mathbf{r} - \mathbf{r}'|}
\tag{2.2.20}
$$

Satisfies:
$$
\nabla^2 G_0 + k^2 G_0 = -\delta(\mathbf{r} - \mathbf{r}')
$$

### 2.2.3 Field–Source Relations

$$
\mathbf{A}(\mathbf{r}) = \frac{\mu}{4\pi} \iiint_V \mathbf{J}(\mathbf{r}') \frac{e^{-jkR}}{R} dV'
\tag{2.2.21}
$$

$$
\mathbf{F}(\mathbf{r}) = \frac{\epsilon}{4\pi} \iiint_V \mathbf{M}(\mathbf{r}') \frac{e^{-jkR}}{R} dV'
\tag{2.2.22}
$$

### 2.2.4 Why Auxiliary Potentials?

They avoid differentiating discontinuous source functions (line/surface currents). Potentials are always smooth ($e^{-jkR}/R$), so their derivatives exist.

**Example 2.4** — Wave equation in inhomogeneous dielectric $\epsilon(\mathbf{r})$:

$$
\nabla^2 \mathbf{E} + k^2(\mathbf{r}) \mathbf{E} + \nabla[\mathbf{E} \cdot \nabla \ln \epsilon(\mathbf{r})] = 0
$$

### 2.2.5 Dyadic Green's Functions

**Electric dyadic Green's function:**

$$
\overline{\mathbf{G}}_{e0}(\mathbf{r}, \mathbf{r}') = \left( \overline{\mathbf{I}} + \frac{1}{k^2} \nabla\nabla \right) G_0(\mathbf{r}, \mathbf{r}')
\tag{2.2.36}
$$

**Magnetic dyadic Green's function:**

$$
\overline{\mathbf{G}}_{m0}(\mathbf{r}, \mathbf{r}') = \nabla G_0(\mathbf{r}, \mathbf{r}') \times \overline{\mathbf{I}}
\tag{2.2.37}
$$

Compact field expression:

$$
\mathbf{E}(\mathbf{r}) = -j\omega\mu \iiint_V \overline{\mathbf{G}}_{e0} \cdot \mathbf{J} \, dV' - \iiint_V \overline{\mathbf{G}}_{m0} \cdot \mathbf{M} \, dV'
\tag{2.2.35}
$$

## 2.3 Electromagnetic Radiation in Free Space

### 2.3.1 Infinitesimal Electric Dipole (Hertzian Dipole)

$z$-directed dipole of length $l \to 0$, current $I$, at origin.

**Vector potential:**

$$
\mathbf{A}(\mathbf{r}) = \hat{z} \frac{\mu I l}{4\pi r} e^{-jkr}
\tag{2.3.1}
$$

**Fields (all space, $k = \omega\sqrt{\mu\epsilon}$):**

$$
H_\phi = \frac{jk Il \sin\theta}{4\pi r} \left( 1 + \frac{1}{jkr} \right) e^{-jkr}
\tag{2.3.4}
$$

$$
E_r = \frac{\eta Il \cos\theta}{2\pi r^2} \left( 1 + \frac{1}{jkr} \right) e^{-jkr}
$$

$$
E_\theta = \frac{jk\eta Il \sin\theta}{4\pi r} \left[ 1 + \frac{1}{jkr} - \frac{1}{(kr)^2} \right] e^{-jkr}
\tag{2.3.5}
$$

**Far-field ($kr \gg 1$):**

$$
E_\theta \approx \frac{jk\eta Il \sin\theta}{4\pi r} e^{-jkr}, \quad
H_\phi \approx \frac{jk Il \sin\theta}{4\pi r} e^{-jkr}
\tag{2.3.6}
$$

**Power density:**

$$
\langle \mathbf{S} \rangle = \hat{r} \frac{\eta}{2} \left| \frac{kIl \sin\theta}{4\pi r} \right|^2
\tag{2.3.7}
$$

**Directivity:** $D_0 = 1.5$, **Radiation resistance:** $R_r = 20\pi^2 (l/\lambda)^2 \eta/\eta_0$ (for free space $R_r = 80\pi^2 (l/\lambda)^2$).

### 2.3.2 Finite Electric Dipole

Current distribution on a center-fed dipole of length $L$:

$$
I(z) = I_0 \sin[k(L/2 - |z|)]
$$

The far-field is found by integrating the contributions from infinitesimal dipoles along the wire.

**Example 2.6** — Field radiated by a dipole of length $L$, and the influence of current standing-wave pattern.

**Half-wave dipole ($L = \lambda/2$):** directivity $D_0 \approx 1.64$, input resistance $R_{\text{in}} \approx 73~\Omega$.

**Full-wave dipole ($L = \lambda$):** $D_0 \approx 2.41$.

### 2.3.3 Small Circular Current Loop (Magnetic Dipole)

For a loop of radius $a$ carrying current $I$, in the far field:

$$
E_\phi \approx \frac{\eta k^2 I \pi a^2 \sin\theta}{4\pi r} e^{-jkr}
$$

$$
H_\theta \approx -\frac{k^2 I \pi a^2 \sin\theta}{4\pi r} e^{-jkr}
$$

### 2.3.4 Radiation from Surface Currents — Aperture radiation

Aperture fields $\rightarrow$ equivalent currents $\mathbf{J}_s$, $\mathbf{M}_s$ $\rightarrow$ radiated fields via integration of dyadic Green's functions.

### 2.3.5 Radiation from Phased Arrays

Array factor for $N$ elements spaced $d$ apart, phase shift $\alpha$:

$$
AF(\theta) = \sum_{n=0}^{N-1} e^{jn(kd\cos\theta + \alpha)}
$$

### 2.3.6 Sommerfeld Radiation Condition

At infinity, fields must behave as outgoing spherical waves:

$$
\lim_{r\to\infty} r \left( \frac{\partial \mathbf{E}}{\partial r} + jk \mathbf{E} \right) = 0
$$

This selects the physically meaningful (outgoing) solution.

---

## Key Physical Intuition

1. **Potentials simplify radiation problems.** Instead of directly solving coupled Maxwell equations, we solve Helmholtz equations for $\mathbf{A}$ and $\mathbf{F}$, then differentiate to get fields.
2. **The Lorenz gauge** decouples $\mathbf{A}$ and $\varphi$, yielding two independent Helmholtz equations.
3. **$G_0 = e^{-jkR}/(4\pi R)$ represents an outgoing spherical wave** — the fundamental building block for any source distribution via superposition.
4. **The Hertzian dipole is the elementary radiator.** Any antenna can be modeled as a superposition of infinitesimal dipoles.
5. **Dyadic Green's functions** compactly represent the field due to a point current source, analogous to scalar Green's functions but handling the full vector nature.

---

## Original Examples in This Chapter

| Example | Topic | Section |
|---------|-------|---------|
| 2.1 | Potential of electric dipole → polarized dielectric | 2.1.1 |
| 2.2 | Vector potential of current loop → magnetized medium | 2.1.1 |
| 2.3 | Magnetic scalar potential for source-free region | 2.1.1 |
| 2.4 | Wave equation for inhomogeneous $\epsilon(\mathbf{r})$ | 2.2.4 |
| 2.5 | (Direct field-source relation) | 2.2.5 |
| 2.6 | Finite dipole radiation (far field + pattern) | 2.3.2 |

---

## Audit

| Section | Content Coverage | Notes Alignment |
|---------|-----------------|-----------------|
| 2.1 | Scalar/vector potentials, static and dynamic | Full coverage |
| 2.2 | Green's function, field-source relations, dyadics | Full coverage |
| 2.3 | Radiation from dipoles, loops, arrays | Full coverage |
| Examples | All 6 examples | Identified with original numbers |
