# Sadiku《Elements of Electromagnetics》Chapter 2: Coordinate Systems and Transformation
> **中英双语版**

> **Source:** Sadiku, *Elements of Electromagnetics*, 7th Ed. (Oxford University Press, 2017)  
> **PDF:** pages 58-85

---

## 2.1 Introduction | 引言

Physical quantities in EM are functions of space and time. To describe spatial variations, we must define all points uniquely using an appropriate coordinate system.
> 电磁学中的物理量是空间和时间的函数。为描述空间变化，必须使用适当的坐标系唯一定义所有点。

An **orthogonal system** is one where coordinate surfaces are mutually perpendicular. We restrict ourselves to three systems: Cartesian, circular cylindrical, and spherical.
> **正交坐标系**中坐标面相互垂直。本书限制在三种坐标系：笛卡尔（直角）、圆柱和球坐标系。

---

## 2.2 Cartesian Coordinates $(x, y, z)$ | 笛卡尔坐标

$$\mathbf{A} = A_x \mathbf{a}_x + A_y \mathbf{a}_y + A_z \mathbf{a}_z$$

Ranges: $-\infty < x, y, z < \infty$. Right-handed system is used.
> 范围：$-\infty < x, y, z < \infty$。使用右手坐标系。

**Differential quantities / 微分量：**
- $d\mathbf{l} = dx\,\mathbf{a}_x + dy\,\mathbf{a}_y + dz\,\mathbf{a}_z$ (differential length / 线元)
- $d\mathbf{S} = dy\,dz\,\mathbf{a}_x$ (etc., differential surface / 面元)
- $dV = dx\,dy\,dz$ (differential volume / 体元)

---

## 2.3 Circular Cylindrical Coordinates $(\rho, \phi, z)$ | 圆柱坐标

$$\mathbf{A} = A_\rho \mathbf{a}_\rho + A_\phi \mathbf{a}_\phi + A_z \mathbf{a}_z$$

Ranges: $0 \leq \rho < \infty$, $0 \leq \phi < 2\pi$, $-\infty < z < \infty$.
> 范围：$0 \leq \rho < \infty$，$0 \leq \phi < 2\pi$，$-\infty < z < \infty$。

**Transformation to Cartesian / 到笛卡尔坐标的变换：**

$$x = \rho \cos\phi, \quad y = \rho \sin\phi, \quad z = z$$
$$\rho = \sqrt{x^2 + y^2}, \quad \phi = \tan^{-1}(y/x)$$

**Differential quantities / 微分量：**
- $d\mathbf{l} = d\rho\,\mathbf{a}_\rho + \rho\,d\phi\,\mathbf{a}_\phi + dz\,\mathbf{a}_z$
- $dV = \rho\,d\rho\,d\phi\,dz$

---

## 2.4 Spherical Coordinates $(r, \theta, \phi)$ | 球坐标

$$\mathbf{A} = A_r \mathbf{a}_r + A_\theta \mathbf{a}_\theta + A_\phi \mathbf{a}_\phi$$

Ranges: $0 \leq r < \infty$, $0 \leq \theta \leq \pi$, $0 \leq \phi < 2\pi$.
> 范围：$0 \leq r < \infty$，$0 \leq \theta \leq \pi$，$0 \leq \phi < 2\pi$。

**Transformation to Cartesian / 到笛卡尔坐标的变换：**

$$x = r\sin\theta\cos\phi, \quad y = r\sin\theta\sin\phi, \quad z = r\cos\theta$$
$$r = \sqrt{x^2 + y^2 + z^2}, \quad \theta = \tan^{-1}(\sqrt{x^2 + y^2}/z), \quad \phi = \tan^{-1}(y/x)$$

**Differential quantities / 微分量：**
- $d\mathbf{l} = dr\,\mathbf{a}_r + r\,d\theta\,\mathbf{a}_\theta + r\sin\theta\,d\phi\,\mathbf{a}_\phi$
- $dV = r^2\sin\theta\,dr\,d\theta\,d\phi$

---

## 2.5 Coordinate Transformations | 坐标系变换

**Vector transformation procedure / 矢量变换步骤：**
1. Express the vector in the source system
2. Use dot products to find components in the target system:
   > 使用点积求目标系统中的分量
   $$A_u = \mathbf{A} \cdot \mathbf{a}_u, \quad A_v = \mathbf{A} \cdot \mathbf{a}_v, \quad A_w = \mathbf{A} \cdot \mathbf{a}_w$$

---

## 2.6 Distance Between Two Points | 两点间距离

$$d = |\mathbf{r}_2 - \mathbf{r}_1| = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$

---

## Key Formulas Summary | 关键公式总结

| Quantity | Cartesian | Cylindrical | Spherical |
|----------|-----------|-------------|-----------|
| $d\mathbf{l}$ | $dx\mathbf{a}_x + dy\mathbf{a}_y + dz\mathbf{a}_z$ | $d\rho\mathbf{a}_\rho + \rho d\phi\mathbf{a}_\phi + dz\mathbf{a}_z$ | $dr\mathbf{a}_r + r d\theta\mathbf{a}_\theta + r\sin\theta d\phi\mathbf{a}_\phi$ |
| $dV$ | $dx\,dy\,dz$ | $\rho\,d\rho\,d\phi\,dz$ | $r^2\sin\theta\,dr\,d\theta\,d\phi$ |
| Gradient $\nabla V$ | $\frac{\partial V}{\partial x}\mathbf{a}_x + \frac{\partial V}{\partial y}\mathbf{a}_y + \frac{\partial V}{\partial z}\mathbf{a}_z$ | $\frac{\partial V}{\partial \rho}\mathbf{a}_\rho + \frac{1}{\rho}\frac{\partial V}{\partial \phi}\mathbf{a}_\phi + \frac{\partial V}{\partial z}\mathbf{a}_z$ | $\frac{\partial V}{\partial r}\mathbf{a}_r + \frac{1}{r}\frac{\partial V}{\partial \theta}\mathbf{a}_\theta + \frac{1}{r\sin\theta}\frac{\partial V}{\partial \phi}\mathbf{a}_\phi$ |
