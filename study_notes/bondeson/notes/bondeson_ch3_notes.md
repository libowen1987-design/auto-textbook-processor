# Bondeson《Computational Electromagnetics》第3章：有限差分法
> **中英双语版**

> **Source:** Anders Bondeson, Thomas Rylander, Pär Ingelström, *Computational Electromagnetics*, Springer 2005  
> **章节来源:** Chapter 3: Finite Differences, pp.36-52  
> **提取方式:** ✅ 清晰文本PDF直接提取

---

## 3 有限差分法 | Finite Differences

### 3.1 有限差分近似 | Finite Difference Approximations

有限差分法的核心是用**差商**近似**导数**。

#### 3.1.1 一阶导数 | First Derivative

**前向差分（Forward difference）：**
$$\frac{f(x+h) - f(x)}{h} = f'(x) + \mathcal{O}(h) \tag{3.2}$$

**后向差分（Backward difference）：**
$$\frac{f(x) - f(x-h)}{h} = f'(x) + \mathcal{O}(h) \tag{3.3}$$

**中心差分（Central difference）：**
$$\frac{f(x+h) - f(x-h)}{2h} = f'(x) + \mathcal{O}(h^2) \tag{3.2}$$

> **物理直觉：** 中心差分的误差是 $\mathcal{O}(h^2)$，比前向/后向差分的 $\mathcal{O}(h)$ 高一阶。这意味着步长减半，中心差分误差约减小到1/4。

#### 3.1.2 二阶导数 | Second Derivative

$$f''(x) \approx \frac{f(x+h) - 2f(x) + f(x-h)}{h^2} = f''(x) + \mathcal{O}(h^2) \tag{3.4}$$

> **误差阶（Order of accuracy）：** $\mathcal{O}(h^2)$ 表示当 $h \to 0$ 时，误差以 $h^2$ 速度趋于零。

---

### 3.2 二维电容问题 | A 2D Capacitance Problem

#### 3.2.1 问题描述 | Problem Statement

计算**同轴矩形传输线**的电容（每单位长度）。

**几何结构：**
- 内导体：矩形截面 $a \times b$，电位 $\phi_1 = 1\,\text{V}$
- 外导体：矩形截面 $c \times d$，电位 $\phi_2 = 0\,\text{V}$

**真空区域的电位** $\phi(x,y)$ 满足 **Laplace 方程**：

$$\nabla^2 \phi = \frac{\partial^2 \phi}{\partial x^2} + \frac{\partial^2 \phi}{\partial y^2} = 0 \tag{3.5}$$

#### 3.2.2 离散化 | Discretization

采用**正方形网格**（grid spacing $= h$）：

$$x_i = i\\cdot h, \quad y_j = j\\cdot h$$

网格点上的电位近似值：

$$f_{i,j} \approx \phi(i\\cdot h, j\\cdot h)$$

离散 Laplace 方程（代入中心差分近似）：

$$\frac{f_{i+1,j} - 2f_{i,j} + f_{i-1,j}}{h^2} + \frac{f_{i,j+1} - 2f_{i,j} + f_{i,j-1}}{h^2} = 0$$

化简得 **五点差分格式（Five-point stencil）**：

$$f_{i,j} = \frac{1}{4}\\left(f_{i-1,j} + f_{i+1,j} + f_{i,j-1} + f_{i,j+1}\\right) \tag{3.6}$$

> **物理意义：** 每个网格点上的电位 = 四个邻居电位的算术平均。这对应于 Laplace 方程的物理性质——电位在二维场中光滑分布。

**边界条件：**
- 内导体：$f_{i,j} = 1$（电位 $\phi_1 = 1\,\text{V}$）
- 外导体：$f_{i,j} = 0$（电位 $\phi_2 = 0\,\text{V}$）

**电容计算：**
$$Q = \oint \varepsilon_0 \frac{\partial \phi}{\partial n}\\, dl, \quad C = \frac{Q}{V} = Q \quad (V = 1\,\text{V})$$

---

### 3.3 迭代求解 | Iterative Solution Methods

#### 3.3.1 Jacobi 迭代 | Jacobi Iteration

将差分方程 (3.6) 重写为迭代格式：

$$f^{(n+1)}_{i,j} = \frac{1}{4}\\left(f^{(n)}_{i-1,j} + f^{(n)}_{i+1,j} + f^{(n)}_{i,j-1} + f^{(n)}_{i,j+1}\\right) \tag{Jacobi}$$

> **算法：** 每次迭代用上一轮所有邻居的值计算新值。

**收敛性：** Jacobi 方法**收敛慢**，但简单稳定。

#### 3.3.2 Gauss-Seidel 迭代 | Gauss-Seidel Iteration

改进：用**已更新的邻居值**立即覆盖旧值（扫描顺序：i, j 递增）：

$$f^{(n+1)}_{i,j} = \frac{1}{4}\\left(f^{(n+1)}_{i-1,j} + f^{(n)}_{i+1,j} + f^{(n+1)}_{i,j-1} + f^{(n)}_{i,j+1}\\right) \tag{GS}$$

> **优势：** 收敛速度约为 Jacobi 的两倍，因为信息沿扫描方向立即传播。

#### 3.3.3 超松弛（SOR）| Successive Over-Relaxation (SOR)

引入松弛因子 $\omega$ 加速收敛：

$$f^{(n+1)}_{i,j} = f^{(n)}_{i,j} + $\omega$\\left[\frac{1}{4}\\left(f^{(n+1)}_{i-1,j} + f^{(n)}_{i+1,j} + f^{(n+1)}_{i,j-1} + f^{(n)}_{i,j+1}\\right) - f^{(n)}_{i,j}\\right] \tag{SOR}$$

**最优松弛因子（最佳值）：**
$$\omega_{opt} = \frac{2}{1 + \sqrt{1 - $\rho$(J)^2}}$$

其中 $$\rho$(J)$ 是 Jacobi 迭代矩阵的谱半径。

> **注意：** $\omega > 1$ 为**超松弛**（加速），$\omega < 1$ 为**欠松弛**（稳定）。

---

### 3.4 有限差分的误差与收敛 | Error and Convergence

#### 3.4.1 离散误差 | Discretization Error

网格加密（$h \to h/2$），$\mathcal{O}(h^2)$ 方法的误差约减至 1/4。

| 网格尺寸 $h$ | 中心差分误差 $\mathcal{O}(h^2)$ |
|-------------|---------------------------|
| 0.1 | ~0.01 |
| 0.05 | ~0.0025 |
| 0.025 | ~0.0006 |

#### 3.4.2 迭代收敛判定 | Convergence Criteria

$$\max_{i,j}\\left|f^{(n+1)}_{i,j} - f^{(n)}_{i,j}\\right| < \varepsilon_{tol}$$

典型容差：$\varepsilon_{tol} = 10^{-6}$

---

### 3.5 本章要点 | Key Takeaways

1. **中心差分**：$\mathcal{O}(h^2)$ 精度，比前向/后向差分高一阶
2. **五点差分格式**：$f_{i,j} = \frac{1}{4}(f_{i-1,j} + f_{i+1,j} + f_{i,j-1} + f_{i,j+1})$ — Laplace 方程的离散核心
3. **迭代方法比较**：Jacobi（稳定但慢）→ Gauss-Seidel（2倍速）→ SOR（最优 $\omega$ 可达 10 倍速）
4. **收敛判定**：残差最大值 $< \varepsilon_{tol}$

---

### 3.6 数值实现要点 | Numerical Implementation Notes

```python
# Gauss-Seidel 迭代（Python伪代码）
for iteration in range(max_iterations):
    max_diff = 0.0
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            if is_interior(i, j):  # 非边界点
                f_new = 0.25 * (f[i-1,j] + f[i+1,j] + f[i,j-1] + f[i,j+1])
                max_diff = max(max_diff, abs(f_new - f[i,j]))
                f[i,j] = f_new
    if max_diff < tol:
        break
```