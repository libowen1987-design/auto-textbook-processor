---
chapter: 2
title: Transmission Line Analysis
source: Ludwig & Bogdanov, RF Circuit Design, 2nd Edition
pages: 51-112
---

# Chapter 2: Transmission Line Analysis | 第2章：传输线分析
# 第2章：传输线分析

## 2.1 Why Transmission Line Theory? | 传输线理论为何必要

> **Original:** Higher frequencies imply decreasing wavelengths. The consequence for an RF circuit is that voltages and currents no longer remain spatially uniform when compared to the geometric size of the discrete circuit elements: They have to be treated as propagating waves.

**【中文注释】** 频率越高，波长越短。当电磁波的波长与电路元件的物理尺寸可比拟时，电压和电流不再沿导线均匀分布——它们必须被当作传播的波来处理。这是从低频集总电路分析向高频分布电路理论过渡的核心原因。

---

### The 1.5 cm Wire Example | 1.5厘米导线的例子

Consider a simple circuit: sinusoidal voltage source $V_g$ with internal resistance $R_g$ connected to load $R_L$ by a 1.5 cm copper wire.

| Frequency | Wavelength $\lambda$ | Wire vs. $\lambda$ | Analysis Method |
|-----------|----------------------|---------------------|-----------------|
| 1 MHz | $\lambda = 94.86$ m | $l/\lambda \approx 0.016\%$ | Lumped (KVL valid) |
| 10 GHz | $\lambda = 0.949$ cm | $l/\lambda \approx 158\%$ | Transmission line required |

**Rule of thumb:** When average component size $l \geq \lambda/10$, transmission line theory must be applied ($l/\lambda \geq 0.1$).

**【中文注释】** 在1 MHz时，波长约95米，1.5厘米导线仅为波长的万分之一，电压沿线分布可以认为是均匀的，基尔霍夫定律完全适用。但在10 GHz时，波长不到1厘米，1.5厘米的导线已经超过了波长，此时导线上不同位置的电压和电流相位差异巨大，必须使用传输线理论。

---

### From Lumped to Distributed | 从集总到分布

When Kirchhoff's laws fail at RF, the solution is to **subdivide the line into infinitesimal segments** $\Delta z$, over each of which voltage and current can be assumed constant.

Each segment $\Delta z$ is modeled with:
- **Series resistance** $R$ per unit length (conductor losses)
- **Series inductance** $L$ per unit length (magnetic field energy)
- **Shunt capacitance** $C$ per unit length (electric field energy between conductors)
- **Shunt conductance** $G$ per unit length (dielectric losses)

This yields **distributed parameters** $R$, $L$, $C$, $G$ [per unit length], replacing the lumped $R$, $L$, $C$ of low-frequency theory.

**【中文注释】** 传输线理论的核心思想是将导线细分为无数个无限小的段$\Delta z$，在每一段上电压和电流仍然可以近似认为是"均匀"的（满足基尔霍夫定律成立的条件），但这些微段的等效电路包含四个分布参数：单位长度电阻$R$、电感$L$、电容$C$和电导$G$。这一处理方法连接了微观（麦克斯韦方程）和宏观（电路行为）。

---

## 2.2 Examples of Transmission Lines | 传输线类型

### 2.2.1 Two-Wire Lines | 双导线

Two parallel conductors separated by a fixed distance. **Major drawback:** Electric and magnetic field lines extend to infinity, causing:
- **High radiation loss** (acts as an antenna)
- **Interference** with nearby equipment

Applications: 50–60 Hz power lines, telephone connections (where $l \gg \lambda$, distributed effects still matter).

**【中文注释】** 双导线是最基本的传输线形式，但其开放的结构导致很强的电磁辐射，因此不适合射频应用。它主要用于工频电力传输和电话线路——在这些场合，频率足够低（波长足够长），辐射损失不是主要问题。

---

### 2.2.2 Coaxial Lines | 同轴线

**Structure:** Inner conductor (radius $a$) + outer cylindrical conductor (radius $b$) + dielectric medium in between. Usually the outer conductor is grounded.

**Advantages:**
- **Shielded** — fields confined between inner and outer conductor
- **Low radiation loss** — no external field interference
- **Low crosstalk** — isolated from neighboring lines

**Common dielectric materials:**

| Dielectric | $\varepsilon_r$ | $\tan \delta$ (at 10 GHz) |
|------------|-----------------|---------------------------|
| Polystyrene | 2.5 | 0.0003 |
| Polyethylene | 2.3 | 0.0004 |
| Teflon | 2.1 | 0.0004 |

**【中文注释】** 同轴线是射频应用中最常用的传输线类型。其结构将电磁场完全限制在内导体和外导体之间（外部为零），因此几乎没有辐射损失。常见的同轴电缆如RG-58（ polyethylene dielectric）用于测量设备，而半硬同轴电缆（semi-rigid coax）如UT-141则用于构建精密射频电路。

---

### 2.2.3 Microstrip Lines | 微带线

A **planar transmission line** formed by a conducting strip on a dielectric substrate above a ground plane.

**Advantages:**
- **PCB-compatible** — easy manufacturing
- **Low cost** — standard fabrication processes
- **Adjustable** — components can be repositioned and tuned

**Field leakage issue:** Single-layer PCBs suffer from field leakage and crosstalk. Higher $\varepsilon_r$ substrates (e.g., alumina, $\varepsilon_r = 10$) confine fields better than lower $\varepsilon_r$ (e.g., Teflon epoxy, $\varepsilon_r = 2.55$).

**Triple-layer (stripline):** Sandwiched between two ground planes → further reduced radiation loss.

**Parallel-plate line:** For high-power, low-impedance applications — two plates separated by dielectric.

**【中文注释】** 微带线是现代射频电路最常用的传输线形式，因为它可以直接在PCB上光刻制造。在选择基板材料时，高介电常数材料（如氧化铝，$\varepsilon_r = 10$）能够更好地将电磁场限制在介质内部，减少辐射损失和相邻走线间的串扰。但高$\varepsilon_r$材料也会导致微带线的特性阻抗更难控制，线宽更窄。

---

### TEM Mode | TEM模式

All three transmission line types above support **Transverse Electromagnetic (TEM)** mode — both $\mathbf{E}$ and $\mathbf{H}$ fields are perpendicular to the direction of propagation.

This contrasts with **TE** (Transverse Electric) and **TM** (Transverse Magnetic) modes found in waveguides and optical fibers, where field components exist along the propagation direction.

**【中文注释】** TEM模式是传输线中最常见的场分布形式——电场和磁场都横向于传播方向。在本书中，我们只讨论TEM模式，因为它允许我们使用简单的电路模型（$L$和$C$分布参数）来描述传输线行为。TE和TM模式需要更复杂的场论分析，主要用于微波和光通信（超出本书范围）。

---

## 2.3 Equivalent Circuit Representation | 等效电路表示

Each infinitesimal segment $\Delta z$ of a transmission line has the following lumped-parameter model:

| Parameter | Unit | Physical Meaning |
|-----------|------|------------------|
| $R$ | $\Omega$/m | Series resistance (conductor losses), both conductors |
| $L$ | H/m | Series inductance (magnetic field energy), includes mutual inductance |
| $C$ | F/m | Shunt capacitance (electric field energy between conductors) |
| $G$ | S/m | Shunt conductance (dielectric losses) |

**For a two-wire line:** Each conductor contributes $R_1, L_1$ and $R_2, L_2$, combined into single $R, L$.
**For a coaxial cable:** Inner and outer conductors both contribute to $R, L$.

**Key insight:** All parameters $R, L, C, G$ are **frequency-dependent** (as discussed in Chapter 1 — skin effect, dielectric loss tangent).

**【中文注释】** 等效电路模型将传输线的分布参数用集总元件 $R$、$L$、$C$、$G$ 来表示，每单位长度一组。注意这些参数本身是频率的函数——在高频下，导体的趋肤效应使 $R$ 增加，介质的损耗角正切使 $G$ 不为零（理想介质 $G = 0$）。

---

## 2.4 Theoretical Foundation | 理论基础

### 2.4.1 Basic Laws: Faraday's Law and Ampère's Law | 基本定律：法拉第定律与安培定律

The distributed parameters $R, L, C, G$ can be derived from the physical dimensions and material properties of the transmission line using **Faraday's law** and **Ampère's law** — two fundamental electromagnetic laws underlying Maxwell's equations.

**【中文注释】** 传输线的电路参数可以从电磁学基本定律推导出来。法拉第定律说明了时变磁场如何产生电场（感应电压），安培定律说明了电流如何产生磁场。这两个定律共同描述了电磁波在传输线中的传播行为。

---

#### Ampère's Law | 安培定律

**Integral form:**
$$\oint_C \mathbf{H} \cdot d\mathbf{l} = I_{\text{enc}} = \int_S \mathbf{J} \cdot d\mathbf{S}$$

The line integral of magnetic field $\mathbf{H}$ around a closed loop equals the total enclosed current.

**Differential (point) form:**
$$\nabla \times \mathbf{H} = \mathbf{J}$$

The curl of $\mathbf{H}$ equals the current density $\mathbf{J}$.

**Total current density:** $\mathbf{J} = \mathbf{J}_0 + \sigma_{\text{cond}}\mathbf{E} + \varepsilon\frac{\partial\mathbf{E}}{\partial t}$
- $\mathbf{J}_0$ — impressed source current
- $\sigma_{\text{cond}}\mathbf{E}$ — conduction current (conductor losses)
- $\varepsilon\frac{\partial\mathbf{E}}{\partial t}$ — displacement current (radiation losses)

**【中文注释】** 安培定律将电流与磁场联系起来。在传输线分析中，它用于推导单位长度电感$L$。积分形式表明，环绕导线的磁场环路积分等于穿过该环路的总电流；微分形式则描述了空间中每一点的磁场旋度等于该点的电流密度。

---

#### Example 2-1: Magnetic Field of a Current-Carrying Wire | 例2-1：载流导线的磁场

**Problem:** Plot $H(r)$ inside and outside an infinitely long wire (radius $a = 5$ mm, current $I = 5$ A) in air.

**Solution:**

Inside the conductor ($0 \leq r \leq a$), current density is uniform: $J = I/(\pi a^2)$.

Applying Ampère's law:

$$H(2\pi r) = \frac{I r}{a^2} \quad \Rightarrow \quad H(r) = \frac{I r}{2\pi a^2}$$

Outside the conductor ($r \geq a$), all current is enclosed:

$$H(2\pi r) = I \quad \Rightarrow \quad H(r) = \frac{I}{2\pi r}$$

**Result:** Inside the wire, $H$ increases linearly with $r$ (more current contributing to the field). Outside, $H$ decays as $1/r$.

**【中文注释】** 这个例子展示了安培定律在轴对称几何中的直接应用。在导体内部，磁场随半径线性增长（因为距离圆心越远，包含的电流越多）；在导体外部，磁场随半径按$1/r$衰减。这个结果对于理解传输线的电感计算非常重要。

---

#### Faraday's Law | 法拉第定律

**Integral form:**
$$\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt}\int_S \mathbf{B} \cdot d\mathbf{S} = -\frac{d\Phi_B}{dt}$$

The line integral of electric field around a closed loop equals the negative rate of change of magnetic flux through the loop.

**【中文注释】** 法拉第定律表明，时变磁场会在闭合路径上感应出电动势。这是变压器原理的基础，也是传输线分布电感$L$如何与电压耦合的原因。当沿传输线的磁通量变化时，会产生感应电压（楞次定律的体现）。

---

#### Example 2-2: Induced Voltage in a Wire Loop | 例2-2：导线回路中的感应电压

**Problem:** Find the induced voltage in a thin wire loop ($a = 5$ mm) in air with $H = H_0\cos(\omega t)$, $H_0 = 5$ A/m, $f = 100$ MHz.

**Solution:**

$$V = -\frac{d\Phi_B}{dt} = -\frac{d}{dt}\left(\mu_0 H_0 \cos(\omega t) \cdot \pi a^2\right) = \omega \mu_0 H_0 \pi a^2 \sin(\omega t)$$

At $f = 100$ MHz: $V \approx -0.31 \sin(6.28 \times 10^8 t)$ V.

**【中文注释】** 这个例子展示了法拉第定律的"变压器形式"——时变磁场在次级线圈中感应电压。注意感应电压与频率成正比——在高频下，即使较小的磁通变化率也能产生显著的感应电压。这是高频传输线设计中必须考虑互感效应的根本原因。

---

## 2.5 Circuit Parameters for a Parallel-Plate Transmission Line | 平行板传输线的电路参数

### Derivation Summary | 推导概要

For a parallel-plate line with plate width $w$, plate separation $d$, dielectric constant $\varepsilon_r$, conductor conductivity $\sigma_{\text{cond}}$, dielectric conductivity $\sigma_{\text{diel}}$:

**Assumptions:**
- $w \gg d$ (one-dimensional analysis valid)
- Skin depth $\delta \ll$ plate thickness $d_p$ (high-frequency condition)

### Resistance per unit length | 单位长度电阻

$$R_s = \frac{1}{\sigma_{\text{cond}} w \delta} \quad \text{(surface resistance per plate)}$$

Total $R = 2R_s$ (two plates):

$$\boxed{R = \frac{2}{\sigma_{\text{cond}} w \delta} \quad [\Omega/\text{m}]} \tag{2.21}$$

### Inductance per unit length | 单位长度电感

**Skin-effect self-inductance** per plate:

$$L_s = \frac{1}{\sigma_{\text{cond}} \omega \mu \delta^2} = \frac{\delta}{\sigma_{\text{cond}} w \delta^2} = \frac{1}{w \sigma_{\text{cond}} \omega \mu \delta}$$

Total $L_s = 2L_s'$ (two plates). Usually $L_s \ll L_{\text{mutual}}$, so often neglected.

**Mutual inductance** between plates:

$$\boxed{L = \frac{\mu d}{w} \quad \text{[H/m]}} \tag{2.24}$$

### Capacitance per unit length | 单位长度电容

$$\boxed{C = \frac{\varepsilon w}{d} = \frac{\varepsilon_0 \varepsilon_r w}{d} \quad \text{[F/m]}} \tag{2.23}$$

### Conductance per unit length | 单位长度电导

$$\boxed{G = \frac{\sigma_{\text{diel}} w}{d} \quad \text{[S/m]}} \tag{2.25}$$

### Summary Table | 参数汇总表

| Parameter | Formula | Unit |
|-----------|---------|------|
| $R$ | $2/(\sigma_{\text{cond}} w \delta)$ | $\Omega$/m |
| $L_s$ | $2/(\sigma_{\text{cond}} w \omega \mu \delta)$ | H/m |
| $L$ (mutual) | $\mu d/w$ | H/m |
| $C$ | $\varepsilon w/d$ | F/m |
| $G$ | $\sigma_{\text{diel}} w/d$ | S/m |

**【中文注释】** 平行板传输线是分析其他传输线结构的基础。通过法拉第定律和安培定律，我们可以推导出每个分布参数的解析表达式。注意单位长度电容$C$和电感$L$只与几何尺寸和材料参数有关，而电阻$R$和电导$G$还与频率有关（通过$\delta$和$\sigma_{\text{diel}}$）。

---

### Example 2-3: Parallel-Plate Line Parameters at 1 GHz | 例2-3：1 GHz平行板传输线参数

**Given:** $w = 6$ mm, $d = 1$ mm, $\varepsilon_r = 2.25$, $\sigma_{\text{diel}} = 0.125$ mS/m, $f = 1$ GHz, copper ($\sigma_{\text{cond}} = 64.516 \times 10^6$ S/m).

**Solution:**

Skin depth: $\delta = 1/\sqrt{\pi f \mu_0 \sigma_{\text{cond}}} = 1.98\,\mu\text{m}$ (assumed $\ll d_p$)

$$R = \frac{2}{\sigma_{\text{cond}} w \delta} = \frac{2}{64.516 \times 10^6 \times 6 \times 10^{-3} \times 1.98 \times 10^{-6}} \approx 2.6\,\Omega/\text{m}$$

$$L_s = \frac{2}{w \sigma_{\text{cond}} \omega \mu_0 \delta} \approx 0.42 \text{ nH/m}$$

$$L = \frac{\mu_0 d}{w} \approx 209.4 \text{ nH/m} \quad \text{(dominant)}$$

$$C = \frac{\varepsilon_0 \varepsilon_r w}{d} = \frac{8.854 \times 10^{-12} \times 2.25 \times 6 \times 10^{-3}}{10^{-3}} \approx 119.5 \text{ pF/m}$$

$$G = \frac{\sigma_{\text{diel}} w}{d} = \frac{0.125 \times 10^{-3} \times 6 \times 10^{-3}}{10^{-3}} = 0.75 \text{ mS/m}$$

**Key observation:** $L_s \ll L$ — the skin-effect inductance is negligible compared to mutual inductance, so $L \approx 209.4$ nH/m is the dominant inductance.

**【中文注释】** 这个例子展示了在1 GHz频率下各参数的计算过程。集肤深度仅为1.98 \mum（非常小），导致单位长度电阻达到2.6 Ω/m。互感电感（209.4 nH/m）远大于集肤效应自感（0.42 nH/m），因此在实际计算中通常忽略$L_s$。电容约119.5 pF/m，电导0.75 mS/m（介质不是理想绝缘体）。

---

## 2.7 General Transmission Line Equations | 通用传输线方程

### 2.7.1 Kirchhoff Voltage and Current Law Representations | 基尔霍夫电压和电流定律表示

Applying KVL to the loop in Fig 2-17:

$$(R + j\omega L)I(z)\Delta z + V(z + \Delta z) = V(z)$$

$$\Rightarrow \frac{dV}{dz} = -(R + j\omega L)I(z) \tag{2.28}$$

Applying KCL to node $a$:

$$I(z) - V(z+\Delta z)(G + j\omega C)\Delta z = I(z + \Delta z)$$

$$\Rightarrow \frac{dI}{dz} = -(G + j\omega C)V(z) \tag{2.30}$$

These are **coupled first-order differential equations** describing voltage and current waves on a transmission line.

**【中文注释】** 这两个方程是传输线理论的基石。通过对传输线的微分段应用基尔霍夫定律，我们得到了耦合的一阶微分方程——电压对$z$的导数与电流成正比，电流对$z$的导数与电压成正比。求解这些方程将揭示传输线上的波动行为。

---

### 2.7.2 Traveling Voltage and Current Waves | 传播的电压和电流波

Decoupling (2.28) and (2.30) yields the **wave equation**:

$$\frac{d^2V}{dz^2} = \gamma^2 V \quad \text{where} \quad \gamma = \alpha + j\beta = \sqrt{(R + j\omega L)(G + j\omega C)} \tag{2.32}$$

$\gamma$ is the **complex propagation constant**:
- $\alpha$ — attenuation constant [Np/m]
- $\beta$ — phase constant [rad/m]

The general solution:

$$V(z) = V^+ e^{-\gamma z} + V^- e^{+\gamma z} \tag{2.34}$$

$$I(z) = \frac{V^+}{Z_0} e^{-\gamma z} - \frac{V^-}{Z_0} e^{+\gamma z} \tag{2.35}$$

- **First term:** Wave propagating in $+z$ direction (forward wave)
- **Second term:** Wave propagating in $-z$ direction (reflected wave)

**【中文注释】** 波动方程的解包含两个指数项——一个代表沿$+z$方向传播的前向波，另一个代表沿$-z$方向传播的反射波。复数传播常数$\gamma$的实部$\alpha$描述波的衰减，虚部$\beta$描述相位随距离的变化。这与第1章中讨论的平面波传播常数$\beta = 2\pi/\lambda$本质上是相同的。

---

### 2.7.3 Characteristic Impedance | 特性阻抗

From (2.34)–(2.35), the **characteristic impedance** $Z_0$ is defined as the ratio of forward voltage and current waves:

$$\boxed{Z_0 = \sqrt{\frac{R + j\omega L}{G + j\omega C}} \quad [\Omega]} \tag{2.37}$$

**Physical meaning:** $Z_0$ is the impedance seen at any point on an infinite (or matched) transmission line — it is the "intrinsic" impedance of the line itself, not a circuit impedance in the conventional sense.

**【中文注释】** 特性阻抗$Z_0$是传输线最重要的参数之一。它定义为前向电压波与前向电流波的比值（即$V^+/I^+$）。对于无限长的传输线，从任何位置看进去的输入阻抗都等于$Z_0$。$Z_0$取决于传输线的物理结构（$L$和$C$）和频率（通过$R$、$G$的频率依赖性）。

---

### 2.7.4 Lossless Transmission Line Model | 无耗传输线模型

For **lossless line**: $R = G = 0$

$$\boxed{Z_0 = \sqrt{\frac{L}{C}} \quad \text{(real, frequency-independent)}} \tag{2.38}$$

For parallel-plate line:

$$Z_0 = \sqrt{\frac{\mu d}{w}} \cdot \sqrt{\frac{1}{\varepsilon}} = \frac{d}{w}\sqrt{\frac{\mu}{\varepsilon}} = \frac{d}{w} \cdot \frac{\eta}{\sqrt{\varepsilon_r}}$$

where $\eta = \sqrt{\mu_0/\varepsilon_0} \approx 377\,\Omega$ is the intrinsic impedance of free space.

**Important:** For lossless line, $Z_0$ is **purely real** and **independent of frequency** — a fundamental simplification that makes lossless lines much easier to analyze.

**【中文注释】** 在无耗条件下（理想导体、无介质损耗），$Z_0$是实数且与频率无关。这大大简化了射频电路的分析。对于平行板传输线，$Z_0$与几何尺寸比$d/w$成正比——板间距$d$越大或板宽$w$越小，特性阻抗越高。

---

## 2.8 Microstrip Transmission Lines | 微带传输线

Microstrip lines on PCBs are not purely TEM — the substrate causes partial field containment. However, for most RF applications (up to ~30 GHz), a **quasi-TEM approximation** is valid.

### Quasi-TEM Behavior | 准TEM行为

In a microstrip, the wave does not travel purely in the dielectric — part of the field is in air above the substrate. This creates:
- **Effective dielectric constant** $\varepsilon_{\text{eff}}$ (weighted average between substrate $\varepsilon_r$ and air)
- **Velocity of propagation** $v = c/\sqrt{\varepsilon_{\text{eff}}}$

$$\varepsilon_{\text{eff}} = \frac{\varepsilon_r + 1}{2} + \frac{\varepsilon_r - 1}{2}\frac{1}{\sqrt{1 + 12d/w}} \tag{2.??}$$

where $d$ = substrate thickness, $w$ = strip width.

### Characteristic Impedance of Microstrip | 微带线特性阻抗

For a microstrip on substrate with $\varepsilon_r$, the characteristic impedance depends on $w/d$ ratio:

$$Z_0 = \frac{60}{\sqrt{\varepsilon_{\text{eff}}}} \ln\left(\frac{8d}{w} + \frac{w}{4d}\right) \quad \text{for } w/d \leq 1$$

$$Z_0 = \frac{120\pi}{\sqrt{\varepsilon_{\text{eff}}}\left[\frac{w}{d} + 1.393 + 0.667\ln\left(\frac{w}{d} + 1.444\right)\right]} \quad \text{for } w/d \geq 1$$

**【中文注释】** 微带线的特性阻抗取决于导体宽度$w$与介质厚度$d$的比值，以及基片的相对介电常数$\varepsilon_r$。设计微带线时，通常先确定目标特性阻抗（如50 Ω），然后根据所选基片的$\varepsilon_r$和厚度$d$计算出所需的导体宽度$w$。

---

### Example 2-5: Microstrip Line Design | 例2-5：微带线设计

Design a 50 Ω microstrip line on a Teflon substrate ($\varepsilon_r = 2.55$, $d = 1.5$ mm).

**Solution:**

For $Z_0 = 50\,\Omega$, solving the impedance equation yields a specific $w/d$ ratio. Using the quasi-TEM formulas:

$$\varepsilon_{\text{eff}} \approx \frac{2.55 + 1}{2} + \frac{2.55 - 1}{2} \cdot \frac{1}{\sqrt{1 + 12/(w/d)}} \approx 1.95$$

For $Z_0 = 50\,\Omega$, the required $w/d \approx 1.8$, so $w \approx 2.7$ mm.

**Key insight:** Higher $\varepsilon_r$ substrates allow **smaller $w/d$ ratios** for the same impedance — enabling more compact circuits.

**【中文注释】** 微带线设计的核心是根据目标特性阻抗（通常为50 Ω）和基片参数（$\varepsilon_r$、$d$）确定导体宽度$w$。在实际设计中，可以使用商业软件（如ADS、HFSS）或查表来快速得到$w$值。高介电常数基片（如 alumina）允许更窄的走线，从而实现更紧凑的电路布局。

---

## 2.9 Terminated Lossless Transmission Line | 端接无耗传输线

### Voltage Reflection Coefficient | 电压反射系数

When a wave traveling on a transmission line encounters a load $Z_L \neq Z_0$, part of the wave is reflected.

$$\boxed{\Gamma = \frac{V^-}{V^+} = \frac{Z_L - Z_0}{Z_L + Z_0}} \tag{2.64}$$

- $\Gamma = 0$: $Z_L = Z_0$ — **perfect match**, no reflection
- $\Gamma = +1$: $Z_L \to \infty$ — **open circuit**
- $\Gamma = -1$: $Z_L = 0$ — **short circuit**
- $|\Gamma| < 1$: Partial reflection (matched load absorbs some energy)

**Standing wave ratio (SWR / VSWR):**

$$\boxed{\text{VSWR} = \frac{1 + |\Gamma|}{1 - |\Gamma|} \geq 1}$$

**【中文注释】** 反射系数$\Gamma$描述了负载端反射波与入射波的比值。当$Z_L = Z_0$时，$\Gamma = 0$，没有反射——这是射频系统的理想目标（阻抗匹配）。当负载开路（$Z_L \to \infty$）时，$\Gamma = +1$，全反射且相位同向；当负载短路（$Z_L = 0$）时，$\Gamma = -1$，全反射且相位反向。驻波比（VSWR）是衡量匹配质量的另一个常用指标。

---

### Input Impedance of Terminated Lossless Line | 端接无耗线的输入阻抗

The input impedance at a distance $d$ from the load:

$$\boxed{Z_{\text{in}}(d) = Z_0 \frac{1 + \Gamma e^{-j2\beta d}}{1 - \Gamma e^{-j2\beta d}} = Z_0 \frac{Z_L + jZ_0 \tan(\beta d)}{Z_0 + jZ_L \tan(\beta d)}} \tag{2.68}$$

where $\beta = 2\pi/\lambda$ for lossless line.

**【中文注释】** 这个公式是传输线理论中最重要的公式之一。它表明距离负载$d$处的输入阻抗取决于：特性阻抗$Z_0$、负载阻抗$Z_L$、以及电长度$\beta d$（或等价的$d/\lambda$）。通过调整$d$，可以在特定频率下将任意负载阻抗变换为任意期望的输入阻抗——这是阻抗匹配的基础。

---

## 2.10 Special Termination Conditions | 特殊端接条件

### 2.10.2 Short-Circuit Transmission Line | 短路传输线

For $Z_L = 0$, $\Gamma = -1$:

$$Z_{\text{in}}(d) = j Z_0 \tan(\beta d) \tag{2.72}$$

| $\beta d$ | $Z_{\text{in}}$ | Behavior |
|-----------|----------------|----------|
| $0$ | $0$ | Short |
| $\lambda/8$ | $jZ_0$ | Pure inductor |
| $\lambda/4$ | $\infty$ (open) | Resonant |
| $\lambda/2$ | $0$ (short) | Resonant |
| $3\lambda/8$ | $-jZ_0$ | Pure capacitor |

**Applications:** Stub tuners, resonant circuits, bias networks (RFCs).

**【中文注释】** 短路传输线的输入阻抗完全由电长度决定——在不同长度下，它可以从短路（0）变到开路（无限大），中间呈现纯感性或纯容性。这使得短路传输线成为可调电抗元件的基础。例如，$\lambda/4$短路线表现为开路，可用于射频扼流圈（RFC）——对射频开路，对直流短路。

---

### 2.10.3 Open-Circuit Transmission Line | 开路传输线

For $Z_L \to \infty$, $\Gamma = +1$:

$$Z_{\text{in}}(d) = -j \frac{Z_0}{\tan(\beta d)} \tag{2.65}$$

| $\beta d$ | $Z_{\text{in}}$ | Behavior |
|-----------|----------------|----------|
| $0$ | $\infty$ (open) | Open |
| $\lambda/8$ | $-jZ_0$ | Pure capacitor |
| $\lambda/4$ | $0$ (short) | Resonant |
| $\lambda/2$ | $\infty$ (open) | Resonant |

**【中文注释】** 开路传输线的行为与短路传输线互补——$\lambda/4$开路线表现为短路，$\lambda/2$开路线表现为开路。开路短截线（open-circuited stubs）常用于微带电路中的阻抗匹配和滤波。

---

### Example 2-6: Short-Circuit Transmission Line | 例2-6：短路传输线

**Problem:** Find input impedance of a 50 Ω short-circuited line at $f = 10$ GHz with $d = 3$ mm. (For PTFE: $\varepsilon_r = 2.25$, $v \approx 2 \times 10^8$ m/s → $\lambda \approx 2$ cm at 10 GHz)

**Solution:**

$$\beta = \frac{2\pi}{\lambda} = \frac{2\pi}{0.02} = 314 \text{ rad/m}$$

$$\beta d = 314 \times 0.003 = 0.942 \text{ rad} \approx 54^\circ$$

$$Z_{\text{in}} = j 50 \tan(54^\circ) = j 50 \times 1.376 = j68.8\,\Omega$$

**Result:** The shorted line behaves as a **68.8 Ω inductive reactance**.

**【中文注释】** 这个例子展示了如何计算短路传输线的输入阻抗。当线长为$\lambda/10$（约54°）时，短路线表现为感性电抗。在设计匹配网络时，可以选择合适的长度使传输线提供所需的电抗值。

---

### Example 2-7: Open-Circuit Transmission Line | 例2-7：开路传输线

**Problem:** Same parameters as Example 2-6 but with open circuit.

**Solution:**

$$Z_{\text{in}} = -j \frac{Z_0}{\tan(\beta d)} = -j \frac{50}{\tan(54^\circ)} = -j \frac{50}{1.376} = -j36.4\,\Omega$$

**Result:** The open line behaves as a **36.4 Ω capacitive reactance**.

**【中文注释】** 开路线的行为与短路线互补——相同的电长度（$\beta d \approx 54°$）下，开路线表现为容性电抗（-j36.4 Ω）而短路线表现为感性电抗（+j68.8 Ω）。这种互补关系在设计stub匹配网络时非常有用。

---

### 2.10.4 Quarter-Wave Transformer | 四分之一波长变压器

For $d = \lambda/4$ ($\beta d = \pi/2$, $\tan(\beta d) \to \infty$):

$$Z_{\text{in}} = \frac{Z_0^2}{Z_L} \tag{2.82}$$

**Key application: Impedance matching** — a $\lambda/4$ line of appropriate $Z_0$ can transform any load $Z_L$ to any desired $Z_{\text{in}}$.

**Design formula:**

$$\boxed{Z_0 = \sqrt{Z_{\text{in}} \cdot Z_L}}$$

**Example:** Match a $100\,\Omega$ load to a $50\,\Omega$ line: $Z_0 = \sqrt{50 \times 100} = 70.7\,\Omega$.

**【中文注释】** $\lambda/4$传输线是一种经典的阻抗变换器。它利用了传输线阻抗随长度周期性变化（周期为$\lambda/2$）的特性——在$\lambda/4$处，负载阻抗被"翻转为"其倒数形式（乘以$Z_0^2/Z_L$）。通过选择合适的特性阻抗$Z_0$，可以将任意负载阻抗变换为任意目标输入阻抗。$\lambda/4$变压器是窄带匹配的首选方案。

---

### Example 2-8: Impedance Matching via $\lambda/4$ Transformer | 例2-8：$\lambda/4$变压器阻抗匹配

**Problem:** Match a $75\,\Omega$ antenna to a $50\,\Omega$ transmission line at $f = 1$ GHz using a $\lambda/4$ transformer. Find required $Z_0$ and physical length (PTFE, $\varepsilon_r = 2.25$).

**Solution:**

$$Z_0 = \sqrt{Z_{\text{line}} \cdot Z_L} = \sqrt{50 \times 75} = 61.2\,\Omega$$

Wavelength in PTFE: $\lambda = \frac{c}{f\sqrt{\varepsilon_r}} = \frac{3 \times 10^8}{1 \times 10^9 \times \sqrt{2.25}} = \frac{300}{1.5} = 20 \text{ cm}$

$$\lambda/4 = 5 \text{ cm}$$

**Result:** A 5 cm long line with $Z_0 = 61.2\,\Omega$ provides perfect match at 1 GHz.

**【中文注释】** $\lambda/4$变压器的物理长度取决于工作频率和介质材料。在PTFE（$\varepsilon_r = 2.25$）中，波长缩短为空气中的$1/\sqrt{\varepsilon_r}$，因此$\lambda/4 = 5$ cm。设计时需要根据介质的有效介电常数计算正确的物理长度。

---

## 2.11 Sourced and Loaded Transmission Line | 源端与负载端传输线

### 2.11.1 Phasor Representation of Source | 源的相量表示

A voltage source $V_g$ with internal impedance $Z_g = R_g + jX_g$ connected to a line with characteristic impedance $Z_0$:

**Reflection coefficient at source:**

$$\Gamma_g = \frac{Z_g - Z_0}{Z_g + Z_0}$$

**Total input impedance at line input:**

$$Z_{\text{in}} = Z_0 \frac{1 + \Gamma_{\text{ref}}}{1 - \Gamma_{\text{ref}}}$$

where $\Gamma_{\text{ref}} = \Gamma e^{-j2\beta l}$ is the reflection coefficient seen looking toward the load, reflected back to the input.

**【中文注释】** 当源阻抗与传输线特性阻抗不匹配时，信号不仅在负载端反射，还会在源端再次反射。这种双重反射在传输线上形成多个来回的波。当源阻抗也是$Z_0$时（$\Gamma_g = 0$），没有额外的源端反射——这是实现最大功率传输的条件之一。

---

### Example 2-9: Transmission Coefficient | 例2-9：传输系数

**Problem:** A 50 Ω source with $V_g = 1$ V connects to a 50 Ω line terminated in $Z_L = 100\,\Omega$. Find the transmission coefficient to the load.

**Solution:**

Load reflection: $\Gamma_L = \frac{100 - 50}{100 + 50} = \frac{1}{3} \approx 0.333$

Source match: $\Gamma_g = 0$ (50 Ω source = line impedance)

At load: $V_{\text{load}} = V^+(1 + \Gamma_L) = V^+ \times 1.333$

Since $V^+$ is the incident wave from source: $V^+ = \frac{V_g}{2} = 0.5$ V (for matched source)

$$V_{\text{load}} = 0.5 \times 1.333 = 0.667 \text{ V}$$

**【中文注释】** 传输系数描述了从源端到负载端的电压传输。在这个例子中，由于$Z_L = 100\,\Omega \neq Z_0 = 50\,\Omega$，存在33.3%的反射系数。负载端的电压是入射波的1.333倍（因为反射波同相叠加）。

---

### 2.11.2 Power Considerations | 功率关系

**Instantaneous power:**

$$P(z) = \frac{|V(z)|^2}{2Z_0} \quad \text{(for matched load)}$$

**Forward (incident) power:**

$$P^+ = \frac{|V^+|^2}{2Z_0}$$

**Reflected power:**

$$P^- = \frac{|V^-|^2}{2Z_0} = |\Gamma|^2 P^+$$

**Power delivered to load:**

$$P_{\text{load}} = P^+ - P^- = P^+(1 - |\Gamma|^2) = \frac{|V^+|^2}{2Z_0}(1 - |\Gamma|^2) \tag{2.93}$$

**Maximum power transfer:** Occurs when $Z_g = Z_0^*$ (complex conjugate match) — this ensures no reflection from source.

**【中文注释】** 功率传输理论表明，只有当负载与源完全匹配时，才能实现最大功率传输。反射功率$P^- = |\Gamma|^2 P^+$表示被负载反射回来的那部分功率。负载实际接收的功率是入射功率乘以$(1 - |\Gamma|^2)$。

---

### Example 2-10: Power Considerations | 例2-10：传输线功率关系

**Problem:** A 50 Ω line carries $V^+ = 1$ V. Load has $\Gamma = 0.5 \angle 0°$. Find forward, reflected, and delivered power.

**Solution:**

$$P^+ = \frac{|1|^2}{2 \times 50} = 10 \text{ mW}$$

$$P^- = |\Gamma|^2 P^+ = 0.25 \times 10 = 2.5 \text{ mW}$$

$$P_{\text{load}} = P^+ - P^- = 10 - 2.5 = 7.5 \text{ mW} = 0.75 P^+$$

**Verification:** $P_{\text{load}} = \frac{|V^+|^2}{2Z_0}(1 - |\Gamma|^2) = 10 \times (1 - 0.25) = 7.5$ mW ✓

**【中文注释】** 当反射系数$\Gamma = 0.5$时，25%的功率被反射回去，75%的功率被负载吸收。在理想匹配（$\Gamma = 0$）情况下，所有功率都被负载吸收。

---

### 2.11.3 Input Impedance Matching | 输入阻抗匹配

Goal: Maximize power transfer from source to load by making $Z_{\text{in}} = Z_g^*$.

**Common matching techniques:**
1. **$\lambda/4$ transformer** — narrowband, as discussed in Section 2.10.4
2. **Single-stub tuning** — uses a shunt (or series) open/short-circuited stub at a specific position
3. **Double-stub tuning** — more flexible, less position-dependent
4. **L-network matching** — lumped element L-section matching (discussed in Ch 8)
5. **Transformer matching** — using coupled inductors or transmission line transformers

**【中文注释】** 阻抗匹配是射频电路设计的核心目标。不匹配会导致功率反射、效率降低以及系统性能下降。常用的匹配技术包括：$\lambda/4$变压器（窄带）、短截线调谐（stub tuning）、双短截线调谐、以及L网络匹配（使用集总电感电容）。具体选择取决于工作频率、带宽要求和实现复杂度。

---

### 2.11.4 Return Loss and Insertion Loss | 回波损耗与插入损耗

**Return Loss (RL):** Measures power reflected due to mismatch:

$$\boxed{\text{RL} = -20\log_{10}|\Gamma| \quad \text{[dB]}} \tag{2.89}$$

| $|\Gamma|$ | Return Loss |
|------------|-------------|
| 0 (perfect match) | $\infty$ dB |
| 0.1 | 20 dB |
| 0.316 | 10 dB |
| 1.0 (full reflection) | 0 dB |

**Insertion Loss (IL):** Measures power loss through the network:

$$\boxed{\text{IL} = -10\log_{10}\frac{P_{\text{load}}}{P_{\text{available}}} \quad \text{[dB]}} \tag{2.106}$$

For a perfectly matched network: $\text{IL} = 0$ dB. Typical RL targets: $\geq 10$ dB for general RF, $\geq 20$ dB for precision systems.

**【中文注释】** 回波损耗（RL）和插入损耗（IL）是衡量射频网络匹配质量的两个关键参数。RL描述了由于阻抗失配而反射回去的功率（负dB值，越负越好）；IL描述了信号通过传输网络时的功率损耗。在射频系统中，通常要求RL ≥ 10 dB（反射功率≤ 10%）用于一般应用，RL ≥ 20 dB（反射功率≤ 1%）用于精密系统。

---

### Example 2-11: Return Loss | 例2-11：回波损耗

**Problem:** A transmission line section with $Z_0 = 50\,\Omega$ has load $Z_L = 30 + j10\,\Omega$. Find return loss.

**Solution:**

$$\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0} = \frac{(30 + j10) - 50}{(30 + j10) + 50} = \frac{-20 + j10}{80 + j10}$$

$$|\Gamma| = \frac{\sqrt{(-20)^2 + 10^2}}{\sqrt{80^2 + 10^2}} = \frac{\sqrt{500}}{10\sqrt{65}} = \frac{22.36}{80.62} \approx 0.277$$

$$\text{RL} = -20\log_{10}(0.277) = -20 \times (-0.557) = 11.1 \text{ dB}$$

**Result:** RL = 11.1 dB — acceptable for many RF applications (≥ 10 dB typical threshold).

**【中文注释】** 负载阻抗$Z_L = 30 + j10\,\Omega$与50 Ω特性阻抗不完全匹配，导致约11.1 dB的回波损耗。这意味着约7.7%的功率被反射回去（计算：$10^{-11.1/20} \approx 0.277$）。

---

## 2.12 Summary | 本章小结

### Key Concepts | 核心概念

1. **Transmission line theory** replaces lumped circuit analysis when $l \geq \lambda/10$
2. **Distributed parameters** $R$, $L$, $C$, $G$ per unit length fully characterize a transmission line
3. **Telegrapher's equations** — coupled first-order differential equations for $V(z)$ and $I(z)$
4. **Wave equation** — second-order ODE with traveling wave solutions
5. **Characteristic impedance** $Z_0 = \sqrt{(R+j\omega L)/(G+j\omega C)}$; for lossless line: $Z_0 = \sqrt{L/C}$ (real)
6. **Reflection coefficient** $\Gamma = (Z_L - Z_0)/(Z_L + Z_0)$
7. **Input impedance** of terminated line: $Z_{\text{in}}(d) = Z_0\frac{Z_L + jZ_0\tan(\beta d)}{Z_0 + jZ_L\tan(\beta d)}$
8. **Special cases:** Short-circuited line: $Z_{\text{in}} = jZ_0\tan(\beta d)$; Open-circuited line: $Z_{\text{in}} = -jZ_0/\tan(\beta d)$
9. **$\lambda/4$ transformer:** $Z_0 = \sqrt{Z_{\text{in}} \cdot Z_L}$ for impedance matching
10. **Return loss** RL = $-20\log_{10}|\Gamma|$ [dB]; **Insertion loss** measures power dissipated in network

### Key Equations | 核心公式

$$\boxed{\gamma = \alpha + j\beta = \sqrt{(R + j\omega L)(G + j\omega C)}}$$

$$\boxed{Z_0 = \sqrt{\frac{R + j\omega L}{G + j\omega C}}}$$

$$\boxed{\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0}}$$

$$\boxed{Z_{\text{in}}(d) = Z_0 \frac{1 + \Gamma e^{-j2\beta d}}{1 - \Gamma e^{-j2\beta d}}}$$

$$\boxed{Z_{\text{in}} = jZ_0\tan(\beta d) \quad \text{(short circuit)}}$$

$$\boxed{Z_{\text{in}} = -j\frac{Z_0}{\tan(\beta d)} \quad \text{(open circuit)}}$$

$$\boxed{Z_{\text{in}} = \frac{Z_0^2}{Z_L} \quad \text{(}\lambda/4\text{ line)}}$$

$$\boxed{\text{RL} = -20\log_{10}|\Gamma| \text{ [dB]}}$$

**【中文注释】** 本章建立了传输线理论的基础。从麦克斯韦方程出发，推导出了描述传输线上电压和电流波传播的方程。关键结果包括：特性阻抗$Z_0$的定义、反射系数$\Gamma$的计算、以及输入阻抗随位置变化的公式。这些结果将在第3章（史密斯圆图）和后续各章中反复运用，是整个射频电路设计的理论基础。