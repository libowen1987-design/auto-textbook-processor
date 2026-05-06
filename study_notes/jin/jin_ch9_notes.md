---
title: "Chapter 9 — The Finite Element Method"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Weighted residual / variational formulation
  - Galerkin method, shape functions (1D, 2D, 3D)
  - Isoparametric elements
  - Edge-based vector elements (Whitney)
  - Sparse matrix assembly
  - FEM for waveguide, scattering, cavity problems
  - FEM-BEM, ABC, PML for open problems
---

# Chapter 9: The Finite Element Method

## 9.1 Introduction

**Weighted residual:** $\langle \mathcal{L} \phi - f, w_j \rangle = 0$ for test functions $w_j$.

**Galerkin:** test functions = basis functions.

**1D Helmholtz example:**

$$
\int_\Omega \left( -\frac{d\phi}{dx}\frac{dw}{dx} + k^2 \phi w \right) dx = \int_\Omega f w \, dx
$$

## 9.2 Basis Functions

**1D:** linear $N_i(x) = (x_{i+1} - x)/(x_{i+1} - x_i)$, etc.

**2D triangles:** area coordinates $\zeta_1, \zeta_2, \zeta_3$.

**Edge elements (Whitney):** $\mathbf{N}_{ij} = \zeta_i \nabla \zeta_j - \zeta_j \nabla \zeta_i$ — enforce tangential continuity.

## 9.3 Isoparametric Elements

Geometric mapping $x = \sum N_i(\xi,\eta) x_i$ with same basis functions for geometry and field.

## 9.4 Sparse System Assembly

Element matrices $\mathbf{K}^e$, load vectors $\mathbf{b}^e$ assembled into global system.

## 9.5 Applications

**Waveguide analysis:** vector FEM for $\mathbf{E}$ or $\mathbf{H}$ with divergence-free condition imposed naturally.

**Scattering:** FEM + boundary integral (FEM-BEM), or FEM + PML.

**Cavity:** generalized eigenvalue problem $\mathbf{K}\mathbf{x} = \lambda \mathbf{M}\mathbf{x}$.

---

## Audit

| Section | Topic |
|---------|-------|
| 9.1 | Weighted residual / variational |
| 9.2 | Basis functions, edge elements |
| 9.3 | Isoparametric elements |
| 9.4 | System assembly |
| 9.5 | Applications |
