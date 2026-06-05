# Bondeson《Computational Electromagnetics》第2章
> **中英双语版**

> **Source:** Anders Bondeson, Thomas Rylander, Pär Ingelström, *Computational Electromagnetics*, Springer 2005  
> **PDF:** pages 29-35 of 231 (231 total)

---

## Convergence | 收敛性

### 2 Convergence

#### 2.1 Extrapolation to Zero Cell Size | 外推至零单元尺寸

We will use a very simple problem, namely to calculate the electrostatic potential on the symmetry axis of a uniformly charged square, to illustrate how computed results can be extrapolated to zero cell size.
> 我们将使用一个非常简单的问题——计算均匀带电正方形在其对称轴上的静电势——来说明如何将计算结果外推到零单元尺寸。

The square is the region $-a < x < a$, $-a < y < a$, $z = 0$, the surface charge density $\rho_s(x, y) = \rho_{s0}$ is constant, and we seek the potential $\varphi$ at two points on the symmetry axis: $(0, 0, a)$ and $(0, 0, 0)$.
> 正方形区域为 $-a < x < a$, $-a < y < a$, $z = 0$，面电荷密度 $\rho_s(x, y) = \rho_{s0}$ 为常数，我们求对称轴上两点 $(0, 0, a)$ 和 $(0, 0, 0)$ 的电位。

Using the symmetry, we can write the potential from this charge distribution as

$$\varphi(0, 0, z) = \frac{\rho_{s0}}{4\pi\epsilon_0} \int_{x'=-a}^{a} \int_{y'=-a}^{a} \frac{dx'\,dy'}{(x'^2 + y'^2 + z^2)^{1/2}} = \frac{\rho_{s0}}{\pi\epsilon_0} I(z, a),$$

with

$$I(z, a) \equiv \int_{x'=0}^{a} \int_{y'=0}^{a} \frac{dx'\,dy'}{(x'^2 + y'^2 + z^2)^{1/2}}. \tag{2.1}$$

> 利用对称性，可以将此电荷分布产生的电位写为上述形式。

To do the integral $I(z, a)$ numerically, we split the square into $n^2$ smaller squares of side $h = a/n$, and on each square, apply a simple integration rule such as midpoint integration

$$\int_x^{x+h} f(x)\,dx \approx h f\left(x + \frac{h}{2}\right) \tag{2.2}$$

> 为了数值计算积分 $I(z, a)$，我们将正方形分割为 $n^2$ 个边长为 $h = a/n$ 的小正方形，在每个小正方形上应用简单的积分规则，如中点积分 (2.2)

or Simpson's rule

$$\int_x^{x+h} f(x)\,dx \approx \frac{h}{6} \left[ f(x) + 4f\left(x + \frac{h}{2}\right) + f(x + h) \right] \tag{2.3}$$

> 或辛普森规则 (2.3)，在二维中应用。

in two dimensions. The integration can be written as a MATLAB function.
> 积分可以写成 MATLAB 函数。

We call this function with $z = a = 1$ [integr(1,1,n,rule)] and different numbers of grid points $n$ for rule = 'simpson' and 'midpoint', and then extrapolate the results to zero cell size to get as accurate an answer as possible.
> 我们以 $z = a = 1$ 调用此函数，使用不同的网格点数 $n$ 和不同的积分规则，然后将结果外推到零单元尺寸以获得尽可能精确的答案。

The first step is to establish the order of convergence.
> 第一步是建立收敛阶。

Table 2.1 shows some results of calling the function for different cell sizes $h = 1/n$.
> 表 2.1 显示了不同单元尺寸 $h = 1/n$ 下调用该函数的一些结果。

We can carry out the extrapolation using MATLAB routines, by collecting the values of $h$, $I_{\text{midp}}$, and $I_{\text{Simpson}}$ in vectors.
> 我们可以使用 MATLAB 例程进行外推，将 $h$, $I_{\text{midp}}$ 和 $I_{\text{Simpson}}$ 的值收集到向量中。

Plotting $I_{\text{midp}}$ versus $h$ to some power $p$, we find an almost straight line for $p = 2$, as shown in Figure 2.1.
> 将 $I_{\text{midp}}$ 对 $h$ 的某次幂 $p$ 作图，我们发现 $p = 2$ 时几乎为一条直线，如图 2.1 所示。

This indicates that the midpoint rule gives quadratic convergence, i.e., $I_{\text{midp}}(h) = I_0 + I_2 h^2 + \cdots$ where $I_0$ is the extrapolated result.
> 这表明中点规则具有二次收敛性，即 $I_{\text{midp}}(h) = I_0 + I_2 h^2 + \cdots$，其中 $I_0$ 是外推结果。

The term $I_2 h^2$ in the Taylor expansion of $I_{\text{midp}}$ is the dominant contribution to the error when $h$ is sufficiently small, and for such resolutions the higher-order terms in the Taylor expansion can be neglected.
> 当 $h$ 足够小时，$I_{\text{midp}}$ 泰勒展开中的 $I_2 h^2$ 项是误差的主要贡献，对于这样的分辨率，泰勒展开中的高阶项可以忽略。

**Table 2.1.** Integral $I(1, 1)$ from numerical integration with different cell sizes.
> **表 2.1.** 不同单元尺寸下数值积分的 $I(1, 1)$ 值。

| $n$ [-] | $h$ [m] | $I_{\text{midp}}(1, 1)$ [m] | $I_{\text{Simpson}}(1, 1)$ [m] |
|---------|---------|----------------------------|------------------------------|
| 5 | 0.20000 | 0.79432 30171 | 0.79335 94378 |
| 7 | 0.14286 | 0.79385 04952 | 0.79335 92042 |
| 10 | 0.10000 | 0.79359 97873 | 0.79335 91413 |
| 15 | 0.06667 | 0.79346 60584 | 0.79335 91252 |
| 20 | 0.05000 | 0.79341 92684 | 0.79335 91225 |

**Fig. 2.1.** Values of the integral $I(1, 1)$ computed by the midpoint rule, plotted versus $h^2$.
> **图 2.1.** 中点规则计算的积分 $I(1, 1)$ 值对 $h^2$ 的图。

We extrapolate the computed results as a polynomial fit in $h^2$ using the MATLAB command
> 我们使用 MATLAB 命令将计算结果作为 $h^2$ 的多项式拟合进行外推：

```
pfit = polyfit(h.^2, I, m)
```

Here, $m$ is the order of the polynomial, and the extrapolated value of the integral is the coefficient for $h^0$.
> 这里 $m$ 是多项式的阶数，积分的外推值是 $h^0$ 的系数。

A first-order fit ($m = 1$) gives the extrapolation $I(1, 1) \simeq 0.79335\,88818$, second-order ($m = 2$) gives $0.79335\,91208$, and a third-order fit gives $0.79335\,91213$.
> 一阶拟合得到 $I(1, 1) \simeq 0.79335\,88818$，二阶拟合得到 $0.79335\,91208$，三阶拟合得到 $0.79335\,91213$。

The results from the Simpson integration fall on an almost straight line when plotted against $h^4$, and we conclude that the dominant error scales as $h^4$.
> 辛普森积分的结果对 $h^4$ 作图时几乎为一条直线，我们得出结论：主要误差按 $h^4$ 变化。

A fit of $I_{\text{Simpson}}(1, 1)$ to a linear polynomial in $h^4$ gives the extrapolation $0.79335\,91207$, and quadratic and cubic fits give $0.79335\,91202$.
> 将 $I_{\text{Simpson}}(1, 1)$ 拟合为 $h^4$ 的线性多项式得到外推值 $0.79335\,91207$，二次和三次拟合得到 $0.79335\,91202$。

The correct answer to eight digits is $0.79335\,912$.
> 精确到八位的正确答案是 $0.79335\,912$。

Extrapolation allows us to establish this degree of accuracy with a rather moderate effort: a second-order fit of the low-order midpoint rule versus $h^2$, using data computed for rather coarse grids $h \geq 0.05$.
> 外推使我们能够以相当适中的工作量达到这一精度：使用相当粗糙的网格 $h \geq 0.05$ 计算的数据，对低阶中点规则进行二阶 $h^2$ 拟合。

This gives eight-digit accuracy of the extrapolation even though the computed data has only three to four correct digits.
> 即使计算数据只有三到四位有效数字，外推也能达到八位精度。

Thus, extrapolation can bring very significant improvements of accuracy.
> 因此，外推可以带来非常显著的精度提升。

Another advantage of extrapolation is that it makes us aware of how good the accuracy is.
> 外推的另一个优点是它让我们意识到精度有多好。

The example shows that good accuracy can also be obtained by using the higher-order Simpson integration, even without extrapolation, on a grid of moderate size.
> 该示例表明，即使在中等大小的网格上，不使用外推，使用高阶辛普森积分也可以获得良好的精度。

A simple way to estimate the order of convergence is to carry out computations for a geometric sequence of cell sizes such that $h_i/h_{i+1} = h_{i+1}/h_{i+2}$.
> 一种估计收敛阶的简单方法是对几何序列的单元尺寸 $h_i/h_{i+1} = h_{i+1}/h_{i+2}$ 进行计算。

Assuming that the lowest-order term in the expansion of the error is sufficient, i.e. $I(h) = I_0 + I_p h^p$, and that the cell sizes form a geometric series, one can then estimate the order of convergence as

$$p = \frac{\ln\left(\frac{I(h_i) - I(h_{i+1})}{I(h_{i+1}) - I(h_{i+2})}\right)}{\ln\left(\frac{h_i}{h_{i+1}}\right)} \tag{2.4}$$

> 假设误差展开中的最低阶项足够（即 $I(h) = I_0 + I_p h^p$），且单元尺寸构成几何级数，则可按 (2.4) 估计收敛阶。

When applied to the computed results for $h = 0.2$, $0.1$ and $0.05$, this formula gives $p = 2.002$ for the midpoint rule and $p = 3.985$ for Simpson, indicating that the convergence is quadratic and quartic, respectively, for the two methods.
> 将该公式应用于 $h = 0.2$, $0.1$ 和 $0.05$ 的计算结果，中点规则得到 $p = 2.002$，辛普森规则得到 $p = 3.985$，表明两种方法分别具有二次和四次收敛性。

---

##### 2.1.1 A Singular Problem | 奇异问题

It is instructive to consider a more singular problem, such as the potential on the midpoint of the plate, $z = 0$.
> 考虑一个更奇异的问题是有启发性的，比如板中点 $z = 0$ 处的电位。

Now, the integrand is singular, but the integral is nevertheless convergent.
> 现在被积函数是奇异的，但积分仍然是收敛的。

For this problem, Simpson integration gives a divergent result and cannot be used. (This illustrates the fact that high-order methods often experience difficulties in the presence of singularities.)
> 对于这个问题，辛普森积分给出发散的结果，不能使用。（这说明了高阶方法在奇异性存在时经常遇到困难的事实。）

However, the midpoint integration still works, and for the cell sizes above we find the following values for $I_{\text{midp}}(0, 1)$: 1.684320, 1.706250, 1.722947, 1.736083, 1.742700.
> 然而，中点积分仍然有效，对于上述单元尺寸，我们得到 $I_{\text{midp}}(0, 1)$ 的值如下：1.684320, 1.706250, 1.722947, 1.736083, 1.742700。

Plots of $I_{\text{midp}}$ versus $h^p$ reveal that the order of convergence is now lower, $p = 1$.
> 将 $I_{\text{midp}}$ 对 $h^p$ 作图发现收敛阶现在较低，$p = 1$。

Nevertheless, we can still extrapolate using fits to polynomials in $h$.
> 尽管如此，我们仍然可以使用 $h$ 的多项式拟合进行外推。

The results are linear, 1.762015; quadratic, 1.762745; cubic, 1.762748.
> 结果：线性拟合 1.762015；二次拟合 1.762745；三次拟合 1.762748。

This integral can be done analytically: $I(0, 1) = 2\ln(1 + \sqrt{2}) \approx 1.762747$.
> 这个积分可以解析计算：$I(0, 1) = 2\ln(1 + \sqrt{2}) \approx 1.762747$。

Thus, despite the singularity, the midpoint rule gives six-figure accuracy with $h \geq 0.05$ and quadratic extrapolation.
> 因此，尽管存在奇异性，中点规则在 $h \geq 0.05$ 和二次外推下仍能达到六位精度。

**Review Questions | 复习问题**

2.1-1 What is meant by resolution in the context of numerical computations? Give some examples.
> 在数值计算中，分辨率意味着什么？举几个例子。

2.1-2 How can the error in a computation be estimated?
> 如何估计计算中的误差？

2.1-3 What influences the error and the order of convergence?
> 什么因素影响误差和收敛阶？

2.1-4 Give a couple of examples of numerical integration rules and provide a simple comparison. Especially consider the differences for smooth and singular integrands.
> 给出几个数值积分规则的例子并进行简单比较，特别考虑光滑和奇异被积函数的差异。

---

#### 2.2 Practical Procedures | 实用步骤

The example we have just studied is very simple.
> 我们刚刚研究的例子非常简单。

Real application problems have more complex geometry than a square, but on the other hand, six-digit accuracy is very rarely needed, or even possible to achieve.
> 实际应用问题的几何形状比正方形更复杂，但另一方面，六位精度很少需要，甚至很少可能达到。

Furthermore, numerical results converge in the very regular way we found here only if the grid can be refined uniformly over the whole computational region.
> 此外，只有当网格可以在整个计算区域均匀细化时，数值结果才会像我们这里发现的那样以非常规则的方式收敛。

When this is not possible, the convergence may be oscillatory, and the extrapolation to zero cell size becomes more difficult.
> 当这不可能时，收敛可能具有振荡性，外推到零单元尺寸变得更加困难。

In practice, it is often possible to extract a main power of convergence with the number of grid cells, but the remainder is too oscillatory to be convincingly fit by higher-order polynomials.
> 在实践中，通常可以提取网格单元数的主要收敛幂次，但剩余部分振荡性太强，无法用高阶多项式令人信服地拟合。

A more robust and practical procedure for such cases is to use a linear fit of the computed results to $h^p$, where $p$ is the estimated order of convergence.
> 对于这种情况，一种更稳健、更实用的方法是将计算结果对 $h^p$ 进行线性拟合，其中 $p$ 是估计的收敛阶。

When the converged answer is not known, but the convergence is sufficiently regular, the order of convergence can be estimated from results for three different resolutions.
> 当收敛答案未知但收敛足够规则时，可以从三个不同分辨率的结果估计收敛阶。

To ascertain that the estimated order of convergence is not accidental, at least four different resolutions should be used.
> 为确保估计的收敛阶不是偶然的，应至少使用四种不同的分辨率。

Once the order of convergence is established, extrapolation to zero cell size can be made by fitting a lowest-order expansion

$$I(h) = I_0 + I_p h^p \tag{2.5}$$

to the computed results.
> 一旦确定了收敛阶，可以通过将最低阶展开 (2.5) 拟合到计算结果来进行外推。

**Review Question | 复习问题**

2.2-1 Why can extrapolation to zero cell size be difficult for nonuniformly refined grids?
> 为什么对于非均匀细化的网格，外推到零单元尺寸是困难的？

---

#### Summary | 小结

- The accuracy of a numerical result depends on resolution.
> 数值结果的精度取决于分辨率。

- For example, a domain of integration can be divided into segments of size $h$, and a numerical evaluation of the integral $I$ is then expressed as $I(h) = I_0 + I_p h^p + \cdots$, where $I_0$ is the exact result, $I_p h^p$ is the dominant error term (provided that $h$ is sufficiently small), and $p$ is the order of convergence.
> 例如，积分域可以分割为尺寸 $h$ 的段，积分 $I$ 的数值评估表示为 $I(h) = I_0 + I_p h^p + \cdots$，其中 $I_0$ 为精确结果，$I_p h^p$ 为主要误差项（$h$ 足够小时），$p$ 为收敛阶。

- The order of convergence $p$ can be estimated from
> 收敛阶 $p$ 可由下式估计：

$$p = \frac{\ln\left(\frac{I(h_i) - I(h_{i+1})}{I(h_{i+1}) - I(h_{i+2})}\right)}{\ln\left(\frac{h_i}{h_{i+1}}\right)}$$

which requires at least three computations and where $h_i/h_{i+1} = h_{i+1}/h_{i+2}$.
> 这需要至少三次计算，且 $h_i/h_{i+1} = h_{i+1}/h_{i+2}$。

- The result should preferably be verified for at least four resolutions to ascertain that the estimated $p$ is not accidental.
> 结果最好在至少四种分辨率下验证，以确保估计的 $p$ 不是偶然的。

- A simple method to estimate the error of a given computation is to (i) do a convergence test by uniform grid refinement, (ii) find the order of convergence, and (iii) extrapolate the computed results to zero cell size.
> 一种估计给定计算误差的简单方法是：(i) 通过均匀网格细化进行收敛性测试，(ii) 找出收敛阶，(iii) 将计算结果外推到零单元尺寸。

- The order of convergence depends on the method and the regularity of the solution. Singular behavior of the solution decreases the order of convergence $p$ in many real-world problems.
> 收敛阶取决于方法和解的正则性。在许多实际问题中，解的奇异性会降低收敛阶 $p$。

---

#### Problems | 习题

P.2-1 Derive the order of convergence for midpoint integration (2.2) and Simpson's rule (2.3) under the assumption that the integrand is regular. How does a singular integrand influence your derivation?
> 假设被积函数是规则的，推导中点积分 (2.2) 和辛普森规则 (2.3) 的收敛阶。奇异被积函数如何影响你的推导？

P.2-2 Show that (2.4) gives an estimate for $p$. Under what conditions is this estimate accurate?
> 证明 (2.4) 给出了 $p$ 的估计。在什么条件下该估计是准确的？

#### Computer Projects | 计算机项目

C.2-1 Repeat the calculations of $I(1, 1)$ and $I(0, 1)$, where $I(z, a)$ is defined in (2.1), using two-point Gaussian integration

$$\int_x^{x+h} f(x)\,dx = \frac{h}{2}\left[ f\left(x + \frac{h}{2}\left(1 - \frac{1}{\sqrt{3}}\right)\right) + f\left(x + \frac{h}{2}\left(1 + \frac{1}{\sqrt{3}}\right)\right) \right]$$

and find the order of convergence.
> 使用两点高斯积分重复 $I(1, 1)$ 和 $I(0, 1)$ 的计算，并找出收敛阶。

C.2-2 Calculate the integral $\int_0^1 x^{-\alpha}\,dx$, with a singular integrand, numerically by dividing the interval into equal elements and applying midpoint integration on each. Investigate the cases $\alpha = 0.5$ and $0.8$, find the order of convergence, and extrapolate to zero cell size. The exact integral is $1/(1-\alpha)$.
> 数值计算具有奇异被积函数的积分 $\int_0^1 x^{-\alpha}\,dx$，将区间等分并在每个单元应用中点积分。研究 $\alpha = 0.5$ 和 $0.8$ 的情况，找出收敛阶，并外推到零单元尺寸。

---

### Finite Differences | 有限差分

Maxwell's equations are usually formulated as differential equations.
> Maxwell 方程组通常表示为微分方程的形式。

Therefore, it is quite natural to solve them by finite difference methods, where the derivatives are approximated by differences between neighboring points on a grid.
> 因此，很自然地使用有限差分法来求解它们，其中导数由网格上相邻点之间的差分来近似。

In a one-dimensional (1D) problem on the $x$-axis, a finite difference method introduces a set of grid points $x_1, x_2, \ldots, x_N$ where a sought function $f(x)$ takes the values $f(x_1), f(x_2), \ldots, f(x_N)$.
> 在 $x$ 轴上的一维问题中，有限差分法引入一组网格点 $x_1, x_2, \ldots, x_N$，待求函数 $f(x)$ 在这些点上的值为 $f(x_1), f(x_2), \ldots, f(x_N)$。

We will first recapitulate expressions for first- and second-order differences on a uniform grid with grid points $x_{n+i} = x_n + ih$, where $i$ is an integer and $h$ is the distance between the grid points (often referred to as cell size).
> 我们首先回顾均匀网格上一阶和二阶差分的表达式，网格点为 $x_{n+i} = x_n + ih$，其中 $i$ 为整数，$h$ 为网格点间距（常称为单元尺寸）。

The basis for this is the Taylor expansion

$$f(x + \delta) = f(x) + \delta f'(x) + \frac{\delta^2}{2} f''(x) + \frac{\delta^3}{6} f'''(x) + \cdots \tag{3.1}$$

> 其基础是泰勒展开 (3.1)。

To get the first derivative on a grid point $x$, we could use the noncentered difference $[f(x + h) - f(x)]/h = f'(x) + \mathcal{O}(h)$, but the error here is of first order in $h$.
> 为在网格点 $x$ 上获得一阶导数，可以使用非中心差分 $[f(x + h) - f(x)]/h = f'(x) + \mathcal{O}(h)$，但这里的误差是 $h$ 的一阶。

One way to increase the order of approximation is to take the difference across two cells, which gives

$$\frac{f(x + h) - f(x - h)}{2h} = f'(x) + \mathcal{O}(h^2). \tag{3.2}$$

> 提高近似阶数的一种方法是跨两个单元取差分，得到 (3.2)。

As we shall see shortly, this becomes very inaccurate for short wavelengths, in particular, when the wavelength is less than four grid cells.
> 我们很快就会看到，这对于短波长变得非常不准确，特别是当波长小于四个网格单元时。

A better alternative is to use "staggered grids" and compute the first-order derivative on the "half-grid" $x_{i+\frac{1}{2}} = x_i + h/2$:

$$\frac{f(x + h) - f(x)}{h} = f'\left(x + \frac{h}{2}\right) + \mathcal{O}(h^2). \tag{3.3}$$

> 更好的选择是使用"交错网格"并在"半网格"点 $x_{i+\frac{1}{2}}$ 上计算一阶导数，如 (3.3) 所示。

A difference formula for the second derivative on an equidistant grid can be developed by applying (3.3) repeatedly, which gives

$$f''(x) \approx \frac{f(x + h) - 2f(x) + f(x - h)}{h^2} = f''(x) + \mathcal{O}(h^2). \tag{3.4}$$

> 通过重复应用 (3.3) 可以推导出等距网格上二阶导数的差分公式，得到 (3.4)。
