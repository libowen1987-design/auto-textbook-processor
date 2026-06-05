---
title: "Chapter 10 — Cross Talk"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 10
pages: "434–503"
---

# Ch10: Cross Talk

> **中英双语版**

## 10.1 Capacitive and Inductive Coupling | 容性与感性耦合

Cross talk arises from:
串扰来源于以下两种耦合机制：

- **Mutual capacitance** $C_m$: couples voltage noise through displacement current
  **互容 $C_m$：** 通过位移电流耦合电压噪声
- **Mutual inductance** $L_m$: couples current noise through induced voltage
  **互感 $L_m$：** 通过感应电压耦合电流噪声

## 10.2 NEXT and FEXT | 近端串扰与远端串扰

**Near-end cross talk (NEXT):** Noise at the same end as the driver (backward).
**近端串扰 NEXT：** 与驱动端同侧的噪声（向后传播）。

**Far-end cross talk (FEXT):** Noise at the opposite end from the driver (forward).
**远端串扰 FEXT：** 与驱动端异侧的噪声（向前传播）。

**For uniform transmission lines with ideal return plane | 理想返回平面的均匀传输线：**

$$
\text{NEXT} \propto \frac{1}{4} \left(\frac{C_m}{C_L} + \frac{L_m}{L_L}\right)
$$

$$
\text{FEXT} \propto \frac{1}{2} \cdot \frac{\text{TD}_{\text{coupled}}}{\text{RT}} \cdot \left(\frac{C_m}{C_L} - \frac{L_m}{L_L}\right)
$$

For microstrip: $C_m/C_L \neq L_m/L_L$ → both NEXT and FEXT exist.
微带线中容性与感性耦合比例不等 → NEXT 和 FEXT 同时存在。

For stripline: $C_m/C_L = L_m/L_L$ → FEXT cancels (no FEXT in homogeneous medium).
带状线中两者相等 → FEXT 抵消（均匀介质中无远端串扰）。

## 10.3 Saturation Length | 饱和长度

NEXT grows linearly with coupled length until **saturation length** = half the spatial extent of the rising edge:
NEXT 随耦合长度线性增长直到**饱和长度**，等于上升沿空间延伸的一半：

$$
\text{Len}_{\text{sat}} = \frac{RT \cdot v}{2}
$$

Beyond this, NEXT is constant (saturated).
超过此长度后，NEXT 保持不变（饱和）。

## 10.4 Key Design Rules | 关键设计规则

| Goal | Action | 中文说明 |
|:--|:--|:--|
| Reduce NEXT by 50% | Double the trace spacing | NEXT 减半 → 间距加倍 |
| Keep NEXT < 5% (50-Ohm bus) | Spacing $\ge 2 \times$ line width | NEXT < 5% → 间距 ≥ 2 倍线宽 |
| Keep FEXT < 5% | Keep coupled TD < RT | FEXT < 5% → 耦合时延 < 上升时间 |
| Reduce cross talk | Use stripline (homogeneous) | 减小串扰 → 使用带状线（均匀介质） |
| Tightly coupled bus | 95% of noise from nearest neighbors only | 紧耦合总线中 95% 噪声仅来自最近邻线 |

## 10.5 Switching Noise (SSN/SSO) | 开关噪声

When return paths are not ideal planes (connectors, packages):
当返回路径不是理想平面时（连接器、封装）：

- Inductive coupling dominates over capacitive coupling（感性耦合主导，容性耦合退居次要）
- Ground bounce / SSN / SSO noise（地弹 / 同步开关噪声）
- $V_{\text{noise}} = M_{ab} \cdot dI/dt$（噪声电压 = 互感 × 电流变化率）

> **Engineering Intuition:** The best cross talk reduction is spacing. In connectors/packages where spacing can't increase, SSN becomes the dominant problem. Differential signaling helps.
> **工程直觉：** 减小串扰的最佳手段是拉开间距。当连接器/封装中无法增大间距时，SSN 成为主要矛盾。差分信号可以有效缓解。

## 10.6 Key Formulas | 关键公式

| Formula | Description | 中文说明 |
|:--|:--|:--|
| $\text{NEXT} \approx \frac{1}{4}(C_m/C_L + L_m/L_L)$ | Near-end cross talk coupling | 近端串扰耦合系数 |
| $\text{FEXT} \approx \frac{1}{2}(\text{TD}/\text{RT})(C_m/C_L - L_m/L_L)$ | Far-end cross talk | 远端串扰耦合系数 |
| $\text{Len}_{\text{sat}} = RT \cdot v / 2$ | Saturation length | 饱和长度 |
| $V_{\text{noise}} = M \cdot dI/dt$ | Switching noise (SSN) | 开关噪声 |
