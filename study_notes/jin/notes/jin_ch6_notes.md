---
title: "Chapter 6 — Fields and Waves in Cylindrical Coordinates"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Cylindrical wave functions (Bessel, Hankel functions)
  - Circular waveguide TE/TM modes
  - Coaxial waveguide TEM/TE/TM modes
  - Dielectric rod waveguide
  - Plane wave expansion in cylindrical harmonics
  - Scattering by conducting/dielectric cylinders
  - Line source and wedge radiation
---

# Chapter 6: Fields and Waves in Cylindrical Coordinates | 第六章：柱坐标中的场与波

> **中英双语版**

## 6.1 Solution of Wave Equation | 波动方程的解

In cylindrical coordinates, Helmholtz equation separates as $\psi = P(\rho)\Phi(\phi)Z(z)$ / 柱坐标中亥姆霍兹方程分离为 $\psi = P(\rho)\Phi(\phi)Z(z)$。

**$Z(z)$:** $e^{\pm jk_z z}$ (propagating / 传播) 或 $e^{\pm \alpha_z z}$ (evanescent / 凋落)。

**$\Phi(\phi)$:** $e^{\pm j n\phi}$, $n = 0, 1, 2, \dots$

**$P(\rho)$:** Bessel equation / 贝塞尔方程 $\rightarrow$ $J_n(k_\rho \rho)$, $Y_n(k_\rho \rho)$, $H_n^{(1)}(k_\rho \rho)$, $H_n^{(2)}(k_\rho \rho)$。

其中 $k_\rho^2 = k^2 - k_z^2$。

---

## 6.2 Circular Waveguide | 圆波导

**TE$_{nm}$ modes / TE$_{nm}$ 模:** $H_z = J_n(k_c \rho) e^{\pm j n\phi}$, $k_c = p'_{nm}/a$（$p'_{nm}$ = $J_n'$ 的第n个零点）。

**TM$_{nm}$ modes / TM$_{nm}$ 模:** $E_z = J_n(k_c \rho) e^{\pm j n\phi}$, $k_c = p_{nm}/a$（$p_{nm}$ = $J_n$ 的第n个零点）。

**Dominant mode / 主模:** TE$_{11}$ — 最低截止频率。

---

## 6.3 Coaxial Waveguide | 同轴波导

**TEM mode / TEM 模:** $E_\rho = V_0/(\rho \ln(b/a))$, $H_\phi = I_0/(2\pi\rho)$。

**TE/TM modes / TE/TM 模:** 类似圆波导，但同时使用 $J_n$ 和 $Y_n$。

---

## 6.4 Circular Dielectric Waveguide (Optical Fiber) | 圆介质波导（光纤）

混合HE/EH模。对于弱导引（$\Delta \ll 1$）：LP模。

---

## 6.5 Plane Wave / Cylindrical Function Transform | 平面波/柱函数变换

$$
e^{-jk\rho \cos\phi} = \sum_{n=-\infty}^{\infty} j^{-n} J_n(k\rho) e^{jn\phi}
$$

---

## 6.6 Scattering by Cylinders | 圆柱体的散射

Conducting cylinder: Mie series solution using cylindrical harmonics / 导体柱：使用柱谐函数的Mie级数解。

Dielectric cylinder: internal + external fields matched at boundary / 介质柱：内部+外部场在边界匹配。

---

## Audit / 审计

| Section / 节 | Topic / 主题 |
|---------|-------|
| 6.1 | 柱波函数 |
| 6.2 | 圆波导 |
| 6.3 | 同轴波导 |
| 6.4 | 介质棒波导 |
| 6.5 | 平面波展开 |
| 6.6 | 圆柱散射 |
