# Collins Ch7 — Periodic Structures and Microwave Filters

> **来源**: R. E. Collin, *Foundations for Microwave Engineering*, 2nd ed., IEEE Press, 2001.
> **注意**: 本章在第二版中为 Ch8 (Periodic Structures and Filters, pp. 550–647). 此处按第一版编号(Ch7)组织。内容覆盖 §7.1–§7.6 (第二版 §8.1–§8.23).

---

## §7.1 Periodic Structures (Ch8, §8.1–§8.8, pp. 551–577)

### 7.1.1 电容加载传输线 (Capacitively Loaded Line, p. 551)

周期性结构由**单位单元 (unit cell)** 重复级联构成。最基本的例子是传输线上每隔距离 $d$ 并联一个 shunt 电容 $C_s$。

**ABCD 矩阵** 描述一个单位单元 (Eq. 8.1):

$$
\begin{bmatrix}
V_1 \\ I_1
\end{bmatrix}
=
\begin{bmatrix}
A & B \\
C & D
\end{bmatrix}
\begin{bmatrix}
V_2 \\ I_2
\end{bmatrix}
$$

对于 shunt 电容加载线，单位单元分为三段：传输线段长度 $d/2$ → shunt $C_s$ → 传输线段长度 $d/2$。

传输线段 (长度 $l$, 特征阻抗 $Z_0$, 传播常数 $\beta$) 的 ABCD 矩阵:

$$
T_{TL} = \begin{bmatrix}
\cos \beta l & j Z_0 \sin \beta l \\
j Y_0 \sin \beta l & \cos \beta l
\end{bmatrix}
$$

Shunt 导纳 $Y_s = j \omega C_s$ 的 ABCD 矩阵:

$$
T_Y = \begin{bmatrix}
1 & 0 \\
Y_s & 1
\end{bmatrix}
$$

级联得到单位单元传输矩阵 (Eq. 8.2):

$$
T = T_{TL}^{d/2} \cdot T_Y \cdot T_{TL}^{d/2}
$$

### 7.1.2 周期结构的波动分析 (Wave Analysis, p. 557)

对无限周期结构应用 **Floquet 定理 (Floquet's Theorem, §8.8, p. 569)**：沿周期结构传播的波满足

$$
V(z + d) = e^{-\gamma d} V(z)
$$

其中 $\gamma = \alpha + j\beta$ 是传播常数。$e^{-\gamma d}$ 是单位单元的传输因子。

由 ABCD 矩阵和 Floquet 条件:

$$
\begin{bmatrix}
V_1 \\ I_1
\end{bmatrix}
=
\begin{bmatrix}
A & B \\
C & D
\end{bmatrix}
\begin{bmatrix}
V_2 \\ I_2
\end{bmatrix}
= e^{\gamma d}
\begin{bmatrix}
V_2 \\ I_2
\end{bmatrix}
$$

**色散关系 (Dispersion Relation, Eq. 8.8, p. 557):**

$$
\cosh \gamma d = \frac{A + D}{2}
$$

对于无耗对称结构，$A = D$ 为实数，$AD - BC = 1$。

当 $\gamma = j\beta$ (无耗传输) 时:

$$
\cos \beta d = A
$$

- **通带 (Passband)**: $|A| \le 1$，$\beta d$ 为实数，波无衰减传播
- **阻带 (Stopband)**: $|A| > 1$，$\beta d = m\pi + j\alpha d$，波衰减

### 7.1.3 k-β 图 (k-β Diagram, p. 564)

k-β 图 (或 Brillouin 图) 显示频率与相位常数之间的关系。对于电容加载传输线:

$$
\cos \beta d = \cos k_0 d - \frac{\omega C_s Z_0}{2} \sin k_0 d
$$

其中 $k_0 = \omega / v_p$ 是未加载线的波数。

**特征**:
- 当 $\omega \to 0$: $\beta d \to k_0 d$，接近未加载线
- 在 $k_0 d = \pi$ 附近出现第一个阻带
- 群速度 $v_g = d\omega/d\beta$ 在通带边界趋于零

### 7.1.4 群速度和能量流 (§8.7, p. 566)

群速度决定了信号能量传播速度:

$$
v_g = \frac{d\omega}{d\beta} = \frac{P_{av}}{W_d}
$$

其中 $P_{av}$ 为平均功率流，$W_d$ 为单位单元存储能量密度。

在通带边界 $v_g = 0$，意味着能量在周期性结构中驻定。

### 7.1.5 Floquet 定理与空间谐波 (§8.8, p. 569)

Floquet 定理指出，周期结构中的场可表示为:

$$
E(z) = e^{-\gamma z} \sum_{n=-\infty}^{\infty} a_n e^{-j2\pi n z/d}
$$

这是**空间谐波 (spatial harmonics)** 展开。第 $n$ 次谐波的传播常数为:

$$
\beta_n = \beta_0 + \frac{2\pi n}{d}
$$

其中 $\beta_0$ 是基波 (fundamental) 相位常数。

空间谐波满足同步条件时，可用于行波管 (TWT) 中的电子注-波互作用。

---

## §7.2 Insertion Loss Method (Ch8, §8.14–§8.18, pp. 591–597)

### 7.2.1 功率损耗比 (§8.14, p. 591)

滤波器设计的插入损耗法从**功率损耗比 (Power Loss Ratio)** 出发:

$$
P_{LR} = \frac{P_{inc}}{P_{load}} = \frac{1}{1 - |\Gamma(\omega)|^2}
$$

其中 $P_{inc}$ 为入射功率，$P_{load}$ 为负载吸收功率，$\Gamma(\omega)$ 为输入反射系数。

对于一个两端接 $R_L = R_S = 1$ 的无耗二端口网络:

$$
P_{LR} = 1 + |\Gamma(\omega)|^2
$$

插入损耗 (dB):

$$
IL = 10 \log_{10} P_{LR}
$$

### 7.2.2 最大平坦 (Butterworth) 响应 (§8.15, p. 593)

Butterworth 响应的功率损耗比:

$$
P_{LR} = 1 + k^2 \left(\frac{\omega}{\omega_c}\right)^{2N}
$$

其中 $N$ 为滤波器阶数，$\omega_c$ 为截止频率。在 $\omega = \omega_c$ 处：

$$
P_{LR}(\omega_c) = 1 + k^2
$$

通常取 $k = 1$，则 $P_{LR}(\omega_c) = 2$，对应 3 dB 截止。

### 7.2.3 Butterworth 原型 g 值 (§8.16, p. 595)

低通滤波器原型 g 值满足:

$$
g_0 = 1
$$
$$
g_k = 2 \sin\left[\frac{(2k-1)\pi}{2N}\right], \quad k = 1, 2, \dots, N
$$
$$
g_{N+1} = 1
$$

**验证值** ($N=5$):
- $g_0 = 1$, $g_1 = 0.618$, $g_2 = 1.618$, $g_3 = 2.0$, $g_4 = 1.618$, $g_5 = 0.618$, $g_6 = 1.0$

对于三端口 (source/load 均为 $1\ \Omega$), $g_{N+1} = g_0 = 1$.

### 7.2.4 Chebyshev 响应 (§8.17, p. 593)

Chebyshev 响应的功率损耗比:

$$
P_{LR} = 1 + k^2 T_N^2\left(\frac{\omega}{\omega_c}\right)
$$

其中 $T_N(x)$ 是第一类 Chebyshev 多项式:

$$
T_N(x) = \begin{cases}
\cos(N \cos^{-1} x), & |x| \le 1 \\
\cosh(N \cosh^{-1} x), & |x| > 1
\end{cases}
$$

波纹 (ripple) 幅度为 $L_{Ar} = 10 \log_{10}(1+k^2)$ dB.

### 7.2.5 Chebyshev 原型 g 值 (§8.18, p. 595)

$$
g_0 = 1
$$
$$
g_1 = \frac{2}{\gamma} \sin\left(\frac{\pi}{2N}\right)
$$
$$
g_k = \frac{4 \sin\left[\frac{(2k-1)\pi}{2N}\right] \sin\left[\frac{(2k-3)\pi}{2N}\right]}{g_{k-1} (\gamma^2 + \sin^2\left[\frac{(k-1)\pi}{N}\right])}, \quad k = 2, 3, \dots, N
$$
$$
g_{N+1} = \begin{cases}
1 & \text{N 为奇数} \\
\coth^2(\beta/4) & \text{N 为偶数}
\end{cases}
$$

其中:
$$
\beta = \ln\left(\coth\frac{L_{Ar}}{17.37}\right)
$$
$$
\gamma = \sinh\left(\frac{\beta}{2N}\right)
$$

**验证值** (0.5 dB 波纹, $N=3$):
- $g_1 = 1.5963$, $g_2 = 1.0967$, $g_3 = 1.5963$, $g_4 = 1.0$

---

## §7.3 Filter Transformations (Ch8, §8.17, pp. 598–603)

### 7.3.1 频率变换 (§8.17, p. 598)

低通原型经过频率变换得到高通、带通、带阻滤波器。

**低通→高通 (LP→HP, p. 599):**

频率变量映射:

$$
\omega \to -\frac{\omega_c \omega_0}{\omega}
$$

元件变换:
- 电感 $L_k \to$ 电容 $C'_k = 1/(\omega_c \omega_0 L_k)$
- 电容 $C_k \to$ 电感 $L'_k = 1/(\omega_c \omega_0 C_k)$

其中 $\omega_0$ 是高通滤波器的截止频率。

**低通→带通 (LP→BP, p. 600):**

$$
\omega \to \frac{\omega_0}{\Delta}\left(\frac{\omega}{\omega_0} - \frac{\omega_0}{\omega}\right)
$$

其中 $\omega_0 = \sqrt{\omega_1\omega_2}$ 为中心频率，$\Delta = (\omega_2 - \omega_1)/\omega_0$ 为相对带宽。

元件变换:
- 电感 $L_k \to$ 串联 LC: $L_{sk} = L_k / (\Delta \omega_0)$, $C_{sk} = \Delta / (\omega_0 L_k)$
- 电容 $C_k \to$ 并联 LC: $C_{pk} = C_k / (\Delta \omega_0)$, $L_{pk} = \Delta / (\omega_0 C_k)$

**低通→带阻 (LP→BS):**

频率变换:

$$
\omega \to -\frac{\Delta \omega_0}{\omega/\omega_0 - \omega_0/\omega}
$$

### 7.3.2 阻抗和导纳变换器 (§8.18, p. 603)

**阻抗变换器 (Impedance Inverter, K-inverter):**
$$
\begin{bmatrix}
0 & \pm jK \\
\pm j/K & 0
\end{bmatrix}
$$

**导纳变换器 (Admittance Inverter, J-inverter):**
$$
\begin{bmatrix}
0 & \pm j/J \\
\pm jJ & 0
\end{bmatrix}
$$

变换器可使串联元件变换为并联元件，反之亦然，从而简化滤波器实现。

常见的 J-inverter 实现包括:
- 四分之一波长传输线: $J = Y_0$
- 并联电容耦合: $J = \omega C_c$

---

## §7.4 Richards' Transformation and Kuroda Identities

### 7.4.1 Richards 变换

Richards 变换将频率变量 $\omega$ 映射到 $\Omega = \tan(\beta l)$:

$$
\Omega = \tan\left(\frac{\pi \omega}{2 \omega_0}\right)
$$

其中 $l = \lambda_0/4$，$\omega_0$ 对应的传输线长度为 $\lambda_0/4$.

**关键性质**:
- 开路短截线 $\to$ 归一化阻抗 $Z_{oc} = -j Z_0 \cot(\beta l) \to$ 在 $\Omega$ 域为 $\frac{Z_0}{j\Omega}$
- 短路短截线 $\to$ 归一化阻抗 $Z_{sc} = j Z_0 \tan(\beta l) \to$ 在 $\Omega$ 域为 $jZ_0\Omega$

这使集中元件 (lumped L, C) 可映射到分布元件 (传输线短截线):

$$
L \to Z_0 = L \quad (\text{短路短截线})
$$
$$
C \to Z_0 = 1/C \quad (\text{开路短截线})
$$

### 7.4.2 Kuroda 恒等式

Kuroda 恒等式使用单位元件 (UE, 长度为 $\lambda_0/8$ 或 $\lambda_0/4$ 的传输线段) 将串联短截线等效变换为并联短截线，使物理实现更容易。

**第一 Kuroda 恒等式** ($\lambda/4$ 传输线 + 串联短截线 $\to$ 并联短截线 + $\lambda/4$ 传输线):

对于归一化阻抗 $Z$ 的串联短截线 $= 1/Z$ (并联短截线)，以及 $Z' = 1/(Z+1)$ 的单位元件:

$$
\begin{aligned}
Z_{\text{series}} &= Z \\
Z_{UE} &= 1 \\
&\Downarrow \\
Z_{shunt} &= \frac{1}{Z+1} \\
Z'_{UE} &= \frac{Z}{Z+1}
\end{aligned}
$$

---

## §7.5 Stepped-Impedance Low-Pass Filters (Ch8, §8.16, pp. 595–597)

阶梯阻抗低通滤波器使用高/低特性阻抗的传输线段近似集总元件:
- **高阻抗线** ($Z_{high} = Z_h$) 近似串联电感
- **低阻抗线** ($Z_{low} = Z_l$) 近似并联电容

### 设计步骤

已知低通原型 $g_k$ 和截止频率 $f_c$:

**串联电感:** $L_k = \frac{g_k Z_{high}}{2\pi f_c}$

高阻抗线段长度:
$$
l_k = \frac{L_k v_p}{Z_h} = \frac{g_k Z_h}{Z_h} \cdot \frac{v_p}{2\pi f_c} = \frac{g_k v_p}{2\pi f_c}
$$

更精确的表达式:
$$
\beta l_k = \frac{L_k Z_h}{Z_h} \cdot \frac{\omega_c}{v_p} = \frac{g_k Z_h \omega_c}{Z_h 2\pi f_c v_p}
$$

实际上使用:
$$
l_k = \frac{L_k c}{\sqrt{\epsilon_r} Z_h} \quad (\text{微带})
$$

**并联电容:** $C_k = \frac{g_k}{Z_{low} \cdot 2\pi f_c}$

低阻抗线段长度:
$$
l_k = \frac{C_k Z_l v_p}{g_k} = \frac{Z_l v_p}{Z_l \cdot 2\pi f_c} = \frac{v_p}{2\pi f_c}
$$

更精确:
$$
l_k = C_k Z_l v_p
$$

### 设计准则
- $Z_h/Z_l \ge 10$ 以获得良好的近似
- $Z_h$ 尽量高 (如 $100-150\ \Omega$), $Z_l$ 尽量低 (如 $10-20\ \Omega$)
- 断长应远小于 $\lambda/4$ 以保证集总近似有效
- 需进行全波仿真验证优化

---

## §7.6 Coupled-Line Bandpass Filters (Ch8, §8.20, pp. 626–635)

### 7.6.1 平行耦合线 §8.20 (p. 626)

平行耦合线带通滤波器由多个 $\lambda_0/4$ 耦合线段级联而成。每个耦合段作为一个谐振器。

**奇偶模分析:**
耦合线的奇模特性阻抗 $Z_{0o}$ 和偶模特性阻抗 $Z_{0e}$ 决定了耦合强度。

耦合系数:
$$
C = \frac{Z_{0e} - Z_{0o}}{Z_{0e} + Z_{0o}}
$$

单个 $\lambda/4$ 耦合段可视为 J-inverter，其导纳变换参数为:

$$
J_{i,i+1} = \frac{\pi \Delta}{2\sqrt{g_i g_{i+1}}}
$$

其中 $\Delta$ 为相对带宽，$g_i$ 为原型 g 值。

### 7.6.2 设计公式

**第一个/最后一个耦合段的偶/奇模阻抗:**

$$
(Z_{0e})_{01} = Z_0 \left[1 + \frac{J_{01}}{Y_0} + \left(\frac{J_{01}}{Y_0}\right)^2\right]
$$
$$
(Z_{0o})_{01} = Z_0 \left[1 - \frac{J_{01}}{Y_0} + \left(\frac{J_{01}}{Y_0}\right)^2\right]
$$

其中 $Z_0 = 1/Y_0$ 是端口参考阻抗 (通常 50 $\Omega$)。

**内部耦合段:**

$$
J_{i,i+1} = \frac{\pi \Delta}{2} \frac{1}{\sqrt{g_i g_{i+1}}}
$$
$$
(Z_{0e})_{i,i+1} = Z_0 \left[1 + \frac{J_{i,i+1}}{Y_0} + \left(\frac{J_{i,i+1}}{Y_0}\right)^2\right]
$$
$$
(Z_{0o})_{i,i+1} = Z_0 \left[1 - \frac{J_{i,i+1}}{Y_0} + \left(\frac{J_{i,i+1}}{Y_0}\right)^2\right]
$$

**端口加载:**

$$
J_{01} = \sqrt{\frac{\pi \Delta}{2 g_1}}
$$
$$
J_{N,N+1} = \sqrt{\frac{\pi \Delta}{2 g_N g_{N+1}}}
$$

### 7.6.3 物理实现

获得 $Z_{0e}$ 和 $Z_{0o}$ 后，根据传输线类型 (微带、带状线) 确定耦合段物理尺寸 (线宽 $W$ 和间距 $S$)。

对于微带线，$Z_{0e}$ 和 $Z_{0o}$ 反演出 $W/h$ 和 $S/h$ (使用数值方法或经验公式)。

---

## 总结

| 章节 | 主题 | 关键公式/概念 |
|------|------|--------------|
| §7.1 | 周期结构 | Floquet 定理, $\cosh \gamma d = (A+D)/2$, k-β 图, 通带/阻带 |
| §7.2 | 插入损耗法 | Butterworth ($P_{LR}=1+(\omega/\omega_c)^{2N}$), Chebyshev ($P_{LR}=1+k^2T_N^2$) |
| §7.3 | 频率变换 | LP→HP/BP/BS, 频率映射公式 |
| §7.4 | Richards/Kuroda | $\Omega = \tan(\beta l)$, 短截线变换, Kuroda 恒等式 |
| §7.5 | 阶梯阻抗 LPF | 高/低阻抗近似, $l_k$ 设计公式 |
| §7.6 | 耦合线 BPF | $\lambda/4$ 谐振器, J-inverter, 奇偶模阻抗 |
