# Chapter 2: Electromagnetic Radiation in Free Space
> **中英双语版**

> 自由空间中的电磁辐射

**Source:** Jin, *Theory and Computation of Electromagnetic Fields*, 2nd Ed., Chapter 2 (pp. 77–112)

---

## 2.1 Scalar and Vector Potentials
> 标量和矢量势

### 2.1.1 Static Fields / 静态场

For static electric fields, $\nabla \times \mathbf{E} = 0$ implies $\mathbf{E} = -\nabla \Phi$ with Poisson's equation $\nabla^2 \Phi = -\rho_e/\epsilon$.
> 静电场中，$\nabla \times \mathbf{E} = 0$ 意味着 $\mathbf{E}$ 可表示为标量势的梯度。

For static magnetic fields, $\nabla \cdot \mathbf{B} = 0$ allows $\mathbf{B} = \nabla \times \mathbf{A}$.
> 静磁场中，$\nabla \cdot \mathbf{B} = 0$ 允许引入矢量势 $\mathbf{A}$。

With the **Coulomb gauge** $\nabla \cdot \mathbf{A} = 0$: $\nabla^2 \mathbf{A} = -\mu \mathbf{J}$。
> 在**库仑规范** $\nabla \cdot \mathbf{A} = 0$ 下：

### 2.1.2 Time-Harmonic Fields and the Lorenz Gauge
> 时谐场与 Lorenz 规范

The Lorenz gauge condition $\nabla \cdot \mathbf{A} = -j\omega \mu \epsilon \Phi$ decouples the vector and scalar potentials:
> Lorenz 规范条件解耦了矢量和标量势：
$$\nabla^2 \mathbf{A} + k^2 \mathbf{A} = -\mu \mathbf{J}, \quad \nabla^2 \Phi + k^2 \Phi = -\frac{\rho_e}{\epsilon}$$

---

## 2.2 Solution of Vector Potentials in Free Space
> 自由空间中矢量势的解

The free-space Green's function for the Helmholtz equation:
> Helmholtz 方程的自由空间格林函数：
$$G(\mathbf{r}, \mathbf{r}') = \frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{4\pi |\mathbf{r} - \mathbf{r}'|}$$

The vector potential solution:
> 矢量势的解：
$$\mathbf{A}(\mathbf{r}) = \frac{\mu}{4\pi} \iiint_V \mathbf{J}(\mathbf{r}') \frac{e^{-jkR}}{R} dV', \quad R = |\mathbf{r} - \mathbf{r}'|$$

---

## 2.3 Infinitesimal Electric Dipole (Hertzian Dipole)
> 无穷小电偶极子（赫兹偶极子）

For a short dipole of length $dl$ at the origin carrying current $I$:
> 位于原点、载流 $I$、长度为 $dl$ 的短偶极子：

**Vector potential / 矢量势：** $A_z = \frac{\mu I dl}{4\pi} \frac{e^{-jkr}}{r}$

**Fields / 场：**
$$H_\phi = \frac{I dl}{4\pi} jk \sin\theta \frac{e^{-jkr}}{r} \left(1 + \frac{1}{jkr}\right)$$
$$E_r = \frac{I dl}{4\pi} \eta \frac{2\cos\theta}{r^2} \left(1 + \frac{1}{jkr}\right) e^{-jkr}$$
$$E_\theta = \frac{I dl}{4\pi} j\omega\mu \sin\theta \frac{e^{-jkr}}{r} \left(1 + \frac{1}{jkr} - \frac{1}{k^2 r^2}\right)$$

### Near-Field and Far-Field / 近场和远场

**Far field ($kr \gg 1$) / 远场：**
$$E_\theta \approx j \frac{I dl}{4\pi} \eta k \sin\theta \frac{e^{-jkr}}{r}, \quad H_\phi \approx j \frac{I dl}{4\pi} k \sin\theta \frac{e^{-jkr}}{r}$$

**Radiation resistance / 辐射电阻：** $R_{\text{rad}} = 80\pi^2 \left(\frac{dl}{\lambda}\right)^2 \, (\Omega)$

---

## 2.4-2.5 Linear Antenna / 线性天线

For a center-fed dipole of length $L$:
> 对于中心馈电的长度为 $L$ 的偶极子：
$$I(z') = I_0 \sin\left[k\left(\frac{L}{2} - |z'|\right)\right]$$

**Half-wave dipole ($L = \lambda/2$) / 半波偶极子：**
Directivity $D_0 = 1.64$ (2.15 dBi), $R_{\text{rad}} \approx 73 \, \Omega$。

---

## 2.6 Far-Field Approximation / 远场近似

**Fraunhofer distance / Fraunhofer 距离：** $r \geq \frac{2D^2}{\lambda}$

**Far-Field Radiation Integral / 远场辐射积分：**
$$\mathbf{A}(\mathbf{r}) \approx \frac{\mu e^{-jkr}}{4\pi r} \iiint_V \mathbf{J}(\mathbf{r}') e^{jk\hat{\mathbf{r}} \cdot \mathbf{r}'} dV'$$
$$\mathbf{E}(\mathbf{r}) \approx -j\omega \mathbf{A}_t(\mathbf{r})$$
