---
chapter: 9
title: Phase-Locked Loops
source: Razavi, "RF Microelectronics", 2nd Ed.
pages: p623-680 (book pp.599-656)
---

# Ch9: Phase-Locked Loops

## 9.1 Basic Concepts (p599-602)

PLL: negative feedback system that locks the phase/frequency of a VCO to a reference.

**Loop components:** PFD → CP → LPF → VCO → Divider → (back to PFD)

## 9.2 Charge-Pump PLL (p602-640)

### 9.2.1 Phase/Frequency Detector (PFD) (p602-610)

- Three-state: UP, DOWN, HIGH-Z
- Dead zone issue → use delay in reset path
- Detects both phase and frequency error

### 9.2.2 Charge Pump (CP) (p610-614)

- UP/DOWN switches: charge/discharge loop filter
- Current mismatch → reference spurs

**Example 9.2 (p612-613):** Charge pump mismatch analysis — 5% mismatch → 50 dB reference spur.

### 9.2.3 Loop Filter (p614-618)

**2nd-order loop filter:** $C_1$, $R_1$, $C_2$ ($C_2$ = $C_1/10$ for ripple suppression)

**Open-loop transfer function:**
$$G(s) = \frac{I_{CP}}{2\pi} \cdot \frac{1 + sR_1C_1}{s^2C_1(1 + sR_1C_2)} \cdot \frac{K_{VCO}}{s} \cdot \frac{1}{N}$$

### 9.2.4 Stability (p618-623)

- Phase margin at unity-gain frequency $\omega_c$
- Typical PM: $50^\circ{-}70^\circ$
- $\omega_c \ll \omega_{\text{ref}}$ (typically $\omega_c < \omega_{\text{ref}}/10$)

**Example 9.4 (p619-620):** Loop filter calculation for $I_{CP}=100$ μA, $K_{VCO}=100$ MHz/V, $N=100$, $f_{\text{ref}}=10$ MHz → $R_1=20$ kΩ, $C_1=400$ pF, $C_2=40$ pF.

### 9.2.5 Phase Noise (p624-632)

**Phase noise contributions:**
- Reference noise: high-pass filtered (suppressed by PLL bandwidth)
- VCO noise: high-pass filtered (PLL suppresses close-in noise)
- CP/PFD noise: band-pass filtered

**In-band phase noise:**
$$\mathcal{L}_{\text{in-band}} = 10\log\left(\frac{4\pi^2 N^2}{I_{CP}^2} \cdot \frac{S_{I_{CP}}}{2}\right)$$

### 9.2.6 Reference Spurs (p632-640)

- Caused by charge pump mismatch and leakage
- At offsets $\pm f_{\text{ref}}$ from carrier
- Suppressed by $C_2$ (2nd pole)

## 9.3 PFD/CP Nonidealities (p640-648)

- Dead zone → increased phase noise
- Current mismatch → reference spur
- Charge sharing → CP output glitch

## 9.4 PLL Design Procedure (p648-656)

1. Determine $f_{\text{ref}}$ and $N$ from system specs
2. Choose $I_{CP}$, $K_{VCO}$
3. Design loop filter for target bandwidth/phase margin
4. Verify phase noise and spur specifications

**Example 9.11 (p651-654):** Complete PLL design for frequency synthesizer: $f_{\text{out}}=2.4$ GHz, $f_{\text{ref}}=10$ MHz, $N=240$, loop BW = 100 kHz.

## Physical/Engineering Intuition

1. **PLL bandwidth trades settling vs spur suppression:** Wider BW → faster lock but less reference spur filtering.

2. **VCO noise is high-pass filtered:** Outside PLL bandwidth, VCO phase noise dominates. In-band noise is set by PFD/CP noise floor × $N^2$.

3. **Charge pump mismatch directly creates spurs:** Even 1% mismatch can create spurs above -60 dBc.

4. **The $N$ divider amplifies in-band noise:** Every 2× increase in $N$ → 6 dB higher in-band phase noise. Fractional-$N$ helps mitigate this.
