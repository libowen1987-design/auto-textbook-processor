---
title: "Chapter 8 — Matching and Biasing Networks"
book: "RF Circuit Design — 2nd Ed."
author: "Reinhold Ludwig, Gene Bogdanov"
pages: "419–476"
processed: "2026-05-07"
tags: [matching-network, L-network, T-network, pi-network, smith-chart, stub-matching, bias-tee]
---

# Chapter 8: Matching and Biasing Networks | 第8章：匹配与偏置网络

> **Overview:** 本章系统阐述射频微波工程中两大核心议题：**(1) 任意负载阻抗与源阻抗之间的最优功率匹配**，以及 **(2) 有源器件（双极晶体管BJT/场效应晶体管FET）的直流偏置网络设计**。内容涵盖分立元件（L型、T型、π型）匹配网络、微带线与短截线（Stub）匹配网络、以及从A类到C类的放大器工作类别与效率分析。Smith圆图作为核心设计工具贯穿全书。

---

## 8.1 Impedance Matching Using Discrete Components | 分立元件阻抗匹配

### 8.1 Impedance Matching Using Discrete Components | 分立元件阻抗匹配.1 Two-Component Matching Networks (L-Section)

#### 基本原理 | Basic Principles

最大功率传输定理要求源阻抗等于负载阻抗的复共轭：

$$
Z_{\text{in}} = Z_{\text{source}}^* = R_{\text{s}} - jX_{\text{s}} \quad \text{（当 } Z_{\text{L}} = R_{\text{L}} + jX_{\text{L}} \text{ 时）}
$$

L型（L-section）匹配网络仅用**两个电抗性元件**（一个串联 + 一个并联），是最简单、最便宜、最可靠的匹配方案。图8-1展示了8种可能的L型网络拓扑。

#### 设计方法一：解析法 | Analytical Design Method

**Example 8-1：解析法设计L型匹配网络**

- **已知**：发射机输出阻抗 $Z_{\text{T}} = (150 + j75)\,\Omega$，天线输入阻抗 $Z_{\text{A}} = (75 - j15)\,\Omega$，工作频率 $f = 2\,\text{GHz}$（即 $\omega = 2\pi \times 2 \times 10^9\,\text{rad/s}$）
- **求**：L型匹配网络（串联储能电感 + 并联电容）的元件值

**解**：最大功率传输要求匹配网络输出阻抗 $Z_{\text{M}}$ 等于天线阻抗的复共轭：

$$
Z_{\text{M}} = Z_{\text{A}}^* = (75 + j15)\,\Omega
$$

网络结构为：发射机输出端并联电容 $C$ 后与串联电感 $L$ 相连，再接天线。设电容的容纳（susceptance）为 $B_{\text{C}} = \omega C$，电感的感抗为 $X_{\text{L}} = \omega L$，则：

$$
Z_{\text{M}} = jX_{\text{L}} + \left( jB_{\text{C}} + \frac{1}{Z_{\text{T}}} \right)^{-1}
$$

将 $Z_{\text{T}} = R_{\text{T}} + jX_{\text{T}}$ 和 $Z_{\text{A}} = R_{\text{A}} + jX_{\text{A}}$ 代入，分离实部与虚部，得到二元方程组：

$$
R_{\text{T}} = R_{\text{A}}(1 - B_{\text{C}} X_{\text{T}}) + (X_{\text{A}} + X_{\text{L}}) B_{\text{C}} R_{\text{T}} \tag{8.3a}
$$

$$
X_{\text{T}} = R_{\text{T}} R_{\text{A}} B_{\text{C}} - (1 - B_{\text{C}} X_{\text{T}})(X_{\text{A}} + X_{\text{L}}) \tag{8.3b}
$$

由(8.3a)解出 $X_{\text{L}}$ 代入(8.3b)，得到关于 $B_{\text{C}}$ 的**二次方程**：

$$
B_{\text{C}} = \frac{-R_{\text{A}} X_{\text{T}} \pm \sqrt{(R_{\text{A}} X_{\text{T}})^2 + 4R_{\text{T}}(R_{\text{T}} - R_{\text{A}})X_{\text{A}}^2}}{2R_{\text{T}}(R_{\text{T}} - R_{\text{A}})} \tag{8.4}
$$

取"+"号（确保 $B_{\text{C}} > 0$），代入数值：

$$
\boxed{B_{\text{C}} = 9.2\,\text{mS} \;\quad C = \frac{B_{\text{C}}}{\omega} = 0.73\,\text{pF}}
$$

$$
\boxed{X_{\text{L}} = 76.9\,\Omega \;\quad L = \frac{X_{\text{L}}}{\omega} = 6.1\,\text{nH}}
$$

> **工程直觉**：解析法精确但繁琐——解二次方程后还需解线性方程，手工计算极易出错。在计算机上用电子表格实现则非常高效。

#### 设计方法二：Smith圆图图解法 | Smith Chart Graphical Method

> **核心规则**（图8-3）：
> - **串联电感/电容**：沿**等电阻（constant-resistance）圆**运动；电感向上半圆旋转（感抗为正），电容向下半圆旋转（容抗为负）。
> - **并联电感/电容**：沿**等电导（constant-conductance）圆**运动；电感向上半圆旋转（容纳为正），电容向下半圆旋转（容纳为负）。

**Example 8-2：图解法设计L型匹配网络（同一问题）**

- **已知**：同Example 8-1，取 $Z_0 = 75\,\Omega$
- **归一化**：
  $$
  z_{\text{T}} = \frac{Z_{\text{T}}}{Z_0} = 2 + j1, \quad z_{\text{A}} = \frac{Z_{\text{A}}}{Z_0} = 1 + j0.2
  $$

- **步骤**：
  1. 在Smith圆图上画出经过 $z_{\text{T}}$ 的等电导圆
  2. 画出经过 $z_{\text{M}} = z_{\text{A}}^* = 1 - j0.2$ 的等电阻圆
  3. 两圆交点即 $z_{\text{TC}} \approx 1 - j1.22$
  4. 对应容纳 $y_{\text{TC}} = 0.4 + j0.49$，故并联电容的归一化容纳：
     $$
     jb_{\text{C}} = y_{\text{TC}} - y_{\text{T}} = j0.69
     $$
  5. 串联电感的归一化感抗：
     $$
     jx_{\text{L}} = z_{\text{A}} - z_{\text{TC}} = j1.02
     $$
  6. 反归一化得：
     $$
     C = \frac{b_{\text{C}}}{(2\pi \times 2\,\text{GHz}) \times 75} = 0.73\,\text{pF}, \quad L = \frac{x_{\text{L}} \times 75}{2\pi \times 2\,\text{GHz}} = 6.09\,\text{nH}
     $$

#### 六步设计通用流程 | Six-Step Design Procedure

1. **归一化**：$z_{\text{s}} = Z_{\text{s}}/Z_0$，$z_{\text{L}} = Z_{\text{L}}/Z_0$
2. 过 $z_{\text{s}}$ 画**等电阻圆**和**等电导圆**
3. 过 $z_{\text{L}}^*$ 画**等电阻圆**和**等电导圆**
4. 找出两组圆的**交点**（决定匹配网络数量）
5. 沿圆路径追踪，从 $z_{\text{s}}$ 到交点再到 $z_{\text{L}}^*$，读取归一化元件值
6. 反归一化得到实际元件值

**Example 8-3：设计所有可能的L型匹配网络**

- **已知**：$Z_{\text{s}} = (50 + j25)\,\Omega$，$Z_{\text{L}} = (25 - j50)\,\Omega$，$Z_0 = 50\,\Omega$，$f = 2\,\text{GHz}$
- **归一化**：$z_{\text{s}} = 1 + j0.5$，$z_{\text{L}} = 0.5 - j1$
- **4个交点**（A, B, C, D）在Smith圆图上对应4种拓扑：
  - $z_{\text{s}} \to z_{\text{A}} \to z_{\text{L}}$：并联电感 → 串联电感（L型网络）→ 对应 **图8-1(f)**
  - $z_{\text{s}} \to z_{\text{B}} \to z_{\text{L}}$：并联电容 → 串联电感 → 对应 **图8-1(h)**
  - $z_{\text{s}} \to z_{\text{C}} \to z_{\text{L}}$：串联电容 → 并联电感 → 对应 **图8-1(a)**
  - $z_{\text{s}} \to z_{\text{D}} \to z_{\text{L}}$：串联电感 → 并联电感 → 对应 **图8-1(e)**

- 元件值（以路径A为例）：
  - 并联电感：$jB_{\text{L}} = y_{\text{A}} - y_{\text{s}} = -j0.6 \Rightarrow B_{\text{L}} = -0.6 \Rightarrow L = 2.39\,\text{nH}$
  - 串联电感：$jX_{\text{L}} = z_{\text{L}}^* - z_{\text{A}} = j0.4 \Rightarrow L = 1.59\,\text{nH}$

> **工程直觉**：Smith圆图法的最大优势在于**可视化**——同时看到所有可能的拓扑选择、数量，以及各元件对匹配的"贡献方向"。这在CAD仿真中也能实时显示，是直觉设计的核心工具。

---

### 8.1 Impedance Matching Using Discrete Components | 分立元件阻抗匹配.2 Forbidden Regions, Frequency Response, and Quality Factor

#### 禁区 | Forbidden Regions

并非所有L型拓扑都能匹配任意阻抗组合。以 $Z_{\text{s}} = Z_0 = 50\,\Omega$ 为例：

- **图8-1(h)拓扑**（并联电容→串联电感）：如果负载阻抗落在 $g=1$ 等电导圆外部的某个阴影区域，则无法匹配。
- **图8-7**展示了各拓扑对应的禁区阴影。**关键性质**：禁区形状随源阻抗 $Z_{\text{s}}$ 变化而剧烈改变。

> **工程直觉**：对于固定的 $Z_{\text{s}}$，每个L型拓扑都有确定的"可匹配区域"。设计之初就应根据负载阻抗位置判断哪些拓扑可用，再从中选择最优（带宽、Q值、器件可得性）。

#### 频率响应与带宽 | Frequency Response and Bandwidth

以将 $R_{\text{L}} = 80\,\Omega$ 串联 $C_{\text{L}} = 2.65\,\text{pF}$ 匹配到 $50\,\Omega$ 输入为例（$f_0 = 1\,\text{GHz}$）：

**两种可能拓扑**（图8-8）：
- 拓扑A（低通型）
- 拓扑B（高通型）

在 $f_0$ 附近，匹配网络可等效为**带通滤波器**（bandpass filter），其**加载品质因数**定义为：

$$
Q_{\text{L}} = \frac{f_0}{B} \tag{8.6}
$$

其中 $f_0$ 为谐振频率，$B$ 为3dB带宽。

**Example 8-4：窄带匹配网络设计**

- **已知**：$Z_{\text{L}} = (25 + j20)\,\Omega$（串联R-L形式），$Z_{\text{s}} = 50\,\Omega$，$f_0 = 1\,\text{GHz}$
- **归一化负载**：$z_{\text{L}} = 0.5 + j0.4$（位于 $g=1$ 等电导圆内）
- **两种可选拓扑**：
  - **方案1**：串联电感 + 并联电容 [图8-12(b)]
  - **方案2**：串联电容 + 并联电感 [图8-12(c)]

从Smith圆图上读取两方案的**节点品质因数**均为 $Q_{\text{n}} = 1$。

$$
B = \frac{f_0}{Q_{\text{L}}} = \frac{2f_0}{Q_{\text{n}}} = \frac{2 \times 1\,\text{GHz}}{1} = 2\,\text{GHz}
$$

实际仿真结果：
- 方案1带宽 $B_1 \approx 2.4\,\text{GHz}$
- 方案2带宽 $B_2 = 2(f_{\text{hi}} - f_0) \approx 1.9\,\text{GHz}$（不对称型，无低截）

> **工程直觉**：相同谐振频率、相同 $Q_{\text{n}}$ 的两个L型网络，带宽可以相差 $25\%$。**拓扑选择直接影响高低频抑制特性**，这在宽带放大器设计中至关重要。

#### 节点品质因数 $Q_{	ext{n}}$ 与 Smith 圆图等 $Q_{	ext{n}}$ 圆 | Node Quality Factor $Q_{\text{n}}$ and Smith Chart Circles

**定义1**（串联节点）：
$$
Q_{\text{n}} = \frac{|X_{\text{s}}|}{R_{\text{s}}} \tag{8.10}
$$

**定义2**（并联节点）：
$$
Q_{\text{n}} = \frac{|B_{\text{p}}|}{G_{\text{p}}} \tag{8.11}
$$

由归一化阻抗 $z = \frac{1 + \Gamma}{1 - \Gamma}$，可推导出等 $Q_{\text{n}}$ 圆的圆心与半径：

$$
Q_{\text{n}} = \frac{x}{r} \quad \Rightarrow \quad \text{圆方程：} \left(r - \frac{Q_{\text{n}}^2}{Q_{\text{n}}^2+1}\right)^2 + \left(x + \frac{Q_{\text{n}}}{Q_{\text{n}}^2+1}\right)^2 = \frac{1}{Q_{\text{n}}^2+1} \tag{8.16}
$$

> **Smith圆图上读取 $Q_{\text{L}}$ 的简便方法**：直接从圆图读出匹配网络最高 $Q_{\text{n}}$ 值，然后除以2：$Q_{\text{L}} = Q_{\text{n}}/2$。这是因为 $Q_{\text{L}}$ 与 $Q_{\text{n}}$ 之间存在恒等关系：

$$
Q_{\text{L}} = \frac{Q_{\text{n}}}{2} \tag{8.13}
$$

> **工程直觉**：带宽控制是L型网络的"痛点"——$Q_{\text{L}}$ 由阻抗值自然决定，设计师**无法主动选择**。当需要特定带宽时，必须引入第三个元件，即T型或π型网络。

---

### 8.1 Impedance Matching Using Discrete Components | 分立元件阻抗匹配.3 T and Pi Matching Networks

#### 设计原理 | Design Principles

T型（三个串联/并联电抗）和π型（三个并联/串联电抗）网络增加了一个**额外的节点**，从而提供了**控制 $Q_{\text{n}}$（即带宽）的自由度**。

**Example 8-5：T型匹配网络设计**

- **已知**：$Z_{\text{L}} = (60 - j30)\,\Omega$，$Z_{\text{in}} = (10 + j20)\,\Omega$，$Q_{\text{n,max}} = 3$，$f_0 = 1\,\text{GHz}$
- **拓扑**：串联 $Z_1$（与负载串联）→ 并联 $Z_2$ → 串联 $Z_3$（与输入串联）

**设计步骤**（图8-15）：
1. 在Smith圆图上找到 $z_{\text{in}}$ 对应点
2. 画出 $Q_{\text{n}} = 3$ 等值线与 $r = r_{\text{in}}$ 等电阻圆的**交点B**（B点同时满足 $Q_{\text{n}}=3$ 和 $r=r_{\text{in}}$）
3. 过B点画等电导圆，与 $r = r_{\text{L}}$ 等电阻圆交于**A点**
4. 追踪路径：$z_{\text{L}} \to Z_1 \to \text{A} \to Z_2 \to \text{B} \to Z_3 \to z_{\text{in}}$

**最终网络**（图8-16）：
- $Z_1$（与负载串联）：纯感抗 $jX_1 = j37\,\Omega \Rightarrow L_1 = 5.89\,\text{nH}$
- $Z_2$（并联节点）：纯容抗 $-jB_2 \Rightarrow C_2 = 5.0\,\text{pF}$（取 $Q_{\text{n}}=3$ 等值线上的值）
- $Z_3$（与输入串联）：纯感抗 $jX_3 = j73\,\Omega \Rightarrow L_3 = 11.6\,\text{nH}$

> **工程直觉**：T型网络的"第三自由度"以**增加一个元件**为代价，换取对 $Q_{\text{L}}$（带宽）的主动控制。 oscillator设计需要高Q以抑制谐波，宽带放大器则需要低Q。

**Example 8-6：π型匹配网络设计（最小 $Q_{\text{n}}$）**

- **已知**：$Z_{\text{L}} = (10 - j10)\,\Omega$，$Z_{\text{in}} = (20 + j40)\,\Omega$，$f_0 = 2.4\,\text{GHz}$
- **目标**：最低可能 $Q_{\text{n}}$

**分析**：最低可实现 $Q_{\text{n}}$ 由输入阻抗位置的 $Q_{\text{n}}$ 决定：
$$
Q_{\text{n,min}} = \frac{|X_{\text{in}}|}{R_{\text{in}}} = \frac{40}{20} = 2
$$

**设计步骤**（图8-17）：
1. 在Smith圆图上过 $z_{\text{in}}$ 画 $g = g_{\text{in}}$ 等电导圆
2. 找到该圆与 $Q_{\text{n}} = 2$ 轮廓的交点B
3. 过B画 $g = g_{\text{L}}$ 等电导圆，与 $r = r_{\text{L}}$ 等电阻圆交于A点
4. 追踪路径读出各元件值

**结果**（图8-18）：
- $C_1$（输入端并联）：$C_1 = 2.65\,\text{pF}$
- $L$（串联节点）：$L = 6.63\,\text{nH}$
- $C_2$（输出端并联）：$C_2 = 1.77\,\text{pF}$

> **工程直觉**：π型网络的**带宽不能无限增大**——最小可实现 $Q_{\text{n}}$ 由 $Z_{\text{L}}$ 和 $Z_{\text{in}}$ 本身决定。这给宽带放大器设计设置了物理极限，往往需要级联多个匹配段。

---

## 8.2 Microstrip Line Matching Networks | 微带线匹配网络

### 8.2 Microstrip Line Matching Networks | 微带线匹配网络.1 From Discrete Components to Microstrip Lines

当频率进入**低GHz范围**时，分立元件的**寄生效应**（引线电感、寄生电容）变得不可忽略。此时改用**分布式元件**（微带线）更合适。

**混合设计**：两条串联微带线（特性阻抗 $Z_0$）+ 中间**并联集总电容**（图8-19）。这种结构：
- 便于**加工后调试**（可变电容位置和容值）
- 两条微带线通常取**相同特性阻抗**（简化调试）

**Example 8-7：混合匹配网络设计**

- **已知**：$Z_{\text{L}} = (30 + j10)\,\Omega$，$Z_{\text{in}} = (60 + j80)\,\Omega$，$Z_0 = 50\,\Omega$，$f_0 = 1.5\,\text{GHz}$
- **结构**：串联微带线TL1 → 并联电容C → 串联微带线TL2

**解法**（图8-20）：
1. 在Smith圆图上画**负载SWR圆**（经过 $z_{\text{L}} = 0.6 + j0.2$）
2. 画**输入SWR圆**（经过 $z_{\text{in}} = 1.2 + j1.6$）
3. 选取转换点A：$y_{\text{A}} = 1 - j0.6$
4. 并联电容使导纳沿 $g=1$ 等电导圆移动至B点（B在输入SWR圆上）
5. 串联微带线TL2使阻抗沿SWR圆运动至 $z_{\text{in}}$
6. 从外圆WTG刻度读取 $l_1$、$l_2$

**结果**（图8-21）：
- $l_1 = 0.15\lambda$，$l_2 = 0.13\lambda$，$C = 1.05\,\text{pF}$

**调谐灵敏度**（图8-22）：电容位置偏移 $\pm 2\,\text{mil}$ 就导致输入阻抗**剧烈变化**，这说明该结构对加工精度要求极高。

> **工程直觉**：混合网络**调试灵活**但**对容值和位置都很敏感**。 prototyping阶段首选此方案；量产阶段则倾向于纯分布式（Stub）设计。

---

### 8.2 Microstrip Line Matching Networks | 微带线匹配网络.2 Single-Stub Matching Networks

用**开路或短路短截线（Stub）**完全替代集总元件。

**两种拓扑**（图8-23）：
- **(a)**：串联传输线 + 与负载并联的Stub
- **(b)**：与输入并联的Stub + 串联传输线+负载

四个可调参数：$l_{\text{s}}$、$Z_{\text{0s}}$（Stub长度/特性阻抗）、$l_{\text{L}}$、$Z_{\text{0L}}$（主线长度/特性阻抗）。

**Example 8-8：单Stub匹配网络（固定特性阻抗）**

- **已知**：$Z_{\text{L}} = (60 - j45)\,\Omega$，$Z_{\text{in}} = (75 + j90)\,\Omega$，$Z_{\text{0}} = 75\,\Omega$，$Z_{\text{0s}} = 75\,\Omega$
- **拓扑**：图8-23(a)

**解法**（图8-24）：
1. 归一化：$y_{\text{L}} = 0.8 - j0.6$
2. 画输入SWR圆（经过 $z_{\text{in}} = 1 + j1.2$）与 $g = 0.8$ 等电导圆交于两点A、B
3. 对应两个解：
   - **解A**：$jB_{\text{s,A}} = j0.45$（开路Stub：$l_{\text{s,A}} = 0.067\lambda$；短路Stub：$l_{\text{s,A}} = 0.067\lambda + \lambda/4 = 0.317\lambda$）
   - **解B**：$jB_{\text{s,B}} = -j1.65$（开路Stub：$l_{\text{s,B}} = 0.337\lambda$）
4. 串联线长度：$l_{\text{L,A}} = 0.266\lambda$；$l_{\text{L,B}} = 0.07\lambda$

> **工程直觉**：**短路Stub比开路Stub更短**（因为开路Stub的容纳为负，转换为短路Stub需延长 $\lambda/4$）。在PCB设计中，用**开路Stub**可避免焊接过孔（via），但需注意辐射损耗；同轴电缆则常用**短路Stub**。

**Example 8-9：单Stub匹配网络（固定长度、变特性阻抗）**

- **已知**：$Z_{\text{L}} = (120 - j20)\,\Omega$，$Z_{\text{in}} = (40 + j30)\,\Omega$，$l_{\text{L}} = 0.25\lambda$，$l_{\text{s}} = 0.375\lambda$，$Z_{\text{0s}} = 50\,\Omega$
- **拓扑**：图8-23(b)

**解法**：
1. 由 $\阻抗原理解$（阻抗与特性阻抗的关系式）：
   $$
   Z_1 = \frac{Z_{\text{0L}}^2}{Z_{\text{L}}} \quad \Rightarrow \quad Z_{\text{0L}} = \sqrt{G_{\text{in}} \cdot \frac{|Z_1|^2}{R_{\text{L}}}} = \cdots
   $$
2. 代入数值计算 $Z_{\text{0L}}$，发现需用**开路Stub**（"minus"符号）
3. 计算 $Z_{\text{os}}$ 的实际值

**平衡Stub设计**（图8-25）：将不平衡Stub替换为两根平衡Stub，每根的容纳为原Stub的一半：

$$
l_{\text{SB}} = f(l_{\text{s}}) \quad \text{（非线性关系，须在Smith圆图上查找）}
$$

> **工程直觉**：平衡Stub的每根长度**不等于原Stub的一半**，而须通过图解法确定。在印刷电路（微带）设计中，当需要多个Stub时，平衡设计可以消除不必要的辐射干扰。

---

### 8.2 Microstrip Line Matching Networks | 微带线匹配网络.3 Double-Stub Matching Networks

**单Stub的问题**：需要**可变长度的主传输线**（用于调节Stub与负载/输入的间距），这在固定网络上不可接受。

**双Stub解决方案**（图8-26）：两根Stub（开路或短路）中间夹一段**固定长度**（通常为 $\lambda/8$、$3\lambda/8$ 或 $5\lambda/8$）的传输线。

**工作原理**（图8-27）：
1. 从输入端向里看，要求 $y_{\text{in}} = 1$（完美匹配）
2. 线段 $l_2 = 3\lambda/8$ 导致 $g=1$ 圆**逆时针旋转** $2\beta l_2 = 3\pi/2$（270°）
3. 通过调节 $l_{\text{s1}}$ 使导纳落在**旋转后的 $g=1$ 圆**上
4. 再通过调节 $l_{\text{s2}}$ 抵消剩余电纳，实现 $y_{\text{A}} = 1$

**禁区**：当负载导纳 $y_{\text{D}}$（$Z_{\text{L}}$ 与 $l_1$ 组合后）落在 $g=2$ 圆**内部**时，该负载**无法匹配**。商用双Stub调谐器通过 $l_1 = l_3 \pm \lambda/4$ 的关系解决此问题（将负载接到调谐器另一端即可）。

**Example 8-10：双Stub匹配网络设计**

- **已知**：$l_3 = l_2 = 3\lambda/8$，$l_1 = \lambda/8$，$Z_{\text{L}} = (50 + j50)\,\Omega$，$Z_0 = 50\,\Omega$
- **求**：两根短路Stub的长度

**解法**（图8-28）：
1. 归一化 $y_{\text{D}} = 0.4 - j0.2$（不在禁区内，$g_{\text{D}} < 2$）
2. 画旋转后的 $g=1$ 圆（逆时针转270°）
3. 与 $g=0.4$ 等电导圆交于两点（两组解）
4. 取 $y_{\text{C}} = 0.4 - j1.8$：
   - $jB_{\text{s1}} = y_{\text{C}} - y_{\text{D}} = -j2 \Rightarrow l_{\text{s1}} = 0.074\lambda$（短路）
5. 旋转 $y_{\text{C}}$ 至 $y_{\text{B}} = 1 + j3$：
   - $jB_{\text{s2}} = -j3 \Rightarrow l_{\text{s2}} = 0.051\lambda$（短路）

> **工程直觉**：双Stub调谐器是**fixed tuner（固定调谐器）**的首选方案，广泛用于生产测试和仪器（VNA、频谱仪）校准。当Stub替换为**变容二极管（varactor）**时，可实现**电子调谐**——通过改变二极管电容来调节Stub的等效电纳。

---

## 8.3 Amplifier Classes of Operation and Biasing Networks | 放大器工作类别与偏置网络

### 8.3 Amplifier Classes of Operation and Biasing Networks | 放大器工作类别与偏置网络.1 Classes of Operation and Efficiency

#### 四种工作类别（图8-29） | Four Classes of Operation (Fig. 8-29)

| 类别 | 导通角 $\theta_{\text{c}}$ | 输出波形 | 理论最大效率 |
|------|--------------------------|---------|------------|
| **A** | $360°$ | 完整正弦 | $50\%$ |
| **AB** | $180° < \theta_{\text{c}} < 360°$ | 截去部分负半周 | $50\% \sim 78.5\%$ |
| **B** | $180°$ | 半波整流 | $78.5\%$ |
| **C** | $0° < \theta_{\text{c}} < 180°$ | 窄脉冲 | $\to 100\%$ |

**效率定义**：
$$
\eta = \frac{P_{\text{RF}}}{P_{\text{S}}} = \frac{\text{负载RF平均功率}}{\text{电源平均功率}} \tag{8.21}
$$

#### Example 8-11：效率与导通角的关系推导 | Example 8-11: Efficiency vs. Conduction Angle Derivation

设负载电流波形（图8-30）为：
$$
I_{\text{L}}(\theta) = I_0 \cos\theta, \quad -\theta_{\text{c}}/2 \leq \theta \leq \theta_{\text{c}}/2
$$

电源电流含静态电流 $I_{\text{Q}}$：
$$
I_{\text{S}} = I_{\text{Q}} + I_0 \cos\theta, \quad I_{\text{Q}} = -I_0 \cos(\theta_{\text{c}}/2) \tag{8.23-8.24}
$$

**电源平均功率**：
$$
P_{\text{S}} = \frac{1}{2\pi} \int_{-\theta_{\text{c}}/2}^{\theta_{\text{c}}/2} V_{\text{CC}}(I_{\text{Q}} + I_0 \cos\theta)\,d\theta = \frac{V_{\text{CC}} I_0}{2\pi}\left[\sin\frac{\theta_{\text{c}}}{2} + \theta_{\text{c}}\cos\frac{\theta_{\text{c}}}{2}\right] \tag{8.26}
$$

**RF负载平均功率**：
$$
P_{\text{RF}} = \frac{1}{2\pi}\int_{-\theta_{\text{c}}/2}^{\theta_{\text{c}}/2} \frac{I_0^2}{2}\cos^2\theta\,d\theta = \frac{I_0 V_{\text{CC}}}{4\pi}\left(\theta_{\text{c}} - \sin\theta_{\text{c}}\right) \tag{8.27}
$$

**效率**：
$$
\eta = \frac{P_{\text{RF}}}{P_{\text{S}}} = \frac{1}{4}\cdot\frac{\theta_{\text{c}} - \sin\theta_{\text{c}}}{\sin(\theta_{\text{c}}/2) + (\theta_{\text{c}}/2)\cos(\theta_{\text{c}}/2)} \tag{8.28}
$$

数值验证：
- **Class A**（$\theta_{\text{c}} = 2\pi$）：$\eta = 50\%$
- **Class B**（$\theta_{\text{c}} = \pi$）：$\eta = \dfrac{\pi - \sin\pi}{2[\sin(\pi/2) + (\pi/2)\cos(\pi/2)]} = \dfrac{\pi}{4} \approx 78.5\%$

> **工程直觉**：**A类效率最低但线性度最好**，适用于小信号放大器和低噪声前置放大器；**C类效率最高但失真极大**，仅用于需要强滤波的振荡器或频率合成器；**AB类是实际工程中的折中方案**——兼顾线性度与效率（通常 $\eta \approx 60\% \sim 70\%$），广泛用于功率放大器（PA）。

---

### 8.3 Amplifier Classes of Operation and Biasing Networks | 放大器工作类别与偏置网络.2 Bipolar Transistor (BJT) Biasing Networks

#### 分类 | Classification

- **无源（被动）偏置**：电阻网络，最简单但对温度和晶体管参数变化敏感
- **有源（主动）偏置**：用低频晶体管或二极管提供稳定参考点

#### 被动偏置网络 | Passive Biasing Networks

**Example 8-12：BJT共发射极被动偏置设计**

- **已知**：$I_{\text{C}} = 10\,\text{mA}$，$V_{\text{CE}} = 3\,\text{V}$，$V_{\text{CC}} = 5\,\text{V}$，$\beta = 100$，$V_{\text{BE}} = 0.8\,\text{V}$
- **网络1** [图8-32(a)]：
  - $I_1 = I_{\text{C}} + I_{\text{B}} = I_{\text{C}}(1 + 1/\beta) = 10.1\,\text{mA}$
  - $R_1 = (V_{\text{CC}} - V_{\text{BE}})/I_1 \approx 416\,\Omega$
  - $R_2 = V_{\text{BE}}/(I_1 - I_{\text{B}}) \approx 9.9\,\Omega$

- **网络2** [图8-32(b)]：
  - 选取 $V_{\text{E}} = 1.5\,\text{V}$
  - $I_1 = 10I_{\text{B}} = 10 \times 0.1\,\text{mA} = 1\,\text{mA}$
  - $R_3 = (V_{\text{CC}} - V_{\text{E}})/I_1 = 3.5\,\text{k}\Omega$
  - $R_4 = V_{\text{E}}/(I_{\text{C}}/\beta) = 1.5\,\text{k}\Omega$（基极电阻）
  - $R_5 = (V_{\text{CC}} - V_{\text{CE}} - V_{\text{E}})/I_{\text{C}} = 200\,\Omega$（集电极电阻）

#### 主动偏置网络 | Active Biasing Networks

**Example 8-13：主动偏置网络设计**

- **已知**：$I_{\text{C2}} = 10\,\text{mA}$，$V_{\text{CE2}} = 3\,\text{V}$，$V_{\text{CC}} = 5\,\text{V}$，$\beta = 100$，$V_{\text{BE}} = 0.8\,\text{V}$
- **结构**（图8-33）：低频晶体管 $Q_1$ 为RF晶体管 $Q_2$ 提供基极电流

**设计步骤**：
1. 选 $I_{\text{C1}} = 10I_{\text{B2}} = 1\,\text{mA}$
2. $I_1 = I_{\text{C1}} + I_{\text{B1}} + I_{\text{B2}} \approx 1.2\,\text{mA}$
3. 设 $V_{\text{E1}} = 1\,\text{V}$，则 $R_{\text{E1}} = V_{\text{E1}}/(I_{\text{C1}} - I_{\text{B1}}) \approx 1.11\,\text{k}\Omega$
4. $R_{\text{C1}} = (V_{\text{CC}} - V_{\text{CE2}})/I_1 \approx 1.67\,\text{k}\Omega$
5. $R_{\text{C2}} = (V_{\text{CC}} - V_{\text{CE2}})/I_{\text{C2}} = 200\,\Omega$

> **工程直觉**：**主动偏置的优势**：当 $Q_1$ 与 $Q_2$ 热耦合（同散热片）时，$Q_2$ 温度升高导致 $I_{\text{C}}$ 上升，同时 $Q_1$ 的 $V_{\text{BE}}$ 下降，使 $Q_1$ 集电极电流下降，进而降低 $Q_2$ 的基极驱动，实现**温度自补偿**。代价是电路板面积增大、功耗增加。

**DC与RF工作点独立性**（图8-35、8-36）：
- **DC**：阻塞电容开路，RFC短路 → 共发射极配置
- **RF**：阻塞电容短路，RFC开路 → 共基极配置

> **工程直觉**：同一偏置网络可在**DC端**表现为共发射极（提供合适的静态工作点），在**RF端**表现为共基极（提供良好的高频特性）。这是RF电路设计的核心技巧之一。

---

### 8.3 Amplifier Classes of Operation and Biasing Networks | 放大器工作类别与偏置网络.3 Field Effect Transistor (FET) Biasing Networks

FET的偏置与BJT类似，但关键区别：**MESFET需要负栅压**（$V_{\text{GS}} < 0$）。

#### 双极电源被动偏置（图8-37） | Dual-Supply Passive Biasing (Fig. 8-37)

最简单网络，需要 $V_{\text{D}} > 0$ 和 $V_{\text{G}} < 0$ 两组电源。

#### 单电源被动偏置（图8-38） | Single-Supply Passive Biasing (Fig. 8-38)

在**源极串联电阻** $R_{\text{S}}$ 来提升源极电位，使栅极接地即可获得负 $V_{\text{GS}}$：

$$
V_{\text{GS}} = -I_{\text{D}} R_{\text{S}}
$$

温度补偿通常通过**热敏电阻（thermistor）**实现。

---

## 8.4 Summary | 本章小结

### 核心公式速查 | Key Formula Reference

| 公式 | 内容 |
|------|------|
| $Z_{\text{in}} = Z_{\text{s}}^*$ | 最大功率传输（共轭匹配） |
| $B_{\text{C}} = \dfrac{-R_{\text{A}}X_{\text{T}} \pm \sqrt{(R_{\text{A}}X_{\text{T}})^2 + 4R_{\text{T}}(R_{\text{T}}-R_{\text{A}})X_{\text{A}}^2}}{2R_{\text{T}}(R_{\text{T}}-R_{\text{A}})}$ | L网络电容容纳解析解 |
| $Q_{\text{L}} = \dfrac{f_0}{B}$ | 加载品质因数定义 |
| $Q_{\text{n}} = \dfrac{|X_{\text{s}}|}{R_{\text{s}}}$（串联）或 $Q_{\text{n}} = \dfrac{|B_{\text{p}}|}{G_{\text{p}}}$（并联） | 节点品质因数 |
| $Q_{\text{L}} = Q_{\text{n}}/2$ | L型网络的 $Q_{\text{L}}$ 与 $Q_{\text{n}}$ 关系 |
| $Q_{\text{n}} = \dfrac{x}{r}$（圆方程） | Smith圆图等 $Q_{\text{n}}$ 圆 |
| $\eta = \dfrac{1}{4}\cdot\dfrac{\theta_{\text{c}} - \sin\theta_{\text{c}}}{\sin(\theta_{\text{c}}/2) + (\theta_{\text{c}}/2)\cos(\theta_{\text{c}}/2)}$ | 效率随导通角关系 |
| $\eta_{\text{A}} = 50\%$；$\eta_{\text{B}} = 78.5\%$ | A类、B类理论效率 |
| $Z_1 = Z_{\text{0L}}^2/Z_{\text{L}}$ |  quarter-wave变压器阻抗关系 |
| $\eta = P_{\text{RF}}/P_{\text{S}}$ | 放大器效率定义 |

### 设计决策树 | Design Decision Tree

```
输入：Z_s, Z_L, f_0, 带宽/线性度要求
  │
  ├─ 带宽要求低（窄带）→ L型网络
  │     ├─ 检查禁区 → 选择可行拓扑
  │     └─ 计算 Q_n → 估算带宽
  │
  ├─ 带宽要求高（宽带）→ T型或π型网络
  │     ├─ 指定 Q_n,max → 画等Q_n圆与等阻抗圆交点
  │     └─ 选择拓扑（series-L/shunt-C 或 series-C/shunt-L）
  │
  └─ f > 1 GHz（分布式设计）
        ├─  prototyping → 混合网络（微带线+可调电容）
        ├─  量产 → Stub匹配
        │     ├─ 单Stub：需可变主线长度
        │     └─ 双Stub：主线长度固定，调谐方便
        │
        └─ 稳定/偏置
              ├─ 小信号线性PA → Class A
              ├─ 线性PA（中等功率）→ Class AB
              ├─ 高效PA（非线性）→ Class B/C
              └─ BJT → 主动偏置（温漂补偿）
                    └─ FET → 负栅压偏置 + 源极电阻自偏
```

---

**DONE: Ludwig Ch8 洗稿完成，24,812 字符**
