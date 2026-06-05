# Chapter 8: The Finite Difference Method (FDM/FDTD) | 第八章：有限差分法 (FDM/FDTD)

> **中英双语版**

**Source:** Jin, *Theory and Computation of Electromagnetic Fields*, 2nd Ed., Chapter 8 (pp. 409–456)

---

## 8.1 Basic Finite Differencing | 基本有限差分

### 8.1.1 Finite Difference Approximations | 有限差分近似

Central difference for first derivative / 一阶导数的中心差分：
$$
\frac{df}{dx}\bigg|_i \approx \frac{f_{i+1} - f_{i-1}}{2\Delta x} + O(\Delta x^2)
\tag{8.1.5}
$$

Second derivative / 二阶导数：
$$
\frac{d^2f}{dx^2}\bigg|_i \approx \frac{f_{i+1} - 2f_i + f_{i-1}}{\Delta x^2} + O(\Delta x^2)
\tag{8.1.7}
$$

### 8.1.2 FD for 1D Wave Equation | 一维波动方程的有限差分

$$
\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}
$$

Discretized / 离散化：
$$
\frac{u_i^{n+1} - 2u_i^n + u_i^{n-1}}{\Delta t^2} = c^2 \frac{u_{i+1}^n - 2u_i^n + u_{i-1}^n}{\Delta x^2}
\tag{8.1.12}
$$

Explicit update / 显式更新：
$$
u_i^{n+1} = 2(1 - r^2)u_i^n + r^2(u_{i+1}^n + u_{i-1}^n) - u_i^{n-1}
\tag{8.1.13}
$$

where $r = c\Delta t / \Delta x$ is the Courant number / $r = c\Delta t / \Delta x$ 是库朗数。

**CFL stability condition / CFL稳定条件:** $r \leq 1$

### 8.1.3 FD for 1D Diffusion Equation | 一维扩散方程的有限差分

$$
\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}
$$

Explicit (forward-time, central-space) / 显式（时间前向、空间中心）：
$$
u_i^{n+1} = u_i^n + \frac{\alpha \Delta t}{\Delta x^2}(u_{i+1}^n - 2u_i^n + u_{i-1}^n)
\tag{8.1.17}
$$

Stability / 稳定性：$\frac{\alpha \Delta t}{\Delta x^2} \leq \frac{1}{2}$

---

## 8.2 Finite Difference Time-Domain (FDTD) Method | 时域有限差分法

### 8.2.1 Yee's Algorithm (1966) | 耶氏算法 (1966)

Maxwell's curl equations in 3D / 三维麦克斯韦旋度方程：

$$
\frac{\partial H_x}{\partial t} = \frac{1}{\mu}\left(\frac{\partial E_y}{\partial z} - \frac{\partial E_z}{\partial y}\right)
$$
$$
\frac{\partial E_x}{\partial t} = \frac{1}{\epsilon}\left(\frac{\partial H_z}{\partial y} - \frac{\partial H_y}{\partial z} - \sigma E_x\right)
$$

Yee's leapfrog scheme positions E and H staggered in both space and time / 耶氏蛙跳格式在空间和时间上交错放置E和H：

- **Electric field / 电场** E 在整数时间步 ($n$)，位于棱边中心
- **Magnetic field / 磁场** H 在半整数时间步 ($n+1/2$)，位于面心

### 8.2.2 1D FDTD Update Equations | 一维FDTD更新方程

For a 1D TM wave ($E_z, H_y$ propagation along $x$) / 对于一维TM波（$E_z, H_y$ 沿 $x$ 传播）：

$$
E_z^{n+1}(k) = E_z^n(k) + \frac{\Delta t}{\epsilon \Delta x}\left[H_y^{n+1/2}(k+1/2) - H_y^{n+1/2}(k-1/2)\right]
\tag{8.2.6}
$$

$$
H_y^{n+1/2}(k+1/2) = H_y^{n-1/2}(k+1/2) + \frac{\Delta t}{\mu \Delta x}\left[E_z^n(k+1) - E_z^n(k)\right]
\tag{8.2.7}
$$

### 8.2.3 2D FDTD: TM$_z$ Mode | 二维FDTD：TM$_z$ 模

$$
E_z^{n+1}(i,j) = E_z^n(i,j) + \frac{\Delta t}{\epsilon \Delta}\left[H_y^{n+1/2}(i+1/2,j) - H_y^{n+1/2}(i-1/2,j)\right.$$
$$\left. - H_x^{n+1/2}(i,j+1/2) + H_x^{n+1/2}(i,j-1/2)\right]
\tag{8.2.11}
$$

### 8.2.4 3D FDTD | 三维FDTD

$$
E_x^{n+1}(i,j,k) = E_x^n(i,j,k) + \frac{\Delta t}{\epsilon \Delta}\left[H_z^{n+1/2}(i,j+1/2,k) - H_z^{n+1/2}(i,j-1/2,k)\right.$$
$$\left. - H_y^{n+1/2}(i,j,k+1/2) + H_y^{n+1/2}(i,j,k-1/2)\right]
\tag{8.2.12}
$$

---

## 8.3 Numerical Dispersion and Stability | 数值色散与稳定性

### 8.3.1 CFL Condition | CFL条件

For 3D FDTD with uniform cell size $\Delta$ / 均匀网格 $\Delta$ 的三维FDTD：

$$
\Delta t \leq \frac{\Delta}{c\sqrt{3}}
\tag{8.3.1}
$$

For 1D / 一维：
$$
\Delta t \leq \frac{\Delta x}{c}
\tag{8.3.2}
$$

### 8.3.2 Numerical Dispersion Relation | 数值色散关系

For 1D FDTD / 一维FDTD：
$$
\sin^2\left(\frac{\omega \Delta t}{2}\right) = r^2 \sin^2\left(\frac{k \Delta x}{2}\right)
\tag{8.3.3}
$$

Phase velocity error / 相速度误差：
$$
\frac{v_p}{c} = \frac{\omega/k}{c} = \frac{\pi}{N_\lambda r} \cdot \frac{1}{\arcsin\left[r\sin(\pi/N_\lambda)\right]}
$$

For $N_\lambda \geq 10$ (cells per wavelength / 每波长网格数)，error < 1% with $r = 0.5$ / 当 $r = 0.5$ 时误差 < 1%。

---

## 8.4 Absorbing Boundary Conditions (ABCs) | 吸收边界条件

### 8.4.1 Mur's First-Order ABC | Mur一阶ABC

For a wave propagating along $+x$ / 沿 $+x$ 传播的波：

$$
\left(\frac{\partial}{\partial x} + \frac{1}{c}\frac{\partial}{\partial t}\right)E_z^{\text{out}} = 0
\tag{8.4.1}
$$

Discretized at the right boundary $x = N_x \Delta x$ / 在右边界离散化：

$$
E_z^{n+1}(N_x) = E_z^n(N_x-1) + \frac{c\Delta t - \Delta x}{c\Delta t + \Delta x}\left[E_z^{n+1}(N_x-1) - E_z^n(N_x)\right]
\tag{8.4.5}
$$

### 8.4.2 PML (Perfectly Matched Layer) | 完美匹配层

Berenger's PML introduces a lossy anisotropic layer surrounding the computational domain where the wave is absorbed without reflection / 贝伦杰PML在计算域周围引入有耗各向异性层，波在其中无反射地被吸收。

---

## 8.5 Source Excitation | 源激励

### 8.5.1 Hard Source | 硬源

$$
E_z^n(k_s) = f(n\Delta t)
$$

Simple but causes reflections from the source point / 简单但会产生从源点的反射。

### 8.5.2 Soft Source (Total-Field/Scattered-Field) | 软源（总场/散射场）

$$
E_z^{n+1}(k_s) = E_z^{n+1}(k_s)\big|_{\text{FDTD}} + E_z^{\text{inc}}(k_s)
$$

Allows incident wave injection without spurious reflections / 允许入射波注入而无虚假反射。

---

## 8.6 Example: 1D FDTD Simulation | 示例：一维FDTD仿真

**Problem / 问题:** 用一维FDTD模拟高斯脉冲在自由空间中传播。

**Parameters / 参数:**
- 计算域：200个网格，$\Delta x = 1$ mm
- 时间步：$\Delta t = \Delta x / (2c)$ (CFL = 0.5)
- 高斯源：$E_z(t) = \exp\left[-(t - t_0)^2 / T^2\right]$
- 边界处的Mur ABC

**Update loop (per time step) / 更新循环（每时间步）:**
1. 使用 $t=n$ 时的 $E_z$ 更新 $t=n+1/2$ 时的 $H_y$
2. 使用 $t=n+1/2$ 时的 $H_y$ 更新 $t=n+1$ 时的 $E_z$
3. 在边界应用ABC
4. 注入源
5. 记录观测点的场
