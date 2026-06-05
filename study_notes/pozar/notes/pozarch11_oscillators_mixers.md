# Pozar 微波工程 第11章 — 振荡器与混频器 (Oscillators and Mixers)
> **中英双语版**

> 对应：Pozar《Microwave Engineering》4th Edition, Chapter 11, §11.1–§11.6  
> 核心物理：有源器件的非线性特性 → 负阻/变频

---

## §11.1 振荡器基本原理 (Oscillator Fundamentals)

### 11.1.1 反馈模型

```ascii
         +--------+         +--------+
    +--->|  A($\omega$)  |-------->|  $\beta$($\omega$)  |---> V_out
    |    +--------+         +--------+
    |                                  |
    +----------------------------------+
```

**闭环传递函数：**

$$
\frac{V_o}{V_i} = \frac{A($\omega$)}{1 - A($\omega$)$\beta$($\omega$)}
\tag{11.1}
$$

- $A($\omega$)$：放大器开环增益（前向路径，无量纲）
- $$\beta$($\omega$)$：反馈网络传输函数（无量纲）
- $T($\omega$) \equiv $\beta$($\omega$) A($\omega$)$：**环路增益** (loop gain)

### 11.1.2 Barkhausen 起振条件

当分母为零时，系统自激振荡：

$$
1 - A(\omega_0)$\beta$(\omega_0) = 0 \quad\Rightarrow\quad T(\omega_0) = 1
\tag{11.2}
$$

拆分为幅值和相位条件：

$$
\boxed{|T(\omega_0)| = 1,\qquad \angle T(\omega_0) = 0^\circ\ (\text{或}\; 360^\circ)}
\tag{11.3}
$$

**量纲**：$|T|$ 无量纲；$\angle T$ 为度或弧度。

**物理直觉**：
- 幅值条件 $|T|=1$：信号绕环路一周后幅度不变
- 相位条件 $\angle T=0$：绕一周后相位相同（正反馈）
- 起振时需要 $|T| > 1$，稳定后自动降到 $|T| = 1$

### 11.1.3 起振瞬态

$$
V_o(t) = V_{o0}\, e^{\alpha t} \cos(\omega_0 t)
\tag{11.4}
$$

- $\alpha = \frac{1 - |T|}{\tau}$：增长率（$\tau$ 为环路时延）
- $|T| > 1 \Rightarrow \alpha < 0 \Rightarrow$ 幅度增长（起振）
- 非线性限制幅度 → 稳态 $|T| = 1$

### 11.1.4 振荡频率稳定度

$$
\frac{\Delta f}{f_0} = \frac{$\Delta$\phi}{Q}
\tag{11.5}
$$

- $$\Delta$\phi$：环路相移随温度/老化的漂移
- $Q$：谐振回路品质因数
- 高 $Q$ 谐振器 → 高频率稳定度

---

## §11.2 晶体管振荡器 (Transistor Oscillators)

### 11.2.1 二端口网络振荡条件

**反射系数视角**：

$$
\boxed{\Gamma_{\text{in}} \Gamma_S = 1,\qquad \Gamma_{\text{out}} \Gamma_L = 1}
\tag{11.6}
$$

- $\Gamma_{\text{in}} = S_{11} + \frac{S_{12}S_{21}\Gamma_L}{1 - S_{22}\Gamma_L}$（从端口1看入）
- $\Gamma_{\text{out}} = S_{22} + \frac{S_{12}S_{21}\Gamma_S}{1 - S_{11}\Gamma_S}$（从端口2看出）
- 满足 (11.6) 时，端口呈现 **负阻** 抵消外电路正阻

**量纲**：$\Gamma$ 均为无量纲复数。

### 11.2.2 负阻模型 (Negative Resistance Model)

一端口振荡器：

```ascii
      Active Device           Load
    +-------------+      +----------+
    |     Z_in    |------|   Z_L    |
    |  R_in+jX_in |      | R_L+jX_L |
    +-------------+      +----------+
```

**振荡条件**：

$$
\boxed{R_{\text{in}}(\omega_0) + R_L(\omega_0) = 0,\qquad 
X_{\text{in}}(\omega_0) + X_L(\omega_0) = 0}
\tag{11.7}
$$

- $R_{\text{in}} < 0$：有源器件贡献负阻（$|R_{\text{in}}| \equiv |R_n|$）
- $R_L > 0$：负载吸收功率

**起振条件**：

$$
|R_{\text{in}}| > R_L \quad\Rightarrow\quad |\Gamma_{\text{in}}| > 1/\Gamma_L
\tag{11.8}
$$

### 11.2.3 共基/共栅拓扑 (Common-Base/Common-Gate)

**共基 BJT 振荡器**：基极接地，发射极接谐振器 → 集电极输出
- 发射极看入阻抗 $Z_{\text{in}} = -\frac{g_m}{$\omega$^2 C_\pi}$（典型负阻）
- 振荡频率由 $LC$ 谐振器决定

**共栅 FET 振荡器**：栅极接地，源极接谐振器 → 漏极输出
- 源极看入阻抗 $Z_{\text{in}} = -\frac{1}{g_m}$（低频极限）
- 优势：宽带负阻特性

### 11.2.4 S 参数振荡器设计法

**步骤**：
1. 在目标 $f_0$ 附近使 $S_{11}$ 的反射幅度 $|S_{11}| > 1$（通过反馈网络实现）
2. 调整负载 $\Gamma_L$ 使 $\Gamma_{\text{in}}\Gamma_S = 1$
3. 谐振器选择使 $\angle(S_{11}\Gamma_S) = 0$

**实用设计方程**（共基 BJT）：

振荡条件：

$$
S_{11}\Gamma_T = 1
\tag{11.9}
$$

- $\Gamma_T$：调谐网络反射系数（谐振器 + 负载）
- $\Gamma_T = 1/\Gamma_{\text{in}}$

振荡裕度 (Oscillation Margin)：

$$
\text{OM} = 20\log_{10}\left(\frac{|\Gamma_T|}{|1/\Gamma_{\text{in}}|}\right)\ \text{dB}
\tag{11.10}
$$

**量纲**：$\Gamma$ 无量纲，OM 为 dB。

### 11.2.5 频率调谐

振荡器频率变化的小信号近似：

$$
$\Delta$\omega \approx -\frac{\Delta B}{\partial B/\partial\omega}\Big|_{\omega_0}
\tag{11.11}
$$

- $B$：谐振器电纳
- $\partial B/\partial\omega$ 越大 → 频率牵引越小 → 稳定性越高

---

## §11.3 介质谐振振荡器 DRO (Dielectric Resonator Oscillators)

### 11.3.1 介质谐振器 (DR) 基本参数

**谐振频率**：TE$_{01\delta}$ 模

$$
f_0 = \frac{c}{2\pi a\sqrt{\varepsilon_r}} \frac{1}{\sqrt{1 + (a/h)^2}}
\quad\text{(近似)}
\tag{11.12}
$$

- $a$：DR 半径，$h$：DR 高度
- $\varepsilon_r$：相对介电常数（典型 30–100）
- $c = 2.998 \times 10^8$ m/s：光速
- 精确解需查表或全波仿真

**量纲**：$a,\ h$ 为 m，$f_0$ 为 Hz。

**无载 Q 值**：

$$
Q_0 \approx \frac{\varepsilon_r''}{\varepsilon_r'}\quad(\text{介质损耗主导})
\tag{11.13}
$$

- 典型值：$Q_0 = 5000\text{–}10000$（$\varepsilon_r \approx 38$ 时）
- 极高 Q → 极低相位噪声

### 11.3.2 DRO 拓扑

```ascii
         +------DC Bias------+
         |                   |
    [Resonator] --耦合-- [Transistor] --> RF Out
         |                   |
       Ground           匹配网络
```

- DR 耦合到微带线，作为高 Q 谐振元件
- DR 与微带线间距控制耦合系数 $\beta$
- 可调谐：DR 上方加金属螺钉 → 压电调谐

### 11.3.3 DRO 相位噪声

Leeson 模型：

$$
\mathcal{L}(\Delta f) = \frac{FkT}{P_0} \left[1 + \left(\frac{f_0}{2Q_L\Delta f}\right)^2\right]
\tag{11.14}
$$

- $\mathcal{L}(\Delta f)$：单边带相位噪声谱密度（dBc/Hz）
- $F$：晶体管噪声系数
- $k = 1.381 \times 10^{-23}$ J/K：玻尔兹曼常数
- $T$：绝对温度（K）
- $P_0$：输出功率（W）
- $Q_L$：有载 Q 值
- $\Delta f$：偏离载频的频率偏移（Hz）

**物理直觉**：
- $Q_L$ 加倍 → 相位噪声降低 6 dB
- 近载频 ($\Delta f \ll f_0/2Q_L$) 噪声按 $1/(\Delta f)^2$ 滚降
- 远载频噪声趋近于 $FkT/P_0$ 本底

---

## §11.4 压控振荡器 VCO (Voltage-Controlled Oscillators)

### 11.4.1 基本概念

**调谐特性**：

$$
f_{\text{osc}} = f_0 + K_{\text{VCO}}\, V_{\text{tune}}
\tag{11.15}
$$

- $K_{\text{VCO}}$：压控灵敏度（MHz/V）
- $V_{\text{tune}}$：调谐电压（V）
- 实际中 $K_{\text{VCO}}$ 非常量，存在非线性

**调谐带宽**：

$$
\text{Tuning BW} = f_{\max} - f_{\min}
\tag{11.16}
$$

### 11.4.2 变容二极管 (Varactor Diode)

**变容管 C-V 特性**：

$$
C_j(V) = \frac{C_{j0}}{(1 + V/V_j)^n}
\tag{11.17}
$$

- $C_{j0}$：零偏结电容（F）
- $V_j$：内建势（V，Si ~0.7V，GaAs ~0.8V）
- $n$：变容指数（突变结 $n=0.5$，超突变结 $n=0.5\text{–}2$）

**量纲**：$C_j$ 为 F，$V$ 为 V。

**质量因子**：

$$
Q_{\text{var}} = \frac{1}{\omega R_s C_j}
\tag{11.18}
$$

- $R_s$：串联电阻（$\Omega$），$\omega$：角频率（rad/s）

### 11.4.3 VCO 相位噪声

DRO 的 Leeson 模型同样适用于 VCO，但 $Q_L$ 通常更低：

$$
\mathcal{L}_{\text{VCO}}(\Delta f) \approx \frac{FkT}{P_0} \frac{f_0^2}{4Q_L^2 (\Delta f)^2}
\quad (\Delta f \ll f_0/2Q_L)
\tag{11.19}
$$

- VCO 的 $Q_L$ 通常低于 DRO → 噪声更高
- **推振 (Pushing)**: 电源电压变化导致的频率漂移 (MHz/V)
- **牵引 (Pulling)**: 负载阻抗变化导致的频率漂移

---

## §11.5 混频器基本原理 (Mixer Fundamentals)

### 11.5.1 非线性器件与混频原理

理想非线性 I-V 特性（泰勒展开）：

$$
i(v) = I_0 + v\frac{di}{dv}\Big|_0 + \frac{v^2}{2!}\frac{d^2i}{dv^2}\Big|_0 + \frac{v^3}{3!}\frac{d^3i}{dv^3}\Big|_0 + \cdots
\tag{11.20}
$$

令 $v = V_{\text{RF}}\cos\omega_{\text{RF}}t + V_{\text{LO}}\cos\omega_{\text{LO}}t$，则二阶项产生：

$$
v^2 \propto \cos^2(\omega_{\text{RF}}t) + \cos^2(\omega_{\text{LO}}t) + 2\cos(\omega_{\text{RF}}t)\cos(\omega_{\text{LO}}t)
$$

使用三角恒等式：

$$
2\cos A\cos B = \cos(A-B) + \cos(A+B)
$$

得到输出频率：

$$
f_{\text{IF}} = |f_{\text{RF}} \pm f_{\text{LO}}|
\tag{11.21}
$$

- 下变频 (Down-conversion)：$f_{\text{IF}} = |f_{\text{RF}} - f_{\text{LO}}|$
- 上变频 (Up-conversion)：$f_{\text{IF}} = f_{\text{RF}} + f_{\text{LO}}$

### 11.5.2 变频增益/损耗 (Conversion Gain/Loss)

**定义**：

$$
G_c = \frac{P_{\text{IF}}}{P_{\text{RF}}}
\tag{11.22}
$$

- $G_c > 1$：变频增益（有源混频器）
- $G_c < 1$：变频损耗（无源混频器）
- 典型无源二极管混频器 $G_c \approx -6$ dB

**量纲**：$G_c$ 无量纲，常以 dB 表示。

### 11.5.3 交调失真 (Intermodulation Distortion, IMD)

考虑三阶非线性项 $v^3$，当两个强干扰信号 $f_1, f_2$ 靠近 $f_{\text{RF}}$ 时，产生三阶交调产物：

$$
f_{\text{IM3}} = 2f_1 - f_2 \quad\text{和}\quad 2f_2 - f_1
\tag{11.23}
$$

若 $f_{\text{RF}}$ 有干扰在 $f_{\text{RF}}+\Delta f$ 和 $f_{\text{RF}}+2\Delta f$，则交调产物落在 $f_{\text{RF}}$ 带内：

$$
f_{\text{IM3}} = (f_{\text{RF}}+\Delta f) + \Delta f = f_{\text{RF}} - \Delta f
\quad\text{与}\quad f_{\text{RF}} + 2\Delta f - \Delta f = f_{\text{RF}} + \Delta f
$$

**物理**：IM3 产物落在 $f_{\text{RF}} \pm \Delta f$，无法用滤波去除。

### 11.5.4 三阶截点 IP3 (Third-Order Intercept Point)

**定义**：基波输出功率与 IM3 输出功率外推相等的点。

```ascii
    P_out (dBm)
        ↑   \
        |    \  fundamental (斜率=1)
        |     \
    OIP3-----\times------\ 
        |     |\      \ IM3 (斜率=3)
        |     | \      \
        |     |  \      \
        +-----+---+------→ P_in (dBm)
              IIP3
```

**关键参数**：
- **IIP3** (Input IP3)：输入参考三阶截点 (dBm)
- **OIP3** (Output IP3)：输出参考三阶截点 (dBm)

$$
\text{OIP3} = \text{IIP3} + G_c
\tag{11.24}
$$

**量纲**：IP3 为 dBm。

**IM3 功率计算**：

$$
P_{\text{IM3}} = 3P_{\text{in}} - 2\,\text{IIP3} + G_c\quad (\text{dBm})
\tag{11.25}
$$

或等效：

$$
P_{\text{IM3}} = 3P_{\text{out}} - 2\,\text{OIP3}\quad (\text{dBm})
\tag{11.26}
$$

**无杂散动态范围 (SFDR)**：

$$
\text{SFDR} = \frac{2}{3}(\text{IIP3} - \text{N}_{\text{floor}})
\tag{11.27}
$$

- $\text{N}_{\text{floor}} = kTB + \text{NF}$：噪声本底 (dBm)
- 单位：dB

### 11.5.5 噪声系数 (Noise Figure)

**SSB 噪声系数**：

$$
\text{NF}_{\text{SSB}} = \frac{\text{总输出噪声}}{\text{信号源噪声经变频增益放大}}
\tag{11.28}
$$

- 镜像噪声贡献使 NF$_{\text{DSB}} = \text{NF}_{\text{SSB}} - 3$ dB（双边带比单边带少3 dB）

---

## §11.6 混频器设计与拓扑 (Mixer Design)

### 11.6.1 单端二极管混频器 (Single-Ended Diode Mixer)

**拓扑**：

```ascii
    RF Port ---||---+---+---||-- IF Port
                    |   |
                   LO --+-- DC Return
                  Coupler
```

- 肖特基二极管作为非线性元件
- $$\lambda$/4$ 开路线提供 RF 短路、IF 开路
- 输入匹配网络对 RF 和 LO 频率优化

**二极管 I-V**：

$$
I(V) = I_s(e^{\alpha V} - 1),\quad \alpha = \frac{q}{nkT}
\tag{11.29}
$$

- $I_s$：饱和电流 (A)，$q = 1.602 \times 10^{-19}$ C（电子电荷）
- $n$：理想因子 (1.05–1.25)
- $k = 1.381 \times 10^{-23}$ J/K, $T$：温度 (K)

**电导**：

$$
g(t) = \frac{dI}{dV} = \alpha I_s e^{\alpha V_{\text{LO}}\cos\omega_{\text{LO}}t}
\tag{11.30}
$$

### 11.6.2 平衡混频器 (Balanced Mixer)

**90^\circ 混合耦合器型**：

```ascii
    RF → 90^\circ Hybrid → Diode1 → IF+ (同相)
    LO → 90^\circ Hybrid → Diode2 → IF- (反相组合)
```

- RF 和 LO 端口隔离 (20–30 dB)
- AM 噪声抑制
- 输入驻波比改善

**180^\circ 混合耦合器型 (Rat-Race)**：

- RF 和 LO 从和/差端口馈入
- 抵消 LO 噪声

### 11.6.3 FET 混频器

**栅极混频**：RF 和 LO 共同施加于栅极
- 利用 FET 的 $g_m$ 非线性
- 变频增益 $G_c > 0$ dB

**漏极混频**：RF 加于栅极，LO 加于漏极
- 利用 $I_{ds}$-$V_{ds}$ 非线性
- LO-RF 隔离较好

**阻性 FET 混频器** (Resistive FET Mixer)：
- FET 工作在线性区（$V_{ds} \approx 0$）
- 沟道电阻被 LO 调制
- 极低噪声、高线性度
- 变频损耗 ~4–6 dB

### 11.6.4 镜像抑制混频器 (Image-Reject Mixer)

Hartley 结构：

```ascii
    RF → 90^\circHybrid → I通道混频器 → 90^\circ移相 → 合路 → IF_out
                  ↘ Q通道混频器 → 0^\circ移相 → 合路 → 镜像被抵消
```

- 镜像信号在两个通道反相抵消
- 镜像抑制比 20–40 dB
- 需要精确的 90^\circ 移相器和幅度匹配

---

## 关键公式总结表

| 公式 | 含义 | 量纲 | 关键编号 |
|------|------|------|---------|
| $T($\omega$) = $\beta$($\omega$)A($\omega$)$ | 环路增益 | 无量纲 | (11.1) |
| $1 - T(\omega_0) = 0$ | Barkhausen 判据 | 无量纲 | (11.2) |
| $\Gamma_{\text{in}}\Gamma_S = 1$ | 两端口振荡条件 | 无量纲 | (11.6) |
| $R_{\text{in}}+R_L=0, X_{\text{in}}+X_L=0$ | 负阻振荡条件 | Ω | (11.7) |
| $C_j(V) = C_{j0}/(1+V/V_j)^n$ | 变容管特性 | F | (11.17) |
| $G_c = P_{\text{IF}}/P_{\text{RF}}$ | 变频增益/损耗 | 无量纲 | (11.22) |
| $P_{\text{IM3}} = 3P_{\text{out}} - 2\text{IIP3}$ | 三阶交调功率 | dBm | (11.25) |
| $\mathcal{L}(\Delta f) = \frac{FkT}{P_0}[1+(\frac{f_0}{2Q_L\Delta f})^2]$ | 相位噪声 (Leeson) | dBc/Hz | (11.14) |

---

## 物理直觉速查

1. **振荡器** = 放大器 + 正反馈网络 + 非线性限幅
2. **负阻** = 有源器件向外部电路"输送"功率（$R_{\text{in}} < 0$）
3. **Barkhausen 条件** $|T|>1$ 启振，$|T|=1$ 稳幅
4. **DRO** 的高 Q 值 (5000–10000) 带来极低相位噪声
5. **VCO** 调谐用变容二极管，$K_{\text{VCO}}$ 决定调谐灵敏度
6. **混频器** 靠非线性产生和频/差频
7. **IP3** 越高 → 线性度越好 → 交调失真越小
8. **SFDR** 衡量混频器能处理无失真信号的上限范围
9. **平衡结构** 抑制 AM 噪声、改善隔离
