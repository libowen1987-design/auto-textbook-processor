# Sadiku《Elements of Electromagnetics》Chapter 14: Electromagnetic Compatibility (EMC)
> **中英双语版**

## 14.1 Introduction / 引言
EMC ensures electronic systems operate without interference in their electromagnetic environment.
> EMC 确保电子系统在其电磁环境中无干扰地工作。

## 14.2 EMI Sources / 电磁干扰源
- **Natural / 自然**: Lightning ($10^4$-A pulses, 1-100 MHz), electrostatic discharge (ESD / 静电放电)
- **Man-made / 人为**: Digital clocks, switching power supplies, motors, transmitters

## 14.3 Coupling Mechanisms / 耦合机制
- **Conducted coupling / 传导耦合**: Through power/signal cables, common impedance
- **Radiated coupling / 辐射耦合**: Near-field (capacitive/inductive), far-field (plane wave)

## 14.4 Shielding / 屏蔽
**Shielding effectiveness / 屏蔽效能:**
$$\text{SE (dB)} = R + A + M$$
$R$: reflection loss / 反射损耗, $A$: absorption loss / 吸收损耗, $M$: multiple reflection correction.

For a plane wave incident on a metal shield of thickness $t$:
$$A = 131.4 t\sqrt{f\mu_r\sigma_r} \quad \text{[dB]}, \quad R = 168 - 10\log_{10}(f\mu_r/\sigma_r) \quad \text{[dB]}$$

**Skin depth / 趋肤深度:** $\delta = 1/\sqrt{\pi f\mu\sigma}$. Shield must be $> 3\delta$ for effective shielding.

## 14.5 Grounding / 接地
- Single-point ground / 单点接地 (low frequency)
- Multi-point ground / 多点接地 (high frequency)
- Ground loops / 地环路: eliminate by isolating grounds / 通过隔离接地消除

## 14.6 Filtering / 滤波
- EMI filters combine series inductors and shunt capacitors
- Ferrite beads / 铁氧体磁珠 for high-frequency suppression ($> 10$ MHz)

## 14.7 EMC Standards / EMC 标准
- **FCC Part 15** (USA): Class A (commercial) and Class B (residential) emission limits
- **CISPR** (International): Radiated and conducted emission limits
- **IEC 61000**: Immunity and susceptibility standards

## 14.8 EMC Design Guidelines / EMC 设计指南
1. Minimize loop areas of high-speed signals / 最小化高速信号回路面积
2. Use ground planes (not traces) for return currents / 使用地平面而非走线作为回流路径
3. Decouple power supplies near ICs / 在 IC 附近去耦电源
4. Separate analog/digital and high/low frequency sections / 分离模拟/数字和高/低频部分
5. Use twisted pairs or shielded cables / 使用双绞线或屏蔽电缆
6. Proper termination to avoid reflections / 适当端接避免反射
