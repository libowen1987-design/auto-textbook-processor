# Balanis 第 12 章 — 口径天线 (Aperture Antennas)

> **范围:** §12.1 – §12.8  
> **教材:** Balanis, *Antenna Theory: Analysis and Design*, 4th Ed.

---

## §12.1 引言 (Introduction)

口径天线利用开口面（aperture）向空间辐射电磁波。典型例子：

- 波导开口喇叭天线 (horn antenna)
- 反射面天线 (reflector antenna) — 抛物面碟形
- 微带贴片天线 (microstrip patch antenna)
- 缝隙天线 (slot antenna)
- 开口波导 (open-ended waveguide)

**核心思想:** 口径面上的场分布决定了远区辐射特性。通过口径场 → 等效源 → 远场积分 → 方向图/方向性系数。

---

## §12.2 场等效原理：惠更斯原理 (Field Equivalence Principle: Huygens' Principle)

### 表面等效定理 (Surface Equivalence Theorem)

在封闭面 $S$ 上给定等效面电流 $\mathbf{J}_s$ 和面磁流 $\mathbf{M}_s$，可唯一确定外部区域的场：

$$
\boxed{\mathbf{J}_s = \hat{\mathbf{n}} \times \mathbf{H}_a}
\qquad
\boxed{\mathbf{M}_s = -\hat{\mathbf{n}} \times \mathbf{E}_a}
\tag{12-1}
$$

其中 $\mathbf{E}_a, \mathbf{H}_a$ 是口径面上的场，$\hat{\mathbf{n}}$ 是外法向。

### Love 等效原理 (Love's Equivalence Principle)

当 $S$ 与理想导体表面重合时，$\mathbf{M}_s = 0$；当 $S$ 与理想磁体表面重合时，$\mathbf{J}_s = 0$。由此仅需保留一种源：

- 仅 $\mathbf{M}_s$ 在电壁上 → 仅磁流源
- 仅 $\mathbf{J}_s$ 在磁壁上 → 仅电流源

### 惠更斯源 (Huygens Source)

惠更斯原理的电磁表述：波前上每一点都是次级球面波的源。对于平面口径，惠更斯源是电基本振子和磁基本振子的正交组合，方向图因子为：

$$
\boxed{F(\theta) = \frac{1 + \cos\theta}{2}}
\tag{12-2}
$$

即**惠更斯方向图因子** (Huygens pattern factor)。

> **物理含义:** $\cos\theta$ 来自磁振子（等效磁流环），$1$ 来自电场分量组合，二者叠加得到前向增强、后向抑制的单向方向图。

---

## §12.3 辐射方程 (Radiation Equations)

### 矢量位公式

由等效源 $\mathbf{J}_s, \mathbf{M}_s$ 构造矢量电位 $\mathbf{F}$ 和矢量磁位 $\mathbf{A}$：

$$
\mathbf{A} = \frac{\mu}{4\pi} \iint_S \mathbf{J}_s \frac{e^{-jkR}}{R} \, ds'
\qquad
\mathbf{F} = \frac{\varepsilon}{4\pi} \iint_S \mathbf{M}_s \frac{e^{-jkR}}{R} \, ds'
\tag{12-3}
$$

### 远场积分

在远区 ($R \approx r - \mathbf{r}' \cdot \hat{\mathbf{r}}$)，远场为：

$$
\boxed{\mathbf{E} \approx -\frac{j k e^{-jkr}}{4\pi r} \bigl[ \eta \mathbf{N} + \hat{\mathbf{r}} \times \mathbf{L} \bigr]}
\qquad
\boxed{\mathbf{H} \approx +\frac{j k e^{-jkr}}{4\pi r} \bigl[ \frac{1}{\eta} \mathbf{L} - \hat{\mathbf{r}} \times \mathbf{N} \bigr]}
\tag{12-4}
$$

其中辐射矢量 (radiation vectors)：

$$
\boxed{\mathbf{N} = \iint_S \mathbf{J}_s(\mathbf{r}') \, e^{j k \mathbf{r}' \cdot \hat{\mathbf{r}}} \, ds'}
\qquad
\boxed{\mathbf{L} = \iint_S \mathbf{M}_s(\mathbf{r}') \, e^{j k \mathbf{r}' \cdot \hat{\mathbf{r}}} \, ds'}
\tag{12-5}
$$

当考虑口径在 $z=0$ 平面上的辐射：

$$
\mathbf{r}' = x'\hat{\mathbf{x}} + y'\hat{\mathbf{y}}, \quad
\hat{\mathbf{r}} = \sin\theta\cos\phi\,\hat{\mathbf{x}} + \sin\theta\sin\phi\,\hat{\mathbf{y}} + \cos\theta\,\hat{\mathbf{z}}
$$

$$
k \mathbf{r}' \cdot \hat{\mathbf{r}} = k(x' \sin\theta\cos\phi + y' \sin\theta\sin\phi)
\tag{12-6}
$$

---

## §12.4 矩形口径 (Rectangular Apertures)

### 12.4.1 均匀照射 (Uniform Illumination)

口径尺寸 $a \times b$，均匀场 $\mathbf{E}_a = E_0 \hat{\mathbf{y}}$。

**辐射矢量:**

$$
\mathbf{N} = 0, \quad \mathbf{L} = -2 E_0 \iint_{-a/2}^{a/2} \int_{-b/2}^{b/2} e^{j(k_x x' + k_y y')} \, dx'\,dy' \,\hat{\mathbf{x}}
\tag{12-7}
$$

其中 $k_x = k\sin\theta\cos\phi$, $k_y = k\sin\theta\sin\phi$。

积分得：

$$
\boxed{\mathbf{L} = -2 E_0 ab \,
\frac{\sin X}{X} \, \frac{\sin Y}{Y} \,\hat{\mathbf{x}}}
\tag{12-8}
$$

其中：

$$
X = \frac{k a}{2} \sin\theta\cos\phi, \qquad
Y = \frac{k b}{2} \sin\theta\sin\phi
\tag{12-9}
$$

### 辐射场分量

忽略 $\theta$ 无关因子的归一化场：

$$
E_\theta = -j \frac{k e^{-jkr}}{2\pi r} \, ab E_0 \,
\frac{\sin X}{X} \frac{\sin Y}{Y} \, (\sin\phi)
\tag{12-10a}
$$

$$
E_\phi = -j \frac{k e^{-jkr}}{2\pi r} \, ab E_0 \,
\frac{\sin X}{X} \frac{\sin Y}{Y} \, (\cos\phi\cos\theta)
\tag{12-10b}
$$

### 主平面方向图

**E 面** ($\phi = \pi/2$, 电场平行于 $y$ 轴):

$$
\boxed{F_E(\theta) = \frac{\sin Y}{Y}, \quad Y = \frac{k b}{2} \sin\theta}
\tag{12-11}
$$

**H 面** ($\phi = 0$, 磁场所在平面):

$$
\boxed{F_H(\theta) = \frac{\sin X}{X}, \quad X = \frac{k a}{2} \sin\theta}
\tag{12-12}
$$

### 方向性系数 (Directivity)

均匀照射矩形口径的最大方向性系数：

$$
\boxed{D_0 = \frac{4\pi}{\lambda^2} (ab) = \frac{4\pi A_p}{\lambda^2}}
\tag{12-13}
$$

其中 $A_p = ab$ 是物理面积。

> **注:** 均匀照射时口径效率 $\varepsilon_{ap} = 1$ (100%)，但实际中因馈源锥削、边缘绕射等，效率通常低于 1。

### 波瓣宽度 (Beamwidth)

E 面半功率波瓣宽度 (HPBW)：

$$
\boxed{\text{HPBW}_E \approx 0.886 \frac{\lambda}{b} \,\text{(rad)} = 50.8 \frac{\lambda}{b} \,\text{(deg)}}
\tag{12-14}
$$

H 面半功率波瓣宽度：

$$
\boxed{\text{HPBW}_H \approx 0.886 \frac{\lambda}{a} \,\text{(rad)} = 50.8 \frac{\lambda}{a} \,\text{(deg)}}
\tag{12-15}
$$

### 12.4.2 TE₁₀ 模照射 (TE₁₀ Mode Illumination)

典型矩形波导 TE₁₀ 模口径场：

$$
\boxed{\mathbf{E}_a = E_0 \cos\left(\frac{\pi x'}{a}\right) \hat{\mathbf{y}}}
\qquad (|x'| \le a/2, \; |y'| \le b/2)
\tag{12-16}
$$

辐射矢量：

$$
L_x = -2 E_0 \int_{-a/2}^{a/2} \cos\frac{\pi x'}{a} e^{j k_x x'} \,dx' \int_{-b/2}^{b/2} e^{j k_y y'} \,dy'
\tag{12-17}
$$

积分结果：

$$
\boxed{L_x = -2 E_0 ab \,
\frac{\cos X}{1 - (2X/\pi)^2} \, \frac{\sin Y}{Y}}
\tag{12-18}
$$

其中 $X, Y$ 定义同 (12-9)。

### 方向图特性 (TE₁₀)

**E 面** ($\phi = \pi/2$) — 同均匀照射：

$$
F_E(\theta) = \frac{\sin Y}{Y}
\tag{12-19}
$$

**H 面** ($\phi = 0$) — 因余弦锥削变宽：

$$
\boxed{F_H(\theta) = \frac{\cos X}{1 - (2X/\pi)^2}}
\tag{12-20}
$$

**方向性系数：**

$$
\boxed{D_0 \approx 0.81 \times \frac{4\pi A_p}{\lambda^2}}
\tag{12-21}
$$

即口径效率 $\varepsilon_{ap} \approx 0.81$ (余弦锥削比均匀照射旁瓣低但增益略降)。

### 12.4.3 一般口径分布与傅里叶变换法

口径辐射方向图是口径场分布的二维傅里叶变换：

$$
\boxed{F(\theta,\phi) \propto \mathcal{F}\{E_a(x',y')\} =
\iint E_a(x',y') \, e^{j(k_x x' + k_y y')} \, dx'\,dy'}
\tag{12-22}
$$

其中 $k_x = k\sin\theta\cos\phi$, $k_y = k\sin\theta\sin\phi$。

这意味着：
- **宽口径 → 窄波束** (变换对的反比关系)
- **锥削口径 → 低旁瓣、宽主瓣**
- **FFT 可高效计算任意分布的方向图**

---

## §12.5 圆形口径 (Circular Apertures)

### 12.5.1 均匀照射 (Uniform Illumination)

半径为 $a$ 的圆形口径，均匀场 $E_a = E_0$。

利用极坐标变换：

$$
x' = \rho' \cos\phi', \quad y' = \rho' \sin\phi'
$$

辐射积分：

$$
\mathbf{L} \propto \int_0^{a} \int_0^{2\pi} e^{j k \rho' \sin\theta \cos(\phi-\phi')} \rho' \, d\phi' \, d\rho'
\tag{12-23}
$$

### 贝塞尔函数表示

利用 Bessel 恒等式 $\int_0^{2\pi} e^{jz\cos\psi} d\psi = 2\pi J_0(z)$：

$$
\boxed{F(\theta) = 2\pi a^2 \, \frac{J_1(ka\sin\theta)}{ka\sin\theta}}
\tag{12-24}
$$

归一化方向图 (均匀圆形口径)：

$$
\boxed{F_u(\theta) = \frac{2 J_1(u)}{u}, \quad u = ka\sin\theta}
\tag{12-25}
$$

### 方向图特性

| 参数 | 值 |
|------|-----|
| 第一零点 | $u = 3.832$ → $\sin\theta_{0} = 3.832/(ka)$ |
| 第一旁瓣电平 | $-17.6$ dB (在 $u = 5.136$) |
| HPBW | $\approx 1.02 \frac{\lambda}{2a}$ rad = $58.4 \frac{\lambda}{D}$ deg |
| 方向性系数 | $\boxed{D_0 = \frac{4\pi (\pi a^2)}{\lambda^2} = \frac{4\pi A}{\lambda^2}}$ |

### 12.5.2 锥削照射 (Tapered Illumination)

常见锥削函数及其参数：

| 分布类型 | 口径函数 $f(\rho)$ | 旁瓣电平 | 效率 $\varepsilon_{ap}$ |
|----------|-------------------|----------|------------------------|
| Uniform | $1$ | $-17.6$ dB | $1.0$ |
| Parabolic | $1 - (\rho/a)^2$ | $-24.6$ dB | $0.75$ |
| Parabolic² | $[1 - (\rho/a)^2]^2$ | $-30.6$ dB | $0.56$ |
| Cosine | $\cos(\pi\rho/(2a))$ | $-23.0$ dB | $0.79$ |

通用模式积分：

$$
\boxed{F(\theta) = \int_0^a f(\rho') J_0(k\rho'\sin\theta) \, \rho' \, d\rho'}
\tag{12-26}
$$

---

## §12.6 设计考量 (Design Considerations)

### 口径效率 (Aperture Efficiency)

$$
\boxed{\varepsilon_{ap} = \frac{D_0}{4\pi A_p / \lambda^2}}
\tag{12-27}
$$

影响效率的主要因素：

1. **锥削效率** $\varepsilon_t$ — 照射幅度锥削引起的增益下降
2. **溢出效率** $\varepsilon_s$ — 馈源能量溢出口径之外
3. **相位效率** $\varepsilon_p$ — 口径场相位不均匀
4. **阻挡效率** $\varepsilon_b$ — 馈源/支撑结构的阻挡
5. **表面误差效率** $\varepsilon_r$ — 反射面形变

总效率：$\varepsilon_{ap} = \varepsilon_t \cdot \varepsilon_s \cdot \varepsilon_p \cdot \varepsilon_b \cdot \varepsilon_r$

### 增益与方向性系数关系

$$
\boxed{G = \varepsilon_{ap} D_0 = \varepsilon_{ap} \frac{4\pi A_p}{\lambda^2}}
\tag{12-28}
$$

### 旁瓣控制

- 均匀照射 → 最窄波束但最高旁瓣 ($-13.3$ dB 对矩形, $-17.6$ dB 对圆形)
- 锥削 → 旁瓣降低但主瓣展宽
- 泰勒分布 (Taylor distribution) → 可控旁瓣电平的折中设计

---

## §12.7 等效电路 (Equivalent Circuit)

### 口径导纳 (Aperture Admittance)

对于波导馈电的口径，从波导向外看去的等效导纳为：

$$
\boxed{Y_{\text{ap}} = G_{\text{ap}} + j B_{\text{ap}}}
\tag{12-29}
$$

### 电导分量

$$
\boxed{G_{\text{ap}} = \frac{1}{\eta_0} \iint_{\text{aperture}} \mathbf{E}_a \times \mathbf{H}_a^* \cdot \hat{\mathbf{n}} \, ds}
\tag{12-30}
$$

该式表示口径向外辐射的实功率。对于波导开口：

$$
G_{\text{ap}} \approx \frac{1}{\eta_0} \frac{ab}{2} \quad (\text{TE}_{10}模, 无限大地板})
\tag{12-31}
$$

### 电纳分量

电纳 $B_{\text{ap}}$ 是储能近场的反映，与口径尺寸和频率有关：

- 电大口径 $(a \gg \lambda)$ → $B_{\text{ap}} \to 0$ (纯电阻辐射)
- 电小口径 → 显著电纳，谐振特性

### 传输线等效

```
波导(TE₁₀) → [Y_ap = G_ap + jB_ap] → 自由空间
```

匹配条件：波导特性导纳 $Y_0 = G_{\text{ap}}$ 且 $B_{\text{ap}} = 0$。

---

## §12.8 巴俾涅原理 (Babinet's Principle)

### 原理表述

Babinet 原理指出：**互补屏的衍射场之和等于无屏时的入射场。**

$$
\boxed{\mathbf{E}_a + \mathbf{E}_c = \mathbf{E}_i}
\qquad
\boxed{\mathbf{H}_a + \mathbf{H}_c = \mathbf{H}_i}
\tag{12-32}
$$

其中脚标 $a$ 表示口径 (aperture)，$c$ 表示互补屏 (complementary screen)，$i$ 表示入射场 (incident field)。

### 天线中的 Babinet 原理

对于电磁互补天线对：

- 缝隙天线 (slot antenna) 与偶极子天线 (dipole) 互补
- 缝隙的阻抗与互补偶极子的阻抗关系：

$$
\boxed{Z_{\text{slot}} \cdot Z_{\text{dipole}} = \frac{\eta^2}{4}}
\tag{12-33}
$$

对于自由空间，$\eta = \eta_0 \approx 377\,\Omega$：

$$
Z_{\text{slot}} \cdot Z_{\text{dipole}} \approx (188.5)^2 \,\Omega^2
\tag{12-34}
$$

### 应用

- 半波缝隙天线的阻抗可由半波偶极子 $(Z_d \approx 73\,\Omega)$ 推导：

$$
\boxed{Z_{\text{slot}} \approx \frac{\eta_0^2}{4 Z_{\text{dipole}}} \approx \frac{(377)^2}{4 \times 73} \approx 486 \,\Omega}
\tag{12-35}
$$

- 方向图相同但极化正交（电场与磁场互换）

---

## 关键公式汇总

| 内容 | 公式 |
|------|------|
| 等效源 | $\mathbf{J}_s = \hat{\mathbf{n}} \times \mathbf{H}_a$, $\mathbf{M}_s = -\hat{\mathbf{n}} \times \mathbf{E}_a$ |
| 惠更斯因子 | $(1 + \cos\theta)/2$ |
| 辐射矢量 | $\mathbf{N} = \iint \mathbf{J}_s e^{jk\mathbf{r}'\cdot\hat{\mathbf{r}}} ds'$, $\mathbf{L} = \iint \mathbf{M}_s e^{jk\mathbf{r}'\cdot\hat{\mathbf{r}}} ds'$ |
| 远场 | $\mathbf{E} = -\frac{jke^{-jkr}}{4\pi r}[\eta \mathbf{N} + \hat{\mathbf{r}} \times \mathbf{L}]$ |
| 矩形口径均匀 $D_0$ | $D_0 = 4\pi A_p / \lambda^2$ |
| 矩形口径 TE₁₀ $D_0$ | $D_0 \approx 0.81 \times 4\pi A_p / \lambda^2$ |
| 圆形口径均匀 $D_0$ | $D_0 = 4\pi A / \lambda^2$ |
| 圆形口径均匀模式 | $F(u) = 2J_1(u)/u$, $u = ka\sin\theta$ |
| Babinet 阻抗 | $Z_{\text{slot}} Z_{\text{dipole}} = \eta^2/4$ |
| 傅里叶变换法 | $F(\theta,\phi) \propto \mathcal{F}\{E_a(x',y')\}$ |

---

*笔记行数: 230+ lines*
