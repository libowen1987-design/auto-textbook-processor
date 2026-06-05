# Jackson Ch14: Radiation by Moving Charges

## Overview
Electromagnetic radiation from arbitrarily moving charged particles. Lienard-Wiechert potentials, fields, and radiated power.

---

## §14.1 – The Lienard-Wiechert Potentials

### Retarded Potentials for a Point Charge

For a point charge $q$ moving along $\mathbf{r}_0(t)$ with velocity $\mathbf{v}(t) = \dot{\mathbf{r}}_0(t)$:

**Lienard-Wiechert potentials** (the fundamental solution):

$$
\Phi(\mathbf{r}, t) = \frac{q}{4\pi\epsilon_0} \left[ \frac{1}{(1 - \boldsymbol{\beta} \cdot \mathbf{n}) R} \right]_{\text{ret}}
$$

$$
\mathbf{A}(\mathbf{r}, t) = \frac{\mu_0 q}{4\pi} \left[ \frac{\mathbf{v}}{(1 - \boldsymbol{\beta} \cdot \mathbf{n}) R} \right]_{\text{ret}}
$$

where:
- $\mathbf{R} = \mathbf{r} - \mathbf{r}_0(t_{\text{ret}})$, $R = |\mathbf{R}|$
- $\mathbf{n} = \mathbf{R}/R$
- $\boldsymbol{\beta} = \mathbf{v}/c$
- $[\ldots]_{\text{ret}}$ = evaluated at retarded time $t_{\text{ret}} = t - R(t_{\text{ret}})/c$

### Four-vector Form
$$
A^\alpha(x) = \frac{q}{4\pi\epsilon_0 c} \frac{U^\alpha}{U \cdot (x - x_0(\tau))}
$$
where $U^\alpha = (\gamma c, \gamma \mathbf{v})$ is the 4-velocity.

---

## §14.2 – Electric and Magnetic Fields of a Moving Point Charge

### Heaviside-Feynman Fields (Jefimenko form)

$$
\mathbf{E}(\mathbf{r}, t) = \frac{q}{4\pi\epsilon_0} \left[ \frac{\mathbf{n} - \boldsymbol{\beta}}{\gamma^2 (1 - \boldsymbol{\beta} \cdot \mathbf{n})^3 R^2} \right]_{\text{ret}} + \frac{q}{4\pi\epsilon_0 c} \left[ \frac{\mathbf{n} \times [(\mathbf{n} - \boldsymbol{\beta}) \times \dot{\boldsymbol{\beta}}]}{(1 - \boldsymbol{\beta} \cdot \mathbf{n})^3 R} \right]_{\text{ret}}
$$

$$
\mathbf{B}(\mathbf{r}, t) = \frac{1}{c} [\mathbf{n} \times \mathbf{E}]_{\text{ret}}
$$

### Two Terms (Physically)

1. **Velocity field** ($\propto 1/R^2$): self-field of a uniformly moving charge; no radiation
2. **Acceleration field** ($\propto 1/R$): radiation field; depends on $\dot{\boldsymbol{\beta}}$

### Key Fact: 
The radiation field is transverse to $\mathbf{n}$ and $\propto 1/R$ → energy flux to infinity.

---

## §14.3 – Radiated Power from an Accelerated Charge

### Larmor's Formula (non-relativistic)

$$
P = \frac{q^2 a^2}{6\pi \epsilon_0 c^3} = \frac{q^2}{6\pi\epsilon_0 c} \dot{\beta}^2
$$

### Relativistic Generalization (Liénard)

$$
P = \frac{q^2}{6\pi\epsilon_0 c} \gamma^6 \left[ (\dot{\boldsymbol{\beta}})^2 - (\boldsymbol{\beta} \times \dot{\boldsymbol{\beta}})^2 \right]
$$

Or equivalently:
$$
P = \frac{q^2}{6\pi\epsilon_0 c} \left[ \gamma^4 \dot{\beta}_\parallel^2 + \gamma^2 \dot{\beta}_\perp^2 \right]
$$

where $\dot{\boldsymbol{\beta}}_\parallel$ is parallel to $\boldsymbol{\beta}$, $\dot{\boldsymbol{\beta}}_\perp$ is perpendicular.

### Angular Distribution

$$
\frac{dP}{d\Omega} = \frac{q^2}{16\pi^2\epsilon_0 c} \frac{|\mathbf{n} \times [(\mathbf{n} - \boldsymbol{\beta}) \times \dot{\boldsymbol{\beta}}]|^2}{(1 - \boldsymbol{\beta} \cdot \mathbf{n})^5}
$$

---

## §14.4 – Relativistic Four-Vector Formulation

### Larmor's Formula in Covariant Form

Four-momentum radiated per unit proper time:
$$
\frac{dP}{d\tau} = \frac{q^2}{6\pi\epsilon_0 c^3} \frac{dU_\alpha}{d\tau} \frac{dU^\alpha}{d\tau}
$$

### Invariant:
$$
\frac{dU_\alpha}{d\tau} \frac{dU^\alpha}{d\tau} = c^2 \gamma^4 [\dot{\beta}^2 - (\boldsymbol{\beta} \times \dot{\boldsymbol{\beta}})^2]
$$

---

## §14.5 – Synchrotron Radiation

### Circular Motion with $\beta \perp \dot{\beta}$, $\beta \approx 1$

**Total power**: 
$$
P = \frac{q^2}{6\pi\epsilon_0 c} \gamma^4 \dot{\beta}_\perp^2 = \frac{q^2}{6\pi\epsilon_0 c} \gamma^4 \frac{v^4}{c^2 \rho^2}
$$

For a circular accelerator ($\rho$ = radius):
$$
P = \frac{q^2 c}{6\pi\epsilon_0} \frac{\beta^4 \gamma^4}{\rho^2} \approx \frac{e^2 c}{6\pi\epsilon_0} \frac{\gamma^4}{\rho^2} \quad (\beta \approx 1)
$$

### Angular and Spectral Distribution

Beaming: radiation concentrated in a narrow cone of half-angle $\theta_c \sim 1/\gamma$

Angular distribution:
$$
\frac{dP}{d\Omega} \approx \frac{2q^2 \gamma^6 \dot{\beta}_\perp^2}{\pi\epsilon_0 c} \frac{1 + (\gamma\psi)^2 - (\gamma\psi)^4}{[1 + (\gamma\psi)^2]^5}
$$

where $\psi$ is the angle from the instantaneous velocity direction.

### Critical Frequency
$$
\omega_c = \frac{3}{2} \frac{c \gamma^3}{\rho}
$$
Above $\omega_c$ the spectrum falls off exponentially.

---

## §14.6 – Radiation from a Charged Particle with Collinear Velocity and Acceleration

### Linear Accelerator (linear motion with $\boldsymbol{\beta} \parallel \dot{\boldsymbol{\beta}}$)

**Total power**:
$$
P = \frac{q^2}{6\pi\epsilon_0 c} \gamma^6 \dot{\beta}^2
$$

**Angular distribution**:
$$
\frac{dP}{d\Omega} = \frac{q^2 \dot{\beta}^2}{16\pi^2\epsilon_0 c} \frac{\sin^2\theta}{(1 - \beta\cos\theta)^5}
$$

where $\theta$ is the angle from the acceleration direction.

**Beaming**: radiation peaks in the forward direction at $\theta_{\text{max}} \approx 1/(2\gamma)$ for $\gamma \gg 1$

---

## §14.7–14.8 – Frequency Spectrum of Radiation

### Fourier Transform of Radiated Fields

Energy radiated per unit solid angle per unit frequency:
$$
\frac{d^2 I}{d\Omega d\omega} = \frac{q^2}{16\pi^3\epsilon_0 c} \left| \int_{-\infty}^{\infty} \frac{\mathbf{n} \times [(\mathbf{n} - \boldsymbol{\beta}) \times \dot{\boldsymbol{\beta}}]}{(1 - \boldsymbol{\beta} \cdot \mathbf{n})^2} e^{i\omega(t_{\text{ret}})} dt_{\text{ret}} \right|^2
$$

### Alternative form (using integration by parts):
$$
\frac{d^2 I}{d\Omega d\omega} = \frac{q^2 \omega^2}{16\pi^3\epsilon_0 c} \left| \int_{-\infty}^{\infty} \mathbf{n} \times [\mathbf{n} \times \boldsymbol{\beta}] e^{i\omega(t_{\text{ret}})} dt_{\text{ret}} \right|^2
$$

---

## §14.9 – Thomson Scattering

### Scattering from a Free Electron

Differential cross section:
$$
\frac{d\sigma}{d\Omega} = r_e^2 \sin^2\Theta
$$

where $\Theta$ is the angle between scattered polarization and observation direction.

**Total Thomson cross section**:
$$
\sigma_T = \frac{8\pi}{3} r_e^2 \approx 6.65 \times 10^{-29} \,\text{m}^2
$$

---

## §14.10 – Scattering from Bound Electrons (Rayleigh Scattering)

### Low frequency ($\omega \ll \omega_0$):
$$
\sigma \propto \left( \frac{\omega}{\omega_0} \right)^4 r_e^2
$$

Rayleigh's $1/\lambda^4$ law → sky is blue.

---

## §14.11–14.12 – Coherent and Incoherent Scattering

### Coherent Scattering
- Phases add constructively → $d\sigma/d\Omega \propto N^2$ (for $N$ scatterers)
- Requires $\lambda \gg$ spacing → X-rays from crystals, scattering from molecules

### Incoherent Scattering
- Random phases → $d\sigma/d\Omega \propto N$
- Compton scattering, Thomson from free electrons without interference

---

## §14.13 – Transition Radiation

Emitted when a charged particle crosses a boundary between two dielectrics.

### Characteristics
- Forward lobe: $\theta \sim 1/\gamma$
- Broad spectrum: from visible to X-ray
- Intensity $\propto \gamma^2 \ln(1/\omega_p)$ for $\gamma \gg 1$

### Applications
- Particle identification in transition radiation detectors (TRD)
- $\gamma \gtrsim 1000$ detectable

---

## §14.14 – Cherenkov Radiation (revisited with formalism)

### Frank-Tamm Formula

Energy radiated per unit length per unit frequency:
$$
\frac{d^2 E}{dx d\omega} = \frac{q^2}{4\pi\epsilon_0 c^2} \omega \left( 1 - \frac{1}{\beta^2 n^2(\omega)} \right) \quad \text{for } \beta n > 1
$$

### Spectral Dependence
- Number of photons: $dN/dx \propto \sin^2\theta_c = 1 - 1/(\beta^2 n^2)$
- Visible range: ~300 photons/cm for $\beta \approx 1$ in water

---

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Lienard-Wiechert scalar potential | $\Phi = \frac{q}{4\pi\epsilon_0} \left[ \frac{1}{(1-\boldsymbol{\beta}\cdot\mathbf{n})R} \right]_{\text{ret}}$ |
| Lienard-Wiechert vector potential | $\mathbf{A} = \frac{\mu_0 q}{4\pi} \left[ \frac{\mathbf{v}}{(1-\boldsymbol{\beta}\cdot\mathbf{n})R} \right]_{\text{ret}}$ |
| Velocity field | $\mathbf{E}_v = \frac{q}{4\pi\epsilon_0} \frac{\mathbf{n} - \boldsymbol{\beta}}{\gamma^2(1-\boldsymbol{\beta}\cdot\mathbf{n})^3 R^2}$ |
| Acceleration (radiation) field | $\mathbf{E}_a = \frac{q}{4\pi\epsilon_0 c} \frac{\mathbf{n} \times [(\mathbf{n} - \boldsymbol{\beta}) \times \dot{\boldsymbol{\beta}}]}{(1-\boldsymbol{\beta}\cdot\mathbf{n})^3 R}$ |
| Larmor formula | $P = \frac{q^2 a^2}{6\pi\epsilon_0 c^3}$ |
| Relativistic power | $P = \frac{q^2}{6\pi\epsilon_0 c} \gamma^6 [\dot{\beta}^2 - (\boldsymbol{\beta} \times \dot{\boldsymbol{\beta}})^2]$ |
| Covariant power | $\frac{dP}{d\tau} = \frac{q^2}{6\pi\epsilon_0 c^3} \frac{dU_\alpha}{d\tau}\frac{dU^\alpha}{d\tau}$ |
| Synchrotron power | $P = \frac{q^2 c}{6\pi\epsilon_0} \frac{\beta^4\gamma^4}{\rho^2}$ |
| Critical frequency | $\omega_c = \frac{3}{2}\frac{c\gamma^3}{\rho}$ |
| Thomson cross section | $\sigma_T = \frac{8\pi}{3} r_e^2$ |
