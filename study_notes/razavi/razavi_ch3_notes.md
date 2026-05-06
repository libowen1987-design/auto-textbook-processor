---
chapter: 3
title: Communication Concepts
source: Razavi, "RF Microelectronics", 2nd Ed.
pages: p117-180 (book pp.91-154)
---

# Ch3: Communication Concepts

## 3.1 General Concepts (p91-92)

Modulation converts baseband signal to passband:
$$x(t) = a(t)\cos[\omega_c t + \theta(t)]$$

Key attributes of modulation:
1. **Detectability** — how well signal survives noise
2. **Bandwidth efficiency** — bits/sec per Hz
3. **Power efficiency** — compatibility with nonlinear PAs

## 3.2 Analog Modulation (p92-99)

### 3.2.1 AM (p93-94)
$$x_{\text{AM}}(t) = A_c[1 + m x_{\text{BB}}(t)]\cos\omega_c t$$
- Bandwidth = $2\times$ baseband bandwidth
- Requires linear PA

### 3.2.2 PM and FM (p95-99)
PM: $x_{\text{PM}}(t) = A_c\cos[\omega_c t + m x_{\text{BB}}(t)]$
FM: $x_{\text{FM}}(t) = A_c\cos[\omega_c t + m\int_{-\infty}^t x_{\text{BB}}(\tau)d\tau]$

**Narrowband FM** ($m A_m/\omega_m \ll 1$):
$$x_{\text{FM}}(t) \approx A_c\cos\omega_c t - \frac{m A_m A_c}{\omega_m}\sin\omega_m t \sin\omega_c t$$

**Example 3.3 (p97-98):** AM sidebands have same sign; FM sidebands have opposite signs. Phasor rotation differentiates them.

**Example 3.4 (p98-99):** Large sinusoid $+$ small offset frequency through differential pair → hard limiting suppresses AM component, FM component passes.

## 3.3 Digital Modulation (p99-118)

### Modulation Types
- **ASK/OOK:** $x(t) = a_n\cos\omega_c t$, $a_n \in \{0,1\}$
- **BPSK:** $x(t) = a_n\cos\omega_c t$, $a_n \in \{-1,+1\}$
- **FSK:** $x(t) = a_1\cos\omega_1 t + a_2\cos\omega_2 t$

### 3.3.1 ISI & Pulse Shaping (p101-104)
- Spectrum of random binary sequence: $S_x(f) = \frac{1}{T_b}|P(f)|^2$
- Rectangular pulse → sinc$^2$ spectrum (wide)
- Raised-cosine pulse (Eq. 3.25, Fig 3.19):
  $$p(t) = \frac{\sin(\pi t/T_S)}{\pi t/T_S} \frac{\cos(\pi\alpha t/T_S)}{1-4\alpha^2 t^2/T_S^2}$$
  $\alpha$ = roll-off factor (0.3-0.5 typical)

### 3.3.2 Signal Constellations (p105-107)
- Visualize modulation in signal space
- **EVM:** $\text{EVM}_1 = \frac{1}{V_{\text{rms}}} \sqrt{\frac{1}{N}\sum_{j=1}^N e_j^2}$
- BPSK: 2 points ($\pm 1$); QPSK: 4 points on circle

**Example 3.6 (p105):** ASK constellation — points at 0 and +1 on real axis.

### 3.3.3 Quadrature Modulation (p107-112)
**QPSK** (Fig 3.24): serial-to-parallel → I/Q arms → $\cos\omega_ct$ and $\sin\omega_ct$
$$x(t) = b_{2m}A_c\cos\omega_c t - b_{2m+1}A_c\sin\omega_c t$$
- Bandwidth = $1/2$ of BPSK
- Symbol rate = bit rate / 2

**Phase error effect** (Example 3.7, p108-109): Phase mismatch $\theta$ → constellation rotated and skewed.

**OQPSK** (Fig 3.29): I/Q offset by $T_b/2$ → max phase step $90^\circ$.

**$\pi/4$-QPSK** (Fig 3.31-32): alternate between two QPSK constellations rotated $45^\circ$ → max phase step $135^\circ$.

### 3.3.4 GMSK/GFSK (p112-113)
GMSK: Gaussian filter + VCO (Fig 3.34). Constant envelope.
- Used in GSM ($m=0.5$)
- GFSK: Bluetooth ($m=0.3$)

**Example 3.8 (p113):** GMSK modulator using quadrature upconverter (digital baseband $I/Q$).

### 3.3.5 QAM (p114-115)
$$x_{\text{16QAM}}(t) = \alpha_1 A_c\cos\omega_c t - \alpha_2 A_c\sin\omega_c t, \quad \alpha_1,\alpha_2 \in \{\pm 1, \pm 2\}$$
- 16QAM: 4 bits/symbol → $1/4$ bandwidth of BPSK
- 64QAM: 6 bits/symbol → $1/6$ bandwidth
- Trade-off: denser constellation → lower noise immunity, requires linear PA

### 3.3.6 OFDM (p115-118)
- N subcarriers, each with rate $r_b/N$
- Mitigates multipath delay spread
- Large **peak-to-average ratio (PAR):** $\text{PAR} = \max[x^2(t)]/\overline{x^2(t)}$
- PAR $\approx 2\ln N$ for large N

**Example 3.9 (p117):** OFDM realized via digital IFFT + quadrature modulator, not N separate oscillators.

## 3.4 Spectral Regrowth (p118-119)

Variable-envelope signals through nonlinear PA → spectrum broadens:
- Constant envelope: $3^{rd}$ nonlinearity → only harmonics at $3\omega_c$
- Variable envelope: $x_I^3(t)$ and $x_Q^3(t)$ components appear near $\omega_c$, widening spectrum

## 3.5 Mobile RF Communications (p119-123)

- **Cellular:** 7-cell reuse pattern (Fig 3.42)
- **Co-channel interference (CCI):** $D/R \approx 4.6$ for 7-cell → S/CCI $\approx 18$ dB
- **Path loss:** $\propto d^2$ (free space), $\propto d^4$ (reflective paths)
- **Multipath fading:** Rayleigh amplitude distribution
- **Diversity:** space, frequency, time
- **Delay spread:** flat vs frequency-selective fading (Fig 3.48)

## 3.6 Multiple Access (p123-134)

- **TDD/FDD** (Fig 3.49-50): time vs frequency duplexing
- **FDMA:** each user gets a frequency channel
- **TDMA:** each user gets a time slot
- **CDMA:** Walsh codes, orthogonal in code domain
  $$W_1 = [0], \quad W_{2n} = \begin{bmatrix} W_n & W_n \\ W_n & \overline{W_n} \end{bmatrix}$$

**Example 3.12 (p133):** GSM receiver linearity requirements — $P_{\text{1dB}} = -43$ dBm, IIP3 $= -23$ dBm for 3 MHz spacing blockers.

**Example 3.13 (p134):** WCDMA receiver — sensitivity $-117$ dBm, IIP3 $\approx -16$ dBm with $10$ dB NF.

## Physical/Engineering Intuition

1. **Envelope matters most for PA:** Constant-envelope (GMSK, FM) → nonlinear PA → high efficiency. Variable-envelope (QAM, OFDM) → linear PA → low efficiency.

2. **QPSK vs OQPSK vs π/4-QPSK:** The phase-transition hierarchy (180° → 90° → 135°) reflects the trade-off between differential detection capability and PA efficiency.

3. **OFDM PAR problem:** N subcarriers can add constructively → $10\log_{10}(2\ln N)$ dB above average. This drives a large backoff in PA output power.

4. **CDMA near-far problem:** All users share the same band → a nearby transmitter can desensitize the receiver for far users. Power control is essential.
