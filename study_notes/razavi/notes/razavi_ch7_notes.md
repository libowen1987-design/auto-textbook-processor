---
chapter: 7
title: Passive Devices
source: Behzad Razavi, RF Microelectronics, 2nd Edition, McGraw-Hill, 2012
pages: 429-495
---

# Chapter 7: Passive Devices
# 第七章：无源器件

> *"Passive devices — inductors, transformers, varactors, and transmission lines — are the "artistic" elements of RF design, often determining the difference between a mediocre and an excellent RFIC."*
>
> **（中文）** 无源器件（电感、变压器、变容二极管、传输线）是射频集成电路设计中最需要"艺术"的部分。片上电感的品质因子（$Q$）、变压器的耦合系数、变容二极管的调谐范围等参数往往决定了射频电路性能的优劣。

---

## 7.1 General Considerations | 一般性考量

### Role of Passives in RFIC | 无源器件在射频集成电路中的作用

| Device | Primary Function | Key Figure of Merit |
|---|---|---|
| On-chip inductor | Load, matching, chokes | $Q$, self-resonance $f_{\text{SR}}$ |
| Transformer |balun, push-pull, impedance transform | Coupling $k$, $Q$ |
| Varactor | Frequency tuning (VCO) | Tuning range $\Delta f/f$, $Q$ |
| Transmission line | $50\ \Omega$ interconnects, stubs | $Z_0$, loss $\alpha$ |
| MIM/MOS capacitor | AC coupling, decoupling | $C_{\text{per area}}$, $Q$ |

> **（中文）** 在CMOS射频集成电路中，无源器件通常占据最大的芯片面积。例如，一个$2.4\ \text{GHz}$的片上螺旋电感可能占用$200 \times 200\ \mu\text{m}^2$以上。更糟糕的是，片上无源器件的性能（$Q$值、自谐振频率等）远不如分立元件，这迫使射频工程师在电路拓扑和版图设计上做出大量优化。

### Why On-Chip Passives Are Challenging | 片上无源器件的设计挑战

1. **Substrate losses**: Conductive Si substrate (resistivity $\sim 1-10\ \Omega\cdot\text{cm}$) causes eddy current losses in inductors
2. **Metal resistance**: Thin on-chip metals have higher sheet resistance than thick copper
3. **Parasitic capacitance**: Overlaid metal-insulator-semiconductor structure forms parasitic capacitors
4. **No magnetic core**: On-chip "inductors" are purely planar spirals with no magnetic core (low inductance density)

---

## 7.2 Inductors | 电感

### 7.2.1 Basic Structure | 基本结构

A planar spiral inductor consists of metal turns on the top metal layer(s), typically in a square, hexagonal, or octagonal shape:

```
     ───────────────
    │  ← w (track width)
    │ ─ ─ ─ ─ ─ ← s (spacing)
    │ ─────────── │
    │             │ ↑ n turns
    └─────────────┘
    ←─── l ────→
```

**Inductance of a square spiral (Wheeler's formula):**

$$
L \approx \frac{\mu_0 n^2 A_{\text{avg}}}{l_{\text{avg}} + 0.89w} \quad \text{(7.1)}
$$

where $A_{\text{avg}}$ is the average area per turn, $l_{\text{avg}}$ is the average turn length.

**More accurate formula (Monaco):**

$$
L = \frac{1.27 \mu_0 n^2 d_{\text{avg}}}{2} \left[\ln\left(\frac{2.07}{\rho}\right) + 0.18\rho + 0.13\rho^2\right] \quad \text{(7.2)}
$$

where $d_{\text{avg}}$ is average diameter, $\rho = d_{\text{out}}/d_{\text{avg}}$.

> **（中文）** 片上平面螺旋电感的电感值主要由匝数$n$、平均直径$d_{\text{avg}}$和匝间距$s$决定。电感值随匝数$n$的平方增加（因为磁通匝链数），但随着间距$s$增大而减小（磁耦合降低）。实际设计中，电感值通常在$1-50\ \text{nH}$范围内。

### 7.2.2 Inductor Geometries | 电感几何形状

| Shape | Pros | Cons |
|---|---|---|
| Square | Easy layout, standard DRC | Corners increase resistance, eddy currents |
| Hexagonal | Lower resistance than square | Slightly more complex layout |
| Octagonal | Best $Q$ at high frequency | Complex layout |
| Circular | Lowest resistance | Not manufacturable in standard CMOS |

> **（中文）** 八边形（octagonal）电感在高频（$> 5\ \text{GHz}$）时$Q$值最高，因为其金属线中的电流路径更平滑（避免了方形电感尖角处的电流拥挤效应）。但标准CMOS工艺通常只支持矩形金属层，因此八边形是通过模拟逼近实现的。

### 7.2.3 Inductance Equations | 电感方程

**Series resistance of the spiral:**

$$
R_S = \frac{\rho_{\text{eff}} \cdot l_{\text{total}}}{w \cdot t_{\text{eff}}} \quad \text{(7.3)}
$$

where $\rho_{\text{eff}}$ is the effective metal resistivity (including skin effect), $t_{\text{eff}}$ is the effective metal thickness.

**Skin depth at frequency $f$:**

$$
\delta = \sqrt{\frac{\rho}{\pi \mu_0 f}} \quad \text{(7.4)}
$$

For copper at $2.4\ \text{GHz}$: $\delta \approx 1.3\ \mu\text{m}$. Standard aluminum interconnect ($t \approx 1\ \mu\text{m}$) is already affected by skin effect.

> **（中文）** 趋肤效应（skin effect）在高频下使电流集中在金属表面流动，有效导电厚度降低，等效串联电阻$R_S$增大。对于薄金属层（$\sim 1\ \mu\text{m}$），趋肤效应在几$\text{GHz}$频段已开始影响$Q$值。使用厚顶层金属（如$3\ \mu\text{m}$铜）或将多根细金属线并联（以模拟厚金属）是提高$Q$的常见技术。

### 7.2.4 Parasitic Capacitance | 寄生电容

**Inter-turn capacitance $C_{\text{turn}}$:** Between adjacent turns (typically $0.1-0.5\ \text{fF/turn}$).

**Metal-to-substrate capacitance $C_{\text{ox}}$:** 

$$
C_{\text{ox}} = \frac{\epsilon_{\text{ox}}}{t_{\text{ox}}} \cdot A_{\text{spiral}} \quad \text{(7.5)}
$$

**Self-Resonance Frequency $f_{\text{SR}}$:**

$$
f_{\text{SR}} = \frac{1}{2\pi\sqrt{L C_{\text{parasitic}}}} \quad \text{(7.6)}
$$

For an $nH$-range inductor, $f_{\text{SR}} \approx 5-20\ \text{GHz}$.

> **（中文）** 片上电感的寄生电容（$C_{\text{turn}}$和$C_{\text{ox}}$）与其电感$L$在自谐振频率$f_{\text{SR}}$处发生谐振。超过$f_{\text{SR}}$后，电感表现为电容性，不可使用。因此，选择电感时必须确保工作频率远低于$f_{\text{SR}}$（通常要求$f < 0.5 f_{\text{SR}}$）。

### 7.2.5 Quality Factor $Q$ | 品质因子 $Q$

**Definition:**

$$
Q = \frac{\text{Peak magnetic energy stored}}{\text{Energy dissipated per cycle}} \times 2\pi = \frac{\omega L}{R_S} \quad \text{(7.7)}
$$

**Including substrate losses:**

$$
Q = \frac{\omega L}{R_S + R_{\text{sub}}} \quad \text{(7.8)}
$$

where $R_{\text{sub}}$ is the substrate eddy current loss resistance.

> **（中文）** 电感的$Q = \omega L / R_S$是衡量其性能的核心指标。低$R_S$（低金属损耗）和高$L$（高储能）意味着高$Q$。但$L$本身随频率变化（集总参数模型仅在$f < 0.2 f_{\text{SR}}$时成立），因此$Q$的计算需要使用分布参数模型。

**Peak $Q$ phenomenon:** $Q$ does NOT increase monotonically with frequency — it peaks at $f_Q^{\text{max}}$ then drops due to substrate losses and parasitic capacitance:

$$
f_Q^{\text{max}} \approx \frac{1}{2\pi} \sqrt{\frac{1}{LC_{\text{ox}}} - \frac{R_S^2}{L^2}} \quad \text{(7.9)}
$$

> **（中文）** 片上电感的$Q$值通常在某个频率达到峰值（典型$Q_{\max} \approx 10-20$），之后因寄生电容和衬底损耗急剧下降。选择电感时，应确保工作频率接近或略低于$Q_{\max}$对应的频率。

### 7.2.6 Methods to Improve $Q$ | 提高$Q$值的方法

1. **Thick top metal layer**: Increases effective thickness, reduces $R_S$
2. **Hollow inductor**: Removing the center (where $B$ field is weakest) saves metal and reduces $R_S$
3. **Pattering ground shields**: Metal groundebeneath inductor reduces substrate coupling (but adds shunt capacitance)
4. **Silicon-on-Insulator (SOI)**: Thick Buried Oxide reduces substrate eddy currents
5. **Post-processing thick copper**: Post-CMOS copper plating ($t \approx 5-10\ \mu\text{m}$) gives $Q > 30$

> **（中文）** 改善片上电感$Q$值的方法：①使用厚顶层金属（如Copper BEOL工艺）可将$Q$提高$2-3$倍；②空心电感（hollow inductor）去除中心无效区域，降低电阻同时几乎不降低电感；③衬底图案化地屏蔽（pattering ground shield）减少衬底涡流损耗，但会引入额外的寄生电容。

---

## 7.3 Transformers and Baluns | 变压器与平衡-不平衡变换器

### Basic Transformer Model | 变压器基本模型

An on-chip transformer consists of two inductors magnetically coupled:

$$
L_1 = \frac{N_1^2 \mu A_{\text{core}}}{l} \quad \text{(7.10)}
$$
$$
L_2 = \frac{N_2^2 \mu A_{\text{core}}}{l} \quad \text{(7.11)}
$$

**Coupling coefficient $k$:**

$$
k = \frac{M}{\sqrt{L_1 L_2}} = \frac{\mu N_1 N_2 A_{\text{core}}/l}{\sqrt{L_1 L_2}} \quad \text{(7.12)}
$$

For on-chip transformers, $k \approx 0.5-0.9$.

> **（中文）** 变压器利用磁耦合将能量从一个线圈传递到另一个。耦合系数$k$（$0 \le k \le 1$）取决于两个线圈的几何重叠度和距离。在片上变压器中，由于没有磁芯（磁通在空气中闭合），$k$通常较低（$0.5-0.8$），限制了变压器的效率。

### Balun (Balanced-to-Unbalanced Transformer) | 平衡-不平衡变换器

A balun converts a single-ended signal to a differential signal (or vice versa):

**Ideal balun properties:**
1. **Impedance transformation**: $n = \sqrt{Z_{\text{primary}}/Z_{\text{secondary}}}$
2. **Phase balance**: $0^\circ$ and $180^\circ$ outputs (exactly balanced)
3. **Common-mode rejection**: Suppresses common-mode signals

**On-chip balun $Q$ and loss:**

$$
L_{\text{loss}} = 10\log_{10}\frac{1}{1 - k^2} \quad \text{dB} \quad \text{(7.13)}
$$

For $k = 0.7$: $L_{\text{loss}} \approx 3\ \text{dB}$ (coupling loss).

> **（中文）** Balun（平衡-不平衡变换器）在射频集成电路中用于单端-差分信号转换和阻抗匹配。变压器的耦合损耗$k$决定其效率：$k = 0.7$对应约$3\ \text{dB}$的耦合损耗，这是无源变压器无法避免的代价。在毫米波频段，耦合系数$k$可以更高（因为线圈间距离相对波长更近），$k \approx 0.9$是可能的。

---

## 7.4 Varactors | 变容二极管

### Types of Varactors | 变容二极管类型

| Type | Mechanism | Tuning Range $\Delta C/C$ | $Q$ at RF |
|---|---|---|---|
| MOS varactor | Gate oxide capacitance vs. $V_{GB}$ | $\sim 2:1$ | Low (due to series $R$) |
| PN junction varactor | Depletion capacitance vs. $V_{RB}$ | $\sim 3:1$ | Medium |
| Accumulation-mode MOS (AMOS) | Accumulation to inversion | $\sim 4:1$ | Higher |

**Capacitance-voltage relationship (PN junction):**

$$
C_j(V) = \frac{C_0}{\left(1 + \frac{V}{\phi_0}\right)^m} \quad \text{(7.14)}
$$

where $m \approx 0.3-0.5$ for an abrupt junction, $\phi_0 \approx 0.7-0.9\ \text{V}$ built-in potential.

> **（中文）** 变容二极管（varactor）是射频振荡器（VCO）中调谐频率的核心器件。PN结变容二极管的电容随反向偏置$V_{RB}$增大而减小（因为耗尽层展宽），典型调谐范围$\Delta C/C \approx 3:1$。MOS变容二极管（MOSCAP）可提供更大的调谐范围（$\sim 4:1$），但$Q$值较低。

### VCO Tuning Range Equations | VCO调谐范围方程

The VCO oscillation frequency with varactor load:

$$
\omega_{\text{VCO}} = \frac{1}{\sqrt{L(C_{\text{var}} + C_{\text{parasitic}})}} \quad \text{(7.15)}
$$

**Tuning sensitivity (KVCO):**

$$
K_{\text{VCO}} = \frac{d\omega_{\text{VCO}}}{dV_{\text{ctrl}}} = -\frac{\omega_{\text{VCO}}}{2}\frac{dC/C}{dV} \quad \text{(7.16)}
$$

> **（中文）** VCO的调谐灵敏度$K_{\text{VCO}} = d\omega/dV_{\text{ctrl}}$描述了控制电压变化引起的频率变化。$K_{\text{VCO}}$越大，PLL的调谐环路的增益越高，但同时也放大了变容管的噪声（$V_{\text{ctrl}}$噪声通过$K_{\text{VCO}}$转化为相位噪声）。这是一个典型的VCO设计权衡。

---

## Key Takeaways | 本章要点

1. **On-chip inductors** have $Q \approx 10-20$ at GHz frequencies, far below discrete inductors ($Q > 100$).
2. **Self-resonance $f_{\text{SR}}$** limits the usable frequency range; $Q$ peaks at $f < f_{\text{SR}}$.
3. **Substrate eddy current losses** are the dominant $Q$-limiting mechanism in Si ICs.
4. **Thick top metal + hollow inductor** are the primary $Q$-improvement techniques.
5. **Transformer coupling $k$** determines balun loss: $L_{\text{loss}} = -10\log(1-k^2)$.
6. **Varactor tuning range** $\Delta C/C \approx 3:1$ for PN junction; AMOS can reach $\sim 4:1$.
7. **$K_{\text{VCO}}$** is a key VCO design parameter: larger tuning range → larger $K_{\text{VCO}}$ → more VCO phase noise coupling to output.
