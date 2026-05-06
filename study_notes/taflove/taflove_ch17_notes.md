---
chapter: 17
title: "Pseudospectral Time-Domain (PSTD) Method"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, Q. H. Liu"
raw_size: 67,319 bytes
---

# Chapter 17: Pseudospectral Time-Domain (PSTD) Method

## 17.1 Introduction

PSTD replaces finite-difference spatial derivatives with **global** Fourier transform (FFT-based) or Chebyshev polynomial approximations. This achieves spectral accuracy: errors decrease exponentially with grid resolution rather than algebraically.

**Key advantage**: For smooth geometries, PSTD requires only 2 cells per wavelength (Nyquist limit) vs. 10-20 for FDTD, reducing memory by factor (5-10)^D in D dimensions.

## 17.2 FFT-Based PSTD

### Formulation

Maxwell's equations in PSTD form:

$$
\frac{\partial \mathbf{H}}{\partial t} = -\frac{1}{\mu} \mathcal{F}^{-1} \left[ j\mathbf{k} \times \mathcal{F}(\mathbf{E}) \right]
$$

$$
\frac{\partial \mathbf{E}}{\partial t} = \frac{1}{\epsilon} \mathcal{F}^{-1} \left[ j\mathbf{k} \times \mathcal{F}(\mathbf{H}) \right] - \frac{\sigma}{\epsilon} \mathbf{E}
$$

where $\mathcal{F}$ and $\mathcal{F}^{-1}$ are the forward and inverse FFT, and $\mathbf{k}$ is the wavevector in the spectral domain.

### One-Dimensional Example

$$
\frac{\partial E_x}{\partial t} = \frac{1}{\epsilon} \mathcal{F}^{-1} \left[ j k_z \mathcal{F}(H_y) \right]
$$

Implementation steps per time-step:
1. FFT H_y to spectral domain
2. Multiply by $j k_z$ (spectral derivative)
3. Inverse FFT back to spatial domain
4. Update E_x using standard leapfrog in time

### Stability

CFL condition for PSTD:

$$
\Delta t \leq \frac{2}{\pi} \frac{\Delta x}{c \sqrt{D}} \quad \text{(2/π factor vs. FDTD's 1)}
$$

PSTD allows larger time-steps because the spatial discretization is at the Nyquist limit.

## 17.3 Chebyshev PSTD

For non-periodic boundaries, Chebyshev polynomials replace FFT. The Gauss-Lobatto collocation points cluster near boundaries:

$$
x_i = \frac{L}{2} \cos\left( \frac{\pi i}{N} \right), \quad i = 0, 1, \ldots, N
$$

Derivatives computed via Chebyshev differentiation matrix $D_{ij}$:

$$
\frac{\partial u}{\partial x}(x_i) = \sum_{j=0}^N D_{ij} u(x_j)
$$

## 17.4 Applications

### Waveguide Analysis
- PSTD with 2 cells/$\lambda$ matches FDTD with 20 cells/$\lambda$
- Computational saving: $10^3$ in 3D

### Periodic Structures
- Natural fit: FFT inherently satisfies periodic boundary conditions
- No split-field or field-transformation needed for oblique incidence
- Combined with PBC for PhC analysis

### Scattering
- Near-to-far-field transformation similar to FDTD
- Perfectly matched layer (PML) adapted for PSTD

## 17.5 Limitations

1. **Gibbs phenomenon**: Discontinuities cause ringing (mitigated by low-pass filtering)
2. **FFT overhead**: $O(N \log N)$ per step vs. $O(N)$ for FDTD
3. **Parallel efficiency**: Global FFT is harder to parallelize than local FDTD stencils
4. **Non-uniform grids**: FFT requires uniform sampling; Chebyshev addresses this partly

## Summary

| Feature | FDTD | FFT-PSTD | Chebyshev-PSTD |
|---------|------|----------|-----------------|
| Cells/λ | 10-20 | 2 | 2-3 |
| Accuracy | $O(\Delta^2)$ | Spectral | Spectral |
| BCs | Natural | Periodic required | Dirichlet/Neumann |
| Per-step cost | $O(N)$ | $O(N \log N)$ | $O(N^2)$ |
| Parallel | Excellent | Moderate | Poor |
