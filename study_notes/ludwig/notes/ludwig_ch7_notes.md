# Chapter 7: Active RF Component Modeling | 第7章：有源射频器件建模
# 第7章：有源RF器件建模

> **本章简介 / Chapter Overview**  
> 本章将第6章的物理器件知识转化为可在CAD工具中使用的电路模型。重点建立二极管的大信号/小信号模型、双极晶体管的Ebers-Moll和Gummel-Poon大信号模型，以及Hybrid-π小信号模型。最后给出FET的大信号和小信号模型，以及模型参数提取的实验方法。

---

## 7.1 Diode Models | 二极管模型

### 7.1.1 Nonlinear Diode Model (Large-Signal) | 非线性二极管模型（大信号）

#### Large-Signal Circuit Model | 大信号电路模型

The large-signal diode model consists of:
- **Series resistance** $R_S$: accounts for semiconductor bulk resistance and contact resistance
- **Junction capacitance** $C_j$: voltage-dependent depletion capacitance
- **Diffusion capacitance** $C_d$: minority carrier storage effect (dominant in forward bias)

大信号二极管模型包括：
- **串联电阻** $R_S$：半导体体电阻和接触电阻
- **结电容** $C_j$：电压相关的耗尽电容
- **扩散电容** $C_d$：少子存储效应（正向偏置时主导）

The **junction capacitance** is:
**结电容**为：

$$C_j = \frac{C_0}{\left(1 - \frac{V}{V_{\text{bi}}}\right)^m}$$

where $m = 0.5$ for abrupt junction, $m = 0.33$ for linearly graded junction.

其中 $m = 0.5$（突变结），$m = 0.33$（线性缓变结）。

The **diffusion capacitance** (dominant in forward bias) is:
**扩散电容**（正向偏置时主导）为：

$$C_d = \frac{\tau_T I_Q}{V_T}\exp\left(\frac{V}{V_T}\right) \approx \frac{\tau_T I_Q}{V_T}$$

where $\tau_T$ is the carrier transit time and $I_Q$ is the quiescent current.

其中 $\tau_T$ 是载流子渡越时间，$I_Q$ 是静态电流。

#### Temperature Dependence of the Saturation Current | 饱和电流的温度依赖性

The reverse saturation current $I_S$ has strong temperature dependence:
反向饱和电流 $I_S$ 具有强温度依赖性：

$$I_S(T) = I_S(T_0)\left(\frac{T}{T_0}\right)^{n_i^2 \text{-exponent}} \exp\left[-\frac{q}{V_T}\left(\frac{W_g(T)}{T} - \frac{W_g(T_0)}{T_0}\right)\right]$$

The **bandgap voltage** $W_g(T)$ as a function of temperature:
**带隙电压** $W_g(T)$ 随温度变化：

$$W_g(T) = W_g(0) - \frac{\alpha T^2}{T + \beta}$$

For Si: $W_g(0) = 1.16$ eV, $\alpha = 7.02 \times 10^{-4}$ eV/K, $\beta = 1108$ K.

---

### 7.1.2 Linear Diode Model (Small-Signal) | 线性二极管模型（小信号）

#### Small-Signal Equivalent Circuit | 小信号等效电路

At the bias (Q-) point, the diode is linearized. The small-signal impedance is:
在偏置点（Q点），二极管被线性化。小信号阻抗为：

$$Z_d(\omega) = R_S + \frac{R_d}{1 + j\omega R_d C_d}$$

where the **differential resistance** is:
其中**微分电阻**为：

$$R_d = \frac{nV_T}{I_Q}$$

The **impedance behavior**:
- At **low frequencies** ($\omega \ll 1/(R_d C_d)$): $Z_d \approx R_S + R_d$ (purely resistive)
- At **resonance** ($\omega = 1/(R_d C_d)$): $Z_d = R_S + R_d/(1+j)$
- At **high frequencies** ($\omega \gg 1/(R_d C_d)$): $Z_d \approx R_S - j/(\omega C_d)$ (capacitive)

```python
import numpy as np
import matplotlib.pyplot as plt

# Diode small-signal parameters
R_s = 2.0        # Series resistance, Ohm
R_d = 0.518      # Differential resistance at I_Q=50mA, Ohm (nV_T/I_Q = 1*25.9mV/50mA)
C_d = 100e-12    # Diffusion capacitance, Farad
C_j = 2e-12      # Junction capacitance, Farad
C_total = C_d + C_j

f = np.logspace(6, 11, 1000)  # 10 MHz to 100 GHz
omega = 2 * np.pi * f

# Total impedance
Z_d = R_s + (R_d / (1 + 1j * omega * R_d * C_total))
Z_mag = np.abs(Z_d)
Z_phase = np.angle(Z_d, deg=True)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
ax1.loglog(f/1e6, Z_mag, 'b-', linewidth=2)
ax1.set_xlabel('Frequency (MHz)')
ax1.set_ylabel('|Z_d| (Ohm)')
ax1.set_title('Small-Signal Diode Impedance Magnitude vs Frequency')
ax1.grid(True, which='both', alpha=0.5)

ax2.semilogx(f/1e6, Z_phase, 'r-', linewidth=2)
ax2.set_xlabel('Frequency (MHz)')
ax2.set_ylabel('Phase (degrees)')
ax2.set_title('Small-Signal Diode Impedance Phase vs Frequency')
ax2.grid(True, which='both', alpha=0.5)
plt.tight_layout()
plt.savefig('/tmp/diode_impedance.png', dpi=150)
plt.close()
print(f"R_d = {R_d:.3f} Ohm, C_total = {C_total*1e12:.1f} pF")
print(f"Resonance freq = {1/(2*np.pi*R_d*C_total)/1e9:.2f} GHz")
```

---

## 7.2 Transistor Models | 晶体管模型

### 7.2.1 Large-Signal BJT Models | 大信号BJT模型

#### Static Ebers-Moll Model | 静态Ebers-Moll模型

The **Ebers-Moll equations** for an npn BJT in the injection version:
npn BJT在注入版中的**Ebers-Moll方程**：

$$I_E = I_{ES}\left[\exp\left(\frac{V_{BE}}{V_T}\right) - 1\right] - \alpha_R I_{CS}\left[\exp\left(\frac{V_{BC}}{V_T}\right) - 1\right]$$

$$I_C = \alpha_F I_{ES}\left[\exp\left(\frac{V_{BE}}{V_T}\right) - 1\right] - I_{CS}\left[\exp\left(\frac{V_{BC}}{V_T}\right) - 1\right]$$

where $I_{ES}$ and $I_{CS}$ are the base-emitter and base-collector saturation currents, and $\alpha_F$ and $\alpha_R$ are the forward and reverse common-base current gains.

其中 $I_{ES}$ 和 $I_{CS}$ 是基-射和基-集结饱和电流，$\alpha_F$ 和 $\alpha_R$ 是正向和反向共基电流增益。

The relationship between forward current gain and common-emitter gain:
正向电流增益与共发射极增益的关系：

$$\alpha_F = \frac{\beta_F}{1 + \beta_F}, \quad \beta_F = \frac{\alpha_F}{1 - \alpha_F}$$

The **combined current source form** is obtained by substituting:
组合电流源形式通过代入以下关系得到：

$$I_{CC} = I_{ES}\left[\exp\left(\frac{V_{BE}}{V_T}\right) - 1\right], \quad I_{CE} = I_{CS}\left[\exp\left(\frac{V_{BC}}{V_T}\right) - 1\right]$$

Then: $I_C = \alpha_F I_{CC} - I_{CE}$ and $I_E = I_{CC} - \alpha_R I_{CE}$.

#### Gummel-Poon Model | Gummel-Poon模型

The **Gummel-Poon model** extends Ebers-Moll by incorporating:
- **Low-current effects**: base current deviation due to recombination in the depletion region
- **High-injection effects**: Webster effect (base conductivity modulation)
- **Non-ideal base current**: $I_B = I_{SE}[exp(V_{BE}/V_T) - 1] + I_{SC}[exp(V_{BC}/V_{TE}) - 1]$

The **base charge** $Q_B$ in the Gummel-Poon model is:
Gummel-Poon模型中的**基区电荷** $Q_B$：

$$Q_B = Q_{B0}\left[1 + \frac{V_{BC}}{V_{AR}} + \frac{I_C}{I_KF}\right]$$

where $Q_{B0}$ is the zero-bias base charge, $V_{AR}$ is the forward Early voltage, $I_{KF}$ is the forward knee current (high-injection onset), and $I_K = \beta_F V_T / (q V_{AR})$.

The **collector current** becomes:
集电极电流变为：

$$I_C = \frac{I_S}{Q_B}\exp\left(\frac{V_{BE}}{V_T}\right)\left(1 + \frac{V_{CE}}{V_{AN}}\right)$$

The current gain $\beta = I_C/I_B$ is no longer constant but depends on collector current: at low currents, depletion recombination increases; at high currents, high-injection effects reduce $\beta$.

电流增益 $\beta = I_C/I_B$ 不再是常数，而取决于集电极电流：在低电流时，耗尽区复合增加；在高电流时，高注入效应降低 $\beta$。

### 7.2.2 Small-Signal BJT Models | 小信号BJT模型

#### Hybrid-π Model | 混合π模型

The **hybrid-π small-signal model** is the most widely used linear BJT model for RF analysis:

**混合π小信号模型**是RF分析中最广泛使用的线性BJT模型：

```
       r_π        r_o
B ---\/\/\/---C
     |        |
    g_m V_π   |  |
     |        |  v_ce
     +--------+--/\/\/\---C (collector)
     |        |
    C_π       C_\mu
     |        |
     +--------+
     (emitter reference)
```

Key parameters / 关键参数：

| Parameter 参数 | Definition 定义 | Typical Value 典型值 |
|---|---|---|
| $r_{\pi} = \beta_0/g_m$ | Input resistance (base-emitter) | $1$–$10$ kΩ |
| $g_m = I_C/V_T$ | Transconductance | $40 I_C$ (S/A) |
| $r_o = V_{AN}/I_C$ | Output resistance (Early effect) | $10$–$100$ kΩ |
| $C_{\pi} = C_{d} + C_{je}$ | Base-emitter diffusion + junction capacitance | $1$–$100$ pF |
| $C_{\mu}$ | Base-collector junction capacitance (Miller capacitance) | $0.1$–$5$ pF |
| $\tau_F$ | Forward transit time | $0.1$–$10$ ps |

The **unity current-gain cut-off frequency** $f_T$:
**单位电流增益截止频率** $f_T$：

$$\boxed{f_T = \frac{g_m}{2\pi(C_{\pi} + C_{\mu})} = \frac{1}{2\pi\tau_T}}$$

where $\tau_T = \tau_F + C_{\mu}(g_m^{-1} + r_{\pi}\|r_o)$ is the total transit time.

其中 $\tau_T = \tau_F + C_{\mu}(g_m^{-1} + r_{\pi}\|r_o)$ 是总渡越时间。

#### Miller Effect | 米勒效应

The **Miller transformation** converts the feedback impedance $Z_{12}$ (typically $C_{\mu}$) between input and output:

$$C_{M1} = C_{\mu}(1 + A_v), \quad C_{M2} = C_{\mu}\left(1 + \frac{1}{A_v}\right)$$

where $A_v = g_m(R_C \| r_o)$ is the midband voltage gain.

At high frequencies, $C_{\mu}$ appears as a much larger capacitance at the input (Miller capacitance), significantly reducing the input impedance and bandwidth.

在高频时，$C_{\mu}$ 在输入端表现为大得多的电容（米勒电容），显著降低输入阻抗和带宽。

#### h-Parameter Model | h参数模型

For common-emitter configuration, the **h-parameters** are:
对于共发射极配置，**h参数**为：

$$h_{11} = \frac{v_{be}}{i_b}\bigg|_{v_{ce}=0} = r_{\pi} \quad \text{(input resistance)}$$

$$h_{12} = \frac{v_{be}}{v_{ce}}\bigg|_{i_b=0} = \frac{C_{\mu}}{C_{\pi} + C_{\mu}} \approx \frac{C_{\mu}}{C_{\pi}} \quad \text{(reverse voltage gain)}$$

$$h_{21} = \frac{i_c}{i_b}\bigg|_{v_{ce}=0} = \beta_0 \quad \text{(forward current gain)}$$

$$h_{22} = \frac{i_c}{v_{ce}}\bigg|_{i_b=0} = \frac{1}{r_o} \quad \text{(output admittance)}$$

The **frequency-dependent current gain** $\beta(j\omega)$:
频率相关的电流增益 $\beta(j\omega)$：

$$\beta(j\omega) = \frac{\beta_0}{1 + j\omega/\omega_{\beta}} = \frac{\beta_0}{1 + jf/f_{\beta}}$$

where $f_{\beta} = f_T/\beta_0$.

---

### 7.2.3 Large-Signal FET Models | 大信号FET模型

#### Large-Signal FET Circuit Model | 大信号FET电路模型

The large-signal FET model replaces the gate-source and gate-drain diodes (Schottky for MESFET/HEMT) with their nonlinear diode models, and the channel with a **voltage-controlled current source**:

大信号FET模型将栅-源和栅-漏二极管（MESFET/HEMT的肖特基）替换为非线性二极管模型，沟道用**电压控制电流源**表示：

$$I_D = f(V_{GS}, V_{DS}) = \begin{cases} I_{DSS}\left[2\left(1 - \dfrac{V_{GS}}{V_P}\right)\dfrac{V_{DS}}{V_P} - \left(\dfrac{V_{DS}}{V_P}\right)^2\right] & V_{DS} < V_{GS} - V_P \\ I_{DSS}\left(1 - \dfrac{V_{GS}}{V_P}\right)^2\left(1 + \lambda V_{DS}\right) & V_{DS} \geq V_{GS} - V_P \end{cases}$$

The **channel-length modulation** term $(1 + \lambda V_{DS})$ accounts for the Early effect equivalent in FETs.

**沟道长度调制**项 $(1 + \lambda V_{DS})$ 解释了FET中与Early效应等效的现象。

---

### 7.2.4 Small-Signal FET Models | 小信号FET模型

#### Small-Signal FET Circuit Model | 小信号FET电路模型

```
       C_gs        C_gd
G ---||---|----+----+---- D
           |    |    |
          g_m  r_ds  |
          V_gs  |    |
           +----+    |
           |         |
           S ---------+
```

**Small-signal parameters at the Q-point:**
**Q点的小信号参数：**

| Parameter 参数 | Formula 公式 |
|---|---|
| Transconductance $g_m$ | $\dfrac{2I_D}{V_{GS} - V_P} = g_{m0}\left(1 - \dfrac{V_{GS}}{V_P}\right)$ |
| Output conductance $g_{ds}$ | $\dfrac{\lambda I_D}{1 + \lambda V_{DS}} \approx \lambda I_{D,\text{sat}}$ |
| Gate-source capacitance $C_{gs}$ | $C_{gs0}\left(1 - \dfrac{V_{GS}}{V_P}\right)^{-1/2}$ |
| Gate-drain capacitance $C_{gd}$ | $C_{gd0}\left(1 + \dfrac{V_{GD}}{V_P}\right)^{-1/2}$ |

The **cut-off frequency**:
**截止频率**：

$$\boxed{f_T = \frac{g_m}{2\pi(C_{gs} + C_{gd})}}$$

---

## 7.3 Model Parameter Extraction | 模型参数提取

### 7.3.1 Diode Model Parameter Extraction | 二极管模型参数提取

Using forward I-V measurements at low frequency:
使用低频正向I-V测量：

1. Measure $I$ vs. $V$ at known temperature
2. Plot $\ln(I)$ vs. $V$; slope gives $nV_T$, intercept gives $I_S$
3. Determine $R_S$ from the high-current linear region slope

For **junction capacitance** $C_j$ vs. reverse voltage $V_R$:
对于**结电容** $C_j$ vs. 反向电压 $V_R$：

$$\frac{1}{C_j^2} = \frac{2(V_{\text{bi}} + V_R)}{q\epsilon_s A^2 N_{\text{eff}}}$$

A plot of $1/C_j^2$ vs. $V_R$ yields $V_{\text{bi}}$ (intercept) and $N_{\text{eff}}$ (slope).

### 7.3.2 BJT Model Parameter Extraction | BJT模型参数提取

**Forward measurement configuration** (BC junction short-circuited, $V_{BC} = 0$):
**正向测量配置**（BC结短路，$V_{BC} = 0$）：

$$I_C = I_S \exp\left(\frac{V_{BE}}{V_T}\right)$$

Plot $\ln(I_C)$ vs. $V_{BE}$ → slope $= 1/V_T$, intercept $= \ln(I_S)$.

**Gummel-Poon parameters from measurement:**

| Parameter | Measurement |
|---|---|
| $I_S$ | Intercept of $\ln(I_C)$ vs. $V_{BE}$ at low $V_{CE}$ |
| $\beta_F$ | Ratio $I_C/I_B$ in active region |
| $V_{AN}$ (Early voltage) | Slope of $I_C$ vs. $V_{CE}$ at constant $V_{BE}$ |
| $I_{KF}$ | Knee current where $\beta$ begins to roll off at high current |
| $\tau_F$ | From $f_T$ measurement: $\tau_F = 1/(2\pi f_T) - C_{\mu}(1/g_m + r_{\pi}\|r_o)$ |
| $C_{\mu}$ (Miller capacitance) | $S_{12}$ parameter measurement at high frequency |

---

## 📖 Example 7-1: Small-Signal Diode Impedance | 例7-1：小信号二极管阻抗

**Problem:** For a Schottky diode operated at $I_Q = 50$ mA, $T = 300$ K, find: (a) impedance at 10 MHz and 1 GHz; (b) plot impedance vs. frequency from 10 MHz to 10 GHz.

**Solution / 解：**

At $T = 300$ K, $V_T = 25.9$ mV. The differential resistance:
在 $T = 300$ K时，$V_T = 25.9$ mV。微分电阻：

$$R_d = \frac{nV_T}{I_Q} = \frac{1 \times 25.9 \times 10^{-3}}{50 \times 10^{-3}} = 0.518\ \Omega$$

Diffusion capacitance (assuming $\tau_T = 1$ ns):
扩散电容（假设 $\tau_T = 1$ ns）：

$$C_d = \frac{\tau_T I_Q}{V_T} = \frac{10^{-9} \times 0.05}{0.0259} = 1.93\ \text{nF}$$

Series resistance $R_S = 2\ \Omega$.

Total small-signal impedance:
小信号阻抗：

$$Z_d(\omega) = R_S + \frac{R_d}{1 + j\omega R_d(C_d + C_j)}$$

| Frequency | $Z_d$ | $|Z_d|$ | Phase |
|---|---|---|---|
| 10 MHz | $2.51 - j0.32\ \Omega$ | $2.53\ \Omega$ | $-7.2°$ |
| 1 GHz | $2.03 - j1.58\ \Omega$ | $2.56\ \Omega$ | $-37.9°$ |

```python
import numpy as np
import matplotlib.pyplot as plt

R_s = 2.0        # Ohm
n = 1.0
V_T = 25.9e-3    # V
I_Q = 50e-3      # A
R_d = n * V_T / I_Q
C_j = 2e-12      # F
tau_T = 1e-9     # s
C_d = tau_T * I_Q / V_T

f = np.logspace(7, 10.5, 1000)
omega = 2 * np.pi * f
Z_d = R_s + (R_d / (1 + 1j * omega * R_d * (C_d + C_j)))
Z_mag = np.abs(Z_d)
Z_phase = np.angle(Z_d, deg=True)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
ax1.loglog(f/1e6, Z_mag, 'b-', lw=2)
ax1.axhline(R_s+R_d, color='r', ls='--', label=f'Low-freq limit: {R_s+R_d:.2f} Ω')
ax1.set_xlabel('Frequency (MHz)')
ax1.set_ylabel('|Z_d| (Ω)')
ax1.set_title('Small-Signal Diode Impedance vs Frequency')
ax1.legend()
ax1.grid(True, which='both', alpha=0.5)

ax2.semilogx(f/1e6, Z_phase, 'r-', lw=2)
ax2.set_xlabel('Frequency (MHz)')
ax2.set_ylabel('Phase (degrees)')
ax2.set_title('Small-Signal Diode Impedance Phase')
ax2.grid(True, which='both', alpha=0.5)
plt.tight_layout()
plt.savefig('/tmp/diode_z_plot.png', dpi=150)
plt.close()
print(f"R_d = {R_d:.3f} Ω, C_d = {C_d*1e9:.2f} nF, C_j = {C_j*1e12:.1f} pF")
print(f"Corner freq = {1/(2*np.pi*R_d*(C_d+C_j))/1e6:.1f} MHz")
```

---

## 📖 Example 7-2: BJT Hybrid-π Parameter Calculation | 例7-2：BJT混合π参数计算

**Problem:** A BJT is biased at $I_C = 10$ mA, $V_{CE} = 5$ V, $\beta_0 = 145$, $V_{AN} = 120$ V, $\tau_F = 0.3$ ps, $C_{\mu} = 1$ fF, $C_{je} = 2$ pF. Find $g_m$, $r_{\pi}$, $r_o$, $C_{\pi}$, $f_T$.

**Solution / 解：**

$$g_m = \frac{I_C}{V_T} = \frac{0.01}{0.0259} = 386\ \text{mS}$$

$$r_{\pi} = \frac{\beta_0}{g_m} = \frac{145}{0.386} = 376\ \Omega$$

$$r_o = \frac{V_{AN}}{I_C} = \frac{120}{0.01} = 12\ \text{k}\Omega$$

$$C_{\pi} = C_{je} + \frac{\tau_F g_m}{1 + g_m r_o} \approx C_{je} + \tau_F g_m = 2\ \text{pF} + 0.3 \times 10^{-12} \times 386 = 2.12\ \text{pF}$$

$$f_T = \frac{g_m}{2\pi(C_{\pi} + C_{\mu})} = \frac{386 \times 10^{-3}}{2\pi(2.12 \times 10^{-12} + 10^{-15})} \approx 29\ \text{GHz}$$

---

## 7.4 Summary | 本章小结

| Model 模型 | Key Features 关键特性 | Application 应用 |
|---|---|---|
| **Large-signal Diode** | $R_S$, $C_j(V)$, $C_d(I)$ | DC/Transient analysis |
| **Small-signal Diode** | $R_d = nV_T/I_Q$, $C_d + C_j$ | AC/small-signal RF analysis |
| **Ebers-Moll** | Two diodes + controlled sources, $\alpha_F, \alpha_R$ | Large-signal BJT static/dynamic |
| **Gummel-Poon** | Charge-dependent $\beta$, Webster effect, $I_{KF}$ | High-accuracy large-signal BJT |
| **Hybrid-π** | $r_{\pi}, g_m, r_o, C_{\pi}, C_{\mu}$ | Small-signal BJT AC analysis |
| **h-parameters** | $h_{11}, h_{12}, h_{21}, h_{22}$ | Small-signal BJT measurement model |
| **Large-signal FET** | Nonlinear $I_D(V_{GS}, V_{DS})$, diode gates | DC/Transient analysis |
| **Small-signal FET** | $g_m, g_{ds}, C_{gs}, C_{gd}$ | Small-signal RF analysis |

### Key Equations | 关键公式

$$R_d = \frac{nV_T}{I_Q} \quad \text{(Diode differential resistance)}$$
$$f_T = \frac{g_m}{2\pi(C_{\pi} + C_{\mu})} = \frac{1}{2\pi\tau_T} \quad \text{(Transistor cut-off)}$$
$$\beta(j\omega) = \frac{\beta_0}{1 + j\omega/\omega_{\beta}} \quad \text{(Frequency-dependent beta)}$$
$$C_M = C_{\mu}(1 + A_v) \quad \text{(Miller capacitance)}$$
$$g_m = \frac{I_C}{V_T}, \quad r_{\pi} = \frac{\beta_0}{g_m}, \quad r_o = \frac{V_{AN}}{I_C} \quad \text{(Hybrid-π params)}$$
$$I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_P}\right)^2 \quad \text{(FET saturation)}$$
$$f_T = \frac{g_m}{2\pi(C_{gs} + C_{gd})} \quad \text{(FET cut-off)}$$

---

## Further Reading | 深入阅读

- Gummel, H. K., and Poon, H. C., "An Integral Charge Control Model of the Transistor," *Bell Syst. Tech. J.*, Vol. 49, 1970.
- Maas, S. A., *Nonlinear Microwave and RF Circuits*, Artech House, 2003.
- Pedro, J. C., and Carvalho, N. B., *Intermodulation Distortion in Microwave and Wireless Circuits*, Artech House, 2003.
