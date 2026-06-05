# Taflove & Hagness — Computational Electrodynamics: The FDTD Method (3rd Ed.)

> Allen Taflove, Susan C. Hagness. Artech House, 2005. ISBN 1-58053-832-0.

---

## Table of Contents

- [Part I: Maxwell's Yee Algorithm](#part-i-maxwells-yee-algorithm)
  - [1.1 The Yee Grid](#11-the-yee-grid)
  - [1.2 1D FDTD Update Equations](#12-1d-fdtd-update-equations)
  - [1.3 2D and 3D Update Equations](#13-2d-and-3d-update-equations)
  - [1.4 Numerical Dispersion](#14-numerical-dispersion)
  - [1.5 Stability: The Courant Condition](#15-stability-the-courant-condition)
- [Part II: Absorbing Boundary Conditions](#part-ii-absorbing-boundary-conditions)
  - [2.1 Mur Absorbing Boundary Conditions](#21-mur-absorbing-boundary-conditions)
  - [2.2 Berenger's Split-Field PML](#22-berengers-split-field-pml)
  - [2.3 Uniaxial PML (UPML)](#23-uniaxial-pml-upml)
  - [2.4 Convolutional PML (CPML)](#24-convolutional-pml-cpml)
- [Part III: Source Excitation & Near-to-Far-Field](#part-iii-source-excitation--near-to-far-field)
  - [3.1 Total-Field / Scattered-Field Formulation](#31-total-field--scattered-field-formulation)
  - [3.2 Hard and Soft Sources](#32-hard-and-soft-sources)
  - [3.3 Time-Harmonic and Broadband Sources](#33-time-harmonic-and-broadband-sources)
  - [3.4 Near-to-Far-Field Transformation](#34-near-to-far-field-transformation)
- [Part IV: Dispersive, Nonlinear & Gain Media](#part-iv-dispersive-nonlinear--gain-media)
  - [4.1 Debye, Drude, and Lorentz Models](#41-debye-drude-and-lorentz-models)
  - [4.2 Auxiliary Differential Equation (ADE) Method](#42-auxiliary-differential-equation-ade-method)
  - [4.3 Recursive Convolution (RC) and PLRC Methods](#43-recursive-convolution-rc-and-plrc-methods)
  - [4.4 Nonlinear and Gain Media](#44-nonlinear-and-gain-media)
- [Part V: Applications](#part-v-applications)
  - [5.1 Scattering](#51-scattering)
  - [5.2 Antennas and Microwave Circuits](#52-antennas-and-microwave-circuits)
  - [5.3 Photonics](#53-photonics)
  - [5.4 Bioelectromagnetics](#54-bioelectromagnetics)
- [Key Equations Reference](#key-equations-reference)

---

## Part I: Maxwell's Yee Algorithm

### 1.1 The Yee Grid

**Core idea:** Discretize space and time such that the electric and magnetic field components are interleaved on a staggered grid. Each E-field component is surrounded by four circulating H-field components, and vice versa — a natural fit for Faraday's and Ampère's laws in integral form.

**Yee cell (3D):** A unit cube of size Δx × Δy × Δz. Field components are placed as:

- E_x at (i+½, j,   k  )
- E_y at (i,   j+½, k  )
- E_z at (i,   j,   k+½)
- H_x at (i,   j+½, k+½)
- H_y at (i+½, j,   k+½)
- H_z at (i+½, j+½, k  )

**Temporal staggering:**
- E-field updates occur at integer time steps: t = n·Δt
- H-field updates occur at half-integer time steps: t = (n+½)·Δt

This yields the **leapfrog** time-stepping scheme.

### 1.2 1D FDTD Update Equations

Assume TEM wave propagating along z, with E_x and H_y components:

**Electric field update (E_x):**

$$E_x^{n+1}(k) = E_x^n(k) + \frac{\Delta t}{\epsilon \Delta z} \left[H_y^{n+1/2}(k+\tfrac12) - H_y^{n+1/2}(k-\tfrac12)\right]$$

**Magnetic field update (H_y):**

$$H_y^{n+1/2}(k+\tfrac12) = H_y^{n-1/2}(k+\tfrac12) + \frac{\Delta t}{\mu \Delta z} \left[E_x^{n}(k+1) - E_x^{n}(k)\right]$$

These are obtained by central-differencing Faraday's and Ampère's laws in 1D.

### 1.3 2D and 3D Update Equations

**2D TM_z mode** (E_z, H_x, H_y non-zero):

$$E_z^{n+1}(i,j) = E_z^n(i,j) + \frac{\Delta t}{\epsilon}\left[\frac{H_y^{n+1/2}(i+\tfrac12,j) - H_y^{n+1/2}(i-\tfrac12,j)}{\Delta x} - \frac{H_x^{n+1/2}(i,j+\tfrac12) - H_x^{n+1/2}(i,j-\tfrac12)}{\Delta y}\right]$$

$$H_x^{n+1/2}(i,j+\tfrac12) = H_x^{n-1/2}(i,j+\tfrac12) - \frac{\Delta t}{\mu}\left[\frac{E_z^{n}(i,j+1) - E_z^{n}(i,j)}{\Delta y}\right]$$

$$H_y^{n+1/2}(i+\tfrac12,j) = H_y^{n-1/2}(i+\tfrac12,j) + \frac{\Delta t}{\mu}\left[\frac{E_z^{n}(i+1,j) - E_z^{n}(i,j)}{\Delta x}\right]$$

**3D update equations** (general case, using notation from Taflove Ch. 3):

For a medium with electric conductivity σ and magnetic conductivity σ*:

$$E_x|^{n+1}_{i+\tfrac12,j,k} = \frac{1 - \frac{\sigma\Delta t}{2\epsilon}}{1 + \frac{\sigma\Delta t}{2\epsilon}} \, E_x|^n_{i+\tfrac12,j,k} + \frac{\Delta t/\epsilon}{1 + \frac{\sigma\Delta t}{2\epsilon}} \left[\frac{H_z|^{n+\tfrac12}_{i+\tfrac12,j+\tfrac12,k} - H_z|^{n+\tfrac12}_{i+\tfrac12,j-\tfrac12,k}}{\Delta y} - \frac{H_y|^{n+\tfrac12}_{i+\tfrac12,j,k+\tfrac12} - H_y|^{n+\tfrac12}_{i+\tfrac12,j,k-\tfrac12}}{\Delta z}\right]$$

The remaining five components (E_y, E_z, H_x, H_y, H_z) follow by cyclic permutation.

### 1.4 Numerical Dispersion

**The FDTD grid introduces a non-physical dispersion relation.** For a uniform grid (Δx = Δy = Δz = δ):

$$\left[\frac{1}{c\Delta t}\sin\left(\frac{\omega\Delta t}{2}\right)\right]^2 = \sum_{\alpha=x,y,z} \left[\frac{1}{\delta}\sin\left(\frac{k_\alpha\delta}{2}\right)\right]^2$$

Key consequences:

- **Numerical phase velocity ≠ c.** It depends on frequency, propagation direction, and grid resolution.
- **Grid anisotropy:** Waves travel at different speeds in different directions.
- **Mitigation:** Use at least 10–20 cells per wavelength (Δ ≤ λ/10 to λ/20).

For the 1D case:

$$\frac{1}{c\Delta t}\sin\left(\frac{\omega\Delta t}{2}\right) = \frac{1}{\Delta z}\sin\left(\frac{k_z\Delta z}{2}\right)$$

### 1.5 Stability: The Courant Condition

**Courant-Friedrichs-Lewy (CFL) stability condition:**

For 1D: $$S_c = \frac{c\Delta t}{\Delta z} \leq 1$$

For 2D: $$S_c = c\Delta t \sqrt{\frac{1}{\Delta x^2} + \frac{1}{\Delta y^2}} \leq 1$$

For 3D: $$S_c = c\Delta t \sqrt{\frac{1}{\Delta x^2} + \frac{1}{\Delta y^2} + \frac{1}{\Delta z^2}} \leq 1$$

The **Courant number** S_c is the ratio of the physical distance a wave travels in one time step to the grid spacing. For uniform cubes (Δ = δ):

- 1D: c·Δt ≤ δ
- 2D: c·Δt ≤ δ/√2
- 3D: c·Δt ≤ δ/√3

**In practice:** Choose S_c = 0.5 for safety margin.

---

## Part II: Absorbing Boundary Conditions

### 2.1 Mur Absorbing Boundary Conditions

**First-order Mur ABC** (for 1D, z-direction):

At z = 0 boundary, the wave equation ∂E_x/∂t − c·∂E_x/∂z = 0 (absorbing left-traveling waves):

$$E_x^{n+1}(1) = E_x^n(2) + \frac{c\Delta t - \Delta z}{c\Delta t + \Delta z}\left[E_x^{n+1}(2) - E_x^n(1)\right]$$

**Second-order Mur ABC** (for 2D/3D): Uses both spatial derivatives to absorb waves at wider angles. Derivation starts from the 2D wave equation factorized into outgoing and incoming wave operators. The second-order formulation cancels normal derivatives up to the second order.

**Limitations:** Mur ABCs work well only for near-normal incidence. Performance degrades at grazing angles.

### 2.2 Berenger's Split-Field PML

**Key insight:** Split each field component into two sub-components (e.g., E_z → E_zx + E_zy) and introduce artificial anisotropic electric/magnetic conductivities (σ_x, σ_y, σ_z) that absorb waves without reflection.

In the PML region (e.g., x-direction):

$$E_{zx}\text{ update:}\quad \frac{\partial E_{zx}}{\partial t} + \frac{\sigma_x}{\epsilon_0}E_{zx} = \frac{1}{\epsilon_0}\frac{\partial H_y}{\partial x}$$

$$E_{zy}\text{ update:}\quad \frac{\partial E_{zy}}{\partial t} + \frac{\sigma_y}{\epsilon_0}E_{zy} = -\frac{1}{\epsilon_0}\frac{\partial H_x}{\partial y}$$

**Impedance matching condition:** For a reflectionless interface, the electric and magnetic conductivities must satisfy:

$$\frac{\sigma_x}{\epsilon_0} = \frac{\sigma_x^*}{\mu_0}$$

**Polynomial grading:** To minimize numerical reflections at the PML/internal interface, conductivity is gradually increased from the interface:

$$\sigma_x(x) = \sigma_{\max} \cdot \left(\frac{x}{d}\right)^m$$

where d is the PML thickness and m is the grading order (typically 2–4).

**Reflection error:** Theoretical normal-incidence reflection coefficient:

$$R(0) = e^{-2\eta_0\sigma_{\max}d/(m+1)}$$

### 2.3 Uniaxial PML (UPML)

UPML replaces the split-field formulation with an equivalent anisotropic material:

$$\mathbf{D} = \epsilon_0 \epsilon_r \mathbf{s} \cdot \mathbf{E}, \quad \mathbf{B} = \mu_0 \mu_r \mathbf{s} \cdot \mathbf{H}$$

where the diagonal tensor is:

$$\mathbf{s} = \begin{bmatrix} \frac{s_y s_z}{s_x} & 0 & 0 \\ 0 & \frac{s_z s_x}{s_y} & 0 \\ 0 & 0 & \frac{s_x s_y}{s_z} \end{bmatrix}$$

and each s_α = 1 + σ_α/(jωε₀) in the frequency domain.

**Advantages:** UPML is simpler to implement than split-field PML and more physically intuitive. Works directly with Maxwell's curl equations in anisotropic media.

### 2.4 Convolutional PML (CPML)

**CPML uses the complex-frequency-shifted (CFS) tensor:**

$$s_\alpha = \kappa_\alpha + \frac{\sigma_\alpha}{\alpha_\alpha + j\omega\epsilon_0}$$

where κ_α ≥ 1 and α_α is a frequency-shift parameter.

**Key advantage:** CPML works well for low-frequency fields, evanescent waves, and late-time interactions. It is implemented by converting the multiplication by s_α in the frequency domain to a convolution in the time domain:

$$D_x = \epsilon_0 E_x + \epsilon_0 \tilde{\sigma}_x(t) * E_x$$

where \(\tilde{\sigma}_x(t)\) is the inverse Fourier transform of (s_x − 1).

The convolution is efficiently computed using **recursive convolution (RC)** with exponential functions, requiring only 2–3 additional auxiliary arrays per field component per PML layer. This makes CPML the most versatile and widely used ABC in modern FDTD.

**Recommended parameters** (Taflove 3rd Ed., Ch. 7):
- PML thickness: 8–16 cells
- σ_opt = σ_max (with σ_max ≈ 0.8 × (m+1)/(η₀ d) for polynomial grading)
- κ_max = 1–11 (typically 1 for internal, 5–11 at outer boundary)
- α_opt = 0.08–0.8 (reduces late-time reflections from low-frequency evanescent waves)

---

## Part III: Source Excitation & Near-to-Far-Field

### 3.1 Total-Field / Scattered-Field Formulation

**TFSF divides the grid into two regions:**
- **Total-field (TF) region:** Contains both incident and scattered fields
- **Scattered-field (SF) region:** Contains only scattered fields

They are separated by a **Huygens surface** (the TF/SF boundary) where the incident field is injected.

**Implementation:**
1. Update all E and H fields using standard FDTD equations everywhere
2. On the TF/SF boundary, **correct** the fields by adding/subtracing the incident field:

For example, on the left side of the TF/SF boundary (x = x₀ interface for 2D TM_z):

$$E_z^{n+1}_{\text{corr}}(i_0,j) = E_z^{n+1}_{\text{std}}(i_0,j) - \frac{\Delta t}{\epsilon \Delta x} H_{y,\text{inc}}^{n+½}(i_0-\tfrac12,j)$$

### 3.2 Hard and Soft Sources

**Hard source:** Directly set E(t) at a grid point to a prescribed time function:
$$E_z^n(i_0,j_0) = f(n\Delta t)$$

Simple but reflects waves back into the domain. Only suitable for short pulses or when reflections are desired.

**Soft source (additive source):** Add the source term to the standard update equation:
$$E_z^{n+1}(i_0,j_0) = E_z^{n+1}_{\text{std}}(i_0,j_0) + \text{source term}$$

The source term equals the current density J_s that would produce the desired field. An incident plane-wave source is naturally implemented through TFSF.

**Resistive source:** Add a source with an equivalent series resistance to absorb reflections.

### 3.3 Time-Harmonic and Broadband Sources

**Gaussian pulse** (broadband):

$$f(t) = e^{-\frac{(t-t_0)^2}{T^2}}$$

Useful for broadband frequency response. Frequency content extends from DC to f_max ≈ 1/(πT).

**Differentiated (Ricker) wavelet:**

$$f(t) = \left[1 - 2\left(\frac{t-t_0}{T}\right)^2\right] e^{-\frac{(t-t_0)^2}{T^2}}$$

No DC component. Also called "Mexican hat" wavelet.

**Modulated Gaussian pulse:**

$$f(t) = \sin(\omega_c(t-t_0)) \cdot e^{-\frac{(t-t_0)^2}{T^2}}$$

Band-limited around ω_c. Used for narrowband RCS and antenna calculations.

**TFSF setup for plane-wave injection:**
- Compute incident field analytically on the Huygens surface
- Apply corrections to E and H adjacent to the surface
- For arbitrary incident angle, compute the time delay across the surface: Δt = (x·k_x + y·k_y)/(c·k)

### 3.4 Near-to-Far-Field Transformation

**Principle:** Compute far-field scattering/re-radiation from near-field data using the equivalence principle and the Stratton-Chu integrals.

**Procedure:**
1. Record tangential E and H fields on a closed Huygens surface (contour in 2D, surface in 3D) surrounding the scatterer
2. Convert these to equivalent electric and magnetic surface currents:
   $$\mathbf{J}_s = \hat{n} \times \mathbf{H}_{\text{near}}, \quad \mathbf{M}_s = -\hat{n} \times \mathbf{E}_{\text{near}}$$
3. Compute the far-field vector potentials in the frequency domain:
   $$\mathbf{N}(\theta,\phi) = \iint_S \mathbf{J}_s(\mathbf{r}') e^{j k \hat{r}\cdot\mathbf{r}'} dS'$$
   $$\mathbf{L}(\theta,\phi) = \iint_S \mathbf{M}_s(\mathbf{r}') e^{j k \hat{r}\cdot\mathbf{r}'} dS'$$
4. Compute far fields:
   $$E_\theta = -j\omega\mu\left(N_\theta + \frac{L_\phi}{\eta}\right), \quad E_\phi = -j\omega\mu\left(N_\phi - \frac{L_\theta}{\eta}\right)$$

**RCS (Radar Cross Section):**

$$\sigma(\theta,\phi) = \lim_{r\to\infty} 4\pi r^2 \frac{|\mathbf{E}_{\text{scat}}|^2}{|\mathbf{E}_{\text{inc}}|^2}$$

In 2D (per-unit-length):

$$\sigma_{2D}(\phi) = \frac{2\pi r |E_{z,\text{scat}}|^2}{|E_{z,\text{inc}}|^2}$$

**Implementation details:**
- Time-domain near fields are saved at each time step on the output surface
- After the simulation, a discrete Fourier transform converts them to frequency domain
- The far-field integrals are computed (post-processing) for each desired frequency and angle

---

## Part IV: Dispersive, Nonlinear & Gain Media

### 4.1 Debye, Drude, and Lorentz Models

**Debye model** (polar dielectrics, water):

$$\epsilon(\omega) = \epsilon_\infty + \frac{\epsilon_s - \epsilon_\infty}{1 + j\omega\tau}$$

**Drude model** (metals, plasmas):

$$\epsilon(\omega) = \epsilon_\infty - \frac{\omega_p^2}{\omega^2 + j\omega\Gamma}$$

where ω_p is the plasma frequency and Γ is the collision frequency.

**Lorentz model** (resonant absorption bands):

$$\epsilon(\omega) = \epsilon_\infty + \frac{(\epsilon_s - \epsilon_\infty)\omega_0^2}{\omega_0^2 + 2j\omega\delta - \omega^2}$$

where ω₀ is the resonant frequency and δ is the damping coefficient.

**Materials are often represented as a sum of multiple poles:**

$$\epsilon(\omega) = \epsilon_\infty + \sum_{p=1}^P \frac{A_p}{\omega_p^2 + 2j\omega\delta_p - \omega^2}$$

### 4.2 Auxiliary Differential Equation (ADE) Method

**Approach:** Convert the frequency-domain constitutive relation to an ODE in time, which is discretized with central differences.

**Example (Drude model):** D(ω) = ε₀·ε_r(ω)·E(ω)

In time domain: $$\frac{\partial^2 \mathbf{P}}{\partial t^2} + \Gamma \frac{\partial \mathbf{P}}{\partial t} = \epsilon_0 \omega_p^2 \mathbf{E}$$

where P is the polarization current.

**ADE update loop:**
1. Update D from H using curl of Ampère's law
2. Update auxiliary variables (P, J_p, etc.) from ADEs
3. Update E from D and the auxiliary variables
4. Update H from E using curl of Faraday's law

**Benefits:** Simple implementation, handles multiple poles naturally.

### 4.3 Recursive Convolution (RC) and PLRC Methods

**Recursive Convolution (RC) Method:**
- Constitutive relation: D(t) = ε₀·ε_∞·E(t) + ε₀·χ(t) * E(t)
- The convolution is approximated as a sum over previous time steps
- For exponential time-dependence of χ(t), the convolution can be computed recursively

**PLRC (Piecewise Linear Recursive Convolution)** (Kelley & Luebbers, 1995):
- Assumes E(t) varies **linearly** within each time step (vs. constant in standard RC)
- Provides significantly higher accuracy for dispersive media
- Requires storing previous value of E

**Discrete convolution update:**

$$D^n = \epsilon_0\epsilon_\infty E^n + \epsilon_0 \sum_{m=0}^{N-1} \chi^m E^{n-m}$$

For PLRC with exponential χ:

$$D^n = \epsilon_0\epsilon_\infty E^n + \epsilon_0 \left[\xi^0 E^n + \sum_{m=0}^{N-1} \xi^{m+1} E^{n-m-1}\right]$$

where ξ^m are pre-computed recursive coefficients derived from the susceptibility function.

### 4.4 Nonlinear and Gain Media

**Second-order nonlinear effects** (χ²):
- Second harmonic generation (SHG)
- Pockels effect
- Optical rectification

**Third-order nonlinear effects** (χ³):
- Kerr effect (intensity-dependent refractive index): n = n₀ + n₂I
- Self-phase modulation
- Four-wave mixing

**FDTD implementation for Kerr nonlinearity:**

$$\mathbf{D} = \epsilon_0\epsilon_\infty \mathbf{E} + \chi^{(3)}|\mathbf{E}|^2\mathbf{E}$$

At each step, the nonlinear equation E = f(D, |E|²) must be solved, typically via Newton's method or the iterative Ziolkowski approach.

**Gain media** (lasers, amplifiers):
- Modeled via the **semiclassical Maxwell-Bloch equations**
- Maxwell's equations couple to the polarization from a two-level (or multi-level) quantum system:

$$\frac{\partial^2 P}{\partial t^2} + 2\delta \frac{\partial P}{\partial t} + \omega_0^2 P = \frac{N e^2}{m} E$$

where the population inversion N follows the rate equation:

$$\frac{\partial N}{\partial t} = \frac{1}{\hbar\omega_0}E\frac{\partial P}{\partial t} - \frac{N - N_0}{T_1}$$

---

## Part V: Applications

### 5.1 Scattering

**Scattering from PEC objects:**
- Simple implementation: set tangential E = 0 on PEC surface
- RCS computed via NF-FF transform
- Validation against Mie series (spheres, circular cylinders)

**Dielectric / coated scatterers:**
- Material parameter assignment per Yee cell
- Conformal FDTD techniques for curved surfaces (Dey-Mittra, Yu-Mittra)

**Resonant structures:**
- Cavity resonances from broadband pulse excitation + DFT
- Quality factor from ring-down: Q = ω₀·U/(−dU/dt)

### 5.2 Antennas and Microwave Circuits

**Antenna modeling:**
- Voltage gap source at feed point
- Input impedance: Z_in = V_in/I_in in frequency domain
- Far-field pattern via NF-FF transform
- Examples: dipole, patch, horn, Vivaldi

**Microwave circuits:**
- Microstrip lines and filters
- Waveguide discontinuities (iris, post, step)
- S-parameter extraction: S₁₁(ω) = V_reflected/V_incident from DFT

**S-parameter extraction setup:**
1. Excite with modulated Gaussian at port
2. Record incident and reflected voltage waveforms at reference planes
3. DFT to frequency domain
4. De-embed to move reference planes

### 5.3 Photonics

**Photonic crystals:**
- Band structure via Bloch boundary conditions and FDTD
- Defect modes (waveguides, cavities)
- Transmission/reflection spectra

**Plasmonics:**
- Drude model for metals (Ag, Au, Al)
- Surface plasmon polariton (SPP) dispersion
- LSPR (localized SPR) for nanoparticles
- Field enhancement factors

**Integrated optics:**
- Waveguide couplers, Y-branches
- Ring resonators
- Grating couplers

### 5.4 Bioelectromagnetics

**Specific Absorption Rate (SAR):**

$$\text{SAR} = \frac{\sigma_{\text{eff}} |E|^2}{2\rho}$$

where σ_eff is conductivity, ρ is mass density.

**Applications:**
- Mobile phone dosimetry (head models)
- RF hyperthermia treatment planning
- Implant safety (pacemakers, cochlear implants)
- Anatomically realistic voxel models (Duke, Ella from IT'IS Foundation)

---

## Key Equations Reference

| Concept | Equation | Key Parameters |
|---------|----------|---------------|
| 1D E-update (lossless) | E_x^{n+1}(k) = E_x^n(k) + (Δt/(εΔz))[H_y(k+½) − H_y(k−½)] | Δt, ε, Δz |
| 1D H-update (lossless) | H_y^{n+½}(k+½) = H_y^{n-½}(k+½) + (Δt/(μΔz))[E_x(k+1) − E_x(k)] | Δt, μ, Δz |
| Courant limit (1D) | c·Δt ≤ Δz | c = 1/√(μ₀ε₀) |
| Courant limit (3D) | c·Δt ≤ Δ / √3 | uniform Δ |
| Numerical dispersion | sin²(ωΔt/2) / (cΔt)² = Σ sin²(k_α·Δ/2) / Δ² | need Δ ≤ λ/10 |
| PML σ grading | σ(x) = σ_max·(x/d)^m | m = 2–4 |
| UPML tensor | **s** = diag(s_y s_z/s_x, s_z s_x/s_y, s_x s_y/s_z) | s_α = 1+σ_α/(jωε₀) |
| CPML s_α | s_α = κ_α + σ_α/(α_α + jωε₀) | κ≥1, α≈0.08 |
| TFSF correction | Add/subtract incident field on Huygens surface | J_s = n̂×H |
| RC RCS (2D) | σ_{2D} = 2πr|E_scat|²/|E_inc|² | Freq-domain post-processing |
| Debye model | ε = ε_∞ + (ε_s−ε_∞)/(1+jωτ) | τ = relaxation time |
| Drude model | ε = ε_∞ − ω_p²/(ω²+jωΓ) | ω_p = plasma freq |
| Lorentz model | ε = ε_∞ + Δε·ω₀²/(ω₀²+2jωδ−ω²) | ω₀ = resonant freq |

---

## Recommended Reading

- **Ch. 1–3:** Foundational Yee algorithm and numerical properties
- **Ch. 6–7:** PML and CPML (essential for open-region problems)
- **Ch. 8:** TFSF and incident wave injection
- **Ch. 9:** Near-to-far-field transformation
- **Ch. 10–11:** Dispersive media (ADE, RC, PLRC)
- **Ch. 14:** Nonlinear and gain media
- **Ch. 15–19:** Applications (scattering, antennas, microwave, photonics, bio-EM)

---

*Reference: A. Taflove and S. C. Hagness, "Computational Electrodynamics: The FDTD Method," 3rd ed., Artech House, 2005.*
