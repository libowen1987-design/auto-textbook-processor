---
chapter: 9
title: Electromagnetic Waves
source: Griffiths, Introduction to Electrodynamics, 4th Edition
pages: 382-454
---

# Chapter 9: Electromagnetic Waves

## 9.1 Waves in One Dimension (pp. 382-392)

### 9.1.1 The Wave Equation

$$\frac{\partial^2 f}{\partial z^2} = \frac{1}{v^2}\frac{\partial^2 f}{\partial t^2}$$

(9.2)

General solution: $f(z,t) = g(z-vt) + h(z+vt)$ — any function of $z\mp vt$ (traveling waves).

**Sinusoidal waves:** $f(z,t) = A\cos(kz - \omega t + \delta)$, where $k = \omega/v$, $\lambda = 2\pi/k$, $T = 2\pi/\omega$.

### 9.1.2 Polarization

Transverse waves can be polarized. For a string, $\hat{\mathbf{n}}$ = direction of displacement. Circular, elliptical, and linear polarization.

### 9.1.3 Reflection and Transmission

At a boundary between two strings of different densities, wave impedance mismatch causes partial reflection.

---

## 9.2 EM Waves in Vacuum (pp. 393-400)

### 9.2.1 Wave Equation for E and B

From Maxwell's equations in vacuum ($\rho=0, \mathbf{J}=0$):

$$\nabla^2\mathbf{E} = \mu_0\epsilon_0\frac{\partial^2\mathbf{E}}{\partial t^2}, \quad \nabla^2\mathbf{B} = \mu_0\epsilon_0\frac{\partial^2\mathbf{B}}{\partial t^2}$$

(9.41)

The wave speed is:

$$c = \frac{1}{\sqrt{\mu_0\epsilon_0}} = 3.00\times 10^8\ \text{m/s}$$

(9.42)

### 9.2.2 Monochromatic Plane Waves

For a plane wave traveling in the $z$ direction, linearly polarized along $x$:

$$\tilde{\mathbf{E}}(z,t) = \tilde{E}_0 e^{i(kz-\omega t)}\hat{\mathbf{x}}$$

$$\tilde{\mathbf{B}}(z,t) = \frac{1}{c}\tilde{E}_0 e^{i(kz-\omega t)}\hat{\mathbf{y}}$$

(9.47-9.49)

**Properties:**
- Transverse: $\mathbf{E} \perp \hat{\mathbf{z}}$, $\mathbf{B} \perp \hat{\mathbf{z}}$
- $\mathbf{E} \perp \mathbf{B}$ (mutually perpendicular)
- $\mathbf{E}$ and $\mathbf{B}$ are in phase
- $\mathbf{B} = \frac{1}{c}(\hat{\mathbf{k}}\times\mathbf{E})$

**Energy and momentum:**
- Energy density: $u = \frac{1}{2}(\epsilon_0 E^2 + B^2/\mu_0) = \epsilon_0 E_0^2\cos^2(kz-\omega t)$ (9.55)
- Poynting vector: $\mathbf{S} = c u \hat{\mathbf{z}}$ (9.57)
- **Intensity:** $I \equiv \langle S \rangle = \frac{1}{2}c\epsilon_0 E_0^2$ (9.63)
- Momentum density: $\mathbf{g} = \frac{1}{c^2}\mathbf{S} = \frac{u}{c}\hat{\mathbf{z}}$ (9.58-9.59)
- **Radiation pressure** (absorber): $P = I/c$ (9.64); (reflector): $P = 2I/c$

---

## 9.3 EM Waves in Matter (pp. 401-427)

### 9.3.1 Propagation in Linear Media

For linear homogeneous media:

$$v = \frac{1}{\sqrt{\epsilon\mu}} = \frac{c}{n}, \quad n \equiv \sqrt{\frac{\epsilon\mu}{\epsilon_0\mu_0}} \approx \sqrt{\epsilon_r}$$

(9.68-9.70)

Energy density: $u = \frac{1}{2}(\epsilon E^2 + B^2/\mu)$ (9.71)
Poynting vector: $\mathbf{S} = \frac{1}{\mu}(\mathbf{E}\times\mathbf{B})$ (9.72)
Intensity: $I = \frac{1}{2}\epsilon v E_0^2$ (9.73)

### 9.3.2 Reflection and Transmission at Normal Incidence

Boundary conditions for linear media (no free charge/current):

$$E_1^\parallel = E_2^\parallel, \quad \epsilon_1 E_1^\perp = \epsilon_2 E_2^\perp, \quad B_1^\perp = B_2^\perp, \quad \frac{1}{\mu_1}B_1^\parallel = \frac{1}{\mu_2}B_2^\parallel$$

(9.74)

**Fresnel equations (normal incidence):**

$$\tilde{E}_{0R} = \frac{1-\beta}{1+\beta}\tilde{E}_{0I}, \quad \tilde{E}_{0T} = \frac{2}{1+\beta}\tilde{E}_{0I}$$

(9.82)

where $\beta \equiv \mu_1 v_1 / \mu_2 v_2 = \mu_1 n_2 / \mu_2 n_1$.

For $\mu_1 \approx \mu_2 \approx \mu_0$:

$$E_{0R} = \left|\frac{n_1-n_2}{n_1+n_2}\right|E_{0I}, \quad E_{0T} = \frac{2n_1}{n_1+n_2}E_{0I}$$

(9.85)

**Reflection and transmission coefficients (intensity):**

$$R = \frac{I_R}{I_I} = \left(\frac{n_1-n_2}{n_1+n_2}\right)^2, \quad T = \frac{I_T}{I_I} = \frac{4n_1 n_2}{(n_1+n_2)^2}$$

(9.86-9.87)

### 9.3.3 Reflection and Transmission at Oblique Incidence

**Snell's law:** $n_1\sin\theta_I = n_2\sin\theta_T$ (9.101)

**Law of reflection:** $\theta_R = \theta_I$

**Fresnel equations (oblique incidence) for polarization perpendicular to plane of incidence (TE):**

$$E_{0R} = \frac{n_1\cos\theta_I - n_2\cos\theta_T}{n_1\cos\theta_I + n_2\cos\theta_T}E_{0I}$$

(9.109)

**For polarization parallel to plane of incidence (TM):**

$$E_{0R} = \frac{n_2\cos\theta_I - n_1\cos\theta_T}{n_2\cos\theta_I + n_1\cos\theta_T}E_{0I}$$

(9.110)

**Brewster's angle** — reflected wave vanishes for TM polarization when $\theta_I + \theta_T = 90^\circ$:

$$\tan\theta_B = \frac{n_2}{n_1}$$

(9.113)

**Total internal reflection** occurs when $n_1 > n_2$ and $\sin\theta_I \ge n_2/n_1$ (critical angle $\theta_c = \sin^{-1}(n_2/n_1)$).

---

## 9.4 Absorption and Dispersion (pp. 427-439)

### 9.4.1 Electromagnetic Waves in Conductors

In a conductor, $\mathbf{J} = \sigma\mathbf{E}$. The wave equation becomes:

$$\nabla^2\tilde{\mathbf{E}} = \mu\epsilon\frac{\partial^2\tilde{\mathbf{E}}}{\partial t^2} + \mu\sigma\frac{\partial\tilde{\mathbf{E}}}{\partial t}$$

(9.124)

For sinusoidal waves $\tilde{\mathbf{E}}(z,t) = \tilde{E}_0 e^{i(kz-\omega t)}$, the wave number is complex:

$$\tilde{k} = k + i\kappa, \quad k = \omega\sqrt{\frac{\epsilon\mu}{2}}\left[\sqrt{1+\left(\frac{\sigma}{\epsilon\omega}\right)^2}+1\right]^{1/2}, \quad \kappa = \omega\sqrt{\frac{\epsilon\mu}{2}}\left[\sqrt{1+\left(\frac{\sigma}{\epsilon\omega}\right)^2}-1\right]^{1/2}$$

(9.126)

**Skin depth:** $d = 1/\kappa$ — the distance over which the amplitude decreases by $1/e$.

**Good conductor limit** ($\sigma \gg \epsilon\omega$):

$$d = \sqrt{\frac{2}{\mu\sigma\omega}}$$

(9.128)

For copper at 60 Hz: $d \approx 8.5$ mm. For copper at 1 GHz: $d \approx 2.1\ \mu$m.

### 9.4.2 Frequency Dependence of Permittivity

In a dispersive medium, $\epsilon(\omega)$ is complex and frequency-dependent:

- At low frequencies: $\epsilon(\omega) \approx \epsilon(0)$ (static value)
- Near resonance: strong absorption, anomalous dispersion
- At high frequencies: $\epsilon(\omega) \to \epsilon_0$ (bound electrons can't keep up)

---

## 9.5 Guided Waves (pp. 439-454)

### 9.5.1 Waveguides

In a hollow rectangular waveguide (width $a$ in $x$, $b$ in $y$, propagating in $z$):

$$\tilde{\mathbf{E}}(x,y,z,t) = \tilde{\mathbf{E}}_0(x,y) e^{i(k_g z - \omega t)}$$

**TE$_{mn}$ modes** (transverse electric, $E_z = 0$):

$$k_g = \sqrt{\left(\frac{\omega}{c}\right)^2 - \left(\frac{m\pi}{a}\right)^2 - \left(\frac{n\pi}{b}\right)^2}$$

(9.187)

**Cutoff frequency:** $\omega_{mn} = c\sqrt{(m\pi/a)^2 + (n\pi/b)^2}$ — below this, the mode cannot propagate.

**Dominant mode** (lowest cutoff): TE$_{10}$ with $\omega_{10} = c\pi/a$.

**Group velocity:** $v_g = \frac{d\omega}{dk_g} = c\sqrt{1-(\omega_{mn}/\omega)^2}$ — always less than $c$.

### 9.5.2 Coaxial Transmission Line

For a coaxial cable (inner radius $a$, outer $b$), the dominant mode is TEM (transverse electromagnetic) with no cutoff: $v = c/\sqrt{\epsilon_r}$.

---

### Chapter Summary: EM Wave Properties

| Property | Vacuum | Linear medium |
|----------|--------|---------------|
| Wave speed | $c = 1/\sqrt{\mu_0\epsilon_0}$ | $v = 1/\sqrt{\mu\epsilon} = c/n$ |
| Wave impedance | $Z_0 = \sqrt{\mu_0/\epsilon_0}$ | $Z = \sqrt{\mu/\epsilon}$ |
| $B/E$ ratio | $B/E = 1/c$ | $B/E = 1/v$ |
| Intensity | $I = \frac{1}{2}c\epsilon_0 E_0^2$ | $I = \frac{1}{2}\epsilon v E_0^2$ |
| Radiation pressure | $P = I/c$ (absorber) | $P = I/v$ |

**物理直觉（全章回顾）：** Maxwell 方程组的一个重要推论是电磁波——变化的电场产生磁场、变化的磁场产生电场，两者相互扶持、在真空中以光速传播。电磁波是横波（$\mathbf{E}$、$\mathbf{B}$ 均垂直于传播方向），携带能量和动量。在介质中速度减慢，在导体中指数衰减（趋肤效应）。波导中只有高于截止频率的模式才能传播——这是微波工程的基础。
