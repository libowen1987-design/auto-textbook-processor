# Jackson Ch5: Magnetostatics, Faraday's Law, Quasi-Static Fields (§5.1–5.18)

**Unit system:** Gaussian throughout except where noted.

---

## 5.1–5.3: Biot–Savart Law and Ampère's Law

### Biot–Savart Law (Gaussian)

\[
\mathbf{B}(\mathbf{x}) = \frac{1}{c} \int \frac{\mathbf{J}(\mathbf{x}') \times (\mathbf{x} - \mathbf{x}')}{|\mathbf{x} - \mathbf{x}'|^3}\, d^3x'
\]

**SI version** (for reference):

\[
\mathbf{B}(\mathbf{x}) = \frac{\mu_0}{4\pi} \int \frac{\mathbf{J}(\mathbf{x}') \times (\mathbf{x} - \mathbf{x}')}{|\mathbf{x} - \mathbf{x}'|^3}\, d^3x'
\]

### Ampère's Law (Differential)

\[
\nabla \times \mathbf{B} = \frac{4\pi}{c} \mathbf{J}
\]

### Vector Potential

\[
\mathbf{B} = \nabla \times \mathbf{A}, \qquad \nabla \cdot \mathbf{A} = 0 \quad (\text{Coulomb gauge})
\]

\[
\nabla^2 \mathbf{A} = -\frac{4\pi}{c} \mathbf{J} \quad \Longrightarrow \quad
\mathbf{A}(\mathbf{x}) = \frac{1}{c} \int \frac{\mathbf{J}(\mathbf{x}')}{|\mathbf{x} - \mathbf{x}'|}\, d^3x'
\]

### Key expansions

- **Multipole expansion** of vector potential (5.4):

\[
A_i(\mathbf{x}) = \frac{1}{c} \sum_{n=0}^\infty \frac{(-1)^n}{n!} \int J_i(\mathbf{x}')(\mathbf{x}'\cdot \nabla)^n \frac{1}{r}\, d^3x'
\]

- **Magnetic dipole moment**:

\[
\mathbf{m} = \frac{1}{2c} \int \mathbf{x}' \times \mathbf{J}(\mathbf{x}')\, d^3x'
\]

- **Vector potential of a dipole**:

\[
\mathbf{A}(\mathbf{x}) = \frac{\mathbf{m} \times \mathbf{x}}{|\mathbf{x}|^3}
\]

- **Magnetic field of a dipole**:

\[
\mathbf{B}(\mathbf{x}) = \frac{3\mathbf{n}(\mathbf{n}\cdot\mathbf{m}) - \mathbf{m}}{|\mathbf{x}|^3} + \frac{8\pi}{3} \mathbf{m}\,\delta(\mathbf{x})
\]

---

## 5.4–5.6: Energy and Force

### Magnetic Energy

\[
W = \frac{1}{8\pi} \int \mathbf{B}\cdot\mathbf{H}\, d^3x = \frac{1}{2c} \int \mathbf{J}\cdot\mathbf{A}\, d^3x
\]

### Force on a Current Distribution

\[
\mathbf{F} = \int \mathbf{J} \times \mathbf{B}\, d^3x
\]

### Magnetic Torque

\[
\mathbf{N} = \mathbf{m} \times \mathbf{B}
\]

---

## 5.7–5.9: Boundary Conditions and Magnetization

### Macroscopic Equations

\[
\nabla \times \mathbf{H} = \frac{4\pi}{c} \mathbf{J}_f, \qquad
\mathbf{B} = \mathbf{H} + 4\pi \mathbf{M}
\]

### Boundary Conditions

\[
(B_2 - B_1)\cdot \hat{\mathbf{n}} = 0, \qquad
\hat{\mathbf{n}} \times (\mathbf{H}_2 - \mathbf{H}_1) = \frac{4\pi}{c} \mathbf{K}_f
\]

### Magnetic Susceptibility

Linear media: \(\mathbf{M} = \chi_m \mathbf{H}\), \(\mathbf{B} = \mu \mathbf{H}\), \(\mu = 1 + 4\pi\chi_m\) (Gaussian).

**SI version:** \(\mathbf{B} = \mu_0(\mathbf{H} + \mathbf{M})\), \(\mu_r = 1 + \chi_m\).

---

## 5.10–5.12: Faraday's Law and Inductance

### Faraday's Law (Gaussian)

\[
\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{1}{c} \frac{d}{dt} \int_S \mathbf{B} \cdot \hat{\mathbf{n}}\, da
\]

Differential form:

\[
\nabla \times \mathbf{E} = -\frac{1}{c} \frac{\partial \mathbf{B}}{\partial t}
\]

### Mutual Inductance

\[
M_{ij} = \frac{1}{c^2} \oint_{C_i} \oint_{C_j} \frac{d\mathbf{l}_i \cdot d\mathbf{l}_j}{|\mathbf{x}_i - \mathbf{x}_j|}
\]

### Self-Inductance

\[
L = \frac{c\Phi}{I} \quad \text{(Gaussian)} \quad \text{vs} \quad
L = \frac{\Phi}{I} \quad \text{(SI)}
\]

---

## 5.13–5.15: Quasi-Static Fields

### Approximation Conditions

- Displacement current negligible: \(\omega \ll c/L\) where \(L\) is the system size
- Eddy currents: skin depth \(\delta = c/\sqrt{2\pi\mu\sigma\omega}\) (Gaussian)

### Diffusion Equation

\[
\nabla^2 \mathbf{B} = \frac{4\pi\mu\sigma}{c^2} \frac{\partial \mathbf{B}}{\partial t}
\]

**SI version:** \(\nabla^2 \mathbf{B} = \mu_0\mu_r\sigma \frac{\partial \mathbf{B}}{\partial t}\)

---

## 5.16–5.18: Applications

### Magnetic Shielding

- Field penetration through a cylindrical shell
- Spherical shell: interior field is uniform and reduced by factor \(\sim 1/(\mu R)\)

### Hall Effect

\[
\mathbf{E}_H = \frac{1}{nec} \mathbf{J} \times \mathbf{B}
\]

### Magnetic Scalar Potential

In current-free regions:
\[
\mathbf{H} = -\nabla \Phi_M, \qquad \nabla^2 \Phi_M = 0
\]

### Units Conversion Summary

| Quantity | Gaussian | SI |
|----------|----------|-----|
| B field | G (gauss) | T (tesla) |
| H field | Oe (oersted) | A/m |
| B equation | ∇×B = (4π/c)J | ∇×B = μ₀J |
| Faraday | ∇×E = -(1/c)∂B/∂t | ∇×E = -∂B/∂t |
| μ | μ = 1+4πχ_m | μ_r = 1+χ_m |
| E × B | (1/4π)E×B | (1/μ₀)E×B |

Conversion: 1 T = 10⁴ G, 1 A/m = 4π×10⁻³ Oe.
