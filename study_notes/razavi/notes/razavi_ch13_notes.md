---
chapter: 13
title: Transceiver Design Example
source: Behzad Razavi, RF Microelectronics, 2nd Edition, McGraw-Hill, 2012
pages: 833-886
---

# Chapter 13: Transceiver Design Example
# 第十三章：收发机设计实例

> *"This chapter brings together all the building blocks studied in previous chapters — LNA, mixer, VCO, PLL, PA — into a complete 900-MHz/1.9-GHz WCDMA transceiver design."*
>
> **（中文）** 本章将前几章研究的各模块——LNA、混频器、VCO、PLL、PA——整合为一个完整的$900\ \text{MHz}/1.9\ \text{GHz}$ WCDMA收发机设计实例，展示系统级设计与电路级设计之间的协同优化。

---

## 13.1 System-Level Considerations | 系统级考量

### 13.1.1 Receiver | 接收机

#### WCDMA Receiver Specifications | WCDMA接收机规格

| Parameter | Specification | Notes |
|---|---|---|
| Frequency bands | Band I (TX: 1920-1980 MHz, RX: 2110-2170 MHz) | FDD |
| RX sensitivity | $-117\ \text{dBm}$ (BER $< 10^{-3}$) | — |
| NF | $< 9\ \text{dB}$ | — |
| IIP3 | $> -18\ \text{dBm}$ | Out-of-band blockers |
| Max input power | $-25\ \text{dBm}$ (in-band blocker) | $–40\ \text{dBm}$ (out-of-band) |
| Image rejection | $> 60\ \text{dB}$ | Requires SAW or image-reject arch. |
| AGC range | $> 80\ \text{dB}$ | From sensitivity to max input |

**AGC (Automatic Gain Control)**: The receiver must handle signals from $-117\ \text{dBm}$ (sensitivity) to $-25\ \text{dBm}$ (strongest blocker) — a dynamic range of $> 90\ \text{dB}$. This is achieved by variable-gain amplifiers (VGAs) and programmable gain stages.

> **（中文）** WCDMA接收机的动态范围要求极高：从灵敏度$-117\ \text{dBm}$到最大输入$-25\ \text{dBm}$，需要超过$90\ \text{dB}$的自动增益控制（AGC）。这通过可变增益放大器（VGA）和可编程增益级实现。LNA提供固定增益（约$20\ \text{dB}$），后续的VGA提供$60-70\ \text{dB}$的动态范围。

#### Receiver Architecture Choice | 接收机架构选择

**Option 1 — Heterodyne (High-IF)**:
- $f_{\text{IF}} \approx 190\ \text{MHz}$ (in the TX band gap)
- Excellent image rejection with off-chip SAW
- Requires dual-conversion: RF → IF1 → zero-IF

**Option 2 — Direct Conversion**:
- No image problem
- Suffers from DC offset and $1/f$ noise
- $f_{\text{LO}} = f_{\text{RF}}$ (simplifies LO synthesis)

**Selected: Heterodyne with zero second IF** for its superior linearity and image rejection in FDD WCDMA.

> **（中文）** WCDMA接收机采用高中频+零第二中频的超外差架构：第一中频约$190\ \text{MHz}$（落在TX频段间隙内），提供良好的镜像抑制；第二次变频至零中频（zero-IF），简化基带信道选择。这种架构在WCDMA FDD系统中是性能和复杂度的最佳折中。

### 13.1.2 Transmitter | 发射机

#### WCDMA TX Specifications | WCDMA发射机规格

| Parameter | Specification |
|---|---|
| Output power range | $+24\ \text{dBm}$ to $-50\ \text{dBm}$ |
| ACLR (adjacent channel leakage ratio) | $< -33\ \text{dBc}$ @ $5\ \text{MHz}$ |
| EVM | $< 12.5\%$ RMS |
| TX noise in RX band | $< -115\ \text{dBm/Hz}$ |

**ACLR (Adjacent Channel Leakage Ratio)**:

$$
\text{ACLR} = \frac{P_{\text{adjacent channel}}}{P_{\text{transmit channel}}} \quad \text{(13.1)}
$$

WCDMA ACLR requirement of $-33\ \text{dBc}$ is extremely stringent.

> **（中文）** WCDMA发射机的ACLR（邻道泄漏比）要求$< -33\ \text{dBc}$（$5\ \text{MHz}$偏移），这要求PA具有极高的线性度。由于WCDMA是宽带调制（$3.84\ \text{Mchips/s}$），其PAPR约$3-5\ \text{dB}$，PA必须工作在输出回退约$5-7\ \text{dB}$的状态才能满足ACLR要求。

### 13.1.3 Frequency Synthesizer | 频率合成器

**TX LO**: Direct modulation using two-point injection (for GMSK or direct WCDMA modulation).

**RX LO**: Integer-$N$ PLL with $f_{\text{ref}} = 200\ \text{kHz}$ (channel spacing).

**Frequency planning for FDD**: TX and RX operate simultaneously (full duplex) → require excellent TX-RX isolation (duplexer insertion loss $> 45\ \text{dB}$).

> **（中文）** FDD（频分双工）系统的TX和RX同时工作（而不是TDD的时分双工），这要求双工器（duplexer）在TX和RX频段之间提供超过$45\ \text{dB}$的隔离。TX信号泄漏到RX端会在接收机前端产生强阻塞（self-jamming），对LNA的线性度要求极高。

### 13.1.4 Frequency Planning | 频率规划

**WCDMA Band I (FDD)**:

| Parameter | Value |
|---|---|
| TX frequency | $1920-1980\ \text{MHz}$ |
| RX frequency | $2110-2170\ \text{MHz}$ |
| TX-RX spacing | $190\ \text{MHz}$ |
| Channel bandwidth | $5\ \text{MHz}$ |
| Chip rate | $3.84\ \text{Mchips/s}$ |

**LO frequency plan**:
- RX: $f_{\text{LO}} = f_{\text{RF}} - 190\ \text{MHz}$ (first LO), second LO to zero-IF
- TX: Direct upconversion from baseband to RF

---

## 13.2 Receiver Design | 接收机设计

### 13.2.1 LNA Design | LNA设计

**Specifications:**
- $f_0 = 2.14\ \text{GHz}$ (center of RX band)
- $G > 15\ \text{dB}$
- $\text{NF} < 2\ \text{dB}$
- IIP3 $> -5\ \text{dBm}$ (after mixer contribution)

**Selected topology**: Cascode CS stage with inductive source degeneration.

**Design procedure:**

1. **Choose $g_m$ for minimum NF**:
   For $R_S = 50\ \Omega$, $\gamma = 2/3$: $g_m R_S \approx 0.82$ → $g_m \approx 16.4\ \text{mS}$.

2. **Choose $L_S$ for input matching**:
   $\omega_T L_S = R_S = 50\ \Omega$ → $L_S = 50/\omega_T$.
   For $f_T = 50\ \text{GHz}$: $L_S \approx 0.16\ \text{nH}$.

3. **Check $f_{\text{SR}}$ of $L_S$**:
   For $L_S = 0.16\ \text{nH}$, $C_{\text{gs}} \approx 200\ \text{fF}$:
   $f_{\text{SR}} = 1/(2\pi\sqrt{LC}) \approx 900\ \text{GHz}$ (well above $f_0$).

> **（中文）** LNA设计的核心是在噪声、增益和线性度之间取得平衡。电感源简并（inductive degeneration）提供了自然的$50\ \Omega$输入阻抗匹配，且不引入额外的热噪声。电感值$L_S \approx 0.16\ \text{nH}$（在$50\ \text{GHz}$$f_T$的CMOS工艺中）在版图上实现需要精细的布局。

### 13.2.2 Mixer Design | 混频器设计

**Selected topology**: Active Gilbert cell mixer with $g_m$-boosted input stage.

**Conversion gain**: $G_c = \frac{2}{\pi} g_m R_D \approx 6\ \text{dB}$.

**Noise**: $\text{NF}_{\text{mixer}} \approx 12-15\ \text{dB}$ (referred to input).

**Linearity**: With $g_m = 10\ \text{mS}$, $IIP3 \approx -5\ \text{dBm}$.

### 13.2.3 AGC | 自动增益控制

The AGC loop adjusts the receiver gain to maintain a constant signal level at the ADC input:

**AGC loop dynamics**:

```
RSSI (signal strength) → Comparator → Gain Control Word → VGA
                       ↑
              Desired level
```

**RSSI (Received Signal Strength Indicator)**: Measures the total received power, generating an error signal for gain adjustment.

**Programmable gain steps**: $1\ \text{dB}$ steps over $80\ \text{dB}$ range.

> **（中文）** AGC通过检测接收信号强度（RSSI）与参考电平的差值，动态调节可变增益放大器（VGA）的增益，将ADC输入维持在恒定电平。WCDMA的$80\ \text{dB}$ AGC范围通过LNA（固定增益）+ VGA（可变增益$\sim 40\ \text{dB}$）+ PGA（可编程增益$\sim 40\ \text{dB}$）的级联实现。

---

## 13.3 TX Design | 发射机设计

### 13.3.1 PA Design | 功率放大器设计

**Requirements for WCDMA PA**:

| Parameter | Value |
|---|---|
| $P_{\text{out,max}}$ | $+24\ \text{dBm}$ |
| ACLR @ $5\ \text{MHz}$ | $< -33\ \text{dBc}$ |
| EVM | $< 12.5\%$ |
| PAE at $P_{\text{out,max}}$ | $> 35\%$ |

**Selected topology**: Two-stage PA:
- Driver stage: Class AB, $P_{\text{out}} \approx +15\ \text{dBm}$
- Output stage: Class AB, $P_{\text{out}} \approx +24\ \text{dBm}$

**Load-pull analysis**: The optimum load impedance $Z_L$ for maximum output power is determined by load-pull contours on the Smith chart.

**Matching network**: $\pi$-match from PA output ($Z_L \approx 5-10\ \Omega$) to $50\ \Omega$ antenna:

$$
Z_L = \frac{R_L}{1 + j Q_{\pi}(1 - R_L/R_S)} \quad \text{(13.2)}
$$

> **（中文）** WCDMA PA的负载阻抗通常为$5-10\ \Omega$（远低于$50\ \Omega$），需要用$\pi$型或L型匹配网络将其变换为$50\ \Omega$天线阻抗。$\pi$型网络的高$Q$特性允许在窄带内实现良好的匹配和阻抗变换，但会引入插入损耗（$L_{\text{ins}} \approx 0.5-1\ \text{dB}$），降低PA效率。

**Doherty configuration** for efficiency enhancement at $6\ \text{dB}$ backoff:

Main (carrier) PA: Class AB, biased for efficiency at $P_{\text{out}} = +18\ \text{dBm}$.
Auxiliary (peaking) PA: Class C, turns on at $P_{\text{out}} > +18\ \text{dBm}$.

### 13.3.2 Upconverter | 上变频混频器

**Direct upconversion TX architecture**:

```
I(t), Q(t) → [DAC] → [LPF] → [I/Q Modulator] → [PA] → Antenna
                                    ↑
                               LO (f_c)
```

**I/Q modulator requirements**:
- Carrier feedthrough: $< -40\ \text{dBc}$
- Sideband suppression: $> 40\ \text{dB}$
- LO-RF isolation: $> 50\ \text{dB}$

**Calibration**: On-chip DACs calibrate DC offsets and I/Q gain/phase mismatches.

---

## 13.4 Synthesizer Design | 合成器设计

### 13.4.1 VCO Design | VCO设计

**Requirements for WCDMA synthesizer**:

| Parameter | Value |
|---|---|
| Frequency range | $2110-2170\ \text{MHz}$ (RX LO) |
| Tuning range | $\sim 3\%$ |
| Phase noise @ $1\ \text{MHz}$ | $< -122\ \text{dBc/Hz}$ |
| $K_{\text{VCO}}$ | $< 50\ \text{MHz/V}$ |

**Selected topology**: LC VCO with NMOS cross-coupled pair, PMOS current source, switched capacitor bank.

**Inductor design**: $L \approx 2-4\ \text{nH}$, $Q \approx 15$ at $2\ \text{GHz}$.

**Varactor**: AMOS varactor, $C_{\max}/C_{\min} \approx 2:1$, tuning range $\sim 5\%$.

### 13.4.2 Divider Design | 分频器设计

**Injection-locked frequency divider (ILFD)**: The VCO frequency is divided by $2$ or $4$ using an ILFD, which has much lower power consumption than a static divider at high frequencies.

**$$\divisionsymbol$$-Modulus Divider Chain**:

$$
f_{\text{ref}} = 3.84\ \text{MHz} \times 4 = 15.36\ \text{MHz}
$$

Reference frequency must be a multiple of the chip rate for direct modulation.

### 13.4.3 Loop Design | 环路设计

**Integer-$N$ synthesizer parameters** (for WCDMA at $2.14\ \text{GHz}$):

| Parameter | Value |
|---|---|
| $N$ | $2140\ \text{MHz} / 3.84\ \text{MHz} \approx 557$ |
| $f_{\text{ref}}$ | $15.36\ \text{MHz}$ |
| $\omega_n$ | $2\pi \times 200\ \text{krad/s}$ |
| $\zeta$ | $0.7$ |
| Settling time | $< 100\ \mu\text{s}$ |

---

## Key Takeaways | 本章要点

1. **System-level trade-offs dominate**: LNA gain vs. linearity, PA efficiency vs. linearity, synthesizer settling time vs. phase noise.
2. **WCDMA FDD challenges**: Full-duplex operation requires $> 45\ \text{dB}$ TX-RX isolation via duplexer; TX leakage to RX demands high IIP3 LNA.
3. **AGC dynamic range**: $> 90\ \text{dB}$ AGC range needed to handle sensitivity to max input.
4. **Doherty PA** is standard for WCDMA/LTE basestation to maintain efficiency at $6\ \text{dB}$ backoff.
5. **I/Q calibration** in TX is essential for carrier feedthrough $< -40\ \text{dBc}$.
6. **Integer-$N$ with high $f_{\text{ref}}$** ($15.36\ \text{MHz}$) enables fast settling ($< 100\ \mu\text{s}$) for WCDMA.
7. **Load-pull** is essential for PA design — the optimum load for power and efficiency differs from that for linearity.
