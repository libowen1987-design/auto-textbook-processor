---
title: "Chapter 6 — Active RF Components"
book: "RF Circuit Design — 2nd Ed."
author: "Reinhold Ludwig, Gene Bogdanov"
pages: "285–357"
processed: "2026-05-03"
tags: [diode, BJT, FET, HEMT, pn-junction, schottky, PIN, MESFET]
---

# Chapter 6: Active RF Components

> **Overview:** Physical basis of RF semiconductor devices: pn junction, Schottky diode, PIN diode, BJT, MESFET, HEMT. Key parameters for RF/microwave design.

## 6.1 Semiconductor Basics

- Intrinsic Si: $n_i = 1.45\times10^{10}$ cm$^{-3}$ at 300 K
- Doping: donor (n-type) and acceptor (p-type) atoms
- Mobility: $\mu_n > \mu_p$ (electrons faster than holes)
- GaAs advantages: higher electron mobility, semi-insulating substrate, better high-freq performance

## 6.2 RF Diodes

### pn Junction
- Built-in voltage $V_0 = \frac{kT}{q}\ln\left(\frac{N_A N_D}{n_i^2}\right)$
- Depletion capacitance: $C_j = \frac{C_{j0}}{(1 - V/V_0)^m}$, $m=1/2$ (abrupt) or $1/3$ (graded)
- RF resistance: $R_s$ (series bulk) + $R_j$ (junction)

### Schottky Diode
- Metal-semiconductor junction (e.g., Au on Si, GaAs)
- Lower forward voltage ($\approx 0.3$ V), majority carrier device (no storage time)
- Key for mixers and detectors at mm-wave

### PIN Diode
- P$^+$-I-N$^+$ structure; behaves as variable resistor at RF
- Low bias → high R ($>10$ k$\Omega$), High bias → low R ($<1$ $\Omega$)
- Used for RF switches, attenuators, phase shifters

### Varactor Diode
- Voltage-controlled capacitor; used for VCO tuning
- $C(V) = C_{j0}/(1 + V/V_0)^m$

## 6.3 RF Transistors

### BJT (Bipolar Junction Transistor)
- $\beta = I_C/I_B$ (current gain)
- $f_T$: unity current gain frequency
- Key parameters: $r_\pi$, $g_m = I_C/V_T$, $C_\pi$, $C_\mu$

### MESFET (Metal-Semiconductor FET)
- GaAs-based; Schottky gate
- $I_{DSS}$: drain saturation current, $V_P$: pinch-off voltage
- $g_m$: transconductance, $C_{gs}$, $C_{gd}$: gate capacitances

### HEMT (High Electron Mobility Transistor)
- Modulation-doped heterojunction (AlGaAs/GaAs)
- Highest $f_T$ and $f_{\max}$; lowest noise figure
- Used for LNA and mm-wave applications

> **工程直觉:** 器件选择: 1–3 GHz → Si BJT/SiGe HBT; 3–20 GHz → GaAs MESFET; >20 GHz → GaAs/InP HEMT.
