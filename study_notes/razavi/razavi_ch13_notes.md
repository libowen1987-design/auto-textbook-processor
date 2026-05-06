---
chapter: 13
title: Transceiver Design Example
source: Razavi, "RF Microelectronics", 2nd Ed.
pages: p859-911 (book pp.835-888)
---

# Ch13: Transceiver Design Example

## 13.1 System-Level Design (p835-855)

**Design target:** A 5 GHz WLAN transceiver (IEEE 802.11a-compatible).

**Specifications:**
- Frequency band: 5.15-5.35 GHz, 5.725-5.825 GHz
- Modulation: OFDM with BPSK/QPSK/16QAM/64QAM
- Data rate: 6-54 Mb/s
- Sensitivity: -82 dBm (6 Mb/s, BPSK) to -65 dBm (54 Mb/s, 64QAM)
- EVM: < 5% (for 64QAM)
- Channel bandwidth: 20 MHz

### 13.1.1 Receiver Link Budget (p835-840)

**Receiver chain analysis:**

| Stage | Gain | NF | IIP3 | P1dB |
|-------|------|----|------|------|
| BPF (pre-LNA) | -1.5 dB | 1.5 dB | — | — |
| LNA | 18 dB | 2.5 dB | -10 dBm | -20 dBm |
| Mixer | 8 dB | 12 dB | +5 dBm | -5 dBm |
| VGA | 40 dB | 20 dB | +10 dBm | 0 dBm |
| **Total** | **64.5 dB** | **4.7 dB** | **-18.5 dBm** | **-30.5 dBm** |

**Sensitivity calculation:**
$$P_{\text{sen}} = -174 + NF + 10\log B + SNR_{\text{min}}$$

For 54 Mb/s (64QAM): $P_{\text{sen}} = -174 + 4.7 + 10\log(20\times 10^6) + 27 = -174 + 4.7 + 73 + 27 = -69.3$ dBm.

**Example 13.1 (p836-838):** Complete link budget — verifies gains, NF, linearity.

### 13.1.2 Transmitter Link Budget (p840-845)

| Stage | Gain | Pout | OIP3 |
|-------|------|------|------|
| I/Q Baseband | 10 dB | 0 dBm | +20 dBm |
| Upconverter | -2 dB | -2 dBm | +18 dBm |
| Driver | 22 dB | +20 dBm | +32 dBm |
| PA | 20 dB | +40 dBm | +50 dBm |
| **Total** | **+50 dB** | **+40 dBm** | **+24 dBm** |

### 13.1.3 Frequency Planning (p845-850)

- LO1 = RF — IF (low-side injection)
- IF = 1 GHz (high IF for image rejection)
- LO2 = 1 GHz (for quadrature downconversion to baseband)

**Spur analysis:** Verify no mixing products fall in-band.

**Example 13.2 (p847-848):** Spur table for $f_{\text{RF}} = 5.2$ GHz, $f_{\text{LO1}} = 4.2$ GHz, $f_{\text{IF}} = 1$ GHz → no spurs in 20 MHz channel.

## 13.2 Circuit Design (p855-875)

### 13.2.1 LNA Design (p855-860)
- Inductively-degenerated cascode
- $L_S = 0.4$ nH, $L_G = 4$ nH, $W = 120$ μm
- NF = 2.3 dB, gain = 18 dB, IIP3 = -9 dBm
- $S_{11} < -15$ dB over band

### 13.2.2 Mixer Design (p860-865)
- Gilbert cell with current-bleeding
- Conversion gain = 8 dB
- SSB NF = 13 dB
- IIP3 = +3 dBm

### 13.2.3 VCO Design (p865-870)
- Cross-coupled LC VCO
- $f_{\text{osc}} = 4.2$ GHz (LO1)
- Tuning range: 10% (with varactor + switched cap bank)
- Phase noise: -115 dBc/Hz at 1 MHz offset

### 13.2.4 PA Design (p870-875)
- Two-stage Class-AB
- $P_{\text{out}} = 24$ dBm (250 mW) — reduced from +40 dBm for WLAN
- PAE = 30% at $P_{\text{1dB}}$
- ACPR < -30 dBc

## 13.3 Layout and Simulation (p875-880)

- Floor plan: LNA far from VCO/PA
- Substrate isolation: guard rings, deep N-well
- Pad placement: RF, LO, baseband separated

## 13.4 Measurement Results (p880-888)

- RX NF: 5.2 dB (within 0.5 dB of spec)
- RX IIP3: -19 dBm
- TX EVM: 3.2% (for 64QAM, 54 Mb/s)
- TX ACPR: -32 dBc
- Total power: 180 mW (RX), 320 mW (TX)
- Die area: 4.5 mm²

## Physical/Engineering Intuition

1. **The link budget is the most important document:** It determines every circuit specification. A 1 dB error in NF or gain cascades through the entire chain.

2. **Frequency planning drives architecture:** The choice of IF determines image rejection requirements, spur generation, and LO complexity.

3. **Practical LNAs achieve 2-3 dB NF at 5 GHz:** The gap between theoretical NF and measured results comes from package parasitics, ESD, and PCB trace losses.

4. **The PA is the power bottleneck:** In WLAN transceivers, the PA consumes > 50% of the TX power. PA design involves the most modeling uncertainty between schematic and silicon.
