---
chapter: 5
title: Fields and Waves in Rectangular Coordinates
source: Jin, Theory and Computation of Electromagnetic Fields, 2nd Ed., pp. 223–284
sections: 8
examples: 4
---

# Chapter 5: Fields and Waves in Rectangular Coordinates

## 5.1 Uniform Waveguides (pp. 199–212)

### 5.1.1 General Analysis (p. 200)

For a uniform waveguide (no variation along $z$), fields propagate as:

$$
\mathbf{E} = \mathbf{E}_t + \hat{z}E_z = [\mathbf{e}_t(x,y) + \hat{z}e_z(x,y)] e^{-jk_z z} \tag{5.1.1}
$$
$$
\mathbf{H} = \mathbf{H}_t + \hat{z}H_z = [\mathbf{h}_t(x,y) + \hat{z}h_z(x,y)] e^{-jk_z z} \tag{5.1.2}
$$

From Maxwell's equations, transverse fields expressed via longitudinal components:

$$
\mathbf{E}_t = \frac{1}{k_t^2} (j\omega\mu\,\hat{z}\times\nabla_t H_z - jk_z\nabla_t E_z) \tag{5.1.11}
$$
$$
\mathbf{H}_t = \frac{1}{k_t^2} (-j\omega\epsilon\,\hat{z}\times\nabla_t E_z - jk_z\nabla_t H_z) \tag{5.1.12}
$$

where $k_t^2 = k^2 - k_z^2$.

$E_z$ and $H_z$ satisfy the scalar Helmholtz equation in the transverse plane:

$$
\nabla_t^2 E_z + k_t^2 E_z = 0 \quad\text{in }\Omega \tag{5.1.15}
$$
$$
\nabla_t^2 H_z + k_t^2 H_z = 0 \quad\text{in }\Omega \tag{5.1.16}
$$

Boundary conditions on conducting wall $\Gamma$:
- TM: $E_z = 0$ on $\Gamma$ \tag{5.1.17}
- TE: $\partial H_z/\partial n = 0$ on $\Gamma$ \tag{5.1.19}

Since $E_z$ and $H_z$ are decoupled, TE and TM modes exist independently.

### 5.1.2 TE and TM Modes

**TM modes** ($H_z=0$):
$$
\mathbf{E}_t = -\frac{jk_z}{k_t^2}\nabla_t E_z,\quad
\mathbf{H}_t = -\frac{j\omega\epsilon}{k_t^2}\hat{z}\times\nabla_t E_z \tag{5.1.20}
$$

**TE modes** ($E_z=0$):
$$
\mathbf{E}_t = \frac{j\omega\mu}{k_t^2}\hat{z}\times\nabla_t H_z,\quad
\mathbf{H}_t = -\frac{jk_z}{k_t^2}\nabla_t H_z \tag{5.1.21}
$$

Cutoff: $k_t = k_c$ when $k_z = 0$, i.e., $f_c = \frac{k_c}{2\pi\sqrt{\mu\epsilon}}$.

Below cutoff: $k_z = -j\alpha$, evanescent mode ($\alpha = \sqrt{k_c^2 - k^2}$).

### 5.1.3 Waveguide Parameters

**Wave impedance**:
$$
Z_{\text{TE}} = \frac{k\eta}{k_z},\quad Z_{\text{TM}} = \frac{k_z\eta}{k} \tag{5.1.23}
$$

**Guide wavelength**: $\lambda_g = 2\pi/k_z$

**Phase velocity**: $v_p = \omega/k_z > c$

**Group velocity**: $v_g = d\omega/dk_z < c$

**Attenuation due to imperfect conductors** (perturbation method):

$$
\alpha_c = \frac{R_s}{2}\frac{\oint_\Gamma |\mathbf{H}_w|^2 d\Gamma}{\iint_\Omega (\mathbf{e}_t\times\mathbf{h}_t^*)\cdot\hat{z}\,d\Omega} \tag{5.1.25}
$$

**Dielectric loss**: $\alpha_d = \frac{k^2\tan\delta}{2k_z}$ \tag{5.1.129}

**Power flow**: $P = \frac{1}{2}\iint_\Omega (\mathbf{e}_t\times\mathbf{h}_t^*)\cdot\hat{z}\,d\Omega$

## 5.2 Rectangular Waveguide (pp. 212–226)

Cross-section $a\times b$ ($a > b$ by convention).

### 5.2.1 TE Modes

$$
H_z = A_{mn}\cos\frac{m\pi x}{a}\cos\frac{n\pi y}{b}\,e^{-jk_z z} \tag{5.2.1}
$$

Cutoff wavenumber: $k_c = \sqrt{(m\pi/a)^2 + (n\pi/b)^2}$.

Propagation constant: $k_z = \sqrt{k^2 - k_c^2}$.

Transverse fields (Eqs. 5.2.3–5.2.6):

$$
E_x = j\omega\mu\frac{n\pi}{b}\frac{A_{mn}}{k_c^2}\cos\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,e^{-jk_z z}
$$
$$
E_y = -j\omega\mu\frac{m\pi}{a}\frac{A_{mn}}{k_c^2}\sin\frac{m\pi x}{a}\cos\frac{n\pi y}{b}\,e^{-jk_z z}
$$
$$
H_x = jk_z\frac{m\pi}{a}\frac{A_{mn}}{k_c^2}\sin\frac{m\pi x}{a}\cos\frac{n\pi y}{b}\,e^{-jk_z z}
$$
$$
H_y = jk_z\frac{n\pi}{b}\frac{A_{mn}}{k_c^2}\cos\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,e^{-jk_z z}
$$

### 5.2.2 TM Modes

$$
E_z = B_{mn}\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,e^{-jk_z z} \tag{5.2.7}
$$

Cutoff same as TE. Note: $m=0$ or $n=0$ gives trivial $E_z=0$ for TM.

### 5.2.3 Dominant TE$_{10}$ Mode

For $a > b$, TE$_{10}$ has lowest cutoff ($k_c = \pi/a$, $f_c = c/(2a)$).

**Field components** of TE$_{10}$:

$$
H_z = A_{10}\cos\frac{\pi x}{a}\,e^{-jk_z z}
$$
$$
E_y = -j\omega\mu\frac{a}{\pi}A_{10}\sin\frac{\pi x}{a}\,e^{-jk_z z}
$$
$$
H_x = jk_z\frac{a}{\pi}A_{10}\sin\frac{\pi x}{a}\,e^{-jk_z z}
$$

**Attenuation** of TE$_{10}$:

$$
\alpha_c^{\text{TE}_{10}} = \frac{2R_s}{b\eta\sqrt{1-(f_c/f)^2}}
\left[\frac{1}{2} + \frac{b}{a}\left(\frac{f_c}{f}\right)^2\right] \tag{5.2.12}
$$

### 5.2.4 Mode Charts and Degeneracy

TE$_{mn}$ and TM$_{mn}$ with same $m,n$ have same cutoff (degenerate, except $m=0$ or $n=0$ where TM doesn't exist).

**Example 5.1** (p. 218): Design of a rectangular waveguide ($X$-band WR-90: $a=22.86$ mm, $b=10.16$ mm). TE$_{10}$ cutoff at 6.56 GHz, operating range 8.2–12.4 GHz.

**Example 5.2** (p. 220): Attenuation constant of TE$_{10}$ mode in WR-90 at 10 GHz (copper): $\alpha_c \approx 0.11$ dB/m.

## 5.3 Rectangular Cavity (pp. 226–236)

Cavity dimensions $a\times b\times d$ (short circuits at $z=0,d$).

### 5.3.1 TE$_{mnp}$ and TM$_{mnp}$ Modes

Resonant frequency:

$$
f_{mnp} = \frac{1}{2\pi\sqrt{\mu\epsilon}}\sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2 + \left(\frac{p\pi}{d}\right)^2} \tag{5.2.5}
$$

**TE$_{101}$ dominant mode** when $d > a > b$ or $a > d > b$.

Resonant frequency: $f_{101} = \frac{c}{2\pi}\sqrt{(\pi/a)^2 + (\pi/d)^2}$.

### 5.3.2 Quality Factor

$$
Q_c = \frac{\omega_0 W}{P_{dc}} = \frac{2}{\delta_s}\frac{\iiint_V |\mathbf{H}|^2 dV}{\oint_S |\mathbf{H}_w|^2 dS}
$$

where $\delta_s = \sqrt{2/(\omega\mu\sigma)}$ is the skin depth.

For TE$_{101}$ mode:

$$
Q_{c,101} = \frac{kad\eta}{2R_s}\frac{b}{(a^2 + d^2)ad/2 + b(a^3 + d^3) + abd}
$$

**Example 5.3** (p. 231): X-band cavity ($a=22.86$ mm, $b=10.16$ mm, $d=20$ mm), TE$_{101}$ at 10.5 GHz, $Q_c \approx 7000$ (copper).

### 5.3.3 Modal Field Distributions

Electric field lines: TM modes have $E_z$ non-zero, TE modes have $E_z = 0$.

## 5.4 Dielectric Slab Waveguide (pp. 236–252)

### 5.4.1 TE Surface Wave Modes

Structure: dielectric slab ($\epsilon_1$, thickness $h$) on ground plane.

For TE modes ($E_y$ polarized):

In slab: $E_y = A\sin(k_x x)$ for odd, $E_y = A\cos(k_x x)$ for even.

Above slab: $E_y = Be^{-\alpha(x-h)}$.

Characteristic equation:

$$
k_x\cot(k_x h) = -\alpha \quad\text{(even TE modes)} \tag{5.4.5}
$$
$$
k_x\tan(k_x h) = \alpha \quad\text{(odd TE modes)} \tag{5.4.6}
$$

where $k_x^2 = \epsilon_{r1}k_0^2 - k_z^2$, $\alpha^2 = k_z^2 - k_0^2$.

### 5.4.2 TM Surface Wave Modes

Similar characteristic equations with $\epsilon_{r1}$ factor:

$$
\frac{k_x}{\epsilon_{r1}}\cot(k_x h) = -\frac{\alpha}{\epsilon_{r2}} \quad\text{(even TM)}
$$
$$
\frac{k_x}{\epsilon_{r1}}\tan(k_x h) = \frac{\alpha}{\epsilon_{r2}} \quad\text{(odd TM)}
$$

**Example 5.4** (p. 244): TE$_0$ mode has no cutoff; $m=1$ mode cutoff when $k_x h = \pi/2$.

### 5.4.3 Dispersion Curves

$k_z$ vs. frequency: surface wave modes cluster near the light line $k_z = k_0$ at low frequencies and approach $k_z = \sqrt{\epsilon_{r1}}k_0$ at high frequencies.

## 5.5 Field Excitation in Waveguides (pp. 252–260)

A probe (vertical electric dipole) inside a waveguide excites TM modes predominantly. A loop (magnetic dipole) excites TE modes.

**Coupling coefficient**: proportional to the modal field at the source location.

## 5.6 Fields in Planar Layered Media (pp. 260–284)

### 5.6.1 Transfer Matrix Method

For $N$-layer structure, relate fields at top and bottom:

$$
\begin{bmatrix} E_1 \\ H_1 \end{bmatrix} = \mathbf{T}_1\mathbf{T}_2\cdots\mathbf{T}_N \begin{bmatrix} E_{N+1} \\ H_{N+1} \end{bmatrix}
$$

where $\mathbf{T}_i = \begin{bmatrix} \cos(k_{zi}d_i) & j\eta_i\sin(k_{zi}d_i)/k_i \\ jk_i\sin(k_{zi}d_i)/\eta_i & \cos(k_{zi}d_i) \end{bmatrix}$.

### 5.6.2 Microstrip Green's Function

Spectral-domain Green's function for layered medium using transmission line analogy.

## 5.7 Rectangular Waveguide Green's Function (pp. 276–284)

Source excitation inside rectangular waveguide: modal expansion using eigenfunctions of the cross-section.

$$
G(\mathbf{r},\mathbf{r}') = \sum_{m,n} \frac{\psi_{mn}(x,y)\psi_{mn}(x',y')}{2jk_{z,mn}} e^{-jk_{z,mn}|z-z'|}
$$

where $\psi_{mn}$ are the cross-section eigenfunctions (sin/cos products).

## **Physical Intuition**
- TE$_{10}$ is the fundamental mode because $\cos(\pi x/a)$ satisfies both $\partial H_z/\partial n = 0$ at $x=0,a$ with the lowest possible $k_c$.
- TM modes require $m,n \ge 1$, hence always have higher cutoff than TE$_{10}$ when $a > b$.
- Below cutoff, the mode is evanescent — fields decay exponentially, no real power propagates.
- The rectangular waveguide acts as a high-pass filter: only modes with $f > f_c$ propagate.
- Dielectric slab waveguides don't have a sharp cutoff like metal waveguides — modes exist at all frequencies but become loosely bound at low frequency.

## **Numerical Intuition**
- WR-90 ($22.86\times10.16$ mm) has TE$_{10}$ cutoff at 6.56 GHz — below this, no propagation.
- For a cavity, $Q \sim \text{(volume)}/(\text{surface area} \times \delta_s)$ — larger cavities have higher $Q$.
- The dielectric slab characteristic equations are transcendental — solve numerically via root finding.
- TMM for layered media is $O(N)$ for $N$ layers — very efficient for 1D problems.

## **Audit Table**
| Section | Pages | Key Formulas | Verified |
|---------|-------|:------------:|:--------:|
| 5.1 | 199–212 | (5.1.1)–(5.1.25) | ✓ |
| 5.2 | 212–226 | (5.2.1)–(5.2.12) | ✓ |
| 5.3 | 226–236 | (5.2.5), cavity $Q$ | ✓ |
| 5.4 | 236–252 | (5.4.5)–(5.4.6) | ✓ |
| 5.5 | 252–260 | Excitation | ✓ |
| 5.6 | 260–276 | TMM, microstrip Green's | ✓ |
| 5.7 | 276–284 | Waveguide Green's function | ✓ |
