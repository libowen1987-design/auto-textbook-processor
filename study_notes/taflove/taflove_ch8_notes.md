---
chapter: 8
title: Near-to-Far-Field Transformation
book: Computational Electrodynamics — 3rd Ed.
author: Taflove, Li, Hagness
raw_size: 49,226 bytes
---

# Chapter 8: Near-to-Far-Field (NTFF) Transformation

## 8.1 Introduction
Using a single FDTD run, the NTFF transformation computes far-field bistatic RCS or antenna radiation patterns from near fields on a virtual surface enclosing the scatterer/antenna.

**Key advantage:** Lattice need not extend to far-field region. NTFF surface is placed in the scattered-field region (Ch5 TF/SF), and time-domain fields recorded over one or more frequency bins via DFT.

## 8.2 2D Transformation (Phasor Domain)
Using Green's theorem, far-field $E_z^{\text{ff}}$ from tangential $E_z$ and $H_{\text{tan}}$ on contour $C_0$:

$$E_z^{\text{ff}}(\rho,\phi) = \frac{e^{-jk\rho}}{\sqrt{\rho}} F(\phi)$$
$$F(\phi) = \sqrt{\frac{k}{8\pi}} e^{-j\pi/4} \oint_{C_0} \left[ jk(\hat{n}\cdot\hat{\rho}')E_z - j\omega\mu_0(\hat{n}\times\hat{z})\cdot\hat{\phi} H_{\text{tan}} \right] e^{jk\hat{\rho}\cdot\mathbf{r}'} d\ell'$$

## 8.3 3D Transformation (Phasor Domain)

$$\mathbf{E}^{\text{ff}}(r,\theta,\phi) = \frac{e^{-jkr}}{r} \mathbf{F}(\theta,\phi)$$

The far-field pattern vector $\mathbf{F}$ is computed from equivalent electric and magnetic currents on the NTFF surface:

$$\mathbf{J}_{\text{eq}} = \hat{n} \times \mathbf{H}_{\text{near}}, \quad \mathbf{M}_{\text{eq}} = -\hat{n} \times \mathbf{E}_{\text{near}}$$

$$\mathbf{F}(\theta,\phi) = \frac{jk}{4\pi} \iint_S \left[ \eta_0 \hat{r} \times (\hat{r} \times \mathbf{J}_{\text{eq}}) + \hat{r} \times \mathbf{M}_{\text{eq}} \right] e^{jk\hat{r}\cdot\mathbf{r}'} dS'$$

## 8.4 Time-Domain NTFF
The time-domain NTFF yields direct time waveforms at far-field observation points:

$$E_{\theta}^{\text{ff}}(r,\theta,\phi,t) = \frac{1}{2\pi c r} \frac{\partial}{\partial t} \iint_S \left[ -\mu_0 J_{\theta}^{\text{eq}} + \frac{1}{c} M_{\phi}^{\text{eq}} \right]_{\text{ret}} dS'$$

where [ ]$_{\text{ret}}$ indicates evaluation at retarded time $t - r/c + \hat{r}\cdot\mathbf{r}'/c$.

## 8.5 Backscatter Enhancement
For strongly forward-scattering objects (e.g., biological cells, stealth vehicles), a modified NTFF procedure subtracts the forward-scattered component before integration, reducing numerical cancellation errors.

## Examples
- **Ex 8.1:** 2D TM$_z$ RCS of a PEC cylinder — compare to Mie series
- **Ex 8.2:** 3D NTFF — radiation pattern of a half-wave dipole
- **Ex 8.3:** Time-domain NTFF — backscattered pulse from a dielectric sphere

> **Numerical Intuition:** NTFF enables accurate far-field RCS and antenna patterns from compact FDTD domains. The virtual surface should be at least 10 cells from the structure. Using DFT over $N_f$ frequency points adds $O(N_f N_s)$ storage where $N_s$ is the number of surface cells.
