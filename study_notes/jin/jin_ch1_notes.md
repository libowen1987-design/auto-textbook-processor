---
title: "Chapter 1 — Basic Electromagnetic Theory"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Vector analysis (div, curl, gradient, symbolic vector method)
  - Helmholtz decomposition & Green's theorems
  - Maxwell's equations (integral & differential)
  - Constitutive relations & classification of media
  - Boundary conditions at interfaces & PEC/PMC
  - Poynting's theorem & energy conservation
  - Time-harmonic fields & complex power
---

# Chapter 1: Basic Electromagnetic Theory

## 1.1 Review of Vector Analysis

### 1.1.1 Vector Operations and Integral Theorems

**Divergence** — the net outward flux per unit volume:

$$
\nabla \cdot \mathbf{f} = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \oint_s \mathbf{f} \cdot d\mathbf{s}
\tag{1.1.1}
$$

In rectangular coordinates:

$$
\nabla \cdot \mathbf{f} = \frac{\partial f_x}{\partial x} + \frac{\partial f_y}{\partial y} + \frac{\partial f_z}{\partial z}
\tag{1.1.2}
$$

In cylindrical coordinates:

$$
\nabla \cdot \mathbf{f} = \frac{1}{\rho} \frac{\partial (\rho f_\rho)}{\partial \rho} + \frac{1}{\rho} \frac{\partial f_\phi}{\partial \phi} + \frac{\partial f_z}{\partial z}
\tag{1.1.3}
$$

In spherical coordinates:

$$
\nabla \cdot \mathbf{f} = \frac{1}{r^2} \frac{\partial}{\partial r} (r^2 f_r) + \frac{1}{r\sin\theta} \frac{\partial}{\partial \theta} (f_\theta \sin\theta) + \frac{1}{r\sin\theta} \frac{\partial f_\phi}{\partial \phi}
\tag{1.1.4}
$$

**Divergence Theorem (Gauss' Theorem):**

$$
\iiint_V \nabla \cdot \mathbf{f} \, dV = \oiint_S \mathbf{f} \cdot d\mathbf{S}
\tag{1.1.5}
$$

**Curl** — the circulation per unit area:

$$
\nabla \times \mathbf{f} = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \oint_s d\mathbf{s} \times \mathbf{f}
\tag{1.1.6}
$$

Rectangular form:

$$
\nabla \times \mathbf{f} = \hat{x} \left( \frac{\partial f_z}{\partial y} - \frac{\partial f_y}{\partial z} \right)
+ \hat{y} \left( \frac{\partial f_x}{\partial z} - \frac{\partial f_z}{\partial x} \right)
+ \hat{z} \left( \frac{\partial f_y}{\partial x} - \frac{\partial f_x}{\partial y} \right)
\tag{1.1.7}
$$

**Stokes' Theorem:**

$$
\iint_S (\nabla \times \mathbf{f}) \cdot d\mathbf{S} = \oint_C \mathbf{f} \cdot d\mathbf{l}
\tag{1.1.11}
$$

**Gradient** of a scalar function:

$$
\nabla f = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \oint_s f \, d\mathbf{s}
\tag{1.1.12}
$$

**Laplacian:**

$$
\nabla^2 f = \nabla \cdot (\nabla f)
\tag{1.1.17}
$$

### 1.1.2 Symbolic Vector Method

The symbolic vector $\tilde{\nabla}$ is defined such that:

$$
T(\tilde{\nabla}) = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \oint_s T(\hat{n}) \, ds
\tag{1.1.21}
$$

Key relations:

| Operation | Relationship |
|-----------|-------------|
| Divergence | $\nabla \cdot \mathbf{f} = \tilde{\nabla} \cdot \mathbf{f} = \mathbf{f} \cdot \tilde{\nabla}$ |
| Curl | $\nabla \times \mathbf{f} = \tilde{\nabla} \times \mathbf{f} = -\mathbf{f} \times \tilde{\nabla}$ |
| Gradient | $\nabla f = \tilde{\nabla} f = f \tilde{\nabla}$ |

Given two functions $a$ and $b$, the chain rule applies:

$$
T(\tilde{\nabla}, a, b) = T(\tilde{\nabla}_a, a, b) + T(\tilde{\nabla}_b, a, b)
\tag{1.1.28}
$$

**Generalized Gauss' Theorem:**

$$
\iiint_V T(\tilde{\nabla}) \, dV = \oiint_S T(\hat{n}) \, dS
\tag{1.1.37}
$$

**Useful vector identities derived via symbolic method:**

$$
\nabla \times (\nabla \times \mathbf{f}) = \nabla(\nabla \cdot \mathbf{f}) - \nabla^2 \mathbf{f}
\tag{1.1.27}
$$

$$
\nabla \cdot (a\mathbf{b}) = \mathbf{b} \cdot (\nabla a) + a \nabla \cdot \mathbf{b}
\tag{1.1.31}
$$

$$
\nabla \times (a\mathbf{b}) = -\mathbf{b} \times \nabla a + a \nabla \times \mathbf{b}
\tag{1.1.33}
$$

$$
\nabla \times (\mathbf{a} \times \mathbf{b}) = (\mathbf{b} \cdot \nabla)\mathbf{a} - \mathbf{b} \nabla \cdot \mathbf{a} + \mathbf{a} \nabla \cdot \mathbf{b} - (\mathbf{a} \cdot \nabla)\mathbf{b}
\tag{1.1.36}
$$

**Example 1.1** — Derive $\iiint_V (\mathbf{b} \nabla \cdot \mathbf{a} + \mathbf{a} \cdot \nabla \mathbf{b}) dV = \oiint_S (\hat{n} \cdot \mathbf{a})\mathbf{b} \, dS$ using the generalized Gauss' theorem.

### 1.1.3 Helmholtz Decomposition Theorem

Any smooth vector function $\mathbf{F}$ vanishing at infinity can be decomposed into **irrotational** and **solenoidal** parts:

$$
\mathbf{F} = \mathbf{F}_i + \mathbf{F}_s
\tag{1.1.43}
$$

where:

$$
\nabla \times \mathbf{F}_i = 0, \quad \nabla \cdot \mathbf{F}_i \ne 0
\qquad
\nabla \cdot \mathbf{F}_s = 0, \quad \nabla \times \mathbf{F}_s \ne 0
$$

**Key insight:** Once both $\nabla \cdot \mathbf{F}$ and $\nabla \times \mathbf{F}$ are specified, $\mathbf{F}$ is fully determined.

**Vector identities:**

$$
\nabla \times (\nabla \varphi) = 0 \quad \text{(gradient of scalar is irrotational)}
\tag{1.1.41}
$$

$$
\nabla \cdot (\nabla \times \mathbf{A}) = 0 \quad \text{(curl of vector is solenoidal)}
\tag{1.1.42}
$$

### 1.1.4 Green's Theorems

**First scalar Green's theorem** (set $\mathbf{f} = a \nabla b$ in divergence theorem):

$$
\iiint_V (a \nabla^2 b + \nabla a \cdot \nabla b) \, dV = \oiint_S a \frac{\partial b}{\partial n} \, dS
\tag{1.1.45}
$$

**Second scalar Green's theorem:**

$$
\iiint_V (a \nabla^2 b - b \nabla^2 a) \, dV = \oiint_S \left( a \frac{\partial b}{\partial n} - b \frac{\partial a}{\partial n} \right) dS
\tag{1.1.46}
$$

**First vector Green's theorem** (set $\mathbf{f} = \mathbf{a} \times \nabla \times \mathbf{b}$):

$$
\iiint_V [(\nabla \times \mathbf{a}) \cdot (\nabla \times \mathbf{b}) - \mathbf{a} \cdot (\nabla \times \nabla \times \mathbf{b})] dV
= \oiint_S (\mathbf{a} \times \nabla \times \mathbf{b}) \cdot d\mathbf{S}
\tag{1.1.47}
$$

**Second vector Green's theorem:**

$$
\iiint_V [\mathbf{b} \cdot (\nabla \times \nabla \times \mathbf{a}) - \mathbf{a} \cdot (\nabla \times \nabla \times \mathbf{b})] dV
= \oiint_S (\mathbf{a} \times \nabla \times \mathbf{b} - \mathbf{b} \times \nabla \times \mathbf{a}) \cdot d\mathbf{S}
\tag{1.1.48}
$$

**Scalar-vector Green's theorem** (set $\mathbf{b} = \hat{b} b$ in the above):

$$
\iiint_V [b (\nabla \times \nabla \times \mathbf{a}) + \mathbf{a} \nabla^2 b + (\nabla \cdot \mathbf{a}) \nabla b] dV
= \oiint_S [(\hat{n} \cdot \mathbf{a}) \nabla b + (\hat{n} \times \mathbf{a}) \times \nabla b + (\hat{n} \times \nabla \times \mathbf{a}) b] dS
\tag{1.1.49}
$$

---

## 1.2 Maxwell's Equations in Terms of Total Charges and Currents

### 1.2.1 Integral Form

| Law | Equation |
|-----|----------|
| **Faraday's induction law** | $\displaystyle \oint_C \mathbf{E}(\mathbf{r}, t) \cdot d\mathbf{l} = -\frac{d}{dt} \iint_S \mathbf{B}(\mathbf{r}, t) \cdot d\mathbf{S}$ |
| **Maxwell–Ampère law** | $\displaystyle \oint_C \mathbf{B}(\mathbf{r}, t) \cdot d\mathbf{l} = \epsilon_0 \mu_0 \frac{d}{dt} \iint_S \mathbf{E}(\mathbf{r}, t) \cdot d\mathbf{S} + \mu_0 \iint_S \mathbf{J}_{\text{total}}(\mathbf{r}, t) \cdot d\mathbf{S}$ |
| **Gauss' law** | $\displaystyle \oiint_S \mathbf{E}(\mathbf{r}, t) \cdot d\mathbf{S} = \frac{1}{\epsilon_0} \iiint_V \varrho_{e,\text{total}}(\mathbf{r}, t) \, dV$ |
| **Gauss' law (magnetic)** | $\displaystyle \oiint_S \mathbf{B}(\mathbf{r}, t) \cdot d\mathbf{S} = 0$ |

**Free-space constants:**

$$
\epsilon_0 = 8.854 \times 10^{-12} \ \text{F/m} \approx \frac{1}{36\pi} \times 10^{-9} \ \text{F/m}
\qquad
\mu_0 = 4\pi \times 10^{-7} \ \text{H/m}
$$

**Example 1.3** — From Faraday's law, derive Kirchhoff's voltage law for an RLC circuit with source $V_s$.

### 1.2.2 Differential Form

Using Stokes' and Gauss' theorems (valid in a continuous medium):

| Law | Equation |
|-----|----------|
| **Faraday** | $\displaystyle \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$ |
| **Maxwell–Ampère** | $\displaystyle \nabla \times \mathbf{B} = \epsilon_0 \mu_0 \frac{\partial \mathbf{E}}{\partial t} + \mu_0 \mathbf{J}_{\text{total}}$ |
| **Gauss** | $\displaystyle \nabla \cdot \mathbf{E} = \frac{\varrho_{e,\text{total}}}{\epsilon_0}$ |
| **Gauss (magnetic)** | $\displaystyle \nabla \cdot \mathbf{B} = 0$ |

### 1.2.3 Current Continuity Equation

From taking the divergence of the Maxwell–Ampère law:

$$
\nabla \cdot \mathbf{J}_{\text{total}} = -\frac{\partial \varrho_{e,\text{total}}}{\partial t}
\tag{1.2.16}
$$

Which yields the conservation of charge in integral form:

$$
\oiint_S \mathbf{J}_{\text{total}} \cdot d\mathbf{S} = -\frac{d}{dt} \iiint_V \varrho_{e,\text{total}} \, dV
\tag{1.2.17}
$$

**Example 1.4** — From the continuity equation, derive Kirchhoff's current law $\sum_{i=1}^N I_i = 0$ at a node.

### 1.2.4 The Lorentz Force Law

$$
\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})
\tag{1.2.18}
$$

---

## 1.3 Constitutive Relations

### 1.3.1 Electric Polarization

Electric dipole moment: $\mathbf{p} = q \boldsymbol{\ell}$.

Polarization vector: $\mathbf{P} = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \sum_{i=1}^{n_p} \mathbf{p}_i$.

**Bound charge density:** $\varrho_{e,b} = -\nabla \cdot \mathbf{P}$.

Electric flux density: $\mathbf{D} = \epsilon_0 \mathbf{E} + \mathbf{P}$.

**Linear dielectric:** $\mathbf{D} = \epsilon \mathbf{E}$, where $\epsilon = \epsilon_0 (1 + \chi_e)$.

### 1.3.2 Magnetization

Magnetic dipole moment: $\mathbf{m} = I \mathbf{s}$.

Magnetization vector: $\mathbf{M} = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \sum_{i=1}^{n_m} \mathbf{m}_i$.

**Bound current density:** $\mathbf{J}_m = \nabla \times \mathbf{M}$.

Magnetic field intensity: $\mathbf{H} = \frac{\mathbf{B}}{\mu_0} - \mathbf{M}$.

**Linear magnetic material:** $\mathbf{B} = \mu \mathbf{H}$, where $\mu = \mu_0 (1 + \chi_m)$.

### 1.3.3 Electric Conduction

**Ohm's law:** $\mathbf{J}_c = \sigma \mathbf{E}$.

### 1.3.4 Classification of Media

| Criterion | Types |
|-----------|-------|
| Spatial | homogeneous / inhomogeneous |
| Temporal | stationary / nonstationary |
| Directional | isotropic / anisotropic / bi-anisotropic |
| Linearity | linear / nonlinear |
| Frequency | dispersive / nondispersive |
| Conductivity | dielectric ($\sigma=0$) / lossy ($0<\sigma<\infty$) / PEC ($\sigma\to\infty$) |
| Permeability | diamagnetic ($\mu_r \lesssim 1$), paramagnetic ($\mu_r \gtrsim 1$), ferromagnetic ($\mu_r \gg 1$) |

---

## 1.4 Maxwell's Equations in Terms of Free Charges and Currents

**Differential form:**

| Law | Equation |
|-----|----------|
| **Faraday** | $\displaystyle \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} - \mathbf{M}_f$ |
| **Maxwell–Ampère** | $\displaystyle \nabla \times \mathbf{H} = \frac{\partial \mathbf{D}}{\partial t} + \mathbf{J}_f$ |
| **Gauss** | $\displaystyle \nabla \cdot \mathbf{D} = \varrho_{e,f}$ |
| **Gauss (magnetic)** | $\displaystyle \nabla \cdot \mathbf{B} = \varrho_{m,f}$ |

---

## 1.5 Boundary Conditions

### General Interface

From the integral form with a rectangular frame and pillbox:

| Condition | Equation |
|-----------|----------|
| Tangential $\mathbf{H}$ | $\hat{n} \times (\mathbf{H}_2 - \mathbf{H}_1) = \mathbf{J}_s$ |
| Tangential $\mathbf{E}$ | $\hat{n} \times (\mathbf{E}_2 - \mathbf{E}_1) = -\mathbf{M}_s$ |
| Normal $\mathbf{D}$ | $\hat{n} \cdot (\mathbf{D}_2 - \mathbf{D}_1) = \varrho_{e,s}$ |
| Normal $\mathbf{B}$ | $\hat{n} \cdot (\mathbf{B}_2 - \mathbf{B}_1) = \varrho_{m,s}$ |

### Perfect Electric Conductor (PEC)

$$
\hat{n} \times \mathbf{E} = 0, \quad
\hat{n} \times \mathbf{H} = \mathbf{J}_s, \quad
\hat{n} \cdot \mathbf{D} = \varrho_{e,s}, \quad
\hat{n} \cdot \mathbf{B} = 0
$$

**Physical intuition:** In a PEC, free charges move to cancel internal fields instantly, producing surface currents and charges. The tangential $\mathbf{E}$ must vanish on a PEC surface; otherwise infinite current would flow.

**Example 1.5** — Relates total-charge boundary conditions to free-charge boundary conditions and identifies that magnetization produces a surface current $\mathbf{J}_{m,s} = -\hat{n} \times \mathbf{M}$ and polarization produces a bound surface charge $\varrho_{e,b,s} = \hat{n} \cdot \mathbf{P}$.

---

## 1.6 Energy, Power, and Poynting's Theorem

**Poynting vector** (instantaneous power flux density):

$$
\mathbf{S}(\mathbf{r}, t) = \mathbf{E}(\mathbf{r}, t) \times \mathbf{H}(\mathbf{r}, t)
\tag{1.6.17}
$$

**Poynting's theorem (integral form)** — conservation of electromagnetic energy:

$$
P_s = P_e + P_d + \frac{d}{dt} (W_e + W_m)
\tag{1.6.14}
$$

where:

| Quantity | Expression | Meaning |
|----------|------------|---------|
| $P_s$ | $-\iiint_V (\mathbf{E} \cdot \mathbf{J}_i + \mathbf{H} \cdot \mathbf{M}_i) dV$ | Supplied power |
| $P_e$ | $\oiint_S (\mathbf{E} \times \mathbf{H}) \cdot \hat{n} \, dS$ | Exiting power |
| $P_d$ | $\iiint_V \sigma |\mathbf{E}|^2 dV$ | Dissipated power |
| $W_e$ | $\frac{1}{2} \iiint_V \epsilon |\mathbf{E}|^2 dV$ | Electric stored energy |
| $W_m$ | $\frac{1}{2} \iiint_V \mu |\mathbf{H}|^2 dV$ | Magnetic stored energy |

---

## 1.7 Time-Harmonic Fields

### 1.7.1 Phasor Representation

For a time-harmonic field at angular frequency $\omega$:

$$
\mathbf{E}(\mathbf{r}, t) = \text{Re}\left[\mathbf{E}(\mathbf{r}) e^{j\omega t}\right]
$$

The time derivative $\partial/\partial t \mapsto j\omega$:

$$
\nabla \times \mathbf{E} = -j\omega \mathbf{B} - \mathbf{M}_f, \quad
\nabla \times \mathbf{H} = j\omega \mathbf{D} + \mathbf{J}_f
$$

### 1.7.2 Fourier Transforms

For arbitrary time dependence, the Fourier transform yields the same frequency-domain equations. Causality is preserved because future values integrate to zero in the inverse transform.

### 1.7.3 Complex Power

**Time-average Poynting vector:**

$$
\langle \mathbf{S}(\mathbf{r}, t) \rangle = \frac{1}{2} \text{Re}[\mathbf{E} \times \mathbf{H}^*]
\tag{1.7.23}
$$

**Complex Poynting theorem:**

$$
P_s = P_e + P_d + j 2\omega (W_m - W_e)
\tag{1.7.40}
$$

where $P_e = \frac{1}{2} \oiint_S (\mathbf{E} \times \mathbf{H}^*) \cdot d\mathbf{S}$, $P_d = \frac{1}{2} \iiint_V \sigma |\mathbf{E}|^2 dV$, $W_e = \frac{1}{4} \iiint_V \epsilon |\mathbf{E}|^2 dV$, $W_m = \frac{1}{4} \iiint_V \mu |\mathbf{H}|^2 dV$.

**Physical interpretation:** The real part gives time-average power balance; the imaginary part relates to the difference between time-average magnetic and electric energies (reactive power).

### 1.7.4 Complex Permittivity and Permeability

$$
\epsilon_r = \epsilon_r' - j \epsilon_r'', \quad
\mu_r = \mu_r' - j \mu_r''
$$

**Loss tangent:**

$$
\tan\delta_e = \frac{\epsilon_r''}{\epsilon_r'}, \quad
\tan\delta_m = \frac{\mu_r''}{\mu_r'}
$$

**Kramers–Krönig relations** — causality requires that dispersion implies loss:

$$
\epsilon'(\omega) = \epsilon_\infty + \frac{2}{\pi} \,\text{P}\!\!\int_0^\infty \frac{z \epsilon''(z)}{z^2 - \omega^2} dz
$$

$$
\epsilon''(\omega) = -\frac{2\omega}{\pi} \,\text{P}\!\!\int_0^\infty \frac{\epsilon'(z) - \epsilon_\infty}{z^2 - \omega^2} dz
$$

---

## Key Physical Intuition

1. **Symbolic vector method** elegantly derives vector identities by treating $\nabla$ as a regular vector, avoiding component-level derivations.
2. **Helmholtz decomposition** is the mathematical foundation for using vector and scalar potentials: any field is determined by its divergence and curl.
3. **Poynting's theorem** is the energy conservation law for EM fields — the cornerstone for understanding power flow, dissipation, and reactive power.
4. **Complex phasor form** reduces 4D (space + time) problems to 3D, and the imaginary part of Poynting's theorem reveals the reactive power associated with the difference between electric and magnetic stored energy.
5. **Kramers–Krönig** forces the connection between dispersion and loss — a causal material cannot have one without the other.

---

## Original Examples in This Chapter

| Example | Topic | Section |
|---------|-------|---------|
| 1.1 | Deriving integral theorems via generalized Gauss' theorem | 1.1.2 |
| 1.2 | Deriving scalar-vector Green's theorem | 1.1.4 |
| 1.3 | Faraday's law → KVL | 1.2.1 |
| 1.4 | Continuity equation → KCL | 1.2.3 |
| 1.5 | Boundary conditions with total vs. free charges/currents | 1.5 |
| 1.6 | Lorentz model of dielectric (frequency-dependent $\epsilon_r$) | 1.7.2 |
| 1.7 | Complex power through a slot in a metallic box | 1.7.3 |
| 1.8 | Drude model of plasma permittivity | 1.7.4 |
| 1.9 | Kramers–Krönig relations for dispersive media | 1.7.4 |

---

## Audit

| Section | Content Coverage | Notes Alignment |
|---------|-----------------|-----------------|
| 1.1 | Vector analysis, identities, theorems | Full coverage |
| 1.2 | Maxwell's equations (total charges) | Full coverage |
| 1.3 | Constitutive relations | Full coverage |
| 1.4 | Maxwell's equations (free charges) | Full coverage |
| 1.5 | Boundary conditions | Full coverage |
| 1.6 | Poynting theorem | Full coverage |
| 1.7 | Time-harmonic fields, complex power | Full coverage |
| Examples | All 9 examples listed | Identified with original numbers |
