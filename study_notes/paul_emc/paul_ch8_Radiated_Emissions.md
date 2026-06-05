---
chapter: 8
title: Radiated Emissions
source: Paul, Clayton R. *Introduction to Electromagnetic Compatibility*, 2nd Ed., Wiley, 2006
pages: 527-582
---

# Chapter 8: Radiated Emissions

## 8.1 Differential-Mode (DM) Radiation

DM radiation is caused by signal current flowing in a loop. This is the "intentional" signal path.

### Small Loop Model ($A \ll \lambda^2$)

$$E_{\text{DM}} = \eta_0 \cdot \frac{I \cdot A \cdot k^2}{4\pi r} \cdot \sin\theta \quad \text{(V/m)}$$

where:
- $\eta_0 = 120\pi \approx 377\ \Omega$
- $A$ = loop area (m²)
- $k = 2\pi/\lambda$ = wavenumber
- $r$ = distance (m)

**In the far field and maximum direction ($\theta = 90^\circ$):**

$$E_{\text{DM, max}} = \frac{2.63 \times 10^{-3} \cdot I \cdot A \cdot f^2}{r} \quad \text{(V/m)}$$

or in dB$\mu$V/m:

$$E_{\text{DM}} = 40 \log_{10}(f) + 20 \log_{10}(\text{I}) + 20 \log_{10}(\text{A}) - 20 \log_{10}(\text{r}) + 88.4$$

### DM Characteristics
- **Increases with $f^2$** (40 dB/decade)
- **Proportional to loop area** $A$ (reduce area to reduce radiation)
- **Proportional to current** $I$

## 8.2 Common-Mode (CM) Radiation

CM radiation is caused by unintentional current flowing in the same direction on all signal conductors, using ground/cable as an antenna.

### Short Monopole Model

$$E_{\text{CM}} = \eta_0 \cdot \frac{I_{\text{CM}} \cdot \ell \cdot k}{4\pi r} \cdot \sin\theta \quad \text{(V/m)}$$

where $\ell$ = cable length (m).

**Maximum far-field:**

$$E_{\text{CM, max}} = \frac{4.71 \times 10^{-2} \cdot I_{\text{CM}} \cdot \ell \cdot f}{r} \quad \text{(V/m)}$$

### CM Characteristics
- **Increases with $f$** (20 dB/decade)
- **Proportional to cable length** $\ell$
- **CM current is small** (μA–mA) but still dominates DM above ~30 MHz

### CM Dominance Over DM

The ratio of CM to DM fields:

$$\frac{E_{\text{CM}}}{E_{\text{DM}}} = \frac{18 \cdot \ell}{A \cdot f}$$

For $A = 1$ cm², $\ell = 10$ cm, $f = 100$ MHz:

$$\frac{E_{\text{CM}}}{E_{\text{DM}}} = \frac{18 \cdot 0.1}{10^{-4} \cdot 10^8} = 180 \gg 1$$

**Conclusion:** CM radiation dominates for typical PCB geometries above a few MHz.

## 8.3 FCC/CISPR Radiated Emission Limits

### FCC Class B @ 3 m

| Frequency (MHz) | Limit (dB$\mu$V/m) | Limit ($\mu$V/m) |
|---|---|---|
| 30–88 | 40.0 | 100 |
| 88–216 | 43.5 | 150 |
| 216–960 | 46.0 | 200 |
| 960–1000 | 54.0 | 500 |

### Conversion between Measurement Distances

$$E_{\text{d2}} = E_{\text{d1}} + 20 \log_{10}\left(\frac{d_1}{d_2}\right)$$

e.g., 40 dB$\mu$V/m @ 3 m → 30 dB$\mu$V/m @ 10 m (assuming far-field).

## 8.4 Radiated Emission Measurement

### Open Area Test Site (OATS)

The classic measurement site: a conducting ground plane with no reflecting objects.

**Normalized Site Attenuation (NSA):**

$$\text{NSA} = \frac{V_{\text{direct}}}{V_{\text{site}}}$$

NSA must be within ±4 dB of ideal for CISPR compliance.

### Alternative Test Sites

| Site Type | Pros | Cons | Cost |
|---|---|---|---|
| OATS | Most accurate | Weather dependent | Low |
| Semi-anechoic | Weather independent, convenient | Absorber cost/damage | High |
| Fully anechoic | No ground reflection | Less common for FCC | High |
| TEM cell | Coupling measurement | Small EUT only | Moderate |
| GTEM cell | Broadband, quick | Correlation needed | Moderate |

### Measurement Procedure

1. **Prescan:** EUT rotated 360°, antenna at 1–4 m height
2. **Maximize:** Find worst-case EUT orientation and antenna height
3. **Final:** QP measurement at peak frequencies
4. **Record:** Polarization (H/V), frequency, amplitude, margin

## 8.5 Mitigation of Radiated Emissions

| Technique | Effect | Typical Reduction |
|---|---|---|
| Reduce loop area | Reduces DM | 10–20 dB |
| Add CM choke on cables | Reduces CM | 10–30 dB |
| Ground plane | Reduces DM loop, shields | 10–30 dB |
| Shielded cable | Eliminates cable radiation | 20–40 dB |
| Ferrite core on cable | Absorbs CM current | 5–15 dB |
| Filtered I/O connectors | CM/DM filter | 20–40 dB |
| Slow edge rate | Reduces HF content | 10–20 dB |
| Spread-spectrum clocking | Reduces peak harmonics | 8–12 dB |

## 8.6 Engineering Intuition

1. **DM radiation is designed; CM radiation is accidental.** DM follows the intended signal path; CM is a parasitic antenna created by cables and ground loops.

2. **The "antenna factor" of your product** is determined by its largest conductor — typically the connected cables.

3. **FCC limits at 30 MHz are brutal.** A product passing below 30 MHz might fail the first harmonic at 50 MHz by 20 dB.

4. **The $f^2$ vs $f$ dependence** means: at low frequencies DM dominates; above a crossover frequency, CM dominates. The crossover is usually 5–30 MHz.

5. **Near-field vs. far-field:** At 3 m, 30 MHz ($\lambda = 10$ m) is in the near field. At 1 GHz ($\lambda = 0.3$ m), it's firmly in the far field.
