# Fast Multipole Method and MLFMA in 2D / 二维快速多极子方法与多层快速多极子算法

> **中英双语版**

**Source:** Chew, *Fast and Efficient Algorithms in CEM*, Chapter 2 — Weng Cho Chew and Jiming Song
**来源：** Chew《计算电磁学中的快速高效算法》第2章

---

## 2.1 Introduction / 引言

The fast multipole method (FMM) and its multilevel extension (MLFMA) reduce the complexity of matrix-vector products in integral equation solvers from O(N²) to O(N log N). In this chapter, we present the 2D derivation to illustrate the core mathematical ideas without the complexity of 3D expansion functions.
快速多极子方法(FMM)及其多层扩展(MLFMA)将积分方程求解器中矩阵-矢量乘积的复杂度从O(N²)降低到O(N log N)。本章给出二维推导，以展示核心数学思想而不涉及三维展开函数的复杂性。

The key feature of FMM is to diagonalize the translation matrix. This diagonalization was first given by Rokhlin [1].
FMM的关键特征是对角化传输矩阵。这一对角化由Rokhlin首次给出[1]。

---

## 2.2 Introduction to Fast Multipole in 2D / 二维快速多极子方法简介

### 2.2.1 A 2D MOM Problem / 二维MOM问题

Consider the scattering problem of a metallic cylinder by an Eᶻ polarized electromagnetic wave / 考虑金属圆柱对Eᶻ极化电磁波的散射问题：

$$
\int dS' g_0(\rho - \rho') J_z(\rho') = -E_z^{\text{inc}} \tag{2.1}
$$

where / 其中：

$$
g_0(\rho - \rho') = \frac{i}{4} H_0^{(1)}(k|\rho - \rho'|) \tag{2.2}
$$

is the 2D Green's function. J_z(ρ) is the induced current on the surface / 是二维格林函数。J_z(ρ)为散射体表面上的感应电流。

Using pulse basis functions and point matching (collocation), we obtain / 使用脉冲基函数和点匹配（配置法），得到：

$$
\sum_j A_{ji} a_i = b_j, \quad j = 1, \ldots, N \tag{2.3}
$$

where / 其中：

$$
A_{ji} = \int_{\Delta_i} dS' g_0(\rho_j - \rho') \tag{2.4}
$$

### 2.2.2 Factorization of the Green's Function / 格林函数的因子分解

The key to FMM is to factorize the 2D Green's function using the addition theorem / FMM的关键是利用加法定理将二维格林函数因子分解：

$$
H_0^{(1)}(k|\rho_j - \rho_i|) = \sum_{l=-\infty}^{\infty} H_l^{(1)}(k\rho_{JJ'}) e^{il(\phi_{JJ'} - \pi)} J_l(k\rho_{J'i}) e^{-il\phi_{J'i}} \tag{2.18}
$$

where / 其中：

$$
\rho_j - \rho_i = \rho_{JJ'} - (\rho_{J'i} - \rho_{jJ}) \tag{2.19}
$$

This factorization can be written compactly as / 该因子分解可简洁地写为：

$$
A_{ji} = \mathbf{V}_{jJ} \cdot \mathbf{T}_{JJ'} \cdot \mathbf{V}_{J'i} \tag{2.20}
$$

where $\mathbf{V}$ aggregates sources to a group center, $\mathbf{T}$ translates between group centers, and another $\mathbf{V}$ disaggregates to observers. The translation matrix $\mathbf{T}$ is diagonal / 其中 $\mathbf{V}$ 将源聚合到组中心，$\mathbf{T}$ 在组中心之间传输，另一个 $\mathbf{V}$ 将信息分发到观察点。传输矩阵 $\mathbf{T}$ 是对角矩阵。

### 2.2.3 Two-Level Fast Multipole Algorithm / 二级快速多极子算法

In the two-level FMM, the scatterer is divided into groups. For elements within the same group or neighboring groups (near-field), direct computation is used. For far-field groups, the factorized Green's function is employed / 在二级FMM中，散射体被划分为组。同组或相邻组内的元素（近场）使用直接计算。远场组使用因子分解的格林函数。

A matrix-vector product is evaluated as / 矩阵-矢量乘积计算为：

$$
\mathbf{b} \cdot \mathbf{x} \approx \sum_{i=1}^N \sum_{j \in \text{far}} \mathbf{V}_{Jj} \cdot \mathbf{T}_{JJ'} \cdot \mathbf{V}_{J'i} x_i + \sum_{i=1}^N \sum_{j \in \text{near}} A_{ji} x_i \tag{2.37}
$$

Complexity / 复杂度：O(N^(3/2)) for the two-level FMM / 二级FMM为O(N^(3/2))。

---

## 2.3 Motivation for Multilevel Method / 多层方法的动机

### 2.3.1 Factorization of the Green's Function / 格林函数的多层因子分解

A multilevel extension recursively factorizes the Green's function. Using the addition theorem repeatedly / 多层扩展递归地对格林函数进行因子分解。重复使用加法定理：

$$
H_0^{(1)}(k r_{ji}) = \boldsymbol{\beta}_{jJ_1} \cdot \boldsymbol{\beta}_{J_1 J_2} \cdot \boldsymbol{\alpha}_{J_2 I_2} \cdot \boldsymbol{\beta}_{I_2 I_1} \cdot \boldsymbol{\beta}_{I_1 i} \tag{2.59}
$$

where / 其中：

$$
[\beta_{1,l}]_l = J_l(k\rho_{jJ_1}) e^{il(\phi_{jJ_1} - \pi)} \tag{2.60}
$$

$$
[\beta_{J_1 J_2}]_{l,m} = J_{l-m}(k\rho_{J_1 J_2}) e^{-i(l-m)\phi_{J_1 J_2}} \tag{2.61}
$$

$$
[\alpha_{J_2 I_2}]_{m,n} = H_{m-n}^{(1)}(k\rho_{J_2 I_2}) e^{-i(m-n)\phi_{J_2 I_2}} \tag{2.62}
$$

The translation matrices $\beta$ and $\alpha$ are diagonal. To achieve O(N log N) complexity, interpolation and anterpolation operators must be inserted between levels [24].
传输矩阵 $\beta$ 和 $\alpha$ 是对角的。为达到O(N log N)复杂度，必须在层之间插入插值和反插值算子[24]。

---

## 2.4 The Multilevel Fast Multipole Algorithm / 多层快速多极子算法

MLFMA facilitates the matrix-vector product in O(N log N) operations for sparse scatterers and in O(N) for densely packed scatterers / MLFMA在稀疏散射体中实现O(N log N)操作的矩阵-矢量乘积，在密堆积散射体中实现O(N)。

Key steps / 关键步骤：

1. **Discretization / 离散化**：The scatterer is discretized with MoM; elements are ~0.1λ to 0.2λ / 散射体用MoM离散；单元约0.1λ到0.2λ。
2. **Spatial gridding / 空间网格化**：Space is gridded into boxes; smallest boxes contain a few elements / 空间被网格化为小盒子；最小盒子包含少量单元。
3. **Tree structure / 树结构**：In 2D, quad-tree; empty boxes are pruned / 二维中用四叉树；空盒子被剪枝。
4. **Far-field computation / 远场计算**：Use factorized Green's function / 使用因子分解的格林函数。
5. **Near-field computation / 近场计算**：Traditional MoM for neighbors / 邻居使用传统MoM。

### 2.4.1 The Aggregation Process / 聚合过程

Radiation patterns of sources in boxes are computed from the lowest level upward / 从最低层向上计算盒子中源的辐射方向图：

$$
\mathbf{b}_{I_1} = \tilde{\boldsymbol{\beta}}_{I_1 i} \cdot \mathbf{J}_i \tag{2.68}
$$

$$
\mathbf{b}_{I_2} = \tilde{\boldsymbol{\beta}}_{I_2 I_1} \cdot \mathbf{b}_{I_1} \tag{2.69}
$$

### 2.4.2 Translation and Disaggregation / 传输与分发

Outgoing waves from source boxes are converted to incoming waves at the target level, then disaggregated downward / 源盒的出射波在目标层被转换为入射波，然后向下分发。

---

## 2.5 Interpolation Error / 插值误差

In MLFMA, interpolation operators are used between levels for radiation patterns. The interpolation error must be controlled to maintain solution accuracy. The number of multipole modes needed depends on the box size and desired accuracy / 在MLFMA中，辐射方向图层间使用插值算子。必须控制插值误差以保持解的精度。所需的多极子模式数取决于盒子大小和期望精度。

---

## 2.6 FMM and Group Theory / FMM与群论

FMM can be understood in the context of group theory where the translation operators form a representation of the Euclidean group. The diagonalization of the translation operator corresponds to passing to a basis where the group action is diagonal / FMM可以在群论的背景下理解，其中传输算子形成欧几里得群的表示。传输算子的对角化对应于过渡到群作用对角的基。

---

## 2.7 Conclusion / 结论

The 2D FMM and MLFMA reduce computational complexity from O(N²) to O(N log N) by diagonalizing the translation operator. The key insight is the factorization of the Green's function using the addition theorem, enabling a multilevel tree-based algorithm / 二维FMM和MLFMA通过对角化传输算子将计算复杂度从O(N²)降低到O(N log N)。关键见解是使用加法定理对格林函数进行因子分解，从而实现了基于多级树的算法。

---

## References / 参考文献

[1] V. Rokhlin, "Rapid solution of integral equations of scattering theory in two dimensions," *J. Comput. Phys.*, vol. 86, pp. 414–439, 1990.
[4] C. C. Lu and W. C. Chew, "A multilevel algorithm for solving a boundary integral equation of wave scattering," *Microwave Opt. Technol. Lett.*, vol. 7, pp. 466–470, 1994.
[5] J. M. Song and W. C. Chew, "Multilevel fast-multipole algorithm for solving combined field integral equations of electromagnetic scattering," *Microwave Opt. Technol. Lett.*, vol. 10, pp. 14–19, 1995.
[8] R. F. Harrington, *Field Computation by Moment Methods*, Macmillan, 1968.
[24] W. C. Chew et al., *Fast and Efficient Algorithms in Computational Electromagnetics*, Artech House, 2001.
