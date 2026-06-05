# Chapter 1: Introduction to RF and Wireless Technology

**Source:** Razavi, *RF Microelectronics*, 2nd Ed., Chapter 1

---

## 1.1 RF Design Challenges

Key differences between RF and analog/baseband design:
- **Impedance matching:** Power transfer vs voltage transfer
- **Noise:** Critical at RF due to limited signal power
- **Linearity:** Spurs and harmonics cause interference
- **Parasitics:** Device and interconnect parasitics dominate at GHz

## 1.2 Wireless Standards

| Standard | Freq Band | Data Rate | Application |
|----------|-----------|-----------|-------------|
| GSM | 900/1800 MHz | 270 kb/s | Cellular |
| WiFi (802.11b/g/n) | 2.4 GHz | 11-300 Mb/s | WLAN |
| Bluetooth | 2.4 GHz | 1-3 Mb/s | Short-range |
| GPS | 1.5 GHz | 50 b/s | Navigation |
| UWB | 3.1-10.6 GHz | 480+ Mb/s | High-speed |

## 1.3 RF Circuit Components

**Passive:** Inductors (spiral on-chip), capacitors (MIM/MOS), transmission lines

**Active:** MOSFET (dominant in CMOS RF), BJT/HBT (for high f_T), diodes (varactors)
