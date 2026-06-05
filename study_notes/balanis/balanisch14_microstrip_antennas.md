# Chapter 14: Microstrip Antennas

> Balanis, *Antenna Theory: Analysis and Design*, 4th Edition — Chapter 14

---

## 14.1 Introduction

微带天线（Microstrip Antenna / Patch Antenna）由一薄层介质基片上的金属贴片和背面接地平面构成，是当代最广泛使用的天线形式之一。

**核心结构参数：**
- 贴片（Patch）：铜或金，厚度 $t \ll \lambda_0$
- 介质基片：厚度 $h$（典型 $0.003\lambda_0 \le h \le 0.05\lambda_0$），介电常数 $2.2 \le \epsilon_r \le 12$
- 接地平面（Ground Plane）

**典型贴片形状：** 矩形、圆形、圆环形、三角形、偶极子形

**优势：**
- 低剖面，可共形（conformal）安装
- 制造简单（PCB 工艺），成本低
- 易于阵列集成
- 可同时实现多种极化

**劣势：**
- 带宽窄（典型 1–5%）
- 增益有限（典型 5–8 dBi）
- 表面波损耗
- 功率容量低

---

## 14.2 馈电方法 (Feeding Methods)

### 14.2.1 微带线馈电 (Microstrip Line Feed)

金属馈线与贴片共面，通过插入/级联匹配。

$$
Z_{\text{in}}(y_0) = Z_{\text{in}}(0) \cos^2\left(\frac{\pi}{L} y_0\right)
$$

### 14.2.2 同轴探针馈电 (Coaxial Probe Feed)

内导体穿过基片连接贴片，外导体接地。优势是馈电点可选任意位置，但制造复杂（需焊接）。

### 14.2.3 孔径耦合馈电 (Aperture-Coupled Feed)

通过接地平面上的小孔（slot）耦合能量到贴片。馈线在另一层介质上。优势是馈电网络与辐射体隔离，减少 spurious radiation。

### 14.2.4 邻近耦合馈电 (Proximity-Coupled Feed)

馈线端在两层介质之间，贴片在顶层，通过电磁耦合馈电。带宽宽（可达 13%），但制造难度大。

---

## 14.3 传输线模型 (Transmission-Line Model)

将矩形贴片视为两条平行辐射缝隙（slot），缝隙长度为 $W$，宽度为 $h$，间距为 $L$。

### 14.3.1 有效介电常数 (Effective Dielectric Constant)

由于边缘场（fringing fields），部分场在介质外传播：

$$
\epsilon_{reff} = \frac{\epsilon_r + 1}{2} + \frac{\epsilon_r - 1}{2} \left[1 + 12\frac{h}{W}\right]^{-1/2}, \quad W/h \gg 1
\tag{14-1}
$$

### 14.3.2 边缘场延伸长度 (Fringing Extension Length)

两端的边缘场使贴片电长度增加 $\Delta L$：

$$
\frac{\Delta L}{h} = 0.412 \frac{(\epsilon_{reff} + 0.3)(W/h + 0.264)}{(\epsilon_{reff} - 0.258)(W/h + 0.8)}
\tag{14-2}
$$

**有效长度：**

$$
L_{\text{eff}} = L + 2\Delta L
\tag{14-3}
$$

### 14.3.3 谐振频率 (Resonant Frequency)

**TM$_{010}$ 主模（不考虑边缘场）：**

$$
(f_r)_{010} = \frac{1}{2L\sqrt{\epsilon_r}\sqrt{\mu_0\epsilon_0}} = \frac{c}{2L\sqrt{\epsilon_r}}
\tag{14-4}
$$

**考虑边缘场修正：**

$$
(f_{rc})_{010} = \frac{1}{2L_{\text{eff}}\sqrt{\epsilon_{reff}}\sqrt{\mu_0\epsilon_0}} = \frac{c}{2L_{\text{eff}}\sqrt{\epsilon_{reff}}}
\tag{14-5}
$$

### 14.3.4 贴片宽度设计 (Patch Width)

为提高辐射效率，宽度设计为：

$$
W = \frac{c}{2f_r}\sqrt{\frac{2}{\epsilon_r + 1}}
\tag{14-6}
$$

### 14.3.5 缝隙导纳 (Slot Admittance)

每个缝隙的导纳由串联电导 $G_1$ 和电纳 $B_1$ 构成：

$$
G_1 = \frac{W}{120\lambda_0}\left[1 - \frac{1}{24}(k_0 h)^2\right], \quad \frac{h}{\lambda_0} < \frac{1}{10}
\tag{14-8a}
$$

$$
B_1 = \frac{W}{120\lambda_0}\left[1 - 0.636\ln(k_0 h)\right], \quad \frac{h}{\lambda_0} < \frac{1}{10}
\tag{14-8b}
$$

更精确的 $G_1$（积分形式）：

$$
I_1 = -2 + \cos(X) + X\,S_i(X) + \frac{\sin X}{X}
$$
$$
G_1 = \frac{I_1}{120\pi^2}
$$

其中 $X = k_0 W$，$S_i(\cdot)$ 为正弦积分。

### 14.3.6 互导纳 (Mutual Conductance)

两缝隙间的互导纳：

$$
G_{12} = \frac{1}{120\pi^2} \int_0^\pi \left[\frac{\sin\left(\frac{k_0 W}{2}\cos\theta\right)}{\cos\theta}\right]^2 J_0(k_0 L \sin\theta) \sin^3\theta\,d\theta
\tag{14-12}
$$

### 14.3.7 输入阻抗 (Input Impedance)

谐振时总输入电阻（无耦合时）：

$$
R_{\text{in}} = \frac{1}{2G_1}
\tag{14-16}
$$

考虑缝隙耦合：

$$
R_{\text{in}} = \frac{1}{2(G_1 \pm G_{12})}
\tag{14-17}
$$

其中 "$+$" 用于奇对称模，"$-$" 用于偶对称模。

**内缩馈电 (Inset Feed)：** 输入电阻随馈电点位置 $y_0$ 变化：

$$
R_{\text{in}}(y_0) = R_{\text{in}}(0) \cos^2\left(\frac{\pi}{L} y_0\right) = \frac{1}{2(G_1 \pm G_{12})} \cos^2\left(\frac{\pi}{L} y_0\right)
\tag{14-20a}
$$

### 14.3.8 方向性 (Directivity)

基于缝隙模型，方向性可表示为：

$$
D_0 = \frac{2\pi W}{\lambda_0^2} \frac{1}{I_1} \cdot \frac{2}{1 + g_{12}}
$$

其中 $g_{12} = G_{12}/G_1$。

E 平面（$\phi = 0$，$\theta$ 从 z 轴测量）和 H 平面（$\theta = \pi/2$，$\phi$ 从 x 轴测量）的远场方向图：

**E 平面 ($xz$ 平面, $\phi=0$)：**
$$
E_\theta = \frac{j k_0 W V_0 e^{-j k_0 r}}{\pi r} \cdot \frac{\sin\left(\frac{k_0 h}{2} \sin\theta\right)}{\frac{k_0 h}{2} \sin\theta} \cdot \cos\left(\frac{k_0 L_{\text{eff}}}{2} \sin\theta\right)
\tag{14-26}
$$

**H 平面 ($xy$ 平面, $\theta=\pi/2$)：**
$$
E_\phi = \frac{j k_0 W V_0 e^{-j k_0 r}}{\pi r} \cdot \frac{\sin\left(\frac{k_0 h}{2} \sin\phi\right)}{\frac{k_0 h}{2} \sin\phi} \cdot \frac{\sin\left(\frac{k_0 W}{2} \cos\phi\right)}{\frac{k_0 W}{2} \cos\phi} \cdot \cos\phi
\tag{14-27}
$$

### 14.3.9 矩形贴片设计流程

**给定：** $\epsilon_r$、$f_r$、$h$

1. 计算贴片宽度 $W$（式 14-6）
2. 计算有效介电常数 $\epsilon_{reff}$（式 14-1）
3. 计算边缘延伸 $\Delta L$（式 14-2）
4. 计算实际贴片长度 $L = \frac{c}{2f_r\sqrt{\epsilon_{reff}}} - 2\Delta L$
5. 计算有效长度 $L_{\text{eff}} = L + 2\Delta L$
6. 计算接地平面尺寸：$L_g = L + 6h$，$W_g = W + 6h$

**设计实例 (Example 14.1):** $\epsilon_r = 2.2$ (RT/duroid 5880), $h = 0.1588$ cm, $f_r = 10$ GHz
- $W = 1.186$ cm, $\epsilon_{reff} = 1.647$, $\Delta L = 0.036$ cm
- $L = 0.906$ cm, $L_{\text{eff}} = 0.978$ cm

---

## 14.4 腔体模型 (Cavity Model)

将贴片与接地平面之间的区域视为一个磁壁（magnetic wall）围成的谐振腔。

### 14.4.1 矩形贴片腔体模型

腔体边条件：上下电壁（PEC），四周磁壁（PMC）。

腔内电场（TM$_{z}$ 模）：

$$
E_z = E_0 \cos\left(\frac{m\pi}{L}x\right) \cos\left(\frac{n\pi}{W}y\right) \cos\left(\frac{p\pi}{h}z\right)
$$

谐振频率：

$$
(f_r)_{mnp} = \frac{1}{2\pi\sqrt{\mu_0\epsilon_0\epsilon_r}} \sqrt{\left(\frac{m\pi}{L}\right)^2 + \left(\frac{n\pi}{W}\right)^2 + \left(\frac{p\pi}{h}\right)^2}
$$

**TM$_{010}$ 模（$m=0, n=1, p=0$ 或 $m=1, n=0, p=0$）：**

当 $L > W$，主模为 TM$_{010}$（$m=0, n=1, p=0$），电场沿 $z$ 方向不变：

$$
(f_r)_{010} = \frac{1}{2L\sqrt{\mu_0\epsilon_0\epsilon_r}}
\tag{14-33}
$$

当 $W > L$，主模为 TM$_{001}$：

$$
(f_r)_{001} = \frac{1}{2W\sqrt{\mu_0\epsilon_0\epsilon_r}}
\tag{14-34}
$$

**高次模：**

TM$_{020}$（$m=0, n=2$）：

$$
(f_r)_{020} = \frac{1}{L\sqrt{\mu_0\epsilon_0\epsilon_r}}
\tag{14-35}
$$

### 14.4.2 圆形贴片腔体模型 (Circular Patch)

圆形贴片半径为 $a$，同样适用磁壁腔体模型。

**TM$_{nm}$ 模的电场：**

$$
E_z = E_0 J_n(k_{nm}\rho) \cos(n\phi)
$$

其中 $J_n$ 为 $n$ 阶贝塞尔函数。

磁壁边界条件 $H_\phi = 0$ 在 $\rho = a$ 处相当于 $J_n'(k_{nm}a) = 0$。

**主模 TM$_{110}$：** 最小的根为 $J_1'(k_{11}a) = 0 \Rightarrow k_{11} = 1.8412 / a$

**谐振频率 (TM$_{110}$)：**

$$
(f_r)_{110} = \frac{1.8412 c}{2\pi a \sqrt{\epsilon_r}}
\tag{14-66}
$$

**考虑边缘场修正的实际半径：**

$$
a_e = a \left[1 + \frac{2h}{\pi\epsilon_r a}\left(\ln\frac{\pi a}{2h} + 1.7726\right)\right]^{1/2}
\tag{14-67}
$$

修正后的谐振频率：

$$
(f_{rc})_{110} = \frac{1.8412 c}{2\pi a_e \sqrt{\epsilon_r}}
$$

**圆形贴片设计（Example 14.4）：** $\epsilon_r=2.2$, $h=0.1588$ cm, $f_r=10$ GHz
$$
F = \frac{8.791\times 10^9}{f_r \sqrt{\epsilon_r}}
$$
$$
a = \frac{F}{\left[1 + \frac{2h}{\pi\epsilon_r F}\left(\ln\frac{\pi F}{2h} + 1.7726\right)\right]^{1/2}}
$$

设计结果：$a = 0.525$ cm

---

## 14.5 品质因数、带宽与效率 (Q, Bandwidth, Efficiency)

### 14.5.1 品质因数 (Quality Factor)

总品质因数由四个分量决定：

$$
\frac{1}{Q_T} = \frac{1}{Q_{\text{rad}}} + \frac{1}{Q_c} + \frac{1}{Q_d} + \frac{1}{Q_{\text{sw}}}
$$

- $Q_{\text{rad}}$：辐射损耗

矩形贴片近似：

$$
Q_{\text{rad}} = \frac{2\omega \epsilon_r}{h G_t / L}
$$

- $Q_c = h\sqrt{\pi f \mu_0 \sigma}$：导体损耗（$\sigma$ 为电导率）
- $Q_d = 1/\tan\delta$：介质损耗（$\tan\delta$ 为损耗角正切）
- $Q_{\text{sw}}$：表面波损耗（厚基片明显）

### 14.5.2 带宽 (Bandwidth)

$$
\text{BW} = \frac{VSWR - 1}{Q_T \sqrt{VSWR}} \times 100\%
\tag{14-68}
$$

对于 $VSWR = 2$：

$$
\text{BW} \approx \frac{1}{Q_T\sqrt{2}} \times 100\%
$$

（Example 14.5：$f_c=10$ GHz, $\text{BW}=5\%$, VSWR=2 $\Rightarrow Q_T = 14.14$）

### 14.5.3 辐射效率 (Radiation Efficiency)

$$
e = \frac{P_{\text{rad}}}{P_{\text{in}}} = \frac{Q_T}{Q_{\text{rad}}}
$$

---

## 14.6 馈电技术详解

### 14.6.1 微带线馈电 (Microstrip Feed)

- 馈线与贴片共面
- 通过插入深度控制阻抗匹配
- 缺点：馈线自身辐射（spurious radiation）

### 14.6.2 同轴探针馈电 (Coaxial Probe Feed)

- 内导体穿过基片到贴片
- 易于匹配（选择合适的馈电点 $y_0$）
- 缺点：探针引入电感，在厚基片时带宽受限

### 14.6.3 孔径耦合馈电 (Aperture Coupling)

- 馈线与贴片在不同介质层
- 通过接地平面上的槽耦合
- 优点：隔离馈电辐射，设计自由度大

### 14.6.4 邻近耦合馈电 (Proximity Coupling)

- 馈线在两层基片之间
- 带宽最宽（可达 13–20%）
- 制造复杂

---

## 14.7 圆极化 (Circular Polarization)

### 14.7.1 单馈电法 (Single-Feed CP)

通过微扰贴片几何激发两个正交简并模。常用方法：
- 截角（Truncated corners）矩形贴片
- 对角馈电的近方形贴片 ($L \approx 1.03W$)
- 开槽（Slotted）贴片

轴比 (Axial Ratio)：

$$
AR = \left|\frac{E_L}{E_R}\right| = \sqrt{\frac{1 + |\rho|^2 + 2|\rho|\cos(\Delta\phi)}{1 + |\rho|^2 - 2|\rho|\cos(\Delta\phi)}}
$$

### 14.7.2 双馈电法 (Dual-Feed CP)

使用 $90^\circ$ 混合耦合器（如分支线耦合器、Lange 耦合器）产生等幅 $90^\circ$ 相差信号馈入两个正交馈电点。带宽更宽，但需要额外馈电网络。

---

## 14.8 宽带技术 (Broadbanding Techniques)

### 14.8.1 增大基片厚度

- 增加 $h$ 降低 $Q$，提高带宽
- 但过厚会导致表面波激发和馈电电感过大

### 14.8.2 降低介电常数

- 低 $\epsilon_r$（如空气 $\epsilon_r=1$）提供更宽带宽
- 但贴片尺寸增大

### 14.8.3 叠层贴片 (Stacked Patches)

两个或更多贴片垂直层叠，谐振频率略微错开，扩展带宽（可达 15–30%）。

### 14.8.4 U 形槽贴片 (U-Slot Patch)

在贴片上开 U 形槽引入额外谐振，扩展带宽（可达 20–40%）。

### 14.8.5 L 形探针馈电 (L-Probe Feed)

弯折探针降低探针电感，与空气基片配合可实现超过 35% 带宽。

### 14.8.6 缝隙加载 (Slot Loading)

在贴片上开不同形状的槽（如 V 形、H 形、E 形）引入多谐振。

---

## 14.9 微带天线阵 (Microstrip Arrays)

### 14.9.1 串联馈电阵 (Series-Fed Array)

贴片通过微带线串联连接，相邻贴片间距 $\lambda_g$ 或 $2\lambda_g$。

阵因子：

$$
AF(\theta) = \sum_{n=0}^{N-1} e^{j n (k d \cos\theta + \beta)}
$$

其中 $\beta$ 为相邻单元间馈电相位差。

### 14.9.2 并联馈电阵 (Corporate-Fed Array)

使用分路器（T 型接头、Wilkinson 功分器）等幅等相馈电。带宽优于串联馈电。

### 14.9.3 阵列方向图

考虑贴片单元因子 $f(\theta, \phi)$ 和阵因子 $AF(\theta, \phi)$：

$$
F(\theta, \phi) = f(\theta, \phi) \times AF(\theta, \phi)
$$

### 14.9.4 互耦 (Mutual Coupling)

贴片间通过空间波和表面波耦合。互耦影响阵列的阻抗匹配和扫描能力。

---

## 14.10 其他拓扑结构

### 14.10.1 四分之一波长贴片 (Quarter-Wave Patch)

一半长度由短路壁替代，长度减半。适合小型化应用。

### 14.10.2 PIFA (Planar Inverted-F Antenna)

短路壁加馈电探针的结构，广泛用于移动终端。

### 14.10.3 圆环贴片 (Annular-Ring Patch)

圆环形状，可工作于 TM$_{01}$、TM$_{11}$、TM$_{21}$ 等多个模，提供多频或宽带能力。

### 14.10.4 CPW 馈电贴片 (CPW-Fed Patch)

共面波导馈电，易于集成有源器件。

---

## 关键公式总结

| 公式 | 含义 | 编号 |
|:----|:------|:----:|
| $\epsilon_{reff} = \frac{\epsilon_r+1}{2} + \frac{\epsilon_r-1}{2}(1+12h/W)^{-1/2}$ | 有效介电常数 | (14-1) |
| $\Delta L/h = 0.412\frac{(\epsilon_{reff}+0.3)(W/h+0.264)}{(\epsilon_{reff}-0.258)(W/h+0.8)}$ | 归一化边缘延伸长度 | (14-2) |
| $L_{\text{eff}} = L + 2\Delta L$ | 有效长度 | (14-3) |
| $(f_r)_{010} = c/(2L\sqrt{\epsilon_r})$ | 主模谐振频率（无修正） | (14-4) |
| $(f_{rc})_{010} = c/(2L_{\text{eff}}\sqrt{\epsilon_{reff}})$ | 主模谐振频率（修正） | (14-5) |
| $W = \frac{c}{2f_r}\sqrt{2/(\epsilon_r+1)}$ | 矩形贴片宽度 | (14-6) |
| $G_1 = W/(120\lambda_0)[1 - (k_0h)^2/24]$ | 缝隙电导 | (14-8a) |
| $R_{\text{in}} = 1/[2(G_1 \pm G_{12})]$ | 谐振输入电阻 | (14-17) |
| $R_{\text{in}}(y_0) = R_{\text{in}}(0)\cos^2(\pi y_0/L)$ | 内缩馈电输入电阻 | (14-20a) |
| $(f_r)_{110} = 1.8412c/(2\pi a_e\sqrt{\epsilon_r})$ | 圆形贴片 TM$_{110}$ 谐振频率 | (14-66) |
| $a_e = a[1 + 2h/(\pi\epsilon_r a)(\ln(\pi a/(2h)) + 1.7726)]^{1/2}$ | 圆形贴片有效半径 | (14-67) |
| $Q_T = (VSWR - 1)/(\text{BW}\sqrt{VSWR})$ | 品质因数与带宽关系 | (14-68) |
| $1/Q_T = 1/Q_{\text{rad}} + 1/Q_c + 1/Q_d + 1/Q_{\text{sw}}$ | 总品质因数分解 | |
| $E_\theta \propto \cos(k_0 L_{\text{eff}}\sin\theta/2) \cdot \text{sinc}(k_0 h\sin\theta/2)$ | E 平面方向图 | (14-26) |
| $E_\phi \propto \sin(k_0 W\cos\phi/2)/(k_0 W\cos\phi/2) \cdot \cos\phi$ | H 平面方向图 | (14-27) |

---

## 工程应用指南

1. **频率与基片选择：** 高频（> 10 GHz）常用 $\epsilon_r = 2.2–3.5$，低频可用更高 $\epsilon_r$ 缩小尺寸
2. **带宽扩展：** 带宽需求 > 5% 时考虑叠层或 U 形槽结构
3. **圆极化：** 单馈截角法适合窄带 CP，双馈电法适合宽带 CP
4. **阵列设计：** 并联馈电波束指向稳定，串联馈电馈线损耗低
5. **小型化：** $\lambda/4$ 贴片、PIFA、高介电常数基片

---

## 参考文献

1. C. A. Balanis, *Antenna Theory: Analysis and Design*, 4th ed. Wiley, 2016, Ch. 14.
2. K. R. Carver and J. W. Mink, "Microstrip Antenna Technology," *IEEE Trans. Antennas Propagat.*, vol. AP-29, no. 1, pp. 2–24, Jan. 1981.
3. J. R. James and P. S. Hall, *Handbook of Microstrip Antennas*, IEE, 1989.
4. D. M. Pozar, "Microstrip Antennas," *Proc. IEEE*, vol. 80, no. 1, pp. 79–91, Jan. 1992.
5. D. R. Jackson and N. G. Alexopoulos, "Simple Approximate Formulas for Input Resistance, Bandwidth, and Efficiency of a Resonant Rectangular Patch," *IEEE Trans. Antennas Propagat.*, vol. 39, no. 3, pp. 407–410, 1991.
6. E. O. Hammerstad, "Equations for Microstrip Circuit Design," in *Proc. 5th European Microwave Conf.*, pp. 268–272, 1975.
7. R. Garg, P. Bhartia, I. Bahl, and A. Ittipiboon, *Microstrip Antenna Design Handbook*, Artech House, 2001.
