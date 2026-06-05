---
title: "Chapter 10 — The Method of Moments"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Integral equation formulation using Green's functions
  - MoM discretization: basis functions, testing functions
  - EFIE and MFIE for conducting objects
  - RWG basis functions (triangular mesh)
  - Impedance matrix filling
  - Plane wave illumination, RCS computation
  - Microstrip antenna analysis
---

# Chapter 10: The Method of Moments

## 10.1 Introduction

**Electrostatic integral equation:**

$$
\int_S G(\mathbf{r}, \mathbf{r}') \varrho_s(\mathbf{r}') dS' = \Phi
$$

Discretize with pulse basis functions:

$$
\sum_{j=1}^N Z_{ij} \varrho_j = \Phi_i
$$

where $Z_{ij} = \int_{\Delta S_j} \frac{1}{4\pi\epsilon |\mathbf{r}_i - \mathbf{r}'|} dS'$.

## 10.2 EFIE for Conducting Objects

**Electric Field Integral Equation:**
$$
\hat{n} \times [\mathbf{E}^{\text{inc}} + \mathbf{E}^{\text{scat}}(\mathbf{J}_s)] = 0 \quad\text{on } S
$$

Discretized with RWG basis functions on triangular mesh:

$$
\mathbf{J}_s \approx \sum_{n=1}^N I_n \mathbf{f}_n(\mathbf{r})
$$

**Impedance matrix:** $Z_{mn} = \langle \mathbf{f}_m, \mathcal{L}(\mathbf{f}_n) \rangle$.

## 10.3 Scattering and RCS

Bistatic RCS computed from far-field transform of induced currents.

## 10.4 Microstrip and Periodic Structures

Green's function for layered media + MoM for planar circuits.

## 10.5 Time-Domain MoM

Marching-on-in-time (MOT) scheme.

---

## Audit

| Section | Topic |
|---------|-------|
| 10.1 | Introduction, electrostatic example |
| 10.2 | EFIE/MFIE for conductors |
| 10.3 | Scattering/RCS |
| 10.4 | Microstrip/periodic |
| 10.5 | Time-domain MoM |
