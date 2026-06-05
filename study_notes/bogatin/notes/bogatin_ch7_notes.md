---
title: "Chapter 7 — The Physical Basis of Transmission Lines"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 7
pages: "238–308"
---

# Ch7: The Physical Basis of Transmission Lines

> **中英双语版**

## Key Definitions | 关键定义

**Transmission line:** Any two conductors with length. One is the **signal path**, the other the **return path** (never call it "ground").
**传输线：** 任意两个有长度的导体。一个是**信号路径**，另一个是**返回路径**（切勿称之为"地"）。

**Uniform (controlled-impedance) line:** Cross section is constant down the length.
**均匀（受控阻抗）线：** 沿长度方向截面恒定。

**Balanced line:** Both conductors have the same shape/size (twisted pair, coplanar).
**平衡线：** 两个导体形状/尺寸相同（双绞线、共面线）。
**Unbalanced line:** Conductors differ (microstrip, coax, stripline).
**非平衡线：** 两个导体不同（微带线、同轴线、带状线）。

> **Engineering Intuition:** Forget the word "ground." Use "return path." The return current follows the signal current path — it has no idea what voltage level the return conductor is at.
> **工程直觉：** 忘掉"地"这个词，用"返回路径"。返回电流跟随着信号电流路径——它不知道返回导体的电压电平是多少。

## 7.1 Signal Speed | 信号速度

**Speed of electrons in copper:** ~1 cm/sec (about as fast as an ant crawls). Has **nothing** to do with signal speed.
**电子在铜中的运动速度：** ~1 cm/s（约蚂蚁爬行速度），与信号速度**完全无关**。

**Speed of signal (electromagnetic wave) in a transmission line:**
**信号（电磁波）在传输线中的速度：**

$$
v = \frac{1}{\sqrt{\epsilon_0 \epsilon_r \mu_0 \mu_r}} = \frac{c}{\sqrt{\epsilon_r \mu_r}} \approx \frac{12\ \text{in/nsec}}{\sqrt{\epsilon_r}}
$$

**Rules of thumb | 经验法则：**
- In air ($\epsilon_r = 1$): $v = 12$ inches/nsec (speed of light | 光速)
- In FR4 ($\epsilon_r \approx 4$): $v \approx 6$ inches/nsec（FR4 中约 6 英寸/ns）
- Wiring delay in FR4: **170 psec/inch**（FR4 布线时延：170 ps/英寸）

## 7.2 Spatial Extent of the Leading Edge | 上升沿的空间延伸

$$
d = RT \times v
$$

上升时间 × 传播速度 = 上升沿在传输线上的空间长度。

| Rise Time (nsec) | Spatial Extent (FR4) | 空间延伸（FR4） |
|:--:|:--:|:--:|
| 1.0 | 6 inches | 6 英寸 |
| 0.5 | 3 inches | 3 英寸 |
| 0.1 | 0.6 inch | 0.6 英寸 |
| 0.05 | 0.3 inch | 0.3 英寸 |

> **Engineering Intuition:** SI problems from discontinuities depend on their size compared to the spatial extent of the leading edge.
> **工程直觉：** 由不连续性引起的 SI 问题取决于不连续尺寸相对于上升沿空间延伸的大小。

## 7.3 Characteristic Impedance | 特性阻抗

**Zeroth-order model:** The signal sees instantaneous impedance as it charges up capacitance per length while propagating at speed $v$:
**零阶模型：** 信号在传播速度 $v$ 下逐段充电单位长度电容，所"看到"的瞬时阻抗：

$$
Z_0 = \frac{1}{v \cdot C_L} = \frac{83 \cdot \sqrt{\epsilon_r}}{C_L}
$$

where $C_L$ is in pF/inch. For a 50-$\Omega$ line in FR4: $C_L \approx 3.3$ pF/inch, $C_L \times Z_0 \approx 166$ pF/inch.
$C_L$ 单位为 pF/英寸。FR4 中 50 Ω 线的 $C_L$ 约 3.3 pF/英寸。

**Alternative form (from LL and CL) | 用分布电感和分布电容表达：**

$$
Z_0 = \sqrt{\frac{L_L}{C_L}}, \quad v = \frac{1}{\sqrt{L_L \cdot C_L}}
$$

**Famous characteristic impedances | 著名的特性阻抗值：**
| Interconnect | $Z_0$ | 互连类型 |
|:--|:--:|:--|
| Free space | 377 $\Omega$ | 自由空间 |
| RG58 coax | 52 $\Omega$ | RG58 同轴线 |
| RG59 coax (CATV) | 75 $\Omega$ | RG59 同轴线（有线电视） |
| Twisted pair | 100–130 $\Omega$ | 双绞线 |
| PCB microstrip | 50–75 $\Omega$ (typical) | PCB 微带线 |
| PCB power/ground planes | <1 $\Omega$ | PCB 电源/地平面 |
| Rambus | 28 $\Omega$ | Rambus 总线 |

**Why 50 Ω?** Minimum attenuation in coax for a fixed outer diameter — established in 1930s for radio/radar.
**为什么是 50 Ω？** 这是对于固定外径的同轴线衰减最小的阻抗值——起源于 1930 年代的无线电/雷达领域。

> **Engineering Intuition:** The input impedance of a line is **time-dependent**. During the round-trip time of flight ($2 \times TD$), the driver sees $Z_0$. After that, it sees whatever terminates the far end.
> **工程直觉：** 传输线的输入阻抗是**时变的**。在往返飞行时间 ($2 \times TD$) 内，驱动端看到的是 $Z_0$。之后看到的是远端端接的阻抗。

## 7.4 Driving a Transmission Line | 驱动传输线

**Voltage divider:** The launched voltage:
**分压：** 发射电压：

$$
V_{\text{launched}} = V_{\text{output}} \cdot \frac{Z_0}{R_{\text{source}} + Z_0}
$$

For $Z_0 = 50\ \Omega$, $V_{\text{output}} = 3.3\ \text{V}$:
对于 $Z_0 = 50\ \Omega$，$V_{\text{output}} = 3.3\ \text{V}$：
- $R_s = 5\ \Omega$: $V_{\text{launched}} = 3.0$ V (91%)
- $R_s = 50\ \Omega$: $V_{\text{launched}} = 1.65$ V (50%)
- $R_s = 100\ \Omega$: $V_{\text{launched}} = 1.1$ V (33%)

> **Engineering Intuition:** To drive a line (launch most of the voltage), the driver's output impedance must be much less than $Z_0$ — typically <10 $\Omega$.
> **工程直觉：** 要有效驱动传输线（发射绝大部分电压），驱动器的输出阻抗必须远小于 $Z_0$——通常 <10 Ω。

## 7.5 Return Paths | 返回路径

- Current travels in **complete loops**.（电流在**完整回路**中流动）
- Return current flows **through distributed capacitance** between signal and return paths — only where the signal voltage is changing ($dV/dt$).（返回电流通过信号路径与返回路径之间的**分布电容**流动——只在信号电压变化的地方存在）
- The return current in a plane is concentrated **underneath the signal trace**. At >100 kHz, it's highly localized.（平面中的返回电流集中在**信号走线下方**。>100 kHz 时高度局域化）
- **Any gap in the return path** increases loop inductance → higher instantaneous impedance → signal distortion.（**返回路径上的任何间隙**都会增加环路电感 → 瞬时阻抗增大 → 信号失真）

**When return path switches reference planes | 当返回路径切换参考平面时：**
- If planes are DC-coupled: use a return via adjacent to the signal via.（若平面 DC 耦合：在信号过孔旁放置返回过孔）
- If planes are DC-isolated: return current couples through plane-to-plane capacitance.（若平面 DC 隔离：返回电流通过平面间电容耦合）
- The impedance the return current sees between planes decreases with distance from the via:
  返回电流在平面间看到的阻抗随距离过孔的时间增大而减小：

$$
Z_{\text{return}}(t) \approx \frac{5 \cdot h}{t}
$$

where $h$ = plane spacing in mils, $t$ = time in nsec.
其中 $h$ 为平面间距（mil），$t$ 为时间（ns）。
- At $t = 0.1$ nsec, $h = 10$ mils: $Z_{\text{return}} \approx 0.5\ \Omega$
- 10 simultaneous switching signals × 20 mA each = 200 mA × 0.5 $\Omega$ = 100 mV ground bounce
  10 个同时开关信号 × 各 20 mA = 200 mA × 0.5 Ω = 100 mV 地弹

## 7.6 Characteristic Impedance of Planes | 平面的特性阻抗

For wide planes ($w \gg h$):
对于宽平面（$w \gg h$）：

$$
Z_0 \approx \frac{377\ \Omega}{\sqrt{\epsilon_r}} \cdot \frac{h}{w}
$$

## 7.7 Key Rules of Thumb | 关键经验法则

| Rule | Value | 中文说明 |
|:--|:--|:--|
| Speed of light (air) | 12 in/nsec | 光速（空气） |
| Speed of light (FR4) | 6 in/nsec | 光速（FR4） |
| Wiring delay (FR4) | 170 psec/inch | FR4 布线时延 |
| $C_L$ for 50-$\Omega$ line | 3.3 pF/inch | 50 Ω 线单位长度电容 |
| $L_L$ for 50-$\Omega$ line | 8.3 nH/inch | 50 Ω 线单位长度电感 |
| $C_L \times Z_0$ (FR4) | 166 pF/inch | 特征常数 |
| Round-trip delay (6-inch trace) | ~2 nsec | 6 英寸走线往返时延 |
| Signal sees $Z_0$ as resistive load | for $t < 2 \times TD$ | 信号在往返时延内将 $Z_0$ 视为阻性负载 |

## 7.8 Return Path Design Guidelines | 返回路径设计准则

- Use adjacent power/ground planes with thin dielectric for low plane impedance
  使用紧邻的电源/地平面，薄介质以降低平面阻抗
- Place return vias adjacent to signal vias when switching layers
  层切换时在信号过孔旁放置返回过孔
- Keep return paths continuous (no gaps, slots, or splits)
  保持返回路径连续（无间隙、开槽或分割）
- When planes must be DC-isolated, keep them tightly coupled (thin dielectric)
  当平面必须 DC 隔离时，保持紧耦合（薄介质）
- Route signal traces over continuous reference planes
  信号走线应布线在连续的参考平面上方
