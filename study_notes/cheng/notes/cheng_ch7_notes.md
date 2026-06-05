# 程守洙《普通物理学》电磁学部分 第7章：电磁场与电磁波

> **来源：** 谢处方等，《电磁场与电磁波》，第7章
> **提取方式：** 📷 扫描PDF → OCR → 人工清洗

---

## 7.1 电磁场与电磁波 | Electromagnetic Fields and Waves

# David K. Cheng《Field and Wave Electromagnetics》2nd Ed Chapter 7
 本笔记基于  文本清洗整理100% 来源于原书内容
## Chapter 7 — Time-Varying Fields and Maxwell's Equations
### 7-1. Introduction
This chapter extends the static field equations to **time-varying** situations. The key insight is that a changing electric field produces a magnetic field, and vice versa.
### 7-2. Time-Varying Fields
**Displacement current:** Maxwell recognized that the continuity equation $\nabla \cdot \mathbf{J} = -\partial$\rho$/\partial t$, combined with Gauss's law $\nabla \cdot \mathbf{D} = \rho$, requires modifying Ampère's law:
$$\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t} \quad \text{(Maxwell-Ampère equation)}$$
The term $\partial\mathbf{D}/\partial t$ is the **displacement current density**, which allows magnetic fields to exist even in regions with no conduction current (e.g., vacuum, capacitors).
### 7-3. Maxwell's Equations
**Differential Form:**
| Name | Equation |
|---|---|
| Faraday's law | $\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$ |
| Maxwell-Ampère | $\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}$ |
| Gauss's law for electricity | $\nabla \cdot \mathbf{D} = \rho$ |
| Gauss's law for magnetism | $\nabla \cdot \mathbf{B} = 0$ |
**Integral Form:**
$$\oint_C \mathbf{E} \cdot d\boldsymbol{\ell} = -\frac{d}{dt}\int_$\mathbf{S}$ \mathbf{B} \cdot d\mathbf{S} \quad \text{(Faraday's law)}$$
$$\oint_C \mathbf{H} \cdot d\boldsymbol{\ell} = I_{\text{cond}} + \frac{d}{dt}\int_$\mathbf{S}$ \mathbf{D} \cdot d\mathbf{S} \quad \text{(Maxwell-Ampère)}$$
$$\oint_$\mathbf{S}$ \mathbf{D} \cdot d\mathbf{S} = Q_{\text{enc}} \quad \text{(Gauss's law for $\mathbf{E}$)}$$
$$\oint_$\mathbf{S}$ \mathbf{B} \cdot d\mathbf{S} = 0 \quad \text{(Gauss's law for $\mathbf{B}$)}$$
### 7-4. Time-Varying Potentials
Since $\nabla \times \mathbf{E} = -\partial\mathbf{B}/\partial t$, we can still write $\mathbf{E} = -\nabla V - \partial\mathbf{A}/\partial t$.
The **Lorentz gauge** condition for time-varying fields:
$$\nabla \cdot \mathbf{A} + \mu_0\varepsilon_0\frac{\partial V}{\partial t} = 0$$
This leads to the **wave equations** for $V$ and $\mathbf{A}$.
### 7-5. The Wave Equations
In free space ($\rho = 0$, $\mathbf{J} = 0$):
$$\nabla^2 \mathbf{E} = \mu_0\varepsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2} = \frac{1}{c^2}\frac{\partial^2 \mathbf{E}}{\partial t^2}$$
$$\nabla^2 \mathbf{H} = \mu_0\varepsilon_0 \frac{\partial^2 \mathbf{H}}{\partial t^2} = \frac{1}{c^2}\frac{\partial^2 \mathbf{H}}{\partial t^2}$$
where $c = 1/\sqrt{\mu_0\varepsilon_0} = 2.998 \times 10^8$ m/s (speed of light in vacuum).
### 7-6. Time-Harmonic Fields
For sinusoidal (time-harmonic) steady-state analysis, we use **phasors**. With $e^{j\omega t}$ time dependence:
$$\nabla \times \tilde{\mathbf{E}} = -j\omega \tilde{\mathbf{B}}$$
$$\nabla \times \tilde{\mathbf{H}} = \tilde{\mathbf{J}} + j\omega \tilde{\mathbf{D}}$$
Maxwell's equations in phasor form are algebraic and easier to solve.
### Review Questions (Chapter 7)
1. Why was the displacement current term added to Ampère's law?
2. Write all four Maxwell's equations in both differential and integral forms.
3. What is the speed of electromagnetic waves in free space?
4. What is the Lorentz gauge condition?
5. Why are phasors useful in electromagnetic analysis?
---