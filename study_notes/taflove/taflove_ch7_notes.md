---
chapter: 7
title: Perfectly Matched Layer Absorbing Boundary Conditions
book: Computational Electrodynamics — The Finite-Difference Time-Domain Method (3rd Ed.)
author: Stephen Gedney
raw_size: 114,254 bytes
sections: 9
---

# Chapter 7: Perfectly Matched Layer (PML) Absorbing Boundary Conditions

## 7.1 Introduction

PML, introduced by Berenger (1994), is an absorbing material ABC that is reflectionless for plane waves of arbitrary incidence, polarization, and frequency. Unlike analytical ABCs (Ch6), PML works for inhomogeneous, dispersive, anisotropic, and nonlinear media.

**Evolution:** Split-field PML → Stretched-coordinate PML → UPML (Uniaxial PML) → CPML (Convolutional PML)

## 7.2 Plane Wave Incident Upon a Lossy Half-Space

Conventional lossy materials are matched only for normal incidence. For a plane wave at angle $\theta$:

$$R(\theta) = \frac{\eta_2 \cos\theta - \eta_1 \cos\theta_t}{\eta_2 \cos\theta + \eta_1 \cos\theta_t}$$

where $\eta_1 = \sqrt{\mu_0/\epsilon_0}$ and $\eta_2 = \sqrt{j\omega\mu_0/(\sigma + j\omega\epsilon_0)}$.

## 7.3 Berenger's Split-Field PML

Berenger split each field component into two orthogonal components:
$$E_z = E_{zx} + E_{zy}, \quad H_z = H_{zx} + H_{zy}$$

### 7.3.1 2D TE$_z$ Case

Maxwell's equations modified for the split-field PML:

$$\epsilon_0 \frac{\partial E_{zx}}{\partial t} + \sigma_x E_{zx} = \frac{\partial H_y}{\partial x}$$
$$\epsilon_0 \frac{\partial E_{zy}}{\partial t} + \sigma_y E_{zy} = -\frac{\partial H_x}{\partial y}$$
$$\mu_0 \frac{\partial H_x}{\partial t} + \sigma_x^* H_x = -\frac{\partial E_z}{\partial x} \quad \text{(split similarly)}$$

**Perfect matching condition:** Loss parameters must satisfy:
$$\frac{\sigma_x}{\epsilon_0} = \frac{\sigma_x^*}{\mu_0} \quad \text{and} \quad \frac{\sigma_y}{\epsilon_0} = \frac{\sigma_y^*}{\mu_0} \tag{7.8}$$

When the PML conductivity $\sigma_x$ and magnetic loss $\sigma_x^*$ satisfy (7.8), the PML/vacuum interface has zero reflection for all angles and frequencies.

Inside the PML, the wave decays as:

$$e^{-\sigma_x \eta \cos\theta \cdot x} \quad \text{where } \eta = \sqrt{\mu_0/\epsilon_0}$$

## 7.4 Stretched-Coordinate Formulation

The PML can be interpreted as a coordinate stretching into complex space:

$$\tilde{x} = \int_0^x s_x(x') dx', \quad s_x = 1 + \frac{\sigma_x}{j\omega\epsilon_0}$$

Maxwell's equations in stretched coordinates:

$$\nabla_s \times \mathbf{H} = j\omega\epsilon_0 \mathbf{E}$$
$$\nabla_s \times \mathbf{E} = -j\omega\mu_0 \mathbf{H}$$

where $\nabla_s = \hat{x}\frac{1}{s_x}\frac{\partial}{\partial x} + \hat{y}\frac{1}{s_y}\frac{\partial}{\partial y} + \hat{z}\frac{1}{s_z}\frac{\partial}{\partial z}$.

## 7.5 Uniaxial PML (UPML)

The UPML is a physical anisotropic medium with permittivity and permeability tensors:

$$\bar{\bar{\epsilon}} = \epsilon_0 \epsilon_r \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & s_z \end{bmatrix}, \quad
\bar{\bar{\mu}} = \mu_0 \mu_r \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & s_z \end{bmatrix} \tag{7.53}$$

where $s_x = \kappa_x + \frac{\sigma_x}{j\omega\epsilon_0}$, and the matching condition $s_x = s_y = s_z$ ensures zero reflection.

### 7.5.1 Perfectly Matched Uniaxial Medium

The reflection coefficient at a UPML interface is zero when:

$$s_x = s_y, \quad \epsilon_1 = \epsilon_2, \quad \mu_1 = \mu_2$$

### 7.5.2 Relation to Berenger's Split-Field PML

The UPML is equivalent to Berenger's split-field formulation when $s_x = 1 + \sigma_x/(j\omega\epsilon_0)$. The key advantage of UPML is avoiding nonphysical field splitting.

## 7.6 Theoretical PML Performance

### 7.6.1 Continuous Space

The theoretical reflection error for a PEC-backed PML of thickness $d$:

$$R(\theta) = e^{-2\sigma \eta d\cos\theta / (m+1)} \tag{7.58}$$

### 7.6.2 Discrete Space — Loss Parameter Grading

**Polynomial grading:**
$$\sigma_x(x) = \left(\frac{x}{d}\right)^m \sigma_{x,\text{max}} \tag{7.60}$$
$$\sigma_{x,\text{max}} \approx -\frac{(m+1) \ln R(0)}{2\eta d} \tag{7.62}$$

**Geometric grading:**
$$\sigma_x(x) = \sigma_{x,0} g^{x/\Delta} \tag{7.63}$$

## 7.7 Complex Frequency-Shifted (CFS) Tensor

Improves PML absorption of evanescent waves and late-time reflections:

$$s_x = \kappa_x + \frac{\sigma_x}{\alpha_x + j\omega\epsilon_0} \tag{7.55}$$

Typical values: $\kappa_x = 1$–11, $\alpha_x = 0.001$–0.05.

## 7.8 UPML Implementation in FDTD

Using the ADE (Auxiliary Differential Equation) approach:

$$\mathbf{D} = \epsilon_0 \bar{\bar{\epsilon}}_r \mathbf{E}$$

The update equations involve integrating $s_x$ factors via time-domain recursions.

For example, the $D_x$ to $E_x$ conversion:

$$E_x = \frac{1}{\epsilon_0} \left[ \frac{D_x}{\kappa_x} - \psi_{E_x}^n \right]$$

where $\psi_{E_x}$ is an accumulated convolution term:

$$\psi_{E_x}^n = b_x \psi_{E_x}^{n-1} + a_x \left( \frac{D_x^{n-1}}{\kappa_x} \right)$$

$$b_x = e^{-(\sigma_x/\kappa_x + \alpha_x)\Delta t/\epsilon_0}, \quad a_x = \frac{\sigma_x}{\kappa_x(\sigma_x + \kappa_x\alpha_x)} (b_x - 1)$$

## 7.9 CPML (Convolutional PML)

Roden & Gedney's CPML applies stretched-coordinate PML via discrete convolution:

$$\frac{\partial}{\partial\tilde{x}} = \frac{1}{\kappa_x} \frac{\partial}{\partial x} + \zeta_x(t) * \frac{\partial}{\partial x}$$

where $\zeta_x(t) = -\frac{\sigma_x}{\epsilon_0 \kappa_x^2} e^{-(\sigma_x/\kappa_x + \alpha_x)t/\epsilon_0} u(t)$ is implemented recursively.

---

## Example 7.1: 1D FDTD with PML Terminal

Implement an 8-cell PML to terminate a 1D grid. Compare reflection vs. Mur ABC.

**Setup:** 200-cell vacuum, PML thickness $d = 8\Delta$, polynomial grading $m=3$, $\sigma_{\text{max}}$ from $R(0) = 10^{-4}$.

**Result:** PML achieves $R < -60$ dB vs. Mur's $-30$ dB.

---

## Example 7.2: 2D TM$_z$ UPML — Reflection Error vs. PML Thickness

Compute reflection error for a 2D domain as function of PML thickness $d$ and grading order $m$.

**Setup:** 80×80 cell grid with UPML on all sides. Point source at center. Measure $E_z$ at probe point near PML interface.

**Result:** $d=8$, $m=3$ gives $R \approx -60$ dB; $d=16$, $m=4$ gives $R \approx -80$ dB.

---

## Example 7.3: CFS-CPML Absorption of Evanescent Waves

Compare standard PML vs. CFS-CPML for termination close to a metallic edge (strong evanescent fields).

**Setup:** Thin wire radiating 0.1$\lambda_0$ from PML boundary. CFS parameters $\kappa_{\text{max}}=5$, $\alpha=0.02$.

**Result:** CFS-CPML reduces late-time reflections by 20+ dB compared to standard PML.

---

## Audit Table

| Concept | Section | Key Equation | Implementation |
|---------|---------|-------------|----------------|
| Loss half-space matching | 7.2 | — | — |
| Berenger split-field | 7.3 | (7.11) | — |
| Perfect matching condition | 7.3 | (7.8) | — |
| Stretched-coordinate PML | 7.4 | (7.26) | — |
| UPML tensor | 7.5 | (7.53) | Example 7.2 |
| Reflection error (continuous) | 7.6 | (7.58) | — |
| Polynomial grading | 7.6 | (7.60)-(7.62) | Example 7.1 |
| Geometric grading | 7.6 | (7.63) | — |
| CFS tensor | 7.7 | (7.55) | Example 7.3 |
| UPML ADE implementation | 7.8 | — | Example 7.2 |
| CPML recursive convolution | 7.9 | — | Example 7.3 |

> **Numerical Intuition:** PML is the gold standard for lattice truncation in FDTD. With $d = 8$–16 cells and $m = 3$–4 polynomial grading, reflection errors below $-80$ dB are routine. The CPML with CFS tensor coefficients is preferred for evanescent fields and dispersive media. PML thickness is one of the key trade-offs: thicker PML → lower reflection but more computational overhead. For most problems, 10 cells of PML with $m=3$ grading is a good starting point.
