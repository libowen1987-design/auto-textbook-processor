---
chapter: 10
title: "Local Subcell Models of Fine Geometrical Features"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, M. Celuch-Marcysiak, S. Hagness"
raw_size: 111,907 bytes
---

# Chapter 10: Local Subcell Models of Fine Geometrical Features
> **中英双语版**

> 精细几何特征的局部亚网格模型

## 10.1 Introduction
> 引言

Two fundamental approaches exist for handling fine features:
> 处理精细特征有两种基本方法：

1. **Global mesh refinement**: Use graded cells throughout — maintains accuracy but can dominate simulation time.
   > **全局网格细化**：全程使用渐变网格——保持精度但可能主导仿真时间。
2. **Local subcell models**: Use a uniform Cartesian mesh and approximate fine details in local cells.
   > **局部亚网格模型**：使用均匀笛卡尔网格并在局部网格中近似精细细节。

**Core insight**: Deform Faraday/Ampère contours to follow actual geometry, obtaining specialized update equations without global refinement.
> **核心见解**：将法拉第/安培回路变形以贴合实际几何形状，获得专门的更新方程而无需全局网格细化。

### Chapter Roadmap
> 章节路线图

| Section | Topic | Key Application |
|---------|-------|-----------------|
| 章节 | 主题 | 关键应用 |
| §10.3 | Diagonal split-cell & average-properties | PEC surfaces, material interfaces / PEC 表面、材料界面 |
| §10.4 | Narrow slot model | Air gaps in PEC shields / PEC 屏蔽体中的空气缝隙 |
| §10.5 | Thin wire model | Wire antennas / 线天线 |
| §10.6 | Conformal curved surface model | Curved PEC/dielectric boundaries / 弯曲 PEC/介质边界 |
| §10.7 | Thin material sheet model | Resistive paint / 电阻漆 |
| §10.8 | Surface impedance BC | Skin effect / 趋肤效应 |
| §10.9 | Thin coatings on PEC | Radar-absorbing layers / 雷达吸波层 |
| §10.10 | Relativistic moving boundaries | Doppler analysis / 多普勒分析 |

## 10.2 Basis of Contour-Path FDTD
> 回路路径 FDTD 的基础

Departing from Yee's pointwise derivative interpretation, the contour-path approach starts with the integral forms:
> 与 Yee 的点状导数解释不同，回路路径法从积分形式出发：
$$
\oint_C \mathbf{E} \cdot d\mathbf{l} = -\mu \frac{d}{dt} \iint_S \mathbf{H} \cdot d\mathbf{S}
$$
$$
\oint_C \mathbf{H} \cdot d\mathbf{l} = \epsilon \frac{d}{dt} \iint_S \mathbf{E} \cdot d\mathbf{S} + \iint_S \sigma \mathbf{E} \cdot d\mathbf{S}
$$

## 10.3 The Simplest Contour-Path Subcell Models
> 最简单的回路路径亚网格模型

### 10.3.1 Diagonal Split-Cell Model for PEC Surfaces
> PEC 表面的对角分裂网格模型

For curved PEC boundaries, the staircase model is replaced by a diagonal split-cell model, using Faraday's law at a cell split diagonally.
> 对于弯曲 PEC 边界，用对角分裂网格模型替代阶梯模型，在对角分裂的网格上应用法拉第定律。

### 10.3.2 Average Properties Model for Material Surfaces
> 材料表面的平均特性模型

For a material interface cutting a cell, Faraday's law uses weighted average of $\mu_1$ and $\mu_2$ where $0 \le f \le 1$ is the fraction of cell area in Medium #1.
> 对于穿过网格的材料界面，法拉第定律使用 $\mu_1$ 和 $\mu_2$ 的加权平均值，$f$ 为介质 1 占网格面积的比例。

## 10.4 Narrow Slot Model
> 窄缝隙模型

For a slot of width $g \ll \Delta$ in a PEC screen, three Faraday's law contours are used — away from slot, at slot opening, and within slot.
> 对于 PEC 屏中宽度 $g \ll \Delta$ 的缝隙，使用三个法拉第定律回路——远离缝隙、缝隙开口处和缝隙内部。

**Validation**: A $\lambda_0/10$ resolution contour-path model agreed with very high-resolution MoM for gaps as small as $\lambda_0/1000$.
> **验证**：$\lambda_0/10$ 分辨率的回路路径模型与极高分辨率 MoM 一致，即使缝隙小至 $\lambda_0/1000$。

## 10.5 Thin Wire Model
> 细线模型

For a wire of radius $a \ll \Delta$, near-field distributions are assumed static ($1/r$ variation). The model uses specialized update equations for looping H-components and radial E-components.
> 对于半径 $a \ll \Delta$ 的导线，假设近场分布为静态（$1/r$ 变化）。模型对环绕的 H 分量和径向 E 分量使用专门的更新方程。

**Validation**: A 21-cell thin-wire dipole model achieved better accuracy than the original 41-cell model.
> **验证**：21 网格细线偶极子模型的精度超过原 41 网格模型。

## 10.6 Locally Conformal Models of Curved Surfaces
> 弯曲表面的局部共形模型

### 10.6.1 Yu-Mittra PEC Model
> Yu-Mittra PEC 模型

The contour-path update uses deformed contour lengths outside the PEC while keeping the full cell area for the magnetic flux integral.
> 回路路径更新使用 PEC 外部的变形回路长度，同时保持完整网格面积用于磁通量积分。

**Advantage**: At 8 cells/$\lambda$, contour-path FDTD matches staircased FDTD at 32 cells/$\lambda$ — a **64:1** storage reduction and **256:1** runtime reduction in 3D.
> **优势**：8 单元/波长时，回路路径 FDTD 相当于 32 单元/波长的阶梯法——三维下存储减少 **64:1**，运行时间减少 **256:1**。

### 10.6.3 Yu-Mittra Dielectric Model
> Yu-Mittra 介质模型

For a cell intersected by a dielectric interface, effective permittivity uses linear weighting of $\epsilon_1$ and $\epsilon_2$.
> 对于介质界面穿过的网格，有效介电常数使用 $\epsilon_1$ 和 $\epsilon_2$ 的线性加权。

## 10.7 Maloney-Smith Thin Material Sheet Model
> Maloney-Smith 薄材料片模型

For a sheet of thickness $d < \Delta/2$, normal E-field is split into free-space and inside-sheet updates; tangential components use average-properties.
> 对于厚度 $d < \Delta/2$ 的薄片，法向电场分裂为自由空间和薄片内部更新；切向分量使用平均特性。

## 10.8 Surface Impedance Boundary Conditions (SIBC)
> 表面阻抗边界条件

For a lossy conductor with $\sigma_2 \gg \omega \epsilon_2$, the Leontovich impedance BC:
> 对于 $\sigma_2 \gg \omega \epsilon_2$ 的有耗导体，Leontovich 阻抗边界条件：
$$Z_s(\omega) = \sqrt{\frac{j\omega \mu_0}{\sigma_2}}$$

### 10.8.2 Convolution-Based SIBC
> 基于卷积的 SIBC

Full convolution form using Prony's method + recursive summation avoids volumetric modeling of lossy conductors.
> 使用 Prony 方法 + 递归求和的完整卷积形式，避免了对有耗导体的体积建模。

## 10.10 Relativistic Motion of PEC Boundaries
> PEC 边界的相对论运动

For a PEC boundary moving at relativistic velocity $\mathbf{v}$, the boundary condition is $\hat{n} \times \mathbf{E}' = 0$ where $\mathbf{E}'$ is the field in the rest frame.
> 对于以相对论速度 $\mathbf{v}$ 运动的 PEC 边界，边界条件为 $\hat{n} \times \mathbf{E}' = 0$，$\mathbf{E}'$ 为静止系中的场。

**Validation**: A moving PEC wall at $v = 0.1c$ showed frequency shifts accurate to within 0.5% of the relativistic Doppler formula.
> **验证**：以 $v = 0.1c$ 运动的 PEC 壁的频率偏移精度在相对论多普勒公式的 0.5% 以内。

## 10.11 Summary and Discussion
> 总结与讨论

| Subcell Model | Key Idea | Accuracy Gain |
|--------------|----------|---------------------------|
| 亚网格模型 | 核心思想 | 精度增益 |
| Diagonal split-cell / 对角分裂网格 | Diagonal PEC contour | ~2× |
| Thin wire / 细线模型 | $1/r$ static field assumption | 2-4× |
| Conformal PEC (Yu-Mittra) / 共形 PEC | Deformed edges, full area | 4× |
| SIBC / 表面阻抗 | Avoids skin-depth mesh | 存储减少 50× |

### Key Takeaways
> 关键要点

1. Contour-path FDTD achieves 2-4× resolution advantage per dimension over staircasing.
   > 回路路径 FDTD 每维比阶梯法具有 2-4 倍的分辨率优势。
2. Thin-wire models with $1/r$ near-field assumptions accurately capture input impedance.
   > 细线模型精确捕捉输入阻抗。
3. Surface impedance BCs avoid volumetric modeling of lossy conductors.
   > 表面阻抗 BC 避免了有耗导体的体积建模。
4. The Yu-Mittra conformal technique is the most practical for general curved PEC structures.
   > Yu-Mittra 共形技术对一般弯曲 PEC 结构最实用。
