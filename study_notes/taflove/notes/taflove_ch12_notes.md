---
chapter: 12
title: "Bodies of Revolution"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, T. Jurgens, D. B. Davidson, R. W. Ziolkowski"
raw_size: 47,704 bytes
---

# Chapter 12: Bodies of Revolution (BOR-FDTD)
> **中英双语版**

> 旋转体（BOR-FDTD）

## 12.1 Introduction
> 引言

For rotationally symmetric (axisymmetric) structures, FDTD can exploit the azimuthal symmetry to reduce a 3D problem to a set of 2D problems. The fields are expanded in a Fourier series in the azimuthal angle $\phi$:
> 对于旋转对称（轴对称）结构，FDTD 可以利用方位角对称性将三维问题简化为一组二维问题。场量按方位角 $\phi$ 展开为傅里叶级数：
$$
\mathbf{E}(\rho, \phi, z, t) = \sum_{m=-\infty}^{\infty} \mathbf{e}_m(\rho, z, t) e^{jm\phi}
$$
$$
\mathbf{H}(\rho, \phi, z, t) = \sum_{m=-\infty}^{\infty} \mathbf{h}_m(\rho, z, t) e^{jm\phi}
$$
where $m$ is the azimuthal mode index. Each mode $m$ is decoupled from the others, reducing a full 3D FDTD simulation to a 2D grid in $(\rho, z)$ — a computational savings of roughly $N_\phi$ (number of azimuthal grid points, typically 50-200).
> 其中 $m$ 为方位角模式指标。每个模式 $m$ 之间彼此解耦，将一个完整的三维 FDTD 仿真简化为 $(\rho, z)$ 平面上的二维网格——计算量大致节省 $N_\phi$ 倍（方位角网格点数，通常为 50-200）。

## 12.2 Field Expansion in Cylindrical Coordinates
> 柱坐标下的场展开

Maxwell's curl equations in cylindrical $(\rho, \phi, z)$ for a single mode $m$:
> 对于单个模式 $m$，柱坐标下的麦克斯韦旋度方程：

**Ampère's law**:
> **安培定律**：
$$
\epsilon\frac{\partial e_\rho}{\partial t} + \sigma e_\rho = \frac{jm}{\rho} h_z - \frac{\partial h_\phi}{\partial z}
$$
$$
\epsilon\frac{\partial e_\phi}{\partial t} + \sigma e_\phi = \frac{\partial h_\rho}{\partial z} - \frac{\partial h_z}{\partial \rho}
$$
$$
\epsilon\frac{\partial e_z}{\partial t} + \sigma e_z = \frac{1}{\rho}\frac{\partial(\rho h_\phi)}{\partial\rho} - \frac{jm}{\rho} h_\rho
$$

**Faraday's law**:
> **法拉第定律**：
$$
-\mu\frac{\partial h_\rho}{\partial t} = \frac{jm}{\rho} e_z - \frac{\partial e_\phi}{\partial z}
$$
$$
-\mu\frac{\partial h_\phi}{\partial t} = \frac{\partial e_\rho}{\partial z} - \frac{\partial e_z}{\partial \rho}
$$
$$
-\mu\frac{\partial h_z}{\partial t} = \frac{1}{\rho}\frac{\partial(\rho e_\phi)}{\partial\rho} - \frac{jm}{\rho} e_\rho
$$

Each mode $m$ has 6 field components in $(\rho, z)$ space, compared to the full 3D Yee grid's $N_\phi$ azimuthal cells.
> 每个模式 $m$ 在 $(\rho, z)$ 空间中有 6 个场分量，而完整三维 Yee 网格需要 $N_\phi$ 个方位角网格单元。

### Mode Significance
> 模式的物理意义

| $m$ | Physical Meaning | Examples |
|-----|-----------------|----------|
| $m$ | 物理含义 | 示例 |
| $m=0$ | Monopole/TEM | Conical horn, monopole, coaxial feed |
| | 单极子/TEM | 锥形喇叭、单极子、同轴馈电 |
| $m=\pm1$ | Dipole | Half-wave dipole on axis, TE11 circular waveguide |
| | 偶极子 | 轴上半波偶极子、TE11 圆形波导 |
| $m=\pm2$ | Quadrupole | Higher-order waveguide modes, quadrupole antennas |
| | 四极子 | 高阶波导模式、四极天线 |
| $|m|>1$ | Higher-order | Corrugated horns, mode converters |
| | 高阶 | 波纹喇叭、模式转换器 |

## 12.3 Off-Axis Difference Equations
> 离轴差分方程

### 12.3.1 Ampère's Law for $e_\rho$
> $e_\rho$ 的安培定律

Using a contour-path integral in the $\phi$-$z$ plane (Fig. 12.2):
> 在 $\phi$-$z$ 平面使用回路路径积分（图 12.2）：
$$
\epsilon \frac{\partial e_\rho}{\partial t} = \frac{1}{\rho}\frac{\partial h_z}{\partial\phi} - \frac{\partial h_\phi}{\partial z}
$$

The $e_\rho$ component is separated into cosine ($u$) and sine ($v$) parts. After integration:
> $e_\rho$ 分量分为余弦 ($u$) 和正弦 ($v$) 部分。积分后：
$$
\epsilon(\rho_0, z_2) \frac{\partial e_{\rho,u}}{\partial t} = \frac{m}{\rho_0} h_{z,v} - \frac{h_{\phi,u}(z_2) - h_{\phi,u}(z_1)}{\Delta z}
$$
$$
\epsilon(\rho_0, z_2) \frac{\partial e_{\rho,v}}{\partial t} = -\frac{m}{\rho_0} h_{z,u} - \frac{h_{\phi,v}(z_2) - h_{\phi,v}(z_1)}{\Delta z}
$$

### 12.3.2-12.3.4 Further Components
> 其他分量

The full set of 12 update equations (6 E-field + 6 H-field, each with $u$ and $v$ components) is given in (12.19)-(12.30).
> 完整的 12 个更新方程（6 个电场 + 6 个磁场，各有 $u$ 和 $v$ 分量）详见 (12.19)-(12.30)。

## 12.4 On-Axis Difference Equations ($\rho = 0$)
> 轴上差分方程

At $\rho = 0$, the $1/\rho$ singularities require special treatment.
> 在 $\rho = 0$ 处，$1/\rho$ 奇异性需要特殊处理。

### 12.4.1 $e_z$ on the z-Axis
> $z$ 轴上的 $e_z$

For mode $m = 0$: $h_\rho(0, z) = 0$ on axis. The $e_z$ update uses L'Hôpital's rule:
> 对于模式 $m = 0$：轴上 $h_\rho(0, z) = 0$。$e_z$ 更新使用洛必达法则：
$$
\epsilon \frac{\partial e_z}{\partial t}\bigg|_{\rho=0} = \lim_{\rho\to 0} \frac{1}{\rho}\frac{\partial(\rho h_\phi)}{\partial\rho} = 2\frac{\partial h_\phi}{\partial\rho}\bigg|_{\rho=0}
$$

### 12.4.2-12.4.3 Axis Conditions
> 轴条件

For $m = \pm 1$, the azimuthal fields at $\rho = 0$ satisfy:
> 对于 $m = \pm 1$，$\rho = 0$ 处的方位角场满足：
$$
e_{\rho,u}(0,z) = e_{\phi,v}(0,z), \quad e_{\rho,v}(0,z) = -e_{\phi,u}(0,z)
$$

## 12.5 Numerical Stability
> 数值稳定性

The BOR-FDTD CFL condition is similar to the 2D Cartesian case:
> BOR-FDTD 的 CFL 条件与二维笛卡尔情况类似：
$$
\Delta t \leq \frac{1}{c\sqrt{(\Delta\rho_{\min})^{-2} + (\Delta z_{\min})^{-2}}}
$$

For cells near the axis ($\rho \to 0$), the azimuthal cell size $\rho\Delta\phi \to 0$, imposing a stricter limit for large $m$:
> 对于靠近轴的网格单元，方位角网格尺寸 $\rho\Delta\phi \to 0$，对大 $m$ 模式施加更严格的限制：
$$
\Delta t \leq \frac{\rho_{\min}\Delta\phi_{\min}}{c \cdot |m|}
$$

## 12.6 PML for BOR
> BOR 的 PML 实现

The uniaxial PML (UPML) is implemented in cylindrical coordinates with the stretching variables:
> 单轴 PML 在柱坐标中实现，使用拉伸变量：
$$
s_\rho = \kappa_\rho + \frac{\sigma_\rho}{j\omega\epsilon_0}, \quad s_z = \kappa_z + \frac{\sigma_z}{j\omega\epsilon_0}
$$

## 12.7 Application to Particle Accelerator Physics
> 在粒子加速器物理中的应用

BOR-FDTD is extensively used in accelerator cavity modeling:
> BOR-FDTD 广泛用于加速器腔体建模：
1. **RF cavity resonant frequency and Q-factor**: Eigenmode extraction for accelerating cavities
   > **射频腔谐振频率和 Q 值**：加速腔的本征模提取
2. **Wakefield computation**: Beam-induced fields following a charged particle bunch
   > **尾场计算**：带电粒子束团后的感应场
3. **Coupler design**: Input/output coupler optimization
   > **耦合器设计**：输入/输出耦合器优化

For wakefield analysis, the source term (charged particle beam) is added:
> 对于尾场分析，加入源项（带电粒子束）：
$$
\epsilon\frac{\partial e_z}{\partial t} = \frac{1}{\rho}\frac{\partial(\rho h_\phi)}{\partial\rho} - \frac{jm}{\rho} h_\rho - J_{z,\text{beam}}
$$
where $J_{z,\text{beam}}$ represents the beam current density.
> 其中 $J_{z,\text{beam}}$ 为束流电流密度。

## 12.8 Summary
> 总结

Key advantages of BOR-FDTD:
> BOR-FDTD 的关键优势：
- **2D computational domain** for 3D axisymmetric problems
  > 三维轴对称问题的**二维计算域**
- **Natural handling** of on-axis singularity via limiting formulas
  > 通过极限公式**自然处理**轴上奇异性
- **Mode-by-mode solution** allowing independent analysis of each $m$
  > **逐模式求解**，允许独立分析每个 $m$
- **Wakefield capability** by including beam current source terms
  > **尾场能力**，通过添加束流源项

Limitations:
> 局限性：
- Only applicable to **rotationally symmetric** structures
  > 仅适用于**旋转对称**结构
- Mode truncation errors if high-$m$ modes are significant
  > 若高 $m$ 模式显著则存在模式截断误差
- Stricter CFL for large $m$ near the axis
  > 靠近轴的大 $m$ 模式 CFL 条件更严格

BOR-FDTD remains the method of choice for axisymmetric antenna, waveguide, and accelerator cavity modeling.
> BOR-FDTD 仍然是轴对称天线、波导和加速器腔体建模的首选方法。
