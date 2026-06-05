# 第五章 电磁波的辐射

> 郭硕鸿《电动力学》笔记

---

## §5.1 电磁势 — 推迟势

### 矢势和标势

从 Maxwell 方程组出发：

$$
\begin{aligned}
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu_0 \mathbf{J} + \mu_0\varepsilon_0\frac{\partial \mathbf{E}}{\partial t} \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \cdot \mathbf{E} &= \rho / \varepsilon_0
\end{aligned}
$$

由 $\nabla \cdot \mathbf{B} = 0$ 引入矢势 $\mathbf{A}$：

$$
\mathbf{B} = \nabla \times \mathbf{A}
$$

代入 Faraday 定律：

$$
\nabla \times \mathbf{E} = -\frac{\partial}{\partial t}(\nabla \times \mathbf{A})
\Rightarrow \nabla \times \left( \mathbf{E} + \frac{\partial \mathbf{A}}{\partial t} \right) = 0
$$

引入标势 $\varphi$：

$$
\mathbf{E} + \frac{\partial \mathbf{A}}{\partial t} = -\nabla \varphi
$$

因此：

$$
\boxed{\mathbf{E} = -\nabla \varphi - \frac{\partial \mathbf{A}}{\partial t}}, \quad
\boxed{\mathbf{B} = \nabla \times \mathbf{A}}
$$

### 规范变换与 Lorenz 规范

电磁势存在规范自由度：

$$
\begin{aligned}
\mathbf{A}' &= \mathbf{A} + \nabla \psi \\
\varphi' &= \varphi - \frac{\partial \psi}{\partial t}
\end{aligned}
$$

**— Lorenz 规范条件：**

$$
\nabla \cdot \mathbf{A} + \frac{1}{c^2}\frac{\partial \varphi}{\partial t} = 0
$$

在此规范下，电磁势满足 d'Alembert 方程（非齐次波动方程）：

$$
\boxed{\nabla^2 \mathbf{A} - \frac{1}{c^2}\frac{\partial^2 \mathbf{A}}{\partial t^2} = -\mu_0 \mathbf{J}}
$$

$$
\boxed{\nabla^2 \varphi - \frac{1}{c^2}\frac{\partial^2 \varphi}{\partial t^2} = -\rho / \varepsilon_0}
$$

### 推迟势

d'Alembert 方程的格林函数解给出 **推迟势**（retarded potentials）：

$$
\boxed{\varphi(\mathbf{r}, t) = \frac{1}{4\pi \varepsilon_0} \int \frac{\rho(\mathbf{r}', t_r)}{|\mathbf{r} - \mathbf{r}'|} d^3\mathbf{r}'}
$$

$$
\boxed{\mathbf{A}(\mathbf{r}, t) = \frac{\mu_0}{4\pi} \int \frac{\mathbf{J}(\mathbf{r}', t_r)}{|\mathbf{r} - \mathbf{r}'|} d^3\mathbf{r}'}
$$

其中 **推迟时间**（retarded time）：

$$
t_r = t - \frac{|\mathbf{r} - \mathbf{r}'|}{c}
$$

物理意义：在 $t$ 时刻观测到的场是由源在更早时刻 $t_r$ 产生的。信号以有限速度 $c$ 传播，从源点到场点需要时间 $|\mathbf{r} - \mathbf{r}'|/c$。

---

## §5.2 电偶极辐射

### 辐射场的计算

考虑振荡电偶极子（时谐源），电流密度：

$$
\mathbf{J}(\mathbf{r}', t) = \mathbf{J}(\mathbf{r}') e^{-i\omega t}
$$

矢势的频域形式：

$$
\mathbf{A}(\mathbf{r}) = \frac{\mu_0}{4\pi} \int \frac{\mathbf{J}(\mathbf{r}') e^{ik|\mathbf{r} - \mathbf{r}'|}}{|\mathbf{r} - \mathbf{r}'|} d^3\mathbf{r}'
$$

其中 $k = \omega/c$。

对于小区域（$d \ll \lambda \ll r$）的源，做多极展开。第一项即 **电偶极辐射**：

偶极矩 $\mathbf{p}(t) = \mathbf{p}_0 e^{-i\omega t}$，其时间导数：

$$
\dot{\mathbf{p}} = -i\omega \mathbf{p}, \quad \ddot{\mathbf{p}} = -\omega^2 \mathbf{p}
$$

由电流连续性可证 $\mathbf{J} d^3\mathbf{r}'$ 与 $\dot{\mathbf{p}}$ 的关系。

**辐射场（远区）：**

$$
\boxed{\mathbf{A}(\mathbf{r}) = \frac{\mu_0}{4\pi} \frac{e^{ikr}}{r} (-i\omega \mathbf{p}_0)}
$$

$$
\boxed{\mathbf{B} = \nabla \times \mathbf{A} = \frac{\mu_0 c k^2}{4\pi} \frac{e^{ikr}}{r} (\mathbf{e}_r \times \mathbf{p}_0)}
$$

$$
\boxed{\mathbf{E} = c\mathbf{B} \times \mathbf{e}_r = \frac{1}{4\pi \varepsilon_0} k^2 \frac{e^{ikr}}{r} (\mathbf{e}_r \times \mathbf{p}_0) \times \mathbf{e}_r}
$$

在球坐标系中，设 $\mathbf{p}_0$ 沿 $z$ 轴（$\theta = 0$ 方向）：

$$
\begin{aligned}
B_\phi &= -\frac{\mu_0 c k^2}{4\pi} p_0 \frac{e^{ikr}}{r} \sin\theta \\
E_\theta &= \frac{1}{4\pi \varepsilon_0} k^2 p_0 \frac{e^{ikr}}{r} \sin\theta
\end{aligned}
$$

特点：
- 横波（TEM 波）：$\mathbf{E} \perp \mathbf{B} \perp \mathbf{e}_r$
- 振幅 ∝ $\sin\theta$ — 在赤道面最大，极轴方向为零
- 振幅 ∝ $1/r$（辐射场），而非静电场 ∝ $1/r^3$

### 辐射功率与 Larmor 公式

时间平均能流密度（Poynting 矢量）：

$$
\langle \mathbf{S} \rangle = \frac{1}{2\mu_0} \text{Re}(\mathbf{E} \times \mathbf{B}^*)
$$

对球面积分得 **总辐射功率**：

$$
\boxed{P = \frac{\mu_0 p_0^2 \omega^4}{12\pi c} = \frac{p_0^2 \omega^4}{12\pi \varepsilon_0 c^3}}
$$

即 **Larmor 公式**（电偶极辐射形式）。

对于瞬时偶极矩 $\mathbf{p}(t)$，更一般的形式：

$$
\boxed{P = \frac{\mu_0}{6\pi c} |\ddot{\mathbf{p}}|^2 = \frac{|\ddot{\mathbf{p}}|^2}{6\pi \varepsilon_0 c^3}}
$$

### 方向图

辐射强度随角度的分布（归一化）：

$$
\frac{dP}{d\Omega} \propto \sin^2\theta
$$

方向图呈甜甜圈形（torus pattern）：
- 赤道面 (θ=π/2)：辐射最强
- 极轴 (θ=0,π)：辐射为零

---

## §5.3 磁偶极和电四极辐射

### 多极展开的一般框架

在小源近似（$d \ll \lambda$）下，推迟势相位因子 $e^{ik|\mathbf{r} - \mathbf{r}'|}$ 可展开：

$$
e^{ik|\mathbf{r} - \mathbf{r}'|} = e^{ikr} e^{-ik \mathbf{r}' \cdot \mathbf{e}_r} = e^{ikr} \sum_{n=0}^\infty \frac{(-ik)^n}{n!} (\mathbf{r}' \cdot \mathbf{e}_r)^n
$$

代入矢势积分：

$$
\mathbf{A}(\mathbf{r}) = \frac{\mu_0}{4\pi} \frac{e^{ikr}}{r} \sum_{n=0}^\infty \frac{(-ik)^n}{n!} \int \mathbf{J}(\mathbf{r}') (\mathbf{r}' \cdot \mathbf{e}_r)^n d^3\mathbf{r}'
$$

- $n=0$：电偶极项
- $n=1$：磁偶极 + 电四极项
- 高阶：磁四极、电八极等

### 磁偶极辐射

磁偶极矩定义为：

$$
\mathbf{m} = \frac{1}{2} \int \mathbf{r}' \times \mathbf{J}(\mathbf{r}') d^3\mathbf{r}'
$$

磁偶极辐射的矢势：

$$
\mathbf{A}(\mathbf{r}) = \frac{\mu_0}{4\pi} \frac{e^{ikr}}{r} (ik)(\mathbf{m} \times \mathbf{e}_r)
$$

辐射场：

$$
\mathbf{B} = \frac{\mu_0 k^2}{4\pi} \frac{e^{ikr}}{r} (\mathbf{e}_r \times \mathbf{m}) \times \mathbf{e}_r, \quad
\mathbf{E} = c \mathbf{B} \times \mathbf{e}_r
$$

**特点：**
- 辐射场结构形式上与电偶极辐射的对偶（$\mathbf{E} \leftrightarrow \mathbf{B}$ 互换，$\mathbf{p} \leftrightarrow \mathbf{m}/c$）
- 方向图也是 $\sin^2\theta$

**辐射功率：**

$$
\boxed{P_m = \frac{\mu_0 m_0^2 \omega^4}{12\pi c^3}}
$$

### 电四极辐射

电四极矩张量：

$$
D_{\alpha\beta} = \int (3x_\alpha' x_\beta' - r'^2 \delta_{\alpha\beta}) \rho(\mathbf{r}') d^3\mathbf{r}'
$$

电四极辐射的矢势需要从 $n=1$ 展开中分离出对称无迹部分。

辐射场的空间分布更复杂，方向图不是简单的 $\sin^2\theta$。

**辐射功率估算：**
- 电偶极辐射 ~ $(kd)^2$ 量级
- 磁偶极与电四极辐射 ~ $(kd)^4$ 量级（对同样尺度的系统小很多）

**对比：**

| 项 | 相对大小 | 方向图 |
|---|---|---|
| 电偶极 (E1) | 1 | $\sin^2\theta$ |
| 磁偶极 (M1) | $\sim (d/\lambda)^2$ | $\sin^2\theta$ |
| 电四极 (E2) | $\sim (d/\lambda)^2$ | 复杂（四瓣） |

---

## §5.4 天线辐射

### 基本天线理论

天线最基本模型：**中心馈电直线天线**（偶极天线）。

沿 $z$ 轴的线电流：

$$
\mathbf{I}(z,t) = I_0 \sin[k(L/2 - |z|)] e^{-i\omega t} \mathbf{e}_z
$$

其中 $L$ 为天线长度，端电流为零。

矢势：

$$
A_z(\mathbf{r}) = \frac{\mu_0}{4\pi} \int_{-L/2}^{L/2} \frac{I(z') e^{ik|\mathbf{r} - z'\mathbf{e}_z|}}{|\mathbf{r} - z'\mathbf{e}_z|} dz'
$$

### 半波天线 ($L = \lambda/2$)

电流分布：$I(z) = I_0 \cos(kz)$，$|z| \leq \lambda/4$

远区辐射场：

$$
E_\theta = \frac{60 I_0}{r} \frac{\cos(\frac{\pi}{2}\cos\theta)}{\sin\theta} e^{i(kr - \omega t)}
$$

方向图函数（归一化）：

$$
F(\theta) = \frac{\cos(\frac{\pi}{2}\cos\theta)}{\sin\theta}
$$

**特点：**
- 比电偶极子（$\sin\theta$）更有方向性
- 半功率波束宽度约为 $78^\circ$
- 辐射电阻约 $73\;\Omega$

### 天线阵

通过多个天线单元的相干叠加实现方向性增强和波束控制。

方向图乘积定理：

$$
F_{\text{array}}(\theta, \phi) = F_{\text{element}}(\theta, \phi) \cdot F_{\text{AF}}(\theta, \phi)
$$

阵列因子（等间距 $d$，等幅，线性相位递进）：

$$
F_{\text{AF}}(\theta) = \frac{\sin(N\psi/2)}{N\sin(\psi/2)}, \quad \psi = kd\cos\theta + \alpha
$$

其中 $\alpha$ 为相邻单元间的相位差（馈电相位递进）。

---

## 要点总结

1. **推迟势**是电磁辐射理论的基础：场由源的"过去"（推迟时间）决定
2. **Lorenz 规范**下的 d'Alembert 方程将 Maxwell 方程组简化为两个解耦的波动方程
3. **电偶极辐射**是最基本的辐射模式，Larmor 公式 $P \propto \ddot{p}^2$ 是核心结果
4. **方向图**：电偶极辐射的 $\sin^2\theta$ 结构决定了甜甜圈形分布
5. **多极展开**：对于小源，辐射按 $(d/\lambda)^n$ 分级，偶极项占主导
6. **天线理论**建立在实际电流分布的基础上，通过阵列实现波束赋形
