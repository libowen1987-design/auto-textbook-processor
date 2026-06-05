---
chapter: 6
title: Analytical Absorbing Boundary Conditions
book: Computational Electrodynamics — The Finite-Difference Time-Domain Method (3rd Ed.)
author: Allen Taflove, Susan C. Hagness
raw_size: 91,684 bytes
sections: 5
---

# Chapter 6: Analytical Absorbing Boundary Conditions
> **中英双语版**

> 解析吸收边界条件

## 6.1 Introduction
> 引言

FDTD models of open-region problems require the computational domain to be truncated by an **absorbing boundary condition (ABC)** that simulates extension to infinity. ABCs permit outward-propagating numerical waves to exit the domain with minimal spurious reflection.
> 开域问题的 FDTD 模型需要用**吸收边界条件**截断计算域，模拟向无穷远处的延伸。ABC 允许向外传播的数值波以最小的虚假反射离开计算域。

ABCs cannot be directly obtained from the central-difference Yee algorithm, which requires field values one-half cell outside the boundary. Modern ABCs achieve reflection coefficients of $10^{-4}$ to $10^{-6}$, enabling 70+ dB dynamic range.
> ABC 不能直接从中心差分 Yee 算法获得，因为该算法需要边界外半格处的场值。现代 ABC 的反射系数可达 $10^{-4}$ 到 $10^{-6}$，实现 70 dB 以上的动态范围。

Four major ABC theory thrusts:
> 四种主要的 ABC 理论方向：
- **Bayliss-Turkel** radiation operators (annihilation of radially propagating waves)
  > **Bayliss-Turkel** 辐射算符（消除径向传播波）
- **Engquist-Majda** one-way wave equations (pseudodifferential operator factorization)
  > **Engquist-Majda** 单向波动方程（伪微分算符分解）
- **Mur** finite-difference scheme (practical implementation of Engquist-Majda)
  > **Mur** 有限差分格式（Engquist-Majda 的实用实现）
- **Higdon** radiation operators (annihilation by incidence angle)
  > **Higdon** 辐射算符（按入射角消除）

> **Numerical Intuition:** Analytical ABCs are approximate — they reflect 1-5% of outgoing wave energy at normal incidence, rising to ~50% at grazing angles. For most engineering problems this is acceptable, but PML (Ch7) is preferred for high-dynamic-range simulations.
> **数值直觉：** 解析 ABC 是近似的——正入射时反射 1-5% 的出射波能量，掠射角时升至约 50%。大多数工程问题尚可接受，但高动态范围仿真优选 PML（第7章）。

---

## 6.2 Bayliss-Turkel Radiation Operators
> Bayliss-Turkel 辐射算符

Based on the asymptotic expansion of outgoing wave solutions in spherical or cylindrical coordinates.
> 基于球坐标或柱坐标下出射波解的渐近展开。

### Spherical Coordinates
> 球坐标

For a spherical wave $u(R, \theta, \phi, t)$ satisfying the scalar wave equation in 3D, the far-field expansion is:
> 对于满足三维标量波动方程的球面波 $u(R, \theta, \phi, t)$，远场展开为：
$$u(R, \theta, \phi, t) = \sum_{n=1}^{\infty} \frac{f_n(\theta, \phi, t - R/c)}{R^n} \tag{6.2}$$

The **Bayliss-Turkel operator of order 1**:
> **一阶 Bayliss-Turkel 算符**：
$$B_1 = \frac{\partial}{\partial R} + \frac{1}{R} + \frac{1}{c}\frac{\partial}{\partial t} \tag{6.3}$$
$$B_1 u = O(R^{-3}) \quad \text{(eliminates the } R^{-1} \text{ term)}$$
> 消除了 $R^{-1}$ 项

**Order 2 operator:**
> **二阶算符**：
$$B_2 = \left(\frac{\partial}{\partial R} + \frac{3}{R} + \frac{1}{c}\frac{\partial}{\partial t}\right) \left(\frac{\partial}{\partial R} + \frac{1}{R} + \frac{1}{c}\frac{\partial}{\partial t}\right) \tag{6.7}$$
$$B_2 u = O(R^{-5})$$

General $n$th-order operator:
> $n$ 阶通项算符：
$$B_n = \prod_{k=1}^n \left(\frac{\partial}{\partial R} + \frac{2k-1}{R} + \frac{1}{c}\frac{\partial}{\partial t}\right) \tag{6.10}$$

### Cylindrical Coordinates (2D)
> 柱坐标（二维）

Far-field expansion for cylindrical waves:
> 柱面波的远场展开：
$$u(r, \phi, t) = \sum_{n=0}^{\infty} \frac{g_n(\phi, t - r/c)}{r^{n+1/2}} \tag{6.12}$$

First-order cylindrical operator:
> 一阶柱坐标算符：
$$B_1^c = \frac{\partial}{\partial r} + \frac{1}{2r} + \frac{1}{c}\frac{\partial}{\partial t} \tag{6.15}$$

---

## 6.3 Engquist-Majda One-Way Wave Equations
> Engquist-Majda 单向波动方程

Based on factoring the 2D scalar wave operator:
> 基于二维标量波动算符的因式分解：
$$\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}\right) U = 0 \tag{6.20}$$

The operator can be factored as $G = G^- G^+$ where:
> 算符可分解为 $G = G^- G^+$，其中：
$$G^{\pm} = D_x \mp \frac{D_t}{c} \sqrt{1 - s^2}, \quad s = \frac{D_y}{(D_t/c)} \tag{6.23}$$

$G^-U = 0$ at $x=0$ (left boundary) and $G^+U = 0$ at $x=h$ (right boundary) are exact ABCs for waves impinging at any angle.
> $G^-U = 0$ 在左边界、$G^+U = 0$ 在右边界是任意角度入射波的精确 ABC。

### 6.3.1 Taylor Series Approximations
> 泰勒级数逼近

**First-order (one-term):**
> **一阶（单项）：**
$$\frac{\partial U}{\partial x} - \frac{1}{c}\frac{\partial U}{\partial t} = 0 \quad \text{at } x=0 \tag{6.26}$$
This is simply a plane-wave propagator normal to the boundary.
> 这实际上就是垂直于边界的平面波传播算子。

**Second-order (two-term):**
> **二阶（两项）：**
$$\frac{\partial^2 U}{\partial x \partial t} - \frac{1}{c}\frac{\partial^2 U}{\partial t^2} + \frac{c}{2}\frac{\partial^2 U}{\partial y^2} = 0 \quad \text{at } x=0 \tag{6.28a}$$

### 6.3.2 Mur Finite-Difference Scheme (Practical Implementation)
> Mur 有限差分格式（实用实现）

Mur discretized (6.28a) at the $x=0$ boundary using central differences expanded about an auxiliary point $(\tfrac12, j)$. For a square grid ($\Delta x = \Delta y = \Delta$):
> Mur 在 $x=0$ 边界处对 (6.28a) 进行离散化，围绕辅助点 $(\tfrac12, j)$ 展开中心差分。对于正方形网格：

**Second-order Mur ABC at $x=0$:**
> **$x=0$ 处的二阶 Mur ABC：**
$$W_{0,j}^{n+1} = -W_{1,j}^{n-1} + \frac{c\Delta t - \Delta}{c\Delta t + \Delta}(W_{1,j}^{n+1} + W_{0,j}^{n-1}) + \frac{2\Delta}{c\Delta t + \Delta}(W_{1,j}^n + W_{0,j}^n) + \frac{(c\Delta t)^2 \Delta}{2\Delta y^2(c\Delta t + \Delta)}(W_{0,j+1}^n - 2W_{0,j}^n + W_{0,j-1}^n + W_{1,j+1}^n - 2W_{1,j}^n + W_{1,j-1}^n) \tag{6.35}$$

**First-order Mur ABC at $x=0$:**
> **$x=0$ 处的一阶 Mur ABC：**
$$W_{0,j}^{n+1} = W_{1,j}^n + \frac{c\Delta t - \Delta}{c\Delta t + \Delta}(W_{1,j}^{n+1} - W_{0,j}^n) \tag{6.34}$$

### 6.3.3 Trefethen-Halpern Generalized ABCs
> Trefethen-Halpern 广义 ABC

Use rational function (Padé) approximations of $\sqrt{1-s^2}$ to improve wide-angle absorption:
> 使用 $\sqrt{1-s^2}$ 的有理函数（Padé）逼近来改善宽角吸收：
$$\sqrt{1 - s^2} \approx 1 - \frac{s^2}{2} \quad \text{(Padé (2,0), Mur)}$$
$$\sqrt{1 - s^2} \approx \frac{1 - \frac{3}{4}s^2}{1 - \frac{1}{4}s^2} \quad \text{(Padé (2,2))}$$

### 6.3.4 Theoretical Reflection Coefficient
> 理论反射系数

For a plane wave at incidence angle $\theta$ from normal:
> 对于入射角 $\theta$ 的平面波：
$$R(\theta) = \left|\frac{\cos\theta - \sqrt{1 - s^2}}{\cos\theta + \sqrt{1 - s^2}}\right|$$

For the 2nd-order Mur (Padé (2,0)):
> 对于二阶 Mur（Padé (2,0)）：
$$R_{\text{Mur}}(\theta) = \left|\frac{\cos\theta - (1 - \frac12 \sin^2\theta)}{\cos\theta + (1 - \frac12 \sin^2\theta)}\right|^2$$

---

## 6.4 Higdon Radiation Operators
> Higdon 辐射算符

Higdon's operator annihilates plane waves at specified incidence angles $\alpha_1, \alpha_2, \ldots, \alpha_L$:
> Higdon 算符在指定入射角 $\alpha_1, \alpha_2, \ldots, \alpha_L$ 处消除平面波：
$$\prod_{\ell=1}^L \left(\cos\alpha_\ell \frac{\partial}{\partial t} - c\frac{\partial}{\partial x}\right) U = 0 \quad \text{at } x=0 \tag{6.48}$$

**Properties:**
> **性质：**
1. Exactly absorbs any combination of $2L$ plane waves at angles $\pm\alpha_\ell$
   > 精确吸收角度为 $\pm\alpha_\ell$ 的任意 $2L$ 个平面波的组合
2. Theoretical reflection coefficient:
   > 理论反射系数：
$$R(\theta) = -\prod_{\ell=1}^L \frac{\cos\alpha_\ell - \cos\theta}{\cos\alpha_\ell + \cos\theta} \tag{6.49}$$
3. Angles $\alpha_\ell$ can be optimized for the problem
   > $\alpha_\ell$ 可根据问题优化选择
4. Requires only 1D stencil normal to boundary — simple at corners
   > 仅需垂直于边界的一维模板——角点处简单
5. First-order Higdon $\equiv$ first-order Mur when $\alpha_1 = 0$
   > 当 $\alpha_1 = 0$ 时，一阶 Higdon $\equiv$ 一阶 Mur

---

## 6.5 Liao Extrapolation ABC
> Liao 外推 ABC

Liao's ABC uses a space-time extrapolation via Newton backward-difference polynomials:
> Liao ABC 通过 Newton 后向差分多项式进行时空外推：
$$W_{0}^{n+1} = \sum_{k=1}^{N} (-1)^{k+1} C_k^N W_k^{n+1-k\beta}$$
where $\beta = \frac{c\Delta t}{\Delta x}$ and $C_k^N$ are binomial coefficients.
> 其中 $\beta = \frac{c\Delta t}{\Delta x}$，$C_k^N$ 为二项式系数。

---

## Example 6.1: 1D FDTD — Mur First-Order ABC Performance
> 示例 6.1：一维 FDTD——Mur 一阶 ABC 性能

**Setup:** 200-cell grid, Gaussian pulse at center, 400 time steps.
> **设置：** 200 网格单元，中心高斯脉冲，400 时间步。
**Result:** Mur ABC absorbs >95% of incident energy at normal incidence.
> **结果：** Mur ABC 在正入射时吸收 >95% 的入射能量。

---

## Example 6.2: 2D TM$_z$ — Mur Second-Order ABC
> 示例 6.2：二维 TM$_z$——Mur 二阶 ABC

**Setup:** 100×100 grid, point source at center, 300 time steps.
> **设置：** 100×100 网格，中心点源，300 时间步。
- First-order Mur: $R \approx 1\%$ at normal, $>10\%$ at 60°
  > 一阶 Mur：正入射约 1%，60° 时 >10%
- Second-order Mur: $R < 1\%$ up to 50°, $<5\%$ at 70°
  > 二阶 Mur：50° 以内 <1%，70° 时 <5%

---

## Example 6.3: Higdon ABC with Optimized Angles
> 示例 6.3：带优化角度的 Higdon ABC

Apply 3rd-order Higdon ABC with $\alpha = [0^\circ, 30^\circ, 60^\circ]$.
> 应用三阶 Higdon ABC，$\alpha = [0^\circ, 30^\circ, 60^\circ]$。
**Result:** Higdon outperforms Mur at wide angles.
> **结果：** Higdon 在大角度时性能优于 Mur。

---

## Audit Table
> 审计表

| Concept | Section | Key Equation | Implementation |
|---------|---------|-------------|----------------|
| 概念 | 章节 | 关键方程 | 实现 |
| Bayliss-Turkel spherical | 6.2 | (6.3), (6.7), (6.10) | — |
| 球坐标 B-T | 6.2 | | — |
| Bayliss-Turkel cylindrical | 6.2 | (6.15) | — |
| 柱坐标 B-T | 6.2 | | — |
| Engquist-Majda factorization | 6.3 | (6.23) | — |
| E-M 分解 | 6.3 | | — |
| Mur (1st) | 6.3.2 | (6.34) | Example 6.1 |
| Mur (二阶) | 6.3.2 | (6.35) | Example 6.2 |
| Higdon operator | 6.4 | (6.48), (6.49) | Example 6.3 |
| Higdon 算符 | 6.4 | | 示例 6.3 |
| Liao extrapolation | 6.5 | — | — |
| Liao 外推 | 6.5 | | — |

> **Numerical Intuition:** For most practical FDTD simulations, the second-order Mur ABC offers the best balance of simplicity and accuracy. It achieves $R < 1\%$ for angles up to 50° from normal. For wide-angle problems (e.g., sources near boundaries), Higdon's operator with optimized angles is preferred. However, PML (Ch7) has largely superseded analytical ABCs for high-accuracy work.
> **数值直觉：** 对大多数实用 FDTD 仿真，二阶 Mur ABC 在简单性和精度间达到最佳平衡。对于偏离法线 50° 以内的角度，反射系数 <1%。对于宽角问题（如靠近边界的源），建议使用带优化角度的 Higdon 算符。然而，PML（第7章）在高精度工作中已基本取代了解析 ABC。
