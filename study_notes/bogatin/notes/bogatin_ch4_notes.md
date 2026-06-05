---
title: "Chapter 4 — The Physical Basis of Resistance"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 4
pages: "142–153"
---

# Ch4: The Physical Basis of Resistance

> **中英双语版**

## 4.1 Translating Physical Design into Electrical Performance | 从物理设计到电气性能

Modeling = translating physical design (width, length, thickness, material) into equivalent circuit elements (R, L, C).
建模 = 将物理设计参数（宽度、长度、厚度、材料）转化为等效电路元件（R、L、C）。

> **Engineering Intuition:** The design process is intuitive. New ideas come from understanding the **meaning** of the equations, not from numerically solving them.
> **工程直觉：** 设计过程是直观的。新想法来源于理解方程式的**含义**，而非数值求解。

## 4.2 Resistance of a Uniform Conductor | 均匀导体的电阻

For a conductor with **uniform cross section** down its length:
对于沿长度方向**截面均匀**的导体：

$$
R = \rho \cdot \frac{d}{A}
$$

where:
- $R$ = resistance (Ohms) | 电阻（Ω）
- $\rho$ = bulk resistivity (Ohm-cm) | 体电阻率（Ω·cm）
- $d$ = length between ends (cm) | 两端间长度（cm）
- $A$ = cross-sectional area (cm²) | 横截面积（cm²）

**Example:** Gold wire bond, length = 0.2 cm (80 mils), diameter = 0.0025 cm (1 mil), $\rho_{\text{gold}} = 2.5\ \mu\Omega\text{-cm}$:
**示例：** 金线键合，长 0.2 cm (80 mils)，直径 0.0025 cm (1 mil)，$\rho_{\text{金}} = 2.5\ \mu\Omega\text{-cm}$：

$$
R = 2.5\times10^{-6} \cdot \frac{0.2}{\pi/4 \cdot (0.0025)^2} \approx 0.1\ \Omega
$$

> **Engineering Intuition:** A 1-mil diameter wire bond, 80 mils long, has about 0.1 Ohm resistance. Resistance scales linearly with length, inversely with area — just like water flow through a pipe.
> **工程直觉：** 1 mil 粗、80 mils 长的键合线电阻约为 0.1 Ω。电阻与长度成正比、与面积成反比——就像水流过管道一样。

## 4.3 Bulk (Volume) Resistivity | 体电阻率

**Bulk resistivity** $\rho$ is a fundamental material property (intrinsic), independent of the size of the conductor. Units: $\Omega$-cm or $\Omega$-inches.
**体电阻率 $\rho$** 是材料本征属性，与导体尺寸无关。单位：Ω·cm 或 Ω·in。

**Conductivity** $\sigma = 1/\rho$, units: Siemens/meter.
**电导率** $\sigma = 1/\rho$，单位：西门子/米。

| Material | $\rho$ ($\mu\Omega$-cm) | Uses | 用途 |
|:--|:--:|:--|:--|
| Silver | 1.47 | Best conductor | 最佳导体 |
| Copper | 1.58–4.5 | PCBs, wires | PCB、导线（工艺影响） |
| Gold | 2.01 | Wire bonds | 键合线 |
| Aluminum | 2.61 | IC metallization | IC 金属化 |
| Solder (Pb/Sn) | 15 | Solder joints | 焊点 |
| Kovar | 49 | IC lead frames | IC 引线框架 |

> **Engineering Intuition:** Copper resistivity varies 50%+ depending on processing (electroplated vs. rolled vs. annealed). If you need <10% accuracy, measure it.
> **工程直觉：** 铜的电阻率因工艺不同（电镀 vs. 轧制 vs. 退火）可变化 50% 以上。如需 <10% 精度，需实际测量。

## 4.4 Resistance per Length | 单位长度电阻

For uniform cross-section conductors:
对于截面均匀的导体：

$$
R_L = \frac{R}{d} = \frac{\rho}{A}
$$

**Rule of thumb:** Wire bond resistance per length ≈ **1 Ohm/inch** (1-mil diameter gold wire).
**经验法则：** 键合线单位长度电阻 ≈ **1 Ω/英寸**（1 mil 直径金线）。

| Wire (AWG) | Diameter (mils) | $R_L$ ($\Omega$/1000 ft) |
|:--:|:--:|:--:|
| 24 | 20.1 | 25.7 |
| 22 | 25.4 | 16.1 |
| 20 | 32.0 | 10.2 |
| 18 | 40.3 | 6.4 |

## 4.5 Sheet Resistance | 薄层电阻

For traces on a layer with uniform thickness $t$:
对于具有均匀厚度 $t$ 的层上走线：

$$
R = \frac{\rho}{t} \cdot \frac{d}{w} = R_{\text{sq}} \cdot n
$$

where:
- $R_{\text{sq}} = \rho / t$ = **sheet resistance** (Ohms per square) | **薄层电阻**（Ω/方块）
- $n = d/w$ = number of squares | 方块数

> **Engineering Intuition:** Any square (any size) cut from the same sheet has the same resistance = $R_{\text{sq}}$. If you double both length and width, the resistance stays the same.
> **工程直觉：** 从同一薄层上切出的任意方块（任意大小）都具有相同的电阻值 $R_{\text{sq}}$。若同时加倍长和宽，电阻不变。

**Copper sheet resistance | 铜箔薄层电阻：**
| Copper weight | Thickness | $R_{\text{sq}}$ |
|:--|:--:|:--:|
| 1-oz | 1.4 mil (35 $\mu$m) | 0.5 m$\Omega$/sq |
| 1/2-oz | 0.7 mil (17.5 $\mu$m) | 1.0 m$\Omega$/sq |

**Rule of thumb:** $R_{\text{sq}}$ of 1/2-ounce copper = **1 m$\Omega$/sq**. A 5-mil-wide, 5-inch-long trace has $n = 5000/5 = 1000$ squares, so $R = 1\ \Omega$.
**经验法则：** 1/2 oz 铜箔的 $R_{\text{sq}}$ = **1 mΩ/方块**。5 mil 宽、5 英寸长的走线有 $n = 1000$ 个方块，故 $R = 1\ \Omega$。

**Four-point probe measurement:** $R_{\text{sq}} = 4.53 \times R_{\text{meas}}$ (probes far from edges).
**四探针测量：** $R_{\text{sq}} = 4.53 \times R_{\text{meas}}$（探针远离边缘时）。

## 4.6 Resistance per Length vs. Line Width | 单位长度电阻与线宽的关系

| Line width (mils) | $R_L$, 1-oz Cu ($\Omega$/inch) | $R_L$, 1/2-oz Cu |
|:--:|:--:|:--:|
| 5 | 0.1 | 0.2 |
| 10 | 0.05 | 0.1 |
| 20 | 0.025 | 0.05 |

> **Engineering Intuition:** A 10-inch, 5-mil-wide trace in 1/2-oz Cu has $R = 0.2\ \Omega/\text{inch} \times 10 = 2\ \Omega$. At high frequencies, resistance increases due to skin effect (~$\sqrt{f}$).
> **工程直觉：** 10 英寸长、5 mil 宽的 1/2 oz 铜走线 $R = 2\ \Omega$。高频时电阻因趋肤效应增大（~$\sqrt{f}$）。

## 4.7 Key Formulas | 关键公式

| Formula | Description | 中文说明 |
|:--|:--|:--|
| $R = \rho \cdot d / A$ | Uniform conductor resistance | 均匀导体电阻 |
| $\sigma = 1/\rho$ | Conductivity from resistivity | 电导率 |
| $R_L = \rho / A$ | Resistance per length | 单位长度电阻 |
| $R_{\text{sq}} = \rho / t$ | Sheet resistance | 薄层电阻 |
| $R = R_{\text{sq}} \cdot n$ | Trace resistance from sheet resistance | 走线电阻（由薄层电阻计算） |
| $n = d / w$ | Number of squares | 方块数 |
| $R_{\text{sq}} = 4.53 \cdot R_{\text{meas}}$ | Four-point probe extraction | 四探针提取 |
