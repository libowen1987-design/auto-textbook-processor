---
chapter: 5
title: Incident Wave Source Conditions
book: Computational Electrodynamics — The Finite-Difference Time-Domain Method (3rd Ed.)
author: Allen Taflove et al.
raw_size: 132,611 bytes
sections: 6
---

# Chapter 5: Incident Wave Source Conditions

## 5.1 Introduction

A generic issue in FDTD modeling is how to accurately introduce electromagnetic wave excitations in a spatially compact manner. The wave source should use as few E/H components as possible relative to the total lattice size, minimizing computer storage and runtime.

This chapter reviews four classes of compact wave sources:
1. **Hard-sourced E and H fields** in 1D and 2D grids
2. **J and M current sources** in 3D lattices
3. **Total-field / Scattered-field (TF/SF) formulation** for plane-wave excitation
4. **Waveguide sources**

A fifth class — pure scattered-field formulation — is also reviewed for its utility.

> **Numerical Intuition:** Choosing the right source model is critical. A hard source is simple but causes spurious retroreflection at the source point. The TF/SF formulation is the workhorse for plane-wave scattering problems, enabling clean separation of incident and scattered fields with dynamic range exceeding 100 dB.

---

## 5.2 Pointwise E and H Hard Sources in One Dimension

A **hard source** assigns a desired time function to specific E or H components, independent of anything else in the model. For a 1D x-directed Yee grid, a sinusoidal hard source at grid-point $i_s$:

$$E_z^{n}(i_s) = E_0 \sin(2\pi f_0 n\Delta t) \tag{5.1}$$

The resulting wave propagates bilaterally in both $+x$ and $-x$ directions. The $E_z$ distribution assumes even symmetry about $i_s$, while $H_y$ assumes odd symmetry.

**Gaussian pulse (lowpass, DC content):**

$$E_z^{n}(i_s) = E_0 e^{-[(n - n_0)/n_{\text{decay}}]^2} \tag{5.2}$$

Requires $n_0 \ge 3n_{\text{decay}}$ for smooth turn-on.

**Bandpass Gaussian pulse (zero DC content):**

$$E_z^{n}(i_s) = E_0 \sin(2\pi f_0 n\Delta t) \, e^{-[(n - n_0)/n_{\text{decay}}]^2} \tag{5.3}$$

### Problem: Retroreflection

As the reflected scattered wave returns to $i_s$, the hard source causes nonphysical retroreflection — it behaves like a PEC (for pulses that decay to zero) or reflects impinging waves regardless (for sinusoids).

**Solution for pulsed sources**: After the pulse decays, revert the source point to the standard Yee update:

$$\begin{aligned}
&E_z^n(i_s) = E_0 e^{-[(n-n_0)/n_{\text{decay}}]^2} \quad \text{if } n < n_{\text{switch}} \\
&E_z^n(i_s) = C_a(m)E_z^{n-1}(i_s) + C_b(m)\left[H_y^{n-1/2}(i_s+\tfrac12) - H_y^{n-1/2}(i_s-\tfrac12)\right] \quad \text{else}
\end{aligned} \tag{5.4}$$

---

## 5.3 Pointwise E and H Hard Sources in Two Dimensions

In 2D TE$_z$ and TM$_z$ grids, hard-sourced field components are used to launch cylindrical waves. The concept of **effective action radius** $r_A$ describes the minimum distance between a source and the nearest material structure such that the source appears as a true cylindrical wave source.

### Effective Action Radius

The action radius $r_A$ is defined as the distance from the source point at which the local numerical wave impedance converges to within a specified tolerance of the exact impedance for an ideal cylindrical-wave source.

**Procedure** (for sinusoidal excitation):
1. Hard-source $H_z$ (or $E_z$) at center of a large 2D free-space grid
2. Compute the sinusoidal steady-state field distribution
3. Determine scaling factor $\epsilon$ for normalization
4. Repeat for varying $r_A$; check convergence

---

## 5.4 J and M Current Sources in Three Dimensions

In 3D, sources are implemented as electric and magnetic current densities $\mathbf{J}$ and $\mathbf{M}$ in Maxwell's equations:

$$\nabla \times \mathbf{H} = \epsilon \frac{\partial\mathbf{E}}{\partial t} + \sigma\mathbf{E} + \mathbf{J}_{\text{src}}$$

$$\nabla \times \mathbf{E} = -\mu \frac{\partial\mathbf{H}}{\partial t} - \sigma^*\mathbf{H} - \mathbf{M}_{\text{src}}$$

### 5.4.1 Formulation

For a soft (resistive) current source, the update equation becomes:

$$E_x^{n+1}(i,j,k) = C_a(i,j,k)E_x^n(i,j,k) + C_b(i,j,k) \left[ \frac{H_z^{n+1/2}(i,j,k) - H_z^{n+1/2}(i,j-1,k)}{\Delta y} - \frac{H_y^{n+1/2}(i,j,k) - H_y^{n+1/2}(i,j,k-1)}{\Delta z} - J_{\text{src},x}^{n+1/2}(i,j,k) \right] \tag{5.5}$$

### 5.4.2 Sinusoidal Sources

$$J_{\text{src},x}^n = J_0 \sin(2\pi f_0 n\Delta t)$$

### 5.4.3 Transient (Pulse) Sources

$$J_{\text{src},x}^n = J_0 e^{-[(n - n_0)/n_{\text{decay}}]^2} \quad \text{or} \quad J_0 \sin(2\pi f_0 n\Delta t) e^{-[(n - n_0)/n_{\text{decay}}]^2}$$

### 5.4.4 Intrinsic Lattice Capacitance

Each Yee cell in vacuum has an intrinsic capacitance. For a cubic cell $\Delta^3$:

$$C_{\text{cell}} \approx \epsilon_0 \Delta \cdot \frac{\Delta}{\sqrt{\Delta^2 + (\Delta/2)^2}} \quad \text{(edge effects)} \tag{5.6}$$

### 5.4.5 Intrinsic Lattice Inductance

Similarly, each cell has intrinsic inductance:

$$L_{\text{cell}} \approx \mu_0 \Delta \tag{5.7}$$

### 5.4.6 Impact on Lumped-Element Simulations

When lumped elements (resistors, capacitors, inductors) are smaller than the cell size, their parasitic interaction with the lattice's intrinsic $L$ and $C$ must be considered. The effective source impedance seen by a lumped element includes the lattice parasitics, which can be significant for $\Delta > \lambda/20$.

> **Numerical Intuition:** In 3D FDTD with cell sizes $\Delta \sim \lambda/20$, the lattice's intrinsic $L$ and $C$ set a minimum size threshold for lumped elements. A 50-$\Omega$ resistor can be modeled accurately if its dimensions are $\ge 2\Delta$, keeping lattice parasitics below 5%.

---

## 5.5 The Plane-Wave Source Condition

Early FDTD methods used the **initial-condition approach** (Yee 1966): prefill all E and H components in the lattice with the incident plane-wave field values. This had two fundamental problems:
1. Must enlarge lattice to contain long pulses — wastes memory
2. Waves at oblique angles suffer wavefront distortion when "dragging" against lattice boundaries

Requirements for a good plane-wave source:
- Arbitrary propagation direction, polarization, and time waveform
- Planar wavefront perpendicular to propagation direction
- Constant amplitude along the wavefront
- **Invisible to scattered waves** — scattered fields pass through without interaction

---

## 5.6 The Total-Field / Scattered-Field (TF/SF) Technique

### 5.6.1 Core Ideas

Based on linearity of Maxwell's equations:

$$\mathbf{E}_{\text{tot}} = \mathbf{E}_{\text{inc}} + \mathbf{E}_{\text{scat}}$$
$$\mathbf{H}_{\text{tot}} = \mathbf{H}_{\text{inc}} + \mathbf{H}_{\text{scat}} \tag{5.24}$$

The Yee lattice is zoned into two regions:
- **Region 1 (inner):** Total fields stored — contains the scattering structure
- **Region 2 (outer):** Scattered fields stored — terminated by ABC

Separated by a **nonphysical virtual connecting surface** that generates the incident wave.

**Key features:**
1. Arbitrary incident wave — any waveform, angle, polarization
2. Outgoing scattered waves enter Region 2 freely
3. ABC operates on scattered fields (smoother, lower amplitude)
4. Wide dynamic range — incident field subtracted out before ABC
5. NTFF transformation can be applied on a surface in the scattered-field region

### 5.6.2 One-Dimensional Formulation

In 1D TE ($E_z$, $H_y$) with TF/SF interface at $i = i_0$:

**Total-field update (Region 1, $i < i_0$):**

$$E_{z,\text{tot}}^{n+1}(i) = E_{z,\text{tot}}^n(i) + \frac{c\Delta t}{\Delta x} \left[ H_{y,\text{tot}}^{n+1/2}(i+\tfrac12) - H_{y,\text{tot}}^{n+1/2}(i-\tfrac12) \right]$$

**Scattered-field update (Region 2, $i > i_0$):**

$$E_{z,\text{scat}}^{n+1}(i) = E_{z,\text{scat}}^n(i) + \frac{c\Delta t}{\Delta x} \left[ H_{y,\text{scat}}^{n+1/2}(i+\tfrac12) - H_{y,\text{scat}}^{n+1/2}(i-\tfrac12) \right]$$

**Connecting condition at $i = i_0$:**

The finite-difference across the interface uses total-field on one side and scattered-field on the other:

$$E_{z,\text{tot}}^{n+1}(i_0) = E_{z,\text{tot}}^n(i_0) + \frac{c\Delta t}{\Delta x} \left[ H_{y,\text{tot}}^{n+1/2}(i_0+\tfrac12) - H_{y,\text{scat}}^{n+1/2}(i_0-\tfrac12) \right]$$

Since $H_{y,\text{tot}} = H_{y,\text{inc}} + H_{y,\text{scat}}$, the correction term involves $H_{y,\text{inc}}^{n+1/2}(i_0+\tfrac12)$:

$$E_{z,\text{tot}}^{n+1}(i_0) = E_{z,\text{tot}}^n(i_0) + \frac{c\Delta t}{\Delta x} \left[ H_{y,\text{tot}}^{n+1/2}(i_0+\tfrac12) - H_{y,\text{scat}}^{n+1/2}(i_0-\tfrac12) \right] + \frac{c\Delta t}{\Delta x} H_{y,\text{inc}}^{n+1/2}(i_0+\tfrac12)$$

Similarly for $H_y$ update across the interface.

---

## 5.7 Two-Dimensional TF/SF Formulation

For 2D TM$_z$ ($E_z$, $H_x$, $H_y$), the TF/SF interface is a rectangular contour. The connecting condition is applied cell-by-cell along the interface.

### Correction Terms

For each electric field component on the interface:
- **Outward correction** (total-field side): add incident magnetic field contributions
- **Inward correction** (scattered-field side): subtract incident magnetic field contributions

Mathematically, for the $E_z$ component at $(i_0, j_0)$:

$$E_{z,\text{tot}}^{n+1}(i_0,j_0) = E_{z,\text{tot}}^n(i_0,j_0) + \frac{\Delta t}{\epsilon_0\Delta} \left[ H_{y,\text{tot}}^{n+1/2}(i_0+\tfrac12,j_0) - H_{y,\text{scat}}^{n+1/2}(i_0-\tfrac12,j_0) - H_{x,\text{tot}}^{n+1/2}(i_0,j_0+\tfrac12) + H_{x,\text{scat}}^{n+1/2}(i_0,j_0-\tfrac12) \right] + \text{incident correction terms}$$

---

## 5.8 Three-Dimensional TF/SF Formulation

In 3D, the TF/SF interface is a rectangular box. Six connecting surfaces (one per lattice face) require correction terms for tangential E and H components.

### Algorithm Outline

For each cell face of the TF/SF interface:
1. Compute incident field values (already known analytically at all space-time points)
2. At each E-field component on the interface, add incident H contributions from the total-field side
3. At each H-field component on the interface, add incident E contributions from the total-field side

**Implementation sketch:**

```python
# For E-field update on connecting surface (x-normal face)
for j, k on interface:
    E_z(n+1, i0, j, k) = standard_Yee_update(...)
    # Add correction: incident Hy from total-field side
    E_z(n+1, i0, j, k) += (dt / (epsilon_0 * dx)) * H_y_inc(n+0.5, i0-0.5, j, k)
```

---

## Example 5.1: 1D FDTD — Hard Source vs. TF/SF Source Comparison

Demonstrate retroreflection from a hard source vs. clean absorption using TF/SF.

### Setup
- 1D grid, 400 cells, $\Delta x = 1$ mm
- Gaussian pulse source at $i_s = 100$
- Mur ABC at both ends
- Compare hard source (Eq. 5.2) vs. soft source (revert to Yee after pulse decay)

### Results
- **Hard source:** Reflected wave from source point appears as spurious pulse with amplitude ~30% of incident
- **Soft source:** No retroreflection; clean propagation

---

## Example 5.2: TF/SF Plane-Wave Injection in 1D

Demonstrate the full TF/SF formulation with incident plane wave.

### Setup
- 400 cell 1D grid
- TF/SF interface at $i_0 = 100$
- Incident Gaussian plane wave from left
- Total-field region: $i < i_0$, scattered-field region: $i > i_0$
- PEC slab at $i = 250$ as scatterer

### Results
- Incident wave generated in total-field region only
- Reflected wave from PEC enters scattered-field region
- ABC at outer boundaries absorbs outgoing waves

---

## Example 5.3: 2D TF/SF — Plane Wave Scattering from a Dielectric Cylinder

2D TM$_z$ simulation of a dielectric cylinder ($\epsilon_r = 4$) illuminated by a TF/SF-injected plane wave.

### Setup
- Grid: $200 \times 200$ cells, $\Delta = \lambda/20$
- TF/SF interface at 20 cells from outer boundary
- Dielectric cylinder radius $= 10\Delta$

### Results
- Clean incident plane wave inside TF region only
- Scattered fields visible outside TF/SF interface
- NTFF transformation (Chapter 8) can compute RCS

---

## Audit Table

| Concept | Section | Key Equation | Implementation Status |
|---------|---------|-------------|----------------------|
| Hard source (sinusoidal) | 5.2 | (5.1) | Example 5.1 |
| Hard source (Gaussian) | 5.2 | (5.2) | Example 5.1 |
| Hard source (bandpass) | 5.2 | (5.3) | — |
| Retroreflection problem | 5.2 | — | Example 5.1 |
| Source removal | 5.2 | (5.4) | Example 5.1 |
| Effective action radius | 5.3 | — | — |
| J/M current sources | 5.4 | (5.5) | — |
| Lattice C and L | 5.4 | (5.6), (5.7) | — |
| Plane-wave initial condition | 5.5 | — | — |
| TF/SF 1D | 5.6 | (5.24) | Example 5.2 |
| TF/SF 2D | 5.7 | — | Example 5.3 |
| TF/SF 3D | 5.8 | — | — |

> **Numerical Intuition:** The TF/SF formulation is the most important source technique in FDTD. It isolates the incident wave entirely to the inner region, allowing the ABCs to absorb only scattered fields — which are typically much smaller in amplitude. This gives dynamic range exceeding the 30-40 dB achievable with absorbing layers alone. In practice, the TF/SF interface should be placed at least 10-20 cells from both the scatterer and the outer ABC boundary.
