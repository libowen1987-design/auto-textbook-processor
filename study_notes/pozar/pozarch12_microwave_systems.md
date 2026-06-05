# Pozar Ch12 (4e Ch14) — Introduction to Microwave Systems

> **Note:** This chapter corresponds to **Chapter 14** in Pozar *Microwave Engineering*, 4th Edition.
> It is the capstone chapter, integrating antennas, communications, radar, radiometry, propagation, and applications.

---

## 14.1 System Aspects of Antennas

### 14.1.1 Radiation Field and Power Density

From antenna theory, the **far-field** (Fraunhofer region) electric field of an antenna is:

$$
\mathbf{E}(r, \theta, \phi) = \frac{e^{-jkr}}{r} \, \mathbf{F}(\theta, \phi)
$$

where $\mathbf{F}(\theta, \phi)$ is the **vector radiation pattern** (units: V). The far-field is locally a TEM plane wave with $\mathbf{E} \perp \mathbf{H}$ and $\eta = \sqrt{\mu_0/\epsilon_0} \approx 377\;\Omega$.

**Time-averaged Poynting vector** (power density):

$$
\mathbf{S}_{\text{av}} = \frac{1}{2} \text{Re}[\mathbf{E} \times \mathbf{H}^*] = \hat{r} \, \frac{|\mathbf{E}|^2}{2\eta} \quad \text{[W/m}^2\text{]}
$$

### 14.1.2 Radiation Pattern Parameters

| Parameter | Definition | Units |
|---|---|---|
| **Directivity** $D$ | $D(\theta,\phi) = \frac{4\pi U(\theta,\phi)}{P_{\text{rad}}}$ | dimensionless |
| **Gain** $G$ | $G(\theta,\phi) = \frac{4\pi U(\theta,\phi)}{P_{\text{in}}} = \eta_{\text{rad}} D$ | dimensionless (often dB) |
| **Radiation efficiency** $\eta_{\text{rad}}$ | $P_{\text{rad}}/P_{\text{in}}$ | dimensionless |
| **Aperture efficiency** $\eta_{\text{ap}}$ | $A_e / A_p$ (effective / physical aperture) | dimensionless |
| **Effective aperture** $A_e$ | $A_e = \frac{\lambda^2}{4\pi} G$ | m² |
| **Beam solid angle** $\Omega_A$ | $\Omega_A = \iint_{4\pi} P_n(\theta,\phi)\,d\Omega$ | sr |
| **Half-power beamwidth** (HPBW) | Angular width where pattern drops 3 dB | degrees |

**Key identity — Gain and effective aperture:**

$$
G = \frac{4\pi A_e}{\lambda^2} \quad \Longleftrightarrow \quad A_e = \frac{\lambda^2}{4\pi} G
$$

> **量纲检查:** $G$ 无量纲，$A_e$ [m²], $\lambda^2$ [m²] ➔ $4\pi$ [sr] ✓

### 14.1.3 Antenna Noise Temperature

The **antenna noise temperature** $T_A$ accounts for external noise captured by the antenna:

$$
T_A = \frac{1}{\Omega_A} \iint_{4\pi} T_b(\theta, \phi) \, G_n(\theta, \phi) \, d\Omega \quad \text{[K]}
$$

where $T_b(\theta,\phi)$ is the brightness temperature of the scene.

Typical values at 1–10 GHz with a low-noise antenna pointing at zenith: $T_A \approx 5\text{–}30\;\text{K}$.

### 14.1.4 System Noise Temperature and G/T

The **system noise temperature** referred to the receiver input:

$$
T_{\text{sys}} = T_A + T_{\text{rec}}
$$

where $T_{\text{rec}}$ is the receiver noise temperature cascaded through the system (Friis formula for noise).

**Figure of merit for receiving systems:**

$$
\frac{G}{T} = \frac{G_{\text{ant}}}{T_{\text{sys}}} \quad \text{[dB/K]}
$$

This is the single most important metric for a receiving earth station: higher $G/T$ means better sensitivity.

> **Engineering intuition:** For satellite communications, $G/T$ directly sets the SNR at the detector for a given carrier power.

---

## 14.2 Wireless Communications

### 14.2.1 Friis Transmission Formula

For a transmit antenna with gain $G_t$ and receive antenna with gain $G_r$, separated by $R$:

$$
\frac{P_r}{P_t} = G_t G_r \left( \frac{\lambda}{4\pi R} \right)^2 \quad \text{(polarization-matched, free space)}
$$

**In dB form:**

$$
P_r \text{ [dBm]} = P_t \text{ [dBm]} + G_t \text{ [dB]} + G_r \text{ [dB]} - 20\log_{10}\!\left(\frac{4\pi R}{\lambda}\right)
$$

The term $L_{\text{fs}} = (4\pi R/\lambda)^2$ is the **free-space path loss**.

> **量纲检查:** $P_r/P_t$ 无量纲 ✓, $G_t,G_r$ 无量纲 ✓, $(\lambda/4\pi R)^2$ 无量纲 ✓

### 14.2.2 Link Budget

Complete link budget includes all gains and losses:

$$
P_r = P_t + G_t + G_r - L_{\text{fs}} - L_{\text{atm}} - L_{\text{pol}} - L_{\text{misc}} \quad \text{[dB]}
$$

**Link margin:**

$$
M = P_r - P_{\text{min}} \quad \text{[dB]}
$$

where $P_{\text{min}}$ is the minimum detectable power of the receiver.

### 14.2.3 Receiver Architectures

| Architecture | Pros | Cons |
|---|---|---|
| **Superheterodyne** | High selectivity, good sensitivity | Image frequency, LO leakage |
| **Homodyne (Direct conversion)** | No image, simple | DC offsets, flicker noise |
| **Low-IF** | Balanced tradeoff | Complex filtering |

**Noise figure of a cascaded system (Friis formula):**

$$
F_{\text{total}} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \cdots
$$

Equivalent noise temperature:

$$
T_e = (F - 1) T_0 \quad \text{where} \quad T_0 = 290\;\text{K}
$$

### 14.2.4 Link SNR and BER

For a digital communication link:

$$
\frac{E_b}{N_0} = \frac{P_r}{k T_{\text{sys}} R_b}
$$

where $R_b$ is the bit rate [b/s] and $k = 1.38 \times 10^{-23}\;\text{J/K}$.

**Bit error rate** depends on modulation:

- **BPSK:** $P_e = \frac{1}{2} \text{erfc}\!\left(\sqrt{E_b/N_0}\right)$
- **QPSK:** $P_e \approx \text{erfc}\!\left(\sqrt{E_b/N_0}\right)$ (same as BPSK per bit)
- **M-QAM:** $P_e \approx 4\left(1 - \frac{1}{\sqrt{M}}\right) Q\!\left(\sqrt{\frac{3E_b}{N_0(M-1)}}\right)$

> **Key insight:** To achieve BER $= 10^{-6}$ with BPSK, need $E_b/N_0 \approx 10.5\;\text{dB}$.

---

## 14.3 Radar Systems

### 14.3.1 Radar Equation

For a **monostatic radar** (same antenna for Tx and Rx):

$$
P_r = \frac{P_t G_t}{4\pi R^2} \cdot \sigma \cdot \frac{A_e}{4\pi R^2} = \frac{P_t G^2 \lambda^2 \sigma}{(4\pi)^3 R^4}
$$

where $\sigma$ is the radar cross section (RCS) of the target [m²].

**Maximum detectable range:**

$$
R_{\text{max}} = \left[ \frac{P_t G^2 \lambda^2 \sigma}{(4\pi)^3 P_{\text{r,min}}} \right]^{1/4}
$$

> **量纲检查:** $P_t$ [W], $G^2$ 无量纲, $\lambda^2$ [m²], $\sigma$ [m²], 分母 $(4\pi)^3$ 无量纲, $P_{\text{r,min}}$ [W] ➔ $[R_{\text{max}}] = \text{[m]}^{4/4} = \text{[m]}$ ✓

### 14.3.2 Radar Cross Section (RCS)

$\sigma$ is the equivalent area that intercepts power and scatters it isotropically:

$$
\sigma = \lim_{R\to\infty} 4\pi R^2 \frac{|\mathbf{E}_{\text{scat}}|^2}{|\mathbf{E}_{\text{inc}}|^2}
$$

Typical RCS values:

| Target | $\sigma$ [m²] |
|---|---|
| Bird | 0.01 |
| Person | 1 |
| Fighter jet | 1–5 |
| Stealth aircraft | 0.001–0.1 |
| Ship | $10^4$–$10^6$ |
| Rain drop | $10^{-6}$ |

### 14.3.3 Pulse Radar

For a pulsed radar with pulse width $\tau$ and pulse repetition frequency (PRF) $f_r$:

- **Range resolution:** $\Delta R = c\tau / 2$
- **Unambiguous range:** $R_u = c / (2 f_r)$
- **Average power:** $P_{\text{avg}} = P_t \cdot \tau \cdot f_r$

**Pulse-Doppler radar** uses the Doppler shift to measure target velocity:

$$
f_d = \frac{2v}{\lambda} \cos\theta
$$

where $v$ is the relative velocity and $\theta$ is the angle between velocity vector and radar line-of-sight.

### 14.3.4 Radar Range Equation with Integration

For $N$ pulses integrated:

$$
R_{\text{max}} = \left[ \frac{P_{\text{avg}} G^2 \lambda^2 \sigma N}{(4\pi)^3 k T_{\text{sys}} (E_b/N_0)} \right]^{1/4}
$$

> **Engineering note:** Range scales as $P_t^{1/4}$ — doubling power only increases range by 19%!

---

## 14.4 Radiometer Systems

### 14.4.1 Radiometer Principle

A **radiometer** measures noise power to infer the equivalent blackbody temperature of a scene:

$$
P = k T_B B
$$

where $B$ is the receiver bandwidth.

### 14.4.2 Total Power Radiometer

The simplest radiometer measures the total output power:

$$
T_{\text{out}} = G(T_A + T_{\text{rec}})
$$

**Sensitivity** (minimum detectable temperature):

$$
\Delta T_{\text{min}} = T_{\text{sys}} \left( \frac{1}{B\tau} \right)^{1/2}
$$

where $\tau$ is the integration time.

### 14.4.3 Dicke Radiometer

The Dicke radiometer switches between the antenna and a reference load at frequency $f_s$ to mitigate gain fluctuations:

$$
\Delta T_{\text{min}} = \frac{2 T_{\text{sys}}}{\sqrt{B\tau}}
$$

The factor of 2 (vs. total power) is the penalty for the Dicke switching (only half the time on the signal). However, gain fluctuations are suppressed by the switching technique.

### 14.4.4 NEP and Noise Floor

The **Noise Equivalent Power** (NEP) of a radiometer:

$$
\text{NEP} = k T_{\text{sys}} \sqrt{\frac{2}{B\tau}} \quad \text{[W/√Hz]}
$$

> **Application:** Radiometers are used in remote sensing (soil moisture, atmospheric temperature profiles), radio astronomy, and security screening.

---

## 14.5 Microwave Propagation

### 14.5.1 Atmospheric Effects

**Atmospheric attenuation** at microwave frequencies is dominated by:

- **Oxygen ($O_2$):** 60 GHz resonance band, $\alpha \approx 15\;\text{dB/km}$ at peak
- **Water vapor ($H_2O$):** 22.235 GHz resonance, $\alpha \approx 0.2\;\text{dB/km}$ at peak
- **Rain:** Strong frequency-dependent, $\alpha \propto f^{1.5}$ roughly

Empirical model (ITU-R):

$$
\alpha_{\text{atm}}(f) = \alpha_{O_2}(f) + \alpha_{H_2O}(f) \quad \text{[dB/km]}
$$

### 14.5.2 Rain Attenuation

Specific attenuation due to rain:

$$
\gamma_R = k R^\alpha \quad \text{[dB/km]}
$$

where $R$ is the rain rate [mm/h], and $k, \alpha$ are frequency and polarization-dependent coefficients (ITU-R P.838).

| Frequency | $k_H$ | $k_V$ | $\alpha_H$ | $\alpha_V$ |
|---|---|---|---|---|
| 10 GHz | 0.0101 | 0.00887 | 1.276 | 1.264 |
| 30 GHz | 0.167 | 0.151 | 1.090 | 1.062 |
| 100 GHz | 1.13 | 1.11 | 0.754 | 0.744 |

### 14.5.3 Ground and Multipath Effects

**Two-ray ground reflection model:**

$$
\frac{P_r}{P_t} = G_t G_r \left( \frac{\lambda}{4\pi R} \right)^2 \left| 1 + \Gamma e^{-j\Delta\phi} \right|^2
$$

where $\Gamma$ is the ground reflection coefficient and $\Delta\phi = 2\pi \Delta L / \lambda$ is the phase difference between direct and reflected paths.

At large distances, the two-ray model gives $P_r \propto 1/R^4$ (unlike free-space $1/R^2$).

### 14.5.4 Plasma and Ionospheric Effects

- **Plasma frequency:** $f_p = \sqrt{n_e e^2 / (\pi m_e)} \approx 9\sqrt{n_e}$ [Hz] with $n_e$ in m$^{-3}$
- Below $f_p$, waves are reflected (key to ionospheric propagation below ~30 MHz)
- **Faraday rotation:** Polarization rotation by magnetized plasma
- **Group delay:** $\tau_g \propto 1/f^2$ (dispersive medium)

---

## 14.6 Other Applications

### 14.6.1 Microwave Heating

**Power dissipation density:**

$$
P_d = \frac{1}{2} \sigma |E|^2 + \pi f \epsilon_0 \epsilon_r'' |E|^2 \quad \text{[W/m}^3\text{]}
$$

where $\epsilon_r''$ is the imaginary part of the relative permittivity (loss factor).

**Penetration depth:**

$$
\delta_p = \frac{1}{\alpha} = \frac{1}{\omega} \left[ \frac{\mu\epsilon'}{2} \left( \sqrt{1 + \tan^2\delta} - 1 \right) \right]^{-1/2}
$$

**ISM bands for heating:** 915 MHz, 2.45 GHz, 5.8 GHz, 24.125 GHz.

Water has a large $\epsilon_r''$ at 2.45 GHz → efficient microwave oven operation.

### 14.6.2 Wireless Power Transmission

**Beam efficiency** for a focused microwave beam from a circular aperture of diameter $D$ to a receiving aperture at distance $R$:

$$
\eta_b \approx 1 - e^{-(D_r D_t / \lambda R)^2 / 2}
$$

High efficiency requires $D_t D_r / (\lambda R) \gg 1$ (large apertures, short range, high frequency).

Efficiency limit due to diffraction: $\eta_b < 1 - e^{-\tau^2}$ where $\tau = \sqrt{0.5} \, D_t D_r / (\lambda R)$.

### 14.6.3 Biological Effects and Safety

**Two categories:**
1. **Thermal effects** — tissue heating (dominant above ~1 GHz)
   - Specific Absorption Rate (SAR): $\text{SAR} = \frac{\sigma |E|^2}{2\rho}$ [W/kg]
2. **Non-thermal effects** — disputed, research ongoing

**Safety standards:**
- IEEE C95.1: $10\;\text{W/m}^2$ for general public at 2–300 GHz
- ICNIRP guidelines: similar limits

### 14.6.4 Other Notable Applications

| Application | Frequency | Key Parameter |
|---|---|---|
| GPS/GNSS | L1: 1.575 GHz, L2: 1.227 GHz | $C/N_0$ (carrier-to-noise density) |
| RFID | 860–960 MHz, 2.45 GHz | Backscatter link budget |
| 5G mmWave | 24–40 GHz, 60 GHz | Path loss, beamforming |
| Automotive radar | 24 GHz, 77 GHz | RCS, Doppler resolution |
| Radio astronomy | 0.1–1000+ GHz | $T_{\text{sys}}$, bandwidth, integration time |

---

## Key Formulas Reference

| Formula | Description | Section |
|---|---|---|
| $A_e = \lambda^2 G / (4\pi)$ | Aperture–gain relation | 14.1 |
| $G/T = G_{\text{ant}} / T_{\text{sys}}$ | Rx figure of merit | 14.1 |
| $P_r = P_t G_t G_r (\lambda/4\pi R)^2$ | Friis transmission | 14.2 |
| $F_{\text{total}} = F_1 + \frac{F_2-1}{G_1} + \cdots$ | Cascaded noise figure | 14.2 |
| $R_{\text{max}} = [P_t G^2 \lambda^2 \sigma / ((4\pi)^3 P_{\text{r,min}})]^{1/4}$ | Radar maximum range | 14.3 |
| $\Delta T_{\text{min}} = T_{\text{sys}} / \sqrt{B\tau}$ | Radiometer sensitivity | 14.4 |
| $\gamma_R = kR^\alpha$ | Rain attenuation | 14.5 |
| $P_d = \frac12 \sigma|E|^2 + \pi f\epsilon_0\epsilon_r''|E|^2$ | Microwave heating | 14.6 |
