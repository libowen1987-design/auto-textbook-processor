# Chapter 7: Advances in the Theory of Perfectly Matched Layers
# 完美匹配层理论的进展

**Authors:** Fernando L. Teixeira and Weng C. Chew

---

## 7.1 Introduction | 引言

The finite-difference time-domain (FDTD) method is a popular numerical method for full-wave simulation of electromagnetic fields. It is an efficient, second-order accurate scheme combining leapfrog update in time with staggered central differencing in space to simulate Maxwell's equations.

时域有限差分（FDTD）方法是全波模拟电磁场的流行数值方法。它是一种高效、二阶精度格式，结合时间上的蛙跳更新和空间上的交错中心差分来模拟麦克斯韦方程。

A key issue is proper truncation of the computational domain for open-region problems. The perfectly matched layer (PML) is an extremely efficient absorbing boundary condition (ABC) introduced by Berenger in 1994, outperforming previous ABCs by orders of magnitude in reduced reflection coefficients.

一个关键问题是开域问题的计算域正确截断。完美匹配层（PML）是 Berenger 于 1994 年引入的一种极其高效的吸收边界条件（ABC），在降低反射系数方面比以前的方法高出数个量级。

PML achieves reflectionless absorption of electromagnetic waves in the continuum limit. Absorption inside PML operates through conductive losses, achieving exponential decay for fields inside the PML.

PML 在连续极限下实现电磁波的无反射吸收。PML 内的吸收通过导电损耗实现，在 PML 内部实现场的指数衰减。

---

## 7.2 PML via Complex Space Coordinates | 通过复空间坐标的PML

### 7.2.1 Frequency Domain Analysis | 频域分析

PML can be derived through complex stretching of Cartesian coordinates in the frequency domain:

PML 可以通过频域中笛卡尔坐标的复拉伸来推导：

The modified source-free Maxwell's equations in PML are:

PML 中修正的无源麦克斯韦方程为：

$$\nabla_s \times \mathbf{E} = i\omega \mu \cdot \mathbf{H}$$
$$\nabla_s \times \mathbf{H} = -i\omega \epsilon \cdot \mathbf{E}$$

where the complex nabla operator is:

复数纳布拉算子为：

$$\nabla_s = \hat{x} \frac{1}{s_x} \frac{\partial}{\partial x} + \hat{y} \frac{1}{s_y} \frac{\partial}{\partial y} + \hat{z} \frac{1}{s_z} \frac{\partial}{\partial z}$$

The complex stretching variables are:

复拉伸变量为：

$$s_x = \kappa_x + \frac{\sigma_x}{\alpha_x + i\omega\epsilon_0}$$

with $\kappa \geq 1$ and $\sigma \geq 0$ (profile functions).

The reflectionless property can be verified by writing down TE and TM reflection coefficients for a planar interface—they are zero.

无反射特性可以通过写出平面界面的 TE 和 TM 反射系数来验证——它们为零。

A more elegant verification observes that coordinate stretching is a mapping of coordinate space to complex coordinate space (analytic continuation). Fields inside PML are continuous everywhere if original fields are continuous.

更优雅的验证是观察坐标拉伸是坐标空间到复坐标空间的映射（解析延拓）。如果原始场是连续的，PML 内的场处处连续。

For propagating modes: $e^{ik \cdot r} \to e^{ik \cdot \tilde{r}}$ where $\tilde{r}$ has positive imaginary part, achieving exponential decay.

对于传播模式：$e^{ik \cdot r} \to e^{ik \cdot \tilde{r}}$，其中 $\tilde{r}$ 具有正虚部，实现指数衰减。

### 7.2.2 Time Domain Analysis | 时域分析

Because complex coordinates involve frequency dependence, they become convolutional operators in time domain. However, convolutions can be avoided by splitting the electromagnetic fields (Berenger's approach).

因为复坐标涉及频率依赖，在时域中会变成卷积算子。然而，可以通过分割电磁场（Berenger 方法）来避免卷积。

The field splitting produces update equations similar to the original Berenger formulation with added generality of $\kappa$ to address evanescent waves.

场分割产生类似于原始 Berenger 格式的更新方程，增加了 $\kappa$ 的通用性以处理倏逝波。

---

## 7.3 PML-FDTD for Dispersive Media | 色散介质的PML-FDTD

### 7.3.1 Time Domain Analysis | 时域分析

Linear time-dispersive media are common in nature. For perfect matching in dispersive media with conductive loss, assume frequency-dependent parameters everywhere with analytic continuation in PML region.

自然中线性时色散介质很常见。对于具有导电损耗的色散介质的完美匹配，在 PML 区域假设处处为频率依赖参数并进行解析延拓。

Modified Maxwell's equations include medium conductivity $\sigma$:

修正的麦克斯韦方程包含介质电导率 $\sigma$：

$$\nabla \times \mathbf{E} = -i\omega\mu \cdot \mathbf{H} - \sigma_m \mathbf{H}$$
$$\nabla \times \mathbf{H} = i\omega\epsilon(\omega) \cdot \mathbf{E} + \sigma_e \mathbf{E}$$

### 7.3.2 Dispersive Medium Models | 色散介质模型

**Lorentz model:** Lorentzian dispersive medium has frequency-dependent relative permittivity:

**洛伦兹模型：** Lorentz 色散介质的频率相关相对介电常数为：

$$\epsilon_r(\omega) = \epsilon_\infty + \sum_{j=1}^{N} \frac{\omega_{p,j}^2}{\omega_{o,j}^2 - \omega^2 - i\gamma_j \omega}$$

**Debye model:** For Debye relaxation:

**德拜模型：** 对于德拜弛豫：

$$\epsilon_r(\omega) = \epsilon_\infty + \sum_{j=1}^{N} \frac{\Delta\epsilon_j}{1 + i\omega\tau_j}$$

The time-domain susceptibility function for both models can be written as exponential functions, allowing recursive convolution computation.

两种模型的时域灵敏度函数都可以写成指数函数，允许递归卷积计算。

### 7.3.3 Incorporation into FDTD Update | 纳入FDTD更新

The time stepping scheme incorporates the dispersive model using piecewise linear recursive convolution (PLRC). The complete update scheme requires storage for field components and auxiliary species variables.

使用时域逐步方案使用分段线性递归卷积（PLRC）合并色散模型。完整更新方案需要存储场分量和辅助种类变量。

Added storage cost of PML dispersive medium is $O(N)$ while plain Yee's FDTD requires $N$.

PML 色散介质的额外存储成本是 $O(N)$，而普通 Yee FDTD 需要 $N$。

---

## 7.4 Maxwellian PML | 麦克斯韦PML

Through field transformations, the modified Maxwell's equations in PML can be cast into the familiar Maxwell's equations for a modified medium with complex anisotropic permittivity and permeability tensors:

通过场变换，PML 中修正的麦克斯韦方程可以转化为修正介质的熟悉麦克斯韦方程，具有复各向异性介电常数和磁导率张量：

$$\tilde{\epsilon} = \Lambda \cdot \epsilon \cdot \Lambda$$
$$\tilde{\mu} = \Lambda \cdot \mu \cdot \Lambda$$

where $\Lambda = \text{diag}(s_x, s_y, s_z)$.

The Maxwellian PML fields coincide with complex-space fields when $s_x = s_y = s_z = 1$ (in physical domain). This formulation provides a theoretical basis for engineered absorbers and is more easily implemented in variational formulations like FEM.

当 $s_x = s_y = s_z = 1$ 时（物理域中），麦克斯韦 PML 场与复空间场一致。该格式为工程吸波器提供了理论基础，更容易在如 FEM 的变分格式中实现。

Both Maxwellian and non-Maxwellian PML satisfy the same boundary conditions on continuity of tangential $\mathbf{E}$ and $\mathbf{H}$ across PML interface.

麦克斯韦和非麦克斯韦 PML 都满足 PML 界面处切向 $\mathbf{E}$ 和 $\mathbf{H}$ 连续性的相同边界条件。

---

## 7.5 Extension to (Bi)anisotropic Media | 扩展到（双）各向异性介质

Using analytic continuation, extending perfect matching to (bi)anisotropic media is simple—all that is needed is to assume the same constitutive tensors everywhere with complex stretching in PML region.

使用解析延拓，将完美匹配扩展到（双）各向异性介质很简单——只需要假设处处具有相同的本构张量，在 PML 区域进行复拉伸。

### 7.5.1 Non-Maxwellian Formulation | 非麦克斯韦格式

In anisotropic medium, each field component needs to be split into three subcomponents (vs. two in isotropic case) because temporal derivative depends on all three spatial derivatives.

在各向异性介质中，每个场分量需要分割成三个子分量（各向同性情况为两个），因为时间导数取决于所有三个空间导数。

### 7.5.2 Maxwellian Formulation | 麦克斯韦格式

The Maxwellian PML constitutive parameters for bianisotropic media are:

双各向异性介质的麦克斯韦 PML 本构参数为：

$$\tilde{\epsilon}_{ij} = \frac{1}{\det(\Lambda)} \cdot \text{cofactor terms involving } s_x, s_y, s_z, \epsilon, \mu$$

The expression bears formal resemblance to an affine transformation, but $\Lambda$ is a function of position, defining a nonlinear transformation on coordinates.

该表达式形式上类似于仿射变换，但 $\Lambda$ 是位置的函数，在坐标上定义非线性变换。

---

## 7.6 PML for Inhomogeneous Media | 非均匀介质的PML

By recognizing PML as a mapping of coordinate space to complex space (transparent to constitutive properties), implementation in inhomogeneous media follows exactly the same lines as homogeneous case.

将 PML 识别为坐标空间到复空间的映射（对本构性质透明），非均匀介质的实现与均匀情况完全相同。

PML is a local boundary condition depending only locally on medium properties at grid termination surface.

PML 是局部边界条件，仅取决于网格终止表面处介质特性的局部性质。

The PML for inhomogeneous media inherits the constitutive parameters of interior domain at each point of the interface.

非均匀介质的 PML 在界面的每一点继承内部域的本构参数。

---

## 7.7 Curvilinear PML | 曲线坐标PML

### 7.7.1 Cylindrical PML-FDTD | 柱面PML-FDTD

For cylindrical coordinates, the radial coordinate is mapped through:

对于柱面坐标，径向坐标通过以下方式映射：

$$\tilde{\rho} = \rho_0 + \int_0^\rho s_\rho(\rho') d\rho'$$

with $s_\rho = \kappa_\rho + \frac{\sigma_\rho}{\alpha_\rho + i\omega\epsilon_0}$.

The reflectionless property follows from continuity of complex variables $\tilde{\rho}(\rho)$ and $\tilde{\phi}(\phi)$.

无反射特性源于复变量 $\tilde{\rho}(\rho)$ 和 $\tilde{\phi}(\phi)$ 的连续性。

The time-domain equations involve convolutions that can be calculated recursively:

时域方程涉及可递归计算的卷积：

$$E_\phi^{split}(\tilde{\rho}, t) = \int_0^t \kappa_\rho(t-\tau) * E_\phi(\tilde{\rho}, \tau) d\tau$$

### 7.7.2 Spherical PML-FDTD | 球面PML-FDTD

For spherical coordinates, the radial coordinate is mapped:

对于球面坐标，径向坐标映射为：

$$\tilde{r} = r_0 + \int_0^r s_r(r') dr'$$

An important advantage: in spherical coordinates, there is **no need to split the fields at all**. PML is achieved through complex stretching in the radial variable $r$ only.

一个重要优点：在球面坐标中，**根本不需要分割场**。PML 仅通过径向变量 $r$ 的复拉伸来实现。

### 7.7.3 Maxwellian PML in Curvilinear Coordinates | 曲线坐标中的麦克斯韦PML

The constitutive tensors for cylindrical PML are:

柱面 PML 的本构张量为：

$$\tilde{\epsilon} = \text{diag}(\frac{s_\rho}{\rho}, \rho s_\rho, s_\phi) \cdot \epsilon \cdot \text{similar for } \mu$$

Both formulations satisfy same boundary conditions on continuity of tangential fields.

两种格式都满足切向场连续性的相同边界条件。

### 7.7.4 Conformal (Doubly Curved) PML | 共形（双曲）PML

A 3D conformal PML on a general orthogonal curvilinear coordinate system can be derived analytically. The derivation uses complex stretching of the normal coordinate along the PML termination surface.

可以解析推导一般正交曲线坐标系统上的 3D 共形 PML。推导使用沿 PML 终止表面的法向坐标的复拉伸。

The termination surface has principal radii of curvature $R_1$ and $R_2$. The transverse metric coefficients are:

终止表面具有主曲率半径 $R_1$ 和 $R_2$。横向度量系数为：

$$h_1 = 1 + \frac{\tilde{n}}{R_1}, \quad h_2 = 1 + \frac{\tilde{n}}{R_2}$$

Cartesian, cylindrical, and spherical PMLs are special cases of this conformal PML.

笛卡尔、柱面和球面 PML 是此共形 PML 的特例。

---

## 7.8 Causality and Dynamic Stability | 因果性和动态稳定性

### 7.8.1 Cartesian PML Analysis | 笛卡尔PML分析

For Cartesian PML, the stretching variables $s_x, s_y, s_z$ can be written as:

对于笛卡尔 PML，拉伸变量 $s_x, s_y, s_z$ 可写为：

$$s_x(\omega) = \kappa_x + \frac{\sigma_x}{\alpha_x + i\omega\epsilon_0} = \frac{\alpha_x + i\omega\epsilon_0 + \sigma_x/\kappa_x}{\alpha_x + i\omega\epsilon_0}$$

For $\kappa_x \geq 1$, $\sigma_x \geq 0$, $\alpha_x > 0$, this function has no poles in upper half-plane and satisfies Kramers-Kronig relations—therefore **causal**.

对于 $\kappa_x \geq 1$、$\sigma_x \geq 0$、$\alpha_x > 0$，此函数在上半平面没有极点并满足 Kramers-Kronig 关系——因此是**因果的**。

The complex-space PML Green function is analytic in upper half-plane, ensuring dynamic stability.

复空间 PML 格林函数在上半平面解析，确保动态稳定性。

### 7.8.2 Cylindrical PML Analysis | 柱面PML分析

A **major difference** arises: the factor $s_\phi/s_\rho$ may have poles in upper half-plane for **convex** cylindrical PML (inner boundary).

一个**重大差异**：对于**凸**柱面 PML（内边界），因子 $s_\phi/s_\rho$ 在上半平面可能有极点。

Physical interpretation: for concave PML, $\int_\rho^\infty s_\rho/\rho d\rho$ has positive imaginary part, while for convex PML, the integral over decreasing $\rho$ gives negative imaginary part.

物理理解：对于凹 PML，$\int_\rho^\infty s_\rho/\rho d\rho$ 具有正虚部，而对于凸 PML，递减 $\rho$ 上的积分为负虚部。

**Consequence: Dynamic instability for convex cylindrical PML.**

**后果：凸柱面 PML 的动态不稳定。**

For concave PML, all singularities translated to lower half-plane, upper half-plane free of singularities.

对于凹 PML，所有奇异性平移到下半平面，上半平面没有奇异性。

### 7.8.3 Spherical PML Analysis | 球面PML分析

Similar to cylindrical case: for concave spherical PML, no poles in upper half-plane, **dynamically stable**. For convex spherical PML, the inverse tensor has poles in upper half-plane, **dynamic instability expected**.

与柱面情况类似：对于凹球面 PML，上半平面没有极点，**动态稳定**。对于凸球面 PML，逆张量在上半平面有极点，**预期动态不稳定**。

Numerical results confirm dramatic early-time instability for convex PML.

数值结果证实凸 PML 的剧烈早期时间不稳定性。

### 7.8.4 Quasi-PML | 准PML

To avoid upper half-plane singularities for convex case, impose $\sigma_\rho \geq 0$ at inner boundaries (irrespective of sign requirement). This gives a **quasi-PML** that is not perfectly matched but dynamically stable.

为避免凸情况的上半平面奇异性，在内边界施加 $\sigma_\rho \geq 0$（不论符号要求）。这给出**准 PML**，虽然不是完美匹配但是动态稳定。

Quasi-PML behaves as true PML only in limit $\rho/\lambda \to 0$.

准 PML 仅在 $\rho/\lambda \to 0$ 时表现得像真实 PML。

---

## 7.9 Generalized PML-FDTD Schemes | 广义PML-FDTD格式

### 7.9.1 Cylindrical PML-PLRC-FDTD: Split-Field Formulation | 柱面PML-PLRC-FDTD：分裂场格式

The complex-space nabla operator in cylindrical coordinates is split to relate each frequency-dependent stretching term to a split field component.

柱面坐标中的复空间纳布拉算子被分割，以将每个频率依赖拉伸项与分裂场分量关联。

Split-field Maxwell's equations in cylindrical PML for dispersive media require updating equations for split field components.

色散介质柱面 PML 中的分裂场麦克斯韦方程需要分裂场分量的更新方程。

### 7.9.2 Cylindrical PML-PLRC-FDTD: Maxwellian Formulation | 麦克斯韦格式

The unsplit field formulation uses auxiliary fields $\mathbf{E}_a, \mathbf{H}_a$ defined by:

非分裂场格式使用由以下定义的辅助场 $\mathbf{E}_a, \mathbf{H}_a$：

$$\mathbf{E}_a = \Lambda \cdot \mathbf{E}, \quad \mathbf{H}_a = \Lambda \cdot \mathbf{H}$$

The update scheme is complete without specifying how to update original fields from auxiliary ones.

更新方案是完整的，无需指定如何从辅助场更新原始场。

---

## 7.10 Unified Theory | 统一理论

### 7.10.1 PML as a Change on the Metric of Space | PML作为空间度规的改变

Under analytic continuation, the elementary arc length is transformed to:

在解析延拓下，基本弧长变换为：

$$d\tilde{l}^2 = s_x^2 dx^2 + s_y^2 dy^2 + s_z^2 dz^2$$

This is equivalent to a change in the metric tensor from Euclidean to complex:

这等价于度量张量从欧几里得到复数的改变：

$$\tilde{g}_{ij} = \frac{1}{2}(s_i^2 + s_j^2) \quad \text{(in appropriate coordinates)}$$

Therefore, PML can be interpreted as a **complextification of the metric tensor of space** in the Fourier domain.

因此，PML 可以解释为频域中度量张量的**复化**。

### 7.10.2 Metric and Topological Structure of Maxwell's Equations | 麦克斯韦方程的度量与拓扑结构

Using differential forms, the source-free Maxwell's equations are:

使用微分形式，无源麦克斯韦方程为：

$$d\mathcal{E} = -\frac{\partial \mathcal{H}}{\partial t}$$
$$d\mathcal{H} = \frac{\partial \mathcal{E}}{\partial t}$$

where $\mathcal{E}$ and $\mathcal{H}$ are 1-forms, and $d$ is the exterior derivative.

The constitutive parameters relate 1-forms to 2-forms via Hodge operators:

本构参数通过霍奇算子将 1 形式与 2 形式关联：

$$\mathcal{D} = \star \epsilon \mathcal{E}, \quad \mathcal{B} = \star \mu \mathcal{H}$$

PML is obtained through modification of Hodge operators:

PML 通过修改霍奇算子获得：

$$\star \to \tilde{\star} = \star \Lambda$$

This reveals the **metric independence** of Maxwell's equations—a deep geometric property.

这揭示了麦克斯韦方程的**度量独立性**——一个深刻的几何性质。

### 7.10.3 Hybrid PMLs | 混合PML

The differential forms viewpoint reveals infinitely many possible PML formulations corresponding to different choices of metric to govern the form-vector isomorphism.

微分形式观点揭示了无限多种可能的 PML 格式，对应于不同的度量选择来控制形式-向量同构。

Complex-space PML and Maxwellian PML are particular cases of these choices.

复空间 PML 和麦克斯韦 PML 是这些选择的特殊情况。

---

## 7.11 Summary | 本章小结

This chapter presented comprehensive advances in PML theory including derivations, implementations, and fundamental understanding.

本章介绍了 PML 理论的全面进展，包括推导、实现和基本理解。

**Key contributions:**

主要贡献：

1. **Complex coordinate stretching:** Unified framework for deriving PML as analytic continuation of spatial coordinates to complex space.

   **复坐标拉伸：** 将 PML 推导为空间坐标到复空间解析延拓的统一框架。

2. **PML for various geometries:** Extensions to cylindrical, spherical, and general curvilinear coordinates using appropriate coordinate stretching.

   **各种几何的 PML：** 使用适当的坐标拉伸扩展到柱面、球面和一般曲线坐标。

3. **Dispersive media support:** Proper handling of Lorentz and Debye dispersive models within PML-FDTD framework.

   **色散介质支持：** 在 PML-FDTD 框架内正确处理洛伦兹和德拜色散模型。

4. **Maxwellian formulation:** Alternative representation as anisotropic medium with complex constitutive tensors.

   **麦克斯韦格式：** 作为具有复本构张量的各向异性介质的替代表示。

5. **Dynamic stability analysis:** Discovery that convex PML in cylindrical/spherical coordinates is dynamically unstable due to pole locations in upper half-plane.

   **动态稳定性分析：** 发现由于极点在上半平面的位置，柱面/球面坐标中的凸 PML 是动态不稳定的。

6. **Conformal PML:** General formulation for doubly curved surfaces based on local radii of curvature.

   **共形 PML：** 基于局部曲率半径的双曲面的通用格式。

7. **Metric interpretation:** PML as a change in the metric of space, explaining why Maxwellian PML works and revealing underlying geometric structure.

   **度量解释：** PML 作为空间度规的改变，解释了麦克斯韦 PML 为何有效并揭示底层几何结构。

8. **Quasi-PML:** Approximate solution for convex geometries that maintains stability at cost of nonzero reflection.

   **准 PML：** 凸几何的近似解，以非零反射为代价保持稳定性。