# Chapter 1: Vector Analysis

> **中英双语版**

**Source:** Griffiths, *Introduction to Electrodynamics*, 4th Ed., Chapter 1 (pp. 1–77)
**来源：** Griffiths《电动力学导论》第4版，第1章（第1–77页）

---

## 1.1 Vector Algebra / 矢量代数

**Dot / 点积：** $\mathbf{A} \cdot \mathbf{B} = AB\cos\theta = A_xB_x + A_yB_y + A_zB_z$

**Cross / 叉积：** $\mathbf{A} \times \mathbf{B} = \begin{vmatrix} \hat{\mathbf{x}} & \hat{\mathbf{y}} & \hat{\mathbf{z}} \\ A_x & A_y & A_z \\ B_x & B_y & B_z \end{vmatrix}$

**Triple Products / 三重积：**
- Scalar / 标量三重积: $\mathbf{A} \cdot (\mathbf{B} \times \mathbf{C}) = \mathbf{B} \cdot (\mathbf{C} \times \mathbf{A}) = \mathbf{C} \cdot (\mathbf{A} \times \mathbf{B})$
- Vector / 矢量三重积: $\mathbf{A} \times (\mathbf{B} \times \mathbf{C}) = \mathbf{B}(\mathbf{A} \cdot \mathbf{C}) - \mathbf{C}(\mathbf{A} \cdot \mathbf{B})$

## 1.2 Differential Calculus / 微分运算

**Gradient / 梯度：** $\nabla T = \frac{\partial T}{\partial x}\hat{\mathbf{x}} + \frac{\partial T}{\partial y}\hat{\mathbf{y}} + \frac{\partial T}{\partial z}\hat{\mathbf{z}}$

**Divergence / 散度：** $\nabla \cdot \mathbf{v} = \frac{\partial v_x}{\partial x} + \frac{\partial v_y}{\partial y} + \frac{\partial v_z}{\partial z}$

**Curl / 旋度：** $\nabla \times \mathbf{v}$

## 1.3 Integral Calculus / 积分运算

**Fundamental Theorem for Gradients / 梯度基本定理：** $\int_a^b (\nabla T) \cdot d\mathbf{l} = T(b) - T(a)$

**Divergence Theorem / 散度定理（高斯定理）：** $\int_V (\nabla \cdot \mathbf{v})\,dV = \oint_S \mathbf{v} \cdot d\mathbf{a}$

**Stokes' Theorem / 斯托克斯定理：** $\int_S (\nabla \times \mathbf{v})\cdot d\mathbf{a} = \oint_P \mathbf{v} \cdot d\mathbf{l}$

## 1.5 The Dirac Delta Function / 狄拉克 δ 函数

$$
\delta(x) = \begin{cases} 0 & x \neq 0 \\ \infty & x = 0 \end{cases}, \quad \int_{-\infty}^{\infty} \delta(x)\,dx = 1
$$

Key property / 关键性质：$\int_{-\infty}^{\infty} f(x)\delta(x-a)\,dx = f(a)$

In 3D / 三维形式：$\delta^3(\mathbf{r} - \mathbf{r}') = \delta(x-x')\delta(y-y')\delta(z-z')$

$$
\nabla^2 \frac{1}{|\mathbf{r} - \mathbf{r}'|} = -4\pi \delta^3(\mathbf{r} - \mathbf{r}')
$$

## 1.6 Helmholtz Theorem / 亥姆霍兹定理

Any vector field $\mathbf{F}$ can be expressed as / 任意矢量场 $\mathbf{F}$ 可分解为：
$$
\mathbf{F} = -\nabla U + \nabla \times \mathbf{W}
$$

where $U$ depends on $\nabla \cdot \mathbf{F}$ and $\mathbf{W}$ depends on $\nabla \times \mathbf{F}$.
其中 $U$ 由 $\nabla \cdot \mathbf{F}$ 决定，$\mathbf{W}$ 由 $\nabla \times \mathbf{F}$ 决定。
