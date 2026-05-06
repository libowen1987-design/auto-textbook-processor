---
title: "More on One-Dimensional Simulation — Z Transform Formulation"
author: "Jennifer E. Houle and Dennis M. Sullivan"
book: "Electromagnetic Simulation Using the FDTD Method with Python, Third Edition"
chapter: 4
---

## 4.1 Z Transform Formulation for Frequency-Dependent Media

### The Z Transform Advantage

Chapter 3 showed how to handle frequency-dependent media via a convolution approach. The **Z transform** method provides an equivalent but more elegant formulation — particularly valuable as media become more complex.

Starting from the frequency-domain permittivity of a Debye medium:

$$
\varepsilon_r^*(\omega) = \varepsilon_r + \frac{\sigma}{j\omega\varepsilon_0} + \frac{\chi_1}{1 + j\omega\tau} \tag{4.1}
$$

Going to the **Z domain** directly:

$$
D(z) = \varepsilon_r E(z) + \frac{\sigma\Delta t}{\varepsilon_0}\frac{1 - z^{-1}}{1} E(z) + \frac{\chi_1\Delta t}{\tau}\frac{1 - e^{-\Delta t/\tau}z^{-1}}{1} E(z) \tag{4.2}
$$

### Defining Auxiliary Parameters in Z Domain

Define two auxiliary Z-domain variables:

$$
I(z) = \frac{\sigma\Delta t}{\varepsilon_0}(1 - z^{-1})E(z) = z^{-1}I(z) + \frac{\sigma\Delta t}{\varepsilon_0}E(z) \tag{4.3a}
$$

$$
S(z) = \frac{\chi_1\Delta t}{\tau}(1 - e^{-\Delta t/\tau}z^{-1})E(z) = e^{-\Delta t/\tau}z^{-1}S(z) + \frac{\chi_1\Delta t}{\tau}E(z) \tag{4.3b}
$$

Eq. (4.2) becomes:

$$
D(z) = \varepsilon_r E(z) + z^{-1}I(z) + \frac{\sigma\Delta t}{\varepsilon_0}E(z) + e^{-\Delta t/\tau}z^{-1}S(z) + \frac{\chi_1\Delta t}{\tau}E(z) \tag{4.4}
$$

Solving for $E(z)$:

$$
E(z) = \frac{D(z) - z^{-1}I(z) - e^{-\Delta t/\tau}z^{-1}S(z)}{\varepsilon_r + \frac{\sigma\Delta t}{\varepsilon_0} + \frac{\chi_1\Delta t}{\tau}} \tag{4.5}
$$

### Direct Sampled-Time Translation

The **key advantage** of Z transforms: to go to sampled time domain, simply replace:
- $E(z) \rightarrow E^n$
- $z^{-1}E(z) \rightarrow E^{n-1}$
- $z^{-1}I(z) \rightarrow I^{n-1}$
- $z^{-1}S(z) \rightarrow S^{n-1}$

This yields exactly the same equations as the convolution approach (Eq. 3.24):

$$
E^n = \frac{D^n - I^{n-1} - e^{-\Delta t/\tau}S^{n-1}}{\varepsilon_r + \frac{\sigma\Delta t}{\varepsilon_0} + \frac{\chi_1\Delta t}{\tau}} \tag{4.6a}
$$

$$
I^n = I^{n-1} + \frac{\sigma\Delta t}{\varepsilon_0}E^n \tag{4.6b}
$$

$$
S^n = e^{-\Delta t/\tau}S^{n-1} + \frac{\chi_1\Delta t}{\tau}E^n \tag{4.6c}
$$

> **Why Z transforms?** We avoided dealing with convolution integrals and their approximations. As we move to more complicated multi-pole models (Lorentz), the Z transform formulation scales elegantly — you write the Z-domain expression directly from the frequency-domain model.

---

## 4.2 Simulation of an Unmagnetized Plasma

### Plasma Permittivity

The permittivity of an unmagnetized plasma is:

$$
\varepsilon^*(\omega) = 1 + \frac{\omega_p^2}{\nu_c + j\omega} \tag{4.7}
$$

where:
- $\omega_p = 2\pi f_p$ — **plasma frequency** (rad/s)
- $f_p$ — plasma frequency (Hz)
- $\nu_c$ — electron collision frequency (rad/s)

> **Physical intuition:** Below $\omega_p$, the plasma behaves like a metal (reflects waves). Above $\omega_p$, it becomes transparent. This is why metals appear reflective — their plasma frequencies are in the UV range.

### Partial Fraction Expansion

Rewriting Eq. (4.7):

$$
\varepsilon^*(\omega) = 1 + \frac{\omega_p^2}{\nu_c}\frac{1}{j\omega} - \frac{\omega_p^2}{\nu_c}\frac{1}{\nu_c + j\omega} \tag{4.8}
$$

This resembles the Debye form — two pole terms.

### Z Domain Formulation

Taking the Z transform:

$$
\varepsilon^*(z) = 1 + \frac{\omega_p^2\Delta t}{\nu_c}\frac{1 - z^{-1}}{1} - \frac{\omega_p^2\Delta t}{\nu_c}\frac{1 - e^{-\nu_c\Delta t}z^{-1}}{1} \tag{4.9}
$$

By the convolution theorem, $D(z) = \varepsilon^*(z)E(z)\Delta t$:

$$
D(z) = E(z) + \frac{\omega_p^2\Delta t}{\nu_c}\frac{1 - e^{-\nu_c\Delta t}z^{-1}}{1 - z^{-1} + e^{-\nu_c\Delta t}z^{-1} - e^{-\nu_c\Delta t}z^{-2}}E(z) \tag{4.10}
$$

### Auxiliary Variable S(z)

Define:

$$
S(z) = \frac{\omega_p^2\Delta t}{\nu_c}\frac{1 - e^{-\nu_c\Delta t}}{1 - z^{-1} + e^{-\nu_c\Delta t}z^{-1} - e^{-\nu_c\Delta t}z^{-2}}E(z) \tag{4.11}
$$

Then:

$$
E(z) = D(z) - z^{-1}S(z) \tag{4.12a}
$$

$$
S(z) = (1 + e^{-\nu_c\Delta t}z^{-1})S(z) - e^{-\nu_c\Delta t}z^{-2}S(z) + \frac{\omega_p^2\Delta t}{\nu_c}(1 - e^{-\nu_c\Delta t})E(z) \tag{4.12b}
$$

### FDTD Implementation (1D Plasma)

```python
# E field update (Eq. 4.13a)
ex[k] = dx[k] - sx[k]

# S update (Eq. 4.13b) - requires TWO previous values of S
sxm1 = sxm2  # shift sxm2 → sxm1
sxm2 = sxm1_new  # shift previous sx → sxm2 (before update)
sx = (1 + np.exp(-vc*dt)) * sxm1 - np.exp(-vc*dt) * sxm2 \
     + (omega**2 * dt / vc) * (1 - np.exp(-vc*dt)) * ex[k]
```

```python
# From fd1d_2_4.py (plasma simulation)
ex[k] = dx[k] - sx[k]

sxm2[k] = sxm1[k]
sxm1[k] = sx[k]
sx[k] = (1 + np.exp(-vc*dt)) * sxm1[k] \
        - np.exp(-vc*dt) * sxm2[k] \
        + (omega**2 * dt / vc) * (1 - np.exp(-vc*dt)) * ex[k]
```

### Physical Example: Silver Plasma

Silver properties:
- $\omega_p = 2\pi \times 2000$ THz (plasma frequency in visible/UV)
- $\nu_c = 57$ THz (collision frequency)

At **500 THz** (below plasma frequency, Fig. 4.4): The wave is almost completely **reflected** — the plasma behaves like a metal barrier.

At **4000 THz** (above plasma frequency, Fig. 4.5): The majority of the pulse **passes through** — the plasma becomes transparent.

> **Numerical considerations:** At 4000 THz, free-space wavelength $\lambda = c_0/f = 3\times10^8 / 4\times10^{15} = 0.075\,\mu\text{m}$. With 10 points/wavelength rule, $\Delta x \approx 7.5$ nm. The textbook uses $\Delta x = 5$ nm for 500 THz and $\Delta x = 10$ nm for 4000 THz (larger cells acceptable since the pulse is broadband).

---

## 4.3 Formulating a Lorentz Medium

### The Lorentz Model (Two-Pole)

The Debye model has a single pole. The **Lorentz model** introduces a second pole, enabling resonance behavior:

$$
\varepsilon_r^*(\omega) = \varepsilon_r + \frac{\varepsilon_1}{1 + j2\delta_0\frac{\omega}{\omega_0} - \left(\frac{\omega}{\omega_0}\right)^2} \tag{4.13}
$$

Parameters:
- $\varepsilon_r$: static relative dielectric constant
- $\varepsilon_1$: resonance strength
- $\omega_0 = 2\pi f_0$: resonant frequency
- $\delta_0$: damping factor (dimensionless)

### Example Lorentz Medium Properties

$$
\varepsilon_r = 2,\quad \varepsilon_1 = 2,\quad f_0 = 100\text{ MHz},\quad \delta_0 = 0.25
$$

This produces a **resonance** in both $\varepsilon_r'$ and $\sigma$ near $f_0 = 100$ MHz, unlike the Debye medium which shows monotonic behavior.

### ADE Method for Lorentz

Starting from:

$$
S(\omega) = \frac{\varepsilon_1\omega_0^2}{\omega_0^2 + j2\delta_0\omega_0\omega - \omega^2}E(\omega) \tag{4.14}
$$

Rearrange to the auxiliary differential equation form:

$$
(\omega_0^2 + j2\delta_0\omega_0\omega - \omega^2)S(\omega) = \omega_0^2\varepsilon_1 E(\omega) \tag{4.15}
$$

Going to continuous time domain:

$$
\omega_0^2 S(t) + 2\delta_0\omega_0\frac{dS(t)}{dt} + \frac{d^2S(t)}{dt^2} = \omega_0^2\varepsilon_1 E(t) \tag{4.16}
$$

### Finite Difference Approximation

The second-order derivative generates **two-time-step** differencing:

$$
\frac{d^2S}{dt^2} \approx \frac{S^n - 2S^{n-1} + S^{n-2}}{\Delta t^2} \tag{4.17}
$$

The first-order derivative is taken over **two time steps** (centered difference):

$$
\frac{dS}{dt} \approx \frac{S^n - S^{n-2}}{2\Delta t} \tag{4.18}
$$

Substituting into Eq. (4.16) and solving for $S^n$:

$$
S^n = \frac{\frac{2 - \Delta t^2\omega_0^2}{1 + \Delta t\delta_0\omega_0}S^{n-1} - \frac{1 - \Delta t\delta_0\omega_0}{1 + \Delta t\delta_0\omega_0}S^{n-2} + \frac{\Delta t^2\omega_0^2\varepsilon_1}{1 + \Delta t\delta_0\omega_0}E^{n-1}}{} \tag{4.19}
$$

### Alternative Z Transform Method

An equivalent approach using Z transforms (from Table A.1):

$$
S(z) = \frac{e^{-\alpha\Delta t}\sin(\beta\Delta t)}{\Delta t}z^{-1} \cdot \frac{\gamma\varepsilon_1}{1 - 2e^{-\alpha\Delta t}\cos(\beta\Delta t)z^{-1} + e^{-2\alpha\Delta t}z^{-2}}E(z) \tag{4.20}
$$

where:
- $\gamma = \omega_0/\sqrt{1-\delta_0^2}$
- $\alpha = \delta_0\omega_0$
- $\beta = \omega_0\sqrt{1-\delta_0^2}$

Sampled time domain:

$$
S^n = 2e^{-\alpha\Delta t}\cos(\beta\Delta t)S^{n-1} - e^{-2\alpha\Delta t}S^{n-2} + e^{-\alpha\Delta t}\sin(\beta\Delta t)\Delta t\gamma\varepsilon_1 E^{n-1} \tag{4.21}
$$

> **Verification:** Both methods are equivalent when $\beta\Delta t \ll 1$ and $\delta_0 \ll 1$ (Taylor series approximations).

---

## 4.3.1 Simulation of Human Muscle Tissue

### Cole-Cole Model for Biological Tissue

Human muscle tissue is highly dispersive. Over approximately two decades of frequency, it follows a modified Lorentz (Cole-Cole) model:

$$
\varepsilon_r^*(\omega) = \varepsilon_r + \frac{\sigma}{j\omega\varepsilon_0} + \varepsilon_1\frac{\omega_0}{\omega_0^2 + \alpha^2 + j\omega 2\alpha - \omega^2} \tag{4.22}
$$

where $\alpha$ is related to the relaxation distribution.

### Muscle Tissue Properties (Table 4.1)

| Frequency (MHz) | $\varepsilon_r'$ | $\sigma$ (S/m) |
|---|---|---|
| 10   | 160   | 0.625 |
| 40   | 97    | 0.693 |
| 100  | 72    | 0.89  |
| 200  | 56.5  | 1.28  |
| 300  | 54    | 1.37  |
| 433  | 53    | 1.43  |
| 915  | 51    | 1.60  |

> **Physical intuition:** Muscle is lossy and water-rich. At low MHz frequencies (like 10 MHz), the high dielectric constant (~160) reflects the bound water response. As frequency increases, the water molecules can't follow the alternating field as well, so $\varepsilon_r$ drops and $\sigma$ increases.

### Z Domain Formulation for Muscle

Taking the Z transform of Eq. (4.22):

$$
D(z) = \varepsilon_r E(z) + \frac{\sigma\Delta t}{\varepsilon_0}(1 - z^{-1})E(z) + \varepsilon_1\frac{e^{-\alpha\Delta t}\sin(\omega_0\Delta t)\Delta t z^{-1}}{1 - 2e^{-\alpha\Delta t}\cos(\omega_0\Delta t)z^{-1} + e^{-2\alpha\Delta t}z^{-2}}E(z) \tag{4.23}
$$

Define two auxiliary parameters:

$$
I(z) = \frac{\sigma\Delta t}{\varepsilon_0}(1 - z^{-1})E(z) \tag{4.24a}
$$

$$
S(z) = \varepsilon_1\frac{e^{-\alpha\Delta t}\sin(\omega_0\Delta t)\Delta t}{1 - 2e^{-\alpha\Delta t}\cos(\omega_0\Delta t)z^{-1} + e^{-2\alpha\Delta t}z^{-2}}z^{-1}E(z) \tag{4.24b}
$$

Then:

$$
D(z) = \varepsilon_r E(z) + I(z) + z^{-1}S(z) \tag{4.25}
$$

### FDTD Update Equations for Muscle Tissue

$$
E(z) = \frac{D(z) - z^{-1}I(z) - z^{-1}S(z)}{\varepsilon_r + \frac{\sigma\Delta t}{\varepsilon_0}} \tag{4.26a}
$$

$$
I(z) = z^{-1}I(z) + \frac{\sigma\Delta t}{\varepsilon_0}E(z) \tag{4.26b}
$$

$$
S(z) = 2e^{-\alpha\Delta t}\cos(\omega_0\Delta t)z^{-1}S(z) - e^{-2\alpha\Delta t}z^{-2}S(z) + \varepsilon_1 e^{-\alpha\Delta t}\sin(\omega_0\Delta t)\Delta t\, E(z) \tag{4.26c}
$$

> **Note:** Eq. (4.26c) requires storing **two previous values** of $S$ ($S^{n-1}$ and $S^{n-2}$), as well as two previous values of $I$ ($I^{n-1}$ only needed for $I$, but $S$ needs full history).

---

## Code Reference

### Z Transform Plasma Code (`fd1d_2_4.py`)

```python
# 1D FDTD Plasma Simulation
# Silver: fp = 2000 THz, vc = 57 THz
# For 500 THz: dx = 10 nm; for 4000 THz: dx = 5 nm

omega = 2 * np.pi * freq_in   # rad/s
vc = np.ones(ke) * 1e12        # very small for free space
vc[plasma_start:] = 57e12      # collision freq for silver

# Plasma update coefficients
exp_vc_dt = np.exp(-vc * dt)
coef1 = 1 + exp_vc_dt
coef2 = -exp_vc_dt
coef3 = (omega**2 * dt / vc) * (1 - exp_vc_dt)

# S field update (requires sxm1 and sxm2)
sxm2 = sxm1
sxm1 = sx
sx = coef1 * sxm1 + coef2 * sxm2 + coef3 * ex[k]
ex[k] = dx[k] - sx[k]
```

### Lorentz Medium Code

```python
# Lorentz parameters
gamma = omega0 / np.sqrt(1 - delta0**2)
alpha = delta0 * omega0
beta = omega0 * np.sqrt(1 - delta0**2)

exp_alpha_dt = np.exp(-alpha * dt)
cos_beta_dt = np.cos(beta * dt)
sin_beta_dt = np.sin(beta * dt)

# Z-domain coefficients
a0 = 2 * exp_alpha_dt * cos_beta_dt
a1 = -exp_alpha_dt**2
a2 = exp_alpha_dt * sin_beta_dt * dt * gamma * epsilon1

# Update
Sn = a0 * Sn_prev1 + a1 * Sn_prev2 + a2 * En_prev1
En = (Dn - Sn) / epsr
```

### Human Muscle Tissue Code (Cole-Cole)

```python
# From fd1d_2_5.py
# Muscle tissue: epsr=50, sigma=1.6 S/m @ 915 MHz
# Two auxiliary parameters: I (conductive), S (Lorentz Debye)
# S requires sxm1 and sxm2

epsr = 50
sigma = 1.6

gax = 1.0 / (epsr + sigma * dt / epsz)
gbx = sigma * dt / epsz

# S update (two previous values)
sxm2 = sxm1
sxm1 = sx
sx = (1 + exp_alpha_dt * cos_omega0_dt) * sxm1 \
     - exp_alpha_dt**2 * sxm2 \
     + epsilon1 * exp_alpha_dt * sin_omega0_dt * dt * ex[k]

ex[k] = gax * (dx[k] - ix[k] - sx[k])
ix[k] = ix[k] + gbx * ex[k]
```

---

## Key Equations Summary

| Equation | Name | Physical Meaning |
|---|---|---|
| (4.7) | Plasma permittivity | $\omega_p$ determines metal vs. dielectric behavior |
| (4.10) | Z-domain plasma permittivity | Two-pole form similar to Debye |
| (4.12a-b) | Plasma FDTD update | $S$ requires two-step history |
| (4.13) | Lorentz model | Two-pole resonance with damping |
| (4.19) | ADE Lorentz update | $S^n$ uses $S^{n-1}, S^{n-2}, E^{n-1}$ |
| (4.21) | Z-transform Lorentz update | Equivalent exponential form |
| (4.22) | Cole-Cole (muscle) model | Lossy dispersive biological tissue |
| (4.26a-c) | Muscle tissue FDTD update | Three auxiliary variables: $E$, $I$, $S$ |