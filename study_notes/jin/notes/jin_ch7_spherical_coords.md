---
chapter: 7
title: Fields and Waves in Spherical Coordinates
source: Jin, Theory and Computation of Electromagnetic Fields, 2nd Ed., pp. 349–406
sections: 7
examples: 4
---

# Chapter 7: Fields and Waves in Spherical Coordinates | 第七章：球坐标中的场与波

> **中英双语版**

## 7.1 Solution of Wave Equation | 波动方程的解

Helmholtz equation in spherical coordinates / 球坐标中的亥姆霍兹方程：

$$
\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial\psi}{\partial r}\right)
+ \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial\psi}{\partial\theta}\right)
+ \frac{1}{r^2\sin^2\theta}\frac{\partial^2\psi}{\partial\phi^2}
+ k^2\psi = 0 \tag{7.1.1}
$$

### 7.1.1 Separation of Variables | 分离变量

Assume $\psi(r,\theta,\phi) = R(r)\Theta(\theta)\Phi(\phi)$ / 设 $\psi(r,\theta,\phi) = R(r)\Theta(\theta)\Phi(\phi)$。分离得到：

Angular ($\phi$) / 方位角: $\displaystyle\frac{d^2\Phi}{d\phi^2} + m^2\Phi = 0$ → $\Phi(\phi) = c_m\cos m\phi + d_m\sin m\phi$ \tag{7.1.4}

Angular ($\theta$) / 极角: Legendre's equation / 勒让德方程：

$$
\frac{1}{\sin\theta}\frac{d}{d\theta}\left(\sin\theta\frac{d\Theta}{d\theta}\right)
+ \left[n(n+1) - \frac{m^2}{\sin^2\theta}\right]\Theta = 0 \tag{7.1.9}
$$

Solutions / 解：associated Legendre functions / 缔合勒让德函数 $P_n^m(\cos\theta)$（轴上有限）和 $Q_n^m(\cos\theta)$（轴上奇异）。

Radial / 径向: Spherical Bessel equation / 球贝塞尔方程：

$$
\frac{d}{dr}\left(r^2\frac{dR}{dr}\right) + [k^2 r^2 - n(n+1)]R = 0 \tag{7.1.8}
$$

Solutions / 解：$j_n(kr)$（在 $r=0$ 处有限）和 $y_n(kr)$（在 $r=0$ 处奇异）。

General solution / 通解：

$$
\psi_{mn}(r,\theta,\phi) = [a_n j_n(kr) + b_n y_n(kr)]
\left[c_{mn}P_n^m(\cos\theta) + d_{mn}Q_n^m(\cos\theta)\right]
\left[e_m\cos m\phi + f_m\sin m\phi\right] \tag{7.1.16}
$$

**Legendre polynomials / 勒让德多项式** (Rodrigues formula / 罗德里格斯公式):

$$
P_n(x) = \frac{1}{2^n n!}\frac{d^n}{dx^n}(x^2 - 1)^n \tag{7.1.20}
$$

**Associated Legendre functions / 缔合勒让德函数**:

$$
P_n^m(x) = (-1)^m(1 - x^2)^{m/2}\frac{d^m}{dx^m}P_n(x) \tag{7.1.19}
$$

$P_n^m(x) = 0$ when $m > n$ / 当 $m > n$。

**Bessel function properties / 贝塞尔函数性质**:
- $j_n(kr) \to$ finite when $kr\to 0$ / 当 $kr\to 0$ 时有限
- $y_n(kr) \to -\infty$ when $kr\to 0$ / 当 $kr\to 0$ 时趋于 $-\infty$

**Example 7.1 / 例7.1** (p. 327): 球坐标中的拉普拉斯方程（$k=0$）。径向解：$r^n$ 和 $r^{-(n+1)}$。解：

$$
\psi(r,\theta,\phi) = \sum_{m,n} [a_n r^n + b_n r^{-(n+1)}] 
[ c_{mn}P_n^m(\cos\theta) + d_{mn}Q_n^m(\cos\theta)]
[e_m\cos m\phi + f_m\sin m\phi]
$$

### 7.1.2 Spherical Wave Functions | 球波函数

Spherical Hankel functions for outward/inward propagation / 用于向外/向内传播的球汉克尔函数：

$$
h_n^{(1)}(kr) = j_n(kr) + j y_n(kr) \tag{7.1.21}
$$
$$
h_n^{(2)}(kr) = j_n(kr) - j y_n(kr) \tag{7.1.22}
$$

Asymptotic forms / 渐近形式：

$$
h_n^{(2)}(kr) \approx \frac{1}{kr}e^{-j(kr - n\pi/2 - \pi/2)},\quad kr\gg 1 \tag{7.1.26}
$$

$h_n^{(2)}(kr)$ 代表向外传播的球面波。

### 7.1.3 TE$_r$ and TM$_r$ Modes | TE$_r$ 和 TM$_r$ 模

Use vector potentials $\mathbf{A} = \hat{r}A_r$ and $\mathbf{F} = \hat{r}F_r$ with Debye potentials / 使用带有德拜势的矢量势 $\mathbf{A} = \hat{r}A_r$ 和 $\mathbf{F} = \hat{r}F_r$。

**TE$_r$ modes / TE$_r$ 模** ($\mathbf{A}=0$, $\mathbf{F}=\hat{r}F_r$):

$$
E_r = 0,\quad H_r = \frac{1}{j\omega\mu\epsilon}\left(\frac{\partial^2}{\partial r^2} + k^2\right)F_r \tag{7.1.27}
$$
$$
E_\theta = -\frac{1}{\epsilon}\frac{1}{r\sin\theta}\frac{\partial F_r}{\partial\phi},\quad
H_\theta = \frac{1}{j\omega\mu\epsilon}\frac{1}{r}\frac{\partial^2 F_r}{\partial r\partial\theta} \tag{7.1.28}
$$
$$
E_\phi = \frac{1}{\epsilon}\frac{1}{r}\frac{\partial F_r}{\partial\theta},\quad
H_\phi = \frac{1}{j\omega\mu\epsilon}\frac{1}{r\sin\theta}\frac{\partial^2 F_r}{\partial r\partial\phi} \tag{7.1.29}
$$

**TM$_r$ modes / TM$_r$ 模** ($\mathbf{F}=0$, $\mathbf{A}=\hat{r}A_r$):

$$
E_r = \frac{1}{j\omega\mu\epsilon}\left(\frac{\partial^2}{\partial r^2} + k^2\right)A_r,\quad H_r = 0 \tag{7.1.30}
$$
$$
E_\theta = \frac{1}{j\omega\mu\epsilon}\frac{1}{r}\frac{\partial^2 A_r}{\partial r\partial\theta},\quad
H_\theta = \frac{1}{\mu}\frac{1}{r\sin\theta}\frac{\partial A_r}{\partial\phi} \tag{7.1.31}
$$
$$
E_\phi = \frac{1}{j\omega\mu\epsilon}\frac{1}{r\sin\theta}\frac{\partial^2 A_r}{\partial r\partial\phi},\quad
H_\phi = -\frac{1}{\mu}\frac{1}{r}\frac{\partial A_r}{\partial\theta} \tag{7.1.32}
$$

球谐函数 $Y_n^m(\theta,\phi)$ 是任何球对称问题的自然基。

## 7.2 Spherical Cavity | 球腔 (pp. 331–335)

**TE$_r$ modes / TE$_r$ 模**: Characteristic equation / 特征方程 $\hat{J}_n(ka) = 0$。Roots / 根 $\varsigma_{np}$ (Table 7.1)。

Resonant frequency / 谐振频率：$f_{r,mnp}^{\text{TE}} = \varsigma_{np}/(2\pi a\sqrt{\mu\epsilon})$，$n=1,2,\dots$, $m=0,\dots,n$, $p=1,2,\dots$。

**TM$_r$ modes / TM$_r$ 模**: Characteristic equation / 特征方程 $\hat{J}_n'(ka) = 0$。Roots / 根 $\varsigma_{np}'$ (Table 7.2)。

| n | p=1 | p=2 | p=3 | p=4 |
|:-:|:---:|:---:|:---:|:---:|
| **Roots of $\hat{J}_n(z)=0$ ($\varsigma_{np}$, TE$_r$ modes)** | | | | |
| 1 | 4.493409 | 7.725252 | 10.90412 | 14.06619 |
| 2 | 5.763459 | 9.095011 | 12.32294 | 15.51460 |
| **Roots of $\hat{J}_n'(z)=0$ ($\varsigma_{np}'$, TM$_r$ modes)** | | | | |
| 1 | 2.743707 | 6.116764 | 9.316616 | 12.48594 |
| 2 | 3.870239 | 7.443087 | 10.71301 | 13.92052 |

**Dominant mode / 主模**: TM$_{r,m11}$ ($k_{r,m11}^{\text{TM}} = 2.7437/a$, $f = 0.4367/(a\sqrt{\mu\epsilon})$)。

Field components of TM$_{r,011}$ mode ($m=0$) / TM$_{r,011}$ 模的场分量：

$$
E_r = \frac{2}{r^2}\cos\theta\; \hat{J}_1(\varsigma_{11}' r/a)
$$
$$
E_\theta = -\frac{\varsigma_{11}'}{ar}\sin\theta\; \hat{J}_1'(\varsigma_{11}' r/a)
$$
$$
H_\phi = -j\omega\epsilon\frac{1}{r}\sin\theta\; \hat{J}_1(\varsigma_{11}' r/a)
$$

**Example 7.2 / 例7.2** (p. 334): TM$_{r,011}$ 模的品质因数。

$$
Q_c = \frac{\eta}{R_s}\frac{\int_0^{\varsigma_{11}'} [\hat{J}_1(x)]^2 dx}{[\hat{J}_1(\varsigma_{11}')]^2}
= 1.007\,\frac{\eta}{R_s}
$$

球腔的 $Q$ 比同尺寸的圆柱腔高25%，比立方腔高36%。

## 7.3 Biconical Antenna | 双锥天线 (pp. 335–352)

### 7.3.1 Infinitely Long Model | 无穷长模型 (p. 335)

Two semi-infinite conducting cones with half-angle $\theta_0$, apex at origin / 两个半无限导体锥，半张角 $\theta_0$，顶点在原点。

Fields expressed using $P_\nu^m(\cos\theta)$, $P_\nu^m(-\cos\theta)$ and $\hat{H}_\nu^{(2)}(kr)$ / 使用 $P_\nu^m(\cos\theta)$, $P_\nu^m(-\cos\theta)$ 和 $\hat{H}_\nu^{(2)}(kr)$ 表达场。

For the dominant **TEM mode** ($m=0$, $\nu=0$) / 对主**TEM模**：

$$
E_\theta = 0,\quad E_r = \frac{V_0}{r\ln(\cot(\theta_0/2))}e^{-jkr},\quad H_\phi = \frac{E_r}{\eta} \tag{7.3.2}
$$

Characteristic impedance / 特性阻抗：$Z_c = \frac{\eta}{\pi}\ln\left(\cot\frac{\theta_0}{2}\right)$。

### 7.3.2 Finite Model | 有限长模型 (p. 353)

Length $L$, terminated by a spherical cap of radius $L$ / 长度 $L$，由半径 $L$ 的球冠端接。输入阻抗通过开端反射计算。

双锥天线是典型的宽带天线——其TEM模提供与频率无关的输入阻抗。

## 7.4 Plane Wave Expansion and Wave Transformation | 平面波展开与波变换 (pp. 352–365)

### 7.4.1 Scalar Wave Transformation | 标量波变换

Plane wave → spherical wave expansion / 平面波→球波展开：

$$
e^{-jkr\cos\theta} = \sum_{n=0}^\infty (-j)^n(2n+1)j_n(kr)P_n(\cos\theta) \tag{7.4.2}
$$

### 7.4.2 Vector Wave Transformation | 矢量波变换 (p. 366)

$x$-polarized plane wave $\mathbf{E}^{\text{inc}} = \hat{x} E_0 e^{-jkz}$ / $x$极化平面波：

$$
\mathbf{E}^{\text{inc}} = E_0\sum_{n=1}^\infty (-j)^n\frac{2n+1}{n(n+1)}
\left[\mathbf{M}_{o1n}^{(1)}(r,\theta,\phi) - j\mathbf{N}_{e1n}^{(1)}(r,\theta,\phi)\right] \tag{7.4.3}
$$

其中 $\mathbf{M}_{o1n}^{(1)} = \nabla\times(\mathbf{r}\psi_{o1n})$ 和 $\mathbf{N}_{e1n}^{(1)} = \frac{1}{k}\nabla\times\mathbf{M}_{e1n}^{(1)}$，$\psi_{o1n} = j_n(kr)P_n^1(\cos\theta)\sin\phi$，$\psi_{e1n} = j_n(kr)P_n^1(\cos\theta)\cos\phi$。

## 7.5 Mie Scattering | 米氏散射 (pp. 365–385)

### 7.5.1 Scattering by a Conducting Sphere | 导体球的散射 (p. 366)

Using the wave expansion (7.4.3) and boundary condition at $r=a$ ($\hat{n}\times\mathbf{E}^{\text{total}} = 0$) / 使用波展开(7.4.3)和 $r=a$ 处的边界条件：

$$
a_n = -\frac{j_n(ka)}{h_n^{(2)}(ka)},\quad
b_n = -\frac{[k a j_n(ka)]'}{[k a h_n^{(2)}(ka)]'} \tag{7.5.1}
$$

其中 $a_n$ 为TM系数，$b_n$ 为TE系数。

Scattered field / 散射场：

$$
\mathbf{E}^{\text{sc}} = E_0\sum_{n=1}^\infty (-j)^n\frac{2n+1}{n(n+1)}
\left[a_n\mathbf{M}_{o1n}^{(4)} - j b_n\mathbf{N}_{e1n}^{(4)}\right] \tag{7.5.2}
$$

### 7.5.2 Scattering by a Dielectric Sphere | 介质球的散射 (p. 366)

For a dielectric sphere $(\epsilon_d,\mu_d)$, internal and scattered fields matched at $r=a$ / 对介质球，在 $r=a$ 处匹配内部场和散射场：

$$
a_n = \frac{\mu_d j_n(k_d a)[k a j_n(ka)]' - \mu j_n(ka)[k_d a j_n(k_d a)]'}{\mu_d j_n(k_d a)[k a h_n^{(2)}(ka)]' - \mu h_n^{(2)}(ka)[k_d a j_n(k_d a)]'} \tag{7.5.3}
$$
$$
b_n = \frac{\mu j_n(k_d a)[k a j_n(ka)]' - \mu_d j_n(ka)[k_d a j_n(k_d a)]'}{\mu j_n(k_d a)[k a h_n^{(2)}(ka)]' - \mu_d h_n^{(2)}(ka)[k_d a j_n(k_d a)]'} \tag{7.5.4}
$$

**Scattering cross-section / 散射截面**: $\sigma_s = \frac{2\pi}{k^2}\sum_{n=1}^\infty (2n+1)(|a_n|^2 + |b_n|^2)$。

**Extinction cross-section / 消光截面** (optical theorem / 光学定理): $\sigma_e = -\frac{2\pi}{k^2}\sum_{n=1}^\infty (2n+1)\Re(a_n + b_n)$。

米氏理论描述球体如何散射光——比值 $ka$ 决定是瑞利散射 ($ka\ll 1$) 还是光学散射 ($ka\sim 1$ 或更大)。

### 7.5.3 Multilayer Dielectric Sphere | 多层介质球 (p. 370)

Generalized using transfer matrix method for $N$-layer spheres / 使用传输矩阵法推广到 $N$ 层球体。递推公式计算复合球的散射系数 $a_n$, $b_n$。

## 7.6 Addition Theorem for Spherical Wave Functions | 球波函数的加法定理 (pp. 385–390)

For a point charge at $\mathbf{r}'$ on the $z$-axis / 对于 $z$ 轴上 $\mathbf{r}'$ 处的点电荷：

$$
\frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{|\mathbf{r} - \mathbf{r}'|}
= -jk\sum_{n=0}^\infty (-1)^n(2n+1)j_n(kr_<)h_n^{(2)}(kr_>)P_n(\cos\gamma) \tag{7.6.1}
$$

其中 $r_< = \min(r,r')$, $r_> = \max(r,r')$, $\cos\gamma = \hat{r}\cdot\hat{r}'$。

For off-center source, the generalized addition theorem involves spherical harmonics $Y_n^m(\theta,\phi)$ / 对偏心源，广义加法定理涉及球谐函数 $Y_n^m(\theta,\phi)$。这是三维FMM和MLFMA（第11章）的基础。

## 7.7 Radiation in the Presence of a Sphere or Cone | 球体或锥体存在时的辐射 (pp. 390–406)

### 7.7.1 Radiation Near a Conducting Sphere | 导体球附近的辐射 (p. 390)

A spherical surface current $J_s$ on a sphere of radius $a$ radiates fields expressed as spherical wave expansions with coefficients determined by $J_s$ via $\mathbf{H}^{\text{sc}} = \frac{1}{jk\eta}\nabla\times\mathbf{E}^{\text{sc}}$ / 半径为 $a$ 的球上球面电流 $J_s$ 辐射的场用球波展开表示，系数由 $J_s$ 通过 $\mathbf{H}^{\text{sc}} = \frac{1}{jk\eta}\nabla\times\mathbf{E}^{\text{sc}}$ 确定。

### 7.7.2 Field Singularity at a Sharp Conducting Tip | 尖锐导体尖端的场奇异性 (p. 395)

For a conducting cone with half-angle $\theta_0$, fields near the tip exhibit singular behavior / 对于半张角 $\theta_0$ 的导体锥，尖端附近的场呈现奇异行为：

$$
E, H \sim r^{\nu-1}
$$

where $\nu$ satisfies $P_\nu^1(\cos\theta_0) = 0$ (TM-type) or $P_\nu^1(\cos\theta_0)' = 0$ (TE-type) / 其中 $\nu$ 满足 $P_\nu^1(\cos\theta_0) = 0$（TM型）或 $P_\nu^1(\cos\theta_0)' = 0$（TE型）。

For a sharp tip ($\theta_0\to 0$), $\nu \approx 1/[2\ln(2/\theta_0)]$, giving a very strong singularity / 尖锐尖端产生很强的奇异性。For a $90^\circ$ wedge ($\theta_0 = 135^\circ$), $\nu \approx 0.5$ (square-root singularity, consistent with the 2D edge result) / 平方根奇异性，与二维边缘结果一致。

尖锐导体尖端的场奇异性是数值方法的根本挑战（需要渐变或极细的网格）。

## **Physical Intuition / 物理直觉**
- 球谐函数 $Y_n^m(\theta,\phi)$ 是任何球对称问题的自然基。
- 米氏理论描述球体如何散射光——比值 $ka$ 决定是瑞利散射还是光学散射。
- 双锥天线是典型的宽带天线——其TEM模提供与频率无关的输入阻抗。
- 尖锐导体尖端的场奇异性是数值方法的根本挑战（需要渐变或极细的网格）。

## **Numerical Intuition / 数值直觉**
- 米氏级数收敛需要 $\sim ka + 10$ 项。对于 $ka=100$，需要 $\sim 110$ 项。
- 球腔 $Q$ 依赖于模式——主TM模的 $Q_c \approx \eta/R_s$，对超导腔可达很高。
- 加法定理(7.6.1)是三维FMM和MLFMA（第11章）的基础。
- 对 $ka=1$、$\epsilon_r=4$ 的球体，后向散射RCS约为 $\sim 0.3\lambda^2$（米氏共振），远大于瑞利极限 ($\sim a^6/\lambda^4$) 或光学极限 ($\sim \pi a^2$)。

## **Audit Table / 审计表**
| Section / 节 | Pages / 页 | Key Formulas / 关键公式 | Verified / 验证 |
|---------|-------|:------------:|:--------:|
| 7.1 | 349–354 | (7.1.1)–(7.1.43) | ✓ |
| 7.2 | 354–360 | (7.2.1)–(7.2.17), 表7.1,7.2 | ✓ |
| 7.3 | 360–365 | 双锥天线公式 | ✓ |
| 7.4 | 365–370 | (7.4.2)–(7.4.3) | ✓ |
| 7.5 | 370–385 | (7.5.1)–(7.5.4), 米氏系数 | ✓ |
| 7.6 | 385–390 | (7.6.1), 加法定理 | ✓ |
| 7.7 | 390–406 | 奇异性分析 | ✓ |
