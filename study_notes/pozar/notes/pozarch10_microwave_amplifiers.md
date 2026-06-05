# Chapter 10: Microwave Amplifier Design
> **中英双语版**

> Pozar, *Microwave Engineering*, 4th Edition — Chapter 10

---

## 10.1 Introduction

微波放大器是将二端口有源器件（晶体管/FET）与输入/输出匹配网络结合的结构。核心目标是：

- **稳定**：不振荡
- **增益**：达到指定 transducer gain $G_T$
- **带宽/噪声/功率**：视应用而定

```
               +--------+         +-----------+
   Γ_S ←———    | 输入匹配 | ←———   | 晶体管    | ———→ 输出匹配
  Z_S   ———→   |  网络 M1 | ———→   | (S参数)   | ———→  Γ_L → Z_L
               +--------+         +-----------+
```

### 核心 S 参数定义

\[
\begin{aligned}
b_1 &= S_{11} a_1 + S_{12} a_2 \\
b_2 &= S_{21} a_1 + S_{22} a_2
\end{aligned}
\]

输入/输出反射系数（受负载影响）：

\[
\Gamma_{\text{in}} = S_{11} + \frac{S_{12}S_{21}\Gamma_L}{1 - S_{22}\Gamma_L}
\quad\quad
\Gamma_{\text{out}} = S_{22} + \frac{S_{12}S_{21}\Gamma_S}{1 - S_{11}\Gamma_S}
\]

---

## 10.2 稳定性分析 (Stability Considerations)

### 振荡条件

当 $|\Gamma_S \Gamma_{\text{in}}| > 1$ 或 $|\Gamma_L \Gamma_{\text{out}}| > 1$ 时发生振荡。
无源负载：$|\Gamma_S| \le 1,\ |\Gamma_L| \le 1$。

### 无条件稳定 (Unconditionally Stable)

对所有 $|\Gamma_S| \le 1, |\Gamma_L| \le 1$ 满足：

\[
|\Gamma_{\text{in}}| < 1,\quad |\Gamma_{\text{out}}| < 1
\]

### Rollett K-\Delta 判据

\[
\boxed{K = \frac{1 - |S_{11}|^2 - |S_{22}|^2 + |$\Delta$|^2}{2|S_{12}S_{21}|}}
\]

\[
\boxed{\Delta = S_{11}S_{22} - S_{12}S_{21}}
\]

**无条件稳定** $\iff K > 1$ **且** $|$\Delta$| < 1$。

**量纲检查**：$K$ 无量纲，$S_{ij}$ 无量纲 → OK。

### 稳定性圆 (Stability Circles)

在 $\Gamma_L$ 平面上，$|\Gamma_{\text{in}}| = 1$ 的边界是圆。

**输出侧稳定圆**（$\Gamma_L$ 平面）：

\[
C_L = \frac{(S_{22} - \Delta S_{11}^*)^*}{|S_{22}|^2 - |$\Delta$|^2}
\quad
r_L = \left|\frac{S_{12}S_{21}}{|S_{22}|^2 - |$\Delta$|^2}\right|
\]

**输入侧稳定圆**（$\Gamma_S$ 平面）：

\[
C_S = \frac{(S_{11} - \Delta S_{22}^*)^*}{|S_{11}|^2 - |$\Delta$|^2}
\quad
r_S = \left|\frac{S_{12}S_{21}}{|S_{11}|^2 - |$\Delta$|^2}\right|
\]

#### 判断稳定区域

- 若 $|S_{11}| < 1$：Smith 图中心 ($\Gamma = 0$) 属于稳定区
- 若 $|S_{11}| > 1$：Smith 图中心属于不稳定区
- 稳定区在圆外（当圆包含中心）或圆内

### \mu 因子 (Edwards-Sinsky)

\[
\boxed{\mu_1 = \frac{1 - |S_{11}|^2}{|S_{22} - \Delta S_{11}^*| + |S_{12}S_{21}|}}
\]

\[
\boxed{\mu_2 = \frac{1 - |S_{22}|^2}{|S_{11} - \Delta S_{22}^*| + |S_{12}S_{21}|}}
\]

$\mu_1 > 1$ 且 $\mu_2 > 1$ 等价于无条件稳定。优点：单一条件，无需判断 $|$\Delta$|$。

### 有条件稳定/潜在不稳定

当 $K < 1$ 时，需要谨慎选择 $\Gamma_S$ 和 $\Gamma_L$ 使器件工作于稳定区域。

**工程建议**：
- 通过反馈（串联/并联电阻）提高 $K$ 到 $> 1$
- 或使用阻性负载失配来稳定（牺牲增益/噪声）

---

## 10.3 功率增益定义

### 三种主要增益

| 增益 | 定义 | 物理含义 |
|------|------|----------|
| **Transducer Gain** $G_T$ | $\displaystyle \frac{P_L}{P_{\text{avs}}}$ | 传输到负载的功率 / 源可用功率 |
| **Operating Gain** $G_P$ | $\displaystyle \frac{P_L}{P_{\text{in}}}$ | 传输到负载的功率 / 实际输入晶体管功率 |
| **Available Gain** $G_A$ | $\displaystyle \frac{P_{\text{avn}}}{P_{\text{avs}}}$ | 放大器可用输出功率 / 源可用功率 |

### S 参数表达

#### Transducer Gain $G_T$

\[
\boxed{G_T = \frac{1 - |\Gamma_S|^2}{|1 - \Gamma_{\text{in}}\Gamma_S|^2}\; |S_{21}|^2\; \frac{1 - |\Gamma_L|^2}{|1 - S_{22}\Gamma_L|^2}}
\]

**量纲检查**：分子分母均为无量纲 → 无量纲，正确。

或等价形式：

\[
G_T = \frac{(1 - |\Gamma_S|^2)|S_{21}|^2(1 - |\Gamma_L|^2)}{|(1 - S_{11}\Gamma_S)(1 - S_{22}\Gamma_L) - S_{12}S_{21}\Gamma_S\Gamma_L|^2}
\]

#### Operating Power Gain $G_P$

\[
\boxed{G_P = \frac{1}{1 - |\Gamma_{\text{in}}|^2}\; |S_{21}|^2\; \frac{1 - |\Gamma_L|^2}{|1 - S_{22}\Gamma_L|^2}}
\]

$G_P$ 与 $\Gamma_S$ 无关（仅依赖 $\Gamma_L$），适合设计输出匹配。

#### Available Power Gain $G_A$

\[
\boxed{G_A = \frac{1 - |\Gamma_S|^2}{|1 - S_{11}\Gamma_S|^2}\; |S_{21}|^2\; \frac{1}{1 - |\Gamma_{\text{out}}|^2}}
\]

$G_A$ 与 $\Gamma_L$ 无关（仅依赖 $\Gamma_S$），适合设计输入匹配。

#### 三个增益在匹配时的关系

当 $\Gamma_S = \Gamma_{\text{in}}^*$ 且 $\Gamma_L = \Gamma_{\text{out}}^*$（共轭匹配）时：

\[
G_T = G_P = G_A = G_{\text{max}}
\]

### 单向化增益 $G_{TU}$

当忽略 $S_{12} \approx 0$（或 $|S_{12}| \ll |S_{21}|$）：

\[
\boxed{G_{TU} = G_S \cdot G_0 \cdot G_L}
\]

其中：
\[
G_S = \frac{1 - |\Gamma_S|^2}{|1 - S_{11}\Gamma_S|^2}
\quad
G_0 = |S_{21}|^2
\quad
G_L = \frac{1 - |\Gamma_L|^2}{|1 - S_{22}\Gamma_L|^2}
\]

单向化最大增益（$\Gamma_S = S_{11}^*,\ \Gamma_L = S_{22}^*$）：

\[
G_{TU,\max} = \frac{1}{1 - |S_{11}|^2}\; |S_{21}|^2\; \frac{1}{1 - |S_{22}|^2}
\]

### 单向化误差因子 $U$

\[
\boxed{U = \frac{|S_{12}||S_{21}||S_{11}||S_{22}|}{(1 - |S_{11}|^2)(1 - |S_{22}|^2)}}
\]

增益误差边界：
\[
\frac{1}{(1+U)^2} \le \frac{G_T}{G_{TU}} \le \frac{1}{(1-U)^2}
\]

当 $U \ll 1$（通常 $< 0.1$）时单向近似有效。

### MAG 和 MSG

**Maximum Available Gain**（仅在 $K \ge 1$ 时定义）：

\[
\boxed{G_{\text{MAG}} = \frac{|S_{21}|}{|S_{12}|} \left(K - \sqrt{K^2 - 1}\right)}
\]

当 $K=1$ 时退化为：

**Maximum Stable Gain**：

\[
\boxed{G_{\text{MSG}} = \frac{|S_{21}|}{|S_{12}|}}
\]

$G_{\text{MSG}}$ 是 $K=1$ 时最大可用增益的上限。

---

## 10.4 单级放大器设计

### 10.4.1 最大增益设计（共轭匹配）

对于**无条件稳定**器件，最大增益通过同时在输入和输出端共轭匹配实现：

\[
\Gamma_S = \Gamma_{\text{in}}^* = \left(S_{11} + \frac{S_{12}S_{21}\Gamma_L}{1 - S_{22}\Gamma_L}\right)^*
\]

\[
\Gamma_L = \Gamma_{\text{out}}^* = \left(S_{22} + \frac{S_{12}S_{21}\Gamma_S}{1 - S_{11}\Gamma_S}\right)^*
\]

联立求解：

\[
\boxed{\Gamma_S = \frac{B_1 \pm \sqrt{B_1^2 - 4|C_1|^2}}{2C_1}}
\]
\[
\boxed{\Gamma_L = \frac{B_2 \pm \sqrt{B_2^2 - 4|C_2|^2}}{2C_2}}
\]

其中：
\[
\begin{aligned}
C_1 &= S_{11} - \Delta S_{22}^* \\
C_2 &= S_{22} - \Delta S_{11}^* \\
B_1 &= 1 + |S_{11}|^2 - |S_{22}|^2 - |$\Delta$|^2 \\
B_2 &= 1 + |S_{22}|^2 - |S_{11}|^2 - |$\Delta$|^2
\end{aligned}
\]

选择 $|\Gamma| < 1$ 的解（稳定解）。

此时最大 transducer gain：
\[
G_{T,\max} = \frac{|S_{21}|}{|S_{12}|} \left(K - \sqrt{K^2 - 1}\right) = G_{\text{MAG}}
\]

### 10.4.2 指定增益设计（双向器件）

#### Operating Gain 圆（$\Gamma_L$ 平面）

等 $G_P$ 圆方程（固定增益 $g_p = G_P / |S_{21}|^2$）：

圆心和半径：

\[
C_{p} = \frac{g_p C_2^*}{1 + g_p(|S_{22}|^2 - |$\Delta$|^2)}
\quad
R_{p} = \frac{\sqrt{1 - 2K|S_{12}S_{21}|g_p + |S_{12}S_{21}|^2 g_p^2}}{|1 + g_p(|S_{22}|^2 - |$\Delta$|^2)|}
\]

其中 $C_2 = S_{22} - \Delta S_{11}^*$。选定 $\Gamma_L$ 后，$\Gamma_S = \Gamma_{\text{in}}^*$ 实现 $G_T = G_P$。

#### Available Gain 圆（$\Gamma_S$ 平面）

等 $G_A$ 圆方程（$g_a = G_A / |S_{21}|^2$）：

\[
C_{a} = \frac{g_a C_1^*}{1 + g_a(|S_{11}|^2 - |$\Delta$|^2)}
\quad
R_{a} = \frac{\sqrt{1 - 2K|S_{12}S_{21}|g_a + |S_{12}S_{21}|^2 g_a^2}}{|1 + g_a(|S_{11}|^2 - |$\Delta$|^2)|}
\]

其中 $C_1 = S_{11} - \Delta S_{22}^*$。选定 $\Gamma_S$ 后，$\Gamma_L = \Gamma_{\text{out}}^*$ 实现 $G_T = G_A$。

### 10.4.3 单向化指定增益设计（$S_{12} = 0$）

$G_S$ 和 $G_L$ 的等增益圆：

#### 输入等增益圆（$\Gamma_S$ 平面）

\[
g_s = G_S / (1 - |S_{11}|^2) \quad (\text{归一化增益因子})
\]

圆心：
\[
C_{gs} = \frac{g_s S_{11}^*}{1 - |S_{11}|^2(1 - g_s)}
\]

半径：
\[
R_{gs} = \frac{\sqrt{1 - g_s}\,(1 - |S_{11}|^2)}{1 - |S_{11}|^2(1 - g_s)}
\]

#### 输出等增益圆（$\Gamma_L$ 平面）

\[
g_l = G_L / (1 - |S_{22}|^2)
\]

圆心：
\[
C_{gl} = \frac{g_l S_{22}^*}{1 - |S_{22}|^2(1 - g_l)}
\]

半径：
\[
R_{gl} = \frac{\sqrt{1 - g_l}\,(1 - |S_{22}|^2)}{1 - |S_{22}|^2(1 - g_l)}
$$

---

## 10.5 宽带放大器

### 增益滚降补偿

晶体管 $|S_{21}|$ 通常以 ~6 dB/octave 滚降。补偿策略：

1. **失配匹配**：低频故意失配降低增益，高频尽量匹配提高增益
2. **负反馈**：并联或串联反馈平坦化增益
3. **平衡放大器**：3 dB 耦合器 + 两个相同放大器
4. **分布式放大器**：人工传输线结构实现超宽带

### 反馈放大器

- **串联反馈**（源极退化）：提高输入阻抗、稳定增益
- **并联反馈**：降低输入/输出阻抗、平坦增益
- **串联-并联反馈**：设计灵活

---

## 10.6 多级放大器

### 级联总增益

\[
G_{T,\text{total}} = \prod_{i=1}^{N} G_{T,i}
\]

dB 表示：
\[
G_{T,\text{total}}[\text{dB}] = \sum_{i=1}^{N} G_{T,i}[\text{dB}]
\]

### 级间匹配

- 前级输出 $\Gamma_{\text{out}}$ 匹配到后级输入 $\Gamma_{\text{in}}$
- 理想情况：级间共轭匹配
- 忽略级间传输线效应（当级间距离远小于波长时）

### 噪声-增益折中

- 前级 LNA 通常对噪声系数要求高，增益不必最大
- 后续级可优化增益和线性度
- 使用 $G_A$ 圆和恒定噪声圆综合设计

---

## 重要工程要点总结

| 概念 | 要点 |
|------|------|
| 无条件稳定 | $K > 1$ 且 $|$\Delta$| < 1$，对所有无源负载稳定 |
| 有条件稳定 | $K < 1$，需要避免进入不稳定区域 |
| 稳定圆 | 在 $\Gamma_S$ 或 $\Gamma_L$ 平面上画出稳定边界 |
| 最大增益 | 共轭匹配 $\Gamma_S = \Gamma_{\text{in}}^*$, $\Gamma_L = \Gamma_{\text{out}}^*$ |
| MAG vs MSG | $G_{\text{MAG}} \le G_{\text{MSG}}$，$K=1$ 时相等 |
| 单向增益 | $S_{12} \approx 0$ 时使用，$U$ 因子判断误差 |
| 等增益圆 | 在设计增益非最大时选择 $\Gamma_S$ 和 $\Gamma_L$ |
| 宽带 | 反馈/平衡/分布式结构用于宽频带 |
| 多级 | 级间共轭匹配最大化总增益 |

---

## 参考文献

- D. M. Pozar, *Microwave Engineering*, 4th ed., Wiley, 2012, Chapter 10.
- G. Gonzalez, *Microwave Transistor Amplifiers: Analysis and Design*, 2nd ed., Prentice Hall, 1997.
- J. M. Rollett, "Stability and Power-Gain Invariants of Linear Twoports," *IRE Trans. Circuit Theory*, vol. CT-9, pp. 29–32, 1962.
- M. L. Edwards and J. H. Sinsky, "A New Criterion for Linear 2-Port Stability Using a Single Geometrically Derived Parameter," *IEEE Trans. MTT*, vol. 40, no. 12, pp. 2303–2311, 1992.

---

## 10.7 Amplifier Noise (放大器噪声)

> Pozar §10.7 核心内容：噪声系数、二端口噪声模型、恒定噪声圆、LNA 设计中的噪声-增益折中。

---

### 10.7.1 噪声系数与噪声温度 (Noise Figure & Noise Temperature)

#### 噪声系数 (Noise Factor / Noise Figure)

**基本定义**——放大器将噪声叠加到信号上，使输出信噪比劣化：

\[
\boxed{F = \frac{(S/N)_{\text{in}}}{(S/N)_{\text{out}}} = \frac{N_{\text{out}}}{G \cdot N_{\text{in}}}}
\]

- $F$：noise **factor**（线性值，> 1 表示额外噪声）
- $NF$：noise **figure** = $10 \log_{10} F$（单位 dB）
- $G$：放大器可用增益 (available gain)
- $N_{\text{in}} = k T_0 B$：输入噪声功率（$T_0 = 290$ K 为标准参考温度，$k = 1.38\times 10^{-23}$ J/K 为玻尔兹曼常数，$B$ 为带宽）

#### 等效噪声温度 (Equivalent Noise Temperature)

将放大器的内部噪声等效为热噪声，用等效温度 $T_e$ 表示：

\[
\boxed{T_e = T_0 (F - 1)}
\quad\Longleftrightarrow\quad
\boxed{F = 1 + \frac{T_e}{T_0}}
\]

- $T_e$ 越大，器件噪声越差
- 级联系统中，首级 $T_e$ 最为关键

**量纲检查**：$F$ 无量纲，$T_e$ 单位 K，$T_0$ 单位 K → OK。

---

### 10.7.2 二端口噪声模型 (Two-Port Noise Model)

#### 等效输入噪声源

有噪二端口网络可等效为**无噪二端口 + 输入端串联噪声电压源 $v_n$ + 并联噪声电流源 $i_n$**：

```
  端口① ──┬──  + v_n ──── 无噪二端口 ──── 端口②
          │      −        (S参数)
          └── i_n ──┘         
```

- $\overline{v_n^2}$：等效输入噪声电压谱密度（$V^2$/Hz）
- $\overline{i_n^2}$：等效输入噪声电流谱密度（$A^2$/Hz）
- $v_n$ 与 $i_n$ 通常部分相关

#### 噪声相关矩阵 (Correlation Matrix)

在导纳表示中，噪声相关矩阵为：

\[
\mathbf{C}_Y = \begin{bmatrix}
\overline{i_1^2} & \overline{i_1 i_2^*} \\
\overline{i_1^* i_2} & \overline{i_2^2}
\end{bmatrix}
\quad\text{或}\quad
\mathbf{C}_A = 4kT_0 \begin{bmatrix}
R_n & \dfrac{F_{\min} - 1}{2} - R_n Y_{\text{opt}}^* \\
\dfrac{F_{\min} - 1}{2} - R_n Y_{\text{opt}} & R_n |Y_{\text{opt}}|^2
\end{bmatrix}
$$

实践中常用**四个噪声参数**完整描述二端口噪声：
1. **$F_{\min}$**：最小噪声因子（器件能达到的最低噪声）
2. **$R_n$**：等效噪声电阻 [Ω]
3. **$Y_{\text{opt}} = G_{\text{opt}} + jB_{\text{opt}}$**：最优源导纳（给出最小 $F$）
4. **$\Gamma_{\text{opt}}$**：最优源反射系数（等效于 $Y_{\text{opt}}$）

---

### 10.7.3 噪声系数公式推导 (Y参数 → Γ参数)

#### Y-参数形式

二端口噪声系数仅取决于**源阻抗/导纳**，与负载无关（假设单向化或输出匹配良好）：

\[
\boxed{F = F_{\min} + \frac{R_n}{G_s} |Y_s - Y_{\text{opt}}|^2}
\]

其中：
- $Y_s = G_s + jB_s$：源导纳
- $F_{\min}$：最小噪声因子（$Y_s = Y_{\text{opt}}$ 时达到）
- $R_n$：噪声电阻，度量 $F$ 偏离 $F_{\min}$ 的敏感度
- 量纲：$F$ 无量纲，$R_n$ [Ω]，$G_s$ [S] = 1/Ω，$|Y_s - Y_{\text{opt}}|^2$ [S²] → OK

#### 转换到 Γ-参数形式

利用反射系数与导纳的关系：
\[
Y_s = Y_0\frac{1 - \Gamma_s}{1 + \Gamma_s},\quad
Y_{\text{opt}} = Y_0\frac{1 - \Gamma_{\text{opt}}}{1 + \Gamma_{\text{opt}}},\quad
Y_0 = \frac{1}{Z_0}
\]

**第一步**：计算导纳差绝对值

\[
\begin{aligned}
Y_s - Y_{\text{opt}} &= Y_0\left(\frac{1 - \Gamma_s}{1 + \Gamma_s} - \frac{1 - \Gamma_{\text{opt}}}{1 + \Gamma_{\text{opt}}}\right)\\[4pt]
&= Y_0\cdot \frac{(1 - \Gamma_s)(1 + \Gamma_{\text{opt}}) - (1 - \Gamma_{\text{opt}})(1 + \Gamma_s)}{(1 + \Gamma_s)(1 + \Gamma_{\text{opt}})}\\[4pt]
&= Y_0\cdot \frac{2(\Gamma_{\text{opt}} - \Gamma_s)}{(1 + \Gamma_s)(1 + \Gamma_{\text{opt}})}
\end{aligned}
\]

\[
\therefore |Y_s - Y_{\text{opt}}|^2 = \frac{4Y_0^2 |\Gamma_s - \Gamma_{\text{opt}}|^2}{|1 + \Gamma_s|^2 |1 + \Gamma_{\text{opt}}|^2}
\]

**第二步**：用 Γ 表示 $G_s$

\[
G_s = \operatorname{Re}(Y_s) = Y_0 \cdot \frac{1 - |\Gamma_s|^2}{|1 + \Gamma_s|^2}
\]

**第三步**：代入 Y-参数公式

\[
\begin{aligned}
\frac{R_n}{G_s}|Y_s - Y_{\text{opt}}|^2
&= R_n\cdot \frac{|1 + \Gamma_s|^2}{Y_0 (1 - |\Gamma_s|^2)}
   \cdot \frac{4Y_0^2 |\Gamma_s - \Gamma_{\text{opt}}|^2}{|1 + \Gamma_s|^2 |1 + \Gamma_{\text{opt}}|^2}\\[4pt]
&= \frac{4R_n Y_0}{1 - |\Gamma_s|^2}
   \cdot \frac{|\Gamma_s - \Gamma_{\text{opt}}|^2}{|1 + \Gamma_{\text{opt}}|^2}
\end{aligned}
\]

**第四步**：代入 $Y_0 = 1/Z_0$，得到**Γ-参数形式**：

\[
\boxed{F(\Gamma_s) = F_{\min} + \frac{4 R_n}{Z_0}
       \cdot \frac{|\Gamma_s - \Gamma_{\text{opt}}|^2}
                {(1 - |\Gamma_s|^2)\,|1 + \Gamma_{\text{opt}}|^2}}
\]

**关键结论**：
- 当 $\Gamma_s = \Gamma_{\text{opt}}$ 时，$F = F_{\min}$
- 噪声系数的增量正比于 $\Gamma_s$ 平面上距 $\Gamma_{\text{opt}}$ 的距离平方
- 分母 $(1 - |\Gamma_s|^2)$ 表明源反射系数趋近单位圆时，噪声系数急剧恶化

---

### 10.7.4 恒定噪声圆 (Constant Noise Circles)

#### 推导

固定 $F = F_k > F_{\min}$，定义无量纲参数：

\[
\boxed{N \triangleq \frac{F_k - F_{\min}}{4R_n/Z_0}\,|1 + \Gamma_{\text{opt}}|^2}
\]

则噪声公式变为：

\[
\frac{|\Gamma_s - \Gamma_{\text{opt}}|^2}{1 - |\Gamma_s|^2} = N
\]

展开 $|\Gamma_s - \Gamma_{\text{opt}}|^2 = |\Gamma_s|^2 - 2\operatorname{Re}(\Gamma_s \Gamma_{\text{opt}}^*) + |\Gamma_{\text{opt}}|^2$：

\[
|\Gamma_s|^2 - 2\operatorname{Re}(\Gamma_s \Gamma_{\text{opt}}^*) + |\Gamma_{\text{opt}}|^2 = N - N|\Gamma_s|^2
\]

整理为标准圆方程形式：

\[
|\Gamma_s|^2 - \frac{2}{1+N}\operatorname{Re}(\Gamma_s \Gamma_{\text{opt}}^*)
= \frac{N - |\Gamma_{\text{opt}}|^2}{1+N}
\]

配方完成平方：

\[
\left|\Gamma_s - \frac{\Gamma_{\text{opt}}}{1+N}\right|^2
= \frac{N(N+1-|\Gamma_{\text{opt}}|^2)}{(1+N)^2}
\]

#### 圆心和半径

\[
\boxed{C_F = \frac{\Gamma_{\text{opt}}}{1+N}}
\qquad
\boxed{r_F = \frac{\sqrt{N\,(N+1-|\Gamma_{\text{opt}}|^2)}}{1+N}}
\]

其中 $N$ 由目标 NF 值 $F_k$ 定义：

\[
N = \frac{F_k - F_{\min}}{4R_n/Z_0}\,|1 + \Gamma_{\text{opt}}|^2
\]

**恒定噪声圆特点**：
- 圆心 $C_F$ 从原点沿 $\Gamma_{\text{opt}}$ 方向移动，$F_k$ 越大（$N$ 越大）圆心越靠近原点
- 半径随 $F_k$ 增大先增大后减小
- $F_k = F_{\min}$ 时 $N=0$，退化为点 $\Gamma_{\text{opt}}$
- $F_k \to \infty$ 时 $N \to \infty$，$C_F \to 0$（原点），$r_F \to 1$（单位圆）——匹配差时噪声无限大

---

### 10.7.5 等增益圆与噪声圆交点设计法

#### LNA 设计的核心矛盾

- **最大增益**要求 $\Gamma_S = \Gamma_{\text{in}}^*$（共轭匹配，通常在 $S_{11}^*$ 附近）
- **最小噪声**要求 $\Gamma_S = \Gamma_{\text{opt}}$
- 通常 $S_{11}^* \neq \Gamma_{\text{opt}}$ → 无法同时满足
- **解决方案**：在 $\Gamma_S$ 平面上找到等增益圆与恒定噪声圆的**交点**，选择最优折中

#### 设计步骤

1. **确认器件噪声参数**：$F_{\min}$、$R_n$、$\Gamma_{\text{opt}}$
2. **在 $\Gamma_S$ 平面画恒定噪声圆**（$F = F_{\min},\ F_{\min}+0.2,\ F_{\min}+0.5,\ \dots$）
3. **画等 $G_A$ 圆**（使用 §10.4.2 的 Available Gain Circle 公式）
4. **找交点**：某 NF 圆与某 $G_A$ 圆的交点即为候选 $\Gamma_S$
5. **验证稳定性**：确认 $|\Gamma_{\text{in}}| < 1$
6. **设计输出匹配**：$\Gamma_L = \Gamma_{\text{out}}^*$（最大化输出增益）

#### 噪声-增益折中设计流程

```
       Γ_S 平面 (Smith 图)
       ┌──────────────────────┐
       │  • Γ_opt (F_min点)   │
       │  ╰ ─ 恒定噪声圆       │
       │  ╰ ─ 等增益圆         │
       │  ★ 交点 → 最优 Γ_S    │
       └──────────────────────┘
          ↓
   Γ_L = Γ_out* (输出共轭匹配)
          ↓
   最终：G_T 略小，NF 略大
```

**工程经验**：
- 在 $F_{\min}+0.5$ dB 圆内通常可找到较好的增益
- 若 $S_{11}^*$ 与 $\Gamma_{\text{opt}}$ 相距很远，可用**源极退化**（Source Degeneration）调整 $\Gamma_{\text{opt}}$
- 高 $R_n$ 表示 NF 对源匹配不敏感→设计灵活；低 $R_n$ 要求精确匹配 $\Gamma_{\text{opt}}$

---

### 10.7.6 LNA 设计实例 (Pozar Ex10.7 风格)

**器件参数**（典型 pHEMT @ 10 GHz）：

| 参数 | 值 |
|------|-----|
| $F_{\min}$ | 1.0 dB ($F_{\min} = 1.26$ linear) |
| $R_n$ | 5 Ω |
| $\Gamma_{\text{opt}}$ | $0.65 \angle 130^\circ$ |
| $S_{11}$ | $0.55 \angle -120^\circ$ |
| $S_{21}$ | $5.5 \angle 75^\circ$ |
| $S_{12}$ | $0.04 \angle 35^\circ$ |
| $S_{22}$ | $0.45 \angle -50^\circ$ |

**设计目标**：
- NF \leq 1.5 dB
- $G_T \ge 10$ dB
- 无条件稳定

**设计过程**：

1. **计算稳定性**：$K = 1.15,\ |$\Delta$| = 0.62$ → 无条件稳定 ✓
2. **计算等增益圆**：$G_A = 10, 11, 12$ dB 在 $\Gamma_S$ 平面
3. **计算恒定噪声圆**：$NF = 1.0, 1.2, 1.5, 2.0$ dB
4. **选择交点**：$\Gamma_S = 0.60 \angle 115^\circ$ 给出 $NF = 1.3$ dB，$G_A = 10.5$ dB
5. **输出匹配**：$\Gamma_{\text{out}} = S_{22} + \frac{S_{12}S_{21}\Gamma_S}{1 - S_{11}\Gamma_S}$，取 $\Gamma_L = \Gamma_{\text{out}}^*$
6. **最终性能**：$G_T = 10.2$ dB，$NF = 1.4$ dB

---

### 10.7.7 级联放大器噪声 (Cascaded Noise — Friis 公式)

#### Friis 公式（从 §10.7 二端口视角）

级联 $N$ 级的**总噪声因子**：

\[
\boxed{F_{\text{total}} = F_1 + \frac{F_2 - 1}{G_1}
       + \frac{F_3 - 1}{G_1 G_2} + \cdots
       + \frac{F_N - 1}{G_1 G_2 \cdots G_{N-1}}}
\]

其中：
- $F_i$：第 $i$ 级的噪声因子（**线性值**）
- $G_i$：第 $i$ 级的**可用增益**（Available Gain，线性值）

NF 单位转换：
\[
NF_i\ [\text{dB}] = 10\log_{10} F_i,\qquad
F_i = 10^{NF_i/10}
\]

#### Friis 公式的核心结论

**首级主导噪声**——只要 $G_1$ 足够大，后续各级的噪声贡献被 $G_1$ 压缩：

\[
F_{\text{total}} \approx F_1 + \frac{F_2 - 1}{G_1} \quad(\text{当 } G_1 \gg 1)
\]

**工程启示**：
- LNA 第一级必须同时有**低 NF** 和**适当增益**（增益太高会恶化线性度，太低则后续级噪声贡献大）
- 第二级 NF 虽不如第一级关键，但 $G_1$ 有限时仍需关注
- 混频器放在第一级后，因为混频器 NF 通常较高

#### 系统噪声温度

级联噪声温度等效：

\[
\boxed{T_{\text{total}} = T_1 + \frac{T_2}{G_1} + \frac{T_3}{G_1 G_2} + \cdots}
\]

其中 $T_i = T_0 (F_i - 1)$。

#### 噪声-增益乘积

对两级放大器，可定义**噪声-增益乘积**作为优值 (Figure of Merit)：

\[
\boxed{M = F_1 \cdot G_1 + (F_2 - 1)}
\]

较小的 $M$ 表示较好的级联噪声性能。

---

### 10.7.8 器件的噪声参数提取

#### 从数据手册获取噪声参数

典型 FET/MESFET 数据手册提供：
- **$NF_{\min}$ vs. $f$**：最小 NF 随频率变化曲线
- **$\Gamma_{\text{opt}}$ vs. $f$**：最佳源反射系数随频率变化
- **$R_n$ vs. $f$**：噪声电阻随频率变化

#### 频率依赖关系（经验模型）

\[
F_{\min}(f) = 1 + k_f \frac{f}{f_T} \sqrt{g_m (R_g + R_s)}
\]

其中：
- $f_T$：截止频率
- $g_m$：跨导
- $R_g, R_s$：栅极和源极寄生电阻
- $\Gamma_{\text{opt}}$ 和 $R_n$ 通常为频率的复杂函数

#### 测量方法

1. **Y-因子法**：用冷/热噪声源测量 $F$，再通过 tuner 扫描 $\Gamma_s$ 提取四个噪声参数
2. **冷源法**：只用室温负载，通过矢量接收机测量
3. **NPS 法**：使用噪声参数测试仪 (Noise Parameter Set)

---

### 10.7.9 噪声系数计算公式汇总

| 公式 | 适用场景 |
|------|----------|
| $\displaystyle F = F_{\min} + \frac{R_n}{G_s}|Y_s - Y_{\text{opt}}|^2$ | Y-参数形式，$Y_s$ 已知 |
| $\displaystyle F = F_{\min} + \frac{4R_n}{Z_0}\frac{|\Gamma_s - \Gamma_{\text{opt}}|^2}{(1-|\Gamma_s|^2)|1+\Gamma_{\text{opt}}|^2}$ | Γ-参数形式，Smith 图中最实用 |
| $\displaystyle C_F = \frac{\Gamma_{\text{opt}}}{1+N},\ r_F = \frac{\sqrt{N(N+1-|\Gamma_{\text{opt}}|^2)}}{1+N}$ | 恒定噪声圆圆心和半径 |
| $\displaystyle N = \frac{F_k - F_{\min}}{4R_n/Z_0}|1+\Gamma_{\text{opt}}|^2$ | 恒定噪声圆中间参数 |
| $\displaystyle F_{\text{total}} = F_1 + \frac{F_2-1}{G_1} + \frac{F_3-1}{G_1G_2} + \cdots$ | 级联 Friis 公式 |
| $\displaystyle T_e = T_0(F-1)$ | 噪声因子 ↔ 等效噪声温度 |

---

### 10.7.10 工程要点总结

| 概念 | 要点 |
|------|------|
| 噪声系数 | $F = (S/N)_{\text{in}} / (S/N)_{\text{out}}$，$NF[\text{dB}] = 10\log F$ |
| 噪声参数 | $(F_{\min}, R_n, \Gamma_{\text{opt}})$ — 器件出厂即确定 |
| 公式形式 | 两个等价形式：Y-参数和 Γ-参数 |
| 恒定噪声圆 | $\Gamma_s$ 平面上 $NF$=常数 的轨迹 |
| 增益-噪声折中 | $\Gamma_{\text{opt}} \neq S_{11}^*$ → 需要在恒定噪声圆与等增益圆之间选择 |
| 级联噪声 | 首级噪声被后续级增益压缩，LNA 第一级最关键 |
| $R_n$ 的含义 | 大 $R_n$ → NF 对源匹配不敏感；小 $R_n$ → 需精确匹配 $\Gamma_{\text{opt}}$ |
| dB↔线性 | $F_{\text{linear}} = 10^{NF_{\text{dB}}/10}$，$NF_{\text{dB}} = 10\log_{10}(F_{\text{linear}})$ |

