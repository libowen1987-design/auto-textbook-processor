# Chapter 10: EMC Test Verification of Spacecraft Electronic Equipment

> **中英双语版**

*Source: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Chapter 10, pp. 334-410*
*来源：张《航天器电磁兼容性技术》(2020)，第10章，第334–410页*

---

## 10.1 Description of Interpolations and Factors in Computer-Based Test Software | 计算机测试软件中的插值与因子

**From the source / 来源原文：** *"In the EMC test verification, some items can be implemented by computer-based automation tests. In numerical calculations, the parameters of various sensor factors and cable losses are calculated according to the linear interpolation method."*
*"在EMC测试验证中，部分项目可通过计算机自动化测试实现。数值计算中，各种传感器因子参数和电缆损耗按线性插值法计算。"*

### Interpolation in EMC Testing / EMC测试中的插值

**Linear interpolation formula / 线性插值公式：**
$$y = y_1 + \frac{(y_2 - y_1)(x - x_1)}{x_2 - x_1}$$

**Application in EMC test software / 在EMC测试软件中的应用：**
| Parameter / 参数 | Interpolation Use / 插值用途 |
|-----------|-------------------|
| Antenna factor / 天线因子 | Frequency-dependent calibration data / 随频率变化的校准数据 |
| Cable loss / 电缆损耗 | Length-dependent attenuation / 随长度变化的衰减 |
| Sensor sensitivity / 传感器灵敏度 | Temperature compensation / 温度补偿 |
| Field strength / 场强 | Distance-dependent decay / 随距离变化的衰减 |

### Correction Factors in Test Measurements / 测试测量中的修正因子

**From the source / 来源原文：** *"Test correction factors include: antenna pattern correction, site attenuation correction, cable loss correction."*
*"测试修正因子包括：天线方向图修正、场地衰减修正、电缆损耗修正。"*

---

## 10.2 Test Instrumentation and Calibration | 测试仪器与校准

**Key instruments / 关键仪器：**
| Instrument / 仪器 | Purpose / 用途 | Calibration Requirement / 校准要求 |
|-----------|---------|------------------------|
| Spectrum analyzer / 频谱分析仪 | Emission measurement / 发射测量 | Annual calibration / 年度校准 |
| Signal generator / 信号发生器 | Susceptibility testing / 敏感度测试 | Traceability to national standards / 可溯源至国家标准 |
| Antenna / 天线 | Field measurement / 场测量 | Pattern calibration / 方向图校准 |
| LISN / 线路阻抗稳定网络 | Conducted measurement / 传导测量 | Impedance verification / 阻抗验证 |
| Power meter / 功率计 | Power measurement / 功率测量 | Weekly calibration / 每周校准 |

---

## 10.3 EMC Test Procedures | EMC测试程序

**From the source / 来源原文：** *"EMC test procedures should follow the applicable standards (MIL-STD-461G, MIL-STD-464C, etc.) and be documented in detailed test plans."*
*"EMC测试程序应遵循适用标准（MIL-STD-461G、MIL-STD-464C等），并在详细的测试计划中形成文件。"*

**Test plan structure / 测试计划结构：**
1. Test objectives and requirements / 测试目标与要求
2. Equipment under test (EUT) description / 受试设备(EUT)描述
3. Test configuration and setup / 测试配置与布置
4. Measurement procedures / 测量程序
5. Data reduction and reporting / 数据处理与报告
6. Pass/fail criteria / 通过/失效判据

---

**Note / 注：** This notes is based on Chapter 10 of Zhang, *Spacecraft Electromagnetic Compatibility Technologies* (2020), pp. 334-410. Bilingual format.
本文档基于张《航天器电磁兼容性技术》(2020)第10章第334–410页编写，采用双语格式。
