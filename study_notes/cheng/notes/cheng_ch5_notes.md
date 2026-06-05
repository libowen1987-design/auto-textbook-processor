# 程守洙《普通物理学》电磁学部分 第5章：电磁感应

> **来源：** 谢处方等，《电磁场与电磁波》，第5章
> **提取方式：** 📷 扫描PDF → OCR → 人工清洗

---

## 5.1 电磁感应 | Electromagnetic Induction

# David K. Cheng《Field and Wave Electromagnetics》2nd Ed Chapter 5
 本笔记基于  文本清洗整理100% 来源于原书内容
## Chapter 5 — Steady-State Electric Currents
### 5-1. Introduction
This chapter deals with **steady electric currents** — charges in steady motion (DC).
### 5-2. Current Density and Ohm's Law
**Volume current density** $\mathbf{J}$ ($\mathbf{A}$/m$^2$) relates to the drift velocity $\mathbf{u}_d$:
$$\mathbf{J} = \rho_q \mathbf{u}_d = n q \mathbf{u}_d$$
where $n$ is the number of charge carriers per unit volume and $q$ is the charge per carrier.
**Microscopic Ohm's law:**
$$\mathbf{J} = \sigma \mathbf{E}$$
where $\sigma$ is the **conductivity** ($\mathbf{S}$/m = $\Omega^{-1}$ m$^{-1}$).
**Conductivity of a conductor:**
$$\sigma = ne\mu_e$$
where $\mu_e$ is the electron mobility.
**Resistivity** $\rho = 1/\sigma$ (not to be confused with charge density).
### 5-3. Electromotive Force and Kirchhoff's Voltage Law
For a current $I$ to be maintained in a closed circuit, an **electromotive force (emf)** $\mathcal{E}$ is needed:
$$\mathcal{E} = \oint \mathbf{E} \cdot d\boldsymbol{\ell}$$
where $\mathbf{E}$ includes both the conservative electrostatic field and the non-electrostatic field driving the current.
**Kirchhoff's voltage law (KVL):**
$$\sum_{k} V_$\mathbf{k}$ = 0 \quad \text{(around any closed loop)}$$
### 5-4. Equation of Continuity and Kirchhoff's Current Law
**Equation of continuity** (conservation of charge):
$$\nabla \cdot \mathbf{J} = -\frac{\partial \rho}{\partial t}$$
For **steady currents** ($\partial$\rho$/\partial t = 0$):
$$\nabla \cdot \mathbf{J} = 0$$
**Kirchhoff's current law (KCL):**
$$\sum_{k} I_$\mathbf{k}$ = 0 \quad \text{(sum of currents at a junction = 0)}$$
This is the integral form of $\nabla \cdot \mathbf{J} = 0$ for steady currents.
### 5-5. Power Dissipation and Joule's Law
**Power dissipated** per unit volume:
$$p = \mathbf{J} \cdot \mathbf{E} = \sigma |\mathbf{E}|^2 = \frac{|\mathbf{J}|^2}{\sigma} \quad \text{(W/m}^3\text{)}$$
**Joule's law** for a resistor: $$\mathbf{P}$ = I^2 R = V^2 / R = VI$
### 5-6. Boundary Conditions for Current Density
At the interface between two media with conductivities $\sigma_1$ and $\sigma_2$:
$$\hat{\mathbf{n}} \cdot (\mathbf{J}_2 - \mathbf{J}_1) = 0$$
Since $\mathbf{J} = \sigma \mathbf{E}$ and $\hat{\mathbf{n}} \times \mathbf{E}$ is continuous:
$$\frac{$\mathbf{J}$_{2n}}{\sigma_2} = \frac{$\mathbf{J}$_{1n}}{\sigma_1}$$
### 5-7. Resistance Calculations
The resistance $R$ between two equipotential surfaces:
$$R = \frac{V}{I} = \frac{\int_\ell \mathbf{E} \cdot d\boldsymbol{\ell}}{\int_$\mathbf{S}$ \sigma \mathbf{E} \cdot d\mathbf{S}}$$
**Example — Resistance of a wire** of length $\ell$, cross-section $S$, conductivity $\sigma$:
$$R = \frac{\ell}{\sigma S}$$
### Review Questions (Chapter 5)
1. State Ohm's law in both microscopic and macroscopic forms.
2. Write the equation of continuity and explain its physical meaning.
3. State Kirchhoff's voltage and current laws.
4. What is Joule heating?
5. What are the boundary conditions for current density at an interface?
---