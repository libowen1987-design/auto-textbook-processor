---
title: "Chapter 11 — Differential Pairs"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 11
pages: "504–582"
---

# Ch11: Differential Pairs

## 11.1 Differential vs. Common Signals

**Differential signal:** $V_{\text{diff}} = V_1 - V_2$ (signal swings opposite on each line)
**Common signal:** $V_{\text{comm}} = (V_1 + V_2)/2$ (both lines swing together)

## 11.2 Odd Mode and Even Mode

**Odd mode:** Lines driven with opposite polarity ($+V, -V$)
**Even mode:** Lines driven with same polarity ($+V, +V$)

**Impedances:**
- $Z_{\text{odd}}$: impedance of one line in odd mode
- $Z_{\text{even}}$: impedance of one line in even mode
- $Z_{\text{diff}} = 2 \times Z_{\text{odd}}$: impedance seen by differential signal
- $Z_{\text{comm}} = Z_{\text{even}} / 2$: impedance seen by common signal

## 11.3 Effect of Coupling

For coupled lines with mutual inductance $L_m$ and mutual capacitance $C_m$:

$$
Z_{\text{odd}} = \sqrt{\frac{L_L - L_m}{C_L + C_m}} = Z_0 \sqrt{\frac{1 - k_L}{1 + k_C}}
$$

$$
Z_{\text{even}} = \sqrt{\frac{L_L + L_m}{C_L - C_m}} = Z_0 \sqrt{\frac{1 + k_L}{1 - k_C}}
$$

where $k_L = L_m/L_L$, $k_C = C_m/C_L$.

**Key results:**
- **Tighter coupling** → lower $Z_{\text{diff}}$
- **Tighter coupling** → higher $Z_{\text{common}}$
- **Tighter coupling** → lower differential-to-common conversion

## 11.4 Advantages of Differential Signaling

1. **Less EMI:** fields cancel for differential signals
2. **Better noise immunity:** external noise couples as common mode, rejected by receiver
3. **Less rail collapse:** current is constant (one line goes up, other goes down)
4. **Higher signal swing** for same supply voltage
5. **Less sensitivity to ground bounce**

## 11.5 Common Terms

| Term | Meaning |
|:--|:--|
| $Z_{\text{diff}}$ | Impedance between the two lines (differential) |
| $Z_{\text{odd}}$ | Impedance of one line, odd-mode drive |
| $Z_{\text{even}}$ | Impedance of one line, even-mode drive |
| $S_{\text{dd21}}$ | Differential transmission S-parameter |
| $S_{\text{cc21}}$ | Common-mode transmission S-parameter |
| $S_{\text{cd21}}$ | Mode conversion (diff→common) |

> **Engineering Intuition:** In a differential pair, "coupling" between lines REDUCES differential impedance. Tight coupling means the two lines are close together, so each line "sees" the other as part of its return path.

## 11.6 Key Formulas

| Formula | Description |
|:--|:--|
| $V_{\text{diff}} = V_1 - V_2$ | Differential signal |
| $V_{\text{comm}} = (V_1 + V_2)/2$ | Common signal |
| $Z_{\text{diff}} = 2 \cdot Z_{\text{odd}}$ | Differential impedance |
| $Z_{\text{comm}} = Z_{\text{even}}/2$ | Common impedance |
| $Z_{\text{odd}} = \sqrt{(L_L - L_m)/(C_L + C_m)}$ | Odd-mode impedance |
| $Z_{\text{even}} = \sqrt{(L_L + L_m)/(C_L - C_m)}$ | Even-mode impedance |
