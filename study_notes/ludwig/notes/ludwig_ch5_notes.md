# Chapter 5: RF Filter Design | 第5章：射频滤波器设计
# 第5章：RF滤波器设计概论

> **本章简介 / Chapter Overview**  
> 本章从第4章的单端口和双端口网络理论出发，将被动RF器件的知识拓展至RF滤波器的分析与设计。重点讨论四种基本滤波器类型（低通、高通、带通、带阻）的频率响应特性，引入有载Q因子和无载Q因子的概念，建立滤波器设计的归一化低通原型方法。  
> 本章还介绍如何通过Richards变换和Kuroda恒等式将集总元件滤波器转换为分布式传输线滤波器，这对频率>500MHz的微波频段设计至关重要。

---

## 5.1 Basic Resonator and Filter Configurations | 基本谐振器与滤波器配置

### 5.1.1 Filter Types and Parameters | 滤波器类型与参数

#### Four Ideal Filter Types | 四种理想滤波器类型

In analog circuit design, it is of particular interest to manipulate high-frequency signals so as to enhance or attenuate certain frequency ranges or bands. RF filters are the fundamental building blocks that perform this frequency-selective filtering.

在模拟电路设计中，对高频信号进行频率选择性处理以增强或衰减特定频段，是一个核心课题。RF滤波器是执行这种频率选择滤波的基本构建模块。

The four fundamental filter types are illustrated in Fig. 5-1:

四种基本滤波器类型如图5-1所示：

| Filter Type 滤波器类型 | Passband behavior 通带特性 | Stopband behavior 阻带特性 |
|---|---|---|
| **Low-Pass (LP)** 低通 | $0 \leq \Omega \leq 1$ (flat, low attenuation 低衰减) | $\Omega > 1$ (increasing attenuation 衰减增加) |
| **High-Pass (HP)** 高通 | $\Omega \geq 1$ (flat, low attenuation) | $0 \leq \Omega < 1$ (increasing attenuation) |
| **Bandpass (BP)** 带通 | $\Omega_1 \leq \Omega \leq \Omega_2$ (passband) | $\Omega < \Omega_1$ or $\Omega > \Omega_2$ (rejection) |
| **Bandstop (BS)** 带阻 | $\Omega < \Omega_1$ or $\Omega > \Omega_2$ (passband) | $\Omega_1 \leq \Omega \leq \Omega_2$ (rejection) |

The normalized angular frequency is defined as:
归一化角频率定义为：

$$\Omega = \frac{\omega}{\omega_c} = \frac{f}{f_c}$$

where $\omega_c$ is the **cut-off angular frequency** for LP/HP filters and the **center angular frequency** $\omega_0 = \sqrt{\omega_1 \omega_2}$ for BP/BS filters.

其中 $\omega_c$ 是低通/高通滤波器的**截止角频率**，对于带通/带阻滤波器则是**中心角频率** $\omega_0 = \sqrt{\omega_1 \omega_2}$。

#### Filter Approximation Functions | 滤波器逼近函数

Three major approximation functions for the low-pass magnitude response are:

低通幅频响应的三种主要逼近函数为：

| Approximation 逼近函数 | Passband 通带 | Stopband 阻带 | Selectivity 选择性 |
|---|---|---|---|
| **Butterworth (Binomial)** | Monotonic 单调 | Monotonic | Low (需要更多阶数) |
| **Chebyshev** | Equal-ripple 等纹波 | Monotonic | Medium |
| **Elliptic (Cauer)** | Equal-ripple | Equal-ripple | Highest (最陡峭过渡) |

The **Butterworth** (maximally flat) response has a magnitude-squared transfer function:
巴特沃斯（最大平坦）响应的幅平方传递函数为：

$$|H(j\omega)|^2 = \frac{1}{1 + (\omega/\omega_c)^{2N}}$$

where $N$ is the filter order (number of reactive elements). At $\omega = \omega_c$, $|H| = 1/\sqrt{2}$ (i.e., $-3\text{ dB}$).

其中 $N$ 是滤波器阶数（电抗元件数量）。在 $\omega = \omega_c$ 处，$|H| = 1/\sqrt{2}$（即 $-3\text{ dB}$）。

The **Chebyshev** response permits equal-magnitude ripples in the passband (or stopband) and achieves a steeper roll-off than Butterworth for the same $N$. The Chebyshev polynomial $T_N(\Omega)$ of order $N$ satisfies $|T_N(\Omega)| \leq 1$ for $|\Omega| \leq 1$ and grows rapidly for $|\Omega| > 1$.

切比雪夫响应允许通带（或阻带）内等幅纹波，在相同阶数 $N$ 下实现比巴特沃斯更陡的滚降。$N$ 阶切比雪夫多项式 $T_N(\Omega)$ 在 $|\Omega| \leq 1$ 时满足 $|T_N(\Omega)| \leq 1$，在 $|\Omega| > 1$ 时迅速增长。

#### Key Filter Parameters | 滤波器关键参数

**Insertion Loss (IL) / 插入损耗：**
理想滤波器插入RF电路路径时，通带内应无功率损耗（$IL = 0$ dB）。实际滤波器存在一定功率损耗：

$$IL = 10\log_{10}\frac{P_{in}}{P_L} = -10\log_{10}(1 - |\Gamma_{in}|^2) \quad \text{[dB]}$$

where $P_L$ is the power delivered to the load, $P_{in}$ is the input power from the source, and $\Gamma_{in}$ is the reflection coefficient looking into the filter input.

其中 $P_L$ 是传递给负载的功率，$P_{in}$ 是来自源端的输入功率，$\Gamma_{in}$ 是滤波器输入端的反射系数。

**Ripple / 纹波：**
通带内最大与最小幅频响应之差，以 dB 或 Neper 表示。Chebyshev 滤波器的纹波幅度可精确控制。

**Bandwidth (BW) / 带宽：**
对于带通滤波器，带宽定义为上、下3 dB截止频率之差：

$$\text{BW} = f_2 - f_1 \quad \text{[Hz]}$$

**Shape Factor (SF) / 形状因子：**
描述滤波器响应锐度，取60 dB带宽与3 dB带宽之比：

$$\text{SF} = \frac{\text{BW}_{60\text{dB}}}{\text{BW}_{3\text{dB}}}$$

理想矩形系数为 1.0，实际值通常 > 1.5。

**Rejection / 抑制：**
理想滤波器对阻带信号实现无限衰减，实际设计中常以 60 dB 作为典型抑制指标。

---

### 5.1.2 Low-Pass Filter | 低通滤波器

The **loaded quality factor** $Q_L$ of a series RLC resonator is defined as the ratio of average stored energy to energy loss per radian at resonance:

串联RLC谐振器的**有载品质因子** $Q_L$ 定义为在谐振频率下，平均储能除以每弧度能量损耗：

$$Q_L = \frac{\omega_0 W_{\text{stored}}}{P_{\text{loss}}} = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 RC} = \frac{\rho}{R}$$

where $\rho = \sqrt{L/C}$ is the characteristic impedance of the resonator.

其中 $\rho = \sqrt{L/C}$ 是谐振器的特性阻抗。

For a **shunt RLC resonator**, replacing $R$ and $R_G$ by $G$ and $G_E$ (conductances) yields:
对于**并联RLC谐振器**，将 $R$ 和 $R_G$ 替换为 $G$ 和 $G_E$（电导），可得：

$$Q_L = \frac{\omega_0 C}{G} = \frac{1}{\omega_0 RG} = \frac{\rho}{R}$$

The **unloaded quality factor** $Q_0$ (no external loading) is:
**无载品质因子** $Q_0$（无外部负载）为：

$$Q_0 = \frac{\omega_0 L}{R_{\text{internal}}} = \frac{\omega_0 C}{G_{\text{internal}}}$$

The relationship between loaded and unloaded Q is:
有载Q与无载Q的关系为：

$$\frac{1}{Q_L} = \frac{1}{Q_0} + \frac{1}{Q_E}$$

where $Q_E = \omega_0 L / R_G = \rho / R_G$ is the **external quality factor**.

其中 $Q_E = \omega_0 L / R_G = \rho / R_G$ 是**外部品质因子**。

The **normalized frequency deviation** from resonance is:
归一化频率偏离定义为：

$$\xi = \frac{\omega_0}{\Delta\omega}\left(\frac{\omega}{\omega_0} - \frac{\omega_0}{\omega}\right) \approx \frac{2Q_L}{\omega_0}\Delta\omega$$

---

### 5.1.3–5.1.5 Series and Shunt Resonator Responses | 串/并联谐振器响应

For a **series RLC bandpass filter** with source impedance $R_G$ and load $R_L$:
对于源阻抗 $R_G$ 和负载 $R_L$ 的**串联RLC带通滤波器**：

The **transfer function** (voltage ratio) is:
**传递函数**（电压比）为：

$$H(j\omega) = \frac{V_L}{V_G} = \frac{R}{R + R_G + j\left(\omega L - \frac{1}{\omega C}\right)}$$

At resonance $\omega_0 = 1/\sqrt{LC}$, the imaginary part vanishes and:
在谐振 $\omega_0 = 1/\sqrt{LC}$ 时，虚部为零：

$$|H(j\omega_0)| = \frac{R}{R + R_G + R_L}$$

The **loaded Q** of the series resonator:
串联谐振器的**有载Q**：

$$Q_L = \frac{\omega_0 L}{R + R_G + R_L}$$

The **bandwidth** at the $-3\text{ dB}$ points is:
$-3\text{ dB}$ 点处的**带宽**为：

$$\text{BW}_{3\text{dB}} = \frac{\omega_0}{Q_L}$$

The **insertion loss** at resonance is:
谐振点处的**插入损耗**为：

$$IL_{\text{res}} = -20\log_{10}\left(\frac{R}{R + R_G + R_L}\right) \quad \text{[dB]}$$

For a **shunt RLC bandpass filter**, analogous expressions hold with conductances $G$, $G_E$, $G_L$ replacing resistances.

对于**并联RLC带通滤波器**，用电导 $G$、$G_E$、$G_L$ 替换电阻，可得类似表达式。

---

## 5.2 The Arbitrary Resonator | 任意谐振器

For a general two-port network resonator, define the **image impedances** $Z_{i1}$ and $Z_{i2}$ at ports 1 and 2:
对于一般双端口网络谐振器，定义端口1和端口2的**图像阻抗** $Z_{i1}$ 和 $Z_{i2}$：

$$Z_{i1} = \sqrt{\frac{A_{11}A_{12}}{A_{21}A_{22}}}, \quad Z_{i2} = \sqrt{\frac{A_{22}A_{12}}{A_{21}A_{11}}}$$

where $A_{ij}$ are the chain (ABCD) matrix elements of the two-port.

其中 $A_{ij}$ 是双端口链式（ABCD）矩阵元。

When $Z_{i1} = Z_{i2} = Z_0$ (characteristic impedance), the two-port is matched and the transmission coefficient $\tau$ becomes:
当 $Z_{i1} = Z_{i2} = Z_0$（特性阻抗）时，双端口匹配，传输系数 $\tau$ 变为：

$$\tau(\omega) = \frac{1}{\cosh\theta} = \frac{1}{\cosh(\alpha + j\beta)}$$

For a lossless network ($\alpha = 0$), $|\tau| = 1/\sqrt{1 + \sinh^2\theta|}$ which yields the bandpass characteristic.

对于无损耗网络（$\alpha = 0$），$|\tau| = 1/\sqrt{1 + \sinh^2|\theta|}$，产生带通特性。

---

## 5.3 Low-Pass Filter Design | 低通滤波器设计

### 5.3.1 Magnitude and Phase Response | 幅频与相频响应

The **transfer function magnitude squared** for an $N$-element low-pass filter prototype:
$N$ 阶低通滤波器原型的**传递函数幅平方**为：

$$|H(j\Omega)|^2 = \frac{1}{1 + \epsilon^2 C_N^2(\Omega)}$$

where $\epsilon$ is the **ripple factor** and $C_N(\Omega)$ is the Chebyshev polynomial of order $N$.

其中 $\epsilon$ 是**纹波因子**，$C_N(\Omega)$ 是 $N$ 阶切比雪夫多项式。

The **group delay** $t_g$ measures the signal propagation time through the filter:
**群时延** $t_g$ 衡量信号通过滤波器的传播时间：

$$t_g = -\frac{d\beta}{d\omega} = -\frac{d\phi(\omega)}{d\omega}$$

Linear phase response (constant $t_g$) is desirable for minimizing signal distortion.

线性相位响应（恒定 $t_g$）对于减小信号失真非常重要。

### 5.3.2 Butterworth (Maximally Flat) Approximation | 巴特沃斯（最大平坦）逼近

The magnitude-squared response is:
幅平方响应为：

$$|H(j\omega)|^2 = \frac{1}{1 + (\omega/\omega_c)^{2N}}$$

The $-3\text{ dB}$ cut-off occurs at $\omega = \omega_c$ by definition.

按定义，$-3\text{ dB}$ 截止点出现在 $\omega = \omega_c$。

### 5.3.3 Filter Coefficients | 滤波器系数

The **Butterworth polynomial** for $N$-order low-pass prototype with $g_0 = g_{N+1} = 1$:
$N$ 阶低通原型的**巴特沃斯多项式**，其中 $g_0 = g_{N+1} = 1$：

$$g_k g_{N+1-k} = 1, \quad k = 1, 2, \ldots, N$$

The **Chebyshev polynomial** $T_N(\Omega)$ is defined recursively:
切比雪夫多项式 $T_N(\Omega)$ 的递推定义为：

$$T_0(\Omega) = 1, \quad T_1(\Omega) = \Omega, \quad T_{N+1}(\Omega) = 2\Omega T_N(\Omega) - T_{N-1}(\Omega)$$

**Butterworth Low-Pass Prototype Coefficients ($g_k$, $R_G = R_L = 1\ \Omega$):**

| N | $g_1$ | $g_2$ | $g_3$ | $g_4$ | $g_5$ |
|---|---|---|---|---|---|
| 1 | 2.000 | 1.000 | — | — | — |
| 2 | 1.414 | 1.414 | 1.000 | — | — |
| 3 | 1.000 | 2.000 | 1.000 | 1.000 | — |
| 4 | 0.765 | 1.848 | 1.848 | 0.765 | 1.000 |
| 5 | 0.618 | 1.618 | 2.000 | 1.618 | 0.618 |

**Chebyshev Low-Pass Prototype Coefficients (0.5 dB equal-ripple):**

| N | $g_1$ | $g_2$ | $g_3$ | $g_4$ | $g_5$ |
|---|---|---|---|---|---|
| 1 | 0.698 | 1.000 | — | — | — |
| 2 | 1.403 | 1.284 | 1.403 | — | — |
| 3 | 1.596 | 1.670 | 1.596 | 1.000 | — |
| 4 | 1.670 | 2.057 | 2.057 | 1.670 | 1.000 |
| 5 | 1.706 | 2.541 | 2.541 | 1.706 | 1.000 |

---

## 5.4 High-Pass Filter Design | 高通滤波器设计

The frequency transformation from normalized low-pass to high-pass is:
从归一化低通到高通的频率变换为：

$$\Omega_{LP} = \frac{1}{\Omega_{HP}} = \frac{\omega_c}{\omega}$$

The element transformation rules:
元件变换规则：

$$L_{\text{HP}} = \frac{1}{\omega_c^2 C_{\text{LP}}}, \quad C_{\text{HP}} = \frac{1}{\omega_c^2 L_{\text{LP}}}$$

This transformation maps the cut-off $\Omega = 1$ of LP to $\Omega = 1$ of HP, confirming that $\omega = \omega_c$ is the high-pass cut-off frequency.

此变换将低通的截止点 $\Omega = 1$ 映射到高通的 $\Omega = 1$，确认 $\omega = \omega_c$ 是高通截止频率。

---

## 5.5 Bandpass and Bandstop Filter Design | 带通与带阻滤波器设计

### Bandpass Filter | 带通滤波器

The frequency transformation is:
频率变换为：

$$\Omega = \frac{\omega_0}{\Delta\omega}\left(\frac{\omega}{\omega_0} - \frac{\omega_0}{\omega}\right)$$

where the **center angular frequency** is:
其中**中心角频率**为：

$$\omega_0 = \sqrt{\omega_1 \omega_2}$$

and the **bandwidth** is $\Delta\omega = \omega_2 - \omega_1$.

**带宽**为 $\Delta\omega = \omega_2 - \omega_1$。

The element transformations from low-pass prototype:
从低通原型的元件变换：

$$L_{\text{BP}} = \frac{\Delta\omega L_{\text{LP}}}{\omega_0}, \quad C_{\text{BP}} = \frac{1}{\omega_0 \Delta\omega L_{\text{LP}}}$$

$$C_{\text{BP}} = \frac{\Delta\omega C_{\text{LP}}}{\omega_0}, \quad L_{\text{BP}} = \frac{1}{\omega_0 \Delta\omega C_{\text{LP}}}$$

Each low-pass element transforms into a **series** or **shunt resonant circuit** at $\omega_0$.

每个低通元件变换为在 $\omega_0$ 处的**串联**或**并联谐振电路**。

### Bandstop Filter | 带阻滤波器

The frequency transformation is:
频率变换为：

$$\Omega = \frac{\Delta\omega}{\omega_0}}\left(\frac{\omega}{\omega_0} - \frac{\omega_0}{\omega}\right)^{-1}$$

Each low-pass element transforms into an **antiresonant circuit** (parallel LC) at $\omega_0$.

每个低通元件变换为在 $\omega_0$ 处的**反谐振电路**（并联LC）。

---

## 5.6 Distributed Filter Elements | 分布式滤波器元件

At frequencies above approximately **500 MHz**, lumped inductors and capacitors become unsuitable due to parasitic effects. The solution is to replace them with transmission line segments.

在频率约 **500 MHz** 以上时，集总电感和电容因寄生效应变得不适用。解决方案是用传输线段替换它们。

### 5.6.1 Richards' Transformation | Richards变换

Richards' transformation maps an ideal lumped inductor $L$ or capacitor $C$ to an equivalent transmission line of electrical length $\theta = \omega\sqrt{LC}$:

Richards变换将理想集总电感 $L$ 或电容 $C$ 映射为电长度 $\theta = \omega\sqrt{LC}$ 的等效传输线：

$$\boxed{\text{Series inductor: } L \rightarrow \text{ Open-circuited stub of length } \theta = \omega\sqrt{LC}, \quad Z = j\omega L = jZ_0 \tan\theta}$$

$$\boxed{\text{Shunt capacitor: } C \rightarrow \text{ Short-circuited stub of length } \theta = \omega\sqrt{LC}, \quad Z = \frac{1}{j\omega C} = -jZ_0 \cot\theta}$$

$$\boxed{\text{Series capacitor: } C \rightarrow \text{ Short-circuited stub of length } \theta = \omega\sqrt{LC}, \quad Z = \frac{1}{j\omega C} = -jZ_0 \cot\theta}$$

$$\boxed{\text{Shunt inductor: } L \rightarrow \text{ Open-circuited stub of length } \theta = \omega\sqrt{LC}, \quad Z = j\omega L = jZ_0 \tan\theta}$$

This transformation is central in establishing a link between lumped capacitive and inductive elements and distributed transmission line theory.

此变换是建立集总电容/电感元件与分布式传输线理论之间联系的核心。

### 5.6.2 Kuroda's Identities | Kuroda恒等式

Kuroda's identities enable the physical conversion of series stubs to shunt stubs (and vice versa) using **unit elements** ($Z_0$, electrical length $\theta = \pi/8$ or $\lambda/8$ at $\omega_0$). These identities help overcome impractical impedance ratios and enable realizable microstrip implementations.

Kuroda恒等式使用**单元元件**（$Z_0$，电长度 $\theta = \pi/8$ 或 $\lambda/8$）实现串联短截线与并联短截线的物理互换。这些恒等式有助于克服不切实际的阻抗比，实现可实现的微带实现。

**Kuroda's Identity (1):**

$$jZ_0 \tan\theta \parallel (jZ_1) \rightarrow jZ_0 \tan\theta + jZ_1 \quad \text{(parallel to series conversion)}$$

**Kuroda's Identity (2) — Unit Element Insertion:**

Inserting a unit element of impedance $Z_0$ at either end of the filter changes the impedance levels through the transformation:
在滤波器任一端插入阻抗 $Z_0$ 的单元元件，通过以下变换改变阻抗电平：

$$Z_{\text{new}} = Z_0^2 / Z_{\text{old}}$$

This allows high-impedance lines to be converted to physically realizable low-impedance lines.

这允许将高阻抗线转换为物理上可实现的低阻抗线。

### 5.6.3 Filter Implementation | 滤波器实现

**Design Steps for a Microstrip Low-Pass Filter:**

1. **Select** normalized filter parameters ($N$, ripple, cut-off) from tables.
2. **Replace** inductances and capacitances by equivalent $\lambda/8$ transmission lines at $\omega_0$.
3. **Apply** Kuroda's identities to convert series stubs to shunt stubs where necessary.
4. **De-normalize** impedance levels using the system $Z_0$ (typically $50\ \Omega$).
5. **Compute** physical microstrip dimensions from the de-normalized line impedances using the substrate parameters ($\epsilon_r$, $h$).

---

## 5.7 Coupled Lines and Bandpass Filters | 耦合线与带通滤波器

### Coupled Line Theory | 耦合线理论

Two parallel transmission lines with electromagnetic coupling can be characterized by even-mode and odd-mode characteristic impedances $Z_{0e}$ and $Z_{0o}$.

具有电磁耦合的两条平行传输线可以用偶模特性阻抗 $Z_{0e}$ 和奇模特性阻抗 $Z_{0o}$ 表征。

For two coupled lines of length $l$ and characteristic impedance $Z_0$, the even and odd mode impedances are:
对于长度为 $l$、特性阻抗为 $Z_0$ 的两条耦合线，偶模和奇模阻抗为：

$$Z_{0e} = Z_0 \frac{1 + |\Gamma_e|}{1 - |\Gamma_e|}, \quad Z_{0o} = Z_0 \frac{1 - |\Gamma_e|}{1 + |\Gamma_e|}$$

where $|\Gamma_e|$ is the even-mode coupling coefficient.

其中 $|\Gamma_e|$ 是偶模耦合系数。

The **coupling coefficient** $k$ is:
**耦合系数** $k$ 为：

$$k = \frac{Z_{0e} - Z_{0o}}{Z_{0e} + Z_{0o}}$$

### Bandpass Filter from Coupled Lines | 耦合线构成的带通滤波器

The bandpass filter is constructed as a cascade of coupled line sections. Each section acts as a **resonator** with input impedance:
带通滤波器由耦合线段级联构成。每段充当具有输入阻抗的**谐振器**：

$$Z_{\text{in}} = Z_0 \frac{Z_L + jZ_0\tan(\beta l)}{Z_0 + jZ_L\tan(\beta l)}$$

At resonance ($\beta l = \pi/2$, i.e., $l = \lambda/4$), the input impedance simplifies, and the cascade exhibits bandpass behavior.

在谐振时（$\beta l = \pi/2$，即 $l = \lambda/4$），输入阻抗简化，级联呈现带通特性。

The **image impedance** of a coupled line section at the center frequency $\omega_0$ determines the inter-stage matching:
耦合线段在中心频率 $\omega_0$ 处的**图像阻抗**决定级间匹配：

$$Z_{\pi} = \sqrt{\frac{A_{11}A_{12}}{A_{21}A_{22}}}, \quad Z_{0} = \sqrt{\frac{A_{22}A_{12}}{A_{21}A_{11}}}$$

The design procedure for a $N$-section coupled-line bandpass filter:
$N$ 段耦合线带通滤波器的设计步骤：

1. Determine the coupling coefficients $k_1, k_2, \ldots, k_{N+1}$ from filter tables (Butterworth or Chebyshev).
2. Compute the even and odd mode impedances: $Z_{0e,i} = Z_0 \sqrt{\frac{1+k_i}{1-k_i}}$, $Z_{0o,i} = Z_0 \sqrt{\frac{1-k_i}{1+k_i}}$.
3. Convert $Z_{0e}, Z_{0o}$ to physical dimensions using coupled-line formulas for the given substrate.

---

## 📖 Example 5-1: Bandpass Filter Response | 例5-1：带通滤波器响应

**Problem / 问题：**
For a bandpass filter with $Z_L = Z_G = 50\ \Omega$, the following components are selected: $R = 20\ \Omega$, $L = 5\ \text{nH}$, $C = 2\ \text{pF}$. Find the resonance frequency and plot the frequency response of the transfer function magnitude and phase.

对于带通滤波器，$Z_L = Z_G = 50\ \Omega$，选用元件：$R = 20\ \Omega$，$L = 5\ \text{nH}$，$C = 2\ \text{pF}$。求谐振频率，并绘制传递函数幅频和相频响应。

**Solution / 解：**

Resonance angular frequency:
谐振角频率：

$$\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{5 \times 10^{-9} \times 2 \times 10^{-12}}} = 10^{10}\ \text{rad/s}$$

$$f_0 = \frac{\omega_0}{2\pi} = \frac{10^{10}}{2\pi} \approx 1.59\ \text{GHz}$$

The series RLC transfer function is:
串联RLC传递函数为：

$$H(j\omega) = \frac{R}{R + j(\omega L - 1/\omega C) + Z_G}$$

At resonance, the imaginary part cancels:
在谐振时，虚部抵消：

$$|H(j\omega_0)| = \frac{R}{R + Z_G} = \frac{20}{20 + 50} = 0.286 \approx -10.9\ \text{dB}$$

```python
import numpy as np
import matplotlib.pyplot as plt

R = 20        # Ω
L = 5e-9      # H
C = 2e-12     # F
Z_G = 50      # Ω
omega_0 = 1 / np.sqrt(L * C)
f_0 = omega_0 / (2 * np.pi)

f = np.linspace(0.5e9, 2.5e9, 1000)
omega = 2 * np.pi * f
Z_L = R + 1j * (omega * L - 1 / (omega * C))
H = Z_L / (Z_L + Z_G)
mag_H = np.abs(H)
phase_H = np.angle(H, deg=True)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
ax1.plot(f/1e9, 20*np.log10(mag_H), 'b-', linewidth=2)
ax1.axvline(f_0/1e9, color='r', linestyle='--', label=f'$f_0$ = {f_0/1e9:.2f} GHz')
ax1.set_xlabel('Frequency (GHz)')
ax1.set_ylabel('|H(j\omega)| (dB)')
ax1.set_title('Bandpass Filter Magnitude Response')
ax1.legend()
ax1.grid(True)

ax2.plot(f/1e9, phase_H, 'g-', linewidth=2)
ax2.axvline(f_0/1e9, color='r', linestyle='--', label=f'$f_0$ = {f_0/1e9:.2f} GHz')
ax2.set_xlabel('Frequency (GHz)')
ax2.set_ylabel('Phase (degrees)')
ax2.set_title('Bandpass Filter Phase Response')
ax2.legend()
ax2.grid(True)
plt.tight_layout()
plt.savefig('/tmp/bandpass_response.png', dpi=150)
plt.close()
print(f" Resonance frequency: f_0 = {f_0/1e9:.3f} GHz")
```

---

## 5.8 Summary | 本章小结

| Topic 主题 | Key Result 关键结论 |
|---|---|
| Filter types 滤波器类型 | LP, HP, BP, BS — each characterized by cut-off $\omega_c$ and bandwidth 截止频率和带宽 |
| Loaded Q 有载Q | $Q_L = \omega_0 L/(R+R_G+R_L)$ — determines bandwidth and selectivity 决定带宽和选择性 |
| Butterworth response | Maximally flat in passband, monotonic roll-off, $-3\text{ dB}$ at $\omega_c$ |
| Chebyshev response | Equal-ripple passband, steeper roll-off than Butterworth for same $N$ |
| LP → HP transformation | $\Omega_{\text{LP}} = 1/\Omega_{\text{HP}}$, $L_{\text{HP}} = 1/(\omega_c^2 C_{\text{LP}})$ |
| LP → BP transformation | $\Omega = (\omega_0/\Delta\omega)(\omega/\omega_0 - \omega_0/\omega)$ |
| Richards' transformation | $L \rightarrow \lambda/8$ open stub; $C \rightarrow \lambda/8$ short stub |
| Kuroda's identities | Enable series↔shunt stub conversion via unit elements; change impedance levels |
| Coupled-line BPF | $Z_{0e}$, $Z_{0o}$ determine coupling; $k = (Z_{0e}-Z_{0o})/(Z_{0e}+Z_{0o})$ |

---

## Further Reading | 深入阅读

- Pozar, D. M., *Microwave Engineering*, Ch. 8 — Filter Design
- Rizzi, P. A., *Microwave Engineering: Passive Circuits*
- Matthaei, G., Young, L., Jones, E. M. T., *Microwave Filters, Impedance-Matching Networks, and Coupling Structures*
