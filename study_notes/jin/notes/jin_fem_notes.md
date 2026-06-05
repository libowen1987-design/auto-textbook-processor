# Jian-Ming Jin《The Finite Element Method in Electromagnetics》笔记
> **中英双语版**

> 3rd Ed., Wiley-IEEE Press, 2014, ISBN 978-1-118-57136-3

---

## Ch1: Electromagnetic Problems (电磁问题引言)

### 1.1 Maxwell 方程组

**微分形式（时谐场，$e^{j\omega t}$ 约定）：**

$$
\nabla \times \mathbf{E} = -j\omega\mu\mathbf{H} - \mathbf{M}_i
\quad
\nabla \times \mathbf{H} = j\omega\epsilon\mathbf{E} + \mathbf{J}_i
$$

$$
\nabla \cdot \mathbf{D} = \rho_e
\quad
\nabla \cdot \mathbf{B} = \rho_m
$$

其中 $\mathbf{E}$ 电场 (V/m), $\mathbf{H}$ 磁场 (A/m), $\mathbf{D} = \epsilon\mathbf{E}$, $\mathbf{B} = \mu\mathbf{H}$, $\mathbf{J}_i$ 和 $\mathbf{M}_i$ 为外加电流/磁流源。

**本构关系（各向同性媒质）：**

$$
\mathbf{D} = \epsilon \mathbf{E}, \quad \mathbf{B} = \mu \mathbf{H}, \quad \mathbf{J} = \sigma \mathbf{E}
$$

**边界条件：**

| 连续量 | 跃变量 |
|--------|--------|
| $\hat{n} \times (\mathbf{E}_1 - \mathbf{E}_2) = 0$ | $\hat{n} \times (\mathbf{H}_1 - \mathbf{H}_2) = \mathbf{J}_s$ |
| $\hat{n} \cdot (\mathbf{D}_1 - \mathbf{D}_2) = \rho_s$ | $\hat{n} \cdot (\mathbf{B}_1 - \mathbf{B}_2) = 0$ |
| PEC: $\hat{n} \times \mathbf{E} = 0$ | PMC: $\hat{n} \times \mathbf{H} = 0$ |

### 1.2 矢量波方程

从 Maxwell 方程组消去一个场量得到：

**电场矢量波方程：**

$$
\nabla \times \left(\frac{1}{\mu_r}\nabla \times \mathbf{E}\right) - k_0^2 \epsilon_r \mathbf{E} = -j k_0 Z_0 \mathbf{J}_i - \nabla \times \left(\frac{1}{\mu_r}\mathbf{M}_i\right)
$$

**磁场矢量波方程：**

$$
\nabla \times \left(\frac{1}{\epsilon_r}\nabla \times \mathbf{H}\right) - k_0^2 \mu_r \mathbf{H} = -j k_0 Y_0 \mathbf{M}_i + \nabla \times \left(\frac{1}{\epsilon_r}\mathbf{J}_i\right)
$$

其中 $k_0 = \omega\sqrt{\mu_0\epsilon_0}$, $Z_0 = \sqrt{\mu_0/\epsilon_0}$, $Y_0 = 1/Z_0$。

### 1.3 标量波方程（二维问题）

对于 TE$_z$ 模式 ($\mathbf{E} = \hat{z} E_z$, $\partial/\partial z = 0$)：

$$
\nabla_t \cdot \left(\frac{1}{\mu_r} \nabla_t E_z\right) + k_0^2 \epsilon_r E_z = j k_0 Z_0 J_z
$$

对于 TM$_z$ 模式 ($\mathbf{H} = \hat{z} H_z$)：

$$
\nabla_t \cdot \left(\frac{1}{\epsilon_r} \nabla_t H_z\right) + k_0^2 \mu_r H_z = -j k_0 Y_0 M_z
$$

### 1.4 边界条件分类

1. **Dirichlet (第一类):** $\phi = p$ 在边界上
2. **Neumann (第二类):** $\partial\phi/\partial n = q$ 在边界上
3. **Robin/Cauchy (第三类/阻抗边界):** $\partial\phi/\partial n + \alpha\phi = \beta$

### 1.5 变分原理

FEM 的核心思想：将 PDE 问题等价为某个泛函的极值问题。

对于标量 Helmholtz 方程 $\nabla^2\phi + k^2\phi = f$，对应的泛函：

$$
F(\phi) = \frac{1}{2}\int_\Omega \left[(\nabla\phi)^2 - k^2\phi^2\right] d\Omega + \int_\Gamma \phi \bar{q} \, d\Gamma
$$

--- 

## Ch2: Finite Difference Method (有限差分法回顾)

### 2.1 有限差分近似

**一阶导数：**

| 格式 | 公式 | 精度 |
|------|------|------|
| 前向 | $\phi'(x) \approx \frac{\phi(x+\Delta x) - \phi(x)}{\Delta x}$ | $O(\Delta x)$ |
| 后向 | $\phi'(x) \approx \frac{\phi(x) - \phi(x-\Delta x)}{\Delta x}$ | $O(\Delta x)$ |
| 中心 | $\phi'(x) \approx \frac{\phi(x+\Delta x) - \phi(x-\Delta x)}{2\Delta x}$ | $O(\Delta x^2)$ |

**二阶导数（中心差分）：**

$$
\phi''(x) \approx \frac{\phi(x+\Delta x) - 2\phi(x) + \phi(x-\Delta x)}{\Delta x^2} \quad O(\Delta x^2)
$$

### 2.2 2D Laplace 方程的五点差分格式

$$
\phi_{i-1,j} + \phi_{i+1,j} + \phi_{i,j-1} + \phi_{i,j+1} - 4\phi_{i,j} = 0
$$

### 2.3 FDTD 简记

FDTD (Yee 算法) 使用交错网格，电场和磁场在时间和空间上交替采样。Maxwell 旋度方程离散为显式蛙跳格式。

CFL 稳定性条件：$\Delta t \leq \frac{1}{c\sqrt{1/\Delta x^2 + 1/\Delta y^2 + 1/\Delta z^2}}$

FDTD 优势：无矩阵求解、天然并行、时域宽带。
FDTD 劣势：网格必须符合 CFL 条件、难以处理曲线边界和精细结构。

---

## Ch3: FEM for One-Dimensional Problems (一维有限元)

### 3.1 变分法（Ritz 方法）

**一般步骤：**

1. 构造泛函 $F(\phi)$，使其 Euler-Lagrange 方程等于原 PDE
2. 将解近似为基函数的线性组合：$\phi \approx \sum_{j=1}^N c_j v_j$
3. 代入泛函，令 $\partial F / \partial c_i = 0$ 得到线性方程组 $[K]\{c\} = \{b\}$

**示例：一维 Poisson 方程**

$$
-\frac{d}{dx}\left(p\frac{d\phi}{dx}\right) + q\phi = f, \quad 0 < x < L
$$

边界条件：$\phi(0) = \phi_0$, $\phi(L) = \phi_L$

对应泛函：

$$
F(\phi) = \frac{1}{2}\int_0^L \left[p\left(\frac{d\phi}{dx}\right)^2 + q\phi^2 - 2f\phi\right] dx
$$

### 3.2 Galerkin 方法

直接对 PDE 做加权余量，令权函数等于基函数（Galerkin 选择）：

$$
\int_\Omega w_i R(\tilde{\phi})\,d\Omega = 0, \quad i = 1,\dots,N
$$

其中 $R = \mathcal{L}\tilde{\phi} - f$ 为余量，$w_i = v_i$。

**Galerkin 与 Ritz 的等价性：** 对于自伴正定算子，Galerkin 方法导出的方程组与 Ritz 方法完全相同。

### 3.3 一维 Lagrange 插值基函数

**线性元（2节点）：**

$$
N_1(\xi) = \frac{1-\xi}{2}, \quad N_2(\xi) = \frac{1+\xi}{2}, \quad -1 \leq \xi \leq 1
$$

或物理坐标：$N_1(x) = \frac{x_2 - x}{h}, N_2(x) = \frac{x - x_1}{h}$

**二次元（3节点）：**

$$
N_1(\xi) = \frac{\xi(\xi-1)}{2}, \quad
N_2(\xi) = (1-\xi)(1+\xi), \quad
N_3(\xi) = \frac{\xi(\xi+1)}{2}
$$

### 3.4 单元矩阵组装

对 Helmholtz 方程，每个线性元的单元矩阵：

$$
[K^e] = \int_{x_1}^{x_2} \left[ \frac{d\{N\}}{dx}\frac{d\{N\}^T}{dx} - k^2\{N\}\{N\}^T\right] dx
$$

$$
[K^e] = \frac{1}{h_e}\begin{bmatrix}1 & -1 \\ -1 & 1\end{bmatrix} - \frac{k^2 h_e}{6}\begin{bmatrix}2 & 1 \\ 1 & 2\end{bmatrix}
$$

全局矩阵通过 "直接刚度法" 将局部节点编号映射到全局编号。

### 3.5 边界条件处理

- **Dirichlet BC:** 直接修改右端项，删对应行/列（或置 1 法）
- **Neumann BC:** 自然满足，不需要显式处理
- **Robin BC:** 修改边界单元的对角元

---

## Ch4: FEM for Two-Dimensional Scalar Problems (二维标量 FEM)

### 4.1 三角元网格

三角元是 2D FEM 最常用单元，适用于任意形状边界。

**面积坐标（重心坐标）：**

对于三角形节点 $(x_1,y_1), (x_2,y_2), (x_3,y_3)$，面积坐标 $L_1, L_2, L_3$ 满足：

$$
L_i = \frac{1}{2\Delta}(a_i + b_i x + c_i y), \quad i=1,2,3
$$

其中 $\Delta$ 为三角形面积，系数 $a_i, b_i, c_i$ 由节点坐标计算：

$$
a_i = x_j y_k - x_k y_j, \quad b_i = y_j - y_k, \quad c_i = x_k - x_j
$$

（下标 $(i,j,k)$ 为 $(1,2,3)$ 的循环置换）

### 4.2 线性三角元基函数

$$
N_i(x,y) = L_i(x,y), \quad i=1,2,3
$$

具有性质：$N_i(x_j,y_j) = \delta_{ij}$, $\sum_{i=1}^3 N_i = 1$

### 4.3 单元矩阵计算（标量 Helmholtz 方程）

$$
\nabla_t^2\phi + k^2\phi = f
$$

**刚度矩阵项：**

$$
S_{ij}^e = \int_{\Omega^e} \nabla N_i \cdot \nabla N_j \, d\Omega = \frac{1}{4\Delta}(b_i b_j + c_i c_j)
$$

**质量矩阵项：**

$$
T_{ij}^e = \int_{\Omega^e} N_i N_j \, d\Omega = \begin{cases}
\frac{\Delta}{6} & i = j \\
\frac{\Delta}{12} & i \neq j
\end{cases}
$$

**载荷向量项：**

$$
f_i^e = \int_{\Omega^e} f N_i \, d\Omega
$$

若 $f$ 在单元内为常数 $f_0$，则 $f_i^e = f_0 \Delta / 3$。

### 4.4 矩形波导 TE 模分析

对于均匀填充矩形波导的 TE 模 ($\mathbf{H} = \nabla_t \phi + \hat{z} H_z$)，求解标量 Helmholtz 方程：

$$
\nabla_t^2 \phi + k_c^2 \phi = 0
$$

边界条件：PEC 壁 $\phi = 0$（Dirichlet）或 PMC 壁 $\partial \phi / \partial n = 0$（Neumann）。

本征值 $k_c$ 与截止频率 $f_c = k_c / (2\pi\sqrt{\mu\epsilon})$。

### 4.5 后处理

解出 $\phi$ 后：
- $\mathbf{E} = -j\omega\mu \nabla\times(\hat{z}\phi)$
- $\mathbf{H} = \nabla_t \phi + \hat{z}H_z$
- 由 $H_z = -k_c^2\phi/(j\omega\mu)$

---

## Ch5: FEM for Two-Dimensional Vector Problems (二维矢量 FEM / 边元)

### 5.1 为什么需要边元

**节点元的缺陷：**

1. **伪模 (Spurious modes):** 节点元不能保证 $\nabla \cdot \mathbf{B} = 0$ 在单元内成立
2. **切向场不连续:** 节点元强制所有分量连续，但实际物理场在媒质界面只有切向连续
3. **奇异场处理:** 在棱边和尖角处场奇异，节点元无法准确表示

### 5.2 棱边元（Whitney 1-形式）

**一阶三角形棱边元（6个自由度 = 6条边的切向场）：**

基函数 $\mathbf{N}_{ij}$ 对应于从节点 $i$ 到节点 $j$ 的边：

$$
\mathbf{N}_{12} = L_1\nabla L_2 - L_2\nabla L_1
$$

显式形式（面积坐标 $L_1, L_2, L_3$）：

$$
\mathbf{W}_{12} = \frac{1}{2\Delta}(b_2 L_1 - b_1 L_2, c_2 L_1 - c_1 L_2)
$$

**关键性质：**
- $\nabla \cdot \mathbf{N}_{ij} = 0$（自然满足散度条件）
- 切向分量在相邻单元间连续
- 法向分量不强制连续

### 5.3 单元矩阵（矢量 Helmholtz / 旋度-旋度方程）

$$
\nabla \times \left(\frac{1}{\mu_r} \nabla \times \mathbf{E}\right) - k_0^2 \epsilon_r \mathbf{E} = -j k_0 Z_0 \mathbf{J}_i
$$

Galerkin 弱形式：

$$
\int_\Omega \frac{1}{\mu_r} (\nabla \times \mathbf{N}_i) \cdot (\nabla \times \mathbf{N}_j) d\Omega - k_0^2 \int_\Omega \epsilon_r \mathbf{N}_i \cdot \mathbf{N}_j d\Omega
= -j k_0 Z_0 \int_\Omega \mathbf{N}_i \cdot \mathbf{J}_i d\Omega
$$

### 5.4 矩形波导 TE/TM 模（矢量公式）

用棱边元直接求解：

$$
\nabla \times \nabla \times \mathbf{E} - k_0^2 \epsilon_r \mathbf{E} = 0
$$

PEC 边界：$\hat{n} \times \mathbf{E} = 0$（切向电场为零 → 直接置零对应的边自由度）

此方法具有无伪模特性。

---

## Ch6: FEM for Three-Dimensional Problems (三维 FEM)

### 6.1 四面体单元

最简单的 3D 体元，4个节点。

**体积坐标（重心坐标）：**

$$
L_i = \frac{V_i}{V}, \quad i = 1,2,3,4
$$

其中 $V$ 为四面体体积，$V_i$ 为与节点 $i$ 相对的子四面体体积。

**线性四面体基函数：**

$$
N_i(x,y,z) = L_i = \frac{1}{6V}(a_i + b_i x + c_i y + d_i z)
$$

系数由节点坐标的 4×4 行列式计算。

### 6.2 四面体单元矩阵

**刚度矩阵：**

$$
S_{ij}^e = \int_{\Omega^e} \nabla N_i \cdot \nabla N_j dV = \frac{1}{36V}(b_i b_j + c_i c_j + d_i d_j)
$$

**质量矩阵：**

$$
T_{ij}^e = \int_{\Omega^e} N_i N_j dV = \begin{cases}
\frac{V}{10} & i = j \\
\frac{V}{20} & i \neq j
\end{cases}
$$

### 6.3 六面体单元

**三线性基函数（8节点）：**

$$
N_i(\xi,\eta,\zeta) = \frac{1}{8}(1 + \xi_i\xi)(1 + \eta_i\eta)(1 + \zeta_i\zeta), \quad i = 1,\dots,8
$$

在 $(\xi,\eta,\zeta) \in [-1,1]^3$ 参考单元上定义。

### 6.4 三维棱边元（Whitney 2-形式）

四面体的边元基函数（6条边）：

$$
\mathbf{N}_{ij} = L_i \nabla L_j - L_j \nabla L_i
$$

同样有 $\nabla \cdot \mathbf{N}_{ij} = 0$ 和切向连续性质。

### 6.5 谐振腔本征值问题

求解三维谐振腔：

$$
\nabla \times \nabla \times \mathbf{E} - k^2 \mathbf{E} = 0
$$

PEC 边界 $\hat{n} \times \mathbf{E} = 0$。

离散后得到广义本征值问题：

$$
[K]\{\mathbf{e}\} = k^2 [M] \{\mathbf{e}\}
$$

求解得到谐振频率 $f = k / (2\pi\sqrt{\mu\epsilon})$。

---

## Ch7: Absorbing Boundary Conditions (吸收边界条件)

### 7.1 为何需要 ABC

计算电磁学中模拟"无限开放空间"时，必须截断计算域。ABC 在截断边界上近似地模拟无反射条件。

### 7.2 Engquist-Majda ABC

对 2D 标量波动方程，抛物近似引出一阶和二阶 ABC：

**一阶 ABC（Engquist-Majda）：**

$$
\frac{\partial \phi}{\partial n} + \frac{1}{c}\frac{\partial \phi}{\partial t} = 0
$$

**频域（时谐）：**

$$
\frac{\partial \phi}{\partial n} + j k \phi = 0
$$

### 7.3 Bayliss-Turkel ABC

对于 2D 圆对称边界（$r = R$）：

**一阶 BT-ABC：**

$$
\frac{\partial \phi}{\partial r} + \left(jk + \frac{1}{2r}\right)\phi = 0
$$

**二阶 BT-ABC：**

$$
\frac{\partial \phi}{\partial r} + \left(jk + \frac{1}{2r} - \frac{1}{8r(1 + jkr)}\frac{\partial^2}{\partial\theta^2}\right)\phi = 0
$$

### 7.4 PML（完全匹配层）

Berenger 1994 年提出的 PML 是最有效的吸收边界技术。

**关键思想：**
- 在计算域外围设置一层有耗介质
- 通过阻抗匹配保证界面无反射
- 波在 PML 内指数衰减

**单轴 PML (UPML):**

用张量媒质参数：

$$
\bar{\bar{\epsilon}} = \epsilon [s], \quad \bar{\bar{\mu}} = \mu [s]
$$

其中：

$$
[s] = \begin{bmatrix}
s_x^{-1} & 0 & 0 \\
0 & s_x & 0 \\
0 & 0 & s_x
\end{bmatrix}
\begin{bmatrix}
s_y & 0 & 0 \\
0 & s_y^{-1} & 0 \\
0 & 0 & s_y
\end{bmatrix}
$$

$$
s_x = 1 - j\frac{\sigma_x}{\omega\epsilon_0}, \quad s_y = 1 - j\frac{\sigma_y}{\omega\epsilon_0}
$$

**电导率渐变（减少数值反射）：**

$$
\sigma(\rho) = \sigma_{\text{max}} \left(\frac{\rho}{d}\right)^m
$$

其中 $\rho$ 为离 PML 内边界的距离，$d$ 为 PML 厚度，$m$ 通常取 2-3。

$$
\sigma_{\text{max}} = -\frac{(m+1)\ln(R)}{2\eta d}
$$

$R$ 为目标反射系数（通常 $10^{-4}$ 到 $10^{-8}$）。

---

## Ch8: Finite Element — Boundary Integral Method (FEM-BI)

### 8.1 方法概述

FEM-BI 将有限元（处理非均匀、复杂结构）与边界积分（处理无限域）结合。

### 8.2 基本原理

1. **内部区域**（含不均匀媒质）：用 FEM 离散
2. **外部区域**（均匀自由度空间）：用边界积分方程（BIE）描述
3. **耦合条件**：在虚拟边界上通过切向场连续条件耦合

### 8.3 边界积分方程

对于外部均匀区域，利用 Green 函数构造积分方程：

标量情况（Helmholtz 方程）：

$$
\phi(\mathbf{r}) = \int_\Gamma \left[ G(\mathbf{r},\mathbf{r}') \frac{\partial\phi(\mathbf{r}')}{\partial n'} - \phi(\mathbf{r}') \frac{\partial G(\mathbf{r},\mathbf{r}')}{\partial n'} \right] d\Gamma'
$$

其中 $G(\mathbf{r},\mathbf{r}') = -\frac{j}{4}H_0^{(2)}(k|\mathbf{r}-\mathbf{r}'|)$ 为 2D Green 函数。

矢量情况（3D）：

$$
\mathbf{E}(\mathbf{r}) = \mathbf{E}^{\text{inc}} + \int_\Gamma \left[ j\omega\mu \bar{\bar{G}}_0 \cdot (\hat{n} \times \mathbf{H}) + \nabla \times \bar{\bar{G}}_0 \cdot (\hat{n} \times \mathbf{E}) \right] d\Gamma'
$$

### 8.4 耦合策略

- **直接耦合:** FEM 和 BIE 联立求解（稠密子矩阵 + 稀疏子矩阵）
- **迭代耦合:** FEM 内部求解，BIE 作为边界条件（迭代收敛）

---

## Ch9: Periodic Structures (周期结构 FEM)

### 9.1 Floquet 定理

对于周期为 $p$ 的无限周期结构：

$$
\mathbf{E}(x + p, y, z) = \mathbf{E}(x, y, z) e^{-j k_x p}
$$

或一般形式：

$$
\mathbf{E}(\mathbf{r} + \mathbf{p}) = \mathbf{E}(\mathbf{r}) e^{-j\mathbf{k}_\text{F} \cdot \mathbf{p}}
$$

其中 $\mathbf{k}_\text{F} = k_0(\hat{x}\sin\theta\cos\phi + \hat{y}\sin\theta\sin\phi)$ 为 Floquet 波矢。

### 9.2 周期边界条件（PBC）

用 Floquet 周期边界将计算域缩至一个周期单元：

$$
\phi(\mathbf{r} + \mathbf{p}) = \phi(\mathbf{r}) e^{j\theta}
$$

其中 $\theta = -\mathbf{k}_\text{F} \cdot \mathbf{p}$ 为周期相位差。

### 9.3 FEM 实现

周期边界将单元内节点分为：
- **内部节点:** 常规处理
- **主边界节点:** 保留为独立自由度
- **从边界节点:** 通过相位关系关联到主边界

矩阵方程修改：

$$
[K(\theta)] \{\phi\} = k^2 [M(\theta)] \{\phi\}
$$

本征值 $k$ 随相位 $\theta$ 变化 → 得到色散曲线（能带结构）。

### 9.4 应用

- 频率选择表面（FSS）
- 光子晶体
- 相控阵天线
- 超材料（Metamaterials）

---

## Ch10: Eddy Current Problems (涡流/低频 FEM)

### 10.1 低频涡流方程

忽略位移电流（$k_0 \to 0$），Maxwell 方程简化为涡流方程：

$$
\nabla \times \mathbf{H} = \mathbf{J}_s + \sigma \mathbf{E}
$$

$$
\nabla \times \mathbf{E} = -j\omega\mu\mathbf{H}
$$

**$\mathbf{A}$-$\phi$ 公式（磁矢量势 + 标量电势）：**

$$
\mathbf{B} = \nabla \times \mathbf{A}, \quad \mathbf{E} = -j\omega\mathbf{A} - \nabla\phi
$$

代入得：

$$
\nabla \times \left(\frac{1}{\mu}\nabla \times \mathbf{A}\right) + j\omega\sigma\mathbf{A} + \sigma\nabla\phi = \mathbf{J}_s
$$

**库仑规范 $\nabla \cdot \mathbf{A} = 0$**：用罚函数法或棱边元自动满足。

### 10.2 $\mathbf{T}$-$\Omega$ 公式（电感向量势 + 磁标势）

$$
\mathbf{H} = \mathbf{T} - \nabla\Omega
$$

$$
\nabla \times \left(\frac{1}{\sigma}\nabla \times \mathbf{T}\right) + j\omega\mu(\mathbf{T} - \nabla\Omega) = 0
$$

$$
\nabla \cdot [\mu(\mathbf{T} - \nabla\Omega)] = 0
$$

### 10.3 集肤深度

$$
\delta = \frac{1}{\sqrt{\pi f \mu \sigma}}
$$

低频时 $\delta$ 很大（透入深），高频时趋肤效应显著（$\delta$ 小 → 需非常细的网格）。

### 10.4 应用

- 变压器和电机的涡流损耗
- 感应加热
- 电磁屏蔽分析
- 无损检测（NDT/NDE）

---

## Ch11: Mesh Generation (网格生成与自适应)

### 11.1 网格类型

| 类型 | 2D | 3D |
|------|----|-----|
| 结构化 | 四方网格 | 六面体网格 |
| 非结构化 | 三角网格 | 四面体网格 |
| 混合 | 四边形主导 | 棱柱/金字塔过渡 |

### 11.2 三角剖分算法

**Delaunay 三角剖分：**
- 最大化最小角（避免狭长三角形）
- 空外接球准则
- Bowyer-Watson 算法实现

**推进波前法 (Advancing Front):**
- 从边界开始逐层向内推进
- 适合控制边界附近的网格密度

### 11.3 网格质量指标

| 指标 | 公式 | 理想值 |
|------|------|--------|
| 纵横比 (Aspect Ratio) | 最长边 / 最短边 | 1 |
| 偏斜度 (Skewness) | 偏离正三角形程度 | 0 |
| Jacobian 比 | 最小/最大 Jacobian | 1 |

### 11.4 h-自适应（h-Adaptive）

- **h-细化：** 加密误差大的区域 → 分半法（红色/绿色细化）
- **h-粗化：** 合并误差小的区域 → 边交换/边折叠
- **误差估计：** Zienkiewicz-Zhu（Z-Z）超收敛补片恢复法

### 11.5 p-自适应（p-Adaptive）

保持网格不变，提高局部插值阶数：
- 低阶元 → 高阶元
- 更高效（指数收敛），但实现复杂
- 常与 h-自适应结合为 hp-自适应

---

## Ch12: Solution Techniques (求解技术)

### 12.1 线性方程组分类

**FEM 产生的大型稀疏矩阵：**

| 类型 | 特征 | 求解方法 |
|------|------|----------|
| 正定对称 | 静电场/静磁场/涡流(低频) | Cholesky/CG |
| 不定对称 | 亥姆霍兹（波动） | MINRES/SYMMLQ |
| 非对称 | 含辐射边界条件的散射 | GMRES/BiCGSTAB |
| 广义本征值 | $[A]\{x\} = \lambda[B]\{x\}$ | Lanczos/Arnoldi |

### 12.2 直接求解器

- **LDU 分解:** 对稀疏矩阵符号分解 + 数值分解
- **多重波前法 (MUMPS):** 目前最流行的直接法
- **复杂度：** 2D $O(N^{1.5})$, 3D $O(N^2)$

### 12.3 迭代求解器

| 方法 | 适用 | 收敛速度 |
|------|------|----------|
| CG (共轭梯度) | 对称正定 | $\propto \sqrt{\kappa}$ |
| GMRES | 一般非对称 | $\propto \kappa$ |
| BiCGSTAB | 非对称 | 比 GMRES 省内存 |
| IDR(s) | 非对称 | 稳定高效 |

### 12.4 预条件

必要！无预条件的迭代法对 FEM 矩阵几乎不收敛。

| 预条件 | 优点 | 缺点 |
|--------|------|------|
| Jacobi (对角) | 简单 | 效果有限 |
| SSOR | 能处理各向异性 | 串行，难并行 |
| 不完全 Cholesky (IC) | SPD 问题效果好 | 填充多 |
| ILU(0) | 通用 | 高阶元效果差 |
| 多重网格 (MG) | $O(N)$ 最优 | 对非均匀网格实现复杂 |
| 区域分解 (DD) | 并行性好 | 需要重叠 |
| SPAI (稀疏近似逆) | 天然并行 | 构建成本高 |

### 12.5 本征值求解

FEM 分析谐振腔/波导截面的核心：

**Arnoldi 方法 (ARPACK):**
- 使用 Krylov 子空间迭代
- 可求解 $n$ 个最小（或最大）本征值
- Python: `scipy.sparse.linalg.eigs`

**Lanczos 方法：**
- Hermitian 矩阵特化版
- 三对角化 + QR

### 12.6 计算量关系

| 维度 | 自由度 | 矩阵非零元 | 直接法 |
|------|--------|-----------|--------|
| 1D | $N$ | $O(3N)$ | $O(N)$ |
| 2D | $N$ | $O(5N)$ | $O(N^{1.5})$ |
| 3D | $N$ | $O(7N)$ | $O(N^2)$ |

---

## 附录：常用公式速查

### 三角形积分公式

$$
\int_{\Delta} L_1^a L_2^b L_3^c \, dA = \frac{a! b! c!}{(a+b+c+2)!} \cdot 2\Delta
$$

### 四面体积分公式

$$
\int_{V^e} L_1^a L_2^b L_3^c L_4^d \, dV = \frac{a! b! c! d!}{(a+b+c+d+3)!} \cdot 6V
$$

### Green 函数

| 维度 | 方程 | Green 函数 |
|------|------|-----------|
| 2D | $\nabla^2 G + k^2 G = -\delta$ | $G = -\frac{j}{4} H_0^{(2)}(k\rho)$ |
| 3D | $\nabla^2 G + k^2 G = -\delta$ | $G = \frac{e^{-jkr}}{4\pi r}$ |

### 常用数值积分

Gauss-Legendre 积分在参考单元 $[-1,1]$：

| 点数 $n$ | 节点 $\xi_i$ | 权重 $w_i$ |
|----------|-------------|-----------|
| 1 | 0 | 2 |
| 2 | $\pm 1/\sqrt{3}$ | 1 |
| 3 | $0, \pm\sqrt{3/5}$ | $8/9, 5/9$ |

### 归一化坐标变换

**一维：** $x = \frac{x_1 + x_2}{2} + \frac{h}{2}\xi$

**三角形（参考到物理）：**
$$
\begin{bmatrix}x \\ y\end{bmatrix} = 
\begin{bmatrix}x_1 & x_2 & x_3 \\ y_1 & y_2 & y_3\end{bmatrix}
\begin{bmatrix}L_1 \\ L_2 \\ L_3\end{bmatrix}
$$

**四面体（体积坐标到笛卡尔）：** 同上，扩展到 4 个坐标。

---

## 参考文献

[1] J.-M. Jin, *The Finite Element Method in Electromagnetics*, 3rd ed. Wiley-IEEE, 2014.
[2] J.-M. Jin and D. J. Riley, *Finite Element Analysis of Antennas and Arrays*, Wiley, 2008.
[3] P. P. Silvester and R. L. Ferrari, *Finite Elements for Electrical Engineers*, 3rd ed. Cambridge, 1996.
[4] J.-P. Berenger, "A perfectly matched layer for the absorption of electromagnetic waves," *J. Comput. Phys.*, vol. 114, pp. 185-200, 1994.
[5] O. C. Zienkiewicz, R. L. Taylor, and J. Z. Zhu, *The Finite Element Method: Its Basis and Fundamentals*, 6th ed. Butterworth-Heinemann, 2005.
