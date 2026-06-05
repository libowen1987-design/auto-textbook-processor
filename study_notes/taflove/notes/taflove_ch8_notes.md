---
chapter: 8
title: Near-to-Far-Field Transformation
book: Computational Electrodynamics — 3rd Ed.
author: Taflove, Li, Hagness
raw_size: 49,226 bytes
---

# Chapter 8: Near-to-Far-Field (NTFF) Transformation
> **中英双语版**

> 近场-远场变换

## 8.1 Introduction
Using a single FDTD run, the NTFF transformation computes far-field bistatic RCS or antenna radiation patterns from near fields on a virtual surface enclosing the scatterer/antenna.
> 通过单次 FDTD 仿真，NTFF 变换可从包围散射体或天线的虚拟表面上的近场计算出远场双站雷达散射截面或天线辐射方向图。

**Key advantage:** Lattice need not extend to far-field region. NTFF surface is placed in the scattered-field region (Ch5 TF/SF), and time-domain fields recorded over one or more frequency bins via DFT.
> **关键优势：** 计算网格不需要延伸到远场区域。NTFF 表面放置在散射场区域（参见第5章总场/散射场方法），时域场通过离散傅里叶变换记录到一个或多个频率点。

## 8.2 2D Transformation (Phasor Domain)
> 二维变换（相量域）

Using Green's theorem, far-field $E_z^{\text{ff}}$ from tangential $E_z$ and $H_{\text{tan}}$ on contour $C_0$:
> 利用格林定理，从闭合曲线 $C_0$ 上的切向场分量计算远场：
$$E_z^{\text{ff}}(\rho,\phi) = \frac{e^{-jk\rho}}{\sqrt{\rho}} F(\phi)$$
$$F(\phi) = \sqrt{\frac{k}{8\pi}} e^{-j\pi/4} \oint_{C_0} \left[ jk(\hat{n}\cdot\hat{\rho}')E_z - j\omega\mu_0(\hat{n}\times\hat{z})\cdot\hat{\phi} H_{\text{tan}} \right] e^{jk\hat{\rho}\cdot\mathbf{r}'} d\ell'$$
> $F(\phi)$ 为角方向性函数，$\hat{n}$ 为 NTFF 表面的外法向单位矢量。

## 8.3 3D Transformation (Phasor Domain)
> 三维变换（相量域）

$$\mathbf{E}^{\text{ff}}(r,\theta,\phi) = \frac{e^{-jkr}}{r} \mathbf{F}(\theta,\phi)$$

The far-field pattern vector $\mathbf{F}$ is computed from equivalent electric and magnetic currents on the NTFF surface:
> 远场方向图矢量 $\mathbf{F}$ 由 NTFF 表面上的等效电流和等效磁流计算：
$$\mathbf{J}_{\text{eq}} = \hat{n} \times \mathbf{H}_{\text{near}}, \quad \mathbf{M}_{\text{eq}} = -\hat{n} \times \mathbf{E}_{\text{near}}$$

$$\mathbf{F}(\theta,\phi) = \frac{jk}{4\pi} \iint_S \left[ \eta_0 \hat{r} \times (\hat{r} \times \mathbf{J}_{\text{eq}}) + \hat{r} \times \mathbf{M}_{\text{eq}} \right] e^{jk\hat{r}\cdot\mathbf{r}'} dS'$$
> 式中 $\eta_0$ 为自由空间波阻抗，$\hat{r}$ 为观测点方向的单位矢量。该表达式基于等效原理（Surface Equivalence Theorem）。

## 8.4 Time-Domain NTFF
> 时域 NTFF

The time-domain NTFF yields direct time waveforms at far-field observation points:
> 时域 NTFF 直接给出远场观测点的时域波形：
$$E_{\theta}^{\text{ff}}(r,\theta,\phi,t) = \frac{1}{2\pi c r} \frac{\partial}{\partial t} \iint_S \left[ -\mu_0 J_{\theta}^{\text{eq}} + \frac{1}{c} M_{\phi}^{\text{eq}} \right]_{\text{ret}} dS'$$

where [ ]$_{\text{ret}}$ indicates evaluation at retarded time $t - r/c + \hat{r}\cdot\mathbf{r}'/c$.
> 下标 $_{\text{ret}}$ 表示在推迟时刻 $t - r/c + \hat{r}\cdot\mathbf{r}'/c$ 求值，体现了电磁波从源点到观测点的有限传播时间。

## 8.5 Backscatter Enhancement
> 后向散射增强

For strongly forward-scattering objects (e.g., biological cells, stealth vehicles), a modified NTFF procedure subtracts the forward-scattered component before integration, reducing numerical cancellation errors.
> 对于强前向散射物体（如生物细胞、隐身飞行器），改进的 NTFF 程序在积分前减去前向散射分量，减小了数值对消误差。

## Examples
> 典型算例

- **Ex 8.1:** 2D TM$_z$ RCS of a PEC cylinder — compare to Mie series
  > 二维 TM$_z$ 极化理想导体圆柱雷达散射截面——与 Mie 级数结果对比
- **Ex 8.2:** 3D NTFF — radiation pattern of a half-wave dipole
  > 三维 NTFF：半波偶极子天线方向图
- **Ex 8.3:** Time-domain NTFF — backscattered pulse from a dielectric sphere
  > 时域 NTFF：介质球的后向散射脉冲

> **Numerical Intuition:** NTFF enables accurate far-field RCS and antenna patterns from compact FDTD domains. The virtual surface should be at least 10 cells from the structure. Using DFT over $N_f$ frequency points adds $O(N_f N_s)$ storage where $N_s$ is the number of surface cells.
> **数值直觉：** NTFF 可以在紧凑的 FDTD 计算域内获得精确的远场 RCS 和天线方向图。虚拟表面应距离目标结构至少 10 个网格单元。对 $N_f$ 个频率点使用 DFT 需要 $O(N_f N_s)$ 存储量，其中 $N_s$ 为表面网格单元数。
