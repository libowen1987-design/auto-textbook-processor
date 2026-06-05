---
chapter: 1
title: Introduction to Electromagnetic Compatibility (EMC)
source: Paul, Clayton R. *Introduction to Electromagnetic Compatibility*, 2nd Ed., Wiley, 2006
pages: 1-48
---

# Chapter 1: Introduction to EMC

## 1.1 The EMC Problem

EMC is the ability of an electronic system to function compatibly in its electromagnetic environment without causing or suffering interference. Three essential elements form the EMC framework:

```
Source (Emitter) → Coupling Path → Receptor (Victim)
```

Interference occurs when the received energy causes the receptor to behave undesirably.

### 1.1.1 Coupling Mechanisms

| Coupling Mode | Physical Mechanism | Typical Mitigation |
|---|---|---|
| Conducted | Shared power/ground impedance | Filtering, decoupling |
| Radiated | EM field coupling | Shielding, layout |
| Capacitive | Electric field between conductors | Increased spacing, shielding |
| Inductive | Magnetic field coupling | Twisted pair, shielding |

## 1.2 Frequency vs. Wavelength: Electrical Dimensions

An essential concept: a circuit is **electrically large** when its physical dimensions exceed approximately $\lambda/10$.

$$\lambda = \frac{c}{f} = \frac{3 \times 10^8}{f} \text{ m}$$

| Frequency | Wavelength | $\lambda/10$ |
|---|---|---|
| 1 MHz | 300 m | 30 m |
| 100 MHz | 3 m | 30 cm |
| 1 GHz | 30 cm | 3 cm |
| 10 GHz | 3 cm | 3 mm |

**Engineering intuition:** At 1 GHz, even a 3 cm PCB trace is electrically significant — it behaves as a transmission line, not a wire.

## 1.3 Decibel Notation (Fundamental to EMC)

EMC specifications are universally expressed in dB. Key definitions:

$$\text{dB}\mu\text{V} = 20 \log_{10}\left(\frac{V}{1\ \mu\text{V}}\right)$$

$$\text{dBm} = 10 \log_{10}\left(\frac{P}{1\ \text{mW}}\right)$$

$$\text{dB}\mu\text{V/m} = 20 \log_{10}\left(\frac{E}{1\ \mu\text{V/m}}\right)$$

**Useful conversions:**
- $0\ \text{dBm} = 107\ \text{dB}\mu\text{V}$ (into $50\ \Omega$)
- $P(\text{dBm}) = V(\text{dB}\mu\text{V}) - 107$

## 1.4 EMC Regulations Overview

Three regulatory domains dominate commercial EMC:

| Region | Emissions | Immunity |
|---|---|---|
| USA | FCC Part 15 | (FCC) |
| Europe | EN 55022 (CISPR 22) | EN 55024 |
| International | CISPR 22 | IEC 61000-4 |

**Key limits (FCC Class B, residential):**
- Conducted (150 kHz–30 MHz): 48 dB$\mu$V quasi-peak
- Radiated (30–230 MHz): 40 dB$\mu$V/m @ 3m
- Radiated (230–1000 MHz): 47 dB$\mu$V/m @ 3m

## 1.5 EMC Design Philosophy

**The golden rule of EMC:** Suppress emissions at the source. Filtering and shielding at the receptor are last resorts.

**Three-level EMC design hierarchy:**
1. **PCB-level** (best): proper layer stackup, decoupling, routing
2. **Cable-level**: filtering, ferrite beads, shielded cables
3. **System-level** (worst/most expensive): external shielding, add-on filters

## 1.6 Time Delay and Velocity of Propagation

Signal propagation velocity on a PCB is determined by the dielectric:

$$v = \frac{c}{\sqrt{\varepsilon_r}}$$

| Medium | $\varepsilon_r$ | Velocity | Delay/in |
|---|---|---|---|
| Free space/air | 1.0 | $3.0 \times 10^8$ m/s | 85 ps/in |
| FR-4 microstrip | ~3.5 | $1.6 \times 10^8$ m/s | ~160 ps/in |
| FR-4 stripline | 4.7 | $1.38 \times 10^8$ m/s | 183 ps/in |

**Critical rule-of-thumb:** When the one-way transit time exceeds $1/6$ of the signal rise time, transmission line effects must be considered:

$$L_{\text{crit}} > \frac{t_r}{6 \cdot t_{pd}}$$

For FR-4 microstrip with $t_r = 1$ ns: $L_{\text{crit}} \approx 1.0$ inch.

## 1.7 Common EMC Myths Debunked

| Myth | Reality |
|---|---|
| "Only high frequencies matter" | The **edges** of digital signals contain high frequencies regardless of clock rate |
| "Ground pours always help" | Floating ground pours act as parasitic antennas |
| "Ferrite beads are always good" | They only work well in the impedance-matched regime |
| "Slower clock = no EMC problem" | Rise time matters more than clock frequency |
