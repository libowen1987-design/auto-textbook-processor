---
title: "Ch4: Finite-Difference Time-Domain Method"
book: "Sheng & Song, Essentials of Computational Electromagnetics (2012)"
chapter: 4
pages: "213-248"
weight: 4
topics:
  - Yee grid
  - PML perfectly matched layer
  - Surface treatment
  - Dispersive media
  - Lumped elements
  - TF/SF total-field/scattered-field
  - Comparison with MoM and FEM
notes_version: "1.1"
---

# Chapter 4: Finite-Difference Time-Domain Method | 时域有限差分法

> **中英双语版**

The **finite-difference time-domain method (FDTD)** directly discretizes the **time-domain partial differential form of Maxwell's equations** using finite differences. The Yee scheme interleaves E and H components in 3D space and time, forming "interlinked arrays of Faraday's Law and Ampere's Law contours".
**时域有限差分法（FDTD）** 直接用有限差分离散**麦克斯韦方程组的时域偏微分形式**。Yee 格式在三维空间和时间中交错排列 E 和 H 分量，形成"法拉第定律和安培定律回路的互联阵列"。

---

## 4.1 Scattering from Three-Dimensional Objects | 三维目标散射

### 4.1.1 FDTD Solution Scheme | FDTD 求解方案

**Domain truncation | 域截断**:
1. **Differential-equation-based ABCs** (e.g., Mur ABC): approximate outgoing wave equation（微分方程吸收边界条件）
2. **Absorbing-material-based ABCs** (e.g., PML): lossy material surrounding the domain（有耗材料吸收边界）

**Total-Field/Scattered-Field (TF/SF) technique | 总场/散射场技术**:
- **Center region**: total field $\mathbf{E}_{total} = \mathbf{E}_{inc} + \mathbf{E}_{sc}$（中心区：总场）
- **Surrounding region**: scattered field only（周围区：只有散射场）
- **Connection boundary**: injects the incident plane wave（连接边界：注入入射平面波）

**Why TF/SF? | 为什么用 TF/SF？**
In shadow regions, scattered field has opposite phase to incident — total field near zero. Minor errors in scattered field cause large relative error → total field formulation preferred.
在阴影区散射场与入射场反相——总场近零。散射场的小误差导致大相对误差→倾向总场公式。

### 4.1.2 Perfectly Matched Layers (PML) | 完美匹配层

PML (Berenger, 1994) uses **complex coordinate stretching** for exponential attenuation without reflection.
PML 使用**复坐标拉伸**实现无反射指数衰减。

**Design principle | 设计原理**: Apply local Wilcox series expansion to scattered field at inner PML boundary.
对 PML 内边界上的散射场应用局部 Wilcox 级数展开。

**Complex coordinate transformation | 复坐标变换**:
$$
\tilde{w} = s_w w,\quad w > 0,\quad s_w = \kappa_w + \frac{\sigma_w}{j\omega\epsilon_0} \tag{4.2}
$$

**Coordinate stretching operator | 坐标拉伸算子**:
$$
\nabla \rightarrow \bar{\nabla} = \hat{x}\frac{1}{s_x}\frac{\partial}{\partial x} + \hat{y}\frac{1}{s_y}\frac{\partial}{\partial y} + \hat{z}\frac{1}{s_z}\frac{\partial}{\partial z} \tag{4.5}
$$

**Effective constitutive parameters | 有效本构参数**:
$$
\bar{\bar{\epsilon}}_r = \bar{\bar{\mu}}_r = \hat{x}\hat{x}L_x + \hat{y}\hat{y}L_y + \hat{z}\hat{z}L_z \tag{4.18}
$$
$$
L_x = \frac{s_y s_z}{s_x},\quad L_y = \frac{s_z s_x}{s_y},\quad L_z = \frac{s_x s_y}{s_z} \tag{4.19}
$$

**Stretching factors | 拉伸因子**:
$$
s_x = \kappa_x + \frac{\sigma_x}{j\omega\epsilon_0},\quad s_y = \kappa_y + \frac{\sigma_y}{j\omega\epsilon_0},\quad s_z = \kappa_z + \frac{\sigma_z}{j\omega\epsilon_0} \tag{4.20}
$$

**Auxiliary Differential Equation (ADE) method | 辅助微分方程法**:
Introduce auxiliary variables $D_x = \epsilon \frac{s_z}{s_x} E_x$ etc. to avoid convolution.
引入辅助变量避免卷积运算。

**PML parameter profile (Gedney) | PML 参数分布**:
$$
\sigma_z(z) = \sigma_{\max} \left( \frac{z - z_0}{d} \right)^m,\quad m=4 \tag{4.31}
$$
$$
\sigma_{\max} = \frac{m+1}{150 \pi \sqrt{\epsilon_r} \Delta} \tag{4.32}
$$

### 4.1.3 Yee Discretizing Scheme | Yee 离散格式

**Spatial grid**: Each E component surrounded by 4 H components; each H surrounded by 4 E components. This allows central-difference approximation of curl operations.
**空间网格**：每个 E 分量被 4 个 H 分量环绕；每个 H 被 4 个 E 分量环绕。这使旋度运算可用中心差分近似。

**Leapfrog scheme | 跳蛙格式**: E and H defined at interleaved half-time steps.
E 和 H 定义在交错的半时间步上。

**Update for $D_x$** (semi-implicit form, Eq. 4.36):
$$
D_x|^{n+1}_{i+1/2,j,k} = \frac{2\epsilon\kappa_y - \sigma_y\Delta_t}{2\epsilon\kappa_y + \sigma_y\Delta_t} D_x|^{n}_{i+1/2,j,k} + \frac{2\epsilon\Delta_t}{2\epsilon\kappa_y + \sigma_y\Delta_t} \left( \frac{H_z|^{n+1/2}_{i+1/2,j+1/2,k} - H_z|^{n+1/2}_{i+1/2,j-1/2,k}}{\Delta_y} - \frac{H_y|^{n+1/2}_{i+1/2,j,k+1/2} - H_y|^{n+1/2}_{i+1/2,j,k-1/2}}{\Delta_z} \right)
$$

**Update for $E_x$ from $D_x$** (Eq. 4.38), and magnetic field updates (Eq. 4.39-4.40) follow analogously from Faraday's law with PML.
$E_x$ 从 $D_x$ 更新和磁场更新类似地从含 PML 的法拉第定律得到。

---

## 4.2 Surface Treatment | 表面处理

### 4.2.1 Curved Surface Treatment | 曲面处理

**Staircase approximation problem | 阶梯近似问题**: Standard FDTD uses rectangular grid → curved surfaces approximated by staircase → numerical error.
标准 FDTD 用矩形网格，曲面被阶梯化近似，导致数值误差。

**Treatment methods | 处理方法**:
1. **Subcell techniques**: fine mesh near surface（亚网格技术：表面附近精细网格）
2. **Contour-path FDTD**: redefine contour for intersected cells（轮廓路径 FDTD：为交叉单元重新定义轮廓）
3. **Physical smoothing / Conformal FDTD**: modify update equations for cut cells（物理平滑/共形 FDTD：修改切割单元的更新方程）

### 4.2.2 Thin Material Layer Treatment | 薄材料层处理

For layers thinner than one cell, derive analytical transmission/reflection coefficients and incorporate as boundary conditions.
对于比一个网格还薄的层，导出解析透射/反射系数并作为边界条件加入。

---

## 4.3 Dispersive Media | 色散介质

### 4.3.1 Frequency-Dependent Media | 频变介质

Time-domain constitutive relations become convolutions. Common models:
时域本构关系变为卷积。常见模型：
- **Lorentz**: $\epsilon(\omega) = \epsilon_\infty + \sum_p \frac{\omega_p^2}{\omega_0^2 - \omega^2 - j\omega\delta}$
- **Drude** (metals): $\epsilon(\omega) = \epsilon_\infty - \frac{\omega_p^2}{\omega(\omega + j\gamma)}$

### 4.3.2 ADE Treatment for Debye Media | 德拜介质的 ADE 处理

Introduce auxiliary polarization $\mathbf{P}$ and solve $\frac{d\mathbf{P}}{dt} + \frac{1}{\tau} \mathbf{P} = \frac{\epsilon_s - \epsilon_\infty}{\tau} \mathbf{E}$. Combined with Maxwell's equations yields dispersive update equations.
引入辅助极化变量 $\mathbf{P}$，与麦克斯韦方程组联立得到色散更新方程。

---

## 4.4 Lumped Elements | 集总元件

### 4.4.1 Circuit Element Connection | 电路元件连接

Lumped elements connected via interface condition: $\hat{n} \times (\mathbf{E}_2 - \mathbf{E}_1) = \mathbf{J}_s$.
集总元件通过界面条件连接。电压关联切向电场，电流关联周围磁场。

### 4.4.2 Thin Wire Treatment | 细导线处理

Thin wire (radius << cell size): 1D transmission line along wire + coupling to 3D FDTD grid via E-field BC.
细导线：沿导线的一维传输线 + 通过电场边界条件耦合到三维 FDTD 网格。

---

## 4.5 Comparison of MoM, FEM, and FDTD | MoM、FEM 与 FDTD 对比

| Feature | MoM | FEM | FDTD |
|---------|-----|-----|------|
| **Domain** | Open (surface) | Interior/tetrahedral | Volume/hexahedral |
| **Matrix type** | Dense (full) | Sparse | Explicit update |
| **Solution** | Direct/iterative | Direct/iterative | Time-marching |
| **Excitation** | Frequency domain | Frequency domain | Broadband (pulse) |
| **Mesh** | Surface patches | Tetrahedral (unstructured) | Rectangular (structured) |
| **Suitable for** | Thin wires, surfaces | Complex inhomogeneous media | Simple geometries |
| **Memory** | $O(N^2)$ | $O(N)$ | $O(N)$ |
| **Boundary** | Natural (Green's fn) | Artificial truncation | ABC/PML required |

**Key insights | 关键洞察：**
- MoM: most efficient for open-domain scattering from thin metallic structures（开放域薄金属结构散射最高效）
- FEM: excels for complex inhomogeneous dielectrics (arbitrary geometry)（复杂非均匀介质最优）
- FDTD: handles wideband problems naturally, fine mesh needed for curved surfaces（自然处理宽带问题，曲面需细网格）

**Hybrid approach rationale | 混合方法原理**: Combine strengths — e.g., FDTD for wideband regions + FEM for complex local structures.
结合各自优势——FDTD 用于宽带区 + FEM 用于复杂局部结构。

---

## Key Equations Summary | 关键方程总结

| Equation | Description | 说明 |
|----------|-------------|------|
| (4.1) | Wilcox series for PML | PML 的 Wilcox 级数 |
| (4.2) | Complex coordinate stretch | 复坐标拉伸 |
| (4.5) | Stretching operator | 拉伸算子 |
| (4.18)-(4.19) | Effective PML constitutive params | PML 有效本构参数 |
| (4.20) | Stretching factors | 拉伸因子 |
| (4.22) | ADE auxiliary D-field vars | ADE 辅助 D 场变量 |
| (4.36) | $D_x$ update with PML | 含 PML 的 D_x 更新 |
| (4.38) | $E_x$ from $D_x$ | E_x 从 D_x 得到 |
| (4.39)-(4.40) | $B_x$ and $H_x$ updates | B_x 和 H_x 更新 |
