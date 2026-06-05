# Chapter 15: Asymptotic Waveform Evaluation for Broadband Calculations
# 第十五章：渐进波形评估（AWE）用于宽带计算

**Author 作者**: Dan Jiao and Jian-Ming Jin

## 15.1 引言 | Introduction

**应用背景**：许多电磁应用需要计算宽频带内的频率响应，而非仅在个别频率点：
- **雷达目标识别**：RCS 宽频带响应生成距离剖面和 SAR 图像
- **天线分析**：宽频带天线的输入阻抗（需在多个频率计算）
- **色散介质**：介电常数随频率变化的材料

**传统方法的瓶颈**：频域数值方法（如 MOM）需要在每个频率点**重复生成和求解**矩阵方程，当响应在频带内变化剧烈时计算代价极高。

**AWE 的核心思想**：将频域响应展开为**有理函数**（Padé 近似），只需在少量频率点求解，即可推算整个频带的响应。

---

## 15.2 AWE 方法 | The AWE Method

### 15.2.1 问题陈述

数值分析产生的矩阵方程：

$$[Z(k)] \{I(k)\} = \{V(k)\} \tag{15.1}$$

其中 $k = \omega/c$ 是波数，$[Z(k)]$ 阻抗矩阵，$\{V(k)\}$ 激励向量。

**传统方法**：每个频率点重复计算 $[Z(k)]$ 和求解线性方程组 → 计算密集型。

### 15.2.2 Taylor 级数展开

将 $\{I(k)\}$ 在展开点 $k_0$ 处展开为 Taylor 级数：

$$\{I(k)\} = \sum_{n=0}^{\infty} m_n (k - k_0)^n \tag{15.2}$$

**矩向量递归公式**（由系数匹配得到）：

$$m_0 = [Z(k_0)]^{-1} \{V(k_0)\} \tag{15.3}$$

$$m_n = [Z(k_0)]^{-1} \left\{ \frac{1}{n!} \frac{d^n \{V\}}{dk^n}\bigg|_{k_0} - \sum_{i=1}^{n} \frac{1}{i!} \frac{d^i [Z]}{dk^i}\bigg|_{k_0} m_{n-i} \right\} \tag{15.4}$$

关键：**$[Z(k_0)]$ 仅需求逆一次**，所有高阶导数可通过递归关系计算。

### 15.2.3 Padé 有理函数近似

Taylor 展开的收敛半径有限。为获得更宽频带的精度，用有理 Padé 函数逼近：

$$\{I(k)\} \approx \frac{\sum_{j=0}^{L} c_j (k - k_0)^j}{1 + \sum_{j=1}^{M} d_j (k - k_0)^j} \tag{15.5}$$

通过将 (15.2) 代入 (15.5) 并匹配 $(k-k_0)^n$ 的系数，得到矩阵方程：

$$\begin{bmatrix} c_0 \\ c_1 \\ \vdots \\ c_L \end{bmatrix} = \text{solve} \left( \begin{bmatrix} m_0 & m_0 & \cdots & m_0 \\ m_1 & m_0 & \cdots & m_0 \\ \vdots & \vdots & \ddots & \vdots \\ m_L & m_{L-1} & \cdots & m_0 \end{bmatrix} \begin{bmatrix} d_1 \\ d_2 \\ \vdots \\ d_M \end{bmatrix} = \begin{bmatrix} m_1 \\ m_2 \\ \vdots \\ m_{L+1} \end{bmatrix} \right) \tag{15.6}$$

### 15.2.4 复频率跳跃（CFH）技术

单个展开点无法覆盖整个频带。使用 **CFH 二分搜索算法** 自动选择多个展开点：

1. 在频带 $[k_{min}, k_{max}]$ 的中点 $k_0$ 应用 AWE
2. 在频带边界检查精度：$|I_{AWE}(k_{min}) - I_{AWE}(k_{max})| < \epsilon$
3. 若不满足，在子区间 $[k_{min}, k_0]$ 和 $[k_0, k_{max}]$ 分别递归应用
4. 直到整个频带达到精度要求

---

## 15.3 金属天线分析 | Analysis of Metallic Antennas

### 15.3.1 公式化

**积分方程**：使用 EFIE/MFIE 描述导体表面的电流：

$$\hat{n} \times \left[ \int_S [Z] \cdot \mathbf{J} \, dS' \right] = -\hat{n} \times \mathbf{E}^{inc} \tag{15.19}$$

**RWG 基函数展开**：

$$\mathbf{J}(\mathbf{r}) \approx \sum_{n=1}^{N} I_n \mathbf{f}_n(\mathbf{r}) \tag{15.10}$$

**矩阵元素**（需计算对 $k$ 的各阶导数）：

$$Z_{mn}(k) = \int_{T_m} \int_{T_n} \mathbf{f}_m(\mathbf{r}) \cdot [Z] \cdot \mathbf{f}_n(\mathbf{r}') \, dS' dS \tag{15.13}$$

导数公式：

$$\frac{d^i Z_{mn}}{dk^i} = \int_{T_m} \int_{T_n} \mathbf{f}_m(\mathbf{r}) \cdot \frac{d^i [Z]}{dk^i} \cdot \mathbf{f}_n(\mathbf{r}') \, dS' dS \tag{15.18}$$

### 15.3.2 数值算例：MRI 射频线圈

**低通鸟笼线圈（Birdcage Coil）**：
- 直径 26 cm，12 根辐条，每根辐条中点加 1.7 pF 电容（将主模式置于 128 MHz）
- 336 三角形单元，348 未知量

**结果对比**：
| 方法 | 频率点数 | CPU 时间 |
|------|---------|---------|
| 直接法（1 MHz 间隔）| 250 | 1,352 s |
| AWE（六阶，0.01 MHz 间隔）| 25,000 | 35.6 s |
| **加速比** | | **38 倍** |

**加屏蔽罩的线圈**：电感值增大，电容调整为 2.95 pF，加速比达 **50.3 倍**。

**倒 L 型天线和环天线**在有限大地板上的 S 参数计算，与测量值高度吻合。

---

## 15.4 金属散射体分析 | Analysis of Metallic Scatterers

### 15.4.1 公式化

**CFIE**（避免内谐振问题）：

$$\text{CFIE} = \alpha \cdot \text{EFIE} + (1-\alpha) \cdot \text{MFIE} \tag{15.21}$$

**矩阵元素**：

$$Z_{ij} = \alpha \cdot Z_{ij}^{EFIE} + (1-\alpha) \cdot Z_{ij}^{MFIE} \tag{15.22}$$

### 15.4.2 数值算例

**PEC 球**（半径 0.318 cm，10-70 GHz）：
| 方法 | 频率点数 | CPU 时间 |
|------|---------|---------|
| 直接法（1 GHz 间隔）| 61 | 341.1 s |
| AWE（十阶，0.1 GHz 间隔）| — | 10.6 s |
| **加速比** | | **32.3 倍** |

**NASA Almond**（1 m 长，0-1.7 GHz，84 频率点）：
| 方法 | 展开点数 | CPU 时间 |
|------|---------|---------|
| 直接法 | 84 | 23,220 s |
| AWE（二分搜索，7 展开点）| 7 | 1,989.3 s |
| **加速比** | | **11.7 倍** |

误差容差越小，所需展开点越多；选择较大容差可进一步提升加速比。

---

## 15.5 介电散射体分析 | Analysis of Dielectric Scatterers

### 15.5.1 公式化：PMCHW formulation

**PMCHW**（Poggio-Miller-Chang-Harrington-Wu）：
- 目标内外各有一套 EFIE 和 MFIE
- 组合得到四个积分方程
- 免内谐振，稳定求解

**色散介质模型（Debye 模型）**：

$$\varepsilon_r(\omega) = \varepsilon_\infty + \frac{\varepsilon_s - \varepsilon_\infty}{1 + (j\omega\tau)^2} \tag{15.29}$$

### 15.5.2 数值算例

**介电球**（半径 0.5 cm，色散模型：$\varepsilon_{s4} = 2.56$，$\varepsilon_{\infty} = 2.0$，$\tau = 2.0$ ps/rad）：
| 方法 | 频率点数 | CPU 时间 |
|------|---------|---------|
| 直接法（0.5 GHz 间隔）| — | 24,611 s |
| AWE（0.01 GHz 间隔）| — | 2,206 s |

**介电立方体**（1 cm × 1 cm × 1 cm）：类似加速效果。

---

## 15.6 微带天线分析 | Analysis of Microstrip Antennas

### 15.6.1 FEM/BIE 混合方法

**问题几何**：腔体背向微带贴片天线（开凿于金属地平面）：

$$\mathcal{F}(\mathbf{E}) = \text{functional accounting for cavity, aperture, and substrate} \tag{15.31}$$

矩阵方程：

$$[Z(k)] \{x(k)\} = \{b(k)\} \tag{15.32}$$

**色散基底**：Debye 模型描述基底介电常数随频率变化。

### 15.6.2 数值算例

**腔体背向贴片天线**（贴片 3.66 cm × 2.60 cm，基底厚度 0.159 cm，$\varepsilon_r = 2.2$）：

单站 RCS（2-8 GHz）：
| 方法 | 频率点数 | CPU 时间 |
|------|---------|---------|
| 直接法（0.05 GHz 间隔）| 120 | 3,254.4 s |
| AWE（六阶，0.01 GHz 间隔）| 600 | 265.2 s |
| **加速比** | | **12.3 倍** |

**探针馈电贴片天线**（5.0 cm × 3.4 cm，1-4 GHz）：
- 探针阻抗计算：加速比 **15.8 倍**
- 加 50 $\Omega$ 负载阻抗计算：加速比同样显著

**色散基底验证**：AWE 与直接计算在所有色散模型情况下均高度吻合。

---

## 15.7 总结 | Summary

**AWE 方法的核心价值**：
- 将多次重复的矩阵方程求解（每频率点一次）替换为**一次矩阵求逆 + 少量导数计算**
- 通过 **Padé 有理函数** 拓展 Taylor 展开的收敛范围
- 通过 **CFH 二分搜索** 自动适配任意宽频带

**应用效果汇总**：

| 应用领域 | 算例 | 加速比 |
|---------|------|-------|
| MRI 射频线圈 | 无屏蔽鸟笼（348 未知量）| **38 倍** |
| | 有屏蔽鸟笼（1,043 未知量）| **50.3 倍** |
| 金属散射 | PEC 球（10-70 GHz）| **32.3 倍** |
| | NASA Almond（0-1.7 GHz）| **11.7 倍** |
| 介电散射 | 介电球（0.5-35 GHz）| ~**11 倍** |
| 微带天线 | 腔体背向贴片（2-8 GHz）| **12.3 倍** |
| | 探针馈电（1-4 GHz）| **15.8 倍** |

**AWE 的限制与注意事项**：
- 当响应在频带内变化**极其剧烈**时（多 resonance、快速变化），需更多展开点
- **色散介质**：AWE 可直接处理 Debye 模型等频率依赖介电常数
- 对于每点解算代价很高的大规模问题，AWE 的加速比价值更加显著
