---
chapter: 4
title: Single- and Multiport Networks
source: Ludwig & Bogdanov, RF Circuit Design, 2nd Edition
pages: 157-215
---

# Chapter 4: Single- and Multiport Networks | 第4章：单端口与多端口网络

## Introduction | 引言

> **Original:** The ability to reduce a complicated circuit into simpler constituents whose input-output is described through two-port network description is a critical skill in RF circuit design.

**【中文注释】** 在射频电路设计中，我们经常需要将一个复杂的电路分解为多个简单的二端口网络，并研究它们之间的互联。S参数（散射参数）是描述射频网络最常用的方式，因为它直接与测量（而非计算）的电压和电流相关，且在高频下具有明确的物理意义。

---

## 4.1 Basic Definitions | 基本定义

### 4.1.1 Impedance Matrix (Z-Matrix) | 阻抗矩阵

For an N-port network, the impedance matrix relates port voltages to port currents:

$$\begin{bmatrix} V_1 \\ V_2 \\ \vdots \\ V_N \end{bmatrix} = \begin{bmatrix} Z_{11} & Z_{12} & \cdots & Z_{1N} \\ Z_{21} & Z_{22} & \cdots & Z_{2N} \\ \vdots & \vdots & \ddots & \vdots \\ Z_{N1} & Z_{N2} & \cdots & Z_{NN} \end{bmatrix} \begin{bmatrix} I_1 \\ I_2 \\ \vdots \\ I_N \end{bmatrix}$$

Each $Z_{ij}$ is determined by short-circuiting all ports except port $j$, then measuring the current at port $i$ when voltage is applied to port $j$:

$$Z_{ij} = \left.\frac{V_i}{I_j}\right|_{I_k=0, k\neq j}$$

**Properties for passive networks:**
- **Symmetry:** $Z_{ij} = Z_{ji}$ (for reciprocal networks, $Z^T = Z$)
- **Reciprocity:** A network is reciprocal if interchanging source and measurement ports gives the same response

**【中文注释】** 阻抗矩阵（Z矩阵）是描述N端口网络的一种方式。每个元素$Z_{ij}$表示当其他所有端口都短路时，端口$j$的电流与端口$i$的电压之比。对于无源互易网络，Z矩阵是对称的（$Z_{ij} = Z_{ji}$）。

---

### 4.1.2 Admittance Matrix (Y-Matrix) | 导纳矩阵

The admittance matrix relates port currents to port voltages:

$$I_i = \sum_j Y_{ij} V_j, \quad \text{or} \quad [I] = [Y][V]$$

$$Y_{ij} = \left.\frac{I_i}{V_j}\right|_{V_k=0, k\neq j}$$

**Relationship:** $[Y] = [Z]^{-1}$ (when the network is not singular).

For a two-port network:

$$Y_{11} = \frac{I_1}{V_1}\bigg|_{V_2=0} \quad \text{(input admittance with output shorted)}$$

$$Y_{12} = \frac{I_1}{V_2}\bigg|_{V_1=0} \quad \text{(reverse transfer admittance)}$$

**【中文注释】** 导纳矩阵（Y矩阵）是阻抗矩阵的逆矩阵。确定$Y_{ij}$时，需要将除了端口$j$之外的所有端口开路，然后测量端口$i$的电流与端口$j$的电压之比。

---

### Example 4-1: Z and Y Parameters | 例4-1：Z参数与Y参数

For a simple T-network (two series resistors $R_1$, $R_3$ and one shunt resistor $R_2$ between ports 1 and 2):

$$Z_{11} = R_1 + R_2, \quad Z_{12} = Z_{21} = R_2, \quad Z_{22} = R_2 + R_3$$

The Y-matrix (inverse) would be symmetric as well, confirming reciprocity.

**【中文注释】** 这个例子展示了最简单的T型网络（一端口串联电阻$R_1$，中间节点接地电阻$R_2$，二端口串联电阻$R_3$）。由于网络是无源的且互易，Z矩阵和Y矩阵都是对称的。

---

### 4.1.3 Chain (ABCD) Matrix | 级联（ABCD）矩阵

The ABCD matrix is designed for **cascading two-port networks**:

$$\begin{bmatrix} V_1 \\ I_1 \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} V_2 \\ I_2 \end{bmatrix}$$

**Determination:**
- $A = V_1/V_2\big|_{I_2=0}$ — voltage gain with output open
- $B = V_1/(-I_2)\big|_{V_2=0}$ — transfer impedance with output shorted
- $C = I_1/V_2\big|_{I_2=0}$ — transfer admittance with output open
- $D = I_1/(-I_2)\big|_{V_2=0}$ — current gain with output shorted

**Cascade property:** $[ABCD]_{\text{total}} = [ABCD]_1 \cdot [ABCD]_2 \cdot \cdots$

**For a symmetric (reciprocal) network:** $AD - BC = 1$.

**【中文注释】** ABCD矩阵特别适合描述级联的二端口网络，比如多个传输线段或滤波器的级联。它的级联特性（矩阵乘法）使得多个网络的总体ABCD矩阵可以简单地通过各个子矩阵相乘得到。

---

### 4.1.4 Hybrid (h) Matrix | 混合参数（h）矩阵

The hybrid matrix uses a mix of voltage and current variables:

$$\begin{bmatrix} V_1 \\ I_2 \end{bmatrix} = \begin{bmatrix} h_{11} & h_{12} \\ h_{21} & h_{22} \end{bmatrix} \begin{bmatrix} I_1 \\ V_2 \end{bmatrix}$$

**Why "hybrid":** Mixes impedance-like ($h_{11}$) and admittance-like ($h_{22}$) parameters with transfer parameters ($h_{12}, h_{21}$).

**Physical meaning of h-parameters for a BJT (common-emitter):**
- $h_{11} = h_{ie}$: input resistance (with output shorted)
- $h_{12} = h_{re}$: reverse voltage gain (with input open) — usually very small ($\sim 10^{-4}$)
- $h_{21} = h_{fe}$: forward current gain $\beta$ (with output shorted)
- $h_{22} = h_{oe}$: output admittance (with input open)

**【中文注释】** h矩阵（混合参数）特别适合描述晶体管，因为在低频下晶体管的小信号模型本身就包含电压控制电流源（VCCS）。h参数通常可以直接从晶体管数据手册中获得，这也是h矩阵在电路设计中广泛使用的原因。

---

### Example 4-2: BJT Low-Frequency h-Parameters | 例4-2：晶体管低频h参数

For the common-emitter BJT model with $r_{BE}$, $r_{BC}$, $r_{CE}$, and current gain $\beta$:

$$h_{ie} = r_{BE} \| r_{BC} \quad \text{(input impedance)}$$

$$h_{re} = \frac{r_{BC}}{r_{BE} + r_{BC}} \quad \text{(voltage feedback ratio)}$$

$$h_{fe} = \beta \cdot \frac{r_{BC}}{r_{BE} + r_{BC}} \approx \beta \quad \text{(current gain)}$$

$$h_{oe} = \frac{1}{r_{CE}} + \frac{1}{r_{BE}+r_{BC}} \quad \text{(output admittance)}$$

For typical BJTs with $\beta \gg 1$ and $r_{BC} \gg r_{BE}$:
$$h_{ie} \approx r_{BE}, \quad h_{re} \approx 0, \quad h_{fe} \approx \beta, \quad h_{oe} \approx 1/r_{CE}$$

**【中文注释】** 这个例子展示了如何从等效电路模型推导出h参数。在实际应用中，$h_{re}$通常很小（$10^{-4}$量级）可以忽略，$h_{fe}$就是大家熟知的$\beta$（电流放大系数），$h_{oe}$主要由$r_{CE}$决定。这些参数在晶体管数据手册中可以直接查到。

---

### Example 4-3: Extracting BJT Internal Resistances from h-Parameters | 例3-3：从h参数提取BJT内部电阻

**Given measured h-parameters for 2N3904:**
$h_{ie} = 5$ k$\Omega$, $h_{re} = 2 \times 10^{-4}$, $h_{fe} = 250$, $h_{oe} = 20\,\mu$S

**Solution:**

$$r_{BC} = \frac{h_{ie}}{h_{re}} = \frac{5\text{k}\Omega}{2 \times 10^{-4}} = 25\text{M}\Omega$$

$$r_{BE} = \frac{h_{ie}}{1 - h_{re}} \approx 5.001\text{k}\Omega \approx 5\text{k}\Omega$$

$$\beta = h_{fe} \cdot \frac{r_{BE}+r_{BC}}{r_{BC}} \approx 250 \cdot \frac{25.005}{25} \approx 250$$

$$r_{CE} = \frac{1}{h_{oe} - \frac{1}{r_{BE}+r_{BC}}} \approx 63.35\text{k}\Omega$$

**Key observation:** $r_{BC} \gg r_{BE}$ confirms the approximation $h_{ie} \approx r_{BE}$.

**【中文注释】** 这个例子展示了如何"反演"测量得到的h参数来得到晶体管内部电阻的真实值。这种"逆问题"的求解在器件建模中非常重要——我们通过测量得到外部参数（h参数），然后推导出内部等效电路的参数值。

---

## 4.2 Interconnecting Networks | 网络互联

### 4.2.1 Series Connection of Two-Port Networks | 二端口网络的串联

When two networks are **cascaded** (output of one feeds into the input of the next), the ABCD matrices multiply:

$$[ABCD]_{\text{total}} = [ABCD]_2 \cdot [ABCD]_1 \cdot \cdots$$

**Z-matrix for series connection:** $[Z]_{\text{total}} = [Z]_1 + [Z]_2$ (element-wise addition of impedance matrices).

**Y-matrix for parallel connection:** $[Y]_{\text{total}} = [Y]_1 + [Y]_2$ (element-wise addition of admittance matrices).

**【中文注释】** 网络互联时，Z矩阵和Y矩阵的组合规则取决于连接方式。串联连接时Z矩阵相加（因为阻抗串联），并联连接时Y矩阵相加（因为导纳并联）。ABCD矩阵在级联时相乘——这是处理多个传输线段或滤波器级联的标准方法。

---

## 4.3 Scattering Parameters (S-Parameters) | 散射参数

### Why S-Parameters at RF? | 为什么在射频使用S参数？

At RF frequencies:
- **Open/short circuits are difficult to achieve** — stray reactances dominate
- **Z and Y parameters require** dangerous open/short conditions
- **S-parameters use** $50\,\Omega$ terminations — easily achievable with precision resistors
- **S-parameters are directly measurable** with a Network Analyzer
- **S-parameters are frequency-domain** by nature — ideal for RF analysis

**【中文注释】** 在高频下，实现真正的开路或短路条件非常困难——连接线的寄生电感、电容会严重影响测量。而S参数使用50 Ω终端，这是一种容易实现的精确电阻条件。矢量网络分析仪（VNA）可以精确测量S参数，这使得S参数成为描述射频网络的事实标准。

---

### S-Parameter Definition | S参数定义

For a two-port network with characteristic impedance $Z_0$ (typically $50\,\Omega$):

$$b_1 = S_{11} a_1 + S_{12} a_2 \tag{4.19a}$$

$$b_2 = S_{21} a_1 + S_{22} a_2 \tag{4.19b}$$

where:
- $a_n = V_n^+/\sqrt{Z_0}$ — normalized incident wave at port $n$
- $b_n = V_n^-/\sqrt{Z_0}$ — normalized reflected wave at port $n$

In matrix form: $[b] = [S][a]$

**Physical meaning of each S-parameter:**

| Parameter | Definition | Physical Meaning |
|-----------|-----------|------------------|
| $S_{11}$ | $b_1/a_1$ (with $a_2 = 0$, i.e., port 2 matched) | Input reflection coefficient / input return loss |
| $S_{21}$ | $b_2/a_1$ (with $a_2 = 0$) | Forward transmission (gain or loss) |
| $S_{12}$ | $b_1/a_2$ (with $a_1 = 0$) | Reverse isolation |
| $S_{22}$ | $b_2/a_2$ (with $a_1 = 0$) | Output reflection coefficient / output return loss |

**【中文注释】** S参数直接描述了射频网络端口上的波的行为。$S_{11}$是输入反射系数（当输出端口匹配时），$S_{21}$是正向传输系数（信号从端口1到端口2的增益或损耗），$S_{12}$是反向隔离度（端口2到端口1的隔离），$S_{22}$是输出反射系数。

---

### Determining S-Parameters | S参数的确定

$$S_{11} = \left.\frac{b_1}{a_1}\right|_{a_2=0} = \Gamma_{\text{in}} \quad \text{(input reflection coefficient with port 2 matched)}$$

$$S_{21} = \left.\frac{b_2}{a_1}\right|_{a_2=0} \quad \text{(forward gain, with port 2 matched)}$$

$$S_{22} = \left.\frac{b_2}{a_2}\right|_{a_1=0} = \Gamma_{\text{out}} \quad \text{(output reflection coefficient with port 1 matched)}$$

$$S_{12} = \left.\frac{b_1}{a_2}\right|_{a_1=0} \quad \text{(reverse gain, with port 1 matched)}$$

**Key insight:** $S_{11}$ and $S_{22}$ are reflection coefficients measured when the **other port is terminated in $Z_0$** (not open or short). This is the critical condition.

**【中文注释】** 确定S参数时，关键是确保另一个端口是匹配（$Z_0$）端接，而不是开路或短路。当端口2匹配端接时，$a_2 = 0$，此时$b_1/a_1 = S_{11}$就是输入反射系数。类似地，当端口1匹配时，$b_2/a_2 = S_{22}$是输出反射系数。

---

### S-Parameter Properties for Passive Networks | 无源网络的S参数特性

**Reciprocal network** ($S_{ij} = S_{ji}$): $[S]$ is symmetric.

**Passive network** ($|S_{ij}| \leq 1$ for all $i,j$): All singular values $\leq 1$.

**Lossless network** ($[S]^H[S] = [I]$): The S-matrix is unitary. This implies:
- $|S_{11}|^2 + |S_{21}|^2 = 1$ (power conservation at port 1)
- $|S_{22}|^2 + |S_{12}|^2 = 1$ (power conservation at port 2)

**【中文注释】** 无耗网络的S矩阵是酉矩阵（unitary），即$[S][S]^H = [I]$。这保证了功率守恒——入射功率等于反射功率加透射功率之和。对于无耗二端口网络，有$|S_{11}|^2 + |S_{21}|^2 = 1$。

---

### Transmission (T) Parameters | 传输（T）参数

The **T-matrix** relates incident and reflected waves in a common reference frame:

$$\begin{bmatrix} a_1 \\ b_1 \end{bmatrix} = [T] \begin{bmatrix} b_2 \\ a_2 \end{bmatrix}$$

This is useful for cascading S-parameter blocks, since: $[T]_{\text{total}} = [T]_1 \cdot [T]_2$.

However, T-parameters are less commonly used than ABCD matrices for cascade analysis.

**【中文注释】** T参数与ABCD矩阵类似，但使用的是波而不是电压/电流。在级联分析中很有用。不过在大多数射频CAD工具中，ABCD矩阵是更常见的级联表示方式。

---

### Converting Between Parameter Sets | 参数集之间的转换

Common conversions:
- $[Z] \to [S]$: $S_{ij} = \frac{2Z_{ij}\sqrt{\text{Re}(Z_0)}}{Z_{ij} + Z_0^*}$
- $[S] \to [Z]$: $Z_{ij} = Z_0 \frac{(1+S_{ij})(1-S_{jj}^*) - S_{ij}S_{ji}^*}{(1-S_{ii})(1-S_{jj}^*) - S_{ij}S_{ji}^*}$

**For a 2-port network, simpler formulas exist** — see textbook Table 4-1.

**【中文注释】** 在实际工程中，我们经常需要在不同的网络参数集之间转换。例如，我们可能测量得到S参数，但需要转换为Z参数来进行电路分析。现代RF CAD软件（如ADS、HFSS）会自动处理这些转换。

---

## 4.4 Signal Flow Graphs | 信号流图

Signal flow graphs (SFG) provide a graphical method for analyzing complex RF networks without writing matrix equations.

### Basic SFG Elements | 基本信号流图元素

| SFG Element | Meaning |
|-------------|---------|
| Node | Variable (wave amplitude, voltage) |
| Branch (arrow) | Transmission coefficient (S, T, etc.) |
| Input node | Source |
| Output node | Measurement point |

**Mason's Rule** provides a systematic method for finding the transfer function between any two nodes in an SFG.

**【中文注释】** 信号流图是一种图形化的网络分析方法，特别适合分析包含多个反射和透射路径的复杂系统。梅森公式（Mason's Rule）提供了一种系统化的方法来计算任意两个节点之间的传递函数。

---

## 4.5 High-Frequency S-Parameter Measurement | 高频S参数测量

### Measurement Setup | 测量设置

A **Vector Network Analyzer (VNA)** measures S-parameters by:
1. Injecting a known swept-frequency signal into the DUT (Device Under Test)
2. Measuring the reflected and transmitted waves at each port
3. Computing the complex $S_{ij}$ values

**Calibration standards:** SOLT (Short-Open-Load-Through) or TRL (Through-Reflect-Line) are used to remove systematic errors (connector repeatability, cable losses, fixture effects).

**Key VNA specifications:**
- **Dynamic range:** Typically 80–120 dB (determines ability to measure low $S_{12}$, high isolation)
- **Noise floor:** Sets the minimum measurable $S_{ij}$ magnitude
- **Accuracy:** Directivity, source match, reflection tracking

**【中文注释】** 矢量网络分析仪（VNA）是射频工程师最重要的测量仪器。它通过在宽频带上扫频，测量DUT的S参数。校准是确保测量精度的关键步骤——SOLT校准是最常用的方法，它使用短路、开路、负载和直通四个标准件来建立误差模型。

---

## 4.6 One-Port Network Applications | 单端口网络应用

### Input Impedance of a One-Port | 单端口输入阻抗

For a one-port (device with single connection point, e.g., antenna):

$$Z_{\text{in}} = Z_0 \frac{1 + \Gamma}{1 - \Gamma}$$

where $\Gamma = S_{11}$ (measured with port 2 terminated in $Z_0$, but for one-port, $S_{11}$ is directly measured).

**Application: Antenna impedance measurement** — $S_{11}$ directly gives the antenna's input reflection coefficient and return loss.

**【中文注释】** 单端口网络的S参数只有一个——$S_{11}$，它就是输入反射系数。从$S_{11}$可以直接计算输入阻抗和回波损耗。天线阻抗测量就是典型的单端口S参数应用。

---

## 4.7 Multiport Extensions | 多端口扩展

### Three-Port Networks | 三端口网络

For a 3-port network (e.g., a circulator or coupler):

$$[b] = [S][a] \quad \text{where } [S] \text{ is } 3 \times 3$$

A **non-reciprocal** 3-port device (circulator) has an asymmetric S-matrix:

$$[S] = \begin{bmatrix} 0 & 0 & S_{13} \\ S_{21} & 0 & 0 \\ 0 & S_{32} & 0 \end{bmatrix} \quad \text{(example circulator)}$$

A circulator routes signals from port to port in one direction only — critical for separating transmit and receive paths in RF front-ends.

**【中文注释】** 三端口网络在射频系统中有重要应用。环形器（circulator）是一种典型的非互易器件，它只能让信号沿一个方向循环传递（端口1→端口2→端口3→端口1）。这在射频前端的T/R（发射/接收）开关设计中非常重要。

---

### Four-Port Networks: Directional Couplers | 四端口网络：定向耦合器

A **directional coupler** has 4 ports: input (1), through (2), coupled (3), isolated (4).

理想定向耦合器的S矩阵：

$$[S] = \begin{bmatrix} 0 & \sqrt{1-k^2} & jk & 0 \\ \sqrt{1-k^2} & 0 & 0 & jk \\ jk & 0 & 0 & \sqrt{1-k^2} \\ 0 & jk & \sqrt{1-k^2} & 0 \end{bmatrix}$$

其中 $k$ 是耦合系数（coupling factor）。

**Key specifications:**
- **Coupling factor:** $C = -20\log_{10}|S_{31}|$ dB (how much power is coupled out)
- **Directivity:** $D = -20\log_{10}|S_{41}/S_{31}|$ dB (isolation between coupled and isolated ports)
- **Insertion loss:** $\text{IL} = -20\log_{10}|S_{21}|$ dB (through-path loss)

**【中文注释】** 定向耦合器是射频系统中的关键无源器件。它从主传输线中耦合出一部分信号（用于监测、采样或反馈），同时让大部分信号直接通过。耦合系数（dB）和方向性（dB）是两个关键规格——耦合系数描述有多少功率被耦合出来，方向性描述耦合端口与隔离端口之间的隔离度。

---

## Summary | 本章小结

### Key Concepts | 核心概念

1. **Z-matrix** relates voltages to currents; determined with all other ports shorted
2. **Y-matrix** relates currents to voltages; determined with all other ports open
3. **ABCD matrix** is designed for cascading networks (matrix multiplication)
4. **h-matrix** is popular for transistor models (directly available from datasheets)
5. **S-parameters** are the standard at RF — measured with matched ($Z_0$) terminations
6. **$S_{11}$** = input reflection coefficient; **$S_{21}$** = forward gain; **$S_{12}$** = reverse isolation; **$S_{22}$** = output reflection coefficient
7. **Signal flow graphs** provide graphical analysis of complex networks
8. **VNA calibration** (SOLT/TRL) is essential for accurate S-parameter measurements
9. **Circulators** and **directional couplers** are key multiport RF components

### Key Equations | 核心公式

$$\boxed{[V] = [Z][I], \quad [I] = [Y][V], \quad [Y] = [Z]^{-1}}$$

$$\boxed{\begin{bmatrix} V_1 \\ I_1 \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} V_2 \\ I_2 \end{bmatrix}}$$

$$\boxed{[b] = [S][a], \quad S_{ij} = \left.\frac{b_i}{a_j}\right|_{a_k=0, k\neq j}}$$

$$\boxed{S_{11} = \Gamma_{\text{in}} \big|_{Z_L = Z_0}, \quad S_{21} = \frac{V_2}{V_1}\bigg|_{Z_L = Z_0}}$$

$$\boxed{|S_{11}|^2 + |S_{21}|^2 = 1 \quad \text{(lossless network power conservation)}}$$

**【中文注释】** 本章建立了射频网络分析的理论基础：Z矩阵、Y矩阵、ABCD矩阵、h矩阵和S参数是描述同一网络在不同条件下的五种等价表示。在射频工程中，S参数是绝对的标准——几乎所有测量和CAD工具都使用S参数。理解如何从测量得到S参数，以及如何在需要时转换为其他参数集，是射频工程师的核心技能。