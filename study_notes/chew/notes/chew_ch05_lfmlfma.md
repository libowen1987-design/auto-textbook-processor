# Multilevel Fast Multipole Algorithm at Very Low Frequencies / 极低频的多层快速多极子算法

> **中英双语版**

**Source:** Chew, *Fast and Efficient Algorithms in CEM*, Chapter 5 — Junsheng Zhao and Weng Cho Chew
**来源：** Chew《计算电磁学中的快速高效算法》第5章

---

## 5.1 Introduction / 引言

For solving general 2D and 3D electromagnetic problems, the method of moments (MoM) generates a full matrix equation. Conventional methods require O(N²) storage and O(N³) or O(N²) operations. A number of techniques have been proposed to expedite the matrix-vector multiplication / 对于求解通用二维和三维电磁问题，矩量法(MoM)生成满矩阵方程。传统方法需要O(N²)存储和O(N³)或O(N²)操作。已经提出了多种加速矩阵-矢量乘积的技术。

MLFMA is efficient, error controllable, and flexible. However, the standard MLFMA using the diagonalized form of the translation operator breaks down at very low frequencies because the Bessel functions become exponentially small or large, causing numerical overflow/underflow / 标准MLFMA使用传输算子的对角化形式，但在极低频下会失效，因为贝塞尔函数变得指数级小或大，导致数值上溢/下溢。

This chapter presents a low-frequency MLFMA (LF-MLFMA) that works at arbitrarily low frequencies by normalizing the multipole expansions appropriately / 本章介绍一种通过适当归一化多极子展开而在任意低频下工作的低频MLFMA(LF-MLFMA)。

---

## 5.2 2D Multilevel Fast Multipole Algorithm at Very Low Frequencies / 极低频的二维多层快速多极子算法

### 5.2.1 Core Equation of the 2D Undiagonalized Dynamic MLFMA / 二维非对角化动态MLFMA的核心方程

In the 2D MLFMA, the object cross-section is enclosed in a large square, partitioned recursively into four smaller squares (quad-tree). The smallest squares depend on the current distribution / 在二维MLFMA中，物体截面被包围在一个大正方形中，递归地划分为四个更小的正方形（四叉树）。最小的正方形取决于电流分布。

Using the addition theorem for Hankel functions / 使用汉克尔函数的加法定理：

$$
H_0^{(1)}(k|\mathbf{r}_j - \mathbf{r}_i|) = \sum_{m=-M}^{M} H_m^{(1)}(k\rho_{JJ'}) e^{im(\phi_{JJ'} - \pi)} \sum_{n=-N}^{N} J_n(k\rho_{J'i}) e^{-in\phi_{J'i}} \tag{5.3}
$$

In matrix form / 矩阵形式：

$$
\mathbf{A} = \mathbf{V}_{jJ} \cdot \mathbf{T}_{JJ'} \cdot \mathbf{V}_{J'i} \tag{5.6}
$$

### 5.2.2 Normalization for Low Frequencies / 低频的归一化

At low frequencies, $k\rho \ll 1$, the Hankel function $H_m^{(1)}(k\rho)$ becomes very large or very small depending on the order m. The solution is to normalize the multipole amplitudes / 在低频下，$k\rho \ll 1$，汉克尔函数 $H_m^{(1)}(k\rho)$ 根据阶数m变得非常大或非常小。解决方案是归一化多极子幅度。

The normalized outgoing and incoming wave amplitudes are defined as / 归一化的出射波和入射波幅度定义为：

$$
\tilde{b}_m = \frac{b_m}{J_m(k\rho_0)}, \quad \tilde{c}_m = \frac{c_m}{H_m^{(1)}(k\rho_0)} \tag{5.15}
$$

where $\rho_0$ is a reference distance / 其中 $\rho_0$ 为参考距离。

### 5.2.3 The 2D LF-MLFMA Algorithm / 二维LF-MLFMA算法

The LF-MLFMA uses the normalized form of the aggregation and disaggregation steps. The translation matrices are also normalized to maintain numerical stability / LF-MLFMA使用聚合和分发步骤的归一化形式。传输矩阵也进行了归一化以保持数值稳定性。

**Complexity / 复杂度**：The LF-MLFMA achieves O(N log N) or O(N) complexity for low-frequency problems / LF-MLFMA在低频问题中实现O(N log N)或O(N)复杂度。

---

## 5.3 3D Low-Frequency MLFMA / 三维低频MLFMA

### 5.3.1 Scaling of the Multipole Expansion / 多极子展开的缩放

In 3D, the scalar Green's function is expanded using spherical harmonics / 在三维中，标量格林函数使用球谐函数展开：

$$
\frac{e^{ik|r - r'|}}{|r - r'|} = ik \sum_{l=0}^{\infty} \sum_{m=-l}^{l} j_l(kr_<) h_l^{(1)}(kr_>) Y_{lm}(\theta, \phi) Y_{lm}^*(\theta', \phi') \tag{5.29}
$$

At very low frequencies, the spherical Bessel functions $j_l(kr)$ and Hankel functions $h_l^{(1)}(kr)$ exhibit extreme scaling behavior / 在极低频下，球贝塞尔函数 $j_l(kr)$ 和汉克尔函数 $h_l^{(1)}(kr)$ 表现出极端的缩放行为。

### 5.3.2 Normalization Scheme / 归一化方案

The outgoing multipole coefficients $a_{lm}$ and incoming coefficients $b_{lm}$ are scaled / 出射多极子系数 $a_{lm}$ 和入射系数 $b_{lm}$ 被缩放：

$$
\tilde{a}_{lm} = \frac{a_{lm}}{j_l(k\rho_0)}, \quad \tilde{b}_{lm} = \frac{b_{lm}}{h_l^{(1)}(k\rho_0)} \tag{5.35}
$$

### 5.3.3 Matrix Rotation Technique / 矩阵旋转技术

To save storage, the matrix rotation technique is applied to the 3D LF-MLFMA. The translation matrices along the z-direction for the low-frequency case exhibit symmetries that can be exploited to reduce memory requirements / 为节省存储，将矩阵旋转技术应用于三维LF-MLFMA。低频情况下沿z方向的传输矩阵展示出对称性，可加以利用以降低内存需求。

### 5.3.4 Loop-Tree Basis Functions / 环-树基函数

At very low frequencies, the electric field integral equation (EFIE) suffers from the low-frequency breakdown problem where the vector and scalar potentials have different frequency scalings. The loop-tree basis decomposition separates the solenoidal (loop) and non-solenoidal (tree) parts of the current, resolving this issue / 在极低频下，电场积分方程(EFIE)遭受低频崩溃问题，矢势和标势具有不同的频率缩放。环-树基分解将电流分为螺线管（环）和非螺线管（树）两部分，解决了这一问题。

---

## 5.4 Conclusions / 结论

In this chapter, the LF-MLFMA in 2D and 3D with computational complexity O(N log N) for very low-frequency problems is developed. The LF-MLFMA can be used not only independently for low-frequency cases, but also to solve large-scale structures with rapidly varying areas when merged with the dynamic MLFMA described in Chapters 2 and 3. A loop-tree based method that is also efficient for iterative solvers is described / 本章开发了在极低频问题中具有O(N log N)计算复杂度的二维和三维LF-MLFMA。LF-MLFMA不仅可以独立用于低频情况，而且当与第2章和第3章描述的动态MLFMA合并时，可求解具有快速变化区域的大尺度结构。还描述了一种对迭代求解器也高效的基于环-树的方法。

The combination of the dynamic MLFMA and LF-MLFMA provides a broadband algorithm capable of solving problems from static to microwave frequencies / 动态MLFMA和LF-MLFMA的结合提供了一种宽带算法，能够求解从静态到微波频率的问题。

---

## References / 参考文献

[1] R. F. Harrington, *Field Computation by Moment Methods*, Krieger, 1982.
[2] R. L. Wagner and W. C. Chew, "A study of wavelets for the solution of electromagnetic integral equations," *IEEE Trans. Antennas Propagat.*, vol. 43, pp. 802–810, 1995.
[8] V. Rokhlin, "Rapid solution of integral equations of classical potential theory," *J. Comput. Phys.*, vol. 60, pp. 187–207, 1985.
[10] J. M. Song and W. C. Chew, "Multilevel fast-multipole algorithm for solving combined field integral equations of electromagnetic scattering," *Microwave Opt. Technol. Lett.*, vol. 10, pp. 14–19, 1995.
[27] J. S. Zhao and W. C. Chew, "Three-dimensional multilevel fast multipole algorithm at very low frequencies," *IEEE Trans. Magnetics*, vol. 37, pp. 3242–3246, 2001.
[31] J. S. Zhao and W. C. Chew, "Applying LF-MLFMA to solve complex PEC structures," *Microwave Opt. Technol. Lett.*, vol. 28, pp. 21–25, 2001.
