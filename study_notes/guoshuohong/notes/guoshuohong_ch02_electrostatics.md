# 郭硕鸿《电动力学》 第02章：静电学

> **来源：** 谢处方等，《电磁场与电磁波》，第02章
> **提取方式：** 📷 扫描PDF → OCR → 人工清洗

---

## 02.1 静电学 | Electrostatics

# 第二章 静电场
> 郭硕鸿《电动力学》
---
## §2.1 静电场的标势及其微分方程
### 静电场的无旋性与标势
静电场满足：
$$
\nabla \times \mathbf{E} = 0
$$
因此电场可以表示为标势的梯度：
$$
\mathbf{E} = -\nabla $\varphi$
$$
积分形式：$\oint \mathbf{E} \cdot \mathrm{d}\mathbf{l} = 0$
### 电势差
两点间的电势差等于电场力移动单位电荷所做的功：
$$
$\varphi$($\mathbf{P}$_2) - $\varphi$($\mathbf{P}$_1) = -\int_{$\mathbf{P}$_1}^{$\mathbf{P}$_2} \mathbf{E} \cdot \mathrm{d}\mathbf{l}
$$
取无穷远处为零势点：
$$
$\varphi$($\mathbf{P}$) = \int_$\mathbf{P}$^{\infty} \mathbf{E} \cdot \mathrm{d}\mathbf{l}
$$
### Poisson 方程与 Laplace 方程
由 Gauss 定律 $\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}$ 和 $\mathbf{E} = -\nabla\varphi$ 得：
$$
\boxed{\nabla^2 \varphi = -\frac{\rho}{\varepsilon_0}} \quad \text{(Poisson 方程)}
$$
无电荷区域 ($\rho = 0$)：
$$
\boxed{\nabla^2 \varphi = 0} \quad \text{(Laplace 方程)}
$$
### 边值关系
在两种介质的分界面上，电势满足：
**电势连续：**
$$
\varphi_1 = \varphi_2
$$
**法向导数的跃变：**
$$
\varepsilon_1 \frac{\partial \varphi_1}{\partial n} - \varepsilon_2 \frac{\partial \varphi_2}{\partial n} = \sigma_f
$$
其中 $\sigma_f$ 为自由面电荷密度。对于导体表面：
$$
\frac{\partial \varphi}{\partial n} = -\frac{\sigma_f}{\varepsilon_0}
$$
---
## §2.2 唯一性定理
### 静电学中的边值问题
求解区域 $V$ 内满足 Poisson 方程或 Laplace 方程，在边界 $S$ 上满足给定边界条件。
### 唯一性定理的表述
> 设区域 $V$ 内有给定的电荷分布 $\rho$，边界 $S$ 上给定：
> 1. **Dirichlet 边界条件**：$$\varphi$|_$\mathbf{S}$ = f(\mathbf{x})$（电势值）
> 2. **Neumann 边界条件**：$\left.\frac{\partial \varphi}{\partial n}\right|_$\mathbf{S}$ = g(\mathbf{x})$（电势法向导数）
>
> 则 $V$ 内的电场分布是 **唯一确定** 的。
### 证明要点
设两个解 $\varphi_1$ 和 $\varphi_2$ 满足相同的方程和边界条件，令 $\psi = \varphi_1 - \varphi_2$，则：
$$
\nabla^2 \psi = 0
$$
利用 Green 第一恒等式：
$$
\int_V |\nabla$\psi$|^2 \,\mathrm{d}V = \oint_$\mathbf{S}$ \psi \frac{\partial\psi}{\partial n} \,\mathrm{d}$\mathbf{S}$
$$
- Dirichlet: $$\psi$|_$\mathbf{S}$ = 0 \Rightarrow \nabla\psi = 0 \Rightarrow \psi$ 为常数
- Neumann: $\left.\frac{\partial\psi}{\partial n}\right|_$\mathbf{S}$ = 0 \Rightarrow$ 同样得 $\nabla\psi = 0$
因此 $\varphi_1 - \varphi_2 = \text{const}$，电场相同。
### 重要推论
- 唯一性定理为 **镜像法**、**分离变量法** 等提供了理论基础
- 只需找到一个满足方程和边界条件的解，它一定是正确的解
---
## §2.3 拉普拉斯方程 分离变量法
### 2.3.1 直角坐标系
Laplace 方程在直角坐标系中：
$$
\frac{\partial^2 \varphi}{\partial x^2} + \frac{\partial^2 \varphi}{\partial y^2} + \frac{\partial^2 \varphi}{\partial z^2} = 0
$$
分离变量：$$\varphi$(x, y, z) = X(x)Y(y)Z(z)$
代入得：
$$
\frac{X''}{X} + \frac{Y''}{Y} + \frac{Z''}{Z} = 0
$$
设分离常数：
$$
\frac{X''}{X} = -$\alpha$^2, \quad \frac{Y''}{Y} = -$\beta$^2, \quad \frac{Z''}{Z} = $\alpha$^2 + $\beta$^2 = $\gamma$^2
$$
典型解形式：
$$
X(x) \sim \sin(\alpha x), \cos(\alpha x) \quad \text{或} \quad e^{i\alpha x}
$$
$$
Y(y) \sim \sin(\beta y), \cos(\beta y) \quad \text{或} \quad e^{i\beta y}
$$
$$
Z(z) \sim \sinh(\gamma z), \cosh(\gamma z) \quad \text{或} \quad e^{\pm\gamma z}
$$
实际解由边界条件决定特定函数形式。
### 2.3.2 球坐标系
球坐标系 $(r, $\theta$, \phi)$ 的 Laplace 方程：
$$
\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial\varphi}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\left(\sin$\theta$\frac{\partial\varphi}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2\varphi}{\partial\phi^2} = 0
$$
分离变量：$$\varphi$(r, $\theta$, \phi) = R(r)\Theta($\theta$)\Phi(\phi)$
**径向部分：**
$$
\frac{\mathrm{d}}{\mathrm{d}r}\left(r^2\frac{\mathrm{d}R}{\mathrm{d}r}\right) - l(l+1)R = 0
$$
解为：
$$
R(r) = $\mathbf{A}$_l r^l + $\mathbf{B}$_l r^{-(l+1)}
$$
**角度部分：** 球谐函数 $Y_{lm}($\theta$, \phi)$
$$
\nabla^2_\Omega Y_{lm} = -l(l+1)Y_{lm}
$$
其中 $Y_{lm}($\theta$, \phi) = N_{lm} $\mathbf{P}$_l^m(\cos$\theta$) e^{im\phi}$
- $l = 0, 1, 2, \dots$（角量子数）
- $m = -l, -l+1, \dots, l$（磁量子数）
- $$\mathbf{P}$_l^m$ 为缔合 Legendre 多项式
**一般解：**
$$
\boxed{$\varphi$(r, $\theta$, \phi) = \sum_{l=0}^{\infty}\sum_{m=-l}^{l} \left($\mathbf{A}$_{lm} r^l + $\mathbf{B}$_{lm} r^{-(l+1)}\right) Y_{lm}($\theta$, \phi)}
$$
### 2.3.3 柱坐标系
柱坐标系 $($\rho$, \phi, z)$ 的 Laplace 方程：
$$
\frac{1}{\rho}\frac{\partial}{\partial\rho}\left($\rho$\frac{\partial\varphi}{\partial\rho}\right) + \frac{1}{$\rho$^2}\frac{\partial^2\varphi}{\partial\phi^2} + \frac{\partial^2\varphi}{\partial z^2} = 0
$$
分离变量：$$\varphi$($\rho$, \phi, z) = R($\rho$)\Phi(\phi)Z(z)$
**轴向：** $Z'' - $\mathbf{k}$^2 Z = 0 \Rightarrow Z(z) \sim e^{\pm kz}$
**角向：** $\Phi'' + m^2\Phi = 0 \Rightarrow \Phi(\phi) \sim e^{im\phi}$
**径向：** Bessel 方程：
$$
$\rho$^2 R'' + \rho R' + ($\mathbf{k}$^2$\rho$^2 - m^2)R = 0
$$
解为 Bessel 函数 $$\mathbf{J}$_m(k$\rho$)$ 和 Neumann 函数 $N_m(k$\rho$)$（或修正 Bessel 函数 $I_m(k$\rho$), K_m(k$\rho$)$）
---
## §2.4 镜像法
### 基本原理
用假想的 **镜像电荷** 代替边界的影响，使原问题转化为无界空间中的简单问题。
### 2.4.1 导体平面
点电荷 $q$ 位于接地导体平面上方 $h$ 处：
- 镜像电荷：$-q$ 位于导体平面下方 $h$ 处
- 空间中电势：
$$
$\varphi$(x, y, z) = \frac{q}{4$\pi$\varepsilon_0} \left(\frac{1}{\sqrt{x^2+y^2+(z-h)^2}} - \frac{1}{\sqrt{x^2+y^2+(z+h)^2}}\right)
$$
- 导体表面感应电荷密度：
$$
\sigma = -\varepsilon_0 \left.\frac{\partial\varphi}{\partial z}\right|_{z=0} = -\frac{qh}{2$\pi$(x^2+y^2+h^2)^{3/2}}
$$
- 总感应电荷：$-q$
### 2.4.2 导体球
点电荷 $q$ 位于接地导体球（半径 $R_0$）外距离球心 $d$ 处：
- 镜像电荷大小和位置：
$$
q' = -\frac{R_0}{d}q, \quad d' = \frac{R_0^2}{d}
$$
- 空间中电势：
$$
$\varphi$(\mathbf{r}) = \frac{q}{4$\pi$\varepsilon_0}\left(\frac{1}{|\mathbf{r} - d\hat{\mathbf{z}}|} - \frac{R_0/d}{|\mathbf{r} - (R_0^2/d)\hat{\mathbf{z}}|}\right)
$$
对于 **导体球不接地且带总电荷 Q**：
$$
$\varphi$(\mathbf{r}) = \frac{q}{4$\pi$\varepsilon_0}\left(\frac{1}{|\mathbf{r} - d\hat{\mathbf{z}}|} - \frac{R_0/d}{|\mathbf{r} - (R_0^2/d)\hat{\mathbf{z}}|}\right) + \frac{Q+q'}{4$\pi$\varepsilon_0|\mathbf{r}|}
$$
### 2.4.3 电介质平面
点电荷 $q$ 位于介电常数 $\varepsilon_1$ 的介质中，距平面 $h$，另一侧介质为 $\varepsilon_2$：
**上半空间 ($z > 0$)：**
$$
\varphi_1 = \frac{q}{4$\pi$\varepsilon_1}\left(\frac{1}{\sqrt{x^2+y^2+(z-h)^2}} + \frac{\varepsilon_1-\varepsilon_2}{\varepsilon_1+\varepsilon_2}\frac{1}{\sqrt{x^2+y^2+(z+h)^2}}\right)
$$
**下半空间 ($z < 0$)：**
$$
\varphi_2 = \frac{q}{4$\pi$\varepsilon_1}\cdot\frac{2\varepsilon_2}{\varepsilon_1+\varepsilon_2}\frac{1}{\sqrt{x^2+y^2+(z-h)^2}}
$$
实际上是用等效镜像电荷满足边界条件。
---
## §2.5 格林函数法
### 格林函数定义
Green 函数 $G(\mathbf{r}, \mathbf{r}')$ 满足：
$$
\nabla^2 G(\mathbf{r}, \mathbf{r}') = -\frac{1}{\varepsilon_0}$\delta$(\mathbf{r} - \mathbf{r}')
$$
物理意义：位于 $\mathbf{r}'$ 的单位点电荷产生的电势。
### 无界空间 Green 函数
$$
G_0(\mathbf{r}, \mathbf{r}') = \frac{1}{4$\pi$\varepsilon_0}\frac{1}{|\mathbf{r} - \mathbf{r}'|}
$$
### 边值问题的 Green 函数解
利用 Green 第二恒等式，可得任意电荷分布 $$\rho$(\mathbf{r}')$ 在区域 $V$ 内的电势：
$$
$\varphi$(\mathbf{r}) = \int_V G(\mathbf{r}, \mathbf{r}')$\rho$(\mathbf{r}')\,\mathrm{d}V' - \varepsilon_0\oint_$\mathbf{S}$ \left[G(\mathbf{r}, \mathbf{r}')\frac{\partial$\varphi$(\mathbf{r}')}{\partial n'} - $\varphi$(\mathbf{r}')\frac{\partial G(\mathbf{r}, \mathbf{r}')}{\partial n'}\right]\mathrm{d}$\mathbf{S}$'
$$
### Dirichlet Green 函数
若 $G_$\mathbf{D}$(\mathbf{r}, \mathbf{r}')$ 满足 $G_$\mathbf{D}$|_$\mathbf{S}$ = 0$，则：
$$
$\varphi$(\mathbf{r}) = \int_V G_$\mathbf{D}$(\mathbf{r}, \mathbf{r}')$\rho$(\mathbf{r}')\,\mathrm{d}V' - \varepsilon_0\oint_$\mathbf{S}$ $\varphi$(\mathbf{r}')\frac{\partial G_$\mathbf{D}$(\mathbf{r}, \mathbf{r}')}{\partial n'}\,\mathrm{d}$\mathbf{S}$'
$$
### Neumann Green 函数
若 $\left.\frac{\partial G_N}{\partial n'}\right|_$\mathbf{S}$ = -\frac{1}{S}$，则：
$$
$\varphi$(\mathbf{r}) = \int_V G_N(\mathbf{r}, \mathbf{r}')$\rho$(\mathbf{r}')\,\mathrm{d}V' + \varepsilon_0\oint_$\mathbf{S}$ G_N(\mathbf{r}, \mathbf{r}')\frac{\partial$\varphi$(\mathbf{r}')}{\partial n'}\,\mathrm{d}$\mathbf{S}$' + \langle$\varphi$\rangle_$\mathbf{S}$
$$
### 本征函数展开法求 Green 函数
Green 函数可按本征函数展开：
$$
G(\mathbf{r}, \mathbf{r}') = \sum_n \frac{u_n(\mathbf{r})u_n^*(\mathbf{r}')}{\lambda_n}
$$
其中 $u_n$ 是 $\nabla^2 u + \lambda u = 0$ 的本征函数。
---
## §2.6 电多极矩
### 多极展开
对于局域在原点附近的电荷分布 $$\rho$(\mathbf{r}')$，远处 $r \gg r'$ 的电势可展开为：
$$
$\varphi$(\mathbf{r}) = \frac{1}{4$\pi$\varepsilon_0} \left[\frac{Q}{r} + \frac{\mathbf{p}\cdot\hat{\mathbf{r}}}{r^2} + \frac{1}{2}\sum_{i,j} Q_{ij}\frac{x_i x_j}{r^5} + \cdots\right]
$$
### 2.6.1 总电荷（单极矩）
$$
Q = \int $\rho$(\mathbf{r}')\,\mathrm{d}V'
$$
### 2.6.2 电偶极矩
$$
\boxed{\mathbf{p} = \int \mathbf{r}' $\rho$(\mathbf{r}')\,\mathrm{d}V'}
$$
对于点电荷系：$\mathbf{p} = \sum_i q_i \mathbf{r}_i'$
**偶极子的电势：**
$$
\varphi_{\text{dip}}(\mathbf{r}) = \frac{1}{4$\pi$\varepsilon_0}\frac{\mathbf{p}\cdot\hat{\mathbf{r}}}{r^2}
$$
**偶极子的电场：**
$$
\mathbf{E}_{\text{dip}}(\mathbf{r}) = \frac{1}{4$\pi$\varepsilon_0}\left[\frac{3(\mathbf{p}\cdot\hat{\mathbf{r}})\hat{\mathbf{r}} - \mathbf{p}}{r^3}\right]
$$
### 2.6.3 电四极矩
电四极矩张量（无迹化定义）：
$$
\boxed{Q_{ij} = \int \left(3x_i' x_j' - r'^2\delta_{ij}\right)$\rho$(\mathbf{r}')\,\mathrm{d}V'}
$$
性质：$Q_{ij}$ 是对称无迹张量：$Q_{ij} = Q_{ji},\ \sum_i Q_{ii} = 0$，有 5 个独立分量。
对于点电荷系：$Q_{ij} = \sum_a q_a (3x_{a,i} x_{a,j} - r_a^2\delta_{ij})$
**四极子电势：**
$$
\varphi_{\text{quad}}(\mathbf{r}) = \frac{1}{8$\pi$\varepsilon_0}\sum_{i,j} \frac{Q_{ij} x_i x_j}{r^5}
$$
### 2.6.4 电荷分布在外场中的能量
**多极展开：**
$$
W = \int $\rho$(\mathbf{r})\varphi_{\text{ext}}(\mathbf{r})\,\mathrm{d}V = q\varphi_{\text{ext}}\tag{0} - \mathbf{p}\cdot\mathbf{E}_{\text{ext}}\tag{0} - \frac{1}{6}\sum_{i,j} Q_{ij}\frac{\partial $\mathbf{E}$_{\text{ext}, i}}{\partial x_j}\tag{0} + \cdots
$$
### 常见电荷分布的多极矩
| 系统 | 单极矩 | 偶极矩 | 四极矩 (非零) |
|------|--------|--------|---------------|
| 点电荷 $q$ 于原点 | $q$ | $0$ | $0$ |
| 电偶极子 $\pm q$ 相距 $d$ | $0$ | $qd$ | $0$ |
| 两对偶极子 | $0$ | $0$ | 非零 |
| 均匀带电球 | $Q$ | $0$ | $0$ |
---
## 核心公式速查
| 内容 | 公式 |
|------|------|
| Poisson 方程 | $\nabla^2 \varphi = -$\rho$/\varepsilon_0$ |
| 电场与电势 | $\mathbf{E} = -\nabla\varphi$ |
| 边值条件 | $\varphi_1 = \varphi_2,\ \varepsilon_1\frac{\partial\varphi_1}{\partial n} - \varepsilon_2\frac{\partial\varphi_2}{\partial n} = \sigma_f$ |
| Laplace 方程（球坐标） | $\varphi = \sum ($\mathbf{A}$_l r^l + $\mathbf{B}$_l r^{-l-1})$\mathbf{P}$_l(\cos$\theta$)$ |
| 镜像法（导体球） | $q' = -(R_0/d)q,\ d' = R_0^2/d$ |
| 偶极子电势 | $\varphi = \frac{\mathbf{p}\cdot\hat{\mathbf{r}}}{4$\pi$\varepsilon_0 r^2}$ |
| 偶极子电场 | $\mathbf{E} = \frac{3(\mathbf{p}\cdot\hat{\mathbf{r}})\hat{\mathbf{r}} - \mathbf{p}}{4$\pi$\varepsilon_0 r^3}$ |
| 四极矩 | $Q_{ij} = \int (3x_i x_j - r^2\delta_{ij})$\rho$\,\mathrm{d}V$ |
---
*笔记生成于 2026-05-01 | 郭硕鸿《电动力学》Ch2 静电场*