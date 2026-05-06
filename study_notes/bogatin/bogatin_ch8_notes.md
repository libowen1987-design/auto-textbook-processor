---
title: "Chapter 8 — Transmission Lines and Reflections"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 8
pages: "310–363"
---

# Ch8: Transmission Lines and Reflections

## 8.1 Reflection Coefficient

When a signal traveling in impedance $Z_1$ encounters impedance $Z_2$:

**Reflection coefficient:**
$$
\rho = \frac{V_{\text{refl}}}{V_{\text{inc}}} = \frac{Z_2 - Z_1}{Z_2 + Z_1}
$$

**Transmission coefficient:**
$$
\tau = \frac{V_{\text{trans}}}{V_{\text{inc}}} = \frac{2 Z_2}{Z_2 + Z_1}
$$

**Special cases** (for $Z_1 = 50\ \Omega$):
| $Z_2$ | $\rho$ | $V_{\text{end}}$ (for $V_{\text{inc}}=1$V) |
|:--:|:--:|:--:|
| Open ($\infty$) | +1 | 2V |
| Short (0) | -1 | 0V |
| 50 $\Omega$ | 0 | 1V |
| 25 $\Omega$ | -1/3 | 0.67V |
| 75 $\Omega$ | +0.2 | 1.2V |

> **Engineering Intuition:** Reflections exist to maintain voltage continuity and current continuity at an impedance interface. Without reflections, Maxwell's equations would be violated.

## 8.2 Bounce Diagrams

Tracking multiple reflections: source impedance $R_s$, line $Z_0$, far-end impedance $Z_L$.

Initial launched voltage: $V_{\text{launched}} = V_s \cdot Z_0 / (R_s + Z_0)$

**Example:** $V_s=1$V, $R_s=10\Omega$, $Z_0=50\Omega$, open far end, TD=1 nsec:
- $V_{\text{launch}} = 0.84$ V
- After TD=1 ns: end voltage = $0.84 + 0.84 = 1.68$ V
- After 2TD: source refl = $-0.67 \times 0.84 = -0.56$ V
- After 3TD: end voltage = $1.68 - 0.56 - 0.56 = 0.56$ V
- Eventually converges to 1V

## 8.3 When to Terminate

**Critical rule of thumb:** Termination needed when the **time delay of the line > 20% of the rise time**.

$$
\text{Len}_{\text{max}} \approx RT \quad \text{(inches when RT in nsec)}
$$

| RT (nsec) | Max unterminated length |
|:--:|:--:|
| 10 | 10 inches |
| 1 | 1 inch |
| 0.5 | 0.5 inch |
| 0.1 | 0.1 inch |

> **Engineering Intuition:** With 0.1 nsec rise times common today, virtually EVERY trace needs termination. This is why SI matters now.

## 8.4 Source-Series Termination

The most common termination for point-to-point topology. Add resistor $R_T$ such that:

$$
R_T + R_{\text{source}} = Z_0
$$

**Example:** $R_{\text{source}} = 10\ \Omega$, $Z_0 = 50\ \Omega$ → $R_T = 40\ \Omega$.

- Half voltage launched (0.5V for 1V source)
- At far-end open: voltage doubles to full 1V
- Reflected wave sees matched impedance at source → absorbed, no further reflections
- **Result:** Clean 1V signal at receiver, no ringing

## 8.5 Discontinuity Rules

| Feature | Key Rule | Len$_{\text{max}}$ |
|:--|:--|:--:|
| Series TL (neck-down) | TD < 20% RT | $\approx RT$ inches |
| Stub | Length < 20% of $RT \cdot v$ | $\approx RT$ inches |
| Capacitive load | $C_{\text{load}}$ small enough | Simulate |

## 8.6 TDR (Time Domain Reflectometer)

A TDR = fast step generator + sampling scope. It measures reflected voltage vs. time, which maps to impedance vs. position.

**Key relationships:**
- Open → +reflection (voltage goes up)
- Short → -reflection (voltage goes down)
- Matched → no reflection
- Time axis = round-trip delay to discontinuities

## 8.7 Key Formulas

| Formula | Description |
|:--|:--|
| $\rho = (Z_2 - Z_1)/(Z_2 + Z_1)$ | Reflection coefficient |
| $\tau = 2Z_2/(Z_2 + Z_1)$ | Transmission coefficient |
| $V_{\text{launch}} = V_s \cdot Z_0/(R_s + Z_0)$ | Initial launched voltage |
| $R_T + R_s = Z_0$ | Source-series termination |
| $\text{Len}_{\text{max}} \approx RT$ (in) | Max unterminated/discontinuity length |
| $\text{Len}_{\text{stub,max}} \approx RT$ (in) | Max stub length |
