# Chapter 10: Scattering and Diffraction / 散射与衍射

> Jackson *Classical Electrodynamics*, 3rd Ed, §10.1–10.12

---

## 1. Overview / 概述

When an electromagnetic wave encounters an obstacle or inhomogeneity, it **scatters** — part of the energy is reradiated in all directions. **Diffraction** is the limiting case where the scatterer is an aperture or edge in an otherwise opaque screen.

**Central theme**: Given an incident wave $\mathbf{E}_{\text{inc}}$, what is the scattered field $\mathbf{E}_{\text{sc}}$ in the far zone?

---

## 2. 散射基本理论 (Fundamentals of Scattering) / 散射基本理论 (Fundamentals of Scattering)

### 2.1 散射振幅与截面 (Scattering Amplitude and Cross Section) / 2.1 散射振幅与截面 (散射 Amplitude与Cross Section)

**Scattering amplitude** $\mathbf{f}(\mathbf{n}, \mathbf{n}_0)$:

$$
\mathbf{E}_{\text{sc}}(\mathbf{x}) \sim \frac{e^{ikr}}{r} \mathbf{f}(\mathbf{n}, \mathbf{n}_0)
$$

where $\mathbf{n}_0$ = incident direction, $\mathbf{n}$ = observation direction.

**Differential scattering cross section**:

$$
\frac{d\sigma}{d\Omega} = \frac{\text{power scattered into } d\Omega \text{ per unit solid angle}}{\text{incident power per unit area}} = |\mathbf{f}(\mathbf{n}, \mathbf{n}_0)|^2
$$

**Total cross section**:

$$
\sigma_{\text{tot}} = \int \frac{d\sigma}{d\Omega} d\Omega
$$

**Optical theorem** (relates forward scattering to total cross section):

$$
\sigma_{\text{tot}} = \frac{4\pi}{k} \operatorname{Im}\left\mathbf{f}(\mathbf{n}_0, \mathbf{n}_0) \cdot \hat{\epsilon}^*\right
$$

This is a powerful constraint: any scattering process must extract energy from the forward direction.

### 2.2 散射的矢势公式 (Vector Potential Formulation) / 2.2 散射的矢势公式 (Vector Potential Formulation)

From §9.3, the scattered field from a current induced in the scatterer:

$$
\mathbf{A}_{\text{sc}}(\mathbf{x}) = \frac{\mu_0}{4\pi} \frac{e^{ikr}}{r} \int_V \mathbf{J}_{\text{ind}}(\mathbf{x}') e^{-ik\mathbf{n} \cdot \mathbf{x}'} d^3x'
$$

---

## 3. 瑞利散射 (Rayleigh Scattering) / 瑞利散射 (Rayleigh Scattering)

Valid when scatterer size $d \ll \lambda$ (e.g., molecules, small particles).

### 3.1 电偶极散射 (Electric Dipole Scattering) / 3.1 电偶极散射 (Electric Dipole 散射)

The incident field induces an oscillating dipole moment:

$$
\mathbf{p} = \alpha \mathbf{E}_{\text{inc}}, \quad \alpha = \text{polarizability}
$$

For a small dielectric sphere of radius $a$, $\alpha = 4\pi\epsilon_0 a^3 \frac{\epsilon_r - 1}{\epsilon_r + 2}$.

**Scattered fields** (from electric dipole radiation):

$$
\mathbf{E}_{\text{sc}} = \frac{k^2}{4\pi\epsilon_0} \frac{e^{ikr}}{r} (\mathbf{n} \times \mathbf{p}) \times \mathbf{n}
$$

**Differential cross section** (unpolarized incident light):

$$
\frac{d\sigma}{d\Omega} = k^4 |\alpha|^2 \frac{1 + \cos^2\theta}{2}
$$

**Total cross section**:

$$
\sigma_{\text{Rayleigh}} = \frac{8\pi}{3} k^4 |\alpha|^2 \propto \frac{1}{\lambda^4}
$$

This $\lambda^{-4}$ scaling explains why the **sky is blue** and **sunsets are red**.

### 3.2 随机介质中的散射 (Scattering in Random Media) / 3.2 随机介质中的散射 (散射 in Random Media)

For a dilute collection of $N$ scatterers per unit volume:

$$
\sigma_{\text{extinction}} = N \sigma_{\text{scat}}
$$

**Beer-Lambert law**: $I(z) = I_0 e^{-N\sigma_{\text{scat}} z}$

---

## 4. 米氏散射 (Mie Scattering) / 米氏散射 (Mie Scattering)

Valid for spherical particles of **any size** relative to $\lambda$. Solved by Gustav Mie (1908) — full analytic solution using vector spherical harmonics.

### 4.1 散射系数 (Scattering Coefficients $a_l, b_l$) / 4.1 散射系数 (散射 Coefficients $a_l, b_l$)

The incident plane wave is expanded in vector spherical harmonics. The scattered field is expressed in terms of Mie coefficients:

$$
a_l = \frac{m\psi_l(mx)\psi'_l(x) - \psi_l(x)\psi'_l(mx)}{m\psi_l(mx)\xi'_l(x) - \xi_l(x)\psi'_l(mx)}
$$

$$
b_l = \frac{\psi_l(mx)\psi'_l(x) - m\psi_l(x)\psi'_l(mx)}{\psi_l(mx)\xi'_l(x) - m\xi_l(x)\psi'_l(mx)}
$$

where:
- $x = ka = 2\pi a / \lambda$ (size parameter)
- $m = n_{\text{sphere}} / n_{\text{medium}}$ (relative refractive index)
- $\psi_l(\rho) = \rho j_l(\rho)$, $\xi_l(\rho) = \rho h_l^{(1)}(\rho)$ (Ricatti-Bessel functions)

### 4.2 散射截面和消光截面 (Cross Sections) / 4.2 散射截面和消光截面 (Cross Sections)

**Extinction cross section**:

$$
\sigma_{\text{ext}} = \frac{2\pi}{k^2} \sum_{l=1}^\infty (2l+1) \operatorname{Re}(a_l + b_l)
$$

**Scattering cross section**:

$$
\sigma_{\text{scat}} = \frac{2\pi}{k^2} \sum_{l=1}^\infty (2l+1) (|a_l|^2 + |b_l|^2)
$$

**Absorption cross section**: $\sigma_{\text{abs}} = \sigma_{\text{ext}} - \sigma_{\text{scat}}$

### 4.3 瑞利极限与几何极限 (Limiting Cases) / 4.3 瑞利极限与几何极限 (Limiting Cases)

| Regime | Size parameter | Behavior |
|--------|---------------|----------|
| Rayleigh | $x \ll 1$ | $\sigma \propto \lambda^{-4}$, mainly $l=1$ |
| Resonance | $x \sim 1$ | Oscillations in $\sigma$, surface plasmons |
| Geometric | $x \gg 1$ | $\sigma \to 2\pi a^2$ (extinction paradox!) |

**Extinction paradox** ($x \gg 1$): $\sigma_{\text{ext}} \to 2\pi a^2$, twice the geometric cross section $\pi a^2$. The extra $\pi a^2$ comes from diffraction around the edges (Babinet's principle).

---

## 5. 夫琅禾费衍射 (Fraunhofer Diffraction) / 夫琅禾费衍射 (Fraunhofer Diffraction)

Far-field diffraction from an aperture. The scalar approximation (Huygens-Fresnel principle):

$$
U(P) = \frac{i e^{ikr}}{\lambda r} \iint_{\text{aperture}} U_0 e^{-ik(\xi u + \eta v)} d\xi d\eta
$$

where $(u,v) = (\sin\theta\cos\phi, \sin\theta\sin\phi)$ are direction cosines.

**This is a 2D Fourier transform** of the aperture field.

### 5.1 矩孔 (Rectangular Aperture) / 5.1 矩孔 (Rectangular Aperture)

Aperture $a \times b$:

$$
I(\theta_x, \theta_y) = I_0 \left(\frac{\sin\alpha}{\alpha}\right)^2 \left(\frac{\sin\beta}{\beta}\right)^2
$$

where $\alpha = \frac{ka}{2}\sin\theta_x$, $\beta = \frac{kb}{2}\sin\theta_y$.

### 5.2 圆孔 (Circular Aperture) / 5.2 圆孔 (Circular Aperture)

Diameter $D$:

$$
I(\theta) = I_0 \left\frac{2J_1(kD\sin\theta/2)}{kD\sin\theta/2}\right^2
$$

**Airy pattern**: first null at $\sin\theta = 1.22\lambda/D$ (Rayleigh criterion for resolution).

### 5.3 正弦光栅 (Sinusoidal Grating) / 5.3 正弦光栅 (Sinusoidal Grating)

Transmission: $t(x) = t_0 + t_1 \cos(2\pi x/d)$

Produces diffraction orders at $\sin\theta_m = m\lambda/d$.

---

## 6. 玻恩近似 (Born Approximation) / 玻恩近似 (Born Approximation)

Weak scattering: the field inside the scatterer ≈ incident field. Valid when refractive index contrast is small.

**First Born approximation**:

$$
\mathbf{f}(\mathbf{n}, \mathbf{n}_0) = \frac{k^2}{4\pi} (\mathbf{I} - \mathbf{n}\mathbf{n}^T) \cdot \int_V \delta\epsilon(\mathbf{x}') e^{-ik(\mathbf{n} - \mathbf{n}_0) \cdot \mathbf{x}'} d^3x'
$$

The scattering amplitude is the **3D Fourier transform** of the permittivity perturbation $\delta\epsilon$.

**Application**: X-ray crystallography, medical imaging (CT).

---

## 7. 基尔霍夫衍射理论 (Kirchhoff Diffraction Theory) / 基尔霍夫衍射理论 (Kirchhoff Diffraction Theory)

Rigorous scalar diffraction theory using Green's theorem:

$$
U(P) = \frac{1}{4\pi} \iint_S \leftU \frac{\partial G}{\partial n} — G \frac{\partial U}{\partial n}\right dS
$$

### Fresnel-Kirchhoff Formula / Fresnel—Kirchhoff Formula

For a planar screen with aperture:

$$
U(P) = -\frac{i}{2\lambda} \iint_{\text{aperture}} U_0 \frac{e^{ik(r + r')}}{r r'} (\cos\theta_0 + \cos\theta) dS
$$

- **Fresnel diffraction** (near-field): quadratic phase factor $\propto e^{ik(x^2+y^2)/(2z)}$
- **Fraunhofer diffraction** (far-field): linear phase factor $\propto e^{-ik(ux+vy)}$

### Rayleigh-Sommerfeld Diffraction / Rayleigh—Sommerfeld 衍射

More rigorous: uses a different Green's function to avoid the inconsistent boundary conditions of Kirchhoff theory.

$$
U(P) = -\frac{1}{2\pi} \iint_{\text{aperture}} U_0 \frac{\partial}{\partial n} \left(\frac{e^{ikr}}{r}\right) dS
$$

---

## 8. 重要公式速查 (Key Formulas Cheat Sheet) / 重要公式速查 (Key Formulas Cheat Sheet)

| Concept | Formula |
|---------|---------|
| Rayleigh $\sigma$ | $\sigma = \frac{8\pi}{3} k^4 \|\alpha\|^2$ (small particle) |
| Rayleigh $\theta$-dep. | $d\sigma/d\Omega \propto 1 + \cos^2\theta$ |
| Mie extinction | $\sigma_{\text{ext}} = \frac{2\pi}{k^2} \sum (2l+1) \operatorname{Re}(a_l+b_l)$ |
| Fraunhofer rectangle | $I \propto \operatorname{sinc}^2(\alpha) \operatorname{sinc}^2(\beta)$ |
| Fraunhofer circle | $I \propto 2J_1(z)/z^2$, $z = kD\sin\theta/2$ |
| Rayleigh criterion | $\Delta\theta = 1.22\lambda/D$ |
| Born approx. | $\mathbf{f} \propto \mathcal{F}\{\delta\epsilon(\mathbf{x})\}$ |
| Optical theorem | $\sigma_{\text{tot}} = \frac{4\pi}{k} \operatorname{Im}f(0)$ |
| Diffraction order | $d\sin\theta_m = m\lambda$ |

---

## 9. 物理直觉 (Physical Intuition) / 物理直觉 (Physical Intuition)

1. **Blue sky**: Rayleigh scattering $(\propto \lambda^{-4})$ scatters blue light 16× more than red
2. **White clouds**: water droplets are $> \lambda$ → Mie regime → all wavelengths scatter similarly
3. **Red sunset**: light travels through more atmosphere → blue scattered away, red remains
4. **Rainbow**: Mie scattering + dispersion in water droplets
5. **Resolution limit**: dictated by $\lambda/D$ (Heisenberg uncertainty principle for waves)
6. **Extinction paradox**: a large object removes 2× its geometric area from the incident beam

---

## 10. 应用 (Applications) / 应用 (Applications)

- **Atmospheric optics**: sky color, cloud physics, haze
- **Remote sensing**: LIDAR, RADAR cross sections
- **Biomedical optics**: light scattering in tissue, flow cytometry
- **Nanophotonics**: plasmonic nanoparticles, Mie resonances in dielectrics
- **Astronomy**: interstellar dust, atmospheric seeing
- **X-ray diffraction**: crystal structure determination
- **Antenna RCS**: radar cross section of aircraft

---

## References / 参考文献

- Jackson §10.1–§10.12
- Bohren & Huffman, *Absorption and Scattering of Light by Small Particles*
- Born & Wolf, *Principles of Optics* (comprehensive diffraction theory)
- Goodman, *Introduction to Fourier Optics*
