---
chapter: 7
title: Antennas
source: Paul, Clayton R. *Introduction to Electromagnetic Compatibility*, 2nd Ed., Wiley, 2006
pages: 445-526
---

# Chapter 7: Antennas

## 7.1 Fundamental Antenna Parameters

### Radiation from a Current Element (Hertzian Dipole)

For an infinitesimal dipole of length $d\ell$ carrying current $I$:

$$E_\theta = j\eta_0 \frac{I d\ell}{2\lambda r} \sin\theta \cdot e^{-jkr} \quad \text{(V/m)}$$

$$H_\phi = j\frac{I d\ell}{2\lambda r} \sin\theta \cdot e^{-jkr} \quad \text{(A/m)}$$

### Power Density

$$S(r) = \frac{|E_\theta|^2}{\eta_0} \quad \text{(W/m}^2\text{)}$$

### Far-Field Condition

$$r_{\text{ff}} > \frac{2D^2}{\lambda} \quad \text{(for largest dimension } D\text{)}$$

At $r_{\text{ff}}$, the E and H fields are perpendicular and $E/H = \eta_0 = 120\pi \approx 377\ \Omega$.

## 7.2 Common EMC Antenna Types

### 7.2.1 Short Dipole ($\ell \ll \lambda$)

| Parameter | Formula |
|---|---|
| Effective length | $h_e = \ell/2$ |
| Radiation resistance | $R_r = 20\pi^2(\ell/\lambda)^2$ |
| Directivity | $D = 1.5$ (2.2 dB) |

### 7.2.2 Half-Wave Dipole ($\ell = \lambda/2$)

| Parameter | Formula |
|---|---|
| Effective length | $h_e = \lambda/\pi$ |
| Radiation resistance | $R_r = 73\ \Omega$ |
| Directivity | $D = 1.64$ (2.15 dB) |

### 7.2.3 Small Loop ($C_{\text{circ}} < \lambda/3$)

| Parameter | Formula |
|---|---|
| Radiation resistance | $R_r = 320\pi^4(NA/\lambda^2)^2$ |
| Effective length | $h_e = 2\pi NA/\lambda$ |
| Directivity | $D = 1.5$ (same as dipole) |

where $N$ = number of turns, $A$ = loop area.

### 7.2.4 Monopole over Ground Plane

| Parameter | Formula |
|---|---|
| Input impedance | $Z_{\text{in}} = Z_{\text{dipole}}/2$ |
| Directivity | $D = 3$ (twice dipole) |
| Quarter-wave ($\lambda/4$) | $R_r \approx 36.5\ \Omega$ |

### EMC Relevance

| Antenna | Typical Use in EMC |
|---|---|
| Dipole | Radiated emission measurement (30–300 MHz) |
| Biconical | Broadband emission testing (30–300 MHz) |
| Log-periodic | Broadband emission testing (200 MHz–1 GHz+) |
| Loop | Magnetic field emission measurement |
| Monopole | Vehicle-mounted antennas, ISM bands |

## 7.3 Antenna Factor

The **antenna factor** converts measured receiver voltage to field strength:

$$E = V_{\text{rec}} + \text{AF} \quad \text{(dB)}$$

where:
- $E$ = field strength at antenna (dB$\mu$V/m)
- $V_{\text{rec}}$ = receiver voltage (dB$\mu$V)
- $\text{AF}$ = antenna factor (dB/m)

For a lossless antenna:

$$\text{AF} = \frac{9.73}{\lambda \sqrt{G_{\text{ant}}}} \quad \text{(1/m)}$$

in dB:

$$\text{AF}_{\text{dB}} = 20\log_{10}\left(\frac{9.73}{\lambda}\right) - 10\log_{10}(G)$$

### Antenna Factor for Common Antennas
| Antenna | Typical AF (dB/m) | Freq Range |
|---|---|---|
| Biconical | 20–25 | 30–300 MHz |
| Log-periodic | 20–35 | 200–1000 MHz |
| Double-ridged horn | 20–40 | 1–18 GHz |

## 7.4 Receiving Antenna Equivalent Circuit

```
V_oc = E · h_eff ──┬── Z_ant ────┬── V_rec
                    │              │
                   GND           Z_rec
```

$$V_{\text{oc}} = E \cdot h_{\text{eff}}$$

where $h_{\text{eff}}$ = effective length of the antenna.

### Maximum Power Transfer

For conjugate match ($Z_{\text{ant}} = Z_{\text{rec}}^*$):

$$P_{\text{rec, max}} = \frac{V_{\text{oc}}^2}{8R_{\text{ant}}}$$

## 7.5 Balun (Balanced-to-Unbalanced Transformer)

Purpose: Efficiently couple a balanced antenna (dipole) to an unbalanced transmission line (coax).

Key parameters:
- Impedance transformation ratio (typically 1:1 or 4:1)
- Common-mode rejection (reduces CM current on coax shield)
- Bandwidth (limited by balun construction)

### Balun Types in EMC

| Type | Construction | Bandwidth | Common-Mode Rej. |
|---|---|---|---|
| Sleeve/choke balun | Coax sheath choke | 10:1 | > 20 dB |
| Transmission line | Coax wound on ferrite | 2:1 | > 30 dB |
| Ferrite core | Bifilar winding | 10:1 | > 40 dB |

## 7.6 Antenna Arrays

### Two-Element Array

Array factor for two isotropic sources separated by $d$:

$$\text{AF}(\theta) = 2 \cos\left(\frac{kd \cos\theta + \alpha}{2}\right)$$

where:
- $k = 2\pi/\lambda$
- $\alpha$ = phase difference between elements

### Nulls and Grating Lobes

| Condition | $d$ | Result |
|---|---|---|
| $\alpha = 0$ (broadside) | $d < \lambda/2$ | No grating lobes |
| $\alpha = 0$ | $d = \lambda$ | Grating lobes at $\pm 90^\circ$ |
| $\alpha = \pi$ (endfire) | $d < \lambda/2$ | Endfire radiation |

## 7.7 Engineering Intuition

1. **Any conductor is an antenna** at some frequency. A 1 m cable becomes an efficient quarter-wave monopole at 75 MHz.

2. **Effective length is the key to coupling.** A long cable has a large $h_e$ → higher $V_{\text{oc}}$ from incident fields.

3. **Far-field is closer than you think for EMC:** For a 10 cm cable at 300 MHz ($\lambda = 1$ m), $r_{\text{ff}} = 2(0.1)^2/1 = 0.02$ m. EMC measurements at 3 m are always in the far field for GHz-range frequencies.

4. **Loop antennas couple to H-fields; dipoles to E-fields.** Use loops for near-field magnetic probes, dipoles/log-periodics for far-field emission measurements.

5. **Antenna factor ≠ gain.** AF includes the antenna's impedance mismatch and ohmic losses. A high AF means the antenna is less sensitive (needs more field to produce a given receiver voltage).
