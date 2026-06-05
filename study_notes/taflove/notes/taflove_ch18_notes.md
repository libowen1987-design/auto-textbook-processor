---
chapter: 18
title: "Unconditionally Stable FDTD Methods"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, F. Zheng, Z. Chen, Y. T. Lo"
raw_size: 53,397 bytes
---

# Chapter 18: Unconditionally Stable FDTD Methods
> **中英双语版**

> 无条件稳定 FDTD 方法

## 18.1 Introduction
> 引言

Standard FDTD is **conditionally stable**: $\Delta t$ is bounded by the CFL limit. For problems with very small cells (fine features, high mesh grading), the time-step becomes prohibitively small. Unconditionally stable methods remove this bound, allowing $\Delta t$ set by accuracy rather than stability.
> 标准 FDTD 是**条件稳定**的：$\Delta t$ 受 CFL 极限限制。对于具有极小网格单元的问题（精细特征、高网格分级），时间步长变得过小而无法接受。无条件稳定方法消除了这一限制，使 $\Delta t$ 由精度而非稳定性决定。

## 18.2 ADI-FDTD (Alternating Direction Implicit)
> 交替方向隐式 FDTD

### 18.2.1 Formulation
> 公式推导

Splits each time-step into two sub-steps. In sub-step 1, $x$-direction derivatives are implicit:
> 将每个时间步分解为两个子步。在子步1中，$x$ 方向导数为隐式：

**Sub-step 1** ($n \to n+1/2$):
> **子步 1**：
$$
E_x^{n+1/2} = E_x^n + \frac{\Delta t}{2\epsilon} \left[ \frac{\delta H_z}{\delta y} - \frac{\delta H_y^{n+1/2}}{\delta z} \right]
$$
$$
H_y^{n+1/2} = H_y^n + \frac{\Delta t}{2\mu} \left[ \frac{\delta E_x^{n+1/2}}{\delta z} - \frac{\delta E_z}{\delta x} \right]
$$

The $z$-directed derivatives are implicit, requiring solution of a tridiagonal system.
> $z$ 方向导数为隐式，需要求解三对角方程组。

**Sub-step 2** ($n+1/2 \to n+1$):
> **子步 2**：
$$
E_x^{n+1} = E_x^{n+1/2} + \frac{\Delta t}{2\epsilon} \left[ \frac{\delta H_z^{n+1}}{\delta y} - \frac{\delta H_y}{\delta z} \right]
$$

### 18.2.2 Tridiagonal System
> 三对角方程组

The implicit step yields (for $E_x$ update):
> 隐式步骤产生（以 $E_x$ 更新为例）：
$$
-\alpha E_x^{n+1/2}(k-1) + (1+2\alpha) E_x^{n+1/2}(k) - \alpha E_x^{n+1/2}(k+1) = RHS
$$
where $\alpha = \Delta t^2/(4\mu\epsilon\Delta z^2)$. This tridiagonal system is efficiently solved via Thomas algorithm in $O(N)$.
> 其中 $\alpha = \Delta t^2/(4\mu\epsilon\Delta z^2)$。该三对角系统可通过 Thomas 算法高效求解，复杂度为 $O(N)$。

### 18.2.3 Accuracy
> 精度

ADI-FDTD introduces:
> ADI-FDTD 引入了：
- **Splitting error**: $O(\Delta t^2)$ — negligible when $\Delta t$ is at CFL or smaller
  > **分裂误差**：$O(\Delta t^2)$——当 $\Delta t$ 等于或小于 CFL 时可忽略
- **Numerical dispersion**: Increased for large $\Delta t$; the dispersion relation is:
  > **数值色散**：当 $\Delta t$ 较大时增加；色散关系为：
$$
\left[ \frac{1}{c\Delta t} \sin\left(\frac{\omega\Delta t}{2}\right) \right]^2 = \sum_{\xi=x,y,z} \left[ \frac{1}{\Delta_\xi} \sin\left(\frac{k_\xi\Delta_\xi}{2}\right) \right]^2 \frac{1}{1 + (\Delta t^2/(4\mu\epsilon)) \sum \left[ \frac{1}{\Delta_\xi} \sin\left(\frac{k_\xi\Delta_\xi}{2}\right) \right]^2 }
$$

For $\Delta t \ll$ CFL, reduces to standard FDTD dispersion.
> 当 $\Delta t \ll$ CFL 时，退化为标准 FDTD 色散关系。

## 18.3 Crank-Nicolson FDTD
> Crank-Nicolson FDTD

### CN Scheme
> CN 格式

Applies Crank-Nicolson time-stepping (trapezoidal integration) directly:
> 直接应用 Crank-Nicolson 时间步进（梯形积分）：
$$
\frac{\mathbf{U}^{n+1} - \mathbf{U}^n}{\Delta t} = \frac{1}{2} \left[ \mathbf{A}\mathbf{U}^{n+1} + \mathbf{A}\mathbf{U}^n \right]
$$
where $\mathbf{U} = [E_x, E_y, E_z, H_x, H_y, H_z]^T$. This yields:
> 其中 $\mathbf{U} = [E_x, E_y, E_z, H_x, H_y, H_z]^T$。由此得到：
$$
\left( \mathbf{I} - \frac{\Delta t}{2} \mathbf{A} \right) \mathbf{U}^{n+1} = \left( \mathbf{I} + \frac{\Delta t}{2} \mathbf{A} \right) \mathbf{U}^n
$$

### CNSS (Crank-Nicolson Split-Step)
> CNSS（Crank-Nicolson 分裂步）

Splits the 3D Maxwell operator into three 1D operators:
> 将三维 Maxwell 算符分裂为三个一维算符：
$$
\mathbf{U}^{n+1} = \prod_{\xi=x,y,z} \left( \mathbf{I} - \frac{\Delta t}{2} \mathbf{A}_\xi \right)^{-1} \left( \mathbf{I} + \frac{\Delta t}{2} \mathbf{A}_\xi \right) \mathbf{U}^n
$$

Each 1D step requires only tridiagonal solves, making CNSS more efficient than full CN.
> 每个一维步骤只需三对角求解，使 CNSS 比完整 CN 更高效。

## 18.4 Laguerre-FDTD
> Laguerre-FDTD

Uses Laguerre polynomials as temporal basis functions:
> 使用 Laguerre 多项式作为时间基函数：
$$
E(r, t) = \sum_{p=0}^P E_p(r) L_p(\zeta t) e^{-\zeta t/2}
$$
where $L_p$ is the $p$th Laguerre polynomial. This eliminates the time-marching entirely:
> 其中 $L_p$ 为第 $p$ 阶 Laguerre 多项式。这完全消除了时间步进：
- All temporal derivatives are handled analytically by Laguerre properties
  > 所有时间导数通过 Laguerre 多项式性质解析处理
- A **single** large sparse matrix equation is solved for all expansion coefficients
  > 求解**单个**大型稀疏矩阵方程得到所有展开系数
- No CFL constraint — the only constraint is $P$ (number of temporal basis functions)
  > 无 CFL 约束——唯一约束是 $P$（时间基函数数量）

### Implementation
> 实现

The time-domain Maxwell equations become:
> 时域麦克斯韦方程组变为：
$$
\left( \nabla \times \right) \mathbf{H}_p = \left( \frac{\zeta}{2} + jp \zeta \right) \epsilon \mathbf{E}_p + \mathbf{J}_p
$$
$$
\left( \nabla \times \right) \mathbf{E}_p = -\left( \frac{\zeta}{2} + jp \zeta \right) \mu \mathbf{H}_p
$$

A marching-on-in-order scheme solves for $\mathbf{E}_p$, $\mathbf{H}_p$ sequentially from $p=0$ to $P$.
> 按阶步进格式依次求解 $\mathbf{E}_p$、$\mathbf{H}_p$，从 $p=0$ 到 $P$。

## 18.5 Comparison
> 方法对比

| Method | System Size | Accuracy | Implementation | Parallel |
|--------|------------|----------|---------------|----------|
| 方法 | 求解规模 | 精度 | 实现难度 | 并行性 |
| ADI-FDTD | Tridiagonal (×6) | $O(\Delta t^2)$ error | Moderate | Good |
| ADI-FDTD | 三对角 (×6) | $O(\Delta t^2)$ 误差 | 中等 | 好 |
| CN-FDTD | Large sparse | $O(\Delta t^2)$ | Complex | Poor |
| CN-FDTD | 大型稀疏阵 | $O(\Delta t^2)$ | 复杂 | 差 |
| CNSS | Tridiagonal (×3) | $O(\Delta t^2)$ | Moderate | Good |
| CNSS | 三对角 (×3) | $O(\Delta t^2)$ | 中等 | 好 |
| Laguerre-FDTD | Large sparse | Spectral in time | Very complex | Poor |
| Laguerre-FDTD | 大型稀疏阵 | 时间谱精度 | 非常复杂 | 差 |

### Practical Guidance
> 实用指南

- **ADI-FDTD** is the most widely used unconditionally stable method
  > **ADI-FDTD** 是使用最广泛的无条件稳定方法
- For $\Delta t \leq 5\times$ CFL, accuracy is acceptable
  > 当 $\Delta t \leq 5\times$ CFL 时，精度可接受
- For $\Delta t > 10\times$ CFL, dispersion error becomes significant
  > 当 $\Delta t > 10\times$ CFL 时，色散误差变得显著
- Laguerre-FDTD is useful for problems requiring very long simulation times (high-Q cavities)
  > Laguerre-FDTD 适用于需要极长仿真时间的问题（高 Q 值谐振腔）
