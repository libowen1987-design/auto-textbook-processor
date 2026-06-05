# Chapter 4: Introduction to Spacecraft EMC Prediction Analysis Methods
*Source: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Chapter 4, pp. 80-106*

---

## 4.1 EMC Electromagnetic Field Analysis Methods | EMC电磁场分析方法

### 4.1.1 Tasks and Characteristics of EMC Analysis

**From the source:** *"Analysis and design are important engineering processes in the spacecraft EMC, and analysis is the prerequisite of design. The main task of EMC analysis is to evaluate the EMC characteristics and the state of the system or equipment."*

**Analysis tasks:**
1. Evaluate EMC characteristics of system/equipment
2. Predict potential EMI problems before they occur
3. Support design optimization decisions
4. Verify compliance with EMC requirements

### 4.1.2 Main EMC Analysis Methods

| Method | Application | Key Parameters |
|--------|-------------|----------------|
| **Analytical Analysis** | Simple geometries, canonical problems | Field distributions, impedance |
| **Numerical Simulation** | Complex geometries, arbitrary structures | MoM, FDTD, FEM, TLM |
| **Semi-empirical Methods** | Engineering approximations | Empirical coefficients, correction factors |
| **Statistical Analysis** | Uncertainty quantification | Probability distributions, Monte Carlo |

**From the source on numerical methods:**
> *"Numerical simulation methods such as Method of Moments (MoM), Finite Difference Time Domain (FDTD), and Finite Element Method (FEM) are widely used in EMC analysis for complex spacecraft structures."*

---

## 4.2 EMC Prediction and Modeling | EMC预测与建模

### 4.2.1 EMI Source Modeling

**Key EMI sources in spacecraft from the source:**
- Switching power supplies (开关电源)
- Digital circuits with fast clock edges (快速边沿数字电路)
- RF transmitters (射频发射机)
- Electromechanical devices (机电设备)

**Source characterization parameters:**
- Conducted emission spectrum (传导发射频谱)
- Radiated emission pattern (辐射发射方向图)
- Peak/average power (峰值/平均功率)
- Duty cycle (占空比)

### 4.2.2 Coupling Path Analysis

**From the source:** *"Coupling paths in spacecraft include conducted coupling through power and signal lines, and radiated coupling through free space."*

**Coupling path types:**
| Path Type | Mechanism | Analysis Method |
|-----------|-----------|----------------|
| **Conducted (传导)** | Current injection into shared networks | S-parameter analysis, circuit simulation |
| **Radiated (辐射)** | Electromagnetic field coupling | Full-wave EM simulation |
| **Near-field coupling** | Reactive field coupling | Hybrid near/far field methods |
| **Grounding/bonding** | Common impedance coupling | Transfer impedance models |

### 4.2.3 Receiver Susceptibility Modeling

**Susceptibility characteristics from the source:**
- Frequency response of receiver front-end
- Maximum allowable input power/field strength
- Immunity test thresholds (per applicable standards)

---

## 4.3 EMC Analysis Process | EMC分析流程

### 4.3.1 System-Level EMC Analysis

**From the source:** *"System-level EMC analysis should consider the electromagnetic environment, interface characteristics, and the vulnerability of all subsystems."*

**Analysis steps:**
1. Define system electromagnetic environment
2. Identify all potential EMI sources and receivers
3. Analyze coupling paths
4. Calculate EMI margins at each interface
5. Recommend mitigation measures if margins are insufficient

### 4.3.2 Equipment-Level EMC Analysis

**From the source:** *"Equipment-level EMC analysis focuses on the emissions and susceptibility of individual equipment units."*

**Key analysis parameters:**
- Emission limits per applicable standards (MIL-STD-461G, etc.)
- Susceptibility thresholds
- Internal shielding and filtering effectiveness
- Cable shielding and routing

### 4.3.3 EMC Budget Analysis

**EMI margin budget approach:**
$$EMI_{\text{margin}} = L_{\text{susceptibility}} - L_{\text{emission}}$$

**Budget allocation from the source:**
- Source emission allocation (e.g., -10 dB below limit)
- Path loss allocation (coupling loss target)
- Receiver susceptibility margin

---

## 4.4 Typical EMC Analysis Examples | 典型EMC分析实例

### 4.4.1 Printed Circuit Board (PCB) EMC Analysis

**From the source:** *"PCB-level EMC analysis considers the RF characteristics of traces, ground plane effects, and component radiation patterns."*

**Key PCB EMC parameters:**
| Parameter | Impact | Mitigation |
|-----------|--------|------------|
| Trace impedance | Reflection, radiation | Controlled impedance routing |
| Return current path | Common impedance | Solid ground plane |
| Loop area | Antenna effect | Minimize loop size |
| Decoupling | High-frequency bypassing | Proper decoupling capacitor placement |

### 4.4.2 Cable Harness EMC Analysis

**From the source:** *"Cable harness EMC analysis evaluates the pickup and radiation characteristics of interconnecting cables."*

**Cable EMC control measures:**
- Shielded cables for sensitive signals
- Twisted pair for balanced transmission
- Separation distances for different signal types
- Ferrite cores for common-mode suppression

---

## 4.5 EMC Test and Verification | EMC测试与验证

### 4.5.1 Ground Testing Methods

**From the source:** *"Ground EMC testing provides verification of analytical predictions and identifies unexpected EMI issues."*

**Test methods:**
| Test Type | Purpose | Typical Equipment |
|-----------|---------|------------------|
| Conducted emissions (CE) | Measure conducted EMI on power/signal lines | LISN, spectrum analyzer |
| Radiated emissions (RE) | Measure radiated EMI | Antenna, absorber-lined room |
| Conducted susceptibility (CS) | Test immunity to conducted disturbances | Injection transformer, signal generator |
| Radiated susceptibility (RS) | Test immunity to radiated fields | Field generator, antenna |

### 4.5.2 Test Site Requirements

**From the source:** *"EMC testing should be conducted in controlled electromagnetic environments such as anechoic chambers or shielded rooms."*

**Site characteristics required:**
- Low extraneous signals (high isolation)
- Controlled reflection levels (for radiated tests)
- Calibrated field levels (for susceptibility tests)

---

**Note:** This notes is based on Chapter 4 of Zhang, *Spacecraft Electromagnetic Compatibility Technologies* (2020), pp. 80-106. Physical quantities explained with reference to source text. Bilingual format.