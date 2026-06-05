# Jackson Ch15: Bremsstrahlung, Virtual Quanta, and Energy Loss

## Overview
Radiation emitted when charged particles are accelerated in Coulomb fields of nuclei. The Weizsacker-Williams method of virtual quanta.

---

## §15.1 – Bremsstrahlung in a Coulomb Field

### Classical Bremsstrahlung

A charged particle with charge $ze$ colliding with a nucleus of charge $Ze$.

**Radiation energy per unit frequency** (classical, non-relativistic):

$$
\frac{dI}{d\omega} = \frac{8}{3\pi} \frac{z^2 Z^2 e^6}{(4\pi\epsilon_0)^3} \frac{1}{m^2 v_1^2 c^3} \ln\left( \frac{v_1 + v_2}{v_1 - v_2} \right)
$$

where $v_1$ is initial velocity, $v_2$ is final velocity.

### Low-frequency limit

For $\omega \ll v/b_{\text{min}}$:
$$
\frac{dI}{d\omega} \approx \frac{16}{3} \frac{z^2 Z^2 e^6}{(4\pi\epsilon_0)^3} \frac{1}{m^2 c^3 v_1^2}
$$
Independent of $\omega$ → flat spectrum at low frequencies (infrared divergence).

### High-frequency cutoff

At $\omega \gg m v_1^2/\hbar$ (quantum regime): spectrum drops rapidly (quantum cutoff at $E_e = \hbar\omega_{\text{max}}$).

---

## §15.2 – Semiclassical and Quantum Treatment

### Born Approximation Cross Section

Differential cross section for bremsstrahlung:
$$
d\sigma = \alpha_f Z^2 r_e^2 \frac{d\omega}{\omega} \frac{p_2}{p_1} \left[ \text{angular and spin factors} \right]
$$

where $\alpha_f = e^2/(4\pi\epsilon_0 \hbar c) \approx 1/137$ is the fine-structure constant.

### Bethe-Heitler Formula (extreme relativistic limit)

For $E_1, E_2 \gg m_e c^2$:

$$
d\sigma = 4 \alpha_f Z^2 r_e^2 \frac{d\omega}{\omega} \left[ \left( 1 + \left(\frac{E_2}{E_1}\right)^2 - \frac{2}{3} \frac{E_2}{E_1} \right) \left( \ln\frac{2E_1 E_2}{m_e c^2 \hbar\omega} - \frac12 \right) \right]
$$

### Screening

**Complete screening** (Thomas-Fermi atom): multiply by $F_{\text{sc}}$ (screening function):
$$
d\sigma_{\text{sc}} = d\sigma_{\text{BH}} \cdot F_{\text{sc}}(\xi)
$$
where $\xi = 100 m_e c^2 \hbar\omega / (E_1 E_2 Z^{1/3})$.

**No screening** ($\xi \gg 1$): use unscreened Bethe-Heitler.

**Complete screening** ($\xi \ll 1$): 
$$
d\sigma = 4\alpha_f Z^2 r_e^2 \frac{d\omega}{\omega} \left( 1 + \left(\frac{E_2}{E_1}\right)^2 - \frac{2}{3}\frac{E_2}{E_1} \right) \left( \ln\frac{183}{Z^{1/3}} - f(Z) \right)
$$

---

## §15.3 – Energy Loss from Bremsstrahlung

### Radiative Stopping Power

Energy-loss rate from bremsstrahlung for electrons:
$$
-\left(\frac{dE}{dx}\right)_{\text{rad}} = N \int_0^{E_1} \hbar\omega \, d\sigma
$$

Leading to:
$$
-\left(\frac{dE}{dx}\right)_{\text{rad}} = \frac{E}{X_0}
$$

where $X_0$ is the radiation length.

### Total Energy Loss (electrons/positrons)

$$
-\frac{dE}{dx} = -\left(\frac{dE}{dx}\right)_{\text{coll}} - \left(\frac{dE}{dx}\right)_{\text{rad}}
$$

**Critical energy** $E_c$: where $(-dE/dx)_{\text{coll}} = (-dE/dx)_{\text{rad}}$

### Radiation Length
$$
X_0 = \frac{716.4\,\text{g/cm}^2 \cdot A}{Z(Z+1)\ln(287/\sqrt{Z})}
$$

For a high-energy electron traversing $t$ radiation lengths:
$$
E(t) = E_0 e^{-t}
$$

---

## §15.4 – Weizsacker-Williams Method of Virtual Quanta

### Key Idea
The electromagnetic field of a fast charged particle can be represented as a spectrum of virtual photons. When these virtual quanta interact with a target, the cross section = $\sigma_{\text{real-photon}} \times \text{photon spectrum}$.

### Virtual Photon Spectrum

Number of virtual photons per unit frequency:
$$
I(\omega, b) = \frac{2}{\pi} \frac{z^2 \alpha_f c}{v^2} \frac{1}{\omega} \left[ K_0^2\left(\frac{\omega b}{\gamma v}\right) + \frac{v^2}{\gamma^2 c^2} K_1^2\left(\frac{\omega b}{\gamma v}\right) \right]
$$

where $K_0$, $K_1$ are modified Bessel functions, $b$ = impact parameter.

### Integrated Spectrum (summed over all impact parameters > some minimum $b_{\min}$):

$$
N(\omega) \approx \frac{2}{\pi} \frac{z^2 \alpha_f}{c} \frac{1}{\omega} \ln\left( \frac{\gamma v}{\omega b_{\min}} \right) \quad \text{for } \omega \ll \gamma v/b_{\min}
$$

### Applications

1. **Bremsstrahlung cross section**: $\sigma_{\text{brem}} = \int N(\omega) \sigma_{\gamma}(\omega) d\omega$
2. **Electro-disintegration** of nuclei: virtual photon excitation
3. **Pair production** by virtual photons
4. **Ionization energy loss**: virtual photon absorption by atomic electrons

---

## §15.5 – Connection of Virtual Quanta Method with Energy Loss

### Bethe-Bloch from Virtual Quanta

Energy loss = energy absorbed from virtual photon field:
$$
-\frac{dE}{dx} = \int_0^{\infty} \hbar\omega \, n \cdot \sigma_{\gamma}^{\text{abs}}(\omega) \, N(\omega) \, d\omega
$$

Recovers the Bethe-Bloch formula:
$$
-\frac{dE}{dx} = \frac{4\pi z^2 e^4}{m_e v^2} NZ \ln\left( \frac{2m_e v^2}{I} \right) \quad \text{(non-relativistic)}
$$

### Key Insight
The W-W method is very general: any process that can occur with real photons also occurs with virtual photons, with cross section = $\sigma_{\text{real}} \times \text{flux of virtual quanta}$.

### Limitations
- Valid when $\gamma \gg 1$ (ultrarelativistic)
- Assumes straight-line trajectory (small deflection)
- Impact parameter cutoff needed: $b_{\min} \sim \max(\hbar/(mc), \hbar/\gamma mc)$

---

## Key Formulas Summary

| Concept | Formula |
|---------|---------|
| Classical bremsstrahlung spectrum | $\frac{dI}{d\omega} = \frac{8}{3\pi} \frac{z^2 Z^2 e^6}{m^2 c^3 v_1^2} \frac{1}{(4\pi\epsilon_0)^3}$ |
| Bethe-Heitler cross section (relativistic) | $d\sigma = 4\alpha_f Z^2 r_e^2 \frac{d\omega}{\omega} [\ldots]$ with screening |
| Radiative energy loss | $-\frac{dE}{dx} = \frac{E}{X_0}$ |
| Radiation length | $X_0 \approx \frac{716.4 A}{Z(Z+1)\ln(287/\sqrt{Z})}$ g/cm² |
| Virtual photon spectrum | $N(\omega) \approx \frac{2}{\pi} \frac{z^2 \alpha_f}{c} \frac{1}{\omega} \ln(\gamma v/\omega b_{\min})$ |
| Fine-structure constant | $\alpha_f = e^2/(4\pi\epsilon_0\hbar c) \approx 1/137$ |
