# Bondeson《Computational Electromagnetics》第4章
> **中英双语版**

> **Source:** Anders Bondeson, Thomas Rylander, Pär Ingelström, *Computational Electromagnetics*, Springer 2005  
> **PDF:** pages 53-71 of 231 (231 total)

---

## Eigenvalues | 特征值

### 4 Eigenvalues

This chapter deals with eigenvalue problems for Maxwell's equations and related operators.
> 本章讨论 Maxwell 方程组及相关算子的特征值问题。

The eigenvalue problem arises when we seek time-harmonic solutions of the form $\mathbf{E}(\mathbf{r}, t) = \mathbf{E}(\mathbf{r}) e^{j\omega t}$.
> 当我们寻求形式为 $\mathbf{E}(\mathbf{r}, t) = \mathbf{E}(\mathbf{r}) e^{j\omega t}$ 的时谐解时，就会出现特征值问题。

For a self-adjoint operator $L$ with boundary conditions, the eigenvalues $\lambda_m$ and eigenfunctions $f_m$ satisfy

$$L[f_m] = \lambda_m f_m.$$

> 对于带有边界条件的自伴算子 $L$，特征值 $\lambda_m$ 和特征函数 $f_m$ 满足 $L[f_m] = \lambda_m f_m$。

For Maxwell's equations in a lossless cavity bounded by perfect conductors, the curl-curl equation

$$\nabla \times \frac{1}{\mu} \nabla \times \mathbf{E} = \omega^2 \epsilon \mathbf{E} \tag{4.2}$$

> 对于由理想导体包围的无损耗腔体中的 Maxwell 方程组，旋度-旋度方程 (4.2) 给出了特征值问题。

gives an eigenvalue problem where the eigenfunction is the electric field $\mathbf{E}$ and the eigenvalue is $\omega^2$.
> 其中特征函数是电场 $\mathbf{E}$，特征值是 $\omega^2$。

Using integration by parts, we can derive the following identity for the curl-curl operator:
> 使用分部积分，我们可以推导旋度-旋度算子的以下恒等式：

$$\int_\Omega \mathbf{E}_1 \cdot \left(\nabla \times \frac{1}{\mu} \nabla \times \mathbf{E}_2\right) dV = \int_\Omega \frac{1}{\mu} (\nabla \times \mathbf{E}_1) \cdot (\nabla \times \mathbf{E}_2) \, dV \tag{4.4}$$

For fields satisfying the boundary condition $\hat{n} \times \mathbf{E} = 0$, this gives
> 对于满足边界条件 $\hat{n} \times \mathbf{E} = 0$ 的场，这给出

$$\int_\Omega \mathbf{E}_1 \cdot \left(\nabla \times \frac{1}{\mu} \nabla \times \mathbf{E}_2\right) dV = \int_\Omega \mathbf{E}_2 \cdot \left(\nabla \times \frac{1}{\mu} \nabla \times \mathbf{E}_1\right) dV, \tag{4.5}$$

which demonstrates the self-adjointness of the curl-curl operator.
> 这证明了旋度-旋度算子的自伴性。

From (4.2), multiplying by the complex conjugate of $\mathbf{E}$ and integrating, we obtain the Rayleigh quotient for the eigenvalue:
> 从 (4.2) 出发，乘以 $\mathbf{E}$ 的复共轭并积分，得到特征值的瑞利商：

$$\omega^2 = \frac{\int_\Omega \mu^{-1} |\nabla \times \mathbf{E}|^2 \, dV}{\int_\Omega \epsilon |\mathbf{E}|^2 \, dV} \tag{4.6}$$

This expression is manifestly real and nonnegative. Thus, the eigenfrequencies $\omega$ are real for any lossless region bounded by perfect conductors.
> 该表达式显然是实的且非负的。因此，对于由理想导体包围的任何无损耗区域，本征频率 $\omega$ 是实数。

Damping can appear if there is dissipation of energy, for example from regions with finite electrical conductivity, or if the region is not completely enclosed by a perfect conductor.
> 如果存在能量耗散（例如来自有限电导率区域），或者区域未完全被理想导体包围，则可能出现阻尼。

**Review Questions | 复习问题**

4.1-1 What is an eigenvalue problem? What does the solution consist of and physically correspond to? To what extent is the solution uniquely defined?
> 什么是特征值问题？解由什么组成，物理上对应于什么？解的唯一性如何？

4.1-2 What is required for an operator to be self-adjoint?
> 算子需要满足什么条件才是自伴的？

4.1-3 Show that (4.5) is valid.
> 证明 (4.5) 成立。

4.1-4 Show that the eigenfrequencies $\omega$ are real for any lossless region bounded by perfect conductors. What are the physical implications of this result?
> 证明对于由理想导体包围的任何无损耗区域，本征频率 $\omega$ 是实数。此结果的物理意义是什么？

---

#### 4.2 Model Problems | 模型问题

In the previous section we showed that Maxwell's equations are self-adjoint in the absence of losses, and that this leads to real eigenfrequencies.
> 在上一节中，我们证明了在无损耗情况下 Maxwell 方程组是自伴的，并且这导致实的本征频率。

Self-adjoint equations occur in many branches of science and technology.
> 自伴方程出现在科学技术的许多分支中。

One example is the Schrödinger equation, where real eigenvalues describe well-defined energy levels of states with infinite lifetime.
> 一个例子是薛定谔方程，其中实的特征值描述了具有无限寿命的态的明确定义能级。

Another example is provided by the equations of linear elasticity, which have many properties in common with Maxwell's equations.
> 另一个例子是线弹性方程，它与 Maxwell 方程组有许多共同的性质。

This similarity comes from the fact that both can be written as a vector equation with second-order derivatives in time and space.
> 这种相似性源于两者都可以写成具有时间和空间二阶导数的矢量方程。

The only difference is that the curl-curl operator of the Maxwell equations is replaced by another second-order vector operator, involving the modulus of elasticity for bulk compression and shearing.
> 唯一的区别是 Maxwell 方程组的旋度-旋度算子被另一个涉及体压缩和剪切弹性模量的二阶矢量算子所取代。

Because of the many similarities between the two fields, it has been possible to carry over techniques originally developed in computational mechanics (see, e.g., [36]) to CEM.
> 由于这两个领域之间的许多相似性，最初在计算力学中发展的技术可以移植到 CEM。

The self-adjoint curl-curl equation (4.2) leads us to consider eigenvalue problems of the type

$$L[f] = -\omega^2 f \quad \text{in } \Omega \tag{4.7}$$

together with a suitable boundary condition on $\partial\Omega$.
> 自伴的旋度-旋度方程 (4.2) 引导我们考虑类型为 (4.7) 的特征值问题，以及在 $\partial\Omega$ 上的适当边界条件。

We will assume that $L$ is a linear self-adjoint operator with nonpositive eigenvalues.
> 我们将假设 $L$ 是具有非正特征值的线性自伴算子。

As a simple example to illustrate general principles, we will study the 1D Helmholtz equation:

$$\frac{d^2 f}{dx^2} = -k^2 f, \quad 0 < x < a, \quad f(0) = f(a) = 0. \tag{4.8}$$

> 作为一个说明一般原理的简单例子，我们将研究一维亥姆霍兹方程 (4.8)。

This equation models many 1D wave phenomena, not only in electromagnetics.
> 该方程模拟了许多一维波动现象，不仅限于电磁学。

We will use it to introduce both frequency- and time-domain techniques that will be used later to determine eigenfrequencies of more complex electromagnetic systems in two and three dimensions.
> 我们将用它来介绍频域和时域技术，这些技术将在后面用于确定更复杂的二维和三维电磁系统的本征频率。

The eigenvalue problem (4.8) is easy to solve analytically.
> 特征值问题 (4.8) 很容易解析求解。

The solutions of the differential equation are of the form $f = A \cos kx + B \sin kx$.
> 微分方程的解为 $f = A \cos kx + B \sin kx$ 的形式。

The boundary condition $f(0) = 0$ gives $A = 0$, and then $f(a) = 0$ gives $\sin ka = 0$.
> 边界条件 $f(0) = 0$ 给出 $A = 0$，然后 $f(a) = 0$ 给出 $\sin ka = 0$。

Therefore, the wavenumber $k$ can take the following values:

$$k_m = \frac{m\pi}{a}, \quad m \text{ an integer},$$

so the eigenvalues $-k_m^2 = -m^2\pi^2/a^2$ are all real and negative.
> 因此，波数 $k$ 可取 $k_m = m\pi/a$，特征值 $-k_m^2 = -m^2\pi^2/a^2$ 均为实的且为负。

**Review Question | 复习问题**

4.2-1 Calculate analytical eigenvalues and eigenfunctions to the eigenvalue problem $d^2f/dx^2 = -k^2f$ with $f(0) = f(a) = 0$.
> 计算特征值问题 $d^2f/dx^2 = -k^2f$（$f(0) = f(a) = 0$）的解析特征值和特征函数。

---

#### 4.3 Frequency-Domain Eigenvalue Calculation | 频域特征值计算

Frequency-domain eigenvalue problems of the form $L[f] = \lambda f$ are generally transformed into corresponding algebraic eigenvalue problems of the form $A\mathbf{f} = \lambda \mathbf{f}$ by, for example, a finite difference approximation.
> 形式为 $L[f] = \lambda f$ 的频域特征值问题通常通过有限差分近似等变换为相应的代数特征值问题 $A\mathbf{f} = \lambda \mathbf{f}$。

Therefore, the numerical solution of a frequency-domain eigenvalue problem involves the solution of an algebraic eigenvalue problem.
> 因此，频域特征值问题的数值求解涉及代数特征值问题的求解。

##### 4.3.1 MATLAB: The 1D Helmholtz Equation

To discretize the 1D Helmholtz equation (4.8) by finite differences, we divide the interval $[0, a]$ into $N$ subintervals of equal length $h = a/N$.
> 为用有限差分离散化一维亥姆霍兹方程 (4.8)，我们将区间 $[0, a]$ 等分为 $N$ 个长度为 $h = a/N$ 的子区间。

The simplest finite difference approximation of (4.8) is

$$\frac{f_{i-1} - 2f_i + f_{i+1}}{h^2} = -k^2 f_i, \quad i = 1, 2, \ldots, N-1. \tag{4.9}$$

> (4.8) 的最简单有限差分近似为 (4.9)。

The boundary conditions are $f_0 = f_N = 0$, so there is no reason to include $f_0$ and $f_N$ as unknowns.
> 边界条件为 $f_0 = f_N = 0$，因此没有必要将 $f_0$ 和 $f_N$ 作为未知量。

Equation (4.9) can be written as a linear system with an $(N-1) \times (N-1)$ matrix $A$:
> 方程 (4.9) 可写为 $(N-1) \times (N-1)$ 矩阵 $A$ 的线性系统：

$$A\mathbf{f} = \lambda \mathbf{f}.$$

Note that the matrix $A$ is tridiagonal, with nonzero elements on the main diagonal and one lower and one upper subdiagonal.
> 注意矩阵 $A$ 是三对角的，在主对角线以及下、上次对角线上有非零元素。

When $n$ is large, $A$ consists mostly of zeros, and this can be exploited by saving the matrix in sparse form.
> 当 $n$ 很大时，$A$ 主要由零组成，可以通过以稀疏形式保存矩阵来利用这一点。

The physical eigenvalues $-k^2$ are simply the eigenvalues of the matrix $A$.
> 物理特征值 $-k^2$ 就是矩阵 $A$ 的特征值。

These eigenvalues can be computed with the MATLAB routine `eig`, which computes all eigenvalues and corresponding eigenvectors of an algebraic eigenvalue problem.
> 这些特征值可以用 MATLAB 例程 `eig` 计算，该例程计算代数特征值问题的所有特征值和相应的特征向量。

We calculate the first two numerical wavenumbers $k$ on the interval $[0, \pi]$ for four different resolutions. The analytical results are $k = 1, 2, 3, \ldots$, and the numerical results are shown in Table 4.1.
> 我们在区间 $[0, \pi]$ 上对四种不同分辨率计算前两个数值波数 $k$。解析结果为 $k = 1, 2, 3, \ldots$，数值结果如表 4.1 所示。

**Table 4.1.** The two lowest wavenumbers from FD discretizations with different resolutions.
> **表 4.1.** 不同分辨率下有限差分离散化的两个最低波数。

| $N$ [-] | $h$ [m] | $k_1$ [1/m] | $k_2$ [1/m] |
|---------|---------|-------------|-------------|
| 10 | 0.1000 | 0.99589 27352 4357 | 1.96726 32861 6693 |
| 20 | 0.0500 | 0.99897 22332 4854 | 1.99178 54704 8714 |
| 30 | 0.0333 | 0.99954 31365 0068 | 1.99634 65947 4160 |
| 40 | 0.0250 | 0.99974 29988 6918 | 1.99794 44664 9703 |

Plots of $k_m$ versus $h^p$ show a straight line when $p = 2$, which means that the convergence is quadratic.
> 将 $k_m$ 对 $h^p$ 作图，$p = 2$ 时显示为直线，这意味着收敛是二次的。

Extrapolation of the first eigenvalue to zero cell size using `polyfit` gives: linear extrapolation 0.99999 93697 896, quadratic 0.99999 99999 437, and cubic 0.99999 99999 997, which is very close to the exact value 1.
> 使用 `polyfit` 将第一个特征值外推到零单元尺寸得到：线性外推 0.99999 93697 896，二次外推 0.99999 99999 437，三次外推 0.99999 99999 997，非常接近精确值 1。

For the second eigenvalue, linear extrapolation gives 1.99997 98747 162, quadratic 1.99999 99928 090, and cubic 1.99999 99999 989.
> 对于第二个特征值，线性外推给出 1.99997 98747 162，二次外推给出 1.99999 99928 090，三次外推给出 1.99999 99999 989。

Thus, the two lowest eigenvalues could be computed with 12-digit accuracy using the cubic fit for extrapolation, even though the computations have only about 4-digit accuracy.
> 因此，使用三次拟合外推，即使计算只有约 4 位精度，两个最低特征值也可以达到 12 位精度。

The error is larger for the second eigenmode. The second eigenmode oscillates twice as fast and needs twice the resolution to be computed with the same accuracy as the first, as is confirmed by Table 4.1.
> 第二个本征模的误差更大。第二个本征模振荡速度快两倍，需要两倍的分辨率才能达到与第一个相同的精度，如表 4.1 所示。

**Review Questions | 复习问题**

4.3-1 Use finite differences to discretize the eigenvalue problem $d^2f/dx^2 = -k^2f$ with $f(0) = f(a) = 0$. Write down the corresponding matrix eigenvalue problem.
> 使用有限差分离散化特征值问题 $d^2f/dx^2 = -k^2f$（$f(0) = f(a) = 0$），写出相应的矩阵特征值问题。

4.3-2 What is the order of convergence for $k$ in (4.9)?
> (4.9) 中 $k$ 的收敛阶是多少？

4.3-3 Why is the error, in general, larger for higher eigenmodes? What situations could change this?
> 为什么通常情况下高阶本征模的误差更大？什么情况可能改变这一点？

---

#### 4.4 Time-Domain Eigenvalue Calculation | 时域特征值计算

One common way of determining eigenfrequencies in CEM is to time-step a solution, using for example a finite difference program, record the field at some location, and then Fourier transform this signal to locate its main frequency components.
> CEM 中确定本征频率的一种常见方法是对解进行时间步进（例如使用有限差分程序），记录某位置的场，然后对该信号进行傅里叶变换以定位其主要频率分量。

This technique can be used for more general methods than the finite differences.
> 该技术可用于比有限差分更通用的方法。

It can be used to find the eigenvalues of any spatial operator $L$ with real and negative eigenvalues,

$$L[f] = -\omega^2 f. \tag{4.10}$$

> 它可以用于求任何具有实负特征值的空间算子 $L$ 的特征值。

Equation (4.10) is written in such a form that it is the frequency-domain form of the time-domain equation

$$\frac{\partial^2 f}{\partial t^2} = L[f], \tag{4.11}$$

> 方程 (4.10) 的形式使其成为时域方程 (4.11) 的频域形式。

which is, most likely, what the eigenvalue problem (4.10) was derived from.
> 这很可能就是特征值问题 (4.10) 的导出来源。

The simplest time-discretization of (4.11) is

$$\frac{f^{(n+1)} - 2f^{(n)} + f^{(n-1)}}{(\Delta t)^2} = L[f^{(n)}], \tag{4.12}$$

> (4.11) 的最简单时间离散化为 (4.12)，

where $\Delta t$ is the time step.
> 其中 $\Delta t$ 为时间步长。

An important advantage of this formulation is that the time-stepping is explicit, that is, no matrix inversion is needed to compute $f^{(n+1)}$:

$$f^{(n+1)} = 2f^{(n)} - f^{(n-1)} + (\Delta t)^2 L[f^{(n)}]. \tag{4.13}$$

> 该公式的一个重要优点是时间步进是显式的，即计算 $f^{(n+1)}$ 不需要矩阵求逆。

Such time-stepping schemes, often referred to as "leap-frog," are very efficient, and allow determination of the complete eigenvalue spectrum of (4.10).
> 这种通常称为"蛙跳"的时间步进方案非常高效，允许确定 (4.10) 的完整特征值谱。

An important issue for explicit time-stepping schemes is how to choose the time-step $\Delta t$. This is mainly determined by stability.
> 显式时间步进方案的一个重要问题是如何选择时间步长 $\Delta t$，这主要由稳定性决定。

##### 4.4.1 Stability Analysis | 稳定性分析

Before working out a specific example, we discuss how one can analyze the stability of a time-stepping algorithm such as (4.13).
> 在具体例子之前，我们讨论如何分析如 (4.13) 的时间步进算法的稳定性。

The following technique is known as von Neumann stability analysis.
> 以下技术称为 von Neumann 稳定性分析。

The analysis is based on the fact that any discrete time equation, which has no explicit time dependence, has solutions of the form $f^{(n)} = f_\omega \rho^n$, that is, geometrical sequences in discrete time.
> 该分析基于以下事实：任何没有显式时间依赖关系的离散时间方程都有 $f^{(n)} = f_\omega \rho^n$ 形式的解，即离散时间中的几何序列。

Here, $\rho$ is called the amplification factor of the eigenmode $f_\omega$, and stability requires $|\rho| \leq 1$ for all eigenmodes.
> 这里 $\rho$ 称为本征模 $f_\omega$ 的放大因子，稳定性要求对所有本征模 $|\rho| \leq 1$。

Substituting $f^{(n)} = f_\omega \rho^n$ into (4.13), and using $L[f_\omega] = -\omega^2 f_\omega$, we obtain a quadratic equation for the amplification factor

$$\rho^2 - [2 - (\omega \Delta t)^2] \rho + 1 = 0 \tag{4.14}$$

> 将 $f^{(n)} = f_\omega \rho^n$ 代入 (4.13)，并利用 $L[f_\omega] = -\omega^2 f_\omega$，得到放大因子的二次方程 (4.14)，

with the solutions

$$\rho = 1 - \frac{1}{2}(\omega \Delta t)^2 \pm j \omega \Delta t \sqrt{1 - \frac{1}{4}(\omega \Delta t)^2}. \tag{4.15}$$

> 其解为 (4.15)。

If $(\omega \Delta t)^2 \leq 4$, there are two complex conjugate solutions such that $|\rho|^2 = (\text{Re}\,\rho)^2 + (\text{Im}\,\rho)^2 = 1$.
> 如果 $(\omega \Delta t)^2 \leq 4$，存在两个复共轭解，使得 $|\rho|^2 = 1$。

On the other hand, if $(\omega \Delta t)^2 > 4$, there are two real solutions, whose product is unity, so one of them has modulus larger than 1.
> 另一方面，如果 $(\omega \Delta t)^2 > 4$，存在两个实解，其乘积为 1，所以其中一个模大于 1。

The roots stay on the unit circle $|\rho| = 1$ as long as $|\omega \Delta t| \leq 2$, but when $|\omega \Delta t| > 2$, one root has modulus larger than unity.
> 只要 $|\omega \Delta t| \leq 2$，根就保持在单位圆 $|\rho| = 1$ 上，但当 $|\omega \Delta t| > 2$ 时，一个根的模大于 1。

Therefore, if $|\omega \Delta t| > 2$, the solution will grow exponentially in time, and the scheme for time-stepping is unstable.
> 因此，如果 $|\omega \Delta t| > 2$，解将随时间指数增长，时间步进方案不稳定。

Thus, the explicit time-stepping scheme in (4.13) has a stability limit for the time-step: $\Delta t \leq 2/|\omega|$.
> 因此，(4.13) 中的显式时间步进方案存在时间步长的稳定性限制：$\Delta t \leq 2/|\omega|$。

Since this has to hold for all the eigenmodes of (4.10), the condition on the time-step for the explicit scheme is

$$\Delta t \leq \frac{2}{|\omega_{\text{max}}|}. \tag{4.16}$$

> 由于这必须对 (4.10) 的所有本征模成立，显式方案的时间步长条件为 (4.16)。

This means that the time-step times the highest eigenfrequency $f_{\text{max}} = \omega_{\text{max}}/2\pi$ should be at most $1/\pi$.
> 这意味着时间步长乘以最高本征频率 $f_{\text{max}} = \omega_{\text{max}}/2\pi$ 应至多为 $1/\pi$。

If we apply this stability limit to the operator $L = d^2/dx^2$ discretized on a uniform grid with cell size $h$, the largest numerical eigenvalue is $\omega_{\text{max}}^2 = 4/h^2$.
> 如果将此稳定性限制应用于在单元尺寸为 $h$ 的均匀网格上离散化的算子 $L = d^2/dx^2$，最大数值特征值为 $\omega_{\text{max}}^2 = 4/h^2$。

Thus, $\omega_{\text{max}} = 2/h$, and stability requires $\Delta t \leq 2/\omega_{\text{max}} = h$.
> 因此 $\omega_{\text{max}} = 2/h$，稳定性要求 $\Delta t \leq h$。

We conclude that the time-step for our simple explicit scheme for the wave equation $\partial^2 f/\partial t^2 = \partial^2 f/\partial x^2$ should not be larger than the space step, for stability reasons.
> 我们得出结论：出于稳定性原因，波动方程 $\partial^2 f/\partial t^2 = \partial^2 f/\partial x^2$ 的简单显式方案的时间步长不应大于空间步长。

The von Neumann stability analysis is closely related to the analysis in Section 3.2.3.
> von Neumann 稳定性分析与第 3.2.3 节的分析密切相关。

The FDTD has a time-step limit $\Delta t < h/(c\sqrt{3})$ in three dimensions, where $\Delta t$ is the time-step, $h$ is the cell size, and $c$ is the speed of light.
> 在三维中，FDTD 存在时间步长限制 $\Delta t < h/(c\sqrt{3})$，其中 $\Delta t$ 为时间步长，$h$ 为单元尺寸，$c$ 为光速。

This is a serious limitation in problems involving time scales much longer than it takes a light wave to cross the simulation region.
> 对于涉及远大于光波穿越模拟区域所需时间尺度的问题，这是一个严重的限制。

##### 4.4.2 MATLAB: The 1D Wave Equation

As a simple illustration of how to extract spectral information by explicit time-stepping, we seek the spectrum $-\omega^2$ of the operator $L = \partial^2/\partial x^2$ on the interval $0 < x < a$ with the boundary conditions $f(0, t) = f(a, t) = 0$.
> 作为通过显式时间步进提取频谱信息的简单说明，我们求区间 $0 < x < a$ 上算子 $L = \partial^2/\partial x^2$ 的谱 $-\omega^2$，边界条件为 $f(0, t) = f(a, t) = 0$。

The true eigenfrequencies are $\omega_m = m\pi c/a$, $m = 1, 2, \ldots$.
> 真实本征频率为 $\omega_m = m\pi c/a$, $m = 1, 2, \ldots$。

The spectrum of $L$ can be found by solving the wave equation

$$\frac{\partial^2 f}{\partial t^2} = \frac{\partial^2 f}{\partial x^2}, \quad 0 < x < a, \quad f(0, t) = f(a, t) = 0. \tag{4.18}$$

> $L$ 的谱可以通过求解波动方程 (4.18) 得到。

We use the simplest finite difference scheme:

$$f_i^{(n+1)} = 2f_i^{(n)} - f_i^{(n-1)} + \left(\frac{\Delta t}{h}\right)^2 \left(f_{i+1}^{(n)} + f_{i-1}^{(n)} - 2f_i^{(n)}\right) \tag{4.19}$$

> 我们使用最简单的有限差分格式 (4.19)。

A powerful way to find several resonant frequencies of a microwave cavity is to perform an FDTD simulation and then Fourier transform selected signals in time.
> 找到微波腔体多个谐振频率的一种强大方法是执行 FDTD 模拟，然后对选定的时域信号进行傅里叶变换。

This is the same procedure that we discussed for finding the eigenvalues of the 1D Helmholtz equation in Chapter 4.
> 这与我们在第 4 章中讨论的求一维亥姆霍兹方程特征值的方法相同。

**Review Questions | 复习问题**

4.4-1 How are the eigenvalues extracted from a time-domain eigenvalue calculation? Can the corresponding eigenmodes be extracted in a simple way?
> 如何从时域特征值计算中提取特征值？能否以简单方式提取相应的本征模？

4.4-2 What considerations should be taken into account in selecting the time-step $\Delta t$?
> 选择时间步长 $\Delta t$ 时应考虑哪些因素？

4.4-3 What is an explicit time-stepping method?
> 什么是显式时间步进方法？

4.4-4 Describe the meaning and the use of the amplification factor in words.
> 用语言描述放大因子的含义和用途。

4.4-5 How does the highest eigenfrequency relate to the maximal stable time-step for (4.13)?
> 最高本征频率与 (4.13) 的最大稳定时间步长有何关系？

4.4-6 How well is the true oscillation frequency reproduced by (4.15)? Quantify your answer.
> (4.15) 对真实振荡频率的再现效果如何？量化你的答案。

4.4-7 How do the excitation and detector positions influence the frequency spectrum computed from a time-domain method?
> 激励和检测器位置如何影响时域方法计算的频谱？

4.4-8 Why are the frequency estimates of the FFT sensitive to how close the various undamped resonances are to making an integer number of oscillations during the simulation?
> 为什么 FFT 的频率估计对各个无阻尼谐振在模拟期间是否接近整数次振荡很敏感？

---

#### Summary | 小结

The solution of the eigenvalue problem $L[f_m] = \lambda_m f_m$ consists of pairs of eigenvalues $\lambda_m$ and eigenvectors $f_m$, where the pairs typically are indexed by an integer $m$.
> 特征值问题 $L[f_m] = \lambda_m f_m$ 的解由特征值 $\lambda_m$ 和特征向量 $f_m$ 组成，这些对通常由整数 $m$ 索引。

For Maxwell's equations, we have $\nabla \times \mu^{-1} \nabla \times \mathbf{E}_m = \omega_m^2 \epsilon \mathbf{E}_m$, where the eigenfunction is $\mathbf{E}_m$ and the eigenvalue is $\omega_m^2$.
> 对于 Maxwell 方程组，有 $\nabla \times \mu^{-1} \nabla \times \mathbf{E}_m = \omega_m^2 \epsilon \mathbf{E}_m$，其中特征函数为 $\mathbf{E}_m$，特征值为 $\omega_m^2$。

For the 1D Helmholtz equation $d^2f/dx^2 = -k^2f$ on $0 < x < a$ with $f(0) = f(a) = 0$, the eigenvalues are $k^2 = (\pi m/a)^2$ with integer $m = 1, 2, \ldots$ for the continuous problem.
> 对于一维亥姆霍兹方程，连续问题的特征值为 $k^2 = (\pi m/a)^2$。

A time-domain computation of eigenvalues is based on the inverse Fourier transform of $L[f] = -\omega^2 f$, i.e., $L[f] = \partial^2 f/\partial t^2$.
> 特征值的时域计算基于 $L[f] = -\omega^2 f$ 的逆傅里叶变换，即 $L[f] = \partial^2 f/\partial t^2$。

Stable time-stepping is achieved for $\Delta t < 2/|\omega_{\text{max}}|$, where $\omega_{\text{max}}$ is the highest eigenfrequency.
> 当 $\Delta t < 2/|\omega_{\text{max}}|$ 时实现稳定的时间步进，其中 $\omega_{\text{max}}$ 为最高本征频率。

---

#### Problems | 习题

P.4-1 Calculate the eigenvalues $k^2$ of the vector wave equation $\nabla \times \nabla \times \mathbf{E} = k^2 \mathbf{E}$ for a 2D rectangular cavity with PEC boundaries.
> 计算具有 PEC 边界的二维矩形腔体中矢量波动方程 $\nabla \times \nabla \times \mathbf{E} = k^2 \mathbf{E}$ 的特征值 $k^2$。

P.4-2 Show that the eigenvalues of the discretized 1D Helmholtz equation (4.9), for $a = \pi$, are $-k^2 = -(4/h^2) \sin^2(mh/2)$, $m = 1, 2, 3, \ldots$, and find how the error in $k$ depends on the mode number and resolution.
> 证明离散化一维亥姆霍兹方程的特征值，并找出 $k$ 的误差如何依赖于模式数和分辨率。

P.4-3 Let the electric field be $\mathbf{E} = \hat{z} E_z(x)$ for a 1D cavity with PEC walls and constant $\mu$ and $\epsilon$. Use the finite difference scheme and show that (4.6) can be rewritten as $\omega^2 = (\mathbf{e}^T A \mathbf{e})/(\mathbf{e}^T \mathbf{e})$, where $\mathbf{e}$ is a vector with the electric field at the interior grid points.
> 对于具有 PEC 壁和常数 $\mu$、$\epsilon$ 的一维腔体，使用有限差分格式证明 (4.6) 可改写为 $\omega^2 = (\mathbf{e}^T A \mathbf{e})/(\mathbf{e}^T \mathbf{e})$。

P.4-4 In one dimension, Helmholtz equation gives $L = d^2/dx^2$. Find a nonzero solution $f$ that yields $L[f] = 0$ and solve (4.10) and (4.11) for that particular solution.
> 在一维中，亥姆霍兹方程给出 $L = d^2/dx^2$，求满足 $L[f] = 0$ 的非零解。

P.4-5 Consider the questions in the previous exercise when the operator $L = d^2/dx^2$ is discretized by finite differences. How do you treat the boundary conditions so that the order of convergence associated with the finite difference stencils of the interior grid points is preserved?
> 当算子 $L = d^2/dx^2$ 由有限差分离散化时，考虑前一习题的问题。如何处理边界条件以保持内部网格点有限差分模板的收敛阶？

P.4-6 Discretize $L = \partial^2/\partial x^2$ with finite differences so that the dominant term in the error is $O(h^4)$ and derive the stability limit on $\Delta t$ for (4.13). Compare with the $O(h^2)$ case.
> 用有限差分离散化 $L = \partial^2/\partial x^2$ 使误差的主要项为 $O(h^4)$，推导 (4.13) 关于 $\Delta t$ 的稳定性限制，并与 $O(h^2)$ 情况比较。

P.4-7 Compute the discrete Fourier transform of the signal $\sin(\omega t)$ sampled at $t = n\Delta t$, $n = 0, 1, \ldots, N-1$.
> 计算在 $t = n\Delta t$ 采样的信号 $\sin(\omega t)$ 的离散傅里叶变换。

P.4-8 For three resonances, rewrite (4.21) as a ratio of polynomials $s(\omega) = P(\omega)/Q(\omega)$. Use the inverse Fourier transform to derive the time-domain expression.
> 对于三个谐振，将 (4.21) 重写为多项式之比 $s(\omega) = P(\omega)/Q(\omega)$，使用逆傅里叶变换推导时域表达式。

---

#### Computer Projects | 计算机项目

C.4-1 Write a program that solves for the eigenmodes and eigenvalues based on a finite difference discretization of the TE and TM problem for a waveguide with rectangular cross section.
> 编写程序，基于有限差分离散化求解矩形截面波导的 TE 和 TM 问题的本征模和特征值。

C.4-2 Equation (4.2) with losses and constant permeability is given by $\nabla \times \nabla \times \mathbf{E} = \mu(\omega^2 \epsilon - j\omega \sigma) \mathbf{E}$. Implement a finite-difference algorithm and solve for the resonance frequencies and quality factors of a square cavity with PEC boundaries.
> 实现有限差分算法，求解具有 PEC 边界的方形腔体的谐振频率和品质因数。

---

### The Finite-Difference Time-Domain Method | 时域有限差分法

The finite-difference time-domain method, or FDTD for short, is one of the most popular computational methods for microwave problems; it is simple to program, highly efficient, and easily adapted to deal with a variety of problems.
> 时域有限差分法（简称 FDTD）是微波问题中最流行的计算方法之一；它编程简单、效率高、易于适应各种问题。

A major weakness of the method lies in the way it deals with boundaries that are not aligned with the Cartesian grid: for oblique boundaries, FDTD programs typically resort to the "staircase approximation."
> 该方法的主要弱点在于处理与笛卡尔网格不对齐的边界的方式：对于倾斜边界，FDTD 程序通常采用"阶梯近似"。

The finite element method (FEM), which will be discussed in Chapter 6, is better suited for problems with oblique and curved boundaries and fine structures that may need higher resolution locally.
> 将在第 6 章讨论的有限元法（FEM）更适合处理倾斜和弯曲边界以及局部需要更高分辨率的精细结构。

However, the FDTD allows for explicit time-stepping, and this makes it much more efficient than time-domain FEM, which in general is implicit (i.e., a system of equations must be solved at each time step).
> 然而，FDTD 允许显式时间步进，这使其比通常为隐式的时域 FEM 高效得多（即必须在每个时间步求解方程组）。

Another advantage of the FDTD is that no matrix has to be stored. This reduces memory consumption and makes it possible to solve problems with a very large number of unknowns.
> FDTD 的另一个优点是不需要存储矩阵。这减少了内存消耗，使得求解具有大量未知量的问题成为可能。

The type of problems for which the FDTD is particularly suited involves the propagation of electromagnetic waves and geometries where characteristic lengths are comparable to a wavelength.
> FDTD 特别适合的问题类型涉及电磁波传播以及特征长度与波长相当的几何结构。

This typically includes microwave problems. Similar conditions also apply for optical devices whose dimensions are comparable to the wavelength.
> 这通常包括微波问题。类似条件也适用于尺寸与波长相当的光学器件。
