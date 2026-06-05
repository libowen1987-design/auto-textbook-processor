# 郭硕鸿《电动力学》第六章 — 狭义相对论

> **范围**: §6.1 相对论的实验基础 — Michelson-Morley, Lorentz变换
> §6.2 相对论的时空理论 — 四维时空, 间隔, 因果律
> §6.3 相对论电动力学 — 四维势, 场张量, 协变Maxwell方程
> §6.4 相对论力学 — 四维动量, 质能关系

---

## §6.1 相对论的实验基础

### 历史的矛盾

**经典电磁学（Maxwell方程组）** 预言真空中光速 $c = 1/\sqrt{\mu_0 \varepsilon_0}$，是一个**普适常数**。

- 若存在"以太"（绝对参考系），光速应随观测者运动而变化
- Maxwell方程在 Galilean 变换下**不协变**

**Michelson-Morley 实验（1887）**：
- 用干涉仪测量地球在"以太"中的绝对运动
- 结果：**零结果** — 光速各向同性，不存在可探测的以太风
- 推翻了以太假说

### Einstein 的两条基本假设（1905）

1. **相对性原理**：所有惯性系中，物理定律形式相同
2. **光速不变原理**：真空中光速在各惯性系均为 $c$，与光源运动无关

### Lorentz 变换

设 $S'$ 系沿 $S$ 系的 $x$ 轴以速度 $v$ 运动，两系原点在 $t=t'=0$ 重合：

$$
\boxed{
\begin{aligned}
x' &= \gamma (x - vt) \\
y' &= y \\
z' &= z \\
t' &= \gamma \left(t - \frac{v}{c^2}x\right)
\end{aligned}
}
\qquad
\boxed{
\begin{aligned}
x &= \gamma (x' + vt') \\
y &= y' \\
z &= z' \\
t &= \gamma \left(t' + \frac{v}{c^2}x'\right)
\end{aligned}
}
$$

其中 **Lorentz 因子**：

$$
\gamma = \frac{1}{\sqrt{1 - v^2/c^2}} = \frac{1}{\sqrt{1 - \beta^2}}, \quad \beta = \frac{v}{c}
$$

- $\gamma \ge 1$，当 $v \ll c$ 时 $\gamma \approx 1$，退化为 Galilean 变换
- 速度极限：$|v| < c$（否则 $\gamma$ 为虚数，物理上无意义）

### 矩阵形式

$$
\begin{pmatrix} ct' \\ x' \\ y' \\ z' \end{pmatrix}
= \begin{pmatrix}
\gamma & -\gamma\beta & 0 & 0 \\
-\gamma\beta & \gamma & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}
\begin{pmatrix} ct \\ x \\ y \\ z \end{pmatrix}
$$

记变换矩阵为 $\Lambda^\mu_{\;\nu}$，则 $x'^\mu = \Lambda^\mu_{\;\nu} x^\nu$。

---

## §6.2 相对论的时空理论

### 四维时空（Minkowski 空间）

**四维坐标**: $x^\mu = (ct, x, y, z)$，$\mu = 0,1,2,3$

**度规张量**（号差 $+---$ 或 $-+++$，本笔记采用 $+---$）：

$$
\eta_{\mu\nu} = \eta^{\mu\nu} = \mathrm{diag}(1, -1, -1, -1)
$$

**线元/间隔**（Lorentz 不变量）：

$$
ds^2 = \eta_{\mu\nu} dx^\mu dx^\nu = c^2 dt^2 - dx^2 - dy^2 - dz^2
$$

### 间隔的分类（因果结构）

对于两个事件 $P_1$ 和 $P_2$，间隔 $\Delta s^2$ 不依赖于参考系：

| 类型 | $\Delta s^2$ | 物理意义 |
|------|-------------|---------|
| **类光** | $=0$ | 光信号连接 |
| **类时** | $>0$ | 存在因果联系的可能，时间序为绝对 |
| **类空** | $<0$ | 无因果联系，同时性是相对的 |

### 因果律

- 类时间隔的事件：时序是绝对的（因果关系不受 Lorentz 变换影响）
- 类空间隔的事件：可以通过选择参考系反转时间顺序，但**不可传递因果信号**（否则超光速，违反因果律）
- **光锥结构**：未来光锥、过去光锥、类光锥面
  - 只有光锥内部（类时）的事件才能与原点有因果联系

### 重要的相对论效应

**同时性的相对性**：
- $S$ 系中同时（$\Delta t = 0$）但不同地点（$\Delta x \ne 0$）的事件，在 $S'$ 系中不同时：
  $$\Delta t' = -\gamma \frac{v}{c^2} \Delta x$$

**长度收缩**（尺缩）：
- 测量运动杆的长度 → 两端必须同时测量
- $L = L_0 / \gamma$，其中 $L_0$ 为固有长度
- 运动方向的长度收缩，垂直于运动方向长度不变

**时间膨胀**（钟慢）：
- 运动时钟变慢：$\Delta t = \gamma \Delta \tau$
- $\Delta \tau$ 为固有时间（同一地点测量的时间间隔）
- 双生子佯谬：对称破缺来自加速过程（非惯性系）

**速度变换公式**：
$$
u_x' = \frac{u_x - v}{1 - \frac{v u_x}{c^2}}, \quad
u_y' = \frac{u_y}{\gamma\left(1 - \frac{v u_x}{c^2}\right)}, \quad
u_z' = \frac{u_z}{\gamma\left(1 - \frac{v u_x}{c^2}\right)}
$$

---

## §6.3 相对论电动力学

### 四维电流密度

电荷是 Lorentz 标量（不变量）：

$$
\rho_0 = \text{固有电荷密度}, \quad \rho = \gamma \rho_0
$$

**四维电流密度**：

$$
J^\mu = (c\rho, \mathbf{J}) = \rho_0 U^\mu
$$

其中 $U^\mu = \gamma (c, \mathbf{u})$ 为四维速度。

**电荷守恒定律**（连续性方程）的四维形式：

$$
\partial_\mu J^\mu = 0
$$

### 四维势

- 在 Coulomb 规范下，电磁势的波动方程可写成 Lorentz 规范形式
- **Lorentz 规范条件**：$\partial_\mu A^\mu = 0$
- **四维势**：
  $$A^\mu = \left(\frac{\varphi}{c}, \mathbf{A}\right)$$
  其中 $\varphi$ 为标势，$\mathbf{A}$ 为矢势

**达朗贝尔方程的四维形式**：

$$
\Box A^\mu = \mu_0 J^\mu
$$

其中 $\Box = \partial^\mu \partial_\mu = \frac{1}{c^2}\frac{\partial^2}{\partial t^2} - \nabla^2$ 为 d'Alembert 算符。

### 电磁场张量

定义 **Faraday 张量**（电磁场张量）：

$$
F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu = \begin{pmatrix}
0 & -E_x/c & -E_y/c & -E_z/c \\
E_x/c & 0 & -B_z & B_y \\
E_y/c & B_z & 0 & -B_x \\
E_z/c & -B_y & B_x & 0
\end{pmatrix}
$$

**对偶张量**：

$$
\tilde{F}^{\mu\nu} = \frac{1}{2}\varepsilon^{\mu\nu\rho\sigma}F_{\rho\sigma}
= \begin{pmatrix}
0 & -B_x & -B_y & -B_z \\
B_x & 0 & E_z/c & -E_y/c \\
B_y & -E_z/c & 0 & E_x/c \\
B_z & E_y/c & -E_x/c & 0
\end{pmatrix}
$$

其中 $\varepsilon^{\mu\nu\rho\sigma}$ 为四维 Levi-Civita 符号（$\varepsilon^{0123}=1$）。

### 协变 Maxwell 方程组

两组方程统一为两个四维张量方程：

1. **非齐次方程**（含源）：
   $$\partial_\mu F^{\mu\nu} = \mu_0 J^\nu$$
   展开即为 Gauss 定律 + Ampère-Maxwell 定律

2. **齐次方程**（无源/对偶）：
   $$\partial_\mu \tilde{F}^{\mu\nu} = 0$$
   展开即为 $\nabla \cdot \mathbf{B} = 0$ + Faraday 电磁感应定律

### 电磁场的变换

场张量的 Lorentz 变换：$F'^{\mu\nu} = \Lambda^\mu_{\;\alpha} \Lambda^\nu_{\;\beta} F^{\alpha\beta}$

对于沿 $x$ 轴以速度 $v$ 运动的参考系：

$$
\boxed{
\begin{aligned}
E'_x &= E_x \\
E'_y &= \gamma (E_y - v B_z) \\
E'_z &= \gamma (E_z + v B_y)
\end{aligned}
}
\qquad
\boxed{
\begin{aligned}
B'_x &= B_x \\
B'_y &= \gamma (B_y + \frac{v}{c^2} E_z) \\
B'_z &= \gamma (B_z - \frac{v}{c^2} E_y)
\end{aligned}
}
$$

**重要认识**：电场和磁场不是独立的实体，而是电磁场张量在不同惯性系中的不同投影。

**不变量**：
- $E \cdot B$ 是 Lorentz 标量
- $E^2 - c^2 B^2$ 是 Lorentz 标量

**运动电荷的场**：
- 以匀速 $v$ 运动的点电荷 $q$，在空间点 $(x,y,z)$ 产生的电磁场可由 Coulomb 场经 Lorentz 变换得到
- 电场不再球对称，在运动方向被压缩（类似尺缩效应）
- 磁场 $\mathbf{B} = \frac{\mathbf{v}}{c^2} \times \mathbf{E}$（非相对论近似 $v \ll c$）

### Liénard-Wiechert 势的四维形式

对于运动的点电荷，推迟势可写成四维形式：

$$
A^\mu(x) = \frac{\mu_0 q}{4\pi} \frac{U^\mu}{U \cdot (x - x_q)}
$$

其中 $x_q$ 为电荷的世界线，$U^\mu$ 为四维速度，分母为四维点乘。

---

## §6.4 相对论力学

### 四维速度

$$
U^\mu = \frac{dx^\mu}{d\tau} = \gamma (c, \mathbf{u}), \quad
\gamma = \frac{1}{\sqrt{1-u^2/c^2}}
$$

固有时间 $d\tau = \sqrt{1-u^2/c^2}\, dt = dt/\gamma$ 是 Lorentz 标量。

$U^\mu U_\mu = c^2$（恒等于 $c^2$）。

### 四维动量

$$
p^\mu = m_0 U^\mu = \left(\frac{E}{c}, \mathbf{p}\right)
$$

- $m_0$ 为静质量（Lorentz 标量）
- 三维动量：$\mathbf{p} = \gamma m_0 \mathbf{u}$
- 能量：$E = \gamma m_0 c^2$

**质能关系**（最重要的公式之一）：

$$
\boxed{E = mc^2}
$$

其中 $m = \gamma m_0$ 为相对论质量（或运动质量）。

**静能**：$E_0 = m_0 c^2$ — 即使静止的物体也有巨大的内能

**动能**：$T = E - E_0 = (\gamma - 1) m_0 c^2$

对 $v \ll c$ 展开：

$$
T = \frac{1}{2} m_0 v^2 + \frac{3}{8} m_0 \frac{v^4}{c^2} + \cdots
$$

恢复经典动能 $\frac12 m_0 v^2$ 为首项。

**能量-动量关系**：

$$
\boxed{E^2 = p^2 c^2 + m_0^2 c^4}
$$

- 光子：$m_0 = 0$，$E = pc$

### 四维力（Minkowski 力）

$$
K^\mu = \frac{dp^\mu}{d\tau} = m_0 \frac{d^2 x^\mu}{d\tau^2}
$$

四维力与三维力的关系：
$$
K^\mu = \gamma \left(\frac{\mathbf{F} \cdot \mathbf{u}}{c}, \mathbf{F}\right)
$$

**四维力恒垂直于四维速度**：$K^\mu U_\mu = 0$

### 相对论运动方程

$$
\frac{d\mathbf{p}}{dt} = \frac{d}{dt}(\gamma m_0 \mathbf{u}) = \mathbf{F}
$$

力的变换：
$$
\begin{aligned}
F_x' &= F_x \\
F_y' &= \frac{F_y}{\gamma(1 - v u_x / c^2)} \\
F_z' &= \frac{F_z}{\gamma(1 - v u_x / c^2)}
\end{aligned}
$$

### 质能等价的应用

- 核裂变（$^{235}\mathrm{U}$）：质量亏损 $\to$ 能量释放
- 核聚变（氢 $\to$ 氦）：太阳的能量来源
- 粒子物理中：$e^+ + e^- \to \gamma + \gamma$（湮灭）
- $\gamma \to e^+ + e^-$（对生成）

---

## 关键公式总结

| 物理量 | 经典形式 | 相对论四维形式 |
|--------|---------|--------------|
| 坐标 | $(t, \mathbf{x})$ | $x^\mu = (ct, \mathbf{x})$ |
| 速度 | $\mathbf{u}$ | $U^\mu = \gamma(c, \mathbf{u})$ |
| 动量 | $m_0\mathbf{u}$ | $p^\mu = (E/c, \mathbf{p})$ |
| 力 | $\mathbf{F}$ | $K^\mu = \gamma(\mathbf{F}\cdot\mathbf{u}/c, \mathbf{F})$ |
| 电流 | $(\rho, \mathbf{J})$ | $J^\mu = (c\rho, \mathbf{J})$ |
| 势 | $(\varphi, \mathbf{A})$ | $A^\mu = (\varphi/c, \mathbf{A})$ |
| d'Alembert | $\nabla^2 - \partial_t^2/c^2$ | $\Box = \partial^\mu \partial_\mu$ |
| 场 | $\mathbf{E}, \mathbf{B}$ | $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$ |
| 连续方程 | $\partial_t\rho + \nabla\cdot\mathbf{J} = 0$ | $\partial_\mu J^\mu = 0$ |
| Lorentz条件 | $\frac1{c^2}\partial_t\varphi + \nabla\cdot\mathbf{A} = 0$ | $\partial_\mu A^\mu = 0$ |

---

## 参考

- 郭硕鸿，《电动力学》（第三版），高等教育出版社，第6章
- 张宗燧，《电动力学及狭义相对论》
- Landau & Lifshitz, *The Classical Theory of Fields*
- Jackson, *Classical Electrodynamics*, 3rd ed., Ch 11-12
