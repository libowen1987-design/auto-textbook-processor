# Pozar《Microwave Engineering》4th Ed., Chapter 8 — Microwave Filters
> **中英双语版**

> 微波滤波器 — 从低通原型到工程实现

---

## §8.1 Periodic Structures

### 周期加载传输线

均匀传输线周期加载阻抗 $Z_L$，形成**周期结构**。每个单元传输矩阵 (ABCD):

$$
\begin{bmatrix}
A & B \\
C & D
\end{bmatrix}
=
\begin{bmatrix}
\cos$\beta$\ell & jZ_0\sin$\beta$\ell \\
jY_0\sin$\beta$\ell & \cos$\beta$\ell
\end{bmatrix}
\begin{bmatrix}
1 & Z_L \\
0 & 1
\end{bmatrix}
$$

即开路短截线加载的周期性结构。传播波满足 **Bloch 定理**（或 Floquet 定理）：

$$
V(z + d) = e^{-\gamma d} V(z), \quad I(z + d) = e^{-\gamma d} I(z)
$$

Bloch 阻抗 $Z_B$（周期性结构中的特征阻抗）：

$$
Z_B = \frac{B}{\sqrt{A^2 - 1}}, \quad \cosh\gamma d = A
$$

式中 $\gamma = \alpha + j\beta$ 为传播常数，$d$ 为周期长度。

**通带/阻带条件**：
- 通带：$|A| \le 1$，$\alpha = 0$，波无衰减传播
- 阻带：$|A| > 1$，$\alpha > 0$，波快速衰减

**工程要点**：周期结构是滤波器的物理基础。$k\beta d$ 图上的通带/阻带结构决定了滤波器频率响应。周期结构也出现在慢波结构、行波管、频率选择表面（FSS）中。

---

## §8.2 Filter Design by the Image Parameter Method

### 基础

**镜像参数法**是早期(1930s)的滤波器设计方法，基于级联二端口网络的镜像阻抗匹配。

镜像阻抗 $Z_{i1}$、$Z_{i2}$：从端口看进去，当另一端口端接镜像阻抗时该端口的输入阻抗。

二端口网络对称的，镜像阻抗 $Z_i = Z_{i1} = Z_{i2}$：

$$
Z_i = \sqrt{\frac{AB}{CD}}
$$

传播常数的镜像参数表示：

$$
e^{-\gamma} = \sqrt{AD} - \sqrt{BC}
$$

### 定 k 式滤波器（Constant-k）

**低通原型**：串联 L，并联 C，$k = \sqrt{L/C} = R_0$

$$
L = \frac{R_0}{\omega_c}, \quad C = \frac{1}{\omega_c R_0}
$$

**截止频率** $\omega_c$ 处镜像阻抗实部为零。

### m 导出式滤波器（m-Derived）

在定 k 式基础上添加串联/并联谐振支路，改善截止特性。

$$
L_1 = mL, \quad C_1 = mC
$$

$$
L_2 = \frac{1-m^2}{4m}L, \quad C_2 = \frac{1-m^2}{4m}C
$$

$m = 0.6$ 时通常获得最平坦的镜像阻抗特性。

**工程要点**：镜像参数法已基本被插入损耗法取代。但在理解滤波器基本行为和**早期原型构建**中仍有教学价值。实际设计中很少单独使用。

---

## §8.3 Filter Design by the Insertion Loss Method

### 功率损耗比 (Power Loss Ratio)

$$
P_{LR} = \frac{P_{\text{in}}}{P_{\text{load}}} = \frac{1}{1 - |\Gamma($\omega$)|^2}
$$

插入损耗 (Insertion Loss):

$$
IL = 10\log_{10} P_{LR} \quad [\text{dB}]
$$

回波损耗 (Return Loss):

$$
RL = 10\log_{10} \frac{1}{|\Gamma|^2} = -20\log_{10}|\Gamma| \quad [\text{dB}] 
$$

量纲检查：$P_{LR}$ 无量纲，$IL$ 和 $RL$ 均为 dB（无量纲对数）。

**设计流程**：
1. 确定通带/阻带频率、最大允许 IL、最小阻带衰减
2. 选择低通原型类型（Butterworth / Chebyshev / Elliptic）
3. 确定阶数 $n$ 
4. 查表获取归一化元件值 $g_k$
5. 频率/阻抗变换到目标频段

### 最大平坦（Butterworth）低通原型

功率损耗比：

$$
P_{LR} = 1 + k^2 \left(\frac{\omega}{\omega_c}\right)^{2N}
$$

- $N$：滤波器阶数
- $\omega_c$：截止频率（$P_{LR} = 1 + k^2$ 处）
- 3dB 截止时：$k=1$，$P_{LR}(\omega_c) = 2$，$IL(\omega_c) = 3.01$ dB

阶数确定（给定 $\omega_s > \omega_c$ 处衰减 $L_{As}$ [dB]）：

$$
N \ge \frac{L_{As}}{10 \log_{10}\left[(\omega_s/\omega_c)^{2} - 1\right] / 2}
$$

简化近似（$\omega_s \gg \omega_c$）：

$$
N \ge \frac{L_{As}}{20\log_{10}(\omega_s/\omega_c) + 6}
$$

**表 8.3 — Butterworth 低通原型归一化元件值** ($g_0 = 1, \omega_c = 1, g_{N+1} = 1$):

| $N$ | $g_1$ | $g_2$ | $g_3$ | $g_4$ | $g_5$ | $g_6$ | $g_7$ | $g_8$ | $g_9$ | $g_{10}$ |
|-----|-------|-------|-------|-------|-------|-------|-------|-------|-------|----------|
| 1   | 2.0000 | 1.0000 | | | | | | | | |
| 2   | 1.4142 | 1.4142 | 1.0000 | | | | | | | |
| 3   | 1.0000 | 2.0000 | 1.0000 | 1.0000 | | | | | | |
| 4   | 0.7654 | 1.8478 | 1.8478 | 0.7654 | 1.0000 | | | | | |
| 5   | 0.6180 | 1.6180 | 2.0000 | 1.6180 | 0.6180 | 1.0000 | | | | |
| 6   | 0.5176 | 1.4142 | 1.9318 | 1.9318 | 1.4142 | 0.5176 | 1.0000 | | | |
| 7   | 0.4450 | 1.2470 | 1.8019 | 2.0000 | 1.8019 | 1.2470 | 0.4450 | 1.0000 | | |
| 8   | 0.3902 | 1.1111 | 1.6629 | 1.9615 | 1.9615 | 1.6629 | 1.1111 | 0.3902 | 1.0000 | |
| 9   | 0.3473 | 1.0000 | 1.5321 | 1.8794 | 2.0000 | 1.8794 | 1.5321 | 1.0000 | 0.3473 | 1.0000 |
| 10  | 0.3129 | 0.9080 | 1.4142 | 1.7820 | 1.9754 | 1.9754 | 1.7820 | 1.4142 | 0.9080 | 0.3129 |

**物理直觉**：Butterworth 的通带最为平坦（最大平坦），阻带单调下降，$20N$ dB/decade 滚降。适合对通带平坦度要求极高、允许阻带慢滚降的场景。

### 等波纹（Chebyshev）低通原型

功率损耗比：

$$
P_{LR} = 1 + k^2 T_N^2\left(\frac{\omega}{\omega_c}\right)
$$

$T_N(x)$ 是 N 阶 Chebyshev 多项式：

$$
T_N(x) = \begin{cases}
\cos(N\cos^{-1}x), & |x| \le 1 \\
\cosh(N\cosh^{-1}x), & |x| > 1
\end{cases}
$$

通带波纹 $L_{Ar}$ [dB] 与 $k$ 的关系：

$$
L_{Ar} = 10\log_{10}(1 + k^2) \quad \Rightarrow \quad k = \sqrt{10^{L_{Ar}/10} - 1}
$$

阶数确定：

$$
N \ge \frac{\cosh^{-1}\sqrt{(10^{L_{As}/10} - 1) / (10^{L_{Ar}/10} - 1)}}{\cosh^{-1}(\omega_s/\omega_c)}
$$

**表 8.4 — Chebyshev 低通原型归一化元件值** ($g_0 = 1, \omega_c = 1$, 0.5 dB 波纹, $k = 0.3493$):

| $N$ | $g_1$ | $g_2$ | $g_3$ | $g_4$ | $g_5$ | $g_6$ | $g_7$ | $g_8$ | $g_9$ | $g_{10}$ | $g_{11}$ |
|-----|-------|-------|-------|-------|-------|-------|-------|-------|-------|----------|----------|
| 1   | 0.6986 | 1.0000 | | | | | | | | | |
| 2   | 1.4029 | 0.7071 | 1.9841 | | | | | | | | |
| 3   | 1.5963 | 1.0967 | 1.5963 | 1.0000 | | | | | | | |
| 4   | 1.6703 | 1.1926 | 2.3661 | 0.8419 | 1.9841 | | | | | | |
| 5   | 1.7058 | 1.2296 | 2.5408 | 1.2296 | 1.7058 | 1.0000 | | | | | |
| 6   | 1.7254 | 1.2479 | 2.6064 | 1.3137 | 2.4758 | 0.8696 | 1.9841 | | | | |
| 7   | 1.7372 | 1.2581 | 2.6381 | 1.3444 | 2.6381 | 1.2581 | 1.7372 | 1.0000 | | | |
| 8   | 1.7451 | 1.2647 | 2.6564 | 1.3590 | 2.6964 | 1.3389 | 2.5093 | 0.8796 | 1.9841 | | |
| 9   | 1.7504 | 1.2690 | 2.6678 | 1.3673 | 2.7237 | 1.3673 | 2.6678 | 1.2690 | 1.7504 | 1.0000 | |
| 10  | 1.7543 | 1.2721 | 2.6754 | 1.3725 | 2.7392 | 1.3806 | 2.7231 | 1.3485 | 2.5239 | 0.8842 | 1.9841 |

**Chebyshev 原型的特点**：
- 通带内为等波纹响应，阻带单调下降
- 相同阶数下比 Butterworth 阻带衰减更大（通常好 6~10 dB）
- 群延迟在通带边缘恶化明显
- $g_{N+1}$ 值取决于 $N$ 奇偶：$N$ 奇数时 $g_{N+1}=1.0$，$N$ 偶数时 $g_{N+1}$ 取表中最后一列

**物理直觉**：Chebyshev 用通带波纹换取更陡的阻带滚降。$L_{Ar}$ 越大（波纹越大），过渡带越陡。工程中 0.5 dB 和 1.0 dB 波纹最为常用。

### 椭圆函数滤波器（Elliptic）

具有通带和阻带均等波纹的特性，过渡带最陡。

$$
P_{LR} = 1 + \epsilon^2 F_N^2($\omega$/\omega_c)
$$

$F_N$ 为 N 阶椭圆有理函数。阻带零点的位置精确控制阻带最小衰减。

**工程要点**：椭圆滤波器过渡带最陡，但阻带有有限零点（非单调），在需要严格阻带抑制的场景（如发射机和谐波抑制）不如 Chebyshev 可靠。

### 线性相位滤波器（Linear Phase / Bessel）

通带内群延迟平坦（线性相位），但阻带滚降最慢。

**工程要点**：只用在需要最小脉冲失真的场景（如高速数字通信、时域反射测量）。

---

## §8.4 Filter Transformations

### 阻抗与频率缩放（Impedance & Frequency Scaling）

从归一化低通原型 ($g_0 = 1, \omega_c = 1$) 变换到实际滤波器：

**阻抗缩放** ($R_0 = Z_0$ 为目标端口阻抗):

$$
L \rightarrow L' = \frac{R_0}{g_0} L
$$

$$
C \rightarrow C' = \frac{g_0}{R_0} C
$$

量纲检查：$L'$ [H], $C'$ [F]; $R_0$ [Ω], $\omega_c$ [rad/s]。

**频率缩放**（低通→低通，截止 $\omega_c$）：

$$
L \rightarrow L' = \frac{L}{\omega_c}
$$

$$
C \rightarrow C' = \frac{C}{\omega_c}
$$

### 低通→高通变换

频率变量替换：

$$
\Omega \rightarrow -\frac{\omega_c}{\omega}
$$

归一化元件变换：
- 串联电感 $L \rightarrow$ 串联电容 $C' = 1/(\omega_c L)$ [F]
- 并联电容 $C \rightarrow$ 并联电感 $L' = 1/(\omega_c C)$ [H]

量纲检查：$C' = 1/(\omega_c L) \Rightarrow$ [F] ✓

### 低通→带通变换

频率替换：

$$
\Omega \rightarrow \frac{1}{\Delta} \left(\frac{\omega}{\omega_0} - \frac{\omega_0}{\omega}\right)
$$

其中 $\Delta = (\omega_2 - \omega_1)/\omega_0$ 为分数带宽，$\omega_0 = \sqrt{\omega_1\omega_2}$ 为几何中心频率。

**元件变换**（串联支路 $L_k \rightarrow LC$ 串联谐振）：
- 串联电感 $L_k \rightarrow$ 串联 $L_s = \frac{L_k Z_0}{\omega_0 \Delta}$ [H], $C_s = \frac{\Delta}{\omega_0 L_k Z_0}$ [F]

**元件变换**（并联支路 $C_k \rightarrow LC$ 并联谐振）：
- 并联电容 $C_k \rightarrow$ 并联 $L_p = \frac{\Delta}{\omega_0 C_k} Z_0$ [H], $C_p = \frac{C_k}{\omega_0 \Delta Z_0}$ [F]

量纲检查：$\omega_0 L_s = Z_0 L_k / \Delta$ [Ω] ✓

### 低通→带阻变换

频率替换：

$$
\Omega \rightarrow \frac{\Delta}{\omega_0/\omega - $\omega$/\omega_0}
$$

元件变换与带通互补：串联电感→并联 LC 谐振，并联电容→串联 LC 谐振。

### 工程要点

- 频率变换是滤波器设计的**核心桥梁**，连接理想原型与物理实现
- $\Delta$ 不能太大（通常 < 50%），否则变换公式的窄带近似失效
- 宽带带通滤波器常用级联低通+高通实现

---

## §8.5 Filter Implementation

### Richard's Transformation

将集总元件传输线中的 $\omega$ 映射到分布参数域：

$$
\Omega \rightarrow \tan($\beta$\ell) = \tan\left(\frac{\pi}{2}\frac{\omega}{\omega_0}\right)
$$

其中 $\ell = \lambda_0/8$（$\omega_0$ 处为 $90^\circ$ 电长度）。

**变换结果**：
- 集总电感 $L \rightarrow$ 短路短截线，特征阻抗 $Z_L = L$（归一化）
- 集总电容 $C \rightarrow$ 开路短截线，特征阻抗 $Z_C = 1/C$（归一化）

重要特性：Richard 变换将 $s = j\omega$ 平面映射到 $s = j\tan($\beta$\ell)$ 平面，周期为 $2\omega_0$。

### Kuroda's Identities

Kuroda 恒等式将串联短截线变换为并联短截线（或反之），同时引入单位元素（unit element, UE）。

**四个基本恒等式**（$n^2 = 1 + Z_2/Z_1$）：

1. 串联短路短截线 + 单位元素 → 并联开路短截线 + 单位元素
2. 并联开路短截线 + 单位元素 → 串联短路短截线 + 单位元素
3. 串联开路短截线 + 单位元素 → 并联短路短截线 + 单位元素
4. 并联短路短截线 + 单位元素 → 串联开路短截线 + 单位元素

**工程要点**：
- Richard 变换 + Kuroda 恒等式使集总元件滤波器原型可用分布参数传输线实现
- 单位元素的电长度在 $\omega_0$ 处为 $\lambda_0/8$
- Kuroda 恒等式的 $n$ 是变换比，物理上等效于一个理想阻抗变换器

### 阻抗/导纳逆变器（Impedance / Admittance Inverters）

**K 逆变器**（阻抗逆变器）：在输出端将负载阻抗 $Z_L$ 变换为 $K^2/Z_L$

$$
\mathbf{T} = \begin{bmatrix}
0 & jK \\
j/K & 0
\end{bmatrix}
$$

**J 逆变器**（导纳逆变器）：在输出端将负载导纳 $Y_L$ 变换为 $J^2/Y_L$

$$
\mathbf{T} = \begin{bmatrix}
0 & j/J \\
jJ & 0
\end{bmatrix}
$$

K/J 逆变器可用以下方式实现：
- $$\lambda$/4$ 传输线：$K = Z_0$
- 集总元件 $\pi$ 型或 T 型网络

**工程要点**：逆变器允许将串联元件转换为并联元件，简化滤波器拓扑。$$\lambda$/4$ 传输线是最简单的宽频段 K 逆变器实现。

---

## §8.6 Stepped-Impedance Low-Pass Filters

### 原理

**阶跃阻抗滤波器**（或称高-低阻抗滤波器）用交替的高/低特征阻抗短传输线段近似集总电感和电容。

- **高阻抗段**（$Z_{\text{high}} \approx 100\text{--}150\,\Omega$）→ 串联电感
- **低阻抗段**（$Z_{\text{low}} \approx 10\text{--}30\,\Omega$）→ 并联电容

等效电感（高阻抗段）：

$$
L_k \approx \frac{Z_{\text{high}} \ell_k}{v_p} \quad [\text{H}]
$$

等效电容（低阻抗段）：

$$
C_k \approx \frac{\ell_k}{Z_{\text{low}} v_p} \quad [\text{F}]
$$

式中 $v_p = c/\sqrt{\epsilon_r}$ 为相速度，$\ell_k$ 为传输线物理长度。

传输线段长度：

$$
\ell_k^L = \frac{L_k v_p}{Z_{\text{high}}}, \quad \ell_k^C = C_k Z_{\text{low}} v_p
$$

### 设计流程

1. 确定低通原型 $g_k$ 
2. 选择 $Z_{\text{high}}$ 和 $Z_{\text{low}}$（通常 $Z_{\text{high}}/Z_{\text{low}} > 5$）
3. 计算每个传输线段的长度 $\ell_k$
4. 验证各段电长度 $< $\lambda$/8$（短线段近似有效）

### 工程要点

- 实现简单，常用微带线
- 频率响应周期性产生寄生通带（Richard 变换所致）
- 常用于中低性能需求的简单应用场景
- $Z_{\text{high}}/Z_{\text{low}}$ 比值越大，寄生通带越远

---

## §8.7 Coupled-Line Filters

### 耦合线理论

**平行耦合线**（TEM 模式）有两个本征模式：
- 偶模（even mode）：$Z_{0e}$，两线同向电流
- 奇模（odd mode）：$Z_{0o}$，两线反向电流

特征阻抗关系（对称耦合线）：

$$
Z_{0e} = Z_0 \sqrt{\frac{1+k}{1-k}}, \quad Z_{0o} = Z_0 \sqrt{\frac{1-k}{1+k}}
$$

其中 $k$ 为耦合系数（无量纲），逆推得：

$$
k = \frac{Z_{0e} - Z_{0o}}{Z_{0e} + Z_{0o}}
$$

### 单节耦合线带通滤波器

$$\lambda$/4$ 耦合线节可构成带通单元。每个耦合线节等效为一个 K 或 J 逆变器加两段 $$\lambda$/4$ 线。

$-3$ dB 带宽下的设计公式（单节，$n=1$ 偶=4.5章公式）：

$$
\frac{J_{j,j+1}}{Y_0} = \frac{\Delta}{\sqrt{g_j g_{j+1}}}
$$

$$
Z_{0e}^{j,j+1} = Z_0\left[1 + Z_0\frac{J_{j,j+1}}{Y_0} + \left(Z_0\frac{J_{j,j+1}}{Y_0}\right)^2\right]
$$

$$
Z_{0o}^{j,j+1} = Z_0\left[1 - Z_0\frac{J_{j,j+1}}{Y_0} + \left(Z_0\frac{J_{j,j+1}}{Y_0}\right)^2\right]
$$

### N 节耦合线带通滤波器设计

1. 确定低通原型 $g_0, g_1, ..., g_N, g_{N+1}$
2. 计算 J 逆变器系数：

$$
\frac{J_{0,1}}{Y_0} = \sqrt{\frac{$\pi$\Delta}{2g_0 g_1}}, \quad
\frac{J_{j,j+1}}{Y_0} = \frac{$\pi$\Delta}{2\sqrt{g_j g_{j+1}}}, \quad
\frac{J_{N,N+1}}{Y_0} = \sqrt{\frac{$\pi$\Delta}{2g_N g_{N+1}}}
$$

3. 计算奇偶模阻抗并查表（如 Getsinger 模式或数值法）获取物理尺寸

### 物理直觉

- 耦合线滤波器带宽受限于可实现的耦合强度
- 弱耦合（$k < 0.1$）→ 窄带；强耦合（$k > 0.3$）→ 宽带
- 微带实现时因非 TEM 特性，奇偶模相速不同，方向性有限

---

## §8.8 Hairpin, Interdigital, and Combine Filters

### 发卡线滤波器（Hairpin-Line Filter）

**结构**：耦合线谐振器 U 形折叠（形似发卡），级联排列。

- 本质上是折叠的耦合线带通滤波器
- 紧凑尺寸，适合 MMIC 和小型化设计
- 电磁耦合由相邻发卡之间的间隙控制
- 设计方法：先设计耦合线滤波器，再折叠谐振器

### 叉指滤波器（Interdigital Filter）

**结构**：多个 $\lambda_0/4$ 谐振器交叉排列，末端交替接地面。

- 带状线或微带实现
- 谐振器电长度 $90^\circ$（中心频率）
- 相邻谐振器之间的耦合控制带宽
- **特点**：
  - 结构紧凑（通常占总面积的 30-50%）
  - 第二通带出现在 $3f_0$ 处
  - 阻带衰减大（> 40 dB 常见）

设计参数：
- $Y_k$：第 $k$ 个谐振器的特征导纳
- $C_{k,k+1}$：相邻谐振器之间的耦合电容
- 耦合矩阵综合法普遍用于精确设计

### 梳状线滤波器（Combine Filter）

**结构**：多个 $\lambda_0/8$ 谐振器（短于 $\lambda_0/4$），一端接地，一端加载电容，平行排列。

- **特点**：
  - 比叉指滤波器更紧凑（$\lambda_0/8$ 对比 $\lambda_0/4$）
  - 寄生通带在更高频率（$4f_0-5f_0$）
  - 广泛用于窄带应用（%BW < 10-15%）
  - 谐振器之间的耦合通过邻近耦合实现

设计参数（Pozar 表 8.8 近似公式）：

谐振器到地电容：

$$
C_k = \frac{Y_k \tan($\beta$\ell)}{\omega_0}
$$

耦合电容：

$$
C_{k,k+1} = \frac{J_{k,k+1}}{\omega_0}
$$

### 工程要点对比

| 类型 | 长度 | 带宽 | 寄生通带 | 尺寸 | 适用场景 |
|------|------|------|----------|------|----------|
| 耦合线 | $\lambda_0/4$ | 窄-中 | 3$f_0$ | 大 | 通用 |
| 发卡线 | $\lambda_0/4$ 折叠 | 窄-中 | 3$f_0$ | 中 | 小型化 |
| 叉指 | $\lambda_0/4$ | 窄-宽 | 3$f_0$ | 小 | 多节、高抑制 |
| 梳状线 | $\lambda_0/8$ + C | 窄 | 4$f_0$+ | 极小 | 通信系统 |

---

## §8.9 Waveguide and Cavity Resonator Filters

### 波导滤波器

波导作为传输线实现滤波器，常见类型：

**1. 波导膜片滤波器（Waveguide Iris Filter）**
- 膜片（感性或容性膜片）充当 K/J 逆变器
- 波导段充当谐振器
- 高 Q 值（2000-10000），插损低

**2. 波导探针/耦合孔滤波器**
- 通过耦合孔级联腔体
- 切比雪夫或巴特沃斯响应

**3. E 面波导滤波器（E-Plane Filter）**
- 波导中插入金属插件（E 面）
- 低插入损耗，易于加工

### 腔体滤波器（Cavity Filters）

介质谐振腔或金属腔体级联。每个腔体等效为并联 RLC 谐振电路。

**关键参数**：
- 无载 Q 值 $Q_u$：腔体固有品质因数
- 外部 Q 值 $Q_e$：腔体与外部电路耦合强度
- 耦合系数 $k_{ij}$：相邻腔体间的耦合

$$
Q_e = \frac{g_0 g_1}{\Delta}, \quad k_{j,j+1} = \frac{\Delta}{\sqrt{g_j g_{j+1}}}
$$

**工程要点**：
- 腔体滤波器是当今基站和卫星通信中最常用的高性能滤波器
- 温度稳定性常用低膨胀合金或介质陶瓷保证
- 交叉耦合技术可在阻带引入传输零点，显著改善选择性

---

## §8.10 Other Types and Advanced Topics

### 可调谐滤波器（Tunable Filters）
- 变容二极管调谐（YIG、BST、MEMS）
- 调谐范围 30-60%（窄带），3:1（宽带较低 Q）
- 主要挑战：调谐时保持带宽和匹配

### 有源滤波器（Active Filters）
- 负阻补偿（Negative resistance compensation）
- 用于可集成化（MMIC）时补偿无源损耗

### 声波滤波器（SAW / BAW）
- 声表面波（SAW）：1 MHz - 3 GHz
- 体声波（BAW / FBAR）：1 - 10 GHz
- Q 值 1000-10000，极其紧凑

### 超导滤波器（HTS Filters）
- YBCO 高温超导薄膜
- Q 值 > 50000
- 用于基站前端，极低插损，需制冷

---

## §8.11 Summary and Engineering Guidelines

### 选择流程

```
需求规格
  ↓
选择低通原型类型
  ├── 高平坦度 → Butterworth
  ├── 高选择性 → Chebyshev（0.1-1 dB 波纹）
  ├── 最陡过渡带 → Elliptic
  └── 脉冲保真 → Bessel（线性相位）
  ↓
确定阶数 N
  ↓
频率变换 → 目标频段/类型
  ↓
选择实现技术
  ├── 微带集总 → 阶跃阻抗 LPF
  ├── 耦合线 → 耦合线带通
  ├── 折叠/小型 → 发卡/叉指/梳状线
  └── 高性能 → 波导/腔体
  ↓
全波仿真验证
```

### 常见陷阱

1. **寄生通带**：分布参数滤波器的周期性频率响应会在高频产生寄生通带
2. **非 TEM 效应**：微带滤波器的色散使设计公式产生误差
3. **制造公差**：窄带滤波器对加工公差非常敏感
4. **功率容量**：阶跃阻抗滤波器中窄线处的电流密度限制功率容量
5. **无源互调（PIM）**：接触非线性在基站应用中可能导致 PIM 问题

---

## 附录：常用公式速查

| 量 | 公式 | 量纲 |
|---|------|------|
| 功率损耗比 | $P_{LR} = 1/(1-|\Gamma|^2)$ | 无量纲 |
| 插入损耗 | $IL = 10\log_{10}P_{LR}$ [dB] | 无量纲 |
| Butterworth $P_{LR}$ | $P_{LR} = 1 + ($\omega$/\omega_c)^{2N}$ | 无量纲 |
| Chebyshev $P_{LR}$ | $P_{LR} = 1 + k^2 T_N^2($\omega$/\omega_c)$ | 无量纲 |
| 阻抗缩放 | $L' = (Z_0/g_0)L$, $C' = (g_0/Z_0)C$ | [H], [F] |
| 低通→带通 | $\Delta = (\omega_2-\omega_1)/\omega_0$ | 无量纲 |
| 3dB 耦合器 | $Z_{0e} = Z_0(1+k)/(1-k)$ | [Ω] |
| Richard 变换 | $\Omega = \tan($\pi$$\omega$/2\omega_0)$ | 无量纲 |
| K-inv 到耦合线 | $K = Z_{\text{inv}} = Z_0 \cdot \frac{k}{\sqrt{1-k^2}}$ | [Ω] |

---

*Notes prepared by 二龙虾, audited by 🦞 (小龙虾)*
