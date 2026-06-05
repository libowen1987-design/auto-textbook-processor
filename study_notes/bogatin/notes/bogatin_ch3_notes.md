---
title: "Chapter 3 — Impedance and Electrical Models"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 3
pages: "110–139"
---

# Ch3: Impedance and Electrical Models

> **中英双语版**

## 3.1 What Is Impedance? | 什么是阻抗？

**Impedance** $Z$ is the fundamental electrical property linking physical design to electrical performance. The definition (always true, in any domain):
**阻抗 $Z$** 是将物理设计与电气性能联系起来的基本电气属性。其定义（在任何域中都成立）：

$$
Z = \frac{V}{I}
$$

Units: Ohms ($\Omega$). 单位：欧姆。

The four SI problem families described through impedance:
四种 SI 问题族从阻抗角度描述：
1. **Signal quality:** Reflections when the impedance changes（阻抗变化时产生反射）
2. **Cross talk:** Mutual impedance ($C_m$, $L_m$) between traces（线间互阻抗）
3. **Rail collapse:** PDN impedance × switching current = voltage drop（PDN 阻抗 × 开关电流 = 电压跌落）
4. **EMI:** Ground-plane impedance driving common currents on cables（地平面阻抗驱动电缆上的共模电流）

> **Engineering Intuition:** Impedance is the Rosetta stone that links physical design and electrical performance. Strategy: translate system-performance needs into an impedance requirement, and physical design into an impedance property.
> **工程直觉：** 阻抗是连接物理设计与电气性能的罗塞塔石碑。策略：将系统性能需求转换为阻抗需求，将物理设计转换为阻抗特性。

## 3.2 Real vs. Ideal Circuit Elements | 真实 vs. 理想电路元件

- **Real devices:** can be measured. They are the actual hardware.（**真实器件：** 可被测量，是实际硬件）
- **Ideal elements:** mathematical descriptions used in simulators (SPICE). Can only be calculated.（**理想元件：** 用于仿真器的数学描述，只能被计算）

| Ideal Element | Symbol | Unit | Definition | 定义 |
|:--|:--:|:--:|:--|:--|
| Resistor | R | Ohm ($\Omega$) | $V = I \cdot R$ | 电阻 |
| Capacitor | C | Farad (F) | $Q = C \cdot V$, $I = C \cdot dV/dt$ | 电容 |
| Inductor | L | Henry (H) | $V = L \cdot dI/dt$ | 电感 |
| Transmission line | T | $\Omega$ | Distributed; covered in Ch7 | 传输线（分布参数） |

> **Engineering Intuition:** Only real devices can be measured; only ideal elements can be calculated. Our goal: create a model whose impedance closely matches the measured impedance of the real device.
> **工程直觉：** 只有真实器件可以被测量；只有理想元件可以被计算。我们的目标是：建立一个模型，使其阻抗在宽频段内与实际器件的测量阻抗高度吻合。

## 3.3 Impedance in the Time Domain | 时域阻抗

| Element | $Z_{\text{TD}}$ | Insight | 理解 |
|:--|:--|:--|:--|
| R | $Z = R$ | Constant, boring | 恒定，乏味 |
| C | $Z = \dfrac{V}{C \cdot dV/dt}$ | Depends on waveform shape — **complicated** | 依赖波形形状——复杂 |
| L | $Z = \dfrac{L \cdot dI/dt}{I}$ | Depends on waveform shape — **complicated** | 依赖波形形状——复杂 |

> **Engineering Intuition:** Impedance of C and L in the time domain is NOT simple. This is why we move to the frequency domain.
> **工程直觉：** C 和 L 在时域中的阻抗并不简单。这就是我们转到频域的原因。

## 3.4 Impedance in the Frequency Domain (Sine Wave Excitation) | 频域阻抗（正弦激励）

Angular frequency: $\omega = 2\pi f$（角频率）

| Element | $Z(\omega)$ (complex) | Magnitude | Phase | 相位 |
|:--|:--:|:--:|:--|:--|
| R | $R$ | $R$ | $0^\circ$ | 阻性 |
| C | $1 / (j\omega C)$ | $1/(\omega C)$ | $-90^\circ$ (capacitive) | 容性 |
| L | $j\omega L$ | $\omega L$ | $+90^\circ$ (inductive) | 感性 |

**Key insight:** Even though $C$ and $L$ values are constant with frequency, their **impedances** vary:
**关键洞察：** 虽然 $C$ 和 $L$ 的值不随频率变化，但它们的**阻抗**随频率变化：

$$
|Z_C| = \frac{1}{\omega C} \quad\text{(decreases with frequency | 随频率增大而减小)}
$$
$$
|Z_L| = \omega L \quad\text{(increases with frequency | 随频率增大而增大)}
$$

**Example:** A 10 nF capacitance at 1 GHz:
**示例：** 10 nF 电容在 1 GHz：
$$|Z_C| = 1 / (2\pi \times 10^9 \times 10^{-8}) = 0.016\ \Omega$$

The same capacitor's series 2 nH inductance at 1 GHz:
同一电容的串联 2 nH 电感在 1 GHz：
$$|Z_L| = 2\pi \times 10^9 \times 2\times 10^{-9} = 12.6\ \Omega$$

> **Engineering Intuition:** At high frequencies, the inductor's impedance dominates the real capacitor's behavior. This is why decoupling capacitors have a self-resonant frequency (SRF).
> **工程直觉：** 在高频下，电感阻抗主导实际电容的行为。这就是去耦电容存在自谐振频率（SRF）的原因。

## 3.5 Equivalent Circuit Models (RLC Series) | 等效电路模型（RLC 串联）

Impedance of a series RLC circuit:
串联 RLC 电路的阻抗：

$$
Z(\omega) = R + j\omega L + \frac{1}{j\omega C}
$$

**Self-resonant frequency** (SRF) where $Z_L = Z_C$:
**自谐振频率**（$Z_L = Z_C$ 时的频率）：

$$
f_{\text{SR}} = \frac{1}{2\pi\sqrt{LC}}
$$

At $f < f_{\text{SR}}$: capacitive behavior ($-90^\circ$ phase)（低于 SRF：容性，相位 -90°）
At $f = f_{\text{SR}}$: purely resistive ($Z = R$, $0^\circ$ phase)（等于 SRF：纯阻性）
At $f > f_{\text{SR}}$: inductive behavior ($+90^\circ$ phase)（高于 SRF：感性，相位 +90°）

**Example — 1 nF decoupling capacitor model:**
**示例 — 1 nF 去耦电容模型：**
$$C = 0.67\ \text{nF},\quad R = 0.5\ \Omega,\quad L = 1.78\ \text{nH}$$
$$f_{\text{SR}} = \frac{1}{2\pi\sqrt{1.78\times 10^{-9} \times 0.67\times 10^{-9}}} \approx 145\ \text{MHz}$$

Model bandwidths | 模型带宽：
- 1st-order (just C): $BW \approx 70$ MHz（一阶模型，仅 C）
- 2nd-order (RLC): $BW > 5$ GHz（二阶模型，RLC 串联）

> **Engineering Intuition:** Start with the simplest model first (Einstein's principle: "as simple as possible, but not simpler"). A single C is fine for low frequency; add L and R as bandwidth requirements increase.
> **工程直觉：** 从最简单的模型开始（爱因斯坦原则："尽可能简单，但不能更简单"）。低频时单个 C 就够；随着带宽需求增加，再添加 L 和 R。

## 3.6 Common Model Topologies | 常用模型拓扑

| Component | Low-Frequency Model | High-Frequency Model | 低频/高频模型 |
|:--|:--|:--|:--|
| Real resistor | R | R + L (series) | 实际电阻：R / R+L 串联 |
| Real capacitor | C | R + L + C (series) | 实际电容：C / R+L+C 串联 |
| Real inductor | L | R + L + C (parallel) | 实际电感：L / R+L+C 并联 |
| PCB trace (short) | C | LC ($\pi$ or $T$) | PCB 走线（短）：C / LC |
| Wire bond | L | R + L + C | 键合线：L / R+L+C |

## 3.7 Using SPICE for Impedance Analysis | 使用 SPICE 进行阻抗分析

An impedance analyzer in SPICE:
在 SPICE 中实现阻抗分析的方法：
1. Use a constant-current AC source (1 A amplitude)（使用恒流交流源，1 A 幅值）
2. Connect the circuit under test across its terminals（将待测电路连接到其端子两端）
3. The voltage across the source = impedance in Ohms (since $V = Z \times 1\text{A}$)（源两端电压的数值等于阻抗的欧姆数）

**SPICE simulation types | SPICE 仿真类型：**
- **Transient:** time-domain analysis（瞬态分析：时域）
- **AC:** frequency-domain analysis (swept sine wave)（AC 分析：频域，扫频正弦波）

> **Engineering Intuition:** If the schematic can be drawn, SPICE can simulate it. This is the real power of SPICE for general electrical engineering analysis.
> **工程直觉：** 只要能画出原理图，SPICE 就能仿真。这就是 SPICE 在电气工程分析中的真正威力。

## 3.8 Resistor Technologies and Bandwidth | 电阻技术与带宽

| Resistor Type | Bandwidth as Ideal R | 带宽（作为理想电阻） |
|:--|:--|:--|
| Integrated Passive Device (IPD) | >5 GHz | 集成无源器件 |
| Surface Mount (SMT) | ~2 GHz | 表面贴装 |
| Axial lead | ~500 MHz | 轴向引线 |

## 3.9 Key Formulas | 关键公式

| Formula | Description | 中文说明 |
|:--|:--|:--|
| $Z = V/I$ | Definition of impedance | 阻抗定义 |
| $V = I \cdot R$ | Resistor I-V | 电阻伏安关系 |
| $I = C \cdot dV/dt$ | Capacitor I-V (time domain) | 电容伏安关系（时域） |
| $V = L \cdot dI/dt$ | Inductor I-V (time domain) | 电感伏安关系（时域） |
| $Z_C = 1/(j\omega C)$ | Capacitor impedance (freq domain) | 电容阻抗（频域） |
| $Z_L = j\omega L$ | Inductor impedance (freq domain) | 电感阻抗（频域） |
| $\omega = 2\pi f$ | Angular frequency | 角频率 |
| $f_{\text{SR}} = 1/(2\pi\sqrt{LC})$ | Self-resonant frequency | 自谐振频率 |
| $Z_{\text{RLC}} = R + j\omega L + 1/(j\omega C)$ | Series RLC impedance | 串联 RLC 阻抗 |
