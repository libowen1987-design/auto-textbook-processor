# Pozar Chapter 9 — Ferrite Components / 铁氧体器件
> **中英双语版**

> **范围**: §9.1–§9.6 | **核心主题**: 张量磁导率、旋磁效应、隔离器、环行器、移相器、YIG 振荡器
> **单位制**: SI (Pozar 全书一致)
> **量纲检查**: 每节标注 ✅ 通过 / ⚠️ 需验证

---

## 目录

1. [§9.1 铁氧体材料特性](#91-铁氧体材料特性)
2. [§9.2 法拉第旋转](#92-法拉第旋转)
3. [§9.3 隔离器](#93-隔离器)
4. [§9.4 环行器](#94-环行器)
5. [§9.5 移相器](#95-移相器)
6. [§9.6 YIG 器件](#96-yig-器件)

---

## §9.1 铁氧体材料特性

### 9.1.1 物理背景

铁氧体 (ferrite) 是铁磁绝缘体，化学式 $\text{MO\cdotFe}_2\text{O}_3$（M = Mn, Mg, Ni, Zn, Y 等）。
其关键特性：

| 特性 | 数值范围 | 说明 |
|------|----------|------|
| 相对介电常数 $\varepsilon_r$ | 5–25 | 无频率色散（微波段） |
| 损耗角正切 $\tan\delta$ | $10^{-4}$–$10^{-3}$ | 介质损耗极低 |
| 饱和磁化强度 $4\pi M_s$ | 300–5000 G (0.03–0.5 T) | 取决于材料 |
| 共振线宽 $\Delta H$ | 10–500 Oe | 决定损耗峰宽度 |
| 居里温度 $T_c$ | 100–600 ^\circC | 铁磁→顺磁转变 |

### 9.1.2 张量磁导率 (Polder Tensor)

外加直流偏置磁场 $\mathbf{H}_0 = H_0 \hat{z}$ 时，电子自旋发生进动，磁导率呈现各向异性。

**运动方程 (Landau-Lifshitz-Gilbert，无损耗):**

$$
\frac{d\mathbf{M}}{dt} = -\gamma (\mathbf{M} \times \mu_0 \mathbf{H})
$$

- $\gamma = 1.759 \times 10^{11} \ \text{C/kg}$：旋磁比 (gyromagnetic ratio)
- $\mathbf{M}$：磁化强度矢量
- $\mathbf{H}$：磁场强度

**量纲检查** ✅:
- $[$\gamma$] = \text{C/kg} = \text{A\cdots/kg}$，$[\mu_0 \mathbf{H}] = \text{T} = \text{kg/(A\cdots²)}$
- 右侧: $(\text{C/kg})(\text{A/m})(\text{kg/(A\cdots²)}) = (\text{A/(m\cdots)}) = [d\mathbf{M}/dt]$ ✅

**小信号近似**：总场 $\mathbf{H} = H_0 \hat{z} + \mathbf{h}(t)$，总磁化 $\mathbf{M} = M_s \hat{z} + \mathbf{m}(t)$，略去高阶项后得到：

**Polder 张量磁导率** ($\mathbf{b} = \bar{\bar{\mu}} \mathbf{h}$):

$$
\bar{\bar{\mu}} = \mu_0 \begin{bmatrix}
\mu & -j\kappa & 0 \\
j\kappa & \mu & 0 \\
0 & 0 & \mu_z
\end{bmatrix}
$$

其中：

$$
\boxed{\mu = 1 + \frac{\omega_0 \omega_m}{\omega_0^2 - $\omega$^2}}, \quad
\boxed{\kappa = \frac{\omega \omega_m}{\omega_0^2 - $\omega$^2}}, \quad
\mu_z = 1
$$

**定义参量**:

| 符号 | 表达式 | 物理含义 | SI 量纲 |
|------|--------|----------|---------|
| $\omega_0$ | $\gamma \mu_0 H_0$ | 共振角频率 (Larmor 频率) | rad/s ✅ |
| $\omega_m$ | $\gamma \mu_0 M_s$ | 磁化特征角频率 | rad/s ✅ |
| $\omega$ | — | 工作角频率 | rad/s ✅ |

**量纲检查** ✅:
- $\mu$ 无量纲: $[\omega_0 \omega_m / (\omega_0^2 - $\omega$^2)] = (\text{rad/s})^2 / (\text{rad/s})^2 = 1$
- $\kappa$ 无量纲: $[\omega \omega_m / (\omega_0^2 - $\omega$^2)] = (\text{rad/s})^2 / (\text{rad/s})^2 = 1$
- 张量元均为无量纲 ✅

**共振特性分析**:

1. **远离共振** ($\omega \ll \omega_0$): $\mu \approx 1 + \omega_m/\omega_0$ (静态磁导率), $\kappa \approx 0$
2. **接近共振** ($\omega \to \omega_0$): $$\mu$, \kappa \to \infty$ (无损耗模型)
3. **高频极限** ($\omega \gg \omega_0$): $\mu \to 1$, $\kappa \to 0$ (铁氧体透明)
4. **低场区** ($\omega \ll \omega_0$): 对于 $\omega_0 = 0$ (无偏置)，$\mu = 1$，各向同性

### 9.1.3 圆极化波本征模

对于沿 $z$ 方向传播的平面波，圆极化波的本征磁导率：

| 极化方向 | $\mu_{\text{eff}}$ | 传播特性 |
|----------|-------------------|----------|
| 右旋 (RHCP, $+$) | $\mu_+ = \mu + \kappa$ | 共振吸收大 |
| 左旋 (LHCP, $-$) | $\mu_- = \mu - \kappa$ | 共振吸收小 |

代入 $$\mu$, \kappa$ 表达式：

$$
\mu_+ = 1 + \frac{\omega_m}{\omega_0 - \omega}, \quad
\mu_- = 1 + \frac{\omega_m}{\omega_0 + \omega}
$$

**关键洞察**: 当 $\omega \to \omega_0$ 时 $\mu_+ \to \infty$（共振吸收）, 而 $\mu_-$ 有限。这就是**旋磁非互易性**的物理根源。

### 9.1.4 有损耗铁氧体

引入阻尼项 (Landau-Lifshitz-Gilbert 模型)：

$$
\frac{d\mathbf{M}}{dt} = -\gamma (\mathbf{M} \times \mu_0 \mathbf{H}) + \frac{\alpha}{M_s} \left(\mathbf{M} \times \frac{d\mathbf{M}}{dt}\right)
$$

其中 $\alpha$ 是阻尼系数。由此得复数张量磁导率：

$$
\mu = 1 + \frac{(\omega_0 + j$\alpha$$\omega$)\omega_m}{(\omega_0 + j$\alpha$$\omega$)^2 - $\omega$^2}
$$
$$
\kappa = \frac{\omega \omega_m}{(\omega_0 + j$\alpha$$\omega$)^2 - $\omega$^2}
$$

共振线宽 $\Delta H$ 与阻尼系数关系：

$$
\Delta H = \frac{2$\alpha$\omega}{$\gamma$\mu_0} \quad \text{或} \quad \alpha = \frac{$\gamma$\mu_0 \Delta H}{2\omega}
$$

工程上更常用 $\Delta H$ 表示损耗，典型值 10–500 Oe。

### 9.1.5 去磁效应 (Demagnetization)

对于非椭球形铁氧体样品，内部场不等于外加场：

$$
H_{\text{int}} = H_0 - N_z M_s
$$

其中 $N_z$ 是 $z$ 方向退磁因子（对无限长片沿平面偏置 $N_z=0$）。

---

## §9.2 法拉第旋转

### 9.2.1 物理机制

当线极化波沿偏置铁氧体中 $z$ 方向传播时，可分解为两个圆极化本征模 ($+$ 和 $-$)，其传播常数不同：

$$
\beta_\pm = \omega \sqrt{\mu_0 \varepsilon_0 \varepsilon_r \mu_\pm}
$$

传播 $z$ 距离后，两个模式的相位差产生极化面旋转：

**法拉第旋转角**:

$$
\boxed{\theta = \frac{\pi z}{\lambda_0} \left( \sqrt{\varepsilon_r \mu_+} - \sqrt{\varepsilon_r \mu_-} \right)
= \frac{\omega z}{2c} \left( \sqrt{\varepsilon_r \mu_+} - \sqrt{\varepsilon_r \mu_-} \right)}
$$

**量纲检查** ✅:
- $\omega z / c$: $(\text{rad/s})(\text{m})/(\text{m/s}) = \text{rad}$ ✅
- 右侧为无量纲角度 ✅

### 9.2.2 近似公式（小 $\kappa$ 近似）

当 $\kappa \ll \mu$（远离共振）：

$$
\sqrt{\mu_+} - \sqrt{\mu_-} \approx \frac{\kappa}{\sqrt{\mu}}
$$

因此：

$$
\theta \approx \frac{\omega z}{2c} \cdot \frac{\kappa}{\sqrt{\mu}} \sqrt{\varepsilon_r}
$$

### 9.2.3 非互易特性

法拉第旋转是**非互易**的：波来回传播时旋转角加倍（而非抵消）。

- 正方向 ($+z$): 旋转 $+\theta$
- 反方向 ($-z$): 旋转 $+\theta$（相对于传播方向，同一绝对方向）

因此往返总旋转 $2\theta$。对比互易旋光介质（如糖溶液），

| 特性 | 铁氧体 (法拉第) | 糖溶液 (自然旋光) |
|------|------------------|------------------|
| 物理机制 | 磁光效应 | 手性分子 |
| 时间反演对称性 | 破缺 | 保持 |
| 往返旋转 | $2\theta$ | 0（净抵消） |
| 非互易性 | ✅ 是 | ❌ 否 |

### 9.2.4 工程要点

- **旋磁比**在工程常用单位：$f_0(\text{GHz}) = 2.8 \times 10^{-3} H_0(\text{A/m}) = 0.0028 H_0(\text{Oe})$
- 或 $f_0 = 2.8 H_0$ MHz/Oe（$H_0$ 以 Oe 为单位）
- 典型 $H_0 = 1000$ Oe → $f_0 = 2.8$ GHz
- 法拉第旋转隔离器通常在 $\omega \ll \omega_0$ 工作（低场区）

---

## §9.3 隔离器

隔离器是二端口器件，正向低损耗、反向高损耗。Pozar 介绍三种类型：

### 9.3.1 共振隔离器 (Resonance Isolator)

**原理**: 在铁氧体共振频率 $\omega \approx \omega_0$ 处，一个圆极化分量的损耗远大于另一个。

**结构**: 偏置铁氧体片置于波导中磁场圆极化位置（TE$_{10}$ 模的 $h_x, h_z$ 存在 $\pm90^\circ$ 相位差处）。

**关键参数**:

| 参数 | 含义 | 典型值 |
|------|------|--------|
| $\omega = \omega_0$ | 共振条件 | — |
| $\Delta H$ | 铁氧体共振线宽 | 10–500 Oe |
| 反向损耗 | 隔度 | 20–30 dB |
| 正向损耗 | 插损 | 0.5–1 dB |
| 工作带宽 | $\sim 2\omega_0 ($\alpha$)$ | 约 10–20% |

**量纲检查** ✅: dB 是比值对数，无量纲。

**衰减常数** ($\omega = \omega_0$):

$$
\alpha_{\text{RHCP}} = \frac{\omega}{c} \sqrt{\varepsilon_r} \cdot \frac{$\mu$''_+}{2}
$$

其中 $$\mu$''_+$ 是 $\mu_+$ 的虚部。谐振时 $$\mu$''_+$ 达到峰值。

### 9.3.2 法拉第旋转隔离器 (Faraday Rotation Isolator)

**结构**:
1. 输入端: 矩形→圆波导过渡 + 电阻片（吸收 $y$ 极化）
2. 铁氧体段: 产生 $45^\circ$ 法拉第旋转
3. 输出端: 同样带电阻片的过渡

**工作模式**:
- 正向: 极化面旋转 $45^\circ$ → 匹配输出波导
- 反向: 输入波导到铁氧体再旋转 $45^\circ$，总 $90^\circ$ → 被电阻片吸收

**设计公式**:

$$
\theta = 45^\circ \Rightarrow z = \frac{$\pi$/4}{\frac{\pi}{\lambda_0} (\sqrt{\varepsilon_r\mu_+} - \sqrt{\varepsilon_r\mu_-})} = \frac{\lambda_0}{4(\sqrt{\varepsilon_r\mu_+} - \sqrt{\varepsilon_r\mu_-})}
$$

工程上常简化使用材料特定的法拉第旋转常数 $\theta_F$ (deg/cm 或 rad/m)。

### 9.3.3 场移隔离器 (Field Displacement Isolator)

**原理**: 利用铁氧体不同圆极化模式的场分布差异将场"推"向/远离吸收片。

- 一个方向传播时场被推向吸收片（高损耗）
- 另一方向传播时场远离吸收片（低损耗）

**优势**: 宽频带 (倍频程量级)，结构紧凑。

**典型性能**:

| 参数 | 典型值 |
|------|--------|
| 隔度 (反向损耗) | 20 dB |
| 插损 (正向损耗) | 1 dB |
| VSWR | 1.2:1 |
| 带宽 | 40–100% |

---

## §9.4 环行器

环行器是三端口器件，信号按固定方向循环（1→2→3→1）。

### 9.4.1 结式环行器 (Junction Circulator)

**结构**: Y 形波导节，中心放置铁氧体柱，外加垂直偏置磁场。

**工作原理**: 铁氧体柱中形成两个简并模（TM$_{110}$ 模的两种正交极化），偏置磁场破缺简并性，使场分布旋转，实现方向性传输。

**S 参数矩阵** (理想环行器):

$$
S = \begin{bmatrix}
0 & 0 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0
\end{bmatrix}
\quad \text{(顺时针: 1→2→3→1)}
$$

**设计条件** (Bosma 理论):

1. 铁氧体柱半径 $R$ 满足共振条件：
   $$
   kR = 1.84 \quad \text{(TM$_{110}$ 模)},\quad k = $\omega$\sqrt{\mu_0\varepsilon_0\varepsilon_f\mu_{\text{eff}}}
   $$
   其中 $\mu_{\text{eff}} = \mu - $\kappa$^2/\mu$ 是铁氧体的有效磁导率。

2. 归一化导纳匹配：
   $$
   G/Y_0 \approx 1,\quad B/Y_0 \approx 0
   $$

**量纲检查** ✅:
- $k$: $[$\omega$\sqrt{\mu_0\varepsilon_0}] = (\text{rad/s})\sqrt{(\text{H/m})(\text{F/m})} = \text{rad/m}$ ✅
- $kR$ 无量纲 ✅

**实用设计步骤**:

1. 根据工作频率 $f$ 选铁氧体材料（$M_s$ 足够高使 $\mu_{\text{eff}} > 0$）
2. 计算有效磁导率 $\mu_{\text{eff}} = \mu - $\kappa$^2/\mu$
3. 确定铁氧体柱半径 $R = 1.84/k$
4. 偏置场 $H_0$ 调到环行条件

**典型性能**:

| 参数 | 典型值 |
|------|--------|
| 插损 | 0.2–0.5 dB |
| 隔离度 | 20–30 dB |
| 带宽 | 10–40% |
| 功率容量 | 10 W–100 kW |

### 9.4.2 法拉第旋转环行器 (Faraday Rotation Circulator)

**结构**: 由两个 $45^\circ$ 法拉第旋转段和波导-同轴过渡组成四端口环行器。

**工作描述**:
- 端口1输入 → $45^\circ$ 旋转到端口2
- 端口2输入 → 另一个 $45^\circ$ 旋转到端口3
- 以此类推

### 9.4.3 差相移环行器 (Differential Phase Shift Circulator)

**结构**: 由两个 $3$ dB 混合波导耦合器 (Hybrid) 和两个非互易移相器组成四端口环行器。

**原理**: 两路信号经过非互易移相器产生 $\pm90^\circ$ 差相移，在输出端叠加后获得方向性。

---

## §9.5 移相器

移相器提供受控相位偏移，是相控阵天线关键组件。

### 9.5.1 Reggia-Spencer 移相器

**结构**: 矩形波导中放置纵向铁氧体棒，外加纵向偏置磁场（法拉第配置）。

**原理**: 纵向磁场改变铁氧体磁导率，从而改变传播常数 $\beta$。

**相移计算**:

对于矩形波导 TE$_{10}$ 模：

$$
\beta = \sqrt{$\omega$^2\mu_0\varepsilon_0\varepsilon_r\mu_{\text{eff}} - \left(\frac{\pi}{a}\right)^2}
$$

其中 $\mu_{\text{eff}}$ 取决于铁氧体的填充因子和偏置状态。

**差分相移**:

$$
$\Delta$\phi = (\beta_+ - \beta_-)L
$$

**量纲检查** ✅:
- $\beta$: $\text{rad/m}$，乘以长度 $L$ (m) 得 $\text{rad}$ ✅

### 9.5.2 Latching 移相器 (锁定式移相器)

**结构**: 矩形波导内放置铁氧体片，周围绕有导线圈形成磁回路。

**特点**:
- 用短电流脉冲改变磁化状态（非易失性）
- 断电后保持相移量（"锁定"）
- 相位精度取决于磁化水平

**相对相移**:

$$
$\Delta$\phi = \frac{k_0 L}{\cos\theta} \left( \frac{\kappa}{\mu} \right) \left( 1 - \frac{\tan^2\theta}{\mu} \right)^{-1/2}
$$

其中 $\theta$ 是波相对于偏置方向的传播角，$k_0 = $\omega$/c$。

**工程特性**:

| 参数 | 典型值 |
|------|--------|
| 相移/bits | 4–6 bit |
| 最大相移 | 360^\circ |
| 切换时间 | 1–10 $\mu$s |
| 插损 | 0.5–2 dB |
| 功率容量 | 1–100 W 平均 |

### 9.5.3 Rotary-Field 移相器 (旋转场移相器)

**原理**: 在圆波导或方圆过渡中，磁场偏置方向旋转，使波经历的磁导率周期性变化，产生连续相移。

**特点**: 可连续调相、大相移、高功率容量。

---

## §9.6 YIG 器件

YIG (Yttrium Iron Garnet, Y$_3$Fe$_5$O$_{12}$) 是低损耗铁氧体材料，共振线宽极小 ($\Delta H \sim 0.5$ Oe)。

### 9.6.1 YIG 材料特性

| 参数 | YIG 典型值 | 对比 (NiFe ferrite) |
|------|-----------|-------------------|
| $\varepsilon_r$ | 14–16 | 12 |
| $\Delta H$ | 0.3–1.0 Oe | 200–500 Oe |
| $4\pi M_s$ | 1750 G (0.139 T) | 3000–5000 G |
| $\tan\delta$ | $2\times10^{-4}$ | $1\times10^{-3}$ |
| $T_c$ | 280 ^\circC | 500 ^\circC |

### 9.6.2 YIG 调谐振荡器 (YIG-Tuned Oscillator, YTO)

**原理**: 利用 YIG 球的铁磁共振 (FMR) 作为谐振器，改变偏置磁场调谐频率。

**共振条件**:

$$
f_0 = $\gamma$\mu_0 H_{\text{eff}} = 2.80 \times 10^6 H_{\text{eff}} \ \text{Hz}
$$

其中 $H_{\text{eff}}$ 需考虑退磁场：

$$
H_{\text{eff}} = H_0 - \frac{4\pi}{3} M_s \quad (\text{球体}), \quad 4\pi M_s \ \text{in emu/cc}
$$

**实用调谐关系**:

$$
f_0(\text{GHz}) = 0.0028 H_0(\text{Oe}) \quad \text{(粗略估计; Kittel 公式见下)}
$$

**更精确的球体共振条件** (Kittel 公式):

$$
\omega_0 = $\gamma$\mu_0 \sqrt{H_0(H_0 + M_s)} \quad \text{(球体)}
$$

**量纲检查** ✅:
- $$\gamma$\mu_0 H_0$: $(\text{C/kg})(\text{H/m})(\text{A/m}) = (\text{C/kg})(\text{kg/C\cdots}) = 1/\text{s}$ ✅
- $f_0$ 单位为 Hz ✅

**YIG 谐振器无载 Q 值**:

$$
Q_u = \frac{f_0}{\Delta f} = \frac{\omega_0}{$\gamma$\mu_0 \Delta H} = \frac{H_0}{\Delta H}
$$

其中 $\Delta H$ 是共振线宽。对于 YIG 球 ($\Delta H \sim 0.5$ Oe, $H_0 \sim 3000$ Oe):
$Q_u \sim 6000$ (非常高!)

### 9.6.3 YIG 调谐滤波器

**结构**: YIG 球置于微带/带状线耦合环间，外磁场偏置。

**工作原理**: 仅当射频频率等于 YIG 球的铁磁共振频率时，信号从输入环耦合到输出环。

**性能特性**:

| 参数 | 典型值 |
|------|--------|
| 调谐范围 | 多倍频程 (0.5–40 GHz) |
| 瞬时带宽 (3-dB) | 5–50 MHz |
| 插入损耗 | 3–8 dB |
| 带外抑制 | > 60 dB |
| 调谐线性度 | 0.1–1% |
| 调谐速度 | 1–10 ms |

### 9.6.4 YIG 多级滤波器

多级 YIG 球级联以提高选择性：

| 级数 | 矩形系数 (60/3 dB) | 典型插损 |
|------|-------------------|----------|
| 1 | 8:1 | 3 dB |
| 2 | 4:1 | 5 dB |
| 3 | 3:1 | 7 dB |
| 4 | 2.5:1 | 9 dB |

### 9.6.5 YIG 相噪特性

YTO 的近载波相位噪声：

$$
\mathcal{L}(f_m) = \frac{1}{2} \left[ 1 + \left( \frac{f_0}{2Q_L f_m} \right)^2 \right] \frac{FkT}{P_0}
$$

其中 $f_m$ 是偏离载波频率，$Q_L$ 是有载 Q 值，$F$ 是放大器噪声系数。

---

## 总结: 铁氧体器件设计流程

```
┌─────────────────────────────────────────────────────┐
│ 1. 选材: f, Ms, \DeltaH, \varepsilonr (YIG → 窄带高Q, NiFe → 宽带)│
├─────────────────────────────────────────────────────┤
│ 2. 计算 \omega0 = $\gamma$\mu0H0, \omegam = $\gamma$\mu0Ms                     │
├─────────────────────────────────────────────────────┤
│ 3. 计算 $\mu$, \kappa (含损耗: 用复数 \omega0 + j$\alpha$$\omega$)             │
├─────────────────────────────────────────────────────┤
│ 4. 确定 $\mu$+, $\mu$- (圆极化本征模)                      │
├─────────────────────────────────────────────────────┤
│ 5. 器件特定设计:                                    │
│    • 隔离器: 放置于圆极化区, \omega \approx \omega0               │
│    • 环行器: Bosma 条件 kR = 1.84                  │
│    • 移相器: $\Delta$\beta 计算 + 填充因子                    │
│    • YIG: 球体 Kittel 公式                          │
├─────────────────────────────────────────────────────┤
│ 6. 验证: S参数, 隔离度, 插损, 带宽, 功率容量        │
└─────────────────────────────────────────────────────┘
```

---

## 量纲检查总表

| 公式 | 式号 | 量纲 | 状态 |
|------|------|------|------|
| $\mu = 1 + \frac{\omega_0\omega_m}{\omega_0^2-$\omega$^2}$ | 9.1 | 无量纲 | ✅ |
| $\kappa = \frac{$\omega$\omega_m}{\omega_0^2-$\omega$^2}$ | 9.2 | 无量纲 | ✅ |
| $\omega_0 = $\gamma$\mu_0 H_0$ | 9.3 | rad/s | ✅ |
| $\omega_m = $\gamma$\mu_0 M_s$ | 9.4 | rad/s | ✅ |
| $\theta = \frac{\omega z}{2c}(\sqrt{\varepsilon_r\mu_+} - \sqrt{\varepsilon_r\mu_-})$ | 9.5 | rad | ✅ |
| $\mu_{\text{eff}} = \mu - $\kappa$^2/\mu$ | 9.6 | 无量纲 | ✅ |
| $kR = 1.84$ | 9.7 | 无量纲 | ✅ |
| $f_0 = $\gamma$\mu_0 H_{\text{eff}}$ | 9.8 | Hz | ✅ |
| $Q_u = H_0/\Delta H$ | 9.9 | 无量纲 | ✅ |
| $\beta = \sqrt{$\omega$^2\mu_0\varepsilon_0\varepsilon_r\mu_{\text{eff}} - ($\pi$/a)^2}$ | 9.10 | rad/m | ✅ |

---

## 关键概念索引

| 概念 | 章节 | 重要性 |
|------|------|--------|
| Polder 张量 | §9.1 | ★★★ 基础 |
| 圆极化本征模 | §9.1 | ★★★ |
| 法拉第旋转 | §9.2 | ★★★ 核心效应 |
| 非互易性 | §9.2, §9.3 | ★★★ |
| 共振隔离器 | §9.3 | ★★ |
| 结式环行器 | §9.4 | ★★★ 最常见 |
| Bosma 条件 | §9.4 | ★★★ |
| Reggia-Spencer 移相器 | §9.5 | ★★ |
| YIG 调谐振荡器 | §9.6 | ★★ |
| Kittel 公式 | §9.6 | ★★★ |
