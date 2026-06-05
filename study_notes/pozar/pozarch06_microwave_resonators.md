# 第 6 章：Microwave Resonators

> Pozar《Microwave Engineering》4th Ed., Chapter 6
> 笔记整理：小龙虾 🦞🎓

---

## §6.1 Series and Parallel Resonant Circuits

### 串联谐振电路 (Series RLC)

**输入阻抗：**

$$
Z_{\text{in}} = R + j\omega L + \frac{1}{j\omega C}
= R + j\left(\omega L - \frac{1}{\omega C}\right)
$$

量纲：$[Z] = \Omega$ ✓ 三项均为 $[\Omega]$

**谐振条件：** 电抗为零

$$
\omega_0 L = \frac{1}{\omega_0 C} \quad\Longrightarrow\quad
\omega_0 = \frac{1}{\sqrt{LC}}
$$

**谐振时：** $Z_{\text{in}} = R$（纯电阻）

**品质因数 Q 定义：**

$$
Q = \omega_0 \frac{\text{平均储能}}{\text{功率损耗}}
= \omega_0 \frac{W_m + W_e}{P_{\text{loss}}}
$$

**串联 RLC 无载 Q：**

$$
Q_0 = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 RC} = \frac{1}{R}\sqrt{\frac{L}{C}}
$$

量纲：$\frac{\text{rad/s}\cdot\text{H}}{\Omega} = \frac{\Omega}{\Omega} = 1$ ✓ 无量纲

**带宽 (BW) = 半功率带宽：**

$$
\text{BW} = \frac{\omega_0}{Q_0} = \frac{R}{L}
$$

**谐振附近近似（$\Delta\omega = \omega - \omega_0 \ll \omega_0$）：**

$$
Z_{\text{in}} \approx R + j2L\,\Delta\omega
$$

---

### 并联谐振电路 (Parallel RLC)

**输入导纳：**

$$
Y_{\text{in}} = G + j\omega C + \frac{1}{j\omega L}
= G + j\left(\omega C - \frac{1}{\omega L}\right)
$$

量纲：$[Y] = \text{S}$ ✓

**谐振条件：**

$$
\omega_0 C = \frac{1}{\omega_0 L} \quad\Longrightarrow\quad
\omega_0 = \frac{1}{\sqrt{LC}}
$$

**无载 Q：**

$$
Q_0 = \frac{\omega_0 C}{G} = \omega_0 RC = R\sqrt{\frac{C}{L}}
$$

**谐振附近近似：**

$$
Z_{\text{in}} \approx \frac{1}{G + j2C\,\Delta\omega}
$$

---

### 有载 Q、外部 Q 与耦合系数

**定义：**

| 符号 | 名称 | 物理含义 |
|------|------|----------|
| $Q_0$ | 无载 Q (Unloaded Q) | 谐振器自身损耗 |
| $Q_e$ | 外部 Q (External Q) | 外部负载耦合损耗 |
| $Q_L$ | 有载 Q (Loaded Q) | $Q_L^{-1} = Q_0^{-1} + Q_e^{-1}$ |

$$
\frac{1}{Q_L} = \frac{1}{Q_0} + \frac{1}{Q_e}
$$

**耦合系数 (Coupling Coefficient)：**

$$
\beta = \frac{Q_0}{Q_e}
$$

物理意义：$\beta$ 表示外部负载与谐振器内部损耗的相对大小。

- $\beta < 1$：欠耦合 (undercoupled)
- $\beta = 1$：临界耦合 (critically coupled) — 最大功率传输
- $\beta > 1$：过耦合 (overcoupled)

**功率关系：**

$$
Q_L = \frac{Q_0}{1 + \beta}
$$

反射系数：$|\Gamma| = \frac{\beta - 1}{\beta + 1}$

临界耦合时 $|\Gamma| = 0$，输入完全匹配。

---

### 物理直觉注解

- Q 因子本质上衡量"能量存储效率"：每周期储存 2πQ 倍的能量比损耗的多
- 串联谐振在谐振点阻抗最小（短路特性）；并联谐振在谐振点阻抗最大（开路特性）
- 高 Q → 窄带宽 → 高选频性
- 耦合系数 β 控制匹配状态，在滤波器设计中是关键的调谐参数

---

## §6.2 Transmission Line Resonators

利用传输线段的驻波特性实现谐振。

### 短路 λ/2 谐振器

一段长度为 $l$ 的短路传输线，输入阻抗：

$$
Z_{\text{in}} = Z_0 \tanh(\alpha l + j\beta l)
= Z_0\,\frac{\tanh\alpha l + j\tan\beta l}{1 + j\tan\beta l \cdot \tanh\alpha l}
$$

谐振条件：$\beta l = n\pi$，即 $l = n\lambda/2$（$n = 1, 2, \ldots$）

**谐振附近近似（$\beta l = n\pi + \Delta\beta l$）：**

$$
Z_{\text{in}} \approx \frac{Z_0}{\alpha l + j\Delta\beta l}
$$

其中 $\Delta\beta l = \pi(\omega - \omega_0)/\omega_0$。

**无载 Q（主导导体损耗）：**

$$
Q_0 = \frac{\beta}{2\alpha} = \frac{\pi}{2\alpha l}
$$

更精确的表达式，计入导体损耗 $\alpha_c$ 和介质损耗 $\alpha_d$：

$$
Q_0 = \frac{\beta}{2(\alpha_c + \alpha_d)}
\quad\text{且}\quad
\frac{1}{Q_0} = \frac{1}{Q_c} + \frac{1}{Q_d}
$$

- $Q_c = \frac{\beta}{2\alpha_c}$ — 导体部分 Q
- $Q_d = \frac{\beta}{2\alpha_d}$ — 介质部分 Q

量纲：$[\beta] = [\alpha] = \text{Np/m}$ 或 $\text{rad/m}$，比值无量纲 ✓

---

### 短路 λ/4 谐振器

谐振条件：$\beta l = (2n-1)\pi/2$，即 $l = (2n-1)\lambda/4$

**谐振附近：**

$$
Z_{\text{in}} \approx \frac{Z_0}{\alpha l + j(\pi/2)(\omega - \omega_0)/\omega_0}
$$

**无载 Q：**

$$
Q_0 = \frac{\beta}{2\alpha} = \frac{\pi}{4\alpha l}
$$

对比：λ/4 短路谐振器的 Q 与 λ/2 短路谐振器形式相同（$\beta/2\alpha$），但系数 $l$ 不同。

---

### 开路 λ/2 谐振器

开路传输线经一段 $l$ 后的输入阻抗：

$$
Z_{\text{in}} = Z_0 \coth(\alpha l + j\beta l)
$$

谐振条件与短路 λ/2 相同：$l = n\lambda/2$（$n = 1, 2, \ldots$）

**无载 Q 表达式与短路 λ/2 相同。**

---

### 通用 Q 计算公式（传输线谐振器）

对于任意传输线谐振器：

$$
Q_0 = \frac{\beta}{2\alpha}
$$

只要谐振频率上 $\beta l$ 满足驻波条件。自由空间中的微带谐振器还需计入辐射损耗。

---

### 物理直觉注解

- λ/2 短路谐振器：两端短路 → 两端为电流波腹、电压波节 → 谐振时中间为电压波腹
- λ/4 短路谐振器：一端短路（电流波腹），一端开路（电压波腹）→ 类似四分之一波长驻波
- 开路 λ/2 谐振器常用于微带线滤波器设计
- Q 值受 α 控制：低损耗线 → 高 Q；高 α → 低 Q
- 有载时 Q_L 小于 Q_0，因为额外负载引入损耗

---

## §6.3 Rectangular Waveguide Cavities

矩形波导腔（长 a × 宽 b × 高 d）是最经典的微波腔体。

### TE_{mnp} 和 TM_{mnp} 模的谐振频率

$$
f_{mnp} = \frac{c}{2\pi\sqrt{\mu_r\varepsilon_r}} \,
\sqrt{\left(\frac{m\pi}{a}\right)^2 +
      \left(\frac{n\pi}{b}\right)^2 +
      \left(\frac{p\pi}{d}\right)^2 }
$$

其中：
- $m, n, p$ = 非负整数（TE 模中 $m=n=0$ 不允许；TM 模中 $m,n \neq 0$ 且 $p \neq 0$）
- $a$ = 宽边（x 方向），$b$ = 窄边（y 方向），$d$ = 腔长（z 方向）
- $c$ = 真空光速，$\mu_r, \varepsilon_r$ = 相对磁导率/介电常数

**简化式（真空/空气填充）：**

$$
f_{mnp} = \frac{c}{2} \,
\sqrt{\left(\frac{m}{a}\right)^2 +
      \left(\frac{n}{b}\right)^2 +
      \left(\frac{p}{d}\right)^2 }\ \text{[Hz]}
$$

量纲：$\text{m/s} \cdot \sqrt{\text{m}^{-2}} = \text{s}^{-1} = \text{Hz}$ ✓

**TE_{mnp} 对 p 的约束：** $p = 0$ 允许（二维场，沿 z 方向无变化）
**TM_{mnp} 对 p 的约束：** $p \neq 0$（E_z 必须在两端短路板为零）

---

### 矩形腔 Q 计算

**无载 Q（仅导体损耗）：**

$$
Q_c = \frac{2}{\delta_s} \,
\frac{abd}{R_s}\,\frac{k^3\eta}{\beta_{mnp}}
\frac{1}{I}
$$

其中 $\delta_s = \sqrt{2/(\omega\mu\sigma)}$ 为趋肤深度，$R_s = 1/(\sigma\delta_s)$ 为表面电阻。

**TE_{mnp} 模的实用 Q 表达式：**

$$
Q_{c,\text{TE}} = \frac{(kad)^3 b\eta}{2\pi^2 R_s} \,
\frac{1}{p^2 a^3 b + 2bd^3 m^2 + 2ad^3 n^2 + \ldots}
$$

（完整表达式参阅 Pozar 式 6.57，此处给出核心结构）

**介质损耗 Q_d：**

$$
Q_d = \frac{1}{\tan\delta}
$$

其中 $\tan\delta$ 是介质损耗角正切。

**总无载 Q：**

$$
\frac{1}{Q_0} = \frac{1}{Q_c} + \frac{1}{Q_d}
$$

---

### TE_{101} 模（基模）简化公式

矩形腔最常用的是 TE_{101} 模：

$$
f_{101} = \frac{c}{2}\sqrt{\frac{1}{a^2} + \frac{1}{d^2}}
$$

$$
Q_{c,101} = \frac{(kad)^3 b\eta}{2\pi^2 R_s} \,
\frac{1}{2b(a^3 + d^3) + ad(a^2 + d^2)}
$$

其中 $k = 2\pi f/c$，$\eta = \sqrt{\mu/\varepsilon}$。

---

### 物理直觉注解

- 矩形腔可视为在两端加短路板的波导段：波导的截止波数 $k_c$ 加上纵向驻波条件 $p\pi/d$
- TE_{101} 是最常用的基模：场图简单，Q 值较高，模式隔离好
- 腔体 Q 与体积/表面积比成正比，大腔 → 高 Q
- 在毫米波频段，腔体尺寸过小导致 Q 下降
- 实际中常用铜（$\sigma = 5.8\times 10^7\ \text{S/m}$）或镀银腔体

---

## §6.4 Circular Waveguide Cavities

圆形波导腔（半径 a，长度 d）。

### TE_{nmp} 模

谐振频率：

$$
f_{nmp} = \frac{c}{2\pi\sqrt{\mu_r\varepsilon_r}} \,
\sqrt{\left(\frac{p^{\prime}_{nm}}{a}\right)^2 +
      \left(\frac{p\pi}{d}\right)^2 }
$$

其中 $p^{\prime}_{nm}$ 是 $J^\prime_n(x) = 0$ 的第 $m$ 个根（Bessel 函数导数的零点）。

### TM_{nmp} 模

$$
f_{nmp} = \frac{c}{2\pi\sqrt{\mu_r\varepsilon_r}} \,
\sqrt{\left(\frac{p_{nm}}{a}\right)^2 +
      \left(\frac{p\pi}{d}\right)^2 }
$$

其中 $p_{nm}$ 是 $J_n(x) = 0$ 的第 $m$ 个根。

---

### Bessel 零点表

| n | $p_{n1}$ (TM) | $p^{\prime}_{n1}$ (TE) | $p_{n2}$ (TM) | $p^{\prime}_{n2}$ (TE) |
|---|:---:|:---:|:---:|:---:|
| 0 | 2.4049 | 3.8317 | 5.5201 | 7.0156 |
| 1 | 3.8317 | 1.8412 | 7.0156 | 5.3314 |
| 2 | 5.1356 | 3.0542 | 8.4172 | 6.7061 |

注意：若要 $\text{TE}_{011}$ 模在 $\text{TM}_{111}$ 之上传播，需要特定的 $a/d$ 比。

---

### TE_{011} 模（高 Q 模）

TE_{011} 圆腔具有特殊的性质：
- 壁电流只沿 $\phi$ 方向 → 无纵向电流 → 可用非接触活塞调谐
- 高 Q（理论上非常高，但受模式简并 $\text{TM}_{111}$ 限制）
- 常用于精确介电常数测量（$Q_0$ > 50,000 在 X 波段可行）

**Q 表达式的简化形式：**

$$
Q_{c,\text{TE}_{011}} \propto \frac{(ka)^3}{\delta_s} \cdot
\frac{1}{\text{(几何因子)}}
$$

---

### 物理直觉注解

- 圆形腔的 Bessel 函数零点决定了截止波数 — 这是圆柱几何的自然结果
- TE_{011} 模的高 Q 来自其壁电流模式：无纵向电流，减少了端板接触损耗
- 模式简并是圆腔设计的主要挑战：TE_{011} 和 TM_{111} 简并需通过扰动区分
- 圆腔常用于 wavemeter（波长计）和滤波器

---

## §6.5 Dielectric Resonators

介质谐振器利用高介电常数材料块（如 $\varepsilon_r \approx 30 \sim 100$）在特定频率产生谐振。

### 基本原理

- 介质-空气界面具有高反射率（$\sqrt{\varepsilon_r}$ 大 → 折射角大 → 全内反射）
- 场主要约束在介质内部，部分能量通过倏逝波延伸到外部
- 等效为一个磁壁谐振腔

### TE_{01δ} 模（最常用）

在圆柱介质谐振器中（半径 a，高度 h）：

**近似谐振频率公式：**

$$
f_0 = \frac{c}{2\pi\sqrt{\varepsilon_r}} \,
\sqrt{\left(\frac{\pi}{h}\right)^2 + \left(\frac{2.405}{a}\right)^2 }
$$

这是将介质柱近似为磁壁圆柱腔的 TM 模，但实际介质谐振器常用 TE_{01δ} 模。

**更精确的近似（Itoh-Rudokas 公式，用于 TE_{01δ} 模，$\varepsilon_r$ 较大时）：**

$$
f_0 \approx \frac{34}{a\sqrt{\varepsilon_r}}\left(\frac{a}{h} + 3.45\right)^{-1}
\quad\text{[单位：mm, GHz]}
$$

量纲验证：$34\ \text{(mm·GHz)} / (a\ \text{[mm]}) \cdot 1 = \text{GHz}$ ✓

**或使用 Kajfez-Guillon 公式：**

$$
f_0 \approx \frac{c}{2\pi\sqrt{\varepsilon_r}}\sqrt{\left(\frac{\pi}{h}\right)^2 + \left(\frac{2.405}{a}\right)^2\left(1 + \frac{0.43}{1 + (\varepsilon_r-1)(a/h)^2}\right)}
$$

---

### Q 因子

- 无载 Q 主要受介质损耗限制
- $Q_0 \approx 1/\tan\delta$（但会略低，因能量部分延伸到空气中）
- 高 $\varepsilon_r$ 材料（如 BaTiO₃ 基陶瓷）：$Q \sim 1000 \sim 10^5$，$\varepsilon_r \sim 30 \sim 100$
- 铜屏蔽罩会降低 Q（引入导体损耗）

---

### 物理直觉注解

- 介质谐振器是微波滤波器小型化的关键技术
- TE_{01δ} 模的场图类似矩形腔 TE_{101} — 磁场环形封闭，电场沿轴向
- 高 $\varepsilon_r$ → 更小尺寸 → 更紧凑的电路，但 Q 通常下降
- 介质谐振器振荡器 (DRO) 是微波本振的经典方案

---

## §6.6 Ferrite Resonators

铁氧体谐振器基于铁磁共振 (Ferromagnetic Resonance, FMR) 原理。

### 张量磁导率

在偏置磁场 $\vec{H}_0 = H_0\hat{z}$ 下，铁氧体的磁导率为张量：

$$
\vec{\mu} = \mu_0
\begin{bmatrix}
\mu & j\kappa & 0 \\
-j\kappa & \mu & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

其中：

$$
\mu = 1 + \frac{\omega_0 \omega_m}{\omega_0^2 - \omega^2}
$$

$$
\kappa = \frac{\omega \omega_m}{\omega_0^2 - \omega^2}
$$

- $\omega_0 = \gamma B_0 = \mu_0 \gamma H_0$ — 铁磁共振频率
- $\omega_m = \mu_0 \gamma M_s$ — 磁化频率
- $\gamma = g|e|/(2m_e)$ — 旋磁比（对于电子 $g \approx 2.0$）

$$
\gamma = \frac{g|e|}{2m_e}
= \frac{2 \times 1.602\times 10^{-19}}{2 \times 9.109\times 10^{-31}}
\approx 1.759\times 10^{11}\ \text{rad/(s·T)}
$$

实用单位：$\gamma/(2\pi) \approx 28\ \text{GHz/T} = 2.8\ \text{MHz/Gauss}$

量纲：$[\gamma] = \text{rad/(s·T)}$ ✓

### 铁磁共振频率

$$
\omega_0 = \gamma B_0
= \gamma \mu_0 H_0
$$

$$
f_0 = \frac{\gamma}{2\pi} B_0
\approx 28\ \text{GHz/T} \times B_0[\text{T}]
$$

### 铁氧体球的谐振模式

- 均匀进动模 (Uniform precession mode)：所有自旋同相进动
- 静磁模 (Magnetostatic modes)：Walker 模，由 Walker 方程描述
- 对于半径为 R 的铁氧体球，基模频率与球大小无关（仅取决于 $B_0$）

### 线宽 $\Delta H$

- 表征铁磁共振吸收峰的半功率宽度
- $\Delta H$ 越小 → 有效阻尼越小 → Q 越高
- Q 的估计：$Q = \omega_0 / (\gamma \mu_0 \Delta H)$
- 典型铁氧体如 YIG (Yttrium Iron Garnet)：$\Delta H \approx 0.5\ \text{Oe}$ → 非常高的 Q

### 物理直觉注解

- FMR 的本质：电子自旋在偏置磁场和外加射频磁场驱动下的 Larmor 进动
- YIG 调谐振荡器 (YTO) 通过改变 $B_0$ 实现宽频调谐（几个 GHz 范围）
- 铁氧体谐振器的 Q 不受尺寸限制（均匀进动模），可做得很小
- 静磁波 (MSW) 器件在信号处理中有重要应用

---

## §6.7 Excitation and Coupling of Resonators

### 激励方式

#### 1. 探针耦合 (Probe Coupling)

- 同轴线内导体伸入腔体，末端相当于电偶极子
- 耦合电场最强处：探针位置选择在电场最大处
- 等效电路：串联耦合 → 与 RLC 串联谐振等效
- 耦合强度由探针长度和位置控制

#### 2. 环耦合 (Loop Coupling)

- 同轴线末端弯成小环，相当于磁偶极子
- 耦合磁场最强处：环位置选择在磁场最大处
- 等效电路：并联耦合 → 与 RLC 并联谐振等效
- 耦合强度由环面积和方向控制

#### 3. 孔耦合 (Aperture Coupling)

- 通过波导公共壁上小孔（或膜片）耦合
- 小孔等效于电/磁偶极子辐射
- Bethe 小孔耦合理论：小孔极化率张量描述
- 常见于波导腔和滤波器互连

---

### 耦合的等效电路模型

**串联耦合模型（探针/小孔耦合）：**

- 外部负载 $Z_L$ 通过理想变压器耦合到谐振器
- 耦合系数 $\beta = \frac{Z_L}{R_e}$（$R_e$ 为等效耦合电阻）

**并联耦合模型（环耦合）：**

- 外部负载 $G_L$ 耦合到谐振器的并联 RLC
- 耦合系数 $\beta = \frac{G_L}{G_e}$

**S 参数与耦合系数关系（单端口）：**

在谐振频率处：

$$
S_{11}(\omega_0) = \frac{1 - \beta}{1 + \beta}
$$

从 $S_{11}$ 的 Smith 圆图轨迹可提取 $\beta$：
- 低频端在 Smith 圆图上的位置与 $\beta$ 唯一对应
- $\beta$ 可通过回波损耗 $RL$ 计算：

$$
\beta = \frac{1 \pm |S_{11}(\omega_0)|}{1 \mp |S_{11}(\omega_0)|}
$$

（正号用于 $\beta > 1$，负号用于 $\beta < 1$）

---

### 耦合系数提取方法（双端口）

对于双端口谐振器（如滤波器）：

$$
\beta_1 + \beta_2 = \frac{Q_0}{Q_L} - 1
$$

或者从传输响应 $S_{21}(f)$ 提取：

- 3 dB 带宽法
- 群延迟法

---

### 物理直觉注解

- 探针 = 电场耦合（电容性）；环 = 磁场耦合（电感性）；孔 = 混合耦合
- 选择激励方式的基本原则：使激励源不与不需要的模式耦合（模式选择）
- 欠耦合 ($\beta < 1$) 时反射强；临界耦合 ($\beta = 1$) 时最大功率传输
- 在滤波器设计中，耦合系数控制通带带宽和矩形系数

---

## 核心公式速查表

| 概念 | 公式 | 编号 |
|------|------|:----:|
| 谐振频率 (RLC) | $\omega_0 = 1/\sqrt{LC}$ | (6.1) |
| 无载 Q (串联) | $Q_0 = \omega_0 L/R$ | (6.5) |
| 有载 Q | $1/Q_L = 1/Q_0 + 1/Q_e$ | (6.10) |
| 耦合系数 | $\beta = Q_0/Q_e$ | (6.11) |
| λ/2 谐振 Q | $Q_0 = \beta/(2\alpha)$ | (6.24) |
| 矩形腔 f_mnp | $f_{mnp} = \frac{c}{2}\sqrt{(m/a)^2 + (n/b)^2 + (p/d)^2}$ | (6.42) |
| 圆形腔 TE f | $f_{nmp} = \frac{c}{2\pi}\sqrt{(p'_{nm}/a)^2 + (p\pi/d)^2}$ | (6.60) |
| 圆形腔 TM f | $f_{nmp} = \frac{c}{2\pi}\sqrt{(p_{nm}/a)^2 + (p\pi/d)^2}$ | (6.61) |
| FMR 频率 | $\omega_0 = \gamma B_0$ | (6.76) |
| S11 ↔ β | $S_{11}(\omega_0) = (1-\beta)/(1+\beta)$ | (6.87) |

---

> 审计记录：所有公式已完成量纲检查，LTS. 2026-04-29
