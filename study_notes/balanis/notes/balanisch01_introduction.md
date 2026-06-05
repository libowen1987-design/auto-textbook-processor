# Chapter 1: Introduction
# 第1章：引言
> Balanis, *Antenna Theory: Analysis and Design*, 4th Edition — Chapter 1

---

## 1.1 Introduction

天线是"从导行波到自由空间波的能量转换器"（IEEE定义）。作为无线系统的"眼睛"和"耳朵"，天线在整个射频链路中扮演关键角色。

**核心功能：**
- **发射模式**：将传输线/波导中的导行波转换为自由空间传播的电磁波
- **接收模式**：将入射电磁波拾取并转换为导行波

**可逆性（Reciprocity）：** 天线在发射和接收模式下的方向图、增益、阻抗等特性相同（线性无源系统）。

---

## 1.2 Types of Antennas
## 天线分类

天线按结构可分为几大类：

```
天线大家族
│
├── 线天线 (Wire Antennas)
│   ├── 偶极子 (Dipole) — \lambda/2, \lambda/4 单极子
│   ├── 单极子 (Monopole)
│   ├── 环天线 (Loop) — 小环、大环
│   ├── 螺旋天线 (Helix)
│   └── 行波天线 (Traveling Wave, 如 Vee, Rhombic)
│
├── 口径天线 (Aperture Antennas)
│   ├── 喇叭 (Horn) — 角锥、圆锥、波纹
│   ├── 反射面 (Reflector) — 抛物面、卡塞格伦
│   └── 开口波导 (Open-Ended Waveguide)
│
├── 微带天线 (Microstrip/Patch Antennas)
│   ├── 矩形贴片、圆形贴片
│   ├── 印刷偶极子
│   └── 缝隙天线 (Slot)
│
├── 阵列天线 (Array Antennas)
│   ├── 线阵 / 平面阵 / 共形阵
│   └── 相控阵 / 自适应阵 / MIMO
│
└── 其他
    ├── 透镜天线 (Lens)
    ├── 频率无关天线 (Log-Periodic, Spiral)
    └── 漏波天线 (Leaky-Wave)
```

---

## 1.3 Radiation Mechanism
## 辐射机理

辐射的本质是**加速电荷产生电磁波**。在天线中，辐射源于电流和电荷的时变分布。

### 1.3.1 单电荷辐射

一个时变的电荷 $q(t)$ 产生时变的电场和磁场。当电荷加速时，电磁能量从电荷区域"脱落"并向外传播。

辐射功率与加速度的平方成正比：

> **注：** 以下 Larmor 辐射功率公式出自 Griffiths《Introduction to Electrodynamics》而非 Balanis 原书。Balanis Ch1 仅以文字描述加速电荷辐射基本概念，未给出此公式。此处的引用是为了辅助理解辐射功率的物理本质。

$$
P_{\text{rad}} \propto \frac{q^2 a^2}{6\pi \epsilon_0 c^3}
$$

其中 $a$ 是加速度。这就是 Larmor 公式（非相对论形式）。

### 1.3.2 双线传输线的辐射

开路传输线末端的位移电流产生辐射：

```
           +------+        
  传输线 → |      | → 束散开 → 辐射
           +------+        
```

- 平行传输线的场互相抵消，辐射极弱
- 当将导线束散开时，场的抵消不再完全，产生净辐射

**关键直觉：** 天线的本质就是**将传输线打开**，让场暴露于自由空间。

### 1.3.3 偶极子天线

最简单的辐射结构：**\lambda/2 偶极子**由一段开路传输线末端对称张开而成。

电流分布（近似正弦）：
$$
I(z) = I_0 \sin\left[k\left(\frac{l}{2} - |z|\right)\right], \quad -l/2 \leq z \leq l/2
$$

对 \lambda/2 偶极子（$l = \lambda/2$）：
$$
I(z) = I_0 \cos\left(\frac{\pi z}{l}\right), \quad -l/2 \leq z \leq l/2
$$

---

## 1.4 Frequency Bands
## 频段划分

Balanis 覆盖的频率分配：

| 频段 | 频率范围 | 波长范围 | 典型天线类型 |
|:----:|:---------:|:---------:|:-----------:|
| ELF | 30–300 Hz | 10,000–1,000 km | 长波（地面/潜艇） |
| VLF | 3–30 kHz | 100–10 km | 顶部加载单极子 |
| LF | 30–300 kHz | 10–1 km | 线天线 |
| MF | 300–3000 kHz | 1–0.1 km | 直立单极子 |
| HF | 3–30 MHz | 100–10 m | 偶极子、Yagi 天线 |
| VHF | 30–300 MHz | 10–1 m | Yagi、环天线 |
| UHF | 300–3000 MHz | 1–0.1 m | 贴片、螺旋、阵列 |
| L 波段 | 1–2 GHz | 30–15 cm | 阵列、喇叭 |
| S 波段 | 2–4 GHz | 15–7.5 cm | 微带阵列 |
| C 波段 | 4–8 GHz | 7.5–3.75 cm | 喇叭、反射面 |
| X 波段 | 8–12 GHz | 3.75–2.5 cm | 缝隙阵列、喇叭 |
| Ku 波段 | 12–18 GHz | 2.5–1.67 cm | 扁平阵列 |
| K 波段 | 18–27 GHz | 1.67–1.11 cm | 微带、波导 |
| Ka 波段 | 27–40 GHz | 1.11–0.75 cm | 毫米波天线 |
| mm-wave | 40–300 GHz | 7.5–1 mm | 透镜、片上天线 |

**工程要点：** 频率越高 → 波长越短 → 天线尺寸越小 → 增益潜力越大 → 大气衰减越大。

---


现代天线设计依赖三大数值方法：

### 矩量法 (MoM, Method of Moments)
- 求解积分方程（IE）的频域方法
- 适合导线和贴片结构（FW-IE, EFIE, MFIE）
- 商业实现：FEKO, NEC, ADS Momentum

### 有限元法 (FEM, Finite Element Method)
- 求解微分方程的频域方法
- 适合复杂介质结构和波导器件
- 商业实现：HFSS (Ansys), COMSOL

### 时域有限差分法 (FDTD, Finite-Difference Time-Domain)
- 直接求解时域 Maxwell 方程
- 适合宽频带、瞬态响应、复杂电磁环境
- 商业实现：CST MWS, SEMCAD

### 高频近似法
- **GTD/UTD**（几何绕射理论）：电大尺寸散射体
- **PO**（物理光学）：大反射面
- **GO**（几何光学）：透镜

---


| 概念 | 要点 |
|------|------|
| 天线本质 | 导行波 ↔ 自由空间波的能量转换器 |
| 辐射机理 | 加速电荷产生电磁辐射 |
| 可逆性 | 收发天线特性相同（线性无源系统） |
| 天线分类 | 线/口径/微带/阵列/其他 |
| 频段 | 波长决定天线尺度，频段决定应用方向 |
| 数值方法 | MoM/FEM/FDTD 三大支柱，各有适用场景 |

---


- C. A. Balanis, *Antenna Theory: Analysis and Design*, 4th ed., Wiley, 2016, Chapter 1.
- IEEE Std 145-2013, *IEEE Standard for Definitions of Terms for Antennas*.
- J. D. Kraus and R. J. Marhefka, *Antennas for All Applications*, 3rd ed., McGraw-Hill, 2002.
- R. F. Harrington, *Time-Harmonic Electromagnetic Fields*, IEEE Press, 2001.

---

## Supplements: 补充内容

### S.1 天线基本辐射参数 (Basic Antenna Parameters)

以下参数是天线的核心度量，Balanis §1.4–§1.8 系统定义：

#### 辐射强度 Radiation Intensity $U(\theta,\phi)$

单位立体角内的辐射功率（W/sr），与距离 $r$ 无关：
$$
U(\theta,\phi) = r^2 \, W_{\text{rad}}(\theta,\phi)
$$

其中 $W_{\text{rad}}$ 是辐射功率密度（Poynting 矢量实部），单位 W/m²。

- 各向同性源的辐射强度：$U_0 = P_{\text{rad}} / 4\pi$
- 总辐射功率：$P_{\text{rad}} = \oint\limits_{\Omega} U(\theta,\phi) \, d\Omega$

#### 方向性系数 Directivity $D$

衡量天线将能量集中到某个方向的**能力**（不包含损耗）：
$$
D(\theta,\phi) = \frac{U(\theta,\phi)}{U_0} = \frac{4\pi \, U(\theta,\phi)}{P_{\text{rad}}}
$$

**最大方向性系数**（通常简称方向性）：
$$
D_0 = D_{\text{max}} = \frac{U_{\text{max}}}{U_0} = \frac{4\pi \, U_{\text{max}}}{P_{\text{rad}}}
$$

对于各向同性源：$D_0 = 1$（即 0 dB）。

方向性系数的物理含义：最大方向的辐射强度是平均辐射强度的 $D_0$ 倍。

#### 增益 Gain $G$

增益与方向性的区别在于**计入天线欧姆损耗**：
$$
G(\theta,\phi) = \frac{4\pi \, U(\theta,\phi)}{P_{\text{in}}}
$$

其中 $P_{\text{in}}$ 是天线输入功率。带入辐射效率：
$$
G(\theta,\phi) = \eta_{\text{rad}} \, D(\theta,\phi), \quad \eta_{\text{rad}} = \frac{P_{\text{rad}}}{P_{\text{in}}}
$$

**最大增益**：
$$
G_0 = \eta_{\text{rad}} \, D_0
$$

- 增益单位通常用 dBi（相对于各向同性源）或 dBd（相对于半波偶极子，$G_{\text{dBi}} \approx G_{\text{dBd}} + 2.15$）
- 效率 $\eta_{\text{rad}}$ 包含：导体损耗（$I^2R$）、介质损耗、表面波损耗

#### 孔径效率 Aperture Efficiency $\varepsilon_{\text{ap}}$

定义天线的**有效面积**与**物理面积**之比，适用于口径天线（喇叭、反射面等）：
$$
\varepsilon_{\text{ap}} = \frac{A_{\text{eff}}}{A_{\text{phys}}}
$$

其中：
- $A_{\text{eff}}$ = 有效孔径（effective area），对应天线所能截获的入射波功率
- $A_{\text{phys}}$ = 物理孔径面积

孔径效率总是 $0 < \varepsilon_{\text{ap}} \leq 1$，典型值在 0.5–0.8 之间。

最大方向性系数也可以通过有效孔径表达：
$$
D_0 = \frac{4\pi}{\lambda^2} \, A_{\text{eff}} = \frac{4\pi}{\lambda^2} \, \varepsilon_{\text{ap}} A_{\text{phys}}
$$

---

### S.2 标准频率分配表 (Standard Frequency Band Designations)

Balanis Table 1.1 所列的 IEEE 标准频段命名（与前面 §1.4 的工程频段互为补充）：

| 频段代号 | 频率范围 | 波长范围 | 典型天线 | 典型应用 |
|:--------:|:--------:|:--------:|:---------|:---------|
| ELF (Extremely Low) | 3–30 Hz | $10^5$–$10^4$ km | 长导线 | 潜艇通信、地壳探测 |
| VLF (Very Low) | 3–30 kHz | 100–10 km | 顶部加载单极子 | 导航(Loran)、时频标准 |
| LF (Low) | 30–300 kHz | 10–1 km | 线天线 | AM广播(长波)、航空信标 |
| MF (Medium) | 0.3–3 MHz | 1–0.1 km | 直立单极子 | AM广播（中波） |
| HF (High) | 3–30 MHz | 100–10 m | 偶极子、Yagi | 短波广播、业余电台、地波/天波 |
| VHF (Very High) | 30–300 MHz | 10–1 m | Yagi、偶极子阵 | FM广播、电视、空管雷达 |
| UHF (Ultra High) | 0.3–3 GHz | 1–0.1 m | 贴片、螺旋、喇叭 | 电视、手机、GPS、蓝牙/Wi-Fi |
| SHF (Super High) | 3–30 GHz | 10–1 cm | 喇叭、反射面、阵列 | 卫星通信、雷达、微波点对点、5G |
| EHF (Extremely High) | 30–300 GHz | 10–1 mm | 透镜、片上天线 | 毫米波雷达(车载)、6G研究、遥感 |

> **注：** Balanis Table 1.1 的完整频段范围从 3 Hz（ELF）到 300 GHz（EHF）。上表补充了 §1.4 的工程细分频段表，两者使用不同的分类粒度——前者遵循 IEEE Std 521，后者来自传统雷达/通信工程命名。

---

### S.3 辐射机理深度补充 (Radiation Mechanism — §1.3 精华扩展)

Balanis §1.3 从**场论基础**出发阐述辐射机理，以下是关键内容的系统补充：

#### S.3.1 单根载流导线的辐射条件

一段单根载流导线产生辐射需满足的根本条件：存在**时变电流** $\rightarrow$ 存在**加速电荷** $\rightarrow$ 产生**辐射场**。

根据 Maxwell 方程组的连续性：
$$
\nabla \cdot \mathbf{J} = -\frac{\partial \rho_v}{\partial t}
$$

即**电荷守恒定律**的微分形式：
- 时变电荷密度 $\rho_v(t)$ 必然伴随时变电流密度 $\mathbf{J}(t)$
- 时变 $\mathbf{J}$ 根据 Ampère 定律产生时变磁场 $\mathbf{H}$
- 时变 $\mathbf{H}$ 根据 Faraday 定律产生时变电场 $\mathbf{E}$
- 波动的 $\mathbf{E}$ 与 $\mathbf{H}$ 互相激励，以光速向外传播 $\rightarrow$ **辐射**

#### S.3.2 辐射的两类基本源

Balanis 指出天线辐射可由两类等效源描述：

| 源类型 | 数学描述 | 物理对应 |
|:------:|:--------:|:--------|
| **电流源** $\mathbf{J}$ | $\nabla \times \mathbf{H} = \mathbf{J} + j\omega\epsilon\mathbf{E}$ | 导线中的传导电流 |
| **磁流源** $\mathbf{M}$（等效） | $\nabla \times \mathbf{E} = -\mathbf{M} - j\omega\mu\mathbf{H}$ | 口径上的等效磁流 |

实际天线往往同时存在电流元和磁流元。

#### S.3.3 无穷小电偶极子 (Infinitesimal Dipole)

Balanis §1.3 的核心思想通过**无穷小偶极子（Hertzian dipole）**体现：

- 长度 $l \ll \lambda$ 的短导线，载均匀时谐电流 $I = I_0 e^{j\omega t}$
- 电流矩：$I_0 l$ （单位：A·m）

远场区（$kr \gg 1$）的辐射场：
$$
E_\theta \approx j\eta \frac{k I_0 l \, e^{-jkr}}{4\pi r} \sin\theta
$$
$$
H_\phi \approx \frac{E_\theta}{\eta} = j \frac{k I_0 l \, e^{-jkr}}{4\pi r} \sin\theta
$$
$$
W_{\text{rad}}(\theta) = \frac{1}{2} \, |E_\theta H_\phi^*| = \frac{\eta}{8} \left( \frac{k I_0 l}{4\pi r} \right)^2 \sin^2\theta
$$

其中：
- $\eta = \sqrt{\mu/\epsilon} \approx 120\pi \, \Omega$（自由空间波阻抗）
- $k = 2\pi/\lambda$（波数）

**重要物理结论：**
1. 远场辐射方向图为 $\sin^2\theta$ 的甜甜圈形状
2. 辐射功率与 $(I_0 l)^2$ 成正比，即与电流矩的平方成正比
3. 随着偶极子长度从 $l \ll \lambda$ 增加到 $l = \lambda/2$，方向性增强，辐射效率提升

#### S.3.4 辐射近场与远场分区

Balanis §1.3 定义了天线的场区：

| 区域 | 条件 | 场特点 |
|:----:|:----:|:------|
| **反应近场区** (Reactive Near-Field) | $r < 0.62\sqrt{D^3/\lambda}$ | 电抗性储能占主导，$\mathbf{E}, \mathbf{H}$ 准静态 |
| **辐射近场区** (Radiating Near-Field / Fresnel) | $0.62\sqrt{D^3/\lambda} \leq r < 2D^2/\lambda$ | 角分布随距离变化，存在径向场分量 |
| **远场区** (Far-Field / Fraunhofer) | $r \geq 2D^2/\lambda$ | $\mathbf{E}, \mathbf{H}$ 为 TEM 波，方向图与距离无关 |

其中 $D$ 是天线最大尺寸。远场区同时满足 $r \gg \lambda$ 和 $r \gg D$。

---

> **补充说明：** 以上 S.1–S.3 节的内容均基于 Balanis《Antenna Theory》第 1 章原文提取与整理，公式和参数定义与原书一致。Larmor 公式除外（见 §1.3.1 注释）。
