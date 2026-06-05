# Collins Ch8 (2nd Ed. Ch9) — Microwave Tubes

> **来源**: R. E. Collin, *Foundations for Microwave Engineering*, 2nd ed., IEEE Press, 2001.
> **注意**: 本章在第二版中为 **Ch9 (Microwave Tubes, pp. 648–712)**。此处按第一版编号(Ch8)组织,内容对应第二版 §9.1–§9.13。

---

## §8.1 引言 (Introduction, §9.1, p. 648)

微波管(Microwave Tubes)在高功率微波系统中仍然不可替代,尽管低功率领域已被固态器件取代。本章覆盖两大类:

| 类型 | 原理 | 代表 |
|------|------|------|
| **O型管 (O-type / Linear-beam tubes)** | 电子束与轴向电场相互作用,磁场用于聚焦 | 速调管、行波管 |
| **M型管 (M-type / Crossed-field tubes)** | 电场与磁场正交,电子在交叉场中漂移 | 磁控管、交叉场放大器 |

**关键概念:**
- **电子注(Beam)**: 从阴极发射的电子流,经阳极加速后形成。
- **速度调制(Velocity modulation)**: RF 信号通过间隙电场对电子速度进行调制,使电子在漂移空间中形成**群聚(bunching)**。
- **对流电流(Convection current)**: 运动电荷形成的电流,在微波管中起核心作用(p. 648)。

---

## §8.2 直流电子注 (Electron Beams with dc Conditions, §9.2, pp. 650–654)

### 8.2.1 离子中和注 (Ion-Neutralized Beam, p. 650)

当电子注通过残余气体时,气体被电离产生的正离子可部分中和电子空间电荷,降低散焦力。离子中和注的分析假设:

- 电子密度 $\rho_0$ 均匀
- 正离子密度 $n_i \approx n_e$ (准中性)

### 8.2.2 轴向约束注 (Beam with Axially Confined Flow, p. 651)

使用轴向磁场 $B_0$ 约束电子注,阻止径向扩散。电子运动满足:

$$
m \frac{d^2 r}{dt^2} = -e(E_r + v_z B_\theta) - e v_\theta B_0
\tag{9.1, p. 651}
$$

其中 $E_r$ 为空间电荷产生的径向电场,$B_0$ 为外加轴向磁场。

**布里渊流 (Brillouin Flow, p. 652)**:
当磁场刚好足够平衡空间电荷力时,电子注处于**布里渊流**状态。此时磁场满足:

$$
B_0 = B_b = \sqrt{\frac{2 I_0}{\pi \epsilon_0 v_0 (b^2 - a^2)}}
\tag{9.2, p. 652}
$$

其中 $a$ 为电子注半径,$b$ 为漂移管半径。布里渊磁场的典型值在 $0.01$–$0.5$ T 之间。

布里渊流中,电子注内部的电子以角速度 $\omega_L = eB_0/(2m)$ 旋转(Larmor 频率的一半),所有电子具有相同的轴向速度 $v_0$。

---

## §8.3 约束流中的空间电荷波 (Space-Charge Waves on Beams with Confined Flow, §9.3, pp. 654–661)

### 8.3.1 一维空间电荷波理论

假设无限强轴向磁场完全约束电子注(只允许一维轴向运动)。从电子运动方程、连续性方程和泊松方程出发:

**运动方程:**
$$
\frac{\partial v}{\partial t} + v_0 \frac{\partial v}{\partial z} = -\frac{e}{m} E_z
\tag{9.3, p. 654}
$$

**连续性方程:**
$$
\frac{\partial \rho}{\partial t} + \rho_0 \frac{\partial v}{\partial z} + v_0 \frac{\partial \rho}{\partial z} = 0
\tag{9.4, p. 655}
$$

**对流电流:**
$$
J = \rho_0 v + v_0 \rho
\tag{9.5, p. 655}
$$

### 8.3.2 等离子体频率与约化因子

对于无限大电子注,等离子体频率为:

$$
\omega_p = \sqrt{\frac{e \rho_0}{m \epsilon_0}}
\tag{9.6, p. 655}
$$

在实际有限截面电子注中,漂移管壁的镜像效应减小了轴向电场,等离子体频率降低为 **约化等离子体频率**:

$$
\omega_q = R \omega_p
\tag{9.7, p. 656}
$$

其中 $R$ 为**等离子体频率约化因子(plasma frequency reduction factor)**,与 $\beta_e b$ 和 $b/a$ 有关($\beta_e = \omega/v_0$)。

约化因子 $R$ 由以下超越方程给出(p. 657):

$$
R = \frac{1}{\sqrt{1 + T_0^2 / \beta_e^2}}
\tag{9.8, p. 657}
$$

其中 $T_0$ 由特征值问题 $(\nabla_t^2 + T_0^2) E_z = 0$ 决定。

### 8.3.3 空间电荷波解

空间电荷波存在两个模式:

| 模式 | 传播常数 | 物理含义 |
|------|---------|---------|
| **快波 (Fast space-charge wave)** | $\beta_f = \beta_e - \beta_q$ | 速度高于 $v_0$ |
| **慢波 (Slow space-charge wave)** | $\beta_s = \beta_e + \beta_q$ | 速度低于 $v_0$ |

其中 $\beta_e = \omega/v_0$, $\beta_q = \omega_q/v_0$。

轴向电场 $E_z$、对流电流 $J$ 和速度 $v$ 可表示为两个空间电荷波的叠加(p. 659):

$$
E_z = E_f e^{-j\beta_f z} + E_s e^{-j\beta_s z}
\tag{9.9, p. 659}
$$

$$
J = -\frac{j\omega\epsilon_0}{\beta_q} (E_f e^{-j\beta_f z} - E_s e^{-j\beta_s z})
\tag{9.10, p. 660}
$$

---

## §8.4 无聚焦电子注中的空间电荷波 (Space-Charge Waves on Unfocused Beams, §9.4, pp. 661–667)

对于有限聚焦或无聚焦的电子注,需考虑径向电场和横向运动。此时波动方程更复杂:

$$
\left( \frac{\partial^2}{\partial z^2} + \beta_e^2 - \beta_q^2 \right) E_z = 0
\tag{9.11, p. 661}
$$

解形式相同,但 $\beta_q$ 需考虑横向边界条件。注-管填充比 $b/a$ 越小,约化因子 $R$ 越小,空间电荷效应越弱。

---

## §8.5 交流功率关系 (Ac Power Relations, §9.5, pp. 667–670)

电子注中的交变功率流由**动能流(kinetic power flow)** 和**电磁功率流(E-M power flow)** 两部分组成:

**坡印廷功率流(Poynting power):**

$$
P_{em} = \frac{1}{2} \text{Re} \int_S (\mathbf{E} \times \mathbf{H}^*) \cdot \hat{z} \, dS
\tag{9.12, p. 667}
$$

**动能功率流(Kinetic power flow):**

$$
P_k = \frac{1}{2} \frac{v_0}{\eta} \text{Re} \int_S (J^* v) \, dS
\tag{9.13, p. 668}
$$

其中 $\eta = e/m$ 为荷质比。总功率守恒:

$$
\frac{d}{dz} (P_{em} + P_k) = 0
\tag{9.14, p. 668}
$$

**重要结论**: 当电子注的慢空间电荷波被激发时,动能流 $P_k$ 为负值——电子注从电磁波吸收能量(放大时);当快波被激发时,动能流为正值。

---

## §8.6 速度调制 (Velocity Modulation, §9.6, pp. 670–678)

### 8.6.1 间隙耦合(Buncher Cavity)

电子通过谐振腔间隙时受到 RF 电场作用,速度被调制。设间隙电压为 $V_1 \sin \omega t$,电子穿过间隙后的速度:

$$
v(t_1) = v_0 \left[ 1 + \frac{\beta_i V_1}{2 V_0} \sin\left(\omega t_1 - \frac{\theta_g}{2}\right) \right]
\tag{9.15, p. 671}
$$

其中:
- $V_0$ = 直流加速电压
- $\theta_g = \omega d / v_0$ = 间隙渡越角
- $\beta_i$ = **束流耦合系数(beam coupling coefficient)**

### 8.6.2 束流耦合系数

$$
\beta_i = \frac{\sin(\theta_g/2)}{\theta_g/2}
\tag{9.16, p. 671}
$$

束流耦合系数衡量 RF 间隙电场对电子速度调制的效率。当 $\theta_g \to 0$ 时, $\beta_i \to 1$; 实际设计中 $\theta_g \approx \pi/2$ 以获得合理折衷。

### 8.6.3 群聚(Bunching)

速度调制的电子在漂移空间中的飞行时间不同,产生对电流密度的调制——群聚。

**群聚参数 (Bunching parameter):**

$$
X = \frac{\beta_i V_1 \theta_0}{2 V_0}
\tag{9.17, p. 672}
$$

其中 $\theta_0 = \omega L / v_0$ 为漂移空间的直流渡越角。

**对流电流的傅里叶级数:**

被速度调制并对电流调制的电子束在输出间隙处的对流电流为(p. 674):

$$
I_2 = 2 I_0 \sum_{n=1}^\infty \frac{\sin(n\theta_g/2)}{n\theta_g/2} J_n(nX) e^{-j n \omega t_1}
\tag{9.18, p. 674}
$$

基波分量($n=1$)为:

$$
I_2 = 2 I_0 \beta_i J_1(X) e^{-j\omega t_1}
\tag{9.19, p. 675}
$$

其中 $J_1(X)$ 为第一类一阶贝塞尔函数。

**最大基波电流**: 当 $X = 1.841$ 时 $J_1(X)$ 取最大值 $0.582$,此时:

$$
I_{2,max} = 1.164 I_0 \beta_i
\tag{9.20, p. 675}
$$

---

## §8.7 双腔速调管 (Two-Cavity Klystron, §9.7, pp. 678–686)

### 8.7.1 基本结构与工作原理(p. 678)

双腔速调管由以下部分组成:
1. **电子枪(Electron gun)**: 发射并加速电子
2. **输入腔(Input/Buncher cavity)**: 速度调制
3. **漂移空间(Drift space)**: 群聚
4. **输出腔(Output/Catcher cavity)**: 提取能量
5. **收集极(Collector)**: 收集电子

### 8.7.2 增益计算

输出腔中感应电流:
$$
I_{ind} = \beta_o I_2 = 2 I_0 \beta_i \beta_o J_1(X)
\tag{9.21, p. 683}
$$

其中 $\beta_o$ 为输出腔的束流耦合系数(通常 $\beta_o \approx \beta_i = \beta$)。

**输出功率:**

$$
P_{out} = \frac{I_{ind}^2 R_{sh}}{2} = 2 I_0^2 \beta^4 J_1^2(X) R_{sh}
\tag{9.22, p. 684}
$$

其中 $R_{sh}$ 为输出腔的并联阻抗(包括负载)。

**功率增益:**

在小信号下($X \ll 1$), $J_1(X) \approx X/2$,于是:

$$
G = \frac{P_{out}}{P_{in}} = \frac{\beta^4 \theta_0^2 I_0 R_{sh}}{4 V_0} \cdot \frac{R_{sh}}{R_{in}}
\tag{9.23, p. 684}
$$

经验公式:增益典型值 **20–30 dB**。

### 8.7.3 腔体激励(Cavity Excitation, pp. 679–683)

电子注通过谐振腔间隙时,感应电流激励腔体产生 RF 电压。腔体可等效为并联 RLC 电路,其阻抗为:

$$
Z(\omega) = \frac{R_{sh}}{1 + j Q_L (\omega/\omega_0 - \omega_0/\omega)}
\tag{9.24, p. 681}
$$

**最佳负载**:当输出腔调谐在信号频率时,耦合系数 $\beta_c = Q_0/Q_{ext}$ 影响功率传输效率。

### 8.7.4 电子效率

$$
\eta_e = \frac{P_{out}}{P_{dc}} = \frac{P_{out}}{I_0 V_0}
\tag{9.25, p. 685}
$$

双腔速调管的典型效率 **30–40%**,多腔速调管可达 **60–70%**。

---

## §8.8 反射速调管 (Reflex Klystron, §9.8, pp. 686–690)

### 8.8.1 结构与原理(p. 686)

反射速调管是单腔振荡器。电子穿过腔体后被**反射极(Repeller)** 的高负压推回,再次穿过腔体,形成反馈。

### 8.8.2 振荡条件

反射空间的直流渡越角:

$$
\theta_0 = \omega \frac{2L_r}{v_0}
\tag{9.26, p. 687}
$$

其中 $L_r$ 为腔体到反射极的距离。

**最佳模式条件(使电子群在返回时处于减速场):**

$$
\theta_0 = 2\pi n - \frac{\pi}{2} = 2\pi\left(n - \frac{1}{4}\right), \quad n = 1,2,3,\dots
\tag{9.27, p. 688}
$$

每个 $n$ 对应一个振荡模式。电子调谐范围随 $n$ 增大而减小。

### 8.8.3 功率与效率

输出功率:
$$
P_{out} = \frac{2 V_0 I_0 \beta^2 X J_1(X)}{\theta_0}
\tag{9.28, p. 689}
$$

最大效率:
$$
\eta_{max} = \frac{\beta^2 \cdot 1.26}{\theta_0}
\tag{9.29, p. 689}
$$

通常效率 **1–3%** (远低于多腔速调管),但反射速调管具有**电子调谐**能力,调谐范围可达 **1–2%** 的带宽。

---

## §8.9 磁控管 (Magnetron, §9.9, pp. 690–692)

### 8.9.1 结构与原理(p. 690)

磁控管是**交叉场器件(Crossed-field device)**,具有:
- 圆柱形阴极(中心)
- 阳极块(带谐振腔的环状结构)
- 轴向磁场(永磁体或电磁铁)

电场径向($E_r$),磁场轴向($B_z$),电子在 **E × B** 方向漂移,形成围绕阴极旋转的电子云。

### 8.9.2 阈值条件

**Hull 截止条件** (电子刚好到达阳极所需的最小磁场):

$$
B_{c0} = \frac{\sqrt{2 m V_0 / e}}{r_a \left[1 - (r_c/r_a)^2\right]}
\tag{9.30, p. 691}
$$

其中 $r_a$ = 阳极半径, $r_c$ = 阴极半径。当 $B > B_{c0}$ 时,电子无法到达阳极(截止状态)。

**Hartree 条件(同步条件)**,即 RF 波的相速度与电子漂移速度同步:

$$
V_0 = \frac{e B^2 r_a^2}{2 m} \left[ 1 - \left( \frac{r_c}{r_a} \right)^2 \right] - \frac{m \omega^2 r_a^2}{2 e n^2} \left[ 1 - \left( \frac{r_c}{r_a} \right)^2 \right]
\tag{9.31, p. 691}
$$

其中 $n$ 为谐振腔的模数。磁控管通常工作在 $\pi$ 模($n = N/2$, $N$ 为腔数)。

### 8.9.3 色散关系(阳极块结构的谐振模式)

对于 $N$ 个腔的磁控管,工作频率由腔体尺寸决定。相邻腔体相位差:

$$
\phi = \frac{2\pi m}{N}, \quad m = 0, 1, 2, \dots, N-1
\tag{9.32, p. 691}
$$

$\pi$ 模($\phi = \pi$)是最常用模式,具有最好的稳定性和效率。

典型磁控管效率 **40–70%**,脉冲功率可达 MW 级。

---

## §8.10 O 型行波管 (O-Type Traveling-Wave Tube, §9.10, pp. 692–699)

### 8.10.1 结构与原理(p. 692)

行波管(TWT)与速调管的关键区别:
- **速调管**: 使用谐振腔,窄带,高增益
- **行波管**: 使用**慢波结构(slow-wave structure)**,宽带,中等增益

慢波结构(如螺旋线)使电磁波的轴向相速度减慢到与电子速度同步($v_p \approx v_0$)。

### 8.10.2 Pierce 参数

Pierce 小信号理论定义了以下无量纲参数:

**增益参数 $C$:**

$$
C^3 = \frac{K I_0}{4 V_0}
\tag{9.33, p. 693}
$$

其中 $K$ 为**互作用阻抗(interaction impedance)**:

$$
K = \frac{|E_z|^2}{2 \beta_e^2 P}
\tag{9.34, p. 693}
$$

$E_z$ 为轴向电场,$P$ 为沿慢波结构传输的功率。

**空间电荷参数 $QC$:**

$$
QC = \frac{\omega_q^2}{4 \omega^2 C^2}
\tag{9.35, p. 694}
$$

**失谐参数 $b$:**

$$
b = \frac{v_0}{v_p} - 1
\tag{9.36, p. 694}
$$

其中 $v_p$ 为慢波结构的相速度。

**冷损耗参数 $d$:**

$$
d = \frac{\alpha}{\beta_e C}
\tag{9.37, p. 695}
$$

其中 $\alpha$ 为冷电路的衰减常数(Np/m)。

### 8.10.3 增益

行波管的小信号增益由 Pierce 理论的色散方程决定:

**Pierce 色散方程:**

$$
(\delta^2 + 4QC)(j\delta + b - jd) = -1
\tag{9.38, p. 695}
$$

其中 $\delta$ 为**增量传播常数(incremental propagation constant)**:

$$
\Gamma = j\beta_e + \beta_e C \delta
\tag{9.39, p. 695}
$$

在同步和无损耗条件下($b = 0$, $d = 0$, $QC = 0$),三个本征值中:

$$
\delta_1 = \frac{-1 + j\sqrt{3}}{2}, \quad \delta_2 = \frac{-1 - j\sqrt{3}}{2}, \quad \delta_3 = j
$$

其中 $\delta_1$ 对应的模式是增长的(增益)。

**增益公式:**

$$
G = -9.54 + 47.3 C N \quad (\text{dB})
\tag{9.40, p. 696}
$$

其中 $N = L / \lambda_e$ 为以电子波长计的管子长度($\lambda_e = 2\pi v_0 / \omega$)。

实际增益通常 **30–60 dB**,工作带宽可达 **倍频程(octave)**。

### 8.10.4 效率

典型 TWT 效率 **15–40%**,采用**速度再同步(velocity resynchronization)** 或**收集极降压(depressed collector)** 等技术可进一步提高。

---

## §8.11 M 型行波管 (M-Type Traveling-Wave Tube, §9.11, pp. 699–701)

M 型行波管(也称**交叉场放大器,CFA**)使用与磁控管类似的交叉场结构,但具有分离的输入和输出端口。

**工作原理**: 电子在 $E \times B$ 场中漂移,其漂移速度 $v_d = E/B$。当慢波结构的相速度与漂移速度匹配时,电子通过与 RF 场的同步相互作用将势能转化为 RF 能量(而不是动能——这是与 O 型管的关键区别)。

M 型管的优点:
- 更高效率(可达 **70–80%**)
- 与磁控管相比可实现放大而非振荡
- 振幅和相位稳定性好

---

## §8.12 回旋管 (Gyrotrons, §9.12, pp. 701–708)

### 8.12.1 原理(p. 701)

回旋管利用**电子回旋谐振脉塞(Electron Cyclotron Maser)** 机理:
- 电子在强磁场中做回旋运动,回旋频率 $\omega_c = eB/m$
- RF 波频率接近 $\omega_c$ 或其谐波
- 相对论效应引起电子的**相位群聚(phase bunching)**

### 8.12.2 场-粒子相互作用(pp. 703–708)

回旋管中的电子在与波相互作用时,其相对论质量随能量变化:

$$
m = \frac{m_0}{\sqrt{1 - v^2/c^2}}
\tag{9.41, p. 704}
$$

回旋频率对能量的依赖性:

$$
\omega_c = \frac{eB}{m} = \frac{eB}{m_0} \sqrt{1 - \frac{v^2}{c^2}}
\tag{9.42, p. 704}
$$

能量高的电子回旋频率低,能量低的电子回旋频率高,这一差异(相对论效应)使电子产生相位群聚,从而将能量传递给波。

**工作频率**: 30–300 GHz (毫米波至亚毫米波)
**功率**: 连续波可达 MW 级,脉冲可达 GW 级(相对论回旋管)
**效率**: 30–50%

---

## §8.13 其他类型微波管 (Other Types of Microwave Tubes, §9.13, pp. 708–709)

| 器件 | 特点 | 应用 |
|------|------|------|
| **速调管放大器(Klystron amplifier)** | 多腔,高增益,窄带 | 雷达发射机、粒子加速器 |
| **扩展互作用速调管(EIK)** | 结合速调管和 TWT 特点 | 毫米波雷达 |
| **返波振荡器(BWO)** | 电子束与返波相互作用 | 频率可调信号源 |
| **自由电子激光器(FEL)** | 利用相对论电子束通过周期性磁结构产生相干辐射 | 太赫兹至 X 射线源 |

---

## 关键公式汇总

| 公式 | 说明 | 页码 |
|------|------|------|
| $\omega_p = \sqrt{e\rho_0/(m\epsilon_0)}$ | 无限大电子注等离子体频率 | p. 655 |
| $\omega_q = R\omega_p$ | 约化等离子体频率 | p. 656 |
| $\beta_i = \sin(\theta_g/2)/(\theta_g/2)$ | 束流耦合系数 | p. 671 |
| $X = \beta_i V_1 \theta_0/(2V_0)$ | 群聚参数 | p. 672 |
| $I_2 = 2I_0\beta_i J_1(X)e^{-j\omega t_1}$ | 基波对流电流 | p. 675 |
| $G = -9.54 + 47.3CN$ (dB) | TWT 增益 | p. 696 |
| $C^3 = KI_0/(4V_0)$ | Pierce 增益参数 | p. 693 |
| $\theta_0 = 2\pi n - \pi/2$ | 反射速调管模式条件 | p. 688 |
| $V_0 = \frac{eB^2 r_a^2}{2m}[1-(r_c/r_a)^2] - \frac{m\omega^2 r_a^2}{2en^2}[1-(r_c/r_a)^2]$ | Hartree 条件(磁控管) | p. 691 |

---

## 参考文献

1. R. E. Collin, *Foundations for Microwave Engineering*, 2nd ed., IEEE Press, 2001, Ch. 9, pp. 648–712.
2. J. R. Pierce, *Traveling-Wave Tubes*, Van Nostrand, 1950.
3. A. S. Gilmour, Jr., *Klystrons, Traveling Wave Tubes, Magnetrons, Crossed-Field Amplifiers, and Gyrotrons*, Artech House, 2011.
