# David K. Cheng《Field and Wave Electromagnetics》2nd Ed Chapter 11

> 本笔记基于 OCR 文本清洗整理，100% 来源于原书内容。

## Chapter 11 — Antennas and Radiating Systems

### 11-1. Introduction

**Antennas** are structures designed for radiating electromagnetic energy and information into (or receiving from) free space. They convert guided waves on transmission lines to radiating waves in space, and vice versa.

### 11-2. Radiation Fields of Elemental Dipoles

#### 11-2.1. The Elemental Electric Dipole (Hertzian Dipole)

An **elemental electric dipole** is a short conducting wire (length $l \ll \lambda$) carrying a uniform current $I_0$:

$$\mathbf{E}(r) \approx j\eta_0\frac{k I_0 l}{4\pi r}e^{-jkr}\sin\theta\,\hat{\boldsymbol{\theta}} + O\left(\frac{1}{r^2}\right)$$
$$\mathbf{H}(r) \approx j\frac{k I_0 l}{4\pi r}e^{-jkr}\sin\theta\,\hat{\boldsymbol{\phi}} + O\left(\frac{1}{r^2}\right)$$

**Far-field region** ($kr \gg 1$): Only the $1/r$ terms survive.
$$\mathbf{E}_\text{rad} = j\eta_0\frac{I_0 l}{2\pi r}\sin\theta\,e^{-jkr}\,\hat{\boldsymbol{\theta}}$$
$$\mathbf{H}_\text{rad} = \frac{1}{\eta_0}\hat{\mathbf{r}} \times \mathbf{E}_\text{rad}$$

The radiation is **maximum in the broadside direction** ($\theta = 90°$) and **null along the axis** ($\theta = 0°, 180°$).

**Radiation resistance:**
$$R_{\text{rad}} = \frac{2\eta_0}{3\pi}\left(\frac{\pi l}{\lambda}\right)^2 = 80\pi^2\left(\frac{l}{\lambda}\right)^2 \quad (\Omega)$$

#### 11-2.2. The Elemental Magnetic Dipole

An elemental magnetic dipole is equivalent to a small current loop of area $S$ with uniform current $I$. Its magnetic field in the far zone is:

$$\mathbf{H}(r) \approx j\frac{k^2 S I}{4\pi r}e^{-jkr}\sin\theta\,\hat{\boldsymbol{\phi}}$$
$$\mathbf{E}(r) = -\eta_0 \hat{\mathbf{r}} \times \mathbf{H}(r)$$

The radiation pattern is identical to that of an elemental electric dipole (but rotated: maximum in the plane of the loop, null along the axis perpendicular to the loop).

### 11-3. Antenna Parameters

| Parameter | Definition |
|---|---|
| **Radiation pattern** | Spatial distribution of radiation intensity |
| **Beamwidth** | Angular width between half-power points (HPBW) |
| **Directivity $D$** | Ratio of maximum radiation intensity to average radiation intensity |
| **Gain $G$** | $G = \eta_{\text{rad}} D$ (accounting for ohmic losses) |
| **Input impedance** | Impedance presented at the antenna terminals |
| **Bandwidth** | Frequency range over which performance is acceptable |
| **Effective aperture $A_e$** | $A_e = \frac{\lambda^2}{4\pi}G$ (for isotropic: $A_e = \lambda^2/4\pi$) |
| **Polarization** | Polarization of the radiated wave |

**Directivity** of an antenna:
$$D = \frac{4\pi}{\Omega_A}$$
where $\Omega_A$ is the beam solid angle.

**Gain** (in dBi, relative to isotropic):
$$G_{\text{dBi}} = 10\log_{10} G$$

### 11-4. Thin Linear Antennas

#### 11-4.1. The Half-Wave Dipole

For a **half-wave dipole** ($\ell = \lambda/2$) with sinusoidal current distribution:
$$I(z) = I_0 \cos\left(\frac{\pi z}{\lambda}\right), \quad -\lambda/4 \leq z \leq \lambda/4$$

**Far-field:**
$$\mathbf{E}_\theta = j\eta_0\frac{I_0}{2\pi r}e^{-jkr}\frac{\cos(\pi/2\cos\theta)}{\sin\theta}\,\hat{\boldsymbol{\theta}}$$

**Half-power beamwidth (HPBW):** $\approx 78°$ in the E-plane.

**Directivity:** $D \approx 1.64$ ($2.15$ dBi).

**Input impedance:** $Z_{\text{in}} \approx 73 + j42.5$ $\Omega$. (Resonant when $l \approx 0.49\lambda$, giving $Z_{\text{in}} \approx 67 - j0$ $\Omega$.)

### 11-5. Antenna Arrays

#### 11-5.1. Two-Element Arrays

For two isotropic point sources separated by distance $d$, with equal amplitude $E_0$ and phase difference $\psi$:

**Total field:**
$$E_T = E_0 e^{-jkr_1} + E_0 e^{j\psi}e^{-jkr_2} = E_0 e^{-jkr}[1 + e^{j(kd\cos\theta + \psi)}]$$

**Array factor:**
$$AF = 2\cos\left(\frac{kd\cos\theta + \psi}{2}\right)$$

**Broadside array:** $\psi = 0$, $d = \lambda/2$ → maximum at $\theta = 90°$.

**Endfire array:** $\psi = -kd$ → maximum at $\theta = 0°$.

#### 11-5.2. General Uniform Linear Arrays

For an $N$-element uniform linear array with spacing $d$ and progressive phase shift $\psi$:

$$\text{AF} = \frac{\sin(N\Phi/2)}{\sin(\Phi/2)}$$
where $\Phi = kd\cos\theta + \psi$.

**Main beam** occurs when $\Phi = 0$ (broadside to the array axis if $\psi = 0$).

### 11-6. Receiving Antennas

**Equivalent circuit** of a receiving antenna:
$$Z_{\text{in}} = R_{\text{rad}} + R_{\text{loss}} + jX_{\text{in}}$$

**Effective aperture** of a lossless antenna:
$$A_e = \frac{\lambda^2}{4\pi}D$$

The **received power:**
$$P_r = A_e S_{\text{inc}} = \frac{\lambda^2}{4\pi}D \cdot \frac{|E_{\text{inc}}|^2}{\eta_0}$$

### 11-7. Some Other Antenna Types

**Traveling-wave antenna ( Beverage antenna):** A long wire with a matched load at the far end. Produces an endfire pattern with single-lobe main beam.

**Yagi-Uda antenna:** A parasitic array with one driven element, one reflector, and several directors. High gain (up to 15 dBi) with a simple structure.

**Broadband antennas:** Log-periodic antennas maintain constant input impedance and radiation pattern over a wide frequency range (ratio $f_{\max}/f_{\min} \approx 10:1$).

### 11-8. Aperture Radiators

An aperture antenna (e.g., horn antenna, open-ended waveguide) radiates from an aperture. The field in the far zone can be computed using **Huygens's principle** — the aperture is treated as a distribution of equivalent sources (electric and magnetic currents).

### Review Questions (Chapter 11)

1. What is the radiation resistance of a Hertzian dipole?
2. What is the far-field pattern of a half-wave dipole?
3. Define directivity, gain, and effective aperture.
4. What is the array factor for a two-element array?
5. Why is the Yagi-Uda antenna called a parasitic array?
6. Explain Huygens's principle as applied to aperture radiation.

---

## Appendix A — Symbols and Units

**Fundamental SI units:**
- Length: meter (m)
- Mass: kilogram (kg)
- Time: second (s)
- Current: ampere (A)

**Derived quantities:** Force (N), Energy (J), Power (W), Voltage (V), Resistance ($\Omega$), Capacitance (F), Inductance (H), Magnetic flux (Wb), Magnetic flux density (T), etc.

## Appendix B — Useful Material Constants

| Quantity | Symbol | Value |
|---|---|---|
| Permittivity of free space | $\varepsilon_0$ | $8.854 \times 10^{-12}$ F/m |
| Permeability of free space | $\mu_0$ | $4\pi \times 10^{-7}$ H/m |
| Speed of light in vacuum | $c$ | $2.998 \times 10^8$ m/s |
| Characteristic impedance of free space | $\eta_0$ | $120\pi \approx 376.73$ $\Omega$ |
| Electron charge | $e$ | $-1.602 \times 10^{-19}$ C |
| Electron rest mass | $m_e$ | $9.109 \times 10^{-31}$ kg |

**Relative permittivities (dielectric constants):**
- Vacuum: 1 (exact)
- Air: 1.00059
- Polystyrene: 2.56
- Glass: 4–7
- Water: ~80

**Conductivities:**
- Copper: $\sigma \approx 5.8 \times 10^7$ S/m
- Aluminum: $\sigma \approx 3.5 \times 10^7$ S/m
- Seawater: $\sigma \approx 4$ S/m
- Dry earth: $\sigma \approx 10^{-3}$ S/m

**Relative permeabilities:**
- Free space: 1
- Iron: 5000 (varies)
- Ferrite: 100–3000

---

*Notes compiled from David K. Cheng, "Field and Wave Electromagnetics," 2nd Edition, Addison-Wesley, 1983. All formulas, equations, and values derived from the original text.*
