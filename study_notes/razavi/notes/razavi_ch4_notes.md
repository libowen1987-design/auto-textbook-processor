---
chapter: 4
title: Transceiver Architectures
source: Behzad Razavi, RF Microelectronics, 2nd Edition, McGraw-Hill, 2012
pages: 155-250
---

# Chapter 4: Transceiver Architectures
# 第四章：收发机架构

> *"The choice of transceiver architecture determines the overall RF performance, integration level, and cost. This chapter compares heterodyne, direct-conversion, and image-reject architectures."*
>
> **（中文）** 收发机架构的选择直接决定了系统的噪声系数、线性度、镜像抑制能力、功耗和集成度。本章系统比较超外差（heterodyne）、直接转换（direct-conversion）和镜像抑制（image-reject）三大类收发机架构，分析各自的优缺点及设计挑战。

---

## 4.1 General Considerations | 一般性考量

### Receiver Performance Parameters | 接收机性能参数

The essential RX figures of merit:

| Parameter | Symbol | Typical Value (GSM RX) | Unit |
|---|---|---|---|
| Sensitivity | $P_{\text{min}}$ | $-110$ | dBm |
| Noise Figure | NF | $9-12$ | dB |
| Input-referred IP3 | IIP3 | $-10$ to $-5$ | dBm |
| 1-dB Compression | $P_{\text{1dB}}$ | $-20$ to $-15$ | dBm |
| Image rejection | IR | $> 60$ | dB |
| LO-RF isolation | — | $> 80$ | dB |

### The Core Trade-off: Sensitivity vs. Linearity | 核心权衡：灵敏度与线性度

A fundamental tension in RX design:

- **High sensitivity** → High gain + Low NF LNA → High linearity requirement for subsequent stages
- **High linearity** (for strong interferers) → Lower gain or more complex circuits

> **（中文）** 接收机的核心矛盾：前端需要高增益（以放大微弱信号至基带处理水平），但高增益会放大干扰信号，使后续混频器和滤波器承受更大的非线性压力。此外，强阻塞信号（strong blockers）会在LNA产生互调产物，降低有用信号的信噪比。

### Blocker (Interferer) Specification | 阻塞信号规格

GSM specifications mandate that the receiver tolerate interferers far exceeding the wanted signal:

| Blocker | Offset | Power Level |
|---|---|---|
| Wanted signal | — | $-104\ \text{dBm}$ |
| EGSM900 uplink blocker | $0.8-1.6\ \text{MHz}$ | $-49\ \text{dBm}$ |
| EGSM900 uplink blocker | $>1.6\ \text{MHz}$ | $-43\ \text{dBm}$ |
| Out-of-band blocker | $< 1\ \text{MHz}$ | $0\ \text{dBm}$ |

> **（中文）** GSM规范要求接收机在存在强大阻塞信号（比有用信号强$50-60\ \text{dB}$以上）时仍能正常工作。这是接收机架构设计的核心驱动：架构必须能够抑制这些强干扰，防止它们在接收机内产生互调失真（IMD）而"淹没"有用信号。

---

## 4.2 Receiver Architectures | 接收机架构

### 4.2.1 Basic Heterodyne Receivers | 基本超外差接收机

The **heterodyne** (literally "mixing with another frequency") architecture downconverts the RF signal to an **intermediate frequency (IF)** before demodulation.

#### Classical Heterodyne | 经典超外差

```
Antenna → BPF (preselection) → LNA → Mixer (×LO) → IF BPF (channel select) → Detector
```

**Frequency Plan:**

$$
f_{\text{IF}} = |f_{\text{RF}} - f_{\text{LO}}| \quad \text{(4.1)}
$$

**Image Frequency Problem:**

$$
f_{\text{image}} = f_{\text{LO}} \pm f_{\text{IF}} = f_{\text{RF}} \pm 2f_{\text{IF}} \quad \text{(4.2)}
$$

Any signal at $f_{\text{image}}$ will also downconvert to $f_{\text{IF}}$, creating **image interference**.

> **（中文）** 超外差架构的核心问题：镜像频率。每个RF信号都有两个频率（$f_{\text{RF}}$和$f_{\text{image}} = f_{\text{RF}} \pm 2f_{\text{IF}}$）经过混频后都会落在中频$f_{\text{IF}}$上。如果不抑制镜像信号，它将与有用信号在输出端混叠，无法分离。

#### Image Rejection Ratio (IRR) | 镜像抑制比

The IRR quantifies how well the receiver suppresses the image:

$$
\text{IRR} = \frac{P_{\text{RF}}}{P_{\text{image}}} \quad \text{(linear)} \quad \text{or} \quad \text{IRR}[\text{dB}] = 10\log\frac{P_{\text{RF}}}{P_{\text{image}}} \quad \text{(4.3)}
$$

A high-$Q$ **image-reject filter** (SAW or ceramic) before the mixer is essential:

$$
\text{Required IRR} \approx \text{SNR}_{\text{required}} + \text{NF} + 10\log_{10}B \quad \text{(4.4)}
$$

For GSM: IRR $\approx 60\ \text{dB}$ (cannot be achieved with on-chip filters).

> **（中文）** GSM要求镜像抑制比（IRR）达到约$60\ \text{dB}$，这远超过典型片上滤波器的抑制度。因此GSM接收机必须在片外使用高$Q$的SAW（声表面波）或陶瓷滤波器来抑制镜像频率。这是超外差架构在移动终端中难以全集成的根本原因之一。

#### Dual-Conversion Heterodyne | 二次变频超外差

To relax filter requirements, two mixing stages are used:

```
RF → [SAW filter] → LNA → Mixer1 (→ IF1) → [IF filter] → Mixer2 (→ IF2) → Baseband
```

| Parameter | Single Conversion | Double Conversion |
|---|---|---|
| Image problem | One critical image | Two images (both manageable) |
| Filter $Q$ required | Very high | Moderate |
| Complexity | Lower | Higher |
| LO generation | One VCO | Two VCOs / PLLs |

> **（中文）** 双中频超外差通过两级下变频，降低了对各级滤波器$Q$值的要求。第一中频（IF1）较高以实现良好的镜像抑制和邻道选择；第二中频（IF2）较低以实现窄的信道选择和良好的基带解调。GSM接收机常采用这种架构。

#### Heterodyne Receiver with Zero Second IF | 零第二中频的超外差

Modern heterodyne receivers often use:

$$
f_{\text{IF1}} \gg f_{\text{IF2}} = 0 \quad \text{(zero-IF on second stage)}
$$

**Advantage**: Second IF = 0 simplifies channel selection to baseband lowpass filtering.

**Challenge**: DC offsets and low-frequency干扰 (flicker noise, LO leakage) become severe.

> **（中文）** 零第二中频（zero-second-IF）是超外差与直接转换的混合体：第一级下变频至高中频以抑制镜像，第二级下变频至零中频以简化基带信道选择。这一架构在WCDMA接收机中得到广泛应用。

### 4.2.2 Modern Heterodyne Receivers | 现代超外差接收机

#### WCDMA Receiver Example | WCDMA接收机实例

Modern cellular receivers (WCDMA/LTE) employ heterodyne with carefully planned frequency plans:

**WCDMA Band I (TX: 1920-1980 MHz, RX: 2110-2170 MHz)**:

- First LO: $f_{\text{LO}} = f_{\text{RF}} - f_{\text{IF1}}$ with $f_{\text{IF1}} \approx 190\ \text{MHz}$
- Image frequency: $f_{\text{image}} = f_{\text{RF}} - 2f_{\text{IF1}}$ falls in the TX band → must be filtered
- Second conversion: $f_{\text{IF2}} = 0$ (direct to baseband)

> **（中文）** WCDMA接收机的典型频率规划：第一中频约$190\ \text{MHz}$，使用SAW滤波器抑制镜像；第二中频为零（zero-IF），基带通过低通滤波器进行信道选择。关键挑战是处理TX-RX隔离（发射信号泄漏到接收天线）和由此产生的TX自混频。

#### SAW-Less Receivers | 无SAW接收机

A major research direction: eliminating the off-chip SAW filter (expensive, not integratable).

**SAW-less Approaches:**
1. **High-IF architecture**: Increase $f_{\text{IF}}$ so that the image falls outside the TX band
2. **Multi-tap feedforward cancellation**: On-chip DSP cancels the TX leakage
3. **Spatial isolation**: Good antenna TX-RX isolation (depends on FDD duplexer)

> **（中文）** 片上集成是射频收发机的终极目标，但SAW滤波器（用于镜像抑制和邻道选择）目前无法用标准CMOS实现。SAW-less接收机通过提高中频（$f_{\text{IF}}$）使镜像落在TX频段之外，从而减少对SAW的依赖。这需要在片上实现更严格的线性度和镜像抑制。

### 4.2.3 Direct-Conversion Receivers | 直接转换接收机

#### Concept | 概念

Direct-conversion (also called **zero-IF** or **homodyne**) architecture downconverts the RF signal directly to baseband in one step:

$$
f_{\text{IF}} = 0 \Rightarrow f_{\text{LO}} = f_{\text{RF}} \quad \text{(4.5)}
$$

**Advantage**: No image problem (image = RF itself), eliminating the need for off-chip image-reject filters.

> **（中文）** 直接转换（零中频）架构将射频信号一步下变频到基带（$f_{\text{IF}} = 0$），本振频率等于载波频率（$f_{\text{LO}} = f_{\text{RF}}$）。最大的优势是：镜像频率等于信号频率本身，因此不存在镜像干扰问题，理论上可以省去SAW滤波器，实现全集成的射频接收机。

#### Block Diagram | 框图

```
Antenna → BPF → LNA → Quadrature Mixer (×I, ×Q LO) → Lowpass Filter → ADC
                                        ↑
                                    VCO (f_LO = f_RF)
```

The quadrature downconversion produces I and Q baseband signals:

$$
I(t) = \text{LPF}\{s_{\text{RF}}(t)\cos\omega_c t\} \quad \text{(4.6)}
$$
$$
Q(t) = \text{LPF}\{s_{\text{RF}}(t)\sin\omega_c t\} \quad \text{(4.7)}
$$

> **（中文）** 直接转换接收机需要正交混频（I/Q两路），因为单端下变频到零中频会丢失信号的相位信息（$f_{\text{IF}} = 0$时无法区分正负频率）。I/Q双路分别与$\cos\omega_c t$和$\sin\omega_c t$混频后低通滤波，恢复基带I/Q信号。

#### Key Challenges of Direct Conversion | 直接转换的关键挑战

##### (a) DC Offset | 直流偏置

**Sources of DC offset:**
1. **LO leakage**: LO signal couples to LNA input through substrate, package, or PCB traces. This self-mixes at the mixer, producing a DC component.
2. **Self-mixing of large blockers**: A strong interferer at $f_{\text{LO}} \pm f_m$ can self-mix to DC.
3. **Even-order nonlinearity**: Second-order nonlinearity ($\alpha_2$) in LNA/mixer rectifies large signals to DC.

DC offsets can be as large as **tens of mV** at the baseband output, swamping the wanted signal (typical signal level: $\mu\text{V}$ range).

> **（中文）** 直流偏置（DC offset）是直接转换接收机的最大挑战之一。LO泄漏信号通过祼片、封装或PCB耦合到天线端口，再反射回来进入接收机，与LO自混频产生直流偏置。此外，强阻塞信号经过二阶非线性也会产生直流偏置。典型GSM接收机的基带信号只有几十$\mu\text{V}$，而直流偏置可能高达几十$\text{mV}$——完全淹没有用信号！

**Solution — AC Coupling / HPF:**

Insert a highpass filter (HPF) or AC coupling capacitor at baseband:

$$
H_{\text{HPF}}(s) = \frac{s}{s + \omega_c} \quad \text{(4.8)}
$$

However, HPF also attenuates low-frequency components of the wanted signal (GMSK has energy near DC).

##### (b) Flicker Noise (1/f Noise) | 闪烁噪声

The baseband amplifiers (after mixer) have $1/f$ noise that directly adds to the wanted signal. The corner frequency $f_c$ of MOSFET $1/f$ noise can be **hundreds of kHz** in standard CMOS — much higher than the channel bandwidth.

> **（中文）** 闪烁噪声（$1/f$噪声）在低频段功率谱密度很高，会直接叠加在基带信号上。对于$200\ \text{kHz}$带宽的GSM信道，MOSFET的$1/f$噪声角频率可能达到$100\ \text{kHz}$，这意味着很大一部分信道能量会被闪烁噪声"污染"。解决方案：使用大尺寸器件（降低$1/f$角频率）、采用相关双采样（CDS）、或使用特殊工艺（SOS, SOI）。

##### (c) I/Q Mismatch | I/Q失配

Quadrature downconversion requires perfectly orthogonal I and Q carriers with equal amplitudes:

$$
\text{I/Q amplitude mismatch} = \frac{|I| - |Q|}{|I|} \quad \text{(4.9)}
$$
$$
\text{I/Q phase error} = |\phi_I - \phi_Q - 90^\circ| \quad \text{(4.10)}
$$

Typical tolerances: amplitude mismatch $< 1\ \text{dB}$, phase error $< 3^\circ$ (for QPSK).

**Effect on EVM (Error Vector Magnitude):**

$$
\text{EVM} \approx \sqrt{(\Delta A/2)^2 + (\Delta\phi \cdot \pi/360)^2} \quad \text{(4.11)}
$$

> **（中文）** I/Q失配会破坏星座图的正交性，导致解调误差。幅度失配（典型$< 1\ \text{dB}$）和相位失配（典型$< 3^\circ$）都会产生EVM误差。在高阶QAM（64/256-QAM）系统中，I/Q失配要求更加严格。片上振荡器的I/Q失配通常可以控制在可接受范围内（因为振荡器的I/Q通常是差分输出，固有正交性）。

##### (d) Even-Order Distortion (IP2) | 偶阶失真（IP2）

Second-order nonlinearity ($\alpha_2$) in LNA or mixer creates:

$$
y(t) \supset \alpha_2 [A\cos(\omega_1 t)]^2 = \frac{\alpha_2 A^2}{2}[1 + \cos 2\omega_1 t]
$$

The **DC term** ($\alpha_2 A^2/2$) is the problematic component for direct-conversion RX.

The **IIP2** (input-referred second-order intercept point):

$$
IIP2[\text{dBm}] = P_{\text{in}} + \frac{P_{\text{DC}}}{2} \quad \text{(4.12)}
$$

where $P_{\text{DC}}$ is the DC offset power referred to the input.

Required IIP2 for GSM: $> +60\ \text{dBm}$ (very demanding).

> **（中文）** 二阶非线性失真（IP2）在直接转换接收机中特别关键，因为它的二次谐波会产生直流偏置（$2\omega_1$可能在某些阻塞信号下混频到直流）。GSM要求IIP2达到约$+60\ \text{dBm}$——远高于IIP3（典型$-10\ \text{dBm}$），是直接转换接收机的重大设计挑战。

### 4.2.4 Image-Reject Receivers | 镜像抑制接收机

Image-reject architectures attempt to eliminate the off-chip image-reject filter by processing the I/Q signals differently.

#### Hartley Architecture |  Hartley架构

```
RF → 90° hybrid → [Mixer × LO] → [LPF] ──────→ Subtractor → Baseband
                         ↓
                    90° phase shift (LO)
```

**Principle**: The image signal is phase-shifted such that it cancels at the output, while the wanted signal adds constructively.

**Image Rejection Ratio (Theoretical):**

$$
\text{IRR}_{\text{Hartley}} \approx \frac{1 + \cot(\Delta\phi/2)}{1 - \cot(\Delta\phi/2)} \quad \text{(4.13)}
$$

For $\Delta\phi = 90^\circ$ (perfect quadrature): $\text{IRR} \rightarrow \infty$.

In practice, phase/gain errors limit IRR to $20-40\ \text{dB}$.

> **（中文）** Hartley架构利用$90^\circ$相位网络和相减运算来抑制镜像信号。理想情况下，镜像完全被抑制（IRR $\rightarrow \infty$）。但实际系统中，$90^\circ$相位分裂器的误差和I/Q增益失配限制了IRR，实际只能达到$20-40\ \text{dB}$，远不如SAW滤波器（可达$60\ \text{dB}$以上）。

#### Weaver Architecture | Weaver架构

Weaver replaces the $90^\circ$ RF hybrid with a second mixing stage:

```
RF → Mixer1 (×LO1) → LPF → Mixer2 (×LO2, 0° and 90°) → Combiner
                                          ↓
                                    90° phase shift (LO2)
```

**Advantage**: Phase accuracy is determined by LO2 frequency (easier to generate precise quadrature at lower frequencies).

**Limitation**: Requires two LO synthesizers and careful matching.

> **（中文）** Weaver架构用第二级混频替代$90^\circ$ RF混合器，移至第二本振（通常工作在较低频率）进行$90^\circ$相移，从而获得更精确的正交性。但Weaver架构需要两个锁相环（PLL）来产生两个本振频率，增加了复杂度和成本。

### 4.2.5 Low-IF Receivers | 低中频接收机

Low-IF architecture is a compromise between direct-conversion and heterodyne:

$$
0 < f_{\text{IF}} \ll f_{\text{RF}} \quad \text{(4.14)}
$$

Typical $f_{\text{IF}} = 100\ \text{kHz} - 10\ \text{MHz}$.

**Advantages:**
1. No DC offset problem (IF $\neq 0$, so image is not DC)
2. No $1/f$ noise problem (baseband bandwidth $B \gg f_{\text{IF}}$)
3. No need for off-chip SAW filter (image can be filtered on-chip if $f_{\text{IF}}$ is well chosen)

**Challenges:**
1. Image is still present (but falls in an unused band)
2. I/Q mismatch still matters (for image rejection)
3. ADC sampling at lower frequencies requires anti-aliasing

> **（中文）** 低中频架构是直接转换的改进方案：中频$f_{\text{IF}}$选择足够低（如几$\text{MHz}$），使得$1/f$噪声和直流偏置问题大幅缓解（因为基带低通滤波可以抑制低频噪声），同时镜像频率不在有用频段内，因此可以在片上实现信道选择。但低中频架构仍存在镜像抑制问题，需要在电路层面采取措施。

---

## 4.3 Transmitter Architectures | 发射机架构

### 4.3.1 General Considerations | 一般性考量

#### TX Key Parameters | 发射机关键参数

| Parameter | GSM Requirement | Notes |
|---|---|---|
| Output power range | $+33\ \text{dBm}$ to $5\ \text{dBm}$ | $28\ \text{dB}$ dynamic range |
| Modulation accuracy (EVM) | $< 8\%$ (RMS) | GMSK constellation error |
| Adjacent channel power (ACP) | $< -60\ \text{dBc}$ @ $200\ \text{kHz}$ | Spectral regrowth |
| TX noise floor | $< -115\ \text{dBm/Hz}$ | In RX band (自干扰) |
| harmonics | $> 30\ \text{dBc}$ at $2f_c, 3f_c$ | Antenna filter required |

### 4.3.2 Direct-Conversion Transmitters | 直接转换发射机

The TX is the "reverse" of the direct-conversion RX:

```
Baseband I/Q → DAC → LPFilter → [Upconverter: ×I·cosωt - Q·sinωt] → PA → Antenna
```

**Key Challenge — LO Leakage:**

LO leakage from the upconverter mixer to the PA input can radiate from the antenna, creating out-of-band emissions.

**TX LO Leakage Suppression:**

$$
\text{Required suppression} > 50\ \text{dBc} \quad \text{(4.15)}
$$

> **（中文）** 直接转换发射机的核心挑战：LO泄漏。混频器中的LO端口信号可能泄漏到输出端，通过PA和天线辐射出去，在发射频段之外产生杂散辐射。GSM要求LO泄漏抑制超过$50\ \text{dBc}$（即泄漏功率比有用信号低$50\ \text{dB}$以上）。

#### Carrier Feedthrough | 载波馈通

Due to LO self-mixing and DC offsets in the I/Q modulators, a DC offset in the baseband I/Q signals produces a carrier at the output (even when no modulation is present).

**Suppression methods:**
- AC coupling baseband (but corrupts GMSK low-frequency content)
- Calibration: measure DC offset and subtract digitally
- Chopper stabilization

> **（中文）** 载波馈通（carrier feedthrough）是直接转换发射机的另一挑战：由于I/Q调制器的直流偏置，即使没有调制信号，输出端也会出现一个载波分量。GMSK的频谱在直流附近有能量（由于GMSK的连续相位特性），无法用简单的交流耦合消除。校准和斩波稳定是常用的解决方案。

### 4.3.3 Modern Direct-Conversion Transmitters | 现代直接转换发射机

#### Polar Modulation | 极化调制

Polar modulation separates the amplitude and phase paths:

$$
s(t) = A(t) \cdot e^{j\phi(t)} \quad \text{(4.16)}
$$

**Amplitude path**: $A(t)$ → power amplifier with envelope tracking (ET) or average power tracking
**Phase path**: $\phi(t)$ → phase modulator (direct carrier modulation)

**Challenge**: Time delay mismatch between amplitude and phase paths (must be $< 1^\circ$ of symbol period).

> **（中文）** 极化调制（Polar modulation）将射频信号表示为幅度$A(t)$和相位$\phi(t)$的极坐标形式，分别通过幅度路径和相位路径发送。幅度路径需要功放工作在包络跟踪（ET）或平均功率跟踪（APT）模式，以跟踪调制信号的包络变化。LTE和WCDMA的包络跟踪功放是这一架构的应用实例。

### 4.3.4 Heterodyne Transmitters | 超外差发射机

Analogous to heterodyne receivers, but in reverse:

```
Baseband → Upconverter (×LO1) → IF → Upconverter (×LO2) → RF PA → Antenna
```

**Advantages**: 
- Well-proven, excellent spectral purity
- Image and spurious products can be filtered at IF

**Disadvantages**:
- Requires two synthesizers (cost, complexity)
- Multiple upconversion stages amplify LO leakage and spurious emissions

### 4.3.5 Other TX Architectures | 其他发射机架构

**Two-Step Transmitter**: Upconvert twice (IF → RF), filtering between stages. Common in microwave radios.

**Loop-Through Transmitter**: RX and TX share the LO synthesizer to reduce cost and complexity (used in FDD systems like WCDMA).

---

## 4.4OOK Transceivers | 开关键控收发机

On-Off Keying (OOK) is the simplest digital modulation: carrier is present for "1", absent for "0".

Common in: RFID (Radio-Frequency Identification), keyless entry, remote controls.

**RX Architecture — Energy Detection:**

$$
P_{\text{detected}} = \int_{0}^{T_b} |r(t)|^2 dt \begin{array}{c} > \gamma \Rightarrow "1" \\ < \gamma \Rightarrow "0" \end{array} \quad \text{(4.17)}
$$

where $\gamma$ is the detection threshold.

> **（中文）** OOK是成本最低的收发机架构：发射机仅需一个简单的开关（开=载波，关=无载波）；接收机仅需一个包络检波器（能量检测）来判决比特。RFID标签（无源反向散射）是这一架构的典型应用，标签无需发射机，仅通过调制天线阻抗来反向散射读写器的载波。

---

## Key Takeaways | 本章要点

1. **Heterodyne** offers excellent selectivity and image rejection but requires off-chip SAW/BAW filters (integration challenge).
2. **Direct-conversion** enables fully-integrated RF but suffers from DC offset, $1/f$ noise, I/Q mismatch, and IIP2 requirements.
3. **Image-reject** (Hartley/Weaver) architectures eliminate SAW filters but limited IRR ($20-40\ \text{dB}$) due to I/Q mismatches.
4. **Low-IF** is a practical compromise: avoids DC offset and $1/f$ noise, but image rejection is still required.
5. **TX architectures**: Direct-conversion TX faces LO leakage and carrier feedthrough; polar modulation enables efficient wideband PA.
6. **The SAW-less RX challenge**: Achieving $60+\ \text{dB}$ IRR on-chip is an active research area.
7. **Trade-offs dominate**: Every architecture is a set of compromises — no single architecture is optimal for all standards.
