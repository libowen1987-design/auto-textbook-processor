---
title: "Chapter 1 — Signal Integrity Is in Your Future"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 1
pages: "30–68"
---

# Ch1: Signal Integrity Is in Your Future

## 1.1 What Is Signal Integrity?

Signal integrity (SI) refers, in its broadest sense, to **all the problems that arise in high-speed products due to the interconnects**. It is about how the electrical properties of the interconnects, interacting with the digital signal's voltage and current waveforms, can affect performance.

The four families of SI noise problems:

1. **Signal quality on a single net** — reflections and distortions from impedance discontinuities
2. **Cross talk between multiple nets** — mutual C and mutual L coupling
3. **Rail collapse in the power distribution system (PDS/PDN)** — voltage drop across impedance in power/ground network
4. **Electromagnetic interference (EMI)** — radiation from components or system

> **Engineering Intuition:** When clock frequencies exceed ~100 MHz or rise times drop below ~1 nsec, interconnects are no longer "transparent" to signals. Every physical feature of the interconnect matters.

## 1.2 Signal Quality on a Single Net

A **net** includes all metal connected together (signal path + return path). As a signal propagates, it constantly "probes" the instantaneous impedance. If the impedance changes, part of the signal reflects, distorting the waveform.

**Impedance discontinuities** arise from:
- Line-width changes
- Layer changes through vias
- Gaps in return-path plane
- Connectors
- Branches, tees, or stubs
- End of a net (high-Z receiver or low-Z driver)

**Key strategy:** Keep the impedance the signal sees constant throughout the net via:
1. Controlled-impedance traces (uniform transmission lines)
2. Routing rules for constant impedance topology
3. Strategically placed termination resistors

**Rise-time dependence:** A discontinuity harmless at 33 MHz may be fatal at 100 MHz. Shorter rise times → larger distortions.

> **Engineering Intuition:** "Ringing" is almost always reflections from impedance changes, not an exotic phenomenon. Fix the impedance discontinuity and the ringing disappears.

### Rise Time vs. Clock Frequency (Rule of Thumb)

$$
RT \approx \frac{1}{10 \times F_{\text{clock}}}
$$

where:
- $RT$ = rise time (10–90%), in nsec
- $F_{\text{clock}}$ = clock frequency, in GHz

| $F_{\text{clock}}$ | $RT$ (approx) |
|:--:|:--:|
| 10 MHz | 10 nsec |
| 100 MHz | 1 nsec |
| 1 GHz | 100 psec |
| 10 GHz | 10 psec |

## 1.3 Cross Talk

When one net (active) carries a signal, unwanted voltage/current couples to an adjacent quiet net through **capacitive** and **inductive** coupling.

- **Near-end cross talk (NEXT):** dominates when traces have wide uniform return planes
- **Far-end cross talk (FEXT):** can be larger than NEXT in microstrip
- **Ground bounce / SSN / SSO noise:** occurs when return paths are not wide uniform planes (connectors, packages, vias) — dominated by **mutual inductance**

> **Engineering Intuition:** SSO noise is becoming one of the most critical issues in connectors and packages. The solution: minimize mutual inductance through careful geometry and use differential signaling.

## 1.4 Rail-Collapse Noise

When current through power/ground paths changes ($dI/dt$), a voltage drop occurs across the impedance of the PDN. This causes the voltage at the chip to **collapse**.

Trends making it worse:
- Lower supply voltages
- Higher current consumption (more gates switching faster)
- Tighter noise margins

**Target impedance** of the PDN (from Sun Microsystems estimate):

$$
Z_{\text{target}} = \frac{\text{Allowable ripple}}{\Delta I}
$$

| Year | Max PDN Impedance (Ω) |
|:--:|:--:|
| 1992 | ~0.1 |
| 1998 | ~0.01 |
| 2004 | ~0.001 |

**Solutions:**
- Closely spaced power/ground planes with thin dielectric
- Multiple low-ESL decoupling capacitors
- Short, low-inductance package leads
- On-chip decoupling capacitance
- Embedded capacitance materials (e.g., 3M C-Ply: 8 μm thick, $\epsilon_r = 20$)

> **Engineering Intuition:** The same physical designs that lower rail-collapse noise also lower EMI. There is no conflict between good PDN design and good EMI performance.

## 1.5 Electromagnetic Interference (EMI)

Three requirements for EMI:
1. **Source** of noise
2. **Pathway** to a radiator
3. **Antenna**

**Common EMI sources:**
- Conversion of differential → common signal on external cables
- Ground bounce generating common currents on shielded cables

**Mitigation:**
- Ferrite chokes on cables
- Shielded enclosures
- Low-impedance I/O connector return paths
- Good PDN design (same as rail-collapse solutions)

## 1.6 Two Important Generalizations

1. **All four families of SI problems get worse as rise times decrease.** Shorter $t_r$ → higher $dI/dt$, $dV/dt$.
2. **Effective solutions are based on understanding impedance of interconnects.** Relating physical design to impedance is the key skill.

## 1.7 Trends in Electronic Products

- Intel processor clock frequencies double ~every 2 years (from ~1 MHz in 1971 to >3 GHz in 2000s)
- ITRS roadmap projects continued growth
- Even **low clock-frequency products** get short rise times due to finer fab processes (Moore's Law "scary consequence")
- High-speed serial links: OC-48 (2.5 Gbps) → OC-192 (10 Gbps) → OC-768 (40 Gbps)
- Serial buses: PCIe, Infiniband, Serial ATA, XAUI, Gigabit Ethernet all migrating to multi-Gbps

> **Engineering Intuition:** If your chip vendor migrates to a finer process node, the rise time of your "same" chip may drop, silently introducing SI problems even if the clock frequency hasn't changed.

## 1.8 Need for a New Design Methodology

**The old way:** Build it → test it → redesign it (too slow).
**The new way:** Predict performance early through modeling and simulation → design it right the first time.

Five key ingredients:
1. Understand root causes of SI problems
2. Translate into specific design rules
3. Predict performance early via modeling and simulation
4. Optimize design at every step
5. Use measurements for risk reduction

## 1.9 Simulation Tools

Three types:

1. **Electromagnetic (EM) simulators** — solve Maxwell's equations, model fields (HFSS, etc.)
   - Necessary for: resonances, nonuniform wave propagation, EMI
   - Disadvantage: slow, requires skilled user

2. **Circuit simulators (SPICE)** — solve differential equations of circuit elements
   - Popular: HSPICE, PSPICE, LTSPICE
   - Good for: transmission lines, cross talk, switching noise
   - Limitation: cannot handle EMI or resonances directly

3. **Behavioral simulators** — use tables/transfer functions
   - Advantage: fast computation
   - Used for: system-level simulation with IBIS models

### Maxwell's Equations (for reference)

**Time domain:**
$$
\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0} \quad
\nabla \cdot \mathbf{B} = 0 \quad
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \quad
\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}
$$

**Frequency domain ($e^{j\omega t}$ convention):**
$$
\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0} \quad
\nabla \cdot \mathbf{H} = 0 \quad
\nabla \times \mathbf{E} = -j\omega\mu\mathbf{H} \quad
\nabla \times \mathbf{H} = \mathbf{J} + j\omega\epsilon\mathbf{E}
$$

## 1.10 Modeling

**Active device models:**
- **SPICE models:** contain transistor geometry details (vendors reluctant to share)
- **IBIS models:** V-I and V-t curves, no proprietary info (easier to obtain)

**Passive interconnect models:** R, L, C, transmission lines

> **Engineering Intuition:** "Garbage in, garbage out" applies to SI simulation. The model quality is the single most important factor determining simulation accuracy. Always demand vendor verification.

## 1.11 Creating Circuit Models from Calculation

Three levels of approximation:

| Level | Accuracy | Effort | Use Case |
|:--|:--:|:--:|:--|
| Rules of thumb | Low (order-of-magnitude) | Very low | Sanity checks, intuition |
| Analytical approximations | Moderate (2–50%) | Low | Spreadsheet trade-offs |
| Numerical simulations (field solvers) | High (<1–2%) | High | Design sign-off |

### Example: Loop Self-Inductance Approximation

$$
L_{\text{self}} \approx 32 \cdot R \cdot \ln\left(\frac{4R}{D}\right) \quad \text{[nH]}
$$

where $R$ = loop radius (inches), $D$ = wire diameter (inches). Verified to ~2% accuracy against measurements.

### Field Solvers
- **2D field solvers:** for uniform cross-section transmission lines (e.g., microstrip, stripline)
- **3D field solvers:** for nonuniform structures (connectors, packages)

## 1.12 Measurements

Three primary instruments:

| Instrument | Domain | Frequency Range | What It Measures |
|:--|:--:|:--:|:--|
| Impedance Analyzer | Frequency | 100 Hz – 40 MHz | $Z(\omega) = V/I$ |
| Vector Network Analyzer (VNA) | Frequency | kHz – 50+ GHz | S-parameters ($S_{11} \to Z_{\text{DUT}}$) |
| Time-Domain Reflectometer (TDR) | Time | DC – multi-GHz | Instantaneous impedance vs. position |

**Reflection coefficient (VNA):**
$$
\frac{V_{\text{reflected}}}{V_{\text{incident}}} = \frac{Z_{\text{DUT}} - 50\,\Omega}{Z_{\text{DUT}} + 50\,\Omega} = S_{11}
$$

> **Engineering Intuition:** Frequency-domain impedance is the *integrated* impedance of the entire DUT at each frequency. Time-domain impedance (TDR) shows the *spatial* impedance profile along the interconnect.

## 1.13 Role of Measurements

Measurements serve five critical roles, all related to **risk reduction**:
1. Verify accuracy of the design/simulation process
2. Verify as-fabricated components meet specs
3. Create equivalent electrical models
4. Emulate system performance
5. Debug functional parts

> **Engineering Intuition:** The Delphi Electronics case study shows that a verified modeling process reduced connector design cycle from 9 weeks to 4 hours — a >100× improvement. The key was using TDR/VNA measurements to validate the model, then relying on the model for all future designs.

## 1.14 Key Rules of Thumb

1. **Rise time vs. clock frequency:** $RT \approx 1/(10 \cdot F_{\text{clock}})$ [nsec for GHz]
2. **SI problems appear** when $RT < 1$ nsec or $F_{\text{clock}} > 100$ MHz
3. **Loop inductance of a wire:** ~25 nH/inch
4. **Critical net threshold:** at 100 MHz ~5–10% of nets; at 200 MHz+ >50% of nets
5. **PDN target impedance:** decreases ~10× every 6 years

## 1.15 Checklist for Designers

- [ ] Identify all nets with rise times < 1 nsec
- [ ] Ensure controlled-impedance traces for critical nets
- [ ] Minimize impedance discontinuities (vias, layer changes, stubs)
- [ ] Space traces adequately to manage cross talk
- [ ] Design PDN for target impedance across frequency range
- [ ] Place decoupling capacitors with lowest possible ESL
- [ ] Use ferrites on external cables
- [ ] Verify models (IBIS/SPICE) are current and accurate
- [ ] Validate simulations with measurements (TDR/VNA)
