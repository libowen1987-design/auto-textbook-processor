# Chapter 2 — More on One-Dimensional Simulation

> **Source:** Houle & Sullivan, *Electromagnetic Simulation Using the FDTD Method with Python*, 3rd ed. (IEEE Press, 2020), Ch. 2  
> **Raw:** `/tmp/houle_ch3_raw.txt` (lines 381–941) + `/tmp/houle_ch4_raw.txt` (lines 1–732, 162–731)  
> **Status:** ✅ Complete

---

## 2.1 Reformulation Using the Flux Density

### Why Change the Formulation?

The direct $E$, $H$ formulation (Ch1) requires changing update coefficients for every material type. The flux density $\mathbf{D}$ formulation separates the **universal** Maxwell curl equations from the **material-specific** constitutive relation:

$$
\frac{\partial \mathbf{D}}{\partial t} = \nabla \times \mathbf{H} \tag{2.1a}
$$
$$
\mathbf{D}(\omega) = \varepsilon_0 \varepsilon_r^*(\omega) \, \mathbf{E}(\omega) \tag{2.1b}
$$
$$
\frac{\partial \mathbf{H}}{\partial t} = -\frac{1}{\mu_0} \nabla \times \mathbf{E} \tag{2.1c}
$$

**Advantage:** Eqs. (2.1a) and (2.1c) stay **exactly the same** for all media — all complexity is confined to Eq. (2.1b), which becomes a **digital filtering problem**.

### Flux Density in 1D

$$
D_x^{n+1}[k] = D_x^n[k] + \Delta t \left(H_y^n[k+\tfrac{1}{2}] - H_y^n[k-\tfrac{1}{2}]\right) \quad \text{(from Eq. 2.1a)}
$$

Then apply the material filter (2.1b) to get $E_x$ from $D_x$.

### 1D Discretized Updates

```python
# D-field update (universal, same for all materials)
for k in range(1, ke):
    dx[k] = dx[k] + (hy[k-1] - hy[k])   # dt=0.5 in normalized units

# E-field from D via material-specific filter
ex[k] = dx[k] / epsilon_r   # for simple non-dispersive dielectric

# H-field update (universal)
for k in range(ke - 1):
    hy[k] = hy[k] + 0.5 * (ex[k] - ex[k+1])
```

### Material Response as a Filter

The key insight: solving $\mathbf{D} = \varepsilon_0 \varepsilon_r^* \mathbf{E}$ for various media maps directly to well-known **digital filter** structures (IIR, FIR). This connects FDTD to signal processing theory.

---

## 2.2 Calculating the Frequency Domain Output

### Why Frequency Domain?

Time-domain FDTD gives $E(t)$, $H(t)$. Often we need $E(\omega)$ — e.g., to compare with measurements or analyze frequency-selective behavior. The **Discrete Fourier Transform (DFT)** provides this.

### DFT Implementation in FDTD

For a point $k_0$ where we want the frequency spectrum:

$$
E(\omega) = \sum_{n=0}^{N-1} E^n[k_0] \; e^{-j\omega n \Delta t}
$$

Implementation: accumulate field samples during the FDTD loop:

```python
# During FDTD loop:
ex_stored[time_step] = ex[k0]

# After simulation:
E_omega = np.fft.fftfreq(nsteps, d=dt)[:nsteps//2]
E_spectrum = np.fft.fft(ex_stored)[:nsteps//2]
```

### Key Properties

- The DFT naturally gives the **complex spectrum** (magnitude + phase)
- Resolution: $\Delta f = 1/(N \Delta t)$
- Windowing the time signal affects the spectrum (Sinc artifacts from rectangular window)
- DFT at DC ($f=0$): equivalent to time-average of the field

### Fourier Amplitude in the Medium

When a pulse enters a dispersive medium, different frequency components:
1. Have different transmission coefficients (different $\varepsilon_r^*$)
2. Attenuate at different rates (different $\sigma$)
3. Travel at different phase velocities

This explains the spreading and frequency-dependent loss observed in dispersive media simulations.

---

## 2.3 Frequency-Dependent Media

### The Debye Relaxation Model

For many biological tissues and non-magnetic materials, the relative permittivity follows a **Debye relaxation**:

$$
\varepsilon_r^*(\omega) = \varepsilon_\infty + \frac{\chi_1}{1 + j\omega\tau}
$$

| Parameter | Physical Meaning |
|---|---|
| $\varepsilon_\infty$ | High-frequency permittivity (optical/electronic) |
| $\chi_1$ | Static susceptibility (low-frequency contribution) |
| $\tau$ | Relaxation time (molecular reorientation time) |

### Time-Domain Equivalent

Inverse Fourier transform of Debye equation:

$$
\varepsilon_r(t) = \varepsilon_\infty + \chi_1 \cdot e^{-t/\tau} \cdot u(t)
$$

The $e^{-t/\tau}$ term represents the **exponential decay** of polarization response.

### FDTD Update for Debye Medium

Using the flux density approach, the Debye update is:

```python
# Time-domain Debye update
for k in range(1, ke):
    dx[k] = dx[k] + (hy[k-1] - hy[k])          # D-update
    
    # Apply Debye filter to get E from D
    ex[k] = (dx[k] - chi1 * Pol[k]) / eps_inf
    Pol[k] = Pol[k] * np.exp(-dt/tau) + (dx[k] - dx_prev[k]) * chi1 / tau
    dx_prev[k] = dx[k]
```

### Effective Frequency-Dependent Properties

At a given frequency $\omega$:

$$
\varepsilon_r'(\omega) = \varepsilon_\infty + \frac{\chi_1}{1 + \omega^2\tau^2}
$$
$$
\sigma_{\text{eff}}(\omega) = \omega \varepsilon_0 \frac{\chi_1 \omega\tau}{1 + \omega^2\tau^2}
$$

**Important:** Both $\varepsilon_r'$ and $\sigma_{\text{eff}}$ are **frequency-dependent** — the wave sees different properties at different frequencies. This is the fundamental origin of **dispersion**.

### Example: Human Muscle Tissue (Debye Parameters)

Typical Debye parameters for muscle at body temperature ($\approx 37^\circ$C):

| Parameter | Value |
|---|---|
| $\varepsilon_\infty$ | 4.0 |
| $\chi_1$ | 43.0 |
| $\tau$ | 7.96 ps |

This produces $\varepsilon_r \approx 47$ at low frequencies (DC) down to $\approx 4$ at optical frequencies.

---

## 2.3.1 Auxiliary Differential Equation (ADE) Method

### Alternative to Z-Domain Approach

ADE provides an equivalent method for frequency-dependent media by working directly in the time domain with **auxiliary differential equations**.

### ADE for Debye Medium

Starting from:
$$
\mathbf{D}(\omega) = \varepsilon_0 \varepsilon_r^*(\omega) \mathbf{E}(\omega)
$$
with $\varepsilon_r^* = \varepsilon_\infty + \chi_1/(1+j\omega\tau)$, we get:

$$
\mathbf{D} = \varepsilon_0 \varepsilon_\infty \mathbf{E} + \varepsilon_0 \chi_1 \mathcal{F}^{-1}\left[\frac{\mathbf{E}}{1+j\omega\tau}\right]
$$

Define an auxiliary polarization $\mathbf{P}$ satisfying:
$$
\frac{d\mathbf{P}}{dt} = \frac{1}{\tau}\left(\varepsilon_0 \chi_1 \mathbf{E} - \mathbf{P}\right)
$$

Then: $\mathbf{D} = \varepsilon_0 \varepsilon_\infty \mathbf{E} + \mathbf{P}$

### ADE FDTD Update

```python
# ADE update for Debye medium
for k in range(1, ke):
    # D-update (universal)
    dx[k] = dx[k] + (hy[k-1] - hy[k])
    
    # P-update (auxiliary equation)
    P_new = P[k] + dt/tau * (chi1 * eps0 * ex[k] - P[k])
    
    # E from D and P
    ex[k] = (dx[k] - P_new) / (eps0 * eps_inf)
    
    P[k] = P_new
```

### Comparison: ADE vs. Z-Domain (Recursive Convolution)

| Aspect | ADE | Z-Domain / RC |
|---|---|---|
| Formulation | Time-domain ODEs | Z-domain difference equations |
| Implementation | Direct time-stepping | Convolution or recursive filter |
| Stability | Equivalent | Equivalent |
| Complexity | Similar | Similar |
| Numerical precision | Good | Good |

Both methods yield identical results for the Debye medium.

---

## 2.4 Formulation Using Z Transforms

### Z-Domain Representation

The constitutive relation $D(\omega) = \varepsilon_0 \varepsilon_r^*(\omega) E(\omega)$ becomes in discrete time:

$$
D(z) = \varepsilon_0 \varepsilon_r^*(z) \, E(z)
$$

For Debye: $\varepsilon_r^*(z) = \varepsilon_\infty + \chi_1 \cdot \frac{z^{-1}}{1 - e^{-\Delta t/\tau}z^{-1}}$

### Z-Domain FDTD Update

Rearranging into a **causal difference equation**:

$$
E(z) = \frac{1}{\varepsilon_0 \varepsilon_\infty} \left[ D(z) - \frac{\chi_1 z^{-1}}{1 - e^{-\Delta t/\tau}z^{-1}} E(z) \right]
$$

This gives a **recursive filter** for $E$:

```python
# Z-domain (recursive convolution) Debye update
for k in range(1, ke):
    dx[k] = dx[k] + (hy[k-1] - hy[k])       # D-update
    
    # Recursive filter to get E from D
    ex[k] = (dx[k] + chi1 * ex_old[k]) / (eps_inf + chi1 * np.exp(-dt/tau))
    ex_old[k] = ex[k] * np.exp(-dt/tau)      # z^{-1} delay
```

### Signal Processing Connection

The Z-transform formulation makes explicit that FDTD simulation of dispersive media is exactly equivalent to **digital filtering** of the input signal. Key signal processing concepts that apply:
- **Transfer function** $H(z) = E(z)/D(z)$
- **Poles and zeros** of the medium response
- **BIBO stability** requires all poles inside the unit circle
- **Filter coefficients** map directly to physical medium parameters

---

## 2.4.1 Simulation of Unmagnetized Plasma

### Plasma as a Drude Medium

A cold, unmagnetized plasma has the Drude dispersion model:

$$
\varepsilon_r^*(\omega) = 1 - \frac{\omega_p^2}{\omega^2 + j\omega \nu}
$$

| Parameter | Physical Meaning |
|---|---|
| $\omega_p = \sqrt{n_e e^2 / (m_e \varepsilon_0)}$ | Plasma frequency |
| $\nu$ | Collision frequency (energy loss rate) |

### Z-Domain Formulation for Plasma

Using the auxiliary differential equation method for the plasma:

```python
# Plasma update (Drude model)
# D = eps0 * E + P  where dP/dt = eps0 * wp^2 * E - nu * P
for k in range(1, ke):
    dx[k] = dx[k] + (hy[k-1] - hy[k])
    
    # P-update (Drude auxiliary equation)
    P[k] = P[k] * np.exp(-nu * dt) + eps0 * wp**2 * dt * ex[k]
    
    # E from D
    ex[k] = (dx[k] - P[k]) / eps0
```

### Physical Phenomena

- **Low frequency** ($\omega \ll \omega_p$): $\varepsilon_r^* < 0$ → **evanescent** (wave cannot propagate, total reflection)
- **Above plasma frequency** ($\omega > \omega_p$): wave propagates with wavenumber $k = \omega/c \sqrt{1 - \omega_p^2/\omega^2}$
- Plasma acts as a **high-pass filter** — only frequencies above $\omega_p$ can propagate

### Example: Ionosphere

The Earth's ionosphere is a plasma with $\omega_p \approx 10$–$100$ MHz (depending on electron density). This is why AM radio (below ~10 MHz) undergoes total internal reflection at the ionosphere and can propagate beyond line-of-sight, while FM radio (~100 MHz) passes through.

---

## 2.5 Formulating a Lorentz Medium

### Lorentz Model (Multi-Resonance)

The Lorentz model adds **resonant behavior** to the Debye model, allowing multiple resonances:

$$
\varepsilon_r^*(\omega) = \varepsilon_\infty + \sum_m \frac{\omega_{p,m}^2}{\omega_{0,m}^2 - \omega^2 - j\omega \nu_m}
$$

Each term ($m$) represents a **resonance** at $\omega_{0,m}$.

### Single-Resonance Lorentz FDTD

For a single resonance ($\omega_0$, $\omega_p$, $\nu$):

```python
# Lorentz single-resonance update
for k in range(1, ke):
    dx[k] = dx[k] + (hy[k-1] - hy[k])      # D-update
    
    # Lorentz auxiliary: dP/dt = wp^2 * E - 2*alpha*dP/dt - omega0^2 * P
    # where alpha = nu/2
    P_new = P[k] + dt * (wp**2 * ex[k] - 2*alpha*P[k] - omega0**2 * P_dot)
    P_dot_new = P_new - P[k]
    
    ex[k] = (dx[k] - P_new) / eps0
    P_dot = P_dot_new / dt
    P[k] = P_new
```

### Key Distinction from Debye

| Feature | Debye | Lorentz |
|---|---|---|
| Resonance | No (monotonic decay) | Yes (oscillatory response) |
| Poles | Single real pole | Complex conjugate poles |
| Applications | Water, biological tissue | Solids, crystals, resonant media |
| Phase response | Causal, monotonic | Can have resonant phase shifts |

### Lorentz Media in FDTD: Why It's Critical

Lorentz materials exhibit:
- **Anomalous dispersion** near resonance (group velocity > c or < 0)
- **Resonant absorption** peaks
- **Backward waves** possible in certain frequency ranges (gain media)

These effects require careful numerical treatment to maintain stability and causality.

---

## 2.5.1 Simulation of Human Muscle Tissue (Lorentz Model)

### Muscle Tissue as a Multi-Resonance Medium

Real biological tissues like muscle have **multiple relaxation mechanisms**:
1. **Debye relaxations** (water content, ionic solutions)
2. **Lorentz resonances** (protein-bound water, cell membranes)

A complete model uses 4–6 Lorentz terms plus a Debye term.

### Multi-Resonance Lorentz FDTD

```python
# Multi-resonance Lorentz for muscle tissue
N_RESONANCES = 4

# State variables per resonance
P = np.zeros((N_RESONANCES, ke))      # Polarization
P_dot = np.zeros((N_RESONANCES, ke))  # Polarization derivative

for time_step in range(1, nsteps + 1):
    # D-update
    for k in range(1, ke):
        dx[k] = dx[k] + (hy[k-1] - hy[k])
    
    # E from D with multi-resonance Lorentz
    for m in range(N_RESONANCES):
        P_new = P[m] + dt * P_dot[m]
        P_dot_new = P_dot[m] + dt * (wp2[m] * ex - 2*alpha[m] * P_dot[m] - w0_sq[m] * P[m])
        P[m] = P_new
        P_dot[m] = P_dot_new
    
    ex[:] = (dx[:] - sum(P)) / eps0
    
    # H-update
    for k in range(ke - 1):
        hy[k] = hy[k] + 0.5 * (ex[k] - ex[k+1])
```

### Physical Validation

For hyperthermia treatment planning (Ch6), accurate muscle tissue modeling is critical:
- **SAR (Specific Absorption Rate)** = $\sigma |E|^2 / (2\rho)$ determines heating
- At 433 MHz (hyperthermia frequency), muscle has $\varepsilon_r \approx 50-60$, $\sigma \approx 0.8-1.5$ S/m
- Errors in permittivity model → errors in SAR prediction → errors in treatment dose

### Frequency-Dependent Absorption

At the hyperthermia frequency of 433 MHz:
- $\varepsilon_r \approx 55$ (high, dominated by water content)
- $\sigma \approx 1.2$ S/m
- Penetration depth $\delta \approx 2$–$3$ cm in muscle

This shallow penetration is why hyperthermia is used as an **adjunct** to radiation therapy — heat penetrates to depth when combined with radiation.

---

## Key Equations Master Index (Chapter 2)

| Eq. | Description |
|---|---|
| (2.1a–c) | Flux density Maxwell's equations |
| (2.1b) | Constitutive relation: $D = \varepsilon_0 \varepsilon_r^* E$ |
| — | Debye model: $\varepsilon_r^*(\omega) = \varepsilon_\infty + \chi_1/(1+j\omega\tau)$ |
| — | Drude model: $\varepsilon_r^*(\omega) = 1 - \omega_p^2/(\omega^2 + j\omega\nu)$ |
| — | Lorentz model: $\varepsilon_r^* = \varepsilon_\infty + \sum \omega_{p,m}^2/(\omega_{0,m}^2 - \omega^2 - j\omega\nu_m)$ |
| — | Effective permittivity: $\varepsilon_r'(\omega) = \varepsilon_\infty + \chi_1/(1+\omega^2\tau^2)$ |
| — | Effective conductivity: $\sigma_{\text{eff}}(\omega) = \omega\varepsilon_0 \chi_1\omega\tau/(1+\omega^2\tau^2)$ |
| — | Plasma frequency: $\omega_p = \sqrt{n_e e^2/(m_e\varepsilon_0)}$ |
| — | Penetration depth: $\delta = \sqrt{2/(\omega\mu\sigma)}$ |

---

## References (Chapter 2)

6. Cheng, D. K. (1992), *Field and Wave Electromagnetics*, Addison-Wesley.  
7. Yee (1966) — foundational FDTD (already listed Ch1)  
8. Sullivan (2013) — IEEE Fellow material on FDTD and EM dosimetry  
9. Kunz & Luebbers (1993) — standard FDTD textbook  
10. Taflove (1995) — comprehensive FDTD reference  
(Additional references in book: plasma physics, signal processing Z-transform texts)