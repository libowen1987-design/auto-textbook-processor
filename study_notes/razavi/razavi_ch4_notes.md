---
chapter: 4
title: Transceiver Architectures
source: Razavi, "RF Microelectronics", 2nd Ed.
pages: p181-280 (book pp.155-260)
---

# Ch4: Transceiver Architectures

## 4.1 General Considerations (p155-167)

**Key challenge:** The wireless environment is "hostile" — limited bandwidth, strong interferers.

**Shannon's theorem:** $C = B\log_2(1+\text{SNR})$ bits/s.

**Example 4.1 (p157):** CDMA/WCDMA considerations — orthogonal codes, processing gain.

**Example 4.2 (p160-162):** Dynamic range requirements — WCDMA RX must handle $-117$ dBm sensitivity and $-25$ dBm blockers simultaneously.

## 4.2 Receiver Architectures (p167-252)

### 4.2.1 Heterodyne Receivers (p167-177)

Traditional super-heterodyne (Fig 4.4):
$$\text{RF} \rightarrow \text{LNA} \rightarrow \text{BPF} \rightarrow \text{Mixer} \rightarrow \text{IF filter} \rightarrow \text{Demodulator}$$

**Image problem** (p174-176): If $\omega_{\text{LO}} < \omega_{\text{RF}}$ (low-side injection), an image at $\omega_{\text{IM}} = \omega_{\text{RF}} - 2\omega_{\text{IF}}$ also downconverts to IF.
- Image rejection requires pre-filtering at RF

**Example 4.3 (p176-177):** 2.4 GHz RX with 200 kHz IF → image at 2.4 GHz - 400 kHz = 2.3996 GHz.

**Mixing spurs** (Example 4.5-4.6, p180-183): LO harmonics create spurs. $m f_{\text{LO}} \pm n f_{\text{RF}}$ type products.

**Example 4.7 (p183-185):** Spur analysis for heterodyne RX with $f_{\text{LO}} = 2.15$ GHz, $f_{\text{RF}} = 2.4$ GHz.

### Modern Heterodyne (p187-195, Fig 4.22-4.25)

- Dual-IF: first IF high (image rejection easier), second IF low (channel selection)
- Quadrature downconversion at final IF

**Example 4.10 (p190-191):** Sliding-IF architecture where $f_{\text{LO2}} = f_{\text{LO1}}/2$ → simpler LO generation.

**Example 4.11 (p192-193):** Dual-conversion with quadrature IF.

### 4.2.2 Direct-Conversion (Zero-IF) Receivers (p195-224)

**Architecture** (Fig 4.30):
$$\text{RF} \rightarrow \text{LNA} \rightarrow \text{Quadrature Mixers} \rightarrow \text{LPF} \rightarrow \text{Baseband}$$

**Key issues and solutions:**

1. **LO Leakage** (p195-198): LO couples through LNA to antenna
   - Example 4.15: Cascode LNA reverse isolation analysis
   - Solution: differential LO, symmetric layout

2. **DC Offsets** (p198-209): LO self-mixing → DC at baseband
   - Example 4.16: 30 dB RF + 40 dB BB gain, -60 dBm LO leakage → 1V DC offset
   - Example 4.17: I/Q offsets are unequal due to phase
   - Solutions: AC coupling (limited by ISI), active feedback (Fig 4.39), digital DAC offset calibration (Fig 4.40)

3. **Even-Order Distortion** (p209-213): $2^{nd}$-order nonlinearity creates baseband component from two interferers
   - $\cos\omega_1 t \cdot \cos\omega_2 t \rightarrow \cos(\omega_1-\omega_2)t$ — falls in baseband

4. **Flicker Noise** (p213-214): MOSFET $1/f$ noise corrupts baseband signal
   - Worse for narrowband signals (GSM: 200 kHz)

5. **Quadrature Mismatch** (p214-216): I/Q gain/phase imbalance → constellation distortion

### 4.2.3 Image-Reject Receivers (p223-240)

**Hartley Architecture** (Fig 4.62):
- Split signal into I/Q paths → 90° phase shift → add → image cancels
- $V_{\text{out}} \propto V_{\text{RF}}\cos(\omega_{\text{RF}}-\omega_{\text{LO}})t$, image component cancels

**Example 4.25 (p223):** Hartley with high-side injection → image at sum frequency, not difference.

**Weaver Architecture** (Fig 4.66):
- Uses two mixers instead of RC-CR phase shift
- No RC-CR matching issues, but has second-image problem

### 4.2.4 Low-IF Receivers (p240-252)

- IF = few hundred kHz (slightly above zero)
- Avoids DC offset and flicker noise
- Requires image rejection (digital)

## 4.3 Transmitter Architectures (p252-260)

**Direct-conversion TX** (Fig 4.72):
$$\text{I/Q Baseband} \rightarrow \text{Quadrature Upconverter} \rightarrow \text{PA} \rightarrow \text{Antenna$$

**Heterodyne TX:**
- Upconvert to IF first, then to RF
- Sliding-IF: $f_{\text{LO2}} = f_{\text{LO1}} \pm f_{\text{IF}}$

**Key TX issues:**
- Carrier leakage (LO feedthrough to PA output)
- Sideband rejection (I/Q mismatch)
- PA nonlinearity and spectral regrowth

## Physical/Engineering Intuition

1. **Heterodyne vs Direct-Conversion:** Heterodyne avoids DC offsets and flicker noise at the cost of image filtering and external components. DCR is more integrable but requires offset/linearity solutions.

2. **The image problem dominates heterodyne design:** The entire architecture (choice of IF, pre-selection filtering, dual conversion) revolves around suppressing the image.

3. **Direct-conversion survived thanks to CMOS scaling:** Digital DAC offset cancellation and sophisticated DSP made DCR viable — these would have been too expensive in older technologies.

4. **Even-order distortion is unique to DCR:** In heterodyne receivers, second-order products at $|\omega_1-\omega_2|$ are upconverted by the LO, not a problem. In DCR, mixer asymmetries leak them directly to baseband.
