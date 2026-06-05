---
title: Chapter 11: Microwave Integrated Circuits & Antennas / 第11章：微波集成电路与天线
source: Collin, Foundations for Microwave Engineering, 2nd Ed.
---

# Chapter 11: Microwave Integrated Circuits & Antennas / 第11章：微波集成电路与天线

> **中英双语版**

> Synthesized from Collins §§3.12–3.13 (planar transmission lines), §5.3 (lumped elements),
> §10.1–10.11 (solid-state devices & amplifiers), plus standard MMIC/antenna references.
> 综合自Collins第3.12–3.13节（平面传输线）、第5.3节（集总元件）、
> 第10.1–10.11节（固态器件与放大器）以及标准MMIC/天线参考文献。

---

## 11.1 MIC Technology: Substrates, Fabrication, and MMIC / MIC技术：衬底、制造与MMIC

### 11.1.1 What is a Microwave Integrated Circuit? / 什么是微波集成电路？

A **microwave integrated circuit (MIC)** integrates transmission lines, matching elements, capacitors, resistors, and active devices on a common substrate. Two main forms exist / **微波集成电路(MIC)** 将传输线、匹配元件、电容、电阻和有源器件集成在公共衬底上。主要有两种形式：

| Type / 类型 | Description / 描述 | Key References / 主要参考文献 |
|------|-------------|----------------|
| **Hybrid MIC / 混合MIC** | Transmission lines & passives on substrate; discrete actives soldered in place / 传输线与无源器件在衬底上；分立有源器件焊接 | Collins §10 intro |
| **Monolithic MIC (MMIC) / 单片MIC** | All components (active + passive) fabricated on a single semiconductor chip / 所有元件（有源+无源）制作在单个半导体芯片上 | Collins §10, §3.12 |

### 11.1.2 Substrate Materials / 衬底材料

| Material / 材料 | $\varepsilon_r$ | Loss Tangent / 损耗角正切 | Thermal Cond. / 热导率 | Notes / 备注 |
|----------|-----|-------------|---------------|-------|
| **PTFE/woven glass / PTFE/编织玻璃** (Teflon) | 2.84 | 0.001–0.002 | Fair / 中等 | Low cost, common for hybrid MIC / 低成本，常用作混合MIC |
| **PTFE/microfiberglass / PTFE/微纤维玻璃** (RT/Duroid 5880) | 2.26 | 0.0005–0.001 | Fair / 中等 | Low loss, good for high frequencies / 低损耗，适合高频 |
| **Alumina (Al₂O₃) / 氧化铝** | 9.6–10.1 | 0.0001 | Excellent / 优秀 | Most common; good thermal conductivity / 最常见；热导率好 |
| **Gallium Arsenide (GaAs) / 砷化镓** | 12.9 | 0.0005–0.001 | Medium / 中等 | Substrate for MMIC / MMIC的衬底 |
| **Silicon (Si) / 硅** | 11.7–12.9 | — | Medium / 中等 | Low cost / 低成本 |
| **Sapphire / 蓝宝石** | 9.4 | 0.0001 | Good / 良好 | Low loss, expensive / 低损耗、昂贵 |
| **Beryllium Oxide (BeO) / 氧化铍** | 6.7 | 0.0004 | Excellent / 优秀 | High-power applications (toxic dust) / 高功率应用（有毒粉尘） |

**Key substrate requirements / 衬底的关键要求** (Collin §3.12):
- Low loss tangent / 低损耗角正切 (tan $\delta$ < 0.001)
- High $\varepsilon_r$ → shorter guided wavelength → more compact circuits / 高$\varepsilon_r$ → 引导波长更短 → 电路更紧凑
- Good thermal conductivity for power dissipation / 良好的热导率以散热
- Mechanical strength and ease of machining / 机械强度和易加工性
- Uniform thickness and dielectric constant across wafer / 晶圆上厚度和介电常数均匀

### 11.1.3 Fabrication Processes / 制造工艺

| Process / 工艺 | Application / 应用 |
|---------|------------|
| **Photolithography / 光刻** | Define conductor patterns (strip widths, gaps) / 定义导体图形（条宽、间隙） |
| **Ion Implantation / 离子注入** | Create active device regions in MMIC / 在MMIC中创建有源器件区 |
| **Metal Deposition & Evaporation / 金属淀积与蒸发** | Ohmic contacts, transmission lines / 欧姆接触、传输线 |
| **Via Hole Etching & Plating / 通孔刻蚀与电镀** | Ground connections through substrate / 穿过衬底的接地连接 |
| **Dielectric Deposition / 介质淀积** | MIM capacitors, passivation / MIM电容、钝化 |
| **Electron-Beam Lithography / 电子束光刻** | Submicron features (gate lengths < 0.1 $\mu$m) / 亚微米特征（栅长<0.1 $\mu$m） |
| **Molecular Beam Epitaxy (MBE) / 分子束外延** | Grow heterostructures for HEMT/HBT / 生长HEMT/HBT异质结构 |

**Hybrid vs MMIC tradeoffs / 混合与MMIC的权衡** (Collin §10 intro):
- **Below ~10 GHz / ~10 GHz以下**: Hybrid often cheaper / 混合MIC通常更便宜
- **0.1–10 GHz**: Miniature lumped elements enable MMIC / 微型集总元件使MMIC成为可能
- **Millimeter-wave / 毫米波**: MMIC becomes cost-effective / MMIC更具成本效益

---

## 11.2 Planar Transmission Lines for MICs / MIC的平面传输线

### 11.2.1 Microstrip Line / 微带线

The dominant planar transmission line for MICs. A conducting strip of width W on a dielectric substrate (thickness H, $\varepsilon_r$) with a ground plane on the bottom.
MIC中最重要的平面传输线。介质衬底（厚度H，$\varepsilon_r$）上的宽度为W的导体条带，底部为接地面。

**Quasi-static parameters / 准静态参数** (Collin §3.12):

Effective dielectric constant / 有效介电常数：

$$ \varepsilon_e = \frac{\varepsilon_r + 1}{2} + \frac{\varepsilon_r - 1}{2} \cdot \frac{1}{\sqrt{1 + 12H/W}} $$

Characteristic impedance / 特性阻抗：

$$ Z_0 = \begin{cases}
\frac{60}{\sqrt{\varepsilon_e}} \ln\left( \frac{8H}{W} + \frac{W}{4H} \right), & W/H \le 1 \\[6pt]
\frac{120\pi}{\sqrt{\varepsilon_e} \left[ W/H + 1.393 + 0.667 \ln(W/H + 1.444) \right]}, & W/H \ge 1
\end{cases} $$

**Key properties / 关键性质** (Collin §3.12):
- Quasi-TEM mode for frequencies where W, H ≪ $\lambda$ / 在W, H ≪ $\lambda$ 的频率下为准TEM模
- Dispersion / 色散：$\varepsilon_e(f)$ increases with frequency / 随频率增加
- Open structure → easy access for shunt/series component mounting / 开放结构 → 便于安装并联/串联元件

### 11.2.2 Coplanar Waveguide (CPW) / 共面波导

A center conductor (width S) with ground planes on either side, separated by slots (width W), all on the same substrate surface.
中心导体（宽度S）两侧各有接地面，由槽（宽度W）隔开，均位于同一衬底表面。

**Advantages / 优势** (Collin §3.13):
- Active/passive components connect on same side as ground (no via holes) / 有源/无源元件与接地在同一侧连接（无需通孔）
- Lower dispersion than microstrip at mm-wave frequencies / 毫米波频率下色散低于微带线
- Wider center conductor for given $Z_0$ → lower conductor loss / 给定 $Z_0$ 下中心导体更宽 → 导体损耗更低

### 11.2.3 Comparison / 对比

| Property / 特性 | Microstrip / 微带线 | CPW / 共面波导 | Slotline / 槽线 |
|----------|-----------|-----|----------|
| TEM nature / TEM特性 | Quasi-TEM / 准TEM | Quasi-TEM / 准TEM | Non-TEM |
| Via holes needed / 需通孔 | Yes (ground) / 是（接地） | No / 否 | No / 否 |
| Dispersion / 色散 | Moderate / 中等 | Low (small dims) / 低（小尺寸） | Higher / 较高 |
| Fabrication ease / 制造难易 | Very easy / 非常容易 | Easy / 容易 | Easy / 容易 |

---

## 11.3 Lumped Elements at Microwave Frequencies / 微波频率下的集总元件

### 11.3.1 Spiral Inductors / 螺旋电感

The most common lumped inductor for MICs / MIC中最常见的集总电感。

**Design constraints / 设计约束：**
- Total conductor length must be ≪ $\lambda$ to maintain lumped behavior / 总导体长度必须 ≪ $\lambda$ 以保持集总行为
- High-impedance (narrow) line maximizes inductance per unit length / 高阻抗（窄）线最大化单位长度电感

**Wheeler formula / 惠勒公式** (approximate for square spirals / 方螺旋近似)：

$$ L \approx \frac{\mu_0 n^2 d_{avg}}{2} \left[ \ln\left(\frac{2.46}{\rho}\right) + 0.2\rho^2 \right] $$

### 11.3.2 Capacitors / 电容

| Type / 类型 | Configuration / 结构 | Typical Range / 典型范围 | Notes / 备注 |
|------|--------------|---------------|-------|
| **Open-circuit stub / 开路短截线** | Short stub in shunt / 并联短截线 | ~1 pF | Simplest / 最简单 |
| **Interdigital / 交指电容** | Interleaved fingers in series / 交错指状 | Several pF / 数pF | Finger count & length control C / 指数和长度控制电容 |
| **MIM (Metal-Insulator-Metal) / 金属-绝缘体-金属** | Sandwich structure / 三明治结构 | $\leq$ 20 pF | Common in MMIC / 在MMIC中常见 |
| **Chip capacitor / 片式电容** | Discrete soldered / 分立焊接 | $\leq$ 100 pF | Hybrid MIC only / 仅混合MIC |

### 11.3.3 Resistors / 电阻

- Thin-film (NiCr, TaN) on substrate / 衬底上的薄膜（NiCr, TaN）
- Typical range / 典型范围：10 Ω–10 kΩ

---

## 11.4 Semiconductor Device Integration / 半导体器件集成

### 11.4.1 MESFET / 金属-半导体场效应管

The workhorse of GaAs MMIC technology / GaAs MMIC技术的主力。

**Characteristics / 特性：**
- Gate lengths / 栅长：submicron (< 0.5 $\mu$m typical / 典型值)
- $f_T$ (current gain cutoff / 电流增益截止频率)：30–100 GHz
- Gain / 增益：8–15 dB per stage at 2 GHz / 每级在2 GHz下
- Noise figure / 噪声系数：< 1 dB at 2 GHz / 在2 GHz下

### 11.4.2 HEMT / 高电子迁移率晶体管

Uses heterojunction (AlGaAs/GaAs) to create a 2D electron gas with very high mobility / 利用异质结（AlGaAs/GaAs）创建具有极高迁移率的二维电子气。

**Advantages over MESFET / 相比MESFET的优势：**
- Higher mobility → lower noise, higher $f_T$ / 更高迁移率 → 更低噪声、更高$f_T$
- Operating frequencies up to 100 GHz / 工作频率可达100 GHz
- Lower noise figure (~0.5 dB at 10 GHz) / 更低的噪声系数（10 GHz约0.5 dB）

### 11.4.3 HBT / 异质结双极晶体管

**Advantages / 优势：**
- Very low base resistance / 非常低的基极电阻
- High current gain / 高电流增益
- Speed increase 2–3$\times$ over homojunction BJT / 速度比同质结BJT快2–3倍

---

## 11.5 Antennas for MICs / MIC的天线

### 11.5.1 Microstrip Patch Antenna / 微带贴片天线

The most common antenna integrated with MICs / 与MIC集成的最常见天线。

**Resonant length / 谐振长度** (dominant TM₁₀ mode / 主导TM₁₀模)：

$$ L_{eff} = \frac{c}{2 f_r \sqrt{\varepsilon_e}} $$

**Patch width / 贴片宽度** (for efficient radiation / 为了高效辐射)：

$$ W = \frac{c}{2 f_r} \sqrt{\frac{2}{\varepsilon_r + 1}} $$

**Bandwidth / 带宽**：Typically 1–5% for standard patches / 标准贴片典型为1–5%。

### 11.5.2 Other Integrated Antennas / 其他集成天线

- **Slot antennas / 缝隙天线** (slot in ground plane / 接地面上开槽)
- **Yagi-Uda printed arrays / 印刷八木-宇田阵** (for directionality / 用于定向性)
- **Vivaldi (tapered slot) / 维瓦尔第（渐变槽）天线** for wideband applications / 用于宽带应用

---

## 11.6 Circuit Design Examples / 电路设计示例

### 11.6.1 LNA (Low-Noise Amplifier) / 低噪声放大器

Design approach / 设计方法 (Collins §10.10–10.11):

1. **Select device / 选择器件**：MESFET or HEMT with low NF / 低噪声系数的MESFET或HEMT
2. **Stability check / 稳定性检查**：Compute K and |$\Delta$| / 计算K和|$\Delta$|
3. **Source match / 源端匹配**：$\Gamma_{opt}$ for minimum noise figure (noise circles) / 最小噪声系数的$\Gamma_{opt}$（噪声圆）
4. **Load match / 负载匹配**：$\Gamma_L$ for desired gain (constant gain circles) / 期望增益的$\Gamma_L$（等增益圆）
5. **Realization / 实现**：Microstrip matching networks on substrate / 衬底上的微带匹配网络

**Cascaded NF / 级联噪声系数** (Friis formula / 弗里斯公式)：

$$ F = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \cdots $$

---

## Design Example Summary / 设计示例汇总

| Circuit / 电路 | Freq. / 频率 | Technology / 工艺 | Key Figures / 关键指标 |
|---------|-------|-----------|-------------|
| 2 GHz LNA | 2 GHz | GaAs MESFET | NF < 1 dB, G > 12 dB |
| 10 GHz LNA | 10 GHz | GaAs HEMT | NF ~ 0.5 dB, G ~ 10 dB |
| 5 GHz Mixer / 混频器 | 5 GHz | Schottky MMIC | Conv. loss ~ 6 dB |
| 4 GHz VCO | 4 GHz | BJT/HBT | P_out ~ 10 dBm, tuning ~ 200 MHz |

---

> 🎉 **End of Collins Microwave Engineering — Complete Chapter Notes /**
> **Collins微波工程——完整章节笔记结束。**
> Synthesized from Collins §§3.12, 3.13, 5.3, 10.1–10.11 plus standard MIC/antenna references.
> 综合自Collins §§3.12, 3.13, 5.3, 10.1–10.11及标准MIC/天线参考文献。
