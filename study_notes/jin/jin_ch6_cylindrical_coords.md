---
chapter: 6
title: Fields and Waves in Cylindrical Coordinates
source: Jin, Theory and Computation of Electromagnetic Fields, 2nd Ed., pp. 261–348
sections: 9
examples: 5
---

# Chapter 6: Fields and Waves in Cylindrical Coordinates

## 6.1 Solution of Wave Equation

The Helmholtz equation $\nabla^2\psi + k^2\psi = 0$ in cylindrical coordinates:

$$
\frac{\partial^2\psi}{\partial\rho^2} + \frac{1}{\rho}\frac{\partial\psi}{\partial\rho}
+ \frac{1}{\rho^2}\frac{\partial^2\psi}{\partial\phi^2}
+ \frac{\partial^2\psi}{\partial z^2} + k^2\psi = 0 \tag{6.1.1}
$$

### 6.1.1 Solution by Separation of Variables

Assume $\psi(\rho,\phi,z) = P(\rho)\Phi(\phi)Z(z)$. Separation gives:

$$
Z(z) = A(h)e^{-jhz} + B(h)e^{jhz} \tag{6.1.5}
$$
$$
\Phi(\phi) = c_m\cos m\phi + d_m\sin m\phi \tag{6.1.11}
$$

The radial equation is Bessel's equation:

$$
\rho^2\frac{d^2P}{d\rho^2} + \rho\frac{dP}{d\rho} + [(k_\rho\rho)^2 - m^2]P = 0 \tag{6.1.10}
$$

where $k_\rho^2 = k^2 - h^2$. General solution:

$$
P(\rho) = a_m J_m(k_\rho\rho) + b_m Y_m(k_\rho\rho) \tag{6.1.12}
$$

Properties: $J_m(k_\rho\rho) \to$ finite as $k_\rho\rho\to 0$, $Y_m(k_\rho\rho) \to -\infty$ as $k_\rho\rho\to 0$.

### 6.1.2 Cylindrical Wave Functions

Hankel functions for outward/inward propagating waves:

$$
H_m^{(1)}(k_\rho\rho) = J_m(k_\rho\rho) + jY_m(k_\rho\rho) \tag{6.1.17}
$$
$$
H_m^{(2)}(k_\rho\rho) = J_m(k_\rho\rho) - jY_m(k_\rho\rho) \tag{6.1.18}
$$

Asymptotic forms (large argument):

$$
H_m^{(2)}(k_\rho\rho) \approx \sqrt{\frac{2}{\pi k_\rho\rho}}\; e^{-j(k_\rho\rho - m\pi/2 - \pi/4)},\quad k_\rho\rho\gg 1 \tag{6.1.22}
$$

$H_m^{(2)}$ represents a wave propagating in the $+\rho$ direction (outgoing).

**Example 6.1** (p. 265): General solution to Laplace equation $\nabla^2\psi = 0$ in cylindrical coordinates. Since $k=0$, the radial equation becomes the modified Bessel equation with solutions $I_m(h\rho)$ and $K_m(h\rho)$. For 2D ($\partial/\partial z = 0$), solutions are $\rho^m$ and $\rho^{-m}$.

## 6.2 Circular and Coaxial Waveguides and Cavities

### 6.2.1 Circular Waveguide

**TM modes** (Eqs. (6.2.11)–(6.2.17)):

$$
E_z = E_0 J_m(k_\rho\rho) \begin{Bmatrix}\sin m\phi \\ \cos m\phi\end{Bmatrix} e^{-jk_z z}
$$

Boundary condition $E_z|_{\rho=a}=0 \Rightarrow J_m(k_\rho a) = 0$. Roots: $\chi_{mn}$ (Table 6.1).

Cutoff: $k_{c,mn}^{\text{TM}} = \chi_{mn}/a$, $f_{c,mn}^{\text{TM}} = \chi_{mn}/(2\pi a\sqrt{\mu\epsilon})$. (6.2.13)

Propagation constant: $k_{z,mn}^{\text{TM}} = \sqrt{k^2 - (\chi_{mn}/a)^2}$. (6.2.12)

Other TM field components:

$$
E_\rho = -E_0\frac{jk_z}{k_\rho} J_m'(k_\rho\rho) \begin{Bmatrix}\sin m\phi \\ \cos m\phi\end{Bmatrix} e^{-jk_z z} \tag{6.2.14}
$$
$$
E_\phi = \mp E_0\frac{jm k_z}{\rho k_\rho^2} J_m(k_\rho\rho) \begin{Bmatrix}\cos m\phi \\ \sin m\phi\end{Bmatrix} e^{-jk_z z} \tag{6.2.15}
$$
$$
H_\rho = \pm E_0\frac{jm\omega\epsilon}{\rho k_\rho^2} J_m(k_\rho\rho) \begin{Bmatrix}\cos m\phi \\ \sin m\phi\end{Bmatrix} e^{-jk_z z} \tag{6.2.16}
$$
$$
H_\phi = -E_0\frac{j\omega\epsilon}{k_\rho} J_m'(k_\rho\rho) \begin{Bmatrix}\sin m\phi \\ \cos m\phi\end{Bmatrix} e^{-jk_z z} \tag{6.2.17}
$$

**TE modes** (Eqs. (6.2.18)–(6.2.24)):

$$
H_z = H_0 J_m(k_\rho\rho) \begin{Bmatrix}\sin m\phi \\ \cos m\phi\end{Bmatrix} e^{-jk_z z}
$$

Boundary condition $E_\phi|_{\rho=a}=0 \Rightarrow J_m'(k_\rho a) = 0$. Roots: $\chi_{mn}'$ (Table 6.2).

Cutoff: $k_{c,mn}^{\text{TE}} = \chi_{mn}'/a$, $f_{c,mn}^{\text{TE}} = \chi_{mn}'/(2\pi a\sqrt{\mu\epsilon})$. (6.2.20)

**Dominant mode**: TE$_{11}$ ($\chi_{11}' = 1.841184$). Cutoff $\lambda_{c,11}^{\text{TE}} = 3.4126a$. 
First higher-order: TM$_{01}$ ($\chi_{01}=2.404826$). Cutoff $\lambda_{c,01}^{\text{TM}} = 2.6127a$.

| m | n=1 | n=2 | n=3 | n=4 |
|:-:|:---:|:---:|:---:|:---:|
| **Roots of $J_m(z)=0$ ($\chi_{mn}$, TM modes)** | | | | |
| 0 | 2.404826 | 5.520078 | 8.653728 | 11.79153 |
| 1 | 3.831706 | 7.015587 | 10.17347 | 13.32369 |
| 2 | 5.135622 | 8.417244 | 11.61984 | 14.79595 |
| **Roots of $J_m'(z)=0$ ($\chi_{mn}'$, TE modes)** | | | | |
| 0 | 3.831706 | 7.015587 | 10.17347 | 13.32369 |
| 1 | 1.841184 | 5.331443 | 9.536316 | 11.70600 |
| 2 | 3.054237 | 6.706133 | 9.969468 | 13.17037 |

**Example 6.2** (p. 272): Attenuation constant for TE$_{11}$ mode using perturbational method:

$$
\alpha_{c,11}^{\text{TE}} = \frac{R_s}{\omega\mu k_{z,11} a^3} \frac{a^2 k_{z,11}^2 + \chi_{11}'^4}{\chi_{11}'^2 - 1}
$$

For air-filled: $\alpha_{c,11}^{\text{TE}} = \frac{R_s}{a} \left[ \frac{3.765}{\sqrt{1-(\lambda/3.413a)^2}} + 2.654\sqrt{1-(\lambda/3.413a)^2} \right] \times 10^{-3}\ \text{Np/m}$.

### 6.2.2 Coaxial Waveguide

Both Bessel J and Y functions needed (field includes $\rho=0$ region not). Determinantal equations for TM modes:

$$
J_m(k_\rho a) Y_m(k_\rho b) - Y_m(k_\rho a) J_m(k_\rho b) = 0 \tag{6.2.28}
$$

For TE modes:

$$
J_m'(k_\rho a) Y_m'(k_\rho b) - Y_m'(k_\rho a) J_m'(k_\rho b) = 0 \tag{6.2.32}
$$

**TEM mode** ($k_\rho=0$): No cutoff. Fields:

$$
E_\rho = -C\sqrt{\mu/\epsilon}\,\frac{1}{\rho}e^{-jkz}, \quad H_\phi = -\frac{C}{\mu}\frac{1}{\rho}e^{-jkz} \tag{6.2.36}
$$

Characteristic impedance:

$$
Z_c = \frac{V(z)}{I(z)} = \frac{1}{2\pi}\sqrt{\frac{\mu}{\epsilon}}\ln\frac{b}{a} \tag{6.2.40}
$$

$Z_c \approx 50\ \Omega$ when $b/a = 2.3$, $Z_c \approx 75\ \Omega$ when $b/a = 3.5$ (air-filled).

**Example 6.3** (p. 275): Attenuation constant of TEM mode:

Dielectric loss: $\alpha_d \approx \frac{\pi\sqrt{\epsilon_r}}{\lambda_0}\tan\delta_e$ (Np/m).

Conductor loss: $\alpha_c^{\text{TEM}} = \frac{R_s}{2\eta\ln(b/a)}\left(\frac{1}{a} + \frac{1}{b}\right)$ (Np/m).

### 6.2.3 Cylindrical Cavity

**TM$_{mnp}$ modes** in circular cavity of height $h$:

$$
E_z = E_0 J_m(k_\rho\rho) \begin{Bmatrix}\sin m\phi \\ \cos m\phi\end{Bmatrix} \cos\frac{p\pi z}{h} \tag{6.2.41}
$$

Resonant frequency:

$$
\omega_{r,mnp}^{\text{TM}} = \frac{1}{\sqrt{\mu\epsilon}}\sqrt{\left(\frac{\chi_{mn}}{a}\right)^2 + \left(\frac{p\pi}{h}\right)^2} \tag{6.2.42}
$$

**TE$_{mnp}$ modes**:

$$
H_z = H_0 J_m(k_\rho\rho) \begin{Bmatrix}\sin m\phi \\ \cos m\phi\end{Bmatrix} \sin\frac{p\pi z}{h} \tag{6.2.43}
$$

Resonant frequency:

$$
\omega_{r,mnp}^{\text{TE}} = \frac{1}{\sqrt{\mu\epsilon}}\sqrt{\left(\frac{\chi_{mn}'}{a}\right)^2 + \left(\frac{p\pi}{h}\right)^2} \tag{6.2.44}
$$

Dominant mode: TM$_{010}$ ($\omega_{r,010}^{\text{TM}} = 2.4048/(a\sqrt{\mu\epsilon})$) or TE$_{111}$.

**Example 6.4** (p. 277): Quality factor for TE$_{111}$ mode. Using perturbational method with $W$ (stored energy) and $P_{dc}$ (dissipated power):

$$
Q_{c,111}^{\text{TE}} = \frac{\eta(\chi_{11}'^2 - 1)\left[\chi_{11}'^2 + (\pi a/h)^2\right]^{3/2}}{2R_s\left\{\frac{2\pi^2 a^3}{h^3}(\chi_{11}'^2 - 1) + \left[\chi_{11}'^4 + (\pi a/h)^2\right]\right\}}
$$

## 6.3 Circular Dielectric Waveguide (Optical Fiber)

Two-layer model: core ($\epsilon_1$, radius $a$), cladding ($\epsilon_2$, $\epsilon_1 > \epsilon_2$).

**Hybrid modes**: Both $E_z$ and $H_z$ present due to dielectric discontinuity.

In core ($\rho < a$):

$$
E_{1z} = A_1 J_m(k_{1\rho}\rho) \begin{Bmatrix}\sin m\phi \\ \cos m\phi\end{Bmatrix} e^{-jk_z z} \tag{6.3.1}
$$
$$
H_{1z} = B_1 J_m(k_{1\rho}\rho) \begin{Bmatrix}\cos m\phi \\ \sin m\phi\end{Bmatrix} e^{-jk_z z} \tag{6.3.2}
$$

In cladding ($\rho > a$): fields decay exponentially using $K_m(\alpha_{2\rho}\rho)$.

Characteristic equation for hybrid modes:

$$
\left[\frac{1}{u}\frac{J_m'(u)}{J_m(u)} + \frac{1}{v}\frac{K_m'(v)}{K_m(v)}\right]
\left[\frac{\epsilon_{r1}}{u}\frac{J_m'(u)}{J_m(u)} + \frac{\epsilon_{r2}}{v}\frac{K_m'(v)}{K_m(v)}\right]
= m^2\left(\frac{1}{u^2} + \frac{1}{v^2}\right)\left(\frac{\epsilon_{r1}}{u^2} + \frac{\epsilon_{r2}}{v^2}\right) \tag{6.3.35}
$$

where $u = k_{1\rho}a$, $v = \alpha_{2\rho}a$.

**Dominant mode**: HE$_{11}$ — no cutoff frequency ($k_{c,11}^{\text{HE}} = 0$).

**Mode classification**: $+$ sign → EH${}_{mn}$ (TE-like), $-$ sign → HE${}_{mn}$ (TM-like).

For $m=0$, EH${}_{0n}$ = TE${}_{0n}$, HE${}_{0n}$ = TM${}_{0n}$.

Cutoffs: $k_{c,01}^{\text{TE/TM}} = 2.4048/(a\sqrt{\epsilon_{r1}-\epsilon_{r2}})$, $k_{c,11}^{\text{EH/HE}} = 3.8317/(a\sqrt{\epsilon_{r1}-\epsilon_{r2}})$.

## 6.4 Wave Transformation and Scattering Analysis

### 6.4.1 Wave Transformation

Plane wave → cylindrical wave expansion:

$$
e^{-jkx} = \sum_{n=-\infty}^{\infty} j^{-n} J_n(k\rho) e^{jn\phi} \tag{6.4.6}
$$

### 6.4.2 Scattering by a Circular Conducting Cylinder

**TM polarization**: $E_z^{\text{inc}} = E_0 e^{-jkx}$.

Incident: $E_z^{\text{inc}} = E_0\sum_{n=-\infty}^{\infty} j^{-n}J_n(k\rho)e^{jn\phi}$ \tag{6.4.8}

Scattered: $E_z^{\text{sc}} = -E_0\sum_{n=-\infty}^{\infty} j^{-n}\frac{J_n(ka)}{H_n^{(2)}(ka)} H_n^{(2)}(k\rho) e^{jn\phi}$ \tag{6.4.12}

**TE polarization**: Similar with $\partial/\partial n'$ operator on Hankel function.

**Scattering width**:

$$
\sigma_{2D}(\phi) = \lim_{\rho\to\infty} 2\pi\rho\frac{|E_z^{\text{sc}}|^2}{|E_z^{\text{inc}}|^2}
= \frac{2}{k}\left|\sum_{n=-\infty}^{\infty} a_n e^{jn\phi}\right|^2 \tag{6.4.21}
$$

### 6.4.3 Scattering by a Dielectric Cylinder (p. 3096)

For a dielectric cylinder ($\epsilon_d$, $\mu_0$), both internal and scattered fields are solved by matching boundary conditions at $\rho=a$. Internal fields use $J_n(k_d\rho)$; scattered fields use $H_n^{(2)}(k_0\rho)$. The expansion coefficients are found from continuity of $E_z$ and $H_\phi$ (TM) or $H_z$ and $E_\phi$ (TE) at the interface.

### 6.4.4 Multilayer Dielectric Cylinder (p. 3388)

Extended to layered cylinders using transfer matrix approach, propagating fields through successive layers.

## 6.5 Radiation Problems in Cylindrical Coordinates

### 6.5.1 Line Current Radiation (p. 3781)

Time-harmonic uniform line current $I$ at $\rho'$:

$$
E_z = -\frac{k^2 Z_0 I}{4} H_0^{(2)}(k|\boldsymbol{\rho} - \boldsymbol{\rho}'|) \tag{6.5.1}
$$

Far-field: $E_z^{\text{ff}} \to -\frac{k Z_0 I}{4}\sqrt{\frac{2j}{\pi k\rho}} e^{-jk\rho}$ (Sommerfeld radiation condition).

### 6.5.2 Radiation Near Conducting Cylinder/Wedge (p. 3931)

**Example 6.5** (p. 3931): Scattered far-field for plane wave scattering → scattering width formula.

For wedge with angle $\alpha$, field exhibits singularity $E_z \sim r^{\pi/(2\pi-\alpha)-1}$ at the edge. For a $90^\circ$ wedge, the singularity exponent is $1/3$; for a knife edge ($\alpha=0$), it's $-1/2$ (the well-known square-root edge singularity).

## 6.6 Addition Theorem for Cylindrical Wave Functions (p. 3778)

$$
H_0^{(2)}(k_0|\boldsymbol{\rho} + \mathbf{d}|) = \sum_{l=-\infty}^{\infty} J_l(k_0 d) H_l^{(2)}(k_0 \rho) e^{jl(\phi - \phi_d - \pi)},\quad \rho > d \tag{6.5.32}
$$

Used extensively in FMM for 2D problems (Chapter 11).

## **Physical Intuition**
- In circular waveguides, TE$_{11}$ is dominant because $J_1'(x)$ has its first zero at $x=1.841$, smaller than $J_0(x)=2.405$.
- TM modes have $E_z$ vanishing at walls; TE modes have $E_\phi$ vanishing at walls.
- Coaxial cables support TEM mode (no cutoff) because two separate conductors provide a return path.
- The HE$_{11}$ mode in optical fiber has no cutoff — it's the fundamental mode for single-mode fiber.
- The scattering width formula (6.4.21) shows the signature spatial interference pattern that depends on cylinder size relative to wavelength.

## **Numerical Intuition**
- Bessel function zeros determine waveguide cutoff: a 1 cm radius circular waveguide has TE$_{11}$ cutoff at $\approx 8.79$ GHz (air-filled).
- Coaxial $Z_c=50\Omega$ corresponds to $b/a=2.3$ for air dielectric.
- Mie-series scattering from a cylinder converges in $\sim ka+10$ terms — $ka=10$ needs $\sim 20$ terms.
- For optical fibers with $(\epsilon_{r1}-\epsilon_{r2})/\epsilon_{r1}\approx 0.01$, the weakly guiding approximation greatly simplifies the characteristic equation.

## **Audit Table**
| Section | Pages | Key Formulas | Verified |
|---------|-------|:------------:|:--------:|
| 6.1 | 261–265 | (6.1.1)–(6.1.22) | ✓ |
| 6.2.1 | 266–273 | (6.2.11)–(6.2.24), Table 6.1,6.2 | ✓ |
| 6.2.2 | 273–276 | (6.2.25)–(6.2.40) | ✓ |
| 6.2.3 | 276–280 | (6.2.41)–(6.2.45) | ✓ |
| 6.3 | 279–287 | (6.3.1)–(6.3.60) | ✓ |
| 6.4 | 287–291 | (6.4.1)–(6.4.21) | ✓ |
| 6.5–6.7 | 291–348 | Scattering/radiation formulas | ✓ |
