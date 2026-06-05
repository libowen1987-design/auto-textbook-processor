---
title: Chapter 2: Electromagnetic Theory / 第2章：电磁理论
source: Robert E. Collin, Foundations for Microwave Engineering, 2nd Ed., IEEE Press, 2000, Ch. 2 (§2.1–§2.12), pp. 17–70.
---

# Chapter 2: Electromagnetic Theory
# 第2章：电磁理论（Electromagnetic Theory）

**Source:** Robert E. Collin, *Foundations for Microwave Engineering*, 2nd Ed., IEEE Press, 2000, Ch. 2 (§2.1–§2.12), pp. 17–70.

---

## §2.1 Maxwell's Equations (pp. 17–23)
## §2.1 麦克斯韦方程组（Maxwell's Equations）

Collin presents Maxwell's equations as the foundation of all electromagnetic field theory.

> 麦克斯韦方程组是所有电磁场理论的基石，Collin 从微分形式和积分形式两个角度同时给出阐述。

### Differential Form
### 微分形式（Differential Form）

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
\quad \text{(Faraday's law)} \tag{2.1a}
$$

$$
\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}
\quad \text{(Ampère's law)} \tag{2.1b}
$$

$$
\nabla \cdot \mathbf{D} = \rho_v
\quad \text{(Gauss's law for electric fields)} \tag{2.1c}
$$

$$
\nabla \cdot \mathbf{B} = 0
\quad \text{(Gauss's law for magnetic fields)} \tag{2.1d}
$$

**Units:**
| Symbol | Quantity | SI Unit |
|--------|----------|---------|
| $\mathbf{E}$ | Electric field intensity | V/m |
| $\mathbf{D}$ | Electric flux density | C/m² |
| $\mathbf{H}$ | Magnetic field intensity | A/m |
| $\mathbf{B}$ | Magnetic flux density | T (Wb/m²) |
| $\mathbf{J}$ | Electric current density | A/m² |
| $\rho_v$ | Volume charge density | C/m³ |

### Integral Form
### 积分形式（Integral Form）

$$
\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{S}
\tag{2.2a}
$$

$$
\oint_C \mathbf{H} \cdot d\mathbf{l} = \int_S \mathbf{J} \cdot d\mathbf{S} + \frac{d}{dt} \int_S \mathbf{D} \cdot d\mathbf{S}
\tag{2.2b}
$$

$$
\oint_S \mathbf{D} \cdot d\mathbf{S} = \int_V \rho_v \, dV
\tag{2.2c}
$$

$$
\oint_S \mathbf{B} \cdot d\mathbf{S} = 0
\tag{2.2d}
$$

### Equation of Continuity
### 连续性方程（Equation of Continuity）

Derived from the divergence of (2.1b) combined with (2.1c):

$$
\nabla \cdot \mathbf{J} = -\frac{\partial \rho_v}{\partial t}
\tag{2.3}
$$

**Physical intuition:** Current conservation — charge leaving a volume must equal the decrease of charge within it.

> **物理直觉**：连续性方程本质上是电荷守恒定律的数学表述。

### Time-Harmonic Form (phasor notation)
### 时谐形式（phasor notation）

For fields varying as $e^{j\omega t}$ (Collin uses $e^{j\omega t}$ time convention):

$$
\nabla \times \mathbf{E} = -j\omega \mathbf{B}
\tag{2.4a}
$$

$$
\nabla \times \mathbf{H} = \mathbf{J} + j\omega \mathbf{D}
\tag{2.4b}
$$

$$
\nabla \cdot \mathbf{D} = \rho_v
\tag{2.4c}
$$

$$
\nabla \cdot \mathbf{B} = 0
\tag{2.4d}
$$

**Collin's note:** The $e^{j\omega t}$ convention means time derivative $\partial/\partial t \to j\omega$.

> **注**：Collin 采用 $e^{j\omega t}$ 时间约定，时间的偏导数等价于 $j\omega$。

---

## §2.2 Constitutive Relations (pp. 23–28)
## §2.2 本构关系（Constitutive Relations）

These relate the field quantities to material properties.

> 本构关系将场量与材料电磁特性相联系，是求解具体问题的必要补充。

### Simple Media (Linear, Isotropic, Homogeneous)
### 简单介质（Simple Media）

$$
\mathbf{D} = \varepsilon \mathbf{E}
\quad \text{where } \varepsilon = \varepsilon_0 \varepsilon_r
\tag{2.5a}
$$

$$
\mathbf{B} = \mu \mathbf{H}
\quad \text{where } \mu = \mu_0 \mu_r
\tag{2.5b}
$$

$$
\mathbf{J} = \sigma \mathbf{E}
\quad \text{(Ohm's law)} \tag{2.5c}
$$

**Fundamental Constants:**
| Constant | Value |
|----------|-------|
| Speed of light | $c_0 = 299\,792\,458$ m/s |
| Permittivity of free space | $\varepsilon_0 = 8.8541878176\ldots \times 10^{-12}$ F/m |
| Permeability of free space | $\mu_0 = 4\pi \times 10^{-7}$ H/m |
| Intrinsic impedance of free space | $\eta_0 = \sqrt{\mu_0/\varepsilon_0} = 376.7303\ldots\ \Omega$ |

From Maxwell's equations in free space:
$$
c_0 = \frac{1}{\sqrt{\mu_0 \varepsilon_0}}
\tag{2.6}
$$

$$
\eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} = \mu_0 c_0
\tag{2.7}
$$

### Lossy Dielectrics (Complex Permittivity)
### 有损介质（Lossy Dielectrics）

For a lossy dielectric:
$$
\mathbf{J} = \sigma \mathbf{E} + j\omega \varepsilon \mathbf{E} = j\omega \varepsilon_c \mathbf{E}
$$

where the **complex permittivity** is:
$$
\varepsilon_c = \varepsilon' - j\varepsilon'' = \varepsilon_0 \varepsilon_r (1 - j \tan\delta)
\tag{2.8}
$$

The **loss tangent** is defined as:
$$
\tan\delta = \frac{\varepsilon''}{\varepsilon'} = \frac{\sigma}{\omega \varepsilon'}
\tag{2.9}
$$

> 复介电常数和损耗角正切是描述介质损耗的核心参数，损耗角正切越大，电磁能量在介质中耗散越多。

### Anisotropic Media
### 各向异性介质（Anisotropic Media）

For ferrites and other anisotropic materials:
$$
\mathbf{D} = \bar{\bar{\varepsilon}} \cdot \mathbf{E}, \quad
\mathbf{B} = \bar{\bar{\mu}} \cdot \mathbf{H}
$$
where $\bar{\bar{\varepsilon}}$ and $\bar{\bar{\mu}}$ are permittivity and permeability tensors (3\times3 matrices). Ferrites under DC magnetic bias exhibit **gyromagnetic** behavior (§2.2, p. 27).

> 铁氧体等各向异性材料在直流磁场偏置下呈现旋磁特性，是构成环行器和隔离器的物理基础。

---

## §2.3 Static Fields (pp. 28–31)
## §2.3 静态场（Static Fields）

A brief review of electrostatic and magnetostatic fields as limiting cases.

> 静态场是时变电磁场在 $\omega \to 0$ 时的极限情况，分别满足静电场和静磁场的特有方程。

### Electrostatics ($\partial/\partial t = 0$)
### 静电学（Electrostatics）

$$
\nabla \times \mathbf{E} = 0 \quad \Rightarrow \quad \mathbf{E} = -\nabla \Phi
\tag{2.10}
$$

$$
\nabla \cdot \mathbf{D} = \rho_v \quad \Rightarrow \quad \nabla^2 \Phi = -\rho_v / \varepsilon
\quad \text{(Poisson's equation)} \tag{2.11}
$$

In a charge-free region ($\rho_v = 0$):
$$
\nabla^2 \Phi = 0 \quad \text{(Laplace's equation)} \tag{2.12}
$$

### Magnetostatics ($\partial/\partial t = 0$)
### 静磁学（Magnetostatics）

$$
\nabla \times \mathbf{H} = \mathbf{J}, \quad \nabla \cdot \mathbf{B} = 0 \quad \Rightarrow \quad \mathbf{B} = \nabla \times \mathbf{A}
\tag{2.13}
$$

where $\mathbf{A}$ is the magnetic vector potential. In the Coulomb gauge ($\nabla \cdot \mathbf{A} = 0$):
$$
\nabla^2 \mathbf{A} = -\mu \mathbf{J}
\quad \text{(Vector Poisson's equation)} \tag{2.14}
$$

---

## §2.4 Wave Equation (pp. 31–33)
## §2.4 波动方程（Wave Equation）

Collin derives the wave equation from Maxwell's equations.

> 波动方程是电磁波传播行为的控制方程，可由麦克斯韦方程组直接推导得出。

### Derivation
### 推导（Derivation）

Take curl of (2.1a), use (2.1b) and constitutive relations, assuming homogeneous, isotropic, source-free ($\mathbf{J}=0$) region:

$$
\nabla \times (\nabla \times \mathbf{E}) = -\mu \frac{\partial}{\partial t} (\nabla \times \mathbf{H})
= -\mu \frac{\partial}{\partial t} \left( \sigma \mathbf{E} + \varepsilon \frac{\partial \mathbf{E}}{\partial t} \right)
$$

Using vector identity $\nabla \times (\nabla \times \mathbf{E}) = \nabla (\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E}$ and $\nabla \cdot \mathbf{E} = 0$ (source-free):

$$
\nabla^2 \mathbf{E} = \mu \sigma \frac{\partial \mathbf{E}}{\partial t} + \mu \varepsilon \frac{\partial^2 \mathbf{E}}{\partial t^2}
\tag{2.15a}
$$

Similarly for $\mathbf{H}$:
$$
\nabla^2 \mathbf{H} = \mu \sigma \frac{\partial \mathbf{H}}{\partial t} + \mu \varepsilon \frac{\partial^2 \mathbf{H}}{\partial t^2}
\tag{2.15b}
$$

### Time-Harmonic (Phasor) Wave Equation
### 时谐波动方程（Time-Harmonic Wave Equation）

Substituting $\mathbf{E}(x,y,z,t) = \mathbf{E}(x,y,z)e^{j\omega t}$:

$$
\nabla^2 \mathbf{E} = j\omega\mu\sigma \mathbf{E} - \omega^2 \mu\varepsilon \mathbf{E}
= -\omega^2 \mu \varepsilon_c \mathbf{E}
$$

Define **propagation constant**:
$$
\gamma = \alpha + j\beta = \sqrt{j\omega\mu(\sigma + j\omega\varepsilon)}
\tag{2.16}
$$

The wave equation becomes:
$$
\nabla^2 \mathbf{E} - \gamma^2 \mathbf{E} = 0
\tag{2.17}
$$

For **lossless media** ($\sigma = 0$):
$$
\nabla^2 \mathbf{E} + k^2 \mathbf{E} = 0
\quad \text{(Helmholtz equation)} \tag{2.18}
$$

where the **wavenumber** is:
$$
k = \omega \sqrt{\mu\varepsilon} = \frac{2\pi}{\lambda}
\tag{2.19}
$$

> 传播常数 $\gamma = \alpha + j\beta$ 的实部 $\alpha$ 描述衰减，虚部 $\beta$ 描述相位变化。

---

## §2.5 Energy and Power — Poynting's Theorem (pp. 33–38)
## §2.5 能量与功率——坡印廷定理（Energy and Power — Poynting's Theorem）

### Poynting's Theorem in Differential Form
### 微分形式坡印廷定理（Poynting's Theorem in Differential Form）

From Maxwell's equations, Collin derives the power balance:

$$
-\nabla \cdot (\mathbf{E} \times \mathbf{H}) = \mathbf{E} \cdot \mathbf{J} +
\mathbf{H} \cdot \frac{\partial \mathbf{B}}{\partial t} +
\mathbf{E} \cdot \frac{\partial \mathbf{D}}{\partial t}
\tag{2.20}
$$

### Integral (Conservation) Form
### 积分形式（Conservation Form）

$$
-\oint_S (\mathbf{E} \times \mathbf{H}) \cdot d\mathbf{S} =
\int_V \mathbf{E} \cdot \mathbf{J} \, dV +
\frac{\partial}{\partial t} \int_V \left( \frac{1}{2} \mathbf{H} \cdot \mathbf{B} + \frac{1}{2} \mathbf{E} \cdot \mathbf{D} \right) dV
\tag{2.21}
$$

### Poynting Vector
### 坡印廷矢量（Poynting Vector）

$$
\mathbf{S} = \mathbf{E} \times \mathbf{H}
\quad \text{[W/m²]} \tag{2.22}
$$

**Physical interpretation:**
- $\mathbf{E} \times \mathbf{H}$ represents the instantaneous power flow density
- $\oint_S \mathbf{S} \cdot d\mathbf{S}$ = net power leaving the closed surface $S$
- $\int_V \mathbf{E} \cdot \mathbf{J} \, dV$ = power dissipated as heat (ohmic loss)
- $\frac{\partial}{\partial t} (\frac{1}{2}\mathbf{H}\cdot\mathbf{B} + \frac{1}{2}\mathbf{E}\cdot\mathbf{D})$ = rate of change of stored energy

> **物理意义**：坡印廷矢量 $\mathbf{S}$ 表示电磁功率流密度，其面积分为穿过闭合面的净功率。

### Energy Densities
### 能量密度（Energy Densities）

| Quantity | Expression | Unit |
|----------|-----------|------|
| Electric energy density | $w_e = \frac{1}{2} \mathbf{E} \cdot \mathbf{D}$ | J/m³ |
| Magnetic energy density | $w_m = \frac{1}{2} \mathbf{H} \cdot \mathbf{B}$ | J/m³ |
| Total EM energy density | $w = w_e + w_m$ | J/m³ |

### Time-Average Poynting Vector (for Time-Harmonic Fields)
### 时均坡印廷矢量（Time-Average Poynting Vector）

For fields $\mathbf{E}(t) = \mathrm{Re}[\mathbf{E}e^{j\omega t}]$ and $\mathbf{H}(t) = \mathrm{Re}[\mathbf{H}e^{j\omega t}]$:

$$
\mathbf{S}_{\text{avg}} = \frac{1}{2} \mathrm{Re}[\mathbf{E} \times \mathbf{H}^*]
\quad \text{[W/m²]} \tag{2.23}
$$

### Complex Poynting Theorem
### 复坡印廷定理（Complex Poynting Theorem）

$$
-\frac{1}{2} \oint_S (\mathbf{E} \times \mathbf{H}^*) \cdot d\mathbf{S} =
\frac{1}{2} \int_V \mathbf{E} \cdot \mathbf{J}^* \, dV +
j2\omega \int_V (w_m - w_e) \, dV
\tag{2.24}
$$

where the last term represents the reactive (stored) energy.

> 复坡印廷定理的实部表示有功功率，虚部表示无功（储能）功率。

### Power Dissipated in a Conductor
### 导体中的功率耗散（Power Dissipated in a Conductor）

$$
P_d = \frac{1}{2} \int_V \sigma |\mathbf{E}|^2 \, dV = \frac{1}{2} \int_V \frac{|\mathbf{J}|^2}{\sigma} \, dV
\quad \text{[W]} \tag{2.25}
$$

At microwave frequencies, the fields penetrate conductors only to a **skin depth**, so the dissipated power is often expressed using **surface resistance** $R_s$:

$$
P_d = \frac{R_s}{2} \int_S |\mathbf{J}_s|^2 \, dS
\tag{2.26}
$$

where $\mathbf{J}_s$ is the surface current density.

---

## §2.6 Boundary Conditions (pp. 39–44)
## §2.6 边界条件（Boundary Conditions）

Collin lists the boundary conditions at the interface between two media (1) and (2).

> 边界条件是求解电磁问题的三类边界条件之一，描述两种介质界面上的场量突变关系。

### General Boundary Conditions
### 一般边界条件（General Boundary Conditions）

$$
\hat{n} \times (\mathbf{E}_2 - \mathbf{E}_1) = 0
\quad \text{(Tangential $\mathbf{E}$ continuous)} \tag{2.27a}
$$

$$
\hat{n} \times (\mathbf{H}_2 - \mathbf{H}_1) = \mathbf{J}_s
\quad \text{(Tangential $\mathbf{H}$ discontinuity = surface current)} \tag{2.27b}
$$

$$
\hat{n} \cdot (\mathbf{D}_2 - \mathbf{D}_1) = \rho_s
\quad \text{(Normal $\mathbf{D}$ discontinuity = surface charge)} \tag{2.27c}
$$

$$
\hat{n} \cdot (\mathbf{B}_2 - \mathbf{B}_1) = 0
\quad \text{(Normal $\mathbf{B}$ continuous)} \tag{2.27d}
$$

where $\hat{n}$ is the unit normal vector pointing from medium 1 to medium 2.

### Perfect Electric Conductor (PEC) Boundary
### 理想电导体边界（Perfect Electric Conductor Boundary）

For a PEC ($\sigma \to \infty$), fields inside are zero:

$$
\hat{n} \times \mathbf{E} = 0
\quad \text{(Tangential $\mathbf{E} = 0$ on PEC)} \tag{2.28a}
$$

$$
\hat{n} \times \mathbf{H} = \mathbf{J}_s
\quad \text{(Surface current on PEC)} \tag{2.28b}
$$

$$
\hat{n} \cdot \mathbf{D} = \rho_s
\quad \text{(Surface charge on PEC)} \tag{2.28c}
$$

$$
\hat{n} \cdot \mathbf{B} = 0
\quad \text{(Normal $\mathbf{B} = 0$ on PEC)} \tag{2.28d}
$$

### Interface Between Two Dielectrics ($\mathbf{J}_s = 0$, $\rho_s = 0$)
### 两种介质界面（Two Dielectrics Interface）

- Tangential $\mathbf{E}$ and $\mathbf{H}$ are continuous
- Normal $\mathbf{D}$ and $\mathbf{B}$ are continuous
- Field lines **refract** at the interface:
  - $\tan\theta_1 / \tan\theta_2 = \varepsilon_1 / \varepsilon_2$ (for E-field)
  - $\tan\theta_1 / \tan\theta_2 = \mu_1 / \mu_2$ (for H-field)

> 介质界面上，$\mathbf{E}$ 的切向分量和 $\mathbf{D}$ 的法向分量连续，这是电磁场在界面处必须满足的基本约束。

---

## §2.7 Plane Waves (pp. 44–49)
## §2.7 平面波（Plane Waves）

### Uniform Plane Waves in Source-Free, Lossless Media
### 均匀平面波（Uniform Plane Waves）

For a wave propagating in the $+z$ direction with $\mathbf{E}$ and $\mathbf{H}$ uniform in the $x$-$y$ plane:

$$
\mathbf{E}(z,t) = \hat{x} E_0 \cos(\omega t - kz + \phi)
\tag{2.29}
$$

$$
\mathbf{H}(z,t) = \hat{y} \frac{E_0}{\eta} \cos(\omega t - kz + \phi)
\tag{2.30}
$$

where:
- $k = \omega \sqrt{\mu\varepsilon}$ — wavenumber [rad/m] (Eq. 2.19)
- $\eta = \sqrt{\mu/\varepsilon}$ — intrinsic impedance [Ω] (Eq. 2.7)
- Direction of propagation: $\hat{k} = \hat{z}$

### Plane Waves in Free Space
### 自由空间中的平面波（Plane Waves in Free Space）

| Parameter | Value |
|-----------|-------|
| Wavenumber | $k_0 = \omega \sqrt{\mu_0 \varepsilon_0} = 2\pi / \lambda_0$ |
| Intrinsic impedance | $\eta_0 = \sqrt{\mu_0/\varepsilon_0} = 376.73\ \Omega$ |
| Phase velocity | $v_p = \omega/k_0 = c_0$ |
| Wavelength | $\lambda_0 = c_0/f$ |

### Wave Impedance
### 波阻抗（Wave Impedance）

For a plane wave propagating in the $+z$ direction:

$$
\frac{|\mathbf{E}|}{|\mathbf{H}|} = \eta = \sqrt{\frac{\mu}{\varepsilon}}
\quad \text{[Ω]} \tag{2.31}
$$

**Physical intuition:** The intrinsic impedance $\eta$ is analogous to the characteristic impedance $Z_0$ of a transmission line. It relates the transverse electric and magnetic fields.

> **物理直觉**：本征阻抗 $\eta$ 与传输线特性阻抗 $Z_0$ 类似，反映了电场与磁场的比值关系。

### Plane Wave in Lossy Media (pp. 47–49)
### 有损介质中的平面波（Plane Wave in Lossy Media）

In lossy media ($\sigma \neq 0$), use complex permittivity $\varepsilon_c$:

Propagation constant:
$$
\gamma = \alpha + j\beta = j\omega\sqrt{\mu\varepsilon_c}
\tag{2.32}
$$

where:
$$
\varepsilon_c = \varepsilon - j\frac{\sigma}{\omega}
\tag{2.33}
$$

The fields decay as $e^{-\alpha z}$:
$$
\mathbf{E}(z) = \hat{x} E_0 e^{-\alpha z} e^{-j\beta z}
\tag{2.34}
$$

### Skin Effect (§2.7, pp. 47–49)
### 趋肤效应（Skin Effect）

In a **good conductor** ($\sigma \gg \omega\varepsilon$):
$$
\gamma \approx \sqrt{j\omega\mu\sigma} = (1+j)\sqrt{\frac{\omega\mu\sigma}{2}}
\tag{2.35}
$$

The **skin depth** (distance over which fields decay by $e^{-1}$):
$$
\delta_s = \frac{1}{\alpha} = \sqrt{\frac{2}{\omega\mu\sigma}}
\quad \text{[m]} \tag{2.36}
$$

**Surface resistance:**
$$
R_s = \frac{1}{\sigma\delta_s} = \sqrt{\frac{\omega\mu}{2\sigma}}
\quad \text{[Ω/□]} \tag{2.37}
$$

**Engineering implications** (§2.7):
- At 10 GHz: $\delta_s \approx 0.66\ \mu$m for Cu ($\sigma = 5.8\times 10^7$ S/m)
- Conductor losses scale as $\sqrt{f}$ due to skin effect
- Waveguides and microstrip lines use high-conductivity metals (Cu, Au, Ag)
- Surface plating (e.g., Au on Cu) must be > several skin depths

> **工程意义**：趋肤深度随频率升高而减小，10 GHz 时铜的趋肤深度仅约 0.66 μm，因此表面镀金需达数个趋肤深度才能有效保护。

### Intrinsic Impedance for Lossy Media
### 有损介质的本征阻抗（Intrinsic Impedance for Lossy Media）

$$
\eta_c = \sqrt{\frac{\mu}{\varepsilon_c}} = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\varepsilon}}
\tag{2.38}
$$

For a good conductor:
$$
\eta_c \approx (1+j) \sqrt{\frac{\omega\mu}{2\sigma}} = (1+j) \frac{1}{\sigma\delta_s}
\quad \text{[Ω]} \tag{2.39}
$$

---

## §2.8 Reflection from a Dielectric Interface — Fresnel's Equations (pp. 49–53)
## §2.8 介质界面反射——菲涅尔方程（Fresnel's Equations）

### 1. Parallel Polarization ($\mathbf{E}$ in plane of incidence)
### 1. 平行极化（Parallel Polarization）

The electric field vector lies in the plane of incidence ($x$-$z$ plane).

**Reflection and transmission coefficients:**

$$
\Gamma_{\parallel} = \frac{E_r}{E_i} =
\frac{\eta_2 \cos\theta_t - \eta_1 \cos\theta_i}{\eta_2 \cos\theta_t + \eta_1 \cos\theta_i}
\tag{2.40a}
$$

$$
T_{\parallel} = \frac{E_t}{E_i} =
\frac{2\eta_2 \cos\theta_i}{\eta_2 \cos\theta_t + \eta_1 \cos\theta_i}
\tag{2.40b}
$$

Using Snell's law: $k_1 \sin\theta_i = k_2 \sin\theta_t$

### 2. Perpendicular Polarization ($\mathbf{E}$ perpendicular to plane of incidence)
### 2. 垂直极化（Perpendicular Polarization）

$$
\Gamma_{\perp} = \frac{E_r}{E_i} =
\frac{\eta_2 \cos\theta_i - \eta_1 \cos\theta_t}{\eta_2 \cos\theta_i + \eta_1 \cos\theta_t}
\tag{2.41a}
$$

$$
T_{\perp} = \frac{E_t}{E_i} =
\frac{2\eta_2 \cos\theta_i}{\eta_2 \cos\theta_i + \eta_1 \cos\theta_t}
\tag{2.41b}
$$

### Brewster Angle
### 布鲁斯特角（Brewster Angle）

When $\Gamma_{\parallel} = 0$ (for non-magnetic media, $\mu_1 = \mu_2$):

$$
\theta_B = \tan^{-1}\sqrt{\frac{\varepsilon_2}{\varepsilon_1}}
\tag{2.42}
$$

At the Brewster angle, the reflected wave for parallel polarization is **zero**. No Brewster angle exists for perpendicular polarization in non-magnetic media.

> 布鲁斯特角：自然光以该角度入射时，平行极化分量全透射无反射，可用于制造偏振片。

### Total Internal Reflection
### 全内反射（Total Internal Reflection）

When $k_2 < k_1$ ($\varepsilon_2 < \varepsilon_1$) and $\theta_i$ exceeds the critical angle:

$$
\theta_c = \sin^{-1}\sqrt{\frac{\varepsilon_2}{\varepsilon_1}}
\tag{2.43}
$$

For $\theta_i > \theta_c$, $\Gamma = e^{j\phi}$ (unit magnitude — total reflection, but with a phase shift).

**Note:** Collin uses $\eta_1 = \sqrt{\mu_1/\varepsilon_1}$, $\eta_2 = \sqrt{\mu_2/\varepsilon_2}$.

### Normal Incidence ($\theta_i = 0$)
### 垂直入射（Normal Incidence）

$$
\Gamma = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1}
\tag{2.44a}
$$

$$
T = \frac{2\eta_2}{\eta_2 + \eta_1}
\tag{2.44b}
$$

For incidence from air ($\eta_0$) onto a dielectric ($\eta = \eta_0/\sqrt{\varepsilon_r}$):
$$
\Gamma = \frac{1 - \sqrt{\varepsilon_r}}{1 + \sqrt{\varepsilon_r}}, \quad
T = \frac{2}{1 + \sqrt{\varepsilon_r}}
$$

---

## §2.9 Reflection from a Conducting Plane (pp. 53–55)
## §2.9 导体平面反射（Reflection from a Conducting Plane）

### Normal Incidence on PEC
### 垂直入射到理想电导体（Normal Incidence on PEC）

Total tangential $\mathbf{E} = 0$ at the conductor surface.

- Incident wave: $\mathbf{E}^i = \hat{x} E_0 e^{-jkz}$, $\mathbf{H}^i = \hat{y} \frac{E_0}{\eta_0} e^{-jkz}$
- Reflected wave: $\mathbf{E}^r = -\hat{x} E_0 e^{+jkz}$, $\mathbf{H}^r = -\hat{y} \frac{E_0}{\eta_0} e^{+jkz}$
- Total fields form a **standing wave**:

$$
\mathbf{E}^{\text{tot}} = \hat{x} (-2jE_0) \sin(kz)
\tag{2.45a}
$$

$$
\mathbf{H}^{\text{tot}} = \hat{y} \frac{2E_0}{\eta_0} \cos(kz)
\tag{2.45b}
$$

**Key properties:**
- $\mathbf{E}$ has nulls at $z = -n\lambda/2$ ($n = 0,1,2,\ldots$)
- $\mathbf{H}$ has maxima at $z = -n\lambda/2$ (and vice versa)
- $\mathbf{E}$ and $\mathbf{H}$ are $90^\circ$ out of phase in space
- No net time-average power flow (pure standing wave): $\langle \mathbf{S} \rangle = 0$

> **驻波特性**：理想导体表面为电场的波节（为零），磁场的波腹（最大），二者空间相位相差90°，无净功率流。

### Oblique Incidence on PEC
### 斜入射到理想电导体（Oblique Incidence on PEC）

For TE (perpendicular) polarization:
$$
\mathbf{E}^{\text{tot}} = \hat{y} (-2jE_0) \sin(k_z z) e^{-jk_x x}
\tag{2.46}
$$

where $k_z = k\cos\theta$, $k_x = k\sin\theta$. This represents a wave propagating along $x$ with a standing-wave pattern in $z$.

---

## §2.10 Potential Theory (pp. 56–59)
## §2.10 势理论（Potential Theory）

Collin introduces scalar and vector potentials to simplify EM field calculations.

> 势理论通过引入标量势 $\Phi$ 和矢量势 $\mathbf{A}$ 来简化电磁场计算，是求解麦克斯韦方程的重要数学工具。

### Magnetic Vector Potential $\mathbf{A}$
### 磁矢量势（Magnetic Vector Potential）

From $\nabla \cdot \mathbf{B} = 0$:
$$
\mathbf{B} = \nabla \times \mathbf{A}
\tag{2.47}
$$

### Electric Scalar Potential $\Phi$
### 电标量势（Electric Scalar Potential）

From Faraday's law and using (2.47):
$$
\nabla \times \mathbf{E} = -\frac{\partial}{\partial t}(\nabla \times \mathbf{A})
\quad \Rightarrow \quad
\nabla \times \left( \mathbf{E} + \frac{\partial \mathbf{A}}{\partial t} \right) = 0
$$

Thus:
$$
\mathbf{E} = -\nabla \Phi - \frac{\partial \mathbf{A}}{\partial t}
\tag{2.48}
$$

### Lorentz Gauge
### 洛伦兹规范（Lorentz Gauge）

$$
\nabla \cdot \mathbf{A} = -\mu\varepsilon \frac{\partial \Phi}{\partial t}
\tag{2.49}
$$

Under the Lorentz gauge, the potentials satisfy **uncoupled wave equations**:

$$
\nabla^2 \mathbf{A} - \mu\varepsilon \frac{\partial^2 \mathbf{A}}{\partial t^2} = -\mu \mathbf{J}
\tag{2.50}
$$

$$
\nabla^2 \Phi - \mu\varepsilon \frac{\partial^2 \Phi}{\partial t^2} = -\frac{\rho_v}{\varepsilon}
\tag{2.51}
$$

### Time-Harmonic Potentials
### 时谐势（Time-Harmonic Potentials）

$$
\nabla^2 \mathbf{A} + k^2 \mathbf{A} = -\mu \mathbf{J}
\tag{2.52}
$$

$$
\nabla^2 \Phi + k^2 \Phi = -\frac{\rho_v}{\varepsilon}
\tag{2.53}
$$

where $k = \omega\sqrt{\mu\varepsilon}$.

---

## §2.11 Derivation of Solution for Vector Potential (pp. 59–61)
## §2.11 矢量势方程的求解（Solution for Vector Potential）

### Solution for an Infinitesimal Current Source (Hertzian Dipole)
### 点电流源的解——赫兹偶极子（Hertzian Dipole）

For a current element $\mathbf{J} \, dV$ at a point, the solution to (2.52) is:

$$
\mathbf{A}(\mathbf{r}) = \frac{\mu}{4\pi} \int_V \mathbf{J}(\mathbf{r}') \frac{e^{-jkR}}{R} \, dV'
\tag{2.54}
$$

where $R = |\mathbf{r} - \mathbf{r}'|$ is the distance from source point to observation point.

**Key properties:**
- $e^{-jkR}/R$ represents an **outgoing spherical wave** (§2.11, Eq. 2.11.1)
- This is the **retarded potential** solution (causal, outward-propagating)
- For a Hertzian dipole of length $dl$ with current $I$, $\mathbf{J} \, dV = \hat{z} I \, dl$, giving:

$$
\mathbf{A} = \hat{z} \frac{\mu I \, dl}{4\pi} \frac{e^{-jkr}}{r}
\tag{2.55}
$$

The fields are then obtained from:
$$
\mathbf{H} = \frac{1}{\mu} \nabla \times \mathbf{A}, \quad
\mathbf{E} = \frac{1}{j\omega\varepsilon} \nabla \times \mathbf{H},
\quad \text{(for source-free regions)}
\tag{2.56}
$$

> **核心结果**：赫兹偶极子的矢量势为 $e^{-jkr}/r$ 形式的推迟球面波，反映了电磁作用的有限传播速度。

---

## §2.12 Lorentz Reciprocity Theorem (pp. 62–65)
## §2.12 洛伦兹互易定理（Lorentz Reciprocity Theorem）

Collin derives this powerful theorem relating two sets of sources and fields in a linear medium.

> 洛伦兹互易定理是微波网络理论的重要基础，它保证了互易网络的S参数矩阵对称。

### Statement
### 定理表述（Statement）

Consider two sets of sources ($\mathbf{J}_1$, $\mathbf{M}_1$) and ($\mathbf{J}_2$, $\mathbf{M}_2$) producing fields ($\mathbf{E}_1$, $\mathbf{H}_1$) and ($\mathbf{E}_2$, $\mathbf{H}_2$) in the same linear medium. The reciprocity theorem states:

$$
\nabla \cdot (\mathbf{E}_1 \times \mathbf{H}_2 - \mathbf{E}_2 \times \mathbf{H}_1) =
\mathbf{E}_1 \cdot \mathbf{J}_2 + \mathbf{H}_2 \cdot \mathbf{M}_1 -
\mathbf{E}_2 \cdot \mathbf{J}_1 - \mathbf{H}_1 \cdot \mathbf{M}_2
\tag{2.57}
$$

### Integral Form
### 积分形式（Integral Form）

$$
\oint_S (\mathbf{E}_1 \times \mathbf{H}_2 - \mathbf{E}_2 \times \mathbf{H}_1) \cdot d\mathbf{S} =
\int_V (\mathbf{E}_1 \cdot \mathbf{J}_2 + \mathbf{H}_2 \cdot \mathbf{M}_1 -
\mathbf{E}_2 \cdot \mathbf{J}_1 - \mathbf{H}_1 \cdot \mathbf{M}_2) \, dV
\tag{2.58}
$$

### Reciprocity for a Source-Free Region
### 无源区域的互易性（Source-Free Reciprocity）

If the volume $V$ is source-free with boundary $S$:

$$
\oint_S (\mathbf{E}_1 \times \mathbf{H}_2 - \mathbf{E}_2 \times \mathbf{H}_1) \cdot d\mathbf{S} = 0
\tag{2.59}
$$

### Lorentz Reciprocity for Antennas
### 天线系统的洛伦兹互易（Lorentz Reciprocity for Antennas）

For two antennas with port currents $I_1$, $I_2$ and open-circuit voltages $V_1$, $V_2$:

$$
Z_{12} = Z_{21}
\quad \text{(mutual impedance symmetry)} \tag{2.60}
$$

**Engineering significance:**
- The **scattering matrix** of a reciprocal junction is symmetric: $S_{ij} = S_{ji}$
- All passive, linear microwave circuits made of isotropic materials are reciprocal
- Non-reciprocal devices (circulators, isolators) require anisotropic materials (ferrites) or active elements

> **工程意义**：互易性意味着 $S_{ij} = S_{ji}$，这大大简化了微波网络的测量与设计；非互易器件（如环行器）必须依赖铁氧体等各向异性材料。

---

## Summary of Key Equations (Ch. 2)
## 第2章重要公式汇总（Summary of Key Equations）

| Quantity | Equation | § Ref | Units |
|----------|----------|-------|-------|
| Faraday's law | $\nabla \times \mathbf{E} = -\partial\mathbf{B}/\partial t$ | §2.1 | — |
| Ampère's law | $\nabla \times \mathbf{H} = \mathbf{J} + \partial\mathbf{D}/\partial t$ | §2.1 | — |
| Gauss's law (E) | $\nabla \cdot \mathbf{D} = \rho_v$ | §2.1 | — |
| Gauss's law (H) | $\nabla \cdot \mathbf{B} = 0$ | §2.1 | — |
| Poynting vector | $\mathbf{S} = \mathbf{E} \times \mathbf{H}$ | §2.5 | W/m² |
| Wave equation (E) | $\nabla^2 \mathbf{E} - \gamma^2 \mathbf{E} = 0$ | §2.4 | — |
| Helmholtz eqn | $\nabla^2 \mathbf{E} + k^2 \mathbf{E} = 0$ | §2.4 | — |
| Wavenumber | $k = \omega\sqrt{\mu\varepsilon}$ | §2.4 | rad/m |
| Intrinsic impedance | $\eta = \sqrt{\mu/\varepsilon}$ | §2.7 | Ω |
| Skin depth | $\delta_s = \sqrt{2/(\omega\mu\sigma)}$ | §2.7 | m |
| Surface resistance | $R_s = 1/(\sigma\delta_s)$ | §2.7 | Ω/□ |
| Fresnel reflection | $\Gamma_\perp, \Gamma_\parallel$ | §2.8 | — |
| Brewster angle | $\theta_B = \tan^{-1}\sqrt{\varepsilon_2/\varepsilon_1}$ | §2.8 | rad |
| Vector potential solution | $\mathbf{A} = \frac{\mu}{4\pi} \int \mathbf{J} \frac{e^{-jkR}}{R} dV'$ | §2.11 | Wb/m |
| Propagation constant | $\gamma = \sqrt{j\omega\mu(\sigma + j\omega\varepsilon)}$ | §2.4 | m⁻¹ |
| Lorentz reciprocity | $\nabla\cdot(\mathbf{E}_1\times\mathbf{H}_2 - \mathbf{E}_2\times\mathbf{H}_1) = \ldots$ | §2.12 | — |

---

## Physical Constants (from §2.2)
## 物理常数（Physical Constants）

| Constant | Symbol | Value |
|----------|--------|-------|
| Speed of light in vacuum | $c_0$ | $2.99792458 \times 10^8$ m/s |
| Permeability of free space | $\mu_0$ | $4\pi \times 10^{-7}$ H/m |
| Permittivity of free space | $\varepsilon_0$ | $8.8541878176 \times 10^{-12}$ F/m |
| Intrinsic impedance of free space | $\eta_0$ | $376.7303\ \Omega$ |

---

**End of Ch. 2 notes.** Source: Collin, *Foundations for Microwave Engineering*, 2nd Ed., IEEE Press, 2000, pp. 17–70.
