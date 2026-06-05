---
title: "Chapter 13 — Power Distribution Network (PDN)"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 13
pages: "644–746"
---

# Ch13: PDN — Power Distribution Network

## 13.1 PDN Goal

Deliver **constant voltage** ($V_{\text{dd}}$ to $V_{\text{ss}}$) at each chip's pads with ripple < 5%.

**Target impedance:**
$$
Z_{\text{target}} = \frac{V_{\text{dd}} \times \text{Ripple\%}}{\Delta I}
$$

## 13.2 PDN Impedance Components

The PDN impedance across frequency comes from:
1. **VRM (voltage regulator module):** good at DC to ~1 kHz
2. **Bulk capacitors:** good ~1 kHz to ~1 MHz
3. **MLCC decoupling capacitors:** good ~1 MHz to ~100 MHz
4. **On-chip / on-package capacitance:** good >100 MHz
5. **Power/ground planes:** provide low inductance at all frequencies

## 13.3 Decoupling Capacitor Model

Real capacitor = $R_{\text{ESR}} + L_{\text{ESL}} + C$ in series.

**Self-resonant frequency:** $f_{\text{SR}} = 1/(2\pi\sqrt{L_{\text{ESL}} \cdot C})$

**Above SRF:** $|Z| \approx \omega \cdot L_{\text{ESL}}$ (inductive, independent of $C$)

> **Engineering Intuition:** At high frequency (>100 MHz), ALL capacitors of the same package size have the SAME impedance. The ONLY knob is ESL, not capacitance value.

## 13.4 MLCC Capacitor ESL

| Package | Typical ESL (nH) |
|:--|:--:|
| 1206 | ~1.5 |
| 0805 | ~1.0 |
| 0603 | ~0.7 |
| 0402 | ~0.4 |
| 0201 | ~0.2 |

**Total ESL in parallel:** $L_{\text{eq}} \approx (\text{ESL} + L_{\text{mounting}})/N$

## 13.5 PDN Design Strategies

1. **Close power/ground planes:** thin dielectric → low loop inductance per square ($L_{\text{sq}} = \mu_0 h$)
2. **Multiple decaps in parallel:** reduce effective ESL
3. **Short vias:** keep planes near surface
4. **On-package decoupling:** best for >100 MHz
5. **On-chip decoupling:** best for >1 GHz

## 13.6 Decoupling Time Equation

$$
\Delta t \approx \frac{C \cdot 0.05 \cdot V^2}{P}
$$

**Required capacitance for given decoupling time:**
$$
C = \frac{1}{0.05} \cdot \frac{P}{V^2} \cdot \Delta t
$$

## 13.7 FDTI Method (Fast Decoupling Threshold Identification)

Practical method: determine how many decoupling capacitors are actually needed by computing the impedance profile of the PDN and checking against $Z_{\text{target}}$.

## 13.8 Key Rules of Thumb

| Rule | Value |
|:--|:--|
| Target impedance trend | Decreases ~10× every 6 years |
| MLCC ESL (0402) | ~0.4 nH |
| Plane inductance per square (2 mil) | ~64 pH |
| Decoupling capacitor spacing | Closer to chip = better |
| Number of caps needed | Determined by ESL, not capacitance |

> **Engineering Intuition:** PDN design is about INDUCTANCE, not capacitance. The capacitance value determines the low-frequency impedance; the ESL determines the high-frequency impedance. At high frequency, a 1 nF cap with 0.4 nH ESL and a 100 nF cap with 0.4 nH ESL look IDENTICAL.

## 13.9 Key Formulas

| Formula | Description |
|:--|:--|
| $Z_{\text{target}} = V_{\text{dd}} \cdot \text{Ripple} / \Delta I$ | PDN target impedance |
| $f_{\text{SR}} = 1/(2\pi\sqrt{L_{\text{ESL}} C})$ | Self-resonant frequency |
| $|Z|_{\text{above SRF}} \approx \omega L_{\text{ESL}}$ | High-frequency impedance |
| $L_{\text{eq}} = (\text{ESL} + L_{\text{via}})/N$ | Parallel decaps |
| $\Delta t = 0.05 \cdot C \cdot V^2 / P$ | Decoupling time |
| $L_{\text{sq}} = \mu_0 h$ | Plane inductance per square |
