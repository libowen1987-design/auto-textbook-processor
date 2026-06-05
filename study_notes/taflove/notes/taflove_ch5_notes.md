---
chapter: 5
title: Incident Wave Source Conditions
book: Computational Electrodynamics — The Finite-Difference Time-Domain Method (3rd Ed.)
author: Allen Taflove et al.
raw_size: 132,611 bytes
sections: 6
---

# Chapter 5: Incident Wave Source Conditions
> **中英双语版**

> 入射波源条件

## 5.1 Introduction
> 引言

A generic issue in FDTD modeling is how to accurately introduce electromagnetic wave excitations in a spatially compact manner.
> FDTD 建模中的一个基本问题是如何以空间紧凑的方式精确引入电磁波激励。

This chapter reviews four classes of compact wave sources:
> 本章回顾四类紧凑波源：
1. **Hard-sourced E and H fields** in 1D and 2D grids
   > 一维和二维网格中的**硬源电场和磁场**
2. **J and M current sources** in 3D lattices
   > 三维网格中的**J 和 M 电流源**
3. **Total-field / Scattered-field (TF/SF) formulation** for plane-wave excitation
   > 用于平面波激励的**总场/散射场公式**
4. **Waveguide sources**
   > **波导源**

> **Numerical Intuition:** Choosing the right source model is critical. A hard source is simple but causes spurious retroreflection at the source point. The TF/SF formulation is the workhorse for plane-wave scattering problems, enabling clean separation of incident and scattered fields with dynamic range exceeding 100 dB.
> **数值直觉：** 正确选择源模型至关重要。硬源简单但会在源点引起伪反射。TF/SF 公式是平面波散射问题的主力，可实现入射场和散射场的干净分离，动态范围超过 100 dB。

---

## 5.2 Pointwise E and H Hard Sources in One Dimension
> 一维点状电场和磁场硬源

A **hard source** assigns a desired time function to specific E or H components, independent of anything else. For a 1D grid:
> **硬源** 将期望的时间函数赋给特定的 E 或 H 分量，与其他因素无关。

$$E_z^{n}(i_s) = E_0 \sin(2\pi f_0 n\Delta t) \tag{5.1}$$

### Problem: Retroreflection
> 问题：回反射

As the reflected scattered wave returns to $i_s$, the hard source causes nonphysical retroreflection — it behaves like a PEC.
> 当反射的散射波返回 $i_s$ 时，硬源会引起非物理的回反射——其行为类似于理想导体。

**Solution for pulsed sources**: After the pulse decays, revert the source point to the standard Yee update.
> **脉冲源的解决方案**：脉冲衰减后将源点恢复为标准 Yee 更新。

---

## 5.4 J and M Current Sources in Three Dimensions
> 三维 J 和 M 电流源

In 3D, sources are implemented as electric and magnetic current densities $\mathbf{J}$ and $\mathbf{M}$:
> 在三维中，源作为电、磁流密度实现：
$$\nabla \times \mathbf{H} = \epsilon \frac{\partial\mathbf{E}}{\partial t} + \sigma\mathbf{E} + \mathbf{J}_{\text{src}}$$
$$\nabla \times \mathbf{E} = -\mu \frac{\partial\mathbf{H}}{\partial t} - \sigma^*\mathbf{H} - \mathbf{M}_{\text{src}}$$

---

## 5.6 The Total-Field / Scattered-Field (TF/SF) Technique
> 总场/散射场技术

### 5.6.1 Core Ideas
> 核心思想

Based on linearity of Maxwell's equations:
> 基于麦克斯韦方程的线性性质：
$$\mathbf{E}_{\text{tot}} = \mathbf{E}_{\text{inc}} + \mathbf{E}_{\text{scat}}$$
$$\mathbf{H}_{\text{tot}} = \mathbf{H}_{\text{inc}} + \mathbf{H}_{\text{scat}} \tag{5.24}$$

The Yee lattice is zoned into two regions:
> Yee 网格分为两个区域：
- **Region 1 (inner):** Total fields stored — contains the scattering structure
  > **区域 1（内部）：** 存储总场——包含散射结构
- **Region 2 (outer):** Scattered fields stored — terminated by ABC
  > **区域 2（外部）：** 存储散射场——由 ABC 截断

Separated by a **nonphysical virtual connecting surface** that generates the incident wave.
> 由生成入射波的**非物理虚拟连接面**分隔。

**Key features:**
> **关键特性：**
1. Arbitrary incident wave — any waveform, angle, polarization
   > 任意入射波——任意波形、角度、极化
2. Outgoing scattered waves enter Region 2 freely
   > 向外传播的散射波自由进入区域 2
3. ABC operates on scattered fields (smoother, lower amplitude)
   > ABC 作用于散射场（更平滑、幅度更低）
4. Wide dynamic range — incident field subtracted out before ABC
   > 宽动态范围——在 ABC 前已减去入射场
5. NTFF transformation can be applied in the scattered-field region
   > NTFF 变换可在散射场区域应用

### 5.6.2 One-Dimensional Formulation
> 一维公式

Connecting condition at $i = i_0$: the finite-difference across the interface uses total-field on one side and scattered-field on the other, with an incident field correction term.
> 连接条件：界面上的有限差分在一边使用总场，另一边使用散射场，附加一个入射场修正项。

---

## 5.7 Two-Dimensional TF/SF Formulation
> 二维 TF/SF 公式

For 2D TM$_z$ ($E_z$, $H_x$, $H_y$), the TF/SF interface is a rectangular contour. Correction terms are applied cell-by-cell.
> 对于二维 TM$_z$，TF/SF 界面是一个矩形轮廓。逐网格单元施加修正项。

---

## 5.8 Three-Dimensional TF/SF Formulation
> 三维 TF/SF 公式

In 3D, the TF/SF interface is a rectangular box with six connecting surfaces requiring correction terms for tangential E and H components.
> 在三维中，TF/SF 界面是一个矩形盒子，六个连接面需要对切向 E 和 H 分量施加修正项。

---

## Audit Table
> 审计表

| Concept | Section | Key Equation |
|---------|---------|-------------|
| 概念 | 章节 | 关键方程 |
| Hard source / 硬源 | 5.2 | (5.1) |
| J/M current sources / 电流源 | 5.4 | (5.5) |
| TF/SF 1D / 一维总场散射场 | 5.6 | (5.24) |
| TF/SF 2D / 二维总场散射场 | 5.7 | — |
| TF/SF 3D / 三维总场散射场 | 5.8 | — |

> **Numerical Intuition:** The TF/SF formulation is the most important source technique in FDTD. It isolates the incident wave entirely to the inner region, allowing the ABCs to absorb only scattered fields. The TF/SF interface should be placed at least 10-20 cells from both the scatterer and the outer ABC boundary.
> **数值直觉：** TF/SF 公式是 FDTD 中最重要的源技术。它将入射波完全隔离在内部区域，使 ABC 仅吸收散射场。TF/SF 界面应至少距离散射体和外部 ABC 边界 10-20 个网格单元。
