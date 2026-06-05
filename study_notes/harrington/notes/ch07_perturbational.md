---
chapter: 7
title: Perturbational and Variational Techniques
source: Roger F. Harrington, Time-Harmonic Electromagnetic Fields, IEEE Press
pages: 401-500
---

# Chapter 7: Perturbational and Variational Techniques / 微扰法与变分法

## Section 7-1: Introduction / 引言

**English:**

Many practical problems cannot be solved exactly. **Perturbational** and **variational** techniques provide approximate solutions.

**Perturbation theory:** Start with a known exact solution (unperturbed problem), then apply small changes (perturbations).

**Variational methods:** Express a quantity of interest as a functional that is stationary (first-order variation = 0) with respect to small changes in the field.

Both methods are essential for:
- Waveguide imperfections and losses
- Cavity perturbation for material measurement
- Variational solutions for transmission lines and antennas

**中文：**

许多实际问题无法精确求解。**微扰法**和**变分法**提供近似解。

**微扰理论：** 从已知的精确解（未微扰问题）出发，然后施加小的变化（微扰）。

**变分法：** 将感兴趣量表示为泛函，该泛函对场的小变化是稳定的（一次变分 = 0）。

---

## Section 7-2: Degenerate Perturbation / 简并微扰

**English:**

**Perturbation of degenerate states** occurs when the unperturbed problem has multiple solutions with the same eigenvalue.

Example: Two orthogonal modes with same cutoff frequency $f_c$. When perturbed (e.g., slight asymmetry), they split into two distinct frequencies.

**Method:** Form matrix representation of perturbation operator in basis of degenerate unperturbed modes. Diagonalize to find perturbed eigenvalues.

**For 2 × 2 degenerate basis:**
$$[H] = [H_0] + \lambda[V]$$

If $[H_0]$ has eigenvalue $E_0$ with eigenvectors $\mathbf{e}_1, \mathbf{e}_2$, then in the degenerate subspace:
$$E^{(1)} = E_0 + \lambda\langle\mathbf{e}_i|V|\mathbf{e}_j\rangle$$

**Solved by:** Diagonalize the matrix $\langle\mathbf{e}_i|V|\mathbf{e}_j\rangle$.

**Application:** Coupled-mode theory for parallel waveguides, directional couplers.

**中文：**

**简并态的微扰**发生在未微扰问题有多个相同特征值的解时。

例如：两个正交模式具有相同的截止频率 $f_c$。当微扰（如轻微不对称）时，它们分裂成两个不同的频率。

**方法：** 在简并未微扰模的基中形成微扰算子的矩阵表示。对角化以找到微扰后的特征值。

**应用：** 耦合模理论，用于平行波导和定向耦合器。

---

## Section 7-3: Non-degenerate Perturbation / 非简并微扰

**English:**

**Non-degenerate perturbation** applies when the unperturbed states have distinct eigenvalues.

**First-order correction** to eigenvalue $E_n$:
$$E_n^{(1)} = \langle\mathbf{e}_n|V|\mathbf{e}_n\rangle \tag{7-12}$$

**First-order correction** to eigenvector $\mathbf{e}_n$:
$$\mathbf{e}_n^{(1)} = \sum_{m \neq n} \frac{\langle\mathbf{e}_m|V|\mathbf{e}_n\rangle}{E_n - E_m}\mathbf{e}_m \tag{7-14}$$

**Application: Waveguide wall roughness**

For a rectangular waveguide with slight wall roughness $\Delta(x,y)$:
$$\alpha_\text{rough} \approx \frac{k^2}{2\beta}\left(\frac{\Delta}{a}\right)^2 \quad \text{(for TE10 mode)}$$

The perturbation increases attenuation.

**Application: Waveguide irises**

Small capacitive or inductive irises cause perturbation in cutoff wavenumber:
$$\Delta k_c \approx -\frac{\omega\epsilon_0 A}{a b}$$

where $A$ is the iris area.

**中文：**

**非简并微扰**适用于未微扰态具有不同特征值的情况。

**特征值 $E_n$ 的一阶修正：**
$$E_n^{(1)} = \langle\mathbf{e}_n|V|\mathbf{e}_n\rangle \tag{7-12}$$

**特征向量 $\mathbf{e}_n$ 的一阶修正：**
$$\mathbf{e}_n^{(1)} = \sum_{m \neq n} \frac{\langle\mathbf{e}_m|V|\mathbf{e}_n\rangle}{E_n - E_m}\mathbf{e}_m \tag{7-14}$$

**应用：波导壁粗糙度**

对于轻微粗糙度的矩形波导：
$$\alpha_\text{rough} \approx \frac{k^2}{2\beta}\left(\frac{\Delta}{a}\right)^2$$

---

## Section 7-4: Variational Methods / 变分法

**English:**

**Variational methods** express a functional $F[\psi]$ that is stationary (extremum) at the true solution.

**Stationarity condition:**
$$\delta F = 0 \quad \text{(first-order variation vanishes)}$$

**Ritz method:** Assume trial solution $\psi = \sum_i a_i f_i$ where $f_i$ are known basis functions. Minimize $F$ with respect to coefficients $a_i$:

$$\frac{\partial F}{\partial a_i} = 0 \Rightarrow \text{solve for } a_i$$

**Example: Transmission line impedance**

$$Z = \frac{\int_S \mathbf{E} \times \mathbf{H}^* \cdot d\mathbf{s}}{I^2}$$

This is stationary with respect to small errors in $\mathbf{E}$ and $\mathbf{H}$.

**Example: Cavity resonance frequency**

$$f - f_0 = \frac{\delta W}{\omega W}$$

where $W$ is stored energy and $\delta W$ is perturbation in energy due to material loading.

**For admittance function:**
$$Y = \frac{I^2}{\int_V \mathbf{E} \cdot \mathbf{J}^*\, dV}$$

**Reciprocity variational method:** Express S-matrix elements as functionals that are stationary.

**中文：**

**变分法**将泛函 $F[\psi]$ 表达为在真实解处是稳定的（极值）。

**稳定性条件：**
$$\delta F = 0 \quad \text{（一次变分消失）}$$

**里茨法：** 假设试探解 $\psi = \sum_i a_i f_i$，其中 $f_i$ 是已知的基函数。对系数 $a_i$ 最小化 $F$：

$$\frac{\partial F}{\partial a_i} = 0 \Rightarrow \text{求解 } a_i$$

---

## Section 7-5: Method of Moments (MoM) / 矩量法

**English:**

**Method of Moments (MoM)** converts integral equations to matrix equations by expanding the unknown in a set of basis functions and testing with weighting functions.

**General procedure:**

1. **Choose basis functions** $\{f_n(\mathbf{r})\}$ to expand unknown $J(\mathbf{r})$:
$$J(\mathbf{r}) = \sum_n I_n f_n(\mathbf{r})$$

2. **Choose weighting (testing) functions** $\{w_m(\mathbf{r})\}$ and form inner products:
$$\langle w_m, \mathcal{L}J \rangle = \langle w_m, V \rangle$$

where $\mathcal{L}$ is the integral operator and $V$ is the known excitation.

3. **Form matrix equation:**
$$[Z]\{I\} = \{V\}$$

where $Z_{mn} = \langle w_m, \mathcal{L}f_n \rangle$ is the **impedance matrix**.

**Galerkin's method:** Use same functions for basis and weighting ($w_m = f_m$). Most common for electromagnetic problems.

**Pulse basis functions:** Piecewise constant on small intervals. Simple but requires many elements for smooth solutions.

**Sinusoidal basis functions:** Match current distribution better for wire antennas. Used in NEC (Numerical Electromagnetics Code).

**Convergence:** MoM solution converges to exact solution as number of basis functions increases, provided basis is complete.

**Ill-conditioned matrices:** EM MoM matrices are typically dense and ill-conditioned. Preconditioning techniques (e.g., iterative solvers, multilevel methods) are needed for large problems.

**Application: Wire antennas**

Pocklington's equation for thin wire:
$$\int_{-L/2}^{L/2} I(z')\left(\frac{\partial^2}{\partial z^2} + k^2\right)\frac{e^{-jkR}}{4\pi R}\, dz' = \frac{V}{Z_s}$$

where $Z_s$ is the surface impedance.

**Application: Microstrip lines**

Green's function for layered media. Basis functions with singular behavior at edges.

**Application: Scattering from conducting bodies**

EFIE or MFIE discretized on conducting surface. Dense matrix solved by direct or iterative methods.

**中文：**

**矩量法（MoM）**通过将未知量展开为一组基函数，并用权函数进行测试，将积分方程转换为矩阵方程。

**一般步骤：**

1. **选择基函数** $\{f_n(\mathbf{r})\}$ 展开未知量 $J(\mathbf{r})$：
$$J(\mathbf{r}) = \sum_n I_n f_n(\mathbf{r})$$

2. **选择权（测试）函数** $\{w_m(\mathbf{r})\}$ 并形成内积：
$$\langle w_m, \mathcal{L}J \rangle = \langle w_m, V \rangle$$

3. **形成矩阵方程：**
$$[Z]\{I\} = \{V\}$$

其中 $Z_{mn} = \langle w_m, \mathcal{L}f_n \rangle$ 是**阻抗矩阵**。

**应用：线天线**

Pocklington方程：
$$\int_{-L/2}^{L/2} I(z')\left(\frac{\partial^2}{\partial z^2} + k^2\right)\frac{e^{-jkR}}{4\pi R}\, dz' = \frac{V}{Z_s}$$

---

## Section 7-6: Hallén's Integral Equation / 哈伦积分方程

**English:**

**Hallén's integral equation** is an alternative to Pocklington for thin wire antennas.

For a symmetric cylindrical dipole of length $L$:
$$\int_{-L/2}^{L/2} I(z')\frac{e^{-jkR}}{4\pi R}\, dz' = A\cos(kz) + B\sin(kz) + \frac{V}{2Z_0}\sin(k|z|)$$

where $A$ and $B$ are determined by boundary conditions:
- $I(0) = 0$ (center of dipole)
- $I(\pm L/2) = 0$ (end conditions)

**Solution by MoM:** Expand $I(z) = \sum_n I_n f_n(z)$ and form matrix equation.

**Basis functions for dipole:**
- Triangular functions (piecewise linear) — common in NEC
- Sinusoidal functions — match current distribution

**Current distribution approximation:**
For a half-wave dipole, $I(z) = I_0 \sin(k(|z| - L/2))$ (sinusoidal approximation)

**Input admittance:**
$$Y_\text{in} = Y_c \frac{2\sin^2(kL/2)}{2\cos^2(kL/2) - jZ_0 Y_c\sin^2(kL/2)}$$

At resonance ($L = \lambda/2$): $Y_\text{in} \approx 1/73$ S, $R_\text{in} \approx 73\ \Omega$.

**中文：**

**Hallén积分方程**是细线天线的另一种方法（替代Pocklington）。

对于长度为 $L$ 的对称圆柱偶极子：
$$\int_{-L/2}^{L/2} I(z')\frac{e^{-jkR}}{4\pi R}\, dz' = A\cos(kz) + B\sin(kz) + \frac{V}{2Z_0}\sin(k|z|)$$

**用MoM求解：** 展开 $I(z) = \sum_n I_n f_n(z)$ 并形成矩阵方程。

**输入导纳：**
$$Y_\text{in} = Y_c \frac{2\sin^2(kL/2)}{2\cos^2(kL/2) - jZ_0 Y_c\sin^2(kL/2)}$$

在谐振时（$L = \lambda/2$）：$R_\text{in} \approx 73\ \Omega$。

---


---

## Section 7-7: Variational Principles for S-Parameters / S参数的变分原理

**English:**

**Variational expressions** for S-parameters provide stable approximations that are first-order accurate.

**Reflection coefficient variational:**
$$\\Gamma = \\frac{\\langle \\mathbf{E}_t, \\mathbf{Z}_0 \\mathbf{H}_t \\times \\hat{n} \\rangle}{\\langle \\mathbf{E}_t, \\mathbf{H}_t \\times \\hat{n} \\rangle}$$

This is stationary with respect to small errors in $\\mathbf{E}_t, \\mathbf{H}_t$.

**Impedance matrix elements:**
$$Z_{ij} = \\frac{\\langle \\mathbf{E}_i, \\mathbf{J}_j \\rangle}{I_i I_j}$$

where $\\mathbf{E}_i$ is the field due to port $i$ current and $\\mathbf{J}_j$ is the current distribution at port $j$.

**Admittance matrix elements:**
$$Y_{ij} = \\frac{\\langle \\mathbf{H}_i, \\mathbf{E}_j \\rangle}{V_i V_j}$$

**Reaction formulation for S-matrix:**
$$S_{ij} = \\frac{2\\langle a, b \\rangle}{\\sqrt{P_i P_j}}$$

where $a$ is the wave amplitude at port $i$ with port $j$ matched, and $b$ is the wave leaving port $j$.

**Perturbation of resonant cavities:**

For a cavity with small perturbation $\\Delta\\epsilon, \\Delta\\mu$:
$$\\frac{\\Delta f}{f} = \\frac{\\langle \\Delta\\epsilon |\\mathbf{E}|^2 + \\Delta\\mu |\\mathbf{H}|^2 \\rangle}{2\\langle \\epsilon |\\mathbf{E}|^2 + \\mu |\\mathbf{H}|^2 \\rangle}$$

This is the **cavity perturbation formula** used for material measurement.

**Dielectric constant measurement:** Insert sample into cavity, measure resonant frequency shift, compute permittivity from perturbation formula.

**Quality factor perturbation:**
$$\\frac{1}{Q} = \\frac{1}{Q_0} + \\tan\\delta_\\text{sample} \\cdot \\frac{\\text{stored energy in sample}}{\\text{total stored energy}}$$

**Chinese:**

**S参数的变分表达式**提供稳定的第一阶精确近似。

**阻抗矩阵元素：**
$$Z_{ij} = \\frac{\\langle \\mathbf{E}_i, \\mathbf{J}_j \\rangle}{I_i I_j}$$

**谐振腔微扰：**

对于具有小微扰 $\\Delta\\epsilon, \\Delta\\mu$ 的腔体：
$$\\frac{\\Delta f}{f} = \\frac{\\langle \\Delta\\epsilon |\\mathbf{E}|^2 + \\Delta\\mu |\\mathbf{H}|^2 \\rangle}{2\\langle \\epsilon |\\mathbf{E}|^2 + \\mu |\\mathbf{H}|^2 \\rangle}$$

这是用于材料测量的**腔体微扰公式**。

---

## Section 7-8: Mode Matching Method / 模式匹配法

**English:**

**Mode matching** solves waveguide discontinuities by expanding fields in terms of complete sets of waveguide modes.

**Procedure:**

1. **Expand fields** in region 1 as sum of modes with unknown amplitudes $A_n$:
$$\\mathbf{E}_1 = \\sum_n A_n \\mathbf{E}_n^{(1)}$$
$$\\mathbf{H}_1 = \\sum_n A_n \\mathbf{H}_n^{(1)}$$

2. **Expand fields** in region 2 as sum of modes with unknown amplitudes $B_n$:
$$\\mathbf{E}_2 = \\sum_n B_n \\mathbf{E}_n^{(2)}$$
$$\\mathbf{H}_2 = \\sum_n B_n \\mathbf{H}_n^{(2)}$$

3. **Match boundary conditions** at the interface $S$:
$$\\hat{n} \\times (\\mathbf{E}_1 - \\mathbf{E}_2) = 0 \\quad \\text{(tangential E continuous)}$$
$$\\hat{n} \\times (\\mathbf{H}_1 - \\mathbf{H}_2) = 0 \\quad \\text{(tangential H continuous)}$$

4. **Project onto each mode** to obtain matrix equation:
$$[T]\\{A\\} = [U]\\{B\\}$$

where $[T]$ and $[U]$ contain mode overlap integrals.

**Eigenfunctions** are complete for representing any field in the guide.

**Truncation:** Keep $N_1$ modes in region 1 and $N_2$ modes in region 2. Accuracy increases with $N_1, N_2$.

**Singular value decomposition:** Used to solve ill-conditioned mode matching matrices.

**Application: Step discontinuity in rectangular waveguide**

For step from guide $a \\times b$ to guide $a \\times b'$:
$$\\begin{pmatrix} b_1 \\\\ b_2 \\end{pmatrix} = \\begin{pmatrix} S_{11} & S_{12} \\\\ S_{21} & S_{22} \\end{pmatrix} \\begin{pmatrix} a_1 \\\\ a_2 \\end{pmatrix}$$

where modes in narrower guide are evanescent (below cutoff).

**Chinese:**

**模式匹配**通过用完整波导模式集展开场来求解波导不连续性。

**步骤：**

1. **展开**区域1中的场为模的和，包含未知振幅 $A_n$：
$$\\mathbf{E}_1 = \\sum_n A_n \\mathbf{E}_n^{(1)}$$

2. **展开**区域2中的场为模的和，包含未知振幅 $B_n$：
$$\\mathbf{E}_2 = \\sum_n B_n \\mathbf{E}_n^{(2)}$$

3. **匹配**界面 $S$ 处的边界条件：
$$\\hat{n} \\times (\\mathbf{E}_1 - \\mathbf{E}_2) = 0$$
$$\\hat{n} \\times (\\mathbf{H}_1 - \\mathbf{H}_2) = 0$$

4. **投影到每个模**以获得矩阵方程。

---

## Section 7-9: Finite Element Method Basics / 有限元法基础

**English:**

**Finite Element Method (FEM)** discretizes space into small elements and solves for fields at element nodes.

**Weak form** of Maxwell's equations:
$$\\int_V \\left((\\nabla \\times \\mathbf{E}) \\cdot (\\nabla \\times \\mathbf{E}_t) - k^2 \\mathbf{E} \\cdot \\mathbf{E}_t\\right) dV = 0$$

where $\\mathbf{E}_t$ are test (weighting) functions.

**Triangular or tetrahedral elements** for 2D or 3D discretization.

**Basis functions** are piecewise polynomials defined on each element.

**Assembly:** Form global matrix by summing element contributions.

**Sparse matrix** results from FEM — amenable to efficient sparse solvers.

**PML absorbing boundary conditions** simulate open regions.

**Application to waveguides:** Complex propagation constants found by solving eigenvalue problem:
$$[K]\\{\\mathbf{E}\\} = k_z^2 [M]\\{\\mathbf{E}\\}$$

**Application to cavities:** Find resonant frequencies by solving:
$$\\text{det}([K] - \\omega^2 [M]) = 0$$

**Commercial FEM tools:** HFSS, COMSOL, ANSYS Maxwell.

**Chinese:**

**有限元法（FEM）**将空间离散为小单元，并求解单元节点处的场。

**弱形式**的麦克斯韦方程：
$$\\int_V \\left((\\nabla \\times \\mathbf{E}) \\cdot (\\nabla \\times \\mathbf{E}_t) - k^2 \\mathbf{E} \\cdot \\mathbf{E}_t\\right) dV = 0$$

**三角或四面体单元**用于2D或3D离散化。

**组装：** 通过求和单元贡献形成全局矩阵。

**稀疏矩阵**源自FEM——适用于高效稀疏求解器。

---

