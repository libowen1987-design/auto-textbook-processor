---
chapter: 8
title: Microwave Networks
source: Roger F. Harrington, Time-Harmonic Electromagnetic Fields, IEEE Press
pages: 501-600
---

# Chapter 8: Microwave Networks / 微波网络

## Section 8-1: Network Theorems / 网络定理

**English:**

**Microwave networks** are an extension of low-frequency circuit theory to waveguide and transmission-line systems at microwave frequencies.

**Multi-conductor systems** support multiple propagating modes. Each mode at each frequency is a "transmission line channel."

**Network parameters:**

| Parameter | Definition | Used for |
|-----------|-----------|----------|
| **Z-parameters** (impedance) | $V_n = \sum_m Z_{nm} I_m$ | Open-circuit conditions |
| **Y-parameters** (admittance) | $I_n = \sum_m Y_{nm} V_m$ | Short-circuit conditions |
| **S-parameters** (scattering) | $b_n = \sum_m S_{nm} a_m$ | Traveling waves, matched systems |
| **T-parameters** (transfer) | Relates waves at two ports | Cascade analysis |

**S-parameters** are most commonly used in microwave engineering:

$$b_1 = S_{11}a_1 + S_{12}a_2$$
$$b_2 = S_{21}a_1 + S_{22}a_2$$

or in matrix form: $[b] = [S][a]$

where $a_n$ is the normalized incident wave and $b_n$ is the normalized reflected wave.

**Normalization:**
$$a_n = \frac{V_n^+}{\sqrt{Z_0}} \quad b_n = \frac{V_n^-}{\sqrt{Z_0}}$$

so that $|a_n|^2$ and $|b_n|^2$ represent power.

**S-parameter properties:**

- **Symmetry** for reciprocal networks: $[S]^T = [S]$, so $S_{ij} = S_{ji}$
- **Unitarity** for lossless networks: $[S][S]^* = [I]$, so $\sum_k S_{ik}S_{jk}^* = \delta_{ij}$
- **Lossless**: $|S_{11}|^2 + |S_{21}|^2 = 1$ for 2-port

**Power relationships:**
$$P_\text{incident} = \sum_n |a_n|^2$$
$$P_\text{reflected} = \sum_n |b_n|^2$$
$$P_\text{absorbed} = \sum_n (|a_n|^2 - |b_n|^2)$$

**中文：**

**微波网络**是将低频电路理论扩展到微波频率的波导和传输线系统。

**网络参数：**

| 参数 | 定义 | 用途 |
|------|------|------|
| **Z参数**（阻抗） | $V_n = \sum_m Z_{nm} I_m$ | 开路条件 |
| **Y参数**（导纳） | $I_n = \sum_m Y_{nm} V_m$ | 短路条件 |
| **S参数**（散射） | $b_n = \sum_m S_{nm} a_m$ | 行波、匹配系统 |
| **T参数**（转移） | 关联两端口处的波 | 级联分析 |

**S参数**在微波工程中最常用：

$$[b] = [S][a]$$

**性质：**
- 互易网络：**对称性** $[S]^T = [S]$
- 无耗网络：**酉性** $[S][S]^* = [I]$

---

## Section 8-2: Waveguide Junctions / 波导接头

**English:**

**Waveguide junctions** are discontinuities where modes convert between different waveguide sections or to other transmission structures.

**Two-port junction:** Waveguide of cross-section $A$ connected to waveguide of cross-section $B$.

**Mode matching:** Expand fields in each guide in terms of modal functions. Match tangential fields at the junction. This gives infinite matrix, truncated for numerical solution.

**Discontinuity capacitance:** For E-plane step in rectangular waveguide.

**H-plane iris:** Reactive obstacle with inductive characteristic.

**E-plane iris:** Reactive obstacle with capacitive characteristic.

**Resonant iris:** Series R-L-C at resonance.

**Equivalent circuit models:**

| Discontinuity | Equivalent Circuit |
|---------------|------------------|
| H-plane step | shunt inductor |
| E-plane step | series capacitor |
| Thin inductive post | shunt inductor |
| Thin capacitive post | series capacitor |
| Iris (symmetric) | parallel resonant circuit |

**Multi-port junctions:** $N$-port junction described by $N \times N$ S-matrix.

For $N$-port with all ports matched: $[S]$ has $S_{ii} = 0$.

**T-junction:** 3-port. Can be characterized by E-plane (series) or H-plane (shunt) configuration.

**Cross junction:** 4-port. Used in magic-T and hybrid coupling.

**Magic-T (hybrid tee):** 4-port with special properties:
- $S_{12} = S_{34} = 0$ (ports 1 and 2 are isolated)
- $S_{14} = S_{23} = 1/\sqrt{2}$ (E-arm to H-arm coupling)

**中文：**

**波导接头**是模式在不同波导段之间或与其他传输结构之间转换的不连续性。

**模式匹配：** 将每个波导中的场展开为模函数。在接头处匹配切向场。

**等效电路模型：**

| 不连续性 | 等效电路 |
|---------|---------|
| H面阶梯 | 并联电感 |
| E面阶梯 | 串联电容 |
| 感性膜片 | 并联电感 |
| 容性膜片 | 串联电容 |

---

## Section 8-3: Apertures and Irises / 孔径与膜片

**English:**

**Apertures** and **irises** in waveguides create reactive discontinuities.

**Thin iris (window):** Conductive diaphragm across waveguide aperture.

**Inductive iris (H-plane):** Iris with opening in narrow dimension. Equivalent to shunt inductance.

$$X_L \approx -\frac{\omega\mu a}{2\pi}\ln\left(\sin\frac{\pi d}{a}\right) \quad \text{(for narrow iris)}$$

where $d$ is the iris opening.

**Capacitive iris (E-plane):** Iris with opening in wide dimension. Equivalent to shunt capacitance.

$$X_C \approx \frac{\lambda_g}{2\pi b}\ln\left(\csc\frac{\pi d}{b}\right) \quad \text{(for narrow iris)}$$

**Symmetric iris:** Both broad walls present, opening in center. Equivalent to parallel resonant circuit.

**Resonant iris:** At certain dimensions, iris becomes resonant (match condition $X = 0$). Used for matching and filter的设计.

**Narrow coupling aperture:** Used to couple two waveguides. Equivalent to series transformer.

**Cross-coupling iris:** Creates coupling between non-adjacent cavities in filter structures.

**Filter design:** Iris-coupled waveguide filters use cascaded irises to create band-pass response.

**中文：**

波导中的**孔径**和**膜片**产生电抗性不连续性。

**感性膜片（H面）：** 在窄边有开口。等效为并联电感。

$$X_L \approx -\frac{\omega\mu a}{2\pi}\ln\left(\sin\frac{\pi d}{a}\right)$$

**容性膜片（E面）：** 在宽边有开口。等效为串联电容。

$$X_C \approx \frac{\lambda_g}{2\pi b}\ln\left(\csc\frac{\pi d}{b}\right)$$

**谐振膜片：** 在特定尺寸下，膜片变得谐振（匹配条件 $X = 0$）。

---

## Section 8-4: Coupling Slots / 耦合缝隙

**English:**

**Coupling slots** in waveguides are used for power coupling to other waveguides, antennas, or cavities.

**Radiating slot in waveguide wall:** Cuts in broad wall of rectangular waveguide.

**Broad-wall longitudinal slot:** Induces radiating current, equivalent to shunt conductance.

**Broad-wall transverse slot:** Equivalent to series resistance.

**Resonant slot:** At $L = \lambda/2$, input resistance matches waveguide characteristic impedance for maximum power transfer.

**Condition for resonance:**
$$\frac{G}{Y_0} = 2.09\left(\frac{\lambda_g}{\lambda}\right)^2 \frac{d}{a}\sin^2\frac{\pi x_0}{a}$$

where $d$ is slot width, $a$ is waveguide width, $x_0$ is slot offset from center.

**Non-radiating slots:** Slots that do not interrupt surface currents — no power coupled.

**Endfire slot array:** Series-fed array of slots on broad wall of waveguide, designed for endfire radiation pattern.

**Sidewall coupling:** Coupling to smaller waveguides or cavities through narrow wall slots.

**Slot-fed dipole:** Slot as feed for printed dipole antenna, used in microstrip array design.

**中文：**

波导中的**耦合缝隙**用于功率耦合到其他波导、天线或腔体。

**宽壁纵向缝隙：** 感应辐射电流，等效为并联电导。

**谐振缝隙：** 在 $L = \lambda/2$ 时，输入电阻与波导特性阻抗匹配以获得最大功率传输。

**谐振条件：**
$$\frac{G}{Y_0} = 2.09\left(\frac{\lambda_g}{\lambda}\right)^2 \frac{d}{a}\sin^2\frac{\pi x_0}{a}$$

其中 $d$ 是缝隙宽度，$a$ 是波导宽度，$x_0$ 是缝隙偏离中心的距离。

---

## Section 8-5: Network Analysis of Multi-port Junctions / 多端口接头的网络分析

**English:**

**Multi-port junctions** generalize the 2-port case to $N$ ports.

**General S-matrix formulation:**

For $N$-port junction, the S-matrix relates incident waves $[a]$ to reflected waves $[b]$:

$$[b] = [S][a]$$

**Properties:**
- For **lossless** junction: $[S]$ is unitary ($[S][S]^* = [I]$)
- For **reciprocal** junction: $[S]^T = [S]$ (symmetric)
- For **lossless and reciprocal**: $[S]$ is symmetric and unitary

**Port reference impedances** are arbitrary but conventionally chosen as real ($Z_0 = 50\ \Omega$ standard for microwave).

**Reference plane shift:** Moving reference plane by distance $l$ on port $n$ multiplies $S_{nm}$ by $e^{-j2\beta_n l}$ for $m = n$ (diagonal) and $e^{-j\beta_n l}$ for $m \neq n$ (off-diagonal).

**Cascade connection of 2-ports:**

Use T-parameters (ABCD-like):
$$\begin{bmatrix} b_1 \\ a_1 \end{bmatrix} = [T] \begin{bmatrix} a_2 \\ b_2 \end{bmatrix}$$

$$[T] = \begin{bmatrix} T_{11} & T_{12} \\ T_{21} & T_{22} \end{bmatrix}$$

Cascade: $[T_\text{total}] = [T_1][T_2]$

**Generalized scattering matrix (GSM):** For multi-mode, multi-port junctions with different modal impedances at each port.

**Network graph methods:** Mason's rule for signal flow graph analysis of microwave networks.

**Signal flow graph:** Nodes represent waves at ports. Branches represent S-parameters.

**Cut-set analysis:** For finding network eigenvalues and resonant conditions.

**Coupling matrix for filters:** Modern filter synthesis uses coupling matrix representation of coupled-resonator filters.

**Nonreciprocal devices** (circulators, isolators) require modified network theory since they violate reciprocity.

**中文：**

**多端口接头**将2端口情况推广到 $N$ 端口。

**一般S矩阵公式：**

对于 $N$ 端口接头，S矩阵将入射波 $[a]$ 与反射波 $[b]$ 关联：

$$[b] = [S][a]$$

**性质：**
- 对于**无耗**接头：$[S]$ 是酉矩阵 ($[S][S]^* = [I]$)
- 对于**互易**接头：$[S]^T = [S]$（对称）
- 对于**无耗且互易**：$[S]$ 是对称且酉的

**级联连接：**

使用T参数（类似于ABCD）：
$$[T_\text{total}] = [T_1][T_2]$$

**耦合矩阵用于滤波器：** 现代滤波器合成使用耦合矩阵表示耦合谐振器滤波器。

---

## Section 8-6: General Network Properties / 一般网络性质

**English:**

**Tellegen's theorem** applies to any lumped network (including microwave networks):

$$\sum_{n=1}^{N} V_n I_n^* = 0$$

This is a consequence of conservation of power in any network.

**Reciprocity** in networks: For reciprocal networks, the transfer function from port $i$ to port $j$ equals that from port $j$ to port $i$.

**Lossless networks:** Power is conserved. The S-matrix is unitary:
$$\sum_{k=1}^{N} S_{ik}S_{jk}^* = \delta_{ij}$$

This implies that:
- $\sum_i |S_{ij}|^2 = 1$ (all power incident at port $j$ is reflected or transmitted)
- $\sum_j |S_{ij}|^2 = 1$ (all power incident at port $i$ is reflected or transmitted)

**Passivity:** For passive networks, the sum of absorbed powers must be non-negative:
$$\sum_{n=1}^{N} \frac{|b_n|^2 - |a_n|^2}{2} \geq 0$$

which implies that $[I] - [S]^+[S]$ is positive semi-definite.

**Stability:** A network is stable if all traveling waves decay with time. Requires eigenvalues of $[S]$ to have magnitude $\leq 1$.

**Impedance matching:** Minimize reflections at ports. Common matching networks: stub tuners, quarter-wave transformers, multisection transformers.

**Smith chart:** Graphical representation of complex reflection coefficient and impedance for transmission line calculations.

**Broadband matching:** Requires careful design of matching network to achieve wide bandwidth with low VSWR.

**Synthesis:** Given desired S-parameters, synthesize network using Darlington synthesis or other techniques.

**中文：**

**Tellegen定理**适用于任何集总网络（包括微波网络）：

$$\sum_{n=1}^{N} V_n I_n^* = 0$$

这是功率守恒的结果。

**互易性：** 互易网络中，从端口 $i$ 到端口 $j$ 的传递函数等于从端口 $j$ 到端口 $i$ 的传递函数。

**无耗网络：** 功率守恒。S矩阵是酉矩阵：
$$\sum_{k=1}^{N} S_{ik}S_{jk}^* = \delta_{ij}$$

**被动性：** 对于被动网络，吸收功率之和必须非负：
$$\sum_{n=1}^{N} \frac{|b_n|^2 - |a_n|^2}{2} \geq 0$$

这意味着 $[I] - [S]^+[S]$ 是半正定的。

---

