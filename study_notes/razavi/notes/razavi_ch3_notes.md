---
chapter: 3
title: Communication Concepts
source: Behzad Razavi, RF Microelectronics, 2nd Edition, McGraw-Hill, 2012
pages: 91-152
---

# Chapter 3: Communication Concepts
# 第三章：通信概念

> *"Understanding modulation methods, spectral efficiency, and multiple access techniques is essential to appreciating the trade-offs in RF transceiver design."*
>
> **（中文）** 本章系统梳理射频通信系统的核心概念：调制方式（模拟与数字）、频谱效率、多址接入技术以及主流无线标准。这些知识是理解后续章节（收发机架构、低噪声放大器、混频器、频率合成器等）的关键背景。

---

## 3.1 General Considerations | 一般性考量

### Why Modulation? | 为什么要调制？

A communication system must transmit *information* (voice, data, video) over a *channel* (wireless, fiber, copper). Three fundamental requirements drive modulation:

1. **Spectral Efficiency**: Place the information signal at a frequency where the antenna is efficient ($l \approx \lambda/10$ to $\lambda/20$ for reasonable radiation efficiency).
   - A $\lambda/4$ antenna at $f_c = 1\ \text{MHz}$ has length $\approx 75\ \text{m}$ — impractical for mobile devices.
   - At $f_c = 2\ \text{GHz}$, $\lambda/4 \approx 3.75\ \text{cm}$ — manageable.

2. **Channel Allocation**: Regulatory bodies allocate specific frequency bands to services. Modulation allows multiple users to share the spectrum via frequency-division.

3. **Interference Rejection**: Modulation to high frequencies allows the use of narrowband filters to suppress adjacent-channel interference.

> **（中文）** 低频信号（如基带音频$20\ \text{Hz}-20\ \text{kHz}$）的天线尺寸巨大（$\lambda/4$在$1\ \text{kHz}$时约为$75\ \text{km}$！），无法高效辐射。调制将信息"搬运"到射频载波上，使天线尺寸可行，同时允许多用户共享频谱。

### RF Communication Chain | 射频通信链路

```
[Information] → [Modulator] → [Upconverter: 0 → f_c] → [PA] → [Antenna]
                                                                         ↓
[Reconstructed] ← [Demodulator] ← [Downconverter: f_c → 0] ← [LNA] ← [Antenna]
```

> **（中文）** 发射路径：基带信息先经调制（常用正交调制，I/Q），再上变频至载波$f_c$，经功率放大器（PA）放大后由天线辐射。接收路径：天线接收的微弱信号经低噪声放大器（LNA）放大后，下变频至基带进行解调。

---

## 3.2 Analog Modulation | 模拟调制

### 3.2.1 Amplitude Modulation | 幅度调制

#### Standard AM (Double-Sideband Full Carrier) | 标准调幅（双边带全载波）

The carrier is modulated by the message signal $m(t)$:

$$
x_{\text{AM}}(t) = [A_c + m(t)]\cos\omega_c t \quad \text{(3.1)}
$$

where $A_c$ is the carrier amplitude, $m(t)$ is the baseband message.

**Modulation Index $\mu$:**

$$
\mu = \frac{|m(t)|_{\max}}{A_c} \quad \text{(3.2)}
$$

For no overmodulation: $0 \le \mu \le 1$.

**Spectrum of AM:**

$$
X_{\text{AM}}(\omega) = \pi A_c[\delta(\omega - \omega_c) + \delta(\omega + \omega_c)] + \frac{1}{2}[M(\omega - \omega_c) + M(\omega + \omega_c)] \quad \text{(3.3)}
$$

Total transmitted power:

$$
P_{\text{AM}} = \frac{A_c^2}{2} + \frac{\overline{m^2(t)}}{2} = P_c\left(1 + \frac{\mu^2}{2}\right) \quad \text{(3.4)}
$$

where $P_c = A_c^2/2$ is the carrier power.

> **（中文）** 标准AM的频谱包含载波分量（不携带信息）+ 上、下两个边带（携带信息）。载波功率占总功率的大部分但不含信息，这是标准AM效率低下的根本原因（理论效率上限仅$1/3$）。因此通信系统几乎不使用标准AM，而采用抑制载波的调制方式。

#### Double-Sideband Suppressed Carrier (DSB-SC) | 双边带抑制载波

$$
x_{\text{DSB}}(t) = m(t)\cos\omega_c t \quad \text{(3.5)}
$$

- No carrier power → higher efficiency
- Requires coherent (synchronous) demodulation at receiver
- Spectrum: upper and lower sidebands only

#### Single-Sideband (SSB) | 单边带

Filtered DSB-SC, retaining only one sideband:

$$
x_{\text{SSB}}(t) = m(t)\cos\omega_c t \pm \hat{m}(t)\sin\omega_c t \quad \text{(3.6)}
$$

where $\hat{m}(t)$ is the Hilbert transform of $m(t)$.

> **（中文）** SSB是频谱效率最高的模拟调制方式之一，仅传输一个边带（另一半是冗余的，因为下边带是上边带的镜像）。SSB广泛应用于短波通信和军事通信，但接收机需要精确的载波恢复电路。

### 3.2.2 Phase and Frequency Modulation | 相位调制与频率调制

#### Phase Modulation (PM) | 相位调制

$$
x_{\text{PM}}(t) = A_c\cos[\omega_c t + \phi(t)] \quad \text{(3.7)}
$$

where $\phi(t) = k_p m(t)$ is the instantaneous phase deviation, $k_p$ is the phase sensitivity.

#### Frequency Modulation (FM) | 频率调制

$$
x_{\text{FM}}(t) = A_c\cos\left[\omega_c t + k_f \int_{-\infty}^{t} m(\tau)d\tau\right] \quad \text{(3.8)}
$$

Instantaneous frequency:

$$
\omega_i(t) = \frac{d}{dt}[\omega_c t + \phi(t)] = \omega_c + k_f m(t) \quad \text{(3.9)}
$$

**Frequency Deviation $\Delta f$:**

$$
\Delta f = k_f |m(t)|_{\max} \quad \text{(3.10)}
$$

**Carson's Rule — FM Bandwidth:**

$$
B_{\text{FM}} \approx 2(\Delta f + f_m) \quad \text{(3.11)}
$$

where $f_m$ is the maximum baseband frequency.

**Example — FM for FM Radio:**
- $f_c = 88\ \text{MHz} - 108\ \text{MHz}$ (US)
- $\Delta f = 75\ \text{kHz}$ (maximum deviation)
- $f_m = 15\ \text{kHz}$ (audio)
- $B \approx 2(75 + 15) = 180\ \text{kHz}$

> **（中文）** FM与PM本质上是同一类调制（角度调制）的两种形式：PM的相位正比于$m(t)$，FM的相位正比于$m(t)$的积分，频率正比于$m(t)$本身。FM的优势在于其恒包络特性——峰值功率等于平均功率，功放效率高，且抗幅度噪声能力强。FM广播是角度调制最成功的商业应用。

#### Narrowband FM vs. Wideband FM | 窄带FM与宽带FM

**Narrowband FM** ($\Delta f \ll f_c$): FM can be approximated as:

$$
x_{\text{NBFM}}(t) \approx A_c\cos\omega_c t - A_c k_f\left[\int m(\tau)d\tau\right]\sin\omega_c t \quad \text{(3.12)}
$$

Bandwidth: $B \approx 2f_m$

**Wideband FM**: Carson's rule applies; large $\Delta f$ yields large bandwidth.

---

## 3.3 Digital Modulation | 数字调制

### Why Digital Modulation? | 为什么要数字调制？

| Advantage | Explanation |
|---|---|
| **Error correction** | FEC codes can detect and correct errors |
| **Compression** | Shannon's source coding theorem enables efficient data representation |
| **Encryption** | Easy to implement secure communication |
| **Regenerative repeaters** | Noise does not accumulate in digital links |
| **Flexibility** | Software-defined radio adapts modulation to channel conditions |

> **（中文）** 数字调制相比模拟调制具有显著优势：前向纠错（FEC）可以在接收端检测和纠正错误；信源编码（压缩）提高信息效率；加密易于实现；中继器可再生数字信号而不累积噪声。正是这些优势，使得现代无线通信系统（4G LTE, 5G NR, WiFi 6）全面采用数字调制技术。

### 3.3.1 Intersymbol Interference (ISI) | 符号间干扰

#### Nyquist Criterion for Zero ISI | 零ISI的奈奎斯特准则

For a symbol rate $R_s$ [symbols/sec], the minimum bandwidth (Nyquist bandwidth) is:

$$
B_{\min} = \frac{R_s}{2} \quad \text{(for baseband, both-sided)} \quad \text{(3.13)}
$$

Or equivalently, the symbol period $T_s = 1/R_s$.

A pulse shape $p(t)$ satisfies the **Nyquist zero-ISI criterion** if:

$$
p(nT_s) = \begin{cases} 1 & n = 0 \\ 0 & n \neq 0 \end{cases} \quad \text{(3.14)}
$$

The **raised cosine** roll-off spectrum is commonly used:

$$
P(f) = \begin{cases}
T_s, & |f| \le \frac{1-\alpha}{2T_s} \\
\frac{T_s}{2}\left[1 + \cos\frac{\pi T_s}{\alpha}\left(|f| - \frac{1-\alpha}{2T_s}\right)\right], & \frac{1-\alpha}{2T_s} < |f| \le \frac{1+\alpha}{2T_s} \\
0, & |f| > \frac{1+\alpha}{2T_s}
\end{cases} \quad \text{(3.15)}
$$

where $\alpha \in [0,1]$ is the *roll-off factor* (spectral efficiency trade-off).

> **（中文）** 奈奎斯特零ISI准则是数字通信的基础：脉冲响应在$t = nT_s$（$n \neq 0$）处必须为零，确保相邻符号不在采样点相互干扰。升余弦滚降滤波在实际系统中广泛使用，滚降因子$\alpha$越大（带宽越宽），时域脉冲越接近理想 sinc 函数，但频谱效率越低。

### 3.3.2 Signal Constellations | 信号星座图

Digital modulation maps bits to symbols in the I/Q (complex envelope) plane.

#### Key Constellations | 关键星座图

| Modulation | Bits/Symbol | Symbol Energy $E_s$ | Peak-to-Average Ratio |
|---|---|---|---|
| BPSK | 1 | $2E_b$ (normalized) | $1$ (constant) |
| QPSK (4-QAM) | 2 | $2E_b$ | $1$ (constant) |
| 16-QAM | 4 | $10E_b/4$ (normalized) | $\approx 2.55$ |
| 64-QAM | 6 | $42E_b/6$ (normalized) | $\approx 3.68$ |

**QPSK (Quaternary PSK):**

$$
s(t) = \sqrt{E_s}\left[I(t)\cos\omega_c t - Q(t)\sin\omega_c t\right] \quad \text{(3.16)}
$$

with $I, Q \in \{+1, -1\}$.

> **（中文）** 星座图是设计数字调制方案的核心工具。在I/Q平面中，每个点代表一个符号（若干比特）。QPSK的4个星座点构成正方形，8-PSK的8个点均匀分布在单位圆上。16-QAM的16个点形成$4\times4$网格，提供4比特/符号。阶数越高，频谱效率越高，但对信噪比（SNR）的要求也越高。

**Bit Error Rate (BER) Approximations:**

| Modulation | Coherent BPSK | QPSK | 16-QAM | 64-QAM |
|---|---|---|---|---|
| BER (approx.) | $Q(\sqrt{2E_b/N_0})$ | $Q(\sqrt{2E_b/N_0})$ | $\approx 3Q(\sqrt{0.4E_b/N_0})$ | $\approx 7Q(\sqrt{E_b/21N_0})$ |

where $Q(x) = \frac{1}{\sqrt{2\pi}}\int_x^\infty e^{-t^2/2}dt$.

> **（中文）** 误码率（BER）是衡量数字调制性能的核心指标。在AWGN信道下，BPSK和QPSK具有相同的每比特能量与噪声功率谱密度比$E_b/N_0$时的BER性能（$Q(\sqrt{2E_b/N_0})$）。高阶QAM（16/64/256）的BER性能随$E_b/N_0$恶化而急剧下降，因为星座点之间的欧氏距离减小。

### 3.3.3 Quadrature Modulation | 正交调制

Quadrature modulation uses two carriers in quadrature ($\cos\omega_c t$ and $\sin\omega_c t$):

$$
s(t) = I(t)\cos\omega_c t - Q(t)\sin\omega_c t = \text{Re}\{(I + jQ)e^{j\omega_c t}\} \quad \text{(3.17)}
$$

This is equivalent to sending a complex baseband signal $s_L(t) = I(t) + jQ(t)$ upconverted by $e^{j\omega_c t}$.

**Complex Envelope / Lowpass Equivalent:**

$$
s_L(t) = I(t) + jQ(t) \quad \text{(3.18)}
$$

**Power of the Passband Signal:**

$$
P = \frac{1}{2}\mathbb{E}[|s_L(t)|^2] = \frac{1}{2}(P_I + P_Q) \quad \text{(3.19)}
$$

> **（中文）** 正交调制（I/Q调制）是现代射频通信系统的基石。它将基带I路和Q路信号分别与正交的$\cos\omega_c t$和$\sin\omega_c t$相乘后相加。从复数角度看，等效于将复基带信号$s_L(t) = I + jQ$乘以上变频因子$e^{j\omega_c t}$。接收端通过解调（与$\cos\omega_c t$和$\sin\omega_c t$相乘后低通滤波）恢复I/Q。

#### Offset QPSK (OQPSK) | 偏移QPSK

OQPSK offsets the Q channel by $T_s/2$ relative to I channel, preventing phase transitions of $180^\circ$ (which cause high envelope fluctuations).

> **（中文）** OQPSK将Q路延迟半个符号周期$T_s/2$，使I路和Q路永远不会同时跳变，从而将最大相位跳变从$180^\circ$降低到$90^\circ$。这减少了PA的包络波动（Peak-to-Average Ratio），是GSM等系统采用的方案。

#### $\pi/4$-DQPSK | $\pi/4$-差分QPSK

$\pi/4$-DQPSK uses two QPSK constellations rotated by $\pi/4$ relative to each other. The symbol is encoded as the phase difference between successive symbols.

Advantages:
- Maximum phase jump: $135^\circ$ (smaller envelope variation than QPSK)
- Differential encoding → simple non-coherent detection possible

> **（中文）** $\pi/4$-DQPSK采用两套相差$\pi/4$的QPSK星座图交替使用，符号由相邻符号之间的相位差编码。这一方案兼顾了较小的包络波动和差分检测的可行性，是北美IS-136和TETRA等系统的调制方式。

### 3.3.4 GMSK and GFSK Modulation | GMSK与GFSK调制

#### Gaussian Minimum Shift Keying (GMSK) | 高斯最小频移键控

GMSK is a continuous-phase frequency modulation (CPFM) scheme used in GSM:

$$
\theta(t) = 2\pi h \int_{-\infty}^{t} \sum_{k} b_k q(t - kT_s) dt \quad \text{(3.20)}
$$

where $b_k \in \{+1, -1\}$ are the data bits, $q(t)$ is the Gaussian pulse shape, and $h = 0.5$ is the modulation index (minimum spacing for orthogonal signals).

**Gaussian Pulse Shape:**

$$
q(t) = \frac{1}{T_s}\int_{-\infty}^{t} g(\tau)d\tau \quad \text{(3.21)}
$$
$$
g(t) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-t^2/(2\sigma^2)} \quad \text{(3.22)}
$$

where $\sigma = \frac{\sqrt{\ln 2}}{2\pi BT_s}$, $BT_s$ is the bandwidth-time product ($BT_s = 0.3$ for GSM).

**Key Properties of GMSK:**
- Constant envelope (no amplitude modulation) → allows use of Class-C nonlinear PA
- Narrow spectrum (due to Gaussian filtering) → $BT_s = 0.3$ gives excellent spectral containment
- Phase changes are continuous → low sidelobes in frequency domain

> **（中文）** GMSK是GSM系统采用的调制方式。其核心特性：①恒包络——功放可工作在非线性状态（Class-C），效率高；②频谱紧凑——高斯滤波将符号间干扰降到最低，带宽-时间积$BT_s = 0.3$；③调制指数$h = 0.5$（最小频移键控），使两个正交信号在理论上正交。

### 3.3.5 Quadrature Amplitude Modulation (QAM) | 正交幅度调制

QAM combines amplitude and phase modulation:

$$
s(t) = I(t)\cos\omega_c t - Q(t)\sin\omega_c t \quad \text{(3.23)}
$$

where $I, Q$ take $M$ discrete levels (not just binary).

**$M$-QAM Constellations**: $M = 4$ (QPSK), $16$, $64$, $256$, etc.

**Minimum Euclidean Distance:**

For square $M$-QAM ($M = L^2$), the minimum distance:

$$
d_{\min} = \frac{2}{\sqrt{M} - 1} \cdot d_{\max} \quad \text{(3.24)}
$$

where $d_{\max}$ is the maximum distance from origin to a constellation point.

> **（中文）** QAM通过同时调制幅度和相位来提高频谱效率。16-QAM用4级I和4级Q产生16个星座点（4比特/符号），64-QAM用6比特/符号。阶数越高，对线性功放的要求越苛刻（因为包络变化大），对SNR的要求也越高。WiFi (802.11a/g)使用64-QAM，LTE和5G NR使用256-QAM。

### 3.3.6 Orthogonal Frequency Division Multiplexing (OFDM) | 正交频分复用

OFDM divides the available bandwidth $B$ into $N$ orthogonal subcarriers:

$$
x(t) = \sum_{k=0}^{N-1} s_k(t) \cdot e^{j2\pi k \Delta f t} \quad \text{(3.25)}
$$

where $\Delta f = B/N$ is the subcarrier spacing, $s_k(t)$ is the symbol on subcarrier $k$.

**Key Property — Orthogonality:**

$$
\frac{1}{T_s}\int_0^{T_s} e^{j2\pi (m-n)\Delta f t}dt = \begin{cases} 1 & m = n \\ 0 & m \neq n \end{cases} \quad \text{(3.26)}
$$

**OFDM Symbol Duration $T_s$:**

$$
T_s = T_{\text{FFT}} + T_{\text{GI}} = \frac{N}{\Delta f \cdot N} + T_{\text{GI}} = \frac{1}{\Delta f} + T_{\text{GI}} \quad \text{(3.27)}
$$

where $T_{\text{GI}}$ is the guard interval (cyclic prefix).

> **（中文）** OFDM是现代宽带无线系统的核心技术。其核心思想：将宽信道划分为$N$个窄带正交子载波，每个子载波上独立进行低符号率调制（QPSK、16/64/256-QAM），然后叠加发送。正交性通过FFT/IFFT实现。循环前缀（CP）作为保护间隔，吸收多径延迟扩展，防止符号间干扰。LTE使用$N = 2048$，子载波间隔$\Delta f = 15\ \text{kHz}$；5G NR支持$15\ \text{kHz}$和$30\ \text{kHz}$两种子载波间隔。

**OFDM Advantages:**
1. **Robust to multipath**: Long symbol period $T_s \gg \tau_{\text{rms}}$ (rms delay spread)
2. **Simple equalization**: One-tap per subcarrier (no complex time-domain equalizer)
3. **Spectral efficiency**: Subcarriers pack tightly (no guard bands needed due to orthogonality)

**OFDM Challenges:**
1. **High PAPR**: Peak-to-Average Power Ratio can be $> 10\ \text{dB}$ → requires linear PA
2. **Frequency offset sensitivity**: Subcarrier orthogonality is destroyed by frequency error $\Delta f_{\text{err}}$ → requires accurate frequency synchronization
3. **Phase noise sensitivity**: LO phase noise rotates constellation → ICI (inter-carrier interference)

> **（中文）** OFDM的高峰均功率比（PAPR）是射频设计的重大挑战。PAPR $> 10\ \text{dB}$意味着PA必须有很大的输出功率回退（output backoff）才能维持线性，导致效率极低。这是5G NR和WiFi 6系统中功放效率远低于理论值的主要原因。数字预失真（DPD）和包络跟踪（Envelope Tracking）是应对这一挑战的主流技术。

---

## 3.4 Spectral Efficiency | 频谱效率

### Spectral Efficiency $\eta$ | 频谱效率$\eta$

$$
\eta = \frac{R_b}{B} = \frac{\text{bits/sec}}{\text{Hz}} \quad \text{(3.28)}
$$

where $R_b$ is the data rate and $B$ is the occupied bandwidth.

**Shannon's Capacity (AWGN Channel):**

$$
C = B\log_2\left(1 + \frac{S}{N}\right) = B\log_2\left(1 + \frac{E_b}{N_0}\right) \quad \text{(3.29)}
$$

Rearranging for minimum $E_b/N_0$:

$$
\frac{E_b}{N_0} = 2^{\eta} - 1 \quad \text{(3.30)}
$$

This sets the theoretical minimum energy per bit for reliable communication at spectral efficiency $\eta$.

| Modulation | $\eta$ [bits/sec/Hz] | Min $E_b/N_0$ [dB] |
|---|---|---|
| BPSK | 1 | $1.76$ |
| QPSK | 2 | $3.76$ |
| 16-QAM | 4 | $9.54$ |
| 64-QAM | 6 | $14.54$ |
| 256-QAM | 8 | $18.54$ |

> **（中文）** 香农容量公式是数字通信的理论极限。它表明：频谱效率$\eta$越高（更密集的调制），所需的最小$E_b/N_0$越大。例如，64-QAM的理论最小$E_b/N_0$约为$14.54\ \text{dB}$，而实际系统还需要额外的$5-10\ \text{dB}$余量来应对实现损耗和非理想信道。

---

## 3.5 Multiple Access Techniques | 多址接入技术

### FDMA — Frequency Division Multiple Access | 频分多址

Each user is assigned a dedicated frequency channel (bandwidth $B_i$) for the duration of the call.

| Feature | Value |
|---|---|
| Channel bandwidth (GSM) | $200\ \text{kHz}$ |
| Total spectrum (GSM 900) | $25\ \text{MHz}$ per operator |
| Duplex scheme | FDD (separate TX/RX bands) |

> **（中文）** FDMA是早期蜂窝系统（如AMPS、NMT）采用的多址方式。每个用户独占一个信道，优点是简单，缺点是频谱利用率低（信道利用率不高时浪费严重）。

### TDMA — Time Division Multiple Access | 时分多址

Users share a frequency channel but transmit in assigned time slots.

| Feature | GSM | IS-136 (TDMA) |
|---|---|---|
| Time slots per carrier | 8 | 3 |
| Frame duration | $4.615\ \text{ms}$ | $40\ \text{ms}$ |
| Time slot duration | $577\ \mu\text{s}$ | $6.67\ \text{ms}$ |
| Modulation | GMSK | $\pi/4$-DQPSK |

> **（中文）** TDMA将时间划分为帧（Frame）和时隙（Time Slot），每个用户在分配的时隙中发送。GSM每帧$4.615\ \text{ms}$包含8个时隙，每个时隙$577\ \mu\text{s}$，时隙之间需要保护时间以防止碰撞。TDMA允许一个载波服务多个用户，提高了频谱利用率。

### CDMA — Code Division Multiple Access | 码分多址

All users transmit simultaneously in the same frequency band, distinguished by unique *spreading codes* (pseudo-noise sequences).

**Spreading Factor $SF$**: The ratio of chip rate to data rate:

$$
SF = \frac{R_c}{R_b} \quad \text{(3.31)}
$$

**Processing Gain $G_p$** (in dB):

$$
G_p = 10\log_{10} SF \quad \text{(3.32)}
$$

**Spreading Spectrum Signal:**

$$
s(t) = \sum_{k} b_k p(t - kT_c) \quad \text{(3.33)}
$$

where $p(t)$ is the chip pulse (duration $T_c$), $b_k$ is the spreading code chip.

**Near-Far Problem**: A strong nearby user can drown out a weak distant user (self-jamming). Requires tight power control.

> **（中文）** CDMA利用伪随机扩频码区分用户，所有用户同时同频发送。接收端通过相关检测（与相同扩频码相关）解出目标信号。cdmaOne（IS-95）和3G WCDMA采用CDMA技术。扩频处理增益$G_p$越大，抗干扰能力越强，但数据速率越低。

### OFDMA — Orthogonal Frequency Division Multiple Access | 正交频分多址

OFDMA = OFDM + FDMA: Multiple users share the OFDM bandwidth, each assigned specific subcarriers and time slots.

Used in: WiMAX, LTE (downlink), 5G NR.

---

## 3.6 Wireless Standards | 无线标准

### 3.6.1 GSM (Global System for Mobile Communications) | GSM

| Parameter | GSM 900 (Primary) | DCS 1800 | PCS 1900 |
|---|---|---|---|
| Uplink (TX) | $880-915\ \text{MHz}$ | $1710-1785\ \text{MHz}$ | $1850-1910\ \text{MHz}$ |
| Downlink (RX) | $925-960\ \text{MHz}$ | $1805-1880\ \text{MHz}$ | $1930-1990\ \text{MHz}$ |
| Channel spacing | $200\ \text{kHz}$ | $200\ \text{kHz}$ | $200\ \text{kHz}$ |
| TX power (mobile) | $33\ \text{dBm}$ (max) | $30\ \text{dBm}$ | $30\ \text{dBm}$ |
| Modulation | GMSK ($BT_s = 0.3$) | GMSK | GMSK |
| Speech coding | $13\ \text{kbps}$ (RPE-LTP) | — | — |
| Frame duration | $4.615\ \text{ms}$ | — | — |
| Time slots/frame | 8 | — | — |
| Burst length | $577\ \mu\text{s}$ | — | — |

> **（中文）** GSM是第二代数字蜂窝通信的里程碑。它采用TDMA+FDMA多址方式、GMSK调制、$13\ \text{kbps}$语音编码。GSM的频率规划将$25\ \text{MHz}$带宽（每运营商）划分为$124$个$200\ \text{kHz}$信道，每个载波最多服务8个用户。GSM定义了严格的射频收发机指标：灵敏度$-104\ \text{dBm}$、邻道抑制$>9\ \text{dB}$等。

### 3.6.2 IEEE 802.11b/g (WiFi) | WiFi

| Parameter | 802.11b (DSSS) | 802.11g (OFDM) |
|---|---|---|
| Frequency | $2.4-2.4835\ \text{GHz}$ | $2.4-2.4835\ \text{GHz}$ |
| Channel bandwidth | $22\ \text{MHz}$ | $20\ \text{MHz}$ |
| Data rates | $1, 2, 5.5, 11\ \text{Mbps}$ | $6-54\ \text{Mbps}$ |
| Modulation | DQPSK (CCK) | BPSK/QPSK/16-QAM/64-QAM |
| Spreading | 11-chip Barker code | OFDM ($N=52$ subcarriers) |

### 3.6.3 IEEE 802.11a (WiFi 5 GHz) | WiFi 5 GHz

| Parameter | Value |
|---|---|
| Frequency | $5.15-5.875\ \text{GHz}$ |
| Channel bandwidth | $20\ \text{MHz}$ |
| Subcarriers | $N = 64$ (48 data + 8 pilot) |
| Subcarrier spacing | $312.5\ \text{kHz}$ |
| FFT period | $3.2\ \mu\text{s}$ |
| Guard interval | $0.8\ \mu\text{s}$ |
| Modulation | BPSK to 64-QAM |
| Max data rate | $54\ \text{Mbps}$ |

> **（中文）** 802.11a/g是WiFi的核心标准。802.11a工作在$5\ \text{GHz}$频段，使用OFDM（64个子载波），最高$54\ \text{Mbps}$；802.11g在$2.4\ \text{GHz}$频段提供相同速率，但采用OFDM而非802.11b的DSSS/CCK，保证了向后兼容。OFDM的高PAPR（峰值因子约$10-12\ \text{dB}$）对WiFi射频前端的线性度提出了极高要求。

### 3.6.4 Bluetooth (IEEE 802.15.1) | 蓝牙

| Parameter | Bluetooth 1.2 | Bluetooth 2.1+EDR |
|---|---|---|
| Frequency | $2.402-2.480\ \text{GHz}$ | $2.402-2.480\ \text{GHz}$ |
| Channel spacing | $1\ \text{MHz}$ | $1\ \text{MHz}$ |
| Modulation | GFSK ($\mu = 0.28-0.35$) | GFSK + DQPSK + 8-DPSK |
| Data rates | $1\ \text{Mbps}$ | $2-3\ \text{Mbps}$ |
| Hopping | Frequency hopping (1600 hops/s) | Same |

> **（中文）** 蓝牙工作在$2.4\ \text{GHz}$ ISM频段（$2402-2480\ \text{MHz}$），采用跳频（Frequency Hopping）方式对抗干扰和衰落。主设备在$79$个（或$40$个，蓝牙低能耗）$1\ \text{MHz}$信道间以$1600$跳/秒的速率跳变。蓝牙EDR使用$\pi/4$-DQPSK（$2\ \text{Mbps}$）和8-DPSK（$3\ \text{Mbps}$）提高数据速率。

---

## Key Takeaways | 本章要点

1. **Modulation moves information to RF** for efficient radiation and spectrum allocation.
2. **AM/PM/FM**: Angle modulation (FM/PM) offers constant envelope (efficient PA) but wider bandwidth.
3. **Digital modulation** enables error correction, compression, and flexible adaptation via constellation scaling.
4. **GMSK** (GSM) = constant envelope + narrow spectrum; suits cellular standards with nonlinear PA.
5. **OFDM** enables robust wideband transmission through multicarrier orthogonal multiplexing; high PAPR is the key RF design challenge.
6. **Multiple access**: FDMA (GSM early systems), TDMA (GSM), CDMA (3G), OFDMA (4G/5G).
7. **Shannon capacity** sets the theoretical floor on $E_b/N_0$ for a given spectral efficiency.
8. **RF implications**: Each modulation scheme places specific demands on the transceiver — linearity (for high-order QAM/OFDM), phase noise sensitivity (for coherent detection), and PA efficiency trade-offs.
