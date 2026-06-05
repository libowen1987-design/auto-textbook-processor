# 郭硕鸿《电动力学》 第01章：电磁学基本定律

> **来源：** 谢处方等，《电磁场与电磁波》，第01章
> **提取方式：** 📷 扫描PDF → OCR → 人工清洗

---

## 01.1 电磁学基本定律 | Fundamental Laws of Electrodynamics

# 第1章 电磁现象的普遍规律
 郭硕鸿电动力学第3版高教社  7-04-023924-82008
---
## §1.1 电荷和电场
### 库仑定律
真空中静止点电荷 $Q$ 对另一静止点电荷 $q$ 的作用力：
$$
\vec{F} = \frac{1}{4$\pi$\varepsilon_0} \frac{Qq}{r^2} \hat{\vec{r}}
$$
其中 $\varepsilon_0 \approx 8.854 \times 10^{-12}\,\text{$\mathbf{F}$/m}$ 为真空介电常数。
### 电场强度
电场定义为试探电荷所受的每单位电荷的力：
$$
\vec{E}(\vec{r}) = \frac{\vec{F}}{q}
$$
连续电荷分布产生的电场（库仑叠加原理）：
$$
\boxed{\vec{E}(\vec{r}) = \frac{1}{4$\pi$\varepsilon_0} \int \frac{$\rho$(\vec{r}')(\vec{r} - \vec{r}')}{|\vec{r} - \vec{r}'|^3} \,\mathrm{d}V'}
$$
### 高斯定理与散度方程
**积分形式：**
$$
\oint_$\mathbf{S}$ \vec{E} \cdot \mathrm{d}\vec{S} = \frac{Q}{\varepsilon_0}
$$
**微分形式：（静电场的有源无旋性）**
$$
\boxed{\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0}}
$$
$$
\boxed{\nabla \times \vec{E} = 0}
$$
静电场的旋度为零 \rightarrow 电场为保守场，可引入标势 $\phi$：
$$
\vec{E} = -\nabla \phi
$$
---
## §1.2 电流和磁场
### 电荷守恒定律
电流密度 $\vec{J}$ 与电荷密度 $\rho$ 的关系（连续性方程）：
$$
\boxed{\nabla \cdot \vec{J} + \frac{\partial \rho}{\partial t} = 0}
$$
**积分形式：**
$$
\oint_$\mathbf{S}$ \vec{J} \cdot \mathrm{d}\vec{S} = -\frac{\mathrm{d}Q}{\mathrm{d}t}
$$
### 毕奥-萨伐尔定律
电流元 $\vec{I}\mathrm{d}\vec{l}$ 在空间某点产生的磁场：
$$
\mathrm{d}\vec{B} = \frac{\mu_0}{4\pi} \frac{I\,\mathrm{d}\vec{l} \times \hat{\vec{r}}}{r^2}
$$
体电流分布：
$$
\boxed{\vec{B}(\vec{r}) = \frac{\mu_0}{4\pi} \int \frac{\vec{J}(\vec{r}') \times (\vec{r} - \vec{r}')}{|\vec{r} - \vec{r}'|^3} \,\mathrm{d}V'}
$$
$\mu_0 = 4\pi \times 10^{-7}\,\text{N/A}^2$ 为真空磁导率。
### 磁场的散度与旋度
**无源性（磁单极不存在）：**
$$
\boxed{\nabla \cdot \vec{B} = 0}
$$
\rightarrow 可引入矢量势 $\vec{A}$：
$$
\vec{B} = \nabla \times \vec{A}
$$
**安培定律（静磁场）：**
$$
\boxed{\nabla \times \vec{B} = \mu_0 \vec{J}}
$$
**积分形式：**
$$
\oint_C \vec{B} \cdot \mathrm{d}\vec{l} = \mu_0 I
$$
---
## §1.3 麦克斯韦方程组
### 法拉第电磁感应定律
感应电动势等于磁通量变化率的负值：
**积分形式：**
$$
\oint_C \vec{E} \cdot \mathrm{d}\vec{l} = -\frac{\mathrm{d}}{\mathrm{d}t} \int_$\mathbf{S}$ \vec{B} \cdot \mathrm{d}\vec{S}
$$
**微分形式：**
$$
\boxed{\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}}
$$
### 位移电流
麦克斯韦发现安培定律在非稳恒情况下的矛盾，引入**位移电流密度**：
$$
\vec{J}_d = \varepsilon_0 \frac{\partial \vec{E}}{\partial t}
$$
修正后的安培定律：
$$
\boxed{\nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0\varepsilon_0 \frac{\partial \vec{E}}{\partial t}}
$$
### 麦克斯韦方程组（真空中）
**微分形式：**
$$
\begin{aligned}
\nabla \cdot \vec{E} &= \frac{\rho}{\varepsilon_0} \quad &\text{(高斯定理)} \\
\nabla \cdot \vec{B} &= 0 \quad &\text{(磁通连续性)} \\
\nabla \times \vec{E} &= -\frac{\partial \vec{B}}{\partial t} \quad &\text{(法拉第定律)} \\
\nabla \times \vec{B} &= \mu_0\vec{J} + \mu_0\varepsilon_0\frac{\partial \vec{E}}{\partial t} \quad &\text{(安培-麦克斯韦定律)}
\end{aligned}
$$
### 洛伦兹力公式
运动电荷在电磁场中受力：
$$
\boxed{\vec{F} = q(\vec{E} + \vec{v} \times \vec{B})}
$$
电荷分布所受的力密度：
$$
\vec{f} = $\rho$\vec{E} + \vec{J} \times \vec{B}
$$
---
## §1.4 介质中的电磁性质
### 极化强度与电位移矢量
电极化强度 $\vec{P}$：
$$
\vec{P} = \lim_{\Delta V \to 0} \frac{\sum \vec{p}}{\Delta V}
$$
极化电荷密度：
$$
\rho_p = -\nabla \cdot \vec{P}, \quad \sigma_p = \vec{P} \cdot \hat{\vec{n}}
$$
**电位移矢量：**
$$
\boxed{\vec{D} = \varepsilon_0 \vec{E} + \vec{P}}
$$
介质中高斯定理：
$$
\boxed{\nabla \cdot \vec{D} = \rho_f}
$$
其中 $\rho_f$ 为自由电荷密度。
### 磁化强度与磁场强度
磁化强度 $\vec{M}$：
$$
\vec{M} = \lim_{\Delta V \to 0} \frac{\sum \vec{m}}{\Delta V}
$$
磁化电流密度：
$$
\vec{J}_m = \nabla \times \vec{M}, \quad \vec{K}_m = \vec{M} \times \hat{\vec{n}}
$$
**磁场强度：**
$$
\boxed{\vec{H} = \frac{\vec{B}}{\mu_0} - \vec{M}}
$$
介质中安培定律：
$$
\boxed{\nabla \times \vec{H} = \vec{J}_f + \frac{\partial \vec{D}}{\partial t}}
$$
### 本构关系
各向同性线性介质：
$$
\vec{P} = \varepsilon_0 \chi_e \vec{E}, \quad \vec{D} = \varepsilon \vec{E} = \varepsilon_0 \varepsilon_r \vec{E}
$$
$$
\vec{M} = \chi_m \vec{H}, \quad \vec{B} = \mu \vec{H} = \mu_0 \mu_r \vec{H}
$$
其中 $\varepsilon_r = 1 + \chi_e$ 为相对介电常数，$\mu_r = 1 + \chi_m$ 为相对磁导率。
### 边值关系
| 物理量 | 边界条件 |
|--------|----------|
| $\vec{D}$ | $(\vec{D}_2 - \vec{D}_1) \cdot \hat{\vec{n}} = \sigma_f$ |
| $\vec{B}$ | $(\vec{B}_2 - \vec{B}_1) \cdot \hat{\vec{n}} = 0$ |
| $\vec{E}$ | $\hat{\vec{n}} \times (\vec{E}_2 - \vec{E}_1) = 0$ |
| $\vec{H}$ | $\hat{\vec{n}} \times (\vec{H}_2 - \vec{H}_1) = \vec{K}_f$ |
---
## §1.5 电磁场的能量
### 能量守恒定律与坡印廷矢量
电磁场对电荷做功的功率密度：
$$
\vec{J} \cdot \vec{E} = -\frac{\partial}{\partial t}\left(\frac{1}{2}\varepsilon_0 $\mathbf{E}$^2 + \frac{1}{2}\frac{$\mathbf{B}$^2}{\mu_0}\right) - \nabla \cdot (\vec{E} \times \vec{H})
$$
**坡印廷矢量（能流密度）：**
$$
\boxed{\vec{S} = \vec{E} \times \vec{H}}
$$
方向为电磁能量传播方向，大小为单位时间通过单位面积的能量。
**电磁场能量密度：**
$$
\boxed{w = \frac{1}{2}(\vec{E} \cdot \vec{D} + \vec{B} \cdot \vec{H})}
$$
真空中：
$$
w = \frac{1}{2}\varepsilon_0 $\mathbf{E}$^2 + \frac{1}{2}\frac{$\mathbf{B}$^2}{\mu_0}
$$
### 能量守恒的微分形式（坡印廷定理）
$$
\boxed{-\frac{\partial w}{\partial t} = \nabla \cdot \vec{S} + \vec{J} \cdot \vec{E}}
$$
**物理意义：** 单位体积内电磁场能量的减少率 = 单位时间流出体积的电磁能量 + 场对电荷做功的功率。
### 积分形式
$$
-\frac{\mathrm{d}}{\mathrm{d}t} \int_V w \,\mathrm{d}V = \oint_$\mathbf{S}$ \vec{S} \cdot \mathrm{d}\vec{S} + \int_V \vec{J} \cdot \vec{E} \,\mathrm{d}V
$$
---
## 本章关键公式速查
| 公式 | 名称 |
|------|------|
| $\nabla \cdot \vec{E} = \rho / \varepsilon_0$ | 高斯定理（电场散度） |
| $\nabla \times \vec{E} = -\partial\vec{B}/\partial t$ | 法拉第定律 |
| $\nabla \cdot \vec{B} = 0$ | 磁通连续性 |
| $\nabla \times \vec{B} = \mu_0\vec{J} + \mu_0\varepsilon_0 \partial\vec{E}/\partial t$ | 安培-麦克斯韦定律 |
| $\nabla \cdot \vec{D} = \rho_f$ | 介质中高斯定理 |
| $\nabla \times \vec{H} = \vec{J}_f + \partial\vec{D}/\partial t$ | 介质中安培定律 |
| $\vec{S} = \vec{E} \times \vec{H}$ | 坡印廷矢量 |
| $w = \frac{1}{2}(\vec{E}\cdot\vec{D} + \vec{B}\cdot\vec{H})$ | 电磁场能量密度 |