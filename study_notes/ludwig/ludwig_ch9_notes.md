---
title: "Chapter 9 — RF Transistor Amplifier Design"
book: "RF Circuit Design — 2nd Ed."
author: "Reinhold Ludwig, Gene Bogdanov"
pages: "477–543"
processed: "2026-05-03"
tags: [amplifier, gain, stability-circle, noise-figure, unilateral, bilateral, broadband, multistage]
---

# Chapter 9: RF Transistor Amplifier Design

> **Overview:** This chapter covers RF amplifier design: power gain definitions, stability analysis, constant gain and noise circles, unilateral/bilateral design, broadband techniques, and multistage amplifiers.

## 9.1 Characteristics of Amplifiers

Key specifications: gain, bandwidth, noise figure (NF), output power, linearity (IP3), stability.

## 9.2 Amplifier Power Relations

### Power Gain Definitions
- **Transducer gain:** $G_T = \frac{P_L}{P_{\text{avs}}} = |S_{21}|^2 \frac{(1-|\Gamma_S|^2)(1-|\Gamma_L|^2)}{|1-\Gamma_{\text{in}}\Gamma_S|^2|1-S_{22}\Gamma_L|^2}$
- **Operating gain:** $G_P = \frac{P_L}{P_{\text{in}}} = |S_{21}|^2 \frac{1-|\Gamma_L|^2}{|1-S_{22}\Gamma_L|^2(1-|\Gamma_{\text{in}}|^2)}$
- **Available gain:** $G_A = |S_{21}|^2 \frac{1-|\Gamma_S|^2}{|1-S_{11}\Gamma_S|^2(1-|\Gamma_{\text{out}}|^2)}$

### Maximum Available Gain
For **unilateral** case ($S_{12}=0$): $G_{\text{TU}} = G_S \cdot G_0 \cdot G_L$ where:
- $G_S = 1/(1-|\Gamma_S|^2)$, $G_0 = |S_{21}|^2$, $G_L = (1-|\Gamma_L|^2)/|1-S_{22}\Gamma_L|^2$

## 9.3 Stability Considerations

### Rollett's Stability Factor $K$

$$
K = \frac{1 - |S_{11}|^2 - |S_{22}|^2 + |\Delta|^2}{2|S_{12}S_{21}|} > 1
$$

where $\Delta = S_{11}S_{22} - S_{12}S_{21}$.

**Unconditionally stable** if $K > 1$ and $|\Delta| < 1$.

### Stability Circles (Smith Chart)
- Input stability circle: $C_S = \frac{(S_{11} - \Delta S_{22}^*)^*}{|S_{11}|^2 - |\Delta|^2}$, radius $R_S = \left|\frac{S_{12}S_{21}}{|S_{11}|^2 - |\Delta|^2}\right|$
- Output stability circle: similar with indices swapped

### Stabilization (Example 9-5)
Add resistive loading at input/output to push $K > 1$ (at the cost of reduced gain and increased NF).

## 9.4 Constant Gain Circles

For unilateral design:
$$
G_S(dB) = 10\log\left(\frac{1-|\Gamma_S|^2}{|1-S_{11}\Gamma_S|^2}\right)
$$
Circles centered at $S_{11}^*/(1+|S_{11}|^2 - g_S)$.

## 9.5 Noise Figure Circles

$$
\text{NF} = \text{NF}_{\min} + \frac{r_n}{G_S}|\Gamma_S - \Gamma_{\text{opt}}|^2
$$

where $r_n = R_n/Z_0$, $\Gamma_{\text{opt}}$ is optimum source reflection coefficient.

## 9.6 Broadband and Multistage Amplifiers

- **Broadband:** Negative feedback, distributed amplifiers, balanced (90° hybrids)
- **Multistage:** Cascaded NF (Friis): $\text{NF}_{\text{total}} = \text{NF}_1 + \frac{\text{NF}_2-1}{G_1} + \ldots$

> **工程直觉:** 放大器设计典型流程: (1) 稳定性分析 → (2) 选择 $\Gamma_S$ 和 $\Gamma_L$ (增益/噪声/Nash) → (3) 设计输入/输出匹配网络 → (4) 全波EM验证.
