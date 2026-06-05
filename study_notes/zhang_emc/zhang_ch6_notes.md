# Chapter 6: EMC Design and Implementation of General Electronic Equipment
*Source: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Chapter 6, pp. 155-211*

---

## 6.1 Spacecraft Equipment-Level EMC Standards and Specifications | 设备级EMC标准与规范

**From the source:** *"The spacecraft equipment-level EMC standards include MIL-STD-461G-2015, MSFC-SPEC-521C-2013, GSFC-STD-7000A-2013, ECSS-E-20-07C-2012, AIAA-S-121A-2017, SMC-S-008-2008, ISO-14302-2002."*

### MIL-STD-461G as Reference Baseline

**From the source:** *"Due to the main role of MIL-STD-461G in equipment-level EMC requirements, it is taken as the reference baseline standard for other standards and specifications to be compared with."*

**Key test items in MIL-STD-461G:**

| Test | Description | Frequency Range |
|------|-------------|----------------|
| **CE101** | Conducted emissions, 30 Hz - 10 kHz | Power leads |
| **CE102** | Conducted emissions, 10 kHz - 10 MHz | Power leads |
| **CE106** | Conducted emissions, 10 kHz - 40 GHz | Antenna terminal |
| **RE101** | Radiated emissions, 30 Hz - 100 kHz | Magnetic field |
| **RE102** | Radiated emissions, 10 kHz - 18 GHz | Electric field |
| **CS101** | Conducted susceptibility, 30 Hz - 150 kHz | Power leads |
| **CS103** | Conducted susceptibility, 10 kHz - 1 GHz | Antenna terminal |
| **CS114** | Conducted susceptibility, 10 kHz - 200 MHz | Bulk cable injection |
| **CS115** | Conducted susceptibility, impulse excitation | Bulk cable injection |
| **CS116** | Conducted susceptibility, damped sine wave transients | Power leads |
| **RS101** | Radiated susceptibility, 30 Hz - 100 kHz | Magnetic field |
| **RS103** | Radiated susceptibility, 10 kHz - 18 GHz | Electric field |

**Two newly added test items (from source):**
- **CS117:** Lightning effect (system-level E3 requirements)
- **CS118:** Human body electrostatic effect (ESD protection)

### Special Requirements from Other Standards

**MSFC-SPEC-521C:**
- **CE108:** Bundled cable CE from 150 kHz to 200 MHz (similar to CS114)
- **CS109:** Structure current CS of 60 Hz - 100 kHz for equipment with operating frequency < 100 kHz

**GSFC-STD-7000A:**
- Power and signal lines common-mode CE (150 kHz - 200 MHz)
- Start-up transient CE for power-on conditions

---

## 6.2 General EMC Design Requirements for Equipment | 设备通用EMC设计要求

**From the source:** *"The general EMC design requirements for spacecraft equipment include bonding, shielding, filtering, cable layout, and component selection."*

### 6.2.1 Bonding Requirements

**From the source:** *"The electrical bonding of spacecraft structures and equipment are classified into Class C, H, R, and S."*

**Key bonding requirements:**

| Requirement | Value | Application |
|-------------|-------|-------------|
| Class C (Current Return) | < 0.1 mΩ | Power current return path |
| Class H (Fault Protection) | < 2.5 mΩ, low inductance | Personnel safety, fire prevention |
| Class R (RF/EMI Suppression) | < 1.0 mΩ | RF equipment, EMI control |
| Class S (ESD Control) | — | Electrostatic charge control |

**From the source:** *"The DC resistance between the equipment bonding stud and the nearby spacecraft structure shall be less than 2.5 mΩ."*

### 6.2.2 Shielding Requirements

**From the source:** *"The spacecraft should be structured as a 'Faraday cage' and consider apertures used for pressure drop during ascent and for outgassing."*

**Shielding effectiveness targets:**
- General enclosure: > 60 dB
- High-sensitivity equipment: > 80 dB
- Critical RF systems: > 100 dB

### 6.2.3 Filtering Requirements

**Filter design principles from the source:**
- Filter insertion loss should provide sufficient attenuation for conducted emissions
- Filters should not degrade signal integrity for sensitive circuits
- Feedthrough capacitors for RF penetration points

### 6.2.4 Cable Layout

**From the source:** *"The cables shall be bunched according to the requirements of classification. Similar cables can be integrated into the same bundle. If different cables are routed on parallel paths, they shall be separated by 5 cm or by a metal screen."*

**Cable classification and routing:**
| Cable Type | Separation Requirement |
|-----------|----------------------|
| Power (high current) | Isolated from signal cables |
| RF/analog | Shielded, separated from digital |
| Low-level signal | Maximum separation from interference sources |

---

## 6.3 General EMC Analysis, Design and Implementation | 通用EMC分析、设计与实现

**From the source:** *"The EMC design process should be integrated into the overall equipment design cycle from the early stages."*

### 6.3.1 EMC Design Process

**Design flow from the source:**
1. Define equipment EMC requirements
2. Perform preliminary EMC analysis
3. Implement EMC control measures
4. Verify through analysis and test
5. Document and maintain traceability

### 6.3.2 PCB-Level EMC Design

**From the source:** *"PCB-level EMC design considers RF characteristics of traces, ground plane integrity, and component placement."*

**PCB EMC guidelines:**
| Aspect | Guideline | Rationale |
|--------|----------|-----------|
| Ground plane | Solid, continuous | Minimize return path impedance |
| Trace routing | Short, direct | Reduce radiation/ pickup |
| Decoupling | Multiple capacitor values | Broadband decoupling |
| Clock routing | Guard traces | Reduce crosstalk |
| Via stitching | Ground vias adjacent to signal vias | Ground continuity |

### 6.3.3 Component Selection

**EMC considerations in component selection:**
- Switching speed of digital devices (faster = more emissions)
- Output drive strength (minimal adequate)
- Input filtering (ESD protection diodes)
- Shielded enclosures for oscillators, clocks

### 6.3.4 EMC Test and Verification

**Equipment-level verification methods from the source:**
1. Analysis: Theoretical calculations, simulation
2. Unit testing: Individual equipment EMC characterization
3. Subsystem integration testing
4. System-level verification

**Documentation requirements:**
- EMC analysis reports
- Test plans and procedures
- Test results and compliance statements
- As-built configuration records

---

## Key Physical Parameters Summary

| Parameter | Symbol | Typical Value/Range |
|-----------|--------|-------------------|
| Bonding resistance (Class C) | $R_b$ | < 0.1 mΩ |
| Bonding resistance (Class H) | $R_b$ | < 2.5 mΩ |
| Bonding resistance (Class R) | $R_b$ | < 1.0 mΩ |
| Shielding effectiveness | $SE$ | > 60 dB |
| Cable separation | $d$ | > 5 cm (unshielded) |
| EMI margin | $M$ | > 6 dB |
| EED safety margin | $M_{\text{EED}}$ | > 20 dB |

---

**Note:** This notes is based on Chapter 6 of Zhang, *Spacecraft Electromagnetic Compatibility Technologies* (2020), pp. 155-211. All content from original source text. Bilingual format.