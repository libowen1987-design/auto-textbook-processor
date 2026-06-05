---
chapter: 8
title: Oscillators
source: Behzad Razavi, RF Microelectronics, 2nd Edition, McGraw-Hill, 2012
pages: 497-581
---

# Chapter 8: Oscillators
# 第八章：振荡器

> *"The oscillator is the heart of the frequency synthesizer, and its phase noise performance directly determines the quality of the communication link."*
>
> **（中文）** 振荡器是频率合成器的核心，其相位噪声性能直接决定了通信系统的频谱纯度和抗干扰能力。本章从振荡器的基本原理出发，深入分析相位噪声理论，最后讨论VCO设计实践。

---

## 8.1 Performance Parameters | 性能参数

### Key Oscillator Figures of Merit | 振荡器关键性能指标

| Parameter | Symbol | Typical Value (2.4 GHz CMOS VCO) | Unit |
|---|---|---|---|
| Oscillation frequency | $f_0$ | $2.4-2.5$ | GHz |
| Phase noise @ 1 MHz offset | $\mathcal{L}(1\ \text{MHz})$ | $-100$ to $-120$ | $\text{dBc/Hz}$ |
| Tuning range | $\Delta f / f_0$ | $5-15\%$ | — |
| Power consumption | $P_{\text{DC}}$ | $1-10$ | mW |
| Figure of Merit | FOM | $180-190$ | $\text{dBc/Hz}$ |

**Phase Noise $\mathcal{L}(\Delta\omega)$**: Single-sideband phase noise power spectral density at offset $\Delta\omega$ from the carrier, normalized to carrier power:

$$
\mathcal{L}(\Delta\omega) = \frac{P_{\text{SSB}}(\Delta\omega)}{P_{\text{carrier}}} \quad \text{(8.1)}
$$

> **（中文）** 相位噪声$\mathcal{L}(\Delta\omega)$是振荡器最重要的性能指标。它描述了振荡器输出频谱中载波附近$\Delta\omega$偏移处的噪声功率密度与载波功率的比值（单位：$\text{dBc/Hz}$）。GSM规范要求在$600\ \text{kHz}$偏移处$< -126\ \text{dBc/Hz}$。

**Oscillator Figure of Merit (FOM):**

$$
\text{FOM} = \mathcal{L}(\Delta\omega) - 10\log_{10}\left(P_{\text{DC}}[\text{mW}]\right) + 20\log_{10}\left(\frac{f_0}{\Delta\omega}\right) \quad \text{(8.2)}
$$

Higher FOM (more negative $\mathcal{L}$ at same $P_{\text{DC}}$) = better VCO.

---

## 8.2 Basic Principles | 基本原理

### 8.2.1 Feedback View of Oscillators | 振荡器的反馈视图

**Barkhausen Criterion** (necessary but not sufficient for oscillation):

1. **Loop gain magnitude** $|H(j\omega_0)H(j\omega_0)| = 1$
2. **Loop phase** $\angle H(j\omega_0) = 180^\circ$

For a common-source LC oscillator:

$$
H(s) = \frac{-g_m R_P}{1 + sCR_P} \cdot \frac{1}{s^2LC + sCR_P + 1} \quad \text{(8.3)}
$$

At resonance $\omega_0 = 1/\sqrt{LC}$: $|H(j\omega_0)| = -g_m R_P$. For oscillation: $g_m R_P > 1$.

> **（中文）** 巴克豪森判据是振荡器设计的基石：环路增益在振荡频率处必须等于1（相位条件满足时）。对于LC振荡器，振荡条件$g_m R_P > 1$意味着跨导$g_m$必须提供足够的增益来补偿LC谐振回路的损耗（包括电感的寄生电阻和电容的漏电导）。

**Start-up condition:**

$$
g_{m,\text{required}} = \frac{1}{R_P}\left(1 + \frac{r_O}{R_P}\right) \approx \frac{1}{R_P} \quad \text{(8.4)}
$$

For $R_P \approx 1\ \text{k}\Omega$: $g_{m,\text{required}} \approx 1\ \text{mS}$.

> **（中文）** 起振条件：初始启动时（振荡幅度趋于零），电路必须工作在线性模式，此时$g_m R_P > 1$确保净增益。随着振荡幅度增大，晶体管进入非线性区域（增益压缩），环路增益最终稳定在1，实现稳态振荡。

### 8.2.2 One-Port View of Oscillators | 振荡器的单端口视图

The oscillator can be viewed as a **negative-resistance device** in parallel with a resonant network:

**Negative resistance**: $R_{\text{neg}} = -2/g_m$ (for cross-coupled pair)

**Start-up condition:**

$$
|R_{\text{neg}}| < R_P \quad \text{or} \quad g_m > \frac{2}{R_P} \quad \text{(8.5)}
$$

> **（中文）** 单端口（负阻）视图将振荡器视为一个与谐振腔并联的二端口负阻器件。交叉耦合对（cross-coupled pair）的等效负阻$R_{\text{neg}} = -2/g_m$（因为两个晶体管各贡献一半的负阻）。只要$|R_{\text{neg}}| < R_P$（即$g_m > 2/R_P$），负阻补偿了谐振腔的损耗，振荡得以维持。

---

## 8.3 Cross-Coupled Oscillator | 交叉耦合振荡器

The NMOS cross-coupled LC VCO is the most popular RF oscillator topology:

```
V_DD
 │
L
 │
M1 ⇄ M2   (cross-coupled pair)
 │    │
C (varactor)
 │
GND
```

**Differential pair negative resistance:**

$$
R_{\text{neg}} = -\frac{2}{g_m} \quad \text{(8.6)}
$$

**Oscillation frequency:**

$$
\omega_0 = \frac{1}{\sqrt{L(C_{\text{var}} + C_{\text{parasitic}})}} \quad \text{(8.7)}
$$

> **（中文）** NMOS交叉耦合LC VCO是射频振荡器最经典的拓扑。两个NMOS晶体管M1/M2交叉耦合（栅接另一边的漏），形成负阻$R_{\text{neg}} = -2/g_m$，与LC谐振腔并联实现振荡。变容管$C_{\text{var}}$提供频率调谐能力。

**Tail current source**: Adding a current source $I_{\text{tail}}$ improves supply noise rejection but reduces the effective negative resistance (because at large signal, the tail current source limits the differential swing).

---

## 8.4 Three-Point Oscillators | 三点振荡器

The Colpitts, Clapp, and crystal oscillators are three-point oscillators, where the resonator connects to three nodes of the active device:

**Colpitts Oscillator (common-base):**

$$
\omega_0 \approx \frac{1}{\sqrt{L\frac{C_1 C_2}{C_1 + C_2}}} \quad \text{(8.8)}
$$

**Condition for oscillation**: $g_m \geq \frac{1}{R_P}\left(\frac{C_1}{C_2} + \frac{C_2}{C_1}\right)$

> **（中文）** 三点振荡器（Colpitts, Clapp等）利用电容分压器实现反馈，广泛用于晶体振荡器和微波振荡器。Colpitts振荡器的反馈系数为$C_1/C_2$，与LC谐振腔一起决定了振荡频率和起振条件。

---

## 8.5 Voltage-Controlled Oscillators | 压控振荡器

### 8.5.1 Tuning Range Limitations | 调谐范围限制

The VCO frequency is controlled by a tuning voltage $V_{\text{ctrl}}$ applied to the varactor:

$$
\omega_0(V_{\text{ctrl}}) = \frac{1}{\sqrt{L(C_{\min} + C_{\text{fixed}})}} \quad \text{at } V_{\text{ctrl}} = V_{\max} \quad \text{(8.9)}
$$
$$
\omega_0(V_{\text{ctrl}}) = \frac{1}{\sqrt{L(C_{\max} + C_{\text{fixed}})}} \quad \text{at } V_{\text{ctrl}} = V_{\min} \quad \text{(8.10)}
$$

**Relative tuning range:**

$$
\frac{\Delta f}{f_0} = \frac{C_{\max} - C_{\min}}{2(C_{\max} + C_{\min})} \quad \text{(8.11)}
$$

> **（中文）** VCO的调谐范围受限于变容管的$C_{\max}/C_{\min}$比值（典型$\sim 3:1$）和电路的寄生电容。即使变容管调谐范围很宽，电路的固定电容（$C_{\text{fixed}}$）会限制相对调谐范围。

### 8.5.2 Effect of Varactor $Q$ | 变容管$Q$值的影响

The varactor's $Q_{\text{var}}$ at frequency $\omega_0$ directly adds to the total oscillator noise:

$$
Q_{\text{eff}} = \frac{Q_L \cdot Q_{\text{var}}}{Q_L + Q_{\text{var}}} \quad \text{(8.12)}
$$

For $Q_{\text{var}} \ll Q_L$: $Q_{\text{eff}} \approx Q_{\text{var}}$, meaning the varactor dominates the $Q$ and thus the phase noise.

> **（中文）** 变容管的$Q_{\text{var}}$值限制了振荡回路的有效$Q$，进而影响相位噪声。当$Q_{\text{var}} \ll Q_L$时，回路有效$Q$约为$Q_{\text{var}}$，相位噪声由变容管主导。选择高$Q$变容管（PN结变容管优于MOS变容管）是降低VCO相位噪声的关键。

---

## 8.6 LC VCOs with Wide Tuning Range | 宽带LC VCO

### 8.6.1 VCOs with Continuous Tuning | 连续调谐VCO

**Switched capacitor bank** (digital tuning):

$$
C_{\text{bank}} = \sum_{i=1}^{N} C_i \cdot b_i \quad \text{(8.13)}
$$

where $b_i \in \{0,1\}$ are digital control bits.

**Coarse-fine tuning**: Combines a switched capacitor bank (coarse, discrete) with a varactor (fine, continuous).

> **（中文）** 宽带VCO通常采用粗调（switched capacitor bank，数字控制）和细调（varactor，模拟电压控制）相结合的方式。粗调将频率范围划分为$2^N$个离散频段，每个频段内由变容管提供连续调谐。这种方法在PLL中广泛应用（用于覆盖工艺角和温度变化）。

### 8.6.2 Amplitude Variation with Frequency Tuning | 调谐时的幅度变化

When the varactor capacitance changes with $V_{\text{ctrl}}$, the loop gain $g_m R_P$ changes, causing the oscillation amplitude to vary:

$$
A_{\text{osc}} \propto \frac{1}{\sqrt{L(C_{\text{var}}(V_{\text{ctrl}}) + C_{\text{fixed}})}} \quad \text{(8.14)}
$$

**AM-PM coupling**: Large KVCO (high tuning sensitivity) often correlates with large amplitude variation.

> **（中文）** 调谐频率时，变容管的电容变化导致LC回路的有效阻抗变化，从而使振荡幅度也发生变化。这种幅度变化会通过AM-PM转换效应（在放大器的非线性传递函数中）产生额外的相位噪声。

### 8.6.3 Discrete Tuning | 离散调谐

**Phase-locked loop with discrete tuning**: In modern synthesizers, a DAC programs the capacitor bank to lock the VCO to the desired frequency:

**Dithering technique**: Rapidly switching between adjacent capacitor banks to average out the frequency glitches, reducing discrete spurs.

> **（中文）** 离散调谐（开关电容阵列）在切换瞬间会产生频率毛刺（frequency glitch），这些毛刺在PLL输出频谱中表现为离散杂散（spurs）。抖动（dithering）技术通过快速在相邻电容值之间切换，利用平均效应降低杂散幅度，代价是稍微增加相位噪声底。

---

## 8.7 Phase Noise | 相位噪声

### 8.7.1 Basic Concepts | 基本概念

**Phase noise definition (IEEE):**

$$
\mathcal{L}(\Delta\omega) = \frac{S_\phi(\Delta\omega)}{2} \quad \text{(8.15)}
$$

where $S_\phi(\Delta\omega)$ is the phase noise power spectral density (two-sided).

**Total phase variance over bandwidth $B$:**

$$
\sigma_\phi^2 = \int_{0}^{B} S_\phi(\omega)\, d\omega \quad \text{(8.16)}
$$

> **（中文）** 相位噪声$\mathcal{L}(\Delta\omega)$是振荡器输出相位$\phi(t)$的功率谱密度在偏移频率$\Delta\omega$处的单边带值。它描述了振荡器频谱中载波周围"裙带"（skirt）的形状，是衡量振荡器频谱纯度的核心指标。

### 8.7.2 Effect of Phase Noise | 相位噪声的影响

Phase noise degrades communication system performance in several ways:

1. **Adjacent channel interference**: Phase noise spreads the carrier, leaking into adjacent channels
2. **EVM degradation**: For digitally modulated signals, phase noise adds random rotation to constellation points
3. **BER degradation**: In coherent detection, phase noise reduces the effective SNR
4. **Jitter in clock recovery**: Adds timing uncertainty

**Phase noise requirement for GSM:**

At $600\ \text{kHz}$ offset: $\mathcal{L} < -126\ \text{dBc/Hz}$ (for $f_c = 900\ \text{MHz}$).

> **（中文）** GSM规范对相位噪声的要求：在$600\ \text{kHz}$偏移处$< -126\ \text{dBc/Hz}$。这相当于在$200\ \text{kHz}$信道带宽内，相位噪声积累引起的误差向量幅度（EVM）应$< 10\%$。

### 8.7.3 Analysis of Phase Noise: Approach I (Leeson Model) | 相位噪声分析：方法一（Leeson模型）

Leeson (1966) derived an empirical phase noise model:

$$
\mathcal{L}(\Delta\omega) = \frac{F kT}{P_{\text{carrier}}} \left[1 + \left(\frac{\omega_0}{2Q_L \Delta\omega}\right)^2\right] \quad \text{(8.17)}
$$

where $F$ is the empirical "noise factor", $P_{\text{carrier}}$ is the carrier power, $Q_L$ is the loaded quality factor.

**Regions:**
- **Near-carrier ($\Delta\omega < \omega_0/(2Q_L)$)**: $\mathcal{L} \propto 1/\Delta\omega^2$ (flicker noise upconverted by nonlinear processes)
- **Far-from-carrier ($\Delta\omega \gg \omega_0/(2Q_L)$)**: $\mathcal{L} \propto 1/\Delta\omega^2$ (linear time-invariant white noise)

> **（中文）** Leeson模型是振荡器相位噪声分析的第一个系统性模型。它预测了$\mathcal{L} \propto 1/\Delta\omega^2$的斜率（对于偏离载波$\Delta\omega \gg \omega_0/(2Q_L)$的区域），这与实际测量相符。但Leeson模型是经验性的，无法从电路参数直接预测噪声因子$F$。

### 8.7.4 Analysis of Phase Noise: Approach II (Hajimiri-McNeill) | 相位噪声分析：方法二（Hajimiri-McNeill模型）

Hajimiri and McNeill (1998) derived a more accurate, linear periodically-time-varying (LPTV) model:

**Impulse sensitivity function (ISF) $\Gamma(\phi)$:**

The ISF describes how much phase perturbation $\Delta\phi$ is produced by a current impulse $i$ injected at phase $\phi$:

$$
\Delta\phi = \frac{\Gamma(\phi)}{q_{\max}} \cdot i \quad \text{(8.18)}
$$

where $q_{\max} = C_{\text{eff}} V_{\text{osc}}$ is the maximum charge swing.

**Phase noise spectrum from white noise:**

$$
\mathcal{L}(\Delta\omega) = \frac{\Gamma_{\text{rms}}^2}{q_{\max}^2} \cdot \frac{\overline{i_n^2}/\Delta\omega}{P_{\text{carrier}}} \quad \text{(8.19)}
$$

where $\Gamma_{\text{rms}}^2 = \frac{1}{2\pi}\int_0^{2\pi}|\Gamma(\phi)|^2 d\phi$.

> **（中文）** Hajimiri-McNeill（LPTV）模型是相位噪声理论的重大突破。它指出：振荡器是周期性时变（LPTV）系统，任何注入到振荡回路的噪声都会在敏感时刻（通过ISF）产生相位扰动。ISF $\Gamma(\phi)$是一个周期性函数，在振荡电压过零点最大（电流在此刻注入最敏感），在峰值最小。这一模型能够从电路参数直接计算相位噪声，不需要经验参数$F$。

**Key result — ISF and noise upconversion:**

The ISF can be expanded in Fourier series:

$$
\Gamma(\phi) = \frac{c_0}{2} + \sum_{n=1}^{\infty} c_n \cos(n\phi + \theta_n) \quad \text{(8.20)}
$$

- $c_0$ term: converts $1/f$ noise to close-to-carrier $\mathcal{L} \propto 1/\Delta\omega^3$
- $c_1$ term: converts white noise to $\mathcal{L} \propto 1/\Delta\omega^2$

> **（中文）** ISF的傅里叶展开揭示了为什么不同类型的噪声以不同的斜率影响相位噪声：直流分量$c_0$将$1/f$（闪烁）噪声上变频为近载波处的$\mathcal{L} \propto 1/\Delta\omega^3$噪声；奇次谐波分量$c_1$将白噪声转换为$\mathcal{L} \propto 1/\Delta\omega^2$噪声。

### 8.7.5 Noise of Bias Current Source | 偏置电流源的噪声

The tail current source in a VCO contributes noise in a unique way:

**Noise injection mechanism**: The current source noise $i_{n,\text{tail}}$ modulates the tail current, which modulates the oscillator frequency (frequency modulation by noise):

$$
\frac{\Delta\omega}{\omega_0} = \frac{\Delta I_{\text{tail}}}{2I_{\text{bias}}} \quad \text{(8.21)}
$$

This FM modulation creates noise sidebands:

$$
\mathcal{L}_{\text{tail}}(\Delta\omega) \propto \frac{\overline{i_{n,\text{tail}}^2}}{I_{\text{bias}}^2} \cdot \left(\frac{\omega_0}{\Delta\omega}\right)^2 \quad \text{(8.22)}
$$

> **（中文）** 尾电流源噪声通过调频机制（而非直接注入）对VCO相位噪声贡献：当电流源噪声调制$I_{\text{bias}}$时，振荡器的频率随之调制（因为振荡频率与$1/\sqrt{LC}$有关，而$C$受$I_{\text{bias}}$的电子-空穴效应调制）。这种FM机制产生的噪声谱在偏离载波较近处表现为$\mathcal{L} \propto 1/\Delta\omega^2$。

### 8.7.6 Figures of Merit of VCOs | VCO品质因子

**Standard FOM:**

$$
\text{FOM} = \mathcal{L}(\Delta\omega) - 10\log_{10}\left(\frac{P_{\text{DC}}}{1\ \text{mW}}\right) + 20\log_{10}\left(\frac{\omega_0}{\Delta\omega}\right) \quad \text{(8.23)}
$$

**FOM with $K_{\text{VCO}}$:**

$$
\text{FOM}_T = \mathcal{L}(\Delta\omega) - 10\log_{10}(kT) - 10\log_{10}\left(\frac{\omega_0}{\Delta\omega}\right)^2 - 20\log_{10}(K_{\text{VCO}}) \quad \text{(8.24)}
$$

> **（中文）** VCO的品质因子（FOM）在学术界用于比较不同VCO的性能。FOM综合考虑了相位噪声$\mathcal{L}$、功耗$P_{\text{DC}}$、载波频率$\omega_0$和调谐灵敏度$K_{\text{VCO}}$。典型高性能CMOS VCO的FOM约为$-190\ \text{dBc/Hz}$（即更好的值更负）。

---

## 8.10 Mathematical Model of VCOs | VCO的数学模型

### Linear Time-Invariant (LTI) VCO Model | 线性时不变VCO模型

In PLL analysis, the VCO is modeled as an ideal frequency modulator:

$$
\omega_{\text{VCO}}(t) = \omega_0 + K_{\text{VCO}} v_{\text{ctrl}}(t) \quad \text{(8.25)}
$$

**Phase accumulator:**

$$
\phi_{\text{VCO}}(t) = \int_0^t \omega_{\text{VCO}}(\tau) d\tau = \omega_0 t + K_{\text{VCO}}\int_0^t v_{\text{ctrl}}(\tau) d\tau \quad \text{(8.26)}
$$

**Transfer function (Laplace):**

$$
\frac{\phi_{\text{out}}(s)}{V_{\text{ctrl}}(s)} = \frac{K_{\text{VCO}}}{s} \quad \text{(8.27)}
$$

> **（中文）** 在PLL小信号分析中，VCO被建模为一个积分器（$1/s$）——控制电压$v_{\text{ctrl}}$通过$K_{\text{VCO}}$调频，然后积分得到输出相位。这与VCO作为"相位累加器"的物理行为完全一致。PLL的环路分析必须将VCO的$1/s$特性纳入传递函数。

---

## 8.11 Quadrature Oscillators | 正交振荡器

### 8.11.1 Basic Concepts | 基本概念

A quadrature oscillator produces two outputs $90^\circ$ apart in phase:

$$
V_1(t) = A\cos\omega_0 t, \quad V_2(t) = A\sin\omega_0 t \quad \text{(8.28)}
$$

Quadrature signals are essential for:
- Direct-conversion TX/RX I/Q modulation
- Image-reject receivers (Hartley/Weaver architecture)
- Frequency synthesis (single-sideband mixing)

### 8.11.2 Coupled Oscillators | 耦合振荡器

Two LC oscillators coupled through a coupling factor $k_c$ produce quadrature outputs:

**Coupling mechanism**: Edge coupling or cross coupling between the two resonant tanks.

**Coupling condition for quadrature:**

$$
\tan^{-1}\left(\frac{k_c Q}{1 - k_c}\right) = 45^\circ \Rightarrow k_c = \frac{1}{1 + Q^2} \approx \frac{1}{Q^2} \quad \text{(8.29)}
$$

> **（中文）** 耦合振荡器（coupled oscillators）是产生正交信号的重要方法。两个LC振荡器通过耦合因子$k_c$相互耦合，当耦合足够强时，两个振荡器的相位锁定在$90^\circ$（正交）。对于高$Q$振荡器，耦合系数只需要$k_c \approx 1/Q^2$即可实现正交相位锁定。

---

## Key Takeaways | 本章要点

1. **Barkhausen criterion**: $GH(j\omega_0) = 1$ for steady-state oscillation; start-up requires $GH > 1$.
2. **Negative resistance view**: Cross-coupled pair provides $R_{\text{neg}} = -2/g_m$, cancelling tank losses.
3. **Phase noise sources**: Flicker noise upconverted near carrier ($\propto 1/\Delta\omega^3$), white noise far out ($\propto 1/\Delta\omega^2$).
4. **Leeson model**: $\mathcal{L}(\Delta\omega) \propto FkT/P_{\text{carrier}} \times (\omega_0/2Q_L\Delta\omega)^2$.
5. **Hajimiri-McNeill ISF model**: LPTV model predicting phase noise directly from circuit parameters and ISF Fourier coefficients.
6. **Tail current source noise**: Upconverted to phase noise via FM modulation of the carrier.
7. **KVCO and phase noise**: Larger $K_{\text{VCO}}$ gives wider tuning range but also higher phase noise (more VCO control voltage noise converted to phase noise).
8. **Quadrature VCO**: Two coupled LC oscillators lock in quadrature with coupling $k_c \approx 1/Q^2$.
