---
title: "Chapter 6 — The Physical Basis of Inductance"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 6
pages: "180–235"
---

# Ch6: The Physical Basis of Inductance

## 6.1 Three Fundamental Principles

**Principle #1:** There are circular rings of magnetic-field lines around all currents. Counted in **Webers**. Direction by right-hand rule.

**Principle #2:** Inductance = number of Webers of field line rings around a conductor per Amp of current:

$$
L = \frac{\Psi}{I}
$$

Inductance is a **geometric property** — independent of current magnitude, depends only on conductor geometry and (for ferromagnetic materials) permeability.

**Principle #3:** When the number of field line rings around a conductor changes, a voltage is induced across its ends:

$$
V = \frac{d\Psi}{dt} = L\frac{dI}{dt}
$$

> **Engineering Intuition:** "An inductor resists a change in current." This induced voltage is the root cause of transmission line effects, cross talk, switching noise, rail collapse, ground bounce, and EMI.

## 6.2 Types of Inductance

| Type | Description | Measurable? |
|:--|:--|:--:|
| **Self-inductance** | Field rings from a wire's own current | ✓ (partial) |
| **Mutual inductance** | Field rings around one wire from another's current | ✓ (partial) |
| **Partial inductance** | Field rings around a segment, ignoring the rest of the loop | No (mathematical) |
| **Loop inductance** | Total field rings around the complete current loop | Yes |
| **Effective/net/total inductance** | Field rings around one leg of a loop, from all segments | Yes |
| **Equivalent inductance** | Combined inductance of series/parallel inductors with mutual | Yes |

## 6.3 Partial Self-Inductance

**Round rod approximation:**

$$
L \approx 5d\left[\ln\left(\frac{2d}{r}\right) - \frac{3}{4}\right] \quad \text{[nH]}
$$

$d$ = length (inches), $r$ = radius (inches).

**Rule of thumb:** ~25 nH/inch or ~1 nH/mm for a narrow wire.

**Example:** 1-inch, 10-mil diameter wire: $L \approx 26$ nH.

> **Engineering Intuition:** The more spread out the current distribution, the lower the partial self-inductance. Making wires wider reduces inductance; making them longer increases it faster than linearly.

## 6.4 Partial Mutual Inductance

Between two parallel round rods (same length $d$, center spacing $s$):

$$
M \approx 5d\left[\ln\left(\frac{2d}{s}\right) - 1 + \frac{s}{d} - \left(\frac{s}{2d}\right)^2\right] \quad \text{[nH]}
$$

**Rule of thumb:** If $s > d$, mutual inductance is <10% of self-inductance and can be ignored.

## 6.5 Effective Inductance and Ground Bounce

For a signal/return loop with legs $a$ and $b$:

$$
L_{\text{total},b} = L_b - L_{ab}
$$

**Ground bounce voltage** across the return path:

$$
V_{\text{gb}} = L_{\text{total}} \frac{dI}{dt}
$$

To **decrease ground bounce**:
1. Decrease $L_b$ (short, wide return path — use planes)
2. Increase $L_{ab}$ (bring signal and return paths closer together)

**Example:** Two 100-mil wire bonds, 1-mil diameter:
- $s = 100$ mils → $L_{\text{total}} \approx 2.5$ nH, $V_{\text{gb}} = 250$ mV (for 100 mA, 1 nsec)
- $s = 5$ mils → $L_{\text{total}} \approx 1.3$ nH, $V_{\text{gb}} = 130$ mV

> **Engineering Intuition:** For opposite-direction currents (signal+return): bring them close. For same-direction currents (multiple power wires): keep them apart (spacing ≥ length).

## 6.6 Loop Self-Inductance

**Circular loop:**

$$
L_{\text{loop}} \approx 32R\ln\left(\frac{4R}{D}\right) \quad [\text{nH}]
$$

$R$ = radius (inches), $D$ = wire diameter (inches).

**Rule of thumb:** A 1-inch finger-circle loop has $L \approx 85$ nH (~25 nH/inch of circumference).

**Two parallel rods (signal + return):**

$$
L_{\text{loop}} \approx 10 \cdot \text{len} \cdot \ln\left(\frac{s}{r}\right) \quad [\text{nH}]
$$

**Two wide planes ($w \gg h$):**

$$
L_{\text{loop}} \approx \mu_0 h \frac{\text{Len}}{w}
$$

$\mu_0 = 32$ pH/mil.

**Loop inductance per square of planes:** $L_{\text{sq}} = \mu_0 \cdot h$

| Spacing $h$ (mils) | $L_{\text{sq}}$ (pH) |
|:--:|:--:|
| 2 | 64 |
| 5 | 160 |
| 10 | 320 |

## 6.7 PDN and Decoupling Capacitor Inductance

**Required capacitance for decoupling time $\Delta t$ (5% droop):**

$$
C = \frac{1}{0.05} \cdot \frac{P}{V^2} \cdot \Delta t
$$

**Self-resonant frequency (SRF) of a real capacitor:**

Above SRF, impedance = $|Z| = \omega \cdot \text{ESL}$. To decrease high-frequency impedance, decrease **loop inductance** (ESL), not increase capacitance.

| Method to Reduce ESL | Effect |
|:--|:--|
| Short vias (planes near surface) | Major |
| Small body-size capacitors | Major |
| Short pad-to-via connections | Major |
| Multiple capacitors in parallel | Inverse with number |
| Closely spaced power/ground planes | Major |

> **Engineering Intuition:** At high frequency, ALL capacitors have the same impedance — determined solely by their mounting inductance. Six different capacitor values (10 pF to 1 µF) all converge to the same impedance above SRF.

## 6.8 Skin Depth and Current Distribution

**Skin depth in copper:**

$$
\delta = \frac{66\ \mu\text{m}}{\sqrt{f\ \text{(MHz)}}}
$$

| $f$ | $\delta$ in Cu | Effect on 1-oz Cu (35 $\mu$m) |
|:--:|:--:|:--|
| 1 MHz | 66 $\mu$m | Uniform current |
| 10 MHz | 21 $\mu$m | Skin-limiting begins |
| 100 MHz | 6.6 $\mu$m | Skin-depth regime |
| 1 GHz | 2.1 $\mu$m | Strong skin effect |

**High-frequency resistance:** $R_{\text{HF}} = \rho / (w \cdot \delta)$ increases as $\sqrt{f}$.

> **Engineering Intuition:** At AC, current takes the path of lowest impedance = lowest loop inductance. This pushes current to the outer surface of conductors and pulls signal and return currents together. A 5-mil-wide, 1-oz trace has 15× higher resistance at 1 GHz than at DC.

## 6.9 Eddy Currents

A changing current near a conducting plane induces **eddy currents** in the plane. These can be modeled as an **image current** at $h$ below the plane, opposite direction. The closer the plane, the lower the loop inductance — even if the plane is floating.

**Rule of thumb:** Eddy currents matter when spacing to the plane is less than the total conductor span.

## 6.10 High-Permeability Materials

Only iron, nickel, cobalt, and their alloys (Kovar, Alloy 42) have $\mu_r > 1$. They have:
- Much smaller skin depth (e.g., nickel: $\delta \approx 13\ \mu\text{m}/\sqrt{f}$)
- Much higher high-frequency resistance
- But the **high-frequency loop inductance** is the same as copper (external fields dominate)

> **Engineering Intuition:** A Ni/Au plating on traces doesn't affect electrical properties — current flows in the copper below. But solid Alloy 42 or Kovar leads have very high resistance at high frequencies.

## 6.11 Key Formulas

| Formula | Description |
|:--|:--|
| $L = \Psi / I$ | Inductance definition |
| $V = L \cdot dI/dt$ | Induced voltage |
| $V_{\text{noise}} = M \cdot dI/dt$ | Crosstalk from mutual inductance |
| $L_{\text{total},b} = L_b - L_{ab}$ | Total inductance of return path |
| $L_{\text{loop}} = L_a + L_b - 2L_{ab}$ | Loop inductance |
| $L_{\text{loop,sq}} = \mu_0 h$ | Loop inductance per square of planes |
| $\delta = \sqrt{1/(\pi f \mu \sigma)}$ | Skin depth |
| $\Delta t \approx C \cdot 0.05 V^2 / P$ | Decoupling time |
