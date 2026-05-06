# Hemming《Electromagnetic Anechoic Chambers》
Leland H. Hemming  
IEEE Press, 2002

> **⚠️ OCR 说明 (IMPORTANT):** 本笔记基于 tesseract OCR 识别扫描页面后洗稿整理。由于扫描质量及 OCR 识别率限制，笔记中可能存在错误，请以原书为准。

---

## 目录 | Table of Contents

| 章 | 标题 | OCR页 |
|----|------|-------|
| 1 | Introduction | p.17 |
| 2 | Measurement Principles Pertaining to Anechoic Chamber Design | p.19 |
| 3 | Electromagnetic Absorbing Materials | p.42 |
| 4 | The Chamber Enclosure (Shielding) | p.64 |
| 5 | Anechoic Chamber Design Techniques | p.72 |
| 6 | The Rectangular Anechoic Chamber | p.88 |
| 7 | The Compact Range Chamber | p.112 |
| 8 | Shaped Chambers | p.124 |
| 9 | Electromagnetic Test Procedures | p.152 |
| 10 | Examples of Indoor Electromagnetic Test Facilities | p.174 |

---

## 第 1 章：Introduction | 引言
**Source:** Hemming, Chapter 1, OCR pages 17-18

### 1.1 文本结构 | Text Organization

**本教材的编写目的：**
为电磁吸波暗室的设计者和采购方提供单一、完整的实用信息来源，涵盖从基础到规格的全方位指导。

**内容覆盖范围：**
- 吸波暗室的基本设计原理
- 各种吸波材料的特性与应用
- 天线测试、RCS（雷达散射截面）测试、EMC测试等多种测试设施
- 设计/采购检查清单

**吸波暗室的工程价值：**
在航空航天领域，对导弹、飞机等武器平台的雷达散射截面进行测试时，吸波暗室提供了可控的室内测试环境，避免了户外测试受天气和电磁干扰的影响。

> **物理直觉：** 理想的吸波暗室应模拟"自由空间（free space）"——无反射、无多径干涉。一个设计良好的暗室，可以让待测天线"以为"自己在无限大的真空中工作。

---

## 第 2 章：Measurement Principles Pertaining to Anechoic Chamber Design
**Source:** Hemming, Chapter 2, OCR pages 19-41

### 2.1 引言 | Introduction

**Maxwell 方程组：**
宏观电磁现象由 Maxwell 方程组描述：

$$\nabla \cdot \mathbf{D} = \rho_v, \quad \nabla \cdot \mathbf{B} = 0$$
$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}, \quad \nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}$$

**本构关系（Constitutive Relationships）：**
$$\mathbf{D} = \varepsilon \mathbf{E}, \quad \mathbf{B} = \mu \mathbf{H}, \quad \mathbf{J} = \sigma \mathbf{E}$$

其中 $\varepsilon$ 为介电常数，$\mu$ 为磁导率，$\sigma$ 为电导率。

### 2.2 电磁场测量 | Measurement of Electromagnetic Fields

#### 2.2.1 平面波近似 | Plane Wave Approximation

在离开天线足够远的区域（远场，far-field），球面波可近似为平面波：

$$E(r) \approx E_0 \frac{e^{-jkr}}{r}, \quad r \gg \frac{2D^2}{\lambda}$$

其中 $D$ 是天线最大尺寸，$\lambda$ 是波长。

**远场条件的重要性：** 在远场区，电场 $\mathbf{E}$ 和磁场 $\mathbf{H}$ 相互垂直，且都垂直于传播方向，形成特征阻抗 $\eta_0 \approx 377\ \Omega$ 的横电磁波（TEM）。

#### 2.2.2 天线 | Antennas

**天线阻抗（Antenna Impedance）：**
天线的输入阻抗 $Z_{\text{in}} = R_{\text{rad}} + R_{\text{loss}} + jX$ 受到周边物理环境的强烈影响。当周围有反射物体时，反射波重新进入天线，改变了天线的视在阻抗。

> **物理意义：** 这就是为什么在天线测量中，环境中的任何金属物体（墙壁、支架、甚至人）都会影响测量结果——它们改变了天线的真实阻抗，从而改变了匹配状态和辐射效率。

#### 2.2.3 辐射发射 | Radiated Emissions

测量来自电子设备的辐射发射时，需要确保测量天线能够正确接收来自待测设备（DUT）的辐射，而不受暗室墙壁残余反射的影响。

#### 2.2.4 辐射敏感性 | Radiated Susceptibility

将待测设备暴露于已知强度和极化的电磁场中，评估其在特定电磁环境下的正常工作能力。

#### 2.2.5 军用电磁兼容性 | Military EMC

军用辐射电磁测量在屏蔽吸波暗室中进行，测试程序和吸波处理按 **MIL-STD-461E** 执行。

#### 2.2.6 天线系统隔离度 | Antenna System Isolation

天线隔离度测量要求极低的外部电磁信号环境，通常需要 < -100 dB 的隔离度。

### 2.3 自由空间测试要求 | Free-Space Test Requirements

**理想自由空间测试场条件：**
1. **幅度均匀性（Amplitude Uniformity）：** AUT（待测天线）照射区域内场强变化 < 1 dB
2. **相位均匀性（Phase Uniformity）：** 照射区域内相位变化 < 几个度
3. **平面度（Planarity）：** 入射波近似为理想平面波
4. **极化纯度（Polarization Purity）：** 主极化与交叉极化比 > 20 dB

#### 2.3.2 相位要求 | Phase Requirements

**相位均匀性条件（式2-6）：**
$$kD < \frac{\pi}{4} \quad \Leftrightarrow \quad D < \frac{\lambda}{8}$$

其中 $k = 2\pi/\lambda$ 是波数，$D$ 是照射区域直径。

**路径长度差（Path Length Difference）：**
球面波与理想平面波之间的路径差 $\delta$ 导致相位差：
$$\delta = R - \sqrt{R^2 + (D/2)^2} \approx -\frac{(D/2)^2}{2R}$$

当路径差 $\delta < \lambda/16$ 时，相位近似满足均匀性要求。

#### 2.3.3 幅度要求 | Amplitude Requirements

**幅度均匀性条件：**
$$K = \frac{2R}{\lambda} \geq 2 \sim 10$$

$K$ 值的选择取决于待测目标特性——边缘散射较强的目标需要更大的 $K$ 值（更大的距离或更小的照射区）。

> **经验法则：** 对于大多数天线测量，将幅度变化控制在 1 dB 以内通常可接受。

#### 2.3.4 极化 | Polarization

在远离辐射天线的区域，电场 $\mathbf{E}$ 和磁场 $\mathbf{H}$ 相互垂直，且都垂直于传播方向。

**轴比（Axial Ratio）：**
$$AR = \frac{|E_{\text{max}}|}{|E_{\text{min}}|} \geq 1$$

纯圆极化时 $AR = 1$；线极化时 $AR \to \infty$。

### 2.4 支持性测量概念 | Supporting Measurement Concepts

#### 2.4.3 分贝（Decibel）回顾

**基本定义：**
$$L_{\text{dB}} = 10 \log_{10} \frac{P_2}{P_1} = 20 \log_{10} \frac{V_2}{V_1}$$

**常用换算：**
| 分贝变化 | 功率比 | 电压/电流比 |
|---------|--------|------------|
| +3 dB | 2× | 1.414× |
| -3 dB | 0.5× | 0.707× |
| +10 dB | 10× | 3.162× |
| -20 dB | 0.01× | 0.1× |

#### 2.4.4 反射能量效应 | Effects of Reflected Energy

**反射系数（Reflection Coefficient）：**
$$\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0}$$

**电压驻波比（VSWR）：**
$$VSWR = \frac{1 + |\Gamma|}{1 - |\Gamma|}$$

> **物理意义：** 暗室吸波材料的作用是将入射电磁能量转化为热能，从而将反射系数降低到可接受水平（通常 < -30 dB）。

#### 2.4.5 天线耦合 | Antenna Coupling

**弗里斯传输公式（Friis Transmission Equation）：**
$$P_r = P_t G_t G_r \left(\frac{\lambda}{4\pi R}\right)^2 |\hat{\rho}_t \cdot \hat{\rho}_r|^2$$

其中 $G_t, G_r$ 为发射/接收天线增益，$\hat{\rho}_t, \hat{\rho}_r$ 为极化单位矢量。

**天线隔离度（Isolation）：**
$$I = 10 \log\frac{P_t}{P_r} = -10 \log\left[G_t G_r \left(\frac{\lambda}{4\pi R}\right)^2\right] \text{ dB}$$

在暗室设计中，高天线隔离度意味着待测天线和测量天线之间的耦合最小，测量结果更准确。

### 2.5 户外测试设施 | Outdoor Measurement Facilities

| 设施类型 | 优点 | 缺点 |
|---------|------|------|
| 开放测试场（OATS）| 接近真实自由空间 | 受天气、环境干扰 |
| 屏蔽暗室 | 受控环境，可全天候 | 需要吸波处理 |
| 紧凑距离（Compact Range）| 大型AUT，静态平面波 | 造价高，忌口区限制 |

---

## 第 3 章：Electromagnetic Absorbing Materials
**Source:** Hemming, Chapter 3, OCR pages 42-63

### 3.1 引言 | Introduction

电磁吸波材料是暗室设计的核心。材料的吸波性能直接决定了暗室能否模拟"自由空间"。

**吸波材料的基本类型：**

| 类型 | 原理 | 适用频段 |
|------|------|---------|
| **介质损耗型（Dielectric）** | 通过电导率 $\sigma$ 损耗电磁能 | 低频 |
| **磁损耗型（Magnetic）** | 通过磁导率 $\mu$ 损耗电磁能 | 中频 |
| **锥形吸收器（Tapered）** | 阻抗渐变，减小反射 | 宽频带 |
| **频率选择表面（FSS）** | 谐振型吸收 | 特定频点 |

### 3.2 吸波机理 | Absorption Mechanism

**复介电常数表示：**
$$\varepsilon_r = \varepsilon_r' - j\varepsilon_r''$$

其中 $\varepsilon_r'$ 存储电场能量，$\varepsilon_r''$ 造成介电损耗。

**复磁导率：**
$$\mu_r = \mu_r' - j\mu_r''$$

**功率损耗密度：**
$$p_{\text{loss}} = \frac{1}{2}\sigma |E|^2 + \frac{1}{2}\omega \varepsilon_r'' |E|^2 + \frac{1}{2}\omega \mu_r'' |H|^2$$

### 3.3 尖劈吸收器 | Wedge Absorber

**设计原理：**
尖劈形状提供从空气阻抗（$377\ \Omega$）到材料阻抗的**渐变过渡**，使入射波在尖劈内部经历多次反射和损耗，最终大部分能量被转化为热能。

**性能指标：**
- 反射率（Reflectivity）：$R = 20\log|\Gamma|$（通常 <-30 dB）
- 最低工作频率：与尖劈长度相关，$\lambda_{\text{min}} \approx L/4$

> **物理直觉：** 想象把一块光滑的金属板换成一把"金属刷"——尖劈的多孔结构让电磁波难以原路反射回去，而是反复"钻进"材料深处被消耗掉。

### 3.4 薄膜吸收器 | Thin Absorber / Jaumann Absorber

由多层介质和导电膜交替组成，通过多层干涉效应实现吸收。

** Salisbury 屏：**
在导电基板上放置 $\lambda/4$ 厚度的介质层，前表面反射与基板反射相干相消。

**Dallenbach 层：**
阻抗匹配层直接附着在金属基板上，通过整体厚度设计实现宽频带吸收。

---

## 第 4 章：The Chamber Enclosure (Shielding)
**Source:** Hemming, Chapter 4, OCR pages 64-71

### 4.1 引言 | Introduction

**屏蔽的双重功能：**
1. **防止干扰（Interference Prevention）：** 阻止外部电磁干扰进入暗室
2. **防止电子窃听（Electronic Eavesdropping Prevention）：** 阻止暗室内测试信号泄漏

### 4.2 屏蔽效能 | Shielding Effectiveness

屏蔽效能（SE）以分贝（dB）为单位：

$$SE = 20 \log\frac{E_{\text{outside}}}{E_{\text{inside}}} \quad \text{[dB]}$$

典型屏蔽效能要求：

| 频段 | 屏蔽效能要求 |
|------|------------|
| 14 kHz - 1 MHz | 60 - 80 dB |
| 1 MHz - 1 GHz | 80 - 100 dB |
| 1 - 10 GHz | > 100 dB |

### 4.3 屏蔽材料与接缝 | Shielding Materials and Seams

**实心屏蔽板（Solid Shield）：** 连续金属板提供最高屏蔽效能。

**焊接屏蔽（Welded Shield）：** 接缝处焊接，连续导通，无泄漏。

**夹接缝（Clamped Seam）：** 可拆卸接缝，使用RF垫片（导电橡胶）确保接触连续性。

**紧固件穿透（Fastener Penetrations）：** 螺钉和螺栓的穿透会降低屏蔽效能，需要专门的RF垫片处理。

> **关键物理量：** 屏蔽效能由**吸收损耗**和**反射损耗**共同决定。厚度 $t$ 的金属板在高频下的吸收损耗：

$$A \approx 8.7 \frac{t}{\delta} \quad \text{dB}$$

其中 $\delta = \sqrt{2/(\omega\mu\sigma)}$ 是集肤深度（skin depth）。

### 4.5 穿透处理 | Penetrations

所有穿过屏蔽层的导体（电缆、导管、波导通风口）都需要专门的过滤和屏蔽处理，否则会成为电磁泄漏的"漏洞"。

### 4.7 屏蔽接地 | Shielding Grounding

屏蔽结构需要单点接地，防止地环路导致的额外干扰。

---

## 第 5 章：Anechoic Chamber Design Techniques
**Source:** Hemming, Chapter 5, OCR pages 72-87

### 5.1 引言 | Introduction

暗室设计在20世纪50年代主要依靠经验，直到电磁理论的发展使得更为系统化的设计成为可能。

**设计参数：**
- 工作频率范围（下限频率 $f_{\text{min}}$）
- 照射区尺寸（Test Zone Size）
- 场均匀性要求（Field Uniformity）
- 反射电平（Reflection Level）
- 静区（Quiet Zone）质量

### 5.2 吸波材料布置 | Absorber Arrangement

**材料选择依据：**
- 频率范围：低频需要更长的尖劈吸收器
- 功率容量：高功率测试需要耐高温材料
- 重量限制：航空航天应用需要轻量化

**吸波材料的安装密度和方向：**
所有吸波材料应直接接触金属墙壁，缝隙会形成缝隙天线效应，导致额外泄漏。

---

## 第 6 章：The Rectangular Anechoic Chamber
**Source:** Hemming, Chapter 6, OCR pages 88-111

### 6.1 引言 | Introduction

矩形暗室是最常见的暗室形式。其设计相对简单，但由于墙角和墙壁交界处的反射处理较为复杂。

**主要误差来源：**
1. 墙壁和天花板的残余反射
2. 吸波材料的方向性（材料背面金属板反射）
3. 暗室内物体（转台、支架）的散射

### 6.2 测试区设计 | Test Zone Design

**静区（Quiet Zone）的定义：**
静区是暗室内部一个指定区域，在该区域内场均匀性满足测试要求。

**静区与吸波材料的关系：**
待测天线必须完全位于静区内，且静区外的所有表面均覆盖高效吸波材料。

---

## 附录：关键技术指标速查

| 符号 | 含义 | 典型值 |
|------|------|--------|
| $\eta_0$ | 自由空间阻抗 | $377\ \Omega$ |
| $\delta$ | 集肤深度 | $\delta = \sqrt{2/(\omega\mu\sigma)}$ |
| $VSWR$ | 电压驻波比 | $< 1.5$ |
| $SE$ | 屏蔽效能 | $> 80$ dB |
| $R$ | 反射率 | $< -30$ dB |
| $K$ | 距离比 $2R/\lambda$ | $2 \sim 10$ |

---

**⚠️ 笔记说明：** 本笔记基于 OCR 识别文本洗稿整理，OCR 识别率约 85-90%，可能存在错误。公式和数值请以原书为准。