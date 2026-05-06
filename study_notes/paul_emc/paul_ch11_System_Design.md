---
chapter: 11
title: System Design for EMC
source: Paul, Clayton R. *Introduction to Electromagnetic Compatibility*, 2nd Ed., Wiley, 2006
pages: 777-1013
---

# Chapter 11: System Design for EMC

## 11.1 PCB Layer Stackup Strategy

### Recommended Stackups

| Layers | Stackup | Best For |
|---|---|---|
| 2-layer | Signal + pour | Low-speed (< 10 MHz) |
| 4-layer | Signal - GND - PWR - Signal | General-purpose |
| 6-layer | Signal - GND - Signal - PWR - GND - Signal | High-speed digital |
| 8-layer | Signal - GND - Signal - GND - PWR - Signal - GND - Signal | Very high-speed |

### Critical Rules
1. **Every signal layer must be adjacent to a reference plane** (GND preferred)
2. **Minimize distance between signal and reference plane** (reduces loop area)
3. **Use at least one dedicated ground plane** (return path integrity)
4. **Split planes only under controlled conditions** (avoid crossing splits with signals)

### Stackup Impedance Control

For a 4-layer board with 0.25 mm prepreg:

$$Z_0 \approx \frac{87}{\sqrt{\varepsilon_r + 1.41}} \ln\left(\frac{5.98h}{0.8w + t}\right)$$

Typical FR-4 ($\varepsilon_r = 4.5$), $h = 0.2$ mm, $w = 0.3$ mm → $Z_0 \approx 50\ \Omega$

## 11.2 Grounding Strategies

| Frequency | Ground Strategy | Description |
|---|---|---|
| < 1 MHz | Single-point ground | Star ground, one reference point |
| 1–10 MHz | Hybrid | Single-point + multi-point mix |
| > 10 MHz | Multi-point ground | Ground plane, multiple connections |

### Single-Point Ground (SPG)

$$\text{Common impedance coupling} < \frac{\lambda}{20} \text{ constraint}$$

Used for: audio, low-frequency analog, safety grounds.

### Multi-Point Ground (MPG)

All circuits connect to a low-impedance ground plane. Return currents follow the path of minimum impedance (at HF: path of minimum loop area).

### Ground Loops

A ground loop is formed when there are multiple paths between two ground points. The loop area acts as a receiving loop antenna:

$$V_{\text{loop}} = \mu_0 A \frac{dH}{dt}$$

**Breaking ground loops:**
- Optical isolation
- Common-mode choke
- Transformer isolation
- Physical separation of grounds

## 11.3 Decoupling and Bypass Capacitors

### Decoupling Strategy

| Frequency | Capacitor Type | Mounting |
|---|---|---|
| < 1 MHz | 10–100 $\mu$F electrolytic | Bulk storage |
| 1–100 MHz | 0.01–0.1 $\mu$F MLCC | Near each IC |
| 100 MHz–1 GHz | 100 pF–1 nF MLCC 0402 | Under IC, shortest loop |
| > 1 GHz | Embedded capacitance (plane) | Power/GND sandwich |

### Mounting Inductance

**Critical:** Via inductance dominates decoupling at high frequencies.

$$L_{\text{via}} \approx 1.3 \text{ nH/mm} \cdot h \left[ \ln\left(\frac{4h}{d}\right) + 1 \right]$$

For $h = 1.6$ mm, $d = 0.3$ mm: $L_{\text{via}} \approx 1.2$ nH.

**SRF of a decoupling capacitor** including vias:

$$f_{\text{SR}} = \frac{1}{2\pi\sqrt{(C \cdot \text{ESL}_{\text{total}})}}$$

where $\text{ESL}_{\text{total}} = \text{ESL}_{\text{cap}} + \text{ESL}_{\text{pad}} + \text{ESL}_{\text{via}}$.

## 11.4 I/O Filtering

### Ferrite Bead + Capacitor Filter

$$\text{Insertion Loss} = 20 \log_{10}\left[1 + \frac{1}{2}\left(\frac{Z_b}{R_S} + \frac{R_L}{Z_b} + \frac{Z_b}{Z_c}\right)\right]$$

where $Z_b$ = bead impedance, $Z_c = 1/j\omega C$.

### Filter Placement
- **Input filter:** Before any other circuit (within 10 mm of connector)
- **Output filter:** After all processing, right at connector
- **Shield penetration:** Filter at the shield wall entry point

### Common I/O Filter Topologies

| Topology | Attenuation | Components |
|---|---|---|
| C-filter | -20 dB/dec | Single cap to GND |
| L-filter | -20 dB/dec | Series inductor/ferrite |
| Pi-filter | -40 dB/dec | C-L-C |
| T-filter | -40 dB/dec | L-C-L |

## 11.5 Cable and Connector Design

### Cable Selection for EMC

| Cable Type | Shielding | Use Case |
|---|---|---|
| Unshielded twisted pair (UTP) | None | Low-frequency signals (< 10 MHz) |
| Shielded twisted pair (STP) | Braid 80–95% | Mid-frequency signals |
| Coaxial | Solid braid | RF signals |
| Triaxial | Double shield | Sensitive measurements |
| Ribbon cable with ground | Every 3rd wire GND | Digital buses |

### Connector Grounding

**Rule:** Connect the cable shield to chassis at the connector entry point, not to the signal ground.

```
Cable Shield ──┬── Chassis GND (via connector shell)
                │
                └── 1 nF cap ── Signal GND (for HF only)
```

### Shield Termination: 360° vs Pigtail

- **Pigtail:** 1 cm pigtail creates ~10 nH inductance → degrades SE by 10–20 dB at 100 MHz
- **360° ferrule:** Inductance < 0.1 nH → full SE maintained

## 11.6 ESD Protection

### ESD Discharge Path

The ESD current must be diverted away from sensitive circuits:

$$I_{\text{ESD}} \approx \frac{V_{\text{ESD}}}{R_{\text{arc}} + R_{\text{body}}} \approx \frac{8\text{ kV}}{330\ \Omega} \approx 24\text{ A}$$

### Protection Devices

| Device | Clamp Voltage | Capacitance | Response Time |
|---|---|---|---|
| TVS diode | $V_{\text{BR}} + 0.5\text{V}$ | 1–10 pF | < 1 ns |
| Varistor | $V_{\text{BR}}$ | 10–100 pF | < 1 ns |
| Spark gap | 50–500 V | < 1 pF | 1–10 ns |
| Polymer PTC | Resettable | Low | Slow |

### PCB ESD Design Rules
1. **Keep ESD path away from clock traces** (> 3 mm spacing)
2. **Use guard ring** around sensitive I/O
3. **TVS diode as close to connector as possible** (< 5 mm)
4. **Place ESD ground vias** next to every TVS
5. **Avoid sharp corners** on ESD routing

## 11.7 Power Supply Design for EMC

### Buck Converter Noise

Switching power supplies are major noise sources. Key frequencies:
- **Switching frequency:** 100 kHz–2 MHz
- **Ringing at switch node:** 50–300 MHz (due to parasitic L-C)
- **Diode reverse recovery:** 10–50 MHz

### Mitigation

| Technique | Reduces |
|---|---|
| Snubber across switch node | Ringing (10–30 dB) |
| Input L-C filter | Conducted emissions (20–40 dB) |
| Shielded inductor | Radiated from inductor (10–20 dB) |
| Ground island for switcher | PCB coupling (10–20 dB) |

### Layout Critical Rules for DC-DC
1. **Minimize hot loop** (switch node to diode to cap) area
2. **Keep input cap close to FET**
3. **Use Kelvin connection** for current sense
4. **Separate power GND and signal GND** with single-point connection

## 11.8 Clock and High-Speed Routing

### Routing Rules

| Rule | Guideline |
|---|---|
| Maximum stub length | $< t_r/10$ |
| Minimum spacing (3W rule) | $3 \times$ trace width |
| Return via for layer transition | Within $\lambda/20$ of signal via |
| Differential pair length matching | $< t_r/20$ skew |
| Clock clearance to I/O | $> 5 \times$ dielectric height |

### Clock Line Filtering
- Series resistor at clock source (22–33 $\Omega$)
- Ferrite bead on clock output (if frequency allows)
- Keep clock traces short and direct
- Shield clock traces with GND vias along sides

## 11.9 Enclosure and Chassis Design

| Material | SE at 100 MHz | Notes |
|---|---|---|
| Steel (1 mm) | > 80 dB | Magnetic, heavy |
| Aluminum (2 mm) | > 50 dB | Non-magnetic, light |
| Plastic + coating | 20–40 dB | Coat with conductive paint/plating |
| Plastic (uncoated) | 0 dB | No shielding |

### Seam and Joint Design

| Joint Type | SE at 100 MHz | Cost |
|---|---|---|
| Welded/brazed | 80–100 dB | High |
| Gasketed (finger stock) | 80–100 dB | Medium |
| Overlapping (screws every 2 cm) | 40–60 dB | Low |
| Simple butt joint | 20–40 dB | Low |

## 11.10 Engineering Intuition

1. **Start EMC design at architecture phase.** Adding a ferrite during pre-compliance testing costs 10× more than designing it in.

2. **The return current path is the most important invisible trace.** Every signal must have a continuous return path directly underneath it.

3. **2-layer boards are the enemy of EMC.** The added cost of a 4-layer board (typically $0.50–1.00 per board) is the cheapest EMC fix available.

4. **I/O cables are antennas.** Every external cable should be treated as a potential transmit/receive antenna. Filter or shield at the enclosure boundary.

5. **10 ns → 1 ns rise time increases bandwidth by 10× and emission potential by 20 dB.** Use the slowest acceptable edge rate.

6. **EMC is not black magic.** It's good engineering: controlled impedance, minimal loop area, effective decoupling, proper grounding, and shielding where needed.
