# Sadiku《Elements of Electromagnetics》Chapter 3: Vector Calculus
> **中英双语版**

## 3.1 Introduction | 引言
Vector calculus deals with integration and differentiation of vectors. Key operators: gradient, divergence, curl, and Laplacian.
> 矢量微积分处理矢量的积分和微分。关键算子：梯度、散度、旋度和拉普拉斯算子。

## 3.2 Differential Length, Area, and Volume | 微分长度、面积和体积
- $d\mathbf{l} = dx\,\mathbf{a}_x + dy\,\mathbf{a}_y + dz\,\mathbf{a}_z$ (Cartesian)
- Surface elements $d\mathbf{S}$ are directed normal to the surface.
- Volume element $dV = dx\,dy\,dz$.

## 3.3 Line, Surface, and Volume Integrals | 线、面和体积积分
- $\int \mathbf{A} \cdot d\mathbf{l}$: line integral (work) / 线积分（功）
- $\int \mathbf{A} \cdot d\mathbf{S}$: surface integral (flux) / 面积分（通量）
- $\int \rho\,dV$: volume integral (charge) / 体积积分（电荷）

## 3.4 Del Operator / Nabla 算子
$$\nabla = \frac{\partial}{\partial x}\mathbf{a}_x + \frac{\partial}{\partial y}\mathbf{a}_y + \frac{\partial}{\partial z}\mathbf{a}_z$$

## 3.5 Gradient of a Scalar | 标量场的梯度
$$\nabla V = \frac{\partial V}{\partial x}\mathbf{a}_x + \frac{\partial V}{\partial y}\mathbf{a}_y + \frac{\partial V}{\partial z}\mathbf{a}_z$$
Direction of maximum increase of $V$ / $V$ 最大增加的方向。

## 3.6 Divergence of a Vector | 矢量场的散度
$$\nabla \cdot \mathbf{A} = \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z}$$
Measures "outflow" per unit volume / 度量单位体积的"净流出"。

### Divergence Theorem / 散度定理：
$$\int_V \nabla \cdot \mathbf{A}\,dV = \oint_S \mathbf{A} \cdot d\mathbf{S}$$

## 3.7 Curl of a Vector | 矢量场的旋度
$$\nabla \times \mathbf{A} = \begin{vmatrix} \mathbf{a}_x & \mathbf{a}_y & \mathbf{a}_z \\ \partial/\partial x & \partial/\partial y & \partial/\partial z \\ A_x & A_y & A_z \end{vmatrix}$$
Measures rotation / circulation density / 度量旋转/环量密度。

### Stokes's Theorem / 斯托克斯定理：
$$\int_S (\nabla \times \mathbf{A}) \cdot d\mathbf{S} = \oint_L \mathbf{A} \cdot d\mathbf{l}$$

## 3.8 Laplacian | 拉普拉斯算子
$$\nabla^2 V = \nabla \cdot \nabla V = \frac{\partial^2 V}{\partial x^2} + \frac{\partial^2 V}{\partial y^2} + \frac{\partial^2 V}{\partial z^2}$$

## 3.9 Classification of Vector Fields | 矢量场分类
- **Conservative**: $\nabla \times \mathbf{F} = 0$, $\oint \mathbf{F} \cdot d\mathbf{l} = 0$ / 保守场
- **Solenoidal**: $\nabla \cdot \mathbf{F} = 0$, $\oint \mathbf{F} \cdot d\mathbf{S} = 0$ / 无散场
- **Helmholtz theorem**: Any vector field can be decomposed into irrotational and solenoidal parts / 亥姆霍兹定理：任何矢量场可分解为无旋部分和无散部分
