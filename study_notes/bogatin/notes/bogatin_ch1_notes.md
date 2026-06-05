---
title: "Chapter 1 — Signal Integrity Is in Your Future"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 1
pages: "30–68"
---

# Ch1: Signal Integrity Is in Your Future

> **中英双语版**

## 1.1 What Is Signal Integrity? | 什么是信号完整性？

Signal integrity (SI) refers, in its broadest sense, to **all the problems that arise in high-speed products due to the interconnects**. It is about how the electrical properties of the interconnects, interacting with the digital signal's voltage and current waveforms, can affect performance.
**信号完整性（SI）** 广义上指高速产品中由于互连引起的**所有问题**。它研究互连的电气特性与数字信号的电压/电流波形相互作用如何影响性能。

The four families of SI noise problems:
SI 噪声问题的四大类别：

1. **Signal quality on a single net** — reflections and distortions from impedance discontinuities
   **单根网络信号质量** — 阻抗不连续性引起的反射与失真
2. **Cross talk between multiple nets** — mutual C and mutual L coupling
   **多网络间的串扰** — 互容和互感耦合
3. **Rail collapse in the power distribution system (PDS/PDN)** — voltage drop across impedance in power/ground network
   **电源分配系统中的轨道塌陷** — 电源/地网络阻抗上的电压降
4. **Electromagnetic interference (EMI)** — radiation from components or system
   **电磁干扰** — 元件或系统的辐射

> **Engineering Intuition:** When clock frequencies exceed ~100 MHz or rise times drop below ~1 nsec, interconnects are no longer "transparent" to signals. Every physical feature of the interconnect matters.
> **工程直觉：** 当时钟频率超过约 100 MHz 或上升时间低于约 1 ns 时，互连对信号不再是"透明"的。互连的每一个物理特征都会产生影响。

## 1.2 Signal Quality on a Single Net | 单根网络的信号质量

A **net** includes all metal connected together (signal path + return path). As a signal propagates, it constantly "probes" the instantaneous impedance. If the impedance changes, part of the signal reflects, distorting the waveform.
一个**网络**包含所有连接在一起的金属（信号路径 + 返回路径）。信号传播时不断"探测"瞬时阻抗。如果阻抗变化，部分信号就会反射，使波形失真。

**Impedance discontinuities** arise from | **阻抗不连续性**来源于：
- Line-width changes（线宽变化）
- Layer changes through vias（过孔换层）
- Gaps in return-path plane（返回路径平面上的间隙）
- Connectors（连接器）
- Branches, tees, or stubs（分支、T 形接头或短桩线）
- End of a net (high-Z receiver or low-Z driver)（网络末端，高阻接收端或低阻驱动端）

**Key strategy:** Keep the impedance the signal sees constant throughout the net via:
**关键策略：** 通过网络保持信号所看到的阻抗恒定：
1. Controlled-impedance traces (uniform transmission lines)（受控阻抗走线，即均匀传输线）
2. Routing rules for constant impedance topology（恒定阻抗拓扑的布线规则）
3. Strategically placed termination resistors（策略性放置的端接电阻）

**Rise-time dependence:** A discontinuity harmless at 33 MHz may be fatal at 100 MHz. Shorter rise times → larger distortions.
**上升时间依赖性：** 在 33 MHz 无害的不连续性在 100 MHz 可能是致命的。上升时间越短 → 失真越大。

> **Engineering Intuition:** "Ringing" is almost always reflections from impedance changes, not an exotic phenomenon. Fix the impedance discontinuity and the ringing disappears.
> **工程直觉：** "振铃"几乎总是由阻抗变化引起的反射，不是奇异现象。修复阻抗不连续性，振铃就会消失。

### Rise Time vs. Clock Frequency (Rule of Thumb) | 上升时间 vs. 时钟频率（经验法则）

$$
RT \approx \frac{1}{10 \times F_{\text{clock}}}
$$

where:
- $RT$ = rise time (10–90%), in nsec | 上升时间（10–90%），单位 ns
- $F_{\text{clock}}$ = clock frequency, in GHz | 时钟频率，单位 GHz

| $F_{\text{clock}}$ | $RT$ (approx) |
|:--:|:--:|
| 10 MHz | 10 nsec |
| 100 MHz | 1 nsec |
| 1 GHz | 100 psec |
| 10 GHz | 10 psec |

## 1.3 Cross Talk | 串扰

When one net (active) carries a signal, unwanted voltage/current couples to an adjacent quiet net through **capacitive** and **inductive** coupling.
当一根网络（主动）携带信号时，不需要的电压/电流通过**容性**和**感性**耦合进入相邻的安静网络。

- **Near-end cross talk (NEXT):** dominates when traces have wide uniform return planes
  **近端串扰（NEXT）：** 走线具有宽且均匀的返回平面时占主导
- **Far-end cross talk (FEXT):** can be larger than NEXT in microstrip
  **远端串扰（FEXT）：** 微带线中可能大于 NEXT
- **Ground bounce / SSN / SSO noise:** occurs when return paths are not wide uniform planes (connectors, packages, vias) — dominated by **mutual inductance**
  **地弹 / SSN / SSO 噪声：** 返回路径不是宽而均匀的平面时发生（连接器、封装、过孔），由**互感**主导

> **Engineering Intuition:** SSO noise is becoming one of the most critical issues in connectors and packages. The solution: minimize mutual inductance through careful geometry and use differential signaling.
> **工程直觉：** SSO 噪声正成为连接器和封装中最关键的问题之一。解决方案：通过精心的几何设计最小化互感，并使用差分信号。

## 1.4 Rail-Collapse Noise | 轨道塌陷噪声

When current through power/ground paths changes ($dI/dt$), a voltage drop occurs across the impedance of the PDN. This causes the voltage at the chip to **collapse**.
当通过电源/地路径的电流变化时（$dI/dt$），PDN 阻抗上产生电压降，导致芯片处的电压**塌陷**。

Trends making it worse | 使问题恶化的趋势：
- Lower supply voltages（更低的电源电压）
- Higher current consumption (more gates switching faster)（更高的电流消耗，更多门电路更快开关）
- Tighter noise margins（更严格的噪声容限）

**Target impedance** of the PDN (from Sun Microsystems estimate):
**PDN 的目标阻抗**（源于 Sun Microsystems 的估算）：

$$
Z_{\text{target}} = \frac{\text{Allowable ripple}}{\Delta I}
$$

| Year | Max PDN Impedance (Ω) | 最大 PDN 阻抗 |
|:--:|:--:|:--:|
| 1992 | ~0.1 | |
| 1998 | ~0.01 | |
| 2004 | ~0.001 | |

**Solutions | 解决方案：**
- Closely spaced power/ground planes with thin dielectric（紧耦合电源/地平面，薄介质）
- Multiple low-ESL decoupling capacitors（多颗低 ESL 去耦电容）
- Short, low-inductance package leads（短而低电感的封装引线）
- On-chip decoupling capacitance（片上去耦电容）
- Embedded capacitance materials (e.g., 3M C-Ply: 8 μm thick, $\epsilon_r = 20$)（嵌入式电容材料）

> **Engineering Intuition:** The same physical designs that lower rail-collapse noise also lower EMI. There is no conflict between good PDN design and good EMI performance.
> **工程直觉：** 降低轨道塌陷噪声的物理设计同样会降低 EMI。良好的 PDN 设计与良好的 EMI 性能之间没有冲突。

## 1.5 Electromagnetic Interference (EMI) | 电磁干扰

Three requirements for EMI | EMI 的三个必要条件：
1. **Source** of noise（噪声**源**）
2. **Pathway** to a radiator（通往辐射器的**路径**）
3. **Antenna**（**天线**）

**Common EMI sources | 常见 EMI 源：**
- Conversion of differential → common signal on external cables（外部电缆上差模→共模转换）
- Ground bounce generating common currents on shielded cables（地弹在屏蔽电缆上产生共模电流）

**Mitigation | 抑制措施：**
- Ferrite chokes on cables（线缆上的铁氧体磁环）
- Shielded enclosures（屏蔽壳体）
- Low-impedance I/O connector return paths（低阻抗 I/O 连接器返回路径）
- Good PDN design (same as rail-collapse solutions)（良好的 PDN 设计，与轨道塌陷方案相同）

## 1.6 Two Important Generalizations | 两个重要的普适结论

1. **All four families of SI problems get worse as rise times decrease.** Shorter $t_r$ → higher $dI/dt$, $dV/dt$.
   **四种 SI 问题都随上升时间减小而恶化。** 更短的 $t_r$ → 更高的 $dI/dt$ 和 $dV/dt$。
2. **Effective solutions are based on understanding impedance of interconnects.** Relating physical design to impedance is the key skill.
   **有效的解决方案基于对互连阻抗的理解。** 将物理设计与阻抗联系起来是关键技能。

## 1.7 Trends in Electronic Products | 电子产品趋势

- Intel processor clock frequencies double ~every 2 years (from ~1 MHz in 1971 to >3 GHz in 2000s)
  Intel 处理器时钟频率约每 2 年翻倍（从 1971 年的 ~1 MHz 到 2000 年代的 >3 GHz）
- Even **low clock-frequency products** get short rise times due to finer fab processes (Moore's Law "scary consequence")
  即使是**低时钟频率产品**，由于更精细的制造工艺，上升时间也在缩短（摩尔定律的"可怕后果"）
- High-speed serial links: OC-48 (2.5 Gbps) → OC-192 (10 Gbps) → OC-768 (40 Gbps)
- Serial buses: PCIe, Infiniband, Serial ATA, XAUI, Gigabit Ethernet all migrating to multi-Gbps

> **Engineering Intuition:** If your chip vendor migrates to a finer process node, the rise time of your "same" chip may drop, silently introducing SI problems even if the clock frequency hasn't changed.
> **工程直觉：** 如果芯片制造商迁移到更精细的工艺节点，你的"相同"芯片的上升时间可能会下降，即使时钟频率没有变化，也会悄悄引入 SI 问题。

## 1.8 Need for a New Design Methodology | 新设计方法论的需求

**The old way:** Build it → test it → redesign it (too slow).
**传统方式：** 构建 → 测试 → 重新设计（太慢）。
**The new way:** Predict performance early through modeling and simulation → design it right the first time.
**新方式：** 通过建模与仿真早期预测性能 → 一次做对。

Five key ingredients | 五个关键要素：
1. Understand root causes of SI problems（理解 SI 问题的根本原因）
2. Translate into specific design rules（转化为具体设计规则）
3. Predict performance early via modeling and simulation（通过建模与仿真早期预测性能）
4. Optimize design at every step（每一步优化设计）
5. Use measurements for risk reduction（利用测量降低风险）

## 1.9 Simulation Tools | 仿真工具

Three types | 三种类型：

1. **Electromagnetic (EM) simulators** — solve Maxwell's equations, model fields (HFSS, etc.)
   **电磁（EM）仿真器** — 求解麦克斯韦方程组，建模场
   - Necessary for: resonances, nonuniform wave propagation, EMI（用于：谐振、非均匀波传播、EMI）
   - Disadvantage: slow, requires skilled user（缺点：慢，需要熟练操作者）

2. **Circuit simulators (SPICE)** — solve differential equations of circuit elements
   **电路仿真器（SPICE）** — 求解电路元件的微分方程
   - Popular: HSPICE, PSPICE, LTSPICE
   - Good for: transmission lines, cross talk, switching noise（适用于：传输线、串扰、开关噪声）
   - Limitation: cannot handle EMI or resonances directly（局限：不能直接处理 EMI 或谐振）

3. **Behavioral simulators** — use tables/transfer functions
   **行为级仿真器** — 使用查表/传递函数
   - Advantage: fast computation（优点：计算速度快）
   - Used for: system-level simulation with IBIS models（用于：IBIS 模型的系统级仿真）

### Maxwell's Equations (for reference) | 麦克斯韦方程组（供参考）

**Time domain | 时域：**
$$
\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0} \quad
\nabla \cdot \mathbf{B} = 0 \quad
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \quad
\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}
$$

**Frequency domain ($e^{j\omega t}$ convention) | 频域：**
$$
\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0} \quad
\nabla \cdot \mathbf{H} = 0 \quad
\nabla \times \mathbf{E} = -j\omega\mu\mathbf{H} \quad
\nabla \times \mathbf{H} = \mathbf{J} + j\omega\epsilon\mathbf{E}
$$

## 1.10 Modeling | 建模

**Active device models | 有源器件模型：**
- **SPICE models:** contain transistor geometry details (vendors reluctant to share)（包含晶体管几何细节，厂商不愿分享）
- **IBIS models:** V-I and V-t curves, no proprietary info (easier to obtain)（VI 和 Vt 曲线，无专有信息，更易获取）

**Passive interconnect models:** R, L, C, transmission lines（**无源互连模型：** R、L、C、传输线）

> **Engineering Intuition:** "Garbage in, garbage out" applies to SI simulation. The model quality is the single most important factor determining simulation accuracy. Always demand vendor verification.
> **工程直觉：** "垃圾进，垃圾出"适用于 SI 仿真。模型质量是决定仿真精度的最重要因素。始终要求厂商验证。

## 1.11 Creating Circuit Models from Calculation | 通过计算创建电路模型

Three levels of approximation | 三个近似层次：

| Level | Accuracy | Effort | Use Case | 用途 |
|:--|:--:|:--:|:--|:--|
| Rules of thumb | Low (order-of-magnitude) | Very low | Sanity checks, intuition | 合理性检查、直觉 |
| Analytical approximations | Moderate (2–50%) | Low | Spreadsheet trade-offs | 电子表格权衡 |
| Numerical simulations (field solvers) | High (<1–2%) | High | Design sign-off | 设计签核 |

### Example: Loop Self-Inductance Approximation | 示例：环路自感近似

$$
L_{\text{self}} \approx 32 \cdot R \cdot \ln\left(\frac{4R}{D}\right) \quad \text{[nH]}
$$

where $R$ = loop radius (inches), $D$ = wire diameter (inches). Verified to ~2% accuracy against measurements.
其中 $R$ 为环路半径（英寸），$D$ 为导线直径（英寸）。经实测验证精度约 2%。

### Field Solvers | 场求解器
- **2D field solvers:** for uniform cross-section transmission lines (e.g., microstrip, stripline)
  **2D 场求解器：** 用于均匀截面传输线（如微带线、带状线）
- **3D field solvers:** for nonuniform structures (connectors, packages)
  **3D 场求解器：** 用于非均匀结构（连接器、封装）

## 1.12 Measurements | 测量

Three primary instruments | 三种主要仪器：

| Instrument | Domain | Frequency Range | What It Measures | 测量内容 |
|:--|:--:|:--:|:--|:--|
| Impedance Analyzer | Frequency | 100 Hz – 40 MHz | $Z(\omega) = V/I$ | 阻抗分析仪 |
| VNA | Frequency | kHz – 50+ GHz | S-parameters ($S_{11} \to Z_{\text{DUT}}$) | 矢量网络分析仪 |
| TDR | Time | DC – multi-GHz | Instantaneous impedance vs. position | 时域反射计 |

**Reflection coefficient (VNA) | 反射系数（VNA）：**
$$
\frac{V_{\text{reflected}}}{V_{\text{incident}}} = \frac{Z_{\text{DUT}} - 50\,\Omega}{Z_{\text{DUT}} + 50\,\Omega} = S_{11}
$$

> **Engineering Intuition:** Frequency-domain impedance is the *integrated* impedance of the entire DUT at each frequency. Time-domain impedance (TDR) shows the *spatial* impedance profile along the interconnect.
> **工程直觉：** 频域阻抗是每个频率下整个 DUT 的*积分*阻抗。时域阻抗（TDR）显示沿互连的*空间*阻抗分布。

## 1.13 Role of Measurements | 测量的作用

Measurements serve five critical roles, all related to **risk reduction**:
测量有五个关键作用，都与**降低风险**相关：
1. Verify accuracy of the design/simulation process（验证设计/仿真过程的准确性）
2. Verify as-fabricated components meet specs（验证制造后的元件满足规格）
3. Create equivalent electrical models（创建等效电气模型）
4. Emulate system performance（模拟系统性能）
5. Debug functional parts（调试功能故障部件）

> **Engineering Intuition:** The Delphi Electronics case study shows that a verified modeling process reduced connector design cycle from 9 weeks to 4 hours — a >100× improvement. The key was using TDR/VNA measurements to validate the model, then relying on the model for all future designs.
> **工程直觉：** Delphi Electronics 案例表明，经过验证的建模过程将连接器设计周期从 9 周缩短到 4 小时——提升了 100 倍以上。关键是用 TDR/VNA 测量验证模型，然后依赖模型进行所有后续设计。

## 1.14 Key Rules of Thumb | 关键经验法则

1. **Rise time vs. clock frequency:** $RT \approx 1/(10 \cdot F_{\text{clock}})$ [nsec for GHz]（上升时间 vs. 时钟频率）
2. **SI problems appear** when $RT < 1$ nsec or $F_{\text{clock}} > 100$ MHz（上升时间 < 1 ns 或时钟 > 100 MHz 时出现 SI 问题）
3. **Loop inductance of a wire:** ~25 nH/inch（导线环路电感约 25 nH/英寸）
4. **Critical net threshold:** at 100 MHz ~5–10% of nets; at 200 MHz+ >50% of nets（关键网络阈值）
5. **PDN target impedance:** decreases ~10× every 6 years（PDN 目标阻抗每 6 年降低约 10 倍）

## 1.15 Checklist for Designers | 设计师检查清单

- [ ] Identify all nets with rise times < 1 nsec（识别所有上升时间 < 1 ns 的网络）
- [ ] Ensure controlled-impedance traces for critical nets（确保关键网络是受控阻抗走线）
- [ ] Minimize impedance discontinuities (vias, layer changes, stubs)（最小化阻抗不连续性）
- [ ] Space traces adequately to manage cross talk（保持足够线间距以控制串扰）
- [ ] Design PDN for target impedance across frequency range（在全频段内设计满足目标阻抗的 PDN）
- [ ] Place decoupling capacitors with lowest possible ESL（放置 ESL 尽可能低的去耦电容）
- [ ] Use ferrites on external cables（在外部电缆上使用铁氧体）
- [ ] Verify models (IBIS/SPICE) are current and accurate（验证模型是最新且准确的）
- [ ] Validate simulations with measurements (TDR/VNA)（用测量验证仿真结果）
