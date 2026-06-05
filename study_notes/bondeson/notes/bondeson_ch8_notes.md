# Bondeson《Computational Electromagnetics》第8章
> **中英双语版**

> **Source:** Anders Bondeson, Thomas Rylander, Pär Ingelström, *Computational Electromagnetics*, Springer 2005  
> **PDF:** pages 204-221 of 231 (231 total)

---

## Summary and Overview | 总结与概述

### 8 Summary and Overview

Successful hybrid methods offer possibilities to treat significantly larger classes of problems.
> 成功的混合方法提供了处理更广泛问题的可能性。

One of the major challenges in CEM is to model systems that are electrically large, that is, for which the spatial extent $D$ is many wavelengths $\lambda$ in three dimensions.
> CEM 的主要挑战之一是对电大尺寸系统进行建模，即空间范围 $D$ 在三维中为多个波长 $\lambda$ 的系统。

In this setting, it is useful to compare how the number of floating-point operations and the memory requirements for the different methods scale with the wave frequency $f$ for a system of fixed spatial extent.
> 在此背景下，比较不同方法在固定空间范围的系统中浮点运算次数和内存需求如何随波频率 $f$ 变化是很有用的。

**Table 8.1.** Scalings for the number of operations with frequency $f$ and the number of iterations $N_{it}$.
> **表 8.1.** 运算次数随频率 $f$ 和迭代次数 $N_{it}$ 的缩放关系。

| Method | 2D | 3D |
|--------|----|----|
| FEM/FDTD | $N_{it} f^2$ | $N_{it} f^3$ |
| MoM-matrix | $N_{it} f^4$ | $N_{it} f^4$ |
| MoM-MLFMA | $N_{it} f \log f$ | $N_{it} f^2 \log f$ |

It should be pointed out that there are multipliers in front of the scalings in Table 8.1, and that these coefficients can be quite significant.
> 需要指出的是，表 8.1 中的缩放关系前面有乘数因子，这些系数可能相当显著。

For instance, the multiplier is large for the MLFMA (which is a version of the MoM), so that the application problems need to be quite large before this method is competitive.
> 例如，MLFMA（MoM 的一种版本）的乘数很大，因此该方法需要相当大规模的问题才具有竞争力。

However, the MLFMA is the most competitive full-wave method for very large scale scattering problems, e.g., to compute the radar cross section for an entire aircraft.
> 然而，MLFMA 是超大规模散射问题（例如计算整架飞机的雷达散射截面）中最具竞争力的全波方法。

---

#### 8.1 Differential Equation Solvers | 微分方程求解器

Differential equation solvers are used for both frequency- and time-domain computations. They can be applied to both driven problems and eigenvalue problems.
> 微分方程求解器用于频域和时域计算，可应用于受驱问题和特征值问题。

For differential equation solvers in frequency domain, one often uses iterative solvers (especially in three dimensions).
> 对于频域中的微分方程求解器，通常使用迭代求解器（特别是在三维中）。

The number of iterations needed for convergence scales as the square root of the condition number $\kappa$ of the matrix, where $\kappa$ is the ratio of largest to smallest eigenvalues.
> 收敛所需的迭代次数与矩阵条件数 $\kappa$ 的平方根成正比，$\kappa$ 为最大与最小特征值之比。

Therefore, for frequency-domain FEM (or finite difference methods) the total number of operations scales as $f^3$ in 2D and $f^4$ in 3D (for a single frequency).
> 因此，对于频域 FEM（或有限差分方法），总运算次数在二维中按 $f^3$ 缩放，在三维中按 $f^4$ 缩放（对于单频）。

For differential equation solvers in time domain, the time-step varies as $h \propto 1/f$, so the number of operations for time-domain methods (such as FDTD) scales as $f^3$ in 2D and $f^4$ in 3D. But the time-domain method gives a complete frequency spectrum.
> 对于时域微分方程求解器，时间步长按 $h \propto 1/f$ 变化，因此时域方法（如 FDTD）的运算次数在二维中按 $f^3$、在三维中按 $f^4$ 缩放。但时域方法给出完整的频谱。

##### 8.1.1 Finite-Difference Time-Domain | 时域有限差分法

To keep a certain relative phase error, the FDTD needs a certain number of points per wavelength $\lambda/h$; 1% phase error requires about 18 cells per wavelength.
> 为保持一定的相对相位误差，FDTD 需要一定数量的每波长点数；1% 的相位误差需要约 18 个单元每波长。

The major drawback of the FDTD is that it is tied to structured grids, which force oblique boundaries to appear as "staircases."
> FDTD 的主要缺点是其局限于结构化网格，这迫使倾斜边界以"阶梯"形式出现。

##### 8.1.2 Finite-Volume Time-Domain | 时域有限体积法

Finite volume time-domain (FVTD) methods generate discrete equations by integrating the Ampère and Faraday laws over each grid cell.
> 时域有限体积法（FVTD）通过对每个网格单元积分安培定律和法拉第定律来生成离散方程。

Unlike the FDTD, the FVTD does not conserve electric and magnetic charges.
> 与 FDTD 不同，FVTD 不守恒电荷和磁荷。

The FVTD is explicit and therefore efficient, as long as the cells are of reasonably uniform size.
> FVTD 是显式的，因此只要单元尺寸合理均匀，其效率就很高。

The primary grid can be made of tetrahedra, which gives the method good ability to model complex geometry.
> 主网格可以由四面体构成，这使该方法具有良好的复杂几何建模能力。

A drawback of the FVTD is the appearance of a weak "late time" instability. This can be prevented by adding dissipation, which, however, may decrease accuracy.
> FVTD 的一个缺点是出现弱的"晚期"不稳定性。可以通过添加耗散来防止，但这可能会降低精度。

##### 8.1.3 Finite Element Method | 有限元法

The finite element method easily handles complex geometry, and FEM is used both in frequency- and time-domain analyses.
> 有限元法易于处理复杂几何形状，FEM 在频域和时域分析中都有应用。

Together with standard iterative solvers, a frequency-domain calculation requires $O(f^4)$ operations per frequency.
> 结合标准迭代求解器，频域计算每频率需要 $O(f^4)$ 次运算。

The scaling in time-domain calculations is the same as for the FDTD, but time-domain FEM typically involves at least a factor of 10 more operations.
> 时域计算的缩放关系与 FDTD 相同，但时域 FEM 通常需要至少多 10 倍的运算量。

A valuable property of the finite element method, in comparison to the FVTD, is that both the mass matrix and the stiffness matrix are symmetric and real, which guarantees that the eigenvalues $\omega^2$ are real.
> 与 FVTD 相比，有限元法的一个宝贵性质是质量矩阵和刚度矩阵都是对称且实的，这保证了特征值 $\omega^2$ 是实数。

##### 8.1.4 Transmission Line Method | 传输线法

Transmission line methods (TLM) work with combinations of electric and magnetic fields, represented as pulses propagating on a 3D grid of transmission lines.
> 传输线法（TLM）使用电场和磁场的组合，表示为在三维传输线网格上传播的脉冲。

At the intersections, the nodes, the pulses are scattered according to scattering matrices. By imposing unitary condition, energy conservation can be enforced.
> 在交点（节点）处，脉冲根据散射矩阵散射。通过施加幺正条件，可以强制执行能量守恒。

##### 8.1.5 Finite Integration Technique | 有限积分技术

The finite integration technique (FIT) is based on the integral representation of Maxwell's equations.
> 有限积分技术（FIT）基于 Maxwell 方程组的积分表示。

The FIT reduces to the FDTD scheme on grids consisting of cubes.
> FIT 在立方体网格上简化为 FDTD 格式。

The matrix operators correctly reproduce well-known properties; for example, the zero divergence of the curl is $DC = 0$ and the zero curl of the gradient is $C \tilde{D}^T = 0$.
> 矩阵算子正确地再现了众所周知的性质；例如，旋度的零散度为 $DC = 0$，梯度的零旋度为 $C \tilde{D}^T = 0$。

The property $C = \tilde{C}^T$ is important for stability, and the diagonal matrices allow for explicit time-stepping.
> 性质 $C = \tilde{C}^T$ 对稳定性很重要，对角矩阵允许显式时间步进。

---

#### 8.2 Integral Equation Solvers | 积分方程求解器

For integral equations, the number of unknowns is much smaller than for volume discretizations such as FDTD or FEM, but the matrix is dense.
> 对于积分方程，未知量数量远小于 FDTD 或 FEM 等体离散化方法，但矩阵是稠密的。

The integral formulation is nevertheless superior for large problems because of the fast multipole method (FMM).
> 然而，由于快速多极子法（FMM），积分公式对于大问题仍具有优势。

The hierarchical version is called the MLFMA (multilevel fast multipole algorithm). The operation count becomes $\propto N_{it} f \log f$ in 2D and $N_{it} f^2 \log f$ in 3D.
> 层次化版本称为多层快速多极子算法（MLFMA）。

##### 8.2.1 Frequency-Domain Integral Equations | 频域积分方程

In frequency-domain formulations, both the EFIE and the MFIE may suffer from internal resonance; this can be avoided by using the CFIE (combined field integral equation).
> 在频域公式中，EFIE 和 MFIE 都可能遭受内部谐振；这可以通过使用 CFIE 来避免。

A main advantage of the MoM is the low number of unknowns, which scale with frequency as $O(f^2)$.
> MoM 的一个主要优点是未知量数量少，按 $O(f^2)$ 随频率缩放。

However, the matrix is dense, so direct solution by LU decomposition has $O(f^6)$ scaling.
> 然而，矩阵是稠密的，因此通过 LU 分解直接求解具有 $O(f^6)$ 的缩放关系。

**Fast Multipole Methods | 快速多极子方法**

The FMM was introduced by Rokhlin and developed into the MLFMA by a group at the University of Illinois.
> FMM 由 Rokhlin 引入，并由伊利诺伊大学的一个团队发展为 MLFMA。

The savings come from the fact that only a moderate number of terms are needed in the multipole expansion.
> 节省的来源是多重极子展开中只需要中等数量的项。

For 3D problems the FMM gives $O(f^3)$ and the MLFMA gives $O(f^2 \log f)$ scaling per iteration.
> 对于三维问题，FMM 给出 $O(f^3)$ 的缩放，MLFMA 给出每次迭代 $O(f^2 \log f)$ 的缩放。

##### 8.2.2 Time-Domain Integral Equations | 时域积分方程

Time-domain integral equations (TDIE) is a relatively new area of research.
> 时域积分方程（TDIE）是一个相对较新的研究领域。

The time-domain MFIE can be written as

$$2\pi \mathbf{J}(\mathbf{r}, t) = 2\pi \hat{n} \times \mathbf{H}^i(\mathbf{r}, t) + \hat{n} \times \int_{S'} \left[ \frac{\hat{R} \times \mathbf{J}(\mathbf{r}', \tau)}{R^2} + \frac{\hat{R} \times \partial \mathbf{J}(\mathbf{r}', \tau)/\partial \tau}{cR} \right] dS', \tag{8.1}$$

where $\tau = t - R/c$ is the retarded time and $R = |\mathbf{r} - \mathbf{r}'|$.
> 其中 $\tau = t - R/c$ 为延迟时间，$R = |\mathbf{r} - \mathbf{r}'|$。

The early TDIE algorithms were unstable and required dissipation for stability. This problem appears to have been overcome recently for the EFIE.
> 早期的 TDIE 算法不稳定，需要耗散来维持稳定性。最近对于 EFIE 这个问题似乎已被克服。

---

#### 8.3 Hybrid Methods | 混合方法

The different basic techniques used in CEM all have their strengths and limitations.
> CEM 中使用的不同基本技术都有各自的优势和局限性。

One way to achieve better performance than two individual methods is to combine them into a hybrid method.
> 要获得优于两种单独方法的性能，一种方法是将它们组合成混合方法。

The FDTD is efficient, but has difficulties with complex geometry. Therefore, hybrid methods combine the FDTD with either FVTD or time-domain FEM.
> FDTD 效率高，但处理复杂几何有困难。因此，混合方法将 FDTD 与 FVTD 或时域 FEM 结合。

When differential equation solvers are applied to problems in unbounded geometries, the computational region must be truncated. The preferred choice is the perfectly matched layer (PML).
> 当微分方程求解器应用于无界几何问题时，计算区域必须被截断。首选是完全匹配层（PML）。

For open-region problems with complicated materials, it can be useful to use FEM for the object and its surroundings, combined with MoM for the remaining free-space environment.
> 对于具有复杂材料的开放区域问题，可以对物体及其周围使用 FEM，结合 MoM 处理剩余的自由空间环境。

---

### Appendix A: Large Linear Systems | 大型线性系统

#### A.1 Sparse Matrices | 稀疏矩阵

Many CEM problems require the solution of large linear systems of equations. For realistic 3D applications, the number of unknowns can be in the range of tens of thousands to several millions.
> 许多 CEM 问题需要求解大型线性方程组。在实际的三维应用中，未知量数量可以从数万到数百万。

For the largest systems, direct inversion is seldom possible, and iterative methods are needed.
> 对于最大的系统，直接求逆很少可行，需要迭代方法。

#### A.2 Solvers for Large Sparse Systems of Equations | 大型稀疏方程组的求解器

**Direct Solvers | 直接求解器:** In direct methods, a complete factorization (e.g., LU decomposition) of the matrix $A$ is done. A major advantage is that additional right-hand sides can be solved with low additional cost.
> 在直接方法中，对矩阵 $A$ 进行完全分解（如 LU 分解）。一个主要优点是额外右端项可以以较低成本求解。

**Iterative Solvers | 迭代求解器:** For symmetric positive definite systems, Krylov methods generally work very well.
> 对于对称正定系统，Krylov 方法通常效果很好。

To speed up convergence, preconditioning is useful. A common choice is incomplete LU decomposition (ILU).
> 为加速收敛，预处理是有用的。一个常见选择是不完全 LU 分解（ILU）。

**Multigrid Methods | 多重网格法:** The multigrid (MG) method greatly improves convergence rate. The convergence rate can be made independent of the cell size $h$.
> 多重网格法（MG）极大地提高了收敛速度。收敛速度可以做到与单元尺寸 $h$ 无关。

#### A.3 Capacitance Calculation on Larger Grids | 大网格上的电容计算

With efficient solvers, we can extend the capacitance calculation to much larger grids, up to $400 \times 400$.
> 使用高效的求解器，我们可以将电容计算扩展到更大的网格，可达 $400 \times 400$。

---

### Appendix B: Krylov Methods | Krylov 方法

#### B.1 Projection Methods | 投影法

In projection methods, one minimizes the residual $\mathbf{r} = \mathbf{b} - A\mathbf{x}$ by constructing the solution as a sum of basis vectors.
> 在投影法中，通过将解构造为基向量的和来最小化残差。

#### B.2 Krylov Methods | Krylov 方法

A better strategy is to generate the increment directions as $\mathbf{r}_0, A\mathbf{r}_0, A^2\mathbf{r}_0, \ldots, A^{m-1}\mathbf{r}_0$, where $\mathbf{r}_0$ is the first residual. Then $K$ is called a Krylov space.
> 一种更好的策略是生成增量方向为 $\mathbf{r}_0, A\mathbf{r}_0, A^2\mathbf{r}_0, \ldots, A^{m-1}\mathbf{r}_0$，其中 $\mathbf{r}_0$ 为初始残差。$K$ 称为 Krylov 空间。

GMRES is Arnoldi's method followed by a minimization. The disadvantage is that one needs to store all incremental directions.
> GMRES 是 Arnoldi 方法加最小化。缺点是需要存储所有增量方向。

The conjugate gradient (CG) method for symmetric $A$ keeps going in orthogonal directions. For positive definite symmetric matrices, the required number of iterations for CG is proportional to the square root of the condition number.
> 对称 $A$ 的共轭梯度法（CG）在正交方向上进行。对于正定对称矩阵，CG 所需的迭代次数与条件数的平方根成正比。

#### B.3 Nonsymmetric A | 非对称矩阵

The symmetric Lanczos algorithm can be extended to nonsymmetric matrices using Lanczos biorthogonalization, which constructs a pair of biorthogonal bases.
> 对称 Lanczos 算法可以通过 Lanczos 双正交化扩展到非对称矩阵，该算法构造一对双正交基。
