---
title: "Chapter 12 — S-Parameters"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 12
pages: "584–642"
---

# Ch12: S-Parameters

> **中英双语版**

## 12.1 What Are S-Parameters? | 什么是 S 参数？

**Scattering parameters (S-parameters):** Ratio of output sine wave to input sine wave at each frequency.
**散射参数（S 参数）：** 每个频率下输出正弦波与输入正弦波的比值。

- $S_{11}$: reflection from port 1 (input match) | 端口 1 反射（输入匹配）
- $S_{21}$: transmission from port 1 to port 2 (insertion loss) | 端口 1 到端口 2 传输（插入损耗）
- $S_{22}$: reflection from port 2 (output match) | 端口 2 反射（输出匹配）
- $S_{12}$: reverse transmission (isolation) | 反向传输（隔离度）

## 12.2 Key Relationships | 关键关系式

**Reflection coefficient from $S_{11}$ | 由 $S_{11}$ 得到反射系数：**
$$
S_{11} = \frac{Z_{\text{DUT}} - Z_0}{Z_{\text{DUT}} + Z_0}
$$

**Insertion loss (dB):** $\text{IL} = 20 \log_{10} |S_{21}|$
**插入损耗（dB）：** 衡量信号从端口 1 到端口 2 的能量损耗。

**Return loss (dB):** $\text{RL} = 20 \log_{10} |S_{11}|$
**回波损耗（dB）：** 衡量端口反射能量的大小。

## 12.3 Mixed-Mode S-Parameters (Differential) | 混合模式 S 参数（差分）

For differential pairs | 对于差分对：

| Parameter | Meaning | 中文含义 |
|:--|:--|:--|
| $S_{\text{dd11}}$ | Differential reflection | 差模反射 |
| $S_{\text{dd21}}$ | Differential transmission | 差模传输 |
| $S_{\text{cc21}}$ | Common-mode transmission | 共模传输 |
| $S_{\text{cd21}}$ | Mode conversion (diff → common) | 模式转换（差模→共模） |

## 12.4 Eye Diagram from S-Parameters | 由 S 参数得到眼图

S-parameters + PRBS (pseudo-random bit stream) → IFFT → time-domain eye diagram.
S 参数 + PRBS（伪随机比特流）→ IFFT（逆傅里叶变换）→ 时域眼图。

**Eye diagram metrics | 眼图度量：**
- **Vertical eye opening:** noise margin（**垂直眼宽：** 噪声容限）
- **Horizontal eye opening:** jitter margin (unit interval — jitter)（**水平眼宽：** 抖动容限 = 码元周期 - 总抖动）
- **Bathtub curve:** BER vs. sampling phase（**浴盆曲线：** 误码率随采样相位的变化）

## 12.5 Key Design Guidelines | 关键设计准则

- $|S_{11}| < -15$ dB (return loss, good match | 回波损耗，良好匹配)
- $|S_{21}|$: smooth roll-off, no resonances（平滑滚降，无谐振尖峰）
- $S_{\text{cd21}}$ (mode conversion): keep as low as possible (bad → EMI)（模式转换：尽量低，否则引起 EMI）
- VNA is the instrument for S-parameter measurement (kHz to 50+ GHz)
  矢量网络分析仪是测量 S 参数的标准仪器（覆盖 kHz 到 50+ GHz）

> **Engineering Intuition:** S-parameters are the "universal language" of interconnects. Any interconnect's performance can be completely described by its S-parameters. They're becoming the industry standard for SI analysis.
> **工程直觉：** S 参数是互连的"通用语言"。任何互连的性能都可以通过其 S 参数完全描述，已成为 SI 分析的行业标准。

## 12.6 Key Formulas | 关键公式

| Formula | Description | 中文说明 |
|:--|:--|:--|
| $S_{11} = (Z_{\text{DUT}} - Z_0)/(Z_{\text{DUT}} + Z_0)$ | Reflection S-parameter | 反射 S 参数 |
| $\text{IL(dB)} = 20\log|S_{21}|$ | Insertion loss | 插入损耗 |
| $\text{RL(dB)} = 20\log|S_{11}|$ | Return loss | 回波损耗 |
| $V_{\text{refl}}/V_{\text{inc}} = S_{11}$ | Reflection coefficient | 反射系数 |
| $V_{\text{trans}}/V_{\text{inc}} = S_{21}$ | Transmission coefficient | 传输系数 |
