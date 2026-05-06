---
chapter: 8
title: Oscillators
source: Razavi, "RF Microelectronics", 2nd Ed.
pages: p523-622 (book pp.499-598)
---

# Ch8: Oscillators

## 8.1 General Considerations (p499-504)

**Oscillation condition** (Barkhausen):
$$|H(j\omega_0)| \geq 1, \quad \angle H(j\omega_0) = 180^\circ$$

**Start-up condition:** Loop gain $> 1$ at $\omega_0$, settles to unity.

**Example 8.1 (p500-501):** Three-stage ring oscillator — each stage provides $60^\circ$ phase shift, DC gain $> 1$ → oscillation at $\omega_0 = \sqrt{3}/RC$.

## 8.2 LC Oscillators (p505-530)

### 8.2.1 Cross-Coupled LC VCO (p505-515)

**Standard topology** (Fig 8.5): Cross-coupled NMOS pair + $LC$ tank.

**Negative resistance:** $-2/g_m$ (differential)

**Oscillation frequency:** $\omega_0 = 1/\sqrt{L_p C_p}$

**Start-up condition:** $g_m R_p > 1$ (or $g_m > 1/R_p$)

**Example 8.2 (p505-506):** $L=5$ nH, $C=2$ pF → $f_0 = 1.59$ GHz. $R_p = 500\;\Omega$ → $g_m > 2$ mS needed.

**Phase noise:**
$$\mathcal{L}(\Delta\omega) = \frac{4kTR_p}{V_0^2} \cdot \left(\frac{\omega_0}{2Q\Delta\omega}\right)^2$$

**Example 8.5 (p510-511):** $f_0=2.4$ GHz, $Q=10$, $V_0=1$ V → PN at 1 MHz offset: $\mathcal{L} \approx -120$ dBc/Hz.

### 8.2.2 Colpitts Oscillator (p515-520)

- Higher startup gain for same power
- Better phase noise than cross-coupled (theoretically)
- More difficult to implement in CMOS

### 8.2.3 VCO Tuning (p520-530)

**Varactor tuning:**
$$\omega_0 = \frac{1}{\sqrt{L(C_{\text{fixed}} + C_{\text{var}}(V_{\text{tune}}))}}$$

**Tuning range:**
$$\frac{\omega_{\text{max}}}{\omega_{\text{min}}} = \sqrt{\frac{C_{\text{max}} + C_{\text{fixed}}}{C_{\text{min}} + C_{\text{fixed}}}}$$

**KVCO (gain):** $K_{VCO} = \frac{d\omega_0}{dV_{\text{tune}}} \propto - \frac{1}{2} \frac{\omega_0}{C_{\text{var}} + C_{\text{fixed}}} \cdot \frac{dC_{\text{var}}}{dV}$

**Example 8.8 (p522-523):** $L=5$ nH, varactor $C_{\text{max}}=2$ pF, $C_{\text{min}}=0.5$ pF, $C_{\text{fixed}}=1$ pF → tuning range $f_{\text{max}}/f_{\text{min}} = \sqrt{(2+1)/(0.5+1)} = 1.41$ → 40% tuning.

### 8.2.4 Amplitude Limiting (p530-538)

- Oscillation amplitude grows until nonlinearity limits it
- Current-limited vs voltage-limited regime
- In current-limited: $V_0 \approx I_{\text{tail}} R_p$

## 8.3 Phase Noise Theory (p538-552)

### Lesson's Model (p540-541):
$$\mathcal{L}(\Delta\omega) = 10\log\left[\frac{2FkT}{P_{\text{sig}}}\left(1 + \left(\frac{\omega_0}{2Q\Delta\omega}\right)^2\right)\left(1 + \frac{\Delta\omega_{1/f^3}}{|\Delta\omega|}\right)\right]$$

**Three regions:**
- $1/f^3$ region: $\propto 1/(\Delta\omega)^3$ (close-in)
- $1/f^2$ region: $\propto 1/(\Delta\omega)^2$ (mid-offset)
- Noise floor: flat (far-out)

**Example 8.12 (p541-543):** $P_{\text{sig}} = 0$ dBm, $Q=10$, $f_0=2.4$ GHz, $F = 4$ → PN = $-119$ dBc/Hz at 1 MHz offset.

**Pushing and pulling** (p543-548):
- **Pushing:** supply-dependent frequency variation
- **Pulling:** frequency variation due to load impedance

## 8.4 Ring Oscillators (p552-558)

- No inductor → small area
- Wide tuning range
- Poor phase noise

**Phase noise of ring oscillator:**
$$\mathcal{L}(\Delta\omega) = \frac{8kT}{3\eta P_{\text{sig}}} \cdot \frac{NV_{\text{DD}}}{\Delta\omega^2}$$

Where $\eta$ = proportionality constant, $N$ = number of stages.

## 8.5 Quadrature Generation (p558-568)

**Methods:**
1. RC-CR network (narrowband, process-sensitive)
2. Polyphase filters (wideband, lossy)
3. Divide-by-2 from $2f_0$ oscillator
4. Coupled oscillators

**Divide-by-2 quadrature:** Master-slave flip-flops → generate I/Q from $2f_{LO}$.

## 8.6 VCO Design Examples (p568-588)

**Design procedure** (Example 8.18, p570-572):
1. Choose $L$ and $f_0$ → $C_{\text{tot}}$
2. Size varactor for tuning range
3. Design cross-coupled pair for startup
4. Add tail current source
5. Optimize phase noise

**Example 8.18 (p570-572):** 2.4 GHz VCO:
- $L=4$ nH, $Q=12$, $R_p = Q\omega_0 L = 724\;\Omega$
- $I_{\text{tail}} = 2$ mA → $V_0 \approx I_{\text{tail}} R_p = 1.45$ V (current-limited)
- $g_m = 20$ mS (startup margin: $g_m R_p = 14.5 \gg 1$)
- PN at 1 MHz: $\mathcal{L} \approx -118$ dBc/Hz

**Example 8.20 (p576-578):** Class-C VCO:
- Bias at $V_{GS} - V_{TH} \approx V_{DD}/4$
- Higher efficiency, better phase noise

## 8.7 Injection Locking (p588-598)

**Locking range:**
$$\omega_L = \frac{\omega_0}{2Q} \cdot \frac{I_{\text{inj}}}{I_{\text{osc}}}$$

**Example 8.22 (p590-591):** $f_0=5$ GHz, $Q=10$, $I_{\text{inj}}/I_{\text{osc}}=0.1$ → $\omega_L = 2\pi \times 25$ MHz locking range.

**Applications:**
- Frequency division
- Quadrature injection locking
- Injection-locked oscillators for frequency synthesis

## Physical/Engineering Intuition

1. **Phase noise is the VCO's most critical parameter:** It directly affects the receiver's ability to reject adjacent channel interferers (reciprocal mixing).

2. **Lesson's model captures the three PN regions:** The $1/f^2$ to $1/f^3$ corner depends on the device flicker noise. The flat noise floor depends on the buffer/limiter.

3. **Higher Q → lower phase noise:** The LC tank filters phase perturbations. $Q$ improvement of $2\times$ → PN improvement of $6$ dB.

4. **Voltage-limited regime must be avoided:** Once the amplitude clips, $P_{\text{sig}}$ stops increasing with bias current, and PN no longer improves.

5. **Current-biased vs voltage-biased:** Current-biased VCOs have better supply rejection but more noise from the tail current source.
