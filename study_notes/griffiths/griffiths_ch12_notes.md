---
chapter: 12
title: Electrodynamics and Relativity
source: Griffiths, Introduction to Electrodynamics, 4th Edition
pages: 502-593
---

# Chapter 12: Electrodynamics and Relativity

## 12.1 Special Theory of Relativity (pp. 502-532)

### 12.1.1 Einstein's Postulates

1. **Principle of relativity:** Laws of physics are the same in all inertial frames.
2. **Universal speed of light:** $c$ is the same for all inertial observers.

These resolve the tension between the principle of relativity (Galileo) and Maxwell's equations (which predict $c = 1/\sqrt{\mu_0\epsilon_0}$). The Michelson-Morley experiment (1887) showed no ether wind — the speed of light is isotropic.

### 12.1.2 Lorentz Transformations

For $S$ and $\bar{S}$ with $\bar{S}$ moving at velocity $v$ along the $x$ axis:

$$\begin{aligned}
\bar{x} &= \gamma(x - vt), \quad \bar{y} = y, \quad \bar{z} = z \\
\bar{t} &= \gamma\left(t - \frac{v}{c^2}x\right)
\end{aligned}$$

(12.18)

where $\displaystyle \gamma \equiv \frac{1}{\sqrt{1 - v^2/c^2}}$.

**Inverse transformation:** swap primes and replace $v \to -v$.

### 12.1.3 Relativistic Consequences

**Time dilation:** Moving clocks run slow: $\Delta t = \gamma\Delta\tau$ (12.19)

**Lorentz contraction:** Moving objects contract along the direction of motion: $L = L_0/\gamma$ (12.22)

**Velocity addition:** $\displaystyle \bar{u}_x = \frac{u_x - v}{1 - vu_x/c^2}$, $\bar{u}_y = \frac{u_y}{\gamma(1 - vu_x/c^2)}$ (12.45)

### 12.1.4 Four-Vectors and Metric

**Four-vectors:** $x^\mu = (ct, x, y, z)$ transforms via Lorentz matrix $\Lambda^\mu_\nu$:

$$\bar{x}^\mu = \Lambda^\mu_\nu x^\nu$$

(12.24)

**Minkowski metric:** $\eta_{\mu\nu} = \text{diag}(-1, 1, 1, 1)$ (sign depends on convention; Griffiths uses the signature appropriate to $ds^2 = -c^2dt^2 + dx^2 + dy^2 + dz^2$).

**Invariant interval:** $ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2$ (12.26)

- If $ds^2 < 0$: **timelike** (causal connection possible)
- If $ds^2 = 0$: **lightlike** (on the light cone)
- If $ds^2 > 0$: **spacelike** (no causal connection)

**Proper time:** $d\tau = \sqrt{1 - u^2/c^2}\,dt$ (12.37) — invariant.

---

## 12.2 Relativistic Mechanics (pp. 532-558)

### 12.2.1 Proper Velocity and 4-Velocity

$$\eta^\mu \equiv \frac{dx^\mu}{d\tau} = \gamma_u(c, \mathbf{u})$$

(12.41)

where $\gamma_u = 1/\sqrt{1-u^2/c^2}$. The invariant product:

$$\eta^\mu\eta_\mu = -c^2$$

### 12.2.2 Relativistic Energy and Momentum

**4-momentum:** $p^\mu \equiv m\eta^\mu = (E/c, \mathbf{p})$ (12.49)

where:

$$E = \gamma_u m c^2, \quad \mathbf{p} = \gamma_u m \mathbf{u}$$

(12.50-51)

**Energy-momentum relation:**

$$E^2 = p^2 c^2 + m^2 c^4$$

(12.55)

**Rest energy:** $E_0 = mc^2$ (12.54)

For $u \ll c$: $E = mc^2 + \frac{1}{2}mu^2 + \cdots$ (kinetic energy emerges naturally).

**Relativistic force:** $\mathbf{F} = \frac{d\mathbf{p}}{dt}$ (12.59), and the power equation:

$$\mathbf{F}\cdot\mathbf{u} = \frac{dE}{dt}$$

(12.60)

### 12.2.3 Relativistic Kinematics

**Energy and momentum are conserved** in all inertial frames. Particle decays and collisions use 4-momentum conservation:

$$p^\mu_{\text{initial}} = p^\mu_{\text{final}}$$

**Example:** Photon with $E = hf$, $p = E/c$. Compton scattering, pair production.

### 12.2.4 Relativistic Dynamics

**Minkowski force (4-force):**

$$K^\mu \equiv \frac{dp^\mu}{d\tau} = \gamma_u\left(\frac{\mathbf{F}\cdot\mathbf{u}}{c}, \mathbf{F}\right)$$

(12.65)

---

## 12.3 Relativistic Electrodynamics (pp. 558-593)

### 12.3.1 Magnetism as a Relativistic Phenomenon

A current-carrying wire that is neutral in the lab frame (equal positive and negative charge densities) appears charged in the rest frame of a moving test charge, due to **unequal Lorentz contraction** of the two line charges (Fig. 12.34). This explains magnetic forces as relativistic corrections to electrostatic forces.

### 12.3.2 Field Transformations

For $\bar{S}$ moving at velocity $\mathbf{v} = v\hat{\mathbf{x}}$:

$$\begin{aligned}
\bar{E}_x &= E_x, \quad \bar{B}_x = B_x \\
\bar{E}_y &= \gamma(E_y - vB_z), \quad \bar{B}_y = \gamma(B_y + vE_z/c^2) \\
\bar{E}_z &= \gamma(E_z + vB_y), \quad \bar{B}_z = \gamma(B_z - vE_y/c^2)
\end{aligned}$$

(12.109)

**Coordinate-free form:** For arbitrary $\mathbf{v}$:

$$\bar{\mathbf{E}}_\parallel = \mathbf{E}_\parallel, \quad \bar{\mathbf{B}}_\parallel = \mathbf{B}_\parallel$$

$$\bar{\mathbf{E}}_\perp = \gamma(\mathbf{E}_\perp + \mathbf{v}\times\mathbf{B}_\perp), \quad \bar{\mathbf{B}}_\perp = \gamma(\mathbf{B}_\perp - \frac{1}{c^2}\mathbf{v}\times\mathbf{E}_\perp)$$

(12.108)

**Invariants:**

$$E^2 - c^2B^2 = \text{invariant}$$

(12.119)

$$\mathbf{E}\cdot\mathbf{B} = \text{invariant}$$

(12.118)

### 12.3.3 Field Tensor

The electromagnetic fields can be combined into a single **electromagnetic field tensor** (a rank-2 antisymmetric 4-tensor):

$$F^{\mu\nu} = \begin{pmatrix}
0 & -E_x/c & -E_y/c & -E_z/c \\
E_x/c & 0 & -B_z & B_y \\
E_y/c & B_z & 0 & -B_x \\
E_z/c & -B_y & B_x & 0
\end{pmatrix}$$

(12.132)

**Maxwell's equations in tensor form:**

$$\partial_\mu F^{\mu\nu} = \mu_0 J^\nu \quad\text{(with sources)}$$

(12.134)

$$\partial_\mu G^{\mu\nu} = 0 \quad\text{(without sources)}$$

(12.136)

where $G^{\mu\nu}$ is the dual tensor ($\mathbf{E}\leftrightarrow c\mathbf{B}$), and $J^\nu = (c\rho, \mathbf{J})$ is the **4-current**.

The **Lorentz force law** in tensor form:

$$\frac{dp^\mu}{d\tau} = q F^{\mu\nu}\eta_\nu$$

(12.135)

### 12.3.4 Relativistic Potentials

The 4-potential: $A^\mu = (V/c, \mathbf{A})$ (12.139). The Lorenz gauge condition:

$$\partial_\mu A^\mu = 0$$

(12.142)

The field tensor from potentials:

$$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$$

(12.143)

Wave equation in Lorenz gauge:

$$\Box^2 A^\mu = -\mu_0 J^\mu$$

(12.145)

---

### Chapter Summary: Relativistic Electrodynamics

| Concept | 4-vector/Tensor | Components |
|---------|----------------|------------|
| Spacetime | $x^\mu$ | $(ct, x, y, z)$ |
| 4-velocity | $\eta^\mu$ | $\gamma_u(c, \mathbf{u})$ |
| 4-momentum | $p^\mu$ | $(E/c, \mathbf{p})$ |
| 4-current | $J^\mu$ | $(c\rho, \mathbf{J})$ |
| 4-potential | $A^\mu$ | $(V/c, \mathbf{A})$ |
| Field tensor | $F^{\mu\nu}$ | $\partial^\mu A^\nu - \partial^\nu A^\mu$ |
| Maxwell eq. | $\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$ | — |

**物理直觉（全章回顾）：** 狭义相对论源于电磁学：Michelson-Morley 实验否定了以太的存在，Einstein 提出光速不变原理。Lorentz 变换取代了 Galilei 变换，导致了时间膨胀、长度收缩和质能等价 $E=mc^2$。电磁场在相对论框架下统一为电磁张量 $F^{\mu\nu}$——电场和磁场在不同惯性系间混合变换，磁场本质上是电场的相对论修正。Maxwell 方程组可以简洁地写为两个张量方程，这是经典电动力学的最高形式。
