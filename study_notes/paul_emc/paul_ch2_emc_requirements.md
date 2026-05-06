---
chapter: 2
title: EMC Requirements
source: Paul, Clayton R. *Introduction to Electromagnetic Compatibility*, 2nd Ed., Wiley, 2006
pages: 49-90
---

# Chapter 2: EMC Requirements

## 2.1 Regulatory Framework

Three major regulatory bodies set emission and immunity standards worldwide:

| Region | Regulatory Body | Key Standard | Scope |
|---|---|---|---|
| USA | FCC | Part 15 | Radiated/Conducted emissions |
| Europe | CENELEC | EN 55022 (CISPR 22) | ITE emissions |
| International | CISPR/IEC | CISPR 22 / IEC 61000 | Emissions / Immunity |

### FCC Part 15 Classification

- **Class A**: Commercial/industrial — less restrictive (higher limit)
- **Class B**: Residential — more restrictive (lower limit by ~10 dB)

## 2.2 Conducted Emission Limits (150 kHz–30 MHz)

Conducted emissions are measured on power lines using a **LISN** (Line Impedance Stabilization Network).

| Band | FCC Class A (dB$\mu$V) | FCC Class B (dB$\mu$V) |
|---|---|---|
| 150–500 kHz | 79 (QP) / 66 (AVG) | 66–56* (QP) / 56–46* (AVG) |
| 500 kHz–5 MHz | 73 (QP) / 60 (AVG) | 56 (QP) / 46 (AVG) |
| 5–30 MHz | 73 (QP) / 60 (AVG) | 60 (QP) / 50 (AVG) |

*Limit decreases linearly with log(frequency)

## 2.3 Radiated Emission Limits (30 MHz–1 GHz)

Radiated emissions are measured at a specified distance (3 m for Class B, 10 m for Class A).

| Frequency (MHz) | FCC Class B @ 3m (dB$\mu$V/m) | FCC Class A @ 10m (dB$\mu$V/m) |
|---|---|---|
| 30–88 | 40.0 | 39.0 |
| 88–216 | 43.5 | 43.5 |
| 216–960 | 46.0 | 46.4 |
| 960–1000 | 54.0* | 49.5 |

*FCC actually specifies 49.5 for 960+ MHz Class B; check latest revision for exact values.

## 2.4 CISPR 22 Limits (EN 55022)

### Conducted (150 kHz–30 MHz)

| Frequency | Class A (dB$\mu$V) | Class B (dB$\mu$V) |
|---|---|---|
| 150–500 kHz | 79 (QP) / 66 (AVG) | 66–56 (QP) / 56–46 (AVG) |
| 500 kHz–30 MHz | 73 (QP) / 60 (AVG) | 56 (QP) / 46 (AVG) |

### Radiated (30 MHz–1 GHz)

| Frequency | Class A @ 10m | Class B @ 10m |
|---|---|---|
| 30–230 MHz | 40 dB$\mu$V/m (QP) | 30 dB$\mu$V/m (QP) |
| 230–1000 MHz | 47 dB$\mu$V/m (QP) | 37 dB$\mu$V/m (QP) |

## 2.5 The LISN (Line Impedance Stabilization Network)

The LISN serves three purposes:
1. **Stabilizes** line impedance at 50 $\Omega$ over the measurement band
2. **Blocks** the AC mains voltage while passing noise to the receiver
3. **Provides** a 50 $\Omega$ measurement port

**Typical LISN circuit (CISPR 16-1-2):**
- 50 $\mu$H inductor in series with L
- 1 $\mu$F capacitor to isolate mains
- 0.1 $\mu$F capacitor to measurement port
- 50 $\Omega$ internal impedance

$$\text{LISN impedance} \approx 50\ \Omega \parallel j\omega(50\ \mu\text{H})$$

At low frequencies (< 1 MHz), the 50 $\mu$H dominates; at high frequencies, the 50 $\Omega$ resistor sets the impedance.

## 2.6 Measurement Uncertainty & Quasi-Peak Detection

### Detector Types

| Detector | Time Constant (Charge) | Time Constant (Discharge) | Application |
|---|---|---|---|
| Peak (PK) | 1 ms | 550 ms | Initial scan |
| Quasi-Peak (QP) | 1 ms | 550 ms | CISPR compliance |
| Average (AVG) | — | — | Low-frequency noise |

**Important:** QP readings are always ≤ PK readings. For repetitive impulsive noise, QP ≈ PK. QP is the legally binding detector for CISPR/FCC.

## 2.7 Immunity Requirements (Overview)

| Standard | Phenomenon | Level |
|---|---|---|
| IEC 61000-4-2 | ESD | ±2, ±4, ±8, ±15 kV |
| IEC 61000-4-3 | Radiated RF | 3/10 V/m |
| IEC 61000-4-4 | EFT/Burst | ±0.5, ±1, ±2 kV |
| IEC 61000-4-5 | Surge | ±0.5, ±1, ±2 kV |
| IEC 61000-4-6 | Conducted RF | 3/10 V (150 kHz–80 MHz) |

## 2.8 Engineering Intuition: Margin and CISPR Quasi-Peak

**Margin = Limit − Measured Value** (positive = pass)

$$
\text{Margin (dB)} = L_{\text{limit}} - E_{\text{measured}}
$$

Industry best practice: **6 dB margin** minimum to account for:
- Measurement repeatability (±2–3 dB)
- Production variation
- Temperature drift
- Cable/setup variation

### Why quasi-peak exists:
Quasi-peak detection weights impulsive noise by "annoyance factor." A repetitive spark gap produces a higher QP reading than a steady CW tone at the same peak level. This mimics human perception of radio interference.
