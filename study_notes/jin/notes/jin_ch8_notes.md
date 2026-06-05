---
title: "Chapter 8 — The Finite Difference Method"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Finite difference formulas (forward, backward, central)
  - 1D/2D wave equation FDM
  - FDTD: Yee cell, leapfrog scheme
  - Stability: CFL condition
  - Numerical dispersion
  - PML absorbing boundary conditions
---

# Chapter 8: The Finite Difference Method | 第八章：有限差分法

> **中英双语版**

## 8.1 Differencing Formulas | 差分公式

$$
f'(x) \approx \frac{f(x+\Delta x)-f(x)}{\Delta x} \quad\text{(forward / 前向)}
$$

$$
f'(x) \approx \frac{f(x)-f(x-\Delta x)}{\Delta x} \quad\text{(backward / 后向)}
$$

$$
f'(x) \approx \frac{f(x+\Delta x)-f(x-\Delta x)}{2\Delta x} \quad\text{(central / 中心)}
$$

$$
f''(x) \approx \frac{f(x+\Delta x)-2f(x)+f(x-\Delta x)}{\Delta x^2}
$$

## 8.2 FDTD Method | FDTD方法

**Yee cell / 耶氏网格:** $\mathbf{E}$ 在棱边中心，$\mathbf{H}$ 在面心，时空交错（蛙跳）。

**2D TEz update / 二维TEz更新:**

$$
H_x|_{i,j}^{n+1/2} = H_x|_{i,j}^{n-1/2} - \frac{\Delta t}{\mu\Delta y} (E_z|_{i,j+1}^n - E_z|_{i,j}^n)
$$

$$
H_y|_{i,j}^{n+1/2} = H_y|_{i,j}^{n-1/2} + \frac{\Delta t}{\mu\Delta x} (E_z|_{i+1,j}^n - E_z|_{i,j}^n)
$$

$$
E_z|_{i,j}^{n+1} = E_z|_{i,j}^n + \frac{\Delta t}{\epsilon\Delta x} (H_y|_{i+1/2,j}^{n+1/2} - H_y|_{i-1/2,j}^{n+1/2}) - \frac{\Delta t}{\epsilon\Delta y} (H_x|_{i,j+1/2}^{n+1/2} - H_x|_{i,j-1/2}^{n+1/2})
$$

## 8.3 Stability: CFL Condition | 稳定性：CFL条件

$$
\Delta t \le \frac{1}{c\sqrt{1/\Delta x^2 + 1/\Delta y^2 + 1/\Delta z^2}}
$$

## 8.4 Numerical Dispersion | 数值色散

FDTD引入依赖于网格分辨率（$\lambda/\Delta x$）的人为色散。

## 8.5 PML (Perfectly Matched Layer) | 完美匹配层

Stretched-coordinate PML (Berenger 1994): split-field formulation / 拉伸坐标PML：分裂场公式。
UPML (uniaxial PML): anisotropic material absorber / 单轴PML：各向异性材料吸收体。

---

## Audit / 审计

| Section / 节 | Topic / 主题 |
|---------|-------|
| 8.1 | 差分公式 |
| 8.2 | FDTD格式 |
| 8.3 | CFL稳定性 |
| 8.4 | 数值色散 |
| 8.5 | PML/UPML |
