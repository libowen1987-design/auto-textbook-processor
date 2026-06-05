---
chapter: 9
title: Crosstalk
source: Paul, Clayton R. *Introduction to Electromagnetic Compatibility*, 2nd Ed., Wiley, 2006
pages: 583-736
---

# Chapter 9: Crosstalk

## 9.1 Three-Conductor Transmission Line Model

Crosstalk is parasitic coupling between two transmission lines (aggressor/victim) in proximity. The three-conductor model adds the third conductor (return/ground).

### Per-Unit-Length Parameters (3-Conductor)

For two signal conductors + ground return:

$$\mathbf{L} = \begin{bmatrix} l_{11} & l_{12} \\ l_{21} & l_{22} \end{bmatrix} \quad \mathbf{C} = \begin{bmatrix} c_{11} + c_{12} & -c_{12} \\ -c_{12} & c_{22} + c_{12} \end{bmatrix}$$

where:
- $l_{11}, l_{22}$ = self inductances
- $l_{12} = l_{21}$ = mutual inductance
- $c_{12}$ = mutual capacitance between lines 1 and 2
- $c_{11}, c_{22}$ = capacitance to ground

### TL Equations (PHTN Form)

For the two signal lines:

$$\frac{\partial \mathbf{V}}{\partial z} = -\mathbf{L} \frac{\partial \mathbf{I}}{\partial t}$$

$$\frac{\partial \mathbf{I}}{\partial z} = -\mathbf{C} \frac{\partial \mathbf{V}}{\partial t}$$

where $\mathbf{V} = [V_1, V_2]^T$ and $\mathbf{I} = [I_1, I_2]^T$.

## 9.2 Weak Coupling Approximation

When $l_{12} \ll l_{11}, l_{22}$ and $c_{12} \ll c_{11}, c_{22}$, the total crosstalk is the sum of inductive and capacitive components.

### Inductive Coupling

Mutual inductance couples current changes:

$$V_{\text{ind}}(z, t) = -l_{12} \Delta z \frac{\partial I_1}{\partial t}$$

For a matched line with source voltage $V_S$ and $R_S = Z_C$:

$$V_{\text{NEXT, ind}} = \frac{1}{4} \left( \frac{l_{12}}{l_{11}} \right) V_S$$

$$V_{\text{FEXT, ind}} = -\frac{1}{2} \left( \frac{l_{12}}{l_{11}} \right) \frac{T_D}{\tau} V_S$$

### Capacitive Coupling

Mutual capacitance couples voltage changes:

$$I_{\text{cap}}(z, t) = -c_{12} \Delta z \frac{\partial V_1}{\partial t}$$

For matched lines:

$$V_{\text{NEXT, cap}} = \frac{1}{4} \left( \frac{c_{12}}{c_{11} + c_{12}} \right) V_S$$

$$V_{\text{FEXT, cap}} = \frac{1}{2} \left( \frac{c_{12}}{c_{11} + c_{12}} \right) \frac{T_D}{\tau} V_S$$

## 9.3 Near-End vs. Far-End Crosstalk

### Near-End Crosstalk (NEXT) — Backward

$$K_{\text{NE}} = \frac{1}{4} \left( \frac{l_{12}}{l_{11}} + \frac{c_{12}}{c_{11}} \right)$$

$$V_{\text{NEXT}} = K_{\text{NE}} V_S \quad \text{(for matched lines)}$$

### Far-End Crosstalk (FEXT) — Forward

$$K_{\text{FE}} = -\frac{1}{2} \left( \frac{l_{12}}{l_{11}} - \frac{c_{12}}{c_{11}} \right) \frac{T_D}{\tau}$$

$$V_{\text{FEXT}} = \frac{1}{2} K_{\text{FE}} V_S \quad \text{(for matched lines)}$$

### Characteristics

| Parameter | NEXT | FEXT |
|---|---|---|
| Direction | Backward (toward source) | Forward (away from source) |
| Duration | 2× rise time | Pulse width |
| Level vs. length | Saturates after $L > v \cdot \tau$ | Increases with length |
| Homogeneous medium | $K_{\text{NE}} \approx \frac{1}{2}K_{\text{inductive}}$ | $K_{\text{FE}} \approx 0$ |
| Inhomogeneous medium | Always present | Always present |

### Homogeneous vs. Inhomogeneous Media

For homogeneous medium (stripline):

$$\frac{l_{12}}{l_{11}} = \frac{c_{12}}{c_{11}}$$

Result: $K_{\text{FE}} = 0$ — no FEXT in homogeneous media. All crosstalk is NEXT.

For inhomogeneous medium (microstrip):

$$\frac{l_{12}}{l_{11}} < \frac{c_{12}}{c_{11}}$$

Result: $K_{\text{FE}} \neq 0$ — FEXT appears due to unequal inductive/capacitive coupling.

## 9.4 Guard Traces and Separation

### Guard Trace Effectiveness

A grounded guard trace between aggressor and victim:
- Provides additional isolation via Faraday cage effect
- **Must be stitched** with vias at both ends (every $\lambda/20$ or better)
- Ungrounded guard traces **increase** coupling

### Reduction from Guard Trace

Typical crosstalk reduction with grounded guard trace:
- Without guard: baseline
- With guard + vias at ends: 10–15 dB
- With guard + vias every $\lambda/20$: 20–30 dB

### Coupling vs. Separation

$$K_{\text{NE}} \propto \frac{1}{s^{1.5}} \quad \text{(approximately)}$$

where $s$ = center-to-center spacing.

## 9.5 Crosstalk in Ribbon Cables

For a ribbon cable, crosstalk depends on:
- Wire gauge and separation
- Cable length relative to rise time
- Termination impedance

**Measured crosstalk (typical):**
- Adjacent wires in ribbon cable @ 10 ns rise time: 5–15%
- Every other wire: 1–5%
- Shielded pair in ribbon: 0.5–2%

## 9.6 Modal Analysis of Coupled Lines

### Even/Odd Mode Decomposition

$$\mathbf{V}_m = \begin{bmatrix} V_e \\ V_o \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} \mathbf{V}$$

### Mode Impedances

$$Z_{Ce} = \sqrt{\frac{l_{11} + l_{12}}{c_{11}}} \quad Z_{Co} = \sqrt{\frac{l_{11} - l_{12}}{c_{11} + 2c_{12}}}$$

### Mode Velocities

In inhomogeneous media: $v_e \neq v_o$ → modal dispersion → FEXT.

## 9.7 SPICE Model for Crosstalk

```
* Coupled microstrip lines
* Line 1: aggressor, Line 2: victim

; Per-unit-length parameters
L11  = 0.33 uH/m
L22  = 0.33 uH/m
L12  = 0.06 uH/m
C11  = 120 pF/m
C22  = 120 pF/m
C12  = 20 pF/m

; Use coupled TL model or lumped Pi segments
; For L_total < tr/(6*tpd), use 3-5 Pi sections
```

### Equivalent PSPICE Coupled Line Model

PSPICE supports coupled lines directly:

```
K1 L1 L2 0.6       ; Coupling coefficient
.models ...
```

## 9.8 Engineering Intuition

1. **NEXT saturates, FEXT grows with length.** For long buses (> 12 inch), FEXT is the dominant problem.

2. **In stripline, only NEXT matters.** Since $L_m/L_{11} = C_m/C_{11}$, FEXT cancels in homogeneous media.

3. **Guard traces that are not grounded are worse than no guard.** They capacitively couple more than they shield.

4. **The 3W rule** (3× trace width spacing) reduces coupling by ~90% compared to minimum spacing.

5. **Crosstalk in cables gets worse with faster edges.** Halving rise time doubles both NEXT and FEXT.
