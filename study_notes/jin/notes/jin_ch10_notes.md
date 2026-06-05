---
title: "Chapter 10 — The Method of Moments"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Integral equation formulation using Green's functions
  - MoM discretization: basis functions, testing functions
  - EFIE and MFIE for conducting objects
  - RWG basis functions (triangular mesh)
  - Impedance matrix filling
  - Plane wave illumination, RCS computation
  - Microstrip antenna analysis
---

# Chapter 10: The Method of Moments (MoM) | 第十章：矩量法

> **中英双语版**

## 10.1 Introduction | 引言

**Electrostatic integral equation / 静电积分方程:**

$$
\int_S G(\mathbf{r}, \mathbf{r}') \varrho_s(\mathbf{r}') dS' = \Phi
$$

Discretize with pulse basis functions / 用脉冲基函数离散化：

$$
\sum_{j=1}^N Z_{ij} \varrho_j = \Phi_i
$$

其中 $Z_{ij} = \int_{\Delta S_j} \frac{1}{4\pi\epsilon |\mathbf{r}_i - \mathbf{r}'|} dS'$。

## 10.2 EFIE for Conducting Objects | 导体物体的EFIE

**Electric Field Integral Equation / 电场积分方程:**
$$
\hat{n} \times [\mathbf{E}^{\text{inc}} + \mathbf{E}^{\text{scat}}(\mathbf{J}_s)] = 0 \quad\text{on } S
$$

Discretized with RWG basis functions on triangular mesh / 使用三角形网格上的RWG基函数离散化：

$$
\mathbf{J}_s \approx \sum_{n=1}^N I_n \mathbf{f}_n(\mathbf{r})
$$

**Impedance matrix / 阻抗矩阵:** $Z_{mn} = \langle \mathbf{f}_m, \mathcal{L}(\mathbf{f}_n) \rangle$。

## 10.3 Scattering and RCS | 散射与雷达散射截面

Bistatic RCS computed from far-field transform of induced currents / 从感应电流的远场变换计算双站RCS。

## 10.4 Microstrip and Periodic Structures | 微带与周期结构

Green's function for layered media + MoM for planar circuits / 分层媒质格林函数 + 矩量法用于平面电路。

## 10.5 Time-Domain MoM | 时域矩量法

Marching-on-in-time (MOT) scheme / 时间步进 (MOT) 格式。

---

## Audit / 审计

| Section / 节 | Topic / 主题 |
|---------|-------|
| 10.1 | 引言，静电示例 |
| 10.2 | 导体的EFIE/MFIE |
| 10.3 | 散射/RCS |
| 10.4 | 微带/周期 |
| 10.5 | 时域矩量法 |
