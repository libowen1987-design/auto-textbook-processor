---
title: "Ch4: Finite-Difference Time-Domain Method"
book: "Sheng & Song, Essentials of Computational Electromagnetics (2012)"
chapter: 4
pages: "213-248"
weight: 4
topics:
  - Yee grid
  - PML perfectly matched layer
  - Surface treatment
  - Dispersive media
  - Lumped elements
  - TF/SF total-field/scattered-field
  - Comparison with MoM and FEM
notes_version: "1.0"
---

# Chapter 4: Finite-Difference Time-Domain Method

The **finite-difference time-domain method (FDTD)** is a full-wave numerical method that directly discretizes the **time-domain partial differential form of Maxwell's equations** using finite differences. Developed by K.S. Yee in the 1960s, the Yee scheme defines electric and magnetic field components in an interleaving fashion both in 3D space and in time, forming an "interlinked array of Faraday's Law and Ampere's Law contours" representing physical EM wave propagation.

## 4.1 Scattering from a Three-Dimensional Objects

### 4.1.1 FDTD Solution Scheme

**Domain truncation**: The unbounded problem domain is truncated using an **absorbing boundary condition (ABC)** to suppress spurious reflections of outgoing numerical waves. Two main approaches:

1. **Differential-equation-based ABCs** (e.g., Engquist-Majda/Mur ABC): approximate the outgoing wave equation by linear Taylor expressions
2. **Absorbing-material-based ABCs** (e.g., PML): surround the computational domain with a lossy material that attenuates outgoing waves

**Total-Field/Scattered-Field (TF/SF) technique**: The Yee lattice is zoned into:
- **Center region** (containing scatterers): total field $\mathbf{E}_{total} = \mathbf{E}_{inc} + \mathbf{E}_{sc}$ used as unknowns
- **Surrounding region**: scattered field only (outside connection boundary)

A **connection boundary** separates the two regions. Huygens' principle is applied on an **output boundary** (usually a box enclosing the scatterer between ABC and connection boundary) to compute far-zone scattering.

**Why TF/SF?**: In shadow regions, scattered field has equivalent amplitude and opposite phase to incident field, resulting in total field close to zero. A minor error in scattered field causes large relative error — hence total field formulation is preferred in those regions.

### 4.1.2 Perfectly Matched Layers (PML)

The PML (Berenger, 1994) achieves reflectionless absorption by using a complex coordinate stretching that introduces exponential attenuation in the absorbing direction.

**Design principle**: Apply the local Wilcox series expansion to the scattered field at point $P$ from the inner PML boundary:

$$
\mathbf{E}_S(u,v,w) = \frac{e^{-jkw}}{4\pi(r_1 r_2)^{1/2}} \sum_{n=0}^{\infty} \mathbf{E}_S^{(n)}(u,v) \frac{1}{(r_1 r_2)^{n/2}} \tag{4.1}
$$

where $(u,v,w)$ are local coordinates with stretching coefficients $(h_1, h_2, 1)$, $k = \omega/c$, and $r_1, r_2$ are principal radii at point $P$.

**Complex coordinate transformation** in the absorbing material region:

$$
\tilde{w} = s_w w, \quad w > 0, \quad s_w = \kappa_w + \frac{\sigma_w}{j\omega\epsilon_0} \tag{4.2}
$$

The attenuation factor $e^{-\kappa_w w}$ and phase term $e^{-jk_0\kappa_w w}$ together ensure:
1. Field continuity at the PML interface (analytic continuation)
2. Exponential decay inside PML

**Coordinate stretching operator**:

$$
\nabla \rightarrow \bar{\nabla} = \hat{x}\frac{1}{s_x}\frac{\partial}{\partial x} + \hat{y}\frac{1}{s_y}\frac{\partial}{\partial y} + \hat{z}\frac{1}{s_z}\frac{\partial}{\partial z} \tag{4.5}
$$

where

$$
\bar{\bar{S}} = \hat{x}\hat{x}\frac{1}{s_x} + \hat{y}\hat{y}\frac{1}{s_y} + \hat{z}\hat{z}\frac{1}{s_z} \tag{4.7}
$$

**Modified Maxwell's equations in PML**:

$$
\bar{\nabla} \times \mathbf{E}^c = -j\omega\mu \mathbf{H}^c \tag{4.8}
$$

$$
\bar{\nabla} \times \mathbf{H}^c = j\omega\epsilon \mathbf{E}^c \tag{4.9}
$$

**Effective constitutive parameters**: From identity (4.10) and (4.17):

$$
\bar{\bar{\epsilon}}_r = \bar{\bar{\mu}}_r = \bar{\bar{L}} = \hat{x}\hat{x}L_x + \hat{y}\hat{y}L_y + \hat{z}\hat{z}L_z \tag{4.18}
$$

$$
L_x = \frac{s_y s_z}{s_x}, \quad L_y = \frac{s_z s_x}{s_y}, \quad L_z = \frac{s_x s_y}{s_z} \tag{4.19}
$$

**Stretching factors** (general form):

$$
s_x = \kappa_x + \frac{\sigma_x}{j\omega\epsilon_0}, \quad s_y = \kappa_y + \frac{\sigma_y}{j\omega\epsilon_0}, \quad s_z = \kappa_z + \frac{\sigma_z}{j\omega\epsilon_0} \tag{4.20}
$$

| Region | $s_x$ | $s_y$ | $s_z$ |
|--------|-------|-------|-------|
| Interior (lossless) | 1 | 1 | 1 |
| PML face (e.g., x=PML) | $\neq 1$ | 1 | 1 |
| PML edge (e.g., x,y=PML) | $\neq 1$ | $\neq 1$ | 1 |
| PML corner (x,y,z=PML) | $\neq 1$ | $\neq 1$ | $\neq 1$ |

**Auxiliary Differential Equation (ADE) method**: Direct substitution of (4.20) into (4.21) would require convolution. ADE introduces auxiliary variables:

$$
D_x = \epsilon \frac{s_z}{s_x} E_x, \quad D_y = \epsilon \frac{s_x}{s_y} E_y, \quad D_z = \epsilon \frac{s_y}{s_z} E_z \tag{4.22}
$$

This yields a composite self-consistent system of time-domain differential equations (4.26).

**PML parameter profile** (Gedney's recommendation):

$$
\sigma_z(z) = \sigma_{\max} \left( \frac{z - z_0}{d} \right)^m \tag{4.31}
$$

with $m = 4$ and

$$
\sigma_{\max} = \frac{m+1}{150 \pi \sqrt{\epsilon_r} \Delta} \tag{4.32}
$$

where $d$ is PML thickness, $z_0$ is the PML interface position, and $\Delta$ is the FDTD spatial discretization.

### 4.1.3 Yee Discretizing Scheme

**Spatial grid**: Each electric field component is surrounded by four magnetic field components, and each magnetic field component is surrounded by four electric field components. This interleaving allows direct central-difference approximation of curl operations.

**Grid notation**:

$$
(i,j,k) = (i\Delta_x, j\Delta_y, k\Delta_z) \tag{4.33}
$$

$$
u(i\Delta_x, j\Delta_y, k\Delta_z, n\Delta_t) = u|^{n}_{i,j,k} \tag{4.34}
$$

**Time interleaving (leapfrog scheme)**: E and H components are defined at interleaved half-time steps. Define auxiliary fields $\mathbf{D}$ and $\mathbf{B}$ aligned with $\mathbf{E}$ and $\mathbf{H}$.

**Update for $D_x$** (semi-implicit form):

$$
D_x|^{n+1}_{i+1/2,j,k} = \frac{2\epsilon\kappa_y - \sigma_y\Delta_t}{2\epsilon\kappa_y + \sigma_y\Delta_t} D_x|^{n}_{i+1/2,j,k} + \frac{2\epsilon\Delta_t}{2\epsilon\kappa_y + \sigma_y\Delta_t} \left( \frac{H_z|^{n+1/2}_{i+1/2,j+1/2,k} - H_z|^{n+1/2}_{i+1/2,j-1/2,k}}{\Delta_y} - \frac{H_y|^{n+1/2}_{i+1/2,j,k+1/2} - H_y|^{n+1/2}_{i+1/2,j,k-1/2}}{\Delta_z} \right) \tag{4.36}
$$

**Update for $E_x$**:

$$
E_x|^{n+1}_{i+1/2,j,k} = \frac{2\epsilon\kappa_z - \sigma_z\Delta_t}{2\epsilon\kappa_z + \sigma_z\Delta_t} E_x|^{n}_{i+1/2,j,k} + \frac{1}{2\epsilon\kappa_z + \sigma_z\Delta_t} \left[ (2\epsilon\kappa_x + \sigma_x\Delta_t) D_x|^{n+1}_{i+1/2,j,k} - (2\epsilon\kappa_x - \sigma_x\Delta_t) D_x|^{n}_{i+1/2,j,k} \right] \tag{4.38}
$$

**Magnetic field updates** follow analogously (from Faraday's law):

$$
B_x|^{n+3/2}_{i,j+1/2,k+1/2} = \frac{2\mu\kappa_y - \sigma_y\Delta_t}{2\mu\kappa_y + \sigma_y\Delta_t} B_x|^{n+1/2}_{i,j+1/2,k+1/2} + \frac{2\mu\Delta_t}{2\mu\kappa_y + \sigma_y\Delta_t} \left( \frac{E_z|^{n+1}_{i,j+1,k+1/2} - E_z|^{n+1}_{i,j,k+1/2}}{\Delta_y} - \frac{E_y|^{n+1}_{i,j+1/2,k+1} - E_y|^{n+1}_{i,j+1/2,k}}{\Delta_z} \right) \tag{4.39}
$$

$$
H_x|^{n+3/2}_{i,j+1/2,k+1/2} = \frac{2\mu\kappa_z - \sigma_z\Delta_t}{2\mu\kappa_z + \sigma_z\Delta_t} H_x|^{n+1/2}_{i,j+1/2,k+1/2} + \frac{1}{2\mu\kappa_z + \sigma_z\Delta_t} \left[ (2\mu\kappa_x + \sigma_x\Delta_t) B_x|^{n+3/2}_{i,j+1/2,k+1/2} - (2\mu\kappa_x - \sigma_x\Delta_t) B_x|^{n+1/2}_{i,j+1/2,k+1/2} \right] \tag{4.40}
$$

**Connection boundary adjustment**: At the TF/SF interface, the update equations must be modified to account for the connecting condition that injects the incident plane wave uniformly through the boundary.

**Special attention required for**: corner points, face points — the total-field and scattered-field distributions differ, requiring separate treatment.

---

## 4.2 Surface Treatment

### 4.2.1 Curved Surface Treatment

**Staircase approximation problem**: Standard FDTD uses rectangular grid; curved surfaces are approximated by staircase, causing numerical error especially for electrically large objects.

**Treatment methods**:

1. **Subcell techniques**: Use fine mesh near surface (memory-intensive)
2. **Contour-path FDTD**: Redefine the contour path for cells intersected by the surface to better approximate the geometry
3. **Physical smoothing**: Conformal FDTD methods that modify update equations for cells cut by the surface

**For cells intersecting the boundary**: The average material properties in the cell are used, or a modified contour path that follows the actual surface is employed. This improves accuracy without requiring extremely fine mesh.

### 4.2.2 Thin Material Layer Treatment

For layers thinner than one cell, the effective transmission coefficient and reflection coefficient are derived analytically and incorporated into the FDTD update equations as boundary conditions.

---

## 4.3 Dispersive Media

### 4.3.1 Frequency-Dependent Media

In dispersive media, $\epsilon(\omega)$ and $\mu(\omega)$ vary with frequency. The time-domain constitutive relations become convolutions:

$$
\mathbf{D}(t) = \epsilon(\infty) \mathbf{E}(t) + \int_0^t \epsilon(\tau) \mathbf{E}(t - \tau) d\tau
$$

**Common dispersive models**:
- **Lorentz model** for permittivity: $\epsilon(\omega) = \epsilon_\infty + \sum_p \frac{\omega_p^2}{\omega_0^2 - \omega^2 - j\omega\delta}$
- **Drude model** for metals: $\epsilon(\omega) = \epsilon_\infty - \frac{\omega_p^2}{\omega(\omega + j\gamma)}$

### 4.3.2 ADE Treatment for Debye Media

For a single-pole Debye medium $\epsilon(\omega) = \epsilon_\infty + \frac{\epsilon_s - \epsilon_\infty}{1 + j\omega\tau}$:

Introduce auxiliary polarization variable $\mathbf{P}$ and solve:

$$
\frac{d\mathbf{P}}{dt} + \frac{1}{\tau} \mathbf{P} = \frac{\epsilon_s - \epsilon_\infty}{\tau} \mathbf{E}
$$

Combined with Maxwell's equations, this yields update equations that handle the dispersion explicitly.

---

## 4.4 Lumped Elements

### 4.4.1 Connection to Circuit Elements

Lumped circuit elements (resistors, capacitors, inductors, diodes) are connected to the FDTD grid at specific points using the **lumped element interface** condition:

$$
\hat{n} \times (\mathbf{E}_2 - \mathbf{E}_1) = \mathbf{J}_s \quad \text{(surface current from lumped element)}
$$

The voltage across the element is related to the tangential E-field at the connection, and the current is related to the surrounding H-fields.

### 4.4.2 Thin Wire Treatment

A thin wire (radius << cell size) carrying current $I$ is modeled by:

- **1D transmission line equation** along the wire
- **Coupling** to 3D FDTD grid through the electric field boundary condition

---

## 4.5 Comparison of MoM, FEM, and FDTD

| Feature | MoM | FEM | FDTD |
|---------|-----|-----|------|
| **Domain** | Open (surface) | Interior/tetrahedral | Volume/hexahedral |
| **Matrix type** | Dense (full) | Sparse | Explicit update |
| **Solution method** | Direct/iterative | Direct/iterative | Time-marching |
| **Excitation** | Frequency domain | Frequency domain | Broadband (time pulse) |
| **Mesh** | Surface patches | Tetrahedral (unstructured) | Rectangular (structured) |
| **Suitable for** | Thin wires, surfaces | Complex inhomogeneous media | Homogeneous/simple geometries |
| **Memory** | $O(N^2)$ | $O(N)$ | $O(N)$ |
| **Time behavior** | Single frequency | Single frequency | Full time history |
| **Boundary** | Natural (Green's function) | Artificial truncation required | ABC/PML required |

**Key insights**:
- MoM is most efficient for open-domain radiation/scattering from thin metallic structures (surface currents only)
- FEM excels for complex inhomogeneous dielectric objects with arbitrary geometry
- FDTD handles wideband problems naturally but requires fine mesh for curved surfaces

**Hybrid approach rationale**: Since each method has distinct advantages, hybrid methods combine their strengths — e.g., FDTD for wideband excitation regions combined with FEM for detailed modeling of complex local structures.

---

## Key Equations Summary

| Equation | Physical Meaning |
|----------|-----------------|
| (4.1) | Wilcox series expansion for PML field |
| (4.2) | Complex coordinate stretching in PML |
| (4.5) | Coordinate stretching operator |
| (4.18)-(4.19) | Effective PML constitutive parameters |
| (4.20) | Stretching factors with conductivity and kappa |
| (4.22) | Auxiliary variables (D-field) for ADE-PML |
| (4.36) | D_x update equation (Yee scheme with PML) |
| (4.38) | E_x update from D_x |
| (4.39)-(4.40) | B_x and H_x update equations |

---

## Problems

**4.1** Derive explicit update equations for the E-field components in a PML region with conductivity $\sigma$ (conductive medium case).

**4.2** Derive explicit time-marching expressions for $D_y$, $E_y$, $B_z$, and $H_z$.

**4.3** Write the adjusted equations for the connection boundary (TF/SF interface).

**4.4** Write a 2D FDTD program (TE$_z$ mode, $E_x$, $E_y$, $H_z$) for a domain with PEC truncation, with a hard line source at a specified location.

**4.5** Replace the outer 25 layers of Problem 4.4 with PML and test performance.

**4.6** Define TF/SF region in the center (Problem 4.4 without hard source), add connection boundary for plane wave injection.

**4.7** Simulate a cylindrical PEC cavity resonator (radius 0.15 m) and compare lowest four resonant frequencies with analytical values (0.586 GHz, 0.9721 GHz, 1.2198 GHz, 1.3372 GHz) at different spatial resolutions.

**4.8** Simulate an air-filled rectangular PEC cavity (0.4m × 0.2m × 0.3m) and obtain the lowest five resonant frequencies.

---

## References

[1] Mur, G. (1981) Absorbing boundary conditions for the finite-difference approximation of the time-domain electromagnetic field equations. IEEE Transactions on Electromagnetic Compatibility, 23, 377–382.
[2] Berenger, J. (1994) A perfectly matched layer for the absorption of electromagnetic waves. Journal of Computational Physics, 114, 185–200.
[3] Gedney, S.D. (1996) An anisotropic perfectly matched layer-absorbing medium for the truncation of FDTD lattices. IEEE Transactions on Antennas and Propagation, 44, 1630–1639.
[4] Taflove, A. and Hagness, S.C. (2005) Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd edn, Artech House, Norwood, MA.
[5] Yee, K.S. (1966) Numerical solution of initial boundary value problems involving Maxwell's equations in isotropic media. IEEE Transactions on Antennas and Propagation, 14, 302–307.
[6] Umashankar, K. and Taflove, A. (1982) A novel method to analyze electromagnetic scattering of complex objects. IEEE Transactions on Electromagnetic Compatibility, 24, 397–405.
[7] Luebbers, R.J., Kunz, K.S., Schneider, M., and Hunsberger, F. (1991) A finite-difference time-domain near zone to far zone transformation. IEEE Transactions on Antennas and Propagation, 39, 429–433.