---
title: "Chapter 5 — The Physical Basis of Capacitance"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 5
pages: "156–179"
---

# Ch5: The Physical Basis of Capacitance

> **中英双语版**

## 5.1 Current Flow in Capacitors | 电容中的电流

Capacitance: measure of the capacity to store charge between two conductors at the cost of voltage:
**电容：** 衡量在两个导体之间以电压为代价存储电荷的能力：

$$
C = \frac{Q}{V}
$$

**Displacement current:** Current appears to flow through a capacitor only when the voltage changes:
**位移电流：** 只有当电压变化时，电流才"呈现"为流过电容：

$$
I = \frac{dQ}{dt} = C \frac{dV}{dt}
$$

> **Engineering Intuition:** Even though there's no DC path between conductors, capacitance provides an AC sneak path. This is the root of cross talk and many SI problems.
> **工程直觉：** 虽然导体之间没有直流通路，但电容提供了交流潜行路径。这是串扰和许多 SI 问题的根源。

## 5.2 Capacitance of a Sphere | 孤立球的电容

An isolated conductor has a **minimum** capacitance to "infinity" (earth/chassis):
孤立导体相对于"无穷远"（大地/机壳）存在一个**最小**电容：

$$
C \approx 4\pi\epsilon_0 r
$$

**Rule of thumb:** A sphere with 1-inch diameter has $C \approx 2$ pF.
**经验法则：** 直径 1 英寸的球体电容约 2 pF。

At 1 GHz, $|Z_C| = 1/(2\pi \times 10^9 \times 2\times10^{-12}) \approx 80\ \Omega$ — significant!
在 1 GHz 下，阻抗约 80 Ω——不可忽略！

> **Engineering Intuition:** Any conductor sticking out of a chassis has at least ~2 pF stray capacitance. At GHz frequencies, this is a low-impedance path.
> **工程直觉：** 任何伸出机壳的导体至少具有 ~2 pF 的杂散电容。在 GHz 频率下，这是一个低阻抗路径。

## 5.3 Parallel Plate Approximation | 平行板近似

$$
C = \frac{\epsilon_0 \epsilon_r A}{h}
$$

where $\epsilon_0 = 0.089$ pF/cm = 0.225 pF/inch.
其中真空介电常数 $\epsilon_0 = 0.089$ pF/cm = 0.225 pF/英寸。

**Example:** Penny-sized plates (1 cm²) separated by 1 mm:
**示例：** 便士大小的极板（1 cm²），间距 1 mm：
$$C = 0.089 \times 1 / 0.1 = 0.9\ \text{pF}$$

**Limitations:** Underestimates true capacitance by up to 2× when $h \approx w$ (fringe fields).
**局限性：** 当间距 $h \approx w$ 时，会低估真实电容达 2 倍（边缘场效应）。

## 5.4 Dielectric Constant | 介电常数

The relative dielectric constant $\epsilon_r$ (or Dk) increases capacitance:
相对介电常数 $\epsilon_r$（或 Dk）会增大电容：

$$
\epsilon_r = \frac{C_{\text{filled}}}{C_{\text{air}}}
$$

| Material | $\epsilon_r$ | Notes | 说明 |
|:--|:--:|:--|:--|
| Air | 1.0 | Reference | 参考标准 |
| Teflon (PTFE) | 2.1 | Lowest solid | 最低的固体介质 |
| Polyethylene | 2.3 | Coax cable | 同轴电缆 |
| FR4 | 4.0–4.5 | PCB laminate | PCB 层压板（取决于树脂/玻璃比） |
| Alumina | 9–10 | Ceramic packages | 陶瓷封装 |
| Water | ~80 | High dipole density | 高偶极密度 |
| Barium titanate | ~5000 | High-Dk ceramic | 高 Dk 陶瓷 |

> **Engineering Intuition:** FR4's Dk varies from ~4.8 at 1 kHz to ~4.4 at 10 MHz. Always specify frequency. If you need <10% accuracy, measure your specific sample.
> **工程直觉：** FR4 的 Dk 从 1 kHz 下的 ~4.8 变化到 10 MHz 下的 ~4.4。始终要标明频率。如需 <10% 精度，实测具体样品。

## 5.5 Power/Ground Plane Capacitance | 电源/地平面电容

**Parallel plate between power and ground planes:**
**电源层与地层之间的平行板电容：**

$$
C = \frac{\epsilon_0 \epsilon_r A}{h}
$$

For FR4 ($\epsilon_r \approx 4$), 10 mil spacing:
对于 FR4，10 mil 间距：
$$C \approx 1000\ \text{pF/in}^2 / h_{\text{mils}}$$

| Spacing | Capacitance per in² | 每平方英寸电容 |
|:--:|:--|:--|
| 10 mil FR4 | 100 pF/in² | |
| 2 mil FR4 | 500 pF/in² | |
| C-Ply (8 $\mu$m, $\epsilon_r$=20) | 14 nF/in² | |

**Decoupling time** (before 5% droop):
**去耦时间**（5% 电压跌落之前）：

$$
\Delta t \approx \frac{C \times 0.05 \times V^2}{P}
$$

**Example:** 4 in² of 10-mil FR4 planes → only 0.4 nF → decouples a 1W 3.3V chip for only **0.2 nsec**.
**示例：** 4 平方英寸的 10 mil FR4 平面仅 0.4 nF → 对 1W 3.3V 芯片的去耦时间仅 **0.2 ns**。

> **Engineering Intuition:** The primary value of power/ground planes is **low loop inductance**, NOT decoupling capacitance. The plane capacitance is typically 4+ orders of magnitude too small for bulk decoupling.
> **工程直觉：** 电源/地平面的主要价值在于**低环路电感**，而非去耦电容。平面电容通常比大容量去耦所需小 4 个数量级以上。

## 5.6 Capacitance per Length — Uniform Cross Sections | 单位长度电容——均匀截面

**50-Ohm transmission line rule of thumb:** $C_L \approx 3.5$ pF/inch.
**50 Ω 传输线经验法则：** 单位长度电容约 3.5 pF/英寸。

**Exact formulas | 精确公式：**

| Geometry | $C_L$ | 结构 |
|:--|:--|:--|
| **Coax** | $\dfrac{2\pi\epsilon_0\epsilon_r}{\ln(b/a)}$ | 同轴线 |
| **Twin rods** | $\dfrac{\pi\epsilon_0\epsilon_r}{\cosh^{-1}(s/2r)}$ or $\dfrac{\pi\epsilon_0\epsilon_r}{\ln(s/r)}$ for $s \gg r$ | 双杆线 |
| **Rod over plane** | $\dfrac{2\pi\epsilon_0\epsilon_r}{\ln(2h/r)}$ | 导线-平面 |
| **Microstrip (IPC approx)** | $\dfrac{0.67(1.41 + \epsilon_r)}{\ln(5.98h/(0.8w + t))}$ | 微带线（IPC 近似） |
| **Stripline (IPC approx)** | $\dfrac{1.4\epsilon_r}{\ln(2.4b/(0.8w + t))}$ | 带状线（IPC 近似） |

**Example RG58 coax:** $b/a = 3$, $\epsilon_r = 2.3$ → $C_L = 2.9$ pF/inch.
**示例 RG58 同轴线：** $b/a = 3$，介电常数 2.3 → 单位长度电容 2.9 pF/英寸。

## 5.7 2D Field Solvers | 二维场求解器

Only accurate way (<1% error) for arbitrary cross sections with non-homogeneous dielectrics. The **effective dielectric constant** captures the mixed dielectric environment:
对于非均匀介质的任意截面，是唯一的精确方法（误差 <1%）。**等效介电常数**捕捉了混合介质环境：

$$
\epsilon_{\text{eff}} = \frac{C_{\text{filled}}}{C_{\text{air}}}
$$

For microstrip:
对于微带线：
- Wide traces → $\epsilon_{\text{eff}} \to \epsilon_r$ (fields mostly in dielectric)（宽走线 → 场主要在介质中）
- Narrow traces → $\epsilon_{\text{eff}} \ll \epsilon_r$ (fields partly in air)（窄走线 → 场部分在空气中）
- Top coating ≈ trace width needed to fully enclose fields（顶层覆盖 ≈ 完全包围场所需的走线宽度）

> **Engineering Intuition:** IPC approximations can be off by 20%+. Never trust an approximation for sign-off. Use a verified 2D field solver.
> **工程直觉：** IPC 近似公式误差可达 20% 以上。切勿仅凭近似公式做设计签核。使用经过验证的 2D 场求解器。

## 5.8 Key Formulas | 关键公式

| Formula | Description | 中文说明 |
|:--|:--|:--|
| $C = Q/V$ | Definition of capacitance | 电容定义 |
| $I = C \cdot dV/dt$ | Displacement current | 位移电流 |
| $C = \epsilon_0 \epsilon_r A/h$ | Parallel plate approximation | 平行板近似 |
| $\epsilon_r = C_{\text{filled}}/C_{\text{air}}$ | Dielectric constant definition | 介电常数定义 |
| $\Delta t \approx 0.05 \cdot C \cdot V^2 / P$ | Decoupling time (5% droop) | 去耦时间（5% 跌落） |
| $C_L \approx 3.5$ pF/inch | 50-$\Omega$ line rule of thumb | 50 Ω 线经验法则 |
| $\epsilon_{\text{eff}} = C_{\text{filled}}/C_{\text{air}}$ | Effective dielectric constant | 等效介电常数 |
