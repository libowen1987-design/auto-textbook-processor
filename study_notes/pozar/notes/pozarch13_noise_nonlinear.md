# Pozar Chapter 13 — Noise and Nonlinear Distortion in Microwave Systems
> **中英双语版**

> Comprehensive notes on Pozar *Microwave Engineering*, 4th Edition.
> Covers thermal noise, noise figure, nonlinear distortion, intermodulation, and dynamic range.

---

## 13.1 Noise in Microwave Systems | 微波系统中的噪声

### 13.1.1 Thermal Noise | 热噪声

Available noise power from a resistor at temperature $T$ over bandwidth $B$:
> 温度为 $T$ 的电阻在带宽 $B$ 上可用的噪声功率：

$$N_0 = kTB \quad [\text{W}]$$

where $k = 1.38 \times 10^{-23}$ J/K is Boltzmann's constant.
> 其中 $k = 1.38 \times 10^{-23}$ J/K 为玻尔兹曼常数。

**Available noise power density:** $N_0/B = kT = -174$ dBm/Hz at $T = 290$ K.
> 可用噪声功率密度：$T=290$ K 时为 $-174$ dBm/Hz。

**Noise voltage from a resistor / 电阻的噪声电压：**

$$v_n = \sqrt{4kTRB} \quad [\text{V}]$$

### 13.1.2 Noise Figure | 噪声系数

**Definition / 定义：**

$$F = \frac{\text{SNR}_{\text{in}}}{\text{SNR}_{\text{out}}} = \frac{S_i/N_i}{S_o/N_o} \quad (\text{linear}), \quad NF = 10\log_{10} F \quad [\text{dB}]$$

> 噪声系数 $F$ 定义为输入信噪比与输出信噪比之比。

For a two-port network with gain $G$ and noise added by the network:
> 对于增益为 $G$ 且网络自身有噪声的二端口网络：

$$F = \frac{N_o}{G N_i} = \frac{N_o}{GkT_0B}, \quad T_0 = 290\;\text{K}$$

### 13.1.3 Noise Temperature | 噪声温度

$$T_e = T_0 (F - 1), \quad F = 1 + \frac{T_e}{T_0}$$

> 等效噪声温度 $T_e$ 与噪声系数的关系。

### 13.1.4 Noise of Cascaded Networks | 级联网络的噪声

**Friis formula / Friis 公式：**

$$F_{\text{total}} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \cdots$$

> 级联网络的总噪声系数主要由第一级决定，因为后续级的噪声被前面级的增益除。

**Key insight / 关键结论：** The first-stage gain $G_1$ reduces the noise contribution of all subsequent stages.
> 第一级的增益 $G_1$ 减少了后续所有级的噪声贡献。

---

## 13.2 Nonlinear Distortion | 非线性失真

### 13.2.1 Gain Compression | 增益压缩

For a nonlinear amplifier, the output voltage can be expressed as:
> 对于非线性放大器，输出电压可表示为：

$$v_o = a_1 v_i + a_2 v_i^2 + a_3 v_i^3 + \cdots$$

For a sinusoidal input $v_i = V_0 \cos\omega t$:
> 对于正弦输入 $v_i = V_0 \cos\omega t$：

$$v_o = \underbrace{(a_1 V_0 + \frac{3}{4}a_3V_0^3)}_{\text{fundamental}} \cos\omega t + \text{(harmonics)}$$

When $a_3 < 0$ (typical for amplifiers), the fundamental gain decreases with increasing input power—this is **gain compression**.
> 当 $a_3 < 0$ 时，基波增益随输入功率增加而减小，即**增益压缩**。

**1-dB compression point ($P_{\text{1dB}}$):** Input power where gain drops by 1 dB.
> **1-dB 压缩点：** 增益下降 1 dB 时的输入功率。

### 13.2.2 Intermodulation Distortion | 互调失真

With a two-tone input $v_i = V_0(\cos\omega_1 t + \cos\omega_2 t)$:
> 双音输入 $v_i = V_0(\cos\omega_1 t + \cos\omega_2 t)$：

**Third-order intermodulation products / 三阶互调产物：**
- $2\omega_1 - \omega_2$ and $2\omega_2 - \omega_1$ (close to the fundamentals)
- These fall within the desired bandwidth and cannot be filtered out
  > 落在所需带宽内，无法滤除

**Third-order intercept point (IP3):** The power level where the extrapolated fundamental and third-order intermodulation products intersect.
> **三阶交调截点 (IP3)：** 外推基波和三阶互调产物交汇处的功率电平。

**Dynamic range (SFDR) / 无杂散动态范围：**

$$\text{SFDR} = \frac{2}{3}(\text{IIP3} - N_{\text{floor}}) \quad [\text{dB}]$$

where $N_{\text{floor}}$ is the noise floor and IIP3 is the input-referred third-order intercept.
> 其中 $N_{\text{floor}}$ 为噪声基底，IIP3 为输入参考三阶交调截点。

---

## 13.3 Summary / 总结

| Parameter | Symbol | Definition |
|-----------|--------|------------|
| Noise figure | $F$ | $\text{SNR}_{\text{in}}/\text{SNR}_{\text{out}}$ |
| Noise temperature | $T_e$ | $T_0(F-1)$ |
| 1-dB compression point | $P_{\text{1dB}}$ | Gain drops 1 dB |
| Third-order intercept | IP3 | Extrapolated crossing of fundamental and IM3 |
| Spurious-free dynamic range | SFDR | Range between noise floor and distortion |

**Design trade-off / 设计权衡：** Low noise figure (front-end) vs. high linearity (high-power stages).
> 低噪声系数（前端）与高线性度（大功率级）之间的权衡。
