# Bondeson《Computational Electromagnetics》第7章
> **中英双语版**

> **Source:** Anders Bondeson, Thomas Rylander, Pär Ingelström, *Computational Electromagnetics*, Springer 2005  
> **PDF:** pages 167-203 of 231 (231 total)

---

## The Method of Moments | 矩量法

### 7 The Method of Moments

The Method of Moments (MoM) discretizes Maxwell's equations in integral form.
> 矩量法（MoM）对积分形式的 Maxwell 方程组进行离散化。

The unknowns are sources such as currents or charges on the surfaces of conductors and dielectrics.
> 未知量是导体和介质表面的电流或电荷等源量。

This method is advantageous for problems involving open regions.
> 该方法适用于涉及开放区域的问题。

As an alternative to solving Laplace's equation for the potential in the vacuum region, we can calculate the charges $\rho_s$ on the conducting walls $S$ by solving the integral equation:

$$\int_{S'} \frac{\rho_s(\mathbf{r}')}{4\pi\epsilon_0 |\mathbf{r} - \mathbf{r}'|} dS' = \varphi_{\text{spec}}(\mathbf{r}). \tag{7.3}$$

> 作为求解真空区域中电位的拉普拉斯方程的替代方案，我们可以通过求解积分方程 (7.3) 来计算导体壁 $S$ 上的电荷 $\rho_s$。

In the 2D capacitor problem, the surface integral reduces to a line integral, using the potential from a line charge:
> 在二维电容问题中，面积分简化为线积分，使用线电荷产生的电位：

$$-\frac{1}{2\pi\epsilon_0} \int_{L'} \rho_l(\mathbf{r}') \ln |\mathbf{r} - \mathbf{r}'| \, dl' = \varphi_{\text{spec}}(\mathbf{r}). \tag{7.4}$$

A characteristic property of the integral formulation is that it deals readily with open geometries.
> 积分公式的一个特性是它易于处理开放几何形状。

---

#### 7.1 Integral Formulation of Electrostatics | 静电学积分公式

##### 7.1.1 Green's Function | Green 函数

A Green's function $G(\mathbf{r}, \mathbf{r}')$ represents the "field" at $\mathbf{r}$ produced by a point source at $\mathbf{r}'$.
> Green 函数 $G(\mathbf{r}, \mathbf{r}')$ 表示 $\mathbf{r}'$ 处点源在 $\mathbf{r}$ 处产生的"场"。

In electrostatics, the Green's function represents the electric potential at $\mathbf{r}$ produced by a unit charge at $\mathbf{r}'$:
> 在静电学中，Green 函数表示 $\mathbf{r}'$ 处单位电荷在 $\mathbf{r}$ 处产生的电位：

$$G(\mathbf{r}, \mathbf{r}') = \frac{1}{4\pi\epsilon_0 |\mathbf{r} - \mathbf{r}'|}. \tag{7.5}$$

The potential from a point charge satisfies Poisson's equation:
> 点电荷产生的电位满足泊松方程：

$$-\epsilon_0 \nabla_r^2 \varphi(\mathbf{r}) = \delta^3(\mathbf{r} - \mathbf{r}'). \tag{7.6}$$

The solution $\varphi(\mathbf{r})$ to (7.6) is the Green's function $G(\mathbf{r}, \mathbf{r}')$.
> (7.6) 的解 $\varphi(\mathbf{r})$ 即为 Green 函数 $G(\mathbf{r}, \mathbf{r}')$。

$$-\epsilon_0 \nabla_r^2 G(\mathbf{r}, \mathbf{r}') = \delta^3(\mathbf{r} - \mathbf{r}'). \tag{7.7}$$

The Green's function depends only on the distance $R = |\mathbf{r} - \mathbf{r}'|$ between the source and observation point.
> Green 函数仅依赖于源点和观测点之间的距离 $R = |\mathbf{r} - \mathbf{r}'|$。

Except at $R = 0$, $G$ satisfies:
> 除 $R=0$ 外，$G$ 满足：

$$\frac{1}{R^2} \frac{d}{dR} \left(R^2 \frac{dG}{dR}\right) = 0, \quad R > 0. \tag{7.8}$$

##### 7.1.2 Boundary Integral Equation | 边界积分方程

Using Green's second identity:
> 使用 Green 第二恒等式：

$$\int_\Omega (\varphi \nabla^2 \psi - \psi \nabla^2 \varphi) \, dV = \oint_{\partial\Omega} (\varphi \nabla \psi - \psi \nabla \varphi) \cdot \hat{n} \, dS, \tag{7.12}$$

and choosing $\psi = G$, we can reformulate the differential equation as a boundary integral equation.
> 并选择 $\psi = G$，我们可以将微分方程重新表述为边界积分方程。

For the electrostatic potential $\varphi$ satisfying $\nabla^2 \varphi = 0$ in $\Omega$, we obtain:
> 对于在 $\Omega$ 中满足 $\nabla^2 \varphi = 0$ 的静电势 $\varphi$，得到：

$$\alpha(\mathbf{r}) \varphi(\mathbf{r}) = \oint_{\partial\Omega} \left[ G(\mathbf{r}, \mathbf{r}') \frac{\partial \varphi(\mathbf{r}')}{\partial n'} - \varphi(\mathbf{r}') \frac{\partial G(\mathbf{r}, \mathbf{r}')}{\partial n'} \right] dS', \tag{7.13}$$

where $\alpha(\mathbf{r})$ is the interior angle at $\mathbf{r}$ divided by $4\pi$.
> 其中 $\alpha(\mathbf{r})$ 是 $\mathbf{r}$ 处的内角除以 $4\pi$。

---

#### 7.2 The Method of Moments | 矩量法

The MoM transforms the integral equation into a matrix equation by expanding the unknown function in basis functions and testing with weighting functions.
> MoM 通过将未知函数展开为基函数并用权函数测试，将积分方程转化为矩阵方程。

**General procedure / 一般步骤：**

1. Expand the unknown $f$ in basis functions $\{f_n\}$:
   > 将未知函数 $f$ 展开为基函数 $\{f_n\}$：
   $$f(\mathbf{r}') = \sum_{n=1}^N \alpha_n f_n(\mathbf{r}')$$

2. Substitute into the integral equation $L[f] = g$
   > 代入积分方程 $L[f] = g$

3. Test with weighting functions $\{w_m\}$ (Galerkin's method if $w_m = f_m$):
   > 用权函数 $\{w_m\}$ 测试（若 $w_m = f_m$ 则为 Galerkin 方法）：
   $$\sum_{n=1}^N \alpha_n \langle w_m, L[f_n] \rangle = \langle w_m, g \rangle$$

4. This gives a matrix equation: $A\boldsymbol{\alpha} = \mathbf{b}$, where $A_{mn} = \langle w_m, L[f_n] \rangle$
   > 得到矩阵方程

##### 7.2.1 Basis Functions | 基函数

Common choices for basis functions:
> 基函数的常见选择：

- **Pulse functions:** $f_n(x) = 1$ on segment $n$, 0 elsewhere. Simple but discontinuous.
> **脉冲函数：** 在段 $n$ 上 $f_n(x) = 1$，其他处为 0。简单但不连续。

- **Rooftop (triangle) functions:** Piecewise linear, continuous. Better accuracy.
> **屋顶（三角）函数：** 分段线性连续。精度更好。

- **Rao-Wilton-Glisson (RWG) functions:** For 3D surface MoM on triangular meshes.
> **Rao-Wilton-Glisson (RWG) 函数：** 用于三角形网格上的三维曲面 MoM。

##### 7.2.2 Testing Methods | 测试方法

- **Point matching (collocation):** $w_m(\mathbf{r}) = \delta(\mathbf{r} - \mathbf{r}_m)$. Simplest.
> **点匹配（配置法）：** 最简单的 $w_m(\mathbf{r}) = \delta(\mathbf{r} - \mathbf{r}_m)$。

- **Galerkin's method:** $w_m = f_m$. More accurate and symmetric matrix.
> **Galerkin 方法：** $w_m = f_m$。更精确且矩阵对称。

- **Method of weighted residuals:** General $w_m$.
> **加权残量法：** 一般的 $w_m$。

##### 7.2.3 Electrostatic Example: Charged Wire | 静电学示例：带电导线

Consider a thin wire of length $L$ and radius $a$ ($a \ll L$) held at potential $V_0$.
> 考虑长度为 $L$、半径为 $a$（$a \ll L$）、电位为 $V_0$ 的细导线。

The integral equation for the charge density $\rho_l(z)$ is:
> 电荷密度 $\rho_l(z)$ 的积分方程为：

$$\frac{1}{4\pi\epsilon_0} \int_0^L \frac{\rho_l(z')}{\sqrt{(z - z')^2 + a^2}} dz' = V_0, \quad 0 < z < L. \tag{7.22}$$

Discretizing with pulse basis functions and point matching gives a matrix system.
> 使用脉冲基函数和点匹配离散化得到矩阵系统。

---

#### 7.3 The Electric Field Integral Equation (EFIE) | 电场积分方程

For time-harmonic electromagnetic scattering from a PEC object, the scattered field is:
> 对于 PEC 物体的时谐电磁散射，散射场为：

$$\mathbf{E}^s(\mathbf{r}) = -j\omega \mu \int_{S'} \mathbf{J}(\mathbf{r}') G(\mathbf{r}, \mathbf{r}') \, dS' + \frac{1}{j\omega\epsilon} \nabla \int_{S'} \nabla' \cdot \mathbf{J}(\mathbf{r}') G(\mathbf{r}, \mathbf{r}') \, dS', \tag{7.39}$$

where the 3D Green's function for the Helmholtz equation is:
> 其中亥姆霍兹方程的三维 Green 函数为：

$$G(\mathbf{r}, \mathbf{r}') = \frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{4\pi |\mathbf{r} - \mathbf{r}'|}. \tag{7.40}$$

> 注意这是频域形式，$k = \omega\sqrt{\mu\epsilon}$。

On the surface of a PEC, the total tangential electric field vanishes:
> 在 PEC 表面上，总切向电场为零：

$$\hat{n} \times (\mathbf{E}^i + \mathbf{E}^s) = 0. \tag{7.41}$$

This gives the EFIE:
> 这给出 EFIE：

$$-\hat{n} \times \mathbf{E}^i(\mathbf{r}) = \hat{n} \times \left[ j\omega\mu \int_{S'} \mathbf{J}(\mathbf{r}') G \, dS' - \frac{1}{j\omega\epsilon} \nabla \int_{S'} \nabla' \cdot \mathbf{J}(\mathbf{r}') G \, dS' \right], \quad \mathbf{r} \in S. \tag{7.42}$$

> 这就是电场积分方程 (EFIE)。

---

#### 7.4 Magnetic Field Integral Equation (MFIE) | 磁场积分方程

The MFIE is derived from the magnetic field integral:
> MFIE 从磁场积分推导：

$$\frac{1}{2} \mathbf{J}(\mathbf{r}) = \hat{n} \times \mathbf{H}^i(\mathbf{r}) + \hat{n} \times \int_{S'} \mathbf{J}(\mathbf{r}') \times \nabla' G \, dS'. \tag{7.49}$$

> MFIE 主要适用于闭合 PEC 表面。

For open surfaces, the EFIE must be used.
> 对于开放表面，必须使用 EFIE。

---

#### 7.5 Combined Field Integral Equation (CFIE) | 组合场积分方程

The CFIE is a linear combination of the EFIE and MFIE:
> CFIE 是 EFIE 和 MFIE 的线性组合：

$$\text{CFIE} = \alpha \, \text{EFIE} + (1-\alpha) \, \text{MFIE}, \quad 0 \leq \alpha \leq 1. \tag{7.55}$$

> CFIE 通过在 EFIE 和 MFIE 之间插值，避免了内部谐振问题。

The CFIE avoids internal resonance problems that plague both the EFIE and MFIE at certain frequencies.
> CFIE 避免了 EFIE 和 MFIE 在某些频率上出现的内部谐振问题。

---

#### 7.6 MoM Summary | MoM 总结

**Advantages / 优势：**
- Fewer unknowns than volume methods / 未知量比体方法少
- Naturally handles open regions / 自然处理开放区域
- High accuracy for smooth surfaces / 对光滑表面精度高

**Disadvantages / 缺点：**
- Dense matrix ($O(N^2)$ storage) / 稠密矩阵
- Green's function must be known / 必须已知 Green 函数
- Difficult for inhomogeneous materials / 对非均匀材料困难
- Internal resonance issues (EFIE/MFIE) / 内部谐振问题

**Review Questions / 复习问题：**

7.1-1 What is a Green's function? Derive the Green's function for 3D electrostatics.
> 什么是 Green 函数？推导三维静电学的 Green 函数。

7.2-1 Describe the general procedure for the Method of Moments.
> 描述矩量法的一般步骤。

7.2-2 Write a short MATLAB program that solves the charged wire problem using pulse bases and point matching.
> 编写一个简短的 MATLAB 程序，使用脉冲基函数和点匹配求解带电导线问题。

7.3-1 Derive the EFIE for a PEC scatterer.
> 推导 PEC 散射体的 EFIE。

7.4-1 Derive the MFIE. What is its range of applicability?
> 推导 MFIE。其适用范围是什么？

7.5-1 Why is the CFIE needed? How is it constructed?
> 为什么需要 CFIE？如何构造？
