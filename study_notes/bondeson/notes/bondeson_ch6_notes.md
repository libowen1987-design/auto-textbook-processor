# Bondeson《Computational Electromagnetics》第6章
> **中英双语版**

> **Source:** Anders Bondeson, Thomas Rylander, Pär Ingelström, *Computational Electromagnetics*, Springer 2005  
> **PDF:** pages 102-166 of 231 (231 total)

---

## The Finite Element Method | 有限元法

### 6 The Finite Element Method

The finite element method (FEM) is a powerful technique for solving partial differential equations on complex geometries by dividing the domain into small elements.
> 有限元法（FEM）是一种通过将域划分为小单元来求解复杂几何上偏微分方程的强大技术。

Common element shapes include lines (1D), triangles and squares (2D), and tetrahedra, prisms, pyramids, and cubes (3D).
> 常见的单元形状包括线段（一维）、三角形和正方形（二维）以及四面体、棱柱、棱锥和立方体（三维）。

---

#### 6.1 General Recipe | 一般步骤

1. **Subdivide the domain** $\Omega$ into cells/elements (e.g., triangles in 2D).
   > **细分域：** 将域 $\Omega$ 细分为单元（例如二维的三角形）。

2. **Approximate the solution** by an expansion in basis functions: $f(\mathbf{r}) \approx \sum_{i=1}^n f_i \phi_i(\mathbf{r})$, where $f_i$ are unknown coefficients and $\phi_i$ are basis functions (typically low-order polynomials, nonzero only in a few adjacent elements).
   > **近似解：** 用基函数展开近似解 $f(\mathbf{r}) \approx \sum_{i=1}^n f_i \phi_i(\mathbf{r})$。

3. **Form the residual** $r = L[f] - s$. It will not be zero pointwise, so we require it to be zero in the weak (weighted) sense.
   > **形成残差：** $r = L[f] - s$。它不会逐点为零，因此我们要求它在弱（加权）意义上为零。

4. **Choose test (weighting) functions** $w_i$, $i = 1, 2, \ldots, n$. If $w_i = \phi_i$, this is Galerkin's method.
   > **选择测试（权）函数：** $w_i$。若 $w_i = \phi_i$，则为 Galerkin 方法。

5. **Set the weighted residuals to zero**: $\langle w_i, r \rangle = \int_\Omega w_i r \, d\Omega = 0$, for $i = 1, 2, \ldots, n$. Solve for $f_i$.
   > **令加权残差为零**，求解 $f_i$。

In electrical engineering, the term "finite element" typically refers to an element together with its basis functions and degrees of freedom.
> 在电气工程中，"有限元"通常指单元及其基函数和自由度。

**Review Questions | 复习问题：**

6.1-1 List some pros and cons of the finite element method.
> 列出有限元法的一些优缺点。

6.1-2 Compare the FEM recipe to the typical finite difference discretization procedure.
> 比较 FEM 一般步骤与典型的有限差分离散化过程。

6.1-3 What is a finite element?
> 什么是有限元？

---

#### 6.2 1D Finite Element Analysis | 一维有限元分析

As the first model problem, we choose the 1D Helmholtz equation:
> 作为第一个模型问题，我们选择一维亥姆霍兹方程：

$$-\frac{d}{dx}\left(\alpha \frac{df}{dx}\right) + \beta f = s, \quad a < x < b, \tag{6.1}$$

with $f(a) = f_a$ and $f(b) = f_b$.
> 边界条件为 $f(a) = f_a$ 和 $f(b) = f_b$。

Here $\alpha = \alpha(x)$, $\beta = \beta(x)$ and $s = s(x)$ are prescribed functions of $x$.
> 其中 $\alpha(x)$, $\beta(x)$ 和 $s(x)$ 是 $x$ 的给定函数。

The basis functions $\phi_i(x)$ are chosen as linear "hat" functions: $\phi_i(x)$ is 1 at node $x_i$ and 0 at all other nodes, linear on each element.
> 基函数 $\phi_i(x)$ 选择为线性"帽"函数：$\phi_i(x)$ 在节点 $x_i$ 处为 1，在其他节点为 0，在每个单元上为线性。

The weak form is obtained by multiplying (6.1) by a test function $w$ and integrating by parts:
> 弱形式通过将 (6.1) 乘以测试函数 $w$ 并分部积分得到：

$$\int_a^b \alpha \frac{df}{dx} \frac{dw}{dx} \, dx + \int_a^b \beta f w \, dx = \int_a^b s w \, dx + \left[\alpha w \frac{df}{dx}\right]_a^b. \tag{6.8}$$

> 边界项 $[\alpha w \, df/dx]_a^b$ 处理自然边界条件（Neumann 边界条件）。

Applying Galerkin's method ($w = \phi_i$, $f = \sum f_j \phi_j$) gives:
> 应用 Galerkin 方法得到：

$$\sum_{j=1}^n K_{ij} f_j = b_i, \quad i = 1, 2, \ldots, n, \tag{6.9}$$

where the stiffness matrix $K_{ij}$ and load vector $b_i$ are:
> 其中刚度矩阵 $K_{ij}$ 和载荷向量 $b_i$ 为：

$$K_{ij} = \int_a^b \left( \alpha \frac{d\phi_i}{dx} \frac{d\phi_j}{dx} + \beta \phi_i \phi_j \right) dx, \quad b_i = \int_a^b s \phi_i \, dx. \tag{6.10}$$

> 注意矩阵 $K$ 是稀疏的（仅相邻节点有耦合）且对称的。

---

#### 6.3 2D Finite Element Analysis | 二维有限元分析

##### 6.3.1 Triangular Elements | 三角形单元

In 2D, the domain is divided into triangles. On each triangle, we define linear basis functions:
> 在二维中，域被划分为三角形。在每个三角形上，定义线性基函数：

$$\phi_i(\mathbf{r}) = a_i + b_i x + c_i y, \quad i = 1, 2, 3 \text{ (for each triangle)}. \tag{6.17}$$

These are "hat" functions in 2D: $\phi_i$ is 1 at node $i$ and 0 at the other two nodes of the triangle.
> 这些是二维的"帽"函数：$\phi_i$ 在节点 $i$ 处为 1，在三角形的另外两个节点处为 0。

**Area coordinates / 面积坐标:**

For a triangle with nodes $(x_1, y_1)$, $(x_2, y_2)$, $(x_3, y_3)$, the area coordinates $L_1, L_2, L_3$ satisfy:
> 对于节点为 $(x_1, y_1)$, $(x_2, y_2)$, $(x_3, y_3)$ 的三角形，面积坐标 $L_1, L_2, L_3$ 满足：

$$L_i(\mathbf{r}) = \frac{\text{area of subtriangle opposite node } i}{\text{total triangle area}}. \tag{6.20}$$

> 面积坐标是方便的计算工具。

##### 6.3.2 Element Matrices | 单元矩阵

For the scalar Helmholtz equation $-\nabla \cdot (\alpha \nabla f) + \beta f = s$ in 2D, the element matrix for a triangle with linear basis functions is:
> 对于二维标量亥姆霍兹方程，线性基函数的三角形单元矩阵为：

$$K_{ij}^{(e)} = \int_{\Delta_e} (\alpha \nabla \phi_i \cdot \nabla \phi_j + \beta \phi_i \phi_j) \, dS. \tag{6.26}$$

The global matrix is assembled by summing contributions from all elements:
> 全局矩阵通过累加所有单元的贡献来组装：

$$K = \sum_{e} K^{(e)}, \quad \mathbf{b} = \sum_e \mathbf{b}^{(e)}. \tag{6.27}$$

> 这就是**矩阵组装（assembly）** 过程。

---

#### 6.4 3D Finite Element Analysis | 三维有限元分析

##### 6.4.1 Tetrahedral Elements | 四面体单元

In 3D, the simplest element is the tetrahedron with 4 nodes.
> 在三维中，最简单的单元是 4 节点的四面体。

Linear basis functions on a tetrahedron are:
> 四面体上的线性基函数为：

$$\phi_i(\mathbf{r}) = a_i + b_i x + c_i y + d_i z, \quad i = 1, 2, 3, 4. \tag{6.32}$$

**Volume coordinates / 体积坐标** allow integration over the tetrahedron.
> **体积坐标**允许在四面体上进行积分。

##### 6.4.2 Vector (Edge) Elements | 矢量（棱边）元

For Maxwell's equations, standard nodal elements are problematic because they do not enforce the divergence condition and allow spurious modes.
> 对于 Maxwell 方程组，标准节点元存在问题，因为它们不强制执行散度条件并允许虚假模式。

**Vector (edge/Whitney) elements** provide the correct finite element discretization for the curl-curl equation.
> **矢量（棱边/Whitney）元**为旋度-旋度方程提供了正确的有限元离散化。

The basis function for edge $ij$ connecting nodes $i$ and $j$ is:
> 连接节点 $i$ 和 $j$ 的棱边 $ij$ 的基函数为：

$$\mathbf{N}_{ij} = \phi_i \nabla \phi_j - \phi_j \nabla \phi_i = \frac{1}{2} \nabla (\phi_i \phi_j) + \text{curl part}. \tag{6.41}$$

Key properties of edge elements:
> 棱边元的关键性质：

- $\nabla \cdot \mathbf{N}_{ij} = 0$ inside the element (divergence-free)
- The tangential component is continuous across element boundaries
- $\nabla \times \mathbf{N}_{ij}$ is nonzero (captures the curl)

---

#### 6.5 FEM for Time-Harmonic Maxwell's Equations | 时谐 Maxwell 方程组的 FEM

##### 6.5.1 The Curl-Curl Equation | 旋度-旋度方程

Starting from the time-harmonic Maxwell equations:
> 从时谐 Maxwell 方程组出发：

$$\nabla \times \left(\frac{1}{\mu} \nabla \times \mathbf{E}\right) - k_0^2 \epsilon_r \mathbf{E} = -j\omega \mathbf{J}, \tag{6.61}$$

where $k_0 = \omega \sqrt{\mu_0 \epsilon_0}$.
> 其中 $k_0 = \omega \sqrt{\mu_0 \epsilon_0}$。

##### 6.5.2 Weak Form | 弱形式

Multiplying by a test function $\mathbf{W}$ and integrating over $\Omega$:
> 乘以测试函数 $\mathbf{W}$ 并在 $\Omega$ 上积分：

$$\int_\Omega \frac{1}{\mu} (\nabla \times \mathbf{E}) \cdot (\nabla \times \mathbf{W}) \, dV - k_0^2 \int_\Omega \epsilon_r \mathbf{E} \cdot \mathbf{W} \, dV = -j\omega \int_\Omega \mathbf{J} \cdot \mathbf{W} \, dV - \oint_{\partial\Omega} \frac{1}{\mu} (\hat{n} \times \nabla \times \mathbf{E}) \cdot \mathbf{W} \, dS. \tag{6.64}$$

> 边界项处理自然边界条件（如 PEC、PMC、吸收边界）。

##### 6.5.3 Discretization | 离散化

Expanding $\mathbf{E} = \sum_j e_j \mathbf{N}_j$ (using edge elements) and testing with $\mathbf{W}_i = \mathbf{N}_i$ gives:
> 展开 $\mathbf{E} = \sum_j e_j \mathbf{N}_j$（使用棱边元）并用 $\mathbf{W}_i = \mathbf{N}_i$ 测试：

$$\sum_j \left[ \int_\Omega \frac{1}{\mu} (\nabla \times \mathbf{N}_i) \cdot (\nabla \times \mathbf{N}_j) \, dV - k_0^2 \int_\Omega \epsilon_r \mathbf{N}_i \cdot \mathbf{N}_j \, dV \right] e_j = -j\omega \int_\Omega \mathbf{J} \cdot \mathbf{N}_i \, dV. \tag{6.67}$$

> 这给出矩阵系统 $(S - k_0^2 T) \mathbf{e} = \mathbf{b}$，其中 $S$ 是刚度矩阵，$T$ 是质量矩阵。

##### 6.5.4 Boundary Conditions | 边界条件

- **PEC ($\hat{n} \times \mathbf{E} = 0$):** Enforced by setting edge degrees of freedom on the PEC boundary to zero.
> **PEC ($\hat{n} \times \mathbf{E} = 0$)：** 通过将 PEC 边界上的棱边自由度设为零来强制执行。

- **PMC ($\hat{n} \times \mathbf{H} = 0$):** Natural boundary condition (automatic).
> **PMC ($\hat{n} \times \mathbf{H} = 0$)：** 自然边界条件（自动满足）。

- **ABC/PML (absorbing):** Handled by the boundary integral term in the weak form.
> **ABC/PML（吸收）：** 通过弱形式中的边界积分项处理。

---

#### 6.6 Low-Frequency and Eddy Current Problems | 低频与涡流问题

##### 6.6.1 The $A-\varphi$ Formulation | $A-\varphi$ 公式

For low-frequency problems (neglecting displacement current), we use the magnetic vector potential $\mathbf{A}$ and the electric scalar potential $\varphi$:
> 对于低频问题（忽略位移电流），我们使用磁矢量势 $\mathbf{A}$ 和电标量势 $\varphi$：

$$\mathbf{B} = \nabla \times \mathbf{A}, \quad \mathbf{E} = -\frac{\partial \mathbf{A}}{\partial t} - \nabla \varphi. \tag{6.80}$$

##### 6.6.2 The $T-\Omega$ Formulation | $T-\Omega$ 公式

An alternative formulation uses the electric vector potential $\mathbf{T}$ and the magnetic scalar potential $\Omega$:
> 另一种公式使用电矢量势 $\mathbf{T}$ 和磁标量势 $\Omega$：

$$\mathbf{J} = \nabla \times \mathbf{T}, \quad \mathbf{H} = \mathbf{T} - \nabla \Omega. \tag{6.82}$$

##### 6.6.3 Numerical Challenges | 数值挑战

The main difficulty with the low-frequency approximation is the null-space of the curl operator: gradient fields are in the null-space.
> 低频近似的主要困难是旋度算子的零空间：梯度场在零空间中。

This requires special preconditioners and solvers for the resulting linear system.
> 这需要为得到的线性系统设计特殊的预处理器和求解器。

---

#### 6.7 Time-Domain FEM | 时域有限元法

##### 6.7.1 Newmark Scheme | Newmark 方案

The time-dependent curl-curl equation:
> 时间相关的旋度-旋度方程：

$$\epsilon \frac{\partial^2 \mathbf{E}}{\partial t^2} + \nabla \times \left(\frac{1}{\mu} \nabla \times \mathbf{E}\right) = -\frac{\partial \mathbf{J}}{\partial t}. \tag{6.89}$$

Discretizing in space with FEM gives:
> 用 FEM 在空间离散化得到：

$$M \frac{d^2 \mathbf{e}}{dt^2} + S \mathbf{e} = \mathbf{f}, \tag{6.90}$$

where $M$ is the mass matrix and $S$ is the stiffness matrix.
> 其中 $M$ 是质量矩阵，$S$ 是刚度矩阵。

The Newmark scheme for time discretization:
> 时间离散化的 Newmark 方案：

$$\mathbf{e}^{n+1} = \mathbf{e}^n + \Delta t \dot{\mathbf{e}}^n + \frac{(\Delta t)^2}{2} \left[ (1-2\beta) \ddot{\mathbf{e}}^n + 2\beta \ddot{\mathbf{e}}^{n+1} \right], \tag{6.92}$$

$$\dot{\mathbf{e}}^{n+1} = \dot{\mathbf{e}}^n + \Delta t \left[ (1-\gamma) \ddot{\mathbf{e}}^n + \gamma \ddot{\mathbf{e}}^{n+1} \right]. \tag{6.93}$$

> 参数 $\beta$ 和 $\gamma$ 控制方案的精度和稳定性：
- $\beta = 1/4$, $\gamma = 1/2$: Trapezoidal rule (unconditionally stable, implicit)
- $\beta = 0$, $\gamma = 1/2$: Central difference (conditionally stable, explicit)

Unlike the FDTD which is explicit, time-domain FEM is typically implicit, requiring the solution of a linear system at each time step.
> 与显式的 FDTD 不同，时域 FEM 通常是隐式的，需要在每个时间步求解线性系统。

---

#### 6.8 FEM Summary | FEM 总结

**Advantages / 优势：**
- Handles complex geometry naturally / 自然处理复杂几何
- Unstructured grids allow local refinement / 非结构化网格允许局部细化
- High accuracy with higher-order elements / 高阶单元精度高
- Symmetric matrices (for self-adjoint problems) / 对称矩阵
- Unconditionally stable implicit schemes / 无条件稳定的隐式方案

**Disadvantages / 缺点：**
- More complex to program than FDTD / 编程比 FDTD 复杂
- Implicit time-stepping (solves linear system each step) / 隐式时间步进
- Need for edge elements to avoid spurious modes / 需要棱边元避免虚假模式
- Higher memory and operations per time step / 每时间步内存和运算更多

**Review Questions / 复习问题：**

6.1-1 Describe the five steps of the general FEM recipe.
> 描述 FEM 一般步骤的五个步骤。

6.2-1 Derive the weak form and the finite element equations for the 1D Helmholtz equation.
> 推导一维亥姆霍兹方程的弱形式和有限元方程。

6.3-1 Explain the assembly process for the global stiffness matrix in 2D FEM.
> 解释二维 FEM 中全局刚度矩阵的组装过程。

6.4-1 Why are edge elements preferred over nodal elements for Maxwell's equations?
> 为什么对于 Maxwell 方程组，棱边元优于节点元？

6.5-1 Derive the weak form of the curl-curl equation.
> 推导旋度-旋度方程的弱形式。

6.6-1 What is the $A-\varphi$ formulation? When is it used?
> 什么是 $A-\varphi$ 公式？何时使用？

6.7-1 Compare the Newmark scheme with the leap-frog scheme used in FDTD.
> 比较 Newmark 方案与 FDTD 中使用的蛙跳方案。
