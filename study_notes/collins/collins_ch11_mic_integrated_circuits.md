# Collins Chapter 11 — Microwave Integrated Circuits & Antennas

> 📡 **Final Chapter — Collins Microwave Engineering, 2nd Ed.**
> Synthesized from Collins §§3.12–3.13 (planar transmission lines), §5.3 (lumped elements),
> §10.1–10.11 (solid-state devices & amplifiers), plus standard MMIC/antenna references.

---

## 11.1 MIC Technology: Substrates, Fabrication, and MMIC

### 11.1.1 What is a Microwave Integrated Circuit?

A **microwave integrated circuit (MIC)** integrates transmission lines, matching elements,
capacitors, resistors, and active devices on a common substrate. Two main forms exist:

| Type | Description | Key References |
|------|-------------|----------------|
| **Hybrid MIC** | Transmission lines & passives on substrate; discrete actives soldered in place | Collins §10 intro |
| **Monolithic MIC (MMIC)** | All components (active + passive) fabricated on a single semiconductor chip | Collins §10, §3.12 |

> **Monolithic** — from Greek *monos* (single) + *lithos* (stone). Everything on one chip.

### 11.1.2 Substrate Materials

Collin Table 3.2 summarizes key substrates:

| Material | εᵣ | Loss Tangent | Thermal Cond. | Notes |
|----------|-----|-------------|---------------|-------|
| **PTFE/woven glass** (Teflon) | 2.84 | 0.001–0.002 | Fair | Low cost, common for hybrid MIC |
| **PTFE/microfiberglass** (RT/Duroid 5880) | 2.26 | 0.0005–0.001 | Fair | Low loss, good for high frequencies |
| **Alumina (Al₂O₃)** | 9.6–10.1 | 0.0001 | Excellent | Most common; good thermal conductivity |
| **Gallium Arsenide (GaAs)** | 12.9 | 0.0005–0.001 | Medium | Substrate for MMIC; semi-insulating |
| **Silicon (Si)** | 11.7–12.9 | — | Medium | Low cost; lossy at high ρ without high resistivity |
| **Sapphire** | 9.4 | 0.0001 | Good | Low loss, expensive |
| **Beryllium Oxide (BeO)** | 6.7 | 0.0004 | Excellent | High-power applications (toxic dust) |

**Key substrate requirements** (Collin §3.12):
- Low loss tangent (tan δ < 0.001)
- High εᵣ → shorter guided wavelength → more compact circuits
- Good thermal conductivity for power dissipation
- Mechanical strength and ease of machining
- Uniform thickness and dielectric constant across wafer

### 11.1.3 Fabrication Processes

| Process | Application |
|---------|------------|
| **Photolithography** | Define conductor patterns (strip widths, gaps) |
| **Ion Implantation** | Create active device regions in MMIC |
| **Metal Deposition & Evaporation** | Ohmic contacts, transmission lines |
| **Via Hole Etching & Plating** | Ground connections through substrate |
| **Dielectric Deposition** | MIM capacitors, passivation |
| **Electron-Beam Lithography** | Submicron features (gate lengths < 0.1 μm) |
| **Plasma-Enhanced Etching** | Precise pattern definition |
| **Molecular Beam Epitaxy (MBE)** | Grow heterostructures for HEMT/HBT |

**Hybrid vs MMIC tradeoffs** (Collin §10 intro):
- **Below ~10 GHz**: Hybrid often cheaper (distributed elements are large, wafer cost high)
- **0.1–10 GHz**: Miniature lumped elements enable MMIC with compact size
- **Millimeter-wave**: MMIC becomes cost-effective due to small size and reliability benefits

> Cost equation: `cost_per_chip = wafer_processing_cost / chips_per_wafer`

---

## 11.2 Planar Transmission Lines for MICs

### 11.2.1 Microstrip Line

The dominant planar transmission line for MICs. A conducting strip of width W on a
dielectric substrate (thickness H, εᵣ) with a ground plane on the bottom.

**Quasi-static parameters** (Collin §3.12):

Effective dielectric constant:

$$ \varepsilon_e = \frac{\varepsilon_r + 1}{2} + \frac{\varepsilon_r - 1}{2} \cdot \frac{1}{\sqrt{1 + 12H/W}} $$

Characteristic impedance:

$$ Z_0 = \begin{cases}
\frac{60}{\sqrt{\varepsilon_e}} \ln\left( \frac{8H}{W} + \frac{W}{4H} \right), & W/H \le 1 \\[6pt]
\frac{120\pi}{\sqrt{\varepsilon_e} \left[ W/H + 1.393 + 0.667 \ln(W/H + 1.444) \right]}, & W/H \ge 1
\end{cases} $$

**Key properties** (Collin §3.12):
- Quasi-TEM mode for frequencies where W, H ≪ λ
- Dispersion: εₑ(f) increases with frequency
- Conductor and dielectric losses both contribute to attenuation
- Open structure → easy access for shunt/series component mounting

### 11.2.2 Coplanar Waveguide (CPW)

A center conductor (width S) with ground planes on either side, separated by slots
(width W), all on the same substrate surface.

**Advantages** (Collin §3.13):
- Active/passive components connect on same side as ground (no via holes)
- Lower dispersion than microstrip at mm-wave frequencies
- Wider center conductor for given Z₀ → lower conductor loss
- Quasi-TEM formulas valid up to ~50 GHz for typical dimensions

**Quasi-TEM parameters** (Collin Eqs. 3.191–3.192):
- k = S/(S + 2W)
- εₑ = 1 + q(εᵣ − 1), where q ≈ 0.5 for typical dimensions
- Z₀ uses complete elliptic integrals K(k)/K'(k)

### 11.2.3 Slotline

A slot cut in a ground plane on a dielectric substrate. Not as widely used as microstrip
or CPW. Supports a non-TEM mode. Used for balanced mixers and antenna feeds.

### 11.2.4 Comparison

| Property | Microstrip | CPW | Slotline |
|----------|-----------|-----|----------|
| TEM nature | Quasi-TEM | Quasi-TEM | Non-TEM |
| Via holes needed | Yes (ground) | No | No |
| Dispersion | Moderate | Low (small dims) | Higher |
| Fabrication ease | Very easy | Easy | Easy |
| Active device mounting | Wire bonds to ground | Easy (same plane) | Moderate |

---

## 11.3 Lumped Elements at Microwave Frequencies

### 11.3.1 Spiral Inductors

The most common lumped inductor for MICs (Collins §5.3, Fig. 5.15).

**Design constraints:**
- Total conductor length must be ≪ λ to maintain lumped behavior
- Electrical length Bl ≤ 0.26 rad for < 5% resistive change (Collins analysis)
- High-impedance (narrow) line maximizes inductance per unit length

**Example values** (Collins):
- ~7 nH/cm for a 100 Ω line on 1 mm substrate (εₑ = 4) at 2 GHz
- 5-turn spiral: 1.4 mm diameter, 0.06 mm conductor, 0.038 mm spacing → 25 nH at 2 GHz

**Self-resonance**: Every spiral inductor has distributed capacitance; Q peaks near
self-resonant frequency.

**Wheeler formula** (approximate for square spirals):

$$ L \approx \frac{\mu_0 n^2 d_{avg}}{2} \left[ \ln\left(\frac{2.46}{\rho}\right) + 0.2\rho^2 \right] $$

where ρ = (d_out − d_in)/(d_out + d_in), d_avg = (d_out + d_in)/2.

**Q estimation**:

$$ Q \approx \frac{\omega L}{R_s} \cdot \frac{1}{1 + R_s/R_{sub}} $$

where R_s is conductor skin-effect resistance, R_sub represents substrate losses.

### 11.3.2 Capacitors

| Type | Configuration | Typical Range | Notes |
|------|--------------|---------------|-------|
| **Open-circuit stub** | Short stub in shunt | ~1 pF | Simplest |
| **Interdigital** | Interleaved fingers in series | Several pF | Finger count & length control C |
| **MIM (Metal-Insulator-Metal)** | Sandwich structure | ≤ 20 pF | Common in MMIC |
| **Chip capacitor** | Discrete soldered | ≤ 100 pF | Hybrid MIC only |

**MIM capacitor formula**:

$$ C = \frac{\varepsilon_0 \varepsilon_r A}{t} $$

Example: 1 mm × 1 mm, εᵣ = 10, t = 10 μm → C ≈ 9 pF (Collins).

### 11.3.3 Resistors

- Thin-film (NiCr, TaN) on substrate
- Typical range: 10 Ω–10 kΩ
- Tolerances ~10–20% without trimming

---

## 11.4 Semiconductor Device Integration

### 11.4.1 MESFET (Metal-Semiconductor Field-Effect Transistor)

The workhorse of GaAs MMIC technology (Collins §10.2).

**Characteristics:**
- Gate lengths: submicron (< 0.5 μm typical)
- f_T (current gain cutoff): 30–100 GHz
- Gain: 8–15 dB per stage at 2 GHz
- Noise figure: < 1 dB at 2 GHz (low-noise designs)
- Common-source configuration most common

**Key applications**: LNA, power amplifier, oscillator, mixer

### 11.4.2 HEMT (High-Electron-Mobility Transistor)

Also called MODFET (MODulation-doped FET). Uses heterojunction (AlGaAs/GaAs)
to create a 2D electron gas with very high mobility (Collins §10.2).

**Advantages over MESFET:**
- Higher mobility → lower noise, higher f_T
- Operating frequencies up to 100 GHz
- Lower noise figure (~0.5 dB at 10 GHz)
- Better for millimeter-wave applications

### 11.4.3 HBT (Heterojunction Bipolar Transistor)

Uses heterojunction technology applied to bipolar transistors (Collins §10.1).

**Advantages:**
- Very low base resistance
- High current gain
- Speed increase 2–3× over homojunction BJT
- Reported f_max = 175 GHz (AlGaAs/GaAs HBT, circa 1987)

**Applications:** Power amplifiers, oscillators, high-speed digital circuits

### 11.4.4 Integration Considerations

- **GaAs** is preferred for MMIC: semi-insulating (low substrate loss) + native for MESFET/HEMT
- **SiGe HBT** is a competitor: CMOS compatibility + good RF performance
- **Thermal management**: Active devices generate heat; substrate must conduct it to ground plane
- **Metal heat sinks are difficult** in MICs — they interact with EM fields unpredictably

---

## 11.5 Antennas for MICs

### 11.5.1 Microstrip Patch Antenna

The most common antenna integrated with MICs. Consists of a rectangular patch of
length L on a substrate (εᵣ, H) above a ground plane.

**Resonant length** (dominant TM₁₀ mode):

$$ L_{eff} = \frac{c}{2 f_r \sqrt{\varepsilon_e}} $$

Accounting for fringing fields (ΔL extension):

$$ L = L_{eff} - 2\Delta L $$

where:

$$ \Delta L = 0.412H \cdot \frac{(\varepsilon_e + 0.3)(W/H + 0.264)}{(\varepsilon_e - 0.258)(W/H + 0.8)} $$

**Patch width** (for efficient radiation):

$$ W = \frac{c}{2 f_r} \sqrt{\frac{2}{\varepsilon_r + 1}} $$

**Input impedance**: Depends on feed position. At the patch edge:

$$ R_{in,edge} \approx \frac{90 \varepsilon_r^2}{(\varepsilon_r - 1)} \left(\frac{L}{W}\right)^2 \quad \text{(for } \varepsilon_r > 1) $$

**Bandwidth**: Typically 1–5% for standard patches. Enhanced by:
- Thick substrates (increased H)
- Proximity-coupled feeds
- Aperture-coupled feeds
- Parasitic elements (stacked patches)

### 11.5.2 Printed Dipoles

A printed dipole consists of two arms printed on a substrate. Balanced feed required
(often via a balun). Simpler geometry than a patch but narrower bandwidth.

**Resonant length**: ~0.47λₑ for a half-wave dipole on substrate.

### 11.5.3 Other Integrated Antennas

- **Slot antennas** (slot in ground plane — complements patch)
- **Yagi-Uda printed arrays** (for directionality)
- **Vivaldi (tapered slot)** antennas for wideband applications
- **Grid arrays** for millimeter-wave

---

## 11.6 Circuit Design Examples

### 11.6.1 LNA (Low-Noise Amplifier)

Design approach (Collins §10.10–10.11):

1. **Select device**: MESFET or HEMT with low NF at operating frequency
2. **Stability check**: Compute K and |Δ|; device may be conditionally stable
3. **Source match**: Γ_opt for minimum noise figure (noise circles)
4. **Load match**: Γ_L for desired gain (constant gain circles)
5. **Tradeoff**: Between NF_min, gain, and input match (VSWR)
6. **Realization**: Microstrip matching networks on substrate (e.g., GaAs)

**Cascaded NF** (Friis formula):

$$ F = F_1 + \frac{F_2 - 1}{G_1} + \frac{F_3 - 1}{G_1 G_2} + \cdots $$

### 11.6.2 Mixer

- Diode-based (Schottky) or FET-based (resistive mixer)
- Gate mixing in FET: RF applied to gate, LO to source or gate, IF at drain
- Conversion loss: 5–10 dB typical (passive)
- **Active mixer** (FET transconductance mixing) can provide conversion gain

### 11.6.3 VCO (Voltage-Controlled Oscillator)

- Varactor-tuned oscillator
- FET or HBT in common-source/gate with feedback
- Tuning range: 10–30% bandwidth typical
- Phase noise minimized by high-Q resonator (dielectric resonator, cavity, or planar)

---

## Design Example Summary

| Circuit | Freq. | Technology | Key Figures |
|---------|-------|-----------|-------------|
| 2 GHz LNA | 2 GHz | GaAs MESFET | NF < 1 dB, G > 12 dB |
| 10 GHz LNA | 10 GHz | GaAs HEMT | NF ~ 0.5 dB, G ~ 10 dB |
| 5 GHz Mixer | 5 GHz | Schottky MMIC | Conv. loss ~ 6 dB |
| 4 GHz VCO | 4 GHz | BJT/HBT | P_out ~ 10 dBm, tuning ~ 200 MHz |

---

## References (from Collins)

1. M. V. Schneider, "Microstrip Lines for Microwave Integrated Circuits," *Bell Syst. Tech. J.*, vol. 48, pp. 1422–1444, 1969.
2. D. A. Daly et al., "Lumped Elements in Microwave Integrated Circuits," *IEEE Trans. MTT*, vol. 15, pp. 713–721, 1967.
3. R. W. Jackson, "Considerations in the Use of Coplanar Waveguide for Millimeter-Wave Integrated Circuits," *IEEE Trans. MTT*, vol. 34, pp. 1450–1456, 1986.
4. A. Nakatani and N. G. Alexopoulos, "Modeling of Dispersive Properties of Integrated Circuit Structures," *IEEE Trans. MTT*, vol. 33, pp. 1436–1441, 1985.
5. N. H. Sheng et al., "High Power GaAlAs/GaAs HBT's for Microwave Applications," *IEDM Digest*, pp. 619–622, 1987.
6. C. A. Liechti, "High Speed Transistors: Directions for the 1990's," *Microwave Journal*, pp. 165–177, Sept. 1989.
7. I. J. Bahl and P. Bhartia, *Microwave Solid State Circuit Design*, Wiley, 1988.
8. R. Garg, P. Bhartia, I. Bahl, A. Ittipiboon, *Microstrip Antenna Design Handbook*, Artech House, 2001.

---

> 🎉 **End of Collins Microwave Engineering — Complete Chapter Notes.**
> This file synthesizes content from Collins §§3.12, 3.13, 5.3, 10.1–10.11 plus
> standard MIC/antenna references into a unified Chapter 11 on Microwave Integrated Circuits.
