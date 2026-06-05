# Ch10: Deep Regional Hyperthermia Treatment Planning — SAR, Phased Array, and FDTD Optimization

> **中英双语版**
> **Source:** Houle & Sullivan — *Electromagnetic Simulation Using the FDTD Method with Python* (IEEE Press, 3rd ed. 2020), Chapter 6 (original pp. 159–169)
> **Core Topic:** BSD Sigma 60 phased-array hyperthermia system + FDTD treatment planning + SAR calculation + superposition + amplitude/phase control

## 10.1 Clinical Background: Deep Regional Hyperthermia | 临床背景：深部区域性热疗

### 10.1.1 What Is Hyperthermia? | 什么是热疗？

Hyperthermia heats tissue to therapeutic temperatures (40–46°C) to assist cancer treatment, often combined with radiation or chemotherapy. Deep tumors (prostate, bladder, cervical) are most challenging.
热疗通过将组织加热到治疗温度（通常 40–46°C）辅助癌症治疗，常与放疗或化疗联合使用。深部肿瘤（前列腺、膀胱、宫颈癌）最具挑战性。

### 10.1.2 Annular Phased Array (APA) | 环形相控阵

Multiple antennas around the patient, with adjustable amplitude/phase per channel, produce **constructive interference** at the target point.
多天线环绕患者排列，各路幅度和相位可调，使辐射能量在目标点产生**相长干涉**。

---

## 10.2 BSD Sigma 60 System Modeling | BSD Sigma 60 系统建模

### 10.2.1 System Parameters | 系统参数

- **Ring volume**: 60 cm diameter（环形容积：直径 60 cm）
- **Antennas**: 8 dipole antennas, evenly spaced on circumference（8 个偶极子天线，均匀分布在圆周）
- **Groups**: 4 quadrants, each with 2 dipoles（4 个象限，每象限含 2 个偶极子）
- **Frequency**: typically 90 MHz（工作频率：通常 90 MHz）
- **Power**: independent linear Class A amplifiers per quadrant, amplitude and phase independently adjustable（独立线性放大器，幅度和相位均可独立调节）

### 10.2.2 FDTD Problem Space | FDTD 问题空间

```python
ie = je = ke = 80    # 80×80×80 grid cells | 网格单元
ddx = 0.01           # 1 cm³ per cell | 每格 1 cm³
# Total: 80 cm × 80 cm × 80 cm, 5-cell PML on all boundaries
```

### 10.2.3 Dipole Antenna Model | 偶极子天线建模

```python
E_z_source = exp(-0.5 * ((time_step - 200) ** 2 / 30**2))
```

$$E_z^{\text{source}}(T) = \exp\left[-\frac{(T - 200)^2}{2 \cdot 30^2}\right]$$

### 10.2.4 Current Distribution Monitoring | 电流分布监测

Using **Ampere's circuital law** (Eq. 6.1):
通过**安培环路定理**监测电流分布：

$$I = \oint_C \mathbf{H} \cdot d\mathbf{l}$$

Monitor $H_x$ field in front of the dipole (x direction) to infer the current flowing through the dipole arms.
监测偶极子前方 $H_x$ 场间接获得流过偶极子臂的电流分布。

---

## 10.3 Patient Model: CT to FDTD Parameters | 患者模型：CT 扫描到 FDTD 参数

### 10.3.1 Tissue Classification | 组织分类

| Tissue Type | $\epsilon_r$ | $\sigma$ (S/m) |
|:-----------|:------------|:---------------|
| Fat | Low $\epsilon_r$ | Low $\sigma$ |
| Muscle | High $\epsilon_r$ | High $\sigma$ |
| Bone | Moderate | Low $\sigma$ |

CT pixel values map to three tissue types. Multiple pixels average into one FDTD cell (1 cm$^3$).
CT 像素值映射为三类组织参数，多像素平均到 FDTD 网格单元。

---

## 10.4 FDTD Simulation Workflow | FDTD 仿真流程

### 10.4.1 Four Independent FDTD Runs | 四次独立 FDTD 运行

`fd3d_apa.py` runs FDTD **separately for each quadrant**, producing four sets of 3D field distributions:
对四个象限分别运行一次 FDTD，产生四组独立的三维场分布：

- Run 1: Only Quadrant 1 feeds → $E_{z,1}(\mathbf{r})$, amplitude $A_1$, phase $P_1$
- Run 2: Quadrant 2 → $A_2$, $P_2$
- Run 3: Quadrant 3 → $A_3$, $P_3$
- Run 4: Quadrant 4 → $A_4$, $P_4$

### 10.4.2 Discrete Fourier Transform at 90 MHz | 90 MHz 离散傅里叶变换

$$E_z(x,y,z)\big|_{\omega = 2\pi \times 90\text{MHz}} = \sum_{n=0}^{N-1} E_z^n(x,y,z) \cdot e^{-j\omega n\Delta t}$$

---

## 10.5 SAR (Specific Absorption Rate) Calculation | 比吸收率计算

### 10.5.1 SAR Definition (Eq. 6.3) | SAR 定义

$$\text{SAR}(x, y, z) = \frac{\sigma(x, y, z) \cdot |E_{\text{total}}(x, y, z)|^2}{\rho}$$

where: $\sigma$ = tissue conductivity (S/m), $|E_{\text{total}}|$ = total E-field magnitude (V/m), $\rho$ = tissue density (kg/m$^3$), typically $\approx 1000$ kg/m$^3$.
其中 $\sigma$ 为组织电导率，$|E_{\text{total}}|$ 为总电场幅度，$\rho$ 为组织密度。

### 10.5.2 Linear Superposition | 线性叠加原理

All quadrants at 90 MHz — by **linear superposition**:
所有象限以 90 MHz 工作，由**线性叠加原理**：

$$E_{z,\text{total}}(x, y, z) = \sum_{n=1}^{4} \alpha_n \cdot |E_n| \angle (\phi_n + \theta_n) \quad (6.6)$$

where $\alpha_n$ = relative amplitude, $\theta_n$ = phase delay set by operator.
其中 $\alpha_n$ 为相对幅度，$\theta_n$ 为操作者设定的相位延迟。

---

## 10.6 Phase Control Strategy (Eq. 6.7) | 相位控制策略

### 10.6.1 Target Point Selection | 目标点选择

$$\theta_i = 0.1 \times f_{\text{MHz}} \times (\text{dist}_i - \text{dist}_{\max}) \quad (6.7)$$

where: $f_{\text{MHz}}$ = frequency (MHz), $\text{dist}_i$ = distance from target to quadrant $i$, $\text{dist}_{\max}$ = max of the four distances.
其中 $f_{\text{MHz}}$ 为频率，$\text{dist}_i$ 为目标点到第 $i$ 象限距离，$\text{dist}_{\max}$ 为四个距离的最大值。

**Physical interpretation | 物理解释**: The goal is to compensate path-length differences so signals arrive at the target **in phase** (constructive interference).
目标是补偿各象限到目标点的路径差，使各路信号到达目标点时**相位相同**（相长干涉）。

### 10.6.2 Amplitude Control | 幅度设置

Amplitudes $\alpha_n$ are directly set by the operator, normalized so max = 1.
幅度 $\alpha_n$ 由操作者直接指定，最大值归一化为 1。

---

## 10.7 SAR Distribution Visualization (Fig. 6.13) | SAR 分布可视化

Fig. 6.13 shows axial SAR slices under four amplitude settings:
四种幅度设置下的 SAR 分布轴向切片图：

| Setting | [Q1, Q2, Q3, Q4] | Characteristic |
|:--------|:-----------------|:---------------|
| `[0,0] 1 1 1 1` | [1, 1, 1, 1] | Uniform, centered |
| `[-2,0] .9 .9 1.8` | [.9, .9, 1.8, ?] | Off-center peak |
| `[-4,2] 1 .7 1 .7` | [1, .7, 1, .7] | Asymmetric |
| `[4,0] .8 .8 .6 1` | [.8, .8, .6, 1] | Opposite shift |

---

## 10.8 System Workflow Summary | 系统工作流程

```
Patient CT scan
      ↓
fd3d_apa.py (4 independent FDTD runs, one quadrant each)
      ↓
Amplitude A1–A4, Phase P1–P4, σ files
      ↓
super_apa.py (superposition SAR calculation)
Operator specifies [α1,α2,α3,α4] and target (ipos, jpos)
      ↓
SAR color map → clinical decision
```

**Computation time**: Four FDTD runs (~5000 steps each) ≈ **10 minutes** on HP Spectre x360 laptop.

---

## 10.9 Key Parameters | 关键参数汇总

| Parameter | Value | Source |
|:----------|:------|:-------|
| Grid size | $80 \times 80 \times 80$ | p. 161 |
| Cell size | 1 cm$^3$ | p. 161 |
| Frequency | 90 MHz | p. 160 |
| PML thickness | 5 cells | p. 161 |
| Quadrants | 4 | p. 160 |
| Dipoles per quadrant | 2 | p. 160 |
| Simulation steps | 5000 | p. 167 |

---

## 10.10 Clinical Safety Thresholds | SAR 临床安全阈值

| Standard | Local SAR limit | Method |
|:---------|:----------------|:-------|
| IEEE C95.1-2019 | 10 g: 10 W/kg | Spatial peak |
| FCC OET Bull. 65 | 1 g: 1.6 W/kg | Spatial peak |

Clinically, **whole-body SAR** < 1 W/kg to avoid hyperthermia (>39°C).
临床需确保全身 SAR < 1 W/kg，避免体温过高。

---

## 10.11 Why 90 MHz? | 90 MHz 的物理依据

- Wavelength in muscle $\lambda \approx 0.5$ m (small enough for focusing) | 波长足够小实现聚焦
- Penetration depth ~2–3 cm (deep enough for deep tissue) | 穿透深度足够深
- Avoids too-high frequency ($>$300 MHz, skin overheating) | 避免皮肤过热
- Avoids too-low frequency ($<$30 MHz, poor focusing) | 避免聚焦困难

---

## Audit Table | 审计表格

| Item | Source | Status |
|:-----|:------|:------:|
| Sigma 60 system (8 dipoles, 4 quadrants) | raw text p.159 | ✅ |
| Dipole antenna model (gaz=0) | raw text p.161 | ✅ |
| Grid $80\times80\times80$ | raw text p.161 | ✅ |
| Gaussian pulse Eq. 6.2 | raw text p.162 | ✅ |
| CT → tissue mapping | raw text p.163 | ✅ |
| SAR definition Eq. 6.3 | raw text p.167 | ✅ |
| Superposition Eq. 6.4–6.6 | raw text pp.167-168 | ✅ |
| Phase estimation Eq. 6.7 | raw text p.167 | ✅ |
| Four FDTD runs | raw text p.165 | ✅ |
| SAR distribution Fig. 6.13 | raw text p.169 | ✅ |
