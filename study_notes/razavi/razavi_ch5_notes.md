---
chapter: 5
title: Low-Noise Amplifiers
source: Razavi, "RF Microelectronics", 2nd Ed.
pages: p281-362 (book pp.255-340)
---

# Ch5: Low-Noise Amplifiers

## 5.1 General Considerations (p255-263)

**LNF requirements** (NF = 2 dB → input-referred noise $\sqrt{\overline{V_{n,\text{in}}^2}} = 0.696$ nV/$\sqrt{\text{Hz}}$ for $R_S = 50\;\Omega$).

**NF formula:** $\text{NF} = 1 + \frac{\overline{V_{n,\text{in}}^2}}{4kT R_S}$

**Example 5.1 (p256-257):** 200 μm × 0.5 μm metal line with $R_\square = 40$ mΩ → $R_L = 16\;\Omega$ → NF degrades by $16/50 = 0.32 = 1.4$ dB.

**Example 5.2 (p258-259):** Input-referred noise of CS stage with gate resistance: $\overline{V_{n,\text{in}}^2} = 4kT R_G/3 + 4kT\gamma/g_m$.

**Example 5.3 (p259-262):** LNA driven by unbalanced source → noise from substrate coupling. Model source imbalance as $V_{cm} = (V_1 - V_2)/2$ → degrades NF.

**Gain requirements:** 15-25 dB typical. Input return loss $S_{11} < -10$ dB. Linearity: $P_{\text{1dB}} > -20$ dBm.

**Power dissipation trade-off:** NF generally more critical than power for LNA.

## 5.2 Problem of Input Matching (p263-266)

**Passive resistive termination** (Fig 5.9):
- $R_P$ in parallel → NF > 3 dB (Example 5.5 proves NF ≥ 2 = 3 dB with lossless matching network)
- $\text{NF} = 1 + R_S/R_P + \gamma R_S/[g_m(R_S||R_P)^2] + \cdots$

**Key insight:** LNA must produce $50\;\Omega$ real input impedance WITHOUT a physical $50\;\Omega$ resistor → use active circuit techniques.

### CS Stage Input Impedance (p263)
$$Y_{\text{in}} \approx \frac{R_D C_F \omega^2 [C_F + g_m R_D (C_L + C_F)]}{R_D^2 (C_L + C_F)^2 \omega^2 + 1} + j(\ldots)$$

### Common-Gate Input Impedance
$Z_{\text{in}} \approx 1/g_m$ → set $g_m = 1/50\;\Omega = 20$ mS.

## 5.3 LNA Topologies (p266-340)

### 5.3.1 CS with Inductive Load (p266-269)
- High gain at resonance, low supply voltage
- Miller effect through $C_{GD}$ can cause negative input resistance at other frequencies
- Neutralization possible but adds parasitics

### 5.3.2 CS with Resistive Feedback (p269-271)
- $R_{\text{in}} \approx 1/g_{m1}$ when $R_F \gg 1/g_{m1}$
- Bandwidth limited by feedback loop
- $g_m = 1/R_S$ for matching → NF limited by $R_F$ noise

### 5.3.3 CS with Inductive Degeneration (p271-280) ⭐KEY TOPOLOGY

**Input impedance:**
$$Z_{\text{in}} = \frac{g_m L_S}{C_{GS}} + j\left(\omega(L_S + L_G) - \frac{1}{\omega C_{GS}}\right)$$

At resonance: $\text{Re}\{Z_{\text{in}}\} = \omega_T L_S$ where $\omega_T = g_m/C_{GS}$.

**Design:** $L_S = R_S/\omega_T$ (typically 0.5-2 nH), then choose $L_G$ to resonate: $L_G = 1/(\omega_0^2 C_{GS}) - L_S$.

**NF of inductively-degenerated CS LNA:**
$$\text{NF} \approx 1 + \frac{\gamma}{\alpha} \cdot \frac{\omega_0}{\omega_T} \cdot \frac{R_S}{\text{Re}\{Z_{\text{in}}\}} \quad \text{(simplified)}$$

For $R_S = \text{Re}\{Z_{\text{in}}\} = 50\;\Omega$:
$$\text{NF} \approx 1 + \frac{\gamma}{\alpha} \cdot \frac{\omega_0}{\omega_T}$$

**Example 5.7 (p275):** $f_T = 80$ GHz, $f_0 = 5$ GHz → $\text{NF} \approx 1 + (2.5/1) \cdot (5/80) = 1.16 = 0.64$ dB (idealized).

### 5.3.4 Cascode LNA with Inductive Degeneration (p280-295) ⭐

**Cascode advantages:**
- Reduces Miller effect ($C_{GD}$ coupling)
- Improves reverse isolation ($S_{12}$)
- Higher output impedance → higher gain
- Better stability

**Design procedure (Example 5.8, p281-283):**
1. Size M1 for $C_{GS}$ such that $\omega_T L_S = R_S$
2. Choose $C_{GS}$ for resonance at $\omega_0$
3. Size M2 (cascode) at same or slightly smaller width
4. Design output load (LC tank) for gain and bandwidth

**Example 5.8 (p281-283):** 5 GHz LNA: $W_1 = 100\;\mu\text{m}$, $L_S = 0.5$ nH, $L_G = 8$ nH, $I_D = 5$ mA → $\text{NF} \approx 1.5$ dB.

**Noise of cascode device M2** (p285-290):
- M2's noise appears at output with gain ≈ 1 (for $V_{\text{out}}$ referred to M2 drain)
- Contribution ≈ $\overline{I_{n,M2}^2} \cdot (1/g_{m2})^2$
- Usually negligible compared to M1 noise

**Example 5.10 (p285-286):** Compare M1 vs M2 noise contribution → M2 adds ~0.2 dB.

### 5.3.5 Noise Optimization (p295-310)

**Power-constrained noise optimization:**
- For given $P_D$, optimize $W$ and $V_{GS} - V_{TH}$
- Optimum device width $W_{\text{opt}} \approx 1/(3\omega R_S C_{ox})$

**Example 5.13 (p297-298):** Optimize W for min NF at $f_0 = 2.4$ GHz, $I_D = 3$ mA → $W_{\text{opt}} \approx 200\;\mu\text{m}$.

**Power-constrained simultaneous noise and input match (PCSNIM):**
- Add $C_{ex}$ between gate and source to adjust $C_{GS}$ separately from $g_m$
- Allows independent optimization of NF and input matching

### 5.3.6 Common-Gate LNA (p310-318)

**Input impedance:** $Z_{\text{in}} \approx 1/g_m$ → matching requires $g_m = 20$ mS.

**NF of CG LNA:**
$$\text{NF} = 1 + \frac{\gamma}{\alpha} + \frac{4kT R_D}{4kT R_S A_v^2}$$

For $g_m = 20$ mS and $\gamma/\alpha \approx 1$: $\text{NF} \approx 1 + 1 = 3$ dB (minimum).

**Example 5.16 (p311-312):** CG LNA design at 5 GHz: $g_m = 20$ mS, $I_D = 2$ mA, NF ≈ 3.5 dB with load noise.

**CG LNA advantages:**
- Broadband matching (no resonant input)
- Better linearity than CS stage
- Simpler topology

### 5.3.7 Broadband LNAs (p318-335)

**Resistive feedback LNA** (Example 5.18, p319-321):
$$\text{NF} = 1 + \frac{\gamma}{\alpha} + \frac{R_S}{R_F} \left(1 + \frac{R_S}{R_F}\right)$$
- Gain $A_v \approx R_F/R_S$ for $g_m R_F \gg 1$
- Bandwidth limited by $R_F C_{\text{in}}$

**Noise-cancelling LNA** (p325-335, Fig 5.49):
- Two paths: feedforward and common-gate
- Noise of matching device cancels at output
- Signal adds constructively
- NF can approach 1 dB over wide bandwidth

### 5.3.8 Reactance-Cancelling LNAs (p335-340)

- Use $LC$ network to cancel input capacitance over wide bandwidth
- Example 5.23: three-section $LC$ ladder → BW > 10 GHz

## Physical/Engineering Intuition

1. **Source degeneration is the key LNA technique:** Inductive degeneration allows noise-free input matching ($\text{Re}\{Z_{\text{in}}\} = \omega_T L_S = 50\;\Omega$). The NF is fundamentally limited by $\gamma/\alpha \cdot \omega_0/\omega_T$.

2. **Cascode is almost always used:** It eliminates the Miller effect, which would otherwise create a negative input resistance and instability at high frequencies.

3. **CG LNA vs CS LNA:** CG gives lower voltage headroom and simpler matching but worse NF (~3 dB minimum). CS with inductive degeneration gives superior NF but is narrowband.

4. **Noise optimization is a device-sizing problem:** For a given bias current, there's an optimum device width that balances $C_{GS}$ (affects input match frequency) and $g_m$ (affects NF).

5. **Broadband LNAs use feedback or noise cancellation:** Resistive feedback gives wideband matching but moderate NF. Noise-cancelling topologies can break the NF-matching trade-off.
