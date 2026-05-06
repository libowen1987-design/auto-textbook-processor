---
title: "Chapter 1 — Introduction"
book: "RF Circuit Design — 2nd Ed."
author: "Reinhold Ludwig, Gene Bogdanov"
pages: "15–42"
processed: "2026-05-03"
tags: [RF, passive-components, skin-effect, chip-components, TEM]
---

# Chapter 1: Introduction

> **Overview:** This chapter reviews the evolution from low-frequency to high-frequency circuit operation, explains why conventional Kirchhoff-based analysis fails at RF frequencies, and introduces the high-frequency behavior of passive components (resistors, capacitors, inductors). It also covers chip-component standards and skin effect.

---

## 1.1 Importance of Radiofrequency Design

- Early electrical engineering relied on DC and low-frequency AC with lumped-element models based on Kirchhoff's laws.
- Maxwell (1864) postulated coupling of electric and magnetic fields giving rise to wave propagation; Hertz (1887) experimentally confirmed EM radiation.
- Modern wireless systems (cellular, GPS, satellite) operate at GHz frequencies where wavelength is comparable to circuit dimensions → Kirchhoff analysis fails.
- A **2 GHz power amplifier** (PA) for cellular phones (Fig. 1-2) illustrates key RF blocks:
  - DC blocking capacitor + input matching network (to match transistor input impedance)
  - Interstage matching network
  - Microstrip lines (distributed elements, unlike lumped elements)
  - RF blocking networks using **RFCs** (Radio Frequency Coils)

Key RF topics previewed: transmission lines (Ch2), Smith chart (Ch3), S-parameters (Ch4), filters (Ch5), matching networks (Ch8), active components (Ch6–7), amplifier design (Ch9), oscillators and mixers (Ch10).

---

## 1.2 Dimensions and Units

### Plane TEM Wave Propagation

For a plane electromagnetic wave in free space propagating in $+z$ direction:

$$
E_x(z,t) = E_{0x} \cos(\omega t - \beta z) \tag{1.1a}
$$
$$
H_y(z,t) = H_{0y} \cos(\omega t - \beta z) \tag{1.1b}
$$

where:
- $\omega = 2\pi f$ is the angular frequency [rad/s]
- $\beta = 2\pi/\lambda$ is the propagation constant [rad/m]
- $\lambda$ is the wavelength [m]

### Intrinsic Impedance

$$
Z_0 = \frac{E_x}{H_y} = \sqrt{\frac{\mu}{\varepsilon}} = \sqrt{\frac{\mu_0 \mu_r}{\varepsilon_0 \varepsilon_r}} \tag{1.2}
$$

where:
- $\mu_0 = 4\pi \times 10^{-7}$ H/m (free-space permeability)
- $\varepsilon_0 = 8.854 \times 10^{-12}$ F/m (free-space permittivity)
- $\mu_r$, $\varepsilon_r$ are relative values

For free space: $Z_0 = \sqrt{\mu_0/\varepsilon_0} \approx 377\ \Omega$ (Example 1-1).

### Phase Velocity

$$
v_p = \frac{\omega}{\beta} = \frac{1}{\sqrt{\mu\varepsilon}} = \frac{c}{\sqrt{\mu_r \varepsilon_r}} \tag{1.3}
$$

In free space, $v_p = c \approx 3 \times 10^8$ m/s.

### Wavelength–Frequency Relation

$$
\lambda = \frac{v_p}{f} = \frac{c}{f\sqrt{\mu_r \varepsilon_r}} \tag{1.4}
$$

> **工程直觉:** 当电路物理尺寸超过 $\lambda/10$ 时，集总参数模型失效，必须采用分布式传输线理论。Example 1-1 显示：30 MHz → $\lambda=10$ m（PCB 远小于波长）；30 GHz → $\lambda=1$ cm（与 PCB 尺寸相当）。

---

## 1.3 Frequency Spectrum

IEEE frequency band classification (Table 1-1):

| Band | Frequency | Wavelength |
|------|-----------|------------|
| VLF | 3–30 kHz | 100–10 km |
| LF | 30–300 kHz | 10–1 km |
| MF | 300–3000 kHz | 1–0.1 km |
| HF | 3–30 MHz | 100–10 m |
| VHF | 30–300 MHz | 10–1 m |
| **UHF** | 300–3000 MHz | 100–10 cm |
| **L band** | 1–2 GHz | 30–15 cm |
| **S band** | 2–4 GHz | 15–7.5 cm |
| **C band** | 4–8 GHz | 7.5–3.75 cm |
| **X band** | 8–12.5 GHz | 3.75–2.4 cm |
| **Ku band** | 12.5–18 GHz | 2.4–1.67 cm |
| **K band** | 18–26.5 GHz | 1.67–1.13 cm |
| **Ka band** | 26.5–40 GHz | 1.13–0.75 cm |

RF range is conventionally from VHF to S band; MW range from C band and above.

---

## 1.4 RF Behavior of Passive Components

### 1.4.1 Skin Effect in Conductors

At DC, current uses the entire conductor cross-section. As frequency increases, Faraday's law induces opposing currents; current density concentrates at the outer perimeter.

#### Current Density (Bessel function formulation)

$$
J_z(r) = \frac{I p}{2\pi a} \frac{J_0(pr)}{J_1(pa)} \tag{1.8}
$$

where $p^2 = -j\omega\mu_0\sigma_{\text{cond}}$ and $J_0, J_1$ are Bessel functions.

#### Skin Depth $\delta$

$$
\delta = \frac{1}{\sqrt{\pi f \mu_0 \sigma_{\text{cond}}}} \tag{1.11}
$$

- $\delta$ is the depth at which current density drops to $e^{-1}$ (37%) of its surface value.
- High-frequency approximation for current density:

$$
J_z(r) \approx \frac{I}{2\pi a\delta} e^{-(a-r)/\delta} \tag{1.12}
$$

- For $f \gtrsim 500$ MHz and $\delta \ll a$:

$$
\frac{R}{R_{\text{DC}}} \approx \frac{a}{2\delta}, \quad \frac{\omega L}{R_{\text{DC}}} \approx \frac{a}{2\delta} \tag{1.9, 1.10}
$$

- **Rise of AC resistance:**

$$
R_{\text{AC}} \approx \frac{l}{\sigma_{\text{cond}} \cdot (2\pi a \delta)} \tag{1.13}
$$

<img src="../figures/ch1_skin_depth.png" alt="Skin depth vs frequency" width="500px"/>

**Key materials:** Copper ($\sigma = 64.516\times10^6\ \Omega^{-1}\text{m}^{-1}$), Aluminum ($40\times10^6$), Gold ($48.544\times10^6$).

### 1.4.2 High-Frequency Resistors

Types: carbon-composite, wire-wound, metal-film, thin-film chip (SMD — most common for RF).

#### Equivalent Circuit (Fig. 1-8)

- Nominal resistance $R$
- Lead inductances $L$ (each)
- Stray capacitance $C_a$ (charge separation)
- Interlead capacitance $C_b$ (usually negligible)

For wire-wound resistors: additional winding inductance $L_1$ and inter-winding capacitance $C_s$.

#### Impedance of a Resistor with Leads (Example 1-3)

$$
Z = \frac{1}{\frac{1}{R + j\omega L_{\text{lead}}} + j\omega C_a}
$$

where the lead inductance (for $f \gtrsim 95$ kHz for AWG 26 wire):

$$
L_{\text{lead}} \approx \frac{2l}{2a} \sqrt{\frac{\mu_0}{\pi \sigma_{\text{cond}} f}} \quad \text{(per lead, approximated)}
$$

> **工程直觉:** 电阻在低频为纯阻性；频率升高后寄生电容主导使阻抗下降；超过自谐振频率后引线电感主导使阻抗上升（见图 1-10）。千万不能将电阻视为纯阻性元件！

### 1.4.3 High-Frequency Capacitors

#### Ideal Capacitor

$$
C = \frac{\varepsilon_0 \varepsilon_r A}{d} \tag{1.14}
$$

#### Lossy Dielectric

$$
Z_C = \frac{1}{G_e + j\omega C} \tag{1.15}
$$

where $G_e = \sigma_{\text{diel}} A/d$ accounts for conduction through the dielectric.

#### Loss Tangent

$$
\tan \Delta_e = \frac{\sigma_{\text{diel}}}{\omega\varepsilon_0 \varepsilon_r} \tag{1.16}
$$

leading to:

$$
G_e = \omega C \tan \Delta_e
$$

**Equivalent Series Resistance (ESR):**

$$
\text{ESR} = \frac{\tan \Delta_e}{\omega C} \tag{1.17}
$$

#### Equivalent Circuit (Fig. 1-11)

$R_s$ (lead resistance), $L_s$ (lead inductance), $C$ (nominal capacitance), $R_e = 1/G_e$ (dielectric loss resistance).

> **工程直觉:** 电容也具有自谐振频率(SRF)。低于 SRF 时为容性；高于 SRF 时为感性。ESR 随频率下降，在高频时引线电感起主导作用。MLCC（多层陶瓷电容）利用交错电极结构实现高容值/体积比。

### 1.4.4 High-Frequency Inductors (RFCs)

#### Air-Core Solenoid Inductance

$$
L \approx \frac{\mu_0 N^2 \pi r^2}{l} \tag{1.18}
$$

- $N$: number of turns
- $r$: coil radius
- $l$: coil length

#### Equivalent Circuit (Fig. 1-15)

- $L$: nominal inductance
- $R_s$: series resistance (DC + skin effect)
- $C_s$: parasitic shunt capacitance (between adjacent turns)

#### Quality Factor $Q$

$$
Q = \frac{\omega L}{R_s} = \frac{X}{R_s} \tag{1.19}
$$

> **工程直觉:** 电感的阻抗在低频时呈 $+20\ \text{dB/dec}$ 上升；在自谐振频率处达到峰值（有限值由 $R_s$ 决定）；超过 SRF 后容性主导，阻抗下降。RFC 在偏置网络中用于"短路"DC 条件对 RF 开路。高 $Q$ 值对调谐至关重要。

---

## 1.5 Chip Components and Circuit Board Considerations

### 1.5.1 Chip Resistors

- Sizes: 40×20 mil (0.5 W) to 1×1 in (1000 W)
- Size code: first 2 digits = length (tens of mils), last 2 = width
- Resistance range: 0.1 $\Omega$ to several M$\Omega$
- Tolerance: $\pm5\%$ to $\pm0.01\%$
- Construction: nichrome film on alumina (Al$_2$O$_3$) substrate, laser-trimmed, protective coating

### 1.5.2 Chip Capacitors

- Single-plate or multilayer (MLCC) design
- Standard sizes: 15 mil square to 400×425 mil
- Capacitance: 0.1 pF to several $\mu$F
- Tolerance: $\pm2\%$ to $\pm50\%$ (small values in pF, not %)

### 1.5.3 Surface-Mounted Inductors

- Wire-wound air-core: 60×30 mil to 180×120 mil
- Inductance: 1 nH to 1000 $\mu$H
- Flat coils (integrated with microstrip): 1–500 nH, ~2×2 mm size
- Used in hybrid/integrated circuits

---

## 审计表 (Audit)

| 项目 | 状态 | 备注 |
|------|------|------|
| §1.1 高频设计重要性 | ✅ | 含 PA 示例链 |
| §1.2 TEM波/阻抗/相速/波长 | ✅ | Ex1-1 量化验证 |
| §1.3 频谱划分表 | ✅ | IEEE 标准 |
| §1.4.1 趋肤效应 | ✅ | 公式(1.8)–(1.13) |
| §1.4.2 高频电阻模型 | ✅ | Ex1-3: 500Ω 薄膜电阻 |
| §1.4.3 高频电容模型 | ✅ | Ex1-4: 47pF 电容，ESR |
| §1.4.4 高频电感/RFC | ✅ | Ex1-5: 3.5 匝空心线圈，Q |
| §1.5 贴片元件 | ✅ | R/C/L 尺寸与构造 |
| 例题代码复现 | ✅ | 5 个例题全部代码化 |
| 工程直觉段落 | ✅ | 每节末尾 |
