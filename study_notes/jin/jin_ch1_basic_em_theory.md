# Chapter 1: Basic Electromagnetic Theory

**Source:** Jin, *Theory and Computation of Electromagnetic Fields*, 2nd Ed., Chapter 1 (pp. 27–76)

---

## 1.1 Review of Vector Analysis

### 1.1.1 Vector Operations and Integral Theorems

**Divergence:**

$$
\nabla \cdot \mathbf{f} = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \oint_{s} \mathbf{f} \cdot d\mathbf{s}
\tag{1.1.1}
$$

- Rectangular: $\nabla \cdot \mathbf{f} = \frac{\partial f_x}{\partial x} + \frac{\partial f_y}{\partial y} + \frac{\partial f_z}{\partial z}$ (1.1.2)
- Cylindrical: $\nabla \cdot \mathbf{f} = \frac{1}{\rho}\frac{\partial(\rho f_\rho)}{\partial \rho} + \frac{\partial f_\phi}{\rho \partial \phi} + \frac{\partial f_z}{\partial z}$ (1.1.3)
- Spherical: $\nabla \cdot \mathbf{f} = \frac{1}{r^2}\frac{\partial}{\partial r}(r^2 f_r) + \frac{1}{r\sin\theta}\frac{\partial}{\partial \theta}(f_\theta\sin\theta) + \frac{1}{r\sin\theta}\frac{\partial f_\phi}{\partial \phi}$ (1.1.4)

**Divergence Theorem (Gauss' Theorem):**

$$
\iiint_V \nabla \cdot \mathbf{f} \, dV = \oint_{S} \mathbf{f} \cdot d\mathbf{S}
\tag{1.1.5}
$$

**Curl:**

$$
\nabla \times \mathbf{f} = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \oint_{s} d\mathbf{s} \times \mathbf{f}
\tag{1.1.6}
$$

- Rectangular: $\nabla \times \mathbf{f} = \hat{x}\left(\frac{\partial f_z}{\partial y} - \frac{\partial f_y}{\partial z}\right) + \hat{y}\left(\frac{\partial f_x}{\partial z} - \frac{\partial f_z}{\partial x}\right) + \hat{z}\left(\frac{\partial f_y}{\partial x} - \frac{\partial f_x}{\partial y}\right)$ (1.1.7)
- Cylindrical: $\nabla \times \mathbf{f} = \hat{\rho}\left(\frac{\partial f_z}{\rho\partial\phi} - \frac{\partial f_\phi}{\partial z}\right) + \hat{\phi}\left(\frac{\partial f_\rho}{\partial z} - \frac{\partial f_z}{\partial \rho}\right) + \hat{z}\frac{1}{\rho}\left[\frac{\partial (\rho f_\phi)}{\partial \rho} - \frac{\partial f_\rho}{\partial \phi}\right]$ (1.1.8)
- Spherical: $\nabla \times \mathbf{f} = \hat{r}\frac{1}{r\sin\theta}\left[\frac{\partial}{\partial\theta}(f_\phi\sin\theta) - \frac{\partial f_\theta}{\partial\phi}\right] + \hat{\theta}\frac{1}{r}\left[\frac{1}{\sin\theta}\frac{\partial f_r}{\partial\phi} - \frac{\partial}{\partial r}(rf_\phi)\right] + \hat{\phi}\frac{1}{r}\left[\frac{\partial}{\partial r}(rf_\theta) - \frac{\partial f_r}{\partial\theta}\right]$ (1.1.9)

**Alternative definition** (curl in a given direction $\hat{a}$):

$$
\hat{a} \cdot (\nabla \times \mathbf{f}) = \lim_{\Delta s \to 0} \frac{1}{\Delta s} \oint_c \mathbf{f} \cdot d\mathbf{l}
\tag{1.1.10}
$$

**Stokes' Theorem:**

$$
\iint_S (\nabla \times \mathbf{f}) \cdot d\mathbf{S} = \oint_C \mathbf{f} \cdot d\mathbf{l}
\tag{1.1.11}
$$

**Gradient:**

$$
\nabla f = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \oint_s f \, d\mathbf{s}
\tag{1.1.12}
$$

$$
\hat{a} \cdot \nabla f = \frac{\partial f}{\partial a}
\tag{1.1.13}
$$

- Rectangular: $\nabla f = \hat{x}\frac{\partial f}{\partial x} + \hat{y}\frac{\partial f}{\partial y} + \hat{z}\frac{\partial f}{\partial z}$ (1.1.14)
- Cylindrical: $\nabla f = \hat{\rho}\frac{\partial f}{\partial \rho} + \hat{\phi}\frac{\partial f}{\rho\partial\phi} + \hat{z}\frac{\partial f}{\partial z}$ (1.1.15)
- Spherical: $\nabla f = \hat{r}\frac{\partial f}{\partial r} + \hat{\theta}\frac{\partial f}{r\partial\theta} + \hat{\phi}\frac{1}{r\sin\theta}\frac{\partial f}{\partial \phi}$ (1.1.16)

**Laplacian:**

$$
\nabla^2 f = \nabla \cdot (\nabla f)
\tag{1.1.17}
$$

- Rectangular: $\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}$ (1.1.18)
- Cylindrical: $\nabla^2 f = \frac{1}{\rho}\frac{\partial}{\partial \rho}\left(\rho\frac{\partial f}{\partial \rho}\right) + \frac{1}{\rho^2}\frac{\partial^2 f}{\partial \phi^2} + \frac{\partial^2 f}{\partial z^2}$ (1.1.19)
- Spherical: $\nabla^2 f = \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial f}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial \theta}\left(\sin\theta\frac{\partial f}{\partial \theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2 f}{\partial \phi^2}$ (1.1.20)

### 1.1.2 Symbolic Vector Method

Defines a symbolic vector $\tilde{\nabla}$ such that:

$$
T(\tilde{\nabla}) = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \oint_s T(\hat{n}) \, ds
\tag{1.1.21}
$$

Properties:
- $\tilde{\nabla} \cdot \mathbf{f} = \mathbf{f} \cdot \tilde{\nabla} = \nabla \cdot \mathbf{f}$
- $\tilde{\nabla} \times \mathbf{f} = -\mathbf{f} \times \tilde{\nabla} = \nabla \times \mathbf{f}$
- $\tilde{\nabla} f = f \tilde{\nabla} = \nabla f$

**Generalized Gauss' Theorem:**

$$
\iiint_V T(\tilde{\nabla}) \, dV = \oint_S T(\hat{n}) \, dS
\tag{1.1.37}
$$

**Key identities derived:**
- $\nabla \times (\nabla \times \mathbf{f}) = \nabla(\nabla \cdot \mathbf{f}) - \nabla^2 \mathbf{f}$ (1.1.27)
- $\nabla \cdot (a\mathbf{b}) = \mathbf{b} \cdot (\nabla a) + a\nabla \cdot \mathbf{b}$ (1.1.31)
- $\nabla \times (a\mathbf{b}) = -\mathbf{b} \times \nabla a + a\nabla \times \mathbf{b}$ (1.1.33)
- $\nabla \times (\mathbf{a} \times \mathbf{b}) = (\mathbf{b} \cdot \nabla)\mathbf{a} - \mathbf{b}\nabla \cdot \mathbf{a} + \mathbf{a}\nabla \cdot \mathbf{b} - (\mathbf{a} \cdot \nabla)\mathbf{b}$ (1.1.36)

**Curl Theorem:**

$$
\iiint_V \nabla \times \mathbf{f} \, dV = \oint_S d\mathbf{S} \times \mathbf{f}
\tag{1.1.38}
$$

---

### 1.1.3 Helmholtz Decomposition Theorem

Any smooth vector function $\mathbf{F}$ that vanishes at infinity can be decomposed:

$$
\mathbf{F} = \mathbf{F}_i + \mathbf{F}_s
\tag{1.1.43}
$$

- Irrotational (curl-free) part: $\nabla \times \mathbf{F}_i = 0$, $\nabla \cdot \mathbf{F}_i \neq 0$
- Solenoidal (divergence-free) part: $\nabla \cdot \mathbf{F}_s = 0$, $\nabla \times \mathbf{F}_s \neq 0$

**Key identities:**
- $\nabla \times (\nabla \phi) = 0$ (1.1.41)
- $\nabla \cdot (\nabla \times \mathbf{A}) = 0$ (1.1.42)

> Once both the divergence and curl of a vector function are specified, the function is fully determined.

### 1.1.4 Green's Theorems

**First Scalar Green's Theorem:**

$$
\iiint_V (a\nabla^2 b + \nabla a \cdot \nabla b) \, dV = \oint_S a\frac{\partial b}{\partial n} \, dS
\tag{1.1.45}
$$

**Second Scalar Green's Theorem:**

$$
\iiint_V (a\nabla^2 b - b\nabla^2 a) \, dV = \oint_S \left(a\frac{\partial b}{\partial n} - b\frac{\partial a}{\partial n}\right) dS
\tag{1.1.46}
$$

**First Vector Green's Theorem:**

$$
\iiint_V [(\nabla \times \mathbf{a}) \cdot (\nabla \times \mathbf{b}) - \mathbf{a} \cdot (\nabla \times \nabla \times \mathbf{b})] \, dV = \oint_S (\mathbf{a} \times \nabla \times \mathbf{b}) \cdot d\mathbf{S}
\tag{1.1.47}
$$

**Second Vector Green's Theorem:**

$$
\iiint_V [\mathbf{b} \cdot (\nabla \times \nabla \times \mathbf{a}) - \mathbf{a} \cdot (\nabla \times \nabla \times \mathbf{b})] \, dV = \oint_S (\mathbf{a} \times \nabla \times \mathbf{b} - \mathbf{b} \times \nabla \times \mathbf{a}) \cdot d\mathbf{S}
\tag{1.1.48}
$$

**Scalar–Vector Green's Theorem:**

$$
\iiint_V [b(\nabla \times \nabla \times \mathbf{a}) + \mathbf{a}\nabla^2 b + (\nabla \cdot \mathbf{a})\nabla b] \, dV
= \oint_S [(\hat{n} \cdot \mathbf{a})\nabla b + (\hat{n} \times \mathbf{a}) \times \nabla b + (\hat{n} \times \nabla \times \mathbf{a})b] \, dS
\tag{1.1.49}
$$

---

## 1.2 Maxwell's Equations in Terms of Total Charges and Currents

### 1.2.1 Maxwell's Equations in Integral Form

**Faraday's Induction Law:**

$$
\oint_C \mathbf{E}(\mathbf{r}, t) \cdot d\mathbf{l} = -\frac{d}{dt} \iint_S \mathbf{B}(\mathbf{r}, t) \cdot d\mathbf{S}
\tag{1.2.1}
$$

**Maxwell–Ampère Law:**

$$
\oint_C \mathbf{B}(\mathbf{r}, t) \cdot d\mathbf{l} = \epsilon_0\mu_0 \frac{d}{dt} \iint_S \mathbf{E}(\mathbf{r}, t) \cdot d\mathbf{S} + \mu_0 \iint_S \mathbf{J}_{\text{total}}(\mathbf{r}, t) \cdot d\mathbf{S}
\tag{1.2.2}
$$

**Gauss' Law (Electric):**

$$
\oint_S \mathbf{E}(\mathbf{r}, t) \cdot d\mathbf{S} = \frac{1}{\epsilon_0} \iiint_V \varrho_{e,\text{total}}(\mathbf{r}, t) \, dV
\tag{1.2.8}
$$

**Gauss' Law (Magnetic):**

$$
\oint_S \mathbf{B}(\mathbf{r}, t) \cdot d\mathbf{S} = 0
\tag{1.2.9}
$$

**Physical constants:**
- $\epsilon_0 = 8.854 \times 10^{-12}$ F/m $\approx 1/(36\pi) \times 10^{-9}$ F/m
- $\mu_0 = 4\pi \times 10^{-7}$ H/m

### 1.2.2 Maxwell's Equations in Differential Form

Applying Stokes' and Gauss' theorems to a continuous medium:

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
\tag{1.2.12}
$$

$$
\nabla \times \mathbf{B} = \epsilon_0\mu_0 \frac{\partial \mathbf{E}}{\partial t} + \mu_0 \mathbf{J}_{\text{total}}
\tag{1.2.13}
$$

$$
\nabla \cdot \mathbf{E} = \frac{\varrho_{e,\text{total}}}{\epsilon_0}
\tag{1.2.14}
$$

$$
\nabla \cdot \mathbf{B} = 0
\tag{1.2.15}
$$

### 1.2.3 Current Continuity Equation

$$
\nabla \cdot \mathbf{J}_{\text{total}} = -\frac{\partial \varrho_{e,\text{total}}}{\partial t}
\tag{1.2.16}
$$

**Integral form:**

$$
\oint_S \mathbf{J}_{\text{total}} \cdot d\mathbf{S} = -\frac{d}{dt} \iiint_V \varrho_{e,\text{total}} \, dV
\tag{1.2.17}
$$

> The four Maxwell's equations are not independent for time-varying fields — the continuity equation connects them.

### 1.2.4 The Lorentz Force Law

$$
\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})
\tag{1.2.18}
$$

---

## 1.3 Constitutive Relations

### 1.3.1 Electric Polarization

- **Dipole moment:** $\mathbf{p} = q\mathbf{l}$ (1.3.1)
- **Polarization vector:** $\mathbf{P} = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \sum_{i=1}^{n_p} \mathbf{p}_i$ (1.3.2)
- **Bound charge density:** $\varrho_{e,b} = -\nabla \cdot \mathbf{P}$ (1.3.3)
- **Total charge density:** $\varrho_{e,\text{total}} = \varrho_{e,f} + \varrho_{e,b}$ (1.3.4)

**Electric flux density:**

$$
\mathbf{D} = \epsilon_0\mathbf{E} + \mathbf{P}
\tag{1.3.6}
$$

**Gauss' law in terms of free charges:**

$$
\nabla \cdot \mathbf{D} = \varrho_{e,f}
\tag{1.3.7}
$$

**Linear dielectric:**

$$
\mathbf{P} = \epsilon_0\chi_e\mathbf{E}, \quad \mathbf{D} = \epsilon_0(1 + \chi_e)\mathbf{E} = \epsilon\mathbf{E}
\tag{1.3.9–1.3.10}
$$

- $\chi_e$ = electric susceptibility, $\epsilon = \epsilon_0(1 + \chi_e)$ = permittivity, $\epsilon_r = \epsilon/\epsilon_0$ = relative permittivity

### 1.3.2 Magnetization

- **Magnetic dipole moment:** $\mathbf{m} = I\mathbf{s}$ (1.3.12)
- **Magnetization vector:** $\mathbf{M} = \lim_{\Delta v \to 0} \frac{1}{\Delta v} \sum_{i=1}^{n_m} \mathbf{m}_i$ (1.3.13)
- **Magnetization current density:** $\mathbf{J}_m = \nabla \times \mathbf{M}$ (1.3.14)

**Magnetic field intensity:**

$$
\mathbf{H} = \frac{\mathbf{B}}{\mu_0} - \mathbf{M}
\tag{1.3.17}
$$

$$
\mathbf{B} = \mu_0(\mathbf{H} + \mathbf{M})
\tag{1.3.19}
$$

**Linear magnetic material:**

$$
\mathbf{M} = \chi_m\mathbf{H}, \quad \mathbf{B} = \mu_0(1 + \chi_m)\mathbf{H} = \mu\mathbf{H}
\tag{1.3.20–1.3.21}
$$

- $\chi_m$ = magnetic susceptibility, $\mu = \mu_0(1 + \chi_m)$ = permeability, $\mu_r = \mu/\mu_0$ = relative permeability

### 1.3.3 Electric Conduction

**Ohm's law (local form):**

$$
\mathbf{J}_c = \sigma \mathbf{E}
\tag{1.3.23}
$$

- $\sigma$ = conductivity (S/m)

### 1.3.4 Classification of Media

| Classification | Criterion |
|---|---|
| **Homogeneous vs inhomogeneous** | $\epsilon, \mu, \sigma$ depend on position? |
| **Stationary vs nonstationary** | $\epsilon, \mu, \sigma$ depend on time? |
| **Isotropic vs anisotropic** | $\mathbf{D} \parallel \mathbf{E}$, $\mathbf{B} \parallel \mathbf{H}$? |
| **Linear vs nonlinear** | $\epsilon, \mu, \sigma$ depend on field intensity? |
| **Dispersive vs nondispersive** | $\epsilon, \mu$ depend on frequency? |
| **Dielectric, lossy, conductor** | Value of $\sigma$ |
| **Diamagnetic/paramagnetic/ferromagnetic** | Value of $\mu$ |

**Anisotropic constitutive relations (tensor form):**

$$
\begin{bmatrix} D_x \\ D_y \\ D_z \end{bmatrix} =
\begin{bmatrix} \epsilon_{xx} & \epsilon_{xy} & \epsilon_{xz} \\ \epsilon_{yx} & \epsilon_{yy} & \epsilon_{yz} \\ \epsilon_{zx} & \epsilon_{zy} & \epsilon_{zz} \end{bmatrix}
\begin{bmatrix} E_x \\ E_y \\ E_z \end{bmatrix}
\tag{1.3.25}
$$

**Bianisotropic (most general linear form):**

$$
\mathbf{D} = \boldsymbol{\epsilon} \cdot \mathbf{E} + \boldsymbol{\xi} \cdot \mathbf{H}
$$
$$
\mathbf{B} = \boldsymbol{\mu} \cdot \mathbf{H} + \boldsymbol{\zeta} \cdot \mathbf{E}
\tag{1.3.28}
$$

**Dispersive media (convolution form):**

$$
\mathbf{D} = \epsilon_0\mathbf{E} + \epsilon_0 \int_{-\infty}^{t} \chi_e(t - \tau)\mathbf{E}(\tau) \, d\tau
\tag{1.3.29}
$$

$$
\mathbf{B} = \mu_0\mathbf{H} + \mu_0 \int_{-\infty}^{t} \chi_m(t - \tau)\mathbf{H}(\tau) \, d\tau
\tag{1.3.30}
$$

---

## 1.4 Maxwell's Equations in Terms of Free Charges and Currents

**Integral form:**

$$
\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \iint_S \mathbf{B} \cdot d\mathbf{S}
\tag{1.4.1}
$$

$$
\oint_C \mathbf{H} \cdot d\mathbf{l} = \frac{d}{dt} \iint_S \mathbf{D} \cdot d\mathbf{S} + \iint_S \mathbf{J}_f \cdot d\mathbf{S}
\tag{1.4.2}
$$

$$
\oint_S \mathbf{D} \cdot d\mathbf{S} = \iiint_V \varrho_{e,f} \, dV
\tag{1.4.3}
$$

$$
\oint_S \mathbf{B} \cdot d\mathbf{S} = 0
\tag{1.4.4}
$$

**With magnetic sources (symmetrized form):**

$$
\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \iint_S \mathbf{B} \cdot d\mathbf{S} - \iint_S \mathbf{M}_f \cdot d\mathbf{S}
\tag{1.4.5}
$$

$$
\oint_S \mathbf{B} \cdot d\mathbf{S} = \iiint_V \varrho_{m,f} \, dV
\tag{1.4.6}
$$

**Differential form:**

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} - \mathbf{M}_f
\tag{1.4.7}
$$

$$
\nabla \times \mathbf{H} = \frac{\partial \mathbf{D}}{\partial t} + \mathbf{J}_f
\tag{1.4.8}
$$

$$
\nabla \cdot \mathbf{D} = \varrho_{e,f}
\tag{1.4.9}
$$

$$
\nabla \cdot \mathbf{B} = \varrho_{m,f}
\tag{1.4.10}
$$

**Continuity equations:**

$$
\nabla \cdot \mathbf{J}_f = -\frac{\partial \varrho_{e,f}}{\partial t}
\tag{1.4.11}
$$

$$
\nabla \cdot \mathbf{M}_f = -\frac{\partial \varrho_{m,f}}{\partial t}
\tag{1.4.12}
$$

---

## 1.5 Boundary Conditions

**Tangential $\mathbf{H}$:**

$$
\hat{n} \times (\mathbf{H}_2 - \mathbf{H}_1) = \mathbf{J}_s
\tag{1.5.4}
$$

**Tangential $\mathbf{E}$:**

$$
\hat{n} \times (\mathbf{E}_2 - \mathbf{E}_1) = -\mathbf{M}_s
\tag{1.5.5}
$$

**Normal $\mathbf{D}$:**

$$
\hat{n} \cdot (\mathbf{D}_2 - \mathbf{D}_1) = \varrho_{e,s}
\tag{1.5.7}
$$

**Normal $\mathbf{B}$:**

$$
\hat{n} \cdot (\mathbf{B}_2 - \mathbf{B}_1) = \varrho_{m,s}
\tag{1.5.8}
$$

**PEC (Perfect Electric Conductor) boundary:**

$$
\hat{n} \times \mathbf{E} = 0
\tag{1.5.9}
$$

$$
\hat{n} \times \mathbf{H} = \mathbf{J}_s
\tag{1.5.10}
$$

$$
\hat{n} \cdot \mathbf{D} = \varrho_{e,s}
\tag{1.5.11}
$$

$$
\hat{n} \cdot \mathbf{B} = 0
\tag{1.5.12}
$$

---

## 1.6 Energy, Power, and Poynting's Theorem

Starting from Maxwell's equations with impressed currents $\mathbf{J}_i$, $\mathbf{M}_i$:

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} - \mathbf{M}_i
\tag{1.6.1}
$$

$$
\nabla \times \mathbf{H} = \frac{\partial \mathbf{D}}{\partial t} + \sigma\mathbf{E} + \mathbf{J}_i
\tag{1.6.2}
$$

Derived power balance:

$$
\nabla \cdot (\mathbf{E} \times \mathbf{H}) + \mathbf{E} \cdot \frac{\partial \mathbf{D}}{\partial t} + \mathbf{H} \cdot \frac{\partial \mathbf{B}}{\partial t} + \sigma \mathbf{E} \cdot \mathbf{E} + \mathbf{E} \cdot \mathbf{J}_i + \mathbf{H} \cdot \mathbf{M}_i = 0
\tag{1.6.4}
$$

**Poynting vector (power flux density):**

$$
\mathbf{S} = \mathbf{E} \times \mathbf{H}
\tag{1.6.17}
$$

**Energy densities:**
- Electric: $\mathcal{w}_e = \frac{1}{2}\epsilon E^2$ (J/m³)
- Magnetic: $\mathcal{w}_m = \frac{1}{2}\mu H^2$ (J/m³)

**Poynting's theorem (global form):**

$$
P_s = P_e + P_d + \frac{d}{dt}(W_e + W_m)
\tag{1.6.14}
$$

where:
- $P_s = -\iiint_V (\mathbf{E} \cdot \mathbf{J}_i + \mathbf{H} \cdot \mathbf{M}_i) \, dV$ — supplied power
- $P_e = \oint_S (\mathbf{E} \times \mathbf{H}) \cdot \hat{n} \, dS$ — exiting power
- $P_d = \iiint_V \sigma E^2 \, dV$ — dissipated power
- $W_e = \frac{1}{2}\iiint_V \epsilon E^2 \, dV$ — electric energy
- $W_m = \frac{1}{2}\iiint_V \mu H^2 \, dV$ — magnetic energy

---

## 1.7 Time-Harmonic Fields

### 1.7.1 Phasor Representation

For time-harmonic fields at angular frequency $\omega$:

$$
\mathbf{E}(\mathbf{r}, t) = \text{Re}[\mathbf{E}(\mathbf{r}) e^{j\omega t}]
\tag{1.7.4}
$$

**Replacement rule:** $\partial/\partial t \to j\omega$

**Maxwell's equations in phasor form:**

$$
\nabla \times \mathbf{E} = -j\omega\mathbf{B} - \mathbf{M}_f
\tag{1.7.6}
$$

$$
\nabla \times \mathbf{H} = j\omega\mathbf{D} + \mathbf{J}_f
\tag{1.7.7}
$$

$$
\nabla \cdot \mathbf{D} = \varrho_{e,f}
\tag{1.7.8}
$$

$$
\nabla \cdot \mathbf{B} = \varrho_{m,f}
\tag{1.7.9}
$$

$$
\nabla \cdot \mathbf{J}_f = -j\omega\varrho_{e,f}
\tag{1.7.10}
$$

$$
\nabla \cdot \mathbf{M}_f = -j\omega\varrho_{m,f}
\tag{1.7.11}
$$

### 1.7.2 Fourier Transforms

An arbitrary time-domain field can be represented as:

$$
\mathbf{E}(\mathbf{r}, t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \mathbf{E}(\mathbf{r}, \omega) e^{j\omega t} \, d\omega
\tag{1.7.14}
$$

Fourier-transformed Maxwell's equations are identical to the phasor form, with $\omega$ now as a continuous variable.

### 1.7.3 Complex Power

**Time-average of product of two phasors:**

$$
\overline{\mathbf{A}(t) \circ \mathbf{B}(t)} = \frac{1}{2}\text{Re}[\mathbf{A} \circ \mathbf{B}^*]
\tag{1.7.22}
$$

**Complex Poynting vector:**

$$
\mathbf{S} = \frac{1}{2} \mathbf{E} \times \mathbf{H}^*
\tag{1.7.24}
$$

**Time-average Poynting vector:** $\overline{\mathbf{S}} = \text{Re}(\mathbf{S})$

**Time-average energy densities:**
- Electric: $w_e = \frac{1}{4}\epsilon|\mathbf{E}|^2$
- Magnetic: $w_m = \frac{1}{4}\mu|\mathbf{H}|^2$

**Poynting's theorem for complex phasors (differential form):**

$$
p_s = p_e + p_d + j2\omega(w_m - w_e)
\tag{1.7.39}
$$

**Integral form:**

$$
P_s = P_e + P_d + j2\omega(W_m - W_e)
\tag{1.7.40}
$$

- $\text{Re}(P_s) = \text{Re}(P_e) + P_d$ — real power balance
- $\text{Im}(P_s) = \text{Im}(P_e) + 2\omega(W_m - W_e)$ — reactive power balance

### 1.7.4 Complex Permittivity and Permeability

**Complex constitutive parameters:**

$$
\epsilon_r = \epsilon'_r - j\epsilon''_r, \quad \mu_r = \mu'_r - j\mu''_r
\tag{1.7.56}
$$

**Loss tangents:**

$$
\tan\delta_e = \frac{\epsilon''_r}{\epsilon'_r}, \quad \tan\delta_m = \frac{\mu''_r}{\mu'_r}
\tag{1.7.57}
$$

**Kramers–Krönig relations (causality condition):**

$$
\epsilon'(\omega) = \epsilon_\infty + \frac{2}{\pi} \mathcal{P}\!\!\int_{0}^{\infty} \frac{z\epsilon''(z)}{z^2 - \omega^2} \, dz
$$
$$
\epsilon''(\omega) = -\frac{2\omega}{\pi} \mathcal{P}\!\!\int_{0}^{\infty} \frac{\epsilon'(z) - \epsilon_\infty}{z^2 - \omega^2} \, dz
\tag{1.7.58}
$$

**Combined conduction and dielectric loss:**

$$
\nabla \times \mathbf{H} = j\omega\epsilon_0\left[\epsilon'_r - j\left(\epsilon''_r + \frac{\sigma}{\omega\epsilon_0}\right)\right] \mathbf{E} + \mathbf{J}_i
\tag{1.7.59}
$$

**Effective loss tangent:**

$$
\tan\delta_e = \frac{\epsilon''_r}{\epsilon'_r} + \frac{\sigma}{\omega\epsilon'_r\epsilon_0}
\tag{1.7.60}
$$

---

## Examples

### Example 1.1 — Generalized Gauss' Theorem Application
Derive $\iiint_V (\mathbf{b}\nabla\cdot\mathbf{a} + \mathbf{a}\cdot\nabla\mathbf{b}) \, dV = \oint_S (\hat{n}\cdot\mathbf{a})\mathbf{b} \, dS$ from the generalized Gauss' theorem.

### Example 1.2 — Derivation of Scalar–Vector Green's Theorem
From the second vector Green's theorem with $\mathbf{b} = \hat{b}b$, derive the scalar–vector Green's theorem.

### Example 1.3 — Kirchhoff's Voltage Law from Faraday's Law
Applying $\oint \mathbf{E} \cdot d\mathbf{l} = -d/dt \iint \mathbf{B} \cdot d\mathbf{S}$ to an RLC circuit yields $\sum_{i=1}^{N} V_i = 0$.

### Example 1.4 — Kirchhoff's Current Law from Continuity
Applying $\oint_S \mathbf{J} \cdot d\mathbf{S} = -d/dt \iiint \varrho \, dV$ to a circuit node yields $\sum_{i=1}^{N} I_i = 0$.

### Example 1.5 — Boundary Conditions for Total vs Free Quantities
Showing that magnetization produces a surface current $\mathbf{J}_{m,s} = -\hat{n} \times \mathbf{M}$, and polarization produces bound surface charge $\varrho_{e,s,b} = \hat{n} \cdot \mathbf{P}$.

### Example 1.6 — Lorentz Model of Dielectric Permittivity
For a classical electron oscillator model:
$$
\epsilon_r(\omega) = 1 + \frac{N_e q_e^2}{\epsilon_0 m_e(\omega_0^2 - \omega^2 + j\omega\delta)}
$$

### Example 1.7 — Power Dissipation in a Slotted Metallic Box
Time-average power dissipated: $P_d = \sqrt{3} w l E_0^2 / (8\eta)$
Energy difference: $W_e - W_m = w l E_0^2 / (16\omega\eta)$

### Example 1.8 — Drude Model of Plasma Permittivity
$$
\epsilon_{\text{eff}} = \epsilon_0 + \frac{\epsilon_0\omega_p^2}{j\omega(\nu + j\omega)}, \quad \omega_p = \sqrt{\frac{N_e q_e^2}{\epsilon_0 m_e}}
$$

### Example 1.9 — Kramers–Krönig Relations
Proof via Cauchy integration theorem on the complex susceptibility function.

---

## Problems (Ch1, 25 problems)

| # | Topic |
|---|---|
| 1.1–1.3 | Divergence, curl, gradient derivations from definitions |
| 1.4–1.5 | $\nabla(1/R)$ and $\nabla^2(1/R)$ — Dirac delta |
| 1.6–1.7 | Vector identities via symbolic vector method |
| 1.8 | Green's theorems on a vanishingly thin surface |
| 1.9 | Helmholtz decomposition theorem proof |
| 1.10 | Resistance of a conductive post |
| 1.11–1.12 | Electrostatic and magnetostatic boundary value problems |
| 1.13–1.14 | Capacitor with dielectric slab — forces |
| 1.15 | Cylindrical charge distribution — field and surface charge |
| 1.16 | Parallel-plate waveguide — fields and currents |
| 1.17 | Equivalence of total vs free charge formulations |
| 1.18 | From differential + boundary conditions back to integral form |
| 1.19 | Thin resistive sheet boundary conditions |
| 1.20 | Time-domain susceptibility for Lorentz and Drude models |
| 1.21–1.24 | Waveguide power dissipation problems |
| 1.25 | Kramers–Krönig for Lorentz and Drude models |
