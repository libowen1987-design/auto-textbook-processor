---
chapter: 11
title: Fractional-N Synthesizers
source: Behzad Razavi, RF Microelectronics, 2nd Edition, McGraw-Hill, 2012
pages: 715-749
---

# Chapter 11: Fractional-N Synthesizers
# 第十一章：分数-N频率合成器

> *"The fractional-N synthesizer overcomes the integer-N trade-off between channel spacing and settling time, enabling fine frequency resolution without sacrificing PLL bandwidth."*
>
> **（中文）** 分数-N合成器打破了整数-N合成器中信道间隔与锁定时间之间的权衡，以细频率分辨率实现快速锁定，是现代无线通信系统（4G LTE, 5G NR, WiFi 6）频率合成的核心技术。

---

## 11.1 Basic Concepts | 基本概念

### Fractional Division | 分数分频

The average division ratio can be fractional:

$$
\bar{N} = N + \frac{K}{M} \quad \text{(11.1)}
$$

where $K < M$ are integers. The instantaneous division ratio is an integer $N$ or $N+1$, but over $M$ cycles the average is $N + K/M$.

**Example**: $N = 20$, $K/M = 1/100$ → $\bar{N} = 20.01$ → $f_{\text{out}} = 20.01 \times f_{\text{ref}}$.

> **（中文）** 分数-N合成的平均分频比可以是任意有理数。瞬时分频比仍是整数（$N$或$N+1$），但通过脉冲删除/填充技术在$M$个周期内平均得到$N + K/M$。这使得$f_{\text{ref}}$可以远大于信道间隔——例如，WiFi信道间隔$5\ \text{MHz}$时，$f_{\text{ref}}$可以用$20-40\ \text{MHz}$，大幅改善锁定时间和相位噪声。

**Advantage over Integer-$N$**: Reference frequency can be much higher than channel spacing:

| Feature | Integer-$N$ | Fractional-$N$ |
|---|---|---|
| $f_{\text{ref}}$ | = channel spacing | $\gg$ channel spacing |
| $N$ | Large ($\sim 10,000$) | Small ($\sim 100$) |
| $\omega_n$ | Small → slow settle | Large → fast settle |
| Phase noise | Worse (large $N$) | Better (small $N$) |

> **（中文）** 分数-N的核心优势：参考频率可以远大于信道间隔（如$20-40\ \text{MHz}$ vs. $200\ \text{kHz}$），使$N$从$\sim 20,000$降低到$\sim 100$。$N$的平方根关系（$\omega_n \propto 1/\sqrt{N}$）意味着分数-N的锁定速度可以比整数-N快约14倍！同时，VCO噪声被乘以$N$的因子被放大，小$N$意味着更好的相位噪声。

---

## 11.2 Randomization and Noise Shaping | 随机化与噪声整形

### 11.2.1 Modulus Randomization | 分频比随机化

The simplest fractional-$N$ technique: randomly select between division ratios $N$ and $N+1$:

$$
P(N + 1) = \frac{K}{M}, \quad P(N) = 1 - \frac{K}{M} \quad \text{(11.2)}
$$

**Problem**: Random fluctuations in the divided frequency create **fractional spurs** — discrete spurious tones in the output spectrum.

> **（中文）** 简单的分频比随机化（无规选择$N$和$N+1$）会产生分数杂散（fractional spurs）——输出频谱中在$f_{\text{ref}}/M$整数倍处出现离散杂散。这是因为随机的分频比切换在频域表现为周期性分量（尽管是伪随机的）。

### 11.2.2 Basic Noise Shaping | 基本噪声整形

A **$\Sigma\Delta$ modulator** ( SDM) shapes the quantization noise to high frequencies:

**First-order $\Sigma\Delta$ modulator:**

```
      +----[Accumulator]----+
      |         ↑            |
      ↓         |            |
e[n] ──→ [+] ──→ z^(-1) ──→ v[n]
     |                  |
     ↑                  |
     K                  |
     ←───── feedback ←───┘
```

**Transfer functions:**

$$
V(z) = \frac{K}{1 - z^{-1}} + z^{-1} E(z) \quad \text{(11.3)}
$$

Signal transfer function: $H_{\text{signal}}(z) = K \cdot \frac{z^{-1}}{1-z^{-1}}$

Noise transfer function: $H_N(z) = \frac{1}{1-z^{-1}} = \frac{z}{z-1}$ → **integration** (shapes noise to high frequencies).

> **（中文）** 一阶Sigma-Delta调制器（SDM）对量化噪声进行积分整形（noise shaping）：信号被$K \cdot z^{-1}/(1-z^{-1})$传递（低频通过），而量化噪声被$1/(1-z^{-1})$传递（高频整形）。这意味着量化噪声被"推"到高频，然后在PLL的LPF中被滤除。

**Noise PSD after shaping:**

$$
S_{\text{SDM}}(\omega) = \frac{(2\pi)^2}{12} \cdot \left(2\sin\frac{\omega}{2f_s}\right)^2 \cdot \left|\frac{1}{1-e^{-j\omega/f_s}}\right|^2 \quad \text{(11.4)}
$$

For small $\omega/f_s$: $S_{\text{SDM}} \propto \omega^2$ (noise shaping reduces low-frequency quantization noise).

> **（中文）** Sigma-Delta调制器的噪声整形效果：将量化噪声从白噪声（平坦谱）转换为$\propto \omega^2$型谱（在低频偏移处显著降低）。这使得分数-N合成器的近载波量化噪声远低于简单随机化方案。

### 11.2.3 Higher-Order Noise Shaping | 高阶噪声整形

**Second-order $\Sigma\Delta$ modulator** (MASH 1-1):

$$
H_N(z) = \frac{(1-z^{-1})^2}{1 - 2z^{-1} + z^{-2}} \quad \text{(11.5)}
$$

**Noise spectrum**: $\propto \omega^4$ (for second-order) → even better near-carrier noise suppression.

> **（中文）** 高阶SDM（二阶、三阶甚至四阶）提供更强的噪声整形：$\omega^2$（一阶）→ $\omega^4$（二阶）→ $\omega^6$（三阶）→ 越来越好的低频量化噪声抑制。但高阶SDM在大信号条件下可能失去稳定性，需要仔细设计（modulus scaling, stability monitoring）。

### 11.2.4 Problem of Out-of-Band Noise | 带外噪声问题

While SDM shapes quantization noise to high frequencies, these high-frequency quantization components may **excite the VCO** or **overload the charge pump**:

$$
P_{\text{quant,out}} \propto \frac{1}{T_s^3} \quad \text{(11.6)}
$$

> **（中文）** SDM将量化噪声整形到高频，虽然在PLL的LPF中被部分滤除，但高频量化噪声仍可能通过以下途径影响系统：①直接注入VCO控制线；②通过PFD产生不正确的UP/DOWN脉冲；③在混频器中产生互调产物。需要精心设计LPF来衰减这些高频分量。

### 11.2.5 Effect of Charge Pump Mismatch | 电荷泵失配的影响

Charge pump mismatch interacts with the SDM in a fractional-$N$ PLL:

**Mismatch-induced fractional spur**: The SDM output $v[n]$ modulates the charge pump current, producing a spurious tone at $K \cdot f_{\text{ref}}/M$:

$$
\mathcal{L}(f_{\text{frac}}) \approx 20\log_{10}\left|\frac{I_{\text{mismatch}}}{I_P} \cdot \frac{H_N(j\omega_{\text{frac}})}{N}\right| \quad \text{(11.7)}
$$

> **（中文）** 电荷泵电流失配与SDM的相互作用是分数-N合成器中分数杂散的重要来源。SDM输出的调制序列与失配的泵电流相乘，在$f_{\text{frac}} = K \cdot f_{\text{ref}}/M$处产生离散杂散。减小失配（增大器件面积）和提高LPF对$f_{\text{frac}}$的衰减是抑制该杂散的方法。

---

## 11.3 Quantization Noise Reduction Techniques | 量化噪声降低技术

### 11.3.1 DAC Feedforward | DAC前馈

A DAC feeds back the fractional component $K/M$ to cancel the quantization error:

```
K/M ──→ [DAC] ──→ LPF ──→ VCO
              ↑
         (cancellation)
```

**Result**: Reduces quantization noise by $20-40\ \text{dB}$, but requires high-precision DAC.

> **（中文）** DAC前馈（DAC feedforward）技术用高精度DAC重建分频比的分数部分（$K/M$），在LPF输入端与SDM的量化误差相减，将量化噪声降低$20-40\ \text{dB}$。但这一技术需要非常高精度的DAC（通常12-16位以上），且DAC的非线性会引入新的杂散。

### 11.3.2 Fractional Divider | 分数分频器

A multi-modulus divider ($P$, $P+1$, ..., $P+M-1$) programmed by the SDM directly implements fractional division without a separate DAC:

$$
N_{\text{inst}} = P + v[n] \quad \text{(11.8)}
$$

where $v[n]$ is the SDM output.

> **（中文）** 分数分频器（fractional divider）用多模分频器（由SDM直接控制）实现分数分频，避免了独立DAC的精度和非线性问题。这是现代分数-N合成器的标准架构。

### 11.3.3 Reference Doubling | 参考倍频

Multiply the reference frequency by $M$ using a delay-locked loop (DLL) or multiplier:

$$
f_{\text{ref,new}} = M \cdot f_{\text{ref}} \quad \text{(11.9)}
$$

Then use a smaller $N$ (since $f_{\text{ref}}$ is larger).

> **（中文）** 参考倍频技术使用DLL或倍频器将参考频率提高$M$倍，使$N$相应减小$\sqrt{M}$倍（因为$\omega_n \propto 1/\sqrt{N}$），从而改善相位噪声和锁定时间。

### 11.3.4 Multiphase Frequency Division | 多相频率分频

Use multiple phases of a ring oscillator to achieve fractional division by $N + 1/P$:

$$
f_{\text{out}} = \frac{P}{PN + 1} f_{\text{ref}} \quad \text{(11.10)}
$$

**Advantage**: Fine resolution without SDM complexity.

> **（中文）** 多相频率分频利用环形振荡器的多相位输出实现精细的分数分频。例如，使用8相位的振荡器可以实现$1/8$周期的分辨率，对应$\pm 1/16$个周期的分数分频精度。

---

## Key Takeaways | 本章要点

1. **Fractional-$N$ advantage**: High $f_{\text{ref}}$ → small $N$ → fast settling + low phase noise vs. fine channel spacing.
2. **$\Sigma\Delta$ modulation**: Shapes quantization noise from white to $\omega^2$ (1st order), $\omega^4$ (2nd order), etc.
3. **Fractional spurs**: From SDM quantization + charge pump mismatch; suppressed by higher-order SDM + better CP matching.
4. **Out-of-band SDM noise**: Can excite VCO or CP nonidealities; needs strong LPF filtering.
5. **DAC feedforward**: Cancels quantization error, reducing noise by $20-40\ \text{dB}$.
6. **Modern fractional-$N$**: All-digital $\Sigma\Delta$ modulator + multi-modulus divider + differential CP is the standard RF synthesizer architecture.
