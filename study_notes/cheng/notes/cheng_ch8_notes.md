# 程守洙《普通物理学》电磁学部分 第8章：电磁振荡与电磁波

> **来源：** 谢处方等，《电磁场与电磁波》，第8章
> **提取方式：** 📷 扫描PDF → OCR → 人工清洗

---

## 8.1 电磁振荡与电磁波 | Electromagnetic Oscillations and Waves

# David K. Cheng《Field and Wave Electromagnetics》2nd Ed Chapter 8
 本笔记基于  文本清洗整理100% 来源于原书内容
## Chapter 8 — Plane Electromagnetic Waves
### 8-1. Introduction
$\mathbf{A}$ **plane wave** is a wave in which the field vectors $\mathbf{E}$ and $\mathbf{H}$ are constant in magnitude and direction over a plane (wavefront). Plane waves are the fundamental building blocks for analyzing more complex wave phenomena.
### 8-2. Uniform Plane Waves in Lossless Media
In a lossless medium ($\sigma = 0$, $\varepsilon$, $\mu$ real), the wave equation simplifies. For a uniform plane wave propagating in the $\pm z$ direction:
$$\mathbf{E}(z) = $\mathbf{E}$_0 e^{\mp jkz} \hat{\mathbf{x}}$$
$$\mathbf{H}(z) = \pm \frac{$\mathbf{E}$_0}{\eta} e^{\mp jkz} \hat{\mathbf{y}}$$
where:
- **Wave number:** $$\mathbf{k}$ = $\omega$\sqrt{$\mu$\varepsilon} = \frac{2\pi}{\lambda}$
- **Intrinsic impedance:** $\eta = \sqrt{$\mu$/\varepsilon}$
- **Wave velocity:** $u = \frac{\omega}{k} = \frac{1}{\sqrt{$\mu$\varepsilon}} = \frac{c}{n}$
In free space: $\eta_0 = \sqrt{\mu_0/\varepsilon_0} \approx 120\pi \approx 377$ $\Omega$.
**Important properties:**
- $\mathbf{E}$, $\mathbf{H}$, and propagation direction are mutually perpendicular (TEM wave).
- $\mathbf{E} \times \mathbf{H}$ points in the direction of propagation.
- $|\mathbf{E}|/|\mathbf{H}| = \eta$.
### 8-2.1. Transverse Electromagnetic (TEM) Waves
In a TEM wave, both $\mathbf{E}$ and $\mathbf{H}$ are perpendicular to the direction of propagation. Uniform plane waves in free space or lossless dielectrics are TEM waves.
### 8-2.2. Polarization
**Polarization** describes the direction and phase relationship of the $\mathbf{E}$ vector as a function of time.
- **Linear polarization:** $\mathbf{E}$ oscillates along a fixed direction.
- **Circular polarization:** $\mathbf{E}$ rotates at constant angular velocity (tip traces a circle). Right-hand circular polarization (RHC): $\mathbf{E}$ rotates clockwise when viewed from behind the source.
- **Elliptical polarization:** General case — tip traces an ellipse.
For RHC wave propagating in $+z$:
$$\mathbf{E} = $\mathbf{E}$_0(\hat{\mathbf{x}} - j\hat{\mathbf{y}})e^{-jkz}$$
### 8-3. Plane Waves in Conducting Media
In a conducting medium ($\sigma \neq 0$), the wave propagates with **attenuation**:
$$\gamma = \alpha + j\beta = \sqrt{j$\omega$$\mu$(\sigma + j$\omega$$\varepsilon$)}$$
For **good conductors** ($\sigma \gg $\omega$\varepsilon$):
$$\alpha \approx \beta \approx \sqrt{\frac{$\omega$$\mu$\sigma}{2}} = \frac{1}{\delta_s}$$
$$\delta_s = \sqrt{\frac{2}{$\omega$$\mu$\sigma}} \quad \text{(skin depth)}$$
The **skin depth** $\delta_s$ is the distance over which the wave amplitude decays by $1/e$.
**Intrinsic impedance of a conductor:**
$$\eta_c \approx (1+j)\frac{\alpha}{\sigma} = (1+j)\frac{1}{$\sigma$\delta_s}$$
For **low-loss dielectrics** ($\sigma \ll $\omega$\varepsilon$):
$$\alpha \approx \frac{\sigma}{2}\sqrt{\frac{\mu}{\varepsilon}}, \quad \beta \approx $\omega$\sqrt{$\mu$\varepsilon}$$
### 8-4. Flow of Electromagnetic Power — The Poynting Vector
**Instantaneous Poynting vector:**
$$\mathbf{S} = \mathbf{E} \times \mathbf{H} \quad \text{(W/m}^2\text{)}$$
The direction of $\mathbf{S}$ is the direction of power flow.
**For time-harmonic fields (time-average):**
$$\mathbf{S}_{\text{avg}} = \frac{1}{2}\text{Re}\{\tilde{\mathbf{E}} \times \tilde{\mathbf{H}}^*\} = \frac{|$\mathbf{E}$_0|^2}{2\eta}\hat{\mathbf{k}} \quad \text{(for uniform plane wave)}$$
In a conducting medium:
$$\mathbf{S}_{\text{avg}} = \frac{|$\mathbf{E}$_0|^2}{2\eta_{\text{real}}}\hat{\mathbf{z}}$$
### 8-5. Normal Incidence at a Plane Conducting Boundary
For a wave incident normally on a perfect conductor ($z = 0$):
- The **standing wave** pattern forms: $\mathbf{E}(z) = -jE_0\sin(kz)\hat{\mathbf{x}}$ (since $$\mathbf{E}$_z=0$ at $z=0$)
- $\mathbf{H}$ has no zeros at the surface: $\mathbf{H}(z) = \frac{$\mathbf{E}$_0}{\eta}\cos(kz)\hat{\mathbf{y}}$
- The electric field is maximum at the surface (antinode), magnetic field is maximum (node for $H$? No, $\mathbf{E}$ is zero for a perfect conductor at the boundary).
For a **finite conductivity** conductor, some power is absorbed (dissipated as heat).
### 8-6. Oblique Incidence at a Plane Conducting Boundary
For oblique incidence, decompose into perpendicular (horizontal, $\perp$) and parallel (vertical, $\parallel$) polarization components relative to the plane of incidence.
**Snell's laws** at reflection:
$$\theta_i = \theta_r \quad \text{(angle of incidence = angle of reflection)}$$
**For perpendicular polarization:**
$$\cos\theta_i \neq 0$$ and there may be a Brewster angle where reflection is zero (for non-perfect conductors).
### 8-7. Normal Incidence at a Plane Dielectric Boundary
At the interface between two lossless media ($\varepsilon_1$, $\mu_1 = \mu_0$; $\varepsilon_2$, $\mu_2 = \mu_0$):
**Reflection coefficient:**
$$\Gamma = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1}$$
**Transmission coefficient:**
$$\tau = \frac{2\eta_2}{\eta_2 + \eta_1}$$
The standing wave ratio (SWR):
$$\text{SWR} = \frac{1+|\Gamma|}{1-|\Gamma|}$$
### 8-8. Normal Incidence at Multiple Dielectric Interfaces
For multiple parallel dielectric layers, the overall reflection and transmission coefficients are computed by cascading the individual reflection/transmission at each interface using the transmission-line analogy.
### 8-9. Oblique Incidence at a Plane Dielectric Boundary
**Snell's law of refraction:**
$$\frac{\sin\theta_i}{\sin\theta_t} = \frac{u_1}{u_2} = \sqrt{\frac{\varepsilon_2}{\varepsilon_1}} = \frac{n_2}{n_1}$$
**Total reflection** occurs when the wave goes from a denser to a rarer medium and $\sin\theta_t > 1$. The **critical angle**:
$$\theta_c = \sin^{-1}\sqrt{\frac{\varepsilon_2}{\varepsilon_1}} \quad (\varepsilon_2 < \varepsilon_1)$$
Above $\theta_c$, **total internal reflection** occurs.
**Brewster angle** (angle of zero reflection for parallel polarization):
$$\theta_$\mathbf{B}$ = \tan^{-1}\sqrt{\frac{\varepsilon_2}{\varepsilon_1}} \quad \text{(parallel polarization only)}$$
### Review Questions (Chapter 8)
1. What is a uniform plane wave? What are its key properties?
2. Define wave number, intrinsic impedance, and skin depth.
3. What is the difference between a good conductor and a low-loss dielectric?
4. Explain polarization — linear, circular, elliptical.
5. What is the Poynting vector and what does it represent?
6. State Snell's laws for reflection and refraction.
7. Under what condition does total internal reflection occur?
---