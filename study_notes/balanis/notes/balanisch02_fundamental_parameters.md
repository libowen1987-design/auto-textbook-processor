# Chapter 2: Fundamental Parameters of Antennas
# 第2章：天线基础参数
**Balanis — *Antenna Theory: Analysis and Design*, 4th Edition**

---

## 2.1 Introduction

天线的基本参数是描述和比较天线性能的定量指标。本章定义并讨论所有关键参数，这些参数贯穿全书。

> 核心思路：天线是一个 **过渡结构**（transition device），将导波（transmission line / waveguide）上的束缚电磁能量转换为自由空间中的辐射波。

---


### 2.2.1 定义

**Radiation Pattern**（辐射方向图）定义为天线辐射特性的空间分布数学函数或图形表示，通常用远场区域的条件描述。

方向图的分类：

| 类型 | 描述 | 数学形式 |
|------|------|----------|
| **Power Pattern**（功率方向图） | 辐射功率密度的空间分布 | \(U(\theta,\phi)\) |
| **Field Pattern**（场方向图） | 电场幅值的空间分布 | \(|E(\theta,\phi)|\) |
| **Normalized Pattern**（归一化方向图） | 相对于最大值的归一化 | \(F(\theta,\phi) = E(\theta,\phi)/E_{\max}\) |

归一化功率方向图：

\[
P_n(\theta,\phi) = \frac{U(\theta,\phi)}{U_{\max}} = |F(\theta,\phi)|^2
\]

### 2.2.2 方向图的关键区域

- **Main Lobe**（主瓣）— 包含最大辐射方向的波瓣
- **Side Lobes**（旁瓣）— 主瓣之外的波瓣
- **Back Lobe**（后瓣）— 与主瓣方向相反的波瓣
- **Nulls**（零点）— 辐射为零的方向

**SLL（Side Lobe Level）** 旁瓣电平：

\[
\text{SLL} = \frac{U_{\text{side}}}{U_{\max}} \quad \text{(通常用 dB 表示)}
\]

### 2.2.3 E-plane 和 H-plane Pattern

- **E-plane**：包含电场矢量方向和最大辐射方向的平面
- **H-plane**：包含磁场矢量方向和最大辐射方向的平面

对于线极化天线，E-plane 和 H-plane 是正交的。

---


### 2.3.1 Half-Power Beamwidth (HPBW)

**HPBW**（半功率波束宽度 / 3dB 波束宽度）：功率方向图下降到最大值一半（-3 dB）时两个方向之间的夹角。

\[
\text{HPBW} = \Theta_{3\text{dB}}
\]

物理意义：主瓣的"宽度"，决定了天线的角分辨率——HPBW 越小，方向性越强。

### 2.3.2 First Null Beamwidth (FNBW)

**FNBW**（第一零点波束宽度）：主瓣两侧第一个零点之间的夹角。

\[
\text{FNBW} = 2 \times \Theta_{\text{null}}
\]

对于均匀口径分布：\(\text{FNBW} \approx 2 \times \text{HPBW}\)

### 2.3.3 波束宽度与口径的关系

对于均匀激励的口径天线（近似）：

\[
\text{HPBW} \approx 0.886 \frac{\lambda}{L} \quad \text{(radians)}
\]

其中 \(L\) 为口径尺寸，\(\lambda\) 为自由空间波长。

---


### 2.4.1 定义

**方向性系数** \(D\) 定义为：在相同辐射功率下，给定方向的辐射强度与各向同性辐射强度之比。

\[
D(\theta,\phi) = \frac{U(\theta,\phi)}{U_0} = \frac{4\pi \, U(\theta,\phi)}{P_{\text{rad}}}
\]

通常关心的是 **最大方向性**：

\[
D_0 = D_{\max} = \frac{U_{\max}}{U_0} = \frac{4\pi \, U_{\max}}{P_{\text{rad}}}
\]

其中：
- \(U(\theta,\phi)\) — 辐射强度（单位立体角的功率，W/sr）
- \(U_0 = P_{\text{rad}} / 4\pi\) — 各向同性源的辐射强度
- \(P_{\text{rad}}\) — 总辐射功率

### 2.4.2 典型天线的方向性

| 天线类型 | \(D_0\) (线性) | \(D_0\) (dB) |
|----------|:-------------:|:------------:|
| 各向同性源 | 1 | 0 dBi |
| 短偶极子 (\(l \ll \lambda\)) | 1.5 | 1.76 dBi |
| \(\lambda/2\) 偶极子 | 1.643 | 2.15 dBi |
| 均匀面阵（大型） | \(4\pi A / \lambda^2\) | — |

### 2.4.3 Kraus 近似公式

Kraus 提出了用两个主平面 HPBW 估算方向性的近似公式：

\[
D_0 \approx \frac{4\pi}{\Theta_{1r} \, \Theta_{2r}} = \frac{41253}{\Theta_{1d} \, \Theta_{2d}}
\]

其中 \(\Theta_{1r}, \Theta_{2r}\) 为弧度制的 HPBW，\(\Theta_{1d}, \Theta_{2d}\) 为角度制。

> 注意：这个公式假设方向图是理想的"矩形"波束，实际方向性略低。仅适用于高方向性天线（HPBW < 100°）。

### 2.4.4 Tai & Pereira 精确公式

Tai & Pereira 给出了更精确的方向性计算：

\[
D_0 = \frac{4\pi}{\Omega_A}
\]

其中 **波束立体角**（Beam Solid Angle）：

\[
\Omega_A = \iint_{4\pi} P_n(\theta,\phi) \, d\Omega
\]

近似为：

\[
\Omega_A \approx \Theta_{1r} \, \Theta_{2r}
\]

### 2.4.5 口径方向性

对于平面口径天线，方向性与有效口径面积直接相关：

\[
D_0 = \frac{4\pi}{\lambda^2} A_{em}
\]

其中 \(A_{em}\) 为最大有效口径（maximum effective aperture）。

---


### 2.5.1 增益定义

**增益** \(G\) 定义为：在相同输入功率下，给定方向的辐射强度与各向同性辐射强度之比。

\[
G(\theta,\phi) = \frac{4\pi \, U(\theta,\phi)}{P_{\text{in}}}
\]

最大增益：

\[
G_0 = \frac{4\pi \, U_{\max}}{P_{\text{in}}}
\]

### 2.5.2 辐射效率

天线总效率 \(\epsilon_0\) 是三个效率因子的乘积：

\[
\epsilon_0 = \epsilon_r \, \epsilon_c \, \epsilon_d
\]

- \(\epsilon_r\) — 反射效率（阻抗失配）：\(\epsilon_r = 1 - |\Gamma|^2\)
- \(\epsilon_c\) — 导体效率（conduction efficiency）  
- \(\epsilon_d\) — 介质效率（dielectric efficiency）

常用表达式 **辐射效率**（radiation efficiency）：

\[
\epsilon_{\text{rad}} = \frac{P_{\text{rad}}}{P_{\text{in}}}
\]

### 2.5.3 增益与方向性的关系

\[
G_0 = \epsilon_{\text{rad}} \, D_0
\]

dB 表示：

\[
G_0 \, (\text{dBi}) = D_0 \, (\text{dB}) + 10\log_{10}(\epsilon_{\text{rad}})
\]

> 注意：**dBi** 表示相对于各向同性源的 dB 值。**dBd** 表示相对于半波偶极子的 dB 值。\(0 \, \text{dBd} = 2.15 \, \text{dBi}\)。

### 2.5.4 部分增益

\[
G_\theta = \epsilon_{\text{rad}} \, D_\theta, \quad G_\phi = \epsilon_{\text{rad}} \, D_\phi
\]

---


波束效率定义为主瓣辐射功率与总辐射功率之比：

\[
\eta_B = \frac{P_{\text{main lobe}}}{P_{\text{rad}}}
\]

\[
\eta_B = \frac{\iint_{\text{main lobe}} U(\theta,\phi) \, d\Omega}{\iint_{4\pi} U(\theta,\phi) \, d\Omega}
\]

**Stray Factor**（杂散因子）：\(\eta_{\text{stray}} = 1 - \eta_B\)

---


### 2.7.1 定义

**带宽**是指天线性能参数（方向图、阻抗、极化、增益等）保持在可接受范围内的频率范围。

### 2.7.2 带宽分类

| 带宽类型 | 描述 |
|----------|------|
| **Impedance Bandwidth**（阻抗带宽） | VSWR ≤ 2（或 S11 ≤ -10 dB）的频率范围 |
| **Pattern Bandwidth**（方向图带宽） | 方向图特性（HPBW、SLL）保持稳定的频率范围 |
| **Polarization Bandwidth**（极化带宽） | 极化特性（轴比等）保持稳定的频率范围 |

### 2.7.3 窄带 vs 宽带

\[
\text{BW} = \frac{f_{\max} - f_{\min}}{f_c} \times 100\%
\]

| 分类 | 百分比带宽 |
|------|:----------:|
| 窄带 | ≤ 5% |
| 宽带 | 5% – 25% |
| 超宽带 | ≥ 25% |

---


### 2.8.1 极化的定义

**极化** 描述了电磁波在空间固定点处电场矢量末端随时间变化的轨迹。

### 2.8.2 极化类型

| 类型 | 条件 | 特征 |
|------|------|------|
| **Linear Polarization**（线极化） | \(\delta = \delta_y - \delta_x = 0^\circ\) 或 \(180^\circ\) | 电场沿固定直线振荡 |
| **Circular Polarization**（圆极化） | \(E_x = E_y\), \(\delta = \pm 90^\circ\) | 电场矢量末端画圆 |
| **Elliptical Polarization**（椭圆极化） | 其他情况 | 电场矢量末端画椭圆 |

**RHCP**（Right-Hand Circular Polarization / 右旋圆极化）：沿传播方向看，电场顺时针旋转。

**LHCP**（Left-Hand Circular Polarization / 左旋圆极化）：沿传播方向看，电场逆时针旋转。

### 2.8.3 极化失配因子（Polarization Efficiency / Polarization Loss Factor, PLF）

\[
\text{PLF} = |\hat{\rho}_w \cdot \hat{\rho}_a|^2 = \cos^2(\psi_p)
\]

其中 \(\hat{\rho}_w\) 为入射波的极化单位矢量，\(\hat{\rho}_a\) 为接收天线的极化单位矢量，\(\psi_p\) 为两矢量之间的夹角。

- 线极化对齐：PLF = 1 (0 dB)
- 线极化垂直：PLF = 0 (−∞ dB)
- RHCP 接收 LHCP：PLF ≈ 0 (完全失配)

### 2.8.4 Axial Ratio（轴比，AR）

椭圆极化的轴比定义为极化椭圆的长轴与短轴之比：

\[
\text{AR} = \frac{OA}{OB} = \frac{\text{major axis}}{\text{minor axis}}, \quad 1 \leq \text{AR} \leq \infty
\]

- 圆极化：AR = 1 (0 dB)
- 线极化：AR = ∞

通常用 dB 表示：\(\text{AR}_{\text{dB}} = 20 \log_{10}(\text{AR})\)

---


### 2.9.1 定义

天线输入阻抗定义为天线输入端口的电压与电流之比：

\[
Z_{\text{in}} = R_{\text{in}} + jX_{\text{in}}
\]

其中：
- \(R_{\text{in}}\) — 输入电阻（包含辐射电阻和损耗电阻）
- \(X_{\text{in}}\) — 输入电抗（储存近场能量）

辐射电阻（Radiation Resistance）：

\[
R_r = \frac{2P_{\text{rad}}}{|I_{\text{in}}|^2}
\]

### 2.9.2 阻抗匹配

**VSWR**（电压驻波比）：

\[
\text{VSWR} = \frac{1 + |\Gamma|}{1 - |\Gamma|}
\]

**回波损耗**（Return Loss）：

\[
\text{RL} = -20\log_{10}|\Gamma| \quad (\text{dB})
\]

其中反射系数 \(\Gamma = \frac{Z_{\text{in}} - Z_0}{Z_{\text{in}} + Z_0}\)。

| VSWR | RL (dB) | 匹配质量 |
|:----:|:-------:|:--------:|
| 1.0 | −∞ | 完美匹配 |
| 1.5 | −14.0 | 良好 |
| 2.0 | −9.54 | 可接受（工程标准） |
| 3.0 | −6.02 | 较差 |

---


### 2.10.1 定义

**有效口径** \(A_e\) 定义为天线接收功率与入射功率密度之比：

\[
A_e = \frac{P_r}{W_i} \quad (\text{m}^2)
\]

其中 \(W_i\) 为入射波的功率密度（W/m²）。

### 2.10.2 有效口径与增益的关系

\[
G = \frac{4\pi A_e}{\lambda^2}
\]

最大有效口径与物理口径的关系：

\[
A_{em} = \epsilon_{ap} \, A_p
\]

其中 \(\epsilon_{ap}\) 为 **口径效率**（aperture efficiency），\(A_p\) 为物理口径面积。

### 2.10.3 典型天线的口径效率

- 均匀激励的喇叭天线：\(\epsilon_{ap} \approx 0.8\)（锥削）
- 抛物面天线：\(\epsilon_{ap} \approx 0.5\)–\(0.65\)
- 均匀线阵：\(\epsilon_{ap} \approx 1\)（无锥削时）

---


### 2.11.1 基本 Friis 方程

考虑收发天线在自由空间中的通信链路：

\[
\frac{P_r}{P_t} = G_t \, G_r \, \left(\frac{\lambda}{4\pi R}\right)^2
\]

其中：
- \(P_r\) — 接收功率（W）
- \(P_t\) — 发射功率（W）
- \(G_t\) — 发射天线增益（线性值）
- \(G_r\) — 接收天线增益（线性值）
- \(\lambda\) — 工作波长（m）
- \(R\) — 距离（m）

### 2.11.2 包含极化失配和阻抗失配

完整的 Friis 方程：

\[
\frac{P_r}{P_t} = \epsilon_t \, \epsilon_r \, G_t(\theta_t,\phi_t) \, G_r(\theta_r,\phi_r) \, \left(\frac{\lambda}{4\pi R}\right)^2 \, |\hat{\rho}_t \cdot \hat{\rho}_r|^2
\]

其中 \(\epsilon_t, \epsilon_r\) 为阻抗匹配效率，\(|\hat{\rho}_t \cdot \hat{\rho}_r|^2\) 为极化失配因子。

### 2.11.3 路径损耗

**Free Space Path Loss**（自由空间路径损耗）：

\[
\text{FSPL} = \left(\frac{4\pi R}{\lambda}\right)^2 = \left(\frac{4\pi f R}{c}\right)^2
\]

dB 形式：

\[
\text{FSPL}_{\text{dB}} = 20\log_{10}(R) + 20\log_{10}(f) + 20\log_{10}\left(\frac{4\pi}{c}\right)
\]

在常用单位下（R in km, f in MHz）：

\[
\text{FSPL}_{\text{dB}} = 32.45 + 20\log_{10}(R_{\text{km}}) + 20\log_{10}(f_{\text{MHz}})
\]

---


### 2.12.1 基本雷达方程

对于单站雷达（monostatic radar）：

\[
P_r = \frac{P_t \, G_t \, G_r \, \lambda^2 \, \sigma}{(4\pi)^3 R^4}
\]

其中 \(\sigma\) 为目标的 **RCS**（Radar Cross Section / 雷达散射截面，m²）。

### 2.12.2 最大探测距离

令 \(P_r = P_{r,\min}\)（最小可检测信号）：

\[
R_{\max} = \left[ \frac{P_t \, G_t \, G_r \, \lambda^2 \, \sigma}{(4\pi)^3 P_{r,\min}} \right]^{1/4}
\]

---


### 2.13.1 定义

天线噪声温度 \(T_A\) 描述了天线从周围环境接收到的噪声功率：

\[
T_A = \frac{1}{4\pi} \iint_{4\pi} T_B(\Omega) \, G(\Omega) \, d\Omega
\]

其中 \(T_B(\Omega)\) 为方向的 **亮温**（brightness temperature），\(G(\Omega)\) 为天线增益方向图。

### 2.13.2 典型亮温

| 源 | 亮温 |
|----|:----:|
| 宇宙微波背景 | 2.7 K |
| 晴天天空（天顶） | ~5–10 K |
| 晴天天空（低仰角） | ~50–100 K |
| 地面 | ~290 K |
| 太阳 | ~10⁴–10⁶ K |

### 2.13.3 系统噪声温度

天线系统总噪声温度：

\[
T_{\text{sys}} = T_A + T_{\text{feed}} + T_{\text{LNA}}
\]

---


| 参数 | 符号 | 核心公式 | 工程意义 |
|------|:----:|----------|----------|
| 方向性系数 | \(D_0\) | \(D_0 = 4\pi U_{\max}/P_{\text{rad}}\) | 辐射能量集中程度 |
| 增益 | \(G_0\) | \(G_0 = \epsilon_{\text{rad}} D_0\) | 包含效率的"实际方向性" |
| 辐射效率 | \(\epsilon_{\text{rad}}\) | \(\epsilon_{\text{rad}} = P_{\text{rad}}/P_{\text{in}}\) | 天线损耗度量 |
| 波束宽度 | HPBW | \(\approx 0.886\lambda/L\) | 角分辨率指标 |
| 有效口径 | \(A_e\) | \(A_e = \lambda^2 G / 4\pi\) | 接收能力度量 |
| 口径效率 | \(\epsilon_{ap}\) | \(\epsilon_{ap} = A_e/A_p\) | 口径利用率 |
| Friis 传输 | \(P_r/P_t\) | \(= G_t G_r (\lambda/4\pi R)^2\) | 链路预算基础 |
| 极化失配 | PLF | \(= \cos^2(\psi_p)\) | 极化对齐的重要性 |
| 噪声温度 | \(T_A\) | \(\propto \int T_B G \, d\Omega\) | 接收系统灵敏度 |

---


1. C. A. Balanis, *Antenna Theory: Analysis and Design*, 4th ed., Wiley, 2016, Ch. 2.
2. J. D. Kraus, *Antennas*, 2nd ed., McGraw-Hill, 1988.
3. C. T. Tai and C. S. Pereira, "An approximate formula for calculating the directivity of an antenna," *IEEE Trans. Antennas Propagat.*, vol. AP-24, no. 2, pp. 235–236, Mar. 1976.
