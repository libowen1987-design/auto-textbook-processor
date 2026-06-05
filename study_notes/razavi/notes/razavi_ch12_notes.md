---
chapter: 12
title: Power Amplifiers
source: Behzad Razavi, RF Microelectronics, 2nd Edition, McGraw-Hill, 2012
pages: 751-830
---

# Chapter 12: Power Amplifiers
# 第十二章：功率放大器

> *"The power amplifier is the most power-hungry block in any transmitter, often dissipating $30-60\%$ of the total TX power budget. Its efficiency directly determines battery life and thermal design."*
>
> **（中文）** 功率放大器（PA）是发射机中功耗最大的模块，通常占发射机总功耗的$30-60\%$。PA效率直接影响电池续航和热设计。PA的设计需要在效率、线性度、输出功率和增益之间做出复杂的权衡。

---

## 12.1 General Considerations | 一般性考量

### PA Figures of Merit | PA性能指标

| Parameter | Symbol | Typical Value | Notes |
|---|---|---|---|
| Output power | $P_{\text{out}}$ | $+33\ \text{dBm}$ (GSM max) | W |
| Power-added efficiency | PAE | $30-60\%$ | $(P_{\text{out}} - P_{\text{in}})/P_{\text{DC}}$ |
| Drain efficiency | $\eta$ | $40-70\%$ | $P_{\text{out}}/P_{\text{DC}}$ |
| Linear output power | $P_{1\text{dB}}$ | $+30\ \text{dBm}$ | $1\ \text{dB}$ gain compression |
| Output $P_1$dB | $OP_{1\text{dB}}$ | $+35\ \text{dBm}$ | At PA output |
| Gain | $G$ | $10-20$ | dB |
| Adjacent channel power ratio | ACPR | $< -30\ \text{dBc}$ | For digital modulation |

**Power-Added Efficiency (PAE):**

$$
\text{PAE} = \frac{P_{\text{out}} - P_{\text{in}}}{P_{\text{DC}}} = \frac{P_{\text{out}} - P_{\text{out}}/G}{P_{\text{DC}}} = \eta\left(1 - \frac{1}{G}\right) \quad \text{(12.1)}
$$

> **（中文）** 功率附加效率（PAE）是PA最重要的指标，它考虑了驱动级的功耗。与漏极效率$\eta = P_{\text{out}}/P_{\text{DC}}$不同，PAE考虑了输入信号功率和驱动级的功耗。对于高增益PA，PAE接近漏极效率。

### 12.1.1 Effect of High Currents | 大电流的影响

At high output power, the PA transistor conducts very large currents (amps for mobile PA):

**Current density $J$ limits:**

$$
J_{\max} \approx \frac{I_{\max}}{W \cdot t_{\text{ox}}} \quad \text{(12.2)}
$$

For reliable operation, $J < 1\ \text{mA}/\mu\text{m}$ in standard CMOS.

**Metal electromigration**: Current density $> 5 \times 10^5\ \text{A/cm}^2$ causes metal migration and failure.

> **（中文）** PA在最大输出功率时流经数安培电流。金属电迁移（electromigration）是限制最大电流的关键可靠性问题：电流密度超过$5 \times 10^5\ \text{A/cm}^2$时，金属原子会沿电子流方向迁移，导致开路或短路。版图设计必须使用宽金属线（或多根细线并联）来降低电流密度。

### 12.1.2 Efficiency | 效率

**Definition**: $\eta = P_{\text{out}}/P_{\text{DC}}$ (drain efficiency).

**PAE**: $(P_{\text{out}} - P_{\text{driver}})/P_{\text{DC}}$.

The fundamental efficiency limit for a sinusoidal signal:

$$
\eta_{\max} = \frac{\pi}{4} \cdot \frac{V_{\text{out}}}{V_{\text{DC}}} = \frac{\pi}{4} \cdot \frac{V_{\text{pp}}}{2V_{\text{DC}}} \quad \text{(12.3)}
$$

> **（中文）** PA效率的根本限制是：输出信号的峰值电压受电源电压$V_{\text{DD}}$和晶体管的饱和电压$V_{\text{sat}}$限制。对于正弦波，最大效率为$\pi/4 \approx 78.5\%$（Class B），这是所有PA效率的理论上限。

### 12.1.3 Linearity | 线性度

PA linearity is critical for digitally modulated signals with high PAPR:

**Peak-to-Average Power Ratio (PAPR):**

$$
\text{PAPR} = \frac{P_{\text{peak}}}{P_{\text{avg}}} \quad \text{(12.4)}
$$

| Modulation | PAPR (dB) |
|---|---|
| QPSK | $3-4$ |
| 16-QAM | $4-6$ |
| 64-QAM | $5-8$ |
| OFDM (LTE/WiFi) | $7-12$ |

> **（中文）** OFDM信号（如LTE、WiFi）的PAPR高达$7-12\ \text{dB}$，意味着PA必须能输出比平均功率高$7-12\ \text{dB}$的峰值功率，同时保持线性工作。这导致PA必须工作在很大的输出回退（output backoff）状态下，效率严重降低。例如，一个PAPR为$10\ \text{dB}$的OFDM信号，PA的峰值效率可能只有$10\%$（即使$78.5\%$是理论最大值）。

**Backoff and Efficiency:**

For a PA with $1\ \text{dB}$ compression at $P_{\text{out}} = +33\ \text{dBm}$, and a $10\ \text{dB}$ PAPR signal:

$$
P_{\text{avg}} = P_{\text{peak}} - \text{PAPR} = +33 - 10 = +23\ \text{dBm} \quad \text{(12.5)}
$$

The PA operates at $+23\ \text{dBm}$ (Class AB), but with efficiency severely reduced due to backoff.

### 12.1.4 Single-Ended and Differential PAs | 单端与差分PA

| Configuration | Pros | Cons |
|---|---|---|
| Single-ended | Simple, half the transistors | Requires balun (lossy), high current on supply |
| Differential | No balun needed, better supply rejection, even harmonics cancel | 2× transistors, area |

---

## 12.2 Classification of Power Amplifiers | 功率放大器分类

### 12.2.1 Class A Power Amplifiers | A类功率放大器

**Operation**: Transistor conducts for the entire RF cycle ($360^\circ$ conduction angle).

**Bias point**: Gate biased at $V_{GS} = V_{DD}/2$ (midpoint), transistor always in saturation.

**Theoretical maximum efficiency**: $\eta_{\max} = 50\%$ (for sine wave output).

**Derivation:**

With $V_{\text{out}} = V_{\text{DC}} + v_{\text{out}}\sin\omega t$, and $i_{\text{D}} = I_{\text{DC}} + i_{\text{out}}\sin\omega t$:

$$
\eta = \frac{P_{\text{out}}}{P_{\text{DC}}} = \frac{v_{\text{out}} \cdot i_{\text{out}}/2}{V_{\text{DC}} \cdot I_{\text{DC}}} = \frac{\alpha \beta}{2} \quad \text{(12.6)}
$$

where $\alpha = V_{\text{DC}}/v_{\text{out}}$ (voltage swing factor), $\beta = I_{\text{DC}}/i_{\text{out}}$.

Maximum when $\alpha = \beta = 1$: $\eta_{\max} = 50\%$.

> **（中文）** A类PA在整个RF周期内导通，效率上限为$50\%$（因为直流偏置电流在无信号时也在消耗功率）。A类PA提供最佳线性度，但效率最低。实际应用中，A类PA的效率通常只有$25-35\%$。

### 12.2.2 Class B Power Amplifiers | B类功率放大器

**Operation**: Two transistors in push-pull configuration, each conducts for $180^\circ$.

**Theoretical maximum efficiency**: $\eta_{\max} = \pi/4 \approx 78.5\%$.

**Derivation**: For a transistor conducting $180^\circ$:

$$
\eta = \frac{P_{\text{out}}}{P_{\text{DC}}} = \frac{\pi}{4}\frac{V_{\text{out,max}}}{V_{\text{DC}}} \quad \text{(12.7)}
$$

> **（中文）** B类PA使用推挽（push-pull）架构，两个晶体管交替导通，各工作$180^\circ$。理论上最大效率$\pi/4 \approx 78.5\%$，比A类PA高得多。但B类PA的线性度较差（因为每个晶体管只在半周期内导通，交叉点附近存在严重的非线性）。

### 12.2.3 Class C Power Amplifiers | C类功率放大器

**Operation**: Conduction angle $< 180^\circ$ per transistor.

**Efficiency**: Increases as conduction angle decreases:

$$
\eta_C = \frac{\pi \cos\theta}{2(\pi - \theta + \sin\theta\cos\theta)} \quad \text{(12.8)}
$$

| Conduction Angle | $\theta$ | Efficiency $\eta$ |
|---|---|---|
| $180^\circ$ (Class B) | $\pi/2$ | $78.5\%$ |
| $120^\circ$ | $\pi/3$ | $\sim 85\%$ |
| $90^\circ$ | $\pi/4$ | $\sim 90\%$ |

But gain decreases as conduction angle decreases.

> **（中文）** C类PA的导通角小于$180^\circ$，效率可以接近甚至超过B类PA，但增益（gain）严重降低，且输出功率大幅降低。C类PA仅适用于振荡器（oscillator）而不适用于线性PA。

---

## 12.3 High-Efficiency Power Amplifiers | 高效率功率放大器

### 12.3.1 Class A Stage with Harmonic Enhancement | 带谐波增强的A类PA

Placing a resonant network at the second harmonic ($2\omega_0$) at the PA output **shapes** the voltage waveform, pushing it towards a square wave → higher efficiency:

**Theoretical limit**: Approaches Class F efficiency ($\eta \rightarrow 88-90\%$).

> **（中文）** 在PA输出端加入二次谐波（$2\omega_0$）谐振网络可以将输出电压波形"整形"为接近方波，从而在理论上将效率提高到$88-90\%$（Class F）。这是因为方波包含了丰富的谐波分量，能量被更有效地传递到负载。

### 12.3.2 Class E Power Amplifier | E类功率放大器

Class E uses a **shunt capacitor** and **series inductor** to shape voltage and current waveforms so they never overlap simultaneously:

**Key waveform conditions:**
1. $v_{\text{DS}}(t)$ rises after $i_{\text{D}}(t)$ has fallen to zero (switch off → voltage rises after current is zero)
2. $dv_{\text{DS}}/dt$ is zero at the moment of switch-on

**Theoretical maximum efficiency**: $100\%$ (with ideal components and optimal waveform shaping).

**Output network design:**

$$
\omega_0 L_1 = \frac{1.365}{C_{\text{shunt}}} \quad \text{(12.9)}
$$
$$
R_L = \frac{1.365}{C_{\text{shunt}} \cdot \omega_0^2 L_1} \quad \text{(12.10)}
$$

> **（中文）** E类PA是开关模式PA的经典拓扑，其核心思想是"波形整形"：通过输出网络（并联电容$C_{\text{shunt}}$和串联电感$L_1$）使电压和电流波形在任意时刻都不重叠（当电流流过时电压为零或最小化），从而将功耗降到最低（理论上$100\%$效率）。E类PA广泛用于毫米波和RF功率应用。

### 12.3.3 Class F Power Amplifier | F类功率放大器

Class F PA uses **harmonic resonators** ($L_3$, $C_3$ at $3\omega_0$, $L_5$, $C_5$ at $5\omega_0$) to shape the voltage waveform to a square wave (odd harmonics add in-phase) while current waveform is half-sinusoid:

**Voltage waveform (ideal Class F):**

$$
v_{\text{DS}}(t) = V_{\text{DC}} + \sum_{n=1,3,5,\ldots} \frac{2V_{\text{DC}}}{n^2\pi^2} \cos(n\omega_0 t) \quad \text{(12.11)}
$$

**Theoretical maximum efficiency**: $100\%$ for infinite odd harmonics → practical limit $\eta \approx 85-90\%$.

> **（中文）** F类PA利用奇次谐波（$3\omega_0$, $5\omega_0$, ...）的谐振器将电压波形整形为方波，同时电流波形保持为半正弦波。理想情况下（无限多个奇次谐波），F类PA效率可达$100\%$；实际中，受限于谐波抑制度，效率约$85-90\%$。F类PA是高频PA（> $5\ \text{GHz}$）的常用选择。

---

## 12.4 Linearization Techniques | 线性化技术

### 12.4.1 Feedforward | 前馈

A feedforward PA cancels distortion by extracting the distortion component and subtracting it from the output:

**Error amplifier** detects the nonlinear distortion after the main PA:

$$
v_{\text{error}} = G_{\text{error}}(G_{\text{PA}} v_{\text{in}} - v_{\text{out}}) \quad \text{(12.12)}
$$

> **（中文）** 前馈（Feedforward）线性化通过提取并消除失真分量来改善PA线性度。主PA输出与输入经过适当衰减后的信号之差（包含失真分量）被误差放大器放大，然后从主PA输出中减去。前馈技术可以改善线性度$15-25\ \text{dB}$，但需要额外的误差放大器和功率耦合器，成本高。

### 12.4.2 Feedback | 反馈

**Envelope feedback (envelope elimination and restoration, EER):**

$$
P_{\text{out}} = \eta(V_{\text{ctrl}}) \cdot P_{\text{in,env}} \quad \text{(12.13)}
$$

Envelope elimination: Detect the envelope of the modulation signal → drive PA supply with this envelope.

**Cartesian feedback**: Close the loop around the I/Q modulator + PA, converting PA nonlinearity into loop dynamics.

> **（中文）** 反馈线性化技术将PA的输出反馈到输入端，将非线性转换为环路动态的一部分。包络反馈（EER）消除了信号的包络分量，仅放大相位调制成分，包络信息通过独立的包络放大器恢复。笛卡尔反馈（Cartesian feedback）则将I/Q调制器和PA一起包含在反馈环内。

### 12.4.3 Digital Predistortion (DPD) | 数字预失真

Modern transmitters use **digital predistortion (DPD)** to linearize the PA:

**Concept**: Characterize the PA's AM-AM (gain compression) and AM-PM (phase compression) characteristics, then pre-distort the input signal to compensate:

$$
x_{\text{DPD}}(t) = f^{-1}(y_{\text{desired}}(t)) \quad \text{(12.14)}
$$

where $f(\cdot)$ is the PA nonlinear transfer function.

**Implementation**: DSP or FPGA implements the inverse characteristic, updated adaptively.

> **（中文）** 数字预失真（DPD）是现代基站PA线性化的主流技术。它在数字域表征PA的AM-AM（增益压缩）和AM-PM（相位压缩）特性，然后在基带数字信号上预补偿这些非线性效应。DPD可以实现$15-20\ \text{dB}$的ACPR改善，使PA工作在更接近饱和的状态（更高效率）。这是4G LTE基站和5G NR基站的标准配置。

---

## 12.8 Outphasing | 异相技术

### 12.8.1 Basic Idea | 基本原理

Outphasing (also called LINC — Linear Amplification using Nonlinear Components) separates the amplitude and phase of the input signal:

$$
s(t) = A(t) e^{j\phi(t)} = \frac{A(t)}{A_{\max}}\left[e^{j(\omega_c t + \phi(t) + \theta)} + e^{j(\omega_c t + \phi(t) - \theta)}\right] \quad \text{(12.15)}
$$

where $\cos\theta = A(t)/A_{\max}$.

**Two constant-envelope PA** then amplify $e^{j(\omega_c t + \phi \pm \theta)}$ → high efficiency.

**Output recombination** at the antenna load reconstructs $A(t)$.

> **（中文）** 异相（outphasing/LINC）技术的核心思想：将调幅信号分解为两个恒包络信号的叠加（和、差相位路径），每个恒包络信号由高效率的非线性PA放大，然后在输出端通过功率合成器重构调幅信号。由于两个PA始终以恒包络工作，理论上可以达到很高的效率。

---

## 12.9 Doherty Power Amplifier | Doherty功率放大器

The Doherty PA uses a **main (carrier) amplifier** and an **auxiliary (peaking) amplifier**:

**At low power**: Main PA only (biased Class AB), auxiliary OFF.
**At high power**: Auxiliary PA turns on, adding its power to the output.

**Efficiency enhancement**: The main PA sees a lower load impedance at low power, maintaining high efficiency:

$$
R_{\text{eff}} = \frac{R_L}{2}\left(1 + \frac{V_{\text{aux}}}{V_{\text{main}}}\right) \quad \text{(12.16)}
$$

> **（中文）** Doherty PA是现代无线基站中使用最广泛的高效率PA架构。它使用两个PA（主PA和峰值PA）并联：低功率时仅主PA工作（高效率Class AB）；高功率时峰值PA开启，补充额外功率。Doherty架构使PA在整个功率回退范围内保持较高效率（$\sim 50\%$ at $6\ \text{dB}$ backoff），是LTE和5G NR基站PA的标准配置。

---

## Key Takeaways | 本章要点

1. **PA efficiency vs. linearity trade-off**: Higher efficiency classes (B, C, E, F) are less linear; for digital modulation (OFDM), linearization or backoff is required.
2. **PAPR problem**: OFDM signals have $7-12\ \text{dB}$ PAPR, requiring $7-12\ \text{dB}$ output backoff → severe efficiency degradation.
3. **Class E/F**: Switch-mode PAs achieve $\eta > 80\%$ by shaping voltage/current waveforms to avoid overlap.
4. **DPD**: Essential for modern basestation PAs, providing $15-20\ \text{dB}$ linearization, enabling near-saturation operation.
5. **Doherty**: Standard architecture for basestation PAs, achieving $\eta \sim 50\%$ at $6\ \text{dB}$ backoff.
6. **PAE** = $(P_{\text{out}} - P_{\text{driver}})/P_{\text{DC}}$; lower gain PA → lower PAE for same output power.
