---
title: "Chapter 9 — Lossy Lines"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 9
pages: "366–432"
---

# Ch9: Lossy Lines

> **中英双语版**

## 9.1 Two Loss Mechanisms | 两种损耗机制

1. **Conductor loss (skin effect):** $R(f) \propto \sqrt{f}$
2. **Dielectric loss:** $G(f) \propto f$ (dissipation factor $\tan \delta$)

**导体损耗（趋肤效应）：** 电阻随频率平方根增大；**介质损耗：** 电导随频率线性增大，取决于损耗角正切 $\tan \delta$。

**Total attenuation constant | 总衰减常数：**
$$
\alpha(f) = \alpha_{\text{cond}} + \alpha_{\text{diel}} = k_1 \sqrt{f} + k_2 f
$$

总衰减为导体衰减与介质衰减之和，分别在低频和高频段起主导作用。

## 9.2 Skin Effect Resistance | 趋肤效应电阻

$$
R_{\text{HF}}(f) = \frac{\rho}{w \cdot \delta(f)}, \quad \delta(f) = \sqrt{\frac{1}{\pi f \mu \sigma}}
$$

高频电阻反比于导体宽度与趋肤深度的乘积。趋肤深度 $\delta$ 随频率增大而减小。

For copper: $\delta(\mu\text{m}) = 66 / \sqrt{f(\text{MHz})}$
—— 对铜而言，$f=1\text{ GHz}$ 时趋肤深度约 $2.1\ \mu\text{m}$。

## 9.3 Dielectric Loss | 介质损耗

**Dissipation factor** $\tan \delta$: measure of how "lossy" a dielectric is.
**损耗角正切 $\tan \delta$：** 衡量介质损耗程度的参数，数值越大损耗越严重。

| Material | $\tan \delta$ (at 1 GHz) |
|:--|:--|
| FR4 | 0.02 |
| Rogers 4350B | 0.0037 |
| Megtron 6 | 0.002 |
| PTFE | 0.0002 |

**Dielectric attenuation:** $\alpha_{\text{diel}} \approx 2.3 \cdot f \cdot \tan \delta \cdot \sqrt{\epsilon_r}$ (dB/inch)
**介质衰减经验公式：** 与频率 $\cdot$ 损耗角正切 $\cdot$ 介电常数平方根成正比。

## 9.4 Intersymbol Interference (ISI) | 码间干扰

Loss attenuates high frequencies more than low → rise time degradation → bits "smear" into adjacent bit periods → ISI.
损耗对高频衰减更大 → 上升时间退化 → 码元"拖尾"进入相邻码元周期 → 码间干扰。

**ISI threshold:** When $RT_{\text{degraded}} \approx$ bit period / 2, the eye closes.
**ISI 阈值：** 当退化后的上升时间约等于码元周期的一半时，眼图闭合。

## 9.5 Eye Diagram | 眼图

- **Vertical eye opening | 垂直眼宽：** decreases with loss（随损耗增大而减小）
- **Horizontal eye opening (jitter) | 水平眼宽（抖动）：** increases with loss（随损耗增大而增大）
- Deterministic jitter from loss + impedance discontinuities（确定性抖动来源于损耗和阻抗不连续性的共同作用）

## 9.6 Equalization and Pre-Emphasis | 均衡与预加重

**Equalization | 均衡：** Filter that attenuates low frequencies to match high-frequency loss (passive or active).
对低频分量进行衰减以匹配高频损耗的滤波器（无源或有源）。

**Pre-emphasis (de-emphasis) | 预加重（去加重）：** Boost high-frequency components at the transmitter to compensate for channel loss.
在发射端提升高频分量以补偿信道损耗。

> **Engineering Intuition:** Lossy lines are THE dominant SI problem for >1 Gbps serial links over >10 inches. The solution is either better materials (low-loss laminate) or signal processing (equalization).
> **工程直觉：** 损耗线是高于 1 Gbps、长度超过 10 英寸的串行链路中最主要的 SI 问题。解决方案要么是更好的材料（低损耗层压板），要么是信号处理（均衡）。

## 9.7 Key Formulas | 关键公式

| Formula | Description | 中文说明 |
|:--|:--|:--|
| $\delta = \sqrt{1/(\pi f \mu \sigma)}$ | Skin depth | 趋肤深度 |
| $R_{\text{AC}} \propto \sqrt{f}$ | Skin effect resistance | 趋肤效应电阻 |
| $\alpha_{\text{total}} = \alpha_{\text{cond}} + \alpha_{\text{diel}}$ | Total attenuation | 总衰减常数 |
| $\alpha_{\text{diel}} \propto f \cdot \tan \delta$ | Dielectric loss | 介质损耗 |
| $RT_{\text{out}} = \sqrt{RT_{\text{in}}^2 + RT_{\text{line}}^2}$ | Rise time degradation | 上升时间退化 |
