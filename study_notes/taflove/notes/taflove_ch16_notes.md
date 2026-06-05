---
chapter: 16
title: "Photonic Crystals and Optical Devices"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, S. C. Hagness, B. J. Ward"
raw_size: 290,881 bytes
---

# Chapter 16: Photonic Crystals and Optical Devices
> **中英双语版**

> 光子晶体与光学器件

## 16.1 Introduction
> 引言

FDTD is the leading numerical method for nanophotonic device modeling. Key applications: photonic crystals (PhC), microcavities, plasmonic structures, waveguide couplers, and nonlinear optical devices.
> FDTD 是纳米光子器件建模的领先数值方法。关键应用：光子晶体、微腔、等离激元结构、波导耦合器和非线性光学器件。

**Optical FDTD challenges**: (1) sub-wavelength features require fine meshing, (2) material dispersion ($\epsilon(\omega)$), (3) high Q-factor cavities need long simulation times, (4) nonlinear effects.
> **光学 FDTD 的挑战**：(1) 亚波长特征需要精细网格，(2) 材料色散，(3) 高 Q 值谐振腔需要长时间仿真，(4) 非线性效应。

## 16.2 Material Modeling
> 材料建模

### Drude Model (Metals)
> Drude 模型（金属）
$$
\epsilon(\omega) = \epsilon_\infty - \frac{\omega_p^2}{\omega^2 + j\omega\gamma}
$$

Implemented via auxiliary differential equation (ADE):
> 通过辅助微分方程实现：
$$
\frac{\partial \mathbf{P}}{\partial t} + \gamma \mathbf{P} = \epsilon_0 \omega_p^2 \mathbf{E}
$$

### Lorentz Model (Dielectrics)
> Lorentz 模型（介电材料）
$$
\epsilon(\omega) = \epsilon_\infty + \frac{(\epsilon_s - \epsilon_\infty)\omega_0^2}{\omega_0^2 - \omega^2 + j\omega\delta}
$$

ADE implementation:
> ADE 实现：
$$
\frac{\partial^2 \mathbf{P}}{\partial t^2} + \delta \frac{\partial \mathbf{P}}{\partial t} + \omega_0^2 \mathbf{P} = \epsilon_0 (\epsilon_s - \epsilon_\infty) \omega_0^2 \mathbf{E}
$$

### Sellmeier Model (Optical Glasses)
> Sellmeier 模型（光学玻璃）
$$
n^2(\lambda) = 1 + \sum_{k=1}^K \frac{B_k \lambda^2}{\lambda^2 - C_k}
$$

## 16.3 Optical Waveguides
> 光波导

### 16.3.1 Dielectric Slab Waveguide
> 介质平板波导

Mode field distribution: TE/TM modes solved via transcendental equation:
> 模式场分布：通过超越方程求解 TE/TM 模式：
TE: $\kappa d = m\pi + \tan^{-1}(\gamma/\kappa)$, where $\kappa = \sqrt{n_f^2 k_0^2 - \beta^2}$, $\gamma = \sqrt{\beta^2 - n_s^2 k_0^2}$
> TE 模：$\kappa d = m\pi + \tan^{-1}(\gamma/\kappa)$，其中 $\kappa = \sqrt{n_f^2 k_0^2 - \beta^2}$，$\gamma = \sqrt{\beta^2 - n_s^2 k_0^2}$

### 16.3.2 Channel Waveguides (Rib, Ridge)
> 通道波导（脊形、条形）

2D mode solvers (e.g., beam propagation method, finite difference) provide initial fields for FDTD propagation.
> 二维模式求解器（如光束传播法、有限差分法）为 FDTD 传播提供初始场。

### 16.3.3 Tapered Waveguides
> 锥形波导

Adiabatic taper design: $\theta < \lambda / (2w)$ taper angle ensures >95% transmission.
> 绝热锥形设计：锥角 $\theta < \lambda / (2w)$ 确保 >95% 传输。

## 16.4 Microcavity Resonators
> 微腔谐振器

### 16.4.1 Microdisk Resonators
> 微盘谐振器

Whispering-gallery modes (WGM) with Q > 10^6. FDTD computes:
> 回音壁模式，Q 值 > 10^6。FDTD 计算：
- Resonant frequencies (from FFT of time-domain decay)
  > 谐振频率（来自时域衰减的 FFT）
- Q-factor: $Q = \omega_0 \tau / 2$ where $\tau$ is the energy decay time constant
  > Q 值：$Q = \omega_0 \tau / 2$，$\tau$ 为能量衰减时间常数
- Mode field patterns
  > 模式场分布

### 16.4.2 Microring Resonators
> 微环谐振器

Add-drop filter configuration:
> 上载下载滤波器配置：
- Through-port transmission: $T = |1 - t e^{-j\phi}|^2$
  > 直通端口传输：
- Drop-port transmission: $D = |-\kappa e^{-j\phi/2}|^2$
  > 下载端口传输：
where $t^2 + \kappa^2 = 1$ and $\phi$ is the round-trip phase.
> 其中 $t^2 + \kappa^2 = 1$，$\phi$ 为往返相位。

### 16.4.3 Photonic Crystal Cavities
> 光子晶体谐振腔

Point defects in PhC slabs create high-Q cavities:
> 光子晶体平板中的点缺陷形成高 Q 谐振腔：
- Q > 10^6 for optimized designs
  > 优化设计可达 Q > 10^6
- Mode volume $V_{\text{mode}} < (\lambda/n)^3$
  > 模体积 $V_{\text{mode}} < (\lambda/n)^3$
- Purcell factor: $F_p = \frac{3}{4\pi^2} \left( \frac{\lambda}{n} \right)^3 \frac{Q}{V_{\text{mode}}}$
  > Purcell 因子：用于量化腔体对自发辐射的增强效应

### 16.4.4 Racetrack Resonators
> 跑道形谐振器

Elongated ring designs:
> 拉长的环形设计：
- Straight section length controls FSR
  > 直线段长度控制自由光谱范围
- Bend radius impacts radiation loss
  > 弯曲半径影响辐射损耗
- FDTD optimization for low-loss bends
  > FDTD 优化低损耗弯曲

## 16.5 Laterally Coupled Microcavity Disk Resonators
> 侧向耦合微腔盘谐振器

### 16.5.1 Mode Spectrum
> 模式频谱

First-order radial modes: periodic in azimuthal number $m$:
> 一阶径向模式：在方位角数 $m$ 上周期分布：
Resonant wavelengths follow: $m\lambda \approx 2\pi n_{\text{eff}} R$
> 谐振波长遵循：$m\lambda \approx 2\pi n_{\text{eff}} R$

### 16.5.2 Mode Suppression
> 模式抑制

Higher-order radial modes suppressed by:
> 高阶径向模式通过以下方式抑制：
- Optimizing coupling gap (evanescent coupling favors fundamental)
  > 优化耦合间隙（倏逝耦合偏好基模）
- Tapered waveguide couplers
  > 锥形波导耦合器

## 16.6 Photonic Crystal Waveguides
> 光子晶体波导

### Line Defect Waveguides
> 线缺陷波导

Removing a row of holes creates a waveguide within the bandgap.
> 移除一排孔在带隙内创建波导。
- Group velocity: $v_g = d\omega/dk$ (can be < c/100)
  > 群速度：$v_g = d\omega/dk$（可小于光速的 1/100）
- Slow-light regime enhances nonlinear effects
  > 慢光区域增强非线性效应
- FDTD computes dispersion diagram via Bloch boundary conditions
  > FDTD 通过 Bloch 边界条件计算色散图

## 16.7 Plasmonic Devices
> 等离激元器件

### Surface Plasmon Polaritons (SPP)
> 表面等离激元极化子

At metal-dielectric interfaces:
> 在金属-介质界面：
$$
k_{\text{SPP}} = k_0 \sqrt{\frac{\epsilon_m \epsilon_d}{\epsilon_m + \epsilon_d}}
$$

FDTD with Drude dispersion models SPP propagation and confinement.
> 带 Drude 色散模型的 FDTD 模拟 SPP 传播和约束。

### Plasmonic Waveguides
> 等离激元波导

- Metal strip waveguides: propagation length ~10-100 $\mu$m
  > 金属条带波导：传播长度约 10-100 $\mu$m
- V-groove channel plasmon polaritons: enhanced confinement
  > V 形槽通道等离激元极化子：增强约束
- FDTD predicts loss and mode profiles
  > FDTD 预测损耗和模式分布

## 16.8 Nonlinear Optics
> 非线性光学

### 16.8.1 Kerr Nonlinearity (Passive)
> Kerr 非线性（无源）

Third-order nonlinear polarization:
> 三阶非线性极化：
$$
\mathbf{P}_{\text{NL}} = \epsilon_0 \chi^{(3)} |\mathbf{E}|^2 \mathbf{E}
$$

FDTD ADE update:
> FDTD ADE 更新：
$$
\mathbf{D} = \epsilon_\infty \epsilon_0 \mathbf{E} + \mathbf{P}_{\text{NL}}
$$

### 16.8.2 Second-Harmonic Generation
> 二次谐波产生
$$
P_i(2\omega) = \epsilon_0 d_{ijk} E_j(\omega) E_k(\omega)
$$

FDTD naturally models SHG by including the nonlinear polarization in the Ampère update.
> FDTD 通过在安培定律更新式中包含非线性极化来自然模拟二次谐波产生。

### 16.8.3 Raman Amplification
> 拉曼放大

Stimulated Raman scattering modeled via coupled amplitude equations or full FDTD with Raman susceptibility.
> 受激拉曼散射通过耦合振幅方程或带拉曼极化率的完整 FDTD 建模。

## Summary
> 总结

| Device | Key FDTD Feature | Typical Q | Typical Size |
|--------|-----------------|-----------|--------------|
| 器件 | 关键 FDTD 特性 | 典型 Q 值 | 典型尺寸 |
| Microdisk | WGM resonance | $10^4-10^6$ | 2-10 $\mu$m radius |
| 微盘 | 回音壁模式谐振 | $10^4-10^6$ | 半径 2-10 $\mu$m |
| Microring | Add-drop filter | $10^3-10^5$ | 5-50 $\mu$m radius |
| 微环 | 上载下载滤波器 | $10^3-10^5$ | 半径 5-50 $\mu$m |
| PhC cavity | Defect mode | $10^4-10^7$ | Few $\mu$m |
| 光子晶体腔 | 缺陷模式 | $10^4-10^7$ | 几个 $\mu$m |
| SPP waveguide | Drude model | — | 10-100 $\mu$m |
| SPP 波导 | Drude 模型 | — | 10-100 $\mu$m |
| Nonlinear device | ADE for $\chi^{(2)}$, $\chi^{(3)}$ | — | Sub-mm |
| 非线性器件 | 使用 ADE 处理 $\chi^{(2)}$、$\chi^{(3)}$ | — | 亚毫米级 |
| PCF | Mode solver + FDTD | — | 1-10 cm |
| 光子晶体光纤 | 模式求解器 + FDTD | — | 1-10 cm |
| Laser | Coupled rate eq. | $10^3-10^6$ | 0.1-10 mm |
| 激光器 | 耦合速率方程 | $10^3-10^6$ | 0.1-10 mm |

## 16.9 Time-Domain Modeling of Nonlinear Optics
> 非线性光学的时域建模

### Kerr Effect (Third-Order)
> Kerr 效应（三阶）

The instantaneous Kerr nonlinearity is implemented directly in the FDTD Ampère update:
> 瞬时 Kerr 非线性直接在 FDTD 安培定律更新中实现：
$$
\nabla \times \mathbf{H} = \epsilon_0 \epsilon_\infty \frac{\partial \mathbf{E}}{\partial t} + \frac{\partial \mathbf{P}_{\text{NL}}}{\partial t}, \quad \mathbf{P}_{\text{NL}} = \epsilon_0 \chi^{(3)} |\mathbf{E}|^2 \mathbf{E}
$$

For large nonlinearities, Newton-Raphson iteration is required at each time-step.
> 对于大的非线性效应，每个时间步需要 Newton-Raphson 迭代。

### Second-Harmonic Generation (SHG)
> 二次谐波产生
$$
P_i(2\omega) = \epsilon_0 d_{ijk} E_j(\omega) E_k(\omega)
$$

FDTD naturally models SHG including phase matching and pulse walk-off.
> FDTD 自然建模 SHG，包括相位匹配和脉冲走离。

### Raman Amplification
> 拉曼放大

Stimulated Raman scattering modeled via the Raman susceptibility $\chi_R^{(3)}(\Omega)$, with peak gain at ~13 THz in silica.
> 受激拉曼散射通过拉曼极化率 $\chi_R^{(3)}(\Omega)$ 建模，在石英中峰值增益约在 13 THz。

## 16.10 Photonic Crystal Fibers (PCF)
> 光子晶体光纤

FDTD computes mode profiles, dispersion $D(\lambda)$, and confinement loss for:
> FDTD 计算模式分布、色散 $D(\lambda)$ 和约束损耗：
- **Index-guiding PCF**: solid core, air-hole cladding
  > **折射率导引型 PCF**：实芯，空气孔包层
- **Photonic bandgap fibers**: hollow core guided by cladding bandgap
  > **光子带隙光纤**：空芯，由包层带隙导引

Typical parameters: $\lambda_0/(20 n_{\text{core}})$ cell size, $10\Lambda \times 10\Lambda$ domain.
> 典型参数：网格大小 $\lambda_0/(20 n_{\text{core}})$，计算域 $10\Lambda \times 10\Lambda$。

## 16.11 Active Devices (Lasers, Amplifiers)
> 有源器件（激光器、放大器）

Gain via coupled rate equations:
> 通过耦合速率方程引入增益：
$$
\frac{\partial N}{\partial t} = R_p - \frac{N}{\tau} - \frac{g(N)}{\hbar\omega} |\mathbf{E}|^2, \quad g(N) = \frac{N_0 \sigma_g}{1 + I/I_{\text{sat}}}
$$

Spontaneous emission added as random polarization noise. Complete laser simulation includes Maxwell solver, carrier dynamics, noise, and output coupling.
> 自发辐射作为随机极化噪声添加。完整的激光器仿真包括 Maxwell 求解器、载流子动力学、噪声和输出耦合。

## Key Takeaways
> 关键要点

1. **Dispersion modeling** (Drude/Lorentz/ADE) is essential for optical-frequency FDTD.
   > **色散建模**对光频 FDTD 至关重要。
2. **High-Q cavities** require long simulation times; Padé extrapolation or Prony's method reduces requirements.
   > **高 Q 腔**需要长仿真时间；Padé 外推或 Prony 方法可降低要求。
3. **Nonlinear effects** (Kerr, SHG, Raman) are naturally handled via auxiliary polarization equations.
   > **非线性效应**通过辅助极化方程自然处理。
4. **Active device modeling** extends FDTD beyond passive structures to lasers and amplifiers.
   > **有源器件建模**将 FDTD 从无源结构扩展到激光器和放大器。
5. **PCF and plasmonic devices** push FDTD to its limits with sub-wavelength features.
   > **PCF 和等离激元器件**以亚波长特征将 FDTD 推向极限。
