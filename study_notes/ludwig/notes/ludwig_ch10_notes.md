---
title: "Chapter 10 — Oscillators and Mixers"
book: "RF Circuit Design — 2nd Ed."
author: "Reinhold Ludwig, Gene Bogdanov"
pages: "539–606"
processed: "2026-05-07"
tags: [oscillator, Colpitts, Hartley, negative-resistance, mixer, RF-front-end]
---

# Chapter 10: Oscillators and Mixers | 第10章：振荡器与混频器

Radio and radar systems require stable sinusoidal oscillations at specific carrier frequencies to enable modulation and frequency mixing. While early systems operated in the low-to-mid MHz range, modern RF systems routinely exceed 1 GHz. This creates a need for specialized oscillator circuits that provide stable, spectrally pure sinusoids. The fundamental challenge is that oscillators exploit inherently nonlinear circuit behavior that linear tools can only partially describe — a complication compounded by frequency-dependent loading and parasitic effects at high frequencies.

This chapter is organized in two major parts:

1. **Oscillators** — from the Barkhausen criterion through Colpitts, Hartley, crystal, and high-frequency S-parameter-based designs (DRO, YIG, VCO, Gunn).
2. **Mixers** — from basic frequency translation through single-ended, single-balanced, and double-balanced diode/BJT/FET implementations.

---

## 10.1 Basic Oscillator Model | 基本振荡器模型

### 10.1.1 Feedback Oscillator Principle — The Barkhausen Criterion | 反馈振荡器原理——Barkhausen判据

At the core of any oscillator is a loop that produces positive feedback at a chosen frequency $\omega_0$. The generic closed-loop system consists of an amplification stage $H_A(\omega)$ and a feedback stage $H_F(\omega)$.

The closed-loop transfer function is:

$$H_{CL}(\omega) = \frac{H_A(\omega)}{1 - H_A(\omega) H_F(\omega)}$$

Since an oscillator has no external input ($V_{in} = 0$), a non-zero output $V_{out}$ can only arise if the **denominator is zero**:

$$\boxed{H_A(\omega_0) H_F(\omega_0) = 1} \tag{10.2}$$

This is the **Barkhausen criterion** (loop gain equation). Decomposing $H_F(\omega) = H_{Fr}(\omega) + jH_{Fi}(\omega)$ with a real amplifier gain $H_{A0}$, the condition becomes:

$$H_{A0} \, H_{Fr}(\omega_0) = 1, \qquad H_{Fi}(\omega_0) = 0 \tag{10.3}$$

- The **magnitude** condition $H_{A0}|H_F| = 1$ ensures steady-state amplitude.
- The **phase** condition $|H_F(\omega_0)| = 0^\circ$ ensures constructive self-coherence.

> **工程直觉 — Barkhausen判据**: 该判据是**稳态**条件。启动振荡需要 $|H_A H_F| > 1$（环路增益大于1，使振幅不断增大），随后非线性饱和机制将环路增益压回1，使振幅稳定。这是振荡器启动与稳定的本质。

For increasing output voltage the loop gain must initially exceed unity. The amplitude eventually stabilizes due to the nonlinear decrease in gain (see Figure 10-2), creating a stable operating point at $|V_{out}| = V_Q$ where $H_{A0} = H_{Fr}(\omega_0)$.

### 10.1.2 Negative Resistance Devices | 负阻器件

The series resonance circuit of Figure 10-3 — comprising resistance $R$, inductance $L$, and capacitance $C$, driven by a current-controlled voltage source — obeys:

$$v(t) = Ri(t) + L\frac{di}{dt} + \frac{1}{C}\int i\,dt \tag{10.4}$$

Setting the source term to zero (steady state), the homogeneous solution is $i(t) = I_0 e^{\alpha t} \cos(\omega_0 t)$ with $\alpha = -R/(2L)$ and $\omega_0 = \sqrt{1/(LC) - (R/(2L))^2}$. Since $\alpha < 0$, the natural response decays to zero. To sustain oscillation we need an **active element that introduces negative resistance** to cancel $R$.

If the device voltage-current relation is approximated by a power series:

$$v(i) = v_0 + R_1 i + R_2 i^2 + \cdots$$

and we substitute the first two terms into (10.4), the coefficient of $di/dt$ becomes $R + R_1$. Setting this coefficient to zero gives:

$$\boxed{R_1 = -R} \tag{10.7}$$

The device must possess a **negative differential resistance** $R_1 < 0$. Oscillation startup requires $R_1 < -R$ (positive attenuation coefficient), placing poles in the right-half complex frequency plane.

**工程直觉 — 负阻振荡**: 负阻不是"魔法"，而是主动器件的非线性 $I$–$V$ 曲线在特定工作点处的微分电阻为负。隧道二极管是最经典的负阻器件，其 $I$–$V$ 特性在峰值电压附近呈"S"形负斜率，广泛用于10 GHz–100 GHz振荡器。

A **tunnel diode** oscillator circuit is shown in Figure 10-4. Since the tunnel diode already has intrinsic capacitance $C_d$, no external capacitor is needed. This configuration supports oscillation frequencies up to ~100 GHz.

### 10.1.3 Colpitts, Hartley, and Feedback Topologies | Colpitts、 Hartley与反馈拓扑

For **feedback oscillator design**, we examine two-port feedback networks (Pi-type and T-type, Figure 10-5). For a Pi-network with high-impedance input/output assumptions, the transfer function is:

$$H_F(\omega) = \frac{Z_1}{Z_1 + Z_3} \cdot \frac{1/Z_2}{1/Z_2 + 1/(Z_1+Z_3)} \tag{10.9}$$

Using a simple low-frequency FET model with voltage gain $\mu$ and output resistance $R_B$, the loop equation yields the closed-loop gain:

$$H_{CL}(\omega) = \frac{\mu Z_c}{Z_c + Z_3 + (\mu+1)Z_1 + Z_2} \tag{10.12}$$

Eliminating resistive loss requires **purely reactive components** $Z_i = jX_i$. For the denominator to be real: $X_1 + X_2 + X_3 = 0$, implying one reactance equals the negative sum of the other two. Negative-valued reactances correspond to capacitors; positive ones to inductors.

**Two canonical topologies:**

| Oscillator Type | $X_1$ | $X_2$ | $X_3$ | Resonant Condition |
|---|---|---|---|---|
| **Hartley** | $\omega L_1$ | $\omega L_2$ | $-\frac{1}{\omega C_3}$ | $\omega = \frac{1}{\sqrt{(L_1+L_2)C_3}}$ |
| **Colpitts** | $-\frac{1}{\omega C_1}$ | $-\frac{1}{\omega C_2}$ | $\omega L_3$ | $\omega = \sqrt{\frac{C_1+C_2}{L_3 C_1 C_2}}$ |
| **Clapp** | $-\frac{1}{\omega C_1}$ | $-\frac{1}{\omega C_2}$ | $\omega L_3$ (fixed) + varactor | Tuning via $C_3$ variation |

The **Colpitts oscillator** (Figure 10-7b) uses a capacitive voltage divider ($C_1$, $C_2$) in the feedback loop and is preferred at higher frequencies due to the more realizable component values. The **Hartley oscillator** (Figure 10-7a) uses an inductive divider ($L_1$, $L_2$).

> **工程直觉 — 选型判断**: 当所需振荡频率对应的电感 $L$ 值过小时（难以实现），优先选用 Colpitts 拓扑，因为小电感可用较小电容替代。反之，当所需电容值过小时（如片上实现），Hartley 拓扑更合适。Clapp 是 Colpitts 的变体，通过在谐振回路中加入额外可调电容（变容二极管）实现频率调节。

**Design procedure for Colpitts oscillators** uses h-parameters (hybrid parameters). The determinant conditions yield:

$$\text{Resonance: } \omega_0 = \sqrt{\frac{C_1 + C_2}{L_3 C_1 C_2}} \quad \Rightarrow \quad \omega_0^2 = \frac{C_1 + C_2}{L_3 C_1 C_2} \tag{10.15}$$

Under the assumption $h_{11} \gg 4(h_{11}h_{22} - h_{12}h_{21})$, the capacitance ratio satisfies:

$$\frac{C_1}{C_2} \approx \frac{h_{11}h_{22} - h_{12}h_{21}}{h_{11}^2} \tag{10.17}$$

**Example 10-1** designs a 200 MHz Colpitts BJT oscillator with given DC h-parameters. At $f = 200$ MHz the h-parameters differ only slightly from DC values, confirming the approximate analysis — but at higher frequencies, frequency-dependent phase shifts invalidate the DC approximation, requiring full complex h-parameter analysis.

### 10.1.4 Crystal Oscillators — Quartz Resonators | 晶体振荡器——石英谐振器

Quartz crystals exploit the **piezoelectric effect**: an applied electric field causes mechanical deformation. They offer:

- **Quality factor** $Q$ up to $10^5$–$10^6$ (vs. $10^2$–$10^3$ for LC tanks)
- Superior frequency stability and temperature immunity
- Limitation: mechanical construction restricts operation to $\lesssim 250$ MHz

The **quartz crystal equivalent circuit** (Figure 10-10) has:

| Element | Physical Meaning | Typical Value |
|---|---|---|
| $L_q$ | Acoustic mass of the crystal | 0.1 mH – 100 H |
| $R_q$ | Mechanical damping losses | ~25 Ω |
| $C_q$ | Elastic compliance | 0.01 – 0.3 pF |
| $C_0$ | Electrode capacitance (package shunt) | 1 – 10 pF |

The admittance is:

$$Y(\omega) = j\omega C_0 + \frac{1}{R_q + j(\omega L_q - 1/(\omega C_q))} \tag{10.19}$$

Setting the imaginary part $B(\omega) = 0$ gives the **series resonance** $\omega_{s} = 1/\sqrt{L_q C_q}$ and **parallel resonance** $\omega_{p} = \sqrt{(C_q + C_0)/(L_q C_q C_0)}$. These are very closely spaced because $C_0 \gg C_q$ typically:

$$\omega_s = \frac{1}{\sqrt{L_q C_q}}, \qquad \omega_p \approx \omega_s\left(1 + \frac{C_q}{2C_0}\right) \tag{10.21a,b}$$

> **工程直觉 — 石英晶体选型注意**: 石英晶体有**多个谐振点**（series 和 parallel），且附近可能有 spurious resonances。设计时必须检查 crystal 的 susceptance vs. frequency 曲线（Figure 10-11），确保所需振荡频率落在 series resonance 附近且远离 spurious modes。

---

## 10.2 High-Frequency Oscillator Configuration | 高频振荡器配置 (S-Parameter Design)

As frequency enters the GHz range, transmission-line effects become significant, and **S-parameters** replace lumped h-parameters. The Barkhausen criterion must be reformulated in terms of reflection coefficients.

### 10.2.1 S-Parameter Formulation of the Oscillation Conditions | 振荡条件的S参数表述

Starting from the signal flow graph (Figure 10-12), the **input reflection coefficient** with source matched to $Z_0$ is:

$$\Gamma_{in} = S_{11} + \frac{S_{12}S_{21}\,\Gamma_S}{1 - S_{22}\Gamma_S} \tag{10.24}$$

The **loop gain** expressed as the ratio $b_{in}/b_s$ (where $b_s = \Gamma_S/(1-\Gamma_{in}\Gamma_S)$) gives the loop condition:

$$\Gamma_{in}\,\Gamma_S = 1 \quad \Longleftrightarrow \quad |T_{in}| \cdot |\Gamma_S| = 1 \tag{10.25}$$

Including the **Rollett stability factor** $k = (1 - |S_{11}|^2 - |S_{22}|^2 + |\Delta|^2)/(2|S_{12}S_{21}|)$, the oscillation conditions are:

$$\boxed{k < 1}, \qquad \boxed{|\Gamma_{in}| \cdot |\Gamma_S| = 1}, \qquad \boxed{|\Gamma_{out}| \cdot |\Gamma_L| = 1} \tag{10.26a-c}$$

Condition (10.26a) ensures the transistor is **potentially unstable**. Then (10.26b) and (10.26c) ensure oscillations build up at input and output ports respectively. An important identity relates the two:

$$\Gamma_L = \frac{1}{\Gamma_{out}} \tag{10.30}$$

> **工程直觉 — 振荡条件本质**: $k < 1$ 仅表示器件可能振荡，真正起振还需正确的源和负载阻抗配合。若 $|\Gamma_{in}||\Gamma_S| > 1$，振荡在输入端口建立，输出端口自动满足条件（通过 10.30 的互逆关系）。反之亦然。

**Example 10-3** shows that adding a small base inductance (0.6 nH) to a BJT at 2 GHz minimizes $k$ (maximizes instability) by providing positive feedback. Even PCB via parasitics (~0.6 nH) can be sufficient to trigger oscillation at GHz frequencies.

### 10.2.2 Fixed-Frequency Lumped-Element Oscillator Design | 固定频率集总元件振荡器设计

**Design procedure (Example 10-4)** for a series-feedback BJT oscillator at $f_0 = 1.5$ GHz:

1. **Compute $k$** — check potential instability: $k = 0.63 < 1$ (potentially unstable ✓)
2. **Plot input stability circle** — find allowed $\Gamma_S$ region (outside the stability circle for $|S_{22}| < 1$)
3. **Choose $\Gamma_S$** near $S_{11}^{-1}$ to maximize $|\Gamma_{out}|$ — in practice, pick $\Gamma_S = 0.65\angle-125^\circ$ (not exactly $S_{11}^{-1}$ to avoid extreme sensitivity to load variations)
4. **Compute output matching network** from $\Gamma_L = 1/\Gamma_{out}$ — yields $Z_L = (55.6 - j4.57)\,\Omega$, implemented as series $R + L$

> **工程直觉 — 负载敏感性**: 若选取 $\Gamma_S = S_{11}^{-1}$，则 $\Gamma_{out} \to \infty$，理论上对应 $Z_L = Z_0 = 50\,\Omega$。但此时 $Z_L$ 任何微小偏差都会导致振荡停止（$\Gamma_L \neq 1/\Gamma_{out}$）。工程上取 $\Gamma_S$ 接近但不完全等于 $S_{11}^{-1}$，在稳定性与起振条件之间取得平衡。

### 10.2.3 Microstrip Oscillator Design | 微带振荡器设计

At microwave frequencies, lumped inductors become comparable to lead inductances and parasitic capacitances. **Microstrip transmission lines** replace lumped elements. Example 10-5 designs a **GaAs FET oscillator at 10 GHz** using:

- A short-circuited stub (length $\theta = 48.5^\circ$) to replace the feedback inductor
- Input: open-circuit stub with $\theta = 80^\circ$ for matching
- Output: 50 Ω line with $\theta = 67^\circ$ plus short-circuit stub ($\theta = 66^\circ$) for impedance transformation

The complete design uses six microstrip lines (Table 10-2) on a FR-4 substrate (40 mil thick).

### 10.2.4 Dielectric Resonator Oscillators (DRO) | 介质谐振振荡器（DRO）

A **dielectric resonator (DR)** — a cylindrical "puck" — provides $Q_u$ up to $10^5$ with temperature stability better than $\pm 10$ ppm/$^\circ$C. Near resonance it is modeled as a **parallel RLC circuit** (Figure 10-20), characterized by:

$$Q_u = \frac{P}{Q_l} = (1 + P)\,Q_l, \qquad P = \frac{R_{ext}}{R_{eq}} \tag{10.34}$$

where $P$ is the coupling coefficient (typically 2–20). The DR is placed in proximity to a microstrip line; its impedance near resonance is:

$$Z_{DR} \approx R_{eq}\,\frac{1}{1 + j2Q_l(\Delta f/f_0)} \tag{10.36}$$

A DR-oscillator (DRO) achieves much narrower $|\Gamma_{out}| > 1$ bandwidth compared to a conventional design (Figure 10-23), resulting in high frequency selectivity and reduced drift. The tuning screw allows small adjustments in the range $\pm 0.01 f_0$.

> **工程直觉 — DRO vs. LC振荡器**: DRO 的 Q 值比 LC 振荡器高 2–3 个数量级，因此频率稳定性极好。但 DR 的几何尺寸随频率降低而增大（$\lambda/4$ 量级），低频(< ~2 GHz) 应用中体积过大是其主要限制。

### 10.2.5 YIG-Tuned Oscillators | YIG调谐振荡器

**Yttrium Iron Garnet (YIG)** is a ferrimagnetic material whose effective permeability — and hence the resonance frequency of its equivalent parallel circuit — can be **externally controlled** via a static bias field $H_0$:

$$\omega_0 = 2\pi\gamma H_0, \qquad \gamma = 2.8 \ \frac{\text{MHz}}{\text{Oe}} \tag{10.42}$$

YIG oscillators offer **wideband tuning over more than a decade of bandwidth**, far exceeding the 0.01–1% tuning range of dielectric resonators. The equivalent inductance and capacitance of the YIG sphere are:

$$L_0 = \frac{\mu_0 a^3 \omega_s}{d^2}, \qquad C_0 = \frac{1}{L_0 \omega_0^2} \tag{10.42b,c}$$

where $a$ is the sphere radius and $d$ the coupling loop diameter.

### 10.2.6 Voltage-Controlled Oscillators (VCO) | 压控振荡器（VCO）

**Varactor diodes** provide voltage-tunable capacitance: $C_V = C_{V0}(1 - V/V_{bi})^{-\gamma}$, typically $\gamma \approx 0.5$ for abrupt junctions. Replacing $C_3$ in a Colpitts or Clapp feedback loop with a reverse-biased varactor yields a VCO.

The **varactor-controlled Clapp oscillator** (Figure 10-25) input resistance is negative:

$$R_{in} = \frac{-\mu R_E}{1 + \omega^2 C_V^2 R_E^2} < 0 \tag{10.46a}$$

The oscillation frequency is:

$$f_0 = \frac{1}{2\pi\sqrt{L_3\,\frac{C_1 C_2}{C_1 + C_2 + C_V}}} \tag{10.46b}$$

For sustained oscillations: $R_V \leq |R_{in}|$, where $R_V$ is the varactor's series resistance.

**工程直觉 — VCO 设计**: 变容二极管提供电子调谐，但调谐范围受 $C_V$ 变化率和品质因子限制。设计时需确保变容管的串联电阻 $R_V$ 在整个频率调节范围内满足 $R_V \leq |R_{in}|$，否则振荡停止。与 YIG 的磁场调谐相比，变容管调谐速度快但 Q 值低、相位噪声差。

### 10.2.7 Gunn Diode Oscillators | Gunn二极管振荡器

The **Gunn element** exploits the **transferred-electron (Gunn) effect** in GaAs and InP: as the electric field increases beyond a threshold $E_{th}$, electrons transfer from the central valley to satellite valleys, reducing mobility and producing a **negative differential resistance** region in the $I$–$V$ characteristic. This creates traveling **dipole domains** from cathode to anode.

The **oscillation frequency** is approximately:

$$f_0 \approx \frac{v_d}{L}, \qquad v_d \approx 10^7 \ \frac{\text{m}}{\text{s}} \tag{10.47}$$

For $L = 10\,\mu\text{m}$ domain length: $f_0 \approx 1$ GHz. Gunn oscillators operate from **1 GHz to 100 GHz** at power levels up to ~1 W.

External DC bias can influence domain velocity, enabling tuning within ~1% of the resonance frequency. A typical implementation (Figure 10-28) uses a Gunn element connected to a $\lambda/4$ microstrip line, coupled to a dielectric resonator.

---

## 10.3 Basic Characteristics of Mixers | 混频器基本特性

Mixers perform **frequency translation** — combining an RF input signal with a local oscillator (LO) through a **nonlinear (quadratic or higher) transfer characteristic** to produce new frequencies at the output. The primary application is **downconversion** in heterodyne receivers: $f_{IF} = |f_{RF} - f_{LO}|$, where the IF is more manageable for subsequent filtering and signal processing.

### 10.3.1 Mixer Fundamentals — Taylor Series Analysis | 混频器基础——Taylor级数分析

A **Schottky diode** follows the Shockley equation:

$$I(V) = I_S\left[\exp\left(\frac{qV}{kT}\right) - 1\right]$$

A **MESFET** has an approximately square-law transfer characteristic:

$$I_D(V_{GS}) \approx I_{DSS}\left(1 - \frac{V_{GS}}{V_p}\right)^2$$

The combined input voltage (bias + RF + LO) is:

$$V = V_Q + V_{RF}\cos(\omega_{RF}t) + V_{LO}\cos(\omega_{LO}t) \tag{10.55}$$

Expanding the current via a Taylor series around $V_Q$ and collecting terms:

$$I(V) \approx A\,V_{RF}\cos(\omega_{RF}t) + A\,V_{LO}\cos(\omega_{LO}t) + \frac{B}{2}V_{RF}V_{LO}\cos[(\omega_{RF} \pm \omega_{LO})t] + \cdots \tag{10.58}$$

The **cross-product term** $\frac{B}{2}V_{RF}V_{LO}$ generates the desired mixing products at $\omega_{RF} \pm \omega_{LO}$. All higher-order terms ($v^3$, etc.) generate additional unwanted intermodulation products.

**工程直觉 — FET vs. 二极管混频**: FET 的转移特性更接近平方率，对高阶非线性项的敏感度低于指数特性的二极管/BJT。这意味着 FET 混频器的三阶互调失真(IMD)更小，更适合需要高动态范围的应用。

### 10.3.2 Frequency Domain and Image Frequencies | 频域与镜像频率

Mixing produces both **lower sideband (LSB)** $\omega_{RF} - \omega_{LO}$ and **upper sideband (USB)** $\omega_{RF} + \omega_{LO}$ — together called **double sideband (DSB)**. The **image frequency** problem arises when an interferer at $\omega_{im} = \omega_{LO} - (\omega_{RF} - \omega_{LO}) = 2\omega_{LO} - \omega_{RF}$ also maps to the same IF after mixing. This requires an **image rejection filter** (or image-rejection mixer architecture) before the mixer.

> **工程直觉 — 镜像抑制**: 镜像频率与有用信号频率关于 LO 对称 ($\omega_{im} = 2\omega_{LO} - \omega_{RF}$)。若不抑制，镜像干扰将无法与有用信号区分，直接叠加在 IF 输出上。镜像抑制滤波器在高频段要求极高的 Q 值（如 Example 10-8 中，未下变频前 $Q = 94.5$，下变频后 $Q = 10$），这正是混频器的核心价值所在。

**Example 10-8** (LO frequency selection): For $f_{RF} = 1.89$ GHz and $f_{IF} = 200$ MHz, either $f_{LO} = 1.69$ GHz (**low-side injection**) or $f_{LO} = 2.09$ GHz (**high-side injection**) is valid. Low-side injection is generally preferred because lower LO frequencies are easier to generate and process.

### 10.3.3 Mixer Performance Figures of Merit | 混频器性能指标

| Parameter | Definition | Typical Value |
|---|---|---|
| **Conversion Loss (CL)** | $CL = 10\log_{10}(P_{RF}/P_{IF})$ [dB] | 5–10 dB (diode); < 0 dB (FET with gain) |
| **Noise Figure (NF)** | $F = (P_{noise,IF}/(G_C \cdot P_{noise,RF})) + (P_{noise,device}/(G_C \cdot P_{noise,RF}))$ | 4–8 dB ( Schottky); 2–5 dB (FET) |
| **Conversion Gain (CG)** | $CG = 10\log_{10}(P_{IF}/P_{RF})$ [dB] | Active mixers: 5–15 dB |
| **1 dB Compression Point** | $P_{IF}$ deviates by 1 dB from ideal linear response | RF input power level |
| **Third-Order Intercept (IP3)** | Intercept of linear IMD response and desired signal response | High value = better linearity |
| **Isolation (LO-RF, LO-IF, RF-IF)** | Coupling between ports [dB] | 20–40 dB typical |
| **Dynamic Range** | Input power range without performance degradation | Set by IP3 and noise floor |

The **two-tone intermodulation test** measures third-order IMD: signals at $f_1$ and $f_2$ produce intermodulation products at $2f_1 - f_2$ and $2f_2 - f_1$, which may fall near the desired IF and cannot be filtered out — making IP3 a critical specification.

### 10.3.4 Single-Ended Mixer Designs | 单端混频器设计

**Diode single-ended mixer** (Figure 10-33a): Simplest configuration using one Schottky diode. RF and LO are combined and applied to the diode; output is bandpass-filtered to select the IF. Main drawback: no port isolation — LO can reradiate through the antenna.

**FET single-ended mixer** (Figure 10-33b): Provides gain (conversion gain instead of loss), port isolation, and lower noise figure due to the nearly square-law characteristic. Design follows the same matching methodology as RF amplifiers, with special attention to:

- **Input matching**: Match to $Z_{in}(\omega_{RF})$ at RF and $Z_{in}(\omega_{LO})$ at LO
- **Output matching**: Match to $Z_{out}(\omega_{IF})$ at IF
- **Isolation requirements**: Short circuit at the output for RF and at the input for IF (Figure 10-35)

**Example 10-9** details a BJT mixer design at $f_{RF} = 1900$ MHz, $f_{IF} = 200$ MHz. Key steps:

1. DC bias network: compute $R_1$, $R_2$ from desired $V_{CE}$, $I_C$
2. LO coupling: small capacitor $C_{LO} = 0.2$ pF provides isolation but introduces insertion loss of 13.6 dB at LO — still tolerable
3. Input matching network: shunt inductor + series capacitor topology, with $C_{B1} = 120$ pF chosen to create series resonance at IF for a **solid short at IF** while maintaining RF isolation
4. Output matching: similar L-C topology with additional capacitance $C_g = 120$ pF for RF grounding

> **工程直觉 — 混频器匹配的特殊挑战**: 混频器的输入端需要同时工作在 RF 和 LO 两个相近频率，且输出端在 IF。匹配网络必须同时满足"对 RF/LO 呈现高阻抗，对 IF 呈现短路"（或反之）的矛盾需求。多功能匹配网络的设计是混频器设计的核心难点。

### 10.3.5 Single-Balanced Mixers | 单平衡混频器

The **single-balanced mixer** (Figure 10-41) uses a **quadrature (90°) hybrid coupler** to drive two antiparallel diodes. Advantages:

- **Broadband operation** with good VSWR
- **Noise suppression/cancellation**: the opposite diode arrangement with 90° phase shift provides noise cancellation (see Problem 10.22)
- **Spurious mode rejection** of certain harmonics

**MESFET single-balanced mixer** (Figure 10-42): Two MESFETs driven by 90° and 180° hybrids. The 180° hybrid is needed because the second FET cannot be reversed like an antiparallel diode pair. This circuit provides LO→RF and LO→IF isolation but no RF→IF isolation — requiring a low-pass filter at the output.

### 10.3.6 Double-Balanced Mixers | 双平衡混频器

The **double-balanced mixer** (Figure 10-43) uses **four diodes in a ring (rectifier) configuration**, providing:

- **Complete isolation** between all three ports (LO, RF, IF)
- **Suppression of all even harmonics** of both LO and RF signals
- Trade-offs: higher LO drive power required and increased conversion loss (~2–3 dB higher than single-balanced)

> **工程直觉 — 选型决策树**: 入门级应用选**单端二极管混频器**（最简单的结构）；宽频带、低噪声需求选**单端FET混频器**（有增益）；抑制偶次谐波和镜像需求选**单平衡混频器**；最高隔离度、最佳 spurious rejection 选**双平衡混频器**（代价是更高的LO驱动功耗和更大的转换损耗）。

---

## 10.4 RF Front-End Architecture | 射频前端架构

A complete **RF front-end** (receiver chain) integrates the LNA, mixer, local oscillator, and filter components described in Chapters 9 and 10 into a coherent system.

### 10.4.1 Heterodyne Receiver Structure | 超外差接收机结构

The canonical **heterodyne receiver** (Figure 10-29) works as follows:

1. **LNA** (Low-Noise Amplifier): amplifies the weak received RF signal while adding minimal noise
2. **Image filter**: suppresses the image frequency before the mixer (placed either before or after the LNA depending on LNA noise figure and filter selectivity)
3. **Mixer (downconverter)**: multiplies RF with LO to produce IF
4. **IF filter + amplifier**: channel selection and amplification
5. **Detector/demodulator**: extracts baseband signal

Key system-level trade-offs:

| Design Decision | Consideration |
|---|---|
| **IF selection** | Lower IF → easier channel filtering, but image problem more severe; Higher IF → better image rejection, but harder IF design |
| **LO injection** | Low-side ($f_{LO} < f_{RF}$) preferred (easier LO generation) |
| **LNA-mixer interface** | Gain distribution: high LNA gain reduces mixer noise contribution but may cause mixer compression |
| **Filter Q requirements** | Without mixing: $Q = f_{RF}/BW$ (Example 10-8: $Q = 94.5$); With mixing: $Q = f_{IF}/BW$ (Example 10-8: $Q = 10$) |

### 10.4.2 Receiver Dynamic Range and Spurii | 接收机动态范围与杂散响应

Real receivers face **spurious responses** from intermodulation products (especially second and third order) that fall within the IF band. The **second-order intercept point (IP2)** and **third-order intercept point (IP3)** characterize these.

The **spurious-free dynamic range (SFDR)** is:

$$SFDR = \frac{2}{3}(IIP_3 - NF) + \frac{2}{3}\left(10\log_{10}(kT_0 B)\right) \ [\text{dB}] \tag{10.113}$$

where $kT_0 B$ is the thermal noise floor. SFDR represents the range between the noise floor and the input power level at which third-order intermodulation products equal the noise floor.

### 10.4.3 Integrated Front-End Design Considerations | 集成前端设计考虑

Practical RF front-end design balances:

- **Gain distribution**: Too much LNA gain → mixer overdrive and compression; Too little → system noise figure dominated by mixer
- **LO isolation**: LO leakage into the RF path can cause reciprocal mixing with strong interferers
- **Frequency planning**: Careful choice of IF and LO frequencies to push image frequencies and spurious responses out of band
- **PCB layout**: At GHz frequencies, microstrip/strip-line effects, via parasitics, and grounding become critical

**工程直觉 — 系统级设计核心**: RF 前端设计是一个多约束优化问题，核心是在噪声系数(NF)、线性度(IP3)、动态范围(DR)、功耗和成本之间取得平衡。混频器在此扮演"频率翻译器"的角色，其非线性特性既是优势（频率转换）也是威胁（互调失真）。优秀的系统架构师懂得在链路的每一级合理分配这些指标，而不是在某一环节点上过度设计。

---

## 10.5 Summary | 本章小结

### Key Oscillator Equations | 关键振荡器公式

| Topic | Equation | Significance |
|---|---|---|
| **Barkhausen criterion** | $H_A(\omega_0)H_F(\omega_0) = 1$ | Fundamental oscillation condition |
| **Loop gain magnitude** | $\|H_A H_F\| > 1$ (startup), $= 1$ (steady state) | Distinguishes startup from stable oscillation |
| **Colpitts resonance** | $\omega_0 = \sqrt{(C_1+C_2)/(L_3 C_1 C_2)}$ | Frequency of Colpitts oscillator |
| **Hartley resonance** | $\omega_0 = 1/\sqrt{(L_1+L_2)C_3}$ | Frequency of Hartley oscillator |
| **Quartz series resonance** | $\omega_s = 1/\sqrt{L_q C_q}$ | Crystal series resonance |
| **Quartz parallel resonance** | $\omega_p = \sqrt{(C_q+C_0)/(L_q C_q C_0)}$ | Crystal parallel resonance |
| **S-parameter oscillation** | $k < 1$, $\Gamma_{in}\Gamma_S = 1$, $\Gamma_{out}\Gamma_L = 1$ | High-frequency oscillation conditions |
| **DRO impedance** | $Z_{DR} \approx R_{eq}/(1 + j2Q_l\Delta f/f_0)$ | Parallel resonant model near resonance |
| **Gunn oscillation freq.** | $f_0 \approx v_d/L$ | Domain transit frequency |

### Key Mixer Equations | 关键混频器公式

| Topic | Equation | Significance |
|---|---|---|
| **Mixing product** | $f_{IF} = |f_{RF} \pm f_{LO}|$ | Downconversion and upconversion frequencies |
| **Diode/Taylor expansion** | $I(V) \approx A\,V + B\,V^2/2 + \cdots$ | Source of nonlinear mixing |
| **Cross-term frequency** | $\cos[(\omega_{RF} \pm \omega_{LO})t]$ | Desired mixing products from $V_{RF}V_{LO}$ term |
| **Image frequency** | $f_{im} = f_{LO} - (f_{RF} - f_{LO}) = 2f_{LO} - f_{RF}$ | Frequency that also maps to IF |
| **Conversion loss** | $CL = 10\log_{10}(P_{RF}/P_{IF})$ [dB] | Passive diode mixer figure of merit |
| **Mixer noise figure** | $F = (P_{n,IF}/(G_C P_{n,RF})) + (P_{n,device}/(G_C P_{n,RF}))$ |accounts for conversion gain and noise contributions |

### Chapter-Level Engineering Intuition | 本章工程直觉

> **振荡器与放大器的根本区别**: 放大器是"确定性"的线性网络，设计者通过选择 $\Gamma_S$ 和 $\Gamma_L$ 优化增益；振荡器是"非确定性"的非线性系统，设计者通过主动制造不稳定（$k < 1$）并选择正确的端接来**强制**系统自激。振荡器设计在 GHz 以上频段更多是"艺术"而非精确工程，因为寄生参数、非线性 S-parameter、以及制造容差都会显著影响实际性能。

> **混频器的核心矛盾**: 混频器需要非线性来完成频率转换，但非线性同时产生高阶互调失真（IM3, IM5...）。FET 的准平方率特性天然优于指数特性的二极管/BJT，在动态范围要求高的系统中应优先选用有源混频器（FET）而非无源二极管混频器。同时，混频器的端口隔离度（LO↔RF↔IF）是系统架构的关键约束，双平衡混频器提供最佳隔离但代价最高。

> **系统架构中的频率规划**: 在设计 RF 前端时，应优先利用混频器的频率平移能力降低 IF 以简化后续滤波，而不是试图在 RF 频率直接进行高 Q 滤波（需要 $Q = f_{RF}/BW \gg 1$）。合理的 IF 选择和镜像抑制是系统灵敏度（sensitivity）的决定因素。

---

*Chapter 10 ends. Problems 10.1–10.31 cover oscillator feedback analysis, S-parameter stability, Colpitts/Hartley design, crystal resonance, DRO design, and mixer conversion loss / NF calculations.*
