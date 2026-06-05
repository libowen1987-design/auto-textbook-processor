---
chapter: 6
title: Fields and Waves in Cylindrical Coordinates
source: Jin, Theory and Computation of Electromagnetic Fields, 2nd Ed., pp. 261–348
sections: 9
examples: 5
---

# Chapter 6: Fields and Waves in Cylindrical Coordinates | 第六章：柱坐标中的场与波

> **中英双语版**

## 6.1 Solution of Wave Equation | 波动方程的解

The Helmholtz equation $\nabla^2\psi + k^2\psi = 0$ in cylindrical coordinates / 柱坐标中的亥姆霍兹方程：

$$
\frac{\partial^2\psi}{\partial\rho^2} + \frac{1}{\rho}\frac{\partial\psi}{\partial\rho}
+ \frac{1}{\rho^2}\frac{\partial^2\psi}{\partial\phi^2}
+ \frac{\partial^2\psi}{\partial z^2} + k^2\psi = 0 \tag{6.1.1}
$$

### 6.1.1 Solution by Separation of Variables | 分离变量法求解

Assume $\psi(\rho,\phi,z) = P(\rho)\Phi(\phi)Z(z)$ / 设 $\psi(\rho,\phi,z) = P(\rho)\Phi(\phi)Z(z)$。分离给出：

$$
Z(z) = A(h)e^{-jhz} + B(h)e^{jhz} \tag{6.1.5}
$$
$$
\Phi(\phi) = c_m\cos m\phi + d_m\sin m\phi \tag{6.1.11}
$$

The radial equation is Bessel's equation / 径向方程是贝塞尔方程：

$$
\rho^2\frac{d^2P}{d\rho^2} + \rho\frac{dP}{d\rho} + [(k_\rho\rho)^2 - m^2]P = 0 \tag{6.1.10}
$$

where $k_\rho^2 = k^2 - h^2$ / 其中 $k_\rho^2 = k^2 - h^2$。General solution / 通解：

$$
P(\rho) = a_m J_m(k_\rho\rho) + b_m Y_m(k_\rho\rho) \tag{6.1.12}
$$

Properties / 性质：$J_m(k_\rho\rho) \to$ 有限当 $k_\rho\rho\to 0$，$Y_m(k_\rho\rho) \to -\infty$ 当 $k_\rho\rho\to 0$。

### 6.1.2 Cylindrical Wave Functions | 柱波函数

Hankel functions for outward/inward propagating waves / 用于向外/向内传播波的汉克尔函数：

$$
H_m^{(1)}(k_\rho\rho) = J_m(k_\rho\rho) + jY_m(k_\rho\rho) \tag{6.1.17}
$$
$$
H_m^{(2)}(k_\rho\rho) = J_m(k_\rho\rho) - jY_m(k_\rho\rho) \tag{6.1.18}
$$

Asymptotic forms (large argument) / 渐近形式（大自变量）：

$$
H_m^{(2)}(k_\rho\rho) \approx \sqrt{\frac{2}{\pi k_\rho\rho}}\; e^{-j(k_\rho\rho - m\pi/2 - \pi/4)},\quad k_\rho\rho\gg 1 \tag{6.1.22}
$$

$H_m^{(2)}$ 代表沿 $+\rho$ 方向传播的波（出射波）。

**Example 6.1 / 例6.1** (p. 265): 柱坐标中拉普拉斯方程 $\nabla^2\psi = 0$ 的通解。由于 $k=0$，径向方程变为修正贝塞尔方程，解为 $I_m(h\rho)$ 和 $K_m(h\rho)$。对于二维（$\partial/\partial z = 0$），解为 $\rho^m$ 和 $\rho^{-m}$。

## 6.2 Circular and Coaxial Waveguides and Cavities | 圆波导、同轴波导和圆柱腔

### 6.2.1 Circular Waveguide | 圆波导

**TM modes / TM模** (Eqs. (6.2.11)–(6.2.17)):

$$
E_z = E_0 J_m(k_\rho\rho) \begin{Bmatrix}\sin m\phi \\ \cos m\phi\end{Bmatrix} e^{-jk_z z}
$$

Boundary condition $E_z|_{\rho=a}=0 \Rightarrow J_m(k_\rho a) = 0$。Roots / 根：$\chi_{mn}$ (Table 6.1)。

Cutoff / 截止：$k_{c,mn}^{\text{TM}} = \chi_{mn}/a$，$f_{c,mn}^{\text{TM}} = \chi_{mn}/(2\pi a\sqrt{\mu\epsilon})$。 (6.2.13)

Propagation constant / 传播常数：$k_{z,mn}^{\text{TM}} = \sqrt{k^2 - (\chi_{mn}/a)^2}$。 (6.2.12)

Other TM field components / 其他TM场分量：

$$
E_\rho = -E_0\frac{jk_z}{k_\rho} J_m'(k_\rho\rho) \begin{Bmatrix}\sin m\phi \\ \cos m\phi\end{Bmatrix} e^{-jk_z z} \tag{6.2.14}
$$
$$
E_\phi = \mp E_0\frac{jm k_z}{\rho k_\rho^2} J_m(k_\rho\rho) \begin{Bmatrix}\cos m\phi \\ \sin m\phi\end{Bmatrix} e^{-jk_z z} \tag{6.2.15}
$$
$$
H_\rho = \pm E_0\frac{jm\omega\epsilon}{\rho k_\rho^2} J_m(k_\rho\rho) \begin{Bmatrix}\cos m\phi \\ \sin m\phi\end{Bmatrix} e^{-jk_z z} \tag{6.2.16}
$$
$$
H_\phi = -E_0\frac{j\omega\epsilon}{k_\rho} J_m'(k_\rho\rho) \begin{Bmatrix}\sin m\phi \\ \cos m\phi\end{Bmatrix} e^{-jk_z z} \tag{6.2.17}
$$

**TE modes / TE模** (Eqs. (6.2.18)–(6.2.24)):

$$
H_z = H_0 J_m(k_\rho\rho) \begin{Bmatrix}\sin m\phi \\ \cos m\phi\end{Bmatrix} e^{-jk_z z}
$$

Boundary condition $E_\phi|_{\rho=a}=0 \Rightarrow J_m'(k_\rho a) = 0$。Roots / 根：$\chi_{mn}'$ (Table 6.2)。

Cutoff / 截止：$k_{c,mn}^{\text{TE}} = \chi_{mn}'/a$，$f_{c,mn}^{\text{TE}} = \chi_{mn}'/(2\pi a\sqrt{\mu\epsilon})$。 (6.2.20)

**Dominant mode / 主模**: TE$_{11}$ ($\chi_{11}' = 1.841184$)。Cutoff $\lambda_{c,11}^{\text{TE}} = 3.4126a$。
First higher-order / 第一高阶：TM$_{01}$ ($\chi_{01}=2.404826$)。Cutoff $\lambda_{c,01}^{\text{TM}} = 2.6127a$。

| m | n=1 | n=2 | n=3 | n=4 |
|:-:|:---:|:---:|:---:|:---:|
| **Roots of $J_m(z)=0$ ($\chi_{mn}$, TM modes)** | | | | |
| 0 | 2.404826 | 5.520078 | 8.653728 | 11.79153 |
| 1 | 3.831706 | 7.015587 | 10.17347 | 13.32369 |
| 2 | 5.135622 | 8.417244 | 11.61984 | 14.79595 |
| **Roots of $J_m'(z)=0$ ($\chi_{mn}'$, TE modes)** | | | | |
| 0 | 3.831706 | 7.015587 | 10.17347 | 13.32369 |
| 1 | 1.841184 | 5.331443 | 9.536316 | 11.70600 |
| 2 | 3.054237 | 6.706133 | 9.969468 | 13.17037 |

**Example 6.2 / 例6.2** (p. 272): 微扰法求TE$_{11}$模的衰减常数：

$$
\alpha_{c,11}^{\text{TE}} = \frac{R_s}{\omega\mu k_{z,11} a^3} \frac{a^2 k_{z,11}^2 + \chi_{11}'^4}{\chi_{11}'^2 - 1}
$$

空气填充：$\alpha_{c,11}^{\text{TE}} = \frac{R_s}{a} \left[ \frac{3.765}{\sqrt{1-(\lambda/3.413a)^2}} + 2.654\sqrt{1-(\lambda/3.413a)^2} \right] \times 10^{-3}\ \text{Np/m}$。

### 6.2.2 Coaxial Waveguide | 同轴波导

Both Bessel J and Y functions needed (field includes $\rho=0$ region not) / 需要贝塞尔J和Y函数（场不包含 $\rho=0$ 区域）。Determinantal equations for TM modes / TM模的确定方程：

$$
J_m(k_\rho a) Y_m(k_\rho b) - Y_m(k_\rho a) J_m(k_\rho b) = 0 \tag{6.2.28}
$$

For TE modes / 对TE模：

$$
J_m'(k_\rho a) Y_m'(k_\rho b) - Y_m'(k_\rho a) J_m'(k_\rho b) = 0 \tag{6.2.32}
$$

**TEM mode / TEM模** ($k_\rho=0$): No cutoff / 无截止。Fields / 场：

$$
E_\rho = -C\sqrt{\mu/\epsilon}\,\frac{1}{\rho}e^{-jkz}, \quad H_\phi = -\frac{C}{\mu}\frac{1}{\rho}e^{-jkz} \tag{6.2.36}
$$

Characteristic impedance / 特性阻抗：

$$
Z_c = \frac{V(z)}{I(z)} = \frac{1}{2\pi}\sqrt{\frac{\mu}{\epsilon}}\ln\frac{b}{a} \tag{6.2.40}
$$

$Z_c \approx 50\ \Omega$ when $b/a = 2.3$, $Z_c \approx 75\ \Omega$ when $b/a = 3.5$ (air-filled / 空气填充)。

同轴电缆支持TEM模（无截止），因为双导体提供回流路径。

**Example 6.3 / 例6.3** (p. 275): TEM模的衰减常数：

Dielectric loss / 介质损耗：$\alpha_d \approx \frac{\pi\sqrt{\epsilon_r}}{\lambda_0}\tan\delta_e$ (Np/m)。

Conductor loss / 导体损耗：$\alpha_c^{\text{TEM}} = \frac{R_s}{2\eta\ln(b/a)}\left(\frac{1}{a} + \frac{1}{b}\right)$ (Np/m)。

### 6.2.3 Cylindrical Cavity | 圆柱腔

**TM$_{mnp}$ modes / TM$_{mnp}$ 模** in circular cavity of height $h$ / 高度为 $h$ 的圆柱腔中：

$$
E_z = E_0 J_m(k_\rho\rho) \begin{Bmatrix}\sin m\phi \\ \cos m\phi\end{Bmatrix} \cos\frac{p\pi z}{h} \tag{6.2.41}
$$

Resonant frequency / 谐振频率：

$$
\omega_{r,mnp}^{\text{TM}} = \frac{1}{\sqrt{\mu\epsilon}}\sqrt{\left(\frac{\chi_{mn}}{a}\right)^2 + \left(\frac{p\pi}{h}\right)^2} \tag{6.2.42}
$$

**TE$_{mnp}$ modes / TE$_{mnp}$ 模**:

$$
H_z = H_0 J_m(k_\rho\rho) \begin{Bmatrix}\sin m\phi \\ \cos m\phi\end{Bmatrix} \sin\frac{p\pi z}{h} \tag{6.2.43}
$$

Resonant frequency / 谐振频率：

$$
\omega_{r,mnp}^{\text{TE}} = \frac{1}{\sqrt{\mu\epsilon}}\sqrt{\left(\frac{\chi_{mn}'}{a}\right)^2 + \left(\frac{p\pi}{h}\right)^2} \tag{6.2.44}
$$

Dominant mode / 主模：TM$_{010}$ ($\omega_{r,010}^{\text{TM}} = 2.4048/(a\sqrt{\mu\epsilon})$) 或 TE$_{111}$。

**Example 6.4 / 例6.4** (p. 277): TE$_{111}$ 模的品质因数：

$$
Q_{c,111}^{\text{TE}} = \frac{\eta(\chi_{11}'^2 - 1)\left[\chi_{11}'^2 + (\pi a/h)^2\right]^{3/2}}{2R_s\left\{\frac{2\pi^2 a^3}{h^3}(\chi_{11}'^2 - 1) + \left[\chi_{11}'^4 + (\pi a/h)^2\right]\right\}}
$$

## 6.3 Circular Dielectric Waveguide (Optical Fiber) | 圆介质波导（光纤）

Two-layer model: core ($\epsilon_1$, radius $a$), cladding ($\epsilon_2$, $\epsilon_1 > \epsilon_2$) / 两层模型：纤芯（$\epsilon_1$，半径 $a$），包层（$\epsilon_2$，$\epsilon_1 > \epsilon_2$）。

**Hybrid modes / 混合模**: Both $E_z$ and $H_z$ present due to dielectric discontinuity / 由于介质不连续性，$E_z$ 和 $H_z$ 都存在。

In core ($\rho < a$) / 纤芯中：

$$
E_{1z} = A_1 J_m(k_{1\rho}\rho) \begin{Bmatrix}\sin m\phi \\ \cos m\phi\end{Bmatrix} e^{-jk_z z} \tag{6.3.1}
$$
$$
H_{1z} = B_1 J_m(k_{1\rho}\rho) \begin{Bmatrix}\cos m\phi \\ \sin m\phi\end{Bmatrix} e^{-jk_z z} \tag{6.3.2}
$$

In cladding ($\rho > a$) / 包层中：场使用 $K_m(\alpha_{2\rho}\rho)$ 指数衰减。

Characteristic equation for hybrid modes / 混合模的特征方程：

$$
\left[\frac{1}{u}\frac{J_m'(u)}{J_m(u)} + \frac{1}{v}\frac{K_m'(v)}{K_m(v)}\right]
\left[\frac{\epsilon_{r1}}{u}\frac{J_m'(u)}{J_m(u)} + \frac{\epsilon_{r2}}{v}\frac{K_m'(v)}{K_m(v)}\right]
= m^2\left(\frac{1}{u^2} + \frac{1}{v^2}\right)\left(\frac{\epsilon_{r1}}{u^2} + \frac{\epsilon_{r2}}{v^2}\right) \tag{6.3.35}
$$

其中 $u = k_{1\rho}a$, $v = \alpha_{2\rho}a$。

**Dominant mode / 主模**: HE$_{11}$ — no cutoff frequency / 无截止频率 ($k_{c,11}^{\text{HE}} = 0$)。

**Mode classification / 模式分类**: $+$ 号 → EH${}_{mn}$ (TE-like)，$-$ 号 → HE${}_{mn}$ (TM-like)。

For $m=0$, EH${}_{0n}$ = TE${}_{0n}$, HE${}_{0n}$ = TM${}_{0n}$。

Cutoffs / 截止：$k_{c,01}^{\text{TE/TM}} = 2.4048/(a\sqrt{\epsilon_{r1}-\epsilon_{r2}})$, $k_{c,11}^{\text{EH/HE}} = 3.8317/(a\sqrt{\epsilon_{r1}-\epsilon_{r2}})$。

光纤中HE$_{11}$模无截止——它是单模光纤的基模。

## 6.4 Wave Transformation and Scattering Analysis | 波变换与散射分析

### 6.4.1 Wave Transformation | 波变换

Plane wave → cylindrical wave expansion / 平面波→柱波展开：

$$
e^{-jkx} = \sum_{n=-\infty}^{\infty} j^{-n} J_n(k\rho) e^{jn\phi} \tag{6.4.6}
$$

### 6.4.2 Scattering by a Circular Conducting Cylinder | 圆形导体柱的散射

**TM polarization / TM极化**: $E_z^{\text{inc}} = E_0 e^{-jkx}$。

Incident / 入射：$E_z^{\text{inc}} = E_0\sum_{n=-\infty}^{\infty} j^{-n}J_n(k\rho)e^{jn\phi}$ \tag{6.4.8}

Scattered / 散射：$E_z^{\text{sc}} = -E_0\sum_{n=-\infty}^{\infty} j^{-n}\frac{J_n(ka)}{H_n^{(2)}(ka)} H_n^{(2)}(k\rho) e^{jn\phi}$ \tag{6.4.12}

**TE polarization / TE极化**: 类似，对汉克尔函数使用 $\partial/\partial n'$ 算子。

**Scattering width / 散射宽度**:

$$
\sigma_{2D}(\phi) = \lim_{\rho\to\infty} 2\pi\rho\frac{|E_z^{\text{sc}}|^2}{|E_z^{\text{inc}}|^2}
= \frac{2}{k}\left|\sum_{n=-\infty}^{\infty} a_n e^{jn\phi}\right|^2 \tag{6.4.21}
$$

### 6.4.3 Scattering by a Dielectric Cylinder | 介质柱的散射

For a dielectric cylinder ($\epsilon_d$, $\mu_0$), both internal and scattered fields are solved by matching boundary conditions at $\rho=a$ / 对介质柱，通过匹配 $\rho=a$ 处的边界条件求解内部场和散射场。Internal fields use $J_n(k_d\rho)$; scattered fields use $H_n^{(2)}(k_0\rho)$。展开系数由界面上 $E_z$ 和 $H_\phi$ (TM) 或 $H_z$ 和 $E_\phi$ (TE) 的连续性确定。

### 6.4.4 Multilayer Dielectric Cylinder | 多层介质柱

Extended to layered cylinders using transfer matrix approach / 使用传输矩阵法扩展到分层柱。

## 6.5 Radiation Problems in Cylindrical Coordinates | 柱坐标中的辐射问题

### 6.5.1 Line Current Radiation | 线电流辐射

Time-harmonic uniform line current $I$ at $\rho'$ / 在 $\rho'$ 处的时谐均匀线电流 $I$：

$$
E_z = -\frac{k^2 Z_0 I}{4} H_0^{(2)}(k|\boldsymbol{\rho} - \boldsymbol{\rho}'|) \tag{6.5.1}
$$

Far-field / 远场：$E_z^{\text{ff}} \to -\frac{k Z_0 I}{4}\sqrt{\frac{2j}{\pi k\rho}} e^{-jk\rho}$（索末菲辐射条件）。

### 6.5.2 Radiation Near Conducting Cylinder/Wedge | 导体柱/楔附近的辐射

**Example 6.5 / 例6.5** (p. 3931): 平面波散射的散射远场 → 散射宽度公式。

对于张角 $\alpha$ 的楔，场呈现奇异性 $E_z \sim r^{\pi/(2\pi-\alpha)-1}$ 在边缘处。对于 $90^\circ$ 楔，奇异性指数为 $1/3$；对于刀口 ($\alpha=0$)，为 $-1/2$（著名的平方根边缘奇异性）。

## 6.6 Addition Theorem for Cylindrical Wave Functions | 柱波函数的加法定理

$$
H_0^{(2)}(k_0|\boldsymbol{\rho} + \mathbf{d}|) = \sum_{l=-\infty}^{\infty} J_l(k_0 d) H_l^{(2)}(k_0 \rho) e^{jl(\phi - \phi_d - \pi)},\quad \rho > d \tag{6.5.32}
$$

Used extensively in FMM for 2D problems (Chapter 11) / 广泛用于二维问题的快速多极子法（第11章）。

## **Physical Intuition / 物理直觉**
- 圆波导中，TE$_{11}$ 为主模，因为 $J_1'(x)$ 的第一个零点在 $x=1.841$，小于 $J_0(x)=2.405$。
- TM模的 $E_z$ 在壁面上为零；TE模的 $E_\phi$ 在壁面上为零。
- 同轴电缆支持TEM模（无截止），因为双导体提供回流路径。
- 光纤中HE$_{11}$模无截止——它是单模光纤的基模。
- 散射宽度公式(6.4.21)显示了依赖于圆柱体尺寸与波长之比的典型空间干涉图样。

## **Numerical Intuition / 数值直觉**
- 贝塞尔函数零点决定波导截止：1 cm半径圆波导的TE$_{11}$ 截止约为8.79 GHz（空气填充）。
- 同轴线 $Z_c=50\Omega$ 对应 $b/a=2.3$（空气介质）。
- 圆柱体Mie级数散射收敛需要 $\sim ka+10$ 项——$ka=10$ 需要 $\sim 20$ 项。
- 对于 $(\epsilon_{r1}-\epsilon_{r2})/\epsilon_{r1}\approx 0.01$ 的光纤，弱导引近似极大简化特征方程。

## **Audit Table / 审计表**
| Section / 节 | Pages / 页 | Key Formulas / 关键公式 | Verified / 验证 |
|---------|-------|:------------:|:--------:|
| 6.1 | 261–265 | (6.1.1)–(6.1.22) | ✓ |
| 6.2.1 | 266–273 | (6.2.11)–(6.2.24), 表6.1,6.2 | ✓ |
| 6.2.2 | 273–276 | (6.2.25)–(6.2.40) | ✓ |
| 6.2.3 | 276–280 | (6.2.41)–(6.2.45) | ✓ |
| 6.3 | 279–287 | (6.3.1)–(6.3.60) | ✓ |
| 6.4 | 287–291 | (6.4.1)–(6.4.21) | ✓ |
| 6.5–6.7 | 291–348 | 散射/辐射公式 | ✓ |
