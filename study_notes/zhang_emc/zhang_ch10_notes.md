# Chapter 10: EMC Test Verification of Spacecraft Electronic Equipment
*Source: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Chapter 10, pp. 334-410*

---

## 10.1 Description of Interpolations and Factors in Computer-Based Test Software | 计算机测试软件中的插值与因子

**From the source:** *"In the EMC test verification, some items can be implemented by computer-based automation tests. In numerical calculations, the parameters of various sensor factors and cable losses are calculated according to the linear interpolation method."*

### Interpolation in EMC Testing

**Linear interpolation formula:**
$$y = y_1 + \frac{(y_2 - y_1)(x - x_1)}{x_2 - x_1}$$

**Application in EMC test software:**
| Parameter | Interpolation Use |
|-----------|-------------------|
| Antenna factor | Frequency-dependent calibration data |
| Cable loss | Length-dependent attenuation |
| Sensor sensitivity | Temperature compensation |
| Field strength | Distance-dependent decay |

### Correction Factors in Test Measurements

**From the source:** *"Test correction factors include: antenna pattern correction, site attenuation correction, cable loss correction."*

---

## 10.2 Test Instrumentation and Calibration | 测试仪器与校准

**Key instruments:**
| Instrument | Purpose | Calibration Requirement |
|-----------|---------|------------------------|
| Spectrum analyzer | Emission measurement | Annual calibration |
| Signal generator | Susceptibility testing | Traceability to national standards |
| Antenna | Field measurement | Pattern calibration |
| LISN | Conducted measurement | Impedance verification |
| Power meter | Power measurement | Weekly calibration |

---

## 10.3 EMC Test Procedures | EMC测试程序

**From the source:** *"EMC test procedures should follow the applicable standards (MIL-STD-461G, MIL-STD-464C, etc.) and be documented in detailed test plans."*

**Test plan structure:**
1. Test objectives and requirements
2. Equipment under test (EUT) description
3. Test configuration and setup
4. Measurement procedures
5. Data reduction and reporting
6. Pass/fail criteria

---

**Note:** This notes is based on Chapter 10 of Zhang, *Spacecraft Electromagnetic Compatibility Technologies* (2020), pp. 334-410. Bilingual format.