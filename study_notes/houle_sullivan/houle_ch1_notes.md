# Chapter 1 — One-Dimensional Simulation with the FDTD Method

> **Source:** Houle & Sullivan, *Electromagnetic Simulation Using the FDTD Method with Python*, 3rd ed. (IEEE Press, 2020), Ch. 1  
> **Raw:** `/tmp/houle_ch1_raw.txt` (front matter) + `/tmp/houle_ch2_raw.txt` (chapter content, lines 27–915)  
> **Status:** ✅ Complete

---

## 1.1 One-Dimensional Free-Space Simulation

### Maxwell's Equations in 1D Free Space

For a plane wave propagating in the $z$-direction with $\mathbf{E}$ in $x$ and $\mathbf{H}$ in $y$:

$$
\frac{\partial E_x}{\partial t} = -\frac{1}{\varepsilon_0} \frac{\partial H_y}{\partial z} \tag{1.2a}
$$
$$
\frac{\partial H_y}{\partial t} = -\frac{1}{\mu_0} \frac{\partial E_x}{\partial z} \tag{1.2b}
$$

### Central Difference Discretization (Yee Grid)

Using central differences in both time and space:

$$
E_x^{n+\frac{1}{2}}[k] = E_x^{n-\frac{1}{2}}[k] - \frac{\Delta t}{\varepsilon_0 \Delta x}\left(H_y^n[k+\tfrac{1}{2}] - H_y^n[k-\tfrac{1}{2}]\right) \tag{1.4a}
$$
$$
H_y^{n+1}[k+\tfrac{1}{2}] = H_y^n[k+\tfrac{1}{2}] - \frac{\Delta t}{\mu_0 \Delta x}\left(E_x^{n+\frac{1}{2}}[k+1] - E_x^{n+\frac{1}{2}}[k]\right) \tag{1.4b}
$$

### Normalized Field Variables

Define: $\quad \tilde{E}_x = \sqrt{\varepsilon_0/\mu_0}\;E_x$

This gives $\tilde{E}_x$ and $H_y$ the same order of magnitude (key advantage for PML formulation):

$$
\tilde{E}_x^{n+\frac{1}{2}}[k] = \tilde{E}_x^{n-\frac{1}{2}}[k] - \frac{1}{2}\left(H_y^n[k+\tfrac{1}{2}] - H_y^n[k-\tfrac{1}{2}]\right) \tag{1.6a}
$$
$$
H_y^{n+1}[k+\tfrac{1}{2}] = H_y^n[k+\tfrac{1}{2}] - \frac{1}{2}\left(\tilde{E}_x^{n+\frac{1}{2}}[k+1] - \tilde{E}_x^{n+\frac{1}{2}}[k]\right) \tag{1.6b}
$$

The factor $\frac{\Delta t}{\varepsilon_0\mu_0\Delta x} = \frac{1}{2}$ follows from choosing $\Delta t = \Delta x/(2c_0)$.

### Python Implementation (1D FDTD core loop)

```python
# ex[k] = ex[k] + 0.5 * (hy[k-1] - hy[k])   # Update E field
# hy[k] = hy[k] + 0.5 * (ex[k] - ex[k+1])   # Update H field
```

Key points:
- E and H updates use **separate loops** (interleaved in space and time)
- **Hard source**: override `ex[kc] = pulse` after E-update
- $E_x$ is positive in both propagation directions; $H_y$ changes sign with direction
- Without absorbing boundaries, the pulse reflects at grid edges

---

## 1.2 Stability and the FDTD Method

### Courant–Friedrichs–Lewy (CFL) Stability Condition

An EM wave in free space cannot travel faster than $c_0$. To propagate one cell requires $\Delta t \geq \Delta x / c_0$.

General dimension-`n` CFL condition:

$$
\Delta t = \frac{\Delta x}{n \, c_0} \tag{1.10}
$$

For 1D: $\Delta t = \Delta x / c_0$; the book uses $\Delta t = \Delta x/(2c_0)$ for simplicity to avoid square roots.

**If coefficient 0.5 is changed to 1.0 → instability (field grows without bound).**  
**If changed to 0.25 → stable but overly dissipative.**

---

## 1.3 The Absorbing Boundary Condition (ABC) in One Dimension

### Concept

At the grid edge, FDTD needs $H$ values on one side that don't exist. Absorbing boundary conditions prevent outgoing waves from reflecting back into the problem space.

### First-Order ABC (Mur, 1981)

For a forward-traveling wave: $\quad \frac{\partial E}{\partial t} + c_0 \frac{\partial E}{\partial z} = 0$

In normalized units ($c_0=1$, $\Delta x = \Delta t = 1$): $E[0]^{n+1} = E[1]^n$ (left boundary).

Implementation:
```python
# Left boundary (k=0)
ex[0] = ex_prev_left   # stored from previous step
ex_prev_left = ex[1]   # update stored value

# Right boundary (k=ke-1)
ex[ke-1] = ex_prev_right
ex_prev_right = ex[ke-2]
```

Higher-order ABCs exist but first-order is sufficient for many 1D problems.

---

## 1.4 Propagation in a Dielectric Medium

### Formulation with Permittivity $\varepsilon_r$

When $\varepsilon = \varepsilon_r \varepsilon_0$:

$$
E_x^{n+\frac{1}{2}}[k] = E_x^{n-\frac{1}{2}}[k] - \frac{1}{2\varepsilon_r}\left(H_y^n[k+\tfrac{1}{2}] - H_y^n[k-\tfrac{1}{2}]\right) \tag{1.17}
$$

Python update: `ex[k] = ex[k] + (1/eps_r) * (hy[k-1] - hy[k])`

### Physical Consequences

| Property | Value |
|---|---|
| Wave speed in dielectric | $c = c_0 / \sqrt{\varepsilon_r}$ |
| Wavelength in dielectric | $\lambda = \lambda_0 / \sqrt{\varepsilon_r}$ |
| Intrinsic impedance | $\eta = \eta_0 / \sqrt{\varepsilon_r}$ |

---

## 1.5 Simulating Different Sources

### Hard Source (Explicit Field Value)

```python
ex[kc] = pulse  # overrides computed value
```
Disadvantage: introduces spurious reflections if not smoothly ramped.

### Soft Source (Additive)

```python
ex[kc] += pulse  # adds to existing field
```
Less reflection, more physical.

### Magnetic Source (Hy injection)

```python
hy[kc-1] = -hy[kc]   # dipole-like magnetic source
```
Produces radiation pattern consistent with an oscillating magnetic dipole.

---

## 1.6 Determining Cell Size

### Resolution Requirement

To accurately model a wave, the spatial cell size $\Delta x$ must be small enough to resolve the shortest wavelength of interest:

$$
\Delta x \leq \frac{\lambda_{\min}}{10} \quad \text{(typical rule of thumb)}
$$

For a Gaussian pulse with spread $\sigma$, the effective bandwidth determines the minimum $\lambda$.

### Time Step Selection

Given $\Delta x$, the time step is set by the CFL condition:

$$
\Delta t = \frac{\Delta x}{2c_0} \quad \text{(1D, normalized)}
$$

### Normalized Units Summary

| Quantity | Normalized Value |
|---|---|
| $c_0$ | 1 |
| $\varepsilon_0$ | 1 |
| $\mu_0$ | 1 |
| $\Delta x$ | 1 |
| $\Delta t$ | 1 (in normalized system where $\Delta x = \Delta t$) |

---

## 1.7 Propagation in a Lossy Dielectric Medium

### Maxwell's Equations with Conductivity

$$
\frac{\partial E_x}{\partial t} = \frac{1}{\varepsilon} \frac{\partial H_y}{\partial z} - \frac{\sigma}{\varepsilon} E_x \tag{1.18}
$$

The conductivity term causes **exponential attenuation** of the wave as it propagates.

### FDTD Update Coefficients

Define: `eaf = dt * sigma / (2 * eps_r * eps0)`

$$
\text{ca}[k] = \frac{1 - \text{eaf}}{1 + \text{eaf}} \tag{1.23b}
$$
$$
\text{cb}[k] = \frac{0.5}{\varepsilon_r \cdot (1 + \text{eaf})} \tag{1.23c}
$$

Update: `ex[k] = ca[k] * ex[k] + cb[k] * (hy[k-1] - hy[k])`

### Physical Interpretation

| Parameter | Physical Meaning |
|---|---|
| $\sigma$ | Conductivity (S/m) |
| Loss tangent | $\tan\delta = \sigma / (\omega \varepsilon)$ |
| Penetration depth | $\delta_p = \sqrt{2 / (\omega \mu \sigma)}$ |

### PEC (Perfect Electric Conductor) Approximation

For metal: set $\sigma = 10^6$ (or any very large value). This makes `ca ≈ -1`, essentially zeroing the E field inside the conductor.

---

## 1.A Appendix — Reflection and Transmission at Dielectric Interfaces

### Reflection and Transmission Coefficients

For a plane wave incident from medium 1 onto medium 2:

$$
\Gamma = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1} = \frac{\varepsilon_1^* - \varepsilon_2^*}{\varepsilon_1^* + \varepsilon_2^*} \tag{1.A.4}
$$
$$
\tau = \frac{2\eta_2}{\eta_2 + \eta_1} = \frac{2\varepsilon_1^*}{\varepsilon_1^* + \varepsilon_2^*} \tag{1.A.5}
$$

### Complex Permittivity

$$
\varepsilon_r^* = \varepsilon_r + \frac{\sigma}{j\omega\varepsilon_0}
$$

### Wave Propagation in Lossy Medium

$$
E_x(z) = E_0 e^{-\alpha z} e^{-j\beta z}
$$

where $k = \omega\sqrt{\mu\varepsilon} = \alpha + j\beta$ and:

$$
\alpha = \omega\sqrt{\frac{\mu\varepsilon}{2}}\left[\sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} - 1\right]^{1/2}
$$
$$
\beta = \omega\sqrt{\frac{\mu\varepsilon}{2}}\left[\sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} + 1\right]^{1/2}
$$

---

## References (Chapter 1)

1. **Yee, K. S.** (1966), "Numerical solution of initial boundary value problems involving Maxwell's equations in isotropic media," *IEEE Trans. Antennas Propag.*, vol. 17, pp. 585–589.  
   → The foundational Yee algorithm paper (1966).

2. **Taflove, A. & Brodwin, M.** (1975), "Numerical solution of steady-state electromagnetic scattering problems using the time-dependent Maxwell's equations," *IEEE Trans. Microwave Theory Tech.*, vol. 23, pp. 623–730.

3. **Taflove, A.** (1995), *Computational Electrodynamics: The Finite-Difference Time-Domain Method*, 3rd Edition, Artech House, Boston, MA.

4. **Kunz, K. S. & Luebbers, R. J.** (1993), *The Finite Difference Time Domain Method for Electromagnetics*, CRC Press, Boca Raton, FL.

5. **Mur, G.** (1981), "Absorbing boundary conditions for the finite-difference approximation of the time domain electromagnetic field equations," *IEEE Trans. Electromagn. Compat.*, vol. 23, pp. 377–384.  
   → First-order ABC for FDTD.

6. **Cheng, D. K.** (1992), *Field and Wave Electromagnetics*, Addison-Wesley, Menlo Park, CA.

---

## Python Programs Summary (Chapter 1)

| Program | Description | Key Technique |
|---|---|---|
| `fd1d_1_1.py` | Free-space 1D FDTD, Gaussian pulse | Basic E/H interleaved updates |
| `fd1d_1_2.py` | Free-space with first-order ABC | Mur ABC at both boundaries |
| `fd1d_1_3.py` | Dielectric medium ($\varepsilon_r$) | Scaled E-update coefficient |
| `fd1d_1_4.py` | Hard source sinusoidal in lossy medium | ca/cb loss coefficients |
| `fd1d_1_5.py` | Sinusoid hitting lossy dielectric slab | Domain-specific loss parameters |

---

## Key Equations Master Index (Chapter 1)

| Eq. | Description |
|---|---|
| (1.1a,b) | Maxwell's curl equations, free space |
| (1.2a,b) | 1D reduction for $E_x$, $H_y$ propagating in $z$ |
| (1.4a,b) | FDTD discretized update equations (pre-normalization) |
| (1.5) | Normalized field definition: $\tilde{E} = \sqrt{\varepsilon_0/\mu_0}\;E$ |
| (1.6a,b) | Normalized FDTD update equations |
| (1.9a,b) | Python-executable FDTD core loop |
| (1.10) | General CFL stability condition: $\Delta t = \Delta x/(n c_0)$ |
| (1.11) | Book's simplified choice: $\Delta t = \Delta x/(2c_0)$ |
| (1.17) | E-field update in dielectric with $\varepsilon_r$ |
| (1.18) | Maxwell's equation with conductivity $\sigma$ |
| (1.22a,b) | Lossy dielectric FDTD update with ca, cb coefficients |
| (1.23a–c) | Loss coefficient definitions: `ca`, `cb` |
| (1.A.1–5) | Reflection/transmission coefficients at dielectric interface |
| (1.A.6) | Wave number in lossy dielectric: $k = \omega\sqrt{\mu\varepsilon_r^*}/c_0$ |