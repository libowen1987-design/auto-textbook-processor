# Chapter 3: Transmission Lines and Waveguides

**Source:** Robert E. Collin, *Foundations for Microwave Engineering*, 2nd Ed., IEEE Press, 2000, Ch. 3 (§3.1–§3.8), pp. 71–140.

> IEEE Press Classic Reissue, ISBN 0-7803-6031-1

---

## §3.1 Transmission Line Theory (pp. 71–96)

### Distributed Parameters (p. 72, Fig. 3.1)

A transmission line is characterized by **per-unit-length parameters**:

| Parameter | Symbol | Unit | Physical Origin |
|-----------|--------|------|----------------|
| Series resistance | $R$ | Ω/m | Conductor ohmic loss (skin effect) |
| Series inductance | $L$ | H/m | Magnetic flux around conductors |
| Shunt conductance | $G$ | S/m | Dielectric loss in insulation |
| Shunt capacitance | $C$ | F/m | Electric field between conductors |

For a **lossless line**: $R = 0$, $G = 0$.

### Telegrapher's Equations (§3.1, p. 73)

From Kirchhoff's laws applied to an infinitesimal segment $\Delta z$:

**Time-domain:**
$$
-\frac{\partial v(z,t)}{\partial z} = R\,i(z,t) + L\frac{\partial i(z,t)}{\partial t}
$$
$$
-\frac{\partial i(z,t)}{\partial z} = G\,v(z,t) + C\frac{\partial v(z,t)}{\partial t}
$$

**Phasor form** (assuming $e^{j\omega t}$ time dependence):
$$
-\frac{dV(z)}{dz} = (R + j\omega L)\,I(z)
$$
$$
-\frac{dI(z)}{dz} = (G + j\omega C)\,V(z)
$$

### Wave Equation and Solution (§3.1, pp. 73–74)

Combine the telegrapher's equations to obtain the **wave equation**:
$$
\frac{d^2 V(z)}{dz^2} - \gamma^2 V(z) = 0, \qquad
\frac{d^2 I(z)}{dz^2} - \gamma^2 I(z) = 0
$$

**Propagation constant:**
$$
\gamma = \alpha + j\beta = \sqrt{(R + j\omega L)(G + j\omega C)}
$$

where:
- $\alpha$ = attenuation constant [Np/m] (conductor + dielectric losses)
- $\beta$ = phase constant [rad/m]

**General solution** (forward + backward traveling waves):
$$
V(z) = V_0^+ e^{-\gamma z} + V_0^- e^{\gamma z}
$$
$$
I(z) = I_0^+ e^{-\gamma z} + I_0^- e^{\gamma z}
$$

### Characteristic Impedance (§3.1, p. 74)

$$
Z_0 = \sqrt{\frac{R + j\omega L}{G + j\omega C}} \quad [\Omega]
$$

For a **lossless line**:
$$
Z_0 = \sqrt{\frac{L}{C}}, \qquad \beta = \omega\sqrt{LC}, \qquad v_p = \frac{\omega}{\beta} = \frac{1}{\sqrt{LC}}
$$

The current waves relate to voltage waves through $Z_0$:
$$
I_0^+ = \frac{V_0^+}{Z_0}, \qquad I_0^- = -\frac{V_0^-}{Z_0}
$$

### Reflection Coefficient and VSWR (§3.1, pp. 74–76)

For a line terminated in load impedance $Z_L$:
$$
\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0} = \frac{V_0^-}{V_0^+}
$$

**Properties:**
- $|\Gamma| \le 1$ for passive loads
- $\Gamma = 0$ when $Z_L = Z_0$ (matched load)
- $\Gamma = 1$ for open circuit ($Z_L \to \infty$)
- $\Gamma = -1$ for short circuit ($Z_L = 0$)

**Voltage Standing Wave Ratio (VSWR):**
$$
\text{VSWR} = S = \frac{|V|_{\text{max}}}{|V|_{\text{min}}} = \frac{1 + |\Gamma|}{1 - |\Gamma|}
$$

### Input Impedance of a Terminated Line (§3.1, p. 79, Eq. 3.22)

For a line of length $\ell$ terminated in $Z_L$:
$$
Z_{\text{in}} = Z_0 \frac{Z_L + Z_0 \tanh(\gamma \ell)}{Z_0 + Z_L \tanh(\gamma \ell)}
$$

For a **lossless line** ($\gamma = j\beta$):
$$
Z_{\text{in}} = Z_0 \frac{Z_L + j Z_0 \tan(\beta \ell)}{Z_0 + j Z_L \tan(\beta \ell)}
$$

**Special cases:**

| Termination | $Z_{\text{in}}$ |
|-------------|-----------------|
| Short circuit ($Z_L = 0$) | $Z_{\text{in}} = j Z_0 \tan(\beta \ell)$ |
| Open circuit ($Z_L = \infty$) | $Z_{\text{in}} = -j Z_0 \cot(\beta \ell)$ |
| Matched ($Z_L = Z_0$) | $Z_{\text{in}} = Z_0$ |

### Quarter-Wave Transformer (§3.1, pp. 82–84)

When $\ell = \lambda/4$ ($\beta\ell = \pi/2$):
$$
Z_{\text{in}} = \frac{Z_0^2}{Z_L}
$$

This impedance inversion property is used for impedance matching. A quarter-wave transformer with characteristic impedance $Z_{0T}$ can match a load $Z_L$ to a source impedance $Z_S$:
$$
Z_{0T} = \sqrt{Z_S Z_L}
$$

### Power Flow (§3.1, p. 81)

Time-average power on a lossless line:
$$
P_{\text{avg}} = \frac{1}{2} \frac{|V_0^+|^2}{Z_0} (1 - |\Gamma|^2)
$$

The first term is the incident power; $|\Gamma|^2$ is the power reflection coefficient.

### General Transmission Line Equation Summary

| Quantity | Expression |
|----------|-----------|
| Propagation constant | $\gamma = \alpha + j\beta = \sqrt{(R+j\omega L)(G+j\omega C)}$ |
| Characteristic impedance | $Z_0 = \sqrt{(R+j\omega L)/(G+j\omega C)}$ |
| Phase velocity (lossless) | $v_p = 1/\sqrt{LC}$ |
| Wavelength (lossless) | $\lambda = 2\pi/\beta = 2\pi/(\omega\sqrt{LC})$ |
| Reflection coefficient | $\Gamma = (Z_L - Z_0)/(Z_L + Z_0)$ |
| VSWR | $S = (1 + \|\Gamma\|)/(1 - \|\Gamma\|)$ |
| Input impedance | $Z_{\text{in}} = Z_0 (Z_L + Z_0 \tanh \gamma\ell)/(Z_0 + Z_L \tanh \gamma\ell)$ |

---

## §3.2 Coaxial Line (pp. 96–107)

### Geometry

A coaxial line consists of an inner conductor (radius $a$) and outer conductor (radius $b$), separated by a dielectric ($\epsilon_r$).

### TEM Mode Field Solution (§3.2, pp. 96–99)

The dominant mode is **TEM** (Transverse Electromagnetic): both $E$ and $H$ fields are transverse to the propagation direction $z$. The fields have the same structure as the static fields:

$$
E_r = \frac{V_0 e^{-\gamma z}}{r \ln(b/a)}, \qquad
H_\phi = \frac{I_0 e^{-\gamma z}}{2\pi r}
$$

**Characteristic impedance:**
$$
Z_0 = \frac{1}{2\pi} \sqrt{\frac{\mu}{\epsilon}} \ln\left(\frac{b}{a}\right) = \frac{60}{\sqrt{\epsilon_r}} \ln\left(\frac{b}{a}\right) \quad [\Omega]
$$

### Distributed Parameters (p. 99)

From the field solution:

$$
L = \frac{\mu}{2\pi} \ln\left(\frac{b}{a}\right) \quad [\text{H/m}], \qquad
C = \frac{2\pi\epsilon}{\ln(b/a)} \quad [\text{F/m}]
$$

**Check:** $Z_0 = \sqrt{L/C} = \frac{1}{2\pi}\sqrt{\mu/\epsilon} \ln(b/a)$ ✓

### Attenuation (§3.2, pp. 99–103)

Total attenuation constant:
$$
\alpha = \alpha_c + \alpha_d
$$

**Conductor attenuation** (Eq. 3.73, p. 101):
$$
\alpha_c = \frac{R_s}{2 Z_0} \left(\frac{1}{a} + \frac{1}{b}\right) \quad [\text{Np/m}]
$$

where $R_s = \sqrt{\pi f \mu_c / \sigma}$ is the surface resistivity of the conductor.

**Dielectric attenuation:**
$$
\alpha_d = \frac{\pi f \sqrt{\epsilon_r} \tan\delta}{c_0} \quad [\text{Np/m}]
$$

### Higher-Order Modes (§3.2, pp. 104–106)

The first higher-order mode is **TE$_{11}$** with cutoff frequency:
$$
f_c = \frac{c_0}{\pi \sqrt{\epsilon_r} (a + b)}
$$

To ensure TEM-only propagation, the operating frequency must remain below $f_c$.

### Coaxial Line Parameter Summary

| Parameter | Expression | Notes |
|-----------|-----------|-------|
| $Z_0$ | $\frac{60}{\sqrt{\epsilon_r}} \ln(b/a)$ | Standard: 50 Ω |
| $L$ | $\frac{\mu}{2\pi} \ln(b/a)$ | H/m |
| $C$ | $\frac{2\pi\epsilon}{\ln(b/a)}$ | F/m |
| $\alpha_c$ | $\frac{R_s}{2Z_0}\left(\frac{1}{a} + \frac{1}{b}\right)$ | Conductor loss |
| $\alpha_d$ | $\frac{\pi f \sqrt{\epsilon_r} \tan\delta}{c_0}$ | Dielectric loss |
| $f_{c,\text{TE}_{11}}$ | $\frac{c_0}{\pi\sqrt{\epsilon_r}(a+b)}$ | TE$_{11}$ cutoff |

---

## §3.3 Rectangular Waveguide (pp. 107–123)

### Geometry

Rectangular waveguide: width $a$ (x-direction), height $b$ (y-direction), propagation in $z$-direction. Convention: $a > b$.

### TEₘₙ Modes (§3.3, pp. 108–113)

**Field components** for TE$_{mn}$ ($E_z = 0$):

$$
H_z = H_0 \cos\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{-\gamma z}
$$

$$
E_x = \frac{j\omega\mu n\pi}{k_c^2 b} H_0 \cos\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right) e^{-\gamma z}
$$
$$
E_y = -\frac{j\omega\mu m\pi}{k_c^2 a} H_0 \sin\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{-\gamma z}
$$
$$
H_x = \frac{\gamma m\pi}{k_c^2 a} H_0 \sin\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{-\gamma z}
$$
$$
H_y = \frac{\gamma n\pi}{k_c^2 b} H_0 \cos\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right) e^{-\gamma z}
$$

**Cutoff wavenumber:**
$$
k_c = \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}
$$

**Cutoff frequency** (Eq. 3.111, p. 111):
$$
f_{c,mn} = \frac{c}{2\pi} k_c = \frac{c}{2} \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}
$$

### Dominant TE₁₀ Mode (§3.3, pp. 113–115)

The **TE$_{10}$** mode ($m = 1$, $n = 0$) has the lowest cutoff frequency (most widely used):

$$
f_{c,10} = \frac{c}{2a}
$$

**Fields for TE$_{10}$:**

$$
E_y = -\frac{j\omega\mu a}{\pi} H_0 \sin\left(\frac{\pi x}{a}\right) e^{-j\beta z}
$$
$$
H_x = \frac{j\beta a}{\pi} H_0 \sin\left(\frac{\pi x}{a}\right) e^{-j\beta z}
$$
$$
H_z = H_0 \cos\left(\frac{\pi x}{a}\right) e^{-j\beta z}
$$

### TMₘₙ Modes (§3.3, pp. 115–116)

**Field components** for TM$_{mn}$ ($H_z = 0$):

$$
E_z = E_0 \sin\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right) e^{-\gamma z}
$$

$$
E_x = -\frac{\gamma m\pi}{k_c^2 a} E_0 \cos\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right) e^{-\gamma z}
$$
$$
E_y = -\frac{\gamma n\pi}{k_c^2 b} E_0 \sin\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{-\gamma z}
$$
$$
H_x = \frac{j\omega\epsilon n\pi}{k_c^2 b} E_0 \sin\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{-\gamma z}
$$
$$
H_y = -\frac{j\omega\epsilon m\pi}{k_c^2 a} E_0 \cos\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right) e^{-\gamma z}
$$

Note: TM$_{m0}$ and TM$_{0n}$ modes do not exist (field vanishes if $m = 0$ or $n = 0$).

### Propagation Characteristics (§3.3, pp. 116–119)

**Above cutoff** ($f > f_c$):

Propagation constant: $\beta = \sqrt{k^2 - k_c^2}$ where $k = \omega\sqrt{\mu\epsilon}$

**Guide wavelength:**
$$
\lambda_g = \frac{2\pi}{\beta} = \frac{\lambda}{\sqrt{1 - (f_c/f)^2}} > \lambda
$$

**Phase velocity:**
$$
v_p = \frac{\omega}{\beta} = \frac{c}{\sqrt{1 - (f_c/f)^2}} > c
$$

**Group velocity:**
$$
v_g = \left(\frac{d\beta}{d\omega}\right)^{-1} = c \sqrt{1 - (f_c/f)^2} < c
$$

**Below cutoff** ($f < f_c$):

The mode is **evanescent**: $\gamma = \alpha$ (real), fields decay exponentially with no real power flow.

### Power Handling (§3.3, pp. 119–121)

**Power flow for TE$_{10}$** (Eq. 3.152, p. 121):
$$
P = \frac{ab}{4Z_{\text{TE}}} |E_0|^2 = \frac{ab}{4} \frac{\beta}{\omega\mu} |E_0|^2
$$

where $Z_{\text{TE}} = \omega\mu / \beta$ is the TE mode wave impedance.

**Maximum power** is limited by dielectric breakdown (typically $E_{\text{max}} \approx 3 \times 10^6$ V/m for air):
$$
P_{\text{max}} = \frac{ab}{4 Z_{\text{TE}}} |E_{\text{max}}|^2
$$

### Attenuation (§3.3, pp. 121–123)

**TE$_{10}$ conductor attenuation** (Eq. 3.162, p. 122):

For TE$_{10}$ in a rectangular waveguide with conducting walls:
$$
\alpha_c = \frac{2R_s}{b\eta\sqrt{1 - (f_c/f)^2}}
\left[ 1 + \frac{2b}{a}\left(\frac{f_c}{f}\right)^2 \right] \quad [\text{Np/m}]
$$

### Rectangular Waveguide Mode Summary

| Property | Value for TE$_{10}$ | General TE$_{mn}$ |
|----------|--------------------|--------------------|
| Cutoff $f_c$ | $c/(2a)$ | $\frac{c}{2}\sqrt{(m/a)^2+(n/b)^2}$ |
| $\beta$ | $\sqrt{k^2 - (\pi/a)^2}$ | $\sqrt{k^2 - k_c^2}$ |
| $Z_{\text{TE}}$ | $k\eta/\beta$ | $k\eta/\beta$ |
| $Z_{\text{TM}}$ | — | $\beta\eta/k$ |
| $\lambda_g$ | $\lambda/\sqrt{1-(f_c/f)^2}$ | same |
| $v_p$ | $c/\sqrt{1-(f_c/f)^2}$ | same |
| $v_g$ | $c\sqrt{1-(f_c/f)^2}$ | same |

---

## §3.4 Circular Waveguide (pp. 123–131)

### Geometry

Circular waveguide of radius $a$ (cylindrical coordinates $r$, $\phi$, $z$).

### TEₙₘ Modes (§3.4, pp. 124–127)

Solutions involve **Bessel functions** $J_n(x)$:

$$
H_z = H_0 J_n(k_c r) \cos(n\phi) e^{-j\beta z} \quad \text{or} \quad \sin(n\phi)
$$

**Cutoff condition:** $\partial J_n(k_c a)/\partial r = 0$, i.e., $J_n'(k_c a) = 0$

Let $p'_{nm}$ be the $m$-th root of $J_n'(x) = 0$. Then:
$$
k_c = \frac{p'_{nm}}{a}, \qquad
f_{c,nm} = \frac{c p'_{nm}}{2\pi a}
$$

**Field components** for TE$_{nm}$:

$$
E_r = -\frac{j\omega\mu n}{k_c^2 r} H_0 J_n(k_c r) \sin(n\phi) e^{-j\beta z}
$$
$$
E_\phi = -\frac{j\omega\mu}{k_c} H_0 J_n'(k_c r) \cos(n\phi) e^{-j\beta z}
$$
$$
H_r = -\frac{j\beta}{k_c} H_0 J_n'(k_c r) \cos(n\phi) e^{-j\beta z}
$$
$$
H_\phi = \frac{j\beta n}{k_c^2 r} H_0 J_n(k_c r) \sin(n\phi) e^{-j\beta z}
$$

### Dominant TE₁₁ Mode (§3.4, pp. 126–127)

The **TE$_{11}$** mode has the lowest cutoff ($p'_{11} = 1.841$):

$$
f_{c,11} = \frac{1.841 c}{2\pi a}
$$

This is the dominant mode in circular waveguide.

| $n$ | $p'_{n1}$ | $p'_{n2}$ | $p'_{n3}$ |
|-----|-----------|-----------|-----------|
| 0 | 3.832 | 7.016 | 10.173 |
| 1 | 1.841 | 5.331 | 8.536 |
| 2 | 3.054 | 6.706 | 9.969 |

### TMₙₘ Modes (§3.4, pp. 127–128)

**Cutoff condition:** $J_n(k_c a) = 0$

Let $p_{nm}$ be the $m$-th root of $J_n(x) = 0$. Then:
$$
k_c = \frac{p_{nm}}{a}, \qquad
f_{c,nm} = \frac{c p_{nm}}{2\pi a}
$$

**Field components** for TM$_{nm}$:

$$
E_z = E_0 J_n(k_c r) \cos(n\phi) e^{-j\beta z}
$$
$$
E_r = -\frac{j\beta}{k_c} E_0 J_n'(k_c r) \cos(n\phi) e^{-j\beta z}
$$
$$
E_\phi = \frac{j\beta n}{k_c^2 r} E_0 J_n(k_c r) \sin(n\phi) e^{-j\beta z}
$$
$$
H_r = -\frac{j\omega\epsilon n}{k_c^2 r} E_0 J_n(k_c r) \sin(n\phi) e^{-j\beta z}
$$
$$
H_\phi = -\frac{j\omega\epsilon}{k_c} E_0 J_n'(k_c r) \cos(n\phi) e^{-j\beta z}
$$

| $n$ | $p_{n1}$ | $p_{n2}$ | $p_{n3}$ |
|-----|---------|---------|---------|
| 0 | 2.405 | 5.520 | 8.654 |
| 1 | 3.832 | 7.016 | 10.173 |
| 2 | 5.136 | 8.417 | 11.620 |

### Mode Chart (Fig. 3.19, p. 129)

The mode chart for circular waveguide shows the relative cutoff frequencies of TE$_{nm}$ and TM$_{nm}$ modes, with TE$_{11}$ as the lowest:

| Mode | $f_c / f_{c,\text{TE}_{11}}$ |
|------|------------------------------|
| TE$_{11}$ | 1.000 |
| TM$_{01}$ | 1.306 |
| TE$_{21}$ | 1.659 |
| TE$_{01}$, TM$_{11}$ | 2.081 |

---

## §3.5 Stripline (pp. 131–134)

### Geometry

A conducting strip of width $w$ centered between two parallel ground planes separated by distance $b$, filled with dielectric $\epsilon_r$.

### TEM Mode Propagation (§3.5, pp. 131–133)

Stripline supports a **TEM mode** (approximately). The characteristic impedance can be computed from the capacitance per unit length:

$$
Z_0 = \frac{\sqrt{\epsilon_r}}{c C}
$$

**Approximate formula** (for $w/b > 0.35$):

$$
Z_0 = \frac{30}{\sqrt{\epsilon_r}} \ln\left[ 1 + \frac{4}{\pi} \frac{w/b}{(1 + 1/\pi \ln(1 + \cot^2[\pi w/(2b)]))} \right]
$$

**Simplified formula** (Wheeler, often used):
$$
Z_0 = \frac{30}{\sqrt{\epsilon_r}} \ln\left(1 + \frac{4}{\pi} \frac{w/b}{t/b + 1}\right)
$$

where $t$ is the strip thickness.

---

## §3.6 Microstrip (pp. 134–137)

### Geometry

A conducting strip of width $w$ on top of a dielectric substrate of thickness $h$ with relative permittivity $\epsilon_r$, with a ground plane on the bottom.

### Quasi-TEM Mode (§3.6, pp. 134–135)

Microstrip does **not** support a pure TEM mode because the field exists partly in the dielectric ($\epsilon_r$) and partly in air ($\epsilon_0$). The dominant mode is **quasi-TEM**, characterized by an **effective dielectric constant**:

$$
\epsilon_{\text{eff}} = \frac{\epsilon_r + 1}{2} + \frac{\epsilon_r - 1}{2} \frac{1}{\sqrt{1 + 12h/w}}
$$

### Characteristic Impedance (§3.6, pp. 135–137)

**For $w/h \le 1$** (narrow strip):
$$
Z_0 = \frac{60}{\sqrt{\epsilon_{\text{eff}}}} \ln\left(\frac{8h}{w} + \frac{w}{4h}\right)
$$

**For $w/h \ge 1$** (wide strip):
$$
Z_0 = \frac{120\pi}{\sqrt{\epsilon_{\text{eff}}}} \frac{1}{w/h + 1.393 + 0.667 \ln(w/h + 1.444)}
$$

### Key Properties

- **Dispersion:** $\epsilon_{\text{eff}}$ increases with frequency (more field confined in substrate)
- **Surface waves:** Can be excited at high frequencies, causing radiation loss
- **Conductor and dielectric losses:** Determine total attenuation
- **Widely used** in MICs (Microwave Integrated Circuits) and MMICs

---

## §3.7 Dielectric Waveguide (pp. 137–139)

### Geometry

A dielectric rod of permittivity $\epsilon_1$ surrounded by a different dielectric (typically air, $\epsilon_0$). Propagation occurs by total internal reflection.

### Modes

Dielectric waveguides support **hybrid modes** (both $E_z$ and $H_z$ non-zero):
- **HE$_{nm}$ modes:** $H_z$ dominant
- **EH$_{nm}$ modes:** $E_z$ dominant

The dominant mode is **HE$_{11}$**, which has no cutoff frequency (unlike metallic waveguides).

### Optical Fiber Connection (§3.7, p. 139)

Dielectric waveguide theory is the foundation for **optical fiber** analysis. The step-index fiber is a cylindrical dielectric waveguide.

---

## §3.8 Finline (pp. 139–140)

### Geometry

A finline consists of a dielectric substrate with a conducting **fin** pattern, placed inside a rectangular waveguide housing. It combines the low-loss characteristics of waveguide with the planar fabrication advantages of microstrip.

### Modes

Finline supports quasi-TE$_{10}$ modes with field concentrated in the fin gap region. Common configurations:
- **Unilateral finline:** Fin on one side of substrate
- **Bilateral finline:** Fins on both sides
- **Antipodal finline:** Fins on opposite sides

### Applications

- Millimeter-wave circuits (30–300 GHz)
- Mixers, detectors, and oscillators
- Where microstrip losses become unacceptable

---

## Summary of Transmission Line Types

| Type | Mode | $Z_0$ Range | Bandwidth | Loss | Integration |
|------|------|-------------|-----------|------|-------------|
| Coaxial | TEM | 10–100 Ω | DC–mm-wave | Low | Moderate |
| Stripline | TEM | 20–150 Ω | DC–mm-wave | Medium | Good |
| Microstrip | Quasi-TEM | 10–150 Ω | DC–~100 GHz | Medium | Excellent |
| Rectangular WG | TE$_{10}$ | — | $f > f_c$ | Low | Poor |
| Circular WG | TE$_{11}$ | — | $f > f_c$ | Low | Poor |
| Dielectric WG | Hybrid | — | All frequencies | Very low | Poor |
| Finline | Quasi-TE$_{10}$ | — | mm-wave | Low | Fair |

---

## Key Equations (Ch. 3)

| Quantity | Expression | § Ref |
|----------|-----------|-------|
| Propagation constant | $\gamma = \sqrt{(R+j\omega L)(G+j\omega C)}$ | §3.1 |
| Characteristic impedance | $Z_0 = \sqrt{(R+j\omega L)/(G+j\omega C)}$ | §3.1 |
| Reflection coefficient | $\Gamma = (Z_L - Z_0)/(Z_L + Z_0)$ | §3.1 |
| Input impedance | $Z_{\text{in}} = Z_0 \frac{Z_L + Z_0 \tanh(\gamma\ell)}{Z_0 + Z_L \tanh(\gamma\ell)}$ | §3.1 |
| Coax $Z_0$ | $Z_0 = \frac{60}{\sqrt{\epsilon_r}} \ln(b/a)$ | §3.2 |
| Coax $\alpha_c$ | $\alpha_c = \frac{R_s}{2Z_0}(1/a + 1/b)$ | §3.2 |
| WG cutoff $f_c$ | $f_c = \frac{c}{2}\sqrt{(m/a)^2+(n/b)^2}$ | §3.3 |
| Guide wavelength | $\lambda_g = \lambda/\sqrt{1-(f_c/f)^2}$ | §3.3 |
| WG TE$_{10}$ $\alpha_c$ | $\alpha_c = \frac{2R_s}{b\eta\sqrt{1-(f_c/f)^2}}\left[1 + \frac{2b}{a}(f_c/f)^2\right]$ | §3.3 |
| Circular WG $f_{c,\text{TE}_{11}}$ | $f_c = 1.841c/(2\pi a)$ | §3.4 |
| Microstrip $\epsilon_{\text{eff}}$ | $\epsilon_{\text{eff}} = \frac{\epsilon_r+1}{2} + \frac{\epsilon_r-1}{2}\frac{1}{\sqrt{1+12h/w}}$ | §3.6 |

---

**End of Ch. 3 notes.** Source: Collin, *Foundations for Microwave Engineering*, 2nd Ed., IEEE Press, 2000, pp. 71–140.
