---
title: "Chapter 11 — Fast Algorithms and Hybrid Techniques"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - CG-FFT: iterative solver + FFT for Toeplitz matrices
  - AIM: Adaptive Integral Method
  - FMM/MLFMA: Fast Multipole Method
  - ACA: Adaptive Cross-Approximation
  - Hybrid FEM/FDTD
  - Hybrid FEM/MoM (FE-BI)
---

# Chapter 11: Fast Algorithms and Hybrid Techniques

## 11.1 Fast Algorithms

**CG-FFT:** Conjugate Gradient + FFT exploits Toeplitz structure of Green's function on uniform grids. Complexity $O(N \log N)$ per iteration.

**AIM:** Projects basis functions onto a uniform grid, uses FFT for far-field interactions. $O(N \log N)$.

**FMM:** Decomposes interactions into near-field (direct) and far-field (multipole expansion). $O(N^{1.5})$ per iteration.

**MLFMA (Multilevel FMM):** Tree-based recursive subdivision. $O(N \log N)$ per iteration.

**ACA:** Low-rank approximation of sub-blocks. $O(N \log N)$.

| Algorithm | Complexity | Memory |
|-----------|-----------|--------|
| Direct MoM | $O(N^3)$ | $O(N^2)$ |
| CG-FFT | $O(N_{\text{iter}} N \log N)$ | $O(N)$ |
| FMM | $O(N_{\text{iter}} N^{1.5})$ | $O(N^{1.5})$ |
| MLFMA | $O(N_{\text{iter}} N \log N)$ | $O(N \log N)$ |
| ACA | $O(N \log N)$ | $O(N \log N)$ |

## 11.2 Hybrid Techniques

**FEM/FDTD hybrid:** FEM for fine geometric details, FDTD for large regular regions.

**FEM/MoM (FE-BI):** FEM inside (inhomogeneous), MoM on boundary (open region). Boundary integral provides exact radiation condition.

---

## Audit

| Section | Topic |
|---------|-------|
| 11.1 | CG-FFT, AIM, FMM, MLFMA, ACA |
| 11.2 | Hybrid FEM/FDTD, FEM/MoM |
