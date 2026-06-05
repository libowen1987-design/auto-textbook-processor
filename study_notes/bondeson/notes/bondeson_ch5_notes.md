# Bondeson《Computational Electromagnetics》第5章
> **中英双语版**

> **Source:** Anders Bondeson, Thomas Rylander, Pär Ingelström, *Computational Electromagnetics*, Springer 2005  
> **PDF:** pages 72-101 of 231 (231 total)

---

## The Finite-Difference Time-Domain Method | 时域有限差分法

The finite-difference time-domain method (FDTD) is one of the most popular computational methods for microwave problems.
> 时域有限差分法（FDTD）是微波问题中最流行的计算方法之一。

The FDTD algorithm was originally proposed by K.S. Yee in 1966 [87].
> FDTD 算法最初由 K.S. Yee 于 1966 年提出。

Selected time signals from an FDTD simulation can be Fourier transformed while the simulation proceeds, and a single FDTD run can produce frequency-domain results at any desired number of frequencies.
> FDTD 模拟中的选定时域信号可以在模拟进行中被傅里叶变换，单次 FDTD 运行可以产生任意频率数的频域结果。

This is a major advantage of time-domain methods.
> 这是时域方法的一个主要优势。

---

#### 5.1 The 1D Wave Equation | 一维波动方程

To solve the wave equation numerically, we divide the $z$-axis into intervals of length $\Delta z$ and the time axis into intervals of length $\Delta t$.
> 为数值求解波动方程，我们将 $z$ 轴分割成长度为 $\Delta z$ 的区间，将时间轴分割成长度为 $\Delta t$ 的区间。

The discrete equation is obtained using standard difference approximations for the derivatives:

$$\frac{E_r^{n+1} - 2E_r^n + E_r^{n-1}}{(\Delta t)^2} = c^2 \frac{E_{r+1}^n - 2E_r^n + E_{r-1}^n}{(\Delta z)^2} \tag{5.1}$$

> 使用导数的标准差分近似得到离散方程 (5.1)。

This gives an explicit expression for $E$ at the next time level $n+1$:

$$E_r^{n+1} = 2E_r^n - E_r^{n-1} + \left(\frac{c\Delta t}{\Delta z}\right)^2 (E_{r+1}^n - 2E_r^n + E_{r-1}^n), \tag{5.2}$$

> 这给出了 $E$ 在下一时间层 $n+1$ 的显式表达式 (5.2)。

which is identical to (4.19) when $c = 1$.
> 当 $c = 1$ 时，这与 (4.19) 相同。

##### 5.1.1 Dispersion and Stability | 色散与稳定性

The dispersion relation for the numerical scheme is:

$$\frac{\sin(\omega \Delta t/2)}{c\Delta t/\Delta z} = \pm \sin\left(\frac{k\Delta z}{2}\right) \tag{5.3}$$

> 数值方案的色散关系为 (5.3)。

The important parameter is $R = c\Delta t / \Delta z$, i.e., how many grid cells the exact solution propagates in one time-step.
> 重要参数为 $R = c\Delta t / \Delta z$，即精确解在一个时间步中传播的网格单元数。

**Three regimes | 三种情况：**

- **$R = 1$ (magic time step):** If $\Delta t = \Delta z/c$, then $R = 1$ and (5.3) simplifies to $\omega = \pm ck$, which is exactly the analytical dispersion relation. The errors of the spatial and temporal difference approximations cancel.
> **$R = 1$（魔法时间步长）：** 如果 $\Delta t = \Delta z/c$，则 $R = 1$，(5.3) 简化为 $\omega = \pm ck$，即精确的解析色散关系。空间和时间差分近似的误差相互抵消。

- **$R < 1$:** The numerical dispersion relation differs from the analytical. The smaller $R$, the stronger the numerical dispersion.
> **$R < 1$：** 数值色散关系与解析解不同。$R$ 越小，数值色散越强。

- **$R > 1$:** The scheme is unstable. The stability condition $c\Delta t \leq \Delta z$ is called the Courant (or Courant-Friedrichs-Levy, CFL) condition.
> **$R > 1$：** 方案不稳定。稳定性条件 $c\Delta t \leq \Delta z$ 称为 Courant（或 Courant-Friedrichs-Levy，CFL）条件。

---

#### 5.2 The FDTD Method: Staggered Grids | FDTD 方法：交错网格

The wave equation can also be stated as a system of coupled first-order differential equations for both $\mathbf{E}$ and $\mathbf{H}$.
> 波动方程也可以表示为 $\mathbf{E}$ 和 $\mathbf{H}$ 的耦合一阶微分方程组。

In three dimensions, Maxwell's equations in a source-free region give:
> 在三维无源区域中，Maxwell 方程组给出六个标量方程：

$$\epsilon \frac{\partial E_x}{\partial t} = \frac{\partial H_z}{\partial y} - \frac{\partial H_y}{\partial z}, \quad \epsilon \frac{\partial E_y}{\partial t} = \frac{\partial H_x}{\partial z} - \frac{\partial H_z}{\partial x}, \quad \epsilon \frac{\partial E_z}{\partial t} = \frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y}, \tag{5.4-5.6}$$

$$\mu \frac{\partial H_x}{\partial t} = \frac{\partial E_y}{\partial z} - \frac{\partial E_z}{\partial y}, \quad \mu \frac{\partial H_y}{\partial t} = \frac{\partial E_z}{\partial x} - \frac{\partial E_x}{\partial z}, \quad \mu \frac{\partial H_z}{\partial t} = \frac{\partial E_x}{\partial y} - \frac{\partial E_y}{\partial x}. \tag{5.7-5.9}$$

**Key idea | 核心思想：** Put different $E$- and $H$-components at different positions on the grid (staggered grids), and evaluate the equations at different positions.
> 将不同的 $E$ 和 $H$ 分量放在网格的不同位置（交错网格），并在不同位置评估方程。

First-order derivatives are much more accurately evaluated on staggered grids.
> 一阶导数在交错网格上评估要精确得多。

##### 5.2.1 One Space Dimension | 一维空间

For a plane wave propagating in the $z$-direction with $E_x$ and $H_y$:

$$\epsilon \frac{\partial E_x}{\partial t} = -\frac{\partial H_y}{\partial z}, \quad \mu \frac{\partial H_y}{\partial t} = -\frac{\partial E_x}{\partial z}. \tag{5.10-5.11}$$

> 对于沿 $z$ 方向传播且具有 $E_x$ 和 $H_y$ 的平面波：

The finite difference approximation on staggered grids reads:

$$\frac{E_x|^{n+1}_r - E_x|^n_r}{\Delta t} = -\frac{1}{\epsilon} \frac{H_y|^{n+1/2}_{r+1/2} - H_y|^{n+1/2}_{r-1/2}}{\Delta z}, \tag{5.12}$$

$$\frac{H_y|^{n+1/2}_{r+1/2} - H_y|^{n-1/2}_{r+1/2}}{\Delta t} = -\frac{1}{\mu} \frac{E_x|^n_{r+1} - E_x|^n_r}{\Delta z}. \tag{5.13}$$

> 交错网格上的有限差分近似如 (5.12)-(5.13) 所示。

$E_x$ is located on integer grid points (both in space and time), while $H_y$ is on the half-grids.
> $E_x$ 位于整数网格点（空间和时间都是），而 $H_y$ 位于半网格。

##### 5.2.2 The Yee Algorithm in 3D | 三维 Yee 算法

In 3D, the electric field components are placed on the edges of the Cartesian grid cells, and the magnetic field components are placed on the faces of the cells. This is the Yee cell.
> 在三维中，电场分量放置在笛卡尔网格单元的边上，磁场分量放置在单元面上。这就是 Yee 元胞。

**Yee cell / 三维 Yee 元胞：**
- $E_x$, $E_y$, $E_z$ are located on the cell edges (midpoints of edges parallel to each axis)
- $H_x$, $H_y$, $H_z$ are located on the cell faces (centers of faces normal to each axis)

This arrangement naturally satisfies:
> 这种安排自然满足：
- Faraday's law: $\nabla \times \mathbf{E} = -\mu \partial \mathbf{H}/\partial t$ is applied to each face
- Ampère's law: $\nabla \times \mathbf{H} = \epsilon \partial \mathbf{E}/\partial t$ is applied around each edge

**FDTD update procedure / FDTD 更新过程：**

1. Update $\mathbf{H}$ at time $n+1/2$ using $\nabla \times \mathbf{E}$ at time $n$ (Faraday)
2. Update $\mathbf{E}$ at time $n+1$ using $\nabla \times \mathbf{H}$ at time $n+1/2$ (Ampère)
3. Repeat

**Stability condition in 3D / 三维稳定性条件：**

$$\Delta t \leq \frac{1}{c\sqrt{\frac{1}{\Delta x^2} + \frac{1}{\Delta y^2} + \frac{1}{\Delta z^2}}}$$

For a cubic cell ($\Delta x = \Delta y = \Delta z = h$):
> 对于立方体单元：

$$\Delta t \leq \frac{h}{c\sqrt{3}}$$

##### 5.2.3 Dispersion in 3D | 三维色散

The numerical dispersion relation for the 3D Yee scheme is:

$$\left[\frac{1}{c\Delta t} \sin\left(\frac{\omega \Delta t}{2}\right)\right]^2 = \sum_{\alpha=x,y,z} \left[\frac{1}{\Delta \alpha} \sin\left(\frac{k_\alpha \Delta \alpha}{2}\right)\right]^2$$

> 三维 Yee 格式的数值色散关系如上所示。

This shows that the numerical phase velocity depends on the direction of propagation (numerical anisotropy), in addition to the frequency dependence.
> 这表明数值相速度除了依赖于频率外，还依赖于传播方向（数值各向异性）。

##### 5.2.4 Integral Representation of the Yee Algorithm | Yee 算法的积分表示

The Yee algorithm can be derived directly from the integral form of Maxwell's equations:

$$\oint_{\partial S} \mathbf{E} \cdot d\mathbf{l} = -\frac{\partial}{\partial t} \int_S \mu \mathbf{H} \cdot d\mathbf{S} \quad \text{(Faraday)}$$

$$\oint_{\partial S} \mathbf{H} \cdot d\mathbf{l} = \frac{\partial}{\partial t} \int_S \epsilon \mathbf{E} \cdot d\mathbf{S} \quad \text{(Ampère)}$$

> Yee 算法可以直接从 Maxwell 方程组的积分形式推导。

Applied to the Yee cell, the line integrals approximate the curl, and the surface integrals approximate the flux.
> 应用于 Yee 元胞时，线积分近似旋度，面积分近似通量。

---

#### 5.3 Boundaries and Initial Conditions | 边界与初始条件

##### 5.3.1 Absorbing Boundary Conditions | 吸收边界条件

For open-region problems, the computational domain must be truncated by absorbing boundary conditions (ABCs).
> 对于开放区域问题，计算域必须通过吸收边界条件（ABC）截断。

The perfectly matched layer (PML), introduced by Berenger [8], is the most popular ABC.
> 由 Berenger 引入的完全匹配层（PML）是最流行的 ABC。

PML works by adding a lossy layer surrounding the computational domain that absorbs outgoing waves with minimal reflection.
> PML 通过在计算域周围添加有损耗层来工作，该层以最小反射吸收出射波。

##### 5.3.2 Total-Field / Scattered-Field Formulation | 总场/散射场公式

For scattering problems, the computational domain is divided into a total-field region (incident + scattered fields) and a scattered-field region.
> 对于散射问题，计算域分为总场区域（入射场 + 散射场）和散射场区域。

The incident field is introduced through a Huygens surface connecting the two regions.
> 入射场通过连接两个区域的惠更斯表面引入。

##### 5.3.3 Initial Conditions | 初始条件

For time-domain simulations, initial conditions for both $\mathbf{E}$ and $\mathbf{H}$ must be specified.
> 对于时域模拟，必须指定 $\mathbf{E}$ 和 $\mathbf{H}$ 的初始条件。

The fields must satisfy the divergence conditions $\nabla \cdot \mathbf{D} = \rho$ and $\nabla \cdot \mathbf{B} = 0$ at $t = 0$.
> 场必须满足 $t=0$ 时的散度条件 $\nabla \cdot \mathbf{D} = \rho$ 和 $\nabla \cdot \mathbf{B} = 0$。

---

#### 5.4 Source Excitation | 源激励

Common source types include:
> 常见的源类型包括：

- **Hard source:** $E_z$ is set to a prescribed time function at a specific grid point ($E_z = f(t)$). Simple but causes reflections.
> **硬源：** 在特定网格点将 $E_z$ 设为预设的时间函数。简单但会引起反射。

- **Soft source:** The source current $J_z$ is added to Ampère's law. Prevents reflections.
> **软源：** 将源电流 $J_z$ 添加到安培定律。防止反射。

- **Total-field/scattered-field:** A Huygens surface injects the incident plane wave.
> **总场/散射场：** 惠更斯表面注入入射平面波。

---

#### 5.5 FDTD Summary | FDTD 总结

**Advantages / 优势：**
- Simple to program / 编程简单
- Highly efficient / 效率高
- Explicit time-stepping (no matrix inversion) / 显式时间步进（无需求逆矩阵）
- Low memory requirements / 内存需求低
- Single simulation gives full frequency spectrum / 单次模拟给出完整频谱

**Disadvantages / 缺点：**
- Structured Cartesian grids only / 仅限于结构化笛卡尔网格
- Staircase approximation for oblique boundaries / 倾斜边界的阶梯近似
- Stability limit ($\Delta t \leq h/(c\sqrt{3})$ in 3D) / 稳定性限制
- Difficult to model fine structures / 难以建模精细结构

**Review Questions / 复习问题：**

5.1-1 List some pros and cons of the FDTD scheme.
> 列出 FDTD 方案的一些优缺点。

5.1-2 What is a dispersion relation? Derive the dispersion relation for the 1D wave equation discretized by the standard finite difference approximation.
> 什么是色散关系？推导标准有限差分近似离散化的一维波动方程的色散关系。

5.1-3 Under what conditions will $E(z,t) = E_+(z-ct) + E_-(z+ct)$ satisfy the discretized 1D wave equation?
> 在什么条件下 $E(z,t) = E_+(z-ct) + E_-(z+ct)$ 满足离散化的一维波动方程？

5.1-4 Generally, higher resolutions lead to more accurate results, but in some cases this is not true. Give an example and explain why.
> 通常情况下，更高分辨率导致更精确的结果，但在某些情况下并非如此。举一个例子并解释原因。

5.2-1 Derive the 3D FDTD update equations from the integral form of Maxwell's equations.
> 从 Maxwell 方程组的积分形式推导三维 FDTD 更新方程。

5.2-2 Describe the arrangement of field components in the Yee cell.
> 描述 Yee 元胞中场分量的排列方式。

5.3-1 What is the rationale behind the PML?
> PML 的基本原理是什么？

5.3-2 Why are the divergence conditions for the fields important for FDTD simulations?
> 为什么场的散度条件对 FDTD 模拟很重要？

5.4-1 What is the difference between a hard source and a soft source?
> 硬源和软源之间的区别是什么？
