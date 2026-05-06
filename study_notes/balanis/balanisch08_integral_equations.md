# Chapter 8: Integral Equations, Method of Moments

> Balanis, *Antenna Theory: Analysis and Design*, 4th Edition — Chapter 8

---

## 8.1 Introduction

### 积分方程 vs 微分方程

| 特征 | 积分方程 (IE) | 微分方程 (DE) |
|:----|:-------------|:--------------|
| 定义域 | 整个问题域（全局） | 每个点局部 |
| 边界条件 | 隐含在核函数中 | 显式附加 |
| 数值离散 | 只离散导体表面（降维） | 离散整个空间域 |
| 开域问题 | 自动满足辐射条件 | 需附加吸收边界 |
| 矩阵填充 | 稠密矩阵 $O(N^2)$ | 稀疏矩阵 $O(N)$ |
| 典型方法 | MoM, BEM | FEM, FDTD |

**为什么要用 IE？** 对线天线和导体散射体，辐射/散射场由**表面电流/电荷分布**决定。积分方程直接在导体表面建立方程（1D 线 → 2D 面），相比 DE 在三维空间离散大幅降低自由度。

### MoM 核心思想

Method of Moments (MoM) 是将连续积分方程离散为线性代数方程组的方法：

1. 将未知函数展开为一组基函数的线性组合
2. 选取一组权函数，令残差在加权积分意义下为零
3. 得到 $N \times N$ 线性方程组 $[Z][I] = [V]$

---

## 8.2 Integral Equation Formulation for Wire Antennas

### 8.2.1 矢量位与标量位

对于一个沿 $z$ 轴放置的细线天线，电流密度 $\mathbf{J}$ 仅沿 $z$ 方向。磁矢量位：

$$
A_z(z) = \frac{\mu_0}{4\pi} \int_{-l/2}^{l/2} I(z') \frac{e^{-jkR}}{R} dz'
$$

量纲：$[A_z] = \text{Wb/m}$，$[\mu_0 I dz' / (4\pi R)] = \text{H/m} \cdot \text{A} \cdot \text{m} / \text{m} = \text{Wb/m}$ ✓

其中 $R = \sqrt{(z - z')^2 + a^2}$，$a$ 为导线半径。

> **物理直觉：** 这是惠更斯原理的体现——线元 $dz'$ 上的电流 $I(z')$ 产生的矢量位在场点 $z$ 处球面波叠加。$a$ 避免奇点（观测点在线上，但电流在轴线上，场在表面）。

### 8.2.2 Pocklington 积分方程

从矢量位出发，电场与矢量位的关系：

$$
E_z = -j\omega A_z - \frac{\partial \Phi}{\partial z} = \frac{1}{j\omega\mu_0\epsilon_0} \left( \frac{\partial^2 A_z}{\partial z^2} + k^2 A_z \right)
$$

在导体表面总切向电场为零（PEC 边界条件）：

$$
E_z^{\text{inc}} + E_z^{\text{scat}} = 0 \quad \Rightarrow \quad E_z^{\text{inc}} = -E_z^{\text{scat}}
$$

代入 $A_z$ 表达式，得到 **Pocklington 积分方程**：

$$
E_z^{\text{inc}}(z) = \frac{1}{j\omega\epsilon_0} \int_{-l/2}^{l/2} I(z') \left[ \frac{\partial^2}{\partial z^2} + k^2 \right] \frac{e^{-jkR}}{4\pi R} dz'
$$

量纲：$[E] = \text{V/m}$，$[I] = \text{A}$，$[\frac{1}{\omega\epsilon_0} \cdot \frac{\partial^2}{\partial z^2} \cdot \frac{e^{-jkR}}{4\pi R}] = [\eta \cdot \frac{1}{k} \cdot \frac{1}{m^2} \cdot \frac{1}{m}] = \text{V/m} / \text{A}$ ✓

展开微分算子后得到实用形式：

$$
E_z^{\text{inc}}(z) = \frac{-j\eta}{4\pi k} \int_{-l/2}^{l/2} I(z') \left[ \frac{(1 + jkR)(2R^2 - 3a^2) + k^2 a^2 R^2}{R^5} \right] e^{-jkR} dz'
$$

其中 $\eta = \sqrt{\mu_0/\epsilon_0}$，$R = \sqrt{(z - z')^2 + a^2}$，核函数包含 $1/R$ 和 $1/R^3$ 项。

> **物理直觉：** 当 $R \to 0$ 时 $1/R^3$ 剧烈发散，这是细线模型的奇点问题。实操中取 $a > 0$（有限半径）和去奇点技术来保持数值稳定。

#### 简化形式（薄线近似）

当 $a \ll \lambda$ 且 $a \ll l$，$\partial^2/\partial z^2$ 可移出积分：

$$
E_z^{\text{inc}}(z) = \frac{1}{j4\pi\omega\epsilon_0} \left[ \frac{d^2}{dz^2} + k^2 \right] \int_{-l/2}^{l/2} I(z') \frac{e^{-jkR}}{R} dz'
$$

> **物理直觉：** 此形式将一个线积分 + 微分算子分离——先做积分（求矢量位），再对 $z$ 求导得到电场。数值实现更灵活。

### 8.2.3 Hallén 积分方程

Hallén 方程是从波动方程出发的另一种积分方程形式。

对 $A_z$ 满足 Helmholtz 方程：

$$
\frac{d^2 A_z}{dz^2} + k^2 A_z = -j\omega\mu_0\epsilon_0 E_z^{\text{inc}}
$$

在 $|z| \le l/2$ 上，齐次解 + 特解形式。最终得到 **Hallén 积分方程**：

$$
\int_{-l/2}^{l/2} I(z') \frac{e^{-jkR}}{4\pi R} dz' = C_1 \cos(kz) + C_2 \sin(kz) + \frac{j}{2\eta} \int_0^z E_z^{\text{inc}}(z') \sin[k(z - z')] dz'
$$

对于对称激励（中心馈电的偶极子），$C_2 = 0$：

$$
\int_{-l/2}^{l/2} I(z') \frac{e^{-jkR}}{4\pi R} dz' = C_1 \cos(kz) + \frac{j}{2\eta} \int_0^z E_z^{\text{inc}}(z') \sin[k(z - z')] dz'
$$

> **物理直觉：** Hallén 的核函数仅含 $e^{-jkR}/R$，比 Pocklington 弱（没有 $1/R^3$ 项），数值积分更容易。代价是需要确定两个积分常数 $C_1, C_2$，需附加边界条件。

### Pocklington vs Hallén 对比

| 特征 | Pocklington | Hallén |
|:----|:-----------|:-------|
| 核函数 | $1/R + 1/R^3$ | $1/R$ |
| 奇异性 | 强 (Cauchy) | 弱 (可积) |
| 数值积分 | 需去奇点技术 | 直接积分可行 |
| 未知常数 | 无 | 2 个 ($C_1, C_2$) |
| 激励模型 | 直接 $E^{\text{inc}}$ | 间接 |
| 适用性 | 通用 | 细线天线为主 |

---

## 8.3 Method of Moments Solution

### 8.3.1 一般框架

积分方程可以写为算子形式：

$$
\mathcal{L}(I) = V
$$

其中 $\mathcal{L}$ 是线性积分算子，$I(z')$ 是未知电流，$V$ 是已知激励。

将 $I(z')$ 展开为基函数 $\{f_n\}$ 的线性组合：

$$
I(z') \approx \sum_{n=1}^{N} I_n f_n(z')
$$

代入算子方程，定义残差 $r(z) = \mathcal{L}(\sum I_n f_n) - V$。选取权函数 $\{w_m\}$ 令加权残差为零：

$$
\langle w_m, r \rangle = \int w_m(z) r(z) dz = 0 \quad m = 1, 2, \dots, N
$$

得到 $N \times N$ 线性方程组：

$$
\sum_{n=1}^{N} Z_{mn} I_n = V_m
$$

其中：

$$
Z_{mn} = \langle w_m, \mathcal{L}(f_n) \rangle = \int_{-l/2}^{l/2} w_m(z) \left[ \frac{\partial^2}{\partial z^2} + k^2 \right] \frac{e^{-jkR_{mn}}}{4\pi R_{mn}} dz
$$

$$
V_m = \langle w_m, V \rangle = \int_{-l/2}^{l/2} w_m(z) E_z^{\text{inc}}(z) dz
$$

### 8.3.2 基函数 (Basis Functions)

| 基函数类型 | 表达式 | 特点 | 适用场景 |
|:-----------|:-------|:-----|:---------|
| **脉冲 (Pulse)** | $f_n(z) = \begin{cases} 1 & z \in [z_n - \Delta/2, z_n + \Delta/2] \\ 0 & \text{else} \end{cases}$ | 最简单，分段常数 | 点匹配快速估算 |
| **三角 (Triangle)** | $f_n(z) = \begin{cases} 1 - \frac{|z - z_n|}{\Delta} & |z - z_n| \le \Delta \\ 0 & \text{else} \end{cases}$ | 连续，导数分段常数 | Galerkin 匹配 |
| **正弦 (Sinusoidal)** | $f_n(z) = \begin{cases} \frac{\sin k(z - z_{n-1})}{\sin k\Delta} & z \in [z_{n-1}, z_n] \\ \frac{\sin k(z_{n+1} - z)}{\sin k\Delta} & z \in [z_n, z_{n+1}] \\ 0 & \text{else} \end{cases}$ | 满足波动方程性质 | 细线精确计算 |
| **全域 (Entire-domain)** | $f_n(z) = \sin\left[\frac{n\pi}{l}(z + l/2)\right]$ | 光滑，收敛快 | 简单结构（偶极子） |

> **物理直觉：** 基函数是电流沿导线的"形状模板"。脉冲基像分段常数楼梯，三角基像线性插值，正弦基像小段驻波。密集度越高（$N$ 越大），逼近越精确，但矩阵越大。

### 8.3.3 权函数 (Weighting / Testing Functions)

| 权函数类型 | 表达式 | 特点 |
|:-----------|:-------|:-----|
| **点匹配 (Point Matching)** | $w_m(z) = \delta(z - z_m)$ | 只在一个点检验，矩阵填充最快 |
| **Galerkin** | $w_m(z) = f_m(z)$ | 与基函数相同，矩阵对称，精度最高 |
| **最小二乘** | $w_m(z) = \frac{\partial r}{\partial I_m}$ | 残差平方和最小，计算量大 |

### 8.3.4 阻抗矩阵元素计算

#### 点匹配 + 脉冲基

对 Pocklington 方程，点匹配 $w_m(z) = \delta(z - z_m)$：

$$
Z_{mn} = -\frac{j\eta}{4\pi k} \left[ \frac{(1 + jkR)(2R^2 - 3a^2) + k^2 a^2 R^2}{R^5} \right] e^{-jkR} \cdot \Delta_n
$$

其中 $R = \sqrt{(z_m - z_n)^2 + a^2}$，$\Delta_n$ 为第 $n$ 段的长度。

$$
V_m = E_z^{\text{inc}}(z_m) \approx \frac{V_0}{\Delta_m}
$$

对于 delta-gap 馈电模型，$V_m = 1$（归一化，仅在馈电段非零）。

#### 阻抗矩阵对称性

**互易定理**保证 $Z_{mn} = Z_{nm}$（对 Galerkin 精确成立，点匹配近似成立）。利用此性质只需计算上三角矩阵。

### 8.3.5 去奇点技术 (Singularity Treatment)

当 $m = n$ 时，$R = a$（导线半径），核函数剧烈变化。

**方法一：减奇异法 (Subtract-out Singularity)**

$$
\int f_n(z') K(z_m, z') dz' = \int f_n(z') [K(z_m, z') - K_s(z_m, z')] dz' + \int f_n(z') K_s(z_m, z') dz'
$$

其中 $K_s$ 选取可解析积分的奇性近似。

**方法二：细分积分区间**

将 $m = n$ 段再细分为子段，用高精度 Gauss-Legendre 积分处理。

**方法三：解析近似**

对 $m = n$ 使用自阻抗解析公式：

$$
Z_{mm} \approx \frac{\eta \Delta}{4\pi} \left[ 1 - j\frac{2}{\pi} \ln\left(\frac{ka}{2}\right) - \frac{2}{\pi} \right] \quad \text{(近似)}
$$

---

## 8.4 Current Distribution and Impedance

### 8.4.1 偶极子电流分布

通过 MoM 求解 $[Z][I] = [V]$ 得到各段的电流系数 $\{I_n\}$。

**关键结果：**
- $l = \lambda/2$：接近正弦分布 $I(z) \approx I_0 \sin[k(l/2 - |z|)]$
- $l = \lambda$：电流在中心反相，中间有零点
- $l = 1.5\lambda$：更复杂的分布，出现多个驻波节点

> **物理直觉：** 电流分布是传输线驻波与天线上行波的叠加。$\lambda/2$ 偶极子接近理想正弦，但 MoM 结果包含有限半径、末端效应等修正。

### 8.4.2 输入阻抗

$$
Z_{\text{in}} = \frac{1}{I_{\text{feed}}}
$$

归一化激励 $V_{\text{feed}} = 1$，所以 $Z_{\text{in}} = 1 / I_{\text{feed}}$。

$Z_{\text{in}}$ 随 $l/\lambda$ 振荡：
- $l/\lambda \approx 0.5$：$Z_{\text{in}} \approx 73 + j42.5\ \Omega$
- $l/\lambda \approx 0.5$ (调整长度至谐振)：$Z_{\text{in}} \approx 73\ \Omega$
- $l/\lambda \approx 1.0$：$Z_{\text{in}}$ 很大（接近开路）
- $l/\lambda \approx 1.5$：再次出现低阻区

---

## 8.5 Mutual Impedance

### 8.5.1 两个平行偶极子

天线 1 馈电，天线 2 开路。通过 MoM 建立耦合方程：

$$
\begin{bmatrix}
Z_{11} & Z_{12} \\
Z_{21} & Z_{22}
\end{bmatrix}
\begin{bmatrix}
I_1 \\
I_2
\end{bmatrix}
=
\begin{bmatrix}
V_1 \\
V_2
\end{bmatrix}
$$

互阻抗 $Z_{21} = V_2 / I_1\big|_{I_2=0}$ 可通过 MoM 互阻抗矩阵元素直接读出。

**互阻抗特性：**
- $d \to 0$（并列）：$Z_{21} \to Z_{11}$（相同天线）
- $d \to \infty$：$Z_{21} \to 0$
- $d$ 为 $\lambda/2$ 倍数时互阻振荡变化

> **物理直觉：** 互阻抗是天线的电磁耦合度量。近距耦合强（$Z_{21} \sim Z_{11}$），随距离振荡衰减。对于阵列设计，互耦影响单元阻抗和方向图，不可忽略。

### 8.5.2 E 面和 H 面耦合

- **E 面耦合**（天线并排，电流平行）：强耦合
- **H 面耦合**（天线首尾对齐）：弱耦合

---

## 8.6 Radiation Patterns

### 8.6.1 从 MoM 电流计算远场

已知 MoM 求解的电流分布 $I(z')$，远场方向图通过辐射积分：

$$
E_\theta(\theta) = j\eta \frac{e^{-jkr}}{2\lambda r} \sin\theta \int_{-l/2}^{l/2} I(z') e^{jkz' \cos\theta} dz'
$$

量纲：$[E_\theta] = \text{V/m}$，$[\eta I e^{-jkr}/(\lambda r) \cdot \text{length}] = \Omega \cdot \text{A} / \text{m} = \text{V/m}$ ✓

对离散段：

$$
E_\theta(\theta) \approx j\eta \frac{e^{-jkr}}{2\lambda r} \sin\theta \sum_{n=1}^{N} I_n \int_{\Delta z_n} e^{jkz' \cos\theta} dz'
$$

### 8.6.2 MoM 方向图 vs 理想正弦近似

| 特征 | MoM 电流 | 理想正弦近似 |
|:----|:---------|:------------|
| 末端效应 | 包含 | 假设 $I(l/2) = 0$（理想） |
| 半径影响 | 包含 | 假设 $a = 0$ |
| 馈电区细节 | 包含 | 假设 delta-gap |
| 旁瓣 | 精确 | 近似 |

> **物理直觉：** 对于半波偶极子，两种结果几乎重合。随长度增加，MoM 的末端效应和有限半径修正变得显著，尤其在大长度比时方向图差异明显。

---

## 8.7 MoM for Microstrip Antennas

### 8.7.1 贴片天线的 MoM 建模

微带贴片天线建模为薄导体贴片在接地介质基板上。MoM 应用于贴片表面电流。

**关键步骤：**
1. 使用**空域格林函数**（包含介质基板效应）
2. 贴片电流展开为**整域基函数**（腔模）或**分域基**（Rao-Wilton-Glisson RWG 基函数）
3. 阻抗矩阵包含介质层的 Sommerfeld 积分

### 8.7.2 挑战

- **格林函数复杂性**：需数值计算 Sommerfeld 积分（沿实轴或最陡下降路径）
- **表面波激励**：介质基板支持 TM$_0$ 表面波模式
- **馈电建模**：探针馈电/微带线馈电/共面波导馈电各有不同的激励模型

> **物理直觉：** 微带 MoM 比自由空间线天线复杂一个量级——格林函数不再是简单的 $e^{-jkR}/4\pi R$，而包含无限个反射和表面波项。

---

## 8.8 MoM for Large Structures

### 8.8.1 大规模 MoM 的挑战

传统的 MoM 矩阵是稠密的，存储复杂度 $O(N^2)$，求解复杂度 $O(N^3)$（直接法）或 $O(N_{\text{iter}} N^2)$（迭代法）。

对于 $N > 10^4$ 的问题，传统 MoM 不可行。

### 8.8.2 分域基 (Subdomain Basis)

将大型结构分解为多个子区域，每个子区域上定义本地基函数。相比整域基：
- 矩阵更稀疏（远区耦合弱）
- 适合复杂几何
- 基函数数量更多但每个计算更快

### 8.8.3 快速多极子方法 (FMM / MLFMA)

**核心思想：** 将阻抗矩阵分解为近区（直接计算）和远区（聚合-转移-配置三步）。

$$
Z = Z_{\text{near}} + Z_{\text{far}}
$$

- **近区**：直接计算（小矩阵）
- **远区**：通过多极子展开做群-群交互

**计算复杂度：**
| 方法 | 存储 | 每次迭代 |
|:----|:----|:---------|
| 传统 MoM | $O(N^2)$ | $O(N^2)$ |
| FMM | $O(N^{1.5})$ | $O(N^{1.5})$ |
| MLFMA | $O(N \log N)$ | $O(N \log N)$ |

> **物理直觉：** MLFMA 就像组织军队通信——每个人不需要跟所有人都通话，只需同小队直接通信（近区），小队之间通过指挥官中转（聚合-转移-配置）。$N$ 个人的复杂度从 $N^2$ 降到 $N\log N$。

### 8.8.4 常用大规模求解方法

| 方法 | 复杂度 | 适用问题 |
|:----|:------|:--------|
| MLFMA | $O(N \log N)$ | 一般散射/辐射 |
| ACA (Adaptive Cross Approximation) | $O(N \log N)$ | 低秩远区矩阵压缩 |
| H-Matrix | $O(N \log N)$ | 分层矩阵分解 |
| FFT-based methods | $O(N \log N)$ | 规则网格结构 |

---

## 8.9 Summary

本章核心体系：

```
物理问题（线天线辐射）
    ↓
Pocklington / Hallén 积分方程
    ↓
MoM 离散（基函数 + 权函数）
    ↓
线性方程组 [Z][I] = [V]
    ↓
电流分布 → 输入阻抗 / 方向图
```

| 概念 | 要点 |
|:----|:----|
| Pocklington IE | 核函数含 $1/R^3$，强奇异，需去奇点 |
| Hallén IE | 核函数 $1/R$，弱奇异，需积分常数 |
| 基函数 | 脉冲/三角/正弦/全域 — 精度 vs 效率权衡 |
| 权函数 | 点匹配（快）vs Galerkin（对称、精确） |
| $Z_{mn}$ 计算 | 奇点处理是 MoM 实现的核心难点 |
| 对称性 | $Z_{mn} = Z_{nm}$ 加速填充 |
| 大规模 | MLFMA 将 $O(N^2)$ 降至 $O(N \log N)$ |

---

## References

1. Balanis, C. A., *Antenna Theory: Analysis and Design*, 4th ed., Wiley, 2016, Ch. 8.
2. Harrington, R. F., *Field Computation by Moment Methods*, IEEE Press, 1993.
3. Gibson, W. C., *The Method of Moments in Electromagnetics*, 2nd ed., CRC Press, 2015.
4. Chew, W. C., et al., *Fast and Efficient Algorithms in Computational Electromagnetics*, Artech House, 2001.
