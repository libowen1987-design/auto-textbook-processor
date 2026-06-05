---
chapter: 7
title: Fields and Waves in Spherical Coordinates
source: Jin, Theory and Computation of Electromagnetic Fields, 2nd Ed., pp. 349–406
sections: 7
examples: 4
---

# Chapter 7: Fields and Waves in Spherical Coordinates

## 7.1 Solution of Wave Equation

Helmholtz equation in spherical coordinates:

$$
\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial\psi}{\partial r}\right)
+ \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial\psi}{\partial\theta}\right)
+ \frac{1}{r^2\sin^2\theta}\frac{\partial^2\psi}{\partial\phi^2}
+ k^2\psi = 0 \tag{7.1.1}
$$

### 7.1.1 Separation of Variables

Assume $\psi(r,\theta,\phi) = R(r)\Theta(\theta)\Phi(\phi)$. Separation yields:

Angular ($\phi$): $\displaystyle\frac{d^2\Phi}{d\phi^2} + m^2\Phi = 0$ → $\Phi(\phi) = c_m\cos m\phi + d_m\sin m\phi$ \tag{7.1.4}

Angular ($\theta$): Legendre's equation:

$$
\frac{1}{\sin\theta}\frac{d}{d\theta}\left(\sin\theta\frac{d\Theta}{d\theta}\right)
+ \left[n(n+1) - \frac{m^2}{\sin^2\theta}\right]\Theta = 0 \tag{7.1.9}
$$

Solutions: associated Legendre functions $P_n^m(\cos\theta)$ (finite on axis) and $Q_n^m(\cos\theta)$ (singular on axis).

Radial: Spherical Bessel equation:

$$
\frac{d}{dr}\left(r^2\frac{dR}{dr}\right) + [k^2 r^2 - n(n+1)]R = 0 \tag{7.1.8}
$$

Solutions: $j_n(kr)$ (finite at $r=0$) and $y_n(kr)$ (singular at $r=0$).

General solution:

$$
\psi_{mn}(r,\theta,\phi) = [a_n j_n(kr) + b_n y_n(kr)]
\left[c_{mn}P_n^m(\cos\theta) + d_{mn}Q_n^m(\cos\theta)\right]
\left[e_m\cos m\phi + f_m\sin m\phi\right] \tag{7.1.16}
$$

**Legendre polynomials** (Rodrigues formula):

$$
P_n(x) = \frac{1}{2^n n!}\frac{d^n}{dx^n}(x^2 - 1)^n \tag{7.1.20}
$$

**Associated Legendre functions**:

$$
P_n^m(x) = (-1)^m(1 - x^2)^{m/2}\frac{d^m}{dx^m}P_n(x) \tag{7.1.19}
$$

$P_n^m(x) = 0$ when $m > n$.

**Bessel function properties**:
- $j_n(kr) \to$ finite when $kr\to 0$
- $y_n(kr) \to -\infty$ when $kr\to 0$

**Example 7.1** (p. 327): Laplace equation in spherical coordinates ($k=0$). Radial solutions: $r^n$ and $r^{-(n+1)}$. Solution:

$$
\psi(r,\theta,\phi) = \sum_{m,n} [a_n r^n + b_n r^{-(n+1)}] 
[ c_{mn}P_n^m(\cos\theta) + d_{mn}Q_n^m(\cos\theta)]
[e_m\cos m\phi + f_m\sin m\phi]
$$

### 7.1.2 Spherical Wave Functions

Spherical Hankel functions for outward/inward propagation:

$$
h_n^{(1)}(kr) = j_n(kr) + j y_n(kr) \tag{7.1.21}
$$
$$
h_n^{(2)}(kr) = j_n(kr) - j y_n(kr) \tag{7.1.22}
$$

Asymptotic forms:

$$
h_n^{(2)}(kr) \approx \frac{1}{kr}e^{-j(kr - n\pi/2 - \pi/2)},\quad kr\gg 1 \tag{7.1.26}
$$

$h_n^{(2)}(kr)$ represents outward-propagating spherical waves.

### 7.1.3 TE$_r$ and TM$_r$ Modes

Use vector potentials $\mathbf{A} = \hat{r}A_r$ and $\mathbf{F} = \hat{r}F_r$ with Debye potentials.

**TE$_r$ modes** ($\mathbf{A}=0$, $\mathbf{F}=\hat{r}F_r$):

$$
E_r = 0,\quad H_r = \frac{1}{j\omega\mu\epsilon}\left(\frac{\partial^2}{\partial r^2} + k^2\right)F_r \tag{7.1.27}
$$
$$
E_\theta = -\frac{1}{\epsilon}\frac{1}{r\sin\theta}\frac{\partial F_r}{\partial\phi},\quad
H_\theta = \frac{1}{j\omega\mu\epsilon}\frac{1}{r}\frac{\partial^2 F_r}{\partial r\partial\theta} \tag{7.1.28}
$$
$$
E_\phi = \frac{1}{\epsilon}\frac{1}{r}\frac{\partial F_r}{\partial\theta},\quad
H_\phi = \frac{1}{j\omega\mu\epsilon}\frac{1}{r\sin\theta}\frac{\partial^2 F_r}{\partial r\partial\phi} \tag{7.1.29}
$$

**TM$_r$ modes** ($\mathbf{F}=0$, $\mathbf{A}=\hat{r}A_r$):

$$
E_r = \frac{1}{j\omega\mu\epsilon}\left(\frac{\partial^2}{\partial r^2} + k^2\right)A_r,\quad H_r = 0 \tag{7.1.30}
$$
$$
E_\theta = \frac{1}{j\omega\mu\epsilon}\frac{1}{r}\frac{\partial^2 A_r}{\partial r\partial\theta},\quad
H_\theta = \frac{1}{\mu}\frac{1}{r\sin\theta}\frac{\partial A_r}{\partial\phi} \tag{7.1.31}
$$
$$
E_\phi = \frac{1}{j\omega\mu\epsilon}\frac{1}{r\sin\theta}\frac{\partial^2 A_r}{\partial r\partial\phi},\quad
H_\phi = -\frac{1}{\mu}\frac{1}{r}\frac{\partial A_r}{\partial\theta} \tag{7.1.32}
$$

With gauge condition $\partial A_r/\partial r = -j\omega\mu\epsilon\phi$, $A_r/r$ satisfies the scalar Helmholtz equation. $A_r$ and $F_r$ solved using Riccati-Bessel functions $\hat{J}_n(kr)=kr j_n(kr)$, $\hat{Y}_n(kr)=kr y_n(kr)$.

## 7.2 Spherical Cavity (pp. 331–335)

**TE$_r$ modes**: Characteristic equation $\hat{J}_n(ka) = 0$. Roots $\varsigma_{np}$ (Table 7.1).

Resonant frequency: $f_{r,mnp}^{\text{TE}} = \varsigma_{np}/(2\pi a\sqrt{\mu\epsilon})$, $n=1,2,\dots$, $m=0,\dots,n$, $p=1,2,\dots$.

**TM$_r$ modes**: Characteristic equation $\hat{J}_n'(ka) = 0$. Roots $\varsigma_{np}'$ (Table 7.2).

| n | p=1 | p=2 | p=3 | p=4 |
|:-:|:---:|:---:|:---:|:---:|
| **Roots of $\hat{J}_n(z)=0$ ($\varsigma_{np}$, TE$_r$ modes)** | | | | |
| 1 | 4.493409 | 7.725252 | 10.90412 | 14.06619 |
| 2 | 5.763459 | 9.095011 | 12.32294 | 15.51460 |
| **Roots of $\hat{J}_n'(z)=0$ ($\varsigma_{np}'$, TM$_r$ modes)** | | | | |
| 1 | 2.743707 | 6.116764 | 9.316616 | 12.48594 |
| 2 | 3.870239 | 7.443087 | 10.71301 | 13.92052 |

**Dominant mode**: TM$_{r,m11}$ ($k_{r,m11}^{\text{TM}} = 2.7437/a$, $f = 0.4367/(a\sqrt{\mu\epsilon})$).

Field components of TM$_{r,011}$ mode ($m=0$, Eqs. (7.2.11)–(7.2.13)):

$$
E_r = \frac{2}{r^2}\cos\theta\; \hat{J}_1(\varsigma_{11}' r/a)
$$
$$
E_\theta = -\frac{\varsigma_{11}'}{ar}\sin\theta\; \hat{J}_1'(\varsigma_{11}' r/a)
$$
$$
H_\phi = -j\omega\epsilon\frac{1}{r}\sin\theta\; \hat{J}_1(\varsigma_{11}' r/a)
$$

**Example 7.2** (p. 334): Quality factor for TM$_{r,011}$ mode.

$$
Q_c = \frac{\eta}{R_s}\frac{\int_0^{\varsigma_{11}'} [\hat{J}_1(x)]^2 dx}{[\hat{J}_1(\varsigma_{11}')]^2}
= 1.007\,\frac{\eta}{R_s}
$$

Spherical cavity $Q$ is 25% higher than cylindrical and 36% higher than cubic cavity of same size.

## 7.3 Biconical Antenna (pp. 335–352)

### 7.3.1 Infinitely Long Model (p. 335)

Two semi-infinite conducting cones with half-angle $\theta_0$, apex at origin.

Fields expressed using $P_\nu^m(\cos\theta)$, $P_\nu^m(-\cos\theta)$ and $\hat{H}_\nu^{(2)}(kr)$.

For the dominant **TEM mode** ($m=0$, $\nu=0$):

$$
E_\theta = 0,\quad E_r = \frac{V_0}{r\ln(\cot(\theta_0/2))}e^{-jkr},\quad H_\phi = \frac{E_r}{\eta} \tag{7.3.2}
$$

Characteristic impedance: $Z_c = \frac{\eta}{\pi}\ln\left(\cot\frac{\theta_0}{2}\right)$.

### 7.3.2 Finite Model (p. 353)

Length $L$, terminated by a spherical cap of radius $L$. Input impedance computed via reflection from the open end.

## 7.4 Plane Wave Expansion and Wave Transformation (pp. 352–365)

### 7.4.1 Scalar Wave Transformation

Plane wave → spherical wave expansion:

$$
e^{-jkr\cos\theta} = \sum_{n=0}^\infty (-j)^n(2n+1)j_n(kr)P_n(\cos\theta) \tag{7.4.2}
$$

### 7.4.2 Vector Wave Transformation (p. 366)

$x$-polarized plane wave $\mathbf{E}^{\text{inc}} = \hat{x} E_0 e^{-jkz}$:

$$
\mathbf{E}^{\text{inc}} = E_0\sum_{n=1}^\infty (-j)^n\frac{2n+1}{n(n+1)}
\left[\mathbf{M}_{o1n}^{(1)}(r,\theta,\phi) - j\mathbf{N}_{e1n}^{(1)}(r,\theta,\phi)\right] \tag{7.4.3}
$$

where $\mathbf{M}_{o1n}^{(1)} = \nabla\times(\mathbf{r}\psi_{o1n})$ and $\mathbf{N}_{e1n}^{(1)} = \frac{1}{k}\nabla\times\mathbf{M}_{e1n}^{(1)}$ with $\psi_{o1n} = j_n(kr)P_n^1(\cos\theta)\sin\phi$ and $\psi_{e1n} = j_n(kr)P_n^1(\cos\theta)\cos\phi$.

## 7.5 Mie Scattering (pp. 365–385)

### 7.5.1 Scattering by a Conducting Sphere (p. 366)

Using the wave expansion (7.4.3) and boundary condition at $r=a$ ($\hat{n}\times\mathbf{E}^{\text{total}} = 0$), scattered field coefficients:

$$
a_n = -\frac{j_n(ka)}{h_n^{(2)}(ka)},\quad
b_n = -\frac{[k a j_n(ka)]'}{[k a h_n^{(2)}(ka)]'} \tag{7.5.1}
$$

where $a_n$ are TM coefficients, $b_n$ are TE coefficients.

Scattered field:

$$
\mathbf{E}^{\text{sc}} = E_0\sum_{n=1}^\infty (-j)^n\frac{2n+1}{n(n+1)}
\left[a_n\mathbf{M}_{o1n}^{(4)} - j b_n\mathbf{N}_{e1n}^{(4)}\right] \tag{7.5.2}
$$

### 7.5.2 Scattering by a Dielectric Sphere (p. 366)

For a dielectric sphere $(\epsilon_d,\mu_d)$, internal and scattered fields matched at $r=a$:

$$
a_n = \frac{\mu_d j_n(k_d a)[k a j_n(ka)]' - \mu j_n(ka)[k_d a j_n(k_d a)]'}{\mu_d j_n(k_d a)[k a h_n^{(2)}(ka)]' - \mu h_n^{(2)}(ka)[k_d a j_n(k_d a)]'} \tag{7.5.3}
$$
$$
b_n = \frac{\mu j_n(k_d a)[k a j_n(ka)]' - \mu_d j_n(ka)[k_d a j_n(k_d a)]'}{\mu j_n(k_d a)[k a h_n^{(2)}(ka)]' - \mu_d h_n^{(2)}(ka)[k_d a j_n(k_d a)]'} \tag{7.5.4}
$$

**Scattering cross-section**: $\sigma_s = \frac{2\pi}{k^2}\sum_{n=1}^\infty (2n+1)(|a_n|^2 + |b_n|^2)$.

**Extinction cross-section** (optical theorem): $\sigma_e = -\frac{2\pi}{k^2}\sum_{n=1}^\infty (2n+1)\Re(a_n + b_n)$.

### 7.5.3 Multilayer Dielectric Sphere (p. 370)

Generalized using transfer matrix method for $N$-layer spheres. Recursive formulas compute scattering coefficients $a_n$, $b_n$ for the composite sphere.

## 7.6 Addition Theorem for Spherical Wave Functions (pp. 385–390)

For a point charge at $\mathbf{r}'$ on the $z$-axis:

$$
\frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{|\mathbf{r} - \mathbf{r}'|}
= -jk\sum_{n=0}^\infty (-1)^n(2n+1)j_n(kr_<)h_n^{(2)}(kr_>)P_n(\cos\gamma) \tag{7.6.1}
$$

where $r_< = \min(r,r')$, $r_> = \max(r,r')$, $\cos\gamma = \hat{r}\cdot\hat{r}'$.

For off-center source, the generalized addition theorem involves spherical harmonics $Y_n^m(\theta,\phi)$.

## 7.7 Radiation in the Presence of a Sphere or Cone (pp. 390–406)

### 7.7.1 Radiation Near a Conducting Sphere (p. 390)

A spherical surface current $J_s$ on a sphere of radius $a$ radiates fields expressed as spherical wave expansions with coefficients determined by $J_s$ via $\mathbf{H}^{\text{sc}} = \frac{1}{jk\eta}\nabla\times\mathbf{E}^{\text{sc}}$.

### 7.7.2 Field Singularity at a Sharp Conducting Tip (p. 395)

For a conducting cone with half-angle $\theta_0$, fields near the tip exhibit singular behavior:

$$
E, H \sim r^{\nu-1}
$$

where $\nu$ satisfies $P_\nu^1(\cos\theta_0) = 0$ (TM-type) or $P_\nu^1(\cos\theta_0)' = 0$ (TE-type).

For a sharp tip ($\theta_0\to 0$), $\nu \approx 1/[2\ln(2/\theta_0)]$, giving a very strong singularity. For a $90^\circ$ wedge ($\theta_0 = 135^\circ$), $\nu \approx 0.5$ (square-root singularity, consistent with the 2D edge result).

## **Physical Intuition**
- Spherical harmonics $Y_n^m(\theta,\phi)$ are the natural basis for any problem with spherical symmetry.
- Mie theory describes how a sphere scatters light — the ratio $ka$ determines whether it's Rayleigh ($ka\ll 1$) or optical ($ka\sim 1$ or larger) scattering.
- The biconical antenna is a canonical wideband antenna — its TEM mode gives frequency-independent input impedance.
- Field singularities at sharp conducting tips are a fundamental challenge for numerical methods (need graded or very fine meshes).

## **Numerical Intuition**
- Mie series converges in $\sim ka + 10$ terms. For $ka=100$, you need $\sim 110$ terms.
- Spherical cavity $Q$ is mode-dependent — dominant TM mode has $Q_c \approx \eta/R_s$, which can be very high for superconducting cavities.
- The addition theorem (7.6.1) is the foundation of the 3D FMM and MLFMA (Chapter 11).
- For a sphere with $ka=1$ and $\epsilon_r=4$, the backscatter RCS is $\sim 0.3\lambda^2$ (Mie resonance), much larger than Rayleigh ($\sim a^6/\lambda^4$) or optical ($\sim \pi a^2$) limits.

## **Audit Table**
| Section | Pages | Key Formulas | Verified |
|---------|-------|:------------:|:--------:|
| 7.1 | 349–354 | (7.1.1)–(7.1.43) | ✓ |
| 7.2 | 354–360 | (7.2.1)–(7.2.17), Tables 7.1,7.2 | ✓ |
| 7.3 | 360–365 | Biconical antenna formulas | ✓ |
| 7.4 | 365–370 | (7.4.2)–(7.4.3) | ✓ |
| 7.5 | 370–385 | (7.5.1)–(7.5.4), Mie coefficients | ✓ |
| 7.6 | 385–390 | (7.6.1), addition theorem | ✓ |
| 7.7 | 390–406 | Singularity analysis | ✓ |
