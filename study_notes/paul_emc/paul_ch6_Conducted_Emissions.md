---
chapter: 6
title: Conducted Emissions
source: Paul, Clayton R. *Introduction to Electromagnetic Compatibility*, 2nd Ed., Wiley, 2006
pages: 401-444
---

# Chapter 6: Conducted Emissions

## 6.1 Conducted Emission Coupling Paths

Conducted emissions travel along power lines, signal cables, and ground connections in the 150 kHz–30 MHz frequency range.

**Three coupling paths:**
1. **Power line conducted:** Noise from the DUT propagates through the AC/DC power cord
2. **Signal cable conducted:** Common-mode currents on I/O cables
3. **Ground loop:** Voltage differences between grounds drive currents

### Differential-Mode (DM) vs. Common-Mode (CM)

| Mode | Definition | Path | Impedance | Mitigation |
|---|---|---|---|---|
| **DM** | Signal current on one wire, return on other | Line → L → Neutral | Low (source Z) | X-capacitor, DM choke |
| **CM** | Current in same direction on both wires | Line + Neutral → Earth | High (antenna) | CM choke, Y-capacitor |

$$V_{\text{noise, DM}} = I_{\text{DM}} \cdot Z_{\text{LISN}}$$

$$V_{\text{noise, CM}} = I_{\text{CM}} \cdot \frac{Z_{\text{LISN}}}{2}$$

**Typically:** CM emissions dominate above 5 MHz due to cable radiation and ground coupling.

## 6.2 The LISN (Line Impedance Stabilization Network)

### Purpose
1. Provides defined impedance (50 $\Omega$) to the DUT across 150 kHz–30 MHz
2. Isolates the AC mains from the measurement
3. Provides a 50 $\Omega$ measurement port to the receiver

### CISPR 16-1-2 LISN Equivalent Circuit

```
AC Mains ─┬─ 1 μF ── L = 50 μH ──┬─ 0.1 μF ──┬─ Receiver (50 Ω)
           │                       │            │
          GND                    GND          GND
```

### Impedance Characteristic

$$Z_{\text{LISN}}(f) = 50\ \Omega \parallel \left(j\omega \cdot 50\ \mu\text{H} + \frac{1}{j\omega \cdot 1\ \mu\text{F}}\right)$$

At 150 kHz: $Z \approx j\omega L = j47\ \Omega$ (inductive)
At 30 MHz: $Z \approx 50\ \Omega$ (resistive)

## 6.3 Conducted Emission Measurement

### Setup
```
DUT ──┬── LISN ──┬── Receiver
       │          │
      GND       GND
```

**Required equipment:**
- LISN (one per power line)
- EMI receiver (or spectrum analyzer with QP detector)
- Ground plane (reference)
- Cable clamp or ferrite cores on measurement cables

### Measurement Process
1. Initial scan: Peak detector, 150 kHz–30 MHz
2. Identify frequencies within 10 dB of limit
3. Final measurement: Quasi-peak at identified frequencies
4. If QP fails: diagnostic and rework

## 6.4 Conducted Emission Filters

### Input Filter Topology

```
LISN ──┬── L_CM ──┬── L_DM ───────┬── L_CM ──┬── DUT
       │          │                │          │
      C_Y1     C_X1              C_X2      C_Y2
       │          │                │          │
      GND      GND/Neutral      GND/Neutral  GND
```

### Component Selection

| Component | Function | Typical Value |
|---|---|---|
| $C_X$ (X-cap) | DM filtering, across L+N | 0.1–1.0 $\mu$F, Class X rated |
| $C_Y$ (Y-cap) | CM filtering, L/N to Earth | 1–10 nF, Class Y rated |
| $L_{\text{DM}}$ | DM choke | 10–100 $\mu$H |
| $L_{\text{CM}}$ | CM choke | 1–50 mH |

### Insertion Loss of a CM Choke

$$\text{IL}_{\text{CM}} = 20 \log_{10}\left(1 + \frac{j\omega L_{\text{CM}}}{Z_{\text{source}} + Z_{\text{load}}}\right) \text{ dB}$$

For ideal CM choke: $L_{\text{CM}} = L_{\text{leakage}} + L_{\text{mutual}}$

### CM Choke Saturation
- CM current: no net flux (DM cancelation) → low saturation
- DM current (imbalance): net flux → core saturation at high current
- **Leakage inductance provides DM filtering** (typically 0.5–2% of CM inductance)

## 6.5 FCC/CISPR Conducted Limits

### FCC Part 15 Class B (residential)

| Frequency (MHz) | Quasi-Peak (dB$\mu$V) | Average (dB$\mu$V) |
|---|---|---|
| 0.15–0.5 | 66–56* | 56–46* |
| 0.5–5 | 56 | 46 |
| 5–30 | 60 | 50 |

*Limit decreases linearly with log(frequency)

### Generic Limit Plot

$$\text{Margin} = \text{Limit} - \text{Measured} \quad \text{(dB)}$$

## 6.6 CM/DM Separation Techniques

### Hardware Method
Use a CM/DM rejection network (two current probes or a 1:1 transformer):

$$V_{\text{CM}} = \frac{V_L + V_N}{2} \quad V_{\text{DM}} = \frac{V_L - V_N}{2}$$

### Software Method
Measure voltage on Line and Neutral with phase information:

```python
V_CM = (V_line + V_neutral) / 2
V_DM = (V_line - V_neutral) / 2
```

### Diagnostic Rule
| Dominant Mode | Symptom | Fix |
|---|---|---|
| DM | High below 5 MHz | X-capacitor, larger DM choke |
| CM | High above 5 MHz | Y-capacitor, CM choke, shielded cable |

## 6.7 Engineering Intuition

1. **Always check conducted emissions first** — if DM is the problem, add X-caps. If CM is the problem, add Y-caps and CM choke.

2. **The LISN is your friend** — it provides a repeatable impedance. Without it, the line impedance varies from 2 to 200 $\Omega$ depending on the outlet.

3. **Cable-to-ground capacitance matters** — long cables increase CM current because cable capacitance provides a lower-impedance path to ground at higher frequencies.

4. **Y-capacitor leakage current is a safety issue** — for mains-powered equipment, total Y-cap leakage must be < 0.5 mA (UL) or < 3.5 mA (IEC). This limits $C_Y$ typically to 1–10 nF.
