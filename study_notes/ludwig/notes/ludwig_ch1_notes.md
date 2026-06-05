---
chapter: 1
title: Introduction
source: Ludwig & Bogdanov, RF Circuit Design, 2nd Edition
pages: 15-42
---

# Chapter 1: RF Circuit Design Intro | 第1章：射频电路设计导论
# 射频电路设计导论

## 1.1 Importance of Radiofrequency Design | 射频设计的重要性

> **Original:** The beginning of electrical circuit design is most likely traced back to the late eighteenth and early nineteenth centuries when the first reliable batteries became available. Named after their inventor A. Volta (1745–1827), the Voltaic cells permitted the supply of reliable DC energy to power the first crude circuits.

**【中文注释】** 电路设计的起源可追溯至18世纪末至19世纪初最早的可充电电池出现。意大利物理学家亚历山德罗·伏特（Alessandro Volta, 1745–1827）发明的伏打电池首次为原始电路提供了稳定的直流电源。这一发明标志着人类利用电力的开端。

---

### Historical Context: From DC to RF | 从直流到射频的历史脉络

The transition from direct current (DC) to radiofrequency (RF) operation follows a well-defined historical trajectory:

| Era | Key Figure | Contribution |
|-----|-----------|--------------|
| 1791–1827 | Alessandro Volta | Invented the first reliable battery (Voltaic cell) |
| 1831 | Michael Faraday | Discovered electromagnetic induction (Faraday's law) |
| 1864 | James Clerk Maxwell | Formulated the coupled EM field equations (Maxwell's equations) |
| 1887 | Heinrich Hertz | Experimentally proved EM wave propagation |
| 1920s–1930s | — | Radio and TV broadcasting begins |
| 1980s–1990s | — | Cellular phones and GPS introduced |

**【中文注释】** 从伏打电池到麦克斯韦方程组，再到赫兹的电磁波实验验证，人类花了将近一个世纪才理解电磁波的本质。麦克斯韦1864年的论文首次提出电场与磁场的耦合理论，预言了电磁波的存在。1887年赫兹通过实验证明了电磁波的辐射与接收，从此开启了无线通信的时代。

---

### Why Conventional Circuit Analysis Fails at RF | 传统电路分析在射频失效的原因

Conventional Kirchhoff-based analysis (KVL, KCL) is only valid when:
1. **Circuit dimensions $\ll \lambda$** (quasi-static assumption)
2. **Lumped element model holds** — i.e., $R$, $L$, $C$ are frequency-independent

At RF frequencies (e.g., $f = 2$ GHz, $\lambda = 15$ cm in free space), the physical dimensions of components are comparable to the wavelength. The **wave nature** of voltage and current dominates, requiring transmission line theory.

$$\lambda = \frac{c}{f} = \frac{3 \times 10^8}{2 \times 10^9} = 0.15 \text{ m} = 15 \text{ cm}$$

**【中文注释】** 在2 GHz频率下，波长仅为15厘米。当元件尺寸与波长可比时，电压和电流不再只是"节点"上的标量值，而必须被当作沿传输线分布的波动来处理。基尔霍夫电压定律和电流定律在此处失效，因为电磁能量以波的形式在空间传播，而非简单地沿导线流动。

---

### Cellular Phone PA Example | 手机功率放大器实例

Figure 1-2(a) shows a simplified circuit diagram of the **first stage of a 2 GHz power amplifier (PA)** for cellular phones, implemented as a dual-stage amplifier.

Key RF blocks in the PA:
- **DC blocking capacitor** — isolates DC bias from RF signal path
- **Input matching network** — matches transistor input impedance $Z_{in}$ to mixer's output impedance (typically $50\,\Omega$) for optimal power transfer
- **Interstage matching network** — matches output of first transistor to input of second stage
- **Microstrip lines** — distributed elements acting as transmission lines (shaded rectangles in Fig 1-2a)
- **RFCs (Radio Frequency Coils)** — RF blocking networks that isolate RF from DC bias

**【中文注释】** 以飞利浦半导体BFG425W晶体管为例，工作在共发射极组态。输入匹配网络将晶体管的输入阻抗与混频器的输出阻抗（通常为50 Ω）匹配，以确保最大功率传输并消除反射。级间匹配网络将第一级的输出阻抗与第二级的输入阻抗匹配。微带线在高频下表现为分布式元件，其特性阻抗与长度密切相关，这与低频下的集总元件截然不同。

---

## 1.2 Dimensions and Units | 尺寸与单位

### Plane TEM Wave Propagation | 平面TEM波传播

For a plane electromagnetic wave propagating in the $+z$ direction in free space:

$$E_x(z,t) = E_{0x} \cos(\omega t - \beta z) \tag{1.1a}$$

$$H_y(z,t) = H_{0y} \cos(\omega t - \beta z) \tag{1.1b}$$

where:
- $E_x$ — x-directed electric field component [V/m]
- $H_y$ — y-directed magnetic field component [A/m]
- $E_{0x}, H_{0y}$ — constant amplitude factors
- $\omega = 2\pi f$ — angular frequency [rad/s]
- $\beta = 2\pi/\lambda$ — propagation constant [rad/m]
- $\lambda$ — wavelength [m]

**【中文注释】** 平面电磁波的传播特性由麦克斯韦方程组决定。$E_x$和$H_y$两个场分量相互正交，且都垂直于传播方向$+z$，这正是**横电磁波（TEM模）**的特征。在本书中，我们只讨论TEM模，因为它是最常见的射频传播模式。相比之下，微波和光通信中还会遇到TE模（横电模）和TM模（横磁模），它们的场分量不再垂直于传播方向。

---

### Intrinsic Impedance | 本征阻抗

The ratio of electric to magnetic field components defines the **intrinsic impedance** $Z_0$ of the medium:

$$Z_0 = \frac{E_x}{H_y} = \sqrt{\frac{\mu}{\varepsilon}} = \sqrt{\frac{\mu_0 \mu_r}{\varepsilon_0 \varepsilon_r}} \tag{1.2}$$

where:
- $\mu_0 = 4\pi \times 10^{-7}$ H/m — free-space permeability
- $\varepsilon_0 = 8.854 \times 10^{-12}$ F/m — free-space permittivity
- $\mu_r, \varepsilon_r$ — relative permeability and permittivity

For free space ($\mu_r = \varepsilon_r = 1$):

$$Z_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} \approx 377\,\Omega$$

**【中文注释】** 本征阻抗$Z_0$描述了介质中电场与磁场的比例关系。在自由空间中，该值约为377 Ω，这是一个非常重要的基准值。在后续的传输线理论中，特性阻抗$Z_0$与本征阻抗有着密切的关系。

---

### Phase Velocity | 相速度

$$v_p = \frac{\omega}{\beta} = \frac{1}{\sqrt{\mu\varepsilon}} = \frac{c}{\sqrt{\mu_r \varepsilon_r}} \tag{1.3}$$

In free space, $v_p = c = 2.998 \times 10^8$ m/s (speed of light).

**【中文注释】** 相速度是电磁波在介质中传播的速度。在非磁性介质（$\mu_r = 1$）中，$v_p = c/\sqrt{\varepsilon_r}$。这意味着介质的相对介电常数$\varepsilon_r$越大，电磁波传播的速度越慢。

---

### Wavelength | 波长

$$\lambda = \frac{v_p}{f} = \frac{c}{f\sqrt{\mu_r \varepsilon_r}} \tag{1.4}$$

**【中文注释】** 波长是电磁波在一个周期内传播的距离。当频率升高时，波长减小，这就是为什么在高频时元件尺寸会变得与波长可比，从而需要引入传输线理论。

---

### Example 1-1: Intrinsic Impedance, Phase Velocity, and Wavelength | 例1-1：本征阻抗、相速度与波长

**Problem:** Compute the intrinsic wave impedance, phase velocity, and wavelengths in free space at $f = 30$ MHz, $300$ MHz, and $30$ GHz.

**Solution:**

Since $\mu_r = \varepsilon_r = 1$ for free space:

$$Z_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} = \sqrt{\frac{4\pi \times 10^{-7}}{8.854 \times 10^{-12}}} \approx 376.7\,\Omega \approx 377\,\Omega$$

$$v_p = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} = 2.998 \times 10^8 \text{ m/s} = c$$

Using $\lambda = c/f$:

| Frequency | Wavelength |
|-----------|-----------|
| 30 MHz | $\lambda = 10$ m |
| 300 MHz | $\lambda = 1$ m |
| 30 GHz | $\lambda = 1$ cm |

**【中文注释】** 从这个例子可以清楚地看到：随着频率从30 MHz升至30 GHz，波长从10米骤降至1厘米。当波长降至电路板尺寸甚至元件尺寸量级时，传统的集总电路分析方法就不再适用了——必须引入传输线理论来描述电磁波的波动行为。

---

## 1.3 Frequency Spectrum | 频谱

### IEEE Frequency Band Classification | IEEE频段分类

| Band | Frequency | Wavelength |
|------|-----------|------------|
| VLF (Very Low Frequency) | 3–30 kHz | 100–10 km |
| LF (Low Frequency) | 30–300 kHz | 10–1 km |
| MF (Medium Frequency) | 300–3000 kHz | 1–0.1 km |
| HF (High Frequency) | 3–30 MHz | 100–10 m |
| VHF (Very High Frequency) | 30–300 MHz | 10–1 m |
| UHF (Ultrahigh Frequency) | 300–3000 MHz | 1–0.1 m |
| SHF (Superhigh Frequency) | 3–30 GHz | 10–1 cm |
| EHF (Extreme High Frequency) | 30–300 GHz | 1–0.1 cm |

| Sub-Band | Frequency |
|----------|-----------|
| L Band | 1–2 GHz (\lambda = 30–15 cm) |
| S Band | 2–4 GHz (\lambda = 15–7.5 cm) |
| C Band | 4–8 GHz (\lambda = 7.5–3.75 cm) |
| X Band | 8–12.5 GHz (\lambda = 3.75–2.4 cm) |
| Ku Band | 12.5–18 GHz |
| K Band | 18–26.5 GHz |
| Ka Band | 26.5–40 GHz |

**【中文注释】** 在工程实践中，RF频段通常指VHF到S波段（大致30 MHz至4 GHz），而微波频段则与雷达系统（C波段及以上）相关。电视广播通常工作在VHF/UHF频段（大约470 MHz至862 MHz），这也是波长首次与电子系统物理尺寸相当的区域——从这一点开始，电磁波的波动性质开始主导电路行为。

---

## 1.4 RF Behavior of Passive Components | 射频无源元件的行为

### Low-Frequency Reactance Formulas | 低频电抗公式

At low frequencies, ideal $R$, $L$, $C$ elements have frequency-independent values:

$$X_C = \frac{1}{\omega C} = \frac{1}{2\pi f C} \tag{1.5a}$$

$$X_L = \omega L = 2\pi f L \tag{1.5b}$$

**Example: At $f = 60$ Hz, with $C = 1$ pF and $L = 1$ nH:**

$$X_C(60\ \text{Hz}) = \frac{1}{2\pi \times 60 \times 10^{-12}} \approx 2.65\ \text{G}\Omega \quad \text{(nearly open circuit)}$$

$$X_L(60\ \text{Hz}) = 2\pi \times 60 \times 10^{-9} \approx 0.377\ \text{m}\Omega \quad \text{(nearly short circuit)}$$

**【中文注释】** 在低频下，1 pF的电容表现为几乎开路（阻抗极大），而1 nH的电感表现为几乎短路（阻抗极小）。但这些理想公式只在频率足够低时才成立。在GHz频段，这些元件的寄生效应开始主导，表现出复杂的频率响应。

---

### Skin Effect | 集肤效应

A crucial phenomenon at RF: the **alternating current tends to flow near the surface** of a conductor, reducing the effective cross-sectional area.

For a cylindrical conductor of radius $a$, conductivity $\sigma_{\text{cond}}$, permeability $\mu = \mu_0 \mu_r$:

The **skin depth** $\delta$ is:

$$\delta = \sqrt{\frac{2}{\omega \mu \sigma_{\text{cond}}}} = \sqrt{\frac{1}{\pi f \mu \sigma_{\text{cond}}}} \tag{1.11}$$

**Physical meaning:** $\delta$ is the depth at which the current density drops to $e^{-1} \approx 37\%$ of its surface value.

**【中文注释】** 集肤效应的物理根源是：交流电流在导体内部产生的时变磁场，根据法拉第电磁感应定律，会在导体中心感生一个反向电动势，阻止电流在中心流动。结果是电流被"挤"到导体表面。集肤深度$\delta$是描述这一现象的核心参数——频率越高，$\delta$越小，电流越集中于表面。

---

### High-Frequency Normalized Resistance and Inductance | 高频归一化电阻与电感

At high frequencies ($f \geq 500$ MHz, assuming $\delta \ll a$):

$$\frac{R}{R_{\text{DC}}} \approx \frac{a}{2\delta} \tag{1.9}$$

$$\frac{\omega L}{R_{\text{DC}}} \approx \frac{a}{2\delta} \tag{1.10}$$

**【中文注释】** 当集肤深度$\delta$远小于导体半径$a$时，高频电阻和感抗都与$a/(2\delta)$成正比。这意味着随着频率升高，有效导电截面积减小（从$\pi a^2$减小到约$2\pi a \delta$），导致电阻急剧增加。

---

### Skin Depth for Copper | 铜的集肤深度

Using $\sigma_{\text{Cu}} = 64.516 \times 10^6$ S/m, $\mu_r = 1$:

| Frequency | Skin Depth $\delta$ |
|-----------|---------------------|
| 1 MHz | ~66 \mum |
| 100 MHz | ~6.6 \mum |
| 1 GHz | ~2.1 \mum |
| 10 GHz | ~0.66 \mum |

**【中文注释】** 在1 GHz时，铜的集肤深度仅为2.1微米。这意味着高频电流只在导体表面约2 \mum的薄层内流动，导体的中心区域几乎没有电流。因此，在射频应用中，镀银（silver plating）被广泛用于减小导体损耗，因为银的电导率最高。

---

### AWG Wire Gauge | 美制线规（AWG）

The **American Wire Gauge (AWG)** system standardizes wire sizes in the US. Key rule: diameter doubles every 6 AWG steps. For AWG 50, diameter = 1 mil = $2.54 \times 10^{-5}$ m.

**Example 1-2:** For AWG 50 wire ($d = 1$ mil), AWG 26 wire has diameter $d = 16$ mils:

$$r_{\text{AWG26}} = 8 \times 2.54 \times 10^{-5} = 0.2032 \text{ mm}$$

**【中文注释】** 线规系统的设计非常精巧：每增加6个AWG编号，直径大约增加一倍（具体来说是从AWG 50的1 mil起，每6步翻一番）。这是一种对数尺度的设计，从AWG 50（最细）到AWG 0000（最粗）共40个级别。射频工程中常用的AWG 26（约0.2 mm半径）在MHz频率下仍需考虑集肤效应。

---

## 1.4.1 High-Frequency Resistors | 高频电阻器

### Types of Resistors | 电阻器类型

1. **Carbon-composite resistors** — high-density dielectric granules
2. **Wire-wound resistors** — nickel or other winding material
3. **Metal-film resistors** — temperature-stable materials
4. **Thin-film chip resistors** (SMD) — aluminum or beryllium-based materials

For RF/MW circuits, **thin-film chip resistors** are preferred due to their small size and low parasitic inductance.

**【中文注释】** 在射频应用中，碳复合电阻和线绕电阻由于其显著的寄生电感（线绕结构本身就是一个电感器）而不适用。薄膜芯片电阻器凭借其紧凑的物理尺寸和相对较低的寄生效应，成为射频电路的首选。

---

### RF Equivalent Circuit of a Resistor | 电阻器的高频等效电路

The equivalent circuit of a high-frequency resistor includes:

- **$L$** — lead inductance (modeling finite lead dimensions)
- **$C_a$** — capacitance due to actual wire arrangement (charge separation)
- **$C_b$** — inter-lead capacitance

For wire-wound resistors, additional elements:
- **$L_1$** — inductance of the wound coil itself
- **$C_s$** — stray capacitance between windings

**【中文注释】** 即使是一个看似"纯电阻"的元件，在高频下也包含多个寄生参数。引线电感$L$在GHz频段会显著增加阻抗，而寄生电容$C_a$和$C_b$则在高频下使阻抗减小。等效电路模型是一个典型的二阶系统，具有谐振特性。

---

### Example 1-3: 500 Ω Metal-Film Resistor | 例1-3：500 Ω金属膜电阻

**Problem:** Find the high-frequency impedance of a $500\,\Omega$ metal-film resistor with 2.5 cm AWG 26 copper leads and $C_s = 5$ pF stray capacitance.

**Solution:**

Lead radius: $a = 0.2032$ mm (from Example 1-2)

Lead inductance at high frequency:

$$L = \frac{R_{\text{DC}} \cdot a}{2\delta}$$

$$\delta = \sqrt{\frac{1}{\pi f \mu_0 \sigma_{\text{Cu}}}} = \sqrt{\frac{1}{\pi f \times 4\pi \times 10^{-7} \times 64.516 \times 10^6}}$$

For $f \gg 95$ kHz (where $\delta \ll a$):

$$L \approx \frac{R \cdot a}{2\delta} = \frac{500 \times 0.2032 \times 10^{-3}}{2\delta} = \frac{0.1016}{\delta} \text{ H}$$

The total impedance:

$$Z(\omega) = R + j\omega L \parallel \frac{1}{j\omega C_s} = R + \frac{j\omega L}{1 - \omega^2 LC_s}$$

**Result (Figure 1-10):**
- **Low frequency:** $Z \approx R = 500\,\Omega$ (purely resistive)
- **10 MHz–20 GHz:** Capacitive reactance dominates → impedance decreases
- **Near 20 GHz:** Resonance peak due to lead inductance
- **Above resonance:** Inductive behavior → impedance rises

**【中文注释】** 这个例子深刻说明了看似简单的电阻器在高频下的复杂行为。在低频时，阻抗就是标称值500 Ω；但当频率超过10 MHz时，寄生电容开始主导，使阻抗减小；在约20 GHz处，引线电感与寄生电容发生谐振，产生阻抗峰值；超过谐振点后，感性行为主导，阻抗再次上升。设计射频电路时必须考虑这些谐振点。

---

## 1.4.2 High-Frequency Capacitors | 高频电容器

### Dielectric Loss and Loss Tangent | 介质损耗与损耗角正切

At high frequencies, dielectric materials become **lossy** (they conduct). The impedance of a real capacitor is:

$$Z_C = \frac{1}{G_e + j\omega C} = \frac{1}{j\omega C + G_e} \tag{1.15}$$

where $G_e = \sigma_{\text{diel}} A / d$ is the dielectric conductance.

The **loss tangent** is defined as:

$$\tan \delta = \frac{\sigma_{\text{diel}}}{\omega \varepsilon} = \frac{G_e}{\omega C} \tag{1.16}$$

The equivalent series resistance (ESR):

$$\text{ESR} = \frac{\tan \delta}{\omega C}$$

**【中文注释】** 损耗角正切$\tan \delta$是衡量电容器介质损耗的关键参数。$\tan \delta$越小，介质越理想。对于高质量的射频电容器，$\tan \delta$通常在$10^{-4}$至$10^{-3}$量级。ESR（等效串联电阻）是损耗角正切的直接体现，ESR越大，射频能量在电容器中转化为热能越多。

---

### RF Capacitor Equivalent Circuit | 射频电容器等效电路

The equivalent circuit of a high-frequency capacitor includes:

- **$R_s$** — series resistance (conductor losses in leads)
- **$L$** — lead inductance
- **$R_e = 1/G_e$** — parallel leakage resistance (dielectric loss)
- **$C$** — ideal capacitance

**【中文注释】** 与电阻器类似，电容器也有寄生元件。引线电感$L$在高频下与电容$C$形成串联谐振，影响电容的高频性能。在选择射频电容器时，需要关注其ESR、自谐振频率（SRF）以及损耗角正切的频率特性。

---

### Example 1-4: 47 pF Capacitor | 例1-4：47 pF电容器

**Problem:** Compute the high-frequency impedance of a 47 pF capacitor with alumina dielectric ($\tan \delta = 10^{-4}$, assumed frequency-independent), 1.25 cm AWG 26 copper leads.

**Solution:**

Lead inductance: $L = \frac{R_{\text{DC}} \cdot a}{2\delta}$ (similar to resistor example)

Series resistance of leads: $R_s = \frac{l}{\sigma_{\text{Cu}} \pi a^2}$

Leakage resistance: $R_e = \frac{1}{\omega C \tan \delta}$

The frequency response (Figure 1-12) shows:
- **Low frequency:** Capacitive reactance dominates, $Z \approx 1/(\omega C)$
- **At SRF:** Series resonance of $L$ and $C$ creates a minimum impedance
- **Above SRF:** Inductive behavior dominates

**【中文注释】** 47 pF电容器的阻抗频率响应展示了典型电容器的高频行为：随着频率升高，容抗$1/(\omega C)$减小；当频率达到自谐振频率时，电容的容性阻抗与引线电感的感性阻抗相消，产生最小阻抗；超过自谐振频率后，电感主导，阻抗开始随频率增加。

---

### Surface-Mounted Ceramic Capacitor | 表面贴装陶瓷电容器

A ceramic multilayer capacitor (Figure 1-13) consists of interleaved metal electrodes sandwiched in a ceramic dielectric block. This construction maximizes electrode surface area $A$ for a given volume, achieving high capacitance per unit volume.

Typical specifications:
- Capacitance range: $0.47$ pF to $100$ nF
- Operating voltage: $16$ V to $63$ V
- Loss tangent: $\tan \delta \approx 10^{-5}$ (at 1 MHz test frequency)
- **Note:** Loss tangent increases significantly at GHz frequencies

**【中文注释】** 表面贴装陶瓷电容器（SMD陶瓷电容）是射频电路中最常用的无源元件之一。多层结构通过增加电极有效面积来提高单位体积的容值。在1 MHz测试频率下$\tan \delta \approx 10^{-5}$看起来很好，但在GHz频率下损耗角正切会显著增加，这意味着介质损耗增加。在选择射频电容时，需要查阅厂家提供的GHz频段ESR数据。

---

## 1.4.3 High-Frequency Inductors | 高频电感器

### Distributed Capacitance and Series Resistance | 分布电容与串联电阻

A wound coil has:
- **Series resistance** $R_s$ — frequency-dependent (skin effect in wire)
- **Distributed shunt capacitance** $C_d$ — between adjacent turns

The equivalent circuit: $L$ (ideal inductor) in series with $R_s$, with $C_d$ shunting the entire structure.

**【中文注释】** 线圈电感器在高频下的行为比电阻器和电容器更为复杂。由于线匝之间的紧密排列，相邻线匝之间存在寄生电容（分布电容$C_d$），同时导线的集肤效应使串联电阻$R_s$随频率增加。这些寄生效应共同导致了电感器在高频下的多种谐振模式。

---

### Quality Factor Q | 品质因数Q

The **quality factor** $Q$ characterizes the ratio of stored energy to dissipated energy:

$$Q = \frac{|X|}{R_s} = \frac{\omega L}{R_s} \tag{1.18}$$

A **high $Q$** indicates low losses (desirable for tuning elements).
A **low $Q$** indicates significant resistive dissipation.

**【中文注释】** 品质因数$Q$是射频电感器和电容器最重要的性能指标之一。$Q$值越高，元件在谐振时的选择性越好，带宽越窄。对于射频线圈（RFC），高$Q$值意味着对射频信号的有效阻塞（近似开路），同时对直流低阻抗（近似短路）。

---

### Example 1-5: RF Coil (RFC) | 例1-5：射频线圈

**Problem:** Estimate the frequency response of an RFC with $N = 3.5$ turns of AWG 36 copper wire on a $0.1$ inch (radius $r = 1.27$ mm) air core, coil length $l = 0.05$ inch ($1.27$ mm).

**Solution:**

From Table A-4, AWG 36 wire radius: $a = 2.5$ mils $= 63.5\,\mu\text{m}$

Turn spacing: $d = l/N = 3.6 \times 10^{-4}$ m

Air-core solenoid inductance (approx.):

$$L = \frac{\mu_0 N^2 \pi r^2}{l} = \frac{4\pi \times 10^{-7} \times 3.5^2 \times \pi \times (1.27 \times 10^{-3})^2}{1.27 \times 10^{-3}} \approx 61.4 \text{ nH}$$

Distributed capacitance (parallel-plate approximation):

$$C_d \approx \frac{\varepsilon_0 A}{d} = \frac{\varepsilon_0 \cdot (2\pi r N) \cdot (2a)}{d}$$

Wire DC resistance (neglect skin effect at these dimensions):

$$R_s = \frac{l_{\text{wire}}}{\sigma_{\text{Cu}} \pi a^2} = \frac{2\pi r N}{\sigma_{\text{Cu}} \pi a^2}$$

The resulting frequency response (Figure 1-17):
- **Low frequency:** Inductive response, $Z = j\omega L$
- **Near resonance:** $Z$ peaks due to $L$–$C_d$ resonance (finite $R_s$ limits peak)
- **Above resonance:** Capacitive response, $Z$ decreases

**【中文注释】** 这个例子展示了一个典型的射频线圈（RFC）的频率响应。RFC在射频电路中用于直流偏置网络，对射频信号呈现高阻抗（近似开路），对直流呈现低阻抗（近似短路）。但图1-17显示，RFC在高频下会因分布电容$C_d$而产生谐振，此时它不再表现为纯感性。因此在设计偏置网络时，必须考虑RFC的谐振特性。

---

## 1.5 Chip Components and Circuit Board Considerations | 芯片元件与电路板考虑

### 1.5.1 Chip Resistors | 芯片电阻器

Chip resistors use a **metal film** (typically nichrome, NiCr) deposited on a ceramic substrate (aluminum oxide, $\text{Al}_2\text{O}_3$). The resistive layer is trimmed to the desired value, and contacts are soldered at both ends.

**Size code convention:** First two digits = length in tens of mils; last two digits = width in mils.
Example: "1210" → length = 120 mils, width = 100 mils.

| Power Rating | Size (mil) | Typical Use |
|-------------|-----------|-------------|
| 0.5 W | 40 × 20 | Mobile RF circuits |
| 1 W | 60 × 30 | General RF |
| 1000 W | 1 × 1 inch | RF power amplifiers |

Resistance range: $0.1\,\Omega$ to several M$\Omega$; typical tolerance: $\pm 5\%$ to $\pm 0.01\%$.

**【中文注释】** 芯片电阻器的尺寸代码是一个二位数字系统：前两位表示长度（以十分之一 mil 为单位），后两位表示宽度。例如，"0603"表示长度6×0.1=0.6 mil，宽度0.3 mil（但实际上这个换算规则因制造商而异）。在功率放大器（PA）中，可能需要高达1000 W的电阻器，这类电阻器的尺寸可达1英寸×1英寸。

---

### 1.5.2 Chip Capacitors | 芯片电容器

Single-plate and multilayer (MLC) configurations are common. Capacitor clusters (dual, quadruple) share a common dielectric.

| Type | Size Range | Capacitance Range |
|------|-----------|-------------------|
| Single-plate | 15–400 mils square | 0.1 pF to several pF |
| Multilayer (MLC) | up to 400 × 425 mils | up to 100 nF |

Typical tolerance: $\pm 2\%$ to $\pm 50\%$; for small capacitances: expressed in pF (e.g., $0.5 \pm 0.25$ pF).

**【中文注释】** 多层陶瓷电容器（MLCC）是目前最常用的射频电容类型。通过在陶瓷介质中交替堆叠金属电极，MLCC在紧凑的封装内实现了很高的容值。常见的MLCC使用X7R、C0G（NPO）等介质材料，其中C0G具有更好的温度稳定性但容值较低。

---

### 1.5.3 Surface-Mounted Inductors | 表面贴装电感器

Two main types:
1. **Wire-wound air-core inductors** — most common; dimensions 60×30 mils to 180×120 mils; inductance range $1$ nH to $1000\,\mu$H
2. **Flat coils** — integrated with microstrip lines; very thin (2 mm × 2 mm possible); inductance $1$ to $500$ nH

Flat coils use an **air bridge** (wire or conductive ribbon) to connect the coil ends without shorting to the underlying substrate.

**【中文注释】** 表面贴装线绕电感器仍然是射频应用中最常见的形式。当电路板厚度受限（如手机）时，扁平线圈成为更好的选择。扁平线圈可以与微带传输线集成在一起，尺寸可以做到2 mm × 2 mm，但电感值较低（约1–500 nH）。在GHz频段，即使较低的感值也能提供足够的电抗（$\omega L > 1$ kΩ）。

---

## 1.6 Summary | 本章小结

### Key Concepts | 核心概念

1. **Electromagnetic wave nature dominates at RF** — Kirchhoff's laws fail when component dimensions are comparable to wavelength

2. **TEM wave parameters:**
   - Intrinsic impedance: $Z_0 = \sqrt{\mu/\varepsilon} \approx 377\,\Omega$ (free space)
   - Phase velocity: $v_p = c/\sqrt{\mu_r \varepsilon_r}$
   - Wavelength: $\lambda = c/f$

3. **Skin effect:** Current flows near conductor surface; skin depth $\delta = \sqrt{2/(\omega\mu\sigma)}$

4. **RF passive component equivalent circuits are frequency-dependent:**
   - Resistors: show resonance at GHz due to lead $L$ and parasitic $C$
   - Capacitors: show series resonance at SRF due to lead $L$
   - Inductors: show parallel resonance due to distributed $C_d$

5. **Chip components:** Physical dimensions must be minimized to keep component sizes $\ll \lambda$

### Key Equations | 核心公式

$$\boxed{Z_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} \approx 377\,\Omega}$$

$$\boxed{\delta = \sqrt{\frac{1}{\pi f \mu \sigma_{\text{cond}}}}$$

$$\boxed{Q = \frac{|X|}{R_s} = \frac{\omega L}{R_s}}$$

$$\boxed{\tan \delta = \frac{\sigma_{\text{diel}}}{\omega \varepsilon} = \frac{G_e}{\omega C}}$$

**【中文注释】** 本章建立了射频电路分析的基础：理解为什么在高频下传统电路理论失效，引入电磁波传播的基本概念，掌握集肤效应对导体行为的影响，以及理解电阻、电容、电感在高频下的等效电路模型。这些基础知识将在后续章节中（传输线理论、史密斯圆图、S参数、滤波器设计、匹配网络、放大器设计等）反复运用。