# Pozar Chapter 14 — Active RF and Microwave Devices
> **中英双语版**

> Comprehensive notes on Pozar *Microwave Engineering*, 4th Edition.
> Covers diodes, transistors, amplifiers, oscillators, and mixers.

---

## 14.1 Semiconductor Diodes | 半导体二极管

### 14.1.1 pn Junction | pn 结

The current-voltage characteristic of an ideal diode:
> 理想二极管的 I-V 特性：

$$I = I_S \left(e^{V/\eta V_T} - 1\right), \quad V_T = \frac{kT}{q} \approx 26\;\text{mV at 300 K}$$

where $I_S$ is the saturation current and $\eta$ is the ideality factor ($\approx 1$-$2$).
> 其中 $I_S$ 为饱和电流，$\eta$ 为理想因子。

**Small-signal equivalent / 小信号等效电路：**
- Junction resistance: $r_j = \eta V_T / I$
- Junction capacitance: $C_j = C_{j0} / \sqrt{1 + V_R/V_{bi}}$ (varies with reverse bias)
  > 结电容随反向偏压变化

### 14.1.2 Schottky Diode | 肖特基二极管

Metal-semiconductor junction with faster switching than pn junction.
> 金属-半导体结，开关速度高于 pn 结。

Used for: mixing, detection, and rectification at microwave frequencies.
> 用于微波频率的混频、检波和整流。

### 14.1.3 PIN Diode | PIN 二极管

Has intrinsic ($I$) layer between P and N regions.
> P 区和 N 区之间有本征 ($I$) 层。

**RF switch operation / RF 开关工作：**
- Forward bias: Low impedance (ON) / 正偏：低阻抗（导通）
- Reverse bias: High impedance (OFF) / 反偏：高阻抗（截止）

### 14.1.4 Varactor Diode | 变容二极管

Variable capacitor (C-V characteristic). Used for tuning.
> 可变电容（C-V 特性），用于调谐。

### 14.1.5 IMPATT and Gunn Diodes | IMPATT 和 Gunn 二极管

**IMPATT (Impact Ionization Avalanche Transit-Time) / 碰撞雪崩渡越时间二极管：**
- Generates negative resistance for oscillation at mm-wave frequencies
  > 产生负阻，用于毫米波振荡

**Gunn diode / 耿氏二极管：**
- Uses transferred electron effect (GaAs) for negative resistance
  > 利用转移电子效应（GaAs）产生负阻
- Simple two-terminal oscillator up to 100+ GHz
  > 简单的两端振荡器，频率可达 100+ GHz

---

## 14.2 Microwave Transistors | 微波晶体管

### 14.2.1 MESFET (GaAs FET) | 金属-半导体场效应管

Metal-Semiconductor Field-Effect Transistor. Common in GaAs MMICs.
> 金属-半导体场效应晶体管，常用于 GaAs MMIC。

**Small-signal equivalent circuit / 小信号等效电路：**
- $g_m$: transconductance / 跨导
- $C_{gs}$, $C_{gd}$: gate-source and gate-drain capacitances / 栅-源和栅-漏电容
- $R_{ds}$: output resistance / 输出电阻
- $f_T \approx g_m/(2\pi C_{gs})$: current-gain cutoff frequency / 电流增益截止频率

### 14.2.2 HEMT (High Electron Mobility Transistor) | 高电子迁移率晶体管

Uses heterojunction (AlGaAs/GaAs) for higher electron mobility.
> 使用异质结（AlGaAs/GaAs）获得更高的电子迁移率。

- Higher $f_T$, lower noise than MESFET / 比 MESFET 更高的 $f_T$ 和更低的噪声
- Used in low-noise amplifiers and high-speed digital circuits
  > 用于低噪声放大器和高速数字电路

### 14.2.3 HBT (Heterojunction Bipolar Transistor) | 异质结双极晶体管

Heterojunction between emitter and base for higher gain.
> 发射极和基极之间的异质结可获得更高增益。

- High linearity / 高线性度
- Good for power amplifiers / 适用于功率放大器

### 14.2.4 BJT and MOSFET at Microwave Freq | BJT 和 MOSFET 在微波频率

- Silicon BJT: $f_T$ up to ~10 GHz / 硅 BJT 的 $f_T$ 可达 ~10 GHz
- SiGe HBT: $f_T$ up to ~300 GHz / SiGe HBT 的 $f_T$ 可达 ~300 GHz
- CMOS (nanoscale): $f_T$ up to ~500 GHz / 纳米级 CMOS 的 $f_T$ 可达 ~500 GHz

---

## 14.3 Microwave Amplifiers | 微波放大器

### 14.3.1 Amplifier Design Using S-Parameters | 使用 S 参数设计放大器

For a transistor characterized by S-parameters, design input and output matching networks:
> 对于由 S 参数表征的晶体管，设计输入和输出匹配网络：

$$\Gamma_{\text{in}} = S_{11} + \frac{S_{12}S_{21}\Gamma_L}{1 - S_{22}\Gamma_L}, \quad \Gamma_{\text{out}} = S_{22} + \frac{S_{12}S_{21}\Gamma_S}{1 - S_{11}\Gamma_S}$$

**Stability / 稳定性：** Unconditional stability requires $|\Gamma_{\text{in}}| < 1$ and $|\Gamma_{\text{out}}| < 1$ for all passive loads.
> 无条件稳定要求对所有无源负载 $|\Gamma_{\text{in}}| < 1$ 和 $|\Gamma_{\text{out}}| < 1$。

**Stability circles / 稳定圆：** Boundaries on the Smith chart separating stable and unstable regions.
> Smith 圆图上区分稳定和不稳定区域的边界。

**Maximum gain / 最大增益：** Simultaneous conjugate match: $\Gamma_S = \Gamma_{\text{in}}^*$, $\Gamma_L = \Gamma_{\text{out}}^*$.
> 同时共轭匹配给出最大增益。

### 14.3.2 Low-Noise Amplifier (LNA) | 低噪声放大器

Design for minimum noise figure, usually not at maximum gain.
> 设计以获得最小噪声系数为目标，通常不追求最大增益。

$$\Gamma_S = \Gamma_{\text{opt}}, \quad F = F_{\text{min}} + \frac{R_n}{G_S} |Y_S - Y_{\text{opt}}|^2$$

> 噪声系数由源反射系数 $\Gamma_S$ 决定，在 $\Gamma_S = \Gamma_{\text{opt}}$ 时达到最小。

### 14.3.3 Power Amplifier (PA) | 功率放大器

- Class A: Linear but low efficiency ($\eta \leq 50\%$) / A 类：线性但效率低
- Class B: Push-pull, $\eta \leq 78.5\%$ / B 类：推挽结构
- Class C: Nonlinear, $\eta \leq 90\%$ for conduction angle $\to 0$
- Class E/F: Switching-mode, theoretical $\eta = 100\%$

---

## 14.4 Oscillators | 振荡器

### 14.4.1 Feedback Oscillator | 反馈振荡器

Barkhausen criterion: $|\Gamma_{\text{in}}\Gamma_{\text{res}}| \geq 1$ and $\angle(\Gamma_{\text{in}}\Gamma_{\text{res}}) = 0^\circ$.
> 巴克豪森准则：环路增益 $\geq 1$，环路相移 $= 0^\circ$。

### 14.4.2 Reflection Oscillator | 反射振荡器

Uses a negative resistance diode (Gunn, IMPATT) or transistor with feedback.
> 使用负阻二极管（Gunn, IMPATT）或带反馈的晶体管。

Design condition: $\Gamma_S \Gamma_{\text{in}} = 1$ at the desired frequency.
> 设计条件：在所需频率处 $\Gamma_S \Gamma_{\text{in}} = 1$。

### 14.4.3 Phase Noise | 相位噪声

Leeson's model / Leeson 模型：

$$\mathcal{L}(\Delta\omega) = \frac{FkT}{P_s} \left[ 1 + \left(\frac{\omega_0}{2Q\Delta\omega}\right)^2 \right]$$

> 相位噪声由 $Q$ 值、信号功率 $P_s$ 和噪声系数 $F$ 决定。高 $Q$ 谐振器降低相位噪声。

---

## 14.5 Mixers | 混频器

### 14.5.1 Principle | 原理

A mixer multiplies two signals to produce sum and difference frequencies:
> 混频器将两个信号相乘产生和频与差频：

$$V_{\text{out}} = V_{\text{RF}} V_{\text{LO}} \cos(\omega_{\text{RF}} t) \cos(\omega_{\text{LO}} t) = \frac{V_{\text{RF}} V_{\text{LO}}}{2} [\cos(\omega_{\text{RF}}-\omega_{\text{LO}})t + \cos(\omega_{\text{RF}}+\omega_{\text{LO}})t]$$

The IF output can be at either the difference (down-conversion) or sum (up-conversion).
> IF 输出可以是差频（下变频）或和频（上变频）。

### 14.5.2 Types | 类型

- **Single-ended**: One diode, simple but poor port isolation
  > 单端混频器：一个二极管，简单但端口隔离度差
- **Balanced (rat-race, hybrid)**: Better isolation, higher LO power handling
  > 平衡混频器：更好的隔离度、更高的 LO 功率处理能力
- **Double-balanced**: Excellent isolation, high dynamic range
  > 双平衡混频器：优秀的隔离度、高动态范围

### 14.5.3 Mixer Parameters | 混频器参数

| Parameter | Description |
|-----------|-------------|
| Conversion loss $L_c$ | RF-to-IF power ratio / RF 到 IF 的功率比 |
| Noise figure | Includes IF amplifier noise / 包括 IF 放大器噪声 |
| LO-RF isolation | Leakage from LO to RF port / LO 到 RF 端口的泄漏 |
| IP3 | Third-order intercept (linearity) / 三阶交调截点（线性度） |
