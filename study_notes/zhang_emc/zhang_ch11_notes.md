# Chapter 11: Spacecraft System-Level EMC Test Verification
*Source: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Chapter 11, pp. 411-470*

---

## 11.1 Electromagnetic Environmental Effect (E3) Test | 电磁环境效应(E3)测试

### 11.1.1 Test Requirements | 测试要求

**From the source:** *"The system electromagnetic environment effect (E3) requirements are based on the general development requirements or specifications in the contract, which include the test content and specific test items. The E3 test shall be carried out according to the test program."*

**E3 test categories (from source):**
| Category | Content | Applicable Standard |
|---------|---------|-------------------|
| Radiated emissions | RE102, RE103 | MIL-STD-461G |
| Radiated susceptibility | RS101, RS103 | MIL-STD-461G |
| Conducted emissions | CE101, CE102 | MIL-STD-461G |
| Conducted susceptibility | CS101, CS114, CS115, CS116 | MIL-STD-461G |
| Lightning | CS117 | MIL-STD-464C |
| ESD | CS118 | MIL-STD-464C |

### 11.1.2 System-Level Verification | 系统级验证

**From the source:** *"System-level EMC verification confirms that all subsystems and equipment function correctly together under the specified electromagnetic environment."*

**Verification levels:**
1. **Unit level:** Individual equipment testing
2. **Subsystem level:** Integration testing of multiple units
3. **System level:** Full spacecraft EMC characterization

---

## 11.2 Intrasystem EMC Analysis | 系统内EMC分析

**From the source:** *"Intrasystem EMC analysis evaluates the electromagnetic compatibility between spacecraft subsystems and equipment operating simultaneously."*

**Analysis scope:**
- Transmitter-receiver isolation
- Digital clock interference with RF circuits
- Power bus noise coupling to sensitive circuits

---

## 11.3 Lightning and EMP Testing | 雷电与电磁脉冲测试

**From the source:** *"Lightning and electromagnetic pulse (EMP) tests verify the spacecraft's ability to withstand high-intensity electromagnetic environments."*

**CS117 lightning test requirements (from source):**
- Current waveform: damped sinusoid
- Peak current: up to 1000 A
- Duration: varies by test level

---

## 11.4 Test Documentation and Compliance | 测试文档与符合性

**From the source:** *"All EMC test results must be documented and reviewed against the applicable requirements to determine compliance."*

**Required documentation:**
- Test procedures and setup photos
- Raw measurement data
- Data reduction calculations
- Pass/fail determination with margin
- Non-conformance reports (if applicable)

---

**Note:** This notes is based on Chapter 11 of Zhang, *Spacecraft Electromagnetic Compatibility Technologies* (2020), pp. 411-470. Bilingual format.