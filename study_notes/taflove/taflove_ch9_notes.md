---
chapter: 9
title: Dispersive, Nonlinear, and Gain Materials
book: Computational Electrodynamics — 3rd Ed.
raw_size: 101,845 bytes
---

# Chapter 9: Dispersive, Nonlinear, and Gain Materials

## 9.1 Introduction
FDTD naturally handles dispersive, nonlinear, and active media. Three main approaches: PLRC (piecewise-linear recursive convolution), ADE (auxiliary differential equation), and Z-transform methods.

## 9.2 Generic Material Dispersion Models

### Debye (Relaxation)
$$\epsilon_r(\omega) = \epsilon_\infty + \sum_{p=1}^P \frac{\Delta\epsilon_p}{1 + j\omega\tau_p} \tag{9.1}$$
Time-domain susceptibility: $\chi(t) = \sum_p \frac{\Delta\epsilon_p}{\tau_p} e^{-t/\tau_p} u(t) \tag{9.2}$

### Lorentz (Resonance)
$$\epsilon_r(\omega) = \epsilon_\infty + \sum_{p=1}^P \frac{\Delta\epsilon_p \omega_p^2}{\omega_p^2 + 2j\omega\delta_p - \omega^2} \tag{9.4}$$
Time-domain: $\chi(t) = \sum_p \frac{\Delta\epsilon_p \omega_p^2}{\sqrt{\omega_p^2 - \delta_p^2}} e^{-\delta_p t} \sin\left(\sqrt{\omega_p^2 - \delta_p^2} t\right) u(t) \tag{9.5}$

### Drude (Metals)
$$\epsilon_r(\omega) = \epsilon_\infty - \sum_{p=1}^P \frac{\omega_p^2}{\omega^2 + j\omega\gamma_p} \tag{9.7}$$
Time-domain: $\chi(t) = -\sum_p \frac{\omega_p^2}{\gamma_p} (1 - e^{-\gamma_p t}) u(t)$

## 9.3 PLRC Method
$$\mathbf{D}(t) = \epsilon_0\epsilon_\infty \mathbf{E}(t) + \epsilon_0 \int_0^t \mathbf{E}(t - \tau) \chi(\tau) d\tau$$
PLRC approximates $\mathbf{E}$ as linear between time-steps:
$$\mathbf{D}^n = \epsilon_0\epsilon_\infty \mathbf{E}^n + \epsilon_0 \sum_{m=0}^{N-1} \mathbf{E}^{n-m} \chi^m + \mathbf{E}^{n-m-1} \xi^m$$

## 9.4 ADE Method (Linear Dispersive)
Introduce polarization current $\mathbf{J}_p$:
$$\frac{d\mathbf{J}_p}{dt} + \Gamma \mathbf{J}_p = \epsilon_0 \omega_p^2 \mathbf{E} \quad \text{(Drude)}$$
$$\frac{d^2\mathbf{P}}{dt^2} + 2\delta\frac{d\mathbf{P}}{dt} + \omega_0^2 \mathbf{P} = \epsilon_0 \Delta\epsilon \omega_0^2 \mathbf{E} \quad \text{(Lorentz)}$$

## 9.5 Nonlinear Dispersive Media (Kerr, Raman)
$$\mathbf{P}_{\text{NL}} = \chi^{(3)} |\mathbf{E}|^2 \mathbf{E}$$
Use ADE with nonlinear polarization term, solved via predictor-corrector or Newton iteration.

## 9.6 Active Gain Media (Lasers)
For a four-level gain system + Lorentz dispersion:
$$\frac{dN_1}{dt} = \frac{N_2}{\tau_{21}} - \frac{N_1}{\tau_{10}} + \frac{\mathbf{E} \cdot d\mathbf{P}/dt}{\hbar\omega_a}$$
$$\frac{dN_0}{dt} = \frac{N_1}{\tau_{10}} - R_p \quad \text{(pumping)}$$

## Examples
- **Ex 9.1:** FDTD + Drude model — optical reflection from silver at 600 nm
- **Ex 9.2:** Lorentz medium — pulse propagation in dispersive dielectric slab
- **Ex 9.3:** Saturable gain — laser cavity startup dynamics
