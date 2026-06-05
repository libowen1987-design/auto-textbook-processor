# Chapter 6: Arrays — Linear, Planar, and Circular
# 第6章：天线阵
> Balanis, *Antenna Theory: Analysis and Design*, 4th Edition — Chapter 6

---

## 6.1 Introduction

单个天线元的方向性有限。通过将多个单元按一定规律排列并馈以适当的幅度和相位，可以实现：
- 高方向性（窄波束）
- 波束电扫描（相控阵）
- 低/可控旁瓣
- 多波束、自适应零点

**核心概念：方向图乘积 (Pattern Multiplication)**
$$
F(\theta, \phi) = \text{EF}(\theta, \phi) \times \text{AF}(\theta, \phi)
$$

其中 EF 是单元因子，AF 是阵列因子。

---

## 6.2 Two-Element Array
## 二元阵

### 阵列因子

两个各向同性单元，间距 $d$，相位差 $\beta$：

$$
\text{AF} = 1 + e^{j(kd\cos\theta + \beta)} = 2\cos\left[\frac{1}{2}(kd\cos\theta + \beta)\right]
$$

归一化功率方向图：
$$
F_n(\theta) = \cos^2\left[\frac{1}{2}(kd\cos\theta + \beta)\right]
$$

### 三种常见情况

| 条件 | 相位差 $\beta$ | 方向图特征 |
|:----:|:--------------:|:----------:|
| **边射阵 (Broadside)** | $0$ | 最大辐射垂直于阵列轴向 |
| **端射阵 (Endfire)** | $-kd$ | 最大辐射沿阵列轴向 |
| **其他** | 任意 | 波束可控 |

### 关键参数

- 阵列因子零点位置：$\theta_n = \arccos\left[\frac{-\beta \pm (2n+1)\pi}{kd}\right]$
- HPBW 与 $d$ 和 $\beta$ 有关
- 方向性：$D \approx 2$（两单元）

---

## 6.3 N-Element Linear Array — Uniform Amplitude

### 阵列因子

N 个等间距、等幅、线性相位递进的单元：

$$
\text{AF} = \sum_{n=0}^{N-1} e^{jn\psi}, \quad \psi = kd\cos\theta + \beta
$$

### 闭式表达式

$$
\text{AF} = \frac{\sin(N\psi/2)}{\sin(\psi/2)} e^{j(N-1)\psi/2}
$$

归一化幅度：
$$
\text{AF}_n = \frac{\sin(N\psi/2)}{N\sin(\psi/2)}
$$

### 方向图特征

| 参数 | 公式 |
|:----|:----|
| 主瓣位置 | $\psi = 0 \Rightarrow \theta_{\text{max}} = \arccos(-\beta/kd)$ |
| 零点位置 | $\psi = 2\pi n/N, n=1,2,\ldots$ |
| 旁瓣位置 | $\psi = \pi(2n+1)/N$ 附近 |
| 第一旁瓣电平 (ULA) | $-13.46$ dB (相对于主瓣) |
| HPBW（边射阵） | $\text{HPBW} \approx 0.886 / (Nd/\lambda)$ [rad] |
| HPBW（端射阵） | $\text{HPBW} \approx 1.08 / \sqrt{Nd/\lambda}$ [rad] |

### 方向性

$$
D_0 = \frac{|\text{AF}_{\max}|^2}{\frac{1}{2}\int_0^\pi |\text{AF}_n|^2 \sin\theta\, d\theta}
$$

近似公式（大 $N$）：
- 边射阵：$D_0 \approx 2Nd/\lambda$
- 端射阵（Hansen-Woodyard）：$D_0 \approx 4Nd/\lambda$

---

## 6.4 N-Element Linear Array — Nonuniform Amplitude

### 为什么要非均匀幅度？

均匀幅度（ULA）的第一旁瓣 -13.46 dB 在很多应用中不够低。通过幅度锥削（taper），可抑制旁瓣至 -20 到 -60 dB，代价是 HPBW 展宽和方向性降低。

### 常见幅度分布

| 分布 | 幅度 $a_n$ | 第一旁瓣 | HPBW 展宽 | 方向性损失 |
|:----|:----------:|:--------:|:---------:|:---------:|
| **Uniform** | 1 | -13.46 dB | 1× (基准) | 0 dB |
| **Triangular** | $1 - 2\|n\|/N$ | -26.5 dB | 1.33× | ~1.3 dB |
| **Cosine** | $\cos[\pi n / (N+1)]$ | -23 dB | 1.29× | ~1.1 dB |
| **Hanning** | $0.5 + 0.5\cos(2\pi n/N)$ | -31.5 dB | 1.44× | ~1.8 dB |
| **Hamming** | $0.54 + 0.46\cos(2\pi n/N)$ | -42.6 dB | 1.36× | ~1.4 dB |
| **Blackman** | $0.42 + 0.5\cos(2\pi n/N) + 0.08\cos(4\pi n/N)$ | -58.1 dB | 1.51× | ~2.1 dB |
| **Dolph-Chebyshev** | 可调旁瓣级 | 指定值 | 最小展宽 | 最小损失 |

### Dolph-Chebyshev 分布

**核心思想：** 在给定旁瓣级下，获得最窄的 HPBW。

阵列因子用 Chebyshev 多项式表示：
$$
\text{AF}_n(\psi) = \frac{T_{N-1}(x_0\cos\psi/2)}{T_{N-1}(x_0)}
$$

其中 $T_m$ 是 m 阶 Chebyshev 多项式，$x_0 = \cosh\left[\frac{1}{N-1}\operatorname{arccosh}(R)\right]$，
$R$ 是主瓣/旁瓣幅度比。

---

## 6.5 Mutual Coupling in Arrays

### 互耦效应

相邻单元间的电磁耦合会导致：
- 单元方向图畸变（非孤立单元 "
- 阻抗偏移（扫描盲点）
- 阵列方向图误差

### 扫描盲点 (Scan Blindness)

在相控阵中，当波束扫描到某个角度时，表面波谐振导致所有能量被束缚而无法辐射。这是互耦引起的**极端效应**。

### 工程缓解

- 单元间距选择避免表面波谐振
- 使用宽带单元（如 Vivaldi）
- 电磁带隙结构 (EBG) / 去耦网络
- 校准矩阵补偿

---

## 6.6 Planar Array
## 平面阵

### 矩形网格阵列

$$
\text{AF}(\theta, \phi) = \sum_{n=0}^{N_x-1} \sum_{m=0}^{N_y-1} w_{nm} e^{j[(n-0.5)k d_x \sin\theta\cos\phi + (m-0.5)k d_y \sin\theta\sin\phi]}
$$

### 阵列因子的可分离性

若 $w_{nm} = a_n b_m$：
$$
\text{AF} = \left[\sum_n a_n e^{jknd_x\sin\theta\cos\phi}\right] \cdot \left[\sum_m b_m e^{jkmd_y\sin\theta\sin\phi}\right]
$$

即：二维矩形阵列因子 = 两个正交一维阵列因子的乘积。

### HPBW 近似

$$
\Theta_{3\text{dB}} \approx \frac{0.886\lambda}{N_x d_x \cos\theta_0} \quad (\text{E-plane})
$$

### 方向性

$$
D_0 = \pi \cos\theta_0 D_x D_y
$$

其中 $D_x$、$D_y$ 是正交方向的方向性，$\theta_0$ 是扫描角。

---

## 6.7 Circular Array

### 环形阵列

单元均匀分布在半径为 $a$ 的圆周上：

$$
\text{AF}(\theta, \phi) = \sum_{n=0}^{N-1} I_n e^{j[ka\sin\theta\cos(\phi-\phi_n) + \alpha_n]}
$$

其中 $\phi_n = 2\pi n/N$，$\alpha_n$ 是可控相位。

### 特点

- 全向扫描能力 (360°)
- 方向图在环平面内对称
- 扫描时 HPBW 几乎不变（相比线阵）

---


| 概念 | 要点 |
|:----|:------|
| 方向图乘积 | EF × AF → 对阵中单元为 E 场相乘 |
| 边射阵 | $\beta=0$，最大辐射垂直阵列轴向 |
| 端射阵 | $\beta=-kd$，波束沿轴向 |
| ULA 旁瓣 | 第一旁瓣恒为 -13.46 dB（无论 N 多大） |
| 幅度锥削 | 旁瓣 ↔ 波束宽度 的折中 |
| Dolph-Chebyshev | 给定旁瓣级下的最优分布 |
| 互耦 | 导致扫描盲点，需小心设计 |
| 平面阵 | AF 可分离（矩形网格），方向图分析简便 |
| 环形阵 | 360° 扫描能力，HPBW 恒定 |

---


- C. A. Balanis, *Antenna Theory*, 4th ed., Wiley, 2016, Ch. 6.
- R. S. Elliott, *Antenna Theory and Design*, IEEE Press, 2003.
- C. L. Dolph, "A Current Distribution for Broadside Arrays," *Proc. IRE*, vol. 34, pp. 335–348, 1946.
- W. W. Hansen and J. R. Woodyard, "A New Principle in Directional Antenna Design," *Proc. IRE*, vol. 26, pp. 333–345, 1938.
- R. J. Mailloux, *Phased Array Antenna Handbook*, 3rd ed., Artech House, 2018.
