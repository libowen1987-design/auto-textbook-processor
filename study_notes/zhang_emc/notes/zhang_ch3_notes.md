# Chapter 3: Electromagnetic Compatibility Management | 第3章：电磁兼容性管理

> **中英双语版**

*Source: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Chapter 3, pp. 63-79*
*来源：张《航天器电磁兼容性技术》(2020)，第3章，第63–79页*

---

## 3.1 Overview of EMC Management Standards | EMC管理标准概述

**Main spacecraft EMC management standards and manuals from the source / 主要航天器EMC管理标准与手册：**

| Standard / 标准 | Organization / 组织 | Content / 内容 |
|----------|--------------|---------|
| DEF-STAN 59-411 Part 1-2014 | UK Defense Standards / 英国国防标准 | EMC Management and Planning / EMC管理与规划 |
| MIL-HDBK-237D-2005 | US DoD / 美国国防部 | Electromagnetic Environmental Effects Management / 电磁环境效应管理 |
| GJB/Z 170-2018 | China / 中国 | Design Process for Spacecraft EMC Risk Management / 航天器EMC风险管理设计流程 |

**Core standard systems by region / 各区域核心标准体系：**

| Region / 区域 | Primary Standards / 主要标准 |
|--------|-------------------|
| **Europe / 欧洲** | ECSS-E-ST-20-07C, ECSS-E-HB-20-07A |
| **USA / 美国** | MIL-STD-464C, MIL-HDBK-237D |
| **UK / 英国** | DEF-STAN 59-411 |
| **China / 中国** | GJB/Z 170, GJB 151B |

---

## 3.2 The Spacecraft EMC Management | 航天器EMC管理

### 3.2.1 Main EMC Management Activities (Based on DEF STAN 59-411) / 主要EMC管理活动（基于DEF STAN 59-411）

**Key EMC management activities from the source / 来源给出的关键EMC管理活动：**
1. EMC management planning / EMC管理规划
2. EMC design and analysis / EMC设计与分析
3. EMC verification and testing / EMC验证与测试
4. EMC documentation and traceability / EMC文档与可追溯性

### 3.2.2 EMC Risk Management / EMC风险管理

**From the source / 来源原文：** *"The EMC risk management design process should identify potential EMC problems early in the development phase, evaluate their impact on system performance, and implement mitigation measures before they become critical."*
*"EMC风险管理设计流程应在开发阶段早期识别潜在的EMC问题，评估其对系统性能的影响，并在问题变得严重之前实施缓解措施。"*

**Risk assessment matrix / 航天器EMC风险矩阵：**
| Risk Level / 风险等级 | Criteria / 判据 | Action / 措施 |
|------------|----------|--------|
| **Critical / 致命** | EMI margin < 0 dB, no mitigation possible / EMI裕度<0 dB，无法缓解 | Redesign required / 需重新设计 |
| **High / 高** | EMI margin 0-6 dB, mitigation possible / EMI裕度0-6 dB，可缓解 | Detailed analysis + testing / 详细分析+测试 |
| **Medium / 中** | EMI margin 6-20 dB / EMI裕度6-20 dB | Standard controls sufficient / 标准控制即可 |
| **Low / 低** | EMI margin > 20 dB / EMI裕度>20 dB | Routine verification / 常规验证 |

---

## 3.3 EMC Working Group | EMC工作组

### 3.3.1 Responsibilities of the EMC Working Group / EMC工作组职责

**From the source / 来源原文：** *"The EMC Working Group is responsible for coordinating EMC activities across all subsystems, ensuring compliance with EMC requirements, and managing EMC risk throughout the project lifecycle."*
*"EMC工作组负责协调所有子系统的EMC活动，确保符合EMC要求，并在项目全生命周期内管理EMC风险。"*

### 3.3.2 Tasks of the EMC Working Group / EMC工作组任务

**Main tasks / 主要任务：**
1. Review and approve EMC control plans / 审查并批准EMC控制计划
2. Coordinate EMC testing activities / 协调EMC测试活动
3. Resolve EMC non-conformances / 解决EMC不符合项
4. Maintain EMC risk register / 维护EMC风险登记册
5. Provide EMC training and guidance / 提供EMC培训与指导

### 3.3.3 System-Level and Equipment-Level EMC Personnel / 系统级与设备级EMC人员

| Role / 角色 | Responsibility / 职责 |
|------|--------------|
| **System-Level EMC Supervisor / 系统级EMC主管** | Overall system EMC compliance, interface control / 整体系统EMC合规、接口控制 |
| **Equipment-Level EMC Designer / 设备级EMC设计师** | Individual equipment EMC design and verification / 单机设备EMC设计与验证 |

---

## 3.4 EMC Control Program and Technical Requirements | EMC控制程序与技术要求

### 3.4.1 EMC Control Plan Structure / EMC控制计划结构

**From the source / 来源原文：** *"The EMC control program should include the following elements: EMC requirements document, EMC control plan, EMC analysis reports, EMC test plans and results, EMC verification reports."*
*"EMC控制程序应包括以下要素：EMC要求文件、EMC控制计划、EMC分析报告、EMC测试计划与结果、EMC验证报告。"*

### 3.4.2 Technical Requirements Flow-Down / 技术要求逐级分解

**Requirements flow-down hierarchy / 要求分解层级：**
```
Mission-Level EMC Requirements / 任务级EMC要求
    ↓
System-Level EMC Requirements / 系统级EMC要求
    ↓
Subsystem-Level EMC Requirements / 分系统级EMC要求
    ↓
Equipment-Level EMC Requirements / 设备级EMC要求
```

**Flow-down principles from the source / 来源给出的分解原则：**
- Requirements should be traceable from top-level mission objectives to individual equipment specifications / 要求应从顶层任务目标逐级追溯到单机设备规范
- Each level should add margin to protect against accumulated uncertainties / 每一级应增加裕度以应对累积的不确定性
- Verification methods should be specified at each level / 每一级应指定验证方法

### 3.4.3 Verification and Compliance / 验证与合规

**Verification methods / 验证方法：**
1. **Analysis / 分析：** Theoretical analysis, simulation, calculation / 理论分析、仿真、计算
2. **Test / 测试：** Ground testing, flight testing / 地面测试、飞行测试
3. **Inspection / 检查：** Design review, physical inspection / 设计评审、实物检查

**Compliance verification levels / 合规验证层级：**
- Unit level (single equipment) / 单元级（单机设备）
- Subsystem level (multiple equipment integration) / 分系统级（多设备集成）
- System level (full spacecraft) / 系统级（整星）

---

**Note / 注：** This notes is based on Chapter 3 of Zhang, *Spacecraft Electromagnetic Compatibility Technologies* (2020), pp. 63-79. Bilingual format, physical quantities explained with reference to source text.
本文档基于张《航天器电磁兼容性技术》(2020)第3章第63–79页编写，采用双语格式，物理量参考原文标注。
