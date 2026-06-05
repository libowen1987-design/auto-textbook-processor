# 郭硕鸿《电动力学》笔记

> 本笔记依据郭硕鸿《电动力学》（第三版，高等教育出版社，2008）OCR文本洗稿而成。
> 内容 100% 来自原文，仅改写表达格式，公式使用 LaTeX 渲染。

---

## 第一章 电磁现象的普遍规律

本章把电磁现象的实验定律总结为电磁场的普遍规律。电磁场是物质存在的一种形态，它弥漫于空间之中，用两个矢量场——电场强度 $\mathbf{E}(\mathbf{r}, t)$ 和磁感应强度 $\mathbf{B}(\mathbf{r}, t)$——来描述。

---

### §1.1 电荷和电场

#### 1. 库仑定律

库仑定律是静电现象的基本实验定律：真空中静止点电荷 $Q$ 对另一个静止点电荷 $Q'$的作用力为

$$
\mathbf{F} = \frac{1}{4\pi\varepsilon_0} \frac{QQ'}{r^2} \mathbf{e}_r
$$

其中 $\mathbf{e}_r$ 为由 $Q$ 指向 $Q'$ 的单位径矢，$\varepsilon_0$ 为真空电容率。

**场的观点**：电荷周围空间存在电场，另一电荷处于电场中就受到电场的作用力。由库仑定律，电场强度定义为

$$
\mathbf{F} = q\mathbf{E} \quad \Rightarrow \quad \mathbf{E}(\mathbf{r}) = \frac{1}{4\pi\varepsilon_0} \frac{Q}{r^2}\mathbf{e}_r
$$

对于多个点电荷，电场强度满足叠加原理：

$$
\mathbf{E}(\mathbf{r}) = \sum_i \frac{1}{4\pi\varepsilon_0} \frac{Q_i}{r_i^2}\mathbf{e}_{r_i}
$$

对于连续分布电荷：

$$
\mathbf{E}(\mathbf{r}) = \frac{1}{4\pi\varepsilon_0}\int_V \frac{\rho(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|^2}\mathbf{e}_{|\mathbf{r}-\mathbf{r}'|} \, dV'
$$

#### 2. 高斯定理和电场的散度

电场强度通量对闭合曲面 $S$ 的积分为

$$
\oint_S \mathbf{E} \cdot d\mathbf{S} = \frac{Q}{\varepsilon_0}
$$

其中 $Q$ 为 $S$ 内的总电荷。**高斯定理**的积分形式为

$$
\oint_S \mathbf{E} \cdot d\mathbf{S} = \frac{1}{\varepsilon_0}\int_V \rho \, dV
$$

转化为微分形式，由散度定义得

$$
\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0} \tag{1.8}
$$

这表明电荷是电场的源，电场线从正电荷发出终止于负电荷。

#### 3. 静电场的旋度

由库仑定律可证静电场的环量为零：

$$
\oint_L \mathbf{E} \cdot d\mathbf{l} = 0
$$

对任意闭合回路成立，转化为微分形式得

$$
\nabla \times \mathbf{E} = 0 \tag{1.10}
$$

表明静电场是无旋场（保守场）。

**例**：半径为 $a$ 的均匀带电球体（总电荷 $Q$），求电场强度并计算散度。

解：由高斯定理，当 $r > a$ 时

$$
\mathbf{E} = \frac{Q}{4\pi\varepsilon_0 r^2}\mathbf{e}_r
$$

当 $r < a$ 时

$$
\mathbf{E} = \frac{Qr}{4\pi\varepsilon_0 a^3}\mathbf{e}_r
$$

散度计算表明，电场的散度只存在于有电荷分布的区域内，没有电荷处 $\nabla \cdot \mathbf{E} = 0$。

---

### §1.2 电流和磁场

#### 1. 电荷守恒定律

电流密度矢量 $\mathbf{J}$ 的方向沿电流方向，数值等于单位时间垂直通过单位面积的电荷量。通过任意曲面 $S$ 的电流为

$$
I = \int_S \mathbf{J} \cdot d\mathbf{S}
$$

若电流由带电粒子构成，设电荷密度为 $\rho$，平均速度为 $\mathbf{v}$，则 $\mathbf{J} = \rho\mathbf{v}$。

**电荷守恒定律**（连续性方程）的积分形式：

$$
\oint_S \mathbf{J} \cdot d\mathbf{S} = -\frac{d}{dt}\int_V \rho \, dV
$$

微分形式：

$$
\nabla \cdot \mathbf{J} + \frac{\partial \rho}{\partial t} = 0 \tag{2.5}
$$

对于恒定电流 $\partial\rho/\partial t = 0$，有 $\nabla \cdot \mathbf{J} = 0$，流线必为闭合曲线。

#### 2. 毕奥-萨伐尔定律

电流元 $Id\mathbf{l}$ 在磁场中所受的力为

$$
d\mathbf{F} = Id\mathbf{l} \times \mathbf{B}
$$

磁感应强度 $\mathbf{B}$ 描述磁场的性质。恒定电流激发磁场的规律为**毕奥-萨伐尔定律**：

$$
\mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi}\int_V \frac{\mathbf{J}(\mathbf{r}') \times \mathbf{e}_{|\mathbf{r}-\mathbf{r}'|}}{|\mathbf{r}-\mathbf{r}'|^2} \, dV' \tag{2.8a}
$$

对于细导线：

$$
\mathbf{B}(\mathbf{r}) = \frac{\mu_0 I}{4\pi}\oint \frac{d\mathbf{l}' \times \mathbf{e}_{|\mathbf{r}-\mathbf{r}'|}}{|\mathbf{r}-\mathbf{r}'|^2} \tag{2.8b}
$$

#### 3. 磁场的环量和旋度

**安培环路定律**的积分形式：

$$
\oint_L \mathbf{B} \cdot d\mathbf{l} = \mu_0 I \tag{2.9}
$$

对于连续电流分布：

$$
\oint_L \mathbf{B} \cdot d\mathbf{l} = \mu_0 \int_S \mathbf{J} \cdot d\mathbf{S} \tag{2.10}
$$

微分形式：

$$
\nabla \times \mathbf{B} = \mu_0 \mathbf{J} \tag{2.11}
$$

#### 4. 磁场的散度

磁感应线是闭合曲线，磁场是无源场：

$$
\oint_S \mathbf{B} \cdot d\mathbf{S} = 0 \quad \Rightarrow \quad \nabla \cdot \mathbf{B} = 0 \tag{2.13}
$$

（目前尚无磁单极子存在的实验证据。）

#### 5. 磁场旋度和散度公式的证明

由毕奥-萨伐尔定律可严格推出 $\nabla \times \mathbf{B} = \mu_0 \mathbf{J}$ 和 $\nabla \cdot \mathbf{B} = 0$，详见书中推导。

**例**：电流均匀分布于半径为 $a$ 的无穷长直导线内，求空间各点的磁感应强度并计算旋度。

解：当 $r > a$ 时

$$
\mathbf{B} = \frac{\mu_0 I}{2\pi r}\mathbf{e}_\phi
$$

当 $r < a$ 时

$$
\mathbf{B} = \frac{\mu_0 I r}{2\pi a^2}\mathbf{e}_\phi
$$

旋度：$r > a$ 处 $\nabla \times \mathbf{B} = 0$；$r < a$ 处 $\nabla \times \mathbf{B} = \mu_0 \mathbf{J}$。旋度概念的局域性表明某点的旋度只与该点的电流密度有关。

---

### §1.3 麦克斯韦方程组

#### 1. 电磁感应定律

法拉第发现：闭合线圈中的感应电动势与通过该线圈内部的磁通量变化率成正比，

$$
\mathcal{E} = -\frac{d\Phi}{dt} \tag{3.1}
$$

感应电动势是电场强度沿闭合回路的线积分，因此

$$
\oint_L \mathbf{E} \cdot d\mathbf{l} = -\frac{\partial}{\partial t}\int_S \mathbf{B} \cdot d\mathbf{S}
$$

微分形式：

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \tag{3.3}
$$

表明变化磁场激发（有旋）电场。

#### 2. 位移电流

恒定电流满足 $\nabla \cdot \mathbf{J} = 0$；但非恒定情况下一般有 $\nabla \cdot \mathbf{J} \neq 0$，此时安培定律 $\nabla \times \mathbf{B} = \mu_0 \mathbf{J}$ 与电荷守恒定律矛盾。

麦克斯韦引入**位移电流**假设：

$$
\mathbf{J}_d = \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} \tag{3.9}
$$

要求 $\mathbf{J} + \mathbf{J}_d$ 闭合（无散），即将安培定律修正为

$$
\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0\varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} \tag{3.5}
$$

位移电流的物理实质是变化的电场激发磁场。

#### 3. 麦克斯韦方程组

综合以上结果，得到一般情况下互相协调的方程组（国际单位制）：

$$
\boxed{
\begin{aligned}
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu_0\mathbf{J} + \mu_0\varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} \\
\nabla \cdot \mathbf{E} &= \frac{\rho}{\varepsilon_0} \\
\nabla \cdot \mathbf{B} &= 0
\end{aligned}
} \tag{3.10}
$$

**重要意义**：
- 电荷、电流可以激发电磁场
- 变化的电场和磁场可以互相激发
- 某处发生电磁扰动，通过互相激发在空间中传播形成电磁波
- 麦克斯韦从理论上预言电磁波的存在，并指出光波是一种电磁波

#### 4. 洛伦兹力公式

场对电荷系统的作用力密度为

$$
\mathbf{f} = \rho\mathbf{E} + \mathbf{J} \times \mathbf{B} \tag{3.11}
$$

对于带电粒子：

$$
\mathbf{F} = q\mathbf{E} + q\mathbf{v} \times \mathbf{B} \tag{3.12}
$$

麦克斯韦方程组与洛伦兹力公式构成经典电动力学的理论基础。

---

### §1.4 介质的电磁性质

#### 1. 关于介质的概念

介质由分子组成，分子内部有带正电的原子核和绕核运动的电子。介质是电中性的，在外场作用下出现极化和磁化现象，产生**束缚电荷**和**磁化电流**分布。

#### 2. 介质的极化

用**电极化强度**矢量 $\mathbf{P}$ 描述介质的极化程度：

$$
\mathbf{P} = \frac{\sum \mathbf{p}_i}{\Delta V} \tag{4.1}
$$

其中 $\mathbf{p}_i = q\mathbf{l}$ 为分子电偶极矩。

束缚电荷体密度：

$$
\rho_p = -\nabla \cdot \mathbf{P} \tag{4.3}
$$

界面上的面束缚电荷密度：

$$
\sigma_p = -(\mathbf{P}_2 - \mathbf{P}_1) \cdot \mathbf{e}_n \tag{4.4}
$$

#### 3. 介质的磁化

类似地，用**磁化强度**矢量 $\mathbf{M}$ 描述介质的磁化程度。

磁化电流体密度：

$$
\mathbf{J}_M = \nabla \times \mathbf{M}
$$

界面上磁化电流面密度：

$$
\mathbf{K}_M = (\mathbf{M}_2 - \mathbf{M}_1) \times \mathbf{e}_n
$$

#### 4. 介质的电磁性质方程组

引入电位移矢量 $\mathbf{D}$ 和磁场强度 $\mathbf{H}$：

$$
\mathbf{D} = \varepsilon_0 \mathbf{E} + \mathbf{P}, \quad \mathbf{B} = \mu_0 (\mathbf{H} + \mathbf{M})
$$

对于线性各向同性介质：

$$
\mathbf{P} = \varepsilon_0 \chi_e \mathbf{E}, \quad \mathbf{D} = \varepsilon \mathbf{E}, \quad \varepsilon = \varepsilon_0(1+\chi_e)
$$

$$
\mathbf{M} = \chi_m \mathbf{H}, \quad \mathbf{B} = \mu \mathbf{H}, \quad \mu = \mu_0(1+\chi_m)
$$

其中 $\chi_e$、$\chi_m$ 分别为电极化率和磁化率，$\varepsilon$、$\mu$ 为介电常量和磁导率。

**有介质时的麦克斯韦方程组**：

$$
\boxed{
\begin{aligned}
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{H} &= \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t} \\
\nabla \cdot \mathbf{D} &= \rho_f \\
\nabla \cdot \mathbf{B} &= 0
\end{aligned}
}
$$

其中 $\rho_f$ 为自由电荷密度，$\mathbf{J}$ 为自由电流密度。

---

### §1.5 电磁场边值关系

#### 1. 电场和磁场的边值关系

在两种介质的分界面上，电场和磁场的法向分量和切向分量满足边值关系：

**电场**：
- $\mathbf{E}_1^t = \mathbf{E}_2^t$（电场切向分量连续）
- $\mathbf{D}_2^n - \mathbf{D}_1^n = \sigma_f$（电位移法向分量跃变等于自由面电荷密度）

**磁场**：
- $\mathbf{H}_1^t - \mathbf{H}_2^t = \mathbf{K}_f \times \mathbf{e}_n$（磁场切向分量跃变等于自由面电流密度）
- $\mathbf{B}_2^n = \mathbf{B}_1^n$（磁感应法向分量连续）

矢量形式汇总：

$$
\boxed{
\begin{aligned}
\mathbf{e}_n \times (\mathbf{E}_2 - \mathbf{E}_1) &= 0 \\
\mathbf{e}_n \times (\mathbf{H}_2 - \mathbf{H}_1) &= \mathbf{K}_f \\
\mathbf{e}_n \cdot (\mathbf{D}_2 - \mathbf{D}_1) &= \sigma_f \\
\mathbf{e}_n \cdot (\mathbf{B}_2 - \mathbf{B}_1) &= 0
\end{aligned}
} \tag{5.11}
$$

其中 $\mathbf{e}_n$ 为由介质1指向介质2的法向单位矢量。

#### 2. 电磁场边值关系的推导

由麦克斯韦方程组的积分形式，利用斯托克斯定理和散度定理，可推导上述边值关系。这些关系在求解电磁场边值问题（尤其在波导和谐振腔问题）中具有重要作用。

---

### §1.6 电磁场的能量和能流

#### 1. 场和电荷系统的能量守恒定律的一般形式

考虑空间某区域 $V$，其界面为 $S$。能量守恒定律要求：单位时间通过界面 $S$ 流入 $V$ 内的能量等于场对 $V$ 内电荷作功的功率与 $V$ 内电磁场能量增加率之和。

积分形式：

$$
-\oint_S \mathbf{S} \cdot d\mathbf{S} = \int_V \mathbf{J} \cdot \mathbf{E} \, dV + \frac{d}{dt}\int_V w \, dV \tag{6.1}
$$

微分形式：

$$
\nabla \cdot \mathbf{S} + \frac{\partial w}{\partial t} = -\mathbf{J} \cdot \mathbf{E} \tag{6.2}
$$

#### 2. 电磁场能量密度和能流密度表示式

由麦克斯韦方程组和洛伦兹力公式可推出：

**坡印廷矢量**（能流密度）：

$$
\mathbf{S} = \mathbf{E} \times \mathbf{H} \tag{6.8}
$$

**电磁场能量密度**：

$$
w = \frac{1}{2}(\mathbf{E} \cdot \mathbf{D} + \mathbf{B} \cdot \mathbf{H}) \tag{6.12}
$$

在真空中：

$$
w = \frac{1}{2}\left(\varepsilon_0 E^2 + \frac{B^2}{\mu_0}\right), \quad \mathbf{S} = \frac{1}{\mu_0}\mathbf{E} \times \mathbf{B}
$$

#### 3. 电磁能量的传输

坡印廷矢量 $\mathbf{S}$ 描述电磁能量的传输方向和大小。在恒定情况下，通过闭合曲面的电磁能量净流入等于该区域内带电粒子所受的功率。

**例**：同轴传输线（内导线半径 $a$，外导线半径 $b$，填充电介质），载有电流 $I$、电压 $U$。介质中能流密度 $\mathbf{S} = E_\rho H_\phi \mathbf{e}_z$（轴向），传输功率 $P = UI$。当导线有有限电导率时，能流有径向分量进入导线，供给导线的焦耳热损耗。

---

## 第二章 静电场

本章研究静电场的基本理论：在给定的自由电荷分布以及周围空间介质和导体分布的情况下，求解静电场。

---

### §2.1 静电场的标势及其微分方程

#### 1. 静电场的标势

静电情况下，电场部分满足：

$$
\nabla \times \mathbf{E} = 0 \tag{1.1}, \quad \nabla \cdot \mathbf{D} = \rho \tag{1.2}
$$

由无旋性，可引入标势 $\varphi$ 描述静电场：

$$
\mathbf{E} = -\nabla \varphi \tag{1.5}
$$

电荷由 $P_1$ 移至 $P_2$ 时电场作功与路径无关，电势差定义为

$$
\varphi(P_2) - \varphi(P_1) = -\int_{P_1}^{P_2} \mathbf{E} \cdot d\mathbf{l} \tag{1.4}
$$

对于有限区域分布的电荷，选无穷远点为参考点 $\varphi(\infty) = 0$，则

$$
\varphi(\mathbf{r}) = \frac{1}{4\pi\varepsilon}\int_V \frac{\rho(\mathbf{r}')}{|\mathbf{r}-\mathbf{r}'|} dV' \tag{1.7}
$$

#### 2. 静电势的微分方程和边值关系

在均匀各向同性线性介质中，代入 $\mathbf{D} = \varepsilon\mathbf{E}$ 和 $\mathbf{E} = -\nabla\varphi$，得**泊松方程**：

$$
\nabla^2 \varphi = -\frac{\rho}{\varepsilon} \tag{1.8}
$$

在两介质界面上，电势满足边值关系：
- **电势连续**：$\varphi_1 = \varphi_2$
- **法向分量跃变**：$\varepsilon_2 \frac{\partial \varphi_2}{\partial n} - \varepsilon_1 \frac{\partial \varphi_1}{\partial n} = \sigma_f$

**导体的静电条件**：导体内部电场为零；电荷只分布于导体表面上；导体表面为等势面。

导体表面边界条件：$\varphi|_{\text{导体表面}} = \text{常量}$，$\varepsilon \frac{\partial \varphi}{\partial n} = \sigma_f$。

#### 3. 静电场能量

线性介质中静电场总能量：

$$
W = \frac{1}{2}\int_V \mathbf{E} \cdot \mathbf{D} \, dV = \frac{1}{2}\int_V \rho \varphi \, dV \tag{1.13, 1.14}
$$

注意：$\frac{1}{2}\rho\varphi$ 不是能量密度，因为能量分布于整个电场内，而不仅在电荷分布区域内。

**例**：均匀带电无限长直导线（电荷线密度 $\tau$），选距导线垂直距离 $R$ 处 $\varphi(R) = 0$，则电势

$$
\varphi(\rho) = -\frac{\tau}{2\pi\varepsilon}\ln\frac{\rho}{R} \tag{1.17}
$$

**例**：带电荷量 $Q$、半径为 $a$ 的导体球，球面电势 $\varphi = Q/4\pi\varepsilon_0 a$，静电场总能量 $W = \frac{Q^2}{8\pi\varepsilon_0 a}$。

---

### §2.2 唯一性定理

#### 1. 静电问题的唯一性定理

**唯一性定理**：设区域 $V$ 内给定自由电荷分布 $\rho(\mathbf{r})$，在 $V$ 的边界 $S$ 上给定：
- (1) 电势 $\varphi|_S$ 或
- (2) 电势的法向偏导数 $\frac{\partial \varphi}{\partial n}|_S$

则 $V$ 内的电场唯一地确定。

**证明**：设两组不同的解 $\varphi$ 和 $\varphi'$，令 $\psi = \varphi - \varphi'$。在每个均匀区域内 $\nabla^2 \psi = 0$；在内部分界面上 $\psi$ 连续、$\varepsilon \frac{\partial \psi}{\partial n}$ 连续；在边界 $S$ 上 $\psi|_S = 0$ 或 $\frac{\partial \psi}{\partial n}|_S = 0$。利用积分

$$
\oint_S \psi \frac{\partial \psi}{\partial n} dS = \int_V \varepsilon (\nabla \psi)^2 dV
$$

左边由边界条件为零，故 $\int_V (\nabla \psi)^2 dV = 0$，从而 $\nabla \psi = 0$，即 $\psi = \text{常数}$。由边界条件得常数为零，故 $\varphi = \varphi'$ 唯一。

#### 2. 有导体存在时的唯一性定理

若区域 $V$ 内有 $n$ 个导体，给定每个导体所带的总电荷 $Q_i$（或电势），则静电场唯一确定。

实际求解时，可根据条件提出尝试解，若满足唯一性定理所要求的全部条件，就是唯一正确的解。

---

### §2.3 拉普拉斯方程——分离变量法

当空间无自由电荷（$\rho = 0$）时，泊松方程化为**拉普拉斯方程**：

$$
\nabla^2 \varphi = 0
$$

#### 1. 球坐标系下的分离变量

在球坐标系 $(r, \theta, \phi)$ 中，拉普拉斯方程的通解为

$$
\varphi(r, \theta, \phi) = \sum_{l=0}^{\infty} \sum_{m=-l}^{l} \left[ \left(A_l^m r^l + \frac{B_l^m}{r^{l+1}}\right) Y_l^m(\theta, \phi) \right]
$$

其中 $Y_l^m(\theta, \phi)$ 为球面调和函数。

对于轴对称情况（$\frac{\partial}{\partial \phi} = 0$），解简化为

$$
\varphi(r, \theta) = \sum_{l=0}^{\infty} \left[ \left(A_l r^l + \frac{B_l}{r^{l+1}}\right) P_l(\cos\theta) \right]
$$

其中 $P_l(\cos\theta)$ 为勒让德多项式。

#### 2. 柱坐标系下的分离变量

在柱坐标系 $(\rho, \phi, z)$ 中，拉普拉斯方程的通解涉及贝塞尔函数和指数函数。

#### 3. 格林函数

引入格林函数 $G(\mathbf{r}, \mathbf{r}')$，满足

$$
\nabla^2 G = -\delta(\mathbf{r} - \mathbf{r}')
$$

边值问题的解可表为

$$
\varphi(\mathbf{r}) = \int_V G(\mathbf{r}, \mathbf{r}')\rho(\mathbf{r}') dV' + \oint_S \left[ \varphi \frac{\partial G}{\partial n} - G \frac{\partial \varphi}{\partial n} \right] dS
$$

---

### §2.4 电多极矩

#### 1. 电势的多极展开

设电荷分布于有限区域 $V$ 内，考察远离电荷分布处的电势展开。取源点为原点，场点距原点为 $r$，当 $r \gg r'$（$r'$ 为电荷分布区域的特征尺度）时，

$$
\frac{1}{|\mathbf{r} - \mathbf{r}'|} = \frac{1}{r} + \frac{\mathbf{r}' \cdot \mathbf{r}}{r^3} + \cdots
$$

代入电势积分表达式，得电势的多极展开式：

$$
\varphi(\mathbf{r}) = \frac{1}{4\pi\varepsilon_0}\left[ \frac{Q}{r} + \frac{\mathbf{p} \cdot \mathbf{r}}{r^3} + \frac{1}{6}\sum_{i,j} Q_{ij} \frac{r_i r_j}{r^5} + \cdots \right]
$$

其中：
- $Q = \int_V \rho(\mathbf{r}') dV'$ —— **总电荷**（单极矩）
- $\mathbf{p} = \int_V \rho(\mathbf{r}') \mathbf{r}' dV'$ —— **电偶极矩**（一阶矩）
- $Q_{ij} = \int_V \rho(\mathbf{r}')(3x_i' x_j' - r'^2 \delta_{ij}) dV'$ —— **电四极矩张量**（二阶矩）

#### 2. 电多极矩

电四极矩张量是对称张量，满足 $Q_{ii} = 0$（缩并），独立分量只有5个。电四极矩在原子核物理中有重要应用。

#### 3. 电荷体系在外电场中的能量

一个电荷体系在外电场 $\mathbf{E}$ 中的电势能为

$$
W = Q\varphi(\mathbf{r}_0) - \mathbf{p} \cdot \mathbf{E}(\mathbf{r}_0) + \cdots
$$

当外电场缓变时，高阶项可忽略，最低阶项正是电偶极矩与电场的相互作用 $- \mathbf{p} \cdot \mathbf{E}$。

---

> 本章小结：静电场是有源无旋场，可引入标势 $\varphi$ 描述；$\varphi$ 满足泊松方程（$\rho \neq 0$）或拉普拉斯方程（$\rho = 0$）；唯一性定理是求解边值问题的理论依据；分离变量法和电多极展开是重要的求解方法。

---

## 第三章 静磁场

本章讨论恒定电流分布所激发的静磁场。恒定情况下，电场和磁场不发生直接联系，因而可以把磁场和电场分离开来求解。和静电场的标势相对应，静磁场的矢势是一个重要的概念。

---

### §3.1 矢势及其微分方程

#### 1. 矢势

恒定电流磁场的基本方程是

$$
\nabla \times \mathbf{H} = \mathbf{J} \tag{1.1}, \quad \nabla \cdot \mathbf{B} = 0 \tag{1.2}
$$

静电场是有源无旋场（$\nabla \times \mathbf{E} = 0$，$\nabla \cdot \mathbf{D} = \rho$），静磁场则是有旋无源场（$\nabla \times \mathbf{H} = \mathbf{J}$，$\nabla \cdot \mathbf{B} = 0$）。由于磁场的无源性，磁感应强度 $\mathbf{B}$ 可表为另一矢量的旋度：

$$
\mathbf{B} = \nabla \times \mathbf{A} \tag{1.3}
$$

$\mathbf{A}$ 称为磁场的**矢势**。

矢势 $\mathbf{A}$ 的物理意义：沿任一闭合回路的环量代表通过以该回路为边界的任一曲面的磁通量。只有 $\mathbf{A}$ 的环量才有物理意义，每点上的 $\mathbf{A}(\mathbf{r})$ 值没有直接的物理意义。

矢势具有**规范任意性**：若 $\mathbf{A}$ 满足 $\nabla \times \mathbf{A} = \mathbf{B}$，则 $\mathbf{A}' = \mathbf{A} + \nabla \chi$ 也满足 $\nabla \times \mathbf{A}' = \mathbf{B}$，因为 $\nabla \times (\nabla \chi) = 0$。可对 $\mathbf{A}$ 加上辅助的**规范条件**：

$$
\nabla \cdot \mathbf{A} = 0 \tag{1.5}
$$

这总可以通过适当的规范变换做到。

#### 2. 矢势微分方程

在线性均匀介质中，$\mathbf{B} = \mu \mathbf{H}$，代入 $\mathbf{B} = \nabla \times \mathbf{A}$，利用矢量公式 $\nabla \times (\nabla \times \mathbf{A}) = \nabla(\nabla \cdot \mathbf{A}) - \nabla^2 \mathbf{A}$，取规范条件 $\nabla \cdot \mathbf{A} = 0$，得矢势的微分方程（泊松方程型）：

$$
\nabla^2 \mathbf{A} = -\mu \mathbf{J} \tag{1.8}
$$

每个直角分量 $A_i$ 满足 $\nabla^2 A_i = -\mu J_i$，与静电势的泊松方程形式相同。

其特解为

$$
\mathbf{A}(\mathbf{r}) = \frac{\mu}{4\pi}\int_V \frac{\mathbf{J}(\mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|} dV' \tag{1.9}
$$

对细导线情形，过渡到线电流 $I$：

$$
\mathbf{B}(\mathbf{r}) = \frac{\mu_0 I}{4\pi}\oint \frac{d\mathbf{l}' \times \mathbf{e}_{|\mathbf{r}-\mathbf{r}'|}}{|\mathbf{r}-\mathbf{r}'|^2} \tag{1.11}
$$

这正是毕奥-萨伐尔定律。

#### 3. 矢势边值关系

在两介质分界面上，矢势 $\mathbf{A}$ 满足：

- $\mathbf{A}$ 的切向分量连续：$A_{1t} = A_{2t}$（由界面两侧 $\mathbf{A}$ 连续可推出）
- 规范下 $\nabla \cdot \mathbf{A} = 0$ 时，$\mathbf{A}$ 的法向分量也连续：$A_{1n} = A_{2n}$

合起来即：在界面上矢势 $\mathbf{A}$ 是连续的。

#### 4. 静磁场的能量

磁场的总能量：

$$
W = \frac{1}{2}\int_V \mathbf{H} \cdot \mathbf{B} \, dV \tag{1.19}
$$

用矢势和电流表示：

$$
W = \frac{1}{2}\int_V \mathbf{J} \cdot \mathbf{A} \, dV \tag{1.20}
$$

电流 $J$ 在外磁场 $\mathbf{A}_{\text{外}}$ 中的相互作用能：

$$
W_{\text{互}} = \int_V \mathbf{J} \cdot \mathbf{A}_{\text{外}} \, dV \tag{1.22}
$$

**例1**：无穷长直导线载电流 $I$，求矢势和磁感应强度。

解：取导线沿 $z$ 轴，场点到导线垂直距离为 $\rho$，两点矢势差：

$$
A_z = -\frac{\mu_0 I}{2\pi}\ln\frac{\rho}{R_0} \tag{1.23}
$$

取旋度得

$$
\mathbf{B} = \frac{\mu_0 I}{2\pi\rho}\mathbf{e}_\phi \tag{1.24}
$$

**例2**：半径为 $a$ 的导线圆环载电流 $I$，求矢势和磁感应强度。在远场 $(R \gg a)$：

$$
\mathbf{B} = \frac{\mu_0 I a^2}{2R^3}(2\cos\theta \mathbf{e}_R + \sin\theta \mathbf{e}_\theta) \tag{1.30}
$$

即磁偶极子场。

---

### §3.2 磁标势

#### 1. 磁标势的存在条件

在电流分布区域以外（$\mathbf{J} = 0$），磁场满足 $\nabla \times \mathbf{H} = 0$，可引入磁标势 $\varphi_m$：

$$
\mathbf{H} = -\nabla \varphi_m \tag{2.10}
$$

条件：该区域内任何回路都不被自由电流所链环（即该区域是没有自由电流分布的单连通区域）。

永磁体的磁场（完全由分子电流激发，没有任何自由电流）可以在全空间（包括磁铁内部）都用磁标势描述。

#### 2. 磁标势的微分方程

在 $\mathbf{J} = 0$ 区域内，$\nabla \times \mathbf{H} = 0$ 和 $\nabla \cdot \mathbf{B} = 0$ 结合 $\mathbf{B} = \mu_0(\mathbf{H} + \mathbf{M})$，得

$$
\nabla^2 \varphi_m = -\frac{\rho_m}{\mu_0} \tag{2.16}
$$

其中 $\rho_m = -\mu_0 \nabla \cdot \mathbf{M}$ 为假想磁荷密度。

#### 3. 静电场与静磁场的对比

| 静电场 | 静磁场 |
|--------|--------|
| $\nabla \times \mathbf{E} = 0$ | $\nabla \times \mathbf{H} = 0$ |
| $\nabla \cdot \mathbf{D} = \rho_f$ | $\nabla \cdot \mathbf{B} = 0$ |
| $\mathbf{E} = -\nabla \varphi$ | $\mathbf{H} = -\nabla \varphi_m$ |
| $\nabla^2 \varphi = -\rho/\varepsilon$ | $\nabla^2 \varphi_m = -\rho_m/\mu_0$ |
| $\mathbf{D} = \varepsilon \mathbf{E}$ | $\mathbf{B} = \mu \mathbf{H}$ |

**例**：均匀磁化铁球（磁化强度 $\mathbf{M}_0$），球外磁场为磁偶极子场，球内磁场 $\mathbf{B} = \frac{2}{3}\mu_0 \mathbf{M}_0$（常量）。

---

### §3.3 磁多极矩

#### 1. 矢势的多极展开

设电流分布于有限区域 $V$，考察远离电流分布处的矢势展开。当 $r \gg r'$ 时：

$$
\mathbf{A}(\mathbf{r}) = \frac{\mu_0}{4\pi}\left[ \frac{\mathbf{m}}{r^3} + \cdots \right] \tag{3.1}
$$

其中 $\mathbf{m} = \frac{1}{2}\int_V \mathbf{r}' \times \mathbf{J}(\mathbf{r}') dV'$ 为**磁偶极矩**。

对于平面电流线圈，若面积为 $S$、电流为 $I$，则 $\mathbf{m} = I S \mathbf{e}_n$。

#### 2. 磁偶极矩的场和磁标势

磁偶极矩 $\mathbf{m}$ 在远处激发的磁场：

$$
\mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi r^3}[3(\mathbf{m} \cdot \mathbf{e}_r)\mathbf{e}_r - \mathbf{m}] + O(r^{-4})
$$

相应地，磁标势（远场）为

$$
\varphi_m(\mathbf{r}) = \frac{\mathbf{m} \cdot \mathbf{e}_r}{4\pi r^2}
$$

#### 3. 小区域内电流分布在外磁场中的能量

小区域电流分布在外磁场 $\mathbf{B}_{\text{外}}$ 中的相互作用能量：

$$
W = -\mathbf{m} \cdot \mathbf{B}_{\text{外}} \tag{3.4}
$$

---

### §3.4 阿哈罗诺夫-玻姆效应

在量子力学中，即使在 $\mathbf{E} = 0$ 和 $\mathbf{B} = 0$ 的区域，电磁势 $\varphi$ 和 $\mathbf{A}$ 仍可产生可观测的物理效应。

**阿哈罗诺夫-玻姆效应**：电子束分成两束，在各自路径上 $\mathbf{B} = 0$（但 $\mathbf{A} \neq 0$），会合后出现干涉条纹。干涉相位差与矢势 $\mathbf{A}$ 沿路径的环量相关：

$$
\Delta \phi = \frac{e}{\hbar}\oint \mathbf{A} \cdot d\mathbf{l} = \frac{e}{\hbar}\Phi_B
$$

其中 $\Phi_B$ 为通过两路径所围面积的磁通量。

这表明矢势 $\mathbf{A}$ 具有可观测的物理效应，规范场论正是建立在势的物理效应之上的。

---

### §3.5 超导体的电磁性质

#### 1. 概述

超导体具有零电阻效应和完全抗磁性（迈斯纳效应）。在临界温度 $T_c$ 以下，超导体转入超导态。

#### 2. 超导体的基本现象

- **零电阻**：超导体电阻为零，电流可以在其中无衰减地流动
- **完全抗磁性（迈斯纳效应）**：超导体内部 $\mathbf{B} = 0$，外磁场被排斥出超导体外

#### 3. 伦敦唯象理论与皮帕德修正

**伦敦方程**（描述超导电流与电磁场的关系）：

$$
\nabla \times \mathbf{J}_s = -\frac{n_s e^2}{m}\mathbf{B} \tag{5.1}
$$

或等价地

$$
\nabla \times \mathbf{B} = \mu_0 \mathbf{J}_s \tag{5.2}
$$

联立麦克斯韦方程可得：

$$
\nabla^2 \mathbf{B} = \frac{\mathbf{B}}{\lambda_L^2}, \quad \lambda_L = \sqrt{\frac{m}{\mu_0 n_s e^2}} \tag{5.5}
$$

其中 $\lambda_L$ 为伦敦穿透深度。超导体内部磁场按指数规律衰减，$\lambda_L$ 量级为 $10^{-2}\mu\text{m}$。

皮帕德非局域修正：当相干长度 $\xi$ 与穿透深度可比拟时，伦敦理论需要修正。

#### 4. 磁通量子化

在超导体环中，磁通量 $\Phi$ 是量子化的：

$$
\Phi = n\Phi_0, \quad \Phi_0 = \frac{h}{2e} \approx 2.07 \times 10^{-15}\ \text{Wb}
$$

这是超导量子干涉的基础。

---

> 本章小结：静磁场是有旋无源场，可用矢势 $\mathbf{A}$ 描述（$\mathbf{B} = \nabla \times \mathbf{A}$）；矢势满足泊松方程 $\nabla^2 \mathbf{A} = -\mu \mathbf{J}$；在没有电流分布的单连通区域可用磁标势 $\varphi_m$ 描述；电流分布在远处产生磁偶极场，能量 $-\mathbf{m} \cdot \mathbf{B}$；超导体具有完全抗磁性和磁通量子化特性。

---

## 第四章 电磁波的传播

在迅变情况下，电磁场以波动形式存在。变化着的电场和磁场互相激发，形成在空间中传播的电磁波。本章研究无界空间中平面电磁波传播的主要特性，以及电磁波在介质界面上的反射和折射、有导体存在时的传播和有界空间中的电磁波问题。

---

### §4.1 平面电磁波

#### 1. 电磁场波动方程

在自由空间（$\rho = 0$，$\mathbf{J} = 0$）中，麦克斯韦方程组化为

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}, \quad \nabla \times \mathbf{H} = \frac{\partial \mathbf{D}}{\partial t}, \quad \nabla \cdot \mathbf{D} = 0, \quad \nabla \cdot \mathbf{B} = 0
$$

取第一式旋度并利用第二式，在真空中 $\mathbf{D} = \varepsilon_0 \mathbf{E}$，$\mathbf{B} = \mu_0 \mathbf{H}$，得

$$
\nabla^2 \mathbf{E} - \mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{E}}{\partial t^2} = 0 \tag{1.4a}
$$

$$
\nabla^2 \mathbf{B} - \mu_0 \varepsilon_0 \frac{\partial^2 \mathbf{B}}{\partial t^2} = 0 \tag{1.4b}
$$

这是波动方程。令

$$
c = \frac{1}{\sqrt{\mu_0 \varepsilon_0}} \approx 3 \times 10^8\ \text{m/s}
$$

则电磁波在真空中的传播速度为 $c$（光速）。

#### 2. 时谐电磁波

设角频率为 $\omega$，场量对时间的依赖关系为 $e^{-i\omega t}$（复数形式）。在一定频率下，对线性均匀介质有 $\mathbf{D} = \varepsilon \mathbf{E}$，$\mathbf{B} = \mu \mathbf{H}$，麦克斯韦方程组化为

$$
\nabla \times \mathbf{E} = i\omega \mathbf{B}, \quad \nabla \times \mathbf{H} = -i\omega \mathbf{D}, \quad \nabla \cdot \mathbf{E} = 0, \quad \nabla \cdot \mathbf{H} = 0
$$

取旋度并消去，得**亥姆霍兹方程**：

$$
\nabla^2 \mathbf{E} + k^2 \mathbf{E} = 0, \quad k = \omega \sqrt{\mu \varepsilon} \tag{1.13}
$$

其中 $k$ 为波数。电磁场还需满足 $\nabla \cdot \mathbf{E} = 0$。

#### 3. 平面电磁波

设电磁波沿 $z$ 轴方向传播，在与 $z$ 轴正交的平面上各点场强相同，仅与 $z$ 和 $t$ 有关，这种波称为**平面电磁波**。

一维亥姆霍兹方程的解：

$$
E(z) = E_0 e^{ikz} \tag{1.18}
$$

完整时谐平面波：

$$
\mathbf{E}(z, t) = \mathbf{E}_0 e^{i(kz - \omega t)} \tag{1.19}
$$

由 $\nabla \cdot \mathbf{E} = 0$，可知 $\mathbf{E}$ 与传播方向垂直（横波），即 $\mathbf{E} \perp \mathbf{e}_z$。

**相速度**：

$$
v_p = \frac{\omega}{k} = \frac{1}{\sqrt{\mu \varepsilon}} = \frac{c}{n} \tag{1.21}
$$

其中 $n = \sqrt{\varepsilon_r \mu_r}$ 为介质的折射率。

对于时谐场，取实部：

$$
\mathbf{E}(z, t) = \mathbf{E}_0 \cos(kz - \omega t)
$$

$k = \frac{2\pi}{\lambda}$，$\lambda$ 为波长。

**波阻抗**（介质的本征阻抗）：

$$
\eta = \sqrt{\frac{\mu}{\varepsilon}}, \quad \text{真空中}\ \eta_0 = \sqrt{\frac{\mu_0}{\varepsilon_0}} \approx 377\ \Omega \tag{1.22}
$$

在平面波中，$\mathbf{E}$、$\mathbf{H}$ 和传播方向 $\mathbf{e}_k$ 两两正交，且

$$
\mathbf{B} = \frac{1}{c}\mathbf{e}_k \times \mathbf{E} \quad \text{（真空中）}
$$

或一般介质中 $\sqrt{\mu}\mathbf{H} = \sqrt{\varepsilon}\mathbf{e}_k \times \mathbf{E}$。

#### 4. 电磁波的能量和能流

电磁场能量密度：

$$
w = \frac{1}{2}(\mathbf{E} \cdot \mathbf{D} + \mathbf{B} \cdot \mathbf{H}) = \frac{1}{2}\varepsilon E^2 + \frac{1}{2\mu}B^2
$$

**坡印廷矢量**：

$$
\mathbf{S} = \mathbf{E} \times \mathbf{H}
$$

对于平面电磁波，$\mathbf{S} = w v_p \mathbf{e}_k$，能量以相速度 $v_p$ 沿传播方向传输。

---

### §4.2 电磁波在介质界面上的反射和折射

#### 1. 反射和折射定律

当平面电磁波入射到两介质分界面上时，产生反射波和折射波。由边值关系和相位匹配条件，可导出**斯涅尔定律**（反射和折射定律）：

$$
\frac{\sin \theta_i}{\sin \theta_t} = \frac{n_2}{n_1}, \quad \theta_i = \theta_r
$$

其中 $\theta_i$、$\theta_r$、$\theta_t$ 分别为入射角、反射角和折射角，$n_1$、$n_2$ 为两介质的折射率。

#### 2. 振幅关系——菲涅耳公式

设入射面为 $xz$ 平面，入射波、反射波和折射波的电场分解为垂直入射面（$s$ 波）和平行入射面（$p$ 波）两个分量。

**菲涅耳公式**（振幅关系）：

对于 $s$ 波（垂直入射面）：

$$
r_s = \frac{E_{0r}}{E_{0i}} = \frac{\cos \theta_i - \sqrt{\varepsilon_2/\varepsilon_1 - \sin^2 \theta_i}}{\cos \theta_i + \sqrt{\varepsilon_2/\varepsilon_1 - \sin^2 \theta_i}} \tag{2.8}
$$

$$
t_s = \frac{E_{0t}}{E_{0i}} = \frac{2\cos \theta_i}{\cos \theta_i + \sqrt{\varepsilon_2/\varepsilon_1 - \sin^2 \theta_i}}
$$

对于 $p$ 波（平行入射面）：

$$
r_p = \frac{E_{0r}}{E_{0i}} = \frac{-\sqrt{\varepsilon_2/\varepsilon_1 - \sin^2 \theta_i} + \cos \theta_i}{-\sqrt{\varepsilon_2/\varepsilon_1 - \sin^2 \theta_i} - \cos \theta_i} \tag{2.9}
$$

$$
t_p = \frac{E_{0t}}{E_{0i}} = \frac{2\cos \theta_i}{\cos \theta_i - \sqrt{\varepsilon_2/\varepsilon_1 - \sin^2 \theta_i}}
$$

反射系数 $R = |r|^2$，透射系数 $T = \frac{n_2 \cos \theta_t}{n_1 \cos \theta_i}|t|^2$，且 $R + T = 1$（能量守恒）。

#### 3. 全反射

当电磁波从光密介质向光疏介质入射（$n_1 > n_2$）时，若入射角大于临界角

$$
\theta_c = \arcsin \frac{n_2}{n_1}
$$

则发生**全反射**。此时在第二种介质中，电磁波沿界面方向传播，但振幅随垂直于界面的方向指数衰减（倏逝波），不携带能量进入第二种介质。

---

### §4.3 有导体存在时电磁波的传播

#### 1. 导体内的自由电荷分布

在导体内部，由于自由电子的运动，静电平衡时 $\mathbf{E} = 0$。但在迅变电磁场中，情况不同：高频下场中自由电子不能完全重新分布以维持静电平衡，因此 $\mathbf{E} \neq 0$。

在良导体中，位移电流远小于传导电流，安培环路定律近似为 $\nabla \times \mathbf{H} \approx \mathbf{J}$。结合欧姆定律 $\mathbf{J} = \sigma \mathbf{E}$ 和麦克斯韦方程，可导出**趋肤效应**和**穿透深度**的概念。

#### 2. 导体内的电磁波

设导体为均匀良导体，电磁波垂直入射到导体表面。进入导体后，电磁场满足亥姆霍兹方程，其解为指数衰减形式：

$$
\mathbf{E}(z) = \mathbf{E}_0 e^{-kz}, \quad k = \sqrt{\omega \mu \sigma / 2}\ (1+i)
$$

定义**穿透深度**（趋肤深度）$\delta$：

$$
\delta = \sqrt{\frac{2}{\omega \mu \sigma}} = \frac{1}{\alpha}
$$

其中 $\alpha$ 为衰减常数。$\delta$ 的物理意义：电磁场在导体表面下 $\delta$ 深度处衰减为表面值的 $1/e$。

#### 3. 趋肤效应和穿透深度

在良导体中，由于趋肤效应，高频电流趋向于在导体表面很薄的一层内流动，等效电阻增大。

**例**：铜在 $f = 10^9$ Hz 时，$\delta \approx 2\mu\text{m}$，可见极高频时电流几乎完全集中在导体表面。

#### 4. 导体表面上的反射

电磁波在导体表面上反射时，反射系数接近 1（理想导体为 1），透入导体的电磁波在很浅的表层内被吸收转化为焦耳热。良导体对电磁波是不透明的。

---

### §4.4 有界空间中的电磁波

#### 1. 理想导体边界条件

理想导体内部 $\mathbf{E} = 0$、$\mathbf{B} = 0$。由边值关系，导体表面的边界条件为：

- $\mathbf{E}$ 的切向分量 $= 0$（$\mathbf{e}_n \times \mathbf{E} = 0$）
- $\mathbf{B}$ 的法向分量 $= 0$（$\mathbf{e}_n \cdot \mathbf{B} = 0$）

即电场线垂直于导体表面，磁感应线平行于导体表面。

#### 2. 谐振腔

由良导体壁围成的空腔构成**谐振腔**，腔内电磁场在特定频率下形成驻波（谐振模式）。谐振频率由腔的几何形状和模式决定。

矩形谐振腔的基本模式 $TE_{101}$ 的谐振频率：

$$
\omega_{101} = c\pi\sqrt{\frac{1}{a^2} + \frac{1}{b^2} + \frac{1}{d^2}}
$$

其中 $a \times b \times d$ 为腔的边长。谐振腔的品质因数 $Q$ 取决于腔壁的导电性。

#### 3. 波导

波导是用于传输高频电磁波的导波系统。矩形波导是最常见的类型。

**矩形波导中的电磁波**：

设波导截面为 $a \times b$，电磁波在波导内形成多种模式。$TE$ 波（横电波，$E_z = 0$）和 $TM$ 波（横磁波，$H_z = 0$）。

**截止频率**：每种模式都有对应的截止频率 $\omega_c$，只有 $\omega > \omega_c$ 的波才能在波导中传播。

对于 $TE_{10}$ 波（最常用模式）：

$$
\omega_c = \frac{\pi}{a}, \quad v_p = \frac{\omega}{\sqrt{\omega^2 - \omega_c^2}}c, \quad v_g = c\sqrt{1 - \frac{\omega_c^2}{\omega^2}}
$$

其中 $v_p$ 为相速度，$v_g$ 为群速度，且 $v_p v_g = c^2$。

---

### §4.5 传输线

#### 1. 高频电磁能量的传输

在高频情况下，传输线上的电流分布不再是均匀的，需用波动理论处理。同轴线、平行导线等都是常用的传输线。

#### 2. 矩形波导中的电磁波

矩形波导中电磁场的解需满足亥姆霍兹方程和理想导体边界条件。通过分离变量法可得到各种 $TE_{mn}$ 和 $TM_{mn}$ 模式的场分布。

**$TE_{10}$ 波的场分量**：

$$
E_y = E_0 \sin\frac{\pi x}{a} e^{i(kz - \omega t)}, \quad H_x = -\frac{E_0}{\eta}\sin\frac{\pi x}{a} e^{i(kz - \omega t)}
$$

$$
H_z = \frac{i\pi}{ka}\frac{E_0}{\eta}\cos\frac{\pi x}{a} e^{i(kz - \omega t)}
$$

管壁电流集中在波导内壁表面层内。

---

### §4.6 光子晶体

光子晶体是一种周期性介电结构，其折射率在光学波长尺度上周期性变化。

#### 1. 一维光子晶体的转移矩阵

用转移矩阵方法分析一维光子晶体的能带结构。

#### 2. 光子带隙

光子晶体的周期性结构导致某些频率范围的电磁波不能在其中传播，形成**光子带隙**（类似于电子在晶体中的能带）。

#### 3. 一维光子晶体的全反射

在带隙频率范围内，电磁波被完全反射，一维光子晶体可作为理想镜子。

---

### §4.7 高斯光束

激光束在自由空间中传播时表现为**高斯光束**，其场分布在横截面上呈高斯函数形式：

$$
E(r, z) = E_0 \frac{w_0}{w(z)} \exp\left(-\frac{r^2}{w(z)^2}\right) \exp\left(-i k z - i \frac{k r^2}{2R(z)} + i \zeta(z)\right)
$$

其中 $w(z)$ 为束宽，$R(z)$ 为波前曲率半径，$\zeta(z)$ 为相位因子。

---

### §4.8 光学空间孤子

光学空间孤子是非线性介质中自聚焦效应与衍射效应平衡形成的无衍射光束。

#### 1. 孤子和光学空间孤子

孤子是孤立的波包，在传播过程中保持形状不变。

#### 2. 非线性波动方程

在非线性克尔介质中，光场满足非线性薛定谔方程：

$$
i\frac{\partial A}{\partial z} + \frac{1}{2k_0}\nabla_\perp^2 A + n_2 |A|^2 A = 0
$$

#### 3. 自治孤子解

该方程的解具有钟形或孤子形状，在传播过程中保持形状不变。

---

### §4.9 等离子体的电磁现象

#### 1. 等离子体的准电中性和屏蔽库仑场

等离子体是电离气体，其中自由电子和离子共存。在宏观尺度上呈电中性（准电中性），但库仑场被屏蔽，屏蔽长度（德拜长度）$\lambda_D = \sqrt{\frac{\varepsilon_0 k_B T_e}{n_e e^2}}$。

#### 2. 等离子体振荡

等离子体有固有的振荡频率（等离子体频率）：

$$
\omega_p = \sqrt{\frac{n_e e^2}{\varepsilon_0 m_e}}
$$

当电磁波频率 $\omega > \omega_p$ 时可在等离子体中传播，$\omega < \omega_p$ 时被全反射。

#### 3. 电磁波在等离子体中的传播

电磁波在等离子体中的折射率：

$$
n = \sqrt{1 - \frac{\omega_p^2}{\omega^2}}
$$

当 $\omega < \omega_p$ 时，$n$ 为虚数，电磁波被截止（被全反射）。

---

> 本章小结：电磁波是电磁场互相激发的波动形式，在真空中以光速 $c$ 传播；平面电磁波是横波，$\mathbf{E}$、$\mathbf{H}$ 与传播方向两两正交；介质中电磁波传播速度为 $v = c/n$；界面上的反射和折射满足斯涅尔定律和菲涅耳公式；导体中电磁波有趋肤效应和穿透深度 $\delta$；波导中只有截止频率以上的波才能传播。

---

## 第五章 电磁波的辐射

本章讨论电磁波的辐射问题，介绍一般情况下势的概念和辐射电磁场的计算方法。内容包括电磁势、辐射场计算（电偶极、磁偶极、电四极辐射）、天线辐射以及衍射和电磁场动量。

---

### §5.1 电磁势的协变性

#### 1. 电磁势

麦克斯韦方程组可以写成对称形式：

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}, \quad \nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}
$$

由于 $\nabla \cdot \mathbf{B} = 0$，可令 $\mathbf{B} = \nabla \times \mathbf{A}$；由于 $\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$，有 $\nabla \times (\mathbf{E} + \frac{\partial \mathbf{A}}{\partial t}) = 0$，故可引入标势 $\varphi$：

$$
\mathbf{E} = -\nabla \varphi - \frac{\partial \mathbf{A}}{\partial t}, \quad \mathbf{B} = \nabla \times \mathbf{A}
$$

#### 2. 规范变换

电磁势不是唯一的。在**规范变换**下：

$$
\mathbf{A}' = \mathbf{A} + \nabla \chi, \quad \varphi' = \varphi - \frac{\partial \chi}{\partial t}
$$

电磁场 $\mathbf{E}$ 和 $\mathbf{B}$ 不变。

为简化势的方程，可选择特定的规范条件。**洛伦兹规范**：

$$
\nabla \cdot \mathbf{A} + \frac{1}{c^2}\frac{\partial \varphi}{\partial t} = 0
$$

在此规范下，势的方程化为**达朗贝尔方程**（波动方程）：

$$
\nabla^2 \varphi - \frac{1}{c^2}\frac{\partial^2 \varphi}{\partial t^2} = -\frac{\rho}{\varepsilon_0}, \quad \nabla^2 \mathbf{A} - \frac{1}{c^2}\frac{\partial^2 \mathbf{A}}{\partial t^2} = -\mu_0 \mathbf{J}
$$

#### 3. 势的解——推迟势

达朗贝尔方程的特解（推迟势）为：

$$
\varphi(\mathbf{r}, t) = \frac{1}{4\pi\varepsilon_0}\int_V \frac{\rho(\mathbf{r}', t_r)}{|\mathbf{r} - \mathbf{r}'|} dV', \quad \mathbf{A}(\mathbf{r}, t) = \frac{\mu_0}{4\pi}\int_V \frac{\mathbf{J}(\mathbf{r}', t_r)}{|\mathbf{r} - \mathbf{r}'|} dV'
$$

其中 $t_r = t - \frac{|\mathbf{r} - \mathbf{r}'|}{c}$ 为**推迟时间**，表示电磁作用以有限速度 $c$ 传播。

---

### §5.2 辐射场计算的一般公式

#### 1. 计算辐射场的一般公式

已知电流分布 $\mathbf{J}(\mathbf{r}', t)$，辐射场可由推迟势公式计算。设 $t$ 时刻在场点 $\mathbf{r}$ 的场，源点为 $\mathbf{r}'$，延迟时间为 $t_r = t - R/c$（$R = |\mathbf{r} - \mathbf{r}'|$）。

在远离源区（$r \gg r'$）的条件下，对推迟势展开，可得到不同多极辐射的近似。

#### 2. 矢势的展开式

当 $r \gg r'$ 时，对 $1/R$ 作多极展开，矢势 $\mathbf{A}$ 可展开为：

$$
\mathbf{A}(\mathbf{r}, t) = \frac{\mu_0}{4\pi}\left[ \frac{\mathbf{p}(t_r)}{r^2} + \frac{\dot{\mathbf{p}}(t_r)}{c r} + \cdots \right] \quad (\text{电偶极项})
$$

其中 $\mathbf{p}(t) = \int_V \rho(\mathbf{r}', t)\mathbf{r}' dV'$ 为电偶极矩。

---

### §5.3 电偶极辐射

#### 1. 辐射场

电偶极辐射场（远场）为：

$$
\mathbf{E}(\mathbf{r}, t) = \frac{\mu_0}{4\pi r}\ddot{\mathbf{p}}(t_r) \times \mathbf{e}_r \times \mathbf{e}_r, \quad \mathbf{B}(\mathbf{r}, t) = \frac{\mu_0}{4\pi c r}\ddot{\mathbf{p}}(t_r) \times \mathbf{e}_r
$$

或等价地 $\mathbf{E} = \mathbf{B} \times \mathbf{e}_r \cdot c$。

#### 2. 辐射能流

**坡印廷矢量**在远场近似下为

$$
\mathbf{S} = \frac{\mu_0}{16\pi^2 c r^2} |\ddot{\mathbf{p}}(t_r)|^2 \mathbf{e}_r \sin^2\theta
$$

其中 $\theta$ 为 $\mathbf{e}_r$ 与偶极矩 $\mathbf{p}$ 方向的夹角。

#### 3. 角分布

辐射强度按 $\sin^2\theta$ 分布，在偶极矩方向无辐射，在垂直方向辐射最强。

#### 4. 辐射功率

对球面积分得总辐射功率：

$$
P = \frac{\mu_0}{6\pi c} |\ddot{\mathbf{p}}|^2
$$

#### 5. 短天线的辐射

长度为 $l \ll \lambda$ 的短直线天线（终端电流为 $I_0$），其辐射功率：

$$
P = \frac{\mu_0}{12\pi c}\left(\frac{I_0 l \omega}{2\pi}\right)^2
$$

---

### §5.4 磁偶极辐射和电四极辐射

#### 1. 高频电流分布的磁偶极矩和电四极矩

对于以频率 $\omega$ 振荡的电流分布，可定义：

- **磁偶极矩**：$\mathbf{m} = \frac{1}{2}\int_V \mathbf{r}' \times \mathbf{J}(\mathbf{r}') dV'$
- **电四极矩张量**：$Q_{ij} = \int_V \rho(\mathbf{r}')(3x_i' x_j' - r'^2 \delta_{ij}) dV'$

#### 2. 磁偶极辐射

磁偶极辐射场为：

$$
\mathbf{E} = -\frac{\mu_0}{4\pi c^2 r}\ddot{\mathbf{m}}(t_r) \times \mathbf{e}_r, \quad \mathbf{B} = \frac{\mu_0}{4\pi c^2 r}\ddot{\mathbf{m}}(t_r) \times \mathbf{e}_r \times \mathbf{e}_r
$$

辐射功率：$P = \frac{\mu_0}{12\pi c^3} |\ddot{\mathbf{m}}|^2$。

#### 3. 电四极辐射

电四极辐射的辐射场正比于 $\dddot{Q}_{ij}$，辐射功率正比于 $|\dddot{Q}_{ij}|^2$，比电偶极辐射弱一个因子 $(k r')^2$ 数量级。

---

### §5.5 天线辐射

#### 1. 天线上的电流分布

天线上的电流分布由天线形状和边界条件决定。对于细天线，电流近似满足波动方程。

#### 2. 半波天线

半波天线（总长度 $l = \lambda/2$）的辐射场可直接计算，其辐射电阻 $R_{\text{辐射}} \approx 73\ \Omega$。

#### 3. 天线阵

由多个天线单元按一定相位关系排列构成天线阵，可实现方向性辐射（波束成形）。

---

### §5.6 电磁波的衍射

#### 1. 衍射问题

当电磁波遇到障碍物（孔径或屏）时，产生衍射现象。衍射问题的严格求解是边值问题。

#### 2. 基尔霍夫公式

在近似条件下（基尔霍夫近似），衍射场可表为障碍物孔径上场的积分：

$$
\mathbf{E}(\mathbf{r}) = \oint_S \left[ \mathbf{E} \frac{\partial}{\partial n}\left(\frac{e^{ikR}}{R}\right) - \frac{e^{ikR}}{R}\frac{\partial \mathbf{E}}{\partial n} \right] dS
$$

其中 $k = \omega/c$。

#### 3. 巴比涅原理

在互补屏（一个屏的障碍物部分恰好是另一屏的孔径）情形下，衍射场满足巴比涅原理。

---

### §5.7 电磁场的动量

#### 1. 电磁场的动量密度和动量流密度

电磁场具有动量，其**动量密度**为

$$
\mathbf{g} = \frac{\mathbf{S}}{c^2} = \frac{\mathbf{E} \times \mathbf{H}}{c^2}
$$

动量流密度（**麦克斯韦应力张量**）描述动量的传输。

#### 2. 辐射压力

电磁波照射到物体上产生压力，称为**辐射压力**。对于完全吸收体，压力 $p = \frac{I}{c}$（$I$ 为入射能流）；对于完全反射体，压力 $p = \frac{2I}{c}$。

---

## 第六章 狭义相对论

本章从电动力学的参考系问题引出狭义相对论时空观，由物理规律对惯性参考系协变的要求把电动力学基本方程表为四维形式，并导出电磁场量在不同参考系间的变换。

---

### §6.1 相对论的实验基础

相对论是解决电磁现象与经典力学时空观矛盾而产生的。迈克耳孙-莫雷实验否定了以太的存在，各种高能粒子实验支持相对论时空观。

---

### §6.2 相对论的基本原理和洛伦兹变换

#### 1. 相对论的基本原理

- **相对性原理**：所有惯性系中物理规律的形式都相同
- **光速不变原理**：真空中光速在任何惯性系中都等于 $c$

#### 2. 间隔不变性

时空间隔 $ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2$ 在洛伦兹变换下是不变量。

#### 3. 洛伦兹变换

两个惯性系 $S$ 和 $S'$（$S'$ 相对 $S$ 以速度 $v$ 沿 $x$ 轴运动），洛伦兹变换为：

$$
x' = \gamma(x - vt), \quad y' = y, \quad z' = z, \quad t' = \gamma\left(t - \frac{v}{c^2}x\right)
$$

其中 $\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}$。

---

### §6.3 相对论的时空理论

#### 1. 相对论时空结构

时间和空间不再是独立的，时空是一个四维流形。

#### 2. 因果律和相互作用的最大传播速度

由于 $c$ 是最大信号传播速度，因果关系在相对论中受到限制。

#### 3. 同时的相对性

在一个惯性系中同时发生的事件，在另一惯性系中一般不同时。

#### 4. 运动时钟的延缓

运动时钟变慢：$\Delta t = \gamma \Delta \tau$（$\Delta \tau$ 为固有时）。

#### 5. 运动尺度的缩短

运动方向长度收缩：$L = L_0/\gamma$。

#### 6. 速度变换公式

$$
\mathbf{u}' = \frac{\mathbf{u} - \mathbf{v}}{1 - \frac{\mathbf{u} \cdot \mathbf{v}}{c^2}}
$$

---

### §6.4 相对论理论的四维形式

#### 1. 三维空间的正交变换

三维空间正交变换（转动）保持 $x^2 + y^2 + z^2$ 不变。

#### 2. 物理量按空间变换性质的分类

标量、矢量、张量等按其在空间转动下的变换性质分类。

#### 3. 洛伦兹变换的四维形式

四维形式将物理量组织为四维矢量、四维张量等形式。

#### 4. 四维协变量

**四维速度** $U_\mu = \frac{dx_\mu}{d\tau}$，**四维波矢** $k_\mu = \left(\frac{\omega}{c}, \mathbf{k}\right)$ 等。

#### 5. 物理规律的协变性

物理规律写成四维协变形式，在洛伦兹变换下形式不变。

---

### §6.5 电动力学的相对论不变性

#### 1. 四维电流密度矢量

$$
J_\mu = (\rho c, \mathbf{J}), \quad \nabla_\mu J_\mu = 0 \quad (\text{四维连续性方程})
$$

#### 2. 四维势矢量

$$
A_\mu = \left(\frac{\varphi}{c}, \mathbf{A}\right), \quad \nabla_\mu A_\mu = 0 \quad (\text{洛伦兹规范})
$$

#### 3. 电磁场张量

电磁场构成反对称四维张量：

$$
F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu
$$

其分量：

$$
F_{ij} = -\varepsilon_{ijk}B_k, \quad F_{0i} = E_i/c
$$

#### 4. 电磁场的不变量

$$
F_{\mu\nu}F_{\mu\nu} = 2(B^2 - \frac{E^2}{c^2}), \quad \frac{1}{2}\varepsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma} = \frac{\mathbf{E} \cdot \mathbf{B}}{c}
$$

---

### §6.6 相对论力学

#### 1. 能量-动量四维矢量

$$
P_\mu = \left(\frac{E}{c}, \mathbf{p}\right), \quad P_\mu P_\mu = -m^2 c^2
$$

#### 2. 质能关系

$$
E = mc^2 = \frac{m_0 c^2}{\sqrt{1 - v^2/c^2}}
$$

#### 3. 相对论力学方程

$$
\frac{dP_\mu}{d\tau} = F_\mu
$$

其中 $F_\mu$ 为四维力。

---

### §6.7 电磁场中带电粒子的拉格朗日量和哈密顿量

#### 1. 拉格朗日形式

相对论性带电粒子的拉格朗日量：

$$
L = -mc^2\sqrt{1 - v^2/c^2} + \frac{q}{c}\mathbf{A} \cdot \mathbf{v} - q\varphi
$$

#### 2. 哈密顿形式

哈密顿量：

$$
H = \sqrt{(\mathbf{p} - q\mathbf{A})^2 c^2 + m^2 c^4} + q\varphi
$$

#### 3. 非相对论情形

过渡到非相对论情形：$H \approx mc^2 + \frac{(\mathbf{p} - q\mathbf{A})^2}{2m} + q\varphi$。

---

## 第七章 带电粒子和电磁场的相互作用

本章讨论带电粒子和电磁场的相互作用，包括运动带电粒子的辐射、高速运动粒子的辐射、辐射的频谱分析、切连科夫辐射、带电粒子的自反作用以及电磁波的散射吸收和介质色散。

---

### §7.1 运动带电粒子的势和辐射电磁场

#### 1. 任意运动带电粒子的势

任意运动带电粒子的四维势为

$$
A_\mu(\mathbf{r}, t) = \frac{\mu_0 c}{2\pi} \int \delta\left(t' - t + \frac{R}{c}\right) J_\mu(\mathbf{r}', t') d^4x'
$$

或用李纳-维谢尔势表述。

#### 2. 偶极辐射

对于低速运动（$v \ll c$）的带电粒子，电偶极辐射是主要辐射机制，辐射功率 $P = \frac{\mu_0}{6\pi c} |\ddot{\mathbf{p}}|^2$。

#### 3. 任意运动带电粒子的电磁场

任意运动带电粒子的辐射场在远场近似下为

$$
\mathbf{E}(\mathbf{r}, t) = \frac{\mu_0 q}{4\pi R} \left[ \mathbf{n} \times \left( \mathbf{n} \times \dot{\mathbf{v}} \right) \right]_{t_r}, \quad \mathbf{B} = \frac{1}{c}\mathbf{n} \times \mathbf{E}
$$

其中 $\mathbf{n} = \mathbf{R}/R$。

---

### §7.2 高速运动带电粒子的辐射

#### 1. 高速运动带电粒子的辐射功率和角分布

相对论性高速带电粒子的辐射有强烈的方向性，集中于速度方向的一个小角锥内（**搜寻辐射**）。

辐射功率（拉莫尔公式的相对论推广）：

$$
P = \frac{\mu_0 q^2 \gamma^6}{6\pi c} |\dot{\mathbf{v}}|^2 - \frac{\mu_0 q^2}{6\pi c} |\dot{\mathbf{v}}|^2
$$

#### 2. $\gamma \gg 1$ 情形

当 $\gamma \gg 1$（ultra-relativistic）时，辐射功率

$$
P \approx \frac{\mu_0 q^2 c}{6\pi R_g^2}\gamma^4, \quad R_g = \frac{mc^2}{eE_{\perp}}
$$

其中 $R_g$ 为特征曲率半径。

#### 3. $\gamma \gg 1$ 的辐射

同步辐射（圆周运动的相对论辐射）是典型例子。

---

### §7.3 辐射的频谱分析

#### 1. 频谱分析的一般公式

辐射场可作傅里叶展开，频谱分布由粒子的运动轨迹决定。

#### 2. 低速运动带电粒子在碰撞过程中的辐射频谱

碰撞辐射的频谱是连续的，功率谱密度正比于 $|\mathbf{a}(\omega)|^2$。

#### 3. 高速圆周运动带电粒子的辐射频谱

同步辐射的频谱：低频部分 $I(\omega) \propto \omega^{1/3}$，在 $\omega \approx \omega_c = \frac{3}{2}\gamma^3 \frac{v}{R}$ 处达到峰值。

---

### §7.4 切连科夫辐射

当带电粒子在介质中的速度超过该介质中的光速（$v > c/n$）时，产生**切连科夫辐射**。

辐射角满足

$$
\cos \theta = \frac{c/n}{v} = \frac{1}{\beta n}
$$

这一辐射被用于粒子探测（切连科夫计数器）。

---

### §7.5 带电粒子的电磁场对粒子本身的反作用

#### 1. 电磁质量

带电粒子的自有场能量导致额外的"电磁质量"。

#### 2. 辐射阻尼

带电粒子加速运动时，其自有场对粒子施加反作用力（辐射阻尼），导致运动方程修正：

$$
m_0 \dot{\mathbf{v}} = \mathbf{F}_{\text{外}} + \frac{\mu_0 q^2}{6\pi c}\dot{\mathbf{a}}
$$

#### 3. 谱线的自然宽度

辐射阻尼导致谱线有有限宽度 $\Delta \omega \approx \frac{r_e \omega_0^2}{c}$（$r_e = \frac{\mu_0 e^2}{4\pi m_0}$ 为电子经典半径）。

---

### §7.6 电磁波的散射、吸收和介质的色散

#### 1. 散射和吸收

电磁波与介质相互作用产生散射和吸收。汤姆孙散射（自由电子）散射截面 $\sigma_T = \frac{8\pi}{3}r_e^2$。瑞利散射（束缚电子）散射截面与 $\omega^4$ 成正比。

#### 2. 介质色散

介质的极化率 $\chi(\omega)$ 是频率的函数，导致：

- **正常色散**：$\frac{dn}{d\lambda} < 0$（如可见光区域）
- **反常色散**：在共振频率附近，吸收导致色散性质的特殊变化

#### 3. 克拉默斯-克勒尼希色散关系

实部和虚部之间满足因果律所要求的积分关系。

#### 4. 介质的色散

介电常量 $\varepsilon(\omega) = \varepsilon_0\left(1 + \sum_j \frac{\omega_{pj}^2}{\omega_j^2 - \omega^2 - i\gamma_j \omega}\right)$。

#### 5. 原子光陷阱

利用激光冷却技术可将原子囚禁在光场中，实现极低温的原子气体。

#### 6. 经典电动力学的局限性

经典电动力学在微观尺度上必须用量子电动力学（QED）取代。经典理论的困难包括：原子稳定性、辐射阻尼的自能问题、黑体辐射的紫外灾难等。

---

> 本笔记涵盖了郭硕鸿《电动力学》教材的主要内容。各章摘要如下：
>
> - **第一章**：电磁现象的普遍规律——麦克斯韦方程组的建立
> - **第二章**：静电场——标势、泊松方程、唯一性定理、分离变量法、电多极矩
> - **第三章**：静磁场——矢势、磁标势、磁多极矩、阿哈罗诺夫-玻姆效应、超导体
> - **第四章**：电磁波的传播——波动方程、平面波、反射折射、导体中传播、波导、光子晶体
> - **第五章**：电磁波的辐射——电磁势、推迟势、电偶极/磁偶极/电四极辐射、天线、衍射
> - **第六章**：狭义相对论——洛伦兹变换、时空理论、四维形式、相对论力学
> - **第七章**：带电粒子和电磁场的相互作用——辐射、反作用、色散、QED局限性
