---
chapter: 6
title: Mixers
source: Behzad Razavi, RF Microelectronics, 2nd Edition, McGraw-Hill, 2012
pages: 337-424
---

# Chapter 6: Mixers
# 第六章：混频器

> *"The mixer is the heart of frequency translation in any transceiver, and its noise and linearity figures directly impact the overall system performance."*
>
> **（中文）** 混频器是射频收发机中完成频率变换的核心模块。其噪声系数和线性度直接影响接收机的灵敏度与阻塞性能，发射机的邻道功率泄漏等关键指标。

---

## 6.1 General Considerations | 一般性考量

### What is a Mixer? | 混频器是什么

A mixer multiplies two signals: the RF input and the LO (local oscillator):

$$
v_{\text{IF}}(t) = v_{\text{RF}}(t) \cdot v_{\text{LO}}(t) \quad \text{(6.1)}
$$

Using trig identities:

$$
\cos\omega_{\text{RF}}t \cdot \cos\omega_{\text{LO}}t = \frac{1}{2}\left[\cos(\omega_{\text{RF}} - \omega_{\text{LO}})t + \cos(\omega_{\text{RF}} + \omega_{\text{LO}})t\right] \quad \text{(6.2)}
$$

**Downconversion**: $f_{\text{IF}} = |f_{\text{RF}} - f_{\text{LO}}|$

**Upconversion**: $f_{\text{IF}} = f_{\text{RF}} + f_{\text{LO}}$

> **（中文）** 混频的本质是乘法运算。射频信号与本振信号相乘，产生和频（$f_{\text{RF}} + f_{\text{LO}}$）和差频（$|f_{\text{RF}} - f_{\text{LO}}|$）两个分量。接收机下变频使用差频，发射机上变频使用和频（或差频取上变频）。

### Mixer as a Switching Network | 混频器作为开关网络

At RF frequencies, LO drives a switching pair (Gilbert cell) that alternates the connection of the RF transconductor to the output:

$$
v_{\text{LO}}(t) = \begin{cases} +V_{\text{LO}} & \text{upper pair on} \\ -V_{\text{LO}} & \text{lower pair on} \end{cases} \quad \text{(6.3)}
$$

The output is effectively $g_m v_{\text{RF}}$ multiplied by a square wave $\pm 1$ at the LO frequency.

> **（中文）** 在实际混频器中，LO信号驱动开关对（Gilbert单元），使RF跨导级$g_m v_{\text{RF}}$以$\pm 1$的方波形式切换到输出。这个方波可展开为基波和各次谐波的叠加：$\pm 1 = \frac{4}{\pi}(\cos\omega_{\text{LO}}t - \frac{1}{3}\cos 3\omega_{\text{LO}}t + \cdots)$。这意味着混频器也会产生奇次谐波的混频产物。

---

## 6.1.1 Performance Parameters | 性能参数

### Conversion Gain (Loss) | 转换增益（损耗）

**Passive (switching) mixer**: Typically has conversion **loss** $L \approx 3-8\ \text{dB}$ (resistive divider effect).

**Active mixer**: Can provide conversion **gain** $G_c \approx 3-10\ \text{dB}$.

For a Gilbert cell mixer:

$$
G_c = \frac{2}{\pi} g_m R_L \quad \text{(passive, switching)} \quad \text{(6.4)}
$$
$$
G_c = \frac{2}{\pi} g_m R_L \cdot A_v \quad \text{(active)} \quad \text{(6.5)}
$$

> **（中文）** 无源混频器（MOS开关与电阻负载）具有转换损耗（约$3-8\ \text{dB}$），因为开关的方波波形每次只有一半时间将电流传递到输出。有源混频器（Gilbert单元加跨阻放大器）可以提供转换增益，代价是额外的噪声和功耗。

### Noise Figure | 噪声系数

**SSB vs DSB Noise Factor:**

Mixers are typically characterized by two noise figures:

| Type | Definition | Typical Value |
|---|---|---|
| SSB NF | Single-sideband (image not filtered) | $10-15\ \text{dB}$ (passive), $15-20\ \text{dB}$ (active) |
| DSB NF | Double-sideband (image filtered/neglected) | Lower by $3\ \text{dB}$ |

> **（中文）** SSB NF和DSB NF相差约$3\ \text{dB}$（因为SSB情况下，RF输入端有噪声但只有一半进入IF——另一半分到了被镜像抑制的"像"上）。在直接转换接收机中，镜像=信号本身，因此SSB NF = DSB NF。

### Linearity — IIP3 and P1dB | 线性度

The mixer's IIP3 is critical because it processes strong out-of-band interferers that may be close to the LO frequency.

For a passive mixer driven by a square-wave LO (amplitude $V_{\text{LO}}$):

$$
IIP3 \propto \frac{V_{\text{LO}}}{R_S} \quad \text{(6.6)}
$$

Higher LO amplitude → better linearity (up to the device breakdown/power limit).

> **（中文）** 混频器的IIP3与LO驱动电平成正比——更强的LO驱动使开关切换更彻底，减少了晶体管的非线性区域参与信号通路的程度。但LO驱动太强可能导致晶体管进入深三极管区或产生过多的LO馈通。

---

## 6.1.2 Mixer Noise Figures | 混频器噪声系数

### Noise in Passive Mixers | 无源混频器的噪声

A passive mixer driven by a square wave LO can be modeled as a periodically-varying resistance $R_{\text{sw}}(t)$ that switches between $R_{\text{ON}}$ and $R_{\text{OFF}}$:

**Output noise spectral density:**

$$
S_{n,\text{out}}(\omega) = 4kT[R_{\text{ON}} \cdot D + R_{\text{OFF}} \cdot (1-D)] \quad \text{(6.7)}
$$

where $D = 0.5$ for 50% duty cycle LO.

**Conversion Gain and NF relationship:**

$$
G_c = \left(\frac{2}{\pi}\right)^2 \frac{R_L}{R_S} = \frac{4}{\pi^2}\frac{R_L}{R_S} \quad \text{(6.8)}
$$
$$
F = \frac{\pi^2}{4}\left(1 + \frac{R_{\text{ON}}}{R_S}\right) \quad \text{(6.9)}
$$

For $R_{\text{ON}} \approx 5\ \Omega$, $R_S = 50\ \Omega$: $F \approx \frac{\pi^2}{4}(1.1) \approx 2.72$ → $\text{NF} \approx 4.35\ \text{dB}$.

> **（中文）** 无源混频器的噪声系数主要来源于开关的导通电阻$R_{\text{ON}}$。即使$R_{\text{ON}} \to 0$，由于开关以50%占空比切换信号，NF也有一个理论下限：$\text{NF}_{\min} = 10\log_{10}(\pi^2/4) \approx 3.9\ \text{dB}$。

### Noise Folding | 噪声折叠

The LO switching action "folds" the RF noise spectrum around DC (for downconversion) and around $2\omega_{\text{LO}}$ (for wideband LO waveforms).

**Mathematical representation:**

The switching function $s(t) = \text{sgn}[\cos\omega_{\text{LO}}t]$ has Fourier components at $\omega_{\text{LO}}, 3\omega_{\text{LO}}, \ldots$

The noise at $\omega_{\text{LO}} + \Omega$ gets downconverted to $\Omega$:

$$
n_{\text{IF}}(\Omega) = n_{\text{RF}}(\omega_{\text{LO}} + \Omega) \cdot s(t) \quad \text{(6.10)}
$$

> **（中文）** 噪声折叠是混频器噪声分析的关键效应。当LO以$\omega_{\text{LO}}$开关RF噪声时，频率为$f_{\text{LO}} + f_{\text{noise}}$的噪声被下变频到$f_{\text{noise}}$。这意味着从DC到$f_{\text{LO}}$的所有RF前端噪声都会折叠到基带，增加基带噪声功率。

---

## 6.1.3 Single-Balanced and Double-Balanced Mixers | 单平衡与双平衡混频器

### Single-Balanced Mixer | 单平衡混频器

```
         M1 (switch)
RF → gm →          → IF+
         M2 (switch) → IF-
         ↑ (LO)
```

**Advantage**: Rejects the LO feedthrough to IF output (to first order).

**Limitation**: Does not reject image frequency.

> **（中文）** 单平衡混频器利用差分结构（一对开关管M1/M2）抑制LO信号的馈通（LO feedthrough）。当M1/M2完美匹配时，LO共模分量在IF差分输出端相互抵消。但RF输入的镜像频率仍然会进入输出。

### Double-Balanced Mixer | 双平衡混频器

```
        M1/M2 (switch pair)
RF → gm →                  → IF+
        M3/M4 (switch pair) → IF-
        ↑ (LO, 180° shifted)
```

**Advantages:**
1. **Rejects both LO feedthrough and RF common-mode** (both sides balanced)
2. **Better linearity** (two switching pairs share the current)
3. **Rejects even-order distortion products**

**Gilbert Cell (Classical Double-Balanced):**

$$
i_{\text{out}} = I_B \cdot \tanh\left(\frac{v_{\text{LO}}}{2V_T}\right) \quad \text{(6.11)}
$$

where $I_B$ is the tail current, $V_T \approx 26\ \text{mV}$ at room temperature.

> **（中文）** 双平衡（Gilbert单元）是射频混频器最经典的拓扑。两个开关对在LO的相反相位驱动，将RF跨导电流切换到差分输出。Gilbert单元平衡了LO和RF两个端口的共模信号，因此对LO馈通和偶阶失真都有更好的抑制能力。

---

## 6.2 Passive Downconversion Mixers | 无源下变频混频器

### 6.2.1 Gain | 增益

A passive mixer can be modeled as a resistive switch with conversion gain:

**Switch conductance switching:**

$$
G_c = \frac{2}{\pi} \cdot \frac{1}{R_S + R_{\text{ON}}} \cdot R_L \quad \text{(6.12)}
$$

**Practical values**: $G_c \approx -3\ \text{dB}$ to $-8\ \text{dB}$ (lossy).

> **（中文）** 无源混频器的转换损耗$L \approx 3-8\ \text{dB}$，主要来源：①开关的非理想切换（方波vs正弦LO）；②$R_{\text{ON}}$电阻的热噪声损耗；③开关时序误差（占空比偏离50%）。

### 6.2.2 LO Self-Mixing | LO自混频

LO self-mixing occurs when LO leakage at the RF port mixes with the LO at the mixer input:

**DC offset at IF output:**

$$
V_{\text{DC,offset}} \propto A_{\text{LO}}^2 \cdot \text{LO-RF isolation} \quad \text{(6.13)}
$$

This is a major problem in direct-conversion receivers.

> **（中文）** LO自混频（LO self-mixing）是指LO泄漏信号从混频器的LO端口反向耦合到RF端口，与真正的LO信号混频，在IF输出产生直流偏置。这个效应在直接转换接收机中特别严重，因为IF=0，直流偏置直接叠加在基带信号上。

### 6.2.3 Noise | 噪声

Passive mixer noise is dominated by:

1. **Thermal noise of $R_{\text{ON}}$** ($\overline{i_n^2} = 4kT/R_{\text{ON}} \cdot B$)
2. **Noise folding from RF input** (finite switch $R_{\text{ON}}$ doesn't fully suppress noise during OFF periods)

**Effective NF of passive mixer:**

$$
F \approx 1 + \frac{R_{\text{ON}}}{R_S} + \frac{\pi^2}{4}\frac{kT}{P_{\text{LO,available}}} \cdot \frac{1}{R_S} \quad \text{(6.14)}
$$

> **（中文）** 无源混频器的噪声主要来自开关导通电阻的热噪声。LO噪声（来自LO驱动电路）也会通过开关的非理想性注入到信号通路。当LO功率降低时，开关的隔离性能变差，LO噪声对总噪声的贡献增加。

### 6.2.4 Input Impedance | 输入阻抗

The RF port of a passive mixer presents a time-varying impedance:

$$
Z_{\text{in}}(t) = R_{\text{ON}} \cdot s(t) + R_{\text{OFF}} \cdot [1 - s(t)] \quad \text{(6.15)}
$$

where $s(t) \in \{0,1\}$ is the switch state.

**Time-averaged input impedance:**

$$
\overline{Z_{\text{in}}} = \frac{R_{\text{ON}} + R_{\text{OFF}}}{2} \quad \text{(6.16)}
$$

> **（中文）** 无源混频器的RF输入阻抗是时变参数——开关导通时为$R_{\text{ON}}$（约几欧），断开时为$R_{\text{OFF}}$（非常高）。时间平均的输入阻抗约为$(R_{\text{ON}} + R_{\text{OFF}})/2$，但对匹配网络设计而言，更重要的是在开关状态下的阻抗。

### 6.2.5 Current-Driven Passive Mixers | 电流驱动无源混频器

In this topology, the RF transconductor is placed **outside** the switching quad:

```
I_RF(t) → [Switching Quad] → IF Output
```

**Advantage**: The transconductor sees a high-impedance current-source load (not the switching quad), improving linearity and NF.

**Conversion gain:**

$$
G_c = \frac{2}{\pi} \cdot \frac{I_{\text{RF}}}{V_{\text{IF,pp}}/2} \quad \text{(6.17)}
$$

---

## 6.3 Active Downconversion Mixers | 有源下变频混频器

### 6.3.1 Conversion Gain | 转换增益

Active mixers provide conversion gain because the switching quad is followed by a transimpedance or voltage amplifier.

**Gilbert Cell with Resistive Load $R_D$:**

$$
G_c = \frac{2}{\pi} g_m R_D \quad \text{(6.18)}
$$

**Gilbert Cell with PMOS Current-Source Load (folded):**

$$
G_c = \frac{2}{\pi} g_m \cdot r_{O,\text{eff}} \quad \text{(6.19)}
$$

where $r_{O,\text{eff}}$ is the effective output resistance.

> **（中文）** 有源Gilbert混频器的转换增益$G_c = \frac{2}{\pi} g_m R_D$。要实现$0\ \text{dB}$的转换增益（$G_c = 1$），需要$g_m R_D = \pi/2 \approx 1.57$。这在$50\ \Omega$系统中是合理的——若$R_D = 1\ \text{k}\Omega$，则$g_m \approx 1.57\ \text{mS}$。

### 6.3.2 Noise in Active Mixers | 有源混频器的噪声

**Noise Sources:**

1. **Transconductor noise** ($\overline{i_{n,g_m}^2} = 4kT\gamma g_m B$): flows to IF output with factor $(2/\pi)^2$
2. **Switching quad noise**: LO phase noise modulates the transconductor current
3. **Load resistor noise** ($\overline{v_{n,R_D}^2} = 4kTR_D B$)

**Total NF (at moderate LO levels):**

$$
F \approx 1 + \frac{\gamma}{g_m R_S} + \frac{\pi^2}{4}\frac{1}{g_m^2 R_S R_D} \quad \text{(6.20)}
$$

> **（中文）** 有源混频器的噪声分析比无源混频器更复杂。跨导级$g_m$的沟道噪声是主要来源，其贡献为$\gamma/(g_m R_S)$。开关级的噪声与LO相位噪声紧密相关——LO的相位抖动使$g_m$电流被"随机化"，在输出产生额外的噪声。

### 6.3.3 Linearity | 线性度

The active mixer linearity is limited by:

1. **Transconductor compression** ($P_{\text{1dB}}$ of the $g_m$ stage)
2. **Switching quad distortion**: Large RF voltage swing at the switch source nodes degrades switching linearity
3. **Voltage headroom**: Cascoding reduces linearity due to reduced $V_{DS}$ swing

**IIP3 of Gilbert Cell:**

$$
IIP3 \approx \frac{4}{3}\frac{V_T^2}{R_S} \cdot \frac{1}{(g_m R_S)^2} \quad \text{(6.21)}
$$

for a well-designed cell in strong inversion.

> **（中文）** 有源Gilbert混频器的线性度受限于跨导级的压缩和开关对的电压摆幅。开关源节点（switching quad source nodes）上的RF电压摆幅会改变开关的导通电阻（因为$V_{DS}$变化导致$r_O$变化），从而产生额外的失真（AM-AM and AM-PM distortion）。

---

## 6.4 Improved Mixer Topologies | 改进的混频器拓扑

### 6.4.1 Active Mixers with Current-Source Helpers | 带电流源辅助的有源混频器

Adding a current-source $I_B$ between the transconductor tail and ground increases linearity by:

1. Providing a high-impedance current source at the source node of the transconductor
2. Reducing the transconductor's $V_{DS}$ variation with signal swing

**Trade-off**: Current-source noise ($4kT\gamma g_{m,\text{cs}}$) adds to total noise.

> **（中文）** 在Gilbert混频器的跨导级尾部加入电流源（current-source helper）可以提高线性度，因为电流源在源端提供了高阻抗，减小了信号摆幅对跨导工作的影响。但电流源本身会贡献噪声，需要仔细设计其$g_m$以在噪声和线性度之间取得平衡。

### 6.4.2 Active Mixers with Enhanced Transconductance | 增强跨导的有源混频器

Using a differential pair with multiple transistors (e.g., $g_m$-boosted common-gate) increases the effective transconductance without proportionally increasing bias current.

**$g_m$-boosted CG stage:**

$$
G_{m,\text{eff}} = g_m(1 + g_m R_{\text{boost}}) \quad \text{(6.22)}
$$

> **（中文）** $g_m$增强型共栅级通过反馈环（$R_{\text{boost}}$）提高有效跨导至$g_m(1 + g_m R_{\text{boost}})$，在不增加偏置电流的情况下提升转换增益和噪声性能。

### 6.4.3 Active Mixers with High IP2 | 高IP2有源混频器

IIP2 (second-order intercept point) is critical in direct-conversion receivers because second-order nonlinearity produces DC offsets.

**Sources of IIP2 degradation:**

1. **Switch mismatch**: Threshold voltage mismatch between switching transistors
2. **Charge injection**: Gate-charge injection asymmetry in switches
3. **Layout asymmetry**: Physical asymmetry in the switching quad

**Calibration techniques:**
- **DC offset cancellation**: Highpass filter or digital subtraction
- ** chopper stabilization**: Modulate DC offset to high frequency, then filter

> **（中文）** 直接转换接收机对混频器的IIP2要求极高（GSM: $> +60\ \text{dBm}$），因为二阶非线性产生的直流偏置会破坏基带信号。通过精心设计（匹配布局、斩波稳定、DC偏移校准），可以提高IIP2。电荷注入的不对称性是开关对IIP2恶化的重要来源，需要通过dummy开关或差分技术来缓解。

### 6.4.4 Active Mixers with Low Flicker Noise | 低闪烁噪声有源混频器

**Chopper mixing**: Upconvert the baseband signal (and its noise) to RF, then downconvert — moving the $1/f$ noise to a high offset frequency where it is filtered:

$$
v_{\text{IF}}(t) = v_{\text{RF}}(t) \cdot \text{sgn}[\cos\omega_{\text{LO}}t] \quad \text{(6.23)}
$$

**Result**: Flicker noise is modulated to $f_{\text{LO}} \pm f_{\text{baseband}}$ — well above the channel bandwidth.

> **（中文）** 闪烁噪声（$1/f$噪声）在直接转换接收机的基带中是一个严重问题。斩波混频（chopper mixing）通过将基带信号调制到LO频率的奇次边带上，将$1/f$噪声"搬移"到远离基带的频率，然后通过高通滤波器滤除。这是在直接转换接收机中抑制$1/f$噪声的标准技术。

---

## 6.5 Upconversion Mixers | 上变频混频器

### 6.5.1 Performance Requirements | 性能要求

TX upconversion mixers have different requirements from RX downconversion mixers:

| Parameter | RX Mixer | TX Mixer |
|---|---|---|
| Primary concern | NF | Linearity, LO leakage |
| Output load | Typically fixed (BPF) | Often PA input (wideband) |
| LO drive | Moderate | High (for linearity) |
| DC offset | Critical (DC at output) | Less critical (modulated output) |

### 6.5.2 Upconversion Mixer Topologies | 上变频混频器拓扑

**Single-sideband upconversion** (for I/Q modulation):

$$
s_{\text{RF}}(t) = I(t)\cos\omega_c t - Q(t)\sin\omega_c t \quad \text{(6.24)}
$$

This is the standard I/Q modulator topology, equivalent to a direct-conversion TX mixer.

**Sideband suppression**: Achieved by precise I/Q amplitude and phase matching (similar to image rejection in RX).

> **（中文）** 发射机I/Q调制器（上变频混频器）将基带I/Q信号调制到载波频率。关键要求：①载波泄漏（carrier feedthrough）要低（$< -50\ \text{dBc}$）；②边带抑制要好（$<-40\ \text{dBc}$）。这两项指标分别取决于I/Q直流偏置和I/Q幅度/相位匹配精度。

---

## Key Takeaways | 本章要点

1. **Mixer fundamentals**: Mixing = multiplication, producing sum and difference frequencies.
2. **Passive mixers** have conversion loss (NF $> 3.9\ \text{dB}$ minimum) but excellent linearity and low $1/f$ noise.
3. **Active (Gilbert) mixers** provide conversion gain but add transistor noise and have poorer $1/f$ noise.
4. **Double-balanced** topology rejects LO feedthrough and even-order distortion.
5. **SSB vs DSB NF**: differs by $3\ \text{dB}$ due to image noise folding.
6. **Noise folding** at the switching quad is a key noise mechanism in both active and passive mixers.
7. **LO self-mixing** is a major DC offset source in direct-conversion receivers.
8. **IIP2** is critical for direct-conversion RX mixers; requires careful layout and calibration.
9. **Chopper stabilization** moves $1/f$ noise away from baseband, enabling direct-conversion RX.
