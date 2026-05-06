# Jackson Ch16: Radiation Damping, Classical Models of Charged Particles

## Overview
Reaction of radiation on the emitting charge; classical electron model; Abraham-Lorentz force; preacceleration and runaway solutions.

---

## §16.1 – Radiation Reaction and Self-Force

### The Problem
When a charged particle accelerates and radiates energy, the radiated energy must come from the particle's kinetic energy → a damping force appears.

### Energy Balance
$$
\frac{dE_{\text{mech}}}{dt} = -P_{\text{rad}} + \text{work done by external forces}
$$

The radiation reaction force $\mathbf{F}_{\text{rad}}$ is defined by:
$$
\mathbf{F}_{\text{rad}} \cdot \mathbf{v} = -P_{\text{rad}}
$$

---

## §16.2 – Abraham-Lorentz Force (Non-Relativistic)

### Derivation from Self-Field

For a non-relativistic extended charge distribution (radius $a$):

$$
\mathbf{F}_{\text{self}} \approx -\frac{q^2}{6\pi\epsilon_0 a c^2} \dot{\mathbf{v}} + \frac{q^2}{6\pi\epsilon_0 c^3} \ddot{\mathbf{v}} + O(a)
$$

### The Abraham-Lorentz Formula

In the limit $a \to 0$ (point particle):

$$
\mathbf{F}_{\text{rad}} = \frac{q^2}{6\pi\epsilon_0 c^3} \ddot{\mathbf{v}} \equiv m \tau_0 \ddot{\mathbf{v}}
$$

where:
$$
\tau_0 = \frac{q^2}{6\pi\epsilon_0 m c^3} \quad \text{(characteristic time scale)}
$$

For an electron:
$$
\tau_0 \approx 6.24 \times 10^{-24} \,\text{s} \quad \text{(or } 2/3 \, r_e/c \text{)}
$$

### Equation of Motion with Radiation Reaction

$$
m\ddot{\mathbf{x}} = \mathbf{F}_{\text{ext}} + m \tau_0 \dddot{\mathbf{x}}
$$

---

## §16.3 – Consistency Issues: Runaway and Preacceleration

### Runaway Solutions

For $\mathbf{F}_{\text{ext}} = 0$:
$$
m\ddot{\mathbf{x}} = m \tau_0 \dddot{\mathbf{x}}
$$
Solution: $\ddot{\mathbf{x}}(t) = \ddot{\mathbf{x}}(0) e^{t/\tau_0}$, which grows exponentially → **non-physical**.

### Preacceleration

The physical solution requires imposing $\ddot{\mathbf{x}} \to 0$ as $t \to \infty$ (no runaway).

For an external force $\mathbf{F}_{\text{ext}}(t)$:
$$
\ddot{\mathbf{x}}(t) = \frac{1}{m\tau_0} \int_t^{\infty} e^{-(t'-t)/\tau_0} \mathbf{F}_{\text{ext}}(t') \, dt'
$$

**Consequence**: acceleration depends on **future** forces → preacceleration (apparent violation of causality at the $\tau_0$ scale).

### The "Runaway or Preacceleration" Dilemma
- Point particle: must choose between acausal preacceleration or runaway
- Extended charge: removes both at the cost of internal forces

---

## §16.4 – Relativistic Generalization (Abraham-Lorentz-Dirac)

### Dirac's Relativistic Radiation Reaction

$$
F^\mu_{\text{rad}} = \frac{q^2}{6\pi\epsilon_0 c} \left( \frac{d^2 U^\mu}{d\tau^2} - \frac{U^\mu}{c^2} \frac{dU_\alpha}{d\tau} \frac{dU^\alpha}{d\tau} \right)
$$

where $U^\mu$ is the 4-velocity.

### Key Terms

1. **Schott term**: $\propto d^2U^\mu/d\tau^2$ — the relativistic $\ddot{\mathbf{v}}$
2. **Damping term**: $\propto U^\mu (dU_\alpha/d\tau)(dU^\alpha/d\tau)$ — 4-force that reduces energy

### ALD Equation of Motion

$$
m c \frac{dU^\mu}{d\tau} = \mathcal{F}^\mu_{\text{ext}} + \frac{q^2}{6\pi\epsilon_0 c} \left( \frac{d^2 U^\mu}{d\tau^2} - \frac{U^\mu}{c^2} \frac{dU_\alpha}{d\tau} \frac{dU^\alpha}{d\tau} \right)
$$

**Note**: The ALD equation is a third-order differential equation with the same runaway/preacceleration issues.

---

## §16.5 – Energy-Momentum of Radiating Charged Particle

### Landau-Lifshitz Reduction

The ALD equation can be reduced to a second-order equation by iterating (assuming $P_{\text{rad}}$ is a small correction to leading order):

$$
F^\mu_{\text{rad}} \approx \frac{q^2}{6\pi\epsilon_0 c} \left[ \frac{\mathcal{F}^{\mu\nu}_{\text{ext}} \mathcal{F}_{\nu\alpha}^{\text{ext}} U^\alpha}{m c} + \frac{1}{c^2} \left( \frac{\partial \mathcal{F}^{\mu\nu}_{\text{ext}}}{\partial x^\alpha} - \frac{\mathcal{F}^{\mu\alpha}_{\text{ext}} \mathcal{F}^{\mu\nu}_{\text{ext}} U_\nu}{m c} \right) U^\alpha \right]
$$

where $\mathcal{F}^{\mu\nu}_{\text{ext}}$ is the external electromagnetic field tensor.

### Energy-Momentum Tensor of a Point Charge

The total 4-momentum radiated = integral of stress-energy tensor flux through a timelike surface surrounding the worldline.

Radiation 4-momentum:
$$
dP^\mu_{\text{rad}} = \frac{q^2}{6\pi\epsilon_0 c^5} \frac{dU^\alpha}{d\tau} \frac{dU_\alpha}{d\tau} \, U^\mu d\tau
$$

---

## §16.6 – Line Broadening as Radiation Damping

### Classical Damped Oscillator

A radiating electron bound by a harmonic force:
$$
\ddot{x} + \Gamma \dot{x} + \omega_0^2 x = 0
$$

**Damping constant from radiation reaction**:
$$
\Gamma = \frac{q^2 \omega_0^2}{6\pi\epsilon_0 m c^3} = \frac{2}{3} \frac{r_e \omega_0^2}{c}
$$

### Spectral Line Shape

For a weakly damped oscillator $\Gamma \ll \omega_0$:

**Lorentzian line shape**:
$$
I(\omega) = I_0 \frac{\Gamma/2\pi}{(\omega - \omega_0)^2 + (\Gamma/2)^2}
$$

- FWHM = $\Gamma$
- Natural line width: $\Delta\omega = 1/\tau_{\text{decay}}$ where $\tau_{\text{decay}} = 1/\Gamma$

### Classical Lifetime

$$
\tau = \frac{1}{\Gamma} = \frac{3 m c^3}{2 r_e \omega_0^2}
$$

For optical transitions ($\lambda \sim 500$ nm): $\tau \sim 10^{-8}$ s

---

## §16.7 – Scattering and Absorption of Radiation

### Cross Section for a Damped Oscillator

$$
\sigma_{\text{abs}}(\omega) = \frac{\pi q^2}{m\epsilon_0 c} \frac{\Gamma \omega^2}{(\omega^2 - \omega_0^2)^2 + (\Gamma\omega)^2}
$$

**At resonance** $(\omega = \omega_0)$:
$$
\sigma_{\text{abs}}(\omega_0) = \frac{2\pi^2 q^2}{m\epsilon_0 c} \frac{1}{\Gamma} = \frac{6\pi c^2}{\omega_0^2}
$$

### Relation to Classical Electron Radius

$$
\sigma_{\text{abs}}(\omega_0) \approx \frac{3}{2} \lambda_0^2
$$

where $\lambda_0 = 2\pi c/\omega_0$ is the wavelength.

---

## §16.8 – The Classical Electron Model: Extended Charge

### Attempts to Remove Runaway/Preacceleration

1. **Semi-relativistic extended electron** (Lorentz model): finite radius $R$
2. **Rigid charge distribution**: momentum of electromagnetic field depends on velocity, but self-force complicated
3. **Nonrelativistic rigid sphere**: 
   $$
   m_{\text{em}} = \frac{4}{3} \frac{U_{\text{field}}}{c^2} \quad \text{(electromagnetic mass)}
   $$

### The 4/3 Problem

For a spherical shell of charge (radius $a$):
- Electrostatic energy: $U = q^2/(8\pi\epsilon_0 a)$
- Electromagnetic momentum gives mass: $m_{\text{em}} = (4/3) U/c^2$ (non-covariant result)

### Poincaré Stress

Poincaré proposed **cohesive non-electromagnetic forces** (Poincaré stresses) to stabilize the electron:
- Provides negative pressure → resolves 4/3 problem
- Restores covariant energy-momentum tensor

### Modern View

- Quantum electrodynamics (QED) handles radiation reaction properly
- At classical level, the Landau-Lifshitz equation is the practical form
- No need for extended charge models in modern physics

---

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Abraham-Lorentz force | $\mathbf{F}_{\text{rad}} = \frac{q^2}{6\pi\epsilon_0 c^3} \ddot{\mathbf{v}} = m \tau_0 \ddot{\mathbf{v}}$ |
| Characteristic time | $\tau_0 = \frac{q^2}{6\pi\epsilon_0 m c^3} \approx 6.24\times 10^{-24}$ s |
| Equation (non-relativistic) | $m\ddot{\mathbf{x}} = \mathbf{F}_{\text{ext}} + m\tau_0\dddot{\mathbf{x}}$ |
| ALD relativistic 4-force | $F^\mu_{\text{rad}} = \frac{q^2}{6\pi\epsilon_0 c} \left( \frac{d^2U^\mu}{d\tau^2} - \frac{U^\mu}{c^2} \frac{dU_\alpha}{d\tau}\frac{dU^\alpha}{d\tau} \right)$ |
| Damping constant | $\Gamma = \frac{2}{3}\frac{r_e\omega_0^2}{c}$ |
| Lorentzian line shape | $I(\omega) = I_0 \frac{\Gamma/(2\pi)}{(\omega-\omega_0)^2 + (\Gamma/2)^2}$ |
| Classical electron radius | $r_e = \frac{e^2}{4\pi\epsilon_0 m_e c^2} \approx 2.82\times 10^{-15}$ m |
| Absorption cross section (resonance) | $\sigma_{\text{abs}}(\omega_0) = \frac{6\pi c^2}{\omega_0^2}$ |
