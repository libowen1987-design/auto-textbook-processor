# Pozar Ch13 (4e Ch10) — Noise & Nonlinear Distortion

> **Note:** This chapter corresponds to **Chapter 10** in Pozar *Microwave Engineering*, 4th Edition.
> Covers noise in microwave systems, nonlinear distortion mechanisms, and dynamic range.

---

## 10.1 Noise

### 10.1.1 Thermal (Johnson-Nyquist) Noise

Random thermal agitation of charge carriers produces a **thermal noise power** available from a resistor at temperature $T$ (K) over bandwidth $B$ (Hz):

$$
P_n = kTB \quad \text{[W]}
$$

> **量纲检查:** $k = 1.38 \times 10^{-23}\;\text{J/K}$, $T$ [K], $B$ [Hz = 1/s] $\Rightarrow$ J/s = W ✓

**Key properties:**
- Available noise power is independent of resistance value (only depends on $T$, $B$)
- **White noise:** Power spectral density (PSD) $\approx$ flat across RF/microwave frequencies
- PSD: $S_n(f) = kT$ [W/Hz] for a matched termination

**RMS noise voltage** of an open-circuit resistor $R$:

$$
v_n = \sqrt{4kTRB} \quad \text{[V]}
$$

**Available noise power** from any two-port (matched source at temperature $T$):

$$
P_{n,\text{avail}} = \frac{|v_n|^2}{4R} = \frac{4kTBR}{4R} = kTB
$$

> **Physical intuition:** Even at absolute zero, quantum zero-point fluctuations give a residual $hf/2$ per mode; at microwave frequencies ($f \lesssim 300$ GHz), $hf \ll kT$ at room temperature, so the classical $kTB$ formula is accurate.

### 10.1.2 Noise Figure (F) and Noise Temperature ($T_e$)

**Noise figure** quantifies the SNR degradation through a two-port network:

$$
F = \frac{\text{SNR}_{\text{in}}}{\text{SNR}_{\text{out}}} \quad \text{(linear)}
$$

At standard temperature $T_0 = 290\;\text{K}$:

$$
F = 1 + \frac{T_e}{T_0} \quad \Longleftrightarrow \quad T_e = (F - 1)T_0
$$

where $T_e$ is the **equivalent input noise temperature** of the device.

**In dB:**

$$
F_{\text{dB}} = 10 \log_{10}(F)
$$

| Device Type | Typical $F$ [dB] | Typical $T_e$ [K] |
|---|---|---|
| Low-noise HEMT @ 10 GHz | 0.3–0.5 | 21–36 |
| GaAs MESFET @ 10 GHz | 0.8–1.5 | 60–120 |
| BJT @ 2 GHz | 1.0–2.0 | 75–170 |
| LNA module @ 1–6 GHz | 0.5–1.5 | 36–120 |
| Schottky mixer | 5–7 | 600–1200 |
| Lossy passive component | $= L_{\text{dB}}$ (same as loss) | $= (L - 1)T_0$ |

### 10.1.3 Cascaded System (Friis Formula)

For $N$ cascaded stages with noise figures $F_i$ and available gains $G_i$:

$$
F_{\text{total}} = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \cdots + \frac{F_N - 1}{G_1 G_2 \cdots G_{N-1}}
$$

In terms of noise temperature:

$$
T_{\text{total}} = T_{e1} + \frac{T_{e2}}{G_1} + \frac{T_{e3}}{G_1 G_2} + \cdots + \frac{T_{eN}}{G_1 G_2 \cdots G_{N-1}}
$$

> **Engineering intuition:** The first stage dominates the system noise figure. A low-noise, modest-gain LNA before a higher-noise mixer is the classic receiver front-end strategy. For example, an LNA with $F_1 = 1.5$ dB, $G_1 = 12$ dB reduces the contribution of a $F_2 = 6$ dB mixer by a factor of $G_1 = 15.8$ $\Rightarrow$ $F_{\text{total}} \approx F_1 + 0.25$ dB.

**Passive lossy components** have noise figure equal to their loss ($L$ is the loss factor):

$$
F_{\text{passive}} = L \quad (\text{linear}) \quad \text{or} \quad F_{\text{passive,dB}} = L_{\text{dB}}
$$

This is because a lossy matched component at thermal equilibrium outputs $kT_0B$ — the same noise as from the matched input — and the signal is attenuated by $L$, so SNR degrades by exactly $L$.

### 10.1.4 Noise in Two-Ports — Generalized Noise Figure

The noise figure of a two-port depends on the source admittance $Y_s = G_s + jB_s$:

$$
F(Y_s) = F_{\min} + \frac{R_n}{G_s} |Y_s - Y_{\text{opt}}|^2
$$

where:
- $F_{\min}$ = **minimum noise figure** (achievable with optimum source)
- $R_n$ = **equivalent noise resistance** [$\Omega$] — sensitivity to mismatch from optimum
- $Y_{\text{opt}} = G_{\text{opt}} + jB_{\text{opt}}$ = **optimum source admittance**

**In terms of reflection coefficient** (often given in data sheets):

$$
F(\Gamma_s) = F_{\min} + \frac{4R_n}{Z_0} \frac{|\Gamma_s - \Gamma_{\text{opt}}|^2}{(1 - |\Gamma_s|^2) |1 + \Gamma_{\text{opt}}|^2}
$$

> **量纲检查:** $\frac{R_n}{G_s}$ [$\Omega$ / S = $\Omega^2$], $(Y_s - Y_{\text{opt}})^2$ [S²] $\Rightarrow$ 无量纲 ✓

**Engineering application:** Noise circles on the Smith chart. For LNA design, the input matching network must trade off between:
- **Conjugate match** $(\Gamma_s = \Gamma_{\text{in}}^*$) for maximum gain
- **Noise match** $(\Gamma_s = \Gamma_{\text{opt}}$) for minimum noise figure

The "noise measure" $M$ for comparing devices:

$$
M = \frac{F - 1}{1 - 1/G}
$$

where $G$ is the associated gain.

### 10.1.5 System Noise Temperature

The **system noise temperature** referred to the receiver input:

$$
T_{\text{sys}} = T_A + T_{\text{rec}} = T_A + \sum_i \frac{T_{ei}}{G_{1} \cdots G_{i-1}}
$$

where $T_A$ is the **antenna noise temperature** (external noise, sky noise, ground noise).

**Link SNR** (fundamental for link budget):

$$
\text{SNR} = \frac{P_{\text{sig}}}{k T_{\text{sys}} B}
$$

The figure of merit $G/T = G_{\text{ant}} / T_{\text{sys}}$ [dB/K] determines receiver sensitivity. Higher $G/T$ = better sensitivity.

---

## 10.2 Nonlinear Distortion

### 10.2.1 Memoryless Nonlinear Model

A weakly nonlinear amplifier can be modeled by a power series:

$$
v_{\text{out}} = a_1 v_{\text{in}} + a_2 v_{\text{in}}^2 + a_3 v_{\text{in}}^3 + \cdots
$$

where $a_1$ is the small-signal voltage gain, and $a_2, a_3$ represent second- and third-order nonlinearity.

> **Caveat:** This model assumes **memoryless** nonlinearity (instantaneous response). Real amplifiers also exhibit memory effects (bias circuits, thermal dynamics), causing asymmetric distortion.

For a single-tone input $v_{\text{in}} = V_0 \cos(\omega t)$:

$$
v_{\text{out}} = \underbrace{\left( a_1 V_0 + \frac{3}{4} a_3 V_0^3 \right)}_{\text{fundamental}} \cos(\omega t) \;+\;
\underbrace{\frac{1}{2} a_2 V_0^2}_{\text{2nd harmonic}} \cos(2\omega t) \;+\;
\underbrace{\frac{1}{4} a_3 V_0^3}_{\text{3rd harmonic}} \cos(3\omega t) + \cdots
$$

**Key observation:** $a_3$ is typically **negative** for real amplifiers (gain compression). The $a_2$ term produces DC offset ($\frac{1}{2}a_2 V_0^2$) and second harmonic.

### 10.2.2 Gain Compression

The **1 dB compression point** ($P_{1\text{dB}}$) is the input (or output) power where the gain drops by 1 dB from the ideal linear value:

$$
G_{1\text{dB}} = G_0 - 1 \quad \text{[dB]}
$$

From the power series, the fundamental output amplitude is:

$$
V_{\text{out},1} \approx a_1 V_0 \left( 1 + \frac{3 a_3}{4 a_1} V_0^2 \right)
$$

The 1 dB compression occurs when:

$$
20 \log_{10}\left| 1 + \frac{3 a_3}{4 a_1} V_0^2 \right| = -1 \;\text{dB}
$$

Solving: $\displaystyle V_{0,\text{1dB}} \approx \sqrt{0.108 \left| \frac{4a_1}{3a_3} \right| }$ (for $a_3 < 0$)

> **量纲检查:** $a_1$ [V/V], $a_3$ [V/V³], $V_0^2$ [V²] $\Rightarrow$ $\frac{a_3 V_0^2}{a_1}$ 无量纲 ✓

**Typical values:**
- LNA: $P_{1\text{dB,out}} \approx -10$ to +5 dBm
- Power amplifier: $P_{1\text{dB,out}} \approx +25$ to +50 dBm
- Mixer: $P_{1\text{dB}} \approx -10$ to 0 dBm (input-referred)

### 10.2.3 Harmonic Distortion

The **n-th harmonic** amplitude relative to the fundamental:

$$
\text{HD}_2 = \frac{1}{2} \frac{a_2}{a_1} V_0 \quad \text{(second harmonic)}
$$

$$
\text{HD}_3 = \frac{1}{4} \frac{a_3}{a_1} V_0^2 \quad \text{(third harmonic)}
$$

**Total harmonic distortion (THD):**

$$
\text{THD} = \frac{\sqrt{V_2^2 + V_3^2 + \cdots}}{V_1} \approx \sqrt{\text{HD}_2^2 + \text{HD}_3^2}
$$

### 10.2.4 Intermodulation Distortion

For a **two-tone input** $v_{\text{in}} = V_0(\cos \omega_1 t + \cos \omega_2 t)$:

- **Fundamental outputs** at $\omega_1, \omega_2$: $\displaystyle a_1 V_0 + \frac{9}{4}a_3 V_0^3$ (compression)
- **Second-order IM products** at $\omega_1 \pm \omega_2$: $\displaystyle \frac{a_2 V_0^2}{2} \cos(\omega_1 \pm \omega_2)t$
- **Third-order IM products** at $2\omega_1 \pm \omega_2$ and $\omega_1 \pm 2\omega_2$:

  $$
  \text{IM}_3\text{ at } 2\omega_1 - \omega_2:\; \frac{3}{4}a_3 V_0^3 \cos(2\omega_1 - \omega_2)t
  $$

  $$
  \text{IM}_3\text{ at } 2\omega_2 - \omega_1:\; \frac{3}{4}a_3 V_0^3 \cos(2\omega_2 - \omega_1)t
  $$

**Critical observation:** The third-order IM products fall **in-band** for a narrowband system when $\omega_1 \approx \omega_2$. The frequencies $2\omega_1 - \omega_2$ and $2\omega_2 - \omega_1$ are very close to $\omega_1, \omega_2$, making them impossible to filter out.

> **Physical intuition:** IM3 products grow as $V_0^3$ (slope 3 dB/dB on a log-log plot), while the fundamental grows as $V_0$ (1 dB/dB). They eventually overpower the signal.

### 10.2.5 Third-Order Intercept Point (IP3)

The **third-order intercept point** is the extrapolated input (IIP3) or output (OIP3) power where the fundamental and IM3 products would be equal:

$$
\text{IIP}_3 \text{ [dBm]} = P_{\text{in}} + \frac{\text{IMR}_3}{2}
$$

where $\text{IMR}_3 = P_{\text{out,1}} - P_{\text{out,IM3}}$ [dB] is the third-order intermodulation ratio at the given input power $P_{\text{in}}$.

**Relationship to $P_{1\text{dB}}$:**

For most amplifiers, empirically:

$$
\text{IIP}_3 \approx P_{1\text{dB,in}} + 9\!-\!12 \text{ dB}
$$

For an ideal cubic nonlinearity:

$$
\text{IIP}_3 = P_{1\text{dB,in}} + 9.6 \text{ dB}
$$

**Linear relationship between OIP3 and IIP3:**

$$
\text{OIP}_3 = \text{IIP}_3 + G \quad \text{[dBm]}
$$

> **量纲检查:** Both IIP3/OIP3 in dBm, $G$ in dB $\Rightarrow$ dBm ✓

### 10.2.6 Cascaded IP3

For $N$ cascaded stages:

$$
\frac{1}{\text{IIP3}_{\text{total}}} = \frac{1}{\text{IIP3}_1} + \frac{G_1}{\text{IIP3}_2} + \frac{G_1 G_2}{\text{IIP3}_3} + \cdots
$$

**Note:** This is the **inverse** of the Friis formula behavior. Linearity gets harder to maintain as gain accumulates, whereas noise figure is dominated by the first stage. This creates the classic **gain distribution tradeoff**:
- High first-stage gain $\Rightarrow$ low noise figure $\oplus$ poor linearity
- Low first-stage gain $\Rightarrow$ higher noise figure $\oplus$ better linearity

### 10.2.7 Cross Modulation

Cross modulation occurs when a strong interfering signal modulates the gain of the desired signal through nonlinearity. From the cubic term:

$$
v_{\text{out}}(\omega_1) = a_1 V_1 \left(1 + \frac{3a_3}{4a_1} V_2^2\right) \cos \omega_1 t
$$

The amplitude of the carrier $\omega_1$ is modulated by $\frac{3a_3}{4a_1} V_2^2$, which changes with the envelope of the interferer at $\omega_2$.

---

## 10.3 Dynamic Range

### 10.3.1 Definitions

**Linear Dynamic Range (DR):**

$$
\text{DR} = \frac{P_{1\text{dB,in}}}{P_{n,\text{in}}} \quad \text{(linear)} \quad \text{or} \quad \text{DR} = P_{1\text{dB,in}} - P_{n,\text{in}} \quad \text{[dB]}
$$

where $P_{n,\text{in}} = kT_0B \cdot F$ is the input-referred noise floor (including system noise figure).

### 10.3.2 Spurious-Free Dynamic Range (SFDR)

SFDR is defined as the maximum signal-to-noise ratio such that the IM3 products are below the noise floor:

$$
\text{SFDR} = \frac{2}{3} (\text{IIP}_3 - P_{n,\text{in}}) \quad \text{[dB]} \quad \text{or} \quad \text{SFDR} = \frac{2}{3} (\text{IIP}_3 + 174 - F_{\text{dB}} - 10 \log_{10} B) \quad \text{[dB]}
$$

where:
- $P_{n,\text{in}} = -174 + F_{\text{dB}} + 10\log_{10}B$ [dBm]
- $-174$ is $k T_0$ in [dBm/Hz] ($10\log_{10}(kT_0 \cdot 1000)$)
- $F_{\text{dB}}$ is the system noise figure [dB]
- $B$ is the bandwidth [Hz]

> **量纲检查:** $\text{IIP}_3$ [dBm], $P_{n,\text{in}}$ [dBm] $\Rightarrow$ SFDR [dB] ✓

**Derivation:**
- IM3 power at input power $P_{\text{in}}$: $P_{\text{IM3}} = 3P_{\text{in}} - 2\text{IIP}_3$ [dBm]
- Set $P_{\text{IM3}} = P_{n,\text{in}}$ $\Rightarrow$ $3P_{\text{in,max}} - 2\text{IIP}_3 = P_{n,\text{in}}$
- $P_{\text{in,max}} = \frac{2}{3}\text{IIP}_3 + \frac{1}{3}P_{n,\text{in}}$
- $\text{SFDR} = P_{\text{in,max}} - P_{n,\text{in}} = \frac{2}{3}(\text{IIP}_3 - P_{n,\text{in}})$

### 10.3.3 Receiver Dynamic Range

| Type | Definition | Typical Value |
|---|---|---|
| **Linear DR** | $P_{1\text{dB,in}} / P_{n,\text{in}}$ | 40–80 dB |
| **SFDR** | $\frac{2}{3}(\text{IIP}_3 - P_{n,\text{in}})$ | 40–70 dB |
| **Instantaneous DR** | Full-scale / noise floor (ADC-limited) | 60–90 dB (depends on bits) |
| **AGC DR** | Range over which AGC maintains constant output | 60–120 dB |

**Receiver dynamic range bottleneck:** The ADC bit resolution sets the ultimate limit. Each bit gives $\approx 6$ dB of dynamic range. A 12-bit ADC gives $\approx 72$ dB ideal, but effective bits are often 1–2 bits lower (ENOB = Effective Number of Bits).

### 10.3.4 Tradeoff Summary

```
                     Noise Figure (F) ← first stage gain dominates
                    /
     Receiver     /
    Performance  ---- Linearity (IIP3) ← first stage gain hurts
                    \
                     Dynamic Range (SFDR) ← balanced by F and IIP3
```

**Design flow:**
1. Choose LNA with low $F$ and sufficient $G$ to suppress noise from subsequent stages
2. Check cascaded IIP3; if too low, reduce first-stage gain or use higher-IIP3 LNA
3. Compute SFDR for the required bandwidth
4. Adjust gain distribution to balance $F$ and IIP3

---

## Summary — Key Formulas

| Quantity | Formula | Units |
|---|---|---|
| Thermal noise power | $P_n = kTB$ | W |
| Noise figure → noise temp | $T_e = (F - 1)T_0$ | K |
| Friis formula | $F_{\text{total}} = F_1 + \frac{F_2 - 1}{G_1} + \cdots$ | linear |
| Two-port NF | $F = F_{\min} + \frac{R_n}{G_s}\|Y_s - Y_{\text{opt}}\|^2$ | linear |
| Gain compression | $P_{1\text{dB,out}} = P_{1\text{dB,in}} + G - 1\text{ dB}$ | dBm, dB |
| Third-order intercept | $\text{IIP}_3 = P_{\text{in}} + \frac{\text{IMR}_3}{2}$ | dBm |
| Cascaded IP3 | $\frac{1}{\text{IIP3}_{\text{total}}} = \frac{1}{\text{IIP3}_1} + \frac{G_1}{\text{IIP3}_2} + \cdots$ | mW, linear |
| SFDR | $\text{SFDR} = \frac{2}{3}(\text{IIP}_3 - P_{n,\text{in}})$ | dB |

---

## References

- Pozar, D.M., *Microwave Engineering*, 4th Ed., Chapter 10
- Friis, H.T., "Noise Figure of Radio Receivers," *Proc. IRE*, 1944
- Bahl, I., *Fundamentals of RF and Microwave Transistor Amplifiers*, 2009
- Gonzalez, G., *Microwave Transistor Amplifiers: Analysis and Design*, 2nd Ed.
