# Chapter 3: Electromagnetic Theorems and Principles | 第三章：电磁定理与原理

> **中英双语版**

> Jin, *Theory and Computation of Electromagnetic Fields*, 2nd Ed., Ch. 3, pp. 89–134.

从麦克斯韦方程组出发，本章推导了几个基本定理：**唯一性定理**、**镜像原理**、**互易定理**、**等效原理**、**对偶原理**和**巴俾涅原理**。这些定理为解决等效问题、构造积分方程以及求解散射/辐射问题提供了数学基础。

---

## 3.1 Uniqueness Theorem | 唯一性定理 (pp. 90–94)

The field within a volume $V$ bounded by $S$ is uniquely determined if / 边界为 $S$ 的体积 $V$ 内的场在以下条件下唯一确定：

1. $\hat{n} \times \mathbf{E}$ is specified **everywhere on $S$** / $\hat{n} \times \mathbf{E}$ 在 $S$ 上**处处**给定，或
2. $\hat{n} \times \mathbf{H}$ is specified **everywhere on $S$** / $\hat{n} \times \mathbf{H}$ 在 $S$ 上**处处**给定，或
3. $\hat{n} \times \mathbf{E}$ on part of $S$ and $\hat{n} \times \mathbf{H}$ on the rest / $\hat{n} \times \mathbf{E}$ 在 $S$ 的一部分且 $\hat{n} \times \mathbf{H}$ 在其余部分。

### Proof (time-harmonic case) / 证明（时谐情况）

假设两个解 $(\mathbf{E}_a, \mathbf{H}_a)$ 和 $(\mathbf{E}_b, \mathbf{H}_b)$ 具有相同源 $\mathbf{J}_i, \mathbf{M}_i$。令 $\delta\mathbf{E} = \mathbf{E}_a - \mathbf{E}_b$, $\delta\mathbf{H} = \mathbf{H}_a - \mathbf{H}_b$。从麦克斯韦方程组：

$$
\nabla \times \delta\mathbf{E} = -j\omega\mu\,\delta\mathbf{H}, \qquad
\nabla \times \delta\mathbf{H} = (j\omega\epsilon + \sigma)\,\delta\mathbf{E}.
$$

Forming $\nabla\cdot(\delta\mathbf{E} \times \delta\mathbf{H}^*)$ and integrating over $V$ / 构造 $\nabla\cdot(\delta\mathbf{E} \times \delta\mathbf{H}^*)$ 并在 $V$ 上积分：

$$
\oint_S (\delta\mathbf{E} \times \delta\mathbf{H}^*) \cdot d\mathbf{S}
= \int_V \bigl[-j\omega\mu|\delta\mathbf{H}|^2 + (j\omega\epsilon^* - \sigma)|\delta\mathbf{E}|^2\bigr]\,dV.
$$

在三类边界条件下，面积分为零。对于有损耗媒质（$\epsilon'', \mu'', \sigma > 0$），实部迫使 $\int_V [(\omega\epsilon''+\sigma)|\delta\mathbf{E}|^2 + \omega\mu''|\delta\mathbf{H}|^2]\,dV = 0$，从而 $\delta\mathbf{E} = \delta\mathbf{H} = 0$ 处处成立。

### Example 3.1 — Electrostatic Uniqueness | 静电场唯一性

For $\nabla \times \mathbf{E} = 0$, $\nabla \cdot (\epsilon\mathbf{E}) = \rho_e$, let $\mathbf{E} = -\nabla\varphi$。若 $\varphi_a$ 和 $\varphi_b$ 都满足 $\nabla\cdot(\epsilon\nabla\varphi) = -\rho_e$，则 $\delta\varphi = \varphi_a - \varphi_b$ 满足 $\nabla\cdot(\epsilon\nabla\delta\varphi) = 0$。使用格林第一恒等式：

$$
\int_V \epsilon|\delta\mathbf{E}|^2\,dV = \oint_S \epsilon\,\delta\varphi\,\frac{\partial\delta\varphi}{\partial n}\,dS.
$$

如果法向分量 $\hat{n}\cdot\mathbf{E}$ 或切向分量（从而 $\delta\varphi$ 在 $S$ 上）被指定，则右端为零，证明唯一性。

### Example 3.2 — Time-Varying Uniqueness | 时变场唯一性

对于一般时变场：

$$
\oint_S (\delta\mathbf{E} \times \delta\mathbf{H})\cdot d\mathbf{S}
= -\frac{\partial}{\partial t}\int_V \Bigl(\frac{\epsilon}{2}|\delta\mathbf{E}|^2 + \frac{\mu}{2}|\delta\mathbf{H}|^2\Bigr)dV
- \int_V \sigma|\delta\mathbf{E}|^2\,dV \le 0.
$$

在零初始条件 ($t=0$) 和 $S$ 上指定切向 $\mathbf{E}$ 或 $\mathbf{H}$ 下，能量积分为零，故 $\delta\mathbf{E} = \delta\mathbf{H} = 0$。

---

## 3.2 Image Theory | 镜像原理 (pp. 94–101)

将**半空间**问题（PEC/PMC接地平面上方的源）通过放置镜像源转化为**自由空间**问题。

### 3.2.1 Basic Image Rules | 基本镜像规则

| Source type / 源类型 | Above PEC ($\hat{n}\times\mathbf{E}=0$) / PEC上方 | Above PMC ($\hat{n}\times\mathbf{H}=0$) / PMC上方 |
|---|---|---|
| 垂直电偶极子 | 同方向 | 反方向 |
| 水平电偶极子 | 反方向 | 同方向 |
| 垂直磁偶极子 | 反方向 | 同方向 |
| 水平磁偶极子 | 同方向 | 反方向 |

For an **arbitrary electric current** $\mathbf{J}(\mathbf{r})$ above an electric ground plane ($z=0$) / 对于电接地平面 ($z=0$) 上方的**任意电流** $\mathbf{J}(\mathbf{r})$：

$$
\mathbf{J}_{\text{im}}(\mathbf{r}) = 2\hat{z}\hat{z}\!\cdot\!\mathbf{J}(\mathbf{r}_i) - \mathbf{J}(\mathbf{r}_i),
\qquad \mathbf{r}_i = x\hat{x} + y\hat{y} - z\hat{z}.
$$

Likewise for **magnetic current** $\mathbf{M}(\mathbf{r})$ / 对**磁流** $\mathbf{M}(\mathbf{r})$ 类似：

$$
\mathbf{M}_{\text{im}}(\mathbf{r}) = -2\hat{z}\hat{z}\!\cdot\!\mathbf{M}(\mathbf{r}_i) + \mathbf{M}(\mathbf{r}_i).
$$

### Example 3.3 — Images Between Two Parallel Conducting Planes | 两平行导体板间的镜像

对于 $x = d$ 处电流元 $Il\hat{u}$ 位于 $x=0$ 和 $x=l$ 两PEC板之间，需要两套无穷镜像集：

- 同方向镜像在 $x = 2il + d$ ($-\infty < i < \infty$)
- 反方向镜像在 $x = 2jl - d$, 且 $\hat{u}_{\text{im}} = 2\hat{x}\hat{x}\!\cdot\!\hat{u} - \hat{u}$

场为：

$$
\mathbf{E}(\mathbf{r}) = -j\omega\mu Il\Bigl[\sum_{i=-\infty}^{\infty} \mathbf{G}_{e0}(\mathbf{r},\mathbf{r}_i)\cdot\hat{u}
+ \sum_{j=-\infty}^{\infty} \mathbf{G}_{e0}(\mathbf{r},\mathbf{r}_j)\cdot\hat{u}_{\text{im}}\Bigr],
\quad 0 \le x \le l.
$$

### 3.2.2 Half-Space Dyadic Green's Functions | 半空间并矢格林函数

对于 $z=0$ 处的PEC接地平面（$\mathbf{r}'_i = x'\hat{x} + y'\hat{y} - z'\hat{z}$）：

**电场**：

$$
\mathbf{E}(\mathbf{r}) = -j\omega\mu \int_V \mathbf{G}_{e1}(\mathbf{r},\mathbf{r}') \cdot \mathbf{J}(\mathbf{r}')\,dV'
- \int_V \mathbf{G}_{m1}(\mathbf{r},\mathbf{r}') \cdot \mathbf{M}(\mathbf{r}')\,dV',
$$

其中

$$
\begin{aligned}
\mathbf{G}_{e1}(\mathbf{r},\mathbf{r}') &= \Bigl(\mathbf{I} - \frac{1}{k^2}\nabla'\nabla\Bigr)
[G_0(\mathbf{r},\mathbf{r}') - G_0(\mathbf{r},\mathbf{r}'_i)] + 2\hat{z}\hat{z}\,G_0(\mathbf{r},\mathbf{r}'_i), \\[4pt]
\mathbf{G}_{m1}(\mathbf{r},\mathbf{r}') &= -\nabla'[G_0(\mathbf{r},\mathbf{r}') + G_0(\mathbf{r},\mathbf{r}'_i)] \times \mathbf{I}.
\end{aligned}
$$

**磁场**：

$$
\mathbf{H}(\mathbf{r}) = \int_V \mathbf{G}_{m2}(\mathbf{r},\mathbf{r}') \cdot \mathbf{J}(\mathbf{r}')\,dV'
- j\omega\epsilon \int_V \mathbf{G}_{e2}(\mathbf{r},\mathbf{r}') \cdot \mathbf{M}(\mathbf{r}')\,dV',
$$

其中

$$
\begin{aligned}
\mathbf{G}_{e2}(\mathbf{r},\mathbf{r}') &= \Bigl(\mathbf{I} - \frac{1}{k^2}\nabla'\nabla\Bigr)
[G_0(\mathbf{r},\mathbf{r}') + G_0(\mathbf{r},\mathbf{r}'_i)] - 2\hat{z}\hat{z}\,G_0(\mathbf{r},\mathbf{r}'_i), \\[4pt]
\mathbf{G}_{m2}(\mathbf{r},\mathbf{r}') &= -\nabla'[G_0(\mathbf{r},\mathbf{r}') - G_0(\mathbf{r},\mathbf{r}'_i)] \times \mathbf{I}.
\end{aligned}
$$

---

## 3.3 Reciprocity Theorems | 互易定理 (pp. 101–106)

关联同一（互易）媒质中两组独立源产生的两个独立电磁场。

### 3.3.1 General Reciprocity Theorem | 一般互易定理

$$
\boxed{\nabla\cdot(\mathbf{H}_2 \times \mathbf{E}_1 - \mathbf{H}_1 \times \mathbf{E}_2)
= \mathbf{E}_1\!\cdot\!\mathbf{J}_2 + \mathbf{H}_2\!\cdot\!\mathbf{M}_1 - \mathbf{E}_2\!\cdot\!\mathbf{J}_1 - \mathbf{H}_1\!\cdot\!\mathbf{M}_2}
$$

体积 $V$（边界 $S$）上的积分形式：

$$
\boxed{\oint_S (\mathbf{H}_2 \times \mathbf{E}_1 - \mathbf{H}_1 \times \mathbf{E}_2)\cdot d\mathbf{S}
= \int_V (\mathbf{E}_1\!\cdot\!\mathbf{J}_2 + \mathbf{H}_2\!\cdot\!\mathbf{M}_1 - \mathbf{E}_2\!\cdot\!\mathbf{J}_1 - \mathbf{H}_1\!\cdot\!\mathbf{M}_2)\,dV}.
$$

当 $\bm{\epsilon}, \bm{\mu}, \bm{\sigma}$ 张量**对称**（互易媒质）时成立。

### 3.3.2 Lorentz Reciprocity Theorem | 洛伦兹互易定理

在**无源**区域或包含**所有**源的表面上：

$$
\nabla\cdot(\mathbf{H}_2 \times \mathbf{E}_1 - \mathbf{H}_1 \times \mathbf{E}_2) = 0,
\qquad
\oint_S (\mathbf{H}_2 \times \mathbf{E}_1 - \mathbf{H}_1 \times \mathbf{E}_2) \cdot d\mathbf{S} = 0.
$$

### 3.3.3 Rayleigh–Carson Reciprocity Theorem (Reaction Concept) | 瑞利–卡森互易定理（反应概念）

Define **reaction** of field "1" on source "2" / 定义场"1"对源"2"的**反应**：

$$
\langle 1,2 \rangle \equiv \int_V (\mathbf{E}_1\!\cdot\!\mathbf{J}_2 - \mathbf{H}_1\!\cdot\!\mathbf{M}_2)\,dV.
$$

Then / 则：

$$
\boxed{\langle 1,2 \rangle = \langle 2,1 \rangle}.
$$

**关键推论**：PEC表面的切向电流**不**辐射。

**天线应用**：辐射方向图等于接收方向图。这意味着天线发射和接收特性相同——一个基本的节省时间的设计原理。

### Example 3.4 — Aperture Radiation via Reciprocity | 通过互易定理分析口径辐射

PEC平面上 $a \times b$ 矩形口径，口径场 $\mathbf{E}_a = \hat{y}E_0\cos(\pi x/a)$，远场 ($r,\theta,\phi$)：

$$
\begin{aligned}
E_{2\theta} &= j\frac{2aE_0}{r}\,e^{-jkr}\,
\frac{\cos\!\bigl(\frac{ka}{2}\sin\theta\cos\phi\bigr)
      \sin\!\bigl(\frac{kb}{2}\sin\theta\sin\phi\bigr)}
     {[\pi^2 - (ka\sin\theta\cos\phi)^2]\,\sin\theta}, \\[6pt]
E_{2\phi} &= j\frac{2aE_0}{r}\,e^{-jkr}\,
\frac{\cos\!\bigl(\frac{ka}{2}\sin\theta\cos\phi\bigr)
      \sin\!\bigl(\frac{kb}{2}\sin\theta\sin\phi\bigr)}
     {[\pi^2 - (ka\sin\theta\cos\phi)^2]\,\tan\theta\tan\phi}.
\end{aligned}
$$

---

## 3.4 Equivalence Principles | 等效原理 (pp. 107–119)

### 3.4.1 Surface Equivalence Principle (Huygens' Principle) | 表面等效原理（惠更斯原理）

For any closed surface $S$ separating interior from exterior, the exterior field can be reproduced by placing **equivalent surface currents** on $S$ / 对于分隔内部和外部的任意封闭曲面 $S$，在 $S$ 上放置**等效面电流**可重现外部场：

$$
\mathbf{J}_s = \hat{n} \times (\mathbf{H} - \mathbf{H}'), \qquad
\mathbf{M}_s = (\mathbf{E} - \mathbf{E}') \times \hat{n}.
$$

**Love's equivalence / 乐甫等效** (zero interior field $\mathbf{E}' = \mathbf{H}' = 0$):

$$
\mathbf{J}_s = \hat{n} \times \mathbf{H}, \qquad
\mathbf{M}_s = \mathbf{E} \times \hat{n}.
$$

If the interior is filled with PEC, only $\mathbf{M}_s = \mathbf{E} \times \hat{n}$ radiates / 若内部填充PEC，仅 $\mathbf{M}_s = \mathbf{E} \times \hat{n}$ 辐射。If filled with PMC, only $\mathbf{J}_s = \hat{n} \times \mathbf{H}$ radiates / 若填充PMC，仅 $\mathbf{J}_s = \hat{n} \times \mathbf{H}$ 辐射。

### 3.4.2 Scattering by a Conducting Object — Physical Optics (PO) | 导体散射——物理光学法 (PO)

For a PEC object, the scattered field is / 对于PEC目标，散射场为：

$$
\mathbf{E}^{\text{sc}}(\mathbf{r}) = -j\omega\mu \oint_S \mathbf{G}_{e0}(\mathbf{r},\mathbf{r}')
\cdot [\hat{n}' \times \mathbf{H}(\mathbf{r}')]\,dS'.
$$

**PO approximation / PO近似** (large, smooth PEC / 大而光滑的PEC):

$$
\mathbf{J}_s \approx \begin{cases}
2\hat{n} \times \mathbf{H}^{\text{inc}} & \text{on illuminated side / 照亮侧}, \\
0 & \text{on shadow side / 阴影侧}.
\end{cases}
$$

**Induction theorem / 感应定理**: $\mathbf{M}_s = \hat{n} \times \mathbf{E}^{\text{inc}}$ 在PEC表面；对大型物体使用镜像原理。

### Example 3.5 — PO for Circular Conducting Plate | 圆导体板的PO

入射 $\mathbf{E}^{\text{inc}} = \hat{x}E_0 e^{jk_0z}$，半径 $a$：

$$
\mathbf{E}^{\text{sc}} \approx -\frac{jaE_0}{r\sin\theta}\,J_1(k_0 a\sin\theta)\,e^{-jk_0r}
(\hat{\theta}\cos\theta\cos\phi - \hat{\phi}\sin\phi).
$$

### Example 3.6 — Induction Theorem for Circular Plate | 圆板的感应定理

相同几何，使用 $\mathbf{M}_s$ 经镜像加倍：

$$
\mathbf{E}^{\text{sc}} \approx -\frac{jaE_0}{r\sin\theta}\,J_1(k_0 a\sin\theta)\,e^{-jk_0r}
(\hat{\theta}\cos\phi - \hat{\phi}\cos\theta\sin\phi).
$$

两种结果在前向/后向方向上一致，但在角度方向图上有差异。

### 3.4.3 Scattering by a Dielectric Object | 介质体散射

Two coupled surface integral equations (PMCHWT formulation) using equivalent currents / 使用等效电流 $\mathbf{J}_s = \hat{n}\times\mathbf{H}$, $\mathbf{M}_s = \mathbf{E}\times\hat{n}$ 的两个耦合表面积分方程（PMCHWT公式）。

### 3.4.4 Volume Equivalence Principle & Born Approximation | 体等效原理与玻恩近似

Replace object by equivalent **volume currents** / 将目标替换为等效**体电流**：

$$
\mathbf{J}_{\text{eq}} = j\omega[\tilde{\epsilon}(\mathbf{r}) - \epsilon]\,\mathbf{E},
\qquad
\mathbf{M}_{\text{eq}} = j\omega[\tilde{\mu}(\mathbf{r}) - \mu]\,\mathbf{H}.
$$

First-order **Born approximation** (weak scatterer) / 一阶**玻恩近似**（弱散射体）：

$$
\mathbf{E}(\mathbf{r}) \approx \mathbf{E}^{\text{inc}}(\mathbf{r})
+ \omega^2\mu \int_{V_o} \mathbf{G}_{e0}(\mathbf{r},\mathbf{r}')
  \cdot (\tilde{\epsilon}-\epsilon)\,\mathbf{E}^{\text{inc}}(\mathbf{r}')\,dV'.
$$

### Example 3.7 — Rayleigh Scattering by Small Dielectric Sphere | 小介质球的瑞利散射

$ka \ll 1$, $\epsilon_r$, $\mathbf{E}^{\text{inc}} = \hat{x}E_0 e^{-jk_0z}$：

$$
\mathbf{E}^{\text{int}} \approx \hat{x}\,\frac{3}{\epsilon_r+2}\,E_0,
\qquad
E^{\text{sc}} \propto k_0^2 a^3\,\frac{\epsilon_r-1}{\epsilon_r+2}\,E_0\,\frac{e^{-jk_0r}}{r}.
$$

Scattered power $\propto 1/\lambda_0^4$ — Rayleigh scattering (blue sky) / 散射功率 $\propto 1/\lambda_0^4$ — 瑞利散射（蓝天）。

---

## 3.5 Duality Principle | 对偶原理 (pp. 120–121)

Swap variables in Maxwell's equations / 交换麦克斯韦方程组中的变量：

$$
\mathbf{E} \to \mathbf{H},\quad
\mathbf{H} \to -\mathbf{E},\quad
\mathbf{J} \to \mathbf{M},\quad
\mathbf{M} \to -\mathbf{J},\quad
\epsilon \to \mu,\quad
\mu \to \epsilon,\quad
\mathbf{A} \to \mathbf{F},\quad
\mathbf{F} \to -\mathbf{A}.
$$

Normalized form (preserving $\eta = \sqrt{\mu/\epsilon}$) / 归一化形式（保持 $\eta = \sqrt{\mu/\epsilon}$）：

$$
\mathbf{E} \to \eta\mathbf{H},\quad
\mathbf{H} \to -\mathbf{E}/\eta,\quad
\mathbf{J} \to \mathbf{M}/\eta,\quad
\mathbf{M} \to -\eta\mathbf{J}.
$$

**核心意义**：工作量减半——解出一个问题，免费得到另一个。

---

## 3.6 Aperture Radiation and Scattering | 口径辐射与散射 (pp. 121–128)

### 3.6.1 Equivalent Problems | 等效问题

For a PEC screen with an aperture / 对于带有口径的PEC屏：
1. Seal aperture with PEC → form ground plane / 用PEC密封口径 → 形成接地平面。
2. Replace aperture field by $\mathbf{M}_s = \mathbf{E}\times\hat{n}$ over aperture / 用 $\mathbf{M}_s = \mathbf{E}\times\hat{n}$ 替换口径上的场。
3. Image theory → $\mathbf{M}_s = 2\mathbf{E}\times\hat{n}$ radiating in free space / 镜像原理 → $\mathbf{M}_s = 2\mathbf{E}\times\hat{n}$ 在自由空间中辐射。

**矩形波导开口** ($a\times b$, TE$_{10}$ 模)：

$$
\begin{aligned}
E_\theta &= j\frac{2aE_0}{r}e^{-jkr}\,
\frac{\cos\!\bigl(\frac{ka}{2}\sin\theta\cos\phi\bigr)
      \sin\!\bigl(\frac{kb}{2}\sin\theta\sin\phi\bigr)}
     {[\pi^2 - (ka\sin\theta\cos\phi)^2]\,\sin\theta}, \\[4pt]
E_\phi &= j\frac{2aE_0}{r}e^{-jkr}\,
\frac{\cos\!\bigl(\frac{ka}{2}\sin\theta\cos\phi\bigr)
      \sin\!\bigl(\frac{kb}{2}\sin\theta\sin\phi\bigr)}
     {[\pi^2 - (ka\sin\theta\cos\phi)^2]\,\tan\theta\tan\phi}.
\end{aligned}
$$

### 3.6.2 Babinet's Principle | 巴俾涅原理

For an apertured PEC screen and its complementary PMC plate / 对于带口径的PEC屏及其互补PMC板：

$$
\mathbf{E}_a + \mathbf{E}_m = \mathbf{E}^{\text{inc}},\qquad
\mathbf{H}_a + \mathbf{H}_m = \mathbf{H}^{\text{inc}}.
$$

Via duality (PMC → PEC plus dual source) / 通过对偶性（PMC → PEC 加对偶源）：

$$
\mathbf{E}_a + \eta\mathbf{H}_d = \mathbf{E}^{\text{inc}},\qquad
\mathbf{H}_a - \frac{\mathbf{E}_d}{\eta} = \mathbf{H}^{\text{inc}}.
$$

### 3.6.3 Complementary Antennas | 互补天线

For two complementary planar structures / 两个互补平面结构：

$$
\boxed{Z_a Z_c = \frac{\eta^2}{4}}.
$$

A **self-complementary** antenna has $Z_a = Z_c = \eta/2$ — constant input impedance (wideband antennas: log-periodic, spiral) / **自互补**天线的 $Z_a = Z_c = \eta/2$ — 恒定输入阻抗（宽带天线：对数周期、螺旋）。

---

## Key Formulas Summary | 关键公式汇总

| Concept / 概念 | Formula / 公式 |
|---|---|
| Uniqueness condition / 唯一性条件 | Specify $\hat{n}\times\mathbf{E}$ or $\hat{n}\times\mathbf{H}$ on $S$ |
| Image (PEC, arbitrary $\mathbf{J}$) / 镜像 | $\mathbf{J}_{\text{im}} = 2\hat{z}\hat{z}\!\cdot\!\mathbf{J}(\mathbf{r}_i) - \mathbf{J}(\mathbf{r}_i)$ |
| General Reciprocity / 一般互易 | $\nabla\cdot(\mathbf{H}_2\times\mathbf{E}_1 - \mathbf{H}_1\times\mathbf{E}_2) = \mathbf{E}_1\!\cdot\!\mathbf{J}_2 + \mathbf{H}_2\!\cdot\!\mathbf{M}_1 - \mathbf{E}_2\!\cdot\!\mathbf{J}_1 - \mathbf{H}_1\!\cdot\!\mathbf{M}_2$ |
| Rayleigh–Carson / 瑞利–卡森 | $\langle 1,2 \rangle = \langle 2,1 \rangle$ |
| Love's Equivalence / 乐甫等效 | $\mathbf{J}_s = \hat{n}\times\mathbf{H},\; \mathbf{M}_s = \mathbf{E}\times\hat{n}$ |
| PO approximation / PO近似 | $\mathbf{J}_s \approx 2\hat{n}\times\mathbf{H}^{\text{inc}}$ (lit side / 照亮侧) |
| Volume equivalence / 体等效 | $\mathbf{J}_{\text{eq}} = j\omega(\tilde{\epsilon}-\epsilon)\mathbf{E}$ |
| Complement. antennas / 互补天线 | $Z_a Z_c = \eta^2/4$ |

---

## Figures Generated / 生成的图表

| File / 文件 | Description / 描述 |
|---|---|
| `ex35_po_pattern.png` | PO: 圆板辐射方向图 |
| `ex35_po_cuts.png` | PO: E/H面切面 |
| `ex35_po_map.png` | PO: 方向图色彩图 |
| `ex35_vs_ex36_compare.png` | PO与感应定理对比 |
| `ex36_induction_pattern.png` | 感应定理辐射方向图 |
| `ex36_induction_cuts.png` | 感应定理切面 |
| `ex36_aperture_pattern.png` | 矩形口径方向图 |
| `ex36_aperture_cuts.png` | 口径E/H面切面 |
| `ex37_rayleigh_pattern.png` | 瑞利球方向图 |
| `ex37_rayleigh_map.png` | 瑞利球色彩图 |
| `ex37_rayleigh_sweep.png` | 瑞利 $\sigma$ vs. 频率扫描 |
