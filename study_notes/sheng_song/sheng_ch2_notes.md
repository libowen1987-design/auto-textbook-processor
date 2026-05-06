---
title: "Ch2: Method of Moments"
book: "Sheng & Song, Essentials of Computational Electromagnetics (2012)"
chapter: 2
pages: "29-150"
weight: 2
topics:
  - Method of Moments (MoM)
  - 3D PEC scattering
  - EFIE and MFIE
  - RWG basis functions
  - Singularity handling
  - Fast Multipole Method (FMM)
  - MLFMA
  - Parallel computing
  - Homogeneous dielectric scattering
  - Inhomogeneous dielectric (VIE)
  - 2D and periodic problems
notes_version: "1.0"
---

# Chapter 2: Method of Moments

## Outline

| § | Topic | Page |
|:-:|-------|:----:|
| 2.1 | Scattering from 3D PEC Objects | 29 |
| 2.2 | Scattering from 3D Homogeneous Dielectric Objects | 109 |
| 2.3 | Scattering from 3D Inhomogeneous Dielectric Objects | 128 |
| 2.4 | Essential Points in MoM for Solving Other Problems | 136 |

---

## 2.1 Scattering from 3D PEC Objects

The method of moments (MoM) is a full-wave numerical method that discretizes the integral equations of electromagnetic fields. Since integral equations automatically satisfy the Sommerfeld radiation condition, MoM is especially suitable for **open problems** — scattering and radiation.

The four essential aspects of MoM:
1. **Choice of basis and testing functions**
2. **Handling of singularities**
3. **Relationship between discretized forms and numerical performance**
4. **Accelerating the solution of discretized matrix equations**

### 2.1.1 Formulation of the Problem

For radar scattering from metallic targets (aircraft, ships, etc.), the incident wave is approximated by a plane wave:

$$
\mathbf{E}^i(\mathbf{r}) = (\cos\alpha\,\hat{\boldsymbol{\theta}} + \sin\alpha\,\hat{\boldsymbol{\phi}})\,e^{-j\mathbf{k}^i\cdot\mathbf{r}}
\tag{2.1}
$$

$$
\mathbf{H}^i(\mathbf{r}) = \frac{1}{\eta}\,\hat{\mathbf{k}}^i \times \mathbf{E}^i(\mathbf{r})
\tag{2.2}
$$

where $\alpha$ is the polarization angle, $\eta$ is the wave impedance, and:

$$
\mathbf{k}^i = k_0(\sin\theta_i\cos\phi_i\,\hat{\mathbf{x}} + \sin\theta_i\sin\phi_i\,\hat{\mathbf{y}} + \cos\theta_i\,\hat{\mathbf{z}})
\tag{2.3}
$$

From §1.3.3, the **Electric Field Integral Equation (EFIE)** on the PEC surface is:

$$
\bigl[\mathbf{E}^i + \eta\,\mathcal{L}(\mathbf{J})\bigr]_{\text{tan}} = 0
\tag{2.4}
$$

and the **Magnetic Field Integral Equation (MFIE)**:

$$
\mathbf{J} - \hat{\mathbf{n}} \times \mathcal{K}(\mathbf{J}) = \hat{\mathbf{n}} \times \mathbf{H}^i
\tag{2.5}
$$

### 2.1.2 Discretization in MoM

A general integral equation can be written as:

$$
\mathcal{L}f = g
\tag{2.6}
$$

Expand $f$ in basis functions $\{f_j\}$:

$$
f \approx \sum_{j=1}^N a_j f_j
\tag{2.7}
$$

Substitute into (2.6) and test with $\{\omega_i\}$:

$$
\sum_{j=1}^N a_j \langle \omega_i, \mathcal{L}f_j \rangle = \langle \omega_i, g \rangle, \quad i=1,\dots,N
\tag{2.8-2.9}
$$

In matrix form:

$$
[\,\mathbf{A}\,]\,\{\mathbf{a}\} = \{\mathbf{g}\}
\tag{2.10}
$$

where:

$$
\{\mathbf{g}\} = \{\langle\omega_i, g\rangle\}, \quad
[\mathbf{A}] = \{\langle\omega_i, \mathcal{L}f_j\rangle\}
\tag{2.11-2.12}
$$

If $[\mathbf{A}]$ is nonsingular:

$$
\{\mathbf{a}\} = [\mathbf{A}]^{-1}\{\mathbf{g}\}
\tag{2.13}
$$

### 2.1.3 Choice of Basis and Testing Functions

The choice of basis and testing functions is **the most critical** decision in MoM. The key requirements:

1. **Accurately represent the unknown** — physical behavior of current on the geometry
2. **Produce well-conditioned matrices** — for stable numerical solution
3. **Computational efficiency** — minimize the cost of filling and solving the matrix

#### Types of Basis Functions

| Type | Support | Example | Application |
|------|---------|---------|-------------|
| Sub-domain | Small patches | RWG, rooftop | 3D/2D general geometries |
| Entire-domain | Whole object | Fourier series | Canonical shapes (sphere, cylinder) |
| Mixed | Partial or complete | Edge elements | Waveguides, cavities |

#### RWG Basis Functions (Most Common for 3D PEC)

The Rao-Wilton-Glisson (RWG) basis function [3] is defined on a pair of adjacent triangles sharing a common edge:

$$
\mathbf{f}_n(\mathbf{r}) = 
\begin{cases}
\dfrac{l_n}{2A_n^+}\,\boldsymbol{\rho}_n^+(\mathbf{r}), & \mathbf{r} \in T_n^+ \\[6pt]
\dfrac{l_n}{2A_n^-}\,\boldsymbol{\rho}_n^-(\mathbf{r}), & \mathbf{r} \in T_n^- \\[6pt]
0, & \text{otherwise}
\end{cases}
\tag{2.14}
$$

where:
- $l_n$ = length of the common edge
- $A_n^\pm$ = area of triangle $T_n^\pm$
- $\boldsymbol{\rho}_n^+(\mathbf{r}) = \mathbf{r} - \mathbf{v}_n^+$ (vector from free vertex to point)
- $\boldsymbol{\rho}_n^-(\mathbf{r}) = \mathbf{v}_n^- - \mathbf{r}$ (vector from point to free vertex)

**Key properties:**
- Normal component across the shared edge is continuous: $\hat{\mathbf{n}}_n^\pm \cdot \mathbf{f}_n = 1$ on the edge
- Divergence is constant: $\nabla_s \cdot \mathbf{f}_n = \pm l_n/A_n^\pm$
- Total charge on the basis function pair is zero (divergence theorem)

#### Testing Functions: Galerkin's Method

Galerkin's method uses the **same functions for testing** as for basis:

$$
\omega_i(\mathbf{r}) = \mathbf{f}_i(\mathbf{r})
\tag{2.15}
$$

This yields a **symmetric** impedance matrix for EFIE (if the Green's function is symmetric), improving conditioning.

For MFIE, a different testing (e.g., pulse testing with $\hat{\mathbf{n}}\times$) is often employed to handle the identity term properly.

### 2.1.4 Discretized Integral Equation (DIE) and Numerical Behavior

#### Discretized EFIE

The surface current is expanded as:

$$
\mathbf{J}(\mathbf{r}) = \sum_{n=1}^N I_n \mathbf{f}_n(\mathbf{r})
\tag{2.16}
$$

Applying Galerkin testing to (2.4):

$$
\sum_{n=1}^N I_n \langle \mathbf{f}_m, \mathcal{L}(\mathbf{f}_n) \rangle = -\frac{1}{\eta}\langle \mathbf{f}_m, \mathbf{E}^i \rangle
\tag{2.17}
$$

The impedance matrix element:

$$
Z_{mn} = \langle \mathbf{f}_m, \mathcal{L}(\mathbf{f}_n) \rangle
= \int_{S_m} \!\int_{S_n} \mathbf{f}_m(\mathbf{r}) \cdot 
\left[ \mathbf{I} + \frac{\nabla\nabla'}{k^2} \right] G(\mathbf{r},\mathbf{r}') \cdot \mathbf{f}_n(\mathbf{r}') \,dS'\,dS
\tag{2.18}
$$

where $G(\mathbf{r},\mathbf{r}') = e^{-jkR}/(4\pi R)$ is the free-space Green's function, $R = |\mathbf{r}-\mathbf{r}'|$.

#### Numerical Behavior of EFIE vs. MFIE

| Property | EFIE | MFIE |
|----------|------|------|
| Operator type | Fredholm 1st kind (compact) | Fredholm 2nd kind |
| Conditioning | Poor at low frequencies | Better conditioned |
| Accuracy | More accurate for smooth surfaces | Less accurate (hypersingular) |
| Resonance | Suffers from interior resonance | Suffers from interior resonance |
| Closed surfaces | Works for open and closed | Only for closed surfaces |
| Memory | Same $O(N^2)$ | Same $O(N^2)$ |

#### Combined Field Integral Equation (CFIE)

To eliminate the interior resonance problem:

$$
\text{CFIE} = \alpha\,\text{EFIE} + (1-\alpha)\,\eta\,\text{MFIE}
\tag{2.19}
$$

where $0 \le \alpha \le 1$ is the combination parameter (typically $\alpha = 0.5$).

### 2.1.5 Handling of Singularity

The MoM matrix elements $Z_{mn}$ involve integrals with the Green's function $G(R) = e^{-jkR}/(4\pi R)$. When the basis and testing triangles overlap or touch ($R \to 0$), the integrand is **singular**.

#### Singularity Extraction

Decompose the Green's function into singular ($1/R$) and regular parts:

$$
\frac{e^{-jkR}}{4\pi R} = \underbrace{\frac{1}{4\pi R}}_{\text{static}} 
- \underbrace{\frac{jk}{4\pi}}_{\text{regular}} 
- \underbrace{\frac{k^2 R}{8\pi}}_{\text{regular}} + \cdots
\tag{2.20}
$$

The $1/R$ singularity is extracted and integrated analytically.

#### Analytical Integration of the Self-Cell ($m=n$)

For the self-interaction term where basis and testing are on the same triangle pair, the singular integral is evaluated analytically. The approach:

1. **Source triangle**: Split the source triangle into three sub-triangles with the observation point as vertex
2. **Analytical formula** [4]: For a triangle with vertices $\mathbf{r}_1, \mathbf{r}_2, \mathbf{r}_3$ and observation point $\mathbf{r}_0$:

$$
I = \int_T \frac{1}{R}\,dS = \sum_{i=1}^3 p_i \ln\frac{R_i^+ + R_i^- + l_i}{R_i^+ + R_i^- - l_i}
\tag{2.21}
$$

where $p_i$ is a geometric factor, $R_i^\pm$ are distances from $\mathbf{r}_0$ to endpoints of the $i$th edge, and $l_i$ is the edge length.

#### Near-Singularity Integration

For $m \ne n$ but triangles close together, a **Duffy transformation** is used to cancel the singularity:

$$
\int_{-1}^1\int_{-1}^1 f(u,v)\,du\,dv = \int_0^1\int_{-1}^1 f(u',v')\,J\,du'\,dv'
\tag{2.22}
$$

The Jacobian $J$ provides a factor that cancels the $1/R$ behavior.

#### Far-Field Approximation

For well-separated basis-testing pairs ($R$ large compared to element size), the integrand is smooth and Gaussian quadrature suffices.

### 2.1.6 Comparison of EFIE and MFIE

**Quantitative comparison:**

For a PEC sphere of radius $a$, the EFIE solution converges faster (fewer unknowns per wavelength) but MFIE produces a better-conditioned matrix.

| Metric | EFIE | MFIE |
|--------|------|------|
| Condition number $\kappa$ | $O(N)$ | $O(1)$ |
| Unknowns/$\lambda^2$ | $\sim$100-200 | $\sim$200-300 |
| RMS error (coarse mesh) | 1-3% | 3-5% |
| Convergence (iterative solver) | Slow | Fast |

### 2.1.7 Interior Resonance Problem

At interior resonant frequencies (where the cavity formed by the PEC surface supports a non-trivial solution to the homogeneous boundary value problem), both EFIE and MFIE have **non-unique solutions**. 

The discrete matrix becomes nearly singular. CFIE (2.19) resolves this by combining the two formulations — the combined operator has no null space for closed PEC surfaces.

### 2.1.8 Fast Multipole Method (FMM)

Direct MoM has $O(N^2)$ complexity for matrix fill and $O(N^3)$ for direct solve (or $O(N_{\text{iter}}N^2)$ for iterative solve). For large $N$ ($>$10,000), this becomes prohibitive.

The **Fast Multipole Method (FMM)** [5] reduces the complexity to $O(N^{1.5})$ for matrix-vector products, enabling iterative solution of large problems.

#### FMM Grouping Strategy

1. **Divide** the computational domain into cubes of size $d$
2. **Group** basis functions into boxes by location
3. **Classify** interactions as:
   - **Near-field**: Adjacent boxes → computed via direct MoM ($O(N)$)
   - **Far-field**: Non-adjacent boxes → accelerated via FMM

#### Multipole Expansion (source-to-multipole)

For $N_s$ sources in box $B$ at positions $\mathbf{r}_i$ with strengths $I_i$:

$$
S(\hat{\mathbf{k}}) = \sum_{i \in B} I_i e^{jk\hat{\mathbf{k}}\cdot\mathbf{r}_i'}
\tag{2.23}
$$

#### Multipole-to-Multipole Translation

Translating a multipole expansion from center $\mathbf{r}_B$ to center $\mathbf{r}_{B'}$:

$$
S'(\hat{\mathbf{k}}) = e^{-jk\hat{\mathbf{k}}\cdot\mathbf{r}_{B\to B'}} S(\hat{\mathbf{k}})
\tag{2.24}
$$

where $\mathbf{r}_{B\to B'} = \mathbf{r}_{B'} - \mathbf{r}_B$.

#### Multipole-to-Local Translation

Convert multipole expansion at $\mathbf{r}_{B'}$ to local expansion at observation box center $\mathbf{r}_C$:

$$
L(\hat{\mathbf{k}}) = \sum_{l=0}^L (-j)^l (2l+1) h_l^{(2)}(k r_{B'C}) P_l(\hat{\mathbf{k}}\cdot\hat{\mathbf{r}}_{B'C}) S(\hat{\mathbf{k}})
\tag{2.25}
$$

where $h_l^{(2)}$ is the spherical Hankel function of the second kind and $P_l$ is the Legendre polynomial.

#### Local-to-Observation (local-to-field)

For an observation point $\mathbf{r}$ in box $C$:

$$
E_{\text{far}}(\mathbf{r}) = \frac{jk\eta}{4\pi} \int L(\hat{\mathbf{k}})\, e^{-jk\hat{\mathbf{k}}\cdot(\mathbf{r}-\mathbf{r}_C)}\, d^2\hat{\mathbf{k}}
\tag{2.26}
$$

#### FMM Algorithm Summary

```
1. Build octree structure for all unknowns
2. For each box, compute multipole expansion from sources
3. Upward pass: aggregate multipoles from children to parents
4. Downward pass: translate multipoles to local expansions
5. Evaluate far-field contribution at each observation point
6. Add near-field contribution directly
```

### 2.1.9 Calculation of Scattered Fields

Once the surface current $\mathbf{J}$ is obtained, the far-field scattered field is calculated using the **physical optics approximation for the far zone**:

$$
\mathbf{E}^s(\mathbf{r}) = -jk\eta\,\frac{e^{-jkr}}{4\pi r}\,
(\mathbf{I} - \hat{\mathbf{r}}\hat{\mathbf{r}}) \cdot 
\int_S \mathbf{J}(\mathbf{r}') e^{jk\hat{\mathbf{r}}\cdot\mathbf{r}'}\,dS'
\tag{2.27}
$$

The radar cross-section (RCS) is:

$$
\sigma = \lim_{r\to\infty} 4\pi r^2 \frac{|\mathbf{E}^s|^2}{|\mathbf{E}^i|^2}
\tag{2.28}
$$

### 2.1.10 Writing Computer Programs

The book provides a detailed step-by-step guide for writing a MoM code for 3D PEC scattering. The key stages:

1. **Mesh input**: Read triangular mesh (nodes, elements, edges), detect boundary edges
2. **RWG basis construction**: Assign basis function to each interior edge
3. **Matrix filling**: Loop over all basis-testing pairs, compute $Z_{mn}$
4. **RHS computation**: Calculate excitation vector $\mathbf{g}$ from incident plane wave
5. **Matrix solve**: Use LU decomposition (small $N$) or iterative solver (large $N$)
6. **Current recovery**: Obtain surface current coefficients $I_n$
7. **RCS calculation**: Compute monostatic or bistatic RCS

#### Computational Cost

| Step | Operation | Complexity |
|------|-----------|:----------:|
| Fill $Z_{mn}$ (near) | $O(N_{\text{near}}^2)$ | $O(N^2)$ |
| Fill $Z_{mn}$ (far via FMM) | $O(N)$ | $O(N)$ |
| LU solve | $O(N^3)$ | $O(N^3)$ |
| Iterative solve (per iter) | $O(N^2)$ or $O(N\log N)$ | $O(N_{\text{iter}}N^2)$ |
| RCS computation | $O(N)$ | $O(N)$ |

### 2.1.11 Numerical Examples

The book presents numerical validation using canonical targets:

1. **PEC sphere** (Mie series reference): Monostatic RCS vs. $\theta$ at $ka = 1, 3, 5$
2. **PEC cube**: Bistatic RCS validation
3. **NASA almond**: Benchmark geometry for RCS validation
4. **Generic aircraft model**: Large-scale demonstration

**Key observations:**
- RWG basis with $N \approx 100\text{--}200$ per $\lambda^2$ gives 1-3% RMS error in RCS
- EFIE more accurate than MFIE for smooth surfaces
- CFIE eliminates interior resonance artifacts
- MLFMA enables problems with $N > 10^6$ unknowns

### 2.1.12 Parallel Technology

#### Parallel Filling of the Impedance Matrix

The MoM matrix filling is **embarrassingly parallel**:
- Each $Z_{mn}$ is independent
- Distribute rows/columns across processors
- Near-linear speedup observed

#### Parallel Iterative Solver

- **Distributed matrix-vector product**: Each processor holds a block of rows
- **All-reduce operation** for vector updates
- **Preconditioner**: Block Jacobi or additive Schwarz
- **Communication pattern**: Nearest-neighbor for FMM, global reduction for inner products

### 2.1.13 Strong Scalability

**Strong scaling** — fixed problem size, increasing processors:

$$
S_p = \frac{T_1}{T_p}
\tag{2.29}
$$

Ideal: $S_p = p$. For MoM, the communication overhead in FMM limits strong scalability.

**Amdahl's Law:**

$$
S_p = \frac{1}{(1-f) + f/p}
\tag{2.30}
$$

where $f$ is the fraction of code that is parallelizable. For MoM matrix fill, $f \approx 0.99$, giving significant but not perfect speedup.

### 2.1.14 Weak Scalability

**Weak scaling** — fixed problem size per processor, increasing total size:

- Maintain constant local work while increasing global problem
- Measure efficiency: $E_p = T_1/T_p$
- For FMM, the communication volume grows slowly with $p$, yielding good weak scaling

**Gustafson's Law:**

$$
S_p = (1-f) + f\,p
\tag{2.31}
$$

---

## 2.2 Scattering from 3D Homogeneous Dielectric Objects

### 2.2.1 Mathematical Formulation

For a homogeneous dielectric object with permittivity $\varepsilon_r$, two equivalent formulations:

#### Volume Equivalence Principle (VEP)

Replace the dielectric with an equivalent volume polarization current:

$$
\mathbf{J}_v(\mathbf{r}) = j\omega(\varepsilon - \varepsilon_0)\mathbf{E}(\mathbf{r})
\tag{2.32}
$$

This leads to a **Volume Integral Equation (VIE)**.

#### Surface Equivalence Principle (PMCHWT Formulation)

Use equivalent surface currents on both sides of the dielectric boundary:

- **Outside** ($S^+$): $(\mathbf{J}_s, \mathbf{M}_s)$ in free space
- **Inside** ($S^-$): $(-\mathbf{J}_s, -\mathbf{M}_s)$ in the dielectric

The Poggio-Miller-Chang-Harrington-Wu-Tsai (PMCHWT) formulation:

$$
\begin{aligned}
&\bigl[\eta_0 \mathcal{L}_0(\mathbf{J}_s) + \mathcal{K}_0(\mathbf{M}_s)\bigr]_{\text{tan}} + 
\bigl[\eta_d \mathcal{L}_d(-\mathbf{J}_s) + \mathcal{K}_d(-\mathbf{M}_s)\bigr]_{\text{tan}} = -\mathbf{E}^i_{\text{tan}} \\
&\bigl[\frac{1}{\eta_0}\mathcal{L}_0(\mathbf{M}_s) - \mathcal{K}_0(\mathbf{J}_s)\bigr]_{\text{tan}} + 
\bigl[\frac{1}{\eta_d}\mathcal{L}_d(-\mathbf{M}_s) - \mathcal{K}_d(-\mathbf{J}_s)\bigr]_{\text{tan}} = -\mathbf{H}^i_{\text{tan}}
\end{aligned}
\tag{2.33}
$$

### 2.2.2 Discretized Forms and Numerical Performance

The PMCHWT formulation requires both RWG basis functions for $\mathbf{J}_s$ and $\mathbf{M}_s$ on the same surface mesh.

**Key characteristics:**
- **Well-conditioned** compared to single-equation formulations
- **No interior resonance problem**
- **Matrix size**: $2N \times 2N$ for $N$ edges (J + M unknowns)
- **Higher memory** than PEC case due to four matrix blocks

#### Numerical Performance

| Formulation | Condition $\kappa$ | Iterations | Accuracy |
|-------------|:------------------:|:----------:|:--------:|
| PMCHWT | $\sim$10-30 | Fast | Excellent |
| EFIE-only (dielectric) | $\sim$100-1000 | Moderate | Depends on contrast |
| Müller | $\sim$1-5 | Very fast | Good (low contrast) |
| Single-source (N-Müller) | $\sim$1-10 | Fast | Good |

### 2.2.3 Numerical Examples

- **Dielectric sphere**: RCS vs. Mie series for $\varepsilon_r = 2, 4, 8$
- **Dielectric cube**: Validation against VIE solutions
- **Coated PEC sphere**: Combined surface and volume discretization

### 2.2.4 Implementation of Single Integral Equation and Numerical Characteristics

The **single integral equation** (SIE) formulation reduces the number of unknowns by using only $\mathbf{J}_s$ (or a linear combination) on the surface. The N-Müller formulation:

$$
(\mathcal{L}_0 + \mathcal{L}_d)(\mathbf{J}_s) = \text{known RHS}
\tag{2.34}
$$

This reduces the matrix size to $N \times N$ but with more complicated Green's function evaluations.

---

## 2.3 Scattering from 3D Inhomogeneous Dielectric Objects

### 2.3.1 Mathematical Formulation

For inhomogeneous dielectric objects ($\varepsilon(\mathbf{r})$ varies within the volume), the **Volume Integral Equation (VIE)** is used:

$$
\frac{\mathbf{D}(\mathbf{r})}{\varepsilon(\mathbf{r})} + \frac{k_0^2}{\varepsilon_0}\int_V \overline{\mathbf{G}}(\mathbf{r},\mathbf{r}') \cdot [\varepsilon(\mathbf{r}') - \varepsilon_0]\mathbf{E}(\mathbf{r}')\,dV' = \mathbf{E}^i(\mathbf{r})
\tag{2.35}
$$

In terms of the electric flux density $\mathbf{D}$ and the contrast function:

$$
\chi(\mathbf{r}) = \frac{\varepsilon(\mathbf{r}) - \varepsilon_0}{\varepsilon(\mathbf{r})}
\tag{2.36}
$$

### 2.3.2 Rooftop Basis Functions

For volume discretization, the **rooftop basis function** is used:

$$
\mathbf{b}_n(\mathbf{r}) = 
\begin{cases}
\dfrac{x - x_{n-1}}{\Delta x}\,\hat{\mathbf{x}}, & x \in [x_{n-1}, x_n] \\[6pt]
\dfrac{x_{n+1} - x}{\Delta x}\,\hat{\mathbf{x}}, & x \in [x_n, x_{n+1}] \\[6pt]
0, & \text{otherwise}
\end{cases}
\tag{2.37}
$$

(similar for $y$ and $z$ components)

These are 3D extensions of the 2D rooftop basis, ensuring continuity of the normal component across cell faces.

### 2.3.3 Discretization of the VIE

Using SWG (Schaubert-Wilton-Glisson) basis functions [6] — the volume analog of RWG:

- Tetrahedral mesh of the volume
- Each SWG basis is defined on a tetrahedron pair sharing a common face
- Normal component is continuous across the face
- Divergence is constant within each tetrahedron

The matrix equation becomes:

$$
[\mathbf{A}]\,\{\mathbf{d}\} = \{\mathbf{e}^i\}
\tag{2.38}
$$

where $\mathbf{d}$ are the expansion coefficients for $\mathbf{D}$.

### 2.3.4 Singularity Processing

The VIE has a **weaker singularity** ($1/R^2$) compared to the surface EFIE ($1/R$). Treatment:

1. **Extract the principal value** using analytical integration
2. **Duffy transformation** for near-singular integrals
3. **Source point treatment** for the self-term

### 2.3.5 Fast Solution of the Discretized VIE

The VIE matrix is typically solved iteratively using:

1. **Conjugate Gradient (CG)** or **GMRES** for non-symmetric systems
2. **Preconditioner**: Diagonal (Jacobi) or block-diagonal
3. **Matrix-vector acceleration**: FMM or FFT-based methods

### 2.3.6 Numerical Examples

- **Inhomogeneous dielectric sphere**: Layered permittivity profile
- **Dielectric lens**: Focusing and scattering characteristics
- **Biological tissue**: Human head model for SAR calculation

---

## 2.4 Essential Points in MoM for Solving Other Problems

### 2.4.1 Scattering from 2D Objects (TM$_z$ and TE$_z$)

For 2D problems (objects uniform in $z$), the MoM is simplified:

#### TM$_z$ Polarization

The EFIE reduces to a scalar integral equation:

$$
E_z^i(\boldsymbol{\rho}) = \frac{k\eta}{4}\int_C J_z(\boldsymbol{\rho}') H_0^{(2)}(k|\boldsymbol{\rho}-\boldsymbol{\rho}'|)\,dl'
\tag{2.39}
$$

where $H_0^{(2)}$ is the Hankel function of the second kind.

Basis: **Pulse basis functions** on line segments.
Testing: **Point matching** (collocation).

#### TE$_z$ Polarization

The MFIE for TE$_z$:

$$
J_\rho(\boldsymbol{\rho}) - \frac{jk}{2}\int_C J_\rho(\boldsymbol{\rho}')\cos\phi'\,H_1^{(2)}(k|\boldsymbol{\rho}-\boldsymbol{\rho}'|)\,dl' = H_z^i(\boldsymbol{\rho})
\tag{2.40}
$$

### 2.4.2 Scattering from Periodic Structures

For **Frequency Selective Surfaces (FSS)** and **metamaterials**:

- Unit cell with periodic boundary conditions
- **Floquet's theorem**:
  
  $$
  \mathbf{J}(\boldsymbol{\rho} + \mathbf{p}) = \mathbf{J}(\boldsymbol{\rho})\,e^{-j\mathbf{k}_t\cdot\mathbf{p}}
  \tag{2.41}
  $$

- **Periodic Green's function**: Sum over Floquet modes

  $$
  G_P(\mathbf{r},\mathbf{r}') = \frac{1}{2D_x D_y}\sum_{m=-\infty}^\infty\sum_{n=-\infty}^\infty
  \frac{e^{-j\mathbf{k}_{mn}\cdot(\boldsymbol{\rho}-\boldsymbol{\rho}')}}{jk_{z,mn}}
  \tag{2.42}
  $$

### 2.4.3 Scattering from 2.5D Objects (Body of Revolution)

For axially symmetric objects (BOR), the azimuthal dependence is expanded in Fourier modes:

$$
\mathbf{J}(\mathbf{r}) = \sum_{m=-\infty}^\infty \mathbf{J}_m(\rho,z)\,e^{jm\phi}
\tag{2.43}
$$

Each mode $m$ decouples due to orthogonality, reducing a 3D problem to a 2D one.

### 2.4.4 Radiation Problems

For antenna radiation, the MoM formulation is similar to scattering, but:

1. **RHS is a delta-gap or magnetic frill source** at the feed point
2. **Input impedance** is computed from:

   $$
   Z_{\text{in}} = -\frac{1}{I_0^2}\int_{S_{\text{feed}}} \mathbf{J}\cdot\mathbf{E}^i\,dS
   \tag{2.44}
   $$

3. **Far-field pattern** is computed from the surface current

---

## Key Equations Summary

| Eq. | Type | Description |
|:---:|------|-------------|
| (2.1)-(2.2) | Geometry | Incident plane wave |
| (2.4) | IE | EFIE for PEC |
| (2.5) | IE | MFIE for PEC |
| (2.10) | Matrix | MoM system $[\mathbf{A}]\{\mathbf{a}\}=\{\mathbf{g}\}$ |
| (2.14) | Basis | RWG basis functions |
| (2.18) | Matrix | Impedance matrix elements |
| (2.19) | IE | CFIE combination |
| (2.21) | Integral | Analytical singularity treatment |
| (2.23)-(2.26) | Algorithm | Fast Multipole Method |
| (2.27) | Physics | Far-field scattered field |
| (2.33) | IE | PMCHWT for dielectric |
| (2.35) | IE | Volume Integral Equation |
| (2.39)-(2.40) | IE | 2D MoM (TM/TE) |
| (2.41) | BC | Floquet periodicity |
| (2.44) | Physics | Input impedance |

---

## Problems

2.1 Derive the EFIE for a PEC scatterer starting from the equivalence principle and the free-space Green's function.

2.2 Prove that the RWG basis function has continuous normal component across the shared edge and constant divergence.

2.3 Show that the CFIE (2.19) with $\alpha = 0.5$ eliminates the interior resonance problem.

2.4 Derive the translation formula (2.25) for the FMM using the addition theorem for spherical Hankel functions.

2.5 Extend the 3D PMCHWT formulation to the case of a multi-layer dielectric object.

2.6 Prove the orthogonality of Fourier modes in (2.43) for BOR problems.

2.7 Compare the computational complexity of direct MoM, FMM-accelerated MoM, and MLFMA for a problem with $N = 10^5$ unknowns.

---

## References

1. Peterson, A.F., Ray, S.L., and Mittra, R. (1998) *Computational Methods for Electromagnetics*, IEEE Press, New York.
2. Harrington, R.F. (1968) *Field Computation by Moment Methods*, Macmillan, New York.
3. Rao, S.M., Wilton, D.R., and Glisson, A.W. (1982) "Electromagnetic scattering by surfaces of arbitrary shape." *IEEE Trans. AP*, 30(3), 409–418.
4. Wilton, D.R., Rao, S.M., Glisson, A.W., et al. (1984) "Potential integrals for uniform and linear source distributions on polygonal and polyhedral domains." *IEEE Trans. AP*, 32(3), 276–281.
5. Coifman, R., Rokhlin, V., and Wandzura, S. (1993) "The fast multipole method for the wave equation." *IEEE Antennas and Propagation Magazine*, 35(3), 7–12.
6. Schaubert, D.H., Wilton, D.R., and Glisson, A.W. (1984) "A tetrahedral modeling method for electromagnetic scattering by arbitrarily shaped inhomogeneous dielectric bodies." *IEEE Trans. AP*, 32(1), 77–85.
7. Sheng, X.Q., Jin, J.M., Song, J., et al. (1998) "On the formulation of hybrid finite-element and boundary-integral methods for 3D scattering." *IEEE Trans. AP*, 46(3), 303–311.
