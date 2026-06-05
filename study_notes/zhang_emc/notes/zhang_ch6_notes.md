# Chapter 6: EMC Design and Implementation of General Electronic Equipment

> **中英双语版**

*Source: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Chapter 6, pp. 155-211*
*来源：张《航天器电磁兼容性技术》(2020)，第6章，第155–211页*

---

## 6.1 Spacecraft Equipment-Level EMC Standards and Specifications | 设备级EMC标准与规范

**From the source / 来源原文：** *"The spacecraft equipment-level EMC standards include MIL-STD-461G-2015, MSFC-SPEC-521C-2013, GSFC-STD-7000A-2013, ECSS-E-20-07C-2012, AIAA-S-121A-2017, SMC-S-008-2008, ISO-14302-2002."*
*"航天器设备级EMC标准包括 MIL-STD-461G-2015、MSFC-SPEC-521C-2013、GSFC-STD-7000A-2013、ECSS-E-20-07C-2012、AIAA-S-121A-2017、SMC-S-008-2008、ISO-14302-2002。"*

### MIL-STD-461G as Reference Baseline / 以MIL-STD-461G为基准

**From the source / 来源原文：** *"Due to the main role of MIL-STD-461G in equipment-level EMC requirements, it is taken as the reference baseline standard for other standards and specifications to be compared with."*
*"由于MIL-STD-461G在设备级EMC要求中的主导地位，将其作为基准标准，供其他标准规范参照对比。"*

**Key test items in MIL-STD-461G / MIL-STD-461G关键测试项：**

| Test / 测试项 | Description / 描述 | Frequency Range / 频率范围 |
|------|-------------|----------------|
| **CE101** | Conducted emissions, 30 Hz - 10 kHz / 传导发射，30 Hz–10 kHz | Power leads / 电源引线 |
| **CE102** | Conducted emissions, 10 kHz - 10 MHz / 传导发射，10 kHz–10 MHz | Power leads / 电源引线 |
| **CE106** | Conducted emissions, 10 kHz - 40 GHz / 传导发射，10 kHz–40 GHz | Antenna terminal / 天线端子 |
| **RE101** | Radiated emissions, 30 Hz - 100 kHz / 辐射发射，30 Hz–100 kHz | Magnetic field / 磁场 |
| **RE102** | Radiated emissions, 10 kHz - 18 GHz / 辐射发射，10 kHz–18 GHz | Electric field / 电场 |
| **CS101** | Conducted susceptibility, 30 Hz - 150 kHz / 传导敏感度，30 Hz–150 kHz | Power leads / 电源引线 |
| **CS103** | Conducted susceptibility, 10 kHz - 1 GHz / 传导敏感度，10 kHz–1 GHz | Antenna terminal / 天线端子 |
| **CS114** | Conducted susceptibility, 10 kHz - 200 MHz / 传导敏感度，10 kHz–200 MHz | Bulk cable injection / 电缆束注入 |
| **CS115** | Conducted susceptibility, impulse excitation / 传导敏感度，脉冲激励 | Bulk cable injection / 电缆束注入 |
| **CS116** | Conducted susceptibility, damped sine wave transients / 传导敏感度，阻尼正弦瞬态 | Power leads / 电源引线 |
| **RS101** | Radiated susceptibility, 30 Hz - 100 kHz / 辐射敏感度，30 Hz–100 kHz | Magnetic field / 磁场 |
| **RS103** | Radiated susceptibility, 10 kHz - 18 GHz / 辐射敏感度，10 kHz–18 GHz | Electric field / 电场 |

**Two newly added test items (from source) / 新增的两项测试：**
- **CS117:** Lightning effect (system-level E3 requirements) / 雷电效应（系统级E3要求）
- **CS118:** Human body electrostatic effect (ESD protection) / 人体静电效应（ESD防护）

### Special Requirements from Other Standards / 其他标准的特殊要求

**MSFC-SPEC-521C:**
- **CE108:** Bundled cable CE from 150 kHz to 200 MHz (similar to CS114) / 电缆束传导发射，150 kHz–200 MHz（类似于CS114）
- **CS109:** Structure current CS of 60 Hz - 100 kHz for equipment with operating frequency < 100 kHz / 结构电流传导敏感度，60 Hz–100 kHz，适用于工作频率<100 kHz的设备

**GSFC-STD-7000A:**
- Power and signal lines common-mode CE (150 kHz - 200 MHz) / 电源线和信号线共模传导发射（150 kHz–200 MHz）
- Start-up transient CE for power-on conditions / 开机瞬态传导发射

---

## 6.2 General EMC Design Requirements for Equipment | 设备通用EMC设计要求

**From the source / 来源原文：** *"The general EMC design requirements for spacecraft equipment include bonding, shielding, filtering, cable layout, and component selection."*
*"航天器设备的通用EMC设计要求包括接地搭接、屏蔽、滤波、电缆布局和元器件选择。"*

### 6.2.1 Bonding Requirements / 搭接要求

**From the source / 来源原文：** *"The electrical bonding of spacecraft structures and equipment are classified into Class C, H, R, and S."*
*"航天器结构和设备的电气搭接分为C、H、R、S四类。"*

**Key bonding requirements / 关键搭接要求：**

| Requirement / 要求 | Value / 值 | Application / 应用 |
|-------------|-------|-------------|
| Class C (Current Return) / C类（电流回路） | < 0.1 mΩ | Power current return path / 电源电流回路 |
| Class H (Fault Protection) / H类（故障防护） | < 2.5 mΩ, low inductance / 低电感 | Personnel safety, fire prevention / 人员安全、防火 |
| Class R (RF/EMI Suppression) / R类（射频/EMI抑制） | < 1.0 mΩ | RF equipment, EMI control / 射频设备、EMI控制 |
| Class S (ESD Control) / S类（静电控制） | — | Electrostatic charge control / 静电荷控制 |

**From the source / 来源原文：** *"The DC resistance between the equipment bonding stud and the nearby spacecraft structure shall be less than 2.5 mΩ."*
*"设备搭接螺柱与附近航天器结构之间的直流电阻应小于2.5 mΩ。"*

### 6.2.2 Shielding Requirements / 屏蔽要求

**From the source / 来源原文：** *"The spacecraft should be structured as a 'Faraday cage' and consider apertures used for pressure drop during ascent and for outgassing."*
*"航天器应构建为'法拉第笼'结构，并考虑发射上升段压降和排气所需的孔缝。"*

**Shielding effectiveness targets / 屏蔽效能目标：**
- General enclosure / 通用机箱：> 60 dB
- High-sensitivity equipment / 高灵敏度设备：> 80 dB
- Critical RF systems / 关键射频系统：> 100 dB

### 6.2.3 Filtering Requirements / 滤波要求

**Filter design principles from the source / 来源给出的滤波器设计原则：**
- Filter insertion loss should provide sufficient attenuation for conducted emissions / 滤波器插入损耗应能充分衰减传导发射
- Filters should not degrade signal integrity for sensitive circuits / 滤波器不应降低敏感电路的信号完整性
- Feedthrough capacitors for RF penetration points / 射频穿入点使用穿心电容

### 6.2.4 Cable Layout / 电缆布局

**From the source / 来源原文：** *"The cables shall be bunched according to the requirements of classification. Similar cables can be integrated into the same bundle. If different cables are routed on parallel paths, they shall be separated by 5 cm or by a metal screen."*
*"电缆应按分类要求进行成束。同类电缆可集成在同一线束中。若不同电缆并行布线，应间隔5 cm或在其间加装金属屏蔽。"*

**Cable classification and routing / 电缆分类与布线：**
| Cable Type / 电缆类型 | Separation Requirement / 间距要求 |
|-----------|----------------------|
| Power (high current) / 电源（大电流） | Isolated from signal cables / 与信号电缆隔离 |
| RF/analog / 射频/模拟 | Shielded, separated from digital / 屏蔽，与数字电缆隔离 |
| Low-level signal / 低电平信号 | Maximum separation from interference sources / 与干扰源最大限度隔离 |

---

## 6.3 General EMC Analysis, Design and Implementation | 通用EMC分析、设计与实现

**From the source / 来源原文：** *"The EMC design process should be integrated into the overall equipment design cycle from the early stages."*
*"EMC设计流程应从早期阶段就融入整体设备设计周期。"*

### 6.3.1 EMC Design Process / EMC设计流程

**Design flow from the source / 来源给出的设计流程：**
1. Define equipment EMC requirements / 确定设备EMC要求
2. Perform preliminary EMC analysis / 进行初步EMC分析
3. Implement EMC control measures / 实施EMC控制措施
4. Verify through analysis and test / 通过分析与测试验证
5. Document and maintain traceability / 记录并保持可追溯性

### 6.3.2 PCB-Level EMC Design / PCB级EMC设计

**From the source / 来源原文：** *"PCB-level EMC design considers RF characteristics of traces, ground plane integrity, and component placement."*
*"PCB级EMC设计需考虑走线的射频特性、地平面完整性和元器件布局。"*

**PCB EMC guidelines / PCB EMC设计指南：**
| Aspect / 方面 | Guideline / 准则 | Rationale / 原理 |
|--------|----------|-----------|
| Ground plane / 地平面 | Solid, continuous / 实心连续 | Minimize return path impedance / 最小化回流通路阻抗 |
| Trace routing / 走线 | Short, direct / 短而直接 | Reduce radiation/pickup / 减小辐射/拾取 |
| Decoupling / 去耦 | Multiple capacitor values / 多值电容 | Broadband decoupling / 宽带去耦 |
| Clock routing / 时钟走线 | Guard traces / 防护走线 | Reduce crosstalk / 减小串扰 |
| Via stitching / 过孔缝合 | Ground vias adjacent to signal vias / 信号过孔旁接地点过孔 | Ground continuity / 地连续性 |

### 6.3.3 Component Selection / 元器件选择

**EMC considerations in component selection / 元器件选择的EMC考量：**
- Switching speed of digital devices (faster = more emissions) / 数字器件的开关速度（越快 → 发射越大）
- Output drive strength (minimal adequate) / 输出驱动强度（取最低足够值）
- Input filtering (ESD protection diodes) / 输入滤波（ESD防护二极管）
- Shielded enclosures for oscillators, clocks / 振荡器、时钟的屏蔽罩

### 6.3.4 EMC Test and Verification / EMC测试与验证

**Equipment-level verification methods from the source / 来源给出的设备级验证方法：**
1. Analysis / 分析：Theoretical calculations, simulation / 理论计算、仿真
2. Unit testing / 单机测试：Individual equipment EMC characterization / 单机设备EMC特性表征
3. Subsystem integration testing / 分系统集成测试
4. System-level verification / 系统级验证

**Documentation requirements / 文档要求：**
- EMC analysis reports / EMC分析报告
- Test plans and procedures / 测试计划与程序
- Test results and compliance statements / 测试结果与符合性声明
- As-built configuration records / 实际硬件配置记录

---

## Key Physical Parameters Summary / 关键物理参数汇总

| Parameter / 参数 | Symbol / 符号 | Typical Value/Range / 典型值/范围 |
|-----------|--------|-------------------|
| Bonding resistance (Class C) / 搭接电阻（C类） | $R_b$ | < 0.1 mΩ |
| Bonding resistance (Class H) / 搭接电阻（H类） | $R_b$ | < 2.5 mΩ |
| Bonding resistance (Class R) / 搭接电阻（R类） | $R_b$ | < 1.0 mΩ |
| Shielding effectiveness / 屏蔽效能 | $SE$ | > 60 dB |
| Cable separation / 电缆间距 | $d$ | > 5 cm (unshielded / 非屏蔽) |
| EMI margin / EMI裕度 | $M$ | > 6 dB |
| EED safety margin / 电爆装置安全裕度 | $M_{\text{EED}}$ | > 20 dB |

---

**Note / 注：** This notes is based on Chapter 6 of Zhang, *Spacecraft Electromagnetic Compatibility Technologies* (2020), pp. 155-211. All content from original source text. Bilingual format.
本文档基于张《航天器电磁兼容性技术》(2020)第6章第155–211页编写，内容均来自原文，采用双语格式。
