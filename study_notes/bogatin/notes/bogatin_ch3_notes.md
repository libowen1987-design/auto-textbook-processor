---
title: "Chapter 3 — Impedance and Electrical Models"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 3
pages: "110–139"
---

# Ch3: Impedance and Electrical Models

## 3.1 What Is Impedance?

**Impedance** $Z$ is the fundamental electrical property linking physical design to electrical performance. The definition (always true, in any domain):

$$
Z = \frac{V}{I}
$$

Units: Ohms ($\Omega$).

The four SI problem families described through impedance:
1. **Signal quality:** Reflections when the impedance changes
2. **Cross talk:** Mutual impedance ($C_m$, $L_m$) between traces
3. **Rail collapse:** PDN impedance × switching current = voltage drop
4. **EMI:** Ground-plane impedance driving common currents on cables

> **Engineering Intuition:** Impedance is the Rosetta stone that links physical design and electrical performance. Strategy: translate system-performance needs into an impedance requirement, and physical design into an impedance property.

## 3.2 Real vs. Ideal Circuit Elements

- **Real devices:** can be measured. They are the actual hardware.
- **Ideal elements:** mathematical descriptions used in simulators (SPICE). Can only be calculated.

| Ideal Element | Symbol | Unit | Definition |
|:--|:--:|:--:|:--|
| Resistor | R | Ohm ($\Omega$) | $V = I \cdot R$ |
| Capacitor | C | Farad (F) | $Q = C \cdot V$, $I = C \cdot dV/dt$ |
| Inductor | L | Henry (H) | $V = L \cdot dI/dt$ |
| Transmission line | T | $\Omega$ | Distributed; covered in Ch7 |

> **Engineering Intuition:** Only real devices can be measured; only ideal elements can be calculated. Our goal: create a model whose impedance closely matches the measured impedance of the real device.

## 3.3 Impedance in the Time Domain

| Element | $Z_{\text{TD}}$ | Insight |
|:--|:--|:--|
| R | $Z = R$ | Constant, boring |
| C | $Z = \dfrac{V}{C \cdot dV/dt}$ | Depends on waveform shape — **complicated** |
| L | $Z = \dfrac{L \cdot dI/dt}{I}$ | Depends on waveform shape — **complicated** |

> **Engineering Intuition:** Impedance of C and L in the time domain is NOT simple. This is why we move to the frequency domain.

## 3.4 Impedance in the Frequency Domain (Sine Wave Excitation)

Angular frequency: $\omega = 2\pi f$

| Element | $Z(\omega)$ (complex) | Magnitude | Phase |
|:--|:--:|:--:|:--:|
| R | $R$ | $R$ | $0^\circ$ |
| C | $1 / (j\omega C)$ | $1/(\omega C)$ | $-90^\circ$ (capacitive) |
| L | $j\omega L$ | $\omega L$ | $+90^\circ$ (inductive) |

**Key insight:** Even though $C$ and $L$ values are constant with frequency, their **impedances** vary:

$$
|Z_C| = \frac{1}{\omega C} \quad\text{(decreases with frequency)}
$$
$$
|Z_L| = \omega L \quad\text{(increases with frequency)}
$$

**Example:** A 10 nF capacitance at 1 GHz:
$$|Z_C| = 1 / (2\pi \times 10^9 \times 10^{-8}) = 0.016\ \Omega$$

The same capacitor's series 2 nH inductance at 1 GHz:
$$|Z_L| = 2\pi \times 10^9 \times 2\times 10^{-9} = 12.6\ \Omega$$

> **Engineering Intuition:** At high frequencies, the inductor's impedance dominates the real capacitor's behavior. This is why decoupling capacitors have a self-resonant frequency (SRF).

## 3.5 Equivalent Circuit Models (RLC Series)

Impedance of a series RLC circuit:

$$
Z(\omega) = R + j\omega L + \frac{1}{j\omega C}
$$

**Self-resonant frequency** (SRF) where $Z_L = Z_C$:

$$
f_{\text{SR}} = \frac{1}{2\pi\sqrt{LC}}
$$

At $f < f_{\text{SR}}$: capacitive behavior ($-90^\circ$ phase)
At $f = f_{\text{SR}}$: purely resistive ($Z = R$, $0^\circ$ phase)
At $f > f_{\text{SR}}$: inductive behavior ($+90^\circ$ phase)

**Example — 1 nF decoupling capacitor model:**
$$C = 0.67\ \text{nF},\quad R = 0.5\ \Omega,\quad L = 1.78\ \text{nH}$$
$$f_{\text{SR}} = \frac{1}{2\pi\sqrt{1.78\times 10^{-9} \times 0.67\times 10^{-9}}} \approx 145\ \text{MHz}$$

Model bandwidths:
- 1st-order (just C): $BW \approx 70$ MHz
- 2nd-order (RLC): $BW > 5$ GHz

> **Engineering Intuition:** Start with the simplest model first (Einstein's principle: "as simple as possible, but not simpler"). A single C is fine for low frequency; add L and R as bandwidth requirements increase.

## 3.6 Common Model Topologies

| Component | Low-Frequency Model | High-Frequency Model |
|:--|:--|:--|
| Real resistor | R | R + L (series) |
| Real capacitor | C | R + L + C (series) |
| Real inductor | L | R + L + C (parallel) |
| PCB trace (short) | C | LC ($\pi$ or $T$) |
| Wire bond | L | R + L + C |

## 3.7 Using SPICE for Impedance Analysis

An impedance analyzer in SPICE:
1. Use a constant-current AC source (1 A amplitude)
2. Connect the circuit under test across its terminals
3. The voltage across the source = impedance in Ohms (since $V = Z \times 1\text{A}$)

**SPICE simulation types:**
- **Transient:** time-domain analysis
- **AC:** frequency-domain analysis (swept sine wave)

> **Engineering Intuition:** If the schematic can be drawn, SPICE can simulate it. This is the real power of SPICE for general electrical engineering analysis.

## 3.8 Resistor Technologies and Bandwidth

| Resistor Type | Bandwidth as Ideal R |
|:--|:--:|
| Integrated Passive Device (IPD) | >5 GHz |
| Surface Mount (SMT) | ~2 GHz |
| Axial lead | ~500 MHz |

## 3.9 Key Formulas

| Formula | Description |
|:--|:--|
| $Z = V/I$ | Definition of impedance |
| $V = I \cdot R$ | Resistor I-V |
| $I = C \cdot dV/dt$ | Capacitor I-V (time domain) |
| $V = L \cdot dI/dt$ | Inductor I-V (time domain) |
| $Z_C = 1/(j\omega C)$ | Capacitor impedance (freq domain) |
| $Z_L = j\omega L$ | Inductor impedance (freq domain) |
| $\omega = 2\pi f$ | Angular frequency |
| $f_{\text{SR}} = 1/(2\pi\sqrt{LC})$ | Self-resonant frequency |
| $Z_{\text{RLC}} = R + j\omega L + 1/(j\omega C)$ | Series RLC impedance |
