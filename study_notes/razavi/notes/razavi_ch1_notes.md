---
chapter: 1
title: Introduction to RF and Wireless Technology
source: Behzad Razavi, RF Microelectronics, 2nd Edition, McGraw-Hill, 2012
pages: 1-5
---

# Chapter 1: Introduction to RF and Wireless Technology
# 第一章：射频与无线技术概论

## Overview | 概述

This chapter sets the stage for the entire book by illustrating the evolution of RF transceivers and identifying the key challenges in RF integrated circuit (RFIC) design. Two landmark papers are compared:

- **"A 2.7-V GSM RF Transceiver IC"** (1997) — early integrated RF, few bands, basic functionality
- **"A Single-Chip 10-Band WCDMA/HSDPA 4-Band GSM/EDGE SAW-Less CMOS Receiver"** (2009) — multi-band, highly integrated, complex

> **（中文）** 本章通过对比1997年与2009年的两款射频收发器，揭示了RFIC从单模单带向多模多带、从分立元件向全集成化演进的历史轨迹，引出RF设计的核心挑战。

---

## 1.1 A Wireless World | 无线世界

### The Rise of Wireless Communication | 无线通信的崛起

Wireless communication has become nearly as ubiquitous as electricity. Modern cell phones integrate encyclopedia, shopping portal, GPS navigator, weather monitor, and telephone — all through wireless connectivity.

> **（中文）** 无线通信已渗透到现代生活的方方面面。手机不再只是通话工具，而是集成了信息查询、导航、支付、健康监测等功能的智能终端。

### Key Growth Drivers | 增长的核心驱动力

The explosive growth stems from several converging factors:

**1. Declining cost of electronics** — Moore's Law and VLSI scaling reduce per-function cost.

**2. Higher integration levels** — More functionality on fewer chips. The extreme case: *system-on-chip* (SoC).

**3. Performance improvement** — Lower power consumption for given function; higher $f_T$ (transit frequency) of MOSFETs.

Figure 1.1 illustrates trends from 1988–2010:
- CMOS minimum feature size: $0.5\ \mu\text{m} \rightarrow 40\ \text{nm}$
- NMOS $f_T$: $12\ \text{GHz} \rightarrow$ hundreds of GHz
- RF oscillator speed: $1.2\ \text{GHz} \rightarrow 300\ \text{GHz}$
- Number of RF/wireless papers at ISSCC: steadily increasing

> **（中文）** 射频集成电路的发展依赖于两大支柱：①CMOS工艺的持续缩小（从$0.5\ \mu\text{m}$到$40\ \text{nm}$），使晶体管的截止频率$f_T$从约$12\ \text{GHz}$提升至数百$\text{GHz}$；②射频架构与电路拓扑的创新，使系统功能密度呈指数增长。

---

## 1.2 RF Design Is Challenging | 射频设计的挑战

Despite decades of RF/microwave theory and two decades of RFIC research, RF design remains one of the most challenging fields in electrical engineering.

> **（中文）** 尽管微波理论与集成电路研究已有数十年积累，射频设计仍然是电子工程中最具挑战性的领域之一。

### Three Fundamental Reasons | 三大根本原因

#### (a) Multidisciplinary Nature | 多学科交叉性

RF design draws upon a wide range of disciplines:

| Discipline | Role in RF Design |
|---|---|
| Communication Theory | Modulation, demodulation, spectral efficiency |
| Random Signals & Noise | SNR analysis, noise figure |
| Microwave Theory | Transmission lines, S-parameters, Smith charts |
| Signal Propagation | Path loss, fading, multipath |
| Transceiver Architectures | Heterodyne, direct-conversion, IF-sampling |
| Wireless Standards | GSM, CDMA, LTE, 802.11a/b/g/n/ac |
| IC Design | Device models, layout, parasitics |
| CAD Tools | Harmonic balance, transient, EM simulation |

> **（中文）** 射频工程师必须同时掌握通信理论、随机过程、微波工程、电磁传播、集成电路设计等多个学科的知识体系。这种跨领域的特性使得新人入门门槛极高。

#### (b) Trade-offs: The RF Design Hexagon | 权衡取舍：射频设计六边形

Figure 1.3 presents the fundamental trade-offs in RF design:

$$
\text{RF Design} = f(\text{Noise},\ \text{Power},\ \text{Linearity},\ \text{Gain},\ V_{DD},\ f_{\text{max}})
$$

A change in one parameter inevitably affects others. Examples:

- **Noise vs. Power**: Lower noise requires higher bias current (more power)
- **Linearity vs. Power**: Better linearity often requires more power consumption
- **Gain vs. Bandwidth**: Broadband amplifiers typically have lower gain
- **$f_{\max}$ vs. $V_{DD}$**: Higher speed often demands lower supply voltages (technology scaling)

> **（中文）** 射频设计的六大核心指标——噪声、功耗、线性度、增益、电源电压、最大工作频率——构成一个相互制约的六边形。例如，要降低低噪声放大器的噪声，就必须增大偏置电流，从而增加功耗；要提高功率放大器的线性度，往往需要降低效率。

#### (c) Demand for Higher Performance, Lower Cost, More Functionality | 性能、成本、功能密度的持续压力

The evolution from single-transceiver to multi-standard SoC illustrates this pressure:

| Era | Chip Area Dominated By | On-Chip Inductors |
|---|---|---|
| 1990s | Digital baseband processor | Abundant |
| 2010s | Multiple RF transceivers | Minimal (large footprint) |

> **（中文）** 早期RF系统的芯片面积由数字基带处理器主导，射频工程师有较大自由度选择电路拓扑。但现代多模多带收发器中，射频部分的面积占比超过基带处理器，迫使射频设计必须在性能与面积之间做出严格权衡。

---

## 1.3 The Big Picture | 全局视角

### RF Transceiver: Conceptual Architecture | 射频收发器的概念架构

The fundamental objective of an RF transceiver is **transmit** and **receive** information.

```
Antenna ↔ (TX Path)
  Voice/Data → Modulator/Upconverter → Power Amplifier (PA) → Antenna

Antenna → (RX Path)
  Antenna → Low-Noise Amplifier (LNA) → Downconverter/Demodulator → Reconstructed Voice/Data
```

> **（中文）** 射频收发器的核心功能可以简化为：发射链路将基带信号调制并上变频至射频，经功率放大器（PA）驱动天线发射；接收链路将天线接收的微弱射频信号经低噪声放大器（LNA）放大后，下变频至基带进行解调。

### Key Functions in TX and RX | 发射与接收链路的关键模块

| Block | TX Role | RX Role |
|---|---|---|
| **Modulator/Upconverter** | Modulates baseband onto carrier $f_c$ | — |
| **PA (Power Amplifier)** | Drives antenna with high power | — |
| **LNA (Low-Noise Amplifier)** | — | Amplifies tiny received signal with minimal noise addition |
| **Downconverter/Demodulator** | — | Converts $f_c$ back to baseband |
| **Frequency Synthesizer** | Provides local oscillator $f_{\text{LO}}$ | Provides local oscillator $f_{\text{LO}}$ |
| **ADC/DAC** | Digital-to-Analog conversion | Analog-to-Digital conversion |

### Carrier Frequency Consideration | 载波频率的选取

Modern wireless standards operate at carrier frequencies $f_c$ from hundreds of MHz to tens of GHz:

| Standard | Typical $f_c$ |
|---|---|
| GSM 900 | $880\ \text{MHz} - 915\ \text{MHz}$ (RX), $925\ \text{MHz} - 960\ \text{MHz}$ (TX) |
| DCS 1800 | $1710\ \text{MHz} - 1785\ \text{MHz}$ (RX), $1805\ \text{MHz} - 1880\ \text{MHz}$ (TX) |
| WiFi (802.11b/g) | $2.4\ \text{GHz} - 2.4835\ \text{GHz}$ |
| WiFi (802.11a) | $5.15\ \text{GHz} - 5.875\ \text{GHz}$ |
| LTE Band 1 | $2110\ \text{MHz} - 2170\ \text{MHz}$ (RX), $1920\ \text{MHz} - 1980\ \text{MHz}$ (TX) |

> **（中文）** 载波频率$f_c$的选取是无线系统设计的首要决策。频率越高，天线尺寸越小，路径损耗越大，可用带宽越宽；频率越低，绕射能力强但可用带宽受限。

### The Deceptive Simplicity | 表象的欺骗性

Figure 1.4(c) shows the generic RF transceiver as a handful of blocks — but this apparent simplicity is deeply misleading. Razavi notes:

> *"We will need the next 900 pages to cover its RF sections."*

The remaining chapters of this book systematically cover each building block:

| Chapter | Topic |
|---|---|
| Ch2 | Basic Concepts: Nonlinearity, Noise, Impedance Matching, S-Parameters |
| Ch3 | Communication Concepts: Modulation, Demodulation, Multiple Access |
| Ch4 | Transceiver Architectures: Heterodyne, Direct-Conversion, Image-Reject |
| Ch5 | Low-Noise Amplifiers (LNA) |
| Ch6 | Mixers |
| Ch7 | Passive Devices: Inductors, Transformers, varactors |
| Ch8 | Oscillators and VCOs |
| Ch9 | Phase-Locked Loops (PLL) |
| Ch10 | Integer-$N$ Frequency Synthesizers |
| Ch11 | Fractional-$N$ Synthesizers |
| Ch12 | Power Amplifiers (PA) |
| Ch13 | Transceiver Design Example |

> **（中文）** 射频收发器的"框图"看似简单，但每个模块的设计都涉及深奥的物理与电路理论。噪声、非线性、阻抗匹配、频率合成、时钟抖动等问题的交织，使得射频工程师必须对系统与电路均有深入理解。

### Transit Frequency $f_T$ | 截止频率 $f_T$

**Definition**: The frequency at which the small-signal current gain ($\left|h_{fe}\right|$) of a transistor falls to unity (0 dB).

For a MOSFET in saturation:

$$
f_T = \frac{g_m}{2\pi (C_{gs} + C_{gd})} \approx \frac{\mu_n C_{ox} (W/L) V_{OV}}{2\pi [(WLC_{ox}) + (WLC_{ox}/2)]} \approx \frac{\mu_n V_{OV}}{2\pi L^2}
$$

where $V_{OV} = V_{GS} - V_{TH}$ is the overdrive voltage, $\mu_n$ is the electron mobility, and $L$ is the channel length.

> **（中文）** $f_T$是衡量射频晶体管高速性能的核心指标。它表示晶体管电流增益降为1（即$0\ \text{dB}$）时的工作频率。现代$40\ \text{nm}$ CMOS工艺的NMOS器件$f_T$可达数百$\text{GHz}$，支撑了毫米波射频电路的设计。

---

## Key Takeaways | 本章要点

1. **Wireless is ubiquitous** — RF integration has transformed from single-function discrete circuits to multi-standard SoCs.
2. **Three RF design challenges**: multidisciplinary knowledge, fundamental trade-offs (the hexagon), and relentless demand for higher performance at lower cost.
3. **The generic transceiver** consists of LNA, Mixer, PA, Oscillator/VCO, PLL synthesizer, and ADC/DAC — each a deep topic.
4. **$f_T$ trends** track technology scaling: $0.5\ \mu\text{m} \rightarrow 40\ \text{nm}$ CMOS drove $f_T$ from $\sim 12\ \text{GHz}$ to hundreds of GHz, enabling integration.

---

## References | 参考文献

[1] T. Yamawaki et al., "A 2.7-V GSM RF Transceiver IC," *IEEE J. Solid-State Circuits*, vol. 32, pp. 2089–2096, Dec. 1997.

[2] D. Kaczman et al., "A Single-Chip 10-Band WCDMA/HSDPA 4-Band GSM/EDGE SAW-Less CMOS Receiver with DigRF 3G Interface and 190-dBm IIP2," *IEEE J. Solid-State Circuits*, vol. 44, pp. 718–739, March 2009.

[3] M. Banu, "MOS Oscillators with Multi-Decade Tuning Range and Gigahertz Maximum Speed," *IEEE J. Solid-State Circuits*, vol. 23, pp. 474–479, April 1988.

[4] B. Razavi et al., "A 3-GHz 25-mW CMOS Phase-Locked Loop," *Dig. of Symposium on VLSI Circuits*, pp. 131–132, June 1994.

[5] M. Soyuer et al., "A 3-V 4-GHz nMOS Voltage-Controlled Oscillator with Integrated Resonator," *IEEE J. Solid-State Circuits*, vol. 31, pp. 2042–2045, Dec. 1996.

[6] B. Kleveland et al., "Monolithic CMOS Distributed Amplifier and Oscillator," *ISSCC Dig. Tech. Papers*, pp. 70–71, Feb. 1999.

[7] H. Wang, "A 50-GHz VCO in 0.25-μm CMOS," *ISSCC Dig. Tech. Papers*, pp. 372–373, Feb. 2001.

[8] L. Franca-Neto, R. Bishop, and B. Bloechel, "64 GHz and 100 GHz VCOs in 90 nm CMOS Using Optimum Pumping Method," *ISSCC Dig. Tech. Papers*, pp. 444–445, Feb. 2004.

[9] E. Seok et al., "A 410 GHz CMOS Push-Push Oscillator with an On-Chip Patch Antenna," *ISSCC Dig. Tech. Papers*, pp. 472–473, Feb. 2008.

[10] B. Razavi, "A 300-GHz Fundamental Oscillator in 65-nm CMOS Technology," *Symposium on VLSI Circuits Dig. of Tech. Papers*, pp. 113–114, June 2010.
