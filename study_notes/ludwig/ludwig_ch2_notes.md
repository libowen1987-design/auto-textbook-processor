---
title: "Chapter 2 — Transmission Line Analysis"
book: "RF Circuit Design — 2nd Ed."
author: "Reinhold Ludwig, Gene Bogdanov"
pages: "51–107"
processed: "2026-05-03"
tags: [transmission-line, microstrip, reflection-coefficient, VSWR, impedance-matching, quarter-wave]
---

# Chapter 2: Transmission Line Analysis

> **Overview:** This chapter introduces transmission line theory as the foundation of RF circuit analysis. It covers the transition from lumped to distributed parameter representation, derivation of the telegrapher's equations, characteristic impedance, reflection coefficient, VSWR, impedance transformation, microstrip line design, and power considerations for sourced/loaded lines.

---

## 2.1 Why Transmission Line Theory?

- When wavelength $\lambda$ becomes comparable to circuit dimensions, voltages and currents are no longer spatially uniform → Kirchhoff's laws fail.
- **Rule of thumb:** when average component size $l_A > \lambda/10$, transmission line theory must be applied.
- At $f = 1$ MHz, $\lambda \approx 95$ m → 1.5 cm wire is negligible. At $f = 10$ GHz, $\lambda \approx 0.95$ cm → the same wire spans $2/3$ of a wavelength.
- Solution: subdivide the line into infinitesimal segments $\Delta z$ over which voltage/current are constant → **distributed parameter** representation ($R, L, C, G$ per unit length).

---

## 2.2 Examples of Transmission Lines

### Two-Wire Line
- Two parallel conductors; fields extend to infinity → high radiation loss, acts as antenna.
- Limited RF use (TV antenna connections); common in 50–60 Hz power lines (where distance spans km → $\lambda \approx 5000$ km, so distributed effects matter).

### Coaxial Cable
- Inner conductor (radius $a$), outer conductor (radius $b$), dielectric between them.
- Outer conductor grounded → shields against radiation and interference.
- Common dielectrics: polystyrene ($\varepsilon_r = 2.5$, $\tan\Delta_e = 0.0003$ @ 10 GHz), polyethylene ($\varepsilon_r = 2.3$, $0.0004$), teflon ($\varepsilon_r = 2.1$, $0.0004$).

### Microstrip Lines
- Planar conductor trace on dielectric substrate over ground plane (Fig. 2-6).
- Field leakage depends on $\varepsilon_r$: high $\varepsilon_r$ (e.g., alumina $\varepsilon_r = 10$) confines fields better than low $\varepsilon_r$ (teflon epoxy $\varepsilon_r = 2.55$).
- Multilayer (sandwich) configurations reduce radiation loss further.

### Parallel-Plate Line
- Two parallel conducting plates separated by dielectric.
- Low impedance, high-power applications.
- Used as the canonical geometry for analytical derivation of line parameters.

---

## 2.3 Equivalent Circuit Representation

The transmission line is segmented into length $\Delta z$, with per-unit-length parameters:

- $R$: series resistance (conductor loss) [$\Omega$/m]
- $L$: series inductance (mutual + self) [H/m]
- $G$: shunt conductance (dielectric loss) [S/m]
- $C$: shunt capacitance [F/m]

**Advantages:** intuitive, two-port network representation, KVL/KCL applicable microscopically, expandable to macroscale.
**Disadvantages:** one-dimensional (no fringing fields), neglects hysteresis nonlinearities.

---

## 2.4 Theoretical Foundation

### Ampère's Law (integral form)

$$
\oint_C \mathbf{H} \cdot d\mathbf{l} = \iint_S \mathbf{J} \cdot d\mathbf{S} \tag{2.3}
$$

Total current density: $\mathbf{J} = \mathbf{J}_0 + \sigma\mathbf{E} + \partial(\varepsilon\mathbf{E})/\partial t$ (source + conduction + displacement).

**Differential form:**

$$
\nabla \times \mathbf{H} = \mathbf{J} \tag{2.4}
$$

> **Example 2-1:** Magnetic field of an infinitely long wire ($a=5$ mm, $I=5$ A):
> $$
> H(r) = \begin{cases}
> \dfrac{Ir}{2\pi a^2}, & 0 \le r \le a \quad\text{(linear increase)} \\[6pt]
> \dfrac{I}{2\pi r}, & r \ge a \quad\text{(decay)}
> \end{cases}
> $$

### Faraday's Law (integral form)

$$
\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt}\iint_S \mathbf{B} \cdot d\mathbf{S} \tag{2.7}
$$

**Differential form:**

$$
\nabla \times \mathbf{E} = -\mu\frac{\partial\mathbf{H}}{\partial t} \tag{2.8}
$$

> **Example 2-2:** Induced voltage in a wire loop ($a=5$ mm, $H = 5\cos(\omega t)$ A/m, $f=100$ MHz):
> $$
> V = -\mu_0 \pi a^2 \frac{d}{dt}[H_0\cos(\omega t)] = -0.31\sin(6.28\times 10^8 t) \text{ V}
> $$

---

## 2.5 Circuit Parameters for a Parallel-Plate Transmission Line

For wide plates ($w \gg d$) with skin depth $\delta \ll d_p$ (plate thickness):

### Field Solutions
From Faraday's and Ampère's laws in the conductor:

$$
\frac{\partial^2 H_y}{\partial x^2} = p^2 H_y, \quad p^2 = -j\omega\mu_0\sigma_{\text{cond}}, \quad \delta = \frac{1}{\sqrt{\pi f \mu_0 \sigma_{\text{cond}}}}
$$

Magnetic field in lower plate: $H_y(x) = H_0 e^{px}$ (exponential decay into conductor).

### Surface Impedance (per unit length, single conductor)

$$
Z_s = R_s + j\omega L_s = \frac{1+j}{w\sigma_{\text{cond}}\delta} \tag{2.20}
$$

$$
R_s = \frac{1}{w\sigma_{\text{cond}}\delta}, \quad L_s = \frac{1}{w\sigma_{\text{cond}}\omega\delta} \tag{2.21, 2.22}
$$

Total for two plates: $R = 2R_s$, $L_s^{\text{(total)}} = 2L_s$.

### Mutual Inductance and Capacitance

$$
L = \frac{\mu d}{w} \quad [\text{H/m}] \tag{2.24}
$$

$$
C = \frac{\varepsilon w}{d} \quad [\text{F/m}] \tag{2.23}
$$

### Shunt Conductance

$$
G = \frac{\sigma_{\text{diel}} w}{d} \quad [\text{S/m}] \tag{2.25}
$$

> **Example 2-3:** At $f=1$ GHz, copper plates: $w=6$ mm, $d=1$ mm, $\varepsilon_r=2.25$, $\sigma_{\text{diel}}=0.125$ mS/m.
> $$
> \delta = 1.98\ \mu\text{m}, \quad R = 2.6\ \Omega/\text{m}, \quad L = 209.4\ \text{nH/m}
> $$
> $$
> C = 119.5\ \text{pF/m}, \quad G = 0.75\ \text{mS/m}
> $$
> Note: $L_s \approx 0.42$ nH/m is negligible compared to mutual $L = 209.4$ nH/m.

---

## 2.6 Summary of Different Line Configurations

### Table 2-1: Transmission Line Parameters

| Parameter | Two-Wire | Coaxial | Parallel-Plate |
|-----------|----------|---------|----------------|
| $R$ [$\Omega$/m] | $\dfrac{1}{\pi a \sigma_{\text{cond}} \delta}$ | $\dfrac{1}{2\pi\sigma_{\text{cond}}\delta}\left(\dfrac{1}{a}+\dfrac{1}{b}\right)$ | $\dfrac{2}{w\sigma_{\text{cond}}\delta}$ |
| $L$ [H/m] | $\dfrac{\mu}{\pi}\operatorname{acosh}\left(\dfrac{D}{2a}\right)$ | $\dfrac{\mu}{2\pi}\ln\left(\dfrac{b}{a}\right)$ | $\dfrac{\mu d}{w}$ |
| $G$ [S/m] | $\dfrac{\pi\sigma_{\text{diel}}}{\operatorname{acosh}(D/(2a))}$ | $\dfrac{2\pi\sigma_{\text{diel}}}{\ln(b/a)}$ | $\dfrac{\sigma_{\text{diel}} w}{d}$ |
| $C$ [F/m] | $\dfrac{\pi\varepsilon}{\operatorname{acosh}(D/(2a))}$ | $\dfrac{2\pi\varepsilon}{\ln(b/a)}$ | $\dfrac{\varepsilon w}{d}$ |

---

## 2.7 General Transmission Line Equation

### 2.7.1 KVL and KCL per Unit Length

From the equivalent circuit (Fig. 2-17):

$$
-\frac{dV(z)}{dz} = (R + j\omega L)I(z) \tag{2.28}
$$

$$
-\frac{dI(z)}{dz} = (G + j\omega C)V(z) \tag{2.30}
$$

### 2.7.2 Traveling Wave Solution

Decoupling yields the wave equation:

$$
\frac{d^2 V(z)}{dz^2} = k^2 V(z), \quad k = \sqrt{(R + j\omega L)(G + j\omega C)} \tag{2.31, 2.32}
$$

General solution:

$$
V(z) = V^+ e^{-kz} + V^- e^{kz} \tag{2.34}
$$

$$
I(z) = I^+ e^{-kz} + I^- e^{kz} \tag{2.35}
$$

where $e^{-kz}$ represents propagation in $+z$ direction and $e^{kz}$ in $-z$ direction.

### 2.7.3 Characteristic Impedance

$$
Z_0 = \frac{V^+}{I^+} = \sqrt{\frac{R + j\omega L}{G + j\omega C}} \tag{2.37}
$$

$Z_0$ is **not** a circuit impedance—it relates forward/backward traveling waves, not total voltage/current.

### 2.7.4 Lossless Line Model

For $R = G = 0$:

$$
Z_0 = \sqrt{\frac{L}{C}} \quad\text{(real, frequency-independent)} \tag{2.40}
$$

Propagation constant: $k = j\beta = j\omega\sqrt{LC}$, $\alpha = 0$, $\beta = \omega\sqrt{LC}$.

Phase velocity: $v_p = \frac{\omega}{\beta} = \frac{1}{\sqrt{LC}} \tag{2.58}$

For parallel-plate line: $Z_0 = \frac{d}{w}\sqrt{\frac{\mu}{\varepsilon}} \tag{2.41}$

---

## 2.8 Microstrip Transmission Lines

### Effective Dielectric Constant

$$
\varepsilon_{\text{eff}} = \frac{\varepsilon_r + 1}{2} + \frac{\varepsilon_r - 1}{2}\frac{1}{\sqrt{1 + 12h/w}} \tag{2.43}
$$

### Characteristic Impedance (zero strip thickness, $t \ll h$)

**Narrow strip** ($w/h \le 1$):

$$
Z_0 = \frac{Z_f}{2\pi\sqrt{\varepsilon_{\text{eff}}}}\ln\left(\frac{8h}{w} + \frac{w}{4h}\right), \quad Z_f = \sqrt{\mu_0/\varepsilon_0} \tag{2.42}
$$

**Wide strip** ($w/h \ge 1$):

$$
Z_0 = \frac{Z_f}{\sqrt{\varepsilon_{\text{eff}}}}\left[\frac{w}{h} + 1.393 + 0.667\ln\left(\frac{w}{h} + 1.444\right)\right]^{-1} \tag{2.44}
$$

### Synthesis Formulas (given $Z_0$, $\varepsilon_r$)

**For $w/h \le 2$:**

$$
\frac{w}{h} = \frac{8e^A}{e^{2A} - 2}, \quad A = \frac{Z_0}{60}\sqrt{\frac{\varepsilon_r + 1}{2}} + \frac{\varepsilon_r - 1}{\varepsilon_r + 1}\left(0.23 + \frac{0.11}{\varepsilon_r}\right) \tag{2.46}
$$

**For $w/h \ge 2$:**

$$
\frac{w}{h} = \frac{2}{\pi}\left[B - 1 - \ln(2B - 1) + \frac{\varepsilon_r - 1}{2\varepsilon_r}\left(\ln(B - 1) + 0.39 - \frac{0.61}{\varepsilon_r}\right)\right] \tag{2.47}
$$

$$
B = \frac{377\pi}{2Z_0\sqrt{\varepsilon_r}} \tag{2.48}
$$

### Finite Strip Thickness Correction

$$
w_e = w + \frac{t}{\pi}\left(1 + \ln\frac{x}{t}\right)
$$

where $x = h$ if $w > h/(2\pi) > 2t$, else $x = 2\pi w$.

> **Example 2-5:** Design a 50 $\Omega$ microstrip on FR-4 ($\varepsilon_r=4.6$, $h=40$ mil):
> - $w/h \approx 1.9$ → $w = 73.9$ mil
> - $\varepsilon_{\text{eff}} = 3.39$
> - $v_p = 1.63 \times 10^8$ m/s, $\lambda = 80.67$ mm @ 2 GHz

---

## 2.9 Terminated Lossless Transmission Line

### Voltage Reflection Coefficient

$$
\Gamma_0 = \frac{V^-}{V^+}\Big|_{z=0} = \frac{Z_L - Z_0}{Z_L + Z_0} \tag{2.52}
$$

**Special cases:**
- Open circuit ($Z_L \to \infty$): $\Gamma_0 = +1$
- Short circuit ($Z_L = 0$): $\Gamma_0 = -1$
- Matched ($Z_L = Z_0$): $\Gamma_0 = 0$

### Voltage and Current Along the Line (coordinate $d$ from load)

$$
V(d) = V^+ e^{j\beta d} \left[1 + \Gamma(d)\right] \tag{2.63}
$$

$$
I(d) = \frac{V^+}{Z_0} e^{j\beta d} \left[1 - \Gamma(d)\right] \tag{2.65}
$$

where $\Gamma(d) = \Gamma_0 e^{-j2\beta d}$ is the reflection coefficient at distance $d$ from load.

### Standing Wave Ratio (SWR/VSWR)

$$
\text{VSWR} = \frac{|V|_{\text{max}}}{|V|_{\text{min}}} = \frac{1 + |\Gamma_0|}{1 - |\Gamma_0|} \tag{2.67}
$$

- Matched: VSWR $= 1$
- Open/short: VSWR $= \infty$
- Distance between successive minima: $\lambda/2$

> **工程直觉:** VSWR 是描述失配程度的工程指标。VSWR = 2.0 对应 $|\Gamma| = 0.33$（33%功率反射），在大多数RF系统中是可以接受的；VSWR > 3 通常需要重新设计匹配网络。

---

## 2.10 Special Termination Conditions

### Input Impedance of Terminated Lossless Line

$$
Z_{\text{in}}(d) = Z_0 \frac{Z_L + jZ_0\tan(\beta d)}{Z_0 + jZ_L\tan(\beta d)} \tag{2.71}
$$

### Short-Circuit Line ($Z_L = 0$)

$$
Z_{\text{in}}(d) = jZ_0\tan(\beta d) \tag{2.72}
$$

- $d < \lambda/4$: inductive ($+j$)
- $d = \lambda/4$: open circuit ($\infty$)
- $\lambda/4 < d < \lambda/2$: capacitive ($-j$)
- $d = \lambda/2$: short circuit ($0$)

### Open-Circuit Line ($Z_L \to \infty$)

$$
Z_{\text{in}}(d) = -jZ_0\cot(\beta d) \tag{2.75}
$$

> **Examples 2-6, 2-7:** 10 cm line ($Z_0 = 41.86\ \Omega$, $v_p = 1.99\times 10^8$ m/s), frequency swept 1–4 GHz:
> - Short-circuit line: periodic zeros (short) and poles (open) at multiples of $\lambda/4$.
> - Open-circuit line: complementary behavior — zeros where short-circuit line has poles.
> - **Key insight:** matching is frequency-dependent; deviations from design frequency cause significant impedance variation.

### Quarter-Wave Transformer

For $d = \lambda/4$:

$$
Z_{\text{in}} = \frac{Z_0^2}{Z_L} \tag{2.81}
$$

Design equation (real impedances):

$$
Z_0 = \sqrt{Z_L Z_{\text{in}}} \tag{2.82}
$$

> **Example 2-8:** Match $Z_L = 25\ \Omega$ transistor to $50\ \Omega$ line at 500 MHz:
> - $Z_0 = \sqrt{25 \times 50} = 35.35\ \Omega$
> - Parallel-plate: $w = 2.13$ mm ($d=1$ mm, $\varepsilon_r=4$), $l = \lambda/4 = 75$ mm
> - $L = 235.8$ nH/m, $C = 188.6$ pF/m
> - Matching achieved at 500 MHz and odd harmonics (1.5 GHz, etc.)

> **工程直觉:** $\lambda/4$ 变压器是窄带匹配器件。带宽随 $Z_L/Z_0$ 比值偏离1而减小。宽带匹配需要多节或渐变线结构。

---

## 2.11 Sourced and Loaded Transmission Line

### Input Reflection Coefficient

$$
\Gamma_{\text{in}} = \Gamma(d=l) = \Gamma_0 e^{-j2\beta l} \tag{2.84}
$$

### Source Reflection Coefficient

$$
\Gamma_S = \frac{Z_G - Z_0}{Z_G + Z_0} \tag{2.87}
$$

### Power Delivered to Load (lossless line)

$$
P_L = P_{\text{in}} = \frac{|V_G|^2}{8Z_0} \frac{|1 - \Gamma_S|^2 |1 - \Gamma_0|^2}{|1 - \Gamma_S\Gamma_0 e^{-j2\beta l}|^2} \tag{2.95}
$$

Under perfect match ($\Gamma_S = \Gamma_0 = 0$):

$$
P_{\text{avs}} = \frac{|V_G|^2}{8Z_0} \quad\text{(maximum available power from source)} \tag{2.96}
$$

### Conjugate Matching for Maximum Power Transfer

$$
Z_{\text{in}} = Z_G^* \quad (\text{input matching})
$$

$$
Z_{\text{out}} = Z_L^* \quad (\text{output matching}) \tag{2.104}
$$

### Return Loss and Insertion Loss

$$
\text{RL (dB)} = -20\log_{10}|\Gamma_{\text{in}}| \tag{2.105a}
$$

$$
\text{IL (dB)} = -10\log_{10}\left(\frac{P_t}{P_i}\right) \tag{2.107}
$$

> **Example 2-10:** $Z_0=75\ \Omega$, $Z_G=50\ \Omega$, $Z_L=40\ \Omega$, $l=\lambda/2$, $V_G=5$ V:
> - $\Gamma_S = -0.2$, $\Gamma_0 = -0.304$
> - $P_L = 61.7$ mW ($\approx 17.9$ dBm)

> **Example 2-11:** RL = 20 dB → $|\Gamma_{\text{in}}| = 0.1$. For $R_{\text{in}}=50\ \Omega$:
> - $|\Gamma| = 0.1 \implies R_G = 61.1\ \Omega$ or $40.9\ \Omega$ (two possible solutions)

---

## 审计表 (Audit)

| 项目 | 状态 | 备注 |
|------|------|------|
| §2.1 为何传输线理论 | ✅ | $\lambda/10$ 判据 |
| §2.2 传输线示例 | ✅ | 双线/同轴/微带/平行板 |
| §2.3 等效电路模型 | ✅ | $R,L,C,G$ 分布参数 |
| §2.4 理论基础 (Ampere/Faraday) | ✅ | Ex2-1, Ex2-2 |
| §2.5 平行板线参数 | ✅ | Ex2-3 |
| §2.6 线型参数表 | ✅ | Table 2-1 完整 |
| §2.7 传输线方程 | ✅ | 波动方程/特性阻抗/无耗 |
| §2.8 微带线设计 | ✅ | Ex2-5, 合成/分析公式 |
| §2.9 有载传输线 | ✅ | $\Gamma_0$, VSWR |
| §2.10 特殊端接 | ✅ | Ex2-6/7/8 |
| §2.11 源/负载功率 | ✅ | Ex2-10/11 |
| 例题代码复现 | ✅ | 5 个关键例题 |
| 工程直觉段落 | ✅ | 每节末尾 |
