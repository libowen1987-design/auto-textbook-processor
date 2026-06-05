# Ch9 — Solid-State Amplifiers & Oscillators

> Based on: R. E. Collin, *Foundations for Microwave Engineering*, 2nd ed., IEEE Press, 2001.
> PDF page references correspond to the 2001 IEEE Press Classic Reissue edition.

---

## Overview

This chapter covers solid-state microwave amplifier and oscillator design. The topics span small-signal S-parameter amplifier design (stability, gain, noise), negative-resistance and transistor oscillators, varactor multipliers/parametric amplifiers, and balanced/distributed amplifier architectures. The discussion assumes familiarity with two-port network theory and Smith chart techniques from earlier chapters.

---

## 9.1 Two-Port Network Representation & S-Parameter Amplifier Design [pp. 713–735]

### S-Parameter Representation of a Transistor

A transistor at microwave frequencies is treated as a linear two-port network characterized by its scattering parameters (S-parameters). For a common-source/common-emitter configuration:

```
        Port 1                     Port 2
   Z0 ────┬──── [S] ────┬──── Z0
          │              │
         Γin            Γout
          │              │
         ΓS             ΓL
```

Input reflection coefficient with load $\Gamma_L$:

$$\Gamma_{in} = S_{11} + \frac{S_{12} S_{21} \Gamma_L}{1 - S_{22} \Gamma_L} \tag{9.1a}$$

Output reflection coefficient with source $\Gamma_S$:

$$\Gamma_{out} = S_{22} + \frac{S_{12} S_{21} \Gamma_S}{1 - S_{11} \Gamma_S} \tag{9.1b}$$

These expressions account for the internal feedback through $S_{12}$.

### Power Gain Definitions

Three gain definitions are commonly used [pp. 728–735]:

**1. Transducer Power Gain $G_T$** — ratio of power delivered to the load to power available from the source:

$$G_T = \frac{|S_{21}|^2 (1 - |\Gamma_S|^2)(1 - |\Gamma_L|^2)}{|(1 - S_{11}\Gamma_S)(1 - S_{22}\Gamma_L) - S_{12}S_{21}\Gamma_S\Gamma_L|^2} \tag{9.2}$$

**2. Operating Power Gain $G_P$** — ratio of power delivered to the load to power input to the network:

$$G_P = \frac{|S_{21}|^2 (1 - |\Gamma_L|^2)}{(1 - |\Gamma_{in}|^2)|1 - S_{22}\Gamma_L|^2} \tag{9.3}$$

**3. Available Power Gain $G_A$** — ratio of power available from the network to power available from the source:

$$G_A = \frac{|S_{21}|^2 (1 - |\Gamma_S|^2)}{(1 - |\Gamma_{out}|^2)|1 - S_{11}\Gamma_S|^2} \tag{9.4}$$

### Stability Criteria [pp. 735–744]

A two-port is **unconditionally stable** if $|\Gamma_{in}| < 1$ and $|\Gamma_{out}| < 1$ for all passive source/load terminations ($|\Gamma_S| < 1$, $|\Gamma_L| < 1$).

**K-Δ Test (Rollett's stability factor):**

$$K = \frac{1 - |S_{11}|^2 - |S_{22}|^2 + |\Delta|^2}{2|S_{12}S_{21}|} > 1 \tag{9.5}$$

$$|\Delta| = |S_{11}S_{22} - S_{12}S_{21}| < 1 \tag{9.6}$$

Both conditions must hold for unconditional stability.

When $K < 1$, the device is **conditionally stable** (potentially unstable). Stability circles on the Smith chart define stable and unstable regions:

- **Input stability circle** (center $C_S$, radius $R_S$) in $\Gamma_S$-plane:

$$C_S = \frac{(S_{11} - \Delta S_{22}^*)^*}{|S_{11}|^2 - |\Delta|^2}, \quad R_S = \left|\frac{S_{12}S_{21}}{|S_{11}|^2 - |\Delta|^2}\right| \tag{9.7a}$$

- **Output stability circle** (center $C_L$, radius $R_L$) in $\Gamma_L$-plane:

$$C_L = \frac{(S_{22} - \Delta S_{11}^*)^*}{|S_{22}|^2 - |\Delta|^2}, \quad R_L = \left|\frac{S_{12}S_{21}}{|S_{22}|^2 - |\Delta|^2}\right| \tag{9.7b}$$

### Maximum Available Gain (MAG)

For unconditionally stable devices, the maximum transducer gain occurs under **conjugate match** at both ports:

$$\Gamma_S = \Gamma_{in}^*, \quad \Gamma_L = \Gamma_{out}^* \tag{9.8}$$

The simultaneous conjugate match solution:

$$\Gamma_{MS} = \frac{B_1 \pm \sqrt{B_1^2 - 4|C_1|^2}}{2C_1} \tag{9.9a}$$
$$\Gamma_{ML} = \frac{B_2 \pm \sqrt{B_2^2 - 4|C_2|^2}}{2C_2} \tag{9.9b}$$

where:

$$B_1 = 1 + |S_{11}|^2 - |S_{22}|^2 - |\Delta|^2$$
$$B_2 = 1 + |S_{22}|^2 - |S_{11}|^2 - |\Delta|^2$$
$$C_1 = S_{11} - \Delta S_{22}^*$$
$$C_2 = S_{22} - \Delta S_{11}^*$$

The **Maximum Available Gain** (MAG):

$$G_{max} = \frac{|S_{21}|}{S_{12}} \left(K - \sqrt{K^2 - 1}\right) \tag{9.10}$$

---

## 9.2 Small-Signal Amplifier Design [pp. 744–760]

### Unilateral Approximation

When $|S_{12}|$ is small (negligible feedback), set $S_{12} = 0$:

$$\Gamma_{in} \approx S_{11}, \quad \Gamma_{out} \approx S_{22} \tag{9.11}$$

The **unilateral transducer gain**:

$$G_{TU} = G_S \cdot G_0 \cdot G_L \tag{9.12}$$

where:

$$G_S = \frac{1 - |\Gamma_S|^2}{|1 - S_{11}\Gamma_S|^2}, \quad G_0 = |S_{21}|^2, \quad G_L = \frac{1 - |\Gamma_L|^2}{|1 - S_{22}\Gamma_L|^2} \tag{9.13}$$

Maximum unilateral gain occurs for $\Gamma_S = S_{11}^*$, $\Gamma_L = S_{22}^*$:

$$G_{TU,max} = \frac{|S_{21}|^2}{(1 - |S_{11}|^2)(1 - |S_{22}|^2)} \tag{9.14}$$

### Unilateral Gain Error Bound

The error introduced by neglecting $S_{12}$ is bounded by:

$$\frac{1}{(1 + U)^2} < \frac{G_T}{G_{TU}} < \frac{1}{(1 - U)^2} \tag{9.15}$$

where the **unilateral figure of merit**:

$$U = \frac{|S_{12}||S_{21}||S_{11}||S_{22}|}{(1 - |S_{11}|^2)(1 - |S_{22}|^2)} \tag{9.16}$$

### Constant Gain Circles

For bilateral design, constant operating-power-gain circles are used. The center and radius of a constant $G_P$ circle (in $\Gamma_L$ plane):

$$C_g = \frac{g S_{22}^*}{1 - (1 - g)|S_{22}|^2} \tag{9.17a}$$
$$R_g = \frac{\sqrt{1 - g(1 - |S_{22}|^2)}}{1 - (1 - g)|S_{22}|^2} \tag{9.17b}$$

where the normalized gain parameter $g = G_P/|S_{21}|^2$.

The input matching network is then designed to present $\Gamma_S = \Gamma_{in}^*$ for the chosen $\Gamma_L$.

Unilateral gain circles ($S_{12} = 0$) can be drawn for $G_S$ and $G_L$ separately. For $G_S$ circles:

$$d_S = \frac{g_S S_{11}^*}{1 - (1 - g_S)|S_{11}|^2}, \quad r_S = \frac{\sqrt{1 - g_S(1 - |S_{11}|^2)}}{1 - (1 - g_S)|S_{11}|^2} \tag{9.18}$$

where $g_S = G_S/(1 - |S_{11}|^2)$ is the normalized gain relative to the matched $G_S$ value.

---

## 9.3 Noise in Amplifiers [pp. 760–776]

### Noise Figure

The **noise figure** $F$ of a two-port is defined as:

$$F = \frac{\text{input SNR}}{\text{output SNR}} = \frac{N_o}{G_T N_i} \tag{9.19}\]

For a two-port with noise parameters, the noise figure depends on the source reflection coefficient $\Gamma_S$:

$$F(\Gamma_S) = F_{min} + \frac{4R_n}{Z_0} \frac{|\Gamma_S - \Gamma_{opt}|^2}{(1 - |\Gamma_S|^2)|1 + \Gamma_{opt}|^2} \tag{9.20}$$

or equivalently:

$$F = F_{min} + \frac{R_n}{G_S} |Y_S - Y_{opt}|^2 \tag{9.21}$$

where:
- $F_{min}$ = minimum noise figure
- $\Gamma_{opt}$ = optimal source reflection coefficient for minimum NF
- $R_n$ = equivalent noise resistance
- $Y_S = G_S + jB_S$ = source admittance

### Constant Noise-Figure Circles

For a given noise figure $F_k > F_{min}$, the locus of $\Gamma_S$ that yields $F_k$ is a circle with:

$$N = \frac{F_k - F_{min}}{4R_n/Z_0} |1 + \Gamma_{opt}|^2 \tag{9.22a}$$

$$C_F = \frac{\Gamma_{opt}}{1 + N} \tag{9.22b}$$

$$R_F = \frac{\sqrt{N(N + 1 - |\Gamma_{opt}|^2)}}{1 + N} \tag{9.22c}$$

### Noise Figure for Cascaded Stages (Friis' Formula)

For a cascade of $n$ stages:

$$F_{total} = F_1 + \frac{F_2 - 1}{G_{A1}} + \frac{F_3 - 1}{G_{A1}G_{A2}} + \cdots \tag{9.23}$$

where $F_i$ and $G_{Ai}$ are the noise figure and available gain of the $i$th stage.

### Amplifier Design Trade-off

In practice, the source termination is chosen as a compromise between:
- **Maximum gain** ($\Gamma_S = \Gamma_{MS}$, conjugate match)
- **Minimum noise** ($\Gamma_S = \Gamma_{opt}$)

Design proceeds by drawing constant gain circles and constant noise circles on the Smith chart and selecting a $\Gamma_S$ that provides acceptable gain with low noise figure.

---

## 9.4 Oscillator Design [pp. 831–860]

### Negative-Resistance Oscillator Concept

An oscillator can be viewed as a one-port negative-resistance device. Oscillation occurs when:

$$Z_{in}(f) + Z_L(f) = 0 \quad \text{(resonance condition)} \tag{9.24}$$

where $Z_{in} = R_{in} + jX_{in}$ is the input impedance of the active device and $Z_L = R_L + jX_L$ is the load impedance.

For steady-state oscillation:

$$R_{in}(I, f_o) + R_L(f_o) = 0 \tag{9.25a}$$
$$X_{in}(I, f_o) + X_L(f_o) = 0 \tag{9.25b}$$

where $I$ is the RF current amplitude. The negative resistance ($R_{in} < 0$) provides power to sustain oscillation.

Start-up condition: $R_{in}(0) + R_L < 0$ (overall negative resistance at small signal).

### Transistor Oscillator Design [p. 854]

A transistor can be configured as an oscillator by designing the feedback network to make the device potentially unstable ($K < 1$) and then presenting the appropriate termination to create a negative resistance at one port.

**Common design approach:**
1. Choose a transistor with $K < 1$ at the desired frequency, or add external feedback
2. Design the output matching network such that $\Gamma_L$ produces $|\Gamma_{in}| > 1$ (negative resistance at input)
3. Design the input resonant network to satisfy the oscillation condition
4. Design for specific output power by adjusting the load line

For a transistor oscillator, the loop gain must exceed unity at the desired frequency, and the total phase shift around the loop must be a multiple of $2\pi$.

The oscillator output power is determined by the large-signal characteristics. A small-signal design provides the starting point; the final design requires large-signal S-parameters or load-pull data.

### Oscillator Coupling

The load is typically coupled through a matching network. For maximum power transfer:

$$R_L = -\frac{R_{in}}{3} \quad \text{(optimal coupling for maximum power)} \tag{9.26}$$

This allows the device to swing into the positive resistance region for stable oscillation.

### Dielectric Resonator Oscillators (DROs)

DROs use a high-$Q$ dielectric resonator coupled to the transistor for frequency stabilization. The dielectric puck (typically BaTi$_4$O$_9$ or similar) is placed near a microstrip line and acts as a band-stop/band-pass element.

---

## 9.5 Varactor Multipliers & Parametric Amplifiers [pp. 799–830]

### Varactor Diode

A **varactor** (variable reactor) is a p-n junction diode operated in reverse bias. The junction capacitance varies with bias voltage:

$$C_j(V) = \frac{C_{j0}}{(1 + V/V_j)^m} \tag{9.27}$$

where $C_{j0}$ is the zero-bias capacitance, $V_j$ is the built-in potential, and $m = 1/2$ for abrupt junctions, $m = 1/3$ for graded junctions.

The **Varactor figure of merit** is the cutoff frequency:

$$f_c = \frac{1}{2\pi R_s C_{j0}} \tag{9.28}$$

### Manley-Rowe Relations [pp. 807–809]

For a nonlinear reactance pumped at frequency $f_p$ with signal at $f_s$, the Manley-Rowe power relations govern the power flow:

$$\sum_{m=0}^\infty \sum_{n=-\infty}^\infty \frac{m P_{m,n}}{m f_p + n f_s} = 0 \tag{9.29a}$$
$$\sum_{m=0}^\infty \sum_{n=-\infty}^\infty \frac{n P_{m,n}}{m f_p + n f_s} = 0 \tag{9.29b}$$

where $P_{m,n}$ is the power at frequency $mf_p + nf_s$.

For a **parametric up-converter** ($m=1$, $n=1$, idler at $f_i = f_p - f_s$):

$$P_s + P_i + P_p = 0 \quad \text{(power conservation)} \tag{9.30}$$
$$\frac{P_s}{f_s} + \frac{P_i}{f_i} = 0, \quad \frac{P_p}{f_p} - \frac{P_i}{f_i} = 0 \tag{9.31}$$

The up-converter gain ($f_o = f_p + f_s$):

$$G = \frac{f_o}{f_s} \cdot \frac{4Q^2}{(1 + Q^2)^2} \quad \text{(reactive up-converter)} \tag{9.32}$$

### Negative-Resistance Parametric Amplifier [pp. 821–829]

With a resonant circuit at the signal and idler frequencies, the varactor exhibits a negative resistance at the signal port:

$$R_{neg} = -\frac{M^2}{\omega_s \omega_i R_{idler}} \tag{9.33}$$

where $M = C_1/2C_0$ is the modulation index of the varactor capacitance.

Gain of the negative-resistance paramp:

$$G_S = \left(\frac{R_L - |R_{neg}|}{R_L + R_s - |R_{neg}|}\right)^2 \tag{9.34}$$

### Varactor Frequency Multipliers

The efficiency of an $n$th-order varactor frequency multiplier:

$$\eta_n = \frac{P_{out}(nf_p)}{P_{in}(f_p)} \leq \frac{1}{n^2} \quad \text{(ideal abrupt-junction)} \tag{9.35}$$

Practical doublers can achieve 60–80% efficiency; triplers 40–60%.

---

## 9.6 Balanced & Distributed Amplifiers [pp. 778–785]

### Balanced Amplifier [pp. 778–780]

A balanced amplifier uses two identical amplifiers and two 3-dB quadrature hybrids (Lange couplers or branch-line couplers):

```
        ┌─────────┐      ┌───────┐      ┌─────────┐
Port 1──┤ 3 dB 90°├──────┤ Amp 1 ├──────┤ 3 dB 90°├───Port 2
        │ Hybrid  │      ├───────┤      │ Hybrid  │
Port 4──┤ (Input) ├──────┤ Amp 2 ├──────┤ (Output)├───Port 3
        └─────────┘      └───────┘      └─────────┘
```

**Key advantages:**
- **VSWR improvement**: Reflections from individual amplifiers are absorbed by the hybrid loads, giving excellent input/output match even if the individual amplifiers are poorly matched
- **Gain redundancy**: If one amplifier fails, gain drops by ~6 dB but the system continues operating
- **Increased dynamic range**: 3 dB more output power capability
- **Wide bandwidth**: Limited primarily by the hybrids

The overall gain equals the gain of a single amplifier minus the hybrid loss (~0.3–0.5 dB per hybrid).

Input return loss:

$$S_{11}(total) = \frac{S_{11}^{(1)} - S_{11}^{(2)}}{2} \approx 0 \quad \text{(for identical amplifiers)} \tag{9.36}$$

where $S_{11}^{(1)} = \Gamma_1$ and $S_{11}^{(2)} = \Gamma_2$ are the input reflection coefficients of the two amplifiers.

### Distributed Amplifier [pp. 780–785]

A distributed amplifier (also called **traveling-wave amplifier**) combines the input and output capacitances of multiple transistors with artificial transmission lines:

```
Input ──┬── L/2 ──┬── L ──┬── ... ──┬── L/2 ──┬── Termination
        │         │       │          │         │
      Gate-1   Gate-2   Gate-3    Gate-n    Z_g
        │         │       │          │
      Drain-1  Drain-2  Drain-3   Drain-n
        │         │       │          │
Output ──┴── L/2 ──┴── L ──┴── ... ──┴── L/2 ──┴── Termination
                                                      Z_d
```

**Key characteristics:**
- **Wide bandwidth**: Gain-bandwidth product far exceeds that of a single transistor (up to decades of bandwidth)
- **Gain**: $G \approx \frac{n^2 g_m^2 Z_{0g} Z_{0d}}{4}$ for $n$ stages
- **Gain per stage**: ~3–5 dB per transistor for wideband designs
- **Cutoff frequency**: $f_c = 1/(\pi \sqrt{L C_{gs}})$ for the gate line
- **Noise figure**: Relatively high, typically > 5 dB

Gain roll-off is caused by:
1. Loss in the artificial transmission lines
2. Transistor $f_T$ limitations
3. Mismatch between gate and drain line phase velocities

The **optimum number of transistors** balances gain contribution against line losses:

$$n_{opt} \approx \frac{\ln(G_0/\alpha_d L_d)}{\alpha_g L_g + \alpha_d L_d} \tag{9.37}$$

where $\alpha_g$, $\alpha_d$ are attenuation constants of gate/drain lines and $L_g$, $L_d$ their lengths per section.

---

## Key Equations Summary

| Concept | Key Equation | Ref. |
|---------|-------------|------|
| Input ref. coeff. | $\Gamma_{in} = S_{11} + \frac{S_{12}S_{21}\Gamma_L}{1-S_{22}\Gamma_L}$ | p. 726 |
| Output ref. coeff. | $\Gamma_{out} = S_{22} + \frac{S_{12}S_{21}\Gamma_S}{1-S_{11}\Gamma_S}$ | p. 726 |
| Stability factor $K$ | $K = \frac{1 - \|S_{11}\|^2 - \|S_{22}\|^2 + \|\Delta\|^2}{2\|S_{12}S_{21}\|}$ | p. 735 |
| $ \|\Delta\|$ | $\|\Delta\| = \|S_{11}S_{22} - S_{12}S_{21}\|$ | p. 735 |
| MAG (unconditional) | $G_{max} = \frac{\|S_{21}\|}{S_{12}} (K - \sqrt{K^2 - 1})$ | p. 743 |
| Unilateral gain | $G_{TU} = \frac{\|S_{21}\|^2(1-\|\Gamma_S\|^2)(1-\|\Gamma_L\|^2)}{\|1-S_{11}\Gamma_S\|^2\|1-S_{22}\Gamma_L\|^2}$ | p. 746 |
| Unilateral figure of merit | $U = \frac{\|S_{12}\|\|S_{21}\|\|S_{11}\|\|S_{22}\|}{(1-\|S_{11}\|^2)(1-\|S_{22}\|^2)}$ | p. 747 |
| Noise figure equation | $F = F_{min} + \frac{4R_n}{Z_0}\frac{\|\Gamma_S - \Gamma_{opt}\|^2}{(1-\|\Gamma_S\|^2)\|1+\Gamma_{opt}\|^2}$ | p. 772 |
| Oscillation condition | $Z_{in} + Z_L = 0$ | p. 855 |
| Varactor $C(V)$ | $C_j(V) = C_{j0}/(1+V/V_j)^m$ | p. 800 |
| Manley-Rowe | $\sum \frac{mP_{m,n}}{mf_p+nf_s} = 0$, $\sum \frac{nP_{m,n}}{mf_p+nf_s} = 0$ | p. 807 |

---

## References

1. Collin, R.E., *Foundations for Microwave Engineering*, 2nd ed., IEEE Press, 2001, Chapter 10 (pp. 713–798), Chapter 11 (pp. 799–830), Chapter 12 (pp. 831–860).
2. Gonzalez, G., *Microwave Transistor Amplifiers: Analysis and Design*, 2nd ed., Prentice-Hall, 1997.
3. Vendelin, G.D., Pavio, A.M., and Rohde, U.L., *Microwave Circuit Design Using Linear and Nonlinear Techniques*, 2nd ed., Wiley, 2005.
4. Pozar, D.M., *Microwave Engineering*, 4th ed., Wiley, 2012, Chapter 10 (Amplifier Design), Chapter 11 (Oscillators).
5. Penfield, P. and Rafuse, R.P., *Varactor Applications*, MIT Press, 1962.
