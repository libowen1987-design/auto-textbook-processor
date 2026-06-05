---
chapter: 10
title: Shielding
source: Paul, Clayton R. *Introduction to Electromagnetic Compatibility*, 2nd Ed., Wiley, 2006
pages: 737-776
---

# Chapter 10: Shielding

## 10.1 Shielding Effectiveness (SE)

Shielding effectiveness is the ratio of fields with and without the shield:

$$\text{SE} = 20 \log_{10}\left(\frac{E_0}{E_1}\right) \text{ dB} \quad \text{or} \quad 20 \log_{10}\left(\frac{H_0}{H_1}\right) \text{ dB}$$

### Total SE Components

$$\text{SE} = A + R + B \quad \text{(dB)}$$

where:
- $A$ = absorption loss (penetration loss through the shield)
- $R$ = reflection loss (impedance mismatch at air-metal interfaces)
- $B$ = multiple reflection correction (important only for thin shields where $A < 10$ dB)

## 10.2 Absorption Loss

### Skin Depth

$$\delta = \frac{1}{\sqrt{\pi f \mu \sigma}} = \frac{66.1}{\sqrt{f \mu_r \sigma_r}} \text{ mm}$$

where $\sigma_r$ = conductivity relative to Cu.

| Material | $\sigma_r$ | $\mu_r$ | $\delta$ at 1 MHz | $\delta$ at 100 MHz |
|---|---|---|---|---|
| Copper | 1.00 | 1 | 0.066 mm | 6.6 $\mu$m |
| Aluminum | 0.61 | 1 | 0.085 mm | 8.5 $\mu$m |
| Steel | 0.17 | 200 | 0.17 mm | 17 $\mu$m |
| Mu-metal | 0.03 | 30,000 | 5.5 mm | 0.55 mm |

### Absorption Loss Formula

$$A = 3.34 \cdot t \sqrt{f \mu_r \sigma_r} \quad \text{(dB)}$$

where $t$ = shield thickness in mm, $f$ in MHz.

**In English units** (t in mils):

$$A = 0.1314 \cdot t \sqrt{f \mu_r \sigma_r} \quad \text{(dB)}$$

### Absorption Characteristics
- Increases with $\sqrt{f}$ (10 dB/decade)
- Proportional to thickness
- Higher for magnetic materials (steel has $\mu_r = 200$)

## 10.3 Reflection Loss

Reflection loss depends on the **wave impedance** relative to the shield impedance:

$$R = 20 \log_{10}\left|\frac{Z_w}{4Z_s}\right| \quad \text{(dB)}$$

where:
- $Z_w$ = wave impedance (far-field: $\eta_0 = 377\ \Omega$)
- $Z_s$ = intrinsic impedance of shield material = $\sqrt{j\omega\mu/\sigma}$

### Electric Field Reflection Loss (Far Field / Plane Wave)

$$R_E = 168 - 20 \log_{10}\left(\sqrt{\frac{\mu_r}{f \sigma_r}}\right) \quad \text{(dB)}$$

For copper ($\mu_r=1, \sigma_r=1$) at 1 MHz:

$$R_E = 168 - 20 \log_{10}\left(\sqrt{\frac{1}{1 \times 10^6}}\right) = 168 + 60 = 228 \text{ dB}$$

### Magnetic Field Reflection Loss (Near Field, H-Wave)

$$R_H = 14.6 + 10 \log_{10}\left(\frac{f \sigma_r}{\mu_r}\right) \quad \text{(dB)}$$

For copper at 1 MHz:

$$R_H = 14.6 + 10 \log_{10}(10^6) = 14.6 + 60 = 74.6 \text{ dB}$$

### Electric vs. Magnetic Field Reflection

| Field Type | $R$ vs. $f$ | $R$ vs. $\sigma$ | Magnitude |
|---|---|---|---|
| E-field (near) | Decreases with $f$ (5 dB/decade) | Increases | Very high (> 200 dB at low frequencies) |
| H-field (near) | Increases with $f$ (10 dB/decade) | Increases | Lower (20–80 dB at low frequencies) |
| Plane wave (far) | Decreases with $f$ (10 dB/decade) | Increases | Moderate (80–120 dB) |

## 10.4 Multiple Reflection Correction

When the shield is thin ($A < 10$ dB), internal reflections enhance the transmitted field:

$$B = 20 \log_{10}\left(1 - e^{-2t/\delta}\right) \text{ dB}$$

$B$ is negative (reduces SE) and is most significant for:
- Thin magnetic shields (low $A$)
- Low frequencies (large $\delta$)

## 10.5 Apertures and Slots

Apertures degrade shielding dramatically. The maximum dimension determines the cutoff:

### Slot Antenna Effect

A slot of length $\ell_s$ behaves as a resonant slot antenna at:

$$f_{\text{res}} = \frac{c}{2\ell_s} = \frac{150}{\ell_s(\text{m})} \text{ MHz}$$

**Rule:** For $\ell_s < \lambda/100$, the degradation is small. For $\ell_s > \lambda/20$, the shield is ineffective.

### Aperture Degradation

$$\text{SE}_{\text{aperture}} = 20 \log_{10}\left(\frac{\lambda}{2\ell_s}\right) \text{ dB} \quad (\ell_s \ll \lambda)$$

| Slot Length | Degradation at 100 MHz ($\lambda = 3$ m) |
|---|---|
| 1 cm | 43 dB |
| 10 cm | 23 dB |
| 30 cm | 14 dB |

### Aperture Array

For a grid of apertures of spacing $s$:

$$\text{SE}_{\text{grid}} = 20 \log_{10}\left(\frac{\lambda}{s}\right) - 20 \log_{10}\sqrt{N} \quad \text{dB}$$

where $N$ = number of apertures.

## 10.6 Gasket Design

Finger stock, conductive elastomer, or knitted mesh gaskets restore SE across seams.

| Gasket Type | Typical SE | Compression | Cost |
|---|---|---|---|
| Finger stock (BeCu) | 80–100 dB | Moderate | Medium |
| Conductive elastomer | 60–80 dB | Low | Low |
| Knitted wire mesh | 50–70 dB | Moderate | Low |
| Conductive foam | 30–50 dB | Very low | Low |

**Key design rules:**
- Gasket compression should be 20–50% of initial height
- Flange must be conductive (paint-free, corrosion-resistant)
- Bolt spacing: every $\lambda/20$ maximum (e.g., 3 cm at 500 MHz)

## 10.7 Honeycomb Vent Panels

For ventilation, honeycomb panels provide waveguide-below-cutoff attenuation:

$$f_c = \frac{c}{2a} \quad \text{(TE}_{10}\text{ mode)}$$

where $a$ = largest cell dimension.

$$\text{SE}_{\text{honeycomb}} = 27.3 \frac{t}{a} \quad \text{(dB/cell)}$$

for $f < f_c$.

## 10.8 Cable Shield Termination

### Shield Current Transfer Impedance

$$Z_t = \frac{1}{V_{\text{shield}}} \left.\frac{dV_{\text{inner}}}{dz}\right|_{I_{\text{shield}}}$$

Low $Z_t$ = good shielding. In practice, the cable shield **must be terminated with 360° contact**, not a pigtail.

| Termination | $Z_t$ at 100 MHz | SE Degradation |
|---|---|---|
| 360° ferrule/connector | < 1 m$\Omega$/m | 0 dB |
| Pigtail (1 cm) | 10–50 m$\Omega$/m | 10–20 dB |
| Pigtail (5 cm) | 50–500 m$\Omega$/m | 20–40 dB |
| No connection | ∞ | 0 dB |

## 10.9 Engineering Intuition

1. **Reflection loss is high for electric fields, low for magnetic fields.** H-field shielding requires **magnetic materials** (steel, mu-metal) or **thick copper**.

2. **A 0.1 mm gap renders a 1 mm copper shield useless** at 1 GHz ($\ell_{\text{gap}} = 0.1$ m → $f_{\text{res}} = 1.5$ GHz — close to the operating band).

3. **Magnetic field shielding below 100 kHz is extremely difficult.** Skin depth in Cu at 60 Hz is 8.5 mm. Use mu-metal ($\mu_r = 30,\!000$, $\delta = 0.55$ cm at 60 Hz).

4. **Cable pigtails are the #1 cause of shielding failures.** Every dB of SE from the enclosure is lost if the cable shield is terminated with a 2 cm pigtail.

5. **Multiple thin shields > one thick shield** for H-fields: two 0.5 mm steel sheets with an air gap provide more H-field SE than one 1 mm sheet.
