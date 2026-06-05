# Chapter 9 — Crosstalk / 第9章——串扰

> **中英双语版**

**Source:** Paul, *Introduction to Electromagnetic Compatibility*, 2nd Ed., Ch. 9 (P559–742)
**来源：** Paul《电磁兼容导论》第2版，第9章（第559–742页）

---

## 9.1 Overview / 概述

Crosstalk is the **unintended electromagnetic coupling** between wires or PCB lands in close proximity. Unlike antenna coupling (far-field), crosstalk is a **near-field coupling** problem. The source and receptor reside within the same system — this is *intrasystem* EMC.
串扰是邻近导线或PCB走线之间的**无意电磁耦合**。与天线耦合（远场）不同，串扰是一个**近场耦合**问题。源和受扰者位于同一系统内——这是*系统内*EMC。

**Three roles of crosstalk in EMC failure / 串扰在EMC失效中的三种角色：**

| Failure Mode / 失效模式 | Mechanism / 机制 |
|---|---|
| Self-interference / 自干扰 | Coupling between internal conductors / 内部导体之间的耦合 |
| Radiated emission / 辐射发射 | Ribbon cable → peripheral cable → external radiation / 排线→外设电缆→外部辐射 |
| Conducted emission / 传导发射 | Coupling to power cord / 耦合至电源线 |
| Susceptibility / 敏感度 | External emissions couple to internal cables / 外部发射耦合至内部电缆 |

**Fundamental requirement / 基本要求：** A crosstalk problem requires **≥ 3 conductors** (a generator circuit + a receptor circuit + a reference conductor). Two-conductor lines have no crosstalk by definition.
串扰问题需要**≥ 3根导体**（一个产生电路 + 一个受扰电路 + 一个参考导体）。两导体传输线定义上不存在串扰。

---

## 9.2 Three-Conductor Transmission Lines / 三导体传输线

### 9.2.1 Geometry / 几何结构

A three-conductor transmission line consists of / 三导体传输线包括：

- **Generator conductor / 产生导体** — driven by source $V_S(t)$ through $R_S$, load $R_L$ / 由源 $V_S(t)$ 通过 $R_S$ 驱动，负载 $R_L$
- **Reference conductor / 参考导体** — common return path / 公共返回路径
- **Receptor conductor / 受扰导体** — terminated at near-end ($R_{NE}$) and far-end ($R_{FE}$) / 近端($R_{NE}$)和远端($R_{FE}$)端接

- Line extends $z = 0$ to $z = L$ / 传输线从 $z = 0$ 延伸到 $z = L$
- **Near-end (NE) / 近端：** adjacent to the source end / 靠近源端
- **Far-end (FE) / 远端：** opposite the source end / 远离源端

### 9.2.2 Typical Configurations / 典型结构

**Wire-type lines / 线缆型：**
- Three wires in a ribbon cable (one as reference) / 排线中的三根线（一根作参考）
- Two wires above an infinite ground plane / 无限大地平面上方的两根线
- Two wires inside a cylindrical shield (reference = shield) / 圆柱形屏蔽体内的两根线（参考=屏蔽体）

**PCB-type lines / PCB型：**
- **Coupled stripline / 耦合带状线：** lands between two infinite ground planes (homogeneous medium, $\varepsilon_r$ of board material) / 两个无限大地平面之间的走线（均匀介质，板材$\varepsilon_r$）
- **Coupled microstrip / 耦合微带线：** lands on outer surface of board (inhomogeneous — fields partly in air, partly in dielectric; two propagation velocities) / 板外层表面的走线（非均匀——场部分在空气中、部分在介质中；两种传播速度）
- **Single-sided PCB / 单面PCB：** one land as reference on outer surface / 外层表面一条走线作参考

### 9.2.3 Velocity of Propagation / 传播速度

For a homogeneous medium / 对于均匀介质：

$$v = \frac{c_0}{\sqrt{\varepsilon_r}} = \frac{3\times 10^8\ \text{m/s}}{\sqrt{\varepsilon_r}}$$

For glass-epoxy PCB ($\varepsilon_r \approx 4.7$) / 对于玻璃环氧PCB ($\varepsilon_r \approx 4.7$)：$v = 1.38\times 10^8$ m/s $= 5.45$ in/ns.

---

## 9.3 Transmission-Line Equations for Lossless Lines / 无耗线的传输线方程

### 9.3.1 Fundamental Assumption: TEM Mode / 基本假设：TEM模

The **transverse electromagnetic (TEM)** field structure assumes $\mathbf{E}$ and $\mathbf{H}$ lie entirely in the transverse ($xy$) plane — no field components along the line axis ($z$). Under TEM / **横电磁(TEM)**场结构假设 $\mathbf{E}$ 和 $\mathbf{H}$ 完全位于横向($xy$)平面内——沿传输线轴($z$)方向无场分量。在TEM条件下：

- Line voltages $V_G(z,t)$, $V_R(z,t)$ and currents $I_G(z,t)$, $I_R(z,t)$ are uniquely defined / 线电压 $V_G(z,t)$、$V_R(z,t)$ 和电流 $I_G(z,t)$、$I_R(z,t)$ 唯一确定
- Cross-sectional field structure equals a static (DC) case → per-unit-length $L$ and $C$ can be computed using dc methods / 截面场结构等于静态(DC)情况 → 可用DC方法计算单位长度 $L$ 和 $C$
- Pure TEM cannot exist for inhomogeneous medium / 非均匀介质中无法存在纯TEM模

### 9.3.2 Per-Unit-Length Equivalent Circuit / 单位长度等效电路

For a $\Delta z$ section / 对于 $\Delta z$ 段：

- **$l_G$, $l_R$:** self-inductances per unit length of generator/receptor circuits / 产生/受扰电路的单位长度自感
- **$l_m$:** per-unit-length mutual inductance between circuits / 电路间的单位长度互感
- **$c_G$, $c_R$:** self-capacitances per unit length / 单位长度自电容
- **$c_m$:** per-unit-length mutual capacitance / 单位长度互电容

### 9.3.3 MTL Equations (Time Domain) / 多导体传输线方程（时域）

$$\frac{\partial V_G}{\partial z} = -l_G\frac{\partial I_G}{\partial t} - l_m\frac{\partial I_R}{\partial t} \quad (9.2a)$$

$$\frac{\partial V_R}{\partial z} = -l_m\frac{\partial I_G}{\partial t} - l_R\frac{\partial I_R}{\partial t} \quad (9.2b)$$

$$\frac{\partial I_G}{\partial z} = -(c_G + c_m)\frac{\partial V_G}{\partial t} - c_m\frac{\partial V_R}{\partial t} \quad (9.2c)$$

$$\frac{\partial I_R}{\partial z} = -c_m\frac{\partial V_G}{\partial t} - (c_R + c_m)\frac{\partial V_R}{\partial t} \quad (9.2d)$$

In matrix form / 矩阵形式：

$$\frac{\partial}{\partial z}\mathbf{V}(z,t) = -\mathbf{L}\frac{\partial}{\partial t}\mathbf{I}(z,t) \quad (9.3a)$$

$$\frac{\partial}{\partial z}\mathbf{I}(z,t) = -\mathbf{C}\frac{\partial}{\partial t}\mathbf{V}(z,t) \quad (9.3b)$$

where / 其中：

$$\mathbf{V}(z,t) = \begin{bmatrix}V_G(z,t)\\ V_R(z,t)\end{bmatrix},\quad \mathbf{I}(z,t) = \begin{bmatrix}I_G(z,t)\\ I_R(z,t)\end{bmatrix}$$

$$\mathbf{L} = \begin{bmatrix}l_G & l_m\\ l_m & l_R\end{bmatrix} \quad (9.5a)$$

$$\mathbf{C} = \begin{bmatrix}c_G + c_m & -c_m\\ -c_m & c_R + c_m\end{bmatrix} \quad (9.5b)$$

### 9.3.4 Phasor (Frequency-Domain) Equations / 相量（频域）方程

$$\frac{d}{dz}\hat{\mathbf{V}}(z) = -j\omega\mathbf{L}\ \hat{\mathbf{I}}(z) \quad (9.6a)$$

$$\frac{d}{dz}\hat{\mathbf{I}}(z) = -j\omega\mathbf{C}\ \hat{\mathbf{V}}(z) \quad (9.6b)$$

---

## 9.4 Per-Unit-Length Parameters / 单位长度参数

### 9.4.1 Homogeneous Medium / 均匀介质

For a homogeneous surrounding medium / 对于均匀介质环境：

$$\mathbf{LC} = \mathbf{CL} = \mu\varepsilon\ \mathbf{I}_2 \tag{9.8}$$

$$\mathbf{C} = \frac{1}{v^2}\mathbf{L}^{-1} \tag{9.10}$$

**Only one parameter matrix needs to be determined** / **仅需确定一个参数矩阵**。

### 9.4.2 Wide-Separation Approximations for Bare Wires / 裸导线的大间距近似

**Three-Wire Ribbon Cable (center wire = reference) / 三线排线（中间导线=参考）：**

$$l_G = l_R = \frac{\mu_0}{\pi}\ln\frac{d}{r_w} \tag{9.28-9.29}$$

$$l_m = \frac{\mu_0}{2\pi}\ln\frac{d}{2r_w} \tag{9.30}$$

**Two Wires above Ground Plane / 地平面上方双线：**

$$l_G = \frac{\mu_0}{2\pi}\ln\frac{2h_G}{r_{wG}} \tag{9.31}$$

$$l_m = \frac{\mu_0}{4\pi}\ln\left(1 + \frac{4h_Gh_R}{s^2}\right) \tag{9.35}$$

**Two Wires within Cylindrical Shield (shield = reference) / 圆柱形屏蔽体内双线（屏蔽体=参考）：**

$$l_G = \frac{\mu_0}{2\pi}\ln\frac{r_{SH}^2 - d_G^2}{r_{SH}r_{wG}} \tag{9.36}$$

### 9.4.3 Proximity Effect / 邻近效应

When wire separation-to-radius ratio $< 5:1$, charge distributions peak on facing sides / 当线间距与半径比 $< 5:1$ 时，电荷分布在相对侧集中。Wide-separation formulas become inaccurate / 大间距公式不再准确。For close spacing, **numerical methods (MoM)** must be used / 对于紧密间距，必须使用**数值方法（矩量法）**。

---

## 9.5 Inductive–Capacitive Coupling Approximate Model / 电感-电容耦合近似模型

### 9.5.1 Weak Coupling Assumption / 弱耦合假设

The **weak coupling** condition means coupling is a **one-way effect**: from generator circuit to receptor circuit only.
**弱耦合**条件指耦合是**单向效应**：仅从产生电路到受扰电路。

### 9.5.2 Physical Mechanism / 物理机制

**Inductive coupling / 电感耦合：** Time-varying current in generator circuit creates changing magnetic flux that penetrates the receptor loop → Faraday's law induces a voltage / 产生电路中的时变电流产生变化磁通，穿透受扰回路 → 法拉第定律感应出电压 $v_{ind} = l_m \frac{dI_G}{dt}$ per unit length / 每单位长度。

**Capacitive coupling / 电容耦合：** Time-varying voltage on generator circuit creates changing electric field → displacement current / 产生电路上的时变电压产生变化电场 → 位移电流 $i_{cap} = c_m \frac{dV_G}{dt}$ coupled between circuits / 在电路之间耦合。

### 9.5.3 Frequency-Domain Model / 频域模型

**Near-end crosstalk / 近端串扰：**

$$\hat{V}_{NE} = \frac{R_{NE}}{R_{NE}+R_{FE}}j\omega L_m\frac{\hat{V}_S}{R_S+R_L} + \frac{R_{NE}R_{FE}}{R_{NE}+R_{FE}}j\omega C_m\frac{R_L\hat{V}_S}{R_S+R_L} \tag{9.66a}$$

**Far-end crosstalk / 远端串扰：**

$$\hat{V}_{FE} = -\frac{R_{FE}}{R_{NE}+R_{FE}}j\omega L_m\frac{\hat{V}_S}{R_S+R_L} + \frac{R_{NE}R_{FE}}{R_{NE}+R_{FE}}j\omega C_m\frac{R_L\hat{V}_S}{R_S+R_L} \tag{9.66b}$$

### 9.5.5 Dominance of Coupling Mechanism / 耦合机制的主导性

**Inductive coupling dominates / 电感耦合主导** (current-driven / 电流驱动) when termination impedances are low relative to $Z_C$ / 当终端阻抗相对于 $Z_C$ 较低时：

$$\frac{L_m}{C_m} = Z_C^2 \ll R_{NE}R_{FE}$$

**Capacitive coupling dominates / 电容耦合主导** (voltage-driven / 电压驱动) when termination impedances are high relative to $Z_C$ / 当终端阻抗相对于 $Z_C$ 较高时：

$$R_{NE}R_{FE} \gg Z_C^2$$

### 9.5.6 Frequency Response / 频率响应

Both inductive and capacitive contributions are **proportional to $\omega$** → crosstalk transfer function rises at **+20 dB/decade** up to the frequency where $L \sim \lambda/6$, then resonances appear.
电感和电容贡献均**正比于 $\omega$** → 串扰传递函数以**+20 dB/十倍频程**上升，至 $L \sim \lambda/6$ 的频率后出现谐振。

### 9.5.7 Common-Impedance Coupling / 公共阻抗耦合

Imperfect reference conductor resistance $R_0 = r_0 L$ produces a frequency-independent floor / 非理想参考导体电阻 $R_0 = r_0 L$ 产生与频率无关的基底。

---

## 9.6 Time-Domain Inductive–Capacitive Model / 时域电感-电容模型

### 9.6.1 The Derivative Relationship / 导数关系

Since $j\omega \leftrightarrow d/dt$ / 由于 $j\omega \leftrightarrow d/dt$：

$$V_{NE}(t) = M_{NE}\frac{dV_S(t)}{dt} \quad (9.80a)$$

$$V_{FE}(t) = M_{FE}\frac{dV_S(t)}{dt} \quad (9.80b)$$

### 9.6.2 Waveform Shape — Trapezoidal Pulse Train / 波形形状——梯形脉冲序列

The crosstalk is the **derivative** of the source voltage. A fast edge produces large crosstalk spikes.
串扰是源电压的**导数**。快速边沿产生大的串扰尖峰。

**Peak amplitude (ignoring losses) / 峰值幅度（忽略损耗）：**

$$\text{Peak} = M \cdot \frac{V_{PP}}{t_r}$$

### 9.6.3 Validity Criterion / 有效性判据

The line must be **electrically short** / 传输线必须是**电短**的：

$$t_r,\ t_f \gtrsim 10\ T_D \tag{9.84}$$

where $T_D = L/v$ is the one-way transit time / 其中 $T_D = L/v$ 为单向传播时间。

### 9.6.4 Time-Domain with Common-Impedance / 含公共阻抗的时域模型

$$V_{NE}(t) = \left(M_{NE}^{IND}+M_{NE}^{CAP}\right)\frac{dV_S(t)}{dt} + M_{NE}^{CI}V_S(t) \quad (9.85a)$$

---

## 9.7 Lumped-Circuit Approximate Models / 集总电路近似模型

For SPICE simulation when exact MTL solution is not required / 当不需要精确MTL解时用于SPICE仿真。Using **5 Pi sections** gives good accuracy for most practical lines / 使用**5个Pi节**对大多数实际传输线可获得良好精度。

---

## 9.8 Exact SPICE/PSPICE Model for Lossless Coupled Lines / 无耗耦合线的精确SPICE/PSPICE模型

### 9.8.1 Modal Decomposition / 模态分解

The key to exact solution is **decoupling** the MTL equations via a modal transformation.
精确解的关键是通过模态变换**解耦**MTL方程。

$$\mathbf{V}(z,t) = \mathbf{T}_V\mathbf{V}_m(z,t) \quad (9.90a)$$

$$\mathbf{I}(z,t) = \mathbf{T}_I\mathbf{I}_m(z,t) \quad (9.90b)$$

---

## 9.9 Engineering Intuition Summary / 工程直觉总结

| Concept / 概念 | Intuition / 直觉 |
|---|---|
| **Near-end crosstalk / 近端串扰** | Always positive; sum of inductive and capacitive contributions / 始终为正；电感与电容贡献之和 |
| **Far-end crosstalk / 远端串扰** | Inductive and capacitive contributions have opposite signs → may partially cancel / 电感与电容贡献符号相反 → 可能部分抵消 |
| **Inductive dominates / 电感主导** | Low-$Z$ terminations (50 Ω) / 低$Z$端接(50 Ω) |
| **Capacitive dominates / 电容主导** | High-$Z$ terminations (1 kΩ) / 高$Z$端接(1 kΩ) |
| **Crosstalk rises with frequency / 串扰随频率上升** | $+20$ dB/decade because both mechanisms $\propto \omega$ / 两种机制均$\propto \omega$ |
| **Common-impedance floor / 公共阻抗基底** | Imperfect reference conductor / 非理想参考导体 |
| **Line electrically short criterion / 电短线判据** | $L < \lambda/6$ or $t_r > 10\cdot T_D$ |
| **Crosstalk during transitions / 跳变期间的串扰** | Derivative relationship / 导数关系 |
| **Ribbon cable reference / 排线参考导体选择** | Center wire as reference gives lower crosstalk / 中间导线作参考串扰更低 |

---

## 9.10 Key Formula Reference / 关键公式参考

### Per-Unit-Length Parameters / 单位长度参数

| Configuration / 结构 | $l_G, l_R$ | $l_m$ |
|---|---|---|
| 3-wire ribbon (center ref) / 三线排线（中间参考） | $\frac{\mu_0}{\pi}\ln\frac{d}{r_w}$ | $\frac{\mu_0}{2\pi}\ln\frac{d}{2r_w}$ |
| 2 wires over ground plane / 地平面上方双线 | $\frac{\mu_0}{2\pi}\ln\frac{2h}{r_w}$ | $\frac{\mu_0}{4\pi}\ln\left(1+\frac{4h_Gh_R}{s^2}\right)$ |

### Crosstalk Transfer Functions / 串扰传递函数

$$\frac{\hat{V}_{NE}}{\hat{V}_S} = j\omega\left[\frac{R_{NE}}{R_{NE}+R_{FE}}\frac{L_m}{R_S+R_L} + \frac{R_{NE}R_{FE}}{R_{NE}+R_{FE}}\frac{R_LC_m}{R_S+R_L}\right]$$

### Time-Domain (Electrically Short) / 时域（电短线）

$$V_{NE}(t) = M_{NE}\frac{dV_S(t)}{dt} + M_{NE}^{CI}V_S(t)$$

### Validity Criterion / 有效性判据

$$t_r,\ t_f \gtrsim 10\cdot\frac{L}{v}$$

---

*Notes compiled by 小龙虾 (Xiǎolóngxiā) — 电磁组*
*No content generated from internal knowledge; all formulas and values derived from source text only.*
