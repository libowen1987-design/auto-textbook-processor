# Taflove & Hagness — Computational Electrodynamics: The FDTD Method (3rd Ed.)
> **中英双语版**

> Taflove & Hagness — 计算电动力学：FDTD 方法（第三版）

> Allen Taflove, Susan C. Hagness. Artech House, 2005. ISBN 1-58053-832-0.

---

## Part I: Maxwell's Yee Algorithm
> 第一部分：麦克斯韦 Yee 算法

### 1.1 The Yee Grid
> Yee 网格

**Core idea:** Discretize space and time such that the electric and magnetic field components are interleaved on a staggered grid.
> **核心思想：** 离散化空间和时间，使电场和磁场分量在交错网格上交织排列。

**Yee cell (3D):** A unit cube of size Δx × Δy × Δz.
> **Yee 网格单元（三维）：** 大小为 Δx × Δy × Δz 的单位立方体。

Field components are placed as:
> 场分量放置如下：
- E_x at (i+½, j,   k  )
- E_y at (i,   j+½, k  )
- E_z at (i,   j,   k+½)
- H_x at (i,   j+½, k+½)
- H_y at (i+½, j,   k+½)
- H_z at (i+½, j+½, k  )

**Temporal staggering:** E at integer time steps, H at half-integer time steps → **leapfrog** scheme.
> **时间交错：** E 在整数时间步，H 在半整数时间步→**蛙跳**格式。

### 1.2 1D FDTD Update Equations
> 一维 FDTD 更新方程

Assume TEM wave propagating along z, with E_x and H_y components:
> 假设 TEM 波沿 z 传播，具有 E_x 和 H_y 分量：

**Electric field update (E_x):**
> **电场更新：**
$$E_x^{n+1}(k) = E_x^n(k) + \frac{\Delta t}{\epsilon \Delta z} \left[H_y^{n+1/2}(k+\tfrac12) - H_y^{n+1/2}(k-\tfrac12)\right]$$

**Magnetic field update (H_y):**
> **磁场更新：**
$$H_y^{n+1/2}(k+\tfrac12) = H_y^{n-1/2}(k+\tfrac12) + \frac{\Delta t}{\mu \Delta z} \left[E_x^{n}(k+1) - E_x^{n}(k)\right]$$

### 1.3 2D and 3D Update Equations
> 二维和三维更新方程

**2D TM_z mode** (E_z, H_x, H_y non-zero):
> **二维 TM_z 模式：**

$$E_z^{n+1}(i,j) = E_z^n(i,j) + \frac{\Delta t}{\epsilon}\left[\frac{H_y^{n+1/2}(i+\tfrac12,j) - H_y^{n+1/2}(i-\tfrac12,j)}{\Delta x} - \frac{H_x^{n+1/2}(i,j+\tfrac12) - H_x^{n+1/2}(i,j-\tfrac12)}{\Delta y}\right]$$

### 1.4 Numerical Dispersion
> 数值色散

**The FDTD grid introduces a non-physical dispersion relation:**
> **FDTD 网格引入了非物理的色散关系：**

$$\left[\frac{1}{c\Delta t}\sin\left(\frac{\omega\Delta t}{2}\right)\right]^2 = \sum_{\alpha=x,y,z} \left[\frac{1}{\delta}\sin\left(\frac{k_\alpha\delta}{2}\right)\right]^2$$

Key consequences:
> 关键后果：
- **Numerical phase velocity ≠ c.** Depends on frequency, direction, and grid resolution.
  > 数值相速度 ≠ c，取决于频率、方向和网格分辨率。
- **Grid anisotropy:** Waves travel at different speeds in different directions.
  > 网格各向异性：波在不同方向以不同速度传播。
- **Mitigation:** Use at least 10–20 cells per wavelength (Δ ≤ λ/10 to λ/20).
  > 缓解方法：每波长至少 10-20 个网格单元。

### 1.5 Stability: The Courant Condition
> 稳定性：Courant 条件

**CFL condition:**
- 1D: c·Δt ≤ Δz
- 2D: c·Δt ≤ δ/√2
- 3D: c·Δt ≤ δ/√3

**In practice:** Choose S_c = 0.5 for safety margin.
> **在实践中：** 选择 S_c = 0.5 作为安全裕度。

---

## Part II: Absorbing Boundary Conditions
> 第二部分：吸收边界条件

### 2.1 Mur Absorbing Boundary Conditions
> Mur 吸收边界条件

**First-order Mur ABC** (for 1D, z-direction):
> **一阶 Mur ABC**（一维，z 方向）：

$$E_x^{n+1}(1) = E_x^n(2) + \frac{c\Delta t - \Delta z}{c\Delta t + \Delta z}\left[E_x^{n+1}(2) - E_x^n(1)\right]$$

**Limitations:** Mur ABCs work well only for near-normal incidence.
> **局限性：** Mur ABC 仅对近正入射效果良好。

### 2.2 Berenger's Split-Field PML
> Berenger 分裂场 PML

**Key insight:** Split each field component into two sub-components and introduce artificial conductivities.
> **关键见解：** 将每个场分量分裂为两个子分量，引入人工电导率。

**Impedance matching condition:**
> **阻抗匹配条件：**
$$\frac{\sigma_x}{\epsilon_0} = \frac{\sigma_x^*}{\mu_0}$$

**Polynomial grading:** σ(x) = σ_max·(x/d)^m
> **多项式渐变：** σ(x) = σ_max·(x/d)^m

### 2.3 Uniaxial PML (UPML)
> 单轴 PML

Replaces split-field with anisotropic material tensor. Simpler to implement and more physically intuitive.
> 用各向异性材料张量替代分裂场。实现更简单，物理更直观。

### 2.4 Convolutional PML (CPML)
> 卷积 PML

Uses complex-frequency-shifted (CFS) tensor: s_α = κ_α + σ_α/(α_α + jωε₀)
> 使用复频移张量：

**Recommended parameters:** 8–16 cells thick, κ_max = 1–11, α_opt = 0.08–0.8
> **推荐参数：** 8–16 网格厚，κ_max = 1–11，α_opt = 0.08–0.8

---

## Part III: Source Excitation & Near-to-Far-Field
> 第三部分：源激励与近远场变换

### 3.1 Total-Field / Scattered-Field Formulation
> 总场/散射场公式

**TFSF** divides the grid into total-field and scattered-field regions, separated by a Huygens surface.
> **TFSF** 将网格分为总场和散射场区域，由惠更斯面分隔。

### 3.3 Time-Harmonic and Broadband Sources
> 时谐和宽带源

**Gaussian pulse:** $f(t) = e^{-(t-t_0)^2/T^2}$
> **高斯脉冲：**
**Ricker wavelet:** $f(t) = [1 - 2((t-t_0)/T)^2] e^{-(t-t_0)^2/T^2}$
> **Ricker 子波：**
**Modulated Gaussian:** $f(t) = \sin(\omega_c(t-t_0)) \cdot e^{-(t-t_0)^2/T^2}$
> **调制高斯脉冲：**

### 3.4 Near-to-Far-Field Transformation
> 近远场变换

**RCS (Radar Cross Section):**
> **雷达散射截面：**
$$\sigma(\theta,\phi) = \lim_{r\to\infty} 4\pi r^2 \frac{|\mathbf{E}_{\text{scat}}|^2}{|\mathbf{E}_{\text{inc}}|^2}$$

---

## Part IV: Dispersive, Nonlinear & Gain Media
> 第四部分：色散、非线性和增益介质

### 4.1 Debye, Drude, and Lorentz Models
> Debye、Drude 和 Lorentz 模型

**Debye model:** $\epsilon(\omega) = \epsilon_\infty + \frac{\epsilon_s - \epsilon_\infty}{1 + j\omega\tau}$
> **Debye 模型：**（极化介质、水）

**Drude model:** $\epsilon(\omega) = \epsilon_\infty - \frac{\omega_p^2}{\omega^2 + j\omega\Gamma}$
> **Drude 模型：**（金属、等离子体）

**Lorentz model:** $\epsilon(\omega) = \epsilon_\infty + \frac{(\epsilon_s - \epsilon_\infty)\omega_0^2}{\omega_0^2 + 2j\omega\delta - \omega^2}$
> **Lorentz 模型：**（谐振吸收带）

### 4.2 Auxiliary Differential Equation (ADE) Method
> 辅助微分方程法

Convert frequency-domain constitutive relation to ODE in time, discretized with central differences.
> 将频域本构关系转换为时间的常微分方程，使用中心差分离散。

### 4.3 Recursive Convolution (RC) and PLRC Methods
> 递归卷积法

PLRC assumes E(t) varies linearly within each time step, providing higher accuracy for dispersive media.
> PLRC 假设 E(t) 在每个时间步内线性变化，为色散介质提供更高精度。

### 4.4 Nonlinear and Gain Media
> 非线性和增益介质

**Kerr nonlinearity:** n = n₀ + n₂I. Solved via Newton's method or iterative approach.
> **Kerr 非线性：** 通过牛顿法或迭代法求解。

**Gain media:** Maxwell's equations couple to two-level quantum system via Maxwell-Bloch equations.
> **增益介质：** 通过 Maxwell-Bloch 方程将麦克斯韦方程与二能级量子系统耦合。

---

## Part V: Applications
> 第五部分：应用

### 5.1 Scattering / 散射
### 5.2 Antennas and Microwave Circuits / 天线和微波电路
### 5.3 Photonics / 光子学
### 5.4 Bioelectromagnetics / 生物电磁学

**SAR:** $\text{SAR} = \frac{\sigma_{\text{eff}} |E|^2}{2\rho}$
> **比吸收率：**

---

## Key Equations Reference
> 关键方程参考

| Concept | Equation | Key Parameters |
|---------|----------|---------------|
| 概念 | 方程 | 关键参数 |
| 1D E-update / 一维 E 更新 | E_x^{n+1}(k) = E_x^n(k) + (Δt/(εΔz))[H_y(k+½) − H_y(k−½)] | Δt, ε, Δz |
| 1D H-update / 一维 H 更新 | H_y^{n+½}(k+½) = H_y^{n-½}(k+½) + (Δt/(μΔz))[E_x(k+1) − E_x(k)] | Δt, μ, Δz |
| Courant limit (3D) / 三维 Courant 极限 | c·Δt ≤ Δ / √3 | uniform Δ |
| Numerical dispersion / 数值色散 | sin²(ωΔt/2) / (cΔt)² = Σ sin²(k_α·Δ/2) / Δ² | need Δ ≤ λ/10 |
| PML σ grading / PML 渐变 | σ(x) = σ_max·(x/d)^m | m = 2–4 |
| CPML s_α | s_α = κ_α + σ_α/(α_α + jωε₀) | κ≥1, α≈0.08 |
| Debye model / Debye 模型 | ε = ε_∞ + (ε_s−ε_∞)/(1+jωτ) | τ = relaxation time |
| Drude model / Drude 模型 | ε = ε_∞ − ω_p²/(ω²+jωΓ) | ω_p = plasma freq |
| Lorentz model / Lorentz 模型 | ε = ε_∞ + Δε·ω₀²/(ω₀²+2jωδ−ω²) | ω₀ = resonant freq |
