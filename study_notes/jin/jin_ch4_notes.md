---
title: "Chapter 4 — Transmission Lines and Plane Waves"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Transmission line theory (RLCG parameters, Telegrapher's equations)
  - Uniform plane waves in unbounded media
  - Reflection and transmission at planar interfaces
  - Polarization (linear, circular, elliptical)
  - Dispersive media, group velocity, attenuation
  - Waves in anisotropic (uniaxial, gyrotropic) and bi-isotropic (chiral) media
---

# Chapter 4: Transmission Lines and Plane Waves

## 4.1 Transmission Line Theory

**Telegrapher's equations:**

$$
\frac{dV}{dz} + (j\omega L + R)I = 0, \quad \frac{dI}{dz} + (j\omega C + G)V = 0
\tag{4.1.1, 4.1.2}
$$

Wave equation:

$$
\frac{d^2 V}{dz^2} - \gamma^2 V = 0, \quad \gamma = \sqrt{(j\omega L + R)(j\omega C + G)}
\tag{4.1.3}
$$

**Characteristic impedance:**

$$
Z_0 = \sqrt{\frac{j\omega L + R}{j\omega C + G}}
$$

For lossless line: $Z_0 = \sqrt{L/C}$, $\beta = \omega\sqrt{LC}$, $v_p = 1/\sqrt{LC}$.

**Reflection coefficient:**

$$
\Gamma(z) = \frac{V^-(z)}{V^+(z)} = \Gamma_L e^{2\gamma(z - L)}, \quad
\Gamma_L = \frac{Z_L - Z_0}{Z_L + Z_0}
$$

**Input impedance:**

$$
Z_{\text{in}}(z) = Z_0 \frac{Z_L + Z_0 \tanh(\gamma l)}{Z_0 + Z_L \tanh(\gamma l)}
$$

**Smith chart** — graphical tool for impedance/reflection coefficient visualization.

---

## 4.2 Uniform Plane Waves

For a plane wave propagating in $+\hat{z}$ direction, fields are transverse ($E_z = H_z = 0$):

$$
\mathbf{E}(z) = \hat{x} E_0 e^{-jkz}, \quad \mathbf{H}(z) = \hat{y} \frac{E_0}{\eta} e^{-jkz}
$$

**Intrinsic impedance:** $\eta = \sqrt{j\omega\mu / (\sigma + j\omega\epsilon)}$.

For lossless media: $\eta = \sqrt{\mu/\epsilon}$.

**Phase velocity:** $v_p = \omega/k = 1/\sqrt{\mu\epsilon}$.

**Attenuation in lossy media:** $\gamma = \alpha + j\beta$, where $\alpha$ is attenuation constant.

---

## 4.3 Reflection and Transmission at Planar Interfaces

**Normal incidence:**

$$
\Gamma = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1}, \quad
T = \frac{2\eta_2}{\eta_2 + \eta_1}
$$

**Oblique incidence** — Snell's law:

$$
k_1 \sin\theta_i = k_1 \sin\theta_r = k_2 \sin\theta_t
$$

**Fresnel coefficients (TE/S polarization):**

$$
R_\perp = \frac{\eta_2 \cos\theta_i - \eta_1 \cos\theta_t}{\eta_2 \cos\theta_i + \eta_1 \cos\theta_t}
$$

**Fresnel coefficients (TM/P polarization):**

$$
R_\parallel = \frac{\eta_2 \cos\theta_t - \eta_1 \cos\theta_i}{\eta_2 \cos\theta_t + \eta_1 \cos\theta_i}
$$

**Brewster angle** (zero reflection for TM): $\tan\theta_B = \sqrt{\epsilon_2/\epsilon_1}$.

**Total internal reflection** when $\theta_i > \theta_c = \sin^{-1}(\sqrt{\epsilon_2/\epsilon_1})$.

---

## 4.4 Polarization

**Linear:** $E_x$ and $E_y$ in phase.

**Circular:** $|E_x| = |E_y|$, phase difference $\pm 90^\circ$.

**Elliptical:** general case.

---

## 4.5 Dispersion

**Group velocity:** $v_g = d\omega/dk$.

In a dispersive medium, signal pulse broadens. Relation: $v_g v_p = c^2/n_g$.

---

## 4.6 Anisotropic & Bi-isotropic Media

**Uniaxial medium:** $\overline{\epsilon} = \text{diag}(\epsilon_t, \epsilon_t, \epsilon_z)$. Ordinary ($k_o = \omega\sqrt{\mu\epsilon_t}$) and extraordinary waves.

**Gyrotropic medium (magnetized plasma):** $\overline{\epsilon}$ has off-diagonal components → Faraday rotation.

**Chiral medium:** $D = \epsilon E + \xi H$, $B = \mu H + \zeta E$ → handedness-dependent propagation.

---

## Key Physical Intuition

1. **TL analogy** connects distributed-circuit concepts ($V$, $I$, $Z_0$) to wave propagation ($E$, $H$, $\eta$).
2. **Plane waves are the simplest wave solution** — any wavefront can be approximated as locally planar.
3. **Polarization** matters for antenna design, radar polarimetry, and optical communication.
4. **Dispersion** distorts pulses — crucial for high-speed digital and broadband systems.

---

## Audit

| Section | Content Coverage |
|---------|-----------------|
| 4.1 | Transmission line theory |
| 4.2 | Uniform plane waves |
| 4.3 | Reflection & transmission |
| 4.4 | Polarization |
| 4.5 | Dispersion |
| 4.6 | Anisotropic media |
