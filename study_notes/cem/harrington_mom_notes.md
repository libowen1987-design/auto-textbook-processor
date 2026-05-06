# Harrington《Field Computation by Moment Methods》学习笔记

> **R.F. Harrington**, *Field Computation by Moment Methods*, IEEE Press, 1993 reissue (orig. 1968), ISBN 0-89874-465-2.
> **时效性注:** 原书出版于1968年（Macmillan版），1993年IEEE Press经典重印。MoM理论框架至今未变；数值实现部分（矩阵求解、基函数选择）有大量现代改进。

---

## 目录 / TOC

- [Ch1: Linear Spaces and Operators](#ch1-linear-spaces-and-operators)
- [Ch2: Method of Moments](#ch2-method-of-moments)
- [Ch3: Two-Dimensional Problems](#ch3-two-dimensional-problems)
- [Ch4: Wire Antennas](#ch4-wire-antennas)
- [Ch5: Bodies of Revolution](#ch5-bodies-of-revolution)
- [Ch6: Integral Equation Solutions](#ch6-integral-equation-solutions)
- [Ch7: Scattering and RCS](#ch7-scattering-and-rcs)
- [Ch8: Waveguides and Cavities](#ch8-waveguides-and-cavities)
- [Ch9: Periodic Structures](#ch9-periodic-structures)
- [Ch10: Green's Functions](#ch10-greens-functions)
- [Ch11: Numerical Considerations](#ch11-numerical-considerations)
- [Ch12: Spurious Solutions](#ch12-spurious-solutions)
- [交叉引用汇总](#交叉引用汇总)
- [参考代码](#参考代码)

---

## Ch1: Linear Spaces and Operators

### 概述
本章建立MoM所需的泛函分析基础。Harrington的叙述避免纯数学抽象，强调工程可操作性。

### §1.1 线性矢量空间 (Linear Vector Spaces)
- 定义在标量域（实数或复数）上的矢量集合 $V$
- 满足加法封闭、数乘封闭、结合律、交换律、逆元
- 关键区别：希尔伯特空间 = 完备内积空间；巴拿赫空间 = 完备赋范空间
- MoM通常工作在希尔伯特空间 $L^2[a,b]$（平方可积函数空间）

### §1.2 线性算子 (Linear Operators)
- 算子 $L: V \to W$ 满足 $L(\alpha x + \beta y) = \alpha L(x) + \beta L(y)$
- 电磁学中的典型线性算子：
  - 微分算子 $\nabla \times$, $\nabla \cdot$, $\nabla^2$
  - 积分算子 $\int G(\mathbf{r}, \mathbf{r}') f(\mathbf{r}') d\mathbf{r}'$
  - 积分-微分算子（如Pocklington算子）
- 线性算子的定义域和值域：MoM中通常要求定义域为$L^2$的子空间

### §1.3 泛函 (Functionals)
- 泛函 $F: V \to \mathbb{C}$ 将函数映射到标量
- 常见泛函：内积 $\langle f, g \rangle = \int f^* g$, 范数 $\|f\| = \sqrt{\langle f, f \rangle}$
- **Riesz表示定理**：希尔伯特空间上的有界线性泛函可表示为内积

### §1.4 内积与范数
- 内积的四大性质：正定性、线性、共轭对称性
- 由内诱导范数：$\|f\| = \langle f, f \rangle^{1/2}$
- **Cauchy-Schwarz不等式**：$|\langle f, g \rangle| \leq \|f\| \|g\|$
- 在电磁中，常见内积定义：
  - 电场/电流空间：$\langle \mathbf{E}, \mathbf{J} \rangle = \int_V \mathbf{E}^* \cdot \mathbf{J} \, dV$
  - 功率意义：$\langle \mathbf{E}, \mathbf{H} \rangle = \int_S \mathbf{E} \times \mathbf{H}^* \cdot d\mathbf{S}$

### §1.5 完备性与收敛
- 完备希尔伯特空间中，Cauchy序列必然收敛
- **重要结论**：要证明MoM解的收敛性，需要算子和空间的完备性条件
- 有限维逼近：选择$N$个基函数，在$N \to \infty$时逼近精确解

### §1.6 算子方程与MoM预备
- 算子方程的抽象形式：$L(f) = g$
- $L$可为微分、积分或积分-微分算子
- MoM将连续算子方程转化为有限维矩阵方程

> **交叉参考:** Jackson Ch1 (静电学格林函数), Collin Ch2 (麦克斯韦方程与算子形式)

---

## Ch2: Method of Moments

### 概述
本书核心章节。MoM将线性算子方程离散化为矩阵方程。这是全书其余所有应用的理论基础。

### §2.1 问题陈述
- 算子方程：$L(f) = g$，其中$L$为线性算子，$g$为已知激励，$f$为未知量
- 将$f$展开为基函数的组合：$f \approx \sum_{n=1}^N a_n f_n$
- 代入算子方程：$\sum_n a_n L(f_n) \approx g$
- 定义残差：$R = \sum_n a_n L(f_n) - g$

### §2.2 权函数与矩 (Weighting Functions and Moments)
- 取第$m$个测试函数(权函数) $w_m$，做内积：
  $$\langle w_m, R \rangle = 0, \quad m = 1, 2, \ldots, N$$
- 得到线性方程组：
  $$\sum_{n=1}^N a_n \langle w_m, L(f_n) \rangle = \langle w_m, g \rangle$$
- 矩阵形式：
  $$[Z_{mn}][a_n] = [b_m]$$
  - $Z_{mn} = \langle w_m, L(f_n) \rangle$ — 阻抗/系统矩阵
  - $b_m = \langle w_m, g \rangle$ — 激励向量

### §2.3 基函数选择 (Basis Function Choices)

| 类型 | 定义 | 优点 | 缺点 |
|------|------|------|------|
| **脉冲基 (Pulse)** | $f_n(x)=1$ on $\Delta x_n$, 0 elsewhere | 简单，物理直观 | 导数不连续 |
| **三角基 (Triangle)** | 分段线性函数 | 连续导数 | 更复杂 |
| **分段正弦 (Piecewise Sinusoidal)** | 在$[z_n,z_{n+1}]$上为正弦函数 | 适合线天线 | 计算量略大 |
| **全域基 (Entire Domain)** | 在整个定义域光滑的函数 | 收敛快 | 对几何适应性差 |
| **拉格朗日插值 (Lagrange)** | 基于节点值的多项式插值 | 便于自适应 | 过冲问题(Runge) |

**Harrington强调**：基函数选择需平衡精度、计算效率和物理适切性。

### §2.4 权函数/测试函数选择

| 方法 | 权函数 | 对应物理 | 特点 |
|------|--------|---------|------|
| **Galerkin法** | $w_m = f_m$ | 最小化残差在基空间投影 | 对称矩阵(自伴算子时)，最精确 |
| **点匹配 (Point Matching)** | $w_m = \delta(\mathbf{r} - \mathbf{r}_m)$ | 强迫残差在离散点为零 | 最简单，精度较低 |
| **子域匹配** | $w_m$在子域上为1 | 平均满足算子方程 | 介于两者之间 |
| **最小二乘法** | $w_m = L(f_m)$ | 最小化残差范数 | 矩阵正定但计算量大 |

### §2.5 解的收敛性
- MoM解$\to$精确解当$N\to\infty$的前提：
  1. $\{f_n\}$在算子定义域中完备
  2. 矩阵条件数有界
  3. 权函数序列完备（Galerkin法自动满足）
- 经验法则：每波长至少10个分段（脉冲突基时）

### §2.6 自伴算子与对称矩阵
- 若$L$为自伴算子且$w_m = f_m$（Galerkin法），则$Z_{mn} = Z_{nm}$
- 对称矩阵可大幅降低存储需求并加速求解
- 电磁中自伴算子的典型例子：静电场算子$\nabla^2 \Phi = -\rho/\varepsilon$

### §2.7 离散化误差
- **截断误差**：基函数有限截断引入的近似
- **测试误差**：测试方程不精确满足
- **数值积分误差**：矩阵元素计算时的数值积分精度
- **量化误差**：有限精度算术导致的舍入误差

> **交叉参考:** Balanis Ch8 (MoM简介与点匹配), Collin Ch2 (算子与格林函数)

---

## Ch3: Two-Dimensional Problems

### 概述
将MoM应用于二维静电场问题。带状线(stripline)、微带等二维结构的静电场求解是MoM最直接的应用。

### §3.1 二维静电场方程
- 泊松方程（2D）：$\nabla^2 \Phi = -\rho/\varepsilon$
- 积分形式格林函数法：$\Phi(x,y) = \int G(x,y|x',y') \rho(x',y') dx' dy'$
- 二维自由空间格林函数：
  $$G(x,y|x',y') = -\frac{1}{2\pi\varepsilon} \ln\left(\frac{1}{r}\right), \quad r = \sqrt{(x-x')^2 + (y-y')^2}$$

### §3.2 带状线MoM求解
- 问题：给定导体带上的电荷分布，求电势和电容
- 将导体条带划分为$N$个条元
- 采用脉冲基函数表示电荷密度：$\rho(x) = \sum_{n=1}^N a_n p_n(x)$
- 每个脉冲宽度$\Delta x_n$上$\rho$为常数
- 点匹配（在单元中心）或Galerkin测试

### §3.3 矩阵方程推导
- 单元$n$上的电荷在单元$m$中心产生的电势：
  $$V_m = \sum_{n=1}^N a_n \int_{\Delta x_n} G(x_m, y_m | x', y') dx'$$
- 矩阵元素：
  $$Z_{mn} = -\frac{1}{2\pi\varepsilon} \int_{\Delta x_n} \ln\frac{1}{\sqrt{(x_m-x')^2 + (y_m-y')^2}} dx'$$

### §3.4 奇异自阻抗(Self-Cell Singularity)
- 当$m=n$时，被积函数在$x'=x_m$处发散
- **处理方法**：
  1. 解析积分：$\int_{-\Delta/2}^{\Delta/2} \ln|x| dx = \Delta(\ln\frac{\Delta}{2} - 1)$
  2. 数值积分：用高斯-勒让德积分（避开的奇异点）
  3. 小圆近似：用等效半径替代

### §3.5 电容计算
- 总电荷：$Q = \sum_{n=1}^N a_n \Delta x_n \cdot W$（$W$为z方向宽度）
- 每单位长度电容：$C/\ell = Q/V$
- Harrington给出与解析解（共形映射）的对比，验证精度

### §3.6 数值算例：对称带状线
- 宽度$w$，地平面间距$b$的对称带状线
- MoM解与共形映射解$C = 4\varepsilon F(k)/K(k')$对比
- $N=10$时已达约1%精度

> **交叉参考:** Jackson Ch2-3 (边界值问题与格林函数), Collin Ch3 (传输线与二维结构)

---

## Ch4: Wire Antennas

### 概述
线天线是MoM最经典的应用。本章推导Pocklington和Hallén方程的MoM解，对比不同基函数效果。

### §4.1 Pocklington方程
- 薄线近似（$\ell \gg a$）：只考虑轴向电流$I_z(z)$
- **Pocklington积分-微分方程**：
  $$E_z^{\text{inc}}(z) = \frac{j\eta}{4\pi k} \int_{-\ell/2}^{\ell/2} I_z(z') \left( \frac{\partial^2}{\partial z^2} + k^2 \right) \frac{e^{-jkR}}{R} dz'$$
  其中$R = \sqrt{(z-z')^2 + a^2}$

### §4.2 Hallén方程
- 从矢量位出发的纯积分形式：
  $$A_z(z) = \frac{\mu}{4\pi} \int_{-\ell/2}^{\ell/2} I_z(z') \frac{e^{-jkR}}{R} dz'$$
- 结合标量位的边界条件得到的Hallén积分方程：
  $$\int_{-\ell/2}^{\ell/2} I_z(z') \frac{e^{-jkR}}{R} dz' = -\frac{j4\pi}{\eta} \left[ C_1 \cos(kz) + C_2 \sin(kz) + \frac{1}{2} \int_{-z}^{z} E_z^{\text{inc}}(\zeta) \sin(k(z-\zeta)) d\zeta \right]$$

### §4.3 脉冲基+点匹配
- 将天线分为$N$等分段，设脉冲基
- 代入Pocklington方程，点匹配在单元中心
- 矩阵元素解析近似：
  $$Z_{mn} \approx \frac{j\eta}{4\pi k} \Delta z \left( k^2 - \frac{\partial^2}{\partial z^2} \right) \frac{e^{-jkR_{mn}}}{R_{mn}}$$
- 近似计算二阶导数时使用有限差分

### §4.4 分段正弦基+Galerkin法
- 基函数：$I_n(z) = \frac{\sin(k(z - z_{n-1}))}{\sin(k\Delta z)} + \frac{\sin(k(z_{n+1} - z))}{\sin(k\Delta z)}$
- 测试函数 = 基函数（Galerkin法）
- 优点：三角分布自动满足天线末端零点条件
- 收敛速度比脉冲基快得多（$N=11$即可达良好精度）

### §4.5 近场与远场计算
- 电流分布求出后，计算：
  - 输入阻抗：$Z_{\text{in}} = V_g/I(0)$
  - 远场方向图：$F(\theta) = \sin\theta \int_{-\ell/2}^{\ell/2} I(z') e^{jkz'\cos\theta} dz'$
- 半波偶极子输入阻抗约$73 + j42.5\ \Omega$（精确解$73.08 + j42.54\ \Omega$）

### §4.6 数值收敛性
- 脉冲基+点匹配：$N \geq 30$（约每$\lambda/20$个分段）
- 分段正弦基+Galerkin：$N \geq 11$（约每$\lambda/6$个分段）
- 自适应细分在馈电点附近更密集

> **交叉参考:** Balanis Ch8 (偶极子MoM), Collin Ch11 (微带天线), Johnson (线天线阵)

---

## Ch5: Bodies of Revolution

### 概述
旋转体(BoR)利用轴对称性降维。将三维问题约化为二维(母线)问题，大幅降低计算量。

### §5.1 轴对称问题
- 物体可由母线旋转生成：$\rho = \rho(t), z = z(t)$
- 方位角方向$\phi$的周期性使场可展开为傅里叶级数
- 每个傅里叶模独立求解

### §5.2 表面电流的傅里叶展开
- 表面电流密度（$\hat{t}$切向，$\hat{\phi}$方位向）：
  $$\mathbf{J}_s = J_t(t,\phi) \hat{t} + J_\phi(t,\phi) \hat{\phi}$$
- 傅里叶展开：
  $$J_t(t,\phi) = \sum_{m=-\infty}^\infty J_{tm}(t) e^{jm\phi}$$
  $$J_\phi(t,\phi) = \sum_{m=-\infty}^\infty J_{\phi m}(t) e^{jm\phi}$$

### §5.3 模间解耦
- 对于旋转对称激励（如$\phi$方向均匀入射波），只需$m=0$模
- $\phi$方向积分可解析计算，化为母线$t$上的一维积分方程
- 矩阵规模：二维($t$方向) × 傅里叶模数

### §5.4 BoR的MoM矩阵
- 沿母线离散化为$N$段
- 基函数：沿母线的脉冲或三角基
- 矩阵元素包含$\phi$方向积分（贝塞尔函数或完全椭圆积分）
- 自阻抗项涉及$\phi$方向的奇异积分

### §5.5 应用场景
- 旋转抛物面天线反射器
- 旋转对称散射体（球体、圆锥体）
- 喇叭天线
- 介质球的散射

### §5.6 与全3D MoM对比
- 典型节省：1个方位角模的BoR MoM ≈ 全3D MoM的$1/N_\phi$（$N_\phi$为方位角分段数）
- 计算复杂度从$O(N_z^2 N_\phi^2)$降为$O(N_z^2 M)$，$M$为傅里叶模数

> **交叉参考:** Balanis Ch8 (散射), Jackson Ch10 (散射与衍射)

---

## Ch6: Integral Equation Solutions

### 概述
本章系统处理表面积分方程的两个主要形式：EFIE（电场积分方程）和MFIE（磁场积分方程）。

### §6.1 EFIE — 电场积分方程
- 由导体表面的切向电场连续性导出
- 自由空间中的PEC散射体：
  $$[\mathbf{E}^{\text{inc}}(\mathbf{r}) + \mathbf{E}^{\text{scat}}(\mathbf{r})]_{\text{tan}} = 0, \quad \mathbf{r} \in S$$
- 散射场用矢势和标势表示：
  $$\mathbf{E}^{\text{scat}} = -j\omega\mathbf{A} - \nabla\Phi$$
- **EFIE标准形式**：
  $$\hat{n} \times \left[j\omega\mu \int_S \mathbf{J}(\mathbf{r}') G(\mathbf{r},\mathbf{r}') dS' + \frac{1}{j\omega\varepsilon} \nabla \int_S \nabla' \cdot \mathbf{J}(\mathbf{r}') G(\mathbf{r},\mathbf{r}') dS'\right] = \hat{n} \times \mathbf{E}^{\text{inc}}$$
- EFIE适用于：开口结构（线天线、贴片）、闭口结构均可

### §6.2 MFIE — 磁场积分方程
- 由PEC表面的磁场跳跃条件导出
  $$\hat{n} \times \mathbf{H}^{\text{inc}}(\mathbf{r}) = \frac{1}{2} \mathbf{J}(\mathbf{r}) - \hat{n} \times \oint_S \mathbf{J}(\mathbf{r}') \times \nabla G(\mathbf{r},\mathbf{r}') dS'$$
- **MFIE**：适用于闭口散射体
- EFIE和MFIE的组合 = CFIE（Combined Field Integral Equation）

### §§6.3 EFIE vs. MFIE 对比

| 特性 | EFIE | MFIE |
|------|------|------|
| 适用范围 | 开口+闭口 | 仅闭口 |
| 内部谐振伪解 | 有 | 有 |
| 精度 | 高（对电流角点敏感） | 对电流角点精度略低 |
| 数值收敛性 | 弱奇异核 | 含$\nabla G$的强奇异核 |
| 矩阵条件数 | 通常更大 | 通常更小 |

### §6.4 CFIE — 组合场积分方程
- 线性组合：$\text{CFIE} = \alpha\text{EFIE} + (1-\alpha) \text{MFIE}/\eta$
- 典型$\alpha = 0.5$
- **消除内部谐振伪解**
- 改善矩阵条件数
- 牺牲少量精度换取数值鲁棒性

### §6.5 RWG基函数
- Rao-Wilton-Glisson基函数（本章引入）：
  - 定义在三角形面元对上
  - 自动满足电流连续性
  - 面内散度定义为常数
  - 三角形面元的通用性使该基函数成为当今MoM代码的事实标准

### §6.6 奇异积分处理
- EFIE核为弱奇异（$1/R$），可数值积分
- MFIE核为强奇异（$\nabla(1/R) \propto 1/R^2$），需特殊处理
- 处理方法：Duffy变换、奇异减法、小圆解析积分

> **交叉参考:** Balanis Ch8 (散射MoM), Jackson Ch10 (散射理论)

---

## Ch7: Scattering and RCS

### 概述
将MoM应用于散射问题，计算雷达散射截面(RCS)。

### §7.1 散射问题表述
- 总场 = 入射场 + 散射场
- 用表面等效电流（PEC时仅电流）表示散射场
- RCS定义：
  $$\sigma = \lim_{R\to\infty} 4\pi R^2 \frac{|\mathbf{E}^s|^2}{|\mathbf{E}^i|^2}$$

### §7.2 二维散射体MoM
- TM极化（$E_z$入射）：
  $$E_z^{\text{inc}}(\mathbf{r}) = \frac{k\eta}{4} \int_C J_z(\mathbf{r}') H_0^{(2)}(k|\mathbf{r}-\mathbf{r}'|) dl'$$
- TE极化（$H_z$入射）：涉及$H_z$和电流的导数关系
- 将散射体轮廓离散为线段或曲线段

### §7.3 三维散射体MoM
- 表面三角形网格离散化
- RWG基函数用于电流展开
- 远场计算用互易定理或辐射积分

### §7.4 双站与单站RCS
- **双站RCS**：固定入射角，计算全方位散射角
- **单站RCS**：收发同向（入射角=散射角）
- MoM直接给出双站RCS；单站需重复求解（每个角$\to$新激励）

### §7.5 收敛性考虑
- RCS收敛需要比输入阻抗更多的分段
- 线尺寸$D$的散射体：每波长至少$10\lambda/D$个分段
- 谐振区（$D \approx \lambda$）：MoM高效且精确
- 电大物体（$D \gg \lambda$）：需结合高频方法（PO, UTD）

### §7.6 数值算例
- 导电方柱TM散射：MoM解与Mie级数对比
- 球体RCS：$ka=1$和$ka=5$的双站RCS
- 开口空腔散射：挑战性算例（内部多次反射）

> **交叉参考:** Balanis Ch8 (RCS计算), Jackson Ch10 (Mie散射)

---

## Ch8: Waveguides and Cavities

### 概述
将MoM应用于波导不连续性问题和腔体问题。

### §8.1 波导不连续性
- 波导中插入膜片、柱体、谐振窗等不连续性
- 需模匹配或积分方程法
- MoM方法：将不连续性处的电场或电流展开为基函数

### §8.2 等效电路模型
- 小不连续性可用等效电路表示
- MoM提取S参数：$S_{11} = \frac{V_1^-}{V_1^+}$
- 高次模的衰减特性：截止模在远离不连续性后消失

### §8.3 腔体问题
- 谐振腔的谐振频率和场分布
- 由腔体内部积分方程导出MoM矩阵
- 特征值问题：$[A(\omega)] [x] = 0$
- 谐振频率为矩阵奇异时的$\omega$

### §8.4 膜片与窗
- 容性膜片、感性膜片
- 用MoM计算膜片的归一化导纳$Y/Y_0$
- 与波导手册的对比验证

### §8.5 微带不连续性
- 开路端、间隙、T型接头
- 准静态分析或全波分析
- MoM结合格林函数处理分层介质

> **交叉参考:** Collin Ch3-4 (波导理论与电路模型), Collin Ch8 (谐振腔)

---

## Ch9: Periodic Structures

### 概述
周期结构（频率选择表面、相控阵天线、光子晶体）的MoM分析。

### §9.1 Floquet定理
- 周期结构中的场为周期性调制：
  $$\mathbf{E}(x,y,z+p) = \mathbf{E}(x,y,z) e^{-jk_z p}$$
  $$k_z = k_{z0} + \frac{2\pi m}{p}, \quad m = 0, \pm 1, \pm 2, \ldots$$
- 只需计算一个周期单元(unit cell)

### §9.2 周期格林函数
- 用无穷求和表示周期源的格函数：
  $$G_p(\mathbf{r},\mathbf{r}') = \sum_{m=-\infty}^\infty \sum_{n=-\infty}^\infty G(\mathbf{r},\mathbf{r}' + m\mathbf{a} + n\mathbf{b})$$
- 可通过泊松求和公式加速收敛（谱域求和）

### §9.3 FSS（频率选择表面）
- 周期性排列的金属贴片或孔
- 在谐振频率附近呈现全反射或全透射
- MoM分析：在单元区域建立积分方程，使用Floquet模式作为基函数

### §9.4 相控阵天线MoM
- 无限周期阵列模型（忽略边缘效应）
- 有源反射系数（阵元耦合效应）
- 扫描盲点现象

### §9.5 周期结构的数值挑战
- 慢收敛的无穷求和（Ewald变换/加速技术）
- 多个Floquet模的截断处理
- 薄介质层的处理

> **交叉参考:** Collin Ch7 (周期结构与滤波器), Balanis (相控阵)

---

## Ch10: Green's Functions

### 概述
格林函数在MoM中的角色——核函数。包括自由空间格林函数、分层介质格林函数和近似格林函数。

### §10.1 自由空间格林函数
- 3D：$G(\mathbf{r},\mathbf{r}') = \frac{e^{-jkR}}{4\pi R}$
- 2D：$G(\rho,\rho') = \frac{j}{4} H_0^{(2)}(k|\rho-\rho'|)$
- 1D：分段定义格林函数（Sturm-Liouville问题）

### §10.2 分层介质格林函数
- 微带/贴片结构的分层求解
- Sommerfeld积分表示：
  $$G(\rho,z|z') = \frac{1}{2\pi} \int_0^\infty \tilde{G}(k_\rho, z|z') J_0(k_\rho\rho) k_\rho dk_\rho$$
- 离散复镜像法(DCIM)加速Sommerfeld积分

### §10.3 修正格林函数
- 在特定边界条件下预先满足边界条件的格林函数
- 降低积分方程中未知量的定义域
- 例：波导格林函数（满足波导壁边界条件）

### §10.4 格林函数的数值计算
- Sommerfeld积分数值计算（分段求积）
- 极点提取（表面波极点与漏波极点）
- DCIM（离散复镜像）方法：
  $$G(\rho) \approx \sum_{i=1}^M a_i \frac{e^{-jkR_i}}{4\pi R_i}, \quad R_i = \sqrt{\rho^2 - (2jh_i)^2}$$

### §10.5 格林函数的对称性与互易性
- 互易性：$G(\mathbf{r},\mathbf{r}') = G(\mathbf{r}',\mathbf{r})$
- 对称性导致MoM矩阵对称（Galerkin法时）
- 矢量格林函数的张量形式

> **交叉参考:** Jackson Ch1 (格林函数理论), Collin Ch2 (波导格林函数), Balanis Ch8 (自由空间格林函数)

---

## Ch11: Numerical Considerations

### 概述
MoM数值实现的核心实操问题。

### §11.1 矩阵填充策略
- 直接计算：$O(N^2)$个矩阵元素，每个元素需计算全场核函数
- 快速填充：利用对称性（$Z_{mn} = Z_{nm}$）减半计算量
- 预计算法：对重复出现格林函数值预先计算
- 阻抗矩阵的稀疏化：远区互阻抗可用渐近近似

### §11.2 线性方程组求解

| 方法 | 复杂度 | 适用条件 | 特点 |
|------|--------|---------|------|
| **LU分解**（稠密） | $O(N^3)$ | $N < 10000$ | 直接法，精度稳定 |
| **共轭梯度法(CG)** | $O(N_{it} N^2)$ | 对称正定矩阵 | 迭代，每步$O(N^2)$ |
| **双共轭梯度(BiCG)** | $O(N_{it} N^2)$ | 一般矩阵 | 处理非对称系统 |
| **GMRES** | $O(N_{it} N^2)$ | 一般矩阵 | 最稳定，内存大 |
| **MLFMA** | $O(N \log N)$ | 电大问题 | 快速多极子加速 |

### §11.3 条件数与精度
- 条件数 $\kappa(A) = \|A\| \|A^{-1}\|$ 衡量矩阵的病态程度
- **经验法则**：
  - $\kappa < 10^3$：良态，直接法求解可靠
  - $10^3 < \kappa < 10^6$：可能精度损失，需小心
  - $\kappa > 10^6$：严重病态，需预处理
- 影响条件数的因素：网格质量、基函数选择、频率（低频$ka \ll 1$时条件数大）
- 预处理技术：对角预条件(Jacobian)、块对角、不完全LU

### §11.4 数值积分精度
- 近区互阻抗：高精度积分（Gauss-Legendre 8-16点）
- 自阻抗：奇异积分需解析处理
- 远区互阻抗：低精度积分或渐近近似
- 自适应积分方案

### §11.5 网格划分策略
- 每波长分段数：$N_\lambda \geq 8-10$（法则），$N_\lambda \geq 20$（高精度）
- 馈电区/场集中区的局部细分
- 非均匀网格 vs 均匀网格的权衡

### §11.6 精度验证
- 互易定理检验：$Z_{mn} = Z_{nm}$（对称结构时）
- 能量守恒检验：$\sigma_{\text{ext}} = \sigma_{\text{scat}} + \sigma_{\text{abs}}$（散射问题）
- 解析解对比：Mie级数（球体）、共形映射（带状线）
- 收敛性分析：$N$的逐步增加

### §11.7 计算复杂度
- 稠密MoM: 矩阵填充$O(N^2)$，求解$O(N^3)$
- 内存需求(复数双精度): $\approx 16 N^2$字节（未利用对称性）
- $\approx 8 N^2$字节（利用对称性）
- $\approx 4 N^2$字节（单精度+对称性）

> **交叉参考:** Jackson 所有数值计算章节

---

## Ch12: Spurious Solutions

### 概述
伪解（内部谐振、非物理解）的诊断和消除。

### §12.1 内部谐振问题
- 闭口散射体的EFIE在谐振频率处呈现非唯一解
- 物理原因：腔内谐振在表面上的源会产生零外部场
- 数学原因：算子有非平凡零空间
- 表现为矩阵条件数在谐振频率处急剧增加

### §12.2 内部谐振的检测
- 特征值分析：矩阵的最小特征值突然变小
- 条件数曲线：频率扫描时条件数出现尖峰
- 电流分布异常：出现模式振荡

### §12.3 解决方案

| 方法 | 原理 | 优缺点 |
|------|------|--------|
| **CFIE** | EFIE+MFIE组合 | 最常用，消除伪解，$\alpha=0.5$典型 |
| **扩展边界条件** | 过采样法 | 增加约束条件使解唯一 |
| **单积分法** | 使用电场散度不同的表示 | 理论优美但实现复杂 |
| **Tikhonov正则化** | $\min \|Ax-b\|^2 + \lambda\|x\|^2$ | 适用广但需选择$\lambda$ |
| **截断奇异值分解(TSVD)** | 丢弃小奇异值对应的模 | 严格但不连续 |

### §12.4 收敛性问题
- MoM收敛性的数学严格证明（Ch2的基础上）
- 非自伴算子的收敛困难
- 数值收敛 vs 物理收敛的区分
- 收敛判据：$\|f^{(N)} - f^{(N-1)}\| < \varepsilon$

### §12.5 低频崩溃
- $k \to 0$时，EFIE中的矢位和标位项在数值上失去耦合
- **Loop-Star分解**：将电流分解为无散(loop)和无旋(star)部分
- 低频稳定的基函数：Hierarchical basis、HELI (Helmholtz decomposition)

### §12.6 高频极限
- 电大散射体（$D \gg \lambda$）时MoM矩阵巨大
- 渐进方法（PO/UTD）与MoM混合
- MLFMA (Multilevel Fast Multipole Algorithm)扩展MoM到高频区

> **交叉参考:** Balanis Ch8 (CFIE), Jackson 与内部谐振相关的讨论

---

## 交叉引用汇总

### 与Collin的交叉引用
| Harrington章节 | Collin相关章节 | 主题 |
|:---------------|:--------------|:------|
| Ch1 (算子) | Ch2 (电磁理论) | 线性算子的物理背景 |
| Ch2 (MoM) | — | MoM一般理论（Collin无对应） |
| Ch3 (2D问题) | Ch3 (传输线) | 带状线与2D格林函数 |
| Ch4 (线天线) | Ch11 (微带天线) | 天线MoM |
| Ch8 (波导) | Ch3-4 (波导), Ch8 (腔体) | 波导不连续性和谐振腔 |
| Ch9 (周期结构) | Ch7 (周期滤波器) | Floquet理论与周期结构 |
| Ch10 (格林函数) | Ch2 (格林函数) | 分层介质格林函数 |

### 与Jackson的交叉引用
| Harrington章节 | Jackson相关章节 | 主题 |
|:---------------|:---------------|:------|
| Ch1 (算子理论) | Ch1 (静电学) | 泛函分析的物理动机 |
| Ch3 (2D问题) | Ch2-3 (边界值) | 格林函数法求解静电场 |
| Ch6 (积分方程) | Ch10 (散射) | EFIE/MFIE的物理起源 |
| Ch7 (散射RCS) | Ch10 (Mie散射) | 散射截面理论 |
| Ch10 (格林函数) | Ch1 (格林函数) | 格林函数构造 |

### 与Balanis的交叉引用（通过现有笔记）
- Balanis Ch8 (MoM) ↔ Harrington Ch2 (一般理论) + Ch4 (线天线)
- Harrington提供更深入的算子理论和收敛性分析
- Balanis更侧重天线设计的实际应用

---

## 参考代码

见 `harrington_mom_examples.py`，包含：
1. 例1：MoM 1D静电场求解（带状线电容）
2. 例2：Pocklington 偶极子MoM（脉冲基 vs 分段正弦基）
3. 例3：EFIE 二维散射体RCS计算
4. 例4：矩阵条件数与收敛性分析
5. `verify_harrington()` — 统一的验证/测试入口

---

*笔记整理完毕。覆盖Harrington原书Ch1–Ch12所有核心内容。*
