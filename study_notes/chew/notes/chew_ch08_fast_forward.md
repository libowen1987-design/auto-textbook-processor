# Chapter 8: Fast Forward and Inverse Methods for Objects in Layered Media
# 埋地物体的快速前向与逆散射方法

**Author:** Weng C. Chew and Junqi Shi

---

## 8.1 Introduction | 引言

This chapter addresses the analysis and inverse scattering problems for objects buried in layered media. Applications include ground penetrating radar (GPR), land mine detection, underground resource exploration, and sensing of underneath surface objects.

本章讨论埋地物体的分析和逆散射问题。应用包括探地雷达（GPR）、地雷探测、地下资源勘探和表面下方物体感应。

The presence of layered media complicates the problem because the Green's function is more complex than free-space case. The fast multipole method (FMM) and fast Illinois solver code (FISC) have been extended to handle layered medium Green's functions.

层状介质的存在使问题复杂化，因为格林函数比自由空间情况更复杂。快速多极子方法（FMM）和快速伊利诺伊求解器代码（FISC）已扩展以处理层状介质格林函数。

---

## 8.2 Formulation | 公式化

### 8.2.1 Physics of the Problem | 问题的物理

When an object is buried in layered media, the incident field on the object is modified by the presence of the layered medium. The scattered field is also affected by the layered medium on its path to the observation point.

当物体埋入层状介质时，入射到物体的场受到层状介质存在的影响。散射场在到达观察点的路径上也受层状介质影响。

The buried object can be characterized by its material properties contrast with the background medium. The goal of inverse scattering is to reconstruct the object's position, shape, and material properties from measured scattered field data.

埋地物体可以用与背景介质的材料特性对比来表征。逆散射的目标是从测量的散射场数据重建物体的位置、形状和材料特性。

### 8.2.2 Governing Equations | 控制方程

For an object with permittivity $\epsilon_2$ embedded in a half-space with permittivity $\epsilon_1$, the electric field integral equation (EFIE) for 2D TM case is:

对于嵌入介电常数 $\epsilon_1$ 半空间中的物体（介电常数 $\epsilon_2$），二维 TM 情况的电场积分方程（EFIE）为：

$$\mathcal{L} J = E^{inc}$$

where $\mathcal{L}$ involves the layered medium Green's function $G_1$ for the half-space:

其中 $\mathcal{L}$ 涉及半空间的层状介质格林函数 $G_1$：

$$\mathcal{L} J = k_2^2 \int_S G_1(r, r') J(r') ds'$$

The incident field in the presence of layered media is computed using reflection and transmission coefficients for the layered medium.

层状介质存在时的入射场使用层状介质的反射和透射系数计算。

---

## 8.3 Fast Multipole Method for Layered Media | 层状介质的快速多极子方法

### 8.3.1 Green's Function in Layered Media | 层状介质中的格林函数

The layered medium Green's function can be written using the discrete complex image method (DCIM):

层状介质格林函数可以使用离散复镜像方法（DCIM）写出：

$$G(\rho, z; \rho', z') = \frac{i}{4} H_0^{(1)}(k_1 \rho_{>}) \left[ e^{ik_1 z_<} + R e^{-ik_1 z_>}\right] + \text{complex images}$$

where $R$ is the reflection coefficient and complex images account for the layered structure effect.

其中 $R$ 是反射系数，复镜像解释层状结构效应。

### 8.3.2 Fast Multipole Representation | 快速多极表示

The fast multipole method represents the Green's function using addition theorem:

快速多极子方法使用加法定理表示格林函数：

$$G(r, r') \approx \sum_{l=0}^{L} \sum_{m=-l}^{l} \text{exp}(i k r_<) h_l^{(1)}(k r_>) Y_{lm}^*(\hat{r}') Y_{lm}(\hat{r})$$

For layered media, additional terms account for multiple reflections between layers.

对于层状介质，附加项解释层之间的多次反射。

The multilevel fast multipole algorithm (MLFMA) achieves $O(N \log N)$ complexity for matrix-vector products.

多级快速多极子算法（MLFMA）实现矩阵向量乘积的 $O(N \log N)$ 复杂度。

---

## 8.4 Forward Scattering Computation | 前向散射计算

The forward problem computes the scattered field given the object properties and location. Using FMM, the computational complexity is reduced to $O(N \log N)$ for $N$ unknowns.

前向问题给定物体特性和位置计算散射场。使用 FMM，计算复杂度降低到 $O(N \log N)$（$N$ 为未知数）。

The iterative solver (CG or GMRES) converges in fewer iterations due to the preconditioning effect of FMM.

由于 FMM 的预条件效应，迭代求解器（CG 或 GMRES）收敛所需迭代次数更少。

---

## 8.5 Inverse Scattering Formulation | 逆散射公式化

### 8.5.1 Data Model | 数据模型

Measured scattered field data at various receiver locations forms the data vector:

各处接收器位置测量的散射场数据形成数据向量：

$$\mathbf{d}^{obs} = \mathbf{d}^{calc}(\mathbf{m}) + \mathbf{\epsilon}$$

where $\mathbf{m}$ is the model parameter vector (object properties) and $\mathbf{\epsilon}$ is noise.

其中 $\mathbf{m}$ 是模型参数向量（物体特性），$\mathbf{\epsilon}$ 是噪声。

### 8.5.2 Optimization Approach | 优化方法

The inverse problem is posed as minimizing the data misfit:

逆散射问题表述为最小化数据拟合差：

$$\min_{\mathbf{m}} \Phi(\mathbf{m}) = \|\mathbf{d}^{obs} - \mathbf{d}^{calc}(\mathbf{m})\|^2 + \alpha R(\mathbf{m})$$

where $R(\mathbf{m})$ is a regularizer and $\alpha$ is the regularization parameter.

其中 $R(\mathbf{m})$ 是正则化项，$\alpha$ 是正则化参数。

### 8.5.3 Linearization | 线性化

Using Born approximation, the relationship between data and model is linearized:

使用玻恩近似，数据与模型之间的关系线性化为：

$$\Delta \mathbf{d} \approx \mathbf{J} \Delta \mathbf{m}$$

where $\mathbf{J}$ is the Jacobian (sensitivity) matrix.

其中 $\mathbf{J}$ 是雅可比（灵敏度）矩阵。

### 8.5.4 Iterative Inversion | 迭代反演

The distorted Born iterative method (DBIM) updates the object properties iteratively:

扭曲玻恩迭代方法（DBIM）迭代更新物体特性：

1. Start with initial guess $\mathbf{m}_0$
2. Compute scattered field with current model
3. Update model using data residual
4. Repeat until convergence

1. 从初始猜测 $\mathbf{m}_0$ 开始
2. 用当前模型计算散射场
3. 使用数据残差更新模型
4. 重复直到收敛

---

## 8.6 Fast Jacobian Calculation | 快速雅可比计算

### 8.6.1 Adjoint Field Method | 伴随场方法

The adjoint field method computes the Jacobian efficiently using one additional forward solve:

伴随场方法使用一次额外的正向求解高效计算雅可比：

$$\frac{\partial d_i}{\partial m_j} = \langle \mathbf{E}_j^{(s)}, \mathbf{E}_i^{(adj)} \rangle$$

where $\mathbf{E}_j^{(s)}$ is the scattered field from a unit dipole at location $j$, and $\mathbf{E}_i^{(adj)}$ is the adjoint field excited by the data residual at receiver $i$.

其中 $\mathbf{E}_j^{(s)}$ 是在位置 $j$ 处单位偶极子产生的散射场，$\mathbf{E}_i^{(adj)}$ 是由接收器 $i$ 处数据残差激励的伴随场。

### 8.6.2 Complexity Analysis | 复杂度分析

Using FMM, the forward solve is $O(N \log N)$. Computing the full Jacobian naively would be $O(N^2)$, but the adjoint method achieves $O(N \log N)$ per iteration.

使用 FMM，正向求解为 $O(N \log N)$。朴素计算完整雅可比为 $O(N^2)$，但伴随方法实现每次迭代 $O(N \log N)$。

---

## 8.7 Numerical Examples | 数值例子

### 8.7.1 Forward Scattering | 前向散射

Results for cylinders buried in half-space show good agreement between FMM solution and method of moments (MoM).

半空间中埋地柱体的结果，FMM 解与矩量法（MoM）有良好一致性。

The computational time savings are significant for large $N$.

对于大 $N$，计算时间节省显著。

### 8.7.2 Inverse Scattering | 逆散射

Reconstructed images of buried objects using DBIM show the method can recover object location and approximate size.

使用 DBIM 重建埋地物体的图像显示该方法可以恢复物体位置和近似尺寸。

Multiple frequency data improves resolution.

多频率数据提高分辨率。

---

## 8.8 Applications | 应用

### 8.8.1 Ground Penetrating Radar | 探地雷达

GPR survey data can be processed using these forward and inverse scattering techniques to locate and characterize buried objects.

GPR 勘测数据可以使用这些前向和逆散射技术处理，以定位和表征埋地物体。

The air-ground interface and soil properties affect the data and must be accounted for.

空气-地面界面和土壤特性影响数据，必须加以考虑。

### 8.8.2 Mine Detection | 地雷探测

Metal mines have high contrast compared to soil, making them detectable via electromagnetic methods.

金属地雷与土壤相比具有高对比度，使它们可通过电磁方法检测。

The forward solver helps design antenna systems and survey strategies.

前向求解器帮助设计天线系统和勘测策略。

---

## 8.9 Summary | 本章小结

This chapter discussed fast algorithms for forward and inverse scattering problems involving buried objects in layered media.

本章讨论了涉及层状介质中埋地物体的前向和逆散射问题的快速算法。

**Key contributions:**

主要贡献：

1. **Fast multipole method for layered media:** Extension of FMM to handle the more complex Green's function in stratified media.

   **层状介质的快速多极子方法：** 扩展 FMM 以处理分层介质中更复杂的格林函数。

2. **Efficient Jacobian calculation:** Adjoint field method achieves $O(N \log N)$ complexity per iteration, enabling practical inverse scattering.

   **高效雅可比计算：** 伴随场方法实现每次迭代 $O(N \log N)$ 复杂度，使实际逆散射成为可能。

3. **Distorted Born iterative method:** DBIM enables quantitative reconstruction of buried object properties.

   **扭曲玻恩迭代方法：** DBIM 实现埋地物体特性的定量重建。

4. **Applications to GPR and mine detection:** Demonstrated utility for real-world sensing problems.

   **GPR 和地雷探测应用：** 展示了对实际传感问题的实用性。

5. **Complex image representation:** Discrete complex image method provides efficient representation of layered medium Green's function.

   **复镜像表示：** 离散复镜像方法提供层状介质格林函数的有效表示。