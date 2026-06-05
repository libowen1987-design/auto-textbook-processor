---
chapter: 5
title: Low-Noise Amplifiers
source: Behzad Razavi, RF Microelectronics, 2nd Edition, McGraw-Hill, 2012
pages: 255-334
---

# Chapter 5: Low-Noise Amplifiers
# 第五章：低噪声放大器

> *"The low-noise amplifier (LNA) is the first active stage in a receiver, and its noise figure largely determines the overall receiver sensitivity."*
>
> **（中文）** 低噪声放大器（LNA）是接收机的第一个有源模块，其噪声系数在很大程度上决定了整个接收机的灵敏度。LNA的设计需要在噪声、增益、线性度、输入匹配和功耗之间进行复杂的权衡。

---

## 5.1 General Considerations | 一般性考量

### LNA as the Receiver Front-End | LNA作为接收机前端

The LNA must satisfy several conflicting requirements simultaneously:

1. **Low Noise Figure (NF)**: Typically $< 2\ \text{dB}$ for cellular RX front-end
2. **Sufficient Gain**: Typically $10-20\ \text{dB}$ to overcome subsequent stage noise
3. **Good Input Matching**: $S_{11} < -10\ \text{dB}$ at the operating frequency (for $50\ \Omega$ system)
4. **High Linearity**: IIP3 $> -10\ \text{dBm}$ to handle GSM blockers
5. **Stability**: $K > 1$, $|\Delta| < 1$ (unconditional stability)
6. **Low Power Consumption**: Critical for battery-powered mobile devices

**Overall RX Noise Factor (with LNA gain $G_{\text{LNA}}$ and NF $F_{\text{LNA}}$):**

$$
F_{\text{total}} \approx F_{\text{LNA}} + \frac{F_{\text{mixer}} - 1}{G_{\text{LNA}}} \quad \text{(5.1)}
$$

> **（中文）** LNA是接收机噪声系数的最主要决定因素。由Friis公式可见，若LNA增益$G_{\text{LNA}} > 10\ \text{dB}$，则后续混频器的噪声贡献被充分衰减。因此设计低噪声、高增益、高线性度的LNA是接收机前端设计的核心。

### Noise Figure Requirement from Sensitivity | 从灵敏度推导NF需求

For GSM RX (sensitivity $-104\ \text{dBm}$, $B = 200\ \text{kHz}$, SNR$_{\min} = 9\ \text{dB}$):

$$
P_{\text{min}} = -174 + 10\log(200\times 10^3) + \text{NF} + 9 = -104\ \text{dBm}
$$

Solving: $\text{NF} \approx 9\ \text{dB}$ → with $G_{\text{LNA}} \approx 15\ \text{dB}$, mixer NF $\approx 15\ \text{dB}$:

$$
F_{\text{total}} = F_{\text{LNA}} + \frac{F_{\text{mixer}} - 1}{G_{\text{LNA}}} \approx 1.8 + \frac{31.6 - 1}{31.6} \approx 2.7 \Rightarrow \text{NF}_{\text{total}} \approx 4.3\ \text{dB}
$$

> **（中文）** GSM接收机的灵敏度$-104\ \text{dBm}$要求接收机总噪声系数约$9\ \text{dB}$。考虑到混频器和基带的噪声贡献，LNA本身的NF需要约$2\ \text{dB}$（若$G_{\text{LNA}} = 15\ \text{dB}$）。这在CMOS工艺中是可以实现的，但需要精心设计。

---

## 5.2 Problem of Input Matching | 输入匹配问题

### Why Input Matching Matters | 为什么输入匹配重要

The LNA presents an input impedance to the preceding block (typically a $50\ \Omega$ source, often via an SAW filter or antenna):

**Power Matching vs. Noise Matching:**

| Criterion | Condition | Goal |
|---|---|---|
| Power matching (Max power transfer) | $Z_{\text{in}} = Z_S^*$ | Maximum signal power transfer |
| Noise matching | $Z_{\text{in}} \neq Z_S$ (optimum) | Minimum noise figure |

> **（中文）** 传统微波理论强调功率匹配（$Z_{\text{in}} = Z_S^*$），以最大化信号功率传输。但LNA的噪声最优化要求最佳源阻抗（$Z_{\text{opt}}$），这通常不等于$50\ \Omega$。在实际设计中，我们需要在功率匹配与噪声最优之间做权衡——通常先确保噪声接近最优，然后在允许范围内调节匹配到接近$50\ \Omega$。

### Optimum Source Resistance for Minimum NF | 最小NF的最佳源电阻

For a MOSFET with gate-referred voltage noise $\overline{v_n^2} = 4kT\gamma/g_m$ and source resistance $R_S$:

$$
F = 1 + \frac{\overline{v_n^2} + \overline{i_n^2}R_S^2}{4kTR_S} = 1 + \frac{\gamma}{2g_m R_S} + \frac{g_m R_S}{2} \quad \text{(5.2)}
$$

Setting $\partial F/\partial R_S = 0$:

$$
R_{\text{opt}} = \sqrt{\frac{\gamma}{g_m}} \quad \text{(5.3)}
$$

> **（中文）** MOSFET的最小噪声系数发生在源电阻$R_{\text{opt}} = \sqrt{\gamma/g_m}$处。对于典型CMOS LNA（$g_m = 20\ \text{mS}$, $\gamma = 2/3$）：$R_{\text{opt}} \approx \sqrt{(2/3)/(0.02)} \approx \sqrt{33.3} \approx 5.8\ \Omega$，远小于$50\ \Omega$！这说明CMOS LNA的噪声最优源阻抗远低于$50\ \Omega$系统阻抗。

### Simultaneous Noise and Power Matching | 噪声与功率的同时匹配

The的矛盾在窄带LNA中可以通过**电感源简并（inductive source degeneration）**来解决：引入一个纯电感性（无损）元件$L_S$，使输入阻抗的实部与$R_S$匹配，而虚部通过$L_g$与$C_{gs}$谐振抵消，不引入额外的热噪声。

---

## 5.3 LNA Topologies | LNA拓扑结构

### 5.3.1 Common-Source Stage with Inductive Load | 电感性负载的共源级

A MOSFET CS stage with an inductive load $L_D$:

**Small-signal analysis (at resonance $\omega_0 = 1/\sqrt{L_D C_L}$):**

$$
A_v = \frac{v_{\text{out}}}{v_{\text{in}}} = -g_m R_P \quad \text{(5.4)}
$$

where $R_P$ is the equivalent parallel resistance of the inductor (including load and device output resistance).

**Inductor $Q$ effect:**

$$
R_P = Q_L \cdot \omega_0 L_D \quad \text{(5.5)}
$$

where $Q_L = \omega_0 L_D / r_D$ is the inductor quality factor.

> **（中文）** 电感性负载的共源级在谐振频率$\omega_0$处提供最大的阻抗变换（从感性负载变成纯电阻$R_P$）。电压增益$g_m R_P$可以很高，因为$Q_L \cdot \omega_0 L_D$可以远大于$r_D$（线圈的串联电阻）。但片上电感的$Q$值有限（$Q_L \approx 10-20$），限制了最大增益。

**Noise of Inductive Load CS Stage:**

$$
F = 1 + \frac{R_S}{R_P} + \frac{\gamma}{g_m R_S} \quad \text{(5.6)}
$$

The first term ($R_S/R_P$) is the load inductor noise contribution; the third term is the transistor channel noise.

> **（中文）** 电感性负载CS级的噪声系数包含两个主要来源：①电感负载的热噪声（$R_S/R_P$，与$Q_L$成反比）；②晶体管沟道热噪声（$\gamma/(g_m R_S)$）。当$g_m R_S$很大时，晶体管噪声项可以忽略，NF主要由负载电感的$Q$决定。

### 5.3.2 Common-Source Stage with Resistive Feedback | 电阻反馈的共源级

Adding a resistor $R_F$ from drain to gate creates feedback:

**Input impedance (with feedback):**

$$
Z_{\text{in}} \approx \frac{R_F}{1 + A_v} \quad \text{(5.7)}
$$

**Voltage gain:**

$$
A_v \approx -\frac{R_D}{R_S + \frac{1}{g_m}} \quad \text{(5.8)}
$$

**Noise Figure:**

$$
F \approx 1 + \frac{R_S}{R_D} + \frac{\gamma}{g_m R_S} + \frac{R_S}{R_F} \quad \text{(5.9)}
$$

> **（中文）** 电阻反馈CS级通过负反馈改善输入匹配（降低$Z_{\text{in}}$）、扩展带宽并控制增益。但反馈电阻$R_F$本身会贡献热噪声（$R_S/R_F$项），且$R_F$在输出和输入之间引入耦合，可能导致稳定性问题。

### 5.3.3 Common-Gate Stage | 共栅级

The CG stage has a fundamentally different input impedance:

$$
Z_{\text{in,CG}} \approx \frac{1}{g_m} \left(1 + \frac{r_O}{R_D}\right) \approx \frac{1}{g_m} \quad \text{(5.10)}
$$

**Key Property**: Input matching is inherently achieved when $1/g_m \approx 50\ \Omega$ (for $g_m \approx 20\ \text{mS}$).

> **（中文）** 共栅（CG）级是LNA设计中最重要的拓扑之一。输入阻抗近似为$1/g_m \approx 50\ \Omega$（当$g_m = 20\ \text{mS}$时），自然实现了$50\ \Omega$系统匹配，无需额外的匹配电感！但CG级的噪声系数通常比CS级差，因为源端电流噪声直接进入信号通路。

**CG Stage Noise Figure:**

The source resistance $R_S$ sees $Z_{\text{in}} \approx 1/g_m$, so the signal current is:

$$
i_{\text{sig}} = \frac{v_{\text{sig}}}{R_S + 1/g_m} \quad \text{(5.11)}
$$

The transistor noise current $\overline{i_{n,d}^2} = 4kT\gamma g_m B$ flows through $R_S$ to the output:

$$
F = 1 + \frac{\overline{i_{n,d}^2} R_S^2}{\overline{v_n^2 R_S}} = 1 + \gamma g_m R_S \quad \text{(5.12)}
$$

For $R_S = 50\ \Omega$, $g_m = 20\ \text{mS}$: $F = 1 + (2/3)(0.02)(50) = 1 + 0.667 \approx 1.67$ → $\text{NF} \approx 2.2\ \text{dB}$.

> **（中文）** CG级的NF可计算为$F = 1 + \gamma g_m R_S$。对于$50\ \Omega$系统中的$g_m = 20\ \text{mS}$ CMOS器件，NF约为$2.2\ \text{dB}$，这与CS inductive degeneration的NF接近。但CG级的优点是无需电感匹配，节省了片上面积。

### 5.3.4 Cascode CS Stage with Inductive Degeneration | 电感源简并的共源共栅级

The most popular narrowband LNA topology:

```
V_DD
 │
L_D
 │
M1 (CS) ──── M2 (cascode)
 │              │
L_g          C gs (M1)
 │              
R_S (50Ω)──────
```

**Input Impedance (with $L_S$ degeneration):**

$$
Z_{\text{in}} = \frac{1}{j\omega C_{gs}} + j\omega L_S + \frac{g_m L_S}{C_{gs}} + j\omega(L_g + L_S) 
$$

At resonance ($\omega_0 L_S = 1/(\omega_0 C_{gs})$):

$$
\text{Re}(Z_{\text{in}}) = \frac{g_m L_S}{C_{gs}} = \omega_T L_S \quad \text{(5.13)}
$$

Setting $\text{Re}(Z_{\text{in}}) = R_S = 50\ \Omega$:

$$
L_S = \frac{50\ \Omega}{\omega_T} \quad \text{(5.14)}
$$

> **（中文）** 电感源简并共源共栅LNA是窄带应用中最经典的拓扑。$L_S$（源简并电感）在输入阻抗中引入一个正实部$\omega_T L_S$，在不需要额外电阻的情况下实现$50\ \Omega$匹配！同时$L_S$是纯电感（无热噪声），不影响噪声性能。$L_g$与$C_{gs}$谐振在$\omega_0$处抵消输入阻抗的虚部。

**Voltage Gain at Resonance:**

$$
A_v = -g_m R_P \quad \text{(5.15)}
$$

where $R_P$ is the parallel combination of $r_O$ of M1, $r_O$ of M2, and the load.

**Noise Figure at Resonance:**

$$
F = 1 + \underbrace{\frac{R_S}{R_P}}_{\text{load noise}} + \underbrace{\frac{\gamma}{\alpha g_m R_S}}_{\text{transistor noise}} \quad \text{(5.16)}
$$

where $\alpha = g_{m1}/I_D$ is the transistor efficiency factor.

**Optimum $g_m$ for Minimum NF:**

Setting $\partial F/\partial g_m = 0$:

$$
(g_m R_S)_{\text{opt}} = \sqrt{\frac{\gamma}{\alpha}} \quad \text{(5.17)}
$$

For $\gamma = 2/3$, $\alpha \approx 1$: $(g_m R_S)_{\text{opt}} \approx 0.82$ → $g_m \approx 16.4\ \text{mS}$ for $R_S = 50\ \Omega$.

> **（中文）** 电感源简并LNA的NF最优化给出了$g_m R_S \approx 0.82$（对于典型CMOS参数）。这意味着$g_m \approx 16.4\ \text{mS}$（$R_S = 50\ \Omega$），对应的跨导效率$\alpha = g_m/I_D$约为$2-3\ \text{V}^{-1}\cdot\mu\text{m}$。这个$g_m$值在功耗和NF之间是合理的折中。

### 5.3.5 Variants of Common-Gate LNA | 共栅LNA的变体

#### Current-Bias-Based CG LNA | 电流偏置共栅LNA

Replace $R_S$ with a current source $I_{\text{bias}}$ to allow higher supply voltages and better linearity:

$$
Z_{\text{in}} = \frac{1}{g_m} + \frac{V_{DS}}{I_{\text{bias}}} \quad \text{(5.18)}
$$

#### CG LNA with Inductive Source Degeneration | 带源简并电感的CG LNA

Adding $L_S$ to a CG stage improves noise performance:

$$
F = 1 + \frac{R_S}{R_P} + \frac{\gamma (1 + \omega_T^2 L_S^2/R_S^2)}{g_m R_S} \quad \text{(5.19)}
$$

> **（中文）** 在CG LNA的源端加入简并电感$L_S$可以降低等效输入电导（$\approx 1/(g_m R_S^2)$），从而降低噪声。当$L_S$足够大（$\omega_T L_S \gg R_S$）时，CG LNA的NF可以接近CS inductive degeneration级的NF，但保持了CG固有的宽带输入匹配特性。

### 5.3.6 Noise-Canceling LNAs | 噪声消除LNA

A recent innovation: exploiting the fact that the noise of the input transistor and the load resistor can be simultaneously canceled at the output.

**Principle:**

$$
F = 1 + \frac{P_{\text{canceled}}}{P_{\text{signal}}} = 1 \quad \text{(ideally)} \quad \text{(5.20)}
$$

**Architecture:**

```
M1 (CS) ── R1 ── Output
  ↓               ↑
  ├─ (noise)──────┤
  M2 (CG) ── R2 ──┘
```

M1 provides forward gain; M2 (CG) provides a noise-canceling path.

> **（中文）** 噪声消除LNA是一种先进的低噪声技术。其核心思想：输入晶体管M1的噪声电流通过两条路径（CS通路和CG通路）到达输出端，相位相反而抵消（因为两条路径对信号的相位关系不同）。适当选择电路参数可以使晶体管噪声在输出端完美消除，而信号同相叠加。但噪声消除的准确性受工艺角和温度影响，实际NF改善有限。

---

## Key LNA Design Parameters Summary | LNA设计参数汇总

| Topology | NF (dB) | Gain (dB) | IIP3 (dBm) | Area | Notes |
|---|---|---|---|---|---|
| CS + $L_D$ | $\sim 2$ | $15-20$ | $-10$ to $-5$ | Medium | Requires input matching |
| CS + $R_F$ feedback | $\sim 3$ | $10-15$ | $-5$ to $0$ | Small | Broadband, no inductors |
| CG | $\sim 2.2$ | $10-15$ | $-10$ to $-5$ | Small | Inherently $50\ \Omega$ matched |
| CS + $L_S$ degeneration | $\sim 1.5-2$ | $15-20$ | $-10$ to $-5$ | Large | Best NF, narrowband |
| Noise-canceling | $\sim 1-1.5$ | $15-20$ | $-10$ | Medium | Complex, process-sensitive |

---

## Key Takeaways | 本章要点

1. **LNA determines RX sensitivity**: First-stage NF dominates due to Friis formula.
2. **Noise vs. power matching conflict**: Resolved by inductive degeneration (lossless matching element).
3. **Inductive source degeneration** provides real-part input resistance $R_{\text{in}} = \omega_T L_S$ without adding thermal noise.
4. **CG LNA** inherently provides $Z_{\text{in}} \approx 1/g_m \approx 50\ \Omega$, but NF $\approx 1 + \gamma g_m R_S$.
5. **Cascode** improves reverse isolation ($S_{12}$) and increases output impedance without degrading NF.
6. **Optimum $g_m$** for minimum NF: $(g_m R_S)_{\text{opt}} \approx \sqrt{\gamma/\alpha}$.
7. **$1/f$ noise** can be a limiting factor in direct-conversion RX; large devices or special circuits (chopper stabilization) needed.
