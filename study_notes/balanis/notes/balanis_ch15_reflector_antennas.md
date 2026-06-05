> **范围:** §15.1–§15.9 | 量化验证级笔记

---

## §15.1 Introduction

**核心思想:** 反射面天线通过一个或多个反射面将馈源（feed）的球面波前转换为平面波前，实现高方向性。

**面天线 vs 线天线:**

| 特性 | 线天线 | 面天线（反射面） |
|------|--------|-----------------|
| 典型增益 | 2–15 dBi | 15–70 dBi |
| 波束宽度 | 宽 ($>20^\circ$) | 窄 ($<20^\circ$，可小至 $<0.1^\circ$) |
| 分析方法 | 电流分布积分 | 口径场法 / 表面电流法 |
| 工作频段 | HF–Ku | SHF–EHF (典型 > 1 GHz) |

**反射面天线类型综述:**

```
                  ┌─ 单反射面: 抛物面 (paraboloidal)
                  │    ├─ 前馈 (front-fed / prime-focus)
                  │    ├─ 偏馈 (offset-fed)
                  │    └─ 球面 (spherical)
  Reflectors ─────┤
                  ├─ 双反射面: 
                  │    ├─ Cassegrain (双曲面副反射面)
                  │    └─ Gregorian (椭球面副反射面)
                  │
                  └─ 特殊: 赋形反射面 (shaped reflector)
```

**基本问题:**
1. **馈源设计** — 匹配反射面的照射 taper 和边缘电平
2. **遮挡** — 馈源和支撑结构的遮挡降低效率
3. **表面公差** — 机械制造误差导致增益损失
4. **交叉极化** — 偏馈系统固有的交叉极化

---

## §15.2 Parabolic Reflector Geometry

### 抛物面方程

旋转抛物面（paraboloid of revolution）由抛物线绕其焦轴旋转而成。在极坐标系 $(r', \psi, \phi')$ 中：

$$
r' = \frac{2f}{1 + \cos\psi} = \frac{f}{\cos^2(\psi/2)} \quad (\psi \in [0, \pi/2))
$$

其中：
- $f$ — 焦距（focal length）[L]
- $\psi$ — 从焦轴测量的角度（半张角）
- $r'$ — 从焦点到反射面上点的距离 [L]

**直角坐标系：** $z = \frac{x^2 + y^2}{4f}$

### 重要几何参数

| 符号 | 含义 | 关系式 | 量纲 |
|------|------|--------|------|
| $D$ | 口径直径 | $D = 2a$ | [L] |
| $a$ | 口径半径 | $a = D/2$ | [L] |
| $f$ | 焦距 | | [L] |
| $f/D$ | 焦距口径比（关键设计参数） | | [1] |
| $\psi_0$ | 口径半张角 | $\psi_0 = 2 \arctan\left(\frac{D}{4f}\right)$ 或 $\tan(\psi_0/2) = \frac{D}{4f}$ | [rad] |
| $d_s$ | 口径面到焦点的距离 | $d_s = \frac{D^2}{16f}$ | [L] |

**量纲检查:**
- $\tan(\psi_0/2) = D/(4f)$ → [1] = [L]/[L] ✅
- $d_s = D^2/(16f)$ → [L] = [L]²/[L] ✅

### f/D 的物理含义

- **小 f/D (深盘, e.g. 0.25):** $\psi_0$ 大 → 馈源波束宽 → 更多 spillover → 结构紧凑
- **大 f/D (浅盘, e.g. 1.0):** $\psi_0$ 小 → 馈源波束窄 → 低 spillover → 长 focal arm
  
**工程经验:** 典型 $f/D \in [0.25, 1.0]$

### 抛物面的关键性质

1. **等光程性:** 从焦点出发的任何射线到达口径面上的光程相等（$r' + r'\cos\psi = 2f$）
2. **平行出射:** 焦点发出的球面波经反射后变成平行于轴线的平面波
3. **可逆性:** 平行入射波经反射汇聚于焦点

---

## §15.3 Aperture Distribution & Radiation Patterns

### 口径场法 (Aperture Field Method)

**步骤:**
1. 由馈源方向图计算反射面上的入射场
2. 利用几何光学（GO）反射定律得到反射场
3. 将反射场投影到口径平面（aperture plane）
4. 对口径场做傅里叶变换得到远场方向图

### 均匀分布

口径场 $E_a = \text{constant}$:

$$
\mathbf{E}(\theta, \phi) = E_0 \, 2\pi a^2 \frac{e^{-jkr}}{r} \frac{J_1(ka\sin\theta)}{ka\sin\theta}
$$

其中 $a = D/2$。

**方向图特性 (均匀口径):**

| 参数 | 值 |
|------|-----|
| 第一零点 (BWFN) | $2\theta_0 \approx 2\arcsin(1.22\lambda/D) \approx 2.44\lambda/D$ (rad, 小角) |
| 半功率波束宽度 (HPBW) | $\approx 1.02\lambda/D$ (rad) |
| 第一旁瓣电平 (SLL) | $-17.6\,\text{dB}$ |
| 方向性系数 | $D_0 = 4\pi A_p/\lambda^2 = \pi^2 D^2/\lambda^2$ |

**量纲检查:** $D_0 = 4\pi A_p/\lambda^2$ → [1] = [L²]/[L²] ✅

### 锥削分布 (Tapered)

典型锥削分布 $E_a(\rho) = C + (1-C)\left[1 - (\rho/a)^2\right]^n$

**关键影响:**
- 锥削降低 SLL，但展宽 HPBW、降低方向性
- 常见 $n = 1$ 抛物线锥削: SLL $\approx -24.6\,\text{dB}$
- $n = 2$: SLL $\approx -30.6\,\text{dB}$  
- **锥削效率** $\eta_t < 1$

### 方向性系数修正

$$
D_0 = \frac{4\pi}{\lambda^2} \, \varepsilon_{ap} \, A_p
$$

其中 $\varepsilon_{ap}$ 为口径效率（含锥削、相位等损失）。

---

## §15.4 Feed Systems

### 馈源要求

1. **方向图匹配:** 馈源方向图应恰好照射反射面边缘到所需的 taper 电平
2. **低旁瓣/后瓣:** 减少 spillover 和噪声温度
3. **稳定的相位中心:** 相位中心应与抛物面的焦点重合
4. **低交叉极化:** 保持极化纯度

### 常见馈源类型

| 类型 | 工作频段 | 特点 |
|------|---------|------|
| **Horn feed** (角锥/圆锥喇叭) | 宽带 | 最常用，极化纯度高，相位中心稳定 |
| **Dipole feed** (偶极子) | 低频 | 结构简单，带宽较窄 |
| **Waveguide feed** (开口波导) | 毫米波 | 结构紧凑，增益较低 |
| **Corrugated horn** (波纹喇叭) | 宽带 | 对称方向图，低交叉极化 |
| **Dual-mode horn** (双模喇叭) | 窄带 | 改善口径效率 |

### Feed Pattern Taper

馈源方向图通常近似为 $f(\psi) = \cos^q(\psi)$（或 $\cos^n(\psi)$）:

$$
G_f(\psi) = G_0 \begin{cases}
\cos^q(\psi), & 0 \le \psi \le \pi/2 \\
0, & \psi > \pi/2
\end{cases}
$$

$q$ 值决定馈源波束宽度。**边缘 taper (edge taper):**

$$
\text{Edge Taper (dB)} = 10\log_{10}\left[\cos^q(\psi_0)\right]
$$

工程中 edge taper 通常选择 $-10$ 到 $-15$ dB。

### Spillover 效率

馈源发出的能量中，未射到反射面而被"漏掉"的部分定义为 spillover:

$$
\eta_{\text{spill}} = \frac{\int_0^{\psi_0} G_f(\psi) \sin\psi \, d\psi}{\int_0^{\pi} G_f(\psi) \sin\psi \, d\psi}
$$

### 效率与 f/D 的权衡

- 小 f/D: $\psi_0$ 大 → spillover 小 √, 但 taper 效率低 ×
- 大 f/D: $\psi_0$ 小 → taper 效率高 √, 但 spillover 大 ×
- **最优:** 在 $\eta_{\text{spill}}$ 和 $\eta_{\text{taper}}$ 之间平衡 → 最大化 $\eta_t \times \eta_{\text{spill}}$

---

## §15.5 Dual-Reflector Systems

### Cassegrain

**结构:** 主反射面（抛物面）+ 副反射面（双曲面，convex）

```
            ┌─────────────┐
            │  Paraboloid │ (主反射面)
            │             │
            │  ┌───────┐  │
            │  │Hyperb.│  │ (副反射面, 凸面)
            │  └───────┘  │
            │   ╱  point  │
            │  F₁    F₂   │ (F₁=抛物面焦点, F₂=双曲面另一焦点=馈源相位中心)
            └─────────────┘
```

**几何关系:**

- 双曲面的两个焦点: 一个与主反射面焦点重合（$F_1$），另一个放置馈源相位中心（$F_2$）
- 双曲面偏心率 $e > 1$

### Gregorian

**结构:** 主反射面（抛物面）+ 副反射面（椭球面，concave）

- 椭球面的两个焦点: $F_1$（主反射面焦点）+ $F_2$（馈源相位中心）
- 椭球偏心率 $e < 1$

### 等效抛物面原理

双反射面系统可用一个**等效的单反射面**表示:

$$
f_e = e \cdot f_m \quad (\text{Cassegrain})
$$

其中 $f_m$ 为主反射面焦距，$e$ 为双曲面偏心率。

**等效 $f/D$:** $f_e/D = e \cdot (f_m/D)$

由于 $e > 1$，Cassegrain 的等效 f/D 大于实际 f/D。这意味着：
- 更低的 spillover
- 馈源可以放在主反射面后面（方便安装低噪声放大器）
- 等效焦距长但物理结构紧凑

**双反射面的优势:**
1. 减少馈线损耗（LNA 可安装在后）
2. 等效 f/D 大 → 设计更灵活
3. 可赋形改善口径效率

---

## §15.6 Offset-Fed Reflectors

### 动机

前馈（front-fed）反射面的主要问题:
- **馈源遮挡** — 降低增益、增加旁瓣
- **支撑结构散射** — 降低效率

### 偏馈结构

将馈源移出反射面主波束路径，同时仅使用反射面的一部分。

**偏馈设计参数:**
- $D$ — 投影口径直径 [L]
- $f$ — 焦距 [L]
- $h$ — 偏置高度（馈源到口径投影中心的偏移）[L]
- $\psi_c$ — 偏置角

**优点:**
- ✅ 无遮挡 → 旁瓣更低、效率更高
- ✅ 馈源和支撑结构不与主波束交互

**缺点:**
- ❌ **固有交叉极化** — 对称性破缺导致交叉极化分量
- ❌ 大偏置时方向图不对称增加

### 交叉极化补偿方法

1. 使用双偏馈或双反射面偏馈
2. 使用波纹喇叭馈源抑制交叉极化
3. 赋形反射面补偿

---

## §15.7 Spherical Reflectors

### 球面反射面的问题

球面反射面制造简单（所有曲率半径相等），但存在**球差 (spherical aberration)** — 即从焦点发出的射线经不同环形区域反射后不交于同一点。

### 补偿方法

1. **Luneburg Lens:** 渐变介电常数透镜补偿球差
   
   $$
   \epsilon_r(r) = 2 - (r/R)^2
   $$
   
   其中 $R$ 为透镜半径。

2. **带状馈源 (line feed):** 沿焦轴移动馈源实现不同环形区域的补偿

### 应用

- 射电天文（Arecibo 305米球面望远镜 — 现已升级改造）
- 多波束接收天线

---

## §15.8 Aperture Efficiency

### 总效率分解

$$
\eta_{\text{total}} = \eta_{\text{spill}} \times \eta_{\text{taper}} \times \eta_{\text{phase}} \times \eta_{\text{blockage}} \times \eta_{\text{surf}} \times \eta_{\text{pol}}
$$

| 效率分量 | 符号 | 物理含义 | 典型值 |
|---------|------|---------|--------|
| Spillover efficiency | $\eta_{\text{spill}}$ | 馈源能量照射到反射面的比例 | 0.85–0.95 |
| Taper efficiency | $\eta_{\text{taper}}$ | 口径场分布均匀度 | 0.75–0.90 |
| Phase efficiency | $\eta_{\text{phase}}$ | 口径场相位均匀度 | 0.90–0.99 |
| Blockage efficiency | $\eta_{\text{blockage}}$ | 馈源/支撑遮挡损失 | 0.90–0.98 |
| Surface error efficiency | $\eta_{\text{surf}}$ | 反射面表面误差 | 0.80–0.99 |
| Cross-pol efficiency | $\eta_{\text{pol}}$ | 极化纯度 | 0.95–0.99 |

**总口径效率:** 典型值 $\eta_{\text{total}} = 0.55$–$0.75$ ($55\%$–$75\%$)

### Spillover 效率 (详细)

$$
\eta_{\text{spill}} = \frac{\int_0^{\psi_0} G_f(\psi) \sin\psi \, d\psi}{\int_0^{\pi} G_f(\psi) \sin\psi \, d\psi}
$$

对于 $\cos^q(\psi)$ 馈源:

分母: $\int_0^{\pi/2} \cos^q(\psi) \sin\psi \, d\psi = \frac{1}{q+1}$ (馈源只向前半球 $\psi \le \pi/2$ 辐射)

分子: $\int_0^{\psi_0} \cos^q(\psi) \sin\psi \, d\psi = \frac{1 - \cos^{q+1}(\psi_0)}{q+1}$

因此:

$$
\eta_{\text{spill}} = 1 - \cos^{q+1}(\psi_0)
$$

### Taper (Illumination) 效率

$$
\eta_{\text{taper}} = \frac{\left[\iint_A E_a(\rho) \, dS\right]^2}{A_p \iint_A E_a^2(\rho) \, dS}
$$

对于轴对称口径:

$$
\eta_{\text{taper}} = \frac{2\left[\int_0^a E_a(\rho) \rho \, d\rho\right]^2}{a^2 \int_0^a E_a^2(\rho) \rho \, d\rho}
$$

**物理含义:** 均匀分布 ($E_a = \text{const}$) 时 $\eta_{\text{taper}} = 1$。锥削越强，$\eta_{\text{taper}}$ 越低。

---

## §15.9 Surface Error Tolerance

### Ruze 公式

反射面表面的随机误差会导致增益损失。Ruze (1966) 给出了统计结果:

$$
\frac{G}{G_0} = e^{-(4\pi \varepsilon/\lambda)^2} = \eta_{\text{surf}}
$$

其中:
- $G_0$ — 理想表面增益
- $G$ — 实际表面增益
- $\varepsilon = \sqrt{\langle \delta^2 \rangle}$ — RMS 表面误差（均方根）[L]
- $\delta$ — 表面相对于理想抛物面的法向偏差
- 假设: 误差$\,\delta\,$是零均值高斯分布且相关长度 $\gg \lambda$

### 增益损失 (dB)

$$
\Delta G \,(\text{dB}) = -10\log_{10}\left[e^{-(4\pi\varepsilon/\lambda)^2}\right] = 686\left(\frac{\varepsilon}{\lambda}\right)^2
$$

**工程常用近似:** $\varepsilon \le \lambda/16$ 时损失 < 0.3 dB；$\varepsilon = \lambda/30$ 时损失可忽略。

### Ruze 公式工程表格

| $\varepsilon/\lambda$ | $\Delta G$ (dB) | 评价 |
|----------------------|-----------------|------|
| $1/100$ | 0.07 | 极好 |
| $1/50$ | 0.27 | 好 |
| $1/30$ | 0.76 | 可接受 |
| $1/20$ | 1.71 | 差 |
| $1/10$ | 6.86 | 不可接受 |

**量纲检查:** $(4\pi\varepsilon/\lambda)^2$ 中 $\varepsilon/\lambda$ 为 [1] ✅

### 表面误差对工作频率的限制

给定 RMS 表面误差 $\varepsilon$，可使用 Ruze 公式反推最高可用频率（$f_{\max}$ 对应 $\Delta G_{\max}$）。

---


| 编号 | 公式 | 描述 |
|------|------|------|
| (15-1) | $r' = 2f/(1+\cos\psi)$ | 抛物面极坐标方程 |
| (15-2) | $\tan(\psi_0/2) = D/(4f)$ | 半张角与 f/D 关系 |
| (15-17) | $\text{HPBW} \approx 1.02\lambda/D$ | 均匀口径 HPBW |
| (15-18a) | $D_0 = \pi^2 D^2/\lambda^2$ | 均匀口径方向性 |
| (15-36) | $\eta_{\text{spill}} = 1 - \cos^{q+1}(\psi_0)$ | Spillover 效率 ($\cos^q$馈源) |
| (15-50) | $f_e = e \cdot f_m$ | Cassegrain 等效焦距 |
| Ruze | $G/G_0 = \exp[-(4\pi\varepsilon/\lambda)^2]$ | 表面误差增益损失 |

---


1. **确定需求:** $G_{\min}$, HPBW, SLL $_{\max}$, 工作频率 $f$
2. **选 f/D:** 权衡 spillover 和 taper，初选 $f/D \approx 0.3$–$0.5$
3. **计算 D:** $D \approx \lambda\sqrt{D_0/\pi^2}$ (从增益需求)
4. **设计馈源:** 确定 $q$ (或 edge taper) 匹配 $\psi_0$
5. **计算效率:** $\eta_{\text{total}} = \prod \eta_i$，验算增益
6. **表面公差:** 确定 $\varepsilon_{\max}$ 使 $\Delta G$ 可接受
7. **双反射面设计 (可选):** 确定 $e$, $f_m$, 副反射面尺寸

---

*笔记结束 | 对应 Balanis 4th Ed. Ch15 §15.1–§15.9*
