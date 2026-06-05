# Chapter 6: Error Analysis of Surface Integral Equation Methods
# 面积分方程方法的误差分析

**Authors:** Karl F. Warnick and Weng Cho Chew

---

## 6.1 Introduction | 引言

Numerical methods based on surface integral equations have enjoyed widespread use in computational electromagnetics for many years, since the introduction of the method of moments in the early days of the field of computational electromagnetics [1]. The recent development of techniques for fast evaluation of interactions has greatly extended the frontier of problems that can be analyzed using integral equation solvers [2].

基于面积分方程的数值方法在计算电磁学领域已有多年广泛应用，这得益于矩量法（MOM，Method of Moments）的早期引入。近年来，快速评估交互作用的技术发展极大地拓展了积分方程求解器可分析问题的范围。

An understanding of the convergence behavior of a numerical method requires an estimate or bound on the final solution error in terms of parameters of the algorithm and physical properties of the problem to be solved. If the solution is obtained using an iterative method, then a complete understanding of the numerical method requires iteration count estimates as well.

理解数值方法的收敛行为需要对最终解误差进行估计或界定，以算法参数和问题的物理特性为函数。若使用迭代法求解，则还需估计迭代次数，才能完整理解该数值方法。

---

## 6.1.1 Surface Integral Equations and the Method of Moments | 面积分方程与矩量法

For conducting or dielectric bodies, Maxwell's equations and the boundary conditions on the electromagnetic fields at the surface of the scatterer can be cast into an equivalent system of surface integral equations. These equations are based on integral operators that relate an unknown, equivalent current on the surface of the body to the fields scattered in response to a given incident field.

对于导体或介质体，麦克斯韦方程组以及散射体表面电磁场的边界条件可以等价为面积分方程组。这些方程基于积分算子，将物体表面未知的等效电流与给定入射场激励下的散射场联系起来。

The electric field integral equation (EFIE) for a perfectly electrically conducting (PEC) body is:

完美电导体（PEC）体的电场积分方程（EFIE）为：

$$\hat{n} \times \mathcal{T} J = \hat{n} \times E^{inc}$$

where the integral operator is:

积分算子定义为：

$$\mathcal{T} J = ik\eta \int_S ds' \left[ I + \frac{\nabla \nabla}{k^2} \right] \frac{e^{ikR}}{R} J(r')$$

The free space Green's function is:

自由空间格林函数为：

$$g(r, r') = \frac{e^{ikR}}{4\pi R}, \quad R = |r - r'|$$

For 2D problems with translational invariance, the EFIE reduces to a scalar integral equation:

对于具有平移不变性的二维问题，EFIE 退化为标量积分方程：

$$\mathcal{L} J = E^{inc}$$

The integral operator for TM polarization is:

TM 极化的积分算子为：

$$\mathcal{L} J = k^2 \int_D ds' H_0^{(1)}(k|x - x'|) J(x')$$

The method of moments (MOM) discretizes the integral equation by expanding the unknown current in basis functions:

矩量法（MOM）通过将未知电流展开为基函数来离散化积分方程：

$$J(x) \approx \sum_{n=1}^{N} I_n f_n(x)$$

Testing with another set of functions produces the linear system:

用另一组函数检验得到线性方程组：

$$\sum_n Z_{mn} I_n = V_m$$

where the moment matrix elements are:

矩量矩阵元素为：

$$Z_{mn} = \langle t_m, \mathcal{L} f_n \rangle$$

---

## 6.1.2 Error Measures | 误差度量

The relative $L^2$ error of the current is:

电流的相对 $L^2$ 误差为：

$$\text{Err}_{L^2} = \frac{\| \tilde{J} - J \|_{L^2}}{\| J \|_{L^2}}$$

The relative root mean square (RMS) error is also commonly used:

相对均方根（RMS）误差也是常用指标：

$$\text{Err}_{\text{RMS}} = \sqrt{\frac{\sum_n | \tilde{J}_n - J_n |^2}{\sum_n |J_n|^2}}$$

For scattering problems, the scattering amplitude error is:

对于散射问题，散射幅度误差为：

$$\text{Err}_S = \frac{|\tilde{S} - S|}{|S|}$$

The maximum relative RCS error and relative RMS RCS error are:

最大相对雷达散射截面（RCS）误差和相对 RMS RCS 误差为：

$$\text{Err}_{\max} = \max_m \frac{|\tilde{\sigma}_m - \sigma_m|}{|\sigma_m|}$$

$$\text{Err}_{\text{RMS}} = \sqrt{\frac{1}{M} \sum_{m=1}^{M} \left| \log_{10} \frac{\tilde{\sigma}_m}{\sigma_m} \right|^2}$$

---

## 6.1.3 Approaches to Error Analysis | 误差分析方法

There are two main approaches: theoretical analysis using operator theory and Sobolev spaces, and empirical comparison with benchmark solutions.

主要有两种方法：基于算子理论和索伯列夫空间的理论分析，以及与基准解的经验比较。

### 6.1.3.1 Asymptotic Error Estimates | 渐近误差估计

The asymptotic error estimates have roots in Laplace's equation and Sobolev space theory. The key parameter is $h$, the mesh or discretization length. The convergence behavior for small $h$ is close to that of the static problem.

渐近误差估计源于拉普拉斯方程和索伯列夫空间理论。关键参数是 $h$，即网格或离散长度。对于小的 $h$，收敛行为接近静态问题。

The error estimate in Sobolev norm is:

索伯列夫范数中的误差估计为：

$$\| \tilde{J} - J \|_{H^s} \approx ch^\alpha$$

where $\alpha$ is the order of convergence and $s$ determines the smoothness class.

The Sobolev norm is defined in Fourier domain as:

索伯列夫范数在傅里叶域中定义为：

$$\| u \|_{H^s} = \left( \int_{-\infty}^{\infty} dk \, (1 + |k|^2)^s |U(k)|^2 \right)^{1/2}$$

Surface currents due to TM polarized incident fields belong to $H^{-1/2}$, and $H^{1/2}$ for the TE case.

TM 极化入射场产生的表面电流属于 $H^{-1/2}$ 空间，TE 情况则属于 $H^{1/2}$ 空间。

For smooth scatterers with localized low-order basis functions, the exponent is $\alpha = 2$. For scatterers with edges where current behaves as $x^{-1/2}$, the theoretical prediction is $\alpha = 1/2$.

对于光滑散射体，局部低阶基函数，指数为 $\alpha = 2$。对于有边缘的散射体，电流特性如 $x^{-1/2}$，理论预测为 $\alpha = 1/2$。

### 6.1.3.2 Empirical Methods | 经验方法

Empirical validation uses canonical test cases with exact or tabulated solutions. This approach provides confidence over classes of similar geometries but gives limited insight into underlying error mechanisms.

经验验证使用具有精确解或表格化解的典型测试案例。该方法对类似几何形状类别提供置信度，但对底层误差机制的理解有限。

---

## 6.1.4 Spectral Convergence Theory | 谱收敛理论

The spectral convergence theory extends asymptotic theories by providing absolute, nonasymptotic estimates valid for large scattering problems. The fundamental results are spectral estimates for surface integral operators, which provide solution error and condition number estimates.

谱收敛理论通过提供对大型散射问题有效的绝对非渐近估计来扩展渐近理论。基本结果是面积分算子的谱估计，可提供解误差和条件数估计。

The influence on solution accuracy comes from combined effects of:
- Smooth regions | 光滑区域
- Edge, corner, and point singularities | 边缘、角点和点奇异性
- Resonance | 共振
- Low-frequency breakdown | 低频失效
- Incident electromagnetic field | 入射电磁场

Error estimates also depend on numerical method choices:
- Expansion and testing functions | 展开和检验函数
- Quadrature rule | 求积规则
- Linear system solution algorithm | 线性系统求解算法

---

## 6.2 Spectral Convergence Theory—2D | 谱收敛理论——二维

The integral operators $\mathcal{L}$, $\mathcal{N}$, and $\mathcal{T}$ are non-self-adjoint. A decomposition of the form:

积分算子 $\mathcal{L}$、$\mathcal{N}$ 和 $\mathcal{T}$ 是非自伴的。形式如下的分解：

$$\mathcal{L} = H + R$$

where $H$ is normal and $R$ is a nonnormal perturbation, allows spectral analysis.

其中 $H$ 是正规算子，$R$ 是非正规扰动。

---

## 6.2.1 Circular Cylinder—TM | 圆形柱体——TM极化

The circular cylinder has an analytical solution for plane wave scattering and serves as a benchmark. For the cylinder, $\mathcal{L}$ is normal with an exact spectral decomposition.

圆形柱体对平面波散射有解析解，常作为基准。对于柱体，$\mathcal{L}$ 是正规的，具有精确的谱分解。

The cylindrical mode expansion of the kernel is:

核函数的柱面模展开为：

$$H_0^{(1)}(k|x - x'|) = \sum_{l=-\infty}^{\infty} J_l(ka) H_l^{(1)}(ka) e^{il(\phi - \phi')}$$

The moment matrix eigenvalues approximate the continuous operator eigenvalues:

矩量矩阵特征值逼近连续算子特征值：

$$\bar{\lambda}_r = k \sum_{q \neq 0} J_{r+qN}(ka) H_{r+qN}^{(1)}(ka) \bar{t}_{r+qN} \bar{f}_{r+qN}$$

In the limit $N \to \infty$, the eigenvalues approach the exact values:

在 $N \to \infty$ 时，特征值逼近精确值：

$$\lambda_r = \frac{ik}{4} J_r(ka) H_r^{(1)}(ka)$$

### 6.2.1.1 Spectral Error | 谱误差

The relative spectral error for piecewise polynomial expansion and testing functions is:

分段多项式展开和检验函数的相对谱误差为：

$$E_r \approx \frac{i}{n_\lambda \bar{\lambda}_r} \sum_{q \neq 0} \frac{\bar{t}_{r+qN} \bar{f}_{r+qN}}{|q + r/N|^b}$$

For pulse expansion functions and point testing ($b = 1$), the spectral error for small $\bar{k}a/n_\lambda$ is:

对于脉冲展开函数和点检验（$b = 1$），小 $\bar{k}a/n_\lambda$ 的谱误差为：

$$E_r \approx \frac{2\pi \zeta(3)}{|n_\lambda|^2} \frac{\bar{k}^2 a^2}{|\bar{\lambda}_r|^2}$$

### 6.2.1.2 Quadrature Error | 求积误差

The M-point first order Riemann integration rule introduces additional spectral error:

M 点一阶黎曼求积规则引入额外的谱误差：

$$E_r^{(quadrature)} \approx \frac{i}{n_\lambda} \ln M$$

The quadrature error is first order in $1/n_\lambda$ and can dominate for small $M$.

求积误差在 $1/n_\lambda$ 中是一阶的，对于小的 $M$ 可能占主导。

### 6.2.1.3 Current Error | 电流误差

The surface current solution error is determined from the spectral error. The RMS current error is:

表面电流解误差由谱误差决定。RMS 电流误差为：

$$\| \Delta J \| \approx \frac{2\pi \zeta(3)}{|n_\lambda|^2} \cdot \text{(constant)}$$

The current error is **second order** in $n_\lambda$.

电流误差在 $n_\lambda$ 中是**二阶**的。

### 6.2.1.4 Scattering Amplitude Error | 散射幅度误差

The bistatic scattering amplitude is obtained from the approximate current. The scattering amplitude error is:

双站散射幅度由近似电流得到。散射幅度误差为：

$$\Delta S \approx \sum_r J_r(ka) H_r^{(1)}(ka) E_r^{(sampling)}$$

To leading order, the smoothing error does **not** contribute to scattering amplitude error. The scattering amplitude error is **third order**, higher than the current error.

主要项中，平滑误差对散射幅度误差**没有**贡献。散射幅度误差是**三阶**的，高于电流误差。

This is due to the **stationarity** of the scattering amplitude with respect to perturbations of the solution.

这是由于散射幅度相对于解的扰动具有**平稳性**。

### 6.2.1.5 Internal Resonance | 内部共振

At internal resonances, the EFIE becomes ill-conditioned. The eigenvalue near a resonance can be expanded as:

在内部共振处，EFIE 变得病态。共振附近的特征值可展开为：

$$\lambda_r \approx \frac{ik}{4} \frac{2}{x J_r'(x) H_r^{(1)'}(x)} (ka - x_0)$$

where $x_0$ is a zero of $J_r(x)$. The conjugate gradient (CG) iterative solver applied to the normal equations $Z^\dagger \tilde{Z} \tilde{J} = Z^\dagger E$ can converge at nonresonant rates even at resonance.

即使在共振频率，使用共轭梯度（CG）迭代求解正规方程也能以非共振速率收敛。

---

## 6.2.2 Circular Cylinder—TE | 圆形柱体——TE极化

The TE polarization has a stronger singularity in the kernel. The moment matrix elements involve derivatives of Bessel and Hankel functions:

TE 极化在核函数中有更强的奇异性。矩量矩阵元素涉及贝塞尔和汉克尔函数的导数：

$$Z_{mn} \approx k \sum_l J_l'(ka) H_l^{(1)'}(ka) \bar{t}_l \bar{f}_l e^{il(\phi_m - \phi_n)}$$

The spectral error for pulse expansion ($b = 1$) is:

脉冲展开（$b = 1$）的谱误差为：

$$E_r \approx \frac{\pi \zeta(5)}{|n_\lambda|^4} \frac{\bar{k}^3 a^3}{|\bar{\lambda}_r|^2}$$

The sampling error is **third order** in $1/n_\lambda$, and smoothing error is **second order**.

抽样误差在 $1/n_\lambda$ 中是**三阶**的，平滑误差是**二阶**的。

---

## 6.2.3 Flat Strip—TM | 平板条——TM极化

For the flat strip, the EFIE operator is nonnormal, so exact modal expansion is not available. The operator $\mathcal{L}$ is decomposed as $\mathcal{L} = H + R$, where $H$ is diagonal in Fourier space.

对于平板条，EFIE 算子是非正规的，因此无法进行精确的模展开。算子 $\mathcal{L}$ 分解为 $\mathcal{L} = H + R$，其中 $H$ 在傅里叶空间中是对角的。

The diagonal elements $L_{rr}$ for TM polarization are:

TM 极化的对角元素 $L_{rr}$ 为：

$$L_{rr} \approx \frac{ik}{2\sqrt{k_x^2 - k^2}} + \frac{1}{2D} \ln\left(\frac{k - k_x}{k + k_x}\right)$$

where $k_x$ is the normalized spatial frequency.

### 6.2.3.1 Discretized Operator | 离散算子

The Fourier representation of the discretized EFIE is:

离散 EFIE 的傅里叶表示为：

$$\bar{L}_{rs} \approx \frac{k^2}{2\pi} \int_{-\infty}^{\infty} dk_x \frac{F_r(k_x) F_s(k_x)}{\sqrt{k_x^2 - k^2}} \bar{t}(-k_x) \bar{f}(k_x)$$

where $F_r(k_x) = \text{sinc}((k_x - \bar{k}_r)N/2)$.

### 6.2.3.2 Spectral Error | 谱误差

The relative spectral error for piecewise polynomial basis functions is:

分段多项式基函数的相对谱误差为：

$$E_r \approx \frac{ik}{2\sqrt{2k_x^2 - k^2} \cdot n_\lambda} \left[ \sum_{q \neq 0} \frac{s_b(\bar{k}_r - q n_\lambda)}{q^{b+1}} + (1 - \bar{t}(\bar{k}_r)\bar{f}(\bar{k}_r)) \right]$$

For $b = 2$ discretization, the spectral error is smallest if the testing function is shifted by $\xi = 1/3$.

对于 $b = 2$ 的离散化，如果检验函数平移 $\xi = 1/3$，谱误差最小。

### 6.2.3.3 Current Error | 电流误差

For TM polarization, the current is singular at edges as $x^{-1/2}$, so $L^2$ norm is infinite. The interior current error can be estimated from the spectral error.

对于 TM 极化，电流在边缘处如 $x^{-1/2}$ 发散，所以 $L^2$ 范数无穷。内部电流误差可由谱误差估计。

The error is **second order** in $1/n_\lambda$ for $b \geq 1$ discretization.

对于 $b \geq 1$ 的离散化，误差在 $1/n_\lambda$ 中是**二阶**的。

### 6.2.3.4 Scattering Amplitude Error | 散射幅度误差

The relative forward scattering amplitude error is:

相对前向散射幅度误差为：

$$\frac{|S(\theta_{inc}) - \tilde{S}(\theta_{inc})|}{|S(\theta_{inc})|} \approx |E_r^{(sampling)}(\bar{k}_r)|$$

Only the **sampling error** contributes; smoothing error cancels.

只有**抽样误差**有贡献；平滑误差相互抵消。

---

## 6.2.4 Flat Strip—TE | 平板条——TE极化

For TE polarization, the domain of $\mathcal{N}$ is the fractional Sobolev space $H^{1/2}$, which contains square integrable functions vanishing at edges.

对于 TE 极化，$\mathcal{N}$ 的定义域是分数索伯列夫空间 $H^{1/2}$，包含在边缘处为零的平方可积函数。

The spectrum is approximately the inverse of the TM spectrum:

谱大约是 TM 谱的倒数：

$$N_{rr} \approx \frac{2}{D} \frac{1}{\sqrt{2k_x^2 - k^2}} + \frac{ik}{D} \ln(k - k_x)$$

---

## 6.2.5 Flat Strip—Edge Error | 平板条——边缘误差

At the edges, the current singularity $x^{-1/2}$ (TM) causes additional error. Using the stationarity of the scattering amplitude, the edge error contribution can be estimated.

在边缘处，电流奇异性 $x^{-1/2}$（TM）引起额外误差。利用散射幅度的平稳性，可以估计边缘误差贡献。

The scattering amplitude error estimate from quasioptimality theory gives order $h^{1/2}$, but actual error is much smaller—**second order** relative to current error.

准最优性理论给出的散射幅度误差估计为 $h^{1/2}$ 阶，但实际误差小得多——相对于电流误差是**二阶**的。

The edge error can be written in variational form:

边缘误差可写为变分形式：

$$\Delta S \approx \frac{ik}{4} \langle \mathcal{L}\Delta J, \Delta J_a \rangle + \frac{ik}{4} \langle \Delta J, E^{inc} \rangle - \langle \Delta J_a, E^{inc} \rangle$$

which is **second order** in the solution errors.

这是解误差的**二阶**量。

---

## 6.3 Summary | 本章小结

This chapter presented a spectral convergence theory for error analysis of surface integral equation methods in computational electromagnetics.

本章介绍了计算电磁学中面积分方程方法误差分析的谱收敛理论。

**Key contributions include:**

主要贡献包括：

1. **Spectral decomposition approach:** By decomposing the integral operator as $\mathcal{L} = H + R$ where $H$ is normal, spectral estimates for the discretized operator were obtained.

   **谱分解方法：** 将积分算子分解为 $\mathcal{L} = H + R$（$H$ 为正规算子），获得离散算子的谱估计。

2. **Error categorization:** Identified sampling error (aliasing of high spatial frequency components) and smoothing error (inaccurate representation of low frequency modes) as distinct error sources.

   **误差分类：** 识别出抽样误差（高空间频率分量混叠）和平滑误差（低频模表示不准确）作为不同的误差源。

3. **Convergence rates:** For smooth scatterers with pulse/triangle basis functions:
   - Current error: **second order** ($1/n_\lambda^2$)
   - Scattering amplitude error: **third order** ($1/n_\lambda^3$)

   **收敛阶数：** 对于光滑散射体，脉冲/三角形基函数：
   - 电流误差：**二阶**（$1/n_\lambda^2$）
   - 散射幅度误差：**三阶**（$1/n_\lambda^3$）

4. **Stationarity benefit:** The scattering amplitude is stationary with respect to solution perturbations, giving higher accuracy than current error.

   **平稳性优势：** 散射幅度相对于解的扰动是平稳的，比电流误差具有更高精度。

5. **Resonance handling:** CG applied to normal equations converges at nonresonant rates even at internal resonances.

   **共振处理：** 即使在内部共振处，应用于正规方程的 CG 也能以非共振速率收敛。

6. **Edge singularities:** Proper treatment using Sobolev norms and variational analysis shows actual edge error is much smaller than theoretical upper bounds.

   **边缘奇异性：** 使用索伯列夫范数和变分分析的正确处理表明，实际边缘误差远小于理论上界。

7. **Quadrature error:** First-order accurate in $1/n_\lambda$ for commonly used integration rules, requiring careful treatment near kernel singularities.

   **求积误差：** 对于常用求积规则在 $1/n_\lambda$ 中是一阶精度，需要仔细处理核函数奇异性附近。

The spectral convergence theory provides absolute, nonasymptotic error estimates that are valid for large scattering problems, complementing both asymptotic analysis and empirical validation approaches.

谱收敛理论提供了对大型散射问题有效的绝对非渐近误差估计，补充了渐近分析和经验验证方法。