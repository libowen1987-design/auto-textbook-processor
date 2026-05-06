---
title: "Ch1: Mathematical Formulations for Electromagnetic Fields"
book: "Sheng & Song, Essentials of Computational Electromagnetics (2012)"
chapter: 1
pages: "1-28"
weight: 1
topics:
  - Maxwell's equations
  - Constitutive relations
  - Boundary conditions
  - Vector wave equation
  - Vector integral equation
  - Green's function
  - Layered medium
notes_version: "1.0"
---

# Chapter 1: Mathematical Formulations for Electromagnetic Fields

## 1.1 Deterministic Vector Partial Differential System of the Electromagnetic Fields

A complete system of vector partial differential equations for EM fields comprises three parts:

1. **Maxwell's equations** — the fundamental field equations
2. **Constitutive relations** — material responses (D, B to E, H)
3. **Boundary conditions** — field behavior at interfaces

### 1.1.1 Maxwell's Equations

In differential form (time domain):

$$
\nabla \times \mathbf{E} + \frac{\partial \mathbf{B}}{\partial t} = \mathbf{0} \quad \text{(Faraday's law)} \tag{1.1}
$$

$$
\nabla \times \mathbf{H} - \frac{\partial \mathbf{D}}{\partial t} = \mathbf{J} \quad \text{(Ampere's law with displacement current)} \tag{1.2}
$$

$$
\nabla \cdot \mathbf{D} = \rho \quad \text{(Gauss' law for electric fields)} \tag{1.3}
$$

$$
\nabla \cdot \mathbf{B} = 0 \quad \text{(Gauss' law for magnetic fields)} \tag{1.4}
$$

**Physical field quantities** (LHS):
- $\mathbf{E}$: electric field intensity $[\mathrm{V/m}]$
- $\mathbf{D}$: electric flux density $[\mathrm{C/m^2}]$
- $\mathbf{H}$: magnetic field intensity $[\mathrm{A/m}]$
- $\mathbf{B}$: magnetic flux density $[\mathrm{Wb/m^2}]$

**Source quantities** (RHS):
- $\mathbf{J}$: volume current density $[\mathrm{A/m^2}]$
- $\rho$: free volume charge density $[\mathrm{C/m^3}]$

**Charge conservation** (continuity equation):

$$
\nabla \cdot \mathbf{J} = -\frac{\partial \rho}{\partial t} \tag{1.5}
$$

**Key observation**: Only 3 of the 5 equations are independent. Applying $\nabla \cdot$ to (1.1) yields (1.4); applying $\nabla \cdot$ to (1.2) and using (1.5) yields (1.3).

**Practical selection**:
- Electrostatics: use (1.1) and (1.3) only
- Magnetostatics: use (1.2) and (1.3) only
- Time-varying EM waves: use (1.1) and (1.2) only

### 1.1.2 Constitutive Relations

For linear, isotropic materials:

$$
\mathbf{D} = \epsilon \mathbf{E} \tag{1.6}
$$

$$
\mathbf{B} = \mu \mathbf{H} \tag{1.7}
$$

$$
\mathbf{J} = \sigma \mathbf{E} \tag{1.8}
$$

Where:
- $\epsilon$ [F/m]: permittivity
- $\mu$ [H/m]: permeability
- $\sigma$ [S/m]: electrical conductivity

**Classification**:
| Property | Homogeneous | Non-homogeneous |
|----------|-------------|------------------|
| Definition | $\epsilon, \mu, \sigma$ constant in space | vary with position |
| Classification | Dispersive if parameters are frequency-dependent |

**Dispersive media examples**: plasma, water, biological tissues, wave-absorbing materials. In dispersive media, $\epsilon(\omega)$, $\mu(\omega)$ vary with frequency.

### 1.1.3 Boundary Conditions

At an interface between two media, the electromagnetic fields must satisfy:

**Tangential component continuity** (from Faraday's and Ampere's laws):

$$
\hat{n} \times (\mathbf{E}_2 - \mathbf{E}_1) = \mathbf{0} \quad \Rightarrow \quad E_{t2} = E_{t1} \tag{1.9}
$$

$$
\hat{n} \times (\mathbf{H}_2 - \mathbf{H}_1) = \mathbf{J}_s \quad \Rightarrow \quad H_{t2} - H_{t1} = J_s \tag{1.10}
$$

**Normal component discontinuity** (from Gauss' laws):

$$
\hat{n} \cdot (\mathbf{D}_2 - \mathbf{D}_1) = \rho_s \quad \Rightarrow \quad D_{n2} - D_{n1} = \rho_s \tag{1.11}
$$

$$
\hat{n} \cdot (\mathbf{B}_2 - \mathbf{B}_1) = 0 \quad \Rightarrow \quad B_{n2} = B_{n1} \tag{1.12}
$$

Where $\rho_s$ is surface charge density and $\mathbf{J}_s$ is surface current density.

**Special cases**:

1. **Perfect Electric Conductor (PEC)**: $\mathbf{E} = \mathbf{0}$, $\hat{n} \times \mathbf{H} = \mathbf{J}_s$
2. **Perfect Magnetic Conductor (PMC)**: $\mathbf{H} = \mathbf{0}$, $\hat{n} \times \mathbf{E} = -\mathbf{M}_s$

### 1.1.4 Maxwell's Equations in the Frequency Domain

Using phasor representation $\mathbf{E}(\mathbf{r}, t) = \mathrm{Re}\{\tilde{\mathbf{E}}(\mathbf{r}) e^{j\omega t}\}$, we obtain:

$$
\nabla \times \tilde{\mathbf{E}} = -j\omega \tilde{\mathbf{B}} \tag{1.107}
$$

$$
\nabla \times \tilde{\mathbf{H}} = \tilde{\mathbf{J}} + j\omega \tilde{\mathbf{D}} \tag{1.108}
$$

$$
\nabla \cdot \tilde{\mathbf{D}} = \tilde{\rho} \tag{1.109}
$$

$$
\nabla \cdot \tilde{\mathbf{B}} = 0 \tag{1.110}
$$

**Physical insight**: The $j\omega$ terms represent the displacement current — Maxwell's key addition to Ampere's law that enables wave propagation.

### 1.1.5 Uniqueness Theorem

**Theorem**: The electromagnetic field in a lossless region is uniquely determined by specifying either:
- The tangential electric field $\mathbf{E}_t$ on the boundary (Dirichlet condition), or
- The tangential magnetic field $\mathbf{H}_t$ on the boundary (Neumann condition)

**Implication for computational electromagnetics**: Knowing the boundary condition is sufficient to determine the field uniquely inside the domain. This forms the theoretical foundation for all numerical methods (MoM, FEM, FDTD).

---

## 1.2 Vector Wave Equation

From Maxwell's equations and constitutive relations, the electric field satisfies:

$$
\nabla \times \nabla \times \mathbf{E} - k^2 \mathbf{E} = -j\omega\mu \mathbf{J} \tag{1.41}
$$

where $k = \omega\sqrt{\mu\epsilon}$ is the wavenumber. This is the **vector Helmholtz equation**.

For a source-free region ($\mathbf{J} = 0$):

$$
\nabla \times \nabla \times \mathbf{E} - k^2 \mathbf{E} = \mathbf{0} \tag{1.42}
$$

Using the vector identity $\nabla \times \nabla \times \mathbf{E} = \nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E}$ and Coulomb gauge $\nabla \cdot \mathbf{E} = 0$ (source-free):

$$
\nabla^2 \mathbf{E} + k^2 \mathbf{E} = \mathbf{0} \tag{1.43}
$$

---

## 1.3 Vector Integral Equations

The integral equation formulation provides an alternative to partial differential equations, naturally satisfying the Sommerfeld radiation condition at infinity.

### 1.3.1 Equivalence Principle

**First form of equivalence** (exterior equivalent problem):
- Replace the original scatterer with PEC of the same shape
- Keep the same external field
- Introduce equivalent surface current $\mathbf{J}_s = \hat{n} \times \mathbf{H}$ and magnetic current $\mathbf{M}_s = -\hat{n} \times \mathbf{E}$

**Huygens' principle**: Fields in a source-free region can be expressed as integrals of tangential field components on a closed surface.

**Second form of equivalence** (interior equivalent problem):
- Replace interior region with the same medium as exterior
- Use equivalent currents $\mathbf{J} = -\hat{n} \times \mathbf{H}$, $\mathbf{M} = \hat{n} \times \mathbf{E}$
- Field inside equals original field; field outside is zero

### 1.3.2 Solution of Maxwell's Equation in Free Space

**Scalar Green's function** in free space (3D Helmholtz):

$$
G(\mathbf{r}, \mathbf{r}') = \frac{e^{-jk|\mathbf{r}-\mathbf{r}'|}}{4\pi|\mathbf{r}-\mathbf{r}'|} \tag{1.52}
$$

**Dyadic Green's function** for electric field:

$$
\overline{\overline{G}}_e(\mathbf{r}, \mathbf{r}') = \left(\overline{\overline{I}} + \frac{\nabla \nabla}{k^2}\right) G \tag{1.59}
$$

The electric field due to current distribution $\mathbf{J}$ in free space:

$$
\mathbf{E} = -j\omega\mu \int_V \overline{\overline{G}}_e \cdot \mathbf{J} \, dV' \tag{1.61}
$$

**Physical meaning**: The Green's function describes the field from a point source. The integral equation formulation sums contributions from all equivalent sources on the surface.

### 1.3.3 Integral Equations of Metallic Scattering Problems

For a PEC scatterer under plane wave incidence $\mathbf{E}^i$, the **Electric Field Integral Equation (EFIE)**:

$$
\mathbf{E}^i + \mathcal{L}(\mathbf{J}) = 0 \quad \text{on } S \tag{1.77}
$$

Where the operator $\mathcal{L}$ is:

$$
\mathcal{L}(\mathbf{J}) = j\omega\mu \int_S \left[ \mathbf{J} G + \frac{1}{k^2} \nabla \cdot \mathbf{J} \nabla G \right] dS' \tag{1.78}
$$

The **Magnetic Field Integral Equation (MFIE)**:

$$
\mathbf{J} - \hat{n} \times \mathcal{K}(\mathbf{J}) = \hat{n} \times \mathbf{H}^i \quad \text{on } S \tag{1.79}
$$

Where $\mathcal{K}$ is:

$$
\mathcal{K}(\mathbf{J}) = \int_S \mathbf{J} \times \nabla' G \, dS' \tag{1.80}
$$

**Numerical behavior**:
- EFIE: Fredholm integral equation of the **first kind** — ill-conditioned but accurate
- MFIE: Fredholm integral equation of the **second kind** — better conditioned, faster convergence in iterative solvers

### 1.3.4 Integral Equation of Homogeneous Dielectric Scattering Problems

For a homogeneous dielectric body with permittivity $\epsilon_1$ inside, $\epsilon_2$ outside, the PMCHW formulation (Peterson, Chew, Harrington, Wu, Chen) is widely used:

$$
\mathcal{L}_1(\mathbf{J}) + \mathcal{L}_2(-\mathbf{J}) + \mathcal{K}_1(\mathbf{M}) + \mathcal{K}_2(-\mathbf{M}) = -\mathbf{E}^i \tag{1.186}
$$

$$
\mathcal{K}_1(\mathbf{J}) + \mathcal{K}_2(-\mathbf{J}) - \frac{1}{Z_1}\mathcal{L}_1(\mathbf{M}) - \frac{1}{Z_2}\mathcal{L}_2(-\mathbf{M}) = -\mathbf{H}^i \tag{1.187}
$$

Where $Z_1 = \sqrt{\mu/\epsilon_1}$, $Z_2 = \sqrt{\mu/\epsilon_2}$ are wave impedances.

**Key insight**: The PMCHW system combines both interior and exterior operators in each equation, eliminating the interior resonance problem that affects single-equation formulations.

### 1.3.5 Integral Equation of Inhomogeneous Dielectric Scattering Problems

For inhomogeneous media, the **Volume Integral Equation (VIE)** is required:

$$
\mathbf{E}^i(\mathbf{r}) = \mathbf{E}(\mathbf{r}) - k_0^2 \int_V \overline{\overline{G}}(\mathbf{r}, \mathbf{r}') \cdot \chi(\mathbf{r}') \mathbf{E}(\mathbf{r}') \, dV' \tag{1.200}
$$

Where $\chi(\mathbf{r}) = \epsilon_r(\mathbf{r}) - 1$ is the contrast ratio.

### 1.3.6 Integral Equations of Scattering in Layered Medium

For a PEC scatterer embedded in a layered medium, the Green's function becomes more complex.

**Sommerfeld integration** (1D integral form):

$$
f(\mathbf{r}) = \frac{1}{2\pi} \int_0^\infty \tilde{f}(k_\rho) J_0(k_\rho \rho) k_\rho \, dk_\rho \tag{1.115}
$$

The **mixed-potential expression** for the electric field:

$$
\mathbf{E} = -j\omega\mu \int_V \overline{\overline{G}}_A \cdot \mathbf{J} \, dV + \frac{1}{j\omega\epsilon} \nabla \int_V K \nabla' \cdot \mathbf{J} \, dV' + \int_V C \mathbf{J}_z \, dV' \tag{1.162}
$$

**Physical meaning**: The layered medium Green's function accounts for multiple reflections between interfaces. The Sommerfeld integration represents a spectral decomposition into cylindrical waves.

**Numerical challenge**: Direct evaluation of Sommerfeld integrals is computationally expensive. Special techniques (e.g., fast far-field approximation, discrete complex image method) are required for efficient evaluation.

---

## Key Equations Summary

| Equation | Type | Physical Meaning |
|----------|-------|------------------|
| (1.1)-(1.4) | PDE system | Maxwell's equations in time domain |
| (1.6)-(1.8) | Constitutive | Material response (D, B to E, H) |
| (1.9)-(1.12) | BC | Field discontinuity at interfaces |
| (1.77) | Integral | EFIE for PEC scatterer |
| (1.79) | Integral | MFIE for PEC scatterer |
| (1.115) | Integral | Sommerfeld integration (layered medium) |

---

## Problems

1.6 Prove the relation $\nabla_t = -j\mathbf{k}_\rho$ used in deriving (1.116)–(1.119).

1.7 Prove the reciprocity relations (1.134) for the transmission-line equations.

---

## References

1. Senior, T.B.A. (1960) "Impedance boundary conditions for imperfectly conducting surface." Applied Scientific Research, Section B, 8, 418–436.
2. Peterson, A.F., Ray, S.L., and Mittra, R. (1998) Computational Methods for Electromagnetics, IEEE Press, New York.
3. Ise, K., Inoue, K., and Koshiba, M. (1990) "Three-dimensional finite-element solution of dielectric scattering obstacles in a rectangular waveguide." IEEE Transactions on Antennas and Propagation, 38(9), 1352–1359.
4. Stratton, J.A. (1941) Electromagnetic Theory, McGraw-Hill, New York.
5. Harrington, R.F. (1961) Time-Harmonic Electromagnetic Fields, McGraw-Hill, New York.
6. Tai, C.T. (1971) Dyadic Green's Functions in Electromagnetic Theory, International Textbook Company.
7. Michalski, K.A. and Mosig, J.R. (1997) "Multilayered media Green's functions in integral equation formulations." IEEE Transactions on Antennas and Propagation, 45(3), 508–519.
8. Aksun, M.I. (1996) "A Robust Approach for the Derivation of Closed-form Green's Functions." IEEE Transactions on Microwave Theory and Techniques, 44(5), 651–658.