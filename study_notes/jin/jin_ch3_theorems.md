# Chapter 3: Electromagnetic Theorems and Principles

> Jin, *Theory and Computation of Electromagnetic Fields*, 2nd Ed., Ch. 3, pp. 89–134.

Starting from Maxwell's equations, this chapter derives several fundamental theorems:
**Uniqueness Theorem**, **Image Theory**, **Reciprocity Theorem**, **Equivalence
Principles**, **Duality Principle**, and **Babinet's Principle**.  These provide the
mathematical foundation for constructing equivalent problems, formulating integral
equations, and solving scattering/radiation problems.

---

## 3.1 Uniqueness Theorem (pp. 90–94)

The field within a volume $V$ bounded by $S$ is uniquely determined if:

1. $\hat{n} \times \mathbf{E}$ is specified **everywhere on $S$**, or
2. $\hat{n} \times \mathbf{H}$ is specified **everywhere on $S$**, or
3. $\hat{n} \times \mathbf{E}$ on part of $S$ and $\hat{n} \times \mathbf{H}$ on the rest.

### Proof (time-harmonic case)

Assume two solutions $(\mathbf{E}_a, \mathbf{H}_a)$ and $(\mathbf{E}_b, \mathbf{H}_b)$ with the
same sources $\mathbf{J}_i, \mathbf{M}_i$.  Let $\delta\mathbf{E} = \mathbf{E}_a - \mathbf{E}_b$,
$\delta\mathbf{H} = \mathbf{H}_a - \mathbf{H}_b$.  From Maxwell's equations:

$$
\nabla \times \delta\mathbf{E} = -j\omega\mu\,\delta\mathbf{H}, \qquad
\nabla \times \delta\mathbf{H} = (j\omega\epsilon + \sigma)\,\delta\mathbf{E}.
$$

Forming $\nabla\cdot(\delta\mathbf{E} \times \delta\mathbf{H}^*)$ and integrating over $V$:

$$
\oint_S (\delta\mathbf{E} \times \delta\mathbf{H}^*) \cdot d\mathbf{S}
= \int_V \bigl[-j\omega\mu|\delta\mathbf{H}|^2 + (j\omega\epsilon^* - \sigma)|\delta\mathbf{E}|^2\bigr]\,dV.
$$

Under one of the three boundary conditions, the surface integral vanishes.  For a lossy
medium ($\epsilon'', \mu'', \sigma > 0$), the real part gives
$\int_V [(\omega\epsilon''+\sigma)|\delta\mathbf{E}|^2 + \omega\mu''|\delta\mathbf{H}|^2]\,dV = 0$,
forcing $\delta\mathbf{E} = \delta\mathbf{H} = 0$ everywhere.

### Example 3.1 — Electrostatic Uniqueness

For $\nabla \times \mathbf{E} = 0$, $\nabla \cdot (\epsilon\mathbf{E}) = \rho_e$, let
$\mathbf{E} = -\nabla\varphi$.  If $\varphi_a$ and $\varphi_b$ both satisfy
$\nabla\cdot(\epsilon\nabla\varphi) = -\rho_e$, then $\delta\varphi = \varphi_a - \varphi_b$
satisfies $\nabla\cdot(\epsilon\nabla\delta\varphi) = 0$.  Using Green's first identity:

$$
\int_V \epsilon|\delta\mathbf{E}|^2\,dV = \oint_S \epsilon\,\delta\varphi\,\frac{\partial\delta\varphi}{\partial n}\,dS.
$$

If either the normal component $\hat{n}\cdot\mathbf{E}$ or the tangential component
(hence $\delta\varphi$ on $S$) is specified, the RHS vanishes, proving uniqueness.

### Example 3.2 — Time-Varying Uniqueness

For general time-varying fields, the same approach gives:

$$
\oint_S (\delta\mathbf{E} \times \delta\mathbf{H})\cdot d\mathbf{S}
= -\frac{\partial}{\partial t}\int_V \Bigl(\frac{\epsilon}{2}|\delta\mathbf{E}|^2 + \frac{\mu}{2}|\delta\mathbf{H}|^2\Bigr)dV
- \int_V \sigma|\delta\mathbf{E}|^2\,dV \le 0.
$$

With zero initial conditions ($t=0$) and specified tangential $\mathbf{E}$ or $\mathbf{H}$ on $S$,
the energy integral is identically zero, hence $\delta\mathbf{E} = \delta\mathbf{H} = 0$.

---

## 3.2 Image Theory (pp. 94–101)

Converts a **half-space** problem (source above a PEC/PMC ground plane) into a
**free-space** problem by placing image sources.

### 3.2.1 Basic Image Rules

| Source type | Above PEC ($\hat{n}\times\mathbf{E}=0$) | Above PMC ($\hat{n}\times\mathbf{H}=0$) |
|---|---|---|
| Vertical electric dipole | Same orientation | Opposite orientation |
| Horizontal electric dipole | Opposite orientation | Same orientation |
| Vertical magnetic dipole | Opposite orientation | Same orientation |
| Horizontal magnetic dipole | Same orientation | Opposite orientation |

For an **arbitrary electric current** $\mathbf{J}(\mathbf{r})$ above an electric ground plane
($z=0$):

$$
\mathbf{J}_{\text{im}}(\mathbf{r}) = 2\hat{z}\hat{z}\!\cdot\!\mathbf{J}(\mathbf{r}_i) - \mathbf{J}(\mathbf{r}_i),
\qquad \mathbf{r}_i = x\hat{x} + y\hat{y} - z\hat{z}.
$$

Likewise for **magnetic current** $\mathbf{M}(\mathbf{r})$:

$$
\mathbf{M}_{\text{im}}(\mathbf{r}) = -2\hat{z}\hat{z}\!\cdot\!\mathbf{M}(\mathbf{r}_i) + \mathbf{M}(\mathbf{r}_i).
$$

### Example 3.3 — Images Between Two Parallel Conducting Planes

For a current element $Il\hat{u}$ at $x = d$ between two PEC planes at $x=0$ and $x=l$,
two infinite image sets are required:

- Same-orientation images at $x = 2il + d$ ($-\infty < i < \infty$)
- Opposite-orientation images at $x = 2jl - d$, with $\hat{u}_{\text{im}} = 2\hat{x}\hat{x}\!\cdot\!\hat{u} - \hat{u}$

The field is:

$$
\mathbf{E}(\mathbf{r}) = -j\omega\mu Il\Bigl[\sum_{i=-\infty}^{\infty} \mathbf{G}_{e0}(\mathbf{r},\mathbf{r}_i)\cdot\hat{u}
+ \sum_{j=-\infty}^{\infty} \mathbf{G}_{e0}(\mathbf{r},\mathbf{r}_j)\cdot\hat{u}_{\text{im}}\Bigr],
\quad 0 \le x \le l.
$$

### 3.2.2 Half-Space Dyadic Green's Functions

For a PEC ground plane at $z=0$ ($\mathbf{r}'_i = x'\hat{x} + y'\hat{y} - z'\hat{z}$):

**Electric field**:

$$
\mathbf{E}(\mathbf{r}) = -j\omega\mu \int_V \mathbf{G}_{e1}(\mathbf{r},\mathbf{r}') \cdot \mathbf{J}(\mathbf{r}')\,dV'
- \int_V \mathbf{G}_{m1}(\mathbf{r},\mathbf{r}') \cdot \mathbf{M}(\mathbf{r}')\,dV',
$$

where

$$
\begin{aligned}
\mathbf{G}_{e1}(\mathbf{r},\mathbf{r}') &= \Bigl(\mathbf{I} - \frac{1}{k^2}\nabla'\nabla\Bigr)
[G_0(\mathbf{r},\mathbf{r}') - G_0(\mathbf{r},\mathbf{r}'_i)] + 2\hat{z}\hat{z}\,G_0(\mathbf{r},\mathbf{r}'_i), \\[4pt]
\mathbf{G}_{m1}(\mathbf{r},\mathbf{r}') &= -\nabla'[G_0(\mathbf{r},\mathbf{r}') + G_0(\mathbf{r},\mathbf{r}'_i)] \times \mathbf{I}.
\end{aligned}
$$

**Magnetic field**:

$$
\mathbf{H}(\mathbf{r}) = \int_V \mathbf{G}_{m2}(\mathbf{r},\mathbf{r}') \cdot \mathbf{J}(\mathbf{r}')\,dV'
- j\omega\epsilon \int_V \mathbf{G}_{e2}(\mathbf{r},\mathbf{r}') \cdot \mathbf{M}(\mathbf{r}')\,dV',
$$

where

$$
\begin{aligned}
\mathbf{G}_{e2}(\mathbf{r},\mathbf{r}') &= \Bigl(\mathbf{I} - \frac{1}{k^2}\nabla'\nabla\Bigr)
[G_0(\mathbf{r},\mathbf{r}') + G_0(\mathbf{r},\mathbf{r}'_i)] - 2\hat{z}\hat{z}\,G_0(\mathbf{r},\mathbf{r}'_i), \\[4pt]
\mathbf{G}_{m2}(\mathbf{r},\mathbf{r}') &= -\nabla'[G_0(\mathbf{r},\mathbf{r}') - G_0(\mathbf{r},\mathbf{r}'_i)] \times \mathbf{I}.
\end{aligned}
$$

---

## 3.3 Reciprocity Theorems (pp. 101–106)

Relates two independent EM fields produced by two different sets of sources in the same
(reciprocal) medium.

### 3.3.1 General Reciprocity Theorem

$$
\boxed{\nabla\cdot(\mathbf{H}_2 \times \mathbf{E}_1 - \mathbf{H}_1 \times \mathbf{E}_2)
= \mathbf{E}_1\!\cdot\!\mathbf{J}_2 + \mathbf{H}_2\!\cdot\!\mathbf{M}_1 - \mathbf{E}_2\!\cdot\!\mathbf{J}_1 - \mathbf{H}_1\!\cdot\!\mathbf{M}_2}
$$

In integral form over volume $V$ bounded by $S$:

$$
\boxed{\oint_S (\mathbf{H}_2 \times \mathbf{E}_1 - \mathbf{H}_1 \times \mathbf{E}_2)\cdot d\mathbf{S}
= \int_V (\mathbf{E}_1\!\cdot\!\mathbf{J}_2 + \mathbf{H}_2\!\cdot\!\mathbf{M}_1 - \mathbf{E}_2\!\cdot\!\mathbf{J}_1 - \mathbf{H}_1\!\cdot\!\mathbf{M}_2)\,dV}.
$$

Valid when the $\bm{\epsilon}, \bm{\mu}, \bm{\sigma}$ tensors are **symmetric** (reciprocal media).

### 3.3.2 Lorentz Reciprocity Theorem

In a **source-free** region, or on a surface containing **all** sources:

$$
\nabla\cdot(\mathbf{H}_2 \times \mathbf{E}_1 - \mathbf{H}_1 \times \mathbf{E}_2) = 0,
\qquad
\oint_S (\mathbf{H}_2 \times \mathbf{E}_1 - \mathbf{H}_1 \times \mathbf{E}_2) \cdot d\mathbf{S} = 0.
$$

### 3.3.3 Rayleigh–Carson Reciprocity Theorem (Reaction Concept)

Define **reaction** of field "1" on source "2":

$$
\langle 1,2 \rangle \equiv \int_V (\mathbf{E}_1\!\cdot\!\mathbf{J}_2 - \mathbf{H}_1\!\cdot\!\mathbf{M}_2)\,dV.
$$

Then:

$$
\boxed{\langle 1,2 \rangle = \langle 2,1 \rangle}.
$$

**Key consequence**: A tangential electric current on a PEC surface does **not radiate**.

**Antenna application**: The radiation pattern equals the receiving pattern.

### Example 3.4 — Aperture Radiation via Reciprocity

A rectangular aperture $a \times b$ in a PEC plane at $z=0$ with aperture field
$\mathbf{E}_a = \hat{y}E_0\cos(\pi x/a)$ yields far field ($r,\theta,\phi$):

$$
\begin{aligned}
E_{2\theta} &= j\frac{2aE_0}{r}\,e^{-jkr}\,
\frac{\cos\!\bigl(\frac{ka}{2}\sin\theta\cos\phi\bigr)
      \sin\!\bigl(\frac{kb}{2}\sin\theta\sin\phi\bigr)}
     {[\pi^2 - (ka\sin\theta\cos\phi)^2]\,\sin\theta}, \\[6pt]
E_{2\phi} &= j\frac{2aE_0}{r}\,e^{-jkr}\,
\frac{\cos\!\bigl(\frac{ka}{2}\sin\theta\cos\phi\bigr)
      \sin\!\bigl(\frac{kb}{2}\sin\theta\sin\phi\bigr)}
     {[\pi^2 - (ka\sin\theta\cos\phi)^2]\,\tan\theta\tan\phi}.
\end{aligned}
$$

---

## 3.4 Equivalence Principles (pp. 107–119)

### 3.4.1 Surface Equivalence Principle (Huygens' Principle)

For any closed surface $S$ separating interior from exterior, the exterior field can be
reproduced by placing **equivalent surface currents** on $S$:

$$
\mathbf{J}_s = \hat{n} \times (\mathbf{H} - \mathbf{H}'), \qquad
\mathbf{M}_s = (\mathbf{E} - \mathbf{E}') \times \hat{n}.
$$

**Love's equivalence** (zero interior field $\mathbf{E}' = \mathbf{H}' = 0$):

$$
\mathbf{J}_s = \hat{n} \times \mathbf{H}, \qquad
\mathbf{M}_s = \mathbf{E} \times \hat{n}.
$$

If the interior is filled with PEC, only $\mathbf{M}_s = \mathbf{E} \times \hat{n}$ radiates.
If filled with PMC, only $\mathbf{J}_s = \hat{n} \times \mathbf{H}$ radiates.

### 3.4.2 Scattering by a Conducting Object — Physical Optics (PO)

For a PEC object, the scattered field is:

$$
\mathbf{E}^{\text{sc}}(\mathbf{r}) = -j\omega\mu \oint_S \mathbf{G}_{e0}(\mathbf{r},\mathbf{r}')
\cdot [\hat{n}' \times \mathbf{H}(\mathbf{r}')]\,dS'.
$$

**PO approximation** (large, smooth PEC):

$$
\mathbf{J}_s \approx \begin{cases}
2\hat{n} \times \mathbf{H}^{\text{inc}} & \text{on illuminated side}, \\
0 & \text{on shadow side}.
\end{cases}
$$

**Induction theorem**: $\mathbf{M}_s = \hat{n} \times \mathbf{E}^{\text{inc}}$ on PEC surface;
use image theory for large objects.

### Example 3.5 — PO for Circular Conducting Plate

Incident $\mathbf{E}^{\text{inc}} = \hat{x}E_0 e^{jk_0z}$, radius $a$:

$$
\mathbf{E}^{\text{sc}} \approx -\frac{jaE_0}{r\sin\theta}\,J_1(k_0 a\sin\theta)\,e^{-jk_0r}
(\hat{\theta}\cos\theta\cos\phi - \hat{\phi}\sin\phi).
$$

### Example 3.6 — Induction Theorem for Circular Plate

Same geometry, using $\mathbf{M}_s$ doubled by image:

$$
\mathbf{E}^{\text{sc}} \approx -\frac{jaE_0}{r\sin\theta}\,J_1(k_0 a\sin\theta)\,e^{-jk_0r}
(\hat{\theta}\cos\phi - \hat{\phi}\cos\theta\sin\phi).
$$

The two results agree in backward/forward directions but differ in angular pattern.

### 3.4.3 Scattering by a Dielectric Object

Two coupled surface integral equations (PMCHWT formulation) using equivalent currents
$\mathbf{J}_s = \hat{n}\times\mathbf{H}$, $\mathbf{M}_s = \mathbf{E}\times\hat{n}$.

### 3.4.4 Volume Equivalence Principle & Born Approximation

Replace object by equivalent **volume currents**:

$$
\mathbf{J}_{\text{eq}} = j\omega[\tilde{\epsilon}(\mathbf{r}) - \epsilon]\,\mathbf{E},
\qquad
\mathbf{M}_{\text{eq}} = j\omega[\tilde{\mu}(\mathbf{r}) - \mu]\,\mathbf{H}.
$$

First-order **Born approximation** (weak scatterer):

$$
\mathbf{E}(\mathbf{r}) \approx \mathbf{E}^{\text{inc}}(\mathbf{r})
+ \omega^2\mu \int_{V_o} \mathbf{G}_{e0}(\mathbf{r},\mathbf{r}')
  \cdot (\tilde{\epsilon}-\epsilon)\,\mathbf{E}^{\text{inc}}(\mathbf{r}')\,dV'.
$$

### Example 3.7 — Rayleigh Scattering by Small Dielectric Sphere

$ka \ll 1$, $\epsilon_r$, $\mathbf{E}^{\text{inc}} = \hat{x}E_0 e^{-jk_0z}$:

$$
\mathbf{E}^{\text{int}} \approx \hat{x}\,\frac{3}{\epsilon_r+2}\,E_0,
\qquad
E^{\text{sc}} \propto k_0^2 a^3\,\frac{\epsilon_r-1}{\epsilon_r+2}\,E_0\,\frac{e^{-jk_0r}}{r}.
$$

Scattered power $\propto 1/\lambda_0^4$ — Rayleigh scattering (blue sky).

---

## 3.5 Duality Principle (pp. 120–121)

Swap variables in Maxwell's equations:

$$
\mathbf{E} \to \mathbf{H},\quad
\mathbf{H} \to -\mathbf{E},\quad
\mathbf{J} \to \mathbf{M},\quad
\mathbf{M} \to -\mathbf{J},\quad
\epsilon \to \mu,\quad
\mu \to \epsilon,\quad
\mathbf{A} \to \mathbf{F},\quad
\mathbf{F} \to -\mathbf{A}.
$$

Normalized form (preserving $\eta = \sqrt{\mu/\epsilon}$):

$$
\mathbf{E} \to \eta\mathbf{H},\quad
\mathbf{H} \to -\mathbf{E}/\eta,\quad
\mathbf{J} \to \mathbf{M}/\eta,\quad
\mathbf{M} \to -\eta\mathbf{J}.
$$

---

## 3.6 Aperture Radiation and Scattering (pp. 121–128)

### 3.6.1 Equivalent Problems

For a PEC screen with an aperture:
1. Seal aperture with PEC → form ground plane.
2. Replace aperture field by $\mathbf{M}_s = \mathbf{E}\times\hat{n}$ over aperture.
3. Image theory → $\mathbf{M}_s = 2\mathbf{E}\times\hat{n}$ radiating in free space.

**Rectangular waveguide opening** ($a\times b$, TE$_{10}$ mode):

$$
\begin{aligned}
E_\theta &= j\frac{2aE_0}{r}e^{-jkr}\,
\frac{\cos\!\bigl(\frac{ka}{2}\sin\theta\cos\phi\bigr)
      \sin\!\bigl(\frac{kb}{2}\sin\theta\sin\phi\bigr)}
     {[\pi^2 - (ka\sin\theta\cos\phi)^2]\,\sin\theta}, \\[4pt]
E_\phi &= j\frac{2aE_0}{r}e^{-jkr}\,
\frac{\cos\!\bigl(\frac{ka}{2}\sin\theta\cos\phi\bigr)
      \sin\!\bigl(\frac{kb}{2}\sin\theta\sin\phi\bigr)}
     {[\pi^2 - (ka\sin\theta\cos\phi)^2]\,\tan\theta\tan\phi}.
\end{aligned}
$$

### 3.6.2 Babinet's Principle

For an apertured PEC screen and its complementary PMC plate:

$$
\mathbf{E}_a + \mathbf{E}_m = \mathbf{E}^{\text{inc}},\qquad
\mathbf{H}_a + \mathbf{H}_m = \mathbf{H}^{\text{inc}}.
$$

Via duality (PMC → PEC plus dual source):

$$
\mathbf{E}_a + \eta\mathbf{H}_d = \mathbf{E}^{\text{inc}},\qquad
\mathbf{H}_a - \frac{\mathbf{E}_d}{\eta} = \mathbf{H}^{\text{inc}}.
$$

### 3.6.3 Complementary Antennas

For two complementary planar structures:

$$
\boxed{Z_a Z_c = \frac{\eta^2}{4}}.
$$

A **self-complementary** antenna has $Z_a = Z_c = \eta/2$ — constant input impedance
(wideband antennas: log-periodic, spiral).

---

## Key Formulas Summary

| Concept | Formula |
|---|---|
| Uniqueness condition | Specify $\hat{n}\times\mathbf{E}$ or $\hat{n}\times\mathbf{H}$ on $S$ |
| Image (PEC, arbitrary $\mathbf{J}$) | $\mathbf{J}_{\text{im}} = 2\hat{z}\hat{z}\!\cdot\!\mathbf{J}(\mathbf{r}_i) - \mathbf{J}(\mathbf{r}_i)$ |
| General Reciprocity | $\nabla\cdot(\mathbf{H}_2\times\mathbf{E}_1 - \mathbf{H}_1\times\mathbf{E}_2) = \mathbf{E}_1\!\cdot\!\mathbf{J}_2 + \mathbf{H}_2\!\cdot\!\mathbf{M}_1 - \mathbf{E}_2\!\cdot\!\mathbf{J}_1 - \mathbf{H}_1\!\cdot\!\mathbf{M}_2$ |
| Rayleigh–Carson | $\langle 1,2 \rangle = \langle 2,1 \rangle$ |
| Love's Equivalence | $\mathbf{J}_s = \hat{n}\times\mathbf{H},\; \mathbf{M}_s = \mathbf{E}\times\hat{n}$ |
| PO approximation | $\mathbf{J}_s \approx 2\hat{n}\times\mathbf{H}^{\text{inc}}$ (lit side) |
| Volume equivalence | $\mathbf{J}_{\text{eq}} = j\omega(\tilde{\epsilon}-\epsilon)\mathbf{E}$ |
| Complement. antennas | $Z_a Z_c = \eta^2/4$ |

---

## Figures Generated

| File | Description |
|---|---|
| `ex35_po_pattern.png` | PO: circular plate radiation pattern |
| `ex35_po_cuts.png` | PO: E/H plane cuts |
| `ex35_po_map.png` | PO: pattern colormap |
| `ex35_vs_ex36_compare.png` | PO vs induction theorem comparison |
| `ex36_induction_pattern.png` | Induction theorem radiation pattern |
| `ex36_induction_cuts.png` | Induction theorem cuts |
| `ex36_aperture_pattern.png` | Rectangular aperture pattern |
| `ex36_aperture_cuts.png` | Aperture E/H plane cuts |
| `ex37_rayleigh_pattern.png` | Rayleigh sphere pattern |
| `ex37_rayleigh_map.png` | Rayleigh sphere colormap |
| `ex37_rayleigh_sweep.png` | Rayleigh $\sigma$ vs. frequency sweep |
