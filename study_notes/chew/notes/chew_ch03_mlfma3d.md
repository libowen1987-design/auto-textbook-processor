# FMM and MLFMA in 3D and Fast Illinois Solver Code / 三维FMM、MLFMA与快速伊利诺伊求解器代码

> **中英双语版**

**Source:** Chew, *Fast and Efficient Algorithms in CEM*, Chapter 3 — Jiming Song and Weng Cho Chew
**来源：** Chew《计算电磁学中的快速高效算法》第3章

---

## 3.1 Introduction / 引言

We have discussed the 2D FMM and MLFMA in Chapter 2. In this chapter, we extend these ideas to 3D and present the Fast Illinois Solver Code (FISC).
我们在第2章中讨论了二维FMM和MLFMA。在章，我们将这些思想扩展到三维，并介绍快速伊利诺伊求解器代码(FISC)。

---

## 3.2 Three-Dimensional FMM and MLFMA / 三维FMM和MLFMA

### 3.2.1 Integral Equations and the Method of Moments / 积分方程与矩量法

For conducting objects, the electric field integral equation (EFIE) is given by / 对于导电物体，电场积分方程(EFIE)为：

$$
\int \hat{t} \cdot \overline{\mathbf{G}}(r, r') \cdot \mathbf{J}(r') dS' = \frac{4\pi i}{\omega\mu} \hat{t} \cdot \mathbf{E}^i(r) \tag{3.1}
$$

where / 其中：

$$
\overline{\mathbf{G}}(r, r') = \left(\mathbf{I} - \frac{1}{k^2} \nabla \nabla'\right) g(r, r'), \quad g(r, r') = \frac{e^{ikR}}{R}, \quad R = |r - r'| \tag{3.2-3.3}
$$

For closed conducting objects, the magnetic field integral equation (MFIE) is / 对于闭合导电物体，磁场积分方程(MFIE)为：

$$
2\pi \hat{t} \cdot \mathbf{J}(r) - \hat{t} \cdot \hat{n} \times \nabla \times \int dS' g(r, r') \mathbf{J}(r') = 4\pi \hat{t} \cdot \hat{n} \times \mathbf{H}^i(r) \tag{3.4}
$$

The combined field integral equation (CFIE) is used to avoid internal resonances / 使用组合场积分方程(CFIE)避免内部谐振：

$$
\alpha \text{EFIE} + (1 - \alpha) \frac{i}{k} \text{MFIE} \tag{3.5}
$$

### 3.2.2 Diagonalization of the Translation Operator / 传输算子的对角化

In 3D, the scalar Green's function can be expanded using the plane wave expansion / 在三维中，标量格林函数可以使用平面波展开：

$$
g(r, r') = \frac{e^{ik|r - r'|}}{|r - r'|} = \frac{i}{2\pi} \int_0^{2\pi} \int_0^\pi e^{i\mathbf{k} \cdot (r - r')} \sin\theta d\theta d\phi \tag{3.21}
$$

More precisely, using the addition theorem in 3D / 更精确地，使用三维加法定理：

$$
\frac{e^{ik|r_j - r_i|}}{|r_j - r_i|} = \frac{ik}{4\pi} \int d^2\hat{k} e^{i\mathbf{k} \cdot (r_j - r_{J})} T_L(\hat{k}, r_{JJ'}) e^{i\mathbf{k} \cdot (r_{J'} - r_i)} \tag{3.26}
$$

where $T_L$ is the diagonal translation operator, and the integral is over the Ewald sphere / 其中 $T_L$ 是对角传输算子，积分在Ewald球面上进行。

### 3.2.3 FMM Matrix-Vector Product / FMM矩阵-矢量乘积

The matrix-vector product is decomposed into three steps / 矩阵-矢量乘积分解为三步：

1. **Aggregation / 聚合**：Compute outgoing plane wave expansions for each group / 计算每组的出射平面波展开
2. **Translation / 传输**：Translate outgoing waves to incoming waves between well-separated groups / 在良好分离的组之间将出射波转换为入射波
3. **Disaggregation / 分发**：Receive incoming waves and compute fields / 接收入射波并计算场

---

## 3.3 Multilevel Fast Multipole Algorithm (MLFMA) / 多层快速多极子算法

To implement 3D MLFMA, the object is enclosed in a large cube, partitioned recursively into eight smaller cubes (oct-tree). The finest cube edge length is about 0.25λ.
为了实现三维MLFMA，将物体包围在一个大立方体中，递归地划分为八个更小的立方体（八叉树）。最细的立方体边长约为0.25λ。

We use L to denote the number of levels. Level L is the finest, level 0 is the coarsest. Nonempty cubes are recorded using tree-structured data [26,27].
用L表示层数。L层为最细层，0层为最粗层。使用树结构数据记录非空立方体[26,27]。

The basic algorithm for matrix-vector multiply has two sweeps / 矩阵-矢量乘积的基本算法有两个扫描过程：

**First sweep (aggregation) / 第一扫描（聚合）：** Construct outgoing wave expansions for each nonempty cube from level L to 2. At level L, expansions are computed by combining all sources in the cube. From level L−1 to 2, expansions are computed from children using shifting and interpolation.
从L层到2层为每个非空立方体构建出射波展开。在L层，通过组合立方体中所有源计算展开。从L−1层到2层，利用子立方体的展开通过偏移和插值计算。

The outgoing wave expansion for a coarser level l−1 is / 较粗层l−1的出射波展开为：

$$
V_{l-1}^i(\hat{k}) = e^{-i\mathbf{k} \cdot \mathbf{r}_{m'}^{l-1}} V_{s_{m'}^l}^i(\hat{k}) \tag{3.33}
$$

Interpolation is needed to go from K_l values to K_{l-1} values / 需要插值从K_l值到K_{l-1}值。

**Second sweep (translation + disaggregation) / 第二扫描（传输+分发）：** Construct local incoming wave expansions for well-separated cubes from level 2 to L. At level 2, local expansions are constructed by translating outgoing expansions from well-separated cubes. From levels 3 to L, expansions consist of contributions from the parent's well-separated cubes plus new well-separated cubes.
从2层到L层为良好分离的立方体构建局部入射波展开。在2层，通过传输来自良好分离立方体的出射波展开来构建局部展开。从3层到L层，展开包括来自父立方体的良好分离立方体贡献加上新的良好分离立方体。

---

## 3.4 Error Analysis in FMM and MLFMA / FMM和MLFMA的误差分析

The error in FMM/MLFMA arises from truncation of the multipole expansion. The number of multipole terms K must be chosen such that / FMM/MLFMA的误差来自多极子展开的截断。必须选择多极子项数K使得：

- Accuracy of the translation is maintained / 保持传输精度
- The computational cost is minimized / 计算成本最小化

The required number of terms for a given accuracy ε is / 对于给定精度ε所需的项数为：

$$
K \approx kd + c \cdot (k d)^{1/3} \cdot (\log \epsilon)^{2/3} \tag{3.51}
$$

where d is the box size and c is a constant / 其中d为盒子大小，c为常数。

---

## 3.5 Large Scale Computing / 大规模计算

### 3.5.1 Block Diagonal Preconditioner / 块对角预条件器

The CPU time for iterative methods is proportional to the number of iterations. A block diagonal preconditioner improves spectral properties / 迭代方法的CPU时间与迭代次数成正比。块对角预条件器改善谱特性：

$$
\mathbf{A} \cdot \mathbf{x} = (\mathbf{A}_0 + \mathbf{A}_1) \cdot \mathbf{x} + \mathbf{A}_2 \cdot \mathbf{x} \tag{3.57}
$$

where $\mathbf{A}_0$ is block diagonal, $\mathbf{A}_1$ accounts for near interactions, and $\mathbf{A}_2$ accounts for far interactions computed via MLFMA / 其中 $\mathbf{A}_0$ 为块对角，$\mathbf{A}_1$ 处理近相互作用，$\mathbf{A}_2$ 是通过MLFMA计算的远相互作用。

### 3.5.2 Initial Guess for Monostatic RCS / 单站RCS的初始猜测

For monostatic RCS at different angles, using the solution from the previous angle with phase correction as the initial guess significantly reduces iterations / 对于不同角度的单站RCS，使用前一个角度的解经相位校正作为初始猜测可显著减少迭代次数。

$$
\tilde{\mathbf{J}}(r) = \mathbf{J}(r) e^{-i\mathbf{k}_i \cdot r} \tag{3.59}
$$

---

## 3.6 Fast Illinois Solver Code (FISC) / 快速伊利诺伊求解器代码

FISC is a parallel implementation of MLFMA for solving large-scale electromagnetic scattering problems. Key features / FISC是MLFMA的并行实现，用于求解大规模电磁散射问题。关键特性：

- Parallelization using MPI / 使用MPI进行并行化
- Handles problems with millions of unknowns / 处理百万级未知数的问题
- Application to radar cross section (RCS) computation / 应用于雷达截面(RCS)计算
- Demonstrated on targets like aircraft and ships / 在飞机、舰船等目标上得到验证

### 3.6.1 Parallel Implementation / 并行实现

FISC uses a distributed memory parallel architecture with dynamic load balancing. The oct-tree of MLFMA is distributed across processors / FISC使用分布式内存并行架构和动态负载平衡。MLFMA的八叉树分布在各个处理器上。

### 3.6.2 Numerical Examples / 数值示例

FISC has been used to compute RCS of complex targets with millions of unknowns. Results demonstrate O(N log N) complexity and good parallel scalability / FISC已被用于计算具有百万未知数的复杂目标的RCS。结果展示了O(N log N)复杂度和良好的并行可扩展性。

---

## 3.7 Conclusions / 结论

The 3D MLFMA reduces the complexity of matrix-vector products to O(N log N). Combined with parallel computing, it enables the solution of electromagnetic scattering problems with millions of unknowns / 三维MLFMA将矩阵-矢量乘积的复杂度降低到O(N log N)。结合并行计算，它使得求解具有百万未知数的电磁散射问题成为可能。

---

## References / 参考文献

[22] J. R. Mautz and R. F. Harrington, "H-field, E-field, and combined-field solutions for conducting bodies of revolution," *AEÜ*, vol. 32, pp. 157–164, 1978.
[23] R. F. Harrington, *Field Computation by Moment Methods*, Macmillan, 1968.
[26] J. M. Song and W. C. Chew, "Multilevel fast-multipole algorithm for solving combined field integral equations of electromagnetic scattering," *Microwave Opt. Technol. Lett.*, vol. 10, pp. 14–19, 1995.
[27] J. M. Song, C. C. Lu, and W. C. Chew, "Multilevel fast multipole algorithm for electromagnetic scattering by large complex objects," *IEEE Trans. Antennas Propagat.*, vol. 45, pp. 1488–1493, 1997.
