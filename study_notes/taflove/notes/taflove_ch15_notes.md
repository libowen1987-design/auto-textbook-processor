---
chapter: 15
title: "Modeling of High-Speed Digital and Analog Circuits"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, M. Piket-May, S. Gedney, S. O. Nelson"
raw_size: 143,812 bytes
---

# Chapter 15: Modeling of High-Speed Digital and Analog Circuits
> **中英双语版**

> 高速数字与模拟电路建模

## 15.1 Introduction
> 引言

FDTD is widely used for analyzing high-speed circuits: microstrip interconnects, vias, discontinuities, and their signal integrity effects. Key capabilities: (1) broadband S-parameter extraction, (2) lumped element models, (3) nonlinear device embedding, (4) SPICE coupling.
> FDTD 广泛应用于高速电路分析：微带互连、过孔、不连续性及其信号完整性效应。关键能力：(1) 宽带 S 参数提取，(2) 集总元件模型，(3) 非线性器件嵌入，(4) SPICE 耦合。

## 15.2 Microstrip Discontinuity Modeling
> 微带不连续性建模

### Effective Dielectric Constant
> 有效介电常数

For a microstrip line width $w$, substrate thickness $h$, $\epsilon_r$:
> 对于微带线宽度 $w$、衬底厚度 $h$、相对介电常数 $\epsilon_r$：
$$
\epsilon_{\text{eff}} = \frac{\epsilon_r + 1}{2} + \frac{\epsilon_r - 1}{2} \left( 1 + \frac{12h}{w} \right)^{-1/2}
$$

Characteristic impedance:
> 特性阻抗：
$$
Z_0 = \frac{60}{\sqrt{\epsilon_{\text{eff}}}} \ln\left( \frac{8h}{w} + \frac{w}{4h} \right), \quad w/h \leq 1
$$

### S-Parameter Extraction
> S 参数提取

Using time-domain fields on two reference planes $z_1$, $z_2$:
> 利用两个参考平面 $z_1$、$z_2$ 上的时域场：
$$
S_{11} = \frac{V_1^{-}(\omega)}{V_1^{+}(\omega)}, \quad S_{21} = \frac{V_2^{-}(\omega)}{V_1^{+}(\omega)}
$$

Voltage is computed as line integral of E-field from strip to ground. Current via Ampère's law around the strip.
> 电压通过从带状线到地面的电场线积分计算。电流通过带状线周围的安培环路定律计算。

## 15.3 Lumped Inductance and Capacitance
> 集总电感和电容

### Inductance from Magnetic Flux
> 由磁通量计算电感
$$
L = \frac{\Phi}{I} = \frac{\iint_S \mu \mathbf{H} \cdot d\mathbf{S}}{I}
$$
where $S$ is the surface bounded by the signal and return paths.
> 其中 $S$ 为信号路径与回流路径所围成的曲面。

### Capacitance from Electric Flux
> 由电通量计算电容
$$
C = \frac{Q}{V} = \frac{\iint_S \epsilon \mathbf{E} \cdot d\mathbf{S}}{V}
$$

### Equivalent Circuit Fitting
> 等效电路拟合

Fit $Z(\omega)$ or $S(\omega)$ to an equivalent circuit (RLC):
> 将 $Z(\omega)$ 或 $S(\omega)$ 拟合到等效 RLC 电路：
$$
Z(\omega) = R + j\omega L + \frac{1}{j\omega C}
$$

## 15.4 Discontinuity Characterization
> 不连续性表征

### Microstrip Gap
> 微带缝隙

Equivalent $\pi$-network: $C_{\text{series}}$, $C_{\text{shunt}}$ from FDTD field data. Gap coupling increases with decreasing gap width.
> 等效 $\pi$ 型网络：从 FDTD 场数据提取 $C_{\text{series}}$（串联电容）和 $C_{\text{shunt}}$（并联电容）。缝隙耦合随缝隙宽度减小而增强。

### Microstrip Bend
> 微带拐角

Mitred bend optimization: FDTD determines optimal 45° chamfer for minimum reflection ($|S_{11}| < -25$ dB).
> 切角弯头优化：FDTD 确定最佳 45° 倒角以实现最小反射。

### Microstrip Via
> 微带过孔

via inductance: $L_{\text{via}} \approx \frac{\mu_0 h}{2\pi} \ln\left( \frac{2h}{r} \right)$ for via radius $r$ through substrate thickness $h$.
> 过孔电感：对于穿过厚度为 $h$ 衬底的半径为 $r$ 的过孔。

## 15.5 Parallel Coplanar Microstrips
> 平行共面微带线

### Coupled Line Parameters
> 耦合线参数

Even- and odd-mode impedances $Z_{0e}$, $Z_{0o}$ from FDTD:
> 从 FDTD 获得的偶模和奇模阻抗：
$$
Z_{0e} = \sqrt{\frac{L_{11} + L_{12}}{C_{11} - C_{12}}}, \quad
Z_{0o} = \sqrt{\frac{L_{11} - L_{12}}{C_{11} + C_{12}}}
$$

### Directional Coupler
> 定向耦合器

4-port S-parameters for a quarter-wave coupled section. FDTD predicts coupling level within 0.5 dB of measurements.
> 四分之一波长耦合段的 4 端口 S 参数。FDTD 预测的耦合度与测量值偏差在 0.5 dB 以内。

## 15.6 Multilayered Interconnect Modeling
> 多层互连建模

For complex PCB/package structures with multiple layers:
> 对于具有多层的复杂 PCB/封装结构：
- FDTD naturally handles layer transitions
  > FDTD 自然处理层间过渡
- Signal vias, ground vias, power planes modeled directly
  > 信号过孔、接地过孔、电源平面直接建模
- Simultaneous switching noise (SSN) analysis
  > 同步开关噪声分析
- Results: $S_{21}$ within 1 dB of measurements to 20 GHz
  > 结果：$S_{21}$ 与测量值偏差在 1 dB 以内，频率达 20 GHz

## 15.7 S-Parameter Extraction
> S 参数提取

General procedure for $N$-port waveguide structures:
> $N$ 端口波导结构的通用流程：
1. Excite port $p$ with broadband pulse
   > 用宽带脉冲激励端口 $p$
2. Record incident/reflected waves at all ports
   > 记录所有端口的入射/反射波
3. Compute $S_{qp}(\omega) = V_q^-(\omega)/V_p^+(\omega)$
   > 计算 S 参数

For non-TEM waveguides (rectangular, circular), mode decomposition is required using field orthogonality:
> 对于非 TEM 波导（矩形、圆形），需要使用场正交性进行模式分解：
$$
a_p(\omega) = \iint \mathbf{E}_{\text{total}} \times \mathbf{h}_p^* \cdot d\mathbf{S}
$$
where $\mathbf{h}_p$ is the normalized magnetic field of mode $p$.
> 其中 $\mathbf{h}_p$ 为模式 $p$ 的归一化磁场。

## 15.8 Digital Signal Processing
> 数字信号处理

### Prony's Method
> Prony 方法

Extract resonant frequencies and Q-factors from time-domain data:
> 从时域数据提取谐振频率和 Q 值：
$$
x[n] = \sum_{k=1}^K A_k e^{(\alpha_k + j\omega_k) n\Delta t}
$$

### Pencil Method (MPM)
> 矩阵束法

More robust than Prony for noisy data. Constructs a matrix pencil from the time series and solves a generalized eigenvalue problem.
> 对含噪声数据比 Prony 法更稳健。从时间序列构造矩阵束并求解广义特征值问题。

### Padé Approximation
> Padé 逼近

Extrapolates frequency response beyond the FDTD bandwidth:
> 外推频率响应超出 FDTD 带宽范围：
$$
S(\omega) \approx \frac{\sum_{p=0}^P a_p (j\omega)^p}{1 + \sum_{q=1}^Q b_q (j\omega)^q}
$$

## 15.9 Modeling of Lumped Circuit Elements
> 集总电路元件建模

### 15.9.1 Extended FDTD Formulation
> 扩展 FDTD 公式

Lumped elements modify the Ampère law update at specific cells:
> 集总元件修改特定网格单元处的安培定律更新式：
$$
\nabla \times \mathbf{H} = \epsilon \frac{\partial \mathbf{E}}{\partial t} + \sigma \mathbf{E} + \mathbf{J}_{\text{lumped}}
$$

### 15.9.2 Resistor
> 电阻

For a resistor $R$ at cell $(i,j,k)$:
> 位于 $(i,j,k)$ 网格单元处的电阻 $R$：
$$
J_{\text{lumped}} = \frac{E_z}{R \cdot \Delta z}
$$

The update becomes:
> 更新公式变为：
$$
E_z^{n+1} = \frac{2\epsilon - \Delta t(\sigma + 1/(R\Delta z))}{2\epsilon + \Delta t(\sigma + 1/(R\Delta z))} E_z^n + \frac{2\Delta t}{2\epsilon + \Delta t(\sigma + 1/(R\Delta z))} (\nabla \times \mathbf{H})^{n+1/2}
$$

### 15.9.3 Capacitor
> 电容

For a capacitor $C$:
> 对于电容 $C$：
$$
I_C = C \frac{dV}{dt} = C\Delta z \frac{dE_z}{dt}
$$

Update (using trapezoidal integration):
> 更新公式（使用梯形积分）：
$$
E_z^{n+1} = E_z^n + \frac{\Delta t}{\epsilon + C\Delta z/\Delta t} (\nabla \times \mathbf{H})^{n+1/2} - \frac{C\Delta z}{\epsilon\Delta t + C\Delta z} (E_z^n - E_z^{n-1})
$$

### 15.9.4 Inductor
> 电感

For inductor $L$, using the current-voltage relation $V = L dI/dt$:
> 对于电感 $L$，使用伏安关系 $V = L dI/dt$：
$$
E_z^{n+1} = E_z^n + \frac{\Delta t}{\epsilon} (\nabla \times \mathbf{H})^{n+1/2} - \frac{\Delta t \cdot I_L}{\epsilon \Delta x \Delta y}
$$
where $I_L^{n+1/2} = I_L^{n-1/2} + \Delta t \cdot E_z^n / (L/\Delta z)$.
> 其中 $I_L^{n+1/2} = I_L^{n-1/2} + \Delta t \cdot E_z^n / (L/\Delta z)$。

### 15.9.5 Diode
> 二极管

For a PN junction diode, the nonlinear current:
> 对于 PN 结二极管，非线性电流：
$$
I_D = I_s \left[ \exp\left( \frac{qV}{nkT} \right) - 1 \right], \quad V = E_z \cdot \Delta z
$$

Newton-Raphson iteration solves the nonlinear update at each time-step:
> 在每个时间步使用 Newton-Raphson 迭代求解非线性更新：
$$
E_z^{n+1} = E_z^n + \frac{\Delta t}{\epsilon} (\nabla \times \mathbf{H})^{n+1/2} - \frac{\Delta t}{\epsilon \Delta x \Delta y} \cdot I_D(E_z^{n+1})
$$

## 15.10 SPICE-FDTD Hybrid
> SPICE-FDTD 混合法

For complex nonlinear circuits, the FDTD field solver is coupled to a SPICE circuit solver:
> 对于复杂非线性电路，FDTD 场求解器与 SPICE 电路求解器耦合：
$$
I_{\text{port}}(t) = \text{SPICE}_{\text{solve}}(V_{\text{port}}(t))
$$

The SPICE model provides current as a function of voltage, while FDTD provides voltage from the field solution. Coupling at each time-step:
> SPICE 模型提供电流作为电压的函数，FDTD 从场解提供电压。每时间步的耦合：
1. FDTD provides $V_{\text{port}}^n$
   > FDTD 提供端口电压
2. SPICE computes $I_{\text{port}}^{n+1/2}$
   > SPICE 计算端口电流
3. FDTD updates $E$-field with $J_{\text{lumped}} = I_{\text{port}} / (\Delta x \Delta y)$
   > FDTD 用集总电流密度更新电场

## Summary
> 总结

| Element | FDTD Implementation | Nonlinear | Stability Impact |
|---------|-------------------|-----------|-----------------|
| 元件 | FDTD 实现方式 | 非线性 | 稳定性影响 |
| Resistor | Additive conductivity | No | Negligible |
| 电阻 | 附加电导率 | 否 | 可忽略 |
| Capacitor | Modified permittivity | No | CFL reduced |
| 电容 | 修改介电常数 | 否 | CFL 减小 |
| Inductor | Recursive current integral | No | CFL reduced |
| 电感 | 递归电流积分 | 否 | CFL 减小 |
| Diode | Newton-Raphson | Yes | Time-step limited |
| 二极管 | Newton-Raphson | 是 | 时间步受限 |
| BJT/FET | SPICE coupling | Yes | SPICE-dependent |
| 晶体管 | SPICE 耦合 | 是 | 取决于 SPICE |
| Transmission line | 1D FDTD | No | CFL of 1D line |
| 传输线 | 一维 FDTD | 否 | 一维线 CFL |
