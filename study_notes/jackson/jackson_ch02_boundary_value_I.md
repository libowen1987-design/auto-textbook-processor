# Jackson《Classical Electrodynamics》Ch2 — Boundary-Value Problems in Electrostatics I

> **Sections:** §2.1–§2.12 | **Book:** John David Jackson, 3rd Ed, Wiley 1999

---

## 2.1 — 2.2: Method of Images — Point Charge and Conducting Sphere

### Uncharged grounded conducting sphere

Point charge $q$ at $\mathbf{y}$ outside a grounded sphere of radius $a$ centered at origin.

**Image charge:** $q' = -\frac{a}{y} q$ placed at $\mathbf{y}' = \frac{a^2}{y^2} \mathbf{y}$ (the inversion point)

**Potential:**

$$
\Phi(\mathbf{x}) = \frac{1}{4\pi\epsilon_0} \left( \frac{q}{|\mathbf{x} - \mathbf{y}|} + \frac{q'}{|\mathbf{x} - \mathbf{y}'|} \right), \quad |\mathbf{x}| > a
$$

With the boundary condition $\Phi(|\mathbf{x}| = a) = 0$ satisfied by construction.

### Sphere held at potential $V$

Add a second image charge $q'' = 4\pi\epsilon_0 a V$ at the center.

### Sphere with net charge $Q$

Image charge $q' = -qa/y$ at $\mathbf{y}'$ as before, plus $q'' = Q - q'$ at the center.

---

## 2.3: Point Charge Near a Conducting Plane

### Grounded infinite plane

Charge $q$ at $(0,0,d)$. Image charge $-q$ at $(0,0,-d)$.

**Potential:**

$$
\Phi(x,y,z) = \frac{1}{4\pi\epsilon_0} \left[ \frac{q}{\sqrt{x^2 + y^2 + (z-d)^2}} - \frac{q}{\sqrt{x^2 + y^2 + (z+d)^2}} \right], \quad z > 0
$$

**Surface charge induced:**

$$
\sigma(x,y) = -\epsilon_0 \left.\frac{\partial \Phi}{\partial z}\right|_{z=0} = -\frac{q d}{2\pi (x^2 + y^2 + d^2)^{3/2}}
$$

**Force on charge:** $\mathbf{F} = -\frac{1}{4\pi\epsilon_0} \frac{q^2}{(2d)^2} \hat{\mathbf{z}}$ (attraction to plane)

---

## 2.4 — 2.5: Conducting Sphere in Uniform Field & Crossed Cylinders

### Sphere in uniform external field $\mathbf{E} = E_0 \hat{\mathbf{z}}$

Think of it as $q \to \infty$, $a \to \infty$ keeping $q/a^2 = 4\pi\epsilon_0 E_0$ fixed.

Equivalent to dipole image: $\mathbf{p} = 4\pi\epsilon_0 a^3 E_0 \hat{\mathbf{z}}$

**Potential:**

$$
\Phi(r,\theta) = -E_0 r \cos\theta + \frac{E_0 a^3}{r^2} \cos\theta
$$

- First term: external field
- Second term: induced dipole field

**Surface charge:**

$$
\sigma(\theta) = 3\epsilon_0 E_0 \cos\theta
$$

**Induced dipole moment:** $\mathbf{p} = 4\pi\epsilon_0 a^3 \mathbf{E}_0$

---

## 2.6 — 2.7: Green Function for the Sphere

### Dirichlet Green function for sphere of radius $a$

$$
G_D(\mathbf{x}, \mathbf{x}') = \frac{1}{|\mathbf{x} - \mathbf{x}'|} - \frac{a}{x' |\mathbf{x} - (a^2/x'^2) \mathbf{x}'|}
$$

In spherical coordinates:

$$
G_D(\mathbf{x}, \mathbf{x}') = \sum_{l=0}^{\infty} \frac{r_<^{\,l}}{r_>^{\,l+1}} P_l(\cos\gamma) - \sum_{l=0}^{\infty} \frac{a^{2l+1}}{(rr')^{l+1}} \frac{r_<^{\,l}}{r_>^{\,l+1}} P_l(\cos\gamma)
$$

where $r_<$ = min$(r, r')$, $r_>$ = max$(r, r')$, and $\gamma$ = angle between $\mathbf{x}$ and $\mathbf{x}'$.

Better form:

$$
G_D(\mathbf{x}, \mathbf{x}') = \sum_{l=0}^{\infty} \frac{1}{2l+1} \frac{r_<^{\,l}}{r_>^{\,l+1}}\left[1 - \left(\frac{a^2}{rr'}\right)^{l+1}\right] P_l(\cos\gamma)
$$

---

## 2.8: Orthogonal Functions & Expansions

### Key idea: expand potential in eigenfunctions of $\nabla^2$

For a given geometry (Cartesian, spherical, cylindrical), solve $\nabla^2 \Phi = 0$ by separation of variables.

**Sturm-Liouville theory:** Eigenfunctions form a complete orthogonal set.

**Fourier series:**

- $\Phi(x)$ on $[0,L]$: $\Phi(x) = \sum_{n=1}^\infty A_n \sin\frac{n\pi x}{L}$ (sine series for Dirichlet BC)
- Coefficients: $A_n = \frac{2}{L} \int_0^L \Phi(x) \sin\frac{n\pi x}{L} dx$

---

## 2.9 — 2.10: Separation of Variables — Cartesian Coordinates & Examples

### 2D Laplace equation (Cartesian)

$$
\frac{\partial^2 \Phi}{\partial x^2} + \frac{\partial^2 \Phi}{\partial y^2} = 0
$$

Separate: $\Phi(x,y) = X(x)Y(y)$

$$
\frac{1}{X}\frac{d^2 X}{dx^2} = -\frac{1}{Y}\frac{d^2 Y}{dy^2} = -\alpha^2
$$

Solutions:
- $X(x) = A \cos\alpha x + B \sin\alpha x$ (oscillatory if $\alpha^2 > 0$)
- $Y(y) = C e^{\alpha y} + D e^{-\alpha y}$ (exponential if $\alpha^2 > 0$)

### Example: Rectangular box with $\Phi = V$ on top face $y = b$, zero on others

$$
\Phi(x,y) = \sum_{n=1,3,5,\ldots}^\infty \frac{4V}{n\pi} \frac{\sinh(n\pi y/a)}{\sinh(n\pi b/a)} \sin\frac{n\pi x}{a}
$$

### 3D Cartesian: Parallel plates, infinite rectangular waveguide

General form:

$$
\Phi(x,y,z) = \sum_{m,n} A_{mn} \sin(\alpha_m x) \sin(\beta_n y) \sinh(\gamma_{mn} z)
$$

where $\alpha_m = m\pi/a$, $\beta_n = n\pi/b$, $\gamma_{mn}^2 = \alpha_m^2 + \beta_n^2$.

---

## 2.11: Separation of Variables — Spherical Coordinates

### Laplace equation in spherical coordinates

$$
\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2 \frac{\partial \Phi}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta \frac{\partial \Phi}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta} \frac{\partial^2 \Phi}{\partial\phi^2} = 0
$$

**Separation:** $\Phi(r,\theta,\phi) = \frac{U(r)}{r} P(\theta) Q(\phi)$

### Radial equation

$$
r^2 \frac{d^2 U}{dr^2} - l(l+1) U = 0 \quad \Rightarrow \quad U(r) = Ar^{l+1} + Br^{-l}
$$

So radial part: $R(r) = A_l r^l + B_l r^{-(l+1)}$

### Angular equation → Spherical harmonics

$$
Y_{lm}(\theta,\phi) = \sqrt{\frac{2l+1}{4\pi} \frac{(l-m)!}{(l+m)!}} P_l^m(\cos\theta) e^{im\phi}
$$

**Legendre polynomials** (for $m=0$, azimuthal symmetry):

$$
P_l(x) = \frac{1}{2^l l!} \frac{d^l}{dx^l} (x^2 - 1)^l
$$

**Orthogonality:**

$$
\int_{-1}^1 P_l(x) P_{l'}(x) dx = \frac{2}{2l+1} \delta_{ll'}
$$

### General solution to Laplace in spherical coordinates

$$
\Phi(r,\theta,\phi) = \sum_{l=0}^\infty \sum_{m=-l}^l \left[ A_{lm} r^l + B_{lm} r^{-(l+1)} \right] Y_{lm}(\theta,\phi)
$$

### Expansion of $1/|\mathbf{x} - \mathbf{x}'|$

$$
\frac{1}{|\mathbf{x} - \mathbf{x}'|} = \sum_{l=0}^\infty \frac{r_<^{\,l}}{r_>^{\,l+1}} P_l(\cos\gamma) = 4\pi \sum_{l=0}^\infty \sum_{m=-l}^l \frac{1}{2l+1} \frac{r_<^{\,l}}{r_>^{\,l+1}} Y_{lm}^*(\theta',\phi') Y_{lm}(\theta,\phi)
$$

---

## 2.12: Separation of Variables — Cylindrical Coordinates

### Laplace equation in cylindrical coordinates

$$
\frac{1}{\rho}\frac{\partial}{\partial\rho}\left(\rho \frac{\partial \Phi}{\partial\rho}\right) + \frac{1}{\rho^2}\frac{\partial^2 \Phi}{\partial\phi^2} + \frac{\partial^2 \Phi}{\partial z^2} = 0
$$

### Separation: $\Phi(\rho,\phi,z) = R(\rho) Q(\phi) Z(z)$

- $\frac{d^2 Q}{d\phi^2} + m^2 Q = 0 \Rightarrow Q(\phi) = e^{\pm im\phi}$
- $\frac{d^2 Z}{dz^2} - k^2 Z = 0 \Rightarrow Z(z) = e^{\pm kz}$
- $\rho^2 \frac{d^2 R}{d\rho^2} + \rho \frac{dR}{d\rho} + (k^2\rho^2 - m^2)R = 0 \Rightarrow$ **Bessel's equation**

### Bessel functions

$R(\rho) = J_m(k\rho)$ (regular at origin) or $N_m(k\rho)$ (singular at origin)

**Modified Bessel functions:**
- $R(\rho) = I_m(k\rho)$ or $K_m(k\rho)$ for imaginary arguments

### General solution

$$
\Phi(\rho,\phi,z) = \sum_m \int_0^\infty dk \, e^{im\phi} \left[ A_m(k) J_m(k\rho) e^{-k|z|} + B_m(k) J_m(k\rho) \sinh(kz) + \ldots \right]
$$

---

## Key Formulas Summary

| Concept | Formula |
|---|---|
| Sphere image charge | $q' = -\frac{a}{y} q$, $\mathbf{y}' = \frac{a^2}{y^2}\mathbf{y}$ |
| Plane image | $q$ at $d$ → $-q$ at $-d$ |
| Sphere in uniform E | $\Phi = -E_0 r\cos\theta + E_0 a^3 r^{-2}\cos\theta$ |
| $1/|\mathbf{x}-\mathbf{x}'|$ expansion | $4\pi \sum_{lm} \frac{1}{2l+1} \frac{r_<^l}{r_>^{l+1}} Y_{lm}^* Y_{lm}$ |
| Legendre orthogonality | $\int_{-1}^1 P_l P_{l'} = \frac{2}{2l+1}\delta_{ll'}$ |
| Spherical Laplace | $\Phi = \sum \left[ A_{lm}r^l + B_{lm}r^{-(l+1)} \right] Y_{lm}$ |
| Bessel equation | $\rho^2 R'' + \rho R' + (k^2\rho^2 - m^2)R = 0$ |

---

## Key Problems

- **Problem 2.1** — Two conducting hemispheres at $\pm V$ (Legendre expansion)
- **Problem 2.7** — Point charge and conducting sphere (force calculation)
- **Problem 2.10** — Conducting sphere in uniform field with surface charge
- **Problem 2.13** — Cylindrical cavity potential (Bessel functions)
- **Problem 2.22** — Green function for Dirichlet half-space
