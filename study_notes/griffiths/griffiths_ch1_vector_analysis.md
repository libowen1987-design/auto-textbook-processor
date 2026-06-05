# Chapter 1: Vector Analysis

**Source:** Griffiths, *Introduction to Electrodynamics*, 4th Ed., Chapter 1 (pp. 1–77)

---

## 1.1 Vector Algebra

**Dot:** $\mathbf{A} \cdot \mathbf{B} = AB\cos\theta = A_xB_x + A_yB_y + A_zB_z$

**Cross:** $\mathbf{A} \times \mathbf{B} = \begin{vmatrix} \hat{\mathbf{x}} & \hat{\mathbf{y}} & \hat{\mathbf{z}} \\ A_x & A_y & A_z \\ B_x & B_y & B_z \end{vmatrix}$

**Triple Products:**
- Scalar: $\mathbf{A} \cdot (\mathbf{B} \times \mathbf{C}) = \mathbf{B} \cdot (\mathbf{C} \times \mathbf{A}) = \mathbf{C} \cdot (\mathbf{A} \times \mathbf{B})$
- Vector: $\mathbf{A} \times (\mathbf{B} \times \mathbf{C}) = \mathbf{B}(\mathbf{A} \cdot \mathbf{C}) - \mathbf{C}(\mathbf{A} \cdot \mathbf{B})$

## 1.2 Differential Calculus

**Gradient:** $\nabla T = \frac{\partial T}{\partial x}\hat{\mathbf{x}} + \frac{\partial T}{\partial y}\hat{\mathbf{y}} + \frac{\partial T}{\partial z}\hat{\mathbf{z}}$

**Divergence:** $\nabla \cdot \mathbf{v} = \frac{\partial v_x}{\partial x} + \frac{\partial v_y}{\partial y} + \frac{\partial v_z}{\partial z}$

**Curl:** $\nabla \times \mathbf{v}$

## 1.3 Integral Calculus

**Fundamental Theorem for Gradients:** $\int_a^b (\nabla T) \cdot d\mathbf{l} = T(b) - T(a)$

**Divergence Theorem:** $\int_V (\nabla \cdot \mathbf{v})\,dV = \oint_S \mathbf{v} \cdot d\mathbf{a}$

**Stokes' Theorem:** $\int_S (\nabla \times \mathbf{v})\cdot d\mathbf{a} = \oint_P \mathbf{v} \cdot d\mathbf{l}$

## 1.5 The Dirac Delta Function

$$
\delta(x) = \begin{cases} 0 & x \neq 0 \\ \infty & x = 0 \end{cases}, \quad \int_{-\infty}^{\infty} \delta(x)\,dx = 1
$$

Key property: $\int_{-\infty}^{\infty} f(x)\delta(x-a)\,dx = f(a)$

In 3D: $\delta^3(\mathbf{r} - \mathbf{r}') = \delta(x-x')\delta(y-y')\delta(z-z')$

$$
\nabla^2 \frac{1}{|\mathbf{r} - \mathbf{r}'|} = -4\pi \delta^3(\mathbf{r} - \mathbf{r}')
$$

## 1.6 Helmholtz Theorem

Any vector field $\mathbf{F}$ can be expressed as:
$$
\mathbf{F} = -\nabla U + \nabla \times \mathbf{W}
$$

where $U$ depends on $\nabla \cdot \mathbf{F}$ and $\mathbf{W}$ depends on $\nabla \times \mathbf{F}$.
