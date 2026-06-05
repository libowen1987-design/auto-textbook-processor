---
chapter: 6
title: Analytical Absorbing Boundary Conditions
book: Computational Electrodynamics — The Finite-Difference Time-Domain Method (3rd Ed.)
author: Allen Taflove, Susan C. Hagness
raw_size: 91,684 bytes
sections: 5
---

# Chapter 6: Analytical Absorbing Boundary Conditions

## 6.1 Introduction

FDTD models of open-region problems require the computational domain to be truncated by an **absorbing boundary condition (ABC)** that simulates extension to infinity. ABCs permit outward-propagating numerical waves to exit the domain with minimal spurious reflection.

ABCs cannot be directly obtained from the central-difference Yee algorithm, which requires field values one-half cell outside the boundary. Modern ABCs achieve reflection coefficients of $10^{-4}$ to $10^{-6}$, enabling 70+ dB dynamic range.

Four major ABC theory thrusts:
- **Bayliss-Turkel** radiation operators (annihilation of radially propagating waves)
- **Engquist-Majda** one-way wave equations (pseudodifferential operator factorization)
- **Mur** finite-difference scheme (practical implementation of Engquist-Majda)
- **Higdon** radiation operators (annihilation by incidence angle)

> **Numerical Intuition:** Analytical ABCs are approximate — they reflect 1-5% of outgoing wave energy at normal incidence, rising to ~50% at grazing angles. For most engineering problems this is acceptable, but PML (Ch7) is preferred for high-dynamic-range simulations.

---

## 6.2 Bayliss-Turkel Radiation Operators

Based on the asymptotic expansion of outgoing wave solutions in spherical or cylindrical coordinates.

### Spherical Coordinates

For a spherical wave $u(R, \theta, \phi, t)$ satisfying the scalar wave equation in 3D, the far-field expansion is:

$$u(R, \theta, \phi, t) = \sum_{n=1}^{\infty} \frac{f_n(\theta, \phi, t - R/c)}{R^n} \tag{6.2}$$

The **Bayliss-Turkel operator of order 1**:

$$B_1 = \frac{\partial}{\partial R} + \frac{1}{R} + \frac{1}{c}\frac{\partial}{\partial t} \tag{6.3}$$

$$B_1 u = O(R^{-3}) \tag{eliminates the $R^{-1}$ term}$$

**Order 2 operator:**

$$B_2 = \left(\frac{\partial}{\partial R} + \frac{3}{R} + \frac{1}{c}\frac{\partial}{\partial t}\right) \left(\frac{\partial}{\partial R} + \frac{1}{R} + \frac{1}{c}\frac{\partial}{\partial t}\right) \tag{6.7}$$

$$B_2 u = O(R^{-5})$$

General $n$th-order operator:

$$B_n = \prod_{k=1}^n \left(\frac{\partial}{\partial R} + \frac{2k-1}{R} + \frac{1}{c}\frac{\partial}{\partial t}\right) \tag{6.10}$$

### Cylindrical Coordinates (2D)

Far-field expansion for cylindrical waves:

$$u(r, \phi, t) = \sum_{n=0}^{\infty} \frac{g_n(\phi, t - r/c)}{r^{n+1/2}} \tag{6.12}$$

First-order cylindrical operator:

$$B_1^c = \frac{\partial}{\partial r} + \frac{1}{2r} + \frac{1}{c}\frac{\partial}{\partial t} \tag{6.15}$$

---

## 6.3 Engquist-Majda One-Way Wave Equations

Based on factoring the 2D scalar wave operator:

$$\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}\right) U = 0 \tag{6.20}$$

The operator can be factored as $G = G^- G^+$ where:

$$G^{\pm} = D_x \mp \frac{D_t}{c} \sqrt{1 - s^2}, \quad s = \frac{D_y}{(D_t/c)} \tag{6.23}$$

$G^-U = 0$ at $x=0$ (left boundary) and $G^+U = 0$ at $x=h$ (right boundary) are exact ABCs for waves impinging at any angle.

### 6.3.1 Taylor Series Approximations

**First-order (one-term):**
$$\frac{\partial U}{\partial x} - \frac{1}{c}\frac{\partial U}{\partial t} = 0 \quad \text{at } x=0 \tag{6.26}$$

This is simply a plane-wave propagator normal to the boundary.

**Second-order (two-term):**
$$\frac{\partial^2 U}{\partial x \partial t} - \frac{1}{c}\frac{\partial^2 U}{\partial t^2} + \frac{c}{2}\frac{\partial^2 U}{\partial y^2} = 0 \quad \text{at } x=0 \tag{6.28a}$$

**At $x = h$:**
$$\frac{\partial^2 U}{\partial x \partial t} + \frac{1}{c}\frac{\partial^2 U}{\partial t^2} - \frac{c}{2}\frac{\partial^2 U}{\partial y^2} = 0 \tag{6.28b}$$

**At $y = 0$:**
$$\frac{\partial^2 U}{\partial y \partial t} - \frac{1}{c}\frac{\partial^2 U}{\partial t^2} + \frac{c}{2}\frac{\partial^2 U}{\partial x^2} = 0 \tag{6.28c}$$

**At $y = h$:**
$$\frac{\partial^2 U}{\partial y \partial t} + \frac{1}{c}\frac{\partial^2 U}{\partial t^2} - \frac{c}{2}\frac{\partial^2 U}{\partial x^2} = 0 \tag{6.28d}$$

### 6.3.2 Mur Finite-Difference Scheme (Practical Implementation)

Mur discretized (6.28a) at the $x=0$ boundary using central differences expanded about an auxiliary point $(\tfrac12, j)$. For a square grid ($\Delta x = \Delta y = \Delta$):

**Second-order Mur ABC at $x=0$:**

$$W_{0,j}^{n+1} = -W_{1,j}^{n-1} + \frac{c\Delta t - \Delta}{c\Delta t + \Delta}(W_{1,j}^{n+1} + W_{0,j}^{n-1}) + \frac{2\Delta}{c\Delta t + \Delta}(W_{1,j}^n + W_{0,j}^n) + \frac{(c\Delta t)^2 \Delta}{2\Delta y^2(c\Delta t + \Delta)}(W_{0,j+1}^n - 2W_{0,j}^n + W_{0,j-1}^n + W_{1,j+1}^n - 2W_{1,j}^n + W_{1,j-1}^n) \tag{6.35}$$

**First-order Mur ABC at $x=0$:**

$$W_{0,j}^{n+1} = W_{1,j}^n + \frac{c\Delta t - \Delta}{c\Delta t + \Delta}(W_{1,j}^{n+1} - W_{0,j}^n) \tag{6.34}$$

### 3D Mur ABC

For a cubic cell $\Delta$:

$$W_{0,j,k}^{n+1} = -W_{1,j,k}^{n-1} + \frac{c\Delta t - \Delta}{c\Delta t + \Delta}(W_{1,j,k}^{n+1} + W_{0,j,k}^{n-1}) + \frac{2\Delta}{c\Delta t + \Delta}(W_{1,j,k}^n + W_{0,j,k}^n) + \frac{(c\Delta t)^2}{2\Delta(c\Delta t + \Delta)} \left[\nabla_{yz}^2 W_{0,j,k}^n + \nabla_{yz}^2 W_{1,j,k}^n\right]$$

where $\nabla_{yz}^2$ is the Laplacian in the y-z plane.

### 6.3.3 Trefethen-Halpern Generalized ABCs

Use rational function (Padé) approximations of $\sqrt{1-s^2}$ to improve wide-angle absorption:

$$\sqrt{1 - s^2} \approx 1 - \frac{s^2}{2} \quad \text{(Padé (2,0), Mur)}$$
$$\sqrt{1 - s^2} \approx \frac{1 - \frac{3}{4}s^2}{1 - \frac{1}{4}s^2} \quad \text{(Padé (2,2))}$$

### 6.3.4 Theoretical Reflection Coefficient

For a plane wave at incidence angle $\theta$ from normal:

$$R(\theta) = \left|\frac{\cos\theta - \sqrt{1 - s^2}}{\cos\theta + \sqrt{1 - s^2}}\right|$$

where $s = \sin\theta$. For the 2nd-order Mur (Padé (2,0)):

$$R_{\text{Mur}}(\theta) = \left|\frac{\cos\theta - (1 - \frac12 \sin^2\theta)}{\cos\theta + (1 - \frac12 \sin^2\theta)}\right|^2$$

---

## 6.4 Higdon Radiation Operators

Higdon's operator annihilates plane waves at specified incidence angles $\alpha_1, \alpha_2, \ldots, \alpha_L$:

$$\prod_{\ell=1}^L \left(\cos\alpha_\ell \frac{\partial}{\partial t} - c\frac{\partial}{\partial x}\right) U = 0 \quad \text{at } x=0 \tag{6.48}$$

**Properties:**
1. Exactly absorbs any combination of $2L$ plane waves at angles $\pm\alpha_\ell$
2. Theoretical reflection coefficient:

$$R(\theta) = -\prod_{\ell=1}^L \frac{\cos\alpha_\ell - \cos\theta}{\cos\alpha_\ell + \cos\theta} \tag{6.49}$$

3. Angles $\alpha_\ell$ can be optimized for the problem
4. Requires only 1D stencil normal to boundary — simple at corners
5. First-order Higdon $\equiv$ first-order Mur when $\alpha_1 = 0$

---

## 6.5 Liao Extrapolation ABC

Liao's ABC uses a space-time extrapolation via Newton backward-difference polynomials, requiring $N$ layers of interior grid points. For a wave speed $c$, the field at a boundary is extrapolated from interior points using a corrected Taylor series accounting for the wave propagation delay.

$$W_{0}^{n+1} = \sum_{k=1}^{N} (-1)^{k+1} C_k^N W_k^{n+1-k\beta}$$

where $\beta = \frac{c\Delta t}{\Delta x}$ and $C_k^N$ are binomial coefficients.

---

## Example 6.1: 1D FDTD — Mur First-Order ABC Performance

Compare Mur first-order ABC vs. a PEC boundary in 1D.

**Setup:** 200-cell grid, Gaussian pulse at center, 400 time steps.
- With Mur ABC: clean absorption at boundaries
- With PEC: full reflection

**Result:** Mur ABC absorbs >95% of incident energy at normal incidence.

---

## Example 6.2: 2D TM$_z$ — Mur Second-Order ABC

Compare second-order Mur ABC with first-order for plane waves at various incidence angles.

**Setup:** 100×100 grid, point source at center, 300 time steps.
- Measure $E_z$ at corner to compute reflection coefficient
- First-order Mur: $R \approx 1\%$ at normal, $>10\%$ at 60°
- Second-order Mur: $R < 1\%$ up to 50°, $<5\%$ at 70°

---

## Example 6.3: Higdon ABC with Optimized Angles

Apply 3rd-order Higdon ABC with $\alpha = [0^\circ, 30^\circ, 60^\circ]$.

**Setup:** 150×150 grid, dipole source offset from center.
- Measure reflection across incidence angles
- Higdon outperforms Mur at wide angles

---

## Audit Table

| Concept | Section | Key Equation | Implementation |
|---------|---------|-------------|----------------|
| Bayliss-Turkel spherical | 6.2 | (6.3), (6.7), (6.10) | — |
| Bayliss-Turkel cylindrical | 6.2 | (6.15) | — |
| Engquist-Majda factorization | 6.3 | (6.23) | — |
| First-order Taylor ABC | 6.3.1 | (6.26) | Example 6.1 |
| Second-order Taylor ABC | 6.3.1 | (6.28) | Example 6.2 |
| Mur finite-difference (1st) | 6.3.2 | (6.34) | Example 6.1 |
| Mur finite-difference (2nd) | 6.3.2 | (6.35) | Example 6.2 |
| Trefethen-Halpern Padé | 6.3.3 | — | — |
| Reflection coefficient | 6.3.4 | (6.40) | Example 6.2 |
| Higdon operator | 6.4 | (6.48), (6.49) | Example 6.3 |
| Liao extrapolation | 6.5 | — | — |

> **Numerical Intuition:** For most practical FDTD simulations, the second-order Mur ABC offers the best balance of simplicity and accuracy. It achieves $R < 1\%$ for angles up to 50° from normal. For wide-angle problems (e.g., sources near boundaries), Higdon's operator with optimized angles is preferred. However, PML (Ch7) has largely superseded analytical ABCs for high-accuracy work.
