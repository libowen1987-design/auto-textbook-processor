# Chapter 10: Traveling Wave and Broadband Antennas
# 第10章：行波天线与宽带天线

> **核心思想**：行波天线（Traveling Wave Antenna）与驻波天线的本质区别在于电流分布。驻波天线（如标准半波偶极子）上电流为驻波分布，存在反射和末端开路效应；行波天线在终端接匹配负载，电流沿导线单向传播，无反射波。这种特性带来更宽的阻抗带宽和独特的单向辐射方向图。

**章节目录**（Balanis 4th Ed. Ch10）：
- §10.1 Introduction
- §10.2 Traveling Wave Antennas
  - §10.2.1 Long Wire
  - §10.2.2 V-Antenna
  - §10.2.3 Rhombic Antenna
- §10.3 Broadband Antennas
  - §10.3.1 Helical Antenna
  - §10.3.2 Yagi-Uda Array (reference to Ch4)
  - §10.3.3 Other Traveling Wave Structures (dielectric rod, etc.)

---

## §10.1 Introduction

### 行波 vs 驻波

| 特性 | 驻波天线（偶极子） | 行波天线 |
|:----:|:-----------------:|:--------:|
| 电流分布 | $I(z) = I_0 \sin[k(L/2 - \|z\|)]$ | $I(z) = I_0 e^{-j\beta z}$ |
| 终端 | 开路（$I=0$） | 接匹配负载 |
| 是否有反射波 | 是，构成驻波 | 否，纯行波 |
| 阻抗带宽 | 窄（~5-10%） | 宽（~2:1 或更宽） |
| 方向图 | 双向或全向 | 单向（朝传播方向） |
| 典型效率 | 高 | 因终端负载有电阻损耗而略低 |

### 行波天线的分类

1. **慢波行波天线**（Slow-wave）：相速 $v_p < c$，如长导线（电流波速约等于光速，但结构上形成慢波）
2. **快波行波天线**（Fast-wave / Leaky-wave）：相速 $v_p > c$，如漏波天线（波导开槽）

本章重点讨论慢波行波天线中的经典结构：长导线、V 形天线、菱形天线，以及宽带螺旋天线和 Yagi-Uda。

---

## §10.2 Traveling Wave Antennas

### §10.2.1 Long Wire (Traveling Wave on a Wire)

#### 电流分布

沿 $z$ 轴放置的长导线，长度 $L$，一端馈电，另一端接匹配负载。在馈电端（$z=0$）激励的电流沿 +z 方向传播：

$$
\boxed{I(z) = I_0 e^{-j\beta z}}, \quad 0 \le z \le L
$$

其中 $\beta = \omega/v_p \approx 2\pi/\lambda$（导线上的相速近似等于自由空间光速，$\beta \approx k$）。

这是一个**纯行波**——没有反射波从负载端返回，因此没有驻波分量。

对比：相同长度的驻波导线（两端开路）：

$$
I_{\text{standing}}(z) = I_0 \sin[\beta(L - z)]
$$

---

#### 辐射场的推导

对于 $z$ 方向放置的线电流源，远区电场由矢量位推出：

$$
\mathbf{A} = \hat{\mathbf{z}} \frac{\mu I_0}{4\pi} \int_0^L \frac{e^{-j\beta z'} e^{-jkR}}{R} \, dz'
$$

远场近似（$R \approx r - z'\cos\theta$，$R \approx r$ for amplitude）：

$$
A_z = \frac{\mu I_0 e^{-jkr}}{4\pi r} \int_0^L e^{-j\beta z'} e^{jkz'\cos\theta} \, dz'
$$

$$
A_z = \frac{\mu I_0 e^{-jkr}}{4\pi r} \cdot \frac{1 - e^{-jL(k - \beta\cos\theta)}}{j(k - \beta\cos\theta)}
$$

对于 $\beta = k$（导线波速等于光速）：

$$
A_z = \frac{\mu I_0 e^{-jkr}}{4\pi r} \cdot \frac{1 - e^{-jkL(1 - \cos\theta)}}{jk(1 - \cos\theta)}
$$

$$= \frac{\mu I_0 L e^{-jkr}}{4\pi r} \cdot e^{-j\psi/2} \frac{\sin(\psi/2)}{\psi/2}, \quad \psi = kL(1 - \cos\theta) $$

远区电场 $\mathbf{E} = -j\omega \mathbf{A}_t$（仅横向分量）：

$$
\boxed{E_\theta = j\eta \frac{k I_0 L e^{-jkr}}{4\pi r} \sin\theta \cdot e^{-j\psi/2} \frac{\sin(\psi/2)}{\psi/2}}
$$

其中 $\psi = kL(1 - \cos\theta)$。

**归一化方向图函数**：

$$
\boxed{F(\theta) = \sin\theta \cdot \frac{\sin[\frac{kL}{2}(1 - \cos\theta)]}{\frac{kL}{2}(1 - \cos\theta)}}
$$

两个因子的物理含义：
- $\sin\theta$：**单元因子**（短偶极子的方向图）
- $\frac{\sin[\frac{kL}{2}(1 - \cos\theta)]}{\frac{kL}{2}(1 - \cos\theta)}$：**行波阵列因子**（沿长度方向的渐进相位）

---

#### 方向图特性

**主瓣方向** $\theta_m$（从导线轴向测量的角度）：

$$
\cos\theta_m \approx 1 - \frac{0.371\lambda}{L} \quad \text{(近似公式)}
$$

更精确的极值条件来自 $dF(\theta)/d\theta = 0$。

**数值特征**：
- $L = \lambda$：主瓣在 $\theta_m \approx 60^\circ$
- $L = 5\lambda$：主瓣在 $\theta_m \approx 22^\circ$
- $L = 10\lambda$：主瓣在 $\theta_m \approx 14^\circ$

随着 $L/\lambda$ 增大，主瓣更靠近导线方向（$\theta \to 0$）。

**波瓣宽度**：近似为

$$
\text{HPBW} \approx \frac{0.89\lambda}{L} \quad (\text{弧度})
$$

**总辐射功率**：

$$
P_{\text{rad}} = \frac{1}{2\eta} \int_0^{2\pi} \int_0^\pi |E_\theta|^2 r^2 \sin\theta \, d\theta \, d\phi
$$

辐射电阻：

$$
R_{\text{rad}} = \frac{2P_{\text{rad}}}{I_0^2}
$$

对于 $\beta = k$，辐射电阻的近似表达式：

$$
R_{\text{rad}} \approx 60 \left[\ln(2kL) - \text{Ci}(2kL) + \frac{\sin(2kL)}{2kL} - 1\right]
$$

其中 $\text{Ci}(x) = -\int_x^\infty \frac{\cos t}{t} dt$ 是余弦积分函数。

对于长导线（$L \gg \lambda$）：

$$
R_{\text{rad}} \approx 60 \left[\ln(2kL) - \text{Ci}(2kL) - 1\right] \approx 60[\ln(2kL) - \gamma - 1]
$$

其中 $\gamma \approx 0.5772$ 是欧拉常数。

**激励功率**：

$$
P_{\text{in}} = \frac{1}{2} I_0^2 (R_{\text{rad}} + R_L)
$$

其中 $R_L$ 是终端匹配负载电阻。**辐射效率**：

$$
\eta_{\text{rad}} = \frac{P_{\text{rad}}}{P_{\text{in}}} = \frac{R_{\text{rad}}}{R_{\text{rad}} + R_L}
$$

---

#### 方向性系数

长导线的方向性系数随 $L/\lambda$ 增大而增大。近似公式：

$$
D_0 \approx \frac{4(L/\lambda)^2}{\int_0^{2\pi} \left[\frac{\sin(kL(1-\cos\theta)/2)}{kL(1-\cos\theta)/2}\right]^2 \sin^3\theta \, d\theta}
$$

工程近似（$L > 2\lambda$）：

$$
D_0 \approx 10\log_{10}(4L/\lambda) \quad \text{[dBi]}
$$

---

#### 数值示例

| $L/\lambda$ | $\theta_m$ (deg) | HPBW (deg) | $D_0$ (dBi) | $R_{\text{rad}}$ (Ohm) |
|:----------:|:----------------:|:----------:|:----------:|:---------------------:|
| 1 | ~57 | ~51 | ~5.2 | ~105 |
| 2 | ~35 | ~26 | ~8.0 | ~165 |
| 3 | ~25 | ~17 | ~9.8 | ~225 |
| 5 | ~17 | ~10 | ~12.0 | ~340 |
| 10 | ~10 | ~5 | ~15.0 | ~620 |

---

#### 行波与驻波长导线的方向图对比

相同长度（$L = 5\lambda$）的对比：

| 特性 | 行波（匹配终端） | 驻波（开路终端） |
|:----:|:---------------:|:---------------:|
| 电流分布 | $I(z) = I_0 e^{-j\beta z}$ | $I(z) = I_0 \sin[\beta(L-z)]$ |
| 主瓣数 | 1 个（朝传播方向） | 多个（双向） |
| 副瓣电平 | -13.5 dB | 变化 |
| 阻抗 | 宽频带 | 窄频带 |

---

### §10.2.2 V-Antenna

#### 结构

V 形天线由两根长导线构成，呈 V 形排列，顶点馈电：

```
        /\
       /  \
      /    \
     /      \
    /        \
   /__________\
   <-- 2\psi -->    \psi: 半张角
   馈电点位于顶点
```

#### 工作原理

V 形天线的辐射方向图是两臂方向图的**叠加**。每臂在各自的外端方向产生主瓣，通过选择合适的张角 $2\psi$，可使两个主瓣在中间方向合成并增强。

#### 方向图合成

两臂的归一化方向图函数（自由空间，无接地）：

$$
F(\theta, \phi) = F_1(\theta, \phi) + F_2(\theta, \phi)
$$

其中 $F_1$ 是沿 $+\psi$ 方向的臂，$F_2$ 是沿 $-\psi$ 方向的臂。

每臂的方向图函数沿用长导线的形式，但需坐标旋转到各臂的轴向。

**远场近似**：

$$
F(\theta, \phi) \propto \sin\theta_1 \frac{\sin[\frac{kL}{2}(1 - \cos\theta_1)]}{\frac{kL}{2}(1 - \cos\theta_1)} + \sin\theta_2 \frac{\sin[\frac{kL}{2}(1 - \cos\theta_2)]}{\frac{kL}{2}(1 - \cos\theta_2)}
$$

其中 $\theta_1$ 和 $\theta_2$ 分别是观察方向与两臂方向的夹角。

---

#### 最优张角

对于给定 $L/\lambda$，存在最优张角 $2\psi_{\text{opt}}$ 使得：
1. 两臂的主瓣在中间方向合成，形成尖锐的单向波束
2. 副瓣的相互抵消最佳

**经验最优张角**：

$$
\boxed{2\psi_{\text{opt}} \approx \frac{2 \times 0.371\lambda}{L} \quad (\text{弧度}) \approx 42.5^\circ \cdot \frac{\lambda}{L}}
$$

更精确地，对于 $L/\lambda$ 范围 1-10：

| $L/\lambda$ | $\psi_{\text{opt}}$ (deg) | $2\psi_{\text{opt}}$ (deg) |
|:----------:|:------------------------:|:--------------------------:|
| 1 | 60 | 120 |
| 2 | 50 | 100 |
| 3 | 40 | 80 |
| 5 | 30 | 60 |
| 10 | 20 | 40 |

**实际设计方案**：在 $L/\lambda$ 较大时采用约 $70^\circ$ 的张角可以获得较好的前向辐射和增益。

---

#### 接地平面的 V 形天线

实际中 V 形天线常架设在地平面上（单极版本）。使用镜像法，V 形天线和其镜像构成一个完整的 V 形天线阵列。

方向图由地面反射和导线方向图共同决定，优化高度 $h$ 通常为 $\lambda/4$ 的奇数倍。

---

### §10.2.3 Rhombic Antenna

#### 结构与几何参数

菱形天线由四根等长导线构成菱形：

```
        A
       /\
      /  \
   D /____\ B   馈电点在 A 点，终端负载在 C 点
     \    /
      \  /
       \/
        C  (接匹配负载)
```

**几何参数**：
- $L$：每边的长度
- $\phi$：菱形半角（锐角的一半）
- $h$：天线架设高度
- $R_L$：终端负载电阻（接 C 点）

---

#### 工作原理

1. 从 A 点馈电，电流沿 AB 和 AD 两臂传播
2. 在 B 点和 D 点，导线方向改变，但波继续沿 BC 和 DC 传播
3. 在 C 点接入匹配负载 $R_L$，吸收剩余功率（避免反射）
4. 四段导线上的行波电流辐射合成，在特定方向形成单向波束

每个边上的电流均为行波：

$$
I_i(z_i) = I_0 e^{-j\beta z_i}, \quad i = 1, 2, 3, 4
$$

其中 $z_i$ 沿各边方向。

---

#### 合成方向图

总远场是四段行波导线的辐射场之和。对于自由空间（无地）的理想菱形：

$$
F_{\text{total}}(\theta, \phi) = \sum_{i=1}^4 F_i(\theta, \phi) e^{-j\beta \Delta_i}
$$

其中 $\Delta_i$ 是各段起始点与馈电点的相位差。

**主方向**：菱形平面的法线方向（垂直于菱形平面，即 $\theta = 0$，如果菱形在 $\theta = 90^\circ$ 平面内）。

**最佳高度** $h_{\text{opt}}$（考虑地面反射）：

$$
\boxed{h_{\text{opt}} = \frac{\lambda}{4\sin\phi}}
$$

---

#### 设计公式

菱形天线的方向性系数近似为：

$$
D_0 \approx 10\log_{10} \left[ \frac{4L}{\lambda} \right] \quad \text{[dBi]}
$$

更精确的公式（Balanis 4th Ed. 10-43）：

$$
\boxed{D_0 \approx \frac{4L}{\lambda} \cdot \frac{1 - e^{-2\alpha L}}{2\alpha L}}
$$

其中 $\alpha$ 是导线衰减常数（Np/m），包含了辐射损耗和欧姆损耗。

**输入阻抗**：

$$
Z_{\text{in}} \approx R_L + j0 \quad \text{（匹配良好时）}
$$

实际上，由于菱形天线具有一定带宽，输入阻抗在线路匹配带宽内为纯阻性。

**辐射电阻**（Beverage 近似，用于菱形的一边）：

$$
R_{\text{rad}}^{(1)} \approx 60 \left[\ln\left(\frac{2L}{a}\right) - 1\right]
$$

其中 $a$ 是导线半径。

---

#### 典型设计参数

| 参数 | 推荐值 | 说明 |
|:----:|:------:|:----:|
| 每边长度 $L$ | 3-8$\lambda$ | 越长增益越高 |
| 菱形半角 $\phi$ | 15°-35° | 优化方向性和阻抗 |
| 架设高度 $h$ | $\lambda/4\sin\phi$ | 地面反射的相位配合 |
| 终端电阻 $R_L$ | 600-800 $\Omega$ | 匹配菱形天线特性阻抗 |
| 工作带宽 | ~1.5:1 | VSWR < 2 |

---

#### 菱形天线 vs V 形天线

| 特性 | V-Antenna | Rhombic Antenna |
|:----:|:---------:|:---------------:|
| 馈电点 | 顶点 | 一角 |
| 终端负载 | 无/可选 | 对端角点 |
| 波束方向 | 沿张角平分线向前 | 菱形平面法线 |
| 实现单向 | 靠地平面+镜像 | 靠地平面+镜像+终端匹配 |
| 增益 | 中等 | 较高 |
| 带宽 | 中等 | 较宽（因行波） |

---

#### Beverage Antenna（行波天线特例）

Beverage 天线（§10.2.1 的特例）是一根沿地面水平架设的长导线，终端接地（或接匹配负载）：

- 结构：$L$ 长（2-10$\lambda$），高度 $h \approx 2$-$5$ m（< $\lambda/4$）
- 方向图：沿导线方向有主瓣，垂直极化
- 频率范围：低频（LF, MF, HF），尤其是 100 kHz - 30 MHz
- 典型增益：接近长导线理论值 $- 3$-$6$ dBi（考虑地面损耗）
- 用途：远程接收天线（方向性好、噪声低）

**水平长导线的地面镜像**：地面反射使有效高度加倍，方向图由反射系数和高度决定。

---

## §10.3 Broadband Antennas

### §10.3.1 Helical Antenna（螺旋天线）

#### 结构与几何参数

螺旋天线由螺旋状导线绕制而成，常见于 VHF/UHF 频段。

```
       ┌──┐
       │  │
       │  │ ← N 圈
       │  │
       └──┘
       │
   同轴馈电
       │
     接地平面
```

关键几何参数：

| 参数 | 符号 | 定义 |
|:----:|:----:|:----:|
| 螺旋直径 | $D$ | 螺旋外径 |
| 匝间距 | $S$ | 相邻匝的轴向距离 |
| 匝数 | $N$ | 总圈数 |
| 螺距角 | $\alpha$ | $\alpha = \tan^{-1}(S/\pi D)$ |
| 螺旋周长 | $C$ | $C = \pi D$ |
| 总长度 | $L_{\text{total}}$ | $L_{\text{total}} = N S$（轴向） |
| 导线长度 | $L_{\text{wire}}$ | $L_{\text{wire}} = N\sqrt{(\pi D)^2 + S^2} = N C/\cos\alpha$ |

---

#### 工作模式

螺旋天线有两种基本工作模式：

| 模式 | 条件 | 方向图 | 极化 |
|:----:|:----:|:------:|:----:|
| **法向模式** (Normal) | $C \ll \lambda$ | 侧射（broadside） | 线极化或椭圆极化 |
| **轴向模式** (Axial) | $C \approx \lambda$ | 端射（end-fire） | 圆极化（CP） |

---

#### 法向模式 (Normal Mode)

当 $D \ll \lambda$（$C \ll \lambda$），每个小螺旋圈可等效为一个短偶极子和一个小环的叠加。

**等效模型**：

螺旋一圈的辐射是：
- 垂直方向（$z$）：短偶极子（电流沿 $\hat{\mathbf{z}}$）
- 水平方向：小环（磁偶极子）

**轴比**（Axial Ratio）：

$$
\boxed{\text{AR} = \frac{|E_\theta|}{|E_\phi|} = \frac{S k^2 I_0 / (4\pi r)}{(\pi D^2) k^2 I_0 / (4\pi r)} = \frac{S}{\pi D} \cdot \frac{\lambda}{2\pi} \cdot \text{(因子)}}
$$

更精确的公式（Balanis (10-53)）：

$$
\boxed{\text{AR} = \frac{S}{2\pi a} \cdot \frac{\lambda}{2\pi a} = \frac{S\lambda}{4\pi^2 a^2}, \quad a = D/2}
$$

使用周长 $C$ 和间距 $S$ 表达轴比：

$$
\boxed{\text{AR} = \frac{2S\lambda}{(\pi D)^2} = \frac{2S\lambda}{C^2}}
$$

**极化特性**：
- 当 $AR = 0$（$\pi D = 0$ 或 $S = 0$）：纯线极化（短偶极子）
- 当 $AR \to \infty$（$S \gg C$）：纯线极化（环）
- 螺旋参数设计可实现圆极化：$C = \sqrt{2S\lambda}$

**输入阻抗**（法向模式）：

$$
Z_{\text{in}} \approx R_r + jX
$$

其中辐射电阻 $R_r$ 很小（法向模式效率低），电抗 $X$ 呈感性。

法向模式实用价值有限，因为：
1. 辐射电阻低，效率低
2. 带宽窄
3. 方向图为侧射，增益有限

---

#### 轴向模式 (Axial Mode)

当螺旋周长 $C \approx \lambda$（通常 $0.75\lambda < C < 1.33\lambda$）时，产生轴向模式。

**物理机制**：沿螺旋导线的行波电流产生圆极化辐射，在轴向（螺旋轴方向）同相叠加。

**轴向模式条件**：

$$
\boxed{\frac{3}{4}\lambda < C < \frac{4}{3}\lambda}
$$

螺距角 $\alpha$ 的典型范围：$12^\circ < \alpha < 18^\circ$

---

#### 轴向模式特性

**方向图**：近似于 $\cos^n\theta$ 形式，沿轴向有单一主瓣。

**半功率波束宽度**（HPBW）：

$$
\boxed{\text{HPBW} \approx \frac{52}{C/\lambda \sqrt{N S/\lambda}} \quad \text{[deg]}}
$$

其中 $C/\lambda$ 是归一化周长，$N$ 是匝数，$S/\lambda$ 是归一化匝间距。

**方向性系数**（Directivity）：

$$
\boxed{D_0 \approx 12 \left(\frac{C}{\lambda}\right)^2 \frac{N S}{\lambda} \quad \text{[线性]}}
$$

或：

$$
\boxed{D_0 \approx 10\log_{10}\left[15 N \left(\frac{C}{\lambda}\right)^2 \frac{S}{\lambda}\right] \quad \text{[dBi]}}
$$

对于典型设计（$C = \lambda$，$\alpha \approx 14^\circ$，$S/\lambda \approx 0.25$）：

$$
D_0 \approx 10\log_{10}(3.75 N) \quad \text{[dBi]}
$$

**输入阻抗**（轴向模式近似为纯阻性）：

$$
\boxed{R_{\text{in}} \approx 140 \frac{C}{\lambda} \quad [\Omega]}
$$

对于 $C = \lambda$：$R_{\text{in}} \approx 140\;\Omega$。

**轴比**（Axial Ratio，轴向模式）：

$$
\boxed{\text{AR} = \frac{2N + 1}{2N}}
$$

对于大 $N$（$N \to \infty$）：$\text{AR} \to 1$（理想圆极化）

具体值：
| $N$ | AR (dB) | 极化 |
|:---:|:-------:|:----:|
| 5 | 0.83 dB | 接近圆极化 |
| 10 | 0.43 dB | 良好圆极化 |
| 20 | 0.22 dB | 极好圆极化 |

---

#### 轴向模式设计步骤

**设计目标**：在 $f_{\text{min}}$ 到 $f_{\text{max}}$ 频段内实现轴向模式圆极化。

**设计流程**：

1. 选择螺旋周长：$C = \lambda_{\text{center}}$（约为 1.05$\lambda$ 以获得最佳轴比）
2. 选择螺距角 $\alpha \approx 14^\circ$
3. 计算匝间距：$S = C \tan\alpha$
4. 选择匝数 $N$（通常 5-15，更多匝数提高增益和方向性）
5. 接地平面尺寸：$\geq \lambda_{\text{max}}/2$

**示例**（Balanis Example 10.1）：
> **问题**：设计一个在 400-600 MHz 工作的轴向模式螺旋天线（中心频率 500 MHz）。求几何参数和性能指标。

**解**：
- $\lambda_0 = c/f_0 = 0.6$ m
- 选 $C = 1.05\lambda_0 = 0.63$ m（$D = C/\pi = 0.2$ m）
- 选 $\alpha = 14^\circ$，$S = C\tan\alpha = 0.63 \times 0.249 = 0.157$ m
- 选 $N = 10$ 匝
- HPBW ≈ 52 / [1.05 × √(10 × 0.261)] ≈ 52 / (1.05 × 1.615) ≈ 30.7°
- $D_0 ≈ 12 × (1.05)² × 10 × 0.261 ≈ 34.5$（~15.4 dBi）
- $R_{\text{in}} ≈ 140 × 1.05 ≈ 147\;\Omega$
- AR ≈ (2×10 + 1)/(2×10) = 21/20 = 1.05（~0.42 dB）

---

#### 轴向模式频率特性

轴向模式具有宽频带特性（典型 1.7:1，VSWR < 2）：

| 频率 | $C/\lambda$ | $R_{\text{in}}$ (Ohm) | 极化质量 |
|:----:|:-----------:|:-------------------:|:--------:|
| $f_{\text{min}}$ | 0.75 | 105 | 边缘 |
| $f_0$ | 1.05 | 147 | 最佳 |
| $f_{\text{max}}$ | 1.33 | 186 | 下降 |

---

#### 螺旋天线阵列

螺旋天线可组成阵列以进一步提高增益：
- 4 元阵列：增益增加 6 dB
- 16 元阵列：增益增加 12 dB
- 单元间距：$\approx 0.8$-$1.0\lambda$

螺旋阵列的馈电需保证各单元相位一致（对于轴向辐射）。

---

### §10.3.2 Yagi-Uda Array（参考 Ch4）

Yagi-Uda 天线已在 Ch4 详细介绍。在 Ch10 中，Yagi-Uda 被归类为行波天线（引向器/反射器中的电流具有行波渐进相位特性）。关键要点：

- Yagi 是一种端射阵列，引向器中的电流相对于驱动元具有渐进相位滞后
- 方向性系数取决于引向器数量和间距
- 典型带宽：2-5%（VSWR < 2）
- 此处不重复公式，详见 Ch4 的笔记和代码。

---

### §10.3.3 Other Traveling Wave Structures

#### Dielectric Rod Antenna（介质杆天线）

介质杆天线是一种**表面波天线**，电磁波沿介质杆传播，相速小于光速（$v_p < c$）。

结构：介质杆（矩形或圆截面）的一端由波导或同轴-介质过渡结构馈电。

**工作原理**：
- HE₁₁ 模在介质杆中传播
- 波在介质-空气界面处缓慢泄漏（辐射）
- 方向图沿杆轴向端射

**设计参数**：
- 介质杆长度 $L_{\text{rod}}$：通常 6-10$\lambda$
- 介质相对介电常数 $\epsilon_r$：2-10
- 杆截面尺寸：约为 $\lambda/4$ 量级
- 直径渐缩（taper）可降低副瓣

**典型性能**：
- 增益：15-20 dBi
- 带宽：10-20%（依赖于介质）
- 应用：毫米波频段、雷达

---

#### Polyrod Antenna

聚苯乙烯介质杆天线（聚杆天线），$L = 5$-$10\lambda$：

- 增益：约 20 dBi
- 副瓣：-15 dB
- 使用介质渐缩控制波瓣宽度

---

#### Leaky-Wave Antenna（漏波天线）

漏波天线是一种快波结构（$v_p > c$），沿波导周期性开口或变化使能量逐步泄漏辐射。

**分类**：
1. 均匀漏波天线（波导开槽）
2. 周期性漏波天线（表面变化周期 $p$）

**特性**：
- 频率扫描特性：主瓣方向随频率变化
- 方向图：扇形波束
- 带宽：依赖于结构

---

#### Surface Wave Antenna（表面波天线）

表面波天线利用介质层或波纹金属表面引导波传播。典型结构：

- **波纹喇叭**（Corrugated Horn）：在喇叭内壁加周期性波纹
- **介质加载天线**：在金属表面涂覆介质层

---


| 编号 | 公式 | 量纲 | 说明 |
|:----:|:----:|:----:|:----:|
| (10-1) | $I(z) = I_0 e^{-j\beta z}$ | A | 长导线行波电流 |
| (10-2a) | $F(\theta) = \sin\theta \cdot \dfrac{\sin[\frac{kL}{2}(1-\cos\theta)]}{\frac{kL}{2}(1-\cos\theta)}$ | — | 长导线归一化方向图 |
| (10-2b) | $R_{\text{rad}} = 60 \left[\ln(2kL) - \text{Ci}(2kL) + \frac{\sin(2kL)}{2kL} - 1\right]$ | Ω | 行波导线辐射电阻 |
| (10-3) | $2\psi_{\text{opt}} \approx 42.5^\circ \cdot \dfrac{\lambda}{L}$ | ° | V 形天线最优张角 |
| (10-4) | $h_{\text{opt}} = \dfrac{\lambda}{4\sin\phi}$ | m | 菱形天线最佳高度 |
| (10-5) | $D_0 \approx \dfrac{4L}{\lambda} \cdot \dfrac{1 - e^{-2\alpha L}}{2\alpha L}$ | — | 菱形方向性 |
| (10-6) | $\text{AR}_{\text{nm}} = \dfrac{2S\lambda}{C^2}$ | — | 法向模式轴比 |
| (10-7) | $\dfrac{3}{4}\lambda < C < \dfrac{4}{3}\lambda$ | m | 轴向模式条件 |
| (10-8) | $\text{HPBW} \approx \dfrac{52}{C/\lambda \sqrt{N S/\lambda}}$ | ° | 螺旋 HPBW |
| (10-9) | $D_0 \approx 12 \left(\dfrac{C}{\lambda}\right)^2 \dfrac{N S}{\lambda}$ | — | 螺旋方向性 |
| (10-10) | $R_{\text{in}} \approx 140 \dfrac{C}{\lambda}$ | Ω | 螺旋输入阻抗（轴向） |
| (10-11) | $\text{AR} = \dfrac{2N + 1}{2N}$ | — | 螺旋轴比（轴向） |
| (10-12) | $\alpha = \tan^{-1}\left(\dfrac{S}{\pi D}\right)$ | ° | 螺距角定义 |

---


- 代码实现：`python/balanis_ch10_traveling_wave.py`
- 图 1：长导线方向图（行波 vs 驻波）→ `figures/ch10/ch10_ex1_long_wire_pattern.png`
  ![长导线方向图](../python/figures/ch10/ch10_ex1_long_wire_pattern.png)
- 图 2：V 形天线方向图 → `figures/ch10/ch10_ex2_v_antenna.png`
  ![V 形天线方向图](../python/figures/ch10/ch10_ex2_v_antenna.png)
- 图 3：菱形天线方向图 → `figures/ch10/ch10_ex3_rhombic.png`
  ![菱形天线方向图](../python/figures/ch10/ch10_ex3_rhombic.png)
- 图 4：螺旋天线轴向模式设计 → `figures/ch10/ch10_ex4_helical_axial.png`
  ![螺旋天线轴向模式](../python/figures/ch10/ch10_ex4_helical_axial.png)
- 图 5：螺旋天线 HPBW 和增益 vs 频率 → `figures/ch10/ch10_ex5_helical_freq_sweep.png`
  ![螺旋频率特性](../python/figures/ch10/ch10_ex5_helical_freq_sweep.png)

---


1. Balanis, C. A., *Antenna Theory: Analysis and Design*, 4th Ed., Wiley, 2016, Chapter 10.
2. Kraus, J. D., *Antennas*, 2nd Ed., McGraw-Hill, 1988 (helical antenna pioneer).
3. Beverage, H. H., Rice, C. W., and Kellogg, E. W., "The Wave Antenna: A New Type of Highly Directive Antenna," *Trans. AIEE*, vol. 42, pp. 215-266, 1923.
4. Bruce, E., Beck, A. C., and Lowry, L. R., "Horizontal Rhombic Antennas," *Proc. IRE*, vol. 23, pp. 23-46, 1935.
5. Christiansen, W. N., "Directional Patterns for Rhombic Antenna," *Aust. J. Sci. Res.*, vol. A3, pp. 501-518, 1950.
6. King, H. E. and Wong, J. L., "Characteristics of 1 to 8 Wavelength Uniform Helical Antennas," *IEEE Trans. Antennas Propagat.*, vol. AP-28, No. 2, pp. 291-296, 1980.
7. Emerson, D. T., "The Gain of the Axial-Mode Helix Antenna," *Antenna Compendium*, Vol. 1, ARRL, pp. 64-69, 1985.
8. Zucker, F. J., "Surface-Wave Antennas," in *Antenna Engineering Handbook*, 4th Ed., McGraw-Hill, 2007 (Ch. 11).

---

*Last updated: 2026-04-30*
