---
chapter: 6
title: Mixers
source: Razavi, "RF Microelectronics", 2nd Ed.
pages: p363-454 (book pp.341-430)
---

# Ch6: Mixers

## 6.1 General Considerations (p341-356)

**Mixer function:** Frequency translation — multiplication of RF signal with LO.

$$V_{\text{out}} = V_{\text{RF}} \cos\omega_{\text{RF}}t \cdot V_{\text{LO}} \cos\omega_{\text{LO}}t$$
$$= \frac{V_{\text{RF}}V_{\text{LO}}}{2}[\cos(\omega_{\text{RF}}+\omega_{\text{LO}})t + \cos(\omega_{\text{RF}}-\omega_{\text{LO}})t]$$

**Key performance metrics:**
- Conversion gain ($CG$): IF output / RF input
- Noise figure ($NF$): single-sideband (SSB) vs double-sideband (DSB)
- Linearity ($IIP_3$, $P_{\text{1dB}}$)
- Port-to-port isolation (LO→RF, LO→IF, RF→IF)
- LO power (affects gain, noise, linearity)

### Mixer Types
1. **Passive mixers**: No DC bias → no DC power, lower flicker noise, conversion loss
2. **Active mixers**: Provide conversion gain, higher LO power requirement

### 6.1.1 Switching (Commutating) Mixers

Ideal: switch driven by LO at $\omega_{\text{LO}}$. Output $\propto$ RF × square wave at $\omega_{\text{LO}}$.

Square wave: $S(t) = \frac{4}{\pi}\sum_{n=1,3,5,\ldots} \frac{1}{n}\sin(n\omega_{\text{LO}}t)$

Conversion gain of ideal switching mixer = $2/\pi \approx -3.9$ dB (fundamental only).

### 6.1.2 Noise in Mixers

**SSB vs DSB NF:**
- DSB: both sidebands carry signal → NF = NF$_{\text{SSB}} - 3$ dB
- For zero-IF receivers, both sidebands are signal → DSB

**Flicker noise in mixers:**
- CMOS mixers suffer from $1/f$ noise that corrupts the baseband signal
- Critical for direct-conversion receivers (signal centered at DC)

### 6.1.3 Linearity in Mixers

- $IIP_3$ limited by switching pair and transconductance stage
- RF feedthrough and LO leakage degrade effective linearity

## 6.2 Mixer Topologies (p356-410)

### 6.2.1 Single-Balanced Mixer (p356-366)

**Single-balanced active mixer** (Fig 6.8):
- $M_1$: transconductance stage ($V_{\text{RF}} \rightarrow I_{\text{RF}}$)
- $M_2$, $M_3$: switching pair driven by LO
- Differential IF output

**Conversion gain:**
$$CG \approx \frac{2}{\pi} g_{m1} R_D$$

**Noise sources:**
- $M_1$: thermal noise upconverted to IF
- $M_2$, $M_3$: direct noise at IF
- LO phase noise affecting noise folding

**Example 6.1 (p359-361):** Single-balanced mixer design: $g_{m1}=20$ mS, $R_D=200\;\Omega$ → $CG \approx (2/\pi) \times 20\text{mS} \times 200\;\Omega = 2.55 = 8.1$ dB.

### 6.2.2 Double-Balanced (Gilbert Cell) Mixer (p366-380)

**Gilbert cell** (Fig 6.17):
- Differential RF input ($M_1$, $M_2$) and differential LO switching ($M_3$-$M_6$)
- Rejects LO→RF and LO→IF feedthrough
- Balanced topology cancels even-order distortion

**Conversion gain:**
$$CG \approx \frac{2}{\pi} g_{m1} R_D$$

**Example 6.4 (p369-372):** Gilbert cell at 2.4 GHz: $I_{SS}=4$ mA, $R_D=200\;\Omega$, $g_{m1}=40$ mS → $CG \approx 5.1 = 14.2$ dB, NF ≈ 12 dB.

**Noise in Gilbert cell:**
- Tail current $I_{SS}$ noise appears as common-mode
- Switching pair noise is the dominant contributor
- Noise from $M_1$-$M_2$ appears at IF with gain $\approx 2/\pi$

### 6.2.3 Passive Mixers (p380-390)

**Passive ring mixer** (Fig 6.28):
- Four MOSFETs in ring configuration (no DC bias)
- Loss: $CG = -4$ to $-7$ dB typical
- Very low flicker noise (ideal for direct-conversion)
- Good linearity ($IIP_3 > 10$ dBm)

**Example 6.7 (p381-383):** Passive mixer conversion loss vs LO swing.

### 6.2.4 Mixer with Current-Source Boosting (p390-395)

- Add $RC$ degeneration at source of switching pair
- Improves linearity without sacrificing gain
- Reduces switching pair noise contribution

### 6.2.5 High-Frequency Mixers (p395-402)

- Use inductive loads instead of resistive
- Resonant at IF frequency
- Higher gain, lower supply voltage

### 6.2.6 Noise Analysis (p402-410)

**Detailed noise contributions in Gilbert cell:**
- RF transconductor: $\overline{I_{n,\text{out}}^2} = 4kT\gamma g_{m1} \cdot (2/\pi)^2$
- Switching pair: noise during transitions
- Load resistors: $4kT/R_D$

**Total output noise:**
$$\overline{V_{n,\text{out}}^2} = \left[4kT\gamma g_{m1}\left(\frac{2}{\pi}\right)^2 + \frac{16kT}{R_D}\right] R_D^2$$

**Example 6.12 (p406-408):** Complete Gilbert cell NF calculation → NF ≈ 15 dB for typical 2.4 GHz design.

## 6.3 Active vs Passive Mixer Trade-offs (p410-430)

| Parameter | Active (Gilbert) | Passive |
|-----------|-----------------|---------|
| Conversion Gain | 10-20 dB | -4 to -7 dB |
| NF (DSB) | 10-15 dB | 5-10 dB |
| Flicker Noise | High | Low |
| IIP₃ | -5 to +5 dBm | +10 to +25 dBm |
| LO Power | -10 to 0 dBm | 0 to +10 dBm |
| DC Power | 2-10 mW | ~0 mW |

**Application guidance:**
- **Heterodyne RX:** Active mixers preferred (gain, relaxed NF)
- **Direct-conversion RX:** Passive mixers preferred (low flicker noise, high linearity)

## Physical/Engineering Intuition

1. **Gilbert cell vs passive ring:** The Gilbert cell provides gain but burns power and has high flicker noise. The passive mixer consumes no DC power and has excellent flicker noise but requires LO buffering.

2. **Flicker noise dominates in DCRs:** Since the desired signal is at DC (direct-conversion), the $1/f$ noise of active mixers directly corrupts the signal. Passive mixers avoid this.

3. **Conversion gain formula is key:** $CG = (2/\pi) g_m R_D$ for active mixers. Half the gain comes from the fundamental component of the square wave.

4. **Noise folding:** Broadband noise at multiples of $f_{\text{LO}}$ folds to IF. This makes mixer NF higher than expected from simple calculations.
