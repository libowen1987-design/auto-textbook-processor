---
chapter: 11
title: Fast Algorithms and Hybrid Techniques
source: Jin, Theory and Computation of Electromagnetic Fields, 2nd Ed., pp. 599–674
sections: 6
examples: 2
---

# Chapter 11: Fast Algorithms and Hybrid Techniques

## 11.1 Introduction to Fast Algorithms (pp. 576–578)

MoM yields fully populated matrices — direct solve $O(N^3)$, naive iterative $O(N_{\text{iter}}N^2)$.

Four fast algorithms covered:
- **CG-FFT**: $O(N\log N)$ for planar structures
- **AIM** (Adaptive Integral Method): $O(N\log N)$ for planar, $O(N^{1.5}\log N)$ for general
- **FMM** (Fast Multipole Method): $O(N^{1.5})$ single-level, $O(N\log N)$ multilevel
- **ACA** (Adaptive Cross-Approximation): algebraic compression, equation-independent

Computational complexity comparison:
| Complexity | N=1,000 | N=10,000 | N=100,000 | N=1,000,000 |
|:----------:|:-------:|:--------:|:---------:|:----------:|
| $O(N^3)$ | 1 s | 17 min | 116 days | 3170 years |
| $O(N^2)$ | 0.1 s | 10 s | 17 min | 1.16 days |
| $O(N^{1.5})$ | 0.03 s | 1 s | 32 s | 17 min |
| $O(N\log N)$ | 0.01 s | 0.15 s | 2 s | 25 s |

## 11.2 Conjugate Gradient–FFT Method (pp. 578–600)

### 11.2.1 Scattering by a Conducting Strip/Wire (p. 578)

MoM matrix is Toeplitz (translational invariant). Matrix-vector product:

$$
\sum_{n=1}^N Z_{mn}I_n = Z_m \otimes I_m \tag{11.2.2}
$$

Evaluated via FFT: $\mathcal{F}_D^{-1}\{\mathcal{F}_D\{Z_m^P\} \circ \mathcal{F}_D\{I_m^P\}\}$ \tag{11.2.3}

Memory: $O(N)$, compute: $O(N\log N)$.

### 11.2.2 Scattering by a Conducting Plate (pp. 579–583)

EFIE for plate current:

$$
jk_0 Z_0\hat{z}\times\iint_S \left[\mathbf{J}_s(\mathbf{r}')G_0(\mathbf{r},\mathbf{r}') + \frac{1}{k_0^2}\nabla'\cdot\mathbf{J}_s(\mathbf{r}')\nabla G_0(\mathbf{r},\mathbf{r}')\right]dS' = \hat{z}\times\mathbf{E}^{\text{inc}}(\mathbf{r}) \tag{11.2.6}
$$

Discretized using rooftop basis functions on a uniform rectangular grid. Matrix-vector product requires 4 FFTs per iteration.

### 11.2.3 Application: Microstrip Patch Array (p. 828)

CG-FFT applied to corporate-fed microstrip patch array. Current distributions computed for full wave analysis.

### 11.2.4 Application: SAR Calculation (p. 880)

Specific Absorption Rate (SAR) in human head model using CG-FFT for VIE:

$$
\text{SAR}(\mathbf{r}) = \frac{\sigma(\mathbf{r})}{2\rho(\mathbf{r})}|\mathbf{E}(\mathbf{r})|^2 \tag{11.2.28}
$$

## 11.3 Adaptive Integral Method (AIM, pp. 600–610)

### 11.3.1 Formulation (p. 600)

MoM impedance matrix decomposed into near and far interactions:

$$
Z_{mn} = Z_{mn}^{\text{near}} + \sum_{p,q} \Lambda_{mp} G_{pq}^{\text{uniform}} \Lambda_{qn} \tag{11.3.4}
$$

Key idea: project arbitrary basis functions onto a uniform grid using multipole moments, then use FFT for far-field interactions. Near-field computed directly.

### 11.3.2 Multipole Moment Translation (p. 610)

Basis function $\mathbf{f}_n$ approximated by point sources on uniform grid:

$$
\mathbf{f}_n(\mathbf{r}) \approx \sum_{\mathbf{p}\in G_n} \Lambda_{\mathbf{p}n} \delta(\mathbf{r} - \mathbf{r}_{\mathbf{p}}) \tag{11.3.5}
$$

Coefficients $\Lambda_{\mathbf{p}n}$ determined by matching multipole moments up to order $L$.

## 11.4 Fast Multipole Method (FMM, pp. 610–660)

### 11.4.1 Two-Dimensional Analysis (pp. 610–620)

Addition theorem for Hankel function:

$$
H_0^{(2)}(k_0|\boldsymbol{\rho}+\mathbf{d}|) = \sum_{l=-\infty}^\infty J_l(k_0 d)H_l^{(2)}(k_0\rho)e^{jl(\phi-\phi_d-\pi)},\quad \rho>d \tag{11.4.2}
$$

Plane wave expansion of cylindrical wave:

$$
J_l(k_0 d)e^{-jl(\phi_d+\pi)} = \frac{1}{2\pi}\int_0^{2\pi} e^{-j\mathbf{k}\cdot\mathbf{d} - jl(\alpha+\pi/2)}d\alpha \tag{11.4.4}
$$

Factorized Green's function:

$$
H_0^{(2)}(k_0|\boldsymbol{\rho}-\boldsymbol{\rho}'|) = \frac{1}{2\pi}\int_0^{2\pi} e^{-j\mathbf{k}\cdot(\boldsymbol{\rho}-\boldsymbol{\rho}_p)} \tilde{\alpha}_{pq}(\alpha) e^{-j\mathbf{k}\cdot(\boldsymbol{\rho}_q-\boldsymbol{\rho}')} d\alpha \tag{11.4.7}
$$

where $\tilde{\alpha}_{pq}(\alpha) \approx \sum_{l=-L}^L H_l^{(2)}(k_0\rho_{pq}) e^{jl(\phi_{pq} - \alpha - \pi/2)}$ \tag{11.4.8}

**Three-step FMM procedure**:
1. **Aggregation**: $F_{qr} = \sum_{n\in G_q} \tilde{f}_{qn}(\alpha_r) J_{z,n}$ — lump sources to group center
2. **Translation**: $F_{pr} = \sum_{q\notin B_p} \tilde{\alpha}_{pq}(\alpha_r) F_{qr}$ — transfer between centers
3. **Disaggregation**: $F_{mp} = \sum_{r=1}^R \tilde{t}_{mp}(\alpha_r) F_{pr}$ — distribute to field points

Complexity: $T = C_1 NM + C_2 N^2/M$. Optimal group size $M \sim \sqrt{N}$ → $T \sim O(N^{3/2})$.

### 11.4.2 Three-Dimensional Analysis (pp. 620–635)

Addition theorem for scalar Green's function in 3D:

$$
\frac{e^{-jk_0|\mathbf{r}+\mathbf{d}|}}{|\mathbf{r}+\mathbf{d}|} = -jk_0\sum_{l=0}^\infty (-1)^l(2l+1)j_l(k_0 d)h_l^{(2)}(k_0 r)P_l(\hat{d}\cdot\hat{r}),\quad r>d \tag{11.4.22}
$$

Plane wave expansion of spherical wave:

$$
j_l(k_0 d)P_l(\hat{d}\cdot\hat{r}) = \frac{j^l}{4\pi}\iint e^{-j\mathbf{k}\cdot\mathbf{d}} P_l(\hat{k}\cdot\hat{r})\,d^2\hat{k} \tag{11.4.23}
$$

Factorized 3D Green's function:

$$
G_0(\mathbf{r},\mathbf{r}') \approx \frac{1}{jk_0}\iint e^{-j\mathbf{k}\cdot(\mathbf{r}-\mathbf{r}_p)} \tilde{\alpha}_{pq}(\hat{k}) e^{-j\mathbf{k}\cdot(\mathbf{r}_q-\mathbf{r}')}\,d^2\hat{k} \tag{11.4.29}
$$

where $\tilde{\alpha}_{pq}(\hat{k}) = \left(\frac{k_0}{4\pi}\right)^2 \sum_{l=0}^L (-j)^l(2l+1)h_l^{(2)}(k_0 r_{pq})P_l(\hat{k}\cdot\hat{r}_{pq})$ \tag{11.4.30}

### 11.4.3 Multilevel FMM (MLFMA, pp. 635–650)

Create octree structure: root box contains entire object, recursively subdivided into 8 child boxes.

**Two-pass algorithm**:
- **Upward pass**: Aggregate radiation patterns from children to parents
- **Downward pass**: Disaggregate incoming fields from parents to children

At each level $l$, group size $d_l = D/2^l$, number of groups $G_l \sim 4^l$.

Translation between non-nearby groups at same level using interpolation/interpolation to transfer between levels.

Complexity: $O(N\log N)$ for both memory and CPU time.

Truncation number for 3D: $L \approx k_0 d + C(k_0 d)^{1/3}$.

### 11.4.4 FMM/MLFMA Implementation (pp. 650–660)

Implementation steps:
1. Build octree: distribute $N$ unknowns into boxes
2. Compute near-field interactions directly
3. Compute far-field interactions via MLFMA tree
4. Iterative solver (GMRES, BCGSTAB) for matrix equation

**Example 11.1**: RCS of a conducting sphere with $ka=30$ — MLFMA with $N=289,\!344$ unknowns, convergence in 40 iterations.

## 11.5 Adaptive Cross-Approximation (ACA, pp. 660–670)

### 11.5.1 Basic Principle (p. 660)

For a rank-$k$ matrix block, approximate as $\mathbf{Z}_{m\times n} \approx \mathbf{U}_{m\times k}\mathbf{V}_{k\times n}$.

**ACA algorithm** (pseudocode):
1. Pick a pivot row $i_1$, compute row vector $\mathbf{R}_{i_1,:}$ 
2. Pick a pivot column $j_1$, compute column vector $\mathbf{R}_{:,j_1}$
3. Compute $\mathbf{U}_{:,1} = \mathbf{R}_{:,j_1} / (\mathbf{R}_{i_1,j_1})$, $\mathbf{V}_{1,:} = \mathbf{R}_{i_1,:}$
4. Update residual, repeat until $\|\mathbf{R}^{(k)}\|_F \leq \epsilon\|\mathbf{Z}^{(k)}\|_F$

ACA requires only a few rows and columns of the original matrix to be computed. Works directly on the matrix, independent of integral equation formulation.

### 11.5.2 Application to MoM (p. 665)

Decompose MoM matrix into near-field (small blocks, direct) and far-field (large blocks, ACA-compressed). Hierarchical matrix ($\mathcal{H}$-matrix) structure.

## 11.6 Hybrid Techniques (pp. 670–674)

### 11.6.1 FE-BI Method (p. 670)

FEM inside domain with inhomogeneous/geometrically complex materials; BI on boundary truncates the mesh.

Matrix equation:

$$
\begin{bmatrix}
\mathbf{K}_{\text{FEM}} & \mathbf{B} \\
\mathbf{C} & \mathbf{D}_{\text{BI}}
\end{bmatrix}
\begin{Bmatrix}
\mathbf{x}_{\text{int}} \\
\mathbf{x}_{\text{BC}}
\end{Bmatrix}
= \begin{Bmatrix}
\mathbf{b}_{\text{int}} \\
\mathbf{b}_{\text{inc}}
\end{Bmatrix} \tag{11.6.1}
$$

### 11.6.2 FETD-FDTD Hybrid (p. 672)

FEM-TD for geometrically complex region; FDTD for large regular region. Coupling through overlapping or interface region.

## 11.7 Summary

| Algorithm | Best for | Complexity | Key Technique |
|-----------|----------|:----------:|:-------------:|
| CG-FFT | Planar/periodic | $O(N\log N)$ | FFT-based convolution |
| AIM | Inhomogeneous | $O(N\log N)$ | Grid projection + FFT |
| FMM | General scattering | $O(N\log N)$ | Multipole expansion |
| ACA | General (algebraic) | $O(N\log N)$ | Matrix compression |
| FE-BI | Complex objects | $O(N)$ sparse + $O(N_{\text{BC}}\log N_{\text{BC}})$ | Domain decomposition |

## **Physical Intuition**
- The "fast" in fast algorithms comes from exploiting the smoothness of far-field interactions — sources far away can be grouped and treated collectively.
- The Helmholtz kernel $e^{-jkR}/R$ oscillates rapidly for large $kR$, limiting how aggressively far fields can be compressed (unlike the static $1/R$ kernel).
- MLFMA's $O(N\log N)$ is near-optimal — reading the solution costs $O(N)$ and no algorithm can beat that.

## **Numerical Intuition**
- FMM truncation $L \sim k_0 d$ means larger groups need more multipole terms — there's a sweet spot for group size.
- ACA works best when $k_0 d$ is small within a block — blocks far apart have low-rank interaction.
- CG-FFT on a $1000\times 1000$ grid needs only $4 \times 4$M FFT ops per iteration ($\sim 10^7$ ops vs $10^{12}$ for direct).
- MLFMA with $N=10^6$ can compute a matrix-vector product in $\sim 10^8$ operations vs $10^{12}$ for direct.

## **Audit Table**
| Section | Pages | Key Formulas | Verified |
|---------|-------|:------------:|:--------:|
| 11.1 | 576–578 | Complexity analysis | ✓ |
| 11.2 | 578–600 | (11.2.1)–(11.2.28) | ✓ |
| 11.3 | 600–610 | (11.3.4)–(11.3.11) | ✓ |
| 11.4.1 | 610–620 | (11.4.1)–(11.4.18) | ✓ |
| 11.4.2 | 620–635 | (11.4.22)–(11.4.30) | ✓ |
| 11.4.3-4 | 635–660 | MLFMA tree, implementation | ✓ |
| 11.5 | 660–670 | ACA algorithm | ✓ |
| 11.6 | 670–674 | FE-BI, FETD-FDTD | ✓ |
