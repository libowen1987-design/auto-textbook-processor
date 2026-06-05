---
title: "Chapter 11 — Appendices: Physical Foundations & CAD Tools"
book: "RF Circuit Design — 2nd Ed."
author: "Reinhold Ludwig, Gene Bogdanov"
pages: "607–656"
processed: "2026-05-07"
tags: [physical-constants, skin-effect, smith-chart, matrix-conversions, semiconductor-parameters, diode-models, couplers, wilkinson, branch-line, lange-coupler, noise-analysis, matlab, cad, oscillators, mixers]
---

# Chapter 11: Appendices | 第11章：附录

> **Note to Reader:** This "Chapter 11" corresponds to pages 607–656 of the Ludwig 2nd Ed. textbook, which consists of **Appendices A through I** — the supporting technical reference material that underlies all RF circuit design. The chapter problems from Chapter 10 (Oscillators and Mixers) appear at the top of the file and are reviewed first, followed by the appendices. All content is drawn exclusively from the textbook.

---

## §11.1 Chapter 10 Problems — Oscillators and Mixers | 第10章习题——振荡器与混频器

### §11.1.1 Colpitts Oscillator Design | Colpitts振荡器设计（习题10.8）

**Given:** $f_0 = 250\ \text{MHz}$, $V_{CE} = 2.7\ \text{V}$, $I_c = 2\ \text{mA}$, $C_{BC} = 0.2\ \text{fF}$, $r_{BE} = 3\ \text{k}\Omega$, $r_{CE} = 12\ \text{k}\Omega$, $C_{BE} = 80\ \text{fF}$, $L = 47\ \text{nH}$.

**Find:** Feedback loop capacitances $C_1$ and $C_2$, and validity of DC $h$-parameters.

The small-signal $\pi$-model of the BJT at the bias point gives us the transconductance:

$$
g_m = \frac{I_C}{V_T} = \frac{2\ \text{mA}}{26\ \text{mV}} \approx 77\ \text{mS}
$$

The standard Colpitts loop gain condition (Barkhausen) requires the loop reactance to vanish. The effective capacitance seen by the inductor is the series combination:

$$
C_{\Sigma} = \frac{C_1 C_2}{C_1 + C_2}
$$

The oscillation frequency is:

$$
\omega_0 = \frac{1}{\sqrt{L\,C_{\Sigma}}}
\quad\Longrightarrow\quad
C_{\Sigma} = \frac{1}{\omega_0^2 L}
= \frac{1}{(2\pi \times 250\ \text{MHz})^2 \times 47\ \text{nH}}
\approx 8.65\ \text{pF}
$$

The feedback ratio is set by $C_1/C_2$ and must satisfy the loop gain condition:

$$
\frac{C_1}{C_2} = \frac{r_{BE}}{r_{CE}} \cdot \frac{1}{g_m\, r_{BE} + 1} \approx \frac{3\ \text{k}\Omega}{12\ \text{k}\Omega} = 0.25
$$

Solving simultaneously with $C_{\Sigma} = C_1 C_2 / (C_1 + C_2) = 8.65\ \text{pF}$ yields $C_1 \approx 34.6\ \text{pF}$ and $C_2 \approx 11.5\ \text{pF}$.

**DC $h$-Parameter Validity:** At $f_0 = 250\ \text{MHz}$, the device $f_T \approx g_m/(2\pi C_{\pi})$ is only marginally above the operating frequency. The hybrid-$\pi$ model parameters ($r_{BE}$, $C_{BE}$, $C_{BC}$) deviate significantly from DC extractions due to:
- Transit-time effects at UHF
- Distributed base-collector capacitance (non-quasi-static)
- Bias-dependent $g_m$ variation with signal amplitude

**Engineering Intuition:** DC $h$-parameters are **not** appropriate for oscillator design at 250 MHz. Small-signal S-parameters measured at the actual frequency and bias are mandatory. A VNA characterization at $V_{CE}=2.7$ V, $I_c=2$ mA should replace the DC-extracted values.

---

### §11.1.2 Quartz Crystal Resonator | 石英晶体谐振器——串联与并联谐振（习题10.9）

The quartz crystal is modeled by the **Borkhausen** equivalent circuit (Fig. 10-7):

$$
Z_s(\omega) = j\omega L_q \parallel \left(\frac{1}{j\omega C_q} + R_q\right) + \frac{1}{j\omega C_p}
$$

where $L_q$ = motional inductance, $C_q$ = motional capacitance, $R_q$ = motional resistance, $C_p$ = shunt (package) capacitance.

**Series resonance** occurs when the motional branch resonates:

$$
\omega_s = \frac{1}{\sqrt{L_q C_q}}
$$

At $\omega_s$, the impedance is purely resistive $Z_s(\omega_s) = R_q$.

**Parallel resonance** occurs when the motional reactance cancels the shunt capacitance:

$$
\omega_p = \omega_s \sqrt{1 + \frac{C_q}{C_p}} \approx \omega_s\left(1 + \frac{C_q}{2C_p}\right)
$$

The **Taylor series expansion** confirms this. For $C_q \ll C_p$, write:

$$
\omega_p^2 = \frac{1}{L_q}\left(\frac{1}{C_q} + \frac{1}{C_p}\right)
= \omega_s^2\left(1 + \frac{C_q}{C_p}\right)
$$

Using $\sqrt{1+\epsilon} \approx 1 + \frac{\epsilon}{2} - \frac{\epsilon^2}{8} + \cdots$ with $\epsilon = C_q/C_p$:

$$
\omega_p \approx \omega_s\left(1 + \frac{C_q}{2C_p}\right)
$$

**Example calculation:** $R_q = 50\ \Omega$, $L_q = 50\ \text{mH}$, $C_q = 0.4\ \text{pF}$, $C_p = 0.8\ \text{pF}$

$$
f_s = \frac{1}{2\pi\sqrt{L_q C_q}}
= \frac{1}{2\pi\sqrt{50\ \text{mH} \times 0.4\ \text{pF}}}
\approx 1.126\ \text{MHz}
$$

$$
f_p = f_s\sqrt{1 + \frac{C_q}{C_p}}
= 1.126\ \text{MHz} \times \sqrt{1 + \frac{0.4}{0.8}}
\approx 1.59\ \text{MHz}
$$

**Engineering Intuition:** The fractional separation $\frac{f_p - f_s}{f_s} = \frac{C_q}{2C_p} \approx 25\%$ for this device — a wide separation indicating a high-$Q$ resonator. In practice, adding an external inductor in parallel with the crystal lowers the effective parallel resonance frequency (since $L_{\text{ext}}$ counteracts $C_p$), causing the oscillator to shift **downward** in frequency. Conversely, adding a series inductor between crystal and load raises the series resonance contribution.

---

### §11.1.3 CE→CB S-Parameter Conversion | CE→CB S参数转换（习题10.10）

S-parameters are measured in CE (common-emitter) configuration but oscillator design often requires CB (common-base). The conversion path is:

$$
\mathbf{S}^{\text{CE}} \xrightarrow{\text{S→Y}} \mathbf{Y}^{\text{CE}} \xrightarrow{\text{CE→CB}} \mathbf{Y}^{\text{CB}} \xrightarrow{\text{Y→S}} \mathbf{S}^{\text{CB}}
$$

**CE → CB Y-parameter transformation:**

For a 3-port Y-matrix with node 1=emitter, 2=base, 3=collector, the CB configuration shares the base node as common. The transformation follows from Y-parameter additivity:

$$
Y_{11}^{\text{CB}} = Y_{11}^{\text{CE}} + Y_{12}^{\text{CE}}, \qquad
Y_{12}^{\text{CB}} = -(Y_{12}^{\text{CE}} + Y_{22}^{\text{CE}})
$$

$$
Y_{21}^{\text{CB}} = -(Y_{21}^{\text{CE}} + Y_{11}^{\text{CE}}), \qquad
Y_{22}^{\text{CB}} = Y_{22}^{\text{CE}} + Y_{21}^{\text{CE}}
$$

**Derivation sketch:** The CB input (emitter) sees the emitter as the reference node. Re-referencing the Y-parameters from CE (emitter common) to CB (base common) requires subtracting out the common-node admittance terms, which appear as $Y_{12}$ and $Y_{21}$ in the CE representation.

**Engineering Intuition:** The CE→CB conversion is **not** simply a matrix transpose. The CB configuration has different port definitions, so the Y-matrix elements transform as above. After conversion, the CB $S_{11}$ typically becomes more stable (closer to the unit circle edge) because the common-base configuration naturally suppresses the feedback effect.

---

### §11.1.4 S-Parameter Oscillator Design | S参数振荡器设计——负阻等价（习题10.11）

The two fundamental oscillator design conditions are:

1. **Unconditional stability parameter:** $k < 1$ (device is potentially unstable)
2. **Loop gain magnitude:** $\Gamma_{\text{in}}\Gamma_L = 1$ and $\Gamma_{\text{out}}\Gamma_S = 1$

Let $Z_{\text{in}} = R_{\text{in}} + jX_{\text{in}}$, $Z_S = R_S + jX_S$, $Z_L = R_L + jX_L$, $Z_{\text{out}} = R_{\text{out}} + jX_{\text{out}}$

From $\Gamma_{\text{in}} = (Z_{\text{in}} - Z_0)/(Z_{\text{in}} + Z_0)$ and the condition $\Gamma_{\text{in}}\Gamma_L = 1$:

$$
\frac{Z_{\text{in}} - Z_0}{Z_{\text{in}} + Z_0} \cdot \frac{Z_L - Z_0}{Z_L + Z_0} = 1
$$

Expanding and equating real and imaginary parts:

$$
R_{\text{in}} = -R_S, \quad X_{\text{in}} = -X_S
$$
$$
R_{\text{out}} = -R_L, \quad X_{\text{out}} = -X_L
$$

**This proves** that the S-parameter oscillator condition $\Gamma_{\text{in}}\Gamma_L = 1$ is mathematically **identical** to the negative-resistance condition: the oscillator requires the input impedance to present the **negative of the source resistance** to sustain oscillation.

**Engineering Intuition:** When the base is driven with a positive feedback inductance to maximize instability (Problem 10.12), the negative resistance magnitude $|R_{\text{in}}|$ increases, making oscillation easier to start. The optimal base inductance satisfies $j\omega L_{\text{base}} = -jX_{11}^{\text{CB}}$ at the oscillation frequency.

---

## §11.2 Appendix A — Physical Quantities and Units | 附录A——物理量与单位

### §11.2.1 Fundamental Physical Constants | 基本物理常数

| Constant | Symbol | Value | Unit |
|---|---|---|---|
| Vacuum permittivity | $\varepsilon_0$ | $8.85418 \times 10^{-12}$ | F/m |
| Vacuum permeability | $\mu_0$ | $4\pi \times 10^{-7}$ | H/m |
| Speed of light | $c$ | $2.99792 \times 10^8$ | m/s |
| Boltzmann's constant | $k_B$ | $1.38066 \times 10^{-23}$ | J/K |
| Electron charge | $e$ | $1.60218 \times 10^{-19}$ | C |
| Electron rest mass | $m_0$ | $0.91095 \times 10^{-30}$ | kg |

The intrinsic impedance of free space is:

$$
\eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} = 376.73\ \Omega \approx 377\ \Omega
$$

### §11.2.2 SI Unit Prefixes | SI单位前缀

From femto ($10^{-15}$) to giga ($10^9$): f, p, n, μ, m, k, M, G. The **mil** (non-SI) equals $10^{-3}$ inch = $25.4\ \mu\text{m}$.

### §11.2.3 Loss Tangent for RF Dielectrics | 射频介质损耗角正切

The loss angle $\tan\delta$ determines dielectric loss. Key values at RF/microwave frequencies:

| Material | $\tan\delta$ @ 1 GHz |
|---|---|
| Teflon | $\approx 2 \times 10^{-4}$ |
| Polyethylene | $\approx 3 \times 10^{-4}$ |
| Silicon dioxide | $\approx 10^{-3}$ |
| Alumina ($Al_2O_3$) | $\approx 10^{-4}$–$10^{-3}$ |
| Water (distilled) | $\approx 0.05$–$0.16$ |

The quality factor of a dielectric resonator is $Q_d = 1/\tan\delta$. Teflon and polyethylene are excellent low-loss dielectrics for RF boards; **water is never used** in resonant structures due to its enormous loss.

**Engineering Intuition:** For a dielectric substrate at 10 GHz, $\tan\delta = 10^{-4}$ gives $Q_d = 10{,}000$ — excellent. But water at the same frequency has $\tan\delta \approx 0.6$, yielding $Q_d \approx 1.67$, making it behave almost like a conductor at microwave frequencies.

---

## §11.3 Appendix B — Skin Equation | 附录B——圆柱导体集肤方程

### §11.3.1 Maxwell's Equations in Cylindrical Form | 圆柱坐标麦克斯韦方程

For a cylindrical conductor (radius $a$, axis along $z$) with only $E_z$ and $H_\phi$ components:

From Ampere's law (neglecting displacement current inside conductor):

$$
\frac{\partial H_\phi}{\partial r + \frac{H_\phi}{r}} = -j\omega\mu_0 H_\phi = \sigma E_z \quad \text{(B.1)}
$$

From Faraday's law:

$$
j\omega\mu_0 H_\phi = \frac{\partial E_z}{\partial r} \quad \text{(B.2)}
$$

Combining to eliminate $H_\phi$ yields the **Bessel equation**:

$$
\frac{\partial^2 E_z}{\partial r^2} + \frac{1}{r}\frac{\partial E_z}{\partial r} + \gamma^2 E_z = 0
$$

where the **propagation constant in the conductor** is:

$$
\gamma = \sqrt{j\omega\mu_0(\sigma + j\omega\varepsilon_0)} \approx \sqrt{j\omega\mu_0\sigma}
\quad (\text{since }\sigma \gg \omega\varepsilon_0 \text{ at RF})
$$

The **skin depth** $\delta_s = \sqrt{2/(\omega\mu_0\sigma)}$ emerges from this. The solution is:

$$
E_z(r) = -j\frac{I\,\gamma}{2\pi a\sigma}\cdot\frac{J_0(\gamma r)}{J_1(\gamma a)} \quad \text{(B.8)}
$$

where $J_0$ and $J_1$ are Bessel functions of the first kind.

### §11.3.2 Low-Frequency Limit (DC) | 低频极限（直流）

For $\omega \to 0$, using $J_0(x) \to 1$, $J_1(x) \to x/2$ as $x \to 0$:

$$
E_z \to \frac{I}{\pi a^2 \sigma} \quad \Rightarrow \quad J_z = \frac{I}{\pi a^2}
$$

This recovers **Ohm's law for uniform current density** — the DC limit is consistent.

**Engineering Intuition:** At DC, current distributes uniformly across the wire cross-section. At RF, the current crowds to the surface with exponential decay $e^{-r/\delta_s}$. The **effective conducting area** shrinks to $\pi a \delta_s$ (for thin skin depth), so AC resistance is $R_{\text{AC}} = R_{\text{DC}} \cdot (a / \delta_s)$, growing as $\sqrt{f}$ due to the $1/\sqrt{f}$ dependence of $\delta_s$.

---

## §11.4 Appendix C — Complex Numbers | 附录C——复数

### §11.4.1 Smith Chart — The Circle Equation | 史密斯圆图——圆方程

The foundation of the Smith Chart is the **normalized impedance circle equation**:

$$
|z - w| = r \quad \Longleftrightarrow\quad (x - u)^2 + (y - v)^2 = r^2 \quad \text{(C.3)}
$$

where $z = x + jy$ and $w = u + jv$ is the circle center.

For the Smith Chart, the complex reflection coefficient plane $\Gamma$ has:
- Center at origin ($w = 0$)
- Unit circle ($|\Gamma| = 1$, radius $r = 1$)
- Real axis maps to points on the horizontal diameter

The bilinear transform $z = (1+\Gamma)/(1-\Gamma)$ maps the $|\Gamma| \leq 1$ unit disk to the right half of the $z$-plane ($\text{Re}(z) \geq 0$), thereby converting the $\Gamma$-circle equation into impedance circles in the $z$-plane.

### §11.4.2 Key Complex Number Identities | 关键复数恒等式

**Magnitude-squared:**
$$
|z|^2 = z \cdot z^* = x^2 + y^2
$$

**Product with conjugate:**
$$
|z + w|^2 = |z|^2 + |w|^2 + 2\,\text{Re}\{z\,w^*\} \quad \text{(C.4)}
$$

**Engineering Intuition:** The Smith Chart elegantly solves transmission line problems where impedance calculations involve $z \pm w^*$ conjugates — the circle geometry lets engineers find solutions graphically without solving complex polynomial equations. Every rotation by $\lambda/8$ on the Smith Chart is a $\pi/4$ rotation in the $\Gamma$-plane.

---

## §11.5 Appendix D — Matrix Conversions | 附录D——矩阵转换

### §11.5.1 S ↔ Z, Y, h, ABCD Conversion Formulas | S↔Z, Y, h, ABCD转换公式

**Y → Z conversion:**
$$
Z_{11} = \frac{Y_{22}}{|Y|},\quad
Z_{12} = \frac{-Y_{12}}{|Y|},\quad
Z_{21} = \frac{-Y_{21}}{|Y|},\quad
Z_{22} = \frac{Y_{11}}{|Y|}
$$
where $|Y| = Y_{11}Y_{22} - Y_{12}Y_{21}$.

**S → Y conversion:**
$$
Y_{11} = \frac{(1-S_{11})(1+S_{22}) - S_{12}S_{21}}{D_S}
$$
$$
Y_{12} = \frac{-2S_{12}}{D_S},\quad
Y_{21} = \frac{-2S_{21}}{D_S}
$$
where $D_S = (1+S_{11})(1+S_{22}) - S_{12}S_{21}$.

**S → h (hybrid) conversion:**
$$
h_{11} = \frac{D_S}{(1-S_{11})(1+S_{22}) + S_{12}S_{21}},\quad
h_{12} = \frac{2S_{12}}{(1+S_{11})(1+S_{22}) - S_{12}S_{21}}
$$

**ABCD → S conversion (for reference impedance $Z_0$):**
$$
S_{11} = \frac{A + B/Z_0 - C Z_0 - D}{\Delta},\quad
S_{12} = \frac{2(A D - B C)}{\Delta}
$$
$$
S_{21} = \frac{2}{\Delta},\quad
S_{22} = \frac{-A + B/Z_0 - C Z_0 + D}{\Delta}
$$
where $\Delta = A + B/Z_0 + C Z_0 + D$.

**Engineering Intuition:** Matrix conversion is the **language of RF design**. You measure S-parameters (VNA), convert to Y for parallel admittance addition (matching networks), convert to ABCD for cascading transmission lines, and convert back to S for final port behavior. Always use $Z_0 = 50\ \Omega$ consistently in all conversions.

---

## §11.6 Appendix E — Semiconductor Parameters | 附录E——半导体参数

### §11.6.1 Key Material Properties at 300 K | 300K主要材料特性

| Property | Ge | Si | GaAs |
|---|---|---|---|
| Bandgap $E_g$ | 0.66 eV | 1.12 eV | 1.42 eV |
| Electron mobility $\mu_n$ | 3900 cm²/V·s | 1350 cm²/V·s | 8500 cm²/V·s |
| Hole mobility $\mu_p$ | 1900 cm²/V·s | 480 cm²/V·s | 400 cm²/V·s |
| Intrinsic carrier $n_i$ | $2.4 \times 10^{13}$ cm⁻³ | $1.5 \times 10^{10}$ cm⁻³ | $1.8 \times 10^6$ cm⁻³ |
| Intrinsic resistivity $\rho_i$ | 47 Ω·cm | $2.3 \times 10^5$ Ω·cm | $10^8$ Ω·cm |

**GaAs vs Si:**
- GaAs has $\sim 6\times$ higher electron mobility → lower series resistance at microwave frequencies
- GaAs has much wider bandgap → higher $V_{DD}$ operation (up to 15 V vs 5 V for Si)
- GaAs is semi-insulating substrate → lower parasitic capacitances
- Si is cheaper, better thermal conductivity, easier to integrate

**Engineering Intuition:** For oscillators above 5 GHz, GaAs MESFETs dominate because of their high mobility and semi-insulating substrate. For power oscillators below 2 GHz, Si BJT is more economical and has better thermal management.

---

## §11.7 Appendix F — Diode Models | 附录F——长二极管与短二极管模型

### §11.7.1 Excess Carrier Concentration | 过剩载流子浓度

Under forward bias $V_A$, the excess minority carrier concentrations at the junction edges are:

$$
\Delta p_{n0} = p_{n0}\left(e^{V_A/V_T} - 1\right),\quad
\Delta n_{p0} = n_{p0}\left(e^{V_A/V_T} - 1\right)
$$

where $V_T = k_B T/q \approx 26\ \text{mV}$ at 300 K.

### §11.7.2 Diffusion Length | 扩散长度

$$
L_p = \sqrt{D_p \tau_p},\quad L_n = \sqrt{D_n \tau_n}
$$

where $D = \mu \cdot V_T$ (Einstein relation), and $\tau$ is the minority carrier lifetime.

### §11.7.3 Long Diode vs Short Diode | 长二极管与短二极管

The key parameter is the ratio of semiconductor layer width $W$ to diffusion length $L$:

**Long diode ($W_p \gg L_p$):** Minority carriers recombine completely before reaching the far contact. The current follows the ideal Shockley diode equation:

$$
I = I_S\left(e^{V_A/V_T} - 1\right),\quad I_S = \frac{q A D_p p_{n0}}{L_p}
$$

**Short diode ($W_p \ll L_p$):** Carriers reach the far contact before significant recombination. The current is linear in $W$ (not exponential in $L$):

$$
I = I_S^{\text{short}}\left(e^{V_A/V_T} - 1\right),\quad I_S^{\text{short}} = \frac{q A D_p p_{n0}}{W_p}
$$

**Engineering Intuition:** In a short diode, the saturation current $I_S^{\text{short}} \propto 1/W_p$ — making the diode **less ideal** (larger $I_S$) than a long diode of the same material. This is why ** Schottky barrier diodes** (with very thin depletion layers, $W \sim 10^{-3}\ \mu\text{m}$) have high $I_S$ and excellent high-frequency rectification properties — the depletion layer is so thin that tunneling dominates, making the junction essentially resistive at microwave frequencies.

---

## §11.8 Appendix G — Couplers | 附录G——耦合器

### §11.8.1 Wilkinson Power Divider | Wilkinson功率分配器

**S-parameter matrix** (for ports 1=input, 2=output, 3=isolated output):

$$
\mathbf{S} = \begin{bmatrix}
0 & -j/\sqrt{2} & -j/\sqrt{2} \\
-j/\sqrt{2} & 0 & 0 \\
-j/\sqrt{2} & 0 & 0
\end{bmatrix} \quad \text{(G.1)}
$$

**Key figures of merit:**

| Parameter | Definition | Ideal Value |
|---|---|---|
| Return loss | $RL_1 = -20\log|S_{11}|$ | $+\infty$ dB |
| Coupling | $CP_{12} = -20\log|S_{12}|$ | $3\ \text{dB}$ |
| Isolation | $IL_{23} = -20\log|S_{23}|$ | $+\infty$ dB |

**Even/Odd Mode Analysis:** The 3-port network is decomposed into symmetric (even) and antisymmetric (odd) excitation modes. In even mode, ports 2 and 3 are driven in-phase — the $2Z_0$ crossbar has no current, ports 2 and 3 are isolated. In odd mode, ports 2 and 3 are driven 180° out-of-phase — the middle of the $2Z_0$ resistor is a virtual ground, perfectly matching port 1.

The resulting S-parameters confirm: $S_{11} = S_{22} = S_{33} = 0$, $S_{12} = S_{13} = -j/\sqrt{2}$, $S_{23} = 0$.

**Engineering Intuition:** The **Wilkinson divider is lossless** in the matched state — power from port 1 splits equally between ports 2 and 3. The resistor between ports 2 and 3 **only dissipates power when ports 2 and 3 are mismatched** (providing isolation). At resonance ($f_0$), return loss approaches infinity and coupling is exactly 3 dB. Typical bandwidth is $\leq 20\%$ due to the $\lambda/4$ transformer frequency response.

### §11.8.2 Branch-Line Coupler | 分支线耦合器

The branch-line is a 4-port quadrature hybrid using four $\lambda/4$ transmission line sections. For an ideal 3 dB branch-line:

$$
S_{14} = 1,\quad S_{12} = S_{13} = -j/\sqrt{2},\quad S_{23} = 0
$$

(directivity from the $\lambda/4$ port-to-port coupling). The **quadrature phase difference** ($90°$) between output ports is inherent to the branch-line geometry.

### §11.8.3 Lange Coupler | Lange耦合器

A **3 dB Lange coupler** (Fig. G-7) achieves tight coupling in microstrip through an **interdigitated 4-strip** (or 6/8-strip) geometry. The interdigital structure provides **wide bandwidth** (up to 40% fractional bandwidth) and coupling of $-5$ to $-1$ dB.

The trade-off: Lange couplers are physically compact but require precise manufacturing (photolithography for MMIC). They're standard in balanced mixers and image-reject receivers.

**Engineering Intuition:** When selecting a coupler:
- **Wilkinson** for power splitting (dissipative isolation) — use in feed networks
- **Branch-line** for I/Q generation — use in balanced mixers
- **Lange** for tight coupling at mm-wave — use in MMIC mixers

---

## §11.9 Appendix H — Noise Analysis | 附录H——噪声分析

### §11.9.1 Johnson-Nyquist Thermal Noise | Johnson-Nyquist热噪声

A resistor at temperature $T$ generates thermal noise power:

$$
P_n = k_B T\, \Delta f = k_B T B \quad \text{(H.2)}
$$

where $B$ is the noise bandwidth (Hz). The RMS noise voltage across resistor $R$ under matched load ($R_L = R$) is:

$$
V_n = \sqrt{4 k_B T R\, B} \quad \text{(H.5)}
$$

The **one-sided spectral density** is $S_v = 4k_B T R$ (V²/Hz), or $S_i = 4k_B T/R$ (A²/Hz).

**Two uncorrelated noise sources:** Their powers (not amplitudes) add:

$$
V_n^2 = V_{n1}^2 + V_{n2}^2 + 2C_{n1,n2}\sqrt{V_{n1}^2 V_{n2}^2} \quad \text{(H.9)}
$$

where $C_{n1,n2}$ is the correlation coefficient ($-1 \leq C \leq 1$). If $C = 1$ (fully correlated), voltages add linearly; if $C = 0$, powers add.

### §11.9.2 Noise Figure and Friiss's Formula | 噪声系数与Friiss公式

**Noise factor** $F$ of a two-port:

$$
F = \frac{\text{total output noise power}}{\text{output noise due to source alone}} = \frac{P_{n,\text{out}}}{G\, k_B T B}
$$

**Friiss's formula** for $N$ cascaded stages:

$$
F_{\text{total}} = F_1 + \frac{F_2-1}{G_1} + \frac{F_3-1}{G_1 G_2} + \cdots + \frac{F_N-1}{\prod_{i=1}^{N-1} G_i} \quad \text{(H.39)}
$$

This fundamental result shows that **the first stage dominates** — a low-noise amplifier (LNA) with $F_1 = 1.5$ dB and $G_1 = 20$ dB placed before a mixer with $F_2 = 10$ dB contributes only $1.5 + (10-1)/100 \approx 1.6$ dB to the total noise figure.

### §11.9.3 Noise Measure | 噪声量

The **noise measure** $M$ combines noise figure and gain:

$$
M = \frac{F - 1}{1 - G^{-1}} = \frac{F - 1}{1 - 1/G_A} \quad \text{(H.45)}
$$

The cascade ordering rule: **always place the stage with the lower noise measure first.** For $M_1 < M_2$, stage 1 must precede stage 2 for minimum overall noise figure.

### §11.9.4 Noise Circles | 噪声圆

At the input of an amplifier, constant noise figure circles in the $\Gamma_S$-plane are derived from:

$$
F = F_{\min} + \frac{4\,R_N}{|1+\Gamma_{\text{opt}}|^2}\cdot\frac{|\Gamma_S - \Gamma_{\text{opt}}|^2}{|1-\Gamma_S|^2} \quad \text{(H.34)}
$$

For a given $F > F_{\min}$, the center and radius of the noise circle are:

$$
\text{Center:}\quad \Gamma_{\text{opt}} \cdot \frac{1}{1 + \frac{(F-F_{\min})(1-|\Gamma_{\text{opt}}|^2)}{4\,R_N/Z_0}}
$$
$$
\text{Radius:}\quad \frac{\sqrt{\frac{(F-F_{\min})^2}{|\Gamma_{\text{opt}}|^2-1 + \frac{4\,R_N}{Z_0}(F-F_{\min})}}}{1 + |\Gamma_S|}
$$

**Engineering Intuition:** There is a **fundamental trade-off** between gain circles and noise circles — the optimal noise source impedance ($\Gamma_{\text{opt}}$) is often far from the optimal gain impedance. Low-noise amplifier design navigates this compromise, typically accepting slightly higher $F$ to achieve adequate gain.

---

## §11.10 Appendix I — MATLAB | 附录I——MATLAB简介

### §11.10.1 Matrix Operations and Scripting | 矩阵运算与脚本

MATLAB is the standard computational engine for RF circuit analysis. Key operations:

```matlab
% Complex S-parameters in magnitude/phase form
S11 = 0.7 * exp(j*(-70 * pi/180));   % convert degrees to radians
S12 = 0.2 * exp(j*(-10 * pi/180));

% S-parameter matrix assembly
sparam = [S11 S12; S21 S22];

% Smith Chart utilities
smith-chart;           % create Smith Chart background
input-stability(sparam, 'r');   % plot input stability circle in red
output-stability(sparam, 'b');  % plot output stability circle in blue
```

### §11.10.2 Stability Factor K-Factor Function | 稳定性K因子函数

```matlab
function [K, delta] = K_factor(sparam)
% K-factor and delta for a 2-port S-parameter matrix
% Unconditional stability: K > 1 AND |delta| < 1
S11 = sparam(1,1); S12 = sparam(1,2);
S21 = sparam(2,1); S22 = sparam(2,2);

delta = S11.*S22 - S12.*S21;
K = (1 - abs(S11).^2 - abs(S22).^2 + abs(delta).^2) ./ (2.*abs(S12.*S21));
end
```

### §11.10.3 Plotting and Graphics | 绘图与图形

```matlab
plot(r*1000, H, 'k')         % black curve, x in mm
semilogx(f, gain_db, 'r')   % log-x axis for frequency response
semilogy(f, loss_db, 'b')   % log-y axis for loss plots
polar(theta, |Gamma|, 'r')  % polar plot for reflection coefficients
print -deps 'fig9-8.eps'     % export as Encapsulated PostScript
```

### §11.10.4 CAD Validation Workflow | CAD验证工作流

The textbook's M-file philosophy: **every analytical result must be reproducible by independent code.** The workflow for oscillator design is:

1. Measure/input S-parameters at the bias point and frequency
2. Compute $k$-factor and $\Delta$: `[K, delta] = K_factor(sparam)`
3. If $K < 1$, draw stability circles on Smith Chart
4. Select $\Gamma_S$ on the unstable region such that $|\Gamma_{\text{in}}| > 1$
5. Synthesize matching networks using $Z \to \Gamma$ transforms

**Engineering Intuition:** MATLAB is an excellent **design verification** tool but does not replace circuit simulators (ADS, HFSS) for layout and electromagnetic effects. Use MATLAB for equation-level validation and ADS/MMICAD for full-wave electromagnetic verification.

---

## §11.11 Key Formula Reference Card | 关键公式速查卡

| Topic | Formula | Application |
|---|---|---|
| Skin depth | $\delta_s = \sqrt{2/(\omega\mu_0\sigma)}$ | Conductor loss at frequency $f$ |
| Crystal series $f_s$ | $f_s = 1/(2\pi\sqrt{L_q C_q})$ | Quartz resonator design |
| Crystal parallel $f_p$ | $f_p = f_s\sqrt{1 + C_q/C_p}$ | Crystal oscillator mode |
| Thermal noise voltage | $V_n = \sqrt{4 k_B T R\, B}$ | Receiver sensitivity |
| Friiss's formula | $F_{\text{tot}} = F_1 + \frac{F_2-1}{G_1} + \cdots$ | Cascade noise budget |
| Noise measure | $NM = (F-1)/(1-1/G_A)$ | Stage ordering optimization |
| Skin effect $R$ ratio | $R_{\text{AC}}/R_{\text{DC}} = a/(2\delta_s)$ | Conductor loss scaling |
| Smith $\Gamma\to Z$ | $Z = Z_0\frac{1+\Gamma}{1-\Gamma}$ | Impedance transformation |
| S→Y determinant | $D_S = (1+S_{11})(1+S_{22})-S_{12}S_{21}$ | Y-parameter conversion |
