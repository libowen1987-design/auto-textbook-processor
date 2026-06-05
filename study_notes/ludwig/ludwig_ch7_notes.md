---
title: "Chapter 7 — Active RF Component Modeling"
book: "RF Circuit Design — 2nd Ed."
author: "Reinhold Ludwig, Gene Bogdanov"
pages: "365–411"
processed: "2026-05-03"
tags: [modeling, SPICE, ebers-moll, gummel-poon, hybrid-pi, miller-effect, s-parameters]
---

# Chapter 7: Active RF Component Modeling

> **Overview:** Large- and small-signal models for RF diodes and transistors. Ebers-Moll, Gummel-Poon BJT models, hybrid-π parameters, and S-parameter-based modeling.

## 7.1 Diode Models

### Nonlinear Model
- $I_D = I_S(e^{V_D/(\eta V_T)} - 1)$, $V_T = kT/q$
- Junction capacitance: $C_j(V) = C_{j0}/(1 - V/V_0)^m$
- Diffusion capacitance: $C_d = \tau_F I_D / (\eta V_T)$
- Series resistance $R_S$, package parasitics $L_p$, $C_p$

### Small-Signal Model (Example 7-1)
- $r_d = \eta V_T / I_D$ (dynamic resistance)
- $C_d = \tau_F / r_d$ (diffusion capacitance)

## 7.2 Transistor Models

### Ebers-Moll (BJT)
Transport and injection formulations. Large-signal model with current sources and diodes representing $I_{BE}$ and $I_{BC}$.

### Gummel-Poon (BJT)
More accurate: includes base-width modulation (Early effect), high-level injection, temperature effects. Used by SPICE (40+ parameters).

### Miller Effect (Example 7-3)
$$
C_{\text{Miller}} = C_\mu(1 + |A_V|)
$$
Doubles input capacitance due to collector-base feedback. Critical at RF.

### Hybrid-π Small-Signal Model (Example 7-6, 7-7)
- **Low-freq parameters:** $g_m$, $r_\pi$, $r_o$
- **High-freq:** $C_\pi$, $C_\mu$, $r_b$, $L_e$
- $f_T = g_m / (2\pi(C_\pi + C_\mu))$

### S-Parameter Modeling
- Manufacturer supplies $S_{11}$, $S_{12}$, $S_{21}$, $S_{22}$ vs $f$
- Convert to equivalent circuit if needed
- CAD tools (SPICE, ADS) directly use S-parameter files

> **工程直觉:** 小信号模型的有效性取决于偏置点和信号幅度。大信号(谐波)行为需要非线性模型或谐波平衡仿真.
