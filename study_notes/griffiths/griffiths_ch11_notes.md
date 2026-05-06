---
chapter: 11
title: Radiation
source: Griffiths, Introduction to Electrodynamics, 4th Edition
pages: 466-520
---

# Chapter 11: Radiation

## 11.1 Dipole Radiation (pp. 466-498)

### 11.1.1 What is Radiation?

Radiation = irreversible transport of energy to infinity. The power passing through a large sphere of radius $r$:

$$P(r,t) = \oint \mathbf{S}\cdot d\mathbf{a} = \frac{1}{\mu_0}\oint (\mathbf{E}\times\mathbf{B})\cdot d\mathbf{a}$$

(11.1)

For radiation to occur, $\mathbf{S} \sim 1/r^2$ (giving finite $P$ as $r\to\infty$). Static fields ($\sim 1/r^4$) don't radiate; the $1/r$ terms from time-dependent sources do.

### 11.1.2 Electric Dipole Radiation

An oscillating electric dipole $\mathbf{p}(t) = p_0\cos(\omega t)\hat{\mathbf{z}}$.

**Radiation zone** ($r \gg \lambda \gg d$): The fields are:

$$\mathbf{E} = -\frac{\mu_0 p_0 \omega^2}{4\pi}\frac{\sin\theta}{r}\cos[\omega(t-r/c)]\,\hat{\boldsymbol{\theta}}$$

$$\mathbf{B} = -\frac{\mu_0 p_0 \omega^2}{4\pi c}\frac{\sin\theta}{r}\cos[\omega(t-r/c)]\,\hat{\boldsymbol{\phi}}$$

(11.18)

**Poynting vector:**

$$\mathbf{S} = \frac{\mu_0 p_0^2\omega^4}{32\pi^2 c}\frac{\sin^2\theta}{r^2}\cos^2[\omega(t-r/c)]\,\hat{\mathbf{r}}$$

(11.19)

**Total radiated power** (time-averaged):

$$\boxed{\langle P \rangle = \frac{\mu_0 p_0^2 \omega^4}{12\pi c}}$$

(11.22)

**Angular distribution:** $dP/d\Omega \propto \sin^2\theta$ — dipole radiates most strongly perpendicular to its axis, and not at all along the axis.

### 11.1.3 Magnetic Dipole Radiation

An oscillating magnetic dipole $\mathbf{m}(t) = m_0\cos(\omega t)\hat{\mathbf{z}}$ (e.g., a small current loop).

Radiation fields:

$$\mathbf{E} = \frac{\mu_0 m_0 \omega^2}{4\pi c}\frac{\sin\theta}{r}\cos[\omega(t-r/c)]\,\hat{\boldsymbol{\phi}}$$

$$\mathbf{B} = -\frac{\mu_0 m_0 \omega^2}{4\pi c^2}\frac{\sin\theta}{r}\cos[\omega(t-r/c)]\,\hat{\boldsymbol{\theta}}$$

(11.33)

Average power:

$$\langle P \rangle = \frac{\mu_0 m_0^2 \omega^4}{12\pi c^3}$$

(11.34)

### 11.1.4 Radiation from an Arbitrary Source

For a localized source with oscillating charge/current:

- **Electric dipole** ($\mathbf{p}$): $\langle P \rangle \propto \omega^4 p_0^2/c$
- **Magnetic dipole** ($\mathbf{m}$): $\langle P \rangle \propto \omega^4 m_0^2/c^3$
- **Electric quadrupole** ($Q_{ij}$): $\langle P \rangle \propto \omega^6 Q_{ij}^2/c^5$

At low frequencies, electric dipole dominates if $\mathbf{p} \neq 0$.

---

## 11.2 Radiation from Point Charges (pp. 498-520)

### 11.2.1 Larmor Formula

For a nonrelativistic ($v \ll c$) accelerating point charge:

$$\boxed{P = \frac{\mu_0 q^2 a^2}{6\pi c}}$$

**(Larmor formula)** (11.70)

### 11.2.2 Liénard's Generalization

For relativistic motion:

$$P = \frac{\mu_0 q^2}{6\pi c}\gamma^6\left[a^2 - \left|\frac{\mathbf{v}\times\mathbf{a}}{c}\right|^2\right]$$

(11.73)

where $\gamma = 1/\sqrt{1-v^2/c^2}$.

**Special cases:**
- Acceleration parallel to velocity: $P = \frac{\mu_0 q^2}{6\pi c}\gamma^6 a^2$
- Acceleration perpendicular to velocity (circular motion): $P = \frac{\mu_0 q^2}{6\pi c}\gamma^4 a^2$

### 11.2.3 Angular Distribution of Radiation

For a point charge with arbitrary motion, the power radiated per unit solid angle:

$$\frac{dP}{d\Omega} = \frac{\mu_0 q^2}{16\pi^2 c}\frac{|\hat{\mathbf{r}}\times[(\hat{\mathbf{r}}-\boldsymbol{\beta})\times\dot{\boldsymbol{\beta}}]|^2}{(1-\hat{\mathbf{r}}\cdot\boldsymbol{\beta})^5}$$

(11.74)

where $\boldsymbol{\beta} = \mathbf{v}/c$, $\dot{\boldsymbol{\beta}} = \mathbf{a}/c$, and all quantities evaluated at retarded time. This is the **Liénard result**.

**Radiation from linear acceleration:** Forward-backward symmetric at low speeds; sharply peaked forward at relativistic speeds.

**Radiation from circular motion (synchrotron radiation):** Strongly peaked forward, with opening angle $\sim 1/\gamma$.

### 11.2.4 Radiation Reaction

An accelerating charge radiates, losing energy. This energy loss must be accounted for by a **radiation reaction force**. For nonrelativistic motion, the **Abraham-Lorentz formula** is:

$$\mathbf{F}_{\text{rad}} = \frac{\mu_0 q^2}{6\pi c}\dot{\mathbf{a}}$$

(11.92)

This force is proportional to the **third derivative** of position (the jerk). Key properties:
- Very small: for an electron in a classical orbit, $F_{\text{rad}}/F_{\text{Coulomb}} \sim 10^{-23}$
- Causality problems: **pre-acceleration** (the force depends on future acceleration)
- Runaway solutions: the equation $m\dot{v} = F_{\text{ext}} + \tau\ddot{v}$ (with $\tau = \mu_0 q^2/6\pi mc$) admits exponentially growing spurious solutions

The relativistic generalization is the **Abraham-Lorentz-Dirac force**.

**Example 11.3** (p. 517): **Classical electron radius.** Equating the electrostatic self-energy to rest energy:

$$\frac{e^2}{4\pi\epsilon_0 r_e} = m_e c^2 \quad\Rightarrow\quad r_e = \frac{e^2}{4\pi\epsilon_0 m_e c^2} \approx 2.8\times10^{-15}\ \text{m}$$

This is the scale at which classical electrodynamics breaks down and quantum effects dominate.

### 11.2.5 Multipole Radiation Summary

| Radiation type | Source | Power $\propto$ | Angular pattern |
|---------------|--------|-----------------|-----------------|
| Electric dipole | $\mathbf{p}$ | $\omega^4 p_0^2/c$ | $\sin^2\theta$ (doughnut) |
| Magnetic dipole | $\mathbf{m}$ | $\omega^4 m_0^2/c^3$ | $\sin^2\theta$ |
| Electric quadrupole | $Q_{ij}$ | $\omega^6 Q_0^2/c^5$ | More complex |
| Relativistic charge | $\gamma m \mathbf{a}$ | $\gamma^4 a^2$ (perp.) | Strongly forward-peaked |

---

### Chapter Summary

| Concept | Formula |
|---------|---------|
| Electric dipole power | $\langle P \rangle = \mu_0 p_0^2 \omega^4/12\pi c$ (11.22) |
| Magnetic dipole power | $\langle P \rangle = \mu_0 m_0^2 \omega^4/12\pi c^3$ (11.34) |
| Larmor formula | $P = \mu_0 q^2 a^2/6\pi c$ (11.70) |
| Liénard formula | $P = \mu_0 q^2\gamma^6[a^2 - |\mathbf{v}\times\mathbf{a}/c|^2]/6\pi c$ (11.73) |
| Radiation reaction | $\mathbf{F}_{\text{rad}} = \mu_0 q^2\dot{\mathbf{a}}/6\pi c$ (11.92) |

**物理直觉（全章回顾）：** 辐射是加速电荷"甩掉"电磁场能量到无穷远的过程。电偶极辐射是最重要的辐射模式——功率正比于 $\omega^4$，蓝光比红光散射更强（天空为什么是蓝色的）。非相对论性粒子的辐射由 Larmor 公式描述；相对论性粒子的辐射强烈地向前聚焦（同步辐射）。辐射反作用力虽小，但带来深刻的物理问题（经典电动力学的自洽性危机）。
