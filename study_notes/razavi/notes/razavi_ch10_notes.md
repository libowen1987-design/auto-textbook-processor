---
chapter: 10
title: Integer-N Frequency Synthesizers
source: Behzad Razavi, RF Microelectronics, 2nd Edition, McGraw-Hill, 2012
pages: 655-712
---

# Chapter 10: Integer-N Frequency Synthesizers
# 第十章：整数-N频率合成器

> *"The integer-N frequency synthesizer multiplies the reference frequency by an integer N, producing a channelized LO signal. Its simplicity and excellent phase noise make it the workhorse of many wireless standards."*
>
> **（中文）** 整数-N频率合成器将参考频率乘以整数$N$，产生信道化的本振信号。其简单性和优异的相位噪声使其成为许多无线标准的首选。

---

## 10.1 General Considerations | 一般性考量

### Channel Spacing and Reference Frequency | 信道间隔与参考频率

For a channel spacing $\Delta f_{\text{ch}}$:

$$
f_{\text{out}} = N \cdot f_{\text{ref}}, \quad f_{\text{ref}} = \Delta f_{\text{ch}} \quad \text{(10.1)}
$$

**GSM example**: $f_{\text{ref}} = 200\ \text{kHz}$ (channel spacing), $f_{\text{VCO}} \approx 4-6\ \text{GHz}$ → $N \approx 20,000-30,000$.

**Trade-off**: Lower $f_{\text{ref}}$ (smaller channel spacing) → larger $N$ → smaller $\omega_n$ for given $\zeta$ (because $\omega_n \propto 1/\sqrt{N}$) → slower settling time.

> **（中文）** 整数-N合成器的信道间隔等于参考频率$f_{\text{ref}}$。要获得$200\ \text{kHz}$的信道间隔（如GSM），$f_{\text{ref}}$必须为$200\ \text{kHz}$，而VCO频率为$4-6\ \text{GHz}$意味着$N \approx 20,000-30,000$。大$N$降低了环路自然频率$\omega_n$（$\omega_n \propto 1/\sqrt{N}$），导致锁定时间变慢。

### Integer-N PLL Architecture | 整数-N PLL架构

```
f_ref → [PFD/CP] → [LPF] → [VCO] → [÷N] → f_out = N·f_ref
```

**Key design parameters:**
- $N$: Programmable integer divider ratio
- $f_{\text{ref}}$: Reference frequency (channel spacing)
- $\omega_n$, $\zeta$: Loop bandwidth and damping
- $P_{\text{spur}}$: Reference spur level at $f_{\text{ref}}$

> **（中文）** 整数-N PLL的基本架构与通用CP-PLL相同，核心区别在于分频比$N$是整数。设计的关键挑战是：在满足锁定时间和相位噪声要求的同时，控制$f_{\text{ref}}$杂散电平。

---

## 10.2 Basic Integer-N Synthesizer | 基本整数-N合成器

### Frequency Resolution | 频率分辨率

The frequency resolution (channel spacing) is:

$$
\Delta f_{\text{ch}} = f_{\text{ref}} = \frac{f_{\text{VCO}}}{N} \quad \text{(10.2)}
$$

For a given VCO frequency range $[\omega_{\min}, \omega_{\max}]$ and fixed $f_{\text{ref}}$, the number of channels is:

$$
N_{\text{ch}} = \frac{\omega_{\max} - \omega_{\min}}{\omega_{\text{VCO}}/\omega_{\min}} \cdot \frac{1}{f_{\text{ref}}} \quad \text{(10.3)}
$$

> **（中文）** 整数-N合成器的频率分辨率等于参考频率$f_{\text{ref}}$。在给定VCO调谐范围的情况下，$f_{\text{ref}}$越小，可覆盖的信道数越多，但$N$越大，环路锁定时间越长。这是整数-N合成器的基本矛盾：细信道间隔 ↔ 快锁定时间 ↔ 低相位噪声。

---

## 10.3 Settling Behavior | 锁定行为

### Settling Time | 锁定时间

The settling time for a frequency step $\Delta f$ is dominated by the PLL's closed-loop dynamics:

For a step frequency change of $\Delta\omega$:

$$
t_{\text{settle}} \approx \frac{4.6}{\zeta\omega_n} \quad \text{(for 1% settling)} \quad \text{(10.4)}
$$

**Trade-off with $\omega_n$**: Larger $\omega_n$ → faster settling → better phase noise (at the expense of reference spur suppression).

> **（中文）** 锁定时间$t_{\text{settle}}$与环路自然频率$\omega_n$成反比：$\omega_n$越大，锁定越快。但$\omega_n$增大意味着LPF带宽增大，对$f_{\text{ref}}$纹波的滤波能力减弱，参考杂散增加。典型GSM整数-N合成器的锁定时间约$250\ \mu\text{s}$。

**Example — GSM settling time requirement:**

GSM specifications require frequency settling to within $\pm 90\ \text{Hz}$ (relative to $900\ \text{MHz}$ carrier) within one timeslot ($577\ \mu\text{s}$).

For $N \approx 4500$ (at $900\ \text{MHz}$ with $f_{\text{ref}} = 200\ \text{kHz}$), this requires $\omega_n \approx 2\pi \times 50\ \text{krad/s}$.

---

## 10.4 Spur Reduction Techniques | 杂散抑制技术

### Reference Spur Mechanisms | 参考杂散机制

Reference spurs at $f_{\text{ref}}$ arise from:

1. **PFD/CP dead zone and minimum pulse width**: Even in lock, PFD produces minimum-width UP/DOWN pulses
2. **Charge injection and clock feedthrough**: Discrete events at each reference cycle
3. **Charge pump current mismatch**: Net charge error per reference cycle
4. **$V_{\text{ctrl}}$ ripple**: Modulates VCO frequency at $f_{\text{ref}}$

**Spur level**:

$$
\mathcal{L}(f_{\text{ref}}) \approx 20\log_{10}\left(\frac{K_{\text{VCO}} \cdot \Delta V_{\text{ripple}}}{f_{\text{ref}}}\right) \quad \text{(10.5)}
$$

> **（中文）** 参考杂散（reference spur）在$f_{\text{ref}}$处产生，其电平取决于：①$V_{\text{ctrl}}$在每个参考周期的纹波幅度$\Delta V_{\text{ripple}}$；②VCO的调谐灵敏度$K_{\text{VCO}}$（将电压纹波转化为相位调制）；③参考频率$f_{\text{ref}}$（决定纹波的"调制指数"）。杂散电平通常要求$< -60\ \text{dBc}$。

### Spur Reduction Methods | 杂散抑制方法

**1. Higher $f_{\text{ref}}$**: Reduces the number of channels $N$, requiring faster settling → trade-off.

**2. Better charge pump design**: Current mismatch < 0.5%, minimum pulse width control.

**3. Differential charge pump**: Rejects common-mode perturbations.

**4. Offset charge pump**: Add a constant offset current to avoid dead zone operation.

**5. LPF with higher attenuation at $f_{\text{ref}}$**: Third-order or higher LPF with pole at $f_{\text{ref}}$:

$$
|H_{\text{LPF}}(j\omega_{\text{ref}})| \propto \frac{1}{\omega_{\text{ref}}^3 C_1 R_1 C_2} \quad \text{(10.6)}
$$

> **（中文）** 抑制参考杂散的方法：①增大$f_{\text{ref}}$（但会减少信道数）；②降低电荷泵失配（增大器件面积）；③使用差分电荷泵；④使用更高阶LPF（三个或更多极点）在$f_{\text{ref}}$处提供更强的衰减。典型三阶LPF在$f_{\text{ref}} = 200\ \text{kHz}$处可提供约$40-50\ \text{dB}$的杂散抑制。

---

## 10.5 PLL-Based Modulation | 基于PLL的调制

### 10.5.1 In-Loop Modulation | 环内调制

In in-loop modulation, the modulation signal is applied inside the PLL loop:

```
m(t) → [Modulator] → [÷N] → PFD ← f_ref
                    ↓
                  VCO → f_out = N·f_ref + m(t)·K_MOD
```

The PLL tracks the average frequency, while the modulation modulates the VCO directly.

**Challenge**: Loop filter attenuates high-frequency modulation components → distortion.

> **（中文）** 环内调制（GMSK等）将调制信号注入到PLL环路内部。环路跟踪平均频率，而调制信号直接调制VCO。LPF对高频调制分量的衰减会导致调制失真——这是直接用PLL进行调制的主要限制。

### 10.5.2 Two-Point Modulation | 双点调制

Two-point modulation applies modulation at both the VCO input and the reference input (or ÷N input):

$$
\omega_{\text{out}}(t) = \omega_0 + K_{\text{VCO}} m(t) + K_{\text{div}} m(t) \quad \text{(10.7)}
$$

where $K_{\text{VCO}}$ and $K_{\text{div}}$ are chosen to cancel each other in the loop response, leaving flat modulation frequency response.

> **（中文）** 双点调制（two-point modulation）是解决环内调制带宽限制的方法：在VCO控制端和分频器输入端同时注入调制信号，两个路径的环路响应差异通过精心设计相互补偿，实现从直流到调制信号最高频率的平坦响应。这是LTE和GSM发射机中PLL调制的主要技术。

---

## 10.6 Divider Design | 分频器设计

### 10.6.1 Pulse Counter and Swallow Counter | 脉冲计数器与吞咽计数器

**Dual-modulus prescaler**: Divides by $P$ or $P+1$ (e.g., $P = 64/65$).

**Operation**:
1. Prescaler divides by $P+1$ for $M$ cycles, then by $P$ for $(N - M)$ cycles
2. Total division ratio: $N = (P+1)M + P(N-M) = PN + M$
3. Solve for $M$: $M = N - PN$

> **（中文）** 双模前置分频器（prescaler）是实现大$N$分频比的关键：它以$P$或$P+1$分频（典型值$P = 8/9$, $16/17$, $32/33$, $64/65$）。吞咽计数器（swallow counter）控制前置分频器在$M$个周期内分频$P+1$，其余$N-M$个周期分频$P$，从而实现总分频比$N = PN + M$。

### 10.6.2 Multi-Modulus Dividers | 多模分频器

Multi-modulus dividers ($P/(P+1)/\ldots/(P+M)$) enable fractional-$N$ synthesis (Chapter 11).

**Sigma-delta modulator**: Controls the multi-modulus divider ratio, shaping quantization noise to high frequencies.

> **（中文）** 多模分频器（multi-modulus divider）与Sigma-Delta调制器（$\Sigma\Delta$ modulator）结合是现代分数-N合成器（fractional-$N$）的核心技术。Sigma-Delta调制器动态控制分频比，将量化噪声"整形"到高频，再通过LPF滤除。

---

## Key Takeaways | 本章要点

1. **Integer-$N$ limitation**: Fine channel spacing → large $N$ → slow settling; coarse spacing → fast settling → fewer channels.
2. **Settling time**: $t_{\text{settle}} \approx 4.6/(\zeta\omega_n)$; GSM requires $< 250\ \mu\text{s}$.
3. **Reference spurs**: From CP mismatches, charge injection; suppressed by higher-order LPF.
4. **Modulation**: In-loop modulation for narrowband (GMSK); two-point modulation for wider bandwidth (LTE).
5. **Integer-$N$ vs. Fractional-$N$**: Integer-$N$ has simpler noise (no quantization noise), but coarse channel spacing limits use to standards with large channel spacing (e.g., microwave point-to-point).
