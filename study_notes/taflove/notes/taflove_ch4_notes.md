---
chapter: 4
title: Numerical Dispersion and Stability
book: Computational Electrodynamics — The Finite-Difference Time-Domain Method (3rd Ed.)
author: Allen Taflove, Susan C. Hagness
---

# Chapter 4: Numerical Dispersion and Stability
> **中英双语版**

> 数值色散与稳定性

## 4.1 Introduction
> 引言

FDTD algorithms cause **nonphysical dispersion** — the phase velocity of numerical wave modes differs from $c$, varying with wavelength, propagation direction, and grid discretization. Think of a tenuous "numerical ether" causing phase errors, pulse broadening, ringing, anisotropy, and pseudorefraction.
> FDTD 算法会导致**非物理色散**——数值波模的相速度偏离物理光速 $c$，且随波长、传播方向和网格离散化程度变化。这类似于一种稀薄的"数值以太"，导致相位误差、脉冲展宽、振铃、各向异性和伪折射。

The time-step $\Delta t$ also has a **specific bound** (CFL condition) required to avoid numerical instability.
> 时间步长 $\Delta t$ 也存在避免数值不稳定的**特定界限**（CFL 条件）。

---

## 4.2 Derivation of 2D Numerical Dispersion Relation
> 二维数值色散关系推导

Starting from the 2D TM$_z$ Yee equations (lossless):
> 从二维 TM$_z$ Yee 方程（无耗）出发：
$$
\frac{\partial H_x}{\partial t} = -\frac{1}{\mu}\frac{\partial E_z}{\partial y},\quad
\frac{\partial H_y}{\partial t} = \frac{1}{\mu}\frac{\partial E_z}{\partial x},\quad
\frac{\partial E_z}{\partial t} = \frac{1}{\varepsilon}\left[\frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y}\right] \tag{4.1}
$$

Following substitution of a monochromatic plane wave trial solution:
> 代入单色平面波试探解：
$$
E_z\big|^n_{i,j} = E_{z0}\, e^{j(\omega n\Delta t - \tilde{k}_x i\Delta x - \tilde{k}_y j\Delta y)} \tag{4.3a}
$$

The derived dispersion relation for the 2D Yee algorithm (square cell, $\Delta x = \Delta y = \Delta$):
> 推导得到的二维 Yee 算法色散关系（正方形网格，$\Delta x = \Delta y = \Delta$）：
$$
\left[\frac{1}{S^2}\sin^2\left(\frac{\omega\Delta t}{2}\right)\right] = 
\sin^2\left(\frac{\tilde{k}_x\Delta}{2}\right) + \sin^2\left(\frac{\tilde{k}_y\Delta}{2}\right) \tag{4.5}
$$
其中 $S = c\Delta t/\Delta$ 为 Courant 数。

In terms of propagation angle $\phi$ and grid sampling density $N_\lambda = \lambda_0/\Delta$:
> 用传播角 $\phi$ 和网格采样密度 $N_\lambda = \lambda_0/\Delta$ 表示：
$$
\frac{1}{S^2}\sin^2\left(\frac{\pi S}{N_\lambda}\right) = 
\sin^2\left(\frac{\Delta k\cos\phi}{2}\right) + \sin^2\left(\frac{\Delta k\sin\phi}{2}\right) \tag{4.6}
$$

### Numerical Phase Velocity
> 数值相速度

**Along major axes** ($\phi = 0^\circ, 90^\circ$):
> **沿主轴方向**：
$$
k = \frac{2}{\Delta}\sin^{-1}\left[\frac{1}{S}\sin\left(\frac{\pi S}{N_\lambda}\right)\right],\quad
\frac{v_p}{c} = \frac{\pi}{N_\lambda S}\cdot\frac{1}{\sin^{-1}\left[\frac{1}{S}\sin\left(\frac{\pi S}{N_\lambda}\right)\right]} \tag{4.14}
$$

**Along grid diagonals** ($\phi = 45^\circ$):
> **沿网格对角线方向**：
$$
k = \frac{2\sqrt{2}}{\Delta}\sin^{-1}\left[\frac{1}{S\sqrt{2}}\sin\left(\frac{\pi S}{N_\lambda}\right)\right],\quad
\frac{v_p}{c} = \frac{\pi}{N_\lambda S}\cdot\frac{1}{\sqrt{2}\sin^{-1}\left[\frac{1}{S\sqrt{2}}\sin\left(\frac{\pi S}{N_\lambda}\right)\right]} \tag{4.15}
$$

---

## 4.3 Extension to 3D
> 推广到三维

The 3D numerical dispersion relation:
> 三维数值色散关系：
$$
\left[\frac{1}{c\Delta t}\sin\left(\frac{\omega\Delta t}{2}\right)\right]^2 = 
\left[\frac{1}{\Delta x}\sin\left(\frac{\tilde{k}_x\Delta x}{2}\right)\right]^2 + 
\left[\frac{1}{\Delta y}\sin\left(\frac{\tilde{k}_y\Delta y}{2}\right)\right]^2 + 
\left[\frac{1}{\Delta z}\sin\left(\frac{\tilde{k}_z\Delta z}{2}\right)\right]^2 \tag{4.12}
$$

### 4.4 Comparison with Ideal
> 与理想情况对比

Ideal (continuous) dispersion:
> 理想（连续）色散：
$$
\left(\frac{\omega}{c}\right)^2 = k_x^2 + k_y^2 + k_z^2 \tag{4.13}
$$

(4.12) → (4.13) as $\Delta x, \Delta y, \Delta z, \Delta t \to 0$.
> 当 $\Delta x, \Delta y, \Delta z, \Delta t \to 0$ 时，(4.12) 趋近于 (4.13)。

**Special cases where numerical = ideal:**
> **数值色散等于理想色散的特殊情况：**
- 3D diagonal propagation with $S = 1/\sqrt{3}$
  > 三维对角线传播，$S = 1/\sqrt{3}$
- 2D diagonal propagation with $S = 1/\sqrt{2}$
  > 二维对角线传播，$S = 1/\sqrt{2}$
- 1D with $S = 1$ (magic time-step)
  > 一维传播，$S = 1$（魔法时间步）

---

## 4.5 Anisotropy of Numerical Phase Velocity
> 数值相速度的各向异性

For $S = 0.5$, $N_\lambda = 20$:
> 当 $S = 0.5$, $N_\lambda = 20$ 时：
- Along axes: $v_p = 0.996892c$
  > 沿坐标轴方向：
- Along diagonals: $v_p = 0.998968c$
  > 沿对角线方向：
- Anisotropy: ~0.2%
  > 各向异性：约 0.2%

For $S = 1/\sqrt{2}$, $N_\lambda = 20$:
> 当 $S = 1/\sqrt{2}$, $N_\lambda = 20$ 时：
- Along axes: $v_p < c$ (subluminal)
  > 沿坐标轴：$v_p < c$（亚光速）
- Along diagonals: $v_p = c$ (ideal)
  > 沿对角线：$v_p = c$（理想值）
- The diagonal direction achieves zero dispersion at $S = 1/\sqrt{2}$
  > 对角线方向在 $S = 1/\sqrt{2}$ 时达到零色散

### 4.5.2 Intrinsic Grid Velocity Anisotropy
> 网格固有速度各向异性

The Yee grid is fundamentally anisotropic for numerical wave propagation. This anisotropy decreases with finer sampling ($\propto 1/N_\lambda^2$) and is minimized when $S$ is close to the stability limit.
> Yee 网格对于数值波传播本质上是各向异性的。各向异性随采样细化而减小（$\propto 1/N_\lambda^2$），并在 $S$ 接近稳定性极限时最小化。

> **Numerical Intuition:** For large electrically-sized problems (many $\lambda$), the cumulative phase error from anisotropy can cause serious problems (e.g., incorrect beam direction in phased arrays). Rule of thumb: $N_\lambda \geq 20$ for < 1% phase velocity error.
> **数值直觉：** 对于电大尺寸问题（很多个波长），各向异性引起的累积相位误差可能导致严重问题（如相控阵中波束方向错误）。经验法则：$N_\lambda \geq 20$ 可保证相速度误差 < 1%。

---

## 4.6 Complex-Valued Numerical Wavenumbers
> 复数值数值波数

When the grid sampling is too coarse ($N_\lambda < \pi/S$), $\tilde{k}$ becomes complex → numerical waves become evanescent (attenuate exponentially with distance). Two regimes:
> 当网格采样过于粗糙时，$\tilde{k}$ 变为复数 → 数值波变为倏逝波（随距离指数衰减）：

### 4.6.1 Propagation Along Principal Axes
> 沿主轴传播

Cutoff occurs when $\frac{1}{S}\sin\left(\frac{\pi S}{N_\lambda}\right) > 1$ → $N_\lambda < \pi S / \arcsin(S)$
> 截止发生在 $\frac{1}{S}\sin\left(\frac{\pi S}{N_\lambda}\right) > 1$ 时

### 4.6.2 Propagation Along Diagonal
> 沿对角线传播

Cutoff at finer sampling → diagonal propagation is more robust to coarse grids.
> 在更精细的采样处截止 → 对角线传播对粗网格更稳健。

---

## 4.7 Numerical Stability (CFL Condition)
> 数值稳定性（CFL 条件）

### Complex-Frequency Analysis
> 复频率分析

Allow $\tilde{\omega} = \omega_{\text{real}} + j\omega_{\text{imag}}$ and analyze (4.12):
> 允许 $\tilde{\omega} = \omega_{\text{real}} + j\omega_{\text{imag}}$ 并分析 (4.12)：

Define:
> 定义：
$$
\xi = c\Delta t \sqrt{\frac{\sin^2\left(\frac{k_x\Delta x}{2}\right)}{(\Delta x)^2} + \frac{\sin^2\left(\frac{k_y\Delta y}{2}\right)}{(\Delta y)^2} + \frac{\sin^2\left(\frac{k_z\Delta z}{2}\right)}{(\Delta z)^2}} \tag{4.51b}
$$

Maximum $\xi$ when all sine² terms = 1:
> 当所有正弦平方项等于 1 时 $\xi$ 取最大值：
$$
0 \leq \xi \leq c\Delta t \sqrt{\frac{1}{(\Delta x)^2} + \frac{1}{(\Delta y)^2} + \frac{1}{(\Delta z)^2}} \tag{4.52}
$$

**Stable:** $\xi \leq 1$ → real $\tilde{\omega}$ → bounded amplitude  
> **稳定：** $\xi \leq 1$ → $\tilde{\omega}$ 为实数 → 振幅有界
**Unstable:** $\xi > 1$ → complex $\tilde{\omega}$ with $\omega_{\text{imag}} < 0$ → exponential growth  
> **不稳定：** $\xi > 1$ → $\tilde{\omega}$ 为复数且 $\omega_{\text{imag}} < 0$ → 指数增长

### 3D CFL Condition
> 三维 CFL 条件

$$
\Delta t \leq \frac{1}{c\sqrt{\frac{1}{(\Delta x)^2} + \frac{1}{(\Delta y)^2} + \frac{1}{(\Delta z)^2}}} \tag{4.54}
$$

**Special cases:**
> **特殊情况：**
- **Cubic cell ($\Delta$):** $\Delta t \leq \Delta / (c\sqrt{3})$
  > **立方体网格：**
- **Square cell 2D:** $\Delta t \leq \Delta / (c\sqrt{2})$
  > **二维正方形网格：**
- **Uniform 1D:** $\Delta t \leq \Delta / c$
  > **一维均匀网格：**

**Growth factor for unstable case ($S > S_{\max}$):**
> **不稳定情况下的增长因子：**
$$
q_{\text{growth}} = \xi + \sqrt{\xi^2 - 1} > 1 \quad \text{per time-step} \tag{4.55}
$$

> **Numerical Intuition:** The CFL condition ensures that the numerical domain of dependence contains the physical domain of dependence. Violating CFL means the numerical wave "skips over" information it needs, causing unbounded growth — typically at the Nyquist mode (2-cell wavelength).
> **数值直觉：** CFL 条件确保数值依赖域包含物理依赖域。违反 CFL 意味着数值波"跳过"了它所需的信息，导致无界增长——通常出现在 Nyquist 模式（2 个网格单元的波长）。

---

## 4.8 Summary
> 总结

| Concept | Expression | Notes |
|---------|-----------|-------|
| 概念 | 表达式 | 说明 |
| 2D numerical dispersion | (4.5) or (4.6) | Square-cell TM$_z$ |
| 二维数值色散 | (4.5)/(4.6) | 正方形网格 TM$_z$ |
| 3D numerical dispersion | (4.12) | Full-vector Yee |
| 三维数值色散 | (4.12) | 全矢量 Yee |
| Ideal dispersion | (4.13) | Continuous limit |
| 理想色散 | (4.13) | 连续极限 |
| Phase velocity (axis) | (4.14) | $v_p < c$ for $S < 1$ |
| 相速度（主轴） | (4.14) | $S < 1$ 时 $v_p < c$ |
| Phase velocity (diagonal) | (4.15) | $v_p = c$ when $S = 1/\sqrt{2}$ |
| 相速度（对角线） | (4.15) | $S = 1/\sqrt{2}$ 时 $v_p = c$ |
| CFL 3D | $\Delta t \leq 1/(c\sqrt{1/\Delta x^2 + 1/\Delta y^2 + 1/\Delta z^2})$ | Cubic: $\Delta t \leq \Delta/(c\sqrt{3})$ |
| 三维 CFL | | 立方体网格 |
| CFL 2D | $\Delta t \leq \Delta/(c\sqrt{2})$ | Square cell |
| 二维 CFL | | 正方形网格 |
| CFL 1D | $\Delta t \leq \Delta/c$ | Magic step |
| 一维 CFL | | 魔法步长 |
| Anisotropy | $\propto 1/N_\lambda^2$ | Reduces with finer grids |
| 各向异性 | $\propto 1/N_\lambda^2$ | 随网格细化而减小 |

---

## Ch.4 Example Code
> 第 4 章示例代码

1. **Ex4.1:** Dispersion curves — $v_p/c$ vs $N_\lambda$ for axis/diagonal propagation  
   > 色散曲线——$v_p/c$ 随 $N_\lambda$ 变化
2. **Ex4.2:** Anisotropy visualization — 2D TM$_z$ simulation of cylindrical wave showing anisotropic wavefront  
   > 各向异性可视化——二维 TM$_z$ 柱面波仿真
3. **Ex4.3:** CFL stability — energy growth monitor for stable ($S=0.5$), marginal ($S=1/\sqrt{2}$), unstable ($S=1$)
   > CFL 稳定性——能量增长监测

## Chapter Audit
> 章节审计

| Section | Content | ✓ |
|---------|---------|:-:|
| 章节 | 内容 | 完成 |
| 4.1 | Introduction / 引言 | ✓ |
| 4.2 | 2D numerical dispersion / 二维数值色散 | ✓ |
| 4.3 | 3D extension / 三维推广 | ✓ |
| 4.4 | Comparison with ideal / 与理想对比 | ✓ |
| 4.5 | Anisotropy of $v_p$ / 相速度各向异性 | ✓ |
| 4.6 | Complex wavenumbers / 复波数 | ✓ |
| 4.7 | Numerical stability / 数值稳定性 | ✓ |
