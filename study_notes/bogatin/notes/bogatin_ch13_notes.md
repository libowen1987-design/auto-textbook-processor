---
title: "Chapter 13 — Power Distribution Network (PDN)"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 13
pages: "644–746"
---

# Ch13: PDN — Power Distribution Network

> **中英双语版**

## 13.1 PDN Goal | PDN 的目标

Deliver **constant voltage** ($V_{\text{dd}}$ to $V_{\text{ss}}$) at each chip's pads with ripple < 5%.
在每个芯片的焊盘处提供**恒定电压**（$V_{\text{dd}}$ 与 $V_{\text{ss}}$ 之间），纹波 < 5%。

**Target impedance | 目标阻抗：**
$$
Z_{\text{target}} = \frac{V_{\text{dd}} \times \text{Ripple\%}}{\Delta I}
$$

目标阻抗 = 供电电压 × 允许纹波百分比 / 电流变化量。这是 PDN 设计的基本约束。

## 13.2 PDN Impedance Components | PDN 阻抗组成

The PDN impedance across frequency comes from:
PDN 在全频段内的阻抗由以下部分组成：

1. **VRM (voltage regulator module):** good at DC to ~1 kHz（稳压电源模块：DC ~ 1 kHz 有效）
2. **Bulk capacitors:** good ~1 kHz to ~1 MHz（大容量电容：1 kHz ~ 1 MHz 有效）
3. **MLCC decoupling capacitors:** good ~1 MHz to ~100 MHz（MLCC 去耦电容：1 MHz ~ 100 MHz 有效）
4. **On-chip / on-package capacitance:** good >100 MHz（芯片内/封装内电容：>100 MHz 有效）
5. **Power/ground planes:** provide low inductance at all frequencies（电源/地平面：全频段提供低电感）

## 13.3 Decoupling Capacitor Model | 去耦电容模型

Real capacitor = $R_{\text{ESR}} + L_{\text{ESL}} + C$ in series.
实际电容等效为 $R_{\text{ESR}} + L_{\text{ESL}} + C$ 串联。

**Self-resonant frequency:** $f_{\text{SR}} = 1/(2\pi\sqrt{L_{\text{ESL}} \cdot C})$
**自谐振频率：** 电容的容性与感性阻抗在此频率恰好抵消。

**Above SRF:** $|Z| \approx \omega \cdot L_{\text{ESL}}$ (inductive, independent of $C$)
**高于自谐振频率：** 阻抗呈感性，仅取决于 ESL，与电容值无关。

> **Engineering Intuition:** At high frequency (>100 MHz), ALL capacitors of the same package size have the SAME impedance. The ONLY knob is ESL, not capacitance value.
> **工程直觉：** 在高频 (>100 MHz) 下，所有相同封装尺寸的电容阻抗**完全一样**。唯一可调的参数是 ESL，而不是电容值。

## 13.4 MLCC Capacitor ESL | MLCC 电容的 ESL

| Package | Typical ESL (nH) |
|:--|:--:|
| 1206 | ~1.5 |
| 0805 | ~1.0 |
| 0603 | ~0.7 |
| 0402 | ~0.4 |
| 0201 | ~0.2 |

封装越小，ESL 越低，高频性能越好。

**Total ESL in parallel:** $L_{\text{eq}} \approx (\text{ESL} + L_{\text{mounting}})/N$
**并联总 ESL：** 等于单颗 ESL 加安装电感之和除以并联数量。

## 13.5 PDN Design Strategies | PDN 设计策略

1. **Close power/ground planes:** thin dielectric → low loop inductance per square ($L_{\text{sq}} = \mu_0 h$)
   电源/地平面靠紧：薄介质 → 单位方块的环路电感低
2. **Multiple decaps in parallel:** reduce effective ESL（多颗去耦电容并联：降低等效 ESL）
3. **Short vias:** keep planes near surface（短过孔：将电源/地平面靠近表面层）
4. **On-package decoupling:** best for >100 MHz（封装上去耦：>100 MHz 效果最佳）
5. **On-chip decoupling:** best for >1 GHz（芯片内去耦：>1 GHz 效果最佳）

## 13.6 Decoupling Time Equation | 去耦时间方程

$$
\Delta t \approx \frac{C \cdot 0.05 \cdot V^2}{P}
$$

**Required capacitance for given decoupling time:**
**给定去耦时间所需的电容值：**
$$
C = \frac{1}{0.05} \cdot \frac{P}{V^2} \cdot \Delta t
$$

## 13.7 FDTI Method (Fast Decoupling Threshold Identification) | FDTI 方法

Practical method: determine how many decoupling capacitors are actually needed by computing the impedance profile of the PDN and checking against $Z_{\text{target}}$.
实用方法：通过计算 PDN 阻抗曲线并与 $Z_{\text{target}}$ 对比，确定实际所需的去耦电容数量。

## 13.8 Key Rules of Thumb | 关键经验法则

| Rule | Value | 中文说明 |
|:--|:--|:--|
| Target impedance trend | Decreases ~10× every 6 years | 目标阻抗每 6 年降低约 10 倍 |
| MLCC ESL (0402) | ~0.4 nH | 0402 封装的 ESL 约 0.4 nH |
| Plane inductance per square (2 mil) | ~64 pH | 2 mil 间距电源平面每方块电感约 64 pH |
| Decoupling capacitor spacing | Closer to chip = better | 去耦电容越靠近芯片越好 |
| Number of caps needed | Determined by ESL, not capacitance | 所需电容数量由 ESL 决定，而非电容值 |

> **Engineering Intuition:** PDN design is about INDUCTANCE, not capacitance. The capacitance value determines the low-frequency impedance; the ESL determines the high-frequency impedance. At high frequency, a 1 nF cap with 0.4 nH ESL and a 100 nF cap with 0.4 nH ESL look IDENTICAL.
> **工程直觉：** PDN 设计的核心是**电感**而非电容。电容值决定低频阻抗，ESL 决定高频阻抗。在高频下，ESL 同为 0.4 nH 的 1 nF 电容和 100 nF 电容的高频阻抗**完全相同**。

## 13.9 Key Formulas | 关键公式

| Formula | Description | 中文说明 |
|:--|:--|:--|
| $Z_{\text{target}} = V_{\text{dd}} \cdot \text{Ripple} / \Delta I$ | PDN target impedance | PDN 目标阻抗 |
| $f_{\text{SR}} = 1/(2\pi\sqrt{L_{\text{ESL}} C})$ | Self-resonant frequency | 自谐振频率 |
| $|Z|_{\text{above SRF}} \approx \omega L_{\text{ESL}}$ | High-frequency impedance | 高频阻抗 |
| $L_{\text{eq}} = (\text{ESL} + L_{\text{via}})/N$ | Parallel decaps | 并联去耦等效电感 |
| $\Delta t = 0.05 \cdot C \cdot V^2 / P$ | Decoupling time | 去耦持续时间 |
| $L_{\text{sq}} = \mu_0 h$ | Plane inductance per square | 单位方块平面电感 |
