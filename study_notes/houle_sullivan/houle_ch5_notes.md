---
title: "Two-Dimensional Simulation"
author: "Jennifer E. Houle and Dennis M. Sullivan"
book: "Electromagnetic Simulation Using the FDTD Method with Python, Third Edition"
chapter: 5
---

## 5.1 FDTD in Two Dimensions: TM Mode

### Reducing Maxwell's Equations to TM Mode

For 2D simulation, we choose between two modes:
- **TM mode:** $E_z, H_x, H_y$ (transverse magnetic — E has no transverse component)
- **TE mode:** $H_z, E_x, E_y$ (transverse electric — H has no transverse component)

Using the normalized Maxwell's equations from Chapter 3:

$$
\frac{\partial D_z}{\partial t} = \frac{1}{\varepsilon_0\mu_0}\left(\frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y}\right) \tag{5.1a}
$$

$$
D_z(\omega) = \varepsilon_r^*(\omega)E_z(\omega) \tag{5.1b}
$$

$$
\frac{\partial H_x}{\partial t} = -\frac{1}{\varepsilon_0\mu_0}\frac{\partial E_z}{\partial y} \tag{5.1c}
$$

$$
\frac{\partial H_y}{\partial t} = \frac{1}{\varepsilon_0\mu_0}\frac{\partial E_z}{\partial x} \tag{5.1d}
$$

### Yee Grid in 2D

The TM-mode Yee grid staggers $D_z$, $E_z$ on the main grid points, with $H_x$ at $(i, j+1/2)$ and $H_y$ at $(i+1/2, j)$. This interleaving allows centered finite differences for both curl operators.

### FDTD Update Equations (2D TM, Free Space)

Setting $\Delta t = \Delta x / (2c_0)$ and assuming $\Delta x = \Delta y$:

```python
# D-field (flux density) update
dz[i, j] = dz[i, j] + 0.5 * (hy[i, j] - hy[i-1, j] 
                              - hx[i, j] + hx[i, j-1])                        # (5.2a)

# E-field update (simple lossy dielectric)
ez[i, j] = gaz[i, j] * dz[i, j]                                              # (5.2b)

# Hx update
hx[i, j] = hx[i, j] + 0.5 * (ez[i, j] - ez[i, j+1])                          # (5.2c)

# Hy update
hy[i, j] = hy[i, j] + 0.5 * (ez[i+1, j] - ez[i, j])                          # (5.2d)
```

> **Physical intuition:** In 2D TM, $H_x$ depends on the **y-derivative** of $E_z$ (curling around $H_x$ in the x-y plane) while $H_y$ depends on the **x-derivative**. The wave propagates in the $x$-$y$ plane with $E$ polarized in $z$.

---

## 5.2 The Perfectly Matched Layer (PML)

### The ABC Problem

In any FDTD simulation, the problem space is finite. Without special treatment, waves reflect from boundaries and contaminate the results. **Absorbing boundary conditions (ABCs)** minimize this.

### Reflection Coefficient Between Media

When a wave propagates from medium A to medium B:

$$
\Gamma = \frac{\eta_B - \eta_A}{\eta_B + \eta_A} \tag{5.3}
$$

where $\eta = \sqrt{\mu/\varepsilon}$ is the intrinsic impedance.

If $\mu$ changed with $\varepsilon$ such that $\eta$ remained constant, $\Gamma = 0$ — **no reflection**. But the wave still propagates. We also need **loss** so the wave dies out before reaching the boundary.

### Berenger's PML Solution

Idea: Use **fictitious anisotropic media** with complex permittivity and permeability. For wave incident on the PML from free space:

**Condition 1 — Impedance matching:**
$$
\eta_0 = \eta_m = \sqrt{\frac{\mu_{Fx}^*}{\varepsilon_{Fx}^*}} = 1 \quad \text{(normalized units)} \tag{5.4}
$$

**Condition 2 — Anisotropic indexing (perpendicular direction):**
$$
\varepsilon_{Fx}^* = \frac{1}{\varepsilon_{Fy}^*},\quad \mu_{Fx}^* = \frac{1}{\mu_{Fy}^*} \tag{5.5}
$$

Choosing:
$$
\varepsilon_{Fm} = \mu_{Fm} = 1,\quad \frac{\sigma_m}{\varepsilon_0} = \frac{\sigma_m}{\mu_0} = \sigma_D \quad (m = x \text{ or } y) \tag{5.6}
$$

then $\eta_m = 1$ everywhere — **perfectly matched**.

### PML Equations (X-direction only)

With the PML in the x-direction, the field equations become:

$$
j\omega\left(1 + \frac{\sigma_D(x)}{j\omega\varepsilon_0}\right)D_z = c_0\left(\frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y}\right) \tag{5.7a}
$$

$$
j\omega\left(1 + \frac{\sigma_D(x)}{j\omega\varepsilon_0}\right)^{-1}H_x = -c_0\frac{\partial E_z}{\partial y} \tag{5.7b}
$$

$$
j\omega\left(1 + \frac{\sigma_D(x)}{j\omega\varepsilon_0}\right)H_y = c_0\frac{\partial E_z}{\partial x} \tag{5.7c}
$$

> **Key:** The inverse permeability for $H_x$ (vs. $H_y$) satisfies Eq. (5.5).

### D-Field Update with PML

From Eq. (5.7a), the time-domain update for $D_z$ at the PML edge:

$$
D_z^{n+1/2}[i,j] = \texttt{gi3}[i]\,D_z^{n-1/2}[i,j] + \texttt{gi2}[i]\cdot 0.5\bigl(H_y^{n}[i+1/2,j] - H_y^{n}[i-1/2,j] - H_x^{n}[i,j+1/2] + H_x^{n}[i,j-1/2]\bigr) \tag{5.8}
$$

where:

$$
\texttt{gi2}[i] = \frac{1}{1 + xn[i]},\quad \texttt{gi3}[i] = \frac{1 - xn[i]}{1 + xn[i]} \tag{5.9a,b}
$$

$$
xn[i] = \frac{\sigma_D[i]\Delta t}{2\varepsilon_0} \tag{5.10}
$$

### H-Field Updates with PML

**Hy update** (similar to D):

```python
# At i+1/2 position
Hy[i+1/2,j] = fi3[i+1/2] * Hy[i+1/2,j] 
             + fi2[i+1/2] * 0.5 * (Ez[i+1,j] - Ez[i,j])
```

where `fi2, fi3` are calculated with `xn[i+1/2]` at half-cell positions.

**Hx update** (uses auxiliary current $I_{Hx}$ to handle the inverse permeability):

```python
curl_e = Ez[i,j] - Ez[i,j+1]                          # (5.11a)
IHx[i,j+1/2] = IHx[i,j+1/2] + curl_e                  # (5.11b) history integral
Hx[i,j+1/2] = Hx[i,j+1/2] + 0.5 * curl_e 
             + fi1[i] * IHx[i,j+1/2]                  # (5.11c)
```

where `fi1[i] = xn[i]`.

### Full 2D PML (X and Y directions)

When PML is applied on all four sides, the D-field update combines both directions:

$$
D_z^{n+1/2}[i,j] = \texttt{gi3}[i]\,\texttt{gj3}[j]\,D_z^{n-1/2}[i,j] + \texttt{gi2}[i]\,\texttt{gj2}[j]\cdot 0.5\bigl(H_y^{n}[i+1/2,j] - H_y^{n}[i-1/2,j] - H_x^{n}[i,j+1/2] + H_x^{n}[i,j-1/2]\bigr) \tag{5.12}
$$

Hy in the y-direction uses an auxiliary current `IHy`, similar to IHx in x.

### PML Profile and Parameters

The conductivity $\sigma_D$ grows quadratically from the boundary inward:

```python
for i in range(1, length_pml+1):
    xn[i] = 0.333 * (i / length_pml) ** 3

fi1[i] = xn[i]
gi2[i] = 1 / (1 + xn[i])
gi3[i] = (1 - xn[i]) / (1 + xn[i])
fi2[i] = 1 / (1 + xn[i+0.5])   # half-cell
fi3[i] = (1 - xn[i+0.5]) / (1 + xn[i+0.5])
```

Parameters range:

| Parameter | At boundary | At depth |
|---|---|---|
| fi1, fj1 | 0 → 0.333 | 0 (interior) |
| fi2, gi2, fj2, gj2 | 1 → 0.75 | 1 |
| fi3, gi3, fj3, gj3 | 1 → 0.5 | 1 |

> **Empirical insight:** The factor 0.333 and cubic profile were found empirically to provide the best absorption without numerical instability.

### Physical Interpretation

The PML is essentially a **graded anisotropic absorber**. Impedance is matched at every point so waves enter without reflection. The imaginary part of the complex permittivity/permeability causes exponential decay. At depth 8 cells inside the PML, the wave has essentially decayed to near zero, making the outer boundary condition irrelevant.

---

## 5.3 Total-Field/Scattered-Field (TF/SF) Formulation

### Why TF/SF?

Simulating plane waves in FDTD requires careful handling:
1. The incident wave should not interact with ABCs
2. The load on ABCs should be minimized (only **scattered** fields should reach them)

Solution: Divide the problem space into two regions:
- **Total field region:** contains both incident + scattered waves
- **Scattered field region:** contains only scattered waves

### TF/SF Boundary

At the boundary (dashed line in Fig. 5.5), the update formulas that use points on the other side must be corrected using the **incident field array** (1D auxiliary array).

**Three correction locations:**

1. **Dz at bottom (j=ja) and top (j=jb):**
```python
dz[i, ja] += 0.5 * Hx_inc[ja-1]   # (5.13a)
dz[i, jb] -= 0.5 * Hx_inc[jb+1]   # (5.13b)
```

2. **Hx just outside at j=ja and j=jb:**
```python
Hx[i, ja-1/2] += 0.5 * Ez_inc[ja]   # (5.14a)
Hx[i, jb+1/2] -= 0.5 * Ez_inc[jb]   # (5.14b)
```

3. **Hy just outside at i=ia and i=ib:**
```python
Hy[ia-1/2, j] -= 0.5 * Ez_inc[j]   # (5.15a)
Hy[ib+1/2, j] += 0.5 * Ez_inc[j]   # (5.15b)
```

### Incident Array Generation

The incident field is a 1D array propagating in the +y direction (for this example). At each time step, a source is injected at `ja` and the wave propagates through the incident array using standard 1D FDTD updates. This 1D array is used to correct the TF/SF boundary.

### Plane Wave Pulse Generation

A Gaussian pulse in the incident array:
```python
pulse = exp(-0.5 * ((t0 - time_step) / spread)**2)
ez_inc[ja] = pulse + ez_inc[ja]   # inject at boundary
```

The same pulse is simultaneously subtracted at `jb`, ensuring no net energy accumulates at the boundary.

---

## 5.3.1 Plane Wave Impinging on a Dielectric Cylinder

### Object Specification

The cylinder is specified by dielectric constant $\varepsilon_r$ and conductivity $\sigma$:

```python
for j in range(ja, jb):
    for i in range(ia, ib):
        xdist = ic - i
        ydist = jc - j
        dist = sqrt(xdist**2 + ydist**2)
        if dist <= radius:
            gaz[i, j] = 1 / (epsr + sigma * dt / epsz)
            gbz[i, j] = sigma * dt / epsz
```

> **Limitation:** "In-or-out" specification causes **staircasing** — the curved boundary is approximated as blocky steps. This is the fundamental accuracy limitation of FDTD on curved geometries.

### Subcell Averaging (Smoother Boundaries)

A 3×3 subcell averaging technique reduces staircasing:

```python
for j in range(ja, jb):
    for i in range(ia, ib):
        eps = 1.0
        cond = 0.0
        for jj in range(-1, 2):
            for ii in range(-1, 2):
                xdist = (ic - i) + (1/3) * ii
                ydist = (jc - j) + (1/3) * jj
                dist = sqrt(xdist**2 + ydist**2)
                if dist <= radius:
                    eps += (1/9) * (epsr - 1)
                    cond += (1/9) * sigma
        gaz[i,j] = 1.0 / (eps + cond * dt / epsz)
        gbz[i,j] = cond * dt / epsz
```

Each cell is divided into 9 subcells; the fraction of the cell inside the cylinder determines the effective permittivity and conductivity.

### Physical Results

Fig. 5.9: Plane wave with $\varepsilon_r = 30$, $\sigma = 0.3$ hits a 20 cm diameter cylinder.
- At T=25: incident pulse just starting
- At T=50: pulse interacting with cylinder — part transmitted, part scattered around
- At T=75: main pulse leaving total field region; only scattered field reaches PML

### Fourier Analysis and Validation

Because the dielectric cylinder has an **analytical solution** (Bessel function expansion), we can validate FDTD accuracy. The discrete Fourier transform is used to extract the frequency response at 50, 300, and 700 MHz from a single Gaussian pulse simulation.

> **Numerical validation:** Fig. 5.10 shows excellent agreement between FDTD and analytical Bessel function solutions along the center axis. This confirms the TF/SF + DFT methodology is working correctly.

---

## Code Reference

### Basic 2D TM FDTD (`fd2d_3_1.py`)

```python
import numpy as np
from matplotlib import pyplot as plt

ie = 60  # x-direction size
je = 60  # y-direction size

dz = np.zeros((ie, je))
ez = np.zeros((ie, je))
hx = np.zeros((ie, je))
hy = np.zeros((ie, je))
gaz = np.ones((ie, je))

# Gaussian pulse source at center
ic = ie // 2
jc = je // 2
t0 = 20
spread = 8

nsteps = 50
for time_step in range(1, nsteps + 1):
    # D-field update
    for j in range(1, je):
        for i in range(1, ie):
            dz[i, j] += 0.5 * (hy[i, j] - hy[i-1, j] 
                              - hx[i, j] + hx[i, j-1])
    
    # Inject Gaussian pulse
    pulse = np.exp(-0.5 * ((t0 - time_step) / spread)**2)
    ez[ic, jc] = pulse
    
    # E-field from D
    for j in range(1, je):
        for i in range(1, ie):
            ez[i, j] = gaz[i, j] * dz[i, j]
    
    # Hx update
    for j in range(1, je-1):
        for i in range(1, ie):
            hx[i, j] += 0.5 * (ez[i, j] - ez[i, j+1])
    
    # Hy update
    for j in range(1, je):
        for i in range(1, ie-1):
            hy[i, j] += 0.5 * (ez[i+1, j] - ez[i, j])
```

### 2D PML Code (`fd2d_3_2.py` — 8-cell PML)

```python
# PML parameters
length_pml = 8

# Initialize PML parameters
xn = np.zeros(ie)
fi1 = np.zeros(ie)
gi2 = np.ones(ie)
gi3 = np.ones(ie)
fi2 = np.ones(ie)
fi3 = np.ones(ie)

# X-direction PML
for i in range(1, length_pml + 1):
    xn[i] = 0.333 * (i / length_pml) ** 3
    fi1[i] = xn[i]
    gi2[i] = 1 / (1 + xn[i])
    gi3[i] = (1 - xn[i]) / (1 + xn[i])
    fi2[i] = 1 / (1 + xn[i+0.5])
    fi3[i] = (1 - xn[i+0.5]) / (1 + xn[i+0.5])

# For Y-direction, similar arrays: yn, fj1, gj2, gj3, fj2, fj3

# D-field update with PML
for j in range(1, je):
    for i in range(1, ie):
        dz[i,j] = gi3[i] * gj3[j] * dz[i,j] \
                + gi2[i] * gj2[j] * 0.5 * (
                  hy[i,j] - hy[i-1,j] 
                - hx[i,j] + hx[i,j-1])

# E-field from D
for j in range(1, je):
    for i in range(1, ie):
        ez[i,j] = gaz[i,j] * dz[i,j]

# Hx update with PML (requires IHx auxiliary field)
for j in range(1, je-1):
    for i in range(1, ie):
        curl_e = ez[i,j] - ez[i,j+1]
        IHx[i,j+1] += curl_e
        hx[i,j] += 0.5 * curl_e + fi1[i] * IHx[i,j+1]

# Hy update with PML (requires IHy auxiliary field)
for j in range(1, je):
    for i in range(1, ie-1):
        curl_e = ez[i+1,j] - ez[i,j]
        IHy[i+1,j] += curl_e
        hy[i,j] += 0.5 * curl_e + fj1[j] * IHy[i,j]
```

> **Physical intuition:** The `fi1 * IHx` term adds the conductive loss effect at the PML boundary. As the wave enters the PML, the curl_e field is attenuated by the exponential factor in `IHx` accumulation, and the `fi1` coefficient controls how aggressively the loss kicks in.

---

## Key Equations Summary

| Equation | Name | Physical Meaning |
|---|---|---|
| (5.1a-d) | 2D TM Maxwell equations | Reduced from 3D; only $E_z, H_x, H_y$ |
| (5.2a-d) | 2D TM FDTD updates | Yee grid on a plane |
| (5.4) | PML impedance match | $\eta=1$ at every point |
| (5.5) | PML anisotropic indexing | Inverse relationship between directions |
| (5.8) | D-field update with PML | Attenuated by gi3 coefficient |
| (5.11a-c) | Hx update with PML | Uses IHx auxiliary current for inverse $\mu$ |
| (5.13a-b) | TF/SF Dz correction | Adds incident Hx contribution at boundary |