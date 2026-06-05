---
title: "Ch3: Finite-Element Method"
book: "Sheng & Song, Essentials of Computational Electromagnetics (2012)"
chapter: 3
pages: "159-213"
weight: 3
topics:
  - Variational formulation
  - Edge element basis functions
  - Waveguide eigenvalue problem
  - 3D discontinuous waveguide
  - 3D scattering
  - Node-edge elements
  - Higher-order elements
  - FETD
notes_version: "1.0"
---

# Chapter 3: Finite-Element Method

The finite-element method (FEM) is a full-wave numerical method that discretizes the **variational formulation of a functional**. The evolution of FEM in electromagnetics traces back to solving two types of problems: **eigenmode problems** (waveguide and cavity) and **boundary-value problems** (closed-domain EM problems and open-domain scattering/radiating problems).

## 3.1 Eigenmodes Problems of Dielectric-Loaded Waveguides

### 3.1.1 Functional Formulation

The partial differential equation for the fields in a dielectric-loaded waveguide is (from Section 1.2):

$$
\nabla \times \frac{1}{\mu_r} \nabla \times \mathbf{E} - k_0^2 \epsilon_r \mathbf{E} = 0 \quad \text{in } S \tag{3.1}
$$

with boundary conditions:

$$
\hat{n} \times \mathbf{E} = 0 \quad \text{on } G_1 \text{ (PEC)} \tag{3.2}
$$

$$
\hat{n} \times \nabla \times \mathbf{E} = 0 \quad \text{on } G_2 \text{ (PMC)} \tag{3.3}
$$

where $S$ is the waveguide cross section. The PMC boundary condition exploits field symmetry to reduce the computational domain.

**Derivation of the functional**: Multiplying (3.1) by an infinitesimal arbitrary variation $\delta\mathbf{E}$ and integrating over $S$:

$$
\int_S \left( \nabla \times \frac{1}{\mu_r} \nabla \times \mathbf{E} - k_0^2 \epsilon_r \mathbf{E} \right) \cdot \delta\mathbf{E} \, dS = 0 \tag{3.4}
$$

Applying the boundary condition (3.3) and using **Green's theorem**:

$$
\int_S \left[ u (\nabla \times \mathbf{a}) \cdot (\nabla \times \mathbf{b}) - (\nabla \times u \mathbf{a}) \cdot \mathbf{b} \right] dS = \oint_G u (\mathbf{a} \times \nabla \times \mathbf{b}) \cdot \hat{n} \, d\Gamma \tag{3.7}
$$

the functional becomes:

$$
F(\mathbf{E}) = \frac{1}{2} \int_S \left[ \frac{1}{\mu_r} (\nabla \times \mathbf{E}) \cdot (\nabla \times \mathbf{E}) - k_0^2 \epsilon_r \mathbf{E} \cdot \mathbf{E} \right] dS \tag{3.9}
$$

The variational problem is:

$$
\delta F = 0, \quad \hat{n} \times \mathbf{E} = 0 \text{ on } G_1 \tag{3.10}
$$

**Field decomposition in regular waveguides**: For a regular waveguide infinite along the $z$-axis:

$$
\mathbf{E}(x,y,z) = \mathbf{E}_t(x,y) + \hat{z} E_z(x,y) \, e^{-j\beta z} \tag{3.11}
$$

where $\mathbf{E}_t$ is the transverse component and $\beta$ is the propagation constant.

Applying the transformation $\tilde{E}_x = \beta E_x$, $\tilde{E}_y = \beta E_y$, $\tilde{E}_z = -jE_z$ to (3.9), we obtain the functional in terms of $k_0$ and $\beta$:

$$
F(\mathbf{e}) = \frac{1}{2} \int_S \left\{ \beta^2 \frac{1}{\mu_r} (\mathbf{e}_t + \nabla_t e_z) \cdot (\mathbf{e}_t + \nabla_t e_z) - k_0^2 \left[ \epsilon_r e_z^2 + \frac{1}{\mu_r} \mathbf{e}_t \cdot \mathbf{e}_t \right] \right\} dS \tag{3.15}
$$

### 3.1.2 Choice of Basis Functions

**The spurious solution problem**: Using nodal electric fields (3 values per node) as interpolation parameters enforces both tangential **and** normal continuity of $\mathbf{E}$ across element boundaries — but physically only tangential continuity is required. The spurious (unphysical) solutions originate from this over-constraint.

**Edge-element basis functions**: The solution uses:
- **Longitudinal component** $E_z$: nodal values at the 3 nodes (using area coordinates $L_i$)
- **Transverse component** $\mathbf{E}_t$: tangential components at edge midpoints

**Area coordinates** on a triangular element with nodes labeled anticlockwise (1,2,3):

$$
L_i = \frac{\Delta_i}{\Delta} \quad (i=1,2,3), \quad L_1 + L_2 + L_3 = 1 \tag{3.19}
$$

where $\Delta$ is the element area and $\Delta_i$ are the sub-triangle areas.

**Edge-element basis functions** (Whitney forms):

$$
\mathbf{N}_1 = (L_2 \nabla L_3 - L_3 \nabla L_2) l_1 \tag{3.20}
$$

$$
\mathbf{N}_2 = (L_3 \nabla L_1 - L_1 \nabla L_3) l_2 \tag{3.24}
$$

$$
\mathbf{N}_3 = (L_1 \nabla L_2 - L_2 \nabla L_1) l_3 \tag{3.25}
$$

where $l_i$ is the length of edge $i$, and $\hat{e}_i$ is the unit vector along edge $i$ (pointing from the start node to the end node in the local numbering).

**Key property**: On edge $i$, $\hat{e}_i \cdot \mathbf{N}_j = \delta_{ij}$. On all other edges, $\hat{e}_j \cdot \mathbf{N}_i = 0$.

This enforces only tangential continuity — the correct physical constraint.

**Field interpolation**:

$$
\mathbf{E}_t = \sum_{i=1}^{3} \mathbf{N}_i E_{ti} \tag{3.26}
$$

$$
E_z = \sum_{i=1}^{3} L_i E_{zi} \tag{3.27}
$$

### 3.1.3 Discretization of the Functional

Substituting the expansions into (3.15) yields the discrete functional:

$$
F = \frac{1}{2} \mathbf{e}_t^T \mathbf{A}_{tt} \mathbf{e}_t + \frac{1}{2} \beta^2 \begin{pmatrix} \mathbf{e}_t \\ \mathbf{e}_z \end{pmatrix}^T \begin{pmatrix} \mathbf{B}_{tt} & \mathbf{B}_{tz} \\ \mathbf{B}_{zt} & \mathbf{B}_{zz} \end{pmatrix} \begin{pmatrix} \mathbf{e}_t \\ \mathbf{e}_z \end{pmatrix} \tag{3.30}
$$

where element matrices are:

$$
A^{e}_{tt} = \int_{S_e} \left[ \frac{1}{\mu_r^e} (\nabla_t \times \mathbf{N}^e) \cdot (\nabla_t \times \mathbf{N}^{eT}) - k_0^2 \epsilon_r^e \mathbf{N}^e \cdot \mathbf{N}^{eT} \right] dS \tag{3.31}
$$

$$
B^{e}_{tt} = \frac{1}{\mu_r^e} \int_{S_e} \mathbf{N}^e \cdot \mathbf{N}^{eT} dS \tag{3.32}
$$

$$
B^{e}_{tz} = \frac{1}{\mu_r^e} \int_{S_e} \mathbf{N}^e \cdot \nabla_t L^e dS \tag{3.33}
$$

$$
B^{e}_{zz} = \int_{S_e} \left[ \frac{1}{\mu_r^e} (\nabla_t L^e) \cdot (\nabla_t L^{eT}) - k_0^2 \epsilon_r^e L^e \cdot L^{eT} \right] dS \tag{3.35}
$$

For constant $\epsilon_r^e$, $\mu_r^e$ inside each element, the integrals have closed forms using the area coordinate integration formula:

$$
\int_{\Delta} L_1^k L_2^l L_3^m d\Omega = \frac{k! \, l! \, m!}{(k+l+m+2)!} \, 2\Delta \tag{3.36}
$$

**Explicit forms** (where $[T]$, $[R]$, $[U]$, $[P]$, $[Q]$ are $3\times 3$ matrices per element):

$$
A^{e}_{tt} = \frac{1}{\mu_r^e} [T]^e - k_0^2 \epsilon_r^e [R]^e \tag{3.37}
$$

$$
B^{e}_{tt} = \frac{1}{\mu_r^e} [R]^e \tag{3.38}
$$

$$
B^{e}_{tz} = \frac{1}{\mu_r^e} [U]^e \tag{3.39}
$$

$$
B^{e}_{zz} = \frac{1}{\mu_r^e} [P]^e - k_0^2 \epsilon_r^e [Q]^e \tag{3.40}
$$

The labels for edges and nodes follow the convention in Table 3.1.

| $i$ | $i_1$ | $i_2$ |
|-----|-------|-------|
| 1   | 2     | 3     |
| 2   | 3     | 1     |
| 3   | 1     | 2     |

**Table 3.1**: Edge labeling convention in triangular element.

Applying the variational principle ($\delta F = 0$) yields the **generalized eigenvalue equation**:

$$
\begin{pmatrix} \mathbf{A}_{tt} & 0 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} \mathbf{e}_t \\ \mathbf{e}_z \end{pmatrix} = \beta^2 \begin{pmatrix} \mathbf{B}_{tt} & \mathbf{B}_{tz} \\ \mathbf{B}_{zt} & \mathbf{B}_{zz} \end{pmatrix} \begin{pmatrix} \mathbf{e}_t \\ \mathbf{e}_z \end{pmatrix} \tag{3.49}
$$

### 3.1.4 Imposition of the Boundary Condition

For PEC boundary ($G_1$), $\hat{n} \times \mathbf{E} = 0$ on the boundary edges. The procedure:
1. Relabel unknowns so boundary unknowns are last
2. Set the coefficient row for boundary unknowns to $[1, 0, \ldots, 0]$ (for zero Dirichlet)
3. Transfer effects symmetrically to column entries
4. Eliminate boundary unknowns from the system

### 3.1.5 Solution of the Generalized Eigenvalue Equation

From (3.49), eliminating $\mathbf{e}_z$ using $\mathbf{B}_{zt} \mathbf{e}_t + \mathbf{B}_{zz} \mathbf{e}_z = 0$ gives:

$$
\mathbf{A}_{tt} \mathbf{e}_t = \beta^2 \mathbf{B}'_{tt} \mathbf{e}_t \tag{3.51}
$$

where $\mathbf{B}'_{tt} = \mathbf{B}_{tz} \mathbf{B}_{zz}^{-1} \mathbf{B}_{zt} + \mathbf{B}_{tt}$.

A more stable form uses the transformation:

$$
\begin{pmatrix} \mathbf{B}_{tt} & \mathbf{B}_{tz} \\ \mathbf{B}_{zt} & \mathbf{B}_{zz} \end{pmatrix} \rightarrow \begin{pmatrix} \mathbf{B}_{tt} + \frac{1}{\gamma^2}\mathbf{A}_{tt} & \mathbf{B}_{tz} \\ \mathbf{B}_{zt} & \mathbf{B}_{zz} \end{pmatrix} \tag{3.53}
$$

where $\gamma^2 = k_0^2 \epsilon_{\max} \mu_{\max}$ is the TEM wave propagation constant in the highest-permittivity material.

Standard eigenvalue solvers (EISPACK, ARPACK, MATLAB's `eigs`) can be applied to the resulting sparse symmetric matrices.

### 3.1.6 Computer Programming

The 1D row-indexed sparse storage scheme stores only non-zero entries:
- Arrays `sa` and `ija`: `sa` stores values, `ija` stores column indices
- Diagonal entries stored in first $N$ positions
- Non-zero off-diagonal entries stored in ascending column order

**Module structure**: mesh information → matrix assembly → boundary condition → eigenvalue solution

**Matrix entry formulas for the $3\times 3$ element matrices** (using node coordinates):

$$
T_{ij} = 4\Delta \, l_i l_j \, \mathbf{r}_{i_1 i_2} \cdot \mathbf{r}_{j_1 j_2} \tag{3.41}
$$

$$
R_{ij} = \Delta \, l_i l_j \left[ (1+\delta_{i_1 j_1})\xi_{i_1 j_1} - (1+\delta_{i_1 j_2})\xi_{i_2 j_1} - (1+\delta_{i_2 j_1})\xi_{i_1 j_2} + (1+\delta_{i_2 j_2})\xi_{i_2 j_2} \right] \tag{3.42}
$$

$$
U_{ij} = l_i \Delta \left( \xi_{i_2 j} - \xi_{i_1 j} \right) \tag{3.43}
$$

$$
P_{ij} = \Delta \, \xi_{ij} \tag{3.44}
$$

$$
Q_{ij} = \frac{1+\delta_{ij}}{12} \Delta \tag{3.45}
$$

where $\xi_{ij} = \mathbf{r}_{L_i} \cdot \mathbf{r}_{L_j}$ and $\mathbf{r}_{L_i} = \nabla L_i$.

---

## 3.2 Three-Dimensional Discontinuous Waveguide Problem

The discontinuity problem involves joining two waveguides with different cross sections or media. The solution uses the **penalty function method** to enforce continuity of the tangential electric and magnetic fields at the discontinuity plane.

The functional formulation includes both waveguide sections connected through a surface integral representing the discontinuity:

$$
F = \frac{1}{2} \sum_{m=1}^{2} \int_{S^{(m)}} \left[ \frac{1}{\mu_r} (\nabla \times \mathbf{E}^{(m)}) \cdot (\nabla \times \mathbf{E}^{(m)*}) - k_0^2 \epsilon_r \mathbf{E}^{(m)} \cdot \mathbf{E}^{(m)*} \right] dS + \text{discontinuity terms}
$$

---

## 3.3 Three-Dimensional Scattering Problem

For the 3D scattering problem (open domain), the FEM domain must be truncated. Two approaches:

1. **Global boundary condition (radiation condition)**: More accurate but results in full matrix
2. **PML (Perfectly Matched Layer)**: lossy material that attenuates waves; leads to sparse matrices

The functional for 3D scattering:

$$
F(\mathbf{E}) = \frac{1}{2} \int_V \left[ \frac{1}{\mu_r} (\nabla \times \mathbf{E}) \cdot (\nabla \times \mathbf{E}^*) - k_0^2 \epsilon_r \mathbf{E} \cdot \mathbf{E}^* \right] dV + \text{PML boundary terms}
$$

---

## 3.4 Node-Edge Elements

Standard Whitney edge elements have 6 DOFs per tetrahedron. The **node-edge element** improves performance by adding specially constructed node-based functions that enhance convergence while maintaining the edge-element sparsity pattern.

---

## 3.5 Higher-Order Elements

Using higher-order basis functions (hierarchical vector basis functions on triangles/tetrahedra) improves accuracy per DOF compared to linear edge elements. These are particularly useful for problems with smooth field variations.

---

## 3.6 FETD (Finite Element Time Domain)

FETD solves time-domain Maxwell's equations using FEM spatial discretization combined with **Newmark-beta** or similar time-integration schemes. Advantages over FDTD:
- Unstructured meshes for complex geometry
- Higher-order spatial accuracy
- Easy handling of anisotropic materials

The system results in a matrix ODE:

$$
\mathbf{M} \frac{d^2 \mathbf{u}}{dt^2} + \mathbf{K} \mathbf{u} = 0
$$

---

## Key Equations Summary

| Equation | Physical Meaning |
|----------|-----------------|
| (3.1) | PDE for waveguide fields |
| (3.9) | Variational functional for eigenmode problem |
| (3.15) | Functional in terms of $k_0$ and $\beta$ |
| (3.20) | Edge-element basis function $\mathbf{N}_1$ |
| (3.30) | Discrete functional matrix form |
| (3.49) | Generalized eigenvalue equation |
| (3.51) | Reduced eigenvalue equation after eliminating $e_z$ |
| (3.36) | Area coordinate integration formula |

---

## Problems

**3.1** Prove that (3.10) is equivalent to (3.1) and (3.3) by showing the vanishing variation of $F$.

**3.2** Derive the functional for the second-order scalar PDE with mixed boundary conditions.

**3.3** Derive the functional for the vector wave equation with inhomogeneous boundary conditions for magnetic field $\mathbf{H}$.

**3.4** Apply the modified variational principle for inhomogeneous boundary conditions $f = p$ on $S_1$.

**3.5** Derive the functional for the vector wave equation with inhomogeneous boundary conditions.

**3.6** Prove $\mathbf{N}_i \times \hat{n} = g_i$ (equivalence between edge-element and RWG basis functions).

**3.7** Write a program for generating element matrices analytically and by Gauss-Legendre quadrature.

---

## References

[1] Jin, J.M. (2010) The Finite Element Method in Electromagnetics, 2nd edn, Wiley, New York.
[2] Silvester, P.P. and Ferrari, R.L. (1996) Finite Elements for Electrical Engineers, 3rd edn, Cambridge University Press.
[3] Harrington, R.F. (1968) Field Computation by Moment Methods, Macmillan, New York.
[4] Berk, A. (1956) On the Fourier expansion of discontinuously adherent waveguides. IRE Transactions on Antennas and Propagation, 4, 113–119.
[5] Li, W. and Chen, Q. (1991) Variational principle for waveguide with arbitrary cross section. Science in China, 34, 1262–1270.
[6] Kishk, A.A. and Shafai, L. (1986) Potential formulation for waveguide eigenproblems. IEE Proceedings, 133, 135–140.
[7] Lee, J.F. (1994) WETD — A novel finite element time-domain approach. Microwave and Optical Technology Letters, 7, 266–269.
[8] Lee, J.F. and Sacks, Z. (1995) Whitney elements time domain (WETD) methods. IEEE Transactions on Magnetics, 31, 1325–1329.
[9] Golub, G.H. and Van Loan, C.F. (1996) Matrix Computations, 3rd edn, Johns Hopkins University Press.