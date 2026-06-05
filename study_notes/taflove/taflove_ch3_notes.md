---
chapter: 3
title: Introduction to Maxwell's Equations and the Yee Algorithm
book: Computational Electrodynamics — The Finite-Difference Time-Domain Method (3rd Ed.)
author: Allen Taflove, Susan C. Hagness
---

# Chapter 3: Introduction to Maxwell's Equations and the Yee Algorithm

## 3.1 Introduction

This chapter presents the foundation of FDTD electromagnetic field analysis — the **Yee algorithm** (1966) [1]. Yee's insight was to choose a geometry for spatially sampling E and H field components that robustly represents both the differential and integral forms of Maxwell's equations. No alternative gridding proposed in the ~40 years since has matched its seminal impact.

---

## 3.2 Maxwell's Equations in Three Dimensions

### Differential and Integral Forms

**Faraday's Law:**
$$
\frac{\partial\mathbf{B}}{\partial t} = -\nabla\times\mathbf{E} - \mathbf{M}
\qquad
\oint_L \mathbf{E}\cdot d\mathbf{L} = -\frac{\partial}{\partial t}\iint_A \mathbf{B}\cdot d\mathbf{A} - \iint_A \mathbf{M}\cdot d\mathbf{A} \tag{3.1}
$$

**Ampere's Law:**
$$
\frac{\partial\mathbf{D}}{\partial t} = \nabla\times\mathbf{H} - \mathbf{J}
\qquad
\oint_L \mathbf{H}\cdot d\mathbf{L} = \frac{\partial}{\partial t}\iint_A \mathbf{D}\cdot d\mathbf{A} + \iint_A \mathbf{J}\cdot d\mathbf{A} \tag{3.2}
$$

**Gauss' Law (electric):**
$$
\nabla\cdot\mathbf{D} = 0
\qquad
\oint_A \mathbf{D}\cdot d\mathbf{A} = 0 \tag{3.3}
$$

**Gauss' Law (magnetic):**
$$
\nabla\cdot\mathbf{B} = 0
\qquad
\oint_A \mathbf{B}\cdot d\mathbf{A} = 0 \tag{3.4}
$$

### Constitutive Relations (linear, isotropic, nondispersive)

$$
\mathbf{D} = \varepsilon\mathbf{E} = \varepsilon_r\varepsilon_0\mathbf{E}
\qquad
\mathbf{B} = \mu\mathbf{H} = \mu_r\mu_0\mathbf{H} \tag{3.5}
$$

where $\varepsilon_0 = 8.854\times10^{-12}$ F/m, $\mu_0 = 4\pi\times10^{-7}$ H/m.

### Lossy Media

For materials with isotropic, nondispersive electric and magnetic losses:

$$
\mathbf{J} = \mathbf{J}_\text{source} + \sigma\mathbf{E}
\qquad
\mathbf{M} = \mathbf{M}_\text{source} + \sigma^*\mathbf{H} \tag{3.6}
$$

where $\sigma$ = electric conductivity [S/m], $\sigma^*$ = equivalent magnetic loss [$\Omega$/m].

### Maxwell's Curl Equations in Lossy Media

Substituting (3.5) and (3.6) into (3.1a) and (3.2a):

$$
\frac{\partial\mathbf{H}}{\partial t} = -\frac{1}{\mu}\nabla\times\mathbf{E} - \frac{1}{\mu}(\mathbf{M}_\text{source} + \sigma^*\mathbf{H}) \tag{3.7}
$$

$$
\frac{\partial\mathbf{E}}{\partial t} = \frac{1}{\varepsilon}\nabla\times\mathbf{H} - \frac{1}{\varepsilon}(\mathbf{J}_\text{source} + \sigma\mathbf{E}) \tag{3.8}
$$

### Cartesian Component Equations

Expanding the curl operators yields six coupled scalar equations:

**H-field components:**
$$
\frac{\partial H_x}{\partial t} = \frac{1}{\mu}\left[\frac{\partial E_y}{\partial z} - \frac{\partial E_z}{\partial y} - (M_{\text{source},x} + \sigma^* H_x)\right] \tag{3.9a}
$$
$$
\frac{\partial H_y}{\partial t} = \frac{1}{\mu}\left[\frac{\partial E_z}{\partial x} - \frac{\partial E_x}{\partial z} - (M_{\text{source},y} + \sigma^* H_y)\right] \tag{3.9b}
$$
$$
\frac{\partial H_z}{\partial t} = \frac{1}{\mu}\left[\frac{\partial E_x}{\partial y} - \frac{\partial E_y}{\partial x} - (M_{\text{source},z} + \sigma^* H_z)\right] \tag{3.9c}
$$

**E-field components:**
$$
\frac{\partial E_x}{\partial t} = \frac{1}{\varepsilon}\left[\frac{\partial H_z}{\partial y} - \frac{\partial H_y}{\partial z} - (J_{\text{source},x} + \sigma E_x)\right] \tag{3.10a}
$$
$$
\frac{\partial E_y}{\partial t} = \frac{1}{\varepsilon}\left[\frac{\partial H_x}{\partial z} - \frac{\partial H_z}{\partial x} - (J_{\text{source},y} + \sigma E_y)\right] \tag{3.10b}
$$
$$
\frac{\partial E_z}{\partial t} = \frac{1}{\varepsilon}\left[\frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y} - (J_{\text{source},z} + \sigma E_z)\right] \tag{3.10c}
$$

> **Numerical Intuition:** These six equations are the core of FDTD. The Yee algorithm discretizes each into explicit update equations for every cell in the grid. Each E-component update uses four surrounding H-components (the curl), and vice versa, creating a self-consistent electromagnetic simulation.

---

## 3.3 Reduction to Two Dimensions

### 3.3.1 TM$_z$ Mode ($E_z, H_x, H_y$)

For structures invariant in $z$ with $\partial/\partial z = 0$, Maxwell's equations decouple into TM$_z$ and TE$_z$ modes.

TM$_z$ equations (components $E_z, H_x, H_y$):
$$
\frac{\partial H_x}{\partial t} = -\frac{1}{\mu}\frac{\partial E_z}{\partial y} \tag{3.13a}
$$
$$
\frac{\partial H_y}{\partial t} = \frac{1}{\mu}\frac{\partial E_z}{\partial x} \tag{3.13b}
$$
$$
\frac{\partial E_z}{\partial t} = \frac{1}{\varepsilon}\left[\frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y}\right] \tag{3.13c}
$$

### 3.3.2 TE$_z$ Mode ($H_z, E_x, E_y$)

TE$_z$ equations (components $H_z, E_x, E_y$):
$$
\frac{\partial E_x}{\partial t} = \frac{1}{\varepsilon}\frac{\partial H_z}{\partial y} \tag{3.14a}
$$
$$
\frac{\partial E_y}{\partial t} = -\frac{1}{\varepsilon}\frac{\partial H_z}{\partial x} \tag{3.14b}
$$
$$
\frac{\partial H_z}{\partial t} = \frac{1}{\mu}\left[\frac{\partial E_x}{\partial y} - \frac{\partial E_y}{\partial x}\right] \tag{3.14c}
$$

---

## 3.4 Reduction to One Dimension — TEM Modes

### 3.4.1 $x$-Directed, $z$-Polarized TEM Mode ($E_z, H_y$)

For fields invariant in $y$ and $z$, propagating in $x$:

$$
\frac{\partial H_y}{\partial t} = \frac{1}{\mu}\frac{\partial E_z}{\partial x} \tag{3.15a}
$$
$$
\frac{\partial E_z}{\partial t} = \frac{1}{\varepsilon}\frac{\partial H_y}{\partial x} \tag{3.15b}
$$

### 3.4.2 $x$-Directed, $y$-Polarized TEM Mode ($E_y, H_z$)

$$
\frac{\partial H_z}{\partial t} = -\frac{1}{\mu}\frac{\partial E_y}{\partial x} \tag{3.16a}
$$
$$
\frac{\partial E_y}{\partial t} = \frac{1}{\varepsilon}\frac{\partial H_z}{\partial x} \tag{3.16b}
$$

---

## 3.5 Equivalence to the Wave Equation in 1D

Starting from the 1D TEM mode equations (3.15a,b), differentiate (3.15b) by $t$ and (3.15a) by $x$:

$$
\frac{\partial^2 E_z}{\partial t^2} = \frac{1}{\varepsilon}\frac{\partial}{\partial t}\frac{\partial H_y}{\partial x}
= \frac{1}{\varepsilon}\frac{\partial}{\partial x}\frac{\partial H_y}{\partial t}
= \frac{1}{\varepsilon\mu}\frac{\partial^2 E_z}{\partial x^2}
$$

Since $c = 1/\sqrt{\mu\varepsilon}$:

$$
\frac{\partial^2 E_z}{\partial t^2} = c^2 \frac{\partial^2 E_z}{\partial x^2} \tag{3.20}
$$

The 1D Yee TEM mode discretization is equivalent to the scalar wave equation (Ch. 2).

---

## 3.6 The Yee Algorithm

### 3.6.1 Basic Ideas

1. **Solves both E and H** using coupled curl equations (not wave equation alone). This makes the solution more robust for a wider class of structures.
2. **Staggered spatial grid:** Every E component surrounded by four circulating H components, and vice versa (Fig. 3.1).
3. **Leapfrog time-stepping:** All E computations completed first, then all H computations using the new E data; cycle repeats (Fig. 3.2).

**Key attributes:**
- Central-difference space derivatives → second-order accurate
- Tangential E and H continuity naturally maintained at material interfaces parallel to coordinate axes (staircase approximation)
- Implicitly enforces Gauss' laws (divergence-free)
- Fully explicit → no matrix inversion needed
- Nondissipative: numerical waves do not spuriously decay

### 3.6.2 Finite Differences and Notation

Space point in rectangular lattice:
$$
(i, j, k) = (i\Delta x,\; j\Delta y,\; k\Delta z) \tag{3.21}
$$

Function of space and time:
$$
F^n(i, j, k) = F(i\Delta x, j\Delta y, k\Delta z, n\Delta t) \tag{3.22}
$$

Central-difference for space derivative (second-order accurate):
$$
\left.\frac{\partial F}{\partial x}\right|_{(i,j,k)}^n = \frac{F^n(i+\tfrac{1}{2}, j, k) - F^n(i-\tfrac{1}{2}, j, k)}{\Delta x} + O[(\Delta x)^2] \tag{3.23}
$$

### 3.6.3 Finite-Difference Expressions in 3D

**E-field update** (example for $E_x$ at $(i, j+\frac{1}{2}, k+\frac{1}{2})$):

$$
E_x\big|^{n+1/2}_{i, j+1/2, k+1/2} = C_{\text{ae}}\cdot E_x\big|^{n-1/2}_{i, j+1/2, k+1/2} + C_{\text{be}} \cdot \left[\frac{H_z|^{n}_{i, j+1, k+1/2} - H_z|^{n}_{i, j, k+1/2}}{\Delta y} - \frac{H_y|^{n}_{i, j+1/2, k+1} - H_y|^{n}_{i, j+1/2, k}}{\Delta z}\right] \tag{3.29a}
$$

where the loss coefficients are:

$$
C_{\text{ae}} = \frac{1 - \frac{\sigma\Delta t}{2\varepsilon}}{1 + \frac{\sigma\Delta t}{2\varepsilon}}, \qquad
C_{\text{be}} = \frac{\frac{\Delta t}{\varepsilon}}{1 + \frac{\sigma\Delta t}{2\varepsilon}} \tag{3.30}
$$

Similarly, $E_y$ and $E_z$ (3.29b, 3.29c) follow cyclic permutation of indices.

**H-field update** (example for $H_x$ at $(i-\frac{1}{2}, j+1, k+1)$):

$$
H_x\big|^{n+1}_{i-1/2, j+1, k+1} = C_{\text{ah}}\cdot H_x\big|^{n}_{i-1/2, j+1, k+1} - C_{\text{bh}} \cdot \left[\frac{E_z|^{n+1/2}_{i-1/2, j+1, k+1} - E_z|^{n+1/2}_{i-1/2, j, k+1}}{\Delta y} - \frac{E_y|^{n+1/2}_{i-1/2, j+1, k+1} - E_y|^{n+1/2}_{i-1/2, j+1, k}}{\Delta z}\right] \tag{3.31a}
$$

where:

$$
C_{\text{ah}} = \frac{1 - \frac{\sigma^*\Delta t}{2\mu}}{1 + \frac{\sigma^*\Delta t}{2\mu}}, \qquad
C_{\text{bh}} = \frac{\frac{\Delta t}{\mu}}{1 + \frac{\sigma^*\Delta t}{2\mu}} \tag{3.32}
$$

### 3.6.4 Space Region with Continuous Material Variation

For regions where $\varepsilon(x,y,z)$, $\mu(x,y,z)$, $\sigma(x,y,z)$, $\sigma^*(x,y,z)$ vary continuously, the values are assigned at each field component location. The update coefficients $C_{\text{ae}}, C_{\text{be}}, C_{\text{ah}}, C_{\text{bh}}$ are computed once at the start based on the local material parameters at each cell.

### 3.6.5 Space Region with Finite Number of Distinct Media

For piecewise-homogeneous media with interfaces parallel to coordinate axes:
- Tangential **E** and **H** continuity is automatically satisfied by the Yee algorithm due to the staggered grid.
- No special boundary condition enforcement needed at interfaces — simply assign the appropriate $\varepsilon, \mu, \sigma$ at each field component location.
- This yields a "staircase" approximation of non-grid-aligned surfaces.

### 3.6.6 Nonpermeable Media

For $\mu_r = 1$ (nonmagnetic materials widely used in practice), the C-coefficients simplify since $\mu = \mu_0$.

### 3.6.7 Reduction to 2D TM$_z$ and TE$_z$

**TM$_z$ Yee update:**

$$
E_z|^{n+1/2}_{i,j} = E_z|^{n-1/2}_{i,j} + \frac{\Delta t}{\varepsilon}\left[\frac{H_y|^{n}_{i+1/2,j} - H_y|^{n}_{i-1/2,j}}{\Delta x} - \frac{H_x|^{n}_{i,j+1/2} - H_x|^{n}_{i,j-1/2}}{\Delta y}\right] \tag{3.41}
$$

**TE$_z$ Yee update** follows similarly.

### 3.6.8 Interpretation via Integral Forms

The Yee algorithm simultaneously simulates the pointwise differential form and the macroscopic integral form of Maxwell's equations. Each $E$ update corresponds to Ampere's law integrated over a rectangular contour linking four surrounding $H$ components; each $H$ update corresponds to Faraday's law.

### 3.6.9 Divergence-Free Nature

The Yee algorithm implicitly enforces Gauss' laws:

$$
\nabla\cdot\mathbf{D} = 0, \qquad \nabla\cdot\mathbf{B} = 0
$$

This is because the central-difference curl operations in a staggered grid naturally preserve zero divergence in the absence of free charges. A rigorous proof follows from taking the divergence of the update equations and observing that $\nabla\cdot(\nabla\times\mathbf{H}) \equiv 0$.

---

## 3.7 Alternative Finite-Difference Grids

### 3.7.1 Cartesian Grids
Extensions to cartesian grids include nonuniform (graded) meshes, where $\Delta x$, $\Delta y$, $\Delta z$ vary across the grid, and subgridding (local mesh refinement in regions of interest).

### 3.7.2 Hexagonal Grids
Hexagonal (triangular) grids offer improved isotropy for numerical wave propagation compared to Cartesian grids, at the cost of more complex indexing.

---

## 3.8 Emerging Application: Gridding the Planet Earth

An emerging application illustrating 3D FDTD gridding concepts: modeling **impulsive ELF propagation** within the global Earth-ionosphere cavity.

**Key challenges:**
- Spherical Earth geometry → latitude-longitude grid with cell eccentricity near poles
- Converging lines of longitude → smaller cells near poles → reduced Courant limit

**Imnovation [21–23]:** Adaptive cell-combination in the East-West direction near poles to maintain approximately square cells → preserves time-step near equatorial limit.

**Applications:**
- ELF/VLF propagation in Earth-ionosphere waveguide
- Remote sensing of lightning, sprites, global temperature change
- Detection of electromagnetic precursors of major earthquakes
- Detection of underground ore/oil deposits

---

## 3.9 Summary

| Concept | Equation | Key Result |
|---------|----------|------------|
| Maxwell's curl eqs. | (3.7)–(3.8) | Six coupled scalar equations for E, H in lossy media |
| Yee unit cell | Fig. 3.1 | E and H staggered in space |
| Leapfrog time-stepping | Fig. 3.2 | E, H staggered in time |
| E-field update (3D, lossy) | (3.29) with (3.30) | Fully explicit, second-order accurate |
| H-field update (3D, lossy) | (3.31) with (3.32) | Fully explicit, second-order accurate |
| TM$_z$ 2D update | (3.41) | Three-component 2D FDTD |
| Divergence-free | Sec. 3.6.9 | Gauss' laws implicitly satisfied |
| CFL stability condition | (Ch. 4) | $\Delta t \leq 1/(c\sqrt{1/\Delta x^2 + 1/\Delta y^2 + 1/\Delta z^2})$ |

**Yee cell geometry (Fig. 3.1):** In one cubic unit cell of side $\Delta x = \Delta y = \Delta z = \delta$:
- $E_x$ located at $(i, j+1/2, k+1/2)$ — center of x-directed edge
- $E_y$ located at $(i+1/2, j, k+1/2)$ — center of y-directed edge  
- $E_z$ located at $(i+1/2, j+1/2, k)$ — center of z-directed edge
- $H_x$ located at $(i+1/2, j, k)$ — center of x-directed face
- $H_y$ located at $(i, j+1/2, k)$ — center of y-directed face
- $H_z$ located at $(i, j, k+1/2)$ — center of z-directed face

---

## Ch.3 Example Code

The code file implements:
1. **Ex3.1:** 1D FDTD (Ez, Hy) — TEM wave propagation with lossy medium
2. **Ex3.2:** 2D TM$_z$ FDTD — point source radiation in free space
3. **Ex3.3:** Yee cell visualization — schematic 3D unit cell with field components

See: `taflove_ch3_examples.py`

---

## Chapter Audit

| Section | Content | Notes |
|---------|---------|-------|
| 3.1 | Introduction | ✓ |
| 3.2 | Maxwell's eqs. in 3D | ✓ Full derivation |
| 3.3 | Reduction to 2D | ✓ TM$_z$, TE$_z$ |
| 3.4 | Reduction to 1D | ✓ TEM modes |
| 3.5 | Equivalence to wave eq. | ✓ |
| 3.6 | The Yee algorithm | ✓ Core update equations |
| 3.6.1–3.6.3 | Basic ideas, notation, FD expressions | ✓ |
| 3.6.4–3.6.5 | Material assignments | ✓ |
| 3.6.6 | Nonpermeable media | ✓ |
| 3.6.7 | 2D reduction | ✓ |
| 3.6.8 | Integral interpretation | ✓ |
| 3.6.9 | Divergence-free nature | ✓ |
| 3.7 | Alternative grids | ✓ Summary |
| 3.8 | Earth gridding | ✓ |
