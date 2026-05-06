---
chapter: 1
title: Electrodynamics Entering the 21st Century
book: Computational Electrodynamics — The Finite-Difference Time-Domain Method (3rd Ed.)
author: Allen Taflove, Susan C. Hagness
raw_size: 74,967 bytes
tokens_processed: ~15K
---

# Chapter 1: Electrodynamics Entering the 21st Century

## 1.1 Introduction

Maxwell's partial differential equations of electrodynamics, formulated approximately 140 years ago, represent a fundamental unification of electric and magnetic fields predicting electromagnetic wave phenomena. Feynman called this "the most outstanding achievement of 19th-century science."

The central question: *"Of what relevance are solutions of Maxwell's equations to modern society?"*

This chapter discusses prospects for using numerical solutions of Maxwell's equations — in particular the finite-difference time-domain (FDTD) method — to help innovate and design key electrical engineering technologies ranging from cellphones and computers to lasers and photonic circuits.

**Key shift:** Large-scale solutions of Maxwell's equations, historically motivated primarily by military defense, are shifting rapidly toward commercial applications in high-speed communications, computing, and biomedicine.

---

## 1.2 The Heritage of Military Defense Applications

From WWII until ~1990, the primary answer was military defense.

**Radar technology** development during WWII motivated early computational electromagnetics. Key drivers:
- **Radar system design:** Microwave sources, circuits, waveguides, antennas
- **Stealth technology:** Understanding scattering from complex electrically large structures → reduced or confusing scattering responses
- **EMP hardening:** Nuclear EMP (electromagnetic pulse) could burn out electrical equipment hundreds of miles from detonation point → need to predict EMP penetration/coupling

> **Numerical Intuition:** Military defense drove the entire field for 50 years. The computational scale required for full-aircraft RCS at microwave frequencies motivated virtually all algorithmic advances (PML ABCs, conformal gridding, hybrid methods).

---

## 1.3 Frequency-Domain Solution Techniques

Pre-FDTD techniques fell into two major categories:

### 1.3.1 High-Frequency/Asymptotic Techniques
- Geometrical optics (ray tracing)
- Geometrical theory of diffraction (GTD) [1]
- Uniform theory of diffraction (UTD) [2]
- Physical optics (PO)
- Physical theory of diffraction (PTD)

**Limitations:** Valid only for electrically large objects with smooth surfaces; fail for complex inhomogeneous, anisotropic, or nonlinear media.

### 1.3.2 Integral Equation / Method of Moments (MoM) [3,4]
- Solve for surface currents on PEC/PMC/dielectric objects
- Convert integral equations to matrix equations via basis functions
- Frequency sweep requires solving at each frequency independently

### 1.3.3 Fast Multipole Method (FMM) / MLFMA [5]
- Accelerates MoM matrix-vector products for large problems
- O(N log N) complexity vs O(N³) for standard MoM
- Still frequency-domain; wideband problems remain expensive

> **Numerical Intuition:** Frequency-domain techniques require solving a separate matrix equation for each frequency point. For broadband problems (pulse responses, UWB radar), this becomes prohibitive — FDTD naturally provides wideband response from a single simulation via Fourier transform.

---

## 1.4 Rise of Finite-Difference Time-Domain Techniques

FDTD emerged from the recognition that time-domain solutions of Maxwell's curl equations could provide:
- **Direct physical insight:** Watch fields evolve in time
- **Wideband response:** Single simulation → any frequency via DFT
- **Nonlinear/dynamic media:** Naturally handled in time domain
- **Arbitrary geometry:** No Green's function required

**Scaling note:** By the late 1990s, FDTD simulation of whole-aircraft RCS with ~$10^8$ cells became feasible on massively parallel supercomputers.

---

## 1.5 History of FDTD Techniques for Maxwell's Equations

**Key historical milestones:**

| Year | Contributor | Contribution |
|------|-------------|--------------|
| 1966 | Yee [6] | Original Yee algorithm: staggered grid, leapfrog time-stepping |
| 1975 | Taflove & Brodwin [8] | First demonstration of steady-state scattering solutions using FDTD |
| 1980s | Various | Absorbing boundary conditions (Mur, Liao) |
| 1994 | Berenger | Perfectly matched layer (PML) — revolutionary ABC |
| 1990s–2000s | Many | Conformal grids, dispersive media, nonlinear optics, hybrid methods |

**Original Yee algorithm (1966) [6]:**
- Let's each electric field component be located between pairs of magnetic field components, and vice versa — the **staggered grid** (will be formalized in Ch. 3).
- All field components are interleaved in space and time using a **leapfrog** time-stepping scheme, where E and H updates are performed alternately in time.

> **Numerical Intuition:** The leapfrog scheme is *explicit* — no matrix inversion. Each field update depends only on previously stored adjacent fields. This is the source of FDTD's simplicity and parallel efficiency, but also imposes the CFL stability condition ($\Delta t \leq \Delta x / c$ for 1D).

---

## 1.6 Characteristics of FDTD and Related Space-Grid Time-Domain Techniques

FDTD is a **direct solution method** for Maxwell's curl equations employing **volumetric sampling** of E and H within and surrounding the structure.

### Key Characteristics

1. **No potentials** — operates directly on E and H fields.
2. **Sub-wavelength spatial sampling:** Typically 10–20 samples per $\lambda_0$ (free-space wavelength at highest frequency of interest).
3. **Time-stepping stability:** $\Delta t$ selected to ensure numerical stability (CFL condition).
4. **Marching-in-time:** Simulates continuous EM waves using sampled-data numerical analogs propagating in computer data space.
5. **Absorbing boundary conditions (ABCs)** at outer lattice truncation to simulate infinite space.
6. **Self-consistency** of modeled phenomena assured if spatial and temporal variations are well-resolved.
7. **Wideband frequency response** via discrete Fourier transformation (DFT) of field-vs-time waveforms at points of interest.

### 1.6.1 Classes of Algorithms

Three categories based on mesh structure:

#### 1. Almost Completely Structured (Yee-type)
- Uniform Cartesian grid with rectangular cells (Yee [6])
- Staircasing to approximate non-grid-parallel features
- **Refinement:** Conformal cells adjacent to structural features [22,52,58]
  - Number of modified cells ∝ surface area → favorable scaling for large structures
  - Disadvantage: special mesh-generation software needed

#### 2. Surface-Fitted (Globally Distorted)
- Space lattice globally distorted to fit structural shape
- Multiple zones for distinct features [24]
- **Advantages:** Available mesh-generation software
- **Disadvantages:**
  - Extra memory for per-cell position/stretching factors
  - Extra operations for Maxwell's equations and field continuity at zone interfaces
  - Possible numerical dissipation that limits electrical size

#### 3. Completely Unstructured
- Collection of varying-size/shape cells conforming to surfaces [25]
- **Advantages:** Flexible mesh generation, handles complicated 3D shapes with volumetric inhomogeneities
- **Disadvantages:**
  - Potential numerical inaccuracy/instability from highly skewed cells
  - Difficulty mapping unstructured mesh to parallel architectures

> **Numerical Intuition:** For high-Q resonant structures (e.g., photonic crystal cavities with Q > 10^4), staircasing errors can shift resonant frequencies unacceptably. Conformal or unstructured meshes near boundaries are essential. For lossy scattering problems, the structured Yee grid with staircasing often suffices.

### 1.6.2 Predictive Dynamic Range

**Definition:** Let $P_0$ be the power density of the primary (incident) wave, and $P_s$ be the minimum observable power density of a secondary (scattered) wave (where numerical artifacts degrade accuracy below $\eta$ dB). Then:
$$
\text{Predictive Dynamic Range} = 10 \log_{10}\left(\frac{P_0}{P_s}\right) \quad \text{[dB]}
$$

This concept is analogous to the "quiet zone" in an anechoic chamber.

**Typical values:**
- 32-bit arithmetic: ~40–60 dB dynamic range
- 64-bit arithmetic: ~60–80 dB

### 1.6.3 Scaling to Very Large Problem Sizes

**Scaling law for structured FDTD:**
- Memory required ∝ number of cells $N$
- Operations per time-step ∝ $N$
- Total operations ∝ $N \times \text{(number of time-steps)}$

For the largest problems (early 2000s):
- $10^8$–$10^9$ cells on massively parallel machines
- Memory: 100 GB to several TB
- Run time: hours to days

> **Numerical Intuition:** The O(N) memory and O(N) per-step operation count of FDTD is fundamentally more favorable than MoM's O(N²) or O(N³) for large problems. This is why FDTD dominates for electrically large, inhomogeneous structures.

---

## 1.7 Key Application Domains (Case Studies)

### 1.7.1 Impulsive Around-the-World Extremely Low-Frequency Propagation

**Problem:** ELF (3 Hz–3 kHz) and VLF (3–30 kHz) propagation in the Earth-ionosphere waveguide.

**FDTD approach [59–62]:**
- 3D model of Earth ±100 km including lithosphere and ionosphere
- Resolution: ~40 × 40 × 5 km
- Variable-cell grid wrapping around entire Earth
- Periodic boundary conditions

**Results:**
- Frequency-dependent propagation attenuation
- Schumann resonances
- Pulse propagation from simulated lightning strikes
- Asymmetries due to lithosphere conductivity inhomogeneities (not numerical artifacts)

**Ongoing work:** ULF precursors of major earthquakes; ULF/ELF for remote detection of underground ore/deposits.

### 1.7.2 Cellphone Radiation Interacting with the Human Head

**Problem:** SAR (Specific Absorption Rate) compliance for PWC (Personal Wireless Communications) devices. Peak SAR for any 1 g of tissue must be < 1.6 W/kg (U.S. standard).

**FDTD advantages:**
- Straightforward, accurate modeling of near/far fields for arbitrary inhomogeneous media
- Complex tissue structure of human body

**Case study (Ch. 14, Sec. 14.9):** Motorola i250 phone
- Graded FDTD meshes + local refinement → cell sizes as small as 0.1 mm
- Phone details: housing, pushbuttons, multilayer PCB, interconnects, helical antenna
- Head model: 121 MRI-derived slices (1 mm ear, 3 mm elsewhere), 0.2 mm transverse
- 15 tissue types

**Validation:** Good-to-excellent agreement with experimental 1g- and 10g-averaged peak SAR.

### 1.7.3 Early-Stage Detection of Breast Cancer Using UWB Microwave Radar

**Problem:** Detect malignant tumors < 5 mm within inhomogeneous breast tissue.

**FDTD approach:**
- Simulate UWB pulse illumination by antenna array at breast surface
- Record scattered pulses → space-time imaging algorithms
- Model arbitrary lossy, dispersive dielectrics

**Status:** Advanced to initial preclinical investigations [69,70].

### 1.7.4 Homing Accuracy of a Radar-Guided Missile

**Problem:** EM wave interactions between antenna and protective radome generate angular target-location errors.

**FDTD application:**
- Model antenna + radome in single computational domain
- Capture picosecond-by-picosecond wave physics
- Test effectiveness of proposed design alterations computationally

**Key physics revealed by FDTD:**
1. Incident wave generates radially propagating scattered field at radome metal tip and curved surface
2. Part of energy scatters from hom antenna, part propagates down horn to matched load
3. Trapped energy in dielectric radome wall encounters radome-missile body junction, reflects, reradiates
4. New guided wave forms in radome wall due to structural scattering from horn antenna

### 1.7.5 Electromagnetic Wave Vulnerabilities of a Military Jet Plane

**Problem:** Aircraft vulnerability to radar detection / circuit upset from enemy microwave threats.

**Hybrid FDTD-FE approach [58,60]:**
- Flexible FE (finite element) mesh for complex surfaces/shapes
- FDTD "bricks" (4 cm, ~$\lambda/15$) throughout remainder of space
- Only 3 layers of unstructured FE cells needed for accurate geometric representation

**Demonstration:** Saab Trainer aircraft (11 m long, 8 m wingspan) — induced surface currents on aircraft and jet engine air inlet. Excellent RCS agreement with fast-multipole MoM at 500 MHz.

**Resource requirement:** 1.9 GB memory, 8 hours on single 900-MHz Itanium2 processor.

### 1.7.6 Millimeter-Wave Propagation in Defect-Mode EBG Waveguides

**Problem:** Baseband metal-strip interconnects become unusable for clock rates > 3 GHz (signal integrity, cross-coupling, radiation).

**Proposed solution:** Wireless interconnects using defect-mode electromagnetic bandgap (EBG) waveguides [71,72].

**Characteristics:**
- Square arrays of copper via pins
- One or more rows removed → linear waveguide
- Operation above 100 GHz conceptually feasible

**Prototype at 50 GHz [72]:**
- Double-sided circuit board (Rogers 5880)
- 8.6 cm between probes, 0.76 mm between ground planes
- Passband from ~28 to >90 GHz, ±1.5 dB flatness (~90% bandwidth)
- Midband insertion loss: ~4 dB at 50 GHz (2 dB dielectric, ~1 dB per coaxial transition)
- Scalable to >100 GHz center frequency

### 1.7.7 Photonic Crystal Microcavity Laser

**Structure [73]:**
- Slab photonic crystal (air holes in 282.5-nm semiconductor, $n = 3.4$)
- Single defect → microcavity resonator
- InP post injects holes; top electrode supplies electrons → quantum well recombination at 1.55 μm

**FDTD modeling:**
- Used actual SEM-image structural data → incorporated fabrication imperfections
- Predicted monopole-mode operation and field asymmetry
- $Q \approx 3,000$, lasing wavelength 1,519.7 nm
- Modal volume: $0.0587\;\mu\text{m}^3 = 0.684(\lambda/n)^3$ — near smallest theoretical

### 1.7.8 Photonic Crystal Cross-Waveguide Switch

**All-optical switch [14,74]:**
- Two photonic crystal waveguides crossing at right angles
- Microcavity at intersection with two orthogonal dipole modes
- Kerr nonlinearity in AlGaAs → index shift → bistable switching
- 10 Gbits/s operation, ~100 fJ/pulse

**Operation:**
1. Without control: cavity out of resonance → low transmission
2. Control pulse injected → index shift → cavity shifts into resonance → high transmission
3. Bistable → digital switching (only low/high states allowed)

**Implications:** Fundamental building block for "optoelectronics" — successor technology to electronics in 21st century.

---

## 1.8 Conclusions

Key statement: The field of computational electrodynamics has shifted from military-defense-driven to applications in **communications, computing, and biomedicine**.

**Remaining grand challenge:** Computational unification of electromagnetic, heat transport, and quantum phenomena to model the broadest range of problems:
- Frequency range: ULF to ultraviolet (minutes to sub-femtoseconds)
- Distance scales: Earth's circumference to single atom

FDTD and related space-grid time-domain techniques are arguably the most robust means to solve problems spanning these ranges, especially where **complexity, nonlinearity, and multiphysics** dominate.

---

## Ch.1 Example Code: Basic 1D FDTD Demonstration

Since Ch. 1 is an overview without detailed equations/examples, we provide a minimal 1D FDTD simulation that demonstrates core concepts: discretization, leapfrog stepping, CFL condition, and absorbing boundary conditions.

See: `taflove_ch1_examples.py`

---

## Chapter Audit

| Section | Content | Notes |
|---------|---------|-------|
| 1.1 | Introduction | ✓ Full coverage |
| 1.2 | Military Heritage | ✓ Full coverage |
| 1.3 | Freq-Domain Techniques | ✓ Summary |
| 1.4 | Rise of FDTD | ✓ Summary |
| 1.5 | History of FDTD | ✓ Milestone table |
| 1.6 | Characteristics of FDTD | ✓ Full coverage |
| 1.6.1 | Algorithm classes | ✓ Three categories |
| 1.6.2 | Predictive dynamic range | ✓ Definition |
| 1.6.3 | Scaling | ✓ Complexity analysis |
| 1.7.1 | ELF/VLF propagation | ✓ |
| 1.7.2 | Cellphone SAR | ✓ |
| 1.7.3 | Breast cancer detection | ✓ |
| 1.7.4 | Missile homing | ✓ |
| 1.7.5 | Aircraft vulnerability | ✓ |
| 1.7.6 | EBG waveguides | ✓ |
| 1.7.7 | Photonic crystal laser | ✓ |
| 1.7.8 | Photonic crystal switch | ✓ |
| 1.8 | Conclusions | ✓ |
| Examples | 1D FDTD code | ✓ 3 example scripts |

---

**References cited in Ch.1 (extracted from raw):**
1. Keller, J.B., "Geometrical theory of diffraction"
2. Kouyoumjian & Pathak, "Uniform geometrical theory of diffraction"
3. Harrington, R.F., "Field Computation by Moment Methods"
4. Umashankar, K.R., "Numerical analysis of EM wave scattering..."
5. Song & Chew, "The fast Illinois solver code"
6. Yee, K.S., "Numerical solution of initial boundary value problems..." (1966)
7. Shlager & Schneider, "Survey of the FDTD Literature" (1998)
8. Taflove & Brodwin, "Numerical solution of steady-state EM scattering..." (1975)
