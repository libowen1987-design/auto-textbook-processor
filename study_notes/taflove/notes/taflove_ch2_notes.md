---
chapter: 2
title: The One-Dimensional Scalar Wave Equation
book: Computational Electrodynamics — The Finite-Difference Time-Domain Method (3rd Ed.)
author: Allen Taflove, Susan C. Hagness
---

# Chapter 2: The One-Dimensional Scalar Wave Equation
> **中英双语版**

> 一维标量波动方程

## 2.1 Introduction
> 引言

This chapter introduces the numerical FDTD solution of the most basic PDE describing wave motion — the **one-dimensional scalar wave equation**.
> 本章介绍描述波动的最基本偏微分方程——**一维标量波动方程**的数值 FDTD 解法。

---

## 2.2 Propagating-Wave Solutions
> 传播波解

The one-dimensional scalar wave equation is:
> 一维标量波动方程为：
$$
\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2} \tag{2.1}
$$
where $u = u(x,t)$.
> 其中 $u = u(x,t)$。

### General Solution
> 通解

The general propagating-wave solution is:
> 传播波通解为：
$$
u(x,t) = F(x + ct) + G(x - ct) \tag{2.2}
$$
where $F(x + ct)$ represents a wave propagating in the $-x$ direction, and $G(x - ct)$ represents a wave propagating in the $+x$ direction.
> 其中 $F(x + ct)$ 代表沿 $-x$ 方向传播的波，$G(x - ct)$ 代表沿 $+x$ 方向传播的波。

> **Numerical Intuition:** The parameter $c$ is the wave propagation speed. After $\Delta t$ seconds, $F(x+ct)$ shifts left by $c\Delta t$, and $G(x-ct)$ shifts right by $c\Delta t$.
> **数值直觉：** 参数 $c$ 为波传播速度。经过 $\Delta t$ 秒后，$F(x+ct)$ 左移 $c\Delta t$，$G(x-ct)$ 右移 $c\Delta t$。

---

## 2.3 Dispersion Relation — Continuous
> 色散关系——连续情况

A **dispersion relation** expresses the dependence of wavelength $\lambda$ (or wavenumber $k$) on frequency $\omega$.
> **色散关系** 描述波长 $\lambda$（或波数 $k$）对频率 $\omega$ 的依赖性。

For the scalar wave equation, consider a sinusoidal traveling wave:
> 对标量波动方程，考虑正弦行波：
$$
u(x,t) = e^{j(\omega t - k x)} \tag{2.6}
$$

Substituting into (2.1) yields:
> 代入 (2.1) 得到：
$$
k = \pm \omega / c \tag{2.7b}
$$

### Physical Significance
> 物理意义

- **Phase velocity:** $v_p = \omega/k = \pm c$ — constant, independent of frequency
  > **相速度：** 常数，与频率无关
- **Group velocity:** $v_g = d\omega/dk = \pm c$ — also constant
  > **群速度：** 也是常数
- Since $v_p$ and $v_g$ are constant, waves are **dispersionless**.
  > 由于 $v_p$ 和 $v_g$ 均为常数，波是**无色散的**。

> **Numerical Intuition:** The continuous wave equation is nondispersive. But the *discrete* approximation introduces artificial dispersion — a key source of error in FDTD.
> **数值直觉：** 连续波动方程是无色散的。但*离散*近似会引入人工色散——这是 FDTD 中误差的关键来源。

---

## 2.4 Finite Differences
> 有限差分

### Central Difference for Second Spatial Derivative
> 空间二阶导数的中心差分

Using Taylor series expansions about $x_i$:
> 使用 $x_i$ 处的泰勒级数展开：
$$
\left.\frac{\partial^2 u}{\partial x^2}\right|_i^n = \frac{u_{i+1}^n - 2u_i^n + u_{i-1}^n}{(\Delta x)^2} + O[(\Delta x)^2] \tag{2.13}
$$

### Central Difference for Second Time Derivative
> 时间二阶导数的中心差分

By analogy:
> 类似地：
$$
\left.\frac{\partial^2 u}{\partial t^2}\right|_i^n = \frac{u_i^{n+1} - 2u_i^n + u_i^{n-1}}{(\Delta t)^2} + O[(\Delta t)^2] \tag{2.14}
$$

Both approximations are **second-order accurate**.
> 两个近似都是**二阶精度**。

---

## 2.5 Finite-Difference Approximation of the Scalar Wave Equation
> 标量波动方程的有限差分近似

Substituting (2.13) and (2.14) into (2.1):
> 将 (2.13) 和 (2.14) 代入 (2.1)：
$$
u_i^{n+1} = 2u_i^n - u_i^{n-1} + \left(\frac{c\Delta t}{\Delta x}\right)^2 (u_{i+1}^n - 2u_i^n + u_{i-1}^n) \tag{2.16}
$$

This is a **fully explicit** second-order accurate (2,2) scheme — no simultaneous equation solution is needed.
> 这是一个**完全显式**的二阶精度 (2,2) 格式——无需联立方程求解。

### The Magic Time-Step
> 魔法时间步

When $c\Delta t = \Delta x$ (Courant number $S = 1$), equation (2.16) simplifies to:
> 当 $c\Delta t = \Delta x$（Courant 数 $S = 1$）时，(2.16) 简化为：
$$
u_i^{n+1} = u_{i+1}^n + u_{i-1}^n - u_i^{n-1} \tag{2.17}
$$

**Remarkable property:** For $S = 1$, the solution is an **exact** solution to the original differential wave equation.
> **惊人的性质：** 当 $S = 1$ 时，解是原始微分波动方程的**精确**解。

> **Numerical Intuition:** The magic time-step causes truncation errors in space and time to exactly cancel. For Maxwell's equations in 2D/3D, the magic time-step does not exist in the same sense.
> **数值直觉：** 魔法时间步使空间和时间的截断误差完全抵消。对于 2D/3D 的麦克斯韦方程，不存在相同意义上的魔法时间步。

---

## 2.6 Numerical Dispersion Relation
> 数值色散关系

Consider a numerical sinusoidal traveling wave:
> 考虑数值正弦行波：
$$
u_i^n = e^{j(\omega n\Delta t - \tilde{k} i\Delta x)} \tag{2.20}
$$

Substituting into (2.16) yields:
> 代入 (2.16) 得到：
$$
\sin^2\left(\frac{\omega\Delta t}{2}\right) = \left(\frac{c\Delta t}{\Delta x}\right)^2 \sin^2\left(\frac{\tilde{k}\Delta x}{2}\right) \tag{2.22}
$$

This is the **numerical dispersion relation** — much more complicated than $k = \omega/c$.
> 这是**数值色散关系**——比 $k = \omega/c$ 复杂得多。

### 2.6.1 Case 1: Very Fine Sampling
> 情况 1：非常精细的采样

For $\omega\Delta t \ll 1$ and $\tilde{k}\Delta x \ll 1$, using small-angle approximations:
> 对于 $\omega\Delta t \ll 1$ 和 $\tilde{k}\Delta x \ll 1$，使用小角度近似：
$\tilde{k} \to k_0$, numerical dispersion vanishes.
> 数值色散消失。

### 2.6.2 Case 2: The Magic Time-Step ($S = 1$)
> 情况 2：魔法时间步

For $S = 1$, (2.22) becomes $\omega/\tilde{k} = \pm c$. **No numerical dispersion**.
> 当 $S = 1$ 时，**无数值色散**。

### 2.6.3 Case 3: Dispersive Wave Propagation ($S \neq 1$)
> 情况 3：色散波传播

For $S < 1$, $\tilde{k}$ can be complex. The numerical phase velocity:
> 对于 $S < 1$，$\tilde{k}$ 可为复数。数值相速度：
$$
v_p = \frac{\omega}{\tilde{k}_{\text{real}}}
$$

For $S = 0.5$: at $N_\lambda = 3$, minimum $v_p = (2/3)c$; as $N_\lambda \to 10$, $v_p \to c$.
> $S = 0.5$ 时：$N_\lambda = 3$ 时最小 $v_p = (2/3)c$；$N_\lambda \to 10$ 时 $v_p \to c$。

**Percent error in phase velocity** ($N_\lambda \gg 3$, $S = 0.5$):
> **相速度误差百分比**：
$$
\text{Error} \propto \frac{1}{N_\lambda^2} = \left(\frac{\Delta x}{\lambda}\right)^2
$$

---

## 2.7 Numerical Stability (CFL Condition)
> 数值稳定性（CFL 条件）

Using von Neumann analysis: allow $\tilde{\omega} = \omega_{\text{real}} + j\omega_{\text{imag}}$.
> 使用 von Neumann 分析：允许 $\tilde{\omega} = \omega_{\text{real}} + j\omega_{\text{imag}}$。

**Case (a): $0 \leq S \leq 1$** — $\tilde{\omega}$ is real-valued → constant amplitude. **Stable.**
> $0 \leq S \leq 1$ 时 $\tilde{\omega}$ 为实数→振幅恒定。**稳定。**

**Case (b): $S > 1$** — $\tilde{\omega}$ becomes complex with $\omega_{\text{imag}} < 0$ → exponential growth.
> $S > 1$ 时 $\tilde{\omega}$ 为复数→指数增长。

**CFL Condition:**
$$
S = \frac{c\Delta t}{\Delta x} \leq 1 \tag{2.52}
$$

> **Numerical Intuition:** The CFL condition ensures the numerical domain of dependence includes the physical domain of dependence. Named after Courant, Friedrichs, and Lewy (1928).
> **数值直觉：** CFL 条件确保数值依赖域包含物理依赖域。以 Courant、Friedrichs 和 Lewy（1928）命名。

---

## 2.8 Summary
> 总结

| Concept | Expression | Key Insight |
|---------|-----------|-------------|
| 概念 | 表达式 | 关键见解 |
| Wave equation / 波动方程 | $\partial^2 u / \partial t^2 = c^2 \partial^2 u / \partial x^2$ | Simplest wave PDE |
| Analytical solution / 解析解 | $u = F(x+ct) + G(x-ct)$ | Two propagating waves / 两个传播波 |
| FD approximation / 有限差分近似 | $u_i^{n+1} = 2u_i^n - u_i^{n-1} + S^2(u_{i+1}^n - 2u_i^n + u_{i-1}^n)$ | (2,2) explicit scheme / 显式格式 |
| CFL condition / CFL 条件 | $S = c\Delta t/\Delta x \leq 1$ | Required for stability / 稳定性要求 |
| Magic time-step / 魔法时间步 | $S = 1$ | Exact solution / 精确解 |
| Numerical dispersion / 数值色散 | $\sin^2(\omega\Delta t/2) = S^2 \sin^2(\tilde{k}\Delta x/2)$ | Pulse distortion / 脉冲畸变 |
| Minimum sampling / 最小采样 | $N_\lambda \geq 10$ recommended | For < 1% phase velocity error |

---

## Chapter Audit
> 章节审计

| Section | Content | ✓ |
|---------|---------|:-:|
| 章节 | 内容 | 完成 |
| 2.1 | Introduction / 引言 | ✓ |
| 2.2 | Propagating-wave solutions / 传播波解 | ✓ |
| 2.3 | Dispersion relation (continuous) / 色散关系（连续） | ✓ |
| 2.4 | Finite differences / 有限差分 | ✓ |
| 2.5 | FD approximation / 有限差分近似 | ✓ |
| 2.6 | Numerical dispersion / 数值色散 | ✓ |
| 2.7 | Numerical stability / 数值稳定性 | ✓ |
