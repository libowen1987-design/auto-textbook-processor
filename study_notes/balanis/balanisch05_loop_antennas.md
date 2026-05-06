# Chapter 5: Loop Antennas

> Balanis, *Antenna Theory: Analysis and Design*, 4th Edition — Chapter 5

---

## 5.1 Introduction

环天线分为两类：
- **小环** ($C < \lambda/10$)：辐射电阻小，用于接收
- **大环** ($C \approx \lambda$)：可作谐振天线

环的形状可为圆形、方形、三角形等，基本电性能相似。

---

## 5.2 Small Circular Loop

周长 $C < \lambda/10$，均匀电流近似。

### 辐射场

小环相当于**磁偶极子**（对偶于电偶极子）。远场：

$$
E_\phi \approx \eta \frac{(\pi a^2) k^2 I_0 e^{-jkr}}{4\pi r} \sin\theta
$$

其中 $a$ 是环半径，$C = 2\pi a$。

### 方向图

$$
F(\theta) = \sin\theta
$$

与无穷小电偶极子完全相同——E 面为 $\sin\theta$，H 面全向。
区别在于**极化方向**：小环发出 $\hat{\phi}$ 极化（水平极化于环面内）。

### 辐射电阻

$$
R_r = 20\pi^2 \left(\frac{C}{\lambda}\right)^4 = 320\pi^4 \left(\frac{a}{\lambda}\right)^4
$$

> 注意：$R_r \propto (C/\lambda)^4$，比短偶极子 $(l/\lambda)^2$ 下降更快。

因此小环的辐射效率极低，常作为**接收天线**（磁场探头）或**测向天线**。

### 方向性

$$
D_0 = 1.5\ (1.76\ \text{dB})
$$

与短偶极子相同。

### 多匝环

N 匝小环：
- 辐射电阻增大 $N^2$ 倍：$R_r^{(N)} = N^2 R_r^{(1)}$
- 方向图不变
- 测向环常用多匝结构提高灵敏度

---

## 5.3 Circular Loop of Constant Current

假设 $I(\phi') = I_0$（均匀），适用于 $C \lesssim 0.2\lambda$。

### 一般远场积分

$$
\begin{aligned}
E_\phi &= -\frac{\eta k a I_0 e^{-jkr}}{2r} J_1(ka\sin\theta) \\
E_\theta &= 0
\end{aligned}
$$

其中 $J_1$ 是一阶第一类 Bessel 函数。

当 $ka \ll 1$ 时，$J_1(x) \approx x/2$，退化为小环结果。

---

## 5.4 Circular Loop with Circumference ~ λ

当 $C \approx \lambda$ 时，电流不再是均匀的。

### 驻波电流分布

$$
I(\phi') = I_0 \cos\phi'
$$

### 方向图

对于 $C = \lambda$ 环：
$$
E_\theta \sim J_2(ka\sin\theta)\cos 2\phi'
$$

方向图在环平面内有两个主瓣，垂直于环面方向为零。

### $C = \lambda$ 环的特点

| 参数 | 数值 |
|:----|:----:|
| 方向性 | $D_0 \approx 3.7$ (5.68 dBi) |
| 辐射电阻 | $R_r \approx 100$–$300\ \Omega$ |
| 输入阻抗 | 高阻、谐振时纯阻 |
| HPBW (E-plane) | ≈ $72^\circ$ |

---

## 5.5 Loop Antenna Applications

| 应用 | 环类型 | 理由 |
|:----|:-------|:------|
| AM 广播接收 | 铁氧体小环 | 紧凑、磁耦合好 |
| 测向 (DF) | 小环 + 垂直天线 | 8 字形方向图 + 全向 → 消除模糊 |
| EMC 探头 | 小屏蔽环 | 近场 H 场测量 |
| RFID 标签 | 多匝小环 | 紧凑、阻抗可调 |
| 卫星通信 | 大环 (C≈λ) | 环面内全向、圆极化 |
| 手机 NFC | 小环 | 13.56 MHz 近场耦合 |

---

## 重要工程要点

| 概念 | 要点 |
|:----|:------|
| 小环 vs 短偶极子 | 方向图相同 ($\sin\theta$)，极化垂直 |
| $R_r \propto (C/\lambda)^4$ | 小环辐射效率极低，不适合发射 |
| 多匝环 | $R_r \propto N^2$，灵敏度线性提高 |
| 磁偶极子 | 小环的对偶模型，便于分析 |
| 大环 | $C \approx \lambda$ 时具高 $D$ 和 $R_r$ |
| 屏蔽环 | 只响应 H 场，消除 E 场耦合 → EMC 探头 |

---

## 参考文献

- C. A. Balanis, *Antenna Theory*, 4th ed., Wiley, 2016, Ch. 5.
- R. W. P. King, *The Loop Antenna*, IEEE Press, 1982.
- G. S. Smith, "The Circular Loop Antenna," *IEEE Trans. Antennas Propag.*, vol. 19, pp. 256–262, 1971.
