---
title: "Chapter 10 — Oscillators and Mixers"
book: "RF Circuit Design — 2nd Ed."
author: "Reinhold Ludwig, Gene Bogdanov"
pages: "553–604"
processed: "2026-05-03"
tags: [oscillator, negative-resistance, colpitts, hartley, VCO, DRO, mixer, schottky]
---

# Chapter 10: Oscillators and Mixers

> **Overview:** Negative-resistance and feedback oscillators (Colpitts, Hartley, VCO), dielectric resonator oscillator (DRO), quartz crystal oscillators, and Schottky diode mixers.

## 10.1 Oscillator Concepts

### Negative Resistance Oscillator
- Active device presents $Z_{\text{in}} = R_{\text{in}} + jX_{\text{in}}$ where $R_{\text{in}} < 0$
- Condition for oscillation: $R_{\text{in}} + R_L < 0$ and $X_{\text{in}} + X_L = 0$
- S-parameter condition: $|\Gamma_{\text{in}}\Gamma_L| > 1$, $\angle(\Gamma_{\text{in}}\Gamma_L) = 0$

### Feedback (Two-Port) Oscillator
- Loop gain $|A\beta| > 1$ and phase shift $360^\circ$ (Barkhausen criterion)
- Frequency determined by resonant tank

## 10.2 Types of Oscillators

### Colpitts Oscillator (Example 10-1)
- Capacitive divider feedback ($C_1$, $C_2$)
- Resonant frequency: $f_0 = 1/(2\pi\sqrt{L C_{\text{eq}}})$, $C_{\text{eq}} = C_1C_2/(C_1 + C_2)$

### Hartley Oscillator
- Inductive divider feedback ($L_1$, $L_2$ in series with $C$)
- $f_0 = 1/(2\pi\sqrt{(L_1+L_2)C})$

### Crystal Oscillator
- Quartz: high $Q$ ($10^4$–$10^6$), stable $f_0$
- Equivalent circuit: $RLC$ series + parallel $C_0$
- Series and parallel resonance very close (Δ$f$ ~ 0.1%)

### VCO (Voltage-Controlled Oscillator)
- Varactor diode provides voltage-variable capacitance
- $f_0(V) = 1/(2\pi\sqrt{LC(V)})$

### DRO (Dielectric Resonator Oscillator)
- High-$\varepsilon_r$ ceramic puck resonator (typically $\varepsilon_r = 30$–$80$)
- Stable, low-phase-noise, used at microwave frequencies

## 10.3 Mixers

### Schottky Diode Mixer
- Nonlinear $I$-$V$ characteristic generates $f_{\text{RF}} \pm f_{\text{LO}}$
- **Conversion loss:** $L_c = 10\log(P_{\text{RF}}/P_{\text{IF}})$
- **Single-ended:** one diode, simple but poor port isolation
- **Balanced:** two diodes (90° or 180° hybrid), better isolation
- **Double-balanced:** four diodes (ring), best isolation and spurious rejection

### Key Mixer Parameters
- Conversion loss $L_c$
- Noise figure (NF ≈ $L_c$ for passive diode mixers)
- Isolation (LO→RF, LO→IF, RF→IF)
- IP3 (third-order intercept point)

> **工程直觉:** 振荡器设计核心: 确保起振条件(小信号$|\Gamma_{\text{in}}\Gamma_L|>1$)且稳态限幅(大信号)。混频器选型: 单端→简单但隔离差; 双平衡→最佳性能但需要更高的本振功率.
