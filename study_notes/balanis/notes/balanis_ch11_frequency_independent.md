# Chapter 11: Frequency-Independent Antennas
# 第11章：频率无关天线

> **核心思想**：频率无关天线（Frequency Independent Antenna）的阻抗、方向图和极化特性在极宽的频率范围（10:1 甚至 40:1）内保持恒定。其理论基础是 Rumsey 原理：**若天线几何形状完全由角度定义，则其电性能与频率无关**。另一类是天线小型化（Antenna Miniaturization），在保持电性能的前提下减小物理尺寸。

**章节目录**（Balanis 4th Ed. Ch11）：
- §11.1 Introduction
- §11.2 Theory — Rumsey's Principle, Scaling, Truncation
- §11.3 Equiangular Spiral Antennas
- §11.4 Archimedean Spiral Antennas
- §11.5 Log-Periodic Dipole Array (LPDA)
- §11.6 Log-Periodic Other Configurations
- §11.7 Antenna Miniaturization

---

## §11.1 Introduction

### 频率无关天线的定义与历史

频率无关天线是一类**阻抗、方向图和极化特性在极宽频带内保持近似恒定**的天线。与之相对的是窄带谐振天线（如半波偶极子，带宽仅 ~5-10%）。

- **1954年**：Edwin Turner 首次将偶极子臂缠绕成螺旋形状，发现了宽带特性
- **1957年**：V. H. Rumsey 提出频率无关天线的理论基础（Rumsey's Principle）
- **1957-1960年**：DuHamel & Isbell 发明对数周期偶极子阵列（LPDA）
- **1959年**：Dyson 发表等角螺旋天线的系统研究

### 典型带宽对比

| 天线类型 | 典型带宽（BW） | 频比范围 |
|:--------:|:--------------:|:--------:|
| 半波偶极子 | 5–10% | ~1.05:1 |
| 行波天线 | ~2:1 | 2:1 |
| 等角螺旋 | 10:1 – 40:1 | 10–40:1 |
| Archimedean 螺旋 | 5:1 – 10:1 | 5–10:1 |
| LPDA | 3:1 – 10:1 | 3–10:1 |

### 应用场景

- 电子战（ESM/ECM）宽带侦察
- 超宽带（UWB）通信
- 频谱监测与测量
- GPS 多频段接收（RHCP 螺旋天线）
- 太空探测与射电天文

### 本章结构

- **§11.2 理论**：Rumsey 原理、缩放与截断条件
- **§11.3–11.4 螺旋天线**：等角螺旋与 Archimedean 螺旋
- **§11.5–11.6 对数周期天线**：LPDA 及其他结构
- **§11.7 天线小型化**：电小天线极限与设计技术

---

## §11.2 Theory — Rumsey's Principle

### Rumsey 原理（原始表述，1957）

若一个天线的几何形状**完全由角度定义**（即不存在任何特征长度尺度），则该天线的电性能与频率无关。

数学表述：若天线形状满足

$$
\boxed{r = F(\theta, \phi)} \quad \text{(仅角度函数，无长度参数)} \tag{11-1}
$$

则对于任意频率 $f$，当频率变为 $f' = k f$ 时，天线只需按比例缩放 $1/k$ 倍，其电尺寸保持不变。

### 频率缩放的物理直觉

关键推理链：

1. Maxwell 方程在频率缩放 $f \to k f$ 下，若同时将空间坐标缩放 $r \to r/k$，则方程形式不变
2. 如果天线形状只由角度定义，则**缩放后的天线与原始天线几何完全相同**
3. 因此天线在所有频率上具有相同的电性能

### 两类满足 Rumsey 原理的结构

**A. 等角螺旋**：
$$
r = r_0 e^{a\phi} \tag{11-2}
$$
其中 $r_0$ 和 $a$ 是常数。当 $\phi \to \phi + \Delta\phi$ 时，$r \to r \cdot e^{a\Delta\phi}$，即为缩放射变换。

**B. 对数周期结构**：
几何参数按对数周期重复：
$$
\tau = \frac{L_{n+1}}{L_n} = \frac{R_{n+1}}{R_n} \quad \text{(常数)} \tag{11-3}
$$
虽然存在离散的特征长度比例因子 $\tau$，但对数周期结构的性能在 $\log f$ 坐标下是周期的，因此当 $\tau \to 1$ 时趋近于频率无关。

### 截断原理（Truncation Principle）

实际天线必须是有限尺寸。截断原理指出：

> 若电流在到达天线末端之前已衰减到足够小（通常 < -20 dB），则截断对天线性能的影响可忽略。

这对螺旋天线特别重要：**主动区（Active Region）** 的电流在辐射后迅速衰减，到达末端时已很小。

### 自互补结构（Self-Complementary Structure）

若天线的形状与其互补形状（金属 ↔ 缝隙）完全相同（旋转 90° 后重合），则为**自互补结构**。由 Babinet 原理：

$$
\boxed{Z_{\text{ant}} \cdot Z_{\text{slot}} = \frac{\eta_0^2}{4}} \tag{11-4}
$$

对于自互补天线，$Z_{\text{ant}} = Z_{\text{slot}}$，因此：

$$
\boxed{Z_{\text{ant}} = \frac{\eta_0}{2} = \frac{120\pi}{2} \approx 188.5\ \Omega} \tag{11-5}
$$

等角螺旋天线近似为自互补结构，其输入阻抗通常在 100–188 $\Omega$ 范围内。

### 主动区（Active Region）概念

这是频率无关天线最核心的物理概念：

- 在给定频率 $f$ 下，只有天线上**周长 ≈ 波长**的那部分区域参与有效辐射
- 对于螺旋天线：$\text{周长} \approx \lambda$ 的环带即为主动区
- 对于 LPDA：长度 $L_n \approx \lambda/2$ 的振子构成主动区
- 主动区随频率移动：$f \uparrow$ → 主动区向馈电端（小尺寸端）移动
- 主动区以外的部分电流很小，对辐射贡献可忽略

> **物理直觉**：想象螺旋天线在不同频率下的"有效部分"——高频时只有中心几圈工作，低频时外围大圈工作。整个天线通过在不同频率使用不同的物理部分来实现超宽带。

---

## §11.3 Equiangular Spiral Antennas

### 几何定义

等角螺旋（Log-Periodic Spiral / Equiangular Spiral）的每一臂由极坐标方程定义：

$$
\boxed{r = r_0 e^{a\phi}} \quad \text{或等价地} \quad \boxed{r = r_0 e^{a(\phi - \phi_0)}} \tag{11-6}
$$

其中：
- $r_0$：起始半径（$\phi = 0$ 处）
- $a = 1/\tan\psi$：螺旋展开速率（flare rate）
- $\psi$：螺旋角（螺旋切线与径向的夹角），对等角螺旋为常数
- $\phi$：极角

二臂等角螺旋：第二臂由第一臂旋转 180° 得到

$$
r_2 = r_0 e^{a(\phi - \pi)} \tag{11-7}
$$

### 关键设计参数

**1. 最低工作频率 $f_{\text{low}}$**（由外半径 $R_{\text{out}}$ 决定）：

$$
\boxed{R_{\text{out}} \approx \frac{\lambda_{\text{max}}}{2\pi} = \frac{c}{2\pi f_{\text{low}}}} \tag{11-8}
$$

更常用的经验公式：外圈周长 ≈ $\lambda_{\text{max}}$

$$
2\pi R_{\text{out}} \approx \lambda_{\text{max}} \quad \Rightarrow \quad R_{\text{out}} \approx \frac{\lambda_{\text{max}}}{2\pi} \tag{11-9}
$$

**2. 最高工作频率 $f_{\text{high}}$**（由内半径 $R_{\text{in}}$ 决定）：

$$
\boxed{R_{\text{in}} \approx \frac{\lambda_{\text{min}}}{4} = \frac{c}{4 f_{\text{high}}}} \tag{11-10}
$$

即馈电点附近的最小间距应 $\approx \lambda_{\text{min}}/4$。

**3. 带宽**（由内外半径比决定）：

$$
\boxed{B = \frac{f_{\text{high}}}{f_{\text{low}}} \approx \frac{R_{\text{out}}}{R_{\text{in}}}} \tag{11-11}
$$

**4. 螺旋展开速率 $a$**：
- $a$ 太小 → 螺旋缠绕过紧 → 类似电容耦合 → 辐射差
- $a$ 太大 → 螺旋展开过快 → 类似偶极子 → 窄带
- 工程推荐值：$a \approx 0.2\text{–}0.3$（常见 $a = 0.22$）

**5. 圈数 $N$**：
- 至少 0.5 圈
- 通常 1.5–3 圈
- $N = 1.5$ 是很常用的折中值

**6. 金属宽度 $w$**：
- 通常与间隙相等（自互补）
- $w = s = (R_{n+1} - R_n)/2$

### 辐射特性

**极化**：圆极化（CP）
- 从平面正面看：右手圆极化（RHCP）或左手（LHCP），由螺旋旋向决定
- 右手法则：拇指指向辐射方向，四指沿螺旋方向 → 若右手匹配则为 RHCP
- 平面等角螺旋双向辐射：正面 RHCP，反面 LHCP

**方向图**（近似公式）：

$$
\boxed{E(\theta) \approx \cos\theta} \quad \text{(宽波束，HPBW ≈ 70–90°)} \tag{11-12}
$$

更精确的方向图可用等效磁流环模型：

$$
E(\theta) \propto J_0(k a \sin\theta) - J_2(k a \sin\theta) \quad \text{(Bessel 函数近似)} \tag{11-13}
$$

其中 $a$ 为主动区平均半径。

**方向性系数**：
$$
D_0 \approx 3\text{–}4\ \text{dBi} \quad \text{(双向辐射)} \tag{11-14}
$$

Cavity-backed 单向版本：$D_0 \approx 5\text{–}7\ \text{dBi}$

**输入阻抗**：
- 自互补等角螺旋：$Z_{\text{in}} \approx 188\ \Omega$（理论值）
- 实际值：$Z_{\text{in}} \approx 100\text{–}150\ \Omega$（因介质的加载效应）
- 需用 balun 将不平衡馈电转为平衡馈电

### Cavity-Backed 等角螺旋

为了获得单向辐射，在螺旋背面加金属腔体：

- 腔体深度 $d$：通常 $\approx \lambda_{\text{max}}/4$
- 腔体直径：略大于 $2R_{\text{out}}$
- 填充吸波材料可消除腔体谐振
- 方向图：单向、宽波束、HPBW ≈ 60–80°
- 前后比（F/B）：15–20 dB

### 电流带理论（Current Band Theory）

Dyson (1959) 提出的近似模型：

1. 对于每个频率，存在一个环形"电流带"（current band）
2. 电流带中心位于周长 $\approx \lambda$ 处
3. 带内电流幅度大、几乎同相 → 有效辐射
4. 带外电流快速衰减
5. 电流衰减率由螺旋参数 $a$ 控制

---

## §11.4 Archimedean Spiral Antennas

### 几何定义

Archimedean 螺旋的半径随角度**线性增长**（而非指数）：

$$
\boxed{r = r_0 + a\phi} \tag{11-15}
$$

其中 $a$ 是螺旋臂间距参数。与等角螺旋不同，Archimedean 螺旋**不是严格的频率无关天线**——其形状包含特征长度 $a$。

二臂 Archimedean 螺旋：
$$
r_1 = r_0 + a\phi, \quad r_2 = r_0 + a(\phi - \pi) \tag{11-16}
$$

### 与等角螺旋的对比

| 特性 | 等角螺旋 | Archimedean 螺旋 |
|:----:|:--------:|:----------------:|
| 半径增长 | 指数 $e^{a\phi}$ | 线性 $a\phi$ |
| 频率无关 | 严格（角度定义） | 近似（有特征长度） |
| 阻抗带宽 | ~40:1 | ~10:1 |
| 方向图带宽 | ~10:1 | ~5:1 |
| 设计灵活性 | 参数较少 | 更易控制臂间距 |
| 制作难度 | 略高 | 较简单 |

### 设计参数

**最低频率**（由外半径 $R_{\text{out}}$ 决定）：
$$
\boxed{2\pi R_{\text{out}} \approx \lambda_{\text{max}} \;\Rightarrow\; R_{\text{out}} \approx \frac{c}{2\pi f_{\text{low}}}} \tag{11-17}
$$

**最高频率**（由内半径 $R_{\text{in}}$ 决定）：
$$
\boxed{R_{\text{in}} \approx \frac{\lambda_{\text{min}}}{4}} \tag{11-18}
$$

**臂间距 $a$** 与**圈数 $N$** 的关系：
$$
R_{\text{out}} - R_{\text{in}} = 2\pi N a \quad \Rightarrow \quad a = \frac{R_{\text{out}} - R_{\text{in}}}{2\pi N} \tag{11-19}
$$

**臂宽**（通常等于臂间距）：
$$
w = \pi a \quad \text{(用于自互补设计)} \tag{11-20}
$$

### 多臂 Archimedean 螺旋

4 臂 Archimedean：
$$
r_m = r_0 + a\left(\phi - \frac{2\pi m}{N_{\text{arms}}}\right), \quad m = 0, 1, \dots, N_{\text{arms}}-1 \tag{11-21}
$$

多臂的优势：
- 更对称的方向图
- 可产生多种极化模式
- 4 臂可用相位馈电实现轴向模或锥形模

### 辐射特性

- **极化**：圆极化（主波束方向）
- **HPBW**：70–90°（双向），60–80°（单向）
- **方向性系数**：$D_0 \approx 3\text{–}4$ dBi（双向）
- **输入阻抗**：$Z_{\text{in}} \approx 50\text{–}200\ \Omega$（与 $w/s$ 比相关）
- **AR（轴比）带宽**：可达 5:1（AR < 3 dB）

### Cavity-Backed Archimedean 螺旋

- 最常用的工程实现形式
- 腔体填充吸波材料 → 单向辐射
- 腔体深度对带宽影响不大（因电流在到达末端前已衰减）
- 典型增益：5–7 dBi（含腔体）
- 广泛应用于 1–18 GHz 电子战系统

---

## §11.5 Log-Periodic Dipole Array (LPDA)

### 几何结构与参数定义

LPDA 是一组长度递增的平行偶极子，相邻振子交替馈电（相位差 180°），沿传输线排列。

**四个关键设计参数**：

$$
\boxed{\tau = \frac{L_{n+1}}{L_n} = \frac{R_{n+1}}{R_n} = \frac{d_{n+1}}{d_n}} \quad \text{(缩放因子, 0 < \tau < 1)} \tag{11-22}
$$

$$
\boxed{\sigma = \frac{S_n}{2L_n}} \quad \text{(相对间距常数)} \tag{11-23}
$$

其中 $S_n = d_n - d_{n+1}$ 为相邻振子间距，$d_n$ 为第 $n$ 个振子到顶点的距离。

$$
\boxed{\alpha = \tan^{-1}\left(\frac{1-\tau}{4\sigma}\right)} \quad \text{(半顶角)} \tag{11-24}
$$

$$
\boxed{\sigma_{\text{opt}} = 0.243\tau - 0.051} \quad \text{（Carrel 最优} \sigma \text{线，用于最大方向性）} \tag{11-25}
$$

### 振子几何计算

给定 $\tau$、$\sigma$、最低频率 $f_{\text{low}}$ 和最高频率 $f_{\text{high}}$：

**最长振子**（对应 $f_{\text{low}}$）：
$$
L_1 = \frac{\lambda_{\text{max}}}{2} = \frac{c}{2 f_{\text{low}}} \tag{11-26}
$$

**振子长度序列**：
$$
L_n = L_1 \cdot \tau^{n-1} \tag{11-27}
$$

**振子间距**：
$$
S_n = 2\sigma L_n \tag{11-28}
$$

**顶点到第 n 个振子的距离**：
$$
d_n = \frac{L_n}{2\tan\alpha} \quad \text{或迭代} \quad d_{n+1} = d_n - S_n \tag{11-29}
$$

### 主动区概念

LPDA 的主动区满足：振子长度 $L_n \approx \lambda/2$。

给定频率 $f$，主动区中心位于满足 $L_n = c/(2f)$ 的振子附近。主动区内一般包含 **3–5 个振子**。

**主动区带宽** $B_{\text{ar}}$：
$$
\boxed{B_{\text{ar}} \approx 1.1 + 7.7(1-\tau)^2\cot\alpha} \quad \text{(Carrel 公式)} \tag{11-30}
$$

**结构带宽** $B_s$：
$$
\boxed{B_s = B \cdot B_{\text{ar}}} \quad \text{其中 } B = \frac{f_{\text{high}}}{f_{\text{low}}} \tag{11-31}
$$

**所需振子数** $N$：
$$
\boxed{N = 1 + \frac{\log(B_s)}{\log(1/\tau)}} \tag{11-32}
$$

### Carrel 设计步骤（1961）

1. 指定 $f_{\text{low}}$、$f_{\text{high}}$、期望方向性 $D_0$（dBi）
2. 从 Carrel 的 $D_0$ vs $\tau,\sigma$ 曲线选择 $\tau$ 和 $\sigma$
3. 由 $\tan\alpha = (1-\tau)/(4\sigma)$ 计算 $\alpha$
4. 计算 $L_1 = c/(2f_{\text{low}})$
5. 计算 $B_{\text{ar}}$ 和 $B_s$
6. 计算振子数 $N$
7. 计算所有 $L_n$、$S_n$、$d_n$

**工程经验值**：
- $\tau = 0.84\text{–}0.96$（高 $\tau$ → 高增益，更多振子）
- $\sigma = 0.04\text{–}0.12$（接近最优 $\sigma$ 时增益最大）
- $D_0 = 6\text{–}12$ dBi（取决于 $\tau,\sigma$）
- 典型增益：$\tau=0.88,\sigma=0.06$ → $D_0 \approx 7.5$ dBi

### 方向图计算

LPDA 的方向图由所有振子的叠加得到（需考虑馈电相位）：

主动区内振子的近似方向图（短偶极子近似）：

$$
F_n(\theta) = \frac{\cos\left(\frac{kL_n}{2}\cos\theta\right) - \cos\left(\frac{kL_n}{2}\right)}{\sin\theta} \tag{11-33}
$$

阵列因子（考虑交替馈电的 180° 相移）：

$$
AF(\theta) = \sum_{n=1}^{N} I_n e^{j k d_n \cos\theta} \cdot e^{j(n-1)\pi} \tag{11-34}
$$

其中 $I_n$ 为各振子电流幅度（主动区内最大，两侧衰减）。

简化的电流幅度分布（主动区模型）：
$$
|I_n| \propto \begin{cases}
e^{-\alpha (n - n_0)^2} & \text{靠近主动区}\\
0 & \text{远离主动区}
\end{cases} \tag{11-35}
$$

### 方向性系数估算

粗略估计（Carrel 方法）：
$$
\boxed{D_0 \approx 10\log_{10}\left[\frac{4\pi \cot\alpha}{\Omega_a}\right]} \quad \text{(dBi)} \tag{11-36}
$$

其中 $\Omega_a$ 是主动区的平均波束立体角。

也可使用工程表格（见 §11.5 的增益表）。

### LPDA 馈电与阻抗

- 传输线特性阻抗 $Z_0$ 通常为 50–200 $\Omega$
- 振子通过交替连接（transpose）实现 180° 相移
- 输入阻抗近似：$Z_{\text{in}} \approx \sqrt{Z_0 \cdot R_{\text{av}}}$
- 典型 VSWR < 2:1 在整个频带内

---

## §11.6 Log-Periodic Other Configurations

### Log-Periodic Zigzag Antenna

- 用折线（zigzag）替代偶极子阵列
- 结构更紧凑，适合较低频率
- 可选平面或锥形结构
- 辐射特性与 LPDA 类似但增益略低

### Log-Periodic Slot Antenna

- 使用缝隙替代偶极子
- 互补结构 → 阻抗为 LPDA 的 $\eta_0^2/(4Z_{\text{LPDA}})$
- 适用于与金属表面共形安装
- 典型增益：5–7 dBi

### Log-Periodic Toothed Planar Antenna

- 平面齿形结构
- 自互补 → 188 $\Omega$ 输入阻抗
- 圆极化（在特定频段）
- 带宽可达 10:1

### Conical Log-Spiral Antenna

- 三维锥形螺旋
- 单向辐射（沿锥尖方向）
- 圆极化
- 极宽带宽（可达 20:1）
- 用于测向和宽带监测

---

## §11.7 Antenna Miniaturization

### 电小天线定义

**电小天线（Electrically Small Antenna, ESA）**：天线的最大尺寸 $a$ 满足：

$$
\boxed{ka < 0.5 \quad \text{或} \quad a \ll \lambda/2\pi} \tag{11-37}
$$

其中 $k = 2\pi/\lambda$，$a$ 为包围天线最小球的半径（Wheeler's radian sphere）。

### 基本极限

#### Wheeler 的 Radian Sphere

包围天线的半径为 $a$ 的球体称为 radian sphere。球外的场是辐射场，球内主要存储电抗能量。

#### Chu-Harrington 极限（天线 Q 值的下限）

对于一个包围在半径为 $a$ 的球体内的天线，其最小可能 Q 值为（假设仅激发 TM₁₀ 模）：

$$
\boxed{Q_{\text{Chu}} \approx \frac{1}{(ka)^3} + \frac{1}{ka}} \tag{11-38}
$$

对于 $ka \ll 1$，主导项为：

$$
\boxed{Q_{\text{Chu}} \approx \frac{1}{(ka)^3}} \tag{11-39}
$$

**物理含义**：
- 天线尺寸越小 → Q 值越高 → 阻抗带宽越窄
- $Q$ 与 $1/(ka)^3$ 成正比，意味着缩小一半 → Q 增加 8 倍
- 带宽与 Q 的关系：$BW \approx 1/Q$（对匹配良好的天线）

#### 增益-带宽-尺寸折中

$$
\boxed{G \cdot BW \cdot (ka)^3 \lesssim \text{常数}} \tag{11-40}
$$

即：小型化必须以牺牲增益或带宽为代价。

### 小型化技术

#### 1. 感性/容性加载（Lumped Loading）

在偶极子臂上串联电感或并联电容以降低谐振频率：

$$
f_{\text{res}} \downarrow = \frac{1}{2\pi\sqrt{L_{\text{eff}} C_{\text{eff}}}} \tag{11-41}
$$

- **优点**：设计简单
- **缺点**：欧姆损耗 → 效率降低；Q 升高 → 带宽变窄

#### 2. 分布加载（Dielectric/Magnetic Loading）

用高介电常数 $\epsilon_r$ 或高磁导率 $\mu_r$ 材料包围天线：

$$
\lambda_{\text{eff}} = \frac{\lambda_0}{\sqrt{\mu_r \epsilon_r}} \tag{11-42}
$$

- 应用：陶瓷贴片天线、铁氧体加载
- 限制：材料损耗、重量、温度稳定性

#### 3. 曲折线/弯折结构（Meander Line）

将偶极子臂设计为蛇形/弯折路径，在有限空间内延长有效电流路径：

- 有效长度 $L_{\text{eff}} > L_{\text{phys}}$
- 谐振频率降低，但方向图退化
- 增益损失：通常 2–6 dB（视小型化程度）
- 应用：RFID 标签、移动设备天线

**等效电路**：每个弯折引入串联电感和相邻间的分布电容

$$
f_{\text{res}} = \frac{1}{2\pi\sqrt{(L_{\text{base}} + \Delta L)C_{\text{base}}}} \tag{11-43}
$$

#### 4. 单极子与地平面加载

- 四分之一波长单极子 $\to$ 通过顶加载（top-loading）缩短
- 电容性顶加载：如圆盘、伞形线
- 工字形（ILA）、倒F 天线（IFA）、平面倒F（PIFA）

#### 5. 分形天线（Fractal Antenna）

- 利用分形的空间填充特性在有限面积内延长电流路径
- Koch 分形、Sierpinski 垫片等
- 多频段特性（Sierpinski 偶极子）
- 小型化效果：15–40% 的尺寸缩减

### 小型化性能折中

| 技术 | 尺寸缩减 | 增益损失 | 带宽缩减 | 复杂度 |
|:----:|:--------:|:--------:|:--------:|:------:|
| 感性加载 | 30–50% | 1–3 dB | 50–80% | 低 |
| 介电加载 | 20–40% | 0.5–1 dB | 30–50% | 中 |
| 曲折线 | 30–60% | 2–6 dB | 50–90% | 低 |
| 顶加载 | 30–50% | 1–2 dB | 40–60% | 中 |
| 分形 | 15–40% | 1–4 dB | 30–70% | 中 |

### 设计原则总结

天线的**小型化不可能三角**：

> **Size × Bandwidth × Efficiency ≈ Constant**

- 减小尺寸 → 带宽变窄 且/或 效率降低
- Chu-Harrington 极限是物理不可超越的硬限制
- 合理的工程目标是**逼近但不超过**该极限的 2–3 倍

---


| 公式编号 | 内容 | 表达式 |
|:--------:|:----|:-------|
| (11-2) | 等角螺旋 | $r = r_0 e^{a\phi}$ |
| (11-4) | 自互补阻抗 | $Z_{\text{ant}} = \eta_0/2 = 188.5\ \Omega$ |
| (11-9) | 最低频率 | $R_{\text{out}} \approx \lambda_{\text{max}}/(2\pi)$ |
| (11-10) | 最高频率 | $R_{\text{in}} \approx \lambda_{\text{min}}/4$ |
| (11-15) | Archimedean 螺旋 | $r = r_0 + a\phi$ |
| (11-22) | LPDA \tau | $\tau = L_{n+1}/L_n$ |
| (11-23) | LPDA \sigma | $\sigma = S_n/(2L_n)$ |
| (11-24) | LPDA \alpha | $\alpha = \tan^{-1}[(1-\tau)/(4\sigma)]$ |
| (11-38) | Chu 极限 | $Q_{\text{Chu}} \approx 1/(ka)^3 + 1/(ka)$ |
