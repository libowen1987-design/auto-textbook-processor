---
title: "Chapter 10 — Cross Talk"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 10
pages: "434–503"
---

# Ch10: Cross Talk

## 10.1 Capacitive and Inductive Coupling

Cross talk arises from:
- **Mutual capacitance** $C_m$: couples voltage noise through displacement current
- **Mutual inductance** $L_m$: couples current noise through induced voltage

## 10.2 NEXT and FEXT

**Near-end cross talk (NEXT):** Noise at the same end as the driver (backward).

**Far-end cross talk (FEXT):** Noise at the opposite end from the driver (forward).

**For uniform transmission lines with ideal return plane:**

$$
\text{NEXT} \propto \frac{1}{4} \left(\frac{C_m}{C_L} + \frac{L_m}{L_L}\right)
$$

$$
\text{FEXT} \propto \frac{1}{2} \cdot \frac{\text{TD}_{\text{coupled}}}{\text{RT}} \cdot \left(\frac{C_m}{C_L} - \frac{L_m}{L_L}\right)
$$

For microstrip: $C_m/C_L \neq L_m/L_L$ → both NEXT and FEXT exist.
For stripline: $C_m/C_L = L_m/L_L$ → FEXT cancels (no FEXT in homogeneous medium).

## 10.3 Saturation Length

NEXT grows linearly with coupled length until **saturation length** = half the spatial extent of the rising edge:

$$
\text{Len}_{\text{sat}} = \frac{RT \cdot v}{2}
$$

Beyond this, NEXT is constant (saturated).

## 10.4 Key Design Rules

| Goal | Action |
|:--|:--|
| Reduce NEXT by 50% | Double the trace spacing |
| Keep NEXT < 5% (50-Ohm bus) | Spacing $\ge 2 \times$ line width |
| Keep FEXT < 5% | Keep coupled TD < RT |
| Reduce cross talk | Use stripline (homogeneous) |
| Tightly coupled bus | 95% of noise from nearest neighbors only |

## 10.5 Switching Noise (SSN/SSO)

When return paths are not ideal planes (connectors, packages):

- Inductive coupling dominates over capacitive coupling
- Ground bounce / SSN / SSO noise
- $V_{\text{noise}} = M_{ab} \cdot dI/dt$

> **Engineering Intuition:** The best cross talk reduction is spacing. In connectors/packages where spacing can't increase, SSN becomes the dominant problem. Differential signaling helps.

## 10.6 Key Formulas

| Formula | Description |
|:--|:--|
| $\text{NEXT} \approx \frac{1}{4}(C_m/C_L + L_m/L_L)$ | Near-end cross talk coupling |
| $\text{FEXT} \approx \frac{1}{2}(\text{TD}/\text{RT})(C_m/C_L - L_m/L_L)$ | Far-end cross talk |
| $\text{Len}_{\text{sat}} = RT \cdot v / 2$ | Saturation length |
| $V_{\text{noise}} = M \cdot dI/dt$ | Switching noise (SSN) |
