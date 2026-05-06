---
title: "Chapter 4 — The Physical Basis of Resistance"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 4
pages: "142–153"
---

# Ch4: The Physical Basis of Resistance

## 4.1 Translating Physical Design into Electrical Performance

Modeling = translating physical design (width, length, thickness, material) into equivalent circuit elements (R, L, C).

> **Engineering Intuition:** The design process is intuitive. New ideas come from understanding the **meaning** of the equations, not from numerically solving them.

## 4.2 Resistance of a Uniform Conductor

For a conductor with **uniform cross section** down its length:

$$
R = \rho \cdot \frac{d}{A}
$$

where:
- $R$ = resistance (Ohms)
- $\rho$ = bulk resistivity (Ohm-cm)
- $d$ = length between ends (cm)
- $A$ = cross-sectional area (cm²)

**Example:** Gold wire bond, length = 0.2 cm (80 mils), diameter = 0.0025 cm (1 mil), $\rho_{\text{gold}} = 2.5\ \mu\Omega\text{-cm}$:

$$
R = 2.5\times10^{-6} \cdot \frac{0.2}{\pi/4 \cdot (0.0025)^2} \approx 0.1\ \Omega
$$

> **Engineering Intuition:** A 1-mil diameter wire bond, 80 mils long, has about 0.1 Ohm resistance. Resistance scales linearly with length, inversely with area — just like water flow through a pipe.

## 4.3 Bulk (Volume) Resistivity

**Bulk resistivity** $\rho$ is a fundamental material property (intrinsic), independent of the size of the conductor. Units: $\Omega$-cm or $\Omega$-inches.

**Conductivity** $\sigma = 1/\rho$, units: Siemens/meter.

| Material | $\rho$ ($\mu\Omega$-cm) | Uses |
|:--|:--:|:--|
| Silver | 1.47 | Best conductor |
| Copper | 1.58–4.5 | PCBs, wires (varies with processing) |
| Gold | 2.01 | Wire bonds |
| Aluminum | 2.61 | IC metallization |
| Solder (Pb/Sn) | 15 | Solder joints |
| Kovar | 49 | IC lead frames |

> **Engineering Intuition:** Copper resistivity varies 50%+ depending on processing (electroplated vs. rolled vs. annealed). If you need <10% accuracy, measure it.

## 4.4 Resistance per Length

For uniform cross-section conductors:

$$
R_L = \frac{R}{d} = \frac{\rho}{A}
$$

**Rule of thumb:** Wire bond resistance per length ≈ **1 Ohm/inch** (1-mil diameter gold wire).

| Wire (AWG) | Diameter (mils) | $R_L$ ($\Omega$/1000 ft) |
|:--:|:--:|:--:|
| 24 | 20.1 | 25.7 |
| 22 | 25.4 | 16.1 |
| 20 | 32.0 | 10.2 |
| 18 | 40.3 | 6.4 |

## 4.5 Sheet Resistance

For traces on a layer with uniform thickness $t$:

$$
R = \frac{\rho}{t} \cdot \frac{d}{w} = R_{\text{sq}} \cdot n
$$

where:
- $R_{\text{sq}} = \rho / t$ = **sheet resistance** (Ohms per square)
- $n = d/w$ = number of squares

> **Engineering Intuition:** Any square (any size) cut from the same sheet has the same resistance = $R_{\text{sq}}$. If you double both length and width, the resistance stays the same.

**Copper sheet resistance:**
| Copper weight | Thickness | $R_{\text{sq}}$ |
|:--|:--:|:--:|
| 1-oz | 1.4 mil (35 $\mu$m) | 0.5 m$\Omega$/sq |
| 1/2-oz | 0.7 mil (17.5 $\mu$m) | 1.0 m$\Omega$/sq |

**Rule of thumb:** $R_{\text{sq}}$ of 1/2-ounce copper = **1 m$\Omega$/sq**. A 5-mil-wide, 5-inch-long trace has $n = 5000/5 = 1000$ squares, so $R = 1\ \Omega$.

**Four-point probe measurement:** $R_{\text{sq}} = 4.53 \times R_{\text{meas}}$ (probes far from edges).

## 4.6 Resistance per Length vs. Line Width

| Line width (mils) | $R_L$, 1-oz Cu ($\Omega$/inch) | $R_L$, 1/2-oz Cu |
|:--:|:--:|:--:|
| 5 | 0.1 | 0.2 |
| 10 | 0.05 | 0.1 |
| 20 | 0.025 | 0.05 |

> **Engineering Intuition:** A 10-inch, 5-mil-wide trace in 1/2-oz Cu has $R = 0.2\ \Omega/\text{inch} \times 10 = 2\ \Omega$. At high frequencies, resistance increases due to skin effect (~$\sqrt{f}$).

## 4.7 Key Formulas

| Formula | Description |
|:--|:--|
| $R = \rho \cdot d / A$ | Uniform conductor resistance |
| $\sigma = 1/\rho$ | Conductivity from resistivity |
| $R_L = \rho / A$ | Resistance per length |
| $R_{\text{sq}} = \rho / t$ | Sheet resistance |
| $R = R_{\text{sq}} \cdot n$ | Trace resistance from sheet resistance |
| $n = d / w$ | Number of squares |
| $R_{\text{sq}} = 4.53 \cdot R_{\text{meas}}$ | Four-point probe extraction |
