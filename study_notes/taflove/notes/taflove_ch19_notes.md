---
chapter: 19
title: "Hybrid FDTD-Finite Element Methods"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, R. Lee, A. C. Cangellaris"
raw_size: 104,976 bytes
---

# Chapter 19: Hybrid FDTD-Finite Element Methods
> **中英双语版**

> 混合 FDTD-有限元法

## 19.1 Introduction
> 引言

FDTD excels in homogeneous regions; FEM excels on unstructured meshes for complex boundaries. **Hybrid FDTD-FEM** combines both: FDTD in the bulk, FEM near boundaries/fine features.
> FDTD 在均匀区域中表现出色；有限元法在非结构化网格上处理复杂边界具有优势。**混合 FDTD-FEM** 结合了两者：在大块区域使用 FDTD，在边界或精细特征附近使用 FEM。

## 19.2 FETD (Finite-Element Time-Domain)
> 时域有限元法

### Vector Finite Elements (Edge Elements)
> 矢量有限元（棱边元）

Whitney edge basis functions for tetrahedral/hexahedral elements:
> 四面体/六面体单元的 Whitney 棱边基函数：
$$
\mathbf{N}_i(\mathbf{r}) = \lambda_{i1} \nabla \lambda_{i2} - \lambda_{i2} \nabla \lambda_{i1}
$$

where $\lambda_{ij}$ are barycentric coordinates. Edge elements:
> 其中 $\lambda_{ij}$ 为重心坐标。棱边元具有以下特性：
- Enforce tangential continuity
  > 强制切向连续性
- Allow natural material discontinuities
  > 自然处理材料不连续性
- Eliminate spurious modes
  > 消除伪模

### FETD Formulation
> FETD 公式

Weak form of Maxwell's equations:
> 麦克斯韦方程组的弱形式：
$$
\left[ \mathbf{T} \right] \frac{d^2 \mathbf{e}}{dt^2} + \left[ \mathbf{S} \right] \mathbf{e} + \text{boundary terms} = 0
$$

Mass matrix $T_{ij} = \iiint \epsilon \mathbf{N}_i \cdot \mathbf{N}_j dV$
> 质量矩阵 $T_{ij} = \iiint \epsilon \mathbf{N}_i \cdot \mathbf{N}_j dV$

Stiffness matrix $S_{ij} = \iiint \frac{1}{\mu} (\nabla \times \mathbf{N}_i) \cdot (\nabla \times \mathbf{N}_j) dV$
> 刚度矩阵 $S_{ij} = \iiint \frac{1}{\mu} (\nabla \times \mathbf{N}_i) \cdot (\nabla \times \mathbf{N}_j) dV$

Time-stepping via Newmark-beta scheme (unconditional stable option: $\beta \geq 1/4$).
> 时间步进采用 Newmark-beta 格式（无条件稳定选项要求 $\beta \geq 1/4$）。

## 19.3 Hybrid Coupling Approaches
> 混合耦合方法

### 19.3.1 Overlapping Domain Decomposition
> 重叠区域分解法

FEM region embedded within FDTD grid. Interface handled via:
> FEM 区域嵌入 FDTD 网格中。界面处理方式：
- Huygens' surface equivalence
  > 惠更斯表面等效原理
- Field interpolation between grids
  > 网格间的场值插值
- Stability maintained by implicit FEM time-step ≥ explicit FDTD time-step
  > 通过确保隐式 FEM 时间步长 ≥ 显式 FDTD 时间步长来维持稳定性

### 19.3.2 Non-Overlapping (Mortar) Methods
> 非重叠（Mortar）方法

FDTD and FEM domains meet at a common interface. Mortar elements enforce field continuity:
> FDTD 和 FEM 区域在公共界面上连接。Mortar 单元强制执行场连续性：
$$
\iint_{\Gamma} (\mathbf{E}_{\text{FDTD}} - \mathbf{E}_{\text{FEM}}) \cdot \mathbf{N}_m dS = 0
$$

### 19.3.3 Subgridding Hybrid
> 子网格混合法

FEM replaces the FDTD subgrid for highly irregular regions:
> FEM 替代 FDTD 子网格用于高度不规则区域：
- Better accuracy than Cartesian subgridding for curved features
  > 对于弯曲结构，精度优于直角坐标子网格
- No staircase error at curved boundaries
  > 弯曲边界处无阶梯误差
- Computational overhead of FEM-to-FDTD interpolation
  > 存在 FEM 到 FDTD 插值的计算开销

## 19.4 Stability
> 稳定性

The hybrid method inherits stability if:
> 混合方法的稳定性继承条件：
- FDTD region satisfies its CFL condition
  > FDTD 区域满足其 CFL 条件
- FEM region uses unconditionally stable Newmark scheme
  > FEM 区域使用无条件稳定的 Newmark 格式
- Coupling is energy-conserving (symmetric coupling matrices)
  > 耦合为能量守恒型（对称耦合矩阵）

Stability limit dominated by FDTD's CFL and the FEM element sizes at the interface.
> 稳定性极限由 FDTD 的 CFL 条件和界面处 FEM 单元的尺寸共同决定。

## 19.5 Applications
> 应用领域

### Microwave Components
> 微波器件
- Waveguide filters with rounded corners (FEM at corners, FDTD in waveguide)
  > 带圆角波导滤波器（圆角处用 FEM，波导主体用 FDTD）
- Microstrip patch antenna with curved edges (FEM near patch, FDTD in substrate)
  > 弯曲边缘微带贴片天线（贴片附近用 FEM，衬底用 FDTD）

### Scattering from Complex Targets
> 复杂目标散射
- Aircraft with antenna radome: FEM for radome, FDTD for free space
  > 带天线罩的飞行器：天线罩用 FEM，自由空间用 FDTD
- Coated targets: FEM for coating, FDTD elsewhere
  > 涂覆目标：涂层用 FEM，其余区域用 FDTD

### EMC/EMI
> 电磁兼容/电磁干扰
- Cable bundles in enclosures: FEM for cable cross-section, FDTD for enclosure
  > 机箱中的线缆束：线缆截面用 FEM，机箱主体用 FDTD

## Summary
> 总结

| Coupling Method | Accuracy | Stability | Implementation |
|----------------|----------|-----------|----------------|
| 耦合方法 | 精度 | 稳定性 | 实现难度 |
| Overlapping | 2nd order | Conditional | Moderate |
| 重叠法 | 二阶 | 条件稳定 | 中等 |
| Mortar (non-overlapping) | Spectral | Conditional | Complex |
| Mortar（非重叠） | 谱精度 | 条件稳定 | 复杂 |
| Subgrid hybrid | 2nd order | Conditional | Difficult |
| 子网格混合法 | 二阶 | 条件稳定 | 困难 |
