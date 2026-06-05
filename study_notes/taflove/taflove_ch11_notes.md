---
chapter: 11
title: "Nonuniform Grids, Nonorthogonal Grids, Unstructured Grids, and Subgrids"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, B. Z. Steinberg, M. Okoniewski, T. Weiland, R. Schuhmann"
raw_size: 109,577 bytes
---

# Chapter 11: Nonuniform Grids, Nonorthogonal Grids, Unstructured Grids, and Subgrids

## 11.1 Introduction

Structures with fine geometrical features often cannot conform to a uniform orthogonal lattice. Two strategies exist:

1. **Global mesh variation**: Nonuniform graded meshes, curvilinear body-fitted coordinate systems, or fully unstructured meshes (tetrahedral/hexahedral). These can conform to arbitrary geometries but may add computational overhead due to non-Cartesian numerical dispersion and stability properties.

2. **Local subgridding**: Embed refined subgrids only where needed, leaving the rest of the domain on a coarse Cartesian mesh. This avoids global mesh modification while achieving local resolution enhancement.

This chapter covers the full spectrum from simple nonuniform orthogonal grids to fully unstructured finite-volume methods and nested Cartesian subgrids.

## 11.2 Nonuniform Orthogonal Grids

### 11.2.1 Grid Definition

Let vertices be defined by general one-dimensional coordinates:

$$
\{x_i | i = 1, N_x\},\quad \{y_j | j = 1, N_y\},\quad \{z_k | k = 1, N_z\}
$$

Edge lengths:

$$
\Delta x_i = x_{i+1} - x_i,\quad \Delta y_j = y_{j+1} - y_j,\quad \Delta z_k = z_{k+1} - z_k
$$

Dual edge lengths (distances between edge centers):

$$
h_i^x = \frac{\Delta x_i + \Delta x_{i-1}}{2},\quad
h_j^y = \frac{\Delta y_j + \Delta y_{j-1}}{2},\quad
h_k^z = \frac{\Delta z_k + \Delta z_{k-1}}{2}
$$

### 11.2.2 Update Equations (Integral Form)

Using Faraday's and Ampère's laws in integral form on the Yee cell:

**H-field update** (Faraday):
$$
H_z^{n+1/2}(i+1/2, j+1/2, k) = H_z^{n-1/2}(i+1/2, j+1/2, k) + \frac{\Delta t}{\mu_{i+1/2, j+1/2, k} \Delta x_i \Delta y_j}
\left[ E_x^n(i+1/2, j+1, k) \Delta x_i - E_x^n(i+1/2, j, k) \Delta x_i + E_y^n(i, j+1/2, k) \Delta y_j - E_y^n(i+1, j+1/2, k) \Delta y_j \right]
$$

**E-field update** (Ampère):
$$
E_z^{n+1}(i, j, k+1/2) = \frac{2\epsilon_{i,j,k+1/2} - \sigma_{i,j,k+1/2} \Delta t}{2\epsilon_{i,j,k+1/2} + \sigma_{i,j,k+1/2} \Delta t} E_z^n(i, j, k+1/2)
+ \frac{2\Delta t}{2\epsilon_{i,j,k+1/2} + \sigma_{i,j,k+1/2} \Delta t} \frac{1}{h_i^x h_j^y}
\left[ H_x^{n+1/2}(i, j+1/2, k+1/2) h_i^x - H_x^{n+1/2}(i, j-1/2, k+1/2) h_i^x + H_y^{n+1/2}(i+1/2, j, k+1/2) h_j^y - H_y^{n+1/2}(i-1/2, j, k+1/2) h_j^y \right]
$$

### 11.2.3 Supraconvergence

Although the E-field updates are locally first-order in nonuniform regions (using averaged edge lengths $h_i^x$, $h_j^y$), the overall scheme achieves **global second-order accuracy** — a phenomenon known as *supraconvergence* (Monk 1992).

### 11.2.4 Stability Criterion

$$
\Delta t < \frac{1}{c \sqrt{(\Delta x_{i,\min})^{-2} + (\Delta y_{j,\min})^{-2} + (\Delta z_{k,\min})^{-2}}}
$$

where $\Delta x_{i,\min}$, $\Delta y_{j,\min}$, $\Delta z_{k,\min}$ are the minimum edge lengths in each direction. The time-step is thus limited by the smallest cell in the mesh.

### 11.2.5 Validation: Microstrip Lowpass Filter

Fig. 11.6 compares $S_{11}$ and $S_{21}$ computed with uniform and nonuniform grids for a microstrip lowpass filter. The nonuniform grid achieved equivalent accuracy with far fewer cells by grading the mesh only near the filter discontinuities.

## 11.3 Locally Conformal Grids, Globally Orthogonal

This class uses globally orthogonal grids with only those cells adjacent to curved boundaries deformed to conform (the contour-path approach of Chapter 10, §10.6). The Yu-Mittra technique (§10.6.1) is the most practical implementation:

- Only cells immediately adjacent to curved PEC/dielectric surfaces are modified.
- All other cells use standard Yee updates.
- Result: 4× resolution advantage per dimension over staircasing.
- Excellent stability (no late-time instability observed with the Yu-Mittra method).

## 11.4 Global Curvilinear Coordinates

### 11.4.1 Nonorthogonal Curvilinear FDTD

Coordinate system $(u^1, u^2, u^3)$ with unitary vectors $\mathbf{a}_i = \partial\mathbf{r}/\partial u^i$.
Reciprocal basis $\mathbf{a}^i$ satisfying $\mathbf{a}^i \cdot \mathbf{a}_j = \delta^i_j$.
Metric tensor: $g_{ij} = \mathbf{a}_i \cdot \mathbf{a}_j$, with determinant $g = \det(g_{ij})$.

Maxwell's equations in covariant/contravariant form:

$$
-\mu \frac{\partial h^i}{\partial t} = \frac{1}{\sqrt{g}} \left( \frac{\partial e_k}{\partial u^j} - \frac{\partial e_j}{\partial u^k} \right)
$$

$$
\epsilon \frac{\partial e^i}{\partial t} + \sigma e^i = \frac{1}{\sqrt{g}} \left( \frac{\partial h_k}{\partial u^j} - \frac{\partial h_j}{\partial u^k} \right)
$$

where $(i,j,k)$ are cyclic permutations of $(1,2,3)$, and contravariant components $h^i$, $e^i$ satisfy:

$$
h_i = \sum_{j=1}^3 g_{ij} h^j, \quad h^i = \sum_{j=1}^3 g^{ij} h_j
$$

### 11.4.2 Field Updates (Example: $h^1$ and $e^1$)

$$
h^{1,n+1}_{i,j,k} = h^{1,n}_{i,j,k} - \frac{\Delta t}{\mu \sqrt{g}} \left[ (e_{3,i,j+1,k}^{n+1/2} - e_{3,i,j,k}^{n+1/2}) - (e_{2,i,j,k+1}^{n+1/2} - e_{2,i,j,k}^{n+1/2}) \right]
$$

$$
e^{1,n+1/2}_{i,j,k} = \frac{2\epsilon - \sigma\Delta t}{2\epsilon + \sigma\Delta t} e^{1,n-1/2}_{i,j,k} + \frac{2\Delta t}{2\epsilon + \sigma\Delta t} \frac{1}{\sqrt{g}} \left[ (h_{3,i,j,k}^{n} - h_{3,i-1,j,k}^{n}) - (h_{2,i,j,k}^{n} - h_{2,i,j,k-1}^{n}) \right]
$$

### 11.4.3 Projection Operators

After contravariant fields are updated, covariant fields must be computed via (11.33) before the dual-field update:

$$
h_{1,i,j,k} = g_{11} h^{1}_{i,j,k} + 0.25 g_{12} (h^{2}_{i-1,j,k} + h^{2}_{i-1,j+1,k} + h^{2}_{i,j,k} + h^{2}_{i,j+1,k}) + 0.25 g_{13} (h^{3}_{i-1,j,k} + h^{3}_{i-1,j,k+1} + h^{3}_{i,j,k} + h^{3}_{i,j,k+1})
$$

### 11.4.4 Stability Criterion

$$
\Delta t \leq \frac{2}{c \sqrt{g^{11} + g^{22} + g^{33}}}
$$

where $g^{ii}$ are diagonal elements of the inverse metric tensor. For a uniform Cartesian grid, $g^{11} = (\Delta x)^{-2}$, reducing to the standard CFL condition.

## 11.5 Irregular Nonorthogonal Structured Grids

These use hexahedral cells aligned to boundaries but not necessarily orthogonal. The algorithm follows the same covariant/contravariant formulation as §11.4 but with locally varying metric tensors.

**Key challenge**: Maintaining stability requires careful handling of non-orthogonal terms. The "borrowing" technique (where missing E-field components are interpolated from neighbors) was an early fix, but the Yu-Mittra PEC approach (Chapter 10) is preferred.

## 11.6 Irregular Nonorthogonal Unstructured Grids

### 11.6.1 Generalized Yee Algorithm

Both electric and magnetic fields are represented as **edge-integrated** (or "whirl") quantities:

$$
\hat{E}_i = \int_{\text{edge } i} \mathbf{E} \cdot d\mathbf{l}, \quad
\hat{H}_i = \int_{\text{edge } i} \mathbf{H} \cdot d\mathbf{l}
$$

Faraday's law becomes:

$$
-\mu_{\text{avg}} \hat{H}_i^{n+1/2} = -\mu_{\text{avg}} \hat{H}_i^{n-1/2} + \Delta t \sum_{j\in\partial A_i} C_{i,j} \hat{E}_j^n
$$

where $C_{i,j}$ is the incidence matrix (orientation of edge $j$ relative to face $i$). Similarly, Ampère's law:

$$
\epsilon_{\text{avg}} \hat{E}_i^{n+1} = \epsilon_{\text{avg}} \hat{E}_i^n + \Delta t \sum_{j\in\partial A_i} B_{i,j} \hat{H}_j^{n+1/2}
$$

### 11.6.2 The Finite Integration Technique (FIT)

Developed by Weiland (1977), FIT uses the exact matrix representation of the integral Maxwell equations on a dual grid. The update equations are:

$$
\mathbf{C} \hat{\mathbf{e}} = -\frac{d}{dt} \hat{\mathbf{b}}, \quad
\tilde{\mathbf{C}} \hat{\mathbf{h}} = \frac{d}{dt} \hat{\mathbf{d}} + \hat{\mathbf{j}}
$$

where $\mathbf{C}$ is the discrete curl matrix. FIT extends naturally to unstructured grids.

### 11.6.3 Inhomogeneous Media

Material averaging is performed via:
- **Electric**: $\epsilon_{\text{avg}}$ computed from edge-length-weighted averaging of adjacent cell permittivities.
- **Magnetic**: $\mu_{\text{avg}}$ from face-area-weighted averaging.
- **Conductivity**: $\sigma_{\text{avg}}$ similarly averaged.

## 11.7 A Planar Generalized Yee Algorithm

A specialized 2.5D formulation for planar structures (microstrip, CPW). Uses edge-integrated fields with projection operators between the planar facets and the volumetric edges:

$$
\mathcal{P}_E : \text{planar E-components} \xrightarrow{\text{interpolation}} \text{volumetric edge E}
$$

The projection reduces memory by ~30-50% compared to full 3D, at the cost of some accuracy at high frequencies.

## 11.8 Cartesian Subgrids

### 11.8.1 Geometry

Subgrid blocks with 2:1 cell-size reduction (from primary grid) placed at specific locations. The subgrid is shifted by one-quarter of the primary grid cell dimension in each direction to optimize interpolation.

Key features:
- Up to 5 nested subgrids → 32:1 composite refinement
- Subgrid position offset: $\Delta/4$ in each direction
- All H-fields collocated for simplified interpolation

### 11.8.2 Time-Stepping Scheme

The subgrid uses $\Delta t/2$ (half the primary grid time-step). The 14-step update cycle includes:

1. Update primary $E \to E^{n}$
2. Update primary $H \to H^{n+1/2}$
3. Spatial cubic spline interpolation: primary $E \to$ subgrid border $e_b^n$
4. Spatial cubic spline: primary $H \to$ subgrid border $h_b^{n+1/2}$
5. Temporal quadratic interpolation: $e_s^n, e_s^{n-1}, e_s^{n-2} \to e_s^{n-0.5}$
6. Temporal quadratic interpolation: $h_b^{n+0.5}, h_b^{n-0.75}, h_b^{n-1.5} \to h_b^{n-0.25}$
7. Apply Yee algorithm to subgrid border for alternative $h_b^{n-0.25}$
8. Weighted average: $0.35 \times h_b^{n-0.25}_{\text{Step 6}} + 0.65 \times h_b^{n-0.25}_{\text{Step 7}}$
9-15. Continue Yee updates for interior subgrid cells

This scheme uses **temporal interpolation** (not extrapolation) for better accuracy and stability.

### 11.8.3 Spatial Interpolation

- **E-field border**: 27 primary E-components (3×3×3) → 1 subgrid e-component via 3D cubic spline.
- **H-field border**: 1D or 2D cubic splines from correlated H-components.
- **PEC crossing**: Modified interpolation excluding E-components inside the conductor.

### 11.8.4 Stability

Stable beyond 100,000 time-steps at 90% of the Courant limit. The weighting factors (0.35/0.65 in Step 8) were determined through numerical experiments.

### 11.8.5 Interface Reflection

- Single 2:1 subgrid: reflection < -70 dB at $\lambda_0/30$ primary resolution (Fig. 11.20).
- Nested subgrids (8:1 to 16:1): worst-case reflection ≈ -70 dB (Fig. 11.21).

## 11.9 Summary and Conclusions

| Grid Type | Accuracy | Computational Cost | Ease of Implementation | Stability |
|-----------|----------|-------------------|----------------------|-----------|
| Nonuniform orthogonal | 2nd-order globally | Moderate | Easy | CFL-limited to min cell |
| Locally conformal | Near 2nd-order | Low | Moderate | Good (Yu-Mittra) |
| Global curvilinear | 2nd-order | High | Difficult | Metric-dependent |
| Unstructured (FIT) | 1st-2nd order | High | Very difficult | Complex analysis |
| Cartesian subgrid | ~2nd-order | Moderate | Moderate | 90% of CFL |

### Key Takeaways
1. **Supraconvergence** ensures that nonuniform orthogonal FDTD achieves global second-order accuracy despite local first-order stencils.
2. **Nonorthogonal curvilinear FDTD** provides boundary-conforming capability at the cost of metric tensor computations and projection operations.
3. **Cartesian subgridding** is the most practical approach for localized mesh refinement, offering <-70 dB interface reflections.
4. **The generalized Yee algorithm** (based on edge-integrated fields) provides a unifying framework for all structured-grid formulations.
5. For most applications, a nonuniform orthogonal grid with subgridding in critical regions offers the best balance of accuracy, efficiency, and implementation simplicity.
