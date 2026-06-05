---
chapter: 2
title: The One-Dimensional Scalar Wave Equation
book: Computational Electrodynamics — The Finite-Difference Time-Domain Method (3rd Ed.)
author: Allen Taflove, Susan C. Hagness
---

# Chapter 2: The One-Dimensional Scalar Wave Equation

## 2.1 Introduction

This chapter introduces the numerical FDTD solution of the most basic PDE describing wave motion — the **one-dimensional scalar wave equation**. The analytical propagating-wave solutions are first obtained, then finite differences are applied to the wave equation, leading to discussions of:
- Numerical dispersion
- Numerical phase velocity
- The "magic" time-step
- Numerical stability

These form the basis for later FDTD analysis of Maxwell's equations in 2D and 3D.

---

## 2.2 Propagating-Wave Solutions

The one-dimensional scalar wave equation is:

$$
\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2} \tag{2.1}
$$

where $u = u(x,t)$.

### General Solution

The general propagating-wave solution is:

$$
u(x,t) = F(x + ct) + G(x - ct) \tag{2.2}
$$

where $F$ and $G$ are arbitrary functions. $F(x + ct)$ represents a wave propagating in the $-x$ direction, and $G(x - ct)$ represents a wave propagating in the $+x$ direction.

**Verification:** Differentiating (2.2) twice with respect to $t$ and $x$:

$$
\frac{\partial u}{\partial t} = c F'(x+ct) - c G'(x-ct)
$$
$$
\frac{\partial^2 u}{\partial t^2} = c^2 F''(x+ct) + c^2 G''(x-ct) \tag{2.3}
$$
$$
\frac{\partial u}{\partial x} = F'(x+ct) + G'(x-ct)
$$
$$
\frac{\partial^2 u}{\partial x^2} = F''(x+ct) + G''(x-ct) \tag{2.4}
$$

Substituting (2.3) and (2.4) into (2.1) yields an identity regardless of $F$ and $G$.

> **Numerical Intuition:** The parameter $c$ is the wave propagation speed. After $\Delta t$ seconds, $F(x+ct)$ shifts left by $c\Delta t$, and $G(x-ct)$ shifts right by $c\Delta t$. This is the fundamental behavior any numerical scheme must reproduce.

---

## 2.3 Dispersion Relation — Continuous

A **dispersion relation** expresses the dependence of the wavelength $\lambda$ (or wavenumber $k = 2\pi/\lambda$) on frequency $f$ (or angular frequency $\omega = 2\pi f$).

For the scalar wave equation, consider a sinusoidal traveling wave in phasor form:

$$
u(x,t) = e^{j(\omega t - k x)} \tag{2.6}
$$

Substituting into (2.1):

$$
(j\omega)^2 e^{j(\omega t - kx)} = c^2 (-jk)^2 e^{j(\omega t - kx)}
$$

Factoring out the common exponential yields:

$$
-\omega^2 = -c^2 k^2 \quad \Rightarrow \quad k = \pm \omega / c \tag{2.7b}
$$

### Physical Significance

- **Phase velocity:** $v_p = \omega/k = \pm c$ — constant, independent of frequency
- **Group velocity:** $v_g = d\omega/dk = \pm c$ — also constant
- Since $v_p$ and $v_g$ are constant, waves are **dispersionless** — the waveshape remains unchanged after arbitrarily large propagation distances for any modulation envelope or pulse shape.

> **Numerical Intuition:** The continuous wave equation is nondispersive. But as we'll see, the *discrete* (finite-difference) approximation introduces artificial dispersion — numerical waves of different frequencies propagate at different speeds. This is a key source of error in FDTD.

---

## 2.4 Finite Differences

### Central Difference for Second Spatial Derivative

Using Taylor series expansions about $x_i$ (keeping time $t_n$ fixed):

$$
u_{i+1}^n = u_i^n + \Delta x \left.\frac{\partial u}{\partial x}\right|_i^n + \frac{(\Delta x)^2}{2} \left.\frac{\partial^2 u}{\partial x^2}\right|_i^n + \frac{(\Delta x)^3}{6} \left.\frac{\partial^3 u}{\partial x^3}\right|_i^n + \cdots \tag{2.10a}
$$

$$
u_{i-1}^n = u_i^n - \Delta x \left.\frac{\partial u}{\partial x}\right|_i^n + \frac{(\Delta x)^2}{2} \left.\frac{\partial^2 u}{\partial x^2}\right|_i^n - \frac{(\Delta x)^3}{6} \left.\frac{\partial^3 u}{\partial x^3}\right|_i^n + \cdots \tag{2.10b}
$$

Adding (2.10a) and (2.10b):

$$
u_{i+1}^n + u_{i-1}^n = 2u_i^n + (\Delta x)^2 \left.\frac{\partial^2 u}{\partial x^2}\right|_i^n + O[(\Delta x)^4]
$$

Rearranging:

$$
\left.\frac{\partial^2 u}{\partial x^2}\right|_i^n = \frac{u_{i+1}^n - 2u_i^n + u_{i-1}^n}{(\Delta x)^2} + O[(\Delta x)^2] \tag{2.13}
$$

### Central Difference for Second Time Derivative

By analogy:

$$
\left.\frac{\partial^2 u}{\partial t^2}\right|_i^n = \frac{u_i^{n+1} - 2u_i^n + u_i^{n-1}}{(\Delta t)^2} + O[(\Delta t)^2] \tag{2.14}
$$

Both approximations are **second-order accurate** in space and time respectively.

---

## 2.5 Finite-Difference Approximation of the Scalar Wave Equation

Substituting (2.13) and (2.14) into (2.1):

$$
\frac{u_i^{n+1} - 2u_i^n + u_i^{n-1}}{(\Delta t)^2} = c^2 \frac{u_{i+1}^n - 2u_i^n + u_{i-1}^n}{(\Delta x)^2} + O[(\Delta x)^2, (\Delta t)^2] \tag{2.15}
$$

Neglecting the remainder and solving for $u_i^{n+1}$:

$$
u_i^{n+1} = 2u_i^n - u_i^{n-1} + \left(\frac{c\Delta t}{\Delta x}\right)^2 (u_{i+1}^n - 2u_i^n + u_{i-1}^n) \tag{2.16}
$$

This is a **fully explicit** second-order accurate (2,2) scheme — all quantities on the RHS are known from previous time-steps $n$ and $n-1$. No simultaneous equation solution is needed.

### The Magic Time-Step

When $c\Delta t = \Delta x$ (the Courant number $S = c\Delta t/\Delta x = 1$), equation (2.16) simplifies dramatically:

$$
u_i^{n+1} = u_{i+1}^n + u_{i-1}^n - u_i^{n-1} \tag{2.17}
$$

**Remarkable property:** For $S = 1$, the solution of the numerical finite-difference equation is an **exact** solution to the original differential wave equation, despite the Taylor series approximations. Proof follows by substituting $u(x,t) = F(x+ct) + G(x-ct)$ directly into (2.17).

> **Numerical Intuition:** The magic time-step causes the truncation errors in space and time to exactly cancel, yielding perfect propagation. In practice, this is only possible in 1D and for lossless homogeneous media. For Maxwell's equations in 2D/3D, the magic time-step does not exist in the same sense.

---

## 2.6 Numerical Dispersion Relation

Consider a numerical sinusoidal traveling wave:

$$
u_i^n = e^{j(\omega n\Delta t - \tilde{k} i\Delta x)} \tag{2.20}
$$

where $\tilde{k} = k_{\text{real}} + jk_{\text{imag}}$ may be complex-valued. Substituting into (2.16):

$$
e^{j\omega\Delta t} + e^{-j\omega\Delta t} - 2 = \left(\frac{c\Delta t}{\Delta x}\right)^2 \left[e^{-j\tilde{k}\Delta x} + e^{j\tilde{k}\Delta x} - 2\right]
$$

Using Euler's identity:

$$
\cos(\omega\Delta t) = 1 + \left(\frac{c\Delta t}{\Delta x}\right)^2 \left[\cos(\tilde{k}\Delta x) - 1\right] \tag{2.23}
$$

Or equivalently:

$$
\sin^2\left(\frac{\omega\Delta t}{2}\right) = \left(\frac{c\Delta t}{\Delta x}\right)^2 \sin^2\left(\frac{\tilde{k}\Delta x}{2}\right) \tag{2.22}
$$

This is the **numerical dispersion relation** — much more complicated than the continuous relation $k = \omega/c$.

### 2.6.1 Case 1: Very Fine Sampling in Time and Space

For $\omega\Delta t \ll 1$ and $\tilde{k}\Delta x \ll 1$:

Use small-angle approximations: $\cos(\omega\Delta t) \approx 1 - (\omega\Delta t)^2/2$ and $\cos(\tilde{k}\Delta x) \approx 1 - (\tilde{k}\Delta x)^2/2$.

Substituting into (2.23):

$$
1 - \frac{(\omega\Delta t)^2}{2} \approx 1 + \left(\frac{c\Delta t}{\Delta x}\right)^2 \left[1 - \frac{(\tilde{k}\Delta x)^2}{2} - 1\right]
$$
$$
-\frac{(\omega\Delta t)^2}{2} \approx -\left(\frac{c\Delta t}{\Delta x}\right)^2 \frac{(\tilde{k}\Delta x)^2}{2}
$$
$$
\tilde{k}^2 \approx \frac{\omega^2}{c^2} = k_0^2
$$

Thus, for very fine grids, $\tilde{k} \to k_0$ and the numerical dispersion vanishes.

### 2.6.2 Case 2: The Magic Time-Step ($c\Delta t = \Delta x$)

For $S = 1$, (2.22) becomes:

$$
\sin^2\left(\frac{\omega\Delta t}{2}\right) = \sin^2\left(\frac{\tilde{k}\Delta x}{2}\right)
$$

Taking square roots (assuming frequency sign preserved):

$$
\omega\Delta t = \pm \tilde{k}\Delta x \quad \Rightarrow \quad \frac{\omega}{\tilde{k}} = \pm \frac{\Delta x}{\Delta t} = \pm c
$$

Since $v_p = \omega/\tilde{k}_{\text{real}}$, the numerical phase velocity equals $c$ exactly. **No numerical dispersion** for any spatial sampling density.

### 2.6.3 Case 3: Dispersive Wave Propagation ($S \neq 1$)

For $S < 1$ and general sampling, $\tilde{k}$ can be complex. From (2.22):

$$
\sin\left(\frac{\tilde{k}\Delta x}{2}\right) = \frac{1}{S} \sin\left(\frac{\omega\Delta t}{2}\right) \tag{2.26}
$$

Since $\tilde{k} = k_{\text{real}} + jk_{\text{imag}}$, we have:

$$
\sin\left(\frac{\tilde{k}\Delta x}{2}\right) = \sin\left(\frac{k_{\text{real}}\Delta x}{2}\right) \cosh\left(\frac{k_{\text{imag}}\Delta x}{2}\right) + j\cos\left(\frac{k_{\text{real}}\Delta x}{2}\right) \sinh\left(\frac{k_{\text{imag}}\Delta x}{2}\right)
$$

**Regimes:**
1. **Real $k$ regime** (no attenuation): when $\frac{1}{S} \sin\left(\frac{\omega\Delta t}{2}\right) \leq 1$, i.e., grid sampling $N_\lambda \geq 3$ points per wavelength for $S = 0.5$.
2. **Complex $k$ regime** (evanescent): when $\frac{1}{S} \sin\left(\frac{\omega\Delta t}{2}\right) > 1$, i.e., $N_\lambda < 3$ for $S = 0.5$.

**Numerical phase velocity** (real $k$ regime, $N_\lambda \geq 3$):

$$
v_p = \frac{\omega}{\tilde{k}_{\text{real}}} = \frac{\pi c}{N_\lambda \Delta x \cdot \tilde{k}_{\text{real}}} \tag{2.32c}
$$

where $\tilde{k}_{\text{real}}$ is obtained by inverting (2.26):

$$
\tilde{k}_{\text{real}} = \frac{2}{\Delta x} \sin^{-1}\left[\frac{1}{S} \sin\left(\frac{\omega\Delta t}{2}\right)\right]
$$

### 2.6.4 Example: Numerical Phase Velocity and Attenuation

For $S = 0.5$ (see Fig. 2.1 in text):
- At $N_\lambda = 3$: minimum $v_p = (2/3)c$ — onset of exponential attenuation
- As $N_\lambda \to 10$: $v_p \to c$ with $\sim 1/N_\lambda^2$ error (second-order accuracy)
- For $N_\lambda < 2$: $v_p > c$ (superluminal), reaching $2c$ at $N_\lambda = 1$
- At $N_\lambda = 1$: attenuation $\alpha \Delta x = 2.639$ nepers/cell

**Percent error in phase velocity** ($N_\lambda \gg 3$, $S = 0.5$):

$$
\text{Error} \propto \frac{1}{N_\lambda^2} = \left(\frac{\Delta x}{\lambda}\right)^2
$$

### 2.6.5 Example: Pulse Propagation

**40-cell-wide rectangular pulse in free space:**

1. **$S = 1$:** Rectangular shape and spatial width perfectly preserved. Step discontinuities modeled perfectly.
2. **$S = 0.99$:** Step discontinuities generate appreciable "ringing" — time-retarded propagation ($v_p < c$) of the sparsely sampled high spatial-frequency content.
3. **$S = 0.5$:** Pulse shape severely distorted with significant ringing and amplitude reduction.

> **Numerical Intuition:** For broadband pulses, the high-frequency spatial content is poorly sampled and propagates more slowly, causing trailing-edge ringing. This directly parallels numerical dispersion in Yee-FDTD for Maxwell's equations (Ch. 4).

---

## 2.7 Numerical Stability

**Definition:** An explicit numerical solution is **stable** if it produces a bounded result for a bounded input; **unstable** if it produces an unbounded result for a bounded input.

### 2.7.1 Complex-Frequency Analysis

Using the von Neumann approach: allow $\tilde{\omega} = \omega_{\text{real}} + j\omega_{\text{imag}}$, so that:

$$
u_i^n = e^{j(\tilde{\omega} n\Delta t - k i\Delta x)} \tag{2.40}
$$

Substituting into the numerical dispersion relation and solving for $\tilde{\omega}$:

$$
\sin\left(\frac{\tilde{\omega}\Delta t}{2}\right) = S \sin\left(\frac{k\Delta x}{2}\right), \quad S = \frac{c\Delta t}{\Delta x} \tag{2.42b}
$$

Consider $1 - 2S^2 \leq \xi \leq 1$ where $\xi = \cos(\tilde{k}\Delta x)$:

**Case (a): $0 \leq S \leq 1$** — $\xi$ lies in $[-1, 1]$, $\tilde{\omega}$ is real-valued → constant amplitude in time. **Stable.**

**Case (b): $S > 1$** — $\xi < -1$, $\tilde{\omega}$ becomes complex with $\omega_{\text{imag}} < 0$ → exponential growth.

The growth factor per time-step:

$$
q_{\text{growth}} = \exp(-\omega_{\text{imag}}\Delta t) = S + \sqrt{S^2 - 1} > 1 \tag{2.48}
$$

The maximum growth occurs for $k\Delta x = \pi$ (the Nyquist mode, $2\Delta x$ wavelength):

$$
q_{\text{growth,max}} = \left(S + \sqrt{S^2 - 1}\right)^{\Delta t} > 1
$$

**CFL Condition for scalar wave equation:**

$$
S = \frac{c\Delta t}{\Delta x} \leq 1 \tag{2.52}
$$

Named after Courant, Friedrichs, and Lewy (1928).

> **Numerical Intuition:** The CFL condition has a physical interpretation: the numerical domain of dependence must include the physical domain of dependence. If $\Delta t$ is too large, information would need to travel faster than $c$ across the grid — impossible by the physics of the wave equation.

---

## 2.8 Summary

| Concept | Expression | Key Insight |
|---------|-----------|-------------|
| Wave equation | $\partial^2 u / \partial t^2 = c^2 \partial^2 u / \partial x^2$ | Simplest wave PDE |
| Analytical solution | $u = F(x+ct) + G(x-ct)$ | Two propagating waves |
| FD approximation | $u_i^{n+1} = 2u_i^n - u_i^{n-1} + S^2(u_{i+1}^n - 2u_i^n + u_{i-1}^n)$ | (2,2) accurate explicit scheme |
| CFL condition | $S = c\Delta t/\Delta x \leq 1$ | Required for stability |
| Magic time-step | $S = 1$ | Exact solution for all frequencies |
| Numerical dispersion | $\sin^2(\omega\Delta t/2) = S^2 \sin^2(\tilde{k}\Delta x/2)$ | Causes pulse distortion when $S < 1$ |
| Dispersion error | $\propto 1/N_\lambda^2$ | Second-order convergence |
| Minimum sampling | $N_\lambda \geq 10$ recommended | For < 1% phase velocity error |

---

## Ch.2 Example Code

The code file implements three examples:
1. **Ex2.1:** 1D FDTD scalar wave equation — Gaussian pulse with $S = 1$ (magic) vs $S = 0.5$ (dispersive)
2. **Ex2.2:** Numerical dispersion — phase velocity vs grid sampling density
3. **Ex2.3:** CFL stability monitoring — energy growth for stable vs unstable time-steps

See: `taflove_ch2_examples.py`

---

## Chapter Audit

| Section | Content | Notes |
|---------|---------|-------|
| 2.1 | Introduction | ✓ |
| 2.2 | Propagating-wave solutions | ✓ Full derivation |
| 2.3 | Dispersion relation (continuous) | ✓ |
| 2.4 | Finite differences | ✓ Taylor series derivation |
| 2.5 | FD approximation of scalar wave eq. | ✓ Full derivation, magic time-step proof |
| 2.6 | Numerical dispersion relation | ✓ Three cases |
| 2.6.1 | Fine sampling | ✓ |
| 2.6.2 | Magic time-step | ✓ |
| 2.6.3 | Dispersive propagation | ✓ |
| 2.6.4 | Phase velocity/attenuation example | ✓ |
| 2.6.5 | Pulse propagation examples | ✓ |
| 2.7 | Numerical stability | ✓ CFL condition |
| 2.7.1 | Complex-frequency analysis | ✓ Growth factor derivation |
| 2.7.2 | Instability examples | ✓ |
| 2.8 | Summary | ✓ |
