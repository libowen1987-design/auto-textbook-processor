---
chapter: 4
title: Numerical Dispersion and Stability
book: Computational Electrodynamics — The Finite-Difference Time-Domain Method (3rd Ed.)
author: Allen Taflove, Susan C. Hagness
---

# Chapter 4: Numerical Dispersion and Stability

## 4.1 Introduction

FDTD algorithms cause **nonphysical dispersion** — the phase velocity of numerical wave modes differs from $c$, varying with wavelength, propagation direction, and grid discretization. Think of a tenuous "numerical ether" causing phase errors, pulse broadening, ringing, anisotropy, and pseudorefraction.

The time-step $\Delta t$ also has a **specific bound** (CFL condition) required to avoid numerical instability.

---

## 4.2 Derivation of 2D Numerical Dispersion Relation

Starting from the 2D TM$_z$ Yee equations (lossless):

$$
\frac{\partial H_x}{\partial t} = -\frac{1}{\mu}\frac{\partial E_z}{\partial y},\quad
\frac{\partial H_y}{\partial t} = \frac{1}{\mu}\frac{\partial E_z}{\partial x},\quad
\frac{\partial E_z}{\partial t} = \frac{1}{\varepsilon}\left[\frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y}\right] \tag{4.1}
$$

Following substitution of a monochromatic plane wave trial solution:

$$
E_z\big|^n_{i,j} = E_{z0}\, e^{j(\omega n\Delta t - \tilde{k}_x i\Delta x - \tilde{k}_y j\Delta y)} \tag{4.3a}
$$

The derived dispersion relation for the 2D Yee algorithm (square cell, $\Delta x = \Delta y = \Delta$):

$$
\left[\frac{1}{S^2}\sin^2\left(\frac{\omega\Delta t}{2}\right)\right] = 
\sin^2\left(\frac{\tilde{k}_x\Delta}{2}\right) + \sin^2\left(\frac{\tilde{k}_y\Delta}{2}\right) \tag{4.5}
$$

In terms of propagation angle $\phi$ and grid sampling density $N_\lambda = \lambda_0/\Delta$:

$$
\frac{1}{S^2}\sin^2\left(\frac{\pi S}{N_\lambda}\right) = 
\sin^2\left(\frac{\Delta k\cos\phi}{2}\right) + \sin^2\left(\frac{\Delta k\sin\phi}{2}\right) \tag{4.6}
$$

### Numerical Phase Velocity

**Along major axes** ($\phi = 0^\circ, 90^\circ$):

$$
k = \frac{2}{\Delta}\sin^{-1}\left[\frac{1}{S}\sin\left(\frac{\pi S}{N_\lambda}\right)\right],\quad
\frac{v_p}{c} = \frac{\pi}{N_\lambda S}\cdot\frac{1}{\sin^{-1}\left[\frac{1}{S}\sin\left(\frac{\pi S}{N_\lambda}\right)\right]} \tag{4.14}
$$

**Along grid diagonals** ($\phi = 45^\circ$):

$$
k = \frac{2\sqrt{2}}{\Delta}\sin^{-1}\left[\frac{1}{S\sqrt{2}}\sin\left(\frac{\pi S}{N_\lambda}\right)\right],\quad
\frac{v_p}{c} = \frac{\pi}{N_\lambda S}\cdot\frac{1}{\sqrt{2}\sin^{-1}\left[\frac{1}{S\sqrt{2}}\sin\left(\frac{\pi S}{N_\lambda}\right)\right]} \tag{4.15}
$$

---

## 4.3 Extension to 3D

The 3D numerical dispersion relation:

$$
\left[\frac{1}{c\Delta t}\sin\left(\frac{\omega\Delta t}{2}\right)\right]^2 = 
\left[\frac{1}{\Delta x}\sin\left(\frac{\tilde{k}_x\Delta x}{2}\right)\right]^2 + 
\left[\frac{1}{\Delta y}\sin\left(\frac{\tilde{k}_y\Delta y}{2}\right)\right]^2 + 
\left[\frac{1}{\Delta z}\sin\left(\frac{\tilde{k}_z\Delta z}{2}\right)\right]^2 \tag{4.12}
$$

### 4.4 Comparison with Ideal

Ideal (continuous) dispersion:

$$
\left(\frac{\omega}{c}\right)^2 = k_x^2 + k_y^2 + k_z^2 \tag{4.13}
$$

(4.12) → (4.13) as $\Delta x, \Delta y, \Delta z, \Delta t \to 0$.

**Special cases where numerical = ideal:**
- 3D diagonal propagation with $S = 1/\sqrt{3}$
- 2D diagonal propagation with $S = 1/\sqrt{2}$
- 1D with $S = 1$ (magic time-step)

---

## 4.5 Anisotropy of Numerical Phase Velocity

For $S = 0.5$, $N_\lambda = 20$:
- Along axes: $v_p = 0.996892c$
- Along diagonals: $v_p = 0.998968c$
- Anisotropy: ~0.2%

For $S = 1/\sqrt{2}$, $N_\lambda = 20$:
- Along axes: $v_p < c$ (subluminal)
- Along diagonals: $v_p = c$ (ideal)
- The diagonal direction achieves zero dispersion at $S = 1/\sqrt{2}$

### 4.5.2 Intrinsic Grid Velocity Anisotropy

The Yee grid is fundamentally anisotropic for numerical wave propagation. This anisotropy decreases with finer sampling ($\propto 1/N_\lambda^2$) and is minimized when $S$ is close to the stability limit.

> **Numerical Intuition:** For large electrically-sized problems (many $\lambda$), the cumulative phase error from anisotropy can cause serious problems (e.g., incorrect beam direction in phased arrays). Rule of thumb: $N_\lambda \geq 20$ for < 1% phase velocity error.

---

## 4.6 Complex-Valued Numerical Wavenumbers

When the grid sampling is too coarse ($N_\lambda < \pi/S$), $\tilde{k}$ becomes complex → numerical waves become evanescent (attenuate exponentially with distance). Two regimes:

### 4.6.1 Propagation Along Principal Axes

Cutoff occurs when $\frac{1}{S}\sin\left(\frac{\pi S}{N_\lambda}\right) > 1$ → $N_\lambda < \pi S / \arcsin(S)$

### 4.6.2 Propagation Along Diagonal

Cutoff at finer sampling → diagonal propagation is more robust to coarse grids.

---

## 4.7 Numerical Stability (CFL Condition)

### Complex-Frequency Analysis

Allow $\tilde{\omega} = \omega_{\text{real}} + j\omega_{\text{imag}}$ and analyze (4.12):

Define:
$$
\xi = c\Delta t \sqrt{\frac{\sin^2\left(\frac{k_x\Delta x}{2}\right)}{(\Delta x)^2} + \frac{\sin^2\left(\frac{k_y\Delta y}{2}\right)}{(\Delta y)^2} + \frac{\sin^2\left(\frac{k_z\Delta z}{2}\right)}{(\Delta z)^2}} \tag{4.51b}
$$

Maximum $\xi$ when all sine² terms = 1:

$$
0 \leq \xi \leq c\Delta t \sqrt{\frac{1}{(\Delta x)^2} + \frac{1}{(\Delta y)^2} + \frac{1}{(\Delta z)^2}} \tag{4.52}
$$

**Stable:** $\xi \leq 1$ → real $\tilde{\omega}$ → bounded amplitude  
**Unstable:** $\xi > 1$ → complex $\tilde{\omega}$ with $\omega_{\text{imag}} < 0$ → exponential growth

### 3D CFL Condition

$$
\Delta t \leq \frac{1}{c\sqrt{\frac{1}{(\Delta x)^2} + \frac{1}{(\Delta y)^2} + \frac{1}{(\Delta z)^2}}} \tag{4.54}
$$

**Special cases:**
- **Cubic cell ($\Delta$):** $\Delta t \leq \Delta / (c\sqrt{3})$
- **Square cell 2D:** $\Delta t \leq \Delta / (c\sqrt{2})$
- **Uniform 1D:** $\Delta t \leq \Delta / c$

**Growth factor for unstable case ($S > S_{\max}$):**

$$
q_{\text{growth}} = \xi + \sqrt{\xi^2 - 1} > 1 \quad \text{per time-step} \tag{4.55}
$$

> **Numerical Intuition:** The CFL condition ensures that the numerical domain of dependence contains the physical domain of dependence. Violating CFL means the numerical wave "skips over" information it needs, causing unbounded growth — typically at the Nyquist mode (2-cell wavelength).

---

## 4.8 Summary

| Concept | Expression | Notes |
|---------|-----------|-------|
| 2D numerical dispersion | (4.5) or (4.6) | Square-cell TM$_z$ |
| 3D numerical dispersion | (4.12) | Full-vector Yee |
| Ideal dispersion | (4.13) | Continuous limit |
| Phase velocity (axis) | (4.14) | $v_p < c$ for $S < 1$ |
| Phase velocity (diagonal) | (4.15) | $v_p = c$ when $S = 1/\sqrt{2}$ |
| CFL 3D | $\Delta t \leq 1/(c\sqrt{1/\Delta x^2 + 1/\Delta y^2 + 1/\Delta z^2})$ | Cubic: $\Delta t \leq \Delta/(c\sqrt{3})$ |
| CFL 2D | $\Delta t \leq \Delta/(c\sqrt{2})$ | Square cell |
| CFL 1D | $\Delta t \leq \Delta/c$ | Magic step |
| Anisotropy | $\propto 1/N_\lambda^2$ | Reduces with finer grids |

---

## Ch.4 Example Code

1. **Ex4.1:** Dispersion curves — $v_p/c$ vs $N_\lambda$ for axis/diagonal propagation  
2. **Ex4.2:** Anisotropy visualization — 2D TM$_z$ simulation of cylindrical wave showing anisotropic wavefront  
3. **Ex4.3:** CFL stability — energy growth monitor for stable ($S=0.5$), marginal ($S=1/\sqrt{2}$), unstable ($S=1$)

See: `taflove_ch4_examples.py`

---

## Chapter Audit

| Section | Content | ✓ |
|---------|---------|:-:|
| 4.1 | Introduction | ✓ |
| 4.2 | 2D numerical dispersion | ✓ |
| 4.3 | 3D extension | ✓ |
| 4.4 | Comparison with ideal | ✓ |
| 4.5 | Anisotropy of $v_p$ | ✓ |
| 4.5.1 | Sample values | ✓ |
| 4.5.2 | Intrinsic anisotropy | ✓ |
| 4.6 | Complex wavenumbers | ✓ Summary |
| 4.7 | Numerical stability | ✓ |
| 4.7.1 | Complex-frequency analysis | ✓ |
| 4.7.2 | Growth rate | ✓ |
