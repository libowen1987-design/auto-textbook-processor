# Pozar Chapter 3 — Transmission Lines and Waveguides

> Comprehensive notes on Pozar *Microwave Engineering*, 4th Edition, pp. 116–185.
> These notes derive all waveguiding structures from Maxwell's equations, with emphasis on cutoff conditions, field patterns, attenuation, and engineering design formulas.

---

## 3.1 General Solutions for TEM, TE, and TM Waves

### 3.1.1 Starting from Maxwell's Equations

For time-harmonic fields ($e^{j\omega t}$) in a source-free, homogeneous, isotropic region:

$$
\nabla \times \mathbf{E} = -j\omega\mu \mathbf{H}
$$
$$
\nabla \times \mathbf{H} = j\omega\epsilon \mathbf{E}
$$
$$
\nabla \cdot \mathbf{E} = 0 \quad \nabla \cdot \mathbf{H} = 0
$$

### 3.1.2 Wave Equation

Take curl of Faraday's law:

$$
\nabla \times (\nabla \times \mathbf{E}) = \nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E} = -j\omega\mu \nabla\times\mathbf{H}
$$

Substituting $\nabla\times\mathbf{H} = j\omega\epsilon\mathbf{E}$ and $\nabla\cdot\mathbf{E} = 0$:

$$
\nabla^2 \mathbf{E} + \omega^2\mu\epsilon \mathbf{E} = 0
$$

Define wavenumber $k = \omega\sqrt{\mu\epsilon} = \frac{2\pi}{\lambda}$:

$$
\boxed{\nabla^2 \mathbf{E} + k^2 \mathbf{E} = 0}
$$

Same for $\mathbf{H}$.

### 3.1.3 Longitudinal-Transverse Decomposition

Assume propagation in $+z$ direction: $\mathbf{E}(x,y,z) = [\mathbf{e}(x,y) + \hat{z} e_z(x,y)] e^{-j\beta z}$

The Laplacian separates:

$$
\nabla^2 = \nabla_t^2 + \frac{\partial^2}{\partial z^2} = \nabla_t^2 - \beta^2
$$

Wave equation for transverse and longitudinal components:

$$
\nabla_t^2 \mathbf{e} + (k^2 - \beta^2)\mathbf{e} = 0
$$
$$
\nabla_t^2 e_z + (k^2 - \beta^2) e_z = 0
$$

Define **cutoff wavenumber**: $k_c^2 = k^2 - \beta^2$. Then:

$$
\boxed{\nabla_t^2 e_z + k_c^2 e_z = 0}
$$

### 3.1.4 Transverse Fields from Longitudinal Components

From Maxwell's curl equations, the transverse fields can be expressed entirely in terms of $E_z$ and $H_z$:

For **TE** ($E_z = 0$):

$$
\mathbf{E}_t = -\frac{j\omega\mu}{k_c^2} \hat{z} \times \nabla_t H_z
$$
$$
\mathbf{H}_t = -\frac{j\beta}{k_c^2} \nabla_t H_z
$$

For **TM** ($H_z = 0$):

$$
\mathbf{E}_t = -\frac{j\beta}{k_c^2} \nabla_t E_z
$$
$$
\mathbf{H}_t = -\frac{j\omega\epsilon}{k_c^2} \hat{z} \times \nabla_t E_z
$$

For **TEM** ($E_z = H_z = 0$):

- $k_c^2 = 0$ is required to avoid singular fields
- $\beta = k = \omega\sqrt{\mu\epsilon}$
- Fields are purely transverse and satisfy the 2D electrostatic problem:
  $$
  \nabla_t^2 \phi(x,y) = 0
  $$
  where $\mathbf{E}_t = -\nabla_t \phi$

### 3.1.5 Propagation Constant and Wave Impedance

| Mode | Propagation | Wave Impedance |
|------|-------------|----------------|
| TEM | $\beta = k$ | $Z_{\text{TEM}} = \sqrt{\mu/\epsilon} = \eta$ |
| TE ($f > f_c$) | $\beta = \sqrt{k^2 - k_c^2}$ | $Z_{\text{TE}} = \frac{k\eta}{\beta} = \frac{\eta}{\sqrt{1-(f_c/f)^2}}$ |
| TM ($f > f_c$) | $\beta = \sqrt{k^2 - k_c^2}$ | $Z_{\text{TM}} = \frac{\beta\eta}{k} = \eta\sqrt{1-(f_c/f)^2}$ |
| Below cutoff | $\beta = -j\alpha$ ($\alpha = \sqrt{k_c^2 - k^2}$) | Reactive (evanescent) |

Cutoff frequency: $f_c = \frac{k_c}{2\pi\sqrt{\mu\epsilon}}$

---

## 3.2 Parallel Plate Waveguide

### 3.2.1 Geometry

Two infinite conducting plates at $x = 0$ and $x = a$, filled with dielectric $\epsilon,\mu$. Fields are uniform in $y$ ($\partial/\partial y = 0$).

### 3.2.2 TEM Mode

- $E_z = H_z = 0$
- Solve $\nabla_t^2 \phi = 0$ with $\phi(0)=0$, $\phi(a)=V_0$
- $\phi(x) = V_0 x / a$
- Fields:
  $$
  \mathbf{E} = \hat{x} E_0 e^{-jkz}, \quad \mathbf{H} = \hat{y} \frac{E_0}{\eta} e^{-jkz}
  $$
- No cutoff ($f_c = 0$)
- Characteristic impedance: $Z_0 = \frac{V}{I} = \eta \frac{b}{a}$ (where $b$ = plate width in $y$)

### 3.2.3 TM$_n$ Modes ($H_z = 0$)

Solve $\frac{d^2 e_z}{dx^2} + k_c^2 e_z = 0$ with BC $e_z = 0$ at $x=0,a$:

$$
e_z(x) = A_n \sin\left(\frac{n\pi x}{a}\right)
$$

Cutoff: $k_c = \frac{n\pi}{a}$, $f_{c,n} = \frac{n}{2a\sqrt{\mu\epsilon}}$

Fields:

$$
E_x = -\frac{j\beta_n}{k_c} A_n \cos(k_c x) e^{-j\beta z}
$$
$$
E_z = A_n \sin(k_c x) e^{-j\beta z}
$$
$$
H_y = -\frac{j\omega\epsilon}{k_c} A_n \cos(k_c x) e^{-j\beta z}
$$

### 3.2.4 TE$_n$ Modes ($E_z = 0$)

Solve for $h_z$ with $\partial h_z/\partial x = 0$ at $x=0,a$:

$$
h_z(x) = B_n \cos\left(\frac{n\pi x}{a}\right)
$$

Cutoff: $k_c = \frac{n\pi}{a}$, same as TM.

Fields:

$$
H_x = \frac{j\beta_n}{k_c} B_n \sin(k_c x) e^{-j\beta z}
$$
$$
H_z = B_n \cos(k_c x) e^{-j\beta z}
$$
$$
E_y = -\frac{j\omega\mu}{k_c} B_n \sin(k_c x) e^{-j\beta z}
$$

### 3.2.5 Attenuation

**Conductor attenuation** (for TEM mode):

$$
\alpha_c = \frac{R_s}{b \eta a}
$$

where $R_s = \sqrt{\frac{\omega\mu_0}{2\sigma}}$ is the surface resistivity.

**Dielectric attenuation**:

$$
\alpha_d = \frac{k \tan\delta}{2}
$$

### 3.2.6 Example: Parallel Plate Design

**Example 3.1**: Find cutoff frequencies for TM₁, TE₁ modes of a parallel plate waveguide with $a = 1$ cm, $\epsilon_r = 2.25$

$$
f_{c,1} = \frac{1}{2a\sqrt{\mu\epsilon}} = \frac{3\times10^8}{2(0.01)\sqrt{2.25}} = \frac{3\times10^8}{0.03} = 10\text{ GHz}
$$

---

## 3.3 Rectangular Waveguide

### 3.3.1 Geometry

Rectangular cross-section: $0 \le x \le a$, $0 \le y \le b$, with $a > b$ (convention).

### 3.3.2 TE$_{mn}$ Modes ($E_z = 0$)

Solve Helmholtz equation for $H_z$:

$$
\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + k_c^2\right) h_z = 0
$$

Boundary condition: $\partial h_z/\partial n = 0$ on walls.

Separation of variables: $h_z(x,y) = X(x)Y(y)$

$$
X''/X + Y''/Y + k_c^2 = 0
$$

Let $X''/X = -k_x^2$, $Y''/Y = -k_y^2$, so $k_c^2 = k_x^2 + k_y^2$.

Solution: $h_z(x,y) = A_{mn} \cos(k_x x) \cos(k_y y)$

With BC: $k_x = \frac{m\pi}{a}$, $k_y = \frac{n\pi}{b}$, where $m,n = 0,1,2,\dots$ (not both zero).

**Cutoff wavenumber**:

$$
\boxed{k_{c,mn} = \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}}
$$

**Cutoff frequency**:

$$
\boxed{f_{c,mn} = \frac{k_{c,mn}}{2\pi\sqrt{\mu\epsilon}} = \frac{1}{2\pi\sqrt{\mu\epsilon}} \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}}
$$

**Field components** ($H_0 = A_{mn}$):

$$
H_z = H_0 \cos\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{-j\beta z}
$$

$$
E_x = \frac{j\omega\mu n\pi}{k_c^2 b} H_0 \cos\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right) e^{-j\beta z}
$$

$$
E_y = -\frac{j\omega\mu m\pi}{k_c^2 a} H_0 \sin\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{-j\beta z}
$$

$$
H_x = \frac{j\beta m\pi}{k_c^2 a} H_0 \sin\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{-j\beta z}
$$

$$
H_y = \frac{j\beta n\pi}{k_c^2 b} H_0 \cos\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right) e^{-j\beta z}
$$

**Propagation constant** ($f > f_c$):

$$
\beta = \sqrt{k^2 - k_c^2} = k\sqrt{1 - (f_c/f)^2}
$$

**Wave impedance**:

$$
Z_{\text{TE}} = \frac{E_x}{H_y} = -\frac{E_y}{H_x} = \frac{k\eta}{\beta} = \frac{\eta}{\sqrt{1 - (f_c/f)^2}}
$$

### 3.3.3 Dominant TE$_{10}$ Mode

The **lowest cutoff** TE mode occurs for $m=1, n=0$ (assuming $a > b$):

$$
f_{c,10} = \frac{1}{2a\sqrt{\mu\epsilon}}
$$

Field expressions for TE$_{10}$:

$$
E_y = -\frac{j\omega\mu a}{\pi} H_0 \sin\left(\frac{\pi x}{a}\right) e^{-j\beta z}
$$
$$
H_x = \frac{j\beta a}{\pi} H_0 \sin\left(\frac{\pi x}{a}\right) e^{-j\beta z}
$$
$$
H_z = H_0 \cos\left(\frac{\pi x}{a}\right) e^{-j\beta z}
$$

**Key properties of TE$_{10}$**:
- Single-lobed field variation in $x$, uniform in $y$
- Maximum $E_y$ at center $x = a/2$
- Maximum $H_x$ at center, maximum $H_z$ at side walls

### 3.3.4 TM$_{mn}$ Modes ($H_z = 0$)

Solve Helmholtz for $E_z$ with $E_z = 0$ on walls:

$$
e_z(x,y) = B_{mn} \sin\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right)
$$

$m = 1,2,3,\dots$, $n = 1,2,3,\dots$ (neither can be zero).

Cutoff: same as TE$_{mn}$: $k_{c,mn} = \sqrt{(m\pi/a)^2 + (n\pi/b)^2}$

TM wave impedance: $Z_{\text{TM}} = \frac{\eta\beta}{k} = \eta\sqrt{1 - (f_c/f)^2}$

### 3.3.5 Mode Chart and Degeneracy

- TE$_{mn}$ and TM$_{mn}$ have same cutoff if $m,n \ge 1$ (degenerate)
- TE$_{m0}$ and TE$_{0n}$ have no TM counterpart
- Mode ordering determines the single-mode bandwidth

**Example**: Standard WR-90 ($a=2.286$ cm, $b=1.016$ cm):

| Mode | $f_c$ (GHz) |
|------|-------------|
| TE$_{10}$ | 6.56 |
| TE$_{20}$ | 13.12 |
| TE$_{01}$ | 14.76 |
| TE$_{11}$, TM$_{11}$ | 16.15 |

Bandwidth: $6.56\ \text{GHz} < f < 13.12\ \text{GHz}$

### 3.3.6 Attenuation in Rectangular Waveguide

**Conductor attenuation for TE$_{10}$**:

$$
\alpha_c = \frac{R_s}{a^3 b \beta k \eta} \left(2b\pi^2 + a^3 k^2\right)
$$

More generally for TE$_{mn}$ modes:

$$
\alpha_c = \frac{2R_s}{b\eta\sqrt{1-(f_c/f)^2}} \left[ \left(1+\frac{b}{a}\right)\left(\frac{f_c}{f}\right)^2 + \left(1-\frac{b}{a}\right)\left(\frac{b}{a}\frac{(f_c/f)^2}{(f_c/f)^2_m + (f_c/f)^2_n}\right)^{1/2} \right]
$$

**Dielectric attenuation** (same for all modes):

$$
\alpha_d = \frac{k^2 \tan\delta}{2\beta}
$$

For low-loss dielectrics, $\alpha_d \approx \frac{k \tan\delta}{2\sqrt{1-(f_c/f)^2}}$

### 3.3.7 Power Capacity

Maximum power (TE$_{10}$ mode, limited by $E_{\text{max}}$ at center):

$$
P_{\text{max}} = \frac{ab}{4Z_{\text{TE}}} |E_{\text{max}}|^2
$$

More precisely, for TE$_{10}$:

$$
P = \frac{ab}{4} \frac{\beta k \eta}{k_c^2} |H_0|^2 = \frac{ab}{4Z_{\text{TE}}} |E_0|^2
$$

where $E_0$ is the peak $E_y$ at $x=a/2$.

**Practical power limit for air-filled waveguide**: $E_{\text{max}} \approx 3 \times 10^6$ V/m (breakdown field of air).

### 3.3.8 Example: Rectangular Waveguide Design

**Example 3.2**: WR-90 waveguide dimensions, determine operating band.

Given $a = 2.286$ cm, $b = 1.016$ cm.

$f_{c,10} = \frac{c}{2a} = \frac{3\times10^8}{2(0.02286)} = 6.56$ GHz

$f_{c,20} = \frac{c}{a} = 13.12$ GHz

Recommended operating band: $1.25 f_c$ to $1.9 f_c$:
$8.2\ \text{GHz} < f < 12.4\ \text{GHz}$ (X-band)

**Example 3.3**: Find $a,b$ for $f_c = 10$ GHz with $a=2b$.

$$
f_c = \frac{c}{2a} \Rightarrow a = \frac{c}{2f_c} = \frac{3\times10^8}{2\times10^{10}} = 1.5\ \text{cm}
$$
$$
b = a/2 = 0.75\ \text{cm}
$$

---

## 3.4 Circular Waveguide

### 3.4.1 Geometry

Cylindrical waveguide of radius $a$, filled with $\epsilon,\mu$.

### 3.4.2 Wave Equation in Cylindrical Coordinates

For TE modes ($E_z=0$):

$$
\frac{1}{\rho}\frac{\partial}{\partial\rho}\left(\rho\frac{\partial h_z}{\partial\rho}\right) + \frac{1}{\rho^2}\frac{\partial^2 h_z}{\partial\phi^2} + k_c^2 h_z = 0
$$

Separation of variables: $h_z(\rho,\phi) = R(\rho)\Phi(\phi)$

The $\phi$ equation: $\Phi'' + n^2\Phi = 0 \Rightarrow \Phi(\phi) = \cos(n\phi)$ or $\sin(n\phi)$, $n=0,1,2,\dots$

The $\rho$ equation is Bessel's equation:

$$
\rho^2 R'' + \rho R' + (k_c^2\rho^2 - n^2) R = 0
$$

Solution: $R(\rho) = J_n(k_c\rho)$ (finite at $\rho=0$; Neumann $Y_n$ rejected).

### 3.4.3 TE$_{nm}$ Modes in Circular Waveguide

$h_z(\rho,\phi) = H_0 J_n(k_c\rho) \cos(n\phi) e^{-j\beta z}$

BC: $\partial h_z/\partial\rho = 0$ at $\rho=a \Rightarrow J_n'(k_c a) = 0$

Let $p'_{nm}$ be the $m$-th root of $J_n'(x) = 0$. Then:

$$
k_{c,nm} = \frac{p'_{nm}}{a}
$$

**Field components**:

$$
H_z = H_0 J_n(k_c\rho) \cos(n\phi) e^{-j\beta z}
$$

$$
E_\rho = -\frac{j\omega\mu n}{k_c^2 \rho} H_0 J_n(k_c\rho) \sin(n\phi) e^{-j\beta z}
$$

$$
E_\phi = -\frac{j\omega\mu}{k_c} H_0 J_n'(k_c\rho) \cos(n\phi) e^{-j\beta z}
$$

$$
H_\rho = -\frac{j\beta}{k_c} H_0 J_n'(k_c\rho) \cos(n\phi) e^{-j\beta z}
$$

$$
H_\phi = \frac{j\beta n}{k_c^2 \rho} H_0 J_n(k_c\rho) \sin(n\phi) e^{-j\beta z}
$$

**Dominant TE mode**: TE$_{11}$ ($p'_{11} = 1.841$)

### 3.4.4 TM$_{nm}$ Modes in Circular Waveguide

$e_z(\rho,\phi) = E_0 J_n(k_c\rho) \cos(n\phi) e^{-j\beta z}$

BC: $E_z = 0$ at $\rho=a \Rightarrow J_n(k_c a) = 0$

Let $p_{nm}$ be the $m$-th root of $J_n(x) = 0$. Then:

$$
k_{c,nm} = \frac{p_{nm}}{a}
$$

**Dominant TM mode**: TM$_{01}$ ($p_{01} = 2.405$)

### 3.4.5 Bessel Function Zeros and Mode Ordering

| $n$ | $m$ | $p'_{nm}$ (TE) | $p_{nm}$ (TM) |
|-----|-----|----------------|---------------|
| 0 | 1 | 3.832 | 2.405 |
| 1 | 1 | **1.841** (TE$_{11}$) | 3.832 |
| 2 | 1 | 3.054 | 5.136 |
| 0 | 2 | 7.016 | 5.520 |
| 1 | 2 | 5.331 | 7.016 |
| 2 | 2 | 6.706 | 8.417 |

**Mode ordering by cutoff frequency** (for $a$ = constant):

1. TE$_{11}$: $k_c a = 1.841$ (dominant mode)
2. TM$_{01}$: $k_c a = 2.405$
3. TE$_{21}$: $k_c a = 3.054$
4. TE$_{01}$, TM$_{11}$: $k_c a = 3.832$ (degenerate)
5. TE$_{31}$: $k_c a = 4.201$

### 3.4.6 Attenuation in Circular Waveguide

**TE$_{nm}$**:

$$
\alpha_c = \frac{R_s}{a\eta\sqrt{1-(f_c/f)^2}} \left[ \left(\frac{f_c}{f}\right)^2 + \frac{n^2}{(p'_{nm})^2 - n^2} \right]
$$

For TE$_{01}$ mode ($n=0$):

$$
\alpha_c = \frac{R_s}{a\eta\sqrt{1-(f_c/f)^2}} \left(\frac{f_c}{f}\right)^2
$$

Notable: TE$_{01}$ attenuation **decreases** as frequency increases — unique property.

**TM$_{nm}$**:

$$
\alpha_c = \frac{R_s}{a\eta\sqrt{1-(f_c/f)^2}}
$$

### 3.4.7 Example: Circular Waveguide Design

**Example**: Design circular waveguide for TE$_{11}$ at 10 GHz with $a = 1$ cm.

$$
f_{c,11} = \frac{p'_{11} c}{2\pi a} = \frac{1.841 \times 3\times 10^8}{2\pi \times 0.01} = 8.79\ \text{GHz}
$$

At $f = 10$ GHz:

$$
\beta = \frac{2\pi}{c}\sqrt{f^2 - f_c^2} = \frac{2\pi}{3\times10^8}\sqrt{10^{20} - (8.79\times10^9)^2} = 159.0\ \text{rad/m}
$$

---

## 3.5 Coaxial Line

### 3.5.1 Geometry and TEM Mode

Inner conductor radius $a$, outer radius $b$, dielectric $\epsilon,\mu$.

**TEM mode**: $E_z = H_z = 0$, fields are transverse.

From Laplace: $\nabla_t^2 \phi = 0$ in cylindrical coordinates:

$$
\frac{1}{\rho}\frac{d}{d\rho}\left(\rho\frac{d\phi}{d\rho}\right) = 0 \Rightarrow \phi(\rho) = A\ln\rho + B
$$

With $\phi(a) = V_0$, $\phi(b) = 0$:

$$
\phi(\rho) = V_0 \frac{\ln(b/\rho)}{\ln(b/a)}
$$

Fields:

$$
\mathbf{E} = \hat{\rho} \frac{V_0}{\rho \ln(b/a)} e^{-jkz}
$$
$$
\mathbf{H} = \hat{\phi} \frac{V_0}{\eta \rho \ln(b/a)} e^{-jkz}
$$

### 3.5.2 Characteristic Impedance

$$
Z_0 = \frac{V}{I} = \frac{V_0}{2\pi V_0/(\eta \ln(b/a))} = \frac{\eta}{2\pi} \ln\left(\frac{b}{a}\right)
$$

For an air-filled coax ($\epsilon_r = 1$): $\eta = 377\ \Omega$, so:

$$
Z_0 = 60 \ln\left(\frac{b}{a}\right) \quad (\text{air-filled, ohms})
$$

For dielectric-filled:

$$
Z_0 = \frac{60}{\sqrt{\epsilon_r}} \ln\left(\frac{b}{a}\right) \quad (\text{ohms})
$$

### 3.5.3 Attenuation

**Conductor attenuation**:

$$
\alpha_c = \frac{R_s}{2\eta \ln(b/a)} \left(\frac{1}{a} + \frac{1}{b}\right) \quad (\text{Np/m})
$$

**Dielectric attenuation**:

$$
\alpha_d = \frac{k \tan\delta}{2} \quad (\text{Np/m})
$$

### 3.5.4 Power Capacity (TEM mode)

$$
P_{\text{max}} = \frac{V_0^2}{2Z_0}
$$

Voltage limited by breakdown: $V_{\text{max}} = E_{\text{max}} a \ln(b/a)$ (maximum $E$ occurs at $\rho = a$)

$$
P_{\text{max}} = \frac{\pi a^2 E_{\text{max}}^2}{\eta} \ln\left(\frac{b}{a}\right)
$$

Optimal $b/a$ ratio for power capacity: $b/a = \sqrt{e} \approx 1.65$ (from $\partial P_{\text{max}}/\partial a = 0$).

### 3.5.5 Higher-Order Modes (Cutoff)

To maintain TEM-only operation, the wavelength must be sufficiently large relative to the cross-section.

**TE$_{11}$ mode** (first higher-order mode):

$$
\lambda_c \approx \pi(a + b) \quad \Rightarrow \quad f_c \approx \frac{c}{\pi(a+b)\sqrt{\epsilon_r}}
$$

Design rule: $(a + b) < \frac{\lambda_{\text{min}}}{\pi\sqrt{\epsilon_r}}$

### 3.5.6 Characteristic Impedance — Optimal Values

| $b/a$ | $Z_0$ (air, $\Omega$) | Property |
|-------|----------------------|----------|
| 1.65 | 30 | Maximum power capacity |
| 3.59 | 77 | Minimum attenuation (for air) |
| 2.30 | 50 | Compromise (standard) |

**50 $\Omega$ coax** ($b/a \approx 2.30$) is the most widely used impedance standard, balancing power handling and attenuation.

---

## 3.6 Stripline and Microstrip

### 3.6.1 Stripline Geometry

A flat conductor of width $W$ centered between two ground planes separated by $b$, filled with dielectric $\epsilon_r$.

**TEM mode** (strictly, a TEM mode exists in stripline).

### 3.6.2 Characteristic Impedance of Stripline

For zero-thickness strip, $W/b < 0.5$:

$$
Z_0 = \frac{30\pi}{\sqrt{\epsilon_r}} \frac{1}{W_e/b + 0.441}
$$

where $W_e$ is the effective width correcting for fringing:

$$
W_e = \frac{W}{b} - \left\{
\begin{array}{ll}
0, & W/b > 0.35 \\
(0.35 - W/b)^2, & W/b < 0.35
\end{array}
\right.
$$

For $W/b > 0.5$:

$$
Z_0 = \frac{94.15}{\sqrt{\epsilon_r}} \frac{1}{W/b + 0.883 + \frac{1+1/\epsilon_r'}{\pi}\left[ \ln\left(\frac{W}{b} + 1.88\right) + 0.106 \right]}
$$

More practical formula (Cohn):

$$
Z_0\sqrt{\epsilon_r} = \frac{30}{\sqrt{\epsilon_r}} \ln\left\{1 + \frac{4}{\pi} \frac{1}{W/b} \left[ \frac{8}{\pi} \frac{1}{W/b} + \sqrt{\left(\frac{8}{\pi} \frac{1}{W/b}\right)^2 + 6.27} \right] \right\}
$$

### 3.6.3 Microstrip Geometry

Conductor of width $W$ on a dielectric substrate of thickness $h$ and $\epsilon_r$, with ground plane below.

### 3.6.4 Quasi-TEM Approximation

Microstrip supports a **quasi-TEM** mode because the fields are partly in the dielectric and partly in air. This leads to a frequency-dependent **effective dielectric constant**:

$$
\epsilon_{\text{eff}} = \frac{\epsilon_r + 1}{2} + \frac{\epsilon_r - 1}{2} \frac{1}{\sqrt{1 + 12h/W}}
$$

This accounts for the fact that some field lines travel through air ($\epsilon_r=1$) and some through the substrate.

### 3.6.5 Characteristic Impedance of Microstrip

**Wide strip** ($W/h > 1$):

$$
Z_0 = \frac{\eta}{\sqrt{\epsilon_{\text{eff}}}} \frac{1}{W/h + 1.393 + 0.667 \ln(W/h + 1.444)}
$$

**Narrow strip** ($W/h < 1$):

$$
Z_0 = \frac{60}{\sqrt{\epsilon_{\text{eff}}}} \ln\left(\frac{8h}{W} + \frac{W}{4h}\right)
$$

### 3.6.6 Synthesis Formulas (Given $Z_0$, find $W/h$)

For a given $Z_0$ and $\epsilon_r$:

$$
A = \frac{Z_0}{60}\sqrt{\frac{\epsilon_r + 1}{2}} + \frac{\epsilon_r - 1}{\epsilon_r + 1}\left(0.23 + \frac{0.11}{\epsilon_r}\right)
$$

If $A > 1.52$ ($W/h < 2$):

$$
\frac{W}{h} = \frac{8e^A}{e^{2A} - 2}
$$

If $A \le 1.52$ ($W/h \ge 2$):

$$
\frac{W}{h} = \frac{2}{\pi} \left[ B - 1 - \ln(2B - 1) + \frac{\epsilon_r - 1}{2\epsilon_r} \left\{ \ln(B - 1) + 0.39 - \frac{0.61}{\epsilon_r} \right\} \right]
$$

where $B = \frac{\eta\pi}{2Z_0\sqrt{\epsilon_r}} \approx \frac{377\pi}{2Z_0\sqrt{\epsilon_r}}$.

### 3.6.7 Dispersion in Microstrip

Effective dielectric constant is frequency-dependent:

$$
\epsilon_{\text{eff}}(f) = \epsilon_r - \frac{\epsilon_r - \epsilon_{\text{eff}}(0)}{1 + G(f/f_p)^2}
$$

where:
$$
G = 0.6 + 0.009 Z_0
$$
$$
f_p = \frac{Z_0}{8\pi h} \quad (\text{Hertz}, h \text{ in meters})
$$

or more accurately (Kirschning and Jansen model).

### 3.6.8 Example: Microstrip Design

**Design a 50 $\Omega$ line on FR4 ($\epsilon_r = 4.5$, $h = 1.6$ mm)**:

$$
A = \frac{50}{60}\sqrt{\frac{4.5 + 1}{2}} + \frac{4.5 - 1}{4.5 + 1}\left(0.23 + \frac{0.11}{4.5}\right) = 0.833 \times 1.658 + 0.636 \times 0.252 = 1.542
$$

Since $A > 1.52$, $W/h < 2$:

$$
\frac{W}{h} = \frac{8e^{1.542}}{e^{3.084} - 2} = \frac{37.38}{19.85 - 2} = 2.09 \;\Rightarrow\; W = 3.35\ \text{mm}
$$

---

## 3.7 Surface Waves and Dielectric Waveguides

### 3.7.1 Surface Waves on a Grounded Dielectric Slab

A dielectric layer ($\epsilon_r$) on a conducting ground plane can support TM surface waves.

Fields decay exponentially in the air region above the slab (evanescent in $x$), sinusoidal within the slab.

**Characteristic equation** (TM modes):

$$
\kappa h \tan(\kappa h) = \epsilon_r \alpha h
$$

where $\kappa^2 = \epsilon_r k_0^2 - \beta^2$, $\alpha^2 = \beta^2 - k_0^2$.

**Cutoff**: $\alpha \to 0$, $\beta \to k_0$:

$$
f_c = \frac{nc}{2h\sqrt{\epsilon_r - 1}}, \quad n = 0,1,2,\dots
$$

The TM$_0$ mode has **zero cutoff** — it exists at all frequencies.

### 3.7.2 Dielectric Rod Waveguide

Used in millimeter-wave and optical applications (fiber optics).

Solution involves Bessel functions inside the rod and modified Bessel functions (decaying) outside.

**Hybrid modes** (HE$_{nm}$, EH$_{nm}$) — both $E_z$ and $H_z$ nonzero.

The HE$_{11}$ mode is the dominant (fundamental) mode with no cutoff.

### 3.7.3 Engineering Significance

- Microstrip radiation losses related to surface wave excitation
- Dielectric waveguide used for millimeter-wave integrated circuits
- Optical fibers are the most important practical application (Ch 4 of Pozar)

---

## Summary Table of Waveguide Properties

| Structure | Dominant Mode | Cutoff | Dispersion | Bandwidth | Attenuation |
|-----------|---------------|--------|------------|-----------|-------------|
| Parallel Plate | TEM | None | None (TEM) | Unlimited | Low |
| Rectangular | TE$_{10}$ | $c/2a$ | Medium | ~2:1 | Moderate |
| Circular | TE$_{11}$ | $p'_{11}c/2\pi a$ | Medium | ~1.5:1 | Moderate |
| Coaxial | TEM | None | None (TEM) | $\pi(a+b) < \lambda$ | Low |
| Stripline | TEM | None | None (TEM) | Depends on aspect | Low |
| Microstrip | Quasi-TEM | None (if $W/h \gg 1$) | Weak | Wide | Moderate |

---

## Key Engineering Formulas Cheat Sheet

### Rectangular Guide

- $f_{c,mn} = \frac{c}{2\pi\sqrt{\mu_r\epsilon_r}} \sqrt{(m\pi/a)^2 + (n\pi/b)^2}$
- $\beta = \frac{2\pi f}{c}\sqrt{\epsilon_r\mu_r - (f_c/f)^2}$
- $Z_{\text{TE}} = \frac{377\sqrt{\mu_r/\epsilon_r}}{\sqrt{1-(f_c/f)^2}}$
- $P_{\text{max}} = \frac{ab}{4Z_{\text{TE}}} E_{\text{max}}^2$

### Coax

- $Z_0 = \frac{60}{\sqrt{\epsilon_r}} \ln(b/a)$
- $\alpha_c = \frac{R_s}{2\eta \ln(b/a)}(1/a + 1/b)$
- $\lambda_c \approx \pi(a+b)$ for TE$_{11}$

### Microstrip

- $\epsilon_{\text{eff}} = \frac{\epsilon_r + 1}{2} + \frac{\epsilon_r - 1}{2}\frac{1}{\sqrt{1+12h/W}}$
- $Z_0 (W/h > 1) = \frac{377}{\sqrt{\epsilon_{\text{eff}}}} \frac{1}{W/h + 1.393 + 0.667\ln(W/h + 1.444)}$
