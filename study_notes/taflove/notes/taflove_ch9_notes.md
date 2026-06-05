---
chapter: 9
title: Dispersive, Nonlinear, and Gain Materials
book: Computational Electrodynamics — 3rd Ed.
raw_size: 101,845 bytes
---

# Chapter 9: Dispersive, Nonlinear, and Gain Materials
> **中英双语版**

> 色散、非线性和增益材料

## 9.1 Introduction
FDTD naturally handles dispersive, nonlinear, and active media. Three main approaches: PLRC (piecewise-linear recursive convolution), ADE (auxiliary differential equation), and Z-transform methods.
> FDTD 天然适用于处理色散、非线性和有源介质。主要方法有三种：分段线性递归卷积 (PLRC)、辅助微分方程 (ADE) 和 Z 变换法。

## 9.2 Generic Material Dispersion Models
> 通用材料色散模型

### Debye (Relaxation)
> Debye 弛豫模型

$$\epsilon_r(\omega) = \epsilon_\infty + \sum_{p=1}^P \frac{\Delta\epsilon_p}{1 + j\omega\tau_p} \tag{9.1}$$
Time-domain susceptibility: $\chi(t) = \sum_p \frac{\Delta\epsilon_p}{\tau_p} e^{-t/\tau_p} u(t) \tag{9.2}$
> 时域极化率：其中 $u(t)$ 为单位阶跃函数，$\tau_p$ 为弛豫时间常数。

### Lorentz (Resonance)
> Lorentz 谐振模型

$$\epsilon_r(\omega) = \epsilon_\infty + \sum_{p=1}^P \frac{\Delta\epsilon_p \omega_p^2}{\omega_p^2 + 2j\omega\delta_p - \omega^2} \tag{9.4}$$
Time-domain: $\chi(t) = \sum_p \frac{\Delta\epsilon_p \omega_p^2}{\sqrt{\omega_p^2 - \delta_p^2}} e^{-\delta_p t} \sin\left(\sqrt{\omega_p^2 - \delta_p^2} t\right) u(t) \tag{9.5}$
> 时域表达式：$\delta_p$ 为阻尼系数，$\omega_p$ 为谐振频率。

### Drude (Metals)
> Drude 金属模型

$$\epsilon_r(\omega) = \epsilon_\infty - \sum_{p=1}^P \frac{\omega_p^2}{\omega^2 + j\omega\gamma_p} \tag{9.7}$$
Time-domain: $\chi(t) = -\sum_p \frac{\omega_p^2}{\gamma_p} (1 - e^{-\gamma_p t}) u(t)$
> 时域极化率：$\gamma_p$ 为碰撞频率，适用于金属在光频段的电磁特性描述。

## 9.3 PLRC Method
> 分段线性递归卷积法

$$\mathbf{D}(t) = \epsilon_0\epsilon_\infty \mathbf{E}(t) + \epsilon_0 \int_0^t \mathbf{E}(t - \tau) \chi(\tau) d\tau$$
PLRC approximates $\mathbf{E}$ as linear between time-steps:
> PLRC 近似假设电场 $\mathbf{E}$ 在时间步之间线性变化：
$$\mathbf{D}^n = \epsilon_0\epsilon_\infty \mathbf{E}^n + \epsilon_0 \sum_{m=0}^{N-1} \mathbf{E}^{n-m} \chi^m + \mathbf{E}^{n-m-1} \xi^m$$

## 9.4 ADE Method (Linear Dispersive)
> 辅助微分方程法（线性色散）

Introduce polarization current $\mathbf{J}_p$:
> 引入极化电流 $\mathbf{J}_p$：
$$\frac{d\mathbf{J}_p}{dt} + \Gamma \mathbf{J}_p = \epsilon_0 \omega_p^2 \mathbf{E} \quad \text{(Drude)}$$
$$\frac{d^2\mathbf{P}}{dt^2} + 2\delta\frac{d\mathbf{P}}{dt} + \omega_0^2 \mathbf{P} = \epsilon_0 \Delta\epsilon \omega_0^2 \mathbf{E} \quad \text{(Lorentz)}$$
> ADE 方法通过引入关于极化量（$\mathbf{J}_p$ 或 $\mathbf{P}$）的微分方程，避免存储完整的卷积历史，计算效率更高。

## 9.5 Nonlinear Dispersive Media (Kerr, Raman)
> 非线性色散介质（Kerr 效应、Raman 效应）

$$\mathbf{P}_{\text{NL}} = \chi^{(3)} |\mathbf{E}|^2 \mathbf{E}$$
Use ADE with nonlinear polarization term, solved via predictor-corrector or Newton iteration.
> 使用含非线性极化项的 ADE 方法，通过预测-校正或 Newton 迭代求解。

## 9.6 Active Gain Media (Lasers)
> 有源增益介质（激光器）

For a four-level gain system + Lorentz dispersion:
> 对于四能级增益系统结合 Lorentz 色散：
$$\frac{dN_1}{dt} = \frac{N_2}{\tau_{21}} - \frac{N_1}{\tau_{10}} + \frac{\mathbf{E} \cdot d\mathbf{P}/dt}{\hbar\omega_a}$$
$$\frac{dN_0}{dt} = \frac{N_1}{\tau_{10}} - R_p \quad \text{(pumping)}$$
> $N_i$ 为第 $i$ 能级的粒子数密度，$\tau_{ij}$ 为从能级 $i$ 到 $j$ 的弛豫时间，$R_p$ 为泵浦速率。该模型可模拟激光腔的起振过程。

## Examples
> 典型算例

- **Ex 9.1:** FDTD + Drude model — optical reflection from silver at 600 nm
  > FDTD + Drude 模型：银在 600 nm 波长处的光学反射
- **Ex 9.2:** Lorentz medium — pulse propagation in dispersive dielectric slab
  > Lorentz 介质：脉冲在色散介质板中的传播
- **Ex 9.3:** Saturable gain — laser cavity startup dynamics
  > 可饱和增益：激光腔起振动力学
