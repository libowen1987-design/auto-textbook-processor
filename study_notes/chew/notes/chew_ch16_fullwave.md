# 第 16 章：多层微带问题的全波分析
# Chapter 16: Full-Wave Analysis of Multilayer Microstrip Problems

---

## 16.1 引言 | Introduction

在过去的数十年中，集成电路（ICs）取得了令人瞩目的进展。平面无源组件广泛应用于IC系统。因此，平面组件的快速精确电磁（EM）分析对于IC设计至关重要。

In the past decades, integrated circuits (ICs) have undergone impressive advancements. Planar passive components are extensively used in IC systems. Hence, fast and accurate electromagnetic (EM) analysis of planar components becomes very important for IC design.

开发可靠的计算机辅助设计（CAD）工具需要考虑以下几个方面：

To develop a reliable computer-aided design (CAD) tool for this purpose, several aspects have to be considered:

1. **多层介质**：随着结构复杂性的增加，多层介质常被用于实现更灵活的设计，建模必须能够处理多层介质中的平面组件。
   With the increased complexity of those structures, multilayer media are often employed to allow more versatile designs. This fact necessitates that the modeling be capable of dealing with planar components in multilayer media.

2. **全波建模**：随着IC工作频率的提高，经验公式和准静态模型无法提供精确结果，需要开发严格的全波EM建模方法。
   As the operating frequency of ICs increases, the empirical formulas and quasi-static models are unable to provide accurate results. Consequently, it is desirable to develop a rigorous full-wave EM modeling.

3. **电大尺寸问题**：需要具备处理电大尺寸问题的能力，以执行集成仿真。
   The ability to tackle electrically large problems becomes necessary to perform the integrated simulation.

**全波方法的分类 | Classification of Full-Wave Methods:**

全波EM方法可分为两大类：微分方程方法和积分方程方法。

These methods can be divided into two broad classes: the differential equation approach and the integral equation approach.

| 方法 | Approach | 特点 | Characteristics |
|------|----------|------|----------------|
| 微分方程 | Differential Equation | FDTD、FEM | 体积离散，计算量大 |
| 积分方程 | Integral Equation | MOM | 表面离散，矩阵维度低 |

积分方程方法对于多层介质问题更具吸引力，因为它允许应用Green定理将体积分化为面积分，从而使用表面离散而非体积离散来显著降低矩阵维度。

The integral equation approach is more attractive for multilayer medium problems since the method allows one to apply Green's theorem to reduce volume integrals to surface integrals, thus reducing the matrix dimension significantly because of the use of surface discretization rather than volume discretization.

---

## 16.2 多层介质的Green函数 | Green's Functions for Multilayer Media

本节讨论Green函数的高效评估方法，Green函数以Sommerfeld积分（SIs）的形式表达。

This section addresses the efficient evaluation of Green's functions, which are expressed in terms of the Sommerfeld integrals (SIs).

### 16.2.1 传输线模型 | Transmission Line Model

考虑多层介质中的电流源。每层由相对介电常数 $\varepsilon_{ri}$、相对磁导率 $\mu_{ri}$ 和厚度 $h_i$ 表征。

Consider a current source in a multilayer medium. Each layer is characterized by relative permittivity $\varepsilon_{ri}$, relative permeability $\mu_{ri}$, and thickness $h_i$.

电流产生的电场可用混合势形式表示为：

The electric field due to the current can be expressed in a mixed potential form as:

$$\mathbf{E}(\mathbf{r}) = j\omega \mu_0 \int G_V(\mathbf{r}, \mathbf{r}') \mathbf{J}(\mathbf{r}') dS' + \frac{1}{\varepsilon_0} \nabla \int G_\Phi(\mathbf{r}, \mathbf{r}') \nabla' \cdot \mathbf{J}(\mathbf{r}') dS' \tag{16.1}$$

其中 $\mathbf{J}$ 是源电流密度，$G_V$ 和 $G_\Phi$ 分别是矢量势和标量势的Green函数。

where $\mathbf{J}$ denotes the electric current density of the source, and $G_V$ and $G_\Phi$ are the Green's functions for the vector and scalar potentials, respectively.

**谱域Green函数 | Spectral Domain Green's Functions:**

谱域Green函数可由等效传输线构建。将求解电磁场的问题转化为求解相应传输线的电压和电流问题。

The spectral domain Green's functions for an arbitrary dipole in multilayer media can be accomplished by constructing equivalent transmission lines. Therefore, the original problem to find electric and magnetic fields is converted to the problem of obtaining the voltage and current of the corresponding transmission lines.

### 16.2.2 离散复镜像法（DCIM）| Discrete Complex Image Method

本工作采用改进的DCIM来高效评估Green函数。DCIM的关键步骤包括：

An improved DCIM is employed to efficiently evaluate the Green's functions in this work. The key steps of DCIM include:

1. **提取主场项**：从谱域Green函数中提取主场项 $e^{-j k_\rho \rho}/\rho$（当源点和观察点在同一层时）。
   Extract the primary field term $e^{-j k_\rho \rho}/\rho$ when the source and observation points are in the same layer.

2. **提取表面波贡献**：表面波贡献可写为：
   Extract the guided-mode or surface-wave contributions, which can be written as:
   
$$P_{sw} = \frac{j}{2} \int_{-\infty}^{\infty} \text{Res}_{k_\rho = k_\rho^m} \{\tilde{G}(k_\rho)\} H_0^{(2)}(k_\rho \rho) dk_\rho \tag{16.11}$$

3. **GPOF近似**：剩余部分用广义铅笔函数（GPOF）方法近似为复指数之和。
   The remainder of $\tilde{G}$ can be approximated as a sum of complex exponentials using the generalized pencil-of-function (GPOF) method.

**表面波极点提取 | Surface-Wave Pole Extraction:**

先前DCIM工作中，表面波贡献通过留数计算解析获得，但难以推广到多层情况。本工作通过在复 $k_\rho$ 平面中递归计算轮廓积分来获得 $k_\rho^m$ 和留数。

In the previous work on the DCIM, $\text{Res}_{k_\rho = k_\rho^m}$ is calculated analytically by using residue calculus, which makes it difficult to extend to multilayer cases. Here, we obtain $k_\rho^m$ and $\text{Res}$ by evaluating a contour integral numerically in the complex $k_\rho$-plane recursively.

**近场与远场的过渡 | Transition between Near and Far Field:**

当 $\rho \to 0$ 时，Green函数在 $\mathbf{r} \neq \mathbf{r}'$ 处并不奇异，但表面波项携带奇异性。

When $\rho \to 0$, the Green's function is not singular at $\mathbf{r} \neq \mathbf{r}'$; however, the guided-mode term carries the singularity.

为克服这一困难，引入过渡点，将近场和远场区域分开。因此，DCIM应用两次：一次有表面波提取（用于近场），一次无表面波提取（用于远场）。

To overcome this difficulty, a transition point is introduced, which divides the near- and far-field regions. Therefore, the DCIM is applied twice: once with and once without the guided-mode extraction.

### 16.2.3 插值策略 | Interpolation Scheme

Green函数评估的计算机时间问题仍需考虑，因为Green函数的数量在MOM分析中与未知数的平方成正比。

Issues of computer time still have to be considered since the number of Green's functions to be evaluated is proportional to $N^2$ in the MOM analysis.

采用插值策略：沿结构所在的 $\rho$ 轴分段，然后用Chebyshev插值应用于变量 $\rho$。

An interpolation scheme is usually employed. Sections along the $\rho$-axis where the structure is located are first determined and then subdivided into $N_\rho$ sheets, resulting in a total of $N_\rho^2$ combinations of $\rho$ and $\rho'$.

---

## 16.3 矩量法（MOM）求解 | The Method-of-Moments Solution

### 16.3.1 基函数的选择 | Choice of Basis Functions

高效精确MOM分析的关键因素是基函数的选择。

A critical factor for an efficient and accurate MOM analysis is the choice of basis functions.

**传统基函数 | Traditional Basis Functions:**
- 屋顶函数（Rectangular discretization）
- Rao-Wilton-Glisson（RWG）函数（Triangular discretization）

这些函数在零阶完备，导致需要非常细的离散才能获得精确解，收敛缓慢。

These functions are complete to the zeroth order. As a result, a very fine discretization is often required to yield an accurate solution. This leads to a large matrix equation, and the numerical solution converges slowly to the exact one when the discretization is made finer.

**高阶基函数 | Higher-Order Basis Functions:**

高阶插值矢量基函数（由Graglia等人开发）在本工作中被采用。此外，使用曲线性离散以提供更灵活的模式任意形状能力。

The higher-order interpolatory basis functions developed by Graglia et al. are employed in this work. Also, the curvilinear discretization is used, which provides more flexibility to model arbitrary shapes.

高阶插值矢量基函数在给定三角单元上通过将零阶基函数与一组多项式函数相乘来构造：

The higher-order interpolatory vector basis functions on a given triangular element are constructed by multiplying the zeroth-order basis functions with a set of polynomial functions:

$$\mathbf{N}_n^{(p)}(\mathbf{r}) = c_n^{(p)} \mathbf{\Lambda}_n^{(0)}(\mathbf{r}) T_n^{(p)}(\mathbf{r}) \tag{16.19}$$

其中 $\mathbf{\Lambda}_n^{(0)}$ 是零阶基函数，$T_n^{(p)}$ 是多项式函数。

where $\mathbf{\Lambda}_n^{(0)}$ is the zeroth-order basis function, and $T_n^{(p)}$ is the polynomial function.

### 16.3.2 收敛行为分析 | Convergence Behavior Analysis

以微带贴片天线为例分析高阶MOM的收敛行为。

The convergence behavior of the higher-order MOM is first analyzed using a microstrip patch antenna as an example.

贴片尺寸为 $40 \text{ mm} \times 40 \text{ mm}$，位于相对介电常数2.17、厚度1.58 mm的基板上。

The patch is 40 mm × 40 mm, which resides on a substrate with relative permittivity 2.17 and thickness 1.58 mm.

**观察结果 | Observations:**

1. 对于相同数量的未知数，高阶方案给出更准确的结果。
   For the same number of unknowns, the higher-order scheme gives more accurate results.

2. 不同阶方案的CPU时间相当。
   The CPU times are comparable for different order schemes.

3. 对于小问题，高阶方案使用更多CPU时间（因为奇异和近相互作用项相对主导）。
   For small problems, the higher-order schemes use more CPU time.

4. 当问题规模变大时，高阶方案比低阶方案更高效。
   When the problem size becomes large, the higher-order schemes become more efficient than the lower-order ones.

### 16.3.3 数值结果 | Numerical Results

**矩形微带贴片天线 | Rectangular Microstrip Patch Antenna:**

后向RCS作为频率的函数给出。零阶、一阶和二阶方案用于粗离散（24个三角形）。

The backscatter RCS is given as a function of frequency. The zeroth-, first-, and second-order schemes are employed for a coarse discretization with 24 triangles.

零阶方案无法给出精确结果，尤其在高频率，而一阶和二阶方案收敛到精确结果。

The zeroth-order scheme does not give an accurate result, especially at high frequencies, whereas the first- and second-order schemes converge to the accurate result.

**四端口分支线耦合器 | Four-Port Branch Line Coupler:**

使用968个未知数的二阶方案。S参数与测量数据吻合良好。

With the mesh shown in Figure 16.10, we employ the second-order scheme, which has 968 unknowns. The S-parameters obtained are shown in Figure 16.10, compared with the measured data.

**四端口环形功率分配器 | Four-Port Annular-Ring Power Divider:**

展示曲线性离散的优势。圆形边界由曲线性贴片精确建模。

To show advantages of the curvilinear discretization, the fourth example is a four-port annular-ring power-divider.

**螺旋电感器 | Spiral Inductors:**

两个螺旋电感器示例（有垂直电流的3D结构）：
- 矩形螺旋电感器
- 曲线性边界螺旋电感器

Both examples have vertical currents. Both of them are the spiral inductors, one with a rectangular shape and the other with a curvilinear boundary.

---

## 16.4 快速频率扫描计算 | Fast Frequency-Sweep Calculation

### 16.4.1 渐近波形评估（AWE）| Asymptotic Waveform Evaluation

MOM分析在频域中实现。要获得感兴趣频带内的频率响应，必须在每个离散频率重复计算。

The MOM analysis in the preceding section is implemented in the frequency domain. To obtain frequency responses over a band of interest, we have to repeat the calculation at each discrete frequency.

**AWE技术 | AWE Technique:**

基本思想是用低阶有理函数（Padé近似）来逼近频率响应或传递函数。

The basic idea of these techniques is to approximate the frequency response, or the transfer function, by a low-order rational function, the Padé approximant.

在AWE中，未知电流在展开点展开为Taylor级数。Taylor级数系数或矩与阻抗矩阵的频率导数相关联。

In AWE, the unknown current is first expanded as a Taylor series at the expansion point. The Taylor series coefficients, or the moments, are associated with the frequency derivatives of the impedance matrix.

**CPU时间比较 | CPU Time Comparison:**

| 示例 | Direct (s) | AWE (s) | 加速比 |
|------|-----------|---------|--------|
| Ex. 1 | 384 | 18.1 | 21.2× |
| Ex. 2 | 8,320 | 1,050.6 | 7.9× |
| Ex. 3 | 10,800 | 863.1 | 12.5× |

Example 1: 微带双短截线（205个未知数），AWE加速约21倍。
Example 2: 两端口非对称天线（912个未知数），AWE加速约8倍。
Example 3: 重叠间隙耦合微带滤波器（503个未知数），AWE加速约12.5倍。

Example 1: Microstrip double-stub with 205 unknowns, AWE is approximately 21 times faster.
Example 2: Two-port asymmetric antenna with 912 unknowns, AWE is approximately eight times faster.
Example 3: Overlap-gap-coupled microstrip filter with 503 unknowns, AWE is approximately 12.5 times faster.

---

## 16.5 共轭梯度-FFT方法 | The Conjugate Gradient–FFT Method

### 16.5.1 基本原理 | Basic Principle

模拟大规模微带问题通常需要大量未知数。对于常规MOM，内存需求与 $N^2$ 成正比。

To simulate large-scale microstrip problems, it is often necessary to employ a large number of unknowns. For the conventional MOM, the memory requirement is always proportional to $N^2$.

**CG-FFT方法 | CG-FFT Method:**

通过利用Green函数的平移不变性，矩阵-向量乘积可使用FFT计算。

By exploiting the translational invariance of the Green's function, the matrix-vector product can be computed using the FFT.

当与共轭梯度（CG）方法结合时，得到的算法称为共轭梯度-FFT（CG-FFT）方法。

When this is combined with the conjugate gradient (CG) method, the resulting algorithm is called the conjugate gradient–FFT (CG-FFT) method.

**复杂度 | Complexity:**
- 每次迭代的CPU时间为 $O(N \log N)$
- 内存需求为 $O(N)$

CPU time per iteration is of $O(N \log N)$ and the memory requirement is of $O(N)$.

### 16.5.2 数值结果 | Numerical Results

**公司馈电微带天线阵列 | Corporate-Fed Microstrip Antenna Array:**

| 阵列规模 | 未知数 | 每次迭代CPU时间 | 迭代次数 | 存储 |
|----------|--------|-----------------|----------|------|
| Array size | Unknowns | CPU time per iteration | Number of iterations | Storage |
| $8 \times 4$ | 118,073 | 11.6 s | 313 | 18 MB |
| $8 \times 4$ | 118,073 | 11.6 s | 599 | 18 MB |
| $8 \times 8$ | 495,044 | 97.81 s | 425 | 65 MB |
| $8 \times 8$ | 495,044 | 97.81 s | 1,070 | 65 MB |

---

## 16.6 自适应积分方法（AIM）| The Adaptive Integral Method

### 16.6.1 基本原理 | Basic Principle

CG-FFT方法需要均匀离散以利用Green函数的平移不变性。这限制了方法对复杂几何结构的适用性，并对弯曲边界产生阶梯近似。

The CGFFT method requires a uniform discretization to make use of the translational invariance of the Green's functions. This limits the applicability of the method to complex geometries and results in a staircase approximation for curved boundaries.

AIM的开发是为了解除这一限制。AIM的基本原理是将三角基函数转换到规则Cartesian网格，然后利用FFT进行矩阵-向量乘法。

The AIM is developed to lift this restriction. The basic principle of this method is to translate the triangular basis function onto a regular Cartesian grid and then utilize FFT to carry out the matrix-vector multiplication.

**阻抗矩阵分解 | Impedance Matrix Decomposition:**

$$\mathbf{Z} = \mathbf{Z}^{(approx)} + \mathbf{Z}^{(residual)} \tag{16.41}$$

只有当基函数和测试函数非常接近时，$Z^{(residual)}$ 才有显著值，使残差矩阵非常稀疏。

Note that only when $\mathbf{\Lambda}_i$ and $\mathbf{\Lambda}_j$ are very close does $Z_{ij}^{(residual)}$ have an appreciable value, which makes the residual matrix $\mathbf{Z}^{(residual)}$ very sparse.

---

## 16.7 本章小结 | Summary

本章介绍了多层微带问题的全波分析：

This chapter presented the full-wave analysis of multilayer microstrip problems:

1. **Green函数评估**：使用离散复镜像法（DCIM）高效评估多层介质的Green函数，包括表面波贡献的递归提取。
   Green's function evaluation: Efficient evaluation using DCIM with recursive extraction of surface-wave contributions.

2. **高阶MOM**：使用高阶插值矢量基函数和曲线性离散，提高收敛效率。
   Higher-order MOM: Using higher-order interpolatory vector basis functions and curvilinear discretization.

3. **快速频率扫描**：AWE技术可实现宽频带的快速频率响应计算。
   Fast frequency sweep: AWE enables rapid frequency response calculation over a broad band.

4. **大规模问题**：CG-FFT和AIM方法将计算复杂度从 $O(N^2)$ 和 $O(N^2)$ 降低到 $O(N \log N)$ 和 $O(N)$。
   Large-scale problems: CG-FFT and AIM reduce computational complexity from $O(N^2)$ to $O(N \log N)$ and $O(N)$.

数值例子验证了所提公式的准确性和能力，包括微带贴片天线、分支线耦合器、环形功率分配器、螺旋电感器和大型微带天线阵列。

Numerical examples demonstrated the accuracy and capability of the proposed formulations, including microstrip patch antennas, branch line couplers, annular-ring power dividers, spiral inductors, and large-scale microstrip antenna arrays.
