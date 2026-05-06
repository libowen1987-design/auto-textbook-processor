# Jackson《Classical Electrodynamics》Ch3 — Boundary-Value Problems in Electrostatics II

> **Sections:** §3.1–§3.13 | **Book:** John David Jackson, 3rd Ed, Wiley 1999

---

## 3.1 — 3.3: Laplace Equation in Spherical Coordinates — Legendre Expansions

### Azimuthal symmetry ($m = 0$)

When no $\phi$ dependence, the general solution reduces to:

$$
\Phi(r,\theta) = \sum_{l=0}^\infty \left[ A_l r^l + B_l r^{-(l+1)} \right] P_l(\cos\theta)
$$

### Legendre polynomials

Recurrence: $(l+1)P_{l+1}(x) = (2l+1)xP_l(x) - lP_{l-1}(x)$

First few:

$$
P_0(x) = 1,\quad P_1(x) = x,\quad P_2(x) = \frac{1}{2}(3x^2 - 1),\quad P_3(x) = \frac{1}{2}(5x^3 - 3x)
$$

### Example: Conducting sphere of radius $a$ in uniform field $E_0 \hat{\mathbf{z}}$

Matching BCs at $r \to \infty$ ($\Phi \to -E_0 r \cos\theta$) and at $r = a$ ($\Phi = 0$):

$$
\Phi(r,\theta) = -E_0 r \cos\theta + E_0 \frac{a^3}{r^2} \cos\theta
$$

### Example: Charged ring on sphere

Potential on sphere surface: $\Phi(a,\theta) = V_0 \delta(\cos\theta - \cos\theta_0)$

Expansion coefficients: $A_l a^l = \frac{2l+1}{2} \int_{-1}^1 \Phi(a,\theta) P_l(\cos\theta) d(\cos\theta)$

---

## 3.4: Legendre Expansion of Coulomb Potential

### Very useful expansion

For $r_>$ = max$(r,a)$, $r_<$ = min$(r,a)$:

$$
\frac{1}{|\mathbf{r} - \mathbf{r}'|} = \frac{1}{\sqrt{r^2 + r'^2 - 2rr'\cos\gamma}} = \sum_{l=0}^\infty \frac{r_<^{\,l}}{r_>^{\,l+1}} P_l(\cos\gamma)
$$

### Applications

- Potential of ring of charge on axis
- Potential of charged disk
- Multipole expansion foundation

---

## 3.5 — 3.6: Cylindrical Coordinates & Bessel Functions

### Bessel equation

$$
x^2 \frac{d^2 J_m}{dx^2} + x \frac{dJ_m}{dx} + (x^2 - m^2) J_m = 0
$$

### Bessel functions of the first kind

Series:

$$
J_m(x) = \sum_{k=0}^\infty \frac{(-1)^k}{k! \, \Gamma(m + k + 1)} \left(\frac{x}{2}\right)^{m + 2k}
$$

### Asymptotic forms

- Small $x$: $J_m(x) \sim \frac{1}{\Gamma(m+1)} (x/2)^m$
- Large $x$: $J_m(x) \sim \sqrt{\frac{2}{\pi x}} \cos\left(x - \frac{m\pi}{2} - \frac{\pi}{4}\right)$

### Orthogonality

$$
\int_0^a J_m\left(\frac{x_{mn}}{a} \rho\right) J_m\left(\frac{x_{mp}}{a} \rho\right) \rho \, d\rho = \frac{a^2}{2} [J_{m+1}(x_{mn})]^2 \delta_{np}
$$

where $x_{mn}$ is the $n$-th zero of $J_m(x)$.

### Fourier-Bessel series

$$
f(\rho) = \sum_{n=1}^\infty c_n J_m\left(\frac{x_{mn}}{a} \rho\right), \quad c_n = \frac{2}{a^2 [J_{m+1}(x_{mn})]^2} \int_0^a f(\rho) J_m\left(\frac{x_{mn}}{a} \rho\right) \rho \, d\rho
$$

---

## 3.7 — 3.8: Cylindrical Boundary Value Problems

### Example: Potential inside a grounded cylinder with top at $V(\rho,\phi)$

Cylinder radius $a$, height $L$, grounded at sides and bottom.

$$
\Phi(\rho,\phi,z) = \sum_{m=-\infty}^\infty \sum_{n=1}^\infty A_{mn} J_m\left(\frac{x_{mn}}{a} \rho\right) e^{im\phi} \sinh\left(\frac{x_{mn}}{a} z\right)
$$

Coefficient $A_{mn}$ determined by the top boundary condition at $z = L$.

### Example: Dielectric cylinder in uniform field

Internal field is uniform (depolarization factor):

$$
E_{\text{in}} = \frac{2}{\epsilon_r + 1} E_0 \quad \text{(transverse field for cylinder)}
$$

---

## 3.9 — 3.11: Spherical Harmonics — General $m$

### Associated Legendre functions

$$
P_l^m(x) = (-1)^m (1 - x^2)^{m/2} \frac{d^m}{dx^m} P_l(x), \quad m \ge 0
$$

- $P_l^{-m}(x) = (-1)^m \frac{(l-m)!}{(l+m)!} P_l^m(x)$

### Spherical harmonics

$$
Y_{lm}(\theta,\phi) = \sqrt{\frac{2l+1}{4\pi} \frac{(l-m)!}{(l+m)!}} P_l^m(\cos\theta) e^{im\phi}
$$

### Orthogonality and completeness

$$
\int Y_{lm}^*(\theta,\phi) Y_{l'm'}(\theta,\phi) d\Omega = \delta_{ll'} \delta_{mm'}
$$
$$
\sum_{l=0}^\infty \sum_{m=-l}^l Y_{lm}^*(\theta',\phi') Y_{lm}(\theta,\phi) = \delta(\phi - \phi') \delta(\cos\theta - \cos\theta')
$$

### Addition theorem

$$
P_l(\cos\gamma) = \frac{4\pi}{2l+1} \sum_{m=-l}^l Y_{lm}^*(\theta',\phi') Y_{lm}(\theta,\phi)
$$

### Expansion of $1/|\mathbf{x} - \mathbf{x}'|$ — full form

$$
\frac{1}{|\mathbf{x} - \mathbf{x}'|} = 4\pi \sum_{l=0}^\infty \sum_{m=-l}^l \frac{1}{2l+1} \frac{r_<^{\,l}}{r_>^{\,l+1}} Y_{lm}^*(\theta',\phi') Y_{lm}(\theta,\phi)
$$

---

## 3.12: Green Function for Cylindrical Coordinates

### Dirichlet Green function inside a cylinder (radius $a$)

$$
G_D(\mathbf{x},\mathbf{x}') = \sum_{m=-\infty}^\infty \sum_{n=1}^\infty \frac{1}{\pi a^2} \frac{J_m\left(\frac{x_{mn}}{a}\rho\right) J_m\left(\frac{x_{mn}}{a}\rho'\right)}{[J_{m+1}(x_{mn})]^2} e^{im(\phi-\phi')} \frac{\sinh\left(\frac{x_{mn}}{a} z_<\right) \sinh\left(\frac{x_{mn}}{a} (L - z_>)\right)}{\frac{x_{mn}}{a} \sinh\left(\frac{x_{mn}}{a} L\right)}
$$

---

## 3.13: Eigenfunction Method for Poisson's Equation

### General approach

For a domain with eigenfunctions $\psi_n(\mathbf{x})$ satisfying $\nabla^2 \psi_n + \lambda_n \psi_n = 0$ and BCs:

1. Expand $\rho(\mathbf{x}) = \sum_n a_n \psi_n(\mathbf{x})$
2. Expand $\Phi(\mathbf{x}) = \sum_n c_n \psi_n(\mathbf{x})$
3. Plug into Poisson: $-\sum_n c_n \lambda_n \psi_n = -\frac{1}{\epsilon_0} \sum_n a_n \psi_n$
4. Therefore: $c_n = \frac{a_n}{\epsilon_0 \lambda_n}$
5. Solution: $\Phi(\mathbf{x}) = \sum_n \frac{a_n}{\epsilon_0 \lambda_n} \psi_n(\mathbf{x})$

### Green function via eigenfunctions

$$
G(\mathbf{x}, \mathbf{x}') = 4\pi \sum_n \frac{\psi_n(\mathbf{x}) \psi_n(\mathbf{x}')}{\lambda_n}
$$

---

## Key Formulas Summary

| Concept | Formula |
|---|---|
| Spherical Laplace (azimuthal) | $\Phi(r,\theta) = \sum [A_l r^l + B_l r^{-(l+1)}] P_l(\cos\theta)$ |
| $1/|\mathbf{x}-\mathbf{x}'|$ Legendre | $\sum_{l=0}^\infty \frac{r_<^l}{r_>^{l+1}} P_l(\cos\gamma)$ |
| Bessel orthogonality | $\int_0^a J_m(\alpha_n \rho) J_m(\alpha_p \rho) \rho d\rho = \frac{a^2}{2} [J_{m+1}(\alpha_n)]^2 \delta_{np}$ |
| Addition theorem | $P_l(\cos\gamma) = \frac{4\pi}{2l+1} \sum_m Y_{lm}^* Y_{lm}$ |
| Full $1/|\mathbf{x}-\mathbf{x}'|$ | $4\pi \sum_{lm} \frac{1}{2l+1} \frac{r_<^l}{r_>^{l+1}} Y_{lm}^* Y_{lm}$ |
| Eigenfunction Green fn | $G = 4\pi \sum_n \frac{\psi_n(\mathbf{x})\psi_n(\mathbf{x}')}{\lambda_n}$ |

---

## Key Problems

- **Problem 3.1** — Conducting sphere hemispheres at $\pm V$ (Legendre series)
- **Problem 3.3** — Charged conducting disk (oblate spheroidal coordinates)
- **Problem 3.5** — Potential of a circular aperture
- **Problem 3.10** — Point charge between two concentric spheres
- **Problem 3.14** — Fringing fields of a parallel-plate capacitor with Bessel functions
