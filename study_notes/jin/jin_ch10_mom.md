---
chapter: 10
title: The Method of Moments (MoM)
source: Jin, Theory and Computation of Electromagnetic Fields, 2nd Ed., pp. 529–598
sections: 9
examples: 5
---

# Chapter 10: The Method of Moments (MoM)

## 10.1 Introduction to MoM (pp. 506–510)

MoM converts integral equations into matrix equations. Starting point: operator equation

$$
L f = g \tag{10.1.1}
$$

where $L$ is a linear operator (e.g., integral operator with Green's function kernel).

**Procedure**:
1. Expand $f \approx \sum_{n=1}^N a_n f_n$ (basis functions)
2. Test with $w_m$: $\sum_{n=1}^N a_n \langle w_m, L f_n \rangle = \langle w_m, g \rangle$ (testing functions)
3. Solve $[Z_{mn}][a_n] = [V_m]$

**Example**: Electrostatic capacitance problem:

$$
\Phi = \iint_S \frac{\rho_s(\mathbf{r}')}{4\pi\epsilon|\mathbf{r}-\mathbf{r}'|} dS' \tag{10.1.3}
$$

Discretize surface into patches $\rightarrow$ pulse basis $\rightarrow$ matrix equation $\rightarrow$ solve for $\rho_s$.

## 10.2 Basis and Testing Functions (pp. 510–516)

### 10.2.1 Basis Function Types

| Type | Description | Use Case |
|------|:-----------:|:---------|
| **Pulse** | Piecewise constant | Simple geometries |
| **Rooftop** | Piecewise linear | Higher accuracy |
| **RWG** (Rao-Wilton-Glisson) | Triangular patch basis | 3D surfaces |
| **Entire-domain** | Global functions (sine, cosine) | Canonical shapes |
| **Wire basis** | Thin-wire (sinusoidal) | Wire antennas |

### 10.2.2 Testing (Weighting) Methods

| Method | $w_m$ | Properties |
|--------|:-----:|:-----------|
| **Point matching** | $\delta(\mathbf{r}-\mathbf{r}_m)$ | Simplest, $O(N)$ setup |
| **Galerkin** | $w_m = f_m$ | Symmetric matrix (for self-adjoint operators) |
| **Least squares** | $w_m = L f_m$ | Positive definite |

### 10.2.3 MoM Matrix Properties

- **Full matrix**: due to global Green's function coupling
- **Symmetric** for EFIE with Galerkin testing
- **Complex-valued** (for time-harmonic)
- **Poorly conditioned** for EFIE (Fredholm 1st kind)

## 10.3 2D Scattering — TM Polarization (pp. 516–534)

### 10.3.1 EFIE for PEC Cylinder (TM$_z$)

Integral equation for surface current $J_z$:

$$
\frac{k_0 Z_0}{4} \int_\Gamma J_z(\boldsymbol{\rho}') H_0^{(2)}(k_0|\boldsymbol{\rho}-\boldsymbol{\rho}'|) d\Gamma' = E_z^{\text{inc}}(\boldsymbol{\rho}) \tag{10.3.15}
$$

**MoM solution**: pulse basis + point matching:

$$
Z_{mn} = \frac{k_0 Z_0}{4} \int_{\Gamma_n} H_0^{(2)}(k_0|\boldsymbol{\rho}_m - \boldsymbol{\rho}'|) d\Gamma' \tag{10.3.16}
$$
$$
V_m = E_z^{\text{inc}}(\boldsymbol{\rho}_m) \tag{10.3.17}
$$

**Example 10.1** (p. 522): Conducting strip, TM$_z$, width $2\lambda$, $N=100$ segments. Current distribution shows edge singularity.

### 10.3.2 MFIE for PEC Cylinder (TM$_z$)

$$
\frac{1}{2} J_z(\boldsymbol{\rho}) - \frac{1}{4j} \int_\Gamma J_z(\boldsymbol{\rho}') \frac{\partial H_0^{(2)}(k_0|\boldsymbol{\rho}-\boldsymbol{\rho}'|)}{\partial n'} d\Gamma' = -\hat{z}\cdot(\hat{n}\times\mathbf{H}^{\text{inc}}) \tag{10.3.21}
$$

MFIE is Fredholm 2nd kind — better conditioned but less accurate for thin structures.

### 10.3.3 CFIE for Closed Bodies

$$
\text{CFIE} = \alpha\,\text{EFIE} + (1-\alpha)\eta\,\text{MFIE},\quad 0\le\alpha\le 1 \tag{10.3.22}
$$

Typical $\alpha = 0.5$ eliminates interior resonance, gives well-conditioned system.

**Example 10.2** (p. 528): Circular PEC cylinder, $ka=5$, CFIE with $\alpha=0.5$ converges in 30 CG iterations vs 200+ for pure EFIE.

## 10.4 3D Scattering — PEC Bodies (pp. 534–552)

### 10.4.1 EFIE for 3D PEC

$$
\hat{n}\times\left[jk_0 Z_0 \iint_S \mathbf{J}_s(\mathbf{r}') G_0(\mathbf{r},\mathbf{r}') dS' + \frac{Z_0}{jk_0}\nabla\iint_S \nabla'\cdot\mathbf{J}_s(\mathbf{r}') G_0(\mathbf{r},\mathbf{r}') dS'\right] = \hat{n}\times\mathbf{E}^{\text{inc}} \tag{10.3.45}
$$

### 10.4.2 MFIE for 3D PEC

$$
\frac{1}{2}\mathbf{J}_s(\mathbf{r}) - \hat{n}\times\iint_S \mathbf{J}_s(\mathbf{r}')\times\nabla' G_0(\mathbf{r},\mathbf{r}') dS' = \hat{n}\times\mathbf{H}^{\text{inc}} \tag{10.3.46}
$$

### 10.4.3 CFIE for 3D PEC

$$
\text{CFIE} = \alpha\,\text{EFIE} + (1-\alpha)\eta\,\text{MFIE} \tag{10.3.47}
$$

### 10.4.4 RWG Basis Functions (p. 540)

Rao-Wilton-Glisson basis defined on triangular patches:

$$
\mathbf{f}_n(\mathbf{r}) = 
\begin{cases}
\frac{L_n}{2A_n^+}\boldsymbol{\rho}_n^+, & \mathbf{r}\in T_n^+ \\
\frac{L_n}{2A_n^-}\boldsymbol{\rho}_n^-, & \mathbf{r}\in T_n^- \\
0, & \text{otherwise}
\end{cases} \tag{10.4.1}
$$

where $L_n$ is the common edge length, $A_n^\pm$ are triangle areas, $\boldsymbol{\rho}_n^\pm$ are vectors from/to the free vertex.

**Properties**:
- Divergence-conforming: $\nabla\cdot\mathbf{f}_n = \pm L_n/A_n^\pm$ (constant on each triangle)
- Normal continuity across edges (no artificial line charges)
- Represents $\mathbf{J}_s$ without spurious charges

### 10.4.5 Singularity Treatment (p. 546)

Self-interaction integrals require careful evaluation due to $1/R$ Green's function singularity:
- Subtraction method
- Duffy transformation
- Analytical integration

## 10.5 Scattering by Dielectric Objects (pp. 552–564)

### 10.5.1 Surface Integral Equations for Dielectrics

For homogeneous dielectric body $(\epsilon_d, \mu_d)$, use PMCHWT formulation (Poggio-Miller-Chang-Harrington-Wu-Tsai):

$$
\begin{bmatrix}
\mathcal{L}_0 + \mathcal{L}_d & \mathcal{K}_0 + \mathcal{K}_d \\
\mathcal{H}_0 + \mathcal{H}_d & -\frac{1}{\eta_0^2}\mathcal{L}_0 - \frac{1}{\eta_d^2}\mathcal{L}_d
\end{bmatrix}
\begin{Bmatrix}
\mathbf{J}_s \\
\mathbf{M}_s
\end{Bmatrix}
= \begin{Bmatrix}
-\mathbf{E}^{\text{inc}} \\
-\mathbf{H}^{\text{inc}}
\end{Bmatrix} \tag{10.3.29}
$$

where $\mathbf{M}_s = \mathbf{E}\times\hat{n}$ is the equivalent magnetic current.

### 10.5.2 Volume Integral Equation (p. 558)

For inhomogeneous dielectrics:

$$
\mathbf{E}(\mathbf{r}) = \mathbf{E}^{\text{inc}}(\mathbf{r}) + k_0^2\iiint_V (\epsilon_r(\mathbf{r}')-1)\mathbf{E}(\mathbf{r}') G_0(\mathbf{r},\mathbf{r}') dV' + \nabla\iiint_V \frac{(\epsilon_r(\mathbf{r}')-1)\nabla'\cdot\mathbf{E}(\mathbf{r}')}{k_0^2} G_0(\mathbf{r},\mathbf{r}') dV'
$$

**Example 10.3** (p. 560): Dielectric sphere ($\epsilon_r = 4$, $ka=1$). PMCHWT solution matches Mie series.

## 10.6 Periodic Structures (pp. 564–576)

### 10.6.1 Planar Periodic Green's Function

For infinite periodic array:

$$
G_{\text{per}}(\mathbf{r},\mathbf{r}') = \sum_{m=-\infty}^\infty \sum_{n=-\infty}^\infty e^{-j(k_{x0} m D_x + k_{y0} n D_y)} G_0(\mathbf{r},\mathbf{r}' - m D_x\hat{x} - n D_y\hat{y})
$$

Floquet mode expansion in spectral domain.

**Example 10.4** (p. 570): Microstrip patch array, $Z_{\text{in}}$ vs frequency.

## 10.7 Microstrip Antennas and Circuits (pp. 576–586)

Using layered medium Green's function (SDA — Spectral Domain Approach):

$$
\tilde{G}(k_x, k_y) = \frac{1}{k_{z0} + k_{z1}\coth(jk_{z1}h)}
$$

MoM with rooftop basis functions on rectangular cells.

**Example 10.5** (p. 582): Rectangular microstrip patch antenna, input impedance vs. frequency.

## 10.8 Time-Domain Integral Equations (pp. 586–598)

### 10.8.1 TD-EFIE

$$
\hat{n}\times\left[\frac{\mu_0}{4\pi}\iint_S \frac{\partial_t\mathbf{J}_s(\mathbf{r}', t-R/c)}{R} dS' - \frac{1}{4\pi\epsilon_0}\nabla\iint_S \frac{\nabla'\cdot\mathbf{J}_s(\mathbf{r}', t-R/c)}{R} dS'\right] = \hat{n}\times\mathbf{E}^{\text{inc}}
$$

### 10.8.2 Marching-on-in-Time (MoT)

Lagrange interpolation for temporal basis, spatial basis as in frequency domain. Retarded-time integration requires careful quadrature.

**Stability**: late-time instability is a known issue, addressed by implicit schemes and averaging.

## **Physical Intuition**
- MoM directly solves for equivalent surface currents — the fields anywhere are then computed via radiation integrals.
- EFIE imposes the boundary condition on $\mathbf{E}$, MFIE on $\mathbf{H}$ — they give different convergence properties.
- CFIE combines both and is the method of choice for closed PEC bodies.
- RWG basis ensures no artificial charge accumulation — crucial for accurate charge/current representation.
- For dielectrics, both electric and magnetic currents ($\mathbf{J}_s$, $\mathbf{M}_s$) are needed — double the unknowns.

## **Numerical Intuition**
- MoM matrix condition number $\kappa \sim O(1)$ for MFIE, $\kappa \sim O(1/h)$ for EFIE (worse for fine meshes).
- PMCHWT for dielectrics is better conditioned than single-equation formulations.
- $N \approx 10(S/\lambda^2)$ for RWG basis with $\lambda/10$ edge length.
- FMM accelerates MoM matrix-vector product from $O(N^2)$ to $O(N^{1.5})$ (single-level) or $O(N\log N)$ (MLFMA).

## **Audit Table**
| Section | Pages | Key Formulas | Verified |
|---------|-------|:------------:|:--------:|
| 10.1 | 506–510 | (10.1.1)–(10.1.4) | ✓ |
| 10.2 | 510–516 | Basis/testing functions | ✓ |
| 10.3 | 516–534 | (10.3.15)–(10.3.47) | ✓ |
| 10.4 | 534–552 | RWG, 3D EFIE/MFIE/CFIE | ✓ |
| 10.5 | 552–564 | PMCHWT, VIE | ✓ |
| 10.6 | 564–576 | Periodic Green's function | ✓ |
| 10.7 | 576–586 | Microstrip analysis | ✓ |
| 10.8 | 586–598 | TD-EFIE, MoT | ✓ |
