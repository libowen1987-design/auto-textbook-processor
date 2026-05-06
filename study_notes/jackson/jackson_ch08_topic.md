# Jackson Ch8: Waveguides, Resonant Cavities, Optical Fibers (§8.1–8.12)

**Unit system:** Gaussian throughout.

---

## 8.1–8.2: Fields in Waveguides

### Assumptions

- Perfectly conducting walls
- Fields have time dependence \(e^{-i\omega t}\)
- Propagation along z: fields ∝ \(e^{i(kz - \omega t)}\)
- Uniform cross-section in xy-plane

### Wave Equation for z-components

\[
\left[\nabla_t^2 + \left(\frac{\omega^2}{c^2} - k^2\right)\right] \begin{Bmatrix} E_z \\ B_z \end{Bmatrix} = 0
\]

where \(\nabla_t^2 = \partial_x^2 + \partial_y^2\).

### Cutoff Wave Number

\[
\gamma^2 = k^2 - \frac{\omega^2}{c^2} = -\kappa^2, \quad
\kappa^2 = \frac{\omega^2}{c^2} - k^2
\]

Propagation when \(\omega > \omega_c\) where \(\omega_c = c\kappa\) is the cutoff frequency.

---

## 8.3: TE and TM Modes

### TE Modes (\(E_z = 0\))

- Boundary condition: \(\frac{\partial B_z}{\partial n} = 0\) on walls
- Transverse fields expressed via \(B_z\):

\[
\mathbf{E}_t = \frac{i\omega/c}{\kappa^2} \, \hat{\mathbf{z}} \times \nabla_t B_z
\]
\[
\mathbf{B}_t = \frac{ik}{\kappa^2} \, \nabla_t B_z
\]

### TM Modes (\(B_z = 0\))

- Boundary condition: \(E_z = 0\) on walls
- Transverse fields via \(E_z\):

\[
\mathbf{E}_t = \frac{ik}{\kappa^2} \, \nabla_t E_z
\]
\[
\mathbf{B}_t = -\frac{i\omega/c}{\kappa^2} \, \hat{\mathbf{z}} \times \nabla_t E_z
\]

---

## 8.4–8.5: Rectangular Waveguide

### Dimensions: \(0 \le x \le a\), \(0 \le y \le b\)

### TM Modes

\[
E_z = E_0 \sin\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right) e^{i(kz - \omega t)}
\]

### TE Modes

\[
B_z = B_0 \cos\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{i(kz - \omega t)}
\]

### Cutoff Frequency

\[
\omega_{mn} = c\pi \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}
\]

### Dispersion Relation

\[
k_{mn} = \sqrt{\frac{\omega^2}{c^2} - \pi^2\left(\frac{m^2}{a^2} + \frac{n^2}{b^2}\right)}
\]

### Dominant Mode (TE₁₀)

- Lowest cutoff for \(a > b\): \(\omega_{10} = \pi c / a\)
- Wavelength: \(\lambda_c = 2a\)
- Used in most practical rectangular waveguides

### Group and Phase Velocity

\[
v_p = \frac{\omega}{k} = \frac{c}{\sqrt{1 - (\omega_c/\omega)^2}}, \quad
v_g = c\sqrt{1 - (\omega_c/\omega)^2}
\]

Note: \(v_p v_g = c^2\).

---

## 8.6: Circular Waveguide

### TE Modes (Bessel functions)

\[
B_z = B_0 J_m(\kappa_{mn} \rho) \cos(m\phi) e^{i(kz - \omega t)}
\]

Boundary condition: \(J_m'(\kappa_{mn} a) = 0\)

### TM Modes

\[
E_z = E_0 J_m(\kappa_{mn} \rho) \cos(m\phi) e^{i(kz - \omega t)}
\]

Boundary condition: \(J_m(\kappa_{mn} a) = 0\)

### Cutoff Frequencies

- TE₁₁: \(\kappa_{11} a = 1.841\) (dominant mode)
- TE₀₁: \(\kappa_{01} a = 3.832\)
- TM₀₁: \(\kappa_{01} a = 2.405\)

---

## 8.7: Energy Flow and Attenuation

### Power Flow

\[
P = \frac{c}{8\pi} \operatorname{Re} \int_S (\mathbf{E} \times \mathbf{B}^*) \cdot \hat{\mathbf{z}} \, da
\]

### Attenuation Constant

\[
\alpha = \frac{P_\text{loss}}{2P}
\]

For imperfect conductors: loss in walls due to finite conductivity.

### Dielectric Loss

If waveguide is filled with dielectric \(\varepsilon = \varepsilon' + i\varepsilon''\):
\[
\alpha_d = \frac{\omega}{c} \frac{\varepsilon''}{2\sqrt{\varepsilon'}}
\]

---

## 8.8–8.9: Resonant Cavities

### Rectangular Cavity

Dimensions: \(0 \le x \le a\), \(0 \le y \le b\), \(0 \le z \le d\)

Standing wave along z: \(k = p\pi/d\)

### Resonant Frequency

\[
\omega_{mnp} = c\pi \sqrt{\frac{m^2}{a^2} + \frac{n^2}{b^2} + \frac{p^2}{d^2}}
\]

### Quality Factor (Q)

\[
Q = \omega_0 \frac{U}{P_\text{loss}} = \frac{2}{\delta} \frac{V}{S} \quad (\text{for good conductors})
\]

where \(\delta\) is skin depth, V is cavity volume, S is surface area.

### TE₁₀₁ Mode Example

- Fields:

\[
E_y = E_0 \sin\left(\frac{\pi x}{a}\right) \sin\left(\frac{\pi z}{d}\right)
\]
\[
B_x = -\frac{i ck_z}{\omega} E_0 \sin\left(\frac{\pi x}{a}\right) \cos\left(\frac{\pi z}{d}\right)
\]
\[
B_z = -\frac{i \pi c}{\omega a} E_0 \cos\left(\frac{\pi x}{a}\right) \sin\left(\frac{\pi z}{d}\right)
\]

---

## 8.10: Cylindrical Cavity

### TE Modes

- Resonant frequency: \(\omega_{mnp} = c\sqrt{(\kappa_{mn}/R)^2 + (p\pi/d)^2}\)
- \(\kappa_{mn} a = \) roots of \(J_m'(x) = 0\)

### TM Modes

- \(\omega_{mnp} = c\sqrt{(\kappa_{mn}/R)^2 + (p\pi/d)^2}\)
- \(\kappa_{mn} a = \) roots of \(J_m(x) = 0\)

---

## 8.11: Dielectric Waveguides (Optical Fibers)

### Step-Index Fiber

- Core: \(n_1\), radius \(a\)
- Cladding: \(n_2 < n_1\)

### V Parameter (Normalized Frequency)

\[
V = \frac{2\pi a}{\lambda} \sqrt{n_1^2 - n_2^2} = \frac{\omega a}{c} \sqrt{n_1^2 - n_2^2}
\]

### Single-Mode Condition

\[
V < 2.405
\]

### HE₁₁ Mode: fundamental mode of optical fiber

- Always propagates (no cutoff)
- Hybrid mode (both Ez and Bz nonzero)

### Mode Classification

- **TE₀ₘ, TM₀ₘ:** axially symmetric modes
- **HEₘₙ, EHₘₙ:** hybrid modes, \(m \neq 0\)

---

## 8.12: Attenuation in Optical Fibers

### Loss Mechanisms

- **Rayleigh scattering:** \(\propto 1/\lambda^4\) (dominates at short wavelengths)
- **Absorption:** OH⁻ impurities, electronic transitions
- **Bending loss:** radiative loss at bends
- **Connector/splice loss:** misalignment

### Minimum Loss

- Practical silica fiber: ~0.2 dB/km at 1.55 μm
- Window wavelengths: 1.3 μm, 1.55 μm

---

### Key Formulas Summary

| Quantity | Expression |
|----------|-----------|
| Cutoff freq (rect.) | \(\omega_{mn} = c\pi\sqrt{(m/a)^2 + (n/b)^2}\) |
| Rectangular cavity | \(\omega_{mnp} = c\pi\sqrt{(m/a)^2 + (n/b)^2 + (p/d)^2}\) |
| v_p v_g | \(v_p v_g = c^2\) |
| V parameter | \(V = (2\pi a/\lambda)\sqrt{n_1^2 - n_2^2}\) |
| Single-mode fiber | \(V < 2.405\) |
| Q factor | \(Q = \omega_0 U / P_\text{loss}\) |
