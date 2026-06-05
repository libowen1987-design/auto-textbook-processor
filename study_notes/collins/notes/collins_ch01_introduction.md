---
title: Chapter 1: Introduction / 第1章：引言
source: Robert E. Collin, Foundations for Microwave Engineering, 2nd Ed., IEEE Press, 2000, Ch. 1 (§1.1–§1.3), pp. 1–16.
---

# Chapter 1: Introduction
# 第1章：引言（Introduction）

**Source:** Robert E. Collin, *Foundations for Microwave Engineering*, 2nd Ed., IEEE Press, 2000, Ch. 1 (§1.1–§1.3), pp. 1–16.

> IEEE Press Classic Reissue, ISBN 0-7803-6031-1

---

## §1.1 Microwave Frequencies
## §1.1 微波频率（Microwave Frequencies）

Collin defines **microwave frequencies** as the range where the wavelength is comparable to the dimensions of circuit elements, requiring distributed-circuit analysis rather than lumped-element models.

> 本节定义了微波频率的范围：当波长与电路元件尺寸相当时，必须采用分布式电路分析，而非集总参数模型。

| Property | Range |
|---|---|
| Wavelength | 1 m to 1 cm |
| Frequency | 300 MHz to 30 GHz |

### Standard Frequency Band Designations (§1.1, Table 1.1)
### 标准频段名称（Standard Frequency Band Designations）

> Collin 采用 IEEE 标准频段命名法，从 VHF（30–300 MHz）到 EHF（40–300 GHz），其中"微波"特指 300 MHz–30 GHz 范围。

| Band | Frequency Range | Wavelength Range |
|------|----------------|------------------|
| VHF | 30–300 MHz | 10–1 m |
| UHF | 300–1000 MHz | 1–0.3 m |
| L | 1–2 GHz | 30–15 cm |
| S | 2–4 GHz | 15–7.5 cm |
| C | 4–8 GHz | 7.5–3.75 cm |
| X | 8–12 GHz | 3.75–2.5 cm |
| Ku | 12–18 GHz | 2.5–1.67 cm |
| K | 18–27 GHz | 1.67–1.11 cm |
| Ka | 27–40 GHz | 1.11–0.75 cm |
| U (EHF) | 40–300 GHz | 7.5–1 mm |

> Note: Collin defines "microwave" as 300 MHz–30 GHz. The mm-wave range (30–300 GHz, EHF) is described separately.

**Physical intuition:** At lower frequencies (say 1 MHz, \lambda \approx 300 m), component dimensions (cm-scale) are << $\lambda$, so lumped circuit theory is valid. At microwave frequencies (e.g., 10 GHz, \lambda \approx 3 cm), component dimensions become comparable to $\lambda$, and wave phenomena (phase shifts, standing waves, radiation) dominate.

> **工程直觉**：低频时元件尺寸远小于波长，集总电路理论有效；微波频段尺寸与波长相当，波现象（相移、驻波、辐射）占主导。

---

## §1.2 Microwave Applications
## §1.2 微波应用（Microwave Applications）

Collin identifies the following major application areas (§1.2, pp. 3–6):

> 微波技术的主要应用领域涵盖雷达、通信、广播、科学、工业、医疗及导航等方面。

### Radar
### 雷达（Radar）

- **First major driver** of microwave technology (WWII)
- Requires high-power pulsed sources (magnetron, klystron)
- Key radar bands: L (long-range surveillance), S (weather), X (fire control), Ku/Ka (high-resolution)

> 雷达是微波技术发展的首要推动力，二战期间由军事需求催生至今仍在演进。

### Communication Systems
### 通信系统（Communication Systems）

- **Point-to-point links:** Terrestrial microwave relay (4–6 GHz, 11 GHz)
- **Satellite communications:** C-band (4/6 GHz), Ku-band (12/14 GHz), Ka-band (20/30 GHz)
- **Mobile/satellite:** L-band (1.5/1.6 GHz for GPS, Iridium)

> 点对点地面中继与卫星通信是微波通信的两大支柱，从C波段到Ka波段覆盖了主要商业与军事频段。

### Broadcasting
### 广播（Broadcasting）

- Satellite TV (Ku-band direct-to-home, ~12 GHz)
- Microwave links for TV distribution

### Scientific & Industrial
### 科学与工业应用（Scientific & Industrial）

- **Remote sensing:** Passive radiometry, synthetic aperture radar (SAR)
- **Radio astronomy:** Observations in protected bands
- **Microwave heating:** Industrial processing, microwave ovens (ISM 2.45 GHz)
- **Medical:** Diathermy, hyperthermia treatment

### Navigation
### 导航（Navigation）

- GPS (L1 = 1.57542 GHz, L2 = 1.2276 GHz)
- Aircraft landing systems

### ISM Bands — Industrial Heating (§1.2)
### ISM频段——工业加热（ISM Bands — Industrial Heating）

Collin notes that for industrial heating applications, the frequencies of **915 MHz** and **2,450 MHz** are commonly allocated (ISM bands).

> ISM（工业、科学、医疗）频段中，915 MHz 和 2450 MHz 是最常用的工业加热频率。

---

## §1.3 Microwave Circuit Elements and Analysis
## §1.3 微波电路元件与分析（Microwave Circuit Elements and Analysis）

This section explains **how microwave engineering differs from lower-frequency circuit design** (§1.3, pp. 6–16).

> 本节阐述微波工程与低频电路设计的根本区别：尺寸与波长可比时，分布式效应不可忽略。

### Key Difference: Distributed vs. Lumped Elements
### 核心差异：分布式元件与集总元件（Distributed vs. Lumped Elements）

At microwave frequencies:

- **Wavelength is short** (\lambda \approx 3 cm at 10 GHz)
- **Circuit dimensions are comparable to $\lambda$**
- **Voltage and current are not uniquely defined** along a conductor — phase varies spatially
- **Transmission line theory** (or full-wave EM field theory) replaces Kirchhoff's voltage/current laws
- **Impedance becomes a complex function of position**

### Transmission Lines (§1.3, Fig. 1.1)
### 传输线（Transmission Lines）

Collin introduces the basic transmission-line concept:
- **Coaxial line:** Inner conductor + outer shield, dominant TEM mode
- **Two-wire line:** Balanced line, used at lower microwave frequencies
- **Waveguide:** Hollow metal pipe (rectangular, circular), TE/TM modes
- **Microstrip:** Planar, widely used in modern MICs (Microwave Integrated Circuits)

Distributed parameters (per-unit-length):
| Parameter | Symbol | Unit | Physical Origin |
|-----------|--------|------|----------------|
| Series resistance | $R$ | Ω/m | Conductor ohmic loss (skin effect) |
| Series inductance | $L$ | H/m | Magnetic flux around conductors |
| Shunt conductance | $G$ | S/m | Dielectric loss in insulation |
| Shunt capacitance | $C$ | F/m | Electric field between conductors |

> 传输线理论是微波工程的基石，同轴线、波导、微带线各有其适用场景与模式特性。

### Waveguides vs. Transmission Lines
### 波导与传输线的比较（Waveguides vs. Transmission Lines）

| Property | Coax/Microstrip | Waveguide |
|----------|----------------|-----------|
| Mode type | TEM (or quasi-TEM) | TE, TM |
| Frequency range | DC–mm-wave | Above cutoff |
| Cutoff frequency | None (DC capable) | Waveguide-specific |
| Q factor | Moderate | High |
| Power handling | Moderate | High (kW–MW) |
| Fabrication | PCB, easy integration | Machined metal |

### Microwave Network Description
### 微波网络描述（Microwave Network Description）

At microwave frequencies, circuits are described by:
- **Scattering parameters (S-parameters):** Power wave relationships, measurable with VNA
- **Impedance/admittance matrices:** Z, Y parameters generalized to distributed networks
- **Smith chart:** Graphical impedance matching tool (§1.3, reference to Ch. 5)

> S参数是微波工程中最实用的测量量，可通过网络分析仪直接获取。

### Common Microwave Components (Overview)
### 常见微波元件概述（Common Microwave Components）

| Component | Function | Operating Principle |
|-----------|----------|-------------------|
| Directional coupler | Sample forward/reflected power | Coupled transmission lines |
| Circulator/Isolator | Nonreciprocal signal flow | Ferrite materials + magnetic bias |
| Power divider | Split/combine power | Wilkinson, hybrid junctions |
| Filter | Frequency selection | Coupled resonators, stubs |
| Attenuator | Controlled power reduction | Resistive film, PIN diode |
| Phase shifter | Controlled phase delay | Varactor, ferrite, switched lines |
| Mixer | Frequency conversion | Nonlinear diode (Schottky) |
| Detector | Power measurement | Diode rectification |

> 无源微波元件构成微波系统的基本功能单元，定向耦合器、环行器、滤波器等各有其独特功能。

### Circuit Theory vs. Field Theory (§1.3, pp. 14–16)
### 电路理论与场论（Circuit Theory vs. Field Theory）

| Aspect | Circuit Theory | Field Theory |
|--------|---------------|--------------|
| Basic variables | V, I | E, H (vector fields) |
| Governing eqns | Kirchhoff's laws | Maxwell's equations |
| Valid when | Dimensions << \lambda | Arbitrary dimensions |
| Element types | Lumped R, L, C | Distributed, waveguide, cavity |
| Analysis tools | Network analysis, S-params | Wave equation, mode matching |
| Examples | Filter design (narrowband) | Waveguide discontinuities, radiation |

Collin emphasizes that microwave engineers must be **equally comfortable with both** approaches. Circuit theory provides design convenience; field theory provides physical accuracy.

> Collin 强调：微波工程师必须同时掌握电路理论与场论——电路理论便于设计，场论提供物理准确性。

### Materials at Microwave Frequencies (§1.3)
### 微波频段的材料特性（Materials at Microwave Frequencies）

Key material properties affecting circuit behavior:
- **Conductor losses:** Skin effect — current concentrates near surface; surface resistivity $R_s = \sqrt{\pi f \mu / \sigma}$ [Ω/□]
- **Dielectric losses:** Loss tangent $\tan \delta$ characterizes energy dissipation in dielectrics
- **Ferrite materials:** Gyromagnetic properties enabling nonreciprocal devices

> 导体趋肤效应和介质损耗正切是决定微波元件性能的关键材料参数。

---

## Summary of Key Equations (Ch. 1)
## 第1章重要公式汇总（Summary of Key Equations）

These are context equations from Ch. 1 (definitions, not derived — derived in Ch. 2 and later):

| Quantity | Expression | Eq. Ref | Units |
|----------|-----------|---------|-------|
| Wavelength | $\lambda = c/f$ | — | m |
| Skin depth | $\delta_s = 1/\sqrt{\pi f \mu \sigma}$ | §1.3 | m |
| Surface resistance | $R_s = 1/(\sigma \delta_s)$ | §1.3 | Ω/□ |
| Propagation constant | $\gamma = \alpha + j\beta$ | Ch. 3 | m⁻¹ |
| Characteristic impedance | $Z_0 = \sqrt{(R+j\omega L)/(G+j\omega C)}$ | Ch. 3 | Ω |

---

## References (from Collin Ch. 1, p. 16)
## 参考文献（References）

1. C. G. Montgomery, R. H. Dicke, and E. M. Purcell, *Principles of Microwave Circuits*, McGraw-Hill, 1948. (MIT Rad. Lab. Ser., Vol. 8)
2. G. L. Ragan, *Microwave Transmission Circuits*, McGraw-Hill, 1948. (MIT Rad. Lab. Ser., Vol. 9)
3. T. Moreno, *Microwave Transmission Design Data*, McGraw-Hill, 1948. (MIT Rad. Lab. Ser., Vol. 11)
4. S. Ramo, J. R. Whinnery, and T. Van Duzer, *Fields and Waves in Communication Electronics*, Wiley, 1965.
5. R. E. Collin, *Field Theory of Guided Waves*, 2nd Ed., IEEE Press, 1991.

---

**End of Ch. 1 notes.** Source: Collin, *Foundations for Microwave Engineering*, 2nd Ed., IEEE Press, 2000, pp. 1–16.
