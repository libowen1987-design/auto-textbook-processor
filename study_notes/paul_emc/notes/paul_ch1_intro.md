# Chapter 1: Introduction to Electromagnetic Compatibility (EMC)

> **Source:** Paul, *Introduction to Electromagnetic Compatibility*, 2nd Ed., Wiley, 2006. Chapter 1.
> **Status:** Fully washed — all formulas LaTeX'd, variables physics-meaningful.

---

## 1.1 The EMC Problem: Source–Path–Receptor

Every electromagnetic compatibility (EMC) problem decomposes into three canonical elements:

```
[Source (Emitter)] → [Coupling Path] → [Receptor (Receiver)]
```

- **Source / Emitter:** Generates electromagnetic energy — intentional (radio transmitter) or unintentional (digital clock, universal motor, spark gap).
- **Coupling Path:** Transfers energy from source to receptor. May be **radiated** (free-space propagation) or **conducted** (direct metallic conduction).
- **Receptor:** Processes the received energy. Interference occurs when the received energy causes the receptor to behave in an undesired manner.

A system is **electromagnetically compatible** with its environment iff it satisfies **all three** of:

1. It does **not cause** interference with other systems. *(Emissions suppressed)*
2. It is **not susceptible** to emissions from other systems. *(Immunity ensured)*
3. It does **not cause** interference with **itself**. *(Internal isolation verified)*

> **工程直觉:** 三个条件缺一不可。消费电子出口各国必须同时满足发射限值和抗扰度要求。

---

### 1.1.1 The Four EMC Subproblems

Any EMC problem can be classified into **four subproblems**, as illustrated in Fig. 1.2:

| Subproblem | Description | Coupling Medium |
|---|---|---|
| **Radiated Emissions (RE)** | Unintended EM energy radiated from product | Free space / air |
| **Radiated Susceptibility (RS)** | Product malfunctions due to external radiated fields | Free space / air |
| **Conducted Emissions (CE)** | Unintended EM energy conducted out on power/signal cables | Metallic conductors |
| **Conducted Susceptibility (CS)** | Product malfunctions due to conducted transients on cables | Metallic conductors |

A typical electronic system consists of multiple subsystems interconnected by cables. These cables, including the AC power cord, are efficient **antennas** — the longer the cable, the more efficient the radiative/receptive coupling. Even the AC power cord (intended for 50/60 Hz) typically carries high-frequency conducted emissions that couple from internal digital circuitry.

**Key principle — "Currents radiate":**
A time-varying current (accelerated charge) is the fundamental mechanism behind all radiated emissions. A 60 Hz power cord carrying 60 Hz current radiates inefficiently, but high-frequency noise currents on that same cable will radiate efficiently because their frequency corresponds to shorter wavelengths.

---

### 1.1.2 Three Strategies for Interference Prevention

When interference occurs, there are exactly three remedial strategies, applied in order of preference:

1. **Suppress emission at the source** *(First line of defense — usually lowest cost)*
   - Slow digital signal rise/fall times (reduces high-frequency spectral content)
   - Suppress arcing in motors (snubber circuits, RF chokes)
2. **Reduce coupling path efficiency** *(Second line of defense)*
   - Shielded enclosures (metal cabinets)
   - Filtering on cables (common-mode chokes, feedthrough capacitors)
   - Proper cable routing and grounding
3. **Reduce receptor susceptibility** *(Last resort — often conflicts with product function)*
   - Error-correcting codes in digital receivers
   - Differential signaling
   - Hysteresis and filtering at receptor input

> **工程直觉:** 永远优先从源头抑制。降-rise time成本最低、效果最广。屏蔽和滤波是" brute force"手段，但会增加成本且安装后性能往往低于理想值。

---

### 1.1.3 Other EMC Concerns

Beyond the four canonical subproblems, EMC engineering addresses:

- **ESD (Electrostatic Discharge):** Walking across carpet can charge the body to > 10 kV. Touching a keyboard causes an arc that transfers charge directly and radiates an EM wave. ESD can destroy ICs and cause system malfunction.
- **EMP (Electromagnetic Pulse):** Nuclear detonations create intense EM fields (from charge separation/movement) that destroy semiconductor devices. Military hardening against EMP is a radiated susceptibility problem.
- **Lightning:** ~50,000 A current pulses in the lightning channel. Coupling occurs via direct radiation and conduction through the AC power distribution system. Products must be tested for surge immunity on AC mains.
- **TEMPEST:** Intercepting unintentional EM emissions from electronic equipment (e.g., monitoring emissions from typewriters to reconstruct typed text). Critical for military and corporate espionage prevention.

---

## 1.2 History of EMC

EMC as a discipline evolved alongside the proliferation of electronic systems:

| Era | Milestone | EMC Impact |
|---|---|---|
| Late 1800s | Marconi's spark-gap transatlantic transmission | First recognition that spark gaps cause EMI |
| ~1920 | Technical papers on radio interference appear | Self-oscillations, crude antennas |
| ~1930 | Electric motors, railroads, signs create major EMI | First broad EMI problem |
| WWII | Radios, navigation, radar on aircraft | Frequency reassignment, cable routing |
| 1950s | Bipolar transistor invented | Increased density, more EMI sources |
| 1960s | Integrated circuit (IC) invented | Denser noise-rich digital systems |
| 1970s | Microprocessor chip invented | Explosion of switching waveforms |
| 1979 | **FCC Rule (U.S.)** — first digital device emission limits | Made EMC compliance legally mandatory |
| 1980s+ | Clock speeds reach GHz; rise times < 1 ns | EMC becomes critical design constraint |

**CISPR (International Special Committee on Radio Interference)** was formed in 1933 (IEC, Paris). It published measurement techniques and recommended emission limits; European countries adopted these earlier than the U.S.

**MIL-STD-461** (U.S. military) imposed emission and susceptibility limits from the early 1960s — well before commercial FCC rules. Military additionally imposed **susceptibility requirements** (intentionally injecting interfering signals to verify the equipment functions properly).

> **工程直觉:** 1979年FCC规则是EMC学科的历史转折点。此后EMC设计从"自愿最佳实践"变为"产品上市的法定前提"。

---

## 1.3 Illustrative EMC Case Studies

| Case | Root Cause | Coupling Path | Solution |
|---|---|---|---|
| TV picture rolls when blender runs | Universal motor arcing (L di/dt) generates broadband noise | Conducted via AC power cord → household power distribution → TV antenna | EMI filter on motor, snubber |
| Office copier causes hallway clocks to reset | SCR firing in power conditioning chops AC abruptly | Conducted via AC power net to synchronized clock circuit | Filtering, improved grounding |
| Car stalls near illegal FM transmitter | FM signal couples to ECU wiring | Radiated → wiring harness → processor shutdown | Shielding, TVS diodes |
| CB keying locks truck brakes | CB transmit signal couples to electronic brake circuit | Conducted into brake control wiring | Shielding |
| Computer room malfunctions near airport radar | Surveillance radar pulse illuminates office | Radiated → computer room shielding insufficient | Shielded enclosure |
| HMS Sheffield destroyed by Exocet (1982) | Ship's radio ↔ antimissile system mutual interference; antimissile disabled during comms | System-level EMI; self-interference | System-level EMC design |
| U.S. Army Black Hawk crashes (1988+) | Electronically controlled flight system susceptible to radar/radio/CB emissions | Radiated coupling to flight control wiring | Hardening, shielding |
| USS Forrestal fire (1967) | High-power search radar induced RF voltages on shielded connector contacts → inadvertent missile deployment | Conducted via shield/connector → weapons system | Improved shielding practices |

> **工程直觉:** 从日常烦恼(电视雪花)到生死攸关(军舰被击沉)，EMI的后果跨越10个数量级。系统性EMC设计是唯一出路。

---

## 1.4 Electrical Dimensions and Wave Behavior

This is the **most critical conceptual foundation** in EMC. Physical dimensions are irrelevant; **electrical dimensions** (in wavelengths) determine radiative behavior.

### 1.4.1 Wavelength and Wave Propagation

A sinusoidal wave in free space propagates at the speed of light:

$$
v_0 = \frac{1}{\sqrt{\varepsilon_0 \mu_0}} \approx 3 \times 10^8 \text{ m/s}
$$

The wavelength $\lambda$ is the distance a wave travels to change phase by $2\pi$ radians (360°):

$$
\lambda = \frac{v}{f} \quad \text{[m]}
$$

For free space: $\lambda_0 = c/f \approx 300/f_{\text{MHz}}$ meters.

A propagating sinusoidal current (phasor form):

$$
i(z,t) = I \cos(\omega t - \beta z) \quad \text{where } \beta = \frac{2\pi}{\lambda} \text{ rad/m}
$$

The **phase shift** across a structure of length $L$ is:

$$
\phi = \beta L = \frac{2\pi L}{\lambda} \quad \text{[radians]}
$$

**Phase shift examples:**

| $L$ relative to $\lambda$ | Phase shift |
|---|---|
| $L = \lambda$ | $360^\circ$ (2π rad) — current returns to in-phase |
| $L = \lambda/2$ | $180^\circ$ — current is completely out of phase |
| $L = \lambda/10$ | $36^\circ$ — usually negligible for lumped modeling |
| $L = \lambda/20$ | $18^\circ$ — often acceptable |
| $L = \lambda/100$ | $3.6^\circ$ — negligible in most contexts |

**Key rule:** A circuit is **electrically small** when its largest dimension $L_{\max} < \lambda/10$. Only then are **lumped-circuit models** (Kirchhoff's laws) valid. If $L_{\max} > \lambda/10$, Maxwell's equations (or transmission-line theory) must be used.

### 1.4.2 Representative Wavelengths in Free Space

| Frequency | Wavelength | Typical Use |
|---|---|---|
| 60 Hz | 3107 miles (5000 km) | Power distribution |
| 3 MHz | 100 m | Shortwave radio |
| 30 MHz | 10 m | FM radio, VHF |
| 300 MHz | 1 m | UHF, TV (Ch 14–83) |
| 3 GHz | 10 cm | Microwave ovens, WiFi |
| 30 GHz | 1 cm | Radar, EHF |

### 1.4.3 Wavelength in Dielectrics

For a nonmagnetic medium ($\mu_r = 1$) with relative permittivity $\varepsilon_r$:

$$
v = \frac{c}{\sqrt{\varepsilon_r}} = c \cdot \frac{1}{\sqrt{\varepsilon_r}}, \quad \lambda = \frac{\lambda_0}{\sqrt{\varepsilon_r}}
$$

| Dielectric | $\varepsilon_r$ | $v/c$ | $\lambda$ at 1 GHz |
|---|---|---|---|
| Air | 1.0005 | ~1.0 | 30 cm |
| Teflon | 2.1 | 0.69 | 20.7 cm |
| FR-4 (PCB substrate) | 4.7 | 0.46 | 13.8 cm |
| PVC | 3.5 | 0.53 | 16.1 cm |
| Silicon | 12.0 | 0.29 | 8.7 cm |

### 1.4.4 Propagation Delay in Digital Systems

Time delay for a wave to transit a connection of length $L$:

$$
T_D = \frac{L}{v} \quad \text{[s]}
$$

For free space: $L = 1 \text{ m} \Rightarrow T_D \approx 3.33 \text{ ns}$.

For FR-4 PCB ($v \approx 1.8 \times 10^8$ m/s): $L = 6 \text{ in} = 0.152 \text{ m} \Rightarrow T_D \approx 850 \text{ ps}$.

**Modern relevance:** In the mid-1980s, clock speeds ~10 MHz (rise/fall times ~20 ns). Propagation delays (~ns) were negligible compared to gate delays. By the 2000s, clock speeds reached 3 GHz with rise/fall times of 100–500 ps. On-chip and PCB interconnects now have propagation delays comparable to signal transition times — **interconnect delay** has become the dominant signal integrity issue.

### 1.4.5 Electrical Size Calculation

The electrical size of a structure in wavelengths:

$$
k = \frac{L}{\lambda}
$$

A structure is **electrically small** if $k < 0.1$; it is **electrically large** if $k > 0.1$.

**Example:** A 3.6 m vertical conductor at 86 MHz in air:
$$
\lambda_0 = \frac{300}{86} = 3.49 \text{ m} \Rightarrow k = \frac{3.6}{3.49} = 1.03 \quad (\text{electrically large!})
$$

In PVC ($\varepsilon_r = 3.5$, $\lambda = 3.49/\sqrt{3.5} = 1.865$ m):
$$
k = \frac{3.6}{1.865} = 1.93 \quad (\text{even larger})
$$

> **工程直觉:** 一根看似"小"的3.6米导体在86 MHz时已是超过1个波长！城市基站和调频广播天线周围的净空区设计必须用波长的电气尺寸来判断。

---

## 1.5 Decibels and Common EMC Units

EMC quantities span enormous dynamic ranges (e.g., electric fields: $1 \text{ mV/m}$ to $200 \text{ V/m}$ — eight orders of magnitude). Decibels (dB) compress this range. One dB is one-tenth of a Bel.

### 1.5.1 Definition of dB for Power, Voltage, and Current

$$
\text{Power ratio (dB)} \equiv 10 \log_{10}\!\left(\frac{P_2}{P_1}\right)
$$

$$
\text{Voltage ratio (dB)} \equiv 20 \log_{10}\!\left(\frac{V_2}{V_1}\right)
$$

$$
\text{Current ratio (dB)} \equiv 20 \log_{10}\!\left(\frac{I_2}{I_1}\right)
$$

**Why the factor of 20 for voltage/current?** Because $P \propto V^2/R$, so $10\log_{10}(P_2/P_1) = 10\log_{10}(V_2^2/V_1^2) = 20\log_{10}(V_2/V_1)$ when $R$ cancels (or when comparing voltages across the same impedance).

### 1.5.2 Absolute dB Units (Referenced)

Decibels are inherently ratios. Absolute levels are obtained by referencing to a standard:

| Unit | Definition | Reference |
|---|---|---|
| **dBmV** | $20 \log_{10}(V / 1 \text{ mV})$ | 1 mV |
| **dBμV** | $20 \log_{10}(V / 1 \text{ μV})$ | 1 μV |
| **dBmA** | $20 \log_{10}(I / 1 \text{ mA})$ | 1 mA |
| **dBμA** | $20 \log_{10}(I / 1 \text{ μA})$ | 1 μA |
| **dBmW** (dBm) | $10 \log_{10}(P / 1 \text{ mW})$ | 1 mW |
| **dBW** | $10 \log_{10}(P / 1 \text{ W})$ | 1 W |
| **dBμV/m** | $20 \log_{10}(E / 1 \text{ μV/m})$ | 1 μV/m |
| **dBmV/m** | $20 \log_{10}(E / 1 \text{ mV/m})$ | 1 mV/m |

**Conversions from dB to absolute:**

$$
V = 10^{\text{dBμV}/20} \times 10^{-6} \quad \text{[V]}
$$

$$
V = 10^{\text{dBmV}/20} \times 10^{-3} \quad \text{[V]}
$$

$$
P = 10^{\text{dBmW}/10} \times 10^{-3} \quad \text{[W]}
$$

**Key conversions to memorize:**

| Ratio | Voltage/Current (dB) | Power (dB) |
|---|---|---|
| $\times 10^6$ | 120 | 60 |
| $\times 10^3$ | 60 | 30 |
| $\times 10^2$ | 40 | 20 |
| $\times 10$ | 20 | 10 |
| $\times 3$ | 9.54 | 4.77 |
| $\times 2$ | 6.02 | 3.01 |
| $\times 1$ | 0 | 0 |
| $\div 10$ | $-20$ | $-10$ |
| $\div 2$ | $-6.02$ | $-3.01$ |

**Mental math trick:** Decompose numbers into products of 2, 3, and powers of 10:
- $25 \approx 3 \times 2 \times 2 \times 2 \Rightarrow 20\log_{10}(25) \approx 10 + 6 + 6 + 6 = 28$ dB (exact: 27.96 dB)

### 1.5.3 Addition of Gains in dB

One of the most useful properties: **gains add in dB** (rather than multiply in linear units).

For cascaded amplifier stages or cascaded systems:

$$
P_{\text{out, dB}} = G_1 + G_2 + G_3 + \cdots + P_{\text{in, dB}}
$$

$$
V_{\text{out, dBμV}} = G_{\text{dB}} + V_{\text{in, dBμV}} \quad \text{(same impedance)}
$$

**Example:** A 60 dB gain amplifier fed with $-30$ dBm signal:
$$
P_{\text{out}} = 60 + (-30) = 30 \text{ dBm} \quad \Rightarrow \quad 1 \text{ W}
$$

**FCC Class B limit for radiated electric field at 3 m:** 100 μV/m = $40$ dBμV/m.

> **工程直觉:** 记住 6 dB ≈ 2×(电压/电流)，3 dB ≈ 2×(功率)。这样在评估EMI测试超标量级时，可以快速心算需要多少dB的衰减。

### 1.5.4 Cable Loss and Transmission Lines

For a **matched** transmission line (load $Z_L = Z_C$), the power delivered to the load is:

$$
P_{\text{out}} = P_{\text{in}} \cdot e^{-2\alpha L}
$$

The cable loss in dB (manufacturer specification):

$$
\text{Cable loss}_{\text{dB}} = 10 \log_{10}\!\left(\frac{P_{\text{in}}}{P_{\text{out}}}\right) = 8.686 \, \alpha L \quad \text{[dB]}
$$

where $\alpha$ is the attenuation constant (Np/m) and $L$ is the cable length.

**Example:** RG58U coaxial cable at 100 MHz: loss = 4.5 dB/100 ft.
$$
\alpha = \frac{4.5}{8.686 \times 100} = 5.18 \times 10^{-3} \text{ Np/ft}
$$

**Critical note:** Cable loss specifications **assume the cable is matched** ($Z_L = Z_C$). If mismatched, the specification does not apply directly — reflected waves increase the power delivered to the load (or reduce it) in a frequency-dependent manner.

### 1.5.5 Signal Source Specification (Thevenin Equivalent)

A signal source is characterized by its **Thevenin equivalent**: open-circuit voltage $\hat{V}_{OC}$ and source impedance $\hat{Z}_S = R_S + jX_S$. For EMC, source impedance characteristics determine how efficiently emissions couple to the victim circuit.

---

## 1.6 Summary: Key Takeaways for EMC Engineering

1. **Every EMI problem = Source + Path + Receptor.** Eliminating any one breaks the interference chain.
2. **Lumped-circuit models (Kirchhoff) are valid only for electrically small structures** ($L < \lambda/10$). Above that, wave effects (transmission-line theory / Maxwell) dominate.
3. **Rise/fall time of digital pulses is the primary determinant of high-frequency spectral content.** Slower transitions = lower emission frequencies = easier to suppress.
4. **Cables are antennas.** Both the AC power cord and interconnect cables efficiently radiate and receive unwanted EM energy.
5. **Decibels are the universal language of EMC.** Logarithmic compression enables convenient arithmetic (addition/subtraction instead of multiplication/division).
6. **Regulatory compliance is mandatory.** FCC (U.S.), CISPR (international), MIL-STD-461 (military) — no product can be sold without meeting applicable EMC limits.
7. **EMC is not optional:** An brilliantly designed product that cannot be legally sold is worthless.

---

*End of Chapter 1 — Paul, Introduction to Electromagnetic Compatibility, 2nd Ed.*
