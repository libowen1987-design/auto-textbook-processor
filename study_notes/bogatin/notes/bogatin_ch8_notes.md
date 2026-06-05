---
title: "Chapter 8 — Transmission Lines and Reflections"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 8
pages: "310–363"
---

# Ch8: Transmission Lines and Reflections

> **中英双语版**

## 8.1 Reflection Coefficient | 反射系数

When a signal traveling in impedance $Z_1$ encounters impedance $Z_2$:
当信号在阻抗 $Z_1$ 中传播时遇到阻抗 $Z_2$：

**Reflection coefficient | 反射系数：**
$$
\rho = \frac{V_{\text{refl}}}{V_{\text{inc}}} = \frac{Z_2 - Z_1}{Z_2 + Z_1}
$$

**Transmission coefficient | 传输系数：**
$$
\tau = \frac{V_{\text{trans}}}{V_{\text{inc}}} = \frac{2 Z_2}{Z_2 + Z_1}
$$

**Special cases** (for $Z_1 = 50\ \Omega$)：
**特殊情况（$Z_1 = 50\ \Omega$）：**

| $Z_2$ | $\rho$ | $V_{\text{end}}$ (for $V_{\text{inc}}=1$V) | 说明 |
|:--:|:--:|:--:|:--|
| Open ($\infty$) | +1 | 2V | 开路，全反射（同相） |
| Short (0) | -1 | 0V | 短路，全反射（反相） |
| 50 $\Omega$ | 0 | 1V | 匹配，无反射 |
| 25 $\Omega$ | -1/3 | 0.67V | 低阻抗部分反射 |
| 75 $\Omega$ | +0.2 | 1.2V | 高阻抗部分反射 |

> **Engineering Intuition:** Reflections exist to maintain voltage continuity and current continuity at an impedance interface. Without reflections, Maxwell's equations would be violated.
> **工程直觉：** 反射存在的意义是在阻抗界面处维持电压连续性和电流连续性。如果没有反射，麦克斯韦方程组将被违反。

## 8.2 Bounce Diagrams | 反弹图

Tracking multiple reflections: source impedance $R_s$, line $Z_0$, far-end impedance $Z_L$.
追踪多次反射过程：源阻抗 $R_s$、线阻抗 $Z_0$、远端阻抗 $Z_L$。

Initial launched voltage: $V_{\text{launched}} = V_s \cdot Z_0 / (R_s + Z_0)$
初始发射电压由源电压按阻抗分压确定。

**Example:** $V_s=1$V, $R_s=10\Omega$, $Z_0=50\Omega$, open far end, TD=1 nsec:
**示例：**
- $V_{\text{launch}} = 0.84$ V（初始发射电压）
- After TD=1 ns: end voltage = $0.84 + 0.84 = 1.68$ V（1 TD 后远端电压）
- After 2TD: source refl = $-0.67 \times 0.84 = -0.56$ V（2 TD 后源端反射）
- After 3TD: end voltage = $1.68 - 0.56 - 0.56 = 0.56$ V（3 TD 后远端电压）
- Eventually converges to 1V（最终收敛到 1V）

## 8.3 When to Terminate | 何时需要端接

**Critical rule of thumb:** Termination needed when the **time delay of the line > 20% of the rise time**.
**关键经验法则：** 当**传输线时延 > 上升时间的 20%** 时需要端接。

$$
\text{Len}_{\text{max}} \approx RT \quad \text{(inches when RT in nsec)}
$$

最大不端接长度（英寸）≈ 上升时间（纳秒）。

| RT (nsec) | Max unterminated length | 最大不端接长度 |
|:--:|:--:|:--:|
| 10 | 10 inches | 10 英寸 |
| 1 | 1 inch | 1 英寸 |
| 0.5 | 0.5 inch | 0.5 英寸 |
| 0.1 | 0.1 inch | 0.1 英寸 |

> **Engineering Intuition:** With 0.1 nsec rise times common today, virtually EVERY trace needs termination. This is why SI matters now.
> **工程直觉：** 当今 0.1 ns 上升时间已很常见，几乎**每条走线**都需要端接。这就是 SI 如今至关重要的原因。

## 8.4 Source-Series Termination | 源端串联端接

The most common termination for point-to-point topology. Add resistor $R_T$ such that:
点对点拓扑中最常用的端接方式。串联电阻 $R_T$ 使得：

$$
R_T + R_{\text{source}} = Z_0
$$

**Example:** $R_{\text{source}} = 10\ \Omega$, $Z_0 = 50\ \Omega$ → $R_T = 40\ \Omega$.
**示例：** 源阻抗 10 Ω，线阻抗 50 Ω → 串联 40 Ω 电阻。

- Half voltage launched (0.5V for 1V source)（发射半电压，1V 源 → 0.5V 入射）
- At far-end open: voltage doubles to full 1V（远端开路，电压倍增至满摆幅 1V）
- Reflected wave sees matched impedance at source → absorbed, no further reflections（反射波在源端看到匹配阻抗 → 被吸收，无后续反射）
- **Result:** Clean 1V signal at receiver, no ringing（**结果：** 接收端得到干净的 1V 信号，无振铃）

## 8.5 Discontinuity Rules | 不连续性规则

| Feature | Key Rule | Len$_{\text{max}}$ | 中文说明 |
|:--|:--|:--:|:--|
| Series TL (neck-down) | TD < 20% RT | $\approx RT$ inches | 串联传输线（窄线） |
| Stub | Length < 20% of $RT \cdot v$ | $\approx RT$ inches | 短桩线 |
| Capacitive load | $C_{\text{load}}$ small enough | Simulate | 容性负载 → 仿真确定 |

## 8.6 TDR (Time Domain Reflectometer) | 时域反射计

A TDR = fast step generator + sampling scope. It measures reflected voltage vs. time, which maps to impedance vs. position.
TDR 由快沿阶跃脉冲发生器和采样示波器组成，测量反射电压随时间的变化，映射为阻抗沿位置的分布。

**Key relationships | 关键关系：**
- Open → +reflection (voltage goes up)（开路 → 正反射，电压升高）
- Short → -reflection (voltage goes down)（短路 → 负反射，电压降低）
- Matched → no reflection（匹配 → 无反射）
- Time axis = round-trip delay to discontinuities（时间轴 = 到不连续点的往返时延）

## 8.7 Key Formulas | 关键公式

| Formula | Description | 中文说明 |
|:--|:--|:--|
| $\rho = (Z_2 - Z_1)/(Z_2 + Z_1)$ | Reflection coefficient | 反射系数 |
| $\tau = 2Z_2/(Z_2 + Z_1)$ | Transmission coefficient | 传输系数 |
| $V_{\text{launch}} = V_s \cdot Z_0/(R_s + Z_0)$ | Initial launched voltage | 初始发射电压 |
| $R_T + R_s = Z_0$ | Source-series termination | 源端串联端接条件 |
| $\text{Len}_{\text{max}} \approx RT$ (in) | Max unterminated/discontinuity length | 最大不端接长度 |
| $\text{Len}_{\text{stub,max}} \approx RT$ (in) | Max stub length | 最大短桩线长度 |
