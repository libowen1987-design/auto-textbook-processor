# Pozar Chapter 4 — Microwave Network Analysis
> **中英双语版**

> Comprehensive notes on Pozar *Microwave Engineering*, 4th Edition, pp. 186–249.
> Covers impedance/admittance matrices, scattering parameters, ABCD matrix, signal flow graphs, T-parameters, and generalized scattering parameters.

---

## 4.1 Impedance and Admittance Matrices | 阻抗和导纳矩阵

A microwave network is characterized by its **ports** — points where energy enters or leaves the network.
> 微波网络由其**端口**表征——能量进出网络的点。

For an $N$-port network, the impedance matrix $\mathbf{Z}$ relates port voltages to port currents:
> 对于 $N$ 端口网络，阻抗矩阵 $\mathbf{Z}$ 将端口电压与端口电流联系起来：

$$\boxed{\mathbf{V} = \mathbf{Z} \mathbf{I}}, \quad Z_{ij} = \left.\frac{V_i}{I_j}\right|_{I_k=0,\;k\neq j}$$

$Z_{ii}$ is the input impedance at port $i$ with all other ports open-circuited. $Z_{ij}$ is the transfer impedance.
> $Z_{ii}$ 是端口 $i$ 的输入阻抗（其他端口开路），$Z_{ij}$ 是转移阻抗。

The admittance matrix $\mathbf{Y} = \mathbf{Z}^{-1}$:
> 导纳矩阵 $\mathbf{Y} = \mathbf{Z}^{-1}$：

$$\boxed{\mathbf{I} = \mathbf{Y} \mathbf{V}}, \quad Y_{ij} = \left.\frac{I_i}{V_j}\right|_{V_k=0,\;k\neq j}$$

**Properties / 性质：**
- **Reciprocal / 互易** (passive, no anisotropic media): $\mathbf{Z} = \mathbf{Z}^T$, $\mathbf{Y} = \mathbf{Y}^T$
- **Lossless / 无损耗**: All $Z_{ij}$ and $Y_{ij}$ are purely imaginary

---

## 4.2 Scattering Parameters | 散射参数 (S 参数)

S-parameters relate incident and reflected voltage waves at the ports:
> S 参数将端口处的入射波和反射波电压联系起来：

$$\mathbf{V}^- = \mathbf{S} \mathbf{V}^+, \quad V_n = V_n^+ + V_n^-$$

Normalized waves: $a_n = V_n^+/\sqrt{Z_{0n}}$, $b_n = V_n^-/\sqrt{Z_{0n}}$.
> 归一化波：$a_n$, $b_n$。

$$S_{ij} = \left.\frac{V_i^-}{V_j^+}\right|_{V_k^+=0,\;k\neq j}$$

$S_{ii}$ is the **input reflection coefficient** at port $i$ when all other ports are matched.
> $S_{ii}$ 是端口 $i$ 的输入反射系数（其他端口匹配时）。

$S_{ij}$ ($i\neq j$) is the **transmission coefficient** from port $j$ to port $i$.
> $S_{ij}$ ($i\neq j$) 是从端口 $j$ 到端口 $i$ 的传输系数。

**Properties / 性质：**
- **Reciprocal**: $\mathbf{S} = \mathbf{S}^T$
- **Lossless**: $\mathbf{S}^\dagger \mathbf{S} = \mathbf{I}$ (unitary matrix / 幺正矩阵)
- **Shift in reference plane**: $S_{ij}' = S_{ij} e^{-j(\theta_i + \theta_j)}$ (changing line lengths)
> **参考面移动**：改变传输线长度时 S 参数相位变化。

---

## 4.3 The Scattering Matrix of a Lossless Network | 无损耗网络的散射矩阵

For a lossless, reciprocal network, the unitary condition $\mathbf{S}^\dagger \mathbf{S} = \mathbf{I}$ implies:
> 对于无损耗互易网络，幺正条件意味着：

- Power conservation: $\sum_{k=1}^N |S_{ki}|^2 = 1$ for each column $i$
  > 每列平方和等于 1，即功率守恒
- Orthogonality: $\sum_{k=1}^N S_{ki}^* S_{kj} = 0$ for $i \neq j$
  > 不同列之间正交

**Example: 2-port lossless network / 二端口无损耗网络示例：**

$$|S_{11}|^2 + |S_{21}|^2 = 1, \quad S_{11}^* S_{12} + S_{21}^* S_{22} = 0$$

This leads to the relationship between the magnitudes and phases of S-parameters.
> 这给出了 S 参数幅度和相位之间的关系。

---

## 4.4 ABCD Matrix (Transfer Matrix) | ABCD 矩阵（转移矩阵）

For two-port networks, the ABCD matrix relates the input to the output:
> 对于二端口网络，ABCD 矩阵关联输入和输出：

$$\begin{bmatrix} V_1 \\ I_1 \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} V_2 \\ I_2 \end{bmatrix}$$

**Properties / 性质：**
- **Reciprocal**: $AD - BC = 1$
- **Symmetric**: $A = D$
- **Lossless**: $A$ and $D$ real, $B$ and $C$ imaginary

**Cascading / 级联：** For networks in cascade, the overall ABCD matrix is the product of individual matrices.
> 级联网络的 ABCD 矩阵等于各网络 ABCD 矩阵的乘积。

**Common 2-port networks / 常见二端口网络：**

| Network | ABCD Matrix |
|---------|-------------|
| Series impedance $Z$ | $\begin{bmatrix} 1 & Z \\ 0 & 1 \end{bmatrix}$ |
| Shunt admittance $Y$ | $\begin{bmatrix} 1 & 0 \\ Y & 1 \end{bmatrix}$ |
| Transmission line (length $\ell$) | $\begin{bmatrix} \cos\beta\ell & jZ_0\sin\beta\ell \\ jY_0\sin\beta\ell & \cos\beta\ell \end{bmatrix}$ |
| Ideal transformer ($1$:$N$) | $\begin{bmatrix} 1/N & 0 \\ 0 & N \end{bmatrix}$ |

---

## 4.5 Signal Flow Graphs | 信号流图

Signal flow graphs provide a graphical representation of S-parameter networks.
> 信号流图提供了 S 参数网络的图形化表示。

**Rules / 规则：**
- Nodes represent variables ($a_n, b_n$)
- Branches represent S-parameters
- **Mason's rule / Mason 规则**: $T = \frac{\sum_k T_k \Delta_k}{\Delta}$, where $\Delta = 1 - \sum L_1 + \sum L_2 - \cdots$
  > Mason 规则用于从信号流图计算传递函数。

---

## 4.6 T-Parameters (Transfer Scattering Parameters) | T 参数（转移散射参数）

T-parameters relate forward and backward waves at port 1 to those at port 2:
> T 参数将端口 1 的正向和反向波与端口 2 的关联起来：

$$\begin{bmatrix} b_1 \\ a_1 \end{bmatrix} = \begin{bmatrix} T_{11} & T_{12} \\ T_{21} & T_{22} \end{bmatrix} \begin{bmatrix} a_2 \\ b_2 \end{bmatrix}$$

Useful for cascading networks (multiply T-matrices).
> 适用于级联网络（相乘 T 矩阵）。

---

## 4.7 Generalized Scattering Parameters | 广义散射参数

For networks with different characteristic impedances at different ports:
> 对于不同端口具有不同特征阻抗的网络：

Normalized wave amplitudes: $a_i = \frac{1}{2\sqrt{Z_{0i}}}(V_i + Z_{0i} I_i)$, $b_i = \frac{1}{2\sqrt{Z_{0i}}}(V_i - Z_{0i}^* I_i)$.
> 归一化波幅定义如上。

The generalized S-parameters are defined as $\mathbf{b} = \mathbf{S} \mathbf{a}$.
> 广义 S 参数定义为 $\mathbf{b} = \mathbf{S} \mathbf{a}$。

For lossless networks: $\mathbf{S}^\dagger \mathbf{S} = \mathbf{I}$ (unitary in generalized sense).
> 对于无损耗网络，广义幺正条件仍成立。

---

## 4.8 Conversions Between Network Parameters | 网络参数之间的转换

| Conversion | Formula |
|------------|---------|
| $Z \to S$ | $\mathbf{S} = (\mathbf{Z} - Z_0\mathbf{I})(\mathbf{Z} + Z_0\mathbf{I})^{-1}$ |
| $S \to Z$ | $\mathbf{Z} = Z_0(\mathbf{I} + \mathbf{S})(\mathbf{I} - \mathbf{S})^{-1}$ |
| $S \to ABCD$ | $A = \frac{(1+S_{11})(1-S_{22})+S_{12}S_{21}}{2S_{21}}$, etc. |
| $ABCD \to S$ | $S_{11} = \frac{A+B/Z_0-CZ_0-D}{A+B/Z_0+CZ_0+D}$, etc. |

---

## 4.9 Measurement of S-Parameters | S 参数的测量

S-parameters are measured using a Vector Network Analyzer (VNA).
> S 参数使用矢量网络分析仪（VNA）测量。

**Calibration / 校准：** Errors are removed using known standards (open, short, load, thru).
> 使用已知标准（开路器、短路器、负载、直通）去除测量误差。

Common calibration methods: SOLT (Short-Open-Load-Thru), TRL (Thru-Reflect-Line), and LRM (Line-Reflect-Match).
> 常见校准方法：SOLT、TRL、LRM。

**Summary Table / 汇总表：**

| Parameter | Size | Relation | Best for |
|-----------|------|----------|----------|
| $\mathbf{Z}$ | $N \times N$ | $\mathbf{V} = \mathbf{Z}\mathbf{I}$ | Series networks |
| $\mathbf{Y}$ | $N \times N$ | $\mathbf{I} = \mathbf{Y}\mathbf{V}$ | Shunt networks |
| $\mathbf{S}$ | $N \times N$ | $\mathbf{V}^- = \mathbf{S}\mathbf{V}^+$ | High-frequency measurement |
| $ABCD$ | $2 \times 2$ | $\begin{bmatrix}V_1\\I_1\end{bmatrix}=ABCD\begin{bmatrix}V_2\\I_2\end{bmatrix}$ | Cascading 2-port networks |
| $\mathbf{T}$ | $2 \times 2$ | $\begin{bmatrix}b_1\\a_1\end{bmatrix} = \mathbf{T}\begin{bmatrix}a_2\\b_2\end{bmatrix}$ | Cascading (via multiplication) |
