---
title: "Chapter 6 — Fields and Waves in Cylindrical Coordinates"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Cylindrical wave functions (Bessel, Hankel functions)
  - Circular waveguide TE/TM modes
  - Coaxial waveguide TEM/TE/TM modes
  - Dielectric rod waveguide
  - Plane wave expansion in cylindrical harmonics
  - Scattering by conducting/dielectric cylinders
  - Line source and wedge radiation
---

# Chapter 6: Fields and Waves in Cylindrical Coordinates

## 6.1 Solution of Wave Equation

In cylindrical coordinates, Helmholtz equation separates as $\psi = P(\rho)\Phi(\phi)Z(z)$.

**$Z(z)$:** $e^{\pm jk_z z}$ (propagating) or $e^{\pm \alpha_z z}$ (evanescent).

**$\Phi(\phi)$:** $e^{\pm j n\phi}$, $n = 0, 1, 2, \dots$

**$P(\rho)$:** Bessel equation $\rightarrow$ $J_n(k_\rho \rho)$, $Y_n(k_\rho \rho)$, $H_n^{(1)}(k_\rho \rho)$, $H_n^{(2)}(k_\rho \rho)$.

where $k_\rho^2 = k^2 - k_z^2$.

---

## 6.2 Circular Waveguide

**TE$_{nm}$ modes:** $H_z = J_n(k_c \rho) e^{\pm j n\phi}$, $k_c = p'_{nm}/a$ ($p'_{nm}$ = nth zero of $J_n'$).

**TM$_{nm}$ modes:** $E_z = J_n(k_c \rho) e^{\pm j n\phi}$, $k_c = p_{nm}/a$ ($p_{nm}$ = nth zero of $J_n$).

**Dominant mode:** TE$_{11}$ — lowest cutoff.

---

## 6.3 Coaxial Waveguide

**TEM mode:** $E_\rho = V_0/(\rho \ln(b/a))$, $H_\phi = I_0/(2\pi\rho)$.

**TE/TM modes:** Similar to circular but with both $J_n$ and $Y_n$.

---

## 6.4 Circular Dielectric Waveguide (Optical Fiber)

Hybrid HE/EH modes. For weakly guiding ($\Delta \ll 1$): LP modes.

---

## 6.5 Plane Wave / Cylindrical Function Transform

$$
e^{-jk\rho \cos\phi} = \sum_{n=-\infty}^{\infty} j^{-n} J_n(k\rho) e^{jn\phi}
$$

---

## 6.6 Scattering by Cylinders

Conducting cylinder: Mie series solution using cylindrical harmonics.

Dielectric cylinder: internal + external fields matched at boundary.

---

## Audit

| Section | Topic |
|---------|-------|
| 6.1 | Cylindrical wave functions |
| 6.2 | Circular waveguide |
| 6.3 | Coaxial waveguide |
| 6.4 | Dielectric rod waveguide |
| 6.5 | Plane wave expansion |
| 6.6 | Cylinder scattering |
