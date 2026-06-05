---
title: Chapter 10: Negative Resistance Devices & Circuits / 第10章：负阻器件与电路
source: Collin, Foundations for Microwave Engineering, 2nd Ed., Ch.10–12
---

# Chapter 10: Negative Resistance Devices & Circuits / 第10章：负阻器件与电路

> **中英双语版**

> Based on: R. E. Collin, *Foundations for Microwave Engineering*, 2nd ed., IEEE Press, 2001.
> 基于：R. E. Collin《微波工程基础》第2版，IEEE出版社，2001年。

---

## Overview / 概述

This chapter covers negative-resistance devices used in microwave oscillators and amplifiers. The unifying principle is that a static or dynamic negative resistance can cancel positive circuit losses, enabling oscillation or reflection gain. The devices discussed include:
本章涵盖用于微波振荡器和放大器的负阻器件。其统一原理是：静态或动态负电阻可以抵消正电路损耗，从而实现振荡或反射增益。讨论的器件包括：

- **Tunnel (Esaki) diode / 隧道（江崎）二极管** — quantum-mechanical tunneling through a narrow junction produces an N-type I–V characteristic with a static negative resistance region / 量子力学隧穿穿过窄结，产生具有静态负阻区的N型I-V特性。
- **Gunn diode / 耿氏二极管** — the transferred-electron effect (intervalley scattering in III–V semiconductors) yields a bulk negative differential mobility, leading to Gunn-domain formation and transit-time oscillations / 转移电子效应（III-V族半导体中的谷间散射）产生体负微分迁移率，导致耿氏畴形成和渡越时间振荡。
- **IMPATT diode / IMPATT二极管** — impact ionization avalanche combined with transit-time delay produces a dynamic negative conductance from DC to RF conversion / 碰撞电离雪崩与渡越时间延迟相结合，从DC到RF转换产生动态负电导。
- **TRAPATT diode / TRAPATT二极管** — trapped plasma avalanche triggered transit time / 俘获等离子体雪崩触发渡越时间，工作频率低于IMPATT但效率更高。
- **Circuit applications / 电路应用** — negative-resistance oscillators, reflection amplifiers, injection locking, and stabilisation techniques / 负阻振荡器、反射放大器、注入锁定和稳定化技术。

---

## 10.1 Tunnel (Esaki) Diode / 隧道（江崎）二极管

### Physical Principle (Quantum-Mechanical Tunneling) / 物理原理（量子隧穿）

A tunnel diode is a heavily doped ($N \approx 10^{19}\text{--}10^{20}\text{ cm}^{-3}$) p–n junction with a depletion width of order 10 nm. At this scale, electrons can tunnel through the forbidden bandgap. The I–V characteristic exhibits an **N-type negative resistance** region.
隧道二极管是重掺杂($N \approx 10^{19}\text{--}10^{20}\text{ cm}^{-3}$)的p-n结，耗尽层宽度约10 nm。在此尺度下，电子可以隧穿禁带。I-V特性呈现**N型负阻**区域。

### Characteristic Parameters / 特性参数

- **Peak current / 峰值电流** $I_p$ — current at the peak voltage $V_p$ / 峰值电压 $V_p$ 处的电流
- **Valley current / 谷值电流** $I_v$ — current minimum after the negative-resistance region / 负阻区之后的最小电流
- **Peak-to-valley current ratio (PVCR) / 峰谷电流比** $= I_p / I_v$ — figure of merit (typically 3–15 for Ge, 3–6 for GaAs) / 品质因数（锗通常3–15，砷化镓3–6）
- **Negative resistance / 负电阻** $R_n$:

$$R_n = \left.\frac{\Delta V}{\Delta I}\right|_{\text{neg. region}} \quad \text{(typically } -5\;\Omega\text{ to }-100\;\Omega\text{)}$$

### I–V Characteristic (Approximate Model) / I-V特性（近似模型）

A common empirical fit for the tunnel-diode I–V curve / 隧道二极管I-V曲线的常用经验拟合：

$$I(V) = I_p \frac{V}{V_p} \exp\!\left(1 - \frac{V}{V_p}\right) + I_0\!\left[\exp\!\left(\frac{qV}{nkT}\right) - 1\right] \tag{10.1}$$

where the first term models the tunneling current and the second models the normal diode diffusion current.
其中第一项模拟隧穿电流，第二项模拟正常二极管扩散电流。

### Equivalent Circuit / 等效电路

- $R_n$: negative resistance (static, small-signal) / 负电阻（静态、小信号）
- $C_j$: junction capacitance (typically 1–10 pF) / 结电容（典型1–10 pF）
- $R_s$: series resistance (ohmic contacts) / 串联电阻（欧姆接触）
- $L_s$: package/lead inductance / 封装/引线电感

The diode can be self-resonant and may oscillate if the external circuit provides the right impedance.
二极管可自谐振，若外部电路提供适当的阻抗则可产生振荡。

### Switching (Bistable Operation) / 开关（双稳态工作）

A tunnel diode biased in the negative-resistance region with a load line that intersects the I–V curve at three points acts as a bistable element.
在负阻区偏置的隧道二极管，若负载线与I-V曲线相交于三点，则作为双稳态元件工作。

---

## 10.2 Gunn Diode (Transferred-Electron Device) / 耿氏二极管（转移电子器件）

### Transferred-Electron Effect (Ridley–Watkins–Hilsum) / 转移电子效应（Ridley-Watkins-Hilsum）

In GaAs, InP, and certain III–V compounds, the conduction band has a **lower-valley minimum** (high mobility, low effective mass, $\Gamma$-valley) and an **upper-valley minimum** (low mobility, higher effective mass, L-valley), separated by $\Delta E \approx 0.36\text{ eV}$ for GaAs.
在GaAs、InP及某些III-V族化合物中，导带具有**低谷极小值**（高迁移率、低有效质量，$\Gamma$谷）和**上谷极小值**（低迁移率、较高有效质量，L谷），对于GaAs，能隙 $\Delta E \approx 0.36\text{ eV}$。

When the applied electric field exceeds a **threshold field** $E_{th} \approx 3.2\text{ kV/cm}$ for GaAs, electrons gain enough energy to scatter into the upper valley, where mobility is 10–20× lower. The result is a **negative differential mobility**:
当外加电场超过GaAs的**阈值场** $E_{th} \approx 3.2\text{ kV/cm}$ 时，电子获得足够能量散射到上谷，该处迁移率低10–20倍。结果为**负微分迁移率**：

$$\mu_d = \frac{dv}{dE} < 0 \quad \text{for } E > E_{th} \tag{10.2}$$

### Gunn-Domain Formation / 耿氏畴形成

A **Gunn domain** is a high-field dipole layer that forms when $E > E_{th}$ / **耿氏畴**是在 $E > E_{th}$ 时形成的高场偶极层：

1. A doping fluctuation causes a local field increase above $E_{th}$ / 掺杂涨落导致局部场超过 $E_{th}$
2. Electrons slow down (negative mobility), accumulating behind the fluctuation / 电子减速（负迁移率），在涨落后面积聚
3. A dipole forms: excess negative charge trailing, depleted region ahead / 形成偶极层：后面多余负电荷，前面耗尽区
4. The domain drifts at the saturation velocity $v_{sat}$ toward the anode / 畴以饱和速度 $v_{sat}$ 向阳极漂移
5. When the domain reaches the anode, the current spikes and a new domain nucleates at the cathode / 当畴到达阳极时，电流尖峰，新的畴在阴极成核

### Transit-Time Frequency / 渡越时间频率

The fundamental oscillation frequency is determined by the transit time across the active region of length $L$ / 基波振荡频率由有源区长度 $L$ 上的渡越时间决定：

$$f_t = \frac{v_{sat}}{L} \tag{10.4}$$

### Modes of Operation / 工作模式

| Mode / 模式 | Condition / 条件 | Efficiency / 效率 | Notes / 备注 |
|------|-----------|------------|-------|
| **Transit-time / 渡越时间模** | $n_0 L > 10^{12}\text{ cm}^{-2}$ | ~2–15% | Fundamental mode / 基模 |
| **LSA / 限界空间电荷积累模** | $f > f_t$, $n_0/f > 10^4\text{ s/cm}^3$ | ~15–20% | Domain never fully forms / 畴从未完全形成 |
| **Delayed-domain / 延迟畴模** | Tuned circuit at $f < f_t$ | ~10–20% | Domain extinguishes before reaching anode / 畴在到达阳极前消失 |
| **Quenched-domain / 猝灭畴模** | Tuned circuit at $f > f_t$ | ~10–15% | Domain collapses in transit / 畴在渡越中崩溃 |

---

## 10.3 IMPATT Diode / IMPATT二极管

### Structure / 结构

IMPATT (IMPact Avalanche Transit Time) diodes use a **p⁺–n–n⁺** or **p⁺–p–n–n⁺** (Read diode) structure biased into avalanche breakdown.
IMPATT（碰撞雪崩渡越时间）二极管采用**p⁺–n–n⁺**或**p⁺–p–n–n⁺**（Read二极管）结构，偏置于雪崩击穿状态。

### Operating Principle / 工作原理

The IMPATT diode generates negative resistance through a **phase delay** mechanism combining two effects / IMPATT二极管通过结合两种效应的**相位延迟**机制产生负电阻：

1. **Avalanche multiplication / 雪崩倍增** — The RF electric field modulates the avalanche current. Due to the finite build-up time of the avalanche process, the avalanche current lags the RF voltage by 90° (inductive) / 射频电场调制雪崩电流。由于雪崩过程的有限建立时间，雪崩电流滞后射频电压90°（感性）。

2. **Transit-time delay / 渡越时间延迟** — Carriers generated in the avalanche region drift through the depletion region, producing an additional 90° delay (total 180°) / 雪崩区产生的载流子漂移穿过耗尽区，产生额外的90°延迟（总计180°）。

The combined effect is a **negative conductance** at the device terminals.
综合效果是在器件端子处呈现**负电导**。

### Small-Signal Model (Read's Model) / 小信号模型（Read模型）

The diode exhibits negative conductance over a frequency range roughly determined by the depletion region transit angle / 二极管在由耗尽区渡越角大致决定的频率范围内呈现负电导：

$$\theta = \omega \tau_d = \omega \frac{W_d}{v_s} \tag{10.5}$$

Maximum negative conductance occurs when $\theta \approx \pi$ (transit angle of 180°) / 最大负电导出现在 $\theta \approx \pi$（渡越角180°）时：

$$f_{opt} \approx \frac{v_s}{2W_d} \tag{10.6}$$

### Key Parameters (Si IMPATT) / 关键参数（硅IMPATT）

| Parameter / 参数 | Typical Value / 典型值 |
|-----------|---------------|
| Breakdown voltage $V_B$ / 击穿电压 $V_B$ | 30–150 V DC |
| DC bias current $I_{dc}$ / 直流偏置电流 $I_{dc}$ | 10–500 mA |
| Junction capacitance $C_j$ / 结电容 $C_j$ | 0.1–1 pF |
| Optimum frequency $f_{opt}$ / 最佳频率 $f_{opt}$ | 5–100 GHz |
| RF output power / 射频输出功率 | 0.1–10 W (pulsed to 100 W+) |
| Efficiency / 效率 | 10–30% |
| Thermal resistance / 热阻 | 10–30 °C/W |

---

## 10.4 TRAPATT Diode / TRAPATT二极管

### Properties / 特性

- **Lower frequency** than IMPATT (typically $f_{opt}/3$ to $f_{opt}/2$) / 频率低于IMPATT（通常为 $f_{opt}/3$ 到 $f_{opt}/2$）
- **Higher efficiency** (30–75% compared to 10–30% for IMPATT) / 效率更高（30–75%，相比IMPATT的10–30%）
- **Higher power** (up to several kW pulsed) / 功率更高（脉冲可达数kW）
- **Narrower bandwidth** and more critical circuit design / 带宽更窄，电路设计更苛刻

### Comparison / 对比

| Property / 特性 | IMPATT | TRAPATT |
|----------|--------|---------|
| Operating freq. / 工作频率 | 5–100+ GHz | 0.5–20 GHz |
| Efficiency / 效率 | 10–30% | 30–75% |
| Output power / 输出功率 | 0.1–10 W CW | 1 W–1 kW pulsed |
| Noise / 噪声 | High | Higher |
| Bias voltage / 偏压 | 30–150 V | 50–200 V |

---

## 10.5 Circuit Applications / 电路应用

### 10.5.1 Negative-Resistance Oscillator / 负阻振荡器

A negative-resistance device can be modelled as a one-port with small-signal impedance $Z_d = R_d + jX_d$, where $R_d < 0$ in some frequency range.
负阻器件可建模为单端口网络，小信号阻抗 $Z_d = R_d + jX_d$，其中 $R_d < 0$ 在某个频率范围内。

#### Oscillation Condition / 振荡条件

For steady-state oscillation / 对于稳态振荡：

$$Z_d(\omega_0, I_0) + Z_L(\omega_0) = 0 \tag{10.8}$$

$$R_d(\omega_0, I_0) + R_L = 0 \quad \Rightarrow \quad R_L = -R_d \quad (R_d < 0) \tag{10.9a}$$

#### Start-Up Condition / 起振条件

For oscillation to start from noise / 要从噪声开始振荡：

$$R_d(0) + R_L < 0 \quad \Rightarrow \quad R_L < |R_d(0)| \tag{10.10}$$

#### Stabilised Oscillator Design / 稳定化振荡器设计

$$R_L = \frac{|R_d|}{3} \quad \Rightarrow \quad R_d + R_L = -\frac{2}{3}|R_d| \quad \text{(start-up / 起振)} \tag{10.11}$$

### 10.5.2 Negative-Resistance Reflection Amplifier / 负阻反射放大器

A circulator-coupled reflection amplifier uses the negative resistance of the diode / 环行器耦合反射放大器利用二极管的负电阻：

$$\Gamma = \frac{Z_d - Z_0}{Z_d + Z_0} \tag{10.12}$$

Power gain / 功率增益：

$$G = |\Gamma|^2 = \left|\frac{Z_d - Z_0}{Z_d + Z_0}\right|^2 \tag{10.13}$$

### 10.5.3 Injection Locking / 注入锁定

An external signal injected into a free-running negative-resistance oscillator can synchronise (lock) the output / 注入到自由运行负阻振荡器的外部信号可以同步（锁定）输出：

$$\frac{d\phi}{dt} = \Delta\omega - \frac{\omega_0}{2Q}\frac{V_{inj}}{V_{osc}} \sin\phi \tag{10.14}$$

Locking range (Adler's formula) / 锁定范围（Adler公式）：

$$\Delta\omega_{L} = \frac{\omega_0}{2Q} \frac{V_{inj}}{V_{osc}} \tag{10.15}$$

---

## Summary Table / 汇总表

| Device / 器件 | Mechanism / 机制 | Static/Dynamic $R_n$ / 静态/动态 | Freq. Range / 频率范围 | Eff./效率 | Power / 功率 |
|--------|-----------|----------------------|-------------|------|-------|
| Tunnel diode / 隧道二极管 | Quantum tunneling / 量子隧穿 | Static N-type / 静态N型 | 1–10 GHz | Low | mW |
| Gunn diode / 耿氏二极管 | Transferred electron / 转移电子 | Dynamic (bulk) / 动态（体） | 1–100+ GHz | 2–20% | mW–W |
| IMPATT | Avalanche + transit / 雪崩+渡越 | Dynamic / 动态 | 5–100+ GHz | 10–30% | W–10 W |
| TRAPATT | Trapped plasma / 俘获等离子体 | Dynamic / 动态 | 0.5–20 GHz | 30–75% | kW pulsed |

---

## Key Formulas / 关键公式

| Description / 描述 | Formula / 公式 | Eqn / 方程 |
|-------------|---------|-----|
| Tunnel diode current / 隧道二极管电流 | $I(V) = I_p(V/V_p)\exp(1-V/V_p) + I_0[\exp(qV/nkT)-1]$ | (10.1) |
| Negative mobility condition / 负迁移率条件 | $dv/dE < 0$ for $E > E_{th}$ | (10.2) |
| Gunn transit frequency / 耿氏渡越频率 | $f_t = v_{sat}/L$ | (10.4) |
| IMPATT transit angle / IMPATT渡越角 | $\theta = \omega W_d/v_s$ | (10.5) |
| IMPATT optimum frequency / IMPATT最佳频率 | $f_{opt} \approx v_s/(2W_d)$ | (10.6) |
| Oscillation condition / 振荡条件 | $Z_d + Z_L = 0$, $R_L = -R_d$ | (10.9) |
| Start-up condition / 起振条件 | $R_L < |R_d(0)|$ | (10.10) |
| Reflection gain / 反射增益 | $G = |(Z_d - Z_0)/(Z_d + Z_0)|^2$ | (10.13) |
| Injection locking range / 注入锁定范围 | $\Delta\omega_L = (\omega_0/2Q)(V_{inj}/V_{osc})$ | (10.15) |
