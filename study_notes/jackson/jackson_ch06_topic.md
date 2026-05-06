# Jackson Ch6: Maxwell Equations, Macroscopic Electromagnetism (§6.1–6.13)

**Unit system:** Gaussian throughout.

---

## 6.1–6.2: Maxwell's Equations

### Microscopic Maxwell Equations (Gaussian)

\[
\nabla \cdot \mathbf{E} = 4\pi\rho
\]
\[
\nabla \cdot \mathbf{B} = 0
\]
\[
\nabla \times \mathbf{E} + \frac{1}{c}\frac{\partial \mathbf{B}}{\partial t} = 0
\]
\[
\nabla \times \mathbf{B} - \frac{1}{c}\frac{\partial \mathbf{E}}{\partial t} = \frac{4\pi}{c} \mathbf{J}
\]

### Integral form surface

| Equation | Integral Form |
|----------|--------------|
| Gauss E | ∮ E·da = 4πQ_enc |
| Gauss B | ∮ B·da = 0 |
| Faraday | ∮ E·dl = -(1/c) dΦ_B/dt |
| Ampère-Maxwell | ∮ B·dl = (4π/c)I_enc + (1/c) dΦ_E/dt |

### SI Version for Reference

\[
\nabla \cdot \mathbf{E} = \rho/\varepsilon_0
\]
\[
\nabla \cdot \mathbf{B} = 0
\]
\[
\nabla \times \mathbf{E} + \frac{\partial \mathbf{B}}{\partial t} = 0
\]
\[
\nabla \times \mathbf{B} - \mu_0\varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} = \mu_0\mathbf{J}
\]

where \(c = 1/\sqrt{\mu_0\varepsilon_0}\).

---

## 6.3–6.4: Conservation Laws

### Poynting's Theorem (Energy Conservation)

\[
\frac{\partial u}{\partial t} + \nabla \cdot \mathbf{S} = -\mathbf{J} \cdot \mathbf{E}
\]

- **Energy density:** \(u = \frac{1}{8\pi}(E^2 + B^2)\)
- **Poynting vector:** \(\mathbf{S} = \frac{c}{4\pi} \mathbf{E} \times \mathbf{B}\)

**SI:** \(u = \frac{1}{2}\varepsilon_0 E^2 + \frac{1}{2\mu_0}B^2\), \(\mathbf{S} = \frac{1}{\mu_0}\mathbf{E}\times\mathbf{B}\)

### Momentum Conservation

\[
\mathbf{g} = \frac{1}{4\pi c} \mathbf{E} \times \mathbf{B} = \frac{1}{c^2} \mathbf{S}
\]

- **Maxwell stress tensor** \(T_{ij}\):

\[
T_{ij} = \frac{1}{4\pi}\left[ E_i E_j + B_i B_j - \frac{1}{2}\delta_{ij}(E^2 + B^2) \right]
\]

**Force:** \(F_i = \oint_S T_{ij} n_j da\)

---

## 6.5–6.8: Macroscopic Equations

### Macroscopic Maxwell Equations

\[
\nabla \cdot \mathbf{D} = 4\pi\rho_f
\]
\[
\nabla \cdot \mathbf{B} = 0
\]
\[
\nabla \times \mathbf{E} + \frac{1}{c}\frac{\partial \mathbf{B}}{\partial t} = 0
\]
\[
\nabla \times \mathbf{H} - \frac{1}{c}\frac{\partial \mathbf{D}}{\partial t} = \frac{4\pi}{c} \mathbf{J}_f
\]

### Constitutive Relations

Linear isotropic media:

\[
\mathbf{D} = \varepsilon \mathbf{E}, \quad \mathbf{B} = \mu \mathbf{H}, \quad \mathbf{J}_f = \sigma \mathbf{E}
\]

In vacuum: \(\varepsilon = 1\), \(\mu = 1\).

### Dielectric Boundary Conditions

\[
(D_2 - D_1)\cdot \hat{\mathbf{n}} = 4\pi\sigma_f
\]
\[
\hat{\mathbf{n}} \times (\mathbf{E}_2 - \mathbf{E}_1) = 0
\]
\[
(B_2 - B_1)\cdot \hat{\mathbf{n}} = 0
\]
\[
\hat{\mathbf{n}} \times (\mathbf{H}_2 - \mathbf{H}_1) = \frac{4\pi}{c} \mathbf{K}_f
\]

---

## 6.9–6.10: Frequency-Dependent Properties

### Complex Dielectric Constant

\[
\tilde{\varepsilon}(\omega) = \varepsilon'(\omega) + i\varepsilon''(\omega)
\]

### Complex Conductivity

\[
\tilde{\sigma}(\omega) = \sigma'(\omega) + i\sigma''(\omega)
\]

Relation: \(\tilde{\varepsilon}(\omega) = 1 + \frac{4\pi i}{\omega} \tilde{\sigma}(\omega)\) (Gaussian).

### Dispersion Relations (Kramers–Kronig)

\[
\varepsilon'(\omega) - 1 = \frac{2}{\pi} P \int_0^\infty \frac{\omega' \varepsilon''(\omega')}{\omega'^2 - \omega^2} d\omega'
\]
\[
\varepsilon''(\omega) = -\frac{2\omega}{\pi} P \int_0^\infty \frac{\varepsilon'(\omega') - 1}{\omega'^2 - \omega^2} d\omega'
\]

These follow from causality (analyticity of \(\varepsilon(\omega)\) in upper half-plane).

---

## 6.11–6.13: Applications

### Simple Polarizable Media

- **Lorentz oscillator model:**

\[
m\ddot{\mathbf{x}} + m\gamma \dot{\mathbf{x}} + m\omega_0^2 \mathbf{x} = -e\mathbf{E}(t)
\]

- **Resulting polarization:**

\[
\mathbf{P} = N e \mathbf{x}, \quad \varepsilon(\omega) = 1 + \frac{\omega_p^2}{\omega_0^2 - \omega^2 - i\gamma\omega}
\]

where \(\omega_p = \sqrt{4\pi N e^2/m}\) is the plasma frequency.

### Plasma Frequency

\[
\omega_p = \sqrt{\frac{4\pi N e^2}{m}} \quad \text{(Gaussian)} \quad \text{vs} \quad
\omega_p = \sqrt{\frac{N e^2}{\varepsilon_0 m}} \quad \text{(SI)}
\]

### Pulsed Plane Wave Reflection

- Reflection from conducting surface: boundary condition \(\mathbf{E}_{\parallel} = 0\)
- Retarded potentials used for time-dependent sources

### Retarded Potentials

\[
\Phi(\mathbf{x}, t) = \int \frac{[\rho(\mathbf{x}', t')]}{|\mathbf{x} - \mathbf{x}'|} d^3x'
\]
\[
\mathbf{A}(\mathbf{x}, t) = \frac{1}{c} \int \frac{[\mathbf{J}(\mathbf{x}', t')]}{|\mathbf{x} - \mathbf{x}'|} d^3x'
\]

where \(t' = t - |\mathbf{x} - \mathbf{x}'|/c\) is the retarded time.

### Inhomogeneous Wave Equation

\[
\Box^2 \Phi = -4\pi\rho, \quad \Box^2 \mathbf{A} = -\frac{4\pi}{c} \mathbf{J}
\]

where \(\Box^2 \equiv \nabla^2 - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}\) is the d'Alembertian operator.

---

### Key Formulas Summary

| Quantity | Gaussian | SI |
|----------|----------|-----|
| ∇·E | 4πρ | ρ/ε₀ |
| ∇×B - (1/c)∂E/∂t | (4π/c)J | μ₀J + μ₀ε₀∂E/∂t |
| ∂u/∂t + ∇·S | -J·E | -J·E |
| u | (E²+B²)/8π | ½ε₀E² + B²/2μ₀ |
| S | (c/4π)E×B | (1/μ₀)E×B |
| ω_p² | 4πNe²/m | Ne²/ε₀m |
