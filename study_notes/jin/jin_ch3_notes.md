---
title: "Chapter 3 — Electromagnetic Theorems and Principles"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Uniqueness theorem
  - Image theory (PEC/PMC ground planes)
  - Surface equivalence principle
  - Induction theorem
  - Reciprocity theorem
  - Duality principle
  - Aperture radiation & Babinet's principle
---

# Chapter 3: Electromagnetic Theorems and Principles

## 3.1 Uniqueness Theorem

The field in a volume $V$ with given sources is **unique** if either the tangential $\mathbf{E}$ or tangential $\mathbf{H}$ (or a mix) is specified on the bounding surface $S$.

**Proof (time-harmonic, lossy medium):** Assume two solutions, subtract, integrate $\nabla \cdot (\delta\mathbf{E} \times \delta\mathbf{H}^*)$ over $V$:

$$
\oiint_S (\delta\mathbf{E} \times \delta\mathbf{H}^*) \cdot d\mathbf{S} = \iiint_V [ -j\omega\mu|\delta\mathbf{H}|^2 + (j\omega\epsilon^* - \sigma)|\delta\mathbf{E}|^2 ] dV
$$

Surface integral vanishes when $\hat{n} \times \mathbf{E}$ or $\hat{n} \times \mathbf{H}$ is specified → for lossy media $\delta\mathbf{E} = \delta\mathbf{H} = 0$.

**Three sufficient conditions:**
1. $\hat{n} \times \mathbf{E}$ specified everywhere on $S$
2. $\hat{n} \times \mathbf{H}$ specified everywhere on $S$
3. $\hat{n} \times \mathbf{E}$ on part, $\hat{n} \times \mathbf{H}$ on rest

---

## 3.2 Image Theory

Replace a PEC/PMC ground plane with equivalent image sources in free space.

| Dipole Type | Above PEC | Above PMC |
|:-----------|:----------|:----------|
| Vertical electric $\hat{z}Il$ | Same $\hat{z}Il$ | Opposite $-\hat{z}Il$ |
| Horizontal electric $\hat{x}Il$ | Opposite $-\hat{x}Il$ | Same $\hat{x}Il$ |
| Vertical magnetic $\hat{z}K$ | Opposite $-\hat{z}K$ | Same $\hat{z}K$ |
| Horizontal magnetic $\hat{x}K$ | Same $\hat{x}K$ | Opposite $-\hat{x}K$ |

For an arbitrary current above PEC ground plane:

$$
\mathbf{J}_{\text{im}}(\mathbf{r}) = 2\hat{z}\hat{z}\cdot\mathbf{J}(\mathbf{r}_i) - \mathbf{J}(\mathbf{r}_i), \quad \mathbf{r}_i = x\hat{x} + y\hat{y} - z\hat{z}
$$

---

## 3.3 Surface Equivalence Principle

Replace actual sources on a closed surface $S$ with **equivalent surface currents**:

$$
\mathbf{J}_s = \hat{n} \times \mathbf{H}, \quad \mathbf{M}_s = -\hat{n} \times \mathbf{E}
$$

These produce the same fields outside $S$ (zero fields inside — Love's equivalence).

---

## 3.4 Induction Theorem

Special case of equivalence: a PEC scatterer is replaced by induced surface currents equal to $2\hat{n} \times \mathbf{H}^{\text{inc}}$ in the illuminated region (physical optics approximation).

---

## 3.5 Reciprocity Theorem

For two sets of sources $(\mathbf{J}_1, \mathbf{M}_1)$ and $(\mathbf{J}_2, \mathbf{M}_2)$ producing $(\mathbf{E}_1, \mathbf{H}_1)$ and $(\mathbf{E}_2, \mathbf{H}_2)$ in the same medium:

$$
\iiint_V (\mathbf{E}_1 \cdot \mathbf{J}_2 - \mathbf{H}_1 \cdot \mathbf{M}_2) dV = \iiint_V (\mathbf{E}_2 \cdot \mathbf{J}_1 - \mathbf{H}_2 \cdot \mathbf{M}_1) dV
$$

For isotropic media: receiving and transmitting patterns of an antenna are identical.

**Example 3.3:** A vertical receiving antenna picks up the same signal as a transmitting vertical antenna.

**Example 3.4:** For a small loop inside a waveguide — loop signal $\propto$ magnetic field at loop's location.

---

## 3.6 Duality Principle

Maxwell's equations are symmetric under the exchange:

$$
\mathbf{E} \leftrightarrow \mathbf{H}, \quad \mathbf{J} \leftrightarrow \mathbf{M}, \quad \epsilon \leftrightarrow \mu, \quad \varrho_e \leftrightarrow \varrho_m
$$

Thus, given any solution, the dual solution is obtained by replacing the quantities above.

---

## 3.7 Aperture Radiation and Babinet's Principle

**Aperture in PEC plane:** Fields in the aperture are equivalent to magnetic current $\mathbf{M}_s = -2\hat{n} \times \mathbf{E}_{\text{ap}}$.

**Babinet's principle:** The diffraction pattern from an aperture is complementary to that from its complementary obstacle (screen).

---

## Key Physical Intuition

1. **Uniqueness** guarantees that any method solving a well-posed EM problem yields the same answer.
2. **Image theory** eliminates ground planes via virtual sources — a standard trick for microstrip antennas and radar cross-section (RCS) problems.
3. **Surface equivalence** is the foundation of all integral-equation methods (MoM, FEM-BEM).
4. **Reciprocity** is why antennas work the same for Tx and Rx — a fundamental time-saving design principle.
5. **Duality** halves the work: solve one problem, get the other for free.

---

## Original Examples

| Example | Topic | Section |
|---------|-------|---------|
| 3.1 | Uniqueness theorem for static fields | 3.1 |
| 3.2 | Uniqueness theorem for time-varying fields | 3.1 |
| 3.3 | Reciprocity for two dipoles | 3.5 |
| 3.4 | Loop probe inside a waveguide | 3.5 |

---

## Audit

| Section | Content Coverage | Notes Alignment |
|---------|-----------------|-----------------|
| 3.1 | Uniqueness theorem | Full coverage |
| 3.2 | Image theory | Full coverage |
| 3.3 | Equivalence principle | Full coverage |
| 3.4 | Induction theorem | Full coverage |
| 3.5 | Reciprocity theorem | Full coverage |
| 3.6 | Duality principle | Full coverage |
| 3.7 | Aperture, Babinet | Full coverage |
