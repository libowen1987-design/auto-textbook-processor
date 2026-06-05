---
chapter: 4
title: Transmission Lines and Signal Integrity
source: Paul, Clayton R. *Introduction to Electromagnetic Compatibility*, 2nd Ed., Wiley, 2006
pages: 177-322
---

# Chapter 4: Transmission Lines and Signal Integrity

## 4.1 The Transmission-Line Equations

For a uniform two-conductor transmission line (lossless):

$$\frac{\partial V(z,t)}{\partial z} = -l \frac{\partial I(z,t)}{\partial t} \tag{4.2a}$$

$$\frac{\partial I(z,t)}{\partial z} = -c \frac{\partial V(z,t)}{\partial t} \tag{4.2b}$$

where:
- $l$ = per-unit-length inductance (H/m)
- $c$ = per-unit-length capacitance (F/m)

### Uncoupled Wave Equations

Combining (4.2a) and (4.2b) gives the one-dimensional wave equation:

$$\frac{\partial^2 V(z,t)}{\partial z^2} = lc \frac{\partial^2 V(z,t)}{\partial t^2} \tag{4.3a}$$

$$\frac{\partial^2 I(z,t)}{\partial z^2} = lc \frac{\partial^2 I(z,t)}{\partial t^2} \tag{4.3b}$$

**General solution (D'Alembert):**

$$V(z,t) = V^+\!\left(t - \frac{z}{v}\right) + V^-\!\left(t + \frac{z}{v}\right)$$

$$I(z,t) = \frac{1}{Z_C} V^+\!\left(t - \frac{z}{v}\right) - \frac{1}{Z_C} V^-\!\left(t + \frac{z}{v}\right)$$

### Key Parameters

| Parameter | Formula | Units |
|---|---|---|
| Velocity | $v = 1/\sqrt{lc}$ | m/s |
| Characteristic Impedance | $Z_C = \sqrt{l/c}$ | $\Omega$ |
| Time Delay | $T_D = L/v = L\sqrt{lc}$ | s |

### Homogeneous Medium (lc = με)
When the dielectric is uniform around the conductors (e.g., coax, stripline):

$$v = \frac{1}{\sqrt{lc}} = \frac{1}{\sqrt{\mu\varepsilon}} = \frac{c_0}{\sqrt{\varepsilon_r}}$$

$$lc = \mu\varepsilon \quad \text{(important check relation)}$$

## 4.2 Per-Unit-Length Parameters

### 4.2.1 Two-Wire Line

**Approximate form** (widely spaced, $s/r_w > 5$):

$$l = \frac{\mu_0}{\pi} \ln\left(\frac{s}{r_w}\right) \quad \text{(H/m)}$$

$$c = \frac{\pi\varepsilon_0}{\ln(s/r_w)} \quad \text{(F/m)}$$

$$Z_C = \frac{120}{\sqrt{\varepsilon_r}} \ln\left(\frac{s}{r_w}\right) \quad (\Omega)$$

**Exact form:**

$$l = \frac{\mu_0}{\pi} \cosh^{-1}\left(\frac{s}{2r_w}\right) \quad c = \frac{\pi\varepsilon_0}{\cosh^{-1}(s/2r_w)}$$

### 4.2.2 Wire Above Ground Plane

$$c = \frac{2\pi\varepsilon_0}{\cosh^{-1}(h/r_w)} \xrightarrow{h \gg r_w} \frac{2\pi\varepsilon_0}{\ln(2h/r_w)}$$

$$l = \frac{\mu_0}{2\pi} \cosh^{-1}\left(\frac{h}{r_w}\right) \xrightarrow{h \gg r_w} \frac{\mu_0}{2\pi} \ln\left(\frac{2h}{r_w}\right)$$

$$Z_C = \frac{60}{\sqrt{\varepsilon_r}} \ln\left(\frac{2h}{r_w}\right) \quad (\Omega)$$

### 4.2.3 Coaxial Cable

$$l = \frac{\mu_0}{2\pi} \ln\left(\frac{r_s}{r_w}\right) \quad c = \frac{2\pi\varepsilon_0\varepsilon_r}{\ln(r_s/r_w)}$$

$$Z_C = \frac{60}{\sqrt{\varepsilon_r}} \ln\left(\frac{r_s}{r_w}\right) \quad (\Omega)$$

### 4.2.4 Stripline (PCB Inner Layer)

$$Z_C = \frac{60}{\sqrt{\varepsilon_r}} \ln\left(\frac{4h}{0.67\pi w(0.8 + t/w)}\right) \quad (\Omega)$$

### 4.2.5 Microstrip (PCB Outer Layer)

Effective permittivity accounts for mixed air/dielectric fields:

$$\varepsilon_{\text{eff}} = \frac{\varepsilon_r + 1}{2} + \frac{\varepsilon_r - 1}{2} \frac{1}{\sqrt{1 + 12h/w}}$$

$$Z_C = \frac{60}{\sqrt{\varepsilon_{\text{eff}}}} \ln\left(\frac{8h}{w} + \frac{w}{4h}\right) \quad w/h < 1$$

$$Z_C = \frac{120\pi}{\sqrt{\varepsilon_{\text{eff}}}[w/h + 1.393 + 0.667\ln(w/h + 1.444)]} \quad w/h \ge 1$$

## 4.3 Reflection and Transmission

### Reflection Coefficients

$$\Gamma_L = \frac{Z_L - Z_C}{Z_L + Z_C} \quad \Gamma_S = \frac{Z_S - Z_C}{Z_S + Z_C}$$

- $\Gamma = 0$: matched (no reflection)
- $\Gamma = 1$: open circuit
- $\Gamma = -1$: short circuit
- $\Gamma = j|\Gamma|$: reactive load

### Voltage Standing Wave Ratio (VSWR)

$$\text{VSWR} = \frac{1 + |\Gamma|}{1 - |\Gamma|} = \frac{V_{\max}}{V_{\min}}$$

- VSWR = 1: perfect match
- VSWR = ∞: open/short

## 4.4 Time-Domain Response: Bounce Diagrams

The bounce (lattice) diagram method traces incident and reflected waves:

### Source and Load Voltage Series Form

$$V(0,t) = \frac{Z_C}{R_S + Z_C}\left[V_S(t) + (1 + \Gamma_S)\Gamma_L V_S(t - 2T_D) + (1 + \Gamma_S)(\Gamma_S\Gamma_L)\Gamma_L V_S(t - 4T_D) + \cdots\right]$$

$$V(L,t) = \frac{Z_C}{R_S + Z_C}\left[(1 + \Gamma_L)V_S(t - T_D) + (1 + \Gamma_L)\Gamma_S\Gamma_L V_S(t - 3T_D) + \cdots\right]$$

### Matched Load ($R_L = Z_C$, $\Gamma_L = 0$)

$$V(0,t) = \frac{Z_C}{R_S + Z_C} V_S(t)$$

$$V(L,t) = \frac{Z_C}{R_S + Z_C} V_S(t - T_D)$$

The only effect is a time delay — the line "doesn't matter."

## 4.5 Signal Integrity Criteria

### When Does the Line Matter?

The critical length threshold:

$$L_{\text{crit}} = \frac{t_r}{2 \cdot t_{pd}} \approx \frac{t_r}{2} \cdot v$$

**Rule of thumb:** If the line length exceeds $L_{\text{crit}}$, transmission line effects (ringing, reflections) must be considered.

Typical delays:
| PCB Type | $t_{pd}$ (ps/in) | $L_{\text{crit}}$ for $t_r = 1$ ns |
|---|---|---|
| Air wire | 85 | ~6 in |
| Microstrip (FR-4) | ~160 | ~3 in |
| Stripline (FR-4) | 183 | ~2.7 in |

### Eye Diagram Metrics

| Parameter | Definition | Typical Spec |
|---|---|---|
| Eye height | $V_{\text{OH}} - V_{\text{OL}}$ | > 200 mV |
| Eye width | Time window where eye is open | > 60% UI |
| Jitter (p-p) | Edge variation | < 30% $t_r$ |
| Overshoot | Peak above steady-state | < 20% |

## 4.6 Termination Strategies

| Termination | Circuit | Pros | Cons |
|---|---|---|---|
| **Series** | $R_S$ in series at driver | Low power, simple | Signal division |
| **Parallel** | $R_L$ to GND at receiver | Clean signal | DC power loss |
| **Thevenin** | $R_1\|R_2 = Z_C$ at receiver | No DC block | DC power |
| **AC** | $R + C$ in parallel | Low power | AC coupling |
| **Diode clamp** | Schottky to VDD/GND | Clamp overshoot | No impedance match |

**Series termination** $R_S = Z_C - Z_{\text{driver out}}$ is the most common for CMOS point-to-point links.

## 4.7 The SPICE Transmission Line Model

The lossless T-element in SPICE:

```
TXXX N1 N2 N3 N4 Z0=<Z0> TD=<TD>
```

- Port 1: N1-N2 (input)
- Port 2: N3-N4 (output)
- $Z_0$ = characteristic impedance
- $T_D$ = one-way time delay

### Branin Equivalent Circuit

The SPICE T-model uses controlled sources with time delay:

$$V(0,t) = Z_C I(0,t) + \underbrace{V(L, t - T_D) - Z_C I(L, t - T_D)}_{E_0(L, t - T_D)}$$

$$V(L,t) = -Z_C I(L,t) + \underbrace{V(0, t - T_D) + Z_C I(0, t - T_D)}_{E_L(0, t - T_D)}$$

This exact circuit is valid for **lossless** lines with **linear** terminations.

## 4.8 Discontinuities and Impedance Variations

### Impedance discontinuity (step change):

$$V_{\text{transmitted}} = V_{\text{incident}} \cdot \frac{2Z_{C2}}{Z_{C1} + Z_{C2}}$$

$$V_{\text{reflected}} = V_{\text{incident}} \cdot \frac{Z_{C2} - Z_{C1}}{Z_{C1} + Z_{C2}}$$

### Common discontinuities:
- Vias (layer transition): ~1–3 pF parasitic capacitance
- Connectors: ~0.5–1 nH parasitic inductance
- Stubs: cause reflections; keep unterminated stubs < $t_r/10$

## 4.9 Differential Pairs

| Parameter | Single-ended | Differential |
|---|---|---|
| Impedance | $Z_0$ | $Z_{\text{diff}} \approx 2Z_0(1 - k)$ |
| Return current | GND plane | Complementary signal |
| Common-mode rejection | N/A | Inherent |

Differential impedance with line spacing $s$ and height $h$:

$$Z_{\text{diff}} = 2Z_0\left(1 - 0.48 e^{-0.96 s/h}\right)$$

### Key design rules for differential pairs:
- Maintain constant coupling (keep $s$ constant)
- Route both lines identically (matched delay)
- Avoid vias on one line without the other
- Use ground vias near differential via transitions

## 4.10 Engineering Intuition

1. **Lossless line approximation** is usually valid for PCB traces up to a few GHz — conductor and dielectric losses matter only for long backplane traces.

2. **50 $\Omega$ is a convention**, not a law. In digital CMOS, line impedance matching should be done for signal quality, not for power transfer.

3. **The characteristic impedance depends on geometry, not length.** A 1 cm trace has the same $Z_C$ as a 1 m trace.

4. **Rise time degradation:** A line with loss increases $t_r$. The bandwidth of a lossy line section is approximately $BW \approx 0.35/t_r$.

5. **The $t_r/6$ rule** for electrically short lines: if $L < t_r/(6 \cdot t_{pd})$, the line can be treated as a lumped element.
