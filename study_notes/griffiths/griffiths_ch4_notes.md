---
chapter: 4
title: Electric Fields in Matter
source: Griffiths, Introduction to Electrodynamics, 4th Edition
pages: 167-228
---

# Chapter 4: Electric Fields in Matter

## 4.1 Polarization (pp. 167-172)

### 4.1.1 Dielectrics

Matter broadly divides into two classes: **conductors** (free charges can roam) and **insulators** or **dielectrics** (charges bound to atoms/molecules). In dielectrics, an external electric field causes microscopic charge displacements that accumulate to produce macroscopic effects.

### 4.1.2 Induced Dipoles

A neutral atom placed in an external field $\mathbf{E}$ becomes polarized: the nucleus is pushed one way, the electron cloud the opposite way. The resulting **induced dipole moment** is proportional to the field (for weak fields):

$$\mathbf{p} = \alpha \mathbf{E}$$

(4.1)

where $\alpha$ is the **atomic polarizability**.

**Example 4.1** (p. 168): Primitive atomic model — point nucleus $+q$ surrounded by uniform spherical electron cloud of radius $a$. In external field $\mathbf{E}$, the nucleus displaces by $d$. Equilibrium: external field equals the field of the electron cloud at distance $d$:

$$E = \frac{1}{4\pi\epsilon_0}\frac{qd}{a^3} \quad\Rightarrow\quad p = qd = (4\pi\epsilon_0 a^3)E$$

Thus $\alpha = 4\pi\epsilon_0 a^3$ (4.2). Accurate to within a factor of ~4 for simple atoms.

For anisotropic molecules, polarizability is a tensor (Eq. 4.3). For $\text{CO}_2$, $\alpha_\parallel \neq \alpha_\perp$.

**物理直觉：** 原子极化率正比于原子体积（$\alpha \propto a^3$）。越大的原子越容易被极化，因为其外层电子离原子核更远，受到的束缚更弱。

### 4.1.3 Alignment of Polar Molecules

Some molecules have **permanent dipole moments** (e.g., H$_2$O with $p = 6.1\times 10^{-30}$ C·m). In a uniform field, a permanent dipole experiences a **torque** but no net force:

$$\mathbf{N} = \mathbf{p} \times \mathbf{E}$$

(4.4)

This torque tends to align the dipole with the field.

In a **nonuniform field**, a dipole also experiences a net force:

$$\mathbf{F} = (\mathbf{p}\cdot\nabla)\mathbf{E}$$

(4.5)

**Energy of a dipole:** $U = -\mathbf{p}\cdot\mathbf{E}$ (4.6)

**Interaction energy of two dipoles:**

$$U = \frac{1}{4\pi\epsilon_0}\frac{1}{r^3}[\mathbf{p}_1\cdot\mathbf{p}_2 - 3(\mathbf{p}_1\cdot\hat{\mathbf{r}})(\mathbf{p}_2\cdot\hat{\mathbf{r}})]$$

(4.7)

### 4.1.4 Polarization

**Polarization $\mathbf{P}$** is the dipole moment per unit volume. Two mechanisms produce it:
1. **Induced dipoles** in nonpolar molecules (stretching).
2. **Alignment** of permanent dipoles in polar molecules (rotation), competing with thermal agitation.

**物理直觉：** 宏观极化是数十亿微观偶极子的统计平均。即使每个分子只发生原子尺度的位移（~$10^{-14}$ m），累积效应也可产生可观测的宏观电场。

---

## 4.2 The Field of a Polarized Object (pp. 173-181)

### 4.2.1 Bound Charges

For a polarized object with given $\mathbf{P}(\mathbf{r}')$, the potential is:

$$V(\mathbf{r}) = \frac{1}{4\pi\epsilon_0}\int_{\mathcal{V}} \frac{\mathbf{P}(\mathbf{r}')\cdot\hat{\mathscr{r}}}{\mathscr{r}^2}\,d\tau'$$

(4.9)

Using $\nabla'(1/\mathscr{r}) = \hat{\mathscr{r}}/\mathscr{r}^2$ and integration by parts:

$$V(\mathbf{r}) = \frac{1}{4\pi\epsilon_0}\oint_S \frac{1}{\mathscr{r}}\mathbf{P}\cdot d\mathbf{a}' - \frac{1}{4\pi\epsilon_0}\int_{\mathcal{V}} \frac{1}{\mathscr{r}}(\nabla'\cdot\mathbf{P})\,d\tau'$$

(4.10)

This is the potential of a **bound charge distribution**:

$$\boxed{\sigma_b = \mathbf{P}\cdot\hat{\mathbf{n}}}\quad\text{(surface bound charge density)}$$

(4.11)

$$\boxed{\rho_b = -\nabla\cdot\mathbf{P}}\quad\text{(volume bound charge density)}$$

(4.12)

Thus the field of a polarized object equals that produced by its bound charges.

**Example 4.2** (p. 174): Uniformly polarized sphere ($\mathbf{P} = P\hat{\mathbf{z}}$). Since $\mathbf{P}$ is constant, $\rho_b = 0$; $\sigma_b = P\cos\theta$.

From Ex. 3.9, the potential is:

$$V(r,\theta) = \begin{cases} \frac{P}{3\epsilon_0}r\cos\theta & r \le R \\ \frac{P}{3\epsilon_0}\frac{R^3}{r^2}\cos\theta & r \ge R \end{cases}$$

Inside: $\displaystyle \mathbf{E} = -\frac{1}{3\epsilon_0}\mathbf{P}$ (uniform!) (4.14)

Outside: field of a perfect dipole $\displaystyle \mathbf{p} = \frac{4}{3}\pi R^3\mathbf{P}$ (4.16)

### 4.2.2 Physical Interpretation

Polarization shifts positive charge slightly in one direction, negative in the other. Along a chain of dipoles, heads cancel tails in the interior, leaving net charge at surfaces. Diverging $\mathbf{P}$ produces volume bound charge (Fig. 4.14).

### 4.2.3 Macroscopic Field Inside a Dielectric

The true microscopic field inside matter is wildly complicated. The **macroscopic field** is the average over regions large enough to contain many molecules. Remarkably, the average field produced by the dipoles inside a sphere is $-\frac{1}{3\epsilon_0}\mathbf{P}$, and this precisely compensates for the error in using the dipole formula at interior points. The macroscopic field is correctly given by Eq. 4.9.

**物理直觉：** 边界上的 $\sigma_b = \mathbf{P}\cdot\hat{\mathbf{n}}$ 反映了极化如何"露出头"——就像一盒笔，所有笔尖朝上，则盒子上表面有正电荷（笔尖），下表面有负电荷（笔尾）。

---

## 4.3 The Electric Displacement (pp. 181-185)

### 4.3.1 Gauss's Law in Dielectrics

Total charge density: $\rho = \rho_f + \rho_b = \rho_f - \nabla\cdot\mathbf{P}$

Gauss's law: $\epsilon_0\nabla\cdot\mathbf{E} = \rho = \rho_f - \nabla\cdot\mathbf{P}$

Rearrange: $\nabla\cdot(\epsilon_0\mathbf{E} + \mathbf{P}) = \rho_f$

Define the **electric displacement**:

$$\boxed{\mathbf{D} \equiv \epsilon_0\mathbf{E} + \mathbf{P}}$$

(4.21)

Then Gauss's law becomes:

$$\nabla\cdot\mathbf{D} = \rho_f \quad\text{(differential)}$$

(4.22)

$$\oint \mathbf{D}\cdot d\mathbf{a} = Q_{f,\text{enc}} \quad\text{(integral)}$$

(4.23)

**Example 4.4** (p. 182): Long wire with line charge $\lambda$ surrounded by rubber insulation (radius $a$). By cylindrical symmetry:

$$D = \frac{\lambda}{2\pi s}\hat{\mathbf{s}}$$

Inside the rubber, $\mathbf{E}$ cannot be determined without knowing $\mathbf{P}$; outside, $\mathbf{P}=0$ so $\mathbf{E} = \mathbf{D}/\epsilon_0$.

### 4.3.2 A Deceptive Parallel

**Warning:** $\nabla\times\mathbf{D} = \nabla\times\mathbf{P}$, which is not generally zero. Therefore $\mathbf{D}$ cannot always be derived from free charge alone. D is **not** analogous to $\mathbf{E}$ for "Coulomb's law" purposes.

**Rule of thumb:** When the problem has sufficient symmetry (spherical, cylindrical, planar), you can get $\mathbf{D}$ directly from $\oint\mathbf{D}\cdot d\mathbf{a} = Q_{f,\text{enc}}$.

### 4.3.3 Boundary Conditions

| Quantity | Perpendicular component | Parallel component |
|----------|------------------------|---------------------|
| $\mathbf{D}$ | $D_\perp^{\text{above}} - D_\perp^{\text{below}} = \sigma_f$ (4.26) | $D_\parallel^{\text{above}} - D_\parallel^{\text{below}} = P_\parallel^{\text{above}} - P_\parallel^{\text{below}}$ (4.27) |
| $\mathbf{E}$ | $E_\perp^{\text{above}} - E_\perp^{\text{below}} = \frac{1}{\epsilon_0}\sigma$ (4.28) | $E_\parallel^{\text{above}} = E_\parallel^{\text{below}}$ (4.29) |

---

## 4.4 Linear Dielectrics (pp. 185-228)

### 4.4.1 Susceptibility, Permittivity, Dielectric Constant

For many materials (linear dielectrics), polarization is proportional to the field:

$$\boxed{\mathbf{P} = \epsilon_0\chi_e\mathbf{E}}$$

(4.30)

where $\chi_e$ is the **electric susceptibility** (dimensionless).

Then:

$$\mathbf{D} = \epsilon_0\mathbf{E} + \mathbf{P} = \epsilon_0(1+\chi_e)\mathbf{E} \equiv \epsilon\mathbf{E}$$

(4.31-4.32)

where $\epsilon \equiv \epsilon_0(1+\chi_e)$ is the **permittivity**, and $\epsilon_r \equiv 1+\chi_e = \epsilon/\epsilon_0$ is the **dielectric constant**.

| Material | $\epsilon_r$ | Material | $\epsilon_r$ |
|----------|-------------|----------|-------------|
| Vacuum | 1 | Diamond | 5.7-5.9 |
| Air (dry) | 1.000536 | Silicon | 11.7 |
| Water | 80.1 | Methanol | 33.0 |
| Ice ($-30^\circ$C) | 104 | KTaNbO$_3$ ($0^\circ$C) | 34,000 |

**When all space is filled with a homogeneous linear dielectric:**

$$\mathbf{E} = \frac{1}{\epsilon_r}\mathbf{E}_{\text{vac}}$$

(4.35)

The field is simply reduced by a factor $1/\epsilon_r$, because the polarization partially "shields" free charges.

**Example 4.5** (p. 187): Metal sphere (radius $a$, charge $Q$) surrounded by linear dielectric ($\epsilon$) out to $b$. By symmetry, $\mathbf{D} = (Q/4\pi r^2)\hat{\mathbf{r}}$ everywhere. Then $\mathbf{E} = \mathbf{D}/\epsilon$ in the dielectric, $\mathbf{E} = \mathbf{D}/\epsilon_0$ outside.

**Example 4.6** (p. 190): Parallel-plate capacitor filled with dielectric. $C = \epsilon_r C_{\text{vac}}$ (4.37). This is why dielectrics are used to increase capacitance.

### 4.4.2 Boundary Value Problems

In a homogeneous linear dielectric, $\rho_b = -(\chi_e/(1+\chi_e))\rho_f$ (4.39). If no free charge is embedded in the dielectric, $\rho = 0$ and Laplace's equation holds.

**Boundary conditions at a dielectric interface** (no free surface charge):

$$V_{\text{above}} = V_{\text{below}}$$

(4.42)

$$\epsilon_{\text{above}}\frac{\partial V_{\text{above}}}{\partial n} = \epsilon_{\text{below}}\frac{\partial V_{\text{below}}}{\partial n}$$

(4.41)

**Example 4.7** (p. 193): Dielectric sphere in uniform external field $\mathbf{E}_0$.

Boundary conditions at $r=R$: (i) $V_{\text{in}} = V_{\text{out}}$, (ii) $\epsilon\,\partial V_{\text{in}}/\partial r = \epsilon_0\,\partial V_{\text{out}}/\partial r$.

Only $l=1$ term contributes:

$$V_{\text{in}}(r,\theta) = -\frac{3E_0}{\epsilon_r+2}r\cos\theta$$

Field inside is **uniform**:

$$\boxed{\mathbf{E} = \frac{3}{\epsilon_r+2}\mathbf{E}_0}$$

(4.49)

For $\epsilon_r \to \infty$ (conductor limit), $\mathbf{E} \to 0$ (field cancels inside). For $\epsilon_r \to 1$ (vacuum), $\mathbf{E} \to \mathbf{E}_0$.

**Example 4.8** (p. 194): Point charge $q$ above a linear dielectric half-space ($z<0$, susceptibility $\chi_e$). Solution by images: an image charge $q_b = -[\chi_e/(\chi_e+2)]q$ at $(0,0,-d)$ works for $z>0$. The force on $q$:

$$\mathbf{F} = -\frac{1}{4\pi\epsilon_0}\frac{\chi_e}{\chi_e+2}\frac{q^2}{4d^2}\hat{\mathbf{z}}$$

(4.54)

For $\chi_e\to\infty$ (conductor limit), $F \to -q^2/(4\pi\epsilon_0\cdot 4d^2)$, recovering the grounded plane result.

### 4.4.3 Energy in Dielectric Systems

Energy stored in the electric field in the presence of linear dielectrics:

$$\boxed{W = \frac{1}{2}\int \mathbf{D}\cdot\mathbf{E}\,d\tau}$$

(4.58)

Note: This differs from $W = (\epsilon_0/2)\int E^2 d\tau$ because it includes the "spring energy" of polarizing the molecules.

**Example 4.9** (p. 199): Sphere (radius $R$, dielectric constant $\epsilon_r$) with uniform embedded free charge $\rho_f$. The total energy using Eq. 4.58:

$$W = \frac{2\pi}{9\epsilon_0}\rho_f^2 R^5\left(\frac{1}{5\epsilon_r} + 1\right)$$

The purely electrostatic energy (excluding molecular spring energy) is:

$$W_1 = \frac{2\pi}{9\epsilon_0}\rho_f^2 R^5\left(\frac{1}{5\epsilon_r^2} + 1\right)$$

### 4.4.4 Forces on Dielectrics (p. 204-209)

When a dielectric is partially inserted into a capacitor, a force acts to pull it in. For a parallel-plate capacitor with dielectric partially inserted (distance $x$):

$$F = \frac{(a-x)}{2d}(\epsilon - \epsilon_0)E^2$$

The force can be found from $F = -\partial W/\partial x$ (keeping charge or potential constant).

---

### Chapter Summary: Key Formula Table

| Concept | Formula | Eq. |
|---------|---------|-----|
| Atomic polarizability | $\mathbf{p} = \alpha\mathbf{E}$ | (4.1) |
| Bound charge densities | $\sigma_b = \mathbf{P}\cdot\hat{\mathbf{n}}$, $\rho_b = -\nabla\cdot\mathbf{P}$ | (4.11-4.12) |
| Electric displacement | $\mathbf{D} = \epsilon_0\mathbf{E} + \mathbf{P}$ | (4.21) |
| Gauss's law in dielectrics | $\oint\mathbf{D}\cdot d\mathbf{a} = Q_{f,\text{enc}}$ | (4.23) |
| Linear dielectric | $\mathbf{P} = \epsilon_0\chi_e\mathbf{E}$ | (4.30) |
| Permittivity | $\epsilon = \epsilon_0(1+\chi_e) = \epsilon_0\epsilon_r$ | (4.33) |
| Uniform field in dielectric sphere | $\mathbf{E} = \frac{3}{\epsilon_r+2}\mathbf{E}_0$ | (4.49) |
| Energy in dielectrics | $W = \frac{1}{2}\int\mathbf{D}\cdot\mathbf{E}\,d\tau$ | (4.58) |
| Boundary condition (normal D) | $D_\perp^{\text{above}} - D_\perp^{\text{below}} = \sigma_f$ | (4.26) |
| Boundary condition (tangential E) | $E_\parallel^{\text{above}} = E_\parallel^{\text{below}}$ | (4.29) |

**物理直觉（全章回顾）：** 电介质中，外加电场使原子/分子极化，形成宏观极化 $\mathbf{P}$。极化产生的束缚电荷可以像自由电荷一样计算电场。引入 $\mathbf{D}$ 场后，Gauss 定律只涉及自由电荷——这是我们能控制的量。对于线性电介质，场强被缩小 $1/\epsilon_r$，因为束缚电荷部分抵消了自由电荷产生的场。能量公式 $W = \frac{1}{2}\int\mathbf{D}\cdot\mathbf{E}\,d\tau$ 包含了极化所需的分子"弹簧能"，而 $\frac{\epsilon_0}{2}\int E^2 d\tau$ 只包含纯粹的电场能。
