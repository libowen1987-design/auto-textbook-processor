---
title: "Chapter 7 — The Physical Basis of Transmission Lines"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 7
pages: "238–308"
---

# Ch7: The Physical Basis of Transmission Lines

## Key Definitions

**Transmission line:** Any two conductors with length. One is the **signal path**, the other the **return path** (never call it "ground").

**Uniform (controlled-impedance) line:** Cross section is constant down the length.

**Balanced line:** Both conductors have the same shape/size (twisted pair, coplanar).
**Unbalanced line:** Conductors differ (microstrip, coax, stripline).

> **Engineering Intuition:** Forget the word "ground." Use "return path." The return current follows the signal current path — it has no idea what voltage level the return conductor is at.

## 7.1 Signal Speed

**Speed of electrons in copper:** ~1 cm/sec (about as fast as an ant crawls). Has **nothing** to do with signal speed.

**Speed of signal (electromagnetic wave) in a transmission line:**

$$
v = \frac{1}{\sqrt{\epsilon_0 \epsilon_r \mu_0 \mu_r}} = \frac{c}{\sqrt{\epsilon_r \mu_r}} \approx \frac{12\ \text{in/nsec}}{\sqrt{\epsilon_r}}
$$

**Rules of thumb:**
- In air ($\epsilon_r = 1$): $v = 12$ inches/nsec (speed of light)
- In FR4 ($\epsilon_r \approx 4$): $v \approx 6$ inches/nsec
- Wiring delay in FR4: **170 psec/inch**

## 7.2 Spatial Extent of the Leading Edge

$$
d = RT \times v
$$

| Rise Time (nsec) | Spatial Extent (FR4) |
|:--:|:--:|
| 1.0 | 6 inches |
| 0.5 | 3 inches |
| 0.1 | 0.6 inch |
| 0.05 | 0.3 inch |

> **Engineering Intuition:** SI problems from discontinuities depend on their size compared to the spatial extent of the leading edge.

## 7.3 Characteristic Impedance

**Zeroth-order model:** The signal sees instantaneous impedance as it charges up capacitance per length while propagating at speed $v$:

$$
Z_0 = \frac{1}{v \cdot C_L} = \frac{83 \cdot \sqrt{\epsilon_r}}{C_L}
$$

where $C_L$ is in pF/inch. For a 50-$\Omega$ line in FR4: $C_L \approx 3.3$ pF/inch, $C_L \times Z_0 \approx 166$ pF/inch.

**Alternative form (from LL and CL):**

$$
Z_0 = \sqrt{\frac{L_L}{C_L}}, \quad v = \frac{1}{\sqrt{L_L \cdot C_L}}
$$

**Famous characteristic impedances:**
| Interconnect | $Z_0$ |
|:--|:--:|
| Free space | 377 $\Omega$ |
| RG58 coax | 52 $\Omega$ |
| RG59 coax (CATV) | 75 $\Omega$ |
| Twisted pair | 100–130 $\Omega$ |
| PCB microstrip | 50–75 $\Omega$ (typical) |
| PCB power/ground planes | <1 $\Omega$ |
| Rambus | 28 $\Omega$ |

**Why 50 $\Omega$?** Minimum attenuation in coax for a fixed outer diameter — established in 1930s for radio/radar.

> **Engineering Intuition:** The input impedance of a line is **time-dependent**. During the round-trip time of flight ($2 \times TD$), the driver sees $Z_0$. After that, it sees whatever terminates the far end.

## 7.4 Driving a Transmission Line

**Voltage divider:** The launched voltage:

$$
V_{\text{launched}} = V_{\text{output}} \cdot \frac{Z_0}{R_{\text{source}} + Z_0}
$$

For $Z_0 = 50\ \Omega$, $V_{\text{output}} = 3.3\ \text{V}$:
- $R_s = 5\ \Omega$: $V_{\text{launched}} = 3.0$ V (91%)
- $R_s = 50\ \Omega$: $V_{\text{launched}} = 1.65$ V (50%)
- $R_s = 100\ \Omega$: $V_{\text{launched}} = 1.1$ V (33%)

> **Engineering Intuition:** To drive a line (launch most of the voltage), the driver's output impedance must be much less than $Z_0$ — typically <10 $\Omega$.

## 7.5 Return Paths

- Current travels in **complete loops**.
- Return current flows **through distributed capacitance** between signal and return paths — only where the signal voltage is changing ($dV/dt$).
- The return current in a plane is concentrated **underneath the signal trace** (Fig 7-20). At >100 kHz, it's highly localized.
- **Any gap in the return path** increases loop inductance → higher instantaneous impedance → signal distortion.

**When return path switches reference planes:**
- If planes are DC-coupled: use a return via adjacent to the signal via.
- If planes are DC-isolated: return current couples through plane-to-plane capacitance.
- The impedance the return current sees between planes decreases with distance from the via:

$$
Z_{\text{return}}(t) \approx \frac{5 \cdot h}{t}
$$

where $h$ = plane spacing in mils, $t$ = time in nsec.
- At $t = 0.1$ nsec, $h = 10$ mils: $Z_{\text{return}} \approx 0.5\ \Omega$
- 10 simultaneous switching signals × 20 mA each = 200 mA × 0.5 $\Omega$ = 100 mV ground bounce

## 7.6 Characteristic Impedance of Planes

For wide planes ($w \gg h$):

$$
Z_0 \approx \frac{377\ \Omega}{\sqrt{\epsilon_r}} \cdot \frac{h}{w}
$$

## 7.7 Key Rules of Thumb

| Rule | Value |
|:--|:--|
| Speed of light (air) | 12 in/nsec |
| Speed of light (FR4) | 6 in/nsec |
| Wiring delay (FR4) | 170 psec/inch |
| $C_L$ for 50-$\Omega$ line | 3.3 pF/inch |
| $L_L$ for 50-$\Omega$ line | 8.3 nH/inch |
| $C_L \times Z_0$ (FR4) | 166 pF/inch |
| Round-trip delay (6-inch trace) | ~2 nsec |
| Signal sees $Z_0$ as resistive load | for $t < 2 \times TD$ |

## 7.8 Return Path Design Guidelines

- Use adjacent power/ground planes with thin dielectric for low plane impedance
- Place return vias adjacent to signal vias when switching layers
- Keep return paths continuous (no gaps, slots, or splits)
- When planes must be DC-isolated, keep them tightly coupled (thin dielectric)
- Route signal traces over continuous reference planes
