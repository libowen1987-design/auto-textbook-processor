---
chapter: 2
title: Basic Concepts in RF Design
source: Behzad Razavi, RF Microelectronics, 2nd Edition, McGraw-Hill, 2012
pages: 7-86
---

# Chapter 2: Basic Concepts in RF Design
# 第二章：射频设计基本概念

> *"RF design draws upon many concepts from a variety of fields, including signals and systems, electromagnetics and microwave theory, and communications. Nonetheless, RF design has developed its own analytical methods and its own language."*
>
> **（中文）** 射频设计融合了信号系统、电磁场理论与通信理论的诸多概念，但同时发展出了自己独特的分析方法和专业术语。本章系统梳理后续各章节必需的基础知识，包括非线性效应、噪声分析、阻抗变换与散射参数。

---

## 2.1 General Considerations | 一般性考量

### 2.1.1 Units in RF Design | 射频设计中的单位制

#### Decibels (dB) | 分贝

RF engineers use decibels universally for gains and signal levels due to the enormous dynamic range involved.

**Voltage Gain (dB):**

$$
A_{V,\text{dB}} = 20 \log_{10}\frac{V_{\text{out}}}{V_{\text{in}}} \quad \text{(2.1)}
$$

**Power Gain (dB):**

$$
A_{P,\text{dB}} = 10 \log_{10}\frac{P_{\text{out}}}{P_{\text{in}}} \quad \text{(2.2)}
$$

> **（中文）** 注意：电压增益用$20\log_{10}$，功率增益用$10\log_{10}$。两者仅在输入输出阻抗相等时才在数值上相等。

**Special Case — Equal Impedances ($R_{\text{in}} = R_{\text{out}} = R_0$):**

$$
A_{P,\text{dB}} = 10 \log\frac{V_{\text{out}}^2 / R_0}{V_{\text{in}}^2 / R_0} = 20 \log\frac{V_{\text{out}}}{V_{\text{in}}} = A_{V,\text{dB}} \quad \text{(2.3)-(2.5)}
$$

> **（中文）** 在$50\ \Omega$系统中，若输入输出阻抗均为$R_0$，则功率增益与电压增益的dB数相等。但在大多数射频集成电路中，各级的输入输出阻抗并不相等，因此必须区分这两种增益。

#### dBm (Absolute Power Level) | dBm（绝对功率电平）

dBm expresses absolute power relative to 1 mW:

$$
P_{\text{sig}}[\text{dBm}] = 10 \log_{10}\frac{P_{\text{sig}}}{1\ \text{mW}} \quad \text{(2.6)}
$$

**Key Reference Values ($R_0 = 50\ \Omega$):**

| $P_{\text{sig}}$ [dBm] | $P_{\text{sig}}$ [mW] | $V_{\text{pp}}$ (sinusoid) |
|---|---|---|
| $0$ | $1$ | $632\ \text{mV}$ |
| $-10$ | $0.1$ | $200\ \text{mV}$ |
| $-30$ | $10^{-3}$ | $12.6\ \text{mV}$ |
| $-100$ | $10^{-10}$ | $6.32\ \mu\text{V}$ |

**Derivation of $0\ \text{dBm} \Leftrightarrow 632\ \text{mV}_{pp}$:**

For a sinusoid across $R_L = 50\ \Omega$ delivering $P = 1\ \text{mW}$:

$$
\frac{V_{\text{pp}}^2}{8R_L} = 1\ \text{mW} \Rightarrow V_{\text{pp}} = \sqrt{8 R_L \cdot 1\ \text{mW}} = \sqrt{8 \times 50 \times 10^{-3}} = 632\ \text{mV} \quad \text{(2.7),(2.8)}
$$

> **（中文）** 这是一个极其有用的参考值：$0\ \text{dBm}$（即$1\ \text{mW}$）对应$632\ \text{mV}_{pp}$（正弦波）。从此可快速推导其他功率电平的等效电压：每降低$20\ \text{dB}$，电压幅度降低10倍；每降低$20\ \text{dB}$电压，功率降低100倍（因为$P = V^2/R$）。

**Example 2.2 — GSM Receiver Sensitivity Calculation:**

GSM minimum sensitivity $\approx -104\ \text{dBm}$. With $15\ \text{dB}$ voltage gain:

Input level: $-104\ \text{dBm} \Leftrightarrow 6.32\ \mu\text{V}_{pp}$ (since $0\ \text{dBm} = 632\ \text{mV}_{pp}$ and $-100\ \text{dB} \approx 100\ \text{dB}$ for voltage)

Output swing: $6.32\ \mu\text{V}_{pp} \times 10^{15/20} = 6.32\ \mu\text{V}_{pp} \times 5.62 \approx 35.5\ \mu\text{V}_{pp}$

> **（中文）** 注意：$15\ \text{dB}$的电压增益对应对应幅度放大$10^{15/20} \approx 5.62$倍（而非$10^{1.5}$）。这是因为电压增益是$20\log$刻度，而功率增益是$10\log$刻度。

---

### 2.1.2 Time Variance | 时变性

#### Definitions | 定义

**Linearity**: A system is *linear* if superposition holds:

$$
y_1(t) = f[x_1(t)], \quad y_2(t) = f[x_2(t)] \Rightarrow f[ax_1(t) + bx_2(t)] = ay_1(t) + by_2(t) \quad \text{(2.9)-(2.11)}
$$

**Time-Invariance**: A system is *time-invariant* if a time shift in input produces identical time shift in output:

$$
y(t) = f[x(t)] \Rightarrow y(t - \tau) = f[x(t - \tau)] \quad \forall\ \tau
$$

> **（中文）** 线性与时不变性是两个独立概念。时变系统未必非线性，反之亦然。在射频电路中，切换（switching）是最常见的时变来源，例如Gilbert单元中的LO开关对。

#### Switching as a Time-Variant System | 开关切换作为时变系统

Consider a switch driven by $v_{\text{in1}}(t) = A_1\cos\omega_1 t$ (LO) and input $v_{\text{in2}}(t) = A_2\cos\omega_2 t$ (RF signal):

- If $v_{\text{in1}} > 0$: switch ON $\Rightarrow v_{\text{out}}(t) = v_{\text{in2}}(t)$
- If $v_{\text{in1}} < 0$: switch OFF $\Rightarrow v_{\text{out}}(t) = 0$

This is a **time-variant** system because the output depends on the instantaneous value of $v_{\text{in1}}(t)$, not just on $v_{\text{in2}}(t)$ as a function of time.

**Self-Mixing (Self-Downconversion) | 自混频（自下变频）**

A critical consequence of time variance: the LO signal can mix with itself (or with its harmonics) and fold interference back to baseband. This manifests as **DC offset** or **LO leakage** problems in direct-conversion receivers.

> **（中文）** 时变性在射频电路中的典型危害是"自混频"：本振信号通过非线性通路与自身混频，将干扰信号直接下变频到基带。在零中频（direct-conversion）接收机中，这是直流偏置和本振泄漏的主要来源之一。

---

### 2.1.3 Nonlinearity | 非线性

#### Taylor Series Representation | 泰勒级数表示

Any nonlinear system can be expressed around an operating point $Q$:

$$
y(t) = \alpha_1 x(t) + \alpha_2 x^2(t) + \alpha_3 x^3(t) + \cdots \quad \text{(2.57)}
$$

For an RF circuit with $x(t) = A\cos\omega_0 t$:

$$
y(t) = \alpha_1 A\cos\omega_0 t + \frac{\alpha_2 A^2}{2}(1 + \cos 2\omega_0 t) + \frac{\alpha_3 A^3}{4}(3\cos\omega_0 t + \cos 3\omega_0 t) + \cdots
$$

| Term | Coefficient | Output Component |
|---|---|---|
| Fundamental | $\alpha_1 A + \frac{3\alpha_3 A^3}{4}$ | $\omega_0$ |
| 2nd harmonic | $\frac{\alpha_2 A^2}{2}$ | $2\omega_0$ |
| 3rd harmonic | $\frac{\alpha_3 A^3}{4}$ | $3\omega_0$ |
| DC offset | $\frac{\alpha_2 A^2}{2}$ | $\omega = 0$ |

> **（中文）** 泰勒级数是分析射频非线性电路的标准工具。注意$\alpha_3$项在基波频率$\omega_0$处产生附加增益$\frac{3\alpha_3 A^2}{4}$，这正是增益扩展（gain expansion/compression）的来源。

---

## 2.2 Effects of Nonlinearity | 非线性的影响

### 2.2.1 Harmonic Distortion | 谐波失真

For a single-tone input $x(t) = A\cos\omega_1 t$, the output contains harmonics at $n\omega_1$:

$$
y(t) \approx \underbrace{\alpha_1 A\cos\omega_1 t}_{\text{fundamental}} + \underbrace{\frac{\alpha_2 A^2}{2}\cos 2\omega_1 t}_{2\text{nd harmonic}} + \underbrace{\frac{\alpha_3 A^3}{4}\cos 3\omega_1 t}_{3\text{rd harmonic}} + \cdots
$$

**Total Harmonic Distortion (THD):**

$$
\text{THD} = \frac{\sqrt{V_2^2 + V_3^2 + \cdots}}{V_1} \quad \text{(2.64)}
$$

where $V_n$ is the rms amplitude of the $n$-th harmonic.

> **（中文）** 谐波失真（THD）在射频中不如在音频中重要（因为谐波通常在滤波后被抑制），但它反映了电路非线性的严重程度。在窄带射频系统中，谐波失真通常不是主要问题——主要关注的是互调失真（IMD）和增益压缩。

---

### 2.2.2 Gain Compression | 增益压缩

The fundamental gain including the $\alpha_3$ term:

$$
\frac{y_{\text{fund}}(t)}{A} = \alpha_1 + \frac{3\alpha_3 A^2}{4} \quad \text{(2.70)}
$$

**Definition — 1-dB Compression Point ($P_{\text{1dB}}$):**

The input amplitude $A_{\text{1dB}}$ (or output) at which the actual gain is $1\ \text{dB}$ below the small-signal (linear) gain.

Mathematically:

$$
20\log_{10}\left|\alpha_1 + \frac{3\alpha_3 A_{\text{1dB}}^2}{4}\right| = 20\log_{10}|\alpha_1| - 1\ \text{dB}
$$

Solving for the case $|\alpha_1| \gg |\frac{3\alpha_3 A^2}{4}|$:

$$
A_{\text{1dB}}^2 \approx \frac{4}{3}\left|\frac{\alpha_1}{\alpha_3}\right| \cdot 10^{-1/20} \approx 0.145\left|\frac{\alpha_1}{\alpha_3}\right| \quad \text{(2.71)}
$$

Or in terms of input-referred power:

$$
P_{\text{1dB}}[\text{dBm}] = 10\log_{10}\frac{A_{\text{1dB}}^2 / (2R)}{1\ \text{mW}} \quad \text{(2.72)}
$$

**Relationship between $P_{\text{1dB}}$ and IP3:**

The third-order intercept point (IP3) relates to $P_{\text{1dB}}$ by approximately:

$$
P_{\text{1dB}} \approx \text{IP3} - 9.6\ \text{dB} \quad \text{(empirical)}
$$

> **（中文）** $P_{\text{1dB}}$是射频电路设计中最重要的非线性指标之一。它表示当增益从线性增益压缩$1\ \text{dB}$时的输入功率。典型射频LNA的$P_{\text{1dB}}$约为$-10\ \text{dBm}$到$0\ \text{dBm}$。IP3与$P_{\text{1dB}}$的经验关系约为$9.6\ \text{dB}$，即IP3比$P_{\text{1dB}}$高约$10\ \text{dB}$。

---

### 2.2.3 Cross Modulation | 交叉调制

When a large interferer (modulated carrier) and a desired signal share a nonlinear stage, the interferer's modulation can "transfer" onto the desired signal. This is **cross-modulation**.

For a desired signal $A\cos\omega_1 t$ and an interferer $B[1 + m\cos\omega_m t]\cos\omega_2 t$:

The third-order term $\alpha_3 x^3(t)$ generates a component at $\omega_1$ proportional to the interferer's envelope $m\cos\omega_m t$.

> **（中文）** 交叉调制的物理机制：强干扰信号的调幅包络通过$\alpha_3$非线性项"污染"有用信号。这是移动蜂窝系统中邻近频道干扰（adjacent channel interference）的重要机制。当一个频道的调幅信号经过非线性器件时，其包络变化会被交叉调制到相邻频道。

---

### 2.2.4 Intermodulation | 互调失真

#### Two-Tone Intermodulation | 双音互调

Consider two closely-spaced tones: $x(t) = A\cos\omega_1 t + A\cos\omega_2 t$.

Third-order nonlinearity generates:

$$
\alpha_3 x^3(t) \supset \frac{3\alpha_3 A^3}{4}\left[\cos\omega_1 t + \cos\omega_2 t + \frac{1}{4}\cos(3\omega_1 - 2\omega_2)t + \frac{1}{4}\cos(3\omega_2 - 2\omega_1)t\right]
$$

**Third-Order Intermodulation Products (IM3):**

| Product | Frequency | Location |
|---|---|---|
| $2\omega_1 - \omega_2$ | $2f_1 - f_2$ | Near band of interest |
| $2\omega_2 - \omega_1$ | $2f_2 - f_1$ | Near band of interest |

> **（中文）** IM3产物（尤其是$2f_1 - f_2$和$2f_2 - f_1$）落在有用信号附近，无法通过滤波器滤除，因此是窄带射频系统的主要非线性干扰来源。

#### Third-Order Intercept Point (IP3) | 三阶截点

Define the *input-referred* third-order intercept point (IIP3) as the input amplitude at which the extrapolated fundamental and IM3 powers are equal.

For input amplitude $A$:

$$
P_{\text{fund}} \propto \alpha_1^2 A^2 \quad \text{(linear in dB)} \quad \text{(2.76)}
$$
$$
P_{\text{IM3}} \propto \alpha_3^2 A^6 \quad \text{(6× slope in dB)} \quad \text{(2.77)}
$$

Setting $P_{\text{fund}} = P_{\text{IM3}}$:

$$
A_{\text{IIP3}} = \sqrt{\frac{4}{3}\left|\frac{\alpha_1}{\alpha_3}\right|} \quad \text{(2.79)}
$$

Or in dBm:

$$
IIP3[\text{dBm}] = 10\log_{10}\frac{A_{\text{IIP3}}^2 / (2R_0)}{1\ \text{mW}} \quad \text{(2.80)}
$$

**Fundamental vs. IM3 Power Relationship:**

$$
P_{\text{IM3}} = P_{\text{fund}} - 2(P_{\text{IIP3}} - P_{\text{in}}) \quad \text{(2.84)}
$$

or equivalently:

$$
P_{\text{IM3}}[\text{dBm}] = 3P_{\text{in}}[\text{dBm}] - 2\cdot IIP3[\text{dBm}] \quad \text{(2.85)}
$$

> **（中文）** IIP3是射频系统最重要的线性度指标之一。IIP3比输入信号每高$1\ \text{dB}$，IM3产物就降低$3\ \text{dB}$（因为IM3功率与$A^6$成正比，即$\text{dB}$斜率为输入的$3$倍）。典型的CMOS LNA的IIP3约为$-10\ \text{dBm}$至$-5\ \text{dBm}$。

---

### 2.2.5 Cascaded Nonlinear Stages | 级联非线性级

For two cascaded nonlinear stages, the overall IP3 depends on each stage's IP3 and gain.

**Friis Formula for IP3 (Cascaded IIP3):**

$$
\frac{1}{A_{\text{IIP3,tot}}^2} \approx \frac{1}{A_{\text{IIP3,1}}^2} + \frac{G_1^2}{A_{\text{IIP3,2}}^2} + \cdots \quad \text{(2.97)}
$$

In voltage amplitude units. In dB:

$$
\frac{1}{IIP3_{\text{tot}}^2} \approx \frac{1}{IIP3_1^2} + \frac{G_1^2}{IIP3_2^2} + \cdots \quad \text{(2.98)}
$$

where $G_1$ is the power gain (not in dB) of stage 1.

**Key Insight**: The front-end (first stage) dominates the overall IP3 because its noise and nonlinearity are not "amplified" by prior stages.

> **（中文）** 级联系统的IIP3遵循平方和的倒数规律（类似噪声系数的Friis公式）。第一级对总体IIP3的贡献最为关键，因为它的失真不会被前置增益"放大"。这正是为什么LNA（第一级）必须同时具备低噪声和高线性度。

**Second-Order Cascaded Nonlinearity**: Two stages with only second-order ($\alpha_2$) nonlinearity can still produce finite IP3 when cascaded, due to the second stage's $\alpha_2$ processing the second-order product from stage 1.

---

### 2.2.6 AM/PM Conversion | 幅相转换

AM/PM conversion describes the phenomenon where amplitude variations in the input cause phase variations in the output — i.e., the transfer function has an *AM-PM* effect.

A circuit with AM/PM conversion distorts phase-modulated (PM) or frequency-modulated (FM) signals even if it is perfectly linear in amplitude.

**Taylor Series Treatment**:

If $y(t) = f[x(t)]$ with a large-signal bias, and $f(\cdot)$ contains higher-order terms, then the effective transconductance $g_m = \partial y / \partial x$ becomes a function of signal amplitude $A$:

$$
g_m(A) = \alpha_1 + \frac{3\alpha_3 A^2}{4} + \cdots
$$

A change in signal amplitude $\Delta A$ causes a change in phase:

$$
\Delta\phi \propto \frac{\partial g_m}{\partial A}\Delta A
$$

> **（中文）** AM/PM转换是锁相环（PLL）和振荡器设计中的关键问题。当VCO的输出幅度因调谐或其他效应而变化时，其相位也会随之改变，产生意外的相位调制。在功率放大器中，AM/PM效应会导致调幅信号经过PA后产生相位失真，是线性化技术（如Feedforward、Digital Pre-Distortion）必须补偿的效应。

---

## 2.3 Noise | 噪声

### 2.3.1 Noise as a Random Process | 噪声作为随机过程

Noise in electronic systems is a random process characterized statistically by:

- **Mean (DC value)**: $\mu = \mathbb{E}[n(t)]$
- **Variance**: $\sigma^2 = \mathbb{E}[(n(t)-\mu)^2] = \overline{n^2} - \mu^2$
- **Autocorrelation**: $R_n(\tau) = \mathbb{E}[n(t)n(t+\tau)]$

For thermal noise in resistors, the DC mean is zero ($\mu = 0$).

> **（中文）** 电阻热噪声的均值$\mu = 0$（无直流分量），其随机性来源于载流子的热运动。在电路分析中，我们用统计量（均值、方差、自相关函数）来描述噪声特性。

**Probability Density Function (PDF)**: Thermal (Gaussian) noise follows a Gaussian (normal) distribution:

$$
p_n(v) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{v^2}{2\sigma^2}\right) \quad \text{(2.104)}
$$

### 2.3.2 Noise Spectrum | 噪声频谱

#### Power Spectral Density (PSD) | 功率谱密度

The PSD $S_n(\omega)$ is the Fourier transform of the autocorrelation:

$$
S_n(\omega) = \int_{-\infty}^{\infty} R_n(\tau) e^{-j\omega\tau}\ d\tau \quad \text{(2.105)}
$$

and by Wiener-Khinchin:

$$
R_n(\tau) = \frac{1}{2\pi}\int_{-\infty}^{\infty} S_n(\omega)e^{j\omega\tau}\ d\omega \quad \text{(2.106)}
$$

**Total Noise Power**:

$$
\overline{n^2} = R_n(0) = \frac{1}{2\pi}\int_{-\infty}^{\infty} S_n(\omega)\ d\omega \quad \text{(2.107)}
$$

#### White Noise | 白噪声

White noise has a flat (constant) PSD:

$$
S_n(\omega) = \frac{\overline{n^2}}{\Delta\omega} = \frac{\eta}{2\pi} \quad \text{(2.108)}
$$

where $\eta$ is the two-sided PSD in W/Hz. Total noise over bandwidth $B$:

$$
\overline{n^2} = \eta \cdot B \quad \text{(2.109)}
$$

> **（中文）** 白噪声的功率谱密度在所有频率上都是常数$\eta$（单位：$\text{W/Hz}$或$\text{V}^2/\text{Hz}$）。实际系统的有限带宽使白噪声表现为带限白噪声（band-limited white noise）。热噪声和散粒噪声在高频范围内近似为白噪声。

### 2.3.3 Effect of Transfer Function on Noise | 传递函数对噪声的影响

If a noise source $n(t)$ with PSD $S_n(\omega)$ passes through a linear system with transfer function $H(\omega)$, the output noise PSD is:

$$
S_{n,\text{out}}(\omega) = |H(\omega)|^2 S_n(\omega) \quad \text{(2.110)}
$$

**Noise Bandwidth $B_n$**: The equivalent bandwidth of a system with frequency response $H(\omega)$:

$$
B_n = \frac{1}{|H(0)|^2}\int_0^\infty |H(\omega)|^2\ d\omega \quad \text{(2.111)}
$$

> **（中文）** 线性系统的噪声传递：输出噪声功率谱 = 输入噪声功率谱 × $|H(\omega)|^2$。这一定理是噪声分析的核心工具，使我们能够计算任意系统对噪声的响应。噪声带宽$B_n$是将实际系统等效为一个理想矩形滤波器所需的带宽。

### 2.3.4 Device Noise | 器件噪声

#### Thermal Noise in Resistors | 电阻热噪声

Nyquist (1928): A resistor $R$ at temperature $T$ produces thermal noise voltage:

$$
\overline{v_n^2} = 4kTRB \quad \text{(2.112)}
$$

or as a series voltage source:

$$
v_n(t) = \sqrt{4kTR}\cdot \sqrt{B}\cdot n(t) \quad \text{(2.113)}
$$

The two-sided PSD:

$$
S_v(f) = 4kTR \quad \text{(V}^2/\text{Hz)} \quad \text{(2.114)}
$$

where $k = 1.38 \times 10^{-23}\ \text{J/K}$ (Boltzmann constant), $T$ in Kelvin.

**Noise in conductor**: $S_I(f) = 4kT/R$ (current noise).

> **（中文）** 电阻热噪声是所有导体中载流子热运动产生的随机电压/电流。噪声功率与电阻值$R$和温度$T$成正比。这一定律（Nyquist噪声）是所有电阻性元件噪声分析的基础。

#### Shot Noise | 散粒噪声

Shot noise arises from the discrete nature of charge carriers in semiconductor devices:

$$
\overline{i_n^2} = 2qI_{\text{DC}}B \quad \text{(2.115)}
$$

Two-sided PSD: $S_I(f) = 2qI_{\text{DC}}$ (A$^2$/Hz)

> **（中文）** 散粒噪声是PN结中载流子扩散与漂移的随机性产生的噪声。当电流$I_{\text{DC}}$流过势垒时，每个载流子通过的时间具有随机性，导致电流围绕均值涨落。散粒噪声的PSD与频率无关（白噪声）。

#### Flicker Noise (1/f Noise) | 闪烁噪声（1/f噪声）

Flicker noise is dominant at low frequencies:

$$
S_I(f) \propto \frac{I_{\text{DC}}^2}{f^\gamma} \quad \text{(2.116)}
$$

where $\gamma \approx 1$ (typically). The corner frequency $f_c$ is where flicker noise equals white noise.

**MOSFET 1/f Noise Models**:

Two common models:

**(a) Voltage Noise Source (gate-referred)**:

$$
\overline{v_n^2} = \frac{K}{WLC_{\text{ox}}}\frac{1}{f} \quad \text{(2.117)}
$$

**(b) Current Noise Source (drain-referred)**:

$$
\overline{i_n^2} = \frac{K}{WLC_{\text{ox}}}g_m^2\frac{1}{f} \quad \text{(2.118)}
$$

where $K$ is a process-dependent constant ($\sim 10^{-25}\ \text{F}\cdot\text{V}^2\cdot\text{s}$ for NMOS in typical CMOS), $W$, $L$ are device dimensions.

> **（中文）** 闪烁噪声（$1/f$噪声）是MOS器件中氧化层-硅界面陷阱捕获/释放载流子导致的低频噪声。其噪声功率谱密度与频率成反比（$\gamma \approx 1$）。在射频电路中，$1/f$噪声会在零中频（direct-conversion）接收机中产生直流偏置和低频漂移，是直接转换接收机的主要挑战之一。减小$1/f$噪声的方法：增大器件面积$WL$、使用PMOS（载流子迁移率更稳定）、或采用相关双采样（CDS）技术。

#### MOSFET Thermal Noise | MOSFET热噪声

The channel thermal noise in saturation is typically modeled as a drain-current noise source:

$$
\overline{i_{n,d}^2} = 4kT\gamma g_m B \quad \text{(2.119)}
$$

or equivalently as a gate-referred voltage noise:

$$
\overline{v_{n,g}^2} = \frac{4kT\gamma}{g_m}B \quad \text{(2.120)}
$$

For long-channel devices, $\gamma \approx 2/3$. For short-channel devices, $\gamma$ can be $2$ to $3$.

> **（中文）** MOSFET沟道热噪声的$\gamma$因子与器件长度相关：长沟道器件$\gamma \approx 2/3$（符合平方律模型），而短沟道器件$\gamma$可达$2-3$（因为速度饱和效应）。在射频LNA设计中，需要在热噪声性能和$f_T$之间权衡——更大的$g_m$（更大器件）降低噪声，但降低$f_T$和带宽。

### 2.3.5 Representation of Noise in Circuits | 电路中噪声的表示

#### Input-Referred Noise | 输入参考噪声

Any noisy two-port can be represented as a noiseless two-port with two noise sources at its input:

**Series (voltage noise) model**: $v_n$ in series with the input
**Shunt (current noise) model**: $i_n$ in parallel with the input

Total input-referred noise voltage:

$$
\overline{v_{\text{in,eq}}^2} = \overline{v_n^2} + \overline{i_n^2}R_s^2 + 4kTR_s B \quad \text{(2.122)}
$$

> **（中文）** 输入参考噪声是分析级联系统噪声的标准方法。将各级噪声等效到系统输入端，可以直观地比较各级的噪声贡献。关键是选择合适的参考点（通常在信号源阻抗$R_s$处）来合并各噪声源。

#### Noise Figure (NF) | 噪声系数

**Definition (IEEE)**:

$$
\text{NF} = \frac{\text{SNR}_{\text{in}}}{\text{SNR}_{\text{out}}} = \frac{P_{\text{sig,in}}/P_{\text{noise,in}}}{P_{\text{sig,out}}/P_{\text{noise,out}}} \quad \text{(2.123)}
$$

In dB: $\text{NF}[\text{dB}] = 10\log_{10}\text{NF}$.

**Noise Factor** $F = \text{NF}$ (linear).

**Input-Referred Noise Voltage from NF**:

$$
\overline{v_{\text{in,eq}}^2} = 4kTR_s B \cdot F = 4kTR_s B \cdot 10^{\text{NF}/10} \quad \text{(2.126)}
$$

#### Friis Noise Formula | Friis噪声公式

For cascaded two-port stages:

$$
F_{\text{total}} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \cdots \quad \text{(2.127)}
$$

In dB:

$$
\text{NF}_{\text{total}} = 10\log_{10}F_{\text{total}} \quad \text{(2.128)}
$$

> **（中文）** Friis公式是射频系统噪声分析的核心工具。它表明：①第一级的噪声系数$F_1$和功率增益$G_1$对总体噪声系数影响最大；②后续各级的噪声被前置增益逐级"衰减"。因此，降低系统噪声系数的关键是降低第一级的噪声并最大化其增益——这正是LNA作为接收机第一级必须具备低噪声特性的原因。

**Example — Two-Stage LNA**:

$$
F_{\text{total}} = F_{\text{LNA}} + \frac{F_{\text{mixer}} - 1}{G_{\text{LNA}}}
$$

If $F_{\text{LNA}} = 2$ (3 dB), $G_{\text{LNA}} = 20$ (13 dB), $F_{\text{mixer}} = 10$ (10 dB):

$$
F_{\text{total}} = 2 + \frac{10 - 1}{20} = 2 + 0.45 = 2.45 \Rightarrow \text{NF} = 3.9\ \text{dB}
$$

#### Noise Temperature | 噪声温度

Noise temperature is an alternative to noise factor for very low-noise systems:

$$
T_e = (F - 1)T_0 \quad \text{(2.130)}
$$

where $T_0 = 290\ \text{K}$ (standard reference temperature).

Total available noise power from a source resistance $R_s$:

$$
P_{\text{noise}} = kT_e B \quad \text{(2.131)}
$$

> **（中文）** 噪声温度$T_e$在卫星通信、射电天文等极低噪声系统中比噪声系数更常用。对于低噪声系统，$T_e$比$\text{NF}$更能精确反映噪声性能差异。例如，一个$50\ \text{K}$的低噪声放大器对应的噪声系数约为$0.19\ \text{dB}$，但如果用噪声温度$T_e = 290\ \text{K}$（室温）描述则为$3\ \text{dB}$——显然$T_e$提供了更精确的低噪声度量。

---

## 2.4 Sensitivity and Dynamic Range | 灵敏度与动态范围

### 2.4.1 Sensitivity | 灵敏度

**Definition**: The minimum detectable signal power $P_{\text{sig,min}}$ at the input, defined as the signal power that yields a specified $\text{SNR}_{\text{min}}$ at the output:

$$
P_{\text{sig,min}} = kT_0 B \cdot F \cdot \text{SNR}_{\text{min}} \quad \text{(2.132)}
$$

In dBm:

$$
P_{\text{sig,min}}[\text{dBm}] = -174 + 10\log_{10}B + \text{NF} + \text{SNR}_{\text{min}} \quad \text{(2.133)}
$$

where $-174\ \text{dBm/Hz}$ is the thermal noise floor at $290\ \text{K}$.

**Example — GSM Sensitivity:**

- $B = 200\ \text{kHz}$ (GSM channel bandwidth)
- $\text{NF} = 9\ \text{dB}$ (typical RX NF)
- $\text{SNR}_{\text{min}} = 9\ \text{dB}$ (for BER = $2\%$)

$$
P_{\text{sig,min}} = -174 + 53 + 9 + 9 = -103\ \text{dBm}
$$

> **（中文）** 灵敏度是接收机最重要的性能指标之一。它表示接收机能够可靠检测和解调弱信号的能力。由公式可见，降低接收机噪声系数（NF）和前端低噪放（LNA）的增益是提高灵敏度的关键。

### 2.4.2 Dynamic Range (DR) | 动态范围

#### Linear Dynamic Range (LDR) | 线性动态范围

Defined from $P_{\text{1dB}}$ to sensitivity:

$$
\text{LDR} = \frac{P_{\text{1dB}}}{P_{\text{sig,min}}} \quad \text{(2.134)}
$$

In dB: $\text{LDR}[\text{dB}] = P_{\text{1dB}}[\text{dBm}] - P_{\text{sig,min}}[\text{dBm}]$

> **（中文）** 线性动态范围定义为$1\ \text{dB}$压缩点功率与灵敏度之比（比值），或两者之差（dB数）。它表示接收机在线性工作条件下能够处理的信号功率范围。

#### Spurious-Free Dynamic Range (SFDR) | 无杂散动态范围

The ratio between the power of the stronger of two equal-power input tones and the power of the IM3 product they generate (when each tone is at the minimum detectable level):

For two equal-power input tones at $P_{\text{in}}$:

$$
P_{\text{IM3}} = 3P_{\text{in}} - 2IIP3 \quad \text{(from 2.85)}
$$

Setting $P_{\text{IM3}} = P_{\text{sig,min}}$ and solving:

$$
\text{SFDR} = \frac{2}{3}(IIP3 - P_{\text{sig,min}}) \quad \text{(2.139)}
$$

> **（中文）** SFDR是无杂散动态范围，它同时考虑了线性度（IM3产物）和灵敏度两个因素。两个等功率干扰信号产生的三阶互调产物刚好等于灵敏度时，两个输入信号的功率与灵敏度之比即为SFDR。在强干扰场景（如蜂窝基站）中，SFDR是衡量接收机性能的关键指标。

---

## 2.5 Passive Impedance Transformation | 无源阻抗变换

### 2.5.1 Quality Factor $Q$ | 品质因子 $Q$

**Definition — Loaded $Q$ of a Resonant Network:**

$$
Q_{\text{loaded}} = \frac{R_{\text{eq}}}{X_{\text{eq}}} = \frac{\text{Energy Stored}}{\text{Energy Dissipated per cycle}} \times 2\pi \quad \text{(2.140)}
$$

**Series RLC:** $Q_s = \omega_0 L / R_s = 1/(\omega_0 C R_s)$

**Parallel RLC:** $Q_p = R_p / (\omega_0 L) = \omega_0 C R_p$

> **（中文）** 品质因子$Q$是无源谐振电路的核心参数，描述了储能元件（$L$或$C$）与耗能元件（$R$）的比值。高$Q$电路具有窄带、陡峭的频率响应和低损耗；低$Q$电路宽带但损耗较大。在射频匹配网络中，$Q$直接决定了带宽。

### 2.5.2 Series-to-Parallel Conversion | 串并联转换

A series resistor $R_s$ and reactance $X_s$ can be converted to an equivalent parallel form:

$$
R_p = R_s(1 + Q_s^2) \quad \text{(2.141)}
$$
$$
X_p = X_s(1 + \frac{1}{Q_s^2}) \approx X_s \quad \text{for } Q_s \gg 1 \quad \text{(2.142)}
$$

Similarly, parallel-to-series:

$$
R_s = \frac{R_p}{1 + Q_p^2} \quad \text{(2.143)}
$$
$$
X_s = \frac{X_p}{1 + 1/Q_p^2} \approx X_p \quad \text{for } Q_p \gg 1 \quad \text{(2.144)}
$$

> **（中文）** 串并联等效变换在分析包含电感和电容的高$Q$谐振回路时极其有用。在$Q \gg 1$的条件下，串联形式与并联形式的电抗值近似相等，但电阻值差异显著：$R_p \approx Q^2 R_s$。这意味着一个小串联电阻在高$Q$电路中表现为一个大的并联电阻。

### 2.5.3 Basic Matching Networks | 基本匹配网络

**Goal**: Transform a source impedance $Z_S = R_S + jX_S$ to present a specific impedance $Z_L$ at a reference plane, typically $Z_0 = 50\ \Omega$.

#### L-Match (Low-Q) | L型匹配

Two reactive elements forming an "L" shape:

**Case 1 — $R_S < R_L$**: Inductor in series with source, capacitor in shunt to ground (or vice versa).

**Case 2 — $R_S > R_L$**: Capacitor in series, inductor in shunt.

The component values are determined by the $Q$ requirement:

$$
Q = \sqrt{\frac{R_{\text{high}}}{R_{\text{low}}} - 1} \quad \text{(2.145)}
$$

> **（中文）** L型匹配网络仅用两个无源元件（一个电感+一个电容）即可实现任意两个实阻抗之间的宽带匹配。其带宽由$Q = \sqrt{R_{\text{high}}/R_{\text{low}} - 1}$决定，阻抗比越大，$Q$越高，带宽越窄。

#### T-Match and Pi-Match | T型与π型匹配

**T-Network**: Three reactive elements forming a "T", provides greater flexibility and higher $Q$.

**Pi-Network ($\pi$-Match)**: Three reactive elements forming a "$\pi$", commonly used in PA output matching where the load is a low impedance (e.g., $50\ \Omega$ antenna feeding a $5\ \Omega$ transistor drain).

**Bandwidth of T/π networks**:

$$
B \approx \frac{f_0}{Q_{\text{loaded}}} \quad \text{(2.146)}
$$

> **（中文）** T型和π型匹配网络比L型多一个元件，提供两个调节自由度，可同时实现阻抗匹配和特定$Q$（带宽）设计。π型网络在功放（PA）输出匹配中尤为常用，因为PA的负载阻抗通常远低于$50\ \Omega$，需要将$50\ \Omega$天线阻抗变换为PA所需的负载阻抗。

### 2.5.4 Loss in Matching Networks | 匹配网络的损耗

Loss in a matching network arises from the finite $Q$ of inductors (series $r_L$) and capacitors (series $r_C$).

**Insertion Loss $L_{\text{ins}}$** (in dB):

$$
L_{\text{ins}} = 10\log_{10}\frac{P_{\text{available,source}}}{P_{\text{delivered,load}}} \quad \text{(2.147)}
$$

For an L-match with inductor $Q_L$:

$$
L_{\text{ins}} \approx 10\log_{10}\left(1 + \frac{R_S}{Q_L^2 R_{\text{seq}}}\right) \quad \text{(2.148)}
$$

> **（中文）** 匹配网络的损耗直接降低了系统的增益和效率。电感的$Q$值（$Q_L = \omega L / r_L$）是决定损耗的关键：低$Q$电感（片上螺旋电感$Q \approx 10-20$）比高$Q$电感（分立电感$Q \approx 100+$）的损耗大得多。在毫米波频段，匹配网络损耗可能成为限制系统效率的主要因素。

---

## 2.6 Scattering Parameters | 散射参数

S-parameters are the standard way to characterize RF networks at high frequencies where voltage/current measurements become impractical.

### Definition | 定义

For a two-port network terminated in $Z_0 = 50\ \Omega$:

| Parameter | Definition | Physical Meaning |
|---|---|---|
| $S_{11}$ | $\Gamma_{\text{in}} = V_1^- / V_1^+$ | Input reflection coefficient |
| $S_{22}$ | $\Gamma_{\text{out}} = V_2^- / V_2^+$ | Output reflection coefficient |
| $S_{21}$ | $V_2^- / V_1^+$ (with $V_2^+ = 0$) | Forward transmission (gain) |
| $S_{12}$ | $V_1^- / V_2^+$ (with $V_1^+ = 0$) | Reverse isolation |

In dB: $S_{21}[\text{dB}] = 20\log_{10}|S_{21}|$ (voltage gain), $S_{11}[\text{dB}] = 20\log_{10}|S_{11}|$.

> **（中文）** S参数是微波工程的标准描述方式。当频率升高到几百MHz以上时，传统的电压/电流测量变得困难，而S参数通过反射系数（$\Gamma$）和传输系数测量即可表征网络特性。$S_{11}$和$S_{22}$描述阻抗匹配情况（$|\Gamma| = 0$为完美匹配）；$S_{21}$描述正向增益；$S_{12}$描述反向隔离度。

### Stability | 稳定性

A two-port is **unconditionally stable** if $\Kappa > 1$ and $|\Delta| < 1$, where:

$$
\Delta = S_{11}S_{22} - S_{12}S_{21} \quad \text{(2.149)}
$$
$$
K = \frac{1 - |S_{11}|^2 - |S_{22}|^2 + |\Delta|^2}{2|S_{12}S_{21}|} \quad \text{(2.150)}
$$

**Stability Circles**: In the Smith chart, the locus of source or load impedances that make the circuit marginally stable ($\Gamma_L = 1$ or $\Gamma_S = 1$).

> **（中文）** 稳定性判据$K > 1$和$|\Delta| < 1$（也称Rollet条件）是判断放大器是否无条件稳定的标准。若不满足无条件稳定条件，则存在某些源阻抗或负载阻抗使放大器振荡。在振荡器设计中，故意让电路工作在非无条件稳定区域，以激发振荡。

### Gain Circles | 增益圆

For a potentially unstable device, constant-gain circles can be drawn on the Smith chart showing loci of $\Gamma_L$ that yield a given available power gain $G_a$:

$$
\frac{|S_{21}|^2(1 - |\Gamma_S|^2)}{|(1 - S_{11}\Gamma_S)(1 - S_{22}\Gamma_L - S_{11}S_{22}\Gamma_S + S_{12}S_{21}\Gamma_S\Gamma_L)|^2}
$$

> **（中文）** 增益圆是在Smith圆图上绘制的一族等增益轨迹，用于图解法设计放大器的输入/输出匹配网络。在特定频率下，给定$\Gamma_S$即可预测$\Gamma_L$使得电路达到特定增益。

---

## 2.7 Analysis of Nonlinear Dynamic Systems | 非线性动态系统分析

### 2.7.1 Basic Considerations | 基本考量

At RF frequencies, circuits exhibit *dynamic* nonlinear behavior — the output depends not only on the instantaneous input but also on past inputs (memory effects).

Memory effects arise from:
1. **Frequency-dependent nonlinearities** — device capacitances that vary with bias
2. **Time-constant related effects** — $RC$ filtering of nonlinear currents

> **（中文）** 传统的泰勒级数方法（$y(t) = \alpha_1 x(t) + \alpha_2 x^2(t) + \alpha_3 x^3(t)$）假设系统是"静态"的——输出仅取决于当前输入。但射频电路中存在大量记忆效应：结电容、封装寄生、偏置网络等形成低通或带通网络，使非线性电流被"滤波"，导致输出与输入历史相关。

---

## 2.8 Volterra Series | Volterra级数

The Volterra series extends Taylor series to include memory effects:

$$
y(t) = \sum_{n=1}^{\infty} y_n(t) \quad \text{(2.151)}
$$

where each term $y_n(t)$ is an $n$-th order convolution:

$$
y_n(t) = \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} h_n(\tau_1, \ldots, \tau_n) \prod_{i=1}^{n} x(t - \tau_i) \ d\tau_1 \cdots d\tau_n \quad \text{(2.152)}
$$

$h_n(\tau_1, \ldots, \tau_n)$ is the $n$-th order *Volterra kernel* — the multi-dimensional impulse response.

> **（中文）** Volterra级数是处理弱非线性动态系统的标准工具。它将线性系统的冲激响应概念推广到多维，核函数$h_n(\tau_1, \ldots, \tau_n)$完全描述了$n$阶非线性记忆效应。当$n=1$时，Volterra级数退化为标准的线性卷积。Volterra级数在分析RF电路的互调失真、交叉调制等动态非线性效应时非常有用。

### Method of Nonlinear Currents | 非线性电流法

The method of nonlinear currents (also called "device-level Volterra series") computes the response at each frequency by:

1. Computing the nonlinear currents generated at each order
2. Passing each order's current through the linear network's transfer function
3. Superimposing all orders

For a MOSFET with nonlinear transconductance $g_m(v_{gs})$ and gate-source capacitance $C_{gs}(v_{gs})$:

**First-order (linear)**: $i_1(t) = g_m v_{gs,1}(t)$

**Third-order (IM3)**: involves products like $v_{gs}^3(t)$ filtered by $C_{gs}$ and $g_m$ nonlinearities

> **（中文）** 非线性电流法是分析RF电路中互调失真的系统方法。它将非线性器件视为一个线性网络叠加了非线性电流源，然后分别求解每个阶次的响应。这一方法在分析LNA、MIXER等射频电路的IP3时非常有效。

---

## Key Formulas Summary | 核心公式汇总

| Category | Formula | Eq. No. |
|---|---|---|
| Voltage Gain (dB) | $A_{V,\text{dB}} = 20\log(V_{\text{out}}/V_{\text{in}})$ | (2.1) |
| Power Gain (dB) | $A_{P,\text{dB}} = 10\log(P_{\text{out}}/P_{\text{in}})$ | (2.2) |
| dBm to Voltage | $V_{\text{pp}} = 632\ \text{mV} \times 10^{(P_{\text{dBm}}-0)/20}$ | — |
| Taylor Nonlinear | $y(t) = \alpha_1 x + \alpha_2 x^2 + \alpha_3 x^3$ | (2.57) |
| 1-dB Compression | $A_{\text{1dB}}^2 \approx 0.145|\alpha_1/\alpha_3|$ | (2.71) |
| IM3 Power | $P_{\text{IM3}} = 3P_{\text{in}} - 2IIP3$ | (2.85) |
| Thermal Noise | $\overline{v_n^2} = 4kTRB$ | (2.112) |
| Shot Noise | $\overline{i_n^2} = 2qI_{\text{DC}}B$ | (2.115) |
| MOSFET Thermal | $\overline{i_{n,d}^2} = 4kT\gamma g_m B$ | (2.119) |
| Noise Factor (Friis) | $F_{\text{tot}} = F_1 + (F_2-1)/G_1 + \cdots$ | (2.127) |
| Sensitivity | $P_{\text{min}} = -174 + 10\log B + NF + SNR_{\text{min}}$ | (2.133) |
| SFDR | $\text{SFDR} = \frac{2}{3}(IIP3 - P_{\text{min}})$ | (2.139) |
| Series-to-Parallel | $R_p = R_s(1+Q^2)$ | (2.141) |

---

## Key Takeaways | 本章要点

1. **dB/dBm arithmetic**: Voltage gain uses $20\log$, power gain uses $10\log$. $0\ \text{dBm} \Leftrightarrow 632\ \text{mV}_{pp}$ at $50\ \Omega$.
2. **Time variance** causes self-mixing, DC offsets, and LO leakage — distinct from nonlinearity.
3. **Nonlinear figures of merit**: $P_{\text{1dB}}$, IIP3 (or OIP3), IP2. IM3 products grow at $3\ \text{dB/dB}$ slope with input power.
4. **Front-end dominates**: First stage's NF and IIP3 determine overall system performance.
5. **Noise**: Thermal noise ($\overline{v_n^2} = 4kTRB$), shot noise ($2qI_{\text{DC}}B$), flicker noise ($K/(WLC_{\text{ox}}f)$). Total NF = Friis cascade formula.
6. **SFDR** quantifies the ability to handle both weak and strong interferers simultaneously.
7. **Impedance matching**: $Q$ determines bandwidth; L/π/T networks transform impedance with loss.
8. **S-parameters**: The standard RF network description; $S_{11}/S_{22}$ for matching, $S_{21}$ for gain, $S_{12}$ for isolation.
9. **Volterra series** extends Taylor analysis to include memory effects — essential for RF intermodulation analysis.

---

*Chapter 2 establishes the mathematical and conceptual foundation for all subsequent chapters. A thorough mastery of nonlinear distortion analysis, noise figure theory, and impedance matching is essential before proceeding to specific RF building blocks.*
