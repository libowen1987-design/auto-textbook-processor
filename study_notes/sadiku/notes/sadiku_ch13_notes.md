# Sadiku《Elements of Electromagnetics》Chapter 13: Numerical Methods
> **中英双语版**

## 13.1 Introduction / 引言
Numerical methods are needed for practical EM problems with complex geometry.
> 实际复杂几何的电磁问题需要数值方法。

## 13.2 Finite Difference Method / 有限差分法
Approximate derivatives using finite differences on a grid.
> 在网格上使用有限差分近似导数。

**1D Poisson / 一维泊松方程：**
$$\frac{d^2V}{dx^2} \approx \frac{V_{i+1} - 2V_i + V_{i-1}}{h^2} = -\frac{\rho_{vi}}{\epsilon}$$

**2D Laplace / 二维拉普拉斯方程（五点差分）：**
$$V_{i,j} = \frac{1}{4}(V_{i+1,j} + V_{i-1,j} + V_{i,j+1} + V_{i,j-1})$$

**Iterative solutions / 迭代求解：**
- Jacobi: uses old values only
- Gauss-Seidel: uses updated values immediately / 立即使用更新值
- SOR (Successive Over-Relaxation / 超松弛): $\omega > 1$ accelerates convergence

## 13.3 Finite Element Method / 有限元法
Divide domain into elements, define basis functions, minimize energy functional.
> 将域划分为单元，定义基函数，最小化能量泛函。

**Weak form / 弱形式：**
$$\int_\Omega \epsilon \nabla W \cdot \nabla V \, d\Omega = \int_\Omega \rho_v W \, d\Omega + \oint_\Gamma \epsilon W \frac{\partial V}{\partial n} \, d\Gamma$$

**Galerkin's method / Galerkin 方法:** Use same functions for basis and testing.
> 基函数和测试函数相同。

## 13.4 Method of Moments (MoM) / 矩量法
Convert integral equations to matrix equations using basis functions and testing.
> 使用基函数和测试将积分方程转化为矩阵方程。

**EFIE / 电场积分方程:**
$$\hat{n} \times (j\omega\mu \int_S \mathbf{J}G\,dS' + \frac{1}{j\omega\epsilon}\nabla\int_S \nabla'\cdot\mathbf{J}\,G\,dS') = -\hat{n}\times\mathbf{E}^i$$

## 13.5 FDTD Method / 时域有限差分法
Yee algorithm: discretize Maxwell's curl equations on staggered grids.
> Yee 算法：在交错网格上离散化 Maxwell 旋度方程。

**Update equations / 更新方程:**
$$H_z|^{n+1/2}_{i+1/2,j+1/2} = H_z|^{n-1/2}_{i+1/2,j+1/2} + \frac{\Delta t}{\mu}\left(\frac{E_x|^n_{i+1/2,j+1} - E_x|^n_{i+1/2,j}}{\Delta y} - \frac{E_y|^n_{i+1,j+1/2} - E_y|^n_{i,j+1/2}}{\Delta x}\right)$$

**CFL stability condition / CFL 稳定性条件:**
$$\Delta t \leq \frac{1}{c\sqrt{1/\Delta x^2 + 1/\Delta y^2 + 1/\Delta z^2}}$$
