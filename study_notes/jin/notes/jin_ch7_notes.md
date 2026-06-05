---
title: "Chapter 7 — Fields and Waves in Spherical Coordinates"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Spherical wave functions (spherical Bessel, Legendre)
  - Spherical cavity and biconical antenna
  - Plane wave expansion in spherical harmonics
  - Mie scattering by spheres (conducting, dielectric)
  - Addition theorem for spherical waves
---

# Chapter 7: Fields and Waves in Spherical Coordinates | 第七章：球坐标中的场与波

> **中英双语版**

## 7.1 Solution of Wave Equation | 波动方程的解

Separate $\psi(r,\theta,\phi) = R(r) \Theta(\theta) \Phi(\phi)$ / 分离变量 $\psi(r,\theta,\phi) = R(r) \Theta(\theta) \Phi(\phi)$。

**$\Phi$:** $e^{\pm j m\phi}$。

**$\Theta$:** 缔合勒让德方程 $\rightarrow$ $P_n^m(\cos\theta)$。

**$R$:** 球贝塞尔方程 $\rightarrow$ $j_n(kr)$, $y_n(kr)$, $h_n^{(1)}(kr)$, $h_n^{(2)}(kr)$。

---

## 7.2 Spherical Cavity and Biconical Antenna | 球腔与双锥天线

**Spherical cavity / 球腔:** 通过球贝塞尔函数零点得到谐振模。有TE$_{nmp}$和TM$_{nmp}$模。

**Biconical antenna / 双锥天线:** 两锥体间的TEM模。输入阻抗取决于锥角。

---

## 7.3 Plane Wave Expansion | 平面波展开

$$
e^{-jkz} = \sum_{n=0}^\infty j^{-n}(2n+1) j_n(kr) P_n(\cos\theta)
$$

---

## 7.4 Mie Scattering by a Sphere | 球的米氏散射

**Conducting sphere / 导体球:** 表面切向 $\mathbf{E}$ 为零。使用球谐函数的级数解。

**Dielectric sphere / 介质球:** 在 $r=a$ 处匹配内部和外部场。

**Scattering cross-section $\sigma_s$ / 散射截面** 和 **extinction cross-section $\sigma_e$ / 消光截面**。

---

## 7.5 Addition Theorem | 加法定理

Translates spherical wave functions between origins — essential for multiple-sphere scattering / 在原点间平移球波函数——对多球散射至关重要。

---

## Audit / 审计

| Section / 节 | Topic / 主题 |
|---------|-------|
| 7.1 | 球波函数 |
| 7.2 | 球腔、双锥天线 |
| 7.3 | 平面波展开 |
| 7.4 | 米氏散射 |
| 7.5 | 加法定理 |
