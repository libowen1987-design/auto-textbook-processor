# Jackson Ch13: Collisions, Energy Loss, and Scattering

## Overview
Energy loss of charged particles passing through matter; scattering collisions; stopping power; range.

---

## §13.1 – Scattering Cross Section and Energy Loss

### Kinematics of Elastic Scattering

**Lab frame**: projectile (mass $m$, charge $z e$) hits stationary target ($M$, $Ze$).

**Energy transfer in a single collision**:
$$
\Delta E = \frac{2 m M}{(m+M)^2} \, p^2 (1 - \cos\Theta_{cm})
$$
where $\Theta_{cm}$ is the scattering angle in the center-of-mass frame.

For $m \ll M$ (electron on heavy nucleus):
$$
\Delta E \approx \frac{p^2}{M} (1 - \cos\Theta_{cm}) \quad \text{or} \quad \Delta E_{\text{max}} = \frac{2p^2}{M}
$$

### Differential Cross Section for Scattering

Rutherford scattering (Coulomb potential):
$$
\frac{d\sigma}{d\Omega} = \left( \frac{z Z e^2}{4p v} \right)^2 \frac{1}{\sin^4(\Theta/2)}
$$

Energy-loss differential cross section:
$$
\frac{d\sigma}{d\Delta E} = \frac{2\pi z^2 Z^2 e^4}{m v^2} \frac{1}{(\Delta E)^2} \quad \text{(non-relativistic)}
$$

---

## §13.2 – Energy Loss for Moderately Heavy Charged Particles — Stopping Power

### Bethe-Bloch Formula (non-relativistic, heavy incident particle)

Stopping power (energy loss per unit path length):
$$
-\frac{dE}{dx} = \frac{4\pi N_a z^2 e^4}{m_e v^2} Z \rho \frac{1}{A} \left[ \ln\frac{2 m_e v^2}{I} + \text{corrections} \right]
$$

where:
- $N_a$ = Avogadro's number
- $m_e$ = electron mass
- $z e$ = projectile charge, $v$ = projectile speed
- $Z$ = atomic number of medium, $A$ = atomic weight
- $\rho$ = density, $I$ = mean excitation potential ($I \approx 10Z$ eV for $Z \lesssim 30$)
- $\rho$ in g/cm³ → $dE/dx$ in MeV/cm

### Bethe-Bloch (relativistic)

$$
-\frac{dE}{dx} = \frac{4\pi N_a r_e^2 m_e c^2 z^2}{\beta^2} \frac{Z\rho}{A} \left[ \frac12 \ln\frac{2 m_e c^2 \beta^2 \gamma^2 T_{\text{max}}}{I^2} - \beta^2 - \frac{\delta}{2} \right]
$$

where:
- $r_e = e^2/m_e c^2$ = classical electron radius
- $T_{\text{max}} = \frac{2 m_e c^2 \beta^2 \gamma^2}{1 + 2\gamma m_e/M + (m_e/M)^2}$ = max kinetic energy transfer
- $\delta$ = density effect correction (Fermi plateau)
- Validity: $0.1 \lesssim \beta\gamma \lesssim 1000$ for heavy charged particles

### Key Features

1. **$1/\beta^2$ dependence** at low energies → Bragg peak near end of range
2. **Relativistic rise** (ln $\gamma$) → "Fermi plateau" after density correction
3. **Minimum ionizing particles** (MIP) at $\beta\gamma \approx 3$–4
4. **Barkas effect**: $z^3$ correction for very slow particles

---

## §13.3 – Range and Straggling

### Range

Continuous Slowing Down Approximation (CSDA) range:
$$
R(T) = \int_0^T \frac{dE}{(-dE/dx)}
$$

**Empirical range relation** (non-relativistic): $R \propto M v^{3.2}$ for same $z$ at same $v$

### Straggling

Energy-loss fluctuations due to the stochastic nature of collisions:
- **Vavilov distribution**: general case (Landau for thin absorbers, Gaussian for thick)
- **Energy straggling** $\propto \sqrt{x}$ for thick absorbers
- **Range straggling** $\Delta R/R \propto 1/\sqrt{N}$ where $N$ = number of collisions

---

## §13.4 – Energy Loss for Electrons and Positrons

### Electrons are different from heavy particles:
1. Mass = target mass → large energy transfer in single collision
2. **Bremssstrahlung** significant at high energy (radiative vs. collision loss)

**Collision loss** (Bhabha for $e^+$, Møller for $e^-$):
$$
-\left(\frac{dE}{dx}\right)_{\text{coll}} = \frac{4\pi N_a r_e^2 m_e c^2}{\beta^2} \frac{Z\rho}{A} \times \text{logarithmic term}
$$

**Critical energy** $E_c$ where collision loss = radiative loss:
- For most materials: $E_c \approx 800\,\text{MeV}/(Z+1.2)$
- Above $E_c$: radiation dominates

**Radiation length** $X_0$ (mean distance for $1/e$ energy loss via bremsstrahlung):
$$
X_0 \approx \frac{716.4\,\text{g/cm}^2 \cdot A}{Z(Z+1)\ln(287/\sqrt{Z})}
$$

---

## §13.5 – Energy Loss for Light Ions

Extension of Bethe-Bloch to light ions ($p$, $d$, $\alpha$):
$$
-\frac{dE}{dx} = z^2 f(\beta)
$$
where $f(\beta)$ depends on the medium but not on projectile charge or mass (at same velocity).

**Rigidity**: $p/Z$ (momentum per unit charge) determines trajectory in magnetic fields.

---

## §13.6 – Multiple Scattering

### Molière Theory

Angular distribution from many small-angle Coulomb scatterings:
- **Gaussian core**: $\theta \propto \sqrt{x} / (p v)$ for small angles
- **Power-law tails** from single large-angle events

**RMS scattering angle**:
$$
\theta_{\text{rms}} = \frac{13.6\,\text{MeV}}{\beta c p} \sqrt{\frac{x}{X_0}} \left[ 1 + 0.038 \ln\left(\frac{x}{X_0}\right) \right]
$$

**Planar projection**: $\theta_{\text{plane, rms}} = \theta_{\text{space, rms}} / \sqrt{3}$

---

## §13.7 – Cherenkov Radiation

### Threshold
Particle velocity $v > c/n$ (exceeds phase velocity of light in medium)
Threshold $\beta > 1/n$

### Angle
$$
\cos\theta_c = \frac{1}{\beta n}
$$

Energy radiated per unit path length:
$$
\frac{dE}{dx} = \frac{e^2}{c^2} \int_{\beta n > 1} \omega \left(1 - \frac{1}{\beta^2 n^2(\omega)}\right) d\omega
$$

### Applications
- Cherenkov counters for particle identification
- Ring Imaging Cherenkov (RICH) detectors

---

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Bethe-Bloch (relativistic) | $-\frac{dE}{dx} = K \frac{z^2}{\beta^2} \frac{Z}{A} \left[ \frac12 \ln \frac{2m_e c^2 \beta^2 \gamma^2 T_{\text{max}}}{I^2} - \beta^2 - \frac{\delta}{2} \right]$ |
| Rutherford cross section | $\frac{d\sigma}{d\Omega} = \left( \frac{zZe^2}{4pv} \right)^2 \csc^4\frac{\Theta}{2}$ |
| Multiple scattering RMS | $\theta_{\text{rms}} = \frac{13.6\,\text{MeV}}{\beta c p} \sqrt{x/X_0} [1 + 0.038 \ln(x/X_0)]$ |
| Cherenkov angle | $\cos\theta_c = 1/(\beta n)$ |
| Critical energy | $E_c \approx 800/(Z+1.2)$ MeV |
