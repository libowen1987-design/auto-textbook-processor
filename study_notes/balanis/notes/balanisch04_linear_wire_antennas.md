# Chapter 4: Linear Wire Antennas
# 第4章：线天线
> Balanis, *Antenna Theory: Analysis and Design*, 4th Edition — Chapter 4

---

## 4.1 Introduction

线天线是最基础也是最广泛使用的天线类型。本章从**无穷小偶极子**（电流元）出发，逐步推广到有限长度偶极子、半波偶极子，再到工程实用的折合偶极子、套筒偶极子、Yagi-Uda 和 LPDA 天线。

**核心方法：** 已知电流分布 → 矢量位积分 → 远场方向图 / 辐射阻抗

---


长度 $l \ll \lambda$，均匀电流分布 $I = I_0 \hat{z}$。

### 矢量位

磁矢量位 $\mathbf{A}$ 沿 $z$ 轴：
$$
A_z = \frac{\mu_0 I_0 l}{4\pi} \frac{e^{-jkr}}{r}
$$

在球坐标系下分解：
$$
\begin{aligned}
A_r &= A_z \cos\theta \\
A_\theta &= -A_z \sin\theta \\
A_\phi &= 0
\end{aligned}
$$

### 远场辐射场

由 $\mathbf{H} = \frac{1}{\mu_0} \nabla \times \mathbf{A}$ 和 $\mathbf{E} = \frac{1}{j\omega\epsilon_0} \nabla \times \mathbf{H}$，在远区 ($r \to \infty$)：

$$
\begin{aligned}
E_\theta &\approx j\eta \frac{k I_0 l e^{-jkr}}{4\pi r} \sin\theta \\
H_\phi &\approx j \frac{k I_0 l e^{-jkr}}{4\pi r} \sin\theta \\
E_r &\approx E_\phi = H_r = H_\theta \approx 0
\end{aligned}
$$

> 远场为 TEM 波：$\mathbf{E} \perp \mathbf{H} \perp \hat{r}$，$E_\theta = \eta H_\phi$

### 方向图

$$
F(\theta) = \sin\theta
$$

- **E 面** ($\phi = \text{const}$)：8 字形（doughnut 截面）
- **H 面** ($\theta = \pi/2$)：均匀（圆）
- HPBW：$90^\circ$
- 方向性：$D_0 = 1.5$ (1.76 dB)

### 辐射电阻

$$
R_r = 80\pi^2 \left(\frac{l}{\lambda}\right)^2 = 20k^2 l^2
$$

### 场区边界

| 区域 | 条件 | 特征 |
|:----:|:----:|:------|
| 反应近场区 | $r < 0.62\sqrt{l^3/\lambda}$ | 储能场为主，$r^{-3}$ 项主导 |
| 辐射近场区 (Fresnel) | $0.62\sqrt{l^3/\lambda} < r < 2l^2/\lambda$ | 有径向分量 |
| 远场区 (Fraunhofer) | $r > 2l^2/\lambda$ | TEM 球面波 |

---


$l < \lambda/10$，但 $l$ 不可忽略。沿线电流近似三角分布（两端为零）：

$$
I(z') = I_0 \left(1 - \frac{2|z'|}{l}\right), \quad -l/2 \leq z' \leq l/2
$$

### 远场

$$
E_\theta \approx j\eta \frac{k I_0 l e^{-jkr}}{4\pi r} \cdot \frac{1}{2} \sin\theta
$$

与无穷小偶极子相比，幅度减半（等效为电流平均值）。

### 辐射电阻

$$
R_r = 20\pi^2 \left(\frac{l}{\lambda}\right)^2
$$

比无穷小偶极子小 4 倍（因为三角分布的平均电流是均匀分布的一半）。

---


对于长度 $l$ 位于 $z$ 轴的偶极子，电流分布近似正弦：

$$
I(z') = I_0 \sin\left[k\left(\frac{l}{2} - |z'|\right)\right], \quad -l/2 \leq z' \leq l/2
$$

### 矢量位

$$
A_z = \frac{\mu_0}{4\pi} \int_{-l/2}^{l/2} I(z') \frac{e^{-jkR}}{R} dz'
$$

### 远场积分

对于远区 $R \approx r - z'\cos\theta$：

$$
\begin{aligned}
E_\theta &\approx j\eta \frac{I_0 e^{-jkr}}{2\pi r} 
          \frac{\cos\left(\frac{kl}{2}\cos\theta\right) - \cos\left(\frac{kl}{2}\right)}{\sin\theta} \\
H_\phi &= \frac{E_\theta}{\eta}
\end{aligned}
$$

### 归一化方向图函数

$$
F(\theta) = \frac{\cos\left(\frac{kl}{2}\cos\theta\right) - \cos\left(\frac{kl}{2}\right)}{\sin\theta}
$$

### 特殊情况

**$\lambda/2$ 偶极子 ($l = \lambda/2$)：**

$$
F(\theta) = \frac{\cos\left(\frac{\pi}{2}\cos\theta\right)}{\sin\theta}
$$

- HPBW ≈ $78^\circ$
- 方向性 $D_0 \approx 1.643$ (2.15 dB)
- 辐射阻抗 $Z_{\text{in}} \approx 73 + j42.5\ \Omega$
- 谐振时有 $X_{\text{in}} \approx 0$ (实际在 $l \approx 0.47\lambda$)

**全波偶极子 ($l = \lambda$)：**

$$
F(\theta) = \frac{\cos(\pi\cos\theta) + 1}{\sin\theta}
$$

- 方向性 $D_0 \approx 2.41$ (3.82 dB)
- 辐射阻抗 $Z_{\text{in}} \approx 199 - j200\ \Omega$ (高阻、高容性)

**$l = 1.25\lambda$：**

- 方向图出现旁瓣
- 方向性达到约 3.3 (5.2 dB) 的峰值

---


半波偶极子是工程中最常用的线天线。

### 远场方向图

$$
\mathbf{E}_\theta \approx j\eta \frac{I_0 e^{-jkr}}{2\pi r} \frac{\cos\left(\frac{\pi}{2}\cos\theta\right)}{\sin\theta}
$$

### 关键参数

| 参数 | 数值 |
|:----|:----:|
| 方向性 $D_0$ | 1.643 (2.15 dBi) |
| 最大有效口径 $A_{em}$ | $0.13\lambda^2$ |
| 辐射电阻 $R_r$ | 73 $\Omega$ |
| 输入电抗 $X_{\text{in}}$ | $+42.5\ \Omega$（谐振需缩短至 $0.47\lambda$） |
| HPBW | $78^\circ$ |
| FNBW | $180^\circ$ |

### 辐射电阻计算

$$
R_r = \frac{\eta}{2\pi} \left[ \gamma + \ln(2\pi) - C_i(2\pi) + \frac{1}{2} \sin(2\pi) [S_i(4\pi) - 2S_i(2\pi)] \right. \\
\left. + \frac{1}{2} \cos(2\pi) [\gamma + \ln(\pi) + C_i(4\pi) - 2C_i(2\pi)] \right] \approx 73\ \Omega
$$

其中 $\gamma = 0.5772$（Euler 常数），$C_i(x)$ 和 $S_i(x)$ 分别是余弦和正弦积分。

### 工程应用

- 中心馈电，阻抗 ~73 $\Omega$（接近 75 $\Omega$ 同轴线）
- 带宽约 10%
- Flattened 形式：臂与天线成 180°，由传输线约 73 Ω 馈电

---


### 4.6.1 Folded Dipole（折合偶极子）

由两个平行的 \lambda/2 偶极子在端部连接构成。

**特性：**
- 输入阻抗约为标准偶极子的 4 倍：$Z_{\text{in}} \approx 4 \times 73 \approx 300\ \Omega$
- 带宽更宽（~20%）
- 方向图与标准半波偶极子相同
- 常用于 Yagi 天线作为驱动单元（匹配 300 Ω 双线）

**原理：** 两臂电流相等同相 → 辐射功率同 → 输入电流减半 → 阻抗升 4 倍。

### 4.6.2 Sleeve Dipole（套筒偶极子）

- 利用同轴线的外导体形成套筒，用于宽带匹配
- 可实现 2:1 以上的阻抗带宽
- 方向图略微不对称

### 4.6.3 Biconical Dipole / Discone

- 宽带（10:1 带宽）阻抗特性
- 属于行波天线大类
- 用作宽带接收天线、EMC 测试天线

---

## 4.7 Antenna Impedance and Mutual Impedance

### 自阻抗 (Self-Impedance)

偶极子的输入阻抗由 Poynting 矢量法或感应 EMF 法计算。

**感应 EMF 法**（仅对细导线准确）：
$$
Z_{11} = \frac{1}{I_0^2} \int_{-l/2}^{l/2} E_z(z) I(z) dz
$$

### 互耦 (Mutual Impedance)

考虑两个相邻偶极子 $i$ 和 $j$：
$$
Z_{ij} = \frac{1}{I_i I_j} \int_{-l_j/2}^{l_j/2} E_{z,ij}(z_j) I_j(z_j) dz_j
$$

其中 $E_{z,ij}$ 是天线 $i$ 在天线 $j$ 位置处产生的电场 $z$ 分量。

**互阻抗近似公式**（两个平行半波偶极子，间距 $d$）：

$$
R_{21} = \frac{\eta}{4\pi} \left[ 2C_i(kd) - C_i(k\sqrt{d^2+l^2} + kl) - C_i(k\sqrt{d^2+l^2} - kl) \right]
$$

### 互耦影响

- 阵列中相邻单元互耦可达 $-15$ 到 $-5$ dB
- 导致单元方向图畸变、阻抗偏移
- 设计时必须考虑：通过仿真或测量校准

---


### 结构

```
     引向器3 引向器2 引向器1  驱动单元  反射器        
      ◆       ◆       ◆       ◆●     █
                             馈电点
```

### 工作原理

| 元件 | 典型长度 | 间距 | 功能 |
|:----:|:--------:|:----:|:----:|
| 反射器 (Reflector) | $0.5\lambda$ | $0.25\lambda$ | 减少后向辐射 |
| 驱动单元 (Driver) | $0.45$–$0.49\lambda$ | — | 有源馈电单元 |
| 引向器 (Directors) | $0.4$–$0.45\lambda$ | $0.3$–$0.4\lambda$ | 增强前向辐射 |

### 特性

- 方向性由单元数决定：$D \approx 10 \log_{10}(N)$ dB (经验公式)
- 3 单元：~7 dBi，5 单元：~10 dBi，10 单元：~14 dBi
- 带宽约 3–8%（频率与单元间距耦合）
- F/B (Front-to-Back) 比 > 15 dB
- 输入阻抗 ~20–30 Ω（需匹配网络）

### 设计法则

1. 反射器应比驱动单元长 5%
2. 引向器依次比驱动单元短 2–5%
3. 引向器间距 ~0.34\lambda 可最大化方向性
4. 越远引向器的长度递减、间距递增

---

## 4.9 Log-Periodic Dipole Array (LPDA)
## 对数周期偶极子阵

### 结构

一系列长度和间距按等比级数变化的偶极子：

$$
\frac{l_{n+1}}{l_n} = \frac{d_{n+1}}{d_n} = \tau < 1
$$

### 工作频率

LPDA 的频率范围由最长和最短偶极子决定：
- $f_{\min} \approx \frac{0.5c}{l_{\max}}$
- $f_{\max} \approx \frac{0.5c}{l_{\min}}$

### 关键参数

- **缩放因子 $\tau$**：通常 $0.8 \leq \tau \leq 0.95$
- **间距因子 $\sigma$**：$\sigma = d_n / (2l_n)$，通常 $0.03 \leq \sigma \leq 0.2$
- **顶角 $2\alpha$**：$\tan(\alpha/2) = (1-\tau)/(4\sigma)$

### 性能

- 带宽可达 10:1 以上
- 增益约 6–10 dBi（与 $\tau$ 和 $\sigma$ 相关）
- 输入阻抗恒定（通常 50 或 75 Ω）
- 相位中心沿阵列移动（频率变化时）

---


| 概念 | 要点 |
|:----|:------|
| 无穷小偶极子 | 理论基准，$l \ll \lambda$，$D=1.5$，$R_r \propto (l/\lambda)^2$ |
| 半波偶极子 | 工程标准，$D=1.643$，$Z_{in}\approx 73\Omega$ |
| 有限长偶极子 | 方向图随长度变化：$0.5\lambda$ 窄束 → $\lambda$ 分裂 → $>1.25\lambda$ 多瓣 |
| 感应 EMF 法 | 自/互阻抗的计算方法，积分形式 |
| 互耦 | 阵列设计必须考虑，影响阻抗和方向图 |
| 折合偶极子 | $Z_{in} \approx 300\Omega$，带宽加倍 |
| Yagi-Uda | 高方向性（~7–14 dBi），窄带（~5%） |
| LPDA | 极宽频带（~10:1），恒阻抗，相位中心移动 |

---


- C. A. Balanis, *Antenna Theory: Analysis and Design*, 4th ed., Wiley, 2016, Chapter 4.
- R. F. Harrington, *Time-Harmonic Electromagnetic Fields*, IEEE Press, 2001.
- S. Uda and Y. Mushiake, *Yagi-Uda Antenna*, Maruzen, 1954.
- D. E. Isbell, "Log Periodic Dipole Arrays," *IRE Trans. Antennas Propag.*, vol. 8, pp. 260–267, 1960.
- V. H. Rumsey, *Frequency Independent Antennas*, Academic Press, 1966.
