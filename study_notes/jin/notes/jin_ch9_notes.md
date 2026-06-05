---
title: "Chapter 9 — The Finite Element Method"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Weighted residual / variational formulation
  - Galerkin method, shape functions (1D, 2D, 3D)
  - Isoparametric elements
  - Edge-based vector elements (Whitney)
  - Sparse matrix assembly
  - FEM for waveguide, scattering, cavity problems
  - FEM-BEM, ABC, PML for open problems
---

# Chapter 9: The Finite Element Method | 第九章：有限元法

> **中英双语版**

## 9.1 Introduction | 引言

**Weighted residual / 加权余量:** $\langle \mathcal{L} \phi - f, w_j \rangle = 0$ for test functions $w_j$ / 对检验函数 $w_j$。

**Galerkin / 伽辽金法:** test functions = basis functions / 检验函数 = 基函数。

**1D Helmholtz example / 一维亥姆霍兹示例:**

$$
\int_\Omega \left( -\frac{d\phi}{dx}\frac{dw}{dx} + k^2 \phi w \right) dx = \int_\Omega f w \, dx
$$

## 9.2 Basis Functions | 基函数

**1D:** 线性 $N_i(x) = (x_{i+1} - x)/(x_{i+1} - x_i)$ 等。

**2D triangles / 二维三角形:** 面积坐标 $\zeta_1, \zeta_2, \zeta_3$。

**Edge elements (Whitney) / 棱边元（惠特尼）:** $\mathbf{N}_{ij} = \zeta_i \nabla \zeta_j - \zeta_j \nabla \zeta_i$ — 强制切向连续性。

## 9.3 Isoparametric Elements | 等参元

Geometric mapping $x = \sum N_i(\xi,\eta) x_i$ with same basis functions for geometry and field / 几何和场使用相同基函数的几何映射 $x = \sum N_i(\xi,\eta) x_i$。

## 9.4 Sparse System Assembly | 稀疏系统组装

Element matrices $\mathbf{K}^e$, load vectors $\mathbf{b}^e$ assembled into global system / 单元矩阵 $\mathbf{K}^e$、载荷向量 $\mathbf{b}^e$ 组装到全局系统中。

## 9.5 Applications | 应用

**Waveguide analysis / 波导分析:** 矢量有限元用于 $\mathbf{E}$ 或 $\mathbf{H}$，自然地施加无散条件。

**Scattering / 散射:** 有限元 + 边界积分 (FEM-BEM) 或 有限元 + PML。

**Cavity / 腔体:** 广义本征值问题 $\mathbf{K}\mathbf{x} = \lambda \mathbf{M}\mathbf{x}$。

---

## Audit / 审计

| Section / 节 | Topic / 主题 |
|---------|-------|
| 9.1 | 加权余量/变分 |
| 9.2 | 基函数、棱边元 |
| 9.3 | 等参元 |
| 9.4 | 系统组装 |
| 9.5 | 应用 |
