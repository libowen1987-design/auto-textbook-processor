---
chapter: 10
title: Integer-N Synthesizers
source: Razavi, "RF Microelectronics", 2nd Ed.
pages: p681-740 (book pp.657-716)
---

# Ch10: Integer-N Synthesizers

## 10.1 Basic Integer-N Synthesizer (p657-660)

$$\omega_{\text{out}} = N \cdot \omega_{\text{ref}}$$

**Channel spacing** = $\omega_{\text{ref}}$ (integer-$N$).

**Limitation:** For fine channel spacing, $\omega_{\text{ref}}$ must be small → large $N$ → high in-band noise.

## 10.2 Synthesizer Building Blocks (p660-680)

### 10.2.1 Frequency Dividers (p660-668)

**Prescalers:** High-speed dividers (2/3, 4/5, 8/9)

**Dual-modulus prescaler** (Fig 10.11):
- Divide by $P$ or $P+1$
- Combined with programmable counters: $N = P \cdot M + S$

**Example 10.2 (p663-665):** $P=32$, $M=8$, $S=3$ → $N = 32\times 8 + 3 = 259$.

### 10.2.2 Phase/Frequency Detector + Charge Pump (p668-672)

- Already covered in Ch9
- Specific considerations for integer-$N$: reference spur < -70 dBc

### 10.2.3 Loop Filter Design (p672-680)

**Design procedure** (Ex 10.5):
- Given: $I_{CP}$, $K_{VCO}$, $N$, $f_{\text{ref}}$, loop BW, PM
- Calculate $\omega_c$, then $T_1 = R_1 C_1$, $T_2 = R_1 C_2$
- Choose $C_1$ from noise/spur considerations

## 10.3 Synthesizer Performance (p680-696)

### 10.3.1 Settling Time (p680-685)

**Lock time approximation:**
$$t_{\text{lock}} \approx \frac{4}{\omega_c} \ln\left(\frac{\Delta f}{f_{\text{ref}}}\right)$$

**Example 10.8 (p682-683):** $\omega_c = 2\pi \times 100$ kHz, $\Delta f = 10$ MHz, $f_{\text{ref}} = 10$ MHz → $t_{\text{lock}} \approx 50$ μs.

### 10.3.2 Spurs (p685-690)

- Reference spurs at $\pm f_{\text{ref}}$
- Fractional spurs (for fractional-$N$)
- Spur suppression: $-20\log(\omega_{\text{ref}}/\omega_c)$ dB

### 10.3.3 Phase Noise (p690-696)

$$S_{\phi,\text{out}}(f) = N^2 S_{\phi,\text{ref}}(f) |H_{\text{LP}}(f)|^2 + S_{\phi,\text{VCO}}(f) |H_{\text{HP}}(f)|^2$$

## 10.4 Switched Loop Filters (p696-700)

- Use different loop filter for acquisition vs tracking
- Fast lock (wide BW) → narrow BW (low noise)

## 10.5 Frequency Hopping (p700-706)

**Bluetooth** (Example 10.14): 1600 hops/s, 79 channels, 625 μs/slot.
- Settling time < 150 μs required

## 10.6 Multi-Phase Generation (p706-716)

- Dividers generate 0°, 90°, 180°, 270°
- For quadrature up/downconversion

## Physical/Engineering Intuition

1. **Integer-N is simple but noisy:** Fine channel spacing requires large $N$ → in-band noise scales as $N^2$.

2. **Lock time vs bandwidth trade-off:** 4× wider BW → 4× faster settling but 12 dB worse reference spur suppression.

3. **Dual-modulus prescaler is the workhorse:** $P/P+1$ dividers enable arbitrary division ratios while keeping the first stage simple and fast.
