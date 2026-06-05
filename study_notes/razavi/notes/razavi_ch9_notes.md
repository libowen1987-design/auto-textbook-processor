---
chapter: 9
title: Phase-Locked Loops
source: Behzad Razavi, RF Microelectronics, 2nd Edition, McGraw-Hill, 2012
pages: 597-652
---

# Chapter 9: Phase-Locked Loops
# 第九章：锁相环

> *"The phase-locked loop is the backbone of modern frequency synthesis, converting a stable reference frequency into a tunable, low-phase-noise LO signal."*
>
> **（中文）** 锁相环（PLL）是现代频率合成的基石，它将一个稳定的参考频率转换为一个可调谐、低相位噪声的本振信号。本章从PLL的基本原理出发，推导传递函数，分析各类PLL的行为特性。

---

## 9.1 Basic Concepts | 基本概念

### PLL Block Diagram | PLL框图

```
Reference → [PFD/CP] → [LPF] → [VCO] → [÷N] → Output
    ↑__________________________________|
```

**Components:**
- **Phase/Frequency Detector (PFD)**: Compares reference phase with divided VCO phase, outputs error pulses
- **Charge Pump (CP)**: Converts PFD digital pulses to analog current $I_P$
- **Loop Filter (LPF)**: Integrates charge pump current, produces VCO control voltage $V_{\text{ctrl}}$
- **VCO**: Oscillator with frequency $\omega_{\text{VCO}} = \omega_0 + K_{\text{VCO}} V_{\text{ctrl}}$
- **Divider (÷N)**: Divides VCO frequency by $N$ to match reference frequency

> **（中文）** PLL的基本原理是闭环负反馈：PFD比较参考信号与分频后VCO信号的相位差，输出误差脉冲；电荷泵将脉冲转换为电流；低通滤波器（LPF）积分电流产生VCO控制电压；VCO被调谐使输出频率锁定到参考频率的$N$倍。

### PLL Input-Output Relationship | PLL输入-输出关系

The PLL tracks the phase of the input reference:

$$
\phi_{\text{out}}(s) = H(s) \cdot \phi_{\text{ref}}(s) + [1 - H(s)] \cdot \phi_{\text{noise}}(s) \quad \text{(9.1)}
$$

where $H(s)$ is the closed-loop transfer function.

**Steady-state phase error for a step input:**

$$
\phi_{\text{err,ss}} = \lim_{s\to 0} \frac{s}{1 + G(s)} \cdot \frac{\Delta\phi}{s^2} = \frac{\Delta\phi}{K_p} \quad \text{(9.2)}
$$

where $K_p$ is the open-loop DC gain (type-I: finite, type-II: infinite).

---

## 9.2 Type-I PLLs | 一型PLL

### Basic Type-I PLL | 基本一型PLL

A type-I PLL uses a phase detector (not PFD) and has no charge pump:

$$
G(s) = \frac{K_P K_{\text{VCO}}}{s} \cdot \frac{1}{N} \quad \text{(9.3)}
$$

where $K_P$ is the phase detector gain (V/rad).

**Closed-loop transfer function:**

$$
H(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2} \quad \text{(9.4)}
$$

where:
- **Natural frequency**: $\omega_n = \sqrt{\frac{K_P K_{\text{VCO}}}{N \cdot \tau}}$ (where $\tau = R_1 C_1$ of LPF)
- **Damping factor**: $\zeta = \frac{\omega_n \tau}{2} = \frac{R_1 C_1}{2}\sqrt{\frac{K_P K_{\text{VCO}}}{N \cdot R_1 C_1}}$

> **（中文）** 一型PLL使用相位检测器（鉴相器），开环传递函数$G(s) = K_P K_{\text{VCO}}/(Ns)$，闭环传递函数为标准的二阶低通型（$\omega_n^2/(s^2 + 2\zeta\omega_n s + \omega_n^2)$）。一型PLL的同步范围（lock range）有限，且对频率阶跃存在稳态相位误差。

**Lock Range:**

$$
\Delta\omega_L = \pm 2\pi \cdot \frac{K_P K_{\text{VCO}}}{N} \quad \text{(9.5)}
$$

**Hold Range:**

$$
\Delta\omega_H = \pm \frac{K_P K_{\text{VCO}}}{N} \quad \text{(9.6)}
$$

Note: $\Delta\omega_H = \pi \cdot \Delta\omega_L$ for type-I PLL.

---

## 9.3 Type-II PLLs | 二型PLL

### 9.3.1 Phase/Frequency Detectors | 鉴相鉴频器

Type-II PLLs use a **PFD** (Phase/Frequency Detector), which detects both phase and frequency errors:

**State machine**: PFD has three states: UP, DOWN, and idle (when both inputs have the same edges).

**PFD truth table:**

| Reference | VCO/÷N | Output |
|---|---|---|
| Rising edge leads | — | UP pulse |
| Rising edge lags | — | DOWN pulse |
| Same phase | — | Idle |

**PFD reset delay $\tau_{\text{reset}}$** limits the minimum UP/DOWN pulse width.

> **（中文）** 鉴相鉴频器（PFD）是一型PLL与二型PLL的核心区别。PFD能检测频率差和相位差：当参考信号领先VCO/÷N信号时输出UP脉冲；落后时输出DOWN脉冲。PFD的工作速度受限于其内部复位延迟$\tau_{\text{reset}}$（典型值约几纳秒），这限制了PLL的最高工作频率。

### 9.3.2 Charge Pumps | 电荷泵

The charge pump converts digital UP/DOWN pulses to an analog current:

$$
I_{\text{pump}} = I_{\text{UP}} = -I_{\text{DOWN}} = I_P \quad \text{(9.7)}
$$

**Charge pump current mismatch**: Even with ideal PFD, mismatch between $I_{\text{UP}}$ and $I_{\text{DOWN}}$ causes a static phase offset:

$$
\Delta\phi_{\text{offset}} = 2\pi \cdot \frac{I_{\text{mismatch}}}{I_P} \cdot \frac{T_{\text{ref}}}{2} \quad \text{(9.8)}
$$

> **（中文）** 电荷泵将PFD的数字上/下脉冲转换为模拟电流。电荷泵电流失配（$I_{\text{UP}} \neq |I_{\text{DOWN}}|$）会导致稳态相位偏置——即使在锁定状态下，VCO的控制电压也会有一个净的周期性波动，这会在VCO输出引入相位调制（spurs）。

### 9.3.3 Charge-Pump PLLs | 电荷泵PLL

The CP-PLL with a passive second-order loop filter:

```
          I_P (UP/DN)     V_ctrl
PFD →────→ CP ─────────→ LPF ─────→ VCO
         (current)       R_1 + 1/(sC_1)
```

**Open-loop transfer function:**

$$
G(s) = \frac{I_P K_{\text{VCO}}}{2\pi N} \cdot \frac{R_1 s + 1}{s^2 C_1} \quad \text{(9.9)}
$$

**Closed-loop transfer function:**

$$
H(s) = \frac{\omega_n^2 + 2\zeta\omega_n s}{s^2 + 2\zeta\omega_n s + \omega_n^2} \quad \text{(9.10)}
$$

where:
- $\omega_n = \sqrt{\frac{I_P K_{\text{VCO}}}{2\pi N C_1}}$ (natural frequency)
- $\zeta = R_1\sqrt{\frac{I_P K_{\text{VCO}} C_1}{8\pi N}}$ (damping factor)

> **（中文）** 二型PLL（CP-PLL）的开环传递函数在原点有一个二极点（因为VCO的$1/s$积分和LPF的另一个极点），因此具有零稳态相位误差（type-II特性）。环路参数$\omega_n$和$\zeta$完全由$I_P$、$K_{\text{VCO}}$、$N$和$C_1$决定。

**Zero placement**: The LPF zero (at $1/R_1C_1$) is placed to provide phase margin:

$$
\omega_z = \frac{1}{R_1 C_1} = \frac{\omega_n}{4\zeta} \quad \text{(9.11)}
$$

### 9.3.4 Transient Response | 瞬态响应

**Phase step response:**

For a step phase error $\Delta\phi \cdot u(t)$ at reference:

$$
\phi_{\text{err}}(t) = \Delta\phi \cdot \frac{1}{\sqrt{1-\zeta^2}} e^{-\zeta\omega_n t} \sin(\omega_n\sqrt{1-\zeta^2}t + \phi) \quad \text{(9.12)}
$$

**Frequency step response:**

For a step frequency error $\Delta\omega$:

$$
\Delta\phi_{\text{peak}} \approx \frac{\Delta\omega}{2\zeta\omega_n} \quad \text{(9.13)}
$$

> **（中文）** CP-PLL的瞬态响应取决于阻尼因子$\zeta$：过阻尼（$\zeta > 1$）响应慢但无振荡；欠阻尼（$\zeta < 1$）有振荡但响应快。典型设计选择$\zeta \approx 0.7-1$（$60^\circ-70^\circ$相位裕度），在响应速度和过冲之间取得良好平衡。

### 9.3.5 Limitations of Continuous-Time Approximation | 连续时间近似的局限性

The PLL is actually a **sampled system** (PFD operates at $f_{\text{ref}}$). The continuous-time approximation breaks down when:

$$
f_{\text{ref}} < 10 \times \omega_n \quad \text{(9.14)}
$$

**Stability criterion in discrete time**: The phase margin degrades in discrete-time implementation; requires lower $\omega_n$ or higher phase margin in continuous design.

> **（中文）** PLL实际上是一个采样系统（因为PFD以参考频率$f_{\text{ref}}$工作），但我们通常用连续时间模型分析。当$\omega_n > f_{\text{ref}}/10$时，连续时间近似失效，环路在离散时间域的稳定性必须单独分析——这在现代高参考频率（$\sim 10\ \text{MHz}$）的PLL中尤为重要。

### 9.3.6 Frequency-Multiplying CPPLL | 倍频CP-PLL

By adding a pulse swallowing counter (multi-modulus divider), the PLL can multiply frequency by a non-integer factor $N + K/M$:

**Fractional-$N$ PLL** (covered in detail in Chapter 11).

> **（中文）** 通过多模分频器（multi-modulus divider），PLL可以实现分数分频（fractional-$N$），使VCO输出频率为参考频率的任意有理数倍。这大大降低了参考频率对信道间隔的限制，是现代频率合成的核心技术。

### 9.3.7 Higher-Order Loops | 高阶环路

**Third-order LPF** (adding $R_2 C_2$ to the second-order filter):

$$
H(s) = \frac{\omega_n^2(s/\omega_z + 1)}{s^2(s/\omega_{p2} + 1) + \omega_n^2(s/\omega_z + 1)} \quad \text{(9.15)}
$$

> **（中文）** 高阶LPF（三阶及以上）在二阶LPF的基础上增加额外的极点，进一步衰减电荷泵的开关纹波。但高阶环路会使PLL的稳定性分析更复杂，通常需要使用软件工具（如MATLAB/Simulink）进行数值仿真验证。

---

## 9.4 PFD/CP Nonidealities | PFD/CP非理想效应

### 9.4.1 Up and Down Skew and Width Mismatch | 上/下沿偏移与脉宽失配

Mismatch in the UP and DOWN path delays and pulse widths causes a **static phase offset**:

$$
\phi_{\text{offset}} \propto \frac{\tau_{\text{skew}}}{T_{\text{ref}}} \cdot \frac{2\pi I_P}{I_{\text{charge}}} \quad \text{(9.16)}
$$

This offset translates to a frequency error in the locked state.

> **（中文）** UP和DOWN路径的延迟失配（skew）和脉宽失配会在锁定点引入静态相位偏置，导致VCO控制电压在参考频率处有残余纹波。这是PFD/CP电路设计中必须最小化的效应。

### 9.4.2 Voltage Compliance | 电压兼容性

Charge pump current sources must remain in saturation over the full $V_{\text{ctrl}}$ range:

$$
V_{\text{DS,sat}} < V_{\text{ctrl}} < V_{\text{DD}} - V_{\text{DS,sat}} \quad \text{(9.17)}
$$

**Issue**: VCO tuning range may require $V_{\text{ctrl}}$ near rails, causing charge pump nonlinearity.

> **（中文）** 电荷泵电流源必须在整个$V_{\text{ctrl}}$范围内保持饱和。当$V_{\text{ctrl}}$接近$V_{\text{DD}}$或地时，电流源的$V_{\text{DS}}$降低，退出饱和区，导致泵电流下降，环路增益变化，相位裕度恶化。这是设计低压PLL时的重要考虑。

### 9.4.3 Charge Injection and Clock Feedthrough | 电荷注入与时钟馈通

When the charge pump switches turn off, the channel charge stored under the switch gates is injected onto the LPF:

$$
\Delta V_{\text{ripple}} \approx \frac{W L C_{\text{ox}} V_{\text{GS}}}{C_1} \quad \text{(9.18)}
$$

**Mitigation**: Use dummy switches, differential architectures, or bottom-plate sampling.

> **（中文）** 电荷注入（charge injection）是MOS开关固有的效应：当开关关断时，沟道电荷被释放到连接的节点上。对于PLL电荷泵，这会在LPF输出产生一个周期性尖刺（spur），其频率为$f_{\text{ref}}$，幅度与$WLC_{\text{ox}}V_{\text{GS}}$成正比。

### 9.4.4 Random Mismatch between Up and Down Currents | 上下电流随机失配

Process variation causes $I_{\text{UP}}$ and $I_{\text{DOWN}}$ to mismatch randomly:

$$
\sigma(\Delta I/I_P) = \frac{A_{\text{mismatch}}}{\sqrt{WL}} \quad \text{(9.19)}
$$

where $A_{\text{mismatch}} \approx 1-5\% \cdot \mu\text{m}$ for typical CMOS.

This mismatch generates a **reference spur** at $f_{\text{ref}}$:

$$
\mathcal{L}(f_{\text{ref}}) \approx 20\log_{10}\left(\frac{\sigma(\Delta I)}{I_P}\right) \quad \text{(9.20)}
$$

> **（中文）** UP/DOWN电流的随机失配是产生$f_{\text{ref}}$参考杂散（reference spur）的根本原因。失配的电流在每个参考周期内向LPF注入/抽取额外的电荷，导致$V_{\text{ctrl}}$在$f_{\text{ref}}$处有纹波，该纹波通过$K_{\text{VCO}}$调制VCO相位，产生参考杂散。随机失配与器件面积的平方根成反比——增大器件面积是降低失配的有效方法。

### 9.4.6 Circuit Techniques | 电路技术

**Differential charge pump**: Rejects common-mode noise and reduces charge injection errors.

**Switched-capacitor loop filter**: Eliminates continuous current and reference spurs, but adds discrete-time complexity.

**Dead zone elimination**: PFD must produce minimum UP/DOWN pulses even when phase error is very small, to avoid dead zone (insensitivity near lock).

---

## 9.5 Phase Noise in PLLs | PLL中的相位噪声

### 9.5.1 VCO Phase Noise | VCO相位噪声

In the PLL, VCO phase noise is **high-pass filtered** by the closed-loop:

$$
S_{\phi,\text{VCO,out}}(\Delta\omega) = |1 - H(j\omega)|^2 \cdot S_{\phi,\text{VCO}}(\Delta\omega) \quad \text{(9.21)}
$$

Near the carrier ($\Delta\omega \ll \omega_n$): $H \approx 1$, VCO noise passes through (not suppressed).
Far from carrier ($\Delta\omega \gg \omega_n$): $H \approx 0$, VCO noise is suppressed by PLL.

> **（中文）** PLL对VCO相位噪声具有**高通滤波**特性：在低频偏移（$\Delta\omega < \omega_n$）处，PLL环路跟不上VCO的相位变化，VCO噪声直接传递到输出；在高频偏移（$\Delta\omega > \omega_n$）处，PLL的负反馈抑制了VCO的相位扰动，VCO噪声被衰减。$\omega_n$是VCO噪声通过与抑制的转折频率。

### 9.5.2 Reference Phase Noise | 参考振荡器相位噪声

The reference oscillator noise is **low-pass filtered** by the PLL:

$$
S_{\phi,\text{ref,out}}(\Delta\omega) = |H(j\omega)|^2 \cdot S_{\phi,\text{ref}}(\Delta\omega) \quad \text{(9.22)}
$$

Near the carrier ($\Delta\omega \ll \omega_n$): $H \approx 1$, reference noise passes through.
Far from carrier: $H \approx 0$, reference noise is rejected.

> **（中文）** 参考振荡器（通常是晶振）的相位噪声被PLL**低通滤波**：在$\Delta\omega \ll \omega_n$的低频范围内，PLL环路跟踪参考信号的相位变化，因此参考噪声直接传递到输出；在高频范围，PLL的负反馈抑制了参考噪声。由于晶振的相位噪声在高频处非常低（$\mathcal{L} < -150\ \text{dBc/Hz}$），参考噪声主要在近载波处（$\Delta\omega < \omega_n$）影响输出。

---

## 9.6 Loop Bandwidth | 环路带宽

**Optimal loop bandwidth** $\omega_n$ minimizes total output phase noise:

- Too narrow: VCO noise dominates (poor near-carrier performance)
- Too wide: Reference and divider noise dominate (poor far-from-carrier performance)

The optimal $\omega_n$ is where the **in-band noise floor** equals the **out-of-band VCO noise** at $\omega_n$:

$$
\mathcal{L}_{\text{VCO}}(\omega_n) = \mathcal{L}_{\text{ref,divider}}(\omega_n) \quad \text{(9.23)}
$$

> **（中文）** 环路带宽$\omega_n$是PLL设计中最重要的权衡：$\omega_n$太小→VCO噪声未充分抑制→近载波相位噪声差；$\omega_n$太大→参考和分频器噪声通过环路放大→高频相位噪声底升高。最佳$\omega_n$位于VCO噪声谱与参考/分频器噪声谱的交点。

**Typical design rule**: $\omega_n \approx f_{\text{ref}}/10$ to $f_{\text{ref}}/5$ (ensures adequate phase margin while avoiding sampling effects).

---

## Key Takeaways | 本章要点

1. **Type-II CP-PLL**: Zero steady-state phase error for phase steps, frequency steps converge to lock.
2. **Loop filter design**: $\omega_n = \sqrt{I_P K_{\text{VCO}}/(2\pi N C_1)}$, $\zeta = R_1\sqrt{I_P K_{\text{VCO}}C_1/(8\pi N)}$.
3. **CP nonidealities**: Current mismatch → reference spurs; charge injection → $f_{\text{ref}}$ ripple; dead zone → nonlinearity.
4. **PLL as noise filter**: VCO noise is high-pass filtered; reference/divider noise is low-pass filtered.
5. **Optimal $\omega_n$**: Minimizes total phase noise; typically $f_{\text{ref}}/10$.
6. **Stability**: Continuous-time approximation valid for $\omega_n < f_{\text{ref}}/10$; higher $N$ → lower $\omega_n$ for same $\zeta$.
7. **Fractional-$N$**: Allows fractional multiplication, enabling fine frequency resolution without low reference frequency (covered in Ch11).
