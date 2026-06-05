---
chapter: 3
title: Spectra of Digital Signals
source: Paul, Clayton R. *Introduction to Electromagnetic Compatibility*, 2nd Ed., Wiley, 2006
pages: 91-176
---

# Chapter 3: Spectra of Digital Signals

## 3.1 The Fundamental Relationship: Time Domain ↔ Frequency Domain

The Fourier transform is the bridge between time-domain waveforms and their spectral content:

$$X(f) = \int_{-\infty}^{\infty} x(t) e^{-j2\pi ft} dt$$

For periodic signals (clock, data), the Fourier series gives discrete spectral lines:

$$x(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[a_n\cos(2\pi n f_0 t) + b_n\sin(2\pi n f_0 t)\right]$$

where $f_0 = 1/T$ is the fundamental frequency.

## 3.2 The Trapezoidal Pulse: The Universal Digital Waveform

The digital clock waveform is modeled as a **trapezoidal pulse train**:
- Period $T$, pulse width $\tau$, amplitude $A$
- Rise/fall time $t_r = t_f$

**Single trapezoidal pulse spectrum (magnitude):**

$$|X(f)| = A\tau \left|\frac{\sin(\pi f\tau)}{\pi f\tau}\right| \cdot \left|\frac{\sin(\pi f t_r)}{\pi f t_r}\right|$$

### Trapezoidal Pulse Train Spectrum (line spectrum)

For a periodic train with duty cycle $D = \tau/T$:

$$|X_n| = 2A D \left|\frac{\sin(n\pi D)}{n\pi D}\right| \cdot \left|\frac{\sin(n\pi f_0 t_r)}{n\pi f_0 t_r}\right|$$

## 3.3 The Spectrum Envelope — Three Breakpoints

The spectral envelope is defined by three frequency regions:

| Region | Frequency Range | Slope | Physical Cause |
|---|---|---|---|
| Flat | $f < 1/\pi\tau$ | 0 dB/decade | Pulse width dominates |
| −20 dB/dec | $1/\pi\tau < f < 1/\pi t_r$ | -20 dB/dec | Pulse edges (finite rise time) |
| −40 dB/dec | $f > 1/\pi t_r$ | -40 dB/dec | Smooth edges (finite slope) |

### Critical frequencies:

$$f_\tau = \frac{1}{\pi\tau} \quad \text{(first corner, pulse width)}$$

$$f_{t_r} = \frac{1}{\pi t_r} \quad \text{(second corner, rise time)}$$

## 3.4 The Rise-Time / Bandwidth Relationship

The most important EMC relationship in this chapter:

$$\boxed{BW = \frac{0.35}{t_r}}$$

- $BW$ = bandwidth (frequency at which spectral envelope drops ~3 dB)
- $t_r$ = 10–90% rise time

### Physical Intuition:
Faster edge rates → wider spectrum → more high-frequency energy → greater radiated emission potential.

**Numerical examples:**

| Rise Time $t_r$ | Bandwidth $BW = 0.35/t_r$ | EMC Risk |
|---|---|---|
| 10 ns | 35 MHz | Low |
| 1 ns | 350 MHz | Moderate |
| 100 ps | 3.5 GHz | High |
| 10 ps | 35 GHz | Extreme |

## 3.5 Clock vs. Data Spectra

### Periodic Clock:
Discrete spectral lines at $f_0, 2f_0, 3f_0, \dots$ with envelope $1/f$ above $f_\tau$.

$$P_n = 2A D \,\text{sinc}(nD) \,\text{sinc}(n\pi f_0 t_r) \quad \text{(magnitude of $n$th harmonic)}$$

### Random Data (PRBS):
Continuous spectral density with $\text{sinc}^2$ envelope. For NRZ data:

$$S(f) = A^2 T_b \left[\frac{\sin(\pi f T_b)}{\pi f T_b}\right]^2$$

where $T_b$ = bit period = $1/f_{\text{clock}}$.

## 3.6 Reducing Spectral Content (EMI Mitigation)

| Technique | Effect on Spectrum | Cost |
|---|---|---|
| Spread-spectrum clocking | Spreads energy, reduces peak ~10 dB | Moderate |
| Slower edge rate ($t_r$ increase) | Lowers $f_{t_r}$, reduces HF content | Free (if timing allows) |
| Reduced amplitude | Direct reduction in $A$ | Signal integrity concern |
| Filtering | Removes harmonics above cutoff | Component cost |

## 3.7 Engineering Intuition: Rise Time is the Enemy

**The single most important EMC lesson:**
- A 100 MHz clock with 1 ns edges has the same HF spectrum as a 1 GHz clock with 1 ns edges.
- Slowing rise time is the most cost-effective EMC fix.
- The clock frequency sets the **spacing** between spectral lines; the rise time sets the **envelope**.

### Example: FCC Compliance Check
For a 50 MHz clock ($T = 20$ ns), $\tau = 10$ ns, $t_r = 1$ ns:
- $f_\tau = 1/(\pi \cdot 10\text{ ns}) = 31.8$ MHz
- $f_{t_r} = 1/(\pi \cdot 1\text{ ns}) = 318$ MHz
- Harmonics: 50, 100, 150, ... MHz
- First harmonic in −20 dB/decade region: 100, 150, 200, 250, 300 MHz
- Harmonic at 300 MHz has envelope attenuation: $20\log_{10}(f_\tau/300\text{ MHz}) \approx -19.5$ dB from DC level
