---
title: "Chapter 5 — The Physical Basis of Capacitance"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 5
pages: "156–179"
---

# Ch5: The Physical Basis of Capacitance

## 5.1 Current Flow in Capacitors

Capacitance: measure of the capacity to store charge between two conductors at the cost of voltage:

$$
C = \frac{Q}{V}
$$

**Displacement current:** Current appears to flow through a capacitor only when the voltage changes:

$$
I = \frac{dQ}{dt} = C \frac{dV}{dt}
$$

> **Engineering Intuition:** Even though there's no DC path between conductors, capacitance provides an AC sneak path. This is the root of cross talk and many SI problems.

## 5.2 Capacitance of a Sphere

An isolated conductor has a **minimum** capacitance to "infinity" (earth/chassis):

$$
C \approx 4\pi\epsilon_0 r
$$

**Rule of thumb:** A sphere with 1-inch diameter has $C \approx 2$ pF.

At 1 GHz, $|Z_C| = 1/(2\pi \times 10^9 \times 2\times10^{-12}) \approx 80\ \Omega$ — significant!

> **Engineering Intuition:** Any conductor sticking out of a chassis has at least ~2 pF stray capacitance. At GHz frequencies, this is a low-impedance path.

## 5.3 Parallel Plate Approximation

$$
C = \frac{\epsilon_0 \epsilon_r A}{h}
$$

where $\epsilon_0 = 0.089$ pF/cm = 0.225 pF/inch.

**Example:** Penny-sized plates (1 cm²) separated by 1 mm:
$$C = 0.089 \times 1 / 0.1 = 0.9\ \text{pF}$$

**Limitations:** Underestimates true capacitance by up to 2× when $h \approx w$ (fringe fields).

## 5.4 Dielectric Constant

The relative dielectric constant $\epsilon_r$ (or Dk) increases capacitance:

$$
\epsilon_r = \frac{C_{\text{filled}}}{C_{\text{air}}}
$$

| Material | $\epsilon_r$ | Notes |
|:--|:--:|:--|
| Air | 1.0 | Reference |
| Teflon (PTFE) | 2.1 | Lowest solid |
| Polyethylene | 2.3 | Coax cable |
| FR4 | 4.0–4.5 | PCB laminate (varies with resin/glass ratio) |
| Alumina | 9–10 | Ceramic packages |
| Water | ~80 | High dipole density |
| Barium titanate | ~5000 | High-Dk ceramic |

> **Engineering Intuition:** FR4's Dk varies from ~4.8 at 1 kHz to ~4.4 at 10 MHz. Always specify frequency. If you need <10% accuracy, measure your specific sample.

## 5.5 Power/Ground Plane Capacitance

**Parallel plate between power and ground planes:**

$$
C = \frac{\epsilon_0 \epsilon_r A}{h}
$$

For FR4 ($\epsilon_r \approx 4$), 10 mil spacing:
$$C \approx 1000\ \text{pF/in}^2 / h_{\text{mils}}$$

| Spacing | Capacitance per in² |
|:--:|:--:|
| 10 mil FR4 | 100 pF/in² |
| 2 mil FR4 | 500 pF/in² |
| C-Ply (8 $\mu$m, $\epsilon_r$=20) | 14 nF/in² |

**Decoupling time** (before 5% droop):

$$
\Delta t \approx \frac{C \times 0.05 \times V^2}{P}
$$

**Example:** 4 in² of 10-mil FR4 planes → only 0.4 nF → decouples a 1W 3.3V chip for only **0.2 nsec**.

> **Engineering Intuition:** The primary value of power/ground planes is **low loop inductance**, NOT decoupling capacitance. The plane capacitance is typically 4+ orders of magnitude too small for bulk decoupling.

## 5.6 Capacitance per Length — Uniform Cross Sections

**50-Ohm transmission line rule of thumb:** $C_L \approx 3.5$ pF/inch.

**Exact formulas:**

| Geometry | $C_L$ |
|:--|:--|
| **Coax** | $\dfrac{2\pi\epsilon_0\epsilon_r}{\ln(b/a)}$ |
| **Twin rods** | $\dfrac{\pi\epsilon_0\epsilon_r}{\cosh^{-1}(s/2r)}$ or $\dfrac{\pi\epsilon_0\epsilon_r}{\ln(s/r)}$ for $s \gg r$ |
| **Rod over plane** | $\dfrac{2\pi\epsilon_0\epsilon_r}{\ln(2h/r)}$ |
| **Microstrip (IPC approx)** | $\dfrac{0.67(1.41 + \epsilon_r)}{\ln(5.98h/(0.8w + t))}$ |
| **Stripline (IPC approx)** | $\dfrac{1.4\epsilon_r}{\ln(2.4b/(0.8w + t))}$ |

**Example RG58 coax:** $b/a = 3$, $\epsilon_r = 2.3$ → $C_L = 2.9$ pF/inch.

## 5.7 2D Field Solvers

Only accurate way (<1% error) for arbitrary cross sections with non-homogeneous dielectrics. The **effective dielectric constant** captures the mixed dielectric environment:

$$
\epsilon_{\text{eff}} = \frac{C_{\text{filled}}}{C_{\text{air}}}
$$

For microstrip:
- Wide traces → $\epsilon_{\text{eff}} \to \epsilon_r$ (fields mostly in dielectric)
- Narrow traces → $\epsilon_{\text{eff}} \ll \epsilon_r$ (fields partly in air)
- Top coating ≈ trace width needed to fully enclose fields

> **Engineering Intuition:** IPC approximations can be off by 20%+. Never trust an approximation for sign-off. Use a verified 2D field solver.

## 5.8 Key Formulas

| Formula | Description |
|:--|:--|
| $C = Q/V$ | Definition of capacitance |
| $I = C \cdot dV/dt$ | Displacement current |
| $C = \epsilon_0 \epsilon_r A/h$ | Parallel plate approximation |
| $\epsilon_r = C_{\text{filled}}/C_{\text{air}}$ | Dielectric constant definition |
| $\Delta t \approx 0.05 \cdot C \cdot V^2 / P$ | Decoupling time (5% droop) |
| $C_L \approx 3.5$ pF/inch | 50-$\Omega$ line rule of thumb |
| $\epsilon_{\text{eff}} = C_{\text{filled}}/C_{\text{air}}$ | Effective dielectric constant |
