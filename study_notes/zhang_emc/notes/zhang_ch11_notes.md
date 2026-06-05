# Chapter 11: Spacecraft System-Level EMC Test Verification

> **中英双语版**

*Source: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Chapter 11, pp. 411-470*
*来源：张《航天器电磁兼容性技术》(2020)，第11章，第411–470页*

---

## 11.1 Electromagnetic Environmental Effect (E3) Test | 电磁环境效应(E3)测试

### 11.1.1 Test Requirements | 测试要求

**From the source / 来源原文：** *"The system electromagnetic environment effect (E3) requirements are based on the general development requirements or specifications in the contract, which include the test content and specific test items. The E3 test shall be carried out according to the test program."*
*"系统电磁环境效应(E3)要求基于合同中的总体研制要求或规范，包括测试内容和具体测试项目。E3测试应按测试大纲执行。"*

**E3 test categories (from source) / E3测试类别（来源原文）：**
| Category / 类别 | Content / 内容 | Applicable Standard / 适用标准 |
|---------|---------|-------------------|
| Radiated emissions / 辐射发射 | RE102, RE103 | MIL-STD-461G |
| Radiated susceptibility / 辐射敏感度 | RS101, RS103 | MIL-STD-461G |
| Conducted emissions / 传导发射 | CE101, CE102 | MIL-STD-461G |
| Conducted susceptibility / 传导敏感度 | CS101, CS114, CS115, CS116 | MIL-STD-461G |
| Lightning / 雷电 | CS117 | MIL-STD-464C |
| ESD / 静电放电 | CS118 | MIL-STD-464C |

### 11.1.2 System-Level Verification / 系统级验证

**From the source / 来源原文：** *"System-level EMC verification confirms that all subsystems and equipment function correctly together under the specified electromagnetic environment."*
*"系统级EMC验证确认所有分系统和设备在规定的电磁环境下能协同正常工作。"*

**Verification levels / 验证层级：**
1. **Unit level / 单元级：** Individual equipment testing / 单机设备测试
2. **Subsystem level / 分系统级：** Integration testing of multiple units / 多单元集成测试
3. **System level / 系统级：** Full spacecraft EMC characterization / 整星EMC特性表征

---

## 11.2 Intrasystem EMC Analysis | 系统内EMC分析

**From the source / 来源原文：** *"Intrasystem EMC analysis evaluates the electromagnetic compatibility between spacecraft subsystems and equipment operating simultaneously."*
*"系统内EMC分析评估航天器各分系统及同时运行的设备之间的电磁兼容性。"*

**Analysis scope / 分析范围：**
- Transmitter-receiver isolation / 发射机-接收机隔离
- Digital clock interference with RF circuits / 数字时钟对射频电路的干扰
- Power bus noise coupling to sensitive circuits / 电源母线噪声耦合至敏感电路

---

## 11.3 Lightning and EMP Testing | 雷电与电磁脉冲测试

**From the source / 来源原文：** *"Lightning and electromagnetic pulse (EMP) tests verify the spacecraft's ability to withstand high-intensity electromagnetic environments."*
*"雷电和电磁脉冲(EMP)测试验证航天器耐受高强度电磁环境的能力。"*

**CS117 lightning test requirements (from source) / CS117雷电测试要求（来源原文）：**
- Current waveform: damped sinusoid / 电流波形：阻尼正弦波
- Peak current: up to 1000 A / 峰值电流：高达1000 A
- Duration: varies by test level / 持续时间：按测试等级变化

---

## 11.4 Test Documentation and Compliance | 测试文档与符合性

**From the source / 来源原文：** *"All EMC test results must be documented and reviewed against the applicable requirements to determine compliance."*
*"所有EMC测试结果必须记录在案，并对照适用要求进行审查以确定符合性。"*

**Required documentation / 所需文档：**
- Test procedures and setup photos / 测试程序与布置照片
- Raw measurement data / 原始测量数据
- Data reduction calculations / 数据处理计算
- Pass/fail determination with margin / 通过/失效判定及裕度
- Non-conformance reports (if applicable) / 不符合项报告（如适用）

---

**Note / 注：** This notes is based on Chapter 11 of Zhang, *Spacecraft Electromagnetic Compatibility Technologies* (2020), pp. 411-470. Bilingual format.
本文档基于张《航天器电磁兼容性技术》(2020)第11章第411–470页编写，采用双语格式。
