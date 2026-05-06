# Jackson Ch7: Plane EM Waves and Wave Propagation (§7.1–7.11)

**Unit system:** Gaussian throughout.

---

## 7.1–7.2: Plane Waves in Vacuum

### Wave Equation

\[
\nabla^2 \mathbf{E} - \frac{1}{c^2} \frac{\partial^2 \mathbf{E}}{\partial t^2} = 0, \qquad
\nabla^2 \mathbf{B} - \frac{1}{c^2} \frac{\partial^2 \mathbf{B}}{\partial t^2} = 0
\]

### Plane Wave Solution

\[
\mathbf{E}(\mathbf{x}, t) = \mathbf{E}_0 e^{i(\mathbf{k}\cdot\mathbf{x} - \omega t)}, \quad
\mathbf{B}(\mathbf{x}, t) = \mathbf{B}_0 e^{i(\mathbf{k}\cdot\mathbf{x} - \omega t)}
\]

### Dispersion Relation

\[
\omega = ck
\]

### Transversality

\[
\mathbf{k} \cdot \mathbf{E}_0 = 0, \quad \mathbf{k} \cdot \mathbf{B}_0 = 0
\]
\[
\mathbf{B}_0 = \hat{\mathbf{k}} \times \mathbf{E}_0 \quad (\text{Gaussian SI: } \mathbf{B}_0 = \frac{1}{c}\hat{\mathbf{k}} \times \mathbf{E}_0)
\]

**SI:** \(\mathbf{B}_0 = \frac{1}{c} \hat{\mathbf{k}} \times \mathbf{E}_0\).

---

## 7.3: Polarization

### Linear Polarization

\[
\mathbf{E} = \hat{\boldsymbol{\varepsilon}} E_0 e^{i(kz - \omega t)} \quad (\hat{\boldsymbol{\varepsilon}} \perp \hat{\mathbf{z}})
\]

### Circular Polarization (Jones Vectors)

\[
\hat{\boldsymbol{\varepsilon}}_+ = \frac{1}{\sqrt{2}}(\hat{\mathbf{x}} + i\hat{\mathbf{y}}), \quad
\hat{\boldsymbol{\varepsilon}}_- = \frac{1}{\sqrt{2}}(\hat{\mathbf{x}} - i\hat{\mathbf{y}})
\]

### Elliptical Polarization

General case: \(\mathbf{E}_0 = E_1 \hat{\mathbf{x}} + E_2 e^{i\delta} \hat{\mathbf{y}}\)

- \(\delta = 0, \pi\): linear
- \(\delta = \pm \pi/2, E_1 = E_2\): circular
- Otherwise: elliptical

### Stokes Parameters

\[
s_0 = |E_1|^2 + |E_2|^2
\]
\[
s_1 = |E_1|^2 - |E_2|^2
\]
\[
s_2 = 2\operatorname{Re}(E_1^* E_2)
\]
\[
s_3 = 2\operatorname{Im}(E_1^* E_2)
\]

---

## 7.4–7.5: Reflection and Refraction (Fresnel Equations)

### Snell's Law

\[
\frac{\sin\theta_i}{\sin\theta_t} = \sqrt{\frac{\varepsilon_2\mu_2}{\varepsilon_1\mu_1}} \equiv \frac{n_2}{n_1}
\]

### Fresnel Equations (Gaussian, non-magnetic μ=1)

**TE (s-polarization):** E perpendicular to plane of incidence

\[
r_\perp = \frac{E_{0r}}{E_{0i}} = \frac{n_1\cos\theta_i - n_2\cos\theta_t}{n_1\cos\theta_i + n_2\cos\theta_t}
\]
\[
t_\perp = \frac{E_{0t}}{E_{0i}} = \frac{2n_1\cos\theta_i}{n_1\cos\theta_i + n_2\cos\theta_t}
\]

**TM (p-polarization):** E in plane of incidence

\[
r_\parallel = \frac{n_2\cos\theta_i - n_1\cos\theta_t}{n_2\cos\theta_i + n_1\cos\theta_t}
\]
\[
t_\parallel = \frac{2n_1\cos\theta_i}{n_2\cos\theta_i + n_1\cos\theta_t}
\]

### Brewster Angle

For \(\mu_1 = \mu_2 = 1\):
\[
\tan\theta_B = \frac{n_2}{n_1}
\]

At \(\theta_B\), reflected light is fully s-polarized.

### Total Internal Reflection

When \(n_1 > n_2\) and \(\theta_i > \theta_c = \arcsin(n_2/n_1)\):

- No transmission; evanescent wave in medium 2
- **Goos-Hänchen shift:** lateral displacement of reflected beam

---

## 7.6: Waves in Conductors

### Wave Equation with Conduction

\[
\nabla^2 \mathbf{E} = \frac{\mu\varepsilon}{c^2}\frac{\partial^2 \mathbf{E}}{\partial t^2} + \frac{4\pi\mu\sigma}{c^2} \frac{\partial \mathbf{E}}{\partial t}
\]

### Complex Wave Number

\[
\tilde{k}^2 = \frac{\mu\varepsilon\omega^2}{c^2} + i\frac{4\pi\mu\sigma\omega}{c^2}
\]

### Skin Depth

\[
\delta = \frac{c}{\sqrt{2\pi\mu\sigma\omega}} \quad (\text{Gaussian})
\]

**SI:** \(\delta = \sqrt{\frac{2}{\mu_0\mu_r\sigma\omega}}\)

### Surface Impedance

\[
Z_s = \frac{E_\parallel}{H_\parallel} = (1-i)\sqrt{\frac{\pi\mu\omega}{c^2\sigma}} \quad (\text{Gaussian})
\]

**SI:** \(Z_s = (1+i)\sqrt{\frac{\mu_0\mu_r\omega}{2\sigma}}\)

---

## 7.7–7.8: Wave Propagation in Dispersive Media

### Dispersion Relation

For a dilute plasma (ω ≫ ω₀):
\[
\omega^2 = \omega_p^2 + c^2 k^2
\]

### Phase and Group Velocity

\[
v_p = \frac{\omega}{k}, \quad v_g = \frac{d\omega}{dk}
\]

- Normal dispersion: \(v_g < v_p\)
- Anomalous dispersion: \(v_g > v_p\) (near resonance)

### Kramers–Kronig Relations

Connect real and imaginary parts of \(\varepsilon(\omega)\) (see Ch6 notes).

---

## 7.9–7.10: Superposition and Pulses

### Wave Packets

\[
E(z,t) = \int_{-\infty}^{\infty} A(k) e^{i(kz - \omega(k)t)} dk
\]

### Signal Velocity

- Cannot exceed c (Einstein causality)
- Signal velocity = group velocity for smooth modulation
- For sharp fronts: signal velocity ≤ c (Sommerfeld-Brillouin analysis)

---

## 7.11: Causality and Dispersion

### Cauchy's Principal Value Integrals

\[
\varepsilon(\omega) = 1 + \frac{2}{\pi} \int_0^\infty \frac{\omega' \varepsilon''(\omega')}{\omega'^2 - \omega^2} d\omega'
\]

### Sum Rules

\[
\int_0^\infty \omega \varepsilon''(\omega) d\omega = \frac{\pi}{2} \omega_p^2
\]

where \(\omega_p = \sqrt{4\pi Ne^2/m}\) is the plasma frequency.

---

### Key Formulas Summary

| Quantity | Gaussian | SI |
|----------|----------|-----|
| ω = ck | √(μ₀ε₀) implicit | 1/√(μ₀ε₀) |
| B₀ | Ĥ × E₀ | (1/c)Ĥ×E₀ |
| S | (c/4π)E×B | (1/μ₀)E×B |
| Skin depth δ | c/√(2πμσω) | √(2/μ₀μ_rσω) |
| Plasma freq | ω_p² = 4πNe²/m | ω_p² = Ne²/(ε₀m) |
| n | √(εμ) | √(ε_rμ_r) |

### Notation

- \(n\): refractive index
- \(\hat{\mathbf{k}}\): unit vector in propagation direction
- \(\hat{\boldsymbol{\varepsilon}}\): polarization vector
- \(\delta\): skin depth
- \(r_\perp, r_\parallel\): reflection coefficients
- \(t_\perp, t_\parallel\): transmission coefficients
