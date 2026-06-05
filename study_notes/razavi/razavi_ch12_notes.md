---
chapter: 12
title: Power Amplifiers
source: Razavi, "RF Microelectronics", 2nd Ed.
pages: p777-858 (book pp.753-834)
---

# Ch12: Power Amplifiers

## 12.1 General Considerations (p753-760)

**PA metrics:**
- Output power ($P_{\text{out}}$)
- Power gain ($G_P$)
- Power-added efficiency (PAE)
- Linearity (adjacent channel power ratio, ACPR)
- Maximum operating frequency ($f_{\text{max}}$)

**PAE = $\frac{P_{\text{out}} - P_{\text{in}}}{P_{\text{DC}}}$**

## 12.2 Classification of PAs (p760-790)

### 12.2.1 Class A (p760-765)
- Conduction angle = 360°
- Max efficiency: 50% (ideal), ~30-40% practical
- Most linear, least efficient

**Example 12.1 (p761-763):** Class A PA: $V_{DD}=3$ V, $I_{DC}=100$ mA, $P_{DC}=300$ mW, $P_{\text{out}}=120$ mW → $\eta=40\%$.

### 12.2.2 Class B (p765-768)
- Conduction angle = 180°
- Push-pull topology
- Max efficiency: 78.5%

### 12.2.3 Class AB (p768-771)
- Conduction angle between 180° and 360°
- Compromise between linearity and efficiency
- Most common in linear PA design

### 12.2.4 Class C (p771-776)
- Conduction angle < 180°
- Higher efficiency, worse linearity
- Used for constant-envelope signals

**Example 12.4 (p772-774):** Class C PA efficiency calculation: $\eta \approx 85\%$ for very small conduction angle.

### 12.2.5 Class D (p776-778)
- Switched-mode PA (transistor as switch)
- Ideal efficiency: 100%
- Practical: 80-90%
- Requires harmonic termination

### 12.2.6 Class E (p778-784)
- Single-ended switched-mode
- Zero-voltage switching (ZVS)
- High efficiency, narrowband
- $P_{\text{out}} \approx 0.577 V_{DD}^2 / R_{\text{opt}}$

**Example 12.7 (p780-781):** Class E PA design: $f_0=900$ MHz, $V_{DD}=3$ V, $R_{\text{opt}}=10\;\Omega$ → $P_{\text{out}} \approx 520$ mW.

### 12.2.7 Class F (p784-790)
- Harmonic tuning (3rd harmonic short, odd harmonics)
- Voltage waveform squaring
- Efficiency approaches 100%

## 12.3 Linearization Techniques (p790-810)

- **Feedforward:** Cancels distortion by subtracting PA output
- **Predistortion:** Pre-distorts input to cancel PA nonlinearity
- **Cartesian feedback:** Feedback around I/Q modulator + PA
- **Doherty PA:** Two PAs with 90° combining → high efficiency at backoff

**Example 12.10 (p795-796):** Predistortion linearization — 10 dB IM3 improvement.

## 12.4 Load Line and Matching (p810-820)

**Optimum load:** $R_{\text{opt}} = (V_{DD} - V_{\text{knee}})^2 / (2P_{\text{out}})$

**Load-line theory:**
- Voltage swing: $V_{DD} - V_{\text{knee}}$ to $V_{DD} + (V_{DD} - V_{\text{knee}})$
- Current swing: $I_{\text{max}}$
- $P_{\text{out}} = \frac{1}{2} (V_{DD} - V_{\text{knee}}) I_{\text{max}}$ (Class A)

**Example 12.12 (p813-814):** $V_{DD}=3.3$ V, $P_{\text{out}}=1$ W → $R_{\text{opt}} = V_{DD}^2/(2P_{\text{out}}) \approx 5.4\;\Omega$.

**Output matching network:** Transformer or LC network — transform $R_{\text{opt}}$ to $50\;\Omega$.

## 12.5 Power Combining (p820-826)

**Power combiner types:**
- Wilkinson: isolated ports, resistive loss
- Transformer: compact, low loss
- λ/4 transmission line: narrowband

## 12.6 PA Design Examples (p826-834)

**2.4 GHz Class-AB PA** (Example 12.14):
- $P_{\text{out}} = 24$ dBm (250 mW)
- $V_{DD}=3.3$ V, $R_{\text{opt}} = 8\;\Omega$
- PAE ≈ 40%
- ACPR < -30 dBc (at 5 MHz offset)

## Physical/Engineering Intuition

1. **Efficiency vs linearity is the fundamental PA trade-off:** Class A gives the best linearity but < 50% efficiency. Switched-mode (E, F) gives > 70% but requires constant-envelope modulation.

2. **Load-line matching is different from noise matching:** PA matching transforms $R_{\text{opt}}$ (determined by $V_{DD}$ and $P_{\text{out}}$) to $50\;\Omega$. It's not about conjugate matching for max power transfer.

3. **Backoff is the enemy of efficiency:** To maintain linearity with variable-envelope signals (QAM, OFDM), the PA must operate at power levels far below $P_{\text{1dB}}$. Doherty PAs help recover backoff efficiency.

4. **Harmonic terminations are critical for Class E/F:** The efficiency advantage of switched-mode PAs relies on shaping the voltage/current waveforms via harmonic resonators.
