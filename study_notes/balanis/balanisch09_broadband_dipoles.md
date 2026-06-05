# Balanis Ch9: Broadband Dipoles and Matching Techniques

> **核心思想**：标准半波偶极子 Q 值高（~10-20），阻抗带宽仅 ~5-10%。展宽带宽的原理在于降低 Q 值——增大导体体积以降低近场储能密度，或增加辐射电阻。本章系统介绍宽带偶极子的物理机理、设计方法及匹配技术。

**章节目录**（Balanis 4th Ed.）：
- §9.1 Introduction
- §9.2 Biconical Antenna
- §9.3 Triangular Sheet, Bow-Tie, and Wire Simulation
- §9.4 Cylindrical Dipole
- §9.5 Folded Dipole
- §9.6 Sleeve Dipole
- §9.7 Matching Techniques for Dipole Antennas
- §9.8 Discone and Conical Skirt Monopoles
- §9.9 Self-Complementary Antennas
- §9.10 Broadband Characteristics of Some Other Antennas

---

## §9.1 Introduction

### 宽带化的基本物理原理

偶极子天线的 Q 值决定了其阻抗带宽：

$$
Q = \frac{2\omega W_{\text{stored}}}{P_{\text{rad}}} \qquad \text{[dimensionless]}
$$

其中 $W_{\text{stored}}$ 是近场储能时间平均值，$P_{\text{rad}}$ 是辐射功率。对于匹配负载：

$$
\text{BW} \approx \frac{s-1}{Q\sqrt{s}} \quad \text{(VSWR < s)}
$$

对于 VSWR < 2（$s=2$）：

$$
\boxed{\text{BW} \approx \frac{1}{Q\sqrt{2}}}
$$

**降低 Q 值的三条路径**：

| 方法 | 物理机理 | 实现方式 |
|:----:|:--------:|:--------:|
| 增大导体体积 | 降低近场储能密度 | 双锥天线、粗圆柱偶极子 |
| 增加辐射电阻 | $Q \propto 1/R_r$ | 折叠偶极子 |
| 多谐振结构 | 多个谐振点展宽总带宽 | 套筒偶极子、传输线变压器 |

---

## §9.2 Biconical Antenna

### 9.2.1 结构与 TEM 波传输线模型

双锥天线由两个同轴圆锥导体构成，顶点相对、馈电点位于顶点间隙。

```
      \       /
       \ θ_h /    θ_h: 半锥角
        \   /
         \●/<-- 馈电点
         / \
        /   \
       /     \
      /       \
```

**核心洞察**：双锥天线可以看作一段**锥形 TEM 传输线**。在无限双锥中，TEM 球面波在两个锥面之间传播，等相位面为球面。

### 9.2.2 无限双锥的特性阻抗

对于 TEM 球面波，在球坐标系 $(\theta, \phi)$ 中：

电场仅存在 $\theta$ 分量，磁场仅存在 $\phi$ 分量：

$$
\mathbf{E} = \hat{\boldsymbol{\theta}} E_\theta, \quad \mathbf{H} = \hat{\boldsymbol{\phi}} H_\phi
$$

E 与 H 的关系由麦克斯韦方程组推导。引入电压和电流：

$$
V(r) = \int_{\theta_h}^{\pi-\theta_h} E_\theta r \, d\theta = (2 \eta_0 H_\phi r) \ln\left(\cot\frac{\theta_h}{2}\right)
$$

$$
I(r) = \oint_0^{2\pi} H_\phi r \sin\theta \, d\phi = 2\pi r H_\phi \sin\theta
$$

**特性阻抗的核心公式**：

$$
\boxed{Z_c = \frac{V(r)}{I(r)} = \frac{\eta_0}{2\pi} \ln\left(\cot\frac{\theta_h}{2}\right)}
$$

其中 $\eta_0 = \sqrt{\mu_0/\epsilon_0} \approx 120\pi\; \Omega$ 是自由空间波阻抗。

代入 $\eta_0 = 120\pi$：

$$
\boxed{Z_c = 120\, \ln\left(\cot\frac{\theta_h}{2}\right)}
$$

**量纲检查**：$\eta_0$ 单位为 $\Omega$，对数函数无量纲 → $Z_c$ 单位为 $\Omega$ ✅

### 9.2.3 特性阻抗数值表

| $\alpha = \theta_h$ (deg) | $\cot(\alpha/2)$ | $Z_c$ (Ohm) |
|:-------------------------:|:----------------:|:-----------:|
| 1 | 114.59 | 567 |
| 2 | 57.29 | 486 |
| 5 | 22.90 | 374 |
| 10 | 11.43 | 298 |
| 15 | 7.60 | 249 |
| 20 | 5.67 | 209 |
| 30 | 3.73 | 157 |
| 45 | 2.41 | 106 |
| 60 | 1.73 | 66 |
| 90 | 1.00 | 0 |

### 9.2.4 有限长双锥天线的输入阻抗

有限长双锥天线存在末端反射，等效为一段终端有负载的传输线：

$$
\boxed{Z_{\text{in}} = Z_c \frac{Z_L + j Z_c \tan(kL)}{Z_c + j Z_L \tan(kL)}}
$$

其中：
- $Z_c$：双锥特性阻抗（由锥角决定）
- $Z_L$：末端负载阻抗（因辐射能量，$Z_L \neq \infty$）
- $L$：单边锥长
- $k = 2\pi/\lambda$：波数

严格分析需要求解球面波导中的**高阶模**（TE、TM 球面模），在馈电区激励的非 TEM 模会影响输入阻抗。

### 9.2.5 辐射场

对于 TEM 球面波，远区辐射场与球面偶极子一致：

$$
E_\theta \approx j\eta_0 \frac{k I_0 e^{-jkr}}{4\pi r} \frac{e^{-jkL\cos\theta} - e^{jkL\cos\theta} - 2\cos(kL)}{k\sin\theta}
$$

方向图与锥角 $\theta_h$ 有关。当 $\theta_h$ 较小时，方向图接近细线偶极子；$\theta_h$ 较大时，方向图变宽。

### 9.2.6 Schelkunoff 的互补角度概念

定义**互补角** $\alpha'$，使得 $\alpha' = \pi/2 - \alpha$。双锥天线的特性阻抗可表达为：

$$
Z_c = \frac{\eta_0}{2\pi} \ln\left(\frac{1 + \cos\alpha}{1 - \cos\alpha}\right) = \frac{\eta_0}{\pi} \ln\left(\cot\frac{\alpha}{2}\right)
$$

当 $\alpha = \pi/2$（锥角 90°）时，$Z_c = 0$；当 $\alpha \to 0$ 时，$Z_c \to \infty$。

---

## §9.3 Triangular Sheet, Bow-Tie, and Wire Simulation

### 9.3.1 从双锥到蝶形天线

实际应用中，实心双锥太重、风阻太大。工程折衷包括：

1. **三角片天线**（Triangular Sheet）：用薄金属片制成的三角形面近似锥面
2. **蝶形天线**（Bow-Tie）：用平的三角形替代锥面，更易制造
3. **线栅仿真**（Wire Simulation）：用沿锥面母线的导线近似

```
         平面三角片               蝶形天线
      ┌──────────┐           ┌──────────┐
      │ ┌──────┐ │           │  ┌────┐  │
      │ │ ──── │ │           │  │    │  │
      │ │      │ │           │  │    │  │
      └─┴──────┴─┘           └──┴────┴──┘
```

### 9.3.2 宽带特性比较

Brown 和 Woodward 的实验研究 [5] 表明：
- 三角片天线的宽带特性略逊于实心双锥（阻抗波动较大）
- 蝶形线栅天线的带宽更窄
- 过渡表面线密度越高，越接近实心双锥的特性

**等效半径近似**：对于线栅仿真双锥，可用等效半径概念估算：

$$
a_{\text{eq}} = w \cdot \left(\frac{s}{2\pi a}\right)^{1/N}
$$

其中 $w$ 是线栅的总宽度，$s$ 是导线间距，$a$ 是导线半径，$N$ 是导线数量。

---

## §9.4 Cylindrical Dipole

### 9.4.1 圆柱偶极子的宽带化机理

圆柱偶极子通过增大导体半径 $a$ 来降低 $L/a$ 比，从而：
- 降低近场储能密度（电流分布更均匀）
- 降低 $X_{\text{in}}$ 随频率的变化率
- 展宽阻抗带宽

### 9.4.2 King-Middleton 三阶理论

对于 $L/a$ 比不大的圆柱偶极子，Ch4 的细线感应 EMF 法不准确。King-Middleton 三阶理论给出更精确的电流分布：

$$
I(z) = I_0 \sin[k(L-|z|)] + I_1(z) + I_2(z)
$$

其中 $I_1$ 和 $I_2$ 是修正项，依赖于 $L/a$ 比和电长度。

### 9.4.3 谐振长度修正

细线半波偶极子的谐振长度为 $L = \lambda/2$。随着 $a/\lambda$ 增大，谐振长度缩短：

$$
L_{\text{res}} = \frac{\lambda}{2} \left[1 - \frac{2\ln 2 - 1}{2\Omega}\right], \quad \Omega = 2\ln\left(\frac{2L}{a}\right)
$$

其中 $\Omega$ 是**粗细系数**（thickness parameter）。对于非常粗的偶极子，谐振长度可比 $\lambda/2$ 短 5-10%。

### 9.4.4 输入阻抗 vs 半径比

King 的计算数据（Table 9.1）：

| $\Omega = 2\ln(2L/a)$ | $L/a$ | $R_{\text{res}}$ (Ohm) | 备注 |
|:---------------------:|:-----:|:---------------------:|:----:|
| 20 | 11013 | ~64 | 极细 |
| 12.4 | 500 | ~75 | 细线 |
| 9.2 | 100 | ~87 | 中等 |
| 7.8 | 50 | ~98 | 较粗 |
| 4.6 | 10 | ~115 | 非常粗 |

### 9.4.5 带宽经验公式

对于 VSWR < 2 的阻抗带宽：

$$
\boxed{\frac{\Delta f}{f_0} \approx \frac{1.4}{\ln(L/a) - 0.3} \times 100\%}
$$

**验证**：$L/a = 50$ 时，$\Delta f/f_0 \approx 1.4/(\ln 50 - 0.3) \approx 1.4/(3.91 - 0.3) \approx 38\%$，远大于细线的 ~10%。

### 9.4.6 介质涂覆对带宽的影响

在偶极子上涂覆介质材料（$|\epsilon_r| \gg 1$）可以改变近场储能，增大带宽。但代价是辐射效率降低。

### 9.4.7 等效半径概念

对于非圆截面（如三角片、带状线），可用等效半径：

$$
a_{\text{eq}} = \frac{w}{4} \quad \text{（宽度 $w$ 的薄片）}
$$

$$
a_{\text{eq}} = \left( \frac{w}{2\pi} \right) \exp\left( -\frac{\pi w}{2a} \right) \quad \text{（带状导体）}
$$

---

## §9.5 Folded Dipole

### 9.5.1 结构与传输线模型

折叠偶极子由两根平行的偶极子臂构成，末端短路连接，馈电点在一条臂的中点：

```
     ┌─────────────────────┐
     │                     │
  ●──┤     d               ├──●    <-- 馈电点
     │                     │
     └─────────────────────┘
     <------- L --------->
```

**核心原理**：将总电流分解为两种模式的叠加：

1. **天线模式**：两臂同向电流 → 辐射 → 等效为普通偶极子
2. **传输线模式**：两臂反向电流 → 不辐射 → 等效为短路传输线

### 9.5.2 等效电路推导

**天线模式**：两臂并联，等效偶极子的输入阻抗为 $Z_d$。电流分配比 $n$：

$$
n = 1 + \frac{\cosh^{-1}(d/a)}{\cosh^{-1}(d/a) - \cosh^{-1}(s/a)}
$$

对于相同粗细的两臂（$s = a$）：

$$
n = 1 + \frac{\cosh^{-1}(d/a)}{0} \to \infty \quad \Rightarrow \quad \text{变换比} = 4
$$

实际上，对于 $s = a$，电流均匀分布在两臂之间，$n = 2$，阻抗变换比为 $n^2 = 4$。

**传输线模式**：特性阻抗

$$
Z_0 = \frac{\eta_0}{\pi} \cosh^{-1}\left(\frac{d}{2a}\right)
$$

短路传输线输入阻抗：

$$
Z_t = j Z_0 \tan\left(\frac{kL}{2}\right)
$$

### 9.5.3 总输入阻抗

$$
\boxed{Z_{\text{in}} = \frac{2Z_d Z_t}{Z_d + 2Z_t}}
$$

对于 $L = \lambda/2$ 的情况，$\tan(kL/2) = \tan(\pi/2) \to \infty$，$Z_t \to \infty$：

$$
\boxed{Z_{\text{in}} \approx 4 Z_d}
$$

### 9.5.4 数值验证

使用 MoM 计算的半波折叠偶极子：

- 普通偶极子（$L/a = 100$）：$Z_d \approx 73 + j42\; \Omega$（感应 EMF 法）
- 折叠偶极子（$d = 0.005\lambda$）：$Z_{\text{in}} \approx 292 + j168\; \Omega$
- 阻抗变换比：$R_f/R_d \approx 4.00$ ✅

### 9.5.5 N 导体折叠偶极子

对于 N 根等半径导体的折叠偶极子：

$$
\boxed{Z_{\text{in}} = N^2 Z_d}
$$

| N | 阻抗变换比 | 典型输入阻抗（半波） |
|:-:|:---------:|:-------------------:|
| 2 | 4 | ~300 $\Omega$ |
| 3 | 9 | ~675 $\Omega$ |
| 4 | 16 | ~1200 $\Omega$ |

### 9.5.6 三线折叠偶极子

三导体结构：

```
  ┌─────┬─────┐
  │     │     │
  │  d  │  d  │
●─┤     │     ├─●
  │     │     │
  └─────┴─────┘
```

阻抗变换比可通过端子位置调节，一般 $Z_{\text{in}} \approx 1.4 Z_{\text{dipole}}$ ~ $9 Z_{\text{dipole}}$。

---

## §9.6 Sleeve Dipole

### 9.6.1 结构

套筒偶极子由三部分组成：
1. **顶部驱动臂**（$\lambda/4$ 量级）
2. **底部套筒**（同轴线外导体的延伸部分）
3. **同轴馈线**（从套筒内部穿过）

```
     ┌─────┐
     │     │   <-- 顶部臂 L1
     └──┬──┘
        │         馈电点
     ┌──┴──┐
     │     │   <-- 套筒 L2
     │     │
     └─────┘
        │
     同轴馈线
```

### 9.6.2 工作机理

套筒偶极子本质上是一个 **不平衡馈电的对称天线**：
- 套筒外表面的电流形成底部偶极子臂
- 改变电流分布，产生两个或多个临近谐振点
- 总有效长度 $L_{\text{eff}} \approx L_1 + L_2$

套筒偶极子可实现约 2:1 的带宽（VSWR < 2），典型应用在 VHF/UHF 频段。

### 9.6.3 设计参数

| 参数 | 典型值 | 说明 |
|:----:|:------:|:----:|
| $L_1 + L_2$ | $\lambda/4$ - $\lambda/2$ | 总谐振长度 |
| $L_1/L_2$ | 0.5 - 2.0 | 影响阻抗轨迹 |
| 套筒直径 | 3-10 倍馈线直径 | 影响阻抗水平 |

### 9.6.4 套筒单极子（Conical Skirt Monopole）

套筒单极子是套筒偶极子的地平面版本，套筒用锥状裙边（conical skirt）代替，进一步提高带宽。

---

## §9.7 Matching Techniques for Dipole Antennas

### 9.7.1 概述

当单一天线无法覆盖所需带宽时，需引入匹配网络。Ch9 讨论的匹配技术包括：

1. **传输线变压器**（Binomial / Tschebyscheff 多节变换器）
2. **T-match**
3. **Gamma match**
4. **Baluns**（Bazooka, U-shaped, Ferrite core）

### 9.7.2 多节传输线变压器

#### 二项式设计（最平坦响应）

反射系数 $\Gamma$ 的响应函数：

$$
\Gamma = A(1 + e^{-j2\theta})^N
$$

其中 $A = 2^{-N} \Gamma_L$，$\theta = \beta\ell$ 是每节的电长度。

特性阻抗分布：

$$
\ln\left(\frac{Z_{n+1}}{Z_n}\right) = 2^{-N} C(N, n) \ln\left(\frac{R_L}{Z_0}\right)
$$

其中 $C(N, n)$ 是二项式系数。

**带宽**：

$$
\frac{\Delta f}{f_0} = 2 - \frac{4\theta_m}{\pi}, \quad \Gamma_m = |\Gamma_L| \cos^N \theta_m
$$

#### 切比雪夫设计（等波纹响应）

反射系数：

$$
\Gamma = \frac{\Gamma_L e^{-jN\theta}}{2} \frac{T_N(\sec\theta_m \cos\theta)}{T_N(\sec\theta_m)}
$$

其中 $T_N(x)$ 是 N 阶切比雪夫多项式。

**带宽**：

$$
\frac{\Delta f}{f_0} = 2 - \frac{4\theta_m}{\pi}, \quad \theta_m = \arccos\left( \frac{1}{\sec\theta_m} \right)
$$

**设计步骤（Example 9.1）**：

1. 确定 $R_L$（天线阻抗）、$Z_0$（馈线特性阻抗）、$\Gamma_m$（最大允许反射系数）
2. 选择节数 N
3. 计算 $\sec\theta_m = \cosh\left[ \frac{1}{N} \cosh^{-1}\left( \frac{|\Gamma_L|}{\Gamma_m} \right) \right]$
4. 计算各节特性阻抗
5. 确定带宽 $\Delta f/f_0$

**Example 9.1（Balanis 4th Ed.）**：
> **问题**：设计一个二项式多节传输线变压器，将偶极子天线阻抗 $R_L = 300\;\Omega$ 匹配到 $Z_0 = 50\;\Omega$ 的馈线。假设变压器接入处的输入阻抗随频率保持恒定。确定最大带内 VSWR < 1.05 时的带宽。

**解**：
- $\Gamma_L = (300-50)/(300+50) = 0.714$
- N = 3 节时：$\Gamma_m = |\Gamma_L| \cos^3 \theta_m$
- 当 $\Gamma_m = (1.05-1)/(1.05+1) = 0.0244$ 时：
  - $\theta_m = \arccos[(0.0244/0.714)^{1/3}] = \arccos(0.3247) \approx 71.06^\circ$
  - 带宽：$\Delta f/f_0 = 2 - 4(71.06/180) \approx 42\%$
- N = 4 节时：带宽更大（约 60%+）

### 9.7.3 T-Match

T 形匹配通过在偶极子馈电点附近添加平行导体来实现阻抗变换：

```
         ┌──────────────────┐
         │                  │
      ───┤  ─────────────  ├───
         │   ↑ spacing d   │
         └──────────────────┘
         <----- L_T ------>
```

T-match 的等效分析与折叠偶极子类似，分解为天线模式和传输线模式。

关键设计参数：
- $L_T$：T 形杆长度（$\ll \lambda$）
- $d$：与偶极子间距
- 导体直径比（影响电流分配比 $\alpha$）

### 9.7.4 Gamma Match

Gamma 匹配是 T-match 的**单边版本**，广泛应用于 Yagi-Uda 天线的馈电：

```
     ┌───────────────────────┐
     │                       │
  ───┤     gamma rod          │
     │     ←── L_g ──→        │
     │     ─────── d ────     │
     │     ← gamma capacitor  │
     └───────────────────────┘
```

**等效电路**：Gamma rod 引入串联感性电抗，通过串联电容补偿，在馈电点实现共轭匹配。

**Example 9.2（Balanis 4th Ed.）**：
> **问题**：20m 波段（$f \approx 15$ MHz）Yagi-Uda 天线的驱动元阻抗为 $Z_a = 30.44(1 - j)\;\Omega$。需要匹配到 50 $\Omega$ 同轴线，使用 Gamma match。驱动元和 gamma rod 直径分别为 $d_d = 0.95\times10^{-2}\;\text{m}$ 和 $d_r = 3.175\times10^{-3}\;\text{m}$，中心间距 $s = 3.81\times10^{-2}\;\text{m}$。Gamma rod 长度 $L_g = 0.036\lambda$。求所需串联电容值。

**解**：
1. $f = 15$ MHz，$\lambda = 20$ m
2. 驱动元半径 $a_d = d_d/2 = 4.75\times10^{-3}\;\text{m}$
3. Gamma rod 半径 $a_r = d_r/2 = 1.5875\times10^{-3}\;\text{m}$
4. 间距比 $s/a_d = 8.02$
5. 电流分配比：

$$\alpha = \frac{\cosh^{-1}\left( \frac{s^2 - a_d^2 + a_r^2}{2 s a_d} \right)}{\cosh^{-1}\left( \frac{s^2 + a_d^2 - a_r^2}{2 s a_d} \right)}$$

6. 天线模式阻抗转换：

$$Z_a' = \frac{Z_a}{(1+\alpha)^2}$$

7. 传输线模式阻抗（Gamma rod 等效短路传输线）：

$$Z_0 = \frac{\eta_0}{\pi} \cosh^{-1}\left( \frac{s}{2\sqrt{a_d a_r}} \right)$$

$$Z_t = j Z_0 \tan\left(\frac{2\pi L_g}{\lambda}\right)$$

8. 馈电点总阻抗：

$$Z_{\text{in}} = Z_t + Z_a'$$

9. 调节串联电容 $C$ 使 $Z_{\text{in}}$ 的虚部为零：

$$X_C = -\text{Im}[Z_{\text{in}}], \quad C = \frac{1}{2\pi f X_C}$$

**数值结果**（Balanis 原书）：
- $\alpha \approx 0.7$（与几何尺寸有关）
- $Z_a' \approx 10.5(1 - j)\;\Omega$
- $Z_t$ 提供感性补偿，约 $j20\;\Omega$
- 所需串联电容 $C \approx 50$ pF 量级

### 9.7.5 Baluns（Balance-to-Unbalance Transformers）

#### Bazooka Balun（$\lambda/4$ 套筒巴伦）

在馈电点添加 $\lambda/4$ 套筒，阻止同轴线外导体外壁的电流：

```
     偶极子
    ┌──┴──┐
    │     │
    │ ┌──┐│ ← λ/4 套筒
    │ │  ││
    └─┴──┴┘
       │
     同轴电缆
```

- 原理：$\lambda/4$ 短路线将外导体外壁变换为高阻抗
- 带宽：约 1.5:1（受限于 $\lambda/4$ 的频率依赖性）

#### U-shaped Balun（$\lambda/2$ U 形巴伦）

使用 $\lambda/2$ 同轴线构成 U 形：

- 实现平衡-不平衡转换
- 4:1 阻抗变换（$\lambda/2$ 线阻抗变换特性）
- 带宽：约 1.5:1

#### Ferrite Core Balun

在传输线磁芯上加铁氧体，利用铁氧体的高磁导率维持宽频高阻抗：

- 带宽：可达 8-10:1
- 典型设计：4:1 阻抗变换巴伦，1:1 电流巴伦
- 适用频段：HF-VHF

#### Coil Coaxial Balun

将同轴线绕成线圈，利用线圈电感抑制外壁电流：

- 带宽：2-3:1
- 优点：结构简单、成本低

---

## §9.8 Discone and Conical Skirt Monopoles

### 9.8.1 盘锥天线结构

盘锥天线由水平圆盘（顶部）和圆锥（底部）构成，同轴馈电：

```
     ────────     ← 圆盘（半径 Rd）
        │
        │ 馈电间隙
       / \
      /   \       ← 圆锥（锥角 α）
     /     \
    /       \
```

### 9.8.2 工作原理

盘锥天线可视为双锥天线的**不对称变体**：
- 圆盘等效为双锥的上半锥（锥角 180°）
- 圆锥为下半锥
- 圆盘与锥体间馈电，激励 TEM 球面波

### 9.8.3 设计参数

| 参数 | 推荐值 | 说明 |
|:----:|:------:|:----:|
| 锥角 $\alpha$ | 25°-60° | 影响特性阻抗；45° 时 ~50 $\Omega$ |
| 圆盘直径 $D_d$ | $\geq \lambda_{\max}/4$ | 限制低频截止 |
| 圆锥高度 $H_c$ | $\approx 0.7\lambda_{\max}/4$ | 影响低频性能 |
| 馈电间隙 | $\lambda_{\max}/100$ | 尽量小以减少寄生电抗 |

### 9.8.4 方向图特性

- 垂直极化，水平面全向辐射
- E 面方向图近似于偶极子，但在 $\theta = 0^\circ$（天顶方向）有凹陷
- 随频率变化，主瓣稍向下倾斜

### 9.8.5 盘锥天线的带宽极限

可实现的阻抗带宽（VSWR < 2）可达 10:1 或更高。限制因素：
- 低频：由天线最大尺寸（圆盘直径 + 锥高）决定
- 高频：由馈电区域的寄生电抗决定

**经验截止频率**：

$$
f_{\text{min}} \approx \frac{0.7c}{D_d + H_c}
$$

---

## §9.9 Self-Complementary Antennas

### 9.9.1 Mushiake 关系

自互补天线是指天线结构与它的补结构完全相同的天线。其最重要的性质是**恒定输入阻抗**：

$$
Z_{\text{in}} \cdot Z_{\text{in}}^* = \frac{\eta_0^2}{4} \quad \Rightarrow \quad \boxed{Z_{\text{in}} = \frac{\eta_0}{2} \approx 188\; \Omega}
$$

这是 Mushiake 关系（1948），基本原理来自 Booker 关于电/磁互补天线的扩展。

### 9.9.2 典型自互补天线

- 互补蝶形天线（自互补 bow-tie）
- 对数周期自互补结构
- 螺旋天线（自互补形式）

### 9.9.3 频率无关特性

自互补天线在理论上具有无限带宽（频率无关），实际限制来自：
- 有限尺寸导致的低频截断
- 馈电结构引入的寄生效应

---

## §9.10 Broadband Characteristics of Some Other Antennas

### 9.10.1 铁氧体加载天线

在偶极子基座或馈电点附近添加铁氧体磁芯：

**优点**：
- 大幅降低天线尺寸（$L \ll \lambda/4$ 也可工作）
- 增加带宽（铁氧体损耗降低 Q 值）

**缺点**：
- 辐射效率降低（铁氧体磁损耗）
- 功率处理能力受限

### 9.10.2 介质加载

在偶极子周围涂覆高 $\epsilon_r$ 介质：

$$
\text{BW 增益} \propto \frac{\tan\delta}{\epsilon_r}
$$

其中 $\tan\delta$ 是介质损耗角正切。最优化的有耗介质可在带宽和效率之间取得折衷。

### 9.10.3 其他宽带天线概览

| 天线类型 | 带宽 (VSWR<2) | 典型应用 |
|:--------:|:-------------:|:--------:|
| 双锥天线 | ~3:1 | EMC 测试、宽带监测 |
| 蝶形天线 | ~2:1 | GPR、UWB 通信 |
| 盘锥天线 | ~10:1 | 宽带监测、扫描接收 |
| 折叠偶极子 | ~1.5:1 | FM 广播、VHF TV |
| 套筒偶极子 | ~2:1 | VHF/UHF 通信 |
| 自互补天线 | 理论无限 | UWB 系统 |

---

## 核心公式汇总

| 编号 | 公式 | 量纲 | 说明 |
|:----:|:----:|:----:|:----:|
| (9-1) | $Z_c = \dfrac{\eta_0}{2\pi}\ln\cot\dfrac{\alpha}{2}$ | Ω | 双锥特性阻抗 |
| (9-2) | $Z_{\text{in}} = Z_c \dfrac{Z_L + j Z_c \tan(kL)}{Z_c + j Z_L \tan(kL)}$ | Ω | 有限双锥输入阻抗 |
| (9-3) | $Z_{\text{in}} \approx 4Z_d$ | Ω | 半波折叠偶极子阻抗 |
| (9-4) | $n = 1 + \dfrac{\cosh^{-1}(d/a)}{\cosh^{-1}(d/a) - \cosh^{-1}(s/a)}$ | — | 折叠偶极子变换因子 |
| (9-5) | $Z_{\text{in}} = \dfrac{2Z_d Z_t}{Z_d + 2Z_t}$ | Ω | 折叠偶极子一般式 |
| (9-6) | $\dfrac{\Delta f}{f_0} \approx \dfrac{1.4}{\ln(L/a) - 0.3}$ | — | VSWR<2 带宽估算 |
| (9-7) | $Z_{\text{in}} \cdot Z_{\text{in}}^* = \dfrac{\eta_0^2}{4}$ | Ω² | Mushiake 自互补关系 |
| (9-8) | $L_{\text{res}} = \dfrac{\lambda}{2}\left[1 - \dfrac{2\ln2 - 1}{2\Omega}\right]$ | m | 粗偶极子谐振长度修正 |
| (9-9) | $\Gamma = \dfrac{\Gamma_L e^{-jN\theta}}{2} \dfrac{T_N(\sec\theta_m \cos\theta)}{T_N(\sec\theta_m)}$ | — | 切比雪夫变压器响应 |

---

## 参考代码与图表

- 代码实现：`python/balanis_ch09_broadband_dipoles.py`
- 图 1：圆柱偶极子阻抗 vs 半径比 → `python/figures/ch09/ch09_ex1_dipole_vs_radius.png`
  ![圆柱偶极子阻抗 vs 半径比](../python/figures/ch09/ch09_ex1_dipole_vs_radius.png)
- 图 2：折叠偶极子阻抗特性 → `python/figures/ch09/ch09_ex2_folded_dipole.png`
  ![折叠偶极子阻抗特性](../python/figures/ch09/ch09_ex2_folded_dipole.png)
- 图 3：双锥天线特性阻抗 → `python/figures/ch09/ch09_ex3_biconical.png`
  ![双锥天线特性阻抗](../python/figures/ch09/ch09_ex3_biconical.png)
- 图 4：带宽 vs 偶极子半径 → `python/figures/ch09/ch09_ex4_bandwidth_vs_radius.png`
  ![带宽 vs 偶极子半径](../python/figures/ch09/ch09_ex4_bandwidth_vs_radius.png)
- 图 5：粗细偶极子电流分布对比 → `python/figures/ch09/ch09_ex5_thick_vs_thin_current.png`
  ![粗细偶极子电流分布对比](../python/figures/ch09/ch09_ex5_thick_vs_thin_current.png)

---

## 参考文献

1. Balanis, C. A., *Antenna Theory: Analysis and Design*, 4th Ed., Wiley, 2016, Chapter 9.
2. Schelkunoff, S. A., "Theory of Antennas of Arbitrary Size and Shape," *Proc. IRE*, vol. 29, pp. 493-521, 1941.
3. King, R. W. P., *Tables of Antenna Characteristics*, IFI/Plenum, 1971.
4. Harrison, C. W., "Folded Dipole Antennas," *IRE Trans. Antennas Propagat.*, vol. AP-10, pp. 602-605, 1962.
5. Brown, G. H. and Woodward, O. M., "Experimentally Determined Radiation Characteristics of Conical and Triangular Antennas," *RCA Review*, vol. 13, pp. 425-452, 1952.
6. Thiele, G. A., Ekelman, E. P., and Henderson, L. W., "On the Accuracy of the Transmission Line Model for Folded Dipole," *IEEE Trans. Antennas Propagat.*, vol. AP-28, No. 5, pp. 700-703, 1980.
7. Mushiake, Y., "Self-Complementary Antennas," *IEEE Antennas Propagat. Magazine*, vol. 34, pp. 23-29, 1992.
8. Smith, P. H., "The Discone Antenna," *Electronics*, vol. 28, pp. 138-141, 1955.
9. Smith, C. E., Butler, C. M., and Umashankar, K. R., "Characteristics of Wire Biconical Antenna," *Microwave Journal*, pp. 37-40, September 1979.

---

*Last updated: 2026-04-30*
