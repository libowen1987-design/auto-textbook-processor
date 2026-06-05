---
chapter: 13
title: "Periodic Structures"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, J. G. Maloney, M. P. Kesler, G. S. Smith, W. J. Hoefer"
raw_size: 83,465 bytes
---

# Chapter 13: Periodic Structures

## 13.1 Introduction

Periodic structures — frequency selective surfaces (FSS), electromagnetic bandgap (EBG) materials, metamaterials, phased arrays — are characterized by spatial periodicity $p$ in one or two dimensions. Modeling exploits the **Floquet (Bloch) theorem**: fields in adjacent unit cells differ only by a known phase factor.

**Computational savings**: A single unit cell with periodic boundary conditions (PBC) replaces the full $N \times N$ array, yielding $N^2$ savings in 2D or $N^3$ in 3D.

## 13.2 Review of Scattering from Periodic Structures

### Floquet Mode Representation

For a plane wave incident at angle $\phi_I$ on a 1D periodic structure (period $y_p$):

$$
\mathbf{E}(x, y + y_p) = \mathbf{E}(x, y) e^{-j k_0 y_p \sin \phi_I}
$$

Scattered fields decompose into Floquet modes (grating lobes) at angles:

$$
\sin \phi_{T,m} = \sin \phi_I + \frac{2\pi m}{k_0 y_p}, \quad m = 0, \pm 1, \pm 2, \ldots
$$

**Grating lobe turn-on frequencies**:
$$
f_{\text{turn-on},m} = \frac{m c}{y_p (1 + \sin \phi_I)} \quad (m > 0)
$$

### Far-Field Computation

From unit cell fields, the far-field amplitude for Floquet order $m$ is:

$$
E_{\text{far},m}(t) = \frac{1}{N_y} \sum_{\ell=1}^{N_y} P(t, \ell \Delta y) \exp\left(j \frac{2\pi m \ell}{N_y}\right)
$$

where $P$ is the transformed field $P = E_z e^{j k_y y}$, removing the phase taper across the cell (Fig. 13.5 shows transmission amplitudes for a lossy screen).

## 13.3 Direct Field Methods

### 13.3.1 Normal Incidence

For $\phi_I = 0$, the PBC involves only fields at the current time level:

$$
E_z(x, y=0, t) = E_z(x, y=y_p, t)
$$

This is the simplest case — no time advance needed. Standard FDTD stability applies: $\Delta t \leq \Delta / (c\sqrt{N})$.

**Application**: EBG materials. Example: 6 rows of 4-mm-diameter Pyrex rods ($\epsilon_r=4.2$) on 9-mm square lattice. FDTD results (Fig. 13.7) show excellent agreement with mode-matching for transmission through the EBG crystal.

### 13.3.2 Multiple Unit Cells for Oblique Incidence

For $\phi_I \neq 0$, the phase shift corresponds to a time delay. Using $M$ unit cells:

$$
E_z(x, y=y_p, t) = E_z(x, y=0, t + M\Delta t_{y_p})
$$

where $\Delta t_{y_p}$ is the time required for the wave to travel $y_p \sin \phi_I / c$.

**Approach**: Use multiple cells (3-5) connected via PBC at one edge and ABCs at others. The top cell provides the solution. Accuracy comparable to finite-array approximation with $O(M^2)$ storage (2D) or $O(M^3)$ (3D).

### 13.3.3 Sine-Cosine Method

Single-frequency technique using two simultaneous grids (cos $\omega t$ and sin $\omega t$ excitation). At boundaries:

$$
\begin{aligned}
E_z(C) &= \text{Re}\{[E_z(A) + j E_z(B)] e^{j k_y y_p}\} \\
E_z(D) &= \text{Im}\{[E_z(A) + j E_z(B)] e^{j k_y y_p}\}
\end{aligned}
$$

**Advantage**: No time advance needed. **Disadvantage**: Only one frequency per simulation.

Results for 30° incidence on a lossy screen (Fig. 13.10) match mode-matching perfectly.

### 13.3.4 Angled-Update Method

Exploits the natural time gradient across the grid. Fields at different $y$ positions are at different time levels, permitting PBC implementation using stored past values:

$$
E_z^n(i, 0) = E_z^{n-\Delta n}(i, N_y) e^{-j k_y y_p}
$$

where $\Delta n = y_p \sin \phi_I / (c \Delta t)$.

## 13.4 Field-Transformation Technique

The key insight: remove the phase gradient by introducing transformed field variables:

$$
P_z = E_z e^{j k_y y}, \quad Q_x = \eta_0 H_x e^{j k_y y}, \quad Q_y = \eta_0 H_y e^{j k_y y}
$$

The transformed fields satisfy **simple PBC**: $P_z(y=0) = P_z(y=y_p)$, $Q_x(y=0) = Q_x(y=y_p)$.

Maxwell's equations in the transformed domain (time-domain):

$$
\frac{\mu_r}{c} \frac{\partial Q_x}{\partial t} = -\frac{\partial P_z}{\partial y} + \left\{\frac{\sin \phi}{c} \frac{\partial Q_x}{\partial t}\right\}
$$

$$
\frac{\mu_r}{c} \frac{\partial Q_y}{\partial t} = \frac{\partial P_z}{\partial x}
$$

$$
\frac{\epsilon_r \mu_r - \sin^2 \phi}{c} \frac{\partial P_z}{\partial t} = -\epsilon_r \frac{\partial Q_y}{\partial x} + \mu_r \frac{\partial Q_x}{\partial y} - \frac{\sin \phi}{c} \frac{\partial P_z}{\partial t}
$$

### Dispersion Relation

The continuous dispersion relation is:

$$
\frac{v_p}{c} = \sqrt{\sin \alpha \sin \phi + \sqrt{(\sin \alpha \sin \phi)^2 + \cos^2 \phi}}
$$

where $\alpha$ is the scattered-wave propagation angle.

**Key insight**: The minimum phase velocity occurs at $\alpha = -90^\circ$: $v_{p,\min}/c = 1/(1 + \sin \phi)$. As $\phi \to 90^\circ$, the effective cell size shrinks — requiring finer mesh resolution.

## 13.5 Multiple-Grid Approach

Uses two spatially staggered grids (shifted $\Delta y/2$ and $\Delta t/2$) to center-difference the extra time-derivative terms:

- Grid I: black symbols at integer time levels
- Grid II: white symbols at half-integer levels

The 6-equation update system (13.30)-(13.31) handles the coupled $P_z$, $Q_x$, $Q_y$ components across both grids.

### Stability Criterion

$$
\frac{c \Delta t}{\Delta} \leq \frac{1}{\sqrt{N}} \frac{1}{1 + \sin \phi}
$$

where $N$ is the dimensionality. This is more restrictive than the standard CFL limit by the factor $1/(1+\sin \phi)$.

### PML Boundary

The split-field PML is adapted to the transformed variables. The stretching coefficients $\kappa_i$, $\sigma_i$ follow the standard PML profile but applied to the $P$/$Q$ variables.

## 13.6 Split-Field Method (2D)

### 13.6.1 Formulation

A more efficient single-grid approach than the multiple-grid method. The key is to **split** the transformed field variables to handle the extra time-derivative terms implicitly:

$$
P_z = P_{zx} + P_{zy}, \quad Q_x = Q_{xx} + Q_{xy}
$$

The split equations:
$$
\left(\epsilon_r \mu_r - \sin^2 \phi\right) \frac{\partial P_{zx}}{\partial t} = -\epsilon_r \frac{\partial Q_y}{\partial x}
$$
$$
\left(\epsilon_r \mu_r - \sin^2 \phi\right) \frac{\partial P_{zy}}{\partial t} = \mu_r \frac{\partial Q_x}{\partial y} - \frac{\sin \phi}{c} \frac{\partial P_z}{\partial t}
$$
$$
\frac{\mu_r}{c} \frac{\partial Q_{xx}}{\partial t} = -\frac{\partial P_z}{\partial y} + \frac{\sin \phi}{c} \frac{\partial Q_x}{\partial t}
$$
$$
\frac{\mu_r}{c} \frac{\partial Q_{xy}}{\partial t} = 0 \quad (\text{or separate})
$$

### 13.6.2 Stability

Von Neumann analysis yields the stability condition:

$$
\frac{c \Delta t}{\Delta} \leq \frac{1}{\sqrt{N}} \cos \phi
$$

This is **less restrictive** than the multiple-grid approach and allows larger time-steps for small $\phi$.

### 13.6.3 Lossy Materials

Conductivity $\sigma$ is included by modifying the Ampère-law split equations:

$$
\epsilon \frac{\partial P_{zx}}{\partial t} + \sigma P_{zx} = -\frac{\partial Q_y}{\partial x} + \text{(coupling terms)}
$$

The semi-implicit treatment of $\sigma$ follows the standard FDTD approach.

## 13.7 Split-Field Method (3D)

### 13.7.1 Formulation

Extension to 3D with two periodic directions $(x, y)$ and incidence angles $(\theta, \phi)$. The transformation:

$$
P = E e^{j(k_{x0}x + k_{y0}y)}, \quad Q = \eta_0 H e^{j(k_{x0}x + k_{y0}y)}
$$

The split-field equations involve 12 components (6 E, 6 H, each split into two parts). The coupling is more complex due to the 2D phase gradient.

### 13.7.2 PML Termination

The UPML formulation is applied to the transformed variables. The stretching coefficients $s_x$, $s_y$, $s_z$ modify the split-field equations. Example for $P_{zx}$:

$$
\left(\epsilon_r \mu_r - \sin^2 \theta \cos^2 \phi\right) \frac{\partial P_{zx}}{\partial t} = -\frac{\epsilon_r}{s_z} \frac{\partial Q_y}{\partial x}
$$

## 13.8 Applications

### 13.8.1 Electromagnetic Bandgap (EBG) Structures

Split-field PBC enables wideband EBG characterization. The bandgap is identified by zero transmission over a frequency range (Fig. 13.28). For a metallic via EBG:

- Bandgap center frequency controlled by via spacing and dielectric thickness
- Split-field results match unit-cell eigenmode solver to within 2%

### 13.8.2 Metamaterial Unit Cell Analysis

The split-field method retrieves effective $\epsilon_{\text{eff}}(\omega)$ and $\mu_{\text{eff}}(\omega)$ from S-parameters of a single unit cell:

$$
\epsilon_{\text{eff}} = \frac{n}{Z}, \quad \mu_{\text{eff}} = nZ
$$

where $n$ is the refractive index and $Z$ the wave impedance extracted from $S_{11}$ and $S_{21}$.

### Summary

| Method | Storage | Frequency Range | Stability | Implementation |
|--------|---------|----------------|-----------|----------------|
| Normal incidence PBC | 1× | Wideband | Standard CFL | Trivial |
| Multiple unit cells | $M^2$× | Wideband | Standard CFL | Simple |
| Sine-cosine | 2× | Single freq. | Standard CFL | Moderate |
| Angled-update | 1× | Wideband | Modified | Complex |
| Field-transformation | 1× | Wideband | Modified | Complex |
| Split-field | 1× | Wideband | $\cos\phi$ CFL | Moderate |
| Multiple-grid | 2× | Wideband | $(1+\sin\phi)^{-1}$ CFL | Complex |

The **split-field method** is the most practical for wideband oblique-incidence periodic FDTD.
