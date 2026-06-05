# Pozar 《微波工程》第 1 章 — 电磁理论基础

> **参考**: Pozar, D. M., *Microwave Engineering*, 4th Edition, Chapter 1 (pp. 1–69)
> **范围**: Maxwell 方程组 → 波动方程 → 平面波 → Poynting 定理 → 时谐场 → 复数介电常数 → 色散 → 反射与透射

---

## 1.1 引言 — 微波频谱

| 频段 | 频率范围 | 自由空间波长 |
|------|----------|-------------|
| UHF | 300 MHz – 3 GHz | 1 m – 10 cm |
| SHF | 3 – 30 GHz | 10 cm – 1 cm |
| EHF | 30 – 300 GHz | 1 cm – 1 mm |

**工程意义**: 微波波长与电路尺度可比 → 不能再用集总参数电路理论，必须用场论（Maxwell 方程组）。

---

## 1.2 Maxwell 方程组

### 微分形式（Pozar 式 1.1–1.4）

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}
\quad \text{(Faraday 定律)}
$$

$$
\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}
\quad \text{(Ampere 定律 + 位移电流)}
$$

$$
\nabla \cdot \mathbf{D} = \rho
\quad \text{(Gauss 定律 — 电场)}
$$

$$
\nabla \cdot \mathbf{B} = 0
\quad \text{(Gauss 定律 — 磁场)}
$$

**量纲检查**:
- $\nabla \times \mathbf{E}$: [V/m²] = [T/s] = [Wb/m²·s] ✅
- $\nabla \times \mathbf{H}$: [A/m²] = [A/m²] + [C/m²·s] = [A/m²] ✅

### 本构关系（Pozar 式 1.5–1.8）

$$
\mathbf{D} = \epsilon \mathbf{E}, \quad
\mathbf{B} = \mu \mathbf{H}, \quad
\mathbf{J} = \sigma \mathbf{E}
$$

- $\epsilon = \epsilon_0 \epsilon_r$: 介电常数 [F/m]
- $\mu = \mu_0 \mu_r$: 磁导率 [H/m]
- $\sigma$: 电导率 [S/m]
- 各向同性介质中为标量，各向异性介质中为张量

### 积分形式（物理直觉）

$$
\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{\partial}{\partial t} \int_S \mathbf{B} \cdot d\mathbf{s}
\quad \text{变化的磁场产生电场}
$$

$$
\oint_C \mathbf{H} \cdot d\mathbf{l} = \int_S \mathbf{J} \cdot d\mathbf{s} + \frac{\partial}{\partial t} \int_S \mathbf{D} \cdot d\mathbf{s}
\quad \text{电流或变化的电场产生磁场}
$$

---

## 1.3 边界条件（Pozar 式 1.22–1.25）

从 Maxwell 积分形式导出，取跨越介质界面的无穷小回路和高斯面：

| 物理量 | 一般边界条件 | 理想导体边界 ($\sigma \to \infty$) |
|--------|------------|---------------------------|
| 电场切向 | $\hat{n} \times (\mathbf{E}_1 - \mathbf{E}_2) = 0$ | $\hat{n} \times \mathbf{E} = 0$ |
| 磁场切向 | $\hat{n} \times (\mathbf{H}_1 - \mathbf{H}_2) = \mathbf{J}_s$ | $\hat{n} \times \mathbf{H} = \mathbf{J}_s$ |
| 电位移法向 | $\hat{n} \cdot (\mathbf{D}_1 - \mathbf{D}_2) = \rho_s$ | $\hat{n} \cdot \mathbf{D} = \rho_s$ |
| 磁感应法向 | $\hat{n} \cdot (\mathbf{B}_1 - \mathbf{B}_2) = 0$ | $\hat{n} \cdot \mathbf{B} = 0$ |

**物理直觉**:
- $E_\parallel$ 连续：切向电场积分沿回路闭合 → 必须连续
- $H_\parallel$ 跳跃表面电流：$H_\parallel$ 在理想导体表面等于 $J_s$ 大小
- $D_\perp$ 跳跃表面电荷
- $B_\perp$ 连续：磁单极不存在

---

## 1.4 波动方程（Pozar 式 1.26–1.27）

取 $\nabla \times$ Faraday 定律，代入 Ampere 定律，对均匀无源介质：

$$
\nabla^2 \mathbf{E} - \mu \epsilon \frac{\partial^2 \mathbf{E}}{\partial t^2} - \mu \sigma \frac{\partial \mathbf{E}}{\partial t} = 0
$$

$$
\nabla^2 \mathbf{H} - \mu \epsilon \frac{\partial^2 \mathbf{H}}{\partial t^2} - \mu \sigma \frac{\partial \mathbf{H}}{\partial t} = 0
$$

**推导关键**：
1. $\nabla \times (\nabla \times \mathbf{E}) = \nabla(\nabla \cdot \mathbf{E}) - \nabla^2 \mathbf{E}$
2. 无源区 $\nabla \cdot \mathbf{E} = 0$
3. $\nabla \times (\mu \partial \mathbf{H}/\partial t) = \mu \partial (\nabla \times \mathbf{H})/\partial t$
4. 代入 $\nabla \times \mathbf{H} = \sigma \mathbf{E} + \epsilon \partial \mathbf{E}/\partial t$

**量纲检查**:
- $\nabla^2 \mathbf{E}$: [V/m³]
- $\mu \epsilon \partial^2 \mathbf{E} / \partial t^2$: [H/m · F/m · V/m · 1/s²] = [V/m · s²/s²] = [V/m] ✅
- $\mu \sigma \partial \mathbf{E} / \partial t$: [H/m · S/m · V/m · 1/s] = [V/m] ✅

---

## 1.5 Poynting 定理 — 能量守恒（Pozar 式 1.27–1.29）

利用矢量恒等式 $\nabla \cdot (\mathbf{E} \times \mathbf{H}) = \mathbf{H} \cdot (\nabla \times \mathbf{E}) - \mathbf{E} \cdot (\nabla \times \mathbf{H})$：

$$
-\oint_S (\mathbf{E} \times \mathbf{H}) \cdot d\mathbf{s} =
\int_V \mathbf{E} \cdot \mathbf{J} \, dv +
\frac{\partial}{\partial t} \int_V \left( \frac{1}{2} \epsilon |\mathbf{E}|^2 + \frac{1}{2} \mu |\mathbf{H}|^2 \right) dv
$$

**Poynting 矢量**：
$$
\mathbf{S} = \mathbf{E} \times \mathbf{H} \quad [\text{W/m}^2]
$$

表示单位面积上的功率流（瞬时值）。

**物理含义**:
- 左侧：流入闭合面的总功率
- 右侧第一项：欧姆损耗（焦耳热）
- 右侧第二项：电场 + 磁场储能的时间变化率

**量纲检查**:
- $\mathbf{E} \times \mathbf{H}$: [V/m · A/m] = [W/m²] ✅

---

## 1.6 时谐场（Phasor 表示，Pozar 式 1.29–1.40）

对于正弦稳态 $\mathbf{E}(x,y,z,t) = \text{Re}[\mathbf{E}_s(x,y,z) e^{j\omega t}]$：

### Maxwell 方程组（频域）

$$
\nabla \times \mathbf{E}_s = -j\omega \mu \mathbf{H}_s
$$

$$
\nabla \times \mathbf{H}_s = \mathbf{J}_s + j\omega \epsilon \mathbf{E}_s
$$

$$
\nabla \cdot \mathbf{D}_s = \rho_s
$$

$$
\nabla \cdot \mathbf{B}_s = 0
$$

### 波动方程（Helmholtz 方程）

$$
\nabla^2 \mathbf{E}_s + k^2 \mathbf{E}_s = 0
\quad \text{其中复波数} \quad k^2 = \omega^2 \mu \epsilon_c
$$
$$
\nabla^2 \mathbf{H}_s + k^2 \mathbf{H}_s = 0
$$

### 复 Poynting 矢量（Pozar 式 1.39–1.40）

**平均功率**（时间平均 Poynting 矢量）：

$$
\langle \mathbf{S} \rangle = \frac{1}{2} \text{Re}[\mathbf{E}_s \times \mathbf{H}_s^*]
\quad [\text{W/m}^2]
$$

**复 Poynting 定理**：

$$
-\oint_S \frac{1}{2} (\mathbf{E}_s \times \mathbf{H}_s^*) \cdot d\mathbf{s} =
\int_V \frac{1}{2} \mathbf{E}_s \cdot \mathbf{J}_s^* \, dv +
j\omega \int_V \left( \frac{1}{4} \mu |\mathbf{H}_s|^2 - \frac{1}{4} \epsilon |\mathbf{E}_s|^2 \right) dv
$$

---

## 1.7 无损耗介质中的平面波（Pozar 式 1.41–1.55）

### 一维 Helmholtz 方程解

取 $+z$ 方向传播、$x$ 方向极化：

$$
E_x(z) = E_0 e^{-j\beta z} + E_0^- e^{j\beta z}
$$

其中 $\beta = \omega \sqrt{\mu\epsilon}$ 为**相位常数**[rad/m]。

### 相速度

$$
v_p = \frac{\omega}{\beta} = \frac{1}{\sqrt{\mu\epsilon}} = \frac{c}{\sqrt{\mu_r \epsilon_r}}
$$

- 无损耗介质中 $v_p$ 为常数（无色散）
- 自由空间 $v_p = c = 2.998 \times 10^8$ m/s

### 波长

$$
\lambda = \frac{2\pi}{\beta} = \frac{v_p}{f}
$$

### 波阻抗

$$
\eta = \frac{E_x}{H_y} = \sqrt{\frac{\mu}{\epsilon}}
\quad [\Omega]
$$

- 自由空间 $\eta_0 = \sqrt{\mu_0 / \epsilon_0} \approx 377\ \Omega$

### 磁场和电场关系

$$
H_y(z) = \frac{1}{\eta} E_x(z)
$$

右手定则：$\hat{E} \times \hat{H} = \hat{k}$（传播方向）

---

## 1.8 有损耗介质中的平面波（Pozar 式 1.57–1.66）

### 复介电常数

$$
\epsilon_c = \epsilon' - j\epsilon'' = \epsilon_0 \epsilon_r (1 - j \tan\delta)
$$

其中**损耗角正切**：

$$
\tan\delta = \frac{\sigma}{\omega\epsilon} + \frac{\epsilon''}{\epsilon'}
$$

### 复传播常数

$$
\gamma = \alpha + j\beta = j\omega\sqrt{\mu\epsilon_c} = j\omega\sqrt{\mu\epsilon\left(1 - j\frac{\sigma}{\omega\epsilon}\right)}
$$

- $\alpha$: 衰减常数 [Np/m]
- $\beta$: 相位常数 [rad/m]

### $\alpha$ 和 $\beta$ 的显式表达式

$$
\alpha = \omega\sqrt{\frac{\mu\epsilon}{2}} \left[ \sqrt{1 + \left( \frac{\sigma}{\omega\epsilon} \right)^2} - 1 \right]^{1/2}
$$

$$
\beta = \omega\sqrt{\frac{\mu\epsilon}{2}} \left[ \sqrt{1 + \left( \frac{\sigma}{\omega\epsilon} \right)^2} + 1 \right]^{1/2}
$$

**量纲检查**:
- $\alpha$: [rad/s · √(H/m · F/m) · (1)] = [1/m] = [Np/m] ✅
- $\beta$: [rad/s · √(H/m · F/m) · (1)] = [1/m] = [rad/m] ✅

### 场解

$$
E_x(z) = E_0 e^{-\alpha z} e^{-j\beta z}
$$

振幅以 $e^{-\alpha z}$ 指数衰减。

### 有损耗介质波阻抗

$$
\eta_c = \sqrt{\frac{\mu}{\epsilon_c}} = \sqrt{\frac{\mu}{\epsilon \left(1 - j\frac{\sigma}{\omega\epsilon}\right)}}
\quad \text{复数}[ \Omega]
$$

---

## 1.9 良导体中的平面波 — 趋肤效应（Pozar 式 1.67–1.72）

### 条件

$$
\frac{\sigma}{\omega\epsilon} \gg 1 \quad (\text{导体中} \sigma \gg 10^7\text{S/m}, \omega \lesssim 10^{11}\text{rad/s})
$$

### 传播常数简化

$$
\alpha = \beta = \sqrt{\pi f \mu \sigma}
$$

### 趋肤深度

$$
\delta_s = \frac{1}{\alpha} = \frac{1}{\sqrt{\pi f \mu \sigma}}
\quad [\text{m}]
$$

- 场强降至表面值的 $1/e \approx 37\%$
- 铜 ($\sigma = 5.8 \times 10^7$ S/m) 在 10 GHz: $\delta_s \approx 0.66\ \mu\text{m}$

### 良导体波阻抗

$$
\eta_c = (1 + j) \sqrt{\frac{\pi f \mu}{\sigma}} = (1 + j) \frac{1}{\sigma \delta_s}
$$

**物理含义**：
- 频率越高，趋肤深度越小 → 微波电流集中在导体表面
- 导致高频电阻增大（RF 电阻 ≈ DC 电阻的若干倍）

---

## 1.10 复介电常数与极化（Pozar 式 1.73–1.79）

### 极化机制

| 极化类型 | 频率响应范围 | 特征 |
|---------|------------|------|
| 电子极化 | 光学频段 | 电子云偏移 |
| 离子极化 | 红外 | 离子相对偏移 |
| 取向极化 | 微波 | 偶极子转向 |
| 空间电荷极化 | 低频 | 载流子积累 |

### Debye 弛豫模型

$$
\epsilon_r(\omega) = \epsilon_{r\infty} + \frac{\epsilon_{rs} - \epsilon_{r\infty}}{1 + j\omega\tau}
$$

- $\epsilon_{rs}$: 静态（DC）相对介电常数
- $\epsilon_{r\infty}$: 光学频率相对介电常数
- $\tau$: 弛豫时间

**工程意义**: 在微波频段，水的 $\epsilon_r$ 有很大虚部 → 微波加热利用介电损耗。

---

## 1.11 色散与群速度（Pozar 式 1.80–1.84）

### 相速度

$$
v_p = \frac{\omega}{\beta}
$$

### 群速度（能量/信号传播速度）

$$
v_g = \frac{d\omega}{d\beta} = \frac{1}{d\beta/d\omega}
$$

- 无损耗介质：$v_p = v_g$（无色散）
- 有损耗介质 / 波导：$v_p \neq v_g$（有色散）
- 反常色散区可能出现 $v_g > c$ 或负 $v_g$，但**信号速度**仍 $\le c$

### 群速度与相速度关系

$$
v_g = \frac{v_p}{1 - \frac{\omega}{v_p} \frac{dv_p}{d\omega}}
$$

---

## 1.12 正入射时的反射与透射（Pozar 式 1.85–1.100）

### 单层界面（介质 1 → 介质 2）

$$
\Gamma = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1}
\quad \text{(反射系数)}
$$

$$
\tau = \frac{2\eta_2}{\eta_2 + \eta_1}
\quad \text{(透射系数)}
$$

**验证**: $\Gamma + 1 = \tau$（电场边界条件检查）✅

### 功率反射与透射

$$
R = |\Gamma|^2, \quad
T = 1 - R = \frac{4\eta_1\eta_2 \cos^2 \theta_\eta}{|\eta_1 + \eta_2|^2}
$$

### 有损耗介质平板的多次反射

总反射系数（考虑平板内多次反射）：

$$
\Gamma_{\text{total}} = \frac{\Gamma_{12} + \Gamma_{23} e^{-2\gamma_2 d}}{1 + \Gamma_{12} \Gamma_{23} e^{-2\gamma_2 d}}
$$

- $d$: 平板厚度
- $\Gamma_{12}$: 界面 1→2 的 Fresnel 反射系数
- $\Gamma_{23}$: 界面 2→3 的 Fresnel 反射系数

**物理直觉**：
- $d = n\lambda/2$ 时：多次反射相长 → 反射可为零（匹配条件）
- $d = \lambda/4$ 且 $\eta_2 = \sqrt{\eta_1 \eta_3}$ 时：四分之一波长阻抗变换器

---

## 1.13 斜入射 — Snell 定律与 Fresnel 系数（Pozar 式 1.101–1.120）

### Snell 定律

$$
k_1 \sin\theta_i = k_1 \sin\theta_r = k_2 \sin\theta_t
$$

所以 $\theta_i = \theta_r$，且：

$$
\sqrt{\mu_1\epsilon_1} \sin\theta_i = \sqrt{\mu_2\epsilon_2} \sin\theta_t
$$

### 平行极化（TM, $\mathbf{H}$ 平行界面）

$$
\Gamma_{\parallel} = \frac{\eta_2 \cos\theta_t - \eta_1 \cos\theta_i}{\eta_2 \cos\theta_t + \eta_1 \cos\theta_i}
$$

$$
\tau_{\parallel} = \frac{2\eta_2 \cos\theta_i}{\eta_2 \cos\theta_t + \eta_1 \cos\theta_i}
$$

### 垂直极化（TE, $\mathbf{E}$ 平行界面）

$$
\Gamma_{\perp} = \frac{\eta_2 \cos\theta_i - \eta_1 \cos\theta_t}{\eta_2 \cos\theta_i + \eta_1 \cos\theta_t}
$$

$$
\tau_{\perp} = \frac{2\eta_2 \cos\theta_i}{\eta_2 \cos\theta_i + \eta_1 \cos\theta_t}
$$

### Brewster 角（无反射条件）

对于 $\mu_1 = \mu_2$ 的非磁性介质：

$$
\tan\theta_B = \sqrt{\frac{\epsilon_2}{\epsilon_1}}
$$

- 仅在平行极化时存在 Brewster 角
- 用于偏振片设计

### 全内反射

当 $n_1 > n_2$ 且 $\theta_i > \theta_c$：

$$
\theta_c = \arcsin\left( \sqrt{\frac{\epsilon_2}{\epsilon_1}} \right)
$$

界面处产生倏逝波（evanescent wave）。

---

## 1.14 传输线概述（连接第 2 章）

从 Maxwell 方程出发，TEM 传输线满足：

$$
\gamma = \sqrt{(R + j\omega L)(G + j\omega C)}
$$

其中 $R, L, G, C$ 为单位长度的分布参数。

**本章基础**: 传输线类比于平面波传播（波方程形式相同），$\gamma$ 和 $Z_0$ 对应于平面波的 $\gamma$ 和 $\eta$。

---

## 关键物理图像总结

| 概念 | 关键公式 | 物理意义 |
|------|---------|---------|
| Maxwell 方程组 | $\nabla \times \mathbf{E} = -\partial\mathbf{B}/\partial t$ | 电磁统一 |
| 波动方程 | $\nabla^2 \mathbf{E} + k^2\mathbf{E} = 0$ | 电磁波动性 |
| Poynting 矢量 | $\mathbf{S} = \mathbf{E} \times \mathbf{H}$ | 功率流方向 |
| 相速度 | $v_p = \omega/\beta = 1/\sqrt{\mu\epsilon}$ | 等相位面速度 |
| 趋肤深度 | $\delta_s = 1/\sqrt{\pi f \mu \sigma}$ | 穿透深度 |
| 反射系数 | $\Gamma = (\eta_2 - \eta_1)/(\eta_2 + \eta_1)$ | 阻抗失配度量 |
| 复介电常数 | $\epsilon_c = \epsilon' - j\epsilon''$ | 储能 + 损耗 |
| 群速度 | $v_g = d\omega/d\beta$ | 信息/能量传输速度 |

---

## 量纲检查总表

| 公式 | 量纲 | 结果 |
|------|------|------|
| $\nabla \times \mathbf{E} = -\partial\mathbf{B}/\partial t$ | V/m² = T/s | ✅ |
| $\nabla \times \mathbf{H} = \mathbf{J} + \partial\mathbf{D}/\partial t$ | A/m² = A/m² + A/m² | ✅ |
| $\mathbf{S} = \mathbf{E} \times \mathbf{H}$ | V/m · A/m = W/m² | ✅ |
| $\beta = \omega\sqrt{\mu\epsilon}$ | rad/s · √(H/m·F/m) = rad/m | ✅ |
| $\alpha = \sqrt{\pi f \mu \sigma}$ | √(1/s · H/m · S/m) = √(1/s · Vs/A·m · A/Vm) = 1/m | ✅ |
| $\Gamma = (\eta_2 - \eta_1)/(\eta_2 + \eta_1)$ | Ω/Ω = 无量纲 | ✅ |
| $v_p = 1/\sqrt{\mu\epsilon}$ | 1/√(H/m·F/m) = m/s | ✅ |

---

## 工程应用要点

1. **阻抗匹配**: $\Gamma$ 是阻抗失配的直接度量 → 最小化 $\Gamma$ 是微波设计核心
2. **趋肤效应**: 10 GHz 时铜的 $\delta_s \approx 0.66\ \mu\text{m}$ → 镀银/金只需要非常薄
3. **介质损耗**: $\tan\delta$ 决定介质中能量衰减 → 低 $\tan\delta$ 用于高频 PCB
4. **Brewster 角**: 无反射入射角 → 极化分离器设计
5. **群速度色散**: 限制脉冲展宽 → 宽带通信系统的重要约束
