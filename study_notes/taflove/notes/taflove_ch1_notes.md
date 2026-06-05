---
chapter: 1
title: Electrodynamics Entering the 21st Century
book: Computational Electrodynamics — The Finite-Difference Time-Domain Method (3rd Ed.)
author: Allen Taflove, Susan C. Hagness
raw_size: 74,967 bytes
tokens_processed: ~15K
---

# Chapter 1: Electrodynamics Entering the 21st Century
> **中英双语版**

> 进入 21 世纪的电动力学

## 1.1 Introduction
> 引言

Maxwell's partial differential equations of electrodynamics, formulated approximately 140 years ago, represent a fundamental unification of electric and magnetic fields predicting electromagnetic wave phenomena. Feynman called this "the most outstanding achievement of 19th-century science."
> 麦克斯韦的电动力学偏微分方程组（约 140 年前提出）代表了电磁场的基本统一，预言了电磁波现象。费曼称此为"19 世纪科学最杰出的成就"。

**Key shift:** Large-scale solutions of Maxwell's equations are shifting rapidly from military defense toward commercial applications in high-speed communications, computing, and biomedicine.
> **关键转变：** 麦克斯韦方程的大规模求解正迅速从军事防御转向高速通信、计算和生物医学的商业应用。

---

## 1.2 The Heritage of Military Defense Applications
> 军事防御应用的遗产

From WWII until ~1990, the primary answer was military defense.
> 从二战到约 1990 年，主要的答案是军事防御。

**Radar technology** / **Stealth technology** / **EMP hardening**
> **雷达技术** / **隐身技术** / **电磁脉冲加固**

> **Numerical Intuition:** Military defense drove the entire field for 50 years. Full-aircraft RCS computation at microwave frequencies motivated virtually all algorithmic advances.
> **数值直觉：** 军事防御推动了整个领域 50 年的发展。微波频段的全机雷达散射截面计算驱动了几乎所有算法进步。

---

## 1.3 Frequency-Domain Solution Techniques
> 频域求解技术

### 1.3.1 High-Frequency/Asymptotic Techniques
> 高频/渐近技术

Geometrical optics, GTD, UTD, physical optics, PTD.
> 几何光学、几何绕射理论、一致性绕射理论、物理光学、物理绕射理论。

**Limitations:** Valid only for electrically large objects with smooth surfaces.
> **局限性：** 仅适用于具有光滑表面的电大尺寸物体。

### 1.3.2 Integral Equation / Method of Moments (MoM)
> 积分方程/矩量法

Solve for surface currents; frequency sweep requires solving at each frequency independently.
> 求解表面电流；扫频需在每个频率独立求解。

### 1.3.3 Fast Multipole Method (FMM) / MLFMA
> 快速多极子法

O(N log N) complexity vs O(N³) for standard MoM. Still frequency-domain.
> 复杂度 O(N log N)，对比标准 MoM 的 O(N³)。仍为频域方法。

> **Numerical Intuition:** Frequency-domain techniques require solving a separate matrix equation for each frequency point. FDTD naturally provides wideband response from a single simulation.
> **数值直觉：** 频域技术需为每个频率点求解单独矩阵方程。FDTD 通过单次仿真自然获得宽带响应。

---

## 1.4 Rise of Finite-Difference Time-Domain Techniques
> FDTD 技术的兴起

FDTD advantages:
> FDTD 优势：
- **Direct physical insight:** Watch fields evolve in time
  > 直接物理洞察：观察场随时间的演化
- **Wideband response:** Single simulation → any frequency via DFT
  > 宽带响应：单次仿真→通过 DFT 获得任意频率
- **Nonlinear/dynamic media:** Naturally handled in time domain
  > 非线性/动态介质：时域自然处理
- **Arbitrary geometry:** No Green's function required
  > 任意几何：无需格林函数

---

## 1.5 History of FDTD Techniques for Maxwell's Equations
> FDTD 技术史

| Year | Contributor | Contribution |
|------|-------------|--------------|
| 年份 | 贡献者 | 贡献 |
| 1966 | Yee | Original Yee algorithm / 原始 Yee 算法 |
| 1975 | Taflove & Brodwin | First FDTD scattering solutions / 首次 FDTD 散射解 |
| 1994 | Berenger | Perfectly matched layer / 完美匹配层 |

> **Numerical Intuition:** The leapfrog scheme is *explicit* — no matrix inversion. This is the source of FDTD's simplicity and parallel efficiency.
> **数值直觉：** 蛙跳格式是*显式的*——无需矩阵求逆，这是 FDTD 简单性和并行效率的来源。

---

## 1.6 Characteristics of FDTD
> FDTD 的特性

### Key Characteristics
> 关键特性

1. **No potentials** — operates directly on E and H fields
   > 无势——直接对电场和磁场操作
2. **Sub-wavelength spatial sampling:** 10–20 samples per $\lambda_0$
   > 亚波长空间采样：每个波长 10–20 个采样点
3. **Time-stepping stability:** CFL condition
   > 时间步进稳定性：CFL 条件
4. **Marching-in-time:** Simulates continuous EM waves
   > 时间推进：模拟连续电磁波
5. **Absorbing boundary conditions (ABCs)** at outer lattice truncation
   > 外部网格截断处的吸收边界条件
6. **Wideband frequency response** via DFT
   > 通过 DFT 获得宽带频率响应

### 1.6.1 Classes of Algorithms
> 算法分类

1. **Almost Completely Structured (Yee-type):** Uniform Cartesian grid
   > 近似全结构化（Yee 型）：均匀笛卡尔网格
2. **Surface-Fitted (Globally Distorted):** Space lattice distorted to fit shape
   > 表面适配（全局变形）：空间网格变形以贴合形状
3. **Completely Unstructured:** Collection of varying cells
   > 完全非结构化：不同形状大小的网格集合

### 1.6.2 Predictive Dynamic Range
> 预测动态范围

**Definition:** $10 \log_{10}(P_0/P_s)$ [dB] where $P_0$ is incident power density, $P_s$ is minimum observable scattered power density.
> **定义：** $10 \log_{10}(P_0/P_s)$ [dB]

**Typical values:**
> **典型值：**
- 32-bit arithmetic: ~40–60 dB
- 64-bit arithmetic: ~60–80 dB

### 1.6.3 Scaling to Very Large Problem Sizes
> 扩展到超大问题规模

FDTD memory ∝ N, operations per time-step ∝ N. O(N) is fundamentally more favorable than MoM's O(N²) or O(N³).
> FDTD 存储量与 N 成正比，每时间步运算量与 N 成正比。O(N) 本质上优于 MoM 的 O(N²) 或 O(N³)。

---

## 1.7 Key Application Domains (Case Studies)
> 关键应用领域（案例研究）

### 1.7.1 ELF/VLF Propagation
> 极低频/甚低频传播

3D model of Earth ±100 km, resolution ~40 × 40 × 5 km. Schumann resonances, pulse propagation from lightning.
> 地球 ±100 km 的三维模型，分辨率约 40 × 40 × 5 km。Schumann 谐振、闪电脉冲传播。

### 1.7.2 Cellphone SAR
> 手机比吸收率

Motorola i250 phone with 121 MRI-derived head slices, 15 tissue types. Peak SAR < 1.6 W/kg standard compliance.
> Motorola i250 手机，121 层 MRI 头部切片，15 种组织类型。满足峰值 SAR < 1.6 W/kg 标准。

### 1.7.3 Breast Cancer Detection
> 乳腺癌检测

UWB pulse illumination by antenna array → space-time imaging for malignant tumors < 5 mm.
> 天线阵列的 UWB 脉冲照射→时空成像探测 < 5 mm 恶性肿瘤。

### 1.7.4 Missile Homing
> 导弹制导

EM wave interactions between antenna and protective radome generate angular target-location errors.
> 天线与保护罩间的电磁波相互作用产生角度定位误差。

### 1.7.5 Aircraft Vulnerability
> 飞行器易损性

Hybrid FDTD-FE: Flexible FE mesh for surfaces, FDTD bricks for space. Saab Trainer aircraft (11 m, 8 m wingspan).
> 混合 FDTD-FE：表面用灵活 FE 网格，空间用 FDTD 块。Saab 教练机。

### 1.7.6-1.7.8 Photonic Devices
> 光子器件

EBG waveguides > 100 GHz, photonic crystal microcavity laser (Q ≈ 3,000), cross-waveguide switch.
> EBG 波导 > 100 GHz，光子晶体微腔激光器（Q ≈ 3,000），交叉波导开关。

---

## 1.8 Conclusions
> 结论

The field has shifted from military-defense-driven to **communications, computing, and biomedicine**.
> 该领域已从军事防御驱动转向**通信、计算和生物医学**。

**Remaining grand challenge:** Unification of electromagnetic, heat transport, and quantum phenomena.
> **未解决的大挑战：** 电磁、热输运和量子现象的统一。
