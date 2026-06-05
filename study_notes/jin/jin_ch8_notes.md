---
title: "Chapter 8 — The Finite Difference Method"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Finite difference formulas (forward, backward, central)
  - 1D/2D wave equation FDM
  - FDTD: Yee cell, leapfrog scheme
  - Stability: CFL condition
  - Numerical dispersion
  - PML absorbing boundary conditions
---

# Chapter 8: The Finite Difference Method

## 8.1 Differencing Formulas

$$
f'(x) \approx \frac{f(x+\Delta x)-f(x)}{\Delta x} \quad\text{(forward)}
$$

$$
f'(x) \approx \frac{f(x)-f(x-\Delta x)}{\Delta x} \quad\text{(backward)}
$$

$$
f'(x) \approx \frac{f(x+\Delta x)-f(x-\Delta x)}{2\Delta x} \quad\text{(central)}
$$

$$
f''(x) \approx \frac{f(x+\Delta x)-2f(x)+f(x-\Delta x)}{\Delta x^2}
$$

## 8.2 FDTD Method

**Yee cell:** $\mathbf{E}$ on cell edges, $\mathbf{H}$ on cell faces, staggered in space and time (leapfrog).

**2D TEz update:**

$$
H_x|_{i,j}^{n+1/2} = H_x|_{i,j}^{n-1/2} - \frac{\Delta t}{\mu\Delta y} (E_z|_{i,j+1}^n - E_z|_{i,j}^n)
$$

$$
H_y|_{i,j}^{n+1/2} = H_y|_{i,j}^{n-1/2} + \frac{\Delta t}{\mu\Delta x} (E_z|_{i+1,j}^n - E_z|_{i,j}^n)
$$

$$
E_z|_{i,j}^{n+1} = E_z|_{i,j}^n + \frac{\Delta t}{\epsilon\Delta x} (H_y|_{i+1/2,j}^{n+1/2} - H_y|_{i-1/2,j}^{n+1/2}) - \frac{\Delta t}{\epsilon\Delta y} (H_x|_{i,j+1/2}^{n+1/2} - H_x|_{i,j-1/2}^{n+1/2})
$$

## 8.3 Stability: CFL Condition

$$
\Delta t \le \frac{1}{c\sqrt{1/\Delta x^2 + 1/\Delta y^2 + 1/\Delta z^2}}
$$

## 8.4 Numerical Dispersion

FDTD introduces artificial dispersion depending on grid resolution ($\lambda/\Delta x$).

## 8.5 PML (Perfectly Matched Layer)

Stretched-coordinate PML (Berenger 1994): split-field formulation.
UPML (uniaxial PML): anisotropic material absorber.

---

## Audit

| Section | Topic |
|---------|-------|
| 8.1 | Differencing formulas |
| 8.2 | FDTD scheme |
| 8.3 | CFL stability |
| 8.4 | Numerical dispersion |
| 8.5 | PML/UPML |
