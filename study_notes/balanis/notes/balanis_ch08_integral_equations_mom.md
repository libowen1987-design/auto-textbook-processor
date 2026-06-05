# Chapter 8: Integral Equations, Moment Method, and Self and Mutual Impedances
# 第8章：积分方程、矩量法与自阻抗/互阻抗

> **核心思想**：天线问题是开域边值问题，直接解微分方程需要离散整个计算域，而积分方程法（IE）利用 Green 函数自动满足辐射条件，将自由度限制在天线导体表面，降维求解。矩量法（MoM）将积分方程离散为矩阵方程，是天线数值分析的基石。

**注意**：本章在 Balanis 4th Edition 中称为 "Integral Equations, Moment Method, and Self and Mutual Impedances"，内容包含 EFIE/MFIE 的推导、矩量法的一般理论、以及细线天线应用。

---


### 1.1 微分方程方法的局限性

直接解 Maxwell 方程组（FEM/FDTD）需要离散整个计算域 → 开域辐射问题需要对无穷远空间截断 → 引入吸收边界条件 → 带来截断误差。

### 1.2 积分方程的优势

- Green 函数自动满足 Sommerfeld 辐射条件（无穷远边界自动满足）
- 自由度仅分布在散射体/天线表面（降维）
- 对细线天线（线半径 $a \ll \lambda$），进一步降为 1D 积分方程

### 1.3 基本原理

对于自由空间中的任意电流分布 $\mathbf{J}(\mathbf{r}')$，矢量磁位为：

$$
\mathbf{A}(\mathbf{r}) = \mu_0 \iiint_V \mathbf{J}(\mathbf{r}') G(\mathbf{r}, \mathbf{r}') \, dV'
$$

其中自由空间 Green 函数为：

$$
\boxed{G(\mathbf{r}, \mathbf{r}') = \frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{4\pi |\mathbf{r} - \mathbf{r}'|}}
$$

电场由矢量磁位得到：

$$
\mathbf{E}(\mathbf{r}) = -j\omega\mathbf{A}(\mathbf{r}) - \frac{j}{\omega\mu_0\epsilon_0} \nabla(\nabla \cdot \mathbf{A}(\mathbf{r}))
$$

---


### 2.1 一般形式

对于理想导体（PEC）表面 $S$，切向电场满足边界条件：

$$
\hat{\mathbf{n}} \times \mathbf{E}^{\text{total}} = 0 \quad \text{on } S
$$

散射场由感应电流 $\mathbf{J}_s$ 产生：

$$
\mathbf{E}^{\text{scat}}(\mathbf{r}) = -j\omega\mathbf{A}(\mathbf{r}) - \frac{j}{\omega\mu_0\epsilon_0} \nabla(\nabla \cdot \mathbf{A}(\mathbf{r}))
$$

因此：

$$
\hat{\mathbf{n}} \times \left[ \mathbf{E}^{\text{inc}}(\mathbf{r}) + \mathbf{E}^{\text{scat}}(\mathbf{r}) \right] = 0 \quad \text{on } S
$$

得到 EFIE：

$$
\boxed{\hat{\mathbf{n}} \times \mathbf{E}^{\text{inc}}(\mathbf{r}) = \hat{\mathbf{n}} \times \left[ j\omega \iint_S \mathbf{J}_s(\mathbf{r}') G(\mathbf{r}, \mathbf{r}') \, dS' + \frac{j}{\omega\mu_0\epsilon_0} \nabla \iint_S \nabla' \cdot \mathbf{J}_s(\mathbf{r}') G(\mathbf{r}, \mathbf{r}') \, dS' \right]}
$$

### 2.2 EFIE 的物理意义

- EFIE 对**开**和**闭**导体都适用
- 共振频率处（腔体内谐振）解唯一——这是 EFIE 相比 MFIE 的优势
- 薄导体/细线天线中最为常用

---


### 3.1 一般形式

对于 PEC 表面，磁场边界条件为：

$$
\hat{\mathbf{n}} \times \mathbf{H}^{\text{total}} = \mathbf{J}_s \quad \text{on } S
$$

散射磁场为：

$$
\mathbf{H}^{\text{scat}}(\mathbf{r}) = \frac{1}{\mu_0} \nabla \times \mathbf{A}(\mathbf{r}) = \nabla \times \iint_S \mathbf{J}_s(\mathbf{r}') G(\mathbf{r}, \mathbf{r}') \, dS'
$$

代入边界条件：

$$
\boxed{\mathbf{J}_s(\mathbf{r}) = \hat{\mathbf{n}} \times \mathbf{H}^{\text{inc}}(\mathbf{r}) + \hat{\mathbf{n}} \times \iint_S \mathbf{J}_s(\mathbf{r}') \times \nabla' G(\mathbf{r}, \mathbf{r}') \, dS'}
$$

### 3.2 MFIE 的特点

- 仅适用于**封闭** PEC 表面（因为推导用了 Stratton-Chu 公式中的 $\Omega=2\pi$）
- 在共振频率处解**不唯一**（有内部共振解污染）
- 条件数通常比 EFIE 好（第二类 Fredholm 方程）

---


### 4.1 细线近似（Thin Wire Approximation）

对于线半径 $a \ll \lambda$ 且 $a \ll L$ 的细线天线：

- 电流仅有轴向分量（沿 $z$ 方向）：$\mathbf{J}(\mathbf{r}') = \hat{\mathbf{z}} I(z') / (2\pi a)$
- 电流在导线表面等效为在轴线上流动（细线近似）
- 边界条件只在导线表面（$\rho = a$）施加

矢量磁位简化为：

$$
A_z(z) = \frac{\mu_0}{4\pi} \int_{-L/2}^{L/2} I(z') \frac{e^{-jkR}}{R} \, dz'
$$

其中：

$$
R = \sqrt{(z - z')^2 + a^2}
$$

### 4.2 Pocklington 积分方程

在细线近似下，电场只有 $z$ 分量，由边界条件 $E_z^{\text{inc}} + E_z^{\text{scat}} = 0$ 在 $\rho = a$ 处成立：

$$
E_z^{\text{inc}}(z) = \frac{j}{\omega\epsilon_0} \left( \frac{\partial^2}{\partial z^2} + k^2 \right) \int_{-L/2}^{L/2} I(z') \frac{e^{-jkR}}{4\pi R} \, dz'
$$

交换微分和积分，得到 **Pocklington 方程**：

$$
\boxed{E_z^{\text{inc}}(z) = \frac{j\eta_0}{4\pi k} \int_{-L/2}^{L/2} I(z') \left( \frac{\partial^2}{\partial z^2} + k^2 \right) \frac{e^{-jkR}}{R} \, dz'}
$$

其中 $\eta_0 = \sqrt{\mu_0/\epsilon_0} \approx 120\pi \, \Omega$ 是自由空间波阻抗。

展开二阶导数后：

$$
\left( \frac{\partial^2}{\partial z^2} + k^2 \right) \frac{e^{-jkR}}{R} = \frac{e^{-jkR}}{R^5} \left[ (1 + jkR)(2R^2 - 3a^2) + (kaR)^2 \right]
$$

**对于 $\delta$ 间隙电压源**（中心馈电）：$E_z^{\text{inc}}(z) = V_0 \delta(z)$，其中 $V_0$ 是激励电压。

### 4.3 Hallen 积分方程

Pocklington 方程包含二阶导数，数值实现中数值精度要求高。Hallen 将其转化为更简洁的形式。

从 Pocklington 方程出发，交换微分和积分并利用 $k^2 = \omega^2\mu_0\epsilon_0$：

$$
\frac{\partial^2 A_z}{\partial z^2} + k^2 A_z = -j\omega\epsilon_0 \mu_0 E_z^{\text{inc}}(z)
$$

对于 $E_z^{\text{inc}} = \delta$ 源（中心馈电），这是一个 Helmholtz 方程，通解为齐次解 + 特解：

$$
\boxed{\int_{-L/2}^{L/2} I(z') \frac{e^{-jkR}}{4\pi R} \, dz' = C_1 \cos(kz) + C_2 \sin(kz) - \frac{jV_0}{2\eta_0} \sin(k|z|)}
$$

其中 $C_1$ 和 $C_2$ 由端点边界条件 $I(\pm L/2) = 0$ 确定，$V_0$ 是馈电电压幅值。

**Hallen 方程的关键优势**：
- 被积函数无导数（只有 Green 函数本身），数值稳定性好
- 核函数 $e^{-jkR}/R$ 的奇异性为 $1/R$（可积弱奇异）
- 是第二类 Fredholm 积分方程

### 4.4 Pocklington vs Hallen 对比

| 特性 | Pocklington | Hallen |
|------|-------------|--------|
| 被积函数 | 含二阶导数 | 无导数 |
| 数值实现 | 需要数值微分或部分积分 | 直接数值积分 |
| 奇异性 | 高阶（$1/R^3$） | 弱（$1/R$） |
| 方程类型 | 被积函数有导数 → 较敏感 | 第二类 Fredholm |
| 应用中 | Galerkin 法常用 | 点匹配法常用 |

---


### 5.1 一般理论

考虑一般形式的算子方程：

$$
\mathcal{L}(f) = g
$$

其中 $\mathcal{L}$ 是线性算子，$f$ 是未知函数（如电流分布），$g$ 是已知源项（如激励场）。

**MoM 三步骤：**

1. **展开**：将 $f$ 用 $N$ 个基函数逼近
   $$
   f \approx \sum_{n=1}^N I_n f_n
   $$

2. **测试**：用 $N$ 个权函数 $w_m$ 对残差 $R = \mathcal{L}(f) - g$ 施加内积约束
   $$
   \langle w_m, R \rangle = 0, \quad m = 1, 2, \ldots, N
   $$

3. **矩阵求解**：
   $$
   \sum_{n=1}^N I_n \langle w_m, \mathcal{L}(f_n) \rangle = \langle w_m, g \rangle
   $$
   即：
   $$
   \boxed{\mathbf{Z} \mathbf{I} = \mathbf{V}}
   $$
   其中 $Z_{mn} = \langle w_m, \mathcal{L}(f_n) \rangle$ 是阻抗矩阵元素，$V_m = \langle w_m, g \rangle$ 是激励向量。

### 5.2 基函数

#### 子域基函数

| 类型 | 定义 | 特点 |
|------|------|------|
| **脉冲 (Pulse)** | $f_n(z) = \begin{cases} 1, & z_n - \Delta/2 < z < z_n + \Delta/2 \\ 0, & \text{else} \end{cases}$ | 最简单，分段常数，收敛慢 |
| **三角 (Triangle)** | $f_n(z) = \begin{cases} 1 - |z - z_n|/\Delta, & |z - z_n| < \Delta \\ 0, & \text{else} \end{cases}$ | 连续线性，收敛快于脉冲 |
| **正弦 (Sinusoidal)** | $f_n(z) = \frac{\sin(k(\Delta - |z - z_n|))}{\sin(k\Delta)}$ | 符合细线天线物理，精度高 |

#### 全域基函数 (Entire-Domain)

$$
f_n(z) = \sin\left( \frac{n\pi}{L}(z + L/2) \right), \quad n = 1, 2, \ldots
$$

由端点电流为零自动满足：$f_n(\pm L/2) = 0$。

### 5.3 权函数 / 测试方法

| 方法 | $w_m$ | 特点 |
|------|-------|------|
| **点匹配 (Point Matching / Collocation)** | $w_m(z) = \delta(z - z_m)$ | 最简单，仅需在离散点满足方程 |
| **Galerkin 法** | $w_m(z) = f_m(z)$ | 权函数 = 基函数，矩阵对称，精度高 |
| **最小二乘法** | $w_m = \mathcal{L}(f_m)$ | 残差平方最小化 |
| **矩量法（广义）** | 任意权函数 | 以上都是特例 |

**点匹配**最常用於 Hallen 方程，因为 $Z_{mn}$ 是简单的单重积分：

$$
Z_{mn} = \int_{\Delta z_n} \frac{e^{-jkR_{mn}}}{4\pi R_{mn}} \, dz'
$$

其中 $R_{mn} = \sqrt{(z_m - z')^2 + a^2}$。

**Galerkin 法**常用於 Pocklington 方程，阻抗矩阵元素为二重积分：

$$
Z_{mn} = \frac{j\eta_0}{4\pi k} \iint f_m(z) f_n(z') \left( \frac{\partial^2}{\partial z^2} + k^2 \right) \frac{e^{-jkR}}{R} \, dz' \, dz
$$

通过分部积分将二阶导数转移到测试函数 $f_m$ 上：

$$
Z_{mn} = \frac{j\eta_0}{4\pi k} \iint \left[ k^2 f_m(z) f_n(z') - f_m'(z) f_n'(z') \right] \frac{e^{-jkR}}{R} \, dz' \, dz
$$

这降低了奇异核的阶数（从 $1/R^3$ 降至 $1/R$），数值稳定性大大提升。

### 5.4 激励向量

对于中心馈电的 \delta 间隙源 $V_0 \delta(z)$：

- **点匹配**：$V_m = \langle \delta(z - z_m), E_z^{\text{inc}} \rangle = V_0$ 仅在馈电点，其余为 0
- **Galerkin**：$V_m = \langle f_m(z), V_0 \delta(z) \rangle = f_m(0) \cdot V_0$

---


### 6.1 阻抗元素的一般表达式

根据测试方式，阻抗矩阵元素具有不同形式。

**对于点匹配法（Hallen）：**
$$
Z_{mn} = \frac{\mu_0}{4\pi} \int_{z_n - \Delta/2}^{z_n + \Delta/2} \frac{e^{-jkR_{mn}}}{R_{mn}} \, dz'
$$
其中 $R_{mn} = \sqrt{(z_m - z_n')^2 + a^2}$。

**对于 Galerkin 法（Pocklington，分部积分后）：**
$$
Z_{mn} = \frac{j\eta_0}{4\pi k} \int_{z_m - \Delta}^{z_m + \Delta} \int_{z_n - \Delta}^{z_n + \Delta} f_m(z) f_n(z') \left( k^2 + \frac{\partial^2}{\partial z\, \partial z'} \right) \frac{e^{-jkR}}{R} \, dz' \, dz
$$

其中 $R = \sqrt{(z - z')^2 + a^2}$。

### 6.2 自阻抗元素与奇异性处理

当 $m = n$（自阻抗），$z_m = z_n$ 时，Green 函数在 $z' = z$ 处有奇点。

**精确处理**：对于 ${e^{-jkR}}/{R}$ 核，将积分分解为：

$$
\int_{-\Delta/2}^{\Delta/2} \frac{e^{-jk\sqrt{u^2 + a^2}}}{\sqrt{u^2 + a^2}} \, du = \int_{-\Delta/2}^{\Delta/2} \frac{1}{\sqrt{u^2 + a^2}} \, du + \int_{-\Delta/2}^{\Delta/2} \frac{e^{-jk\sqrt{u^2 + a^2}} - 1}{\sqrt{u^2 + a^2}} \, du
$$

第一项解析可积：

$$
\int_{-\Delta/2}^{\Delta/2} \frac{1}{\sqrt{u^2 + a^2}} \, du = \ln\left( \frac{\Delta/2 + \sqrt{(\Delta/2)^2 + a^2}}{-\Delta/2 + \sqrt{(\Delta/2)^2 + a^2}} \right) = 2 \sinh^{-1}\left( \frac{\Delta}{2a} \right)
$$

第二项无奇点，可用高斯数值积分。

### 6.3 数值积分策略

- **非对角线元素**（$m \neq n$）：标准 Gauss-Legendre 积分（4-10 点足够）
- **对角线元素**（$m = n$）：奇点提取 + 剩余部分数值积分
- **远距离元素**（$|z_m - z_n| \gg a$）：可用中点近似 $\int f(z') e^{-jkR}/R \, dz' \approx e^{-jkR_{mn}}/R_{mn} \cdot \Delta z_n$

---


### 7.1 离散化过程

将导线长度 $L$ 分为 $N$ 段，每段长度 $\Delta = L/N$。匹配点在每段中心 $z_m$。

基函数采用脉冲函数：

$$
I(z') = \sum_{n=1}^N I_n p_n(z')
$$

其中 $p_n(z') = 1$ 在 $z_n - \Delta/2 < z' < z_n + \Delta/2$，否则为 0。

Hallen 方程离散为：

$$
\sum_{n=1}^N I_n \frac{\mu_0}{4\pi} \int_{\Delta z_n} \frac{e^{-jkR_{mn}}}{R_{mn}} \, dz' = C_1 \cos(kz_m) + C_2 \sin(kz_m) - \frac{jV_0}{2\eta_0} \sin(k|z_m|)
$$

写为矩阵形式：

$$
\mathbf{Z} \mathbf{I} = C_1 \mathbf{C} + C_2 \mathbf{S} + \mathbf{V}^{\text{inc}}
$$

其中：

$$
C_m = \cos(kz_m), \quad S_m = \sin(kz_m), \quad V_m^{\text{inc}} = -\frac{jV_0}{2\eta_0} \sin(k|z_m|)
$$

### 7.2 未知数处理

因为有 $N$ 个电流未知数 + 2 个常数 $C_1, C_2$，共 $N+2$ 个未知数。补充两个边界条件 $I(z = \pm L/2) = 0$：

$$
\sum_{n=1}^N I_n p_n(z = -L/2) = 0, \quad \sum_{n=1}^N I_n p_n(z = +L/2) = 0
$$

当匹配点与边界重合时，直接设 $I_1 = I_N = 0$，减少系统到 $N-2$ 个未知数。

### 7.3 等效求解方案

更常用的方案：将 $C_1, C_2$ 也作为未知数，写出扩展矩阵：

$$
\begin{bmatrix}
\mathbf{Z} & -\mathbf{C} & -\mathbf{S}
\end{bmatrix}
\begin{bmatrix}
\mathbf{I} \\
C_1 \\
C_2
\end{bmatrix}
= \mathbf{V}^{\text{inc}}
$$

加入两个边界方程后求解 $(N+2) \times (N+2)$ 系统。

### 7.4 输入阻抗计算

得到电流分布 $I(z)$ 后，输入阻抗为馈电点电流的倒数（对 $\delta$ 源 $V_0 = 1$ V）：

$$
Z_{\text{in}} = \frac{V_0}{I(0)} = \frac{1}{I_{\text{feed}}}
$$

其中 $I_{\text{feed}}$ 是馈电点所在段（$z \approx 0$）的电流系数。

---


### 8.1 离散化

采用三角基函数和 Galerkin 测试。使用分部积分降低奇异核阶数：

$$
Z_{mn} = \frac{j\eta_0}{4\pi k} \int_{z_m - \Delta}^{z_m + \Delta} \int_{z_n - \Delta}^{z_n + \Delta} \left[ k^2 f_m(z) f_n(z') - f_m'(z) f_n'(z') \right] \frac{e^{-jkR}}{R} \, dz' \, dz
$$

其中三角基函数定义为：

$$
f_n(z) = \begin{cases}
1 - |z - z_n|/\Delta, & |z - z_n| \leq \Delta \\
0, & \text{otherwise}
\end{cases}
$$

导数为分段常数：

$$
f_n'(z) = \begin{cases}
-1/\Delta, & z_n < z < z_n + \Delta \\
1/\Delta, & z_n - \Delta < z < z_n \\
0, & \text{otherwise}
\end{cases}
$$

### 8.2 激励向量

对于 \delta 间隙源 $V_0 \delta(z)$：

$$
V_m = \int f_m(z) V_0 \delta(z) \, dz = V_0 f_m(0)
$$

只有馈电点附近（$z_m = 0$ 或相邻）的测试函数有非零值。

### 8.3 输入阻抗

$$
Z_{\text{in}} = \frac{V_0}{I(0)} = \frac{1}{\sum_n I_n f_n(0)}
$$

---


### 9.1 从电流分布到远场

得到电流分布 $I(z')$ 后，远场 $E_\theta$ 为：

$$
E_\theta(\theta) = j\eta_0 \frac{e^{-jkr}}{2\lambda r} \sin\theta \int_{-L/2}^{L/2} I(z') e^{jkz' \cos\theta} \, dz'
$$

离散形式：

$$
E_\theta(\theta) = j\eta_0 \frac{e^{-jkr}}{2\lambda r} \sin\theta \sum_{n=1}^N I_n \int_{\Delta z_n} f_n(z') e^{jkz' \cos\theta} \, dz'
$$

### 9.2 方向性系数

$$
D_0 = \frac{4\pi U_{\max}}{P_{\text{rad}}}
$$

其中：

$$
U(\theta) = \frac{r^2}{2\eta_0} |E_\theta(\theta)|^2
$$

$$
P_{\text{rad}} = \frac{1}{2} \text{Re} \left\{ V_0 I^*(0) \right\} \quad \text{（或通过辐射积分）}
$$

---


### 10.1 多导线扩展

对于 $M$ 根平行导线，每根导线 $N_i$ 个基函数，总未知数为 $\sum_{i=1}^M N_i$。

阻抗矩阵分块：

$$
\mathbf{Z} = \begin{bmatrix}
\mathbf{Z}_{11} & \mathbf{Z}_{12} & \cdots & \mathbf{Z}_{1M} \\
\mathbf{Z}_{21} & \mathbf{Z}_{22} & \cdots & \mathbf{Z}_{2M} \\
\vdots & \vdots & \ddots & \vdots \\
\mathbf{Z}_{M1} & \mathbf{Z}_{M2} & \cdots & \mathbf{Z}_{MM}
\end{bmatrix}
$$

其中 $\mathbf{Z}_{ii}$ 是第 $i$ 根导线的自阻抗块，$\mathbf{Z}_{ij}$ 是导线 $j$ 对导线 $i$ 的互阻抗块。

### 10.2 远距离互阻抗近似

当导线间距 $d_{ij} \gg a_i, a_j$ 时：

$$
Z_{mn}^{(ij)} \approx \frac{j\eta_0}{4\pi k} \iint f_m^{(i)}(z) f_n^{(j)}(z') \left( \frac{\partial^2}{\partial z^2} + k^2 \right) \frac{e^{-jkR_{ij}}}{R_{ij}} \, dz' \, dz
$$

其中 $R_{ij} = \sqrt{(z - z')^2 + d_{ij}^2}$。

---


### 11.1 段数选择

- 经验规则：$\Delta \approx \lambda / (10 \sim 20)$
- 半波偶极子（$L = 0.5\lambda$）：$N = 5 \sim 20$ 段即可收敛
- 全波偶极子（$L = \lambda$）：$N = 10 \sim 30$

### 11.2 收敛性检查

计算输入阻抗随 $N$ 的变化：

$$
Z_{\text{in}}(N) = R_{\text{in}}(N) + jX_{\text{in}}(N)
$$

当 $N$ 充分大时，$Z_{\text{in}}(N)$ 应收敛至稳定值。

**重要注意事项**：
- MoM 结果收敛到的极限值取决于导线半径 $a$。对于 $a=0.001\lambda$ 的
半波偶极子，MoM 收敛至 King-Middleton 值约 $85 + j42\,\Omega$。
- Ch4 感应 EMF 法给出的 $73.1 + j42.5\,\Omega$ 是 $a \to 0$ 的极限，
不适用于有限半径的 MoM 验证。
- 电抗 $X_{\text{in}}$ 的收敛速度比电阻 $R_{\text{in}}$ 慢，需要更多分段。
对于 $a=0.001\lambda$ 的半波偶极子，$N \geq 100$ 时 $R_{\text{in}}$ 趋稳，
$N \geq 200$ 时 $X_{\text{in}}$ 趋稳。
- 当 $N$ 太小时（$N < 30$），$X_{\text{in}}$ 可能出现负值——这是
数值欠收敛的表现，并非物理上的容性阻抗。

### 11.3 与 Ch4 解析解的对比验证

半波偶极子（$L = 0.5\lambda$，$a = 0.001\lambda$）：

| 方法 | $R_{\text{in}}$ [Ω] | $X_{\text{in}}$ [Ω] | 说明 |
|------|-------------------|-------------------|------|
| Ch4 感应 EMF 法 (解析, $a \to 0$) | 73.1 | 42.5 | 无限细偶极子极限 |
| King-Middleton 2nd ($a=0.001\lambda$) | 84.5 | 41.3 | 有限半径修正 (King's tables) |
| MoM Hallen PM ($N=21$) | 70.6 | -4.5 | MoM 尚未收敛（$N$ 太小） |
| MoM Hallen PM ($N=51$) | 79.2 | 25.2 | 部分收敛 |
| MoM Hallen PM ($N=101$) | 82.9 | 36.2 | 接近收敛 |
| MoM Hallen PM ($N=201$) | 85.3 | 42.1 | 收敛至 King-Middleton 值 |
| MoM Hallen Galerkin ($N=81$) | 79.7 | 26.8 | 收敛速度慢于点匹配 |

**收敛说明**：MoM 数值结果在大 $N$ 极限下应收敛至 King-Middleton 理论值
（约 $85 + j42\,\Omega$），而非 Ch4 的 $a\to 0$ EMF 解析值（$73.1 + j42.5\,\Omega$）。
差异源于有限导线半径效应（$a=0.001\lambda$）：细线天线的输入电阻因欧姆损耗
和近场储能增加而升高。

---


| 编号 | 公式 | 说明 |
|------|------|------|
| (8-1) | $\mathbf{A}(\mathbf{r}) = \mu_0 \iint \mathbf{J}(\mathbf{r}') \frac{e^{-jkR}}{4\pi R} dS'$ | 矢量磁位 |
| (8-2) | $G(\mathbf{r}, \mathbf{r}') = \frac{e^{-jkR}}{4\pi R}$ | 自由空间 Green 函数 |
| (8-3) | $\hat{\mathbf{n}} \times \mathbf{E}^{\text{inc}} = \hat{\mathbf{n}} \times [j\omega\mathbf{A} + \frac{j}{\omega\mu_0\epsilon_0} \nabla\nabla\cdot\mathbf{A}]$ | EFIE |
| (8-4) | $\mathbf{J}_s = \hat{\mathbf{n}} \times \mathbf{H}^{\text{inc}} + \hat{\mathbf{n}} \times \iint \mathbf{J}_s \times \nabla' G \, dS'$ | MFIE |
| (8-5) | $E_z^{\text{inc}} = \frac{j\eta_0}{4\pi k} \int I(z') \left( \frac{\partial^2}{\partial z^2} + k^2 \right) \frac{e^{-jkR}}{R} dz'$ | **Pocklington 方程** |
| (8-6) | $\int I(z') \frac{e^{-jkR}}{4\pi R} dz' = C_1\cos(kz) + C_2\sin(kz) - \frac{jV_0}{2\eta_0}\sin(k|z|)$ | **Hallen 方程** |
| (8-7) | $\mathbf{Z}\mathbf{I} = \mathbf{V}$ | MoM 矩阵方程 |
| (8-8) | $Z_{mn} = \int\int f_m(z) f_n(z') \frac{e^{-jkR}}{4\pi R} dz' dz$ | Hallen 点匹配阻抗 |
| (8-9) | $Z_{mn} = \frac{j\eta_0}{4\pi k} \iint [k^2 f_m f_n - f_m' f_n'] \frac{e^{-jkR}}{R} dz' dz$ | Pocklington Galerkin 阻抗 |
| (8-10) | $E_\theta = j\eta_0 \frac{e^{-jkr}}{2\lambda r} \sin\theta \int I(z') e^{jkz'\cos\theta} dz'$ | 远场辐射公式 |

---


1. Balanis, C. A., *Antenna Theory: Analysis and Design*, 4th Ed., Wiley, 2016, Chapter 8.
2. Harrington, R. F., *Field Computation by Moment Methods*, Wiley, 1968.
3. Harrington, R. F., "Matrix methods for field problems," *Proc. IEEE*, vol. 55, no. 2, pp. 136-149, 1967.
4. Pocklington, H. C., "Electrical oscillations in wires," *Cambridge Phil. Soc. Proc.*, vol. 9, pp. 324-332, 1897.
5. Hallen, E., "Theoretical investigations into the transmitting and receiving qualities of antennae," *Nova Acta Reg. Soc. Sci. Upsaliensis*, ser. IV, vol. 11, no. 4, 1938.
6. Wallace, J. L. and Jensen, M. A., "A practical guide to the numerical solution of integral equations for thin wire antennas," *IEEE AP Magazine*, 2020.

---

*Last updated: 2026-04-30*
