# Chapter 4: Transmission Lines and Signal Integrity
## Paul — Introduction to Electromagnetic Compatibility, 2nd Ed.

---

## 4.1 传输线基础概念

### 4.1.1 什么是传输线

传输线（Transmission Line）是承载数字或模拟信号的一对平行导体。与普通导线不同，传输线具有**分布参数特性**——电压和电流同时随时间和位置变化。

**三类典型结构**：

| 结构 | 描述 | 介质环境 |
|------|------|---------|
| 双导线 (Two-wire) | 两根平行圆导线 | 空气/自由空间 |
| 单导线 above ground plane | 一根导线平行于大地 | 空气 |
| 同轴电缆 (Coaxial) | 内导体居中，外层圆柱屏蔽 | 介质填充（Teflon、PE等） |

PCB 上的走线（lands）具有矩形截面，典型结构包括**带状线 (Stripline)** 和**微带线 (Microstrip)**。

**信号完整性 (Signal Integrity)**：确保传输线输入端和输出端的波形相同（或近似相同）。当 $R_L = Z_C$（匹配）时，线对信号"无影响"——这是终极目标。

### 4.1.2 传播速度与时延

无损耗线的波速：

$$
v = \frac{1}{\sqrt{lc}} = \frac{c_0}{\sqrt{\varepsilon_{eff}}} \quad \text{m/s} \tag{4.7}
$$

时延：

$$
T_D = \frac{L}{v} \tag{4.1}
$$

**典型数值**：

| 结构 | $\varepsilon_{eff}$ | $v$ (m/s) | $T_D$ (ns/m) |
|------|------------|---------|----------|
| 自由空间/双导线 | 1.0 | $3\times10^8$ | 3.33 |
| 同轴（Teflon, $\varepsilon_r=2.1$） | 2.1 | $2.07\times10^8$ | 4.83 |
| Stripline（FR-4, $\varepsilon_r=4.7$） | 4.7 | $1.38\times10^8$ | 7.2 |
| Microstrip（$\varepsilon_{eff}\approx2.85$） | ~2.85 | $1.78\times10^8$ | 5.6 |

**工程直觉**：现代数字时钟上升/下降时间约 1 ns ~ 500 ps，6英寸的 Stripline 走线总时延已达 1.1 ns——已与信号上升时间可比拟，**必须按传输线处理**。

---

## 4.2 传输线方程（Telegrapher Equations）

### 4.2.1 分布参数电路模型

将传输线视为串联电感 $l\,\Delta z$ 和并联电容 $c\,\Delta z$ 的微段。对长度为 $\Delta z$ 的微元写基尔霍夫定律，取 $\Delta z \to 0$ 极限：

$$
\frac{\partial V}{\partial z} = -l\,\frac{\partial I}{\partial t} \tag{4.2a}
$$

$$
\frac{\partial I}{\partial z} = -c\,\frac{\partial V}{\partial t} \tag{4.2b}
$$

解耦后得到一维波动方程：

$$
\frac{\partial^2 V}{\partial z^2} = lc\,\frac{\partial^2 V}{\partial t^2}, \qquad
\frac{\partial^2 I}{\partial z^2} = lc\,\frac{\partial^2 I}{\partial t^2} \tag{4.3}
$$

**核心物理图像**：脉冲施加于线路左端时，先对第一个电容充电、第一个电感充能，然后脉冲"移动"到下一个单元——这就是有限传播速度的根本原因。

### 4.2.2 有损耗模型（频域）

$$
\frac{d\hat{V}}{dz} = -\hat{z}\,\hat{I}, \qquad \frac{d\hat{I}}{dz} = -\hat{y}\,\hat{V} \tag{4.105}
$$

其中 $\hat{z}=r+j\omega l$、$\hat{y}=g+j\omega c$。

---

## 4.3 每单位长度参数：$l$ 与 $c$

### 4.3.1 TEM 模与静场方法

传输线的传播模是 **TEM（横向电磁）模**——电场和磁场完全在横向平面（$xy$ 平面），无纵向分量。这带来关键结论：**时变场的计算可以等价于静场计算**（解拉普拉斯方程）。

### 4.3.2 两大静场子问题

#### 子问题 1：电流导线的磁通（安培定律）

半径 $r$ 导线载电流 $I$（均匀分布），半径 $R_1$ 到 $R_2$ 之间的单位长度磁通：

$$
\Phi_m = \frac{\mu_0 I}{2\pi}\,\ln\!\left(\frac{R_2}{R_1}\right) \quad \text{Wb/m} \tag{4.12}
$$

磁场 $H_T = I/(2\pi r)$（ circumferential）。

#### 子问题 2：带电导线的电位差（高斯定律）

线电荷密度 $q$ 的导线，半径 $R_1$ 到 $R_2$ 之间的电位差：

$$
V = \frac{q}{2\pi\varepsilon_0}\,\ln\!\left(\frac{R_2}{R_1}\right) \quad \text{V} \tag{4.15}
$$

电场 $E_T = q/(2\pi\varepsilon_0 r)$（radial）。两式存在对偶关系（$B\leftrightarrow E$、$I\leftrightarrow q$）。

### 4.3.3 均匀介质关系

当周围介质均匀时：

$$
lc = \mu\varepsilon, \qquad v = \frac{1}{\sqrt{lc}} \tag{4.6, 4.7}
$$

因此只需求 $c$ 或 $l$ 其一，另一个由介质关系导出。

### 4.3.4 线型结构参数

#### 双导线（半径 $r_w$，间距 $s$，$s \gg r_w$）

$$
l \approx \frac{\mu_0}{\pi}\,\ln\!\left(\frac{s}{r_w}\right) \quad \text{H/m}, \qquad
c \approx \frac{\pi\varepsilon_0}{\ln(s/r_w)} \quad \text{F/m} \tag{4.19, 4.22}
$$

精确公式需用 $\cosh^{-1}$ 修正（误差 $s/r_w > 5$ 时 < 3%）。

#### 单导线 above ground plane（高度 $h$，半径 $r_w$）

镜像法，间距 $2h$ 的双导线系统，电容为一半：

$$
c \approx \frac{2\pi\varepsilon_0}{\ln(2h/r_w)}, \qquad
l \approx \frac{\mu_0}{2\pi}\,\ln\!\left(\frac{2h}{r_w}\right) \tag{4.27, 4.29}
$$

#### 同轴电缆（$r_w$, $r_s$, $\varepsilon_r$）

**对称性优势**：电荷/电流始终均匀分布，**不受邻近效应影响**，精确公式严格成立：

$$
l = \frac{\mu_0}{2\pi}\,\ln\!\left(\frac{r_s}{r_w}\right), \qquad
c = \frac{2\pi\varepsilon_0\varepsilon_r}{\ln(r_s/r_w)} \tag{4.32, 4.35}
$$

典型 RG58U：$Z_C = 50\,\Omega$（几何与介质的折中最优值）。

### 4.3.5 PCB 结构

#### 带状线 (Stripline)

完全嵌入 PCB 介质，$\varepsilon_{eff} = \varepsilon_r$，电场均匀：

$$
Z_C \approx \frac{30\pi}{\sqrt{\varepsilon_r}}\,\ln\!\left(\frac{s}{w}+0.441\right) \quad \Omega \tag{4.40a}
$$

#### 微带线 (Microstrip)

导体在外层表面，场部分在空气中——**非均匀介质**，需计算 $\varepsilon_{eff}$：

$$
\varepsilon_{eff} = \frac{\varepsilon_r+1}{2} + \frac{\varepsilon_r-1}{2}\cdot\frac{1}{\sqrt{1+10h/w}} \tag{4.41b}
$$

- $w \gg h$：$\varepsilon_{eff} \to \varepsilon_r$（场集中在基板内）
- $w \ll h$：$\varepsilon_{eff} \to (\varepsilon_r+1)/2$（场一半在空气中）

**特征阻抗**（分段表达式，见 Paul (4.41a)）。

#### 特征阻抗定义

$$
Z_C = \sqrt{\frac{l}{c}} = v\,l = \frac{1}{v\,c} \quad \Omega \tag{4.37, 4.39}
$$

**工程直觉**：微带线阻抗对工艺参数（$w$、$h$、$\varepsilon_r$ 公差）极敏感，是高速 PCB 制造的核心控制指标。

---

## 4.4 时域解：波反射与反弹图

### 4.4.1 无损波动方程时域通解

$$
V(z,t) = V^+\!\left(t - \frac{z}{v}\right) + V^-\!\left(t + \frac{z}{v}\right) \tag{4.44a}
$$

$$
I(z,t) = \frac{1}{Z_C}\,V^+\!\left(t - \frac{z}{v}\right) - \frac{1}{Z_C}\,V^-\!\left(t + \frac{z}{v}\right) \tag{4.44b}
$$

前向波和后向波的电压/电流比为 $\pm Z_C$。

### 4.4.2 反射系数

**负载反射系数**：

$$
\Gamma_L = \frac{R_L - Z_C}{R_L + Z_C} \tag{4.47}
$$

**源端反射系数**：

$$
\Gamma_S = \frac{R_S - Z_C}{R_S + Z_C} \tag{4.52}
$$

| 条件 | $\Gamma$ | 物理意义 |
|------|---------|---------|
| $R_L = Z_C$（匹配） | $0$ | 无反射 |
| $R_L = \infty$（开路） | $+1$ | 全反射，同相 |
| $R_L = 0$（短路） | $-1$ | 全反射，反相 |
| $R_L > Z_C$ | $>0$ | 部分反射，同相（过冲） |
| $R_L < Z_C$ | $<0$ | 部分反射，反相（下冲） |

### 4.4.3 反弹图法（Lattice / Bounce Diagram）

**步骤**：
1. $t=0$：源电压脉冲出发，幅度 $V_{init} = \frac{Z_C}{R_S+Z_C}\,V_S$
2. $t=T_D$：到达负载，产生反射 $\Gamma_L\,V_{init}$
3. $t=2T_D$：反射波回到源端，产生二次反射 $\Gamma_S\Gamma_L\,V_{init}$
4. 反复，每次幅度乘以 $\Gamma_S\Gamma_L$

**端电压**：

$$
V(0,t) = \frac{Z_C}{R_S+Z_C}\Big[ V_S(t) + (1+\Gamma_S)\Gamma_L V_S(t-2T_D) + \cdots \Big] \tag{4.53a}
$$

$$
V(L,t) = \frac{Z_C}{R_S+Z_C}\Big[ (1+\Gamma_L)V_S(t-T_D) + (1+\Gamma_L)\Gamma_S\Gamma_L V_S(t-3T_D) + \cdots \Big] \tag{4.53b}
$$

**振铃条件**：$\Gamma_S$ 和 $\Gamma_L$ **异号**时，负载电压在目标值附近振荡。大多数数字逻辑电路（低源阻抗 + 高输入阻抗负载）天然满足此条件 → **天然振铃**。

### 4.4.4 动态终端

#### 电容性负载（$Z_L = 1/sC$，源端匹配 $R_S=Z_C$）

$$
V_L(t) = V_0\Big(1 - e^{-(t-T_D)/T_C}\Big), \quad T_C = Z_C\,C \tag{4.67}
$$

50%点额外延迟：$t_d \approx 0.693\,C\,Z_C$。电容初始等效短路，逐渐过渡到开路。

#### 电感性负载（$Z_L = sL$）

$$
V_L(t) = V_0\,e^{-(t-T_D)/T_L}, \quad T_L = L/Z_C \tag{4.72}
$$

电感初始等效开路，逐渐变为短路。

**工程直觉**：实际数字门输入既有电容性（栅极），又有电感性（封装引线），形成复杂瞬态响应。

### 4.4.5 匹配方案

#### 串联匹配 (Series Match)

使 $R_S + R = Z_C$。初始出射 $V_0/2$，到达开路负载全反射，负载瞬间达到 $V_0$。**无功率损耗**（开路时无电流流经 $R$）。

#### 并联匹配 (Parallel Match)

使 $R \parallel R_L = Z_C$。入射波完全被吸收，**无反射**，但负载电压恒低于 $V_0$（分压），且 $R$ 在静态时有功耗。

### 4.4.6 "线不重要"的条件

当 $t_r > 10\,T_D$ 时，反射可忽略：

$$
t_r(\text{ns}) > L(\text{in.}) \tag{4.76}
$$

**典型对比**：

| 时钟频率 | $t_r$ 典型值 | 需要匹配的最小走线 |
|---------|------------|----------------|
| 100 MHz | 2 ns | 2 英寸 |
| 1 GHz | 200 ps | 0.2 英寸 |
| 3 GHz | 66 ps | 0.07 英寸 |

**工程直觉**：今天 3 GHz PC 时钟意味着即使 1 mm 的走线也可能需要匹配处理。

---

## 4.5 串扰 (Crosstalk)

### 耦合机制

- **感性耦合**（$L_m$）：攻击线电流产生的磁场在受害线中感应电压
- **容性耦合**（$C_m$）：攻击线与受害线间电容的分压效应

**串扰电压**：
- **近端串扰 (NEXT)**：在受害线源端，幅值约 $\propto C_m/c$
- **远端串扰 (FEXT)**：在受害线负载端，可能出现负尖峰

**工程直觉**：走线间距越近耦合越强；增加间距是降低串扰的最直接手段。

---

## 4.6 不连续性 (Discontinuities)

### 阻抗突变

走线宽度变化（$Z_{C1} \to Z_{C2}$）产生反射：

$$
\Gamma_{12} = \frac{Z_{C2} - Z_{C1}}{Z_{C2} + Z_{C1}}, \qquad
T_{12} = \frac{2Z_{C2}}{Z_{C2}+Z_{C1}} \tag{4.77}
$$

### 过孔 (Via)

过孔是最常见的阻抗不连续点——容性和感性效应共同作用。**背钻 (Backdrilling)** 可去除残余 stub，减少不连续性。

**工程直觉**：在 GHz 级信号中，即使一个过孔也可能造成显著反射。

---

## 4.7 正弦稳态（相量）解

### 4.7.1 频域方程

将 $\partial/\partial t \to j\omega$：

$$
\frac{d\hat{V}}{dz} = -j\omega l\,\hat{I}, \qquad \frac{d\hat{I}}{dz} = -j\omega c\,\hat{V} \tag{4.83}
$$

解：

$$
\hat{V}(z) = \hat{V}^+ e^{-j\beta z} + \hat{V}^- e^{+j\beta z} \tag{4.85a}
$$

其中 $\beta = \omega/v = 2\pi/\lambda$ 为相位常数。

### 4.7.2 反射系数（频域）

$$
\hat{\Gamma}_L = \frac{\hat{Z}_L - Z_C}{\hat{Z}_L + Z_C}, \qquad
\hat{\Gamma}(z) = \hat{\Gamma}_L\,e^{j2\beta(z-L)} \tag{4.92, 4.93}
$$

### 4.7.3 输入阻抗

$$
\hat{Z}_{in}(0) = Z_C\,\frac{\hat{Z}_L + jZ_C\tan(\beta L)}{Z_C + j\hat{Z}_L\tan(\beta L)} \tag{4.99}
$$

**特殊长度**：
- **短路**：$\hat{Z}_{in} = jZ_C\tan(\beta L)$
- **开路**：$\hat{Z}_{in} = -jZ_C\cot(\beta L)$
- **$\lambda/4$ 线**：$\hat{Z}_{in} = Z_C^2 / \hat{Z}_L$（阻抗变换器）

### 4.7.4 驻波比 (VSWR)

$$
\text{VSWR} = \frac{1+|\hat{\Gamma}_L|}{1-|\hat{\Gamma}_L|} \tag{4.101}
$$

- 匹配 → VSWR = 1
- 全反射 → VSWR = $\infty$

### 4.7.5 平均功率

$$
P_{avg}(z) = \frac{|\hat{V}^+|^2}{2Z_C}\,(1 - |\hat{\Gamma}|^2) \tag{4.103}
$$

反射功率占比 = $|\hat{\Gamma}|^2$。

---

## 4.8 有损耗传输线

### 4.8.1 损耗机制

| 损耗源 | 原因 | 频率特性 |
|--------|------|---------|
| 导体损耗 $r$ | 有限电导率 + 趋肤效应 | $\propto \sqrt{f}$（10 dB/dec） |
| 介质损耗 $g$ | 复介电常数 $\varepsilon_r = \varepsilon'_r - j\varepsilon''_r$ | $= \omega c\,\tan\delta$（20 dB/dec） |

### 4.8.2 趋肤效应

高频电流集中在导体表面，渗透深度：

$$
\delta = \frac{1}{\sqrt{\pi f \mu_0 \sigma}} \quad \text{m} \tag{4.112}
$$

铜在 1 GHz：$\delta \approx 2.1\,\mu\text{m}$。高频单位长度电阻 $r_{hf} \propto 1/\delta \propto \sqrt{f}$。

### 4.8.3 低损耗近似

当 $r \ll \omega l$ 且 $g \ll \omega c$ 时：

$$
\alpha \approx \frac{1}{2}\left(\frac{r}{Z_C} + g\,Z_C\right) \quad \text{Np/m} \tag{4.123a}
$$

$$
Z_C \approx \sqrt{\frac{l}{c}} \quad \text{（保持实数）}, \qquad v \approx \frac{1}{\sqrt{lc}} \tag{4.124}
$$

典型 FR-4 板：上述近似在 $f > 5$ MHz 后有效。

### 4.8.4 损耗对信号的影响

1. **幅度衰减**：功率按 $e^{-2\alpha L}$ 衰减（dB 损耗 = $8.686\,\alpha L$）
2. **色散**：不同频率分量以不同速度传播 → 脉冲展宽
3. **上升时间退化**：高频分量衰减更大

**工程直觉**：有损耗线的危害不仅是幅度衰减，更是**波形失真**——上升时间退化直接导致时序错误，比纯衰减更危险。

---

## 4.9 SPICE 传输线建模

### 精确无损模型

SPICE 的 `T` 元件基于 **Branin 等效电路**，对无损均匀传输线**精确建模**：

**关键参数**：`Z0` = $Z_C$（$\Omega$），`TD` = $T_D = L/v$（s）

```spice
VS 1 0 PWL(0 0 0.1N 5 5N 5 5.1N 0 10N 0)
RS 1 2 20
T   2 0 3 0 Z0=50 TD=0.2N
CL  3 0 5P
.TRAN 0.01N 10N 0 0.01N
.PROBE
.END
```

**SPICE 要点**：
- 最大时间步长必须 $\ll T_D$（否则漏掉快速变化）
- 集总 $\pi$ 模型用于 $L < \lambda/10$ 的近似分析
- SPICE 能处理非线性（二极管、BJT）和动态（$L$、$C$）负载，无需解析推导

---

## 关键公式速查

| 物理量 | 公式 | 编号 |
|--------|------|------|
| 相速度 | $v = 1/\sqrt{lc} = c_0/\sqrt{\varepsilon_{eff}}$ | (4.7) |
| 特性阻抗 | $Z_C = \sqrt{l/c} = v\,l = 1/(v\,c)$ | (4.37, 4.39) |
| 单程时延 | $T_D = L/v$ | (4.1) |
| 负载反射系数 | $\Gamma_L = (R_L-Z_C)/(R_L+Z_C)$ | (4.47) |
| 源端反射系数 | $\Gamma_S = (R_S-Z_C)/(R_S+Z_C)$ | (4.52) |
| 负载电压（匹配） | $V(L,t) = V(0,t-T_D)$ | (4.53d) |
| 双导线电感 | $l \approx (\mu_0/\pi)\ln(s/r_w)$ | (4.19) |
| 同轴电容 | $c = 2\pi\varepsilon_0\varepsilon_r/\ln(r_s/r_w)$ | (4.35) |
| 微带有效 $\varepsilon$ | $\varepsilon_{eff} = (\varepsilon_r+1)/2 + (\varepsilon_r-1)/2/\sqrt{1+10h/w}$ | (4.41b) |
| 趋肤深度 | $\delta = 1/\sqrt{\pi f\mu_0\sigma}$ | (4.112) |
| 低损衰减 | $\alpha \approx (r/Z_C + gZ_C)/2$ | (4.123a) |
| VSWR | $(1+|\Gamma|)/(1-|\Gamma|)$ | (4.101) |
| $\lambda/4$ 阻抗变换 | $Z_{in} = Z_C^2/Z_L$ | — |
| "线不重要"准则 | $t_r(\text{ns}) > L(\text{in.})$ | (4.76) |

---

## 工程直觉总结

1. **TEM 模传输线**的 $l$ 和 $c$ 由横截面几何结构决定，与频率无关（理想无损线）

2. **反射是信号完整性的头号敌人**：$\Gamma_S$ 和 $\Gamma_L$ 异号 → 天然振铃 → 数字逻辑错误

3. **上升时间决定一切**：皮秒级上升时间使厘米级走线也必须按传输线处理；今天的 3 GHz 时钟意味着 1 mm 走线也要考虑匹配

4. **匹配不是万能的**：有损耗线即使匹配也会因色散导致波形退化

5. **过孔和走线宽度变化**是 GHz 级设计中的主要不连续点来源

6. **SPICE 是信号完整性分析的王道工具**：对非线性/动态负载，解析法无能为力，SPICE 精确模型是唯一实用选择
