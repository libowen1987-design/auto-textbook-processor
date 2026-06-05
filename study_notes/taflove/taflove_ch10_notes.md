---
chapter: 10
title: "Local Subcell Models of Fine Geometrical Features"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, M. Celuch-Marcysiak, S. Hagness"
raw_size: 111,907 bytes
---

# Chapter 10: Local Subcell Models of Fine Geometrical Features

## 10.1 Introduction

In any grid-based numerical modeling, the distance scales over which key physical processes must be resolved can range over several orders of magnitude. Two fundamental approaches exist:

1. **Global mesh refinement**: Use a variable lattice of space cells with mesh-generation software to grade cell sizes, completely containing the structure. This maintains second-order accuracy but can dominate simulation time and introduce oddly shaped cells that destabilize the explicit time-stepping.

2. **Local subcell models**: Use a simpler, more uniform Cartesian mesh and approximate fine geometrical details by building them into the local cells adjacent to the features. This relaxes mesh-generation and computer-resource requirements at the cost of some accuracy.

**Core insight**: The integral forms of Faraday's and Ampère's laws yield the Yee algorithm when applied to rectangular contours. By deforming these contours to follow actual geometry, we obtain specialized update equations that capture subcell physics without global mesh refinement.

### Chapter Roadmap
| Section | Topic | Key Application |
|---------|-------|-----------------|
| §10.3 | Diagonal split-cell & average-properties | PEC surfaces, material interfaces |
| §10.4 | Narrow slot model | Air gaps in PEC shields |
| §10.5 | Thin wire model | Wire antennas, bonding wires |
| §10.6 | Conformal curved surface model | Curved PEC/dielectric boundaries |
| §10.7 | Thin material sheet model | Resistive paint, dielectric coatings |
| §10.8 | Surface impedance BC | Skin effect in lossy conductors |
| §10.9 | Thin coatings on PEC | Radar-absorbing layers |
| §10.10 | Relativistic moving boundaries | Doppler analysis, moving scatterers |

## 10.2 Basis of Contour-Path FDTD

Departing from Yee's pointwise derivative interpretation, the contour-path approach starts with the macroscopic integral forms:

$$
\oint_C \mathbf{E} \cdot d\mathbf{l} = -\mu \frac{d}{dt} \iint_S \mathbf{H} \cdot d\mathbf{S} \quad \text{(Faraday)}
$$

$$
\oint_C \mathbf{H} \cdot d\mathbf{l} = \epsilon \frac{d}{dt} \iint_S \mathbf{E} \cdot d\mathbf{S} + \iint_S \sigma \mathbf{E} \cdot d\mathbf{S} \quad \text{(Ampère)}
$$

These are implemented on electrically small, spatially orthogonal contours that mesh like chain links, filling space with a 3D "chain-link" array. Wires, slots, and curved surfaces are accounted for by:
- Incorporating appropriate near-field behavior into contour and surface integrals
- Deforming contour paths to conform with surface curvature

This approach permits the FDTD model to deal directly with EMFs and MMFs developed around each contour.

## 10.3 The Simplest Contour-Path Subcell Models

### 10.3.1 Diagonal Split-Cell Model for PEC Surfaces

For curved PEC boundaries, the staircase model (continuous chain of zeroed $E_x$ and $E_y$ components) is replaced by a diagonal split-cell model. Applying Faraday's law at a cell split diagonally by the PEC boundary:

$$
H_z^{n+1/2}(i,j,k) = H_z^{n-1/2}(i,j,k) + \frac{2\Delta t}{\mu_0 \Delta} \left[E_x^n(i,j+1/2,k) - E_y^n(i+1/2,j,k)\right]
$$

Only the H-field at the center of split cells uses this update; all others use the standard Yee algorithm. Mesh generation: first construct a best-fit staircase, then test each cell face for contiguous PEC-assigned E-components.

### 10.3.2 Average Properties Model for Material Surfaces

For a material interface cutting a cell, Faraday's law yields:

$$
H_z^{n+1/2} = H_z^{n-1/2} + \frac{\Delta t}{\left[\mu_1 f + \mu_2(1-f)\right]\Delta} \left[E_x^n(i,j+1/2) - E_x^n(i,j-1/2) + E_y^n(i-1/2,j) - E_y^n(i+1/2,j)\right]
$$

where $0 \le f \le 1$ is the fraction of cell area in Medium \#1. The cell permeability $\mu$ is the weighted average of $\mu_1$ and $\mu_2$.

## 10.4 Narrow Slot Model

For a slot of width $g \ll \Delta$ in a PEC screen (2D TE$_z$ illumination), three Faraday's law contours are used:

**Away from slot** (Contour C1):
$$
H_z^{n+1/2}(x,y_0) = H_z^{n-1/2}(x,y_0) + \frac{\Delta t}{\mu_0\Delta(\Delta/2 + a)} \left[E_y^n(\Delta/2,y_0) - E_y^n(-\Delta/2,y_0)\right] - \frac{\Delta t}{\mu_0\Delta} E_x^n(x,y_0-\Delta/2)
$$

**At slot opening** (Contour C2):
$$
H_z^{n+1/2}(x_0,y_0) = H_z^{n-1/2}(x_0,y_0) + \frac{\Delta t}{\mu_0 g\Delta} \left[(\cdots)\right]
$$

**Within slot** (Contour C3): reduces to a plane-wave relation (the gap $g$ cancels).

**Validation**: A $\lambda_0/10$ resolution contour-path model agreed with very high-resolution MoM for gap $E_x$ fields, even for gaps as small as $\lambda_0/1000$ (1/1000th of a cell).

## 10.5 Thin Wire Model

For a wire of radius $a \ll \Delta$, near-field distributions are assumed static ($1/r$ variation):

**Looping H-components** ($H_y$ variation $\propto 1/r$):
$$
H_y^{n+1/2}\big|_{\Delta x/2,y_0,z_0} = H_y^{n-1/2}\big|_{\Delta x/2,y_0,z_0} + \frac{2\Delta t}{\mu_0 k_\mathcal{E} \ln(\Delta/r_0)} E_z^n(0,y_0,z_0)
$$
where $k_\mathcal{E} = [(\Delta x \Delta y) \tan^{-1}(\Delta y/\Delta x)]^{-1}$.

**Radial E-components** ($E_x$ variation $\propto 1/r$):
$$
E_x^{n+1}\big|_{\Delta x/2,y_0,z_0-\Delta z/2} = E_x^n\big|_{\Delta x/2,y_0,z_0-\Delta z/2} + \frac{k_\mathcal{H}}{\epsilon_0 \Delta z} \left(H_y^{n+1/2}\big|_{\Delta x/2,y_0,z_0} - H_y^{n+1/2}\big|_{\Delta x/2,y_0,z_0-\Delta z}\right) + \frac{\Delta t}{\epsilon_0 \Delta y} \left(H_z^{n+1/2}\big|_{\Delta x/2,y_0+\Delta y/2,z_0-\Delta z/2} - H_z^{n+1/2}\big|_{\Delta x/2,y_0-\Delta y/2,z_0-\Delta z/2}\right)
$$
where $k_\mathcal{H} = \ln(\Delta x/r_0)/\Delta y$.

**Open-circuit end correction** ($z = z_{\text{top}}$):
Radial E-fields at the wire end use special elliptic-integral-based coefficients involving complete elliptic integrals $K(k_1)$ and $E(k_1)$.

**Validation** ([5], Mäkinen et al. 2002): A 21-cell thin-wire dipole model achieved better accuracy than the original 41-cell model of [2] for both $|S_{11}|$ and input impedance across a wide range of wire radii ($r_0/L$ from $2\times10^{-4}$ to $10^{-2}$).

## 10.6 Locally Conformal Models of Curved Surfaces

### 10.6.1 Yu-Mittra PEC Model

The contour-path update for H-components in cells intersecting PEC surfaces:

$$
H_z^{n+1/2}(i,j,k) = H_z^{n-1/2}(i,j,k) + \frac{\Delta t}{\mu_0 \Delta_x \Delta_y} \left[E_y^n(i+1/2,j,k)\ell_y + E_x^n(i,j+1/2,k)\ell_x - E_y^n(i-1/2,j,k)\Delta_y - E_x^n(i,j-1/2,k)\Delta_x\right]
$$

where $\ell_x$ and $\ell_y$ are the deformed contour lengths outside the PEC. Note: the full cell area $\Delta_x \Delta_y$ is used for the magnetic flux integral. E-components are updated in the usual Yee manner.

**Advantage**: At 8 cells/$\lambda$, contour-path FDTD matches staircased FDTD at 32 cells/$\lambda$ — a **64:1** storage reduction and **256:1** runtime reduction in 3D.

### 10.6.2 Validation Results

- **Twisted elliptical waveguide cavity** (§10.6.2, Fig. 10.8): Fundamental-mode resonant frequency error reduced from ~12% (staircase, 8 cells/$\lambda$) to ~2% (contour-path, 8 cells/$\lambda$).
- **Winglike object RCS** (§10.6.2, Fig. 10.9): $\lambda_0/20$ contour-path FDTD matched measurements over 45-50 dB dynamic range; staircasing required $\lambda_0/80$ for equivalent accuracy.
- **Sphere pair RCS** (§10.6.2, Fig. 10.10): ±1 dB accuracy over 35 dB dynamic range.

### 10.6.3 Yu-Mittra Dielectric Model

For a cell intersected by a dielectric interface, effective permittivity for components spanning the interface:

$$
\epsilon_{\text{eff}} = \frac{(\Delta_x - \Delta_{x1})\epsilon_1 + \Delta_{x1}\epsilon_2}{\Delta_x}
$$

This linear weighting (not requiring 3D volume calculations) yields accuracy comparable to or better than previous conformal methods.

## 10.7 Maloney-Smith Thin Material Sheet Model

For a sheet of thickness $d < \Delta/2$ with properties $\epsilon_s$, $\sigma_s$, $\mu_s = \mu_0$:

**Normal E-field splitting**: $E_x$ is split into $E_{x,\text{out}}$ (free-space update) and $E_{x,\text{in}}$ (inside-sheet update):

$$
E_{x,\text{in}}^{n+1} = \frac{1 - \sigma_s \Delta t / 2\epsilon_s}{1 + \sigma_s \Delta t / 2\epsilon_s} E_{x,\text{in}}^n + \frac{\Delta t / \epsilon_s}{1 + \sigma_s \Delta t / 2\epsilon_s} (\nabla \times \mathbf{H})^{n+1/2}
$$

**Tangential components** ($E_y$, $E_z$): use average-properties method:

$$
\epsilon_{\text{avg}} = \left(1 - \frac{d}{\Delta_x}\right)\epsilon_0 + \frac{d}{\Delta_x}\epsilon_s, \quad \sigma_{\text{avg}} = \left(1 - \frac{d}{\Delta_x}\right)\cdot 0 + \frac{d}{\Delta_x}\sigma_s
$$

**H-field piercing the sheet** (Faraday contours): $H_y$ and $H_z$ at the sheet surface:

$$
H_y^{n+1/2}(i,j-1/2,k) = H_y^{n-1/2}(i,j-1/2,k) + \frac{\Delta t}{\mu_0 \Delta_x \Delta_y} \left[ \cdots \right]
$$

**Validation**: Parallel-plate waveguide loaded with a thin lossy sheet showed <1% error in attenuation constant over $10^{-4}$ to $10^3$ range of loss tangent. Resistively loaded monopole antenna (§10.7.2, Fig. 10.14): excellent agreement with measured reflected voltage.

## 10.8 Surface Impedance Boundary Conditions (SIBC)

For a lossy conductor with $\sigma_2 \gg \omega \epsilon_2$, the **Leontovich impedance BC**:

$$
Z_s(\omega) = \sqrt{\frac{j\omega \mu_0}{\sigma_2 + j\omega \epsilon_2}} \approx \sqrt{\frac{j\omega \mu_0}{\sigma_2}}
$$

In the time domain (monochromatic approximation):

$$
E_x(0,t) = R_s H_y(0,t) + L_s \frac{\partial H_y}{\partial t}, \quad R_s = \frac{1}{2a_2}, \quad L_s = \frac{\mu_0}{2a_2}
$$

### 10.8.1 Monochromatic SIBC (Maly 1992)

Using contour-path Faraday's law with the SIBC substituted for the E-field inside the conductor:

$$
H_y^{n+1/2}(i,-1/2) = \frac{\mu_0 \Delta_z + L_s - R_s \Delta t/2}{\mu_0 \Delta_z + L_s + R_s \Delta t/2} H_y^{n-1/2}(i,-1/2) + \frac{\Delta t \Delta_x}{\mu_0 \Delta_z + L_s + R_s \Delta t/2} \left[E_{z}^n(i+1/2,-1/2) - E_{z}^n(i-1/2,-1/2) + E_{x}^n(i,-1)\right] / \Delta_x
$$

### 10.8.2 Convolution-Based SIBC (Beggs et al. 1992)

Full convolution form:

$$
E_x(0,t) = \int_0^t Z_s'(t-\tau) \frac{\partial H_y(0,\tau)}{\partial \tau} d\tau, \quad Z_s'(t) = \frac{1}{\sqrt{\pi \sigma_2 \mu_0 t}}
$$

Practical implementation via Prony's method + recursive summation:

$$
H_y^{n+1/2} = H_y^{n-1/2} + \frac{\Delta t}{\mu_0 \Delta_z + Z_0(0)} \left[ \cdots \right] - \frac{1}{\mu_0 \Delta_z + Z_0(0)} \sum_{m=0}^{n-1} \left[ (H_y^{n-m+1/2} - H_y^{n-m-1/2}) Z_0(m) \right]
$$

Recursive form (N=10 exponentials adequate for convergence):

$$
\Psi_\ell^n(i,-1/2) = a_\ell e^{b_\ell \Delta t} \Psi_\ell^{n-1}(i,-1/2) + c_\ell \left[H_y^{n+1/2}(i,-1/2) - H_y^{n-1/2}(i,-1/2)\right]
$$

## 10.9 Thin Coatings on PEC Surface

### 10.9.1 Effective Conformal Method

For a thin dielectric/magnetic coating (thickness $d \ll \Delta$) on a PEC surface, the coating modifies the tangential field at the surface. The method approximates the coating by combining the conformal contour-path technique with surface impedance concepts. Key formula for the modified update:

$$
E_t^{n+1} = \frac{2\epsilon_{\text{coat}} - \sigma_{\text{coat}} \Delta t}{2\epsilon_{\text{coat}} + \sigma_{\text{coat}} \Delta t} E_t^n + \frac{2\Delta t}{2\epsilon_{\text{coat}} + \sigma_{\text{coat}} \Delta t} (\nabla \times \mathbf{H})^{n+1/2}
$$

### 10.9.2 Kärkkäinen Method

A more rigorous approach using subcell integration of the coating layer's fields. The magnetic field update acquires a correction factor:

$$
H^{n+1/2} = H^{n-1/2} + \frac{\Delta t}{\mu_0 A_{\text{eff}}} \oint_{C_{\text{eff}}} \mathbf{E} \cdot d\mathbf{l}
$$

where $A_{\text{eff}}$ accounts for the coating layer's contribution to the magnetic flux integral.

## 10.10 Relativistic Motion of PEC Boundaries

### 10.10.1 Basis

For a PEC boundary moving at relativistic velocity $\mathbf{v}$ in the lab frame, the boundary condition is:

$$
\hat{n} \times \mathbf{E}' = 0
$$

where $\mathbf{E}'$ is the field in the rest frame of the moving boundary. Using the Lorentz transformation:

$$
\mathbf{E}' = \gamma (\mathbf{E} + \mathbf{v} \times \mathbf{B}) - \frac{\gamma^2}{\gamma+1} \mathbf{v} (\mathbf{v} \cdot \mathbf{E})
$$

The contrapath FDTD approach captures this by deforming the Faraday contour in the lab frame such that the receding/advancing boundary position is tracked at each time step. For a one-dimensional moving PEC wall at position $x = vt$:

$$
H_y^{n+1/2}(i) = H_y^{n-1/2}(i) - \frac{\Delta t}{\mu_0 \Delta x} \left[ E_z^n(i+1/2) - E_z^n(i-1/2) \right]
$$

where at cells intersected by the moving boundary, the contour length and area are updated each step.

### 10.10.2 Validation

**Doppler shift assessment**: A moving PEC wall at $v = 0.1c$ showed frequency shifts accurate to within 0.5% of the relativistic Doppler formula $f_{\text{reflected}} = (1-2v/c)f_0$. This demonstrates the contour-path model's ability to capture relativistic kinematics without transformation to a co-moving frame.

## 10.11 Summary and Discussion

| Subcell Model | Key Idea | Accuracy Gain vs. Staircase | Computational Overhead |
|--------------|----------|---------------------------|----------------------|
| Diagonal split-cell | Diagonal PEC contour | ~2× resolution gain | Minimal |
| Average properties | Weighted $\epsilon$, $\mu$, $\sigma$ | ~2-4× resolution gain | Minimal |
| Narrow slot | Deformed Faraday contours | Accurate to $\lambda/1000$ gaps | 2-3 special cells/slot |
| Thin wire | $1/r$ static field assumption | 2-4× resolution gain | 4-8 special cells/wire |
| Conformal PEC (Yu-Mittra) | Deformed edges, full area | 4× resolution gain | O(few %) |
| Conformal dielectric (Yu-Mittra) | Linear $\epsilon$ weighting | 2-3× resolution gain | O(few %) |
| Thin material sheet | Split normal $E$ | <1% attenuation error | 2-3 cells/sheet crossing |
| SIBC (monochromatic) | $R_s + L_s \partial/\partial t$ | Avoids skin-depth mesh | 1 boundary cell |
| SIBC (convolution) | Prony + recursive sum | 50× storage reduction | $N$ recursion terms |
| Relativistic boundary | Time-dependent contour | <0.5% Doppler error | Mesh update per step |

### Key Takeaways
1. Contour-path FDTD achieves 2-4× resolution advantage per dimension (16-64× in 3D storage) over staircasing.
2. Thin-wire models with $1/r$ near-field assumptions accurately capture input impedance for wire radius ratios $r_0/L < 10^{-2}$.
3. Surface impedance BCs avoid volumetric modeling of lossy conductors, reducing cell count by orders of magnitude when skin depth is unresolved.
4. The Yu-Mittra conformal technique is the most practical for general curved PEC structures due to its simplicity and stability.
5. Relativistic boundaries are the ultimate extension: FDTD can directly model Lorentz transforms without coordinate transformations.
