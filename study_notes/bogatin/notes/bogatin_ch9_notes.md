---
title: "Chapter 9 — Lossy Lines"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 9
pages: "366–432"
---

# Ch9: Lossy Lines

## 9.1 Two Loss Mechanisms

1. **Conductor loss (skin effect):** $R(f) \propto \sqrt{f}$
2. **Dielectric loss:** $G(f) \propto f$ (dissipation factor $\tan \delta$)

**Total attenuation constant:**
$$
\alpha(f) = \alpha_{\text{cond}} + \alpha_{\text{diel}} = k_1 \sqrt{f} + k_2 f
$$

## 9.2 Skin Effect Resistance

$$
R_{\text{HF}}(f) = \frac{\rho}{w \cdot \delta(f)}, \quad \delta(f) = \sqrt{\frac{1}{\pi f \mu \sigma}}
$$

For copper: $\delta(\mu\text{m}) = 66 / \sqrt{f(\text{MHz})}$

## 9.3 Dielectric Loss

**Dissipation factor** $\tan \delta$: measure of how "lossy" a dielectric is.

| Material | $\tan \delta$ (at 1 GHz) |
|:--|:--|
| FR4 | 0.02 |
| Rogers 4350B | 0.0037 |
| Megtron 6 | 0.002 |
| PTFE | 0.0002 |

**Dielectric attenuation:** $\alpha_{\text{diel}} \approx 2.3 \cdot f \cdot \tan \delta \cdot \sqrt{\epsilon_r}$ (dB/inch)

## 9.4 Intersymbol Interference (ISI)

Loss attenuates high frequencies more than low → rise time degradation → bits "smear" into adjacent bit periods → ISI.

**ISI threshold:** When $RT_{\text{degraded}} \approx$ bit period / 2, the eye closes.

## 9.5 Eye Diagram

- **Vertical eye opening:** decreases with loss
- **Horizontal eye opening (jitter):** increases with loss
- Deterministic jitter from loss + impedance discontinuities

## 9.6 Equalization and Pre-Emphasis

**Equalization:** Filter that attenuates low frequencies to match high-frequency loss (passive or active).

**Pre-emphasis (de-emphasis):** Boost high-frequency components at the transmitter to compensate for channel loss.

> **Engineering Intuition:** Lossy lines are THE dominant SI problem for >1 Gbps serial links over >10 inches. The solution is either better materials (low-loss laminate) or signal processing (equalization).

## 9.7 Key Formulas

| Formula | Description |
|:--|:--|
| $\delta = \sqrt{1/(\pi f \mu \sigma)}$ | Skin depth |
| $R_{\text{AC}} \propto \sqrt{f}$ | Skin effect resistance |
| $\alpha_{\text{total}} = \alpha_{\text{cond}} + \alpha_{\text{diel}}$ | Total attenuation |
| $\alpha_{\text{diel}} \propto f \cdot \tan \delta$ | Dielectric loss |
| $RT_{\text{out}} = \sqrt{RT_{\text{in}}^2 + RT_{\text{line}}^2}$ | Rise time degradation |
