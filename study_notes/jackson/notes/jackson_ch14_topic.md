# Jackson Ch14: Radiation by Moving Charges / 运动电荷的辐射

> **中英双语版**

## Overview / 概述
Electromagnetic radiation from arbitrarily moving charged particles. Lienard-Wiechert potentials, fields, and radiated power.
任意运动带电粒子的电磁辐射。利埃纳-维谢尔特势、场以及辐射功率。

---

## The Lienard-Wiechert Potentials / 利埃纳-维谢尔特势

### Retarded Potentials for a Point Charge / 点电荷的推迟势

For a point charge $q$ moving along $\mathbf{r}_0(t)$ with velocity $\mathbf{v}(t) = \dot{\mathbf{r}}_0(t)$ / 对于沿 $\mathbf{r}_0(t)$ 运动、速度为 $\mathbf{v}(t) = \dot{\mathbf{r}}_0(t)$ 的点电荷 $q$：

**Lienard-Wiechert potentials** (the fundamental solution) / 利埃纳-维谢尔特势（基本解）：

$$
\Phi(\mathbf{r}, t) = \frac{q}{4\pi\epsilon_0} \left[ \frac{1}{(1 - \boldsymbol{\beta} \cdot \mathbf{n}) R} \right]_{\text{ret}}
$$

$$
\mathbf{A}(\mathbf{r}, t) = \frac{\mu_0 q}{4\pi} \left[ \frac{\mathbf{v}}{(1 - \boldsymbol{\beta} \cdot \mathbf{n}) R} \right]_{\text{ret}}
$$

where / 其中：
- $\mathbf{R} = \mathbf{r} - \mathbf{r}_0(t_{\text{ret}})$, $R = |\mathbf{R}|$
- $\mathbf{n} = \mathbf{R}/R$
- $\boldsymbol{\beta} = \mathbf{v}/c$
- $[\ldots]_{\text{ret}}$ = evaluated at retarded time $t_{\text{ret}} = t - R(t_{\text{ret}})/c$ / 在推迟时间 $t_{\text{ret}} = t - R(t_{\text{ret}})/c$ 处取值

### Four-vector Form / 四矢量形式

$$
A^\alpha(x) = \frac{q}{4\pi\epsilon_0 c} \frac{U^\alpha}{U \cdot (x - x_0(\tau))}
$$

where $U^\alpha = (\gamma c, \gamma \mathbf{v})$ is the 4-velocity.
其中 $U^\alpha = (\gamma c, \gamma \mathbf{v})$ 为四速度。

---

## Electric and Magnetic Fields of a Moving Point Charge / 运动点电荷的电场与磁场

### Heaviside-Feynman Fields (Jefimenko form) / 亥维赛-费曼场（杰斐缅科形式）

$$
\mathbf{E}(\mathbf{r}, t) = \frac{q}{4\pi\epsilon_0} \left[ \frac{\mathbf{n} - \boldsymbol{\beta}}{\gamma^2 (1 - \boldsymbol{\beta} \cdot \mathbf{n})^3 R^2} \right]_{\text{ret}} + \frac{q}{4\pi\epsilon_0 c} \left[ \frac{\mathbf{n} \times [(\mathbf{n} - \boldsymbol{\beta}) \times \dot{\boldsymbol{\beta}}]}{(1 - \boldsymbol{\beta} \cdot \mathbf{n})^3 R} \right]_{\text{ret}}
$$

$$
\mathbf{B}(\mathbf{r}, t) = \frac{1}{c} \mathbf{n} \times \mathbf{E}_{\text{ret}}
$$

### Two Terms (Physically) / 两项的物理含义

1. **Velocity field / 速度场** ($\propto 1/R^2$): self-field of a uniformly moving charge; no radiation / 匀速运动电荷的自场；不辐射
2. **Acceleration field / 加速度场** ($\propto 1/R$): radiation field; depends on $\dot{\boldsymbol{\beta}}$ / 辐射场；依赖于 $\dot{\boldsymbol{\beta}}$

### Key Fact / 关键事实：
The radiation field is transverse to $\mathbf{n}$ and $\propto 1/R$ → energy flux to infinity.
辐射场横向于 $\mathbf{n}$，且 $\propto 1/R$ → 能量通量传播至无穷远。

---

## Radiated Power from an Accelerated Charge / 加速电荷的辐射功率

### Larmor's Formula (non-relativistic) / 拉莫尔公式（非相对论）

$$
P = \frac{q^2 a^2}{6\pi \epsilon_0 c^3} = \frac{q^2}{6\pi\epsilon_0 c} \dot{\beta}^2
$$

### Relativistic Generalization (Liénard) / 相对论推广（利埃纳）

$$
P = \frac{q^2}{6\pi\epsilon_0 c} \gamma^6 \left[ (\dot{\boldsymbol{\beta}})^2 - (\boldsymbol{\beta} \times \dot{\boldsymbol{\beta}})^2 \right]
$$

Or equivalently / 等价形式：

$$
P = \frac{q^2}{6\pi\epsilon_0 c} \left[ \gamma^4 \dot{\beta}_\parallel^2 + \gamma^2 \dot{\beta}_\perp^2 \right]
$$

where $\dot{\boldsymbol{\beta}}_\parallel$ is parallel to $\boldsymbol{\beta}$, $\dot{\boldsymbol{\beta}}_\perp$ is perpendicular.
其中 $\dot{\boldsymbol{\beta}}_\parallel$ 平行于 $\boldsymbol{\beta}$，$\dot{\boldsymbol{\beta}}_\perp$ 垂直于 $\boldsymbol{\beta}$。

### Angular Distribution / 角分布

$$
\frac{dP}{d\Omega} = \frac{q^2}{16\pi^2\epsilon_0 c} \frac{|\mathbf{n} \times [(\mathbf{n} - \boldsymbol{\beta}) \times \dot{\boldsymbol{\beta}}]|^2}{(1 - \boldsymbol{\beta} \cdot \mathbf{n})^5}
$$

---

## Relativistic Four-Vector Formulation / 相对论四矢量表述

### Larmor's Formula in Covariant Form / 拉莫尔公式的协变形式

Four-momentum radiated per unit proper time / 单位固有时辐射的四动量：

$$
\frac{dP}{d\tau} = \frac{q^2}{6\pi\epsilon_0 c^3} \frac{dU_\alpha}{d\tau} \frac{dU^\alpha}{d\tau}
$$

### Invariant / 不变式：

$$
\frac{dU_\alpha}{d\tau} \frac{dU^\alpha}{d\tau} = c^2 \left[ \gamma^4 \dot{\beta}^2 - (\boldsymbol{\beta} \times \dot{\boldsymbol{\beta}})^2 \right]
$$

---

## Synchrotron Radiation / 同步辐射

### Circular Motion with $\beta \perp \dot{\beta}$, $\beta \approx 1$ / $\beta \perp \dot{\beta}$ 的圆周运动，$\beta \approx 1$

**Total power / 总功率**：

$$
P = \frac{q^2}{6\pi\epsilon_0 c} \gamma^4 \dot{\beta}_\perp^2 = \frac{q^2}{6\pi\epsilon_0 c} \gamma^4 \frac{v^4}{c^2 \rho^2}
$$

For a circular accelerator ($\rho$ = radius) / 对于圆形加速器（$\rho$ 为半径）：

$$
P = \frac{q^2 c}{6\pi\epsilon_0} \frac{\beta^4 \gamma^4}{\rho^2} \approx \frac{e^2 c}{6\pi\epsilon_0} \frac{\gamma^4}{\rho^2} \quad (\beta \approx 1)
$$

### Angular and Spectral Distribution / 角分布与频谱分布

Beaming / 束流效应：radiation concentrated in a narrow cone of half-angle $\theta_c \sim 1/\gamma$ / 辐射集中在半角 $\theta_c \sim 1/\gamma$ 的窄锥内

Angular distribution / 角分布：

$$
\frac{dP}{d\Omega} \approx \frac{2q^2 \gamma^6 \dot{\beta}_\perp^2}{\pi\epsilon_0 c} \frac{1 + (\gamma\psi)^2 - (\gamma\psi)^4}{[1 + (\gamma\psi)^2]^5}
$$

where $\psi$ is the angle from the instantaneous velocity direction.
其中 $\psi$ 为偏离瞬时速度方向的角度。

### Critical Frequency / 临界频率

$$
\omega_c = \frac{3}{2} \frac{c \gamma^3}{\rho}
$$

Above $\omega_c$ the spectrum falls off exponentially.
高于 $\omega_c$ 时频谱呈指数衰减。

---

## Radiation from a Charged Particle with Collinear Velocity and Acceleration / 速度与加速度共线的带电粒子的辐射

### Linear Accelerator (linear motion with $\boldsymbol{\beta} \parallel \dot{\boldsymbol{\beta}}$) / 直线加速器（$\boldsymbol{\beta} \parallel \dot{\boldsymbol{\beta}}$ 的直线运动）

**Total power / 总功率**：

$$
P = \frac{q^2}{6\pi\epsilon_0 c} \gamma^6 \dot{\beta}^2
$$

**Angular distribution / 角分布**：

$$
\frac{dP}{d\Omega} = \frac{q^2 \dot{\beta}^2}{16\pi^2\epsilon_0 c} \frac{\sin^2\theta}{(1 - \beta\cos\theta)^5}
$$

where $\theta$ is the angle from the acceleration direction.
其中 $\theta$ 为偏离加速度方向的角度。

**Beaming / 束流效应**：radiation peaks in the forward direction at $\theta_{\text{max}} \approx 1/(2\gamma)$ for $\gamma \gg 1$ / 当 $\gamma \gg 1$ 时，辐射在前向 $\theta_{\text{max}} \approx 1/(2\gamma)$ 处达到峰值

---

## 14.8 – Frequency Spectrum of Radiation / 辐射的频谱

### Fourier Transform of Radiated Fields / 辐射场的傅里叶变换

Energy radiated per unit solid angle per unit frequency / 单位立体角单位频率的辐射能量：

$$
\frac{d^2 I}{d\Omega d\omega} = \frac{q^2}{16\pi^3\epsilon_0 c} \left| \int_{-\infty}^{\infty} \frac{\mathbf{n} \times [(\mathbf{n} - \boldsymbol{\beta}) \times \dot{\boldsymbol{\beta}}]}{(1 - \boldsymbol{\beta} \cdot \mathbf{n})^2} e^{i\omega(t_{\text{ret}})} dt_{\text{ret}} \right|^2
$$

### Alternative form (using integration by parts) / 等价形式（分部积分）：

$$
\frac{d^2 I}{d\Omega d\omega} = \frac{q^2 \omega^2}{16\pi^3\epsilon_0 c} \left| \int_{-\infty}^{\infty} \mathbf{n} \times [\mathbf{n} \times \boldsymbol{\beta}] \, e^{i\omega(t_{\text{ret}})} dt_{\text{ret}} \right|^2
$$

---

## Thomson Scattering / 汤姆孙散射

### Scattering from a Free Electron / 自由电子的散射

Differential cross section / 微分截面：

$$
\frac{d\sigma}{d\Omega} = r_e^2 \sin^2\Theta
$$

where $\Theta$ is the angle between scattered polarization and observation direction.
其中 $\Theta$ 为散射极化方向与观测方向之间的夹角。

**Total Thomson cross section / 总汤姆孙截面**：

$$
\sigma_T = \frac{8\pi}{3} r_e^2 \approx 6.65 \times 10^{-29} \,\text{m}^2
$$

---

## Scattering from Bound Electrons (Rayleigh Scattering) / 束缚电子散射（瑞利散射）

### Low frequency ($\omega \ll \omega_0$) / 低频（$\omega \ll \omega_0$）：

$$
\sigma \propto \left( \frac{\omega}{\omega_0} \right)^4 r_e^2
$$

Rayleigh's $1/\lambda^4$ law → sky is blue.
瑞利 $1/\lambda^4$ 定律 → 天空呈蓝色。

---

## 14.12 – Coherent and Incoherent Scattering / 相干与不相干散射

### Coherent Scattering / 相干散射
- Phases add constructively → $d\sigma/d\Omega \propto N^2$ (for $N$ scatterers) / 相位同向叠加，$N$ 个散射体
- Requires $\lambda \gg$ spacing → X-rays from crystals, scattering from molecules / 需要 $\lambda \gg$ 间距 → 晶体X射线衍射、分子散射

### Incoherent Scattering / 不相干散射
- Random phases → $d\sigma/d\Omega \propto N$ / 随机相位 → 截面正比于 $N$
- Compton scattering, Thomson from free electrons without interference / 康普顿散射、自由电子的非干涉汤姆孙散射

---

## Transition Radiation / 渡越辐射

Emitted when a charged particle crosses a boundary between two dielectrics.
当带电粒子穿过两种介电材料之间的界面时产生的辐射。

### Characteristics / 特征
- Forward lobe / 前向瓣：$\theta \sim 1/\gamma$
- Broad spectrum / 宽频谱：from visible to X-ray / 从可见光到X射线
- Intensity / 强度 $\propto \gamma^2 \ln(1/\omega_p)$ for $\gamma \gg 1$

### Applications / 应用
- Particle identification in transition radiation detectors (TRD) / 渡越辐射探测器中的粒子识别
- $\gamma \gtrsim 1000$ detectable / $\gamma \gtrsim 1000$ 可探测

---

## Cherenkov Radiation (revisited with formalism) / 切伦科夫辐射（形式化处理）

### Frank-Tamm Formula / 弗兰克-塔姆公式

Energy radiated per unit length per unit frequency / 单位长度单位频率的辐射能量：

$$
\frac{d^2 E}{dx d\omega} = \frac{q^2}{4\pi\epsilon_0 c^2} \omega \left( 1 - \frac{1}{\beta^2 n^2(\omega)} \right) \quad \text{for / 条件 } \beta n > 1
$$

### Spectral Dependence / 频谱依赖
- Number of photons / 光子数：$dN/dx \propto \sin^2\theta_c = 1 - 1/(\beta^2 n^2)$
- Visible range / 可见光范围：~300 photons/cm for $\beta \approx 1$ in water / 水中约300光子/cm

---

## Key Formulas Summary / 重要公式汇总

| Concept / 概念 | Formula / 公式 |
|---------|---------|
| Lienard-Wiechert scalar potential / 利埃纳-维谢尔特标势 | $\Phi = \frac{q}{4\pi\epsilon_0} \left[ \frac{1}{(1-\boldsymbol{\beta}\cdot\mathbf{n})R} \right]_{\text{ret}}$ |
| Lienard-Wiechert vector potential / 利埃纳-维谢尔特矢势 | $\mathbf{A} = \frac{\mu_0 q}{4\pi} \left[ \frac{\mathbf{v}}{(1-\boldsymbol{\beta}\cdot\mathbf{n})R} \right]_{\text{ret}}$ |
| Velocity field / 速度场 | $\mathbf{E}_v = \frac{q}{4\pi\epsilon_0} \frac{\mathbf{n} - \boldsymbol{\beta}}{\gamma^2(1-\boldsymbol{\beta}\cdot\mathbf{n})^3 R^2}$ |
| Acceleration (radiation) field / 加速度（辐射）场 | $\mathbf{E}_a = \frac{q}{4\pi\epsilon_0 c} \frac{\mathbf{n} \times [(\mathbf{n} - \boldsymbol{\beta}) \times \dot{\boldsymbol{\beta}}]}{(1-\boldsymbol{\beta}\cdot\mathbf{n})^3 R}$ |
| Larmor formula / 拉莫尔公式 | $P = \frac{q^2 a^2}{6\pi\epsilon_0 c^3}$ |
| Relativistic power / 相对论功率 | $P = \frac{q^2}{6\pi\epsilon_0 c} \gamma^6 [\dot{\beta}^2 - (\boldsymbol{\beta} \times \dot{\boldsymbol{\beta}})^2]$ |
| Covariant power / 协变功率 | $\frac{dP}{d\tau} = \frac{q^2}{6\pi\epsilon_0 c^3} \frac{dU_\alpha}{d\tau}\frac{dU^\alpha}{d\tau}$ |
| Synchrotron power / 同步辐射功率 | $P = \frac{q^2 c}{6\pi\epsilon_0} \frac{\beta^4\gamma^4}{\rho^2}$ |
| Critical frequency / 临界频率 | $\omega_c = \frac{3}{2}\frac{c\gamma^3}{\rho}$ |
| Thomson cross section / 汤姆孙截面 | $\sigma_T = \frac{8\pi}{3} r_e^2$ |
