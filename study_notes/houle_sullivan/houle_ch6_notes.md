---
title: "Three-Dimensional Simulation"
author: "Jennifer E. Houle and Dennis M. Sullivan"
book: "Electromagnetic Simulation Using the FDTD Method with Python, Third Edition"
chapter: 6
---

## 6.1 Free-Space Simulation: The Yee Cell in 3D

### The Yee Lattice

The 3D Yee cell interleaves E and H components around a cubic cell:
- $E_x$ at $(i+1/2, j, k)$, $E_y$ at $(i, j+1/2, k)$, $E_z$ at $(i, j, k+1/2)$
- $H_x$ at $(i, j+1/2, k+1/2)$, $H_y$ at $(i+1/2, j, k+1/2)$, $H_z$ at $(i+1/2, j+1/2, k)$

### Full Maxwell's Equations (6 Scalar Components)

Starting from the normalized curl equations:

$$
\frac{\partial D_x}{\partial t} = \frac{1}{\varepsilon_0\mu_0}\left(\frac{\partial H_z}{\partial y} - \frac{\partial H_y}{\partial z}\right) \tag{6.1a}
$$

$$
\frac{\partial D_y}{\partial t} = \frac{1}{\varepsilon_0\mu_0}\left(\frac{\partial H_x}{\partial z} - \frac{\partial H_z}{\partial x}\right) \tag{6.1b}
$$

$$
\frac{\partial D_z}{\partial t} = \frac{1}{\varepsilon_0\mu_0}\left(\frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y}\right) \tag{6.1c}
$$

$$
\frac{\partial H_x}{\partial t} = \frac{1}{\varepsilon_0\mu_0}\left(\frac{\partial E_y}{\partial z} - \frac{\partial E_z}{\partial y}\right) \tag{6.1d}
$$

$$
\frac{\partial H_y}{\partial t} = \frac{1}{\varepsilon_0\mu_0}\left(\frac{\partial E_z}{\partial x} - \frac{\partial E_x}{\partial z}\right) \tag{6.1e}
$$

$$
\frac{\partial H_z}{\partial t} = \frac{1}{\varepsilon_0\mu_0}\left(\frac{\partial E_x}{\partial y} - \frac{\partial E_y}{\partial x}\right) \tag{6.1f}
$$

### FDTD Update Equations (3D)

Using $\Delta t = \Delta x / (2c_0)$ and $\Delta x = \Delta y = \Delta z$:

```python
# D-field updates (6.2a-c)
dx[i,j,k] = dx[i,j,k] + 0.5 * (
    hz[i,j,k] - hz[i,j-1,k] 
  - hy[i,j,k] + hy[i,j,k-1])

dy[i,j,k] = dy[i,j,k] + 0.5 * (
    hx[i,j,k] - hx[i,j,k-1] 
  - hz[i,j,k] + hz[i-1,j,k])

dz[i,j,k] = dz[i,j,k] + 0.5 * (
    hy[i,j,k] - hy[i-1,j,k] 
  - hx[i,j,k] + hx[i,j-1,k])

# E-field from D (simple dielectric)
ex[i,j,k] = gax[i,j,k] * dx[i,j,k]
ey[i,j,k] = gay[i,j,k] * dy[i,j,k]
ez[i,j,k] = gaz[i,j,k] * dz[i,j,k]

# H-field updates (6.2d-f)
hx[i,j,k] = hx[i,j,k] + 0.5 * (
    ey[i,j,k+1] - ey[i,j,k] 
  - ez[i,j+1,k] + ez[i,j,k])

hy[i,j,k] = hy[i,j,k] + 0.5 * (
    ez[i+1,j,k] - ez[i,j,k] 
  - ex[i,j,k+1] + ex[i,j,k])

hz[i,j,k] = hz[i,j,k] + 0.5 * (
    ex[i,j+1,k] - ex[i,j,k] 
  - ey[i+1,j,k] + ey[i,j,k])
```

> **Indexing pattern:** Each component uses neighbors offset by 1 in its own direction (for the positive derivative) and by 1 in the two perpendicular directions (for the negative derivatives). This mirrors the curl operator structure.

### Dipole Antenna Source

In 3D free-space with a point source, $E$ attenuates as $1/r^2$, making it hard to visualize. Instead, a **dipole antenna** is used:

1. Metal arms: set `gaz=0` in cells corresponding to metal → $E_z = 0$ there (as in real metal)
2. Gap: specify $E_z$ in the gap cell directly (Gaussian pulse)

Alternative (more physical): specify **H-field** around the gap per Ampere's law $\oint \mathbf{H}\cdot d\mathbf{l} = I$.

> **Why dipole?** A dipole approximates the far-field radiation pattern of real antennas. After a few wavelengths, the field behaves like a plane wave.

---

## 6.2 The PML in Three Dimensions

### Extending 2D PML to 3D

The 3D PML adds the z-direction to the anisotropic conductivity profile. Starting from:

$$
j\omega\left(1 + \frac{\sigma_{D,x}}{j\omega\varepsilon_0}\right)\left(1 + \frac{\sigma_{D,y}}{j\omega\varepsilon_0}\right)\left(1 + \frac{\sigma_{D,z}}{j\omega\varepsilon_0}\right)^{-1}D_z = c_0\left(\frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y}\right) \tag{6.3}
$$

### D-Field Update with 3D PML

Following the 2D derivation, the z-directed D-field update becomes:

```python
# curl_h definition
curl_h = (hy[i,j,k] - hy[i-1,j,k] 
        - hx[i,j,k] + hx[i,j-1,k])

# Auxiliary integration field IDz
idz[i,j,k] = idz[i,j,k] + curl_h

# D-field update with PML coefficients
dz[i,j,k] = (gi3[i] * gj3[j] * dz[i,j,k] 
           + gi2[i] * gj2[j] * (0.5 * curl_h 
           + gk1[k] * idz[i,j,k]))
```

Where:
- `gi2, gi3, gj2, gj3` are defined the same as in 2D PML
- `gk1` is the z-direction equivalent of `fi1` in x
- `idz` accumulates the "history integral" in the z-direction

### Physical Interpretation

The 3D PML has:
- Three sets of g-parameters (x, y, z directions)
- Three sets of f-parameters
- Three auxiliary integration fields: `idx`, `idy`, `idz`

Each direction attenuates waves as they exit through that face. The corners are handled by the overlap of all three directional PMLs. This makes the PML effective on all 6 faces of the 3D problem space.

> **Memory consideration:** In 2D, the IHx and IHy fields were 2D. In 3D, idx, idy, idz are **3D arrays** — significant additional memory. For large 3D problems, the PML memory overhead becomes substantial.

---

## 6.3 Total-Field/Scattered-Field Formulation in 3D

### Plane Wave Generation in 3D

Similar to 2D, but now the TF/SF boundary is a rectangular box in the XZ plane at $j = j_a$ and $j = j_b$ (Fig. 4.5). A plane wave is injected at $j = j_a$ and subtracted at $j = j_b$.

The plane wave propagates in the y-direction:
- Only $E_z$ and $H_x$ are nonzero (in free space)
- The incident buffer is 1D: `ez_inc[j]`, `hx_inc[j]`

### TF/SF Boundary Corrections (3D)

At the total-field/scattered-field boundary, corrections to D and H fields are applied using the incident buffer values. The corrections for $D_y$ and $H_x$ at the y-boundaries ensure the incident wave is properly added to the total field region.

The corrections for $H_z$ at the x and z edges handle the fact that $H_z$ depends on $E_x$ and $E_y$ which may span the TF/SF boundary.

> **Key insight:** In 3D TF/SF, we inject the plane wave through the y-boundaries (j-planes), and the corrections ensure that the wave front inside the TF region is correct. Only the scattered fields leave through the PML.

---

## Code Reference

### Basic 3D FDTD (`fd3d_4_1.py` — dipole source, no PML)

```python
import numpy as np
from numba import jit

ie = 40; je = 40; ke = 40

dx = np.zeros((ie, je, ke))
dy = np.zeros((ie, je, ke))
dz = np.zeros((ie, je, ke))
ex = np.zeros((ie, je, ke))
ey = np.zeros((ie, je, ke))
ez = np.zeros((ie, je, ke))
hx = np.zeros((ie, je, ke))
hy = np.zeros((ie, je, ke))
hz = np.zeros((ie, je, ke))

gax = np.ones((ie, je, ke))
gay = np.ones((ie, je, ke))
gaz = np.ones((ie, je, ke))

# Dipole: metal arms in z-direction at center
# Set gaz=0 for metal
gaz[ic, jc, kc-2:kc+3] = 0   # gap is at kc

nsteps = 100
for time_step in range(1, nsteps + 1):
    # D-field updates
    for k in range(1, ke):
        for j in range(1, je):
            for i in range(1, ie):
                dx[i,j,k] += 0.5 * (hz[i,j,k] - hz[i,j-1,k] 
                                    - hy[i,j,k] + hy[i,j,k-1])
                dy[i,j,k] += 0.5 * (hx[i,j,k] - hx[i,j,k-1] 
                                    - hz[i,j,k] + hz[i-1,j,k])
                dz[i,j,k] += 0.5 * (hy[i,j,k] - hy[i-1,j,k] 
                                    - hx[i,j,k] + hx[i,j-1,k])
    
    # E-field from D
    ex = gax * dx; ey = gay * dy; ez = gaz * dz
    
    # Inject Gaussian pulse in dipole gap
    pulse = np.exp(-0.5 * ((t0 - time_step) / spread)**2)
    ez[ic, jc, kc] = pulse
    
    # H-field updates
    for k in range(1, ke-1):
        for j in range(1, je-1):
            for i in range(1, ie-1):
                hx[i,j,k] += 0.5 * (ey[i,j,k+1] - ey[i,j,k] 
                                    - ez[i,j+1,k] + ez[i,j,k])
                hy[i,j,k] += 0.5 * (ez[i+1,j,k] - ez[i,j,k] 
                                    - ex[i,j,k+1] + ex[i,j,k])
                hz[i,j,k] += 0.5 * (ex[i,j+1,k] - ex[i,j,k] 
                                    - ey[i+1,j,k] + ey[i,j,k])
```

> **Numba optimization:** 3D FDTD with large arrays is very slow in pure Python. `@numba.jit(nopython=True)` compiles the loop to near-C performance, making 3D FDTD practical in Python.

### 3D PML Code

```python
# Initialize PML parameters (x, y, z directions)
npml = 8
gi1, gi2, gi3, fi1, fi2, fi3, \
gj1, gj2, gj3, fj1, fj2, fj3, \
gk1, gk2, gk3, fk1, fk2, fk3 = calculate_pml_parameters(npml, ie, je, ke)

# idz array for z-PML (3D volume)
idz = np.zeros((ie, je, ke))

# In main loop:
for k in range(1, ke):
    for j in range(1, je):
        for i in range(1, ie):
            curl_h = (hy[i,j,k] - hy[i-1,j,k] 
                    - hx[i,j,k] + hx[i,j-1,k])
            idz[i,j,k] += curl_h
            dz[i,j,k] = (gi3[i] * gj3[j] * dz[i,j,k] 
                        + gi2[i] * gj2[j] * (0.5 * curl_h 
                        + gk1[k] * idz[i,j,k]))
```

---

## Key Equations Summary

| Equation | Name | Physical Meaning |
|---|---|---|
| (6.1a-f) | 3D Maxwell's curl equations | Six scalar equations for all field components |
| (6.3) | 3D PML field equation | Anisotropic lossy medium with inverse z-permittivity |
| D-update + idz | 3D PML D-field | Requires auxiliary `idz` history integral in z |
| TF/SF corrections | 3D plane wave injection | Add/subtract incident field at y-boundary |