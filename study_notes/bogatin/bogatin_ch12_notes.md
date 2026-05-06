---
title: "Chapter 12 — S-Parameters"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 12
pages: "584–642"
---

# Ch12: S-Parameters

## 12.1 What Are S-Parameters?

**Scattering parameters (S-parameters):** Ratio of output sine wave to input sine wave at each frequency.

- $S_{11}$: reflection from port 1 (input match)
- $S_{21}$: transmission from port 1 to port 2 (insertion loss)
- $S_{22}$: reflection from port 2 (output match)
- $S_{12}$: reverse transmission (isolation)

## 12.2 Key Relationships

**Reflection coefficient from $S_{11}$:**
$$
S_{11} = \frac{Z_{\text{DUT}} - Z_0}{Z_{\text{DUT}} + Z_0}
$$

**Insertion loss (dB):** $\text{IL} = 20 \log_{10} |S_{21}|$

**Return loss (dB):** $\text{RL} = 20 \log_{10} |S_{11}|$

## 12.3 Mixed-Mode S-Parameters (Differential)

For differential pairs:

| Parameter | Meaning |
|:--|:--|
| $S_{\text{dd11}}$ | Differential reflection |
| $S_{\text{dd21}}$ | Differential transmission |
| $S_{\text{cc21}}$ | Common-mode transmission |
| $S_{\text{cd21}}$ | Mode conversion (diff → common) |

## 12.4 Eye Diagram from S-Parameters

S-parameters + PRBS (pseudo-random bit stream) → IFFT → time-domain eye diagram.

**Eye diagram metrics:**
- **Vertical eye opening:** noise margin
- **Horizontal eye opening:** jitter margin (unit interval — jitter)
- **Bathtub curve:** BER vs. sampling phase

## 12.5 Key Design Guidelines

- $|S_{11}| < -15$ dB (return loss, good match)
- $|S_{21}|$: smooth roll-off, no resonances
- $S_{\text{cd21}}$ (mode conversion): keep as low as possible (bad → EMI)
- VNA is the instrument for S-parameter measurement (kHz to 50+ GHz)

> **Engineering Intuition:** S-parameters are the "universal language" of interconnects. Any interconnect's performance can be completely described by its S-parameters. They're becoming the industry standard for SI analysis.

## 12.6 Key Formulas

| Formula | Description |
|:--|:--|
| $S_{11} = (Z_{\text{DUT}} - Z_0)/(Z_{\text{DUT}} + Z_0)$ | Reflection S-parameter |
| $\text{IL(dB)} = 20\log|S_{21}|$ | Insertion loss |
| $\text{RL(dB)} = 20\log|S_{11}|$ | Return loss |
| $V_{\text{refl}}/V_{\text{inc}} = S_{11}$ | Reflection coefficient |
| $V_{\text{trans}}/V_{\text{inc}} = S_{21}$ | Transmission coefficient |
