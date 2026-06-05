---
title: "Chapter 6 — The Physical Basis of Inductance"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 6
pages: "180–235"
---

# Ch6: The Physical Basis of Inductance

> **中英双语版**

## 6.1 Three Fundamental Principles | 三个基本原理

**Principle #1:** There are circular rings of magnetic-field lines around all currents. Counted in **Webers**. Direction by right-hand rule.
**原理 1：** 所有电流周围都存在环形的磁力线，以**韦伯**计量，方向由右手定则确定。

**Principle #2:** Inductance = number of Webers of field line rings around a conductor per Amp of current:
**原理 2：** 电感 = 导体周围磁力线环的韦伯数除以电流安培数：

$$
L = \frac{\Psi}{I}
$$

Inductance is a **geometric property** — independent of current magnitude, depends only on conductor geometry and (for ferromagnetic materials) permeability.
电感是**几何属性**——与电流大小无关，仅取决于导体几何形状和（对于铁磁性材料）磁导率。

**Principle #3:** When the number of field line rings around a conductor changes, a voltage is induced across its ends:
**原理 3：** 当导体周围磁力线环数变化时，其两端感应出电压：

$$
V = \frac{d\Psi}{dt} = L\frac{dI}{dt}
$$

> **Engineering Intuition:** "An inductor resists a change in current." This induced voltage is the root cause of transmission line effects, cross talk, switching noise, rail collapse, ground bounce, and EMI.
> **工程直觉：** "电感抵抗电流的变化"。这个感应电压是传输线效应、串扰、开关噪声、电源塌陷、地弹和 EMI 的根本原因。

## 6.2 Types of Inductance | 电感的类型

| Type | Description | Measurable? | 可测量？ |
|:--|:--|:--:|:--|
| **Self-inductance** | Field rings from a wire's own current | ✓ (partial) | 自感 |
| **Mutual inductance** | Field rings around one wire from another's current | ✓ (partial) | 互感 |
| **Partial inductance** | Field rings around a segment, ignoring the rest of the loop | No | 部分电感（数学概念） |
| **Loop inductance** | Total field rings around the complete current loop | Yes | 环路电感 |
| **Effective/net/total inductance** | Field rings around one leg of a loop, from all segments | Yes | 有效/净/总电感 |
| **Equivalent inductance** | Combined inductance of series/parallel inductors with mutual | Yes | 等效电感 |

## 6.3 Partial Self-Inductance | 部分自感

**Round rod approximation | 圆杆近似：**

$$
L \approx 5d\left[\ln\left(\frac{2d}{r}\right) - \frac{3}{4}\right] \quad \text{[nH]}
$$

$d$ = length (inches), $r$ = radius (inches).（$d$ 为长度，$r$ 为半径，单位英寸）

**Rule of thumb:** ~25 nH/inch or ~1 nH/mm for a narrow wire.
**经验法则：** 细导线约 25 nH/英寸 或 1 nH/毫米。

**Example:** 1-inch, 10-mil diameter wire: $L \approx 26$ nH.
**示例：** 1 英寸长、10 mil 直径的导线：L ≈ 26 nH。

> **Engineering Intuition:** The more spread out the current distribution, the lower the partial self-inductance. Making wires wider reduces inductance; making them longer increases it faster than linearly.
> **工程直觉：** 电流分布越分散，部分自感越低。加宽导线降低电感；加长导线使电感超线性增加。

## 6.4 Partial Mutual Inductance | 部分互感

Between two parallel round rods (same length $d$, center spacing $s$):
两根平行圆杆之间（相同长度 $d$，中心间距 $s$）：

$$
M \approx 5d\left[\ln\left(\frac{2d}{s}\right) - 1 + \frac{s}{d} - \left(\frac{s}{2d}\right)^2\right] \quad \text{[nH]}
$$

**Rule of thumb:** If $s > d$, mutual inductance is <10% of self-inductance and can be ignored.
**经验法则：** 若 $s > d$，互感小于自感的 10%，可以忽略。

## 6.5 Effective Inductance and Ground Bounce | 有效电感与地弹

For a signal/return loop with legs $a$ and $b$:
对于信号/返回回路，路径 $a$ 和 $b$：

$$
L_{\text{total},b} = L_b - L_{ab}
$$

**Ground bounce voltage** across the return path:
返回路径两端的**地弹电压**：

$$
V_{\text{gb}} = L_{\text{total}} \frac{dI}{dt}
$$

To **decrease ground bounce**:
**降低地弹的方法：**
1. Decrease $L_b$ (short, wide return path — use planes)（减小 $L_b$：短而宽的返回路径——使用平面）
2. Increase $L_{ab}$ (bring signal and return paths closer together)（增大 $L_{ab}$：将信号与返回路径靠拢）

**Example:** Two 100-mil wire bonds, 1-mil diameter:
**示例：** 两根 100 mil 长的键合线，1 mil 直径：
- $s = 100$ mils → $L_{\text{total}} \approx 2.5$ nH, $V_{\text{gb}} = 250$ mV (for 100 mA, 1 nsec)
- $s = 5$ mils → $L_{\text{total}} \approx 1.3$ nH, $V_{\text{gb}} = 130$ mV

> **Engineering Intuition:** For opposite-direction currents (signal+return): bring them close. For same-direction currents (multiple power wires): keep them apart (spacing ≥ length).
> **工程直觉：** 对于反向电流（信号 + 返回）：使它们靠近。对于同向电流（多根电源线）：使它们远离（间距 ≥ 长度）。

## 6.6 Loop Self-Inductance | 环路自感

**Circular loop | 圆形环路：**

$$
L_{\text{loop}} \approx 32R\ln\left(\frac{4R}{D}\right) \quad [\text{nH}]
$$

$R$ = radius (inches), $D$ = wire diameter (inches).（$R$ 为半径，$D$ 为导线直径，单位英寸）

**Rule of thumb:** A 1-inch finger-circle loop has $L \approx 85$ nH (~25 nH/inch of circumference).
**经验法则：** 1 英寸手指环的环路电感约 85 nH（约 25 nH/英寸周长）。

**Two parallel rods (signal + return) | 两根平行杆（信号 + 返回）：**

$$
L_{\text{loop}} \approx 10 \cdot \text{len} \cdot \ln\left(\frac{s}{r}\right) \quad [\text{nH}]
$$

**Two wide planes ($w \gg h$) | 两个宽平面：**

$$
L_{\text{loop}} \approx \mu_0 h \frac{\text{Len}}{w}
$$

$\mu_0 = 32$ pH/mil.

**Loop inductance per square of planes | 单位方块平面环路电感：** $L_{\text{sq}} = \mu_0 \cdot h$

| Spacing $h$ (mils) | $L_{\text{sq}}$ (pH) | 间距 |
|:--:|:--:|:--:|
| 2 | 64 | 2 mil |
| 5 | 160 | 5 mil |
| 10 | 320 | 10 mil |

## 6.7 PDN and Decoupling Capacitor Inductance | PDN 与去耦电容电感

**Required capacitance for decoupling time $\Delta t$ (5% droop):**
**去耦时间 $\Delta t$（5% 跌落）所需的电容：**

$$
C = \frac{1}{0.05} \cdot \frac{P}{V^2} \cdot \Delta t
$$

**Self-resonant frequency (SRF) of a real capacitor:**
**实际电容的自谐振频率（SRF）：**

Above SRF, impedance = $|Z| = \omega \cdot \text{ESL}$. To decrease high-frequency impedance, decrease **loop inductance** (ESL), not increase capacitance.
高于 SRF 时，阻抗 $|Z| = \omega \cdot \text{ESL}$。降低高频阻抗要靠减小**环路电感**（ESL），而非增大电容。

| Method to Reduce ESL | Effect | 方法 |
|:--|:--|:--|
| Short vias (planes near surface) | Major | 短过孔（平面靠近表面） |
| Small body-size capacitors | Major | 小封装电容 |
| Short pad-to-via connections | Major | 短焊盘到过孔连接 |
| Multiple capacitors in parallel | Inverse with number | 多颗电容并联 |
| Closely spaced power/ground planes | Major | 紧耦合电源/地平面 |

> **Engineering Intuition:** At high frequency, ALL capacitors have the same impedance — determined solely by their mounting inductance. Six different capacitor values (10 pF to 1 µF) all converge to the same impedance above SRF.
> **工程直觉：** 高频下，所有电容的阻抗都相同——仅由安装电感决定。六种不同容值（10 pF 到 1 µF）在 SRF 以上阻抗完全收敛。

## 6.8 Skin Depth and Current Distribution | 趋肤深度与电流分布

**Skin depth in copper | 铜的趋肤深度：**

$$
\delta = \frac{66\ \mu\text{m}}{\sqrt{f\ \text{(MHz)}}}
$$

| $f$ | $\delta$ in Cu | Effect on 1-oz Cu (35 $\mu$m) | 对 1 oz 铜箔的影响 |
|:--:|:--:|:--|:--|
| 1 MHz | 66 $\mu$m | Uniform current | 电流均匀 |
| 10 MHz | 21 $\mu$m | Skin-limiting begins | 趋肤效应开始 |
| 100 MHz | 6.6 $\mu$m | Skin-depth regime | 趋肤深度主导 |
| 1 GHz | 2.1 $\mu$m | Strong skin effect | 强趋肤效应 |

**High-frequency resistance:** $R_{\text{HF}} = \rho / (w \cdot \delta)$ increases as $\sqrt{f}$.
**高频电阻：** $R_{\text{HF}} = \rho / (w \cdot \delta)$，随 $\sqrt{f}$ 增大。

> **Engineering Intuition:** At AC, current takes the path of lowest impedance = lowest loop inductance. This pushes current to the outer surface of conductors and pulls signal and return currents together. A 5-mil-wide, 1-oz trace has 15× higher resistance at 1 GHz than at DC.
> **工程直觉：** 交流下，电流走最低阻抗路径 = 最低环路电感。这使电流挤向导体外表面，并使信号和返回电流相互拉近。5 mil 宽、1 oz 走线在 1 GHz 的电阻是 DC 下的 15 倍。

## 6.9 Eddy Currents | 涡流

A changing current near a conducting plane induces **eddy currents** in the plane. These can be modeled as an **image current** at $h$ below the plane, opposite direction. The closer the plane, the lower the loop inductance — even if the plane is floating.
导电平面附近的时变电流在平面中感应出**涡流**。可建模为平面下方 $h$ 处的**镜像电流**，方向相反。平面越近，环路电感越低——即使平面是浮空的。

**Rule of thumb:** Eddy currents matter when spacing to the plane is less than the total conductor span.
**经验法则：** 当间距小于导体总跨度时，涡流效应显著。

## 6.10 High-Permeability Materials | 高磁导率材料

Only iron, nickel, cobalt, and their alloys (Kovar, Alloy 42) have $\mu_r > 1$. They have:
只有铁、镍、钴及其合金（Kovar、Alloy 42）的 $\mu_r > 1$。它们具有：
- Much smaller skin depth (e.g., nickel: $\delta \approx 13\ \mu\text{m}/\sqrt{f}$)（更小的趋肤深度）
- Much higher high-frequency resistance（更高高频电阻）
- But the **high-frequency loop inductance** is the same as copper (external fields dominate)
  但**高频环路电感**与铜相同（外部场占主导）

> **Engineering Intuition:** A Ni/Au plating on traces doesn't affect electrical properties — current flows in the copper below. But solid Alloy 42 or Kovar leads have very high resistance at high frequencies.
> **工程直觉：** 走线上的 Ni/Au 镀层不影响电气特性——电流在下面的铜中流动。但实心 Alloy 42 或 Kovar 引线在高频下电阻非常高。

## 6.11 Key Formulas | 关键公式

| Formula | Description | 中文说明 |
|:--|:--|:--|
| $L = \Psi / I$ | Inductance definition | 电感定义 |
| $V = L \cdot dI/dt$ | Induced voltage | 感应电压 |
| $V_{\text{noise}} = M \cdot dI/dt$ | Crosstalk from mutual inductance | 互感串扰 |
| $L_{\text{total},b} = L_b - L_{ab}$ | Total inductance of return path | 返回路径总电感 |
| $L_{\text{loop}} = L_a + L_b - 2L_{ab}$ | Loop inductance | 环路电感 |
| $L_{\text{loop,sq}} = \mu_0 h$ | Loop inductance per square of planes | 单位方块平面环路电感 |
| $\delta = \sqrt{1/(\pi f \mu \sigma)}$ | Skin depth | 趋肤深度 |
| $\Delta t \approx C \cdot 0.05 V^2 / P$ | Decoupling time | 去耦时间 |
