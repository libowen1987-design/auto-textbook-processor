---
title: "Ch5: Hybrid Methods"
book: "Sheng & Song, Essentials of Computational Electromagnetics (2012)"
chapter: 5
pages: "248-285"
weight: 5
topics:
  - PO-FEM hybrid
  - PO-MoM hybrid
  - FE-BI-MLFMA
  - CFIE formulations (TENH, NETH, TETH, NENH)
  - Mode-matching hybrid
  - SBR (Shooting-Bouncing Ray)
notes_version: "1.0"
---

# Chapter 5: Hybrid Methods

There are many numerical methods for EM computation, roughly categorized into:

1. **High-frequency asymptotic methods**: PO (Physical Optics), GO (Geometrical Optics), GTD (Geometrical Theory of Diffraction), PTD (Physical Theory of Diffraction), SBR (Shooting-Bouncing Ray)
2. **Full-wave numerical methods**: MoM, FEM, FDTD

Each method has distinct advantages and disadvantages. For practical problems, a single method may suffer from either **inaccuracy** or **low efficiency**. Hybrid methods combine different numerical methods to achieve accurate and efficient results.

Two types of hybridization in CEM:

1. **Domain decomposition** (equivalence principle): Partition domain into subregions, apply different methods to each. Example: **FE-BI (Finite Element–Boundary Integral)**.
2. **Dimension separation** (mode theory/variable separation): Apply different methods for different dimensions. Example: **Mode-matching method**.

## 5.1 Hybrid High-Frequency Asymptotic + Full-Wave Methods

### 5.1.1 Hybrid PO-FEM Method (Cavity Problem)

**Problem**: Electrically large PEC scatterer with a dielectric-filled cavity. The PEC body size is tens to hundreds of wavelengths, while the cavity is only a few wavelengths.

#### 5.1.1.1 Idea

Partition the computational domain into two parts using the **equivalence principle**:

1. **Exterior region** (cavity exterior): Replace cavity with PEC. Calculate scattering of the large PEC body with coexistence of incident wave and equivalent magnetic current $\mathbf{M}$. Apply **PO method** (high-frequency asymptotic).
2. **Interior region** (cavity interior): Apply **FEM** for accurate solution.

#### 5.1.1.2 PO Solution in Exterior Region

The total scattering field outside the cavity:

$$
\mathbf{H} = \mathbf{H}_{po} + \mathbf{H}_m \tag{5.6}
$$

**PO magnetic field** (from incident wave):

$$
\mathbf{H}_{po} = -\int_S \mathbf{J}_{po} \times \nabla G_0 \, dS' \tag{5.1}
$$

where

$$
\mathbf{J}_{po} = \begin{cases} 2\hat{n} \times \mathbf{H}^i(\mathbf{r}) & \mathbf{r} \in S_{\text{slit}} \\ 0 & \mathbf{r} \in S_{\text{dark}} \end{cases} \tag{5.2}
$$

**Scattering from equivalent magnetic current** $\mathbf{M}$:

$$
\mathbf{H}_m = -jk_0 Y_0 \int_{S_a} \overline{\overline{G}} \cdot \mathbf{M} \, dS' \tag{5.3}
$$

where $S_a$ is the open section of the cavity, and $\overline{\overline{G}}$ is approximated by the **half-space dyadic Green's function**:

$$
\overline{\overline{G}}_h(\mathbf{r}, \mathbf{r}') = G_0(\mathbf{r}, \mathbf{r}') \overline{\overline{I}} - G_0(\mathbf{r}, \mathbf{r}'_i) \overline{\overline{I}} + 2\hat{n}_a\hat{n}_a G_0(\mathbf{r}, \mathbf{r}'_i) \tag{5.4}
$$

where $\mathbf{r}'_i$ is the mirror image of $\mathbf{r}'$ with respect to the outward normal $\hat{n}_a$, and

$$
G_0(\mathbf{r}, \mathbf{r}') = \frac{e^{-jk_0|\mathbf{r}-\mathbf{r}'|}}{4\pi|\mathbf{r}-\mathbf{r}'|} \overline{\overline{I}} - \frac{1}{k_0^2} \nabla \nabla \tag{5.5}
$$

#### 5.1.1.3 FEM Solution Inside the Cavity

The field inside the cavity satisfies the variational problem:

$$
F(\mathbf{E}) = \frac{1}{2} \int_V \left[ \frac{1}{\mu_r} (\nabla \times \mathbf{E}) \cdot (\nabla \times \mathbf{E}^*) - k_0^2 \epsilon_r \mathbf{E} \cdot \mathbf{E}^* \right] dV + jk_0 Z_0 \int_{S_a} (\hat{n} \times \mathbf{E}) \cdot \mathbf{H} \, dS \tag{5.7}
$$

where $V$ is the cavity interior and $S_a$ is the open section.

Substituting the exterior field expression (5.6) into (5.7):

$$
F(\mathbf{E}) = \frac{1}{2} \int_V \left[ \frac{1}{\mu_r} (\nabla \times \mathbf{E}) \cdot (\nabla \times \mathbf{E}^*) - k_0^2 \epsilon_r \mathbf{E} \cdot \mathbf{E}^* \right] dV - k_0^2 \int_{S_a} (\hat{n} \times \mathbf{E}) \cdot \int_{S_a} \overline{\overline{G}} \cdot (\hat{n} \times \mathbf{E}) \, dS' \, dS + jk_0 Z_0 \int_{S_a} (\hat{n} \times \mathbf{E}) \cdot \mathbf{H}_{po} \, dS \tag{5.8}
$$

Mesh the domain $V$ into tetrahedral elements with edge basis functions $\mathbf{N}_j$:

$$
\mathbf{E} = \sum_{j=1}^{N} \mathbf{N}_j E_j \tag{5.9}
$$

Discretization yields:

$$
\mathbf{K} \cdot \mathbf{E} = \mathbf{b} \tag{5.10}
$$

where

$$
K_{ij} = \frac{1}{2} \int_V \left[ \frac{1}{\mu_r} (\nabla \times \mathbf{N}_i) \cdot (\nabla \times \mathbf{N}_j) - k_0^2 \epsilon_r \mathbf{N}_i \cdot \mathbf{N}_j \right] dV - k_0^2 \int_{S_a} (\hat{n} \times \mathbf{N}_i) \cdot \int_{S_a} \overline{\overline{G}} \cdot (\hat{n} \times \mathbf{N}_j) \, dS' \, dS \tag{5.11}
$$

$$
b_j = -jk_0 Z_0 \int_{S_a} (\hat{n} \times \mathbf{N}_j) \cdot \mathbf{H}_{po} \, dS \tag{5.12}
$$

#### 5.1.1.4 Far-Field Scattering Calculation

The far-zone scattering field from the equivalent magnetic current $\mathbf{M}$ is obtained using the **reciprocity principle**:

$$
\mathbf{E}_{sc}^{y,f} = \frac{jk_0 Z_0 e^{-jk_0 r}}{4\pi r} \int_{S_a} \mathbf{M} \cdot \mathbf{H}_{po}^{v,h} \, dS \tag{5.15}
$$

where $\mathbf{H}_{po}^v$ and $\mathbf{H}_{po}^h$ are the scattered magnetic fields by the electrically large body (without cavity) under vertical and horizontal polarization incidences, respectively.

**Why reciprocity?** Because we don't have the exact dyadic Green's function $G$ for the PEC body with cavity — reciprocity allows us to use $\mathbf{H}_{po}$ computed from PO as the testing function.

#### 5.1.1.5 Numerical Example

**Metallic cube with slot**: Cube size $5\lambda \times 5\lambda \times 5\lambda$. Slot on upper surface: length $5\lambda$, width $0.2\lambda$, depth $0.25\lambda$.

Results from hybrid PO-FEM and MoM show good agreement, demonstrating satisfactory accuracy.

---

### 5.1.2 Hybrid PO-MoM Method (Protrusion Problem)

**Problem**: Electrically large PEC object with a protrusion (small compared to the body).

#### 5.1.2.1 Model

The smooth PEC body (without protrusion) has known PO solution. The protrusion introduces an **equivalent electric current** $\mathbf{J}$.

At the connection section (interface between PEC body and protrusion):

$$
\mathbf{E}_s - jk_0 \int_{S_p} \overline{\overline{G}} \cdot \mathbf{J} \, dS' \Big|_{\text{tangential}} = 0 \tag{5.16}
$$

The equivalent current $\mathbf{J}$ is solved using MoM (method of moments), and the far-zone scattered field is computed using reciprocity:

$$
\mathbf{E}_{sc}^{y,f} = -\frac{jk_0 e^{-jk_0 r}}{4\pi r} \int_{S_p} \mathbf{J} \cdot \mathbf{E}_{po}^{v,h} \, dS \tag{5.17}
$$

where $\mathbf{E}_{po}^v$ and $\mathbf{E}_{po}^h$ are the scattered electric fields by the smooth PEC body under two polarizations.

**Numerical example**: Rectangular block $8\lambda \times 8\lambda \times 1\lambda$ with two PEC patches ($2\lambda \times 2\lambda$ and $1\lambda \times 1\lambda$) on top.

---

## 5.2 Hybrid Full-Wave Numerical Methods

### 5.2.1 Hybrid FE-BI-MLFMA

**Problem**: Scattering by a coated metallic object (stealth aircraft design).

**Challenges with single methods**:
- **VIEs with FFT**: Inefficient because metallic region (where fields are null) is difficult to exclude from the computational domain
- **FEM/FDTD alone**: Absorbing boundary must be placed far from coating → larger domain, more unknowns, approximate ABC

#### 5.2.1.1 Idea

Partition the domain using the **equivalence principle**:

1. **Interior** (between metallic surface $S_i$ and coating outer surface $S_e$): Apply FEM (tetrahedral mesh, edge elements)
2. **Exterior** (free space outside $S_e$): Apply MoM (boundary integral on $S_e$)
3. **Connection**: Huygens' equivalence principle links FEM and MoM through surface unknowns on $S_e$

The method is called **FE-BI (Finite Element–Boundary Integral)**.

#### 5.2.1.2 Formulation

**FEM functional** (interior region $V$, between $S_i$ and $S_e$):

$$
F(\mathbf{E}) = \frac{1}{2} \int_V \left[ \frac{1}{\mu_r} (\nabla \times \mathbf{E}) \cdot (\nabla \times \mathbf{E}^*) - k_0^2 \epsilon_r \mathbf{E} \cdot \mathbf{E}^* \right] dV + jk_0 \int_{S_0} \mathbf{E} \times (\overline{\overline{I}} - \hat{n}\hat{n}) \cdot \mathbf{H}^* \, dS \tag{5.18}
$$

where $S_0 = S_e$, $\hat{n}$ points outward from $V$, and $\overline{\overline{I}} - \hat{n}\hat{n}$ projects onto the tangential component.

Discretization with edge elements on tetrahedra:

$$
\mathbf{E} = \sum_{i=1}^{3} \mathbf{N}_i E_i \quad \text{on each triangular surface} \tag{5.24}
$$

$$
\overline{\overline{I}} - \hat{n}\hat{n}) \cdot \mathbf{H}^* = -\sum_{i=1}^{3} \hat{n} \times \mathbf{N}_i H_i^* \quad \text{(triangular elements on boundary)} \tag{5.25}
$$

The equivalent currents are:

$$
\mathbf{M} = -\hat{n} \times \mathbf{E} \tag{5.23}
$$

$$
\overline{\overline{I}} - \hat{n}\hat{n}) \cdot \mathbf{H}^* = -\hat{n} \times \mathbf{H}^* = \mathbf{J}^* \quad \text{(since } \mathbf{J} = \hat{n} \times \mathbf{H} \text{)} \tag{5.22}
$$

On the triangular boundary surface, $\hat{n} \times \mathbf{N}_i$ are exactly the **RWG (Rao-Wilton-Glisson) basis functions** $g_i$ (proved in Problem 3.6).

The discrete system:

$$
\begin{pmatrix} \mathbf{K}_{II} & \mathbf{K}_{IS} \\ \mathbf{K}_{SI} & \mathbf{K}_{SS} \end{pmatrix} \begin{pmatrix} \mathbf{E}_I \\ \mathbf{E}_S \end{pmatrix} + \begin{pmatrix} 0 \\ \mathbf{B} \end{pmatrix} \begin{pmatrix} \mathbf{E}_I \\ -\mathbf{H}_S \end{pmatrix} = \begin{pmatrix} 0 \\ \mathbf{b} \end{pmatrix} \tag{5.19}
$$

or compactly:

$$
\begin{pmatrix} \mathbf{K}_{II} & \mathbf{K}_{IS} & 0 \\ \mathbf{K}_{SI} & \mathbf{K}_{SS} & \mathbf{B} \\ 0 & \mathbf{P} & \mathbf{Q} \end{pmatrix} \begin{pmatrix} \mathbf{E}_I \\ \mathbf{E}_S \\ -\mathbf{H}_S \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ \mathbf{b} \end{pmatrix} \tag{5.29}
$$

where $\mathbf{P}\mathbf{E}_S + \mathbf{Q}(-\mathbf{H}_S) = \mathbf{b}$ is the **Combined Field Integral Equation (CFIE)**.

**CFIE options**: Four schemes (from EFIE and MFIE combinations):

| Scheme | Formulation | Interior Resonance |
|--------|-------------|-------------------|
| TETH | EFIE tested with RWG + MFIE tested with RWG | Suffers |
| TENH | EFIE tested with RWG + MFIE tested with $\hat{n} \times$ RWG | **Free** |
| NETH | EFIE tested with $\hat{n} \times$ RWG + MFIE tested with RWG | Poor convergence |
| NENH | EFIE tested with $\hat{n} \times$ RWG + MFIE tested with $\hat{n} \times$ RWG | Suffers |

The **TENH** scheme has the best condition number and is recommended for FE-BI-MLFMA.

**Matrix structure analysis** (for understanding convergence):

| Operator | Dominance |
|----------|-----------|
| $\mathbf{Q}_{TE}$, $\mathbf{P}_{TH}$ | Diagonally strongly dominant |
| $\mathbf{Q}_{NE}$, $\mathbf{Q}_{NH}$ | Diagonally weakly dominant |
| $\mathbf{P}_{TE}$, $\mathbf{Q}_{TH}$, $\mathbf{Q}_{NE}$, $\mathbf{P}_{NH}$ | Off-diagonally dominant |

The TENH scheme yields the best-conditioned combined matrix because it optimally balances diagonal and off-diagonal dominance.

#### 5.2.1.3 Solution and Complexity

Using **conjugate gradient (CG) iteration** with **MLFMA** (Multilevel Fast Multipole Algorithm) to accelerate the MoM matrix-vector products:

- **Memory**: $O(N_v + N_s \lg N_s)$
- **Per iteration cost**: $O(N_v + N_s \lg N_s)$
- **Convergence**: Fast for well-conditioned formulations (TENH)

**Algorithm A** (direct CG with MLFMA): Standard approach but may converge slowly due to large condition number of FEM part.

**Preconditioning** (Algorithm B): Precondition the FEM coefficient matrix by LU decomposition:

$$
\mathbf{K} = \mathbf{L} \mathbf{U} \tag{5.35}
$$

This reduces the condition number and accelerates convergence significantly.

#### 5.2.1.4 Numerical Results

Examples include coated spheres (metallic sphere with dielectric coating) verified against Mie series solution. The results show excellent agreement with high efficiency.

---

## 5.3 Straight-Line Method (Mode Matching)

For waveguide discontinuities and cascading problems, the **straight-line method** separates dimensions and applies different methods in each:

- **Transverse direction**: Galerkin method (MoM or FEM) — solves for modal field patterns
- **Propagation direction**: Analytical propagation of modal amplitudes using transmission-line theory

This is a hybrid of **mode-matching** (analytical in propagation direction) and **numerical** (Galerkin in transverse direction).

---

## Key Equations Summary

| Equation | Physical Meaning |
|----------|-----------------|
| (5.1) | PO magnetic field from incident wave |
| (5.2) | PO surface current on illuminated portion |
| (5.3) | Scattering from equivalent magnetic current |
| (5.6) | Total exterior field (PO + magnetic current) |
| (5.7) | FEM functional for cavity interior |
| (5.10) | Linear system from FEM discretization |
| (5.16) | Integral equation for equivalent electric current (protrusion) |
| (5.18) | FE-BI functional for coated scatterer |
| (5.29) | Combined FE-BI-CFIE matrix equation |
| (5.35) | LU decomposition for FEM preconditioning |

---

## Problems

**5.1** Derive the 2D formulation of the hybrid PO-FE method analogous to the 3D case in Section 5.1.1.

**5.2** Write a program of the hybrid PO-FE method for scattering by a 2D large target with a cavity.

**5.3** Write a program of the hybrid PO-FE method for scattering by a 3D large target with a cavity.

**5.4** Compare the accuracy of methods for computing RCS between using the reciprocity principle and the half-Green's function approximation.

**5.5** Derive the 2D formulation of the hybrid PO-MoM method analogous to the 3D case in Section 5.1.2.

**5.6** Write a program of the hybrid PO-MoM method for scattering by a 2D large target with a protrusion.

---

## References

[1] Thiele, G.A. (1975) Architecture and implementation of the thin-wire moment method. IEEE Antennas and Propagation Magazine, 17, 9–14.
[2] Jakobus, U. and Landqvist, F. (1995) Extension of a combined FEM/MoM approach for dielectric scattering problems. IEEE Transactions on Antennas and Propagation, 43, 1313–1318.
[3] Jin, J.M., Ni, S., and Lee, S.W. (1995) Hybridization of SBR and FEM for scattering by large bodies with cracks and cavities. IEEE Transactions on Antennas and Propagation, 43, 1130–1139.
[4] Jin, J.M., Ling, F., Carolan, S. et al. (1998) A hybrid SBR/MoM for analysis of scattering by small protrusion on a large conducting body. IEEE Transactions on Antennas and Propagation, 46, 1349–1357.
[5] Sheng, X.Q., Jin, J.M., Song, J.M. et al. (1998) On the formulation of hybrid finite-element boundary-integral methods for 3D scattering. IEEE Transactions on Antennas and Propagation, 46, 303–311.
[6] Jin, J.M. (2010) The Finite Element Method in Electromagnetics, 2nd edn, Wiley, New York.