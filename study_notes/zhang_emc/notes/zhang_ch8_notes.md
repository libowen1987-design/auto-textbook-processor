# Chapter 8: EMC Design and Rectification for Typical Equipment
*Source: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Chapter 8, pp. 251-295*

---

## 8.1 EMC Design of Power Supply and Distribution | 电源与配电系统的EMC设计

**From the source:** *"The power supply and distribution system is a major source of conducted emissions. Its design directly affects the EMC performance of the entire spacecraft."*

### Equipment Layout | 设备布局

**From the source:** *"The layout of power supply equipment should consider the separation between power processing components and sensitive circuits."*

**Layout principles:**
1. Isolate high-power switching circuits from sensitive analog circuits
2. Use physical barriers (metal shields) between noisy and quiet zones
3. Route high-current traces away from signal cables

### Power Supply Filtering Design | 电源滤波器设计

**From the source:** *"Power supply filtering is essential for meeting conducted emission limits. The filter must provide sufficient attenuation without degrading power quality."*

**Filter design approach:**
| Stage | Function | Key Components |
|-------|----------|---------------|
| **Input filter** | Reduce upstream emissions | Common mode choke, X-capacitors |
| **Output filter** | Isolate load noise | π-section or T-section filters |
| **Decoupling** | High-frequency bypassing | Multi-layer ceramic capacitors |

---

## 8.2 EMC Design and Rectification for System Management | 系统管理的EMC设计与整改

**From the source:** *"System management circuits include microprocessors, memory, and timing circuits. These digital circuits require careful EMC design to prevent interference with other subsystems."*

### Clock Distribution

**Key EMC concerns:**
- Clock harmonics can cause radiated emissions
- Clock jitter affects spectral purity
- Simultaneous switching causes ground bounce

**Mitigation techniques:**
- Use spread-spectrum clock generators
- Distribute clock on twisted pairs with ground reference
- Implement proper termination to prevent reflections

---

## 8.3 EMC Design for Integrated Services Unit | 综合服务单元的EMC设计

**From the source:** *"Integrated services units combine multiple functions (telecom, telemetry, command) in a single module. This integration creates potential EMI coupling paths between previously separated circuits."*

**Design considerations:**
- RF shielding between transmit and receive sections
- Isolation of digital processing from RF front-ends
- Grounding strategy for mixed-signal circuits

---

## 8.4 EMC Design of Solid State Power Amplifier | 固态功率放大器的EMC设计

**From the source:** *"Solid state power amplifiers (SSPA) generate significant thermal and electromagnetic emissions. The EMC design must address both thermal management and EMI control."*

**Key EMC issues:**
- Harmonic generation at multiples of fundamental frequency
- Intermodulation products in multi-carrier operation
- Power supply interactions causing amplitude modulation

**Design for compliance:**
| Parameter | Requirement | Method |
|-----------|-------------|--------|
| Harmonic emissions | < -60 dBc | Output filtering |
| Spurious emissions | < -80 dBc | Shielding, filtering |
| Conducted emissions | MIL-STD-461G CE102 | Input filtering |

---

## 8.5 EMC Design of RF Receiver | 射频接收机的EMC设计

**From the source:** *"RF receivers are highly sensitive to external interference. The EMC design must protect the receiver front-end from both self-generated and external EMI."*

**Key susceptibility concerns:**
- Desensitization by strong out-of-band signals
- Intermodulation in preamplifier stages
- Cross-modulation from AM interference

**Design for immunity:**
- Front-end bandpass filtering
- Limiting amplifiers for automatic gain control
- Shielded enclosures for LNA stages

---

**Note:** This notes is based on Chapter 8 of Zhang, *Spacecraft Electromagnetic Compatibility Technologies* (2020), pp. 251-295. Bilingual format.