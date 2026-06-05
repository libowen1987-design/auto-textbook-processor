# Chapter 3: Radiation Integrals and Auxiliary Potential Functions
# 第3章：辐射积分与辅助势函数

> **核心思想**：直接求解 Maxwell 方程组得到辐射场需要解 6 个耦合标量方程（3 个 E 分量 + 3 个 H 分量）。通过引入辅助势函数（矢量磁位 **A**、矢量电位 **F**），将问题解耦为两个独立的 Helmholtz 方程，再通过微分得到场。

---


假设时谐因子 $e^{j\omega t}$，Maxwell 方程组化为：

| 方程 | 积分形式 | 微分形式 |
|------|----------|----------|
| Faraday 定律 | $\oint_C \mathbf{E} \cdot d\boldsymbol{\ell} = -j\omega \iint_S \mathbf{B}\cdot d\mathbf{s} - \iint_S \mathbf{M}\cdot d\mathbf{s}$ | $\nabla \times \mathbf{E} = -j\omega\mu\mathbf{H} - \mathbf{M}$ |
| Ampère 定律 | $\oint_C \mathbf{H} \cdot d\boldsymbol{\ell} = j\omega \iint_S \mathbf{D}\cdot d\mathbf{s} + \iint_S \mathbf{J}\cdot d\mathbf{s}$ | $\nabla \times \mathbf{H} = j\omega\varepsilon\mathbf{E} + \mathbf{J}$ |
| Gauss 定律（电） | $\oiint_S \mathbf{D}\cdot d\mathbf{s} = Q_e$ | $\nabla \cdot \mathbf{D} = \rho_e$ |
| Gauss 定律（磁） | $\oiint_S \mathbf{B}\cdot d\mathbf{s} = Q_m$ | $\nabla \cdot \mathbf{B} = \rho_m$ |

其中 **J** 与 **M** 分别是电流密度和**磁流密度**（人造等效源，用于口径/缝隙天线分析）。

本构关系（各向同性介质）：
$$
\mathbf{D} = \varepsilon \mathbf{E}, \quad \mathbf{B} = \mu \mathbf{H}
$$

---


直接求解 Maxwell 方程组：

$$
\nabla \times \mathbf{E} = -j\omega\mu\mathbf{H} - \mathbf{M}, \quad
\nabla \times \mathbf{H} = j\omega\varepsilon\mathbf{E} + \mathbf{J}
$$

→ 6 个耦合 PDE，求解极复杂。

**策略**：引入矢量位，将耦合方程降阶为独立的标量/矢量 Helmholtz 方程。

---


### 3.1 定义

由于 $\nabla \cdot \mathbf{B} = 0$，可定义矢量磁位 **A**：

$$
\boxed{\mathbf{B} = \nabla \times \mathbf{A}}
$$

代入 Faraday 定律：

$$
\nabla \times (\mathbf{E} + j\omega\mathbf{A}) = -\mathbf{M}
$$

对于纯电流源 ($\mathbf{M}=0$)，括号内为无旋场，可写为标量电位 $\Phi_e$ 的梯度：

$$
\mathbf{E} = -j\omega\mathbf{A} - \nabla\Phi_e
$$

### 3.2 Lorenz 规范

$\mathbf{A}$ 的定义有规范自由度。选择 **Lorenz 规范**：

$$
\boxed{\nabla \cdot \mathbf{A} = -j\omega\mu\varepsilon\Phi_e}
$$

代入 Ampère 定律，得到 Helmholtz 方程：

$$
\boxed{\nabla^2\mathbf{A} + k^2\mathbf{A} = -\mu\mathbf{J}}
$$

其中 $k = \omega\sqrt{\mu\varepsilon}$ 是波数。

### 3.3 解（自由空间格林函数）

方程的解是 Helmholtz 方程的基本解与源的卷积：

$$
\boxed{\mathbf{A}(\mathbf{r}) = \mu \iiint_V \mathbf{J}(\mathbf{r}') G(\mathbf{r},\mathbf{r}') \, dv'}
$$

其中自由空间格林函数：

$$
G(\mathbf{r},\mathbf{r}') = \frac{e^{-jk|\mathbf{r}-\mathbf{r}'|}}{4\pi|\mathbf{r}-\mathbf{r}'|}
$$

**物理意义**：$G(\mathbf{r},\mathbf{r}')$ 是点源产生的球面波。**A** 是源区所有电流元贡献的叠加。

---


### 4.1 对偶性

通过**对偶性原理**，磁流 **M** 产生矢量电位 **F**：

- $\mathbf{J} \leftrightarrow \mathbf{M}$
- $\mathbf{E} \leftrightarrow \mathbf{H}$
- $\varepsilon \leftrightarrow \mu$

只要把电流源的全部公式做对偶替换即得磁流源公式。

### 4.2 定义

由于 $\nabla \cdot \mathbf{D} = \rho_e$，对磁流源问题更自然地：

$$
\boxed{\mathbf{D} = -\nabla \times \mathbf{F}}, \quad \mathbf{B} = -\mu\varepsilon\nabla\Phi_m - j\omega\mu\varepsilon\mathbf{F}
$$

### 4.3 解

$$
\boxed{\mathbf{F}(\mathbf{r}) = \varepsilon \iiint_V \mathbf{M}(\mathbf{r}') G(\mathbf{r},\mathbf{r}') \, dv'}
$$

---


**电流源 (**$\mathbf{J}$**) 通过 **$\mathbf{A}$** 贡献：**

$$
\mathbf{E}^A = -j\omega\mathbf{A} - \frac{j}{\omega\mu\varepsilon}\nabla(\nabla\cdot\mathbf{A}) = -j\omega\mathbf{A} - j\frac{1}{\omega\mu\varepsilon}\nabla(\nabla\cdot\mathbf{A})
$$

$$
\mathbf{H}^A = \frac{1}{\mu}\nabla \times \mathbf{A}
$$

**磁流源 (**$\mathbf{M}$**) 通过 **$\mathbf{F}$** 贡献：**

$$
\mathbf{H}^F = -j\omega\mathbf{F} - \frac{j}{\omega\mu\varepsilon}\nabla(\nabla\cdot\mathbf{F})
$$

$$
\mathbf{E}^F = -\frac{1}{\varepsilon}\nabla \times \mathbf{F}
$$

**总场：**

$$
\mathbf{E} = \mathbf{E}^A + \mathbf{E}^F = -j\omega\mathbf{A} - j\frac{1}{\omega\mu\varepsilon}\nabla(\nabla\cdot\mathbf{A}) - \frac{1}{\varepsilon}\nabla\times\mathbf{F}
$$

$$
\mathbf{H} = \mathbf{H}^A + \mathbf{H}^F = \frac{1}{\mu}\nabla\times\mathbf{A} - j\omega\mathbf{F} - j\frac{1}{\omega\mu\varepsilon}\nabla(\nabla\cdot\mathbf{F})
$$

---


在实际天线问题中，我们通常关心**远区辐射场**（$r \gg \lambda, \; r \gg D^2/\lambda$）。

### 6.1 三个近似条件

在远区，格林函数的梯度/旋度可大幅简化：

**条件 1：幅度近似**
$$
\frac{1}{|\mathbf{r} - \mathbf{r}'|} \approx \frac{1}{r} \quad (\text{当 } r \gg r')
$$

**条件 2：相位近似**
$$
e^{-jk|\mathbf{r} - \mathbf{r}'|} \approx e^{-jkr} e^{jk\mathbf{r}'\cdot\hat{\mathbf{r}}} \quad (\text{当 } r \gg r')
$$

> 相位对 $\mathbf{r}'$ 敏感——这是形成阵列方向图的基础。
> 泰勒展开：$|\mathbf{r} - \mathbf{r}'| \approx r - \hat{\mathbf{r}}\cdot\mathbf{r}' + \cdots$

**条件 3：$\nabla$ 算符作用于 $\mathbf{A}$**

在远区，$\nabla$ 可近似为 $-jk\hat{\mathbf{r}}$（球面波的径向梯度）：

$$
\nabla \cdot \mathbf{A} \approx -jk\hat{\mathbf{r}} \cdot \mathbf{A}
$$

$$
\nabla \times \mathbf{A} \approx -jk\hat{\mathbf{r}} \times \mathbf{A}
$$

### 6.2 远区辐射场公式

利用上述近似，从 $\mathbf{E}^A = -j\omega\mathbf{A} - j\frac{1}{\omega\mu\varepsilon}\nabla(\nabla\cdot\mathbf{A})$ 可得：

$$
\mathbf{E}^A \approx -j\omega\left[\mathbf{A} - (\hat{\mathbf{r}}\cdot\mathbf{A})\hat{\mathbf{r}}\right] = -j\omega\mathbf{A}_\perp
$$

其中 $\mathbf{A}_\perp$ 是 **A** 的横向分量（垂直于 $\hat{\mathbf{r}}$）。

在球坐标系中：

$$
\boxed{E_r \approx 0}
$$

$$
\boxed{E_\theta \approx -j\omega(A_\theta + \eta F_\phi)}
$$

$$
\boxed{E_\phi \approx -j\omega(A_\phi - \eta F_\theta)}
$$

$$
\boxed{H_\theta \approx -\frac{E_\phi}{\eta}}
$$

$$
\boxed{H_\phi \approx \frac{E_\theta}{\eta}}
$$

其中 $\eta = \sqrt{\mu/\varepsilon}$ 是自由空间波阻抗。

**物理意义**：
- 远场是 TEM 波（$E_r \approx 0$，$\mathbf{E}$ 与 $\mathbf{H}$ 垂直且同相）
- 电场与磁场通过 $\eta$ 联系
- 只需计算 **A** 和 **F** 的 $\theta,\phi$ 分量即可得到完整远场

---


### 7.1 等效原理（Surface Equivalence Principle）

口径天线（喇叭、反射面）的分析方法：
1. 在口径面上做等效闭合面
2. 由场切向分量定义等效面电流和面磁流
3. 用这些等效源计算远场

### 7.2 表面等效源

$$
\boxed{\mathbf{J}_s = \hat{\mathbf{n}} \times \mathbf{H}} \quad \text{(等效面电流)}
$$

$$
\boxed{\mathbf{M}_s = -\hat{\mathbf{n}} \times \mathbf{E}} \quad \text{(等效面磁流)}
$$

其中 $\hat{\mathbf{n}}$ 是口径面的外法向。

### 7.3 口径→远场（标量近似）

对于大口径（$D \gg \lambda$），远场近似为口径场分布的傅里叶变换：

$$
\mathbf{E}(\mathbf{r}) \approx \frac{je^{-jkr}}{2\pi r} (\hat{\theta} E_\theta + \hat{\phi} E_\phi)
$$

其中：

$$
E_\theta \approx \frac{jk}{2\pi r} e^{-jkr} (1 + \cos\theta) \iint_S E_a(x',y') e^{jk(x'\sin\theta\cos\phi + y'\sin\theta\sin\phi)} dx' dy'
$$

$E_a(x',y')$ 是口径面上的电场切向分量。

**这是口径天线分析的核心——口径场的傅里叶变换关系。**

---


如果已知一种源的解，通过对偶替换可直接得到对偶源的解。

| 电流源量 | ↔ | 磁流源量 |
|---------|---|---------|
| $\mathbf{E}$ | ↔ | $\mathbf{H}$ |
| $\mathbf{H}$ | ↔ | $-\mathbf{E}$ |
| $\mathbf{J}$ | ↔ | $\mathbf{M}$ |
| $\mathbf{A}$ | ↔ | $\mathbf{F}$ |
| $\varepsilon$ | ↔ | $\mu$ |
| $\eta = \sqrt{\mu/\varepsilon}$ | ↔ | $1/\eta$ |
| $k = \omega\sqrt{\mu\varepsilon}$ | ↔ | $k$ |

**应用实例**：

| 特性 | 电偶极子 ($I dl$) | 磁偶极子 ($I_m dl$ / 小环) |
|------|-------------------|---------------------------|
| E 面方向图 | $\sin\theta$ | $1$（环平面内） |
| H 面方向图 | $1$ | $\sin\theta$ |
| E 面极化 | $\theta$ | $\phi$ |
| 辐射电阻 | $R_r = 80\pi^2(dl/\lambda)^2$ | $R_r = 20\pi^2(C/\lambda)^4$ |

---


Babinet 原理将光学中的互补屏概念推广到天线：

> **互补结构**：在一个无限导电平面上，开槽天线（缝隙）与其互补结构（金属条带）的辐射场满足：
>
> $$
> \mathbf{E}_{\text{slot}} + \mathbf{E}_{\text{strip}} = \mathbf{E}_{\text{inc}}
> $$
>
> 更实用形式：缝隙天线的输入阻抗与互补偶极子的阻抗之积：
>
> $$
> Z_{\text{slot}} Z_{\text{dipole}} = \frac{\eta^2}{4}
> $$

这意味着缝隙天线的阻抗特性可以通过其互补偶极子推断。

---


| 物理量 | 公式 | 单位 |
|--------|------|------|
| 矢量磁位 | $\mathbf{A} = \mu \iiint \mathbf{J} G dv$ | Wb/m |
| 矢量电位 | $\mathbf{F} = \varepsilon \iiint \mathbf{M} G dv$ | C/m |
| 格林函数 | $G = e^{-jkR}/(4\pi R)$ | 1/m |
| Lorenz 规范 | $\nabla \cdot \mathbf{A} = -j\omega\mu\varepsilon\Phi_e$ | — |
| 远场 E | $\mathbf{E} \approx -j\omega[\mathbf{A} - (\hat{\mathbf{r}}\cdot\mathbf{A})\hat{\mathbf{r}} + \eta\hat{\mathbf{r}}\times\mathbf{F}]$ | V/m |
| 远场 H | $\mathbf{H} \approx \frac{1}{\eta}\hat{\mathbf{r}}\times\mathbf{E}$ | A/m |
| 口径→远场 | $\mathbf{E}(\theta,\phi) \propto \mathcal{F}\{E_a(x,y)\}$ | V/m |
| 对偶性 | $\mathbf{E} \leftrightarrow \mathbf{H}, \mathbf{J} \leftrightarrow \mathbf{M}, \varepsilon \leftrightarrow \mu$ | — |

---


### 11.1 矢量位计算

在数值计算中，**A** 和 **F** 的计算简化为：
1. 将源区离散为小体积元 $dv'$
2. 将格林函数的幅度/相位近似代入
3. 对每对 $(\mathbf{r}, \mathbf{r}')$ 求和

### 11.2 口径→远场

对于矩形口径（$a \times b$），口径场为均匀分布时：

$$
E_\theta \propto \frac{\sin\left(\frac{k a}{2}\sin\theta\cos\phi\right)}{\frac{k a}{2}\sin\theta\cos\phi} \cdot \frac{\sin\left(\frac{k b}{2}\sin\theta\sin\phi\right)}{\frac{k b}{2}\sin\theta\sin\phi}
$$

这是二维 sinc 函数——口径越大，波束越窄。

### 11.3 参考

- Balanis, C.A. "Antenna Theory: Analysis and Design", 4th Ed., Ch. 3
- Harrington, R.F. "Time-Harmonic Electromagnetic Fields", Ch. 3
- IEEE Std 145-2013 (天线术语标准)
