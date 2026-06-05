# Chapter 1: Introduction

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

天线按结构可分为几大类：

```
天线大家族
│
├── 线天线 (Wire Antennas)
│   ├── 偶极子 (Dipole) — λ/2, λ/4 单极子
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

辐射的本质是**加速电荷产生电磁波**。在天线中，辐射源于电流和电荷的时变分布。

### 1.3.1 单电荷辐射

一个时变的电荷 $q(t)$ 产生时变的电场和磁场。当电荷加速时，电磁能量从电荷区域"脱落"并向外传播。

辐射功率与加速度的平方成正比：
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

最简单的辐射结构：**λ/2 偶极子**由一段开路传输线末端对称张开而成。

电流分布（近似正弦）：
$$
I(z) = I_0 \sin\left[k\left(\frac{l}{2} - |z|\right)\right], \quad -l/2 \leq z \leq l/2
$$

对 λ/2 偶极子（$l = \lambda/2$）：
$$
I(z) = I_0 \cos\left(\frac{\pi z}{l}\right), \quad -l/2 \leq z \leq l/2
$$

---

## 1.4 Frequency Bands

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

## 1.5 Computational Electromagnetics in Antenna Design (Balanis 4e 新增)

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

## 本章要点

| 概念 | 要点 |
|------|------|
| 天线本质 | 导行波 ↔ 自由空间波的能量转换器 |
| 辐射机理 | 加速电荷产生电磁辐射 |
| 可逆性 | 收发天线特性相同（线性无源系统） |
| 天线分类 | 线/口径/微带/阵列/其他 |
| 频段 | 波长决定天线尺度，频段决定应用方向 |
| 数值方法 | MoM/FEM/FDTD 三大支柱，各有适用场景 |

---

## 参考文献

- C. A. Balanis, *Antenna Theory: Analysis and Design*, 4th ed., Wiley, 2016, Chapter 1.
- IEEE Std 145-2013, *IEEE Standard for Definitions of Terms for Antennas*.
- J. D. Kraus and R. J. Marhefka, *Antennas for All Applications*, 3rd ed., McGraw-Hill, 2002.
- R. F. Harrington, *Time-Harmonic Electromagnetic Fields*, IEEE Press, 2001.
