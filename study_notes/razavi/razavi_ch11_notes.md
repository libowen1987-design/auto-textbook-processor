---
chapter: 11
title: Fractional-N Synthesizers
source: Razavi, "RF Microelectronics", 2nd Ed.
pages: p741-776 (book pp.717-752)
---

# Ch11: Fractional-N Synthesizers

## 11.1 Basic Concept (p717-720)

Fractional-$N$: $\omega_{\text{out}} = (N + \alpha) \cdot \omega_{\text{ref}}$ where $0 < \alpha < 1$.

**Advantage:** Fine frequency resolution without small $\omega_{\text{ref}}$ → larger loop BW → faster settling, lower in-band noise.

## 11.2 Fractional-N Techniques (p720-748)

### 11.2.1 Dual-Modulus Fractional Division (p720-722)

Alternate between $N$ and $N+1$ division:
- Average ratio: $N_{\text{avg}} = N + \frac{K}{M}$ where $K/M$ is the duty cycle of $N+1$
- Phase accumulator controls the modulus

### 11.2.2 Phase Interpolation (p722-729)

- Generate fractional phase by interpolating between reference edges
- DAC + analog interpolation

**Example 11.1 (p724-725):** Phase interpolation using switched current sources.

### 11.2.3 Sigma-Delta Modulation (p729-748)

**ΣΔ fractional-N synthesizer** (Fig 11.23):
- ΣΔ modulator controls divider modulus dynamically
- Quantization noise shaped to high frequencies
- PLL low-pass filters the high-frequency noise

**MASH ΣΔ modulator** (Example 11.3):
- Cascaded 1st-order modulators
- 3rd-order noise shaping: $|NTF|^2 \propto (1 - z^{-1})^6$
- In-band noise: $S_Q(f) = \frac{\Delta^2}{12f_{\text{ref}}} \cdot (2\pi f/f_{\text{ref}})^{2L}$

### ΣΔ Noise and Spurs

**Fractional spurs** (Example 11.7, p743-744):
- ΣΔ modulation produces tonal spurs at fractional frequencies
- Dithering breaks up the tones

## 11.3 Design Considerations (p748-752)

- ΣΔ order vs stability: 3rd-order MASH is stable
- Loop filter must suppress ΣΔ quantization noise
- Typical loop BW: $f_{\text{ref}}/10$ to $f_{\text{ref}}/20$ (vs $f_{\text{ref}}/50$ for integer-$N$)

## Physical/Engineering Intuition

1. **Fractional-N breaks the N² noise penalty:** With $\omega_{\text{ref}} \gg$ channel spacing, in-band phase noise can be much lower than integer-$N$ for the same resolution.

2. **ΣΔ noise shaping is key:** The quantization noise is pushed to high frequencies where the PLL's low-pass filtering suppresses it. Higher-order modulators give better in-band noise but can be unstable.

3. **Fractional spurs are the price:** The ΣΔ modulation introduces tones at fractional frequencies. Dithering and careful loop filter design mitigate this.
