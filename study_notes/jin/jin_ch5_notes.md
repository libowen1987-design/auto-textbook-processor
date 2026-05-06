---
title: "Chapter 5 — Fields and Waves in Rectangular Coordinates"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - General theory of uniform waveguides (TE, TM, TEM modes)
  - Rectangular waveguide TE/TM modes
  - Cutoff frequency and dispersion
  - Rectangular cavities and resonators
  - Dielectric slab waveguide
  - Green's function for planar layered media
---

# Chapter 5: Fields and Waves in Rectangular Coordinates

## 5.1 Uniform Waveguides

Fields in a uniform waveguide ($e^{-jk_z z}$ dependence):

$$
\mathbf{E} = (\mathbf{e}_t + \hat{z} e_z) e^{-jk_z z}, \quad
\mathbf{H} = (\mathbf{h}_t + \hat{z} h_z) e^{-jk_z z}
$$

**Transverse fields in terms of longitudinal components:**

$$
\mathbf{E}_t = \frac{1}{k_t^2} \left( j\omega\mu \hat{z} \times \nabla_t H_z - jk_z \nabla_t E_z \right)
\tag{5.1.11}
$$

$$
\mathbf{H}_t = \frac{1}{k_t^2} \left( -j\omega\epsilon \hat{z} \times \nabla_t E_z - jk_z \nabla_t H_z \right)
\tag{5.1.12}
$$

where $k_t^2 = k^2 - k_z^2$.

**Three mode types:**
- **TEM** ($E_z = H_z = 0$): $k_z = k$, no cutoff
- **TE** ($E_z = 0$): $H_z$ satisfies $\nabla_t^2 H_z + k_t^2 H_z = 0$
- **TM** ($H_z = 0$): $E_z$ satisfies $\nabla_t^2 E_z + k_t^2 E_z = 0$

**Cutoff wavenumber:** $k_c = k_t$ — propagation only when $k > k_c$ ($f > f_c$).

---

## 5.2 Rectangular Waveguide

For a waveguide with cross-section $a \times b$:

**TM$_{mn}$ modes:**

$$
E_z = \sin\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right)
$$

$$
k_c = \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}, \quad
f_c = \frac{k_c}{2\pi\sqrt{\mu\epsilon}}
$$

**TE$_{mn}$ modes:**

$$
H_z = \cos\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right)
$$

**Dominant mode:** TE$_{10}$ (lowest cutoff).

**Waveguide wavelength:** $\lambda_g = \frac{2\pi}{\sqrt{k^2 - k_c^2}}$.

**Attenuation:** from conductor losses and dielectric losses.

---

## 5.3 Rectangular Cavity

A waveguide section of length $d$ shorted at both ends.

**Resonant frequencies:**

$$
f_{mnp} = \frac{1}{2\pi\sqrt{\mu\epsilon}} \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2 + \left(\frac{p\pi}{d}\right)^2}
$$

**Quality factor:** $Q = \omega_0 W / P_{\text{loss}}$.

---

## 5.4 Dielectric Slab Waveguide

Guided by total internal reflection. TE and TM surface wave modes.

**Dispersion relation (TE):**

$$
\kappa d = m\pi + 2\tan^{-1}(\gamma/\kappa)
$$

where $\kappa = \sqrt{k_f^2 - k_z^2}$, $\gamma = \sqrt{k_z^2 - k_c^2}$, $k_f = \omega\sqrt{\mu\epsilon_f}$, $k_c = \omega\sqrt{\mu\epsilon_c}$.

---

## 5.5 Green's Function for Planar Layered Media

Constructed using TE/TM decomposition and transmission line analogy.

---

## Key Physical Intuition

1. **Waveguide modes** are standing waves in the transverse plane and traveling waves longitudinally.
2. **Cutoff** occurs when $k < k_c$ — below cutoff, modes are evanescent.
3. **TE$_{10}$** is the dominant mode because it has the simplest field pattern and lowest cutoff.
4. **Cavity resonators** store energy at discrete frequencies — essential for filters and oscillators.

---

## Audit

| Section | Content Coverage |
|---------|-----------------|
| 5.1 | Uniform waveguide theory |
| 5.2 | Rectangular waveguide |
| 5.3 | Rectangular cavity |
| 5.4 | Dielectric slab waveguide |
| 5.5 | Green's function, layered media |
