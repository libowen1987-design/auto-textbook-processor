---
title: "Chapter 8 — Matching and Biasing Networks"
book: "RF Circuit Design — 2nd Ed."
author: "Reinhold Ludwig, Gene Bogdanov"
pages: "419–470"
processed: "2026-05-03"
tags: [matching-network, L-network, T-network, pi-network, smith-chart, stub-matching, bias-tee]
---

# Chapter 8: Matching and Biasing Networks

> **Overview:** Discrete and distributed matching networks (L, T, π, stub) for impedance transformation, plus bias network design for amplifier classes.

## 8.1 Impedance Matching Using Discrete Components

### L-Section Matching

Two possible topologies (Fig. 8-1):
- **Load inside $1+y$ circle:** shunt-L/series-C or shunt-C/series-L
- **Load outside $1+y$ circle:** series-L/shunt-C or series-C/shunt-L

Analytical solution (Example 8-1): Match $Z_L = R_L + jX_L$ to $Z_0$:
1. Add shunt element to change $Y$ conductance to $G_0$
2. Add series element to cancel residual reactance

### T- and π-Networks

- Provide wider bandwidth than L-section
- T-network: series/shunt/series (three components)
- π-network: shunt/series/shunt

### Narrowband Design (Example 8-4)

Smith Chart procedure:
1. Plot normalized load $z_L$
2. Add series/shunt elements to move toward $z=1$
3. Convert between Z- and Y-chart for series vs shunt

## 8.2 Microstrip Line Matching Networks

### Single-Stub Matching

- Series stub or shunt stub
- Two variables: stub length $l_s$ and position $d$
- Smith Chart: rotate from load to intersection with $r=1$ or $g=1$ circle

### Double-Stub Matching

- Two stubs at fixed distances; more practical for tunable designs
- Permits adjustment without changing stub positions

## 8.3 Amplifier Classes and Biasing Networks

### Classes
- **Class A:** Conduction angle $360^\circ$, max linearity, 50% max efficiency
- **Class B:** $180^\circ$, push-pull, 78.5% max efficiency
- **Class C:** $<180^\circ$, high efficiency, poor linearity
- **Class E/F:** Switch-mode, $>80\%$ efficiency

### Bias Networks
- RF choke (RFC) provides DC path while blocking RF
- DC blocking capacitor passes RF but blocks DC
- Bias-tee: combines DC bias and RF signal

> **工程直觉:** L-section匹配是最简单的窄带匹配, T/π提供更多自由度(带宽更宽). 微带短截线在>1 GHz时首选。偏置网络中RFC的自谐振频率(SRF)必须远离工作频段.
