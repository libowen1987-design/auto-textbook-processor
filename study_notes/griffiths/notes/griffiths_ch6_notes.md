---
chapter: 6
title: Magnetic Fields in Matter
source: Griffiths, Introduction to Electrodynamics, 4th Edition
pages: 265-314
---

# Chapter 6: Magnetic Fields in Matter

## 6.1 Magnetization (pp. 265-273)

### 6.1.1 Diamagnets, Paramagnets, Ferromagnets

All magnetic phenomena arise from moving charges (orbital and spin motion of electrons). Materials respond to magnetic fields in three ways:
- **Paramagnets** (Al, Na, Pt): magnetization $\mathbf{M}$ parallel to $\mathbf{B}$ ($\chi_m > 0$)
- **Diamagnets** (Cu, Bi, H$_2$O): magnetization $\mathbf{M}$ antiparallel to $\mathbf{B}$ ($\chi_m < 0$)
- **Ferromagnets** (Fe, Ni, Co): retain magnetization after external field removed

### 6.1.2 Torques and Forces on Magnetic Dipoles

**Torque on a magnetic dipole** in uniform field:

$$\mathbf{N} = \mathbf{m} \times \mathbf{B}$$

(6.1)

Identical in form to electric case $\mathbf{N} = \mathbf{p} \times \mathbf{E}$ (4.4). This torque tends to align $\mathbf{m}$ parallel to $\mathbf{B}$, causing paramagnetism.

**Force on a dipole** in nonuniform field:

$$\mathbf{F} = \nabla(\mathbf{m} \cdot \mathbf{B})$$

(6.3)

**Gilbert model vs. Ampère model:** Magnetic dipoles are **current loops** (Ampère model), not separated magnetic monopoles (Gilbert model). Despite this, the far-field formulas are identical.

### 6.1.3 Effect of Magnetic Field on Atomic Orbits

When a magnetic field is turned on, orbital electrons speed up or slow down, producing a change in the orbital dipole moment:

$$\Delta \mathbf{m} = -\frac{e^2 R^2}{4m_e}\mathbf{B}$$

(6.8)

This change is always **opposite** to $\mathbf{B}$, explaining **diamagnetism** (a universal but weak effect).

### 6.1.4 Magnetization

**Magnetization** $\mathbf{M}$ ≡ dipole moment per unit volume (6.9).

**物理直觉：** 磁化就是使微观磁偶极矩的排列产生净余量。顺磁：已有的永久偶极矩被磁场力矩对齐；抗磁：轨道运动受磁场扰动产生诱导偶极矩（总是反向）。铁磁则是量子力学交换相互作用导致的自发有序。

---

## 6.2 Field of a Magnetized Object (pp. 274-279)

### 6.2.1 Bound Currents

The vector potential of a magnetized object with magnetization $\mathbf{M}$:

$$\mathbf{A}(\mathbf{r}) = \frac{\mu_0}{4\pi}\int \frac{\mathbf{M}(\mathbf{r}')\times\hat{\mathscr{r}}}{\mathscr{r}^2}\,d\tau'$$

(6.11)

Using $\nabla'(1/\mathscr{r}) = \hat{\mathscr{r}}/\mathscr{r}^2$ and integration by parts:

$$\mathbf{A}(\mathbf{r}) = \frac{\mu_0}{4\pi}\int_{\mathcal{V}} \frac{\mathbf{J}_b(\mathbf{r}')}{\mathscr{r}}\,d\tau' + \frac{\mu_0}{4\pi}\oint_S \frac{\mathbf{K}_b(\mathbf{r}')}{\mathscr{r}}\,da'$$

(6.15)

where the **bound currents** are:

$$\boxed{\mathbf{J}_b = \nabla \times \mathbf{M}}\quad\text{(volume bound current)}$$

(6.13)

$$\boxed{\mathbf{K}_b = \mathbf{M} \times \hat{\mathbf{n}}}\quad\text{(surface bound current)}$$

(6.14)

**Example 6.1** (p. 275): Uniformly magnetized sphere ($\mathbf{M}=M\hat{\mathbf{z}}$). $\mathbf{J}_b=0$,
$\mathbf{K}_b = M\sin\theta\,\hat{\boldsymbol{\phi}}$.

Inside: $\displaystyle \mathbf{B} = \frac{2}{3}\mu_0\mathbf{M}$ (uniform!) (6.16)

Outside: field of perfect dipole $\mathbf{m} = \frac{4}{3}\pi R^3\mathbf{M}$.

Note contrast with electric case: polarized sphere gives $\mathbf{E}_{\text{in}} = -\frac{1}{3\epsilon_0}\mathbf{P}$.

**物理直觉：** 磁化物体可以用等效的束缚电流代替。$\mathbf{K}_b = \mathbf{M} \times \hat{\mathbf{n}}$ 意味着切线方向的磁化会在表面产生电流——类似在磁铁表面"滚动的"环形电流。

---

## 6.3 The Auxiliary Field H (pp. 279-284)

### 6.3.1 Ampère's Law in Magnetized Materials

Total current: $\mathbf{J} = \mathbf{J}_f + \mathbf{J}_b = \mathbf{J}_f + \nabla\times\mathbf{M}$

Ampère's law: $\frac{1}{\mu_0}\nabla\times\mathbf{B} = \mathbf{J}_f + \nabla\times\mathbf{M}$

Define the **auxiliary field**:

$$\boxed{\mathbf{H} \equiv \frac{1}{\mu_0}\mathbf{B} - \mathbf{M}}$$

(6.18)

Then Ampère's law becomes:

$$\nabla\times\mathbf{H} = \mathbf{J}_f \quad\Leftrightarrow\quad \oint \mathbf{H}\cdot d\mathbf{l} = I_{f,\text{enc}}$$

(6.19-6.20)

**Example 6.2** (p. 280): Copper rod (radius $R$, free current $I$). By symmetry:

$$\mathbf{H} = \begin{cases} \frac{I}{2\pi R^2}s\,\hat{\boldsymbol{\phi}} & s\le R \\ \frac{I}{2\pi s}\hat{\boldsymbol{\phi}} & s\ge R \end{cases}$$

(6.21-6.22)

**Warning:** Unlike $\mathbf{B}$, $\nabla\cdot\mathbf{H} = -\nabla\cdot\mathbf{M} \neq 0$ in general. So $\mathbf{H}$ is **not** determined by free current alone unless symmetry dictates it. As with $\mathbf{D}$, symmetry (spherical, cylindrical, planar) is the key.

### 6.3.2 Boundary Conditions

| Quantity | Perpendicular | Parallel |
|----------|--------------|----------|
| $\mathbf{B}$ | $B_\perp^{\text{above}} = B_\perp^{\text{below}}$ (6.26) | $B_\parallel^{\text{above}} - B_\parallel^{\text{below}} = \mu_0(\mathbf{K}\times\hat{\mathbf{n}})$ (6.27) |
| $\mathbf{H}$ | $H_\perp^{\text{above}} - H_\perp^{\text{below}} = -(M_\perp^{\text{above}}-M_\perp^{\text{below}})$ (6.24) | $H_\parallel^{\text{above}} - H_\parallel^{\text{below}} = \mathbf{K}_f\times\hat{\mathbf{n}}$ (6.25) |

---

## 6.4 Linear and Nonlinear Media (pp. 284-314)

### 6.4.1 Magnetic Susceptibility and Permeability

For **linear media**:

$$\mathbf{M} = \chi_m\mathbf{H}$$

(6.29)

$\chi_m$ = **magnetic susceptibility** (dimensionless). Positive for paramagnets, negative for diamagnets, typically $\sim 10^{-5}$.

| Material | $\chi_m$ | Type |
|----------|---------|------|
| Bismuth | $-1.7\times10^{-4}$ | Diamagnetic |
| Copper | $-9.7\times10^{-6}$ | Diamagnetic |
| Water | $-9.0\times10^{-6}$ | Diamagnetic |
| Aluminum | $2.2\times10^{-5}$ | Paramagnetic |
| Platinum | $2.7\times10^{-4}$ | Paramagnetic |
| Gadolinium | $4.8\times10^{-1}$ | Paramagnetic (strong) |

Then:

$$\mathbf{B} = \mu_0(1+\chi_m)\mathbf{H} \equiv \mu\mathbf{H}$$

(6.31-6.32)

where $\mu \equiv \mu_0(1+\chi_m)$ is the **permeability**.

In homogeneous linear media: $\mathbf{J}_b = \chi_m\mathbf{J}_f$ (6.33). If no free current flows through the material, all bound current is on the surface.

**Example 6.3** (p. 286): Solenoid ($n$ turns/m, current $I$) filled with linear material of susceptibility $\chi_m$. By symmetry:

$$H = nI \quad\Rightarrow\quad B = \mu_0(1+\chi_m)nI$$

Paramagnetic material enhances $B$; diamagnetic reduces it.

**Sphere in uniform field:** Using separation of variables on the scalar potential $W$ (where $\mathbf{H} = -\nabla W$):

$$\mathbf{B}_{\text{in}} = \frac{3\mu_r}{\mu_r+2}\mathbf{B}_0$$

For $\mu_r \gg 1$ (soft iron), $\mathbf{B}_{\text{in}} \approx 3\mathbf{B}_0$.

### 6.4.2 Ferromagnetism

Ferromagnets have **spontaneous magnetization** due to quantum mechanical exchange interaction — neighboring dipoles align without any external field.

Key features:
- **Domains** ($\sim$μm scale): regions of uniform magnetization, randomly oriented in unmagnetized iron
- **Domain wall motion**: external fields shift domain boundaries — favorable domains grow
- **Hysteresis**: path of $M$ vs $H$ is not reversible; the magnetization lags behind the applied field

Hysteresis loop:
$$H \uparrow \rightarrow M \uparrow \text{(reaches saturation)} \rightarrow H \downarrow \rightarrow M \text{(retains residual magnetization)} \rightarrow H \text{(reverse)} \rightarrow M \downarrow \rightarrow -M \text{(saturation)} \rightarrow \text{cycle closes}$$

**Material classifications:**
- **Soft ferromagnets** (Fe-Si): narrow hysteresis, easily magnetized/demagnetized
- **Hard ferromagnets** (Alnico, ferrites): wide hysteresis, good permanent magnets

---

### Chapter Summary: Key Formula Table

| Concept | Formula | Eq. |
|---------|---------|-----|
| Bound currents | $\mathbf{J}_b = \nabla\times\mathbf{M}$, $\mathbf{K}_b = \mathbf{M}\times\hat{\mathbf{n}}$ | (6.13-6.14) |
| Auxiliary field H | $\mathbf{H} = \frac{1}{\mu_0}\mathbf{B} - \mathbf{M}$ | (6.18) |
| Ampère's law (H) | $\oint\mathbf{H}\cdot d\mathbf{l} = I_{f,\text{enc}}$ | (6.20) |
| Linear medium | $\mathbf{M} = \chi_m\mathbf{H}$, $\mathbf{B} = \mu\mathbf{H}$ | (6.29, 6.31) |
| Permeability | $\mu = \mu_0(1+\chi_m)$ | (6.32) |
| Uniformly magnetized sphere | $\mathbf{B}_{\text{in}} = \frac{2}{3}\mu_0\mathbf{M}$ | (6.16) |

**物理直觉（全章回顾）：** 磁化导致束缚电流，$\mathbf{H}$ 场让我们用自由电流来应用 Ampère 定律。线性介质中 $\mathbf{B} = \mu\mathbf{H}$，类比 $\mathbf{D} = \epsilon\mathbf{E}$。铁磁体中的畴结构和磁滞回线是工程应用的基石——变压器用软磁材料（窄回线），永磁体用硬磁材料（宽回线）。
