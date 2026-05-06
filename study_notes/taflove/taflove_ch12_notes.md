---
chapter: 12
title: "Bodies of Revolution"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, T. Jurgens, D. B. Davidson, R. W. Ziolkowski"
raw_size: 47,704 bytes
---

# Chapter 12: Bodies of Revolution (BOR-FDTD)

## 12.1 Introduction

For rotationally symmetric (axisymmetric) structures, FDTD can exploit the azimuthal symmetry to reduce a 3D problem to a set of 2D problems. The fields are expanded in a Fourier series in the azimuthal angle $\phi$:

$$
\mathbf{E}(\rho, \phi, z, t) = \sum_{m=-\infty}^{\infty} \mathbf{e}_m(\rho, z, t) e^{jm\phi}
$$

$$
\mathbf{H}(\rho, \phi, z, t) = \sum_{m=-\infty}^{\infty} \mathbf{h}_m(\rho, z, t) e^{jm\phi}
$$

where $m$ is the azimuthal mode index. Each mode $m$ is decoupled from the others, reducing a full 3D FDTD simulation to a 2D grid in $(\rho, z)$ — a computational savings of roughly $N_\phi$ (number of azimuthal grid points, typically 50-200).

## 12.2 Field Expansion in Cylindrical Coordinates

Maxwell's curl equations in cylindrical $(\rho, \phi, z)$ for a single mode $m$:

**Ampère's law**:
$$
\epsilon\frac{\partial e_\rho}{\partial t} + \sigma e_\rho = \frac{jm}{\rho} h_z - \frac{\partial h_\phi}{\partial z}
$$
$$
\epsilon\frac{\partial e_\phi}{\partial t} + \sigma e_\phi = \frac{\partial h_\rho}{\partial z} - \frac{\partial h_z}{\partial \rho}
$$
$$
\epsilon\frac{\partial e_z}{\partial t} + \sigma e_z = \frac{1}{\rho}\frac{\partial(\rho h_\phi)}{\partial\rho} - \frac{jm}{\rho} h_\rho
$$

**Faraday's law**:
$$
-\mu\frac{\partial h_\rho}{\partial t} = \frac{jm}{\rho} e_z - \frac{\partial e_\phi}{\partial z}
$$
$$
-\mu\frac{\partial h_\phi}{\partial t} = \frac{\partial e_\rho}{\partial z} - \frac{\partial e_z}{\partial \rho}
$$
$$
-\mu\frac{\partial h_z}{\partial t} = \frac{1}{\rho}\frac{\partial(\rho e_\phi)}{\partial\rho} - \frac{jm}{\rho} e_\rho
$$

Each mode $m$ has 6 field components in $(\rho, z)$ space, compared to the full 3D Yee grid's $N_\phi$ azimuthal cells.

### Mode Significance

| $m$ | Physical Meaning | Examples |
|-----|-----------------|----------|
| $m=0$ | Monopole/TEM | Conical horn, monopole, coaxial feed |
| $m=\pm1$ | Dipole | Half-wave dipole on axis, TE11 circular waveguide |
| $m=\pm2$ | Quadrupole | Higher-order waveguide modes, quadrupole antennas |
| $|m|>1$ | Higher-order | Corrugated horns, mode converters |

## 12.3 Off-Axis Difference Equations

### 12.3.1 Ampère's Law for $e_\rho$

Using a contour-path integral in the $\phi$-$z$ plane (Fig. 12.2):

$$
\epsilon \frac{\partial e_\rho}{\partial t} = \frac{1}{\rho}\frac{\partial h_z}{\partial\phi} - \frac{\partial h_\phi}{\partial z}
$$

The $e_\rho$ component is separated into cosine ($u$) and sine ($v$) parts. After integration:

$$
\epsilon(\rho_0, z_2) \frac{\partial e_{\rho,u}}{\partial t} = \frac{m}{\rho_0} h_{z,v} - \frac{h_{\phi,u}(z_2) - h_{\phi,u}(z_1)}{\Delta z}
$$

$$
\epsilon(\rho_0, z_2) \frac{\partial e_{\rho,v}}{\partial t} = -\frac{m}{\rho_0} h_{z,u} - \frac{h_{\phi,v}(z_2) - h_{\phi,v}(z_1)}{\Delta z}
$$

### 12.3.2 Ampère's Law for $e_\phi$

Using a contour-path integral in the $\rho$-$z$ plane (Fig. 12.3):

$$
\epsilon \frac{\partial e_\phi}{\partial t} = \frac{\partial h_\rho}{\partial z} - \frac{\partial h_z}{\partial \rho}
$$

After discretization:

$$
\epsilon(\rho_2, z_2) \frac{\partial e_{\phi,u}}{\partial t} = \frac{h_{\rho,u}(z_2) - h_{\rho,u}(z_1)}{\Delta z} - \frac{h_{z,u}(\rho_2) - h_{z,u}(\rho_1)}{\Delta\rho}
$$

$$
\epsilon(\rho_2, z_2) \frac{\partial e_{\phi,v}}{\partial t} = \frac{h_{\rho,v}(z_2) - h_{\rho,v}(z_1)}{\Delta z} - \frac{h_{z,v}(\rho_2) - h_{z,v}(\rho_1)}{\Delta\rho}
$$

### 12.3.3 Ampère's Law for $e_z$

Using a contour-path integral in the $\rho$-$z$ plane (Fig. 12.4):

$$
\epsilon \frac{\partial e_z}{\partial t} = \frac{1}{\rho}\frac{\partial(\rho h_\phi)}{\partial\rho} - \frac{1}{\rho}\frac{\partial h_\rho}{\partial\phi}
$$

After discretization:

$$
\epsilon(\rho_2, z) \frac{\partial e_{z,u}}{\partial t} = \frac{1}{\rho_2}\left[\frac{\rho_2 h_{\phi,u}(\rho_2) - \rho_1 h_{\phi,u}(\rho_1)}{\Delta\rho}\right] + \frac{m}{\rho_2} h_{\rho,v}
$$

$$
\epsilon(\rho_2, z) \frac{\partial e_{z,v}}{\partial t} = \frac{1}{\rho_2}\left[\frac{\rho_2 h_{\phi,v}(\rho_2) - \rho_1 h_{\phi,v}(\rho_1)}{\Delta\rho}\right] - \frac{m}{\rho_2} h_{\rho,u}
$$

### 12.3.4 Faraday's Law (H-field Updates)

Similarly, the Faraday law yields updates for $h_\rho$, $h_\phi$, $h_z$. For example:

$$
\mu(\rho_0, z_2) \frac{\partial h_{\phi,u}}{\partial t} = \frac{e_{\rho,v}(z_2) - e_{\rho,v}(z_1)}{\Delta z} - \frac{e_{z,v}(\rho_2) - e_{z,v}(\rho_1)}{\Delta\rho}
$$

The full set of 12 update equations (6 E-field + 6 H-field, each with $u$ and $v$ components) is given in (12.19)-(12.30).

## 12.4 On-Axis Difference Equations ($\rho = 0$)

At $\rho = 0$, the $1/\rho$ singularities require special treatment.

### 12.4.1 $e_z$ on the z-Axis

For mode $m = 0$: $h_\rho(0, z) = 0$ on axis. The $e_z$ update uses L'Hôpital's rule:

$$
\epsilon \frac{\partial e_z}{\partial t}\bigg|_{\rho=0} = \lim_{\rho\to 0} \frac{1}{\rho}\frac{\partial(\rho h_\phi)}{\partial\rho} = 2\frac{\partial h_\phi}{\partial\rho}\bigg|_{\rho=0}
$$

Discretized:
$$
\epsilon \frac{e_{z,u}^{n+1}(0, z) - e_{z,u}^n(0, z)}{\Delta t} = 2\frac{h_{\phi,u}^{n+1/2}(\Delta\rho/2, z) - h_{\phi,u}^{n+1/2}(0, z)}{\Delta\rho}
$$

### 12.4.2 $e_\rho$ on the z-Axis

For $m = 0$, $e_\rho$ is zero on axis. For $m = \pm 1$, the azimuthal fields at $\rho = 0$ satisfy:

$$
e_{\rho,u}(0,z) = e_{\phi,v}(0,z), \quad e_{\rho,v}(0,z) = -e_{\phi,u}(0,z)
$$

### 12.4.3 $h_\phi$ on the z-Axis

Using a special Faraday's law contour around the axis:

$$
\mu \frac{\partial h_\phi}{\partial t}\bigg|_{\rho=0} = -\frac{\partial e_z}{\partial\rho}\bigg|_{\rho=0}
$$

Discretized:
$$
\mu \frac{h_{\phi,u}^{n+1/2}(0,z) - h_{\phi,u}^{n-1/2}(0,z)}{\Delta t} = -\frac{e_{z,v}^n(\Delta\rho/2, z) - e_{z,v}^n(0,z)}{\Delta\rho/2}
$$

## 12.5 Numerical Stability

The BOR-FDTD CFL condition is similar to the 2D Cartesian case:

$$
\Delta t \leq \frac{1}{c\sqrt{(\Delta\rho_{\min})^{-2} + (\Delta z_{\min})^{-2}}}
$$

For cells near the axis ($\rho \to 0$), the azimuthal cell size $\rho\Delta\phi \to 0$, imposing a stricter limit for large $m$:

$$
\Delta t \leq \frac{\rho_{\min}\Delta\phi_{\min}}{c \cdot |m|}
$$

In practice, the $m \neq 0$ modes typically use a reduced time-step or implicit treatment near the axis.

## 12.6 PML for BOR

The uniaxial PML (UPML) is implemented in cylindrical coordinates with the stretching variables:

$$
s_\rho = \kappa_\rho + \frac{\sigma_\rho}{j\omega\epsilon_0}, \quad s_z = \kappa_z + \frac{\sigma_z}{j\omega\epsilon_0}
$$

The PML is applied only to the $\rho$-direction radial boundaries and the $z$-direction terminal ends. The $\phi$-direction does not need PML due to the Fourier expansion.

### BOR-PML Implementation

The split-field PML in cylindrical coordinates:
$$
\epsilon \frac{\partial e_{\rho,z}}{\partial t} + \sigma_z e_{\rho,z} = -\frac{\partial h_\phi}{\partial z}
$$
$$
\epsilon \frac{\partial e_{\rho,\rho}}{\partial t} + \sigma_\rho e_{\rho,\rho} = \frac{jm}{\rho} h_z
$$

## 12.7 Application to Particle Accelerator Physics

BOR-FDTD is extensively used in accelerator cavity modeling:

1. **RF cavity resonant frequency and Q-factor**: Eigenmode extraction for accelerating cavities
2. **Wakefield computation**: Beam-induced fields following a charged particle bunch
3. **Coupler design**: Input/output coupler optimization

For wakefield analysis, the source term (charged particle beam) is added:

$$
\epsilon\frac{\partial e_z}{\partial t} = \frac{1}{\rho}\frac{\partial(\rho h_\phi)}{\partial\rho} - \frac{jm}{\rho} h_\rho - J_{z,\text{beam}}
$$

where $J_{z,\text{beam}}$ represents the beam current density.

## 12.8 Summary

Key advantages of BOR-FDTD:
- **2D computational domain** for 3D axisymmetric problems
- **Natural handling** of on-axis singularity via limiting formulas
- **Mode-by-mode solution** allowing independent analysis of each $m$
- **Wakefield capability** by including beam current source terms

Limitations:
- Only applicable to **rotationally symmetric** structures
- Mode truncation errors if high-$m$ modes are significant
- Stricter CFL for large $m$ near the axis

BOR-FDTD remains the method of choice for axisymmetric antenna, waveguide, and accelerator cavity modeling.
