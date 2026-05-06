---
chapter: 3
title: Potentials
source: Griffiths, Introduction to Electrodynamics, 4th Edition
pages: 113-165
---

# Chapter 3: Potentials

## 3.1 Laplace's Equation (pp. 113-125)

### 3.1.1 Introduction

The primary task of electrostatics is to find the electric field of a stationary charge distribution. While Coulomb's law (Eq. 2.8) gives the field directly, the integral is often intractable. The potential approach is more efficient:

$$V(\mathbf{r}) = \frac{1}{4\pi\epsilon_0}\int \frac{1}{\mathscr{r}}\rho(\mathbf{r}')\,d\tau'$$

(3.2)

In differential form, using Poisson's equation:

$$\nabla^2 V = -\frac{\rho}{\epsilon_0}$$

(3.3)

In charge-free regions ($\rho = 0$), this reduces to **Laplace's equation**:

$$\nabla^2 V = 0$$

(3.4)

In Cartesian coordinates:

$$\frac{\partial^2 V}{\partial x^2} + \frac{\partial^2 V}{\partial y^2} + \frac{\partial^2 V}{\partial z^2} = 0$$

(3.5)

Solutions to Laplace's equation are called **harmonic functions**.

### 3.1.2 Laplace's Equation in One Dimension

If $V = V(x)$ only, Laplace's equation becomes $d^2V/dx^2 = 0$, with general solution:

$$V(x) = mx + b$$

(3.6)

Two key properties of 1D harmonic functions:
1. **Mean value property:** $V(x) = \frac{1}{2}[V(x+a) + V(x-a)]$ for any $a$.
2. **No local extrema:** Extreme values occur only at boundaries.

物理直觉：在 1D 中，Laplace 方程是一条"平均指令"——每个点的势是其左右邻居的平均值，因此最极端的值必然在边界上。

### 3.1.3 Laplace's Equation in Two Dimensions

The 2D Laplace equation $\partial^2 V/\partial x^2 + \partial^2 V/\partial y^2 = 0$ is a partial differential equation with no simple closed-form general solution. Physical analogy: a stretched rubber membrane over a shaped frame.

**Properties (same as 1D):**
1. **Mean value property:** $V(x,y) = \frac{1}{2\pi R}\oint_{\text{circle}} V\,dl$ — the average over any circle equals the value at the center. This is the basis of the **relaxation method** for numerical solutions.
2. **No local extrema:** All hills and valleys occur at boundaries.

### 3.1.4 Laplace's Equation in Three Dimensions

**Mean value property:** The average potential over a spherical surface of radius $R$ centered at $\mathbf{r}$ equals $V(\mathbf{r})$ itself:

$$V(\mathbf{r}) = \frac{1}{4\pi R^2}\iint_{\text{sphere}} V\,da$$

**Proof (for a point charge outside the sphere):** Place $q$ on the $z$-axis at distance $z > R$ from origin. The potential on the sphere surface is $V = q/4\pi\epsilon_0 r$, where $r^2 = z^2 + R^2 - 2zR\cos\theta$. Computing the average:

$$V_{\text{ave}} = \frac{1}{4\pi R^2}\frac{q}{4\pi\epsilon_0}\int [z^2+R^2-2zR\cos\theta]^{-1/2}R^2\sin\theta\,d\theta d\phi = \frac{1}{4\pi\epsilon_0}\frac{q}{z}$$

which is precisely the potential at the center. By superposition, this holds for any external charges.

### 3.1.5 Boundary Conditions and Uniqueness Theorems

**First uniqueness theorem:** The solution to Laplace's equation in a volume $\mathcal{V}$ is **uniquely determined** if $V$ is specified on the boundary surface $S$.

*Proof:* Suppose $V_1$ and $V_2$ both satisfy Laplace's equation and equal boundary values. Let $V_3 \equiv V_1 - V_2$. Then $\nabla^2 V_3 = 0$ and $V_3 = 0$ on all boundaries. Since harmonic functions have no interior extrema, $V_3$ must be zero everywhere, so $V_1 = V_2$.

**Corollary:** The potential is uniquely determined if (a) the charge density $\rho$ throughout the region **and** (b) the value of $V$ on all boundaries are specified.

**Example 3.1** (p. 120): Inside an empty cavity entirely surrounded by conducting material, the potential is constant. Since the cavity wall is at constant $V_0$, and $V = V_0$ everywhere trivially satisfies Laplace's equation, the uniqueness theorem guarantees this is the only solution.

### 3.1.6 Conductors and the Second Uniqueness Theorem

**Second uniqueness theorem:** In a volume $\mathcal{V}$ surrounded by conductors and containing a specified charge density $\rho$, the electric field is uniquely determined if the **total charge on each conductor** is given (Fig. 3.6).

*Proof outline:* Consider two fields $\mathbf{E}_1$ and $\mathbf{E}_2$ satisfying the conditions. Define $\mathbf{E}_3 \equiv \mathbf{E}_1 - \mathbf{E}_2$, which satisfies $\nabla \cdot \mathbf{E}_3 = 0$ between conductors and $\oint \mathbf{E}_3 \cdot d\mathbf{a} = 0$ over each boundary. Using $\nabla \cdot (V_3\mathbf{E}_3) = V_3(\nabla\cdot\mathbf{E}_3) + \mathbf{E}_3\cdot(\nabla V_3) = -(E_3)^2$ and integrating over the volume, the divergence theorem gives $\int_V (E_3)^2 d\tau = 0$, so $\mathbf{E}_3 = 0$ everywhere.

**物理直觉：** 唯一性定理是解题的"执照"——只要你找到的函数满足 Laplace 方程和边界条件，它就一定是正确的解，无论你用什么奇技淫巧得到的。反射法、分离变量法等一切方法之所以可信，都建立在唯一性定理之上。

---

## 3.2 The Method of Images (pp. 125-130)

### 3.2.1 The Classic Image Problem

**Problem:** Point charge $q$ held a distance $d$ above an infinite grounded conducting plane ($z=0$, $V=0$). Find $V$ in the region $z>0$.

**Trick:** Replace the conducting plane by an **image charge** $-q$ at $(0,0,-d)$ — a completely different configuration with no conductor. The potential is:

$$V(x,y,z) = \frac{1}{4\pi\epsilon_0}\left(\frac{q}{\sqrt{x^2+y^2+(z-d)^2}} - \frac{q}{\sqrt{x^2+y^2+(z+d)^2}}\right)$$

(3.9)

This satisfies: (1) $V=0$ at $z=0$, (2) $V\to 0$ as $r\to\infty$, (3) correct charge $+q$ in $z>0$. By the uniqueness theorem, this is **the** solution for $z \ge 0$.

### 3.2.2 Induced Surface Charge

The surface charge density induced on the conductor is:

$$\sigma(x,y) = -\epsilon_0 \left.\frac{\partial V}{\partial z}\right|_{z=0} = -\frac{qd}{2\pi(x^2+y^2+d^2)^{3/2}}$$

(3.10)

Total induced charge:

$$Q = \int \sigma\,da = -q$$

(3.11)

As expected, the total induced charge equals $-q$.

### 3.2.3 Force and Energy

The force on $q$ is the same as the attraction between $+q$ and its image $-q$:

$$\mathbf{F} = -\frac{1}{4\pi\epsilon_0}\frac{q^2}{(2d)^2}\hat{\mathbf{z}}$$

(3.12)

**Energy is half** that of the two-charge system (only the $z>0$ region contributes):

$$W = -\frac{1}{4\pi\epsilon_0}\frac{q^2}{4d}$$

(3.14)

*Why half?* The energy stored in the field is $W = (\epsilon_0/2)\int E^2 d\tau$. With two point charges, both $z>0$ and $z<0$ contribute equally; with the conductor, only $z>0$ has a nonzero field.

### 3.2.4 Other Image Problems

**Example 3.2** (p. 128): Point charge $q$ at distance $a$ from the center of a grounded conducting sphere (radius $R$).

Image charge: $q' = -\frac{R}{a}q$ placed at distance $b = \frac{R^2}{a}$ from center (inside the sphere).

Potential outside the sphere:

$$V(r,\theta) = \frac{1}{4\pi\epsilon_0}\left(\frac{q}{\mathscr{r}} + \frac{q'}{\mathscr{r}'}\right)$$

(3.17)

Force on $q$:

$$F = \frac{1}{4\pi\epsilon_0}\frac{qq'}{(a-b)^2} = -\frac{1}{4\pi\epsilon_0}\frac{q^2 R a}{(a^2-R^2)^2}$$

(3.18)

For a sphere at potential $V_0$ (not grounded), add a second image charge $q'' = 4\pi\epsilon_0 R V_0$ at the center.

**物理直觉：** 反射法的核心是将边界条件"编码"成虚构的镜像电荷。平面反射是"照镜子"——镜像电荷与实物电荷关于平面对称、电性相反；球面反射则是"球面镜子"——镜像电荷在球内，大小按 $R/a$ 比例缩小。镜像电荷必须放在你关心的区域之外。

---

## 3.3 Separation of Variables (pp. 130-150)

### 3.3.1 Cartesian Coordinates — Example 3.3 (p. 131)

**Problem:** Two infinite grounded plates ($y=0$, $y=a$), closed at $x=0$ by a strip at potential $V_0(y)$. Find $V$ inside the slot.

Assume $V(x,y) = X(x)Y(y)$:

$$\frac{1}{X}\frac{d^2 X}{dx^2} + \frac{1}{Y}\frac{d^2 Y}{dy^2} = 0$$

Each term must be constant:

$$\frac{1}{X}\frac{d^2 X}{dx^2} = k^2,\quad \frac{1}{Y}\frac{d^2 Y}{dy^2} = -k^2$$

Solutions: $X(x) = Ae^{kx} + Be^{-kx}$, $Y(y) = C\sin ky + D\cos ky$.

Boundary conditions force $A=0$, $D=0$, $k = n\pi/a$ ($n=1,2,3,\dots$):

$$V(x,y) = \sum_{n=1}^\infty C_n e^{-n\pi x/a}\sin(n\pi y/a)$$

(3.30)

**Fourier's trick:** Multiply by $\sin(n'\pi y/a)$ and integrate $0$ to $a$:

$$C_n = \frac{2}{a}\int_0^a V_0(y)\sin(n\pi y/a)\,dy$$

(3.34)

For constant $V_0$:

$$C_n = \begin{cases} 0 & n\text{ even} \\ \frac{4V_0}{n\pi} & n\text{ odd} \end{cases}$$

(3.35)

The solution can be summed explicitly:

$$V(x,y) = \frac{2V_0}{\pi}\tan^{-1}\left(\frac{\sin(\pi y/a)}{\sinh(\pi x/a)}\right)$$

(3.37)

**Key concepts:** The separable solutions form a **complete** and **orthogonal** set. Completeness ensures any boundary function can be expanded; orthogonality ($\int_0^a \sin(n\pi y/a)\sin(n'\pi y/a)\,dy = \frac{a}{2}\delta_{nn'}$) enables Fourier's trick.

**Example 3.4** (p. 136): Rectangular pipe with top and bottom grounded, sides at $V_0$. Uses $\cosh$ functions due to symmetry:

$$V(x,y) = \frac{4V_0}{\pi}\sum_{n=1,3,5,\dots}\frac{1}{n}\frac{\cosh(n\pi x/a)}{\cosh(n\pi b/a)}\sin(n\pi y/a)$$

(3.42)

**Example 3.5** (p. 138): 3D rectangular pipe with end cap at $V_0(y,z)$. Double Fourier series:

$$V(x,y,z) = \sum_{n=1}^\infty\sum_{m=1}^\infty C_{n,m}e^{-\pi\sqrt{(n/a)^2+(m/b)^2}\,x}\sin(n\pi y/a)\sin(m\pi z/b)$$

(3.48)

$$C_{n,m} = \frac{4}{ab}\int_0^a\int_0^b V_0(y,z)\sin(n\pi y/a)\sin(m\pi z/b)\,dy\,dz$$

(3.50)

### 3.3.2 Spherical Coordinates

For azimuthally symmetric problems ($V$ independent of $\phi$), Laplace's equation in spherical coordinates becomes:

$$\frac{\partial}{\partial r}\left(r^2\frac{\partial V}{\partial r}\right) + \frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial V}{\partial\theta}\right) = 0$$

(3.54)

Let $V(r,\theta) = R(r)\Theta(\theta)$. Separation gives:

$$\frac{1}{R}\frac{d}{dr}\left(r^2\frac{dR}{dr}\right) = l(l+1), \qquad \frac{1}{\Theta\sin\theta}\frac{d}{d\theta}\left(\sin\theta\frac{d\Theta}{d\theta}\right) = -l(l+1)$$

(3.57)

Radial solution:

$$R(r) = Ar^l + \frac{B}{r^{l+1}}$$

(3.59)

Angular solutions are **Legendre polynomials** $P_l(\cos\theta)$.

| $l$ | $P_l(x)$ |
|-----|----------|
| 0 | $P_0(x) = 1$ |
| 1 | $P_1(x) = x$ |
| 2 | $P_2(x) = (3x^2-1)/2$ |
| 3 | $P_3(x) = (5x^3-3x)/2$ |
| 4 | $P_4(x) = (35x^4-30x^2+3)/8$ |
| 5 | $P_5(x) = (63x^5-70x^3+15x)/8$ |

**Rodrigues formula:** $P_l(x) \equiv \frac{1}{2^l l!}\left(\frac{d}{dx}\right)^l (x^2-1)^l$ (3.62), with $P_l(1) = 1$.

**General solution** with azimuthal symmetry:

$$V(r,\theta) = \sum_{l=0}^\infty \left(A_l r^l + \frac{B_l}{r^{l+1}}\right)P_l(\cos\theta)$$

(3.65)

**Orthogonality:**

$$\int_{-1}^1 P_l(x)P_{l'}(x)\,dx = \int_0^\pi P_l(\cos\theta)P_{l'}(\cos\theta)\sin\theta\,d\theta = \frac{2}{2l+1}\delta_{ll'}$$

(3.68)

**Example 3.6** (p. 143): Potential inside a sphere with specified $V_0(\theta)$. Since $r\to 0$ requires $B_l=0$:

$$V(r,\theta) = \sum_{l=0}^\infty A_l r^l P_l(\cos\theta), \quad A_l = \frac{2l+1}{2R^l}\int_0^\pi V_0(\theta)P_l(\cos\theta)\sin\theta\,d\theta$$

(3.66, 3.69)

**Example 3.7** (p. 145): Potential outside a sphere. $r\to\infty$ requires $A_l=0$:

$$V(r,\theta) = \sum_{l=0}^\infty \frac{B_l}{r^{l+1}} P_l(\cos\theta), \quad B_l = \frac{2l+1}{2}R^{l+1}\int_0^\pi V_0(\theta)P_l(\cos\theta)\sin\theta\,d\theta$$

(3.72, 3.73)

**Example 3.8** (p. 145): Uncharged metal sphere in uniform external field $\mathbf{E}_0 = E_0\hat{\mathbf{z}}$.

Boundary conditions: $V=0$ at $r=R$, and $V \to -E_0 r\cos\theta$ as $r\to\infty$.

Only $l=1$ contributes:

$$V(r,\theta) = -E_0\left(r - \frac{R^3}{r^2}\right)\cos\theta$$

(3.76)

Induced surface charge: $\sigma(\theta) = 3\epsilon_0 E_0\cos\theta$ (3.77). Positive on northern hemisphere, negative on southern.

**Example 3.9** (p. 147): Spherical shell with surface charge $\sigma_0(\theta)$.

Interior: $V_{\text{in}} = \sum A_l r^l P_l(\cos\theta)$, exterior: $V_{\text{out}} = \sum B_l r^{-(l+1)}P_l(\cos\theta)$.

Continuity at $r=R$ gives $B_l = A_l R^{2l+1}$. The discontinuity in $\partial V/\partial r$ gives:

$$A_l = \frac{1}{2\epsilon_0 R^{l-1}}\int_0^\pi \sigma_0(\theta)P_l(\cos\theta)\sin\theta\,d\theta$$

(3.84)

For $\sigma_0 = k\cos\theta = kP_1(\cos\theta)$: $V_{\text{in}} = \frac{k}{3\epsilon_0}r\cos\theta$, $V_{\text{out}} = \frac{kR^3}{3\epsilon_0}\frac{1}{r^2}\cos\theta$.

**物理直觉：** 分离变量法将偏微分方程转化为常微分方程。笛卡尔坐标下解是正弦/余弦与指数/双曲函数的乘积；球坐标下则是 $r^l$ 或 $r^{-(l+1)}$ 与 Legendre 多项式的乘积。关键在于利用 Fourier 技巧（正交性）来匹配边界条件。

---

## 3.4 Multipole Expansion (pp. 151-165)

### 3.4.1 Approximate Potentials at Large Distances

For a localized charge distribution, far away it "looks like" a point charge. But if $Q=0$, we need a more systematic expansion.

**Generating function for Legendre polynomials:**

$$\frac{1}{\mathscr{r}} = \frac{1}{r}\sum_{n=0}^\infty \left(\frac{r'}{r}\right)^n P_n(\cos\alpha)$$

(3.94)

where $\alpha$ is the angle between $\mathbf{r}$ and $\mathbf{r}'$.

**Multipole expansion of the potential:**

$$V(\mathbf{r}) = \frac{1}{4\pi\epsilon_0}\sum_{n=0}^\infty \frac{1}{r^{n+1}}\int (r')^n P_n(\cos\alpha)\rho(\mathbf{r}')\,d\tau'$$

(3.95)

Explicitly:

$$V(\mathbf{r}) = \frac{1}{4\pi\epsilon_0}\Bigg[\frac{1}{r}\int \rho\,d\tau' + \frac{1}{r^2}\int r'\cos\alpha\,\rho\,d\tau' + \frac{1}{r^3}\int (r')^2\left(\frac{3}{2}\cos^2\alpha - \frac{1}{2}\right)\rho\,d\tau' + \cdots\Bigg]$$

(3.96)

| Term | Name | Potential ~ | Multipole moment |
|------|------|-------------|------------------|
| $n=0$ | Monopole | $1/r$ | $Q = \int \rho\,d\tau$ |
| $n=1$ | Dipole | $1/r^2$ | $\mathbf{p} = \int \mathbf{r}'\rho\,d\tau'$ |
| $n=2$ | Quadrupole | $1/r^3$ | $Q_{ij} = \frac{1}{2}\int (3r_i'r_j' - r'^2\delta_{ij})\rho\,d\tau'$ |
| $n=3$ | Octopole | $1/r^4$ | (third-rank tensor) |

### 3.4.2 The Monopole and Dipole Terms

**Monopole:** $V_{\text{mon}}(r) = \frac{1}{4\pi\epsilon_0}\frac{Q}{r}$ (3.97)

**Dipole moment:** $\displaystyle \mathbf{p} \equiv \int \mathbf{r}'\rho(\mathbf{r}')\,d\tau'$ (3.98)

For discrete charges: $\displaystyle \mathbf{p} = \sum_{i=1}^n q_i \mathbf{r}'_i$ (3.100)

For a physical dipole ($\pm q$ separated by $\mathbf{d}$): $\mathbf{p} = q\mathbf{d}$ (3.101)

**Dipole potential:**

$$V_{\text{dip}}(\mathbf{r}) = \frac{1}{4\pi\epsilon_0}\frac{\mathbf{p}\cdot\hat{\mathbf{r}}}{r^2}$$

(3.99)

### 3.4.3 Origin Dependence

- **Monopole moment** $Q$ is **independent** of origin.
- **Dipole moment** is independent of origin **iff** $Q=0$. Proof: shifting origin by $\mathbf{a}$ gives $\bar{\mathbf{p}} = \mathbf{p} - Q\mathbf{a}$.

**物理直觉：** 如果一个系统总电荷为零，则偶极矩是唯一定义的（与原点无关）。这正是我们平时说"这个分子的偶极矩是 $p$"时成立的前提——分子是中性的。

### 3.4.4 Electric Field of a Dipole

For a pure dipole $\mathbf{p}=p\hat{\mathbf{z}}$ at the origin:

$$\mathbf{E}_{\text{dip}}(r,\theta) = \frac{p}{4\pi\epsilon_0 r^3}(2\cos\theta\,\hat{\mathbf{r}} + \sin\theta\,\hat{\boldsymbol{\theta}})$$

(3.103)

**Coordinate-free form:**

$$\mathbf{E}_{\text{dip}}(\mathbf{r}) = \frac{1}{4\pi\epsilon_0}\frac{1}{r^3}[3(\mathbf{p}\cdot\hat{\mathbf{r}})\hat{\mathbf{r}} - \mathbf{p}]$$

(3.104)

**Complete dipole field (including contact term):**

$$\mathbf{E}_{\text{dip}}(\mathbf{r}) = \frac{1}{4\pi\epsilon_0}\frac{1}{r^3}[3(\mathbf{p}\cdot\hat{\mathbf{r}})\hat{\mathbf{r}} - \mathbf{p}] - \frac{1}{3\epsilon_0}\mathbf{p}\,\delta^3(\mathbf{r})$$

(3.106)

The delta-function term is crucial; it was missed in the original gradient calculation because differentiation fails at $\mathbf{r}=0$.

**Hierarchy of field falloff:** Monopole $\sim 1/r^2$, dipole $\sim 1/r^3$, quadrupole $\sim 1/r^4$, octopole $\sim 1/r^5$, etc.

---

### Chapter Summary: Key Formula Table

| Concept | Formula |
|---------|---------|
| Laplace's equation | $\nabla^2 V = 0$ (3.4) |
| Image charge (plane) | $-q$ at mirror point |
| Image charge (sphere) | $q' = -\frac{R}{a}q$, $b = R^2/a$ |
| Separable solution (Cartesian) | $V = (Ae^{kx}+Be^{-kx})(C\sin ky+D\cos ky)$ (3.27) |
| Separable solution (spherical) | $V = \sum (A_l r^l + B_l/r^{l+1})P_l(\cos\theta)$ (3.65) |
| Legendre orthogonality | $\int_{-1}^1 P_l P_{l'} dx = \frac{2}{2l+1}\delta_{ll'}$ (3.68) |
| Multipole expansion | $V = \frac{1}{4\pi\epsilon_0}\sum \frac{1}{r^{n+1}}\int (r')^n P_n(\cos\alpha)\rho\,d\tau'$ (3.95) |
| Dipole moment | $\mathbf{p} = \int \mathbf{r}'\rho\,d\tau'$ (3.98) |
| Dipole field | $\mathbf{E} = \frac{1}{4\pi\epsilon_0 r^3}[3(\mathbf{p}\cdot\hat{\mathbf{r}})\hat{\mathbf{r}} - \mathbf{p}]$ (3.104) |

**物理直觉（全章回顾）：** 第三章建立了求解静电势的三大工具箱——反射法（用镜像电荷代替边界）、分离变量法（将 PDE 化为 ODE 并用 Fourier 技巧匹配边界）、多极展开（大距离下用有限个矩量近似任意分布）。唯一性定理是贯穿全章的灵魂：它确保任何"碰巧"找到的解都是正确的，给了物理学家无穷的创造性自由。
