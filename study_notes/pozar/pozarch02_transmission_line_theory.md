# Pozar 《微波工程》第 2 章 — 传输线理论

> **参考**: Pozar, D. M., *Microwave Engineering*, 4th Edition, Chapter 2 (pp. 48–93)
> **范围**: 集总参数电路模型 → 电报方程 → 场分析 → 端接传输线 → Smith 圆图 → λ/4 变换器 → 源-负载失配 → 有耗线 → 瞬态

---

## 2.1 引言 — 何时用传输线模型

**核心判据**: 电路物理尺寸 $D$ 与信号波长 $\lambda$ 可比时，必须用传输线（分布参数）模型。

$$
D \gtrsim \frac{\lambda}{10} \quad \longrightarrow \quad \text{使用传输线理论}
$$

- $D \ll \lambda$（低频/小尺寸）：集总参数电路（基尔霍夫定律适用）
- $D \sim \lambda$（微波频段）：分布参数效应显著 → 电压/电流是空间和时间的函数

**传输线物理本质**: 电磁能量以 TEM（横电磁）波形式沿导波结构传播。

---

## 2.1 集总参数电路模型（Pozar 式 2.1–2.8）

### 分布参数（单位长度）

| 参数 | 符号 | 单位 | 物理含义 |
|------|------|------|---------|
| 串联电阻 | $R$ | $\Omega$/m | 导体损耗（趋肤效应） |
| 串联电感 | $L$ | H/m | 导体周围磁场储能 |
| 并联电导 | $G$ | S/m | 介质漏电损耗 |
| 并联电容 | $C$ | F/m | 导体间电场储能 |

对于无穷小线段 $\Delta z$，其等效电路为：

```
I(z)          RΔz    LΔz           I(z+Δz)
  →      ──┬─/\/\─┬─□□□──┬───┬──        →
  +        │       │      │   │          +
V(z)      ─┬─     ─┬─    ─┬─ ─┬─      V(z+Δz)
  -        │ GΔz   │ CΔz  │   │          -
  ↑        │       │      │   │          ↑
  └─────── 0 ───────────── 0 ──────→ z
```

### 电报方程（Telegrapher's Equations）

时域形式：

$$
-\frac{\partial V(z,t)}{\partial z} = R I(z,t) + L \frac{\partial I(z,t)}{\partial t}
$$

$$
-\frac{\partial I(z,t)}{\partial z} = G V(z,t) + C \frac{\partial V(z,t)}{\partial t}
$$

**推导**: 对 $\Delta z$ 段应用 KVL 和 KCL：

$$
V(z,t) - [R\Delta z] I(z,t) - [L\Delta z] \frac{\partial I(z,t)}{\partial t} - V(z+\Delta z,t) = 0
$$

除以 $\Delta z \to 0$ 得第一式。同理从 KCL 得第二式。

### 时谐形式（Pozar 式 2.5–2.8）

设 $V(z,t) = \text{Re}[V(z) e^{j\omega t}]$, $I(z,t) = \text{Re}[I(z) e^{j\omega t}]$：

$$
\frac{dV(z)}{dz} = -(R + j\omega L) I(z)
$$

$$
\frac{dI(z)}{dz} = -(G + j\omega C) V(z)
$$

### 波动方程

联立消去 $I$ 或 $V$：

$$
\frac{d^2 V(z)}{dz^2} - \gamma^2 V(z) = 0, \qquad
\frac{d^2 I(z)}{dz^2} - \gamma^2 I(z) = 0
$$

其中**传播常数**（Pozar 式 2.10）：

$$
\boxed{\gamma = \alpha + j\beta = \sqrt{(R + j\omega L)(G + j\omega C)}}
$$

- $\alpha$: 衰减常数 [Np/m]
- $\beta$: 相位常数 [rad/m]

**量纲检查**:
- $(R + j\omega L)$: [$\Omega$/m] = [V/A·m]
- $(G + j\omega C)$: [S/m] = [A/V·m]
- 乘积: [1/m²]，开方: [1/m] ✅

### 行波解

$$
\boxed{V(z) = V_0^+ e^{-\gamma z} + V_0^- e^{\gamma z}}
$$
$$
\boxed{I(z) = I_0^+ e^{-\gamma z} + I_0^- e^{\gamma z}}
$$

正向波 $V_0^+ e^{-\gamma z}$ 沿 $+z$ 传播，反向波 $V_0^- e^{\gamma z}$ 沿 $-z$ 传播。

### 特性阻抗（Pozar 式 2.13）

$$
\boxed{Z_0 = \frac{R + j\omega L}{\gamma} = \sqrt{\frac{R + j\omega L}{G + j\omega C}}}
\quad [\Omega]
$$

**物理直觉**: 特性阻抗是传输线的**本征参数**——它表征行波电压与电流之比，**不依赖于**线长或负载。正向波的电压电流比恒为 $+Z_0$，反向波为 $-Z_0$。这是传输线区别于普通导体最重要的概念。

---

## 2.2 无耗传输线（Pozar 式 2.11–2.15）

### 条件：$R = G = 0$

$$
\gamma = j\beta = j\omega\sqrt{LC}, \quad
\beta = \omega\sqrt{LC}
$$

$$
Z_0 = \sqrt{\frac{L}{C}} \quad \text{纯实数}
$$

### 相速度与波长

$$
v_p = \frac{\omega}{\beta} = \frac{1}{\sqrt{LC}}, \quad
\lambda = \frac{2\pi}{\beta} = \frac{v_p}{f}
$$

### 通用解

$$
V(z) = V_0^+ e^{-j\beta z} + V_0^- e^{j\beta z}
$$
$$
I(z) = \frac{V_0^+}{Z_0} e^{-j\beta z} - \frac{V_0^-}{Z_0} e^{j\beta z}
$$

---

## 2.2 传输线的场分析（Pozar 式 2.16–2.27）

### TEM 模式下 $L, C, R, G$ 的场计算公式

$$
L = \frac{\mu}{|I|^2} \iint_S |\mathbf{H}|^2 \, ds \quad [\text{H/m}]
$$

$$
C = \frac{\epsilon'}{|V|^2} \iint_S |\mathbf{E}|^2 \, ds \quad [\text{F/m}]
$$

$$
R = \frac{R_s}{|I|^2} \oint_C |\mathbf{J}|^2 \, dl \quad [\Omega/\text{m}]
$$

$$
G = \frac{\omega\epsilon''}{|V|^2} \iint_S |\mathbf{E}|^2 \, ds \quad [\text{S/m}]
$$

其中 $R_s = \sqrt{\pi f \mu_c / \sigma_c}$ 为表面电阻率。

### 例：同轴线参数（Pozar 式 2.17–2.20, Table 2.1）

| 参数 | 同轴线 | 双线 | 平行板 |
|------|--------|------|--------|
| $L$ | $\frac{\mu}{2\pi}\ln\frac{b}{a}$ | $\frac{\mu}{\pi}\cosh^{-1}\frac{D}{d}$ | $\frac{\mu d}{W}$ |
| $C$ | $\frac{2\pi\epsilon'}{\ln(b/a)}$ | $\frac{\pi\epsilon'}{\cosh^{-1}(D/d)}$ | $\frac{\epsilon' W}{d}$ |
| $R$ | $\frac{R_s}{2\pi}\left(\frac{1}{a}+\frac{1}{b}\right)$ | $\frac{2R_s}{\pi d}$ | $\frac{2R_s}{W}$ |
| $G$ | $\frac{2\pi\omega\epsilon''}{\ln(b/a)}$ | $\frac{\pi\omega\epsilon''}{\cosh^{-1}(D/d)}$ | $\frac{\omega\epsilon'' W}{d}$ |

---

## 2.3 端接无耗传输线（Pozar 式 2.28–2.47）

### 反射系数

在 $z = 0$ 处连接负载 $Z_L$ 的无耗线：

$$
\boxed{\Gamma = \frac{V_0^-}{V_0^+} = \frac{Z_L - Z_0}{Z_L + Z_0}}
$$

**关键性质**:
- $|\Gamma| \le 1$（被动负载）
- $\Gamma = 0$ 当 $Z_L = Z_0$（匹配）
- $\Gamma = +1$ 当 $Z_L = \infty$（开路）
- $\Gamma = -1$ 当 $Z_L = 0$（短路）

### 电压驻波比 VSWR（Pozar 式 2.35）

$$
\boxed{\text{VSWR} = S = \frac{V_{\max}}{V_{\min}} = \frac{1 + |\Gamma|}{1 - |\Gamma|}}
$$

$$
|\Gamma| = \frac{S - 1}{S + 1}
$$

**物理含义**: VSWR 度量阻抗失配度。$S = 1$ 表示完美匹配，$S \to \infty$ 接近全反射。

### 驻波模式

沿线的电压幅值分布：

$$
|V(z)| = |V_0^+| \, \big[ 1 + |\Gamma|^2 + 2|\Gamma|\cos(2\beta z - \theta_\Gamma) \big]^{1/2}
$$

- 电压最大值处：$\cos(2\beta z - \theta_\Gamma) = +1$，$|V|_{\max} = |V_0^+|(1+|\Gamma|)$
- 电压最小值处：$\cos(2\beta z - \theta_\Gamma) = -1$，$|V|_{\min} = |V_0^+|(1-|\Gamma|)$

### 输入阻抗（Pozar 式 2.42）

距负载距离 $l$ 处的输入阻抗：

$$
\boxed{Z_{\text{in}} = Z_0 \frac{Z_L + j Z_0 \tan(\beta l)}{Z_0 + j Z_L \tan(\beta l)}}
$$

### 特殊端接情况

| 负载 | $Z_{\text{in}}$ | $\Gamma$ | VSWR |
|------|----------------|----------|------|
| 短路 ($Z_L=0$) | $j Z_0 \tan(\beta l)$ | $-1$ | $\infty$ |
| 开路 ($Z_L=\infty$) | $-j Z_0 \cot(\beta l)$ | $+1$ | $\infty$ |
| 匹配 ($Z_L=Z_0$) | $Z_0$ | $0$ | $1$ |

**$\lambda/4$ 变换器特性**: 短路在 $\lambda/4$ 处变为开路, 开路在 $\lambda/4$ 处变为短路

**阻抗周期性**: $Z_{\text{in}}(l + \lambda/2) = Z_{\text{in}}(l)$

### 回波损耗（Return Loss, Pozar 式 2.36）

$$
\text{RL} = -20 \log_{10} |\Gamma| \quad [\text{dB}]
$$

- RL = $\infty$ dB 完美匹配 ($\Gamma=0$)
- RL = 0 dB 全反射 ($|\Gamma|=1$)

---

## 2.4 Smith 圆图（Pozar 式 2.48–2.59）

### 数学基础

Smith 圆图是 $\Gamma$ 复平面上的**保角映射**（双线性变换）：

$$
\Gamma = \frac{Z - Z_0}{Z + Z_0} = \frac{z - 1}{z + 1} \quad \text{其中 } z = \frac{Z}{Z_0} = r + jx
$$

反射系数 $\Gamma = \Gamma_r + j\Gamma_i = |\Gamma| e^{j\theta_\Gamma}$。

### 等电阻圆（Pozar 式 2.51）

由 $z = r + jx$ 代入 $\Gamma$ 公式，分离实部得：

$$
\left(\Gamma_r - \frac{r}{r+1}\right)^2 + \Gamma_i^2 = \left(\frac{1}{r+1}\right)^2
$$

- 圆心在 $(\frac{r}{r+1}, 0)$，半径 $\frac{1}{r+1}$
- $r=0$ 时：单位圆（纯电抗边界）
- $r \to \infty$ 时：点 $(1, 0)$（开路点）

### 等电抗圆（Pozar 式 2.52）

$$
(\Gamma_r - 1)^2 + \left(\Gamma_i - \frac{1}{x}\right)^2 = \left(\frac{1}{x}\right)^2
$$

- 圆心在 $(1, 1/x)$，半径 $1/|x|$
- $x=0$：实轴线（纯电阻）
- $x \to \pm\infty$：点 $(1, 0)$（开路点）

### Smith 圆图关键特征

| 特征 | 位置 |
|------|------|
| 开路 | $(1, 0)$ ($\Gamma = +1$) |
| 短路 | $(-1, 0)$ ($\Gamma = -1$) |
| 匹配点 | $(0, 0)$ ($\Gamma = 0$) |
| 纯电阻线 | 实轴 ($\Gamma_i = 0$) |
| 感性区 | 上半平面 ($\Gamma_i > 0$) |
| 容性区 | 下半平面 ($\Gamma_i < 0$) |
| 等 $|\Gamma|$ 圆 | 圆心在 $(0,0)$ 的同心圆 |

### 阻抗-导纳联合 Smith 图

将阻抗圆图旋转 $180^\circ$ 得到导纳圆图。二者叠加即为联合 Smith 图。

导纳：$y = \frac{Y}{Y_0} = g + jb$，其中 $g$ 为归一化电导，$b$ 为归一化电纳。

**关键操作**:
- 从阻抗到导纳：$\Gamma$ 旋转 $180^\circ$（即取反）
- 沿线移动：在等 $|\Gamma|$ 圆上旋转
  - 向发生器（顺时针）：$\theta_\Gamma \to \theta_\Gamma - 2\beta l$
  - 向负载（逆时针）：$\theta_\Gamma \to \theta_\Gamma + 2\beta l$

### Smith 圆图的操作步骤

1. **归一化** $z_L = Z_L/Z_0$，在圆图上找点
2. **画等 $|\Gamma|$ 圆**（以原点为圆心过该点）
3. **读取 $|\Gamma|$** 和 VSWR（圆右端与实轴交点）
4. **沿线变换**：在"向发生器"（WTG）刻度上旋转 $\Delta l/\lambda$
5. **读取新阻抗**：旋转后与等 $|\Gamma|$ 圆的交点

### 开槽线测量（Slotted Line, Pozar 式 2.60）

通过测量短路和负载两种状态下的驻波最小点位置，推算未知负载阻抗：

1. 接短路：记下最小点位置（每 $\lambda/2$ 重复）
2. 接负载：测量 VSWR 和最小点偏移 $\Delta z$
3. 从 Smith 图读出归一化负载阻抗

---

## 2.5 $\lambda/4$ 阻抗变换器（Pozar 式 2.63–2.70）

### 阻抗变换公式

长度为 $\lambda/4$ 的传输线（$\beta l = \pi/2$）：

$$
\boxed{Z_{\text{in}} = \frac{Z_1^2}{Z_L}}
$$

其中 $Z_1$ 为 $\lambda/4$ 段的特性阻抗。

### 匹配设计

要将负载 $R_L$（纯电阻）匹配到特性阻抗 $Z_0$：

$$
\boxed{Z_1 = \sqrt{Z_0 R_L}}
$$

### 带宽特性

反射系数幅值随频率变化：

$$
|\Gamma| = \frac{|R_L - Z_0|}{\sqrt{(R_L + Z_0)^2 + 4Z_0 R_L \tan^2(\beta l)}}
$$

在中心频率 $f_0$ 处 $\beta l = \pi/2$，$\tan(\beta l) \to \infty$，$|\Gamma|=0$。

**分数带宽**（VSWR $\le S_m$）：

$$
\frac{\Delta f}{f_0} = 2 - \frac{4}{\pi} \cos^{-1}\left[ \frac{S_m - 1}{S_m + 1} \cdot \frac{2\sqrt{Z_0 R_L}}{|R_L - Z_0|} \right]
$$

### 多次反射视角

$\lambda/4$ 段的匹配可从多次反射求和来理解：二次反射波的相位差 $180^\circ$，相互抵消。

---

## 2.6 源与负载失配（Pozar 式 2.71–2.78）

### 一般情况

- 源阻抗 $Z_G$，特性阻抗 $Z_0$，负载阻抗 $Z_L$
- 源端反射系数 $\Gamma_G = (Z_G - Z_0)/(Z_G + Z_0)$
- 负载端反射系数 $\Gamma_L = (Z_L - Z_0)/(Z_L + Z_0)$

### 最大功率传输条件

1. **负载匹配**：$Z_L = Z_0$（无反射）
2. **共轭匹配**：$Z_{\text{in}} = Z_G^*$（传输线输入阻抗等于源阻抗的共轭——在有反射时仍可实现最大功率）

---

## 2.7 有耗传输线（Pozar 式 2.79–2.98）

### 低耗近似（Pozar 式 2.85）

若 $R \ll \omega L$ 且 $G \ll \omega C$：

$$
\alpha \approx \frac{1}{2}\left( R\sqrt{\frac{C}{L}} + G\sqrt{\frac{L}{C}} \right)
= \frac{1}{2}\left( \frac{R}{Z_0} + G Z_0 \right)
$$

$$
\beta \approx \omega\sqrt{LC}
$$

$$
Z_0 \approx \sqrt{\frac{L}{C}} \quad \text{（实数）}
$$

### 无畸变线（Distortionless Line, Pozar 式 2.87–2.88）

条件：$RC = GL$（Heaviside 条件），此时：

$$
\gamma = \sqrt{RG} + j\omega\sqrt{LC}
$$

- $\alpha = \sqrt{RG}$ 与频率无关
- $v_p = 1/\sqrt{LC}$ 与频率无关
- 脉冲传播无畸变

### 端接有耗线

输入阻抗公式形式与无耗线相同，但 $\gamma = \alpha + j\beta$：

$$
Z_{\text{in}} = Z_0 \frac{Z_L + Z_0 \tanh(\gamma l)}{Z_0 + Z_L \tanh(\gamma l)}
$$

### 微扰法求衰减

$$
\alpha_c = \frac{R}{2Z_0}, \quad \alpha_d = \frac{G Z_0}{2}
$$

$\alpha_c$ 导体衰减，$\alpha_d$ 介质衰减。

### Wheeler 增量电感法则

$$
Z_0 = \frac{1}{c \sqrt{CC_0}}
$$

其中 $C_0$ 为空气介质时的电容。

---

## 2.8 传输线瞬态（Pozar 式 2.99–2.114）

### 脉冲反射

对于阶跃信号，传输线表现为延迟线：

1. 源产生向负载的入射波 $V^+$
2. 到达负载后，反射波 $V^- = \Gamma_L V^+$
3. 反射波回到源端，再次反射

### 反弹图（Bounce Diagram）

反弹图跟踪脉冲在传输线上的往返过程：

| 时间区间 | $z=0$ 电压 | $z=l$ 电压 |
|----------|-----------|-----------|
| $0 < t < T$ | $V_1 = V_G \frac{Z_0}{Z_G+Z_0}$ | 0 |
| $T < t < 3T$ | $V_1 + \Gamma_G \Gamma_L V_1$ | $V_1(1+\Gamma_L)$ |
| $3T < t < 5T$ | 含二次反射 | 含二次反射 |

其中 $T = l/v_p$ 为单程时延。

**应用**: 时域反射计（TDR）利用脉冲反射定位传输线故障。

---

## 关键公式总结

| 概念 | 公式 | 物理含义 |
|------|------|---------|
| 传播常数 | $\gamma = \alpha + j\beta = \sqrt{(R+j\omega L)(G+j\omega C)}$ | 波沿线的衰减和相移 |
| 特性阻抗 | $Z_0 = \sqrt{(R+j\omega L)/(G+j\omega C)}$ | 行波电压/电流比 |
| 反射系数 | $\Gamma = (Z_L - Z_0)/(Z_L + Z_0)$ | 阻抗失配度量 |
| 输入阻抗 | $Z_{\text{in}} = Z_0 \frac{Z_L + j Z_0 \tan\beta l}{Z_0 + j Z_L \tan\beta l}$ | 沿线阻抗变换 |
| VSWR | $S = (1+|\Gamma|)/(1-|\Gamma|)$ | 驻波严重度 |
| $\lambda/4$ 变换 | $Z_{\text{in}} = Z_1^2/Z_L$, $Z_1 = \sqrt{Z_0 R_L}$ | 阻抗匹配 |
| Smith 圆图 | $\Gamma = (z-1)/(z+1)$, $z$ 归一化阻抗 | 图形化解传输线问题 |
| 低耗衰减 | $\alpha \approx \frac12(R/Z_0 + G Z_0)$ | 导体 + 介质损耗 |

## 量纲检查总表

| 公式 | 量纲 | 结果 |
|------|------|------|
| $\gamma = \sqrt{(R+j\omega L)(G+j\omega C)}$ | $\sqrt{\Omega/\text{m} \cdot \text{S}/\text{m}} = 1/\text{m}$ | ✅ |
| $Z_0 = \sqrt{(R+j\omega L)/(G+j\omega C)}$ | $\sqrt{\Omega/\text{m} / (\text{S}/\text{m})} = \sqrt{\Omega/\text{S}} = \Omega$ | ✅ |
| $\Gamma = (Z_L-Z_0)/(Z_L+Z_0)$ | $\Omega/\Omega$ = 无量纲 | ✅ |
| $\beta = \omega\sqrt{LC}$ | $\text{rad/s} \cdot \sqrt{\text{H/m}\cdot\text{F/m}} = \text{rad/m}$ | ✅ |
| $Z_{\text{in}} = Z_0 \frac{Z_L+jZ_0\tan(\beta l)}{Z_0+jZ_L\tan(\beta l)}$ | $\Omega \cdot \Omega/\Omega = \Omega$ | ✅ |
| $\alpha = \frac12(R/Z_0 + G Z_0)$ | $(\Omega/\text{m})/\Omega + \text{S/m} \cdot \Omega = 1/\text{m}$ | ✅ |

## 工程应用要点

1. **何时用传输线模型**：$D \gtrsim \lambda/10$ 时必须用分布参数
2. **Smith 圆图是微波工程师的"计算尺"**：图形化处理阻抗变换、匹配网络设计
3. **$\lambda/4$ 变换器**：最简单实用的窄带匹配网络
4. **回波损耗**：度量网络匹配质量的常用指标，RL > 20 dB 通常认为效果良好
5. **TDR（时域反射计）**：利用瞬态反射定位传输线故障、测量不连续性
6. **无畸变线**：在长距离通信中控制脉冲波形保真度
