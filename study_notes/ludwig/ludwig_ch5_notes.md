---
title: "Chapter 5 — RF Filter Design"
book: "RF Circuit Design — 2nd Ed."
author: "Reinhold Ludwig, Gene Bogdanov"
pages: "215–277"
processed: "2026-05-03"
tags: [filter, butterworth, chebyshev, kuroda, coupled-line, resonator]
---

# Chapter 5: An Overview of RF Filter Design

> **Overview:** This chapter covers RF filter design using Butterworth, Chebyshev, and elliptic low-pass prototypes, impedance/frequency scaling, Kuroda's identities, and coupled-line microstrip filters.

## 5.1 Basic Resonator and Filter Configurations

### Filter Types: LP, HP, BP, BS

Normalized frequency: $\Omega = \omega/\omega_c$ (cutoff for LP/HP, center for BP/BS).

### Key Parameters
- **Insertion Loss:** $\text{IL} = 10\log(P_{\text{in}}/P_L) = -10\log(1 - |\Gamma_{\text{in}}|^2)$
- **Ripple:** Passband flatness (dB)
- **Bandwidth:** $\text{BW} = f_U - f_L$ (at 3 dB points)
- **Shape Factor:** $\text{SF} = \text{BW}_{60\text{dB}}/\text{BW}_{3\text{dB}}$
- **Rejection:** Typically 60 dB stopband spec

### Quality Factor

$$
Q = \omega \frac{W_{\text{stored}}}{P_{\text{loss}}}
$$

- **Unloaded** $Q_U$: filter alone
- **External** $Q_E$: source/load only
- **Loaded** $Q_{\text{LD}}$: combined

$$
\frac{1}{Q_{\text{LD}}} = \frac{1}{Q_U} + \frac{1}{Q_E}
$$

### Butterworth (Maximally Flat) Response (N=3 prototype, Table 5-1)

$g_k$ values for $N=3$ with $R_S = R_L = 1$: $g_1=1$, $g_2=2$, $g_3=1$, $g_4=1$

### Chebyshev (Equi-ripple) Response

Uses Chebyshev polynomials $T_N(\Omega)$. Ripple in passband, steeper roll-off than Butterworth.

## 5.2 Special Filter Realizations

### Kuroda's Identities
Transform series inductors/shunt capacitors into transmission line stubs with unit elements. Four identities (Fig. 5-24) enable practical microstrip implementation.

### Coupled Line Filters
Parallel coupled microstrip half-wavelength resonators for bandpass filters (Table 5-6).

> **工程直觉:** 滤波器设计三步法: (1) 选择低通原型类型(Bessel/Butterworth/Chebyshev)和阶数, (2) 频率/阻抗变换, (3) 用Kuroda恒等式转换为分布参数结构.
