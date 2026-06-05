---
chapter: 5
title: Nonideal Behavior of Components
source: Paul, Clayton R. *Introduction to Electromagnetic Compatibility*, 2nd Ed., Wiley, 2006
pages: 323-400
---

# Chapter 5: Nonideal Behavior of Components

## 5.1 Wires — Resistance and Internal Inductance

### DC Resistance

$$R_{\text{dc}} = \frac{L}{\sigma A} = \frac{L}{\sigma \pi r_w^2}$$

### Skin Depth

$$\delta = \frac{1}{\sqrt{\pi f \mu_0 \sigma}} = \frac{66.1}{\sqrt{f/1\text{Hz}}} \text{ mm (Cu)}$$

| Frequency | Skin Depth (Cu) |
|---|---|
| 60 Hz | 8.5 mm |
| 1 kHz | 2.09 mm |
| 1 MHz | 66 $\mu$m |
| 100 MHz | 6.6 $\mu$m |
| 1 GHz | 2.1 $\mu$m |

### High-Frequency Resistance ($r_w \gg \delta$)

$$R_{\text{hf}} = \frac{L}{2r_w} \sqrt{\frac{f \mu_0}{\pi \sigma}} = \frac{L}{2r_w \sigma \delta}$$

Per-unit-length:

$$r_{\text{hf}} = \frac{1}{2r_w} \sqrt{\frac{\mu_0}{\pi \sigma}} \sqrt{f} \quad \text{(} \Omega \text{/m)}$$

### Internal Inductance (Skin Effect Region)

$$L_{i,\text{hf}} = \frac{R_{\text{hf}}}{2\pi f} = \frac{1}{4\pi r_w} \sqrt{\frac{\mu_0}{\pi \sigma}} \frac{1}{\sqrt{f}} \quad \text{(H/m)}$$

**Key insight:** Internal inductance drops as $1/\sqrt{f}$ in the skin-effect regime. External inductance (geometry-based) is frequency-independent and dominates at high frequencies.

## 5.2 Resistors — High-Frequency Model

At high frequencies, a resistor behaves as:

$$Z_R = R \parallel C_{\text{parasitic}} \quad \text{in series with } L_{\text{lead}}$$

| Resistor Type | Typical $C_{\text{parasitic}}$ | Typical $L_{\text{lead}}$ | SRF |
|---|---|---|---|
| Carbon comp | ~0.3–0.5 pF | ~5–10 nH | ~500 MHz |
| Metal film | ~0.1–0.3 pF | ~3–7 nH | ~1 GHz |
| Wirewound | ~0.5–2 pF | ~10–50 nH | ~100 MHz |
| SMD 0603 | ~0.05 pF | ~0.5 nH | ~5 GHz |

**SRF of resistor:** $F_{\text{SR}} = 1/(2\pi \sqrt{L_{\text{lead}} C_{\text{parasitic}}})$

## 5.3 Capacitors — ESR, ESL, and SRF

### Equivalent Series Model

$$Z_C = \text{ESR} + j\left(\omega \cdot \text{ESL} - \frac{1}{\omega C}\right)$$

### Self-Resonant Frequency

$$f_{\text{SR}} = \frac{1}{2\pi \sqrt{\text{ESL} \cdot C}}$$

### Impedance Behavior
- **Below SRF:** Capacitive ($Z \propto 1/\omega C$)
- **At SRF:** Minimum impedance ($Z = \text{ESR}$)
- **Above SRF:** Inductive ($Z \propto \omega \cdot \text{ESL}$)

| Capacitor Type | Typical C | Typical ESL | Typical $f_{\text{SR}}$ |
|---|---|---|---|
| Electrolytic | 10–1000 $\mu$F | 5–20 nH | 100–500 kHz |
| Tantalum | 1–100 $\mu$F | 2–10 nH | 500 kHz–5 MHz |
| Ceramic MLCC (0805) | 0.1 $\mu$F | ~1 nH | ~15 MHz |
| Ceramic MLCC (0402) | 1 nF | ~0.5 nH | ~200 MHz |
| X2Y (feedthrough) | 100 nF | ~0.1 nH | ~500 MHz |

### ESL Rules of Thumb
- Leaded capacitor: ESL ≈ 1 nH/mm of lead length
- SMD capacitor: ESL ≈ 0.5–1 nH per mm of body length
- Via to power plane adds ~0.3–0.5 nH

### Decoupling Capacitor Selection

$$f_{\text{max}} = \frac{1}{2\pi \cdot \text{ESL} \cdot C \cdot \text{(target impedance)}}$$

**Target impedance:** $Z_{\text{target}} = V_{\text{dd}} \times \text{ripple%} / \Delta I$

## 5.4 Inductors — Parasitic Capacitance and SRF

### Equivalent Parallel Model

$$Z_L = \frac{j\omega L}{1 - \omega^2 L C_p} \parallel R_p$$

### SRF

$$f_{\text{SR}} = \frac{1}{2\pi \sqrt{L C_p}}$$

At SRF, the inductor behaves as a high-impedance resonant circuit. Below SRF: inductive. Above SRF: capacitive.

## 5.5 Ferrite Beads

### Equivalent Circuit

Ferrite bead model at high frequencies is a lossy inductor:

$$Z_{\text{bead}} = R(f) + j\omega L(f)$$

where both $R$ and $L$ are frequency-dependent due to the complex permeability $\mu(f) = \mu'(f) - j\mu''(f)$.

- **Below 10 MHz:** Mostly inductive ($Z \approx j\omega L$)
- **10–300 MHz:** Lossy ($R \approx \omega L$; $Z \approx R$)
- **Above 300 MHz:** Purely resistive + roll-off

### Saturation
Ferrite beads saturate under DC bias. The inductance drops by 50–90% at rated DC current. **Always derate for DC bias current** — use beads rated for ≥ 2× the expected DC current.

### Impedance Selection
Choose ferrite bead such that $|Z|$ at the noise frequency is:
- 10–100 $\Omega$ for conducted emission filtering
- 100–600 $\Omega$ for high-impedance noise suppression
- 30–300 $\Omega$ at the resonant frequency of parasitic L-C circuit

## 5.6 PCB Trace Inductance and Capacitance

### Microstrip Inductance (for $w/h > 1$)

$$L_{\text{ms}} \approx 5.08 \times h \times \ln\left(\frac{2\pi h}{w} + \frac{w}{2\pi h}\right) \text{ nH/in}$$

### Microstrip Capacitance

$$C_{\text{ms}} \approx \frac{0.67(\varepsilon_r + 1.41)}{\ln(5.98h/(0.8w + t))} \text{ pF/in}$$

### Via Inductance

$$L_{\text{via}} \approx 5.08h \left[\ln\left(\frac{4h}{d}\right) + 1\right] \text{ nH}$$

where $h$ = via height, $d$ = via diameter (inches).

## 5.7 Engineering Intuition

1. **The humble capacitor** is the most misunderstood EMC component. At its SRF, it becomes inductive. A 1 nF cap resonates at ~200 MHz — use it to suppress 200 MHz noise, not 10 kHz ripple.

2. **Parallel capacitors** with different values (e.g., 10 $\mu$F ∥ 0.1 $\mu$F ∥ 1 nF) create anti-resonance peaks where the impedance spikes — use carefully.

3. **Ferrite beads** are not "magic noise blockers." They work by dissipating HF energy as heat in the ferrite material — they are lossy resistors at the noise frequency, not inductors.

4. **Mounting inductance dominates.** A 0.01 $\mu$F cap with 2 mm mounting via has ESL ~ 2 nH. Its SRF = 35 MHz, not the 5 GHz the SMD alone would suggest.
