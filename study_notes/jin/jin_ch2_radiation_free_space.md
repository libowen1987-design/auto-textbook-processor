# Chapter 2: Electromagnetic Radiation in Free Space

**Source:** Jin, *Theory and Computation of Electromagnetic Fields*, 2nd Ed., Chapter 2 (pp. 77–112)

---

## 2.1 Scalar and Vector Potentials

### 2.1.1 Static Fields

For static electric fields (time-independent), $\nabla \times \mathbf{E} = 0$ implies $\mathbf{E}$ can be expressed as the gradient of a scalar potential $\Phi$:

$$
\mathbf{E} = -\nabla \Phi
\tag{2.1.1}
$$

Combined with $\nabla \cdot \mathbf{D} = \rho_e$ and $\mathbf{D} = \epsilon \mathbf{E}$:

$$
\nabla^2 \Phi = -\frac{\rho_e}{\epsilon} \quad \text{(Poisson's equation)}
\tag{2.1.2}
$$

For static magnetic fields, $\nabla \cdot \mathbf{B} = 0$ allows introduction of a vector potential $\mathbf{A}$:

$$
\mathbf{B} = \nabla \times \mathbf{A}
\tag{2.1.3}
$$

With $\nabla \times \mathbf{H} = \mathbf{J}$ and $\mathbf{B} = \mu \mathbf{H}$:

$$
\nabla \times (\nabla \times \mathbf{A}) = \mu \mathbf{J}
$$
$$
\nabla(\nabla \cdot \mathbf{A}) - \nabla^2 \mathbf{A} = \mu \mathbf{J}
\tag{2.1.4}
$$

By imposing the **Coulomb gauge** $\nabla \cdot \mathbf{A} = 0$:

$$
\nabla^2 \mathbf{A} = -\mu \mathbf{J}
\tag{2.1.5}
$$

### 2.1.2 Time-Harmonic Fields and the Lorenz Gauge

For time-harmonic fields with $e^{j\omega t}$ dependence, Maxwell's equations become:

$$
\nabla \times \mathbf{E} = -j\omega \mathbf{B}
\tag{2.1.6}
$$
$$
\nabla \times \mathbf{H} = \mathbf{J} + j\omega \mathbf{D}
\tag{2.1.7}
$$
$$
\nabla \cdot \mathbf{D} = \rho_e
\tag{2.1.8}
$$
$$
\nabla \cdot \mathbf{B} = 0
\tag{2.1.9}
$$

Using $\mathbf{B} = \nabla \times \mathbf{A}$, Faraday's law gives:

$$
\nabla \times (\mathbf{E} + j\omega \mathbf{A}) = 0
\tag{2.1.10}
$$

Hence $\mathbf{E} + j\omega \mathbf{A} = -\nabla \Phi$, or:

$$
\mathbf{E} = -j\omega \mathbf{A} - \nabla \Phi
\tag{2.1.11}
$$

The Lorenz gauge condition:

$$
\nabla \cdot \mathbf{A} = -j\omega \mu \epsilon \Phi
\tag{2.1.12}
$$

Substituting (2.1.11) into the Ampère-Maxwell law yields:

$$
\nabla^2 \mathbf{A} + k^2 \mathbf{A} = -\mu \mathbf{J}
\tag{2.1.13}
$$

where $k = \omega \sqrt{\mu \epsilon}$ is the wavenumber. Similarly for the scalar potential:

$$
\nabla^2 \Phi + k^2 \Phi = -\frac{\rho_e}{\epsilon}
\tag{2.1.14}
$$

---

## 2.2 Solution of Vector Potentials in Free Space

### 2.2.1 Delta Function and Green's Function

The 3D Dirac delta function satisfies:

$$
\int_V f(\mathbf{r}) \delta(\mathbf{r} - \mathbf{r}') \, dV = f(\mathbf{r}')
\tag{2.2.1}
$$

The Green's function $G(\mathbf{r}, \mathbf{r}')$ for the Helmholtz equation satisfies:

$$
\nabla^2 G(\mathbf{r}, \mathbf{r}') + k^2 G(\mathbf{r}, \mathbf{r}') = -\delta(\mathbf{r} - \mathbf{r}')
\tag{2.2.4}
$$

### 2.2.2 Green's Function in Free Space

For unbounded free space, the solution to (2.2.4) is:

$$
G(\mathbf{r}, \mathbf{r}') = \frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{4\pi |\mathbf{r} - \mathbf{r}'|}
\tag{2.2.10}
$$

This represents an outgoing spherical wave from the source point $\mathbf{r}'$.

### 2.2.3 Radiation by a Volume Current Density

Using the Green's function, the vector potential solution is:

$$
\mathbf{A}(\mathbf{r}) = \mu \iiint_V \mathbf{J}(\mathbf{r}') \, G(\mathbf{r}, \mathbf{r}') \, dV'
\tag{2.2.11}
$$

$$
\mathbf{A}(\mathbf{r}) = \frac{\mu}{4\pi} \iiint_V \mathbf{J}(\mathbf{r}') \frac{e^{-jkR}}{R} \, dV'
\tag{2.2.12}
$$

where $R = |\mathbf{r} - \mathbf{r}'|$.

---

## 2.3 Infinitesimal Electric Dipole (Hertzian Dipole)

### 2.3.1 Vector Potential and Fields

For a short dipole of length $dl$ located at the origin carrying current $I$:

$$
\mathbf{J}(\mathbf{r}') dV' = I \, dl \, \hat{\mathbf{z}}
\tag{2.3.1}
$$

The vector potential at $\mathbf{r} = r\hat{\mathbf{r}}$:

$$
A_z = \frac{\mu I dl}{4\pi} \frac{e^{-jkr}}{r}
\tag{2.3.5}
$$

In spherical coordinates:

$$
A_r = A_z \cos\theta, \quad A_\theta = -A_z \sin\theta, \quad A_\phi = 0
\tag{2.3.9}
$$

### 2.3.2 Field Components

From $\mathbf{H} = \frac{1}{\mu} \nabla \times \mathbf{A}$:

$$
H_\phi = \frac{I dl}{4\pi} \, jk \sin\theta \, \frac{e^{-jkr}}{r} \left(1 + \frac{1}{jkr}\right)
\tag{2.3.14}
$$

From $\mathbf{E} = \frac{1}{j\omega\epsilon} \nabla \times \mathbf{H}$:

$$
E_r = \frac{I dl}{4\pi} \, \eta \, \frac{2\cos\theta}{r^2} \left(1 + \frac{1}{jkr}\right) e^{-jkr}
\tag{2.3.15}
$$

$$
E_\theta = \frac{I dl}{4\pi} \, j\omega\mu \, \sin\theta \, \frac{e^{-jkr}}{r} \left(1 + \frac{1}{jkr} - \frac{1}{k^2 r^2}\right)
\tag{2.3.16}
$$

### 2.3.3 Near-Field ($kr \ll 1$) and Far-Field ($kr \gg 1$)

**Near field (quasi-static, $r \ll \lambda/2\pi$):**

$$
E_\theta \approx \frac{I dl}{4\pi} \, \eta \, \frac{\sin\theta}{jkr^3} e^{-jkr}
\tag{2.3.22}
$$

$$
H_\phi \approx \frac{I dl}{4\pi} \, \frac{\sin\theta}{r^2} e^{-jkr}
\tag{2.3.23}
$$

**Far field (radiation zone, $r \gg \lambda/2\pi$):**

$$
E_\theta \approx j \, \frac{I dl}{4\pi} \, \eta k \, \sin\theta \, \frac{e^{-jkr}}{r}
\tag{2.3.24}
$$

$$
H_\phi \approx j \, \frac{I dl}{4\pi} \, k \sin\theta \, \frac{e^{-jkr}}{r}
\tag{2.3.25}
$$

The wave impedance in the far field:

$$
Z_w = \frac{E_\theta}{H_\phi} = \eta = \sqrt{\frac{\mu}{\epsilon}} \approx 377 \, \Omega
$$

### 2.3.4 Radiated Power

The time-average Poynting vector:

$$
\mathbf{S} = \frac{1}{2} \text{Re}(\mathbf{E} \times \mathbf{H}^*) = \hat{\mathbf{r}} \, \frac{\eta}{2} \left(\frac{I dl}{4\pi} k \sin\theta \frac{1}{r}\right)^2
$$

Total radiated power:

$$
P_{\text{rad}} = \iint_S \mathbf{S} \cdot d\mathbf{s} = \frac{\eta \pi}{3} \left(\frac{I dl}{\lambda}\right)^2
\tag{2.3.28}
$$

Radiation resistance:

$$
R_{\text{rad}} = \frac{2P_{\text{rad}}}{|I|^2} = \frac{2\pi}{3} \eta \left(\frac{dl}{\lambda}\right)^2 = 80\pi^2 \left(\frac{dl}{\lambda}\right)^2 \, (\Omega)
\tag{2.3.29}
$$

---

## 2.4 Infinitesimal Magnetic Dipole

### 2.4.1 Vector Potential and Fields

For a small loop of area $A$, the magnetic dipole moment is $\mathbf{m} = I A \hat{\mathbf{n}}$:

The dual solution to the electric dipole gives:

$$
E_\phi = -\frac{I A}{4\pi} \, \mu \, \omega k \sin\theta \, \frac{e^{-jkr}}{r} \left(1 + \frac{1}{jkr}\right)
\tag{2.4.7}
$$

### 2.4.2 Far-Field Pattern

Equal to electric dipole with $\mathbf{E}$ and $\mathbf{H}$ swapped:

$$
E_\phi \approx j \, \frac{IA \eta k^2}{4\pi} \sin\theta \, \frac{e^{-jkr}}{r}
$$

---

## 2.5 Linear Antenna

### 2.5.1 Current Distribution

For a center-fed dipole of length $L$:

$$
I(z') = I_0 \sin\left[k\left(\frac{L}{2} - |z'|\right)\right]
\tag{2.5.2}
$$

### 2.5.2 Far-Field Radiation

$$
E_\theta = j \, \frac{\eta I_0 e^{-jkr}}{2\pi r} \, \frac{\cos\left(\frac{kL}{2}\cos\theta\right) - \cos\left(\frac{kL}{2}\right)}{\sin\theta}
\tag{2.5.14}
$$

### 2.5.3 Half-Wave Dipole ($L = \lambda/2$)

For $L = \lambda/2$, $kL/2 = \pi/2$:

$$
E_\theta = j \, \frac{\eta I_0 e^{-jkr}}{2\pi r} \, \frac{\cos\left(\frac{\pi}{2}\cos\theta\right)}{\sin\theta}
\tag{2.5.17}
$$

**Directivity:**

$$
D_0 = \frac{4\pi U_{\text{max}}}{P_{\text{rad}}} = 1.64 \, (2.15 \, \text{dBi})
\tag{2.5.20}
$$

Radiation resistance: $R_{\text{rad}} \approx 73 \, \Omega$

---

## 2.6 Far-Field Approximation

### 2.6.1 Fraunhofer Approximation

For observation distance:

$$
R = |\mathbf{r} - \mathbf{r}'| \approx r - \hat{\mathbf{r}} \cdot \mathbf{r}'
\tag{2.6.1}
$$

Phase error < $\pi/8$ when:

$$
r \geq \frac{2D^2}{\lambda} \quad \text{(Fraunhofer distance)}
\tag{2.6.4}
$$

### 2.6.2 Far-Field Radiation Integral

$$
\mathbf{A}(\mathbf{r}) \approx \frac{\mu e^{-jkr}}{4\pi r} \iiint_V \mathbf{J}(\mathbf{r}') e^{jk\hat{\mathbf{r}} \cdot \mathbf{r}'} dV'
\tag{2.6.5}
$$

$$
\mathbf{E}(\mathbf{r}) \approx -j\omega \, \mathbf{A}_t(\mathbf{r})
\tag{2.6.7}
$$

where $\mathbf{A}_t$ is the transverse component of $\mathbf{A}$.
