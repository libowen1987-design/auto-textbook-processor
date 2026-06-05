# Chapter 5: Analysis of Spacecraft System-Level EMC
*Source: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Chapter 5, pp. 85-175*

---

## 5.1 Overview of Standards for Spacecraft System-Level EMC | 系统级EMC标准概述

**From the source:** *"The design of the Chinese spacecraft is mainly based on the national standards, the national military standards, and the standards of the aerospace industry."*

**Main international standards covered:**

| Standard | Origin | Key Content |
|----------|--------|-------------|
| **MIL-STD-464C-2010** | US DoD | EME requirements for systems |
| **AIAA-S-121A-2017** | USA | EMC requirements for space equipment |
| **SMC-S-008-2008** | US Air Force | EMC requirements for space equipment |
| **ECSS-E-ST-20C-2008** | European ESA | Electrical and electronic space engineering |
| **ECSS-E-ST-20-07C-2012** | European ESA | EMC for space systems |
| **ISO 14302-2002** | International | EMC requirements for space systems |

**System-level EMC requirements from the source:**
The system-level EMC requirements (also called EME requirements for systems) clarify EMI control requirements by analyzing the impact of the system's internal and external electromagnetic environment on system performance.

**Key requirements include:**
- EMI margins
- External RF electromagnetic environment
- HPM sources and EMP
- Lightning
- Electrostatic charge control
- Intra-system EMC
- EMRADHAZ (Electromagnetic Radiation Hazards)

**Figure 5.1 relationship (from source):**
```
Spacecraft system design → Life cycle → E3 hardness
Internal EME → External RF EME → HPM sources
Lightning effect → EMP effect → Electrostatic charging control
Systematic analysis of EME → Subsystem and equipment EMI
Electric bonding, grounding, isolation → Margins
```

---

## 5.2 Determination of EMI Margin | EMI裕量的确定

**From the source:** *"The verification method of electromagnetic interference margin in space system is introduced, including electromagnetic self-compatibility and electromagnetic interference margin in both conducted and radiated states."*

### EMI Margin Verification Process

**Verification basis:** Analysis and test methods shall fulfill respective approval procedures and comply with corresponding standards.

### Self-compatibility Verification

**From the source:** *"The electronic equipment shall be fully configured and all equipment shall be deployed according to the working state (including solar arrays)."*

**Key verification items:**

| Verification Type | Method | Key Parameter |
|-------------------|--------|---------------|
| **Conducted emission** | Monitor power line emissions | Frequency domain + time domain |
| **Radiated emission** | Monitor system electric and magnetic fields | RE102 compliance |
| **External RFI + EMI margin** | RS103 susceptibility test | 6 dB margin requirement |
| **PIM** | Monitor PIM products | RE102 + EMI margin |

### EMI Margin Calculation

**From the source:**
$$EMI_{\text{margin}} = L_{\text{susceptibility}} - L_{\text{emission}} \quad [\text{dB}]$$

**Verification requirements:**
- Dwell time at each frequency: not less than 3 s
- Test duration: at least 20 min
- EED safety margin: 20 dB

---

## 5.3 Inter-system EMC Analysis | 系统间EMC分析

**From the source:** *"Inter-system EMC analysis considers the electromagnetic compatibility between the spacecraft and external electromagnetic sources such as ground stations, other satellites, and environmental radiation."*

### 5.3.1 Launch Vehicle EMC Analysis

**Coupling analysis areas:**
- RF interference between launch vehicle and spacecraft communication systems
- Electromagnetic environment during launch sequence
- Separation plane EMC analysis

**Key parameters from the source:**
- Frequency compatibility
- Power levels and isolation
- Time-domain coordination

### 5.3.2 Ground Station Compatibility

**From the source:** *"The analysis of the impact of launch vehicle/site radiation on spacecraft should consider the high-power RF radiation from tracking radars and measurement equipment."*

### 5.3.3 Electromagnetic Radiation Field Intensity Analysis

**Analysis of electromagnetic radiation field intensity near spacecraft:**
- Near-field effects from high-power transmitters
- Multiple reflection paths (multipath effect)
- Polarization isolation requirements for GEO satellites

---

## 5.4 EMC Limitation Analysis | EMC限制分析

**From the source:** *"EMC limitation analysis ensures that all electromagnetic emissions from the spacecraft remain below specified limits throughout its operational lifecycle."*

**Analysis scope:**
- Radiated emission limits (RE102, etc.)
- Conducted emission limits (CE101, CE102, etc.)
- Susceptibility thresholds (RS101, RS103, etc.)

---

## 5.5 RF Compatibility Analysis for Spacecraft | 航天器射频兼容性分析

**From the source:** *"RF compatibility analysis evaluates the potential for interference between transmit and receive systems on board the spacecraft."*

### RF Compatibility Key Parameters

| Parameter | Definition | Typical Requirement |
|-----------|-----------|---------------------|
| **Tx emission** | Unintentional radiation from transmitter | <-60 dBc (spurious) |
| **Rx sensitivity** | Minimum detectable signal | Signal floor |
| **Isolation** | Coupling between Tx and Rx | > 80 dB |
| **Intermodulation** | PIM products in multi-carrier systems | < -100 dBm |

---

## 5.6 Evaluation of Passive Intermodulation Using Full-Wave | 无源互调的全场分析

**From the source:** *"The RF transmissions from on-board equipment, or from external transmitters may interact with the electronic equipment to produce unintentional signals such as PIM."*

**PIM characteristics:**
- PIM order: up to 7th order or higher
- PIM frequencies: $|nf_1 \pm mf_2|$ where $n, m$ are integers
- Sources: nonlinear contact junctions, contaminated surfaces

**Mitigation measures (from source):**
- Electrical bonding of equipment (resistance $0.1 - 500\ \text{m}\Omega$)
- Semiconductor device protection from RF exposure
- Environmental field strength limit: $< 250$ mV/m within working band

---

## 5.7 Cable Crosstalk Analysis | 电缆串扰分析

**From the source:** *"Cable crosstalk analysis evaluates the coupling between adjacent signal cables in the spacecraft harness."*

**Crosstalk mechanisms:**
- **Capacitive coupling (容性耦合):** Electric field coupling through parasitic capacitance
- **Inductive coupling (感性耦合):** Magnetic field coupling through mutual inductance

**Reduction techniques:**
| Technique | Application |
|-----------|-------------|
| Shielded cables | Critical signal paths |
| Twisted pair | Balanced circuits |
| Physical separation | Different signal classes |
| Ferrites | Common-mode suppression |

---

## 5.8 Field-Cable Coupling Analysis | 场-电缆耦合分析

**From the source:** *"External electromagnetic fields can couple into spacecraft cables through apertures and unshielded sections."*

**Coupling calculation:**
$$V_{\text{induced}} = \int_0^l \mathbf{E}(\mathbf{r}) \cdot \mathbf{dl} \cdot \text{shielding effectiveness}$$

**Shielding effectiveness requirements:**
- Shielded cables: typically > 60 dB attenuation
- Aperture coupling: depends on aperture dimensions relative to wavelength

---

## 5.9 Hazards and Protection of Electromagnetic Radiation | 电磁辐射危害与防护

**From the source:** *"Electromagnetic radiation hazards (EMRADHAZ) include effects on fuels, personnel, and EEDs, while ensuring that electronically actuated thrusters are not exposed to unsafe electromagnetic radiation levels."*

### EMRADHAZ Categories

| Category | Affected Object | Hazard Level |
|----------|----------------|--------------|
| **Personnel** | Humans in RF field | Specific absorption rate (SAR) limits |
| **EED** | Electro-explosive devices | Safety margin ≥ 20 dB |
| **Fuel** | Flammable materials | Ignition threshold analysis |
| **Thrusters** | Electronic actuators | Field strength limits |

**From the source on fuel ignition:**
> *"The voltage on the casing of electronic equipment should generally be lower than 4.5V, and no bonding damage or fire will occur due to a short circuit."*

---

## 5.10 Summary | 总结

**Key takeaways from Chapter 5:**
1. System-level EMC requires comprehensive analysis of internal and external EME
2. EMI margin verification is the primary compliance metric
3. PIM and multipath are critical issues for spacecraft RF systems
4. EMRADHAZ must be addressed for all safety-critical systems
5. EMI control requires system-level approach across all subsystems

---

**Note:** This notes is based on Chapter 5 of Zhang, *Spacecraft Electromagnetic Compatibility Technologies* (2020), pp. 85-175. All technical content sourced from original text. Bilingual format for bilingual reference.