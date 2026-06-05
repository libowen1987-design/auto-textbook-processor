---
chapter: 2
title: Introduction to Waves
source: Roger F. Harrington, Time-Harmonic Electromagnetic Fields, IEEE Press
pages: 37-150
---

# Chapter 2: Introduction to Waves / 波动学引论

## Section 2-1: The Wave Equation / 波动方程

**English:**

A field that is a function of both time and space coordinates can be called a wave. More precisely, we use the term **wave** to denote a solution to a **wave equation** — a particular type of differential equation that electromagnetic fields obey.

For **source-free** ($\mathbf{J} = 0$), **linear**, **homogeneous**, **isotropic** regions, Maxwell's equations in phasor form are:

$$\nabla \times \mathbf{E} = -j\omega\mu\mathbf{H} \tag{2-1a}$$

$$\nabla \times \mathbf{H} = j\omega\epsilon\mathbf{E} \tag{2-1b}$$

Taking the curl of (2-1a) and substituting from (2-1b):

$$\nabla \times \nabla \times \mathbf{E} = -j\omega\mu(\nabla \times \mathbf{H}) = -j\omega\mu(j\omega\epsilon\mathbf{E}) = \omega^2\mu\epsilon\mathbf{E}$$

Using the vector identity $\nabla \times \nabla \times \mathbf{A} = \nabla(\nabla \cdot \mathbf{A}) - \nabla^2\mathbf{A}$ and noting that $\nabla \cdot \mathbf{E} = 0$ for source-free regions:

$$\nabla^2\mathbf{E} + k^2\mathbf{E} = 0 \tag{2-3}$$

where the **wave number** (相位常数) is:

$$k = \omega\sqrt{\mu\epsilon} \tag{2-2}$$

Similarly for $\mathbf{H}$:

$$\nabla^2\mathbf{H} + k^2\mathbf{H} = 0 \tag{2-4}$$

Equations (2-3) and (2-4) are called the **vector Helmholtz equation** (矢量亥姆霍兹方程). The rectangular components satisfy the **scalar Helmholtz equation**:

$$\nabla^2\psi + k^2\psi = 0 \tag{2-7}$$

---

**Example: Uniform Plane Wave in Perfect Dielectric / 完美电介质中的均匀平面波**

For a perfect dielectric where $\sigma = 0$, $k = \omega\sqrt{\mu\epsilon}$ is real.

Consider a wave propagating in the $z$-direction with only $x$-component of $\mathbf{E}$:

$$E_x = E_0 e^{-jkz} \tag{2-9}$$

This satisfies $\nabla \cdot \mathbf{E} = 0$ and is therefore a valid EM field.

The associated magnetic field from Faraday's law:

$$j\omega\mu H_y = -\frac{\partial E_x}{\partial z} = jk E_x \Rightarrow H_y = \frac{k}{\omega\mu}E_x = \frac{E_x}{\eta} \tag{2-10}$$

where the **intrinsic impedance** (本征阻抗) of the medium is:

$$\eta = \sqrt{\frac{\mu}{\epsilon}} \tag{2-11}$$

In vacuum: $\eta_0 = \sqrt{\mu_0/\epsilon_0} \approx 120\pi \approx 377\ \Omega$ (2-12)

**Instantaneous fields (瞬时场):**

$$\mathcal{E}_x = \sqrt{2}E_0\cos(\omega t - kz)$$
$$\mathcal{H}_y = \frac{\sqrt{2}E_0}{\eta}\cos(\omega t - kz)$$

These represent a **uniform plane wave** traveling in the $+z$ direction with **phase velocity** $v_p = \omega/k = 1/\sqrt{\mu\epsilon}$.

In vacuum: $v_p = c = 3 \times 10^8$ m/s.

**中文：**

场是时间和空间坐标的函数，可以称为波。更准确地说，我们用**波**这个术语来表示一类特殊微分方程——**波动方程**——的解，电磁场服从波动方程。

对于**无源** ($\mathbf{J} = 0$)、**线性**、**均匀**、**各向同性**区域，相量形式的麦克斯韦方程为：

$$\nabla \times \mathbf{E} = -j\omega\mu\mathbf{H} \tag{2-1a}$$

$$\nabla \times \mathbf{H} = j\omega\epsilon\mathbf{E} \tag{2-1b}$$

取(2-1a)的旋度并代入(2-1b)：

$$\nabla \times \nabla \times \mathbf{E} = -j\omega\mu(\nabla \times \mathbf{H}) = -j\omega\mu(j\omega\epsilon\mathbf{E}) = \omega^2\mu\epsilon\mathbf{E}$$

利用向量恒等式 $\nabla \times \nabla \times \mathbf{A} = \nabla(\nabla \cdot \mathbf{A}) - \nabla^2\mathbf{A}$，并注意无源区域 $\nabla \cdot \mathbf{E} = 0$：

$$\nabla^2\mathbf{E} + k^2\mathbf{E} = 0 \tag{2-3}$$

其中**波数**为：

$$k = \omega\sqrt{\mu\epsilon} \tag{2-2}$$

对 $\mathbf{H}$ 类似：

$$\nabla^2\mathbf{H} + k^2\mathbf{H} = 0 \tag{2-4}$$

方程(2-3)和(2-4)称为**矢量亥姆霍兹方程**。直角分量满足**标量亥姆霍兹方程**：

$$\nabla^2\psi + k^2\psi = 0 \tag{2-7}$$

---

## Section 2-2: Waves in Perfect Dielectrics / 完美电介质中的波

**English:**

**Uniform plane wave** propagation in a perfect dielectric:

The wave propagates without attenuation ($\alpha = 0$) with **propagation constant**:

$$\gamma = j\beta = j\omega\sqrt{\mu\epsilon} \tag{in perfect dielectric}$$

**Phase velocity (相速度):**

$$v_p = \frac{\omega}{\beta} = \frac{1}{\sqrt{\mu\epsilon}}$$

**Wavelength (波长):**

$$\lambda = \frac{2\pi}{\beta} = \frac{v_p}{f}$$

**Intrinsic impedance (本征阻抗):**

$$\eta = \sqrt{\frac{\mu}{\epsilon}} = \eta_0\sqrt{\frac{\mu_r}{\epsilon_r}}$$

**Wave impedance** between $\mathcal{E}$ and $\mathcal{H}$ components is $\eta$ for a plane wave propagating in $+z$.

**Energy densities:**
$$w_e = \frac{1}{2}\epsilon|E|^2 \quad w_m = \frac{1}{2}\mu|H|^2$$

For a perfect plane wave: $w_e = w_m$ (equal electric and magnetic energy densities).

**Time-average Poynting vector (时间平均坡印廷矢量):**

$$\mathbf{S}_\text{avg} = \frac{1}{2}\text{Re}\{\mathbf{E} \times \mathbf{H}^*\} = \frac{|E|^2}{2\eta}\hat{\mathbf{z}} \quad \text{W/m}^2$$

**中文：**

**均匀平面波**在完美电介质中的传播：

波在传播过程中无衰减 ($\alpha = 0$)，**传播常数**为：

$$\gamma = j\beta = j\omega\sqrt{\mu\epsilon}$$

**相速度：**

$$v_p = \frac{\omega}{\beta} = \frac{1}{\sqrt{\mu\epsilon}}$$

**波长：**

$$\lambda = \frac{2\pi}{\beta} = \frac{v_p}{f}$$

**本征阻抗：**

$$\eta = \sqrt{\frac{\mu}{\epsilon}} = \eta_0\sqrt{\frac{\mu_r}{\epsilon_r}}$$

$\mathcal{E}$ 和 $\mathcal{H}$ 分量之间的波阻抗在沿 $+z$ 方向传播的平面波中为 $\eta$。

**能量密度：**
$$w_e = \frac{1}{2}\epsilon|E|^2 \quad w_m = \frac{1}{2}\mu|H|^2$$

对于完美平面波：$w_e = w_m$（电场能和磁场能密度相等）。

---

## Section 2-3: Intrinsic Wave Constants / 本征波常数

**English:**

The **intrinsic wave constants** characterize wave propagation in a medium:

$$\gamma = \sqrt{j\omega\mu(\sigma + j\omega\epsilon)}$$

For **lossless media** ($\sigma = 0$):
$$\gamma = j\omega\sqrt{\mu\epsilon} = j\beta, \quad \alpha = 0$$

For **low-loss dielectrics** ($\sigma \ll \omega\epsilon$):
$$\alpha \approx \frac{\sigma}{2}\sqrt{\frac{\mu}{\epsilon}} \quad \text{(attenuation constant)}$$
$$\beta \approx \omega\sqrt{\mu\epsilon} \quad \text{(phase constant)}$$

For **good conductors** ($\sigma \gg \omega\epsilon$):
$$\gamma = (1+j)\sqrt{\frac{\omega\mu\sigma}{2}} = \frac{1+j}{\delta_s}$$

where **skin depth** (皮肤深度) $\delta_s = \sqrt{2/(\omega\mu\sigma)}$.

**Intrinsic impedance:**

$$\eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\epsilon}}$$

For lossless media: $\eta$ is real and equal to $\sqrt{\mu/\epsilon}$.

For lossy media: $\eta = |\eta|e^{j\theta_\eta}$ with phase shift.

**Dispersion** occurs when $\gamma$ (and thus $v_p$) depends on frequency. This happens in:
- Conductors at all frequencies
- Dielectrics near absorption resonances
- Plasmas (electron gas)

**Group velocity (群速度):**

$$v_g = \frac{d\omega}{d\beta}$$

In nondispersive media ($v_p$ constant): $v_g = v_p$.
In dispersive media: $v_g \neq v_p$.

**中文：**

**本征波常数**表征波在介质中的传播特性：

$$\gamma = \sqrt{j\omega\mu(\sigma + j\omega\epsilon)}$$

对于**无损介质** ($\sigma = 0$)：
$$\gamma = j\omega\sqrt{\mu\epsilon} = j\beta, \quad \alpha = 0$$

对于**低损耗电介质** ($\sigma \ll \omega\epsilon$)：
$$\alpha \approx \frac{\sigma}{2}\sqrt{\frac{\mu}{\epsilon}} \quad \text{（衰减常数）}$$
$$\beta \approx \omega\sqrt{\mu\epsilon} \quad \text{（相位常数）}$$

对于**良导体** ($\sigma \gg \omega\epsilon$)：
$$\gamma = (1+j)\sqrt{\frac{\omega\mu\sigma}{2}} = \frac{1+j}{\delta_s}$$

其中**皮肤深度** $\delta_s = \sqrt{2/(\omega\mu\sigma)}$。

**本征阻抗：**

$$\eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\epsilon}}$$

对于无损介质：$\eta$ 为实数，等于 $\sqrt{\mu/\epsilon}$。

对于有损耗介质：$\eta = |\eta|e^{j\theta_\eta}$，存在相位偏移。

---

## Section 2-4: Waves in Lossy Matter / 有损耗物质中的波

**English:**

For **general lossy media**, the propagation constant $\gamma = \alpha + j\beta$:

$$\alpha = \omega\sqrt{\frac{\mu\epsilon}{2}\left(\sqrt{1 + \left(\frac{\sigma}{\omega\epsilon}\right)^2} - 1\right)}$$

$$\beta = \omega\sqrt{\frac{\mu\epsilon}{2}\left(\sqrt{1 + \left(\frac{\sigma}{\omega\epsilon}\right)^2} + 1\right)}$$

Define **loss tangent** (损耗角正切) $\tan\delta = \sigma/(\omega\epsilon)$:

$$\gamma = j\omega\sqrt{\mu\epsilon}\sqrt{1 - j\tan\delta}$$

For $\tan\delta \ll 1$ (low loss):
$$\alpha \approx \frac{\omega\sqrt{\mu\epsilon}}{2}\tan\delta$$
$$\beta \approx \omega\sqrt{\mu\epsilon}\left(1 + \frac{\tan^2\delta}{8}\right)$$

**Complex permittivity representation:**

$$\epsilon_c = \epsilon' - j\epsilon'' = \epsilon'\left(1 - j\tan\delta\right)$$

where $\epsilon' = \epsilon$ and $\epsilon'' = \sigma/\omega$.

The field in a lossy medium decays as $e^{-\alpha z}$ while oscillating as $e^{-j\beta z}$.

**Penetration depth (穿透深度):**

$$\delta = \frac{1}{\alpha} \quad \text{(distance for field to decay to } 1/e \text{)}$$

**Complex wave impedance:**

$$\eta = \sqrt{\frac{j\omega\mu}{\sigma + j\omega\epsilon}} = |\eta|e^{j\phi}$$

where $\phi = \tan^{-1}\left(\frac{\sigma}{\omega\epsilon}\right)/2$ for low-loss media.

**Phase difference between E and H:**
In lossy media, $\mathbf{E}$ and $\mathbf{H}$ are not in phase. The phase difference is $\phi$, where $\tan(2\phi) = \sigma/(\omega\epsilon)$.

**中文：**

对于**一般有损耗介质**，传播常数 $\gamma = \alpha + j\beta$：

$$\alpha = \omega\sqrt{\frac{\mu\epsilon}{2}\left(\sqrt{1 + \left(\frac{\sigma}{\omega\epsilon}\right)^2} - 1\right)}$$

$$\beta = \omega\sqrt{\frac{\mu\epsilon}{2}\left(\sqrt{1 + \left(\frac{\sigma}{\omega\epsilon}\right)^2} + 1\right)}$$

定义**损耗角正切** $\tan\delta = \sigma/(\omega\epsilon)$：

$$\gamma = j\omega\sqrt{\mu\epsilon}\sqrt{1 - j\tan\delta}$$

对于 $\tan\delta \ll 1$（低损耗）：
$$\alpha \approx \frac{\omega\sqrt{\mu\epsilon}}{2}\tan\delta$$
$$\beta \approx \omega\sqrt{\mu\epsilon}\left(1 + \frac{\tan^2\delta}{8}\right)$$

**复介电常数表示：**

$$\epsilon_c = \epsilon' - j\epsilon'' = \epsilon'\left(1 - j\tan\delta\right)$$

其中 $\epsilon' = \epsilon$，$\epsilon'' = \sigma/\omega$。

场在有损耗介质中以 $e^{-\alpha z}$ 衰减，同时以 $e^{-j\beta z}$ 振荡。

---

## Section 2-5: Reflection of Waves / 波的反射

**English:**

When a plane wave encounters an **interface** between two media, part is reflected and part is transmitted.

Consider a plane wave normally incident on a planar boundary at $z = 0$ between medium 1 ($z < 0$) and medium 2 ($z > 0$).

**Reflection coefficient (反射系数):**

$$\Gamma = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1} \tag{2-44}$$

**Transmission coefficient (透射系数):**

$$T = \frac{2\eta_2}{\eta_2 + \eta_1} = 1 + \Gamma \tag{2-45}$$

The total field in medium 1:
$$E_1 = E_i e^{-j\beta_1 z} + \Gamma E_i e^{+j\beta_1 z}$$

The transmitted field in medium 2:
$$E_2 = T E_i e^{-j\beta_2 z}$$

**Standing wave (驻波):**

When $|\Gamma| = 1$ (e.g., perfect conductor), the incident and reflected waves combine to form a standing wave pattern:

$$|E| = |E_i||1 + \Gamma e^{j2\beta_1 z}|$$

**Standing wave ratio (驻波比):**

$$SWR = \frac{1 + |\Gamma|}{1 - |\Gamma|} \tag{2-47}$$

**Power flow (功率流):**

$$P_\text{avg} = \frac{|E_i|^2}{2\eta_1}(1 - |\Gamma|^2) \quad \text{(in +z direction)}$$

**Oblique incidence (斜入射):** For oblique incidence at angle $\theta_i$:

**Snell's law:**
$$\frac{\sin\theta_i}{\sin\theta_t} = \frac{k_2}{k_1} = \frac{n_2}{n_1}$$

**Fresnel reflection coefficients (for parallel/perp polarization):**
$$\Gamma_\perp = \frac{\eta_2\cos\theta_i - \eta_1\cos\theta_t}{\eta_2\cos\theta_i + \eta_1\cos\theta_t}$$
$$\Gamma_\parallel = \frac{\eta_2\cos\theta_t - \eta_1\cos\theta_i}{\eta_2\cos\theta_t + \eta_1\cos\theta_i}$$

**Brewster angle (布鲁斯特角):** For $\Gamma_\parallel = 0$:
$$\theta_B = \tan^{-1}\sqrt{\frac{\epsilon_2\mu_1}{\epsilon_1\mu_2}}$$

**Critical angle (临界角):** For total internal reflection when propagating from higher to lower index:
$$\theta_c = \sin^{-1}\sqrt{\frac{\epsilon_2\mu_1}{\epsilon_1\mu_2}}$$

**中文：**

当平面波遇到两种介质之间的**界面**时，部分反射，部分透射。

考虑在 $z = 0$ 处平面边界上的法向入射波，边界两侧分别为介质1 ($z < 0$) 和介质2 ($z > 0$)。

**反射系数：**

$$\Gamma = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1} \tag{2-44}$$

**透射系数：**

$$T = \frac{2\eta_2}{\eta_2 + \eta_1} = 1 + \Gamma \tag{2-45}$$

介质1中的总场：
$$E_1 = E_i e^{-j\beta_1 z} + \Gamma E_i e^{+j\beta_1 z}$$

介质2中的透射场：
$$E_2 = T E_i e^{-j\beta_2 z}$$

**驻波比：**

$$SWR = \frac{1 + |\Gamma|}{1 - |\Gamma|} \tag{2-47}$$

---

## Section 2-6: Transmission-line Concepts / 传输线概念

**English:**

Transmission lines are **distributed parameter** circuits characterized by per-unit-length parameters $R, L, G, C$.

**Telegrapher's equations (电报员方程):**

$$\frac{\partial V}{\partial z} = -RI - L\frac{\partial I}{\partial t}$$
$$\frac{\partial I}{\partial z} = -GV - C\frac{\partial V}{\partial t}$$

In sinusoidal steady state ($j\omega$):

$$\frac{dV}{dz} = -\gamma V \quad \frac{dI}{dz} = -\gamma I$$

where:
- $\gamma = \sqrt{(R + j\omega L)(G + j\omega C)}$ (propagation constant)
- $Z_0 = \sqrt{(R + j\omega L)/(G + j\omega C)}$ (characteristic impedance)

**Wave propagation on transmission lines:**

$$V(z) = V^+ e^{-\gamma z} + V^- e^{+\gamma z}$$
$$I(z) = \frac{V^+}{Z_0}e^{-\gamma z} - \frac{V^-}{Z_0}e^{+\gamma z}$$

**Reflection coefficient at load:**
$$\Gamma_L = \frac{V^-}{V^+} = \frac{Z_L - Z_0}{Z_L + Z_0}$$

**Input impedance at distance $l$ from load:**
$$Z_in(l) = Z_0 \frac{1 + \Gamma_L e^{-2\gamma l}}{1 - \Gamma_L e^{-2\gamma l}}$$

**Special cases:**
- **Lossless line** ($R = G = 0$): $\gamma = j\beta$, $Z_0$ real
- **Matched line** ($\Gamma_L = 0$): No reflections, $Z_in = Z_0$
- **Short circuit** ($Z_L = 0$): $\Gamma_L = -1$, $Z_in = Z_0 \tanh(\gamma l)$
- **Open circuit** ($Z_L = \infty$): $\Gamma_L = +1$, $Z_in = Z_0 \coth(\gamma l)$

**Power on transmission line:**
$$P(z) = \frac{|V^+|^2}{2Z_0}e^{-2\alpha z}(1 - |\Gamma|^2)$$

**中文：**

传输线是具有**分布参数**的电路，以单位长度参数 $R, L, G, C$ 为特征。

**电报员方程：**

$$\frac{\partial V}{\partial z} = -RI - L\frac{\partial I}{\partial t}$$
$$\frac{\partial I}{\partial z} = -GV - C\frac{\partial V}{\partial t}$$

正弦稳态下 ($j\omega$)：

$$\frac{dV}{dz} = -\gamma V \quad \frac{dI}{dz} = -\gamma I$$

其中：
- $\gamma = \sqrt{(R + j\omega L)(G + j\omega C)}$（传播常数）
- $Z_0 = \sqrt{(R + j\omega L)/(G + j\omega C)}$（特性阻抗）

**负载处反射系数：**
$$\Gamma_L = \frac{V^-}{V^+} = \frac{Z_L - Z_0}{Z_L + Z_0}$$

---

## Section 2-7: Waveguide Concepts / 波导概念

**English:**

Waveguides are **hollow conducting structures** that guide electromagnetic waves at microwave frequencies.

**Parallel-plate waveguide:** Two parallel conducting plates.

For **TEM mode** (Transverse ElectroMagnetic — requires $\epsilon$ and $\mu$ uniform and finite, not possible in hollow waveguide):

$$E_z = 0, \quad H_z = 0, \quad \gamma = j\beta = j\omega\sqrt{\mu\epsilon}$$

**TE/TM modes:** Higher order modes with $E_z$ or $H_z$ nonzero.

**Rectangular waveguide:** Cross-section $a \times b$ with $a > b$.

**TE$_{mn}$ modes** have $H_z \neq 0$, $E_z = 0$:
$$h_z = H_0 \sin\left(\frac{m\pi x}{a}\right)\sin\left(\frac{n\pi y}{b}\right)e^{-\gamma z}$$

**Cutoff frequency (截止频率):**

$$f_c = \frac{c}{2}\sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}$$

Only frequencies $f > f_c$ propagate; below $f_c$, the mode is **evanescent** with real $\alpha$ and $\beta = 0$.

**Dominant mode (主模):** Lowest cutoff frequency mode.
- For rectangular waveguide: **TE$_{10}$** mode with $f_c = c/(2a)$.

**Phase velocity:** $v_p = \omega/\beta > c$ (above cutoff)
**Group velocity:** $v_g = d\omega/d\beta < c$
**Wave impedance:**
$$\eta_{TE} = \frac{\eta}{\cos\theta_g}, \quad \eta_{TM} = \eta\cos\theta_g$$
where $\sin\theta_g = f_c/f$ and $\eta = \sqrt{\mu/\epsilon}$.

**Attenuation in waveguides:**
- Conductor losses: power dissipated in waveguide walls
- Dielectric losses: power dissipated in filling medium

**中文：**

波导是**空心导电结构**，在微波频率下引导电磁波。

**矩形波导：** 截面 $a \times b$，其中 $a > b$。

**TE$_{mn}$ 模式** 具有 $H_z \neq 0$, $E_z = 0$：
$$h_z = H_0 \sin\left(\frac{m\pi x}{a}\right)\sin\left(\frac{n\pi y}{b}\right)e^{-\gamma z}$$

**截止频率：**

$$f_c = \frac{c}{2}\sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}$$

只有 $f > f_c$ 的频率才能传播；低于 $f_c$ 时，模式为**倏逝波**，具有实数 $\alpha$ 和 $\beta = 0$。

**主模：** 最低截止频率模式。
- 对于矩形波导：**TE$_{10}$** 模式，$f_c = c/(2a)$。

---

## Section 2-9: Radiation / 辐射

**English:**

**Radiation** is the process by which electromagnetic energy is converted to energy that propagates freely in space (far field).

**Hertzian dipole (赫兹偶极子):** A short current element of length $l$ carrying current $I$.

**Far-field radiation pattern:**
$$E_\theta = \frac{j\eta I_0 l}{2\pi r}e^{-jkr}\sin\theta$$
$$H_\phi = \frac{j I_0 l}{2\pi r}e^{-jkr}\sin\theta$$

The fields are **transverse** ($\mathbf{E} \perp \mathbf{H} \perp \hat{r}$).

**Radiation resistance (辐射电阻):**
$$R_\text{rad} = \frac{2\pi}{3}\left(\frac{Il}{\lambda}\right)^2 \quad \Omega$$

Power radiated: $P_\text{rad} = \frac{1}{2}|I|^2 R_\text{rad}$

**Directivity (方向性):**
$$D = \frac{4\pi}{\Omega_\text{rad}}$$

where $\Omega_\text{rad}$ is the radiation solid angle.

For Hertzian dipole: $D = 1.5$ (maximum)

**Antenna gain:**
$$G = \eta_e D$$
where $\eta_e$ is the radiation efficiency.

**Array factor (阵列因子):** For $N$ isotropic elements with spacing $d$ and phase shift $\psi$:

$$AF = \frac{\sin(N\psi/2)}{\sin(\psi/2)}$$

where $\psi = kd\cos\theta + \beta_\text{elem}$.

**中文：**

**辐射**是电磁能量转换为在空间中自由传播的能量（远区场）的过程。

**赫兹偶极子：** 长度为 $l$、电流为 $I$ 的短电流元。

**远区辐射场：**
$$E_\theta = \frac{j\eta I_0 l}{2\pi r}e^{-jkr}\sin\theta$$
$$H_\phi = \frac{j I_0 l}{2\pi r}e^{-jkr}\sin\theta$$

场是**横向**的 ($\mathbf{E} \perp \mathbf{H} \perp \hat{r}$)。

**辐射电阻：**
$$R_\text{rad} = \frac{2\pi}{3}\left(\frac{Il}{\lambda}\right)^2 \quad \Omega$$

---

## Section 2-10: Antenna Concepts / 天线概念

**English:**

An **antenna** is a structure that couples guided waves (transmission lines) to free-space waves and vice versa.

**Antenna parameters:**
- **Input impedance:** $Z_A = R_A + jX_A$
- **Radiation efficiency:** $\eta_e = R_\text{rad}/(R_\text{rad} + R_\text{loss})$
- **Bandwidth:** frequency range over which VSWR < specified value
- **Polarization:** orientation of $\mathbf{E}$ field vector

**Reciprocity theorem:** An antenna has the same radiation pattern and impedance when used for transmitting or receiving.

**Linear wire antennas:**
- **Hertzian dipole:** $l \ll \lambda$ (short dipole)
- **Half-wave dipole:** $l = \lambda/2$ (resonant, $R \approx 73\ \Omega$)
- **Full-wave dipole:** $l = \lambda$ ($R \approx 90\ \Omega$)
- **Yagi-Uda antenna:** parasitic directors and reflectors

**Moment method (MoM) analysis:** Used to solve for current distribution on wire antennas by converting integral equation to matrix equation.

**Frill (周线) current:** Current distribution on dipole arms found by solving Pocklington's integral equation.

**Folded dipole:** $R \approx 4 \times$ that of simple dipole ($\approx 300\ \Omega$).

**Aperture antennas:** Horn antennas, parabolic reflectors, microstrip patches.

**Array theory:** Multiple antenna elements arranged to achieve:
- Higher directivity (narrower beam)
- Electronic beam steering (phased arrays)

**Phased array:** Elements with variable phase shifters for beam steering without mechanical movement.

**中文：**

**天线**是将在传输线中传输的导波与自由空间波相互耦合的结构。

**天线参数：**
- **输入阻抗：** $Z_A = R_A + jX_A$
- **辐射效率：** $\eta_e = R_\text{rad}/(R_\text{rad} + R_\text{loss})$
- **带宽：** VSWR < 规定值的频率范围
- **极化：** $\mathbf{E}$ 场矢量的方向

**互易定理：** 天线在发射和接收时具有相同的辐射图和阻抗。

**线性导线天线：**
- **赫兹偶极子：** $l \ll \lambda$（短偶极子）
- **半波偶极子：** $l = \lambda/2$（谐振，$R \approx 73\ \Omega$）

---

## Section 2-11: On Waves in General / 波的一般性质

**English:**

The wave equation $\nabla^2\psi + k^2\psi = 0$ admits **plane wave** solutions:

$$\psi(\mathbf{r}) = \psi_0 e^{-j\mathbf{k} \cdot \mathbf{r}}$$

where $\mathbf{k}$ is the **wave vector** with $|\mathbf{k}| = k = \omega\sqrt{\mu\epsilon}$.

**Dispersion relations:**
- Non-dispersive: $v_p = \omega/k$ constant (vacuum, air at STP)
- Dispersive: $v_p$ varies with $\omega$ (waveguides, plasmas, dielectrics near resonance)

**Phase velocity:** $v_p = \omega/k$
**Group velocity:** $v_g = d\omega/dk$

**Wave types:**
- **Uniform plane wave:** constant amplitude and phase over equiphase planes
- **Non-uniform plane wave:** amplitude varies over equiphase planes
- **Evanescent wave:** decaying (not propagating) solution, $\beta = 0$, real $\alpha$
- **Surface wave:** bound to interface, decays exponentially away from surface
- **Leaky wave:** partially radiative, complex $\beta$

**Wave packet:** A localized group of waves in space, travels at group velocity.

**Phase front:** Surface of constant phase, propagates at phase velocity.

**Boundary conditions (边界条件):**
For perfect electric conductors (PEC):
$$\hat{n} \times \mathbf{E} = 0, \quad \hat{n} \cdot \mathbf{D} = \rho_s$$

For perfect magnetic conductors (PMC):
$$\hat{n} \times \mathbf{H} = 0, \quad \hat{n} \cdot \mathbf{B} = 0$$

**Uniqueness theorem:** A field in a region is uniquely determined by:
- Boundary values of tangential $\mathbf{E}$ or $\mathbf{H}$, OR
- Values at interior sources

**中文：**

波动方程 $\nabla^2\psi + k^2\psi = 0$ 的**平面波**解：

$$\psi(\mathbf{r}) = \psi_0 e^{-j\mathbf{k} \cdot \mathbf{r}}$$

其中 $\mathbf{k}$ 是**波矢量**，$|\mathbf{k}| = k = \omega\sqrt{\mu\epsilon}$。

**色散关系：**
- 非色散：$v_p = \omega/k$ 为常数（真空、STP下的空气）
- 色散：$v_p$ 随 $\omega$ 变化（波导、等离子体、谐振附近的电介质）

**相速度：** $v_p = \omega/k$
**群速度：** $v_g = d\omega/dk$

**波的类型：**
- **均匀平面波：** 等相位面上振幅和相位恒定
- **非均匀平面波：** 等相位面上振幅变化
- **倏逝波：** 衰减（非传播）解，$\beta = 0$，实数 $\alpha$
- **表面波：** 束缚于界面，沿界面传播，远离界面指数衰减
- **泄漏波：** 部分辐射，$\beta$ 为复数

---

