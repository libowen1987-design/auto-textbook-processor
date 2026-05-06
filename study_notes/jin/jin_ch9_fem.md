# Chapter 9: The Finite Element Method

**Source:** Jin, *Theory and Computation of Electromagnetic Fields*, 2nd Ed., Chapter 9 (pp. 457–528)

---

## 9.1 Basic Formulation

### 9.1.1 Weighted Residual Method

For a 1D boundary-value problem:
$$
-\frac{d}{dx}\left(p\frac{du}{dx}\right) + qu = f, \quad 0 < x < L
\tag{9.1.1}
$$

The residual is:
$$
r(x) = -\frac{d}{dx}\left(p\frac{du}{dx}\right) + qu - f
$$

Weighted residual: $\int_0^L r(x) w_i(x)\, dx = 0, \quad i = 1,2,\ldots,N$

### 9.1.2 Weak Form (Galerkin's Method)

Integration by parts reduces continuity requirements:

$$
\int_0^L \left(p\frac{dw_i}{dx}\frac{du}{dx} + q w_i u\right) dx = \int_0^L w_i f\, dx + \left[ w_i p\frac{du}{dx}\right]_0^L
\tag{9.1.6}
$$

This is the **weak form** — only first derivatives appear, suitable for linear basis functions.

### 9.1.3 Basis Functions

For 1D linear elements with nodes at $x_1, x_2, \ldots, x_N$:

$$
u^e(x) = \sum_{j=1}^2 u_j^e N_j^e(x)
\tag{9.1.9}
$$

where $N_1^e(\xi) = 1 - \xi$, $N_2^e(\xi) = \xi$, with local coordinate $\xi = (x - x_1^e)/(x_2^e - x_1^e)$.

---

## 9.2 Finite Element Analysis of 1D Problems

### 9.2.1 Element Matrix Assembly

Element matrix:
$$
K_{ij}^e = \int_{x_1^e}^{x_2^e} \left(p\frac{dN_i}{dx}\frac{dN_j}{dx} + q N_i N_j\right) dx
\tag{9.2.1}
$$

Global assembly: $K = \sum_{e=1}^M K^e$, $b = \sum_{e=1}^M b^e$

System: $K \mathbf{u} = \mathbf{b}$

### 9.2.2 Boundary Conditions

**Dirichlet** (essential): $u$ specified → modify RHS
**Neumann** (natural): $du/dx$ specified → included in boundary term
**Mixed** (Robin): $\alpha u + \beta \frac{du}{dx} = \gamma$

---

## 9.3 2D Scalar FEM

### 9.3.1 Helmholtz Equation

$$
\nabla^2 u + k^2 u = g
\tag{9.3.1}
$$

Weak form (integrate by parts using Green's identity):

$$
\iint_\Omega (\nabla w_i \cdot \nabla u - k^2 w_i u)\, d\Omega = \iint_\Omega w_i g\, d\Omega - \oint_\Gamma w_i (\hat{\mathbf{n}} \cdot \nabla u)\, d\Gamma
\tag{9.3.2}
$$

### 9.3.2 Triangular Elements

Linear triangular element with nodes at $(x_1,y_1), (x_2,y_2), (x_3,y_3)$:

$$
N_i(x,y) = \frac{1}{2\Delta}(a_i + b_i x + c_i y), \quad i = 1,2,3
\tag{9.3.5}
$$

where $\Delta$ is the triangle area, and:

$$
a_i = x_j y_k - x_k y_j, \quad b_i = y_j - y_k, \quad c_i = x_k - x_j
$$

### 9.3.3 Element Matrix (2D)

$$
K_{ij}^e = \iint_{\Omega^e} (\nabla N_i \cdot \nabla N_j - k^2 N_i N_j)\, d\Omega
$$

For linear triangles, $\nabla N_i$ is constant within the element.

---

## 9.4 3D Vector FEM (Edge Elements)

### 9.4.1 Edge Elements (Whitney Elements)

Instead of nodal basis functions for each field component, edge elements use basis functions associated with element edges:

$$
\mathbf{N}_i = \xi_i \nabla\xi_j - \xi_j \nabla\xi_i
\tag{9.4.1}
$$

Advantages:
- Tangential continuity across element boundaries
- No spurious modes in eigenvalue problems
- Correct modeling of field singularities at edges

### 9.4.2 Application to Maxwell's Equations

$$
\iiint_V \left[(\nabla \times \mathbf{w}_i) \cdot (\nabla \times \mathbf{E}) - k^2 \mathbf{w}_i \cdot \mathbf{E}\right] dV = \cdots
\tag{9.4.5}
$$

---

## 9.5 Absorbing Boundary Conditions for FEM

For open-region problems, ABCs are needed to truncate the FEM mesh:
- **First-order ABC:** $(\nabla u) \cdot \hat{\mathbf{n}} = -j k u$
- **PML:** Perfectly Matched Layer, same concept as in FDTD

---

## 9.6 Adaptive Mesh Refinement

Error estimation using the recovered field gradient:

$$
\eta_e = \|\nabla u^h - \mathbf{Q} u^h\|_{L_2(\Omega^e)}
$$

Elements with error > threshold are subdivided.
