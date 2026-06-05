---
title: "Chapter 2 — Time and Frequency Domains"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 2
pages: "72–107"
---

# Ch2: Time and Frequency Domains

> **中英双语版**

## 2.1 The Time Domain | 时域

The **time domain** is the real world — the only domain that actually exists. Key waveform parameters:
**时域**是真实世界——唯一实际存在的域。关键波形参数：

- **Clock period** $T_{\text{clock}}$: time interval to repeat one cycle (nsec) | **时钟周期**：重复一个周期的时间间隔
- **Clock frequency** $F_{\text{clock}} = 1/T_{\text{clock}}$ (GHz when $T$ in nsec) | **时钟频率**
- **Rise time (10–90):** time from 10% to 90% of final voltage | **上升时间（10–90）：** 从最终电压的 10% 到 90% 的时间
- **Rise time (20–80):** time from 20% to 80% (used in some IBIS models) | **上升时间（20–80）：** 用于某些 IBIS 模型
- **Fall time:** typically slightly shorter than rise time (CMOS n-channel turns on faster than p-channel)
  **下降时间：** 通常略短于上升时间（CMOS n 沟道开关速度快于 p 沟道）

> **Engineering Intuition:** Signal integrity problems are more likely on falling edges because n-channel transistors switch faster than p-channel, creating sharper edges.
> **工程直觉：** 信号完整性问题更可能发生在下降沿，因为 n 沟道晶体管比 p 沟道开关更快，产生更陡的边沿。

## 2.2 Sine Waves in the Frequency Domain | 频域中的正弦波

The **frequency domain** is a mathematical construct — not real. The only waveforms that exist there are **sine waves**.
**频域**是一种数学构造——不是真实的。那里存在的唯一波形是**正弦波**。

Why sine waves? Four key properties:
为什么用正弦波？四个关键性质：
1. Any time-domain waveform can be completely and uniquely described by combinations of sine waves（任何时域波形都可以用正弦波组合完整且唯一地描述）
2. Sine waves of different frequencies are **orthogonal** (cross-product integrates to zero)（不同频率的正弦波是**正交**的，交叉乘积积分为零）
3. Well-defined mathematically（数学上定义完备）
4. No infinities anywhere (real-world compatible)（无无穷大，与现实世界兼容）

> **Engineering Intuition:** We use the frequency domain NOT because it's more real, but because it sometimes gets us to an acceptable answer **faster** — especially for problems involving R, L, C circuits where sine waves are the natural solution to the differential equations.
> **工程直觉：** 我们使用频域并非因为它更真实，而是因为它有时能**更快**地得到可接受的答案——尤其对于涉及 R、L、C 电路的问题，正弦波是微分方程的天然解。

## 2.3 Sine Wave Features | 正弦波的特征

A sine wave is fully described by three terms:
一个正弦波由三个参数完全描述：
- **Frequency** $f$ (Hz) or **angular frequency** $\omega = 2\pi f$ (rad/s) | **频率**或**角频率**
- **Amplitude** $A$ (peak value) | **幅度**（峰值）
- **Phase** $\phi$ (radians or degrees) | **相位**（弧度或度）

In the time domain, a sine wave requires thousands of data points. In the frequency domain, it's a **single point** (amplitude vs. frequency).
在时域中，一个正弦波需要数千个数据点；在频域中，它只是一个**单点**（幅度 vs. 频率）。

The collection of amplitudes at all frequencies is called the **spectrum**.
所有频率下的幅度集合称为**频谱**。

## 2.4 The Fourier Transform | 傅里叶变换

Converts time-domain waveforms into frequency-domain spectra. Three types:
将时域波形转换为频域频谱。三种类型：

| Type | Use Case | 用途 |
|:--|:--|:--|
| **Fourier Integral (FI)** | Ideal mathematical waveforms, continuous time → continuous frequency | 理想数学波形 |
| **Discrete Fourier Transform (DFT)** | Real measured waveforms, discrete time → discrete frequency | 实测波形 |
| **Fast Fourier Transform (FFT)** | Same as DFT but requires $N = 2^k$ points; 100–10,000× faster | 与 DFT 相同，但快 100–10000 倍 |

Tools: SPICE `.FOUR` command, Microsoft Excel FFT, Python `numpy.fft`.

## 2.5 Spectrum of a Repetitive Signal | 重复信号的频谱

For a DFT, a waveform must be **repetitive** (period $T$, repeat frequency $F = 1/T$). The spectrum contains only **harmonics** — multiples of $F$:
对于 DFT，波形必须是**重复**的（周期 $T$，重复频率 $F = 1/T$）。频谱只包含**谐波**——频率为 $F$ 的整数倍：

- **First harmonic** = $F$（一次谐波）
- **$n$-th harmonic** = $n \times F$（$n$ 次谐波）
- **Zeroth harmonic** = DC average value（零次谐波 = 直流平均值）

> **Engineering Intuition:** Any arbitrary waveform can be made "repetitive" by repeating the measurement window. Choose the period equal to the clock period for easiest interpretation.
> **工程直觉：** 任何任意波形都可以通过重复测量窗口变为"重复"波形。选择周期等于时钟周期以便于解释。

## 2.6 Spectrum of an Ideal Square Wave | 理想方波的频谱

For a 50% duty-cycle, 0-to-1 V ideal square wave (zero rise time):
对于 50% 占空比、0 到 1V 的理想方波（零上升时间）：

- **Even harmonics** = 0 (all zero amplitude)（**偶次谐波** = 0）
- **Odd harmonics:** $A_n = \dfrac{2}{\pi \cdot n}$（奇次谐波）
- **DC offset (zeroth harmonic):** 0.5 V（直流偏移）

| Harmonic $n$ | Frequency | Amplitude | 幅度 |
|:--:|:--:|:--:|:--:|
| 1 | $F$ | 0.637 V | 基波 |
| 3 | $3F$ | 0.212 V | 三次谐波 |
| 5 | $5F$ | 0.127 V | 五次谐波 |
| 7 | $7F$ | 0.091 V | 七次谐波 |
| $\infty$ | $\infty F$ | 0 | 无穷远 |

Amplitudes decrease as $1/f$. Infinite bandwidth is required for zero rise time.
幅度按 $1/f$ 衰减。零上升时间需要无穷大带宽。

## 2.7 Effect of Bandwidth on Rise Time | 带宽对上升时间的影响

**Bandwidth ($BW$):** the highest sine-wave-frequency component that is significant in the spectrum.
**带宽（$BW$）：** 频谱中有意义的最高的正弦波频率分量。

Adding more harmonics (higher bandwidth) produces a shorter rise time. Removing high-frequency components (lower bandwidth) increases rise time.
增加更多谐波（更高带宽）产生更短的上升时间。移除高频分量（更低带宽）增大上升时间。

> **Engineering Intuition:** This is why lossy transmission lines degrade rise time — they attenuate high frequencies more than low frequencies. A 36-inch FR4 trace can degrade 50 psec rise time to 1.5 nsec.
> **工程直觉：** 这就是有损传输线为什么会使上升时间退化——它们对高频的衰减比对低频更大。36 英寸的 FR4 走线可以将 50 ps 上升时间退化为 1.5 ns。

### Key Relationship: Bandwidth and Rise Time | 关键关系：带宽与上升时间

$$
BW = \frac{0.35}{RT}
$$

where:
- $BW$ = bandwidth (GHz) | 带宽（GHz）
- $RT$ = 10–90 rise time (nsec) | 10–90 上升时间（ns）

| $RT$ | $BW$ |
|:--:|:--:|
| 10 nsec | 35 MHz |
| 1 nsec | 350 MHz |
| 100 psec | 3.5 GHz |
| 50 psec | 7 GHz |
| 10 psec | 35 GHz |

> **Engineering Intuition:** This is one of the most useful rules of thumb in signal integrity. When $RT$ is in nsec, $BW$ is in GHz. When $RT$ is in $\mu$sec, $BW$ is in MHz.
> **工程直觉：** 这是信号完整性中最有用的经验法则之一。$RT$ 以 ns 为单位时，$BW$ 以 GHz 为单位；$RT$ 以 μs 为单位时，$BW$ 以 MHz 为单位。

## 2.8 What Does "Significant" Mean? | "有意义"意味着什么？

**Significant** = when the harmonic amplitude is still >70% of an ideal square wave's amplitude at the same harmonic. Alternatively: the frequency at which harmonic amplitudes drop off faster than $1/f$ — this is the **knee frequency**.
**有意义** = 谐波幅度仍大于同次理想方波谐波幅度的 70%。或者说：谐波幅度开始比 $1/f$ 更快衰减的频率——这就是**膝点频率**。

For a real trapezoidal waveform (finite rise time), harmonics above $BW = 0.35/RT$ contribute <70% of the ideal square wave's amplitude and can be ignored.
对于真实的梯形波（有限上升时间），高于 $BW = 0.35/RT$ 的谐波贡献小于理想方波幅度的 70%，可以忽略。

> **Engineering Intuition:** "Bandwidth" is inherently an approximation — a rule of thumb. If you need 900 MHz vs. 950 MHz precision, use the full spectrum instead.
> **工程直觉：** "带宽"本质上是近似值——一个经验法则。如需区分 900 MHz 与 950 MHz 的精度，请使用全频谱。

## 2.9 Bandwidth and Clock Frequency | 带宽与时钟频率

For most microprocessor-based systems, the rise time is approximately **7% of the clock period**. This yields:
对于大多数基于微处理器的系统，上升时间约为**时钟周期的 7%**。由此可得：

$$
BW_{\text{clock}} \approx 5 \times F_{\text{clock}}
$$

| $F_{\text{clock}}$ | $RT$ (7% of period) | $BW$ |
|:--:|:--:|:--:|
| 10 MHz | 7 nsec | 50 MHz |
| 100 MHz | 0.7 nsec | 500 MHz |
| 1 GHz | 70 psec | 5 GHz |

**WARNING:** This is a generalization. Different waveforms with the **same** clock frequency can have very different rise times and bandwidths (Fig 2-14). Always use rise time directly when available.
**注意：** 这是一个泛化结论。**相同**时钟频率的不同波形可能具有非常不同的上升时间和带宽。尽可能直接使用上升时间。

> **Engineering Intuition:** An OK answer now is often more valuable than a perfect answer late. But never use this approximation for design sign-off.
> **工程直觉：** 一个及时的尚可答案往往比一个完美的迟到答案更有价值。但切勿将此近似用于设计签核。

## 2.10 Bandwidth of a Measurement | 测量的带宽

The **measurement bandwidth** is the highest frequency with significant accuracy:
**测量带宽**是具有可接受精度的最高频率：
- **VNA / Impedance Analyzer:** straightforward — it's the max frequency of the instrument（直接——就是仪器的最高频率）
- **TDR:** $BW_{\text{meas}} \approx 0.35 / RT_{\text{step}}$ (rise time of the launched step)（阶跃脉冲的上升时间决定）

State-of-the-art TDRs can achieve 3–5× the signal bandwidth through calibration (up to ~30 GHz).
最先进的 TDR 可通过校准达到信号带宽的 3–5 倍（高达约 30 GHz）。

## 2.11 Bandwidth of a Model | 模型的带宽

The **model bandwidth** is the highest frequency where the model accurately predicts behavior. Only verifiable by comparison to measurement.
**模型带宽**是模型能准确预测行为的最高频率。只有通过与测量比较来验证。

**Example:** A 300-mil wire bond over a plane:
**示例：** 平面上方 300 mil 的键合线：
- **1st-order model** (R + L): $BW \approx 2$ GHz（一阶模型，R+L）
- **2nd-order model** (R + L + C): $BW \approx 4$ GHz（二阶模型，R+L+C）

## 2.12 Bandwidth of an Interconnect | 互连的带宽

The **3-dB bandwidth** of an interconnect: the frequency at which transmitted amplitude drops to 70% ($-3$ dB) of the incident value.
互连的 **3-dB 带宽**：传输幅度下降到入射值 70%（-3 dB）时的频率。

**Intrinsic rise time** of an interconnect:
互连的**本征上升时间**：
$$
RT_{\text{interconnect}} \approx \frac{0.35}{BW_{\text{interconnect}}}
$$

**Combined rise time** (Gaussian approximation):
**组合上升时间**（高斯近似）：
$$
RT_{\text{out}} = \sqrt{RT_{\text{in}}^2 + RT_{\text{interconnect}}^2}
$$

| Condition | Impact | 影响 |
|:--|:--|:--|
| $RT_{\text{interconnect}} < 0.5 \times RT_{\text{in}}$ | <10% rise time increase (negligible) | 上升时间增加 <10%，可忽略 |
| $RT_{\text{interconnect}} \approx RT_{\text{in}}$ | ~40% rise time increase (significant) | 上升时间增加约 40%，显著 |

> **Engineering Intuition:** To support a 1-GHz bandwidth signal, the interconnect bandwidth should be at least 2 GHz (factor of 2 margin).
> **工程直觉：** 要支持 1 GHz 带宽的信号，互连带宽应至少 2 GHz（2 倍裕量）。

## 2.13 Key Formulas | 关键公式

| Formula | Description | 中文说明 |
|:--|:--|:--|
| $F = 1/T$ | Clock frequency from period | 由周期得时钟频率 |
| $\omega = 2\pi f$ | Angular frequency | 角频率 |
| $A_n = 2/(\pi n)$ (odd $n$) | Ideal square wave harmonic amplitudes | 理想方波谐波幅度 |
| $BW = 0.35/RT$ | Signal bandwidth from rise time | 由上升时间得信号带宽 |
| $BW_{\text{clock}} \approx 5 \times F_{\text{clock}}$ | Clock bandwidth estimate | 时钟带宽估计 |
| $RT_{\text{out}} = \sqrt{RT_{\text{in}}^2 + RT_{\text{ic}}^2}$ | Rise time through interconnect | 通过互连的上升时间 |

## 2.14 Key Rules of Thumb | 关键经验法则

1. **Rise time ~7% of clock period** for typical microprocessor systems（典型微处理器系统中上升时间约时钟周期的 7%）
2. **Bandwidth = 0.35 / rise time** (single most useful SI rule)（带宽 = 0.35 / 上升时间，SI 中最有用的单条法则）
3. **Clock bandwidth ≈ 5× clock frequency** (when rise time is 7% of period)（时钟带宽约 5 倍时钟频率）
4. **Interconnect BW should be ≥ 2× signal BW** for minimal degradation（互连带宽应 ≥ 2 倍信号带宽以最小化退化）
5. **Interconnect intrinsic RT should be ≤ 50% of signal RT** for <10% degradation（互连本征 RT ≤ 信号 RT 的 50% 以保持退化 <10%）
6. **-3 dB = 70% amplitude** (definition of significant in interconnects)（-3 dB = 70% 幅度，互连中"有意义"的定义）
