---
title: "Chapter 5 — Fields and Waves in Rectangular Coordinates"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - General theory of uniform waveguides (TE, TM, TEM modes)
  - Rectangular waveguide TE/TM modes
  - Cutoff frequency and dispersion
  - Rectangular cavities and resonators
  - Dielectric slab waveguide
  - Green's function for planar layered media
---

# Chapter 5: Fields and Waves in Rectangular Coordinates | 第五章：直角坐标中的场与波

> **中英双语版**

## 5.1 Uniform Waveguides | 均匀波导

Fields in a uniform waveguide ($e^{-jk_z z}$ dependence) / 均匀波导中的场（$e^{-jk_z z}$ 依赖）：

$$
\mathbf{E} = (\mathbf{e}_t + \hat{z} e_z) e^{-jk_z z}, \quad
\mathbf{H} = (\mathbf{h}_t + \hat{z} h_z) e^{-jk_z z}
$$

**Transverse fields in terms of longitudinal components / 用纵向分量表示横向场:**

$$
\mathbf{E}_t = \frac{1}{k_t^2} \left( j\omega\mu \hat{z} \times \nabla_t H_z - jk_z \nabla_t E_z \right)
\tag{5.1.11}
$$

$$
\mathbf{H}_t = \frac{1}{k_t^2} \left( -j\omega\epsilon \hat{z} \times \nabla_t E_z - jk_z \nabla_t H_z \right)
\tag{5.1.12}
$$

where $k_t^2 = k^2 - k_z^2$ / 其中 $k_t^2 = k^2 - k_z^2$。

**Three mode types / 三种模式类型:**
- **TEM** ($E_z = H_z = 0$): $k_z = k$，无截止
- **TE** ($E_z = 0$): $H_z$ 满足 $\nabla_t^2 H_z + k_t^2 H_z = 0$
- **TM** ($H_z = 0$): $E_z$ 满足 $\nabla_t^2 E_z + k_t^2 E_z = 0$

**Cutoff wavenumber / 截止波数:** $k_c = k_t$ — 仅当 $k > k_c$ ($f > f_c$) 时传播。

---

## 5.2 Rectangular Waveguide | 矩形波导

For a waveguide with cross-section $a \times b$ / 横截面 $a \times b$ 的波导：

**TM$_{mn}$ modes / TM$_{mn}$ 模:**

$$
E_z = \sin\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right)
$$

$$
k_c = \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}, \quad
f_c = \frac{k_c}{2\pi\sqrt{\mu\epsilon}}
$$

**TE$_{mn}$ modes / TE$_{mn}$ 模:**

$$
H_z = \cos\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right)
$$

**Dominant mode / 主模:** TE$_{10}$（最低截止频率）。

**Waveguide wavelength / 波导波长:** $\lambda_g = \frac{2\pi}{\sqrt{k^2 - k_c^2}}$。

**Attenuation / 衰减:** 来自导体损耗和介质损耗。

---

## 5.3 Rectangular Cavity | 矩形腔

A waveguide section of length $d$ shorted at both ends / 两端短路、长度为 $d$ 的波导段。

**Resonant frequencies / 谐振频率:**

$$
f_{mnp} = \frac{1}{2\pi\sqrt{\mu\epsilon}} \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2 + \left(\frac{p\pi}{d}\right)^2}
$$

**Quality factor / 品质因数:** $Q = \omega_0 W / P_{\text{loss}}$。

---

## 5.4 Dielectric Slab Waveguide | 介质板波导

Guided by total internal reflection / 通过全内反射导引。TE和TM表面波模。

**Dispersion relation (TE) / 色散关系 (TE):**

$$
\kappa d = m\pi + 2\tan^{-1}(\gamma/\kappa)
$$

其中 $\kappa = \sqrt{k_f^2 - k_z^2}$, $\gamma = \sqrt{k_z^2 - k_c^2}$, $k_f = \omega\sqrt{\mu\epsilon_f}$, $k_c = \omega\sqrt{\mu\epsilon_c}$。

---

## 5.5 Green's Function for Planar Layered Media | 平面分层媒质的格林函数

Constructed using TE/TM decomposition and transmission line analogy / 使用TE/TM分解和传输线类比构造。

---

## Key Physical Intuition | 关键物理直觉

1. **波导模** 在横向平面内是驻波，在纵向是行波。
2. **截止** 发生在 $k < k_c$ 时——截止以下，模为凋落模。
3. **TE$_{10}$** 是主模，因为它有最简单的场模式和最低截止频率。
4. **谐振腔** 在离散频率处储存能量——对滤波器和振荡器至关重要。

---

## Audit / 审计

| Section / 节 | Content Coverage / 内容覆盖 |
|---------|-----------------|
| 5.1 | 均匀波导理论 |
| 5.2 | 矩形波导 |
| 5.3 | 矩形腔 |
| 5.4 | 介质板波导 |
| 5.5 | 格林函数、分层媒质 |
