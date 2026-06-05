# Chapter 12: Dynamics of Relativistic Particles / 相对论粒子动力学

> Jackson *Classical Electrodynamics*, 3rd Ed, §12.1–12.13

---

## 1. Overview / 概述

This chapter applies special relativity to the motion of charged particles in electromagnetic fields. Key topics:
- Relativistic equation of motion ($\mathbf{F} = d\mathbf{p}/dt$)
- Lagrangian and Hamiltonian formulations
- Motion in uniform electric and magnetic fields
- Radiation reaction — the self-force problem
- Covariant perturbation theory for scattering

---

## 2. 相对论运动方程 (Relativistic Equation of Motion) / 相对论运动方程 (Relativistic Equation of Motion)

### 2.1 洛伦兹力方程 (Lorentz Force Equation) / 2.1 洛伦兹力方程 (Lorentz Force Equation)

In terms of 4-vectors:

$$
\frac{dp^\mu}{d\tau} = q F^{\mu\nu} U_\nu
$$

In 3-vector form:

$$
\frac{d\mathbf{p}}{dt} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B}), \quad \frac{dE}{dt} = q\mathbf{v} \cdot \mathbf{E}
$$

where $\mathbf{p} = \gamma m \mathbf{v}$, $E = \gamma m c^2$.

**Power equation**: The electric field does work on the particle; the magnetic field only changes direction.

### 2.2 匀速电场中的运动 (Uniform Electric Field E $\parallel$ x) / 2.2 匀速电场中的运动 (Uniform Electric Field E $\parallel$ x)

Initial conditions: $\mathbf{p}_0 = 0$

$$
p_x(t) = qEt
$$

$$
\gamma(t) = \sqrt{1 + (qEt/mc)^2}
$$

$$
v_x(t) = \frac{qEt/m}{\sqrt{1 + (qEt/mc)^2}}
$$

**As $t \to \infty$**: $v_x \to c$ (asymptotically approaches but never reaches $c$)

### 2.3 匀速磁场中的运动 (Uniform Magnetic Field) / 2.3 匀速磁场中的运动 (Uniform Magnetic Field)

Perpendicular to $\mathbf{B}$: circular motion with **relativistic cyclotron frequency**:

$$
\omega_c = \frac{|q|B}{\gamma m}
$$

The radius increases with energy:

$$
r = \frac{p}{|q|B} = \frac{\gamma mv}{|q|B}
$$

**In a synchrotron**: $B$ and $\omega_{\text{RF}}$ are synchronized to keep the particle on a fixed-radius orbit.

### 2.4 交叉电磁场中的运动 (Crossed E $\perp$ B) / 2.4 交叉电磁场中的运动 (Crossed E $\perp$ B)

For $\mathbf{E} \perp \mathbf{B}$ and $E < cB$, there exists a **drift frame** where $\mathbf{E}' = 0$:

$$
\mathbf{v}_d = \frac{\mathbf{E} \times \mathbf{B}}{B^2}
$$

In this frame, the particle undergoes simple gyration. In the lab frame, it follows a **trochoidal** (cycloid-like) path.

---

## 3. 拉格朗日量与哈密顿量 (Lagrangian and Hamiltonian) / 拉格朗日量与哈密顿量 (Lagrangian与Hamiltonian)

### 3.1 相对论点粒子的拉格朗日量 (Relativistic Lagrangian) / 3.1 相对论点粒子的拉格朗日量 (Relativistic Lagrangian)

**Free particle**:

$$
L_{\text{free}} = -mc^2 \sqrt{1 - v^2/c^2}
$$

**With electromagnetic field**:

$$
L = -mc^2 \sqrt{1 - v^2/c^2} + q\mathbf{A} \cdot \mathbf{v} - q\Phi
$$

Canonical momentum:

$$
\mathbf{P} = \frac{\partial L}{\partial \mathbf{v}} = \gamma m \mathbf{v} + q\mathbf{A} = \mathbf{p} + q\mathbf{A}
$$

### 3.2 哈密顿量 (Hamiltonian) / 3.2 哈密顿量 (Hamiltonian)

$$
H = \mathbf{P} \cdot \mathbf{v} - L = c\sqrt{(\mathbf{P} - q\mathbf{A})^2 + m^2c^2} + q\Phi
$$

Hamilton's equations yield the Lorentz force law.

---

## 4. 辐射反作用力 (Radiation Reaction / 辐射反作用力 (Radiation Reaction

### 4.1 问题的提出 (The Problem) / 4.1 问题的提出 (The Problem)

An accelerating charge radiates, which carries away energy and momentum. The radiated fields exert a **back-reaction** on the particle — the Abraham-Lorentz-Dirac (ALD) equation.

### 4.2 狄拉克的推导 (Dirac's Derivation, 1938) / 4.2 狄拉克的推导 (Dirac's Derivation, 1938)

Starting from energy-momentum conservation for a point charge:

$$
m \frac{du^\mu}{d\tau} = q F^{\mu\nu}_{\text{ext}} u_\nu + \Gamma^\mu
$$

where the radiation reaction 4-force is:

$$
\Gamma^\mu = \frac{q^2}{6\pi\epsilon_0 c^3} \left( \frac{d^2 u^\mu}{d\tau^2} - \frac{u^\mu}{c^2} \frac{du_\nu}{d\tau} \frac{du^\nu}{d\tau} \right)
$$

### 4.3 非相对论极限：AL方程 (Non-relativistic Limit: Abraham-Lorentz) / 4.3 非相对论极限：AL方程 (Non—relativistic Limit: Abraham—Lorentz)

$$
\mathbf{F}_{\text{rad}} = \frac{q^2}{6\pi\epsilon_0 c^3} \dot{\mathbf{a}} = \frac{\mu_0 q^2}{6\pi c} \dot{\mathbf{a}}
$$

This is the **third derivative of position** — leads to the **pre-acceleration** and **runaway solution** problems.

**Time scale**: $\tau_0 = q^2/(6\pi\epsilon_0 m c^3) \approx 6 \times 10^{-24}$ s for an electron.

### 4.4 预加速与逃逸解 (Pre-acceleration and Runaway Solutions) / 4.4 预加速与逃逸解 (Pre—acceleration与Runaway Solutions)

The ALD equation has unphysical solutions:
- **Runaway**: acceleration grows exponentially even when external force is removed
- **Pre-acceleration**: particle responds to forces before they are applied

These are artifacts of the point-charge approximation. Physical resolution requires a finite-size charge or quantum electrodynamics.

### 4.5 辐射阻尼的近似处理 (Approximate Treatment: Landau-Lifshitz) / 4.5 辐射阻尼的近似处理 (Approximate Treatment: Landau—Lifshitz)

The Landau-Lifshitz equation avoids runaway solutions:

$$
m \frac{du^\mu}{d\tau} = q F^{\mu\nu}_{\text{ext}} u_\nu + \frac{q^2}{6\pi\epsilon_0 c^3} \left \dots \right
$$

where the RR term is evaluated using the **external field** (not the full equation), making it a correction rather than a higher-order ODE.

---

## 5. 同步辐射 (Synchrotron Radiation) / 同步辐射 (Synchrotron Radiation)

### 5.1 基本特征 (Basic Properties) / 5.1 基本特征 (Basic Properties)

Relativistic electrons in a magnetic field:

**Critical frequency**:

$$
\omega_c = \frac{3}{2} \gamma^3 \frac{c}{\rho} = \frac{3qB}{2m} \gamma^2
$$

**Power radiated**:

$$
P = \frac{q^2 \gamma^4}{6\pi\epsilon_0 c} \frac{v_\perp^2}{\rho^2}
$$

**Angular distribution** — strongly forward-peaked:

$$
\frac{dP}{d\Omega} \propto \frac{1}{(1 - \beta\cos\theta)^3}
$$

Opening angle: $\Delta\theta \sim 1/\gamma$

### 5.2 谱分布 (Spectral Distribution) / 5.2 谱分布 (Spectral Distribution)

**Universal spectrum formula**:

$$
\frac{dP}{d\omega} = \frac{\sqrt{3}}{2\pi} \frac{q^3 B}{m} F\left(\frac{\omega}{\omega_c}\right)
$$

where $F(x) = x \int_x^\infty K_{5/3}(\xi) d\xi$ (modified Bessel function integral).

- $x \ll 1$: $F(x) \propto x^{1/3}$ (rise)
- $x \gg 1$: $F(x) \propto \sqrt{x} e^{-x}$ (exponential cutoff)

**Spectral shape**: Broad continuum from radio to X-ray.

---

## 6. 康普顿散射 (Compton Scattering) / 康普顿散射 (Compton Scattering)

### 6.1 汤姆孙散射回顾 (Thomson Scattering, Classical) / 6.1 汤姆孙散射回顾 (Thomson 散射, Classical)

Cross section for free electron when $\hbar\omega \ll mc^2$:

$$
\sigma_T = \frac{8\pi}{3} \left(\frac{q^2}{4\pi\epsilon_0 m c^2}\right)^2 = 6.65 \times 10^{-29} \text{ m}^2
$$

### 6.2 康普顿散射 (Quantum: Klein-Nishina) / 6.2 康普顿散射 (Quantum: Klein—Nishina)

When $\hbar\omega \gtrsim mc^2$, quantum effects matter:

$$
\frac{d\sigma}{d\Omega} = \frac{r_0^2}{2} \left(\frac{\omega'}{\omega}\right)^2 \left(\frac{\omega}{\omega'} + \frac{\omega'}{\omega} - \sin^2\theta\right)
$$

**Compton shift**:

$$
\lambda' - \lambda = \frac{h}{mc}(1 - \cos\theta)
$$

**Klein-Nishina total cross section** (low energy $\to$ Thomson, high energy $\propto 1/\omega$):

### 6.3 逆康普顿散射 (Inverse Compton Scattering) / 6.3 逆康普顿散射 (Inverse Compton 散射)

Low-energy photon gains energy from a relativistic electron:

$$
E_\gamma' \approx \gamma^2 E_\gamma
$$

**Important in**: astrophysics (Sunyaev-Zeldovich effect, gamma-ray bursts)

---

## 7. 散射矩阵与量子电动力学 (S-Matrix and QED) / 散射矩阵与量子电动力学 (S—Matrix与QED)

### 7.1 最小耦合与费曼规则 (Minimal Coupling and Feynman Rules) / 7.1 最小耦合与费曼规则 (Minimal Coupling与Feynman Rules)

The interaction vertex comes from minimal coupling: $\partial_\mu \to \partial_\mu + i q A_\mu$

**QED scattering amplitudes**:

$$
\mathcal{M} \propto \bar{u}(p') \gamma^\mu u(p) \cdot \frac{1}{q^2} \cdot \bar{u}(k') \gamma_\mu u(k)
$$

Electron-photon interaction vertex: $-i e \gamma^\mu$

### 7.2 电子-电子散射：Møller散射 (Møller Scattering)** / 7.2 电子—电子散射：Møller散射 (Møller 散射)**
$e^- e^- \to e^- e^-$

$$
\frac{d\sigma}{d\Omega} = \frac{\alpha^2}{4s} \left( \frac{s^2 + u^2}{t^2} + \frac{s^2 + t^2}{u^2} + \frac{2s^2}{tu} \right)
$$

### 7.3 电子-正电子散射：Bhabha散射 (Bhabha Scattering)** / 7.3 电子—正电子散射：Bhabha散射 (Bhabha 散射)**
$e^+ e^- \to e^+ e^-$

---

## 8. 重要公式速查 (Key Formulas Cheat Sheet) / 重要公式速查 (Key Formulas Cheat Sheet)

| Concept | Formula |
|---------|---------|
| Relativistic momentum | $\mathbf{p} = \gamma m \mathbf{v}$ |
| Energy | $E = \gamma m c^2$ |
| Lorentz force | $d\mathbf{p}/dt = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})$ |
| Cyclotron frequency | $\omega_c = qB/(\gamma m)$ |
| E×B drift | $\mathbf{v}_d = (\mathbf{E} \times \mathbf{B})/B^2$ |
| AL radiation reaction | $\mathbf{F}_{\text{rad}} = \mu_0 q^2 \dot{\mathbf{a}} / (6\pi c)$ |
| Synchrotron power | $P = q^2 \gamma^4 v_\perp^2 / (6\pi\epsilon_0 c \rho^2)$ |
| Critical frequency | $\omega_c = 3\gamma^3 c / (2\rho)$ |
| Thomson cross section | $\sigma_T = 8\pi r_0^2 / 3 \approx 6.65 \times 10^{-29} \text{ m}^2$ |
| Compton shift | $\Delta\lambda = (h/mc)(1-\cos\theta)$ |
| QED running coupling | $\alpha \approx 1/137$ |

---

## 9. 物理直觉 (Physical Intuition) / 物理直觉 (Physical Intuition)

1. **Relativistic inertia**: as $v \to c$, $d\mathbf{p}/dt = \gamma m \mathbf{a}$ — harder to accelerate
2. **E×B drift**: independent of charge sign (both species drift same way)
3. **Synchrotron radiation**: tightly collimated forward ($\sim 1/\gamma$) due to relativistic beaming
4. **Radiation reaction**: the self-interaction problem remains unsolved in classical electrodynamics
5. **Inverse Compton**: relativistic electrons can "bump" microwave photons up to X-ray energies
6. **Threshold energies**: in particle physics, colliders use center-of-mass energy, not lab energy

---

## 10. 应用 (Applications) / 应用 (Applications)

- **Particle accelerators**: cyclotron, synchrotron, linear accelerator design
- **Synchrotron light sources**: X-ray generation for materials science
- **Free-electron lasers (FELs)**: coherent radiation from relativistic electron beams
- **Astrophysics**: non-thermal emission (supernova remnants, AGN jets, pulsars)
- **Plasma physics**: magnetic confinement, charged particle dynamics
- **Medical**: radiotherapy, medical imaging (synchrotron-based CT)

---

## References / 参考文献

- Jackson §12.1–§12.13
- Landau & Lifshitz, *The Classical Theory of Fields* (radiation reaction)
- Dirac, *Classical Theory of Radiating Electrons* (1938 Proc. R. Soc.)
- Rybicki & Lightman, *Radiative Processes in Astrophysics* (synchrotron, Compton)
- Peskin & Schroeder, *An Introduction to Quantum Field Theory* (QED scattering)
