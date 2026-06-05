# David K. Cheng《Field and Wave Electromagnetics》2nd Ed Chapter 2

> 本笔记基于 OCR 文本清洗整理，100% 来源于原书内容。

## Chapter 2 — Vector Analysis

### 2-1. Introduction

Vector analysis is the mathematical language of electromagnetics. A field is a spatial distribution of a quantity that may or may not be a function of time. This chapter develops the fundamentals of vector algebra and vector calculus.

### 2-2. Vector Addition and Subtraction

Given vectors $\mathbf{A}$ and $\mathbf{B}$, their sum and difference in Cartesian coordinates:
$$\mathbf{A} \pm \mathbf{B} = (A_x \pm B_x)\mathbf{a}_x + (A_y \pm B_y)\mathbf{a}_y + (A_z \pm B_z)\mathbf{a}_z$$

The magnitude:
$$|\mathbf{A}| = \sqrt{A_x^2 + A_y^2 + A_z^2}$$

### 2-3. Products of Vectors

#### 2-3.1. Scalar (Dot) Product

$$\mathbf{A} \cdot \mathbf{B} = AB\cos\theta = A_x B_x + A_y B_y + A_z B_z$$

Properties: commutative, distributive.

#### 2-3.2. Vector (Cross) Product

$$\mathbf{A} \times \mathbf{B} = \mathbf{a}_n AB\sin\theta$$

where $\mathbf{a}_n$ follows the right-hand rule. In Cartesian:
$$\mathbf{A} \times \mathbf{B} = (A_y B_z - A_z B_y)\mathbf{a}_x + (A_z B_x - A_x B_z)\mathbf{a}_y + (A_x B_y - A_z B_x)\mathbf{a}_z$$

Properties: anti-commutative, distributive, not associative.

#### 2-3.3. Product of Three Vectors

**Scalar triple product:**
$$\mathbf{A} \cdot (\mathbf{B} \times \mathbf{C}) = \mathbf{B} \cdot (\mathbf{C} \times \mathbf{A}) = \mathbf{C} \cdot (\mathbf{A} \times \mathbf{B}) = \text{Volume}$$

**Vector triple product:**
$$\mathbf{A} \times (\mathbf{B} \times \mathbf{C}) = \mathbf{B}(\mathbf{A} \cdot \mathbf{C}) - \mathbf{C}(\mathbf{A} \cdot \mathbf{B})$$

### 2-4. Orthogonal Coordinate Systems

#### 2-4.1. Cartesian (Rectangular) Coordinates $(x, y, z)$

$$\hat{\mathbf{x}}, \hat{\mathbf{y}}, \hat{\mathbf{z}} \quad \text{(mutually perpendicular, right-handed)}$$

Differential elements:
$$d\ell = dx\,\hat{\mathbf{x}} + dy\,\hat{\mathbf{y}} + dz\,\hat{\mathbf{z}}$$
$$dS = dy\,dz\,\hat{\mathbf{x}} + dx\,dz\,\hat{\mathbf{y}} + dx\,dy\,\hat{\mathbf{z}}$$
$$dv = dx\,dy\,dz$$

#### 2-4.2. Cylindrical Coordinates $(\rho, \phi, z)$

Conversion from Cartesian:
$$x = \rho\cos\phi,\quad y = \rho\sin\phi,\quad z = z$$
$$\rho = \sqrt{x^2+y^2},\quad \phi = \tan^{-1}\frac{y}{x},\quad z = z$$

Unit vectors: $\hat{\boldsymbol{\rho}}, \hat{\boldsymbol{\phi}}, \hat{\mathbf{z}}$ (right-handed: $\hat{\boldsymbol{\rho}} \times \hat{\boldsymbol{\phi}} = \hat{\mathbf{z}}$).

Differential elements:
$$d\ell = d\rho\,\hat{\boldsymbol{\rho}} + \rho\,d\phi\,\hat{\boldsymbol{\phi}} + dz\,\hat{\mathbf{z}}$$
$$dS = \rho\,d\phi\,dz\,\hat{\boldsymbol{\rho}} + d\rho\,dz\,\hat{\boldsymbol{\phi}} + \rho\,d\rho\,d\phi\,\hat{\mathbf{z}} \quad \text{(surface elements are perpendicular to respective unit vectors)}$$
$$dv = \rho\,d\rho\,d\phi\,dz$$

#### 2-4.3. Spherical Coordinates $(r, \theta, \phi)$

Conversion from Cartesian:
$$x = r\sin\theta\cos\phi,\quad y = r\sin\theta\sin\phi,\quad z = r\cos\theta$$

Unit vectors: $\hat{\mathbf{r}}, \hat{\boldsymbol{\theta}}, \hat{\boldsymbol{\phi}}$ (right-handed: $\hat{\boldsymbol{\theta}} \times \hat{\boldsymbol{\phi}} = \hat{\mathbf{r}}$).

Differential elements:
$$d\ell = dr\,\hat{\mathbf{r}} + r\,d\theta\,\hat{\boldsymbol{\theta}} + r\sin\theta\,d\phi\,\hat{\boldsymbol{\phi}}$$
$$dS = r\,d\theta\,r\sin\theta\,d\phi\,\hat{\mathbf{r}} + \text{...} \quad \text{(Jacobian: } r^2\sin\theta \text{)}$$
$$dv = r^2\sin\theta\,dr\,d\theta\,d\phi$$

### 2-5. Gradient of a Scalar Field

The gradient of a scalar function $V$ is a vector that points in the direction of maximum increase of $V$:

$$\nabla V = \frac{\partial V}{\partial x}\hat{\mathbf{x}} + \frac{\partial V}{\partial y}\hat{\mathbf{y}} + \frac{\partial V}{\partial z}\hat{\mathbf{z}} \quad \text{(Cartesian)}$$

In cylindrical: $\nabla V = \frac{\partial V}{\partial \rho}\hat{\boldsymbol{\rho}} + \frac{1}{\rho}\frac{\partial V}{\partial \phi}\hat{\boldsymbol{\phi}} + \frac{\partial V}{\partial z}\hat{\mathbf{z}}$

In spherical: $\nabla V = \frac{\partial V}{\partial r}\hat{\mathbf{r}} + \frac{1}{r}\frac{\partial V}{\partial \theta}\hat{\boldsymbol{\theta}} + \frac{1}{r\sin\theta}\frac{\partial V}{\partial \phi}\hat{\boldsymbol{\phi}}$

**Directional derivative** of $V$ along unit vector $\hat{\mathbf{u}}$:
$$\frac{dV}{d\ell_u} = \nabla V \cdot \hat{\mathbf{u}}$$

### 2-6. Divergence of a Vector Field

Divergence is a scalar measure of the "source" or "sink" strength of a vector field at a point:

$$\nabla \cdot \mathbf{A} = \lim_{\Delta v \to 0} \frac{\oint_S \mathbf{A} \cdot d\mathbf{S}}{\Delta v}$$

Cartesian: $\nabla \cdot \mathbf{A} = \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z}$

Cylindrical: $\nabla \cdot \mathbf{A} = \frac{1}{\rho}\frac{\partial(\rho A_\rho)}{\partial \rho} + \frac{1}{\rho}\frac{\partial A_\phi}{\partial \phi} + \frac{\partial A_z}{\partial z}$

Spherical: $\nabla \cdot \mathbf{A} = \frac{1}{r^2}\frac{\partial(r^2 A_r)}{\partial r} + \frac{1}{r\sin\theta}\frac{\partial(A_\theta)}{\partial \theta} + \frac{1}{r\sin\theta}\frac{\partial A_\phi}{\partial \phi}$

**Physical meaning:** $\nabla \cdot \mathbf{A} > 0$ indicates a source; $\nabla \cdot \mathbf{A} < 0$ indicates a sink.

### 2-7. Divergence Theorem

The divergence theorem (Gauss's theorem) converts a volume integral of a divergence to a closed surface integral:

$$\oint_S \mathbf{A} \cdot d\mathbf{S} = \int_v (\nabla \cdot \mathbf{A})\,dv$$

### 2-8. Curl of a Vector Field

Curl describes the rotational tendency of a vector field:

$$\nabla \times \mathbf{A} = \lim_{\Delta S \to 0} \frac{\oint_C \mathbf{A} \cdot d\boldsymbol{\ell}}{\Delta S} \quad \text{(direction = normal to } C\text{)}$$

Cartesian:
$$\nabla \times \mathbf{A} = \begin{vmatrix} \hat{\mathbf{x}} & \hat{\mathbf{y}} & \hat{\mathbf{z}} \\ \partial/\partial x & \partial/\partial y & \partial/\partial z \\ A_x & A_y & A_z \end{vmatrix}$$

**Physical meaning:** $\nabla \times \mathbf{A} = \mathbf{0}$ means the field is **irrotational** (conservative).

### 2-9. Stokes's Theorem

Stokes's theorem converts a surface integral of a curl to a closed line integral:

$$\oint_C \mathbf{A} \cdot d\boldsymbol{\ell} = \int_S (\nabla \times \mathbf{A}) \cdot d\mathbf{S}$$

### 2-10. Two Null Identities

**Null Identity I:**
$$\nabla \times (\nabla V) = \mathbf{0}$$
The curl of a gradient is identically zero (irrotational field).

**Null Identity II:**
$$\nabla \cdot (\nabla \times \mathbf{A}) = 0$$
The divergence of a curl is identically zero (solenoidal field).

### 2-11. Helmholtz's Theorem

Any vector field $\mathbf{F}$ that is defined in a simply connected region can be expressed as the sum of an irrotational (curl-free) component and a solenoidal (divergence-free) component:

$$\mathbf{F} = -\nabla V + \nabla \times \mathbf{A}$$

where $V$ is the scalar potential (from the irrotational part) and $\mathbf{A}$ is the vector potential (from the solenoidal part).

**Application:** In electrostatics, $\mathbf{E}$ is irrotational ($\nabla \times \mathbf{E} = \mathbf{0}$), so $\mathbf{E} = -\nabla V$. In magnetostatics, $\mathbf{B}$ is solenoidal ($\nabla \cdot \mathbf{B} = 0$), so $\mathbf{B} = \nabla \times \mathbf{A}$.

### Review Questions (Chapter 2)

1. What is the difference between dot product and cross product?
2. Write the expression for gradient in Cartesian coordinates.
3. State the divergence theorem and Stokes's theorem.
4. What is the physical meaning of divergence and curl?
5. State Helmholtz's theorem and its significance in electromagnetics.

---

