---
title: "Chapter 2 — Time and Frequency Domains"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 2
pages: "72–107"
---

# Ch2: Time and Frequency Domains

## 2.1 The Time Domain

The **time domain** is the real world — the only domain that actually exists. Key waveform parameters:

- **Clock period** $T_{\text{clock}}$: time interval to repeat one cycle (nsec)
- **Clock frequency** $F_{\text{clock}} = 1/T_{\text{clock}}$ (GHz when $T$ in nsec)
- **Rise time (10–90):** time from 10% to 90% of final voltage
- **Rise time (20–80):** time from 20% to 80% (used in some IBIS models)
- **Fall time:** typically slightly shorter than rise time (CMOS n-channel turns on faster than p-channel)

> **Engineering Intuition:** Signal integrity problems are more likely on falling edges because n-channel transistors switch faster than p-channel, creating sharper edges.

## 2.2 Sine Waves in the Frequency Domain

The **frequency domain** is a mathematical construct — not real. The only waveforms that exist there are **sine waves**.

Why sine waves? Four key properties:
1. Any time-domain waveform can be completely and uniquely described by combinations of sine waves
2. Sine waves of different frequencies are **orthogonal** (cross-product integrates to zero)
3. Well-defined mathematically
4. No infinities anywhere (real-world compatible)

> **Engineering Intuition:** We use the frequency domain NOT because it's more real, but because it sometimes gets us to an acceptable answer **faster** — especially for problems involving R, L, C circuits where sine waves are the natural solution to the differential equations.

## 2.3 Sine Wave Features

A sine wave is fully described by three terms:
- **Frequency** $f$ (Hz) or **angular frequency** $\omega = 2\pi f$ (rad/s)
- **Amplitude** $A$ (peak value)
- **Phase** $\phi$ (radians or degrees)

In the time domain, a sine wave requires thousands of data points. In the frequency domain, it's a **single point** (amplitude vs. frequency).

The collection of amplitudes at all frequencies is called the **spectrum**.

## 2.4 The Fourier Transform

Converts time-domain waveforms into frequency-domain spectra. Three types:

| Type | Use Case |
|:--|:--|
| **Fourier Integral (FI)** | Ideal mathematical waveforms, continuous time → continuous frequency |
| **Discrete Fourier Transform (DFT)** | Real measured waveforms, discrete time → discrete frequency |
| **Fast Fourier Transform (FFT)** | Same as DFT but requires $N = 2^k$ points; 100–10,000× faster |

Tools: SPICE `.FOUR` command, Microsoft Excel FFT, Python `numpy.fft`.

## 2.5 Spectrum of a Repetitive Signal

For a DFT, a waveform must be **repetitive** (period $T$, repeat frequency $F = 1/T$). The spectrum contains only **harmonics** — multiples of $F$:

- **First harmonic** = $F$
- **$n$-th harmonic** = $n \times F$
- **Zeroth harmonic** = DC average value

> **Engineering Intuition:** Any arbitrary waveform can be made "repetitive" by repeating the measurement window. Choose the period equal to the clock period for easiest interpretation.

## 2.6 Spectrum of an Ideal Square Wave

For a 50% duty-cycle, 0-to-1 V ideal square wave (zero rise time):

- **Even harmonics** = 0 (all zero amplitude)
- **Odd harmonics:** $A_n = \dfrac{2}{\pi \cdot n}$
- **DC offset (zeroth harmonic):** 0.5 V

| Harmonic $n$ | Frequency | Amplitude |
|:--:|:--:|:--:|
| 1 | $F$ | 0.637 V |
| 3 | $3F$ | 0.212 V |
| 5 | $5F$ | 0.127 V |
| 7 | $7F$ | 0.091 V |
| $\infty$ | $\infty F$ | 0 |

Amplitudes decrease as $1/f$. Infinite bandwidth is required for zero rise time.

## 2.7 Effect of Bandwidth on Rise Time

**Bandwidth ($BW$):** the highest sine-wave-frequency component that is significant in the spectrum.

Adding more harmonics (higher bandwidth) produces a shorter rise time. Removing high-frequency components (lower bandwidth) increases rise time.

> **Engineering Intuition:** This is why lossy transmission lines degrade rise time — they attenuate high frequencies more than low frequencies. A 36-inch FR4 trace can degrade 50 psec rise time to 1.5 nsec.

### Key Relationship: Bandwidth and Rise Time

$$
BW = \frac{0.35}{RT}
$$

where:
- $BW$ = bandwidth (GHz)
- $RT$ = 10–90 rise time (nsec)

| $RT$ | $BW$ |
|:--:|:--:|
| 10 nsec | 35 MHz |
| 1 nsec | 350 MHz |
| 100 psec | 3.5 GHz |
| 50 psec | 7 GHz |
| 10 psec | 35 GHz |

> **Engineering Intuition:** This is one of the most useful rules of thumb in signal integrity. When $RT$ is in nsec, $BW$ is in GHz. When $RT$ is in $\mu$sec, $BW$ is in MHz.

## 2.8 What Does "Significant" Mean?

**Significant** = when the harmonic amplitude is still >70% of an ideal square wave's amplitude at the same harmonic. Alternatively: the frequency at which harmonic amplitudes drop off faster than $1/f$ — this is the **knee frequency**.

For a real trapezoidal waveform (finite rise time), harmonics above $BW = 0.35/RT$ contribute <70% of the ideal square wave's amplitude and can be ignored.

> **Engineering Intuition:** "Bandwidth" is inherently an approximation — a rule of thumb. If you need 900 MHz vs. 950 MHz precision, use the full spectrum instead.

## 2.9 Bandwidth and Clock Frequency

For most microprocessor-based systems, the rise time is approximately **7% of the clock period**. This yields:

$$
BW_{\text{clock}} \approx 5 \times F_{\text{clock}}
$$

| $F_{\text{clock}}$ | $RT$ (7% of period) | $BW$ |
|:--:|:--:|:--:|
| 10 MHz | 7 nsec | 50 MHz |
| 100 MHz | 0.7 nsec | 500 MHz |
| 1 GHz | 70 psec | 5 GHz |

**WARNING:** This is a generalization. Different waveforms with the **same** clock frequency can have very different rise times and bandwidths (Fig 2-14). Always use rise time directly when available.

> **Engineering Intuition:** An OK answer now is often more valuable than a perfect answer late. But never use this approximation for design sign-off.

## 2.10 Bandwidth of a Measurement

The **measurement bandwidth** is the highest frequency with significant accuracy:
- **VNA / Impedance Analyzer:** straightforward — it's the max frequency of the instrument
- **TDR:** $BW_{\text{meas}} \approx 0.35 / RT_{\text{step}}$ (rise time of the launched step)

State-of-the-art TDRs can achieve 3–5× the signal bandwidth through calibration (up to ~30 GHz).

## 2.11 Bandwidth of a Model

The **model bandwidth** is the highest frequency where the model accurately predicts behavior. Only verifiable by comparison to measurement.

**Example:** A 300-mil wire bond over a plane:
- **1st-order model** (R + L): $BW \approx 2$ GHz
- **2nd-order model** (R + L + C): $BW \approx 4$ GHz

## 2.12 Bandwidth of an Interconnect

The **3-dB bandwidth** of an interconnect: the frequency at which transmitted amplitude drops to 70% ($-3$ dB) of the incident value.

**Intrinsic rise time** of an interconnect:
$$
RT_{\text{interconnect}} \approx \frac{0.35}{BW_{\text{interconnect}}}
$$

**Combined rise time** (Gaussian approximation):
$$
RT_{\text{out}} = \sqrt{RT_{\text{in}}^2 + RT_{\text{interconnect}}^2}
$$

| Condition | Impact |
|:--|:--|
| $RT_{\text{interconnect}} < 0.5 \times RT_{\text{in}}$ | <10% rise time increase (negligible) |
| $RT_{\text{interconnect}} \approx RT_{\text{in}}$ | ~40% rise time increase (significant) |

> **Engineering Intuition:** To support a 1-GHz bandwidth signal, the interconnect bandwidth should be at least 2 GHz (factor of 2 margin).

## 2.13 Key Formulas

| Formula | Description |
|:--|:--|
| $F = 1/T$ | Clock frequency from period |
| $\omega = 2\pi f$ | Angular frequency |
| $A_n = 2/(\pi n)$ (odd $n$) | Ideal square wave harmonic amplitudes |
| $BW = 0.35/RT$ | Signal bandwidth from rise time |
| $BW_{\text{clock}} \approx 5 \times F_{\text{clock}}$ | Clock bandwidth estimate |
| $RT_{\text{out}} = \sqrt{RT_{\text{in}}^2 + RT_{\text{ic}}^2}$ | Rise time through interconnect |

## 2.14 Key Rules of Thumb

1. **Rise time ~7% of clock period** for typical microprocessor systems
2. **Bandwidth = 0.35 / rise time** (single most useful SI rule)
3. **Clock bandwidth ≈ 5× clock frequency** (when rise time is 7% of period)
4. **Interconnect BW should be ≥ 2× signal BW** for minimal degradation
5. **Interconnect intrinsic RT should be ≤ 50% of signal RT** for <10% degradation
6. **-3 dB = 70% amplitude** (definition of significant in interconnects)
