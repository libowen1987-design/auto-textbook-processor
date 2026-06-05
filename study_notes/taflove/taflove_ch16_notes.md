---
chapter: 16
title: "Photonic Crystals and Optical Devices"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, S. C. Hagness, B. J. Ward"
raw_size: 290,881 bytes
---

# Chapter 16: Photonic Crystals and Optical Devices

## 16.1 Introduction

FDTD is the leading numerical method for nanophotonic device modeling. Key applications: photonic crystals (PhC), microcavities, plasmonic structures, waveguide couplers, and nonlinear optical devices.

**Optical FDTD challenges**: (1) sub-wavelength features require fine meshing, (2) material dispersion ($\epsilon(\omega)$), (3) high Q-factor cavities need long simulation times, (4) nonlinear effects.

## 16.2 Material Modeling

### Drude Model (Metals)
$$
\epsilon(\omega) = \epsilon_\infty - \frac{\omega_p^2}{\omega^2 + j\omega\gamma}
$$

Implemented via auxiliary differential equation (ADE):

$$
\frac{\partial \mathbf{P}}{\partial t} + \gamma \mathbf{P} = \epsilon_0 \omega_p^2 \mathbf{E}
$$

### Lorentz Model (Dielectrics)
$$
\epsilon(\omega) = \epsilon_\infty + \frac{(\epsilon_s - \epsilon_\infty)\omega_0^2}{\omega_0^2 - \omega^2 + j\omega\delta}
$$

ADE implementation:
$$
\frac{\partial^2 \mathbf{P}}{\partial t^2} + \delta \frac{\partial \mathbf{P}}{\partial t} + \omega_0^2 \mathbf{P} = \epsilon_0 (\epsilon_s - \epsilon_\infty) \omega_0^2 \mathbf{E}
$$

### Sellmeier Model (Optical Glasses)
$$
n^2(\lambda) = 1 + \sum_{k=1}^K \frac{B_k \lambda^2}{\lambda^2 - C_k}
$$

## 16.3 Optical Waveguides

### 16.3.1 Dielectric Slab Waveguide
Mode field distribution: TE/TM modes solved via transcendental equation:

TE: $\kappa d = m\pi + \tan^{-1}(\gamma/\kappa)$, where $\kappa = \sqrt{n_f^2 k_0^2 - \beta^2}$, $\gamma = \sqrt{\beta^2 - n_s^2 k_0^2}$

### 16.3.2 Channel Waveguides (Rib, Ridge)
2D mode solvers (e.g., beam propagation method, finite difference) provide initial fields for FDTD propagation.

### 16.3.3 Tapered Waveguides
Adiabatic taper design: $\theta < \lambda / (2w)$ taper angle ensures >95% transmission.

## 16.4 Microcavity Resonators

### 16.4.1 Microdisk Resonators
Whispering-gallery modes (WGM) with Q > 10^6. FDTD computes:
- Resonant frequencies (from FFT of time-domain decay)
- Q-factor: $Q = \omega_0 \tau / 2$ where $\tau$ is the energy decay time constant
- Mode field patterns

### 16.4.2 Microring Resonators
Add-drop filter configuration:
- Through-port transmission: $T = |1 - t e^{-j\phi}|^2$
- Drop-port transmission: $D = |-\kappa e^{-j\phi/2}|^2$
where $t^2 + \kappa^2 = 1$ and $\phi$ is the round-trip phase.

### 16.4.3 Photonic Crystal Cavities
Point defects in PhC slabs create high-Q cavities:
- Q > 10^6 for optimized designs
- Mode volume $V_{\text{mode}} < (\lambda/n)^3$
- Purcell factor: $F_p = \frac{3}{4\pi^2} \left( \frac{\lambda}{n} \right)^3 \frac{Q}{V_{\text{mode}}}$

### 16.4.4 Racetrack Resonators
Elongated ring designs:
- Straight section length controls FSR
- Bend radius impacts radiation loss
- FDTD optimization for low-loss bends

## 16.5 Laterally Coupled Microcavity Disk Resonators

### 16.5.1 Mode Spectrum
First-order radial modes: periodic in azimuthal number $m$:
Resonant wavelengths follow: $m\lambda \approx 2\pi n_{\text{eff}} R$

### 16.5.2 Mode Suppression
Higher-order radial modes suppressed by:
- Optimizing coupling gap (evanescent coupling favors fundamental)
- Tapered waveguide couplers

## 16.6 Photonic Crystal Waveguides

### Line Defect Waveguides
Removing a row of holes creates a waveguide within the bandgap.
- Group velocity: $v_g = d\omega/dk$ (can be < c/100)
- Slow-light regime enhances nonlinear effects
- FDTD computes dispersion diagram via Bloch boundary conditions

## 16.7 Plasmonic Devices

### Surface Plasmon Polaritons (SPP)
At metal-dielectric interfaces:
$$
k_{\text{SPP}} = k_0 \sqrt{\frac{\epsilon_m \epsilon_d}{\epsilon_m + \epsilon_d}}
$$

FDTD with Drude dispersion models SPP propagation and confinement.

### Plasmonic Waveguides
- Metal strip waveguides: propagation length ~10-100 $\mu$m
- V-groove channel plasmon polaritons: enhanced confinement
- FDTD predicts loss and mode profiles

## 16.8 Nonlinear Optics

### 16.8.1 Kerr Nonlinearity (Passive)
Third-order nonlinear polarization:
$$
\mathbf{P}_{\text{NL}} = \epsilon_0 \chi^{(3)} |\mathbf{E}|^2 \mathbf{E}
$$

FDTD ADE update:
$$
\mathbf{D} = \epsilon_\infty \epsilon_0 \mathbf{E} + \mathbf{P}_{\text{NL}}
$$

### 16.8.2 Second-Harmonic Generation
$$
P_i(2\omega) = \epsilon_0 d_{ijk} E_j(\omega) E_k(\omega)
$$

FDTD naturally models SHG by including the nonlinear polarization in the Ampère update.

### 16.8.3 Raman Amplification
Stimulated Raman scattering modeled via coupled amplitude equations or full FDTD with Raman susceptibility.

## Summary

| Device | Key FDTD Feature | Typical Q | Typical Size |
|--------|-----------------|-----------|--------------|
| Microdisk | WGM resonance | $10^4-10^6$ | 2-10 $\mu$m radius |
| Microring | Add-drop filter | $10^3-10^5$ | 5-50 $\mu$m radius |
| PhC cavity | Defect mode | $10^4-10^7$ | Few $\mu$m |
| SPP waveguide | Drude model | — | 10-100 $\mu$m |
| Nonlinear device | ADE for $\chi^{(2)}$, $\chi^{(3)}$ | — | Sub-mm |
| PCF | Mode solver + FDTD | — | 1-10 cm |
| Laser | Coupled rate eq. | $10^3-10^6$ | 0.1-10 mm |

## 16.9 Time-Domain Modeling of Nonlinear Optics

### Kerr Effect (Third-Order)
The instantaneous Kerr nonlinearity is implemented directly in the FDTD Ampère update:

$$
\nabla \times \mathbf{H} = \epsilon_0 \epsilon_\infty \frac{\partial \mathbf{E}}{\partial t} + \frac{\partial \mathbf{P}_{\text{NL}}}{\partial t}, \quad \mathbf{P}_{\text{NL}} = \epsilon_0 \chi^{(3)} |\mathbf{E}|^2 \mathbf{E}
$$

For large nonlinearities, Newton-Raphson iteration is required at each time-step.

### Second-Harmonic Generation (SHG)
$$
P_i(2\omega) = \epsilon_0 d_{ijk} E_j(\omega) E_k(\omega)
$$

FDTD naturally models SHG including phase matching and pulse walk-off.

### Raman Amplification
Stimulated Raman scattering modeled via the Raman susceptibility $\chi_R^{(3)}(\Omega)$, with peak gain at ~13 THz in silica.

## 16.10 Photonic Crystal Fibers (PCF)
FDTD computes mode profiles, dispersion $D(\lambda)$, and confinement loss for:
- **Index-guiding PCF**: solid core, air-hole cladding
- **Photonic bandgap fibers**: hollow core guided by cladding bandgap

Typical parameters: $\lambda_0/(20 n_{\text{core}})$ cell size, $10\Lambda \times 10\Lambda$ domain.

## 16.11 Active Devices (Lasers, Amplifiers)
Gain via coupled rate equations:

$$
\frac{\partial N}{\partial t} = R_p - \frac{N}{\tau} - \frac{g(N)}{\hbar\omega} |\mathbf{E}|^2, \quad g(N) = \frac{N_0 \sigma_g}{1 + I/I_{\text{sat}}}
$$

Spontaneous emission added as random polarization noise. Complete laser simulation includes Maxwell solver, carrier dynamics, noise, and output coupling.

## Key Takeaways
1. **Dispersion modeling** (Drude/Lorentz/ADE) is essential for optical-frequency FDTD.
2. **High-Q cavities** require long simulation times; Padé extrapolation or Prony's method reduces requirements.
3. **Nonlinear effects** (Kerr, SHG, Raman) are naturally handled via auxiliary polarization equations.
4. **Active device modeling** extends FDTD beyond passive structures to lasers and amplifiers.
5. **PCF and plasmonic devices** push FDTD to its limits with sub-wavelength features.
