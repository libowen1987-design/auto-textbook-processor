---
chapter: 12
title: Concluding Remarks on Computational Electromagnetics
source: Jin, Theory and Computation of Electromagnetic Fields, 2nd Ed., pp. 675–704
sections: 3
examples: 0
---

# Chapter 12: Concluding Remarks on Computational Electromagnetics

## 12.1 Overview of Computational Electromagnetics (pp. 651–678)

CEM methods divide into **time-domain** and **frequency-domain**, related by Fourier transform.

### 12.1.1 Frequency- vs. Time-Domain Analysis

| Feature | Frequency Domain | Time Domain |
|---------|:----------------:|:-----------:|
| Dimensionality | 3D + 1 parameter ($\omega$) | 4D (space + time) |
| Matrix solve | Once per frequency | Marching in time |
| Multiple excitations | Efficient (matrix reused) | Must repeat |
| Broadband | Need many frequencies | Single run sufficient |
| Dispersive media | Natural | More complex |
| Nonlinear media | Difficult | Natural |

### 12.1.2 High-Frequency Asymptotic Techniques (pp. 652–654)

Based on ray optics when object $\gg \lambda$:

- **GO** (Geometrical Optics): Snell's law ray tracing; zero field in shadow.
- **GTD** (Geometrical Theory of Diffraction): Add diffracted fields from edges.
- **UTD** (Uniform Theory of Diffraction): Transition function at shadow boundaries.
- **PO** (Physical Optics): $\mathbf{J}_s \approx 2\hat{n}\times\mathbf{H}^{\text{inc}}$ on lit surface, $0$ in shadow.
- **PTD** (Physical Theory of Diffraction): Adds fringe currents for edge effects.
- **SBR** (Shooting and Bouncing Rays): Grid of rays traced via GO, PO integration at each bounce.

### 12.1.3 First-Principle Numerical Methods (pp. 654–656)

**PDE methods** (FDM, FEM):
- Static: elliptic PDE → positive definite matrix
- Time-harmonic: hyperbolic PDE → indefinite matrix → slow iterative convergence
- Dispersion error: phase error $\propto O[(h/\lambda)^2]$ for linear basis, cumulative
- Higher-order bases reduce phase error exponentially

**Integral equation methods** (MoM):
- SIE (surface): for impenetrable/homogeneous regions
- VIE (volume): for inhomogeneous regions
- EFIE: Fredholm 1st kind → accurate but slow convergence
- MFIE: Fredholm 2nd kind → fast convergence but less accurate
- CFIE: combined for closed bodies → eliminates interior resonance
- Preconditioners: Calderón identity, block diagonal, near-neighbor

**PEEC** (Partial Element Equivalent Circuit): converts EFIE to circuit model for EMI/EMC.

### 12.1.4 Time-Domain Methods (pp. 656–658)

| Method | Key Feature |
|--------|:-----------:|
| **FDTD** (Yee, 1966) | Explicit leapfrog, $O(N)$ per step |
| **FETD** | Unstructured mesh, implicit/explicit |
| **TLM** | Transmission line matrix, Huygens' principle |
| **FIT** (Weiland) | Finite integration on dual grids |
| **FVTD** | Conservative finite volume, shock capturing |
| **PSTD** | Fourier pseudospectral, coarse grid |
| **MRTD** | Wavelet basis, multiresolution |
| **DGTD** | Discontinuous Galerkin, element-local, parallel |

### 12.1.5 Surface Integral Equations (pp. 658–660)

For PEC bodies:
- EFIE: $\hat{n}\times(\mathcal{L}\mathbf{J}) = -\hat{n}\times\mathbf{E}^{\text{inc}}$
- MFIE: $\frac{1}{2}\mathbf{J} - \hat{n}\times(\mathcal{K}\mathbf{J}) = -\hat{n}\times\mathbf{H}^{\text{inc}}$
- CFIE: $\alpha\text{EFIE} + (1-\alpha)\eta\text{MFIE}$

For dielectric bodies: PMCHWT formulation using both EFIE and MFIE.

### 12.1.6 Volume Integral Equations (pp. 660–662)

For inhomogeneous dielectrics:

$$
\mathbf{E}(\mathbf{r}) = \mathbf{E}^{\text{inc}}(\mathbf{r}) + k_0^2\iiint_V (\epsilon_r(\mathbf{r}') - 1)\mathbf{E}(\mathbf{r}')G_0(\mathbf{r},\mathbf{r}')\,dV' + \nabla\iiint_V \frac{(\epsilon_r(\mathbf{r}') - 1)\nabla'\cdot\mathbf{E}(\mathbf{r}')}{k_0^2} G_0(\mathbf{r},\mathbf{r}')\,dV'
$$

VIE yields $3N$ unknowns for $N$ volume cells (vs $2N$ for SIE on surface).

## 12.2 Practical Applications (pp. 678–690)

### 12.2.1 Antenna Analysis and Design
- Wire antennas (MoM-Wu-King, Hallén, Pocklington)
- Microstrip antennas (FEM, MoM with layered Green's function)
- Reflector antennas (PO/PTD + FMM)
- Antenna arrays (FEM for finite arrays, periodic BC for infinite)

### 12.2.2 Microwave Circuits
- Waveguide components (FEM, Mode matching)
- Filters (FEM with adaptive mesh refinement)
- Power dividers, couplers
- RFIC/MMIC (PEEC, FEM)

### 12.2.3 Scattering and RCS
- Monostatic RCS (FMM/MLFMA with iterative solves for each angle)
- Bistatic RCS
- Radar signature (SBR for complex targets)

### 12.2.4 EMC/EMI
- Cable coupling (TL theory + MoM)
- Shielding effectiveness (FEM)
- System-level EMC (hybrid methods)

### 12.2.5 Biomedical Applications
- SAR calculation (FDTD, FEM)
- Hyperthermia treatment planning
- Medical imaging (microwave tomography)
- Wireless body area networks

### 12.2.6 Photonics and Optics
- Optical waveguides (FEM with PML)
- Photonic crystals (FDTD, FEM)
- Plasmonic structures
- Nonlinear optics (FDTD with nonlinear materials)

## 12.3 Challenges and Future Trends (pp. 690–704)

### 12.3.1 Computational Challenges
- **Multi-scale problems**: fine features in electrically large structures
- **Multi-physics**: EM + thermal + mechanical coupling
- **Uncertainty quantification**: random geometries/materials
- **Real-time simulation**: digital twins

### 12.3.2 Algorithmic Development
- Discontinuous Galerkin methods (DGTD, DGFEM)
- Isogeometric analysis (IGA) — higher-order smooth basis
- Model order reduction (MOR) — reduced basis, POD
- Domain decomposition methods (DDM) — additive Schwarz, FETI

### 12.3.3 Hardware Acceleration
- GPU acceleration: $10\times$–$100\times$ speedup for FDTD, FEM, MoM
- Many-core CPUs (Xeon Phi)
- FPGA-based electromagnetic solvers
- Tensor processing units (TPU) for ML-based methods

### 12.3.4 Machine Learning in CEM
- Surrogate models for EM analysis
- Neural network-based solvers (PINN)
- ML for mesh generation and optimization
- ML-accelerated iterative solvers
- Inverse design using deep learning

### 12.3.5 High-Performance Computing
- Parallel FDTD with domain decomposition + MPI
- Distributed MLFMA using hybrid MPI/OpenMP
- Cloud-based EM simulation
- Exascale computing: $10^{18}$ FLOPs

### 12.3.6 CEM at Extremes
- **Low frequency**: DC to daylight — special formulations for stable convergence
- **Ultra-high frequency**: Terahertz, photonics
- **Electrically large**: $>10^6\lambda$ (asymptotic + numerical hybridization)
- **Electrically small**: quantum EM effects

## 12.4 Summary: Choosing the Right Method

| Problem Type | Recommended Method | Why |
|:-------------|:------------------:|:----|
| Large, smooth scatterer ($\gg\lambda$) | PO/PTD, UTD, SBR | Asymptotic, very fast |
| Small-to-medium, complex geometry | FEM | Geometry flexibility, sparse matrix |
| Open region, homogeneous objects | MoM + MLFMA | Exact radiation condition, $O(N\log N)$ |
| Broadband, nonlinear | FDTD, FETD, DGTD | Single run, wideband |
| Inhomogeneous + complex | FE-BI, hybrid FEM/MoM | Best of both worlds |
| Circuit/package EMC | PEEC, FEM | Circuit-theory friendly |
| Biophotonics/nanophotonics | FDTD, FEM | Handles dispersion, nonlinearity |

## **Physical Intuition**
- No single "best" CEM method exists — the choice depends on problem geometry, frequency range, material properties, and desired accuracy.
- The trade-off between accuracy, speed, and generality is fundamental: asymptotic methods are fast but approximate, numerical methods are accurate but expensive.
- Hybrid methods try to have it all — use the right tool for each sub-region.

## **Numerical Intuition**
- $N \sim \lambda/h$: for $\lambda/10$ mesh, a $10\lambda\times10\lambda\times10\lambda$ volume has $10^6$ cells → 3M unknowns for VIE, but only $\sim 60$K for SIE.
- MLFMA makes $N\sim 10^7$ feasible today — a $100\lambda$ sphere needs $\sim 10^7$ unknowns and fits in $\sim 100$ GB.
- FDTD on GPU can run 1 billion cells/second — a $1000^3$ grid runs at $\sim 15$ time-steps/s.
- ML-accelerated solvers can provide $10\times$–$100\times$ speedup for parametric sweeps.

## **Audit Table**
| Section | Pages | Key Content | Verified |
|---------|-------|:-----------:|:--------:|
| 12.1 | 651–662 | CEM overview, method taxonomy | ✓ |
| 12.2 | 678–690 | Applications | ✓ |
| 12.3 | 690–704 | Challenges, future trends | ✓ |
