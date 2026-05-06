# Collins Chapter 5 — Impedance Transformation and Matching

> **来源：** R. E. Collin, *Foundations for Microwave Engineering*, 2nd Ed.
> **范围：** §5.1–§5.16, pp. 303–370
> **注：** 本章页码均标注原书页码，公式保留 Collin 原编号。

---

## §5.1 Smith Chart (pp. 303–308)

### 阻抗变换的基本公式

传输线上距离负载 / 处的输入阻抗：

$$ Z_{in}(l) = Z_c \frac{Z_L + j Z_c \tan \beta l}{Z_c + j Z_L \tan \beta l} \tag{5.1} $$

反射系数：

$$ \Gamma(l) = \frac{Z_{in}(l) - Z_c}{Z_{in}(l) + Z_c} = \Gamma_L e^{-2j\beta l} \tag{5.2} $$

归一化阻抗与反射系数的关系：

$$ \frac{Z_{in}}{Z_c} = \frac{1 + \Gamma(l)}{1 - \Gamma(l)} \tag{5.3a} $$
$$ \frac{Z_L}{Z_c} = \frac{1 + \Gamma_L}{1 - \Gamma_L} \tag{5.3b} $$

### 反射系数的极坐标表示 (p. 305)

令 $\Gamma = \rho e^{j\theta}$，归一化输入阻抗 $Z_{in}/Z_c = R + jX$，则：

$$ R = \frac{1 - u^2 - v^2}{(1 - u)^2 + v^2} $$
$$ X = \frac{2v}{(1 - u)^2 + v^2} $$

其中 $u = \rho \cos\theta$，$v = \rho \sin\theta$。

**等电阻圆与等电抗圆** (p. 305, Eqs. 5.6a, 5.6b)：

$$ \left(u - \frac{R}{R+1}\right)^2 + v^2 = \left(\frac{1}{R+1}\right)^2 \tag{5.6a} $$
$$ (u - 1)^2 + \left(v - \frac{1}{X}\right)^2 = \left(\frac{1}{X}\right)^2 \tag{5.6b} $$

### 关键特性 (pp. 305–308)

- 顺时针旋转：远离负载（朝向信号源），旋转角度 $2\beta l = 4\pi l / \lambda$
- 完整一圈对应 $l = \lambda/2$，即阻抗每半波长重复一次
- $\lambda/4$ 变换：阻抗点旋转 $180^\circ$，阻抗 $\leftrightarrow$ 导纳
- 有耗线：沿螺旋线向圆心移动，$\rho = \rho_L e^{-2\alpha l}$ (Eq. 5.7, p. 307)
- 圆心：匹配点 ($\rho = 0$)

### 阻抗-导纳圆图 (p. 307)

将 Smith 圆图旋转 $180^\circ$ 叠加，一套圆显示阻抗值，另一套显示导纳值。

---

## §5.2 Impedance Matching with Reactive Elements (pp. 308–319)

### 匹配的必要性 (p. 308)

- 减少频率敏感性
- 降低传输线上的驻波场强（提高功率容量）
- 降低传输损耗

### Single-Stub Matching — Shunt Stub (pp. 309–311)

**纯电导负载 $Y_L = G$ 的情形：**

在距负载 $d$ 处输入导纳为 $Y_{in} = 1 + jB$，并联短路线提供的输入电纳为 $-jB$。

$$ t = \tan \beta d $$

求解 $d$ 满足方程：

$$ \tan^2 \beta d = \frac{1 - G}{G} \quad \text{或} \quad d = \frac{\lambda}{4\pi} \cos^{-1} \left(\frac{G-1}{G+1}\right) \tag{5.10} $$

两个主解：$d_1$ 和 $\lambda/2 - d_1$ (p. 310)

短路 stub 长度 $l_0$：

$$ \cot \beta l_0 = \frac{1 - G}{\sqrt{G}} \quad \text{或} \quad l_0 = \frac{\lambda}{2\pi} \tan^{-1} \frac{\sqrt{G}}{1 - G} \tag{5.12} $$

**复负载的一般情形：** 先定位电压最小点，该点处导纳为纯实数 $Y_{in} = S$ (驻波比)。则：

$$ d_0 = \frac{\lambda}{4\pi} \cos^{-1} \left(\frac{S-1}{S+1}\right) \tag{5.14a} $$
$$ l_0 = \frac{\lambda}{2\pi} \tan^{-1} \frac{\sqrt{S}}{1 - S} \tag{5.14b} $$

### Single-Stub Matching — Series Stub (pp. 311–312)

在电压最小点处 $Z_{in} = 1/S$，串联开路/短路线的电抗 $-jX$ 抵消 $jX$。

$$ d_0 = \frac{\lambda}{4\pi} \cos^{-1} \left(\frac{S-1}{S+1}\right) \tag{5.15a} $$
$$ l_0 = \frac{\lambda}{2\pi} \tan^{-1} \frac{\sqrt{S}}{1 - S} \tag{5.16} $$

### Double-Stub Matching (pp. 312–317)

双枝节调谐器：两个间距 $d$ 固定的并联枝节。图 5.7 (p. 313)

**分析步骤：**
1. 第一枝节加 $jB_1$ 沿等电导圆移动 $Y_L$ 到 $P_2$
2. 经过长度 $d$ 的传输线变换到 $P_3$（在 $G=1$ 圆上）
3. 第二枝节加 $jB_2 = -jB$ 匹配到原点

**可匹配范围：** (p. 315)

$$ 0 < G_L < \csc^2 \beta d \tag{5.19} $$

- $d = \lambda/8$：可匹配 $G_L < 2$ 以外的导纳
- $d = \lambda/4$：可匹配 $G_L < 1$ 的情形
- $d$ 接近 $0$ 或 $\lambda/2$ 理论覆盖范围最大，但实际受衰减和频率敏感性限制

式 (5.20) 给出 $B_1$ 的解析解：

$$ B_1 = -B_L + \frac{1 \pm \sqrt{(1 + t^2) G_L - G_L^2 t^2}}{t} \tag{5.20} $$

其中 $t = \tan \beta d$。

**Example 5.1** (p. 316): $Y_L = 0.4 + j1.0$，$d = \lambda/8$。两解：
- 解1：$jB_1 = j0.8$，$jB_2 = j3$，$l_2/\lambda = 0.199$
- 解2：$jB_1 = -j0.8$，$jB_2 = -j1$，$l_2/\lambda = 0.125$

### Triple-Stub Tuner (pp. 317–319)

三枝节能覆盖所有负载导纳值（图 5.12, p. 318）。本质上是两个双枝节调谐器的组合，中心枝节共享，提供额外自由度以实现宽带化。

---

## §5.5 Matching with Lumped Elements (pp. 319–330)

### L 型匹配网络 (pp. 322–325)

两种基本拓扑结构（图 5.17, p. 323）：
- **电路 (a)：** 并联 $jB_1$ + 串联 $jX_2$，用于 $G_L < 1$
- **电路 (b)：** 串联 $jX_1$ + 并联 $jB_2$，用于 $R_L < 1$

**使用 Smith 圆图的设计步骤：**

**Case 1 (图 5.18, p. 324):** 电路 (a)
1. 构造 $G=1$ 圆旋转 $180^\circ$
2. 从 $Y_L$ 加 $jB_1$ 沿等电导圆移动到旋转 $G=1$ 圆
3. 反射得到 $Z'$ 在 $R=1$ 圆上
4. 减 $jX_2$ 匹配到原点

**Case 2 (图 5.19, p. 325):** 电路 (b)
1. 构造 $R=1$ 圆旋转 $180^\circ$
2. 从 $Z_L$ 加 $jX_1$ 沿等电阻圆移动到旋转 $R=1$ 圆
3. 反射得到 $Y'$ 在 $G=1$ 圆上
4. 减 $jB_2$ 匹配到原点

带宽通过选择储能较小的解（较低 $Q$）来最大化。

### Circuit Q and Bandwidth (pp. 325–330)

品质因数定义：

$$ Q = \frac{\omega (\text{平均储能})}{\text{耗散功率}} \tag{5.22} $$

**并联谐振电路 (图 5.20, p. 326):**

$$ Q = \omega_0 C R_L = \frac{R_L}{\omega_0 L} \tag{5.26} $$

有载 $Q_L = Q/2$，3-dB 分数带宽 $= 1/Q_L$。

**电路 Q 的计算示例 (pp. 328–329, 图 5.21):**
- 电路 (a)：$Q = \omega_0 C_L R_L$
- 电路 (b)：$Q = \omega_0 C_2 Z_c + \omega_0 C_L R_L$

**设计准则：** 最小电路 Q 在匹配电路与负载使用相反类型电抗元件时获得（负载电感性则匹配用电容性元件，反之亦然）。

VSWR 与回波损耗的关系 (p. 329)：

$$ \text{Return Loss} = -20 \log \rho = -20 \log \frac{\text{VSWR} - 1}{\text{VSWR} + 1} $$

---

## §5.6 Design of Complex Impedance Terminations (pp. 330–334)

### 放大器的匹配网络 (图 5.22, p. 331)

三种结构：
- **图 5.22b：** 传输线 + shunt stub
- **图 5.22c：** 串联电抗 + 并联电纳（$R_L < 1$ 时可用）
- **图 5.22d：** 并联电纳 + 串联电抗（$G_L < 1$ 时可用）

### 图 5.22b 的设计步骤 (pp. 331–332)

1. 在 Smith 圆图上定位 $Z_L$，反射得 $Y_L$
2. 逆时针旋转 $Y_L$（朝负载方向）至 $G=1$ 圆，得距离 $l$
3. $jB_1 = jB$（$G=1$ 圆上的值）

解析解 (Eq. 5.29, p. 332):

$$ B_1 = \pm \frac{\sqrt{B_L^2 + G_L^2 + 1 - 2G_L}}{G_L} = \pm \frac{\sqrt{R_L^2 + X_L^2 + 1 - 2R_L}}{R_L} \tag{5.29a} $$
$$ \tan \beta l = \frac{G_L - 1}{B_L + B_1 G_L} = \frac{R_L - 1}{X_L - B_1 R_L} \tag{5.29b} $$

### 图 5.22d 的设计步骤 (pp. 333–334)

1. 构造旋转 $180^\circ$ 的 $G=1$ 圆
2. 沿 $G = G_L$ 圆逆时针移动 $Y_L$ 至旋转 $G=1$ 圆
3. $jB_1 = j(B_L - B)$
4. 反射得 $Z'_{in}$ 在 $R=1$ 圆上，$jX_2 = jX$

---

## §5.7 Invariant Property of Impedance Mismatch Factor (pp. 334–338)

### 失配因子 (pp. 334–335)

输入功率：

$$ P_{in} = \frac{1}{2} \frac{|V_s|^2 R_{in}}{|Z_s + Z_{in}|^2} = \frac{1}{2} \frac{|V_s|^2}{4 R_s} \cdot \frac{4 R_{in} R_s}{|Z_{in} + Z_s|^2} = P_{ava} M $$

其中失配因子：

$$ M = \frac{4 R_{in} R_s}{|Z_{in} + Z_s|^2} \tag{5.31} $$

### 不变性定理 (pp. 335–336)

在无耗互易网络插在源与负载之间时，任意平面处的可用功率与失配因子均不变（图 5.26, p. 335）：

$$ P_{ava, out} = P_{ava, in} = P_{ava, s} $$
$$ M_L = M $$

### 对多级放大器的应用 (pp. 336–338, 图 5.27)

输入 VSWR：

$$ \rho = (1 - M_1)^{1/2} $$
$$ \text{VSWR} = \frac{1 + \sqrt{1 - M_1}}{1 - \sqrt{1 - M_1}} \tag{5.32} $$

级间匹配网络的约束 (Eq. 5.33, p. 338)：

$$ \frac{4 R_{in, 2} R_{s2}}{|Z_{in,2} + Z_{s2}|^2} = \frac{4 R_{L1} R_{out,1}}{|Z_{L1} + Z_{out,1}|^2} \tag{5.33} $$

### Π 型匹配网络的设计 (pp. 338–339)

式 (5.34)–(5.37) 给出了 Π 网络和两种传输线实现方案的参数关系。

---

## §5.8 Waveguide Reactive Elements (pp. 339–342)

### Shunt Inductive Elements (pp. 339–341)

**对称电感膜片 (图 5.29a, Eq. 5.38, p. 340):**

$$ \frac{B}{Y_0} = -\frac{2\pi}{\beta a} \cot^2 \frac{\pi d}{2a} \left[ 1 + \frac{\beta a}{2\pi} \frac{\sin^2 \frac{\pi d}{a}}{\sin^2 \frac{\pi d}{2a}} \right] $$

**非对称电感膜片 (图 5.29b, Eq. 5.39):**

$$ \frac{B}{Y_0} = -\frac{2\pi}{\beta a} \cot^2 \frac{\pi d}{2a} \left[ 1 + \csc^2 \frac{\pi d}{2a} \right] $$

**薄圆柱电感柱 (图 5.29c, Eq. 5.40):**

$$ \frac{B}{Y_0} = -\frac{4\pi}{\beta a} \left( \frac{t}{a} \right) \sum_{n=2}^\infty \frac{\sin^2 \frac{n\pi x_0}{a}}{\gamma_n a} $$

**小圆孔 (图 5.29d, Eq. 5.41):**

$$ \frac{B}{Y_0} = -\frac{3ab}{8 \beta r_0^2} $$

### Shunt Capacitive Elements (pp. 341–342)

**非对称电容膜片 (图 5.30a, Eq. 5.42):**

$$ \frac{B}{Y_0} = \frac{2\pi}{\beta b} \ln \csc \frac{\pi d}{2b} \left[ 1 + \frac{\beta b}{2\pi} \left(1 - \cos^2 \frac{\pi d}{2b}\right) \right] $$

**对称电容膜片 (图 5.30b, Eq. 5.43):**

$$ \frac{B}{Y_0} = \frac{4\pi}{\beta b} \ln \csc \frac{\pi d}{2b} \left[ 1 + \frac{\beta b}{4\pi} \left(1 - \cos^4 \frac{\pi d}{2b}\right) \right] $$

### Waveguide Stub Tuners (pp. 342–343)

- **滑动螺钉调谐器 (图 5.31a)：** 可变深度螺钉在宽壁窄槽中滑动，等效于单枝节
- **三螺钉调谐器 (图 5.31b)：** 间距 $3\lambda_g/8$，相当于三枝节调谐器
- **E-H 调谐器 (图 5.31c)：** E 面和 H 面短路线构成的双调谐

---

## §5.9 Quarter-Wave Transformers (pp. 343–347)

### 单节 \lambda/4 变换器

匹配条件 (图 5.32, p. 344)：

$$ Z_2 = \sqrt{Z_1 Z_L} $$

输入阻抗：

$$ Z_{in} = Z_2 \frac{Z_L + j Z_2 \tan \theta}{Z_2 + j Z_L \tan \theta} \tag{5.45} $$

反射系数：

$$ \Gamma = \frac{Z_L - Z_1}{Z_L + Z_1 + j 2 t \sqrt{Z_1 Z_L}} \tag{5.46} $$

$$ \rho = \frac{|Z_L - Z_1|}{\left[ (Z_L + Z_1)^2 + 4 t^2 Z_1 Z_L \right]^{1/2}} \tag{5.47} $$

在 $\theta \approx \pi/2$ 时的近似 (Eq. 5.48, p. 345)：

$$ \rho \approx \frac{|Z_L - Z_1|}{2 \sqrt{Z_1 Z_L}} |\cos \theta| $$

### 带宽 (pp. 345–346)

频带边缘 (Eq. 5.49, p. 345)：

$$ \theta_m = \cos^{-1} \left[ \frac{2 \rho_m \sqrt{Z_1 Z_L}}{|Z_L - Z_1| \sqrt{1 - \rho_m^2}} \right] $$

分数带宽 (Eq. 5.50, p. 346)：

$$ \frac{\Delta f}{f_0} = 2 - \frac{4}{\pi} \theta_m $$

---

## §5.10 Theory of Small Reflections (pp. 347–348)

### 两反射结的精确解 (图 5.34, p. 347)

总反射系数 (Eq. 5.51, p. 348)：

$$ \Gamma = \frac{\Gamma_1 + \Gamma_3 e^{-2j\theta}}{1 + \Gamma_1 \Gamma_3 e^{-2j\theta}} \tag{5.51} $$

### 小反射近似 (Eq. 5.52, p. 348)

当 $|\Gamma_1|, |\Gamma_3| \ll 1$ 时：

$$ \Gamma \approx \Gamma_1 + \Gamma_3 e^{-2j\theta} \tag{5.52} $$

仅需考虑一阶反射。若 $|\Gamma_1| = |\Gamma_3| = 0.2$，误差不超过 4%。

---

## §5.11 Approximate Theory for Multisection Quarter-Wave Transformers (pp. 348–350)

### N 节对称变换器 (图 5.36, p. 349)

各结反射系数 (Eq. 5.53, p. 349)：

$$ \Gamma_0 = \frac{Z_1 - Z_0}{Z_1 + Z_0} = p_0, \quad \Gamma_n = \frac{Z_{n+1} - Z_n}{Z_{n+1} + Z_n} = p_n, \quad \Gamma_N = \frac{Z_L - Z_N}{Z_L + Z_N} = p_N \tag{5.53} $$

总反射系数（一阶近似，式 5.54, p. 349）：

$$ \Gamma = p_0 + p_1 e^{-2j\theta} + p_2 e^{-4j\theta} + \cdots + p_N e^{-2jN\theta} \tag{5.54} $$

### 对称结构的余弦级数形式 (Eqs. 5.55–5.56, p. 350)

若变换器对称（$p_0 = p_N, p_1 = p_{N-1}, \ldots$）：

$$ \Gamma = 2 e^{-jN\theta} \left[ p_0 \cos N\theta + p_1 \cos(N-2)\theta + \cdots \right] \tag{5.56} $$

### 应用

通过选择 $p_n$（从而选择 $Z_n$），可获得不同通带特性。该级数为余弦级数，周期为 $\pi$。以下两节分别给出最大平坦（binomial）和等波纹（Chebyshev）特性的设计。

---

## §5.12 Binomial Transformer (pp. 350–352)

> **PDF 页面 350–352，Collin §5.12**

### 原理

最大平坦通带特性要求在匹配频率 $f_0$（即 $\theta = \pi/2$）处，$\Gamma$ 的前 $N-1$ 阶导数均为零。

通过选择反射系数与 $\cos\theta$ 的 $N$ 次幂成正比来实现：

$$ \Gamma = A 2^{-N} (1 + e^{-2j\theta})^N = A 2^{-N} (2 \cos\theta)^N e^{-jN\theta} \tag{5.57} $$

因此：

$$ |\Gamma| = |A| \cdot |\cos\theta|^N \tag{5.57a} $$

### 常数 $A$ 的确定

在 $\theta = 0$ 或 $\pi$ 时，$\Gamma = (Z_L - Z_0)/(Z_L + Z_0) = A$，因此：

$$ A = \frac{Z_L - Z_0}{Z_L + Z_0} \tag{5.58} $$

### 二项式展开

将式 (5.57) 展开：

$$ \Gamma = A 2^{-N} \sum_{n=0}^N C_n^N e^{-2jn\theta} \tag{5.59} $$

其中二项式系数：

$$ C_n^N = \frac{N!}{n!(N-n)!} $$

### 反射系数与特征阻抗的关系

与式 (5.54) 比较，各结反射系数为：

$$ p_n = A 2^{-N} C_n^N = A 2^{-N} \frac{N!}{n!(N-n)!} \tag{5.60} $$

由于对称性 $p_n = p_{N-n}$，即 $C_n^N = C_{N-n}^N$。

通过逐步计算 $Z_n$：

$$ Z_{n+1} = Z_n \frac{1 + p_n}{1 - p_n} $$

即可确定各节特征阻抗。

### 关键特性

- 通带内 $\theta = \pi/2$ 附近最平坦
- 随 $N$ 增大带宽增加
- 阻抗跳变从两端向中间逐渐变化

---

## §5.13–5.14 Chebyshev Transformer (pp. 352–360)

> **注：** 以下内容基于 Collin 原书的经典 Chebyshev 变换器理论与标准结果。
> 原书 pp. 352–360 包含 Chebyshev 多项式的应用、通带等波纹特性、以及设计图表。

### Chebyshev 多项式

$$ T_n(x) = \begin{cases}
\cos(n \cos^{-1} x) & |x| \le 1 \\
\cosh(n \cosh^{-1} x) & |x| > 1
\end{cases} $$

前几项：
- $T_0(x) = 1$
- $T_1(x) = x$
- $T_2(x) = 2x^2 - 1$
- $T_3(x) = 4x^3 - 3x$
- $T_4(x) = 8x^4 - 8x^2 + 1$

### Chebyshev 变换器的反射系数

令 $x = \cos\theta / \cos\theta_m$，其中 $\theta_m$ 是通带边缘角频率对应的电长度。

$$ \Gamma = A e^{-jN\theta} T_N\left(\frac{\cos\theta}{\cos\theta_m}\right) $$

$$ |\Gamma| = |A| \cdot \left| T_N\left(\frac{\cos\theta}{\cos\theta_m}\right) \right| $$

### 常数 $A$ 的确定

在 $\theta = 0$ 处，$T_N(1/\cos\theta_m) \ne 1$，需满足：

$$ |\Gamma(0)| = |A| \cdot T_N(1/\cos\theta_m) = \left|\frac{Z_L - Z_0}{Z_L + Z_0}\right| $$

因此：

$$ A = \frac{Z_L - Z_0}{Z_L + Z_0} \cdot \frac{1}{T_N(1/\cos\theta_m)} \tag{5.61} $$

### 通带波纹

通带内（$|\cos\theta/\cos\theta_m| \le 1$）的最大反射系数为 $|\Gamma|_m = |A|$。

### 与二项式变换器的对比

- **二项式：** $\theta = \pi/2$ 处最大平坦，远离 $\pi/2$ 时 $\rho$ 迅速增大
- **Chebyshev：** 通带内等波纹，相同节数下带宽更宽（或相同带宽下节数更少）

### 设计步骤

1. 给定 $Z_0$、$Z_L$、允许最大 $\rho_m$、及工作频段
2. 由 $\theta_m$ 和 $N$ 确定 $A$ 满足通带边缘 $\rho = \rho_m$
3. 计算 $p_n$ 通过展开 $T_N(\cos\theta/\cos\theta_m)$ 为 $\cos\theta$ 的级数
4. 由 $p_n = (Z_{n+1} - Z_n)/(Z_{n+1} + Z_n)$ 确定各节阻抗

**标准设计图表** 在 pp. 355–360 给出。

---

## §5.15 Filter Design Based on QWT Prototype (pp. 360–365)

> **注：** 本节展示如何将多节 $\lambda/4$ 变换器设计方法应用于滤波器原型。
> 基于低通原型滤波器的阶梯阻抗变换，通过 Richard 变换（$j\Omega \leftrightarrow j \tan \beta l$）和 Kuroda 恒等式实现从集总参数到分布参数的转换。

### 基本思想

- $\lambda/4$ 线节在 $f_0$ 处长度为 $\lambda/4$，实现阻抗变换
- 多节级联形成带通响应
- 偶奇模分析可用于定向耦合器的设计

### 设计方法

1. 选择滤波器原型（Butterworth 或 Chebyshev 低通）
2. 通过 Richard 变换映射到分布参数域
3. 使用 Kuroda 恒等式将串联短截线转换为并联短截线
4. 确定各节特征阻抗

---

## §5.16 Tapered Transmission Lines (pp. 365–370)

> **注：** 以下内容基于 Collin 原书 pp. 365–370 的渐变线理论。渐变线是 $\lambda/4$ 变换器在 $N \to \infty$ 时的极限情形。

### 基本原理

渐变线（tapered line）的特征阻抗沿长度连续变化：$Z(z)$，$0 \le z \le L$。

### 小反射近似

每单位长度的微分反射系数：

$$ d\Gamma = \frac{1}{2} \frac{d}{dz}[\ln Z(z)] e^{-2j\beta z} dz $$

总反射系数：

$$ \Gamma = \frac{1}{2} \int_0^L e^{-2j\beta z} \frac{d}{dz} [\ln Z(z)] \, dz $$

### 常用渐变线类型

**1. 线性渐变线 （Linear taper）**

$$ Z(z) = Z_0 + (Z_L - Z_0) \frac{z}{L} $$

**2. 指数渐变线 （Exponential taper）**

$$ Z(z) = Z_0 e^{(z/L) \ln(Z_L/Z_0)} $$

**3. Klopfenstein 渐变线 （Klopfenstein taper）**

最优渐变线，在给定长度下实现最小通带反射系数。基于 Chebyshev 等波纹特性。

其导数与修正 Bessel 函数有关：

$$ \frac{d}{dz} \ln Z(z) = \frac{2A}{L} \cdot \frac{I_1(\beta_0\sqrt{1 - (2z/L)^2})}{\beta_0\sqrt{1 - (2z/L)^2}} $$

$$ Z(z) = \sqrt{Z_0 Z_L} \exp\left[ \frac{\Gamma_0}{\cosh A} \cdot A^2 \phi(2z/L, A) \right] $$

其中：
- $\Gamma_0 = \frac{1}{2} \ln(Z_L/Z_0)$
- $A = \cosh^{-1} (\Gamma_0 / \Gamma_m)$
- $\phi(x, A) = \int_0^x \frac{I_1(A\sqrt{1-y^2})}{A\sqrt{1-y^2}} \, dy$

最大通带反射系数 $\Gamma_m$ 由 $A$ 控制。

### 渐变线 vs 阶梯变换器

| 特性 | 阶梯变换器 | 渐变线 |
|------|-----------|--------|
| 物理长度 | $\lambda/4$ 倍数 | 通常 $> \lambda/2$ |
| 带宽 | 有限 | 非常宽（理论上无限） |
| 制造复杂度 | 较低（离散节） | 较高（连续变化） |
| 高频性能 | 周期性响应 | 无周期性响应 |

---

## 参考文献

1. Collin, R. E., *Foundations for Microwave Engineering*, 2nd Ed., McGraw-Hill, 1992.
2. Marcuvitz, N. (ed.), *Waveguide Handbook*, McGraw-Hill, 1951.
3. Cohn, S. B., Optimum Design of Stepped Transmission Line Transformers, *IRE Trans. MTT*, vol. 3, pp. 16–21, April 1955.
4. Klopfenstein, R. W., A Transmission Line Taper of Improved Design, *Proc. IRE*, vol. 44, pp. 31–35, Jan. 1956.
5. Collin, R. E. and Brown, J., The Design of Quarter-Wave Matching Layers for Dielectric Surfaces, *Proc. IEE*, vol. 103, pt. C, pp. 153–158, 1956.
