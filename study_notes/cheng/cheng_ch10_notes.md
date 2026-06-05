# David K. Cheng《Field and Wave Electromagnetics》2nd Ed Chapter 10

> 本笔记基于 OCR 文本清洗整理，100% 来源于原书内容。

## Chapter 10 — Waveguides and Cavity Resonators

### 10-1. Introduction

**Waveguides** are hollow or dielectric-filled conducting structures that guide electromagnetic waves. Unlike transmission lines, waveguides support **non-TEM** modes (TE and TM), which require a cutoff frequency.

### 10-2. General Wave Behaviors along Uniform Guiding Structures

For wave propagation along $z$ with $e^{-\gamma z}$:
$$\frac{\partial^2}{\partial z^2} \gg \frac{\partial^2}{\partial x^2}, \frac{\partial^2}{\partial y^2}$$

For uniform waveguides, Maxwell's equations separate into independent **TE** (transverse electric, $E_z = 0$) and **TM** (transverse magnetic, $H_z = 0$) modes.

**Propagation constant:**
$$\gamma = \sqrt{k_c^2 - k^2}$$
where $k = \omega\sqrt{\mu\varepsilon}$ and $k_c$ is the cutoff wave number determined by boundary conditions.

**Cutoff frequency:** $f_c = \frac{k_c}{2\pi\sqrt{\mu\varepsilon}}$

For $f > f_c$: $\gamma = j\beta$ (propagating); for $f < f_c$: $\gamma = \alpha$ (evanescent).

### 10-3. Parallel-Plate Waveguide

For a parallel-plate waveguide with plate separation $d$ (in vacuum):

**TE modes** ($H_z \neq 0$, $E_z = 0$):
$$k_c = \frac{m\pi}{d}, \quad m = 0,1,2,\ldots$$
$$f_c = \frac{mc}{2d}$$

The **dominant TE mode** is $\text{TE}_1$ ($m=1$): $f_c = c/(2d)$.

**TM modes** ($E_z \neq 0$, $H_z = 0$):
$$k_c = \frac{m\pi}{d}, \quad m = 1,2,\ldots$$
(No TM$_0$ mode since $m=0$ gives trivial solution.)

### 10-4. Rectangular Waveguides

For a rectangular waveguide of width $a$ (along $x$) and height $b$ (along $y$):

**TE modes** ($E_z = 0$):
$$k_c = \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}, \quad m,n = 0,1,2,\ldots \text{ (not both zero)}$$
$$f_{c,m,n} = \frac{c}{2}\sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}$$

**Dominant TE mode:** $\text{TE}_{10}$ ($m=1, n=0$), $f_c = c/(2a)$.

**TM modes** ($H_z = 0$):
$$k_c = \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}, \quad m,n = 1,2,\ldots \text{ (both non-zero)}$$
(No TM$_{m0}$ or TM$_{0n}$ modes.)

**Phase velocity:**
$$u_p = \frac{\omega}{\beta} = \frac{c}{\sqrt{1-(f_c/f)^2}} > c$$

**Group velocity:**
$$u_g = \frac{d\omega}{d\beta} = c\sqrt{1-(f_c/f)^2} < c$$

**Wave impedance:**
- For TE: $\eta_{\text{TE}} = \frac{\eta_0}{\sqrt{1-(f_c/f)^2}} = \frac{\eta_0\beta}{k}$
- For TM: $\eta_{\text{TM}} = \eta_0\sqrt{1-(f_c/f)^2} = \eta_0\frac{k}{\beta}$

### 10-5. Dielectric Waveguides

For a dielectric slab waveguide, modes are hybrid (HE/EH) with no cutoff for some modes. The field extends beyond the dielectric boundary as an evanescent wave (for the cladding).

### 10-6. Cavity Resonators

A **cavity resonator** is a closed conducting structure that supports resonant modes at specific frequencies.

**Rectangular cavity** ($a \times b \times d$):

For $\text{TE}_{mnp}$ modes:
$$f_{mnp} = \frac{c}{2}\sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2 + \left(\frac{p}{d}\right)^2}$$

**Quality factor $Q$:**
$$Q = \frac{\omega_0 W}{P_d} = \frac{\text{stored energy}}{\text{energy dissipated per radian}}$$

For a rectangular cavity with perfect conductors and walls of surface resistance $R_s$:
$$Q_{\text{TE}_{mnp}} = \frac{(kl)^3 b\,d\,a}{2R_s}\frac{1}{\left(\frac{l^2}{a^3}d + \frac{l^2}{b^3}a + \frac{k^2}{d^3}ab\right)\left(1+\frac{n^2 a^3}{m^2 b^3}+\frac{p^2 a^3}{m^2 d^3}\right)}$$

### Review Questions (Chapter 10)

1. Why do waveguides have a cutoff frequency?
2. What is the difference between TE and TM modes?
3. What is the dominant mode in a rectangular waveguide and why?
4. Define phase velocity and group velocity in waveguides.
5. What is a cavity resonator? How are its resonant frequencies determined?

---

