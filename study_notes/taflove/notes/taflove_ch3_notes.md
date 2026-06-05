---
chapter: 3
title: Introduction to Maxwell's Equations and the Yee Algorithm
book: Computational Electrodynamics — The Finite-Difference Time-Domain Method (3rd Ed.)
author: Allen Taflove, Susan C. Hagness
---

# Chapter 3: Introduction to Maxwell's Equations and the Yee Algorithm
> **中英双语版**

> 麦克斯韦方程与 Yee 算法引论

## 3.1 Introduction
> 引言

This chapter presents the foundation of FDTD electromagnetic field analysis — the **Yee algorithm** (1966) [1]. Yee's insight was to choose a geometry for spatially sampling E and H field components that robustly represents both the differential and integral forms of Maxwell's equations.
> 本章介绍 FDTD 电磁场分析的基础——**Yee 算法**（1966）。Yee 的洞见是选择了一种在空间上采样电场和磁场分量的几何排列，能够稳健地表示麦克斯韦方程的微分和积分形式。

---

## 3.2 Maxwell's Equations in Three Dimensions
> 三维麦克斯韦方程

### Differential and Integral Forms
> 微分和积分形式

**Faraday's Law / 法拉第定律：**
$$
\frac{\partial\mathbf{B}}{\partial t} = -\nabla\times\mathbf{E} - \mathbf{M}
\qquad
\oint_L \mathbf{E}\cdot d\mathbf{L} = -\frac{\partial}{\partial t}\iint_A \mathbf{B}\cdot d\mathbf{A} - \iint_A \mathbf{M}\cdot d\mathbf{A} \tag{3.1}
$$

**Ampere's Law / 安培定律：**
$$
\frac{\partial\mathbf{D}}{\partial t} = \nabla\times\mathbf{H} - \mathbf{J}
\qquad
\oint_L \mathbf{H}\cdot d\mathbf{L} = \frac{\partial}{\partial t}\iint_A \mathbf{D}\cdot d\mathbf{A} + \iint_A \mathbf{J}\cdot d\mathbf{A} \tag{3.2}
$$

### Constitutive Relations (linear, isotropic, nondispersive)
> 本构关系（线性、各向同性、无色散）
$$
\mathbf{D} = \varepsilon\mathbf{E} = \varepsilon_r\varepsilon_0\mathbf{E}
\qquad
\mathbf{B} = \mu\mathbf{H} = \mu_r\mu_0\mathbf{H} \tag{3.5}
$$
where $\varepsilon_0 = 8.854\times10^{-12}$ F/m, $\mu_0 = 4\pi\times10^{-7}$ H/m.

### Maxwell's Curl Equations in Lossy Media
> 有耗介质中的麦克斯韦旋度方程

$$
\frac{\partial\mathbf{H}}{\partial t} = -\frac{1}{\mu}\nabla\times\mathbf{E} - \frac{1}{\mu}(\mathbf{M}_\text{source} + \sigma^*\mathbf{H}) \tag{3.7}
$$
$$
\frac{\partial\mathbf{E}}{\partial t} = \frac{1}{\varepsilon}\nabla\times\mathbf{H} - \frac{1}{\varepsilon}(\mathbf{J}_\text{source} + \sigma\mathbf{E}) \tag{3.8}
$$

### Cartesian Component Equations
> 笛卡尔分量方程

Expanding the curl operators yields six coupled scalar equations (3.9a-c and 3.10a-c).
> 展开旋度算符得到六个耦合的标量方程。

> **Numerical Intuition:** These six equations are the core of FDTD. Each E-component update uses four surrounding H-components, and vice versa, creating a self-consistent electromagnetic simulation.
> **数值直觉：** 这六个方程是 FDTD 的核心。每个电场分量更新使用四个环绕的磁场分量，反之亦然，形成一个自洽的电磁仿真。

---

## 3.3 Reduction to Two Dimensions
> 降维到二维

### 3.3.1 TM$_z$ Mode ($E_z, H_x, H_y$)
> TM$_z$ 模式
$$
\frac{\partial H_x}{\partial t} = -\frac{1}{\mu}\frac{\partial E_z}{\partial y},\quad
\frac{\partial H_y}{\partial t} = \frac{1}{\mu}\frac{\partial E_z}{\partial x},\quad
\frac{\partial E_z}{\partial t} = \frac{1}{\varepsilon}\left[\frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y}\right] \tag{3.13a-c}
$$

### 3.3.2 TE$_z$ Mode ($H_z, E_x, E_y$)
> TE$_z$ 模式
$$
\frac{\partial E_x}{\partial t} = \frac{1}{\varepsilon}\frac{\partial H_z}{\partial y},\quad
\frac{\partial E_y}{\partial t} = -\frac{1}{\varepsilon}\frac{\partial H_z}{\partial x},\quad
\frac{\partial H_z}{\partial t} = \frac{1}{\mu}\left[\frac{\partial E_x}{\partial y} - \frac{\partial E_y}{\partial x}\right] \tag{3.14a-c}
$$

---

## 3.4 Reduction to One Dimension — TEM Modes
> 降维到一维——TEM 模式

$x$-Directed, $z$-Polarized TEM Mode ($E_z, H_y$):
> $x$ 方向传播、$z$ 极化的 TEM 模式：
$$
\frac{\partial H_y}{\partial t} = \frac{1}{\mu}\frac{\partial E_z}{\partial x},\quad
\frac{\partial E_z}{\partial t} = \frac{1}{\varepsilon}\frac{\partial H_y}{\partial x} \tag{3.15a-b}
$$

---

## 3.6 The Yee Algorithm
> Yee 算法

### 3.6.1 Basic Ideas
> 基本思想

1. **Solves both E and H** using coupled curl equations (not wave equation alone).
   > 使用耦合旋度方程**同时求解 E 和 H**。
2. **Staggered spatial grid:** Every E component surrounded by four circulating H components, and vice versa.
   > **交错空间网格：** 每个 E 分量周围有四个环绕的 H 分量，反之亦然。
3. **Leapfrog time-stepping:** All E computations completed first, then all H computations using the new E data.
   > **蛙跳时间步进：** 先完成所有 E 计算，然后使用新的 E 数据完成所有 H 计算。

**Key attributes:**
> **关键特性：**
- Central-difference space derivatives → second-order accurate
  > 中心差分空间导数→二阶精度
- Tangential E and H continuity naturally maintained at material interfaces
  > 材料界面处自动维持切向 E 和 H 连续性
- Implicitly enforces Gauss' laws (divergence-free)
  > 隐式满足高斯定律（无散）
- Fully explicit → no matrix inversion needed
  > 完全显式→无需矩阵求逆
- Nondissipative: numerical waves do not spuriously decay
  > 无耗散：数值波不会虚假衰减

### 3.6.3 Finite-Difference Expressions in 3D
> 三维有限差分表达式

**E-field update** (example for $E_x$):
> **电场更新**（以 $E_x$ 为例）：
$$
E_x\big|^{n+1/2}_{i, j+1/2, k+1/2} = C_{\text{ae}}\cdot E_x\big|^{n-1/2}_{i, j+1/2, k+1/2} + C_{\text{be}} \cdot \left[\frac{H_z|^{n}_{i, j+1, k+1/2} - H_z|^{n}_{i, j, k+1/2}}{\Delta y} - \frac{H_y|^{n}_{i, j+1/2, k+1} - H_y|^{n}_{i, j+1/2, k}}{\Delta z}\right] \tag{3.29a}
$$
where:
> 其中：
$$
C_{\text{ae}} = \frac{1 - \frac{\sigma\Delta t}{2\varepsilon}}{1 + \frac{\sigma\Delta t}{2\varepsilon}}, \qquad
C_{\text{be}} = \frac{\frac{\Delta t}{\varepsilon}}{1 + \frac{\sigma\Delta t}{2\varepsilon}} \tag{3.30}
$$

**H-field update** (example for $H_x$):
> **磁场更新**（以 $H_x$ 为例）：
$$
H_x\big|^{n+1}_{i-1/2, j+1, k+1} = C_{\text{ah}}\cdot H_x\big|^{n}_{i-1/2, j+1, k+1} - C_{\text{bh}} \cdot \left[\frac{E_z|^{n+1/2}_{i-1/2, j+1, k+1} - E_z|^{n+1/2}_{i-1/2, j, k+1}}{\Delta y} - \frac{E_y|^{n+1/2}_{i-1/2, j+1, k+1} - E_y|^{n+1/2}_{i-1/2, j+1, k}}{\Delta z}\right] \tag{3.31a}
$$
where:
> 其中：
$$
C_{\text{ah}} = \frac{1 - \frac{\sigma^*\Delta t}{2\mu}}{1 + \frac{\sigma^*\Delta t}{2\mu}}, \qquad
C_{\text{bh}} = \frac{\frac{\Delta t}{\mu}}{1 + \frac{\sigma^*\Delta t}{2\mu}} \tag{3.32}
$$

### 3.6.9 Divergence-Free Nature
> 无散性质

The Yee algorithm implicitly enforces Gauss' laws $\nabla\cdot\mathbf{D} = 0$ and $\nabla\cdot\mathbf{B} = 0$.
> Yee 算法隐式满足高斯定律。

---

## 3.9 Summary
> 总结

| Concept | Key Result |
|---------|----------|
| 概念 | 关键结果 |
| Yee unit cell / Yee 单元网格 | E and H staggered in space / E、H 空间交错 |
| Leapfrog time-stepping / 蛙跳时间步进 | E, H staggered in time / E、H 时间交错 |
| E-field update / 电场更新 | (3.29) with (3.30) — explicit / 显式 |
| H-field update / 磁场更新 | (3.31) with (3.32) — explicit / 显式 |
| Divergence-free / 无散 | Gauss' laws implicitly satisfied / 隐式满足高斯定律 |
| CFL stability / CFL 稳定性 | $\Delta t \leq 1/(c\sqrt{1/\Delta x^2 + 1/\Delta y^2 + 1/\Delta z^2})$ |

**Yee cell geometry / Yee 网格几何：**
- $E_x$: center of x-directed edge / x 方向边中心
- $E_y$: center of y-directed edge / y 方向边中心
- $E_z$: center of z-directed edge / z 方向边中心
- $H_x$: center of x-directed face / x 方向面中心
- $H_y$: center of y-directed face / y 方向面中心
- $H_z$: center of z-directed face / z 方向面中心
