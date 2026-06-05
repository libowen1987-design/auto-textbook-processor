# Chapter 7: Antenna Synthesis (天线综合)
# 第7章：天线综合
> Balanis, *Antenna Theory: Analysis and Design*, 4th Edition — Chapter 7

---


**分析 (Analysis)**：已知电流分布 → 辐射方向图
**综合 (Synthesis)**：已知期望方向图 → 电流分布

综合问题本质上是一个**逆问题** (inverse problem)。给定一个期望的远场方向图 $F_d(\theta)$，求线源（或阵列）的激励分布 $I(z)$ 使得产生的方向图 $F(\theta)$ 尽可能逼近 $F_d(\theta)$。

综合方法分类：
| 方法 | 适用场景 | 思想 |
|:----|:--------|:----|
| **傅里叶综合** | 任意方向图 | 方向图 = 电流的傅里叶变换 → 反变换得电流 |
| **Woodward-Lawson** | 任意方向图，取样点 | 方向图离散取样 → 叠加余弦分布 |
| **Taylor 综合** | 低旁瓣方向图 | 利用 Taylor 函数控制 SLL 和波束宽度 |
| **Dolph-Chebyshev** | 给定 SLL 的最窄波束 | 切比雪夫多项式 → 等旁瓣方向图 |
| **Fourier 级数/正交** | 线源综合 | 正交展开方向图 |

---


### 连续线源 (Continuous Line Source)

线源沿 $z$ 轴放置，长度为 $L$，电流分布 $I(z)$，$z \in [-L/2, L/2]$。

远场方向图（忽略常数因子）：

$$
F(\theta) = \int_{-L/2}^{L/2} I(z) e^{jkz\cos\theta} dz
$$

量纲检查：$[I(z)] = \text{A}$（电流），$[e^{jkz\cos\theta}] = 1$，$[F] = \text{A}\cdot\text{m}$。实际上通常取归一化电流。

定义空间频率 $u = \frac{L}{\lambda} \cos\theta$，令归一化坐标 $s = 2z/L \in [-1, 1]$：

$$
F(u) = \frac{L}{2} \int_{-1}^{1} I(s) e^{j\pi s u} ds
$$

其中 $u = (L/\lambda)\cos\theta$ 是**无量纲**的空间频率参数。

### 方向图 → 电流（逆变换）

当 $|u|$ 超出一定范围时（可见区），$F(u)$ 被截断。对傅里叶变换，有：

$$
F(u) = \int_{-\infty}^{\infty} I(z) e^{jkz\cos\theta} dz
$$

若电流在 $|z| > L/2$ 处为零，则：

$$
I(z) = \frac{1}{\lambda} \int_{-\infty}^{\infty} F(u) e^{-jkz\cos\theta} du
$$

离散采样后即得到傅里叶级数形式的综合方法。

---


### 原理

将方向图展开为傅里叶级数，利用正交性求解电流分布。对线源：

$$
F(u) = \sum_{m=-\infty}^{\infty} C_m \frac{\sin(\pi u - m\pi)}{\pi u - m\pi}
$$

其中 $C_m$ 就是 $F(u)$ 在取样点 $u = m$ 处的值：

$$
C_m = F(m) = F\left(m\right)
$$

电流分布为：

$$
I(s) = \sum_{m=-M}^{M} C_m e^{-j\pi m s} \quad s \in [-1, 1]
$$

对应方向图：

$$
F(u) = \frac{L}{2} \sum_{m=-M}^{M} C_m \frac{\sin[\pi(u - m)]}{\pi(u - m)}
$$

即方向图由 $\sin c$ 函数（与 $\sinc(\pi x) = \sin(\pi x)/(\pi x)$ 等价）的叠加构成。

### 步骤
1. 确定可见区范围 $u_{\max} = L/\lambda$（对应 $\theta = 0,\pi$）
2. 在 $u = 0, \pm 1, \pm 2, \ldots$ 处取样期望方向图 $F_d(u)$
3. 截断到有限项 $M$（$M$ 由角度分辨率决定）
4. 计算电流系数 $C_m = F_d(u=m)$
5. 重构方向图

### 局限性
- Gibbs 现象：方向图不连续处会出现过冲
- 仅线源（一维）情况直接；二维情况需要双傅里叶级数

---


### 原理

Woodward 和 Lawson 提出了一种灵活的综合方法：将期望方向图在 $u$ 域的离散点 $u = m$（$m = 0, \pm 1, \pm 2, \ldots$）处取样，然后用一组**余弦电流分布** (cosine tapering) 叠加实现。

Woodward-Lawson 的核心思想是：取样点在 $u$ 域上均匀分布间隔为 1，使用 $\operatorname{sinc}$ 型方向图作为基函数，每个基函数由特定的线源分布产生。

### 基函数

$m$ 阶基函数的方向图：

$$
g_m(u) = \frac{\sin[\pi(u - m)]}{\pi(u - m)} \equiv \operatorname{sinc}[\pi(u - m)]
$$

对应的线源电流分布（归一化）：

$$
i_m(s) = e^{-j\pi m s} \quad s \in [-1, 1]
$$

### 综合步骤

1. 在 $u = 0, \pm 1, \pm 2, \ldots, \pm M$ 处取样期望方向图 $F_d(u)$，得到取样值 $F_m = F_d(u = m)$
2. 综合方向图：

$$
F(u) = \sum_{m=-M}^{M} F_m \frac{\sin[\pi(u - m)]}{\pi(u - m)}
$$

3. 综合线源分布：

$$
I(s) = \sum_{m=-M}^{M} F_m e^{-j\pi m s}, \quad s \in [-1, 1]
$$

### 取样点选择

- 可见区 $u \in [-L/\lambda, L/\lambda]$
- $M = \lfloor L/\lambda \rfloor$（向下取整）
- 总取样点数为 $2M+1$

### 优点和局限
| 优点 | 局限 |
|:----|:----|
| 方法简单、直观 | 仅适用于线源 |
| 对主瓣形状保持良好 | 旁瓣区域可能有振荡 |
| 在取样点精确匹配 | 取样点之间可能有误差 |

---


### 7.5.1 Taylor 单参数分布 (nbar = 0)

Taylor 单参数分布产生一个方向图，其旁瓣电平低于某个指定值，但波束宽度展宽。它是 Dolph-Chebyshev 离散阵列和连续线源之间的桥梁。

**电流分布**（单参数）：

$$
I(z) = J_0\left(j\pi B \sqrt{1 - (2z/L)^2}\right) = I_0\left(\pi B \sqrt{1 - (2z/L)^2}\right)
$$

其中 $J_0$ 为零阶贝塞尔函数，$I_0$ 为零阶修正贝塞尔函数。$B$ 是控制旁瓣电平的参数。

**方向图**：

$$
F(\theta) = \frac{\sin\left[\sqrt{(\pi L/\lambda)^2\cos^2\theta - (\pi B)^2}\right]}
{\sqrt{(\pi L/\lambda)^2\cos^2\theta - (\pi B)^2}}
$$

对于 $B=0$（均匀分布），退化为：

$$
F(\theta) = \frac{\sin(\pi L\cos\theta/\lambda)}{\pi L\cos\theta/\lambda}
$$

**SLL 与 $B$ 的关系**：

$$
\text{SLL (dB)} = -10\log_{10}\left(\frac{\sinh^2(\pi B)}{(\pi B)^2}\right) \quad \text{当 } L/\lambda \gg B
$$

简化的反推关系：

$$
B \approx \frac{1}{\pi} \operatorname{arccosh}\left(R_{\text{voltage}}\right) \cdot \frac{1}{\pi}
$$

其中 $R_{\text{voltage}} = 10^{-(\text{SLL dB})/20}$。

**波束展宽因子**：

$$
\sigma = \frac{1}{\sqrt{1 + B^2 / (L/\lambda)^2}}
$$

或更精确的形式由 Taylor 给出。

### 7.5.2 Taylor n-bar 分布

Taylor n-bar 分布通过引入 $\bar{n}$ 个等旁瓣后使随后的旁瓣按 $1/u$ 衰减，从而获得比 Dolph-Chebyshev 更好的能量集中。

**方向图函数**：

$$
F(u) = \frac{\sin(\pi u)}{\pi u} \prod_{n=1}^{\bar{n}-1} \frac{1 - (u/u_n)^2}{1 - (u/n)^2}
$$

其中 $u_n$ 是 Taylor 方向图的零点位置：

$$
u_n = \pm \sigma \sqrt{A^2 + (n - 1/2)^2}, \quad n = 1, 2, \ldots, \bar{n}-1
$$

$$
A = \frac{1}{\pi} \operatorname{arccosh}(R_{\text{voltage}})
$$

$$
\sigma = \frac{\bar{n}}{\sqrt{A^2 + (\bar{n} - 1/2)^2}}
$$

**电流分布**（闭式）：

$$
I(s) = 1 + 2 \sum_{m=1}^{\bar{n}-1} F(u=m) \cos(\pi m s), \quad s \in [-1, 1]
$$

其中 $F(u=m)$ 是目标方向图在 $u = m$ 处的取样值。

### 参数选择
| 参数 | 作用 | 典型值 |
|:----|:----|:------|
| $R$ (电压旁瓣比) | 控制 SLL | $R = 10^{-(\text{SLL dB})/20}$ |
| $\bar{n}$ | 控制等旁瓣个数 | $\bar{n} \geq 2(A^2 + 1/4)$，通常 5-15 |
| $A$ | 中间参数 | $A = \frac{1}{\pi}\operatorname{arccosh}(R)$ |
| $\sigma$ | 展宽因子 | $\sigma > 1$，约 1.0-1.2 |

---


Dolph-Chebyshev 综合为给定旁瓣电平的离散阵列提供**最窄波束**（最优化方向图）。核心思想是利用切比雪夫多项式 $T_m(x)$ 的性质：
- 在 $|x| \leq 1$ 范围内等波纹 (equal ripple)
- 在 $|x| > 1$ 范围内单调增长

**核心方程**：

$$
T_{N-1}(x) \big|_{x = x_0 \cos(\psi/2)} = T_{N-1}\left(x_0 \cos\frac{\psi}{2}\right) = F(\psi) \leq R
$$

其中 $x_0 = \cosh\left(\frac{1}{N-1}\operatorname{arccosh}(R)\right)$。

实现细节已在 Ch6 (`dolph_chebyshev_weights`) 中完成。这里侧重连续线源对应。

### 离散阵列与连续线源的类比

| 离散阵列 | 连续线源 |
|:--------|:--------|
| $N$ 个单元 | 长度 $L$ |
| $d$ 间距 | 采样间隔 |
| $I_n$ 离散电流 | $I(s)$ 连续电流 |
| $F(\psi) = \sum I_n e^{jn\psi}$ | $F(u) = \int I(s) e^{j\pi su} ds$ |
| $Nd \to L$ | 连续极限 |

---


### 7.7.1 最小二乘法

最小化目标方向图和综合方向图之间的均方误差：

$$
\min_{I} \int_{-\pi}^{\pi} |F_d(\psi) - F(\psi)|^2 d\psi
$$

等价于 Fourier 级数展开（截断到前 $N$ 项）。

### 7.7.2 凸优化方法

现代方法：将综合问题建模为凸优化问题（如 MVDR、LCMV）：
- 最小化旁瓣能量
- 约束主瓣增益
- 可在任意位置添加零陷 (nulling)
- 支持多约束（SLL, 主瓣宽度, 阵列稀疏等）

### 7.7.3 Villeneuve 综合

Taylor 综合在离散阵列上的推广，适用于任意单元数的线阵。

---


| 方法 | 旁瓣控制 | 波束宽度 | 实现难度 | 适用范围 |
|:----|:--------:|:--------:|:--------:|:--------:|
| **Fourier** | 差 | 窄 | 低 | 任意方向图 |
| **Woodward-Lawson** | 中 | 中 | 低 | 线源 |
| **Taylor (1-param)** | 好 | 稍宽 | 中 | 连续线源 |
| **Taylor (n-bar)** | 优 | 近最优 | 中 | 连续线源 |
| **Dolph-Chebyshev** | 优（等波纹） | 最窄 | 中 | 离散阵列 |
| **凸优化** | 可控 | 可控 | 高 | 任意阵列 |

---

## References

- Balanis, C. A. "Antenna Theory: Analysis and Design", 4th ed., Chapter 7
- Woodward, P. M. & Lawson, J. D. "The Theoretical Precision with which an Arbitrary Radiation Pattern may be Obtained from a Source of Finite Size", *J.IEE*, 1948
- Taylor, T. T. "Design of Line-Source Antennas for Narrow Beamwidth and Low Side Lobes", *IRE Trans. AP*, 1955
- Dolph, C. L. "A Current Distribution for Broadside Arrays Which Optimizes the Relationship between Beam Width and Side-Lobe Level", *Proc. IRE*, 1946
