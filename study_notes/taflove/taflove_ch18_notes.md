---
chapter: 18
title: "Unconditionally Stable FDTD Methods"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, F. Zheng, Z. Chen, Y. T. Lo"
raw_size: 53,397 bytes
---

# Chapter 18: Unconditionally Stable FDTD Methods

## 18.1 Introduction

Standard FDTD is **conditionally stable**: $\Delta t$ is bounded by the CFL limit. For problems with very small cells (fine features, high mesh grading), the time-step becomes prohibitively small. Unconditionally stable methods remove this bound, allowing $\Delta t$ set by accuracy rather than stability.

## 18.2 ADI-FDTD (Alternating Direction Implicit)

### 18.2.1 Formulation

Splits each time-step into two sub-steps. In sub-step 1, $x$-direction derivatives are implicit:

**Sub-step 1** ($n \to n+1/2$):
$$
E_x^{n+1/2} = E_x^n + \frac{\Delta t}{2\epsilon} \left[ \frac{\delta H_z}{\delta y} - \frac{\delta H_y^{n+1/2}}{\delta z} \right]
$$
$$
H_y^{n+1/2} = H_y^n + \frac{\Delta t}{2\mu} \left[ \frac{\delta E_x^{n+1/2}}{\delta z} - \frac{\delta E_z}{\delta x} \right]
$$

The $z$-directed derivatives are implicit, requiring solution of a tridiagonal system.

**Sub-step 2** ($n+1/2 \to n+1$):
$$
E_x^{n+1} = E_x^{n+1/2} + \frac{\Delta t}{2\epsilon} \left[ \frac{\delta H_z^{n+1}}{\delta y} - \frac{\delta H_y}{\delta z} \right]
$$

### 18.2.2 Tridiagonal System

The implicit step yields (for $E_x$ update):

$$
-\alpha E_x^{n+1/2}(k-1) + (1+2\alpha) E_x^{n+1/2}(k) - \alpha E_x^{n+1/2}(k+1) = RHS
$$

where $\alpha = \Delta t^2/(4\mu\epsilon\Delta z^2)$. This tridiagonal system is efficiently solved via Thomas algorithm in $O(N)$.

### 18.2.3 Accuracy

ADI-FDTD introduces:
- **Splitting error**: $O(\Delta t^2)$ — negligible when $\Delta t$ is at CFL or smaller
- **Numerical dispersion**: Increased for large $\Delta t$; the dispersion relation is:

$$
\left[ \frac{1}{c\Delta t} \sin\left(\frac{\omega\Delta t}{2}\right) \right]^2 = \sum_{\xi=x,y,z} \left[ \frac{1}{\Delta_\xi} \sin\left(\frac{k_\xi\Delta_\xi}{2}\right) \right]^2 \frac{1}{1 + (\Delta t^2/(4\mu\epsilon)) \sum \left[ \frac{1}{\Delta_\xi} \sin\left(\frac{k_\xi\Delta_\xi}{2}\right) \right]^2 }
$$

For $\Delta t \ll$ CFL, reduces to standard FDTD dispersion.

## 18.3 Crank-Nicolson FDTD

### CN Scheme
Applies Crank-Nicolson time-stepping (trapezoidal integration) directly:

$$
\frac{\mathbf{U}^{n+1} - \mathbf{U}^n}{\Delta t} = \frac{1}{2} \left[ \mathbf{A}\mathbf{U}^{n+1} + \mathbf{A}\mathbf{U}^n \right]
$$

where $\mathbf{U} = [E_x, E_y, E_z, H_x, H_y, H_z]^T$. This yields:

$$
\left( \mathbf{I} - \frac{\Delta t}{2} \mathbf{A} \right) \mathbf{U}^{n+1} = \left( \mathbf{I} + \frac{\Delta t}{2} \mathbf{A} \right) \mathbf{U}^n
$$

### CNSS (Crank-Nicolson Split-Step)
Splits the 3D Maxwell operator into three 1D operators:

$$
\mathbf{U}^{n+1} = \prod_{\xi=x,y,z} \left( \mathbf{I} - \frac{\Delta t}{2} \mathbf{A}_\xi \right)^{-1} \left( \mathbf{I} + \frac{\Delta t}{2} \mathbf{A}_\xi \right) \mathbf{U}^n
$$

Each 1D step requires only tridiagonal solves, making CNSS more efficient than full CN.

## 18.4 Laguerre-FDTD

Uses Laguerre polynomials as temporal basis functions:

$$
E(r, t) = \sum_{p=0}^P E_p(r) L_p(\zeta t) e^{-\zeta t/2}
$$

where $L_p$ is the $p$th Laguerre polynomial. This eliminates the time-marching entirely:
- All temporal derivatives are handled analytically by Laguerre properties
- A **single** large sparse matrix equation is solved for all expansion coefficients
- No CFL constraint — the only constraint is $P$ (number of temporal basis functions)

### Implementation
The time-domain Maxwell equations become:
$$
\left( \nabla \times \right) \mathbf{H}_p = \left( \frac{\zeta}{2} + jp \zeta \right) \epsilon \mathbf{E}_p + \mathbf{J}_p
$$
$$
\left( \nabla \times \right) \mathbf{E}_p = -\left( \frac{\zeta}{2} + jp \zeta \right) \mu \mathbf{H}_p
$$

A marching-on-in-order scheme solves for $\mathbf{E}_p$, $\mathbf{H}_p$ sequentially from $p=0$ to $P$.

## 18.5 Comparison

| Method | System Size | Accuracy | Implementation | Parallel |
|--------|------------|----------|---------------|----------|
| ADI-FDTD | Tridiagonal (×6) | $O(\Delta t^2)$ error | Moderate | Good |
| CN-FDTD | Large sparse | $O(\Delta t^2)$ | Complex | Poor |
| CNSS | Tridiagonal (×3) | $O(\Delta t^2)$ | Moderate | Good |
| Laguerre-FDTD | Large sparse | Spectral in time | Very complex | Poor |

### Practical Guidance
- **ADI-FDTD** is the most widely used unconditionally stable method
- For $\Delta t \leq 5\times$ CFL, accuracy is acceptable
- For $\Delta t > 10\times$ CFL, dispersion error becomes significant
- Laguerre-FDTD is useful for problems requiring very long simulation times (high-Q cavities)
