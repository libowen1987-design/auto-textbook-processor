---
chapter: 19
title: "Hybrid FDTD-Finite Element Methods"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, R. Lee, A. C. Cangellaris"
raw_size: 104,976 bytes
---

# Chapter 19: Hybrid FDTD-Finite Element Methods

## 19.1 Introduction

FDTD excels in homogeneous regions; FEM excels on unstructured meshes for complex boundaries. **Hybrid FDTD-FEM** combines both: FDTD in the bulk, FEM near boundaries/fine features.

## 19.2 FETD (Finite-Element Time-Domain)

### Vector Finite Elements (Edge Elements)
Whitney edge basis functions for tetrahedral/hexahedral elements:

$$
\mathbf{N}_i(\mathbf{r}) = \lambda_{i1} \nabla \lambda_{i2} - \lambda_{i2} \nabla \lambda_{i1}
$$

where $\lambda_{ij}$ are barycentric coordinates. Edge elements:
- Enforce tangential continuity
- Allow natural material discontinuities
- Eliminate spurious modes

### FETD Formulation
Weak form of Maxwell's equations:

$$
\left[ \mathbf{T} \right] \frac{d^2 \mathbf{e}}{dt^2} + \left[ \mathbf{S} \right] \mathbf{e} + \text{boundary terms} = 0
$$

Mass matrix $T_{ij} = \iiint \epsilon \mathbf{N}_i \cdot \mathbf{N}_j dV$
Stiffness matrix $S_{ij} = \iiint \frac{1}{\mu} (\nabla \times \mathbf{N}_i) \cdot (\nabla \times \mathbf{N}_j) dV$

Time-stepping via Newmark-beta scheme (unconditional stable option: $\beta \geq 1/4$).

## 19.3 Hybrid Coupling Approaches

### 19.3.1 Overlapping Domain Decomposition
FEM region embedded within FDTD grid. Interface handled via:
- Huygens' surface equivalence
- Field interpolation between grids
- Stability maintained by implicit FEM time-step ≥ explicit FDTD time-step

### 19.3.2 Non-Overlapping (Mortar) Methods
FDTD and FEM domains meet at a common interface. Mortar elements enforce field continuity:

$$
\iint_{\Gamma} (\mathbf{E}_{\text{FDTD}} - \mathbf{E}_{\text{FEM}}) \cdot \mathbf{N}_m dS = 0
$$

### 19.3.3 Subgridding Hybrid
FEM replaces the FDTD subgrid for highly irregular regions:
- Better accuracy than Cartesian subgridding for curved features
- No staircase error at curved boundaries
- Computational overhead of FEM-to-FDTD interpolation

## 19.4 Stability

The hybrid method inherits stability if:
- FDTD region satisfies its CFL condition
- FEM region uses unconditionally stable Newmark scheme
- Coupling is energy-conserving (symmetric coupling matrices)

Stability limit dominated by FDTD's CFL and the FEM element sizes at the interface.

## 19.5 Applications

### Microwave Components
- Waveguide filters with rounded corners (FEM at corners, FDTD in waveguide)
- Microstrip patch antenna with curved edges (FEM near patch, FDTD in substrate)

### Scattering from Complex Targets
- Aircraft with antenna radome: FEM for radome, FDTD for free space
- Coated targets: FEM for coating, FDTD elsewhere

### EMC/EMI
- Cable bundles in enclosures: FEM for cable cross-section, FDTD for enclosure

## Summary

| Coupling Method | Accuracy | Stability | Implementation |
|----------------|----------|-----------|----------------|
| Overlapping | 2nd order | Conditional | Moderate |
| Mortar (non-overlapping) | Spectral | Conditional | Complex |
| Subgrid hybrid | 2nd order | Conditional | Difficult |
