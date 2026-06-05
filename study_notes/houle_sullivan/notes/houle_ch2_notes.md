# Chapter 2 — More on One-Dimensional Simulation

> **中英双语版**
> **Source:** Houle & Sullivan, *Electromagnetic Simulation Using the FDTD Method with Python*, 3rd ed. (IEEE Press, 2020), Ch. 2

---

## 2.1 Reformulation Using the Flux Density | 使用电通量密度重新表述

### Why Change the Formulation? | 为什么要改变公式？

The flux density $\mathbf{D}$ formulation separates the **universal** Maxwell curl equations from the **material-specific** constitutive relation:
电通量密度 $\mathbf{D}$ 公式将**通用**麦克斯韦旋度方程与**材料特定**的本构关系分开：

$$
\frac{\partial \mathbf{D}}{\partial t} = \nabla \times \mathbf{H} \tag{2.1a}
$$
$$
\mathbf{D}(\omega) = \varepsilon_0 \varepsilon_r^*(\omega) \, \mathbf{E}(\omega) \tag{2.1b}
$$
$$
\frac{\partial \mathbf{H}}{\partial t} = -\frac{1}{\mu_0} \nabla \times \mathbf{E} \tag{2.1c}
$$

**Advantage:** Eqs. (2.1a) and (2.1c) stay **exactly the same** for all media — all complexity is confined to Eq. (2.1b), which becomes a **digital filtering problem**.
**优势：** 式 (2.1a) 和 (2.1c) 对所有介质**完全相同**——所有复杂性被限制在式 (2.1b) 中，变成一个**数字滤波问题**。

### Material Response as a Filter | 材料响应作为滤波器

The key insight: solving $\mathbf{D} = \varepsilon_0 \varepsilon_r^* \mathbf{E}$ for various media maps directly to well-known **digital filter** structures (IIR, FIR).
关键洞察：为各种介质求解 $\mathbf{D} = \varepsilon_0 \varepsilon_r^* \mathbf{E}$ 直接映射到著名的**数字滤波器**结构（IIR、FIR）。

---

## 2.2 Calculating the Frequency Domain Output | 计算频域输出

### Why Frequency Domain? | 为什么需要频域？

The **Discrete Fourier Transform (DFT)** provides $E(\omega)$ from FDTD time-domain results.
**离散傅里叶变换（DFT）** 从 FDTD 时域结果提供 $E(\omega)$。

### DFT Implementation in FDTD | FDTD 中的 DFT 实现

$$
E(\omega) = \sum_{n=0}^{N-1} E^n[k_0] \; e^{-j\omega n \Delta t}
$$

```python
ex_stored[time_step] = ex[k0]
E_omega = np.fft.fftfreq(nsteps, d=dt)[:nsteps//2]
E_spectrum = np.fft.fft(ex_stored)[:nsteps//2]
```

### Key Properties | 关键性质

- Resolution: $\Delta f = 1/(N \Delta t)$（分辨率）
- DFT at DC ($f=0$): equivalent to time-average（直流：时间平均）
- Windowing affects spectrum (rectangular window → Sinc artifacts)（窗函数影响频谱）

---

## 2.3 Frequency-Dependent Media | 频变介质

### The Debye Relaxation Model | 德拜弛豫模型

$$
\varepsilon_r^*(\omega) = \varepsilon_\infty + \frac{\chi_1}{1 + j\omega\tau}
$$

| Parameter | Physical Meaning | 含义 |
|---|---|---|
| $\varepsilon_\infty$ | High-frequency permittivity | 高频介电常数 |
| $\chi_1$ | Static susceptibility | 静态极化率 |
| $\tau$ | Relaxation time | 弛豫时间 |

### Effective Frequency-Dependent Properties | 有效的频变特性

$$
\varepsilon_r'(\omega) = \varepsilon_\infty + \frac{\chi_1}{1 + \omega^2\tau^2}
$$
$$
\sigma_{\text{eff}}(\omega) = \omega \varepsilon_0 \frac{\chi_1 \omega\tau}{1 + \omega^2\tau^2}
$$

> **Important:** Both $\varepsilon_r'$ and $\sigma_{\text{eff}}$ are **frequency-dependent** — this is the fundamental origin of **dispersion**.
> **重要：** $\varepsilon_r'$ 和 $\sigma_{\text{eff}}$ 都是**随频率变化**的——这是**色散**的根本来源。

### Example: Human Muscle Tissue | 示例：人类肌肉组织

| Parameter | Value |
|---|---|
| $\varepsilon_\infty$ | 4.0 |
| $\chi_1$ | 43.0 |
| $\tau$ | 7.96 ps |

Produces $\varepsilon_r \approx 47$ at DC down to $\approx 4$ at optical frequencies.
DC 下 $\varepsilon_r \approx 47$，光学频率下降至 $\approx 4$。

---

## 2.3.1 Auxiliary Differential Equation (ADE) Method | 辅助微分方程法

### ADE for Debye Medium | 德拜介质的 ADE

Define auxiliary polarization $\mathbf{P}$:
定义辅助极化 $\mathbf{P}$：

$$
\frac{d\mathbf{P}}{dt} = \frac{1}{\tau}\left(\varepsilon_0 \chi_1 \mathbf{E} - \mathbf{P}\right)
$$

Then: $\mathbf{D} = \varepsilon_0 \varepsilon_\infty \mathbf{E} + \mathbf{P}$

### Comparison: ADE vs. Z-Domain | ADE vs. Z 域对比

| Aspect | ADE | Z-Domain / RC |
|---|---|---|
| Formulation | Time-domain ODEs | Z-domain difference equations |
| Implementation | Direct time-stepping | Convolution or recursive filter |
| Stability | Equivalent | Equivalent |

Both methods yield identical results for the Debye medium.
两种方法对德拜介质给出相同结果。

---

## 2.4 Formulation Using Z Transforms | 使用 Z 变换的公式

### Z-Domain Debye Update | Z 域德拜更新

```python
# Z-domain (recursive convolution) Debye update
dx[k] = dx[k] + (hy[k-1] - hy[k])       # D-update

ex[k] = (dx[k] + chi1 * ex_old[k]) / (eps_inf + chi1 * np.exp(-dt/tau))
ex_old[k] = ex[k] * np.exp(-dt/tau)      # z^{-1} delay
```

### Signal Processing Connection | 信号处理联系

The Z-transform makes explicit that FDTD simulation of dispersive media is exactly equivalent to **digital filtering**:
Z 变换明确说明了色散介质的 FDTD 仿真等同于**数字滤波**：
- **Transfer function** $H(z) = E(z)/D(z)$（传递函数）
- **Poles and zeros** of the medium response（介质响应的极点和零点）
- **Filter coefficients** map to physical medium parameters（滤波器系数映射到物理介质参数）

---

## 2.4.1 Simulation of Unmagnetized Plasma | 非磁化等离子体仿真

### Plasma as a Drude Medium | 等离子体作为 Drude 介质

$$
\varepsilon_r^*(\omega) = 1 - \frac{\omega_p^2}{\omega^2 + j\omega \nu}
$$

| Parameter | Physical Meaning | 含义 |
|---|---|---|
| $\omega_p = \sqrt{n_e e^2 / (m_e \varepsilon_0)}$ | Plasma frequency | 等离子体频率 |
| $\nu$ | Collision frequency | 碰撞频率 |

### Physical Phenomena | 物理现象

- **Low freq** ($\omega \ll \omega_p$): $\varepsilon_r^* < 0$ → **evanescent** (total reflection | 全反射)
- **Above $\omega_p$**: wave propagates with $k = \omega/c \sqrt{1 - \omega_p^2/\omega^2}$（波传播）
- Plasma acts as a **high-pass filter**（等离子体作为**高通滤波器**）

### Example: Ionosphere | 示例：电离层

AM radio (below ~10 MHz) undergoes total internal reflection at the ionosphere → propagates beyond line-of-sight. FM radio (~100 MHz) passes through.
AM 无线电波（低于 ~10 MHz）在电离层全内反射 → 超视距传播。FM 无线电（约 100 MHz）穿透通过。

---

## 2.5 Formulating a Lorentz Medium | 建立洛伦兹介质模型

### Lorentz Model (Multi-Resonance) | 洛伦兹模型（多谐振）

$$
\varepsilon_r^*(\omega) = \varepsilon_\infty + \sum_m \frac{\omega_{p,m}^2}{\omega_{0,m}^2 - \omega^2 - j\omega \nu_m}
$$

### Key Distinction from Debye | 与德拜的关键区别

| Feature | Debye | Lorentz |
|---|---|---|
| Resonance | No (monotonic decay) | Yes (oscillatory response) |
| Poles | Single real pole | Complex conjugate poles |
| Applications | Water, biological tissue | Solids, resonant media |

---

## 2.5.1 Simulation of Human Muscle Tissue (Lorentz) | 人体肌肉组织仿真（洛伦兹）

### SAR (Specific Absorption Rate) | 比吸收率

For hyperthermia treatment planning:
用于热疗计划：

- **SAR** = $\sigma |E|^2 / (2\rho)$ determines heating
- At 433 MHz: $\varepsilon_r \approx 50-60$, $\sigma \approx 0.8-1.5$ S/m
- Penetration depth $\delta \approx 2$–$3$ cm in muscle（穿透深度约 2-3 cm）

---

## Key Equations Master Index | 关键方程索引

| Eq. | Description | 说明 |
|---|---|---|
| (2.1a–c) | Flux density Maxwell eqs | 电通量密度麦克斯韦方程 |
| — | Debye model | 德拜模型 |
| — | Drude (plasma) model | Drude（等离子体）模型 |
| — | Lorentz model | 洛伦兹模型 |
| — | $\varepsilon_r'(\omega)$ for Debye | 德拜有效介电常数 |
| — | $\sigma_{\text{eff}}(\omega)$ for Debye | 德拜有效电导率 |
| — | Plasma freq: $\omega_p = \sqrt{n_e e^2/(m_e\varepsilon_0)}$ | 等离子体频率 |
| — | Penetration depth: $\delta = \sqrt{2/(\omega\mu\sigma)}$ | 穿透深度 |
