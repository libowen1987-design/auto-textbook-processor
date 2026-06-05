# Zhang《Spacecraft EMC Technologies》第2章：EMC基础与EMI控制方法

> **Source:** H. Zhang et al., *Spacecraft Electromagnetic Compatibility Technologies*, Springer 2020  
> **章节来源:** Chapter 2: Basic Knowledge of EMC and Methods of EMI Control, pp.36-62  
> **提取方式:** ✅ 清晰英文PDF直接提取

---

## 2. EMC基础与EMI控制方法 | Basic Knowledge of EMC and Methods of EMI Control

### 2.1 EMC基本概念 | Basic EMC Concepts

#### 2.1.1.1 EMC的定义与重要性 | Definition and Importance of EMC

**电磁兼容性（EMC）** 指设备或系统在电磁环境中能够正常工作，且不会对其他设备产生不可接受的电磁干扰的能力。

**EMC三要素：**
- **干扰源（Sources of Interference）**：产生电磁干扰的源头
- **耦合路径（Coupling Paths）**：干扰能量从源到敏感设备的传播通道
- **敏感设备（Susceptible Equipment）**：受到干扰影响的设备

#### 2.1.1.2 EMC Margin 与抗扰度等级 | EMC Margin and Immunity Test Levels

EMC设计的核心是确保**干扰裕量（EMC Margin）** 足够大：

$$\text{EMC Margin} = \text{敏感度门限（Susceptibility Level）} - \text{干扰电平（Emission Level）}$$

干扰裕量必须为正值，且越大越好。

**抗扰度测试等级（Immunity Test Levels）：**

| 等级 | 定义 | 要求 |
|------|------|------|
| **Survival Level（存活级）** | EUT在指定EMI环境下无永久性性能下降 | 最基本要求 |
| **Working Level（工作级）** | EUT在指定EMI环境下不发生故障、功能失效或状态改变 | 正常工作 |
| **Performance Level（性能级）** | EUT在指定EMI环境下可靠完成工程任务 | 最高要求 |

---

### 2.2 数字电路周期信号频谱 | Periodic Signal Spectrum of Digital Circuits

数字电路（如时钟、晶体振荡器）产生周期信号，其谐波含量对EMC分析至关重要。

#### 周期信号的谐波幅度 | Harmonic Amplitude of Periodic Signals

设信号参数：$t_{pw} = T_p/2$（占空比50%），上升时间等于下降时间 $t_r$。

**第 $n$ 次谐波的电压幅度：**

$$V_n = V_0 \cdot \frac{\sin(\pi n f_0 t_{pw})}{\pi n f_0 t_{pw}} \cdot \frac{\sin(\pi n f_0 t_r)}{\pi n f_0 t_r} \tag{2.1.1}$$

其中：
- $V_n$：第 $n$ 次谐波的电压幅度（V）
- $V_0$：信号电压幅度（V）
- $f_0 = 1/T_p$：信号基频（Hz）
- $t_r$：信号上升时间（s）
- $t_{pw}$：信号脉冲宽度（s）

**物理意义：** 当 $\pi n f_0 t_r \approx 0$（上升时间很短）时，$\sin(x)/x \approx 1$，谐波幅度主要由第一项决定。

**频谱包络特性：**

对于宽脉冲（$t_{pw} \approx T_p/2$）信号：
$$|V_n| \approx \frac{2V_0}{\pi} \cdot \frac{1}{|n|} \quad \text{（远低于转折频率）}$$

转折频率（Corner frequency）：
$$f_c = \frac{1}{\pi t_r}$$

---

### 2.3 传导干扰（CE）分析 | Conducted Emission (CE) Analysis

#### 2.3.1 共模与差模干扰 | Common-Mode and Differential-Mode Interference

传导干扰分为**共模（Common-Mode, CM）**和**差模（Differential-Mode, DM）**两种：

**差模干扰：** 在信号线与回线之间流动，遵循 Kirchhoff 定律。

$$I_{DM} = \frac{V_{DM}}{Z_{source} + Z_{load}}$$

**共模干扰：** 在所有导体与地之间同向流动，由不平衡电压驱动。

$$I_{CM} = \frac{V_{CM}}{Z_{CM,source} + Z_{CM,load}}$$

**CM/DM 分离的重要性：** 共模和差模干扰需要不同的抑制技术。共模扼流圈（CM choke）利用 CM 阻抗大、DM 阻抗小的特性实现分离。

#### 2.3.2 电源线传导发射模型 | Power Line Conducted Emission Model

**LISN（线路阻抗稳定网络）** 是传导发射测量的标准接口：

$$Z_{LISN}(f) = 50\,\Omega \parallel \frac{1}{j\omega C_{LISN}} \parallel j\omega L_{LISN}$$

MIL-STD-461 规定的 $50\,$\mu$\text{H}$ LISN 阻抗在 10kHz–30MHz 范围内接近 $50\,\Omega$。

**传导发射极限（MIL-STD-461 CE101）：**

$$P_{CE}(f) \leq P_{limit}(f) - 10\log_{10}(Z_{LISN}) \quad \text{(dBµV)}$$

---

### 2.4 辐射干扰（RE）分析 | Radiated Emission (RE) Analysis

#### 2.4.1 近场与远场 | Near-Field and Far-Field

电磁辐射在近场和远场的行为完全不同：

**远场条件：** $r \gg \lambda / 2\pi$

在远场，电场和磁场相互垂直并满足平面波关系：

$$|\mathbf{E}| = |\mathbf{H}| \cdot Z_0 = |\mathbf{H}| \cdot 377\,\Omega$$

**近场（电偶极子为主）：**
$$E_r \approx \frac{k p \cos\theta}{2\pi \varepsilon_0 r^3}, \quad E_\theta \approx \frac{k^2 p \sin\theta}{4\pi \varepsilon_0 r}$$

其中 $p = q \cdot l$ 是电偶极矩，$k = 2$\pi$/\lambda$。

#### 2.4.2 辐射发射极限 | Radiated Emission Limits

**FCC Part 15B Class B（30cm测量距离）：**

$$E_{RE}(f) \leq \begin{cases} 40 \, \text{dBµV/m} & 30\,\text{MHz} \leq f < 230\,\text{MHz} \\ 47 \, \text{dBµV/m} & 230\,\text{MHz} \leq f \leq 1\,\text{GHz} \end{cases}$$

---

### 2.5 EMI控制方法 | EMI Control Methods

#### 2.5.1 接地（Grounding）| Grounding

接地是EMI控制的基础，可分为：

| 类型 | 定义 | 适用场景 |
|------|------|---------|
| **单点接地** | 所有接地连接到同一点 | 低频（<1MHz）|
| **多点接地** | 各点就近接地 | 高频（>10MHz）|
| **混合接地** | 低频单点，高频多点 | 宽带系统 |

**接地阻抗频率特性：**

$$Z_{ground}(f) = R + j\omega L_{ground}$$

在高频，接地引线的感抗主导，导致公共阻抗耦合。

#### 2.5.2 屏蔽（Shielding）| Shielding

屏蔽的有效性用**屏蔽效能（Shielding Effectiveness, SE）**衡量：

$$\text{SE (dB)} = 20\log_{10}\left|\frac{E_{incident}}{E_{transmitted}}\right|$$

SE 由吸收损耗、反射损耗和多次反射修正组成：

$$\text{SE} = R + A + B \quad \text{(dB)}$$

**吸收损耗：**
$$A (\text{dB}) = 8.69\,t\sqrt{\pi f \mu \sigma}$$

其中 $t$ 为屏蔽厚度，$\mu$ 为磁导率，$\sigma$ 为电导率。

**皮肤深度（Skin Depth）：**
$$\delta = \sqrt{\frac{2}{\omega \mu \sigma}} = \frac{1}{\sqrt{\pi f \mu \sigma}}$$

铜在 1GHz 下的皮肤深度：$\delta_{Cu} \approx 2.1\,$\mu$\text{m}$

#### 2.5.3 滤波（Filtering）| Filtering

滤波器抑制高频干扰能量：

**典型 EMI 滤波器拓扑：**

- **\pi 型滤波器**：$L - C - L$ 结构，提供高阻抗失配
- **T 型滤波器**：$C - L - C$ 结构，提供低阻抗失配
- **共模扼流圈**：对共模信号提供高阻抗，对差模信号透明

**插入损耗（Insertion Loss）：**
$$\text{IL} = 20\log_{10}\left|\frac{V_{without\_filter}}{V_{with\_filter}}\right| \quad \text{(dB)}$$

**宽频带 EMI 滤波器的频率响应：**
$$\text{IL}(f) \approx 10\log_{10}\left[1 + \left(\frac{f}{f_c}\right)^{2n}\right] \quad \text{(dB)}$$

其中 $f_c$ 为截止频率，$n$ 为滤波器阶数。

---

### 2.6 EMC预测分析方法 | EMC Prediction and Analysis Methods

#### 2.6.1 干扰余量计算 | Interference Margin Calculation

$$\text{Interference Margin (dB)} = \text{Received Interference (dBµV)} - \text{Susceptibility Level (dBµV)}$$

如果余量为负，说明存在干扰问题。

#### 2.6.2 传输线耦合模型 | Transmission Line Coupling Model

两根平行传输线之间的**容性耦合（电容耦合）**电流：

$$I_C = C_{12} \cdot \frac{dV_1}{dt} \cdot l$$

其中 $C_{12}$ 为单位长度耦合电容，$l$ 为耦合长度。

**感性耦合（电感耦合）**电压：
$$V_L = M \cdot \frac{dI_1}{dt}$$

其中 $M$ 为互感，$M = k\sqrt{L_1 L_2}$，$k$ 为耦合系数（$0 \leq k \leq 1$）。

**总耦合电压（在负载端）：**
$$V_{coupled} \approx \frac{j\omega C_{12} l Z_L}{1 + j\omega C_{12} l Z_L} \cdot V_1 \cdot l \cdot \frac{M}{L_1}$$

---

### 2.7 本章要点 | Key Takeaways

1. **EMC 三要素**：干扰源 → 耦合路径 → 敏感设备，三者缺一不可
2. **EMC Margin** = 敏感度门限 − 干扰电平，必须为正值
3. **数字电路频谱**：谐波幅度 $\propto 1/n$，转折频率 $f_c = 1/(\pi t_r)$
4. **皮肤深度**：$\delta = \sqrt{2/($\omega$$\mu$$\sigma$)}$，高频屏蔽设计关键参数
5. **共模/差模分离**：CM choke 是区分两者的高效器件
6. **传输线耦合**：容性耦合 $\propto C_{12}\omega$，感性耦合 $\propto M\omega$

---

### 2.8 参考文献与标准 | References and Standards

| 标准 | 名称 | 关键指标 |
|------|------|---------|
| MIL-STD-461 | 电磁干扰控制要求 | CE101/102/103, RE101/102 |
| FCC Part 15B | 消费电子辐射发射 | 30MHz–1GHz, Class B |
| IEC 61000-4-2 | 静电放电（ESD）抗扰度 | \pm8kV 接触放电 |
| CISPR 22 | 信息技术设备辐射发射 | Class B limits |