# Chapter 3: Electromagnetic Compatibility Management | 第3章：电磁兼容性管理
*Source: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Chapter 3, pp. 63-79*

---

## 3.1 Overview of EMC Management Standards | EMC管理标准概述

**Main spacecraft EMC management standards and manuals from the source:**

| Standard | Organization | Content |
|----------|--------------|---------|
| DEF-STAN 59-411 Part 1-2014 | UK Defense Standards | EMC Management and Planning |
| MIL-HDBK-237D-2005 | US DoD | Electromagnetic Environmental Effects Management |
| GJB/Z 170-2018 | China | Design Process for Spacecraft EMC Risk Management |

**Core standard systems by region:**

| Region | Primary Standards |
|--------|-------------------|
| **Europe** | ECSS-E-ST-20-07C, ECSS-E-HB-20-07A |
| **USA** | MIL-STD-464C, MIL-HDBK-237D |
| **UK** | DEF-STAN 59-411 |
| **China** | GJB/Z 170, GJB 151B |

---

## 3.2 The Spacecraft EMC Management | 航天器EMC管理

### 3.2.1 Main EMC Management Activities (Based on DEF STAN 59-411)

**Key EMC management activities from the source:**
1. EMC management planning
2. EMC design and analysis
3. EMC verification and testing
4. EMC documentation and traceability

### 3.2.2 EMC Risk Management

**From the source:** *"The EMC risk management design process should identify potential EMC problems early in the development phase, evaluate their impact on system performance, and implement mitigation measures before they become critical."*

**Risk assessment matrix (航天器EMC风险矩阵):**
| Risk Level | Criteria | Action |
|------------|----------|--------|
| **Critical** | EMI margin < 0 dB, no mitigation possible | Redesign required |
| **High** | EMI margin 0-6 dB, mitigation possible | Detailed analysis + testing |
| **Medium** | EMI margin 6-20 dB | Standard controls sufficient |
| **Low** | EMI margin > 20 dB | Routine verification |

---

## 3.3 EMC Working Group | EMC工作组

### 3.3.1 Responsibilities of the EMC Working Group

**From the source:** *"The EMC Working Group is responsible for coordinating EMC activities across all subsystems, ensuring compliance with EMC requirements, and managing EMC risk throughout the project lifecycle."*

### 3.3.2 Tasks of the EMC Working Group

**Main tasks:**
1. Review and approve EMC control plans
2. Coordinate EMC testing activities
3. Resolve EMC non-conformances
4. Maintain EMC risk register
5. Provide EMC training and guidance

### 3.3.3 System-Level and Equipment-Level EMC Personnel

| Role | Responsibility |
|------|--------------|
| **System-Level EMC Supervisor** | Overall system EMC compliance, interface control |
| **Equipment-Level EMC Designer** | Individual equipment EMC design and verification |

---

## 3.4 EMC Control Program and Technical Requirements | EMC控制程序与技术要求

### 3.4.1 EMC Control Plan Structure

**From the source:** *"The EMC control program should include the following elements: EMC requirements document, EMC control plan, EMC analysis reports, EMC test plans and results, EMC verification reports."*

### 3.4.2 Technical Requirements Flow-Down

**Requirements flow-down hierarchy:**
```
Mission-Level EMC Requirements
    ↓
System-Level EMC Requirements
    ↓
Subsystem-Level EMC Requirements
    ↓
Equipment-Level EMC Requirements
```

**Flow-down principles from the source:**
- Requirements should be traceable from top-level mission objectives to individual equipment specifications
- Each level should add margin to protect against accumulated uncertainties
- Verification methods should be specified at each level

### 3.4.3 Verification and Compliance

**Verification methods:**
1. **Analysis (分析):** Theoretical analysis, simulation, calculation
2. **Test (测试):** Ground testing, flight testing
3. **Inspection (检查):** Design review, physical inspection

**Compliance verification levels:**
- Unit level (single equipment)
- Subsystem level (multiple equipment integration)
- System level (full spacecraft)

---

**Note:** This notes is based on Chapter 3 of Zhang, *Spacecraft Electromagnetic Compatibility Technologies* (2020), pp. 63-79. Bilingual format, physical quantities explained with reference to source text.