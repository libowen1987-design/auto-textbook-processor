# 程守洙《普通物理学》电磁学部分 第9章：光的电磁理论

> **来源：** 谢处方等，《电磁场与电磁波》，第9章
> **提取方式：** 📷 扫描PDF → OCR → 人工清洗

---

## 9.1 光的电磁理论 | Electromagnetic Theory of Light

# David K. Cheng《Field and Wave Electromagnetics》2nd Ed Chapter 9
 本笔记基于  文本清洗整理100% 来源于原书内容
## Chapter 9 — Theory and Applications of Transmission Lines
### 9-1. Introduction
**Transmission lines** are guiding structures that transmit electromagnetic power from one point to another. They are characterized by distributed parameters: series inductance $L'$ ($\mathbf{H}$/m), shunt capacitance $C'$ ($\mathbf{F}$/m), series resistance $R'$ ($\Omega$/m), and shunt conductance $G'$ ($\mathbf{S}$/m).
### 9-2. Transverse Electromagnetic Wave along a Parallel-Plate Transmission Line
For a parallel-plate transmission line (plate width $w$, separation $d$, dielectric $\varepsilon$):
$$L' = \frac{\mu_0 d}{w} \quad \text{($\mathbf{H}$/m)}$$
$$C' = \frac{\varepsilon_0 \varepsilon_r w}{d} \quad \text{($\mathbf{F}$/m)}$$
The characteristic impedance:
$$Z_0 = \sqrt{\frac{L'}{C'}} = \frac{d}{w}\sqrt{\frac{\mu_0}{\varepsilon_0 \varepsilon_r}} = \frac{d}{w}\frac{\eta_0}{\sqrt{\varepsilon_r}}$$
Phase velocity: $u = 1/\sqrt{L'C'} = c/\sqrt{\varepsilon_r}$
### 9-3. General Transmission-Line Equations
For a transmission line with distributed parameters per unit length ($R', L', G', C'$), the **telegrapher's equations**:
$$\frac{\partial V}{\partial z} = -R'I - L'\frac{\partial I}{\partial t}$$
$$\frac{\partial I}{\partial z} = -G'V - C'\frac{\partial V}{\partial t}$$
For **lossless lines** ($R' = G' = 0$) and sinusoidal steady state:
$$\frac{d^2 V}{dz^2} + $\beta$^2 V = 0, \quad \beta = $\omega$\sqrt{L'C'}$$
**General solution** (forward + backward traveling waves):
$$V(z) = V^+ e^{-j\beta z} + V^- e^{j\beta z}$$
**Propagation constant** for lossy lines:
$$\gamma = \sqrt{(R' + j\omega L')(G' + j\omega C')} = \alpha + j\beta$$
**Characteristic impedance:**
$$Z_0 = \sqrt{\frac{R' + j\omega L'}{G' + j\omega C'}} = \sqrt{\frac{L'}{C'}}\frac{1}{\sqrt{1 - j\frac{R'}{\omega L'}}\sqrt{1 - j\frac{G'}{\omega C'}}}$$
For **lossless line:** $Z_0 = \sqrt{L'/C'}$
### 9-3.1. Wave Characteristics on an Infinite Transmission Line
On an infinite (or matched) transmission line, only the forward-traveling wave exists:
$$V(z) = V^+ e^{-j\beta z}$$
$$I(z) = \frac{V^+}{Z_0} e^{-j\beta z}$$
The **phase velocity:** $u_p = $\omega$/\beta = 1/\sqrt{L'C'}$
The **wavelength:** $\lambda = 2$\pi$/\beta = u_p/f$
### 9-4. Wave Characteristics on Finite Transmission Lines
**Input impedance** at a distance $z$ from the load:
$$Z_{\text{in}}(z) = Z_0 \frac{Z_L + jZ_0\tan(\beta z)}{Z_0 + jZ_L\tan(\beta z)}$$
**Special cases:**
| Load Condition | Input Impedance |
|---|---|
| $Z_L = 0$ (short circuit) | $Z_{\text{in}} = jZ_0 \tan(\beta z)$ |
| $Z_L = \infty$ (open circuit) | $Z_{\text{in}} = -jZ_0 \cot(\beta z)$ |
| $Z_L = Z_0$ (matched) | $Z_{\text{in}} = Z_0$ (no reflection) |
### 9-4.1. Transmission Lines as Circuit Elements
For **electrically short lines** ($\beta z \ll 1$, i.e., $z \ll $\lambda$/2\pi$):
$$Z_{\text{open}} \approx \frac{1}{j\omega C' z}, \quad Z_{\text{short}} \approx j\omega L' z$$
This gives the equivalent circuit approximations.
### 9-5. The Smith Chart
The **Smith chart** is a graphical representation of the complex reflection coefficient and impedance. It is an essential tool for transmission-line calculations and impedance matching.
Key relationships:
$$\Gamma = \frac{Z_L - Z_0}{Z_L + Z_0} = |\Gamma|e^{j\phi}$$
$$\text{SWR} = \frac{1+|\Gamma|}{1-|\Gamma|}$$
The Smith chart maps $Z/Z_0$ to $\Gamma$ on a unit circle. The center corresponds to $Z = Z_0$ (matched). The real and imaginary axes are circles.
**Using the Smith chart:**
- Given $Z_L$ and $Z_0$, find $\Gamma$ and SWR
- Find points of $V_{\max}$ and $V_{\min}$ on the line
- Perform impedance matching transformations
### 9-6. Transmission-Line Impedance Matching
**Quarter-wave transformer:**
For a lossless line of length $$\lambda$/4$ connected between $Z_0$ and $Z_L$:
$$Z_{\text{in}} = \frac{Z_0^2}{Z_L}$$
To match: choose $Z_0 = \sqrt{Z_0 Z_L}$ for the transformer characteristic impedance.
**Single-stub matching:**
Use a shorted or open stub of length $d_s$ at a distance $d$ from the load to cancel the reactive part of the input admittance.
**Double-stub matching:**
Two stubs at fixed positions, with adjustable lengths, provide more flexibility for matching arbitrary loads.
### Review Questions (Chapter 9)
1. What are the telegrapher's equations? Derive the wave equation for a lossless transmission line.
2. Define characteristic impedance, propagation constant, phase velocity.
3. What is the input impedance of a short-circuited and open-circuited transmission line?
4. Explain the Smith chart and its applications.
5. Describe the quarter-wave transformer impedance matching technique.
6. What is the difference between single-stub and double-stub matching?
---