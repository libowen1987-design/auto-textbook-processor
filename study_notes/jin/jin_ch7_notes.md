---
title: "Chapter 7 — Fields and Waves in Spherical Coordinates"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Spherical wave functions (spherical Bessel, Legendre)
  - Spherical cavity and biconical antenna
  - Plane wave expansion in spherical harmonics
  - Mie scattering by spheres (conducting, dielectric)
  - Addition theorem for spherical waves
---

# Chapter 7: Fields and Waves in Spherical Coordinates

## 7.1 Solution of Wave Equation

Separate $\psi(r,\theta,\phi) = R(r) \Theta(\theta) \Phi(\phi)$.

**$\Phi$:** $e^{\pm j m\phi}$.

**$\Theta$:** Associated Legendre equation $\rightarrow$ $P_n^m(\cos\theta)$.

**$R$:** Spherical Bessel equation $\rightarrow$ $j_n(kr)$, $y_n(kr)$, $h_n^{(1)}(kr)$, $h_n^{(2)}(kr)$.

---

## 7.2 Spherical Cavity and Biconical Antenna

**Spherical cavity:** resonant modes via spherical Bessel function zeros. TE$_{nmp}$ and TM$_{nmp}$ modes.

**Biconical antenna:** TEM mode between two cones. Input impedance depends on cone angles.

---

## 7.3 Plane Wave Expansion

$$
e^{-jkz} = \sum_{n=0}^\infty j^{-n}(2n+1) j_n(kr) P_n(\cos\theta)
$$

---

## 7.4 Mie Scattering by a Sphere

**Conducting sphere:** zero tangential $\mathbf{E}$ on surface. Series solution using spherical harmonics.

**Dielectric sphere:** internal and external fields matched at $r=a$.

**Scattering cross-section $\sigma_s$** and **extinction cross-section $\sigma_e$**.

---

## 7.5 Addition Theorem

Translates spherical wave functions between origins — essential for multiple-sphere scattering.

---

## Audit

| Section | Topic |
|---------|-------|
| 7.1 | Spherical wave functions |
| 7.2 | Cavity, biconical antenna |
| 7.3 | Plane wave expansion |
| 7.4 | Mie scattering |
| 7.5 | Addition theorem |
