---
title: "Chapter 12 — Concluding Remarks on Computational Electromagnetics"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Overview of CEM methods
  - Frequency-domain vs time-domain methods
  - Asymptotic methods (PO, PTD, GTD, UTD, SBR)
  - Numerical methods (MoM, FEM, FDM, FDTD)
  - Hybrid methods
  - Challenges: multi-scale, multi-physics, HPC
---

# Chapter 12: Concluding Remarks on Computational Electromagnetics

## 12.1 Overview

**Frequency-domain methods:**
- **Asymptotic:** PO (Physical Optics), PTD (Physical Theory of Diffraction), GTD/UTD (Geometrical Theory of Diffraction), SBR (Shooting and Bouncing Rays) — electrically large problems
- **Numerical:** MoM (surface integral), FEM (volume PDE), FDM (volume PDE)

**Time-domain methods:**
- FDTD (finite difference)
- FETD (finite element time-domain)
- IETD (integral equation time-domain / MOT)

## 12.2 Applications

- Antenna design (patch, reflector, arrays)
- RCS prediction (aircraft, vehicles)
- Microwave circuits (filters, couplers, transitions)
- EMI/EMC (shielding, cavity coupling)
- Bioelectromagnetics (SAR, implants)
- Photonics (waveguides, gratings, plasmonics)

## 12.3 Challenges

- **Multi-scale geometries:** fine features + large electrical size
- **Multi-physics:** thermal, mechanical, plasma coupling
- **HPC:** GPU/parallel computing for large-scale simulations
- **Uncertainty quantification:** statistical variations in materials/geometry

---

## Audit

| Section | Topic |
|---------|-------|
| 12.1 | CEM overview |
| 12.2 | Applications |
| 12.3 | Challenges |
