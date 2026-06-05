---
chapter: 7
title: Passive Devices
source: Razavi, "RF Microelectronics", 2nd Ed.
pages: p455-522 (book pp.431-498)
---

# Ch7: Passive Devices

## 7.1 On-Chip Inductors (p431-455)

**Inductor structures:**
- Spiral inductors (square, octagonal, circular)
- Top metal layer for minimum loss
- Shielded vs unshielded

**Inductor model** (Fig 7.5):
- $L_S$: series inductance
- $R_S$: series resistance (metal + skin effect)
- $C_{ox}$: oxide capacitance to substrate
- $C_{sub}$, $R_{sub}$: substrate parasitics

**Quality factor:**
$$Q = \frac{\omega L_S}{R_S} \cdot \frac{R_P}{R_P + [(\omega L_S/R_S)^2 + 1]R_S}$$

Peak $Q$ occurs where $\omega L_S/R_S \approx R_P/(\omega L_S)$.

**Example 7.1 (p435-436):** 5 nH spiral inductor, $R_S=5\;\Omega$, $R_P=1$ kΩ, $f=2.4$ GHz → $Q \approx 11$.

**Self-resonant frequency ($f_{SR}$):**
- Determined by $L_S$ and $C_{ox} + C_{sub}$
- Above $f_{SR}$, inductor behaves capacitively
- Design rule: $f_0 < 0.5 f_{SR}$

**Temperature dependence:**
- $R_S$ increases with $T$ → $Q$ decreases
- $L_S$ stable with $T$

## 7.2 On-Chip Transformers (p455-465)

**Transformer model:**
- $k$: coupling coefficient (0.5-0.9 typical)
- $n$: turns ratio
- Magnetizing and leakage inductances

**Key metrics:**
- Insertion loss: 1-3 dB typical
- Bandwidth: limited by self-resonance

## 7.3 On-Chip Capacitors (p465-475)

**MIM capacitors:**
- High density (1-5 fF/μm²)
- Good linearity
- Low parasitics

**MOS capacitors:**
- High density but nonlinear
- Accumulation-mode preferred

**Varactors (MOS varactors):**
- $C_{\text{max}}/C_{\text{min}}$ ratio: 2-4
- $Q$: 20-100 at GHz
- Tuning range limited

**Example 7.6 (p469-470):** MOS varactor tuning range: $C_{\text{max}}/C_{\text{min}} = 3$, $Q = 30$ at 2.4 GHz.

## 7.4 Transmission Lines (p475-488)

**On-chip transmission lines:**
- Microstrip, coplanar waveguide (CPW)
- Characteristic impedance $Z_0 = \sqrt{(R+j\omega L)/(G+j\omega C)}$
- Loss: dB/mm (higher on Si substrate)

**For low-loss:**
- Top metal, thick dielectric (removed substrate)
- $Z_0$: 20-100 $\Omega$ achievable

## 7.5 Modeling and Simulation (p488-498)

- EM simulation (HFSS, Momentum) required for accurate modeling
- Lumped models valid only below $f_{SR}/5$
- Skin effect: $R_{AC} \propto \sqrt{f}$ above skin depth frequency

## Physical/Engineering Intuition

1. **Inductor Q is the bottleneck:** On-chip spiral inductors have Q ≈ 5-20. This limits LNA gain, VCO phase noise, and matching network loss.

2. **The substrate kills performance:** Silicon substrate losses dominate at high frequencies. Patterned ground shields reduce substrate loss by blocking electric field penetration.

3. **Transformers are area-hungry:** On-chip transformers occupy large area and have limited bandwidth. Used mainly for single-ended to differential conversion.

4. **Capacitors are the "easy" passive:** MIM capacitors are near-ideal at GHz frequencies. Varactors are the only practical tunable elements for VCOs.
