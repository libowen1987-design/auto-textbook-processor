# Chapter 7: Antennas

> **中英双语版**

Antennas are central to EMC—intentional radiators (AM/FM/radar) generate fields that couple to sensitive circuits and also serve as calibrated measurement devices for regulatory compliance. Unintentional antennas (PCB traces, enclosure seams, cables) produce the emissions we seek to suppress.
天线是EMC的核心——有意辐射体（AM/FM/雷达）产生的场會耦合到敏感电路，同时天线也用作合规测试的校准测量设备。无意天线（PCB走线、机箱缝隙、电缆）则产生我们试图抑制的发射。

---

## 7.1 Elemental Dipole Antennas / 基本偶极子天线

### 7.1.1 The Hertzian (Electric) Dipole / 赫兹（电）偶极子

The Hertzian dipole is an **infinitesimally short** current element of length $dl$ carrying phasor current $\hat{I}$ (uniform along the element), in a spherical coordinate system $(r,\theta,\phi)$.
赫兹偶极子是一段**无限短**的电流元，长度为 $dl$，携带相量电流 $\hat{I}$（沿电流元均匀分布），采用球坐标系 $(r,\theta,\phi)$。

**Complete field components / 完整场分量** [from (7.1)]：

**Magnetic field / 磁场：**
$$
\hat{H}_r = 0,\quad \hat{H}_\theta = 0,\quad 
\hat{H}_\phi = \frac{\hat{I}\,dl}{4\pi r^2}\sin\theta\left(j\frac{1}{\beta_0 r}+\frac{1}{\beta_0^2 r^2}\right)e^{-j\beta_0 r} \tag{7.1c}
$$

**Electric field / 电场：**
$$
\hat{E}_r = \frac{\hat{I}\,dl}{4\pi\eta_0\beta_0^2}\cos\theta\left(\frac{1}{\beta_0^2 r^3}-j\frac{1}{\beta_0 r^2}\right)e^{-j\beta_0 r},\quad
\hat{E}_\theta = \frac{\hat{I}\,dl}{4\pi\eta_0\beta_0^2}\sin\theta\!\left(j\frac{1}{\beta_0 r}+\frac{1}{\beta_0^2 r^2}-j\frac{1}{\beta_0^3 r^3}\right)e^{-j\beta_0 r},\quad
\hat{E}_\phi = 0 \tag{7.1d–f}
$$

where $\beta_0=2\pi/\lambda_0$, $\eta_0=\sqrt{\mu_0/\varepsilon_0}=120\pi$ Ω.
其中 $\beta_0=2\pi/\lambda_0$，$\eta_0=\sqrt{\mu_0/\varepsilon_0}=120\pi$ Ω。

**Near field vs. far field / 近场与远场：** The $1/r^3$, $1/r^2$ terms dominate near the antenna; only the $1/r$ terms survive at large distances. The approximate boundary is $r\gtrsim\lambda_0/6$. More generally / $1/r^3$、$1/r^2$ 项在近天线区域占主导；远距离时仅 $1/r$ 项保留。近似边界为 $r\gtrsim\lambda_0/6$。更一般地：
$$
r_{\text{far}}>\max\!\left(3\lambda_0,\;\frac{2D^2}{\lambda_0}\right)
$$
Use $3\lambda_0$ for wire-type antennas and $2D^2/\lambda_0$ for surface-type antennas (horns, parabolic dishes).
线天线使用 $3\lambda_0$，面天线（喇叭、抛物面）使用 $2D^2/\lambda_0$。

### Far-Field Approximation (Retaining Only $1/r$ Terms) / 远场近似（仅保留 $1/r$ 项）

For $r\gg\lambda_0$ / 当 $r\gg\lambda_0$：
$$
\hat{\mathbf{E}}_{\text{far}} = j\eta_0\beta_0\frac{\hat{I}\,dl}{4\pi r}\sin\theta\,e^{-j\beta_0 r}\,\hat{a}_\theta
= j\frac{\eta_0}{2}\frac{\hat{I}\,dl}{\lambda_0 r}\sin\theta\,e^{-j\beta_0 r}\,\hat{a}_\theta \tag{7.2a}
$$
$$
\hat{\mathbf{H}}_{\text{far}} = \frac{\hat{\mathbf{E}}_{\text{far}}}{\eta_0}\times\hat{a}_r
= j\beta_0\frac{\hat{I}\,dl}{4\pi r}\sin\theta\,e^{-j\beta_0 r}\,\hat{a}_\phi \tag{7.2b}
$$

**Key properties / 关键性质：**
1. $|\hat{E}|/|\hat{H}|=\eta_0$ (wave impedance = free space intrinsic impedance / 波阻抗=自由空间本征阻抗)
2. $\hat{\mathbf{E}}\perp\hat{\mathbf{H}}\perp\hat{a}_r$ (locally transverse and orthogonal / 局部横向且正交)
3. Fields $\propto 1/r$, $\hat{I}$, $dl$, $\sin\theta$ / 场正比于 $1/r$、$\hat{I}$、$dl$、$\sin\theta$
4. **Inverse-distance rule / 反距离法则**：If both $D_1$ and $D_2$ are in the far field, $|E_{D2}|=(D_1/D_2)|E_{D1}|$. **Critical restriction:** Do not apply if either distance is in the near field.
若 $D_1$ 和 $D_2$ 均在远场，则 $|E_{D2}|=(D_1/D_2)|E_{D1}|$。**关键限制：** 若任一距离在近场中则不适用。

### Average Power Density and Radiation Resistance / 平均功率密度与辐射电阻

Time-average Poynting vector / 时均坡印廷矢量：
$$
\bar{\mathbf{S}} = \frac{15\pi}{\lambda_0^2}\frac{|\hat{I}|^2\,dl^2\,\sin^2\theta}{r^2}\,\hat{a}_r \quad \text{(W/m}^2\text{)} \tag{7.4}
$$

Total radiated power (integrating over a sphere of radius $r$) / 总辐射功率（对半径为 $r$ 的球面积分）：
$$
P_{\text{rad}} = 80\pi^2\!\left(\frac{dl}{\lambda_0}\right)^2\frac{|\hat{I}|^2}{2} \quad \text{(W)} \tag{7.5}
$$

Radiation resistance / 辐射电阻：
$$
R_{\text{rad}} = 80\pi^2\!\left(\frac{dl}{\lambda_0}\right)^2 \quad \text{(Ω)} \tag{7.6}
$$

**Example 7.1 / 例7.1：** Hertzian dipole / 赫兹偶极子，$dl=1$ cm，$f=100$ MHz，$I=1$ A，$r=1000$ m，$\theta=90°$。$\lambda_0=3$ m，$dl/\lambda_0=1/300$。From (7.2a) / 由(7.2a)：
$$
\hat{E}_\theta = 6.28\times10^{-4}\angle-120{,}000°\;\text{V/m},\qquad
\hat{H}_\phi = 1.67\times10^{-6}\angle-120{,}000°\;\text{A/m}
$$

**Engineering intuition — Hertzian dipole limitations / 工程直觉——赫兹偶极子的局限性：**
- At $dl=1$ cm, $f=300$ MHz: $R_{\text{rad}}=79$ mΩ → requires $I_{\text{rms}}=3.6$ A for 1 W / 需 $I_{\text{rms}}=3.6$ A 才能辐射1 W。
- At $f=3$ MHz: $R_{\text{rad}}=7.9$ mΩ → requires $I_{\text{rms}}=356$ A for 1 W / 需 $I_{\text{rms}}=356$ A 才能辐射1 W。
- Despite being an inefficient radiator, the Hertzian dipole's far fields closely approximate those of most practical antennas in the far-field region.
尽管赫兹偶极子效率极低，但其远场与大多数实用天线的远场特性非常接近。

---

### 7.1.2 The Magnetic Dipole (Loop) / 磁偶极子（环天线）

A small circular loop of radius $b$ (circumference $\ll\lambda_0/10$) lying in the $xy$-plane carries phasor current $\hat{I}$. The loop constitutes a **magnetic dipole moment** / 半径为 $b$ 的小圆环（周长 $\ll\lambda_0/10$）位于 $xy$ 平面，携带相量电流 $\hat{I}$，构成**磁偶极矩**：
$$
\mathbf{\hat{m}} = \hat{I}\pi b^2 \quad \text{(A·m}^2\text{)} \tag{7.7}
$$

Radiated fields from (7.8) / 由(7.8)的辐射场：
$$
\hat{E}_r=0,\;\hat{E}_\theta=0,\;
\hat{E}_\phi = -j\frac{\omega\mu_0\mathbf{\hat{m}}}{4\pi}\sin\theta\!\left(j\frac{1}{\beta_0 r}+\frac{1}{\beta_0^2 r^2}\right)e^{-j\beta_0 r} \tag{7.8c}
$$
$$
\hat{H}_r = j\frac{2\omega\mu_0\mathbf{\hat{m}}}{4\pi\eta_0}\cos\theta\!\left(\frac{1}{\beta_0^2 r^2}-j\frac{1}{\beta_0^3 r^3}\right)e^{-j\beta_0 r} \tag{7.8d}
$$
$$
\hat{H}_\theta = j\frac{\omega\mu_0\mathbf{\hat{m}}}{4\pi\eta_0}\sin\theta\!\left(j\frac{1}{\beta_0 r}+\frac{1}{\beta_0^2 r^2}-j\frac{1}{\beta_0^3 r^3}\right)e^{-j\beta_0 r} \tag{7.8e}
$$

**Far-field / 远场：**
$$
\hat{\mathbf{E}}_{\text{far}} = \frac{\pi f^2\mu_0\hat{I}b^2}{v_0}\frac{\sin\theta}{r}e^{-j\beta_0 r}\,\hat{a}_\phi \tag{7.9a}
$$
$$
\hat{\mathbf{H}}_{\text{far}} = \frac{1}{\eta_0}\hat{\mathbf{E}}_{\text{far}}\times\hat{a}_r \tag{7.9b}
$$

Radiation resistance / 辐射电阻：
$$
R_{\text{rad}} = 31{,}170\!\left(\frac{A}{\lambda_0^2}\right)^2 \quad \text{(Ω)} \tag{7.10}
$$
where $A=\pi b^2$ is the loop area / 其中 $A=\pi b^2$ 为环面积。

**Example 7.2 — PCB loop (EMC warning) / 例7.2——PCB回路（EMC警示）：** A 1×1 cm loop (equivalent radius $b=5.64$ mm) carries $I=100$ mA at $f=50$ MHz. At $r=3$ m (FCC Class B), maximum $E$-field in the loop plane / 1×1 cm回路（等效半径 $b=5.64$ mm）在 $f=50$ MHz 下携带 $I=100$ mA。在 $r=3$ m（FCC B类）处，环面内最大 $E$ 场：
$$
|\hat{E}| = 109.6\;\text{mV/m} = 40.8\;\text{dB}\mu\text{V/m}
$$

FCC Class B limit from 30–88 MHz is **40 dBμV/m**. A 1×1 cm loop at 50 MHz with 100 mA **exceeds the limit**—real PCB structures unintentionally radiate and can fail compliance tests.
FCC B类在30–88 MHz的限值为**40 dBμV/m**。1×1 cm回路在50 MHz下100 mA即**超限**——实际PCB结构会无意辐射，可能导致合规测试失败。

**Engineering intuition — magnetic dipole duality / 工程直觉——磁偶极子的对偶性：**
- The magnetic dipole is the dual of the Hertzian dipole: $E$ and $H$ fields swap roles / 磁偶极子是赫兹偶极子的对偶：$E$ 和 $H$ 场互换角色。
- Like the Hertzian dipole, the loop is an inefficient radiator / 与赫兹偶极子类似，环天线的辐射效率很低。

---

## 7.2 Half-Wave Dipole and Quarter-Wave Monopole / 半波偶极子与四分之一波单极子

### Current Distribution on a Long Dipole / 长偶极子上的电流分布

The long-dipole antenna (thin wire of length $\ell$, fed at midpoint) has current distribution approximately following the transmission-line sinusoid / 长偶极子天线（长度为 $\ell$ 的细导线，中点馈电）的电流分布近似遵循传输线正弦分布：
$$
\hat{I}(z) = 
\begin{cases}
\hat{I}_m \sin\!\left[\beta_0\!\left(\frac{\ell}{2}-z\right)\right], & 0<z<\frac{\ell}{2}\\[6pt]
\hat{I}_m \sin\!\left[\beta_0\!\left(\frac{\ell}{2}+z\right)\right], & -\frac{\ell}{2}<z<0
\end{cases} \tag{7.11}
$$
This correctly goes to zero at the endpoints $z=\pm\ell/2$.
这正确地在端点 $z=\pm\ell/2$ 处为零。

### Far-Field of the Long Dipole / 长偶极子的远场

Applying the far-field (parallel-ray) approximation / 应用远场（平行射线）近似：
$$
\hat{E}_\theta = j\eta_0\frac{\hat{I}_m}{2\pi r}e^{-j\beta_0 r}F(\theta) \tag{7.16}
$$
where the **pattern factor** is / 其中**方向图因子**为：
$$
F(\theta) = \frac{\cos\!\left[\left(\frac{\pi\ell}{\lambda_0}\right)\cos\theta\right]-\cos\!\left(\frac{\pi\ell}{\lambda_0}\right)}{\sin\theta} \tag{7.17}
$$

### Half-Wave Dipole ($\ell=\lambda_0/2$) / 半波偶极子（$\ell=\lambda_0/2$）

With $\beta_0\ell/2=\pi/2$ / 当 $\beta_0\ell/2=\pi/2$：
$$
F(\theta) = \frac{\cos\!\left(\frac{\pi}{2}\cos\theta\right)}{\sin\theta} \tag{7.19}
$$
$F(90°)=1$ (maximum at broadside / 侧射方向最大).

**Maximum far-field / 最大远场：**
$$
|\hat{E}|_{\max} = \frac{60|\hat{I}_m|}{r} \quad (\theta=90°) \tag{7.20}
$$

Average power density / 平均功率密度：
$$
\bar{\mathbf{S}} = \frac{\eta_0}{8\pi^2}\,4.77\,|\hat{I}_m|^2\frac{F^2(\theta)}{r^2}\,\hat{a}_r \quad \text{(W/m}^2\text{)} \tag{7.21}
$$

Total radiated power / 总辐射功率：
$$
P_{\text{rad}} = \frac{73|\hat{I}_m|^2}{2} \quad \text{(W)} \tag{7.22}
$$

**Radiation resistance: $R_{\text{rad}} = 73$ Ω** (half-wave dipole / 半波偶极子).

### Quarter-Wave Monopole ($\ell=\lambda_0/4$, above ground plane) / 四分之一波单极子（$\ell=\lambda_0/4$，置于地平面上）

Using method of images, the monopole radiates only into the upper half-space / 利用镜像法，单极子仅向上半空间辐射，so / 因此：
$$
R_{\text{rad}} = 36.5\;\Omega \tag{7.25}
$$

### Input Impedance / 输入阻抗

General form / 一般形式：$\hat{Z}_{\text{in}} = R_{\text{loss}} + R_{\text{rad}} + jX_{\text{in}}$ (7.27).

- **Half-wave dipole / 半波偶极子**: $\hat{Z}_{\text{in}}=(73+j42.5)$ Ω
- **Quarter-wave monopole / 四分之一波单极子**: $X_{\text{in}}=21.25$ Ω

Antennas **shorter than resonant length** have $R_{\text{rad}}$ dropping dramatically and large negative $X_{\text{in}}$ (capacitive). A **loading coil** (inductor) in series cancels the capacitance.
**长度短于谐振长度**的天线 $R_{\text{rad}}$ 急剧下降，且 $X_{\text{in}}$ 为很大的负值（容性）。串联**加载线圈**（电感）可抵消容抗。

**Example 7.3 / 例7.3：** Half-wave dipole at $f=150$ MHz driven by $V_S=100$ V (peak), $R_S=50$ Ω. Wire: #20 AWG copper, skin depth $\delta=5.4$ μm at 150 MHz / 半波偶极子，$f=150$ MHz，驱动 $V_S=100$ V（峰值），$R_S=50$ Ω。导线：#20 AWG铜线，150 MHz时趋肤深度 $\delta=5.4$ μm。

If dipole is shortened to $\ell=\lambda_0/8$: $R_{\text{rad}}\approx1.5$ Ω, $X_{\text{in}}\approx-600$ Ω. Radiated power drops to **20.7 mW**—a reduction by a factor of ~1000. Adding a loading coil with $X_L=+j600$ Ω restores power to **2.81 W** (136× improvement).
若偶极子缩短至 $\ell=\lambda_0/8$：$R_{\text{rad}}\approx1.5$ Ω，$X_{\text{in}}\approx-600$ Ω。辐射功率降至**20.7 mW**——降低了约1000倍。加入 $X_L=+j600$ Ω 的加载线圈后功率恢复至**2.81 W**（提升136倍）。

**Engineering intuition — dipole vs. monopole / 工程直觉——偶极子 vs 单极子：**
- The 73 Ω radiation resistance makes the half-wave dipole practical to drive / 73 Ω辐射电阻使半波偶极子具有实际驱动性。
- **Shortening destroys efficiency** / **缩短摧毁效率**：halving the dipole length collapses radiation resistance while dramatically increasing capacitive reactance / 偶极子长度减半使辐射电阻急剧下降，同时容抗剧增。

---

## 7.3 Antenna Arrays / 天线阵

### Two-Element Array / 二元阵

Two identical omnidirectional antennas separated by distance $d$, with currents $\hat{I}_1=I_a$ and $\hat{I}_2=I_0$ (equal magnitude, antenna #1 leads #2 by phase $\alpha$). For a field point $P$ in the far field / 两个相同的全向天线相距 $d$，电流 $\hat{I}_1=I_a$ 和 $\hat{I}_2=I_0$（幅度相等，天线#1超前#2相位 $\alpha$）。对于远场中的场点 $P$：

Total field / 总场：
$$
\hat{E}_\theta = 2\hat{M}I\frac{e^{-j\beta_0 r}}{r}e^{j\alpha/2}\cos\!\left(\frac{\pi d}{\lambda_0}\cos\phi+\frac{\alpha}{2}\right) \tag{7.31}
$$

**Array factor** for pattern plotting / 用于绘制方向图的**阵因子**：
$$
F(\phi) = \cos\!\left(\frac{\pi d}{\lambda_0}\cos\phi+\frac{\alpha}{2}\right) \tag{7.33}
$$

**Null locations / 零点位置：** $F(\phi)=0 \Rightarrow \frac{\pi d}{\lambda_0}\cos\phi+\frac{\alpha}{2}=\pm\frac{\pi}{2}$.

**Engineering intuition — array effects in EMC / 工程直觉——EMC中的阵列效应：**
- Even small path differences (fractions of $\lambda_0$) produce dramatic pattern nulls and maxima / 即使很小的路径差也能产生显著的方向图零点和最大值。
- This array superposition model underlies the **wire model** for PCB emission prediction (Chapter 8) / 该阵列叠加模型是PCB发射预测**导线模型**的基础。

---

## 7.4 Characterization of Antennas / 天线表征

### 7.4.1 Directivity and Gain / 方向性与增益

**Radiation intensity / 辐射强度** $U(\theta,\phi)=r^2\bar{S}$ (W/sr, independent of distance / 与距离无关)：
$$
U(\theta,\phi) = \frac{|\hat{E}_{\text{far}}|^2}{2\eta_0} \tag{7.35}
$$

Total radiated power / 总辐射功率：
$$
P_{\text{rad}} = \int_0^{2\pi}\int_0^\pi U(\theta,\phi)\sin\theta\,d\theta\,d\phi \tag{7.36}
$$

Average radiation intensity / 平均辐射强度：$U_{\text{av}}=P_{\text{rad}}/4\pi$.

**Directivity / 方向性系数：**
$$
D(\theta,\phi)=\frac{U(\theta,\phi)}{U_{\text{av}}}=\frac{4\pi U(\theta,\phi)}{P_{\text{rad}}} \tag{7.38}
$$

**Gain / 增益** (accounting for losses / 计入损耗)：
$$
G(\theta,\phi)=\eta_{\text{eff}}D(\theta,\phi)=\frac{4\pi U(\theta,\phi)}{P_{\text{app}}} \tag{7.41–42}
$$

**Key gains / 关键增益：**
- Hertzian dipole / 赫兹偶极子：$G=1.5$ (1.76 dBd)
- Half-wave dipole / 半波偶极子：$G=1.64$ (2.15 dBd)
- Quarter-wave monopole / 四分之一波单极子：$G=3.28$ (5.17 dBd)

**Reciprocity / 互易性：** Source and receiver can be interchanged / 源和接收器可互换。

### 7.4.2 Effective Aperture / 有效孔径

**Effective aperture** $A_e$ of a receiving antenna / 接收天线的**有效孔径** $A_e$：
$$
A_e = \frac{P_R}{S_{\text{av}}} \quad \text{(m}^2\text{)} \tag{7.52}
$$

Maximum effective aperture / 最大有效孔径：
$$
A_{e,m} = \frac{G\,\lambda_0^2}{4\pi} \tag{7.59}
$$

### 7.4.3 Antenna Factor / 天线因子

**Antenna factor** (AF) relates incident $E$-field to received voltage / **天线因子**(AF)将入射 $E$ 场与接收电压相关联：
$$
\text{AF} = \frac{|E_{\text{inc}}|}{|V_{\text{rec}}|} \quad \text{(1/m)} \tag{7.60}
$$

In dB / 用dB表示：
$$
\text{AF}_{\text{dB}} = \text{dB}\mu\text{V/m (incident)} - \text{dB}\mu\text{V (received)} \tag{7.61a}
$$
$$
E_{\text{dB}\mu\text{V/m}} = V_{\text{SA, dB}\mu\text{V}} + \text{AF}_{\text{dB}} + \text{cable loss (dB)} \tag{7.62}
$$

### 7.4.4 Effects of Balancing and Baluns / 平衡与巴伦的影响

**Balun** (balanced-to-unbalanced transformer) blocks common-mode current on the outer shield.
**巴伦**（平衡-不平衡变换器）阻止屏蔽层外壁的共模电流。

- **Bazooka balun / 火箭筒巴伦：** Quarter-wavelength section of shield shorted at feedpoint / 四分之一波长屏蔽段在馈点短路。Narrowband (single frequency) / 窄带（单频）。
- **Ferrite baluns / 铁氧体巴伦：** Ferrite sleeves or toroids act as common-mode chokes. Wideband (up to 3:1 bandwidth ratio) / 铁氧体套管或磁环作为共模扼流圈。宽带（带宽比可达3:1）。

### 7.4.5 Impedance Matching and Pads / 阻抗匹配与衰减器

**Pad / 衰减器:** Resistive network (commonly Pi-structure $\pi$) providing constant input impedance regardless of load, over wide frequency range / 电阻网络（常用 $\pi$ 型结构），在宽频率范围内无论负载如何均提供恒定输入阻抗。

---

## 7.5 The Friis Transmission Equation / 弗里斯传输方程

Two antennas in free space separated by distance $d$, with gains $G_T(\theta_T,\phi_T)$ and $G_R(\theta_R,\phi_R)$ / 自由空间中相距 $d$ 的两个天线，增益分别为 $G_T(\theta_T,\phi_T)$ 和 $G_R(\theta_R,\phi_R)$。

Power density at receiving antenna / 接收天线处的功率密度：
$$
\bar{S} = \frac{P_T}{4\pi d^2}G_T(\theta_T,\phi_T) \tag{7.66}
$$

**Friis transmission equation / 弗里斯传输方程：**
$$
\frac{P_R}{P_T} = \frac{G_T(\theta_T,\phi_T)\,G_R(\theta_R,\phi_R)}{(4\pi d/\lambda_0)^2} \tag{7.69}
$$

Electric field at receiving antenna / 接收天线处的电场：
$$
|\hat{E}| = \sqrt{\frac{60\,P_T\,G_T(\theta_T,\phi_T)}{d}} \quad \text{(V/m)} \tag{7.71}
$$

**Assumptions / 假设：**
1. Both antennas in far field of each other / 两天线互在对方远场
2. Receiving antenna matched to load and polarization-matched / 接收天线与负载匹配且极化匹配
3. Incoming wave locally resembles uniform plane wave / 入射波在接收天线处局部近似为均匀平面波

---

## 7.6 Effects of Reflections / 反射的影响

### 7.6.1 Method of Images / 镜像法

For a charge/current above a perfectly conducting ground plane, replace the ground plane with an image / 对于理想导电平面上方的电荷/电流，用地平面下方的镜像代替：
- Point charge $+Q$ at height $h$: image is $-Q$ at depth $h$ / 高度 $h$ 处的点电荷 $+Q$：镜像为深度 $h$ 处的 $-Q$
- Current parallel to ground: image parallel, same magnitude, **opposite direction** / 平行于地面的电流：镜像平行、等幅、**反向**
- Current perpendicular to ground: image parallel, same magnitude, **same direction** / 垂直于地面的电流：镜像平行、等幅、**同向**

### 7.6.2 Normal Incidence on Plane Boundaries / 平面边界的正入射

Uniform plane wave normally incident on boundary between two media with intrinsic impedances $\eta_1$, $\eta_2$ / 均匀平面波正入射到本征阻抗分别为 $\eta_1$、$\eta_2$ 的两种介质之间的边界：

**Reflection coefficient / 反射系数：**
$$
\hat{\Gamma} = \frac{\eta_2-\eta_1}{\eta_2+\eta_1} \tag{7.77a}
$$

**Transmission coefficient / 传输系数：**
$$
\hat{T} = \frac{2\eta_2}{\eta_2+\eta_1} \tag{7.77b}
$$

### 7.6.3 Multipath Effects (Ground Plane Reflections) / 多径效应（地平面反射）

In practical radiated emission testing, the received signal is the vector sum of the direct wave and the wave reflected from the ground plane.
在实际辐射发射测试中，接收信号是直达波和地平面反射波的矢量和。

**Ground reflection factor / 地平面反射因子：**
$$
\hat{F} = 1 + \hat{\Gamma}\,\frac{d}{d_r}\,e^{-j\beta_0(d_r-d)} \tag{7.88b}
$$

**Engineering intuition — multipath in compliance testing / 工程直觉——合规测试中的多径效应：**
- Ground plane creates deep nulls at specific frequencies and antenna heights / 地平面在特定频率和天线高度下产生深零点。
- A product passing at one height may fail at another—not measurement error but real multipath interference / 产品在一个高度通过但可能在另一高度失败——这不是测量误差，而是真实的多径干涉。

---

## 7.7 Broadband Measurement Antennas / 宽带测量天线

### 7.7.1 The Biconical Antenna / 双锥天线

**Infinite biconical antenna / 无限双锥天线：** Two cones of half-angle $\theta_h$, fed at the apex gap / 两个半角为 $\theta_h$ 的圆锥，在顶点间隙处馈电。

**Input impedance** (purely resistive / 纯电阻)：
$$
\hat{Z}_{\text{in}} = \eta_0\pi\ln\!\left(\cot\frac{\theta_h}{2}\right) = 120\pi\ln\!\left(\cot\frac{\theta_h}{2}\right) \tag{7.94}
$$

**Practical truncated biconicals / 实用截断双锥天线：** Finite cone length causes discontinuities. Typical range / 典型工作范围：**30–200 MHz**.

### 7.7.2 The Log-Periodic Dipole Array (LPDA) / 对数周期偶极子阵列

Primary antenna for **200 MHz–1 GHz** measurements.
**200 MHz–1 GHz** 测量的主要天线。

**Structure / 结构：** Element lengths and spacings follow geometric progression / 单元长度和间距按几何比例变化：
$$
\tau = \frac{l_n}{l_{n+1}} = \frac{R_{n+1}}{R_n} \quad (\tau\approx 0.8\text{–}0.95) \tag{7.98}
$$

**Engineering intuition / 工程直觉：** The LPDA's frequency independence comes from its **self-similar** structure—pattern repeats as frequency changes / LPDA的频率无关性源于其**自相似**结构——方向图随频率变化重复。

---

## Summary of Key Parameters / 关键参数汇总

| Antenna / 天线 | $R_{\text{rad}}$ | Gain (linear) / 增益（线性） | Gain (dBd) |
|----------|-----------------|---------------|------------|
| Hertzian dipole ($dl\ll\lambda_0$) / 赫兹偶极子 | $80\pi^2(dl/\lambda_0)^2$ Ω | 1.5 | $-1.76$ |
| Half-wave dipole / 半波偶极子 | 73 Ω | 1.64 | 0 (reference / 参考) |
| Quarter-wave monopole / 四分之一波单极子 | 36.5 Ω | 3.28 | $+5.17$ |
| Magnetic dipole (loop, area $A$) / 磁偶极子（环天线，面积$A$） | $31{,}170(A/\lambda_0^2)^2$ Ω | — | — |

**Critical thresholds / 关键阈值：**
- Far-field (wire) / 远场（线天线）：$r>3\lambda_0$
- Far-field (surface) / 远场（面天线）：$r>2D^2/\lambda_0$
- FCC Class B test / FCC B类测试：ground reflection factors can vary by ~50 dB with antenna height at 30 MHz / 在30 MHz处地平面反射因子随天线高度变化约50 dB

**Antenna factor / 天线因子：** $E_{\text{dB}\mu\text{V/m}} = V_{\text{SA,dB}\mu\text{V}} + \text{AF}_{\text{dB}} + \text{cable loss (dB)}$

**Friis equation / 弗里斯方程：** $\displaystyle \frac{P_R}{P_T} = \frac{G_T G_R}{(4\pi d/\lambda_0)^2}$

**Key EMC insight / 关键EMC洞察：** A 1×1 cm PCB loop at 50 MHz with 100 mA exceeds FCC Class B limits—unintentional antennas (traces, enclosure seams, cables) are the primary emission concerns / 1×1 cm PCB回路在50 MHz下100 mA即超过FCC B类限值——无意天线（走线、机箱缝隙、电缆）是主要的发射关注点。
