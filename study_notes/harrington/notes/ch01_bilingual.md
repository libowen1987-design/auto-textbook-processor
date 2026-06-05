---
chapter: 1
title: Fundamental Concepts
source: Roger F. Harrington, Time-Harmonic Electromagnetic Fields, IEEE Press
pages: 1-60
---

# Chapter 1: Fundamental Concepts / 基本概念

## Section 1-1: Introduction / 引言

**English:**

The topic of this book is the theory and analysis of electromagnetic phenomena that vary sinusoidally in time, henceforth called a-c (alternating-current) phenomena. The fundamental concepts which form the basis of our study are presented in this chapter.

We shall view electromagnetic phenomena from the "macroscopic" standpoint, that is, linear dimensions are large compared to atomic dimensions and charge magnitudes are large compared to atomic charges. This allows us to neglect the granular structure of matter and charge. We assume all matter to be stationary with respect to the observer.

The rationalized mksc system of units is used throughout. In this system the unit of length is the meter, the unit of mass is the kilogram, the unit of time is the second, and the unit of charge is the coulomb.

**中文：**

本书的主题是正弦时变电磁现象的理论与分析，此后称之为交流（a-c）现象。我们研究所依据的基本概念将在本章中呈现。

我们将从"宏观"角度看待电磁现象，即线性尺寸远大于原子尺寸，电荷量远大于原子电荷。这使我们能够忽略物质和电荷的颗粒状结构。我们假设所有物质相对于观察者都是静止的。

全书采用有理化mksc单位制。在此系统中，长度单位为米，质量单位为千克，时间单位为秒，电荷单位为库仑。


---

## Section 1-2: Basic Equations / 基本方程

**English:**

The usual electromagnetic field equations are expressed in terms of six quantities:

- $\mathcal{E}$, called the **electric intensity** (volts per meter, V/m)
- $\mathcal{H}$, called the **magnetic intensity** (amperes per meter, A/m)  
- $\mathcal{D}$, called the **electric flux density** (coulombs per square meter, C/m²)
- $\mathcal{B}$, called the **magnetic flux density** (webers per square meter, Wb/m²)
- $\mathcal{J}$, called the **electric current density** (amperes per square meter, A/m²)
- $q_v$, called the **electric charge density** (coulombs per cubic meter, C/m³)

Wherever these quantities are well-behaved (continuous with continuous derivatives), they obey the Maxwell equations in differential form:

$$\nabla \times \mathcal{E} = -\frac{\partial \mathcal{B}}{\partial t} \quad \text{(Faraday's law)}$$

$$\nabla \times \mathcal{H} = \mathcal{J} + \frac{\partial \mathcal{D}}{\partial t} \quad \text{(Ampère-Maxwell law)}$$

$$\nabla \cdot \mathcal{D} = q_v \quad \text{(Gauss' law for electricity)}$$

$$\nabla \cdot \mathcal{B} = 0 \quad \text{(Gauss' law for magnetism)}$$

The equation of continuity (conservation of charge) is:

$$\nabla \cdot \mathcal{J} = -\frac{\partial q_v}{\partial t} \tag{1-2}$$

Corresponding integral forms are:

$$\oint_C \mathcal{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int_S \mathcal{B} \cdot d\mathbf{s} \tag{1-3a}$$

$$\oint_C \mathcal{H} \cdot d\mathbf{l} = \int_S \left(\mathcal{J} + \frac{\partial \mathcal{D}}{\partial t}\right) \cdot d\mathbf{s} \tag{1-3b}$$

$$\oint_S \mathcal{D} \cdot d\mathbf{s} = \int_V q_v \, dV \tag{1-3c}$$

$$\oint_S \mathcal{B} \cdot d\mathbf{s} = 0 \tag{1-3d}$$

**Circuit quantities** correspond to field quantities through integration:

| Circuit Quantity | Symbol | Definition | Units |
|-----------------|--------|------------|-------|
| Voltage | $v$ | $v = \int_a^b \mathcal{E} \cdot d\mathbf{l}$ | V (volts) |
| Current | $i$ | $i = \int_S \mathcal{J} \cdot d\mathbf{s}$ | A (amperes) |
| Charge | $q$ | $q = \int_V q_v \, dV$ | C (coulombs) |
| Magnetic flux | $\psi$ | $\psi = \int_S \mathcal{B} \cdot d\mathbf{s}$ | Wb (webers) |
| Electric flux | $\psi^*$ | $\psi^* = \int_S \mathcal{D} \cdot d\mathbf{s}$ | C (coulombs) |
| Magnetomotive force | $u$ | $u = \oint_C \mathcal{H} \cdot d\mathbf{l}$ | A (amperes) |

**中文：**

电磁场方程通常用六个量来表示：

- $\mathcal{E}$，称为**电场强度**（伏特/米，V/m）
- $\mathcal{H}$，称为**磁场强度**（安培/米，A/m）
- $\mathcal{D}$，称为**电通量密度**（库仑/平方米，C/m²）
- $\mathcal{B}$，称为**磁通量密度**（韦伯/平方米，Wb/m²）
- $\mathcal{J}$，称为**电流密度**（安培/平方米，A/m²）
- $q_v$，称为**电荷密度**（库仑/立方米，C/m³）

只要这些量是"良性"的（即连续且具有连续导数），它们就满足微分形式的麦克斯韦方程：

$$\nabla \times \mathcal{E} = -\frac{\partial \mathcal{B}}{\partial t} \quad \text{（法拉第定律）}$$

$$\nabla \times \mathcal{H} = \mathcal{J} + \frac{\partial \mathcal{D}}{\partial t} \quad \text{（安培-麦克斯韦定律）}$$

$$\nabla \cdot \mathcal{D} = q_v \quad \text{（高斯电定律）}$$

$$\nabla \cdot \mathcal{B} = 0 \quad \text{（高斯磁定律）}$$

连续性方程（电荷守恒）为：

$$\nabla \cdot \mathcal{J} = -\frac{\partial q_v}{\partial t} \tag{1-2}$$

对应的积分形式为：

$$\oint_C \mathcal{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int_S \mathcal{B} \cdot d\mathbf{s} \tag{1-3a}$$

$$\oint_C \mathcal{H} \cdot d\mathbf{l} = \int_S \left(\mathcal{J} + \frac{\partial \mathcal{D}}{\partial t}\right) \cdot d\mathbf{s} \tag{1-3b}$$

$$\oint_S \mathcal{D} \cdot d\mathbf{s} = \int_V q_v \, dV \tag{1-3c}$$

$$\oint_S \mathcal{B} \cdot d\mathbf{s} = 0 \tag{1-3d}$$

**电路量**通过积分与场量对应：

| 电路量 | 符号 | 定义 | 单位 |
|--------|------|------|------|
| 电压 | $v$ | $v = \int_a^b \mathcal{E} \cdot d\mathbf{l}$ | V（伏特） |
| 电流 | $i$ | $i = \int_S \mathcal{J} \cdot d\mathbf{s}$ | A（安培） |
| 电荷 | $q$ | $q = \int_V q_v \, dV$ | C（库仑） |
| 磁通量 | $\psi$ | $\psi = \int_S \mathcal{B} \cdot d\mathbf{s}$ | Wb（韦伯） |
| 电通量 | $\psi^*$ | $\psi^* = \int_S \mathcal{D} \cdot d\mathbf{s}$ | C（库仑） |
| 磁动势 | $u$ | $u = \oint_C \mathcal{H} \cdot d\mathbf{l}$ | A（安培） |


---
