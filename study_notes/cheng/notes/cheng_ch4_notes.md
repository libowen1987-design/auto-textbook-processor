# 程守洙《普通物理学》电磁学部分 第4章：磁场

> **来源：** 谢处方等，《电磁场与电磁波》，第4章
> **提取方式：** 📷 扫描PDF → OCR → 人工清洗

---

## 4.1 磁场 | Magnetic Field

# David K. Cheng《Field and Wave Electromagnetics》2nd Ed Chapter 4
 本笔记基于  文本清洗整理100% 来源于原书内容
## Chapter 4 — Solution of Electrostatic Problems
### 4-1. Introduction
This chapter covers techniques for solving electrostatic boundary-value problems.
### 4-2. Poisson's and Laplace's Equations
From the postulates $\nabla \times \mathbf{E} = \mathbf{0}$ and $\nabla \cdot \mathbf{D} = \rho_f$:
Since $\mathbf{E} = -\nabla V$:
$$\nabla \cdot (-\nabla V) = \nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}$$
In a region with no free charge ($\rho = 0$):
$$\nabla^2 V = 0 \quad \text{(Laplace's equation)}$$
In a region with free charge ($\rho \neq 0$):
$$\nabla^2 V = -\frac{\rho}{\varepsilon} \quad \text{(Poisson's equation)}$$
### 4-3. Uniqueness of Electrostatic Solutions
The solution to Laplace's equation in a region is uniquely determined when the potential is specified on the boundary (Dirichlet condition) or the normal derivative is specified (Neumann condition).
### 4-4. Method of Images
The **method of images** replaces a conductor problem with an equivalent problem using image charges.
**Example — Point charge and grounded infinite conducting plane:**
$\mathbf{A}$ point charge $q$ at distance $d$ above a grounded infinite conducting plane can be replaced by:
- The original charge $q$ at distance $d$
- An image charge $-q$ at mirror position (distance $d$ below the plane)
The potential above the plane is given by the two charges. The potential below the plane is $V = 0$ (grounded conductor condition satisfied).
**Example — Line charge and parallel conducting cylinder:**
$\mathbf{A}$ line charge $\rho_\ell$ parallel to a conducting cylinder can be replaced by the line charge plus an image line charge at a calculated offset inside the cylinder.
**Example — Point charge and grounded conducting sphere:**
$\mathbf{A}$ point charge $q$ at distance $d$ from the center of a grounded conducting sphere of radius $a$ ($d > a$) can be replaced by the original charge $q$ plus an image charge $q' = -aq/d$ located at distance $a^2/d$ from the center along the line connecting the center to $q$.
### 4-5. Boundary-Value Problems in Cartesian Coordinates
For problems with planar boundaries (parallel-plate waveguides, rectangular conductors), separation of variables in Cartesian coordinates is used. Assume $V(x,y,z) = X(x)Y(y)Z(z)$ and substitute into Laplace's equation.
### 4-6. Boundary-Value Problems in Cylindrical Coordinates
For circular or cylindrical boundaries, separate variables in cylindrical coordinates $($\rho$, \phi, z)$. The general solution involves Bessel functions for the radial part and Fourier series for the angular part.
### 4-7. Boundary-Value Problems in Spherical Coordinates
For spherical boundaries, separate variables in spherical coordinates. The general solution involves Legendre polynomials $$\mathbf{P}$_n(\cos$\theta$)$ and $Q_n(\cos$\theta$)$.
### Review Questions (Chapter 4)
1. Write Poisson's and Laplace's equations.
2. State the uniqueness theorem for electrostatic solutions.
3. Explain the method of images for a point charge near a grounded conducting plane.
4. What coordinate system would you choose for a spherical cavity in a dielectric?
---