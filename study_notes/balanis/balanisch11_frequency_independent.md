# Chapter 11: Frequency Independent Antennas, Antenna Miniaturization, and Fractal Antennas

> Balanis, *Antenna Theory: Analysis and Design*, 4th Edition — Chapter 11

---

## 11.1 Introduction

传统天线（偶极子、喇叭等）的阻抗和方向图随频率剧烈变化，带宽通常有限（ $\lesssim 10\%$ ）。频率无关天线通过**角度决定形状**的几何结构实现超宽带工作，典型带宽比可达 $10:1$ 甚至 $40:1$。

**核心思想（Rumsey, 1957）：** 若天线的形状仅由角度决定（长度尺寸可随频率缩放），则其电性能与频率无关。数学上，若天线结构在球坐标系中表示为：

$$
r = F(\theta, \phi)
$$

其中 $F$ 不含长度量纲（即角度函数），则该天线满足频率无关条件。

**实际约束：**
- 天线必须有**有限截断**（有限尺寸），决定了低频限
- 馈电区的精细结构决定了高频限
- 实用天线需在截断处电流衰减足够强，使得截断效应可忽略

---

## 11.2 频率无关理论

### Rumsey 原理

考虑一个由角度 $\theta, \phi$ 完全决定的天线表面方程：

$$
r = e^{a\phi} f(\theta)
$$

其中 $a$ 为常数，$f(\theta)$ 为任意函数。若将工作频率从 $f$ 变为 $kf$，则天线上所有电流分布及其产生的场在缩放的球坐标中保持不变。这就是**频率无关**的本质。

### 工作频带

- **低频限 $f_{\text{low}}$**：由天线最大尺寸 $r_{\text{max}}$ 决定
  $$
  f_{\text{low}} \approx \frac{c}{2\pi r_{\text{max}}}
  $$

  实用规律：最低频对应的波长等于螺旋外周长，即 $\lambda_{\text{low}} = 2\pi r_{\text{max}}$

- **高频限 $f_{\text{high}}$**：由馈电区精细结构（最小尺寸 $r_{\text{min}}$）决定
  $$
  f_{\text{high}} \approx \frac{c}{2\pi r_{\text{min}}}
  $$

### 有效辐射区域（Active Region）

频率无关天线上，仅在周长约等于一个波长的环带区域发生有效辐射（active region）。随频率变化，active region 沿天线结构平移，因此远场方向图和阻抗保持不变。

### 电流衰减

天线截断处电流幅度必须远小于馈电处，以保证截断对性能影响可忽略。这要求螺旋或对数周期结构上的行波衰减足够强（通常 $>20$ dB）。

---

## 11.3 等角螺旋天线（Equiangular Spiral Antenna）

### 平面等角螺旋

由 Dyson (1959) 提出。单臂的极坐标方程为：

$$
r = r_0 e^{a\phi}
$$

其中：
- $r_0$：初始半径（$\phi=0$ 时）
- $a = 1/\tan\psi_0$：展开率
- $\psi_0$：螺旋臂与径向线的夹角（螺旋角），典型值 $70^\circ \lesssim \psi_0 \lesssim 85^\circ$

**自补结构：** 当螺旋臂宽等于臂间间距时，结构为自补（self-complementary），输入阻抗由 Booker's relation 给出：

$$
Z_{\text{in}} = \frac{\eta_0}{2} \approx 188.5\ \Omega
$$

其中 $\eta_0 = 120\pi \approx 377\ \Omega$ 为自由空间波阻抗。

### 双臂等角螺旋天线

双臂由两条镜像螺旋构成：
$$
\begin{aligned}
\text{臂 1:}\quad & r_1 = r_0 e^{a\phi} \\
\text{臂 2:}\quad & r_2 = r_0 e^{a(\phi - \pi)}
\end{aligned}
$$

**辐射特性：**
- 双向辐射（垂直于螺旋平面）
- 圆极化（CP），旋向与螺旋绕向一致
- HPBW $\approx 70^\circ$–$90^\circ$
- 轴向比 AR $\lesssim 3$ dB（宽频带内）
- 增益 $\approx 3$–$6$ dBi（取决于螺旋尺寸）

### 圆锥等角螺旋

将平面螺旋投影到锥面上，实现**单向辐射**。锥角 $2\theta_0$ 控制波束指向。

圆锥螺旋的曲面方程：
$$
r = r_0 e^{a\phi} \quad\text{在锥面}\ \theta = \theta_0\ \text{上}
$$

当锥角 $2\theta_0$ 较小时，波束指向锥尖方向；较大时波束变宽。

### 电流带理论（Current Band Theory）

对于 $N$ 臂螺旋，电流在螺旋臂上传播，当周长 $C \approx n\lambda$（$n$ 为整数模数）时发生共振辐射。双臂螺旋主要工作于 $n=1$ 模。

**关键参数关系：**

| 参数 | 符号 | 典型值 | 影响 |
|:----:|:----:|:------:|:------|
| 螺旋角 | $\psi_0$ | $70^\circ$–$85^\circ$ | 展开率、带宽 |
| 外半径 | $r_{\text{max}}$ | $\lambda_{\text{low}}/(2\pi)$ | 低频限 |
| 内半径 | $r_{\text{min}}$ | $\lambda_{\text{high}}/(2\pi)$ | 高频限 |
| 臂数 | $N_{\text{arm}}$ | 2, 4 | 模数控制 |

---

## 11.4 对数周期天线（Log-Periodic Antennas）

### 基本概念

由 DuHamel 和 Isbell (1957) 提出。结构参数随对数周期重复，使得天线的电性能以 $\ln f$ 为周期周期性变化。若周期足够小，则宏观上表现为频率无关。

**对数周期结构定义：** 各相邻单元满足缩放因子：
$$
\tau = \frac{R_{n+1}}{R_n} = \frac{l_{n+1}}{l_n}
$$

其中 $\tau$ 称为**缩放因子**（或周期比），$0 < \tau < 1$。

当频率变化 $\Delta f$ 满足 $f_{n+1} / f_n = 1/\tau$ 时，天线的电性能重复。

### 对数周期偶极子阵列（LPDA）

LPDA 是最广泛使用的对数周期天线形式，结构参数包括：

$$
\tau = \frac{l_{n+1}}{l_n} = \frac{R_{n+1}}{R_n}
$$

$$
\sigma = \frac{d_n}{2 l_n} = \frac{R_n - R_{n+1}}{2 l_n}
$$

其中：
- $l_n$：第 $n$ 个偶极子长度
- $R_n$：第 $n$ 个偶极子到顶点的距离
- $d_n$：第 $n$ 和 $n+1$ 个偶极子间距
- $\tau$：缩放因子（$0.8 \le \tau \le 0.98$）
- $\sigma$：相对间距

**张角半角（apex half-angle）：**
$$
\alpha = \tan^{-1}\left(\frac{1-\tau}{4\sigma}\right)
$$

### Carrel 设计流程 (1961)

Carrel 给出了完整的 LPDA 工程设计方法。

**步骤 1：选择设计参数**

根据所需增益 $G$ 从 Carrel 等增益曲线（$\tau$-$\sigma$ 平面）选择 $(\tau, \sigma)$ 组合。

经验最优间距：
$$
\sigma_{\text{opt}} = 0.243\tau - 0.051
$$

**步骤 2：计算活动区带宽**

$$
B_{\text{ar}} = 1.1 + 7.7(1-\tau)^2 \cot\alpha
$$

其中 $\cot\alpha = 4\sigma / (1-\tau)$。

**步骤 3：计算结构带宽**

$$
B_s = B \cdot B_{\text{ar}} = \frac{f_{\text{max}}}{f_{\text{min}}} \cdot B_{\text{ar}}
$$

**步骤 4：计算阵元数量**

$$
N = 1 + \frac{\ln B_s}{\ln(1/\tau)}
$$

需四舍五入为整数。

**步骤 5：计算阵元尺寸**

最长阵元（$n=1$）：
$$
l_1 = \frac{\lambda_{\text{max}}}{2} = \frac{c}{2f_{\text{min}}}
$$

$$
R_1 = \frac{l_1}{2} \cot\alpha
$$

后续阵元递推：
$$
l_{n+1} = \tau l_n,\quad R_{n+1} = \tau R_n
$$

**步骤 6：馈线设计**

馈线特征阻抗 $Z_0$ 与输入阻抗 $Z_{\text{in}}$、阵元平均特性阻抗 $\bar{Z}_a$ 相关。

阵元 $n$ 的平均特性阻抗（l/d 为长径比）：
$$
Z_{a_n} = 120\left[\ln\left(\frac{l_n}{d_n}\right) - 2.25\right]
$$

Carrel 给出最佳馈线阻抗：
$$
Z_0 = \frac{Z_{\text{in}}^2}{8\sigma' \bar{Z}_a} + Z_{\text{in}} \sqrt{\left(\frac{Z_{\text{in}}}{8\sigma' \bar{Z}_a}\right)^2 + 1}
$$

其中 $\sigma' = \sigma / \sqrt{\tau}$。

**偶极子交错馈电（phase reversal）：** 相邻偶极子馈电相位反转 $180^\circ$，使波束指向顶点方向（端射方向）。这是通过交替连接馈线两导线实现的（criss-cross 连接）。

### LPDA 辐射特性

**典型参数范围与性能：**

| 参数 | 符号 | 典型值范围 | 说明 |
|:----:|:----:|:----------:|:------|
| 缩放因子 | $\tau$ | $0.8$–$0.98$ | 越大增益越高，阵元数越多 |
| 相对间距 | $\sigma$ | $0.03$–$0.06$ | 存在最优值 |
| 张角 | $2\alpha$ | $10^\circ$–$45^\circ$ | 由 $\tau,\sigma$ 决定 |
| 增益 | $G$ | $6$–$11$ dBi | 随 $\tau$ 增大而增大 |
| 前后比 | F/B | $10$–$25$ dB | 高 $\tau$ 时更好 |
| 输入阻抗 | $Z_{\text{in}}$ | $50$–$300\ \Omega$ | 通过馈线设计匹配 |
| 阵元数 | $N$ | $4$–$20$+ | 取决于带宽和 $\tau$ |

### LPDA 方向图近似

LPDA 方向图可以用均匀线阵模型近似，但需考虑：
1. 只有 active region 内的阵元（约 $\lambda/2$ 附近 3–4 个阵元）有效辐射
2. 阵元从最长到最短的幅度分布近似为高斯或三角分布
3. 相邻阵元 $180^\circ$ 相位反转

**简化的有效阵列因子（active region approximation）：**

$$
AF(\theta) \approx \sum_{n=N_{\text{low}}}^{N_{\text{high}}} I_n e^{j k R_n \cos\theta} (-1)^n
$$

其中 $(-1)^n$ 表示相邻交错。

---

## 11.5 阿基米德螺旋天线（Archimedean Spiral Antenna）

### 几何定义

与等角螺旋不同，阿基米德螺旋的半径随角度线性增长：

$$
r = r_0 + a\phi
$$

其中 $a$ 为常数（螺距参数）。双臂结构：
$$
\begin{aligned}
\text{臂 1:}\quad & r_1 = r_0 + a\phi \\
\text{臂 2:}\quad & r_2 = r_0 + a(\phi - \pi)
\end{aligned}
$$

### 与等角螺旋的区别

| 特性 | 等角螺旋 | 阿基米德螺旋 |
|:----:|:---------|:------------|
| 增长律 | 指数 $r = r_0 e^{a\phi}$ | 线性 $r = r_0 + a\phi$ |
| 带宽 | 极宽（理论无限） | 宽（数倍频程） |
| 低频限 | 外半径决定 | 外半径决定 |
| 自补 | 可以 | 有限范围内近似 |

### 辐射特性

阿基米德螺旋的 active region 在周长 $\approx \lambda$ 处。由于不满足严格的角度条件，其频率无关性不如等角螺旋理想，但制造更简单。

**典型性能：**
- 带宽比：$4:1$–$10:1$
- 增益：$3$–$5$ dBi
- 圆极化纯度：AR $\approx 3$ dB
- HPBW：$70^\circ$–$85^\circ$

---

## 11.6 天线小型化（Antenna Miniaturization）

### 基本限制

天线小型化受 Chu-Harrington 极限约束：

$$
Q \ge \frac{1}{(ka)^3} + \frac{1}{ka}
$$

其中 $a$ 为包围天线的最小球半径，$k$ 为波数。这意味着小天线具有高 $Q$、窄带宽。

### 小型化技术

1. **介质加载**：使用高 $\epsilon_r$ 介质降低谐振频率，但会降低效率
2. **短路加载**：在合适位置加短路探针或短路壁
3. **集总元件加载**：串联/并联电感、电容
4. **分形结构**：利用分形几何的自相似性实现多频/宽带小型化

---

## 11.7 分形天线（Fractal Antennas）

### 分形的自相似性

分形结构在不同尺度上重复相同的几何图案。这理论上可以实现频率无关特性，因为天线在不同频率看到相同的几何形状。

**常见分形天线类型：**
- Koch 曲线（偶极子）
- Sierpinski 垫片（贴片、单极子）
- Hilbert 曲线（小型化线天线）
- Minkowski 环（分形环）

### Koch 偶极子

Koch 曲线的迭代过程：将直线段中间 1/3 替换为等边三角形的两条边（缺一边）。

- 第 $n$ 次迭代长度：$L_n = L_0 (4/3)^n$
- 在固定物理长度内，电长度显著增加
- 谐振频率降低（相对于同样物理尺寸的直线偶极子）
- 辐射电阻降低，$Q$ 升高

**分形维数（Hausdorff）：**
$$
D = \frac{\ln N}{\ln r} = \frac{\ln 4}{\ln 3} \approx 1.262
$$

其中 $N$ 为自相似段数，$r$ 为缩放因子。

### Sierpinski 单极子

基于 Sierpinski 垫片的分形单极子，具有对数周期特性——在不同频段呈现相似的辐射方向图。

---

## 关键公式总结

| 公式 | 含义 |
|:----|:------|
| $r = r_0 e^{a\phi}$ | 等角螺旋方程，$a=1/\tan\psi_0$ |
| $r = r_0 + a\phi$ | 阿基米德螺旋方程 |
| $\tau = l_{n+1}/l_n$ | LPDA 缩放因子 |
| $\sigma = d_n/(2l_n)$ | LPDA 相对间距 |
| $\alpha = \tan^{-1}[(1-\tau)/(4\sigma)]$ | LPDA 张角半角 |
| $\sigma_{\text{opt}} = 0.243\tau - 0.051$ | 最优相对间距 |
| $B_{\text{ar}} = 1.1 + 7.7(1-\tau)^2\cot\alpha$ | 活动区带宽 |
| $N = 1 + \ln B_s / \ln(1/\tau)$ | 阵元数 |
| $Z_{\text{in}} = \eta_0/2$ (自补结构) | 自补天线输入阻抗 |
| $f_{\text{low}} \approx c/(2\pi r_{\text{max}})$ | 螺旋低频截止 |
| $Q \ge 1/(ka)^3 + 1/(ka)$ | Chu 小型化极限 |

---

## 工程应用指南

1. **等角螺旋**：适用于需要极宽带宽（$>10:1$）和圆极化的场合，如 ESM、宽带监测
2. **阿基米德螺旋**：制造简单，适合 $4:1$–$10:1$ 带宽应用
3. **LPDA**：线极化、中等增益（$6$–$11$ dBi）、宽带宽，适用于电视接收、EMC 测量、宽带通信
4. **分形天线**：小型化需求为主，多频段/多标准终端

---

## 参考文献

1. V. H. Rumsey, "Frequency Independent Antennas," *IRE National Convention Record*, vol. 5, part 1, pp. 114–118, 1957.
2. R. H. DuHamel and D. E. Isbell, "Broadband Logarithmically Periodic Antenna Structures," *IRE National Convention Record*, vol. 5, part 1, pp. 119–128, 1957.
3. J. D. Dyson, "The Equiangular Spiral Antenna," *IRE Trans. Antennas Propagat.*, vol. AP-7, pp. 181–187, April 1959.
4. R. Carrel, "The Design of Log-Periodic Dipole Antennas," *IRE Int. Convention Record*, vol. 9, pp. 61–75, 1961.
5. R. H. DuHamel and J. P. Scherer, "Frequency-Independent Antennas," in *Antenna Engineering Handbook*, 3rd ed., R. C. Johnson, Ed. McGraw-Hill, 1993, Ch. 14.
6. C. A. Balanis, *Antenna Theory: Analysis and Design*, 4th ed. Wiley, 2016, Ch. 11.
