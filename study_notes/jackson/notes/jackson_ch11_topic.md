# Chapter 11: Special Theory of Relativity / 狭义相对论

> Jackson *Classical Electrodynamics*, 3rd Ed, §11.1–11.13

---

## 1. Overview / 概述

Special relativity reconciles electromagnetism with the principle that all inertial observers measure the same speed of light $c$. Maxwell's equations are **Lorentz covariant** — they keep the same form in all inertial frames.

**Key insight**: Electric and magnetic fields are not independent; they transform into each other under Lorentz boosts. What looks like a pure electric field in one frame may have a magnetic component in another.

---

## 2. 洛伦兹变换 (Lorentz Transformations) / 洛伦兹变换 (Lorentz Transformations)

### 2.1 标准形式 (Standard Form) / 2.1 标准形式 (Standard Form)

Boost along $x$-axis with velocity $v = \beta c$, $\gamma = 1/\sqrt{1-\beta^2}$:

$$
ct' = \gamma(ct - \beta x)
$$
$$
x' = \gamma(x - \beta ct)
$$
$$
y' = y, \quad z' = z
$$

### 2.2 四维形式 (Four-Vector Form) / 2.2 四维形式 (Four—Vector Form)

$$
x'^\mu = \Lambda^\mu_{\ \nu} x^\nu
$$

Lorentz boost matrix (along $x$):

$$
\Lambda^\mu_{\ \nu} = \begin{pmatrix}
\gamma & -\gamma\beta & 0 & 0 \\
-\gamma\beta & \gamma & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

### 2.3 广义洛伦兹变换 (General Boost) / 2.3 广义洛伦兹变换 (General Boost)

For an arbitrary direction $\boldsymbol{\beta} = \mathbf{v}/c$:

$$
\Lambda^0_{\ 0} = \gamma, \quad \Lambda^0_{\ i} = \Lambda^i_{\ 0} = -\gamma \beta_i
$$
$$
\Lambda^i_{\ j} = \delta_{ij} + (\gamma - 1) \frac{\beta_i \beta_j}{\beta^2}
$$

**Invariant interval**:

$$
ds^2 = c^2 dt^2 - dx^2 - dy^2 - dz^2 = \text{invariant}
$$

---

## 3. 四维张量 (Four-Tensors) / 四维张量 (Four—Tensors)

### 3.1 基本四矢量 (Fundamental 4-Vectors) / 3.1 基本四矢量 (Fundamental 4—Vectors)

| 4-Vector | Components | Invariant |
|----------|-----------|-----------|
| Position | $x^\mu = (ct, \mathbf{x})$ | $x_\mu x^\mu = c^2 t^2 - r^2$ |
| Velocity | $U^\mu = \gamma_v(c, \mathbf{v})$ | $U_\mu U^\mu = c^2$ |
| Momentum | $p^\mu = (E/c, \mathbf{p})$ | $p_\mu p^\mu = m^2 c^2$ |
| Potential | $A^\mu = (\Phi/c, \mathbf{A})$ | — |
| Current | $J^\mu = (c\rho, \mathbf{J})$ | $\partial_\mu J^\mu = 0$ |
| Wave vector | $k^\mu = (\omega/c, \mathbf{k})$ | $k_\mu k^\mu = 0$ (lightlike) |

**Energy-momentum relation**:

$$
E^2 = p^2 c^2 + m^2 c^4
$$

For a massless particle: $E = pc$.

### 3.2 度规与张量运算 (Metric and Tensor Operations) / 3.2 度规与张量运算 (Metric与Tensor Operations)

**Minkowski metric** (signature +,−,−,−):

$$
g_{\mu\nu} = g^{\mu\nu} = \operatorname{diag}(1, -1, -1, -1)
$$

**Raising/lowering indices**: $A_\mu = g_{\mu\nu} A^\nu$, $A^\mu = g^{\mu\nu} A_\nu$

**Lorentz scalars**: quantities unchanged by Lorentz transformations (e.g., $F_{\mu\nu}F^{\mu\nu}$, $\partial_\mu J^\mu$)

---

## 4. 电磁场的协变形式 (Covariant Form of Electromagnetism) / 电磁场的协变形式 (Covariant Form of Electromagnetism)

### 4.1 场强张量 (Field Strength Tensor) / 4.1 场强张量 (Field Strength Tensor)

$$
F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu =
\begin{pmatrix}
0 & -E_x/c & -E_y/c & -E_z/c \\
E_x/c & 0 & -B_z & B_y \\
E_y/c & B_z & 0 & -B_x \\
E_z/c & -B_y & B_x & 0
\end{pmatrix}
$$

**Dual tensor** (replaces $\mathbf{E} \to \mathbf{B}$, $\mathbf{B} \to -\mathbf{E}$):

$$
\tilde{F}^{\mu\nu} = \frac12 \epsilon^{\mu\nu\rho\sigma} F_{\rho\sigma}
$$

### 4.2 麦克斯韦方程的张量形式 (Tensor Form of Maxwell's Equations) / 4.2 麦克斯韦方程的张量形式 (Tensor Form of Maxwell's Equations)

$$
\partial_\mu F^{\mu\nu} = \mu_0 J^\nu
\quad\text{(inhomogeneous, with sources)}
$$

$$
\partial_\mu \tilde{F}^{\mu\nu} = 0
\quad\text{(homogeneous, no sources)}
$$

These compact forms contain all four Maxwell equations:

- $\nu = 0$: $\nabla \cdot \mathbf{E} = \rho/\epsilon_0$
- $\nu = i$: $\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \epsilon_0 \partial\mathbf{E}/\partial t$
- $\tilde{F}$: $\nabla \cdot \mathbf{B} = 0$, $\nabla \times \mathbf{E} = -\partial\mathbf{B}/\partial t$

### 4.3 洛伦兹力 (Lorentz Force) / 4.3 洛伦兹力 (Lorentz Force)

**4-force**: $\displaystyle \frac{dp^\mu}{d\tau} = q F^{\mu\nu} U_\nu$

**3-force**: $\displaystyle \frac{d\mathbf{p}}{dt} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})$

---

## 5. 电磁场的变换 (Field Transformations) / 电磁场的变换 (Field Transformations)

### 5.1 场的洛伦兹变换 (Lorentz Transform of E and B) / 5.1 场的洛伦兹变换 (Lorentz Transform of E与B)

For a boost with velocity $\mathbf{v}$ (parallel: $\parallel$, perpendicular: $\perp$):

$$
\mathbf{E}'_\parallel = \mathbf{E}_\parallel, \quad \mathbf{E}'_\perp = \gamma(\mathbf{E}_\perp + \mathbf{v} \times \mathbf{B}_\perp)
$$
$$
\mathbf{B}'_\parallel = \mathbf{B}_\parallel, \quad \mathbf{B}'_\perp = \gamma(\mathbf{B}_\perp - \frac{\mathbf{v}}{c^2} \times \mathbf{E}_\perp)
$$

**Physical interpretation**: An observer moving through electric and magnetic fields sees a mixture — what is "pure E" in one frame becomes "E + B" in another.

### 5.2 洛伦兹不变量 (Lorentz Invariants) / 5.2 洛伦兹不变量 (Lorentz Invariants)

$$
\mathcal{I}_1 = F_{\mu\nu}F^{\mu\nu} = 2\left(B^2 - \frac{E^2}{c^2}\right)
$$
$$
\mathcal{I}_2 = \tilde{F}_{\mu\nu}F^{\mu\nu} = -\frac{4}{c} \mathbf{E} \cdot \mathbf{B}
$$

Same value in all inertial frames. These classify the field:

- $\mathbf{E} \cdot \mathbf{B} = 0$, $E^2 > c^2 B^2$: a frame exists where $\mathbf{B}=0$
- $\mathbf{E} \cdot \mathbf{B} = 0$, $E^2 < c^2 B^2$: a frame exists where $\mathbf{E}=0$
- $\mathbf{E} \cdot \mathbf{B} \neq 0$: no frame can nullify both fields

---

## 6. 电磁场的拉格朗日量 (Lagrangian Formulation) / 电磁场的拉格朗日量 (Lagrangian Formulation)

**Lagrangian density**:

$$
\mathcal{L} = -\frac{1}{4\mu_0} F_{\mu\nu}F^{\mu\nu} - J_\mu A^\mu
$$

**Euler-Lagrange equation**:

$$
\partial_\mu \frac{\partial\mathcal{L}}{\partial(\partial_\mu A_\nu)} - \frac{\partial\mathcal{L}}{\partial A_\nu} = 0
$$

yields $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$.

**Energy-momentum tensor**:

$$
T^{\mu\nu} = \frac{1}{\mu_0} \left( F^{\mu\alpha} F^\nu_{\ \alpha} + \frac14 g^{\mu\nu} F_{\alpha\beta}F^{\alpha\beta} \right)
$$

- $T^{00}$ = energy density $u = \frac12(\epsilon_0 E^2 + B^2/\mu_0)$
- $T^{0i}$ = momentum density / Poynting vector component

---

## 7. 相对论多普勒效应 (Relativistic Doppler Effect) / 相对论多普勒效应 (Relativistic Doppler Effect)

For light emitted at frequency $\omega_0$ and observed at $\omega$:

$$
\omega = \omega_0 \gamma (1 - \beta\cos\theta_0)
$$

where $\theta_0$ is the emission angle in the source rest frame.

**Special cases**:

- **Longitudinal** ($\theta_0 = 0$): $\omega = \omega_0 \sqrt{\frac{1-\beta}{1+\beta}}$ (redshift for recession)
- **Transverse** ($\theta_0 = \pi/2$): $\omega = \omega_0 / \gamma$ (purely relativistic, no classical analog)

**Relativistic aberration**:

$$
\cos\theta = \frac{\cos\theta_0 - \beta}{1 - \beta\cos\theta_0}
$$

---

## 8. 相对性原理与光行差 (Relativity and Aberration) / 相对性原理与光行差 (Relativity与Aberration)

### 8.1 光行差 (Stellar Aberration) / 8.1 光行差 (Stellar Aberration)

The apparent direction of starlight changes due to Earth's motion:

$$
\tan\theta = \frac{\sin\theta_0}{\gamma(\cos\theta_0 + \beta)}
$$

### 8.2 头灯效应 (Headlight Effect) / 8.2 头灯效应 (Headlight Effect)

A moving isotropic emitter appears **forward-focused** in the lab frame. Angular distribution:

$$
\frac{dP}{d\Omega} = \frac{1}{\gamma^2(1 - \beta\cos\theta)^2} \frac{dP_0}{d\Omega_0}
$$

This is why relativistic jets appear narrow.

---

## 9. 闵可夫斯基时空图 (Minkowski Diagrams) / 闵可夫斯基时空图 (Minkowski Diagrams)

Key features of spacetime:
- **Light cone**: $x^2 + y^2 + z^2 = c^2 t^2$
  - Inside → timelike (causally connected)
  - On → lightlike (null)
  - Outside → spacelike (cannot be causally connected)
- **World lines**: paths of particles through spacetime
- **Simultaneity**: depends on the observer's frame
- **Time dilation**: $\Delta t = \gamma \Delta \tau$
- **Length contraction**: $L = L_0/\gamma$

---

## 10. 重要公式速查 (Key Formulas Cheat Sheet) / 重要公式速查 (Key Formulas Cheat Sheet)

| Concept | Formula |
|---------|---------|
| Lorentz factor | $\gamma = 1/\sqrt{1-v^2/c^2}$ |
| Velocity addition | $u' = \frac{u - v}{1 - uv/c^2}$ |
| 4-momentum | $p^\mu = (E/c, \mathbf{p})$ |
| $E^2 = p^2c^2 + m^2c^4$ | Energy-momentum invariant |
| Field tensor | $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$ |
| Maxwell tensor | $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$ |
| E/B transform | $\mathbf{E}'_\perp = \gamma(\mathbf{E} + \mathbf{v} \times \mathbf{B})_\perp$ |
| Invariants | $E^2 - c^2 B^2$, $\mathbf{E} \cdot \mathbf{B}$ |
| Doppler | $\omega = \omega_0 \gamma (1 - \beta\cos\theta_0)$ |

---

## 11. 物理直觉 (Physical Intuition) / 物理直觉 (Physical Intuition)

1. **E and B are frame-dependent manifestations of the same field**
2. **$c$ is the universal speed limit** — only massless particles travel at $c$
3. **Mass-energy equivalence**: $E = mc^2$ is contained in $E^2 = p^2c^2 + m^2c^4$ (rest frame: $p=0$)
4. **Electromagnetism is already relativistic** — Maxwell's equations are Lorentz covariant; only Newtonian mechanics had to be modified
5. **Relativistic beaming**: moving sources appear brighter and more concentrated forward
6. **No "absolute simultaneity"** — temporal order of spacelike-separated events is observer-dependent

---

## 12. 应用 (Applications) / 应用 (Applications)

- **Particle accelerators**: relativistic kinematics of beams
- **GPS**: relativistic corrections (SR + GR) essential for accuracy
- **Astrophysics**: relativistic jets, pulsars, gamma-ray bursts
- **Nuclear physics**: $E=mc^2$, pair production
- **Synchrotron radiation**: relativistic electrons in magnetic fields
- **Quantum electrodynamics (QED)**: fully relativistic field theory

---

## References / 参考文献

- Jackson §11.1–§11.13
- Einstein, *On the Electrodynamics of Moving Bodies* (1905)
- Rindler, *Introduction to Special Relativity*
- French, *Special Relativity*
- Misner, Thorne & Wheeler, *Gravitation* (GR extensions)
