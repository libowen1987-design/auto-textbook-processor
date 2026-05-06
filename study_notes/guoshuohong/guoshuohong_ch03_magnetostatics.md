# 第三章 静磁场

## §3.1 矢势及其微分方程

### 磁矢势 (Vector Potential)

静磁场的基本方程：

$$
\nabla \cdot \boldsymbol{B} = 0, \quad \nabla \times \boldsymbol{B} = \mu_0 \boldsymbol{J}
$$

由于 $\nabla \cdot \boldsymbol{B} = 0$，可引入**矢势 $\boldsymbol{A}$**：

$$
\boldsymbol{B} = \nabla \times \boldsymbol{A}
$$

$\boldsymbol{A}$ 并非唯一确定——规范自由度：$\boldsymbol{A}' = \boldsymbol{A} + \nabla \psi$ 给出相同 $\boldsymbol{B}$。

### 库仑规范 (Coulomb Gauge)

附加条件 $\nabla \cdot \boldsymbol{A} = 0$，使矢势唯一确定。

代入安培定律：

$$
\nabla \times (\nabla \times \boldsymbol{A}) = \mu_0 \boldsymbol{J}
$$

利用矢量恒等式 $\nabla \times (\nabla \times \boldsymbol{A}) = \nabla(\nabla\cdot\boldsymbol{A}) - \nabla^2\boldsymbol{A}$，在库仑规范下：

$$
\nabla^2 \boldsymbol{A} = -\mu_0 \boldsymbol{J}
$$

这是**泊松方程**，每个笛卡尔分量独立满足：

$$
\nabla^2 A_i = -\mu_0 J_i
$$

### 解的形式

类比静电势，矢势解为：

$$
\boldsymbol{A}(\boldsymbol{x}) = \frac{\mu_0}{4\pi} \int \frac{\boldsymbol{J}(\boldsymbol{x}')}{|\boldsymbol{x} - \boldsymbol{x}'|} \, dV'
$$

对于线电流（细导线）：

$$
\boldsymbol{A}(\boldsymbol{x}) = \frac{\mu_0 I}{4\pi} \oint \frac{d\boldsymbol{l}'}{|\boldsymbol{x} - \boldsymbol{x}'|}
$$

由此导出**毕奥-萨伐尔定律**：

$$
\boldsymbol{B}(\boldsymbol{x}) = \frac{\mu_0}{4\pi} \int \frac{\boldsymbol{J}(\boldsymbol{x}') \times (\boldsymbol{x} - \boldsymbol{x}')}{|\boldsymbol{x} - \boldsymbol{x}'|^3} \, dV'
$$

对于线电流：

$$
\boldsymbol{B}(\boldsymbol{x}) = \frac{\mu_0 I}{4\pi} \oint \frac{d\boldsymbol{l}' \times (\boldsymbol{x} - \boldsymbol{x}')}{|\boldsymbol{x} - \boldsymbol{x}'|^3}
$$

---

## §3.2 磁标势 (Magnetic Scalar Potential)

### 适用条件

在 $\boldsymbol{J} = 0$ 的区域，$\nabla \times \boldsymbol{B} = 0$，可引入**磁标势 $\varphi_m$**：

$$
\boldsymbol{B} = -\mu_0 \nabla \varphi_m \qquad (\text{或 } \boldsymbol{H} = -\nabla \varphi_m)
$$

### 磁标势的方程

由 $\nabla \cdot \boldsymbol{B} = 0$ 得：

$$
\nabla^2 \varphi_m = 0
$$

即**拉普拉斯方程**。边界条件：

1. 法向分量连续：$(\boldsymbol{B}_2 - \boldsymbol{B}_1) \cdot \boldsymbol{n} = 0$ → $\mu_2 \frac{\partial \varphi_{m2}}{\partial n} = \mu_1 \frac{\partial \varphi_{m1}}{\partial n}$
2. 切向分量连续：$(\boldsymbol{H}_2 - \boldsymbol{H}_1) \times \boldsymbol{n} = 0$ → $\varphi_{m2} = \varphi_{m1}$

### 与静电势的类比

| 静电势 | 磁标势 |
|--------|--------|
| $\boldsymbol{E} = -\nabla \varphi$ | $\boldsymbol{H} = -\nabla \varphi_m$ |
| $\nabla^2 \varphi = -\rho/\varepsilon_0$ | $\nabla^2 \varphi_m = 0$（无源区域） |
| 边界：$\varphi$ 连续，$\varepsilon \partial \varphi/\partial n$ 连续 | 边界：$\varphi_m$ 连续，$\mu \partial \varphi_m/\partial n$ 连续 |

### 局限性

磁标势仅适用于**无电流区域**。若存在电流，需切割区域或使用多值标势（类似磁荷观点）。

### 磁荷观点

引入等效磁荷密度 $\rho_m = -\mu_0 \nabla \cdot \boldsymbol{M}$ 和面磁荷密度 $\sigma_m = \mu_0 \boldsymbol{M} \cdot \boldsymbol{n}$，则：

$$
\varphi_m(\boldsymbol{x}) = \frac{1}{4\pi\mu_0} \int \frac{\rho_m(\boldsymbol{x}')}{|\boldsymbol{x} - \boldsymbol{x}'|} dV' + \frac{1}{4\pi\mu_0} \oint \frac{\sigma_m(\boldsymbol{x}')}{|\boldsymbol{x} - \boldsymbol{x}'|} dS'
$$

---

## §3.3 磁多极矩 (Magnetic Multipole Moments)

### 矢势的多极展开

对于电流分布 $\boldsymbol{J}(\boldsymbol{x}')$，在远场 $|\boldsymbol{x}| \gg |\boldsymbol{x}'|$ 展开：

$$
\frac{1}{|\boldsymbol{x} - \boldsymbol{x}'|} = \frac{1}{r} + \frac{\boldsymbol{x} \cdot \boldsymbol{x}'}{r^3} + \cdots
$$

矢势展开：

$$
\boldsymbol{A}(\boldsymbol{x}) = \frac{\mu_0}{4\pi} \left[ \frac{1}{r} \int \boldsymbol{J}(\boldsymbol{x}') dV' + \frac{1}{r^3} \int (\boldsymbol{x} \cdot \boldsymbol{x}') \boldsymbol{J}(\boldsymbol{x}') dV' + \cdots \right]
$$

### 磁单极矩 (Monopole)

第一项（磁单极）为零，因为稳恒电流无源：

$$
\int \boldsymbol{J}(\boldsymbol{x}') dV' = 0
$$

这与无磁单极的事实一致（$\nabla \cdot \boldsymbol{B} = 0$）。

### 磁偶极矩 (Magnetic Dipole Moment)

第二项给出主导贡献。定义**磁偶极矩**：

$$
\boldsymbol{m} = \frac{1}{2} \int \boldsymbol{x}' \times \boldsymbol{J}(\boldsymbol{x}') \, dV'
$$

对于线电流回路：

$$
\boldsymbol{m} = I \iint_S d\boldsymbol{S}' = I \boldsymbol{S}
$$

其中 $\boldsymbol{S}$ 是以回路为边界的任意曲面面积矢量（方向由右手定则确定）。

### 偶极矢势

$$
\boldsymbol{A}_{\text{dip}}(\boldsymbol{x}) = \frac{\mu_0}{4\pi} \frac{\boldsymbol{m} \times \boldsymbol{x}}{r^3}
$$

### 偶极磁场

取旋度得偶极磁场：

$$
\boldsymbol{B}_{\text{dip}}(\boldsymbol{x}) = \nabla \times \boldsymbol{A}_{\text{dip}} = \frac{\mu_0}{4\pi} \left[ \frac{3(\boldsymbol{m} \cdot \boldsymbol{r})\boldsymbol{r}}{r^5} - \frac{\boldsymbol{m}}{r^3} \right]
$$

其中 $\boldsymbol{r} = \boldsymbol{x}$（源在原点）。

### 与电偶极场的类比

| 电偶极 | 磁偶极 |
|--------|--------|
| $\boldsymbol{p}$ | $\boldsymbol{m}$ |
| $\phi = \frac{1}{4\pi\varepsilon_0} \frac{\boldsymbol{p} \cdot \boldsymbol{x}}{r^3}$ | $\boldsymbol{A} = \frac{\mu_0}{4\pi} \frac{\boldsymbol{m} \times \boldsymbol{x}}{r^3}$ |
| $\boldsymbol{E} = \frac{1}{4\pi\varepsilon_0} \left[ \frac{3(\boldsymbol{p}\cdot\boldsymbol{r})\boldsymbol{r}}{r^5} - \frac{\boldsymbol{p}}{r^3} \right]$ | $\boldsymbol{B} = \frac{\mu_0}{4\pi} \left[ \frac{3(\boldsymbol{m}\cdot\boldsymbol{r})\boldsymbol{r}}{r^5} - \frac{\boldsymbol{m}}{r^3} \right]$ |

### 磁四极矩 (Magnetic Quadrupole)

展开的第三项。更复杂的电流分布（如两组反向电流环）可能有显著的四极贡献。实际应用中，磁偶极矩通常是主导项。

---

## §3.4 阿哈罗诺夫-玻姆效应 (Aharonov-Bohm Effect)

### 经典预期

在经典电动力学中，电子在 $\boldsymbol{B} = 0$ 的区域运动不受磁场影响。即使螺线管内有磁通，只要电子路径在 $\boldsymbol{B}=0$ 的区域，经典理论预言无物理效应。

### 量子力学预言 (AB效应)

Aharonov和Bohm (1959) 指出：在量子力学中，即使 $\boldsymbol{B} = 0$，**矢势 $\boldsymbol{A}$** 仍对电子波函数有可观测的相位影响。

电子波函数在矢势中的相位因子：

$$
\psi(\boldsymbol{x}) = \psi_0(\boldsymbol{x}) \exp\left( \frac{i e}{\hbar} \int_{\text{path}} \boldsymbol{A} \cdot d\boldsymbol{l} \right)
$$

### 干涉实验

考虑电子双缝干涉实验，两束电子从源到屏的路径包围一个无限长螺线管（内部有磁通 $\Phi$）：

两路径的相位差：

$$
\Delta \varphi = \frac{e}{\hbar} \left( \int_{P_1} \boldsymbol{A} \cdot d\boldsymbol{l} - \int_{P_2} \boldsymbol{A} \cdot d\boldsymbol{l} \right)
= \frac{e}{\hbar} \oint \boldsymbol{A} \cdot d\boldsymbol{l}
= \frac{e}{\hbar} \iint_S (\nabla \times \boldsymbol{A}) \cdot d\boldsymbol{S}
= \frac{e}{\hbar} \iint_S \boldsymbol{B} \cdot d\boldsymbol{S}
= \frac{e \Phi}{\hbar}
$$

其中 $\Phi$ 为螺线管内的磁通量。

### 物理意义

1. **$\boldsymbol{A}$ 的物理实在性**：AB效应表明矢势 $\boldsymbol{A}$ 在量子力学中是物理实在的（不仅仅是数学工具），即使在 $\boldsymbol{B}=0$ 的区域，$\boldsymbol{A}$ 仍影响量子系统。
2. **规范不变性**：相位差 $\Delta \varphi = e\Phi/\hbar$ 是规范不变的——它只依赖于闭合路径包围的磁通量。
3. **拓扑效应**：AB效应是**拓扑效应**——只依赖于路径包围的磁通，而不依赖于路径的具体形状。

### 实验验证

- Chambers (1960) 首次实验验证
- Tonomura 等人 (1986) 用超导磁屏蔽消除了杂散磁场，进行了决定性实验

### 磁通量子化

AB效应也导致超导环中的磁通量子化：

$$
\Phi = n \frac{h}{e} = n \Phi_0
$$

其中 $\Phi_0 = h/e$ 为磁通量子（超导中为 $h/2e$，考虑库珀对）。

### 推广：Berry相位

AB效应是 Berry 相位的一个早期例子——系统参数绝热循环产生的几何相位。

---

## 关键公式总结

| 物理量 | 公式 | 条件 |
|--------|------|------|
| 矢势定义 | $\boldsymbol{B} = \nabla \times \boldsymbol{A}$ | 一般 |
| 库仑规范 | $\nabla \cdot \boldsymbol{A} = 0$ | 规范条件 |
| 矢势泊松方程 | $\nabla^2 \boldsymbol{A} = -\mu_0 \boldsymbol{J}$ | 库仑规范 |
| 矢势解（体电流） | $\boldsymbol{A} = \frac{\mu_0}{4\pi} \int \frac{\boldsymbol{J}}{R} dV'$ | 库仑规范 |
| 毕奥-萨伐尔定律 | $\boldsymbol{B} = \frac{\mu_0}{4\pi} \int \frac{\boldsymbol{J} \times \boldsymbol{R}}{R^3} dV'$ | 一般 |
| 磁标势 | $\boldsymbol{H} = -\nabla \varphi_m$ | $\boldsymbol{J} = 0$ 区域 |
| 磁偶极矩 | $\boldsymbol{m} = \frac{1}{2} \int \boldsymbol{x}' \times \boldsymbol{J} dV'$ | 一般电流分布 |
| 偶极矢势 | $\boldsymbol{A}_{\text{dip}} = \frac{\mu_0}{4\pi} \frac{\boldsymbol{m} \times \boldsymbol{r}}{r^3}$ | 远场近似 |
| 偶极磁场 | $\boldsymbol{B}_{\text{dip}} = \frac{\mu_0}{4\pi} \left[ \frac{3(\boldsymbol{m}\cdot\boldsymbol{r})\boldsymbol{r}}{r^5} - \frac{\boldsymbol{m}}{r^3} \right]$ | 远场近似 |
| AB相位差 | $\Delta \varphi = \frac{e\Phi}{\hbar}$ | 量子力学 |
