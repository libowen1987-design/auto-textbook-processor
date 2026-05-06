---
title: "More on One-Dimensional Simulation"
author: "Jennifer E. Houle and Dennis M. Sullivan"
book: "Electromagnetic Simulation Using the FDTD Method with Python, Third Edition"
chapter: 3
---

## 3.1 Reformulation Using the Flux Density

Until now we have used the form of Maxwell's equations given in Eq. (1.1), which uses only the **E** and **H** fields. A more general form uses the electric flux density **D**:

$$
\frac{\partial \mathbf{D}}{\partial t} = \nabla \times \mathbf{H} \tag{3.1a}
$$

$$
\mathbf{D}(\omega) = \varepsilon_0 \varepsilon_r^*(\omega) \mathbf{E}(\omega) \tag{3.1b}
$$

$$
\frac{\partial \mathbf{H}}{\partial t} = -\frac{1}{\mu_0} \nabla \times \mathbf{E} \tag{3.1c}
$$

where **D** is the electric flux density. Equation (3.1b) is written in the frequency domain to accommodate frequency-dependent materials (discussed in Section 3.3).

### Normalization

We normalize these equations using:

$$
\tilde{\mathbf{E}} = \sqrt{\frac{\varepsilon_0}{\mu_0}} \mathbf{E} \tag{3.2a}
$$

$$
\tilde{\mathbf{D}} = \frac{1}{\sqrt{\varepsilon_0 \mu_0}} \mathbf{D} \tag{3.2b}
$$

which yields:

$$
\frac{\partial \tilde{\mathbf{D}}}{\partial t} = \frac{1}{\varepsilon_0 \mu_0} \nabla \times \mathbf{H} \tag{3.3a}
$$

$$
\tilde{\mathbf{D}}(\omega) = \varepsilon_r^*(\omega) \tilde{\mathbf{E}}(\omega) \tag{3.3b}
$$

$$
\frac{\partial \mathbf{H}}{\partial t} = -\frac{1}{\varepsilon_0 \mu_0} \nabla \times \tilde{\mathbf{E}} \tag{3.3c}
$$

### From Frequency Domain to Time Domain: Lossy Dielectric

For a lossy dielectric medium:

$$
\varepsilon_r^*(\omega) = \varepsilon_r + \frac{\sigma}{j\omega \varepsilon_0} \tag{3.4}
$$

Substituting Eq. (3.4) into Eq. (3.3b):

$$
\tilde{D}(\omega) = \varepsilon_r \tilde{E}(\omega) + \frac{\sigma}{j\omega \varepsilon_0} \tilde{E}(\omega) \tag{3.5}
$$

The second term requires converting $1/(j\omega)$ — Fourier theory tells us this corresponds to **integration in time**:

$$
D(t) = \varepsilon_r E(t) + \frac{\sigma}{\varepsilon_0} \int_0^t E(t')\, dt' \tag{3.6}
$$

In the **sampled time domain**, the integral becomes a summation over time steps $\Delta t$:

$$
D^n = \varepsilon_r E^n + \frac{\sigma \Delta t}{\varepsilon_0} \sum_{i=0}^{n} E^i \tag{3.7}
$$

> **Physical intuition:** The summation term accumulates the history of the electric field weighted by the conductivity $\sigma$. High $\sigma$ → more charge accumulation → greater loss.

### Decoupling the Current $E^n$ Term

Eq. (3.7) requires $E^n$ on both sides. We separate the $E^n$ term from the rest of the summation:

$$
D^n = \varepsilon_r E^n + \frac{\sigma \Delta t}{\varepsilon_0} E^n + \frac{\sigma \Delta t}{\varepsilon_0} \sum_{i=0}^{n-1} E^i
$$

Solving for $E^n$:

$$
E^n = \frac{D^n - I^{n-1}}{\varepsilon_r + \frac{\sigma \Delta t}{\varepsilon_0}} \tag{3.8a}
$$

where we define the **auxiliary parameter** (accumulated current):

$$
I^{n-1} = \frac{\sigma \Delta t}{\varepsilon_0} \sum_{i=0}^{n-1} E^i \tag{3.8b}
$$

The update for $I$ at each time step:

$$
I^n = I^{n-1} + \frac{\sigma \Delta t}{\varepsilon_0} E^n \tag{3.9}
$$

### Final FDTD Formulation (1D)

Using the same 1D orientation as Chapter 1 (field polarized in $\hat{x}$, propagation in $\hat{z}$):

$$
D_x^{n+1}[k] = D_x^n[k] + 0.5 \cdot (H_y^n[k-1] - H_y^n[k]) \tag{3.10a}
$$

$$
E_x^{n+1}[k] = \texttt{gax}[k] \cdot D_x^{n+1}[k] - \texttt{ix}[k] \tag{3.10b}
$$

$$
I_x^{n+1}[k] = I_x^n[k] + \texttt{gbx}[k] \cdot E_x^{n+1}[k] \tag{3.10c}
$$

$$
H_y^{n+1}[k] = H_y^n[k] + 0.5 \cdot (E_x^{n+1}[k] - E_x^{n+1}[k+1]) \tag{3.10d}
$$

where the **media coefficients** are:

$$
\texttt{gax}[k] = \frac{1}{\varepsilon_r + \frac{\sigma \Delta t}{\varepsilon_0}} \tag{3.11a}
$$

$$
\texttt{gbx}[k] = \frac{\sigma \Delta t}{\varepsilon_0} \tag{3.11b}
$$

> **Key insight:** All media information is contained in Eq. (3.10b) and (3.10c). Equations (3.10a) and (3.10d) — the spatial derivatives — remain **unchanged** regardless of the medium.

For **free space**: `gax = 1`, `gbx = 0`.
For **lossy material**: calculate using Eq. (3.11).

> **Why the flux density reformulation?** While it adds $D_x$ and $I_x$ alongside $E_x$, the payoff comes when we handle frequency-dependent materials (Section 3.3). The auxiliary differential equation approach provides a systematic framework for modeling complex dispersive media.

---

## 3.2 Calculating the Frequency Domain Output

### The Impulse Response Approach

Classical approach: use a sinusoidal source, iterate until steady state, record amplitude and phase. **Repeat for every frequency of interest** — computationally prohibitive.

**Better approach:** Use an **impulse** (approximated by a narrow Gaussian pulse). Iterate until the pulse dies out, then take the Fourier transform of $E(t)$ at every point. This yields the response at **all frequencies simultaneously**.

### The Discrete Fourier Transform (DFT) in FDTD

We want the Fourier transform of $E(t)$ at frequency $f_1$:

$$
E(f_1) = \int_0^{t_T} E(t) e^{-j 2\pi f_1 t}\, dt \tag{3.12}
$$

Lower limit is 0 (causal system assumption). Upper limit $t_T = T \Delta t$ is when FDTD iteration stops.

In finite-difference form:

$$
E(f_1) = \sum_{n=0}^{T} E^n \Delta t \, e^{-j 2\pi f_1 n \Delta t} \tag{3.13}
$$

Dividing into real and imaginary parts:

$$
E(f_1) = \sum_{n=0}^{T} E^n \Delta t \cos(2\pi f_1 \Delta t n) - j \sum_{n=0}^{T} E^n \Delta t \sin(2\pi f_1 \Delta t n) \tag{3.14}
$$

### Implementation: Running Sums

At each time step and each point $k$, accumulate:

$$
\texttt{real\_pt}[m,k] \mathrel{+=} \cos(2\pi f_m \Delta t \cdot \texttt{time\_step}) \cdot E_x[k] \tag{3.15a}
$$

$$
\texttt{imag\_pt}[m,k] \mathrel{-=} \sin(2\pi f_m \Delta t \cdot \texttt{time\_step}) \cdot E_x[k] \tag{3.15b}
$$

> **Computational elegance:** Only two values per frequency per cell — no need to store the entire time-series! The running DFT is accumulated as the simulation proceeds.

### Amplitude and Phase Extraction

From the real and imaginary parts at each frequency $f_m$ and cell $k$:

$$
\text{Amplitude}[m,k] = \sqrt{\texttt{real\_pt}[m,k]^2 + \texttt{imag\_pt}[m,k]^2} \tag{3.16a}
$$

$$
\text{Phase}[m,k] = \text{atan2}(\texttt{imag\_pt}[m,k], \texttt{real\_pt}[m,k]) \tag{3.16b}
$$

### Physical Example: Pulse Striking $\varepsilon_r = 4$ Dielectric

When a pulse hits a dielectric with $\varepsilon_r = 4$, transmission coefficient:

$$
\tau = \frac{2}{1 + \sqrt{\varepsilon_r}} = \frac{2}{1 + 2} = \frac{2}{3} \approx 0.667 \tag{3.17}
$$

The Fourier amplitude inside the medium is **0.667**. Outside the medium, it varies between $1 - 0.333$ and $1 + 0.333$ due to the **standing wave** formed by the interference between incident and reflected waves.

> **Signal processing connection:** The FDTD simulation is fundamentally a discrete linear system. The DFT lets us extract the frequency-domain transfer function — amplitude and phase at every spatial point for every frequency of interest.

---

## 3.3 Frequency-Dependent Media: The Debye Formulation

### The Problem

Most real media have $\varepsilon_r$ and $\sigma$ that **vary with frequency**. A Gaussian pulse contains a spectrum of frequencies — if the medium is frequency-dependent, different spectral components will propagate differently.

### Debye Model for Dispersive Media

A single-pole Debye medium is characterized by:

$$
\varepsilon_r^*(\omega) = \varepsilon_r + \frac{\sigma}{j\omega \varepsilon_0} + \frac{\chi_1}{1 + j\omega \tau} \tag{3.18}
$$

Parameters:
- $\varepsilon_r$: static relative dielectric constant
- $\sigma$: conductivity (S/m)
- $\chi_1$: magnitude of the frequency-dependent susceptibility
- $\tau$: relaxation time (s)

### Example Medium Properties

From the textbook figure (Fig. 3.2):

$$
\varepsilon_r = 2,\quad \sigma = 0.01 \text{ S/m},\quad \chi_1 = 2,\quad \tau = 0.001 \mu\text{s}
$$

At different frequencies:

| Frequency (MHz) | $\varepsilon_r^*$ effective | $\sigma$ effective (S/m) |
|---|---|---|
| 50  | 3.82 | 0.012 |
| 200 | 2.78 | 0.021 |
| 500 | 2.18 | 0.026 |

### From Frequency Domain to Time Domain

Define the Debye term (Eq. 3.18 third term) as:

$$
S(\omega) = \frac{\chi_1}{1 + j\omega\tau} E(\omega) \tag{3.19}
$$

The inverse Fourier transform of $\frac{\chi_1}{1 + j\omega\tau}$ is $\frac{\chi_1}{\tau} e^{-t/\tau} u(t)$, where $u(t)$ is the unit step (causality implicit).

In the time domain, this becomes a **convolution**:

$$
S(t) = \frac{\chi_1}{\tau} \int_0^t e^{-(t-t')/\tau} E(t')\, dt' \tag{3.20}
$$

In the sampled time domain (summation):

$$
S^n = \frac{\chi_1 \Delta t}{\tau} \left( E^n + \sum_{i=0}^{n-1} e^{-\Delta t(n-i)/\tau} E^i \right) \tag{3.21}
$$

Let $S^{n-1} = \frac{\chi_1 \Delta t}{\tau} \sum_{i=0}^{n-1} e^{-\Delta t(n-1-i)/\tau} E^i$, which implies:

$$
\sum_{i=0}^{n-1} e^{-\Delta t(n-i)/\tau} E^i = e^{\Delta t/\tau} S^{n-1}
$$

Substituting:

$$
S^n = e^{-\Delta t/\tau} S^{n-1} + \frac{\chi_1 \Delta t}{\tau} E^n \tag{3.22}
$$

### Complete Update Equations for Debye Medium

Combining the loss term (Section 3.1) and the Debye polarization term:

$$
D^n = \varepsilon_r E^n + \underbrace{\frac{\sigma \Delta t}{\varepsilon_0} E^n + I^{n-1}}_{\text{conductive loss}} + \underbrace{e^{-\Delta t/\tau} S^{n-1} + \frac{\chi_1 \Delta t}{\tau} E^n}_{\text{Debye polarization}} \tag{3.23}
$$

Solving for $E^n$:

$$
E^n = \frac{D^n - I^{n-1} - e^{-\Delta t/\tau} S^{n-1}}{\varepsilon_r + \frac{\sigma \Delta t}{\varepsilon_0} + \frac{\chi_1 \Delta t}{\tau}} \tag{3.24a}
$$

Auxiliary equations:

$$
I^n = I^{n-1} + \frac{\sigma \Delta t}{\varepsilon_0} E^n \tag{3.24b}
$$

$$
S^n = e^{-\Delta t/\tau} S^{n-1} + \frac{\chi_1 \Delta t}{\tau} E^n \tag{3.24c}
$$

### FDTD Code Implementation (1D Debye Medium)

```python
dx[k] = dx[k] + 0.5 * (hy[k-1] - hy[k])          # (3.25a) D-field update
ex[k] = gax[k] * dx[k] - ix[k] - del_exp * sx[k]  # (3.25b) E-field update
ix[k] = ix[k] + gbx[k] * ex[k]                    # (3.25c) I update (conductive)
sx[k] = del_exp * sx[k] + gcx[k] * ex[k]           # (3.25d) S update (Debye)
hy[k] = hy[k] + 0.5 * (ex[k] - ex[k+1])            # (3.25e) H-field update
```

where:

```python
# Media coefficients
gax[k] = 1.0 / (epsr + sigma*dt/epsz + chi*dt/tau)    # (3.26a)
gbx[k] = sigma * dt / epsz                             # (3.26b)
gcx[k] = chi * dt / tau                                # (3.26c)
del_exp = exp(-dt / tau)                              # exponential decay
```

> **Physical intuition:** Higher conductivity $\sigma$ → more conductive loss (dissipated as heat). Higher susceptibility $\chi_1$ → stronger Debye polarization response. Smaller $\tau$ → faster polarization relaxation (response moves to higher frequencies).

### Effective Medium Properties at Different Frequencies

The key physical result: at 500 MHz the effective $\varepsilon_r$ drops to 2.18 and $\sigma$ rises to 0.026 S/m → waves attenuate more rapidly than at 50 MHz. This is why a Debye medium is called **dispersive** — different frequency components see different material properties and propagate at different speeds.

---

## 3.3.1 Auxiliary Differential Equation (ADE) Method

An alternative to the convolution approach is the **Auxiliary Differential Equation (ADE)** method.

Starting from Eq. (3.19):

$$
(1 + j\omega\tau) S(\omega) = \chi_1 E(\omega) \tag{3.27}
$$

Going to the continuous time domain:

$$
S(t) + \tau \frac{dS(t)}{dt} = \chi_1 E(t) \tag{3.28}
$$

In the discrete time domain, this becomes a simple algebraic update for $S^n$ that directly couples the time derivative, avoiding the full convolution sum. The ADE approach is often more intuitive for multi-pole Debye or Lorentz models but requires additional auxiliary variables for each pole.

---

## Code Reference

### Figure 3.1 Simulation Code (`fd3d_1_1.py` — 1D FDTD Free Space)

```python
import numpy as np
from math import exp
from matplotlib import pyplot as plt

ke = 200
ex = np.zeros(ke)
hy = np.zeros(ke)

# Gaussian pulse parameters
kc = int(ke / 2)   # center cell
t0 = 40            # peak time
spread = 12        # pulse width

nsteps = 100

for time_step in range(1, nsteps + 1):
    # Calculate Ex field
    for k in range(1, ke):
        ex[k] = ex[k] + 0.5 * (hy[k-1] - hy[k])

    # Inject Gaussian pulse at center
    pulse = exp(-0.5 * ((t0 - time_step) / spread) ** 2)
    ex[kc] = pulse

    # Calculate Hy field
    for k in range(ke - 1):
        hy[k] = hy[k] + 0.5 * (ex[k] - ex[k+1])

    # Plot at each time step
    plt.rcParams['font.size'] = 12
    plt.figure(figsize=(8, 3.5))
    plt.subplot(211)
    plt.plot(ex, color='k', linewidth=1)
    plt.ylabel('E$_x$', fontsize='14')
    plt.xticks(np.arange(0, 201, step=20))
    plt.xlim(0, 200)
    plt.yticks(np.arange(-1, 1.2, step=1))
    plt.ylim(-1.2, 1.2)
    plt.text(100, 0.5, 'T = {}'.format(time_step), ha='center')
    plt.subplot(212)
    plt.plot(hy, color='k', linewidth=1)
    plt.ylabel('H$_y$', fontsize='14')
    plt.xlabel('FDTD cells')
    plt.xticks(np.arange(0, 201, step=20))
    plt.xlim(0, 200)
    plt.yticks(np.arange(-1, 1.2, step=1))
    plt.ylim(-1.2, 1.2)
    plt.subplots_adjust(bottom=0.2, hspace=0.45)
    plt.show()
```

> **Physics:** Yee grid in 1D — E and H fields are staggered by half a cell. The update coefficients 0.5 = $\Delta t / \Delta z$ for free space with $c_0 = 1$.

---

### Absorbing Boundary Condition Code (`fd3d_1_2.py`)

```python
# ABC: first-order Mur boundary
ex[0] = boundary_low.pop(0)
boundary_low.append(ex[1])
ex[ke-1] = boundary_high.pop(0)
boundary_high.append(ex[ke-2])
```

> **Physical intuition:** The ABC treats the boundary as if waves continue into open space. The first-order Mur condition approximates the one-way wave equation at the edge.

---

### Lossy Dielectric Code (`fd3d_1_5.py`)

```python
epsz = 8.854e-12
epsilon = 4
sigma = 0.04

ca = np.ones(ke)
cb = np.ones(ke) * 0.5

cb_start = 100
eaf = dt * sigma / (2 * epsz * epsilon)
ca[cb_start:] = (1 - eaf) / (1 + eaf)
cb[cb_start:] = 0.5 / (epsilon * (1 + eaf))

# In the main loop:
ex[k] = ca[k] * ex[k] + cb[k] * (hy[k-1] - hy[k])
```

---

## Key Equations Summary

| Equation | Name | Physical Meaning |
|---|---|---|
| (3.1b) | D-E constitutive relation | Links flux density to E-field via complex permittivity |
| (3.8a-b) | Flux density reformulation | Enables auxiliary current $I^n$ to track conductive loss history |
| (3.10a-d) | 1D FDTD with flux density | Unified update with media in E-step only |
| (3.11a-b) | Media coefficients gax/gbx | Encodes $\varepsilon_r$ and $\sigma$ |
| (3.15a-b) | Running DFT | Accumulates frequency-domain response without storing time-series |
| (3.18) | Debye model | Single-pole dispersive permittivity |
| (3.24a-c) | Debye update equations | Three auxiliary variables: $E$, $I$ (loss), $S$ (polarization) |